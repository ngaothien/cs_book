# Laplacian Matrices of Graphs


<!-- PAGE 723 -->

## 20.2 Laplacian Matrices of Graphs

Let us begin with directed graphs, although as we will see, graph Laplacians are fundamentally associated with undirected graph. The key proposition below shows how given an undirected graph $G$, for any orientation $\sigma$  of $G, B^{\sigma}(B^{\sigma})^{\top}$ relates to the adjacency matrix $A$ (where $B^{\sigma}$ is the incidence matrix of the directed graph $G^{\sigma})$. We reproduce the proof in Gallier $[72]$ (see also Godsil and Royle $[80])$.

> **Proposition 20.2.** Given any undirected graph $G$, for any orientation $\sigma$  of $G$, if $B^{\sigma}is$ the incidence matrix of the directed graph $G^{\sigma}, A$ is the adjacency matrix of $G^{\sigma}$, and $D$ is the degree matrix such that $D_{i i} = d(v_{i})$, then
$$B^{\sigma}(B^{\sigma})^{\top}= D -A.$$
Consequently, $L = B^{\sigma}(B^{\sigma})^{\top}$ is independent of the orientation $\sigma$  of $G$, and D-A is symmetric and positive semidefinite; that is, the eigenvalues of $D$ - $A$ are real and nonnegative.

*Proof.* The entry $B^{\sigma}(B^{\sigma})_{i j}^{\top}$ is the inner product of the ith row $b_{i}^{\sigma}$ , and the jth row $b_{j}^{\sigma}$ of $B^{\sigma}$. If $i = j$, then as
$$+1if s(e_{k}) = v_{i}$$
$$$$
$$$$
$$b_{i k}^{\sigma} =-1if t(e_{k}) = v_{i}$$
$$0otherwise$$
$$$$
we see that $b_{i}^{\sigma} \cdot  b_{i}^{\sigma} = d(v_{i})$. If $i \neq  j$, then $b_{i}^{\sigma} \cdot  b_{j}^{\sigma}$ ̸ $= 0$ iff there is some edge $e_{k}$ with $s(e_{k}) = v_{i}$ and $t(e_{k}) = v_{j}$ or vice-versa (which are mutually exclusive cases, since $G^{\sigma}$ arises by orienting an undirected graph), in which case, $b_{i}^{\sigma} \cdot  b_{j}^{\sigma} = -1$. Therefore,
$$B^{\sigma}(B^{\sigma})^{\top}= D -A,$$
as claimed. For every $x \in \mathbb{R}^{m}$, we have
$$x^{\top}Lx = x^{\top}B^{\sigma}(B^{\sigma})^{\top}x = ((B^{\sigma})^{\top}x)^{\top}(B^{\sigma})^{\top}x =

$(B^{\sigma})^{\top}x_{2}^{2}$

$\ge$ 0,$$ since the Euclidean norm $\|\|_{2}$ is positive (definite). Therefore, $L = B^{\sigma}(B^{\sigma})^{\top}$ is positive semidefinite. It is well-known that a real symmetric matrix is positive semidefinite iff its eigenvalues are nonnegative.

> **Definition 20.15.** The matrix $L = B^{\sigma}(B^{\sigma})^{\top} = D$ - $A$ is called the (unnormalized) graph Laplacian of the graph $G^{\sigma}$. The (unnormalized) graph Laplacian of an undirected graph $G = (V, E)$ is defined by
$$L = D -A.$$

<!-- PAGE 724 -->
For example, the graph Laplacian of graph $G_{1}$ is
$$L = \begin{pmatrix} 2 & -1 & -1 & 0 & 0 \\ -1 & 4 & -1 & -1 & -1 \\ -1 & -1 & 3 & -1 & 0 \\ 0 & -1 & -1 & 3 & -1 \\ 0 & 1 & 0 & 1 & 2 \end{pmatrix} .$$
$$--$$
Observe that each row of $L$ sums to zero (because $(B^{\sigma})^{\top}1 = 0)$. Consequently, the vector $1$ is in the nullspace of $L$.
Remarks: $1$. With the unoriented version of the incidence matrix (see Definition 20.8), it can be shown that
$$BB^{\top}= D + A.$$
$2$. As pointed out by Evangelos Chatzipantazis, Proposition 20.2 in which the incidence matrix $B^{\sigma}$ is replaced by the incidence matrix $B$ of any arbitrary directed graph $G$ does not hold. The problem is that such graphs may have both edges $(v_{i}, v_{j})$ and $(v_{j}, v_{i})$ between two distinct nodes $v_{i}$ and $v_{j}$, and as a consequence, the inner product $b_{i} \cdot  b_{j} = -2$ instead of $-1$. A simple counterexample is given by the directed graph with three vertices and four edges whose incidence matrix is given by
$$B = \begin{pmatrix} 1 & -1 & 0 & -1 \\ -1 & 1 & -1 & 0 \\ 0 & 0 & 1 & 1 \end{pmatrix} .$$
We have
$$BB^{\top}= \begin{pmatrix} 3 & -2 & -1 \\ -2 & 3 & -1 \\ 1 & 1 & 2 \end{pmatrix} \neq \begin{pmatrix} 3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} = D -A.$$
$$--$$
The natural generalization of the notion of graph Laplacian to weighted graphs is this:

> **Definition 20.16.** Given any weighted graph $G = (V, W)$ with $V = {v_{1}, \dots  , v_{m}}$, the
(unnormalized) graph Laplacian L(G) of $G$ is defined by
$$L(G) = D(G) -W,$$
where D(G) $= diag(d_{1}, \dots  , d_{m})$ is the degree matrix of $G$ (a diagonal matrix), with
$$d_{i} = \sum_{j=1}^{m}  w_{i j}.$$
As usual, unless confusion arises, we write $D$ instead of D(G) and $L$ instead of L(G).

