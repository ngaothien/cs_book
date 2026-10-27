# Permanents


<!-- PAGE 247 -->
and since $B$ is matrix whose entries are polynomials in K[X], it makes sense to multiply on
$$e$$
the left by $B$ and we get
$$e$$
$$Be \cdot  B \cdot \begin{pmatrix} e_{1} \\ e_{2} \\ \vdots \\ e_{n} \end{pmatrix} = (BB e) \cdot \begin{pmatrix} e_{1} \\ e_{2} \\ \vdots \\ e_{n} \end{pmatrix} = P_{A}I \cdot \begin{pmatrix} e_{1} \\ e_{2} \\ \vdots \\ e_{n} \end{pmatrix} = Be \cdot \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix} ;$$
that is,
$$P_{A} \cdot  e_{j} = 0,j = 1, \dots  , n,$$
which proves that $P_{A}(f) = 0$, as claimed. If $K$ is a field, then the characteristic polynomial of a linear map $f$ : $E \to E$ is independent of the basis $(e_{1}, \dots  , e_{n})$ chosen in $E$. To prove this, observe that the matrix of $f$ over another basis will be of the form $P^{-1}$ AP, for some inverible matrix $P$, and then
$$\det(XI -P^{-1} AP) = \det(XP^{-1} IP -P^{-1} AP)$$
$$= \det(P^{-1} (XI -A)P)$$
$$= \det(P^{-1} ) \det(XI -A) \det(P)$$
$$= \det(XI -A).$$
Therefore, the characteristic polynomial of a linear map is intrinsic to $f$, and it is denoted by $P_{f}$. The zeros (roots) of the characteristic polynomial of a linear map $f$ are called the eigenvalues of $f$. They play an important role in theory and applications. We will come back to this topic later on.

## 7.8 Permanents

Recall that the explicit formula for the determinant of an $n \times  n$ matrix is
$$\det(A) = \sum_{\pi\in Sn}  \epsilon (\pi )a_{\pi(1) 1} \cdots  a_{\pi(n)n}.$$
If we drop the sign $\epsilon (\pi$ ) of every permutation from the above formula, we obtain a quantity known as the permanent:
$$per(A) = \sum_{\pi\in Sn}  a_{\pi(1) 1} \cdots  a_{\pi(n)n}.$$
Permanents and determinants were investigated as early as $1812$ by Cauchy. It is clear from the above definition that the permanent is a multilinear symmetric form. We also have
$$per(A) = per(A^{\top}),$$

<!-- PAGE 248 -->
and the following unsigned version of the Laplace expansion formula:
$$per(A) = a_{i1}per(A_{i1}) + \cdots  + a_{i j}per(A_{i j}) + \cdots  + a_{i n}per(A_{i n}),$$
for $i = 1, \dots  , n$. However, unlike determinants which have a clear geometric interpretation as signed volumes, permanents do not have any natural geometric interpretation. Furthermore, determinants can be evaluated efficiently, for example using the conversion to row reduced echelon form, but computing the permanent is hard. Permanents turn out to have various combinatorial interpretations. One of these is in terms of perfect matchings of bipartite graphs which we now discuss. See Definition 20.5 for the definition of an undirected graph. A bipartite (undirected) graph $G = (V, E)$ is a graph whose set of nodes $V$ can be partitioned into two nonempty disjoint subsets $V_{1}$ and $V_{2}$, such that every edge $e \in E$ has one endpoint in $V_{1}$ and one endpoint in $V_{2}$. An example of a bipartite graph with $14$ nodes is shown in Figure 7.3; its nodes are partitioned into the two sets ${x_{1}, x_{2}, x_{3}, x_{4}, x_{5}, x_{6}, x_{7}}$ and ${y_{1}, y_{2}, y_{3}, y_{4}, y_{5}, y_{6}, y_{7}}$.
$$y_{1}y_{2}y_{3}y_{4}y_{5}y_{6}y_{7}$$
$$x_{1}x_{2}x_{3}x_{4}x_{5}x_{6}x_{7}$$
$$Figure 7.3: A bipartite graph G.$$
A matching in a graph $G = (V, E)$ (bipartite or not) is a set $M$ of pairwise non-adjacent edges, which means that no two edges in $M$ share a common vertex. A perfect matching is a matching such that every node in $V$ is incident to some edge in the matching $M$ (every node in $V$ is an endpoint of some edge in $M)$. Figure 7.4 shows a perfect matching (in red) in the bipartite graph $G$. Obviously, a perfect matching in a bipartite graph can exist only if its set of nodes has a partition in two blocks of equal size, say ${x_{1}, \dots  , x_{m}}$ and ${y_{1}, \dots  , y_{m}}$. Then there is a bijection between perfect matchings and bijections $\pi$ : ${x_{1}, \dots  , x_{m}} \to {y_{1}, \dots  , y_{m}}$ such that $\pi (x_{i}) = y_{j}$ iff there is an edge between $x_{i}$ and $y_{j}$. Now every bipartite graph $G$ with a partition of its nodes into two sets of equal size as above is represented by an $m \times  m$ matrix $A = (a_{ij})$ such that $a_{ij} = 1$ iff there is an edge between $x_{i}$ and $y_{j}$, and $a_{ij} = 0$ otherwise. Using the interpretation of perfect matchings as
