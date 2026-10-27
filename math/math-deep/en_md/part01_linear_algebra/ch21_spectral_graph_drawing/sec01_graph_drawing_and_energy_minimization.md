# Graph Drawing and Energy Minimization


<!-- PAGE 737 -->
Chapter $21$ Spectral Graph Drawing

## 21.1 Graph Drawing and Energy Minimization

Let $G = (V, E)$ be some undirected graph. It is often desirable to draw a graph, usually in the plane but possibly in 3D, and it turns out that the graph Laplacian can be used to design surprisingly good methods. Say |V | $= m$. The idea is to assign a point $\rho (v_{i})$ in $\mathbb{R}^{n}$ to the vertex $v_{i} \in V$ , for every $v_{i} \in V$ , and to draw a line segment between the points $\rho (v_{i})$ and $\rho (v_{j})$ iff there is an edge ${v_{i}, v_{j}}$.

> **Definition 21.1.** Let $G = (V, E)$ be some undirected graph with $m$ vertices. A graph drawing is a function $\rho$ : $V \to \mathbb{R}^{n}$, for some $n \ge 1$. The matrix of a graph drawing $\rho$  (in $\mathbb{R}^{n})$ is a $m \times  n$ matrix $R$ whose ith row consists of the row vector $\rho (v_{i})$ corresponding to the point representing $v_{i}$ in $\mathbb{R}^{n}$. For a graph drawing to be useful we want $n \le m$; in fact $n$ should be much smaller than $m$, typically $n = 2$ or $n = 3$.

> **Definition 21.2.** A graph drawing is balanced iff the sum of the entries of every column of the matrix of the graph drawing is zero, that is,
$$1^{\top}R = 0.$$
If a graph drawing is not balanced, it can be made balanced by a suitable translation. We may also assume that the columns of $R$ are linearly independent, since any basis of the column space also determines the drawing. Thus, from now on, we may assume that $n \le m$.
$$\mathbb{R}^{n}$$
Remark: $A$ graph drawing $\rho$ : $V \to$ is not required to be injective, which may result in degenerate drawings where distinct vertices are drawn as the same point. For this reason, we prefer not to use the terminology graph embedding, which is often used in the literature. This is because in differential geometry, an embedding always refers to an injective map. The term graph immersion would be more appropriate.
$$737$$