<!-- PAGE 725 -->
$$\mathbb{R}^{V} \mathbb{R}^{V}$$
The graph Laplacian can be interpreted as a linear map from to itself. For all $x \in$ , we have
$$(Lx)_{i} = \sum_{j\sim i}  w_{ij}(x_{i} -x_{j}).$$
It is clear from the equation $L = D$ - $W$ that each row of $L$ sums to $0$, so the vector $1$ is the nullspace of $L$, but it is less obvious that $L$ is positive semidefinite. One way to prove it is to generalize slightly the notion of incidence matrix.

> **Definition 20.17.** Given a weighted graph $G = (V, W)$, with $V = {v_{1}, \dots  , v_{m}}$, if ${e_{1}, \dots , e_{n}}$ are the edges of the underlying graph of $G$ (recall that ${v_{i}, v_{j}}$ is an edge of this graph iff $w_{ij} > 0)$, for any oriented graph $G^{\sigma}$ obtained by giving an orientation to the underlying graph of $G$, the incidence matrix $B^{\sigma}$ of $G^{\sigma}$ is the $m \times  n$ matrix whose entries $b_{i j}$ are given by
$$\sqrt$$
$$+\overline{w}_{ij}if s(e_{j}) = v_{i}$$
$$\sqrt$$
$$$$
$$b_{i j} =-\overline{w}_{ij}if t(e_{j}) = v_{i}$$
$$0otherwise.$$
$$$$
For example, given the weight matrix
$$W = \begin{pmatrix} 0 & 3 & 6 & 3 \\ 3 & 0 & 0 & 3 \\ 6 & 0 & 0 & 3 \\ 3 & 3 & 3 & 0 \end{pmatrix} ,$$
the incidence matrix $B$ corresponding to the orientation of the underlying graph of $W$ where an edge $(i, j)$ is oriented positively iff $i < j$ is
$$B = \begin{pmatrix} 1.7321 & 2.4495 & 1.7321 & 0 & 0 \\ -1.7321 & 0 & 0 & 1.7321 & 0 \\ 0 & -2.4495 & 0 & 0 & 1.7321 \\ 0 & 0 & 1.7321 & 1.7321 & 1.7321 \end{pmatrix} .$$
$$---$$
The reader should verify that $BB^{\top} = D$ - $W$. This is true in general, see Proposition 20.3. It is easy to see that Proposition 20.1 applies to the underlying graph of $G$. For any oriented graph $G^{\sigma}$ obtained from the underlying graph of $G$, the rank of the incidence matrix $B^{\sigma}$ is equal to m-c, where $c$ is the number of connected components of the underlying graph of $G$, and we have $(B^{\sigma})^{\top}1 = 0$. We also have the following version of Proposition 20.2 whose proof is immediately adapted.

> **Proposition 20.3.** Given any weighted graph $G = (V, W)$ with $V = {v_{1}, \dots  , v_{m}}$, if $B^{\sigma}$ is the incidence matrix of any oriented graph $G^{\sigma}$ obtained from the underlying graph of $G$ and $D$ is the degree matrix of $G$, then
$$B^{\sigma}(B^{\sigma})^{\top}= D -W = L.$$

<!-- PAGE 726 -->
Consequently, $B^{\sigma}(B^{\sigma})^{\top}$ is independent of the orientation of the underlying graph of $G$ and $L = D$ - $W$ is symmetric and positive semidefinite; that is, the eigenvalues of $L = D$ - $W$ are real and nonnegative. Another way to prove that $L$ is positive semidefinite is to evaluate the quadratic form $x^{\top}Lx$.

> **Proposition 20.4.** For any $m \times  m$ symmetric matrix $W = (w_{ij})$, if we let $L = D$ - $W$
$$where D is the degree matrix associated with W (that is, d_{i} = \sum_{j}  m=1 w_{ij}), then we have$$
$$x^{\top}Lx = \frac{1}{2} \sum_{i,j=1}^{m}  w_{i j}(x_{i} -x_{j})^{2}for all x \in \mathbb{R}^{m}.$$
Consequently, $x^{\top}Lx$ does not depend on the diagonal entries in $W$, and if $w_{i j} \ge 0$ for all $i, j \in {1, \dots  , m}$, then $L$ is positive semidefinite.

*Proof.* We have
$$x^{\top}Lx = x^{\top}Dx -x^{\top}Wx$$
$$= \sum_{i=1}^{m}  d_{i}x_{i}^{2} - \sum_{i,j=1}^{m}  w_{i j}x_{i}x_{j}$$
$$!$$
$$= \frac{1}{2} \sum_{i=1}^{m}  d_{i}x_{i}^{2} -2 \sum_{i,j=1}^{m}  w_{i j}x_{i}x_{j} + \sum_{i=1}^{m}  d_{i}x_{i}^{2}$$
$$= \frac{1}{2} \sum_{i,j=1}^{m}  w_{i j}(x_{i} -x_{j})^{2}.$$
Obviously, the quantity on the right-hand side does not depend on the diagonal entries in $W$, and if $w_{i j} \ge 0$ for all $i, j$, then this quantity is nonnegative. Proposition 20.4 immediately implies the following facts: For any weighted graph $G = (V, W), 1$. The eigenvalues $0 = \lambda_{1}  \le \lambda_{2}  \le \dots  \le \lambda_{m}$  of $L$ are real and nonnegative, and there is an orthonormal basis of eigenvectors of $L. 2$. The smallest eigenvalue $\lambda_{1}$  of $L$ is equal to $0$, and $1$ is a corresponding eigenvector. It turns out that the dimension of the nullspace of $L$ (the eigenspace of $0)$ is equal to the number of connected components of the underlying graph of $G$.
