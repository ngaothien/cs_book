# Problems


<!-- PAGE 210 -->
It is immediately verified that if $H$ is a hyperplane in $E$ defined by a nonzero linear form $\phi$  so that $H =$ Ker $\phi$ , then for any nonzero $\alpha  \in K$, the linear form $\alpha \phi$  is a nonzero linear form that also defines $H$, that is, $H =$ Ker $\alpha \phi$ . This fact with the second part of Proposition 6.22 shows that a hyperplane $H$ in $E$ is defined by the one-dimensional subspace of the dual $E^{*}$ of $E$ consisting of all the linear forms that vanish on $H$ (including the zero linear form). This is an instance of duality.

## 6.4 Summary

The main concepts and results of this chapter are listed below: $\bullet$  Direct products, sums, direct sums. $\bullet$  Projections. $\bullet$  The fundamental equation
$$\dim(E) = \dim(\mathrm{Ker} f) + \dim(\mathrm{Im} f) = \dim(\mathrm{Ker} f) + rk(f)$$
(Proposition 6.16). $\bullet$  Grassmann’s relation
$$\dim(U) + \dim(V ) = \dim(U + V ) + \dim(U \cap V ).$$
$\bullet$  Characterizations of a bijective linear map $f$ : $E \to F. \bullet$  Rank of a matrix.

## 6.5 Problems

Problem 6.1. Let $V$ and $W$ be two subspaces of a vector space $E$. Prove that if $V \cup W$ is a subspace of $E$, then either $V \subseteq W$ or $W \subseteq V$ .
Problem 6.2. Prove that for every vector space $E$, if $f$ : $E \to E$ is an idempotent linear map, i.e., $f \circ f = f$, then we have a direct sum
$$E = \mathrm{Ker} f \oplus \mathrm{Im} f,$$
so that $f$ is the projection onto its image Im $f$.
Problem 6.3. Let $U_{1}, \dots  , U_{p}$ be any $p \ge 2$ subspaces of some vector space $E$ and recall that the linear map
$$a: U_{1} \times  \cdots  \times  U_{p} \to E$$

<!-- PAGE 211 -->
is given by
$$a(u_{1}, \dots  , u_{p}) = u_{1} + \cdots  + u_{p},$$
with $u_{i} \in U_{i}$ for $i = 1, \dots  , p$.
$(1)$ If we let $Z_{i} \subseteq U_{1} \times  \cdots  \times  U_{p}$ be given by
$$



$$
$$Z_{i} = \begin{pmatrix} u_{1}, \dots  , u_{i-1}, - & u_{j}, u_{i+1}, \dots  , u_{p} \\ i \end{pmatrix} \sum_{j=1,j\neq}^{p}  \sum_{j=1,j\neq}^{p}  u_{j} \in U_{i} \cap \begin{pmatrix} U_{j} \\ i \end{pmatrix} \sum_{j=1,j\neq}^{p}  ,$$
$$i$$
for $i = 1, \dots  , p$, then prove that
$$\mathrm{Ker} a = Z_{1} = \cdots  = Z_{p}.$$
$$In general, for any given i, the condition U_{i} \cap \sum_{j}  = (0) does not necessarily$$
$$\begin{pmatrix} p & U_{j} \\ =1,j\neq i \end{pmatrix}$$
imply that $Z_{i} = (0)$. Thus, let  
$$Z = \begin{pmatrix} u_{1}, \dots  , u_{i-1}, u_{i}, u_{i+1}, \dots  , u_{p} \end{pmatrix} u_{i} = - \sum_{j=1,j\neq}^{p}  u_{j}, u_{i} \in U_{i} \cap \begin{pmatrix} U_{j} \\ i \end{pmatrix} \sum_{j=1,j\neq}^{p}  , 1 \le i \le p.$$
$$i$$
Since Ker $a = Z_{1} = \cdots  = Z_{p}$, we have $Z =$ Ker a. Prove that if
$$U_{i} \cap \begin{pmatrix} U_{j} \\ i \end{pmatrix} \sum_{j=1,j\neq}^{p}  = (0)1 \le i \le p,$$
then $Z =$ Ker $a = (0)$.
$(2)$ Prove that $U_{1} + \cdots  + U_{p}$ is a direct sum iff
$$U_{i} \cap \begin{pmatrix} U_{j} \\ i \end{pmatrix} \sum_{j=1,j\neq}^{p}  = (0)1 \le i \le p.$$
Problem 6.4. Assume that $E$ is finite-dimensional, and let $f_{i}$ : $E \to E$ be any $p \ge 2$ linear maps such that
$$f_{1} + \cdots  + f_{p} = id_{E}.$$
Prove that the following properties are equivalent:
$(1) f_{i}^{2}  = f_{i}, 1 \le i \le p$.
$(2) f_{j} \circ f_{i} = 0$, for all $i \neq  j, 1 \le i, j \le p$. Hint. Use Problem 6.2.

