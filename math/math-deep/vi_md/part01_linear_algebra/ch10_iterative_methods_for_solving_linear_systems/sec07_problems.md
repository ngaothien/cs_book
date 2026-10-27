# Các bài tập


<!-- PAGE 411 -->

## 10.7 Các bài tập

Bài toán 10.1. Xét ma trận
$$A = \begin{pmatrix} 1 & 2 & -2 \\ 1 & 1 & 1 \\ 2 & 2 & 1 \end{pmatrix} .$$
Chứng minh rằng $\rho (J) = 0$ và $\rho (\mathcal{L}_{1}) = 2$, do đó
$$\rho (J) < 1 < \rho (\mathcal{L}_{1}),$$
Ở đâu $J$ là Jacobi’s ma trận và $\mathcal{L}_{1}$ là ma trận của Gauss–Seidel.
Bài toán 10.2. Xét ma trận
$$A = \begin{pmatrix} 2 & -1 & 1 \\ 2 & 2 & 2 \\ 1 & 1 & 2 \end{pmatrix} .$$
$$--$$
$$\sqrt$$
Chứng minh rằng $\rho (J) = \overline{5}/2$ và $\rho (\mathcal{L}_{1}) = 1/2$, do đó
$$\rho (\mathcal{L}_{1}) < \rho (J),$$
Ở đâu ở đâu $J$ là Jacobi’s ma trận và $\mathcal{L}_{1}$ là ma trận của Gauss–Seidel.
Bài toán 10.3. Xét sau đây hệ phương trình tuyến tính:
$$\begin{pmatrix} 2 & -1 & 0 & 0 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ 0 & 0 & 1 & 2 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \\ x_{4} \end{pmatrix} = \begin{pmatrix} 19 \\ 19 \\ -3 \\ 12 \end{pmatrix} .$$
$$--$$
$(1)$ Giải ở trên hệ bởi Phép khử Gauss (Gaussian elimination).
$(2)$ Tính các dãy của các vectơ $u_{k} = (u_{1}^{k}, u_{2}^{k}, u_{3}^{k}, u_{4}^{k})$ cho $k = 1, \dots  , 10$, bằng cách sử dụng các phương pháp của Jacobi, Gauss–Seidel, và relaxation cho sau đây các giá trị của $\omega$: $\omega  =$ 1.1, 1.2, $\dots$, 1.9. Trong tất cả các trường hợp, ban đầu vectơ là $u_{0} = (0, 0, 0, 0)$.
Bài toán 10.4. Nhắc lại rằng phức hoặc thực $n \times  n$ ma trận $A$ là chặt hàng một cách đường chéo
$$dominant if |a_{ii}| > \sum_{j}  n=1,j\neq i |a_{ij}| for i = 1, \dots  , n.$$
$(1)$ Chứng minh rằng nếu $A$ là chặt hàng một cách đường chéo trội, thì Jacobi’s phương pháp hội tụ.
$(2)$ Chứng minh rằng nếu $A$ là chặt hàng một cách đường chéo trội, thì Gauss–Seidel’s phương pháp hội tụ.

<!-- PAGE 412 -->
Bài toán 10.5. Chứng minh rằng điều ngược lại của Mệnh đề 10.5 nghiệm đúng. Rằng là, nếu $A$ là khả nghịch Ma trận Hermite (Hermitian matrix) với splitting $A = M$ - $N$ ở đâu $M$ là khả nghịch, nếu Ma trận Hermite (Hermitian matrix) $M^{*} + N$ là xác định dương (positive definite) và nếu $\rho (M^{-1} N) < 1$, thì $A$ là xác định dương (positive definite).
Bài toán 10.6. Xét sau đây ba đường chéo $n \times  n$ ma trận:
$$A = \frac{1}{(n + 1)^{2}} \begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ \ddots & \ddots & \ddots \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{pmatrix} .$$
$(1)$ Chứng minh rằng các trị riêng (eigenvalues) của Jacobi ma trận $J$ được cho bởi
$$\lambda_{k}  = \cos \begin{pmatrix} k\pi \\ n + 1 \end{pmatrix} ,k = 1, \dots  , n.$$
Hint. Thứ nhất chỉ ra rằng Jacobi ma trận là
$$J = \frac{1}{2} \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ \ddots & \ddots & \ddots \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix} .$$
Thì các trị riêng (eigenvalues) và các vectơ riêng (eigenvectors) của $J$ là các nghiệm của hệ của các phương trình
$$y_{0} = 0$$
$$y_{k+1} + y_{k-1} = 2\lambda y_{k},k = 1, \dots  , n$$
$$y_{n+1} = 0,$$
Ở đâu các biến $y_{0}$ và $y_{n+1}$ là đã giới thiệu sao cho cùng phương trình áp dụng cho $k = 1, \dots  , n$. Ta đã biết rõ rằng tổng quát nghiệm đến ở trên recurrence được cho bởi
$$y_{k} = \alpha z_{1}^{k} + \beta z_{2}^{k},k = 0, \dots  , n + 1,$$
(với $\alpha , \beta  \neq  0)$ ở đâu $z_{1}$ và $z_{2}$ là các không điểm của phương trình
$$z^{2}-2\lambda z + 1 = 0.$$
Suy ra rằng $z_{2} = z_{1}^{-1}$ và $z_{1} + z_{2} = 2\lambda$. biên (boundary) điều kiện $y_{0} = 0$ cho ta $\alpha  + \beta  = 0$, do đó $y_{k} = \alpha (z_{1}^{k}$ - $z_{1}^{-k}$), và biên (boundary) điều kiện $y_{n+1} = 0$ cho ta
$$z_{1}^{2(n+1)}= 1.$$

<!-- PAGE 413 -->
Suy ra rằng ta có thể giả sử rằng $n$ khả dĩ/có thể các giá trị $(z_{1})_{k}$ cho $z_{1}$ được cho bởi
$$(z_{1})_{k} =\overline{e}_{n+1}^{k\pi i},k = 1, \dots  , n,$$
Và tìm
$$2\lambda_{k}  = (z_{1})_{k} + (z_{1})_{k}^{-1} .$$
Chỉ ra rằng vectơ riêng (eigenvector) $(y_{1}^{(k)} , \dots  , y_{n}^{(k)}$) liên kết với trị riêng (eigenvalue) $\lambda_{k}$ được cho bởi
$$y_{j}^{(k)}= \sin \begin{pmatrix} kj\pi \\ n + 1 \end{pmatrix} ,j = 1, \dots  , n.$$
$(2)$ Tìm bán kính phổ (spectral radius) $\rho (J), \rho (\mathcal{L}_{1})$, và $\rho (\mathcal{L}_{\omega0})$, như các hàm của $h = 1/(n + 1)$.

<!-- PAGE 414 -->
