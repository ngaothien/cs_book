# Bậc hai và Bậc cao Các đạo hàm


<!-- PAGE 1474 -->
Chứng minh là thực sự khá đơn giản. Ta có $T_{a}(\Gamma$) $= a + T_{a}(\Gamma$), và vì $T_{a}(\Gamma$) là
$$\longrightarrow \times  \longrightarrow$$
Không gian con của $E F$, tập hợp $T_{a}(\Gamma$) là afin variety. Do đó, afin tiếp tuyến không gian tại điểm (, f()) là familar object, đường thẳng, mặt phẳng, etc.
$$\mathbb{R}^{2} \mathbb{R}$$
Như illustration, khi $E =$ và $F =$, afin tiếp tuyến mặt phẳng tại điểm (, $b, c)$ đến mặt của phương trình $z =$ f(x, $y)$, được định nghĩa bởi phương trình
$$z = c + \frac{\partial f}{\partial x} (a, b)(x -a) + \frac{\partial f}{\partial y} (a, b)(y -b).$$
Nếu $E = \mathbb{R}$ và $F = \mathbb{R}^{2}$, tiếp tuyến đường thẳng tại (, $b, c)$, đến đường cong của các phương trình $y =$ g(x), $z =$ h(x), được định nghĩa bởi các phương trình
$$y = b + Dg(a)(x -a),$$
$$z = c + Dh(a)(x -a).$$
Do đó, các đạo hàm và các đạo hàm riêng có mong muốn intended hình học interpretation như tiếp tuyến các không gian. Của course, trong thứ tự đến deal với điều này topic một cách thực sự/đúng đắn, ta một cách thực sẽ có đến đi deeper vào study của (vi phân) các đa tạp. Ta bây giờ ngắn gọn xét bậc hai và bậc cao các đạo hàm.

## 39.6 Bậc hai và Bậc cao Các đạo hàm

Cho trước hai được chuẩn (norm) các không gian afin $E$ và $F$, và một số mở tập con $A$ của $E$, nếu Df() được định nghĩa
$$\longrightarrow  \longrightarrow \longrightarrow  \longrightarrow$$
Với mọi $a \in A$, thì ta có ánh xạ Df: $A \to$ L(E; $F$). Vì $\mathcal{L}(E$; $F$) là không gian vectơ định chuẩn (normed vector space), nếu Df tồn tại trên mở tập con $U$ của $A$ chứa, ta có thể xét lấy đạo hàm của Df tại một số $a \in A$.

> **Định nghĩa 39.14.** Cho trước hàm $f$: $A \to F$ được định nghĩa trên một số mở tập con $A$ của $E$ sao cho Df() được định nghĩa với mọi $a \in A$, Nếu D(Df)() tồn tại với mọi $a \in A$, ta
$$\longrightarrow \longrightarrow  \longrightarrow$$
Thu được ánh xạ $D^{2}f$: $A \to$ L(E $;\mathcal{L}(E$; $F$)) được gọi là đạo hàm thứ hai của $f$ trên $A$, ở đâu $D^{2}f(a) =$ D(Df)(), với mọi $a \in A$. Như trong trường hợp của đạo hàm thứ nhất $Df_{a}$ ở đâu $Df_{a}(u) = D_{u}f(a)$, ở đâu $D_{u}f(a)$ là đạo hàm theo hướng (directional derivative) của $f$ tại trong hướng $u$, nó sẽ là hữu ích đến biểu diễn $D^{2}f(a)(u)(v)$ theo hai directional các đạo hàm. Điều này có thể thật vậy được thực hiện. Nếu $D^{2}f(a)$ tồn tại, thì cho
$$\longrightarrow$$
Mọi $u \in E$,
$$\longrightarrow  \longrightarrow$$
$$D^{2}f(a)(u) = D(Df)(a)(u) = D_{u}(Df)(a) \in L(E ;F ).$$
Ta có kết quả sau kết quả.

> **Mệnh đề 39.19.** Nếu $D^{2}f(a)$ tồn tại, thì $D_{u}(D_{v}f)(a)$ tồn tại và
$$\longrightarrow$$
$$D^{2}f(a)(u)(v) = D_{u}(D_{v}f)(a),for all u, v \in E .$$

<!-- PAGE 1475 -->
$$\longrightarrow  \longrightarrow  \times  \longrightarrow  \longrightarrow$$

