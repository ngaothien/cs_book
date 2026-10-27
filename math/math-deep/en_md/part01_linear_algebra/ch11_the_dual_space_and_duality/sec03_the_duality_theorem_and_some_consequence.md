# The Duality Theorem and Some Consequences


<!-- PAGE 427 -->
of algebraic geometry, a beautiful but formidable subject. For a taste of algebraic geometry, see Lang $[113]$ or Dummit and Foote $[55]$. The duality theorem (Theorem 11.4) shows that the situation is much simpler if we restrict our attention to linear subspaces; in this case
$$U =\mathcal{I}(\mathcal{Z}(U))andV =\mathcal{Z}(\mathcal{I}(V )).$$

> **Proposition 11.3.** We have $V \subseteq V^{00}$ for every subspace $V$ of $E$, and $U \subseteq U^{00}$ for every subspace $U$ of $E^{*}$.

*Proof.* Indeed, for any $v \in V$ , to show that $v \in V^{00}$ we need to prove that $u^{*}(v) = 0$ for all $u^{*} \in V^{0}$. However, $V^{0}$ consists of all linear forms $u^{*}$ such that $u^{*}(y) = 0$ for all $y \in V$ ; in particular, for a fixed $v \in V$ , we have $u^{*}(v) = 0$ for all $u^{*} \in V^{0}$ , as required. Similarly, for any $u^{*} \in U$, to show that $u^{*} \in U^{00}$ we need to prove that $u^{*}(v) = 0$ for all $v \in U^{0}$. However, $U^{0}$ consists of all vectors $v$ such that $f^{*}(v) = 0$ for all $f^{*} \in U$; in particular, for a fixed $u^{*} \in U$, we have $u^{*}(v) = 0$ for all $v \in U^{0}$ , as required. We will see shortly that in finite dimension, we have $V = V^{00}$ and $U = U^{00}$.  However, even though $V = V^{00}$ is always true, when $E$ is of infinite dimension, it is not always true that $U = U^{00}$ . Given a vector space $E$ and a subspace $U$ of $E$, by Theorem 3.8, every basis $(u_{i})_{i\in I}$ of $U$ can be extended to a basis $(u_{j})_{j\in I\cup J}$ of $E$, where I $\cap J = \emptyset$ .

## 11.3 The Duality Theorem and Some Consequences

We have the following important theorem adapted from $E$. Artin $[6]$ (Chapter $1)$.

> **Theorem 11.4.** (Duality theorem) Let $E$ be a vector space. The following properties hold:
(a) For every basis $(u_{i})_{i\in I}$ of $E$, the family $(u_{i}^{*} )_{i\in I}$ of coordinate forms is linearly independent.
$(b)$ For every subspace $V$ of $E$, we have $V^{00} = V$ .
$(c)$ For every subspace $V$ of finite codimension $m$ of $E$, for every subspace $W$ of $E$ such that $E = V \oplus W$ (where $W$ is of finite dimension $m)$, for every basis $(u_{i})_{i\in I}$ of $E$ such that $(u_{1}, \dots  , u_{m})$ is a basis of $W$, the family $(u_{1}^{*}, \dots  , u_{m}^{*})$ is a basis of the orthogonal $V^{0}$ of $V$ in $E^{*}$, so that
$$\dim(V^{0} ) = codim(V ).$$
Furthermore, we have $V^{00} = V$ .

<!-- PAGE 428 -->
$(d)$ For every subspace $U$ of finite dimension $m$ of $E^{*}$, the orthogonal $U^{0}$ of $U$ in $E$ is of finite codimension $m$, so that
$$codim(U^{0} ) = \dim(U).$$
Furthermore, $U^{00} = U$.

