# Properties of the Pseudo-Inverse


<!-- PAGE 776 -->

## 23.2 Properties of the Pseudo-Inverse

We begin this section with a proposition which provides a way to calculate the pseudo-inverse of an $m \times  n$ matrix $A$ without first determining an SVD factorization.

> **Proposition 23.3.** When $A$ has full rank, the pseudo-inverse $A^{+}$ can be expressed as $A^{+} = (A^{\top}A)^{-1}A^{\top}$ when $m \ge n$, and as $A^{+} = A^{\top}(AA^{\top})^{-1}$ when $n \ge m$. In the first case $(m \ge n)$, observe that $A^{+}A =$ I, so $A^{+}$ is a left inverse of $A$; in the second case $(n \ge m)$, we have $AA^{+} =$ I, so $A^{+}$ is a right inverse of $A$.

*Proof.* If $m \ge n$ and $A$ has full rank $n$, we have
$$A = V \begin{pmatrix} \Lambda \\ 0_{m-n,n} \end{pmatrix} U^{\top}$$
with $\Lambda$  an $n \times  n$ diagonal invertible matrix (with positive entries), so
$$A^{+}= U \begin{pmatrix} \Lambda^{-1} & 0_{n,m-n} \end{pmatrix} V^{\top}.$$
We find that
$$A^{\top}A = U \begin{pmatrix} \Lambda & 0_{n,m-n} \end{pmatrix} V^{\top} V \begin{pmatrix} \Lambda \\ 0_{m-n,n} \end{pmatrix} U^{\top} = U\Lambda^{2} U^{\top} ,$$
which yields
$$(A^{\top}A)^{-1}A^{\top}= U\Lambda^{-2} U^{\top} U \begin{pmatrix} \Lambda & 0_{n,m-n} \\ rankn,then \end{pmatrix} V^{\top} = U \begin{pmatrix} \Lambda^{-1} & 0_{n,m-n} \end{pmatrix} V^{\top} = A^{+}.$$
Therefore, if $m \ge n$ and $A$ has full
$$A^{+}= (A^{\top}A)^{-1}A^{\top}.$$
If $n \ge m$ and $A$ has full rank $m$, then
$$A = V \begin{pmatrix} \Lambda & 0_{m,n-m} \\ (with \end{pmatrix} U^{\top}$$
with $\Lambda$  an $m \times  m$ diagonal invertible matrix  positive entries), so
$$A^{+}= U \begin{pmatrix} \Lambda^{-1} \\ 0_{n-m,m} \end{pmatrix} V^{\top}.$$
We find that
$$AA^{\top}= V \begin{pmatrix} \Lambda & 0_{m,n-m} \end{pmatrix} U^{\top} U \begin{pmatrix} \Lambda \\ 0_{n-m,m} \end{pmatrix} V^{\top} = V \Lambda^{2} V^{\top} ,$$
which yields
$$A^{\top}(AA^{\top})^{-1}= U \begin{pmatrix} \Lambda \\ 0_{n-m,m} \end{pmatrix} V^{\top}V \Lambda^{-2} V^{\top}= U \begin{pmatrix} \Lambda^{-1} \\ 0_{n-m,m} \end{pmatrix} V^{\top}= A^{+}.$$
Therefore, if $n \ge m$ and $A$ has full rank $m$, then $A^{+} = A^{\top}(AA^{\top})^{-1}$.

