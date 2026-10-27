# The Courant–Fischer Theorem; Perturbation Results


<!-- PAGE 650 -->

## 17.7 The Courant–Fischer Theorem; Perturbation Re-

$$sults$$
Another useful tool to prove eigenvalue equalities is the Courant–Fischer characterization of the eigenvalues of a symmetric matrix, also known as the Min-max (and Max-min) theorem.

> **Theorem 17.27.** (Courant–Fischer) Let $A$ be a symmetric $n \times  n$ matrix with eigenvalues
$$\mathbb{R}^{n}$$
$\lambda_{1}  \le \lambda_{2}  \le \cdots  \le \lambda_{n}$ . If $\mathcal{V}_{k}$ denotes the set of subspaces of of dimension $k$, then
$$\lambda_{k}  =W\in Vmaxx\in minW,x\neq 0 \frac{x^{\top}Ax}{x^{\top}x}$$
$$n-k+1$$
$$\lambda_{k}  = Wmin\in Vx\in maxW,x\neq 0 \frac{x^{\top}Ax}{x^{\top}x} .$$
$$k$$

*Proof.* Let us consider the second equality, the proof of the first equality being similar. Let $(u_{1}, \dots  , u_{n})$ be any orthonormal basis of eigenvectors of $A$, where $u_{i}$ is a unit eigenvector associated with $\lambda_{i}$ . Observe that the space $V_{k}$ spanned by $(u_{1}, \dots  , u_{k})$ has dimension $k$, and by Proposition 17.23, we have
$$\lambda_{k}  =x\neq 0max,x\in V \frac{x^{\top}Ax}{x^{\top}x} \ge Winf\in Vx\in maxW,x\neq 0 \frac{x^{\top}Ax}{x^{\top}x} .$$
$$kk$$
Therefore, we need to prove the reverse inequality; that is, we have to show that
$$\lambda_{k}  \le x\neq 0max,x\in W \frac{x^{\top}Ax}{x^{\top}x} ,for allW \in V_{k}.$$
Now for any $W \in V_{k}$, if we can prove that $W \cap V_{k-1}^{\perp}  = (0)$, then for any nonzero $v \in W \cap V_{k-1}^{\perp}$ ,
$$̸$$
by Proposition 17.24 , we have
$$\lambda_{k}  =x\neq 0min,x\in V\perp \frac{x^{\top}Ax}{x^{\top}x} \le \frac{v^{\top}Av}{v^{\top}v} \le x\in maxW,x\neq 0 \frac{x^{\top}Ax}{x^{\top}x} .$$
$$k -1$$
It remains to prove that dim(W $\cap V_{k}^{\perp}$ ) $\ge 1$. However, $dim(V_{k-1}) = k$ - $1$, so $dim(V_{k-1}^{\perp}$ ) $= n$ - $k + 1$, and by hypothesis $dim(W^{-1}) = k$. By the Grassmann relation,
$$\dim(W) + \dim(V_{k-1}^{\perp} ) = \dim(W \cap V_{k-1}^{\perp} ) + \dim(W + V_{k-1}^{\perp} ),$$
and since dim(W $+ V_{k-1}^{\perp}$ ) $\le dim(\mathbb{R}^{n}) = n$, we get
$$k + n -k + 1 \le \dim(W \cap V_{k-1}^{\perp} ) + n;$$
that is, $1 \le$ dim(W $\cap V_{k-1}^{\perp}$ ), as claimed. Thus we proved that
$$\lambda_{k}  = Winf\in Vx\in maxW,x\neq 0 \frac{x^{\top}Ax}{x^{\top}x} ,$$
$$k$$
but since the inf is achieved for the subspace $V_{k}$, the equation also holds with inf replaced by min.

<!-- PAGE 651 -->
The Courant–Fischer theorem yields the following useful result about perturbing the eigenvalues of a symmetric matrix due to Hermann Weyl.

> **Proposition 17.28.** Given two $n\times n$ symmetric matrices $A$ and $B = A+\Delta A$, if $\alpha_{1}  \le \alpha_{2}  \le \cdots  \le \alpha_{n}$  are the eigenvalues of $A$ and $\beta_{1}  \le \beta_{2}  \le \cdots  \le \beta_{n}$  are the eigenvalues of $B$, then
$$|\alpha_{k}  -\beta_{k} | \le \rho (\Delta A) \le \|\Delta A\|_{2} ,k = 1, \dots  , n.$$

