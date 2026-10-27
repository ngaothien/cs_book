# Limits of Sequences and Series


<!-- PAGE 374 -->
Fortunately, every $n \times m$-matrix $A$ can be written as
$$A = V DU^{\top}$$
where $U$ and $V$ are orthogonal and $D$ is a rectangular diagonal matrix with non-negative entries (singular value decomposition, or SVD); see Chapter $22$. The SVD can be used to solve an inconsistent system. It is shown in Chapter $23$ that there is a vector $x$ of smallest norm minimizing $\|Ax$ - $b\|_{2}$. It is given by the (Penrose) pseudo-inverse of $A$ (itself given by the SVD). It has been observed that solving in the least-squares sense may give too much weight to “outliers,” that is, points clearly outside the best-fit plane. In this case, it is preferable to minimize (the $\ell^{1}$ -norm)
$$\sum_{i=1}^{n}  |ax_{i} + by_{i} + d -z_{i}|.$$
This does not appear to be a linear problem, but we can use a trick to convert this minimization problem into a linear program (which means a problem involving linear constraints). Note that |x| $= max{x, -x}$. So by introducing new variables $e_{1}, \dots  , e_{n}$, our minimization problem is equivalent to the linear program (LP):
$$minimizee_{1} + \cdots  + e_{n}$$
$$subject toax_{i} + by_{i} + d -z_{i} \le e_{i}$$
$$-(ax_{i} + by_{i} + d -z_{i}) \le e_{i}$$
$$1 \le i \le n.$$
Observe that the constraints are equivalent to
$$e_{i} \ge |ax_{i} + by_{i} + d -z_{i}|,1 \le i \le n.$$
For an optimal solution, we must have equality, since otherwise we could decrease some $e_{i}$ and get an even better solution. Of course, we are no longer dealing with “pure” linear algebra, since our constraints are inequalities. We prefer not getting into linear programming right now, but the above example provides a good reason to learn more about linear programming!

## 9.7 Limits of Sequences and Series

$\mathbb{R} \mathbb{C} n$
$$If x \in  or x \in  and if |x| < 1, it is well known that the sums \sum_{k}  x^{k}= 1+x+x^{2}+\cdots +x^{n}$$
converge to the limit $1/(1$ - $x)$ when $n$ goes to infinity, and $we^{=0}$ write
$$\sum_{k=0}^{\infty}  x^{k} = \frac{1}{1 -x} .$$

<!-- PAGE 375 -->
For example,
$$\sum_{k=0}^{\infty}  \frac{1}{2^{k}} = 2.$$
Similarly, the sums
$$S_{n} = \sum_{k=0}^{n}  \frac{x^{k}}{k!}$$
$$\mathbb{R} \mathbb{C}$$
converge to $e^{x}$ when $n$ goes to infinity, for every $x$ (in  or ). What if we replace $x$ by a real or complex $n \times  n$ matrix $A$?
$$n nAk$$
$$The partial sums \sum_{k}  A^{k}and \sum_{k}  =0 still make sense, but we have to define what is$$
the limit of a sequence $of^{=0}$ matrices. $This^{k!}$ can be done in any normed vector space.

