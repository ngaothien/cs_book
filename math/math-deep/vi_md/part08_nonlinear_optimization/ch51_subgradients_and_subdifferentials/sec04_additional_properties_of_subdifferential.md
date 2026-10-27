# Additional Các tính chất của Các vi phân dưới


<!-- PAGE 1886 -->
Tiếp theo hai các kết quả tổng quát hóa quen thuộc các kết quả về các đạo hàm đến các vi phân dưới.

> **Mệnh đề 51.23.** Cho $f_{1}, \dots  , f_{n}$ là thực sự/đúng đắn các hàm lồi $on\mathbb{R}^{n}$, và cho $f = f_{1}+\cdots +f_{n}$. Cho $x \in \mathbb{R}^{n}$, ta có
$$\partial f(x) \supseteq \partial f_{1}(x) + \cdots  + \partial f_{n}(x).$$
$$If \bigcap_{i}  n=1 relint(dom(f_{i})) \neq  \emptyset , then$$
$$\partial f(x) = \partial f_{1}(x) + \cdots  + \partial f_{n}(x).$$
Mệnh đề 51.23 được chứng minh trong Rockafellar $[143]$ (Định lý 23.8). tiếp theo kết quả có thể được được quan điểm như tổng quát hóa của dây chuyền/xích quy tắc.

> **Mệnh đề 51.24.** Cho $f$ là hàm cho trước bởi f(x) $=$ h(Ax) với mọi $x \in \mathbb{R}^{n}$, ở đâu $h$
$$\mathbb{R}^{m}$$
Là thực sự/đúng đắn hàm lồi (convex function) trên và $A$ là một ma trận cỡ $m \times  n$. Thì
$$\partial f(x) \supseteq A^{\top}(\partial h(Ax))for all x \in \mathbb{R}^{n}.$$
Nếu miền giá trị (range) của $A$ chứa điểm của relint(dom(h)), thì
$$\partial f(x) = A^{\top}(\partial h(Ax)).$$
Mệnh đề 51.24 được chứng minh trong Rockafellar $[143]$ (Định lý 23.9).

## 51.4 Additional Các tính chất của Các vi phân dưới

$$\mathbb{R}^{n} \mathbb{R}$$
Nói chung, nếu $f$: $\to$ là hàm (không nhất thiết lồi) và $f$ là khả vi (differentiable) tại $x$,
$$\mathbb{R}^{n}$$
Ta kỳ vọng rằng gradien $\nabla f_{x}$ của $f$ tại $x$ là chuẩn tắc/bình thường đến mức tập hợp ${z \in$ | f(z) $= f(x)}$ tại f(x). tương tự kết quả, như được minh họa trong Hình 51.22, nghiệm đúng cho thực sự/đúng đắn các hàm lồi theo các vi phân dưới.
$$\mathbb{R}^{n}\mathbb{R}^{n}$$

> **Mệnh đề 51.25.** Cho $f$ là thực sự/đúng đắn hàm lồi (convex function) trên, và cho $x \in$ là vectơ sao cho $f$ là khả vi dưới tại $x$ nhưng $f$ thực hiện không đạt được của nó cực tiểu tại $x$. Thì
$$\mathbb{R}^{n}$$
Chuẩn tắc/bình thường nón $N_{C}(x)$ tại $x$ đến sublevel tập hợp $C = {z \in$ | f(z) $\le f(x)}$ là bao đóng (closure) của nón lồi (convex cone) được sinh (spanned) bởi $\partial$ f(x). Mệnh đề 51.25 được chứng minh trong Rockafellar $[143]$ (Định lý 23.7). Kết quả sau đây sharpens Mệnh đề 51.8.

> **Mệnh đề 51.26.** Cho $f$ là đóng thực sự/đúng đắn hàm lồi (convex function) $on\mathbb{R}^{n}$, và cho $S$ là khác rỗng đóng và bị chặn tập con của int(dom(f)). Thì
$$\partial f(S) = \bigcup_{x\in S}  \partial f(x)$$

<!-- PAGE 1887 -->
$$(x, f(x))graph of f: R 2 ->  R$$
$$x$$
$$cone spanned by vf(x)$$
$$N  (x)C$$
$$\overline{x}\overline{x}$$
$$sublevel set Csublevel set C$$
$$\mathbb{R}^{3}$$

![Figure 51.22](../../assets/ch51/fig_51_22.png)

