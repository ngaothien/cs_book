# Cơ bản Các tính chất của Các dưới gradien và Các vi phân dưới


<!-- PAGE 1880 -->
Ta có dom(f) $= [0, +\infty$), $f$ là khả vi (differentiable) với mọi $x > 0$, nhưng nó là không khả vi dưới tại $x = 0$. chỉ tựa/hỗ trợ siêu phẳng (hyperplane) đến epi(f) tại $(0, 0)$ là đứng đường thẳng của phương trình $x = 0$ (trục $y$) như được minh họa bởi Hình 51.18.
$$\sqrt$$

![Figure 51.18](../../assets/ch51/fig_51_18.png)

**Hình 51.18:** đồ thị của riêng hàm f(x) $=$ - $\overline{x}$ và của nó đỏ đứng tựa/hỗ trợ siêu phẳng (hyperplane) tại $x = 0$.

## 51.3 Cơ bản Các tính chất của Các dưới gradien và

$$Subdifferentials$$
Major công cụ để chứng minh các tính chất của các dưới gradien là biến thể của khái niệm của đạo hàm theo hướng (directional derivative).
$$\mathbb{R}^{n} \mathbb{R}\mathbb{R}^{n}$$

> **Định nghĩa 51.15.** Cho $f$: $\to  \cup {-\infty , +\infty$ } là bất kỳ hàm. Với mọi $x \in$ sao cho f(x) là hữu hạn (f(x) $\in \mathbb{R})$, với mọi $u \in \mathbb{R}^{n}$, một phía đạo hàm theo hướng (directional derivative) f' $(x; u)$ được định nghĩa là giới hạn
$$-$$
$$f' (x; u) = lim\lambda \downarrow 0 \frac{f(x + \lambda u)f(x)}{\lambda}$$
Nếu nó tồn tại $(-\infty$ và $+\infty$ đang được phép như các giới hạn). Xem Hình 51.19. ở trên ký hiệu cho giới hạn có nghĩa là ta xét giới hạn khi $\lambda  > 0$ tiến tới đến $0$. Lưu ý rằng
$$-$$
$$lim\lambda \uparrow 0 \frac{f(x + \lambda u)f(x)}{\lambda}$$
Ký hiệu một phía giới hạn khi $\lambda  < 0$ tiến tới đến không, và rằng
$$-$$
$$-f' (x; -u) = lim\lambda \uparrow 0 \frac{f(x + \lambda u)f(x)}{\lambda} ,$$

<!-- PAGE 1881 -->
$$(x,f(x))$$
$$(x + \lambda u ,f(x + \lambda u))$$
$$\lambda > 0$$
$$\overline{u}$$
$$x$$
$$x + \lambda u$$
$$(x,f(x))$$
$$(x + \lambda u ,f(x + \lambda u))$$
$$\lambda < 0$$
$$\overline{u}\overline{x +}\overline{\lambda} u$$
$$x$$
$$\mathbb{R}^{2} \mathbb{R}\mathbb{R}^{3}$$

![Figure 51.19](../../assets/ch51/fig_51_19.png)

**Hình 51.19:** Cho $f$: $\to \cup {-\infty , +\infty$ } là hàm có đồ thị (trong) là mặt của peach pyramid. đỉnh/trên hình minh họa rằng f' $(x; u)$ là hệ số góc của slanted burnt cam đường thẳng, trong khi đáy/dưới hình depicts đường thẳng liên kết với $lim_{\lambda\uparrow0\lambda}^{f(x+\lambda u)-f(x)}$. do đó (hai phía) đạo hàm theo hướng (directional derivative) $D_{u}f(x)$ tồn tại khi và chỉ khi -f' $(x; -u) =$ f' $(x; u)$. Cũng, nếu $f$ là khả vi (differentiable) tại $x$, thì
$$f' (x; u) = \langle \nabla f_{x}, u\rangle ,for all u \in \mathbb{R}^{n},$$
Ở đâu $\nabla f_{x}$ là gradien của $f$ tại $x$. Ở đây là thứ nhất đáng chú ý kết quả.
$$\mathbb{R}^{n} \mathbb{R}\mathbb{R}^{n}$$

