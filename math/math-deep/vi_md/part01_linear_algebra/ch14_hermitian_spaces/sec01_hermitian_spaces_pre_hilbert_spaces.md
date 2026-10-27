# Các không gian Hermite, Pre-Các không gian Hilbert


<!-- PAGE 529 -->
Chương $14$ Các không gian Hermite

## 14.1 Nửa tuyến tính (sesquilinear) và Hermite Các dạng, Pre-Hilbert

$$Spaces and Hermitian Spaces$$
Trong chương này ta tổng quát hóa cơ bản các kết quả của Euclidean hình học được trình bày trong Chương $12$ đến các không gian vectơ trên phức các số. Như vậy tổng quát hóa là inevitable và không đơn giản luxury. Ví dụ, các ánh xạ tuyến tính (linear maps) có thể không có thực các trị riêng (eigenvalues), nhưng chúng luôn luôn có phức các trị riêng (eigenvalues). Hơn nữa, một số rất quan trọng các lớp của các ánh xạ tuyến tính (linear maps) có thể được được chéo hóa nếu chúng được mở rộng đến phức hóa của thực không gian vectơ (vector space). Điều này là trường hợp cho các ma trận trực giao và, tổng quát hơn, các ma trận chuẩn tắc. Cũng, phức các không gian vectơ là thường tự nhiên khung lý thuyết trong vật lý hoặc kỹ thuật, và chúng là nhiều hơn/thêm thuận tiện cho dealing với Fourier chuỗi. Tuy nhiên, một số complications phát sinh do phức liên hợp. Nhắc lại rằng với mọi phức số $z \in \mathbb{C}$, nếu $z = x +$ iy ở đâu $x, y \in \mathbb{R}$, ta cho $\mathcal{ℜ} z = x$, thực phần của $z$, và $\mathcal{ℑ} z = y$, imaginary phần của $z$. Ta cũng ký hiệu liên hợp của $z = x +$ iy bởi $\overline{z} = x$ - iy, và tuyệt đối giá trị (hoặc độ dài, hoặc môđun/độ lớn) của $z$ bởi |z|. Nhắc lại rằng $|z|^{2} =\overline{zz} = x^{2} + y^{2}$. Có nhiều tự nhiên các tình huống ở đâu ánh xạ $\phi$: $E \times  E \to \mathbb{C}$ là tuyến tính trong của nó thứ nhất lập luận và chỉ nửa tuyến tính (semilinear) trong của nó thứ hai lập luận, mà có nghĩa là $\phi (u, \mu v) =\overline{\mu \phi}(u, v)$, như opposed đến $\phi (u, \mu v) = \mu \phi (u, v)$. Ví dụ, tự nhiên tích vô hướng (inner product) đến deal với các hàm $f$: $\mathbb{R} \to \mathbb{C}$, especially Fourier chuỗi, là
$$\langle f, g\rangle = \int_{-}^{}  \pi f(x)\overline{g}\overline{(}\overline{x}\overline{)} dx,$$
$$\pi$$
Mà là nửa tuyến tính (semilinear) (nhưng không tuyến tính) trong $g$. Do đó, khi generalizing kết quả từ thực trường hợp của Không gian Euclid (Euclidean space) đến phức trường hợp, ta luôn luôn có để kiểm tra rất carefully rằng của ta các chứng minh thực hiện không rely trên tính tuyến tính trong thứ hai lập luận. Ngược lại, ta cần đến revise của ta các chứng minh, và đôi khi kết quả là đơn giản sai!
$$529$$

<!-- PAGE 530 -->
Trước định nghĩa tự nhiên tổng quát hóa của tích vô hướng (inner product), nó là thuận tiện để định nghĩa nửa tuyến tính (semilinear) các ánh xạ.

