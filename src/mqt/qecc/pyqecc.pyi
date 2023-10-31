from typing import Any, ClassVar, overload

class Code:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: str) -> None: ...
    @overload
    def __init__(self, arg0: list[list[bool]]) -> None: ...
    @overload
    def __init__(self, arg0: list[list[bool]], arg1: list[list[bool]]) -> None: ...
    def get_hx(self) -> list[list[bool]]: ...
    def get_hz(self) -> list[list[bool]]: ...
    def get_syndrome(self, arg0: list[bool], arg1: list[bool]) -> list[bool]: ...
    def get_x_syndrome(self, arg0: list[bool]) -> list[bool]: ...
    @overload
    def is_stabilizer(self, arg0: list[bool]) -> bool: ...
    @overload
    def is_stabilizer(self, arg0: list[bool], arg1: list[bool]) -> bool: ...
    def is_x_stabilizer(self, arg0: list[bool]) -> bool: ...
    def json(self) -> dict[str, Any]: ...
    def set_hx(self, arg0: list[list[bool]]) -> None: ...
    def set_hz(self, arg0: list[list[bool]]) -> None: ...

    d: int
    k: int
    n: int

class Decoder:
    def __init__(self) -> None: ...
    def decode(self, arg0: list[bool]) -> None: ...
    def set_code(self, arg0: Code) -> None: ...
    def set_growth(self, arg0: GrowthVariant) -> None: ...

    growth: GrowthVariant
    result: DecodingResult

class DecoderType:
    __members__: ClassVar[dict[DecoderType, int]] = ...  # read-only
    original_uf: ClassVar[DecoderType] = ...
    uf_heuristic: ClassVar[DecoderType] = ...

    @overload
    def __init__(self, value: int) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: DecoderType) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ... # noqa: PLW3201
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class DecodingResult:
    def __init__(self) -> None: ...
    def json(self) -> dict[str, Any]: ...

    decoding_time: int
    estim_vec_idxs: list[int]
    estimate: list[bool]

class DecodingResultStatus:
    __members__: ClassVar[dict[DecodingResultStatus, int]] = ...  # read-only
    success: ClassVar[DecodingResultStatus] = ...
    failure: ClassVar[DecodingResultStatus] = ...

    @overload
    def __init__(self, value: int) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: DecodingResultStatus) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ... # noqa: PLW3201
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class DecodingRunInformation:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        arg0: float,
        arg1: int,
        arg2: list[bool],
        arg3: list[bool],
        arg4: DecodingResult,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg0: float,
        arg1: int,
        arg2: list[bool],
        arg3: list[bool],
        arg4: DecodingResultStatus,
        arg5: DecodingResult,
    ) -> None: ...
    def json(self) -> dict[str, Any]: ...

    code_size: int
    error: list[bool]
    physical_err_r: float
    result: DecodingResult
    status: DecodingResultStatus
    syndrome: list[bool]

class DecodingSimulator:
    def __init__(self) -> None: ...
    def simulate_avg_runtime(
        self, arg0: str, arg1: float, arg2: int, arg3: str, arg4: int, arg5: DecoderType
    ) -> None: ...
    def simulate_wer(
        self,
        arg0: str,
        arg1: float,
        arg2: float,
        arg3: int,
        arg4: Code,
        arg5: float,
        arg6: DecoderType,
    ) -> None: ...

class GrowthVariant:
    __members__: ClassVar[dict[GrowthVariant, int]] = ...  # read-only
    all_components: ClassVar[GrowthVariant] = ...
    invalid_components: ClassVar[GrowthVariant] = ...
    single_smallest: ClassVar[GrowthVariant] = ...
    single_random: ClassVar[GrowthVariant] = ...
    single_qubit_random: ClassVar[GrowthVariant] = ...

    @overload
    def __init__(self, value: int) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: GrowthVariant) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ... # noqa: PLW3201
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class UFDecoder(Decoder):
    def __init__(self) -> None: ...
    def decode(self, arg0: list[bool]) -> None: ...
    @property
    def growth(self) -> GrowthVariant: ...
    @growth.setter
    def growth(self, arg0: GrowthVariant) -> None: ...
    @property
    def result(self) -> DecodingResult: ...
    @result.setter
    def result(self, arg0: DecodingResult) -> None: ...

class UFHeuristic(Decoder):
    def __init__(self) -> None: ...
    def decode(self, arg0: list[bool]) -> None: ...
    def reset(self) -> None: ...
    @property
    def growth(self) -> GrowthVariant: ...
    @growth.setter
    def growth(self, arg0: GrowthVariant) -> None: ...
    @property
    def result(self) -> DecodingResult: ...
    @result.setter
    def result(self, arg0: DecodingResult) -> None: ...

def apply_ecc(
    circuit_name: object, ecc_name: str, ecc_frequency: int = 100
) -> dict[str, str]: ...
def sample_iid_pauli_err(arg0: int, arg1: float) -> list[bool]: ...
