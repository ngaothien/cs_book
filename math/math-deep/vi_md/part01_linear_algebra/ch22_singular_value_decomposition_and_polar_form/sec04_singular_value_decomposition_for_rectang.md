# Phân rã giá trị kỳ dị (SVD) cho Rectangular Các ma trận


<!-- PAGE 759 -->
Nếu $A$ là phức $n \times  n$ ma trận, các trị riêng (eigenvalues) $\lambda_{1} , \dots  , \lambda_{n}$ và các giá trị kỳ dị (singular values) $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{n}$ của $A$ là không unrelated, vì
$$\sigma_{1}^{2}  \cdots  \sigma_{n}^{2}  = \det(A^{*}A) = | \det(A)|^{2}$$
Và
$$|\lambda_{1} | \cdots  |\lambda_{n} | = | \det(A)|,$$
Do đó ta có
$$|\lambda_{1} | \cdots  |\lambda_{n} | = \sigma_{1}  \cdots  \sigma_{n} .$$
Tổng quát hơn, Hermann Weyl được chứng minh sau đây đáng chú ý định lý:

> **Định lý 22.6.** (Weyl’s các bất đẳng thức, $1949)$ Với mọi phức $n\times n$ ma trận, $A$, nếu $\lambda_{1} , \dots  , \lambda_{n}  \in \mathbb{C}$ là các trị riêng (eigenvalues) của $A$ và $\sigma_{1} , \dots  , \sigma_{n}  \in \mathbb{R}_{+}$ là các giá trị kỳ dị (singular values) của $A$, được liệt kê sao cho $|\lambda_{1}$ | $\ge \cdots  \ge |\lambda_{n}$ | và $\sigma_{1}  \ge \cdots  \ge \sigma_{n}  \ge 0$, thì
$$|\lambda_{1} | \cdots  |\lambda_{n} | = \sigma_{1}  \cdots  \sigma_{n} and$$
$$|\lambda_{1} | \cdots  |\lambda_{k} | \le \sigma_{1}  \cdots  \sigma_{k} ,fork = 1, \dots  , n -1.$$
Chứng minh của Định lý 22.6 có thể được tìm thấy trong Horn và Johnson $[99]$, Chương $3$, Mục 3.3, ở đâu nhiều hơn/thêm các bất đẳng thức relating các trị riêng (eigenvalues) và các giá trị kỳ dị (singular values) của ma trận là cho trước. Định lý 22.5 có thể được dễ dàng được mở rộng đến rectangular $m \times  n$ các ma trận, như ta chỉ ra trong mục tiếp theo. Cho khác nhau các phiên bản của SVD cho rectangular các ma trận, xem Strang $[176]$ Golub và Van Loan $[83]$, Demmel $[48]$, và Trefethen và Bau $[182]$.

## 22.4 Phân rã giá trị kỳ dị (SVD) cho

$$Rectangular Matrices$$
Ở đây là tổng quát hóa của Định lý 22.5 đến rectangular các ma trận.

> **Định lý 22.7.** (Phân rã giá trị kỳ dị (SVD)) Với mọi thực $m \times  n$ ma trận $A$, có hai các ma trận trực giao $U (n\times n)$ và $V (m\times m)$ và đường chéo $m\times n$ ma trận $D$ sao cho $A = V D U^{\top}$, ở đâu $D$ là của tạo thành
$$D = \begin{pmatrix} \sigma_{1} & \dots \\ \sigma_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & \sigma_{n} \\ \vdots \\ 0 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ \vdots \\ 0 & \dots & 0 \end{pmatrix} or D = \begin{pmatrix} \sigma_{1} & \dots & 0 & \dots & 0 \\ \sigma_{2} & \dots & 0 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 \\ \dots & \sigma_{m} & 0 & \dots & 0 \end{pmatrix} ,$$

