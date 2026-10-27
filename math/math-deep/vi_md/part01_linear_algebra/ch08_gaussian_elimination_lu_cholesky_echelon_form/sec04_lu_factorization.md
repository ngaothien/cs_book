# Nhân tử hóa LU (LU-factorization)


<!-- PAGE 269 -->

> **Định lý 8.1.** (Phép khử Gauss (Gaussian elimination)) Cho $A$ là một ma trận cỡ $n \times  n$ (khả nghịch hoặc không). Thì tồn tại một ma trận khả nghịch (invertible matrix) $M$ sao cho $U = MA$ là tam giác trên (upper-triangular). các phần tử trụ là tất cả khác không khi và chỉ khi $A$ là khả nghịch.

*Chứng minh.* Ta đã được chứng minh định lý khi $A$ là khả nghịch, cũng như cuối cùng assertion. Bây giờ $A$ là suy biến khi và chỉ khi một số phần tử trụ (pivot) là không, nói tại Giai đoạn $k$ của phép khử. Nếu do đó, ta phải có $a_{i k}^{(k)} = 0$ cho $i = k, \dots  , n$; nhưng trong trường hợp này, $A_{k+1} = A_{k}$ và ta có thể chọn $P_{k} = E_{k} =$ I.
Nhận xét: Hiển nhiên, ma trận $M$ có thể được được tính như
$$M = E_{n-1}P_{n-1} \cdots  E_{2}P_{2}E_{1}P_{1},$$
Nhưng điều này biểu thức là của không có sử dụng. Thật vậy, những gì ta cần là $M^{-1}$; khi không có các hoán vị là cần thiết, hóa ra là $M^{-1}$ có thể được thu được ngay lập tức từ các ma trận $E_{k}’s$, thực ra, từ của chúng các nghịch đảo, và không có các phép nhân là cần.
Nhận xét: Thay vì của nhìn cho ma trận khả nghịch (invertible matrix) $M$ sao cho $MA$ là tam giác trên (upper-triangular), ta có thể nhìn cho ma trận khả nghịch (invertible matrix) $M$ sao cho $MA$ là ma trận đường chéo (diagonal matrix). Chỉ đơn giản thay đổi đến Phép khử Gauss (Gaussian elimination) là cần thiết. Tại mọi Giai đoạn $k$, sau phần tử trụ (pivot) có đã được tìm thấy và chọn phần tử trụ đã được performed, nếu cần, ngoài cộng phù hợp các bội của hàng thứ $k$ đến các hàng ở dưới hàng $k$ trong thứ tự đến không các phần tử (entries) trong cột $k$ cho $i = k + 1, \dots  , n$, cũng cộng phù hợp các bội của hàng thứ $k$ đến các hàng ở trên hàng $k$ trong thứ tự đến không các phần tử (entries) trong cột $k$ cho $i = 1, \dots  , k$ - $1$. Như vậy các bước là cũng đạt được bằng cách nhân trên trái bởi sơ cấp các ma trận $E_{i,k;\beta i,k}$, ngoại trừ rằng $i < k$, sao cho các ma trận này là không tam giác dưới (lower-triangular) các ma trận. Tuy nhiên, tại kết thúc/cuối của process, ta tìm rằng $A_{n} = MA$, là ma trận đường chéo (diagonal matrix). phương pháp này được gọi là Gauss-Jordan nhân tử hóa. Bởi vì nó là nhiều hơn/thêm expensive hơn Phép khử Gauss (Gaussian elimination), phương pháp này là không được sử dụng nhiều trong thực tế. Tuy nhiên, Gauss-Jordan nhân tử hóa có thể được được sử dụng để tính nghịch đảo của ma trận $A$. Thật vậy, ta tìm cột thứ $j$ của $A^{-1}$ bởi việc giải hệ $Ax^{(j)} = e_{j}$ (ở đâu $e_{j}$ là vectơ cơ sở chính tắc thứ $j$ $\mathbb{R}^{n}$ của). Bằng cách áp dụng Gauss-Jordan, ta là đã dẫn đến đến hệ của tạo thành $D_{j}x^{(j)} = M_{j}e_{j}$, ở đâu $D_{j}$ là ma trận đường chéo (diagonal matrix), và ta có thể ngay lập tức tính $x^{(j)}$. Nó vẫn còn đến thảo luận lựa chọn của phần tử trụ (pivot), và cũng các điều kiện rằng đảm bảo rằng không có các hoán vị là cần thiết during Phép khử Gauss (Gaussian elimination) process. Ta bắt đầu bởi phát biểu cần và đủ điều kiện cho ma trận khả nghịch (invertible matrix) đến có Nhân tử hóa LU (LU-factorization) (i.e., Phép khử Gauss (Gaussian elimination) thực hiện không đòi hỏi chọn phần tử trụ).

