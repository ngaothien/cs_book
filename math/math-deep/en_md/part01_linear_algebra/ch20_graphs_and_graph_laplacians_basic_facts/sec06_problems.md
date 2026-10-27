# Problems


<!-- PAGE 734 -->
$\bullet$  Normalized graph Laplacian. $\bullet$  Spectral graph theory. $\bullet$  Graph clustering using normalized cuts.

## 20.6 Problems

Problem 20.1. Find the unnormalized Laplacian of the graph representing a triangle and of the graph representing a square.
Problem 20.2. Consider the complete graph $K_{m}$ on $m \ge 2$ nodes.
$(1)$ Prove that the normalized Laplacian $L_{sym}$ of $K$ is
$$L_{sym} = \begin{pmatrix} 1 & -1/(m -1) & \dots & -1/(m -1) & -1/(m -1) \\ -1/(m -1) & 1 & \dots & -1/(m -1) & -1/(m -1) \\ \vdots & \ddots & \ddots & \ddots & \vdots \\ -1/(m -1) & -1/(m -1) & \dots & 1 & -1/(m -1) \\ -1/(m -1) & -1/(m -1) & \dots & -1/(m -1) & 1 \end{pmatrix} .$$
$(2)$ Prove that the characteristic polynomial of $L_{sym}$ is
$$\lambda  -11/(m -1)\dots 1/(m -1)1/(m -1)$$
$$1/(m -1)\lambda  -1\dots 1/(m -1)1/(m -1)$$
$$m-1$$
$$\vdots \ddots \ddots \ddots \vdots$$
$$= \lambda \begin{pmatrix} m \\ \lambda  - \\ m -1 \end{pmatrix} .$$
$$1/(m -1)1/(m -1)\dots \lambda  -11/(m -1)$$
$$1/(m -1)1/(m -1)\dots 1/(m -1)\lambda  -1$$
Hint. First subtract the second column from the first, factor $\lambda$  - $m/(m$ - $1)$, and then add the first row to the second. Repeat this process. You will end up with the determinant
$$\lambda  -1/(m -1)1$$
$$.$$
$$1/(m -1)\lambda  -1$$
Problem 20.3. Consider the complete bipartite graph $K_{m,n}$ on $m + n \ge 3$ nodes, with edges between each of the first $m \ge 1$ nodes to each of the last $n \ge 1$ nodes. Prove that the eigenvalues of the normalized Laplacian $L_{sym}$ of $K_{m,n}$ are $0, 1$ with multiplicity $m + n$ - $2$, and $2$.
Problem 20.4. Let $G$ be a graph with a set of nodes $V$ with $m \ge 2$ elements, without isolated nodes, and let $L_{sym} = D^{-1/2}LD^{-1/2}$ be its normalized Laplacian (with $L$ its unnormalized Laplacian).

<!-- PAGE 735 -->
$$\mathbb{R}^{V}$$
$(1)$ For any $y \in$ , consider the Rayleigh ratio
$$R = \frac{y^{\top}L_{sym} y}{y^{\top}y} .$$
Prove that if $x = D^{-1/2}y$, then
$$\sum_{u\sim v}  (x(u) -x(v))^{2}$$
$$R = \frac{x^{\top}Lx}{(D^{1/2}x)^{\top}D^{1/2}x} = \sum_{v}  d_{v}x(v)^{2}.$$
$(2)$ Prove that the second eigenvalue $\nu_{2}$  of $L_{sym}$ is given by
$$\sum_{u\sim v}  (x(u) -x(v))^{2}$$
$$\nu_{2}  =\min.$$
$$1\top Dx=0,x\neq 0 \sum_{v}  d_{v}x(v)^{2}$$
$(3)$ Prove that the largest eigenvalue $\nu_{m}$  of $L_{sym}$ is given by
$$\sum_{u\sim v}  (x(u) -x(v))^{2}$$
$$\nu_{m}  = \max.$$
$$x\neq 0 \sum_{v}  d_{v}x(v)^{2}$$
Problem 20.5. Let $G$ be a graph with a set of nodes $V$ with $m \ge 2$ elements, without isolated nodes. If $0 = \nu_{1}  \le \nu_{1}  \le \dots  \le \nu_{m}$  are the eigenvalues of $L_{sym}$, prove the following properties:
$(1)$ We have $\nu_{1}  + \nu_{2}  + \cdots  + \nu_{m}  = m$.
$(2)$ We have $\nu_{2}  \le m/(m -1)$, with equality holding iff $G = K_{m}$, the complete graph on $m$ nodes.
$(3)$ We have $\nu_{m}  \ge m/(m$ - $1)$.
$(4)$ If $G$ is not a complete graph, then $\nu_{2}  \le 1$ Hint. If a and $b$ are nonadjacent nodes, consider the function $x$ given by
$$d_{b}if v = a$$
$$$$
$$$$
$$x(v) =-d_{a}if v = b$$
$$0if v \neq  a, b,$$
$$$$
and use Problem 20.4(2).

<!-- PAGE 736 -->
$(5)$ Prove that $\nu_{m}  \le 2$. Prove that $\nu_{m}  = 2$ iff the underlying graph of $G$ contains a nontrivial connected bipartite component. Hint. Use Problem 20.4(3).
$(6)$ Prove that if $G$ is connected, then $\nu_{2}  > 0$.
Problem 20.6. Let $G$ be a graph with a set of nodes $V$ with $m \ge 2$ elements, without
$$isolated nodes. Let vol(G) = \sum_{v}  \in V d_{v} and let$$
$$\overline{x} = \sum_{v}  \frac{d_{v}x(v)}{vol(G)} .$$
Prove that
$$\sum_{u\sim v}  (x(u) -x(v))^{2}$$
$$\nu_{2}  = \min .$$
$$x\neq 0 \sum_{v}  d_{v}(x(v) -\overline{x})^{2}$$
Problem 20.7. Let $G$ be a connected bipartite graph. Prove that if $\nu$  is an eigenvalue of $L_{sym}$, then $2$ - $\nu$  is also an eigenvalue of $L_{sym}$.
Problem 20.8. Prove Proposition 20.7.
