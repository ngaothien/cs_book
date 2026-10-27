# Summary


<!-- PAGE 589 -->
If $B$ is a skew symmetric matrix, since tr(B) $= 0$, we deduce that $det(e^{B}) = e^{0} = 1$. This allows us to obtain the following result. Recall that the (real) vector space of skew symmetric matrices is denoted by $\mathfrak{so}(n)$.

> **Proposition 15.15.** For every skew symmetric matrix $B \in \mathfrak{so}(n)$, we have $e^{B} \in$ SO(n), that is, $e^{B}$ is a rotation.

*Proof.* By Proposition 9.24, $e^{B}$ is an orthogonal matrix. Since tr(B) $= 0$, we deduce that $det(e^{B}) = e^{0} = 1$. Therefore, $e^{B} \in$ SO(n). Proposition 15.15 shows that the map $B \mapsto e^{B}$ is a map exp: $\mathfrak{so}(n) \to$ SO(n). It is not injective, but it can be shown (using one of the spectral theorems) that it is surjective. If $B$ is a (real) symmetric matrix, then
$$(e^{B})^{\top}= e^{B\top}= e^{B},$$
so $e^{B}$ is also symmetric. Since the eigenvalues $\lambda_{1} , \dots  , \lambda_{n}$  of $B$ are real, by Proposition 15.13, since the eigenvalues of $e^{B}$ are $e^{\lambda1}, \dots  , e^{\lambda n}$ and the $\lambda_{i}$  are real, we have $e^{\lambda i} > 0$ for $i = 1, \dots  , n$, which implies that $e^{B}$ is symmetric positive definite. In fact, it can be shown that for every symmetric positive definite matrix $A$, there is a unique symmetric matrix $B$ such that $A = e^{B}$; see Gallier $[73]$.

## 15.6 Summary

The main concepts and results of this chapter are listed below: $\bullet$  Diagonal matrix. $\bullet$  Eigenvalues, eigenvectors; the eigenspace associated with an eigenvalue. $\bullet$  Characteristic polynomial. $\bullet$  Trace. $\bullet$  Algebraic and geometric multiplicity. $\bullet$  Eigenspaces associated with distinct eigenvalues form a direct sum (Proposition 15.3). $\bullet$  Reduction of a matrix to an upper-triangular matrix. $\bullet$  Schur decomposition. $\bullet$  The Gershgorin’s discs can be used to locate the eigenvalues of a complex matrix; see Theorems 15.9 and 15.10. $\bullet$  The conditioning of eigenvalue problems. $\bullet$  Eigenvalues of the matrix exponential. The formula $det(e^{A}) = e^{tr(A)}$.
