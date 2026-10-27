# Problems


<!-- PAGE 117 -->
$\bullet$  The notion of a linear map. $\bullet$  The image Im $f$ (or range) of a linear map $f. \bullet$  The kernel Ker $f$ (or nullspace) of a linear map $f. \bullet$  The rank rk(f) of a linear map $f. \bullet$  The image and the kernel of a linear map are subspaces. A linear map is injective iff its kernel is the trivial space $(0)$ (Proposition 3.19). $\bullet$  The unique homomorphic extension property of linear maps with respect to bases (Proposition 3.20 ). $\bullet$  Quotient spaces. $\bullet$  The vector space of linear maps $Hom_{K}(E, F). \bullet$  Linear forms (covectors) and the dual space $E^{*}. \bullet$  Coordinate forms. $\bullet$  The existence of dual bases (in finite dimension).

## 3.11 Problems

Problem 3.1. Let $H$ be the set of $3 \times  3$ upper triangular matrices given by
$$$$
$$H = \begin{pmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix} | a, b, c \in \mathbb{R}.$$
$$$$
$(1)$ Prove that $H$ with the binary operation of matrix multiplication is a group; find explicitly the inverse of every matrix in $H$. Is $H$ abelian (commutative)?
$(2)$ Given two groups $G_{1}$ and $G_{2}$, recall that a homomorphism if a function $\phi$ : $G_{1} \to G_{2}$ such that
$$\phi (ab) = \phi (a)\phi (b),a, b \in G_{1}.$$
Prove that $\phi (e_{1}) = e_{2}$ (where $e_{i}$ is the identity element of $G_{i})$ and that
$$\phi (a^{-1}) = (\phi (a))^{-1},a \in G_{1}.$$
$(3)$ Let $S^{1}$ be the unit circle, that is
$$S^{1}= {e^{i\theta}= \cos \theta  + i \sin \theta  | 0 \le \theta  < 2\pi },$$

<!-- PAGE 118 -->
and let $\phi$  be the function given by
$$\phi \begin{pmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix} = (a, c, e^{ib}).$$
Prove that $\phi$  is a surjective function onto $G = \mathbb{R} \times  \mathbb{R} \times  S^{1}$, and that if we define multiplication on this set by
$$(x_{1}, y_{1}, u_{1}) \cdot  (x_{2}, y_{2}, u_{2}) = (x_{1} + x_{2}, y_{1} + y_{2}, e^{ix1y2}u_{1}u_{2}),$$
then $G$ is a group and $\phi$  is a group homomorphism from $H$ onto $G$.
$(4)$ The kernel of a homomorphism $\phi$ : $G_{1} \to G_{2}$ is defined as
$$\mathrm{Ker} (\phi ) = {a \in G_{1} | \phi (a) = e_{2}}.$$
Find explicitly the kernel of $\phi$  and show that it is a subgroup of $H$.
Problem 3.2. For any $m \in \mathbb{Z}$ with $m > 0$, the subset $m\mathbb{Z} = {mk$ | $k \in \mathbb{Z}}$ is an abelian subgroup of $\mathbb{Z}$. Check this.
$(1)$ Give a group isomorphism (an invertible homomorphism) from $m\mathbb{Z}$ to $\mathbb{Z}$.
$(2)$ Check that the inclusion map $i: m\mathbb{Z} \to \mathbb{Z}$ given by i(mk) $=$ mk is a group homomorphism. Prove that if $m \ge 2$ then there is no group homomorphism $p: \mathbb{Z} \to m\mathbb{Z}$ such that $p \circ i =$ id.
Remark: The above shows that abelian groups fail to have some of the properties of vector spaces. We will show later that a linear map satisfying the condition $p\circ i =$ id always exists.
Problem 3.3. Let $E =\mathbb{R} \times \mathbb{R}$, and define the addition operation
$$(x_{1}, y_{1}) + (x_{2}, y_{2}) = (x_{1} + x_{2}, y_{1}, +y_{2}),x_{1}, x_{2}, y_{1}, y_{2} \in \mathbb{R},$$
and the multiplication operation $\cdot$ : $\mathbb{R} \times  E \to E$ by
$$\lambda  \cdot  (x, y) = (\lambda x, y),\lambda , x, y \in \mathbb{R}.$$
Show that $E$ with the above operations $+$ and $\cdot$  is not a vector space. Which of the axioms is violated?
Problem 3.4. $(1)$ Prove that the axioms of vector spaces imply that
$$\alpha  \cdot  0 = 0$$
$$0 \cdot  v = 0$$
$$\alpha  \cdot  (-v) = -(\alpha  \cdot  v)$$
$$(-\alpha ) \cdot  v = -(\alpha  \cdot  v),$$