## 8.4 Nhân tử hóa LU (LU-factorization)


> **Định nghĩa 8.1.** Ta nói rằng ma trận khả nghịch (invertible matrix) $A$ có Nhân tử hóa LU (LU-factorization) nếu nó có thể được viết dưới dạng $A = LU$, ở đâu $U$ là tam giác trên (upper-triangular) khả nghịch và $L$ là tam giác dưới (lower-triangular), với $L_{i i} = 1$ cho $i = 1, \dots  , n$.

<!-- PAGE 270 -->
Tam giác dưới (lower-triangular) ma trận với đường chéo các phần tử (entries) bằng $1$ được gọi là một unit tam giác dưới (lower-triangular) ma trận. Cho trước một ma trận cỡ $n\times n$ $A = (a_{i j})$, với mọi $k$ với $1 \le k \le n$, cho (1: $k, 1$: $k)$ ký hiệu ma trận con của $A$ có các phần tử (entries) là $a_{i j}$, ở đâu $1 \le i, j \le k.^{1}$ Ví dụ, nếu $A$ là ma trận cỡ $5 \times  5$
$$A = \begin{pmatrix} a_{11} & a_{12} & a_{13} & a_{14} & a_{15} \\ a_{21} & a_{22} & a_{23} & a_{24} & a_{25} \\ a_{31} & a_{32} & a_{33} & a_{34} & a_{35} \\ a_{41} & a_{42} & a_{43} & a_{44} & a_{45} \\ a_{51} & a_{52} & a_{53} & a_{54} & a_{55} \end{pmatrix} ,$$
Thì
$$A(1 : 3, 1 : 3) = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} .$$

> **Mệnh đề 8.2.** Cho $A$ là khả nghịch ma trận cỡ $n \times n$. Thì $A$ có Nhân tử hóa LU (LU-factorization) $A = LU$ khi và chỉ khi mọi ma trận (1: $k, 1$: $k)$ là khả nghịch cho $k = 1, \dots  , n$. Hơn nữa, khi $A$ có Nhân tử hóa LU (LU-factorization), ta có
$$\det(A(1 : k, 1 : k)) = \pi_{1} \pi_{2}  \cdots  \pi_{k} ,k = 1, \dots  , n,$$
Ở đâu $\pi_{k}$ là phần tử trụ (pivot) thu được sau $k -1$ phép khử các bước. Vì vậy, thứ $k$ phần tử trụ (pivot) được cho bởi
$$a_{11} = \det(A(1 : 1, 1 : 1))if k = 1$$
$$$$
$$\pi_{k}  =$$
$$ \frac{\det(A(1 : k, 1 : k))}{\det(A(1 : k -1, 1 : k -1))} if k = 2, \dots  , n.$$

