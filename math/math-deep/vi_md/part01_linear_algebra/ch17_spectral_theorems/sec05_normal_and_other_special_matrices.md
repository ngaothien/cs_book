# Chuẩn tắc/bình thường và Khác Đặc biệt Các ma trận


<!-- PAGE 642 -->

## 17.5 Chuẩn tắc/bình thường và Khác Đặc biệt Các ma trận

Thứ nhất ta xét thực các ma trận. Nhắc lại sau đây các định nghĩa.

> **Định nghĩa 17.3.** Cho trước thực $m \times  n$ ma trận $A$, chuyển vị (transpose) $A^{\top}$ của $A$ là ma trận cỡ $n \times  m$ $A^{\top} = (a_{i j}^{\top})$ được định nghĩa sao cho
$$a_{i j}^{\top} = a_{j i}$$
Với mọi $i, j, 1 \le i \le m, 1 \le j \le n$. thực $n \times  n$ ma trận $A$ là $\bullet$ chuẩn tắc/bình thường nếu
$$A A^{\top}= A^{\top}A,$$
$\bullet$ đối xứng nếu
$$A^{\top}= A,$$
$\bullet$ phản đối xứng nếu
$$A^{\top}= -A,$$
$\bullet$ trực giao nếu
$$A A^{\top}= A^{\top}A = I_{n}.$$
Nhắc lại từ Mệnh đề 12.14 rằng khi $E$ là Không gian Euclid (Euclidean space) và $(e_{1}, \dots , e_{n})$ là cơ sở trực chuẩn (orthonormal basis) cho $E$, nếu $A$ là ma trận của ánh xạ tuyến tính (linear map) $f$: $E \to E$ w.r.t. cơ sở (basis) $(e_{1}, \dots  , e_{n})$, thì $A^{\top}$ là ma trận của liên hợp (adjoint) $f^{*}$ của $f$. Hệ quả là, chuẩn tắc/bình thường ánh xạ tuyến tính (linear map) có ma trận chuẩn tắc (normal matrix), tự liên hợp (self-adjoint) ánh xạ tuyến tính (linear map) có ma trận đối xứng (symmetric matrix), phản tự liên hợp (skew-self-adjoint) ánh xạ tuyến tính (linear map) có ma trận phản đối xứng (skew-symmetric matrix), và trực giao ánh xạ tuyến tính (linear map) có ma trận trực giao (orthogonal matrix). Hơn nữa, nếu $(u_{1}, \dots  , u_{n})$ là một cái khác cơ sở trực chuẩn (orthonormal basis) cho $E$ và $P$ là ma trận chuyển cơ sở (change of basis matrix) có các cột là các thành phần của $u_{i}$ w.r.t. cơ sở (basis) $(e_{1}, \dots  , e_{n})$, thì $P$ là trực giao, và với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$, nếu $A$ là ma trận của $f$ w.r.t $(e_{1}, \dots  , e_{n})$ và $B$ là ma trận của $f$ w.r.t. $(u_{1}, \dots  , u_{n})$, thì
$$B = P^{\top} AP.$$
Hệ quả là, Các định lý 17.12 và 17.14–17.16 có thể được restated như sau.

<!-- PAGE 643 -->

> **Định lý 17.18.** Với mọi ma trận chuẩn tắc (normal matrix) $A$ có một ma trận trực giao (orthogonal matrix) $P$ và khối ma trận đường chéo (diagonal matrix) $D$ sao cho $A = PD P^{\top}$, ở đâu $D$ là của tạo thành
$$D = \begin{pmatrix} D_{1} & \dots \\ D_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & D_{p} \end{pmatrix}$$
Sao cho mỗi khối $D_{j}$ là hoặc một chiều ma trận (i.e., thực vô hướng (scalar)) hoặc twodimensional ma trận của tạo thành
$$D_{j} = \begin{pmatrix} \lambda_{j} & -\mu_{j} \\ \mu_{j} & \lambda_{j} \end{pmatrix} ,$$
Ở đâu $\lambda_{j} , \mu_{j}  \in \mathbb{R}$, với $\mu_{j}  > 0$.