<!-- PAGE 760 -->
Ở đâu $\sigma_{1} , \dots  , \sigma_{r}$ là các giá trị kỳ dị (singular values) của $A$, i.e. (dương) square các nghiệm của khác không các trị riêng (eigenvalues) của $A^{\top}A$ và $A A^{\top}$, và $\sigma_{r+1}  = \dots  = \sigma_{p}  = 0$, ở đâu $p =$ min(m, $n)$. các cột của $U$ là các vectơ riêng (eigenvectors) của $A^{\top}A$, và các cột của $V$ là các vectơ riêng (eigenvectors) của $A A^{\top}$.

*Chứng minh.* Như trong chứng minh của Định lý 22.5, vì $A^{\top}A$ là đối xứng nửa xác định dương (positive semidefinite), tồn tại một $n \times  n$ ma trận trực giao (orthogonal matrix) $U$ sao cho
$$A^{\top}A = U\Sigma^{2} U^{\top} ,$$
Với $\Sigma  = diag(\sigma_{1} , \dots  , \sigma_{r} , 0, \dots  , 0)$, ở đâu $\sigma_{1}^{2} , \dots  , \sigma_{r}^{2}$ là khác không các trị riêng (eigenvalues) của $A^{\top}A$, và ở đâu $r$ là hạng (rank) của $A$. Nhận thấy rằng $r \le min{m, n}$, và AU là một ma trận cỡ $m \times  n$. Suy ra rằng
$$U^{\top} A^{\top}AU = (AU)^{\top}AU = \Sigma^{2} ,$$
$$\mathbb{R}^{m}$$
Và nếu ta cho $f_{j} \in$ là cột thứ $j$ của $AU$ cho $j = 1, \dots  , n$, thì ta có
$$\langle f_{i}, f_{j}\rangle = \sigma_{i}^{2}  \delta_{ij} ,1 \le i, j \le r$$
Và
$$f_{j} = 0,r + 1 \le j \le n.$$
Nếu ta định nghĩa $(v_{1}, \dots  , v_{r})$ bởi
$$v_{j} = \sigma_{j}^{-1}  f_{j},1 \le j \le r,$$
Thì ta có
$$\langle v_{i}, v_{j}\rangle = \delta_{ij} ,1 \le i, j \le r,$$
Do đó đầy đủ $(v_{1}, \dots  , v_{r})$ vào cơ sở trực chuẩn (orthonormal basis) $(v_{1}, \dots  , v_{r}, v_{r+1}, \dots  , v_{m})$ (ví dụ, bằng cách sử dụng Gram–Schmidt). Bây giờ vì $f_{j} = \sigma_{j} v_{j}$ cho $j = 1 \dots  , r$, ta có
$$\langle v_{i}, f_{j}\rangle = \sigma_{j} \langle v_{i}, v_{j}\rangle = \sigma_{j} \delta_{i,j} ,1 \le i \le m, 1 \le j \le r$$
Và vì $f_{j} = 0$ cho $j = r + 1, \dots  , n$, ta có
$$\langle v_{i}, f_{j}\rangle = 01 \le i \le m, r + 1 \le j \le n.$$
Nếu $V$ là ma trận có các cột là $v_{1}, \dots  , v_{m}$, thì $V$ là $m \times  m$ ma trận trực giao (orthogonal matrix) và nếu $m \ge n$, ta cho
$$D = \begin{pmatrix} \Sigma \\ 0_{m-n} \end{pmatrix} = \begin{pmatrix} \sigma_{1} & \dots \\ \sigma_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & \sigma_{n} \\ 0 & \vdots & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & \vdots & \dots & 0 \end{pmatrix} ,$$

