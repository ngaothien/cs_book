# The Matrix Exponential


<!-- PAGE 377 -->
$$Proof. If \sum_{k}  \infty =0 u_{k} is absolutely convergent, then we prove that the sequence (S_{m}) is a Cauchy$$
sequence; that is, for every $\epsilon  > 0$, there is some $p > 0$ such that for all $n \ge m \ge p$,
$$\|S_{n} -S_{m}\|\le \epsilon .$$
Observe that
$$\|S_{n} -S_{m}\|= \|u_{m+1} + \cdots  + u_{n}\|\le \|u_{m+1}\|+ \cdots  + \|u_{n}\|,$$
$$and since the sequence \sum_{k}  \infty  \|u_{k}\|converges, it satisfies Cauchy’s criterion. Thus, the se-$$
quence $(S_{m})$ also $satisfies^{=0}$ Cauchy’s criterion, and since $E$ is a complete vector space, the sequence $(S_{m})$ converges.
Remark: It can be shown that if $(E, \|\|)$ is a normed vector space such that every absolutely convergent series is also convergent, then $E$ must be complete (see Schwartz $[156])$.
$$An important corollary of absolute convergence is that if the terms in series \sum_{k}  \infty  u_{k}$$
are rearranged, then the resulting series is still absolutely convergent and has $the^{=0}$ same sum. More precisely, let $\sigma$  be any permutation (bijection) of the natural numbers. The
$$series \sum_{k}  \infty =0 u_{\sigma(k)} is called a rearrangement of the original series. The following result can be$$
shown (see Schwartz $[156])$.

> **Proposition 9.20.** Assume $(E, \|\|)$ is a normed vector space. If a series $\infty  u$ is conver-
$$gent as well as absolutely convergent, then for every permutation of\mathbb{N}, the series \sum_{k}  =0 \infty$$
$$\sigma \sum_{k}^{k}  =0 u_{\sigma(k)}$$
is convergent and absolutely convergent, and its sum is equal to the sum of the original series:
$$\sum_{k=0}^{\infty}  u_{\sigma(k)} = \sum_{k=0}^{\infty}  u_{k}.$$
In particular, if $(E, \|\|)$ is a complete normed vector space, then Proposition 9.20 holds. We now apply Proposition 9.19 to the matrix exponential.

## 9.8 The Matrix Exponential


> **Proposition 9.21.** For any $n \times  n$ real or complex matrix $A$, the series
$$\sum_{k=0}^{\infty}  \frac{A^{k}}{k!}$$
converges absolutely for any operator norm on $M_{n}(\mathbb{C})$ (or $M_{n}(\mathbb{R}))$.

<!-- PAGE 378 -->
$$\mathbb{C}^{n}  \mathbb{R}^{n}$$

*Proof.* Pick any norm on (or ) and let $\|\|$ be the corresponding operator norm on $M_{n}(\mathbb{C})$. Since $M_{n}(\mathbb{C})$ has dimension $n^{2}$, it is complete. By Proposition 9.19, it suffices to
$$n


k$$
$$show that the series of nonnegative reals \sum_{k}  =0A\overline{k}\overline{!} converges. Since \|\|is an operator$$
norm, this a matrix norm, so we have
$$\|\|^{k}$$
$$\sum_{k=0}^{n}  \frac{A^{k}}{k!} \le \sum_{k=0}^{n}  \frac{A}{k!} \le e^{\|A\|}.$$
$$n


k$$
$$Thus, the nondecreasing sequence of positive real numbers \sum_{k}  =0A\overline{k}\overline{!} is bounded by e^{\|A\|},$$
and by a fundamental property of $\mathbb{R}$, it has a least upper bound which is its limit.

> **Definition 9.17.** Let $E$ be a finite-dimensional real or complex normed vector space. For any $n \times  n$ matrix $A$, the limit of the series
$$\sum_{k=0}^{\infty}  \frac{A^{k}}{k!}$$
is the exponential of $A$ and is denoted $e^{A}$.
$$\mathbb{C}$$
A basic property of the exponential $x \mapsto e^{x}$ with $x \in$  is
$$\mathbb{C}$$
$$e^{x+y}= e^{x}e^{y},for all x, y \in .$$
As a consequence, $e^{x}$ is always invertible and $(e^{x})^{-1} = e^{-x}$. For matrices, because matrix multiplication is not commutative, in general,
$$e^{A+B}= e^{A}e^{B}$$
fails! This result is salvaged as follows.

> **Proposition 9.22.** For any two $n \times  n$ complex matrices $A$ and $B$, if $A$ and $B$ commute, that is, $AB = BA$, then
$$e^{A+B}= e^{A}e^{B}.$$
A proof of Proposition 9.22 can be found in Gallier $[73]$. Since $A$ and $-A$ commute, as a corollary of Proposition 9.22, we see that $e^{A}$ is always invertible and that
$$(e^{A})^{-1}= e^{-A}.$$
It is also easy to see that
$$(e^{A})^{\top}= e^{A\top}.$$

<!-- PAGE 379 -->
In general, there is no closed-form formula for the exponential $e^{A}$ of a matrix $A$, but for skew symmetric matrices of dimension $2$ and $3$, there are explicit formulae. Everyone should enjoy computing the exponential $e^{A}$ where
$$A = \begin{pmatrix} 0 & -\theta \\ \theta & 0 \end{pmatrix} .$$
If we write
$$J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} ,$$
then
$$A = \theta J$$
The key property is that
$$J^{2}= -I.$$

> **Proposition 9.23.** If $A = \theta J$, then
$$e^{A}= \cos \theta I + \sin \theta J = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} .$$

*Proof.* We have
$$A^{4n}= \theta^{4n} I_{2},$$
$$A^{4n+1}= \theta^{4n+1} J,$$
$$A^{4n+2}= -\theta^{4n+2} I_{2},$$
$$A^{4n+3}= -\theta^{4n+3} J,$$
and so
$$e^{A}= I_{2} + \frac{\theta}{1!} J - \frac{\theta^{2}}{2!} I_{2} - \frac{\theta^{3}}{3!} J + \frac{\theta^{4}}{4!} I_{2} + \frac{\theta^{5}}{5!} J - \frac{\theta^{6}}{6!} I_{2} - \frac{\theta^{7}}{7!} J + \cdots  .$$
Rearranging the order of the terms, we have
$$e^{A}= \begin{pmatrix} \theta^{2} & \theta^{4} & \theta^{6} \\ 1 - & + & - & + \cdots \\ 2! & 4! & 6! \end{pmatrix} I_{2} + \begin{pmatrix} \theta \\ \theta^{3} & \theta^{5} & \theta^{7} \\ - & + & - & + \cdots \\ 1! & 3! & 5! & 7! \end{pmatrix} J.$$
We recognize the power series for cos $\theta$  and sin $\theta$ , and thus
$$e^{A}= \cos \theta I_{2} + \sin \theta J,$$
that is
$$e^{A}= \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} ,$$
as claimed.
