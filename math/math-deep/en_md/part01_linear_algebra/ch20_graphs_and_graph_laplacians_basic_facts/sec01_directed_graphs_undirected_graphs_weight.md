# Directed Graphs, Undirected Graphs, Weighted Graphs


<!-- PAGE 716 -->
$R^{\top}R =$ I and the corresponding drawing is called an orthogonal drawing. This condition also rules out trivial drawings. Then we prove the main theorem about graph drawings (Theorem 21.2), which essentially says that the matrix $R$ of the desired graph drawing is constituted by the $n$ eigenvectors of $L$ associated with the smallest nonzero $n$ eigenvalues of $L$. We give a number examples of graph drawings, many of which are borrowed or adapted from Spielman $[169]$.

## 20.1 Directed Graphs, Undirected Graphs, Incidence

$$Matrices, Adjacency Matrices, Weighted Graphs$$

> **Definition 20.1.** A directed graph is a pair $G = (V, E)$, where $V = {v_{1}, \dots  , v_{m}}$ is a set of nodes or vertices, and $E \subseteq V \times  V$ is a set of ordered pairs of distinct nodes (that is, pairs $(u, v) \in V \times  V$ with $u \neq  v)$, called edges. Given any edge $e = (u, v)$, we let s(e) $= u$ be the source of $e$ and t(e) $= v$ be the target of $e$.
Remark: Since an edge is a pair $(u, v)$ with $u \neq  v$, self-loops are not allowed. Also, there is at most one edge from a node $u$ to a node $v$. Such graphs are sometimes called simple graphs. An example of a directed graph is shown in Figure 20.2.
$$e_{1}$$
$$v_{1}v_{2}$$
$$e_{5}$$
$$e_{2}e_{3}e_{4}$$
$$v_{5}$$
$$e_{6}$$
$$v_{3}v_{4}$$
$$\overline{e}_{7}$$
$$Figure 20.2: Graph G_{1}.$$

> **Definition 20.2.** For every node $v \in V$ , the degree d(v) of $v$ is the number of edges leaving or entering $v$:
$$d(v) = |{u \in V | (v, u) \in E or (u, v) \in E}|.$$
We abbreviate $d(v_{i})$ as $d_{i}$. The degree matrix, D(G), is the diagonal matrix
$$D(G) = \mathrm{diag}(d_{1}, \dots  , d_{m}).$$

<!-- PAGE 717 -->
For example, for graph $G_{1}$, we have
$$D(G_{1}) = \begin{pmatrix} 2 & 0 & 0 & 0 & 0 \\ 0 & 4 & 0 & 0 & 0 \\ 0 & 0 & 3 & 0 & 0 \\ 0 & 0 & 0 & 3 & 0 \\ 0 & 0 & 0 & 0 & 2 \end{pmatrix} .$$
Unless confusion arises, we write $D$ instead of D(G).

> **Definition 20.3.** Given a directed graph $G = (V, E)$, for any two nodes $u, v \in V$ , a path from $u$ to $v$ is a sequence of nodes $(v_{0}, v_{1}, \dots  , v_{k})$ such that $v_{0} = u, v_{k} = v$, and $(v_{i}, v_{i+1})$ is an edge in $E$ for all $i$ with $0 \le i \le k$ - $1$. The integer $k$ is the length of the path. A path is closed if $u = v$. The graph $G$ is strongly connected if for any two distinct nodes $u, v \in V$ , there is a path from $u$ to $v$ and there is a path from $v$ to $u$.
Remark: The terminology walk is often used instead of path, the word path being reserved to the case where the nodes $v_{i}$ are all distinct, except that $v_{0} = v_{k}$ when the path is closed. The binary relation on $V \times  V$ defined so that $u$ and $v$ are related iff there is a path from $u$ to $v$ and there is a path from $v$ to $u$ is an equivalence relation whose equivalence classes are called the strongly connected components of $G$.

