# Xạ ảnh Các ánh xạ


<!-- PAGE 898 -->

## 26.5 Xạ ảnh Các ánh xạ

Cho trước hai không tầm thường các không gian vectơ $E$ và $F$ và ánh xạ tuyến tính (linear map) $f$: $E \to F$, nhận thấy rằng với mọi $u, v \in (E$ - Ker $f)$, nếu $v = \lambda u$ với một số $\lambda  \in K -{0}$, thì f(v) $= \lambda$ f(u), và do đó $f$ bị thu hẹp đến $(E$ -Ker $f)$ cảm sinh hàm P(f): (P(E) -P(Ker $f)) \to$ P(F) được định nghĩa sao cho
$$P(f)([u]_{\sim}) = [f(u)]_{\sim},$$
Như trong sau đây giao hoán biểu đồ:
$$f$$
$$E -\mathrm{Ker} fF -{0}$$
$$pp$$
$$P(E) -P(\mathrm{Ker} f)_{P(f)} /P(F)$$
Khi $f$ là đơn ánh (injective), i.e., khi Ker $f = {0}$, thì P(f): P(E) $\to$ P(F) là thật vậy welldefined hàm. ở trên thảo luận motivates sau đây định nghĩa.

> **Định nghĩa 26.5.** Cho trước hai không tầm thường các không gian vectơ $E$ và $F$, bất kỳ ánh xạ tuyến tính (linear map) $f$: $E \to F$ cảm sinh riêng ánh xạ P(f): P(E) $\to$ P(F) được gọi là ánh xạ xạ ảnh (projective map), sao cho nếu Ker $f = {u \in E$ | f(u) $= 0}$ là hạt nhân (kernel) của $f$, thì P(f): (P(E)-P(Ker $f)) \to$ P(F) là tổng ánh xạ được định nghĩa sao cho
$$P(f)([u]_{\sim}) = [f(u)]_{\sim},$$
Như trong sau đây giao hoán biểu đồ:
$$f$$
$$E -\mathrm{Ker} fF -{0}$$
$$pp$$
$$P(E) -P(\mathrm{Ker} f)_{P(f)} /P(F)$$
Nếu $f$ là đơn ánh (injective), i.e., khi Ker $f = {0}$, thì P(f): P(E) $\to$ P(F) là tổng hàm được gọi là phép biến đổi xạ ảnh, và khi $f$ là song ánh (bijective), ta gọi P(f) phép xạ ảnh (projectivity), hoặc xạ ảnh đẳng cấu, hoặc phép biến đổi phân tuyến tính (homography). tập hợp của projectivities P(f): P(E) $\to$ P(E) là nhóm được gọi là xạ ảnh (tuyến tính) nhóm, và được ký hiệu bởi PGL(E).  Một nên realize rằng nếu ánh xạ tuyến tính (linear map) $f$: $E \to F$ là không đơn ánh (injective), thì xạ ảnh
$$map P(f): P(E) \to P(F) is only a partial map, i.e., it is undefined on P(\mathrm{Ker} f). In$$
Cụ thể, nếu $f$: $E \to F$ là null ánh xạ (i.e., Ker $f = E)$, miền xác định của P(f) là rỗng và P(f) là riêng hàm undefined everywhere. Ta có thể muốn đến đòi hỏi trong Định nghĩa 26.5 rằng $f$ không là null ánh xạ để tránh điều này suy biến trường hợp. Xạ ảnh các ánh xạ là thường được định nghĩa chỉ khi chúng được cảm sinh bởi song ánh (bijective) các ánh xạ tuyến tính (linear maps).

