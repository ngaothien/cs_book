# Problems


<!-- PAGE 621 -->
$\bullet$  The (real) vector space $\mathfrak{su}(2)$ of $2 \times  2$ Hermitian matrices with zero trace. $\bullet$  The group homomorphism $r$: SU(2) $\to$ SO(3); Ker $(r) = {+I, -I}. \bullet$  The matrix representation $R_{q}$ of the rotation $r_{q}$ induced by a unit quaternion $q. \bullet$  Surjectivity of the homomorphism $r$: SU(2) $\to$ SO(3). $\bullet$  The exponential map exp: $\mathfrak{su}(2) \to$ SU(2). $\bullet$  Surjectivity of the exponential map exp: $\mathfrak{su}(2) \to$ SU(2). $\bullet$  Finding a logarithm of a quaternion. $\bullet$  Quaternion interpolation. $\bullet$  Shoemake’s slerp interpolation formula. $\bullet$  Sections $s$: SO(3) $\to$ SU(2) of $r$: SU(2) $\to$ SO(3).

## 16.9 Problems

Problem 16.1. Verify the quaternion identities
$$i^{2}= j^{2}= k^{2}= ijk = -1,$$
$$ij = -ji = k,$$
$$jk = -kj = i,$$
$$ki = -ik = j.$$
Problem 16.2. Check that for every quaternion $X =$ a1 $+$ bi $+$ cj $+$ dk, we have
$$XX^{*}= X^{*}X = (a^{2}+ b^{2}+ c^{2}+ d^{2})1.$$
Conclude that if $X \neq  0$, then $X$ is invertible and its inverse is given by
$$X^{-1}= (a^{2}+ b^{2}+ c^{2}+ d^{2})^{-1}X^{*}.$$
Problem 16.3. Given any two quaternions $X = a1+bi+cj+dk$ and $Y = a'1+b'i+c'j+d'k$, prove that
$$XY = (aa'-bb'-cc'-dd')1 + (ab'+ ba'+ cd'-dc')i$$
$$+ (ac'+ ca'+ db'-bd')j + (ad'+ da'+ bc'-cb')k.$$
Also prove that if $X = [a, U]$ and $Y =$ [a', U' ], the quaternion product $XY$ can be expressed as
$$XY = [aa'-U \cdot  U', aU'+ a'U + U \times  U'].$$

<!-- PAGE 622 -->
Problem 16.4. Let Ad: SU(2) $\to GL(\mathfrak{su}(2))$ be the map defined such that for every $q \in$ SU(2),
$$Ad_{q}(A) = qAq^{*},A \in \mathfrak{su}(2),$$
where $q^{*}$ is the inverse of $q$ (since SU(2) is a unitary group) Prove that the map $Ad_{q}$ is an invertible linear map from $\mathfrak{su}(2)$ to itself and that Ad is a group homomorphism.
Problem 16.5. Prove that every Hermitian matrix with zero trace is of the form $x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1}$ , with
$$\sigma_{1}  = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} ,\sigma_{2}  = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} ,\sigma_{3}  = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} .$$
Check that $i = i\sigma_{3} , j = i\sigma_{2}$ , and that $k = i\sigma_{1}$ .
Problem 16.6. If
$$B = \begin{pmatrix} 0 & -u_{3} & u_{2} \\ u_{3} & 0 & -u_{1} \\ u_{2} & u_{1} & 0 \end{pmatrix} ,$$
$$-$$
and if we write $\theta  = p\overline{u}_{1}^{2} \overline{+}\overline{u}_{2}^{2} \overline{+}\overline{u}_{3}^{2}$ (with $0 \le \theta  \le \pi$ ), then the Rodrigues formula says that
$$-$$
$$e^{B}= I + \frac{\sin \theta}{\theta} B + \frac{(1cos \theta )}{\theta^{2}} B^{2},\theta  \neq  0,$$
with $e^{0} =$ I. Check that $tr(e^{B}) = 1 + 2$ cos $\theta$ . Prove that the quaternion $q$ corresponding to the rotation $R = e^{B}$ (with $B \neq  0)$ is given by
$$$$
$$q =\cos \begin{pmatrix} \theta \\ 2 \end{pmatrix} , \sin \begin{pmatrix} \theta \\ 2 \end{pmatrix} \begin{pmatrix} u_{1}, u_{2}, u_{3} \\ \theta & \overline{\theta} & \overline{\theta} \end{pmatrix} .$$
Problem 16.7. For every matrix $A \in \mathfrak{su}(2)$, with
$$A = \begin{pmatrix} iu_{1} & u_{2} + iu_{3} \\ -u_{2} + iu_{3} & -iu_{1} \end{pmatrix} ,$$
prove that if we write $\theta  = p\overline{u}_{1}^{2} \overline{+}\overline{u}_{2}^{2} \overline{+}\overline{u}_{3}^{2}$, then
$$e^{A}= \cos \theta I + \frac{\sin \theta}{\theta} A,\theta  \neq  0,$$
and $e^{0} =$ I. Conclude that $e^{A}$ is a unit quaternion representing the rotation of angle $2\theta$  and axis $(u_{1}, u_{2}, u_{3})$ (or I when $\theta  = k\pi , k \in \mathbb{Z})$.
Problem 16.8. Write a Matlab program implementing the method of Section 16.4 for finding a unit quaternion corresponding to a rotation matrix.
Problem 16.9. Show that there is a very simple method for producing an orthonormal
$$\mathbb{R}^{4}$$
frame in whose first vector is any given nonnull vector (a, $b, c, d)$.