<!-- PAGE 212 -->
Let $U_{1}, \dots  , U_{p}$ be any $p \ge 2$ subspaces of some vector space $E$. Prove that $U_{1} + \cdots  + U_{p}$ is a direct sum iff
$$U_{i} \cap \begin{pmatrix} U_{j} \end{pmatrix} \sum_{j=1}^{i-1}  = (0),i = 2, \dots  , p.$$
Problem 6.5. Given any vector space $E$, a linear map $f$ : $E \to E$ is an involution if $f \circ f =$ id.
$(1)$ Prove that an involution $f$ is invertible. What is its inverse?
$(2)$ Let $E_{1}$ and $E_{-1}$ be the subspaces of $E$ defined as follows:
$$E_{1} = {u \in E | f(u) = u}$$
$$E_{-1} = {u \in E | f(u) = -u}.$$
Prove that we have a direct sum
$$E = E_{1} \oplus E_{-1}.$$
Hint. For every $u \in E$, write
$$-$$
$$u = \frac{u + f(u)}{2} + \frac{uf(u)}{2} .$$
$(3)$ If $E$ is finite-dimensional and $f$ is an involution, prove that there is some basis of $E$ with respect to which the matrix of $f$ is of the form
$$I_{k,n-k} = \begin{pmatrix} I_{k} & 0 \\ 0 & -I_{n-k} \end{pmatrix} ,$$
where $I_{k}$ is the $k \times  k$ identity matrix (similarly for $I_{n-k})$ and $k = dim(E_{1})$. Can you give a geometric interpretation of the action of $f$ (especially when $k = n$ - $1)$?
Problem 6.6. An $n \times  n$ matrix $H$ is upper Hessenberg if $h_{jk} = 0$ for all $(j, k)$ such that $j$ - $k \ge 0$. An upper Hessenberg matrix is unreduced if $h_{i+1i} \neq  0$ for $i = 1, \dots  , n$ - $1$. Prove that if $H$ is a singular unreduced upper Hessenberg matrix, then dim(Ker $(H)) = 1$.
Problem 6.7. Let $A$ be any $n \times  k$ matrix.
$(1)$ Prove that the $k \times  k$ matrix $A^{\top}A$ and the matrix $A$ have the same nullspace. Use this to prove that $rank(A^{\top}A) =$ rank(A). Similarly, prove that the $n \times  n$ matrix $AA^{\top}$ and the matrix $A^{\top}$ have the same nullspace, and conclude that $rank(AA^{\top}) = rank(A^{\top})$. We will prove later that $rank(A^{\top}) =$ rank(A).
$$\mathbb{R}^{n}$$
$(2)$ Let $a_{1}, \dots  , a_{k}$ be $k$ linearly independent vectors in $(1 \le k \le n)$, and let $A$ be the $n \times  k$ matrix whose ith column is $a_{i}$. Prove that $A^{\top}A$ has rank $k$, and that it is invertible. Let $P = A(A^{\top}A)^{-1}A^{\top}$ (an $n \times  n$ matrix). Prove that
$$P^{2}= P$$
$$P^{\top} = P.$$

