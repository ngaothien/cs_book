# Quaternion Nội suy


<!-- PAGE 616 -->
$$⊛$$

## 16.6 Quaternion Nội suy

Ta là bây giờ đi đến derive công thức cho interpolating giữa hai các quaternion. công thức này là do Ken Shoemake, một lần Penn student và my TA! Vì các phép quay trong Do đó(3) có thể được được định nghĩa bởi các quaternion, điều này có các ứng dụng đến máy tính đồ họa, rô-bốt học, và máy tính thị giác. Thứ nhất ta nhận thấy rằng phép nhân của các quaternion có thể được được biểu diễn theo tích vô hướng (inner product) và cross-product trong $\mathbb{R}^{3}$. Thật vậy, nếu $q_{1} = [a, u_{1}]$ và $q_{2} = [a_{2}, u_{2}]$, nó có thể được được kiểm chứng rằng
$$q_{1}q_{2} = [a_{1}, u_{1}][a_{2}, u_{2}] = [a_{1}a_{2} -u_{1} \cdot  u_{2}, a_{1}u_{2} + a_{2}u_{1} + u_{1} \times  u_{2}].(*_{mult})$$
Ta sẽ cũng cần đồng nhất thức
$$u \times  (u \times  v) = (u \cdot  v)u -(u \cdot  u)v.$$
Cho trước quaternion $q$ được biểu diễn như $q =$ [cos $\theta$, sin $\theta  u]$, ở đâu $u$ là unit vectơ, ta có thể interpolate giữa I và $q$ bởi việc tìm logs của I và $q$, interpolating trong $\mathfrak{su}(2)$, và thì exponentiating. Ta có
$$A = \log(I) = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} ,B = \log(q) = \theta \begin{pmatrix} iu_{1} & u_{2} + iu_{3} \\ -u_{2} + iu_{3} & -iu_{1} \end{pmatrix} ,$$
Và do đó $q = e^{B}$. Vì SU(2) là compắc Lie nhóm và vì tích vô hướng (inner product) trên $\mathfrak{su}(2)$ cho trước bởi
$$\langle X, Y \rangle = \mathrm{tr}(X^{\top}Y )$$
Là Ad(SU(2))-bất biến, nó cảm sinh biinvariant Riemannian mêtric trên SU(2), và đường cong
$$\lambda  \mapsto e^{\lambda B},\lambda  \in [0, 1]$$
Là geodesic từ I đến $q$ trong SU(2). Ta viết $q^{\lambda} = e^{\lambda B}$. Cho trước hai các quaternion $q_{1}$ và $q_{2}$, bởi vì mêtric là trái bất biến, đường cong
$$\lambda  \mapsto Z(\lambda ) = q_{1}(q_{1}^{-1} q_{2})^{\lambda},\lambda  \in [0, 1]$$
Là geodesic từ $q_{1}$ đến $q_{2}$. Đáng chú ý, có một closed-form công thức cho interpolant $Z(\lambda$). Nói $q_{1} =$ [cos $\theta$, sin $\theta  u]$ và $q_{2} =$ [cos $\phi$, sin $\phi  v]$, và giả sử rằng $q_{1} \neq  q_{2}$ và $q_{1} \neq  -q_{2}$. Thứ nhất, ta tính $q^{-1}q_{2}$. Vì $q^{-1} =$ [cos $\theta$, -sin $\theta  u]$, ta có $q^{-1}q_{2} =$ [cos $\theta$ cos $\phi  +$ sin $\theta$ sin $\phi (u \cdot  v)$, -sin $\theta$ cos $\phi  u +$ cos $\theta$ sin $\phi  v$ - sin $\theta$ sin $\phi (u \times  v)]$. Định nghĩa $\Omega$ bởi
$$\cos \Omega = \cos \theta  \cos \phi  + \sin \theta  \sin \phi (u \cdot  v).(*_{\Omega})$$