> **Định nghĩa 14.1.** Cho trước hai các không gian vectơ $E$ và $F$ trên phức trường $\mathbb{C}$, hàm $f$: $E \to F$ là nửa tuyến tính (semilinear) nếu
$$f(u + v) = f(u) + f(v),$$
$$f(\lambda u) =\overline{\lambda f}(u),$$
Với mọi $u, v \in E$ và tất cả $\lambda  \in \mathbb{C}$.
Nhận xét: Thay vì của định nghĩa nửa tuyến tính (semilinear) các ánh xạ, ta có thể có được định nghĩa không gian vectơ (vector space) $\overline{E}$ như không gian vectơ (vector space) với cùng carrier tập hợp $E$ có phép cộng là cùng như rằng của $E$, nhưng có phép nhân bởi phức số được cho bởi
$$(\lambda , u) \mapsto \overline{\lambda u.}$$
Thì nó là dễ để kiểm tra rằng hàm $f$: $E \to \mathbb{C}$ là nửa tuyến tính (semilinear) khi và chỉ khi $f$: $\overline{E} \to \mathbb{C}$ là tuyến tính. Ta có thể bây giờ định nghĩa các dạng nửa tuyến tính và Hermite các dạng.

> **Định nghĩa 14.2.** Cho trước phức không gian vectơ (vector space) $E$, hàm $\phi$: $E\times E \to \mathbb{C}$ là dạng nửa tuyến tính (sesquilinear form) nếu nó là tuyến tính trong của nó thứ nhất lập luận và nửa tuyến tính (semilinear) trong của nó thứ hai lập luận, mà có nghĩa là
$$\phi (u_{1} + u_{2}, v) = \phi (u_{1}, v) + \phi (u_{2}, v),$$
$$\phi (u, v_{1} + v_{2}) = \phi (u, v_{1}) + \phi (u, v_{2}),$$
$$\phi (\lambda u, v) = \lambda \phi (u, v),$$
$$\phi (u, \mu v) =\overline{\mu \phi}(u, v),$$
Với mọi $u, v, u_{1}, u_{2}, v_{1}, v_{2} \in E$, và tất cả $\lambda , \mu  \in \mathbb{C}$. hàm $\phi$: $E \times  E \to \mathbb{C}$ là Hermite tạo thành nếu nó là nửa tuyến tính (sesquilinear) và nếu
$$\phi (v, u) =\overline{\phi}\overline{(}\overline{u, v}\overline{)}$$
Với mọi tất cả $u, v \in E$. Hiển nhiên, $\phi (0, v) = \phi (u, 0) = 0$. Cũng lưu ý rằng nếu $\phi$: $E \times  E \to \mathbb{C}$ là nửa tuyến tính (sesquilinear), ta có
$$\phi (\lambda u + \mu v, \lambda u + \mu v) = |\lambda |^{2}\phi (u, u) +\overline{\lambda \mu \phi}(u, v) +\overline{\lambda \mu \phi}(v, u) + |\mu |^{2}\phi (v, v),$$
Và nếu $\phi$: $E \times  E \to \mathbb{C}$ là Hermite, ta có
$$\phi (\lambda u + \mu v, \lambda u + \mu v) = |\lambda |^{2}\phi (u, u) + 2\mathcal{ℜ}(\overline{\lambda \mu \phi}(u, v)) + |\mu |^{2}\phi (v, v).$$
Lưu ý rằng bị thu hẹp đến thực các hệ số, dạng nửa tuyến tính (sesquilinear form) là song tuyến tính (ta đôi khi nói $\mathbb{R}-bilinear)$.

<!-- PAGE 531 -->

> **Định nghĩa 14.3.** Cho trước dạng nửa tuyến tính (sesquilinear form) $\phi$: $E \times  E \to \mathbb{C}$, hàm $\Phi$: $E \to \mathbb{C}$ được định nghĩa sao cho $\Phi (u) = \phi (u, u)$ với mọi $u \in E$ được gọi là dạng toàn phương (quadratic form) liên kết với $\phi$.
$$\mathbb{C}^{n}$$
Tiêu chuẩn ví dụ của Hermite tạo thành trên là ánh xạ $\phi$ được định nghĩa sao cho
$$\phi ((x_{1}, \dots  , x_{n}), (y_{1}, \dots  , y_{n})) = x_{1}\overline{y}_{1} + x_{2}\overline{y}_{2} + \cdots  + x_{n}\overline{y}_{n}.$$
Ánh xạ này là cũng xác định dương (positive definite), nhưng trước dealing với các phần tử này các vấn đề, ta chỉ ra sau đây hữu ích mệnh đề.

