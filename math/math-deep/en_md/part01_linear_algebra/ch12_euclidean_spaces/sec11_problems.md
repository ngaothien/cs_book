# Problems


<!-- PAGE 495 -->

## 12.11 Problems

Problem 12.1. $E$ be a vector space of dimension $2$, and let $(e_{1}, e_{2})$ be a basis of $E$. Prove that if a $> 0$ and $b^{2}$ - ac $< 0$, then the bilinear form defined such that
$$\phi (x_{1}e_{1} + y_{1}e_{2}, x_{2}e_{1} + y_{2}e_{2}) = ax_{1}x_{2} + b(x_{1}y_{2} + x_{2}y_{1}) + cy_{1}y_{2}$$
is a Euclidean inner product.
Problem 12.2. Let $\mathcal{C}[a, b]$ denote the set of continuous functions $f$ : [a, $b] \to \mathbb{R}$. Given any two functions $f, g \in$ C[a, $b]$, let
$$\langle f, g\rangle = \int_{a}^{}  bf(t)g(t)dt.$$
Prove that the above bilinear form is indeed a Euclidean inner product.
Problem 12.3. Consider the inner product
$$\langle f, g\rangle = \int_{-}^{}  \pi f(t)g(t)dt$$
$$\pi$$
of Problem 12.2 on the vector space $\mathcal{C}[-\pi , \pi$ ]. Prove that
$$\pi if p = q, p, q \ge 1,$$
$$\langle \sin px, \sin qx\rangle =$$
$$0if p \neq  q, p, q \ge 1,$$
$$\pi if p = q, p, q \ge 1,$$
$$\langle \cos px, \cos qx\rangle =$$
$$0if p \neq  q, p, q \ge 0,$$
$$\langle \sin px, \cos qx\rangle = 0,$$
$$for all p \ge 1 and q \ge 0, and \langle 1, 1\rangle =_{\pi}^{\pi} \int_{-}  dx = 2\pi .$$
Problem 12.4. Prove that the following matrix is orthogonal and skew-symmetric:
$$M = \sqrt \frac{1}{\overline{3}} \begin{pmatrix} 0 & 1 & 1 & 1 \\ -1 & 0 & -1 & 1 \\ -1 & 1 & 0 & -1 \\ 1 & 1 & 1 & 0 \end{pmatrix} .$$
$$--$$
Problem 12.5. Let $E$ and $F$ be two finite Euclidean spaces, let $(u_{1}, \dots  , u_{n})$ be a basis of $E$, and let $(v_{1}, \dots  , v_{m})$ be a basis of $F$. For any linear map $f$ : $E \to F$, if $A$ is the matrix of $f$ w.r.t. the basis $(u_{1}, \dots  , u_{n})$ and $B$ is the matrix of $f^{*}$ w.r.t. the basis $(v_{1}, \dots  , v_{m})$, if $G_{1}$ is the Gram matrix of the inner product on $E$ (w.r.t. $(u_{1}, \dots  , u_{n}))$ and if $G_{2}$ is the Gram matrix of the inner product on $F$ (w.r.t. $(v_{1}, \dots  , v_{m}))$, then
$$B = G_{1}^{-1} A^{\top}G_{2}.$$

