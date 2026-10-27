# Việc giải -Hồi quy Bằng cách sử dụng ADMM


<!-- PAGE 2128 -->
Chứng minh là rất đồng dạng đến chứng minh của tương ứng công thức trong Mục 56.5. Theo Định lý 56.5, tồn tại một suppor vectơ $x_{i}$, nói
$$w^{\top}x_{i0} + b -y_{i0} = \epsilon or-w^{\top}x_{j0} -b + y_{j0} = \epsilon .$$
Thì ta tìm phương trình biểu diễn $\epsilon$ theo $\lambda , \mu$ và $w$, miễn là/được cung cấp rằng $\nu$ ̸ $= 2p_{f}/m$ và $\nu$ ̸ $= 2q_{f}/m$. chứng minh là tương tự đến chứng minh của Mệnh đề 54.4 và là để lại như một bài tập.

## 56.3 Việc giải \nu -Hồi quy Bằng cách sử dụng ADMM

Toàn phương phiếm hàm $F(\lambda , \mu$) xảy ra trong đối ngẫu (dual) bài toán quy hoạch cho trước bởi
$$F(\lambda , \mu ) = \frac{1}{2} \sum_{i,j=1}^{m}  (\lambda_{i}  -\mu_{i} )(\lambda_{j}  -\mu_{j} )x_{i}^{\top} x_{j} + \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} )y_{i}$$
$$is not of the form_{2}^{1} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \\ letKbe \end{pmatrix} P \begin{pmatrix} \lambda \\ \mu \end{pmatrix} +q^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} , but it can be converted in such a form using$$
Mẹo/kỹ thuật. Thứ nhất, nếu ta $m \times  m$ ma trận đối xứng (symmetric matrix) $K = XX^{\top} = (x_{i}^{\top} x_{j})$, thì ta có
$$F(\lambda , \mu ) = \frac{1}{2} (\lambda^{\top} -\mu^{\top} )K(\lambda  -\mu ) + y^{\top}\lambda  -y^{\top}\mu .$$
Hệ quả là, nếu ta định nghĩa 2m $\times$ 2m ma trận đối xứng (symmetric matrix) $P$ bởi
$$P = \begin{pmatrix} XX^{\top} & -XX^{\top} \\ -XX^{\top} & XX^{\top} \end{pmatrix} = \begin{pmatrix} K & -K \\ -K & K \end{pmatrix}$$
Và 2m $\times  1$ ma trận $q$ bởi
$$q = \begin{pmatrix} y \\ -y \end{pmatrix} ,$$
Nó là dễ để kiểm tra rằng
$$F(\lambda , \mu ) = \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} P \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + q^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = \frac{1}{2} \lambda^{\top} K\lambda  + \frac{1}{2} \mu^{\top} K\mu  -\lambda^{\top} K\mu  + y^{\top}\lambda  -y^{\top}\mu . (*_{q})$$
Vì
$$\frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} P \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = \frac{1}{2} (\lambda^{\top} -\mu^{\top} )K(\lambda  -\mu )$$
Và ma trận $K = XX^{\top}$ là đối xứng nửa xác định dương (positive semidefinite), ma trận $P$ là cũng đối xứng

