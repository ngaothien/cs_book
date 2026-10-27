# Đối ngẫu (dual) của Lề cứng (hard margin) Máy vectơ hỗ trợ (SVM)


<!-- PAGE 1828 -->
$(2)$ Giả sử Bài toán (P') có một số nghiệm $u \in U$, và rằng $\Omega$ là lồi (mở), các hàm $\phi_{i}  (1 \le i \le m)$ và $J$ là lồi, khả vi (differentiable) tại $u$, và rằng các ràng buộc là qualified. Thì Bài toán (D') có nghiệm $(\lambda , \eta$) $\in \mathbb{R}_{+}^{m} \times \mathbb{R}^{p}$, và J(u) $= G(\lambda , \eta$); rằng là, khoảng cách đối ngẫu (duality gap) là không. Trong mục tiếp theo ta derive đối ngẫu (dual) hàm và đối ngẫu (dual) bài toán quy hoạch của tối ưu hóa bài toán của Mục 50.6 (Lề cứng (hard margin) SVM), mà liên quan đến cả hai bất đẳng thức và đẳng thức các ràng buộc. Ta cũng derive KKT các điều kiện liên kết với đối ngẫu (dual) bài toán quy hoạch.

## 50.10 Đối ngẫu (dual) của Lề cứng (hard margin) Hỗ trợ/giá (support) Vectơ Ma-

$$chine$$
Nhắc lại Lề cứng (hard margin) SVM bài toán $(SVM_{h2})$:
$$,\mathbb{R}^{n}$$
$$minimize \frac{1}{2} \|w\|^{2}w \in$$
$$subject to$$
$$w^{\top}u_{i} -b \ge 1i = 1, \dots  , p$$
$$-w^{\top}v_{j} + b \ge 1j = 1, \dots  , q.$$
Ta tiến hành trong sáu các bước. Bước $1$: Viết các ràng buộc trong ma trận tạo thành. bất đẳng thức các ràng buộc được viết như
$$C \begin{pmatrix} w \\ b \end{pmatrix} \le d,$$
$$\mathbb{R}^{p+q}$$
Ở đâu $C$ là một ma trận cỡ $(p + q) \times  (n + 1)$ $C$ và $d \in$ là vectơ cho trước bởi
$$C = \begin{pmatrix} -u_{1}^{\top} & 1 \\ \vdots & \vdots \\ -u_{p}^{\top} & 1 \\ v_{1}^{\top} & -1 \\ \vdots & \vdots \\ v_{q}^{\top} & 1 \end{pmatrix} ,d = \begin{pmatrix} -1 \\ \vdots \\ -1 \end{pmatrix} = -1_{p+q}.$$
$$-$$
Nếu ta cho $X$ là ma trận cỡ $n \times  (p + q)$ cho trước bởi
$$X = \begin{pmatrix} -u_{1} & \cdots & -u_{p} & v_{1} & \cdots & v_{q} \end{pmatrix} ,$$

