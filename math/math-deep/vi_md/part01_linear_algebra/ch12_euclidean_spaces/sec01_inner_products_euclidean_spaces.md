# Trong Các tích, Các không gian Euclid


<!-- PAGE 453 -->
Chương $12$ Các không gian Euclid Rien n’est beau que le vrai. —Hermann Minkowski

## 12.1 Trong Các tích, Các không gian Euclid

Do đó far khung lý thuyết của các không gian vectơ cho phép chúng ta đến deal với các tỉ số của các vectơ và các tổ hợp tuyến tính, nhưng không có cách đến biểu diễn khái niệm của góc hoặc đến talk về tính trực giao của các vectơ. Euclidean cấu trúc cho phép chúng ta đến deal với mêtric các khái niệm chẳng hạn như các góc, tính trực giao, và độ dài (hoặc khoảng cách). Điều này chương phủ bare bones của Euclidean hình học. Deeper aspects của Euclidean hình học là investigated trong Chương $13$. Một của của ta chính các mục tiêu là đến cho cơ bản các tính chất của các phép biến đổi rằng bảo toàn Euclidean cấu trúc, các phép quay và các phép đối xứng, vì chúng đóng quan trọng vai trò trong thực tế. Euclidean hình học là study của các tính chất bất biến dưới nhất định các ánh xạ afin được gọi là cứng motions. Cứng motions là các ánh xạ rằng bảo toàn khoảng cách giữa các điểm. Ta bắt đầu bởi định nghĩa trong các tích và Các không gian Euclid. Cauchy–Schwarz bất đẳng thức và Minkowski bất đẳng thức được hiển thị. Ta định nghĩa tính trực giao của các vectơ và của các không gian con, trực giao các cơ sở, và các cơ sở trực chuẩn. Ta chứng minh rằng mọi hữu hạn chiều Không gian Euclid (Euclidean space) có các cơ sở trực chuẩn. thứ nhất chứng minh sử dụng đối ngẫu và thứ hai một Gram–Schmidt orthogonalization quy trình. Phân rã QR (QR-decomposition) cho các ma trận khả nghịch được hiển thị như ứng dụng của Gram–Schmidt quy trình. Tuyến tính các phép đẳng cự (cũng được gọi là trực giao các phép biến đổi) được định nghĩa và studied ngắn gọn. Ta kết luận với ngắn mục trong mà một số các ứng dụng của Euclidean hình học được phác thảo. Một của hầu hết quan trọng các ứng dụng, phương pháp của bình phương tối thiểu (least squares), được thảo luận trong Chương $23$. Cho nhiều hơn/thêm chi tiết treatment của Euclidean hình học xem Berger $[11, 12]$, Snapper và Troyer $[168]$, hoặc bất kỳ khác cuốn sách trên hình học, chẳng hạn như Pedoe $[141]$, Coxeter $[44]$, Fresnel $[66]$, Tisseron $[181]$, hoặc Cagnac, Ramis, và Commeau $[32]$. Serious độc giả nên consult Emil
$$453$$

<!-- PAGE 454 -->
Artin’s nổi tiếng cuốn sách $[6]$, mà chứa in-depth study của trực giao nhóm, cũng như khác các nhóm phát sinh trong hình học. Nó là vẫn worth consulting một số của older classics, chẳng hạn như Hadamard $[87, 88]$ và Rouch´e và de Comberousse $[144]$. thứ nhất ấn bản của $[87]$ đã là published trong $1898$ và cuối cùng đạt tới của nó thirteenth ấn bản trong $1947$! Trong chương này nó được giả sử rằng tất cả các không gian vectơ được định nghĩa trên trường $\mathbb{R}$ của thực các số trừ khi specified ngược lại (trong một vài các trường hợp, trên phức các số $\mathbb{C})$. Thứ nhất ta định nghĩa Euclidean cấu trúc trên không gian vectơ (vector space). Technically, Euclidean cấu trúc trên không gian vectơ (vector space) $E$ là miễn là/được cung cấp bởi dạng song tuyến tính đối xứng trên không gian vectơ (vector space) thỏa mãn một số extra các tính chất. Nhắc lại rằng dạng song tuyến tính (bilinear form) $\phi$: $E \times  E \to \mathbb{R}$ là xác định nếu với mọi $u \in E, u \neq  0$ suy ra rằng $\phi (u, u) \neq  0$, và dương nếu với mọi $u \in E, \phi (u, u) \ge 0$.