<!-- PAGE 496 -->
Problem 12.6. Let $A$ be an invertible matrix. Prove that if $A = Q_{1}R_{1} = Q_{2}R_{2}$ are two QR-decompositions of $A$ and if the diagonal entries of $R_{1}$ and $R_{2}$ are positive, then $Q_{1} = Q_{2}$ and $R_{1} = R_{2}$.
Problem 12.7. Prove that the first Hadamard inequality can be deduced from the second Hadamard inequality.
Problem 12.8. Let $E$ be a real vector space of finite dimension, $n \ge 1$. Say that two bases, $(u_{1}, \dots  , u_{n})$ and $(v_{1}, \dots  , v_{n})$, of $E$ have the same orientation iff det(P) $> 0$, where $P$ the change of basis matrix from $(u_{1}, \dots  , u_{n})$ to $(v_{1}, \dots  , v_{n})$, namely, the matrix whose jth columns consist of the coordinates of $v_{j}$ over the basis $(u_{1}, \dots  , u_{n})$.
$(1)$ Prove that having the same orientation is an equivalence relation with two equivalence classes. An orientation of a vector space, $E$, is the choice of any fixed basis, say $(e_{1}, \dots  , e_{n})$, of $E$. Any other basis, $(v_{1}, \dots  , v_{n})$, has the same orientation as $(e_{1}, \dots  , e_{n})$ (and is said to be positive or direct) iff det(P) $> 0$, else it is said to have the opposite orientation of $(e_{1}, \dots  , e_{n})$ (or to be negative or indirect), where $P$ is the change of basis matrix from $(e_{1}, \dots  , e_{n})$ to $(v_{1}, \dots  , v_{n})$. An oriented vector space is a vector space with some chosen orientation (a positive basis).
$(2)$ Let $B_{1} = (u_{1}, \dots  , u_{n})$ and $B_{2} = (v_{1}, \dots  , v_{n})$ be two orthonormal bases. For any sequence of vectors, $(w_{1}, \dots  , w_{n})$, in $E$, let $det_{B1}(w_{1}, \dots  , w_{n})$ be the determinant of the matrix whose columns are the coordinates of the $w_{j}’s$ over the basis $B_{1}$ and similarly for $det_{B2}(w_{1}, \dots  , w_{n})$. Prove that if $B_{1}$ and $B_{2}$ have the same orientation, then
$$det_{B1}(w_{1}, \dots  , w_{n}) = det_{B2}(w_{1}, \dots  , w_{n}).$$
Given any oriented vector space, $E$, for any sequence of vectors, $(w_{1}, \dots  , w_{n})$, in $E$, the common value, $det_{B}(w_{1}, \dots  , w_{n})$, for all positive orthonormal bases, $B$, of $E$ is denoted
$$\lambda_{E} (w_{1}, \dots  , w_{n})$$
and called a volume form of $(w_{1}, \dots  , w_{n})$.
$(3)$ Given any Euclidean oriented vector space, $E$, of dimension $n$ for any $n$ - $1$ vectors, $w_{1}, \dots  , w_{n-1}$, in $E$, check that the map
$$x \mapsto \lambda_{E} (w_{1}, \dots  , w_{n-1}, x)$$
is a linear form. Then prove that there is a unique vector, denoted $w_{1} \times  \cdots  \times  w_{n-1}$, such that
$$\lambda_{E} (w_{1}, \dots  , w_{n-1}, x) = (w_{1} \times  \cdots  \times  w_{n-1}) \cdot  x,$$
for all $x \in E$. The vector $w_{1} \times  \cdots  \times  w_{n-1}$ is called the cross-product of $(w_{1}, \dots  , w_{n-1})$. It is
$$\mathbb{R}^{3}$$
a generalization of the cross-product in (when $n = 3)$.

