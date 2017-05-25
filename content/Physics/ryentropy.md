---
title: Renyi entropy of the wormholes
date: 2017-01-17
summary: In information theory, the Rényi entropy generalizes the Hartley entropy, the Shannon entropy, the collision entropy and the min entropy. Entropies quantify the diversity, uncertainty, or randomness of a system. The Rényi entropy is named after Alfréd Rényi.
---

<span class="mathmacros" style="display:none;">
$\newcommand{\bm}{\mathbf}\newcommand{\dd}{\mathrm{d}}$
</span>
Rényi entropy is defined as: 
$$\begin{aligned}
    S_n(\alpha)&:=\frac{1}{1-\alpha}\log\left({\sum_{a_{1\to n}}}\sum_{\mu=1}^{N}\left(\frac{p_{a_1a_2\cdots a_n}}{N}\right)^\alpha\right) \\
    &=\frac{1}{1-\alpha}\log\left(\frac{1}{\mathcal{D}^{2\alpha(n-1)}}{{{\sum_{a_{1\to n}}}N_{a_1a_2\cdots a_n}{\prod_{i=1}^n d_{a_i}^\alpha}}}\right) \\
    &=\frac{1}{1-\alpha}\left[\log\left({{{\sum_{a_{1\to n}}}N_{a_1a_2\cdots a_n}{\prod_{i=1}^n d_{a_i}^\alpha}}}\right)-\alpha(n-1)\log \mathcal{D}^2\right]\\
    &=\frac{\alpha(n-1)\log \mathcal{D}^2-\log t_n(\alpha)}{\alpha-1}
\end{aligned}$$
We are using $$\begin{aligned}
    t_n(\alpha)&:={{{\sum_{a_{1\to n}}}N_{a_1a_2\cdots a_n}{\prod_{i=1}^n d_{a_i}^\alpha}}}\\
    &= {\sum_{a_{1\to n}}}{\sum_{x_{1\to n-1}}}N_{x_0a_1}^{x_1}N_{x_1a_2}^{x_2}\cdots N_{x_{n-1}a_n}^{x_n}{\prod_{i=1}^n d_{a_i}^\alpha},\quad x_0=x_n=1\\
    &= {\sum_{x_{1\to n-1}}}\prod_{i=1}^n\left({\sum_{a_{1\to n}}}d_{a_i}^\alpha N_{x_{i-1}a_i}^{x_i}\right)\end{aligned}$$
Define $$T_{bc}(\alpha):=\sum_ad_a^\alpha N_{ba}^c$$ Then
$$t_n(\alpha)={\sum_{x_{1\to n-1}}}\prod_{i=1}^nT_{x_{i-1}x_i}(\alpha)\left[\bm T^n(\alpha)\right]_{x_0x_n}=\left[\bm T^n(\alpha)\right]_{11}
\label{t11}$$ It’s obvious that $T$ is an elementwise positive matrix.
Moreover, $T$ is normal: $$\begin{aligned}
\label{key}
T_{ab}T_{cb}&=\sum_x\sum_y d_x^\alpha d_y^\alpha \sum_b N_{xa}^b N_{yc}^b\\
&=\sum_x\sum_y d_x^\alpha d_y^\alpha \sum_b N_{x\bar b}^{\bar a} N_{y\bar b}^{\bar c}\\
&=\sum_x\sum_y d_x^\alpha d_y^\alpha \sum_b  N_{\bar y b}^{c}N_{\bar xb}^{a}\\
&=T_{ba}T_{bc}\end{aligned}$$ Thus, the eigenvectors correspond to
distinct eigenvalues must be orthogonal. Assume the eigenvalues and
orthonormal eigenvectors are $\bm x_i$ with eigenvalue
$\lambda_i(\alpha)$. The eigenvector $\bm x_m:=d_i\bm e_i/\mathcal{D}$
has the maximum eigenvalue because its all components are positive. The
eigenvalue is
$$\lambda_{\max}(\alpha)=\sum_a d_a^{\alpha+1}, \quad\lambda_{\max}(1)=\mathcal{D}^2$$

We decompose $\bm e_1$ into $\bm x_i$ to calculate $[\bm{T}^n]_{11}$:
$$\begin{aligned}
\bm e_1&=\sum_i c_i\bm x_i,\quad c_i=\bm e_1\cdot \bm x_i\\
[\bm{T}_\alpha^n]_{11}&=\bm{e}_1^T\bm{T}_\alpha^n \bm{e}_1=\sum_i c_i^2\lambda_i^n\\
&=c_m^2\lambda_{\max}^n\left[1+\sum_{i\neq m}\frac{c_i^2}{c_m^2}\left( \frac{\lambda_i}{\lambda_{\max}}\right) ^n\right]\\
&=\frac{\lambda_{\max}^n}{\mathcal{D}^2}\left[1+\Theta(k^n)\right],\quad k:=\frac{\lambda_{\mathrm{sub}}}{\lambda_{\max}}<1\end{aligned}$$
$$\begin{aligned}
S_n(\alpha)&=\frac{\alpha(n-1)\log \mathcal{D}^2-\log [\bm{T}_\alpha^n]_{11}}{\alpha-1}\\
&=n\left[\frac{\alpha\log \lambda_{\max}(1)-\log \lambda_{\max}(\alpha)}{\alpha-1}\right]-\log \mathcal{D}^2+\Theta(k^n)\label{al}\end{aligned}$$

In the $\alpha=1$ case, there is no other nontrivial eigenvector except
$\bm x_m$ because $\bm T=\bm x_m\bm x_m^\mathsf{T}$. So the
$\Theta(k^n)$ term in \[al\] reduce to zero.

$$\begin{aligned}
S_{n}(1)&=n\frac{\dd}{\dd\alpha}\Big|_{\alpha=1}\Big[\alpha\log \lambda_{\max}(1)-\log \lambda_{\max}(\alpha)\Big] -\log \mathcal{D}^2\\
&=n\Big[\log \mathcal{D}^2-\sum_a \frac{d_a^2\log d_a}{\mathcal{D}^2}\Big]-\log \mathcal{D}^2\\
&=(n-1)\log \mathcal{D}^2-n\sum_a p_a\log d_a\end{aligned}$$