*Chứng minh.* Thứ nhất giả sử rằng $A = LU$ là Nhân tử hóa LU (LU-factorization) của $A$. Ta có thể viết
$$A = \begin{pmatrix} A(1 : k, 1 : k) & A_{2} \\ A_{3} & A_{4} \end{pmatrix} = \begin{pmatrix} L_{1} & 0 \\ L_{3} & L_{4} \end{pmatrix} \begin{pmatrix} U_{1} & U_{2} \\ 0 & U_{4} \end{pmatrix} = \begin{pmatrix} L_{1}U_{1} & L_{1}U_{2} \\ L_{3}U_{1} & L_{3}U_{2} + L_{4}U_{4} \end{pmatrix} ,$$
Ở đâu $L_{1}, L_{4}$ là unit tam giác dưới (lower-triangular) và $U_{1}, U_{4}$ là tam giác trên (upper-triangular). (Lưu ý, (1: $k, 1$: $k), L_{1}$, và $U_{1}$ là $k \times k$ các ma trận; $A_{2}$ và $U_{2}$ là $k \times$ (n-k) các ma trận; $A_{3}$ và $L_{3}$ là $(n-k)\times k$ các ma trận; $A_{4}, L_{4}$, và $U_{4}$ là $(n$ - $k) \times  (n$ - $k)$ các ma trận.) Do đó,
$$A(1 : k, 1 : k) = L_{1}U_{1},$$
Và vì $U$ là khả nghịch, $U_{1}$ là cũng khả nghịch (định thức (determinant) của $U$ là tích của đường chéo các phần tử (entries) trong $U$, mà là tích của đường chéo các phần tử (entries) trong $U_{1}$ và $U_{4})$. Như $L_{1}$ là khả nghịch (vì của nó đường chéo các phần tử (entries) bằng $1)$, ta xem rằng (1: $k, 1$: $k)$ là khả nghịch cho $k = 1, \dots  , n$. Ngược lại, giả sử rằng (1: $k, 1$: $k)$ là khả nghịch cho $k = 1, \dots  , n$. Ta chỉ cần để chỉ ra rằng Phép khử Gauss (Gaussian elimination) thực hiện không cần chọn phần tử trụ. Ta chứng minh bằng quy nạp theo $k$ rằng bước thứ $k$ thực hiện không cần chọn phần tử trụ. $\overline{1}\overline{We} \overline{are} \overline{using} \overline{Matlab}\overline{’s} \overline{notation.}$

<!-- PAGE 271 -->
Điều này nghiệm đúng cho $k = 1$, vì (1: $1, 1$: $1) = (a_{1 1})$, do đó $a_{1 1} \neq  0$. Giả sử rằng không có chọn phần tử trụ đã là cần cho thứ nhất $k$ - $1$ các bước $(2 \le k \le n$ - $1)$. Trong trường hợp này, ta có
$$E_{k-1} \cdots  E_{2}E_{1}A = A_{k},$$
Ở đâu $L = E_{k-1} \cdots  E_{2}E_{1}$ là unit tam giác dưới (lower-triangular) ma trận và $A_{k}(1$: $k, 1$: $k)$ là uppertriangular, sao cho $LA = A_{k}$ có thể được viết dưới dạng
$$\begin{pmatrix} L_{1} & 0 \\ L_{3} & L_{4} \end{pmatrix} \begin{pmatrix} A(1 : k, 1 : k) & A_{2} \\ A_{3} & A_{4} \end{pmatrix} = \begin{pmatrix} U_{1} & B_{2} \\ 0 & B_{4} \end{pmatrix} ,$$
Ở đâu $L_{1}$ là unit tam giác dưới (lower-triangular) và $U_{1}$ là tam giác trên (upper-triangular). (Một lần một lần nữa (1: $k, 1$: $k), L_{1}$, và $U_{1}$ là $k \times  k$ các ma trận; $A_{2}$ và $B_{2}$ là $k \times  (n$ - $k)$ các ma trận; $A_{3}$ và $L_{3}$ là $(n$ - $k) \times  k$ các ma trận; $A_{4}, L_{4}$, và $B_{4}$ là $(n$ - $k) \times  (n$ - $k)$ các ma trận.) Nhưng khi đó,
$$L_{1}A(1 : k, 1 : k)) = U_{1},$$
Ở đâu $L_{1}$ là khả nghịch (thực ra, $det(L_{1}) = 1)$, và vì bởi giả thiết (1: $k, 1$: $k)$ là khả nghịch, $U_{1}$ là cũng khả nghịch, mà suy ra rằng $(U_{1})_{kk} \neq  0$, vì $U_{1}$ là tam giác trên (upper-triangular). Vì vậy, không có chọn phần tử trụ là cần thiết trong Bước $k$, thiết lập quy nạp bước. Vì $det(L_{1}) = 1$, ta cũng có $det(U_{1}) = det(L_{1}A(1$: $k, 1$: $k)) = det(L_{1})$ det((1: $k, 1$: $k)) =$ det((1: $k, 1$: $k))$, và vì $U_{1}$ là tam giác trên (upper-triangular) và có các phần tử trụ $\pi_{1} , \dots  , \pi_{k}$ trên của nó đường chéo, ta thu được
$$\det(A(1 : k, 1 : k)) = \pi_{1} \pi_{2}  \cdots  \pi_{k} ,k = 1, \dots  , n,$$
Như đã khẳng định.
Nhận xét: sử dụng của các định thức trong phần thứ nhất của chứng minh của Mệnh đề 8.2 có thể được tránh được nếu ta sử dụng sự kiện rằng tam giác ma trận là khả nghịch khi và chỉ khi tất cả của nó đường chéo các phần tử (entries) là khác không.

