# Krylov Các không gian con; Phép lặp Arnoldi (Arnoldi iteration)


<!-- PAGE 680 -->
$(h_{i+1i} \neq  0$ cho $i = 1, \dots$, n-1), thì các cột của chỉ số $2, \dots  , n$ của $U$ được xác định bởi cột thứ nhất của $U$ sai khác dấu; xem Demmel $[48]$ (Định lý 4.9) và Golub và Van Loan $[83]$ (Định lý 7.4.2) cho chứng minh trong trường hợp của thực các ma trận. Thực sự, chứng minh là không khó và sẽ là object của homework bài tập. Trong trường hợp của đơn lẻ shift, ẩn shift sinh ra $A_{k+1} = Q_{k}^{*}A_{k}Q_{k}$ mà không có có để tính Nhân tử hóa QR (QR-factorization) của $A_{k}$ - $\sigma_{k}$ I. Cho thực các ma trận, điều này được thực hiện bằng cách áp dụng dãy của các cho trước các phép quay mà perform bulge chasing process (các cho trước phép quay là trực giao khối ma trận đường chéo (diagonal matrix) bao gồm của đơn lẻ khối mà là 2D phép quay, khác đường chéo các phần tử (entries) đang là bằng $1)$. Tương tự, trong trường hợp của gấp đôi shift, $A_{k+2} = (Q_{k}Q_{k+1})^{*}A_{k}Q_{k}Q_{k+1}$ được sinh mà không có có để tính QR-factorizations của $A_{k}$ - $\sigma_{k}$ I và $A_{k+1}$ - $\overline{\sigma}_{k}I$. Một lần nữa, $(Q_{k}Q_{k+1})^{*}A_{k}Q_{k}Q_{k+1}$ được sinh bằng cách áp dụng một số đơn giản các ma trận trực giao mà perform bulge chasing process. Xem Demmel $[48]$ (Mục 4.4.8) và Golub và Van Loan $[83]$ (Mục 7.5) cho further explanations regarding ẩn shifting liên quan đến bulge chasing trong trường hợp của thực các ma trận. Watkins $[193, 194]$ các thảo luận bulge chasing trong nhiều hơn/thêm tổng quát trường hợp của phức các ma trận. Matlab hàm cho việc tìm các trị riêng (eigenvalues) và các vectơ riêng (eigenvectors) của ma trận $A$ là eig và được gọi là như $[U, D] =$ eig(). Nó được cài đặt bằng cách sử dụng optimized phiên bản của QR-algorithm với ẩn shifts. Nếu số chiều của ma trận $A$ là rất lớn, ta có thể tìm các xấp xỉ của một số của các trị riêng (eigenvalues) của $A$ bằng cách sử dụng truncated phiên bản của reduction đến Hessenberg tạo thành do Arnoldi nói chung và đến Lanczos trong đối xứng (hoặc Hermite) ba đường chéo trường hợp.

## 18.4 Krylov Các không gian con; Phép lặp Arnoldi (Arnoldi iteration)

Trong mục này, ta ký hiệu số chiều của square thực hoặc phức ma trận $A$ bởi $m$ thay vì $n$, để tạo nó dễ hơn cho độc giả đến suy ra Trefethen và Bau trình bày $[182]$, mà là một cách cụ thể lucid. Giả sử rằng ma trận cỡ $m \times  m$ $A$ có đã được rút gọn đến trên Hessenberg tạo thành $H$, như $A = UHU^{*}$. Với mọi $n \le m$ (typically nhiều nhỏ hơn hơn $m)$, xét $(n + 1) \times  n$ trên trái khối
$$H_{n}e = \begin{pmatrix} h_{11} & h_{12} & h_{13} & \cdots & h_{1n} \\ h_{21} & h_{22} & h_{23} & \cdots & h_{2n} \\ 0 & h_{32} & h_{33} & \cdots & h_{3n} \\ \vdots & \ddots & \ddots & \ddots & \vdots \\ 0 & \cdots & 0 & h_{nn-1} & h_{nn} \\ 0 & \cdots & 0 & 0 & h_{n+1n} \end{pmatrix}$$

