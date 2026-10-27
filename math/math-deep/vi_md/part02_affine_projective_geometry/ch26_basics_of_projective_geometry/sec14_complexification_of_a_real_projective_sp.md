# Phức hóa của Thực Không gian xạ ảnh (projective space)


<!-- PAGE 952 -->
$$c$$
$$d_{1}$$
$$d_{2}$$
$$d_{3}$$
$$d_{4}$$
$$\Delta$$
$$d_{1}'d_{2}'d_{3}'d_{4}'\Delta'$$
$$D_{1}D_{2}D_{3}D_{4}$$
$$Figure 26.39: A pencil of lines and its cross-ratio with intersecting lines.$$
$G = \psi^{-1} (0)$. Cho $a =$ P(F) $\cap \Delta$ và $b =$ P(G) $\cap \Delta$. Có một số các vectơ $u, v \in D$ sao cho $a =$ p(u) và $b =$ p(v), và vì $\phi$ và $\psi$ là độc lập tuyến tính (linearly independent), ta có $a \neq  b$, và ta có thể chọn $\phi$ và $\psi$ sao cho $\phi (v) = -1$ và $\psi (u) = 1$. Cũng, $(u, v)$ là cơ sở (basis) của $D$. Thì điểm $p(\alpha u + \beta v)$ trên $\Delta$ thuộc đến siêu phẳng (hyperplane) $H = p(\gamma \phi  + \delta \psi$) của chùm (pencil) $P$ khi và chỉ khi
$$(\gamma \phi  + \delta \psi )(\alpha u + \beta v) = 0,$$
Mà, vì $\phi (u) = 0, \psi (v) = 0, \phi (v) = -1$, và $\psi (u) = 1$, cho ta $\gamma \beta  = \delta \alpha$, mà là tương đương đến $[\alpha , \beta$ ] $= [\gamma , \delta$ ] trong $P(K^{2})$. Nhưng khi đó ánh xạ $h: P \to \Delta$ là phép xạ ảnh (projectivity). Đặt $d_{i} = \Delta \cap H_{i}$, vì theo Mệnh đề 26.20 phép xạ ảnh (projectivity) của các đường thẳng bảo toàn tỉ số kép (cross-ratio), ta thu được $[d_{1}, d_{2}, d_{3}, d_{4}] = [H_{1}, H_{2}, H_{3}, H_{4}]$.

## 26.14 Phức hóa của Thực Không gian xạ ảnh (projective space)

Các khái niệm chẳng hạn như tính trực giao, các góc, và khoảng cách giữa các điểm là không xạ ảnh các khái niệm. Trong thứ tự để định nghĩa như vậy các khái niệm, một cần tích vô hướng (inner product) trên underlying không gian vectơ (vector space). Ta nói rằng như vậy các khái niệm thuộc đến Euclidean hình học. Tại thứ nhất glance, sự kiện rằng một số quan trọng Euclidean các khái niệm là không được phủ bởi xạ ảnh hình học dường như major drawback của xạ ảnh hình học. May mắn thay, geometers của nineteenth century (bao gồm cả Laguerre, Monge, Poncelet, Chasles, von Staudt, Cayley, và Klein) tìm thấy astute cách của recovering nhất định Euclidean các khái niệm chẳng hạn như các góc và tính trực giao (cũng các đường tròn) bởi phép nhúng (embedding) thực các không gian xạ ảnh vào phức các không gian xạ ảnh. Trong tiếp theo hai các mục ta sẽ cho ngắn gọn account của phương pháp này. Nhiều hơn/thêm chi tiết có thể được tìm thấy trong Berger $[11, 12]$, Pedoe $[141]$, Samuel $[148]$, Coxeter $[43, 44]$, Sidler $[167]$, Tisseron $[181]$, Lehmann và Bkouche $[119]$, và, của course, Thể tích II của Veblen và Young $[190]$.

