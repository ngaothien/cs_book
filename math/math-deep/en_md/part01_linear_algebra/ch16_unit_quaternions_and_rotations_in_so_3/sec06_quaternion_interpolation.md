# Quaternion Interpolation


<!-- PAGE 616 -->
$$⊛$$

## 16.6 Quaternion Interpolation

We are now going to derive a formula for interpolating between two quaternions. This formula is due to Ken Shoemake, once a Penn student and my TA! Since rotations in SO(3) can be defined by quaternions, this has applications to computer graphics, robotics, and computer vision. First we observe that multiplication of quaternions can be expressed in terms of the inner product and the cross-product in $\mathbb{R}^{3}$. Indeed, if $q_{1} = [a, u_{1}]$ and $q_{2} = [a_{2}, u_{2}]$, it can be verified that
$$q_{1}q_{2} = [a_{1}, u_{1}][a_{2}, u_{2}] = [a_{1}a_{2} -u_{1} \cdot  u_{2}, a_{1}u_{2} + a_{2}u_{1} + u_{1} \times  u_{2}].(*_{mult})$$
We will also need the identity
$$u \times  (u \times  v) = (u \cdot  v)u -(u \cdot  u)v.$$
Given a quaternion $q$ expressed as $q =$ [cos $\theta$ , sin $\theta  u]$, where $u$ is a unit vector, we can interpolate between I and $q$ by finding the logs of I and $q$, interpolating in $\mathfrak{su}(2)$, and then exponentiating. We have
$$A = \log(I) = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} ,B = \log(q) = \theta \begin{pmatrix} iu_{1} & u_{2} + iu_{3} \\ -u_{2} + iu_{3} & -iu_{1} \end{pmatrix} ,$$
and so $q = e^{B}$. Since SU(2) is a compact Lie group and since the inner product on $\mathfrak{su}(2)$ given by
$$\langle X, Y \rangle = \mathrm{tr}(X^{\top}Y )$$
is Ad(SU(2))-invariant, it induces a biinvariant Riemannian metric on SU(2), and the curve
$$\lambda  \mapsto e^{\lambda B},\lambda  \in [0, 1]$$
is a geodesic from I to $q$ in SU(2). We write $q^{\lambda} = e^{\lambda B}$. Given two quaternions $q_{1}$ and $q_{2}$, because the metric is left invariant, the curve
$$\lambda  \mapsto Z(\lambda ) = q_{1}(q_{1}^{-1} q_{2})^{\lambda},\lambda  \in [0, 1]$$
is a geodesic from $q_{1}$ to $q_{2}$. Remarkably, there is a closed-form formula for the interpolant $Z(\lambda$ ). Say $q_{1} =$ [cos $\theta$ , sin $\theta  u]$ and $q_{2} =$ [cos $\phi$ , sin $\phi  v]$, and assume that $q_{1} \neq  q_{2}$ and $q_{1} \neq  -q_{2}$. First, we compute $q^{-1}q_{2}$. Since $q^{-1} =$ [cos $\theta$ , -sin $\theta  u]$, we have $q^{-1}q_{2} =$ [cos $\theta$  cos $\phi  +$ sin $\theta$  sin $\phi (u \cdot  v)$, -sin $\theta$  cos $\phi  u +$ cos $\theta$  sin $\phi  v$ - sin $\theta$  sin $\phi (u \times  v)]$. Define $\Omega$ by
$$\cos \Omega = \cos \theta  \cos \phi  + \sin \theta  \sin \phi (u \cdot  v).(*_{\Omega})$$

<!-- PAGE 617 -->
Since $q_{1} \neq  q_{2}$ and $q_{1} \neq  -q_{2}$, we have $0 < \Omega < \pi$ , so we get
$$(-\sin \theta  \cos \phi  u + \cos \theta  \sin \phi  v -\sin \theta  \sin \phi (u \times  v)$$
$$q_{1}^{-1} q_{2} =\cos \Omega , \sin \Omega ,$$
$$\sin \Omega$$
where the term multiplying sin $\Omega$ is a unit vector because $q_{1}$ and $q_{2}$ are unit quaternions, so $q_{1}^{-1} q_{2}$ is also a unit quaternion. By $(*_{log})$, we have
$$(-\sin \theta  \cos \phi  u + \cos \theta  \sin \phi  v -\sin \theta  \sin \phi (u \times  v)$$
$$(q_{1}^{-1} q_{2})^{\lambda}=\cos \lambda \Omega , \sin \lambda \Omega .$$
$$\sin \Omega$$
Next we need to compute $q_{1}(q_{1}^{-1} q_{2})^{\lambda}$. The scalar part of this product is
$$\theta$$
$$s = \cos \theta  \cos \lambda \Omega + \frac{\sin \lambda \Omega}{\sin \Omega} \sin^{2} \cos \phi (u \cdot  u) - \frac{\sin \lambda \Omega}{\sin \Omega} \sin \theta  \sin \phi  \cos \theta (u \cdot  v)$$
$$\theta$$
$$+ \frac{\sin \lambda \Omega}{\sin \Omega} \sin^{2} \sin \phi (u \cdot  (u \times  v)).$$
Since $u \cdot  (u \times  v) = 0$, the last term is zero, and since $u \cdot  u = 1$ and
$$\sin \theta  \sin \phi (u \cdot  v) = \cos \Omega -\cos \theta  \cos \phi ,$$
we get
$$\theta$$
$$s = \cos \theta  \cos \lambda \Omega + \frac{\sin \lambda \Omega}{\sin \Omega} \sin^{2} \cos \phi  - \frac{\sin \lambda \Omega}{\sin \Omega} \cos \theta (\cos \Omega -\cos \theta  \cos \phi )$$
$$\theta  \theta$$
$$= \cos \theta  \cos \lambda \Omega + \frac{\sin \lambda \Omega}{\sin \Omega} (\sin^{2} + \cos^{2}) \cos \phi  - \frac{\sin \lambda \Omega}{\sin \Omega} \cos \theta  \cos \Omega$$
$$-$$
$$= \frac{(\cos \lambda \Omega \sin \Omega \sin \lambda \Omega \cos \Omega ) \cos \theta}{\sin \Omega} + \frac{\sin \lambda \Omega}{\sin \Omega} \cos \phi$$
$$-$$
$$= \frac{\sin(1\lambda )\Omega}{\sin \Omega} \cos \theta  + \frac{\sin \lambda \Omega}{\sin \Omega} \cos \phi .$$
The vector part of the product $q_{1}(q_{1}^{-1} q_{2})^{\lambda}$ is given by
$$\theta$$
$$\nu  = - \frac{\sin \lambda \Omega}{\sin \Omega} \cos \theta  \sin \theta  \cos \phi  u + \frac{\sin \lambda \Omega}{\sin \Omega} \cos^{2} \sin \phi  v - \frac{\sin \lambda \Omega}{\sin \Omega} \cos \theta  \sin \theta  \sin \phi (u \times  v)$$
$$\theta$$
$$+ \cos \lambda \Omega \sin \theta  u - \frac{\sin \lambda \Omega}{\sin \Omega} \sin^{2} \cos \phi (u \times  u) + \frac{\sin \lambda \Omega}{\sin \Omega} \cos \theta  \sin \theta  \sin \phi (u \times  v)$$
$$\theta$$
$$- \frac{\sin \lambda \Omega}{\sin \Omega} \sin^{2} \sin \phi (u \times  (u \times  v)).$$
We have $u \times  u = 0$, the two terms involving $u \times  v$ cancel out,
$$u \times  (u \times  v) = (u \cdot  v)u -(u \cdot  u)v,$$
