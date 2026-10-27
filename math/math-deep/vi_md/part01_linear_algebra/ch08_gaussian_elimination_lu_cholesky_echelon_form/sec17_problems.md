# Các bài tập


<!-- PAGE 326 -->
$\bullet$ tránh nhỏ các phần tử trụ: riêng chọn phần tử trụ; đầy đủ chọn phần tử trụ. $\bullet$ Phép khử Gauss (Gaussian elimination) của ba đường chéo các ma trận. $\bullet$ Nhân tử hóa LU (LU-factorization) của ba đường chéo các ma trận. $\bullet$ Đối xứng xác định dương (SPD) các ma trận $(SPD$ các ma trận). $\bullet$ Nhân tử hóa Cholesky (Cholesky factorization) (Định lý 8.10). $\bullet$ Các tiêu chuẩn cho ma trận đối xứng (symmetric matrix) là xác định dương (positive definite); Sylvester’s tiêu chuẩn. $\bullet$ Dạng bậc thang rút gọn theo hàng (RREF). $\bullet$ Reduction của rectangular ma trận đến của nó dạng bậc thang theo hàng (row echelon form). $\bullet$ Bằng cách sử dụng reduction đến dạng bậc thang theo hàng (row echelon form) đến decide liệu hệ Ax $= b$ là giải được, và để tìm các nghiệm của nó, bằng cách sử dụng đặc biệt nghiệm và cơ sở (basis) của thuần nhất hệ Ax $= 0. \bullet$ Magic squares. $\bullet$ Các phép trượt và các phép vị tự.

## 8.17 Các bài tập

Bài toán 8.1. Giải sau đây các hệ phương trình tuyến tính bởi Phép khử Gauss (Gaussian elimination):
$$\begin{pmatrix} 2 & 3 & 1 \\ 1 & 2 & -1 \\ 3 & 5 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 6 \\ 2 \\ 7 \end{pmatrix} , \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 2 \\ 1 & 2 & 3 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 6 \\ 9 \\ 14 \end{pmatrix} .$$
$$---$$
Bài toán 8.2. Giải sau đây hệ phương trình tuyến tính bởi Phép khử Gauss (Gaussian elimination):
$$\begin{pmatrix} 1 & 2 & 1 & 1 \\ 2 & 3 & 2 & 3 \\ -1 & 0 & 1 & -1 \\ 2 & 1 & 4 & 0 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \\ x_{4} \end{pmatrix} = \begin{pmatrix} 7 \\ 14 \\ -1 \\ 2 \end{pmatrix} .$$
$$--$$
Bài toán 8.3. Xét ma trận
$$A = \begin{pmatrix} 1 & c & 0 \\ 2 & 4 & 1 \\ 3 & 5 & 1 \end{pmatrix} .$$
Khi áp dụng Phép khử Gauss (Gaussian elimination), mà giá trị của $c$ cho ta không trong thứ hai phần tử trụ (pivot) position? Mà giá trị của $c$ cho ta không trong thứ ba phần tử trụ (pivot) position? Trong trường hợp này, những gì có thể bạn nói về ma trận $A$?

