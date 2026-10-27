# Hessenberg Các ma trận


<!-- PAGE 669 -->
Thu được bởi settting các phần tử (entries) của phần của $A_{k+1}$ ở dưới đường chéo đến $0$. Thì ta có thể tìm tương ứng các vectơ riêng (eigenvectors) bởi việc giải hệ phương trình tuyến tính
$$Tv = t_{ii}v,$$
Và vì $T$ là tam giác trên (upper triangular), điều này có thể được được thực hiện bởi bottom-up phép khử. Ta để lại nó như một bài tập để chỉ ra rằng sau đây các vectơ $v^{i} = (v_{1}^{i}, \dots  , v_{n}^{i})$ là các vectơ riêng (eigenvectors):
$$v^{1}= e_{1},$$
Và nếu $i = 2, \dots  , n$, thì
$$ \le  \le$$
$$0if i + 1jn$$
$$$$
$$$$
$$1if j = i$$
$$$$
$$v_{j}^{i} =$$
$$\cdots$$
$$- \frac{t_{jj+1}v_{j+1}^{i}+ + t_{ji}v_{i}^{i}}{t_{jj}-t_{ii}} if i -1 \ge j \ge 1.$$
Thì các vectơ $(P_{k}v^{1}, \dots  , P_{k}v^{n})$ là cơ sở (basis) của (xấp xỉ) các vectơ riêng (eigenvectors) cho $A$. Trong trường hợp đặc biệt khi $T$ là ma trận đường chéo (diagonal matrix), thì $v^{i} = e_{i}$ cho $i = 1, \dots  , n$ và các cột của $P_{k}$ là cơ sở trực chuẩn (orthonormal basis) của (xấp xỉ) các vectơ riêng (eigenvectors) cho $A$. Nếu $A$ là thực ma trận có các trị riêng (eigenvalues) là không tất cả thực, thì tồn tại một phức cặp của các trị riêng (eigenvalues) $\lambda  + i\mu$ (với $\mu  \neq  0)$, và QR-algorithm không thể hội tụ đến ma trận có chặt tam giác dưới (lower-triangular) phần là không. Có một cách đến deal với tình huống này bằng cách sử dụng trên Hessenberg các ma trận mà sẽ được thảo luận trong mục tiếp theo. Vì sự hội tụ của QR phương pháp phụ thuộc một cách then chốt chỉ trên sự kiện rằng phần của $A_{k}$ ở dưới đường chéo đi đến không, nó sẽ là một cách cao desirable nếu ta có thể thay thế $A$ bởi đồng dạng ma trận $U^{*}$ AU dễ dàng computable từ $A$ có các nhiều của không chặt ở dưới đường chéo. Ta có thể’t kỳ vọng $U^{*}$ AU là ma trận đường chéo (diagonal matrix) (vì điều này sẽ có nghĩa rằng $A$ đã là dễ dàng được chéo hóa), nhưng hóa ra là có một cách để xây dựng ma trận $H = U^{*}$ AU mà là hầu như tam giác, ngoại trừ rằng nó có thể có extra khác không đường chéo ở dưới chính đường chéo. Như vậy các ma trận được gọi là Hessenberg các ma trận được thảo luận trong mục tiếp theo.

## 18.2 Hessenberg Các ma trận


> **Định nghĩa 18.1.** một ma trận cỡ $n \times  n$ (thực hoặc phức) $H$ là (trên) Ma trận Hessenberg nếu nó là hầu như tam giác, ngoại trừ rằng nó có thể có extra khác không đường chéo ở dưới chính đường chéo. Technically, $h_{jk} = 0$ với mọi $(j, k)$ sao cho $j$ - $k \ge 2$. ma trận cỡ $5 \times  5$ ở dưới là ví dụ của Ma trận Hessenberg.
$$H = \begin{pmatrix} * & * & * & * & * \\ h_{21} & * & * & * & * \\ 0 & h_{32} & * & * & * \\ 0 & 0 & h_{43} & * & * \\ 0 & 0 & 0 & h_{54} \end{pmatrix} .$$
$$*$$

<!-- PAGE 670 -->
Kết quả sau đây có thể được được hiển thị.

