# Afin Các phép đẳng cự (Cứng Motions)


<!-- PAGE 1006 -->
Nhận xét: Cho số tính ổn định, nó được ưu tiên hơn để sử dụng $w_{k+1} = r_{k+1,k+1} e_{k+1} + e^{-i\theta k+1}u_{k+1}''$ thay vì của $w_{k+1} = r_{k+1,k+1} e_{k+1}$ - $e^{-i\theta k+1}u_{k+1}''$. effect của rằng lựa chọn là rằng đường chéo các phần tử (entries) trong $R$ sẽ là của tạo thành $-e^{i\theta j}r_{j, j} = e^{i(\theta j+\pi)}r_{j, j}$. Của course, ta có thể tạo các phần tử (các phần tử (entries)) này nonegative bằng cách áp dụng
$$h_{n+1} = \rho_{en, \pi-\theta n}  \circ \cdots  \circ \rho_{e1,\pi-\theta1}$$
Sau $h_{n}$. Như trong Euclidean trường hợp, Mệnh đề 28.7 ngay lập tức suy ra Phân rã QR (QR-decomposition) cho tùy ý phức các ma trận cỡ $n\times n$, ở đâu $Q$ là bây giờ unita (xem Kincaid và Cheney $[105]$, Golub và Van Loan $[83]$, Trefethen và Bau $[182]$, hoặc Ciarlet $[41])$.

> **Mệnh đề 28.8.** Với mọi phức ma trận cỡ $n \times n$ $A$, có một dãy $H_{1}, \dots  , H_{n-1}$ của các ma trận, ở đâu mỗi $H_{i}$ là hoặc Ma trận Householder hoặc đồng nhất thức, và tam giác trên (upper triangular) ma trận $R$, sao cho
$$R = H_{n-1} \cdots  H_{2}H_{1}A.$$
Như hệ quả, có một cặp của các ma trận $Q, R$, ở đâu $Q$ là unita và $R$ là tam giác trên (upper triangular), sao cho $A = QR$ (Phân rã QR (QR-decomposition) của $A)$. Hơn nữa, $R$ có thể được được chọn sao cho của nó đường chéo các phần tử (entries) là không âm. Điều này có thể được đạt được bởi ma trận đường chéo (diagonal matrix) $D$ với các phần tử (entries) sao cho $|d_{ii}| = 1$ cho $i = 1, \dots  , n$, và ta có $A = QR$ với
$$e e$$
$$Q = H_{1} \cdots  H_{n-1}D,R = D^{*}R,$$
$$ee$$
Ở đâu $R$ là tam giác trên (upper triangular) và có không âm đường chéo các phần tử (entries) $e$

*Chứng minh.* Nó là về cơ bản đồng nhất đến chứng minh của Mệnh đề 13.4, và ta để lại chi tiết như một bài tập. Cho cuối cùng phát biểu, nhận thấy rằng $h_{n} \circ \cdots  \circ h_{1}$ là cũng phép đẳng cự (isometry). Như trong Euclidean trường hợp, Phân rã QR (QR-decomposition) có các ứng dụng đến bình phương tối thiểu (least squares) các bài tập. Nó là cũng khả dĩ/có thể đến chuyển đổi bất kỳ phức ma trận đến bidiagonal tạo thành.

## 28.2 Afin Các phép đẳng cự (Cứng Motions)

Trong mục này, ta study rất ngắn gọn afin các phép đẳng cự của Không gian Hermite (Hermitian space). Hầu hết các kết quả giữ cho Euclidean các không gian afin tổng quát hóa mà không có bất kỳ các bài tập đến Các không gian Hermite. đặc trưng của tập hợp của cố định các điểm của ánh xạ afin (affine map) là unchanged. Tương tự, mọi afin phép đẳng cự (isometry) $f$ (của Không gian Hermite (Hermitian space)) có thể được được viết một cách duy nhất như
$$f = t \circ g,witht \circ g = g \circ t,$$
Ở đâu $g$ là phép đẳng cự (isometry) có cố định điểm, và $t$ là phép tịnh tiến bởi vectơ $\tau$ sao cho $\longrightarrow f (\tau$) $= \tau$, và với một số additional đẹp các tính chất (xem Mệnh đề 28.13). tổng quát hóa

