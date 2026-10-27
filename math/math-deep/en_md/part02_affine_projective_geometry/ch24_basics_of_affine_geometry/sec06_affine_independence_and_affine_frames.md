# Affine Independence and Affine Frames


<!-- PAGE 827 -->

## 24.6 Affine Independence and Affine Frames

Corresponding to the notion of linear independence in vector spaces, we have the notion of affine independence. Given a family $(a_{i})_{i\in I}$ of points in an affine space $E$, we will reduce the notion of (affine) independence of these points to the (linear) independence of the families $-\longrightarrow (a_{i}a_{j})_{j\in(I-{i})}$ of vectors obtained by choosing any $a_{i}$ as an origin. First, the following proposition shows that it is sufficient to consider only one of these families.
$$\longrightarrow$$

> **Proposition 24.4.** Given an affine space $E, E , +$ , let $(a_{i})_{i\in I}$ be a family of points in
$$-\longrightarrow -\longrightarrow$$
$E$. If the family $(a_{i}a_{j})_{j\in(I-{i})}$ is linearly independent for some $i \in$ I, then $(a_{i}a_{j})_{j\in(I-{i})}$ is linearly independent for every $i \in$ I.
$$-\longrightarrow$$

*Proof.* Assume that the family $(a_{i}a_{j})_{j\in(I-{i})}$ is linearly independent for some specific $i \in$ I. Let $k \in$ I with $k \neq  i$, and assume that there are some scalars $(\lambda_{j} )_{j\in(I-{k})}$ such that
$$\sum_{\in(I-{k}  \lambda_{j} -\longrightarrow a_{k}a_{j} = 0.$$
$$j})$$
Since
$$-\longrightarrow  -\longrightarrow  -\longrightarrow$$
$$a_{k}a_{j} =a_{k}a_{i} +a_{i}a_{j},$$
we have
$$\sum_{\in(I-{k}  \lambda_{j} -\longrightarrow a_{k}a_{j}= \sum_{\in(I-{k}  \lambda_{j} -\longrightarrow a_{k}a_{i} + \sum_{\in(I-{k}  \lambda_{j} -\longrightarrow a_{i}a_{j},$$
$$j})j})j})$$
$$= \sum_{\in(I-{k}  \lambda_{j} -\longrightarrow a_{k}a_{i} + \sum_{(I-{i,k}  \lambda_{j} -\longrightarrow a_{i}a_{j},$$
$$j})j\in$$
$$-\longrightarrow -\longrightarrow$$
$$= \sum_{(I-{i,k}  \lambda_{j} a_{i}a_{j} - \begin{pmatrix} \lambda_{j} \\ j & }) \end{pmatrix} \sum_{\in(I-{k}^{})}  a_{i}a_{k},$$
$$j\in })$$
and thus
$$-\longrightarrow -\longrightarrow$$
$$\sum_{(I-{i,k}  \lambda_{j} a_{i}a_{j} - \begin{pmatrix} \lambda_{j} \\ j & }) \end{pmatrix} \sum_{\in(I-{k}  a_{i}a_{k} = 0.$$
$$j\in })$$
$$-\longrightarrow$$
Since the family $(a_{i}a_{j})_{j\in(I-{i})}$ is linearly independent, we must have $\lambda_{j}  = 0$ for all $j \in$
$$(I -{i, k}) and \sum_{j}  \in (I-{k}) \lambda_{j}  = 0, which implies that \lambda_{j}  = 0 for all j \in (I -{k}).$$
We define affine independence as follows.
$$\longrightarrow$$

> **Definition 24.4.** Given an affine space $E, E , +$ , a family $(a_{i})_{i\in I}$ of points in $E$ is affinely
$$-\longrightarrow$$
independent if the family $(a_{i}a_{j})_{j\in(I-{i})}$ is linearly independent for some $i \in$ I.

<!-- PAGE 828 -->
$$\longrightarrow$$
$$EE$$
$$a_{2}$$
$$-\longrightarrow$$
$$a_{0}a_{2}$$
$$a_{0}a_{1}\overline{-\longrightarrow}$$
$$a_{0}a_{1}$$
$$Figure 24.14: Affine independence and linear independence$$
Definition 24.4 is reasonable, because by Proposition 24.4, the independence of the family $-\longrightarrow (a_{i}a_{j})_{j\in(I-{i})}$ does not depend on the choice of $a_{i}$. A crucial property of linearly independent vectors $(u_{1}, \dots  , u_{m})$ is that if a vector $v$ is a linear combination
$$v = \sum_{i=1}^{m}  \lambda_{i} u_{i}$$
of the $u_{i}$, then the $\lambda_{i}$  are unique. A similar result holds for affinely independent points.
$$\longrightarrow$$

