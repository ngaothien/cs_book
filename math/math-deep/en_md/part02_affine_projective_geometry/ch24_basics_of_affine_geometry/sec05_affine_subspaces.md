# Affine Subspaces


<!-- PAGE 821 -->
$$c$$
$$g_{1}$$
$$ab$$
$$c$$
$$g_{2}$$
$$ab$$
$$Figure 24.11: Barycenters, g_{1} =_{4}^{1} a +_{4}^{1} b +_{2}^{1} c,g_{2} = -a + b + c$$
$$\mathbb{A}\mathbb{A}^{2}$$
is a well-defined affine combination. Then, we can define the curve $F$ :  $\to$ such that
$$F(t) = (1 -t)^{3}a + 3t(1 -t)^{2}b + 3t^{2}(1 -t) c + t^{3}d.$$
Such a curve is called a B´ezier curve, and (a, $b, c, d)$ are called its control points. Note that the curve passes through a and $d$, but generally not through $b$ and $c$. It can be sbown that any point F(t) on the curve can be constructed using an algorithm performing affine interpolation steps (the de Casteljau algorithm).

## 24.5 Affine Subspaces

In linear algebra, a (linear) subspace can be characterized as a nonempty subset of a vector space closed under linear combinations. In affine spaces, the notion corresponding to the notion of (linear) subspace is the notion of affine subspace. It is natural to define an affine subspace as a subset of an affine space closed under affine combinations.
$$\longrightarrow$$

> **Definition 24.3.** Given an affine space $E, E , +$ , a subset $V$ of $E$ is an affine subspace (of $\longrightarrow$
$$E,E , +) if for every family of weighted points ((a_{i}, \lambda_{i} ))_{i\in I} in V such that \sum_{i}  \in I \lambda_{i}  = 1,$$
$$the barycenter \sum_{i}  \in I \lambda_{i} a_{i} belongs to V .$$
An affine subspace is also called a flat by some authors. According to Definition 24.3, the empty set is trivially an affine subspace, and every intersection of affine subspaces is an affine subspace.

<!-- PAGE 822 -->
$$\mathbb{R}^{2}$$
As an example, consider the subset $U$ of defined by
$$\mathbb{R}^{2}$$
$$U =(x, y) \in | ax + by = c,$$
i.e., the set of solutions of the equation
$$ax + by = c,$$
where it is assumed that $a \neq  0$ or $b \neq  0$. Given any $m$ points $(x_{i}, y_{i}) \in U$ and any $m$ scalars $\lambda_{i}$  such that $\lambda_{1}  + \cdots  + \lambda_{m}  = 1$, we claim that
$$\sum_{i=1}^{m}  \lambda_{i} (x_{i}, y_{i}) \in U.$$
Indeed, $(x_{i}, y_{i}) \in U$ means that
$$ax_{i} + by_{i} = c,$$
and if we multiply both sides of this equation by $\lambda_{i}$  and add up the resulting $m$ equations, we get
$$\sum_{i=1}^{m}  (\lambda_{i} ax_{i} + \lambda_{i} by_{i}) = \sum_{i=1}^{m}  \lambda_{i} c,$$
and since $\lambda_{1}  + \cdots  + \lambda_{m}  = 1$, we get
$$a \sum_{i=1}^{m}  \lambda_{i} x_{i}!+ b \sum_{i=1}^{m}  \lambda_{i} y_{i}!= \sum_{i=1}^{m}  \lambda_{i} !c = c,$$
which shows that
$$!$$
$$\sum_{i=1}^{m}  \lambda_{i} x_{i}, \sum_{i=1}^{m}  \lambda_{i} y_{i}= \sum_{i=1}^{m}  \lambda_{i} (x_{i}, y_{i}) \in U.$$
Thus, $U$ is an affine subspace of $\mathbb{A}^{2}$. In fact, it is just a usual line in $\mathbb{A}^{2}$.
$$\mathbb{R}^{2}$$
It turns out that $U$ is closely related to the subset of defined by
$$\longrightarrow$$
$$U =(x, y) \in \mathbb{R}^{2}| ax + by = 0,$$
i.e., the set of solutions of the homogeneous equation
$$ax + by = 0$$
obtained by setting the right-hand side of ax $+$ by $= c$ to zero. Indeed, for any $m$ scalars $\lambda_{i}$ , the same calculation as above yields that
$$\longrightarrow$$
$$\sum_{i=1}^{m}  \lambda_{i} (x_{i}, y_{i}) \in U ,$$

