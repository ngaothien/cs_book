# Representation of Rotation in SO(3) By Quaternions in SU(2)


<!-- PAGE 603 -->
Also observe that
$$X^{*}= \begin{pmatrix} a -ib & -(c + id) \\ c -id & a + ib \end{pmatrix} = a1 -bi -cj -dk.$$
This implies that if $X \neq  0$, then $X$ is invertible and its inverse is given by
$$X^{-1}= (a^{2}+ b^{2}+ c^{2}+ d^{2})^{-1}X^{*}.$$
As a consequence, it can be verified that $\mathbb{H}$ is a skew field (a noncommutative field). It is also a real vector space of dimension $4$ with basis $(1, i, j, k)$; thus as a vector space, $\mathbb{H}$ is isomorphic to $\mathbb{R}^{4}$.

> **Definition 16.2.** A concise notation for the quaternion $X$ defined by $\alpha  = a +$ ib and $\beta  = c +$ id is
$$X = [a, (b, c, d)].$$
$$We call a the scalar part of X and (b, c, d) \frac{the}{X.} vector part of \frac{X.}{X} With this notation,$$
$X^{*} = [a$, -(b, $c, d)]$, which is often denoted by  The quaternion  is called the conjugate of $X$. If $q$ is a unit quaternion, then $\overline{q}$ is the multiplicative inverse of $q$.

## 16.2 Representation of Rotations in SO(3) by Quater-

$$nions in SU(2)$$
The key to representation of rotations in SO(3) by unit quaternions is a certain group homomorphism called the adjoint representation of SU(2). To define this mapping, first we define the real vector space $\mathfrak{su}(2)$ of skew Hermitian matrices.

> **Definition 16.3.** The (real) vector space $\mathfrak{su}(2)$ of $2 \times  2$ skew Hermitian matrices with zero trace is given by
$$$$
$$\mathfrak{su}(2) = \begin{pmatrix} ix & y + iz \\ -y + iz & -ix \end{pmatrix} (x, y, z) \in \mathbb{R}^{3}.$$
Observe that for every matrix $A \in \mathfrak{su}(2)$, we have $A^{*} = -A$, that is, $A$ is skew Hermitian, and that tr(A) $= 0$.

> **Definition 16.4.** The adjoint representation of the group SU(2) is the group homomorphism Ad: SU(2) $\to GL(\mathfrak{su}(2))$ defined such that for every $q \in$ SU(2), with
$$q = \begin{pmatrix} \alpha & \beta \\ -\beta & \overline{\alpha} \end{pmatrix} \in SU(2),$$
we have
$$Ad_{q}(A) = qAq^{*},A \in \mathfrak{su}(2),$$
where $q^{*}$ is the inverse of $q$ (since SU(2) is a unitary group) and is given by
$$q^{*}= \begin{pmatrix} \overline{\alpha} & -\beta \\ \beta & \alpha \end{pmatrix} .$$

<!-- PAGE 604 -->
One needs to verify that the map $Ad_{q}$ is an invertible linear map $from\mathfrak{su}(2)$ to itself, and that Ad is a group homomorphism, which is easy to do.
$$\mathbb{R}^{3}  \mathbb{H}$$
In order to associate a rotation $\rho_{q}$  (in SO(3)) to $q$, we need to embed into  as the pure quaternions, by
$$\psi (x, y, z) = \begin{pmatrix} ix & y + iz \\ -y + iz & -ix \end{pmatrix} ,(x, y, z) \in \mathbb{R}^{3}.$$
Then $q$ defines the map $\rho_{q}$  (on $\mathbb{R}^{3})$ given by
$$\rho_{q} (x, y, z) = \psi^{-1} (q\psi (x, y, z)q^{*}).$$
Therefore, modulo the isomorphism $\psi$ , the linear map $\rho_{q}$  is the linear isomorphism $Ad_{q}$. In fact, it turns out that $\rho_{q}$  is a rotation (and so is $Ad_{q})$, which we will prove shortly. So, the representation of rotations in SO(3) by unit quaternions is just the adjoint representation of SU(2); its image is a subgroup of $GL(\mathfrak{su}(2))$ isomorphic to SO(3).
$$\mathbb{R}^{3}$$
Technically, it is a bit simpler to embed in the (real) vector spaces of Hermitian matrices with zero trace,
$$$$
$$\begin{pmatrix} x & z -iy \\ z + iy & -x \end{pmatrix} x, y, z \in \mathbb{R}.$$
Since the matrix $\psi (x, y, z)$ is skew-Hermitian, the matrix $-i\psi (x, y, z)$ is Hermitian, and we have
$$-i\psi (x, y, z) = \begin{pmatrix} x & z -iy \\ z + iy & -x \end{pmatrix} = x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1} ,$$
where $\sigma_{1} , \sigma_{2} , \sigma_{3}$  are the Pauli spin matrices
$$\sigma_{1}  = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} ,\sigma_{2}  = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} ,\sigma_{3}  = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} .$$
Matrices of the form $x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1}$  are Hermitian matrices with zero trace. It is easy to see that every $2 \times  2$ Hermitian matrix with zero trace must be of this form. (observe that $(i\sigma_{1} , i\sigma_{2} , i\sigma_{3}$ ) forms a basis of $\mathfrak{su}(2)$. Also, $i = i\sigma_{3} , j = i\sigma_{2} , k = i\sigma_{1}$ .) Now, if $A = x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1}$  is a Hermitian $2 \times  2$ matrix with zero trace, we have
$$(qAq^{*})^{*}= qA^{*}q^{*}= qAq^{*},$$
so $qAq^{*}$ is also Hermitian, and
$$\mathrm{tr}(qAq^{*}) = \mathrm{tr}(Aq^{*}q) = \mathrm{tr}(A),$$
and $qAq^{*}$ also has zero trace. Therefore, the map $A \mapsto qAq^{*}$ preserves the Hermitian matrices with zero trace. We also have
$$\det(x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1} ) = \det \begin{pmatrix} x & z -iy \\ z + iy & -x \end{pmatrix} = -(x^{2}+ y^{2}+ z^{2}),$$

