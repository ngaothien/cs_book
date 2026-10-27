# Jacobian Các ma trận


<!-- PAGE 1457 -->
Điều này khái niệm là tổng quát hóa của khái niệm được định nghĩa trong Định nghĩa 39.5. Thực ra, khi $E$ là có số chiều $n$, và hệ quy chiếu (frame) $(a_{0}, (u_{1}, \dots  , u_{n}))$ có đã được được chọn, ta có thể viết $E = (E_{1}, a_{1}) \oplus \cdots  \oplus (E_{n}, a_{n})$, với một số hiển nhiên $(E_{j}, a_{j})$ (như được giải thích chỉ sau Mệnh đề 39.9), và thì
$$D_{j}f(c)(\lambda u_{j}) = \lambda \partial_{j} f(c),$$
Và hai các khái niệm là consistent. định nghĩa của $i_{j}^{c}$ và của $D_{j}f(c)$ cũng làm cho nghĩa cho hữu hạn tích $E_{1} \times  \cdots  \times  E_{n}$ của các không gian afin $E_{i}$. Ta sẽ sử dụng một cách tự do ký hiệu $\partial_{j}$ f(c) thay vì của $D_{j}f(c)$. khái niệm $\partial_{j}$ f(c) đã giới thiệu trong Định nghĩa 39.5 là một cách thực rằng của vectơ đạo hàm, trong khi đó $D_{j}f(c)$ là tương ứng ánh xạ tuyến tính (linear map). Mặc dù perhaps confusing, ta đồng nhất hai các khái niệm. sau đây mệnh đề nghiệm đúng.

> **Mệnh đề 39.11.** Cho trước được chuẩn (norm) không gian afin (affine space) $E = (E_{1}, a_{1}) \oplus \cdots  \oplus (E_{n}, a_{n})$, và được chuẩn (norm) không gian afin (affine space) $F$, cho trước bất kỳ mở tập con $A$ của $E$, với mọi hàm $f$: $A \to F$, với mọi $c \in A$, nếu Df(c) tồn tại, thì mỗi $D_{j}f(c)$ tồn tại, và
$$Df(c)(u_{1}, \dots  , u_{n}) = D_{1}f(c)(u_{1}) + \cdots  + D_{n}f(c)(u_{n}),$$
Với mọi $u_{i} \in E_{i}, 1 \le i \le n$. cùng kết quả nghiệm đúng cho hữu hạn tích $E_{1} \times  \cdots  \times  E_{n}$.

*Chứng minh.* Vì mọi $c \in E$ có thể được viết dưới dạng $c = a + c$ - $a$, ở đâu $a = (a_{1}, \dots  , a_{n})$, định nghĩa $\longrightarrow \longrightarrow f_{a}$: $E \to F$ sao cho, $f_{a}(u) =$ f($+ u)$, với mọi $u \in E$, rõ ràng, Df(c) $= Df_{a}(c$ - $a)$, và
$$\longrightarrow$$
Do đó, ta có thể hoạt động/công trình với hàm $f_{a}$ có miền xác định là không gian vectơ (vector space) $E$. mệnh đề là thì đơn giản ứng dụng của Định lý 39.6.

## 39.3 Jacobian Các ma trận

Nếu cả hai $E$ và $F$ là của hữu hạn số chiều, với mọi hệ quy chiếu (frame) $(a_{0}, (u_{1}, \dots  , u_{n}))$ của $E$ và bất kỳ hệ quy chiếu (frame) $(b_{0}, (v_{1}, \dots  , v_{m}))$ của $F$, mọi hàm $f$: $E \to F$ được xác định bởi $m$ các hàm $f_{i}$: $E \to \mathbb{R}$ (hoặc $f_{i}$: $E \to \mathbb{C})$, ở đâu
$$f(x) = b_{0} + f_{1}(x)v_{1} + \cdots  + f_{m}(x)v_{m},$$
Với mọi $x \in E$. Từ Mệnh đề 39.1, ta có
$$Df(a)(u_{j}) = D_{uj}f(a) = \partial_{j} f(a),$$
Và từ Mệnh đề 39.10, ta có
$$Df(a)(u_{j}) = Df_{1}(a)(u_{j})v_{1} + \cdots  + Df_{i}(a)(u_{j})v_{i} + \cdots  + Df_{m}(a)(u_{j})v_{m},$$
Rằng là,
$$Df(a)(u_{j}) = \partial_{j} f_{1}(a)v_{1} + \cdots  + \partial_{j} f_{i}(a)v_{i} + \cdots  + \partial_{j} f_{m}(a)v_{m}.$$