<!-- PAGE 327 -->
Bài toán 8.4. Giải hệ
$$\begin{pmatrix} 2 & 1 & 1 & 0 \\ 4 & 3 & 3 & 1 \\ 8 & 7 & 9 & 5 \\ 6 & 7 & 9 & 8 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \\ x_{4} \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ -1 \\ 1 \end{pmatrix}$$
Bằng cách sử dụng Nhân tử hóa LU (LU-factorization) của Ví dụ 8.1.
Bài toán 8.5. Áp dụng rref đến ma trận
$$A_{2} = \begin{pmatrix} 1 & 2 & 1 & 1 \\ 2 & 3 & 2 & 3 \\ -1 & 0 & 1 & -1 \\ 2 & 1 & 3 & 0 \end{pmatrix} .$$
$$--$$
Bài toán 8.6. Áp dụng rref đến ma trận
$$\begin{pmatrix} 1 & 4 & 9 & 16 \\ 4 & 9 & 16 & 25 \\ 9 & 16 & 25 & 36 \\ 16 & 25 & 36 & 49 \end{pmatrix} .$$
Bài toán 8.7. $(1)$ Chứng minh rằng số chiều của không gian con của $2 \times  2$ các ma trận $A$, sao cho tổng của các phần tử (entries) của mọi hàng là cùng (nói $c_{1})$ và tổng của các phần tử (entries) của mọi cột là cùng (nói $c_{2})$ là $2$.
$(2)$ Chứng minh rằng số chiều của không gian con của $2 \times  2$ các ma trận $A$, sao cho tổng của các phần tử (entries) của mọi hàng là cùng (nói $c_{1})$, tổng của các phần tử (entries) của mọi cột là cùng (nói $c_{2})$, và $c_{1} = c_{2}$ là cũng $2$. Chứng minh rằng mọi như vậy ma trận là của tạo thành
$$\begin{pmatrix} a & b \\ b & a \end{pmatrix} ,$$
Và cho cơ sở (basis) cho không gian con này.
$(3)$ Chứng minh rằng số chiều của không gian con của $3 \times  3$ các ma trận $A$, sao cho tổng của các phần tử (entries) của mọi hàng là cùng (nói $c_{1})$, tổng của các phần tử (entries) của mọi cột là cùng (nói $c_{2})$, và $c_{1} = c_{2}$ là $5$. Bắt đầu bởi chỉ ra rằng ở trên các ràng buộc được cho bởi tập hợp của các phương trình
$$\begin{pmatrix} 1 & 1 & 1 & -1 & -1 & -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 1 & 1 & -1 & -1 & -1 \\ 1 & -1 & 0 & 1 & -1 & 0 & 1 & -1 & 0 \\ 0 & 1 & -1 & 0 & 1 & -1 & 0 & 1 & -1 \\ 0 & 1 & 1 & 1 & 0 & 0 & 1 & 0 & 0 \end{pmatrix} \begin{pmatrix} a_{11} \\ a_{12} \\ a_{13} \\ a_{21} \\ a_{22} \\ a_{23} \\ a_{31} \\ a_{32} \\ a_{33} \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} .$$
$$--$$

<!-- PAGE 328 -->
Chứng minh rằng mọi ma trận thỏa mãn ở trên các ràng buộc là của tạo thành
$$\begin{pmatrix} a + b -c & -a + c + e & -b + c + d \\ -a -b + c + d + e & a & b \\ c & d & e \end{pmatrix} ,$$
Với, $b, c, d, e \in \mathbb{R}$. Tìm cơ sở (basis) cho không gian con này. (Sử dụng phương pháp để tìm cơ sở (basis) cho hạt nhân (kernel) của ma trận).
Bài toán 8.8. Nếu $A$ là một ma trận cỡ $n \times  n$ và $B$ là bất kỳ $n \times  n$ ma trận khả nghịch (invertible matrix), chứng minh rằng $A$ là đối xứng xác định dương (SPD) khi và chỉ khi $B^{\top}AB$ là đối xứng xác định dương (SPD).
Bài toán 8.9. $(1)$ Xét ma trận
$$A_{4} = \begin{pmatrix} 2 & -1 & 0 & 0 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ 0 & 0 & 1 & 2 \end{pmatrix} .$$
$$-$$
Tìm ba các ma trận của tạo thành $E_{2,1;\beta1}, E_{3,2;\beta2}, E_{4,3;\beta3}$, sao cho
$$E_{4,3;\beta3}E_{3,2;\beta2}E_{2,1;\beta1}A_{4} = U_{4}$$
Ở đâu $U_{4}$ là tam giác trên (upper triangular) ma trận. Tính
$$M = E_{4,3;\beta3}E_{3,2;\beta2}E_{2,1;\beta1}$$
Và kiểm tra rằng
$$MA_{4} = U_{4} = \begin{pmatrix} 2 & -1 & 0 & 0 \\ 0 & 3/2 & -1 & 0 \\ 0 & 0 & 4/3 & -1 \\ 0 & 0 & 0 & 5/4 \end{pmatrix} .$$
$(2)$ Bây giờ xét ma trận
$$A_{5} = \begin{pmatrix} 2 & -1 & 0 & 0 & 0 \\ -1 & 2 & -1 & 0 & 0 \\ 0 & -1 & 2 & -1 & 0 \\ 0 & 0 & -1 & 2 & -1 \\ 0 & 0 & 0 & 1 & 2 \end{pmatrix} .$$
$$-$$
Tìm bốn các ma trận của tạo thành $E_{2,1;\beta1}, E_{3,2;\beta2}, E_{4,3;\beta3}, E_{5,4;\beta4}$, sao cho
$$E_{5,4;\beta4}E_{4,3;\beta3}E_{3,2;\beta2}E_{2,1;\beta1}A_{5} = U_{5}$$
Ở đâu $U_{5}$ là tam giác trên (upper triangular) ma trận. Tính
$$M = E_{5,4;\beta4}E_{4,3;\beta3}E_{3,2;\beta2}E_{2,1;\beta1}$$