<!-- PAGE 119 -->
for all $v \in E$ and all $\alpha  \in K$, where $E$ is a vector space over $K$.
$(2)$ For every $\lambda  \in \mathbb{R}$ and every $x = (x_{1}, \dots  , x_{n}) \in \mathbb{R}^{n}$, define $\lambda x$ by
$$\lambda x = \lambda (x_{1}, \dots  , x_{n}) = (\lambda x_{1}, \dots  , \lambda x_{n}).$$
$$\mathbb{R}^{n}$$
Recall that every vector $x = (x_{1}, \dots  , x_{n}) \in$ can be written uniquely as
$$x = x_{1}e_{1} + \cdots  + x_{n}e_{n},$$
$$\mathbb{R}\mathbb{R}^{n}$$
where $e_{i} = (0, \dots  , 0, 1, 0, \dots  , 0)$, with a single $1$ in position $i$. For any operation $\cdot$ : $\times \to \mathbb{R}^{n}$, if $\cdot$  satisfies the Axiom (V1) of a vector space, then prove that for any $\alpha  \in \mathbb{R}$, we have
$$\alpha  \cdot  x = \alpha  \cdot  (x_{1}e_{1} + \cdots  + x_{n}e_{n}) = \alpha  \cdot  (x_{1}e_{1}) + \cdots  + \alpha  \cdot  (x_{n}e_{n}).$$
Conclude that $\cdot$  is completely determined by its action on the one-dimensional subspaces of $\mathbb{R}^{n}$ spanned by $e_{1}, \dots  , e_{n}$.
$$\mathbb{R}\mathbb{R}^{n} \mathbb{R}^{n}$$
$(3)$ Use $(2)$ to define operations $\cdot$ :  $\times \to$ that satisfy the Axioms (V1–V3), but for which Axiom V4 fails.
$$\mathbb{R}\mathbb{R}^{n} \mathbb{R}^{n}$$
$(4)$ For any operation $\cdot$ : $\times \to$ , prove that if $\cdot$  satisfies the Axioms (V2–V3), then for every rational number $r \in \mathbb{Q}$ and every vector $x \in \mathbb{R}^{n}$, we have
$$r \cdot  x = r(1 \cdot  x).$$
$$\mathbb{R}^{n}$$
In the above equation, $1 \cdot  x$ is some vector $(y_{1}, \dots  , y_{n}) \in$ not necessarily equal to $x = (x_{1}, \dots  , x_{n})$, and
$$r(1 \cdot  x) = (ry_{1}, \dots  , ry_{n}),$$
as in Part $(2)$.
$$\mathbb{Q}\mathbb{R}^{n} \mathbb{R}^{n}$$
Use $(4)$ to conclude that any operation $\cdot$ : $\times \to$ that satisfies the Axioms (V1–V3)
$$\mathbb{R}^{n}$$
is completely determined by the action of $1$ on the one-dimensional subspaces of spanned by $e_{1}, \dots  , e_{n}$.
Problem 3.5. Let $A_{1}$ be the following matrix:
$$A_{1} = \begin{pmatrix} 2 & 3 & 1 \\ 1 & 2 & -1 \\ 3 & 5 & 1 \end{pmatrix} .$$
$$--$$
Prove that the columns of $A_{1}$ are linearly independent. Find the coordinates of the vector $x = (6, 2, -7)$ over the basis consisting of the column vectors of $A_{1}$.
Problem 3.6. Let $A_{2}$ be the following matrix:
$$A_{2} = \begin{pmatrix} 1 & 2 & 1 & 1 \\ 2 & 3 & 2 & 3 \\ -1 & 0 & 1 & -1 \\ 2 & 1 & 3 & 0 \end{pmatrix} .$$
$$--$$
Express the fourth column of $A_{2}$ as a linear combination of the first three columns of $A_{2}$. Is the vector $x = (7, 14, -1, 2)$ a linear combination of the columns of $A_{2}$?

<!-- PAGE 120 -->
Problem 3.7. Let $A_{3}$ be the following matrix:
$$A_{3} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 2 \\ 1 & 2 & 3 \end{pmatrix} .$$
Prove that the columns of $A_{1}$ are linearly independent. Find the coordinates of the vector $x = (6, 9, 14)$ over the basis consisting of the column vectors of $A_{3}$.
Problem 3.8. Let $A_{4}$ be the following matrix:
$$A_{4} = \begin{pmatrix} 1 & 2 & 1 & 1 \\ 2 & 3 & 2 & 3 \\ -1 & 0 & 1 & -1 \\ 2 & 1 & 4 & 0 \end{pmatrix} .$$
$$--$$
Prove that the columns of $A_{4}$ are linearly independent. Find the coordinates of the vector $x = (7, 14, -1, 2)$ over the basis consisting of the column vectors of $A_{4}$.
Problem 3.9. Consider the following Haar matrix
$$H = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 1 & -1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & 0 & 1 \end{pmatrix} .$$
$$--$$
Prove that the columns of $H$ are linearly independent. Hint. Compute the product $H^{\top}H$.
Problem 3.10. Consider the following Hadamard matrix
$$H_{4} = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & -1 & 1 & -1 \\ 1 & 1 & -1 & -1 \\ 1 & 1 & 1 & 1 \end{pmatrix} .$$
$$--$$
Prove that the columns of $H_{4}$ are linearly independent. Hint. Compute the product $H_{4}^{\top} H_{4}$.
Problem 3.11. In solving this problem, do not use determinants.
$(1)$ Let $(u_{1}, \dots  , u_{m})$ and $(v_{1}, \dots  , v_{m})$ be two families of vectors in some vector space $E$. Assume that each $v_{i}$ is a linear combination of the $u_{j}s$, so that
$$v_{i} = a_{i1}u_{1} + \cdots  + a_{i m}u_{m},1 \le i \le m,$$