> **Proposition 24.5.** Given an affine space $E, E , +$ , let $(a_{0}, \dots  , a_{m})$ be a family of $m + 1$
$$points in E.Let x \in E, and assume that x = \sum_{i}  m=0 \lambda_{i} a_{i}, where \sum_{i}  m-\longrightarrow  \lambda_{i}  = 1 .-\longrightarrow Then,$$
the family $(\lambda_{0} , \dots  , \lambda_{m}$ ) such that $x = m  \lambda_{i} a_{i}$ is unique iff the $family^{=0} (a_{0}a_{1}, \dots  ,a_{0}a_{m})$ is
$$linearly independent. \sum_{i}  =0$$

*Proof.* The proof is straightforward and is omitted. It is also given in Gallier $[71]$. Proposition 24.5 suggests the notion of affine frame. Affine frames are the affine analogues
$$\longrightarrow$$
of bases in vector spaces. Let $E, E , +$ be a nonempty affine space, and let $(a_{0}, \dots  , a_{m})$ be a family of $m + 1$ points in $E$. The family $(a_{0}, \dots  , a_{m})$ determines the family of $m$
$$-\longrightarrow  -\longrightarrow  \longrightarrow$$
vectors $(a_{0}a_{1}, \dots  ,a_{0}a_{m})$ in $E$ . Conversely, given a point $a_{0}$ in $E$ and a family of $m$ vectors
$$\longrightarrow$$
$(u_{1}, \dots  , u_{m})$ in $E$ , we obtain the family of $m+1$ points $(a_{0}, \dots  , a_{m})$ in $E$, where $a_{i} = a_{0}+u_{i}, 1 \le i \le m$. Thus, for any $m \ge 1$, it is equivalent to consider a family of $m + 1$ points $(a_{0}, \dots  , a_{m})$ in
$$\longrightarrow$$
$E$, and a pair $(a_{0}, (u_{1}, \dots  , u_{m}))$, where the $u_{i}$ are vectors in $E$ . Figure 24.14 illustrates the notion of affine independence.

<!-- PAGE 829 -->
Remark: The above observation also applies to infinite families $(a_{i})_{i\in I}$ of points in $E$ and
$$\longrightarrow$$
families $(u_{i})_{i\in I-{0}}$ of vectors in $E$ , provided that the index set $I$ contains $0$.
$$-\longrightarrow  -\longrightarrow  \longrightarrow  \longrightarrow$$
When $(a_{0}a_{1}, \dots  ,a_{0}a_{m})$ is a basis of $E$ then, for every $x \in E$, since $x = a_{0} + a_{0}x$, there is a unique family $(x_{1}, \dots  , x_{m})$ of scalars such that
$$-\longrightarrow -\longrightarrow$$
$$x = a_{0} + x_{1}a_{0}a_{1} + \cdots  + x_{m}a_{0}a_{m}.$$
The scalars $(x_{1}, \dots  , x_{m})$ may be considered as coordinates with respect to $-\longrightarrow  -\longrightarrow (a_{0}, (a_{0}a_{1}, \dots  ,a_{0}a_{m}))$. Since
$$!$$
$$-\longrightarrow$$
$$x = a_{0} + \sum_{i=1}^{m}  x_{i}a_{0}a_{i}iff x =1 - \sum_{i=1}^{m}  x_{i}a_{0} + \sum_{i=1}^{m}  x_{i}a_{i},$$
$x \in E$ can also be expressed uniquely as
$$x = \sum_{i=0}^{m}  \lambda_{i} a_{i}$$
$$with \sum_{i}  m=0 \lambda_{i}  = 1, and where \lambda_{0}  = 1 - \sum_{i}  m=1 x_{i}, and \lambda_{i}  = x_{i} for 1 \le i \le m. The scalars$$
$(\lambda_{0} , \dots  , \lambda_{m}$ ) are also certain kinds of coordinates with respect to $(a_{0}, \dots  , a_{m})$. All this is summarized in the following definition.
$$\longrightarrow$$