<!-- PAGE 329 -->
Và kiểm tra rằng
$$MA_{5} = U_{5} = \begin{pmatrix} 2 & -1 & 0 & 0 & 0 \\ 0 & 3/2 & -1 & 0 & 0 \\ 0 & 0 & 4/3 & -1 & 0 \\ 0 & 0 & 0 & 5/4 & -1 \\ 0 & 0 & 0 & 0 & 6/5 \end{pmatrix} .$$
$(3)$ Viết Matlab bài toán quy hoạch định nghĩa hàm Ematrix(n, $i, j, b)$ mà là ma trận cỡ $n \times  n$ rằng cộng $b$ lần hàng $j$ đến hàng $i$. Cũng viết một số Matlab code rằng produces một ma trận cỡ $n \times  n$ $A_{n}$ generalizing các ma trận $A_{4}$ và $A_{5}$. Sử dụng của bạn bài toán quy hoạch đến hình ra mà năm các ma trận $E_{i,j;\beta}$ rút gọn $A_{6}$ đến tam giác trên (upper triangular) ma trận
$$U_{6} = \begin{pmatrix} 2 & -1 & 0 & 0 & 0 & 0 \\ 0 & 3/2 & -1 & 0 & 0 & 0 \\ 0 & 0 & 4/3 & -1 & 0 & 0 \\ 0 & 0 & 0 & 5/4 & -1 & 0 \\ 0 & 0 & 0 & 0 & 6/5 & -1 \\ 0 & 0 & 0 & 0 & 0 & 7/6 \end{pmatrix} .$$
Cũng sử dụng của bạn bài toán quy hoạch đến hình ra mà sáu các ma trận $E_{i,j;\beta}$ rút gọn $A_{7}$ đến tam giác trên (upper triangular) ma trận
$$U_{7} = \begin{pmatrix} 2 & -1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 3/2 & -1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 4/3 & -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 5/4 & -1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 6/5 & -1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 7/6 & -1 \\ 0 & 0 & 0 & 0 & 0 & 0 & 8/7 \end{pmatrix} .$$
$(4)$ Tìm tam giác dưới (lower triangular) các ma trận $L_{6}$ và $L_{7}$ sao cho
$$L_{6}U_{6} = A_{6}$$
Và
$$L_{7}U_{7} = A_{7}.$$
$(5)$ Nó là tự nhiên đến giả thuyết rằng có $n -1$ các ma trận của tạo thành $E_{i,j;\beta}$ rằng rút gọn $A_{n}$ đến tam giác trên (upper triangular) ma trận
$$U_{n} = \begin{pmatrix} 2 & -1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 3/2 & -1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 4/3 & -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 5/4 & -1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 6/5 & \ddots & \vdots \\ \vdots & \vdots & \vdots & \vdots & \ddots & \ddots & -1 \\ 0 & 0 & 0 & 0 & 0 & (n + 1)/n \end{pmatrix} ,$$
$$\cdots$$