<!-- PAGE 777 -->
$$For example, if A = \begin{pmatrix} 1 & 2 \\ 2 & 3 \\ 0 & 1 \end{pmatrix} , then A has \mathrm{rank} 2 and since m \ge n, A^{+} = (A^{\top}A)^{-1}A^{\top}$$
where
$$8^{-1}$$
$$A^{+}= \begin{pmatrix} 5 \\ 8 & 14 \end{pmatrix} A^{\top}= \begin{pmatrix} 7/3 & -4/3 \\ -4/3 & 5/6 \end{pmatrix} \begin{pmatrix} 1 & 2 & 0 \\ 2 & 3 & 1 \end{pmatrix} = \begin{pmatrix} -1/3 & 2/3 & -4/3 \\ 1/3 & -1/6 & 5/6 \end{pmatrix} .$$
$$If A = \begin{pmatrix} 1 & 2 & 3 & 0 \\ 0 & 1 & 1 & -1 \end{pmatrix} , since A has \mathrm{rank} 2 and n \ge m, then A^{+}= A^{\top}(AA^{\top})^{-1}where$$
$$A^{+} = A^{\top} \begin{pmatrix} 14 \\ 5 & 3 \end{pmatrix} 5^{-1}= \begin{pmatrix} 1 & 0 \\ 2 & 1 \\ 3 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 3/17 & -5/17 \\ -5/17 & 14/17 \end{pmatrix} = \begin{pmatrix} 3/17 & -5/17 \\ 1/17 & 4/17 \\ 4/17 & -1/17 \\ 5/17 & 14/17 \end{pmatrix} .$$
$$--$$
Let $A = V \Sigma U^{\top}$ be an SVD for any $m \times  n$ matrix $A$. It is easy to check that both $AA^{+}$ and $A^{+}A$ are symmetric matrices. In fact,
$$AA^{+}= V \Sigma U^{\top}U\Sigma^{+} V^{\top}= V \Sigma \Sigma^{+} V^{\top}= V \begin{pmatrix} I_{r} & 0 \\ 0 & 0_{m-r} \end{pmatrix} V^{\top}$$
and
$$A^{+}A = U\Sigma^{+} V^{\top} V \Sigma U^{\top} = U\Sigma^{+} \Sigma U^{\top} = U \begin{pmatrix} I_{r} & 0 \\ 0 & 0_{n-r} \end{pmatrix} U^{\top} .$$
From the above expressions we immediately deduce that
$$AA^{+}A=A,$$
$$A^{+}AA^{+}=A^{+},$$
and that
$$(AA^{+})^{2}=AA^{+},$$
$$(A^{+}A)^{2}=A^{+}A,$$
so both $AA^{+}$ and $A^{+}A$ are orthogonal projections (since they are both symmetric).

> **Proposition 23.4.** The matrix $AA^{+}$ is the orthogonal projection onto the range of $A$ and $A^{+}A$ is the orthogonal projection onto $Ker(A)^{\perp} = Im(A^{\top})$, the range of $A^{\top}$.

*Proof.* Obviously, we have $range(AA^{+}) \subseteq$ range(A), and for any $y =$ Ax $\in$ range(A), since $AA^{+}A = A$, we have
$$AA^{+}y = AA^{+}Ax = Ax = y,$$

<!-- PAGE 778 -->
so the image of $AA^{+}$ is indeed the range of $A$. It is also clear that Ker(A) $\subseteq Ker(A^{+}A)$, and since $AA^{+}A = A$, we also have $Ker(A^{+}A) \subseteq$ Ker(A), and so
$$\mathrm{Ker}(A^{+}A) = \mathrm{Ker}(A).$$
Since $A^{+}A$ is symmetric, $range(A^{+}A) = range((A^{+}A)^{\top}) = Ker(A^{+}A)^{\perp} = Ker(A)^{\perp}$, as claimed.
$$\mathbb{R}^{m}$$

> **Proposition 23.5.** The set range(A) $= range(AA^{+})$ consists of all vectors $y \in$ such that
$$V^{\top} y = \begin{pmatrix} z \\ 0 \end{pmatrix} ,$$
with $z \in \mathbb{R}^{r}$.

