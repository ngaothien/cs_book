# Affine Spaces


<!-- PAGE 805 -->
Chapter $24$ Basics of Affine Geometry L’alg`ebre n’est qu’une g´eom´etrie ´ecrite; la g´eom´etrie n’est qu’une alg`ebre figur´ee. —Sophie Germain

## 24.1 Affine Spaces

Geometrically, curves and surfaces are usually considered to be sets of points with some special properties, living in a space consisting of “points.” Typically, one is also interested in geometric properties invariant under certain transformations, for example, translations, rotations, projections, etc. One could model the space of points as a vector space, but this is not very satisfactory for a number of reasons. One reason is that the point corresponding to the zero vector $(0)$, called the origin, plays a special role, when there is really no reason to have a privileged origin. Another reason is that certain notions, such as parallelism, are handled in an awkward manner. But the deeper reason is that vector spaces and affine spaces really have different geometries. The geometric properties of a vector space are invariant under the group of bijective linear maps, whereas the geometric properties of an affine space are invariant under the group of bijective affine maps, and these two groups are not isomorphic. Roughly speaking, there are more affine maps than linear maps. Affine spaces provide a better framework for doing geometry. In particular, it is possible to deal with points, curves, surfaces, etc., in an intrinsic manner, that is, independently of any specific choice of a coordinate system. As in physics, this is highly desirable to really understand what is going on. Of course, coordinate systems have to be chosen to finally carry out computations, but one should learn to resist the temptation to resort to coordinate systems until it is really necessary. Affine spaces are the right framework for dealing with motions, trajectories, and physical forces, among other things. Thus, affine geometry is crucial to a clean presentation of kinematics, dynamics, and other parts of physics (for example, elasticity). After all, a rigid motion is an affine map, but not a linear map in general. Also, given an $m \times  n$ matrix $A$
$$805$$

<!-- PAGE 806 -->
$$\mathbb{R}^{m}\mathbb{R}^{n}$$
and a vector $b \in$ , the set $U = {x \in$ | Ax $= b}$ of solutions of the system Ax $= b$ is an affine space, but not a vector space (linear space) in general.
$$Use coordinate systems only when needed!$$
This chapter proceeds as follows. We take advantage of the fact that almost every affine concept is the counterpart of some concept in linear algebra. We begin by defining affine spaces, stressing the physical interpretation of the definition in terms of points (particles) and vectors (forces). Corresponding to linear combinations of vectors, we define affine combinations of points (barycenters), realizing that we are forced to restrict our attention to families of scalars adding up to $1$. Corresponding to linear subspaces, we introduce affine subspaces as subsets closed under affine combinations. Then, we characterize affine subspaces in terms of certain vector spaces called their directions. This allows us to define a clean notion of parallelism. Next, corresponding to linear independence and bases, we define affine independence and affine frames. We also define convexity. Corresponding to linear maps, we define affine maps as maps preserving affine combinations. We show that every affine map is completely defined by the image of one point and a linear map. Then, we investigate briefly some simple affine maps, the translations and the central dilatations. At this point, we give a glimpse of affine geometry. We prove the theorems of Thales, Pappus, and Desargues. After this, the definition of affine hyperplanes in terms of affine forms is reviewed. The section ends with a closer look at the intersection of affine subspaces. Our presentation of affine geometry is far from being comprehensive, and it is biased toward the algorithmic geometry of curves and surfaces. For more details, the reader is referred to Pedoe $[141]$, Snapper and Troyer $[168]$, Berger $[11, 12]$, Coxeter $[44]$, Samuel $[148]$, Tisseron $[181]$, Fresnel $[66]$, Vienne $[191]$, and Hilbert and Cohn-Vossen $[95]$. Suppose we have a particle moving in 3D space and that we want to describe the trajectory of this particle. If one looks up a good textbook on dynamics, such as Greenwood $[85]$, one finds out that the particle is modeled as a point, and that the position of this point $x$ is
$$\mathbb{R}^{3}$$
determined with respect to a “frame” in by a vector. Curiously, the notion of a frame is rarely defined precisely, but it is easy to infer that a frame is a pair $(O, (e_{1}, e_{2}, e_{3}))$ consisting of an origin $O$ (which is a point) together with a basis of three vectors $(e_{1}, e_{2}, e_{3})$. For
$$\mathbb{R}^{3}$$
example, the standard frame in has origin $O = (0, 0, 0)$ and the basis of three vectors $e_{1} = (1, 0, 0), e_{2} = (0, 1, 0)$, and $e_{3} = (0, 0, 1)$. The position of a point $x$ is then defined by the “unique vector” from $O$ to $x$. But wait a minute, this definition seems to be defining frames and the position of a point without defining what a point is! Well, let us identify points with elements $of\mathbb{R}^{3}$. If so, given any two points $a = (a_{1}, a_{2}, a_{3})$ and $b = (b_{1}, b_{2}, b_{3})$, there is a unique free vector, denoted by $\longrightarrow  \longrightarrow$ ab, from a to $b$, the vector ab $= (b_{1}$ - $a_{1}, b_{2}$ - $a_{2}, b_{3}$ - $a_{3})$. Note that
$$\longrightarrow$$
$$b = a +ab,$$