<!-- PAGE 330 -->
Cụ thể là,
$$E_{2,1;1/2}, E_{3,2;2/3}, E_{4,3;3/4}, \cdots  , E_{n,n-1;(n-1)/n}.$$
Nó là cũng tự nhiên đến giả thuyết rằng tam giác dưới (lower triangular) ma trận $L_{n}$ sao cho
$$L_{n}U_{n} = A_{n}$$
Được cho bởi
$$L_{n} = E_{2,1;-1/2}E_{3,2;-2/3}E_{4,3;-3/4} \cdots  E_{n,n-1;-(n-1)/n},$$
Rằng là,
$$L_{n} = \begin{pmatrix} 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ -1/2 & 1 & 0 & 0 & 0 & 0 & 0 \\ 0 & -2/3 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & -3/4 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & -4/5 & 1 & \ddots & \vdots \\ \vdots & \vdots & \vdots & \vdots & \ddots & \ddots & 0 \\ 0 & 0 & 0 & 0 & (n & 1)/n & 1 \end{pmatrix} .$$
$$\cdots - -$$
Chứng minh ở trên các giả thuyết.
$(6)$ Chứng minh rằng cột cuối cùng của $A_{n}^{-1}$ là
$$\begin{pmatrix} 1/(n + 1) \\ 2/(n + 1) \\ \vdots \\ n/(n + 1) \end{pmatrix} .$$
Bài toán 8.10. $(1)$ Cho $A$ là bất kỳ khả nghịch $2 \times  2$ ma trận
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} .$$
Chứng minh rằng có một ma trận khả nghịch (invertible matrix) $S$ sao cho
$$SA = \begin{pmatrix} 1 & 0 \\ 0 & ad -bc \end{pmatrix} ,$$
Ở đâu $S$ là tích của nhiều nhất bốn sơ cấp các ma trận của tạo thành $E_{i,j;\beta}$. Kết luận rằng mọi ma trận $A$ trong SL(2) (nhóm của khả nghịch $2 \times  2$ các ma trận $A$ với det() $= +1)$ là tích của nhiều nhất bốn sơ cấp các ma trận của tạo thành $E_{i,j;\beta}$. Với mọi $a \neq  0, 1$, cho tường minh nhân tử hóa như ở trên cho
$$A = \begin{pmatrix} a & 0 \\ 0 & a^{-1} \end{pmatrix} .$$