*Proof.* Indeed, if $y =$ Ax, then
$$V^{\top} y = V^{\top} Ax = V^{\top} V \Sigma U^{\top} x = \Sigma U^{\top} x = \begin{pmatrix} \Sigma_{r} & 0 \\ 0 & 0_{m-r} \end{pmatrix} U^{\top} x = \begin{pmatrix} z \\ 0 \end{pmatrix} ,$$
where $\Sigma_{r}$  is the $r \times  r$ diagonal matrix $diag(\sigma_{1} , \dots  , \sigma_{r}$ ). Conversely, if $V^{\top} y = (_{0}^{z}$  ), then $y = V (_{0}^{z}$  ), and
$$AA^{+}y = V \begin{pmatrix} I_{r} & 0 \\ 0 & 0_{m-r} \end{pmatrix} V^{\top} y$$
$$= V \begin{pmatrix} I_{r} & 0 \\ 0 & 0_{m-r} \end{pmatrix} V^{\top} V \begin{pmatrix} z \\ 0 \end{pmatrix}$$
$$= V \begin{pmatrix} I_{r} & 0 \\ 0 & 0_{m-r} \\  \end{pmatrix} \begin{pmatrix} z \\ 0 \end{pmatrix}$$
$$= V \begin{pmatrix} z \\ 0 \end{pmatrix} = y,$$
which shows that $y$ belongs to the range of $A$. Similarly, we have the following result.
$$\mathbb{R}^{n}$$

> **Proposition 23.6.** The set $range(A^{+}A) = Ker(A)^{\perp}$ consists of all vectors $y \in$ such that
$$U^{\top} y = \begin{pmatrix} z \\ 0 \end{pmatrix} ,$$
with $z \in \mathbb{R}^{r}$.

<!-- PAGE 779 -->

*Proof.* If $y = A^{+}Au$, then
$$y = A^{+}Au = U \begin{pmatrix} I_{r} & 0 \\ 0 & 0_{n-r} \end{pmatrix} U^{\top} u = U \begin{pmatrix} z \\ 0 \end{pmatrix} ,$$
for some $z \in \mathbb{R}^{r}$. Conversely, if $U^{\top} y = (_{0}^{z}$  ), then $y = U (_{0}^{z}$ ), and so
$$A^{+}AU \begin{pmatrix} z \\ 0 \end{pmatrix} = U \begin{pmatrix} I_{r} & 0 \\ 0 & 0_{n-r} \end{pmatrix} U^{\top} U \begin{pmatrix} z \\ 0 \end{pmatrix}$$
$$= U \begin{pmatrix} I_{r} & 0 \\ 0 & 0_{n-r} \\  \end{pmatrix} \begin{pmatrix} z \\ 0 \end{pmatrix}$$
$$= U \begin{pmatrix} z \\ 0 \end{pmatrix} = y,$$
which shows that $y \in range(A^{+}A)$. Analogous results hold for complex matrices, but in this case, $V$ and $U$ are unitary matrices and $AA^{+}$ and $A^{+}A$ are Hermitian orthogonal projections. If $A$ is a normal matrix, which means that $AA^{\top} = A^{\top}A$, then there is an intimate relationship between SVD’s of $A$ and block diagonalizations of $A$. As a consequence, the pseudo-inverse of a normal matrix $A$ can be obtained directly from a block diagonalization of $A$. If $A$ is a (real) normal matrix, then we know from Theorem 17.18 that $A$ can be block diagonalized with respect to an orthogonal matrix $U$ as
$$A = U\Lambda U^{\top} ,$$
where $\Lambda$  is the (real) block diagonal matrix
$$\Lambda  = \mathrm{diag}(B_{1}, \dots  , B_{n}),$$
consisting either of $2 \times  2$ blocks of the form
$$B_{j} = \begin{pmatrix} \lambda_{j} & -\mu_{j} \\ \mu_{j} & \lambda_{j} \end{pmatrix}$$
with $\mu_{j}  \neq  0$, or of one-dimensional blocks $B_{k} = (\lambda_{k}$ ). Then we have the following proposition:

