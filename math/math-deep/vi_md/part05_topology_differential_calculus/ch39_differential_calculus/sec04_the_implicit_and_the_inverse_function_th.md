# Ẩn và Nghịch đảo Hàm Các định lý


<!-- PAGE 1465 -->
Với một số $M \ge 0$, thì
$$\|f(a + h) -f(a)\|\le M\|h\|.$$
$$\longrightarrow \longrightarrow$$
Như hệ quả, nếu $L: E \to F$ là liên tục ánh xạ tuyến tính (linear map), thì
$$\|f(a + h) -f(a) -L(h)\|\le M\|h\|,$$
Ở đâu $M = sup_{x\in(a,a+h)} \|Df(x)$ - $L\|$. ở trên mệnh đề đôi khi được gọi là “có nghĩa giá trị định lý.” Mệnh đề 39.12 có thể được được sử dụng để chỉ ra sau đây quan trọng kết quả.

> **Định lý 39.13.** Cho trước hai được chuẩn (norm) các không gian afin $E$ và $F$, ở đâu $E$ là của hữu hạn số chiều $n$, và ở đâu $(a_{0}, (u_{1}, \dots  , u_{n}))$ là hệ quy chiếu (frame) của $E$, cho trước bất kỳ mở tập con $A$ của $E$, cho trước bất kỳ
$$\longrightarrow  \longrightarrow$$
Hàm $f$: $A \to F$, đạo hàm Df: $A \to$ L(E; $F$) được định nghĩa và liên tục trên $A$ khi và chỉ khi
$$every partial derivative \partial_{j} f (or \frac{\partial f}{\partial x_{j}} ) is defined and continuous on A, for all j, 1 \le j \le n.$$
Như hệ quả, nếu $F$ là của hữu hạn số chiều $m$, và $(b_{0}, (v_{1}, \dots  , v_{m}))$ là hệ quy chiếu (frame) của $F$,
$$\longrightarrow  \longrightarrow$$
Đạo hàm Df: $A \to$ L(E; $F$) được định nghĩa và liên tục trên $A$ khi và chỉ khi mọi đạo hàm riêng (partial derivative)
$$\partial_{j} f_{i} (or \frac{\partial f_{i}}{\partial x_{j}} ) is defined and continuous on A, for all i, j, 1 \le i \le m, 1 \le j \le n.$$
Định lý 39.13 cho cần và đủ điều kiện cho sự tồn tại và tính liên tục của đạo hàm của hàm trên tập mở (open set). Nó nên được lưu ý rằng nhiều hơn/thêm tổng quát phiên bản của Định lý 39.13 nghiệm đúng, giả sử rằng $E = (E_{1}, a_{1}) \oplus \cdots  \oplus (E_{n}, a_{n})$, hoặc $E = E_{1} \times  \cdots  \times  E_{n}$, và bằng cách sử dụng nhiều hơn/thêm tổng quát các đạo hàm riêng $D_{j}f$ đã giới thiệu trước Mệnh đề 39.11.

> **Định nghĩa 39.9.** Cho trước hai được chuẩn (norm) các không gian afin $E$ và $F$, và mở tập con $A$ của $E$, ta nói rằng hàm $f$: $A \to F$ là của lớp $C^{0}$ trên $A$ hoặc $C^{0}-function$ trên $A$ nếu $f$ là liên tục trên $A$. Ta nói rằng $f$: $A \to F$ là của lớp $C^{1}$ trên $A$ hoặc $C^{1}-function$ trên $A$ nếu Df tồn tại và là liên tục trên $A$. Vì sự tồn tại của đạo hàm trên tập mở (open set) suy ra tính liên tục, $C^{1}-function$ là của course $C^{0}-function$. Định lý 39.13 cho cần và đủ điều kiện cho hàm $f$ là $C^{1}-function$ (khi $E$ là của hữu hạn số chiều). Nó là dễ để chỉ ra rằng hợp thành của $C^{1}-functions$ (trên thích hợp các tập mở) là $C^{1}-function$.

## 39.4 Ẩn và Nghịch đảo Hàm Các định lý

Cho trước ba được chuẩn (norm) các không gian afin $E, F$, và $G$, cho trước hàm $f$: $E \times  F \to G$, cho trước bất kỳ $c \in G$, nó có thể xảy ra rằng phương trình
$$f(x, y) = c$$