*Proof.* (a) Assume that
$$\sum_{i\in I}  \lambda_{i} u_{i}^{*} = 0,$$
for a family $(\lambda_{i} )_{i\in I}$ (of scalars in $K)$. Since $(\lambda_{i} )_{i\in I}$ has finite support, there is a finite subset $J$ of I such that $\lambda_{i}  = 0$ for all $i \in$ I - $J$, and we have
$$\sum_{j\in J}  \lambda_{j} u_{j}^{*} = 0.$$
$$Applying the linear form \sum_{j}  \in J \lambda_{j} u_{j}^{*} to each u_{j} (j \in J), by Definition 11.2, since u_{i}^{*} (u_{j}) = 1$$
if $i = j$ and $0$ otherwise, we get $\lambda_{j}  = 0$ for all $j \in J$, that is $\lambda_{i}  = 0$ for all $i \in$ I (by definition of $J$ as the support). Thus, $(u_{i}^{*} )_{i\in I}$ is linearly independent.
$(b)$ Clearly, we have $V \subseteq V^{00}$. If V̸ $= V^{00}$, then let $(u_{i})_{i\in I\cup J}$ be a basis of $V^{00}$ such that $(u_{i})_{i\in I}$ is a basis of $V$ (where I $\cap J = \emptyset$ ). Since V̸ $= V^{00}, u_{j0} \in V^{00}$ for some $j_{0} \in J$ (and thus, $j_{0} \in /$ I). Since $u_{j0} \in V^{00} , u_{j0}$ is orthogonal to every linear form in $V^{0}$ . Now, we have $u_{j0}^{*}(u_{i}) = 0$ for all $i \in$ I, and thus $u_{j0}^{*} \in V^{0}$ . However, $u_{j0}^{*}(u_{j0}) = 1$, contradicting the fact that $u_{j0}$ is orthogonal to every linear form in $V^{0}$ . Thus, $V = V^{00}$ .
$(c)$ Let $J =$ I $-{1, \dots  , m}$. Every linear form $f^{*} \in V^{0}$ is orthogonal to every $u_{j}$, for $j \in J$, and thus, $f^{*} (u_{j}) = 0$, for all $j \in J$. For such a linear form $f^{*} \in V^{0}$ , let
$$g^{*}= f^{*} (u_{1})u_{1}^{*} + \cdots  + f^{*}(u_{m})u_{m}^{*}.$$
We have $g^{*}(u_{i}) = f^{*} (u_{i})$, for every $i, 1 \le i \le m$. Furthermore, by definition, $g^{*}$ vanishes on all $u_{j}$, where $j \in J$. Thus, $f^{*}$ and $g^{*}$ agree on the basis $(u_{i})_{i\in I}$ of $E$, and so, $g^{*} = f^{*}$ . This shows that $(u_{1}^{*}, \dots  , u_{m}^{*})$ generates $V^{0}$ , and since it is also a linearly independent family, $(u_{1}^{*}, \dots  , u_{m}^{*})$ is a basis of $V^{0}$ . It is then obvious that $dim(V^{0}$ ) $=$ codim(V ), and by part $(b)$, we have $V^{00} = V$ .
$(d)$ Let $(u_{1}^{*}, \dots  , u_{m}^{*})$ be a basis of $U$. Note that the map $h: E \to K^{m}$ defined such that
$$h(v) = (u_{1}^{*}(v), \dots  , u_{m}^{*}(v))$$
for every $v \in E$, is a linear map, and that its kernel Ker $h$ is precisely $U^{0}$ . Then, by Proposition 6.16,
$$E \approx \mathrm{Ker} (h) \oplus \mathrm{Im} h = U^{0}\oplus \mathrm{Im} h,$$
and since dim(Im $h) \le m$, we deduce that $U^{0}$ is a subspace of $E$ of finite codimension at most $m$, and by $(c)$, we have $dim(U^{00}$ ) $= codim(U^{0}$ ) $\le m =$ dim(U). However, it is clear that $U \subseteq U^{00}$ , which implies dim(U) $\le dim(U^{00}$ ), and so $dim(U^{00}$ ) $=$ dim(U) $= m$, and we must have $U = U^{00}$ .