<!-- PAGE 899 -->
Ta lấy closer nhìn tại projectivities của xạ ảnh $line\mathbb{P}_{K}^{1}$, vì chúng đóng vai trò trong “thay đổi của các tham số” cho xạ ảnh các đường cong. phép xạ ảnh (projectivity) $f$: $\mathbb{P}_{K}^{1} \to \mathbb{P}_{K}^{1}$ được cảm sinh bởi một số song ánh (bijective) ánh xạ tuyến tính (linear map) $g: K^{2} \to K^{2}$ cho trước bởi một số ma trận khả nghịch (invertible matrix)
$$M(g) = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$
Với ad -bc $\neq  0$. Vì xạ ảnh đường thẳng $\mathbb{P}_{K}^{1}$ là đẳng cấu đến $K \cup {\infty$ }, dễ dàng kiểm chứng được rằng $f$ được định nghĩa như sau:
$$$$
$$z \frac{az + b}{cz + d} if z \neq  - \frac{d}{c} ,$$
$$$$
$$$$
$$$$
$$c \neq  0- \frac{\mapsto d}{c} \mapsto \infty ,$$
$$$$
$$\infty \mapsto \frac{a}{c} ;c = 0z \mapsto \frac{az + b}{d} ,$$
$$$$
$$$$
$$\infty \mapsto \infty .$$
$$$$
Từ Mục 26.4, ta biết rằng các điểm không tại vô cực là repesented bởi các vectơ của tạo thành $(z, 1)$ ở đâu $z \in K$ và rằng $\infty$ được biểu diễn bởi $(1, 0)$. Thứ nhất, giả sử $c \neq  0$. Vì
$$\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} z \\ 1 \end{pmatrix} = \begin{pmatrix} az + b \\ cz + d \end{pmatrix} ,$$
Nếu cz $+ d \neq  0$, nghĩa là, $z \neq  -d/c$, thì
$$(az + b, cz + d) \sim \begin{pmatrix} az + b \\ , 1 \\ cz + d \end{pmatrix} ,$$
Do đó $z$ là là mapped đến (az $+ d)/cz + d)$. Nếu cz $+ d = 0$, thì
$$(az + d, 0) \sim (1, 0) = \infty ,$$
Do đó $-d/c$ là mapped đến $\infty$. Ta cũng có
$$\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} a \\ c \end{pmatrix} ,$$
Và vì $c \neq  0$ ta có
$$(a, c) \sim (a/c, 1),$$
Do đó $\infty$ là mapped đến $a/c$. trường hợp ở đâu $c = 0$ là handled tương tự. Nếu $K = \mathbb{R}$ hoặc $K = \mathbb{C}$, lưu ý rằng $a/c$ là giới hạn của (az $+ b)/(cz + d)$, như $z$ các cách tiếp cận vô cực, và giới hạn của (az $+ b)/(cz + d)$ như $z$ các cách tiếp cận $-d/c$ là $\infty$ (khi $c \neq  0)$. Các phép chiếu giữa các siêu phẳng tạo thành quan trọng ví dụ của projectivities.

<!-- PAGE 900 -->