<!-- PAGE 1007 -->
Của Cartan–Dieudonn´e định lý có thể dễ dàng được hiển thị: mọi afin phép đẳng cự (isometry) trong $Is(n,\mathbb{C})$ có thể được viết dưới dạng hợp thành của nhiều nhất 2n - $1$ các phép đẳng cự nếu nó có cố định điểm, hoặc khác như hợp thành của nhiều nhất $2n+1$ các phép đẳng cự, ở đâu tất cả các phần tử này các phép đẳng cự là afin siêu phẳng (hyperplane) các phép đối xứng ngoại trừ cho có thể một afin Hermite phép đối xứng (reflection). Ta cũng chứng minh rằng mọi cứng motion trong $SE(n,\mathbb{C})$ là hợp thành của nhiều nhất 2n - $2$ flips (cho $n \ge 3)$.

> **Định nghĩa 28.2.** Cho trước bất kỳ hai không tầm thường Hermite các không gian afin $E$ và $F$ của cùng hữu hạn số chiều $n$, hàm $f$: $E \to F$ là afin phép đẳng cự (isometry) (hoặc cứng ánh xạ) khi và chỉ khi nó là ánh xạ afin (affine map) và
$$----\longrightarrow \longrightarrow$$
$$f(a)f(b) =ab ,$$
Với mọi, $b \in E$. Khi $E = F$, afin phép đẳng cự (isometry) $f$: $E \to E$ cũng được gọi là một cứng motion. Do đó, afin phép đẳng cự (isometry) là ánh xạ afin (affine map) rằng bảo toàn khoảng cách. Điều này là khá mạnh requirement, nhưng unlike Euclidean trường hợp, không mạnh đủ đến buộc $f$ là ánh xạ afin (affine map). sau đây đơn giản Mệnh đề là để lại như một bài tập.

> **Mệnh đề 28.9.** Cho trước bất kỳ hai không tầm thường Hermite các không gian afin $E$ và $F$ của cùng hữu hạn số chiều $n$, ánh xạ afin (affine map) $f$: $E \to F$ là afin phép đẳng cự (isometry) khi và chỉ khi của nó liên kết tuyến tính $\longrightarrow  \longrightarrow \longrightarrow$ ánh xạ $f$: $E \to F$ là phép đẳng cự (isometry). afin phép đẳng cự (isometry) là song ánh.
$$\longrightarrow$$
Như trong Euclidean trường hợp, cho trước afin phép đẳng cự (isometry) $f$: $E \to E$, nếu $f$ là phép quay, ta gọi
$$\longrightarrow$$
$f$ thực sự/đúng đắn (hoặc trực tiếp) afin phép đẳng cự (isometry), và nếu $f$ là suy rộng/không thực sự tuyến tính phép đẳng cự (isometry), ta gọi $f$ suy rộng/không thực sự (hoặc skew) afin phép đẳng cự (isometry). Dễ dàng chứng minh được rằng tập hợp của afin các phép đẳng cự
$$\longrightarrow$$
$f$: $E \to E$ các dạng nhóm, và những phần tử đó cho mà $f$ là phép quay là nhóm con. nhóm của afin các phép đẳng cự, hoặc cứng motions, là nhóm con của afin nhóm $GA(E,\mathbb{C})$ được ký hiệu như $Is(E,\mathbb{C})$ (hoặc $Is(n,\mathbb{C})$ khi $E = \mathbb{C}^{n})$. nhóm con của $Is(E,\mathbb{C})$ bao gồm của trực tiếp cứng motions là cũng nhóm con của $SA(E,\mathbb{C})$, và nó được ký hiệu là như $SE(E,\mathbb{C})$ (hoặc $SE(n,\mathbb{C})$,
$$\longrightarrow$$
Khi $E = \mathbb{C}^{n})$. các phép tịnh tiến là afin các phép đẳng cự $f$ cho mà $f =$ id, đồng nhất thức
$$\longrightarrow$$
Ánh xạ trên $E$. sau đây Mệnh đề là counterpart của Mệnh đề 14.14 cho các phép đẳng cự giữa Hermite các không gian vectơ.