<!-- PAGE 213 -->
What is the matrix $P$ when $k = 1$?
$(3)$ Prove that the image of $P$ is the subspace $V$ spanned by $a_{1}, \dots  , a_{k}$, or equivalently
$$\mathbb{R}^{n} \mathbb{R}^{k}$$
the set of all vectors in of the form Ax, with $x \in$ . Prove that the nullspace $U$ of $P$ is
$$\mathbb{R}^{n}$$
the set of vectors $u \in$ such that $A^{\top}u = 0$. Can you give a geometric interpretation of $U$?
$$\mathbb{R}^{n}$$
Conclude that $P$ is a projection of onto the subspace $V$ spanned by $a_{1}, \dots  , a_{k}$, and that
$$\mathbb{R}^{n}$$
$$= U \oplus V.$$
$$\mathbb{R}^{2}$$
Problem 6.8. A rotation $R_{\theta}$ in the plane is given by the matrix
$$R_{\theta} = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} .$$
$(1)$ Use Matlab to show the action of a rotation $R_{\theta}$ on a simple figure such as a triangle or a rectangle, for various values of $\theta$ , including $\theta  = \pi /6, \pi /4, \pi /3, \pi /2$.
$(2)$ Prove that $R_{\theta}$ is invertible and that its inverse is $R_{-\theta}$.
$(3)$ For any two rotations $R_{\alpha}$ and $R_{\beta}$, prove that
$$R_{\beta} \circ R_{\alpha} = R_{\alpha} \circ R_{\beta} = R_{\alpha+\beta}.$$
Use (2)-(3) to prove that the rotations in the plane form a commutative group denoted SO(2).
$$\mathbb{R}^{2}$$
Problem 6.9. Consider the affine map $R_{\theta ,(a1,a2)}$ in given by
$$\begin{pmatrix} y_{1} \\ y_{2} \end{pmatrix} = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} + \begin{pmatrix} a_{1} \\ a_{2} \end{pmatrix} .$$
$(1)$ Prove that if $\theta  \neq  k2\pi$ , with $k \in \mathbb{Z}$, then $R_{\theta ,(a1,a2)}$ has a unique fixed point $(c_{1}, c_{2})$, that is, there is a unique point $(c_{1}, c_{2})$ such that
$$\begin{pmatrix} c_{1} \\ c_{2} \end{pmatrix} = R_{\theta ,(a1,a2)} \begin{pmatrix} c_{1} \\ c_{2} \end{pmatrix} ,$$
and this fixed point is given by
$$\begin{pmatrix} c_{1} \\ c_{2} \end{pmatrix} = \frac{1}{2 \sin(\theta /2)} \begin{pmatrix} \cos(\pi /2 -\theta /2) & -\sin(\pi /2 -\theta /2) \\ \sin(\pi /2 -\theta /2) & \cos(\pi /2 -\theta /2) \end{pmatrix} \begin{pmatrix} a_{1} \\ a_{2} \end{pmatrix} .$$
$(2)$ In this question we still assume that $\theta$ ̸ $= k2\pi$ , with $k \in \mathbb{Z}$. By translating the coordinate system with origin $(0, 0)$ to the new coordinate system with origin $(c_{1}, c_{2})$, which

