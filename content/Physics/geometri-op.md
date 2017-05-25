---
title: Geometrical Optics in Continuum
date: 2017-01-05
tags: Calculus of Variations
---

## Fermat’s Principle
<span class="mathmacros" style="display:none;">
$\newcommand{bm}{\mathbf}\newcommand{\dd}{\mathrm{d}}\newcommand{\pp}{\partial}$
</span>

Fermat’s Principle is $$\delta s=\delta\int n\dd \ell=0$$ If we choose
the path connecting two points to be
$$\bm r=\bm r(t),\quad t_0\leq t\leq t_1$$ We can write
$$s=\int n\frac{\dd \ell}{\dd t}\dd t, \quad \frac{\dd \ell}{\dd t}=|\dot{\bm r}|$$
The Lagrangian about parameter $t$ is
$$L=n\frac{\dd \ell}{\dd t}=n(\bm r)|\bm{\dot r}|$$ then the
Euler-Lagrange Equation is $$\begin{aligned}
&\left(\frac{\dd}{\dd t}\frac{\pp}{\pp\bm{\dot r}}-\frac{\pp}{\pp\bm{r}}\right)L=0\\
\bm p&=\frac{\pp L}{\pp \bm{\dot r}}=n \hat\tau,\quad\hat{\tau}=\frac{\pp |\dot{\bm r}|}{\pp \bm{\dot r}}=\bm{\dot r}/|\bm{\dot r}|=\frac{\dd\bm r}{\dd\ell}\\
\frac{\dd \bm p}{\dd t}&=\frac{\pp L}{\pp \bm{r}}=\frac{\dd\ell}{\dd t}\nabla n\\
\frac{\dd \bm p}{\dd \ell}&=\nabla n=\bm F\end{aligned}$$ Generalized
Momentum $\bm p$ is independent of the choice of $t$, and

## Examples

### Rectangular Coordinates

$$n(x,y,z)=f(x,y),\quad\bm F=\frac{\pp f}{\pp x}\hat x+\frac{\pp f}{\pp y}\hat y$$

It is obvious that $p_z$ are conserved.

### Central Gradient

Define $\bm L=\bm r\times \bm p$, $$\begin{aligned}
    \frac{\dd \bm L}{\dd \ell}&=\frac{\dd\bm r}{\dd \ell}\times\bm p+\bm r\times\frac{\dd\bm p}{\dd \ell}
    \\&=\hat{\tau}\times \bm p+\bm r\times\bm F
    \\&=\bm r\times\bm F\end{aligned}$$ $\bm L$ is conserved for a
spherical symmetric distribution
$$n(\bm r)=f(r),\quad \bm r\times\bm F=\bm 0$$ $L_z$ is conserved for
$$n(\bm r)=f(r,\theta),\quad (\bm r\times\bm F)_z=0$$