> **Mệnh đề 28.10.** Cho trước bất kỳ hai không tầm thường Hermite các không gian afin $E$ và $F$ của cùng hữu hạn số chiều $n$, với mọi hàm $f$: $E \to F$, các tính chất sau đây là tương đương:
$$----\longrightarrow \longrightarrow$$
$(1) f$ là ánh xạ afin (affine map) và f()f(b) $=$ ab, với mọi, $b \in E$.
$$----\longrightarrow \longrightarrow$$
$(2)$ f()f(b) $=$ ab, và tồn tại một $\Omega \in E$ sao cho
$$---------\longrightarrow$$
$$\longrightarrow  \longrightarrow$$
$$f(\Omega + iab) = f(\Omega ) + i(f(\Omega )f(\Omega +ab)),$$
Với mọi, $b \in E$.

<!-- PAGE 1008 -->

*Chứng minh.* Hiển nhiên, $(1)$ suy ra $(2)$. chứng minh rằng rằng $(2)$ suy ra $(1)$ là đồng dạng đến chứng minh của Mệnh đề 27.7, nhưng sử dụng Mệnh đề 14.14 thay vì của Mệnh đề 12.12. chi tiết là để lại như một bài tập. Inspection của chứng minh chỉ ra ngay lập tức rằng Mệnh đề 27.8 nghiệm đúng cho Các không gian Hermite. Cho sake của tính đầy đủ, ta restate Mệnh đề trong phức trường hợp.

> **Mệnh đề 28.11.** Cho $E$ là bất kỳ phức không gian afin (affine space) của hữu hạn số chiều Với mọi ánh xạ afin (affine map) $f$: $E \to E$, cho Fix(f) $= {a \in E$ | f() $= a}$ là tập hợp của cố định các điểm của $f$. Các tính chất sau đây đúng:
$(1)$ Nếu $f$ có một số cố định điểm, sao cho Fix(f) $\neq  \emptyset$, thì Fix(f) là không gian con afin (affine subspace) của $E$ sao cho
$$\longrightarrow \longrightarrow$$
$$Fix(f) = a + E(1,f ) = a + \mathrm{Ker} (f -id),$$
$$\longrightarrow  \longrightarrow$$
Ở đâu E(1, $f$) là không gian riêng (eigenspace) của ánh xạ tuyến tính (linear map) $f$ cho trị riêng (eigenvalue) $1$.
$$\longrightarrow \longrightarrow$$
$(2)$ ánh xạ afin (affine map) $f$ có duy nhất cố định điểm khi và chỉ khi E(1, $f$) $=$ Ker ($f$ - id) $= {0}$. Afin trực giao các phép đối xứng được định nghĩa chỉ như trong Euclidean trường hợp, và Mệnh đề 27.9 cũng áp dụng đến phức các không gian afin.

> **Mệnh đề 28.12.** Cho trước bất kỳ afin phức không gian $E$, nếu $f$: $E \to E$ và $g: E \to E$ là afin trực giao các phép đối xứng về song song afin các không gian con $F_{1}$ và $F_{2}$, thì $g \circ f$ là
$$\longrightarrow  \longrightarrow$$
Phép tịnh tiến được định nghĩa bởi vectơ 2ab, ở đâu ab là bất kỳ vectơ vuông góc đến chung/phổ biến
$$\longrightarrow


$\longrightarrow$$$ direction $F$ of $F_{1}$ and $F_{2}$ such that ab  is the distance between $F_{1}$ and $F_{2}$, with $a \trong F_{1}$ and $b \trong F_{2}$. Conversely, every translation by a vector $\tau$  is obtained as the composition of two affine orthogonal symmetries about parallel affine subspaces $F_{1}$ and $F_{2}$ có chung/phổ biến
$$\longrightarrow$$
Hướng là trực giao đến $\tau  =$ ab, với một số $a \in F_{1}$ và một số $b \in F_{2}$ sao cho khoảng cách
$$\longrightarrow$$
Betwen $F_{1}$ và $F_{2}$ là ab $/2$. Nó là dễ để kiểm tra rằng chứng minh của Mệnh đề 27.10 cũng nghiệm đúng trong Hermite trường hợp.