<!-- PAGE 681 -->
Của $H$, và $n \times  n$ trên Ma trận Hessenberg $H_{n}$ thu được bởi xóa hàng cuối cùng của $H_{n}$,
$$e$$
$$H_{n} = \begin{pmatrix} h_{11} & h_{12} & h_{13} & \cdots & h_{1n} \\ h_{21} & h_{22} & h_{23} & \cdots & h_{2n} \\ 0 & h_{32} & h_{33} & \cdots & h_{3n} \\ \vdots & \ddots & \ddots & \ddots & \vdots \\ 0 & \cdots & 0 & h_{nn-1} & h_{nn} \end{pmatrix} .$$
Nếu ta ký hiệu bởi $U_{n}$ ma trận cỡ $m\times n$ bao gồm của thứ nhất $n$ các cột của $U$, được ký hiệu $u_{1}, \dots  , u_{n}$, thì ma trận bao gồm của thứ nhất $n$ các cột của ma trận $UH = AU$ có thể được biểu diễn dưới dạng
$$AU_{n} = U_{n+1}H_{n}.(*_{1})$$
$$e$$
Suy ra rằng cột thứ $n$ của ma trận này có thể được biểu diễn dưới dạng
$$Au_{n} = h_{1n}u_{1} + \cdots  + h_{nn}u_{n} + h_{n+1n}u_{n+1}.(*_{2})$$
Vì $(u_{1}, \dots  , u_{n})$ tạo thành cơ sở trực chuẩn (orthonormal basis), ta suy ra từ $(*_{2})$ rằng
$$\langle u_{j}, Au_{n}\rangle = u_{j}^{*}Au_{n} = h_{jn},j = 1, \dots  , n.(*_{3})$$
Các phương trình $(*_{2})$ và $(*_{3})$ chỉ ra rằng $U_{n+1}$ và $H_{n}$ có thể được được tính một cách lặp bằng cách sử dụng
$$e$$
Sau đây thuật toán do Arnoldi, đã biết như Phép lặp Arnoldi (Arnoldi iteration): Cho trước tùy ý khác không vectơ $b \in \mathbb{C}^{m}$, cho $u_{1} = b/ \|b\|$; cho $n = 1, 2, 3, \dots$ thực hiện $z := Au_{n}$; cho $j = 1$ đến $n$ thực hiện $h_{jn} := u_{j}^{*}z; z := z$ - $h_{jn}u_{j}$ endfor $h_{n+1n} := \|z\|$; nếu $h_{n+1n} = 0$ quit $u_{n+1} = z/h_{n+1n}$ Khi $h_{n+1n} = 0$, ta nói rằng ta có breakdown của Phép lặp Arnoldi (Arnoldi iteration). Phép lặp Arnoldi (Arnoldi iteration) là thuật toán cho producing $n\times n$ Hessenberg ma trận con $H_{n}$ của đầy đủ Ma trận Hessenberg $H$ bao gồm của của nó thứ nhất $n$ các hàng và $n$ các cột (thứ nhất $n$ các cột của $U$ là cũng produced), không bằng cách sử dụng Householder các ma trận. Như dài như $h_{j+1j}$ ̸ $= 0$ cho $j = 1, \dots  , n$, Phương trình $(*_{2})$ chỉ ra bởi dễ quy nạp rằng $u_{n+1}$ thuộc đến sinh (span) của $(b$, Ab, $\dots  , A^{n}b)$, và hiển nhiên $Au_{n}$ thuộc đến sinh (span) của $(u_{1}, \dots  , u_{n+1})$, và do đó sau đây các không gian là đồng nhất:
$$Span(b, Ab, \dots  , A^{n}b) = Span(u_{1}, \dots  , u_{n+1}).$$