<!-- PAGE 214 -->
means that if $(x_{1}, x_{2})$ are the coordinates with respect to the standard origin $(0, 0)$ and if $(x_{1}', x_{2}')$ are the coordinates with respect to the new origin $(c_{1}, c_{2})$, we have
$$x_{1} = x_{1}' + c_{1}$$
$$x_{2} = x_{2}' + c_{2}$$
and similarly for $(y_{1}, y_{2})$ and $(y_{1}', y_{2}')$, then show that
$$\begin{pmatrix} y_{1} \\ y_{2} \end{pmatrix} = R_{\theta ,(a1,a2)} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix}$$
becomes
$$\begin{pmatrix} y_{1}' \\ y_{2}' \end{pmatrix} = R_{\theta} \begin{pmatrix} x_{1}' \\ x_{2}' \end{pmatrix} .$$
Conclude that with respect to the new origin $(c_{1}, c_{2})$, the affine map $R_{\theta ,(a1,a2)}$ becomes the rotation $R_{\theta}$. We say that $R_{\theta ,(a1,a2)}$ is a rotation of center $(c_{1}, c_{2})$.
$(3)$ Use Matlab to show the action of the affine map $R_{\theta ,(a1,a2)}$ on a simple figure such as a triangle or a rectangle, for $\theta  = \pi /3$ and various values of $(a_{1}, a_{2})$. Display the center $(c_{1}, c_{2})$ of the rotation. What kind of transformations correspond to $\theta  = k2\pi$ , with $k \in \mathbb{Z}$?
$(4)$ Prove that the inverse of $R_{\theta ,(a1,a2)}$ is of the form $R_{-\theta ,(b1,b2)}$, and find $(b_{1}, b_{2})$ in terms of $\theta$  and $(a_{1}, a_{2})$.
$(5)$ Given two affine maps $R_{\alpha ,(a1,a2)}$ and $R_{\beta ,(b1,b2)}$, prove that
$$R_{\beta ,(b1,b2)} \circ R_{\alpha ,(a1,a2)} = R_{\alpha+\beta ,(t1,t2)}$$
for some $(t_{1}, t_{2})$, and find $(t_{1}, t_{2})$ in terms of $\beta , (a_{1}, a_{2})$ and $(b_{1}, b_{2})$. Even in the case where $(a_{1}, a_{2}) = (0, 0)$, prove that in general
$$R_{\beta ,(b1,b2)} \circ R_{\alpha} \neq  R_{\alpha} \circ R_{\beta ,(b1,b2)}.$$
Use (4)-(5) to show that the affine maps of the plane defined in this problem form a nonabelian group denoted SE(2). Prove that $R_{\beta ,(b1,b2)} \circ R_{\alpha ,(a1,a2)}$ is not a translation (possibly the identity) iff $\alpha  +\beta  \neq  k2\pi$ , for all $k \in \mathbb{Z}$. Find its center of rotation when $(a_{1}, a_{2}) = (0, 0)$. If $\alpha +\beta  = k2\pi$ , then $R_{\beta ,(b1,b2)} \circ R_{\alpha ,(a1,a2)}$ is a pure translation. Find the translation vector of $R_{\beta ,(b1,b2)} \circ R_{\alpha ,(a1,a2)}$.
$$\mathbb{R}^{n}$$
Problem 6.10. (Affine subspaces) $A$ subset $\mathcal{A}$ of is called an affine subspace if either
$$\mathbb{R}^{n}  \mathbb{R}^{n}$$
$\mathcal{A} = \emptyset$ , or there is some vector $a \in$ and some subspace $U$ of such that
$$\mathcal{A} = a + U = {a + u | u \in U}.$$

