title: Invariance of Euler-Lagrange Equations
date: 2016-10-30

$\newcommand{bm}{\mathbf}
\newcommand{\dd}{\mathrm{d}}
\newcommand{\pp}{\partial}$E-L is deduced from the Hamilton’s principle
$$\delta S=\delta\int L(\bm q, \dot{\bm q}, t)dt=0$$

It is easy to find that, for $L'=L+\dd f(\bm q, t)/\dd t$ or change of
variables $\bm q\to\bm Q$, the min of $\delta S$ will not change. Here
we want to prove it the hard way—using E-L equations.

The original E-L Equations are:
$$\left(\frac{\dd}{\dd t}\frac{\pp}{\pp \dot q_i}-\frac{\pp}{\pp q_i}\right)L=0$$

Commutator $\left [\dfrac{\dd}{\dd t}, \dfrac{\pp}{\pp q_i}\right ]f(\bm q, t)=0$
=================================================================================

#### Proof

$$\left[\frac{\dd}{\dd t},\frac{\pp}{\pp q_i}\right]f(\bm q, t) = \left[\dot q_i\frac{\pp}{\pp q_i}+\frac{\pp}{\pp t},\frac{\pp}{\pp q_i}\right]f(\bm q, t)=0$$

Condition $L'=L+\dfrac{\dd f(\bm q, t)}{\dd t}$
===============================================

$$\begin{aligned}
\left(\frac{\dd}{\dd t}\frac{\pp}{\pp \dot q_i}-\frac{\pp}{\pp q_i}\right)L'
&=\left(\frac{\dd}{\dd t}\frac{\pp}{\pp \dot q_i}-\frac{\pp}{\pp q_i}\right)\frac{\dd f}{\dd t}\\
&=\frac{\dd}{\dd t}\frac{\pp}{\pp q_i}f-\frac{\pp}{\pp q_i}\frac{\dd}{\dd t}f\\
&=\left[\frac{\dd}{\dd t},\frac{\pp}{\pp q_i}\right]f\\
&=0\end{aligned}$$

Condition $\bm q\to\bm Q$
=========================

We we change generalized coordinates $\bm q\to\bm Q$, the Lagrangian:
$$L(\bm q, \dot{\bm q}, t)\to L'(\bm Q, \dot{\bm Q}, t)=L\big[\bm q(\bm Q, t), \dot{\bm q}(\bm Q, \dot{\bm Q}, t), t\big]$$

We want to prove:
$$\left(\frac{\dd}{\dd t}\frac{\pp}{\pp \dot Q_i}-\frac{\pp}{\pp Q_i}\right)L'=0$$

$$\begin{aligned}
\mathrm{LHS}
&=\left(\frac{\dd}{\dd t}\frac{\pp \dot q_j}{\pp \dot Q_i}\frac{\pp}{\pp \dot q_j}-\frac{\pp q_j}{\pp Q_i}\frac{\pp }{\pp q_j}-\frac{\pp \dot q_j}{\pp Q_i}\frac{\pp }{\pp\dot q_j}\right)L\\
&=\left(\frac{\dd}{\dd t}\frac{\pp q_j}{\pp Q_i}\frac{\pp}{\pp\dot q_j}-\frac{\pp q_j}{\pp Q_i}\frac{\pp }{\pp q_j}-\frac{\pp \dot q_j}{\pp Q_i}\frac{\pp }{\pp\dot q_j}\right)L\\
&=\left[\left(\frac{\dd}{\dd t}\frac{\pp}{\pp Q_i}q_j\right)\frac{\pp}{\pp \dot q_j}+\frac{\pp q_j}{\pp Q_i}\frac{\dd}{\dd t}\frac{\pp}{\pp \dot q_j}-\frac{\pp q_j}{\pp Q_i}\frac{\pp }{\pp q_j}-\left(\frac{\pp}{\pp Q_i}\frac{\dd}{\dd t}q_j\right)\frac{\pp }{\pp\dot q_j}\right]L\\
&=\left(\left[\frac{\dd}{\dd t}, \frac{\pp}{\pp Q_i}\right]q_j\right)\frac{\pp}{\pp \dot q_j}L+\frac{\pp q_j}{\pp Q_i}\left(\frac{\dd}{\dd t}\frac{\pp}{\pp \dot q_j}-\frac{\pp }{\pp q_j}\right)L\\
&=0\end{aligned}$$
