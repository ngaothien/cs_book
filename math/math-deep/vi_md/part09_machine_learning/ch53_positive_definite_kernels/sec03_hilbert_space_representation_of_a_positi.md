# Không gian Hilbert (Hilbert space) Biểu diễn của Dương Hạt nhân (kernel)


<!-- PAGE 1958 -->
Là nhân xác định dương (positive definite kernel). Cho $f$: $X \to \mathbb{R}$ là hàm cho trước bởi
$$f(x) =\overline{e}_{2\sigma}^{-\|x\|22} .$$
Thì theo Mệnh đề 53.6(3),
$$\kappa_{2} (x, y) = f(x)f(y) =\overline{e}_{2\sigma}^{-\|x\|22}\overline{e}_{2\sigma}^{-\|y\|22}=\overline{e}_{2\sigma}^{-\|x\|2X+2\|y\|2X}$$
Là nhân xác định dương (positive definite kernel). Theo Mệnh đề 53.5, hàm $\kappa_{1} \kappa_{2}$ là nhân xác định dương (positive definite kernel), nghĩa là
$$\kappa_{1} (x, y)\kappa_{2} (x, y) =\overline{e}_{\sigma}^{\langle x,y2\rangle X}\overline{e}_{2\sigma}^{-\|x\|2X+2\|y\|2X}=\overline{e}_{\sigma2\sigma}^{\langle x,y2\rangle X-\|x\|2X+2\|y\|2X}=\overline{e}_{2\sigma}^{-\|x-y2\|2X}$$
Là nhân xác định dương (positive definite kernel).

> **Định nghĩa 53.4.** nhân xác định dương (positive definite kernel)
$$\kappa (x, y) =\overline{e}_{2\sigma}^{-\|x-y2\|2X}$$
Được gọi là một Gaussian hạt nhân (kernel). hạt nhân (hạt nhân (kernel)) này đòi hỏi đặc trưng (feature) ánh xạ trong vô hạn chiều không gian bởi vì nó là vô hạn tổng của phân biệt các hạt nhân.
Nhận xét: Nếu $\kappa_{1}$ là nhân xác định dương (positive definite kernel), chứng minh của Mệnh đề 53.7(3) là ngay lập tức được điều chỉnh để chỉ ra rằng
$$\kappa (x, y) =\overline{e}_{2\sigma}^{-\kappa1(x,x)+\kappa1(y,y2)-2\kappa1(x,y)}$$
Là nhân xác định dương (positive definite kernel). Tiếp theo ta chứng minh rằng mọi nhân xác định dương (positive definite kernel) phát sinh từ đặc trưng (feature) ánh xạ trong Không gian Hilbert (Hilbert space) mà là hàm không gian.

## 53.3 Không gian Hilbert (Hilbert space) Biểu diễn của Dương

$$Definite Kernel$$
Kết quả sau đây chỉ ra cách mà để xây dựng so-called không gian Hilbert nhân tái tạo (RKHS), cho ngắn RKHS, từ nhân xác định dương (positive definite kernel).

> **Định lý 53.8.** Cho $\kappa$: $X \times  X \to \mathbb{C}$ là nhân xác định dương (positive definite kernel) trên khác rỗng tập hợp $X$. Với mọi $x \in X$, cho $\kappa_{x}$: $X \to \mathbb{C}$ là hàm cho trước bởi
$$\kappa_{x} (y) = \kappa (x, y),y \in X.$$

<!-- PAGE 1959 -->
$$\mathbb{C}^{X}  \mathbb{C}$$
Cho $H_{0}$ là không gian con của không gian vectơ (vector space) của các hàm từ $X$ đến được sinh (spanned) bởi họ của các hàm $(\kappa_{x} )_{\in X}$, và cho $\phi$: $X \to H_{0}$ là ánh xạ cho trước bởi $\phi (x) = \kappa_{x}$. Có một Hermite tích vô hướng (inner product) $\langle$ -, $-\rangle$ trên $H_{0}$ sao cho
$$\kappa (x, y) = \langle \phi (x), \phi (y)\rangle ,for all x, y \in X.$$
$$\mathbb{C}^{X}$$
Đầy đủ hóa $H$ của $H_{0}$ là Không gian Hilbert (Hilbert space), và ánh xạ $\eta$: $H \to$ cho trước bởi
$$\eta (f)(x) = \langle f, \kappa_{x} \rangle ,x \in X,$$
Là tuyến tính và đơn ánh (injective), do đó $H$ có thể được đồng nhất với không gian con của $\mathbb{C}^{X}$. Ta cũng có
$$\kappa (x, y) = \langle \phi (x), \phi (y)\rangle ,for all x, y \in X.$$
Với mọi $f \in H_{0}$ và tất cả $x \in X$,
$$\langle f, \kappa_{x} \rangle = f(x),(*)$$
Tính chất đã biết như reproducing tính chất.