<!-- PAGE 1829 -->
Thì
$$C = \begin{pmatrix} 1_{p} \\ X^{\top}-1_{q} \end{pmatrix}$$
Và do đó
$$C^{\top}= \begin{pmatrix} X \\ 1_{p}^{\top} & -1_{q}^{\top} \end{pmatrix} .$$
Bước $2$: Viết hàm mục tiêu (objective function) trong ma trận tạo thành. hàm mục tiêu (objective function) được cho bởi
$$J(w, b) = \frac{1}{2} \begin{pmatrix} I_{n} & 0_{n} \\ 0_{n}^{\top} & 0 \end{pmatrix} \begin{pmatrix} w \\ b \end{pmatrix} .$$
$$\begin{pmatrix} w^{\top} & b \end{pmatrix}$$
Lưu ý rằng tương ứng ma trận là đối xứng nửa xác định dương (positive semidefinite), nhưng nó là không khả nghịch. Do đó hàm $J$ là lồi nhưng không lồi chặt (strictly convex). Bước $3$: Viết Hàm Lagrange (Lagrangian) trong ma trận tạo thành. Như trong Ví dụ 50.7, ta thu được Hàm Lagrange (Lagrangian)
$$L(w, b, \lambda , \mu ) = \frac{1}{2} \begin{pmatrix} w^{\top} & b \end{pmatrix} \begin{pmatrix} I_{n} & 0_{n} \\ 0_{n}^{\top} & 0 \end{pmatrix} \begin{pmatrix} w \\ b \end{pmatrix} - \begin{pmatrix} w^{\top} & b \end{pmatrix} \begin{pmatrix} \lambda \\ 0_{n+1} -C^{\top} & \mu \end{pmatrix} \begin{pmatrix}\end{pmatrix} + \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q},$$
Rằng là,
$$L(w, b, \lambda , \mu ) = \frac{1}{2} \begin{pmatrix} I_{n} & 0_{n} \\ 0_{n}^{\top} & 0 \end{pmatrix} \begin{pmatrix} w \\ b \end{pmatrix} + \begin{pmatrix} \lambda \\ X & \mu \\ 1_{p}^{\top}\lambda \end{pmatrix} \begin{pmatrix} 1_{q}^{\top}\mu \end{pmatrix} +1_{p+q}.$$
$$\begin{pmatrix} w^{\top} & b \end{pmatrix} \begin{pmatrix} w^{\top} & b \end{pmatrix} - \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix}$$
Bước $4$: Tìm đối ngẫu (dual) hàm $G(\lambda , \mu$). Trong thứ tự để tìm đối ngẫu (dual) hàm $G(\lambda , \mu$), ta cần để cực tiểu hóa L(w, $b, \lambda , \mu$) với đối với
$$\mathbb{R}^{n+1}$$
Đến $w$ và $b$ và cho điều này, vì hàm mục tiêu (objective function) $J$ là lồi và vì là lồi và mở, ta có thể áp dụng Định lý 40.13, mà cho cần và đủ điều kiện cho cực tiểu. gradien của L(w, $b, \lambda , \mu$) đối với $w$ và $b$ là
$$\nabla L_{w,b} = \begin{pmatrix} I_{n} & 0_{n} \\ 0_{n}^{\top} & 0 \end{pmatrix} \begin{pmatrix} w \\ b \end{pmatrix} + \begin{pmatrix} \lambda \\ X & \mu \\ 1_{p}^{\top}\lambda \end{pmatrix} \begin{pmatrix} 1_{q}^{\top}\mu \end{pmatrix}$$
$$-$$
$$= \begin{pmatrix} w \\ 0 \end{pmatrix} + \begin{pmatrix} \lambda \\ X & \mu \\ 1_{p}^{\top}\lambda \end{pmatrix} \begin{pmatrix} 1_{q}^{\top}\mu \end{pmatrix} .$$
$$-$$
Cần và đủ điều kiện cho cực tiểu là
$$\nabla L_{w,b} = 0,$$

<!-- PAGE 1830 -->
Mà cho ta
$$w = -X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} (*_{1})$$
Và
$$1_{p}^{\top} \lambda  -1_{q}^{\top} \mu  = 0.(*_{2})$$
Phương trình thứ hai có thể được viết dưới dạng
$$\sum_{i=1}^{p}  \lambda_{i}  = \sum_{j=1}^{q}  \mu_{j} .(*_{3})$$
Plugging quay lại $w$ từ $(*_{1})$ vào Hàm Lagrange (Lagrangian) và bằng cách sử dụng $(*_{2})$ ta thu được
$$G(\lambda , \mu ) = - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q};(*_{4})$$
$$of course, \begin{pmatrix} \lambda^{\top} & \mu^{\top} \\ onthe \end{pmatrix} 1_{p+q} = \sum_{i}  p=1 \lambda_{i}  + \sum  q \mu_{j} . Actually, to be perfectly rigorous G(\lambda , \mu ) is$$
$$only defined   intersection  of the^{j=1} hyperplane of equation \sum_{i}  p \lambda_{i}  = \sum_{jq+}  q \mu_{j}  with the$$
Lồi octant trong $\mathbb{R}^{p+q}$ cho trước bởi $\lambda  \ge 0, \mu  \ge 0$, do đó với mọi $\lambda  \in \mathbb{R}_{+}^{p} and^{=1}$ tất cả $\mu  \in \mathbb{R}^{=1}$, ta có
$$!$$
$$\lambda$$
$$G(\lambda , \mu ) =-_{2}^{1} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X\mu + \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q}if \sum_{i}  p=1 \lambda_{i}  = \sum  qj=1 \mu_{j}$$
$$-\infty otherwise.$$
$$$$
Lưu ý rằng điều kiện
$$\sum_{i=1}^{p}  \lambda_{i}  = \sum_{j=1}^{q}  \mu_{j}$$
Là Điều kiện $(*_{2})$ của Ví dụ 50.6, mà là không đáng ngạc nhiên. Bước $5$: Viết đối ngẫu (dual) bài toán quy hoạch trong ma trận tạo thành. Cực đại hóa đối ngẫu (dual) hàm $G(\lambda , \mu$) trên của nó miền xác định của định nghĩa là tương đương đến cực đại hóa
$$Gb(\lambda , \mu ) = - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q}$$
Subject đến ràng buộc
$$\sum_{i=1}^{p}  \lambda_{i}  = \sum_{j=1}^{q}  \mu_{j} ,$$