<!-- PAGE 497 -->
Problem 12.9. Given $p$ vectors $(u_{1}, \dots  , u_{p})$ in a Euclidean space $E$ of dimension $n \ge p$, the Gram determinant (or Gramian) of the vectors $(u_{1}, \dots  , u_{p})$ is the determinant
$$\|u_{1}\|^{2}\langle u_{1}, u_{2}\rangle \dots \langle u_{1}, u_{p}\rangle$$
$$\langle u_{2}, u_{1}\rangle \|u_{2}\|^{2}\dots \langle u_{2}, u_{p}\rangle$$
$$Gram(u_{1}, \dots  , u_{p}) =\vdots \vdots \ddots \vdots .$$
$$\langle u_{p}, u_{1}\rangle \langle u_{p}, u_{2}\rangle \dots \|u_{p}\|^{2}$$
$(1)$ Prove that
$$Gram(u_{1}, \dots  , u_{n}) = \lambda_{E} (u_{1}, \dots  , u_{n})^{2}.$$
Hint. If $(e_{1}, \dots  , e_{n})$ is an orthonormal basis and $A$ is the matrix of the vectors $(u_{1}, \dots  , u_{n})$ over this basis,
$$\det(A)^{2}= \det(A^{\top}A) = \det(A^{i}\cdot  A^{j}),$$
where $A^{i}$ denotes the ith column of the matrix $A$, and $(A^{i} \cdot  A^{j})$ denotes the $n \times  n$ matrix with entries $A^{i} \cdot  A^{j}$.
$(2)$ Prove that
$$\|u_{1} \times  \cdots  \times  u_{n-1}\|^{2}= Gram(u_{1}, \dots  , u_{n-1}).$$
Hint. Letting $w = u_{1} \times  \cdots  \times  u_{n-1}$, observe that
$$\lambda_{E} (u_{1}, \dots  , u_{n-1}, w) = \langle w, w\rangle = \|w\|^{2},$$
and show that
$$\|w\|^{4}= \lambda_{E} (u_{1}, \dots  , u_{n-1}, w)^{2}= Gram(u_{1}, \dots  , u_{n-1}, w)$$
$$= Gram(u_{1}, \dots  , u_{n-1})\|w\|^{2}.$$
Problem 12.10. Let $\phi$ : $E \times  E \to \mathbb{R}$ be a bilinear form on a real vector space $E$ of finite dimension $n$. Given any basis $(e_{1}, \dots  , e_{n})$ of $E$, let $A = (a_{i j})$ be the matrix defined such that
$$a_{i j} = \phi (e_{i}, e_{j}),$$
$1 \le i, j \le n$. We call $A$ the matrix of $\phi$  w.r.t. the basis $(e_{1}, \dots  , e_{n})$.
$(1)$ For any two vectors $x$ and $y$, if $X$ and $Y$ denote the column vectors of coordinates of $x$ and $y$ w.r.t. the basis $(e_{1}, \dots  , e_{n})$, prove that
$$\phi (x, y) = X^{\top}AY.$$
$(2)$ Recall that $A$ is a symmetric matrix if $A = A^{\top}$. Prove that $\phi$  is symmetric if $A$ is a symmetric matrix.
$(3)$ If $(f_{1}, \dots  , f_{n})$ is another basis of $E$ and $P$ is the change of basis matrix from $(e_{1}, \dots  , e_{n})$ to $(f_{1}, \dots  , f_{n})$, prove that the matrix of $\phi$  w.r.t. the basis $(f_{1}, \dots  , f_{n})$ is
$$P^{\top} AP.$$
The common rank of all matrices representing $\phi$  is called the rank of $\phi$ .

<!-- PAGE 498 -->
Problem 12.11. Let $\phi$ : $E \times  E \to \mathbb{R}$ be a symmetric bilinear form on a real vector space $E$ of finite dimension $n$. Two vectors $x$ and $y$ are said to be conjugate or orthogonal w.r.t. $\phi$ if $\phi (x, y) = 0$. The main purpose of this problem is to prove that there is a basis of vectors that are pairwise conjugate w.r.t. $\phi$ .
$(1)$ Prove that if $\phi (x, x) = 0$ for all $x \in E$, then $\phi$  is identically null on $E$. Otherwise, we can assume that there is some vector $x \in E$ such that $\phi (x, x) \neq  0$. Use induction to prove that there is a basis of vectors $(u_{1}, \dots  , u_{n})$ that are pairwise conjugate w.r.t. $\phi$ . Hint. For the induction step, proceed as follows. Let $(u_{1}, e_{2}, \dots  , e_{n})$ be a basis of $E$, with $\phi (u_{1}, u_{1}) \neq  0$. Prove that there are scalars $\lambda_{2} , \dots  , \lambda_{n}$  such that each of the vectors
$$v_{i} = e_{i} + \lambda_{i} u_{1}$$
is conjugate to $u_{1}$ w.r.t. $\phi$ , where $2 \le i \le n$, and that $(u_{1}, v_{2}, \dots  , v_{n})$ is a basis.
$(2)$ Let $(e_{1}, \dots  , e_{n})$ be a basis of vectors that are pairwise conjugate w.r.t. $\phi$  and assume that they are ordered such that
$$\theta_{i}  \neq  0if 1 \le i \le r,$$
$$\phi (e_{i}, e_{i}) =$$
$$0if r + 1 \le i \le n,$$
where $r$ is the rank of $\phi$ . Show that the matrix of $\phi$  w.r.t. $(e_{1}, \dots  , e_{n})$ is a diagonal matrix, and that
$$\phi (x, y) = \sum_{i=1}^{r}  \theta_{i} x_{i}y_{i},$$
$$where x = \sum_{i}  n=1 x_{i}e_{i} and y = \sum  ni=1 y_{i}e_{i}.$$
Prove that for every symmetric matrix $A$, there is an invertible matrix $P$ such that
$$P^{\top} AP = D,$$
where $D$ is a diagonal matrix.
$(3)$ Prove that there is an integer $p, 0 \le p \le r$ (where $r$ is the rank of $\phi$ ), such that $\phi (u_{i}, u_{i}) > 0$ for exactly $p$ vectors of every basis $(u_{1}, \dots  , u_{n})$ of vectors that are pairwise conjugate w.r.t. $\phi$  (Sylvester’s inertia theorem). Proceed as follows. Assume that in the basis $(u_{1}, \dots  , u_{n})$, for any $x \in E$, we have
$$\phi (x, x) = \alpha_{1} x_{1}^{2} + \cdots  + \alpha_{p} x_{p}^{2} -\alpha_{p+1} x_{p+1}^{2} -\cdots  -\alpha_{r} x_{r}^{2},$$
$$where x = \sum_{i}  n=1 x_{i}u_{i}, and that in the basis (v_{1}, \dots  , v_{n}), for any x \in E, we have$$
$$\phi (x, x) = \beta_{1} y_{1}^{2} + \cdots  + \beta_{q} y_{q}^{2} -\beta_{q+1} y_{q+1}^{2} -\cdots  -\beta_{r} y_{r}^{2},$$

