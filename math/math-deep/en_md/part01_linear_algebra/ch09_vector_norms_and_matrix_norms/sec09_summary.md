# Summary


<!-- PAGE 380 -->
Thus, we see that the exponential of a $2 \times  2$ skew-symmetric matrix is a rotation matrix. This property generalizes to any dimension. An explicit formula when $n = 3$ (the Rodrigues’ formula) is given in Section 12.7.

> **Proposition 9.24.** If $B$ is an $n \times  n$ (real) skew symmetric matrix, that is, $B^{\top} = -B$, then $Q = e^{B}$ is an orthogonal matrix, that is
$$Q^{\top}Q = QQ^{\top}= I.$$

*Proof.* Since $B^{\top} = -B$, we have
$$Q^{\top}= (e^{B})^{\top}= e^{B\top}= e^{-B}.$$
Since $B$ and $-B$ commute, we have
$$Q^{\top}Q = e^{-B}e^{B}= e^{-B+B}= e^{0}= I.$$
Similarly,
$$QQ^{\top}= e^{B}e^{-B}= e^{B-B}= e^{0}= I,$$
which concludes the proof. It can also be shown that det(Q) $= det(e^{B}) = 1$, but this requires a better understanding of the eigenvalues of $e^{B}$ (see Section 15.5). Furthermore, for every $n \times  n$ rotation matrix $Q$ (an orthogonal matrix $Q$ such that det(Q) $= 1)$, there is a skew symmetric matrix $B$ such that $Q = e^{B}$. This is a fundamental property which has applications in robotics for $n = 3$. All familiar series have matrix analogs. For example, if $\|A\| < 1$ (where $\|\|$ is an operator
$$\infty$$
$$norm), then the series \sum_{k}  =0 A^{k}converges absolutely, and it can be shown that its limit is$$
(I - $A)^{-1}$. Another interesting series is the logarithm. For any $n \times  n$ complex matrix $A$, if $\|A\| < 1$ (where $\|\|$ is an operator norm), then the series
$$\log(I + A) = \sum_{k=1}^{\infty}  (-1)^{k+1} \frac{A^{k}}{k}$$
converges absolutely.

## 9.9 Summary

The main concepts and results of this chapter are listed below: $\bullet$  Norms and normed vector spaces. $\bullet$  The triangle inequality.

<!-- PAGE 381 -->
$\bullet$  The Euclidean norm; the $\ell^{p}$ -norms. $\bullet$  H¨older’s inequality; the Cauchy–Schwarz inequality; Minkowski’s inequality. $\bullet$  Hermitian inner product and Euclidean inner product. $\bullet$  Equivalent norms. $\bullet$  All norms on a finite-dimensional vector space are equivalent (Theorem 9.6). $\bullet$  Matrix norms. $\bullet$  Hermitian, symmetric and normal matrices. Orthogonal and unitary matrices. $\bullet$  The trace of a matrix. $\bullet$  Eigenvalues and eigenvectors of a matrix. $\bullet$  The characteristic polynomial of a matrix. $\bullet$  The spectral radius $\rho (A)$ of a matrix $A. \bullet$  The Frobenius norm. $\bullet$  The Frobenius norm is a unitarily invariant matrix norm. $\bullet$  Bounded linear maps. $\bullet$  Subordinate matrix norms. $\bullet$  Characterization of the subordinate matrix norms for the vector norms $\|\|_{1} , \|\|_{2}$, and $\|\|_{\infty}. \bullet$  The spectral norm. $\bullet$  For every matrix $A \in M_{n}(\mathbb{C})$ and for every $\epsilon  > 0$, there is some subordinate matrix norm $\|\|$ such that $\|A\|\le \rho (A) + \epsilon$ . $\bullet$  Condition numbers of matrices. $\bullet$  Perturbation analysis of linear systems. $\bullet$  The singular value decomposition (SVD). $\bullet$  Properties of conditions numbers. Characterization of $cond_{2}(A)$ in terms of the largest and smallest singular values of $A. \bullet$  The Hilbert matrix: a very badly conditioned matrix. $\bullet$  Solving inconsistent linear systems by the method of least-squares; linear programming.