<!-- PAGE 2129 -->
Nửa xác định dương (positive semidefinite). Do đó ta là trong position để áp dụng ADMM vì các ràng buộc là
$$\sum_{i=1}^{m}  \lambda_{i}  - \sum_{i=1}^{m}  \mu_{i}  = 0$$
$$\sum_{i=1}^{m}  \lambda_{i}  + \sum_{i=1}^{m}  \mu_{i}  + \gamma  = C\nu$$
$$\lambda  + \alpha  = \frac{C}{m} ,\mu  + \beta  = \frac{C}{m} ,$$
Cụ thể là afin. Ta cần để kiểm tra rằng (2m $+ 2) \times$ (4m $+ 1)$ ma trận $A$ tương ứng với hệ này có hạng (rank) 2m $+ 2$. Cho chúng ta clarify điều này điểm. ma trận $A$ tương ứng với ở trên các phương trình là
$$A = \begin{pmatrix} 1_{m}^{\top} & -1_{m}^{\top} & 0_{m}^{\top} & 0_{m}^{\top} & 0 \\ 1_{m}^{\top} & 1_{m}^{\top} & 0_{m}^{\top} & 0_{m}^{\top} & 1 \\ I_{m} & 0_{m,m} & I_{m} & 0_{m,m} & 0_{m} \\ 0_{m,m} & I_{m} & 0_{m,m} & I_{m} & 0_{m} \end{pmatrix} .$$
Ví dụ, cho $m = 3$ ta có ma trận cỡ $8 \times  13$
$$\begin{pmatrix} 1 & 1 & 1 & -1 & -1 & -1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 1 & 1 & 1 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \end{pmatrix} .$$
Ta để lại nó như một bài tập để chỉ ra rằng $A$ có hạng (rank) 2m $+ 2$. Nhắc lại rằng
$$q = \begin{pmatrix} y \\ -y \end{pmatrix}$$
Và ta cũng định nghĩa vectơ $c$ (có số chiều 2m $+ 2)$ như
$$c = \begin{pmatrix} 0 \\ C\nu \\ C1_{2m} \end{pmatrix} .$$
$$\overline{m}$$
Các ràng buộc được cho bởi hệ của afin các phương trình Ax $= c$, ở đâu
$$x = \begin{pmatrix} \lambda^{\top} & \mu^{\top} & \alpha^{\top} & \beta^{\top} \end{pmatrix} \gamma^{\top} .$$

<!-- PAGE 2130 -->
Vì có 4m $+ 1$ Các nhân tử Lagrange (Lagrange multipliers) $(\lambda , \mu , \alpha , \beta , \gamma$), ta cần đến pad 2m $\times$ 2m ma trận $P$ với các không điểm để tạo nó vào (4m $+ 1) \times$ (4m $+ 1)$ ma trận
$$P_{a} = \begin{pmatrix} P & 0_{2m,2m+1} \\ 0_{2m+1,2m} & 0_{2m+1,2m+1} \end{pmatrix} .$$
Tương tự, ta pad $q$ với các không điểm để tạo nó vectơ $q_{a}$ có số chiều 4m $+ 1$,
$$q_{a} = \begin{pmatrix} q \\ 0_{2m+1} \end{pmatrix} .$$
Trong thứ tự để giải đối ngẫu (đối ngẫu (dual)) của chúng ta bài toán quy hoạch, ta áp dụng ADMM đến quadractic phiếm hàm
$$\frac{1}{2} x^{\top}P_{a}x + q_{a}^{\top} x,$$
Subject đến các ràng buộc
$$Ax = c,x \ge 0,$$
Với $P_{a}, q_{a}, A, b$ và $x$, như ở trên. Vì cho nghiệm tối ưu (optimal solution) với $\epsilon  > 0$ ta phải có $\gamma  = 0$ (từ KKT các điều kiện), ta có thể giải bài toán đối ngẫu (dual problem) với sau đây tập hợp của các ràng buộc chỉ liên quan đến Các nhân tử Lagrange (Lagrange multipliers) $(\lambda , \mu , \alpha , \beta$),
$$\sum_{i=1}^{m}  \lambda_{i}  - \sum_{i=1}^{m}  \mu_{i}  = 0$$
$$\sum_{i=1}^{m}  \lambda_{i}  + \sum_{i=1}^{m}  \mu_{i}  = C\nu$$
$$\lambda  + \alpha  = \frac{C}{m} ,\mu  + \beta  = \frac{C}{m} ,$$
Mà tương ứng với (2m $+ 2) \times$ 4m $A_{2}$ cho trước bởi
$$A_{2} = \begin{pmatrix} 1_{m}^{\top} & -1_{m}^{\top} & 0_{m}^{\top} & 0_{m}^{\top} \\ 1_{m}^{\top} & 1_{m}^{\top} & 0_{m}^{\top} & 0_{m}^{\top} \\ I_{m} & 0_{m,m} & I_{m} & 0_{m,m} \\ 0_{m,m} & I_{m} & 0_{m,m} & I_{m} \end{pmatrix} .$$
Ta để lại nó như một bài tập để chỉ ra rằng $A_{2}$ có hạng (rank) 2m $+ 2$. Ta định nghĩa vectơ $c_{2}$ (có số chiều 2m $+ 2)$ như
$$c_{2} = c = \begin{pmatrix} 0 \\ C\nu \\ C1_{2m} \end{pmatrix} .$$
$$\overline{m}$$