<!-- PAGE 1466 -->
Có tính chất rằng, với một số các tập mở $A \subseteq E$, và $B \subseteq F$, có một hàm $g: A \to B$, sao cho
$$f(x, g(x)) = c,$$
Với mọi $x \in A$. Như vậy tình huống là thường rất rare, nhưng nếu một số nghiệm (, $b) \in E \times  F$ sao cho f(, $b) = c$ là đã biết, dưới nhất định các điều kiện, với một số nhỏ các tập mở $A \subseteq E$ chứa và $B \subseteq F$ chứa $b$, sự tồn tại của duy nhất $g: A \to B$, sao cho
$$f(x, g(x)) = c,$$
Với mọi $x \in A$, có thể được được hiển thị. Dưới nhất định các điều kiện, nó có thể cũng được hiển thị rằng $g$ là liên tục, và khả vi (differentiable). Như vậy định lý, đã biết như định lý hàm ẩn (implicit function theorem), có thể được được chứng minh.
$$\mathbb{R}^{2}\mathbb{R}\mathbb{R}^{2} \mathbb{R} \sim \mathbb{R}^{3} \mathbb{R}^{2} \mathbb{R}\mathbb{R}$$

> **Ví dụ 39.10.** Cho $E = , F = G = , \Omega = \times = , f$: $\times  \to$ cho trước bởi
$$f((x_{1}, x_{2}), x_{3}) = x_{1}^{2} + x_{2}^{2} + x_{3}^{2} -1,$$
$$\mathbb{R}^{2}$$
$$a = \begin{pmatrix} \sqrt & \sqrt & \sqrt & \sqrt \\ \overline{3}/(2 & \overline{2)}, & \overline{3}/(2 & \overline{2)} \end{pmatrix} , b = 1/2, and c = 0. The set of vectors (x_{1}, x_{2}, x_{3}) \in such$$
Rằng
$$f((x_{1}, x_{2}), x_{3}) = x_{1}^{2} + x_{2}^{2} + x_{3}^{2} -1 = 0$$
$$\mathbb{R}^{3} -$$
Là unit mặt cầu trong. vectơ (, $b)$ thuộc đến unit mặt cầu vì $\|a\|_{2}^{2} + b^{2} 1 = 0$.
$$\mathbb{R}^{2} \mathbb{R}$$
Hàm $g: \to$ cho trước bởi
$$q$$
$$g(x_{1}, x_{2}) =1 -x_{1}^{2} -x_{2}^{2}$$
Thỏa mãn phương trình
$$f(x_{1}, x_{2}, g(x_{1}, x_{2})) = 0$$
$$\mathbb{R}^{2}$$
Tất cả cho $(x_{1}, x_{2})$ trong mở đĩa ${(x_{1}, x_{2}) \in$ | $x_{1}^{2} + x_{2}^{2} < 1}$, và g() $= b$. Nhận thấy rằng nếu ta đã có được chọn $b = -1/2$, thì ta sẽ cần đến xét hàm
$$q$$
$$g(x_{1}, x_{2}) = -1 -x_{1}^{2} -x_{2}^{2}.$$
Ta bây giờ phát biểu rất tổng quát phiên bản của định lý hàm ẩn (implicit function theorem). chứng minh của định lý này là fairly liên quan và sử dụng fixed-point định lý cho contracting các ánh xạ trong đầy đủ các không gian mêtric; nó là cho trước trong Schwartz $[157]$. Khác các chứng minh có thể được tìm thấy trong Lang $[115]$ và Cartan $[34]$.

> **Định lý 39.14.** Cho $E, F$, và $G$, được chuẩn (norm) các không gian afin, cho $\Omega$ là mở tập con của $E \times  F$, cho $f$: $\Omega \to G$ là hàm được định nghĩa trên $\Omega$, cho (, $b) \in \Omega$, cho $c \in G$, và giả sử rằng f(, $b) = c$. Nếu sau đây các giả định đúng
$(1)$ hàm $f$: $\Omega \to G$ là liên tục trên $\Omega$;
$(2) F$ là đầy đủ được chuẩn (norm) không gian afin (affine space) (và do đó là $G)$;