> **Mệnh đề 14.1.** Cho trước phức không gian vectơ (vector space) $E$, các tính chất sau đây đúng:
$(1) A$ dạng nửa tuyến tính (sesquilinear form) $\phi$: $E \times E \to \mathbb{C}$ là Hermite tạo thành khi và chỉ khi $\phi (u, u) \in \mathbb{R}$ với mọi $u \in E$.
$(2)$ Nếu $\phi$: $E \times  E \to \mathbb{C}$ là dạng nửa tuyến tính (sesquilinear form), thì
$$4\phi (u, v) = \phi (u + v, u + v) -\phi (u -v, u -v)$$
$$+ i\phi (u + iv, u + iv) -i\phi (u -iv, u -iv),$$
Và
$$2\phi (u, v) = (1 + i)(\phi (u, u) + \phi (v, v)) -\phi (u -v, u -v) -i\phi (u -iv, u -iv).$$
Các phần tử này được gọi là phân cực các đồng nhất thức.

*Chứng minh.* $(1)$ Nếu $\phi$ là Hermite tạo thành, thì
$$\phi (v, u) =\overline{\phi}\overline{(}\overline{u, v}\overline{)}$$
Suy ra rằng
$$\phi (u, u) =\overline{\phi}\overline{(}\overline{u, u}\overline{)},$$
Và do đó $\phi (u, u) \in \mathbb{R}$. Nếu $\phi$ là nửa tuyến tính (sesquilinear) và $\phi (u, u) \in \mathbb{R}$ với mọi $u \in E$, thì
$$\phi (u + v, u + v) = \phi (u, u) + \phi (u, v) + \phi (v, u) + \phi (v, v),$$
Mà chứng tỏ rằng
$$\phi (u, v) + \phi (v, u) = \alpha ,$$
Ở đâu $\alpha$ là thực, và thay đổi $u$ đến iu, ta có
$$i(\phi (u, v) -\phi (v, u)) = \beta ,$$
Ở đâu $\beta$ là thực, và do đó
$$\phi (u, v) = \frac{\alpha i\beta}{2} -and\phi (v, u) = \frac{\alpha  + i\beta}{2} ,$$
Chứng minh rằng $\phi$ là Hermite.
$(2)$ Các phần tử này các đồng nhất thức được kiểm chứng bởi expanding vế phải, và ta để lại chúng như một bài tập.

<!-- PAGE 532 -->
Mệnh đề 14.1 chỉ ra rằng dạng nửa tuyến tính (sesquilinear form) là hoàn toàn được xác định bởi dạng toàn phương (quadratic form) $\Phi (u) = \phi (u, u)$, chẵn/ngay cả nếu $\phi$ là không Hermite. Điều này là sai cho thực dạng song tuyến tính (bilinear form), trừ khi
$$\mathbb{R}^{2} \mathbb{R}^{2} \mathbb{R}$$
Nó là đối xứng. Ví dụ, dạng song tuyến tính (bilinear form) $\phi$: $\times \to$ được định nghĩa sao cho
$$\phi ((x_{1}, y_{1}), (x_{2}, y_{2})) = x_{1}y_{2} -x_{2}y_{1}$$
Là không một cách đồng nhất không, và vẫn chưa nó là null trên đường chéo. Tuy nhiên, thực dạng song tuyến tính đối xứng là thật vậy được xác định bởi các giá trị của nó trên đường chéo, như ta đã thấy trong Chương $12$. Như trong Euclidean trường hợp, Hermite các dạng cho mà $\phi (u, u) \ge 0$ đóng quan trọng vai trò.

> **Định nghĩa 14.4.** Cho trước phức không gian vectơ (vector space) $E$, Hermite tạo thành $\phi$: $E \times  E \to \mathbb{C}$ là dương nếu $\phi (u, u) \ge 0$ với mọi $u \in E$, và xác định dương (positive definite) nếu $\phi (u, u) > 0$ với mọi $u \neq  0$. cặp $\langle E, \phi \rangle$ ở đâu $E$ là phức không gian vectơ (vector space) và $\phi$ là Hermite tạo thành trên $E$ được gọi là một pre-Không gian Hilbert (Hilbert space) nếu $\phi$ là dương, và Hermite (hoặc unita) không gian nếu $\phi$ là xác định dương (positive definite). Ta warn của ta độc giả rằng một số các tác giả, chẳng hạn như Lang $[115]$, định nghĩa pre-Không gian Hilbert (Hilbert space) như những gì ta định nghĩa như Không gian Hermite (Hermitian space). Ta ưu tiên sau đây thuật ngữ được sử dụng trong Schwartz $[156]$ và Bourbaki $[27]$. đại lượng $\phi (u, v)$ là thường được gọi là Hermite tích của $u$ và $v$. Ta sẽ occasionally gọi nó tích vô hướng (inner product) của $u$ và $v$. Cho trước pre-Không gian Hilbert (Hilbert space) $\langle E, \phi \rangle$, như trong trường hợp của Không gian Euclid (Euclidean space), ta cũng ký hiệu $\phi (u, v)$ bởi
$$u \cdot  vor\langle u, v\rangle or(u|v),$$
Và $p\overline{\Phi (}\overline{u}\overline{)}$ bởi $\|u\|$.
$$\mathbb{C}^{n}$$

