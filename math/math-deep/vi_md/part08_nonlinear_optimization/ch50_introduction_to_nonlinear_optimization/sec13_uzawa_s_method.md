# Uzawa's Phương pháp


<!-- PAGE 1847 -->

## 50.13 Uzawa’s Phương pháp

Cho chúng ta đi quay lại đến của ta Cực tiểu hóa Bài toán
$$minimizeJ(v)$$
$$subject to \phi_{i} (v) \le 0,i = 1, \dots  , m,$$
Ở đâu các hàm $J$ và $\phi_{i}$ được định nghĩa trên một số mở tập con $\Omega$ của hữu hạn chiều Euclidean không gian vectơ (vector space) $V$ (tổng quát hơn, thực Không gian Hilbert (Hilbert space) $V$). Như thông thường, cho
$$U = {v \in V | \phi_{i} (v) \le 0, 1 \le i \le m}.$$
Nếu phiếm hàm $J$ thỏa mãn các bất đẳng thức của Mệnh đề 49.18 và nếu các hàm $\phi_{i}$ là lồi, trong lý thuyết, projected-gradient phương pháp hội tụ đến duy nhất điểm cực tiểu hóa của $J$ trên $U$. Không may là, nó là thường không thể để tính phép chiếu ánh xạ $p_{U}$: $V \to U$. Mặt khác, miền xác định của Lagrange đối ngẫu (dual) hàm $G: \mathbb{R}_{+}^{m} \to \mathbb{R}$ cho trước bởi
$$G(\mu ) = infL(v, \mu )\mu  \in \mathbb{R}_{+}^{m},$$
$$v\in \Omega$$
Là $\mathbb{R}_{+}^{m}$, ở đâu
$$L(v, \mu ) = J(v) + \sum_{i=1}^{m}  \mu_{i} \phi_{i} (v)$$
$$\mathbb{R}^{m}  \mathbb{R}_{+}^{m}$$
Là Hàm Lagrange (Lagrangian) của bài toán của chúng ta. Bây giờ phép chiếu $p_{+}$ từ đến là rất đơn giản, cụ thể là
$$(p_{+}(\lambda ))_{i} = \max{\lambda_{i} , 0},1 \le i \le m.$$
Suy ra rằng projection-gradient phương pháp nên là applicable đến Bài toán đối ngẫu (dual problem) $(D)$:
$$maximizeG(\mu )$$
$$subject to \mu  \in \mathbb{R}_{+}^{m}.$$
Nếu các giả thiết của Định lý 50.17 đúng, thì nghiệm $\lambda$ của Đối ngẫu (dual) Bài toán quy hoạch $(D)$ cho ta nghiệm $u_{\lambda}$ của bài toán gốc (primal problem). Uzawa’s phương pháp là về cơ bản gradien phương pháp với cố định bước nhảy (stepsize) ứng dụng đến Bài toán đối ngẫu (dual problem) $(D)$. Tuy nhiên, nó là designed đến cho nghiệm của bài toán gốc (primal problem). Uzawa’s phương pháp:
$$\mathbb{R}_{+}^{m}$$
Cho trước tùy ý ban đầu vectơ $\lambda^{0} \in$, hai các dãy $(\lambda^{k} )_{k\ge0}$ và $(u^{k})_{k\ge0}$ là con-
$$\mathbb{R}_{+}^{m}$$
Structed, với $\lambda^{k} \in$ và $u^{k} \in V$. Giả sử rằng $\lambda^{0} , \lambda^{1} , \dots  , \lambda^{k}$ là đã biết, $u^{k}$ và $\lambda^{k+1}$ được xác định như sau:

