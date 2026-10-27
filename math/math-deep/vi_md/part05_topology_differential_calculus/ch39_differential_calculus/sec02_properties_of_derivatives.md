# Các tính chất của Các đạo hàm


<!-- PAGE 1450 -->
Ta có f($+ H)$ - f() - $(A^{\top}H + H^{\top}A) = (A + H)^{\top}(A + H)$ - I - $(A^{\top}A$ - I) - $A^{\top}H$ - $H^{\top}A$
$$= A^{\top}A + A^{\top}H + H^{\top}A + H^{\top}H -A^{\top}A -A^{\top}H -H^{\top}A$$
$$= H^{\top}H.$$
Suy ra rằng
$$- -$$
$$\epsilon (H) = \frac{f(A + H)f(A)(A^{\top}H + H^{\top}A)}{\|H\|} = \frac{H^{\top}H}{\|H\|} ,$$
Và vì chuẩn (chuẩn (norm)) của chúng ta là Chuẩn Frobenius (Frobenius norm),
$$\|\|$$
$$\|\epsilon (H)\|= \frac{H^{\top}H}{\|H\|} \le \frac{H^{\top}H}{\|H\|} =

$H^{\top}$

$= \|H\|,$$$ do đó
$$lim \epsilon (H) = 0,$$
$$H\mapsto 0$$
Và ta kết luận rằng
$$Df(A)(H) = A^{\top}H + H^{\top}A.$$

> **Định nghĩa 39.4.** Nếu đạo hàm $Df_{a}$ của hàm $f$: $A \to F$ tồn tại với mọi $a \in A$, ta
$$\longrightarrow  \longrightarrow$$
Thu được ánh xạ Df: $A \to$ L(E; $F$), được gọi là đạo hàm của $f$ trên $A$, cũng được ký hiệu bởi df. Ở đây $\longrightarrow  \longrightarrow  \longrightarrow  \longrightarrow \mathcal{L}(E$; $F$) ký hiệu không gian vectơ (vector space) của tất cả liên tục các ánh xạ từ $E$ đến $F$. Lưu ý rằng theo old khái niệm của đạo hàm của hàm $f$: $A \to \mathbb{R}$,
$$\mathbb{R}$$
Đạo hàm f' của $f$ là ánh xạ f': $A \to$ cho trước bởi $a \mapsto$ f'(). Nhưng “phải” khái niệm là rằng
$$\longrightarrow  \longrightarrow  \longrightarrow$$
Đạo hàm Df của $f$ là ánh xạ từ $A$ đến không gian $\mathcal{L}(E$; $F$) của liên tục các ánh xạ từ $E \longrightarrow$ đến $F$. Khi $E = F =\mathbb{R}$, có một accidental đẳng cấu giữa $\mathcal{L}(\mathbb{R};\mathbb{R})$ và $\mathbb{R}$. Ta bây giờ xét số của tiêu chuẩn các kết quả về các đạo hàm.

## 39.2 Các tính chất của Các đạo hàm


> **Mệnh đề 39.3.** Cho trước hai được chuẩn (norm) các không gian afin $E$ và $F$, nếu $f$: $E \to F$ là hằng số
$$\longrightarrow$$
Hàm, thì Df() $= 0$, với mọi $a \in E$. (ở đây, $0$ ký hiệu ánh xạ tuyến tính (linear map) từ $E$ đến $\longrightarrow \longrightarrow \longrightarrow F$ có giá trị là $0 \in F$ với mọi $u \in E$). Nếu $f$: $E \to F$ là liên tục ánh xạ afin (affine map), thì
$$\longrightarrow  \longrightarrow$$
Df() $= f$, với mọi $a \in E$, ở đâu $f$ ký hiệu ánh xạ tuyến tính (linear map) liên kết với $f$. Đặc biệt, nếu $E$ và $F$ là các không gian vectơ định chuẩn và $f$: $E \to F$ là liên tục ánh xạ tuyến tính (linear map), thì Df() $= f$ với mọi $a \in E$.

*Chứng minh.* Nếu $f$: $E \to F$ là hằng số hàm sao cho f(u) $= c$ với mọi $u \in E$ với một số cố định $c \in F$, thì
$$f(a + h) -f(a) = c -c = 0 = 0 \|h\|,$$