<!-- PAGE 499 -->
$$where x = \sum_{i}  n=1 y_{i}v_{i}, with \alpha_{i}  > 0, \beta_{i}  > 0, 1 \le i \le r.$$
Assume that $p > q$ and derive a contradiction. First consider $x$ in the subspace $F$ spanned by
$$(u_{1}, \dots  , u_{p}, u_{r+1}, \dots  , u_{n}),$$
and observe that $\phi (x, x) \ge 0$ if $x \neq  0$. Next consider $x$ in the subspace $G$ spanned by
$$(v_{q+1}, \dots  , v_{r}),$$
and observe that $\phi (x, x) < 0$ if $x \neq  0$. Prove that $F \cap G$ is nontrivial (i.e., contains some nonnull vector), and derive a contradiction. This implies that $p \le q$. Finish the proof. The pair $(p, r$ - $p)$ is called the signature of $\phi$ .
$(4) A$ symmetric bilinear form $\phi$  is definite if for every $x \in E$, if $\phi (x, x) = 0$, then $x = 0$. Prove that a symmetric bilinear form is definite iff its signature is either $(n, 0)$ or $(0, n)$. In other words, a symmetric definite bilinear form has rank $n$ and is either positive or negative.
Problem 12.12. Consider the $n \times  n$ matrices $R^{i,j}$ defined for all $i, j$ with $1 \le i < j \le n$ and $n \ge 3$, such that the only nonzero entries are
$$R^{i,j}(i, j) = -1$$
$$R^{i,j}(i, i) = 0$$
$$R^{i,j}(j, i) = 1$$
$$R^{i,j}(j, j) = 0$$
$$R^{i,j}(k, k) = 1,1 \le k \le n, k \neq  i, j.$$
For example,
$$R^{i,j} = \begin{pmatrix} 1 \\ \ddots \\ 1 \\ 0 & 0 & \cdots & 0 & -1 \\ 0 & 1 & \cdots & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & 1 & 0 \\ 1 & 0 & \cdots & 0 & 0 \\ 1 \\ \ddots \\ 1 \end{pmatrix} .$$
$(1)$ Prove that the $R^{i,j}$ are rotation matrices. Use the matrices $R^{ij}$ to form a basis of the $n \times  n$ skew-symmetric matrices.