> **Hệ quả 8.3.** (Nhân tử hóa LU (LU-factorization)) Cho $A$ là khả nghịch ma trận cỡ $n \times n$. Nếu mọi ma trận (1: $k, 1$: $k)$ là khả nghịch cho $k = 1, \dots  , n$, thì Phép khử Gauss (Gaussian elimination) đòi hỏi không có chọn phần tử trụ và cho ta Nhân tử hóa LU (LU-factorization) $A = LU$.

*Chứng minh.* Ta được chứng minh trong Mệnh đề 8.2 rằng trong trường hợp này Phép khử Gauss (Gaussian elimination) đòi hỏi không có chọn phần tử trụ. Khi đó vì mọi sơ cấp ma trận $E_{i,k;\beta}$ là tam giác dưới (lower-triangular) (vì ta luôn luôn arrange rằng phần tử trụ (pivot) $\pi_{k}$ xảy ra ở trên các hàng rằng nó operates trên), vì $E_{i,k;\beta}^{-1} = E_{i,k;-\beta}$ và $E_{k}s$ là các tích của $E_{i,k;\beta i,k}s$, từ
$$E_{n-1} \cdots  E_{2}E_{1}A = U,$$
Ở đâu $U$ là tam giác trên (upper-triangular) ma trận, ta thu được
$$A = LU,$$
Ở đâu $L = E_{1}^{-1} E_{2}^{-1} \cdots  E_{n}^{-1}$ là tam giác dưới (lower-triangular) ma trận. Hơn nữa, như đường chéo các phần tử (entries) của mỗi $E_{i,k;\beta}$ là $1,^{-1}$ đường chéo các phần tử (entries) của mỗi $E_{k}$ là cũng $1$.

<!-- PAGE 272 -->

> **Ví dụ 8.1.** độc giả nên kiểm chứng rằng
$$\begin{pmatrix} 2 & 1 & 1 & 0 \\ 4 & 3 & 3 & 1 \\ 8 & 7 & 9 & 5 \\ 6 & 7 & 9 & 8 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 2 & 1 & 0 & 0 \\ 4 & 3 & 1 & 0 \\ 3 & 4 & 1 & 1 \end{pmatrix} \begin{pmatrix} 2 & 1 & 1 & 0 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 2 & 2 \\ 0 & 0 & 0 & 2 \end{pmatrix}$$
Là Nhân tử hóa LU (LU-factorization). Một của chính các lý do tại sao sự tồn tại của Nhân tử hóa LU (LU-factorization) cho ma trận $A$ là thú vị là rằng nếu ta cần để giải một vài các hệ phương trình tuyến tính Ax $= b$ tương ứng với cùng ma trận $A$, ta có thể thực hiện điều này cheaply bởi việc giải hai tam giác các hệ
$$Lw = b,andUx = w.$$
Có một nhất định asymmetry trong Phân rã LU (LU-decomposition) $A = LU$ của ma trận khả nghịch (invertible matrix) $A$. Thật vậy, đường chéo các phần tử (entries) của $L$ là tất cả $1$, nhưng điều này là một cách tổng quát sai cho $U$. Điều này asymmetry có thể được được khử như sau: nếu
$$D = \mathrm{diag}(u_{11}, u_{22}, \dots  , u_{nn})$$
Là ma trận đường chéo (diagonal matrix) bao gồm của đường chéo các phần tử (entries) trong $U$ (các phần tử trụ), thì nếu ta cho U' $= D^{-1}U$, ta có thể viết
$$A = LDU' ,$$
Ở đâu $L$ là thấp hơn- tam giác, U' là tam giác trên (upper-triangular), tất cả đường chéo các phần tử (entries) của cả hai $L$ và U' là $1$, và $D$ là ma trận đường chéo (diagonal matrix) của các phần tử trụ. Như vậy phân rã dẫn đến đến sau đây định nghĩa.