<!-- PAGE 1848 -->
$u^{k}$ là duy nhất nghiệm của cực tiểu hóa bài toán, tìm $u^{k} \in V$ sao cho
$$J(u^{k}) + \sum_{i=1}^{m}  \lambda_{i}^{k}  \phi_{i} (u^{k}) = \inf \sum_{i=1}^{m}  ; and$$
$$(UZ)v\in V \begin{pmatrix} J(v) + & \lambda_{i}^{k} \phi_{i} (v) \end{pmatrix}$$
$$\lambda_{i}^{k+1} = \max{\lambda_{i}^{k}  + \rho \phi_{i} (u^{k}), 0},1 \le i \le m,$$
$$$$
Ở đâu $\rho  > 0$ là suitably được chọn tham số. Nhắc lại rằng trong chứng minh của Định lý 50.17 ta đã chỉ ra $(*_{deriv})$, cụ thể là
$$G_{\lambda k}'(\xi ) = \langle \nabla G_{\lambda k}, \xi \rangle = \sum_{i=1}^{m}  \xi_{i} \phi_{i} (u^{k}),$$
Mà có nghĩa là $(\nabla G_{\lambda k})_{i} = \phi_{i} (u^{k})$. Thì phương trình thứ hai trong (UZ) tương ứng với gradient-projection bước
$$\lambda^{k+1} = p_{+}(\lambda^{k} + \rho \nabla G_{\lambda k}).$$
Lưu ý rằng bởi vì bài toán là cực đại hóa bài toán ta sử dụng dương dấu thay vì của âm dấu. Uzawa’s phương pháp là thật vậy gradien phương pháp. Basically, Uzawa’s phương pháp thay thế có ràng buộc tối ưu hóa bài toán bởi dãy của không ràng buộc tối ưu hóa các bài tập liên quan đến Hàm Lagrange (Lagrangian) của (gốc (primal)) bài toán. một cách thú vị, dưới nhất định các giả thiết, nó là khả dĩ/có thể để chứng minh rằng dãy của xấp xỉ các nghiệm $(u^{k})_{k\ge0}$ hội tụ đến điểm cực tiểu hóa $u$ của $J$ trên $U$, chẵn/ngay cả nếu dãy $(\lambda^{k} )_{k\ge0}$ thực hiện không hội tụ. Ta chứng minh như vậy kết quả khi các ràng buộc $\phi_{i}$ là afin.
$$\mathbb{R}^{n} \mathbb{R}$$

> **Định lý 50.21.** Giả sử $J$: $\to$ là elliptic phiếm hàm, mà có nghĩa là $J$ là một cách liên tục khả vi (differentiable) trên $\mathbb{R}^{n}$, và tồn tại một hằng số $\alpha  > 0$ sao cho
$$\langle \nabla J_{v} -\nabla J_{u}, v -u\rangle \ge \alpha  \|v -u\|^{2}for all u, v \in \mathbb{R}^{n},$$
Và rằng $U$ là khác rỗng đóng lồi tập con cho trước bởi
$$\mathbb{R}^{n}$$
$$U = {v \in | Cv \le d},$$
Ở đâu $C$ là thực $m \times  n$ ma trận và $d \in \mathbb{R}^{m}$. Nếu vô hướng (scalar) $\rho$ thỏa mãn điều kiện
$$0 < \rho  < \frac{2\alpha}{\|C\|_{2}^{2}} ,$$
Ở đâu $\|C\|_{2}$ là spectral chuẩn (norm) của $C$, thì dãy $(u^{k})_{k\ge0}$ được tính bởi Uzawa’s phương pháp hội tụ đến duy nhất điểm cực tiểu hóa $u \in U$ của $J$. Hơn nữa, nếu $C$ có hạng (rank) $m$, thì dãy $(\lambda^{k} )_{k\ge0}$ hội tụ đến duy nhất maximizer của Bài toán đối ngẫu (dual problem) $(D)$.

<!-- PAGE 1849 -->