> **Ví dụ 14.1.** phức không gian vectơ (vector space) dưới Hermite tạo thành
$$\phi ((x_{1}, \dots  , x_{n}), (y_{1}, \dots  , y_{n})) = x_{1}\overline{y}_{1} + x_{2}\overline{y}_{2} + \cdots  + x_{n}\overline{y}_{n}$$
Là Không gian Hermite (Hermitian space).

> **Ví dụ 14.2.** Cho $\ell^{2}$ ký hiệu tập hợp tất cả countably vô hạn các dãy $x = (x_{i})_{i\in N}$ của
$$\infty  n$$
$$complex numbers such that \sum_{i}  |x_{i}|^{2}is defined  (i.e.,  \mathbb{C} the sequence \sum_{i}  =0 |x_{i}|^{2}converges as$$
$n \to \infty$). Nó có thể được được hiển thị $that^{=0}$ ánh xạ $\phi$: $\ell^{2} \times  \ell^{2} \to$ được định nghĩa sao cho
$$\phi  ((x_{i})_{i\in N}, (y_{i})_{i\in N}) = \sum_{i=0}^{\infty}  x_{i}\overline{y}_{i}$$
Được xác định tốt (well-defined), và $\ell^{2}$ là Không gian Hermite (Hermitian space) dưới $\phi$. Thực sự, $\ell^{2}$ là chẵn/ngay cả Không gian Hilbert (Hilbert space).

> **Ví dụ 14.3.** Cho $\mathcal{C}_{piece}[a, b]$ là tập hợp của bị chặn từng khúc liên tục các hàm $f$: [, $b] \to \mathbb{C}$ dưới Hermite tạo thành
$$\langle f, g\rangle = \int_{a}^{}  bf(x)\overline{g}\overline{(}\overline{x}\overline{)} dx.$$
Nó là dễ để kiểm tra rằng điều này Hermite tạo thành là dương, nhưng nó là không xác định. Do đó, dưới điều này Hermite tạo thành, $\mathcal{C}_{piece}[a, b]$ là chỉ pre-Không gian Hilbert (Hilbert space).

<!-- PAGE 533 -->

> **Ví dụ 14.4.** Cho $\mathcal{C}[a, b]$ là tập hợp của nhận giá trị phức liên tục các hàm $f$: [, $b] \to \mathbb{C}$ dưới Hermite tạo thành
$$\langle f, g\rangle = \int_{a}^{}  bf(x)\overline{g}\overline{(}\overline{x}\overline{)} dx.$$
Nó là dễ để kiểm tra rằng điều này Hermite tạo thành là xác định dương (positive definite). Do đó, $\mathcal{C}[a, b]$ là Không gian Hermite (Hermitian space).