*Chứng minh.* Nhắc lại từ Mệnh đề 37.61, rằng ánh xạ app từ $\mathcal{L}(E$; $F$) $E$ đến $F$, được định nghĩa
$$\longrightarrow  \longrightarrow \longrightarrow$$
Sao cho với mọi $L \in$ L(E; $F$), với mọi $v \in E$,
$$app(L, v) = L(v),$$
$$\longrightarrow$$
Là liên tục ánh xạ song tuyến tính (bilinear map). Do đó, đặc biệt, cho trước cố định $v \in E$, ánh xạ tuyến tính (linear map)
$$\longrightarrow  \longrightarrow \longrightarrow$$
$app_{v}$: $\mathcal{L}(E$; $F$) $\to F$, được định nghĩa sao cho $app_{v}(L) =$ L(v), là ánh xạ liên tục (continuous map). Cũng nhắc lại từ Mệnh đề 39.7, rằng nếu $h: A \to G$ là hàm sao cho Dh() exits, và $k: G \to H$ là liên tục ánh xạ tuyến tính (linear map), thì, D(k $\circ$ h)() tồn tại, và
$$k(Dh(a)(u)) = D(k \circ h)(a)(u),$$
Rằng là,
$$k(D_{u}h(a)) = D_{u}(k \circ h)(a),$$
Áp dụng các phần tử này hai các sự kiện đến $h =$ Df, và đến $k = app_{v}$, ta có
$$D_{u}(Df)(a)(v) = D_{u}(app_{v} \circ Df)(a).$$
Nhưng $(app_{v} \circ$ Df)(x) $=$ Df(x)(v) $= D_{v}f(x)$, với mọi $x \in A$, nghĩa là, $app_{v} \circ$ Df $= D_{v}f$ trên $A$. Do đó, ta có
$$D_{u}(Df)(a)(v) = D_{u}(D_{v}f)(a),$$
Và vì $D^{2}f(a)(u) = D_{u}(Df)(a)$, ta thu được
$$D^{2}f(a)(u)(v) = D_{u}(D_{v}f)(a).$$
Do đó, khi $D^{2}f(a)$ tồn tại, $D_{u}(D_{v}f)(a)$ tồn tại, và
$$D^{2}f(a)(u)(v) = D_{u}(D_{v}f)(a),$$
$$\longrightarrow$$
Với mọi $u, v \in E$.

> **Định nghĩa 39.15.** Ta ký hiệu $D_{u}(D_{v}f)(a)$ bởi $D_{u,v}^{2}f(a)$ (hoặc $D_{u}D_{v}f(a))$.
$$\longrightarrow  \longrightarrow  \longrightarrow \longrightarrow \longrightarrow  \longrightarrow$$
Nhắc lại từ Mệnh đề 37.60, rằng ánh xạ từ $\mathcal{L}_{2}(E , E$; $F$) đến $\mathcal{L}(E ;\mathcal{L}(E$; $F$)) de-
$$\longrightarrow  \longrightarrow  \longrightarrow$$
Fined sao cho $g \mapsto \phi$ khi và chỉ khi với mọi $g \in L_{2}(E , E$; $F$),
$$\phi (u)(v) = g(u, v),$$
$$\longrightarrow \longrightarrow  \longrightarrow$$
Là đẳng cấu của các không gian vectơ. Do đó, ta sẽ xét $D^{2}f(a) \in$ L(E $;\mathcal{L}(E$; $F$))
$$\longrightarrow  \longrightarrow  \longrightarrow$$
Như liên tục ánh xạ song tuyến tính (bilinear map) trong $\mathcal{L}_{2}(E , E$; $F$), và ta sẽ viết $D^{2}f(a)(u, v)$, thay vì của $D^{2}f(a)(u)(v)$. Thì, ở trên thảo luận có thể được summarized bởi nói rằng rằng khi $D^{2}f(a)$ được định nghĩa, ta có
$$D^{2}f(a)(u, v) = D_{u}D_{v}f(a).$$

<!-- PAGE 1476 -->