**Hình 51.22:** Cho $f$ là thực sự/đúng đắn hàm lồi (convex function) có đồ thị trong là peach polyhedral
$$\mathbb{R}^{2}$$
Mặt. sublevel tập hợp $C = {z \in$ | f(z) $\le f(x)}$ là cam square mà là đóng trên ba các vế/cạnh. Thì chuẩn tắc/bình thường nón $N_{C}(x)$ là bao đóng (closure) của nón lồi (convex cone) được sinh (spanned) bởi $\partial$ f(x). là khác rỗng, đóng và bị chặn. Nếu
$$\alpha  =\sup\|y\|_{2} < +\infty ,$$
$$y\in \partial f(S)$$
Thì $f$ là Lipschitizan trên $S$, và ta có
$$f' (x; z) \le \alpha  \|z\|_{2}for all x \in S and all z \in \mathbb{R}^{n}$$
$$|f(y) -f(x)| \le \alpha  \|y -z\|_{2}for all x, y \in S.$$
Mệnh đề 51.24 được chứng minh trong Rockafellar $[143]$ (Định lý 24.7). các vi phân dưới của thực sự/đúng đắn hàm lồi (convex function) $f$ và của nó liên hợp $f^{*}$ là closely related. Thứ nhất, ta có kết quả sau mệnh đề từ Rockafellar $[143]$ (Định lý 12.2).

> **Mệnh đề 51.27.** Cho $f$ là hàm lồi (convex function) trên $\mathbb{R}^{n}$. liên hợp hàm $f^{*}$ của $f$ là đóng và hàm lồi (convex function), thực sự/đúng đắn khi và chỉ khi $f$ là thực sự/đúng đắn. Hơn nữa, $(cl(f))^{*} = f^{*}$, và $f^{**} =$ cl(f). Như hệ quả của Mệnh đề 51.27, nó có thể được được hiển thị rằng
$$f^{*} (y) =\sup(\langle x, y\rangle -f(x)).$$
$$x\in relint(dom(f))$$
Kết quả sau đây được chứng minh trong Rockafellar $[143]$ (Định lý 23.5).

<!-- PAGE 1888 -->
$$\mathbb{R}^{n} \mathbb{R}^{n}$$

> **Mệnh đề 51.28.** Với mọi thực sự/đúng đắn hàm lồi (convex function) $f$ trên và với mọi vectơ $x \in$,
$$\mathbb{R}^{n}$$
Sau đây các điều kiện trên vectơ $y \in$ là tương đương.
() $y \in \partial$ f(x).
$(b)$ hàm $\langle z, y\rangle$ - f(z) đạt được của nó cận trên đúng (supremum) trong $z$ tại $z = x$.
$(c)$ f(x) $+ f^{*} (y) \le \langle x, y\rangle$.
$(d)$ f(x) $+ f^{*} (y) = \langle x, y\rangle$. Nếu (cl(f))(x) $=$ f(x), thì có ba nhiều hơn/thêm các điều kiện tất cả tương đương đến ở trên các điều kiện. $(a^{*}) x \in \partial f^{*} (y). (b^{*})$ hàm $\langle x, z\rangle$ - $f^{*} (z)$ đạt được của nó cận trên đúng (supremum) trong $z$ tại $z = y. (a^{**}) y \in \partial$ (cl(f))(x). sau đây các kết quả là các hệ quả của Mệnh đề 51.28; xem Rockafellar $[143]$ (Các hệ quả 23.5.1, 23.5.2, 23.5.3).

> **Hệ quả 51.29.** Với mọi thực sự/đúng đắn hàm lồi (convex function) $f$ trên $\mathbb{R}^{n}$, nếu $f$ là đóng, thì $y \in \partial$ f(x) khi và chỉ khi $x \in \partial f^{*} (y)$, với mọi $x, y \in \mathbb{R}^{n}$. Hệ quả 51.29 phát biểu sort của adjunction tính chất.

> **Hệ quả 51.30.** Với mọi thực sự/đúng đắn hàm lồi (convex function) $f$ trên $\mathbb{R}^{n}$, nếu $f$ là khả vi dưới tại $x \in \mathbb{R}^{n}$, thì (cl(f))(x) $=$ f(x) và $\partial$ (cl(f))(x) $= \partial$ f(x). Hệ quả 51.30 chỉ ra rằng bao đóng (closure) của thực sự/đúng đắn hàm lồi (convex function) $f$ agrees với $f$ whereever $f$ là khả vi dưới.

> **Hệ quả 51.31.** Với mọi thực sự/đúng đắn hàm lồi (convex function) $f$ trên $\mathbb{R}^{n}$, với mọi khác rỗng đóng lồi
$$\mathbb{R}^{n}\mathbb{R}^{n}\mathbb{R}^{n}$$
Tập con $C$ của, với mọi $y \in$, tập hợp $\partial \delta^{*}$ (y|C) $= \partial I_{C}^{*}(y)$ bao gồm của các vectơ $x \in$ (nếu bất kỳ) ở đâu dạng tuyến tính (linear form) $z \mapsto \langle z, y\rangle$ đạt được của nó cực đại trên $C$. Có một khái niệm của xấp xỉ dưới gradien (subgradient) mà hóa ra là hữu ích trong tối ưu hóa lý thuyết; xem Bertsekas $[19, 17]$.
$$\mathbb{R}^{n} \mathbb{R}$$

