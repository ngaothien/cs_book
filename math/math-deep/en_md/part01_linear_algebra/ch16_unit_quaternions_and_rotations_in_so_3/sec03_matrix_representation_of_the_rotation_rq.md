# Matrix Representation of the Rotation rq


<!-- PAGE 608 -->

> **Theorem 16.4.** Let $r$: SU(2) $\to$ SO(3) be the homomorphism of Definition 16.5. For every unit quaternion
$$q = \begin{pmatrix} a + ib & c + id \\ -(c -id) & a -ib \end{pmatrix} ,$$
we have $r_{q} = I_{3}$ iff $u = (b, c, d) = 0$ iff |a| $= 1$. If $u \neq  0$, then either $a = 0$ and $r_{q}$ is a rotation by $\pi$  around the axis of rotation determined by the vector $u = (b, c, d)$, or $0 <$ |a| $< 1$ and $r_{q}$ is the rotation around the axis of rotation determined by the vector $u = (b, c, d)$ and the angle of rotation $\theta  \neq  \pi$  with $0 < \theta  < 2\pi$ , is given by
$$\|\|$$
$$\tan(\theta /2) = \frac{u}{a} .$$
Here we are assuming that a basis $(w_{1}, w_{2})$ has been chosen in the plane orthogonal to $u = (b, c, d)$ such that $(w_{1}, w_{2}, u)$ is positively oriented, that is, $det(w_{1}, w_{2}, u) > 0$ (where $w_{1}, w_{2}, u$ are expressed over the canonical basis $(e_{1}, e_{2}, e_{3})$, which is chosen to define positive orientation).
Remark: Under the orientation defined above, we have
$$\cos(\theta /2) = a,0 < \theta  < 2\pi .$$
Note that the condition $0 < \theta  < 2\pi$  implies that $\theta$  is uniquely determined by the above equation. This is not the case if we choose $\pi$  such that $-\pi  < \theta  < \pi$  since both $\theta$  and $-\theta$ satisfy the equation, and this shows why the condition $0 < \theta  < 2\pi$  is preferable. If $0 <$ a $< 1$, then $0 < \theta  < \pi$ , and if $-1 <$ a $< 0$, then $\pi  < \theta  < 2\pi$ . In the second case, $r_{q}$ is also the rotation of axis $-u$ and of angle $-(2\pi$  - $\theta$ ) $= \theta$  - $2\pi$  with $0 < 2\pi$  - $\theta  < \pi$ , but this time the orientation of the plane orthogonal to $-u = (b, c, d)$ is the opposite orientation from before. This orientation is given by $(w_{2}, w_{1})$, so that $(w_{2}, w_{1}, -u)$ has positive orientation. Since the quaternions $q$ and $-q$ define the same rotation, we may assume that a $> 0$, in which case $0 < \theta  < \pi$ , but we have to remember that if a $< 0$ and if we pick $-q$ instead of $q$, the vector defining the axis of rotation becomes $-u$, which amounts to flipping the orientation of the plane orthogonal to the axis of rotation. The map $r$ is surjective, but this is not obvious. We will return to this point after finding the matrix representing $r_{q}$ explicitly.

## 16.3 Matrix Representation of the Rotation r

$$q$$
Given a unit quaternion $q$ of the form
$$q = \begin{pmatrix} \alpha & \beta \\ -\beta & \overline{\alpha} \end{pmatrix}$$