> **Mệnh đề 28.13.** Cho $E$ là Hermite không gian afin (affine space) của hữu hạn số chiều $n$. Với mọi afin phép đẳng cự (isometry) $f$: $E \to E$, tồn tại duy nhất một afin phép đẳng cự (isometry) $g: E \to E$ và duy nhất
$$\longrightarrow \longrightarrow$$
Phép tịnh tiến $t = t_{\tau}$, với $f (\tau$) $= \tau$ (i.e., $\tau  \in$ Ker ($f$ - id)), sao cho tập hợp Fix(g) $= {a \in E$, | g() $= a}$ của cố định các điểm của $g$ là khác rỗng không gian con afin (affine subspace) của $E$ của hướng
$$\longrightarrow \longrightarrow  \longrightarrow$$
$$G = \mathrm{Ker} (f -id) = E(1,f ),$$
Và sao cho
$$f = t \circ gandt \circ g = g \circ t.$$
Hơn nữa, ta có kết quả sau additional các tính chất:

<!-- PAGE 1009 -->
() $f = g$ và $\tau  = 0$ khi và chỉ khi $f$ có một số cố định điểm, i.e., khi và chỉ khi Fix(f) $\neq  \emptyset$.
$$\longrightarrow$$
$(b)$ Nếu $f$ có không có cố định các điểm, i.e., Fix(f) $= \emptyset$, thì dim(Ker ($f$ - id)) $\ge 1$. các nhận xét được tạo trong Euclidean trường hợp cũng áp dụng đến Hermite trường hợp. Đặc biệt, sự kiện rằng $E$ có hữu hạn số chiều là chỉ được sử dụng để chứng minh $(b)$. phiên bản của Cartan–Dieudonn´e cũng nghiệm đúng cho afin các phép đẳng cự, nhưng nó có thể không là khả dĩ/có thể để thu được rid của Hermite các phép đối xứng hoàn toàn.

> **Định lý 28.14.** Cho $E$ là afin Không gian Hermite (Hermitian space) có số chiều $n \ge 1$. Mọi afin phép đẳng cự (isometry) trong $Is(n,\mathbb{C})$ có thể được viết dưới dạng hợp thành của nhiều nhất 2n - $1$ afin các phép đẳng cự nếu nó có cố định điểm, hoặc khác như hợp thành của nhiều nhất 2n $+ 1$ afin các phép đẳng cự, ở đâu tất cả các phần tử này các phép đẳng cự là afin siêu phẳng (hyperplane) các phép đối xứng ngoại trừ cho có thể một afin Hermite phép đối xứng (reflection). Khi $n \ge 2$, đồng nhất thức là hợp thành của bất kỳ phép đối xứng (reflection) với chính nó.

*Chứng minh.* chứng minh là rất đồng dạng đến chứng minh của Định lý 27.11, ngoại trừ rằng nó sử dụng Định lý 28.5 thay vì của Định lý 27.1. chi tiết là để lại như một bài tập. Khi $n \ge 3$, như trong Euclidean trường hợp, ta có thể đặc trưng hóa afin các phép đẳng cự trong $SE(n,\mathbb{C})$ theo flips, và ta có thể chẵn/ngay cả cận số của flips bởi 2n - $2$.

> **Định lý 28.15.** Cho $E$ là Hermite không gian afin (affine space) có số chiều $n \ge 3$. Mọi cứng motion $f \in SE(E,\mathbb{C})$ là hợp thành của chẵn/ngay cả số của afin flips $f = f_{2k} \circ \cdots  \circ f_{1}$, ở đâu $k \le n$ - $1$.

*Chứng minh.* Nó là rất đồng dạng đến chứng minh của định lý 27.12, nhưng nó sử dụng Mệnh đề 28.6 thay vì của Mệnh đề 27.5. chi tiết là để lại như một bài tập. nhiều hơn/thêm chi tiết study của cứng motions của Các không gian Hermite có số chiều $2$ và $3$ sẽ dường như worthwhile, nhưng ta là không biết của bất kỳ reference trên điều này subject.

<!-- PAGE 1010 -->