> **Định nghĩa 51.17.** Cho $f$: $\to  \cup {+\infty$ } là bất kỳ thực sự/đúng đắn hàm lồi (convex function). Với mọi $\epsilon  > 0$,
$$\mathbb{R}^{n}\mathbb{R}^{n}$$
Với mọi $x \in$, nếu f(x) là hữu hạn, thì $\epsilon$ -dưới gradien (subgradient) của $f$ tại $x$ là bất kỳ vectơ $u \in$ sao cho
$$f(z) \ge f(x) -\epsilon  + \langle z -x, u\rangle ,for all z \in \mathbb{R}^{n}.$$
Xem Hình 51.23. Tập hợp tất cả $\epsilon$ -các dưới gradien của $f$ tại $x$ được ký hiệu là $\partial_{\epsilon}$ f(x) và được gọi là $\epsilon$ -vi phân dưới (subdifferential) của $f$ tại $x$.

<!-- PAGE 1889 -->
$$= 1/2$$
$$u$$
$$+f(x)$$
$$,u> >$$
$$<z-x + <z-x,u$$
$$(0,3/2)(0,3/2) -\varepsilon$$
$$(1,1)(1,1)f(x)$$
$$\varepsilon$$
$$(1/2,-1)(1/2,-1)$$
$$subgradient\varepsilon -subgradient$$

![Figure 51.23](../../assets/ch51/fig_51_23.png)

**Hình 51.23:** Cho $f$: $\mathbb{R} \to \mathbb{R}\cup {-\infty , +\infty$ } là từng khúc hàm được định nghĩa bởi f(x) $= x+1$ cho $x \ge 1$ và f(x) $= -_{2}^{1}x +_{2}^{3}$ cho $x < 1$. Của nó trên đồ thị (epigraph) là shaded xanh lam miền trong $\mathbb{R}^{2}$. $line^{1} (x$ - $1) + 1$ (với chuẩn tắc/bình thường $(_{2}^{1}, -1)$ là tựa/hỗ trợ siêu phẳng (hyperplane) đến đồ thị của f(x) tại $(1, 1)^{2}$ trong khi $line_{2}^{1} (x$ - $1) + 1$ - $\epsilon$ là siêu phẳng (hyperplane) liên kết với $\epsilon$ -dưới gradien (subgradient) tại $x = 1$ và chỉ ra rằng $u =_{2}^{1}  \in \partial_{\epsilon}$ f(x). tập hợp $\partial_{\epsilon}$ f(x) có thể được được định nghĩa theo liên hợp của hàm $h_{x}$ cho trước bởi
$$h_{x}(y) = f(x + y) -f(x),for all y \in \mathbb{R}^{n}.$$
$$\mathbb{R}^{n} \mathbb{R}$$

> **Mệnh đề 51.32.** Cho $f$: $\to \cup {+\infty$ } là bất kỳ thực sự/đúng đắn hàm lồi (convex function). Với mọi $\epsilon  > 0$, nếu $h_{x}$ được cho bởi
$$h_{x}(y) = f(x + y) -f(x),for all y \in \mathbb{R}^{n},$$
Thì
$$h_{x}^{*}(y) = f^{*}(y) + f(x) -\langle x, y\rangle for all y \in \mathbb{R}^{n}$$
Và
$$\mathbb{R}^{n}$$
$$\partial_{\epsilon} f(x) = {u \in | h_{x}^{*}(u) \le \epsilon }.$$

*Chứng minh.* Ta có
$$h_{x}^{*}(y) = \sup(\langle y, z\rangle -h_{x}(z))$$
$$z\in \mathbb{R} n$$
$$= \sup(\langle y, z\rangle -f(x + z) + f(x))$$
$$z\in \mathbb{R} n$$
$$=\sup(\langle y, x + z\rangle -f(x + z) -\langle y, x\rangle + f(x))$$
$$x+z\in \mathbb{R} n$$
$$= f^{*} (y) + f(x) -\langle x, y\rangle .$$
Nhận thấy rằng $u \in \partial_{\epsilon}$ f(x) khi và chỉ khi với mọi $y \in \mathbb{R}^{n}$,
$$f(x + y) \ge f(x) -\epsilon  + \langle y, u\rangle$$