> **Proposition 23.7.** For any (real) normal matrix $A$ and any block diagonalization $A = U\Lambda U^{\top}$ of $A$ as above, the pseudo-inverse of $A$ is given by
$$A^{+}= U\Lambda^{+} U^{\top},$$
where $\Lambda^{+}$ is the pseudo-inverse of $\Lambda$ . Furthermore, if
$$\Lambda  = \begin{pmatrix} \Lambda_{r} & 0 \\ 0 & 0 \end{pmatrix} ,$$

<!-- PAGE 780 -->
where $\Lambda_{r}$  has rank $r$, then
$$\Lambda^{+} = \begin{pmatrix} \Lambda_{r}^{-1} & 0 \\ 0 & 0 \end{pmatrix} .$$

*Proof.* Assume that $B_{1}, \dots  , B_{p}$ are $2\times 2$ blocks and that $\lambda_{2p+1} , \dots  , \lambda_{n}$  are the scalar entries.
$$We know \frac{that}{\lambda_{j}^{2} + \mu_{j}^{2}} the numbers \lambda_{j}  \pm  i\mu_{j} , and the \lambda_{2p+k}  are the eigenvalues of A. Let \rho_{2j-1}  =$$
$q p \rho_{2j}  =   = \overline{det(}\overline{B}_{i}\overline{)}$ for $j = 1, \dots  , p, \rho_{j}  = |\lambda_{j}$ | for $j =$ 2p $+ 1, \dots  , r$. Multiplying $U$ by a suitable permutation matrix, we may assume that the blocks of $\Lambda$  are ordered so that $\rho_{1}  \ge \rho_{2}  \ge \cdots  \ge \rho_{r}  > 0$. Then it is easy to see that
$$AA^{\top}= A^{\top}A = U\Lambda U^{\top} U\Lambda^{\top} U^{\top} = U\Lambda \Lambda^{\top} U^{\top} ,$$
with
$$\Lambda \Lambda^{\top} = \mathrm{diag}(\rho_{1}^{2} , \dots  , \rho_{r}^{2} , 0, \dots  , 0),$$
so $\rho_{1}  \ge \rho_{2}  \ge \cdots  \ge \rho_{r}  > 0$ are the singular values $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{r}  > 0$ of $A$. Define the diagonal matrix
$$\Sigma  = \mathrm{diag}(\sigma_{1} , \dots  , \sigma_{r} , 0, \dots  , 0),$$
$$where r = \mathrm{rank}(A), \sigma_{1}  \ge \cdots  \ge \sigma_{r}  > 0 and the block diagonalp \frac{matrix}{\det(B_{i}),} \Theta  defined such that$$
the block $B_{i}$ in $\Lambda$  is replaced by the block $\sigma^{-1} B_{i}$ where $\sigma  =$  the nonzero scalar $\lambda_{j}$  is replaced $\lambda_{j} /|\lambda_{j}$ |, and a diagonal zero is replaced by $1$. Observe that $\Theta$  is an orthogonal matrix and
$$\Lambda  = \Theta \Sigma .$$
But then we can write
$$A = U\Lambda U^{\top} = U\Theta \Sigma U^{\top} ,$$
and we if let $V = U\Theta$ , since $U$ is orthogonal and $\Theta$  is also orthogonal, $V$ is also orthogonal and $A = V \Sigma U^{\top}$ is an SVD for $A$. Now we get
$$A^{+}= U\Sigma^{+} V^{\top}= U\Sigma^{+} \Theta^{\top} U^{\top}.$$
However, since $\Theta$  is an orthogonal matrix, $\Theta^{\top} = \Theta^{-1}$ , and a simple calculation shows that
$$\Sigma^{+} \Theta^{\top} = \Sigma^{+} \Theta^{-1} = \Lambda^{+} ,$$
which yields the formula
$$A^{+}= U\Lambda^{+} U^{\top}.$$
Also observe that $\Lambda_{r}$  is invertible and
$$\Lambda^{+} = \begin{pmatrix} \Lambda_{r}^{-1} & 0 \\ 0 & 0 \end{pmatrix} .$$
Therefore, the pseudo-inverse of a normal matrix can be computed directly from any block diagonalization of $A$, as claimed.
