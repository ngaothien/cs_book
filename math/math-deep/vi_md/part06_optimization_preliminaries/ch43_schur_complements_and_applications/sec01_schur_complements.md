# Các phần bù Schur


<!-- PAGE 1565 -->
Chương $43$ Các phần bù Schur và Các ứng dụng Các phần bù Schur phát sinh một cách tự nhiên trong process của nghịch đảo các ma trận khối của tạo thành
$$M = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$$
Và trong đặc trưng hóa khi đối xứng các phiên bản của các ma trận này là xác định dương (positive definite) hoặc nửa xác định dương (positive semidefinite). Các phần tử này các đặc trưng đến lên trong khác nhau tối ưu hóa toàn phương (quadratic optimization) các bài tập; xem Boyd và Vandenberghe $[29]$, especially Phụ lục $B$. Trong hầu hết tổng quát trường hợp, pseudo-inverses là cũng cần thiết. Trong chương này ta giới thiệu Các phần bù Schur và mô tả một vài thú vị các cách trong mà chúng được sử dụng. Dọc theo cách ta cung cấp một số chi tiết và các chứng minh của một số các kết quả từ Phụ lục.5 (especially Mục.5.5) của Boyd và Vandenberghe $[29]$.

## 43.1 Các phần bù Schur

Cho $M$ là một ma trận cỡ $n \times  n$ được viết như $2 \times  2$ ma trận khối (block matrix)
$$M = \begin{pmatrix} A & B \\ C & D \end{pmatrix} ,$$
Ở đâu $A$ là một ma trận cỡ $p \times  p$ và $D$ là một ma trận cỡ $q \times  q$, với $n = p + q$ (do đó $B$ là một ma trận cỡ $p \times  q$ và $C$ là một ma trận cỡ $q \times  p$). Ta có thể thử để giải hệ phương trình tuyến tính
$$\begin{pmatrix} A & B \\ C & D \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} c \\ d \end{pmatrix} ,$$
Rằng là,
$$Ax + By=c,$$
$$Cx + Dy=d,$$
$$1565$$

<!-- PAGE 1566 -->
Bởi mimicking Phép khử Gauss (Gaussian elimination). Nếu ta giả sử rằng $D$ là khả nghịch, thì ta thứ nhất giải cho $y$, thu được
$$y = D^{-1}(d -Cx),$$
Và sau thế điều này biểu thức cho $y$ trong phương trình thứ nhất, ta thu được
$$Ax + B(D^{-1}(d -Cx)) = c,$$
Rằng là,
$$(A -BD^{-1}C)x = c -BD^{-1}d.$$
Nếu ma trận $A$ - $BD^{-1}C$ là khả nghịch, thì ta thu được nghiệm đến hệ của chúng ta
$$x = (A -BD^{-1}C)^{-1}(c -BD^{-1}d),$$
$$y = D^{-1}(d -C(A -BD^{-1}C)^{-1}(c -BD^{-1}d)).$$
Nếu $A$ là khả nghịch, thì bởi eliminating $x$ thứ nhất bằng cách sử dụng phương trình thứ nhất, ta thu được tương tự các công thức liên quan đến ma trận $D$ - $CA^{-1}B$. ở trên các công thức suggest rằng các ma trận $A$ - $BD^{-1}C$ và $D$ - $CA^{-1}B$ đóng đặc biệt vai trò và suggest sau đây định nghĩa:

> **Định nghĩa 43.1.** Cho trước bất kỳ $n \times  n$ ma trận khối (block matrix) của tạo thành
$$M = \begin{pmatrix} A & B \\ C & D \end{pmatrix} ,$$
Ở đâu $A$ là một ma trận cỡ $p \times  p$ và $D$ là một ma trận cỡ $q \times  q$, với $n = p + q$ (do đó $B$ là một ma trận cỡ $p \times  q$ và $C$ là một ma trận cỡ $q \times  p$), nếu $D$ là khả nghịch, thì ma trận $A$ - $BD^{-1}C$ được gọi là Phần bù Schur (Schur complement) của $D$ trong $M$. Nếu $A$ là khả nghịch, thì ma trận $D$ - $CA^{-1}B$ được gọi là Phần bù Schur (Schur complement) của $A$ trong $M$. ở trên các phương trình được viết như
$$x = (A -BD^{-1}C)^{-1}c -(A -BD^{-1}C)^{-1}BD^{-1}d,$$
$$y = -D^{-1}C(A -BD^{-1}C)^{-1}c$$
$$+ (D^{-1}+ D^{-1}C(A -BD^{-1}C)^{-1}BD^{-1})d,$$
Cho công thức cho nghịch đảo của $M$ theo Phần bù Schur (Schur complement) của $D$ trong $M$, cụ thể là
$$B^{-1}$$
$$\begin{pmatrix} A \\ C & D \end{pmatrix} = \begin{pmatrix} (A -BD^{-1}C)^{-1} & -(A -BD^{-1}C)^{-1}BD^{-1} \\ -D^{-1}C(A -BD^{-1}C)^{-1} & D^{-1}+ D^{-1}C(A -BD^{-1}C)^{-1}BD^{-1} \end{pmatrix} .$$
Moment của phép đối xứng (reflection) reveals rằng
$$B^{-1}$$
$$\begin{pmatrix} A \\ C & D \end{pmatrix} = \begin{pmatrix} (A -BD^{-1}C)^{-1} & 0 \\ -D^{-1}C(A -BD^{-1}C)^{-1} & D^{-1} \end{pmatrix} \begin{pmatrix} I & -BD^{-1} \\ 0 & I \end{pmatrix} ,$$
Và thì
$$B^{-1}$$
$$\begin{pmatrix} A \\ C & D \end{pmatrix} = \begin{pmatrix} I & 0 \\ -D^{-1}C & I \end{pmatrix} \begin{pmatrix} (A -BD^{-1}C)^{-1} & 0 \\ 0 & D^{-1} \end{pmatrix} \begin{pmatrix} I & -BD^{-1} \\ 0 & I \end{pmatrix} .$$
Bằng cách lấy các nghịch đảo, ta thu được kết quả sau kết quả.