<!-- PAGE 605 -->
and
$$\det(qAq^{*}) = \det(q) \det(A) \det(q^{*}) = \det(A) = -(x^{2}+ y^{2}+ z^{2}).$$
$$\mathbb{R}^{3}$$
We can embed into the space of Hermitian matrices with zero trace by
$$\phi (x, y, z) = x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1} .$$
Note that
$$\phi  = -i\psi and\phi^{-1} = i\psi^{-1} .$$
$$\mathbb{R}^{3}$$

> **Definition 16.5.** The unit quaternion $q \in$ SU(2) induces a map $r_{q}$ on by
$$r_{q}(x, y, z) = \phi^{-1} (q\phi (x, y, z)q^{*}) = \phi^{-1} (q(x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1} )q^{*}).$$
The map $r_{q}$ is clearly linear since $\phi$  is linear.

> **Proposition 16.1.** For every unit quaternion $q \in$ SU(2), the linear map $r_{q}$ is orthogonal, that is, $r_{q} \in$ O(3).

*Proof.* Since
$$-\|(x, y, z)\|^{2}= -(x^{2}+ y^{2}+ z^{2}) = \det(x\sigma^{3} + y\sigma^{2} + z\sigma_{1} ) = \det(\phi (x, y, z)),$$
we have
$$-\|r_{q}(x, y, z)\|^{2}= \det(\phi (r_{q}(x, y, z))) = \det(q(x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1} )q^{*})$$
$$= \det(x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1} ) = -

$(x, y, z)^{2}$

,$$ and we deduce that $r_{q}$ is an isometry. Thus, $r_{q} \in$ O(3). In fact, $r_{q}$ is a rotation, and we can show this by finding the fixed points of $r_{q}$. Let $q$ be a unit quaternion of the form
$$q = \begin{pmatrix} \alpha & \beta \\ -\beta & \overline{\alpha} \end{pmatrix}$$
$$\mathbb{R}$$
with $\alpha  = a +$ ib, $\beta  = c +$ id, and $a^{2} + b^{2} + c^{2} + d^{2} = 1$ (a, $b, c, d \in$ ). If $b = c = d = 0$, then $q =$ I and $r_{q}$ is the identity so we may assume that $(b, c, d) \neq (0, 0, 0)$.

> **Proposition 16.2.** If $(b, c, d) \neq  (0, 0, 0)$, then the fixed points of $r_{q}$ are solutions $(x, y, z)$ of the linear system
$$-dy + cz = 0$$
$$cx -by = 0$$
$$dx -bz = 0.$$
This linear system has the nontrivial solution $(b, c, d)$ and has rank $2$. Therefore, $r_{q}$ has the eigenvalue $1$ with multiplicity $1$, and $r_{q}$ is a rotation whose axis is determined by $(b, c, d)$.

<!-- PAGE 606 -->

