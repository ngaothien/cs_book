# Phân rã QR (QR-decomposition) cho Các ma trận khả nghịch


<!-- PAGE 487 -->

## 12.8 Phân rã QR (QR-decomposition) cho Các ma trận khả nghịch

Bây giờ rằng ta có định nghĩa của ma trận trực giao (orthogonal matrix), ta có thể giải thích cách mà Gram– Schmidt trực chuẩn hóa quy trình ngay lập tức cho ta Phân rã QR (QR-decomposition) cho các ma trận.

> **Định nghĩa 12.8.** Cho trước bất kỳ thực $n \times  n$ ma trận $A$, Phân rã QR (QR-decomposition) của $A$ là bất kỳ cặp của $n\times n$ các ma trận $(Q, R)$, ở đâu $Q$ là ma trận trực giao (orthogonal matrix) và $R$ là tam giác trên (upper triangular) ma trận sao cho $A = QR$. Lưu ý rằng nếu $A$ là không khả nghịch, thì một số đường chéo phần tử (entry) trong $R$ phải là không.

> **Mệnh đề 12.16.** Cho trước bất kỳ thực $n \times  n$ ma trận $A$, nếu $A$ là khả nghịch, thì có một ma trận trực giao (orthogonal matrix) $Q$ và tam giác trên (upper triangular) ma trận $R$ với dương đường chéo các phần tử (entries) sao cho $A = QR$.
$$\mathbb{E}^{n}$$