> **Định lý 18.2.** Mọi $n \times  n$ phức hoặc thực ma trận $A$ là đồng dạng đến trên Ma trận Hessenberg $H$, nghĩa là, $A = UHU^{*}$ với một số ma trận unita (unitary matrix) $U$. Hơn nữa, $U$ có thể được được xây dựng như tích của Householder các ma trận (định nghĩa là cùng như trong Mục 13.1, ngoại trừ rằng $W$ là phức vectơ, và rằng tích vô hướng (inner product) là Hermite tích vô hướng (inner product) trên $\mathbb{C}^{n})$. Nếu $A$ là thực ma trận, thì $U$ là ma trận trực giao (orthogonal matrix) (và $H$ là thực ma trận). Định lý 18.2 và các thuật toán cho chuyển đổi ma trận đến Hessenberg tạo thành được thảo luận trong Trefethen và Bau $[182]$ (Lecture $26)$, Demmel $[48]$ (Mục 4.4.6, trong thực trường hợp), Serre $[162]$ (Định lý 13.1), và Meyer $[129]$ (Ví dụ 5.7.4, trong thực trường hợp). chứng minh của tính đúng đắn là không khó và sẽ là object của homework bài toán. sau đây các hàm được viết trong Matlab cài đặt hàm để tính Hessenberg tạo thành của ma trận. hàm house các xây dựng được chuẩn hóa vectơ $u$ định nghĩa Phép đối xứng Householder rằng các không điểm tất cả nhưng thứ nhất các phần tử (entries) trong vectơ $x$. hàm [uu, $u] =$ house(x) tol $= 2*10^(-15)$; % tolerance uu $= x; p =$ kích thước(x,1); % tính $l^1-norm$ của x(2:p,1) n1 $=$ tổng(abs(x(2:p,1))); nếu n1 $<=$ tol $u =$ các không điểm(p,1); uu $= u$; khác $l =$ sqrt(x’*x); % $l^2$ chuẩn (norm) của $x$ uu(1) $=$ x(1) $+$ signe(x(1))*l; $u = uu/sqrt(uu’*uu)$; kết thúc/cuối kết thúc/cuối hàm signe(z) returms $-1$ nếu $z < 0$, khác $+1$. hàm buildhouse xây dựng Phép đối xứng Householder từ vectơ uu. hàm $P =$ buildhouse(v,i) % hàm này xây dựng Phép đối xứng Householder % [I $0$ ] % $[0$ PP] % từ Phép đối xứng Householder % $PP =$ I - 2uu*uu’ % ở đâu uu $=$ v(i:n)

<!-- PAGE 671 -->
% Nếu uu $= 0$ thì $P$ - I % $n =$ kích thước(v,1); nếu v(i:n) $==$ các không điểm(n - $i +$ 1,1) $P =$ eye(n); khác $PP =$ eye(n - $i + 1)$ - 2*v(i:n)*v(i:n)’; $P =$ [eye(i-1) các không điểm(i-1, $n$ - $i + 1)$; các không điểm(n - $i + 1, i$ - $1)$ PP]; kết thúc/cuối kết thúc/cuối hàm Hessenberg1 tính trên Ma trận Hessenberg $H$ và ma trận trực giao (orthogonal matrix) $Q$ sao cho $A = Q^{\top}HQ$. hàm $[H, Q] =$ Hessenberg1() % % hàm này các xây dựng trên Hessenberg % ma trận $H$ và ma trận trực giao (orthogonal matrix) $Q$ sao cho % $A =$ Q’ $H Q n =$ kích thước(,1); $H = A; Q =$ eye(n); cho $i =$ 1:n-2 % $H(i+1:n,i)$ [~,u] $= house(H(i+1:n,i))$; % $u P =$ buildhouse(u,1); $Q(i+1:n,i:n) = P*Q(i+1:n,i:n); H(i+1:n,i:n) = H(i+1:n,i:n)$ - $2*u*(u’)*H(i+1:n,i:n); H(1:n,i+1:n) = H(1:n,i+1:n)$ - $2*H(1:n,i+1:n)*u*(u’)$; kết thúc/cuối kết thúc/cuối

> **Ví dụ 18.2.** Nếu
$$A = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 2 & 3 & 4 & 5 \\ 3 & 4 & 5 & 6 \\ 4 & 5 & 6 & 7 \end{pmatrix} ,$$