<!-- PAGE 331 -->
Những gì là phân rã này cho $a = -1$?
$(2)$ Nhắc lại rằng ma trận quay (rotation matrix) $R$ (member của nhóm Do đó(2)) là ma trận của tạo thành
$$R = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} .$$
Chứng minh rằng nếu $\theta  \neq  k\pi$ (với $k \in \mathbb{Z})$, bất kỳ ma trận quay (rotation matrix) có thể được viết dưới dạng tích
$$R = ULU,$$
Ở đâu $U$ là tam giác trên (upper triangular) và $L$ là tam giác dưới (lower triangular) của tạo thành
$$U = \begin{pmatrix} 1 & u \\ 0 & 1 \end{pmatrix} ,L = \begin{pmatrix} 1 & 0 \\ v & 1 \end{pmatrix} .$$
Vì vậy, mọi mặt phẳng phép quay (ngoại trừ flip về gốc khi $\theta  = \pi$) có thể được viết dưới dạng hợp thành của ba shear các phép biến đổi!
Bài toán 8.11. $(1)$ Nhắc lại rằng $E_{i,d}$ là ma trận đường chéo (diagonal matrix)
$$E_{i,d} = \mathrm{diag}(1, \dots  , 1, d, 1, \dots  , 1),$$
Có đường chéo các phần tử (entries) là tất cả $+1$, ngoại trừ $(i$, i)th phần tử (entry) mà bằng $d$. Cho trước bất kỳ ma trận cỡ $n \times  n$ $A$, với mọi cặp $(i, j)$ của phân biệt hàng các chỉ số $(1 \le i, j \le n)$, chứng minh rằng ở đó tồn tại hai sơ cấp các ma trận $E_{1}(i, j)$ và $E_{2}(i, j)$ của tạo thành $E_{k,\ell;\beta}$, sao cho
$$E_{j,-1}E_{1}(i, j)E_{2}(i, j)E_{1}(i, j)A = P(i, j)A,$$
Ma trận thu được từ ma trận $A$ bởi hoán vị hàng $i$ và hàng $j$. Tương đương, ta có
$$E_{1}(i, j)E_{2}(i, j)E_{1}(i, j)A = E_{j,-1}P(i, j)A,$$
Ma trận thu được từ $A$ bởi hoán vị hàng $i$ và hàng $j$ và nhân hàng $j$ bởi $-1$. Chứng minh rằng với mọi $i = 2, \dots  , n$, ở đó tồn tại bốn sơ cấp các ma trận $E_{3}(i, d), E_{4}(i, d), E_{5}(i, d), E_{6}(i, d)$ của tạo thành $E_{k,\ell;\beta}$, sao cho
$$E_{6}(i, d)E_{5}(i, d)E_{4}(i, d)E_{3}(i, d)E_{n,d} = E_{i,d}.$$
Những gì xảy ra khi $d = -1$, nghĩa là, những gì loại của simplifications xảy ra? Chứng minh rằng tất cả hoán vị các ma trận có thể được viết dưới dạng các tích của sơ cấp các phép toán của tạo thành $E_{k,\ell;\beta}$ và phép toán $E_{n,-1}$.
$(2)$ Chứng minh rằng với mọi khả nghịch $n \times  n$ ma trận $A$, có một ma trận $S$ sao cho
$$SA = \begin{pmatrix} I_{n-1} & 0 \\ 0 & d \end{pmatrix} = E_{n,d},$$

<!-- PAGE 332 -->
Với $d =$ det(), và ở đâu $S$ là tích của sơ cấp các ma trận của tạo thành $E_{k,\ell;\beta}$. Đặc biệt, mọi ma trận trong SL(n) (nhóm của khả nghịch $n \times  n$ các ma trận $A$ với det() $= +1)$ có thể được viết dưới dạng tích của sơ cấp các ma trận của tạo thành $E_{k,\ell;\beta}$. Chứng minh rằng nhiều nhất n(n $+ 1)$ - $2$ như vậy các phép biến đổi là cần thiết.
$(3)$ Chứng minh rằng mọi ma trận trong SL(n) có thể được viết dưới dạng tích của nhiều nhất $(n$ - $1)(max{n, 3} + 1)$ sơ cấp các ma trận của tạo thành $E_{k,\ell;\beta}$.
Bài toán 8.12. ma trận $A$ được gọi là chặt cột một cách đường chéo trội khi và chỉ khi
$$|a_{j j}| > \sum_{=1, i\neq j}^{n}  |a_{i j}|,for j = 1, \dots  , n.$$
$$i$$
Chứng minh rằng nếu $A$ là chặt cột một cách đường chéo trội, thì Phép khử Gauss (Gaussian elimination) với riêng chọn phần tử trụ thực hiện không đòi hỏi chọn phần tử trụ, và $A$ là khả nghịch.
Bài toán 8.13. $(1)$ Tìm tam giác dưới (lower triangular) ma trận $E$ sao cho
$$E \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 2 & 1 & 0 \\ 1 & 3 & 3 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 1 & 2 & 1 \end{pmatrix} .$$
$(2)$ Những gì là effect của tích (trên trái) với
$$E_{4,3;-1}E_{3,2;-1}E_{4,3;-1}E_{2,1;-1}E_{3,2;-1}E_{4,3;-1}$$
Trên ma trận
$$Pa_{3} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 2 & 1 & 0 \\ 1 & 3 & 3 & 1 \end{pmatrix} .$$
$(3)$ Tìm nghịch đảo của ma trận $Pa_{3}$.
$(4)$ Xét $(n + 1) \times  (n + 1)$ Pascal ma trận $Pa_{n}$ có hàng thứ $i$ được cho bởi nhị thức các hệ số
$$\begin{pmatrix} i -1 \\ j -1 \end{pmatrix} ,$$
Với $1 \le i \le n + 1, 1 \le j \le n + 1$, và với thông thường quy ước rằng
$$\begin{pmatrix} 0 \\ 0 \end{pmatrix} = 1, \begin{pmatrix} i \\ j \end{pmatrix} = 0ifj > i.$$

