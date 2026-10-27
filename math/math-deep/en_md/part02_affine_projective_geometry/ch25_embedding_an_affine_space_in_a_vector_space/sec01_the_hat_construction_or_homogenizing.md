# The ``Hat Construction,'' or Homogenizing


<!-- PAGE 853 -->
Chapter $25$ Embedding an Affine Space in a Vector Space

## 25.1 The “Hat Construction,” or Homogenizing

For all practical purposes, most geometric objects, including curves and surfaces, live in affine spaces. A disadvantage of the affine world is that points and vectors live in disjoint universes. It is often more convenient, at least mathematically, to deal with linear objects (vector spaces, linear combinations, linear maps), rather than affine objects (affine spaces, affine combinations, affine maps). Actually, it would also be advantageous if we could manipulate points and vectors as if they lived in a common universe, using perhaps an extra bit of information to distinguish between them if necessary. Such a “homogenization” (or “hat construction”) can be achieved. As a matter of fact, such a homogenization of an affine space and its associated vector space will be very useful to define and manipulate rational curves and surfaces. Indeed, the hat construction yields a canonical construction of the projective completion of an affine space. It also leads to a very elegant method for obtaining the various formulae giving the derivatives of a polynomial curve, or the directional derivatives of polynomial surfaces. However, these formulae are not needed here. Thus we omit this topic, referring the readers to Gallier $[71]$. This chapter proceeds as follows. First, the construction of a vector space $E$ in which
$$\longrightarrow  b$$
both $E$ and $E$ are embedded as (affine) hyperplanes is described. It is shown how affine frames in $E$ become bases in $E$. It turns out that $E$ is characterized by a universality
$$b b$$
property: Affine maps to vector spaces extend uniquely to linear maps. As a consequence, affine maps between affine spaces $E$ and $F$ extend to linear maps between $E$ and $F$.
$$b b$$
Let us first explain how to distinguish between points and vectors practically, using what amounts to a “hacking trick.” Then, we will show that such a procedure can be put on firm mathematical grounds. Assume that we consider the real affine space $E$ of dimension $3$, and that we have some
$$853$$

<!-- PAGE 854 -->
affine frame $(a_{0}, (v_{1}, v_{2}, v_{2}))$. With respect to this affine frame, every point $x \in E$ is repre-
$$\longrightarrow$$
sented by its coordinates $(x_{1}, x_{2}, x_{3})$, where $a = a_{0} + x_{1}v_{1} + x_{2}v_{2} + x_{3}v_{3}$. A vector $u \in E$ is also represented by its coordinates $(u_{1}, u_{2}, u_{3})$ over the basis $(v_{1}, v_{2}, v_{2})$. One way to distinguish between points and vectors is to add a fourth coordinate, and to agree that points are represented by (row) vectors $(x_{1}, x_{2}, x_{3}, 1)$ whose fourth coordinate is $1$, and that vectors are represented by (row) vectors $(v_{1}, v_{2}, v_{3}, 0)$ whose fourth coordinate is $0$. This “programming trick” actually works very well. Of course, we are opening the door for strange elements such as $(x_{1}, x_{2}, x_{3}, 5)$, where the fourth coordinate is neither $1$ nor $0$. The question is, can we make sense of such elements, and of such a construction? The
$$answer is yes. We will present  a\longrightarrow  construction in which an affine space \begin{pmatrix} \longrightarrow \\ E,E \\ through \end{pmatrix} is embedded$$
in a vector space $E$, in which $E$ is embedded as a hyperplane passing  the origin,
$$b$$
and $E$ itself is embedded as an affine hyperplane, defined as $\omega^{-1} (1)$, for some linear form $\omega$ : $E \to \mathbb{R}$. In the case of an affine space $E$ of dimension $2$, we can think of $E$ as the vector $b  \longrightarrow  b \mathbb{R}^{3}$ space of dimension $3$ in which $E$ corresponds to the xy-plane, and $E$ corresponds to the plane of equation $z = 1$, parallel to the xy-plane and passing through the point on the z-axis of coordinates $(0, 0, 1)$. The construction of the vector space $E$ is presented in some detail
$$b$$
in Berger $[11]$. Berger explains the construction in terms of vector fields. We prefer a more geometric and simpler description in terms of simple geometric transformations, translations, and dilatations.
Remark: Readers with a good knowledge of geometry will recognize the first step in embedding an affine space into a projective space. We will also show that the homogenization $E$ of
$$b$$
$$an affine space \begin{pmatrix} \longrightarrow \\ E,E \\ maps. \end{pmatrix} , satisfies a universal property with respect to the extension of affine$$
maps to linear  As a consequence, the vector space $E$ is unique up to isomorphism,
$$b$$
and its actual construction is not so important. However, it is quite useful to visualize the space $E$, in order to understand well rational curves and rational surfaces. $b$ As usual, for simplicity, it is assumed that all vector spaces are defined over the $field\mathbb{R}$ of real numbers, and that all families of scalars (points and vectors) are finite. The extension to arbitrary fields and to families of finite support is immediate. We begin by defining
$$two very simple\longrightarrow  kinds of geometric (affine) transformations. Given an affine space \begin{pmatrix} \longrightarrow \\ E,E \\ that \end{pmatrix} ,$$
every $u \in E$ induces a mapping $t_{u}$ : $E \to E$, called a translation, and defined such $t_{u}(a) = a + u$ for every $a \in E$. Clearly, the set of translations is a vector space isomorphic to $\longrightarrow E$ . Thus, we will use the same notation $u$ for both the vector $u$ and the translation $t_{u}$. Given any point a and any scalar $\lambda  \in \mathbb{R}$, we define the mapping $H_{a,\lambda}$ : $E \to E$, called dilatation (or central dilatation, or homothety) of center a and ratio $\lambda$ , and defined such that
$$\longrightarrow$$
$$H_{a,\lambda}(x) = a + \lambda ax,$$
for every $x \in E$. We have $H_{a,\lambda}(a) = a$, and when $\lambda  \neq  0$ and $x \neq$  a, $H_{a,\lambda}(x)$ is on the line
$$\longrightarrow$$
defined by a and $x$, and is obtained by “scaling” ax by $\lambda$ . The effect is a uniform dilatation