<!-- PAGE 823 -->
$$U$$
$$\longrightarrow$$
$$U$$
$$Figure 24.12: An affine line U and its direction.$$
this time without any restriction on the $\lambda_{i}$ , since the right-hand side of the equation is
$$\longrightarrow  \longrightarrow$$
null. Thus, $U$ is a subspace of $\mathbb{R}^{2}$. In fact, $U$ is one-dimensional, and it is just a usual line in $\mathbb{R}^{2}$. This line can be identified with a line passing through the origin of $\mathbb{A}^{2}$, a line that is parallel to the line $U$ of equation ax $+$ by $= c$, as illustrated in Figure 24.12. Now, if $(x_{0}, y_{0})$ is any point in $U$, we claim that
$$\longrightarrow$$
$$U = (x_{0}, y_{0}) +U ,$$
where
$$\longrightarrow n\longrightarrow o$$
$$(x_{0}, y_{0}) +U =(x_{0} + u_{1}, y_{0} + u_{2}) | (u_{1}, u_{2}) \in U.$$
$$\longrightarrow \longrightarrow$$
First, $(x_{0}, y_{0}) + U \subseteq U$, since $ax_{0} + by_{0} = c$ and $au_{1} + bu_{2} = 0$ for all $(u_{1}, u_{2}) \in U$ . Second, if $(x, y) \in U$, then ax $+$ by $= c$, and since we also have $ax_{0} + by_{0} = c$, by subtraction, we get
$$a(x -x_{0}) + b(y -y_{0}) = 0,$$
$$\longrightarrow  \longrightarrow$$
which shows that $(x$ - $x_{0}, y$ - $y_{0}) \in U$ , and thus $(x, y) \in (x_{0}, y_{0}) + U$ . Hence, we also have
$$\longrightarrow  \longrightarrow$$
$U \subseteq (x_{0}, y_{0}) + U$ , and $U = (x_{0}, y_{0}) + U$ . The above example shows that the affine line $U$ defined by the equation
$$ax + by = c$$
$$\longrightarrow$$
is obtained by “translating” the parallel line $U$ of equation
$$ax + by = 0$$

<!-- PAGE 824 -->
passing through the origin. In fact, given any point $(x_{0}, y_{0}) \in U$,
$$\longrightarrow$$
$$U = (x_{0}, y_{0}) +U .$$
More generally, it is easy to prove the following fact. Given any $m \times  n$ matrix $A$ and any
$$\mathbb{R}^{m} \mathbb{R}^{n}$$
vector $b \in$ , the subset $U$ of defined by
$$\mathbb{R}^{n}$$
$$U = {x \in | Ax = b}$$
is an affine subspace of $\mathbb{A}^{n}$. Actually, observe that Ax $= b$ should really be written as $Ax^{\top} = b$, to be consistent with our convention that points are represented by row vectors. We can also use the boldface notation for column vectors, in which case the equation is written as Ax $= b$. For the sake of minimizing the amount of notation, we stick to the simpler (yet incorrect) notation Ax $= b$. If we consider the corresponding homogeneous equation Ax $= 0$, the set
$$\longrightarrow$$
$$U = {x \in \mathbb{R}^{n}| Ax = 0}$$
is a subspace of $\mathbb{R}^{n}$, and for any $x_{0} \in U$, we have
$$\longrightarrow$$
$$U = x_{0} +U .$$
This is a general situation. Affine subspaces can be characterized in terms of subspaces of $\longrightarrow E$ . Let $V$ be a nonempty subset of $E$. For every family $(a_{1}, \dots  , a_{n})$ in $V$ , for any family $(\lambda_{1} , \dots  , \lambda_{n}$ ) of scalars, and for every point $a \in V$ , observe that $x \in E$ given by
$$x = a + \sum_{i=1}^{n}  \lambda_{i} \longrightarrow aa_{i}$$
is the barycenter of the family of weighted points
$$\begin{pmatrix} (a_{1}, \lambda_{1} ), \dots  , (a_{n}, \lambda_{n} ),a, 1 - & \lambda_{i} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \sum_{i=1}^{n}  ,$$
since
$$\sum_{i=1}^{n}  \lambda_{i}  + \begin{pmatrix} 1 - & \lambda_{i} \end{pmatrix} \sum_{i=1}^{n}  = 1.$$
$$\longrightarrow  \longrightarrow  \longrightarrow$$
Given any point $a \in E$ and any subset $V$ of $E$ , let $a + V$ denote the following subset of $E$:
$$\longrightarrow n\longrightarrow o$$
$$a +V =a + v | v \in V.$$
$$\longrightarrow$$

> **Proposition 24.2.** Let $E, E , +$ be an affine space.

<!-- PAGE 825 -->
$$\longrightarrow$$
$$EE$$
$$\longrightarrow$$
$$aV$$
$$\longrightarrow$$
$$V = a +V$$
$$Figure 24.13: An affine subspace V and its direction .$$
$(1) A$ nonempty subset $V$ of $E$ is an affine subspace iff for every point $a \in V$ , the set
$$\longrightarrow \longrightarrow$$
$$V_{a} = {ax | x \in V }$$
$$\longrightarrow  \longrightarrow$$
is a subspace of $E$ . Consequently, $V = a + V_{a}$. Furthermore,
$$\longrightarrow \longrightarrow$$
$$V = {xy | x, y \in V }$$
$$\longrightarrow  \longrightarrow  \longrightarrow  \longrightarrow$$
is a subspace of $E$ and $V_{a} = V$ for all $a \in E$. Thus, $V = a + V$ .
$$\longrightarrow  \longrightarrow  \longrightarrow$$
$(2)$ For any subspace $V$ of $E$ and for any $a \in E$, the set $V = a + V$ is an affine subspace.

