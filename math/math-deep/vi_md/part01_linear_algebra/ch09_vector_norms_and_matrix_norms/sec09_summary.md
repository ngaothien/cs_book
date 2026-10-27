# Tóm tắt


<!-- PAGE 380 -->
Do đó, ta xem rằng hàm mũ của $2 \times  2$ ma trận phản đối xứng (skew-symmetric matrix) là ma trận quay (rotation matrix). tính chất này tổng quát hóa đến bất kỳ số chiều. tường minh công thức khi $n = 3$ (Rodrigues’ công thức) là cho trước trong Mục 12.7.

> **Mệnh đề 9.24.** Nếu $B$ là $n \times  n$ (thực) skew ma trận đối xứng (symmetric matrix), nghĩa là, $B^{\top} = -B$, thì $Q = e^{B}$ là ma trận trực giao (orthogonal matrix), nghĩa là
$$Q^{\top}Q = QQ^{\top}= I.$$

*Chứng minh.* Vì $B^{\top} = -B$, ta có
$$Q^{\top}= (e^{B})^{\top}= e^{B\top}= e^{-B}.$$
Vì $B$ và $-B$ giao hoán, ta có
$$Q^{\top}Q = e^{-B}e^{B}= e^{-B+B}= e^{0}= I.$$
Tương tự,
$$QQ^{\top}= e^{B}e^{-B}= e^{B-B}= e^{0}= I,$$
Mà kết luận chứng minh. Nó có thể cũng được hiển thị rằng det(Q) $= det(e^{B}) = 1$, nhưng điều này đòi hỏi tốt hơn understanding của các trị riêng (eigenvalues) của $e^{B}$ (xem Mục 15.5). Hơn nữa, với mọi $n \times  n$ ma trận quay (rotation matrix) $Q$ (ma trận trực giao (orthogonal matrix) $Q$ sao cho det(Q) $= 1)$, có một skew ma trận đối xứng (symmetric matrix) $B$ sao cho $Q = e^{B}$. Điều này là cơ bản tính chất mà có các ứng dụng trong rô-bốt học cho $n = 3$. Tất cả quen thuộc chuỗi có ma trận các tương tự. Ví dụ, nếu $\|A\| < 1$ (ở đâu $\|\|$ là toán tử
$$\infty$$
$$norm), then the series \sum_{k}  =0 A^{k}converges absolutely, and it can be shown that its limit is$$
(I - $A)^{-1}$. Một cái khác thú vị chuỗi là lôgarit. Với mọi $n \times  n$ phức ma trận $A$, nếu $\|A\| < 1$ (ở đâu $\|\|$ là chuẩn toán tử (operator norm)), thì chuỗi
$$\log(I + A) = \sum_{k=1}^{\infty}  (-1)^{k+1} \frac{A^{k}}{k}$$
Hội tụ một cách tuyệt đối.

## 9.9 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ Các chuẩn và các không gian vectơ định chuẩn. $\bullet$ tam giác bất đẳng thức.

<!-- PAGE 381 -->
$\bullet$ Euclidean chuẩn (norm); $\ell^{p}$ -các chuẩn. $\bullet$ H¨older’s bất đẳng thức; Cauchy–Schwarz bất đẳng thức; Minkowski’s bất đẳng thức. $\bullet$ Hermite tích vô hướng (inner product) và Euclidean tích vô hướng (inner product). $\bullet$ Tương đương các chuẩn. $\bullet$ Tất cả các chuẩn trên không gian vectơ hữu hạn chiều là tương đương (Định lý 9.6). $\bullet$ Các chuẩn ma trận. $\bullet$ Hermite, đối xứng và các ma trận chuẩn tắc. Trực giao và các ma trận unita. $\bullet$ vết (trace) của ma trận. $\bullet$ Các trị riêng (eigenvalues) và các vectơ riêng (eigenvectors) của ma trận. $\bullet$ đa thức đặc trưng (characteristic polynomial) của ma trận. $\bullet$ bán kính phổ (spectral radius) $\rho (A)$ của ma trận $A. \bullet$ Chuẩn Frobenius (Frobenius norm). $\bullet$ Chuẩn Frobenius (Frobenius norm) là unitarily bất biến chuẩn ma trận (matrix norm). $\bullet$ Bị chặn các ánh xạ tuyến tính (linear maps). $\bullet$ Phụ thuộc các chuẩn ma trận. $\bullet$ Đặc trưng của phụ thuộc các chuẩn ma trận cho các chuẩn vectơ $\|\|_{1} , \|\|_{2}$, và $\|\|_{\infty}. \bullet$ spectral chuẩn (norm). $\bullet$ Với mọi ma trận $A \in M_{n}(\mathbb{C})$ và với mọi $\epsilon  > 0$, tồn tại một chuẩn ma trận phụ thuộc (subordinate matrix norm) $\|\|$ sao cho $\|A\|\le \rho (A) + \epsilon$. $\bullet$ Điều kiện các số của các ma trận. $\bullet$ Perturbation giải tích/phân tích của các hệ phương trình tuyến tính. $\bullet$ phân rã giá trị kỳ dị (SVD) (SVD). $\bullet$ Các tính chất của các điều kiện các số. Đặc trưng của $cond_{2}(A)$ theo lớn nhất và nhỏ nhất các giá trị kỳ dị (singular values) của $A. \bullet$ Hilbert ma trận: rất một cách xấu được điều kiện ma trận. $\bullet$ Việc giải vô nghiệm/không tương thích các hệ phương trình tuyến tính bởi phương pháp của bình phương tối thiểu (least-squares); quy hoạch tuyến tính (linear programming).