<!-- PAGE 1567 -->

> **Mệnh đề 43.1.** Nếu ma trận $D$ là khả nghịch, thì
$$\begin{pmatrix} A & B \\ C & D \end{pmatrix} = \begin{pmatrix} I & BD^{-1} \\ 0 & I \end{pmatrix} \begin{pmatrix} A -BD^{-1}C & 0 \\ 0 & D \end{pmatrix} \begin{pmatrix} I & 0 \\ D^{-1}C & I \end{pmatrix} .$$
Ở trên biểu thức có thể được đã kiểm tra một cách trực tiếp và có advantage của đòi hỏi chỉ tính khả nghịch của $D$.
Nhận xét: Nếu $A$ là khả nghịch, thì ta có thể sử dụng Phần bù Schur (Schur complement) $D$ - $CA^{-1}B$ của $A$ để thu được sau đây nhân tử hóa của $M$:
$$\begin{pmatrix} A & B \\ C & D \end{pmatrix} = \begin{pmatrix} I & 0 \\ CA^{-1} & I \end{pmatrix} \begin{pmatrix} A & 0 \\ 0 & D -CA^{-1}B \end{pmatrix} \begin{pmatrix} I & A^{-1}B \\ 0 & I \end{pmatrix} .$$
Nếu $D$ - $CA^{-1}B$ là khả nghịch, ta có thể nghịch đảo tất cả ba các ma trận ở trên, và ta thu được một cái khác công thức cho nghịch đảo của $M$ theo $(D$ - $CA^{-1}B)$, cụ thể là,
$$B^{-1}$$
$$\begin{pmatrix} A \\ C & D \end{pmatrix} = \begin{pmatrix} A^{-1} + A^{-1}B(D -CA^{-1}B)^{-1}CA^{-1} & -A^{-1}B(D -CA^{-1}B)^{-1} \\ -(D -CA^{-1}B)^{-1}CA^{-1} & (D -CA^{-1}B)^{-1} \end{pmatrix} .$$
Nếu $A, D$ và cả hai Các phần bù Schur $A$ - $BD^{-1}C$ và $D$ - $CA^{-1}B$ là tất cả khả nghịch, bởi comparing hai các biểu thức cho $M^{-1}$, ta thu được (non-obvious) công thức
$$(A -BD^{-1}C)^{-1}= A^{-1}+ A^{-1}B(D -CA^{-1}B)^{-1}CA^{-1}.$$
Bằng cách sử dụng công thức này, ta thu được một cái khác biểu thức cho nghịch đảo của $M$ liên quan đến Các phần bù Schur của $A$ và $D$ (xem Horn và Johnson $[98])$:

> **Mệnh đề 43.2.** Nếu $A, D$ và cả hai Các phần bù Schur $A$ - $BD^{-1}C$ và $D$ - $CA^{-1}B$ là tất cả khả nghịch, thì
$$B^{-1}$$
$$\begin{pmatrix} A \\ C & D \end{pmatrix} = \begin{pmatrix} (A -BD^{-1}C)^{-1} & -A^{-1}B(D -CA^{-1}B)^{-1} \\ -(D -CA^{-1}B)^{-1}CA^{-1} & (D -CA^{-1}B)^{-1} \end{pmatrix} .$$
Nếu ta tập hợp $D =$ I và thay đổi $B$ đến $-B$, ta thu được
$$(A + BC)^{-1}= A^{-1}-A^{-1}B(I -CA^{-1}B)^{-1}CA^{-1},$$
Công thức đã biết như ma trận nghịch đảo bổ đề (xem Boyd và Vandenberghe $[29]$, Phụ lục C.4, especially C.4.3).