> **Định nghĩa 12.1.** Không gian Euclid (Euclidean space) là thực không gian vectơ (vector space) $E$ được trang bị dạng song tuyến tính đối xứng $\phi$: $E \times E \to \mathbb{R}$ rằng là xác định dương (positive definite). Nhiều hơn/thêm một cách tường minh, $\phi$: $E \times E \to \mathbb{R}$ thỏa mãn sau đây axioms:
$$\phi (u_{1} + u_{2}, v)=\phi (u_{1}, v) + \phi (u_{2}, v),$$
$$\phi (u, v_{1} + v_{2})=\phi (u, v_{1}) + \phi (u, v_{2}),$$
$$\phi (\lambda u, v)=\lambda \phi (u, v),$$
$$\phi (u, \lambda v)=\lambda \phi (u, v),$$
$$\phi (u, v)=\phi (v, u),$$
$$u=0 implies that \phi (u, u) > 0.$$
Thực số $\phi (u, v)$ cũng được gọi là tích vô hướng (inner product) (hoặc vô hướng (scalar) tích) của $u$ và $v$. Ta cũng định nghĩa dạng toàn phương (quadratic form) liên kết với $\phi$ như hàm $\Phi$: $E \to \mathbb{R}_{+}$ sao cho
$$\Phi (u) = \phi (u, u),$$
Với mọi $u \in E$. Vì $\phi$ là song tuyến tính, ta có $\phi (0, 0) = 0$, và vì nó là xác định dương (positive definite), ta có mạnh hơn sự kiện rằng
$$\phi (u, u) = 0iffu = 0,$$
Rằng là, $\Phi (u) = 0$ khi và chỉ khi $u = 0$. Cho trước tích vô hướng (inner product) $\phi$: $E \times  E \to \mathbb{R}$ trên không gian vectơ (vector space) $E$, ta cũng ký hiệu $\phi (u, v)$ bởi
$$u \cdot  vor\langle u, v\rangle or(u|v),$$
Và $p\overline{\Phi (}\overline{u}\overline{)}$ bởi $\|u\|$.

> **Ví dụ 12.1.** tiêu chuẩn ví dụ của Không gian Euclid (Euclidean space) là $\mathbb{R}^{n}$, dưới tích vô hướng (inner product) $\cdot$ được định nghĩa sao cho
$$(x_{1}, \dots  , x_{n}) \cdot  (y_{1}, \dots  , y_{n}) = x_{1}y_{1} + x_{2}y_{2} + \cdots  + x_{n}y_{n}.$$
Điều này Không gian Euclid (Euclidean space) được ký hiệu bởi $\mathbb{E}^{n}$.

<!-- PAGE 455 -->
Có khác các ví dụ.

> **Ví dụ 12.2.** Chẳng hạn, cho $E$ là không gian vectơ (vector space) có số chiều $2$, và cho $(e_{1}, e_{2})$ là cơ sở (basis) của $E$. Nếu $> 0$ và $b^{2}$ - ac $< 0$, dạng song tuyến tính (bilinear form) được định nghĩa sao cho
$$\phi (x_{1}e_{1} + y_{1}e_{2}, x_{2}e_{1} + y_{2}e_{2}) = ax_{1}x_{2} + b(x_{1}y_{2} + x_{2}y_{1}) + cy_{1}y_{2}$$
Cho ta Euclidean cấu trúc trên $E$. Trong trường hợp này,
$$\Phi (xe_{1} + ye_{2}) = ax^{2}+ 2bxy + cy^{2}.$$

