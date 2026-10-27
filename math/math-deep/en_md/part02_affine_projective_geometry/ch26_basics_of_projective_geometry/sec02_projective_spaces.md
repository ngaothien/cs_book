# Projective Spaces


<!-- PAGE 876 -->
What we just sketched is a general method to deal with rational curves. We can use our “hat construction” to embed an affine $space\mathcal{E}$ into a vector space $\mathcal{E}$ having one more dimen-
$$b$$
$$sion, then construct the projective space P \begin{pmatrix} \mathcal{E} b \end{pmatrix} . This turns out to be the “projective com-$$
$$pletion” of the affine space \mathcal{E}. Then we can define a rational curve in P \begin{pmatrix} \mathcal{E} b \end{pmatrix} , basically as the$$
central projection of a polynomial curve in $\mathcal{E}$ back onto $P$ . The same approach can be used
$$to deal with rational surfaces.  b \begin{pmatrix} \mathcal{E} b \\ Due to the lack of space, such a presentation is omitted. \end{pmatrix} How-$$
ever, it can be found on the web; see $http://www.cis.upenn.edu/ jean/gbooks/geom2.html$.
$$e$$
More generally, the projective completion of an affine space is a very convenient tool to handle “points at infinity” in a clean fashion. This chapter contains a brief presentation of concepts of projective geometry. The following concepts are presented: projective spaces, projective frames, homogeneous coordinates, projective maps, projective hyperplanes, multiprojective maps, affine patches. The projective completion of an affine space is presented using the “hat construction.” The theorems of Pappus and Desargues are proved, using the method in which points are “sent to infinity.” We also discuss the cross-ratio and duality. The chapter ends with a very brief explanation of the use of the complexification of a projective space in order to define the notion of angle and orthogonality in a projective setting. We also include a short section on applications of projective geometry, notably to computer vision (camera calibration), efficient communication, and error-correcting codes.

## 26.2 Projective Spaces

As in the case of affine geometry, our presentation of projective geometry is rather sketchy. For a systematic treatment of projective geometry, we recommend Berger $[11, 12]$, Samuel $[148]$, Pedoe $[141]$, Coxeter $[45, 46, 43, 44]$, Beutelspacher and Rosenbaum $[22]$, Fresnel $[66]$, Sidler $[167]$, Tisseron $[181]$, Lehmann and Bkouche $[119]$, Vienne $[191]$, and the classical treatise by Veblen and Young $[189, 190]$, which, although slightly old-fashioned, is definitely worth reading. Emil Artin’s famous book $[6]$ contains, among other things, an axiomatic presentation of projective geometry, and a wealth of geometric material presented from an algebraic point of view. Other “oldies but goodies” include the beautiful books by Darboux $[47]$ and Klein $[106]$. For a development of projective geometry addressing the delicate problem of orientation, see Stolfi[173], and for an approach geared towards computer graphics, see Penna and Patterson $[142]$. First, we define projective spaces, allowing the field $K$ to be arbitrary (which does no harm, and is needed to allow finite and complex projective spaces). Roughly speaking, every projective concept is a linear–algebraic concept “up to a scalar.” For spaces, this is made precise as follows.

> **Definition 26.1.** Given a vector space $E$ over a field $K$, the projective space P(E) induced by $E$ is the set $(E -{0})/ \sim$ of equivalence classes of nonzero vectors in $E$ under the

