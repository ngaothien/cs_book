# Similarity Structures on a Projective Space


<!-- PAGE 954 -->
 Note that a real hypersurface may have points other than real points, or no real
$$points at all. For example,$$
$$x^{2}+ y^{2}-z^{2}= 0$$
contains real and complex points such as $(1, i, 0)$ and $(1, -i, 0)$, and
$$x^{2}+ y^{2}+ z^{2}= 0$$
contains only complex points. When $m = 2$ (where $m$ is the total degree of $P)$, a hypersurface is called a quadric, and when $m = 2$ and $n = 2$, a conic. When $m = 1$, a hypersurface is just a hyperplane. Given any homogeneous polynomial $P(x_{1}, \dots  , x_{n+1})$ over $\mathbb{R}$ of total degree $m$, since $\mathbb{R} \subseteq \mathbb{C}, P$ viewed as a homogeneous polynomial over $\mathbb{C}$ defines a hypersurface $V (P)_{C}$ in $E_{C}$, and also a hypersurface $V (P)$ in P(E). It is clear that $V (P)$ is naturally embedded in $e V (P)_{C}$, and $V (P)_{C}$ is called the complexification of $V (P)$. We now show how certain real quadrics without real points can be used to define orthogonality and angles.

## 26.15 Similarity Structures on a Projective Space