<!-- PAGE 333 -->
Ma trận $Pa_{3}$ được hiển thị trong Phần $(3)$ và $Pa_{4}$ được hiển thị dưới đây:
$$Pa_{4} = \begin{pmatrix} 1 & 0 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 & 0 \\ 1 & 2 & 1 & 0 & 0 \\ 1 & 3 & 3 & 1 & 0 \\ 1 & 4 & 6 & 4 & 1 \end{pmatrix} .$$
Tìm $n$ sơ cấp các ma trận $E_{ik,jk;\beta k}$ sao cho
$$E_{in,jn;\beta n} \cdots  E_{i1,j1;\beta1}Pa_{n} = \begin{pmatrix} 1 & 0 \\ 0 & Pa_{n-1} \end{pmatrix} .$$
Sử dụng ở trên để chứng minh rằng nghịch đảo của $Pa_{n}$ là tam giác dưới (lower triangular) ma trận có hàng thứ $i$ được cho bởi được dấu nhị thức các hệ số
$$(-1)^{i+j-2} \begin{pmatrix} i -1 \\ j -1 \end{pmatrix} = (-1)^{i+j} \begin{pmatrix} i -1 \\ j -1 \end{pmatrix} ,$$
Với $1 \le i \le n + 1, 1 \le j \le n + 1$. Ví dụ,
$$Pa_{4}^{-1}= \begin{pmatrix} 1 & 0 & 0 & 0 & 0 \\ -1 & 1 & 0 & 0 & 0 \\ 1 & -2 & 1 & 0 & 0 \\ -1 & 3 & -3 & 1 & 0 \\ 1 & 4 & 6 & 4 & 1 \end{pmatrix} .$$
$$--$$
Hint. Cho trước bất kỳ ma trận cỡ $n \times  n$ $A$, nhân $A$ bởi sơ cấp ma trận $E_{i,j;\beta}$ trên phải cho ta ma trận $AE_{i,j;\beta}$ trong mà $\beta$ lần cột thứ $i$ được cộng đến cột thứ $j$.
Bài toán 8.14. $(1)$ Cài đặt phương pháp cho chuyển đổi rectangular ma trận đến dạng bậc thang rút gọn theo hàng (RREF) trong Matlab.
$(2)$ Sử dụng ở trên phương pháp để tìm nghịch đảo của khả nghịch $n \times  n$ ma trận $A$ bằng cách áp dụng nó đến $n \times$ 2n ma trận $[A$ I] thu được bằng cách cộng $n$ các cột của ma trận đơn vị (identity matrix) đến $A$.
$(3)$ Xét ma trận
$$A = \begin{pmatrix} 1 & 2 & 3 & 4 & \cdots & n \\ 2 & 3 & 4 & 5 & \cdots & n + 1 \\ 3 & 4 & 5 & 6 & \cdots & n + 2 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ n & n + 1 & n + 2 & n + 3 & \cdots & 2n -1 \end{pmatrix} .$$
Bằng cách sử dụng của bạn bài toán quy hoạch, tìm hàng rút gọn bậc thang tạo thành của $A$ cho $n = 4, \dots  , 20$.

