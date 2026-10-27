# Các bài tập


<!-- PAGE 2145 -->
$$80$$
$$60$$
$$40$$
$$20$$
$$0$$
$$-20$$
$$-40$$
$$-40-30-20-100102030405060$$

![Figure 56.16](../../assets/ch56/fig_56_16.png)

**Hình 56.16:** Chạy $\nu$ -SV hồi quy phiên bản $2$ trên tập hợp của $50$ các điểm; $\nu  =$ 0.5.

## 56.7 Các bài tập

Bài toán 56.1. Chứng minh rằng nếu $\nu$ -SV hồi quy thành công và cho ta $w, b, \epsilon  > 0$, thì $\epsilon$ -SV hồi quy với cùng $C$ và cùng giá trị của $\epsilon$ cũng thành công và trả về cùng cặp $(w, b)$.
Bài toán 56.2. Chứng minh các công thức
$$b = \begin{pmatrix}\end{pmatrix} \sum_{\in I\lambda}  \begin{pmatrix}\end{pmatrix} \sum_{0\in I\mu}  \begin{pmatrix}\end{pmatrix} \begin{pmatrix}\end{pmatrix} \sum_{\in I\lambda}  \begin{pmatrix}\end{pmatrix} \sum_{0\in I\mu}  /2$$
$$\begin{pmatrix}  &  &  &  &  &  &  &  &  \\ y_{i0} & /|I_{\lambda}| + & y_{j0} & /|I_{\mu}| -w^{\top} & x_{i0} & /|I_{\lambda}| + & x_{j0} & /|I_{\mu}| \\ i0 & j & i0 & j \\  &  &  &  &  &  &  &  &  \\ y_{j0} & /|I_{\mu}| - & y_{i0} & /|I_{\lambda}| + w^{\top} & x_{i0} & /|I_{\lambda}| - & x_{j0} & /|I_{\mu}| \\ j & i0 & i0 & j \end{pmatrix}$$
$$\epsilon  = \begin{pmatrix}\end{pmatrix} \sum_{0\in I\mu}  \begin{pmatrix}\end{pmatrix} \sum_{\in I\lambda}  \begin{pmatrix}\end{pmatrix} \begin{pmatrix}\end{pmatrix} \sum_{\in I\lambda}  \begin{pmatrix}\end{pmatrix} \sum_{0\in I\mu}  /2$$
Được phát biểu chỉ trước Mệnh đề 56.6.
Bài toán 56.3. Cho chi tiết của chứng minh của Mệnh đề 56.6. Đặc biệt, chứng minh rằng
$$C \begin{pmatrix} p_{f}+ q_{f} \\ \nu  - \\ m \end{pmatrix} \epsilon  = - \begin{pmatrix} \lambda^{\top} & \mu^{\top} \\  \end{pmatrix} P \begin{pmatrix} \lambda \\ \mu \end{pmatrix} - \begin{pmatrix} y^{\top} & -y^{\top} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$- \frac{C}{m} \begin{pmatrix}  \\ w^{\top} & x_{i} - & x_{j} \end{pmatrix} \begin{pmatrix} - & y_{i} + & y_{j}+ (p_{f}-q_{f})b \end{pmatrix} \sum_{i\in K\lambda}  \sum_{j\in K\mu}  \sum_{i\in K\lambda}  \sum_{j\in K\mu}  .$$