<!-- PAGE 1451 -->
$$\longrightarrow \longrightarrow$$
Do đó $\epsilon (h) = 0$ với mọi $h \in E$, và theo Định nghĩa, Df()(h) $= 0$ với mọi $a \in E$ và $h \in E$.
$$\longrightarrow$$
Nếu $f$: $E \to F$ là liên tục ánh xạ afin (affine map), vì $f$ là tuyến tính, ta có
$$\longrightarrow \longrightarrow  \longrightarrow  \longrightarrow \longrightarrow$$
F($+ h)$ - f() $= f (a + h) + c$ - ($f (a) + c) = f (a) + f (h) + c$ - ($f (a) + c)$
$$\longrightarrow  \longrightarrow$$
$$=f (h) =f (h) + 0 \|h\|,$$
$$\longrightarrow  \longrightarrow$$
Do đó $\epsilon (h) = 0$ với mọi $h \in E$, và theo Định nghĩa, Df() $= f$ với mọi $a \in E$.
$$\mathbb{R}^{n} \mathbb{R}$$

> **Ví dụ 39.3.** Xét hàm $f$: $\to M_{1,m}($) cho trước bởi
$$\phi (v) = (Cv -d)^{\top},v \in \mathbb{R}^{n},$$
Ở đâu $C$ là một ma trận cỡ $m \times  n$ và $d \in \mathbb{R}^{m}$. Vì phép chuyển vị là tuyến tính,
$$\phi (v) = (Cv)^{\top}-d^{\top}$$
Là ánh xạ afin (affine map) với tuyến tính phần cho trước bởi $v \mapsto (Cv)^{\top}$, do đó theo Mệnh đề 39.3,
$$D\phi_{v} (w) = (Cw)^{\top},v, w \in \mathbb{R}^{n}.$$

> **Mệnh đề 39.4.** Cho trước được chuẩn (norm) không gian afin (affine space) $E$ và không gian vectơ định chuẩn (normed vector space) $F$, với mọi hai các hàm $f, g: E \to F$, với mọi $a \in E$, nếu Df() và Dg() tồn tại, thì D(f $+g)(a)$ và $D(\lambda$ f)() tồn tại, và
$$D(f + g)(a) = Df(a) + Dg(a),$$
$$D(\lambda f)(a) = \lambda Df(a).$$

*Chứng minh.* Trực tiếp/dễ dàng. Cho trước hai các không gian vectơ định chuẩn $(E_{1}, \|\|_{1})$ và $(E_{2}, \|\|_{2})$, có ba tự nhiên và tương đương các chuẩn rằng có thể được được sử dụng để tạo $E_{1} \times  E_{2}$ vào không gian vectơ định chuẩn (normed vector space): $1. \|(u_{1}, u_{2})\|_{1} = \|u_{1}\|_{1} + \|u_{2}\|_{2}. 2. \|(u_{1}, u_{2})\|_{2} = (\|u_{1}\|_{1}^{2} + \|u_{2}\|_{2}^{2})^{1/2}. 3. \|(u_{1}, u_{2})\|_{\infty} = max(\|u_{1}\|_{1} , \|u_{2}\|_{2})$. Ta thường chọn thứ nhất chuẩn (norm). Nếu $E_{1}, E_{2}$, và $F$ là ba các không gian vectơ định chuẩn, nhắc lại rằng ánh xạ song tuyến tính (bilinear map) $f$: $E_{1} \times  E_{2} \to F$ là liên tục khi và chỉ khi tồn tại một hằng số $C \ge 0$ sao cho
$$\|f(u_{1}, u_{2})\|\le C \|u_{1}\|_{1} \|u_{2}\|_{2}for all u_{1} \in E_{1} and all u_{2} \in E_{2}.$$

> **Mệnh đề 39.5.** Cho trước ba các không gian vectơ định chuẩn $E_{1}, E_{2}$, và $F$, với mọi liên tục ánh xạ song tuyến tính (bilinear map) $f$: $E_{1} \times  E_{2} \to F$, với mọi (, $b) \in E_{1} \times  E_{2}$, Df(, $b)$ tồn tại, và với mọi $u \in E_{1}$ và $v \in E_{2}$,
$$Df(a, b)(u, v) = f(u, b) + f(a, v).$$