<!-- PAGE 1467 -->
$\longrightarrow  \longrightarrow$
$$(3) \frac{\partial f}{\partial y} (x, y) exists for every (x, y) \in \Omega , and \frac{\partial f}{\partial y} : \Omega \to L(F ;G) is continuous;$$
$\longrightarrow  \longrightarrow \longrightarrow  \longrightarrow$
$$(4) \frac{\partial f}{\partial y} (a, b) is a bijection of \mathcal{L}(F ;G), and \begin{pmatrix} \partial f \\ (a, b \\ \partial y \end{pmatrix} )^{-1}\in L(G;F );$$
Thì các tính chất sau đây đúng:
() Ở đó tồn tại một số mở tập con $A \subseteq E$ chứa và một số mở tập con $B \subseteq F$ chứa $b$, sao cho $A \times  B \subseteq \Omega$, và với mọi $x \in A$, phương trình f(x, $y) = c$ có đơn lẻ nghiệm $y =$ g(x), và do đó, tồn tại duy nhất một hàm $g: A \to B$ sao cho f(x, g(x)) $= c$, với mọi $x \in A$;
$(b)$ hàm $g: A \to B$ là liên tục. Nếu ta cũng giả sử rằng
$(5)$ đạo hàm Df(, $b)$ tồn tại; thì
$(c)$ đạo hàm Dg() tồn tại, và
$$Dg(a) = - \begin{pmatrix} \partial f \\ (a, b \\ \partial y \end{pmatrix} )^{-1}\circ \frac{\partial f}{\partial x} (a, b);$$
Và nếu ngoài ra $\longrightarrow  \longrightarrow$
$$(6) \frac{\partial f}{\partial x} : \Omega \to L(E ;G) is also continuous (and thus, in view of (3), f is C^{1}on \Omega );$$
Thì
$$\longrightarrow  \longrightarrow$$
$(d)$ đạo hàm Dg: $A \to$ L(E; $F$) là liên tục, và
$$Dg(x) = - \begin{pmatrix} \partial f \\ (x, g(x \\ \partial y \end{pmatrix} ))^{-1}\circ \frac{\partial f}{\partial x} (x, g(x)),$$
Với mọi $x \in A$.

> **Ví dụ 39.11.** Đi quay lại đến Ví dụ 39.10, viết $x = (x_{1}, x_{2})$ và $y = x_{3}$, sao cho các đạo hàm riêng $\partial f/\partial x$ và $\partial f/\partial y$ là cho trước theo của chúng Jacobian các ma trận bởi
$$\frac{\partial f}{\partial x} (x, y) = \begin{pmatrix} 2x_{1} & 2x_{2} \end{pmatrix}$$
$$\frac{\partial f}{\partial y} (x, y) = 2x_{3}.$$

<!-- PAGE 1468 -->
$$-$$
Nếu $0 <$ |b| $\le 1$ và $\|a\|_{2}^{2} + b^{2} 1 = 0$, thì Các điều kiện $(3)$ và $(4)$ được thỏa mãn. Các điều kiện
$(1)$ và $(2)$ hiển nhiên đúng. Vì $df_{(a,b)}$ được cho bởi của nó Ma trận Jacobi (Jacobian matrix) như
$$df_{(a,b)} = \begin{pmatrix} 2a_{1} & 2a_{2} & 2b \end{pmatrix} ,$$
Điều kiện $(5)$ nghiệm đúng, và rõ ràng, Điều kiện $(6)$ cũng nghiệm đúng.
$$\mathbb{R}^{2}$$
Định lý 39.14 suy ra rằng tồn tại một mở tập con $A$ của chứa, một số mở tập con $B$ của $\mathbb{R}$ chứa $b$, và duy nhất hàm $g: A \to B$ sao cho
$$f(x, g(x)) = 0$$
Với mọi $x \in A$. Thực ra, ta có thể chọn $A$ là mở unit đĩa trong $\mathbb{R}, B = (0, 2)$, và nếu $0 < b \le 1$, thì
$$q$$
$$g(x_{1}, x_{2}) =1 -x_{1}^{2} -x_{2}^{2},$$
Khác nếu $-1 \le b < 0$, thì
$$q$$
$$g(x_{1}, x_{2}) = -1 -x_{1}^{2} -x_{2}^{2}.$$
Giả sử $0 < b \le 1$, Ta có
$$\frac{\partial f}{\partial x} (x, g(x)) = (2x_{1} 2x_{2}),$$
Và
$$-1$$
$$\begin{pmatrix} \partial f \\ (x, g(x)) \\ \partial y \end{pmatrix} = \frac{1}{2p1 -x_{1}^{2}-x_{2}^{2}} ,$$
Do đó theo định lý,
$$dg_{x} = - \frac{1}{p1 -x_{1}^{2}-x_{2}^{2}} (x_{1} x_{2}),$$
Mà matches đạo hàm của $g$ được tính một cách trực tiếp. Nhận thấy rằng các hàm $(x_{1}, x_{2}) \mapsto p\overline{1}\overline{-} \overline{x}_{1}^{2} \overline{-} \overline{x}_{2}^{2}$ và $(x_{1}, x_{2}) \mapsto -p\overline{1}\overline{-} \overline{x}_{1}^{2} \overline{-} \overline{x}_{2}^{2}$ là hai khả vi (differentiable) parametrizations của mặt cầu, nhưng hợp của của chúng các miền giá trị (range) thực hiện không phủ toàn bộ mặt cầu. Vì $b \neq  0$, không có cái nào của các điểm trên unit đường tròn trong $(x_{1}, x_{2})-plane$ được phủ. Của ta hàm $f$ các quan điểm $b$ như lying trên $x_{3}-axis$. Trong thứ tự đến phủ toàn bộ mặt cầu
$$using this method, we need four more maps, which correspond to b lyingp \frac{onthex_{1}-axis}{1 -x_{2}^{2}-x_{3}^{2}} or$$
$$on the x_{2} axis. \frac{Thenwe}{1 -x_{1}^{2}-x_{3}^{2}.} get the additional (implicit) maps (x_{2}, x_{3}) \mapsto \pm   and$$
$(x_{1}, x_{3}) \mapsto \pm p$ định lý hàm ẩn (implicit function theorem) đóng quan trọng vai trò trong vi tích phân của variations. Ta bây giờ xét một cái khác rất quan trọng khái niệm, rằng của (địa phương) vi phôi (diffeomorphism).

