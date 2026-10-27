# Việc giải Lề cứng (hard margin) (SVMh2) Bằng cách sử dụng ADMM


<!-- PAGE 1932 -->
Ta xem ngay lập tức rằng các ràng buộc
$$x + y -z = 0$$
$$x -y -z = 0$$
Suy ra rằng $z = x$ và $y = 0$. Thì nó là dễ bằng cách sử dụng vi tích phân để tìm rằng duy nhất cực tiểu được cho bởi $(x, y, z) = (1, 0, 1)$. Chạy qsolve1 trên $P_{1}, q_{1}, A_{1}, b_{1}$ với $\rho  = 10$, tolr $=$ tols $= 10^{-12}$ và iternum $= 10000$, ta tìm rằng sau $83$ các vòng lặp gốc (primal) và đối ngẫu (dual) các phần dư là ít hơn $10^{-12}$, và ta thu được
$$(x, y, z) = (1.000000000000149, 0.000000000000000, 1.000000000000148).$$

> **Ví dụ 52.12.** Xét toàn phương bài toán quy hoạch cho mà
$$P_{2} = \begin{pmatrix} 4 & 1 & 0 & 0 \\ 1 & 4 & 1 & 0 \\ 0 & 1 & 4 & 1 \\ 0 & 0 & 1 & 4 \end{pmatrix} q_{2} = - \begin{pmatrix} 4 \\ 4 \\ 4 \\ 4 \end{pmatrix}$$
$$A_{2} = \begin{pmatrix} 1 & 1 & -1 & 0 \\ 1 & -1 & -1 & 0 \end{pmatrix} b_{2} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} .$$
Một lần nữa, ta xem ngay lập tức rằng các ràng buộc suy ra rằng $z = x$ và $y = 0$. Thì nó là dễ bằng cách sử dụng vi tích phân để tìm rằng duy nhất cực tiểu được cho bởi $(x, y, z) = (28/31, 0, 28/31, 24/31)$. Chạy qsolve1 trên $P_{2}, q_{2}, A_{2}, b_{2}$ với $\rho  = 10$, tolr $=$ tols $= 10^{-12}$ và iternum $= 10000$, ta tìm rằng sau $95$ các vòng lặp gốc (primal) và đối ngẫu (dual) các phần dư là ít hơn $10^{-12}$, và ta thu được $(x, y, z, t) =$ (0.903225806451495, 0.000000000000000, 0.903225806451495,
$$0.774193548387264),$$
Mà agrees với câu trả lời tìm thấy trước đó sai khác $11$ decimals. Như illustration của wide miền giá trị (range) của các ứng dụng của ADMM ta chỉ ra trong mục tiếp theo cách mà để giải lề cứng (hard margin) SVM $(SVM_{h2})$ được thảo luận trong Mục 50.6.

## 52.7 Việc giải Lề cứng (hard margin) (SVM) Bằng cách sử dụng ADMM

$$h2$$
Nhắc lại rằng ta sẽ like để giải sau đây tối ưu hóa bài toán (xem Mục 50.6): Lề cứng (hard margin) SVM $(SVM_{h2})$:
$$minimize \frac{1}{2} \|w\|^{2}$$
$$subject to$$
$$w^{\top}u_{i} -b \ge 1i = 1, \dots  , p$$
$$-w^{\top}v_{j} + b \ge 1j = 1, \dots  , q.$$

<!-- PAGE 1933 -->
Lề (margin) là $\delta  = 1/ \|w\|$. tách siêu phẳng (hyperplane) $H_{w,b}$ là siêu phẳng (hyperplane) của phương trình $w^{\top}x$ - $b = 0$, và lề (margin) các siêu phẳng là các siêu phẳng $H_{w,b+1}$ (xanh lam siêu phẳng (hyperplane)) của phương trình $w^{\top}x$ - $b$ - $1 = 0$ và $H_{w,b-1}$ (đỏ siêu phẳng (hyperplane)) của phương trình $w^{\top}x$ - $b + 1 = 0$. đối ngẫu (dual) bài toán quy hoạch derived trong Mục 50.10 là sau đây bài toán quy hoạch: Đối ngẫu (dual) của Lề cứng (hard margin) SVM $(SVM_{h2})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} - \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\lambda  \ge 0, \mu  \ge 0,$$
Ở đâu $X$ là ma trận cỡ $n \times  (p + q)$ cho trước bởi
$$X = \begin{pmatrix} -u_{1} & \cdots & -u_{p} & v_{1} & \cdots & v_{q} \end{pmatrix} .$$
Thì $w$ được xác định như sau:
$$w = -X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = \sum_{i=1}^{p}  \lambda_{i} u_{i} - \sum_{j=1}^{q}  \mu_{j} v_{j}.$$
Để giải đối ngẫu (dual) bằng cách sử dụng ADMM ta cần để xác định các ma trận $P, q A$ và $c$ như trong Mục 52.6(2). Ta renamed $b$ như $c$ để tránh clash vì $b$ là đã được sử dụng. Ta có
$$P = X^{\top}X,q = -1_{p+q},$$
Và vì chỉ ràng buộc là
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0,$$
Ma trận $A$ là $1 \times  (p + q)$ vectơ hàng (row vector)
$$A = \begin{pmatrix} 1_{p}^{\top} & -1_{q}^{\top} \end{pmatrix} ,$$
Và vế phải $c$ là vô hướng (scalar)
$$c = 0.$$
Hiển nhiên ma trận $A$ có hạng (rank) $1$. Ta thu được $b$ bằng cách sử dụng bất kỳ $i_{0}$ sao cho $\lambda_{i0}  > 0$ và bất kỳ $j_{0}$ sao cho $\mu_{j0}  > 0$. Vì tương ứng các ràng buộc là hoạt động, ta có
$$w^{\top}u_{i0} -b = 1,-w^{\top}v_{j0} + b = 1,$$
