# Normalized Laplacian Matrices of Graphs


<!-- PAGE 727 -->

> **Proposition 20.5.** Let $G = (V, W)$ be a weighted graph. The number $c$ of connected components $K_{1}, \dots  , K_{c}$ of the underlying graph of $G$ is equal to the dimension of the nullspace of $L$, which is equal to the multiplicity of the eigenvalue $0$. Furthermore, the nullspace of $L$ has a basis consisting of indicator vectors of the connected components of $G$, that is, vectors $(f_{1}, \dots  , f_{m})$ such that $f_{j} = 1$ iff $v_{j} \in K_{i}$ and $f_{j} = 0$ otherwise.

*Proof.* Since $L = BB^{\top}$ for the incidence matrix $B$ associated with any oriented graph obtained from $G$, and since $L$ and $B^{\top}$ have the same nullspace, by Proposition 20.1, the dimension of the nullspace of $L$ is equal to the number $c$ of connected components of $G$ and the indicator vectors of the connected components of $G$ form a basis of Ker $(L)$. Proposition 20.5 implies that if the underlying graph of $G$ is connected, then the second eigenvalue $\lambda_{2}$  of $L$ is strictly positive. Remarkably, the eigenvalue $\lambda_{2}$  contains a lot of information about the graph $G$ (assuming that $G = (V, E)$ is an undirected graph). This was first discovered by Fiedler in $1973$, and for this reason, $\lambda_{2}$  is often referred to as the Fiedler number. For more on the properties of the Fiedler number, see Godsil and Royle $[80]$ (Chapter $13)$ and Chung $[39]$. More generally, the spectrum $(0, \lambda_{2} , \dots  , \lambda_{m}$ ) of $L$ contains a lot of information about the combinatorial structure of the graph $G$. Leverage of this information is the object of spectral graph theory.

## 20.3 Normalized Laplacian Matrices of Graphs

It turns out that normalized variants of the graph Laplacian are needed, especially in applications to graph clustering. These variants make sense only if $G$ has no isolated vertices.

> **Definition 20.18.** Given a weighted graph $G = (V, W)$, a vertex $u \in V$ is isolated if it is not incident to any other vertex. This means that every row of $W$ contains some strictly positive entry. If $G$ has no isolated vertices, then the degree matrix $D$ contains positive entries, so it is invertible and $D^{-1/2}$ makes sense; namely
$$D^{-1/2}= \mathrm{diag}(d_{1}^{-1/2}, \dots  , d_{m}^{-1/2}),$$
and similarly for any real exponent $\alpha$ .

> **Definition 20.19.** Given any weighted directed graph $G = (V, W)$ with no isolated vertex and with $V = {v_{1}, \dots  , v_{m}}$, the (normalized) graph Laplacians $L_{sym}$ and $L_{rw}$ of $G$ are defined by
$$L_{sym} = D^{-1/2}LD^{-1/2}= I -D^{-1/2}WD^{-1/2}$$
$$L_{rw} = D^{-1}L = I -D^{-1}W.$$

<!-- PAGE 728 -->
Observe that the Laplacian $L_{sym} = D^{-1/2}LD^{-1/2}$ is a symmetric matrix (because $L$ and $D^{-1/2}$ are symmetric) and that
$$L_{rw} = D^{-1/2}L_{sym}D^{1/2}.$$
The reason for the notation $L_{rw}$ is that this matrix is closely related to a random walk on the graph $G$.