> **Định nghĩa 39.16.** Khi $E$ có hữu hạn số chiều và $(a_{0}, (e_{1}, \dots  , e_{n}))$ là hệ quy chiếu (frame) cho $E$, ta
$$denote D_{ej}D_{ei}f(a) by \frac{\partial^{2} f}{\partial x_{i}\partial x_{j}} (a), when i \neq  j, and we denote D_{ei}D_{ei}f(a) by \frac{\partial^{2} f}{\partial x_{i}^{2}} (a).$$
Sau đây quan trọng bổ đề attributed đến Schwarz có thể được được hiển thị, bằng cách sử dụng Mệnh đề
$$\longrightarrow \times  \longrightarrow \longrightarrow$$
39.12. Cho trước ánh xạ song tuyến tính (bilinear map) $f$: $E E \to F$, nhắc lại rằng $f$ là đối xứng, nếu
$$f(u, v) = f(v, u),$$
$$\longrightarrow$$
Với mọi $u, v \in E$.

> **Mệnh đề 39.20.** (Schwarz’s bổ đề) Cho trước hai được chuẩn (norm) các không gian afin $E$ và $F$, cho trước bất kỳ mở tập con $A$ của $E$, cho trước bất kỳ $f$: $A \to F$, với mọi $a \in A$, nếu $D^{2}f(a)$ tồn tại, thì
$$\longrightarrow  \longrightarrow  \longrightarrow$$
$D^{2}f(a) \in L_{2}(E , E$; $F$) là liên tục đối xứng ánh xạ song tuyến tính (bilinear map). Như hệ quả, nếu $E$ là của hữu hạn số chiều $n$, và $(a_{0}, (e_{1}, \dots  , e_{n}))$ là hệ quy chiếu (frame) cho $E$, ta có
$$\frac{\partial^{2} f}{\partial x_{i}\partial x_{j}} (a) = \frac{\partial^{2} f}{\partial x_{j}\partial x_{i}} (a).$$
Nhận xét: Có một variation của ở trên kết quả mà thực hiện không giả sử sự tồn tại của $D^{2}f(a)$, nhưng thay vì giả sử rằng $D_{u}D_{v}f$ và $D_{v}D_{u}f$ tồn tại trên mở tập con chứa và là liên tục tại, và kết luận rằng $D_{u}D_{v}f(a) = D_{v}D_{u}f(a)$. Điều này là chỉ khác nhau kết quả mà thực hiện không suy ra Mệnh đề 39.20, và là không hệ quả của Mệnh đề 39.20.
$$When E =\mathbb{R}^{2}, the only existence of \frac{\partial^{2} f}{\partial x\partial y} (a) and \frac{\partial^{2} f}{\partial y\partial x} (a) is not sufficient to insure the$$
Sự tồn tại của $D^{2}f(a)$. Khi $E$ nếu của hữu hạn số chiều $n$ và $(a_{0}, (e_{1}, \dots  , e_{n}))$ là hệ quy chiếu (frame) cho $E$, nếu $D^{2}f(a)$ tồn tại,
$$\longrightarrow$$
Với mọi $u = u_{1}e_{1} + \cdots  + u_{n}e_{n}$ và $v = v_{1}e_{1} + \cdots  + v_{n}e_{n}$ trong $E$, vì $D^{2}f(a)$ là dạng song tuyến tính đối xứng, ta có
$$D^{2}f(a)(u, v) = \sum_{=1,j=1}^{n}  u_{i}v_{j} \frac{\partial^{2} f}{\partial x_{i}\partial x_{j}} (a),$$
$$i$$
Mà có thể được được viết trong ma trận tạo thành như:
$$D^{2}f(a)(u, v) = U^{\top} \begin{pmatrix} \partial^{2} f & \partial^{2} f & \partial^{2} f \\ (a) & (a) & \dots & (a) \\ \partial x_{1}^{2} & \partial x_{1}\partial x_{2} & \partial x_{1}\partial x_{n} \\ \partial^{2} f & \partial^{2} f & \partial^{2} f \\ (a) & (a) & \dots & (a) \\ \partial x_{1}\partial x_{2} & \partial x_{2}^{2} & \partial x_{2}\partial x_{n} \\ \vdots & \vdots & \ddots & \vdots \\ \partial^{2} f & \partial^{2} f & \partial^{2} f \\ (a) & (a) & \dots & (a) \\ \partial x_{1}\partial x_{n} & \partial x_{2}\partial x_{n} & \partial x_{n}^{2} \end{pmatrix} V$$
Ở đâu $U$ là ma trận cột biểu diễn $u$, và $V$ là ma trận cột biểu diễn $v$, trên hệ quy chiếu (frame) $(a_{0}, (e_{1}, \dots  , e_{n}))$.