<!-- PAGE 1831 -->
Do đó ta formulate đối ngẫu (dual) bài toán quy hoạch như,
$$maximize- \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  = \sum_{j=1}^{q}  \mu_{j}$$
$$\lambda  \ge 0, \mu  \ge 0,$$
Hoặc tương đương,
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} - \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  = \sum_{j=1}^{q}  \mu_{j}$$
$$\lambda  \ge 0, \mu  \ge 0.$$
Các ràng buộc của đối ngẫu (dual) bài toán quy hoạch là nhiều đơn giản hơn hơn các ràng buộc
$$\begin{pmatrix} 1_{p} \\ X^{\top}-1_{q} \end{pmatrix} \begin{pmatrix} w \\ b \end{pmatrix} \le -1_{p+q}$$
Của gốc (primal) bài toán quy hoạch bởi vì các phần tử này các ràng buộc có đã được “absorbed” bởi hàm mục tiêu (objective function) $G(\lambda , \nu$) của đối ngẫu (dual) bài toán quy hoạch mà liên quan đến ma trận $X^{\top}X$. ma trận $X^{\top}X$ là
$$b$$
Đối xứng nửa xác định dương (positive semidefinite), nhưng không khả nghịch nói chung. Bước $6$: Giải đối ngẫu (dual) bài toán quy hoạch. bước này liên quan đến bằng cách sử dụng số các quy trình typically based trên hạ gradien (gradient descent) để tìm $\lambda$ và $\mu$, ví dụ, ADMM từ Mục 52.6. Một lần $\lambda$ và $\mu$ được xác định, $w$ được xác định bởi $(*_{1})$ và $b$ được xác định như trong Mục 50.6 bằng cách sử dụng sự kiện rằng ở đó là ít nhất một số $i_{0}$ sao cho $\lambda_{i0}  > 0$ và một số $j_{0}$ sao cho $\mu_{j0}  > 0$.
Các nhận xét:
$(1)$ Vì các ràng buộc là afin và hàm mục tiêu (objective function) là lồi, theo Định lý 50.19(2) khoảng cách đối ngẫu (duality gap) là không, do đó với mọi cực tiểu $w$ của J(w, $b) = (1/2)w^{\top}w$ và bất kỳ cực đại $(\lambda , \mu$) của $G$, ta có
$$J(w, b) = \frac{1}{2} w^{\top}w = G(\lambda , \mu ).$$

<!-- PAGE 1832 -->
Nhưng bởi $(*_{1})$
$$w = -X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = \sum_{i=1}^{p}  \lambda_{i} u_{i} - \sum_{j=1}^{q}  \mu_{j} v_{j},$$
Do đó
$$\begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = w^{\top}w,$$
Và ta thu được
$$\frac{1}{2} w^{\top}w = - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q} = - \frac{1}{2} w^{\top}w + \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q},$$
Do đó
$$w^{\top}w = \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q} = \sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j} ,$$
Mà cho ta
$$!$$
$$G(\lambda , \mu ) = \frac{1}{2} \sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j} .$$
Ở trên các công thức được phát biểu trong Vapnik $[188]$ (Chương $10$, Mục $1)$.
$(2)$ Nó là instructive để tính Hàm Lagrange (Lagrangian) của đối ngẫu (dual) bài toán quy hoạch và đến derive KKT các điều kiện cho điều này Hàm Lagrange (Lagrangian). các điều kiện $\lambda  \ge 0$ đang là tương đương đến $-\lambda  \le 0$, và các điều kiện $\mu  \ge 0$ đang là tương đương đến $-\mu  \le 0$, ta giới thiệu Các nhân tử Lagrange (Lagrange multipliers) $\alpha  \in \mathbb{R}_{+}^{p}$ và $\beta  \in \mathbb{R}_{+}^{q}$ cũng như nhân tử $\rho  \in \mathbb{R}$ cho equational ràng buộc, và ta tạo thành Hàm Lagrange (Lagrangian)
$$L(\lambda , \mu , \alpha , \beta , \rho ) = \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} - \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q}$$
$$- \sum_{i=1}^{p}  \alpha_{i} \lambda_{i}  - \sum_{j=1}^{q}  \beta_{j} \mu_{j}  + \rho \begin{pmatrix} \mu_{j} - & \lambda_{i} \end{pmatrix} \sum_{j=1}^{q}  \sum_{i=1}^{p}  .$$
Suy ra rằng KKT các điều kiện là
$$X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} -1_{p+q} - \begin{pmatrix} \alpha \\ \beta \end{pmatrix} + \rho \begin{pmatrix} -1_{p} \\ 1_{q} \end{pmatrix} = 0_{p+q},(*_{4})$$
Và $\alpha_{i} \lambda_{i}  = 0$ cho $i = 1, \dots  , p$ và $\beta_{j} \mu_{j}  = 0$ cho $j = 1, \dots  , q$. Nhưng $(*_{4})$ là tương đương đến
$$-X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + \rho \begin{pmatrix} 1_{p} \\ -1_{q} \end{pmatrix} + 1_{p+q} + \begin{pmatrix} \alpha \\ \beta \end{pmatrix} = 0_{p+q},$$