<!-- PAGE 500 -->
$(2)$ Consider the $n \times  n$ symmetric matrices $S^{i,j}$ defined for all $i, j$ with $1 \le i < j \le n$ and $n \ge 3$, such that the only nonzero entries are
$$S^{i,j}(i, j) = 1$$
$$S^{i,j}(i, i) = 0$$
$$S^{i,j}(j, i) = 1$$
$$S^{i,j}(j, j) = 0$$
$$S^{i,j}(k, k) = 1,1 \le k \le n, k \neq  i, j,$$
and if $i + 2 \le j$ then $S^{i,j}(i + 1, i + 1) = -1$, else if $i > 1$ and $j = i + 1$ then $S^{i,j}(1, 1) = -1$, and if $i = 1$ and $j = 2$, then $S^{i,j}(3, 3) = -1$. For example,
$$S^{i,j} = \begin{pmatrix} 1 \\ \ddots \\ 1 \\ 0 & 0 & \cdots & 0 & 1 \\ 0 & -1 & \cdots & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & 1 & 0 \\ 1 & 0 & \cdots & 0 & 0 \\ 1 \\ \ddots \\ 1 \end{pmatrix} .$$
Note that $S^{i,j}$ has a single diagonal entry equal to $-1$. Prove that the $S^{i,j}$ are rotations matrices. Use Problem 3.15 together with the $S^{i,j}$ to form a basis of the $n \times  n$ symmetric matrices.
$(3)$ Prove that if $n \ge 3$, the set of all linear combinations of matrices in SO(n) is the space $M_{n}(\mathbb{R})$ of all $n \times  n$ matrices. Prove that if $n \ge 3$ and if a matrix $A \in M_{n}(\mathbb{R})$ commutes with all rotations matrices, then $A$ commutes with all matrices in $M_{n}(\mathbb{R})$. What happens for $n = 2$?
$$\mathbb{R}^{n}$$
Problem 12.13. $(1)$ Let $H$ be the affine hyperplane in given by the equation
$$a_{1}x_{1} + \cdots  + a_{n}x_{n} = c,$$
with $a_{i} \neq  0$ for some $i, 1 \le i \le n$. The linear hyperplane $H_{0}$ parallel to $H$ is given by the equation
$$a_{1}x_{1} + \cdots  + a_{n}x_{n} = 0,$$

<!-- PAGE 501 -->
$$\mathbb{R}^{n}$$
and we say that a vector $y \in$ is orthogonal (or perpendicular) to $H$ iff $y$ is orthogonal to $H_{0}$. Let $h$ be the intersection of $H$ with the line through the origin and perpendicular to $H$. Prove that the coordinates of $h$ are given by
$$\frac{c}{a_{1}^{2}+ \cdots  + a_{n}^{2}} (a_{1}, \dots  , a_{n}).$$
$(2)$ For any point $p \in H$, prove that $\|h\|\le \|p\|$. Thus, it is natural to define the distance d(O, $H)$ from the origin $O$ to the hyperplane $H$ as d(O, $H) = \|h\|$. Prove that
$$||$$
$$d(O, H) = \frac{c}{(a_{1}^{2}+ \cdots  + a_{n}^{2}\overline{)}_{2}^{1}} .$$
$(3)$ Let $S$ be a finite set of $n \ge 3$ points in the plane $(\mathbb{R}^{2})$. Prove that if for every pair of distinct points $p_{i}, p_{j} \in S$, there is a third point $p_{k} \in S$ (distinct from $p_{i}$ and $p_{j})$ such that $p_{i}, p_{j}, p_{k}$ belong to the same (affine) line, then all points in $S$ belong to a common (affine) line. Hint. Proceed by contradiction and use a minimality argument. This is either $\infty$ -hard or relatively easy, depending how you proceed!
Problem 12.14. (The space of closed polygons in $\mathbb{R}^{2}$, after Hausmann and Knutson) An open polygon $P$ in the plane is a sequence $P = (v_{1}, \dots  , v_{n+1})$ of points $v_{i} \in \mathbb{R}^{2}$ called vertices (with $n \ge 1)$. A closed polygon, for short a polygon, is an open polygon $P = (v_{1}, \dots  , v_{n+1})$ such that $v_{n+1} = v_{1}$. The sequence of edge vectors $(e_{1}, \dots  , e_{n})$ associated with the open (or closed) polygon $P = (v_{1}, \dots  , v_{n+1})$ is defined by
$$e_{i} = v_{i+1} -v_{i},i = 1, \dots  , n.$$
Thus, a closed or open polygon is also defined by a pair $(v_{1}, (e_{1}, \dots  , e_{n}))$, with the vertices given by
$$v_{i+1} = v_{i} + e_{i},i = 1, \dots  , n.$$
Observe that a polygon $(v_{1}, (e_{1}, \dots  , e_{n}))$ is closed iff
$$e_{1} + \cdots  + e_{n} = 0.$$
Since every polygon $(v_{1}, (e_{1}, \dots  , e_{n}))$ can be translated by $-v_{1}$, so that $v_{1} = (0, 0)$, we may assume that our polygons are specified by a sequence of edge vectors.
$$\mathbb{R}^{2}  \mathbb{C}$$
Recall that the plane is isomorphic to , via the isomorphism
$$(x, y) \mapsto x + iy.$$
We will represent each edge vector $e_{k}$ by the square of a complex number $w_{k} = a_{k}+ib_{k}$. Thus, every sequence of complex numbers $(w_{1}, \dots  , w_{n})$ defines a polygon (namely, $(w_{1}^{2}, \dots  , w_{n}^{2}))$.

