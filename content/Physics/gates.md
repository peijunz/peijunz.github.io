title: One way quantum computer
date: 2017-02-18

There are some discrepancies between the results here and the paper. But
the results are basically the same. I don’t know why `:-(`

Rotation Gates
==============
$\def\bra#1{\mathinner{\langle{#1}|}}
\def\ket#1{\mathinner{|{#1}\rangle}}
\def\braket#1{\mathinner{\langle{#1}\rangle}}
\newcommand{\ii}{\mathrm{i}}
\newcommand{\tr}{\mathrm{tr}}$
This part corresond to the Gates in paper 0301052v2.
$$S_{ab}=\frac{1+Z_a}{2}+\frac{1-Z_a}{2}Z_b=U_a+D_aZ_b$$

The $u_i, d_i$ are defined by $\ket{\psi_i}=u_i\ket{0_i}+d_i\ket{1_i}$.
And we have $Z_b\ket{+_b}=\ket{-_b}$

$$\begin{aligned}
\mathcal{R}&=\bra{\psi_1}\bra{\psi_2}\bra{\psi_3}\bra{\psi_4}S_{12}S_{23}S_{34}S_{45}\ket{+_2}\ket{+_3}\ket{+_4}\ket{+_5}\\
&=\left(\ket{+_5}\bra{\psi_4}U_4+\ket{-_5}\bra{\psi_4}D_4\right) \bra{\psi_1}\bra{\psi_2}\bra{\psi_3}S_{12}S_{23}S_{34}\ket{+_2}\ket{+_3}\ket{+_4}\\
&=\prod_{i=4}^1 \Big(\ket{+_{i+1}}\bra{0_i}u_i+\ket{-_{i+1}}\bra{1_i}d_i\Big)\\
&=\prod_{i=4}^1  {\frac{1}{\sqrt{2}}\begin{bmatrix}u_i & d_i\\-u_i & -d_i\end{bmatrix}}=\prod_{i=4}^1  H\begin{bmatrix}u_i & \\ & d_i\end{bmatrix}\\
&=\prod_{i=4}^1  H\mathcal{Z}_{\phi_i},\quad \mathcal{Z}_\phi=\exp(-\ii \phi Z/2)\\
&=(H\mathcal{Z}_\zeta H)\mathcal{Z}_\eta (H\mathcal{Z}_\xi H)\\
&=\mathcal{X}_\zeta\mathcal{Z}_\eta\mathcal{X}_\xi\end{aligned}$$

In the
basis of $Z_1\rightarrow Z_5$. If all measurement results $\psi_i$ are
positive for directions $(0, \xi,\eta,\zeta)$, respectively, we can
verify that the rotation matrix $\mathcal{R}$ is equivalent to
$\exp(-\ii \zeta X/2)\exp(-\ii \eta Z/2)\exp(-\ii \xi X/2)$. Hadamard
gate is simply a special case.

CNOT Gates
==========

This part corresponds to PRL.86.5188(Page 3, upper left corner), so we
are using a different $S$:
$$S_{ab}=1-\frac{(1+Z_{a})(1-Z_{b})}{2}=D_a+U_aZ_b=U_b-D_bZ_a$$ So
$$S_{ab}S_{bc}=\frac{Z_c-Z_a}{2}+\frac{Z_c+Z_a}{2}Z_b=U_bZ_c-D_bZ_a$$

$$\begin{aligned}
\mathcal{C}&=\bra{\psi_1}\bra{\psi_2}S_{12}S_{23}S_{24}\ket{+_2}\ket{+_3}\\
&=\Big(\ket{+_{3}}\bra{1_2}d_2+\ket{-_3}\bra{0_2}u_2\Big)\bra{\psi_1}S_{12}S_{24}\ket{+_2}\\
&=\Big(\ket{+_{3}}\bra{1_2}d_2+\ket{-_3}\bra{0_2}u_2\Big)\bra{\psi_1}U_2Z_4-D_2Z_1\ket{+_2}\\
&=\Big(\pm_2\ket{+_{3}}\bra{1_2}+\ket{-_3}\bra{0_2}\Big)\Big(\ket{0_2}\bra{\psi_1}Z_4-\ket{1_2}\bra{\psi_1}Z_1\Big)/2\\
&=\Big( \mp_2\ket{+_{3}}\bra{\mp_1}+\ket{-_3}\bra{\pm_1}Z_4\Big)/2 \\\end{aligned}$$

If $s_1=1, s_2=1$, then
$\mathcal{C}_n=\ket{-_{3}}\bra{-_1}Z_4+\ket{+_3}\bra{+_1}I_4$
$$\mathcal{C}=I_4\otimes\begin{bmatrix}
1& 1\\
1& 1
\end{bmatrix}+Z_4\otimes\begin{bmatrix}
1& -1\\
-1& 1
\end{bmatrix}=\begin{bmatrix}
1& &&\\
& 1&&\\
&&&1\\
&&1&\\
\end{bmatrix}$$ In the basis of
$Z_4\otimes Z_1\rightarrow Z_4\otimes Z_3$