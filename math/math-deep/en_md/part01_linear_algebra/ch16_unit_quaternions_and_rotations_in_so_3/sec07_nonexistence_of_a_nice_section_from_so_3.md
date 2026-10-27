# Nonexistence of a ``Nice'' Section from SO(3) to SU(2)


<!-- PAGE 618 -->
and $u \cdot  u = 1$, so we get
$$\theta$$
$$\nu  = - \frac{\sin \lambda \Omega}{\sin \Omega} \cos \theta  \sin \theta  \cos \phi  u + \cos \lambda \Omega \sin \theta  u + \frac{\sin \lambda \Omega}{\sin \Omega} \cos^{2} \sin \phi  v$$
$$\theta  \theta$$
$$+ \frac{\sin \lambda \Omega}{\sin \Omega} \sin^{2} \sin \phi  v - \frac{\sin \lambda \Omega}{\sin \Omega} \sin^{2} \sin \phi (u \cdot  v)u.$$
Using
$$\sin \theta  \sin \phi (u \cdot  v) = \cos \Omega -\cos \theta  \cos \phi ,$$
we get
$$\nu  = - \frac{\sin \lambda \Omega}{\sin \Omega} \cos \theta  \sin \theta  \cos \phi  u + \cos \lambda \Omega \sin \theta  u + \frac{\sin \lambda \Omega}{\sin \Omega} \sin \phi  v$$
$$- \frac{\sin \lambda \Omega}{\sin \Omega} \sin \theta (\cos \Omega -\cos \theta  \cos \phi )u$$
$$= \cos \lambda \Omega \sin \theta  u + \frac{\sin \lambda \Omega}{\sin \Omega} \sin \phi  v - \frac{\sin \lambda \Omega}{\sin \Omega} \sin \theta  \cos \Omega u$$
$$-$$
$$= \frac{(\cos \lambda \Omega \sin \Omega \sin \lambda \Omega \cos \Omega )}{\sin \Omega} \sin \theta  u + \frac{\sin \lambda \Omega}{\sin \Omega} \sin \phi  v$$
$$-$$
$$= \frac{\sin(1\lambda )\Omega}{\sin \Omega} \sin \theta  u + \frac{\sin \lambda \Omega}{\sin \Omega} \sin \phi  v.$$
Putting the scalar part and the vector part together, we obtain
$$ -   - $$
$$q_{1}(q_{1}^{-1} q_{2})^{\lambda}= \frac{\sin(1\lambda )\Omega}{\sin \Omega} \cos \theta  + \frac{\sin \lambda \Omega}{\sin \Omega} \cos \phi , \frac{\sin(1\lambda )\Omega}{\sin \Omega} \sin \theta  u + \frac{\sin \lambda \Omega}{\sin \Omega} \sin \phi  v,$$
$$-$$
$$= \frac{\sin(1\lambda )\Omega}{\sin \Omega} [\cos \theta , \sin \theta  u] + \frac{\sin \lambda \Omega}{\sin \Omega} [\cos \phi , \sin \phi  v].$$
This yields the celebrated slerp interpolation formula
$$-$$
$$Z(\lambda ) = q_{1}(q_{1}^{-1} q_{2})^{\lambda}= \frac{\sin(1\lambda )\Omega}{\sin \Omega} q_{1} + \frac{\sin \lambda \Omega}{\sin \Omega} q_{2},$$
with
$$\cos \Omega = \cos \theta  \cos \phi  + \sin \theta  \sin \phi (u \cdot  v).$$

## 16.7 Nonexistence of a “Nice” Section from SO(3) to

$$SU(2)$$
We conclude by discussing the problem of a consistent choice of sign for the quaternion $q$ representing a rotation $R = \rho_{q}  \in$ SO(3). We are looking for a “nice” section $s$: SO(3) $\to$ SU(2), that is, a function $s$ satisfying the condition
$$\rho  \circ s = id,$$
where $\rho$  is the surjective homomorphism $\rho$ : SU(2) $\to$ SO(3).

<!-- PAGE 619 -->

> **Proposition 16.9.** Any section $s$: SO(3) $\to$ SU(2) of $\rho$  is neither a homomorphism nor continuous. Intuitively, this means that there is no “nice and simple ” way to pick the sign of the quaternion representing a rotation. The following proof is due to Marcel Berger.

*Proof.* Let $\Gamma$  be the subgroup of SU(2) consisting of all quaternions of the form $q = [a, (b, 0, 0)]$. Then, using the formula for the rotation matrix $R_{q}$ corresponding to $q$ (and the fact that $a^{2} + b^{2} = 1)$, we get
$$R_{q} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 2a^{2}-1 & -2ab \\ 0 & 2ab & 2a^{2} & 1 \end{pmatrix} .$$
$$-$$
Since $a^{2} + b^{2} = 1$, we may write $a =$ cos $\theta , b =$ sin $\theta$ , and we see that
$$R_{q} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos 2\theta & -\sin 2\theta \\ 0 & \sin 2\theta & \cos 2\theta \end{pmatrix} ,$$
a rotation of angle $2\theta$  around the x-axis. Thus, both $\Gamma$  and its image are isomorphic to SO(2), which is also isomorphic to U(1) $= {w \in \mathbb{C}$ | |w| $= 1}$. By identifying $i$ and $i$, and identifying $\Gamma$  and its image to U(1), if we write $w =$ cos $\theta  + i$ sin $\theta  \in \Gamma$ , the restriction of the map $\rho$  to $\Gamma$  is given by $\rho (w) = w^{2}$. We claim that any section $s$ of $\rho$  is not a homomorphism. Consider the restriction of $s$ to U(1). Then since $\rho  \circ s =$ id and $\rho (w) = w^{2}$, for $-1 \in \rho (\Gamma$ ) $\approx$ U(1), we have
$$-1 = \rho (s(-1)) = (s(-1))^{2}.$$
On the other hand, if $s$ is a homomorphism, then
$$(s(-1))^{2}= s((-1)^{2}) = s(1) = 1,$$
contradicting $(s(-1))^{2} = -1$. We also claim that $s$ is not continuous. Assume that s(1) $= 1$, the case where s(1) $= -1$ being analogous. Then $s$ is a bijection inverting $\rho$  on $\Gamma$  whose restriction to U(1) must be given by
$$s(\cos \theta  + i \sin \theta ) = \cos(\theta /2) + i \sin(\theta /2),-\pi  \le \theta  < \pi .$$
If $\theta$  tends to $\pi$ , that is $z =$ cos $\theta  +i$ sin $\theta$  tends to $-1$ in the upper-half plane, then s(z) tends to $i$, but if $\theta$  tends to $-\pi$ , that is $z$ tends to $-1$ in the lower-half plane, then s(z) tends to $-i$, which shows that $s$ is not continuous.