> **Ví dụ 14.5.** Cho $E = M_{n}(\mathbb{C})$ là không gian vectơ (vector space) của phức $n \times  n$ các ma trận. Nếu ta quan điểm ma trận $A \in M_{n}(\mathbb{C})$ như “dài” vectơ cột (column vector) thu được bởi concatenating cùng nhau các cột của nó, ta có thể định nghĩa Hermite tích của hai các ma trận $A, B \in M_{n}(\mathbb{C})$ như
$$\langle A, B\rangle = \sum_{i,j=1}^{n}  a_{ij}\overline{b}_{ij},$$
Mà có thể được một cách thuận tiện được viết như
$$\langle A, B\rangle = \mathrm{tr}(A^{\top}\overline{B}) = \mathrm{tr}(B^{*}A).$$
Vì điều này có thể được được quan điểm như tiêu chuẩn Hermite tích $on\mathbb{C}^{n2}$, nó là Hermite tích trên $M_{n}(\mathbb{C})$. tương ứng chuẩn (norm)
$$\|A\|_{F} =p\overline{\mathrm{tr}(}\overline{A}^{*}\overline{A}\overline{)}$$
Là Chuẩn Frobenius (Frobenius norm) (xem Mục 9.2). Nếu $E$ là hữu hạn chiều và nếu $\phi$: $E \times  E \to \mathbb{R}$ là sequilinear tạo thành trên $E$, cho trước bất kỳ
$$basis (e_{1}, \dots  , e_{n}) of E, we can write x = \sum_{ni}  n=1 x_{i}e_{i} and y = \sum  nj=1 y_{j}e_{j}, and we have$$
$$\phi (x, y) = \phi \begin{pmatrix} x_{i}e_{i}, & y_{j}e_{j} \end{pmatrix} \sum_{i=1}^{n}  \sum_{j=1}  = \sum_{i,j=1}^{n}  x_{i}\overline{y}_{j}\phi (e_{i}, e_{j}).$$
Nếu ta cho $G = (g_{ij})$ là ma trận cho trước bởi $g_{ij} = \phi (e_{j}, e_{i})$, và nếu $x$ và $y$ là các vectơ cột liên kết với $(x_{1}, \dots  , x_{n})$ và $(y_{1}, \dots  , y_{n})$, thì ta có thể viết
$$\phi (x, y) = x^{\top}G^{\top}\overline{y} = y^{*}Gx,$$
$where\overline{y}$ tương ứng với $(\overline{y}_{1}\overline{, \dots  , y}_{n})$. Như trong Mục 12.1, ta là committing slight abuse của
$$notation of letting x denote both the vector x = \sum_{i}  n=1 x_{i}e_{i} and the column vector associated$$
Với $(x_{1}, \dots  , x_{n})$ (và tương tự cho $y)$. “đúng” biểu thức cho $\phi (x, y)$ là
$$\phi (x, y) = y^{*}Gx = x^{\top}G^{\top}\overline{y}.$$
 Nhận thấy rằng trong $\phi (x, y) = y^{*}Gx$, ma trận liên quan là chuyển vị (transpose) của ma trận $(\phi (e_{i}, e_{j}))$. lý do cho điều này là rằng ta muốn $G$ là xác định dương (positive definite) khi $\phi$ là xác định dương (positive definite), không $G^{\top}$.

<!-- PAGE 534 -->
Hơn nữa, nhận thấy rằng $\phi$ là Hermite khi và chỉ khi $G = G^{*}$, và $\phi$ là xác định dương (positive definite) khi và chỉ khi ma trận $G$ là xác định dương (positive definite), nghĩa là,
$$(Gx)^{\top}\overline{x} = x^{*}Gx > 0for all x \in \mathbb{C}^{n}, x \neq  0.$$