<!-- PAGE 807 -->
$$b$$
$$\longrightarrow$$
$$ab$$
$$a$$
$$O$$
$$Figure 24.1: Points and free vectors.$$
addition being understood as addition in $\mathbb{R}^{3}$. Then, in the standard frame, given a point
$$\longrightarrow$$
$x = (x_{1}, x_{2}, x_{3})$, the position of $x$ is the vector Ox $= (x_{1}, x_{2}, x_{3})$, which coincides with the point itself. In the standard frame, points and vectors are identified. Points and free vectors are illustrated in Figure 24.1. What if we pick a frame with a different origin, say $\Omega = (\omega_{1} , \omega_{2} , \omega_{3}$ ), but the same basis vectors $(e_{1}, e_{2}, e_{3})$? This time, the point $x = (x_{1}, x_{2}, x_{3})$ is defined by two position vectors:
$$\longrightarrow$$
$$Ox = (x_{1}, x_{2}, x_{3})$$
in the frame $(O, (e_{1}, e_{2}, e_{3}))$ and
$$\longrightarrow$$
$$\Omega x = (x_{1} -\omega_{1} , x_{2} -\omega_{2} , x_{3} -\omega_{3} )$$
in the frame $(\Omega , (e_{1}, e_{2}, e_{3}))$. See Figure 24.2. This is because
$$\longrightarrow  \longrightarrow  \longrightarrow \longrightarrow$$
$$Ox =O\Omega +\Omega xandO\Omega = (\omega_{1} , \omega_{2} , \omega_{3} ).$$
We note that in the second frame $(\Omega , (e_{1}, e_{2}, e_{3}))$, points and position vectors are no longer identified. This gives us evidence that points are not vectors. It may be computationally convenient to deal with points using position vectors, but such a treatment is not frame invariant, which has undesirable effects. Inspired by physics, we deem it important to define points and properties of points that are frame invariant. An undesirable side effect of the present approach shows up if we attempt to define linear combinations of points. First, let us review the notion of linear combination of vectors. Given two vectors $u$ and $v$ of coordinates $(u_{1}, u_{2}, u_{3})$ and $(v_{1}, v_{2}, v_{3})$ with respect