*Proof.* We have $r_{q}(x, y, z) = (x, y, z)$ iff
$$\phi^{-1} (q(x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1} )q^{*}) = (x, y, z)$$
iff
$$q(x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1} )q^{*}= \phi (x, y, z),$$
and since
$$\phi (x, y, z) = x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1}  = A$$
with
$$A = \begin{pmatrix} x & z -iy \\ z + iy & -x \end{pmatrix} ,$$
we see that $r_{q}(x, y, z) = (x, y, z)$ iff
$$qAq^{*}= AiffqA = Aq.$$
We have
$$qA = \begin{pmatrix} \alpha & \beta \\ -\beta & \overline{\alpha} \end{pmatrix} \begin{pmatrix} x & z -iy \\ z + iy & -x \end{pmatrix} = \begin{pmatrix} \alpha x + \beta z + i\beta y & \alpha z -i\alpha y -\beta x \\ -\beta x +\overline{\alpha z} +\overline{i\alpha y} & -\beta z + i\beta y -\overline{\alpha x} \end{pmatrix}$$
and
$$Aq = \begin{pmatrix} x & z -iy \\ z + iy & -x \end{pmatrix} \begin{pmatrix} \alpha & \beta \\ -\beta & \overline{\alpha} \end{pmatrix} = \begin{pmatrix} \alpha x -\overline{\beta z} +\overline{i\beta y} & \beta x +\overline{\alpha z} -\overline{i\alpha y} \\ \alpha z + i\alpha y + \beta x & \beta z + i\beta y -\overline{\alpha x} \end{pmatrix} .$$
By equating qA and Aq, we get
$$i(\beta  -\overline{\beta})y + (\beta  +\overline{\beta})z = 0$$
$$2\beta x + i(\alpha  -\overline{\alpha})y + (\overline{\alpha} -\alpha )z = 0$$
$$2\overline{\beta x} + i(\alpha  -\overline{\alpha})y + (\alpha  -\overline{\alpha})z = 0$$
$$i(\beta  -\overline{\beta})y + (\beta  +\overline{\beta})z = 0.$$
The first and the fourth equation are identical and the third equation is obtained by conjugating the second, so the above system reduces to
$$i(\beta  -\overline{\beta})y + (\beta  +\overline{\beta})z = 0$$
$$2\beta x + i(\alpha  -\overline{\alpha})y + (\overline{\alpha} -\alpha )z = 0.$$
Replacing $\alpha$  by $a +$ ib and $\beta$  by $c +$ id, we get
$$-dy + cz = 0$$
$$cx -by + i(dx -bz) = 0,$$

<!-- PAGE 607 -->
which yields the equations
$$-dy + cz = 0$$
$$cx -by = 0$$
$$dx -bz = 0.$$
This linear system has the nontrivial solution $(b, c, d)$ and the matrix of this system is
$$\begin{pmatrix} 0 & -d & c \\ c & -b & 0 \\ d & 0 & b \end{pmatrix} .$$
$$-$$
Since $(b, c, d) \neq  (0, 0, 0)$, this matrix always has a $2 \times  2$ submatrix which is nonsingular, so it has rank $2$, and consequently its kernel is the one-dimensional space spanned by $(b, c, d)$. Therefore, $r_{q}$ has the eigenvalue $1$ with multiplicity $1$. If we had $det(r_{q}) = -1$, then the eigenvalues of $r_{q}$ would be either $(-1, 1, 1)$ or $(-1, e^{i\theta}, e^{-i\theta})$ with $\theta$ ̸ $= k2\pi$  (with $k \in \mathbb{Z})$, contradicting the fact that $1$ is an eigenvalue with multiplicity $1$. Therefore, $r_{q}$ is a rotation; in fact, its axis is determined by $(b, c, d)$. In summary, $q \mapsto r_{q}$ is a map $r$ from SU(2) to SO(3).

> **Theorem 16.3.** The map $r$: SU(2) $\to$ SO(3) is a homomorphism whose kernel is ${I, -I}$.

*Proof.* This map is a homomorphism, because if $q_{1}, q_{2} \in$ SU(2), then
$$r_{q2}(r_{q1}(x, y, z)) = \phi^{-1} (q_{2}\phi (r_{q1}(x, y, z))q_{2}^{*})$$
$$= \phi^{-1} (q_{2}\phi (\phi^{-1} (q_{1}\phi (x, y, z)q_{1}^{*}))q_{2}^{*})$$
$$= \phi^{-1} ((q_{2}q_{1})\phi (x, y, z)(q_{2}q_{1})^{*})$$
$$= r_{q2q1}(x, y, z).$$
The computation that showed that if $(b, c, d) \neq  (0, 0, 0)$, then $r_{q}$ has the eigenvalue $1$ with multiplicity $1$ implies the following: if $r_{q} = I_{3}$, namely $r_{q}$ has the eigenvalue $1$ with multiplicity $3$, then $(b, c, d) = (0, 0, 0)$. But then $a = \pm 1$, and so $q = \pm I_{2}$. Therefore, the kernel of the homomorphism $r$: SU(2) $\to$ SO(3) is ${I, -I}$.
Remark: Perhaps the quickest way to show that $r$ maps SU(2) into SO(3) is to observe that the map $r$ is continuous. Then, since it is known that SU(2) is connected, its image by $r$ lies in the connected component of I, namely SO(3). Proposition 16.2 showed that if $u = (b, c, d) \neq  (0, 0, 0)$, then $r_{q}$ is a rotation whose axis is determined by $u = (b, c, d)$. The angle $\theta$  of this rotation can also be determined. The following result is proven in Gallier $[73]$ (Chapter $9)$.