<!-- PAGE 215 -->
We define the dimension $dim(\mathcal{A})$ of $\mathcal{A}$ as the dimension dim(U) of $U$.
$(1)$ If $\mathcal{A} = a + U$, why is $a \in A$? What are affine subspaces of dimension $0$? What are affine subspaces of dimension $1$ (begin with $\mathbb{R}^{2})$? What are affine subspaces of dimension $2$ (begin with $\mathbb{R}^{3})$? Prove that any nonempty affine subspace is closed under affine combinations.
$(2)$ Prove that if $\mathcal{A} = a + U$ is any nonempty affine subspace, then $\mathcal{A} = b + U$ for any $b \in A$.
$$\mathbb{R}^{n}$$
$(3)$ Let $\mathcal{A}$ be any nonempty subset of closed under affine combinations. For any $a \in A$, prove that
$$\mathbb{R}^{n}$$
$$U_{a} = {x -a \in | x \in A}$$
$$\mathbb{R}^{n}$$
is a (linear) subspace of such that
$$\mathcal{A} = a + U_{a}.$$
Prove that $U_{a}$ does not depend on the choice of $a \in A$; that is, $U_{a} = U_{b}$ for all a, $b \in A$. In fact, prove that
$$\mathbb{R}^{n}$$
$$U_{a} = U = {y -x \in | x, y \in A},for all a \in A,$$
and so
$$\mathcal{A} = a + U,for any a \in A.$$
Remark: The subspace $U$ is called the direction of $\mathcal{A}$.
$(4)$ Two nonempty affine $subspaces\mathcal{A} and\mathcal{B}$ are said to be parallel iff they have the same direction. Prove that that if A̸ $=\mathcal{B}$ and $\mathcal{A}$ and $\mathcal{B}$ are parallel, then $A \cap B = \emptyset$ .
Remark: The above shows that affine subspaces behave quite differently from linear subspaces.
Problem 6.11. (Affine frames and affine maps) For any vector $v = (v_{1}, \dots  , v_{n}) \in \mathbb{R}^{n}$, let $\mathbb{R}^{n+1} \mathbb{R}^{n+1} v \in$ be the vector $v = (v_{1}, \dots  , v_{n}, 1)$. Equivalently, $v = (v_{1}, \dots  ,v_{n+1}) \in$ is the $b  b  b b  b$ vector defined by
$$($$
$$v_{i}if 1 \le i \le n,$$
$$v_{i} =$$
$$b1if i = n + 1.$$
$$\mathbb{R}^{n}$$
$(1)$ For any $m + 1$ vectors $(u_{0}, u_{1}, \dots  , u_{m})$ with $u_{i} \in$ and $m \le n$, prove that if the $m$ vectors $(u_{1}$ - $u_{0}, \dots  , u_{m}$ - $u_{0})$ are linearly independent, then the $m + 1$ vectors $(u_{0}, \dots  ,u_{m})$
$$b b$$
are linearly independent.
$(2)$ Prove that if the $m + 1$ vectors $(u_{0}, \dots  ,u_{m})$ are linearly independent, then for any
$$b b$$
choice of $i$, with $0 \le i \le m$, the $m$ vectors $u_{j}$ - $u_{i}$ for $j \in {0, \dots  , m}$ with $j$ - $i \neq  0$ are linearly independent.

<!-- PAGE 216 -->
Any $m + 1$ vectors $(u_{0}, u_{1}, \dots  , u_{m})$ such that the $m + 1$ vectors $(u_{0}, \dots  ,u_{m})$ are linearly
$$b b$$
independent are said to be affinely independent. From $(1)$ and $(2)$, the vector $(u_{0}, u_{1}, \dots  , u_{m})$ are affinely independent iff for any any choice of $i$, with $0 \le i \le m$, the $m$ vectors $u_{j}$ - $u_{i}$ for $j \in {0, \dots  , m}$ with $j$ - $i \neq  0$ are linearly independent. If $m = n$, we say that $n + 1$ affinely independent vectors $(u_{0}, u_{1}, \dots  , u_{n})$ form an affine frame of $\mathbb{R}^{n}$.
$(3)$ if $(u_{0}, u_{1}, \dots  , u_{n})$ is an affine frame of $\mathbb{R}^{n}$, then prove that for every vector $v \in \mathbb{R}^{n}$, there is a unique $(n+1)-tuple (\lambda_{0} , \lambda_{1} , \dots  , \lambda_{n}$ ) $\in \mathbb{R}^{n+1}$, with $\lambda_{0}  +\lambda_{1}  +\cdots +\lambda_{n}  = 1$, such that
$$v = \lambda_{0} u_{0} + \lambda_{1} u_{1} + \cdots  + \lambda_{n} u_{n}.$$
The scalars $(\lambda_{0} , \lambda_{1} , \dots  , \lambda_{n}$ ) are called the barycentric (or affine) coordinates of $v$ w.r.t. the affine frame $(u_{0}, u_{1}, \dots  , u_{n})$. If we write $e_{i} = u_{i}$ - $u_{0}$, for $i = 1, \dots  , n$, then prove that we have
$$v = u_{0} + \lambda_{1} e_{1} + \cdots  + \lambda_{n} e_{n},$$
$$\mathbb{R}^{n}$$
and since $(e_{1}, \dots  , e_{n})$ is a basis of (by $(1)$ & $(2))$, the $n$-tuple $(\lambda_{1} , \dots  , \lambda_{n}$ ) consists of the standard coordinates of $v$ - $u_{0}$ over the basis $(e_{1}, \dots  , e_{n})$.
$$\mathbb{R}^{n}  \mathbb{R}^{n}$$
Conversely, for any vector $u_{0} \in$ and for any basis $(e_{1}, \dots  , e_{n})$ of , let $u_{i} = u_{0} + e_{i}$ for $i = 1, \dots  , n$. Prove that $(u_{0}, u_{1}, \dots  , u_{n})$ is an affine frame of $\mathbb{R}^{n}$, and for any $v \in \mathbb{R}^{n}$, if
$$v = u_{0} + x_{1}e_{1} + \cdots  + x_{n}e_{n},$$
$$\mathbb{R}^{n}$$
with $(x_{1}, \dots  , x_{n}) \in$ (unique), then
$$v = (1 -(x_{1} + \cdots  + x_{x}))u_{0} + x_{1}u_{1} + \cdots  + x_{n}u_{n},$$
so that $(1-(x_{1} +\cdots +x_{x})), x_{1}, \cdots  , x_{n})$, are the barycentric coordinates of $v$ w.r.t. the affine frame $(u_{0}, u_{1}, \dots  , u_{n})$. The above shows that there is a one-to-one correspondence between affine frames $(u_{0}, \dots , u_{n})$ and pairs $(u_{0}, (e_{1}, \dots  , e_{n}))$, with $(e_{1}, \dots  , e_{n})$ a basis. Given an affine frame $(u_{0}, \dots  , u_{n})$, we obtain the basis $(e_{1}, \dots  , e_{n})$ with $e_{i} = u_{i} -u_{0}$, for $i = 1, \dots  , n$; given the pair $(u_{0}, (e_{1}, \dots , e_{n}))$ where $(e_{1}, \dots  , e_{n})$ is a basis, we obtain the affine frame $(u_{0}, \dots  , u_{n})$, with $u_{i} = u_{0} + e_{i}$, for $i = 1, \dots  , n$. There is also a one-to-one correspondence between barycentric coordinates w.r.t. the affine frame $(u_{0}, \dots  , u_{n})$ and standard coordinates w.r.t. the basis $(e_{1}, \dots  , e_{n})$. The barycentric cordinates $(\lambda_{0} , \lambda_{1} , \dots  , \lambda_{n}$ ) of $v$ (with $\lambda_{0}  + \lambda_{1}  + \cdots  + \lambda_{n}  = 1)$ yield the standard coordinates $(\lambda_{1} , \dots  , \lambda_{n}$ ) of $v$ - $u_{0}$; the standard coordinates $(x_{1}, \dots  , x_{n})$ of $v$ - $u_{0}$ yield the barycentric coordinates $(1$ - $(x_{1} + \cdots  + x_{n}), x_{1}, \dots  , x_{n})$ of $v$.
$(4)$ Recall that an affine map is a map $f$ : $E \to F$ between vector spaces that preserves affine combinations; that is,
$$f \sum_{i=1}^{m}  \lambda_{i} u_{i}!= \sum_{i=1}^{m}  \lambda_{i} f(u_{i}),$$