<!-- PAGE 121 -->
and that the matrix $A = (a_{i j})$ is an upper-triangular matrix, which means that if $1 \le j < i \le m$, then $a_{i j} = 0$. Prove that if $(u_{1}, \dots  , u_{m})$ are linearly independent and if all the diagonal entries of $A$ are nonzero, then $(v_{1}, \dots  , v_{m})$ are also linearly independent. Hint. Use induction on $m$.
$(2)$ Let $A = (a_{i j})$ be an upper-triangular matrix. Prove that if all the diagonal entries of $A$ are nonzero, then $A$ is invertible and the inverse $A^{-1}$ of $A$ is also upper-triangular. Hint. Use induction on $m$. Prove that if $A$ is invertible, then all the diagonal entries of $A$ are nonzero.
$(3)$ Prove that if the families $(u_{1}, \dots  , u_{m})$ and $(v_{1}, \dots  , v_{m})$ are related as in $(1)$, then $(u_{1}, \dots  , u_{m})$ are linearly independent $iff(v_{1}, \dots  , v_{m})$ are linearly independent.
Problem 3.12. In solving this problem, do not use determinants. Consider the $n \times  n$ matrix
$$A = \begin{pmatrix} 1 & 2 & 0 & 0 & \dots & 0 & 0 \\ 0 & 1 & 2 & 0 & \dots & 0 & 0 \\ 0 & 0 & 1 & 2 & \dots & 0 & 0 \\ \vdots & \vdots & \ddots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & \dots & 0 & 1 & 2 & 0 \\ 0 & 0 & \dots & 0 & 0 & 1 & 2 \\ 0 & 0 & \dots & 0 & 0 & 0 & 1 \end{pmatrix} .$$
$(1)$ Find the solution $x = (x_{1}, \dots  , x_{n})$ of the linear system
$$Ax = b,$$
for
$$b = \begin{pmatrix} b_{1} \\ b_{2} \\ \vdots \\ b_{n} \end{pmatrix} .$$
$(2)$ Prove that the matrix $A$ is invertible and find its inverse $A^{-1}$. Given that the number of atoms in the universe is estimated to be $\le 10^{82}$, compare the size of the coefficients the inverse of $A$ to $10^{82}$, if $n \ge 300$.
$(3)$ Assume $b$ is perturbed by a small amount $\delta b$ (note that $\delta b$ is a vector). Find the new solution of the system
$$A(x + \delta x) = b + \delta b,$$
where $\delta x$ is also a vector. In the case where $b = (0, \dots  , 0, 1)$, and $\delta b = (0, \dots  , 0, \epsilon$ ), show that
$$|(\delta x)_{1}| = 2^{n-1}|\epsilon |.$$

