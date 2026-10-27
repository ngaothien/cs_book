# Dữ liệu Compression và SVD


<!-- PAGE 781 -->

> **Ví dụ 23.3.** Xét sau đây thực đường chéo tạo thành của ma trận chuẩn tắc (normal matrix)
$$A = \begin{pmatrix} -2.7500 & 2.1651 & -0.8660 & 0.5000 \\ 2.1651 & -0.2500 & -1.5000 & 0.8660 \\ 0.8660 & 1.5000 & 0.7500 & -0.4330 \\ 0.5000 & 0.8660 & 0.4330 & 0.2500 \end{pmatrix} = U\Lambda U^{\top},$$
$$---$$
Với
$$U = \begin{pmatrix} \cos(\pi /3) & 0 & \sin(\pi /3) & 0 \\ \sin(\pi /3) & 0 & -\cos(\pi /3) & 0 \\ 0 & \cos(\pi /6) & 0 & \sin(\pi /6) \\ 0 & \cos(\pi /6) & 0 & \sin(\pi /6) \end{pmatrix} ,\Lambda  = \begin{pmatrix} 1 & -2 & 0 & 0 \\ 2 & 1 & 0 & 0 \\ 0 & 0 & -4 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} .$$
$$-$$
Ta thu được
$$\Lambda^{+}  = \begin{pmatrix} 1/5 & 2/5 & 0 & 0 \\ -2/5 & 1/5 & 0 & 0 \\ 0 & 0 & -1/4 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} ,$$
Và nghịch đảo giả (pseudo-inverse) của $A$ là
$$A^{+} = U\Lambda^{+} U^{\top} = \begin{pmatrix} -0.1375 & 0.1949 & 0.1732 & -0.1000 \\ 0.1949 & 0.0875 & 0.3000 & -0.1732 \\ -0.1732 & -0.3000 & 0.1500 & -0.0866 \\ 0.1000 & 0.1732 & 0.0866 & 0.0500 \end{pmatrix} ,$$
$$-$$
Mà agrees với pinv(). Các tính chất sau đây, do Penrose, đặc trưng hóa nghịch đảo giả (pseudo-inverse) của ma trận. Ta có đã được chứng minh rằng nghịch đảo giả (pseudo-inverse) thỏa mãn các phương trình này. Cho chứng minh của điều ngược lại, xem Kincaid và Cheney $[105]$.

> **Mệnh đề 23.8.** Cho trước bất kỳ ma trận cỡ $m \times  n$ $A$ (thực hoặc phức), nghịch đảo giả (pseudo-inverse) $A^{+}$ của $A$ là duy nhất $n \times  m$ ma trận thỏa mãn các tính chất sau đây:
$$AA^{+}A = A,$$
$$A^{+}AA^{+}= A^{+},$$
$$(AA^{+})^{\top}= AA^{+},$$
$$(A^{+}A)^{\top}= A^{+}A.$$

## 23.3 Dữ liệu Compression và SVD

Trong số nhiều các ứng dụng của SVD, rất hữu ích một là dữ liệu compression, notably cho các ảnh. Trong thứ tự để tạo precise khái niệm của closeness của các ma trận, ta sử dụng khái niệm của

<!-- PAGE 782 -->
Chuẩn ma trận (matrix norm). Điều này khái niệm được định nghĩa trong Chương $9$, và độc giả có thể muốn đến ôn tập/tổng quan nó trước reading bất kỳ further. Cho trước một ma trận cỡ $m \times  n$ của hạng (rank) $r$, ta sẽ like để tìm tốt nhất xấp xỉ của $A$ bởi ma trận $B$ của hạng (rank) $k \le r$ (thực sự, $k < r)$ sao cho $\|A$ - $B\|_{2}$ (hoặc $\|A$ - $B\|_{F})$ được cực tiểu hóa. sau đây mệnh đề là đã biết như Eckart–Young định lý.

> **Mệnh đề 23.9.** Cho $A$ là một ma trận cỡ $m \times  n$ của hạng (rank) $r$ và cho $V DU^{\top} = A$ là SVD cho $A$. Viết $u_{i}$ cho các cột của $U, v_{i}$ cho các cột của $V$, và $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{p}$ cho các giá trị kỳ dị (singular values) của $A (p =$ min(m, $n))$. Thì ma trận của hạng (rank) $k < r$ closest đến $A$ (trong $\|\|_{2}$ chuẩn (norm)) được cho bởi
$$A_{k} = \sum_{i=1}^{k}  \sigma_{i} v_{i}u_{i}^{\top} = V \mathrm{diag}(\sigma_{1} , \dots  , \sigma_{k} , 0, \dots  , 0)U^{\top}$$
Và $\|A$ - $A_{k}\|_{2} = \sigma_{k+1}$.

*Chứng minh.* Bởi cách xây dựng, $A_{k}$ có hạng (rank) $k$, và ta có
$$\|A -A_{k}\|_{2} = \sum_{i=k+1}^{p}  \sigma_{i} v_{i}u_{i}^{\top} =

$V \mathrm{diag}(0, \dots  , 0, \sigma_{k+1} , \dots  , \sigma_{p} )U_{2}^{\top}$

$= \sigma_{k+1}$.$$
$$2$$
Nó vẫn còn để chỉ ra rằng $\|A$ - $B\|_{2} \ge \sigma_{k+1}$ với mọi hạng (rank) $k$ các ma trận $B$. Cho $B$ là bất kỳ hạng (rank) $k$ ma trận, do đó hạt nhân (hạt nhân (kernel)) của nó có số chiều $n -k$. không gian con $U_{k+1}$ được sinh (spanned) bởi $(u_{1}, \dots  , u_{k+1})$ có số chiều $k + 1$, và bởi vì tổng của số chiều của hạt nhân (kernel) của $B$ và của $U_{k+1}$ là $(n$ - $k) + k + 1 = n + 1$, các phần tử này hai các không gian con phải giao nhau trong không gian con có số chiều ít nhất $1$. Chọn bất kỳ unit vectơ $h$ trong Ker(B) $\cap U_{k+1}$. Khi đó vì Bh $= 0$, và vì $U$ và $V$ là các phép đẳng cự, ta có $\|A$ - $B\|_{2}^{2} \ge \|(A$ - $B)h\|_{2}^{2} = \|Ah\|_{2}^{2} =$

$V DU^{\top}h_{2}^{2}$

$=$

$DU^{\top}h_{2}^{2}$

$\ge \sigma_{k+1}^{2}$

$U^{\top}h_{2}^{2}$

$= \sigma_{k+1}^{2}$, mà chứng minh của ta khẳng định. Lưu ý rằng $A_{k}$ có thể được stored bằng cách sử dụng $(m +$ n)k các phần tử (entries), như opposed đến mn các phần tử (entries). Khi $k \ll m$, điều này là substantial gain.

> **Ví dụ 23.4.** Xét một cách xấu được điều kiện ma trận đối xứng (symmetric matrix)
$$A = \begin{pmatrix} 10 & 7 & 8 & 7 \\ 7 & 5 & 6 & 5 \\ 8 & 6 & 10 & 9 \\ 7 & 5 & 9 & 10 \end{pmatrix}$$
Từ Mục 9.5. Vì $A$ là SPD, ta có SVD
$$A = UDU^{\top} ,$$