*Proof.* The proof is straightforward, and is omitted. It is also given in Gallier $[71]$.
$$\longrightarrow$$
In particular, when $E$ is the natural affine space associated with a vector space $E$ ,
$$\longrightarrow$$
Proposition 24.2 shows that every affine subspace of $E$ is of the form $u + U$ , for a subspace $\longrightarrow  \longrightarrow  \longrightarrow U$ of $E$ . The subspaces of $E$ are the affine subspaces of $E$ that contain $0$.
$$\longrightarrow$$
The subspace $V$ associated with an affine subspace $V$ is called the direction of $V$ . It is
$$\times  \longrightarrow  \times  \longrightarrow  \longrightarrow$$
also clear that the map $+: V V \to V$ induced by $+: E E \to E$ confers to $V, V , +$ an affine structure. Figure 24.13 illustrates the notion of affine subspace.
$$\longrightarrow$$
By the dimension of the subspace $V$ , we mean the dimension of $V$ . An affine subspace of dimension $1$ is called a line, and an affine subspace of dimension $2$ is called a plane. An affine subspace of codimension $1$ is called a hyperplane (recall that a subspace $F$ of a vector space $E$ has codimension $1$ iff there is some subspace $G$ of dimension $1$ such that $E = F \oplus G$, the direct sum of $F$ and $G$, see Strang $[176]$ or Lang $[113])$.

<!-- PAGE 826 -->
We say that two affine subspaces $U$ and $V$ are parallel if their directions are identical.
$$\longrightarrow  \longrightarrow  \longrightarrow  \longrightarrow$$
Equivalently, since $U = V$ , we have $U = a + U$ and $V = b + U$ for any $a \in U$ and any
$$\longrightarrow$$
$b \in V$ , and thus $V$ is obtained from $U$ by the translation ab. In general, when we talk about $n$ points $a_{1}, \dots  , a_{n}$, we mean the sequence $(a_{1}, \dots  , a_{n})$, and not the set ${a_{1}, \dots  , a_{n}}$ (the $a_{i}’s$ need not be distinct).
$$\longrightarrow$$
By Proposition 24.2, a line is specified by a point $a \in E$ and a nonzero vector $v \in E$ , i.e., a line is the set of all points of the form $a + \lambda v$, for $\lambda  \in \mathbb{R}$.
$$\longrightarrow  \longrightarrow$$
We say that three points a, $b, c$ are collinear if the vectors ab and ac are linearly dependent. If two of the points a, $b, c$ are distinct, say $a \neq  b$, then there is a unique $\lambda  \in \mathbb{R}$ such $\longrightarrow \longrightarrow$ that ac $= \lambda$ ab, and we define the $ratio_{-\to ab}^{-\to ac} = \lambda$ .
$$\longrightarrow$$
A plane is specified by a point $a \in E$ and two linearly independent vectors $u, v \in E$ , i.e., a plane is the set of all points of the form $a + \lambda u + \mu v$, for $\lambda , \mu  \in \mathbb{R}$.
$$\longrightarrow  \longrightarrow  \longrightarrow$$
We say that four points a, $b, c, d$ are coplanar if the vectors ab, ac, and ad are linearly dependent. Hyperplanes will be characterized a little later.
$$\longrightarrow$$

> **Proposition 24.3.** Given an affine space $E, E , +$ , for any family $(a_{i})_{i\in I}$ of points in
$$E, the set V of barycenters \sum_{i}  \in I \lambda_{i} a_{i} (where \sum_{i}  \in I \lambda_{i}  = 1) is the smallest affine subspace$$
containing $(a_{i})_{i\in I}$.
$$Proof. If (a_{i})_{i\in I} is empty, then V = \emptyset , because of the condition \sum_{i}  \lambda_{i}  = 1. If (a_{i})_{i\in I} is$$
nonempty, then the smallest affine subspace containing $(a_{i})_{i\in I} must^{\in I}$ contain the set $V$ of
$$barycenters \sum_{i}  \lambda_{i} a_{i}, and thus, it is enough to show that V is closed under affine combina-$$
tions, which $is^{\in I}$ immediately verified. Given a nonempty subset $S$ of $E$, the smallest affine subspace of $E$ generated by $S$ is often denoted by $\langle S\rangle$ . For example, a line specified by two distinct points a and $b$ is denoted by $\langle$ a, $b\rangle$ , or even (a, $b)$, and similarly for planes, etc.
Remarks:
$(1)$ Since it can be shown that the barycenter of $n$ weighted points can be obtained by repeated computations of barycenters of two weighted points, a nonempty subset $V$ of $E$ is an affine subspace iff for every two points a, $b \in V$ , the set $V$ contains all barycentric combinations of a and $b$. If $V$ contains at least two points, then $V$ is an affine subspace iff for any two distinct points a, $b \in V$ , the set $V$ contains the line determined by a and $b$, that is, the set of all points $(1$ - $\lambda )a + \lambda b, \lambda  \in \mathbb{R}$.
$(2)$ This result still holds if the field $K$ has at least three distinct elements, but the proof is trickier!