<!-- PAGE 609 -->
$$\mathbb{R}$$
with $\alpha  = a +$ ib, $\beta  = c +$ id, and $a^{2} + b^{2} + c^{2} + d^{2} = 1$ (a, $b, c, d \in$ ), to find the matrix representing the rotation $r_{q}$ we need to compute
$$q(x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1} )q^{*}= \begin{pmatrix} \alpha & \beta \\ -\beta & \overline{\alpha} \end{pmatrix} \begin{pmatrix} x & z -iy \\ z + iy & -x \end{pmatrix} \begin{pmatrix} \overline{\alpha} & -\beta \\ \beta & \alpha \end{pmatrix} .$$
First, we have
$$\begin{pmatrix} x & z -iy \\ z + iy & -x \end{pmatrix} \begin{pmatrix} \overline{\alpha} & -\beta \\ \beta & \alpha \end{pmatrix} = \begin{pmatrix} \overline{x\alpha} +\overline{z\beta} -\overline{iy\beta} & -x\beta  + z\alpha  -iy\alpha \\ \overline{z\alpha} +\overline{iy\alpha} -x\beta & -z\beta  -iy\beta  -x\alpha \end{pmatrix} .$$
Next, we have
$$\begin{pmatrix} \alpha & \beta \\ -\beta & \overline{\alpha} \end{pmatrix} \begin{pmatrix} \overline{x\alpha} +\overline{z\beta} -\overline{iy\beta} & -x\beta  + z\alpha  -iy\alpha \\ \overline{z\alpha} +\overline{iy\alpha} -x\beta & -z\beta  -iy\beta  -x\alpha \end{pmatrix} =$$
$$!$$
$$(\overline{\alpha \alpha} - \frac{\overline{\beta \beta}}{\overline{\alpha \beta x}} )x + i(\overline{\alpha \beta}  -\overline{\alpha \beta})y + ( -\overline{\alpha \beta} \frac{+}{\beta^{2}} \overline{\alpha \beta})z-2\alpha \beta x -i(\alpha^{2} + \beta^{2} ) \frac{y}{\alpha \beta} + (\alpha^{2} - \frac{\beta^{2}}{\alpha \beta} )z$$
$-2  + i(\overline{\alpha}^{2} +\overline{\beta}^{2})y + (\overline{\alpha}^{2} )z -(\overline{\alpha \alpha}$ - $\overline{\beta \beta})x$ - $i(\overline{\alpha \beta}$ - $)y$ - (  $+\overline{\alpha \beta})z$ Since $\alpha  = a +$ ib and $\beta  = c +$ id, with a, $b, c, d \in \mathbb{R}$, we have
$$\overline{\alpha \alpha} -\overline{\beta \beta} = a^{2}+ b^{2}-c^{2}-d^{2}$$
$$i(\overline{\alpha \beta} -\overline{\alpha \beta}) = 2(bc -ad)$$
$$\overline{\alpha \beta} +\overline{\alpha \beta} = 2(ac + bd)$$
$$-\alpha \beta  = -ac + bd -i(ad + bc)$$
$$-i(\alpha^{2} + \beta^{2} ) = 2(ab + cd) -i(a^{2}-b^{2}+ c^{2}-d^{2})$$
$$\alpha^{2} -\beta^{2} = a^{2}-b^{2}-c^{2}+ d^{2}+ i2(ab -cd).$$
Using the above, we get $(\overline{\alpha \alpha}$ - $\overline{\beta \beta})x + i(\overline{\alpha \beta}$ - $\overline{\alpha \beta})y + (\overline{\alpha \beta} +\overline{\alpha \beta})z = (a^{2} + b^{2}$ - $c^{2}$ - $d^{2})x +$ 2(bc - ad)y $+$ 2(ac $+$ bd)z, and - $2\alpha \beta x$ - $i(\alpha^{2} + \beta^{2} )y + (\alpha^{2}$ - $\beta^{2} )z =$ 2(-ac $+$ bd)x $+$ 2(ab $+$ cd)y $+ (a^{2}$ - $b^{2}$ - $c^{2} + d^{2})z$
$$-i[2(ad + bc)x + (a^{2}-b^{2}+ c^{2}-d^{2})y + 2(-ab + cd)z].$$
If we write
$$q(x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1} )q^{*}= \begin{pmatrix} x' & z'-iy' \\ z'+ iy' & -x' \end{pmatrix} ,$$
we obtain
$$x'= (a^{2}+ b^{2}-c^{2}-d^{2})x + 2(bc -ad)y + 2(ac + bd)z$$
$$y'= 2(ad + bc)x + (a^{2}-b^{2}+ c^{2}-d^{2})y + 2(-ab + cd)z$$
$$z'= 2(-ac + bd)x + 2(ab + cd)y + (a^{2}-b^{2}-c^{2}+ d^{2})z.$$
In summary, we proved the following result.