> **Mệnh đề 51.15.** Cho $f$: $\to  \cup {-\infty , +\infty$ } là hàm lồi (convex function). Với mọi $x \in$, nếu f(x) là hữu hạn, thì hàm
$$-$$
$$\lambda  \mapsto \frac{f(x + \lambda u)f(x)}{\lambda}$$
Là nondecreasing hàm của $\lambda  > 0$, sao cho f' $(x; u)$ tồn tại với mọi $u \in \mathbb{R}^{n}$, và
$$-$$
$$f' (x; u) = \lambda >inf0 \frac{f(x + \lambda u)f(x)}{\lambda} .$$
Hơn nữa, f' $(x; u)$ là một cách dương thuần nhất hàm lồi (convex function) của $u$ (mà có nghĩa là f' $(x; \alpha u) = \alpha$ f' $(x; u)$ với mọi $\alpha  \in \mathbb{R}$ với $\alpha  > 0$ và tất cả $u \in \mathbb{R}^{n})$, f' $(x; 0) = 0$, và
$$-f' (x; -u) \le f' (x; u)for all u \in \mathbb{R}^{n}$$

<!-- PAGE 1882 -->
Mệnh đề 51.15 được chứng minh trong Rockafellar $[143]$ (Định lý 23.1). chứng minh là không khó nhưng không rất informative.
Nhận xét: Như hàm lồi (convex function) của $u$, nó có thể được được hiển thị rằng effective miền xác định của hàm $u \mapsto$ f' $(x; u)$ là nón lồi (convex cone) được sinh bởi dom(f) - $x$. Ta sẽ bây giờ phát biểu mà không có chứng minh một số của hầu hết quan trọng các tính chất của các dưới gradien và các vi phân dưới. Đầy đủ chi tiết có thể được tìm thấy trong Rockafellar $[143]$ (Phần $V$, Mục $23)$. Trong thứ tự đến phát biểu tiếp theo mệnh đề, ta cần sau đây định nghĩa.

> **Định nghĩa 51.16.** Với mọi tập lồi (convex set) $C in\mathbb{R}^{n}$, hỗ trợ/giá (support) hàm $\delta^{*}$ (-|C) của $C$ được định nghĩa bởi
$$\delta^{*} (x|C) = \sup\langle x, y\rangle ,x \in \mathbb{R}^{n}.$$
$$y\in C$$
Theo Định nghĩa 50.11, liên hợp của indicator hàm $I_{C}$ của tập lồi (convex set) $C$ được cho bởi
$$I_{C}^{*}(x) = \sup(\langle x, y\rangle -I_{C}(y)) = \sup\langle x, y\rangle = \delta^{*} (x|C).$$
$$y\in \mathbb{R} ny\in C$$
Do đó $\delta^{*}$ (-|C) $= I_{C}^{*}$, liên hợp của indicator hàm $I_{C}$. sau đây mệnh đề relates directional các đạo hàm tại $x$ và vi phân dưới (subdifferential) tại $x$.
$$\mathbb{R}^{n} \mathbb{R}\mathbb{R}^{n}$$

