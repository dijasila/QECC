"""Utility functions for synthesizing circuits."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

import multiprocess
import numpy as np
from ldpc import mod2
from qiskit import QuantumCircuit

if TYPE_CHECKING:  # pragma: no cover
    from collections.abc import Callable

    import numpy.typing as npt


logger = logging.getLogger(__name__)


def run_with_timeout(func: Callable[[Any], Any], *args: Any, timeout: int = 10) -> Any | str | None:  # noqa: ANN401
    """Run a function with a timeout.

    If the function does not complete within the timeout, return None.

    Args:
        func: The function to run.
        args: The arguments to pass to the function.
        timeout: The maximum time to allow the function to run for in seconds.
    """
    manager = multiprocess.Manager()
    return_list = manager.list()
    p = multiprocess.Process(target=lambda: return_list.append(func(*args)))
    p.start()
    p.join(timeout)
    if p.is_alive():
        p.terminate()
        return "timeout"
    return return_list[0]


def iterative_search_with_timeout(
    fun: Callable[[int], QuantumCircuit],
    min_param: int,
    max_param: int,
    min_timeout: int,
    max_timeout: int,
    param_factor: float = 2,
    timeout_factor: float = 2,
) -> None | tuple[None | QuantumCircuit, int]:
    """Geometrically increases the parameter and timeout until a result is found or the maximum timeout is reached.

    Args:
        fun: function to run with increasing parameters and timeouts
        min_param: minimum parameter to start with
        max_param: maximum parameter to reach
        min_timeout: minimum timeout to start with
        max_timeout: maximum timeout to reach
        param_factor: factor to increase the parameter by at each iteration
        timeout_factor: factor to increase the timeout by at each iteration
    """
    curr_timeout = min_timeout
    curr_param = min_param
    while curr_timeout <= max_timeout:
        while curr_param <= max_param:
            logging.info(f"Running iterative search with param={curr_param} and timeout={curr_timeout}")
            res = run_with_timeout(fun, curr_param, timeout=curr_timeout)
            if res is not None and (not isinstance(res, str) or res != "timeout"):
                return res, curr_param
            if curr_param == max_param:
                break

            curr_param = int(curr_param * param_factor)
            curr_param = min(curr_param, max_param)

        curr_timeout = int(curr_timeout * timeout_factor)
        curr_param = min_param
    return None, max_param


def heuristic_gaussian_elimination(
    matrix: npt.NDArray[np.int8], parallel_elimination: bool = True
) -> tuple[npt.NDArray[np.int8], list[tuple[int, int]]]:
    """Perform Gaussian elimination on the column space of a matrix using as few eliminations as possible.

    The algorithm utilizes a greedy heuristic to select the columns to eliminate in order to minimize the number of eliminations required.

    Args:
        matrix: The matrix to perform Gaussian elimination on.
        parallel_elimination: Whether to prioritize elimination steps that act on disjoint columns.

    returns:
        The reduced matrix and a list of the elimination steps taken. The elimination steps are represented as tuples of the form (i, j) where i is the column being eliminated with and j is the column being eliminated.
    """
    matrix = matrix.copy()
    rank = mod2.rank(matrix)

    def is_reduced() -> bool:
        return bool(len(np.where(np.all(matrix == 0, axis=0))[0]) == matrix.shape[1] - rank)

    costs = np.array([
        [np.sum((matrix[:, i] + matrix[:, j]) % 2) for j in range(matrix.shape[1])] for i in range(matrix.shape[1])
    ])

    costs -= np.sum(matrix, axis=0)
    np.fill_diagonal(costs, 1)

    used_columns = []  # type: list[np.int_]
    eliminations = []  # type: list[tuple[int, int]]
    while not is_reduced():
        m = np.zeros((matrix.shape[1], matrix.shape[1]), dtype=bool)  # type: npt.NDArray[np.bool_]
        m[used_columns, :] = True
        m[:, used_columns] = True

        costs_unused = np.ma.array(costs, mask=m)  # type: ignore[no-untyped-call]
        if np.all(costs_unused >= 0) or len(used_columns) == matrix.shape[1]:  # no more reductions possible
            if used_columns == []:  # local minimum => get out by making matrix triangular
                logging.warning("Local minimum reached. Making matrix triangular.")
                matrix = mod2.reduced_row_echelon(matrix)[0]
                costs = np.array([
                    [np.sum((matrix[:, i] + matrix[:, j]) % 2) for j in range(matrix.shape[1])]
                    for i in range(matrix.shape[1])
                ])
                costs -= np.sum(matrix, axis=0)
                np.fill_diagonal(costs, 1)
            else:  # try to move onto the next layer
                used_columns = []
            continue

        i, j = np.unravel_index(np.argmin(costs_unused), costs.shape)
        eliminations.append((int(i), int(j)))

        if parallel_elimination:
            used_columns.append(i)
            used_columns.append(j)

        # update matrix
        matrix[:, j] = (matrix[:, i] + matrix[:, j]) % 2
        # update costs
        new_weights = np.sum((matrix[:, j][:, np.newaxis] + matrix) % 2, axis=0)
        costs[j, :] = new_weights - np.sum(matrix, axis=0)
        costs[:, j] = new_weights - np.sum(matrix[:, j])
        np.fill_diagonal(costs, 1)

    return matrix, eliminations


def build_css_circuit_from_list_and_checks(
    n: int, cnots: list[tuple[int, int]], hadamards: list[int]
) -> QuantumCircuit:
    """Build a quantum circuit consisting of Hadamards followed by a layer of CNOTs from a list of CNOTs and a list of checks.

    Args:
        n: Number of qubits in the circuit.
        cnots: List of CNOTs to apply. Each CNOT is a tuple of the form (control, target).
        hadamards: List of qubits to apply Hadamards to.

    Returns:
        The quantum circuit.
    """
    circ = QuantumCircuit(n)
    circ.h(hadamards)
    for i, j in cnots:
        circ.cx(i, j)
    return circ