*Proof.* Let $\mathcal{V}_{k}$ be defined as in the Courant–Fischer theorem and let $V_{k}$ be the subspace spanned by the $k$ eigenvectors associated with $\alpha_{1} , \dots  , \alpha_{k}$ . By the Courant–Fischer theorem applied to $B$, we have
$$\beta_{k}  = Wmin\in Vx\in maxW,x\neq 0 \frac{x^{\top}Bx}{x^{\top}x}$$
$$k$$
$$\le maxx\in V \frac{x^{\top}Bx}{x^{\top}x}$$
$$k$$
$$= maxx\in V \begin{pmatrix} x^{\top}Ax & x^{\top}\Delta Ax \\ + \\ x^{\top}x & x^{\top}x \\ x^{\top}Ax & x^{\top}\Delta \end{pmatrix}$$
$$k$$
$$\le maxx\in Vx^{\top}x + maxx\in V \frac{A x}{x^{\top}x} .$$
$$kk$$
By Proposition 17.23, we have
$$\alpha_{k}  = maxx\in V \frac{x^{\top}Ax}{x^{\top}x} ,$$
$$k$$
so we obtain
$$\beta_{k}  \le maxx\in V \frac{x^{\top}Ax}{x^{\top}x} + maxx\in V \frac{x^{\top}\Delta A x}{x^{\top}x}$$
$$kk$$
$$= \alpha_{k}  + maxx\in V \frac{x^{\top}\Delta A x}{x^{\top}x}$$
$$k$$
$$\le \alpha_{k}  + maxx\in \mathbb{R} n \frac{x^{\top}\Delta A x}{x^{\top}x} .$$
Now by Proposition 17.23 and Proposition 9.10, we have
$$maxx\in \mathbb{R} n \frac{x^{\top}\Delta A x}{x^{\top}x} = maxi\lambda_{i} (\Delta A) \le \rho (\Delta A) \le \|\Delta A\|_{2} ,$$
where $\lambda_{i} (\Delta A)$ denotes the ith eigenvalue of $\Delta A$, which implies that
$$\beta_{k}  \le \alpha_{k}  + \rho (\Delta A) \le \alpha_{k}  + \|\Delta A\|_{2} .$$
By exchanging the roles of $A$ and $B$, we also have
$$\alpha_{k}  \le \beta_{k}  + \rho (\Delta A) \le \beta_{k}  + \|\Delta A\|_{2} ,$$
and thus,
$$|\alpha_{k}  -\beta_{k} | \le \rho (\Delta A) \le \|\Delta A\|_{2} ,k = 1, \dots  , n,$$
as claimed.

<!-- PAGE 652 -->
Proposition 17.28 also holds for Hermitian matrices. A pretty result of Wielandt and Hoffman asserts that
$$\sum_{k=1}^{n}  (\alpha_{k}  -\beta_{k} )^{2}\le \|\Delta A\|_{F}^{2} ,$$
where $\|\|_{F}$ is the Frobenius norm. However, the proof is significantly harder than the above proof; see Lax $[117]$. The Courant–Fischer theorem can also be used to prove some famous inequalities due to Hermann Weyl. These can also be viewed as perturbation results. Given two symmetric (or Hermitian) matrices $A$ and $B$, let $\lambda_{i} (A), \lambda_{i} (B)$, and $\lambda_{i} (A + B)$ denote the ith eigenvalue of $A, B$, and $A + B$, respectively, arranged in nondecreasing order.

> **Proposition 17.29.** (Weyl) Given two symmetric (or Hermitian) $n \times  n$ matrices $A$ and $B$, the following inequalities hold: For all $i, j, k$ with $1 \le i, j, k \le n: 1$. If $i + j = k + 1$, then
$$\lambda_{i} (A) + \lambda_{j} (B) \le \lambda_{k} (A + B).$$
$2$. If $i + j = k + n$, then
$$\lambda_{k} (A + B) \le \lambda_{i} (A) + \lambda_{j} (B).$$

*Proof.* Observe that the first set of inequalities is obtained from the second set by replacing $A$ by $-A$ and $B$ by $-B$, so it is enough to prove the second set of inequalities. By the Courant–Fischer theorem, there is a subspace $H$ of dimension $n$ - $k + 1$ such that
$$\lambda_{k} (A + B) =x\in minH,x\neq 0 \frac{x^{\top}(A + B)x}{x^{\top}x} .$$
Similarly, there exists a subspace $F$ of dimension $i$ and a subspace $G$ of dimension $j$ such that
$$\lambda_{i} (A) = x\in maxF,x\neq 0 \frac{x^{\top}Ax}{x^{\top}x} ,\lambda_{j} (B) =x\in maxG,x\neq 0 \frac{x^{\top}Bx}{x^{\top}x} .$$
We claim that $F \cap G \cap H \neq  (0)$. To prove this, we use the Grassmann relation twice. First, dim(F $\cap G \cap H) =$ dim(F) $+$ dim(G $\cap H)$ -dim(F $+ (G \cap H)) \ge$ dim(F) $+$ dim(G $\cap H) -n$, and second,
$$\dim(G \cap H) = \dim(G) + \dim(H) -\dim(G + H) \ge \dim(G) + \dim(H) -n,$$
so
$$\dim(F \cap G \cap H) \ge \dim(F) + \dim(G) + \dim(H) -2n.$$