<!-- PAGE 761 -->
Khác nếu $n \ge m$, thì ta cho
$$D = \begin{pmatrix} \sigma_{1} & \dots & 0 & \dots & 0 \\ \sigma_{2} & \dots & 0 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots & 0 & \vdots & 0 \\ \dots & \sigma_{m} & 0 & \dots & 0 \end{pmatrix} .$$
Trong hoặc trường hợp, ở trên các phương trình chứng minh rằng
$$V^{\top} AU = D,$$
Mà cho ta $A = V DU^{\top}$, như cần thiết. phương trình $A = V DU^{\top}$ suy ra rằng
$$A^{\top}A = UD^{\top}DU^{\top} = Udiag(\sigma_{1}^{2} , \dots  , \sigma_{r}^{2} , 0, \dots  , 0)U^{\top}$$
$$| {z }$$
$$n-r$$
Và
$$AA^{\top}= V DD^{\top}V^{\top} = V \mathrm{diag}(\sigma_{1}^{2} , \dots  , \sigma_{r}^{2} , 0, \dots  , 0)V^{\top} ,$$
$$| {z }$$
$$m-r$$
Mà chỉ ra rằng $A^{\top}A$ và $AA^{\top}$ có cùng khác không các trị riêng (eigenvalues), rằng các cột của $U$ là các vectơ riêng (eigenvectors) của $A^{\top}A$, và rằng các cột của $V$ là các vectơ riêng (eigenvectors) của $AA^{\top}$. bộ ba $(U, D, V$) sao cho $A = V D U^{\top}$ được gọi là một phân rã giá trị kỳ dị (SVD) (SVD) của $A$. Nếu $D = diag(\sigma_{1} , \dots  , \sigma_{p}$) (với $p =$ min(m, $n))$, nó là thông lệ giả sử rằng $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{p}$.
$$Example 22.7. Let A = \begin{pmatrix} 1 & 1 \\ 0 & 0 \\ 0 & 0 \end{pmatrix} . Then A^{\top}= \begin{pmatrix} 1 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix} A^{\top}A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} , and AA^{\top}=$$
$$\begin{pmatrix} 2 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} .The reader should verify that A^{\top}A = U\Sigma^{2} U^{\top} where \Sigma^{2}  = \begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix} and$$
$$U = U^{\top} = \begin{pmatrix} \sqrt & \sqrt \\ 1/\sqrt{2} & 1/\sqrt{2} \\ 1/ & 2 & -1/ & 2 \end{pmatrix} . Since AU = \begin{pmatrix} \sqrt \\ \overline{2} & 0 \\ 0 & 0 \\ 0 & 0 \end{pmatrix} , set v_{1} =_{2}^{\sqrt1} \begin{pmatrix} \sqrt \\ \overline{2} \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} ,$$
$$and complete an orthonormal basis for \mathbb{R}^{3} by assigning v_{2} = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} , and v_{3} = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} . Thus$$
$$V = I_{3}, and the reader should verify that A = V DU^{\top} , where D = \begin{pmatrix} \sqrt \\ \overline{2} & 0 \\ 0 & 0 \\ 0 & 0 \end{pmatrix} .$$