> **Định lý 17.19.** Với mọi ma trận đối xứng (symmetric matrix) $A$ có một ma trận trực giao (orthogonal matrix) $P$ và ma trận đường chéo (diagonal matrix) $D$ sao cho $A = PD P^{\top}$, ở đâu $D$ là của tạo thành
$$D = \begin{pmatrix} \lambda_{1} & \dots \\ \lambda_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & \lambda_{n} \end{pmatrix} ,$$
Ở đâu $\lambda_{i}  \in \mathbb{R}$.

> **Định lý 17.20.** Với mọi ma trận phản đối xứng (skew-symmetric matrix) $A$ có một ma trận trực giao (orthogonal matrix) $P$ và khối ma trận đường chéo (diagonal matrix) $D$ sao cho $A = PD P^{\top}$, ở đâu $D$ là của tạo thành
$$D = \begin{pmatrix} D_{1} & \dots \\ D_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & D_{p} \end{pmatrix}$$
Sao cho mỗi khối $D_{j}$ là hoặc $0$ hoặc hai chiều ma trận của tạo thành
$$D_{j} = \begin{pmatrix} 0 \\ -\mu_{j} \\ \mu_{j} & 0 \end{pmatrix} ,$$
Ở đâu $\mu_{j}  \in \mathbb{R}$, với $\mu_{j}  > 0$. Đặc biệt, các trị riêng (eigenvalues) của $A$ là thuần túy imaginary của tạo thành $\pm i\mu_{j}$, hoặc $0$.

> **Định lý 17.21.** Với mọi ma trận trực giao (orthogonal matrix) $A$ có một ma trận trực giao (orthogonal matrix) $P$ và khối ma trận đường chéo (diagonal matrix) $D$ sao cho $A = PD P^{\top}$, ở đâu $D$ là của tạo thành
$$D = \begin{pmatrix} D_{1} & \dots \\ D_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & D_{p} \end{pmatrix}$$

<!-- PAGE 644 -->
Sao cho mỗi khối $D_{j}$ là hoặc $1, -1$, hoặc hai chiều ma trận của tạo thành
$$D_{j} = \begin{pmatrix} \cos \theta_{j} & -\sin \theta_{j} \\ \sin \theta_{j} & \cos \theta_{j} \end{pmatrix}$$
Ở đâu $0 < \theta_{j}  < \pi$. Đặc biệt, các trị riêng (eigenvalues) của $A$ là của tạo thành cos $\theta_{j}  \pm  i$ sin $\theta_{j} , 1$, hoặc $-1$. Định lý 17.21 có thể được được sử dụng để chỉ ra rằng hàm mũ ánh xạ exp: $\mathfrak{so}(n) \to$ Do đó(n) là toàn ánh (surjective); xem Gallier $[73]$. Ta bây giờ xét phức các ma trận.

> **Định nghĩa 17.4.** Cho trước phức $m \times  n$ ma trận $A$, chuyển vị (transpose) $A^{\top}$ của $A$ là $n \times  m$
$$matrix A^{\top}= \begin{pmatrix} a_{i j}^{\top} \end{pmatrix} defined such that$$
$$a_{i j}^{\top} = a_{j i}$$
Với mọi $i, j, 1 \le i \le m, 1 \le j \le n$. liên hợp $\overline{A}$ của $A$ là ma trận cỡ $m \times  n$ $\overline{A} = (b_{i j})$ được định nghĩa sao cho
$$b_{i j} =\overline{a}_{i j}$$
Với mọi $i, j, 1 \le i \le m, 1 \le j \le n$. Cho trước $m \times  n$ phức ma trận $A$, liên hợp (adjoint) $A^{*}$ của $A$ là ma trận được định nghĩa sao cho
$$A^{*}\overline{= (}\overline{A}^{\top}\overline{) = (}\overline{A})^{\top}.$$
Phức $n \times  n$ ma trận $A$ là $\bullet$ chuẩn tắc/bình thường nếu
$$AA^{*}= A^{*}A,$$
$\bullet$ Hermite nếu
$$A^{*}= A,$$
$\bullet$ skew-Hermitian nếu
$$A^{*}= -A,$$
$\bullet$ unita nếu
$$AA^{*}= A^{*}A = I_{n}.$$