> **Định nghĩa 8.2.** Ta nói rằng khả nghịch $n\times n$ ma trận $A$ có LDU-factorization nếu nó có thể được viết dưới dạng $A =$ LDU', ở đâu $L$ là thấp hơn- tam giác, U' là tam giác trên (upper-triangular), tất cả đường chéo các phần tử (entries) của cả hai $L$ và U' là $1$, và $D$ là ma trận đường chéo (diagonal matrix). Ta sẽ xem một cách ngắn hơn nếu $A$ là thực đối xứng, thì U' $= L^{\top}$. Như ta sẽ xem bit sau này, thực đối xứng xác định dương (SPD) các ma trận thỏa mãn điều kiện của

> **Mệnh đề 8.2.** Vì vậy, các hệ phương trình tuyến tính liên quan đến thực đối xứng xác định dương (SPD) các ma trận có thể được được giải bởi Phép khử Gauss (Gaussian elimination) mà không có chọn phần tử trụ. Thực sự, nó là khả dĩ/có thể đến thực hiện tốt hơn: điều này là Nhân tử hóa Cholesky (Cholesky factorization). Nếu square ma trận khả nghịch (invertible matrix) $A$ có Nhân tử hóa LU (LU-factorization), thì nó là khả dĩ/có thể để tìm $L$ và $U$ trong khi performing Phép khử Gauss (Gaussian elimination). Nhắc lại rằng tại Bước $k$, ta chọn phần tử trụ (pivot) $\pi_{k}  = a_{ik}^{(k)}$ ̸ $= 0$ trong portion bao gồm của các phần tử (entries) của chỉ số $j \ge k$ của cột thứ $k$ của ma trận $A_{k}$ thu được do đó far, ta swap các hàng $i$ và $k$ nếu cần (chọn phần tử trụ bước), và thì ta không các phần tử (entries) của chỉ số $j = k + 1, \dots  , n$ trong cột $k$. Schematically, ta có kết quả sau các bước:
$$\begin{pmatrix} \times & \times & \times & \times & \times \\ 0 & \times & \times & \times & \times \\ 0 & \times & \times & \times & \times \\ 0 & a_{ik}^{(k)} & \times & \times & \times \\ 0 \end{pmatrix} pivot=\Rightarrow \begin{pmatrix} \times & \times & \times & \times & \times \\ 0 & a_{ik}^{(k)} & \times & \times & \times \\ 0 & \times & \times & \times & \times \\ 0 & \times & \times & \times & \times \\ 0 \end{pmatrix} elim=\Rightarrow \begin{pmatrix} \times & \times & \times & \times & \times \\ 0 & \times & \times & \times & \times \\ 0 & 0 & \times & \times & \times \\ 0 & 0 & \times & \times & \times \\ 0 & 0 & \times & \times & \times \end{pmatrix} .$$
$$\times \times \times \times \times \times \times \times$$