> **Definition 24.5.** Given an affine space $E, E , +$ , an affine frame with origin $a_{0}$ is a family
$$-\longrightarrow  -\longrightarrow$$
$(a_{0}, \dots  , a_{m})$ of $m + 1$ points in $E$ such that the list of vectors $(a_{0}a_{1}, \dots  ,a_{0}a_{m})$ is a basis of $\longrightarrow -\longrightarrow  -\longrightarrow E$ . The pair $(a_{0}, (a_{0}a_{1}, \dots  ,a_{0}a_{m}))$ is also called an affine frame with origin $a_{0}$. Then, every $x \in E$ can be expressed as
$$-\longrightarrow -\longrightarrow$$
$$x = a_{0} + x_{1}a_{0}a_{1} + \cdots  + x_{m}a_{0}a_{m}$$
for a unique family $(x_{1}, \dots  , x_{m})$ of scalars, called the coordinates of $x$ w.r.t. the affine frame $-\longrightarrow  -\longrightarrow (a_{0}, (a_{0}a_{1}, \dots , a_{0}a_{m}))$. Furthermore, every $x \in E$ can be written as
$$x = \lambda_{0} a_{0} + \cdots  + \lambda_{m} a_{m}$$
for some unique family $(\lambda_{0} , \dots  , \lambda_{m}$ ) of scalars such that $\lambda_{0} +\cdots +\lambda_{m}  = 1$ called the barycentric coordinates of $x$ with respect to the affine frame $(a_{0}, \dots  , a_{m})$. See Figure 24.15. The coordinates $(x_{1}, \dots  , x_{m})$ and the barycentric coordinates $(\lambda_{0} , \dots , \lambda_{m}$ ) are related by
$$the equations \lambda_{0}  = 1 - \sum_{i}  m=1 x_{i} and \lambda_{i}  = x_{i}, for 1 \le i \le m. An affine frame is called an$$
affine basis by some authors. A family $(a_{i})_{i\in I}$ of points in $E$ is affinely dependent if it is not affinely independent. We can also characterize affinely dependent families as follows.

<!-- PAGE 830 -->
$$x = (-1, 0,2)$$
$$a3= (1,3,2)$$
$$a2 = (-1,3,1)$$
$$a0 = (1,2,1)$$
$$a1 = (2,3,1)$$
$$\overline{O}$$
$$x = (-1, 0,2)$$
$$a3= (1,3,2)$$
$$a2 = (-1,3,1)$$
$$a0$$
$$a1 = (2,3,1)$$
$$\overline{O}$$

![Figure 24.15](../../assets/ch24/fig_24_15.png)

**Figure 24.15:** The affine frame $(a_{0}, a_{1}, a_{2}, a_{3})$ for $\mathbb{A}^{3}$. The coordinates for $x = (-1, 0, 2)$ are $x_{1} = -8/3, x_{2} = -1/3, x_{3} = 1$, while the barycentric coordinates for $x$ are $\lambda_{0}  = 3, \lambda_{1}  = -8/3, \lambda_{2}  = -1/3, \lambda_{3}  = 1$.
$$\longrightarrow$$

> **Proposition 24.6.** Given an affine space $E, E , +$ , let $(a_{i})_{i\in I}$ be a family of points in $E$. The family $(a_{i})_{i\in I}$ is affinely dependent iff there is a family $(\lambda_{i} )_{i\in I}$ such that $\lambda_{j}  \neq  0$ for some
$$\longrightarrow$$
$$j \in I, \sum_{i}  \in I \lambda_{i}  = 0, and \sum_{i}  \in I \lambda_{i} xa_{i} = 0 for every x \in E.$$

*Proof.* By Proposition 24.5, the family $(a_{i})_{i\in I}$ is affinely dependent iff the family of vectors $-\longrightarrow -\longrightarrow (a_{i}a_{j})_{j\in(I-{i})}$ is linearly dependent for some $i \in$ I. For any $i \in$ I, the family $(a_{i}a_{j})_{j\in(I-{i})}$ is linearly dependent iff there is a family $(\lambda_{j} )_{j\in(I-{i})}$ such that $\lambda_{j}  \neq  0$ for some $j$, and such that
$$\sum_{\in(I-{i}  \lambda_{j} -\longrightarrow a_{i}a_{j} = 0.$$
$$j})$$
Then, for any $x \in E$, we have
$$-\longrightarrow \longrightarrow \longrightarrow$$
$$\sum_{\in(I-{i}  \lambda_{j} a_{i}a_{j}= \sum_{\in(I-{i}  \lambda_{j} (xa_{j} -xa_{i})$$
$$j})j})$$
$$\longrightarrow \longrightarrow$$
$$= \sum_{\in(I-{i}  \lambda_{j} xa_{j} - \begin{pmatrix} \lambda_{j} \\ j & }) \end{pmatrix} \sum_{\in(I-{i}  xa_{i},$$
$$j)$$
$$and letting \lambda_{i}  = - \sum_{j}  , we get \sum_{i}^{}}  \in I \lambda_{i} \longrightarrow xa_{i} = 0, with \sum_{i}  \in I \lambda_{i}  = 0 and \lambda_{j}  \neq  0 for$$
$$some j \in I. The \begin{pmatrix} \in (I-{i})\lambda_{j} \\ converseis \end{pmatrix} obvious by setting  x = a_{i} for some  i such that \lambda_{i}  \neq  0, since$$
$$\sum_{i}  \in I \lambda_{i}  = 0 implies that \lambda_{j}  \neq  0, for some j \neq  i.$$