<!-- PAGE 122 -->
(where $(\delta x)_{1}$ is the first component of $\delta x)$.
$(4)$ Prove that $(A$ - $I)^{n} = 0$.
Problem 3.13. An $n \times  n$ matrix $N$ is nilpotent if there is some integer $r \ge 1$ such that $N^{r} = 0$.
$(1)$ Prove that if $N$ is a nilpotent matrix, then the matrix $I$ - $N$ is invertible and
$$(I -N)^{-1}= I + N + N^{2}+ \cdots  + N^{r-1}.$$
$(2)$ Compute the inverse of the following matrix $A$ using $(1)$:
$$A = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 0 & 1 & 2 & 3 & 4 \\ 0 & 0 & 1 & 2 & 3 \\ 0 & 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix} .$$
Problem 3.14. $(1)$ Let $A$ be an $n \times  n$ matrix. If $A$ is invertible, prove that for any $x \in \mathbb{R}^{n}$, if Ax $= 0$, then $x = 0$.
$(2)$ Let $A$ be an $m \times  n$ matrix and let $B$ be an $n \times  m$ matrix. Prove that $I_{m}$ - $AB$ is invertible iff $I_{n}$ - $BA$ is invertible. Hint. If for all $x \in \mathbb{R}^{n}$, Mx $= 0$ implies that $x = 0$, then $M$ is invertible.
Problem 3.15. Consider the following $n \times  n$ matrix, for $n \ge 3$:
$$B = \begin{pmatrix} 1 & -1 & -1 & -1 & \cdots & -1 & -1 \\ 1 & -1 & 1 & 1 & \cdots & 1 & 1 \\ 1 & 1 & -1 & 1 & \cdots & 1 & 1 \\ 1 & 1 & 1 & -1 & \cdots & 1 & 1 \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ 1 & 1 & 1 & 1 & \cdots & -1 & 1 \\ 1 & 1 & 1 & 1 & \cdots & 1 & -1 \end{pmatrix}$$
$(1)$ If we denote the columns of $B$ by $b_{1}, \dots  , b_{n}$, prove that
$$(n -3)b_{1} -(b_{2} + \cdots  + b_{n}) = 2(n -2)e_{1}$$
$$b_{1} -b_{2} = 2(e_{1} + e_{2})$$
$$b_{1} -b_{3} = 2(e_{1} + e_{3})$$
$$\vdots \vdots$$
$$b_{1} -b_{n} = 2(e_{1} + e_{n}),$$

<!-- PAGE 123 -->
where $e_{1}, \dots  , e_{n}$ are the canonical basis vectors of $\mathbb{R}^{n}$.
$(2)$ Prove that $B$ is invertible and that its inverse $A = (a_{ij})$ is given by
$$-$$
$$a_{11} = \frac{(n3)}{2(n -2)} ,a_{i1} = - \frac{1}{2(n -2)} 2 \le i \le n$$
and
$$-$$
$$a_{ii} = - \frac{(n3)}{2(n -2)} ,2 \le i \le n$$
$$a_{ji} = \frac{1}{2(n -2)} ,2 \le i \le n, j \neq  i.$$
$(3)$ Show that the $n$ diagonal $n \times  n$ matrices $D_{i}$ defined such that the diagonal entries of $D_{i}$ are equal the entries (from top down) of the ith column of $B$ form a basis of the space of $n \times  n$ diagonal matrices (matrices with zeros everywhere except possibly on the diagonal). For example, when $n = 4$, we have
$$D_{1} = ,$$
$$\begin{pmatrix} 1 & 0 & 0 & 0 & -1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & -1 & 0 & 0 \\ 0 & 0 & 1 & 0 & D_{2}=0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 \\ -1 & 0 & 0 & 0 & -1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & -1 & 0, & D_{4}=0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 \end{pmatrix}$$
$$D_{3} = .$$
$$-$$
Problem 3.16. Given any $m\times n$ matrix $A$ and any $n\times p$ matrix $B$, if we denote the columns of $A$ by $A^{1}, \dots  , A^{n}$ and the rows of $B$ by $B_{1}, \dots  , B_{n}$, prove that
$$AB = A^{1}B_{1} + \cdots  + A^{n}B_{n}.$$
Problem 3.17. Let $f$ : $E \to F$ be a linear map which is also a bijection (it is injective and surjective). Prove that the inverse function $f^{-1}: F \to E$ is linear.
Problem 3.18. Given two vectors spaces $E$ and $F$, let $(u_{i})_{i\in I}$ be any basis of $E$ and let $(v_{i})_{i\in I}$ be any family of vectors in $F$. Prove that the unique linear map $f$ : $E \to F$ such that $f(u_{i}) = v_{i}$ for all $i \in$ I is surjective $iff(v_{i})_{i\in I}$ spans $F$.
Problem 3.19. Let $f$ : $E \to F$ be a linear map with dim(E) $= n$ and dim(F) $= m$. Prove that $f$ has rank $1$ iff $f$ is represented by an $m \times  n$ matrix of the form
$$A = uv^{\top}$$
with $u$ a nonzero column vector of dimension $m$ and $v$ a nonzero column vector of dimension $n$.

<!-- PAGE 124 -->
Problem 3.20. Find a nontrivial linear dependence among the linear forms $\phi_{1} (x, y, z) =$ 2x - $y +$ 3z, $\phi_{2} (x, y, z) =$ 3x - 5y $+ z, \phi_{3} (x, y, z) =$ 4x - 7y $+ z$.
Problem 3.21. Prove that the linear forms $\phi_{1} (x, y, z) = x +$ 2y $+ z, \phi_{2} (x, y, z) =$ 2x $+$ 3y $+$ 3z, $\phi_{3} (x, y, z) =$ 3x $+$ 7y $+ z$ are linearly independent. Express the linear form $\phi (x, y, z) = x+y+z$ as a linear combination of $\phi_{1} , \phi_{2} , \phi_{3}$ .
