# Một chiều Bài toán: Bending của Beam


<!-- PAGE 691 -->
Chương $19$ Variational Xấp xỉ của Boundary-Value Các bài tập; Giới thiệu đến Phương pháp phần tử hữu hạn (FEM)

## 19.1 Một chiều Bài toán: Bending của Beam

Xét beam của unit độ dài được hỗ trợ/giá (support) tại của nó kết thúc trong $0$ và $1$, stretched dọc theo của nó trục bởi buộc $P$, và subjected đến transverse load f(x)dx trên mỗi phần tử dx, như được minh họa trong Hình 19.1.
$$01$$
$$dx$$
$$-PP$$
$$f(x)dx$$
$$Figure 19.1: Vertical deflection of a beam$$
Bending moment u(x) tại absissa $x$ là nghiệm của biên (boundary) bài toán (BP) của tạo thành
$$-u''(x) + c(x)u(x) = f(x),0 < x < 1$$
$$u(0) = \alpha$$
$$u(1) = \beta ,$$
$$691$$

<!-- PAGE 692 -->
Ở đâu c(x) $= P/(EI(x))$, ở đâu $E$ là Young’s môđun/độ lớn của material của mà beam được tạo và I(x) là chính moment của inertia của cross-section của beam tại abcissa $x$, và với $\alpha  = \beta  = 0$. Cho bài toán này, ta có thể giả sử rằng c(x) $\ge 0$ với mọi $x \in [0, 1]$.
Nhận xét: đứng deflection w(x) của beam và bending moment u(x) là related bởi phương trình
$$EI$$
$$u(x) = - \frac{d^{2}w}{dx^{2}} .$$
Nếu ta seek nghiệm $u \in C^{2}([0, 1])$, nghĩa là, hàm có thứ nhất và thứ hai các đạo hàm tồn tại và là liên tục, thì nó có thể được được hiển thị rằng bài toán có duy nhất nghiệm (giả sử $c$ và $f$ là liên tục các hàm trên $[0, 1])$. Ngoại trừ trong rất rare các tình huống, bài toán này có không có closed-form nghiệm, do đó ta là đã dẫn đến đến seek các xấp xỉ của các nghiệm. Một một cách đến tiến hành là để sử dụng hữu hạn difference phương pháp, ở đâu ta discretize bài toán và thay thế các đạo hàm bởi differences. Một cái khác cách là để sử dụng variational cách tiếp cận. Trong điều này cách tiếp cận, ta suy ra somewhat đáng ngạc nhiên đường đi trong mà ta đến lên với so-called “yếu formulation” của bài toán, bằng cách sử dụng mẹo/kỹ thuật based trên integrating bởi các phần! Thứ nhất, cho chúng ta nhận thấy rằng ta có thể luôn luôn giả sử rằng $\alpha  = \beta  = 0$, bởi nhìn cho nghiệm của tạo thành u(x) $-(\alpha (1 -x) + \beta x)$. Điều này hóa ra là then chốt khi ta integrate bởi các phần. Có nhiều tinh tế toán học chi tiết liên quan để tạo những gì suy ra chặt chẽ, nhưng ở đây, ta sẽ lấy “relaxed” cách tiếp cận. Thứ nhất, ta cần đến specify không gian của “yếu các nghiệm.” Điều này sẽ là không gian vectơ (vector space) $V$ của liên tục các hàm $f$ trên $[0, 1]$, với f(0) $=$ f(1) $= 0$, và mà là từng khúc một cách liên tục khả vi (differentiable) trên $[0, 1]$. Điều này có nghĩa là có một hữu hạn số của các điểm $x_{0}, \dots  , x_{N+1}$ với $x_{0} = 0$ và $x_{N+1} = 1$, sao cho $f'(x_{i})$ là undefined cho $i = 1, \dots  , N$, nhưng ngược lại f' được định nghĩa và liên tục trên mỗi khoảng/đoạn $(x_{i}, x_{i+1})$ cho $i = 0, \dots  , N.^{1}$ không gian $V$ trở thành Euclidean không gian vectơ (vector space) dưới tích vô hướng (inner product)
$$\langle f, g\rangle_{V}  = \int_{0}^{}  1(f(x)g(x) + f' (x)g'(x))dx,$$
Với mọi $f, g \in V$. liên kết chuẩn (norm) là
$$\|f\|_{V} = \int_{0}^{}  1/2.$$
$$\begin{pmatrix} 1 \\ (f(x)^{2}+ f'(x)^{2})dx \end{pmatrix}$$
Giả sử rằng $u$ là nghiệm của của ta ban đầu biên (boundary) bài toán (BP), sao cho
$$-u''(x) + c(x)u(x) = f(x),0 < x < 1$$
$$u(0) = 0$$
$$u(1) = 0.$$
$\overline{1}\overline{We} \overline{also} \overline{assume} \overline{that} \overline{f}'\overline{(}\overline{x}\overline{)} \overline{has} \overline{a} \overline{limit}$ khi $x$ tiến tới đến biên (boundary) của $(x_{i}, x_{i+1})$.

<!-- PAGE 693 -->
Nhân vi phân phương trình bởi bất kỳ tùy ý test hàm $v \in V$, thu được
$$-u''(x)v(x) + c(x)u(x)v(x) = f(x)v(x),(*)$$
Và integrate phương trình này! Ta thu được
$$- \int_{0}^{}  1u''(x)v(x)dx + \int_{0}^{}  1c(x)u(x)v(x)dx = \int_{0}^{}  1f(x)v(x)dx.(\dagger )$$
Bây giờ, mẹo/kỹ thuật là để sử dụng phép lấy tích phân bởi các phần trên số hạng thứ nhất. Nhắc lại rằng
$$(u'v)'= u''v + u'v',$$
Và là careful về discontinuities, viết
$$\int_{0}^{}  1u''(x)v(x)dx = \sum_{i=0}^{N}  \int_{x}^{}  xi+1u''(x)v(x)dx.$$
$$i$$
Bằng cách sử dụng phép lấy tích phân bởi các phần, ta có
$$\int_{x}^{}  xi+1u''(x)v(x)dx = \int_{x}^{}  xi+1(u'(x)v(x))'dx - \int_{x}^{}  xi+1u'(x)v'(x)dx$$
$$iii$$
$$= [u'(x)v(x)]_{x=xi}^{x=xi+1}- \int_{x}^{}  xi+1u'(x)v'(x)dx$$
$$i$$
$$= u'(x_{i+1})v(x_{i+1}) -u'(x_{i})v(x_{i}) - \int_{x}^{}  xi+1u'(x)v'(x)dx.$$
$$i$$
Suy ra rằng
$$\int_{0}^{}  1u''(x)v(x)dx = \sum_{i=0}^{N}  \int_{x}^{}  xi+1u''(x)v(x)dx$$
$$i$$
$$= \sum_{i=0}^{N}  \begin{pmatrix} xi+1 \\ u'(x_{i+1})v(x_{i+1}) -u'(x_{i})v(x_{i}) - & u'(x)v'(x)dx \\ i \\ 1 \end{pmatrix} \int_{x}^{}$$
$$= u'(1)v(1) -u'(0)v(0) - \int_{0}^{}  u'(x)v'(x)dx.$$
Tuy nhiên, test hàm $v$ thỏa mãn biên (boundary) các điều kiện v(0) $=$ v(1) $= 0$ (nhắc lại rằng $v \in V$), do đó ta thu được
$$\int_{0}^{}  1u''(x)v(x)dx = - \int_{0}^{}  1u'(x)v'(x)dx.$$
Hệ quả là, phương trình $(\dagger$) trở thành
$$\int_{0}^{}  1u'(x)v'(x)dx + \int_{0}^{}  1c(x)u(x)v(x)dx = \int_{0}^{}  1f(x)v(x)dx,$$

<!-- PAGE 694 -->
Hoặc
$$\int_{0}^{}  1(u'v' + cuv)dx = \int_{0}^{}  1fvdx,for all v \in V.(**)$$
Do đó, nó là tự nhiên đến giới thiệu dạng song tuyến tính (bilinear form): $V \times  V \to \mathbb{R}$ cho trước bởi
$$a(u, v) = \int_{0}^{}  1(u'v' + cuv)dx,for all u, v \in V ,$$
Và dạng tuyến tính (linear form) $f$: $V \to \mathbb{R}$ cho trước bởi
$$e$$
$$f(v) = \int_{0}^{}  1f(x)v(x)dx,for all v \in V .$$
$$e$$
Thì, (**) trở thành
$$a(u, v) =f(v),for all v \in V.$$
$$e$$
Ta cũng giới thiệu năng lượng hàm $J$ cho trước bởi
$$J(v) = \frac{1}{2} a(v, v) -fe(v)v \in V.$$
Thì, ta có kết quả sau định lý.

> **Định lý 19.1.** Cho $u$ là bất kỳ nghiệm của biên (boundary) bài toán (BP).
$(1)$ Thì ta có
$$a(u, v) =f(v),for all v \in V,(WF)$$
$$e$$
Ở đâu
$$a(u, v) = \int_{0}^{}  1(u'v' + cuv)dx,for all u, v \in V ,$$
Và
$$f(v) = \int_{0}^{}  1f(x)v(x)dx,for all v \in V .$$
$$e$$
$(2)$ Nếu c(x) $\ge 0$ với mọi $x \in [0, 1]$, thì hàm $u \in V$ là nghiệm của $(WF)$ khi và chỉ khi $u$ cực tiểu hóa J(v), nghĩa là,
$$J(u) = \inf J(v),$$
$$v\in V$$
Với
$$J(v) = \frac{1}{2} a(v, v) -fe(v)v \in V.$$
Hơn nữa, $u$ là duy nhất.

<!-- PAGE 695 -->

*Chứng minh.* Ta đã được chứng minh $(1)$. để chứng minh $(2)$, thứ nhất ta chỉ ra rằng
$$\|v\|_{V}^{2} \le 2a(v, v),for all v \in V.$$
Cho điều này, nó suffices để chứng minh rằng
$$\|v\|_{V}^{2} \le 2 \int_{0}^{}  1(f' (x))^{2}dx,for all v \in V.$$
Tuy nhiên, bởi Cauchy-Schwarz cho các hàm, với mọi $x \in [0, 1]$, ta có
$$|v(x)| = \int_{0}^{}  xv'(t)dt



$\le \int_{0}^{}$ 1|v'(t)|dt $\le \int_{0}^{}  1/2,$$$
$$\begin{pmatrix} 1 \\ |v'(t)|^{2}dt \end{pmatrix}$$
Và do đó
$$\|v\|_{V}^{2} = \int_{0}^{}  1((v(x))^{2} + (v'(x))^{2})dx \le 2 \int_{0}^{}  1(v'(x))^{2}dx \le 2a(v, v),$$
Vì
$$a(v, v) = \int_{0}^{}  1((v')^{2} + cv^{2})dx.$$
Tiếp theo, nó là dễ để kiểm tra rằng
$$J(u + v) -J(u) = a(u, v) -fe(v) + \frac{1}{2} a(v, v),for all u, v \in V .$$
Thì, nếu $u$ là nghiệm của $(WF)$, ta suy ra rằng
$$J(u + v) -J(u) = \frac{1}{2} a(v, v) \ge \frac{1}{4} \|v\|_{V} \ge 0for all v \in V.$$
Vì (u, $v)$ - f(v) $= 0$ với mọi $v \in V$. Vì vậy, $J$ đạt được minimun cho $u$.
$$e$$
Ta cũng có
$$J(u + \theta v) -J(u) = \theta (a(u, v) -f(v)) + \frac{\theta^{2}}{2} a(v, v)for all \theta  \in \mathbb{R},$$
Và do đó J(u $+ \theta v)$ - J(u) $\ge 0$ với mọi $\theta  \in \mathbb{R}$. Hệ quả là, nếu $J$ đạt được cực tiểu cho $u$, thì (u, $v) =$ f(v), mà có nghĩa là $u$ là nghiệm của $(WF)$.
$$e$$
Cuối cùng, giả sử rằng c(x) $\ge 0$, ta khẳng định rằng nếu $v \in V$ và $v \neq  0$, thì (v, $v) > 0$. Điều này là bởi vì nếu (v, $v) = 0$, vì
$$\|v\|_{V}^{2} \le 2a(v, v)for all v \in V,$$
Ta sẽ có $\|v\|_{V} = 0$, nghĩa là, $v = 0$. Thì, nếu $v \neq  0$, từ
$$J(u + v) -J(u) = \frac{1}{2} a(v, v)for all v \in V$$
Ta xem rằng J(u $+ v) >$ J(u), do đó cực tiểu $u$ là duy nhất

<!-- PAGE 696 -->
Định lý 19.1 chỉ ra rằng mọi nghiệm $u$ của biên (biên (boundary)) của chúng ta bài toán (BP) là nghiệm (thực ra, duy nhất) của phương trình (WF). phương trình (WF) được gọi là yếu tạo thành hoặc variational phương trình liên kết với biên (boundary) bài toán. Điều này ý tưởng đến derive các phương trình này là do Ritz và Galerkin. Bây giờ, tự nhiên câu hỏi là liệu variational phương trình (WF) có nghiệm, và liệu nghiệm này, nếu nó tồn tại, là cũng nghiệm của biên (boundary) bài toán (nó phải thuộc đến $C^{2}([0, 1])$, mà là far từ hiển nhiên). Thì, (BP) và (WF) sẽ là tương đương. Một số fancy các công cụ của giải tích/phân tích có thể được được sử dụng để chứng minh các phần tử này assertions. thứ nhất difficulty là rằng không gian vectơ (vector space) $V$ là không phải không gian của các nghiệm, bởi vì trong thứ tự cho variational bài toán đến có nghiệm, nó phải là đầy đủ. Do đó, ta phải xây dựng đầy đủ hóa của không gian vectơ (vector space) $V$. Điều này có thể được được thực hiện và ta thu được Sobolev không gian $H_{0}^{1}(0, 1)$. Thì, câu hỏi của regularity của “yếu nghiệm” có thể cũng là tackled. Ta sẽ không worry về tất cả điều này. Thay vì, cho chúng ta tìm các xấp xỉ của bài toán (WF). Thay vì của bằng cách sử dụng không gian vectơ vô hạn chiều $V$, ta xét hữu hạn chiều các không gian con $V_{a}$ (với $dim(V_{a}) = n)$ của $V$, và ta xét rời rạc bài toán: Tìm hàm $u^{(a)} \in V_{a}$, sao cho
$$a(u^{(a)}, v) =f(v),for all v \in V_{a}.(DWF)$$
$$e$$
Vì $V_{a}$ là hữu hạn dimensional (có số chiều $n)$, cho chúng ta chọn cơ sở (basis) của các hàm $(w_{1}, \dots  , w_{n})$ trong $V_{a}$, sao cho mọi hàm $u \in V_{a}$ có thể ta được viết như
$$u = u_{1}w_{1} + \cdots  + u_{n}w_{n}.$$
Thì, phương trình (DWF) nghiệm đúng khi và chỉ khi
$$a(u, w_{j}) =f(w_{j}),j = 1, \dots  , n,$$
$$e$$
Và bởi plugging $u_{1}w_{1} + \cdots  + u_{n}w_{n}$ cho $u$, ta thu được hệ của $k$ các phương trình tuyến tính
$$\sum_{i=1}^{n}  a(w_{i}, w_{j})u_{i} = fe(w_{j}),1 \le j \le n.$$
Bởi vì (v, $v) \ge_{2}^{1}  \|v\|_{Va}$, dạng song tuyến tính (bilinear form) là đối xứng xác định dương (SPD), và do đó ma trận $(a(w_{i}, w_{j}))$ là đối xứng xác định dương (SPD), và do đó khả nghịch. Vì vậy, (DWF) có nghiệm cho trước bởi hệ phương trình tuyến tính! Từ thực tế điểm của quan điểm, ta có để tính các tích phân
$$a_{ij} = a(w_{i}, w_{j}) = \int_{0}^{}  1(w_{i}'w_{j}' + cw_{i}w_{j})dx,$$
Và
$$b_{j} =f(w_{j}) = \int_{0}^{}  1f(x)w_{j}(x)dx.$$
$$e$$

<!-- PAGE 697 -->
Tuy nhiên, nếu cơ sở (basis) các hàm là đơn giản đủ, điều này có thể được được thực hiện “bởi hand.” Ngược lại, số phép lấy tích phân các phương pháp phải được sử dụng, nhưng có một số tốt các một. Cho chúng ta cũng nhận xét rằng chứng minh của Định lý 19.1 cũng chỉ ra rằng duy nhất nghiệm của
(DWF) là duy nhất điểm cực tiểu hóa của $J$ trên tất cả các hàm trong $V_{a}$. Nó là cũng khả dĩ/có thể đến compare xấp xỉ nghiệm $u^{(a)} \in V_{a}$ với chính xác nghiệm $u \in V$.

> **Định lý 19.2.** Giả sử c(x) $\ge 0$ với mọi $x \in [0, 1]$. Với mọi hữu hạn chiều không gian con $V_{a} (dim(V_{a}) = n)$ của $V$, với mọi cơ sở (basis) $(w_{1}, \dots  , w_{n})$ của $V_{a}$, các tính chất sau đây đúng:
$(1)$ Tồn tại duy nhất một hàm $u^{(a)} \in V_{a}$ sao cho
$$a(u^{(a)}, v) =f(v),for all v \in V_{a},(DWF)$$
$$e$$
Và nếu $u^{(a)} = u_{1}w_{1} + \cdots  + u_{n}w_{n}$, thì $u = (u_{1}, \dots  , u_{n})$ là nghiệm của hệ phương trình tuyến tính
$$Au = b,(*)$$
Với $A = (a_{ij}) = (a(w_{i}, w_{j}))$ và $b_{j} = f(w_{j}), 1 \le i, j \le n$. Hơn nữa, ma trận
$$e$$
$A = (a_{ij})$ là đối xứng xác định dương (SPD).
$(2)$ duy nhất nghiệm $u^{(a)} \in V_{a}$ của $(DWF)$ là duy nhất điểm cực tiểu hóa của $J$ trên $V_{a}$, nghĩa là,
$$J(u^{(a)}) = \inf J(v),$$
$$v\in Va$$
$(3)$ Có một hằng số $C$ độc lập của $V_{a}$ và của duy nhất nghiệm $u \in V$ của $(WF)$, sao cho
$$u -u_{V}^{(a)}

$\le C \inf \|u -v\|_{V}$.$$
$$v\in Va$$
Ta được chứng minh $(1)$ và $(2)$, nhưng ta sẽ bỏ qua chứng minh của $(3)$ mà có thể được tìm thấy trong Ciarlet $[41]$. Cho chúng ta bây giờ cho các ví dụ của các không gian con $V_{a}$ được sử dụng trong thực tế. Chúng thường bao gồm của từng khúc đa thức các hàm. Chọn số nguyên $N \ge 1$ và subdivide $[0, 1]$ vào $N + 1$ các khoảng $[x_{i}, x_{i+1}]$, ở đâu
$$x_{i} = hi,h = \frac{1}{N+ 1} ,i = 0, \dots  , N + 1.$$
Ta sẽ sử dụng sau đây sự kiện: mọi đa thức P(x) của bậc 2m $+ 1 (m \ge 0)$ là hoàn toàn được xác định bởi các giá trị của nó cũng như các giá trị của của nó thứ nhất $m$ các đạo hàm tại hai phân biệt các điểm $\alpha , \beta  \in \mathbb{R}$.

<!-- PAGE 698 -->
Có khác nhau các cách để chứng minh điều này. Một cách là để sử dụng Bernstein cơ sở (basis), bởi vì đạo hàm thứ $k$ của đa thức được cho bởi công thức theo của nó control các điểm. Ví dụ, cho $m = 1$, mọi bậc $3$ đa thức có thể được viết dưới dạng
$$P(x) = (1 -x)^{3}b_{0} + 3(1 -x)^{2}x b_{1} + 3(1 -x)x^{2}b_{2} + x^{3}b_{3},$$
Với $b_{0}, b_{1}, b_{2}, b_{3} \in \mathbb{R}$, và ta đã chỉ ra rằng
$$P' (0) = 3(b_{1} -b_{0})$$
$$P' (1) = 3(b_{3} -b_{2}).$$
Cho trước P(0) và P(1), ta xác định $b_{0}$ và $b_{3}$, và từ P' $(0)$ và P' $(1)$, ta xác định $b_{1}$ và $b_{2}$. Nói chung, cho đa thức của bậc $m$ được viết như
$$P(x) = \sum_{j=0}^{m}  b_{j}B_{j}^{m} (x)$$
Theo Bernstein cơ sở (basis) $(B_{0}^{m} (x), \dots  , B_{m}^{m}(x))$ với
$$B_{j}^{m} (x) = \begin{pmatrix} m \\ j \end{pmatrix} (1 -x)^{m-j}x^{j},$$
Nó có thể được được hiển thị rằng đạo hàm thứ $k$ của $P$ tại không được cho bởi
$$P^{(k)}(0) = m(m -1) \cdots  (m -k + 1) \begin{pmatrix} k \\ i \end{pmatrix} \sum_{i=0}^{k}  \begin{pmatrix} (-1)^{k-i}b_{i} \end{pmatrix} ,$$
Và có một đồng dạng công thức cho $P^{(k)} (1)$. Thực sự, ta cần để sử dụng Bernstein cơ sở (basis) của các đa thức $B_{k}^{m} [r, s]$, ở đâu
$$x^{m-j}r^{j}$$
$$B_{j}^{m} [r, s](x) = \begin{pmatrix} m \\ j \end{pmatrix} \begin{pmatrix} s - \\ s -r \end{pmatrix} \begin{pmatrix} x - \\ s -r \end{pmatrix} ,$$
Với $r < s$, trong mà trường hợp
$$- \cdots  -$$
$$P^{(k)} (0) = \frac{m(m1) (mk + 1)}{(s -r)^{k}} \begin{pmatrix} k \\ i \end{pmatrix} \sum_{i=0}^{k}  \begin{pmatrix} (-1)^{k-i}b_{i} \end{pmatrix} ,$$
Với đồng dạng công thức cho $P^{(k)} (1)$. Trong trường hợp của chúng ta, ta tập hợp $r = x_{i}, s = x_{i+1}$. Bây giờ, nếu 2m $+ 2$ các giá trị
$$P(0), P^{(1)} (0), \dots  , P^{(m)} (0), P(1), P^{(1)} (1), \dots  , P^{(m)} (1)$$

<!-- PAGE 699 -->
Là cho trước, ta thu được tam giác hệ rằng xác định một cách duy nhất 2m $+ 2$ control các điểm $b_{0}, \dots  , b_{2m+1}$. Nhắc lại rằng $C^{m}([0, 1])$ ký hiệu tập hợp của $C^{m}$ các hàm $f$ trên $[0, 1]$, mà có nghĩa là $f, f^{(1)}, \dots  , f^{(m)}$ tồn tại là là liên tục trên $[0, 1]$. Ta định nghĩa không gian vectơ (vector space) $V_{N}^{m}$ như không gian con của $C^{m}([0, 1])$ bao gồm của tất cả các hàm $f$ sao cho $1$. f(0) $=$ f(1) $= 0. 2$. thu hẹp của $f$ đến $[x_{i}, x_{i+1}]$ là đa thức của bậc 2m $+ 1$, cho $i = 0, \dots  , N$. Nhận thấy rằng các hàm trong $V_{N}^{0}$ là từng khúc afin các hàm $f$ với f(0) $=$ f(1) $= 0$; ví dụ được hiển thị trong Hình 19.2.
$$y$$
$$x$$
$$0ih1$$
$$Figure 19.2: A piecewise affine function$$
Không gian này có số chiều $N$, và cơ sở (basis) bao gồm của “hat các hàm” $w_{i}$, ở đâu chỉ hai nonflat các phần của đồ thị của $w_{i}$ là đường thẳng các đoạn thẳng từ $(x_{i-1}, 0)$ đến $(x_{i}, 1)$, và từ $(x_{i}, 1)$ đến $(x_{i+1}, 0)$, cho $i = 1, \dots  , N$, xem Hình 19.3. cơ sở (basis) các hàm $w_{i}$ có nhỏ hỗ trợ/giá (support), mà là tốt bởi vì trong việc tính toán các tích phân cho $a(w_{i}, w_{j})$, ta tìm rằng ta thu được ma trận ba đường chéo (tridiagonal matrix). Chúng cũng có đẹp tính chất rằng mọi hàm $v \in V_{N}^{0}$ có sau đây biểu thức trên cơ sở (basis) $(w_{i})$:
$$v(x) = \sum_{i=1}^{N}  v(ih)w_{i}(x),x \in [0, 1].$$

<!-- PAGE 700 -->
$$y$$
$$w$$
$$i$$
$$x$$
$$(i -1)hih(i + 1)h$$
$$Figure 19.3: A basis “hat function”$$
Nói chung, nó nó không khó để xem rằng $V_{N}^{m}$ có số chiều mN $+$ 2(m - $1)$. Đi quay lại đến bài toán của chúng ta (bending của beam), giả sử rằng $c$ và $f$ là hằng số các hàm, nó là không khó để chỉ ra rằng hệ phương trình tuyến tính (*) trở thành
$$\frac{1}{h} \begin{pmatrix} 2 +_{3}^{2c}h^{2} & -1 +_{6}^{c}h^{2} \\ -1 +_{6}^{c}h^{2} & 2 +_{3}^{2c}h^{2} & -1 +_{6}^{c}h^{2} \\ \ddots & \ddots & \ddots \\ -1 +_{6}^{c}h^{2} & 2 +_{3}^{2c}h^{2} & -1 +_{6}^{c}h^{2} \\ 1 +_{6}^{c}h^{2} & 2 +_{3}^{2c}h^{2} \end{pmatrix} \begin{pmatrix} u_{1} \\ u_{2} \\ \vdots \\ u_{N-1} \\ u_{N} \end{pmatrix} = h \begin{pmatrix} f \\ f \\ \vdots \\ f \\ f \end{pmatrix} .$$
$$-$$
Ta có thể cũng tìm cơ sở (basis) của 2N $+ 2$ bậc ba các hàm cho $V_{N}^{1}$ bao gồm của các hàm với nhỏ hỗ trợ/giá (support). cơ sở (cơ sở (basis)) này bao gồm của $N$ các hàm $w_{i}^{0}$ và của $N + 2$ các hàm $w_{i}^{1}$

<!-- PAGE 701 -->
Một cách duy nhất được xác định bởi sau đây các điều kiện:
$$w_{i}^{0} (x_{j}) = \delta_{ij} ,1 \le j \le N, 1 \le i \le N$$
$$(w_{i}^{0} )'(x_{j}) = 0,0 \le j \le N + 1, 1 \le i \le N$$
$$w_{i}^{1} (x_{j}) = 0,1 \le j \le N, 0 \le i \le N + 1$$
$$(w_{i}^{1} )'(x_{j}) = \delta_{ij} ,0 \le j \le N + 1, 0 \le i \le N + 1$$
Với $\delta_{ij}  = 1$ khi và chỉ khi $i = j$ và $\delta_{ij}  = 0$ nếu $i \neq  j$. Một số của các hàm này là displayed trong Hình 19.4. hàm $w_{i}^{0}$ là cho trước một cách tường minh bởi
$$w_{i}^{0} (x) = \frac{1}{h^{3}} (x -(i -1)h)^{2}((2i + 1)h -2x),(i -1)h \le x \le ih,$$
$$w_{i}^{0} (x) = \frac{1}{h^{3}} ((i + 1)h -x)^{2}(2x -(2i -1)h),ih \le x \le (i + 1)h,$$
Cho $i = 1, \dots  , N$. hàm $w_{j}^{1}$ là cho trước một cách tường minh bởi
$$w_{j}^{1}(x) = - \frac{1}{h^{2}} (ih -x)(x -(i -1)h)^{2},(i -1)h \le x \le ih,$$
Và
$$w_{j}^{1}(x) = \frac{1}{h^{2}} ((i + 1)h -x)^{2}(x -ih),ih \le x \le (i + 1)h,$$
Cho $j = 0, \dots  , N + 1$. Hơn nữa, với mọi hàm $v \in V_{N}^{1}$, ta có
$$v(x) = \sum_{i=1}^{N}  v(ih)w_{i}^{0} (x) + \sum_{j=0}^{N+1}  v'jih)w_{j}^{1}(x),x \in [0, 1].$$
Nếu ta thứ tự cơ sở (cơ sở (basis)) này các hàm như
$$w_{0}^{1}, w_{1}^{0}, w_{1}^{1}, w_{2}^{0}, w_{2}^{1}, \dots  , w_{N}^{0}, w_{N}^{1}, w_{N+1}^{1},$$
Ta tìm rằng nếu $c = 0$, ma trận $A$ của hệ (*) là ba đường chéo bởi các khối, ở đâu các khối là $2 \times  2, 2 \times  1$, hoặc $1 \times  2$ các ma trận, và với đơn lẻ các phần tử (entries) trong đỉnh/trên trái và đáy/dưới phải góc. khác nhau thứ tự của cơ sở (basis) các vectơ sẽ mess lên ba đường chéo khối cấu trúc của $A$. Ta để lại chi tiết như một bài tập. Cho chúng ta bây giờ lấy quick nhìn tại hai chiều bài toán, bending của elastic membrane.