<!-- PAGE 273 -->
Chính xác hơn, sau hoán vị hàng $k$ và hàng $i$ (chọn phần tử trụ bước), nếu các phần tử (entries) trong cột $k$ ở dưới hàng $k$ là $\alpha_{k+1k} , \dots  , \alpha_{nk}$, thì ta cộng $-\alpha_{jk} /\pi_{k}$ lần hàng $k$ đến hàng $j$; điều này process được minh họa ở dưới:
$$\begin{pmatrix} a_{kk}^{(k)} \\ a_{k+1k}^{(k)} \\ \vdots \\ a_{ik}^{(k)} \\ \vdots \\ a_{nk}^{(k)} \end{pmatrix} pivot=\Rightarrow \begin{pmatrix} a_{ik}^{(k)} \\ a_{k+1k}^{(k)} \\ \vdots \\ a_{kk}^{(k)} \\ \vdots \\ a_{nk}^{(k)} \end{pmatrix} = \begin{pmatrix} \pi_{k} \\ \alpha_{k+1k} \\ \vdots \\ \alpha_{ik} \\ \vdots \\ \alpha_{nk} \end{pmatrix} elim=\Rightarrow \begin{pmatrix} \pi_{k} \\ 0 \\ \vdots \\ 0 \\ \vdots \\ 0 \end{pmatrix} .$$
Thì nếu ta viết $\ell_{jk}  = \alpha_{jk} /\pi_{k}$ cho $j = k + 1, \dots  , n$, cột thứ $k$ của $L$ là
$$\begin{pmatrix} 0 \\ \vdots \\ 0 \\ 1 \\ \ell_{k+1k} \\ \vdots \\ \ell_{nk} \end{pmatrix} .$$
Nhận thấy rằng các dấu của các nhân tử $-\alpha_{jk} /\pi_{k}$ có đã được flipped. Do đó, ta thu được unit tam giác dưới (lower triangular) ma trận
$$L = \begin{pmatrix} 1 & 0 & 0 & \cdots & 0 \\ \ell_{21} & 1 & 0 & \cdots & 0 \\ \ell_{31} & \ell_{32} & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & 0 \\ \ell_{n1} & \ell_{n2} & \ell_{n3} & \cdots & 1 \end{pmatrix} .$$
Nó là dễ để xem (và điều này được chứng minh trong Định lý 8.5) rằng nếu kết quả của Phép khử Gauss (Gaussian elimination) (mà không có chọn phần tử trụ) là $U = E_{n-1} \cdots  E_{1}A$, sao cho $L = E_{1}^{-1} E_{2}^{-1} \cdots  E_{n-1}^{-1}$, thì
$$E_{k} = \begin{pmatrix} 1 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \vdots \\ 0 & \cdots & 1 & 0 & \cdots & 0 \\ 0 & \cdots & -\ell_{k} & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \ddots & \vdots \\ 0 & \ell_{nk} & 0 & 1 \end{pmatrix} andE_{k}^{-1}= \begin{pmatrix} 1 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \vdots \\ 0 & \cdots & 1 & 0 & \cdots & 0 \\ 0 & \cdots & \ell_{k+1k} & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & \ell_{nk} & 0 & 1 \end{pmatrix} ,$$
$$\cdots -\cdots \cdots \cdots$$
Do đó cột thứ $k$ của $E_{k}^{-1}$ là cột thứ $k$ của $L$.

<!-- PAGE 274 -->
Không may là, chẵn/ngay cả dù $L^{-1} = E_{n-1} \cdots  E_{2}E_{1}$, các ma trận $E_{k}$ xảy ra trong sai thứ tự và cột thứ $k$ của $L^{-1}$ là không cột thứ $k$ của $E_{k}$. Đây là một ví dụ minh họa phương pháp.

> **Ví dụ 8.2.** Cho trước
$$A = A_{1} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & -1 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix} ,$$
$$--$$
Ta có kết quả sau dãy của các bước: thứ nhất phần tử trụ (pivot) là $\pi_{1}  = 1$ trong hàng $1$, và ta trừ hàng $1$ từ các hàng $2, 3$, và $4$. Ta thu được
$$A_{2} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 2 & 1 & 1 \end{pmatrix} L_{1} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 0 & 0 & 1 \end{pmatrix} .$$
$$---$$
Tiếp theo phần tử trụ (pivot) là $\pi_{2}  = -2$ trong hàng $2$, và ta trừ hàng $2$ từ hàng $4$ (và cộng $0$ lần hàng $2$ đến hàng $3)$. Ta thu được
$$A_{3} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix} L_{2} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix} .$$
$$-$$
Tiếp theo phần tử trụ (pivot) là $\pi_{3}  = -2$ trong hàng $3$, và vì thứ tư phần tử (entry) trong cột $3$ là đã không, ta cộng $0$ lần hàng $3$ đến hàng $4$. Ta thu được
$$A_{4} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix} L_{3} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix} .$$
$$-$$
Quy trình được hoàn tất, và ta có
$$L = L_{3} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix} U = A_{4} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix} .$$
$$-$$
Nó là dễ để kiểm tra rằng thật vậy
$$LU = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & -1 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix} = A.$$
$$---$$
Ta bây giờ chỉ ra cách mà để mở rộng ở trên phương pháp đến deal với chọn phần tử trụ efficiently. Điều này là $PA = LU$ nhân tử hóa.