*Chứng minh.* Bước $1$. Ta thiết lập đại số các điều kiện relating duy nhất điểm cực tiểu hóa $u \in U$ của $J$ trên $U$ và một số $\lambda  \in \mathbb{R}_{+}^{m}$ sao cho $(u, \lambda$) là điểm yên ngựa (saddle point). Vì $J$ là elliptic và $U$ là khác rỗng đóng và lồi, theo Định lý 49.8, phiếm hàm $J$ là lồi chặt (strictly convex), do đó nó có duy nhất điểm cực tiểu hóa $u \in U$. Vì $J$ là lồi và các ràng buộc là afin, theo Định lý 50.17(2) Bài toán đối ngẫu (dual problem) $(D)$ có ít nhất một nghiệm. Theo Định lý 50.15(2), tồn tại một $\lambda  \in \mathbb{R}_{+}^{m}$ sao cho $(u, \lambda$) là điểm yên ngựa (saddle point) của Hàm Lagrange (Lagrangian) $L$. Nếu ta định nghĩa afin hàm $\phi$ bởi
$$\phi (v) = (\phi_{1} (v), \dots  , \phi_{m} (v)) = Cv -d,$$
Thì Hàm Lagrange (Lagrangian) L(v, $\mu$) có thể được viết dưới dạng
$$L(v, \mu ) = J(v) + \sum_{i=1}^{m}  \mu_{i} \phi_{i} (v) = J(v) + \langle C^{\top}\mu , v\rangle -\langle \mu , d\rangle .$$
Vì
$$L(u, \lambda ) = \inf L(v, \lambda ),$$
$$v\in \mathbb{R} n$$
Theo Định lý 40.13(4) ta phải có
$$\nabla J_{u} + C^{\top}\lambda  = 0,(*_{1})$$
Và vì
$$G(\lambda ) = L(u, \lambda ) = supL(u, \mu ),$$
$$\mu \in \mathbb{R} m$$
$$+$$
Theo Định lý 40.13(3) (và vì maximing hàm $g$ là tương đương đến cực tiểu hóa $-g)$, ta phải có
$$G_{\lambda}'(\mu  -\lambda ) \le 0for all \mu  \in \mathbb{R}_{+}^{m},$$
Và vì như được lưu ý trước đó $\nabla G_{\lambda} = \phi (u)$, ta thu được
$$\langle \phi (u), \mu  -\lambda \rangle \le 0for all \mu  \in \mathbb{R}_{+}^{m}.(*_{2})$$
Như trong chứng minh của Mệnh đề 49.18, $(*_{2})$ có thể được biểu diễn dưới dạng suy ra với mọi $\rho  > 0$:
$$\langle \lambda  -(\lambda  + \rho \phi (u)), \mu  -\lambda \rangle \ge 0for all \mu  \in \mathbb{R}_{+}^{m},(**_{2})$$
Mà chỉ ra rằng $\lambda$ có thể được được quan điểm như phép chiếu lên $\mathbb{R}_{+}^{m}$ của vectơ $\lambda  + \rho \phi (u)$. Trong tóm tắt ta thu được các phương trình
$$(\nabla$$
$$J_{u} + C^{\top}\lambda  = 0$$
$$(\dagger_{1} )$$
$$\lambda  = p_{+}(\lambda  + \rho \phi (u)).$$

<!-- PAGE 1850 -->
Bước $2$. Ta thiết lập đại số các điều kiện relating duy nhất nghiệm $u_{k}$ của cực tiểu hóa bài toán phát sinh during vòng lặp của Uzawa’s phương pháp trong (UZ) và $\lambda^{k}$. Nhận thấy rằng Hàm Lagrange (Lagrangian) L(v, $\mu$) là lồi chặt (strictly convex) như hàm của $v$ (như tổng của chặt hàm lồi (convex function) và afin hàm). Như trong chứng minh của Định lý 49.8(1) và bằng cách sử dụng Cauchy–Schwarz, ta có
$$+$$
$$J(v) + \langle C^{\top}\mu , v\rangle \ge J(0) + \langle \nabla J_{0}, v\rangle + \frac{\alpha}{2} \|v\|^{2} \langle C^{\top}\mu , v$$
$$,$$
$$\ge J(0) -\|\nabla J_{0}\|\|v\|-

$C^{\top}\mu$

$\|v\|+ \frac{\alpha \rangle}{2} \|v\|^{2}$$$ and the term $(-\|\nabla J_{0}\|-$

$C^{\top}\mu$

$\|v\| +_{2}^{\alpha}  \|v\|) \|v\|$ đi đến $+\infty$ khi $\|v\|$ tiến tới đến $+\infty$, do đó L(v, $\mu$) là bức (coercive) như hàm của $v$. Vì vậy, cực tiểu hóa bài toán tìm $u^{k}$ sao cho
$$J(u^{k}) + \sum_{i=1}^{m}  \lambda_{i}^{k}  \phi_{i} (u^{k}) = vinf\in \mathbb{R} n \begin{pmatrix} J(v) + & \lambda_{i}^{k} \phi_{i} (v) \end{pmatrix} \sum_{i=1}^{m}$$
$$\mathbb{R}^{n}$$
Có duy nhất nghiệm $u^{k} \in$. Suy ra từ Định lý 40.13(4) rằng vectơ $u^{k}$ phải thỏa mãn phương trình
$$\nabla J_{uk} + C^{\top}\lambda^{k} = 0,(*_{3})$$
Và vì theo định nghĩa của Uzawa’s phương pháp
$$\lambda^{k+1} = p_{+}(\lambda^{k} + \rho \phi (u^{k})),(*_{4})$$
Ta thu được các phương trình
$$($$
$$\nabla J_{uk} + C^{\top}\lambda^{k} = 0$$
$$(\dagger_{2} )$$
$$\lambda^{k+1} = p_{+}(\lambda^{k} + \rho \phi (u^{k})).$$
Bước $3$. Bằng cách trừ thứ nhất của hai các phương trình của $(\dagger_{1}$) và $(\dagger_{2}$) ta thu được
$$\nabla J_{uk} -\nabla J_{u} + C^{\top}(\lambda^{k} -\lambda ) = 0,$$
Và bằng cách trừ thứ hai của hai các phương trình của $(\dagger_{1}$) và $(\dagger_{2}$) và bằng cách sử dụng Mệnh đề 48.6, ta thu được
$$-

$\le$

- -

.$$
$$\lambda^{k+1} \lambda \lambda^{k} \lambda  + \rho C(u^{k}u)$$
Trong tóm tắt, ta được chứng minh
$$($$
$$\nabla J_{uk} -\nabla J_{u} + C^{\top}(\lambda^{k} -\lambda ) = 0$$
$$(\dagger )$$
$$-

$\le$

- -

.$$
$$\lambda^{k+1} \lambda \lambda^{k} \lambda  + \rho C(u^{k}u)$$
Bước $4$. Sự hội tụ của dãy $(u^{k})_{k\ge0}$ đến $u$.

<!-- PAGE 1851 -->
Squaring cả hai vế của bất đẳng thức trong $(\dagger$) ta thu được
$$-  - + 2 - - .$$
$$\lambda^{k+1} \lambda^{2}

$\le$

$\lambda^{k} \lambda^{2}$

$\rho \langle C^{\top}(\lambda^{k} \lambda$), $u_{k} -u\rangle + \rho^{2}$

$C(u^{k}u)^{2}$$$ Using the equation in $(\dagger$) và bất đẳng thức
$$- ,$$
$$\langle \nabla J_{uk} -\nabla J_{u}, u^{k}-u\rangle \ge \alpha

$u^{k}u^{2}$$$ ta thu được
$$-  - - - -$$
$$\lambda^{k+1} \lambda^{2}

$\le$

$\lambda^{k} \lambda^{2}$

$2\rho \langle \nabla J_{uk} -\nabla J_{u}, u^{k}u\rangle + \rho^{2}$

$C(u^{k}u)^{2}$$$
$$- - - .$$
$$\le

$\lambda^{k} \lambda^{2}$

$\rho (2\alpha  -\rho  \|C\|_{2}^{2})$

$u^{k}u^{2}$$$ Hệ quả là, nếu
$$0 \le \rho  \le \frac{2\alpha}{\|C\|_{2}^{2}} ,$$
Ta có
$$-

$\le$

-

,$$
$$\lambda^{k+1} \lambda \lambda^{k} \lambda for all k \ge 0.(*_{5})$$
$$-$$
Bởi $(*_{5})$, dãy ($\lambda^{k} \lambda )_{k\ge0}$ là nonincreasing và bị chặn ở dưới bởi $0$, do đó nó hội tụ, mà suy ra rằng
$$

-

-

-$$
$$lim\lambda^{k+1} \lambda \lambda^{k} \lambda = 0,$$
$$k\mapsto \infty$$
Và vì
$$-  - - - ,$$
$$\lambda^{k+1} \lambda^{2}

$\le$

$\lambda^{k} \lambda^{2}$

$\rho (2\alpha  -\rho  \|C\|_{2}^{2})$

$u^{k}u^{2}$$$ ta cũng có
$$-  - - - .$$
$$\rho (2\alpha  -\rho  \|C\|_{2}^{2})

$u^{k}u^{2}$

$\le$

$\lambda^{k} \lambda^{2}$



$\lambda^{k+1} \lambda^{2}$$$ Do đó nếu
$$0 < \rho  < \frac{2\alpha}{\|C\|_{2}^{2}} ,$$
Thì $\rho (2\alpha$ - $\rho  \|C\|_{2}^{2}) > 0$, và ta kết luận rằng
$$-

$=$ 0$$
$$limu^{k}u,$$
$$k\mapsto \infty$$
Rằng là, dãy $(u^{k})_{k\ge0}$ hội tụ đến $u$. Bước $5$. Sự hội tụ của dãy $(\lambda^{k} )_{k\ge0}$ đến $\lambda$ nếu $C$ có hạng (rank) $m$.
$$-$$
Vì dãy ($\lambda^{k} \lambda )_{k\ge0}$ là nonincreasing, dãy $(\lambda^{k} )_{k\ge0}$ là bị chặn, và
$$\mathbb{R}_{+}^{m}$$
Do đó nó có convergent dãy con $(\lambda^{i(k)} )_{i\ge0}$ có giới hạn là một số $\lambda' \in$. Vì J' là liên tục, bởi $(\dagger_{2}$) ta có
$$\nabla J_{u} + C^{\top}\lambda' = lim(\nabla J_{ui(k)} + C^{\top}\lambda^{i(k)} ) = 0.(*_{6})$$
$$i\mapsto \infty$$
Nếu $C$ có hạng (rank) $m$, thì Im(C) $= \mathbb{R}^{m}$, mà là tương đương đến Ker $(C^{\top}) = (0)$, do đó $C^{\top}$ là đơn ánh (injective) và vì bởi $(\dagger_{1}$) ta cũng có $\nabla J_{u} +C^{\top}\lambda  = 0$, ta kết luận rằng $\lambda' = \lambda$. ở trên lập luận áp dụng đến bất kỳ dãy con của $(\lambda^{k} )_{k\ge0}$, do đó $(\lambda^{k} )_{k\ge0}$ hội tụ đến $\lambda$.