<!-- PAGE 502 -->
This representation is many-to-one: the sequences $(\pm w_{1}, \dots  , \pm w_{n})$ describe the same polygon. To every sequence of complex numbers $(w_{1}, \dots  , w_{n})$, we associate the pair of vectors (a, $b)$, with a, $b \in \mathbb{R}^{n}$, such that if $w_{k} = a_{k} + ib_{k}$, then
$$a = (a_{1}, \dots  , a_{n}),b = (b_{1}, \dots  , b_{n}).$$
The mapping
$$(w_{1}, \dots  , w_{n}) \mapsto (a, b)$$
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
is clearly a bijection, so we can also represent polygons by pairs of vectors (a, $b) \in \times$ .
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
$(1)$ Prove that a polygon $P$ represented by a pair of vectors (a, $b) \in \times$ is closed iff $a \cdot  b = 0$ and $\|a\|_{2} = \|b\|_{2}$.
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
$(2)$ Given a polygon $P$ represented by a pair of vectors (a, $b) \in \times$ , the length l(P) of the polygon $P$ is defined by l(P) $= |w_{1}|^{2} + \cdots  + |w_{n}|^{2}$, with $w_{k} = a_{k} + ib_{k}$. Prove that
$$l(P) = \|a\|_{2}^{2} + \|b\|_{2}^{2} .$$
Deduce from (a) and $(b)$ that every closed polygon of length $2$ with $n$ edges is represented by a $n \times  2$ matrix $A$ such that $A^{\top}A =$ I.
Remark: The space of all a $n \times  2$ real matrices $A$ such that $A^{\top}A =$ I is a space known as the Stiefel manifold S(2, $n)$.
$(3)$ Recall that in $\mathbb{R}^{2}$, the rotation of angle $\theta$  specified by the matrix
$$R_{\theta} = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$$
is expressed in terms of complex numbers by the map
$$z \mapsto ze^{i\theta}.$$
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
Let $P$ be a polygon represented by a pair of vectors (a, $b) \in \times$ . Prove that the polygon $R_{\theta}(P)$ obtained by applying the rotation $R_{\theta}$ to every vertex $w_{k}^{2} = (a_{k} + ib_{k})^{2}$ of $P$ is specified by the pair of vectors
$$(\cos(\theta /2)a -\sin(\theta /2)b, \sin(\theta /2)a + \cos(\theta /2)b) = \begin{pmatrix} a_{1} & b_{1} \\ a_{2} & b_{2} \\ \vdots & \vdots \\ a_{n} & b_{n} \end{pmatrix} \begin{pmatrix} \cos(\theta /2) & \sin(\theta /2) \\ -\sin(\theta /2) & \cos(\theta /2) \end{pmatrix} .$$
$(4)$ The reflection $\rho_{x}$  about the x-axis corresponds to the map
$$z \mapsto \overline{z,}$$