<!-- PAGE 855 -->
(or contraction, if $\lambda  < 1)$. When $\lambda  = 0, H_{a,0}(x) = a$ for all $x \in E$, and $H_{a,0}$ is the constant affine map sending every point to a. If we assume $\lambda  \neq  1$, note that $H_{a,\lambda}$ is never the identity, and since a is a fixed point, $H_{a,\lambda}$ is never a translation. We now consider the set $E$ of geometric transformations from $E$ to $E$, consisting of the
$$b$$
union of the (disjoint) sets of translations and dilatations of ratio $\lambda$ ̸ $= 1$. We would like
$$\longrightarrow$$
to give this set the structure of a vector space, in such a way that both $E$ and $E$ can be naturally embedded into $E$. In fact, it will turn out that barycenters show up quite naturally
$$b$$
too! In order to “add” two dilatations $H_{a1,\lambda1}$ and $H_{a2,\lambda2}$, it turns out that it is more convenient to consider dilatations of the form $H_{a,1-\lambda}$, where $\lambda  \neq  0$. To see this, let us see the effect of such a dilatation on a point $x \in E$: We have
$$\longrightarrow  \longrightarrow \longrightarrow \longrightarrow$$
$$H_{a,1-\lambda}(x) = a + (1 -\lambda )ax = a +ax -\lambda ax = x + \lambda xa.$$
For simplicity of notation, let us denote $H_{a,1-\lambda}$ by $\langle a, \lambda \rangle$ . Then, we have
$$\longrightarrow$$
$$\langle a, \lambda \rangle (x) = x + \lambda xa.$$
Remarks:
$(1)$ Note that $H_{a,1-\lambda}(x) = H_{x,\lambda}(a)$.
$$\longrightarrow$$
$(2)$ Berger defines a map $h: E \to E$ as a vector field. Thus, each $\langle a, \lambda \rangle$ can be viewed
$$\longrightarrow$$
as the vector field $x \mapsto \lambda$ xa. Similarly, a translation $u$ can be viewed as the constant vector field $x \mapsto u$. Thus, we could define $E$ as the (disjoint) union of these two vector
$$b$$
fields. We prefer our view in terms of geometric transformations. Then, since
$$\longrightarrow \longrightarrow$$
$$\langle a_{1}, \lambda_{1} \rangle (x) = x + \lambda_{1} xa_{1}and\langle a_{2}, \lambda_{2} \rangle (x) = x + \lambda_{2} xa_{2},$$
if we want to define $\langle a_{1}, \lambda_{1} \rangle + \langle a_{2}, \lambda_{2} \rangle$ , we see that we have to distinguish between two cases:
$$b$$
$(1) \lambda_{1}  + \lambda_{2}  = 0$. In this case, since
$$\longrightarrow \longrightarrow \longrightarrow \longrightarrow -\longrightarrow$$
$$\lambda_{1} xa_{1} + \lambda_{2} xa_{2} = \lambda_{1} xa_{1} -\lambda_{1} xa_{2} = \lambda_{1} a_{2}a_{1},$$
we let
$$-\longrightarrow$$
$$\langle a_{1}, \lambda_{1} \rangle + \langle a_{2}, \lambda_{2} \rangle = \lambda_{1} a_{2}a_{1},$$
$$b$$
$$-\longrightarrow -\longrightarrow$$
where $\lambda_{1} a_{2}a_{1}$ denotes the translation associated with the vector $\lambda_{1} a_{2}a_{1}$.
$(2) \lambda_{1}  + \lambda_{2}  \neq  0$. In this case, the points $a_{1}$ and $a_{2}$ assigned the weights $\lambda_{1} /(\lambda_{1}  + \lambda_{2}$ ) and $\lambda_{2} /(\lambda_{1}  + \lambda_{2}$ ) have a barycenter
$$b = \frac{\lambda_{1}}{\lambda_{1}  + \lambda_{2}} a_{1} + \frac{\lambda_{2}}{\lambda_{1}  + \lambda_{2}} a_{2},$$