<!-- PAGE 1458 -->
Vì cột thứ $j$ của ma trận cỡ $m\times n$ biểu diễn Df() w.r.t. các cơ sở $(u_{1}, \dots  , u_{n})$ và $(v_{1}, \dots  , v_{m})$ bằng các thành phần của vectơ $Df(a)(u_{j})$ trên cơ sở (basis) $(v_{1}, \dots  ,v_{m})$, ánh xạ tuyến tính (linear map) Df() được xác định bởi ma trận cỡ $m \times n$ J(f)() $= (\partial_{j} f_{i}(a))$, (hoặc J(f)() $=$
$$( \frac{\partial f_{i}}{\partial x_{j}} (a))):$$
$$J(f)(a) = \begin{pmatrix} \partial_{1} f_{1}(a) & \partial_{2} f_{1}(a) & \dots & \partial_{n} f_{1}(a) \\ \partial_{1} f_{2}(a) & \partial_{2} f_{2}(a) & \dots & \partial_{n} f_{2}(a) \\ \vdots & \vdots & \ddots & \vdots \\ \partial_{1} f_{m}(a) & \partial_{2} f_{m}(a) & \dots & \partial_{n} f_{m}(a) \end{pmatrix}$$
Hoặc
$$J(f)(a) = \begin{pmatrix} \partial f_{1} & \partial f_{1} & \partial f_{1} \\ (a) & (a) & \dots & (a) \\ \partial x_{1} & \partial x_{2} & \partial x_{n} \\ \partial f_{2} & \partial f_{2} & \partial f_{2} \\ (a) & (a) & \dots & (a) \\ \partial x_{1} & \partial x_{2} & \partial x_{n} \\ \vdots & \vdots & \ddots & \vdots \\ \partial f_{m} & \partial f_{m} & \partial f_{m} \\ (a) & (a) & \dots & (a) \\ \partial x_{1} & \partial x_{2} & \partial x_{n} \end{pmatrix}$$

> **Định nghĩa 39.6.** ma trận J(f)() được gọi là Ma trận Jacobi (Jacobian matrix) của Df tại. Khi $m = n$, định thức (determinant), det(J(f)()), của J(f)() được gọi là Jacobian của Df(). Từ trước đó kết quả, ta biết rằng định thức (định thức (determinant)) này thực ra chỉ phụ thuộc vào Df(), và không trên cụ thể các cơ sở. Tuy nhiên, các đạo hàm riêng cho có nghĩa là cho việc tính toán nó.
$$\mathbb{R}^{n}  \mathbb{R}^{m} \mathbb{R}^{n} \mathbb{R}^{m}$$
Khi $E =$ và $F =$, với mọi hàm $f$: $\to$, nó là dễ để tính
$$partial derivatives \frac{\partial f_{i}}{\partial x_{j}} (a). We simply treat the function f_{i} : \mathbb{R}^{n}\to \mathbb{R} as a function of its j-th$$
Lập luận, để lại những cái khác cố định, và tính đạo hàm như trong Định nghĩa 39.1, nghĩa là, thông thường đạo hàm.
$$\mathbb{R}^{2} \mathbb{R}^{2}$$

> **Ví dụ 39.5.** Ví dụ, xét hàm $f$: $\to$, được định nghĩa sao cho
$$f(r, \theta ) = (r \cos(\theta ), r \sin(\theta )).$$
Thì, ta có
$$J(f)(r, \theta ) = \begin{pmatrix} \cos(\theta ) & -r \sin(\theta ) \\ \sin(\theta ) & r \cos(\theta ) \end{pmatrix}$$
Và Jacobian (định thức (determinant)) có giá trị det(J(f)(r, $\theta$)) $= r$. Trong trường hợp ở đâu $E = \mathbb{R}$ (hoặc $E = \mathbb{C})$, với mọi hàm $f$: $\mathbb{R} \to F$ (hoặc $f$: $\mathbb{C} \to F)$, Ma trận Jacobi (Jacobian matrix) của Df() là vectơ cột (column vector). Thực ra, điều này vectơ cột (column vector) là chỉ $D_{1}f(a)$. Thì, với mọi $\lambda  \in \mathbb{R}$ (hoặc $\lambda  \in \mathbb{C})$,
$$Df(a)(\lambda ) = \lambda D_{1}f(a).$$
Trường hợp này là một cách đủ quan trọng đến warrant định nghĩa.