<!-- PAGE 672 -->
Chạy Hessenberg1 ta tìm
$$1.0000-5.385200$$
$$-5.385215.2069-1.6893-0.0000$$
$$H =$$
$$-0.0000-1.6893-0.2069-0.0000$$
$$$$
$$0-0.00000.00000.0000$$
$$1.0000000$$
$$0-0.3714-0.5571-0.7428$$
$$Q =.$$
$$00.83390.1516-0.5307$$
$$$$
$$00.4082-0.81650.4082$$
Quan trọng tính chất của (trên) Hessenberg các ma trận là rằng nếu một số subdiagonal phần tử (entry) $H_{p+1p} = 0$, thì $H$ là của tạo thành
$$H = \begin{pmatrix} H_{11} & H_{12} \\ 0 & H_{22} \end{pmatrix} ,$$
Ở đâu cả hai $H_{11}$ và $H_{22}$ là trên Hessenberg các ma trận (với $H_{11}$ một ma trận cỡ $p \times  p$ và $H_{22}$ $(n$ - $p) \times  (n$ - $p)$ ma trận), và các trị riêng (eigenvalues) của $H$ là các trị riêng (eigenvalues) của $H_{11}$ và $H_{22}$. Ví dụ, trong ma trận
$$H = \begin{pmatrix} * & * & * & * & * \\ h_{21} & * & * & * & * \\ 0 & h_{32} & * & * & * \\ 0 & 0 & h_{43} & * & * \\ 0 & 0 & 0 & h_{54} \end{pmatrix} ,$$
$$*$$
Nếu $h_{43} = 0$, thì ta có ma trận khối (block matrix)
$$H = \begin{pmatrix} * & * & * & * & * \\ h_{21} & * & * & * & * \\ 0 & h_{32} & * & * & * \\ 0 & 0 & 0 & * & * \\ 0 & 0 & 0 & h_{54} \end{pmatrix} .$$
$$*$$
Thì danh sách của các trị riêng (eigenvalues) của $H$ là concatenation của danh sách của các trị riêng (eigenvalues) của $H_{11}$ và danh sách của các trị riêng (eigenvalues) của $H_{22}$. Điều này là dễ dàng được thấy bằng quy nạp theo số chiều của khối $H_{11}$. Tổng quát hơn, mọi trên Ma trận Hessenberg có thể được được viết trong như vậy cách rằng nó có đường chéo các khối rằng là Hessenberg các khối có subdiagonal là không không.

> **Định nghĩa 18.2.** trên Hessenberg $n \times  n$ ma trận $H$ là unreduced nếu $h_{i+1i} \neq  0$ cho $i = 1, \dots  , n$ - $1$. Ma trận Hessenberg mà là không unreduced được nói là rút gọn.

<!-- PAGE 673 -->
Sau đây là ví dụ của một ma trận cỡ $8 \times  8$ bao gồm của ba đường chéo unreduced Hessenberg các khối:
$$H = \begin{pmatrix} ⋆ & ⋆ & ⋆ & * & * & * & * & * \\ h_{21} & ⋆ & ⋆ & * & * & * & * & * \\ 0 & h_{32} & ⋆ & * & * & * & * & * \\ 0 & 0 & 0 & ⋆ & ⋆ & ⋆ & * & * \\ 0 & 0 & 0 & h_{54} & ⋆ & ⋆ & * & * \\ 0 & 0 & 0 & 0 & h_{65} & ⋆ & * & * \\ 0 & 0 & 0 & 0 & 0 & 0 & ⋆ & ⋆ \\ 0 & 0 & 0 & 0 & 0 & 0 & h_{87} & ⋆ \end{pmatrix} .$$
Thú vị và quan trọng tính chất của unreduced Hessenberg các ma trận là sau đây.

> **Mệnh đề 18.3.** Cho $H$ là $n \times  n$ phức hoặc thực unreduced Ma trận Hessenberg. Thì mọi trị riêng (eigenvalue) của $H$ là geometrically đơn giản, nghĩa là, $dim(E_{\lambda}) = 1$ với mọi trị riêng (eigenvalue) $\lambda$, ở đâu $E_{\lambda}$ là không gian riêng (eigenspace) liên kết với $\lambda$. Hơn nữa, nếu $H$ là chéo hóa được (diagonalizable), thì mọi trị riêng (eigenvalue) là đơn giản, nghĩa là, $H$ có $n$ phân biệt các trị riêng (eigenvalues).