> **Definition 20.4.** Given a directed graph $G = (V, E)$, with $V = {v_{1}, \dots  , v_{m}}$, if $E = {e_{1}, \dots  , e_{n}}$, then the incidence matrix B(G) of $G$ is the $m \times  n$ matrix whose entries $b_{i j}$ are given by
$$+1if s(e_{j}) = v_{i}$$
$$$$
$$$$
$$b_{i j} =-1if t(e_{j}) = v_{i}$$
$$0otherwise.$$
$$$$
Here is the incidence matrix of the graph $G_{1}$:
$$B = \begin{pmatrix} 1 & 1 & 0 & 0 & 0 & 0 & 0 \\ -1 & 0 & -1 & -1 & 1 & 0 & 0 \\ 0 & -1 & 1 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 1 & 0 & -1 & -1 \\ 0 & 0 & 0 & 0 & 1 & 1 & 0 \end{pmatrix} .$$
$$-$$
Observe that every column of an incidence matrix contains exactly two nonzero entries, $+1$ and $-1$. Again, unless confusion arises, we write $B$ instead of B(G). When a directed graph has $m$ nodes $v_{1}, \dots  , v_{m}$ and $n$ edges $e_{1}, \dots  , e_{n}$, a vector $x \in \mathbb{R}^{m}$ can be viewed as a function $x: V \to \mathbb{R}$ assigning the value $x_{i}$ to the node $v_{i}$. Under this
$$\mathbb{R}^{m}  \mathbb{R}^{V} \mathbb{R}^{n}$$
interpretation, is viewed as . Similarly, a vector $y \in$ can be viewed as a function

<!-- PAGE 718 -->
$$a$$
$$v_{1}v_{2}$$
$$e$$
$$bcdv_{5}$$
$$f$$
$$v_{3}v_{4}$$
$$g$$
$$Figure 20.3: The undirected graph G_{2}.$$
in $\mathbb{R}^{E}$. This point of view is often useful. For example, the incidence matrix $B$ can be
$$\mathbb{R}^{E}  \mathbb{R}^{V}$$
interpreted as a linear map from to , the boundary map, and $B^{\top}$ can be interpreted
$$\mathbb{R}^{V}  \mathbb{R}^{E}$$
as a linear map from to , the coboundary map.
Remark: Some authors adopt the opposite convention of sign in defining the incidence matrix, which means that their incidence matrix is $-B$. Undirected graphs are obtained from directed graphs by forgetting the orientation of the edges.

> **Definition 20.5.** A graph (or undirected graph) is a pair $G = (V, E)$, where $V = {v_{1}, \dots  , v_{m}}$ is a set of nodes or vertices, and $E$ is a set of two-element subsets of $V$ (that is, subsets ${u, v}$, with $u, v \in V$ and $u \neq  v)$, called edges.
Remark: Since an edge is a set ${u, v}$, we have $u \neq  v$, so self-loops are not allowed. Also, for every set of nodes ${u, v}$, there is at most one edge between $u$ and $v$. As in the case of directed graphs, such graphs are sometimes called simple graphs. An example of a graph is shown in Figure 20.3.

> **Definition 20.6.** For every node $v \in V$ , the degree d(v) of $v$ is the number of edges incident to $v$:
$$d(v) = |{u \in V | {u, v} \in E}|.$$
The degree matrix D(G) (or simply, $D)$ is defined as in Definition 20.2.

> **Definition 20.7.** Given a (undirected) graph $G = (V, E)$, for any two nodes $u, v \in V$ , a path from $u$ to $v$ is a sequence of nodes $(v_{0}, v_{1}, \dots  , v_{k})$ such that $v_{0} = u, v_{k} = v$, and ${v_{i}, v_{i+1}}$ is an edge in $E$ for all $i$ with $0 \le i \le k$ - $1$. The integer $k$ is the length of the path. A path is closed if $u = v$. The graph $G$ is connected if for any two distinct nodes $u, v \in V$ , there is a path from $u$ to $v$.

<!-- PAGE 719 -->
Remark: The terminology walk or chain is often used instead of path, the word path being reserved to the case where the nodes $v_{i}$ are all distinct, except that $v_{0} = v_{k}$ when the path is closed. The binary relation on $V \times V$ defined so that $u$ and $v$ are related iff there is a path from $u$ to $v$ is an equivalence relation whose equivalence classes are called the connected components of $G$. The notion of incidence matrix for an undirected graph is not as useful as in the case of directed graphs