<!-- PAGE 617 -->
Vì $q_{1} \neq  q_{2}$ và $q_{1} \neq  -q_{2}$, ta có $0 < \Omega < \pi$, do đó ta thu được
$$(-\sin \theta  \cos \phi  u + \cos \theta  \sin \phi  v -\sin \theta  \sin \phi (u \times  v)$$
$$q_{1}^{-1} q_{2} =\cos \Omega , \sin \Omega ,$$
$$\sin \Omega$$
Ở đâu số hạng nhân sin $\Omega$ là unit vectơ bởi vì $q_{1}$ và $q_{2}$ là các quaternion đơn vị, do đó $q_{1}^{-1} q_{2}$ là cũng quaternion đơn vị (unit quaternion). Bởi $(*_{log})$, ta có
$$(-\sin \theta  \cos \phi  u + \cos \theta  \sin \phi  v -\sin \theta  \sin \phi (u \times  v)$$
$$(q_{1}^{-1} q_{2})^{\lambda}=\cos \lambda \Omega , \sin \lambda \Omega .$$
$$\sin \Omega$$
Tiếp theo ta cần để tính $q_{1}(q_{1}^{-1} q_{2})^{\lambda}$. vô hướng (scalar) phần của tích này là
$$\theta$$
$$s = \cos \theta  \cos \lambda \Omega + \frac{\sin \lambda \Omega}{\sin \Omega} \sin^{2} \cos \phi (u \cdot  u) - \frac{\sin \lambda \Omega}{\sin \Omega} \sin \theta  \sin \phi  \cos \theta (u \cdot  v)$$
$$\theta$$
$$+ \frac{\sin \lambda \Omega}{\sin \Omega} \sin^{2} \sin \phi (u \cdot  (u \times  v)).$$
Vì $u \cdot  (u \times  v) = 0$, số hạng cuối cùng là không, và vì $u \cdot  u = 1$ và
$$\sin \theta  \sin \phi (u \cdot  v) = \cos \Omega -\cos \theta  \cos \phi ,$$
Ta thu được
$$\theta$$
$$s = \cos \theta  \cos \lambda \Omega + \frac{\sin \lambda \Omega}{\sin \Omega} \sin^{2} \cos \phi  - \frac{\sin \lambda \Omega}{\sin \Omega} \cos \theta (\cos \Omega -\cos \theta  \cos \phi )$$
$$\theta  \theta$$
$$= \cos \theta  \cos \lambda \Omega + \frac{\sin \lambda \Omega}{\sin \Omega} (\sin^{2} + \cos^{2}) \cos \phi  - \frac{\sin \lambda \Omega}{\sin \Omega} \cos \theta  \cos \Omega$$
$$-$$
$$= \frac{(\cos \lambda \Omega \sin \Omega \sin \lambda \Omega \cos \Omega ) \cos \theta}{\sin \Omega} + \frac{\sin \lambda \Omega}{\sin \Omega} \cos \phi$$
$$-$$
$$= \frac{\sin(1\lambda )\Omega}{\sin \Omega} \cos \theta  + \frac{\sin \lambda \Omega}{\sin \Omega} \cos \phi .$$
Vectơ phần của tích $q_{1}(q_{1}^{-1} q_{2})^{\lambda}$ được cho bởi
$$\theta$$
$$\nu  = - \frac{\sin \lambda \Omega}{\sin \Omega} \cos \theta  \sin \theta  \cos \phi  u + \frac{\sin \lambda \Omega}{\sin \Omega} \cos^{2} \sin \phi  v - \frac{\sin \lambda \Omega}{\sin \Omega} \cos \theta  \sin \theta  \sin \phi (u \times  v)$$
$$\theta$$
$$+ \cos \lambda \Omega \sin \theta  u - \frac{\sin \lambda \Omega}{\sin \Omega} \sin^{2} \cos \phi (u \times  u) + \frac{\sin \lambda \Omega}{\sin \Omega} \cos \theta  \sin \theta  \sin \phi (u \times  v)$$
$$\theta$$
$$- \frac{\sin \lambda \Omega}{\sin \Omega} \sin^{2} \sin \phi (u \times  (u \times  v)).$$
Ta có $u \times  u = 0$, hai các số hạng liên quan đến $u \times  v$ cancel ra,
$$u \times  (u \times  v) = (u \cdot  v)u -(u \cdot  u)v,$$