<!-- PAGE 503 -->
whose matrix is,
$$\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} .$$
Prove that the polygon $\rho_{x} (P)$ obtained by applying the reflection $\rho_{x}$  to every vertex $w_{k}^{2} = (a_{k} + ib_{k})^{2}$ of $P$ is specified by the pair of vectors
$$(a, -b) = \begin{pmatrix} a_{1} & b_{1} \\ a_{2} & b_{2} \\ \vdots & \vdots \\ a_{n} & b_{n} \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} .$$
$(5)$ Let $Q \in$ O(2) be any isometry such that det(Q) $= -1$ (a reflection). Prove that there is a rotation $R_{-\theta} \in$ SO(2) such that
$$Q = \rho_{x}  \circ R_{-\theta}.$$
Prove that the isometry $Q$, which is given by the matrix
$$Q = \begin{pmatrix} \cos \theta & \sin \theta \\ \sin \theta & -\cos \theta \end{pmatrix} ,$$
is the reflection about the line corresponding to the angle $\theta /2$ (the line of equation $y = tan(\theta /2)x)$. Prove that the polygon Q(P) obtained by applying the reflection $Q = \rho_{x}  \circ R_{-\theta}$ to every vertex $w_{k}^{2} = (a_{k} + ib_{k})^{2}$ of $P$, is specified by the pair of vectors
$$(\cos(\theta /2)a + \sin(\theta /2)b, \sin(\theta /2)a -\cos(\theta /2)b) = \begin{pmatrix} a_{1} & b_{1} \\ a_{2} & b_{2} \\ \vdots & \vdots \\ a_{n} & b_{n} \end{pmatrix} \begin{pmatrix} \cos(\theta /2) & \sin(\theta /2) \\ \sin(\theta /2) & -\cos(\theta /2) \end{pmatrix} .$$
$(6)$ Define an equivalence relation $\sim$ on S(2, $n)$ such that if $A_{1}, A_{2} \in$ S(2, $n)$ are any $n\times 2$ matrices such that $A_{1}^{\top} A_{1} = A_{2}^{\top} A_{2} =$ I, then
$$A_{1} \sim A_{2}iff A_{2} = A_{1}Qfor some Q \in O(2).$$
Prove that the quotient G(2, $n) =$ S(2, $n)/ \sim$ is in bijection with the set of all 2-dimensional subspaces (the planes) of $\mathbb{R}^{n}$. The space G(2, $n)$ is called a Grassmannian manifold. Prove that up to translations and isometries in O(2) (rotations and reflections), the n-sided closed polygons of length $2$ are represented by planes in G(2, $n)$.