> **Ví dụ 12.3.** Cho $\mathcal{C}[a, b]$ ký hiệu tập hợp của liên tục các hàm $f$: [, $b] \to \mathbb{R}$. Nó là dễ dàng đã kiểm tra rằng $\mathcal{C}[a, b]$ là không gian vectơ (vector space) của vô hạn số chiều. Cho trước bất kỳ hai các hàm $f, g \in$ C[, $b]$, cho
$$\langle f, g\rangle = \int_{a}^{}  bf(t)g(t)dt.$$
Ta để lại nó như dễ bài tập rằng $\langle$ -, $-\rangle$ là thật vậy tích vô hướng (inner product) trên $\mathcal{C}[a, b]$. Trong trường hợp ở đâu $a = -\pi$ và $b = \pi$ (hoặc $a = 0$ và $b = 2\pi$, điều này làm cho basically không có difference), một nên tính
$$\langle \sin px, \sin qx\rangle ,\langle \sin px, \cos qx\rangle ,and\langle \cos px, \cos qx\rangle ,$$
Với mọi tự nhiên các số $p, q \ge 1$. outcome của các phần tử này các phép tính là những gì làm cho Fourier giải tích/phân tích khả dĩ/có thể!

> **Ví dụ 12.4.** Cho $E = M_{n}(\mathbb{R})$ là không gian vectơ (vector space) của thực $n \times  n$ các ma trận. Nếu ta quan điểm ma trận $A \in M_{n}(\mathbb{R})$ như “dài” vectơ cột (column vector) thu được bởi concatenating cùng nhau các cột của nó, ta có thể định nghĩa tích vô hướng (inner product) của hai các ma trận $A, B \in M_{n}(\mathbb{R})$ như
$$\langle A, B\rangle = \sum_{i,j=1}^{n}  a_{ij}b_{ij},$$
Mà có thể được một cách thuận tiện được viết như
$$\langle A, B\rangle = \mathrm{tr}(A^{\top}B) = \mathrm{tr}(B^{\top}A).$$
Vì điều này có thể được được quan điểm như Euclidean tích trên $\mathbb{R}^{n2}$, nó là tích vô hướng (inner product) trên $M_{n}(\mathbb{R})$. tương ứng chuẩn (norm)
$$\|A\|_{F} =p\overline{\mathrm{tr}(}\overline{A}^{\top}\overline{A}\overline{)}$$
Là Chuẩn Frobenius (Frobenius norm) (xem Mục 9.2). Cho chúng ta nhận thấy rằng $\phi$ có thể được recovered từ $\Phi$.

<!-- PAGE 456 -->

> **Mệnh đề 12.1.** Ta có
$$\phi (u, v) = \frac{1}{2} [\Phi (u + v) -\Phi (u) -\Phi (v)]$$
Với mọi $u, v \in E$. Ta nói rằng $\phi$ là dạng cực (polar form) của $\Phi$.