<!-- PAGE 1477 -->

> **Định nghĩa 39.17.** ở trên ma trận đối xứng (symmetric matrix) được gọi là Hessian của $f$ tại.

> **Ví dụ 39.14.** Xét hàm $f$ được định nghĩa trên thực khả nghịch $2\times 2$ các ma trận sao cho ad - bc $> 0$ cho trước bởi
$$f(a, b, c, d) = \log(ad -bc).$$
Ta ngay lập tức kiểm chứng rằng Ma trận Jacobi (Jacobian matrix) của $f$ được cho bởi
$$df_{a,b,c,d} = \frac{1}{ad -bc} \begin{pmatrix} d & -c & -b & a \end{pmatrix} .$$
Nó là dễ dàng đã kiểm tra rằng nếu
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} ,X = \begin{pmatrix} x_{1} & x_{2} \\ x_{3} & x_{4} \end{pmatrix} ,$$
Thì
$$df_{A}(X) = \mathrm{tr}(A^{-1}X) = \frac{1}{ad -bc} \mathrm{tr} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} \begin{pmatrix} x_{1} & x_{2} \\ x_{3} & x_{4} \end{pmatrix} \begin{pmatrix}\end{pmatrix} .$$
Việc tính toán bậc hai các đạo hàm, ta tìm rằng Ma trận Hesse (Hessian matrix) của $f$ được cho bởi
$$Hf(A) = \frac{1}{(ad -bc)^{2}} \begin{pmatrix} -d^{2} & cd & bd & -bc \\ cd & -c^{2} & -ad & ac \\ bd & -ad & -b^{2} & ab \\ bc & ac & ab & a^{2} \end{pmatrix} .$$
$$--$$
Bằng cách sử dụng công thức cho đạo hàm của nghịch đảo ánh xạ và dây chuyền/xích quy tắc ta có thể chỉ ra rằng
$$D^{2}f(A)(X_{1}, X_{2}) = -\mathrm{tr}(A^{-1}X_{1}A^{-1}X_{2}),$$
Và do đó
$$Hf(A)(X_{1}, X_{2}) = -\mathrm{tr}(A^{-1}X_{1}A^{-1}X_{2}),$$
Công thức mà là far từ hiển nhiên. hàm $f$ có thể được suy rộng/tổng quát hóa đến các ma trận $A \in GL^{+}(n,\mathbb{R})$, nghĩa là, $n\times n$ thực các ma trận khả nghịch của dương các định thức, như
$$f(A) = \log \det(A).$$
Nó có thể được được hiển thị rằng các công thức
$$df_{A}(X) = \mathrm{tr}(A^{-1}X)$$
$$D^{2}f(A)(X_{1}, X_{2}) = -\mathrm{tr}(A^{-1}X_{1}A^{-1}X_{2})$$
Cũng đúng.

<!-- PAGE 1478 -->

