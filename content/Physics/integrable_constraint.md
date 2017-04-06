title: Integrable Constraint
date: 2013-12-12
tags: Mechanics, math

$\newcommand{bm}{\mathbf}\newcommand{\dd}{\mathrm{d}}\newcommand{\pp}{\mathrm{p}}$
In N dimension, $$\begin{aligned}
\bm f\times\bm g&\rightarrow f_a\times g_b=[f_ag_b]_{ab}\\
\bm f\cdot\bm g\times\bm h&\rightarrow(f_a, g_b, h_c)=[f_ag_bh_c]_{abc}
    \end{aligned}$$

Suppose $\bm f(\bm r)=f_i\hat e_i$, and a constraint $f_i\dd r_i=0$

Even if the $\nabla\times\bm f\neq 0$, we may find some function
$\varphi$ which is nonzero at the nonzero points of $\bm f$ s.t.
$$\nabla\times(\varphi\bm f)=\nabla\varphi\times\bm f+\varphi\nabla\times\bm f=0$$

Dotted by $\bm f$, we find
$$\varphi\bm f\cdot\nabla \times\bm f=(\bm f,\nabla\varphi, \bm f)\propto [f_i\pp_j f_k]_{ijk} =0$$

E.g. For a 2D function, $A_{ijk}\equiv 0$, so there is always a
solution.