<!-- PAGE 1459 -->

> **Định nghĩa 39.7.** Cho trước hàm $f$: $\mathbb{R} \to F$ (hoặc $f$: $\mathbb{C} \to F)$, ở đâu $F$ được chuẩn (norm) không gian afin (affine space), vectơ
$$Df(a)(1) = D_{1}f(a)$$
Được gọi là vectơ đạo hàm hoặc velocity vectơ (trong thực trường hợp) tại. Ta thường đồng nhất Df() với của nó Ma trận Jacobi (Jacobian matrix) $D_{1}f(a)$, mà là vectơ cột (column vector) tương ứng với $D_{1}f(a)$. Lạm dụng ký hiệu, ta cũng cho Df() ký hiệu vectơ Df()(1) $= D_{1}f(a)$. Khi $E = \mathbb{R}$, vật lý interpretation là rằng $f$ định nghĩa (parametric) đường cong rằng là
$$\mathbb{R}^{m}$$
Trajectory của một số particle di chuyển trong như hàm của time, và vectơ $D_{1}f(a)$ là velocity của di chuyển particle f(t) tại $t = a$. Nó là thường hữu ích đến xét các hàm $f$: [, $b] \to F$ từ đóng khoảng/đoạn [, $b] \subseteq \mathbb{R}$ đến được chuẩn (norm) không gian afin (affine space) $F$, và đạo hàm của nó Df() trên [, $b]$, chẵn/ngay cả dù [, $b]$ là không mở. Trong trường hợp này, như trong trường hợp của nhận giá trị thực (real-valued) hàm, ta định nghĩa phải đạo hàm $D_{1}f(a_{+})$ tại, và trái đạo hàm $D_{1}f(b_{-})$ tại $b$, và ta giả sử của chúng sự tồn tại.

> **Ví dụ 39.6.** $1$. Khi $A = (0, 1)$ và $F =\mathbb{R}^{3}$, hàm
$$\mathbb{R}^{3}  \mathbb{R}^{3}$$
$f$: $(0, 1) \to$ định nghĩa (parametric) đường cong trong. Nếu $f = (f_{1}, f_{2}, f_{3})$, của nó Ma trận Jacobi (Jacobian matrix) tại $a \in \mathbb{R}$ là
$$J(f)(a) = \begin{pmatrix} \partial f_{1} \\ (a) \\ \partial t \\ \partial f_{2} \\ (a) \\ \partial t \\ \partial f_{3} \\ (a) \end{pmatrix} .$$
$$\partial t$$
Xem Hình 39.4.
$$Figure 39.4: The red space curve f(t) = (\cos(t), \sin(t), t).$$

<!-- PAGE 1460 -->
$$The velocity vectors J(f)(a) = \begin{pmatrix} -\sin(t) \\ \cos(t) \\ 1 \end{pmatrix} are represented by the blue arrows.$$
$$\mathbb{R}^{2}  \mathbb{R}^{3} \mathbb{R}^{2} \mathbb{R}^{3}$$
$2$. Khi $E =$ và $F =$, hàm $\phi$: $\to$ định nghĩa parametric mặt.
$$\mathbb{R}^{2}$$
Đặt $\phi  = (f, g, h)$, của nó Ma trận Jacobi (Jacobian matrix) tại $a \in$ là
$$J(\phi )(a) = \begin{pmatrix} \partial f & \partial f \\ (a) & (a) \\ \partial u & \partial v \\ \partial g & \partial g \\ (a) & (a) \\ \partial u & \partial v \\ \partial h & \partial h \\ (a) & (a) \end{pmatrix} .$$
$$\partial u\partial v$$
$$See Figure 39.5. The Jacobian matrix is J(f)(a) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 2u & 2v \end{pmatrix} . The first column is$$
$$Figure 39.5: The parametric surface x = u, y = v, z = u^{2}+ v^{2}.$$
Vectơ tiếp tuyến đến hồng u-direction đường cong, trong khi cột thứ hai là vectơ tiếp tuyến đến xanh lam v-direction đường cong.
$$\mathbb{R}^{3} \mathbb{R} \mathbb{R}^{3} \mathbb{R}\mathbb{R}^{3}$$
$3$. Khi $E =$ và $F =$, cho hàm $f$: $\to$, Ma trận Jacobi (Jacobian matrix) tại $a \in$ là
$$J(f)(a) = \begin{pmatrix} \partial f & \partial f & \partial f \\ (a) & (a) & (a) \\ \partial x & \partial y & \partial z \end{pmatrix} .$$
$$\mathbb{R}^{n} \mathbb{R}\mathbb{R}^{n}$$