<!-- PAGE 623 -->
Problem 16.10. Let $i, j$, and $k$, be the unit vectors of coordinates $(1, 0, 0), (0, 1, 0)$, and $(0, 0, 1)$ in $\mathbb{R}^{3}$.
$(1)$ Describe geometrically the rotations defined by the following quaternions:
$$p = (0, i),q = (0, j).$$
Prove that the interpolant $Z(\lambda$ ) $= p(p^{-1}q)^{\lambda}$ is given by
$$Z(\lambda ) = (0, \cos(\lambda \pi /2)i + \sin(\lambda \pi /2)j) .$$
Describe geometrically what this rotation is.
$(2)$ Repeat Question $(1)$ with the rotations defined by the quaternions
$$p = \frac{1}{2} , \frac{\sqrt{3}}{2} i!,q = (0, j).$$
Prove that the interpolant $Z(\lambda$ ) is given by
$$!$$
$$1$$
$$Z(\lambda ) =2 \cos(\lambda \pi /2), \frac{\sqrt{3}}{2} \cos(\lambda \pi /2)i + \sin(\lambda \pi /2)j.$$
Describe geometrically what this rotation is.
$(3)$ Repeat Question $(1)$ with the rotations defined by the quaternions
$$p = \begin{pmatrix} 1 & 1 \\ \sqrt,\sqrt i \\ \overline{2} & \overline{2} \end{pmatrix} ,q = \begin{pmatrix} 1 \\ 0,\sqrt(i + j) \\ \overline{2} \end{pmatrix} .$$
Prove that the interpolant $Z(\lambda$ ) is given by
$$11$$
$Z(\lambda$ ) $= \sqrt2 cos(\lambda \pi /3)$ - $\sqrt6 sin(\lambda \pi /3)$,
$$\sqrt\sqrt 2$$
$$(1/\overline{2 \cos(}\lambda \pi /3) + 1/\overline{6 \sin(}\lambda \pi /3))i +\sqrt6 \sin(\lambda \pi /3)j.$$
Problem 16.11. Prove that
$$w \times  (u \times  v) = (w \cdot  v)u -(u \cdot  w)v.$$
Conclude that
$$u \times  (u \times  v) = (u \cdot  v)u -(u \cdot  u)v.$$

<!-- PAGE 624 -->