<!-- PAGE 762 -->
Chẵn/ngay cả dù ma trận $D$ là $m \times  n$ rectangular ma trận, vì của nó chỉ khác không các phần tử (entries) là trên descending đường chéo, ta vẫn nói rằng $D$ là ma trận đường chéo (diagonal matrix). Matlab command cho việc tính toán SVD $A = V DU^{\top}$ của ma trận $A$ là $[V, D, U] =$ svd(). Beware rằng Matlab sử dụng quy ước rằng SVD của ma trận $A$ được viết như $A = UDV^{\top}$, và do đó gọi cho điều này phiên bản của SVD là $[U, D, V] =$ svd(). Nếu ta quan điểm $A$ như biểu diễn của ánh xạ tuyến tính (linear map) $f$: $E \to F$, ở đâu dim(E) $= n$ và dim(F) $= m$, chứng minh của Định lý 22.7 chỉ ra rằng có hai các cơ sở trực chuẩn $(u_{1}, \dots , u_{n})$ và $(v_{1}, \dots  , v_{m})$ cho $E$ và $F$, respectively, ở đâu $(u_{1}, \dots  , u_{n})$ là các vectơ riêng (eigenvectors) của $f^{*} \circ f$ và $(v_{1}, \dots  , v_{m})$ là các vectơ riêng (eigenvectors) của $f \circ f^{*}$. Hơn nữa, $(u_{1}, \dots  , u_{r})$ là cơ sở trực chuẩn (orthonormal basis) của Im $f^{*} , (u_{r+1}, \dots  , u_{n})$ là cơ sở trực chuẩn (orthonormal basis) của Ker $f, (v_{1}, \dots  , v_{r})$ là cơ sở trực chuẩn (orthonormal basis) của Im $f$, và $(v_{r+1}, \dots  , v_{m})$ là cơ sở trực chuẩn (orthonormal basis) của Ker $f^{*}$. SVD của các ma trận có thể được được sử dụng để định nghĩa nghịch đảo giả (pseudo-inverse) của rectangular ma trận; ta sẽ thực hiện do đó trong Chương $23$. độc giả có thể cũng consult Strang $[176]$, Demmel $[48]$, Trefethen và Bau $[182]$, và Golub và Van Loan $[83]$. Một của các định lý phổ phát biểu rằng ma trận đối xứng (symmetric matrix) có thể được được chéo hóa bởi ma trận trực giao (orthogonal matrix). Có một vài số các phương pháp để tính các trị riêng (eigenvalues) của ma trận đối xứng (symmetric matrix) $A$. Một phương pháp bao gồm trong tridiagonalizing $A$, mà có nghĩa là tồn tại một ma trận trực giao (orthogonal matrix) $P$ và một số đối xứng ma trận ba đường chéo (tridiagonal matrix) $T$ sao cho $A = PTP^{\top}$. Thực ra, điều này có thể được được thực hiện bằng cách sử dụng Householder các phép biến đổi; xem Định lý 18.2. Nó là thì khả dĩ/có thể để tính các trị riêng (eigenvalues) của $T$ bằng cách sử dụng bisection phương pháp based trên Sturm các dãy. Một có thể cũng sử dụng Jacobi’s phương pháp. Cho chi tiết, xem Golub và Van Loan $[83]$, Chương $8$, Demmel $[48]$, Trefethen và Bau $[182]$, Lecture $26$, Ciarlet $[41]$, và Chương $18$. Việc tính toán SVD của ma trận $A$ là nhiều hơn/thêm liên quan. Hầu hết các phương pháp bắt đầu bởi việc tìm các ma trận trực giao $U$ và $V$ và bidiagonal ma trận $B$ sao cho $A = V BU^{\top}$; xem Bài toán 13.8 và Bài toán 22.3. Điều này có thể cũng được thực hiện bằng cách sử dụng Householder các phép biến đổi. Nhận thấy rằng $B^{\top}B$ là đối xứng ba đường chéo. Do đó, trong nguyên lý, trước đó phương pháp đến diagonalize đối xứng ma trận ba đường chéo (tridiagonal matrix) có thể được ứng dụng. Tuy nhiên, nó là unwise để tính $B^{\top}B$ một cách tường minh, và nhiều hơn/thêm tinh tế các phương pháp được sử dụng cho điều này bước cuối cùng; ma trận của Bài toán 22.1 có thể được được sử dụng, và xem Bài toán 22.3. Một lần nữa, xem Golub và Van Loan $[83]$, Chương $8$, Demmel $[48]$, và Trefethen và Bau $[182]$, Lecture $31$. dạng cực (polar form) có các ứng dụng trong continuum cơ học. Thật vậy, trong bất kỳ deformation nó là quan trọng đến tách stretching từ phép quay. Điều này là chính xác những gì QS đạt được. trực giao phần $Q$ tương ứng với phép quay (perhaps với additional phép đối xứng (reflection)), và ma trận đối xứng (symmetric matrix) $S$ đến stretching (hoặc compression). thực các trị riêng (eigenvalues) $\sigma_{1} , \dots  , \sigma_{r}$ của $S$ là stretch các nhân tử (hoặc compression các nhân tử) (xem Marsden và Hughes $[124])$. sự kiện rằng $S$ có thể được được chéo hóa bởi ma trận trực giao (orthogonal matrix) tương ứng với tự nhiên lựa chọn của các trục, chính các trục. SVD có các ứng dụng đến dữ liệu compression, chẳng hạn trong ảnh (image) processing. ý tưởng là đến retain chỉ các giá trị kỳ dị (singular values) có magnitudes là đáng kể đủ. SVD