> **Definition 20.8.** Given a graph $G = (V, E)$, with $V = {v_{1}, \dots  , v_{m}}$, if $E = {e_{1}, \dots  , e_{n}}$, then the incidence matrix B(G) of $G$ is the $m \times  n$ matrix whose entries $b_{i j}$ are given by
$$($$
$$+1if e_{j} = {v_{i}, v_{k}} for some k$$
$$b_{i j} =$$
$$0otherwise.$$
Unlike the case of directed graphs, the entries in the incidence matrix of a graph (undirected) are nonnegative. We usually write $B$ instead of B(G).

> **Definition 20.9.** If $G = (V, E)$ is a directed or an undirected graph, given a node $u \in V$ , any node $v \in V$ such that there is an edge $(u, v)$ in the directed case or ${u, v}$ in the undirected case is called adjacent to $u$, and we often use the notation
$$u \sim v.$$
Observe that the binary relation $\sim$ is symmetric when $G$ is an undirected graph, but in general it is not symmetric when $G$ is a directed graph. The notion of adjacency matrix is basically the same for directed or undirected graphs.

> **Definition 20.10.** Given a directed or undirected graph $G = (V, E)$, with $V = {v_{1}, \dots  , v_{m}}$, the adjacency matrix A(G) of $G$ is the symmetric $m \times  m$ matrix $(a_{i j})$ such that
$(1)$ If $G$ is directed, then
$$($$
$$1if there is some edge (v_{i}, v_{j}) \in E or some edge (v_{j}, v_{i}) \in E$$
$$a_{i j} =$$
$$0otherwise.$$
$(2)$ Else if $G$ is undirected, then
$$($$
$$1if there is some edge {v_{i}, v_{j}} \in E$$
$$a_{i j} =$$
$$0otherwise.$$

<!-- PAGE 720 -->
As usual, unless confusion arises, we write $A$ instead of A(G). Here is the adjacency matrix of both graphs $G_{1}$ and $G_{2}$:
$$A = \begin{pmatrix} 0 & 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 1 & 1 \\ 1 & 1 & 0 & 1 & 0 \\ 0 & 1 & 1 & 0 & 1 \\ 0 & 1 & 0 & 1 & 0 \end{pmatrix} .$$
If $G = (V, E)$ is an undirected graph, the adjacency matrix $A$ of $G$ can be viewed as a
$$\mathbb{R}^{V}  \mathbb{R}^{V} \mathbb{R}^{m}$$
linear map from to , such that for all $x \in$ , we have
$$(Ax)_{i} = \sum_{j\sim i}  x_{j};$$
that is, the value of Ax at $v_{i}$ is the sum of the values of $x$ at the nodes $v_{j}$ adjacent to $v_{i}$. The adjacency matrix can be viewed as a diffusion operator. This observation yields a geometric
$$\mathbb{R}^{m}$$
interpretation of what it means for a vector $x \in$ to be an eigenvector of $A$ associated with some eigenvalue $\lambda$ ; we must have
$$\lambda x_{i} = \sum_{j\sim i}  x_{j},i = 1, \dots  , m,$$
which means that the the sum of the values of $x$ assigned to the nodes $v_{j}$ adjacent to $v_{i}$ is equal to $\lambda$  times the value of $x$ at $v_{i}$.

> **Definition 20.11.** Given any undirected graph $G = (V, E)$, an orientation of $G$ is a function $\sigma$ : $E \to V \times  V$ assigning a source and a target to every edge in $E$, which means that for every edge ${u, v} \in E$, either $\sigma ({u, v}) = (u, v)$ or $\sigma ({u, v}) = (v, u)$. The oriented graph $G^{\sigma}$ obtained from $G$ by applying the orientation $\sigma$  is the directed graph $G^{\sigma} = (V, E^{\sigma})$, with $E^{\sigma} = \sigma (E)$. The following result shows how the number of connected components of an undirected graph is related to the rank of the incidence matrix of any oriented graph obtained from $G$.

> **Proposition 20.1.** Let $G = (V, E)$ be any undirected graph with $m$ vertices, $n$ edges, and $c$ connected components. For any orientation $\sigma$  of $G$, if $B$ is the incidence matrix of the oriented graph $G^{\sigma}$, then $c =$ dim(Ker $(B^{\top}))$, and $B$ has rank $m$ - $c$. Furthermore, the nullspace of $B^{\top}$ has a basis consisting of indicator vectors of the connected components of $G$; that is, vectors $(z_{1}, \dots  , z_{m})$ such that $z_{j} = 1$ iff $v_{j}$ is in the ith component $K_{i}$ of $G$, and $z_{j} = 0$ otherwise.

*Proof.* (After Godsil and Royle $[80]$, Section 8.3). The fact that rank(B) $= m$ - $c$ will be proved last.
$$\mathbb{R}^{m}$$
Let us prove that the kernel of $B^{\top}$ has dimension $c$. A vector $z \in$ belongs to the kernel of $B^{\top}$ iff $B^{\top}z = 0$ iff $z^{\top}B = 0$. In view of the definition of $B$, for every edge ${v_{i}, v_{j}}$

<!-- PAGE 721 -->
of $G$, the column of $B$ corresponding to the oriented edge $\sigma ({v_{i}, v_{j}})$ has zero entries except for $a +1$ and $a -1$ in position $i$ and position $j$ or vice-versa, so we have
$$z_{i} = z_{j}.$$
An easy induction on the length of the path shows that if there is a path from $v_{i}$ to $v_{j}$ in $G$ (unoriented), then $z_{i} = z_{j}$. Therefore, $z$ has a constant value on any connected component of $G$. It follows that every vector $z \in$ Ker $(B^{\top})$ can be written uniquely as a linear combination
$$z = \lambda_{1} z^{1}+ \cdots  + \lambda_{c} z^{c},$$
where the vector $z^{i}$ corresponds to the ith connected component $K_{i}$ of $G$ and is defined such that
$$($$
$$1iffv_{j} \in K_{i}$$
$$z_{j}^{i} =$$
$$0otherwise.$$
This shows that dim(Ker $(B^{\top})) = c$, and that Ker $(B^{\top})$ has a basis consisting of indicator vectors. Since $B^{\top}$ is a $n \times  m$ matrix, we have
$$m = \dim(\mathrm{Ker} (B^{\top})) + \mathrm{rank}(B^{\top}),$$
and since we just proved that dim(Ker $(B^{\top})) = c$, we obtain $rank(B^{\top}) = m$ - $c$. Since $B$ and $B^{\top}$ have the same rank, rank(B) $= m$ - $c$, as claimed.

> **Definition 20.12.** Following common practice, we denote by $1$ the (column) vector (of dimension $m)$ whose components are all equal to $1$. Since every column of $B$ contains a single $+1$ and a single $-1$, the rows of $B^{\top}$ sum to zero, which can be expressed as
$$B^{\top}1 = 0.$$
According to Proposition 20.1, the graph $G$ is connected iff $B$ has rank m-1 iff the nullspace of $B^{\top}$ is the one-dimensional space spanned by $1$. In many applications, the notion of graph needs to be generalized to capture the intuitive idea that two nodes $u$ and $v$ are linked with a degree of certainty (or strength). Thus, we assign a nonnegative weight $w_{i j}$ to an edge ${v_{i}, v_{j}}$; the smaller $w_{i j}$ is, the weaker is the link (or similarity) between $v_{i}$ and $v_{j}$, and the greater $w_{i j}$ is, the stronger is the link (or similarity) between $v_{i}$ and $v_{j}$.

> **Definition 20.13.** A weighted graph is a pair $G = (V, W)$, where $V = {v_{1}, \dots  , v_{m}}$ is a set of nodes or vertices, and $W$ is a symmetric matrix called the weight matrix, such that $w_{i j} \ge 0$ for all $i, j \in {1, \dots  , m}$, and $w_{i i} = 0$ for $i = 1, \dots  , m$. We say that a set ${v_{i}, v_{j}}$ is an edge iff $w_{i j} > 0$. The corresponding (undirected) graph $(V, E)$ with $E = {{v_{i}, v_{j}}$ | $w_{i j} > 0}$, is called the underlying graph of $G$.

<!-- PAGE 722 -->
Remark: Since $w_{i i} = 0$, these graphs have no self-loops. We can think of the matrix $W$ as a generalized adjacency matrix. The case where $w_{i j} \in {0, 1}$ is equivalent to the notion of a graph as in Definition 20.5. We can think of the weight $w_{i j}$ of an edge ${v_{i}, v_{j}}$ as a degree of similarity (or affinity) in an image, or a cost in a network. An example of a weighted graph is shown in Figure 20.4. The thickness of an edge corresponds to the magnitude of its weight.
$$Figure 20.4: A weighted graph.$$

> **Definition 20.14.** Given a weighted graph $G = (V, W)$, for every node $v_{i} \in V$ , the degree $d(v_{i})$ of $v_{i}$ is the sum of the weights of the edges adjacent to $v_{i}$:
$$d(v_{i}) = \sum_{j=1}^{m}  w_{i j}.$$
Note that in the above sum, only nodes $v_{j}$ such that there is an edge ${v_{i}, v_{j}}$ have a nonzero contribution. Such nodes are said to be adjacent to $v_{i}$, and we write $v_{i} \sim v_{j}$. The degree matrix D(G) (or simply, $D)$ is defined as before, namely by D(G) $= diag(d(v_{1}), \dots  , d(v_{m}))$.
$$\mathbb{R}^{V} \mathbb{R}^{m}$$
The weight matrix $W$ can be viewed as a linear map from to itself. For all $x \in$ , we have
$$(Wx)_{i} = \sum_{j\sim i}  w_{ij}x_{j};$$
that is, the value of Wx at $v_{i}$ is the weighted sum of the values of $x$ at the nodes $v_{j}$ adjacent to $v_{i}$. Observe that W1 is the (column) vector $(d(v_{1}), \dots  , d(v_{m}))$ consisting of the degrees of the nodes of the graph. We now define the most important concept of this chapter: the Laplacian matrix of a graph. Actually, as we will see, it comes in several flavors.