<!-- PAGE 1452 -->

*Chứng minh.* Vì $f$ là song tuyến tính, đơn giản phép tính suy ra rằng f((, $b) + (u, v))$ - f(, $b)$ - (f(u, $b) +$ f(, $v)) =$ f($+ u, b + v)$ - f(, $b)$ - f(u, $b)$ - f(, $v)$
$$= f(a + u, b) + f(a + u, v) -f(a, b) -f(u, b) -f(a, v)$$
$$= f(a, b) + f(u, b) + f(a, v) + f(u, v) -f(a, b) -f(u, b) -f(a, v)$$
$$= f(u, v).$$
Ta định nghĩa
$$f((a, b) + (u, v)) -f(a, b) -(f(u, b) + f(a, v))$$
$$\epsilon (u, v) =,$$
$$\|(u, v)\|_{1}$$
Và nhận thấy rằng tính liên tục của $f$ suy ra $\|f((a, b) + (u, v))$ - f(, $b)$ - (f(u, $b) +$ f(, $v))\| = \|f(u, v)\|$
$$\le C \|u\|_{1} \|v\|_{2} \le C (\|u\|_{1} + \|v\|_{2})^{2}.$$
Do đó
$$\|\|\|\|_{1} \|\|_{2}$$
$$\|\epsilon (u, v)\|= \frac{f(u, v)}{\|(u, v)\|_{1}} = \frac{f(u, v)}{\|(u, v)\|_{1}} \le \frac{C (u +v)^{2}}{\|u\|_{1} + \|v\|_{2}} = C (\|u\|_{1} + \|v\|_{2}) = C \|(u, v)\|_{1} ,$$
Mà trong turn suy ra
$$lim \epsilon (u, v) = 0.$$
$$(u,v)\mapsto (0,0)$$
$$\mathbb{R}^{n} \mathbb{R}^{m} \mathbb{R}$$

> **Ví dụ 39.4.** Xét hàm $f$: $\times \to$ cho trước bởi
$$f(v, \lambda ) = \lambda^{\top} Cv = v^{\top}C^{\top}\lambda ,v \in \mathbb{R}^{n}, \lambda  \in \mathbb{R}^{m},$$
Ở đâu $C$ là một ma trận cỡ $m \times  n$. Vì hàm $f$ là song tuyến tính, theo Mệnh đề 39.5, đạo hàm của nó được cho bởi
$$df_{(v,\lambda)}(w, \mu ) = f(w, \lambda ) + f(v, \mu ) = \lambda^{\top} Cw + \mu^{\top} Cv = (C^{\top}\lambda )^{\top}w + (Cv)^{\top}\mu ,$$
Với $w \in \mathbb{R}^{n}, \mu  \in \mathbb{R}^{m}$. Ta bây giờ phát biểu rất hữu ích dây chuyền/xích quy tắc.

> **Định lý 39.6.** Cho trước ba được chuẩn (norm) các không gian afin $E, F$, và $G$, cho $A$ là tập mở (open set) trong $E$, và cho $B$ tập mở (open set) trong $F$. Với mọi các hàm $f$: $A \to F$ và $g: B \to G$, sao cho f() $\subseteq B$, với mọi $a \in A$, nếu Df() tồn tại và Dg(f()) tồn tại, thì D(g $\circ$ f)() tồn tại, và
$$D(g \circ f)(a) = Dg(f(a)) \circ Df(a).$$

<!-- PAGE 1453 -->