> **Định nghĩa 39.8.** Tổng quát hơn, khi $f$: $\to$, Ma trận Jacobi (Jacobian matrix) tại $a \in$ là vectơ hàng (row vector)
$$J(f)(a) = \begin{pmatrix} \partial f \\ \partial f \\ (a)\cdots & (a) \\ \partial x_{1} & \partial x_{n} \end{pmatrix} .$$

<!-- PAGE 1461 -->
Chuyển vị (chuyển vị (transpose)) của nó là vectơ cột (column vector) được gọi là gradien của $f$ tại, được ký hiệu bởi gradf() hoặc $\nabla$ f(). Thì, cho trước bất kỳ $v \in \mathbb{R}^{n}$, lưu ý rằng
$$Df(a)(v) = \frac{\partial f}{\partial x_{1}} (a) v_{1} + \cdots  + \frac{\partial f}{\partial x_{n}} (a) v_{n} = gradf(a) \cdot  v,$$
Vô hướng (scalar) tích của gradf() và $v$.
$$\mathbb{R}^{n} \mathbb{R}^{m} \mathbb{R}$$

> **Ví dụ 39.7.** Xét hàm $f$: $\times \to$ từ Ví dụ 39.4 cho trước bởi
$$f(v, \lambda ) = \lambda^{\top} Cv = v^{\top}C^{\top}\lambda ,v \in \mathbb{R}^{n}, \lambda  \in \mathbb{R}^{m},$$
Ở đâu $C$ là một ma trận cỡ $m \times  n$. Ta đã chỉ ra rằng đạo hàm của nó được cho bởi
$$df_{(v,\lambda)}(w, \mu ) = (C^{\top}\lambda )^{\top}w + (Cv)^{\top}\mu  = (C^{\top}\lambda Cv)^{\top} \begin{pmatrix} v \\ \lambda \end{pmatrix} ,$$
Do đó gradien của $f$ tại $(v, \lambda$) là
$$\nabla f_{(v,\lambda)} = \begin{pmatrix} C^{\top}\lambda \\ Cv \end{pmatrix} .$$
$$\mathbb{R}^{n} \mathbb{R}$$

> **Ví dụ 39.8.** Xét toàn phương hàm $f$: $\to$ cho trước bởi
$$f(x) = x^{\top}Ax,x \in \mathbb{R}^{n},$$
Ở đâu $A$ là thực $n \times  n$ ma trận đối xứng (symmetric matrix). Ta khẳng định rằng
$$df_{u}(h) = 2u^{\top}Ahfor all u, h \in \mathbb{R}^{n}.$$
Vì $A$ là đối xứng, ta có
$$f(u + h) = (u^{\top}+ h^{\top})A(u + h)$$
$$= u^{\top}Au + u^{\top}Ah + h^{\top}Au + h^{\top}Ah$$
$$= u^{\top}Au + 2u^{\top}Ah + h^{\top}Ah,$$
Do đó ta có
$$f(u + h) -f(u) -2u^{\top}Ah = h^{\top}Ah.$$
Nếu ta viết
$$\epsilon (h) = \frac{h^{\top}Ah}{\|h\|}$$
Cho $h \in / 0$ ở đâu $\|\|$ là 2-chuẩn (norm), bởi Cauchy–Schwarz ta có
$$\|$$
$$\|\|\|\|\|\|^{2}\|$$
$$|\epsilon (h)| \le \frac{hAh}{\|h\|} \le \frac{hA}{\|h\|} = \|h\|\|A\|,$$