*Chứng minh.* Ta suy ra Serre’s chứng minh $[162]$ (Mệnh đề 3.26). Cho $\lambda$ là bất kỳ trị riêng (eigenvalue) của $H$, cho $M = \lambda I_{n}$ - $H$, và cho $N$ là $(n$ - $1) \times  (n$ - $1)$ ma trận thu được từ $M$ bởi xóa của nó hàng thứ nhất và của nó cột cuối cùng. Vì $H$ là trên Hessenberg, $N$ là ma trận đường chéo (diagonal matrix) với các phần tử (entries) $-h_{i+1i} \neq  0, i = 1, \dots  , n$ - $1$. Do đó $N$ là khả nghịch và có hạng (rank) $n$ - $1$. Nhưng ma trận có hạng (rank) greater hơn hoặc bằng hạng (rank) của bất kỳ của của nó submatrices, do đó hạng (rank)(M) $= n$ - $1$, vì $M$ là suy biến. Bởi rank-nullity định lý, hạng (rank)(Ker $N) = 1$, nghĩa là, $dim(E_{\lambda}) = 1$, như đã khẳng định. Nếu $H$ là chéo hóa được (diagonalizable), thì tổng của số chiều của các không gian riêng (eigenspace) bằng $n$, mà suy ra rằng các trị riêng (eigenvalues) của $H$ là phân biệt. Như ta được nói trước đó, trường hợp ở đâu Định lý 18.1 áp dụng là trường hợp ở đâu $A$ là đối xứng (hoặc Hermite) xác định dương (positive definite) ma trận. Điều này suy ra từ hai các sự kiện. thứ nhất sự kiện là rằng nếu $A$ là Hermite (hoặc đối xứng trong thực trường hợp), thì nó là dễ để chỉ ra rằng Ma trận Hessenberg đồng dạng đến $A$ là Hermite (hoặc đối xứng trong thực trường hợp) ma trận ba đường chéo (tridiagonal matrix). conversion phương pháp là cũng nhiều hơn/thêm efficient. Đây là một ví dụ của đối xứng ma trận ba đường chéo (tridiagonal matrix) bao gồm của ba unreduced các khối:
$$H = \begin{pmatrix} \alpha_{1} & \beta_{1} & 0 & 0 & 0 & 0 & 0 & 0 \\ \beta_{1} & \alpha_{2} & \beta_{2} & 0 & 0 & 0 & 0 & 0 \\ 0 & \beta_{2} & \alpha_{3} & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & \alpha_{4} & \beta_{4} & 0 & 0 & 0 \\ 0 & 0 & 0 & \beta_{4} & \alpha_{5} & \beta_{5} & 0 & 0 \\ 0 & 0 & 0 & 0 & \beta_{5} & \alpha_{6} & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & \alpha_{7} & \beta_{7} \\ 0 & 0 & 0 & 0 & 0 & 0 & \beta_{7} & \alpha_{8} \end{pmatrix} .$$

<!-- PAGE 674 -->
Do đó bài toán của việc tìm các trị riêng (eigenvalues) của đối xứng (hoặc Hermite) ma trận rút gọn đến bài toán của việc tìm các trị riêng (eigenvalues) của đối xứng (resp. Hermite) ma trận ba đường chéo (tridiagonal matrix), và điều này có thể được được thực hiện nhiều nhiều hơn/thêm efficiently. thứ hai sự kiện là rằng nếu $H$ là trên Ma trận Hessenberg và nếu nó là chéo hóa được (diagonalizable), thì có một ma trận khả nghịch (invertible matrix) $P$ sao cho $H = P\Lambda P^{-1}$ với $\Lambda$ ma trận đường chéo (diagonal matrix) bao gồm của các trị riêng (eigenvalues) của $H$, sao cho $P^{-1}$ có Phân rã LU (LU-decomposition); xem Serre $[162]$ (Định lý 13.3). Hệ quả là, vì bất kỳ đối xứng (hoặc Hermite) ma trận ba đường chéo (tridiagonal matrix) là khối ma trận đường chéo (diagonal matrix) của unreduced đối xứng (resp. Hermite) ba đường chéo các ma trận, theo Mệnh đề 18.3, ta xem rằng QR thuật toán ứng dụng đến ma trận ba đường chéo (tridiagonal matrix) mà là đối xứng (hoặc Hermite) xác định dương (positive definite) hội tụ đến ma trận đường chéo (diagonal matrix) bao gồm của các trị riêng (các trị riêng (eigenvalues)) của nó. Cho chúng ta record điều này quan trọng sự kiện.