> **Mệnh đề 51.16.** Cho $f$: $\to  \cup {-\infty , +\infty$ } là hàm lồi (convex function). Với mọi $x \in$,
$$\mathbb{R}^{n}$$
Nếu f(x) là hữu hạn, thì vectơ $u \in$ là dưới gradien (subgradient) đến $f$ tại $x$ khi và chỉ khi
$$f' (x; y) \ge \langle y, u\rangle for all y \in \mathbb{R}^{n}.$$
Hơn nữa, bao đóng (closure) của hàm lồi (convex function) $y \mapsto$ f' $(x; y)$ là hỗ trợ/giá (support) hàm của đóng tập lồi (convex set) $\partial$ f(x), vi phân dưới (subdifferential) của $f$ tại $x$:
$$cl(f' (x; -)) = \delta^{*} (-|\partial f(x)).$$
Phác thảo của chứng minh. Mệnh đề 51.16 được chứng minh trong Rockafellar $[143]$ (Định lý 23.2). Ta chứng minh bất đẳng thức. Nếu ta viết $z = x + \lambda y$ với $\lambda  > 0$, thì dưới gradien (subgradient) bất đẳng thức suy ra
$$f(x + \lambda u) \ge f(x) + \langle z -x, u\rangle = f(x) + \lambda \langle y, u\rangle ,$$
Do đó ta thu được
$$-$$
$$\frac{f(x + \lambda y)f(x)}{\lambda} \ge \langle y, u\rangle .$$
Vì biểu thức trên trái tiến tới đến f' $(x; y)$ như $\lambda  > 0$ tiến tới đến không, ta thu được mong muốn bất đẳng thức. phần thứ hai suy ra từ Hệ quả 13.2.1 trong Rockafellar $[143]$.

<!-- PAGE 1883 -->
Nếu $f$ là thực sự/đúng đắn hàm $on\mathbb{R}$, thì của nó effective miền xác định đang là lồi là khoảng/đoạn có tương đối phần trong (interior) là mở khoảng/đoạn (, $b)$. Trong Mệnh đề 51.16, ta có thể chọn $y = 1$ do đó $\langle y, u\rangle = u$, và với mọi $x \in$ (, $b)$, vì các giới hạn $f_{-}' (x) =$ -f'(x; $-1)$ và $f_{+}'(x) =$ f'(x; $1)$ tồn tại, với $f_{-}' (x) \le f_{+}'(x)$, ta suy ra rằng $\partial$ f(x) $= [f_{-}'(x), f_{+}'(x)]$. các số $\alpha  \in [f_{-}'(x), f_{+}'(x)]$ là
$$\mathbb{R}^{2}$$
Các hệ số góc của nonvertical các đường thẳng trong chuyển qua $(x$, f(x)) rằng là tựa/hỗ trợ các đường thẳng đến trên đồ thị (epigraph) epi(f) của $f$.

> **Ví dụ 51.10.** Nếu $f$ là celebrated ReLU hàm (ramp hàm) từ deep học (learning) được định nghĩa sao cho
$$($$
$$0if x < 0$$
$$ReLU(x) = \max{x, 0} =$$
$$xif x \ge 0,$$
Thì $\partial$ ReLU(0) $= [0, 1]$. Xem Hình 51.20. hàm ReLU là khả vi (differentiable) cho $x \neq  0$, với ReLU'(x) $= 0$ nếu $x < 0$ và ReLU'(x) $= 1$ nếu $x > 0$.
$$Figure 51.20: The graph of the ReLU function.$$
Mệnh đề 51.16 có một vài thú vị các hệ quả.
$$\mathbb{R}^{n} \mathbb{R}\mathbb{R}^{n}$$

> **Mệnh đề 51.17.** Cho $f$: $\to \cup {-\infty , +\infty$ } là hàm lồi (convex function). Với mọi $x \in$, nếu f(x) là hữu hạn và nếu $f$ là khả vi dưới tại $x$, thì $f$ là thực sự/đúng đắn. Nếu $f$ là không khả vi dưới tại $x$, thì tồn tại một $y \neq  0$ sao cho
$$f' (x; y) = -f' (x; -y) = -\infty .$$
Mệnh đề 51.17 được chứng minh trong Rockafellar $[143]$ (Định lý 23.3). Nó xác nhận rằng suy rộng/không thực sự các hàm lồi là khá pathological objects, bởi vì nếu hàm lồi (convex function) là khả vi dưới với một số $x$ sao cho f(x) là hữu hạn, thì $f$ phải là thực sự/đúng đắn. Điều này là bởi vì nếu f(x) là hữu hạn, thì dưới gradien (subgradient) bất đẳng thức suy ra rằng $f$ majorizes afin hàm, mà là thực sự/đúng đắn. tiếp theo định lý là một của hầu hết quan trọng các kết quả về connection giữa onesided directional các đạo hàm và các vi phân dưới. Nó sharpens kết quả của Định lý 51.14.

<!-- PAGE 1884 -->
$$\mathbb{R}^{n} \mathbb{R}$$

> **Định lý 51.18.** Cho $f$: $\to \cup {+\infty$ } là thực sự/đúng đắn hàm lồi (convex function). Với mọi $x \in /$ dom(f), ta có $\partial$ f(x) $= \emptyset$. Với mọi $x \in$ relint(dom(f)), ta có $\partial$ f(x) $\neq  \emptyset$, ánh xạ $y \mapsto$ f' $(x; y)$ là lồi, đóng và thực sự/đúng đắn, và
$$f' (x; y) =\sup\langle y, u\rangle = \delta^{*} (y|\partial f(x))for all y \in \mathbb{R}^{n}.$$
$$u\in \partial f(x)$$
Vi phân dưới (subdifferential) $\partial$ f(x) là khác rỗng và bị chặn (cũng đóng và lồi) khi và chỉ khi $x \in$ int(dom(f)), trong mà trường hợp f' $(x; y)$ là hữu hạn với mọi $y \in \mathbb{R}^{n}$. Định lý 51.18 được chứng minh trong Rockafellar $[143]$ (Định lý 23.4). Nếu ta viết
$$\mathbb{R}^{n}$$
$$dom(\partial f) = {x \in | \partial f(x) \neq  \emptyset },$$
Thì Định lý 51.18 suy ra rằng
$$relint(dom(f)) \subseteq dom(\partial f) \subseteq dom(f).$$
Tuy nhiên, $dom(\partial f)$ là không nhất thiết lồi như được hiển thị bởi sau đây phản ví dụ.
$$\mathbb{R}^{2}$$

> **Ví dụ 51.11.** Xét thực sự/đúng đắn hàm lồi (convex function) được định nghĩa trên cho trước bởi
$$f(x, y) = \max{g(x), |y|},$$
Ở đâu
$$\sqrt$$
$$($$
$$1 -\overline{x} if x \ge 0$$
$$g(x) =$$
$$+\infty if x < 0.$$
$$\mathbb{R}^{2}$$
Xem Hình 51.21. Nó là dễ để xem rằng dom(f) $= {(x, y) \in$ | $x \ge 0}$, nhưng
$$\mathbb{R}^{2}$$
$dom(\partial f) = {(x, y) \in$ | $x \ge 0} -{(0, y)$ | $-1 < y < 1}$, mà là không lồi. sau đây định lý là quan trọng bởi vì nó cho ta biết chúng ta khi hàm lồi (convex function) là khả vi (differentiable) theo của nó vi phân dưới (subdifferential), như được hiển thị trong Rockafellar $[143]$ (Định lý 25.1).
$$\mathbb{R}^{n}\mathbb{R}^{n}$$

> **Định lý 51.19.** Cho $f$ là hàm lồi (convex function) trên, và cho $x \in$ sao cho f(x) là hữu hạn. Nếu $f$ là khả vi (differentiable) tại $x$ thì $\partial$ f(x) $= {\nabla f_{x}}$ (ở đâu $\nabla f_{x}$ là gradien của $f$ tại $x)$ và ta có
$$f(z) \ge f(x) + \langle z -x, \nabla f_{x}\rangle for all z \in \mathbb{R}^{n}.$$
Ngược lại, nếu $\partial$ f(x) bao gồm của đơn lẻ vectơ, thì $\partial$ f(x) $= {\nabla f_{x}}$ và $f$ là khả vi (differentiable) tại $x$. thứ nhất hướng là dễ để chứng minh. Thật vậy, nếu $f$ là khả vi (differentiable) tại $x$, thì
$$f' (x; y) = \langle y, \nabla f_{x}\rangle for all y \in \mathbb{R}^{n},$$
Do đó theo Mệnh đề 51.16, vectơ $u$ là dưới gradien (subgradient) tại $x$ khi và chỉ khi
$$\langle y, \nabla f_{x}\rangle \ge \langle y, u\rangle for all y \in \mathbb{R}^{n},$$
Do đó $\langle y, \nabla f_{x}$ - $u\rangle \ge 0$ với mọi $y$, mà suy ra rằng $u = \nabla f_{x}$. Ta thu được kết quả sau hệ quả.

<!-- PAGE 1885 -->

![Figure 51.21](../../assets/ch51/fig_51_21.png)

**Hình 51.21:** đồ thị của hàm từ Ví dụ 51.11 với quan điểm dọc theo dương $x$ trục.
$$\mathbb{R}^{n}\mathbb{R}^{n}$$

> **Hệ quả 51.20.** Cho $f$ là hàm lồi (convex function) trên, và cho $x \in$ sao cho f(x) là hữu hạn. Nếu $f$ là khả vi (differentiable) tại $x$, thì $f$ là thực sự/đúng đắn và $x \in$ int(dom(f)). sau đây định lý chỉ ra rằng thực sự/đúng đắn các hàm lồi là khả vi (differentiable) hầu như everywhere.

> **Định lý 51.21.** Cho $f$ là thực sự/đúng đắn hàm lồi (convex function) trên $\mathbb{R}^{n}$, và cho $D$ là tập hợp của các vectơ ở đâu $f$ là khả vi (differentiable). Thì $D$ là trù mật tập con của int(dom(f)), và phần bù của nó trong int(dom(f)) có measure không. Hơn nữa, gradien ánh xạ $x \mapsto \nabla f_{x}$ là liên tục trên $D$. Định lý 51.21 được chứng minh trong Rockafellar $[143]$ (Định lý 25.5).
Nhận xét: Nếu $f$: (, $b) \to \mathbb{R}$ là hữu hạn hàm lồi (convex function) trên mở khoảng/đoạn của $\mathbb{R}$, thì tập hợp $D$ ở đâu $f$ là khả vi (differentiable) là trù mật trong (, $b)$, và (, $b)$ - $D$ là nhiều nhất đếm được. ánh xạ f' là liên tục và nondecreasing trên $D$. Xem Rockafellar $[143]$ (Định lý 25.3). Ta cũng có kết quả sau đây chỉ ra rằng trong “hầu hết các trường hợp” vi phân dưới (subdifferential) $\partial$ f(x) có thể được được xây dựng từ gradien ánh xạ; xem Rockafellar $[143]$ (Định lý 25.6).

> **Định lý 51.22.** Cho $f$ là đóng thực sự/đúng đắn hàm lồi (convex function) trên $\mathbb{R}^{n}$. Nếu int(dom(f)) $\neq  \emptyset$, thì với mọi $x \in$ dom(f), ta có
$$\partial f(x\overline{) = conv(}\overline{S}\overline{(}\overline{x}\overline{)) +} N_{dom(f)}(x)$$
Ở đâu $N_{dom(f)}(x)$ là chuẩn tắc/bình thường nón đến dom(f) tại $x$, và S(x) là tập hợp tất cả các giới hạn của các dãy của tạo thành $\nabla f_{x1}, \nabla f_{x2}, \dots  , \nabla f_{xp}, \dots$, ở đâu $x_{1}, x_{2}, \dots  , x_{p}, \dots$ là dãy trong dom(f) hội tụ đến $x$ sao cho mỗi $\nabla f_{xp}$ được định nghĩa.