<!-- PAGE 682 -->
Không gian $\mathcal{K}_{n}(A, b) =$ Sinh (span)(b, Ab, $\dots  , A^{n-1}b)$ được gọi là một Krylov không gian con. Ta có thể quan điểm Arnoldi’s thuật toán như cách xây dựng của cơ sở trực chuẩn (orthonormal basis) cho $\mathcal{K}_{n}(A, b)$. Nó là sort của Gram–Schmidt quy trình. Phương trình $(*_{2})$ chỉ ra rằng nếu $K_{n}$ là ma trận cỡ $m \times  n$ có các cột là các vectơ $(b$, Ab, $\dots  , A^{n-1}b)$, thì có một $n \times  n$ tam giác trên (upper triangular) ma trận $R_{n}$ sao cho
$$K_{n} = U_{n}R_{n}.(*_{4})$$
Ở trên được gọi là một rút gọn QR nhân tử hóa của $K_{n}$. Vì $(u_{1}, \dots  , u_{n})$ là trực chuẩn hệ, ma trận $U_{n}^{*} U_{n+1}$ là ma trận cỡ $n\times (n+1)$ bao gồm của ma trận đơn vị (identity matrix) $I_{n}$ cộng extra cột của 0’s, do đó $U_{n}^{*} U_{n+1}H_{n} = U_{n}^{*}AU_{n}$ là
$$e$$
Thu được bởi xóa hàng cuối cùng của $H_{n}$, cụ thể là $H_{n}$, và do đó
$$e$$
$$U_{n}^{*} AU_{n} = H_{n}.(*_{5})$$
Ta summarize ở trên các sự kiện trong sau đây mệnh đề.

> **Mệnh đề 18.5.** Nếu Phép lặp Arnoldi (Arnoldi iteration) chạy trên một ma trận cỡ $m \times  m$ $A$ bắt đầu với khác không
$$\mathbb{C}^{m}$$
Vectơ $b \in$ thực hiện không có breakdown tại giai đoạn $n \le m$, thì các tính chất sau đây đúng:
$(1)$ Nếu $K_{n}$ là $m \times  n$ Krylov ma trận liên kết với các vectơ $(b$, Ab, $\dots  , A^{n-1}b)$ và nếu $U_{n}$ là ma trận cỡ $m \times  n$ của trực giao các vectơ produced bởi Phép lặp Arnoldi (Arnoldi iteration), thì có một Nhân tử hóa QR (QR-factorization)
$$K_{n} = U_{n}R_{n},$$
Với một số $n \times  n$ tam giác trên (upper triangular) ma trận $R_{n}$.
$(2)$ $m \times  n$ trên Hessenberg các ma trận $H_{n}$ produced bởi Phép lặp Arnoldi (Arnoldi iteration) là phép chiếu của $A$ lên Krylov không gian $\mathcal{K}_{n}(A, b)$, nghĩa là,
$$H_{n} = U_{n}^{*} AU_{n}.$$
$(3)$ successive iterates là related bởi công thức
$$AU_{n} = U_{n+1}H_{n}.$$
$$e$$
Nhận xét: Nếu Phép lặp Arnoldi (Arnoldi iteration) có breakdown tại giai đoạn $n$, nghĩa là, $h_{n+1} = 0$, thì ta tìm thấy thứ nhất unreduced khối của Ma trận Hessenberg $H$. Nó có thể được được hiển thị rằng các trị riêng (eigenvalues) của $H_{n}$ là các trị riêng (eigenvalues) của $A$. Do đó breakdown là thực sự tốt thing. Trong trường hợp này, ta có thể chọn một số mới khác không vectơ $u_{n+1}$ trực giao đến các vectơ $(u_{1}, \dots  , u_{n})$ như mới bắt đầu vectơ và chạy Phép lặp Arnoldi (Arnoldi iteration) một lần nữa. Như vậy vectơ tồn tại vì $(n +$ 1)th cột của $U$ hoạt động. Do đó repeated ứng dụng của Arnoldi cho ta đầy đủ Hessenberg reduction của $A$. Tuy nhiên,

<!-- PAGE 683 -->
Điều này là không những gì ta là sau, vì $m$ là rất lớn ta là chỉ interested trong “nhỏ” số của các trị riêng (eigenvalues) của $A$. Ở đó là một cái khác aspect của Phép lặp Arnoldi (Arnoldi iteration), mà là rằng nó giải tối ưu hóa bài toán liên quan đến các đa thức của bậc $n$. Cho $\mathcal{P}^{n}$ ký hiệu tập hợp của (phức) chuẩn hóa (monic) các đa thức của bậc $n$, nghĩa là, các đa thức của tạo thành
$$\mathbb{C}$$
$$p(z) = z^{n}+ c_{n-1}z^{n-1}+ \cdots  + c_{1}z + c_{0}(c_{i} \in ).$$
Cho bất kỳ ma trận cỡ $m \times  m$ $A$, ta viết
$$p(A) = A^{n}+ c_{n-1}A^{n-1}+ \cdots  + c_{1}A + c_{0}I.$$
Kết quả sau đây được chứng minh trong Trefethen và Bau $[182]$ (Lecture $34$, Định lý 34.1).

