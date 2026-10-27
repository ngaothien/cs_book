# Inequalities Involving Subordinate Norms


<!-- PAGE 362 -->

## 9.4 Inequalities Involving Subordinate Norms

In this section we discuss two technical inequalities which will be needed for certain proofs in the last three sections of this chapter. First we prove a proposition which will be needed when we deal with the condition number of a matrix.

> **Proposition 9.12.** Let $\|\|$ be any matrix norm, and let $B \in M_{n}(\mathbb{C})$ such that $\|B\| < 1$.
$(1)$ If $\|\|$ is a subordinate matrix norm, then the matrix $I + B$ is invertible and
$$(I + B)^{-1}

$\le \frac{1}{1 -\|B\|}$ .$$
$(2)$ If a matrix of the form I $+ B$ is singular, then $\|B\|\ge 1$ for every matrix norm (not necessarily subordinate).

*Proof.* $(1)$ Observe that (I $+$ B)u $= 0$ implies Bu $= -u$, so
$$\|u\|= \|Bu\|.$$
Recall that
$$\|Bu\|\le \|B\|\|u\|$$
for every subordinate norm. Since $\|B\| < 1$, if $u \neq  0$, then
$$\|Bu\|< \|u\|,$$
which contradicts $\|u\| = \|Bu\|$. Therefore, we must have $u = 0$, which proves that I $+ B$ is injective, and thus bijective, i.e., invertible. Then we have
$$(I + B)^{-1}+ B(I + B)^{-1}= (I + B)(I + B)^{-1}= I,$$
so we get
$$(I + B)^{-1}= I -B(I + B)^{-1},$$
which yields
$$(I + B)^{-1}

$\le 1 + \|B\|$

(I $+ B)^{-1}$

,$$ and finally,
$$(I + B)^{-1}

$\le \frac{1}{1 -\|B\|}$ .$$
$(2)$ If I $+ B$ is singular, then $-1$ is an eigenvalue of $B$, and by Proposition 9.7, we get $\rho (B) \le \|B\|$, which implies $1 \le \rho (B) \le \|B\|$. The second inequality is a result is that is needed to deal with the convergence of sequences of powers of matrices.

<!-- PAGE 363 -->

> **Proposition 9.13.** For every matrix $A \in M_{n}(\mathbb{C})$ and for every $\epsilon  > 0$, there is some subordinate matrix norm $\|\|$ such that
$$\|A\|\le \rho (A) + \epsilon .$$

*Proof.* By Theorem 15.5, there exists some invertible matrix $U$ and some upper triangular matrix $T$ such that
$$A = UTU^{-1} ,$$
and say that
$$T = \begin{pmatrix} \lambda_{1} & t_{12} & t_{13} & \cdots & t_{1n} \\ 0 & \lambda_{2} & t_{23} & \cdots & t_{2n} \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & \lambda_{n-1} & t_{n-1n} \\ 0 & 0 & \cdots & 0 & \lambda_{n} \end{pmatrix} ,$$
where $\lambda_{1} , \dots  , \lambda_{n}$  are the eigenvalues of $A$. For every $\delta  \neq  0$, define the diagonal matrix
$$D_{\delta} = \mathrm{diag}(1, \delta , \delta^{2} , \dots  , \delta^{n-1} ),$$
and consider the matrix
$$(UD_{\delta})^{-1}A(UD_{\delta}) = D_{\delta}^{-1} TD_{\delta} = \begin{pmatrix} \lambda_{1} & \delta t_{12} & \delta^{2} t_{13} & \cdots & \delta^{n-1} t_{1n} \\ 0 & \lambda_{2} & \delta t_{23} & \cdots & \delta^{n-2} t_{2n} \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & \lambda_{n-1} & \delta t_{n-1n} \\ 0 & 0 & \cdots & 0 & \lambda_{n} \end{pmatrix} .$$
Now define the function $\|\|: M_{n}(\mathbb{C}) \to \mathbb{R}$ by
$$\|B\|=

$(UD_{\delta})^{-1}B(UD_{\delta})_{\infty},$$$ for every $B \in M_{n}(\mathbb{C})$. Then it is easy to verify that the above function is the matrix norm subordinate to the vector norm
$$v \mapsto

$(UD_{\delta})^{-1}v_{\infty}.$$$ Furthermore, for every $\epsilon  > 0$, we can pick $\delta$  so that
$$\sum_{j=i+1}^{n}  |\delta^{j-i} t_{ij}| \le \epsilon ,1 \le i \le n -1,$$
and by definition of the norm $\|\|_{\infty}$, we get
$$\|A\|\le \rho (A) + \epsilon ,$$
which shows that the norm that we have constructed satisfies the required properties.
