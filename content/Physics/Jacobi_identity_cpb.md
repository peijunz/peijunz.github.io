---
title: Jacobi Identity for Classical Possion Bracket
date: 2016-10-30
lang: en
slug: jacobi-identity
tags: Mechanics
---

<span class="mathmacros" style="display:none;">
$\newcommand{\pp}{\partial}
\newcommand{\sgn}{\mathrm{sgn}}
\newcommand{\mdef}{\overset{\mathrm{def}}{=}}$</span>
Definition of Classical Possion Bracket:
$$[f, g]=\sum_{i=1, 2,\ldots, n}\frac{\pp(f, g)}{\pp(p_i, q_i)}=\sum_{i=1, 2,\ldots, n}\left(\frac{\pp f}{\pp p_i}\frac{\pp g}{\pp q_i}-\frac{\pp f}{\pp q_i}\frac{\pp g}{\pp p_i}\right)$$

If we define $p_{-i}\mdef q_{i}$, and
$I=\{\pm 1, \pm, 2,\ldots, \pm n\}$, we can rewrite it:
$$[f, g]=\sum_{i\in I} \sgn(i) \frac{\pp f}{\pp p_i}\frac{\pp g}{\pp p_{-i}}$$

Jacobi Identity is $[f,[g,h]]+[g,[h,f]]+[h,[f,g]]=0$. With the new
notation, we can rewrite it as $$\begin{aligned}
\sum_{\overrightarrow{fgh}}[f,[g,h]]
  &=\sum_{\overrightarrow{fgh}}\sum_{i\in I}\sgn(i)\frac{\pp f}{\pp p_i}\frac{\pp}{\pp p_{-i}}\left(\sum_{j\in I}\sgn(j)\frac{\pp g}{\pp p_j}\frac{\pp h}{\pp p_{-j}}\right)\\
 &=\sum_{\overrightarrow{fgh}}\sum_{i, j\in I}\sgn(ij)\left(\frac{\pp f}{{\pp p_{i}}}\frac{\pp h}{{\pp p_{-j}}}\frac{\pp^2g}{{\pp p_{-i}}{\pp p_{j}}}
 +\frac{\pp f}{{\pp p_{i}}}\frac{\pp g}{{\pp p_{j}}}\frac{\pp^2h}{{\pp p_{-i}}{\pp p_{-j}}}\right)\\
 &=\sum_{\overrightarrow{fgh}}\sum_{i, j\in I}\sgn(ij)\left(\frac{\pp f}{{\pp p_{i}}}\frac{\pp h}{{\pp p_{-j}}}\frac{\pp^2g}{{\pp p_{-i}}{\pp p_{j}}}
 +\frac{\pp h}{{\pp p_{i}}}\frac{\pp f}{{\pp p_{j}}}\frac{\pp^2g}{{\pp p_{-i}}{\pp p_{-j}}}\right)\\
 &=\sum_{\overrightarrow{fgh}}\sum_{i, j\in I}\sgn(ij)\left(\frac{\pp f}{{\pp p_{i}}}\frac{\pp h}{{\pp p_{-j}}}\frac{\pp^2g}{{\pp p_{-i}}{\pp p_{j}}}
 +\frac{\pp f}{{\pp p_{i}}}\frac{\pp h}{{\pp p_{j}}}\frac{\pp^2g}{{\pp p_{-i}}{\pp p_{-j}}}\right)\\
 &=\sum_{\overrightarrow{fgh}}\sum_{i, j\in I}\sgn(ij)\left(\frac{\pp f}{{\pp p_{i}}}\frac{\pp h}{{\pp p_{-j}}}\frac{\pp^2g}{{\pp p_{-i}}{\pp p_{j}}}
 -\frac{\pp f}{{\pp p_{i}}}\frac{\pp h}{{\pp p_{-j}}}\frac{\pp^2g}{{\pp p_{-i}}{\pp p_{j}}}\right)\\
 &=0\end{aligned}$$