<!-- PAGE 877 -->
equivalence relation $\sim$ defined such that for all $u, v \in E -{0}$,
$$u \sim viffv = \lambda u, for some \lambda  \in K -{0}.$$
The canonical projection $p: (E -{0}) \to$ P(E) is the function associating the equivalence class $[u]_{\sim}$ modulo $\sim$ to u̸ $= 0$. The dimension dim(P(E)) of P(E) is defined as follows: If $E$ is of infinite dimension, then dim(P(E)) $=$ dim(E), and if $E$ has finite dimension, dim(E) $= n \ge 1$ then dim(P(E)) $= n$ - $1$. Mathematically, a projective space P(E) is a set of equivalence classes of vectors in $E$. The spirit of projective geometry is to view an equivalence class p(u) $= [u]_{\sim}$ as an “atomic” object, forgetting the internal structure of the equivalence class. For this reason, it is customary to call an equivalence class $a = [u]_{\sim}$ a point (the entire equivalence class $[u]_{\sim}$ is collapsed into a single object viewed as a point).
Remarks:
$(1)$ If we view $E$ as an affine space, then for any nonnull vector $u \in E$, since
$$[u]_{\sim}= {\lambda u | \lambda  \in K, \lambda  \neq  0},$$
letting
$$Ku = {\lambda u | \lambda  \in K}$$
denote the subspace of dimension $1$ spanned by $u$, the map
$$[u]_{\sim}\mapsto Ku$$
from P(E) to the set of one-dimensional subspaces of $E$ is clearly a bijection, and since subspaces of dimension $1$ correspond to lines through the origin in $E$, we can view P(E) as the set of lines in $E$ passing through the origin. So, the projective space P(E) can be viewed as the set obtained from $E$ when lines through the origin are treated as points. However, this is a somewhat deceptive view. Indeed, depending on the structure of the vector space $E$, a line (through the origin) in $E$ may be a fairly complex object, and treating a line just as a point is really a mental game. For example, $E$ may be the vector space of real homogeneous polynomials P(x, $y, z)$ of degree $2$ in three variables $x, y, z$ (plus the null polynomial), and a “line” (through the origin) in $E$ corresponds to an algebraic curve of degree $2$. Lots of details need to be filled in, but roughly speaking, the curve defined by $P$ is the “zero locus of P,” i.e., the set of points $(x, y, z) \in P(\mathbb{R}^{3})$ (or perhaps in $P(\mathbb{C}^{3}))$ for which P(x, $y, z) = 0$. We will come back to this point in Section 26.4 after having introduced homogeneous coordinates. More generally, $E$ may be a vector space of homogeneous polynomials of degree $m$ in $3$ or more variables (plus the null polynomial), and the lines in $E$ correspond to

<!-- PAGE 878 -->
such objects as algebraic curves, algebraic surfaces, and algebraic varieties. The point of view where a complex object such as a curve or a surface is treated as a point in a (projective) space is actually very fruitful and is one of the themes of algebraic geometry (see Fulton $[67]$ or Harris $[90])$.
$(2)$ When dim(E) $= 1$, we have dim(P(E)) $= 0$. When $E = {0}$, we have P(E) $= \emptyset$ . By convention, we give it the dimension $-1$. We denote the projective space $P(K^{n+1})$ by $\mathbb{P}_{K}^{n}$. When $K = \mathbb{R}$, we also denote $\mathbb{P}_{R}^{n}$ by $\mathbb{RP}^{n}$, and when $K = \mathbb{C}$, we denote $\mathbb{P}_{C}^{n}$ by $\mathbb{CP}^{n}$. The projective space $\mathbb{P}_{K}^{0}$ is a (projective) point. The projective space $\mathbb{P}_{K}^{1}$ is called a projective line. The projective space $\mathbb{P}_{K}^{2}$ is called a projective plane. The projective space P(E) can be visualized in the following way. For simplicity, assume
$$\mathbb{R}^{n+1} \mathbb{RP}^{n}$$
that $E =$ , and thus P(E) $=$ (the same reasoning applies to $E = K^{n+1}$, where $K$ is any field). Let $H$ be the affine hyperplane consisting of all points $(x_{1}, \dots  , x_{n+1})$ such that $x_{n+1} = 1$. Every nonzero vector $u$ in $E$ determines a line $D$ passing through the origin, and this line intersects the hyperplane $H$ in a unique point a, unless $D$ is parallel to $H$. When $D$ is parallel to $H$, the line corresponding to the equivalence class of $u$ can be thought of as a point at infinity, often denoted by $u_{\infty}$. Thus, the projective space P(E) can be viewed as the set of points in the hyperplane $H$, together with points at infinity associated with lines in the hyperplane $H_{\infty}$ of equation $x_{n+1} = 0$. We will come back to this point of view when we consider the projective completion of an affine space. Figure 26.3 illustrates the above
$$\mathbb{R}^{2} \mathbb{R}^{3}$$
representation of the projective space for $E =$ and $E =$ .
$$[v]~[u]~[v]~[u]~$$
$$y = 1$$
$$z = 1$$
$$vu$$
$$u\infty$$
$$u\infty$$
$$(i.)$$
$$(ii.)$$
$$\mathbb{RP}^{1}  \mathbb{RP}^{2}$$
$$Figure 26.3: The hyperplane model representations ofand.$$
We refer to the above model of P(E) as the hyperplane model. In this model some