<!-- PAGE 2131 -->
Vì có 4m Các nhân tử Lagrange (Lagrange multipliers) $(\lambda , \mu , \alpha , \beta$), ta cần đến pad 2m $\times$ 2m ma trận $P$ với các không điểm để tạo nó vào 4m $\times$ 4m ma trận
$$P_{2a} = \begin{pmatrix} P & 0_{2m,2m} \\ 0_{2m,2m} & 0_{2m,2m} \end{pmatrix} .$$
Tương tự, ta pad $q$ với các không điểm để tạo nó vectơ $q_{2a}$ có số chiều 4m,
$$q_{2a} = \begin{pmatrix} q \\ 0_{2m} \end{pmatrix} .$$
Ta được cài đặt ở trên các phương pháp trong Matlab; xem Phụ lục $B$, Mục B.4. Chọn $C = m$ là typically tốt lựa chọn bởi vì thì các giá trị của $\lambda_{i}$ và $\mu_{j}$ là không cũng nhỏ $(C/m = 1)$. Nếu $C$ được chọn cũng nhỏ, ta tìm thấy rằng số tính mất ổn định tăng drastically và rất poor các kết quả là thu được. Tăng $C$ tiến tới đến encourage sparsity. Ta ran của ta Matlab implementation của ở trên phương pháp trên tập hợp của $50$ các điểm được sinh tại ngẫu nhiên bởi bài toán quy hoạch được hiển thị dưới đây với $C = 50$ và khác nhau các giá trị của $\nu$ bắt đầu với $\nu  =$ 0.03: X13 $=$ 15*randn(50,1); ww13 $= 1$; y13 $=$ X13*ww13 $+$ 10*randn(50,1) $+ 20$; [~,~,~,~,~,~,~,~,w1] $=$ runuregb(rho,0.03,X13,y13,50) Hình 56.11 chỉ ra kết quả của chạy bài toán quy hoạch với $\nu  =$ 0.03. Ta có $p_{f} = 0, q_{f} = 0, p_{m} = 2$ và $q_{m} = 1$. Có $47$ các điểm chặt bên trong dải phẳng (slab). dải phẳng (slab) là lớn đủ đến chứa tất cả dữ liệu các điểm, do đó không có cái nào của chúng được xét sai số. tiếp theo giá trị của $\nu$ là $\nu  =$ 0.21, xem Hình 56.12. Ta có $p_{f} = 4, q_{f} = 5, p_{m} = 6$ và $q_{m} = 6$. Có $38$ các điểm chặt bên trong dải phẳng (slab).

<!-- PAGE 2132 -->
$$80$$
$$60$$
$$40$$
$$20$$
$$0$$
$$-20$$
$$-40$$
$$-40-30-20-100102030405060$$
$$Figure 56.11: Running \nu -SV regression on a set of 50 points; \nu  = 0.03.$$
$$80$$
$$60$$
$$40$$
$$20$$
$$0$$
$$-20$$
$$-40$$
$$-40-30-20-100102030405060$$
$$Figure 56.12: Running \nu -SV regression on a set of 50 points; \nu  = 0.21.$$
Tiếp theo giá trị của $\nu$ là $\nu  =$ 0.5, xem Hình 56.13. Ta có $p_{f} = 12, q_{f} = 12, p_{m} = 13$ và

<!-- PAGE 2133 -->
$q_{m} = 14$. Có $23$ các điểm chặt bên trong dải phẳng (slab).
$$80$$
$$60$$
$$40$$
$$20$$
$$0$$
$$-20$$
$$-40$$
$$\overline{-40}\overline{-30}\overline{-20}\overline{-10}\overline{0}\overline{10}\overline{20}\overline{30}\overline{40}\overline{50}\overline{60}$$
$$Figure 56.13: Running \nu -SV regression on a set of 50 points; \nu  = 0.5.$$
$$80$$
$$60$$
$$40$$
$$20$$
$$0$$
$$-20$$
$$-40$$
$$\overline{-40}\overline{-30}\overline{-20}\overline{-10}\overline{0}\overline{10}\overline{20}\overline{30}\overline{40}\overline{50}\overline{60}$$
$$Figure 56.14: Running \nu -SV regression on a set of 50 points; \nu  = 0.7.$$
Tiếp theo giá trị của $\nu$ là $\nu  =$ 0.7, xem Hình 56.14. Ta có $p_{f} = 17, q_{f} = 17, p_{m} = 18$ và
