# The Exponential Map exp2mu-:6muplus1musu(2)SU(2)


<!-- PAGE 613 -->
It is easy to check that whenever we computed a square root, if we had chosen a negative sign instead of a positive sign, we would obtain the quaternion $-q$. However, both $q$ and $-q$ determine the same rotation $r_{q}$. The above discussion involving the cases tr(R) $\neq  -1$ and tr(R) $= -1$ is reminiscent of the procedure for finding a logarithm of a rotation matrix using the Rodrigues formula (see Section 12.7). This is not surprising, because if
$$B = \begin{pmatrix} 0 & -u_{3} & u_{2} \\ u_{3} & 0 & -u_{1} \\ u_{2} & u_{1} & 0 \end{pmatrix}$$
$$-$$
and if we write $\theta  = p\overline{u}_{1}^{2} \overline{+}\overline{u}_{2}^{2} \overline{+}\overline{u}_{3}^{2}$ (with $0 \le \theta  \le 2\pi$ ), then the Rodrigues formula says that
$$-$$
$$e^{B}= I + \frac{\sin \theta}{\theta} B + \frac{(1cos \theta )}{\theta^{2}} B^{2},\theta  \neq  0,$$
with $e^{0} =$ I. It is easy to check that $tr(e^{B}) = 1+2$ cos $\theta$ . Then it is an easy exercise to check that the quaternion $q$ corresponding to the rotation $R = e^{B}$ (with $B \neq  0)$ is given by
$$$$
$$q =\cos \begin{pmatrix} \theta \\ 2 \end{pmatrix} , \sin \begin{pmatrix} \theta \\ 2 \end{pmatrix} \begin{pmatrix} u_{1}, u_{2}, u_{3} \\ \theta & \overline{\theta} & \overline{\theta} \end{pmatrix} .$$
So the method for finding the logarithm of a rotation $R$ is essentially the same as the method for finding a quaternion defining $R$.
$$\mathbb{R}^{4}$$
Remark: Geometrically, the group SU(2) is homeomorphic to the 3-sphere $S^{3}$ in ,
$$\mathbb{R}^{4}$$
$$S^{3}= {(x, y, z, t) \in | x^{2}+ y^{2}+ z^{2}+ t^{2}= 1}.$$
However, since the kernel of the surjective homomorphism $r$: SU(2) $\to$ SO(3) is ${I, -I}$, as a topological space, SO(3) is homeomorphic to the quotient of $S^{3}$ obtained by identifying antipodal points $(x, y, z, t)$ and -(x, $y, z, t)$. This quotient space is the (real) projective space $\mathbb{RP}^{3}  \mathbb{RP}^{3}$ , and it is more complicated than $S^{3}$. The space $S^{3}$ is simply-connected, but is not.

## 16.5 The Exponential Map exp: \mathfrak{su}(2) \to SU(2)

Given any matrix $A \in \mathfrak{su}(2)$, with
$$A = \begin{pmatrix} iu_{1} & u_{2} + iu_{3} \\ -u_{2} + iu_{3} & -iu_{1} \end{pmatrix} ,$$
it is easy to check that
$$A^{2}= -\theta^{2} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} ,$$
with $\theta  = p\overline{u}_{1}^{2} \overline{+}\overline{u}_{2}^{2} \overline{+}\overline{u}_{3}^{2}$. Then we have the following formula whose proof is very similar to the proof of the formula given in Proposition 9.23.

<!-- PAGE 614 -->

> **Proposition 16.7.** For every matrix $A \in \mathfrak{su}(2)$, with
$$A = \begin{pmatrix} iu_{1} & u_{2} + iu_{3} \\ -u_{2} + iu_{3} & -iu_{1} \end{pmatrix} ,$$
if we write $\theta  = p\overline{u}_{1}^{2} \overline{+}\overline{u}_{2}^{2} \overline{+}\overline{u}_{3}^{2}$, then
$$e^{A}= \cos \theta I + \frac{\sin \theta}{\theta} A,\theta  \neq  0,$$
and $e^{0} =$ I. Therefore, by the discussion at the end of the previous section, $e^{A}$ is a unit quaternion representing the rotation of angle $2\theta$  and axis $(u_{1}, u_{2}, u_{3})$ (or I when $\theta  = k\pi , k \in \mathbb{Z})$. The above formula shows that we may assume that $0 \le \theta  \le \pi$ . Proposition 16.7 shows that the exponential yields a map exp: $\mathfrak{su}(2) \to$ SU(2). It is an analog of the exponential map exp: $\mathfrak{so}(3) \to$ SO(3).
Remark: $Because\mathfrak{so}(3) and\mathfrak{su}(2)$ are real vector spaces of dimension $3$, they are isomorphic, and it is easy to construct an isomorphism. In fact, $\mathfrak{so}(3)$ and $\mathfrak{su}(2)$ are isomorphic as Lie algebras, which means that there is a linear isomorphism preserving the the Lie bracket $[A, B] = AB$ - $BA$. However, as observed earlier, the groups SU(2) and SO(3) are not isomorphic. An equivalent, but often more convenient, formula is obtained by assuming that $u = (u_{1}, u_{2}, u_{3})$ is a unit vector, equivalently det(A) $= 1$, in which case $A^{2} = -I$, so we have
$$e^{\theta A}= \cos \theta I + \sin \theta A.$$
Using the quaternion notation, this is read as
$$e^{\theta A}= [\cos \theta , \sin \theta  u].$$

