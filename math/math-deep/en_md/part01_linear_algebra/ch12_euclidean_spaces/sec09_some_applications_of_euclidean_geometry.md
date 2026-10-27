# Some Applications of Euclidean Geometry


<!-- PAGE 492 -->

*Proof.* If det(A) $= 0$, the inequality is trivial. Otherwise, $A$ is positive definite, and by Theorem 8.10 (the Cholesky Factorization), there is a unique upper triangular matrix $B$ with positive diagonal entries such that
$$A = B^{\top}B.$$
Thus, det(A) $= det(B^{\top}B) = det(B^{\top})$ det(B) $= det(B)^{2}$. If we apply the Hadamard inequality (Proposition 12.17) to $B$, we obtain
$$1/2$$
$$\det(B) \le \prod_{j=1}^{n}  \begin{pmatrix} b_{ij}^{2} \end{pmatrix} \sum_{i=1}^{n}  .(*)$$
However, the diagonal entries $a_{jj}$ of $A = B^{\top}B$ are precisely the square norms $\|B^{j}\|_{2}^{2} =$
$$\sum_{i}  n=1 b_{ij}^{2}, so by squaring (*), we obtain$$
$$\det(A) = \det(B)^{2}\le \prod_{j=1}^{n}  \begin{pmatrix} b_{ij}^{2} \end{pmatrix} \sum_{i=1}^{n}  = \prod_{j=1}^{n}  a_{jj}.$$
If det(A) $\neq  0$ and equality holds, then $B$ must have orthogonal columns, which implies that $B$ is a diagonal matrix, and so is $A$. We derived the second Hadamard inequality (Proposition 12.18) from the first (Proposition 12.17). We leave it as an exercise to prove that the first Hadamard inequality can be deduced from the second Hadamard inequality.

## 12.9 Some Applications of Euclidean Geometry

Euclidean geometry has applications in computational geometry, in particular Voronoi diagrams and Delaunay triangulations. In turn, Voronoi diagrams have applications in motion planning (see O’Rourke $[138])$. Euclidean geometry also has applications to matrix analysis. Recall that a real $n \times  n$ matrix $A$ is symmetric if it is equal to its transpose $A^{\top}$. One of the most important properties of symmetric matrices is that they have real eigenvalues and that they can be diagonalized by an orthogonal matrix (see Chapter $17)$. This means that for every symmetric matrix $A$, there is a diagonal matrix $D$ and an orthogonal matrix $P$ such that
$$A = PDP^{\top} .$$
Even though it is not always possible to diagonalize an arbitrary matrix, there are various decompositions involving orthogonal matrices that are of great practical interest. For example, for every real matrix $A$, there is the QR-decomposition, which says that a real matrix $A$ can be expressed as
$$A = QR,$$