<!-- PAGE 831 -->
$$a_{2}$$
$$a_{0}a_{0}a_{1}$$
$$a_{3}$$
$$a_{0}a_{1}a_{0}a_{2}$$
$$a_{1}$$
$$Figure 24.16: Examples of affine frames and their convex hulls.$$
Even though Proposition 24.6 is rather dull, it is one of the key ingredients in the proof of beautiful and deep theorems about convex sets, such as Carath´eodory’s theorem, Radon’s theorem, and Helly’s theorem.
$$\longrightarrow$$
A family of two points (a, $b)$ in $E$ is affinely independent iff ab $\neq  0$, iff $a \neq  b$. If $a \neq  b$, the affine subspace generated by a and $b$ is the set of all points $(1-\lambda )a+\lambda b$, which is the unique line passing through a and $b$. A family of three points (a, $b, c)$ in $E$ is affinely independent $\longrightarrow  \longrightarrow$ iff ab and ac are linearly independent, which means that a, $b$, and $c$ are not on the same line (they are not collinear). In this case, the affine subspace generated by (a, $b, c)$ is the set of all points $(1$ - $\lambda$  - $\mu )a + \lambda b + \mu c$, which is the unique plane containing a, $b$, and $c$. A family of
$$\longrightarrow  \longrightarrow  \longrightarrow$$
four points (a, $b, c, d)$ in $E$ is affinely independent iff ab, ac, and ad are linearly independent, which means that a, $b, c$, and $d$ are not in the same plane (they are not coplanar). In this case, a, $b, c$, and $d$ are the vertices of a tetrahedron. Figure 24.16 shows affine frames and their convex hulls for |I| $= 0, 1, 2, 3$. Given $n+1$ affinely independent points $(a_{0}, \dots  , a_{n})$ in $E$, we can consider the set of points $\lambda_{0} a_{0} +\cdots +\lambda_{n} a_{n}$, where $\lambda_{0}  +\cdots +\lambda_{n}  = 1$ and $\lambda_{i}  \ge 0 (\lambda_{i}  \in \mathbb{R})$. Such affine combinations are called convex combinations. This set is called the convex hull of $(a_{0}, \dots  , a_{n})$ (or n-simplex spanned by $(a_{0}, \dots  , a_{n}))$. When $n = 1$, we get the segment between $a_{0}$ and $a_{1}$, including $a_{0}$ and $a_{1}$. When $n = 2$, we get the interior of the triangle whose vertices are $a_{0}, a_{1}, a_{2}$, including boundary points (the edges). When $n = 3$, we get the interior of the tetrahedron

<!-- PAGE 832 -->
whose vertices are $a_{0}, a_{1}, a_{2}, a_{3}$, including boundary points (faces and edges). The set
$$-\longrightarrow -\longrightarrow \mathbb{R}$$
$${a_{0} + \lambda_{1} a_{0}a_{1} + \cdots  + \lambda_{n} a_{0}a_{n} | where 0 \le \lambda_{i}  \le 1 (\lambda_{i}  \in )}$$
is called the parallelotope spanned by $(a_{0}, \dots  , a_{n})$. When $E$ has dimension $2$, a parallelotope is also called a parallelogram, and when $E$ has dimension $3$, a parallelepiped. Figure 24.17 shows the convex hulls and associated parallelotopes for |I| $= 0, 1, 2, 3$.
$$a0$$
$$\overline{a0} a1$$
$$a2$$
$$a0a1$$
$$a3$$
$$a0$$
$$a3$$
$$a1$$
$$a2$$
$$a0$$
$$a1$$

![Figure 24.17](../../assets/ch24/fig_24_17.png)

**Figure 24.17:** Examples of affine frames, convex hulls, and their associated parallelotopes. More generally, we say that a subset $V$ of $E$ is convex if for any two points a, $b \in V$ , we have $c \in V$ for every point $c = (1$ - $\lambda )a + \lambda b$, with $0 \le \lambda  \le 1 (\lambda  \in \mathbb{R})$.  Points are not vectors! The following example illustrates why treating points as
$$vectors may cause problems. Let a, b, c be three affinely independent points in \mathbb{A}^{3}.$$
Any point $x$ in the plane (a, $b, c)$ can be expressed as
$$x = \lambda_{0} a + \lambda_{1} b + \lambda_{2} c,$$
where $\lambda_{0}  + \lambda_{1}  + \lambda_{2}  = 1$. How can we compute $\lambda_{0} , \lambda_{1} , \lambda_{2}$ ? Letting $a = (a_{1}, a_{2}, a_{3}), b = (b_{1}, b_{2}, b_{3}), c = (c_{1}, c_{2}, c_{3})$, and $x = (x_{1}, x_{2}, x_{3})$ be the coordinates of a, $b, c, x$ in the standard frame of $\mathbb{A}^{3}$, it is tempting to solve the system of equations