> **Definition 9.13.** Let $(E, \|\|)$ be a normed vector space. A sequence $(u_{n})_{n\in N}$ in $E$ is any function $u: \mathbb{N} \to E$. For any $v \in E$, the sequence $(u_{n})$ converges to $v$ (and $v$ is the limit of the sequence $(u_{n}))$ if for every $\epsilon  > 0$, there is some integer $N > 0$ such that
$$\|u_{n} -v\|< \epsilon for all n \ge N.$$
Often we assume that a sequence is indexed $by\mathbb{N}-{0}$, that is, its first term is $u_{1}$ rather than $u_{0}$. If the sequence $(u_{n})$ converges to $v$, then since by the triangle inequality
$$\|u_{m} -u_{n}\|\le \|u_{m} -v\|+ \|v -u_{n}\|,$$
we see that for every $\epsilon  > 0$, we can find $N > 0$ such that $\|u_{m}$ - $v\| < \epsilon /2$ and $\|u_{n}$ - $v\| < \epsilon /2$ for all $m, n \ge N$, and so
$$\|u_{m} -u_{n}\|< \epsilon for all m, n \ge N.$$
The above property is necessary for a convergent sequence, but not necessarily sufficient. For example, if $E = \mathbb{Q}$, there are sequences of rationals satisfying the above condition, but
$$whose limit is not a rational number. For example, the sequence \sum_{k}  n1 converges to e, and$$
$$the sequence \sum_{k}  n=0(-1)_{2k+1}^{k1} converges to \pi /4, but e and \pi /4 are^{=1k!} not rational (in fact, they$$
are transcendental). $However,\mathbb{R}$ is constructed $from\mathbb{Q}$ to guarantee that sequences with the above property converge, and so is $\mathbb{C}$.

> **Definition 9.14.** Given a normed vector space $(E, \|\|)$, a sequence $(u_{n})$ is a Cauchy sequence if for every $\epsilon  > 0$, there is some $N > 0$ such that
$$\|u_{m} -u_{n}\|< \epsilon for all m, n \ge N.$$
If every Cauchy sequence converges, then we say that $E$ is complete. A complete normed vector spaces is also called a Banach space.

<!-- PAGE 376 -->
A fundamental property $of\mathbb{R}$ is that it is complete. It follows immediately $that\mathbb{C}$ is also complete. If $E$ is a finite-dimensional real or complex vector space, since any two norms are equivalent, we can pick the $\ell^{\infty}$ norm, and then by picking a basis in $E$, a sequence $(u_{n})$ of vectors in $E$ converges iff the $n$ sequences of coordinates $(u_{n}^{i}) (1 \le i \le n)$ converge, so any finite-dimensional real or complex vector space is a Banach space. Let us now consider the convergence of series.
$$Definition 9.15. Given a normed vector space (E, \|\|), a series is an infinite sum \sum_{k}  \infty =0 u_{k}$$
of elements $u_{k} \in E$. We denote by $S_{n}$ the partial sum of the first $n + 1$ elements,
$$S_{n} = \sum_{k=0}^{n}  u_{k}.$$
$$Definition 9.16. We say that the series \sum_{k}  \infty  u_{k} converges to the limit v \in E if the sequence$$
$(S_{n})$ converges to $v$, i.e., given any $\epsilon  > 0,^{=0}$ there exists a positive integer $N$ such that for all $n \ge N$,
$$\|S_{n} -v\|< \epsilon .$$
In this case, we say that the series is convergent. We say that the series $\infty  u_{k}$ converges
$$absolutely\infty  \|\| \sum_{k}  =0$$
$$if the series of norms \sum_{k}  =0u_{k}is convergent.$$
$$If the series \sum_{k}  \infty =0 u_{k} converges to v, since for all m, n with m > n we have$$
$$\sum_{k=0}^{m}  u_{k} -S_{n} = \sum_{k=0}^{m}  u_{k} - \sum_{k=0}^{n}  u_{k} = \sum_{k=n+1}^{m}  u_{k},$$
$$if we let m go to infinity (with n fixed), we see that the series \sum_{k}  \infty =n+1 u_{k} converges and that$$
$$v -S_{n} = \sum_{k=n+1}^{\infty}  u_{k}.$$
There are series that are convergent but not absolutely convergent; for example, the series
$$\sum_{k=1}^{\infty}  \frac{(1)^{k-1}}{k} -$$
$$converges to \ln 2, but \sum_{k}  \infty =1\overline{k} 1 does not converge (this sum is infinite).$$
If $E$ is complete, the converse is an enormously useful result.
$$Proposition 9.19. Assume (E, \|\|) is a complete normed vector space. If a series \sum_{k}  \infty =0 u_{k}$$
is absolutely convergent, then it is convergent.