<!-- PAGE 1462 -->
Mà chỉ ra rằng $lim_{h\mapsto0} \epsilon (h) = 0$. Vì vậy,
$$df_{u}(h) = 2u^{\top}Ahfor all u, h \in \mathbb{R}^{n},$$
Như đã khẳng định. công thức này chỉ ra rằng gradien $\nabla f_{u}$ của $f$ tại $u$ được cho bởi
$$\nabla f_{u} = 2Au.$$
Như thứ nhất hệ quả ta thu được gradien của hàm của tạo thành
$$f(x) = \frac{1}{2} x^{\top}Ax -b^{\top}x,$$
Ở đâu $A$ là đối xứng $n \times  n$ ma trận và $b$ là một số vectơ $b \in \mathbb{R}^{n}$. Vì đạo hàm của tuyến tính hàm là chính nó, ta thu được
$$df_{u}(h) = u^{\top}Ah -b^{\top}h,$$
Và gradien của $f$ được cho bởi
$$\nabla f_{u} = Au -b.$$
Như thứ hai hệ quả ta thu được gradien của hàm
$$f(x) = \|Ax -b\|_{2}^{2} = (Ax -b)^{\top}(Ax -b) = (x^{\top}A^{\top}-b^{\top})(Ax -b)$$
Mà là hàm để cực tiểu hóa trong bình phương tối thiểu (least squares) bài toán, ở đâu $A$ là một ma trận cỡ $m \times  n$. Ta có
$$f(x) = x^{\top}A^{\top}Ax -x^{\top}A^{\top}b -b^{\top}Ax + b^{\top}b = x^{\top}A^{\top}Ax -2b^{\top}Ax + b^{\top}b,$$
Và vì đạo hàm của hằng số hàm là $0$ và đạo hàm của tuyến tính hàm là chính nó, ta thu được
$$df_{u}(h) = 2u^{\top}A^{\top}Ah -2b^{\top}Ah.$$
Hệ quả là, gradien của $f$ được cho bởi
$$\nabla f_{u} = 2A^{\top}Au -2A^{\top}b.$$