*Chứng minh.* Vì $f$ là khả vi (differentiable) tại và $g$ là khả vi (differentiable) tại $b =$ f() với mọi $\eta$ sao cho $0 < \eta  < 1$ tồn tại một $\rho  > 0$ sao cho với mọi $s, t$, nếu $\|s\|\le \rho$ và $\|t\|\le \rho$ thì
$$f(a + s) = f(a) + Df_{a}(s) + \epsilon_{1} (s)$$
$$g(b + t) = g(b) + Dg_{b}(t) + \epsilon_{2} (t),$$
Với $\|\epsilon_{1} (s)\|\le \eta  \|s\|$ và $\|\epsilon_{2} (t)\|\le \eta  \|t\|$. Vì $Df_{a}$ và $Dg_{b}$ là liên tục, ta có
$$\|Df_{a}(s)\|\le \|Df_{a}\|\|s\|and\|Dg_{b}(t)\|\le \|Dg_{b}\|\|t\|,$$
Mà, vì $\|\epsilon_{1} (s)\|\le \eta  \|s\|$ và $\eta  < 1$, suy ra rằng $\|Df_{a}(s) + \epsilon_{1} (s)\|\le \|Df_{a}\|\|s\| + \|\epsilon_{1} (s)\|\le \|Df_{a}\|\|s\| + \eta  \|s\|\le (\|Df_{a}\| + 1) \|s\|$. Hệ quả là, nếu $\|s\| < \rho /(\|Df_{a}\| + 1)$, ta có
$$\|\epsilon_{2} (Df_{a}(s) + \epsilon_{1} (s))\|\le \eta (\|Df_{a}\|+ 1) \|s\|(*_{1})$$
Và
$$\|Dg_{b}(\epsilon_{1} (s))\|\le \|Dg_{b}\|\|\epsilon_{1} (s)\|\le \eta  \|Dg_{b}\|\|s\|.(*_{2})$$
Khi đó vì $b =$ f(), bằng cách sử dụng ở trên ta có
$$(g \circ f)(a + s) = g(f(a + s)) = g(b + Df_{a}(s) + \epsilon_{1} (s))$$
$$= g(b) + Dg_{b}(Df_{a}(s) + \epsilon_{1} (s)) + \epsilon_{2} (Df_{a}(s) + \epsilon_{1} (s))$$
$$= g(b) + (Dg_{b} \circ Df_{a})(s) + Dg_{b}(\epsilon_{1} (s)) + \epsilon_{2} (Df_{a}(s) + \epsilon_{1} (s)).$$
Bây giờ bởi $(*_{1})$ và $(*_{2})$ ta có
$$\|Dg_{b}(\epsilon_{1} (s)) + \epsilon_{2} (Df_{a}(s) + \epsilon_{1} (s))\|\le \|Dg_{b}(\epsilon_{1} (s))\|+ \|\epsilon_{2} (Df_{a}(s) + \epsilon_{1} (s))\|$$
$$\le \eta  \|Dg_{b}\|\|s\|+ \eta (\|Df_{a}\|+ 1) \|s\|$$
$$= \eta (\|Df_{a}\|+ \|Dg_{b}\|+ 1) \|s\|,$$
Do đó nếu ta viết $\epsilon_{3} (s) = Dg_{b}(\epsilon_{1} (s)) + \epsilon_{2} (Df_{a}(s) + \epsilon_{1} (s))$ ta được chứng minh rằng
$$(g \circ f)(a + s) = g(b) + (Dg_{b} \circ Df_{a})(s) + \epsilon_{3} (s)$$
Với $\epsilon_{3} (s) \le \eta (\|Df_{a}\|+ \|Dg_{b}\|+ 1) \|s\|$, mà chứng tỏ rằng $Dg_{b} \circ Df_{a}$ là đạo hàm của $g \circ f$ tại. Vì $Df_{a}$ và $Dg_{b}$ là liên tục, do đó là $Dg_{b} \circ Df_{a}$, mà chứng minh mệnh đề của chúng ta. Trong trường hợp đặc biệt khi $E = F = G =\mathbb{R}$ và $A$ và $B$ là mở các tập con của $\mathbb{R}$ sao cho f() $\subseteq B$, dây chuyền/xích quy tắc cho chúng ta quay lại tiêu chuẩn phiên bản của dây chuyền/xích quy tắc cho các hàm $f$: $A \to \mathbb{R}$ và $g: B \to \mathbb{R}$, cụ thể là với mọi $a \in A$,
$$(g \circ f)'(a) = g'(f(a)) \cdot  f' (a),$$

<!-- PAGE 1454 -->
Tích của thực các số g'(f()) và f' (). Điều này là bởi vì với mọi $a \in A$ và $b \in B, Df_{a}$ là ánh xạ tuyến tính (linear map) cho trước bởi $Df_{a}(u) =$ f' ()u và $Dg_{b}$ là ánh xạ tuyến tính (linear map) cho trước bởi $Dg_{b}(v) =$ g'(b)v, với $u, v \in \mathbb{R}$, do đó dây chuyền/xích quy tắc với $b =$ f() và $v =$ f' ()u nói rằng rằng
$$D(g \circ f)_{a}(u) = Dg_{f(a)}(Df_{a}(u)) = g'(f(a))(f' (a)u) = (g'(f(a))f' (a))u,$$
Do đó thật vậy
$$(g \circ f)'(a) = g'(f(a))f' (a).$$
Định lý 39.6 có nhiều thú vị các hệ quả. Ta mention hai các hệ quả.