<!-- PAGE 808 -->
$$e3$$
$$e$$
$$2$$
$$x\overline{\Omega}$$
$$\Omega e$$
$$1$$
$$x$$
$$e3x$$
$$O$$
$$e$$
$$1\overline{O}\overline{e}$$
$$2$$
$$Figure 24.2: The two position vectors for the point x.$$
to the basis $(e_{1}, e_{2}, e_{3})$, for any two scalars $\lambda , \mu$ , we can define the linear combination $\lambda u+\mu v$ as the vector of coordinates
$$(\lambda u_{1} + \mu v_{1}, \lambda u_{2} + \mu v_{2}, \lambda u_{3} + \mu v_{3}).$$
If we choose a different basis $(e_{1}', e_{2}', e_{3}')$ and if the matrix $P$ expressing the vectors $(e_{1}', e_{2}', e_{3}')$ over the basis $(e_{1}, e_{2}, e_{3})$ is
$$P = \begin{pmatrix} a_{1} & b_{1} & c_{1} \\ a_{2} & b_{2} & c_{2} \\ a_{3} & b_{3} & c_{3} \end{pmatrix} ,$$
which means that the columns of $P$ are the coordinates of the $e_{j}'$ over the basis $(e_{1}, e_{2}, e_{3})$, since
$$u_{1}e_{1} + u_{2}e_{2} + u_{3}e_{3} = u_{1}'e_{1}' + u_{2}'e_{2}' + u_{3}'e_{3}'$$
and
$$v_{1}e_{1} + v_{2}e_{2} + v_{3}e_{3} = v_{1}'e_{1}' + v_{2}'e_{2}' + v_{3}'e_{3}',$$
it is easy to see that the coordinates $(u_{1}, u_{2}, u_{3})$ and $(v_{1}, v_{2}, v_{3})$ of $u$ and $v$ with respect to the basis $(e_{1}, e_{2}, e_{3})$ are given in terms of the coordinates $(u_{1}', u_{2}', u_{3}')$ and $(v_{1}', v_{2}', v_{3}')$ of $u$ and $v$ with respect to the basis $(e_{1}', e_{2}', e_{3}')$ by the matrix equations
$$\begin{pmatrix} u_{1} \\ u_{2} \\ u_{3} \end{pmatrix} = P \begin{pmatrix} u_{1}' \\ u_{2}' \\ u_{3}' \end{pmatrix} and \begin{pmatrix} v_{1} \\ v_{2} \\ v_{3} \end{pmatrix} = P \begin{pmatrix} v' \\ v^{1'} \\ v_{3}^{2'} \end{pmatrix} .$$
From the above, we get

<!-- PAGE 809 -->
$$\begin{pmatrix} u_{1}' \\ u_{2}' \\ u_{3}' \end{pmatrix} = P^{-1} \begin{pmatrix} u_{1} \\ u_{2} \\ u_{3} \end{pmatrix} and \begin{pmatrix} v' \\ v^{1'} \\ v_{3}^{2'} \end{pmatrix} = P^{-1} \begin{pmatrix} v_{1} \\ v_{2} \\ v_{3} \end{pmatrix} ,$$
and by linearity, the coordinates
$$(\lambda u_{1}' + \mu v_{1}', \lambda u_{2}' + \mu v_{2}', \lambda u_{3}' + \mu v_{3}')$$
of $\lambda u + \mu v$ with respect to the basis $(e_{1}', e_{2}', e_{3}')$ are given by
$$\begin{pmatrix} \lambda u_{1}'+ \mu v_{1}' \\ \lambda u_{2}'+ \mu v_{2}' \\ \lambda u_{3}'+ \mu v_{3}' \end{pmatrix} \begin{pmatrix} u_{1} \\ u_{2} \\ u_{3} \end{pmatrix} \begin{pmatrix} v_{1} \\ v_{2} \\ v_{3} \end{pmatrix} \begin{pmatrix} \lambda u_{1} + \mu v_{1} \\ \lambda u_{2} + \mu v_{2} \\ \lambda u_{3} + \mu v_{3} \end{pmatrix}$$
$$= \lambda P^{-1}+ \mu P^{-1}= P^{-1}.$$
Everything worked out because the change of basis does not involve a change of origin. On the other hand, if we consider the change of frame from the frame $(O, (e_{1}, e_{2}, e_{3}))$ to the frame
$$\longrightarrow$$
$(\Omega , (e_{1}, e_{2}, e_{3}))$, where $O\Omega = (\omega_{1} , \omega_{2} , \omega_{3}$ ), given two points a, $b$ of coordinates $(a_{1}, a_{2}, a_{3})$ and $(b_{1}, b_{2}, b_{3})$ with respect to the frame $(O, (e_{1}, e_{2}, e_{3}))$ and of coordinates $(a_{1}', a_{2}', a_{3}')$ and $(b_{1}', b_{2}', b_{3}')$ with respect to the frame $(\Omega , (e_{1}, e_{2}, e_{3}))$, since
$$(a_{1}', a_{2}', a_{3}') = (a_{1} -\omega_{1} , a_{2} -\omega_{2} , a_{3} -\omega_{3} )$$
and
$$(b_{1}', b_{2}', b_{3}') = (b_{1} -\omega_{1} , b_{2} -\omega_{2} , b_{3} -\omega_{3} ),$$
the coordinates of $\lambda a + \mu b$ with respect to the frame $(O, (e_{1}, e_{2}, e_{3}))$ are
$$(\lambda a_{1} + \mu b_{1}, \lambda a_{2} + \mu b_{2}, \lambda a_{3} + \mu b_{3}),$$
but the coordinates
$$(\lambda a_{1}' + \mu b_{1}', \lambda a_{2}' + \mu b_{2}', \lambda a_{3}' + \mu b_{3}')$$
of $\lambda a + \mu b$ with respect to the frame $(\Omega , (e_{1}, e_{2}, e_{3}))$ are
$$(\lambda a_{1} + \mu b_{1} -(\lambda  + \mu )\omega_{1} , \lambda a_{2} + \mu b_{2} -(\lambda  + \mu )\omega_{2} , \lambda a_{3} + \mu b_{3} -(\lambda  + \mu )\omega_{3} ),$$
which are different from
$$(\lambda a_{1} + \mu b_{1} -\omega_{1} , \lambda a_{2} + \mu b_{2} -\omega_{2} , \lambda a_{3} + \mu b_{3} -\omega_{3} ),$$
unless $\lambda  + \mu  = 1$. See Figure 24.3. Thus, we have discovered a major difference between vectors and points: The notion of linear combination of vectors is basis independent, but the notion of linear combination of points is frame dependent. In order to salvage the notion of linear combination of points, some restriction is needed: The scalar coefficients must add up to $1$.

<!-- PAGE 810 -->
$$e3$$
$$e2$$
$$e\overline{\Omega}\overline{= (3,4,5)}$$
$$1$$
$$a + b = (3,4,2) = (0, 0, -3)$$
$$e3$$
$$a = (1,1,1)$$
$$eb = (2,3,1)$$
$$1\overline{O}\overline{e}\overline{2}$$
$$e3$$
$$e2$$
$$e\overline{\Omega}\overline{= (3,4,5)}$$
$$1$$
$$e3$$
$$a = (-2,-3,-4)$$
$$b = (-1,-1,-4)$$
$$e1$$
$$\overline{O}\overline{e}\overline{2}$$
$$a + b = (-3, -4, -8) = (0, 0, -3)$$

![Figure 24.3](../../assets/ch24/fig_24_3.png)

**Figure 24.3:** The top figure shows the location of the “point” sum $a + b$ with respect to the frame $(O, (e_{1}, e_{2}, e_{3}))$, while the bottom figure shows the location of the “point” sum $a + b$ with respect to the frame $(\Omega , (e_{1}, e_{2}, e_{3}))$. A clean way to handle the problem of frame invariance and to deal with points in a more intrinsic manner is to make a clearer distinction between points and vectors. We duplicate $\mathbb{R}^{3}$ into two copies, the first copy corresponding to points, where we forget the vector space structure, and the second copy corresponding to free vectors, where the vector space structure
$$\mathbb{R}^{3}$$
is important. Furthermore, we make explicit the important fact that the vector space acts
$$\mathbb{R}^{3}$$
on the set of points : Given any point $a = (a_{1}, a_{2}, a_{3})$ and any vector $v = (v_{1}, v_{2}, v_{3})$, we obtain the point
$$a + v = (a_{1} + v_{1}, a_{2} + v_{2}, a_{3} + v_{3}),$$
which can be thought of as the result of translating a to $b$ using the vector $v$. We can imagine that $v$ is placed such that its origin coincides with a and that its tip coincides with $b$. This
$$\mathbb{R}^{3} \mathbb{R}^{3} \mathbb{R}^{3}$$
action $+: \times \to$ satisfies some crucial properties. For example,
$$a + 0=a,$$
$$(a + u) + v=a + (u + v),$$

<!-- PAGE 811 -->
$$\longrightarrow$$
and for any two points a, $b$, there is a unique free vector ab such that
$$\longrightarrow$$
$$b = a +ab.$$
It turns out that the above properties, although trivial in the case of $\mathbb{R}^{3}$, are all that is needed to define the abstract notion of affine space (or affine structure). The basic idea is
$$\longrightarrow$$
to consider two (distinct) sets $E$ and $E$ , where $E$ is a set of points (with no structure) and $\longrightarrow E$ is a vector space (of free vectors) acting on the set $E$.
$$Did you say “A fine space”?$$
$$\longrightarrow$$
Intuitively, we can think of the elements of $E$ as forces moving the points in $E$, considered
$$\longrightarrow$$
as physical particles. The effect of applying a force (free vector) $u \in E$ to a point $a \in E$ is
$$\longrightarrow$$
a translation. By this, we mean that for every force $u \in E$ , the action of the force $u$ is to “move” every point $a \in E$ to the point $a + u \in E$ obtained by the translation corresponding
$$\longrightarrow$$
to $u$ viewed as a vector. Since translations can be composed, it is natural that $E$ is a vector space. For simplicity, it is assumed that all vector spaces under consideration are defined over the field $\mathbb{R}$ of real numbers. Most of the definitions and results also hold for an arbitrary field $K$, although some care is needed when dealing with fields of characteristic different from zero. It is also assumed that all families $(\lambda_{i} )_{i\in I}$ of scalars have finite support. Recall that a family $(\lambda_{i} )_{i\in I}$ of scalars has finite support if $\lambda_{i}  = 0$ for all $i \in$ I $-J$, where $J$ is a finite subset of I. Obviously, finite families of scalars have finite support, and for simplicity, the reader may assume that all families of scalars are finite. The formal definition of an affine space is as follows.

> **Definition 24.1.** An affine space is either the degenerate space reduced to the empty set,
$$\longrightarrow  \longrightarrow$$
or a triple $E, E , +$ consisting of a nonempty set $E$ (of points), a vector space $E$ (of trans-
$$\times  \longrightarrow$$
lations, or free vectors), and an action $+: E E \to E$, satisfying the following conditions.
(A1) $a + 0 = a$, for every $a \in E$.
$$\longrightarrow$$
(A2) $(a + u) + v = a + (u + v)$, for every $a \in E$, and every $u, v \in E$ .
$$\longrightarrow$$
(A3) For any two points a, $b \in E$, there is a unique $u \in E$ such that $a + u = b$.
$$\longrightarrow  \longrightarrow$$
The unique vector $u \in E$ such that $a + u = b$ is denoted by ab, or sometimes by ab, or even by $b$ - $a$. Thus, we also write
$$\longrightarrow$$
$$b = a +ab$$
(or $b = a +$ ab, or even $b = a + (b$ - $a))$.
$$\longrightarrow \longrightarrow$$
The dimension of the affine space $E, E , +$ is the dimension dim(E ) of the vector space $\longrightarrow E$ . For simplicity, it is denoted by dim(E).

<!-- PAGE 812 -->
$$\longrightarrow$$
$$EE$$
$$b = a + u$$
$$u$$
$$ac = a + ww$$
$$v$$
$$Figure 24.4: Intuitive picture of an affine space.$$
$$\longrightarrow$$
Conditions (A1) and (A2) say that the (abelian) group $E$ acts on $E$, and Condition (A3)
$$\longrightarrow$$
says that $E$ acts transitively and faithfully on $E$. Note that
$$----\longrightarrow$$
$$a(a + v) = v$$
$$\longrightarrow  ----\longrightarrow ----\longrightarrow$$
for all $a \in E$ and all $v \in E$ , since a(a $+ v)$ is the unique vector such that $a+v = a+a(a + v)$.
$$\longrightarrow$$
Thus, $b = a + v$ is equivalent to ab $= v$. Figure 24.4 gives an intuitive picture of an affine space. It is natural to think of all vectors as having the same origin, the null vector.
$$\longrightarrow$$
The axioms defining an affine space $E, E , +$ can be interpreted intuitively as saying
$$\longrightarrow$$
that $E$ and $E$ are two different ways of looking at the same object, but wearing different sets of glasses, the second set of glasses depending on the choice of an “origin” in $E$. Indeed, we can choose to look at the points in $E$, forgetting that every pair (a, $b)$ of points defines a
$$\longrightarrow  \longrightarrow  \longrightarrow$$
unique vector ab in $E$ , or we can choose to look at the vectors $u$ in $E$ , forgetting the points in $E$. Furthermore, if we also pick any point a in $E$, a point that can be viewed as an origin
$$\longrightarrow$$
in $E$, then we can recover all the points in $E$ as the translated points $a + u$ for all $u \in E$ .
$$\longrightarrow$$
This can be formalized by defining two maps between $E$ and $E$ .
$$\longrightarrow$$
For every $a \in E$, consider the mapping from $E$ to $E$ given by
$$u \mapsto a + u,$$
$$\longrightarrow  \longrightarrow$$
where $u \in E$ , and consider the mapping from $E$ to $E$ given by
$$\longrightarrow$$
$$b \mapsto ab,$$
where $b \in E$. The composition of the first mapping with the second is
$$----\longrightarrow$$
$$u \mapsto a + u \mapsto a(a + u),$$

<!-- PAGE 813 -->
which, in view of (A3), yields $u$. The composition of the second with the first mapping is
$$\longrightarrow  \longrightarrow$$
$$b \mapsto ab \mapsto a +ab,$$
$$\longrightarrow  \longrightarrow$$
which, in view of (A3), yields $b$. Thus, these compositions are the identity from $E$ to $E$ and the identity from $E$ to $E$, and the mappings are both bijections.
$$\longrightarrow \longrightarrow$$
When we identify $E$ with $E$ via the mapping $b \mapsto$ ab, we say that we consider $E$ as the vector space obtained by taking a as the origin in $E$, and we denote it by $E_{a}$. Because $E_{a}$ is a vector space, to be consistent with our notational conventions we should use the notation $\longrightarrow E_{a}$ (using an arrow), instead of $E_{a}$. However, for simplicity, we stick to the notation $E_{a}$.
$$\longrightarrow$$
Thus, an affine space $E, E , +$ is a way of defining a vector space structure on a set of points $E$, without making a commitment to a fixed origin in $E$. Nevertheless, as soon as we commit to an origin a in $E$, we can view $E$ as the vector space $E_{a}$. However, we urge
$$\longrightarrow$$
the reader to think of $E$ as a physical set of points and of $E$ as a set of forces acting on $E$, rather than reducing $E$ to some isomorphic copy of $\mathbb{R}^{n}$. After all, points are points, and not
$$\longrightarrow  \longrightarrow$$
vectors! For notational simplicity, we will often denote an affine space $E, E , +$ by $(E, E$ ),
$$\longrightarrow$$
or even by $E$. The vector space $E$ is called the vector space associated with $E$.  One should be careful about the overloading of the addition symbol $+$. Addition
$$is well-defined on vectors, as in u + v; the translate a + u of a point a \in E by a$$
$$\longrightarrow$$
vector $u \in E$ is also well-defined, but addition of points $a + b$ does not make sense. In this respect, the notation $b$ - $a$ for the unique vector $u$ such that $b = a + u$ is somewhat confusing, since it suggests that points can be subtracted (but not added!).
$$\longrightarrow  \longrightarrow$$
Any vector space $E$ has an affine space structure specified by choosing $E = E$ , and
$$\longrightarrow \longrightarrow  \longrightarrow$$
letting $+$ be addition in the vector space $E$ . We will refer to the affine structure $E , E , +$
$$\longrightarrow  \longrightarrow$$
on a vector space $E$ as the canonical (or natural) affine structure on $E$ . In particular, the
$$\mathbb{R}^{n} \mathbb{R}^{n}\mathbb{R}^{n} \mathbb{A}^{n}$$
vector space can be viewed as the affine space , , $+$ , denoted by . In general, if $K$ is any field, the affine space $K^{n}, K^{n}, +$ is denoted by $\mathbb{A}_{K}^{n}$. In order to distinguish between the double role played by members of $\mathbb{R}^{n}$, points and vectors, we will denote points
$$\mathbb{R}^{n}$$
by row vectors, and vectors by column vectors. Thus, the action of the vector space over
$$\mathbb{R}^{n}$$
the set simply viewed as a set of points is given by
$$(a_{1}, \dots  , a_{n}) + \begin{pmatrix} u_{1} \\ \vdots \\ u_{n} \end{pmatrix} = (a_{1} + u_{1}, \dots  , a_{n} + u_{n}).$$
We will also use the convention that if $x = (x_{1}, \dots  , x_{n}) \in \mathbb{R}^{n}$, then the column vector associated with $x$ is denoted by $x$ (in boldface notation). Abusing the notation slightly, if $\mathbb{R}^{n} \mathbb{A}^{n}  \mathbb{A}^{n} a \in$ is a point, we also write $a \in$ . The affine space is called the real affine space of dimension $n$. In most cases, we will consider $n = 1, 2, 3$.