<!-- PAGE 429 -->
Part (a) of Theorem 11.4 shows that
$$\dim(E) \le \dim(E^{*}).$$
When $E$ is of finite dimension $n$ and $(u_{1}, \dots  , u_{n})$ is a basis of $E$, by part $(c)$, the family $(u_{1}^{*}, \dots  , u_{n}^{*})$ is a basis of the dual space $E^{*}$, called the dual basis of $(u_{1}, \dots  , u_{n})$. This fact was also proven directly in Theorem 3.26. Define the function $\mathcal{E} (\mathcal{E}$ for equations) from subspaces of $E$ to subspaces of $E^{*}$ and the function $\mathcal{Z} (\mathcal{Z}$ for zeros) from subspaces of $E^{*}$ to subspaces of $E$ by
$$\mathcal{E}(V ) = V^{0} ,V \subseteq E$$
$$\mathcal{Z}(U) = U^{0} ,U \subseteq E^{*}.$$
By Parts $(c)$ and $(d)$ of Theorem 11.4,
$$(\mathcal{Z} \circ E)(V ) = V^{00}= V$$
$$(\mathcal{E} \circ Z)(U) = U^{00}= U,$$
so $\mathcal{Z} \circ E =$ id and $\mathcal{E} \circ Z =$ id, and the maps $\mathcal{E}$ and $\mathcal{Z}$ are inverse bijections. These maps set up a duality between subspaces of $E$ and subspaces of $E^{*}$. In particular, every subspace $V \subseteq E$ of dimension $m$ is the set of common zeros of the space of linear forms (equations) $V^{0}$ , which has dimension $n$ - $m$. This confirms the claim we made about the dimension of the subpsace defined by a set of linear equations.  One should be careful that this bijection does not extend to subspaces of $E^{*}$ of infinite dimension.  When $E$ is of infinite dimension, for every basis $(u_{i})_{i\in I}$ of $E$, the family $(u_{i}^{*} )_{i\in I}$ of coordinate forms is never a basis of $E^{*}$. It is linearly independent, but it is “too small” to generate $E^{*}$. For example, if $E = \mathbb{R}^{(N)}$, where $\mathbb{N} = {0, 1, 2, \dots$ }, the map $f$ : $E \to \mathbb{R}$ that sums the nonzero coordinates of a vector in $E$ is a linear form, but it is easy to see that it cannot be expressed as a linear combination of coordinate forms. As a consequence, when $E$ is of infinite dimension, $E$ and $E^{*}$ are not isomorphic. We now discuss some applications of the duality theorem.
$$\mathbb{R}^{n}$$
Problem $1$ . Suppose that $V$ is a subspace of of dimension $m$ and that $(v_{1}, \dots  , v_{m})$ is a basis of $V$ . The problem is to find a basis of $V^{0}$ . We first extend $(v_{1}, \dots  , v_{m})$ to a basis $(v_{1}, \dots  , v_{n}) of\mathbb{R}^{n}$, and then by part $(c)$ of Theorem 11.4, we know that $(v_{m+1}^{*}, \dots  , v_{n}^{*})$ is a basis of $V^{0}$ .
$$\mathbb{R}^{4}$$

> **Example 11.6.** For example, suppose that $V$ is the subspace of spanned by the two linearly independent vectors
$$v_{1} = \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \end{pmatrix} v_{2} = \begin{pmatrix} 1 \\ 1 \\ -1 \\ 1 \end{pmatrix} ,$$
$$-$$

