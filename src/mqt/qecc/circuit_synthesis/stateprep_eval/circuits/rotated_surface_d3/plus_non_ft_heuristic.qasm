OPENQASM 2.0;
include "qelib1.inc";
qreg q[9];
h q[2];
h q[4];
h q[5];
h q[6];
h q[7];
cx q[7],q[3];
cx q[5],q[1];
cx q[4],q[3];
cx q[2],q[1];
cx q[7],q[8];
cx q[6],q[3];
cx q[4],q[2];
cx q[1],q[0];