<!-- PAGE 856 -->
such that
$$\longrightarrow \longrightarrow \longrightarrow$$
$$xb = \frac{\lambda_{1}}{\lambda_{1}  + \lambda_{2}} xa_{1} + \frac{\lambda_{2}}{\lambda_{1}  + \lambda_{2}} xa_{2}.$$
Since
$$\longrightarrow \longrightarrow \longrightarrow$$
$$\lambda_{1} xa_{1} + \lambda_{2} xa_{2} = (\lambda_{1}  + \lambda_{2} )xb,$$
we let
$$\langle a_{1}, \lambda_{1} \rangle +b \langle a_{2}, \lambda_{2} \rangle = \frac{\lambda_{1}}{\lambda_{1}  + \lambda_{2}} a_{1} + \frac{\lambda_{2}}{\lambda_{1}  + \lambda_{2}} a_{2}, \lambda_{1}  + \lambda_{2} ,$$
the dilatation associated with the point $b$ and the scalar $\lambda_{1}  + \lambda_{2}$ . Given a translation defined by $u$ and a dilatation $\langle a, \lambda \rangle$ , since $\lambda  \neq  0$, we have
$$\longrightarrow \longrightarrow$$
$$\lambda xa + u = \lambda (xa + \lambda^{-1} u),$$
$$\longrightarrow$$
and so, letting $b = a + \lambda^{-1} u$, since ab $= \lambda^{-1} u$, we have
$$\longrightarrow \longrightarrow \longrightarrow  \longrightarrow \longrightarrow$$
$$\lambda xa + u = \lambda (xa + \lambda^{-1} u) = \lambda (xa +ab) = \lambda xb,$$
and we let
$$\langle a, \lambda \rangle + u = \langle a + \lambda^{-1} u, \lambda \rangle ,$$
$$b$$
the dilatation of center $a + \lambda^{-1} u$ and ratio $\lambda$ . The sum of two translations $u$ and $v$ is of course defined as the translation $u + v$. It is also natural to define multiplication by a scalar as follows:
$$\mu  \cdot  \langle a, \lambda \rangle = \langle a, \lambda \mu \rangle ,$$
and
$$\lambda  \cdot  u = \lambda u,$$
$$\longrightarrow$$
where $\lambda u$ is the product by a scalar in $E$ . We can now use the definition of the above operations to state the following proposition, showing that the “hat construction” described above has allowed us to achieve our goal of
$$\longrightarrow$$
embedding both $E$ and $E$ in the vector space $E$.
$$b$$

> **Proposition 25.1.** The set $E$ consisting of the disjoint union of the translations and the
$$b$$
dilatations $H_{a,1-\lambda} = \langle a, \lambda \rangle , \lambda  \in \mathbb{R}, \lambda  \neq  0$, is a vector space under the following operations of addition and multiplication by a scalar: If $\lambda_{1}  + \lambda_{2}  = 0$, then
$$-\longrightarrow$$
$$\langle a_{1}, \lambda_{1} \rangle + \langle a_{2}, \lambda_{2} \rangle = \lambda_{1} a_{2}a_{1};$$
$$b$$
if $\lambda_{1}  + \lambda_{2}  \neq  0$, then
$$\langle a_{1}, \lambda_{1} \rangle +b \langle a_{2}, \lambda_{2} \rangle = \frac{\lambda_{1}}{\lambda_{1}  + \lambda_{2}} a_{1} + \frac{\lambda_{2}}{\lambda_{1}  + \lambda_{2}} a_{2}, \lambda_{1}  + \lambda_{2} ,$$
$$\langle a, \lambda \rangle + u=u+ \langle a, \lambda \rangle = \langle a + \lambda^{-1} u, \lambda \rangle ,$$
$$b b$$
$$u+ v=u + v;$$
$$b$$