> **Ví dụ 39.15.** Nếu ta thu hẹp hàm của Ví dụ 39.14 đến đối xứng xác định dương (SPD) các ma trận ta thu được hàm $g$ được định nghĩa bởi
$$g(a, b, c) = \log(ac -b^{2}).$$
Ta ngay lập tức kiểm chứng rằng Ma trận Jacobi (Jacobian matrix) của $g$ được cho bởi
$$dg_{a,b,c} = \frac{1}{ac -b^{2}} \begin{pmatrix} c & -2b & a \end{pmatrix} .$$
Việc tính toán bậc hai các đạo hàm, ta tìm rằng Ma trận Hesse (Hessian matrix) của $g$ được cho bởi
$$Hg(a, b, c) = \frac{1}{(ac -b^{2})^{2}} \begin{pmatrix} -c^{2} & 2bc & -b^{2} \\ 2bc & -2(b^{2}+ ac) & 2ab \\ b^{2} & 2ab & a^{2} \end{pmatrix} .$$
$$--$$
Mặc dù điều này là không hiển nhiên, nó có thể được được hiển thị rằng nếu ac - $b^{2} > 0$ và, $c > 0$, thì ma trận -Hg(, $b, c)$ là đối xứng xác định dương (SPD). Nếu $F$ chính nó là của hữu hạn số chiều, và $(b_{0}, (v_{1}, \dots  , v_{m}))$ là hệ quy chiếu (frame) cho $F$, thì $f = (f_{1}, \dots  , f_{m})$, và mỗi thành phần $D^{2}f(a)_{i}(u, v)$ của $D^{2}f(a)(u, v) (1 \le i \le m)$, có thể được viết dưới dạng
$$D^{2}f(a)_{i}(u, v) = U^{\top} \begin{pmatrix} \partial^{2} f_{i} & \partial^{2} f_{i} & \partial^{2} f_{i} \\ (a) & (a) & \dots & (a) \\ \partial x_{1}^{2} & \partial x_{1}\partial x_{2} & \partial x_{1}\partial x_{n} \\ \partial^{2} f_{i} & \partial^{2} f_{i} & \partial^{2} f_{i} \\ (a) & (a) & \dots & (a) \\ \partial x_{1}\partial x_{2} & \partial x_{2}^{2} & \partial x_{2}\partial x_{n} \\ \vdots & \vdots & \ddots & \vdots \\ \partial^{2} f_{i} & \partial^{2} f_{i} & \partial^{2} f_{i} \\ (a) & (a) & \dots & (a) \\ \partial x_{1}\partial x_{n} & \partial x_{2}\partial x_{n} & \partial x_{n}^{2} \end{pmatrix} V$$
Do đó, ta có thể mô tả vectơ $D^{2}f(a)(u, v)$ theo $mn\times$ mn-matrix bao gồm của $m$ đường chéo các khối, mà là ở trên Hessians, và ma trận hàng $(U^{\top} , \dots  , U^{\top}$) $(m$ lần) và ma trận cột bao gồm của $m$ copies của $V$. Ta bây giờ indicate ngắn gọn cách mà bậc cao các đạo hàm được định nghĩa. Cho $m \ge 2$. Cho trước hàm $f$: $A \to F$ như trước, với mọi $a \in A$, nếu các đạo hàm $D^{i}f$ tồn tại trên $A$ với mọi $i, 1 \le i \le m$ - $1$, bởi quy nạp, $D^{m-1}f$ có thể được được xét là hàm liên tục (continuous function)
$$--\longrightarrow  \longrightarrow$$
$D^{m-1}f$: $A \to L_{m-1}(E^{m-1}; F$).

> **Định nghĩa 39.18.** Định nghĩa $D^{m}f(a)$, đạo hàm thứ $m$ của $f$ tại, như
$$D^{m}f(a) = D(D^{m-1}f)(a).$$
$$\longrightarrow  \longrightarrow$$
Thì $D^{m}f(a)$ có thể được đồng nhất với liên tục m-ánh xạ đa tuyến tính (multilinear map) trong $\mathcal{L}_{m}(E^{m}; F$). Ta có thể thì chỉ ra (như ta đã thực hiện trước), rằng nếu $D^{m}f(a)$ được định nghĩa, thì
$$D^{m}f(a)(u_{1}, \dots  , u_{m}) = D_{u1} \dots  D_{um}f(a).$$

<!-- PAGE 1479 -->

> **Định nghĩa 39.19.** Khi $E$ nếu của hữu hạn số chiều $n$ và $(a_{0}, (e_{1}, \dots  , e_{n}))$ là hệ quy chiếu (frame) cho $E$, nếu $D^{m}f(a)$ tồn tại, với mọi $j_{1}, \dots  , j_{m} \in {1, \dots  , n}$, ta ký hiệu $D_{ejm} \dots  D_{ej1}f(a)$ bởi
$$\frac{\partial^{m} f}{\partial x_{j1} \dots  \partial x_{jm}} (a).$$

> **Ví dụ 39.16.** Đi quay lại đến hàm $f$ của Ví dụ 39.14 cho trước bởi f() $=$ log det(), bằng cách sử dụng công thức cho đạo hàm của nghịch đảo ánh xạ, dây chuyền/xích quy tắc và tích quy tắc, ta có thể chỉ ra rằng
$$D^{m}f(A)(X_{1}, \dots  , X_{m}) = (-1)^{m-1} \sum_{\in Sm-}  \mathrm{tr}(A^{-1}X_{1}A^{-1}X_{\sigma(1)+1}A^{-1}X_{\sigma(2)+1} \cdots  A^{-1}X_{\sigma(m-1)+1})$$
$$\sigma 1$$
Với mọi $m \ge 1$, ở đâu $A \in GL^{+}(n,\mathbb{R})$ và $X_{1}, \dots  X_{m}$ là bất kỳ $n \times  n$ thực các ma trận.
$$\longrightarrow  \longrightarrow$$
Cho trước m-ánh xạ đa tuyến tính (multilinear map) $f \in L_{m}(E^{m}; F$), nhắc lại rằng $f$ là đối xứng nếu
$$f(u_{\pi(1)}, \dots  , u_{\pi(m)}) = f(u_{1}, \dots  , u_{m}),$$
$$\longrightarrow$$
Với mọi $u_{1}, \dots  , u_{m} \in E$, và tất cả các hoán vị $\pi$ trên ${1, \dots  , m}$. Thì, sau đây tổng quát hóa của Schwarz’s bổ đề nghiệm đúng.