*Chứng minh.* Bởi tính song tuyến tính và tính đối xứng, ta có
$$\Phi (u + v) = \phi (u + v, u + v)$$
$$= \phi (u, u + v) + \phi (v, u + v)$$
$$= \phi (u, u) + 2\phi (u, v) + \phi (v, v)$$
$$= \Phi (u) + 2\phi (u, v) + \Phi (v).$$
Nếu $E$ là hữu hạn chiều và nếu $\phi$: $E \times  E \to \mathbb{R}$ là dạng song tuyến tính (bilinear form) trên $E$, cho trước bất kỳ cơ sở (basis)
$$(e_{1}, \dots  , e_{n}) of E, we can write x = \sum_{ni}  n=1 x_{i}e_{i} and y = \sum_{n}  nj=1 y_{j}e_{j}, and we have$$
$$\phi (x, y) = \phi \begin{pmatrix} x_{i}e_{i}, & y_{j}e_{j} \end{pmatrix} \sum_{i=1}^{}  \sum_{j=1}^{n}  = \sum_{i,j=1}  x_{i}y_{j}\phi (e_{i}, e_{j}).$$
Nếu ta cho $G$ là ma trận $G = (\phi (e_{i}, e_{j}))$, và nếu $x$ và $y$ là các vectơ cột liên kết với $(x_{1}, \dots  , x_{n})$ và $(y_{1}, \dots  , y_{n})$, thì ta có thể viết
$$\phi (x, y) = x^{\top}Gy = y^{\top}G^{\top}x.$$
$$Note that we are committing an abuse of notation since x = \sum_{i}  n=1 x_{i}e_{i} is a vector in E, but$$
Vectơ cột (column vector) liên kết với $(x_{1}, \dots  , x_{n})$ thuộc $to\mathbb{R}^{n}$. để tránh điều này định thức con (minor) abuse, ta có thể ký hiệu vectơ cột (column vector) liên kết với $(x_{1}, \dots  , x_{n})$ bởi $x$ (và tương tự $y$ cho vectơ cột (column vector) liên kết với $(y_{1}, \dots  , y_{n}))$, trong wich trường hợp “đúng” biểu thức cho $\phi (x, y)$ là
$$\phi (x, y) = x^{\top}Gy.$$
Tuy nhiên, xét theo đẳng cấu giữa $E$ và $\mathbb{R}^{n}$, đến giữ ký hiệu như đơn giản như khả dĩ/có thể, ta sẽ sử dụng $x$ và $y$ thay vì của $x$ và $y$. Cũng nhận thấy rằng $\phi$ là đối xứng khi và chỉ khi $G = G^{\top}$, và $\phi$ là xác định dương (positive definite) khi và chỉ khi ma trận $G$ là xác định dương (positive definite), nghĩa là,
$$x^{\top}Gx > 0for all x \in \mathbb{R}^{n}, x \neq  0.$$
Ma trận $G$ liên kết với tích vô hướng (inner product) được gọi là Gram ma trận của tích vô hướng (inner product) đối với cơ sở (basis) $(e_{1}, \dots  , e_{n})$. Ngược lại, nếu $A$ là đối xứng xác định dương (SPD) $n\times n$ ma trận, nó là dễ để kiểm tra rằng dạng song tuyến tính (bilinear form)
$$\langle x, y\rangle = x^{\top}Ay$$