*Chứng minh.* Ta có thể quan điểm các cột của $A$ như các vectơ $A^{1}, \dots  , A^{n}$ trong. Nếu $A$ là khả nghịch, thì chúng là độc lập tuyến tính (linearly independent), và ta có thể áp dụng Mệnh đề 12.10 đến produce cơ sở trực chuẩn (orthonormal basis) bằng cách sử dụng Gram–Schmidt trực chuẩn hóa quy trình. Nhắc lại rằng ta xây dựng các vectơ $Q^{k}$ và $Q^{'k}$ như sau:
$$Q^{'1}= A^{1},Q^{1}= \frac{Q^{'1}}{\|Q^{'1}\|} ,$$
Và cho quy nạp bước
$$-$$
$$Q^{'k+1}= A^{k+1} \sum_{i=1}^{k}  (A^{k+1}\cdot  Q^{i}) Q^{i},Q^{k+1}= \frac{Q^{'k+1}}{\|Q^{'k+1}\|} ,$$
Ở đâu $1 \le k \le n$ - $1$. Nếu ta biểu diễn các vectơ $A^{k}$ theo $Q^{i}$ và $Q^{'i}$, ta thu được tam giác hệ
$$A^{1}=\|Q^{'1}\|Q^{1},$$
$$\vdots$$
$$A^{j}=(A^{j}\cdot  Q^{1}) Q^{1}+ \cdots  + (A^{j}\cdot  Q^{i}) Q^{i}+ \cdots  + (A^{j}\cdot  Q^{j-1}) Q^{j-1}+ \|Q^{'j}\|Q^{j},$$
$$\vdots$$
$$A^{n}=(A^{n}\cdot  Q^{1}) Q^{1}+ \cdots  + (A^{n}\cdot  Q^{n-1}) Q^{n-1}+ \|Q^{'n}\|Q^{n}.$$
Đặt $r_{k k} = \|Q^{'k}\|$, và $r_{i j} = A^{j} \cdot  Q^{i}$ (reversal của $i$ và $j$ trên vế phải là intentional!), ở đâu $1 \le k \le n, 2 \le j \le n$, và $1 \le i \le j$ - $1$, và đặt $q_{i j}$ là thành phần thứ $i$ của $Q^{j}$, ta lưu ý rằng $a_{i j}$, thành phần thứ $i$ của $A^{j}$, được cho bởi
$$a_{i j} = r_{1j}q_{i1} + \cdots  + r_{i j}q_{i i} + \cdots  + r_{j j}q_{i j} = q_{i1}r_{1j} + \cdots  + q_{i i}r_{i j} + \cdots  + q_{i j}r_{j j}.$$
Nếu ta cho $Q = (q_{i j})$, ma trận có các cột là các thành phần của $Q^{j}$, và $R = (r_{i j})$, ở trên các phương trình chỉ ra rằng $A = QR$, ở đâu $R$ là tam giác trên (upper triangular). đường chéo các phần tử (entries)
$$\cdot$$
$r_{k k} = \|Q^{'k}\| = A^{k}  Q^{k}$ là thật vậy dương.

<!-- PAGE 488 -->
Độc giả nên thử ở trên quy trình trên một số concrete các ví dụ cho $2\times 2$ và $3\times 3$ các ma trận.
Các nhận xét:
$(1)$ Bởi vì đường chéo các phần tử (entries) của $R$ là dương, nó có thể được được hiển thị rằng $Q$ và $R$ là duy nhất. Tổng quát hơn, nếu $A$ là khả nghịch và nếu $A = Q_{1}R_{1} = Q_{2}R_{2}$ là hai QR-decompositions cho $A$, thì
$$R_{1}R_{2}^{-1}= Q_{1}^{\top} Q_{2}.$$
Ma trận $Q_{1}^{\top} Q_{2}$ là trực giao và nó là dễ để xem rằng $R_{1}R_{2}^{-1}$ là tam giác trên (upper triangular). Nhưng tam giác trên (upper triangular) ma trận mà là trực giao phải là ma trận đường chéo (diagonal matrix) $D$ với đường chéo các phần tử (entries) $\pm 1$, do đó $Q_{2} = Q_{1}D$ và $R_{1} = DR_{2}$.
$(2)$ Phân rã QR (QR-decomposition) nghiệm đúng chẵn/ngay cả khi $A$ là không khả nghịch. Trong trường hợp này, $R$ có một số không trên đường chéo. Tuy nhiên, khác nhau chứng minh là cần thiết. Ta sẽ cho đẹp chứng minh bằng cách sử dụng Householder các ma trận (xem Mệnh đề 13.4, và cũng Strang $[175, 176]$, Golub và Van Loan $[83]$, Trefethen và Bau $[182]$, Demmel $[48]$, Kincaid và Cheney $[105]$, hoặc Ciarlet $[41])$. Cho tốt hơn số tính ổn định, nó được ưu tiên hơn để sử dụng được sửa đổi Gram–Schmidt phương pháp đến cài đặt Nhân tử hóa QR (QR-factorization) phương pháp. Ở đây là Matlab bài toán quy hoạch cài đặt QRfactorization bằng cách sử dụng được sửa đổi Gram–Schmidt. hàm [Q,R] $=$ qrv4() $n =$ kích thước(,1); cho $i =$ 1:n Q(:,i) $=$ (:,i); cho $j =$ 1:i-1
$$R(j,i) = Q(:,j)’*Q(:,i);$$
$$Q(:,i) = Q(:,i) - R(j,i)*Q(:,j);$$
Kết thúc/cuối R(i,i) $=$ sqrt(Q(:,i)’*Q(:,i)); Q(:,i) $= Q(:,i)/R(i,i)$; kết thúc/cuối kết thúc/cuối

> **Ví dụ 12.13.** Xét ma trận
$$A = \begin{pmatrix} 0 & 0 & 5 \\ 0 & 4 & 1 \\ 1 & 1 & 1 \end{pmatrix} .$$
Để xác định Phân rã QR (QR-decomposition) của $A$, ta thứ nhất sử dụng Trực chuẩn hóa Gram-Schmidt

<!-- PAGE 489 -->
Quy trình để tính toán $Q = (Q^{1}Q^{2}Q^{3})$. Theo Định nghĩa
$$A^{1} = Q^{'1} = Q^{1} = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} ,$$
$$and since A^{2} = \begin{pmatrix} 0 \\ 4 \\ 1 \end{pmatrix} , we discover that$$
$$Q^{'2} = A^{2} -(A^{2} \cdot  Q^{1})Q^{1} = \begin{pmatrix} 0 \\ 4 \\ 1 \end{pmatrix} - \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 4 \\ 0 \end{pmatrix} .$$
$$Hence, Q^{2} = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} . Finally,$$
$$Q^{'3} = A_{3} -(A^{3} \cdot  Q^{1})Q^{1} -(A^{3} \cdot  Q^{2})Q^{2} = \begin{pmatrix} 5 \\ 1 \\ 1 \end{pmatrix} - \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} - \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 5 \\ 0 \\ 0 \end{pmatrix} ,$$
$$which implies that Q^{3} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} . According to Proposition 12.16, in order to determine R we$$
Cần để tính toán
$$= 1$$
$$r_{11} =Q^{'1}r_{12} = A^{2}\cdot  Q^{1}= 1r_{13} = A^{3}\cdot  Q^{1}= 1$$
$$= 4$$
$$r_{22} =Q^{'2}r_{23} = A_{3} \cdot  Q^{2}= 1$$
$$r_{33} =

$Q^{'3}$

$=$ 5.$$
$$In summary, we have found that the QR-decomposition of A = \begin{pmatrix} 0 & 0 & 5 \\ 0 & 4 & 1 \\ 1 & 1 & 1 \end{pmatrix} is$$
$$Q = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix} andR = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 4 & 1 \\ 0 & 0 & 5 \end{pmatrix} .$$

> **Ví dụ 12.14.** Một cái khác ví dụ của Phân rã QR (QR-decomposition) là
$$A = \begin{pmatrix} 1 & 1 & 2 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix} = \begin{pmatrix} \sqrt & \sqrt \\ 1/ & \overline{2} & 1/ & \overline{2} & 0 \\ 0\sqrt & 0\sqrt & 1 \\ 1/ & \overline{2} & 1/ & \overline{2} & 0 \end{pmatrix} \begin{pmatrix} \sqrt & \sqrt & \sqrt \\ \overline{2} & 1/\sqrt{2} & \sqrt{2} \\ 0 & 1/ & 2 & 2 \\ 0 & 0 & 1 \end{pmatrix} .$$
$$-$$

<!-- PAGE 490 -->

> **Ví dụ 12.15.** Nếu ta áp dụng ở trên Matlab hàm đến ma trận
$$A = \begin{pmatrix} 4 & 1 & 0 & 0 & 0 \\ 1 & 4 & 1 & 0 & 0 \\ 0 & 1 & 4 & 1 & 0 \\ 0 & 0 & 1 & 4 & 1 \\ 0 & 0 & 0 & 1 & 4 \end{pmatrix} ,$$
Ta thu được
$$Q = \begin{pmatrix} 0.9701 & -0.2339 & 0.0619 & -0.0166 & 0.0046 \\ 0.2425 & 0.9354 & -0.2477 & 0.0663 & -0.0184 \\ 0 & 0.2650 & 0.9291 & -0.2486 & 0.0691 \\ 0 & 0 & 0.2677 & 0.9283 & -0.2581 \\ 0 & 0 & 0 & 0.2679 & 0.9634 \end{pmatrix}$$
Và
$$R = \begin{pmatrix} 4.1231 & 1.9403 & 0.2425 & 0 & 0 \\ 0 & 3.7730 & 1.9956 & 0.2650 & 0 \\ 0 & 0 & 3.7361 & 1.9997 & 0.2677 \\ 0 & 0 & 073.7324 & 2.0000 \\ 0 & 0 & 0 & 0 & 3.5956 \end{pmatrix} .$$
Nhận xét: Matlab hàm qr, được gọi là bởi $[Q, R] =$ qr(), thực hiện không nhất thiết trả về tam giác trên (upper-triangular) ma trận có đường chéo các phần tử (entries) là dương. Phân rã QR (QR-decomposition) cho ta khá efficient và một cách số stable phương pháp cho việc giải các hệ của các phương trình tuyến tính. Thật vậy, cho trước hệ Ax $= b$, ở đâu $A$ là $n \times  n$ ma trận khả nghịch (invertible matrix), viết $A = QR$, vì $Q$ là trực giao, ta thu được
$$Rx = Q^{\top}b,$$
Và vì $R$ là tam giác trên (upper triangular), ta có thể giải nó bởi Phép khử Gauss (Gaussian elimination), bởi việc giải cho cuối cùng biến $x_{n}$ thứ nhất, thế giá trị của nó vào hệ, thì việc giải cho $x_{n-1}$, etc. Phân rã QR (QR-decomposition) là cũng rất hữu ích trong việc giải bình phương tối thiểu (least squares) các bài tập (ta sẽ đến quay lại đến điều này trong Chương $23)$, và cho việc tìm các trị riêng (eigenvalues); xem Chương $18$. Nó có thể được dễ dàng được điều chỉnh đến trường hợp ở đâu $A$ là rectangular $m\times n$ ma trận với độc lập các cột (do đó, $n \le m)$. Trong trường hợp này, $Q$ là không khá trực giao. Nó là một ma trận cỡ $m \times  n$ có các cột là trực giao, và $R$ là khả nghịch $n\times n$ tam giác trên (upper triangular) ma trận với dương đường chéo các phần tử (entries). Cho nhiều hơn/thêm trên QR, xem Strang $[175, 176]$, Golub và Van Loan $[83]$, Demmel $[48]$, Trefethen và Bau $[182]$, hoặc Serre $[162]$. somewhat đáng ngạc nhiên hệ quả của Phân rã QR (QR-decomposition) là nổi tiếng determinantal bất đẳng thức do Hadamard.

<!-- PAGE 491 -->

> **Mệnh đề 12.17.** (Hadamard) Với mọi thực $n \times  n$ ma trận $A = (a_{ij})$, ta có
$$1/21/2$$
$$| \det(A)| \le \prod_{i=1}^{n}  \begin{pmatrix} a_{ij}^{2} \end{pmatrix} \sum_{j=1}^{n}  and| \det(A)| \le \prod_{j=1}^{n}  \begin{pmatrix} a_{ij}^{2} \end{pmatrix} \sum_{i=1}^{n}  .$$
Hơn thế nữa, đẳng thức nghiệm đúng khi và chỉ khi hoặc $A$ có trực giao các hàng trong trái bất đẳng thức hoặc trực giao các cột trong phải bất đẳng thức.

*Chứng minh.* Nếu det() $= 0$, thì bất đẳng thức là tầm thường. Ngoài ra, nếu righthand vế/cạnh là cũng $0$, thì hoặc một số cột hoặc một số hàng là không. Nếu det() $\neq  0$, thì ta có thể nhân tử $A$ như $A = QR$, với $Q$ là trực giao và $R = (r_{ij})$ tam giác trên (upper triangular) với dương đường chéo các phần tử (entries). Khi đó vì $Q$ là trực giao det(Q) $= \pm 1$, do đó
$$| \det(A)| = | \det(Q)| | \det(R)| = \prod_{j=1}  r_{jj}.$$
Bây giờ như $Q$ là trực giao, nó bảo toàn Euclidean chuẩn (norm), do đó
$$\sum_{i=1}^{n}  a_{ij}^{2} =

$A_{2}^{j2}$

$=$

$QR_{2}^{j2}$

$=$

$R_{2}^{j2}$

$= \sum_{i=1}^{n}  r_{ij}^{2} \ge r_{jj}^{2},$$$ mà suy ra rằng
$$1/2$$
$$| \det(A)| = \prod_{j=1}^{n}  r_{jj} \le \prod_{j=1}^{n}  R_{2}^{j}

$= \prod_{j=1}^{n}  \begin{pmatrix} a_{ij}^{2} \end{pmatrix} \sum_{i=1}^{n}$.$$ The other inequality is obtained by replacing $A$ by $A^{\đỉnh/trên}$. Finally, if det(A) $\neq 0$ và đẳng thức nghiệm đúng, thì ta phải có
$$r_{jj} =

$A_{2}^{j}$

$,1 \le j \le$ n,$$ which can only occur if $A$ có trực giao các cột. Một cái khác phiên bản của Hadamard’s bất đẳng thức áp dụng đến đối xứng nửa xác định dương (positive semidefinite) các ma trận.

> **Mệnh đề 12.18.** (Hadamard) Với mọi thực $n \times  n$ ma trận $A = (a_{ij})$, nếu $A$ là đối xứng nửa xác định dương (positive semidefinite), thì ta có
$$\det(A) \le \prod_{i=1}^{n}  a_{ii}.$$
Hơn thế nữa, nếu $A$ là xác định dương (positive definite), thì đẳng thức nghiệm đúng khi và chỉ khi $A$ là ma trận đường chéo (diagonal matrix).