<!-- PAGE 1469 -->

> **Định nghĩa 39.10.** Cho trước hai các không gian tôpô $E$ và $F$, và mở tập con $A$ của $E$, ta nói rằng hàm $f$: $A \to F$ là địa phương phép đồng phôi (homeomorphism) từ $A$ đến $F$ nếu với mọi $a \in A$, có một tập mở (open set) $U \subseteq A$ chứa và tập mở (open set) $V$ chứa f() sao cho $f$ là phép đồng phôi (homeomorphism) từ $U$ đến $V =$ f(U). Nếu $B$ là mở tập con của $F$, ta nói rằng $f$: $A \to F$ là (toàn cục) phép đồng phôi (homeomorphism) từ $A$ đến $B$ nếu $f$ là phép đồng phôi (homeomorphism) từ $A$ đến $B =$ f(). Nếu $E$ và $F$ được chuẩn (norm) các không gian afin, ta nói rằng $f$: $A \to F$ là địa phương vi phôi (diffeomorphism) từ $A$ đến $F$ nếu với mọi $a \in A$, có một tập mở (open set) $U \subseteq A$ chứa và tập mở (open set) $V$ chứa f() sao cho $f$ là song ánh từ $U$ đến $V , f$ là $C^{1}-function$ trên $U$, và $f^{-1}$ là $C^{1}-function$ trên $V =$ f(U). Ta nói rằng $f$: $A \to F$ là (toàn cục) vi phôi (diffeomorphism) từ $A$ đến $B$ nếu $f$ là phép đồng phôi (homeomorphism) từ $A$ đến $B =$ f(), $f$ là $C^{1}-function$ trên $A$, và $f^{-1}$ là $C^{1}-function$ trên $B$. Lưu ý rằng địa phương vi phôi (diffeomorphism) là địa phương phép đồng phôi (homeomorphism). Cũng, hệ quả là của Mệnh đề 39.8, nếu $f$ là vi phôi (diffeomorphism) trên $A$, thì Df() là tuyến tính đẳng cấu với mọi $a \in A$. sau đây định lý có thể được được hiển thị. Thực ra, có một fairly đơn giản chứng minh bằng cách sử dụng

> **Định lý 39.14.**