<!-- PAGE 857 -->
if $\mu  \neq  0$, then
$$\mu  \cdot  \langle a, \lambda \rangle =\langle a, \lambda \mu \rangle ,$$
$$0 \cdot  \langle a, \lambda \rangle =0;$$
and
$$\lambda  \cdot  u = \lambda u.$$
Furthermore, the map $\omega$ : $E \to \mathbb{R}$ defined such that
$$b$$
$$\omega (\langle a, \lambda \rangle )=\lambda ,$$
$$\omega (u)=0,$$
$$\longrightarrow$$
is a linear form, $\omega^{-1} (0)$ is a hyperplane isomorphic to $E$ under the injective linear map $\longrightarrow i: E \to E$ such that i(u) $= t_{u}$ (the translation associated with $u)$, and $\omega^{-1} (1)$ is an affine
$$b\longrightarrow$$
hyperplane isomorphic to $E$ with direction i(E ), under the injective affine map $j$ : $E \to E$,
$$b$$
where j(a) $= \langle$ a, $1\rangle$ for every $a \in E$. Finally, for every $a \in E$, we have
$$E = i\oplus \mathbb{R} j(a).$$
$$b \begin{pmatrix} \longrightarrow \\ E \end{pmatrix}$$

*Proof.* The verification that $E$ is a vector space is straightforward. The linear map mapping
$$b \longrightarrow  \longrightarrow$$
a vector $u$ to the translation defined by $u$ is clearly an injection $i: E \to E$ embedding $E$ as
$$b$$
an hyperplane in $E$. It is also clear that $\omega$  is a linear form. Note that
$$b$$
$$j(a + u) = \langle a + u, 1\rangle = \langle a, 1\rangle + u,$$
$$b$$
where $u$ stands for the translation associated with the vector $u$, and thus $j$ is an affine injection with associated linear map $i$. Thus, $\omega^{-1} (1)$ is indeed an affine hyperplane isomorphic to $E$ with direction $i$ , under the map $j$ : $E \to E$. Finally, from the definition of $+$ , for
$$every a \in E and every \begin{pmatrix} \longrightarrow \\ E \\ u \end{pmatrix} \in \longrightarrow E , sinceb b$$
$$i(u)+ \lambda  \cdot  j(a) = u+ \langle a, \lambda \rangle = \langle a + \lambda^{-1} u, \lambda \rangle ,$$
$$b b$$
when $\lambda$ ̸ $= 0$, we get any arbitrary $v \in E$ by picking $\lambda  = 0$ and $u = v$, and we get any
$$b\longrightarrow$$
arbitrary element $\langle b, \mu \rangle , \mu  \neq  0$, by picking $\lambda  = \mu$  and $u = \mu$ ab. Thus,
$$E = i+\mathbb{R} j(a),$$
$$b \begin{pmatrix} \longrightarrow \\ E \end{pmatrix}$$
$$and since i \begin{pmatrix} \longrightarrow \\ E \end{pmatrix} \cap \mathbb{R} j(a) = {0}, we have$$
$$E = i\oplus \mathbb{R} j(a),$$
$$b \begin{pmatrix} \longrightarrow \\ E \end{pmatrix}$$
for every $a \in E$.