> **Mệnh đề 39.7.** Cho trước ba được chuẩn (norm) các không gian afin $E, F$, và $G$, với mọi mở tập con $A$ trong $E$, với mọi $a \in A$, cho $f$: $A \to F$ sao cho Df() tồn tại, và cho $g: F \to G$ là liên tục ánh xạ afin (affine map). Thì, D(g $\circ$ f)() tồn tại, và
$$\longrightarrow$$
$$D(g \circ f)(a) =g \circ Df(a),$$
$\longrightarrow$ ở đâu $g$ là ánh xạ tuyến tính (linear map) liên kết với ánh xạ afin (affine map) $g$.

> **Mệnh đề 39.8.** Cho trước hai được chuẩn (norm) các không gian afin $E$ và $F$, cho $A$ là một số mở tập con trong $E$, cho $B$ là một số mở tập con trong $F$, cho $f$: $A \to B$ là song ánh từ $A$ đến $B$, và giả sử rằng Df tồn tại trên $A$ và rằng $Df^{-1}$ tồn tại trên $B$. Thì, với mọi $a \in A$,
$$Df^{-1} (f(a)) = (Df(a))^{-1}.$$
$$\longrightarrow  \longrightarrow$$
Mệnh đề 39.8 có đáng chú ý hệ quả rằng hai các không gian vectơ $E$ và $F$ có cùng số chiều. Nói cách khác, địa phương tính chất, sự tồn tại của song ánh $f$ giữa tập mở (open set) $A$ của $E$ và tập mở (open set) $B$ của $F$, sao cho $f$ là khả vi (differentiable) trên $A$ và
$$\longrightarrow  \longrightarrow$$
$f^{-1}$ là khả vi (differentiable) trên $B$, suy ra toàn cục tính chất, rằng hai các không gian vectơ $E$ và $F$ có cùng số chiều. Cho chúng ta mention hai nhiều hơn/thêm các quy tắc về các đạo hàm rằng được sử dụng tất cả time. Cho $\iota$: $GL(n,\mathbb{C}) \to M_{n}(\mathbb{C})$ là hàm (nghịch đảo) được định nghĩa trên khả nghịch $n\times n$ các ma trận bởi
$$\iota (A) = A^{-1}.$$
Nhận thấy rằng $GL(n,\mathbb{C})$ là thật vậy mở tập con của không gian vectơ định chuẩn (normed vector space) $M_{n}(\mathbb{C})$ của phức $n \times  n$ các ma trận, vì phần bù của nó là tập đóng (closed set) của các ma trận $A \in M_{n}(\mathbb{C})$ thỏa mãn det() $= 0$. Thì ta có
$$d\iota_{A} (H) = -A^{-1}HA^{-1},$$
Với mọi $A \in GL(n,\mathbb{C})$ và với mọi $H \in M_{n}(\mathbb{C})$.

<!-- PAGE 1455 -->
Để chứng minh trước đó đường thẳng nhận thấy rằng cho $H$ với một cách đủ nhỏ chuẩn (norm), ta có $\iota (A + H)$ - $\iota (A) + A^{-1}HA^{-1} = (A + H)^{-1}$ - $A^{-1} + A^{-1}HA^{-1}$
$$= (A + H)^{-1}[I -(A + H)A^{-1}+ (A + H)A^{-1}HA^{-1}]$$
$$= (A + H)^{-1}[I -I -HA^{-1}+ HA^{-1}+ HA^{-1}HA^{-1}]$$
$$= (A + H)^{-1}HA^{-1}HA^{-1}.$$
Hệ quả là, ta thu được
$$-$$
$$\epsilon (H) = \frac{\iota (A + H)\iota (A) + A^{-1}HA^{-1}}{\|H\|} = \frac{(A + H)^{-1}HA^{-1}HA^{-1}}{\|H\|} ,$$
Và vì
$$(A + H)^{-1}HA^{-1}HA^{-1}

