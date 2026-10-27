# An Algorithm to Find a Quaternion Representing a Rotation


<!-- PAGE 610 -->

> **Proposition 16.5.** The matrix representing $r_{q}$ is
$$R_{q} = \begin{pmatrix} a^{2}+ b^{2}-c^{2}-d^{2} & 2bc -2ad & 2ac + 2bd \\ 2bc + 2ad & a^{2}-b^{2}+ c^{2}-d^{2} & -2ab + 2cd \\ 2ac + 2bd & 2ab + 2cd & a^{2} & b^{2} & c^{2}+ d^{2} \end{pmatrix} .$$
$$---$$
Since $a^{2} + b^{2} + c^{2} + d^{2} = 1$, this matrix can also be written as
$$R_{q} = \begin{pmatrix} 2a^{2}+ 2b^{2}-1 & 2bc -2ad & 2ac + 2bd \\ 2bc + 2ad & 2a^{2}+ 2c^{2}-1 & -2ab + 2cd \\ 2ac + 2bd & 2ab + 2cd & 2a^{2}+ 2d^{2} & 1 \end{pmatrix} .$$
$$--$$
The above is the rotation matrix in Euler form induced by the quaternion $q$, which is the matrix corresponding to $\rho_{q}$ . This is because
$$\phi  = -i\psi ,\phi^{-1} = i\psi^{-1} ,$$
so $r_{q}(x, y, z) = \phi^{-1} (q\phi (x, y, z)q^{*}) = i\psi^{-1} (q(-i\psi (x, y, z))q^{*}) = \psi^{-1} (q\psi (x, y, z)q^{*}) = \rho_{q} (x, y, z)$, and so $r_{q} = \rho_{q}$ . We showed that every unit quaternion $q \in$ SU(2) induces a rotation $r_{q} \in$ SO(3), but it is not obvious that every rotation can be represented by a quaternion. This can shown in various ways. One way to is use the fact that every rotation in SO(3) is the composition of two reflec-
$$\mathbb{R}^{3}$$
tions, and that every reflection $\sigma$  of can be represented by a quaternion $q$, in the sense that
$$\sigma (x, y, z) = -\phi^{-1} (q\phi (x, y, z)q^{*}).$$
Note the presence of the negative sign. This is the method used in Gallier $[73]$ (Chapter $9)$.

## 16.4 An Algorithm to Find a Quaternion Representing

$$a Rotation$$

> **Theorem 16.6.** The homomorphism $r$: SU(2) $\to$ SO(3) is surjective. Here is an algorithmic method to find a unit quaternion $q$ representing a rotation matrix $R$, which provides a proof of Theorem 16.6. Let
$$\mathbb{R}$$
$$q = \begin{pmatrix} a + ib & c + id \\ -(c -id) & a -ib \end{pmatrix} ,a^{2}+ b^{2}+ c^{2}+ d^{2}= 1, a, b, c, d \in .$$

<!-- PAGE 611 -->
First observe that the trace of $R_{q}$ is given by
$$\mathrm{tr}(R_{q}) = 3a^{2}-b^{2}-c^{2}-d^{2},$$
but since $a^{2} + b^{2} + c^{2} + d^{2} = 1$, we get $tr(R_{q}) = 4a^{2}$ - $1$, so
$$a^{2}= \frac{\mathrm{tr}(R_{q}) + 1}{4} .$$
If $R \in$ SO(3) is any rotation matrix and if we write
$$R = \begin{pmatrix} r_{11} & r_{12} & r_{13} \\ r_{21} & r_{22} & r_{23} \\ r_{31} & r_{32} & r_{33}, \end{pmatrix}$$
we are looking for a unit quaternion $q \in$ SU(2) such that $R_{q} = R$. Therefore, we must have
$$a^{2}= \frac{\mathrm{tr}(R) + 1}{4} .$$
We also know that
$$\mathrm{tr}(R) = 1 + 2 \cos \theta ,$$
where $\theta  \in [0, \pi$ ] is the angle of the rotation $R$, so we get
$$a^{2}= \frac{\cos \theta  + 1}{2} = \cos^{2} \begin{pmatrix} \theta \\ 2 \end{pmatrix} ,$$
which implies that
$$|a| = \cos \begin{pmatrix} \theta \\ 2 \end{pmatrix} (0 \le \theta  \le \pi ).$$
Note that we may assume that $\theta  \in [0, \pi$ ], because if $\pi  \le \theta  \le 2\pi$ , then $\theta$  - $2\pi  \in [-\pi , 0]$, and then the rotation of angle $\theta$  - $2\pi$  and axis determined by the vector $(b, c, d)$ is the same as the rotation of angle $2\pi$  - $\theta  \in [0, \pi$ ] and axis determined by the vector -(b, $c, d)$. There are two cases. Case $1$. tr(R) $\neq  -1$, or equivalently $\theta  \neq  \pi$ . In this case $a \neq  0$. Pick
$$a = \frac{p\overline{\mathrm{tr}(}\overline{R}\overline{) + 1}}{2} .$$
Then by equating $R$ - $R^{\top}$ and $R_{q}$ - $R_{q}^{\top}$ , we get
$$4ab = r_{32} -r_{23}$$
$$4ac = r_{13} -r_{31}$$
$$4ad = r_{21} -r_{12},$$

<!-- PAGE 612 -->
which yields
$$-  -  -$$
$$b = \frac{r_{32}r_{23}}{4a} ,c = \frac{r_{13}r_{31}}{4a} ,d = \frac{r_{21}r_{12}}{4a} .$$
Case $2$. tr(R) $= -1$, or equivalently $\theta  = \pi$ . In this case $a = 0$. By equating $R + R^{\top}$ and $R_{q} + R_{q}^{\top}$ , we get
$$4bc = r_{21} + r_{12}$$
$$4bd = r_{13} + r_{31}$$
$$4cd = r_{32} + r_{23}.$$
By equating the diagonal terms of $R$ and $R_{q}$, we also get
$$b^{2}= \frac{1 + r_{11}}{2}$$
$$c^{2}= \frac{1 + r_{22}}{2}$$
$$d^{2}= \frac{1 + r_{33}}{2} .$$
Since $q \neq  0$ and $a = 0$, at least one of $b, c, d$ is nonzero. If $b \neq  0$, let
$$b = \frac{\sqrt{1 +}\overline{r}_{11}}{\overline{2}} \sqrt,$$
and determine $c, d$ using
$$4bc = r_{21} + r_{12}$$
$$4bd = r_{13} + r_{31}.$$
If $c \neq  0$, let
$$c = \frac{\sqrt{1 +}\overline{r}_{22}}{\overline{2}} \sqrt,$$
and determine $b, d$ using
$$4bc = r_{21} + r_{12}$$
$$4cd = r_{32} + r_{23}.$$
If $d \neq  0$, let
$$d = \frac{\sqrt{1 +}\overline{r}_{33}}{\overline{2}} \sqrt,$$
and determine $b, c$ using
$$4bd = r_{13} + r_{31}$$
$$4cd = r_{32} + r_{23}.$$