<!-- PAGE 504 -->
Problem 12.15. $(1)$ Find two symmetric matrices, $A$ and $B$, such that $AB$ is not symmetric.
$(2)$ Find two matrices $A$ and $B$ such that
$$e^{A}e^{B}\neq  e^{A+B}.$$
Hint. Try
$$A = \pi \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix} andB = \pi \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix} ,$$
$$-$$
and use the Rodrigues formula.
$(3)$ Find some square matrices $A, B$ such that $AB \neq$  BA, yet
$$e^{A}e^{B}= e^{A+B}.$$
Hint. Look for $2 \times  2$ matrices with zero trace and use Problem 9.15.
Problem 12.16. Given a field $K$ and any nonempty set $I$, let $K^{(I)}$ be the subset of the cartesian product $K^{I}$ consisting of all functions $\lambda$ : I $\to K$ with finite support, which means that $\lambda (i) = 0$ for all but finitely many $i \in$ I. We usually denote the function defined by $\lambda$  as $(\lambda_{i} )_{i\in I}$, and call is a family indexed by I. We define addition and multiplication by a scalar as follows:
$$(\lambda_{i} )_{i\in I} + (\mu_{i} )_{i\in I} = (\lambda_{i}  + \mu_{i} )_{i\in I},$$
and
$$\alpha  \cdot  (\mu_{i} )_{i\in I} = (\alpha \mu_{i} )_{i\in I}.$$
$(1)$ Check that $K^{(I)}$ is a vector space.
$(2)$ If I is any nonempty subset, for any $i \in$ I, we denote by $e_{i}$ the family $(e_{j})_{j\in I}$ defined so that
$$($$
$$1if j = i$$
$$e_{j} =$$
$$0if j \neq  i.$$
Prove that the family $(e_{i})_{i\in I}$ is linearly independent and spans $K^{(I)}$, so that it is a basis of $K^{(I)}$ called the canonical basis of $K^{(I)}$. When I is finite, say of cardinality $n$, then prove that $K^{(I)}$ is isomorphic to $K^{n}$.
$(3)$ The function $\iota$ : I $\to K^{(I)}$, such that $\iota (i) = e_{i}$ for every $i \in$ I, is clearly an injection. For any other vector space $F$, for any function $f$ : I $\to F$, prove that there is a unique linear map $\overline{f}\overline{:} K^{(I)} \to F$, such that
$$f =\overline{f} \circ \iota ,$$
as in the following commutative diagram:
$$I\overline{C} K^{(I)}.$$
$$\overline{C}^{\iota}\overline{C}$$
$$CC$$
$$CC$$
$$CC^{f}$$
$$f!$$
$$F$$

<!-- PAGE 505 -->
We call the vector space $K^{(I)}$ the vector space freely generated by the set $I$.
Problem 12.17. (Some pitfalls of infinite dimension) Let $E$ be the vector space freely generated by the set of natural numbers, $\mathbb{N} = {0, 1, 2, \dots$ }, and let $(e_{0}, e_{1}, e_{2}, \dots  , e_{n}, \dots$ ) be its canonical basis. We define the function $\phi$  such that
$$\delta_{ij} if i, j \ge 1,$$
$$$$
$$$$
$$1if i = j = 0,$$
$$$$
$$\phi (e_{i}, e_{j}) =$$
$$1/2^{j}if i = 0, j \ge 1,$$
$$$$
$$$$
$$1/2^{i}if i \ge 1, j = 0,$$
$$$$
$$and we extend \phi  by bilinearity to a function \phi : E\times E \to K. This means that if u = \sum_{i}  \in \mathbb{N} \lambda_{i} e_{i}$$
$$and v = \sum_{j}  \in \mathbb{N} \mu_{j} e_{j}, then$$
$$\phi \begin{pmatrix} \lambda_{i} e_{i}, & \mu_{j} e_{j} \end{pmatrix} \sum_{i\in N}  \sum_{j\in N}  = \sum_{i,j\in N}  \lambda_{i} \mu_{j} \phi (e_{i}, e_{j}),$$
but remember that $\lambda_{i}  \neq  0$ and $\mu_{j}  \neq  0$ only for finitely many indices $i, j$.
$(1)$ Prove that $\phi$  is positive definite, so that it is an inner product on $E$. What would happen if we changed $1/2^{j}$ to $1$ (or any constant)?
$(2)$ Let $H$ be the subspace of $E$ spanned by the family $(e_{i})_{i\ge1}$, a hyperplane in $E$. Find $H^{\perp}$ and $H^{\perp \perp}$, and prove that
$$H \neq  H^{\perp \perp}.$$
$(3)$ Let $U$ be the subspace of $E$ spanned by the family $(e_{2i})_{i\ge1}$, and let $V$ be the subspace of $E$ spanned by the family $(e_{2i-1})_{i\ge1}$. Prove that
$$U^{\perp} = V$$
$$V^{\perp} = U$$
$$U^{\perp \perp} = U$$
$$V^{\perp \perp} = V,$$
yet
$$(U \cap V )^{\perp}\neq  U^{\perp}+ V^{\perp}$$
and
$$(U + V )^{\perp \perp}\neq  U + V.$$
If $W$ is the subspace spanned by $e_{0}$ and $e_{1}$, prove that
$$(W \cap H)^{\perp}\neq  W^{\perp}+ H^{\perp}.$$

<!-- PAGE 506 -->
$(4)$ Consider the dual space $E^{*}$ of $E$, and let $(e_{i}^{*} )_{i\in N}$ be the family of dual forms of the basis $(e_{i})_{i\in N}$. Check that the family $(e_{i}^{*} )_{i\in N}$ is linearly independent.
$(5)$ Let $f \in E^{*}$ be the linear form defined by
$$f(e_{i}) = 1for all i \in \mathbb{N}.$$
Prove that $f$ is not in the subspace spanned by the $e_{i}^{*}$ . If $F$ is the subspace of $E^{*}$ spanned by the $e_{i}^{*}$ and $f$, find $F^{0}$ and $F^{00}$, and prove that
$$F \neq  F^{00} .$$
