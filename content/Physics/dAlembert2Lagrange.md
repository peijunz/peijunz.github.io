---
title: From d’Alembert to Lagrange
date: 2016-10-01
lang: en
tags: Mechanics
---

## Nowtonian
<span class="mathmacros" style="display:none;">
$\newcommand{\bm}{\mathbf}
\newcommand{\dd}{\mathrm{d}}
\newcommand{\pp}{\partial}
\newcommand{\mdef}{\overset{\mathrm{def}}{=}}$
</span>
Assume $\bm F$ is active force and $\bm R$ is constraint force. Then for
$i$th body we have Newton’s Second Law:
$$\bm F^\mathrm{tot}_i=\bm F_i+\bm R_i=m\bm a_i$$ With a virtual
displacement $\delta \bm x_i$, we define:
$$\delta W_i=\bm F^\mathrm{tot}_i\cdot\delta\bm x_i,\quad
\delta K_i=m\bm a_i\cdot\delta\bm x_i$$ Then we have
$\delta W_i=\delta K_i$. Define
$$\delta W=\sum_i\delta W_i,\quad\delta K=\sum_i\delta K_i$$ and
obviously$$\delta W=\delta K$$ As the constraints will not do work, we
can rewrite $$\delta W=\sum_i\bm F_i\cdot\delta\bm x_i$$

## Lagrangian

### Statics $\delta K=0$

Principle of Virtual Work: $$\frac{\delta W}{\delta q}=0$$ i.e. Minimal
Potential Energy $$Q\mdef-\frac{\delta V}{\delta q}=0$$

### Dynamics

d’Alembert’s Principle—Counterpart of Principle of Virtual Work:
$$\frac{\delta W}{\delta q}=\frac{\delta K}{\delta q}$$

i.e. $$\begin{aligned}
Q\mdef\bm F_i\cdot\frac{\pp \bm x_i}{\pp q}&=m_i\bm a_i\cdot\frac{\pp \bm x_i}{\pp q}\\
&=m_i\frac{\dd \bm v_i}{\dd t}\cdot\frac{\pp \bm x_i}{\pp q}\\
&=m_i\frac{\dd}{\dd t}\left( \bm v\cdot\frac{\pp \bm x_i}{\pp q}\right)-m_i\bm v\cdot\frac{\dd}{\dd t}\frac{\pp}{\pp q}\bm x_i\\
&=m_i\frac{\dd}{\dd t}\left(\bm v\cdot\frac{\pp \dot{\bm x_i}}{\pp\dot q}\right)-m_i\bm v\cdot\frac{\pp}{\pp q}\frac{\dd}{\dd t}\bm x_i\\
&=\frac{\dd}{\dd t}\left(m_i\bm v_i\cdot\frac{\pp\bm v_i}{\pp\dot q}\right)-m_i\bm v_i\cdot\frac{\pp \bm v_i}{\pp q}\\
&=\frac{\dd}{\dd t}\frac{\pp T}{\pp\dot q}-\frac{\pp T}{\pp q}\\
&=\left(\frac{\dd}{\dd t}\frac{\pp}{\pp\dot q}-\frac{\pp}{\pp q}\right)T\label{T}\end{aligned}$$

For conservative or monogenic system,

$$Q=\left(\frac{\dd}{\dd t}\frac{\pp}{\pp\dot q}-\frac{\pp}{\pp q}\right)V\label{V}$$

As a result of last two equations, if we define $L=T-V$, we have
$$\left(\frac{\dd}{\dd t}\frac{\pp}{\pp\dot q}-\frac{\pp}{\pp q}\right)L=0$$