> **Ví dụ 39.9.** Trong Ví dụ 40.3 từ Mục 40.1, ta cần để tìm gradien của hàm
$$L(v, \lambda ) = \frac{1}{2} v^{\top}Av -v^{\top}b + v^{\top}C^{\top}\lambda  -d^{\top}\lambda ,$$
Ở đâu $A$ là $n \times  n$ ma trận đối xứng (symmetric matrix) và $C$ là một ma trận cỡ $m \times  n$ của hạng (rank) $m$. Từ Ví dụ 39.7 và Ví dụ 39.8, ta có
$$\nabla L_{((v,\lambda)} = \begin{pmatrix} Av -b \\ 0 \end{pmatrix} + \begin{pmatrix} C^{\top}\lambda \\ Cv \end{pmatrix} + \begin{pmatrix} 0 \\ -d \end{pmatrix} = \begin{pmatrix} Av -b + C^{\top}\lambda \\ Cv -d \end{pmatrix} .$$

<!-- PAGE 1463 -->
Khi $E, F$, và $G$ có hữu hạn số chiều, và $(a_{0}, (u_{1}, \dots  , u_{p}))$ là hệ quy chiếu afin (affine frame) cho $E, (b_{0}, (v_{1}, \dots  , v_{n}))$ là hệ quy chiếu afin (affine frame) cho $F$, và $(c_{0}, (w_{1}, \dots  , w_{m}))$ là hệ quy chiếu afin (affine frame) cho $G$, nếu $A$ là mở tập con của $E, B$ là mở tập con của $F$, với mọi các hàm $f$: $A \to F$ và $g: B \to G$, sao cho f() $\subseteq B$, với mọi $a \in A$, đặt $b =$ f(), và $h = g \circ f$, nếu Df() tồn tại và Dg(b) tồn tại, theo Định lý 39.6, Ma trận Jacobi (Jacobian matrix) J(h)() $=$ J(g $\circ$ f)() w.r.t. các cơ sở $(u_{1}, \dots  , u_{p})$ và $(w_{1}, \dots  , w_{m})$ là tích của Jacobian các ma trận J(g)(b) w.r.t. các cơ sở $(v_{1}, \dots  , v_{n})$ và $(w_{1}, \dots  , w_{m})$, và J(f)() w.r.t. các cơ sở $(u_{1}, \dots  , u_{p})$ và $(v_{1}, \dots  , v_{n})$:
$$J(h)(a) = \begin{pmatrix} \partial_{1} g_{1}(b) & \partial_{2} g_{1}(b) & \dots & \partial_{n} g_{1}(b) \\ \partial_{1} g_{2}(b) & \partial_{2} g_{2}(b) & \dots & \partial_{n} g_{2}(b) \\ \vdots & \vdots & \ddots & \vdots \\ \partial_{1} g_{m}(b) & \partial_{2} g_{m}(b) & \dots & \partial_{n} g_{m}(b) \end{pmatrix} \begin{pmatrix} \partial_{1} f_{1}(a) & \partial_{2} f_{1}(a) & \dots & \partial_{p} f_{1}(a) \\ \partial_{1} f_{2}(a) & \partial_{2} f_{2}(a) & \dots & \partial_{p} f_{2}(a) \\ \vdots & \vdots & \ddots & \vdots \\ \partial_{1} f_{n}(a) & \partial_{2} f_{n}(a) & \dots & \partial_{p} f_{n}(a) \end{pmatrix}$$
Hoặc
$$J(h)(a) = \begin{pmatrix} \partial g_{1} & \partial g_{1} & \partial g_{1} \\ (b) & (b) & \dots & (b) \\ \partial y_{1} & \partial y_{2} & \partial y_{n} \\ \partial g_{2} & \partial g_{2} & \partial g_{2} \\ (b) & (b) & \dots & (b) \\ \partial y_{1} & \partial y_{2} & \partial y_{n} \\ \vdots & \vdots & \ddots & \vdots \\ \partial g_{m} & \partial g_{m} & \partial g_{m} \\ (b) & (b) & \dots & (b) \\ \partial y_{1} & \partial y_{2} & \partial y_{n} \end{pmatrix} \begin{pmatrix} \partial f_{1} & \partial f_{1} & \partial f_{1} \\ (a) & (a) & \dots & (a) \\ \partial x_{1} & \partial x_{2} & \partial x_{p} \\ \partial f_{2} & \partial f_{2} & \partial f_{2} \\ (a) & (a) & \dots & (a) \\ \partial x_{1} & \partial x_{2} & \partial x_{p} \\ \vdots & \vdots & \ddots & \vdots \\ \partial f_{n} & \partial f_{n} & \partial f_{n} \\ (a) & (a) & \dots & (a) \\ \partial x_{1} & \partial x_{2} & \partial x_{p} \end{pmatrix} .$$
Do đó, ta có quen thuộc công thức
$$\frac{\partial h_{i}}{\partial x_{j}} (a) = \sum_{k=1}^{k=n}  \frac{\partial g_{i}}{\partial y_{k}} (b) \frac{\partial f_{k}}{\partial x_{j}} (a).$$
Cho trước hai được chuẩn (norm) các không gian afin $E$ và $F$ của hữu hạn số chiều, cho trước mở tập con $A$ của $E$, nếu hàm $f$: $A \to F$ là khả vi (differentiable) tại $a \in A$, thì của nó Ma trận Jacobi (Jacobian matrix) được xác định tốt (well-defined).  Một nên là warned rằng điều ngược lại là sai. Có các hàm sao cho tất cả các đạo hàm riêng tồn tại tại một số $a \in A$, nhưng vẫn chưa, hàm là không khả vi (differentiable) tại,
$$\mathbb{R}^{2} \mathbb{R}$$
Và không chẵn/ngay cả liên tục tại. Ví dụ, xét hàm $f$: $\to$, được định nghĩa sao cho f(0, $0) = 0$, và
$$f(x, y) = \frac{x^{2}y}{x^{4}+ y^{2}} if (x, y) \neq  (0, 0).$$
$$For any u \neq  0, letting u = \begin{pmatrix} h \\ k \end{pmatrix} , we have$$
$$\frac{f(0 + tu)f(0)}{t} -= \frac{h^{2}k}{t^{2}h^{4}+ k^{2}} ,$$

<!-- PAGE 1464 -->
Sao cho
$$h2$$
$$if k \neq  0$$
$$D_{u}f(0, 0) =$$
$$0^{k}if k = 0.$$
Do đó, $D_{u}f(0, 0)$ tồn tại với mọi $u \neq  0$. Mặt khác, nếu Df(0, $0)$ được tồn tại, nó sẽ là
$$\mathbb{R}^{2} \mathbb{R}$$
Ánh xạ tuyến tính (linear map) Df(0, $0): \to$ được biểu diễn bởi ma trận hàng $(\alpha  \beta$), và ta sẽ có $D_{u}f(0, 0) =$ Df(0, 0)(u) $= \alpha h + \beta k$, nhưng tường minh công thức cho $D_{u}f(0, 0)$ là không tuyến tính. Như matter của sự kiện, hàm $f$ là không liên tục tại $(0, 0)$. Ví dụ, trên parabol $y = x^{2}$, f(x, $y) =_{2}^{1}$, và khi ta cách tiếp cận gốc trên điều này parabol, giới hạn $is_{2}^{1}$, khi thực ra, f(0, $0) = 0$. Tuy nhiên, có đủ các điều kiện trên các đạo hàm riêng cho Df() đến tồn tại, cụ thể là, tính liên tục của các đạo hàm riêng.
$$\longrightarrow  \longrightarrow$$
Nếu $f$ là khả vi (differentiable) trên $A$, thì $f$ định nghĩa hàm Df: $A \to$ L(E; $F$). Hóa ra là tính liên tục của các đạo hàm riêng trên $A$ là cần và đủ điều kiện cho Df đến tồn tại và là liên tục trên $A$. Nếu $f$: [, $b] \to \mathbb{R}$ là hàm mà là liên tục trên [, $b]$ và khả vi (differentiable) trên (, $b)$, thì tồn tại một $c$ với $< c < b$ sao cho
$$f(b) -f(a) = (b -a)f' (c).$$
Kết quả này là đã biết như có nghĩa giá trị định lý và là tổng quát hóa của Rolle’s định lý, mà tương ứng với trường hợp ở đâu f() $=$ f(b). Không may là, có nghĩa giá trị định lý không thỏa mãn cho nhận giá trị vectơ (vector-valued) các hàm. Ví dụ,
$$\mathbb{R}^{2}$$
Hàm $f$: $[0, 2\pi$ ] $\to$ cho trước bởi
$$f(t) = (\cos t, \sin t)$$
Là sao cho $f(2\pi$) -f(0) $= (0, 0)$, vẫn chưa đạo hàm của nó f' $(t) =$ (-sin $t$, cos $t)$ thực hiện không triệt tiêu trong $(0, 2\pi$). phù hợp tổng quát hóa của có nghĩa giá trị định lý đến nhận giá trị vectơ (vector-valued) các hàm là khả dĩ/có thể nếu ta xét bất đẳng thức (trên cận) thay vì của đẳng thức. Điều này suy rộng/tổng quát hóa phiên bản của có nghĩa giá trị định lý đóng quan trọng vai trò trong chứng minh của một vài major các kết quả của vi phân vi tích phân. Nếu $E$ là không gian afin (affine space) (trên $\mathbb{R}$ hoặc $\mathbb{C})$, cho trước bất kỳ hai các điểm, $b \in E$, đóng đoạn thẳng [, $b]$ là tập hợp tất cả các điểm $a + \lambda (b$ - $a)$, ở đâu $0 \le \lambda  \le 1, \lambda  \in \mathbb{R}$, và mở đoạn thẳng (, $b)$ là tập hợp tất cả các điểm $a + \lambda (b$ - $a)$, ở đâu $0 < \lambda  < 1, \lambda  \in \mathbb{R}$.

> **Mệnh đề 39.12.** Cho $E$ và $F$ là hai được chuẩn (norm) các không gian afin, cho $A$ là mở tập con của $E$, và cho $f$: $A \to F$ là hàm liên tục (continuous function) trên $A$. Cho trước bất kỳ $a \in A$ và bất kỳ $h \neq  0$ trong $\longrightarrow E$, nếu đóng đoạn thẳng [, $a + h]$ được chứa trong $A$, nếu $f$: $A \to F$ là khả vi (differentiable) tại mọi điểm của mở đoạn thẳng (, $a + h)$, và
$$\sup\|Df(x)\|\le M,$$
$$x\in (a,a+h)$$