> **Example 20.1.** As an example, the matrices $L_{sym}$ and $L_{rw}$ associated with the graph $G_{1}$ are
$$L_{sym} = \begin{pmatrix} 1.0000 & -0.3536 & -0.4082 & 0 & 0 \\ -0.3536 & 1.0000 & -0.2887 & -0.2887 & -0.3536 \\ -0.4082 & -0.2887 & 1.0000 & -0.3333 & 0 \\ 0 & -0.2887 & -0.3333 & 1.0000 & -0.4082 \\ 0 & 0.3536 & 0 & 0.4082 & 1.0000 \end{pmatrix}$$
$$--$$
and
$$L_{rw} = \begin{pmatrix} 1.0000 & -0.5000 & -0.5000 & 0 & 0 \\ -0.2500 & 1.0000 & -0.2500 & -0.2500 & -0.2500 \\ -0.3333 & -0.3333 & 1.0000 & -0.3333 & 0 \\ 0 & -0.3333 & -0.3333 & 1.0000 & -0.3333 \\ 0 & 0.5000 & 0 & 0.5000 & 1.0000 \end{pmatrix} .$$
$$--$$
Since the unnormalized Laplacian $L$ can be written as $L = BB^{\top}$, where $B$ is the incidence matrix of any oriented graph obtained from the underlying graph of $G = (V, W)$, if we let
$$B_{sym} = D^{-1/2}B,$$
we get
$$L_{sym} = B_{sym}B_{sym}^{\top}.$$
In particular, for any singular decomposition $B_{sym} = U\Sigma V^{\top}$ of $B_{sym}$ (with $U$ an $m \times  m$ orthogonal matrix, $\Sigma$  a “diagonal” $m\times n$ matrix of singular values, and $V$ an $n\times n$ orthogonal matrix), the eigenvalues of $L_{sym}$ are the squares of the top $m$ singular values of $B_{sym}$, and the vectors in $U$ are orthonormal eigenvectors of $L_{sym}$ with respect to these eigenvalues (the squares of the top $m$ diagonal entries of $\Sigma$ ). Computing the SVD of $B_{sym}$ generally yields more accurate results than diagonalizing $L_{sym}$, especially when $L_{sym}$ has eigenvalues with high multiplicity. There are simple relationships between the eigenvalues and the eigenvectors of $L_{sym}$, and $L_{rw}$. There is also a simple relationship with the generalized eigenvalue problem Lx $= \lambda$ Dx.

> **Proposition 20.6.** Let $G = (V, W)$ be a weighted graph without isolated vertices. The graph Laplacians, $L, L_{sym}$, and $L_{rw}$ satisfy the following properties:

<!-- PAGE 729 -->
$(1)$ The matrix $L_{sym}$ is symmetric and positive semidefinite. In fact,
$$!2$$
$$x^{\top}L_{sym}x = \frac{1}{2} \sum_{i,j=1}^{m}  w_{i j}\sqrt \frac{x_{i}}{\overline{d}_{i}} - \frac{x_{j}}{p\overline{d}_{j}} for all x \in \mathbb{R}^{m}.$$
$(2)$ The normalized graph Laplacians $L_{sym}$ and $L_{rw}$ have the same spectrum $(0 = \nu_{1}  \le \nu_{2}  \le \dots  \le \nu_{m}$ ), and a vector $u \neq  0$ is an eigenvector of $L_{rw}$ for $\lambda$  iff $D^{1/2}u$ is an eigenvector of $L_{sym}$ for $\lambda$ .
$(3)$ The graph Laplacians $L$ and $L_{sym}$ are symmetric and positive semidefinite.
$(4) A$ vector $u \neq  0$ is a solution of the generalized eigenvalue problem Lu $= \lambda$ Du iff $D^{1/2}u$ is an eigenvector of $L_{sym}$ for the eigenvalue $\lambda$  iff $u$ is an eigenvector of $L_{rw}$ for the eigenvalue $\lambda$ .
$(5)$ The graph Laplacians, $L$ and $L_{rw}$ have the same nullspace. For any vector $u$, we have $u \in$ Ker $(L)$ iff $D^{1/2}u \in$ Ker $(L_{sym})$.
$(6)$ The vector $1$ is in the nullspace of $L_{rw}$, and $D^{1/2}1$ is in the nullspace of $L_{sym}$.
$(7)$ For every eigenvalue $\nu_{i}$  of the normalized graph Laplacian $L_{sym}$, we have $0 \le \nu_{i}  \le 2$. Furthermore, $\nu_{m}  = 2$ iff the underlying graph of $G$ contains a nontrivial connected bipartite component.
$(8)$ If $m \ge 2$ and if the underlying graph of $G$ is not a complete $graph,^{1}$ then $\nu_{2}  \le 1$. Furthermore the underlying graph of $G$ is a complete graph iff $\nu_{2}  =_{m-1}^{m}$.
$(9)$ If $m \ge 2$ and if the underlying graph of $G$ is connected, then $\nu_{2}  > 0$.
$(10)$ If $m \ge 2$ and if the underlying graph of $G$ has no isolated vertices, then $\nu_{m}  \ge_{m-1}^{m}$ .