<!-- PAGE 457 -->
Là tích vô hướng (inner product). Nếu ta tạo chuyển cơ sở (change of basis) từ cơ sở (basis) $(e_{1}, \dots  , e_{n})$ đến cơ sở (basis) $(f_{1}, \dots  , f_{n})$, và nếu ma trận chuyển cơ sở (change of basis matrix) là $P$ (ở đâu cột thứ $j$ của $P$ bao gồm của các tọa độ của $f_{j}$ trên cơ sở (basis) $(e_{1}, \dots  , e_{n}))$, thì đối với các tọa độ x' và y' trên cơ sở (basis) $(f_{1}, \dots  , f_{n})$, ta có
$$x^{\top}Gy = x^{'\top}P^{\top} GPy',$$
Do đó ma trận của của ta tích vô hướng (inner product) trên cơ sở (basis) $(f_{1}, \dots  , f_{n})$ là $P^{\top}$ GP. Ta summarize các phần tử này các sự kiện trong sau đây mệnh đề.

> **Mệnh đề 12.2.** Cho $E$ là không gian vectơ hữu hạn chiều, và cho $(e_{1}, \dots  , e_{n})$ là cơ sở (basis) của $E. 1$. Với mọi tích vô hướng (inner product) $\langle$ -, $-\rangle$ trên $E$, nếu $G = (\langle e_{i}, e_{j}\rangle$) là Gram ma trận của tích vô hướng (inner product) $\langle$ -, $-\rangle$ w.r.t. cơ sở (basis) $(e_{1}, \dots  , e_{n})$, thì $G$ là đối xứng xác định dương (SPD). $2$. Với mọi ma trận chuyển cơ sở (change of basis matrix) $P$, Gram ma trận của $\langle$ -, $-\rangle$ đối với mới cơ sở (basis) là $P^{\top}$ GP. $3$. Nếu $A$ là bất kỳ $n \times  n$ đối xứng xác định dương (SPD) ma trận, thì
$$\langle x, y\rangle = x^{\top}Ay$$
Là tích vô hướng (inner product) trên $E$. Ta sẽ xem sau này rằng ma trận đối xứng (symmetric matrix) là xác định dương (positive definite) khi và chỉ khi các trị riêng (các trị riêng (eigenvalues)) của nó là tất cả dương. Một của rất quan trọng các tính chất của tích vô hướng (inner product) $\phi$ là rằng ánh xạ $u \mapsto p\overline{\Phi (}\overline{u}\overline{)}$ là chuẩn (norm).

> **Mệnh đề 12.3.** Cho $E$ là Không gian Euclid (Euclidean space) với tích vô hướng (inner product) $\phi$, và cho $\Phi$ là tương ứng dạng toàn phương (quadratic form). Với mọi $u, v \in E$, ta có Cauchy–Schwarz bất đẳng thức
$$\phi (u, v)^{2}\le \Phi (u)\Phi (v),$$
Đẳng thức giữ khi và chỉ khi $u$ và $v$ là phụ thuộc tuyến tính (linearly dependent). Ta cũng có Minkowski bất đẳng thức
$$p\overline{\Phi (}\overline{u}\overline{+}\overline{v}\overline{)} \le p\overline{\Phi (}\overline{u}\overline{) +} p\overline{\Phi (}\overline{v}\overline{)},$$
Đẳng thức giữ khi và chỉ khi $u$ và $v$ là phụ thuộc tuyến tính (linearly dependent), ở đâu ngoài ra nếu $u \neq  0$ và $v \neq  0$, thì $u = \lambda v$ với một số $\lambda  > 0$.

<!-- PAGE 458 -->

*Chứng minh.* Với mọi các vectơ $u, v \in E$, ta định nghĩa hàm $T$: $\mathbb{R} \to \mathbb{R}$ sao cho
$$T(\lambda ) = \Phi (u + \lambda v),$$
Với mọi $\lambda  \in \mathbb{R}$. Bằng cách sử dụng tính song tuyến tính và tính đối xứng, ta có
$$\Phi (u + \lambda v)=\phi (u + \lambda v, u + \lambda v)$$
$$=\phi (u, u + \lambda v) + \lambda \phi (v, u + \lambda v)$$
$$=\phi (u, u) + 2\lambda \phi (u, v) + \lambda^{2} \phi (v, v)$$
$$=\Phi (u) + 2\lambda \phi (u, v) + \lambda^{2} \Phi (v).$$
Vì $\phi$ là xác định dương (positive definite), $\Phi$ là không âm, và do đó $T(\lambda$) $\ge 0$ với mọi $\lambda  \in \mathbb{R}$. Nếu $\Phi (v) = 0$, thì $v = 0$, và ta cũng có $\phi (u, v) = 0$. Trong trường hợp này, Cauchy–Schwarz bất đẳng thức là tầm thường, và $v = 0$ và $u$ là phụ thuộc tuyến tính (linearly dependent). Bây giờ giả sử $\Phi (v) > 0$. Vì $T(\lambda$) $\ge 0$, toàn phương phương trình
$$\lambda^{2} \Phi (v) + 2\lambda \phi (u, v) + \Phi (u) = 0$$
Không thể có phân biệt thực các nghiệm, mà có nghĩa là của nó discriminant
$$\Delta = 4(\phi (u, v)^{2}-\Phi (u)\Phi (v))$$
Là null hoặc âm, mà là một cách chính xác Cauchy–Schwarz bất đẳng thức
$$\phi (u, v)^{2}\le \Phi (u)\Phi (v).$$
Cho chúng ta bây giờ xét trường hợp ở đâu ta có đẳng thức
$$\phi (u, v)^{2}= \Phi (u)\Phi (v).$$
Có hai các trường hợp. Nếu $\Phi (v) = 0$, thì $v = 0$ và $u$ và $v$ là phụ thuộc tuyến tính (linearly dependent). Nếu $\Phi (v) \neq  0$, thì ở trên toàn phương phương trình có gấp đôi nghiệm (root) $\lambda_{0}$, và ta có $\Phi (u + \lambda_{0} v) = 0$. Vì $\phi$ là xác định dương (positive definite), $\Phi (u + \lambda_{0} v) = 0$ suy ra rằng $u + \lambda_{0} v = 0$, mà chỉ ra rằng $u$ và $v$ là phụ thuộc tuyến tính (linearly dependent). Ngược lại, nó là dễ để kiểm tra rằng ta có đẳng thức khi $u$ và $v$ là phụ thuộc tuyến tính (linearly dependent). Minkowski bất đẳng thức
$$p\overline{\Phi (}\overline{u}\overline{+}\overline{v}\overline{)} \le p\overline{\Phi (}\overline{u}\overline{) +} p\overline{\Phi (}\overline{v}\overline{)}$$
Là tương đương đến
$$\Phi (u + v) \le \Phi (u) + \Phi (v) + 2p\overline{\Phi (}\overline{u}\overline{)\Phi (}\overline{v}\overline{)}.$$
Tuy nhiên, ta có được hiển thị rằng
$$2\phi (u, v) = \Phi (u + v) -\Phi (u) -\Phi (v),$$

<!-- PAGE 459 -->
Và do đó ở trên bất đẳng thức là tương đương đến
$$\phi (u, v) \le p\overline{\Phi (}\overline{u}\overline{)\Phi (}\overline{v}\overline{)},$$
Mà là tầm thường khi $\phi (u, v) \le 0$, và suy ra từ Cauchy–Schwarz bất đẳng thức khi $\phi (u, v) \ge 0$. Do đó, Minkowski bất đẳng thức nghiệm đúng. Cuối cùng giả sử rằng $u \neq  0$ và $v \neq  0$, và rằng
$$p\overline{\Phi (}\overline{u}\overline{+}\overline{v}\overline{) =} p\overline{\Phi (}\overline{u}\overline{) +} p\overline{\Phi (}\overline{v}\overline{)}.$$
Khi điều này là trường hợp, ta có
$$\phi (u, v) =p\overline{\Phi (}\overline{u}\overline{)\Phi (}\overline{v}\overline{)},$$
Và ta biết từ thảo luận của Cauchy–Schwarz bất đẳng thức rằng đẳng thức nghiệm đúng khi và chỉ khi $u$ và $v$ là phụ thuộc tuyến tính (linearly dependent). Minkowski bất đẳng thức là đẳng thức khi $u$ hoặc $v$ là null. Ngược lại, nếu $u \neq  0$ và $v \neq  0$, thì $u = \lambda v$ với một số $\lambda  \neq  0$, và vì
$$\phi (u, v) = \lambda \phi (v, v) =p\overline{\Phi (}\overline{u}\overline{)\Phi (}\overline{v}\overline{)},$$
Bởi positivity, ta phải có $\lambda  > 0$. Lưu ý rằng Cauchy–Schwarz bất đẳng thức có thể cũng được viết như
$$|\phi (u, v)| \le p\overline{\Phi (}\overline{u}\overline{)} p\overline{\Phi (}\overline{v}\overline{)}.$$
Nhận xét: Nó là dễ để chứng minh rằng Cauchy–Schwarz và Minkowski các bất đẳng thức vẫn đúng cho dạng song tuyến tính đối xứng rằng là dương, nhưng không nhất thiết xác định (i.e., $\phi (u, v) \ge 0$ với mọi $u, v \in E)$. Tuy nhiên, $u$ và $v$ cần không là phụ thuộc tuyến tính (linearly dependent) khi đẳng thức nghiệm đúng. Minkowski bất đẳng thức
$$p\overline{\Phi (}\overline{u}\overline{+}\overline{v}\overline{)} \le p\overline{\Phi (}\overline{u}\overline{) +} p\overline{\Phi (}\overline{v}\overline{)}$$
Chỉ ra rằng ánh xạ $u \mapsto p\overline{\Phi (}\overline{u}\overline{)}$ thỏa mãn tính lồi bất đẳng thức (cũng đã biết như tam giác bất đẳng thức), điều kiện (N3) của Định nghĩa 9.1, và vì $\phi$ là song tuyến tính và xác định dương (positive definite), nó cũng thỏa mãn các điều kiện (N1) và (N2) của Định nghĩa 9.1, và do đó nó là chuẩn (norm) trên $E$. chuẩn (norm) được cảm sinh bởi $\phi$ được gọi là Euclidean chuẩn (norm) được cảm sinh bởi $\phi$. Cauchy–Schwarz bất đẳng thức có thể được viết dưới dạng
$$|u \cdot  v| \le \|u\|\|v\|,$$
Và Minkowski bất đẳng thức như
$$\|u + v\|\le \|u\|+ \|v\|.$$

<!-- PAGE 460 -->
Nếu $u$ và $v$ là khác không các vectơ thì Cauchy–Schwarz bất đẳng thức suy ra rằng
$$\cdot$$
$$-1 \le \frac{u v}{\|u\|\|v\|} \le +1.$$
Thì tồn tại duy nhất một $\theta  \in [0, \pi$ ] sao cho
$$\cdot$$
$$\cos \theta  = \frac{u v}{\|u\|\|v\|} .$$
Ta có $u = v$ khi và chỉ khi $\theta  = 0$ và $u = -v$ khi và chỉ khi $\theta  = \pi$. Cho $0 < \theta  < \pi$, các vectơ $u$ và $v$ là độc lập tuyến tính (linearly independent) và có một định hướng của mặt phẳng được sinh (spanned) bởi $u$ và $v$ sao cho $\theta$ là góc giữa $u$ và $v$. Xem Bài toán 12.8 cho precise khái niệm của định hướng. Nếu $u$ là unit vectơ (mà có nghĩa là $\|u\| = 1)$, thì vectơ
$$(\|v\|\cos \theta )u = (u \cdot  v)u = (v \cdot  u)u$$
Được gọi là phép chiếu trực giao (orthogonal projection) của $v$ lên không gian được sinh (spanned) bởi $u$.
Nhận xét: Một có thể tự hỏi nếu mọi chuẩn (norm) trên không gian vectơ (vector space) được cảm sinh bởi một số Euclidean tích vô hướng (inner product). Nói chung điều này là sai, nhưng đáng chú ý, có một đơn giản cần và đủ điều kiện, mà là rằng chuẩn (norm) phải thỏa mãn hình bình hành luật:
$$\|u + v\|^{2}+ \|u -v\|^{2}= 2(\|u\|^{2}+ \|v\|^{2}).$$
Xem Hình 12.1.
$$vv$$
$$-+$$
$$u$$
$$u$$
$$u$$
$$\overline{v}$$

![Figure 12.1](../../assets/ch12/fig_12_1.png)

**Hình 12.1:** hình bình hành luật phát biểu rằng tổng của các độ dài của các đường chéo của hình bình hành được xác định bởi các vectơ $u$ và $v$ các bằng nhau tổng của tất cả các vế/cạnh. Nếu $\langle$ -, $-\rangle$ là tích vô hướng (inner product), thì ta có
$$\|u + v\|^{2}= \|u\|^{2}+ \|v\|^{2}+ 2\langle u, v\rangle$$
$$\|u -v\|^{2}= \|u\|^{2}+ \|v\|^{2}-2\langle u, v\rangle ,$$

<!-- PAGE 461 -->
Và bằng cách cộng và trừ các phần tử này các đồng nhất thức, ta thu được hình bình hành luật và phương trình
$$-\|$$
$$\langle u, v\rangle = \frac{1}{4} (\|u + v\|^{2}u -v\|^{2}),$$
Mà cho phép chúng ta đến recover $\langle$ -, $-\rangle$ từ chuẩn (norm). Ngược lại, nếu $\|\|$ là chuẩn (norm) thỏa mãn hình bình hành luật, và nếu nó đến từ tích vô hướng (inner product), thì điều này tích vô hướng (inner product) phải là cho trước bởi
$$-\|$$
$$\langle u, v\rangle = \frac{1}{4} (\|u + v\|^{2}u -v\|^{2}).$$
Ta cần để chứng minh rằng ở trên tạo thành là thật vậy đối xứng và song tuyến tính. Tính đối xứng nghiệm đúng bởi vì $\|u$ - $v\| = \|-(u$ - $v)\| = \|v$ - $u\|$. Cho chúng ta chứng minh additivity trong biến $u$. Bởi hình bình hành luật, ta có
$$2(\|x + z\|^{2}+ \|y\|^{2}) = \|x + y + z\|^{2}+ \|x -y + z\|^{2}$$
Mà cho ta
$$\|x + y + z\|^{2}= 2(\|x + z\|^{2}+ \|y\|^{2}) -\|x -y + z\|^{2}$$
$$\|x + y + z\|^{2}= 2(\|y + z\|^{2}+ \|x\|^{2}) -\|y -x + z\|^{2},$$
Ở đâu thứ hai công thức là thu được bởi swapping $x$ và $y$. Thì bằng cách cộng lên các phương trình này, ta thu được
$$- .$$
$$\|x + y + z\|^{2}= \|x\|^{2}+ \|y\|^{2}+ \|x + z\|^{2}+ \|y + z\|^{2}- \frac{1}{2} \|x -y + z\|^{2} \frac{1}{2} \|y -x + z\|^{2}$$
Thay thế $z$ bởi $-z$ trong ở trên phương trình, ta thu được
$$- ,$$
$$\|x + y -z\|^{2}= \|x\|^{2}+ \|y\|^{2}+ \|x -z\|^{2}+ \|y -z\|^{2}- \frac{1}{2} \|x -y -z\|^{2} \frac{1}{2} \|y -x -z\|^{2}$$
Vì $\|x$ - $y + z\| = \|-(x$ - $y + z)\| = \|y$ - $x$ - $z\|$ và $\|y$ - $x + z\| = \|-(y$ - $x + z)\| = \|x$ - $y$ - $z\|$, bằng cách trừ cuối cùng hai các phương trình, ta thu được
$$-\|$$
$$\langle x + y, z\rangle = \frac{1}{4} (\|x + y + z\|^{2}x + y -z\|^{2})$$
$$-\|  -\|$$
$$= \frac{1}{4} (\|x + z\|^{2}x -z\|^{2}) + \frac{1}{4} (\|y + z\|^{2}y -z\|^{2})$$
$$= \langle x, z\rangle + \langle y, z\rangle ,$$
Như mong muốn. Chứng minh rằng
$$\langle \lambda x, y\rangle = \lambda \langle x, y\rangle for all \lambda  \in \mathbb{R}$$