<!-- PAGE 334 -->
Cũng chạy Matlab rref hàm và compare các kết quả. Của bạn bài toán quy hoạch probably disagrees với rref chẵn/ngay cả cho nhỏ các giá trị của $n$. bài toán là rằng một số các phần tử trụ là rất nhỏ và normalization bước (để tạo phần tử trụ (pivot) $1)$ gây ra roundofferrors. Sử dụng tolerance tham số đến fix bài toán này. Những gì có thể bạn giả thuyết về hạng (rank) của $A$?
$(4)$ Chứng minh rằng ma trận $A$ có sau đây hàng rút gọn tạo thành:
$$R = \begin{pmatrix} 1 & 0 & -1 & -2 & \cdots & -(n -2) \\ 0 & 1 & 2 & 3 & \cdots & n -1 \\ 0 & 0 & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & 0 & \cdots & 0 \end{pmatrix} .$$
Suy ra từ ở trên rằng $A$ có hạng (rank) $2$. Hint. Một số tốt được chọn dãy của hàng các phép toán.
$(5)$ Sử dụng của bạn bài toán quy hoạch để chỉ ra rằng nếu bạn cộng bất kỳ số greater hơn hoặc bằng $(2/25)n^{2}$ đến mọi đường chéo phần tử (entry) của $A$ bạn thu được ma trận khả nghịch (invertible matrix)! Thực ra, chạy Matlab hàm chol nên cho biết bạn rằng các ma trận này là SPD (đối xứng, xác định dương (positive definite)).
Bài toán 8.15. Cho $A$ là $n \times  n$ phức Hermite xác định dương (positive definite) ma trận. Chứng minh rằng tam giác dưới (lower-triangular) ma trận $B$ với dương đường chéo các phần tử (entries) sao cho $A = BB^{*}$ được cho bởi sau đây các công thức: Cho $j = 1, \dots  , n$,
$$1/2$$
$$!$$
$$b_{j j} =a_{j j} - \sum_{k=1}^{j-1}  |b_{j k}|^{2},$$
Và cho $i = j + 1, \dots  , n$ (và $j = 1, \dots  , n$ - $1)$
$$!$$
$$\overline{b}_{i j} =a_{i j} - \sum_{k=1}^{j-1}  b_{i k}\overline{b}_{j k}/b_{j j}.$$
Bài toán 8.16. (Các hoán vị và hoán vị các ma trận) $A$ hoán vị có thể được được quan điểm như phép toán hoán vị các hàng của ma trận. Ví dụ, hoán vị
$$\begin{pmatrix} 1 & 2 & 3 & 4 \\ 3 & 4 & 2 & 1 \end{pmatrix}$$
Tương ứng với ma trận
$$P_{\pi} = \begin{pmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix} .$$