<!-- PAGE 430 -->
the first two vectors of the Haar basis in $\mathbb{R}^{4}$. The four columns of the Haar matrix
$$W = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 1 & -1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & 0 & 1 \end{pmatrix}$$
$$--$$
form a basis of $\mathbb{R}^{4}$, and the inverse of $W$ is given by
$$W^{-1}  = \begin{pmatrix} 1/4 & 0 & 0 & 0 \\ 0 & 1/4 & 0 & 0 \\ 0 & 0 & 1/2 & 0 \\ 0 & 0 & 0 & 1/2 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & -1 & -1 \\ 1 & -1 & 0 & 0 \\ 0 & 0 & 1 & 1 \end{pmatrix} = \begin{pmatrix} 1/4 & 1/4 & 1/4 & 1/4 \\ 1/4 & 1/4 & -1/4 & -1/4 \\ 1/2 & -1/2 & 0 & 0 \\ 0 & 0 & 1/2 & 1/2 \end{pmatrix} .$$
$$--$$
Since the dual basis $(v_{1}^{*}, v_{2}^{*}, v_{3}^{*}, v_{4}^{*})$ is given by the rows of $W^{-1}$, the last two rows of $W^{-1}$,
$$\begin{pmatrix} 1/2 & -1/2 & 0 & 0 \\ 0 & 0 & 1/2 & -1/2 \end{pmatrix} ,$$
form a basis of $V^{0}$ . We also obtain a basis by rescaling by the factor $1/2$, so the linear forms given by the row vectors
$$\begin{pmatrix} 1 & -1 & 0 & 0 \\ 0 & 0 & 1 & -1 \end{pmatrix}$$
form a basis of $V^{0}$ , the space of linear forms (linear equations) that vanish on the subspace $V$ . The method that we described to find $V^{0}$ requires first extending a basis of $V$ and then inverting a matrix, but there is a more direct method. Indeed, let $A$ be the $n \times  m$ matrix whose columns are the basis vectors $(v_{1}, \dots  , v_{m})$ of $V$ . Then a linear form $u$ represented by a row vector belongs to $V^{0}$ iff $uv_{i} = 0$ for $i = 1, \dots  , m$ iff
$$uA = 0$$
iff
$$A^{\top}u^{\top}= 0.$$
Therefore, all we need to do is to find a basis of the nullspace of $A^{\top}$. This can be done quite effectively using the reduction of a matrix to reduced row echelon form (rref); see Section 8.10.

> **Example 11.7.** For example, if we reconsider the previous example, $A^{\top}u^{\top} = 0$ becomes
$$\begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & -1 & -1 \end{pmatrix} \begin{pmatrix} u_{1} \\ u_{2} \\ u_{3} \\ u_{4} \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} .$$

<!-- PAGE 431 -->
Since the rref of $A^{\top}$ is
$$\begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 \end{pmatrix} ,$$
the above system is equivalent to
$$\begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} u_{1} \\ u_{2} \\ u_{3} \\ u_{4} \end{pmatrix} = \begin{pmatrix} u_{1} + u_{2} \\ u_{3} + u_{4} \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} ,$$
where the free variables are associated with $u_{2}$ and $u_{4}$. Thus to determine a basis for the kernel of $A^{\top}$, we set $u_{2} = 1, u_{4} = 0$ and $u_{2} = 0, u_{4} = 1$ and obtain a basis for $V^{0}$ as
$$\begin{pmatrix} 1 & -1 & 0 & 0 \end{pmatrix} , \begin{pmatrix} 0 & 0 & 1 & -1 \end{pmatrix} .$$
Problem $2$ . Let us now consider the problem of finding a basis of the hyperplane $H$ in $\mathbb{R}^{n}$ defined by the equation
$$c_{1}x_{1} + \cdots  + c_{n}x_{n} = 0.$$
More precisely, if $u^{*}(x_{1}, \dots  , x_{n})$ is the linear form in $(\mathbb{R}^{n})^{*}$ given by $u^{*}(x_{1}, \dots  , x_{n}) = c_{1}x_{1} + \cdots  + c_{n}x_{n}$, then the hyperplane $H$ is the kernel of $u^{*}$. Of course we assume that some $c_{j}$ is nonzero, in which case the linear form $u^{*}$ spans a one-dimensional subspace $U$ of $(\mathbb{R}^{n})^{*}$, and $U^{0} = H$ has dimension $n$ - $1$. Since $u^{*}$ is not the linear form which is identically zero, there is a smallest positive index $j \le n$ such that $c_{j} \neq  0$, so our linear form is really $u^{*}(x_{1}, \dots  , x_{n}) = c_{j}x_{j} + \cdots  + c_{n}x_{n}$. We claim that the following $n$ - $1$ vectors (in $\mathbb{R}^{n})$ form a basis of $H$:
$$12\dots j -1jj + 1\dots n -1$$
$$1$$
$$2$$
$$\vdots$$
$$j -1 \begin{pmatrix} 1 & 0 & \dots & 0 & 0 & 0 & \dots & 0 \\ 0 & 1 & \dots & 0 & 0 & 0 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & 1 & 0 & 0 & \dots & 0 \\ 0 & 0 & \dots & 0 & -c_{j+1}/c_{j} & -c_{j+2}/c_{j} & \dots & -c_{n}/c_{j} \\ 0 & 0 & \dots & 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & \dots & 0 & 0 & 1 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & 0 & 0 & 0 & \dots & 1 \end{pmatrix}$$
$$j.$$
$$j + 1$$
$$j + 2$$
$$\vdots$$
$$n$$
Observe that the $(n-1)\times$ (n-1) matrix obtained by deleting row $j$ is the identity matrix, so the columns of the above matrix are linearly independent. A simple calculation also shows that the linear form $u^{*}(x_{1}, \dots  , x_{n}) = c_{j}x_{j} +\cdots +c_{n}x_{n}$ vanishes on every column of the above