> **Định lý 39.15.** (Định lý hàm ngược (inverse function theorem)) Cho $E$ và $F$ là đầy đủ được chuẩn (norm) các không gian afin, cho $A$ là mở tập con của $E$, và cho $f$: $A \to F$ là $C^{1}-function$ trên $A$. Các tính chất sau đây đúng:
$(1)$ Với mọi $a \in A$, nếu Df() là tuyến tính đẳng cấu (mà có nghĩa là cả hai Df() và $(Df(a))^{-1}$ là tuyến tính và $continuous),^{2}$ thì ở đó tồn tại một số mở tập con $U \subseteq A$ chứa, và một số mở tập con $V$ của $F$ chứa f(), sao cho $f$ là vi phôi (diffeomorphism) từ $U$ đến $V =$ f(U). Hơn nữa,
$$Df^{-1} (f(a)) = (Df(a))^{-1}.$$
Với mọi lân cận (neighborhood) $N$ của, ảnh (ảnh (image)) của nó f(N) là lân cận (neighborhood) của f(), và với mọi hình cầu mở (open ball) $U \subseteq A$ của tâm, ảnh (ảnh (image)) của nó f(U) chứa một số hình cầu mở (open ball) của tâm f().
$(2)$ Nếu Df() là khả nghịch với mọi $a \in A$, thì $B =$ f() là mở tập con của $F$, và $f$ là địa phương vi phôi (diffeomorphism) từ $A$ đến $B$. Hơn nữa, nếu $f$ là đơn ánh (injective), thì $f$ là vi phôi (diffeomorphism) từ $A$ đến $B$. Các chứng minh của định lý hàm ngược (inverse function theorem) có thể được tìm thấy trong Schwartz $[157]$, Lang $[115]$, Abraham và Marsden $[1]$, và Cartan $[34]$. ý tưởng của Schwartz’s chứng minh là rằng nếu ta định nghĩa hàm $f_{1}$: $F \times  \Omega \to F$ bởi
$$f_{1}(y, z) = f(z) -y,$$
Thì nghịch đảo $g = f^{-1}$ của $f$ là ẩn nghiệm của phương trình $f_{1}(y, z) = 0$, vì
$$that the roles of E and F are switched, but this is$$
$$\frac{f_{1}(y, g(y))=f(g(y)) -y=0.Observe}{Actually,sinceEandFareBanach} 2       spaces, by the Open Mapping Theorem, it is sufficient to assume$$
Rằng Df() là liên tục và song ánh (bijective); xem Lang $[115]$.

<!-- PAGE 1470 -->
Không bài toán vì $F$ là đầy đủ. chứng minh bao gồm trong kiểm tra rằng các điều kiện của Định lý 39.14 áp dụng. Phần $(1)$ của Định lý 39.15 là thường referred đến như “(địa phương) định lý hàm ngược (inverse function theorem).” Nó đóng quan trọng vai trò trong study của các đa tạp và (thông thường) vi phân các phương trình. Nếu $E$ và $F$ là cả hai của hữu hạn số chiều, và một số các hệ quy chiếu có đã được được chọn, tính khả nghịch của Df() là tương đương đến sự kiện rằng Jacobian định thức (determinant) det(J(f)()) là khác không. trường hợp ở đâu Df() là chỉ đơn ánh (injective) hoặc chỉ toàn ánh (surjective) là cũng quan trọng cho định nghĩa các đa tạp, bằng cách sử dụng ẩn các định nghĩa.

> **Định nghĩa 39.11.** Cho $E$ và $F$ được chuẩn (norm) các không gian afin, ở đâu $E$ và $F$ là của hữu hạn số chiều (hoặc cả hai $E$ và $F$ là đầy đủ), và cho $A$ là mở tập con của $E$. Với mọi $a \in A$, $C^{1}-function f$: $A \to F$ là phép dìm (immersion) tại nếu Df() là đơn ánh (injective). $C^{1}-function f$: $A \to F$ là phép ngập (submersion) tại nếu Df() là toàn ánh (surjective). $C^{1}-function f$: $A \to F$ là phép dìm (immersion) trên $A$ (resp. phép ngập (submersion) trên $A)$ nếu Df() là đơn ánh (injective) (resp. toàn ánh (surjective)) với mọi $a \in A$. Khi $E$ và $F$ là hữu hạn dimensional với dim(E) $= n$ và dim(F) $= m$, nếu $m \ge n$, thì $f$ là phép dìm (immersion) khi và chỉ khi Ma trận Jacobi (Jacobian matrix), J(f)(), có đầy đủ hạng (rank) $n$ với mọi $a \in E$ và nếu $n \ge m$, thì $f$ là phép ngập (submersion) khi và chỉ khi Ma trận Jacobi (Jacobian matrix), J(f)(), có đầy đủ hạng (rank) $m$ với mọi $a \in E$.
$$\mathbb{R}\mathbb{R}^{2}$$