> **Định lý 18.4.** Cho $H$ là đối xứng (hoặc Hermite) xác định dương (positive definite) ma trận ba đường chéo (tridiagonal matrix). Nếu $H$ là unreduced, thì QR thuật toán hội tụ đến ma trận đường chéo (diagonal matrix) bao gồm của các trị riêng (eigenvalues) của $H$. Vì mọi đối xứng (hoặc Hermite) xác định dương (positive definite) ma trận là đồng dạng đến ba đường chéo đối xứng (resp. Hermite) xác định dương (positive definite) ma trận, ta suy ra rằng ta có phương pháp cho việc tìm các trị riêng (eigenvalues) của đối xứng (resp. Hermite) xác định dương (positive definite) ma trận (nhiều hơn/thêm accurately, để tìm các xấp xỉ như tốt như ta muốn cho các trị riêng (các trị riêng (eigenvalues)) này). Nếu $A$ là đối xứng (hoặc Hermite) ma trận, vì các trị riêng (các trị riêng (eigenvalues)) của nó là thực, với một số $\mu  > 0$ lớn đủ (chọn $\mu  > \rho (A)), A + \mu$ I là đối xứng (resp. Hermitan) xác định dương (positive definite), do đó ta có thể áp dụng QR thuật toán đến trên Ma trận Hessenberg đồng dạng đến $A + \mu$ I để tìm các trị riêng (các trị riêng (eigenvalues)) của nó, và thì các trị riêng (eigenvalues) của $A$ là thu được bằng cách trừ $\mu$. bài toán của việc tìm các trị riêng (eigenvalues) của ma trận đối xứng (symmetric matrix) được thảo luận extensively trong Parlett $[140]$, một của tốt nhất references trên điều này topic. trên Hessenberg tạo thành cũng cho ta cách đến handle suy biến các ma trận. Thứ nhất, kiểm tra chứng minh của Mệnh đề 14.21 rằng $n \times  n$ phức ma trận $A$ (có thể suy biến) có thể được được nhân tử như $A = QR$ ở đâu $Q$ là ma trận unita (unitary matrix) mà là tích của Householder các phép đối xứng và $R$ là tam giác trên (upper triangular), nó là dễ để xem rằng nếu $A$ là trên Hessenberg, thì $Q$ là cũng trên Hessenberg. Nếu $H$ là unreduced trên Ma trận Hessenberg, vì $Q$ là trên Hessenberg và $R$ là tam giác trên (upper triangular), ta có $h_{i+1i} = q_{i+1i}r_{ii}$ cho $i = 1 \dots  , n -1$, và vì $H$ là unreduced, $r_{ii} \neq  0$ cho $i = 1, \dots  , n -1$. Hệ quả là $H$ là suy biến khi và chỉ khi $r_{nn} = 0$. Thì ma trận $RQ$ là ma trận có hàng cuối cùng bao gồm của không’s do đó ta có thể deflate bài toán bởi xét $(n$ - $1) \times  (n$ - $1)$ unreduced Ma trận Hessenberg thu được bởi xóa hàng cuối cùng và cột cuối cùng. Sau một cách hữu hạn nhiều các bước (không lớn hơn rằng bội (multiplicity) của trị riêng (eigenvalue) $0)$, ở đó vẫn còn khả nghịch unreduced Ma trận Hessenberg. Như alternative, xem Serre $[162]$ (Chương $13$, Mục 13.3.2). Như là, QR thuật toán, mặc dù rất đơn giản, là khá inefficient cho một vài các lý do. Trong mục tiếp theo, ta indicate cách mà để tạo phương pháp nhiều hơn/thêm efficient. Điều này liên quan đến nhiều hoạt động/công trình và ta chỉ thảo luận chính các ý tưởng tại cao mức.