*Proof.* $(1)$ We have $L_{sym} = D^{-1/2}LD^{-1/2}$, and $D^{-1/2}$ is a symmetric invertible matrix (since it is an invertible diagonal matrix). It is a well-known fact of linear algebra that if $B$ is an invertible matrix, then a matrix $S$ is symmetric, positive semidefinite iff $BSB^{\top}$ is symmetric, positive semidefinite. Since $L$ is symmetric, positive semidefinite, so is $L_{sym} = D^{-1/2}LD^{-1/2}$. The formula
$$!2$$
$$x^{\top}L_{sym}x = \frac{1}{2} \sum_{i,j=1}^{m}  w_{i j}\sqrt \frac{x_{i}}{\overline{d}_{i}} - \frac{x_{j}}{p\overline{d}_{j}} for all x \in \mathbb{R}^{m}$$
follows immediately from Proposition 20.4 by replacing $x$ by $D^{-1/2}x$, and also shows that $L_{sym}$ is positive semidefinite.
$(2)$ Since
$$L_{rw} = D^{-1/2}L_{sym}D^{1/2},$$
$\overline{1}\overline{Recall} \overline{that} \overline{an} \overline{undirected} \overline{graph} \overline{is} \overline{complete}$ if for any two distinct nodes $u, v$, there is an edge ${u, v}$.

<!-- PAGE 730 -->
the matrices $L_{sym}$ and $L_{rw}$ are similar, which implies that they have the same spectrum. In fact, since $D^{1/2}$ is invertible,
$$L_{rw}u = D^{-1}Lu = \lambda u$$
iff
$$D^{-1/2}Lu = \lambda D^{1/2}u$$
iff
$$D^{-1/2}LD^{-1/2}D^{1/2}u = L_{sym}D^{1/2}u = \lambda D^{1/2}u,$$
which shows that a vector $u \neq  0$ is an eigenvector of $L_{rw}$ for $\lambda$  iff $D^{1/2}u$ is an eigenvector of $L_{sym}$ for $\lambda$ .
$(3)$ We already know that $L$ and $L_{sym}$ are positive semidefinite.
$(4)$ Since $D^{-1/2}$ is invertible, we have
$$Lu = \lambda Du$$
iff
$$D^{-1/2}Lu = \lambda D^{1/2}u$$
iff
$$D^{-1/2}LD^{-1/2}D^{1/2}u = L_{sym}D^{1/2}u = \lambda D^{1/2}u,$$
which shows that a vector $u \neq  0$ is a solution of the generalized eigenvalue problem Lu $= \lambda$ Du iff $D^{1/2}u$ is an eigenvector of $L_{sym}$ for the eigenvalue $\lambda$ . The second part of the statement follows from $(2)$.
$(5)$ Since $D^{-1}$ is invertible, we have Lu $= 0$ iff $D^{-1}Lu = L_{rw}u = 0$. Similarly, since $D^{-1/2}$ is invertible, we have Lu $= 0$ iff $D^{-1/2}LD^{-1/2}D^{1/2}u = 0$ iff $D^{1/2}u \in$ Ker $(L_{sym})$.
$(6)$ Since L1 $= 0$, we get $L_{rw}1 = D^{-1}L1 = 0$. That $D^{1/2}1$ is in the nullspace of $L_{sym}$ follows from $(2)$. Properties (7)–(10) are proven in Chung $[39]$ (Chapter $1)$. The eigenvalues the matrices $L_{sym}$ and $L_{rw}$ from Example 20.1 are
$$0, 7257, 1.1667, 1.5, 1.6076.$$
On the other hand, the eigenvalues of the unnormalized Laplacian for $G_{1}$ are
$$0, 1.5858, 3, 4.4142, 5.$$
Remark: Observe that although the matrices $L_{sym}$ and $L_{rw}$ have the same spectrum, the matrix $L_{rw}$ is generally not symmetric, whereas $L_{sym}$ is symmetric. A version of Proposition 20.5 also holds for the graph Laplacians $L_{sym}$ and $L_{rw}$. This follows easily from the fact that Proposition 20.1 applies to the underlying graph of a weighted graph. The proof is left as an exercise.