$\le \|H\|^{2}$

$A^{-12}$



$(A + H)^{-1}$

,$$ it is clear that $lim_{H\mapsto0} \epsilon (H) = 0$, mà chứng tỏ rằng
$$d\iota_{A} (H) = -A^{-1}HA^{-1}.$$
Đặc biệt, nếu $A =$ I, thì $d\iota_{I} (H) = -H$. Tiếp theo, nếu $f$: $M_{n}(\mathbb{C}) \to M_{n}(\mathbb{C})$ và $g: M_{n}(\mathbb{C}) \to M_{n}(\mathbb{C})$ là khả vi (differentiable) ma trận các hàm, thì
$$d(fg)_{A}(B) = df_{A}(B)g(A) + f(A)dg_{A}(B),$$
Với mọi $A, B \in M_{n}(\mathbb{C})$. Điều này là đã biết như tích quy tắc. Khi $E$ là của hữu hạn số chiều $n$, với mọi hệ quy chiếu (frame) $(a_{0}, (u_{1}, \dots  , u_{n}))$ của $E$, ở đâu $(u_{1}, \dots  , u_{n})$
$$\longrightarrow$$
Là cơ sở (basis) của $E$, ta có thể định nghĩa directional các đạo hàm đối với các vectơ trong cơ sở (basis) $(u_{1}, \dots  , u_{n})$ (thực sự, ta có thể cũng thực hiện nó cho vô hạn hệ quy chiếu (frame)). Điều này cách, ta thu được định nghĩa của các đạo hàm riêng, như sau.

> **Định nghĩa 39.5.** Với mọi hai được chuẩn (norm) các không gian afin $E$ và $F$, nếu $E$ là của hữu hạn số chiều $n$, với mọi hệ quy chiếu (frame) $(a_{0}, (u_{1}, \dots  , u_{n}))$ cho $E$, với mọi $a \in E$, với mọi hàm $f$: $E \to F$, directional các đạo hàm $D_{uj}f(a)$ (nếu chúng tồn tại) được gọi là các đạo hàm riêng của $f$ đối với hệ quy chiếu (frame) $(a_{0}, (u_{1}, \dots  , u_{n}))$. đạo hàm riêng (partial derivative) $D_{uj}f(a)$ cũng được ký hiệu bởi
$$\partial_{j} f(a), or \frac{\partial f}{\partial x_{j}} (a).$$
$$The notation \frac{\partial f}{\partial x_{j}} (a) for a partial derivative, although customary and going back to$$
Leibniz, là “logical obscenity.” Thật vậy, biến $x_{j}$ một cách thực có không có gì đến thực hiện với hình thức định nghĩa. Điều này là chỉ một cái khác của các phần tử này các tình huống ở đâu tradition là chỉ cũng khó đến overthrow! Ta bây giờ xét tình huống ở đâu được chuẩn (norm) không gian afin (affine space) $F$ là hữu hạn tổng trực tiếp (direct sum) $F = (F_{1}, b_{1}) \oplus \cdots  \oplus (F_{m}, b_{m})$.

<!-- PAGE 1456 -->

> **Mệnh đề 39.9.** Cho trước được chuẩn (norm) các không gian afin $E$ và $F = (F_{1}, b_{1}) \oplus \cdots  \oplus (F_{m}, b_{m})$, cho trước bất kỳ mở tập con $A$ của $E$, với mọi $a \in A$, với mọi hàm $f$: $A \to F$, đặt $f = (f_{1}, \dots  , f_{m})$, Df() tồn tại khi và chỉ khi mọi $Df_{i}(a)$ tồn tại, và
$$Df(a) = in_{1} \circ Df_{1}(a) + \cdots  + in_{m} \circ Df_{m}(a).$$