> **Mệnh đề 39.21.** Cho trước hai được chuẩn (norm) các không gian afin $E$ và $F$, cho trước bất kỳ mở tập con $A$ của $E$, cho trước bất kỳ $f$: $A \to F$, với mọi $a \in A$, với mọi $m \ge 1$, nếu $D^{m}f(a)$ tồn tại, thì
$$\longrightarrow  \longrightarrow$$
$D^{m}f(a) \in L_{m}(E^{m}; F$) là liên tục đối xứng m-ánh xạ đa tuyến tính (multilinear map). Như hệ quả, nếu $E$ là của hữu hạn số chiều $n$, và $(a_{0}, (e_{1}, \dots  , e_{n}))$ là hệ quy chiếu (frame) cho $E$, ta có
$$\frac{\partial^{m} f}{\partial x_{j1} \dots  \partial x_{jm}} (a) = \frac{\partial^{m} f}{\partial x_{\pi(j1)} \dots  \partial x_{\pi(jm)}} (a),$$
Với mọi $j_{1}, \dots  , j_{m} \in {1, \dots  , n}$, và với mọi hoán vị $\pi$ trên ${1, \dots  , m}$. Bởi vì vết (trace) hàm là bất biến dưới hoán vị của của nó các đối số/lập luận (tr(XY) $=$ tr(Y $X))$, ta xem rằng thứ $m$ các đạo hàm trong Ví dụ 39.16 là thật vậy đối xứng đa tuyến tính các ánh xạ. Nếu $E$ là của hữu hạn số chiều $n$, và $(a_{0}, (e_{1}, \dots  , e_{n}))$ là hệ quy chiếu (frame) cho $E, D^{m}f(a)$ là đối xứng m-ánh xạ đa tuyến tính (multilinear map), và ta có
$$D^{m}f(a)(u_{1}, \dots  , u_{m}) = \sum_{j}  u_{1,j1} \cdots  u_{m,jm} \frac{\partial^{m} f}{\partial x_{j1} \dots  \partial x_{jm}} (a),$$
Ở đâu $j$ các miền giá trị (range) trên tất cả các hàm $j$: ${1, \dots  , m} \to {1, \dots  , n}$, với mọi $m$ các vectơ
$$u_{j} = u_{j,1}e_{1} + \cdots  + u_{j,n}e_{n}.$$
Khái niệm của $C^{1}-function$ là suy rộng/tổng quát hóa đến khái niệm của $C^{m}-function$, và Định lý 39.13 có thể cũng là suy rộng/tổng quát hóa.

<!-- PAGE 1480 -->

> **Định nghĩa 39.20.** Cho trước hai được chuẩn (norm) các không gian afin $E$ và $F$, và mở tập con $A$ của $E$, với mọi $m \ge 1$, ta nói rằng hàm $f$: $A \to F$ là của lớp $C^{m}$ trên $A$ hoặc $C^{m}-function$ trên $A$ nếu $D^{k}f$ tồn tại và là liên tục trên $A$ với mọi $k, 1 \le k \le m$. Ta nói rằng $f$: $A \to F$ là của lớp $C^{\infty}$ trên $A$ hoặc $C^{\infty}-function$ trên $A$ nếu $D^{k}f$ tồn tại và là liên tục trên $A$ với mọi $k \ge 1$. $C^{\infty}-function$ (trên $A)$ cũng được gọi là một trơn (smooth) hàm (trên $A)$. $C^{m}-diffeomorphism f$: $A \to B$ giữa $A$ và $B$ (ở đâu $A$ là mở tập con của $E$ và $B$ là mở tập con của $B)$ là song ánh giữa $A$ và $B =$ f(), sao cho cả hai $f$: $A \to B$ và của nó nghịch đảo $f^{-1}: B \to A$ là $C^{m}-functions$. Tương đương, $f$ là $C^{m}-function$ trên $A$ nếu $f$ là $C^{1}-function$ trên $A$ và Df là $C^{m-1}-$ hàm trên $A$. Ta có kết quả sau định lý cho cần và đủ điều kiện cho $f$ đến $C^{m}-function$ trên $A$. tổng quát hóa đến trường hợp ở đâu $E = (E_{1}, a_{1}) \oplus \cdots  \oplus (E_{n}, a_{n})$ cũng nghiệm đúng.