> **Định lý 18.6.** Nếu Phép lặp Arnoldi (Arnoldi iteration) chạy trên một ma trận cỡ $m \times  m$ $A$ bắt đầu với khác không vectơ $b$ thực hiện không có breakdown tại giai đoạn $n \le m$, thì tồn tại duy nhất một đa thức $p \in P^{n}$ sao cho $\|p(A)b\|_{2}$ là cực tiểu, cụ thể là đa thức đặc trưng (characteristic polynomial) det(zI - $H_{n})$ của $H_{n}$. Định lý 18.6 có thể được được quan điểm như “justification” cho phương pháp để tìm một số của các trị riêng (eigenvalues) của $A$ (nói $n \ll m$ của chúng). Một cách trực quan, closer các nghiệm của characteristic các đa thức của $H_{n}$ là đến các trị riêng (eigenvalues) của $A$, nhỏ hơn $\|p(A)b\|_{2}$ nên là, và ngược lại. Trong extreme trường hợp ở đâu $m = n$, bởi Cayley–Hamilton định lý, p() $= 0$ (ở đâu $p$ là đa thức đặc trưng (characteristic polynomial) của $A)$, do đó điều này ý tưởng là plausible, nhưng điều này là far từ constituting chứng minh (cũng, $b$ nên có khác không các tọa độ trong tất cả các hướng liên kết với các trị riêng (eigenvalues)). phương pháp đã biết như Rayleigh–Ritz phương pháp là đến chạy Phép lặp Arnoldi (Arnoldi iteration) trên $A$ và một số $b \neq  0$ được chọn tại ngẫu nhiên cho $n \ll m$ các bước trước hoặc cho đến khi breakdown xảy ra. Thì chạy QR thuật toán với shifts trên $H_{n}$. các trị riêng (eigenvalues) của Ma trận Hessenberg $H_{n}$ có thể thì được xét như các xấp xỉ của các trị riêng (eigenvalues) của $A$. các trị riêng (eigenvalues) của $H_{n}$ được gọi là Arnoldi estimates hoặc Ritz các giá trị. Một có là cautious bởi vì $H_{n}$ là truncated phiên bản của đầy đủ Ma trận Hessenberg $H$, do đó không tất cả của Ritz các giá trị là nhất thiết close đến các trị riêng (eigenvalues) của $A$. Nó có đã được được quan sát rằng các trị riêng (eigenvalues) rằng là tìm thấy thứ nhất là extreme các trị riêng (eigenvalues) của $A$, cụ thể là những phần tử đó close đến biên (boundary) của phổ (spectrum) của $A$ plotted trong $\mathbb{C}$. Do đó nếu $A$ có thực các trị riêng (eigenvalues), lớn nhất và nhỏ nhất các trị riêng (eigenvalues) xuất hiện thứ nhất như Ritz các giá trị. Trong nhiều các bài tập ở đâu các trị riêng (eigenvalues) xảy ra, extreme các trị riêng (eigenvalues) là một rằng cần được tính. Tương tự, các vectơ riêng (eigenvectors) của $H_{n}$ có thể được xét như các xấp xỉ của các vectơ riêng (eigenvectors) của $A$. Matlab hàm eigs là based trên phép tính của Ritz các giá trị. Nó tính sáu các trị riêng (eigenvalues) của lớn nhất magnitude của ma trận $A$, và gọi là $[V, D] =$ eigs(). Tổng quát hơn, để thu được đỉnh/trên $k$ các trị riêng (eigenvalues), sử dụng $[V, D] =$ eigs(, $k)$. Trong absence của chặt chẽ các định lý về sai số estimates, nó là khó để tạo ở trên các phát biểu nhiều hơn/thêm precise; xem Trefethen và Bau $[182]$ (Lecture $34)$ cho nhiều hơn/thêm trên điều này subject.
