OPENQASM 2.0;
include "qelib1.inc";
qreg q[9];
h q[0];
h q[2];
h q[5];
h q[6];
cx q[5],q[8];
cx q[0],q[4];
cx q[5],q[7];
cx q[0],q[3];
cx q[7],q[4];
cx q[6],q[3];
cx q[2],q[5];
cx q[0],q[1];