<!-- PAGE 858 -->
$$a, \lambda$$
$$a, 1 = aj (E ) = \omega -1(1)$$
$$\Omega$$
$$u$$
$$i \overline{E}= \omega -1(0)$$
$$Figure 25.1: Embedding an affine space into a vector spaceE.$$
$$b$$
Figure 25.1 illustrates the embedding of the affine space $E$ into the vector space $E$, when
$$b$$
$E$ is an affine plane.
$$\longrightarrow$$
Note that $E$ is isomorphic to $E \cup (E \times \mathbb{R}^{*})$. Intuitively, we can think of $E$ as a stack of
$$b b$$
parallel hyperplanes, one for each $\lambda$ , a little bit like an infinite stack of very thin pancakes! There are two privileged pancakes: one corresponding to $E$, for $\lambda  = 1$, and one corresponding $\longrightarrow$ to $E$ , for $\lambda  = 0$.
$$\longrightarrow$$
$$From now on, we will identify j(E) and E, and i \begin{pmatrix} \longrightarrow \\ E \end{pmatrix} andE . We will also write \lambda a$$
instead of $\langle a, \lambda \rangle$ , which we will call a weighted point, and write 1a just as a. When we want to be more precise, we may also write $\langle$ a, $1\rangle$ as $\overline{a}$. In particular, when we consider the homogenized version  of the affine space $\mathbb{A}$ associated with the field $\mathbb{R}$ considered as an
$$affine space, we write  b \frac{\mathbb{A}}{\lambda} for \langle \lambda , 1\rangle , when viewing \lambda  as a point in both \mathbb{A} and\mathbb{A}, and simply$$
$$b$$
$\lambda$ , when viewing $\lambda$  as a vector in $\mathbb{R}$ and in $\mathbb{A}$. As an example, the expression $2 + 3$ denotes
$$b$$
$$the real number 5, in \mathbb{A}, \overline{(2 + 3)}/2 denotes the midpoint of the segment \begin{bmatrix} \overline{2},\overline{3} \end{bmatrix} , which can be$$
$\overline{denoted$ by $2}\overline{.}\overline{5$, and $2+3$ does not make sense $in}\mathbb{A}$, since it is not a barycentric combination. However, in $\mathbb{A}$, the expression $\overline{2 + 3}$ makes sense: It is the weighted point $\overline{2}\overline{.}\overline{5}, 2$ .
$$b$$
Then, in view of the fact that
$$\langle a + u, 1\rangle = \langle a, 1\rangle + u,$$
$$b$$
and since we are identifying $a + u$ with $\langle a + u, 1\rangle$ (under the injection $j)$, in the simplified notation the above reads as $a + u = a + u$. Thus, we go one step further, and denote $a + u$
$$b b$$

<!-- PAGE 859 -->
by $a + u$. However, since
$$\langle a, \lambda \rangle + u = \langle a + \lambda^{-1} u, \lambda \rangle ,$$
$$b$$
we will refrain from writing $\lambda a + u$ as $\lambda a + u$, because we find it too confusing. From
$$b$$
Proposition 25.1, for every $a \in E$, every element of $E$ can be written uniquely as $u + \lambda$ a.
$$b b$$
We also denote
$$\lambda a+ (-\mu )b$$
$$b$$
by
$$\lambda a-\mu b.$$
$$b$$
We can now justify rigorously the programming trick of the introduction of an extra coordinate to distinguish between points and vectors. First, we make a few observations. Given any family $(a_{i})_{i\in I}$ of points in $E$, and any family $(\lambda_{i} )_{i\in I}$ of scalars in $\mathbb{R}$, it is easily shown by induction on the size of I that the following holds:
$$(1) If \sum_{i}  \in I \lambda_{i}  = 0, then----\longrightarrow$$
$$\sum_{i\in I}  \langle a_{i}, \lambda_{i} \rangle = \sum_{i\in I}  \lambda_{i} a_{i},$$
where
$$----\longrightarrow$$
$$\sum_{i\in I}  \lambda_{i} a_{i} = \sum_{i\in I}  \lambda_{i} \longrightarrow ba_{i}$$
for any $b \in E$, which, by Proposition 24.1, is a vector independent of $b$, or
$$(2) If \sum_{i}  \in I \lambda_{i}  \neq  0, then$$
$$\sum_{i\in I}  \langle a_{i}, \lambda_{i} \rangle =* \sum_{i\in I}  \frac{\lambda_{i}}{\lambda_{i}} a_{i}, \sum_{i\in I}  \lambda_{i} +.$$
$$\sum_{i}  \in I$$
Thus, we see how barycenters reenter the scene quite naturally, and that in $E$, we can
$$b$$
$$make sense of \sum_{i}  \in I\langle a_{i}, \lambda_{i} \rangle , regardless of the value of \sum  \lambda_{i} . When \sum  i \lambda_{i}  = 1, the element$$
$$\sum_{i}  \langle a_{i}, \lambda_{i} \rangle belongs to the hyperplane \omega^{-1} (1), and^{i\in I} thus it is a point.^{\in I} When \sum_{i}  \lambda_{i}  = 0,$$
$$the^{\in I} linear combination of points \sum_{i}  \in I \lambda_{i} a_{i} is a vector, and when I = {1, \dots  , n},^{\in I} we allow$$
ourselves to write
$$\lambda_{1} a_{1}+ \cdots + \lambda_{n} a_{n},$$
$$b b$$
where some of the occurrences of $+$ can be replaced by - , as
$$b b$$
$$\lambda_{1} a_{1} + \cdots  + \lambda_{n} a_{n},$$
where the occurrences of - (if any) are replaced by -.
$$b$$
In fact, we have the following slightly more general property, which is left as an exercise.