> **Định lý 39.22.** Cho trước hai được chuẩn (norm) các không gian afin $E$ và $F$, ở đâu $E$ là của hữu hạn số chiều $n$, và ở đâu $(a_{0}, (u_{1}, \dots  , u_{n}))$ là hệ quy chiếu (frame) của $E$, cho trước bất kỳ mở tập con $A$ của $E$, cho trước bất kỳ hàm $f$: $A \to F$, với mọi $m \ge 1$, đạo hàm $D^{m}f$ là $C^{m}-function$ trên $A$ khi và chỉ khi mọi
$$partial derivative D_{ujk} \dots  D_{uj1}f (or \frac{\partial^{k} f}{\partial x_{j1} \dots  \partial x_{jk}} (a)) is defined and continuous on A, for all$$
$k, 1 \le k \le m$, và tất cả $j_{1}, \dots  , j_{k} \in {1, \dots  , n}$. Như hệ quả, nếu $F$ là của hữu hạn số chiều $p$, và $(b_{0}, (v_{1}, \dots  , v_{p}))$ là hệ quy chiếu (frame) của $F$, đạo hàm $D^{m}f$ được định nghĩa và liên tục trên $A$ khi và chỉ khi
$$every partial derivative D_{ujk} \dots  D_{uj1}f_{i} (or \frac{\partial^{k} f_{i}}{\partial x_{j1} \dots  \partial x_{jk}} (a)) is defined and continuous on A,$$
Với mọi $k, 1 \le k \le m$, với mọi $i, 1 \le i \le p$, và tất cả $j_{1}, \dots  , j_{k} \in {1, \dots  , n}$.

> **Định nghĩa 39.21.** Khi $E = \mathbb{R}$ (hoặc $E = \mathbb{C})$, với mọi $a \in E, D^{m}f(a)(1, \dots  , 1)$ là vectơ $\longrightarrow$ trong $F$, được gọi là thứ $m$-thứ tự vectơ đạo hàm. Như trong trường hợp $m = 1$, ta sẽ thường đồng nhất ánh xạ đa tuyến tính (multilinear map) $D^{m}f(a)$ với vectơ $D^{m}f(a)(1, \dots  , 1)$. Một số notational các quy ước có thể cũng là đã giới thiệu để đơn giản hóa ký hiệu của higherorder các đạo hàm, và ta thảo luận như vậy các quy ước rất ngắn gọn. Nhắc lại rằng khi $E$ là của hữu hạn số chiều $n$, và $(a_{0}, (e_{1}, \dots  , e_{n}))$ là hệ quy chiếu (frame) cho $E, D^{m}f(a)$ là đối xứng m-ánh xạ đa tuyến tính (multilinear map), và ta có
$$D^{m}f(a)(u_{1}, \dots  , u_{m}) = \sum_{j}  u_{1,j1} \cdots  u_{m,jm} \frac{\partial^{m} f}{\partial x_{j1} \dots  \partial x_{jm}} (a),$$
Ở đâu $j$ các miền giá trị (range) trên tất cả các hàm $j$: ${1, \dots  , m} \to {1, \dots  , n}$, với mọi $m$ các vectơ
$$u_{j} = u_{j,1}e_{1} + \cdots  + u_{j,n}e_{n}.$$
Ta có thể thì nhóm khác nhau occurrences của $\partial x_{jk}$ tương ứng với cùng biến $x_{jk}$, và điều này dẫn đến đến ký hiệu
$$\cdots$$
$$\alpha 1\alpha 2\alpha n$$
$$\begin{pmatrix} \partial \\ \partial x_{1} \end{pmatrix} \begin{pmatrix} \partial \\ \partial x_{2} \end{pmatrix} \begin{pmatrix} \partial \\ \partial x_{n} \end{pmatrix} f(a),$$