<!-- PAGE 879 -->
$$\mathbb{R}^{n+1}$$
hyperplane $H_{\infty}$ (through the origin) in is singled out, and the points of P(E) arising from the hyperplane $H_{\infty}$ are declared to be “points at infinity.” The purpose of the affine hyperplane $H$ parallel to $H_{\infty}$ and distinct from $H_{\infty}$ is to get images for the other points in P(E) (i.e., those that arise from lines not contained in $H_{\infty})$. It should be noted that the choice of which points should be considered as infinite is relative to the choice of $H_{\infty}$. Viewing certain points of P(E) as points at infinity is convenient for getting a mental picture of P(E), but there is nothing intrinsic about that. Points of P(E) are all equal, and unless some additional structure in introduced in P(E) (such as a hyperplane), a point in P(E) doesn’t know whether it is infinite! The notion of point at infinity is really an affine notion. This point will be made precise in Section 26.8.
$$\mathbb{RP}^{n} \mathbb{R}^{n+1}$$
Again, for $= P($ ), instead of considering the hyperplane $H$, we can consider the n-sphere $S^{n}$ of center $0$ and radius $1$, i.e., the set of points $(x_{1}, \dots  , x_{n+1})$ such that
$$x_{1}^{2} + \cdots  + x_{n}^{2} + x_{n+1}^{2} = 1.$$
In this case, every line $D$ through the center of the sphere intersects the sphere $S^{n}$ in two
$$\mathbb{RP}^{n}$$
antipodal points $a_{+}$ and $a_{-}$. The projective space is the quotient space obtained from the sphere $S^{n}$ by identifying antipodal points $a_{+}$ and $a_{-}$. It is hard to visualize such an object! We call this model of P(E) the spherical model. See Figure 26.4.
$$y$$
$$x$$
$$x$$
$$xy$$
$$x$$
$$(i.)$$
$$(ii.)$$
$$\mathbb{RP}^{1}  \mathbb{RP}^{2}$$
$$Figure 26.4: The spherical model representations ofand.$$
A more subtle construction consists in considering the (upper) half-sphere instead of the sphere, where the upper half-sphere $S_{+}^{n}$ is set of points on the sphere $S^{n}$ such that $x_{n+1} \ge 0$. This time, every line through the center intersects the (upper) half-sphere in a single point, except on the boundary of the half-sphere, where it intersects in two antipodal points $a_{+}$
$$\mathbb{RP}^{n}$$
and $a_{-}$. Thus, the projective space is the quotient space obtained from the (upper)

<!-- PAGE 880 -->
$$x$$
$$xx$$
$$(i.)$$
$$x$$
$$x$$
$$(ii.)$$
$$\mathbb{RP}^{1}  \mathbb{RP}^{2}$$
$$Figure 26.5: The half-spherical model representations ofand.$$
half-sphere $S_{+}^{n}$ by identifying antipodal points $a_{+}$ and $a_{-}$ on the boundary of the half-sphere. We call this model of P(E) the half-spherical model; see Figure 26.5. When $n = 2$, we get a circle. When $n = 3$, the upper half-sphere is homeomorphic
$$\mathbb{RP}^{2}$$
to a closed disk (say, by orthogonal projection onto the xy-plane), and is in bijection with a closed disk in which antipodal points on its boundary (a unit circle) have been identified. This is hard to visualize! In this model of the real projective space, projective lines are great semicircles on the upper half-sphere, with antipodal points on the boundary identified. Boundary points correspond to points at infinity. By orthogonal projection, these great semicircles correspond to semiellipses, with antipodal points on the boundary identified. Traveling along such a projective “line,” when we reach a boundary point, we “wrap around”! In general, the upper half-sphere $S_{+}^{n}$ is homeomorphic to the closed unit ball in $\mathbb{R}^{n}$, whose boundary is the $(n$ - 1)-sphere $S^{n-1}$. For example, the projective space $\mathbb{RP}^{3}  \mathbb{R}^{3}$ is in bijection with the closed unit ball in , with antipodal points on its boundary (the sphere $S^{2})$ identified!
Remarks:
$(1) A$ projective space P(E) has been defined as a set without any topological structure. When the field $K$ is either the field $\mathbb{R}$ of reals or the field $\mathbb{C}$ of complex numbers, the vector space $E$ is a topological space. Thus, the projection map $p: (E -{0}) \to$ P(E) induces a topology on the projective space P(E), namely the quotient topology. This means that a subset $V$ of P(E) is open iff $p^{-1}(V$ ) is an open set in $E$. Then, for
$$\mathbb{RP}^{n}$$
example, it turns out that the real projective space is homeomorphic to the space
