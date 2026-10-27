# Việc giải SVM (SVMs4) Bằng cách sử dụng ADMM


<!-- PAGE 2045 -->
Đối ngẫu (dual) của Lề mềm (soft margin) hạt nhân (kernel) SVM $(SVM_{s4})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1 \\ K + & I_{p+q} \\ 2K_{s} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  \ge \nu$$
$$\lambda_{i}  \ge 0,i = 1, \dots  , p$$
$$\mu_{j}  \ge 0,j = 1, \dots  , q,$$
Ở đâu $K$ là hạt nhân (kernel) ma trận của Mục 54.1. Thì $w, b$, và f(x) là thu được chính xác như trong Mục 54.5.

## 54.14 Việc giải SVM (SVM) Bằng cách sử dụng ADMM

$$s4$$
Trong thứ tự để giải $(SVM_{s4})$ bằng cách sử dụng ADMM ta cần đến viết ma trận tương ứng với các ràng buộc trong equational tạo thành,
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  -\gamma  = K_{m},$$
Với $K_{m} = (p + q)K_{s}\nu$. Điều này là ma trận cỡ $2 \times  (p + q + 1)$ $A$ cho trước bởi
$$1_{p}^{\top}-1_{q}^{\top}0!$$
$$A =.$$
$$1_{p}^{\top}1_{q}^{\top}-1$$
Ta để lại nó như một bài tập để chứng minh rằng $A$ có hạng (rank) $2$. vế phải là
$$c = \begin{pmatrix} 0 \\ K_{m} \end{pmatrix} .$$
Đối xứng nửa xác định dương (positive semidefinite) $(p+q)\times (p+q)$ ma trận $P$ định nghĩa toàn phương phiếm hàm là
$$P = X^{\top}X + \frac{1}{2K_{s}} I_{p+q},withX = \begin{pmatrix} -u_{1} & \cdots & -u_{p} & v_{1} & \cdots & v_{q} \end{pmatrix} ,$$
Và
$$q = 0_{p+q}.$$

<!-- PAGE 2046 -->
Vì có $p + q + 1$ Các nhân tử Lagrange (Lagrange multipliers) $(\lambda , \mu , \gamma$), ma trận cỡ $(p + q) \times  (p + q)$ $P$ phải là augmented với không’s để tạo nó một ma trận cỡ $(p + q + 1) \times  (p + q + 1)$ $P_{a}$ cho trước bởi
$$P_{a} = \begin{pmatrix} X^{\top}X & 0_{p+q} \\ 0_{p+q}^{\top} & 0 \end{pmatrix} ,$$
Và tương tự $q$ là augmented với các không điểm như vectơ $q_{a} = 0_{p+q+1}$. Như trong Mục 54.8, vì $\eta  \ge 0$ cho nghiệm tối ưu (optimal solution), ta có thể bỏ ràng buộc $\eta  \ge 0$ từ bài toán gốc (primal problem). Trong trường hợp này, có $p + q$ Các nhân tử Lagrange (Lagrange multipliers) $(\lambda , \mu$). Nó là dễ để xem rằng hàm mục tiêu (objective function) của đối ngẫu (dual) là unchanged và tập hợp của các ràng buộc là
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = K_{m},$$
Với $K_{m} = (p + q)K_{s}\nu$. ma trận tương ứng với ở trên các phương trình là ma trận cỡ $2 \times  (p + q)$ $A_{2}$ cho trước bởi
$$1_{p}^{\top}-1_{q}^{\top}!$$
$$A_{2} =.$$
$$1_{p}^{\top}1_{q}^{\top}$$
Ta để lại nó như một bài tập để chứng minh rằng $A_{2}$ có hạng (rank) $2$. vế phải là
$$c_{2} = \begin{pmatrix} 0 \\ K_{m} \end{pmatrix} .$$
Đối xứng nửa xác định dương (positive semidefinite) $(p+q)\times (p+q)$ ma trận $P$ định nghĩa toàn phương phiếm hàm là
$$P = X^{\top}X + \frac{1}{2K_{s}} I_{p+q},withX = \begin{pmatrix} -u_{1} & \cdots & -u_{p} & v_{1} & \cdots & v_{q} \end{pmatrix} ,$$
Và
$$q = 0_{p+q}.$$
Vì có $p + q$ Các nhân tử Lagrange (Lagrange multipliers) $(\lambda , \mu$), ma trận cỡ $(p + q) \times  (p + q)$ $P$ cần không là augmented với không’s, do đó $P_{2a} = P$ và tương tự $q_{2a} = 0_{p+q}$. Ta ran của ta Matlab implementation của ở trên phiên bản của $(SVM_{s4})$ trên dữ liệu tập hợp của Mục 54.12. Vì giá trị của $\nu$ là irrelevant, ta được chọn $\nu  = 1$. Thứ nhất ta ran của ta bài toán quy hoạch với $K = 190$; xem Hình 54.22. Ta có $p_{m} = 23$ và $q_{m} = 18$. bài toán quy hoạch thực hiện không hội tụ cho $K \ge 200$.