<!-- PAGE 335 -->
Nhận thấy rằng ma trận $P_{\pi}$ có đơn lẻ $1$ trên mọi hàng và mọi cột, tất cả khác các phần tử (entries) đang là không, và rằng nếu ta nhân bất kỳ ma trận cỡ $4 \times  4$ $A$ bởi $P_{\pi}$ trên trái, thì các hàng của $A$ là permuted theo hoán vị $\pi$; rằng là, $\pi$ (i)th hàng của $P_{\pi}A$ là hàng thứ $i$ của $A$. Ví dụ,
$$P_{\pi}A = \begin{pmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix} \begin{pmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{41} & a_{42} & a_{43} & a_{44} \end{pmatrix} = \begin{pmatrix} a_{41} & a_{42} & a_{43} & a_{44} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \end{pmatrix} .$$
Tương đương, hàng thứ $i$ của $P_{\pi}A$ là $\pi^{-1}$ (i)th hàng của $A$. Trong thứ tự cho ma trận $P_{\pi}$ đến di chuyển hàng thứ $i$ của $A$ đến $\pi$ (i)th hàng, $\pi$ (i)th hàng của $P_{\pi}$ phải có $1$ trong cột $i$ và các không điểm ở mọi nơi khác; điều này có nghĩa là cột thứ $i$ của $P_{\pi}$ chứa cơ sở (basis) vectơ $e_{\pi(i)}$, vectơ rằng có $1$ trong position $\pi (i)$ và các không điểm ở mọi nơi khác. Điều này là tổng quát tình huống và nó dẫn đến đến sau đây định nghĩa.

> **Định nghĩa 8.10.** Cho trước bất kỳ hoán vị $\pi$: $[n] \to [n]$, hoán vị ma trận $P_{\pi} = (p_{ij})$ biểu diễn $\pi$ là ma trận cho trước bởi
$$($$
$$1if i = \pi (j)$$
$$p_{ij} =$$
$$0if i \neq  \pi (j);$$
Tương đương, cột thứ $j$ của $P_{\pi}$ là cơ sở (basis) vectơ $e_{\pi(j)}$. hoán vị ma trận $P$ là bất kỳ ma trận của tạo thành $P_{\pi}$ (ở đâu $P$ là một ma trận cỡ $n \times  n$, và $\pi$: $[n] \to [n]$ là hoán vị, với một số $n \ge 1)$.
Nhận xét: Có một confusing điểm về ký hiệu cho hoán vị các ma trận. hoán vị ma trận $P$ acts trên ma trận $A$ bởi phép nhân trên trái bởi hoán vị các hàng của $A$. Như ta được nói trước, điều này có nghĩa là $\pi$ (i)th hàng của $P_{\pi}A$ là hàng thứ $i$ của $A$, hoặc tương đương rằng hàng thứ $i$ của $P_{\pi}A$ là $\pi^{-1}$ (i)th hàng của $A$. Nhưng khi đó nhận thấy rằng hàng chỉ số của các phần tử (entries) của hàng thứ $i$ của $PA$ là $\pi^{-1} (i)$, và không $\pi (i)$! Xem sau đây ví dụ:
$$\begin{pmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix} \begin{pmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{41} & a_{42} & a_{43} & a_{44} \end{pmatrix} = \begin{pmatrix} a_{41} & a_{42} & a_{43} & a_{44} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \end{pmatrix} ,$$
Ở đâu
$$\pi^{-1} (1) = 4$$
$$\pi^{-1} (2) = 3$$
$$\pi^{-1} (3) = 1$$
$$\pi^{-1} (4) = 2.$$
Chứng minh sau đây các kết quả

<!-- PAGE 336 -->
$(1)$ Cho trước bất kỳ hai các hoán vị $\pi_{1} , \pi_{2}$: $[n] \to [n]$, hoán vị ma trận $P_{\pi2\circ\pi1}$ biểu diễn hợp thành của $\pi_{1}$ và $\pi_{2}$ bằng tích $P_{\pi2}P_{\pi1}$ của hoán vị các ma trận $P_{\pi1}$ và $P_{\pi2}$ biểu diễn $\pi_{1}$ và $\pi_{2}$; rằng là,
$$P_{\pi2\circ\pi1} = P_{\pi2}P_{\pi1}.$$
$(2)$ ma trận $P_{\pi-1}$ biểu diễn nghịch đảo của hoán vị $\pi_{1}$ là nghịch đảo $P_{\pi1}^{-1}$ của ma trận $P_{\pi1}^{1}$ biểu diễn hoán vị $\pi_{1}$; rằng là,
$$P_{\pi-1}= P_{\pi1}^{-1}  .$$
$$1$$
Hơn nữa,
$$P_{\pi1}^{-1}  = (P_{\pi1})^{\top}.$$
$(3)$ Chứng minh rằng nếu $P$ là ma trận liên kết với phép chuyển vị, thì det(P) $= -1$.
$(4)$ Chứng minh rằng nếu $P$ là hoán vị ma trận, thì det(P) $= \pm 1$.
$(5)$ Sử dụng hoán vị các ma trận đến cho một cái khác chứng minh của sự kiện rằng tính chẵn lẻ của số của các phép chuyển vị được sử dụng đến biểu diễn hoán vị $\pi$ phụ thuộc chỉ trên $\pi$.