<!-- PAGE 217 -->
$$for all u_{1} \dots  , u_{m} \in E and all \lambda_{i}  \in K such that \sum_{i}  m=1 \lambda_{i}  = 1.$$
$$\mathbb{R}^{n} \mathbb{R}^{m}$$
Let $(u_{0}, \dots  , u_{n})$ be any affine frame in and let $(v_{0}, \dots  , v_{n})$ be any vectors in . Prove
$$\mathbb{R}^{n} \mathbb{R}^{m}$$
that there is a unique affine map $f$ : $\to$ such that
$$f(u_{i}) = v_{i},i = 0, \dots  , n.$$
$$\mathbb{R}^{n}$$
$(5)$ Let $(a_{0}, \dots  , a_{n})$ be any affine frame in and let $(b_{0}, \dots  , b_{n})$ be any $n + 1$ points in $\mathbb{R}^{n}$. Prove that there is a unique $(n + 1) \times  (n + 1)$ matrix
$$A = \begin{pmatrix} B & w \\ 0 & 1 \end{pmatrix}$$
corresponding to the unique affine map $f$ such that
$$f(a_{i}) = b_{i},i = 0, \dots  , n,$$
in the sense that
$$Aa_{i} =b_{i},i = 0, \dots  , n,$$
$$b b$$
and that $A$ is given by
$$.$$
$$A = \begin{pmatrix} bb_{0} & bb_{1} & \cdots & bb_{n} \\ bottomrowofA \end{pmatrix} \begin{pmatrix} a_{0} & a_{1} & \cdots \\ b & b & b \end{pmatrix} a_{n}^{-1}$$
Make sure to prove that the     is $(0, \dots  , 0, 1)$. In the special case where $(a_{0}, \dots  , a_{n})$ is the canonical affine frame with $a_{i} = e_{i+1}$ for $i = 0, \dots  , n$ - $1$ and $a_{n} = (0, \dots  , 0)$ (where $e_{i}$ is the ith canonical basis vector), show that
$$\begin{pmatrix} a_{0} & a_{1} & \cdots & a_{n} \\ b & b & b \end{pmatrix} = \begin{pmatrix} 1 & 0 & \cdots & 0 & 0 \\ 0 & 1 & \cdots & 0 & 0 \\ \vdots & \vdots & \ddots & 0 & 0 \\ 0 & 0 & \cdots & 1 & 0 \\ 1 & 1 & \cdots & 1 & 1 \end{pmatrix}$$
and
$$a_{n}^{-1} = \begin{pmatrix} 1 & 0 & \cdots & 0 & 0 \\ 0 & 1 & \cdots & 0 & 0 \\ \vdots & \vdots & \ddots & 0 & 0 \\ 0 & 0 & \cdots & 1 & 0 \\ -1 & -1 & \cdots & -1 & 1 \end{pmatrix} .$$
$$\begin{pmatrix} a_{0} & a_{1} & \cdots \\ b & b & b \end{pmatrix}$$
For example, when $n = 2$, if we write $b_{i} = (x_{i}, y_{i})$, then we have
$$A = \begin{pmatrix} x_{1} & x_{2} & x_{3} \\ y_{1} & y_{2} & y_{3} \\ 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 1 & 1 \end{pmatrix} = \begin{pmatrix} x_{1} -x_{3} & x_{2} -x_{3} & x_{3} \\ y_{1} -y_{3} & y_{2} -y_{3} & y_{3} \\ 0 & 0 & 1 \end{pmatrix} .$$
$$--$$

<!-- PAGE 218 -->
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
$(6)$ Recall that a nonempty affine $subspace\mathcal{A}$ of is any nonempty subset of closed
$$\mathbb{R}^{n} \mathbb{R}^{m}$$
under affine combinations. For any affine map $f$ : $\to$ , for any affine subspace $\mathcal{A}$ of $\mathbb{R}^{n}$, and any affine subspace $\mathcal{B}$ of $\mathbb{R}^{m}$, prove that $f(\mathcal{A})$ is an affine subspace of $\mathbb{R}^{m}$, and that $f^{-1} (\mathcal{B})$ is an affine subspace of $\mathbb{R}^{n}$.
