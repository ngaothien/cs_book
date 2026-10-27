# Summary


<!-- PAGE 493 -->
where $Q$ is orthogonal and $R$ is an upper triangular matrix. This can be obtained from the Gram–Schmidt orthonormalization procedure, as we saw in Section 12.8, or better, using Householder matrices, as shown in Section 13.2. There is also the polar decomposition, which says that a real matrix $A$ can be expressed as
$$A = QS,$$
where $Q$ is orthogonal and $S$ is symmetric positive semidefinite (which means that the eigenvalues of $S$ are nonnegative). Such a decomposition is important in continuum mechanics and in robotics, since it separates stretching from rotation. Finally, there is the wonderful singular value decomposition, abbreviated as SVD, which says that a real matrix $A$ can be expressed as
$$A = V DU^{\top} ,$$
where $U$ and $V$ are orthogonal and $D$ is a diagonal matrix with nonnegative entries (see Chapter $22)$. This decomposition leads to the notion of pseudo-inverse, which has many applications in engineering (least squares solutions, etc). For an excellent presentation of all these notions, we highly recommend Strang $[176, 175]$, Golub and Van Loan $[83]$, Demmel $[48]$, Serre $[162]$, and Trefethen and Bau $[182]$. The method of least squares, invented by Gauss and Legendre around $1800$, is another great application of Euclidean geometry. Roughly speaking, the method is used to solve inconsistent linear systems Ax $= b$, where the number of equations is greater than the number of variables. Since this is generally impossible, the method of least squares consists in finding a solution $x$ minimizing the Euclidean norm $\|Ax$ - $b\|^{2}$, that is, the sum of the squares of the “errors.” It turns out that there is always a unique solution $x^{+}$ of smallest norm minimizing $\|Ax$ - $b\|^{2}$, and that it is a solution of the square system
$$A^{\top}Ax = A^{\top}b,$$
called the system of normal equations. The solution $x^{+}$ can be found either by using the QRdecomposition in terms of Householder transformations, or by using the notion of pseudoinverse of a matrix. The pseudo-inverse can be computed using the SVD decomposition. Least squares methods are used extensively in computer vision. More details on the method of least squares and pseudo-inverses can be found in Chapter $23$.

## 12.10 Summary

The main concepts and results of this chapter are listed below: $\bullet$  Bilinear forms; positive definite bilinear forms. $\bullet$  Inner products, scalar products, Euclidean spaces. $\bullet$  Quadratic form associated with a bilinear form.

<!-- PAGE 494 -->
$\bullet$  The Euclidean space $\mathbb{E}^{n}. \bullet$  The polar form of a quadratic form. $\bullet$  Gram matrix associated with an inner product. $\bullet$  The Cauchy–Schwarz inequality; the Minkowski inequality. $\bullet$  The parallelogram law. $\bullet$  Orthogonality, orthogonal complement $F^{\perp}$ ; orthonormal family. $\bullet$  The musical isomorphisms $\flat$ : $E \to E^{*}$ and $\sharp$ : $E^{*} \to E$ (when $E$ is finite-dimensional);

> **Theorem 12.6.** $\bullet$  The adjoint of a linear map (with respect to an inner product). $\bullet$  Existence of an orthonormal basis in a finite-dimensional Euclidean space (Proposition 12.9). $\bullet$  The Gram–Schmidt orthonormalization procedure (Proposition 12.10). $\bullet$  The Legendre and the Chebyshev polynomials. $\bullet$  Linear isometries (orthogonal transformations, rigid motions). $\bullet$  The orthogonal group, orthogonal matrices. $\bullet$  The matrix representing the adjoint $f^{*}$ of a linear map $f$ is the transpose of the matrix representing $f. \bullet$  The orthogonal group O(n) and the special orthogonal group SO(n). $\bullet$  QR-decomposition for invertible matrices. $\bullet$  The Hadamard inequality for arbitrary real matrices. $\bullet$  The Hadamard inequality for symmetric positive semidefinite matrices. $\bullet$  The Rodrigues formula for rotations in SO(3).
