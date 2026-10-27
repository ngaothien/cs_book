# Việc giải SVM (SVMs5) Bằng cách sử dụng ADMM


<!-- PAGE 2051 -->
Định nghĩa tập lồi (convex set)
$$$$
$$U = \begin{pmatrix} \lambda \\ \mu \end{pmatrix} \in \mathbb{R}_{+}^{p+q}| 1_{p}^{\top} \lambda  + 1_{q}^{\top} \mu  = (p + q)K_{s}\nu .$$
Chứng minh là về cơ bản chứng minh của 54.8 bằng cách sử dụng ở trên SPD ma trận và tập lồi (convex set). “kernelized” phiên bản của Bài toán $(SVM_{s5})$ là sau đây: Lề mềm (soft margin) hạt nhân (kernel) SVM $(SVM_{s5})$:
$$-$$
$$minimize \frac{1}{2} \langle w, w\rangle + \frac{1}{2} b^{2}\nu \eta  + K_{s}(\epsilon^{\top} \epsilon  + \xi^{\top} \xi )$$
$$subject to$$
$$\langle w, \phi (u_{i})\rangle -b \ge \eta  -\epsilon_{i} ,i = 1, \dots  , p$$
$$-\langle w, \phi (v_{j})\rangle + b \ge \eta  -\xi_{j} ,j = 1, \dots  , q,$$
Với $K_{s} = 1/(p + q)$. Tracing qua derivation của đối ngẫu (dual) bài toán quy hoạch, ta thu được Đối ngẫu (dual) của Lề mềm (soft margin) hạt nhân (kernel) SVM $(SVM_{s5})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ K + & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} \begin{pmatrix} 1 \\ + & I_{p+q} \\ 2K_{s} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = \nu$$
$$\lambda_{i}  \ge 0,i = 1, \dots  , p$$
$$\mu_{j}  \ge 0,j = 1, \dots  , q,$$
Ở đâu $K$ là hạt nhân (kernel) ma trận của Mục 54.1. Thì $w, b$, và f(x) là thu được chính xác như trong Mục 54.13.

## 54.16 Việc giải SVM (SVM) Bằng cách sử dụng ADMM

$$s5$$
Trong thứ tự để giải $(SVM_{5})$ bằng cách sử dụng ADMM ta cần đến viết ma trận tương ứng với các ràng buộc trong equational tạo thành,
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = K_{m},$$
Với $K_{m} = (p + q)K_{s}\nu$. Điều này là ma trận cỡ $1 \times  (p + q)$ $A$ cho trước bởi
$$A = \begin{pmatrix} 1_{p}^{\top} & 1_{q}^{\top} \end{pmatrix} .$$

<!-- PAGE 2052 -->
Hiển nhiên, $A$ có hạng (rank) $1$. vế phải là
$$c = K_{m}.$$
Đối xứng xác định dương (SPD) $(p + q) \times  (p + q)$ ma trận $P$ định nghĩa toàn phương phiếm hàm là
$$P = X^{\top}X + \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} + \frac{1}{2K_{s}} I_{p+q},withX = \begin{pmatrix} -u_{1} & \cdots & -u_{p} & v_{1} & \cdots & v_{q} \end{pmatrix} ,$$
Và
$$q = 0_{p+q}.$$
Vì có $p + q$ Các nhân tử Lagrange (Lagrange multipliers) $(\lambda , \mu$), ma trận cỡ $(p + q) \times  (p + q)$ $P$ thực hiện không có là augmented với không’s. Ta ran của ta Matlab implementation của ở trên phiên bản của $(SVM_{s5})$ trên dữ liệu tập hợp của Mục 54.14. Vì giá trị của $\nu$ là irrelevant, ta được chọn $\nu  = 1$. Thứ nhất ta ran của ta bài toán quy hoạch với $K = 190$; xem Hình 54.24. Ta có $p_{m} = 23$ và $q_{m} = 18$. bài toán quy hoạch thực hiện không hội tụ cho $K \ge 200$.
$$30$$
$$20$$
$$10$$
$$0$$
$$-10$$
$$-20$$
$$-30$$
$$-30-20-10010203040$$
$$Figure 54.24: Running (SVM_{s5}) on two sets of 30 points; K = 190.$$