<!-- PAGE 953 -->
Bước thứ nhất là đến embed thực không gian vectơ (vector space) $E$ vào phức không gian vectơ (vector space) $E_{C}$. quick nhưng somewhat bewildering cách đến thực hiện do đó là để định nghĩa phức hóa của $E$ như tích tenxơ (tensor product) $\mathbb{C} \otimes E$. nhiều hơn/thêm tangible cách là để định nghĩa sau đây cấu trúc.

> **Định nghĩa 26.13.** Cho trước thực không gian vectơ (vector space) $E$, cho $E_{C}$ là cấu trúc $E \times  E$ dưới phép cộng phép toán
$$(u_{1}, u_{2}) + (v_{1}, v_{2}) = (u_{1} + v_{1}, u_{2} + v_{2}),$$
Và cho phép nhân bởi phức vô hướng (scalar) $z = x +$ iy được định nghĩa sao cho
$$(x + iy) \cdot  (u, v) = (xu -yv, yu + xv).$$
Dễ dàng chứng minh được rằng cấu trúc $E_{C}$ là phức không gian vectơ (vector space). Nó là cũng immediate rằng
$$(0, v) = i(v, 0),$$
Và do đó, đồng nhất $E$ với không gian con của $E_{C}$ bao gồm của tất cả các vectơ của tạo thành $(u, 0)$, ta có thể viết
$$(u, v) = u + iv.$$
Cho trước vectơ $w = u +$ iv, của nó liên hợp $\overline{w}$ là vectơ $\overline{w} = u$ - iv. Thì liên hợp là ánh xạ từ $E_{C}$ đến chính nó rằng là phép đối hợp (involution). Nếu $(e_{1}, \dots  , e_{n})$ là bất kỳ cơ sở (basis) của $E$, thì $((e_{1}, 0), \dots  , (e_{n}, 0))$ là cơ sở (basis) của $E_{C}$. Ta gọi như vậy cơ sở (basis) thực cơ sở (basis). Cho trước ánh xạ tuyến tính (linear map) $f$: $E \to E$, ánh xạ $f$ có thể được được mở rộng đến ánh xạ tuyến tính (linear map) $f_{C}$: $E_{C} \to E_{C}$ được định nghĩa sao cho
$$f_{C}(u + iv) = f(u) + if(v).$$
$$We define the complexification of P(E) as P(E_{C} ). If \begin{pmatrix} \longrightarrow \\ E,E \\ (E_{C}b \end{pmatrix} is a real affine space, we$$
Định nghĩa complexified bổ sung xạ ảnh (projective completion) của như $P$) và ký hiệu nó bởi $E_{C}$. Thì
$$E is naturally embedded inE_{C}, and it is called \begin{pmatrix} \longrightarrow \\ E,E \\ theset \end{pmatrix} of real  points ofE_{C}. e$$
$e  e  e$ Nếu $E$ có số chiều $n+1$ và $(e_{1}, \dots  , e_{n+1})$ là cơ sở (basis) của $E$, cho trước bất kỳ thuần nhất đa thức $P(x_{1}, \dots  , x_{n+1})$ trên $\mathbb{C}$ của tổng bậc $m$, bởi vì $P$ là thuần nhất, ta kiểm chứng được ngay rằng
$$P(x_{1}, \dots  , x_{n+1}) = 0$$
Khi và chỉ khi
$$P(\lambda x_{1}, \dots  , \lambda x_{n+1}) = 0,$$
Với mọi $\lambda  \neq  0$. Do đó, ta có thể định nghĩa hypersurface $V (P)$ của phương trình $P(x_{1}, \dots  , x_{n+1}) = 0$ như tập con của $E_{C}$ bao gồm của tất cả các điểm của thuần nhất các tọa độ $(x_{1}, \dots  , x_{n+1})$ sao cho
$$e$$
$P(x_{1}, \dots  , x_{n+1}) = 0$. Ta nói rằng hypersurface $V (P)$ của phương trình $P(x_{1}, \dots  , x_{n+1}) = 0$ là thực bất cứ khi nào $P(x_{1}, \dots  , x_{n+1}) = 0$ suy ra rằng $P(\overline{x}_{1}\overline{, \dots  , x}_{n+1}) = 0$.