*Chứng minh.* Nhận thấy rằng f($+ h)$ - f() $=$ (f($+ h)$ - $b)$ - (f() - $b)$, ở đâu $b = (b_{1}, \dots  , b_{m})$,
$$\longrightarrow$$
Và do đó, như far như dealing với các đạo hàm, Df() bằng $Df_{b}(a)$, ở đâu $f_{b}$: $E \to F$ được định nghĩa sao cho $f_{b}(x) =$ f(x)-b, với mọi $x \in E$. Do đó, ta có thể hoạt động/công trình với không gian vectơ (vector space) $\longrightarrow F$ thay vì của không gian afin (affine space) $F$. mệnh đề là thì đơn giản ứng dụng của Định lý 39.6. Trong trường hợp đặc biệt khi $F$ được chuẩn (norm) không gian afin (affine space) của hữu hạn số chiều $m$, với mọi hệ quy chiếu (frame)
$$\longrightarrow$$
$(b_{0}, (v_{1}, \dots  , v_{m}))$ của $F$, ở đâu $(v_{1}, \dots  , v_{m})$ là cơ sở (basis) của $F$, mọi điểm $x \in F$ có thể được được biểu diễn một cách duy nhất như
$$x = b_{0} + x_{1}v_{1} + \cdots  + x_{m}v_{m},$$
Ở đâu $(x_{1}, \dots  , x_{m}) \in K^{m}$, các tọa độ của $x$ trong hệ quy chiếu (frame) $(b_{0}, (v_{1}, \dots  , v_{m}))$ (ở đâu $K =\mathbb{R}$ hoặc $K = \mathbb{C})$. Do đó, đặt $F_{i}$ là tiêu chuẩn được chuẩn (norm) không gian afin (affine space) $K$ với của nó tự nhiên cấu trúc, ta lưu ý rằng $F$ là đẳng cấu đến tổng trực tiếp (direct sum) $F = (K, 0) \oplus \cdots  \oplus (K, 0)$. Thì, mọi hàm $f$: $E \to F$ được biểu diễn bởi $m$ các hàm $(f_{1}, \dots  , f_{m})$, ở đâu $f_{i}$: $E \to K$ (ở đâu $K =\mathbb{R}$ hoặc $K =\mathbb{C})$, và
$$f(x) = b_{0} + f_{1}(x)v_{1} + \cdots  + f_{m}(x)v_{m},$$
Với mọi $x \in E$. sau đây mệnh đề là immediate hệ quả của Mệnh đề 39.9.

> **Mệnh đề 39.10.** Với mọi hai được chuẩn (norm) các không gian afin $E$ và $F$, nếu $F$ là của hữu hạn số chiều
$$\longrightarrow$$
$m$, với mọi hệ quy chiếu (frame) $(b_{0}, (v_{1}, \dots  , v_{m}))$ của $F$, ở đâu $(v_{1}, \dots  , v_{m})$ là cơ sở (basis) của $F$, với mọi $a \in E$, hàm $f$: $E \to F$ là khả vi (differentiable) tại khi và chỉ khi mỗi $f_{i}$ là khả vi (differentiable) tại, và
$$Df(a)(u) = Df_{1}(a)(u)v_{1} + \cdots  + Df_{m}(a)(u)v_{m},$$
$$\longrightarrow$$
Với mọi $u \in E$. Ta bây giờ xét tình huống ở đâu $E$ là hữu hạn tổng trực tiếp (direct sum). Cho trước được chuẩn (norm) không gian afin (affine space) $E = (E_{1}, a_{1}) \oplus \cdots  \oplus (E_{n}, a_{n})$ và được chuẩn (norm) không gian afin (affine space) $F$, cho trước bất kỳ mở tập con $A$ của $E$, với mọi $c = (c_{1}, \dots  , c_{n}) \in A$, ta định nghĩa liên tục các hàm $i_{j}^{c}$: $E_{j} \to E$, sao cho
$$i_{j}^{c}(x) = (c_{1}, \dots  , c_{j-1}, x, c_{j+1}, \dots  , c_{n}).$$
Với mọi hàm $f$: $A \to F$, ta có các hàm $f \circ i_{j}^{c}$: $E_{j} \to F$, được định nghĩa trên $(i_{j}^{c})^{-1}(A)$, mà chứa $c_{j}$. Nếu D(f $\circ i_{j}^{c})(c_{j})$ tồn tại, ta gọi nó đạo hàm riêng (partial derivative) của $f$ w.r.t. của nó thứ $j$ lập luận,
$$\longrightarrow  \longrightarrow$$
Tại $c$. Ta cũng ký hiệu đạo hàm này bởi $D_{j}f(c)$. Lưu ý rằng $D_{j}f(c) \in L(E_{j}; F$).