> **Định nghĩa 26.6.** Cho trước không gian xạ ảnh (projective space) P(E), với mọi hai phân biệt các siêu phẳng P(H) và P(H'), với mọi điểm $c \in$ P(E) không trong P(H) cũng không trong P(H'), phép chiếu (hoặc perspectivity) của tâm $c$ giữa P(H) và P(H') là ánh xạ $f$: P(H) $\to$ P(H') được định nghĩa sao cho với mọi $a \in$ P(H), điểm f() là giao của đường thẳng $\langle c, a\rangle$ qua $c$ và với P(H'). Cho chúng ta kiểm chứng rằng $f$ là tốt–được định nghĩa và song ánh (bijective) phép biến đổi xạ ảnh. Vì các siêu phẳng P(H) và P(H') là phân biệt, các siêu phẳng $H$ và H' trong $E$ là phân biệt, và vì $c$ là không trong P(H) cũng không trong P(H'), đặt $c =$ p(u) với một số khác không vectơ $u \in E$, thì $u \in / H$ và $u \in /$ H', và do đó $E = H \oplus$ Ku $=$ H' $\oplus$ Ku. Nếu $\pi$: $E \to$ H' là ánh xạ tuyến tính (linear map) (phép chiếu lên H' song song đến $u)$ được định nghĩa sao cho
$$\pi (w + \lambda u) = w,$$
Với mọi $w \in$ H' và tất cả $\lambda  \in K$, vì $E = H \oplus$ Ku $=$ H' $\oplus$ Ku, thu hẹp $g: H \to$ H' của $\pi$: $E \to$ H' đến $H$ là tuyến tính song ánh giữa $H$ và H', và rõ ràng $f =$ P(g), mà chỉ ra rằng $f$ là phép xạ ảnh (projectivity).
Nhận xét: Đi quay lại đến ánh xạ tuyến tính (linear map) $\pi$: $E \to$ H' (phép chiếu lên H' song song đến $u)$, lưu ý rằng $P(\pi$): P(E) $\to$ P(H') là cũng ánh xạ xạ ảnh (projective map), nhưng nó là không đơn ánh (injective), và do đó chỉ riêng ánh xạ. Tổng quát hơn, cho trước tổng trực tiếp (direct sum) $E = V \oplus W$, phép chiếu $\pi$: $E \to V$ lên $V$ song song đến $W$ cảm sinh ánh xạ xạ ảnh (projective map) $P(\pi$): P(E) $\to$ P(V), và cho trước một cái khác tổng trực tiếp (direct sum) $E = U \oplus W$, thu hẹp của $\pi$ đến $U$ cảm sinh perspectivity $f$ giữa P(U) và P(V). Geometrically, $f$ được định nghĩa như sau: Cho trước bất kỳ điểm $a \in$ P(U), nếu $\langle$ P(W), $a\rangle$ là nhỏ nhất xạ ảnh không gian con chứa P(W) và, điểm f() là giao của $\langle$ P(W), $a\rangle$ với P(V). Hình 26.11 minh họa phép chiếu $f$ của tâm $c$ giữa hai xạ ảnh các đường thẳng $\Delta$ và $\Delta'$ (trong thực xạ ảnh mặt phẳng). Nếu ta xét ba phân biệt các điểm $d_{1}, d_{2}, d_{3}$ trên $\Delta$ và của chúng các ảnh $d_{1}', d_{2}', d_{3}'$ trên $\Delta'$ dưới phép chiếu $f$, thì các tỉ số là không được bảo toàn, nghĩa là,
$$\frac{-\longrightarrow d_{3}d_{1}}{d_{3}d_{2}} -\longrightarrow = \frac{-\longrightarrow d_{3}'d_{1}'}{d_{3}'d_{2}'} -\longrightarrow .$$
Tuy nhiên, nếu ta xét bốn phân biệt các điểm $d_{1}, d_{2}, d_{3}, d_{4}$ trên $\Delta$ và của chúng các ảnh $d_{1}', d_{2}', d_{3}', d_{4}'$ trên $\Delta'$ dưới phép chiếu $f$, ta sẽ chỉ ra sau này rằng ta có kết quả sau preservation của so-called “tỉ số kép (cross-ratio)”
$$\frac{-\longrightarrow d_{3}d_{1}}{d_{3}d_{2}} , \frac{-\longrightarrow d_{4}d_{1}}{d_{4}d_{2}} = \frac{-\longrightarrow d_{3}'d_{1}'}{d_{3}'d_{2}'} , \frac{-\longrightarrow d_{4}'d_{1}'}{d_{4}'d_{2}'} .$$
$$-\longrightarrow -\longrightarrow -\longrightarrow -\longrightarrow$$
Cross-ratios và các phép chiếu đóng quan trọng vai trò trong hình học (với một số rất thanh lịch illustrations của sự kiện này, xem Sidler $[167])$.

<!-- PAGE 901 -->
$$c$$
$$d_{1}$$
$$d_{2}$$
$$d_{3}$$
$$d_{4}$$
$$\Delta$$
$$d_{1}'d_{2}'d_{3}'d_{4}'\Delta'$$
$$D_{1}D_{2}D_{3}D_{4}$$
$$Figure 26.11: A projection of center c between two lines \Delta and \Delta' .$$
Ta bây giờ turn đến vấn đề của xác định khi hai các ánh xạ tuyến tính (linear maps) $f, g$ xác định cùng ánh xạ xạ ảnh (projective map), i.e., khi P(f) $=$ P(g). sau đây mệnh đề cho chúng ta đầy đủ câu trả lời.

> **Mệnh đề 26.4.** Cho trước hai không tầm thường các không gian vectơ $E$ và $F$, với mọi hai các ánh xạ tuyến tính (linear maps) $f$: $E \to F$ và $g: E \to F$, ta có P(f) $=$ P(g) khi và chỉ khi tồn tại một vô hướng (scalar) $\lambda  \in K -{0}$ sao cho $g = \lambda f$.

*Chứng minh.* Nếu $g = \lambda f$, rõ ràng là P(f) $=$ P(g). Ngược lại, trong thứ tự đến có P(f) $=$ P(g), ta phải có Ker $f =$ Ker $g$. Nếu Ker $f =$ Ker $g = E$, thì $f$ và $g$ là cả hai null ánh xạ, và trường hợp này là tầm thường. Nếu $E$ -Ker $f \neq  \emptyset$, bằng cách lấy cơ sở (basis) của Im $f$ và một số nghịch đảo ảnh (image) của cơ sở (cơ sở (basis)) này, ta thu được cơ sở (basis) $B$ của không gian con $G$ của $E$ sao cho $E =$ Ker $f \oplus G$. Nếu dim(G) $= 1$, thu hẹp của bất kỳ ánh xạ tuyến tính (linear map) $f$: $E \to F$ đến $G$ được xác định bởi một số khác không vectơ $u \in E$ và một số vô hướng (scalar) $\lambda  \in K$, và mệnh đề là hiển nhiên. Do đó, giả sử rằng dim(G) $\ge 2$. Với mọi hai phân biệt cơ sở (basis) các vectơ $u, v \in B$, vì P(f) $=$ P(g), ở đó phải là một số khác không các vô hướng $\lambda (u), \lambda (v)$, và $\lambda (u + v)$ sao cho
$$g(u) = \lambda (u)f(u),g(v) = \lambda (v)f(v),g(u + v) = \lambda (u + v)f(u + v).$$
Vì $f$ và $g$ là tuyến tính, ta thu được
$$g(u) + g(v) = \lambda (u)f(u) + \lambda (v)f(v) = \lambda (u + v)(f(u) + f(v)),$$
Rằng là,
$$(\lambda (u + v) -\lambda (u))f(u) + (\lambda (u + v) -\lambda (v))f(v) = 0.$$
Vì $f$ là đơn ánh (injective) trên $G$ và $u, v \in B \subseteq G$ là độc lập tuyến tính (linearly independent), f(u) và f(v) là cũng độc lập tuyến tính (linearly independent), và do đó ta có
$$\lambda (u + v) = \lambda (u) = \lambda (v).$$

<!-- PAGE 902 -->
Bây giờ ta có được hiển thị rằng $\lambda (u) = \lambda (v)$, với mọi hai phân biệt cơ sở (basis) các vectơ trong $B$, mà chứng tỏ rằng $\lambda (u)$ là độc lập của $u \in G$, và chứng tỏ rằng $g = \lambda f$. Mệnh đề 26.4 chỉ ra rằng xạ ảnh tuyến tính nhóm PGL(E) là đẳng cấu đến nhóm thương (quotient group) của tuyến tính nhóm GL(E) modulo nhóm con $K^{*}id_{E}$ (ở đâu $K^{*} = K$ - ${0})$. Bằng cách sử dụng xạ ảnh các hệ quy chiếu, ta chứng minh sau đây hữu ích kết quả.

> **Mệnh đề 26.5.** Cho trước hai không tầm thường các không gian vectơ $E$ và $F$ của cùng số chiều $n + 1$, với mọi hai xạ ảnh các hệ quy chiếu $(a_{i})_{1\le i\le n+2}$ cho P(E) và $(b_{i})_{1\le i\le n+2}$ cho P(F), tồn tại duy nhất một phép xạ ảnh (projectivity) $h$: P(E) $\to$ P(F) sao cho $h(a_{i}) = b_{i}$ cho $1 \le i \le n + 2$.

*Chứng minh.* Cho $(u_{1}, \dots  , u_{n+1})$ là cơ sở (basis) của $E$ liên kết với xạ ảnh hệ quy chiếu (frame) $(a_{i})_{1\le i\le n+2}$, và cho $(v_{1}, \dots  , v_{n+1})$ là cơ sở (basis) của $F$ liên kết với xạ ảnh hệ quy chiếu (frame) $(b_{i})_{1\le i\le n+2}$. Vì $(u_{1}, \dots  , u_{n+1})$ là cơ sở (basis), tồn tại duy nhất một tuyến tính song ánh $g: E \to F$ sao cho $g(u_{i}) = v_{i}$, cho $1 \le i \le n + 1$. Rõ ràng, $h =$ P(g) là phép xạ ảnh (projectivity) sao cho $h(a_{i}) = b_{i}$, cho $1 \le i \le n + 2$. Cho h': P(E) $\to$ P(F) là bất kỳ phép xạ ảnh (projectivity) sao cho $h'(a_{i}) = b_{i}$, cho $1 \le i \le n + 2$. Theo Định nghĩa, có một tuyến tính đẳng cấu $f$: $E \to F$ sao cho h' $=$ P(f). Vì $h'(a_{i}) = b_{i}$, cho $1 \le i \le n + 2$, ta phải có $f(u_{i}) = \lambda_{i} v_{i}$, với một số $\lambda_{i}  \in K -{0}$, ở đâu $1 \le i \le n + 1$, và
$$f(u_{1} + \cdots  + u_{n+1}) = \lambda (v_{1} + \cdots  + v_{n+1}),$$
Với một số $\lambda  \in K -{0}$. Bởi tính tuyến tính của $f$, ta có
$$\lambda_{1} v_{1} + \cdots  + \lambda_{n+1} v_{n+1} = \lambda v_{1} + \cdots  + \lambda v_{n+1},$$
Và vì $(v_{1}, \dots  , v_{n+1})$ là cơ sở (basis) của $F$, ta phải có
$$\lambda_{1}  = \cdots  = \lambda_{n+1}  = \lambda .$$
Điều này chỉ ra rằng $f = \lambda g$, và do đó rằng
$$h'= P(f) = P(g) = h,$$
Và $h$ là một cách duy nhất được xác định.  ở trên mệnh đề và Mệnh đề 26.4 là sai nếu $K$ là skew trường. Cũng,
$$Proposition 26.5 fails if (b_{i})_{1\le i\le n+2} is not a projective frame, or if a_{n+2} is dropped.$$
Như hệ quả của Mệnh đề 26.5, cho trước không gian xạ ảnh (projective space) P(E), hai phân biệt xạ ảnh các đường thẳng $D$ và D' trong P(E), ba phân biệt các điểm, $b, c$ trên $D$, và bất kỳ ba phân biệt các điểm ', b', c' trên D', tồn tại duy nhất một phép xạ ảnh (projectivity) từ $D$ đến D', ánh xạ đến ', $b$ đến b', và $c$ đến c'. Điều này là bởi vì, như ta mentioned trước đó, bất kỳ ba phân biệt các điểm trên đường thẳng tạo thành xạ ảnh hệ quy chiếu (frame).
Nhận xét: Như trong afin trường hợp, ở đó là “cơ bản định lý của xạ ảnh hình học.” Để đơn giản, ta phát biểu định lý này giả sử rằng các không gian vectơ là trên trường $K =\mathbb{R}$. Cho trước

<!-- PAGE 903 -->
Bất kỳ hai các không gian xạ ảnh P(E) và P(F) của cùng số chiều $n \ge 2$, với mọi song ánh (bijective) hàm $f$: P(E) $\to$ P(F), nếu $f$ các ánh xạ bất kỳ ba phân biệt thẳng hàng các điểm, $b, c$ đến thẳng hàng các điểm f(), f(b), f(c), thì $f$ là phép xạ ảnh (projectivity). Cho nhiều hơn/thêm tổng quát các trường, $f =$ P(g) với một số “nửa tuyến tính (semilinear)” song ánh $g: E \to F$. ánh xạ chẳng hạn như $f$ (bảo toàn collinearity của bất kỳ ba phân biệt các điểm) là thường được gọi là collineation. Cho $K = \mathbb{R}$, collineations và projectivities trùng nhau. Cho nhiều hơn/thêm chi tiết, xem Samuel $[148]$. Trước closing điều này mục, ta minh họa lũy thừa của Mệnh đề 26.5 bởi chứng minh hai thú vị các kết quả. Ta bắt đầu bởi đặc trưng hóa perspectivities giữa các đường thẳng.
$$\mathbb{RP}^{2}$$

> **Mệnh đề 26.6.** Cho trước bất kỳ hai phân biệt các đường thẳng $D$ và D' trong thực xạ ảnh mặt phẳng, phép xạ ảnh (projectivity) $f$: $D \to$ D' là perspectivity khi và chỉ khi f(O) $= O$, ở đâu $O$ là giao của $D$ và D'.

*Chứng minh.* Nếu $f$: $D \to$ D' là perspectivity, thì bởi rất định nghĩa của $f$, ta có f(O) $= O$. Ngược lại, cho $f$: $D \to$ D' là phép xạ ảnh (projectivity) sao cho f(O) $= O$. Cho, $b$ là bất kỳ hai phân biệt các điểm trên $D$ cũng phân biệt từ $O$, và cho ' $=$ f() và b' $=$ f(b) trên D'. Vì $f$ là song ánh và vì, $b, O$ là đôi một phân biệt, ' $\neq$ b'. Cho $c$ là giao của các đường thẳng $\langle$, $a'\rangle$ và $\langle b, b'\rangle$, mà bởi các giả định trên, $b, O$, không thể là trên $D$ hoặc D'. Thì ta có thể định nghĩa perspectivity $g: D \to$ D' của tâm $c$, và bởi định nghĩa của $c$, ta có
$$g(a) = a',g(b) = b',g(O) = O.$$
Xem Hình 26.12. Tuy nhiên, $f$ agrees với $g$ trên $O$,, $b$, và vì $(O$,, $b)$ là xạ ảnh hệ quy chiếu (frame) cho $D$, theo Mệnh đề 26.5, ta phải có $f = g$. Bằng cách sử dụng Mệnh đề 26.6, ta có thể cho thanh lịch chứng minh của phiên bản của Desargues’s định lý (trong mặt phẳng).

> **Mệnh đề 26.7.** (Desargues) Cho trước hai các tam giác (, $b, c)$ và (', b', c') $in\mathbb{RP}^{2}$, ở đâu các điểm, $b, c$, ', b', c' là đôi một phân biệt và các đường thẳng $A = \langle b, c\rangle , B = \langle$, $c\rangle , C = \langle$, $b\rangle$, ' $= \langle$ b', $c'\rangle$, B' $= \langle$ ', $c'\rangle$, C' $= \langle$ ', $b'\rangle$ là đôi một phân biệt, nếu các đường thẳng $\langle$, $a'\rangle , \langle b, b'\rangle$, và $\langle c, c'\rangle$ giao nhau trong chung/phổ biến điểm $d$ phân biệt từ, $b, c$, ', b', c', thì giao các điểm $p = \langle b, c\rangle \cap \langle$ b', $c'\rangle , q = \langle$, $c\rangle \cap \langle$ ', $c'\rangle$, và $r = \langle$, $b\rangle \cap \langle$ ', $b'\rangle$ thuộc đến chung/phổ biến đường thẳng phân biệt từ $A, B, C$, ', B', C'.

*Chứng minh.* Xét theo các giả định trên, $b, c$, ', b', c', và $d$, điểm $r$ là trên không $\langle$, $a'\rangle$ cũng không $\langle b, b'\rangle$, điểm $p$ là trên không $\langle b, b'\rangle$ cũng không $\langle c, c'\rangle$, và điểm $q$ là trên không $\langle$, $a'\rangle$ cũng không $\langle c, c'\rangle$. Nó là cũng ngay lập tức được hiển thị rằng đường thẳng $\langle p, q\rangle$ là phân biệt từ các đường thẳng $A, B, C$, ', B', C'. Cho $f$: $\langle$, $a'\rangle \to \langle b, b'\rangle$ là perspectivity của tâm $r$ và $g: \langle b, b'\rangle \to \langle c, c'\rangle$ là perspectivity của tâm $p$. Cho $h = g \circ f$. Vì cả hai f(d) $= d$ và g(d) $= d$, ta cũng có
