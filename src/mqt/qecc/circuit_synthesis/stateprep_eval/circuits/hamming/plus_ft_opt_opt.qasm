OPENQASM 2.0;
include "qelib1.inc";
qreg q[15];
qreg x_anc[2];
creg x_c[2];
h q[2];
h q[3];
h q[4];
h q[5];
h q[6];
h q[7];
h q[8];
h q[9];
h q[10];
h q[13];
h q[14];
cx q[10],q[0];
cx q[0],q[1];
cx q[7],q[1];
cx q[3],q[12];
cx q[6],q[10];
cx q[8],q[1];
cx q[4],q[11];
cx q[11],q[3];
cx q[13],q[11];
cx q[9],q[8];
cx q[14],q[0];
cx q[10],q[12];
cx q[3],q[1];
cx q[5],q[6];
cx q[0],q[11];
cx q[6],q[0];
cx q[7],q[0];
cx q[1],q[10];
cx q[11],q[1];
cx q[9],q[4];
cx q[2],q[4];
cx q[4],q[5];
h x_anc[0];
cx x_anc[0],q[0];
cx x_anc[0],q[9];
cx x_anc[0],q[10];
h x_anc[0];
measure x_anc[0] -> x_c[0];
h x_anc[1];
cx x_anc[1],q[4];
cx x_anc[1],q[8];
cx x_anc[1],q[11];
h x_anc[1];
measure x_anc[1] -> x_c[1];