> **Ví dụ 39.12.** Ví dụ, $f$: $\to$ được định nghĩa bởi f(t) $=$ (cos(t), sin(t)) là phép dìm (immersion)
$$\mathbb{R}\mathbb{R}^{2}$$
$$since J(f)(t) = \begin{pmatrix} -\sin(t) \\ \cos(t) \end{pmatrix} has \mathrm{rank} 1 for all t. On the other hand, f : \to defined by$$
$$f(t) = (t^{2}, t^{2}) is not an immersion since J(f)(t) = \begin{pmatrix} 2t \\ 2t \end{pmatrix} vanishes at t = 0. See Figure 39.6.$$
$$\mathbb{R}^{2} \mathbb{R}$$
Ví dụ của phép ngập (submersion) được cho bởi phép chiếu ánh xạ $f$: $\to$, ở đâu f(x, $y) = x$,
$$since J(f)(x, y) = \begin{pmatrix} 1 & 0 \end{pmatrix} .$$
Sau đây các kết quả có thể được được hiển thị.
$$\mathbb{R}^{n}\mathbb{R}^{m}$$

> **Mệnh đề 39.16.** Cho $A$ là mở tập con của, và cho $f$: $A \to$ là hàm.
$$\mathbb{R}^{m}$$
Với mọi $a \in A, f$: $A \to$ là phép ngập (submersion) tại khi và chỉ khi tồn tại một mở tập con $U$ của $A$ chứa, mở tập con $W \subseteq \mathbb{R}^{n-m}$, và vi phôi (diffeomorphism) $\phi$: $U \to$ f(U) $\times  W$, sao cho,
$$f = \pi_{1}  \circ \phi ,$$
Ở đâu $\pi_{1}$: f(U) $\times  W \to$ f(U) là thứ nhất phép chiếu. Tương đương,
$$(f \circ \phi^{-1} )(y_{1}, \dots  , y_{m}, \dots  , y_{n}) = (y_{1}, \dots  , y_{m}).$$
$$\phi$$
$$U \subseteq Af(U) \times  W$$
$$N\overline{N}$$
$$\overline{N} N$$
$$NN$$
$$NN\pi$$
$$NN1$$
$$fN&$$
$$f(U) \subseteq \mathbb{R}^{m}$$

<!-- PAGE 1471 -->
$$(i.)$$
$$(ii.)$$
$$\mathbb{R}\mathbb{R}^{2}$$

![Figure 39.6](../../assets/ch39/fig_39_6.png)

**Hình 39.6:** Hình $(i.)$ là phép dìm (immersion) của vào cho trước bởi f(t) $=$ (cos(t), sin(t)). Hình (ii.), parametric đường cong f(t) $= (t^{2}, t^{2})$, là không phép dìm (immersion) vì tiếp tuyến triệt tiêu tại gốc. Futhermore, ảnh (image) của mọi mở tập con của $A$ dưới $f$ là mở tập con của $F$. (cùng
$$\mathbb{C}^{n}  \mathbb{C}^{m}$$
Kết quả nghiệm đúng cho và). Xem Hình 39.7.
$$\mathbb{R}^{n}\mathbb{R}^{m}$$

> **Mệnh đề 39.17.** Cho $A$ là mở tập con của, và cho $f$: $A \to$ là hàm.
$$\mathbb{R}^{m}$$
Với mọi $a \in A, f$: $A \to$ là phép dìm (immersion) tại khi và chỉ khi tồn tại một mở tập con $U$ của $A$ chứa, mở tập con $V$ chứa f() sao cho f(U) $\subseteq V$, mở tập con $W$ chứa $0$ sao cho $W \subseteq \mathbb{R}^{m-n}$, và vi phôi (diffeomorphism) $\phi$: $V \to U \times  W$, sao cho,
$$\phi  \circ f = in_{1},$$
Ở đâu $in_{1}$: $U \to U \times  W$ là đơn ánh ánh xạ sao cho $in_{1}(u) = (u, 0)$, hoặc tương đương,
$$(\phi  \circ f)(x_{1}, \dots  , x_{n}) = (x_{1}, \dots  , x_{n}, 0, \dots  , 0).$$
$$f$$
$$U \subseteq Af(U) \subseteq V$$
$$M\overline{M}$$
$$\overline{M} M$$
$$MM$$
$$MM\phi$$
$$MM$$
$$in1M&$$
$$U \times  W$$
$$\mathbb{C}^{n}  \mathbb{C}^{m}$$
(cùng kết quả nghiệm đúng cho và). Xem Hình 39.8.