$$We begin with a real Euclidean plane \begin{pmatrix} \longrightarrow \\ E,E \\ cross-ratio \end{pmatrix} . We will show that the angle of two lines D_{1}$$
and $D_{2}$ can be expressed as a certain  involving the lines $D_{1}, D_{2}$ and also two lines $D_{I}$ and $D_{J}$ joining the intersection point $D_{1} \cap D_{2}$ of $D_{1}$ and $D_{2}$ to two complex points at infinity I and $J$ called the circular points. However, there is a slight problem, which is that we haven’t yet defined the angle of two lines! Recall that we define the (oriented) angle $u_{1}u_{2}$ of two unit vectors $u_{1}, u_{2}$ as the equivalence class of pairs of unit vectors under the $d$ equivalence relation defined such that
$$\langle u_{1}, u_{2}\rangle \equiv \langle u_{3}, u_{4}\rangle$$
iff there is some rotation $r$ such that $r(u_{1}) = u_{3}$ and $r(u_{2}) = u_{4}$. The set of (oriented) angles of vectors is a group isomorphic to the group SO(2) of plane rotations. If the Euclidean plane is oriented, the measure of the angle of two vectors is defined up to $2k\pi  (k \in \mathbb{Z})$. The angle of two vectors has a measure that is either $\theta$  or $2\pi$  - $\theta$ , where $\theta  \in [0, 2\pi$ [ , depending on the orientation of the plane. The problem with lines is that they are not oriented: $A$ line is defined by a point a and a vector $u$, but also by a and $-u$. Given any two lines $D_{1}$ and $D_{2}$, if $r$ is a rotation of angle $\theta$  such that $r(D_{1}) = D_{2}$, note that the rotation $-r$ of angle
$$\$$
$\theta  + \pi$  also maps $D_{1}$ onto $D_{2}$. Thus, in order to define the (oriented) angle $D_{1}D_{2}$ of two lines $D_{1}, D_{2}$, we define an equivalence relation on pairs of lines as follows:
$$\langle D_{1}, D_{2}\rangle \equiv \langle D_{3}, D_{4}\rangle$$

<!-- PAGE 955 -->
if there is some rotation $r$ such that $r(D_{1}) = D_{2}$ and $r(D_{3}) = D_{4}$. It can be verified that the set of (oriented) angles of lines is a group isomorphic to the quotient group $SO(2)/{id, -id}$, also denoted by PSO(2). In order to define the measure of the angle of two lines, the Euclidean plane $E$ must be oriented. The measure of the angle $\ \mathbb{Z} D_{1}D_{2}$ of two lines is defined up to $k\pi  (k \in$ ). The angle of two lines has a measure that is either $\theta$  or $\pi$  - $\theta$ , where $\theta  \in [0, \pi$ [ , depending on the orientation of the plane. We now go back to the circular points. Let $(a_{0}, a_{1}, a_{2}, a_{3})$ be any projective frame for $E_{C}$ such that $(a_{0}, a_{1})$ arises from an or-
$$\longrightarrow  e$$
thonormal basis $(u_{1}, u_{2})$ of $E$ and the line at infinity $H$ corresponds to $z = 0$ (where $(x, y, z)$ are the homogeneous coordinates of a point w.r.t. $(a_{0}, a_{1}, a_{2}, a_{3}))$. Consider the points belonging to the intersection of the real conic $\Sigma$  of equation
$$x^{2}+ y^{2}-z^{2}= 0$$
with the line at infinity $z = 0$. For such points, $x^{2} + y^{2} = 0$ and $z = 0$, and since
$$x^{2}+ y^{2}= (y -ix)(y + ix),$$
we get exactly two points I and $J$ of homogeneous coordinates $(1, -i, 0)$ and $(1, i, 0)$. The points I and $J$ are called the circular points, or the absolute points, of $E_{C}$. They are complex
$$e$$
points at infinity. Any line containing either I or $J$ is called an isotropic line. What is remarkable about I and $J$ is that they allow the definition of the angle of two lines in terms of a certain cross-ratio. Indeed, consider two distinct real lines $D_{1}$ and $D_{2}$ in $E$, and let $D_{I}$ and $D_{J}$ be the isotropic lines joining $D_{1} \cap D_{2}$ to I and $J$. We will compute the cross-ratio $[D_{1}, D_{2}, D_{I}, D_{J}]$. For this, we simply have to compute the cross-ratio of the four points obtained by intersecting $D_{1}, D_{2}, D_{I}, D_{J}$ with any line not passing through $D_{1} \cap D_{2}$. By changing frame if necessary, so that $D_{1} \cap D_{2} = a_{0}$, we can assume that the equations of the lines $D_{1}, D_{2}, D_{I}, D_{J}$ are of the form
$$y=m_{1}x,$$
$$y=m_{2}x,$$
$$y=-ix,$$
$$y=ix,$$
leaving the cases $m_{1} = \infty$ and $m_{2} = \infty$ as a simple exercise. If we choose $z = 0$ as the intersecting line, we need to compute the cross-ratio of the points $(D_{1})_{\infty} = (1, m_{1}, 0), (D_{2})_{\infty} = (1, m_{2}, 0), I = (1, -i, 0)$, and $J = (1, i, 0)$, and we get
$$- - -$$
$$[D_{1}, D_{2}, D_{I}, D_{J}] = [(D_{1})_{\infty}, (D_{2})_{\infty}, I, J] = \frac{(im_{1})}{(i -m_{1})} \frac{(im_{2})}{(-i -m_{2})} ,$$
that is,
$$-$$
$$[D_{1}, D_{2}, D_{I}, D_{J}] = \frac{m_{1}m_{2} + 1 + i(m_{2}m_{1})}{m_{1}m_{2} + 1 -i(m_{2} -m_{1})} .$$

<!-- PAGE 956 -->
However, since $m_{1}$ and $m_{2}$ are the slopes of the lines $D_{1}$ and $D_{2}$, it is well known that if $\theta$ is the (oriented) angle between $D_{1}$ and $D_{2}$, then
$$-$$
$$\tan \theta  = \frac{m_{2}m_{1}}{m_{1}m_{2} + 1} .$$
Thus, we have
$$[D_{1}, D_{2}, D_{I}, D_{J}] = \frac{m_{1}m_{2} + 1 + i(m_{2}m_{1})}{m_{1}m_{2} + 1 -i(m_{2} -m_{1})} - = \frac{1 + i \tan \theta}{1 -i \tan \theta} ,$$
that is,
$$[D_{1}, D_{2}, D_{I}, D_{J}] = \cos 2\theta  + i \sin 2\theta  = e^{i2\theta}.$$
One can check that the formula still holds when $m_{1} = \infty$ or $m_{2} = \infty$ , and also when $D_{1} = D_{2}$. The formula
$$[D_{1}, D_{2}, D_{I}, D_{J}] = e^{i2\theta}$$
is known as Laguerre’s formula. If $U$ denotes the group ${e^{i\theta}$ | $-\pi  \le \theta  \le \pi$ } of complex numbers of modulus $1$, recall that the map $\Lambda$ : $\mathbb{R} \to U$ defined such that
$$\Lambda (t) = e^{it}$$
is a group homomorphism such that $\Lambda^{-1} (1) = 2k\pi$ , where $k \in \mathbb{Z}$. The restriction
$$\Lambda : ] -\pi , \pi [ \to (U -{-1})$$
of $\Lambda$  to ] - $\pi , \pi$ [ is a bijection, and its inverse will be denoted by
$$log_{U} : (U -{-1}) \to ] -\pi , \pi [ .$$
For stating Proposition 26.28 more conveniently, we extend $log_{U}$ to $U$ by letting $log_{U}(-1) = \pi$ , even though the resulting function is not continuous at $-1$!. Then we can write
$$1$$
$$\theta  =2 log_{U}([D_{1}, D_{2}, D_{I}, D_{J}]).$$
If the orientation of the plane $E$ is reversed, $\theta$  becomes $\pi$  - $\theta$ , and since
$$e^{i2(\pi-\theta)}= e^{2i\pi-i2\theta}= e^{-i2\theta},$$
$log_{U}(e^{i2(\pi-\theta)}) = -log_{U}(e^{i2\theta})$, and
$$1$$
$$\theta  = -2 log_{U}([D_{1}, D_{2}, D_{I}, D_{J}]).$$
In all cases, we have
$$\theta  = \frac{1}{2} | log_{U}([D_{1}, D_{2}, D_{I}, D_{J}])|,$$
a formula due to Cayley. We summarize the above in the following proposition.

<!-- PAGE 957 -->
$$Proposition 26.28. Given any two lines D_{1}, D_{2} in a real Euclidean plane \begin{pmatrix} \longrightarrow \\ E,E \\ ofD_{1} \end{pmatrix} , letting$$
$D_{I}$ and $D_{J}$ be the isotropic lines in $E_{C}$ joining the intersection point $D_{1} \cap D_{2}$   and $D_{2}$
$$e$$
to the circular points I and $J$, if $\theta$  is the angle of the two lines $D_{1}, D_{2}$, we have
$$[D_{1}, D_{2}, D_{I}, D_{J}] = e^{i2\theta},$$
known as Laguerre’s formula, and independently of the orientation of the plane, we have
$$\theta  = \frac{1}{2} | log_{U}([D_{1}, D_{2}, D_{I}, D_{J}])|,$$
known as Cayley’s formula. In particular, note that $\theta  = \pi /2 iff[D_{1}, D_{2}, D_{I}, D_{J}] = -1$, that is, if $(D_{1}, D_{2}, D_{I}, D_{J})$ forms a harmonic division. Thus, two lines $D_{1}$ and $D_{2}$ are orthogonal iff they form a harmonic division with $D_{I}$ and $D_{J}$.
$$The above considerations show that it is not necessary to assume that \begin{pmatrix} \longrightarrow \\ E,E \\ itis \end{pmatrix} is a real$$
Euclidean plane to define the angle of two lines and orthogonality. Instead,   enough to assume that two complex conjugate points I, $J$ on the line $H$ at infinity are given. We say that $\langle$ I, $J\rangle$ provides a similarity structure on $E_{C}$. Note in passing that a circle can be defined
$$e$$
as a conic in $E_{C}$ that contains the circular points I, $J$. Indeed, the equation of a conic is of
$$e$$
the form
$$ax^{2}+ by^{2}+ cxy + dxz + eyz + fz^{2}= 0.$$
If this conic contains the circular points $I = (1, -i, 0)$ and $J = (1, i, 0)$, we get the two equations
$$a -b -ic=0,$$
$$a -b + ic=0,$$
from which we get 2ic $= 0$ and $a = b$, that is, $c = 0$ and $a = b$. The resulting equation
$$ax^{2}+ ay^{2}+ dxz + eyz + fz^{2}= 0$$
is indeed that of a circle. Instead of using the function $log_{U}$ : $(U -{-1}) \to$ ] - $\pi , \pi$ [ as logarithm, one may use the complex logarithm function log: $\mathbb{C}^{*} \to B$, where $\mathbb{C}^{*} =\mathbb{C} -{0}$ and
$$B = {x + iy | x, y \in \mathbb{R}, -\pi  < y \le \pi }.$$
Indeed, the restriction of the complex exponential function $z \mapsto e^{z}$ to $B$ is bijective, and thus, log is well-defined on $C^{*}$ (note that log is a homeomorphism from $\mathbb{C} -{x$ | $x \in \mathbb{R}, x \le 0}$ onto ${x +$ iy | $x, y \in \mathbb{R}, -\pi  < y < \pi$ }, the interior of $B)$. Then Cayley’s formula reads as
$$\theta  = \frac{1}{2i} \log([D_{1}, D_{2}, D_{I}, D_{J}]),$$

<!-- PAGE 958 -->
with $a \pm$  in front when the plane is nonoriented. Observe that this formula allows the definition of the angle of two complex lines (possibly a complex number) and the notion of orthogonality of complex lines. In this case, note that the isotropic lines are orthogonal to themselves! The definition of orthogonality of two lines $D_{1}, D_{2}$ in terms of $(D_{1}, D_{2}, D_{I}, D_{J})$ forming a harmonic division can be used to give elegant proofs of various results. Cayley’s formula can even be used in computer vision to explain modeling and calibrating cameras! (see Faugeras $[60])$. As an illustration, consider a triangle (a, $b, c)$, and recall that the line a' passing through a and orthogonal to $(b, c)$ is called the altitude of a, and similarly for $b$ and $c$. It is well known that the altitudes a', b', c' intersect in a common point called the orthocenter of the triangle (a, $b, c)$. This can be shown in a number of ways using the circular points. Indeed, letting $bc_{\infty}, ab_{\infty}, ac_{\infty}, a_{\infty}', b_{\infty}'$, and $c_{\infty}'$ denote the points at infinity of the lines $\langle b, c\rangle , \langle$ a, $b\rangle , \langle$ a, $c\rangle$ , a', b', and c', we have
$$[bc_{\infty}, a_{\infty}', I, J] = -1,[ab_{\infty}, c_{\infty}', I, J] = -1,[ac_{\infty}, b_{\infty}', I, J] = -1,$$
and it is easy to show that there is an involution $\sigma$  of the line at infinity such that
$$\sigma (I)=J,$$
$$\sigma (J)=I,$$
$$\sigma (bc_{\infty})=a_{\infty}',$$
$$\sigma (ab_{\infty})=c_{\infty}',$$
$$\sigma (ac_{\infty})=b_{\infty}'.$$
Then, it can be shown that the lines a', b', c' are concurrent. For more details and other results, notably on the conics, see Sidler $[167]$, Berger $[12]$, and Samuel $[148]$.
$$The generalization of what we just did to real Euclidean spaces \begin{pmatrix} \longrightarrow \\ E,E \\ (a_{0} \end{pmatrix} of dimension n$$
is simple. Let $(a_{0}, \dots  , a_{n+1})$ be any projective frame for $E_{C}$ such that , $\dots  , a_{n-1})$ arises
$$\longrightarrow  e$$
from an orthonormal basis $(u_{1}, \dots  , u_{n})$ of $E$ and the hyperplane at infinity $H$ corresponds to $x_{n+1} = 0$ (where $(x_{1}, \dots  , x_{n+1})$ are the homogeneous coordinates of a point with respect to $(a_{0}, \dots  , a_{n+1}))$. Consider the points belonging to the intersection of the real quadric $\Sigma$  of equation
$$x_{1}^{2} + \cdots  + x_{n}^{2} -x_{n+1}^{2} = 0$$
with the hyperplane at infinity $x_{n+1} = 0$. For such points,
$$x_{1}^{2} + \cdots  + x_{n}^{2} = 0andx_{n+1} = 0.$$
Such points belong to a quadric called the absolute quadric of $E_{C}$, and denoted by $\Omega$ . Any
$$e$$
line containing any point on the absolute quadric is called an isotropic line. Then, given any two coplanar lines $D_{1}$ and $D_{2}$ in $E$, these lines intersect the hyperplane at infinity $H$ in two points $(D_{1})_{\infty}$ and $(D_{2})_{\infty}$, and the line $\Delta$ joining $(D_{1})_{\infty}$ and $(D_{2})_{\infty}$ intersects the absolute

<!-- PAGE 959 -->
quadric $\Omega$ in two conjugate points $I_{\Delta}$ and $J_{\Delta}$ (also called circular points). It can be shown that the angle $\theta$  between $D_{1}$ and $D_{2}$ is defined by Laguerre’s formula:
$$[(D_{1})_{\infty}, (D_{2})_{\infty}, I_{\Delta}, J_{\Delta}] = [D_{1}, D_{2}, D_{I\Delta}, D_{J\Delta}] = e^{i2\theta},$$
where $D_{I\Delta}$ and $D_{J\Delta}$ are the lines joining the intersection $D_{1}\cap D_{2}$ of $D_{1}$ and $D_{2}$ to the circular points $I_{\Delta}$ and $J_{\Delta}$. As in the case of a plane, the above considerations show that it is not necessary to assume
$$that \begin{pmatrix} \longrightarrow \\ E,E \\ it \end{pmatrix} is a real Euclidean space to define the angle of two lines and orthogonality.$$
Instead,  is enough to assume that a nondegenerate real quadric $\Omega$ in the hyperplane at infinity $H$ and without real points is given. In particular, when $n = 3$, the absolute quadric $\Omega$ is a nondegenerate real conic consisting of complex points at infinity. We say that $\Omega$ provides a similarity structure on $E_{C}$.
$$e$$
It is also possible to show that the real projectivities of $E_{C}$ that leave both the hyperplane
$$e$$
$H$ at infinity and the absolute quadric $\Omega$ (globally) invariant form a group which is none other than the group of affine similarities; see Lehmann and Bkouche $[119]$ (Chapter $10$, page $321)$, and Berger $[11]$ (Chapter $8$, Proposition 8.8.6.4).
$$\longrightarrow$$

> **Definition 26.14.** Let $(E, E , \langle$ -, $-\rangle$ ) be a Euclidean affine space of finite dimension. An
$$\longrightarrow  \longrightarrow$$
affine similarity of $(E, E$ ) is an invertible affine map $f \in$ GA(E) such that if $f$ is the linear map associated with $f$, then there is some positive real $\rho  > 0$ satisfying the condition $\longrightarrow$


$\in \longrightarrow f (u)  = \rho  \|u\|$ for all $u E$ . The number $\rho$  is called the ratio of the affine similarity $f$.
$$\longrightarrow \longrightarrow$$
If $f \in$ GA(E) is an affine similarity of ratio $\rho$ , let $g = \rho^{-1} f$ . Since $\rho  > 0$, we have
$$\longrightarrow


$\longrightarrow$





$\longrightarrow$$$
$$\|g (u)\|=\rho^{-1} f (u) = \rho^{-1} f (u) = \rho^{-1} \rho  \|u\|= \|u\|$$
$$\longrightarrow  \longrightarrow \longrightarrow$$
for all $u \in E$ , and by Proposition 12.12, the map $g = \rho^{-1} f$ is an isometry; that is, $\longrightarrow g \in$ O(E). Consequently, every affine similarity $f$ of $E$ can be written as the composition of an isometry (a member of O(E)), a central dilatation, and a translation. For example, when $n = 2$, a similarity is a transformation of the form
$$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} a & -\epsilon b \\ b & \epsilon a \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} + \begin{pmatrix} c \\ c' \end{pmatrix} ,$$
$$\mathbb{R}$$
with $\epsilon  = \pm 1$ and a, $b, c$, c' $\in$ . We have the following result showing that the affine similarities of the plane can be viewed as special kinds of projectivities of $\mathbb{CP}^{2}$.
$$\mathbb{CP}^{2}$$

> **Proposition 26.29.** If a projectivity $h$ of leaves the set of circular points ${I, J}$ fixed
$$\mathbb{R}^{2}  \mathbb{R}^{2}$$
and maps the affine space into itself (where is viewed as the subspace of all points $(x, y, 1)$ with $x, y \in \mathbb{R})$, then $h$ is an affine similarity.

<!-- PAGE 960 -->

*Proof.* The fact that $h$ leaves the set of circular points ${I, J}$ fixed means that either h(I) $=$ I and h(J) $= J$ or h(I) $= J$ and h(J) $=$ I. If we define I' and J' by
$$I'= (1, -\epsilon i, 0)andJ'= (1, \epsilon i, 0)$$
where $\epsilon  = \pm 1$, then the fact that $h$ leaves the set of circular points ${I, J}$ fixed is equivalent to
$$h(I) = I'andh(J) = J'.$$
Assume that $h$ is represented by the invertible matrix
$$A = \begin{pmatrix} a & a' & a'' \\ b & b' & b'' \\ c & c' & c'' \end{pmatrix} .$$
$$\mathbb{C}$$
Then h(I) $=$ I' and h(J) $=$ J' means that there is some nonzero scalars $\lambda , \mu  \in$  such
$$\begin{pmatrix} a & a' & a'' \\ b & b' & b'' \\ c & c' & c'' \end{pmatrix} \begin{pmatrix} 1 \\ -i \\ 0 \end{pmatrix} = \lambda \begin{pmatrix} 1 \\ -\epsilon i \\ 0 \end{pmatrix} and \begin{pmatrix} a & a' & a'' \\ b & b' & b'' \\ c & c' & c'' \end{pmatrix} \begin{pmatrix} 1 \\ i \\ 0 \end{pmatrix} = \mu \begin{pmatrix} 1 \\ \epsilon i \\ 0 \end{pmatrix} .$$
We obtain the following equations:
$$\lambda  = a -ia'\mu  = a + ia'$$
$$-\lambda \epsilon i = b -ib'\mu \epsilon i = b + ib'$$
$$0 = c + ic'0 = c -ic'.$$
By adding the two equations on the first row we obtain
$$\lambda  + \mu  = 2a,$$
by subtracting the first equation from the second on the second row we obtain
$$(\lambda  + \mu )\epsilon i = 2ib',$$
so we get
$$b'= \epsilon a.$$
By subtracting the first equation from the second on the first row we obtain
$$\mu  -\lambda  = 2ia',$$
and by adding the equations on the second row we obtain
$$(\mu  -\lambda )\epsilon i = 2b,$$

<!-- PAGE 961 -->
and since $\epsilon  = \pm 1$, we have $\epsilon^{2} = 1$, so we get
$$a'= -\epsilon b.$$
By adding and subtracting the equations on the third row we obtain
$$c = c'= 0.$$
$$̸$$
Since $A$ is invertible, c'' $= 0$, and since $A$ is determined up to a nonzero scalar we may assume that c'' $= 1$, and we conclude that
$$A = \begin{pmatrix} a & -\epsilon b & a'' \\ b & \epsilon a & b'' \\ 0 & 0 & 1 \end{pmatrix} .$$
$$\mathbb{R}^{2}$$
If $h$ maps into itself, then
$$\begin{pmatrix} a & -\epsilon b & a'' \\ b & \epsilon a & b'' \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ 1 \end{pmatrix}$$
$$\mathbb{R} \mathbb{R}$$
must be real for all $x, y \in$ , which implies that a, $b$, a'', b'' $\in$ . The following proposition from Berger $[11]$ (Chapter $8$, Proposition 8.8.5.1) gives a convenient characterization of the affine similarities.
$$\longrightarrow$$

> **Proposition 26.30.** Let $(E, E , \langle$ -, $-\rangle$ ) be a Euclidean affine space of finite dimension $n \ge$
$$\longrightarrow$$
$2$. An affine map $f \in$ GA(E) is an affine similarity iff $f$ preserves orthogonality; that is,
$$\longrightarrow \longrightarrow  \longrightarrow$$
for any two vectors $u, v \in E$ , if $\langle u, v\rangle = 0$, then $\langle f (u), f (v)\rangle = 0$.
$$\longrightarrow$$

*Proof.* Assume that $f \in$ GA(E) is an affine map such that for any two vectors $u, v \in E$ , if
$$\longrightarrow  \longrightarrow \longrightarrow$$
$\langle u, v\rangle = 0$, then $\langle f (u), f (v)\rangle = 0$. Fix any nonzero $u \in E$ and consider the linear form $\phi_{u}$ given by
$$\longrightarrow  \longrightarrow \longrightarrow$$
$$\phi_{u} (v) = \langle f (u),f (v)\rangle ,v \in E .$$
$\longrightarrow \longrightarrow$ Since $f$ is invertible, $\phi_{u} (u) \neq  0$. For any $v \in E$ such that $\langle u, v\rangle = 0$, we have
$$\longrightarrow  \longrightarrow$$
$$\phi_{u} (v) = \langle f (u),f (v)\rangle = 0,$$
thus $\phi_{u}$  is a nonzero linear form vanishing on the hyperplane $H$ orthogonal to $u$, which is the kernel of the linear form $v \mapsto \langle u, v\rangle$ . Therefore, there is some nonzero scalar $\rho (u) \in \mathbb{R}$ such that
$$\longrightarrow$$
$$\phi_{u} (v) = \rho (u)\langle u, v\rangle for all v \in E .$$
Evaluating $\phi_{u}$  at $u$, we see that $\rho (u) > 0$. If we can show that $\rho (u)$ is a constant $\rho  > 0$ independent of $u$, we will have shown that
$$\longrightarrow  \longrightarrow \longrightarrow$$
$$\langle f (u),f (v)\rangle = \rho \langle u, v\rangle for all u, v \in E ,$$

<!-- PAGE 962 -->
and we will be done.
$$\longrightarrow$$
Since dim(E) $\ge 2$, pick $v$ to be any nonzero vector in $E$ such that $u$ and $v$ are linearly
$$\longrightarrow  \longrightarrow \longrightarrow$$
independent, and let us evaluate $\langle f (u + v), f (w)\rangle$ for any $w \in E$ . We have
$$\longrightarrow  \longrightarrow$$
$$\langle f (u + v),f (w)\rangle = \phi_{u+v} (w)$$
$$= \rho (u + v)\langle u + v, w\rangle$$
$$= \rho (u + v)\langle u, w\rangle + \rho (u + v)\langle v, w\rangle$$
and
$$\longrightarrow  \longrightarrow \longrightarrow  \longrightarrow  \longrightarrow$$
$$\langle f (u + v),f (w)\rangle = \langle f (u) +f (v),f (w)\rangle$$
$$\longrightarrow  \longrightarrow \longrightarrow  \longrightarrow$$
$$= \langle f (u),f (w)\rangle + \langle f (v),f (w)\rangle$$
$$= \rho (u)\langle u, w\rangle + \rho (v)\langle v, w\rangle ,$$
so we get
$$\longrightarrow$$
$$\langle (\rho (u + v) -\rho (u))u + (\rho (u + v) -\rho (v))v, w\rangle = 0for all w \in E ,$$
which implies that
$$(\rho (u + v) -\rho (u))u + (\rho (u + v) -\rho (v))v = 0.$$
Since $u$ and $v$ are linearly independent, we must have
$$\rho (u + v) = \rho (u) = \rho (v).$$
This proves that $\rho (u)$ is a constant $\rho$  independent of $u$, as claimed. The converse is trivial.
Remark: Let $f \in$ GA(E) be an affine similarity of ratio $\rho$ . If either $\rho  \neq  1$ or $\rho  = 1$ and $\longrightarrow f \in$ O(E) does not admit the eigenvalue $1$, then $f$ has a unique fixed point.
$$\longrightarrow \longrightarrow  \longrightarrow$$
Indeed, we have $f = \rho g$ for some $\rho  > 0$ and some linear isometry $g \in$ O(E), so for any origin $a \in E$, the point $a + u$ is a fixed point of $f$ iff
$$f(a + u) = a + u$$
iff
$$\longrightarrow$$
$$f(a) +f (u) = a + u$$
iff
$$--\longrightarrow$$
$$\longrightarrow$$
$$\rho g (u) =f(a)a + u$$
iff
$$--\longrightarrow$$
$$\longrightarrow$$
$$(g -\rho^{-1} id)(u) = \rho^{-1} f(a)a.$$