> **Định nghĩa 14.5.** ma trận $G$ liên kết với Hermite tích được gọi là Gram ma trận của Hermite tích đối với cơ sở (basis) $(e_{1}, \dots  , e_{n})$. Ngược lại, nếu $A$ là Hermite xác định dương (positive definite) $n \times  n$ ma trận, nó là dễ để kiểm tra rằng Hermite tạo thành
$$\langle x, y\rangle = y^{*}Ax$$
Là xác định dương (positive definite). Nếu ta tạo chuyển cơ sở (change of basis) từ cơ sở (basis) $(e_{1}, \dots  , e_{n})$ đến cơ sở (basis) $(f_{1}, \dots  , f_{n})$, và nếu ma trận chuyển cơ sở (change of basis matrix) là $P$ (ở đâu cột thứ $j$ của $P$ bao gồm của các tọa độ của $f_{j}$ trên cơ sở (basis) $(e_{1}, \dots  , e_{n}))$, thì đối với các tọa độ x' và y' trên cơ sở (basis) $(f_{1}, \dots  , f_{n})$, ta có
$$y^{*}Gx = (y')^{*}P^{*} GPx',$$
Do đó ma trận của của ta tích vô hướng (inner product) trên cơ sở (basis) $(f_{1}, \dots  , f_{n})$ là $P^{*}$ GP. Ta summarize các phần tử này các sự kiện trong sau đây mệnh đề.

> **Mệnh đề 14.2.** Cho $E$ là không gian vectơ hữu hạn chiều, và cho $(e_{1}, \dots  , e_{n})$ là cơ sở (basis) của $E. 1$. Với mọi Hermite tích vô hướng (inner product) $\langle$ -, $-\rangle$ trên $E$, nếu $G = (g_{ij})$ với $g_{ij} = \langle e_{j}, e_{i}\rangle$ là Gram ma trận của Hermite tích $\langle$ -, $-\rangle$ w.r.t. cơ sở (basis) $(e_{1}, \dots  , e_{n})$, thì $G$ là Hermite xác định dương (positive definite). $2$. Với mọi ma trận chuyển cơ sở (change of basis matrix) $P$, Gram ma trận của $\langle$ -, $-\rangle$ đối với mới cơ sở (basis) là $P^{*}$ GP. $3$. Nếu $A$ là bất kỳ $n \times  n$ Hermite xác định dương (positive definite) ma trận, thì
$$\langle x, y\rangle = y^{*}Ax$$
Là Hermite tích trên $E$. Ta sẽ xem sau này rằng Ma trận Hermite (Hermitian matrix) là xác định dương (positive definite) khi và chỉ khi các trị riêng (các trị riêng (eigenvalues)) của nó là tất cả dương. Kết quả sau đây reminiscent của thứ nhất phân cực đồng nhất thức của Mệnh đề 14.1 có thể được được sử dụng để chứng minh rằng hai các ánh xạ tuyến tính (linear maps) là đồng nhất.

> **Mệnh đề 14.3.** Cho trước bất kỳ Không gian Hermite (Hermitian space) $E$ với Hermite tích $\langle$ -, $-\rangle$, với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$, nếu $\langle$ f(x), $x\rangle = 0$ với mọi $x \in E$, thì $f = 0$.

<!-- PAGE 535 -->

*Chứng minh.* Tính $\langle$ f(x $+ y), x + y\rangle$ và $\langle$ f(x - $y), x$ - $y\rangle$:
$$\langle f(x + y), x + y\rangle = \langle f(x), x\rangle + \langle f(x), y\rangle + \langle f(y), x\rangle + \langle y, y\rangle$$
$$\langle f(x -y), x -y\rangle = \langle f(x), x\rangle -\langle f(x), y\rangle -\langle f(y), x\rangle + \langle y, y\rangle ;$$
Thì trừ phương trình thứ hai từ thứ nhất để thu được
$$\langle f(x + y), x + y\rangle -\langle f(x -y), x -y\rangle = 2(\langle f(x), y\rangle + \langle f(y), x\rangle ).$$
Nếu $\langle$ f(u), $u\rangle = 0$ với mọi $u \in E$, ta thu được
$$\langle f(x), y\rangle + \langle f(y), x\rangle = 0for all x, y \in E.$$
Thì ở trên phương trình cũng nghiệm đúng nếu ta thay thế $x$ bởi ix, và ta thu được
$$i\langle f(x), y\rangle -i\langle f(y), x\rangle = 0,for all x, y \in E,$$
Do đó ta có
$$\langle f(x), y\rangle + \langle f(y), x\rangle = 0$$
$$\langle f(x), y\rangle -\langle f(y), x\rangle = 0,$$
Mà suy ra rằng $\langle$ f(x), $y\rangle = 0$ với mọi $x, y \in E$. Vì $\langle$ -, $-\rangle$ là xác định dương (positive definite), ta có f(x) $= 0$ với mọi $x \in E$; nghĩa là, $f = 0$. Một nên là careful không để áp dụng Mệnh đề 14.3 đến ánh xạ tuyến tính (linear map) trên thực Không gian Euclid (Euclidean space) bởi vì nó là sai! độc giả nên tìm phản ví dụ. Cauchy–Schwarz bất đẳng thức và Minkowski các bất đẳng thức mở rộng đến pre-Các không gian Hilbert và đến Các không gian Hermite.

> **Mệnh đề 14.4.** Cho $\langle E, \phi \rangle$ là pre-Không gian Hilbert (Hilbert space) với liên kết dạng toàn phương (quadratic form) $\Phi$. Với mọi $u, v \in E$, ta có Cauchy–Schwarz bất đẳng thức
$$|\phi (u, v)| \le p\overline{\Phi (}\overline{u}\overline{)} p\overline{\Phi (}\overline{v}\overline{)}.$$
Hơn nữa, nếu $\langle E, \phi \rangle$ là Không gian Hermite (Hermitian space), đẳng thức nghiệm đúng khi và chỉ khi $u$ và $v$ là phụ thuộc tuyến tính (linearly dependent). Ta cũng có Minkowski bất đẳng thức
$$p\overline{\Phi (}\overline{u}\overline{+}\overline{v}\overline{)} \le p\overline{\Phi (}\overline{u}\overline{) +} p\overline{\Phi (}\overline{v}\overline{)}.$$
Hơn nữa, nếu $\langle E, \phi \rangle$ là Không gian Hermite (Hermitian space), đẳng thức nghiệm đúng khi và chỉ khi $u$ và $v$ là phụ thuộc tuyến tính (linearly dependent), ở đâu ngoài ra, nếu u̸ $= 0$ và v̸ $= 0$, thì $u = \lambda v$ với một số thực $\lambda$ sao cho $\lambda  > 0$.

<!-- PAGE 536 -->

*Chứng minh.* Với mọi $u, v \in E$ và tất cả $\mu  \in \mathbb{C}$, ta có được quan sát rằng
$$\phi (u + \mu v, u + \mu v) = \phi (u, u) + 2\mathcal{ℜ}(\overline{\mu \phi}(u, v)) + |\mu |^{2}\phi (v, v).$$
Cho $\phi (u, v) = \rho e^{i\theta}$, ở đâu $|\phi (u$, v)| $= \rho  (\rho  \ge 0)$. Cho $F$: $\mathbb{R} \to \mathbb{R}$ là hàm được định nghĩa sao cho
$$F(t) = \Phi (u + te^{i\theta}v),$$
Với mọi $t \in \mathbb{R}$. ở trên chỉ ra rằng
$$F(t) = \phi (u, u) + 2t|\phi (u, v)| + t^{2}\phi (v, v) = \Phi (u) + 2t|\phi (u, v)| + t^{2}\Phi (v).$$
Vì $\phi$ được giả sử là dương, ta có F(t) $\ge 0$ với mọi $t \in \mathbb{R}$. Nếu $\Phi (v) = 0$, ta phải có $\phi (u, v) = 0$, vì ngược lại, F(t) có thể được tạo âm bằng cách chọn $t$ âm và nhỏ đủ. Nếu $\Phi (v) > 0$, trong thứ tự cho F(t) là không âm, phương trình
$$\Phi (u) + 2t|\phi (u, v)| + t^{2}\Phi (v) = 0$$
Phải không có phân biệt thực các nghiệm, mà là tương đương đến
$$|\phi (u, v)|^{2}\le \Phi (u)\Phi (v).$$
Lấy square nghiệm (root) trên cả hai các vế/cạnh cho ta Cauchy–Schwarz bất đẳng thức. Cho phần thứ hai của khẳng định, nếu $\phi$ là xác định dương (positive definite), ta argue như sau. Nếu $u$ và $v$ là phụ thuộc tuyến tính (linearly dependent), ta kiểm chứng được ngay rằng ta thu được đẳng thức. Ngược lại, nếu
$$|\phi (u, v)|^{2}= \Phi (u)\Phi (v),$$
Thì có hai các trường hợp. Nếu $\Phi (v) = 0$, vì $\phi$ là xác định dương (positive definite), ta phải có $v = 0$, do đó $u$ và $v$ là phụ thuộc tuyến tính (linearly dependent). Ngược lại, phương trình
$$\Phi (u) + 2t|\phi (u, v)| + t^{2}\Phi (v) = 0$$
Có gấp đôi nghiệm (root) $t_{0}$, và do đó
$$\Phi (u + t_{0}e^{i\theta}v) = 0.$$
Vì $\phi$ là xác định dương (positive definite), ta phải có
$$u + t_{0}e^{i\theta}v = 0,$$
Mà chỉ ra rằng $u$ và $v$ là phụ thuộc tuyến tính (linearly dependent). Nếu ta square Minkowski bất đẳng thức, ta thu được
$$\Phi (u + v) \le \Phi (u) + \Phi (v) + 2p\overline{\Phi (}\overline{u}\overline{)} p\overline{\Phi (}\overline{v}\overline{)}.$$
Tuy nhiên, ta được quan sát trước đó rằng
$$\Phi (u + v) = \Phi (u) + \Phi (v) + 2\mathcal{ℜ}(\phi (u, v)).$$

<!-- PAGE 537 -->
Do đó, nó là đủ để chứng minh rằng
$$\mathcal{ℜ}(\phi (u, v)) \le p\overline{\Phi (}\overline{u}\overline{)} p\overline{\Phi (}\overline{v}\overline{)},$$
Nhưng điều này suy ra từ Cauchy–Schwarz bất đẳng thức
$$|\phi (u, v)| \le p\overline{\Phi (}\overline{u}\overline{)} p\overline{\Phi (}\overline{v}\overline{)}$$
Và sự kiện rằng $\mathcal{ℜ} z \le$ |z|. Nếu $\phi$ là xác định dương (positive definite) và $u$ và $v$ là phụ thuộc tuyến tính (linearly dependent), ta kiểm chứng được ngay rằng ta thu được đẳng thức. Ngược lại, nếu đẳng thức nghiệm đúng trong Minkowski bất đẳng thức, ta phải có
$$\mathcal{ℜ}(\phi (u, v)) =p\overline{\Phi (}\overline{u}\overline{)} p\overline{\Phi (}\overline{v}\overline{)},$$
Mà suy ra rằng
$$|\phi (u, v)| =p\overline{\Phi (}\overline{u}\overline{)} p\overline{\Phi (}\overline{v}\overline{)},$$
Vì ngược lại, bởi Cauchy–Schwarz bất đẳng thức, ta sẽ có
$$\mathcal{ℜ}(\phi (u, v)) \le |\phi (u, v)| <p\overline{\Phi (}\overline{u}\overline{)} p\overline{\Phi (}\overline{v}\overline{)}.$$
Do đó, đẳng thức nghiệm đúng trong Cauchy–Schwarz bất đẳng thức, và
$$\mathcal{ℜ}(\phi (u, v)) = |\phi (u, v)|.$$
Nhưng khi đó ta được chứng minh trong Cauchy–Schwarz trường hợp rằng $u$ và $v$ là phụ thuộc tuyến tính (linearly dependent). Vì ta cũng chỉ được chứng minh rằng $\phi (u, v)$ là thực và không âm, hệ số của proportionality giữa $u$ và $v$ là thật vậy không âm. Như trong Euclidean trường hợp, nếu $\langle$ Không gian Hermite (Hermitian space), Minkowski bất đẳng thức
$$p \frac{E, \phi \rangle isa}{\Phi (u + v)} \le p\overline{\Phi (}\overline{u}\overline{) +} p\overline{\Phi (}\overline{v}\overline{)}$$
$$shows that the map u \mapsto p\overline{\Phi (}\overline{u}\overline{)} is a norm on E. \frac{The}{\Phi (u)} norm induced by \phi  is called the$$
Hermite chuẩn (norm) được cảm sinh bởi $\phi$. Ta thường ký hiệu $p$ bởi $\|u\|$, và Cauchy–Schwarz bất đẳng thức được viết như
$$|u \cdot  v| \le \|u\|\|v\|.$$
Vì Không gian Hermite (Hermitian space) là không gian vectơ định chuẩn (normed vector space), nó là không gian tôpô (topological space) dưới tôpô được cảm sinh bởi chuẩn (norm) (cơ sở (basis) cho điều này tôpô được cho bởi mở các hình cầu $B_{0}(u, \rho$) của tâm $u$ và bán kính $\rho  > 0$, ở đâu
$$B_{0}(u, \rho ) = {v \in E | \|v -u\|< \rho }.$$
Nếu $E$ có hữu hạn số chiều, mọi ánh xạ tuyến tính (linear map) là liên tục; xem Chương $9$ (hoặc Lang $[115, 116]$, Dixmier $[52]$, hoặc Schwartz $[156, 157])$. Cauchy–Schwarz bất đẳng thức
$$|u \cdot  v| \le \|u\|\|v\|$$