<!-- PAGE 432 -->
matrix. For a concrete example in $\mathbb{R}^{6}$, if $u^{*}(x_{1}, \dots  , x_{6}) = x_{3} + 2x_{4} + 3x_{5} + 4x_{6}$, we obtain the basis for the hyperplane $H$ of equation
$$x_{3} + 2x_{4} + 3x_{5} + 4x_{6} = 0$$
given by the following matrix:
$$\begin{pmatrix} 1 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & -2 & -3 & -4 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$\mathbb{R}^{n}$$
Problem $3$ . Conversely, given a hyperplane $H$ in given as the span of $n -1$ linearly vectors $(u_{1}, \dots  , u_{n-1})$, it is possible using determinants to find a linear form $(\lambda_{1} , \dots  , \lambda_{n}$ ) that vanishes on $H$. In the case $n = 3$, we are looking for a row vector $(\lambda_{1} , \lambda_{2} , \lambda_{3}$ ) such that if
$$u = \begin{pmatrix} u_{1} \\ u_{2} \\ u_{3} \end{pmatrix} andv = \begin{pmatrix} v_{1} \\ v_{2} \\ v_{3} \end{pmatrix}$$
are two linearly independent vectors, then
$$\begin{pmatrix} u_{1} & u_{2} & u_{2} \\ v_{1} & v_{2} & v_{2} \end{pmatrix} \begin{pmatrix} \lambda_{1} \\ \lambda_{2} \\ \lambda_{3} \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} ,$$
and the cross-product $u \times  v$ of $u$ and $v$ given by
$$u \times  v = \begin{pmatrix} u_{2}v_{3} -u_{3}v_{2} \\ u_{3}v_{1} -u_{1}v_{3} \\ u_{1}v_{2} & u_{2}v_{1} \end{pmatrix}$$
$$-$$
is a solution. In other words, the equation of the plane spanned by $u$ and $v$ is
$$(u_{2}v_{3} -u_{3}v_{2})x + (u_{3}v_{1} -u_{1}v_{3})y + (u_{1}v_{2} -u_{2}v_{1})z = 0.$$
Problem $4$ . Here is another example illustrating the power of Theorem 11.4. Let $E = M_{n}(\mathbb{R})$, and consider the equations asserting that the sum of the entries in every row of a matrix $A \in M_{n}(\mathbb{R})$ is equal to the same number. We have $n$ - $1$ equations
$$\sum_{j=1}^{n}  (a_{ij} -a_{i+1j}) = 0,1 \le i \le n -1,$$
