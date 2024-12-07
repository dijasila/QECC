OPENQASM 2.0;
include "qelib1.inc";
qreg q[25];
qreg z_anc[5];
qreg x_anc[6];
qreg a0[3];
qreg a1[3];
qreg a2[2];
qreg a3[2];
qreg a4[2];
qreg a5[2];
creg z_c[5];
creg x_c[6];
creg c0[3];
creg c1[3];
creg c2[2];
creg c3[2];
creg c4[2];
creg c5[2];
h q[0];
h q[1];
h q[2];
h q[4];
h q[5];
h q[7];
h q[11];
h q[14];
h q[15];
h q[18];
h q[21];
h q[24];
cx q[18],q[23];
cx q[11],q[17];
cx q[7],q[13];
cx q[18],q[22];
cx q[11],q[12];
cx q[7],q[8];
cx q[2],q[3];
cx q[1],q[6];
cx q[21],q[22];
cx q[18],q[17];
cx q[15],q[20];
cx q[14],q[19];
cx q[11],q[16];
cx q[8],q[12];
cx q[6],q[7];
cx q[5],q[10];
cx q[4],q[9];
cx q[1],q[2];
cx q[24],q[23];
cx q[20],q[21];
cx q[19],q[18];
cx q[15],q[16];
cx q[14],q[13];
cx q[10],q[11];
cx q[9],q[8];
cx q[5],q[6];
cx q[4],q[3];
cx q[0],q[1];
cx q[2],z_anc[0];
cx q[3],z_anc[0];
cx q[6],z_anc[0];
cx q[9],z_anc[0];
cx q[10],z_anc[0];
cx q[12],z_anc[0];
cx q[13],z_anc[0];
cx q[16],z_anc[0];
cx q[18],z_anc[0];
cx q[21],z_anc[0];
cx q[22],z_anc[0];
cx q[4],z_anc[1];
cx q[8],z_anc[1];
cx q[13],z_anc[1];
cx q[19],z_anc[1];
cx q[16],z_anc[2];
cx q[17],z_anc[2];
cx q[20],z_anc[2];
cx q[23],z_anc[2];
cx q[24],z_anc[2];
cx q[0],z_anc[3];
cx q[1],z_anc[3];
cx q[7],z_anc[3];
cx q[12],z_anc[3];
cx q[16],z_anc[3];
cx q[20],z_anc[3];
cx q[4],z_anc[4];
cx q[5],z_anc[4];
cx q[8],z_anc[4];
cx q[11],z_anc[4];
cx q[12],z_anc[4];
measure z_anc[0] -> z_c[0];
measure z_anc[1] -> z_c[1];
measure z_anc[2] -> z_c[2];
measure z_anc[3] -> z_c[3];
measure z_anc[4] -> z_c[4];
h x_anc[0];
cx x_anc[0],q[5];
cx x_anc[0],a0[0];
cx x_anc[0],q[6];
cx x_anc[0],a0[1];
cx x_anc[0],q[10];
cx x_anc[0],q[12];
cx x_anc[0],a0[2];
cx x_anc[0],q[16];
cx x_anc[0],q[18];
cx x_anc[0],a0[0];
measure a0[0] -> c0[0];
cx x_anc[0],q[21];
cx x_anc[0],a0[2];
measure a0[2] -> c0[2];
cx x_anc[0],a0[1];
measure a0[1] -> c0[1];
cx x_anc[0],q[23];
h x_anc[0];
measure x_anc[0] -> x_c[0];
h x_anc[1];
cx x_anc[1],q[1];
cx x_anc[1],a1[0];
cx x_anc[1],q[3];
cx x_anc[1],a1[1];
cx x_anc[1],q[6];
cx x_anc[1],q[8];
cx x_anc[1],a1[2];
cx x_anc[1],q[12];
cx x_anc[1],q[14];
cx x_anc[1],a1[0];
measure a1[0] -> c1[0];
cx x_anc[1],q[18];
cx x_anc[1],a1[2];
measure a1[2] -> c1[2];
cx x_anc[1],a1[1];
measure a1[1] -> c1[1];
cx x_anc[1],q[19];
h x_anc[1];
measure x_anc[1] -> x_c[1];
h x_anc[2];
cx x_anc[2],q[0];
cx x_anc[2],a2[0];
cx x_anc[2],q[4];
cx x_anc[2],a2[1];
cx x_anc[2],q[6];
cx x_anc[2],q[9];
cx x_anc[2],a2[0];
measure a2[0] -> c2[0];
cx x_anc[2],q[12];
cx x_anc[2],a2[1];
measure a2[1] -> c2[1];
cx x_anc[2],q[13];
h x_anc[2];
measure x_anc[2] -> x_c[2];
h x_anc[3];
cx x_anc[3],q[13];
cx x_anc[3],a3[0];
cx x_anc[3],q[14];
cx x_anc[3],a3[1];
cx x_anc[3],q[17];
cx x_anc[3],q[19];
cx x_anc[3],a3[0];
measure a3[0] -> c3[0];
cx x_anc[3],q[21];
cx x_anc[3],a3[1];
measure a3[1] -> c3[1];
cx x_anc[3],q[23];
h x_anc[3];
measure x_anc[3] -> x_c[3];
h x_anc[4];
cx x_anc[4],q[11];
cx x_anc[4],a4[0];
cx x_anc[4],q[12];
cx x_anc[4],a4[1];
cx x_anc[4],q[16];
cx x_anc[4],q[17];
cx x_anc[4],a4[0];
measure a4[0] -> c4[0];
cx x_anc[4],q[23];
cx x_anc[4],a4[1];
measure a4[1] -> c4[1];
cx x_anc[4],q[24];
h x_anc[4];
measure x_anc[4] -> x_c[4];
h x_anc[5];
cx x_anc[5],q[0];
cx x_anc[5],a5[0];
cx x_anc[5],q[3];
cx x_anc[5],a5[1];
cx x_anc[5],q[6];
cx x_anc[5],q[7];
cx x_anc[5],a5[0];
measure a5[0] -> c5[0];
cx x_anc[5],q[23];
cx x_anc[5],a5[1];
measure a5[1] -> c5[1];
cx x_anc[5],q[24];
h x_anc[5];
measure x_anc[5] -> x_c[5];