<!-- PAGE 2146 -->
Bài toán 56.4. Chứng minh rằng các ma trận
$$A = \begin{pmatrix} 1_{m}^{\top} & -1_{m}^{\top} & 0_{m}^{\top} & 0_{m}^{\top} & 0 \\ 1_{m}^{\top} & 1_{m}^{\top} & 0_{m}^{\top} & 0_{m}^{\top} & 1 \\ I_{m} & 0_{m,m} & I_{m} & 0_{m,m} & 0_{m} \\ 0_{m,m} & I_{m} & 0_{m,m} & I_{m} & 0_{m} \end{pmatrix} ,A_{2} = \begin{pmatrix} 1_{m}^{\top} & -1_{m}^{\top} & 0_{m}^{\top} & 0_{m}^{\top} \\ 1_{m}^{\top} & 1_{m}^{\top} & 0_{m}^{\top} & 0_{m}^{\top} \\ I_{m} & 0_{m,m} & I_{m} & 0_{m,m} \\ 0_{m,m} & I_{m} & 0_{m,m} & I_{m} \end{pmatrix}$$
Có hạng (rank) 2m $+ 2$.
Bài toán 56.5. Derive phiên bản của $\nu$ -SV hồi quy trong mà tuyến tính hình phạt (penalty) hàm
$$\sum_{i}  m=1(\xi_{i}  + \xi_{i}' ) is replaced by the quadratic penalty function \sum_{i}  m=1(\xi_{i}^{2}  + \xi_{i}^{'2}  ). Derive the dual$$
Bài toán quy hoạch.
$$Problem 56.6. The linear penalty function \sum_{i}  m=1(\xi_{i}  + \xi_{i}' ) can be replaced by the quadratic$$
$$penalty function \sum_{i}  m(\xi_{i}^{2}  +\xi_{i}^{'2}  ). Prove that for an optimal solution we must have \xi_{i}  \ge 0 and$$
$\xi_{i}'  \ge 0$, do đó ta $may^{=1}$ bỏ qua các ràng buộc $\xi_{i}  \ge 0$ và $\xi_{i}'  \ge 0$. Ta phải cũng có $\gamma  = 0$ do đó ta có thể bỏ qua biến $\gamma$ cũng vậy. Chứng minh rằng $\xi  = (m/2C)\lambda$ và $\xi' = (m/2C)\mu$. bài toán này là rất đồng dạng đến Lề mềm (soft margin) SVM $(SVM_{s4})$ được thảo luận trong Mục 54.13.
Bài toán 56.7. Xét phiên bản của $\nu$ -SV hồi quy trong Mục 56.5. Chứng minh rằng với mọi nghiệm tối ưu (optimal solution) với $w \neq  0$ và $\epsilon  > 0$, nếu các bất đẳng thức $(p_{f} + q_{f})/m < \nu  < 1$ đúng, thì một số điểm $x_{i}$ là hỗ trợ/giá (support) vectơ.
Bài toán 56.8. Chứng minh rằng ma trận
$$A_{3} = \begin{pmatrix} 1_{m}^{\top} & 1_{m}^{\top} & 0_{m}^{\top} & 0_{m}^{\top} \\ I_{m} & 0_{m,m} & I_{m} & 0_{m,m} \\ 0_{m,m} & I_{m} & 0_{m,m} & I_{m} \end{pmatrix}$$
Có hạng (rank) 2m $+ 1$.
Bài toán 56.9. Xét phiên bản của $\nu$ -SV hồi quy trong Mục 56.5. Chứng minh sau đây các công thức: Nếu $I_{\lambda} \neq  \emptyset$, thì
$$\epsilon  = w^{\top} \begin{pmatrix} x_{i} \\ i \end{pmatrix} \sum_{\in I\lambda}  /|I_{\lambda}| + b - \begin{pmatrix} y_{i} \\ i \end{pmatrix} \sum_{\in I\lambda}  /|I_{\lambda}|,$$
Và nếu $I_{\mu} \neq  \emptyset$, thì
$$\epsilon  = -w^{\top} \begin{pmatrix} x_{j} \end{pmatrix} \sum_{j\in I\mu}  /|I_{\mu}| -b + \begin{pmatrix} y_{i} \\ i \end{pmatrix} \sum_{\in I\mu}  /|I_{\mu}|.$$
Bài toán 56.10. Cài đặt $\nu$ -Hồi quy Phiên bản $2$ được mô tả trong Mục 56.5. Chạy các ví dụ bằng cách sử dụng cả hai ban đầu phiên bản và phiên bản $2$ và compare các kết quả.
