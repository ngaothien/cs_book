# Các bài tập


<!-- PAGE 1571 -->

## 43.4 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ Các phần bù Schur. $\bullet$ ma trận nghịch đảo bổ đề. $\bullet$ Đối xứng xác định dương (SPD) các ma trận và Các phần bù Schur. $\bullet$ Đối xứng nửa xác định dương (positive semidefinite) các ma trận và Các phần bù Schur.

## 43.5 Các bài tập

Bài toán 43.1. Chứng minh rằng cực đại hóa hàm $g(\lambda$) cho trước bởi
$$g(\lambda ) = c_{0} + \lambda c_{1} -(b_{0} + \lambda b_{1})^{\top}(A_{0} + \lambda A_{1})^{+}(b_{0} + \lambda b_{1}),$$
Subject đến
$$A_{0} + \lambda A_{1} ⪰0,b_{0} + \lambda b_{1} \in range(A_{0} + \lambda A_{1}),$$
Với $A_{0}, A_{1}$ một số $n\times n$ đối xứng nửa xác định dương (positive semidefinite) các ma trận, $b_{0}, b_{1} \in \mathbb{R}^{n}$, và $c_{0}, c_{1} \in \mathbb{R}$, là tương đương đến cực đại hóa $\gamma$ subject đến các ràng buộc
$$\lambda  \ge 0$$
$$\begin{pmatrix} A_{0} + \lambda A_{1} & b_{0} + \lambda b_{1} \\ (b_{0} + \lambda b_{1})^{\top} & c_{0} + \lambda c_{1} -\gamma \end{pmatrix} ⪰0.$$
$$\mathbb{R}^{n}  \mathbb{R}^{n}$$
Bài toán 43.2. Cho $a_{1}, \dots  , a_{m}$ là $m$ các vectơ trong và giả sử rằng chúng sinh (span).
$(1)$ Chứng minh rằng ma trận
$$\sum_{k=1}^{m}  a_{k}a_{k}^{\top}$$
Là đối xứng xác định dương (SPD).
$(2)$ Định nghĩa ma trận $X$ bởi
$$!-1$$
$$X = \sum_{k=1}^{m}  a_{k}a_{k}^{\top}.$$
Chứng minh rằng
$$\sum_{k}  m=1 a_{k}a_{k}^{\top}a_{i}!⪰$$
$$0,i = 1, \dots  , m.$$
$$a_{i}^{\top}1$$
Suy ra rằng
$$a_{i}^{\top} Xa_{i} \le 1,1 \le i \le m.$$

<!-- PAGE 1572 -->
Bài toán 43.3. Xét hàm $g$ của Ví dụ 39.15 được định nghĩa bởi
$$g(a, b, c) = \log(ac -b^{2}),$$
Ở đâu ac - $b^{2} > 0$. Ta tìm thấy rằng Ma trận Hesse (Hessian matrix) của $g$ được cho bởi
$$Hg(a, b, c) = \frac{1}{(ac -b^{2})^{2}} \begin{pmatrix} -c^{2} & 2bc & -b^{2} \\ 2bc & -2(b^{2}+ ac) & 2ab \\ b^{2} & 2ab & a^{2} \end{pmatrix} .$$
$$--$$
Sử dụng Phần bù Schur (Schur complement) (của $a^{2})$ để chứng minh rằng ma trận -Hg(, $b, c)$ là đối xứng xác định dương (SPD) nếu ac - $b^{2} > 0$ và, $c > 0$.