> **Proposition 16.8.** The exponential map exp: $\mathfrak{su}(2) \to$ SU(2) is surjective

*Proof.* We give an algorithm to find the logarithm $A \in \mathfrak{su}(2)$ of a unit quaternion
$$q = \begin{pmatrix} \alpha & \beta \\ -\beta & \overline{\alpha} \end{pmatrix}$$
with $\alpha  = a +$ bi and $\beta  = c +$ id. If $q =$ I (i.e. $a = 1)$, then $A = 0$. If $q = -I$ (i.e. $a = -1)$, then
$$A = \pm \pi \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix} .$$

<!-- PAGE 615 -->
Otherwise, $a \neq  \pm 1$ and $(b, c, d) \neq  (0, 0, 0)$, and we are seeking some $A = \theta B \in \mathfrak{su}(2)$ with det(B) $= 1$ and $0 < \theta  < \pi$ , such that, by Proposition 16.7,
$$q = e^{\theta B}= \cos \theta I + \sin \theta B.$$
Let
$$B = \begin{pmatrix} iu_{1} & u_{2} + iu_{3} \\ -u_{2} + iu_{3} & -iu_{1} \end{pmatrix} ,$$
with $u = (u_{1}, u_{2}, u_{3})$ a unit vector. We must have
$$a = \cos \theta ,e^{\theta B}-(e^{\theta B})^{*}= q -q^{*}.$$
Since $0 < \theta  < \pi$ , we have sin $\theta  \neq  0$, and
$$2 \sin \theta \begin{pmatrix} iu_{1} & u_{2} + iu_{3} \\ -u_{2} + iu_{3} & -iu_{1} \end{pmatrix} = \begin{pmatrix} \alpha  -\overline{\alpha} & 2\beta \\ -2\beta & \overline{\alpha} -\alpha \end{pmatrix} .$$
Thus, we get
$$u_{1} = \frac{1}{\sin} \theta  b,u_{2} + iu_{3} = \frac{1}{\sin \theta} (c + id);$$
that is,
$$\cos \theta  = a(0 < \theta  < \pi )$$
$$(u_{1}, u_{2}, u_{3}) = \frac{1}{\sin \theta} (b, c, d).$$
Since $a^{2}+b^{2}+c^{2}+d^{2} = 1$ and $a =$ cos $\theta$ , the vector $(b, c, d)/$ sin $\theta$  is a unit vector. Furthermore if the quaternion $q$ is of the form $q =$ [cos $\theta$ , sin $\theta u]$ where $u = (u_{1}, u_{2}, u_{3})$ is a unit vector (with $0 < \theta  < \pi$ ), then
$$A = \theta \begin{pmatrix} iu_{1} & u_{2} + iu_{3} \\ -u_{2} + iu_{3} & -iu_{1} \end{pmatrix} (*_{\log})$$
is a logarithm of $q$. Observe that not only is the exponential map exp: $\mathfrak{su}(2) \to$ SU(2) surjective, but the above proof shows that it is injective on the open ball
$${\theta B \in \mathfrak{su}(2) | \det(B) = 1, 0 \le \theta  < \pi }.$$
Also, unlike the situation where in computing the logarithm of a rotation matrix $R \in$ SO(3) we needed to treat the case where tr(R) $= -1$ (the angle of the rotation is $\pi$ ) in a special way, computing the logarithm of a quaternion (other than $\pm$ I) does not require any case analysis; no special case is needed when the angle of rotation is $\pi$ .