*Chứng minh.* Bước $1$. Định nghĩa candidate tích vô hướng (inner product).
$$For any two linear combinations f = \sum_{j}  p=1 \alpha_{j} \kappa_{xj}  and g = \sum_{k}  q=1 \beta_{k} \kappa_{yk}  in H_{0}, with$$
$x_{j}, y_{k} \in X$ và $\alpha_{j} , \beta_{k}  \in \mathbb{C}$, định nghĩa $\langle f, g\rangle$ bởi
$$\langle f, g\rangle = \sum_{j=1}^{p}  \sum_{k=1}^{q}  \alpha_{j} \overline{\beta}_{k}\kappa (x_{j}, y_{k}).(\dagger )$$
$$\frac{At first glance, the above expression appears to depend on the expression of}{\kappa (y_{k}, x_{j}),} f and g as linear$$
Các tổ hợp, nhưng vì $\kappa (x_{j}, y_{k}) =$ nhận thấy rằng
$$\sum_{k=1}^{q}  \overline{\beta}_{k}f(y_{k}) = \sum_{j=1}^{p}  \sum_{k=1}^{q}  \alpha_{j} \overline{\beta}_{k}\kappa (x_{j}, y_{k}) = \sum_{j=1}^{p}  \alpha_{j} \overline{g}\overline{(}\overline{x}_{j}\overline{)},(*)$$
Và vì thứ nhất và số hạng thứ ba là bằng nhau với mọi các tổ hợp tuyến tính biểu diễn $f$ và $g$, ta kết luận rằng $(\dagger$) phụ thuộc chỉ trên $f$ và $g$ và không trên biểu diễn của chúng như tổ hợp tuyến tính (linear combination). Bước $2$. Chứng minh rằng tích vô hướng (inner product) được định nghĩa bởi $(\dagger$) là Hermite nửa xác định. Hiển nhiên $(\dagger$) định nghĩa Hermite sequilinear tạo thành. Với mọi $f \in H_{0}$, ta có
$$\langle f, f\rangle = \sum_{j,k=1}^{p}  \alpha_{j} \overline{\alpha}_{k}\kappa (x_{j}, x_{k}) \ge 0,$$
Vì $\kappa$ là nhân xác định dương (positive definite kernel).

<!-- PAGE 1960 -->
Bước $3$. Chứng minh rằng tích vô hướng (inner product) được định nghĩa bởi $(\dagger$) là xác định dương (positive definite). Với mọi hữu hạn tập con ${f_{1}, \dots  , f_{n}}$ của $H_{0}$ và bất kỳ $z \in \mathbb{C}^{n}$, ta có
$$*+$$
$$\sum_{j,k=1}^{n}  \langle f_{j}, f_{k}\rangle z_{j}\overline{z}_{k} = \sum_{j=1}^{n}  z_{j}f_{j}, \sum_{j=1}^{n}  z_{j}f_{j}\ge 0,$$
Mà chỉ ra rằng ánh xạ $(f, g) \mapsto \langle f, g\rangle$ từ $H_{0} \times  H_{0}$ đến $\mathbb{C}$ là nhân xác định dương (positive definite kernel). Nhận thấy rằng với mọi $f \in H_{0}$ và tất cả $x \in X, (\dagger$) suy ra rằng
$$\langle f, \kappa_{x} \rangle = \sum_{j=1}^{k}  \alpha_{j} \kappa (x_{j}, x) = f(x),$$
Tính chất đã biết như reproducing tính chất. ở trên suy ra rằng
$$\langle \kappa_{x} , \kappa_{y} \rangle = \kappa (x, y).(**)$$
Theo Mệnh đề 53.4 ứng dụng đến nhân xác định dương (positive definite kernel) $(f, g) \mapsto \langle f, g\rangle$, ta có
$$|\langle f, \kappa_{x} \rangle |^{2}\le \langle f, f\rangle \langle \kappa_{x} , \kappa_{x} \rangle ,$$
Rằng là,
$$|f(x)|^{2}\le \langle f, f\rangle \kappa (x, x),$$
Do đó $\langle f, f\rangle = 0$ suy ra rằng f(x) $= 0$ với mọi $x \in X$, mà có nghĩa là $\langle$ -, $-\rangle$ như đã định nghĩa bởi $(\dagger$) là xác định dương (positive definite). Vì vậy, $\langle$ -, $-\rangle$ là Hermite tích vô hướng (inner product) trên $H_{0}$, và bởi (**) và vì $\phi (x) = \kappa_{x}$, ta có
$$\kappa (x, y) = \langle \phi (x), \phi (y)\rangle ,for all x, y \in X.$$
Bước $4$. Định nghĩa phép nhúng (embedding) $\eta$. Cho $H$ là Không gian Hilbert (Hilbert space) mà là đầy đủ hóa của $H_{0}$, sao cho $H_{0}$ là trù mật trong $H$.
$$\mathbb{C}^{X}$$
Ánh xạ $\eta$: $H \to$ cho trước bởi
$$\eta (f)(x) = \langle f, \kappa_{x} \rangle$$
Là hiển nhiên tuyến tính, và nó là đơn ánh (injective) bởi vì họ $(\kappa_{x} )_{x\in X}$ sinh ra $H_{0}$ mà là trù mật trong $H$, do đó nó là cũng trù mật trong $H$, do đó nếu $\langle f, \kappa_{x} \rangle = 0$ với mọi $x \in X$, thì $f = 0$.

> **Hệ quả 53.9.** Nếu ta đồng nhất hàm $f \in H$ với hàm $\eta (f)$, thì ta có reproducing tính chất
$$\langle f, \kappa_{x} \rangle = f(x),for all f \in H and all x \in X.$$
$$\mathbb{C}^{X}$$
Nếu $X$ là hữu hạn, thì là hữu hạn chiều. Nếu $X$ là khả ly không gian tôpô (topological space) và nếu $\kappa$ là liên tục, thì nó có thể được được hiển thị rằng $H$ là khả ly Không gian Hilbert (Hilbert space).