<!-- PAGE 738 -->
As explained in Godsil and Royle $[80]$, we can imagine building a physical model of $G$ by connecting adjacent vertices (in $\mathbb{R}^{n})$ by identical springs. Then it is natural to consider a representation to be better if it requires the springs to be less extended. We can formalize this by defining the energy of a drawing $R$ by
$$\mathcal{E}(R) = \sum_{vi,vj}\in}  \|\rho (v_{i}) -\rho (v_{j})\|^{2},$$
$${E$$
where $\rho (v_{i})$ is the ith row of $R$ and $\|\rho (v_{i})$ - $\rho (v_{j})\|^{2}$ is the square of the Euclidean length of the line segment joining $\rho (v_{i})$ and $\rho (v_{j})$. Then, “good drawings” are drawings that minimize the energy $function\mathcal{E}$. Of course, the trivial representation corresponding to the zero matrix is optimum, so we need to impose extra constraints to rule out the trivial solution. We can consider the more general situation where the springs are not necessarily identical. This can be modeled by a symmetric weight (or stiffness) matrix $W = (w_{ij})$, with $w_{ij} \ge 0$. Then our energy function becomes
$$\mathcal{E}(R) = \sum_{vi,vj}\in}  w_{ij} \|\rho (v_{i}) -\rho (v_{j})\|^{2}.$$
$${E$$
It turns out that this function can be expressed in terms of the Laplacian $L = D$ - $W$. The following proposition is shown in Godsil and Royle $[80]$. We give a slightly more direct proof.

> **Proposition 21.1.** Let $G = (V, W)$ be a weighted graph, with |V | $= m$ and $W$ an $m \times  m$
$$\mathbb{R}^{n}$$
symmetric matrix, and let $R$ be the matrix of a graph drawing $\rho$  of $G$ in (a $m\times n$ matrix). If $L = D$ - $W$ is the unnormalized Laplacian matrix associated with $W$, then
$$\mathcal{E}(R) = \mathrm{tr}(R^{\top}LR).$$

*Proof.* Since $\rho (v_{i})$ is the ith row of $R$ (and $\rho (v_{j})$ is the jth row of $R)$, if we denote the kth column of $R$ by $R^{k}$, using Proposition 20.4, we have
$$\mathcal{E}(R) = \sum_{vi,vj}\in}  w_{ij} \|\rho (v_{i}) -\rho (v_{j})\|^{2}$$
$$E$$
$$= \sum_{k=1{}^{{n}  \sum_{vi,vj}\in}  w_{ij}(R_{ik} -R_{jk})^{2}$$
$$E$$
$$= \sum_{k=1}^{n}  \frac{1}{2} \sum_{i,j=1}^{m}  w_{ij}(R_{ik} -R_{jk})^{2}$$
$$= \sum_{k=1}^{n}  (R^{k})^{\top}LR^{k} = \mathrm{tr}(R^{\top}LR),$$
as claimed.

<!-- PAGE 739 -->
Since the matrix $R^{\top}LR$ is symmetric, it has real eigenvalues. Actually, since $L$ is positive semidefinite, so is $R^{\top}LR$. Then the trace of $R^{\top}LR$ is equal to the sum of its positive eigenvalues, and this is the energy $\mathcal{E}(R)$ of the graph drawing. If $R$ is the matrix of a graph drawing in $\mathbb{R}^{n}$, then for any $n \times  n$ invertible matrix $M$, the map that assigns $\rho (v_{i})M$ to $v_{i}$ is another graph drawing of $G$, and these two drawings convey the same amount of information. From this point of view, a graph drawing is determined by the column space of $R$. Therefore, it is reasonable to assume that the columns of $R$ are pairwise orthogonal and that they have unit length. Such a matrix satisfies the equation $R^{\top}R =$ I.

> **Definition 21.3.** If the matrix $R$ of a graph drawing satisfies the equation $R^{\top}R =$ I, then the corresponding drawing is called an orthogonal graph drawing. This above condition also rules out trivial drawings. The following result tells us how to find minimum energy orthogonal balanced graph drawings, provided the graph is connected. Recall that
$$L1 = 0,$$
as we already observed.

> **Theorem 21.2.** Let $G = (V, W)$ be a weighted graph with |V | $= m$. If $L = D$ - $W$ is the
(unnormalized) Laplacian of $G$, and if the eigenvalues of $L$ are $0 = \lambda_{1}  < \lambda_{2}  \le \lambda_{3}  \le \dots  \le \lambda_{m}$ ,
$$\mathbb{R}^{n}$$
then the minimal energy of any balanced orthogonal graph drawing of $G$ in is equal to $\lambda_{2} +\cdots +\lambda_{n+1}$  (in particular, this implies that $n < m)$. The $m\times n$ matrix $R$ consisting of any unit eigenvectors $u_{2}, \dots  , u_{n+1}$ associated with $\lambda_{2}  \le \dots  \le \lambda_{n+1}$  yields a balanced orthogonal graph drawing of minimal energy; it satisfies the condition $R^{\top}R =$ I.

*Proof.* We present the proof given in Godsil and Royle $[80]$ (Section 13.4, Theorem 13.4.1). The key point is that the sum of the $n$ smallest eigenvalues of $L$ is a lower bound for $tr(R^{\top}LR)$. This can be shown using a Rayleigh ratio argument; see Proposition 17.25 (the Poincar´e separation theorem). Then any $n$ eigenvectors $(u_{1}, \dots  , u_{n})$ associated with $\lambda_{1} , \dots  , \lambda_{n}$  achieve this bound. Because the first eigenvalue of $L$ is $\lambda_{1}  = 0$ and because
$$\sqrt$$
we are assuming that $\lambda_{2}  > 0$, we have $u_{1} = 1/ \overline{m}$. Since the $u_{j}$ are pairwise orthogonal
$$\sqrt$$
for $i = 2, \dots  , n$ and since $u_{i}$ is orthogonal to $u_{1} = 1/ \overline{m}$, the entries in $u_{i}$ add up to $0$. Consequently, for any $\ell$ with $2 \le \ell \le n$, by deleting $u_{1}$ and using $(u_{2}, \dots  , u_{\ell})$, we obtain a
$$\mathbb{R}^{\ell-1}$$
balanced orthogonal graph drawing in with the same energy as the orthogonal graph drawing in $\mathbb{R}^{\ell}$ using $(u_{1}, u_{2}, \dots  , u_{\ell})$. Conversely, from any balanced orthogonal drawing in $\mathbb{R}^{\ell-1}  \mathbb{R}^{\ell}$ using $(u_{2}, \dots  , u_{\ell})$, we obtain an orthogonal graph drawing in using $(u_{1}, u_{2}, \dots  , u_{\ell})$ with the same energy. Therefore, the minimum energy of a balanced orthogonal graph
$$\mathbb{R}^{n} \mathbb{R}^{n+1}$$
drawing in is equal to the minimum energy of an orthogonal graph drawing in , and this minimum is $\lambda_{2}  + \cdots  + \lambda_{n+1}$ . Since $1$ spans the nullspace of $L$, using $u_{1}$ (which belongs to Ker $L)$ as one of the vectors in $R$ would have the effect that all points representing vertices of $G$ would have the same
