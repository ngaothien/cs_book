# Xạ ảnh Các hệ quy chiếu


<!-- PAGE 884 -->
$$z = 1$$
$$c$$
$$D$$
$$1D 2$$
$$-$$
$$H$$
$$O2$$
$$H$$
$$1$$
$$H$$
$$Figure 26.6: A pencil of lines through c in the hyperplane model of \mathbb{RP}^{2}$$
P(E), i.e., tập hợp tất cả các siêu phẳng chứa một số cho trước xạ ảnh không gian con $W =$ p(V)
$$\mathbb{RP}^{3} \mathbb{R}^{4}$$
Có số chiều $n$ - $2$. Cho $n = 3$, chùm (pencil) của các mặt phẳng trong $= P($) là tập hợp tất cả các mặt phẳng (trong $\mathbb{RP}^{3})$ chứa một số cho trước đường thẳng $W$. Khác các ví dụ của unusual các không gian xạ ảnh và các chùm sẽ là cho trước trong Mục 26.4. Tiếp theo, ta định nghĩa xạ ảnh analogues của các cơ sở (hoặc các hệ quy chiếu) và các ánh xạ tuyến tính (linear maps).

## 26.4 Xạ ảnh Các hệ quy chiếu

Như tất cả tốt các khái niệm trong xạ ảnh hình học, khái niệm của xạ ảnh hệ quy chiếu (frame) hóa ra là một cách duy nhất được định nghĩa sai khác một vô hướng.

> **Định nghĩa 26.3.** Cho trước không tầm thường không gian vectơ (vector space) $E$ có số chiều $n+1$, họ $(a_{i})_{1\le i\le n+2}$ của $n + 2$ các điểm của không gian xạ ảnh (projective space) P(E) là xạ ảnh hệ quy chiếu (frame) (hoặc cơ sở (basis)) của P(E) nếu tồn tại một cơ sở (basis) $(e_{1}, \dots  , e_{n+1})$ của $E$ sao cho $a_{i} = p(e_{i})$ cho $1 \le i \le n + 1$, và $a_{n+2} = p(e_{1} + \cdots  + e_{n+1})$. Bất kỳ cơ sở (basis) với ở trên tính chất được nói là liên kết với xạ ảnh hệ quy chiếu (frame) $(a_{i})_{1\le i\le n+2}$. justification của Định nghĩa 26.3 được cho bởi sau đây mệnh đề.

> **Mệnh đề 26.2.** Nếu $(a_{i})_{1\le i\le n+2}$ là xạ ảnh hệ quy chiếu (frame) của P(E), với mọi hai các cơ sở $(u_{1}, \dots , u_{n+1}), (v_{1}, \dots  , v_{n+1})$ của $E$ sao cho $a_{i} = p(u_{i}) = p(v_{i})$ cho $1 \le i \le n + 1$, và $a_{n+2} = p(u_{1} + \cdots  + u_{n+1}) = p(v_{1} + \cdots  + v_{n+1})$, có một khác không vô hướng (scalar) $\lambda  \in K$ sao cho $v_{i} = \lambda u_{i}$, với mọi $i, 1 \le i \le n + 1$.

*Chứng minh.* Vì $p(u_{i}) = p(v_{i})$ cho $1 \le i \le n + 1$, ở đó tồn tại một số khác không các vô hướng $\lambda_{i}  \in K$ sao cho $v_{i} = \lambda_{i} u_{i}$ với mọi $i, 1 \le i \le n + 1$. Vì ta phải có
$$p(u_{1} + \cdots  + u_{n+1}) = p(v_{1} + \cdots  + v_{n+1}),$$

<!-- PAGE 885 -->
Tồn tại một $\lambda  \neq  0$ sao cho
$$\lambda (u_{1} + \cdots  + u_{n+1}) = v_{1} + \cdots  + v_{n+1} = \lambda_{1} u_{1} + \cdots  + \lambda_{n+1} u_{n+1},$$
Và do đó ta có
$$(\lambda  -\lambda_{1} )u_{1} + \cdots  + (\lambda  -\lambda_{n+1} )u_{n+1} = 0,$$
Và vì $(u_{1}, \dots  , u_{n+1})$ là cơ sở (basis), ta có $\lambda_{i}  = \lambda$ với mọi $i, 1 \le i \le n + 1$, mà suy ra $\lambda_{1}  = \cdots  = \lambda_{n+1}  = \lambda$. Mệnh đề 26.2 chỉ ra rằng xạ ảnh hệ quy chiếu (frame) xác định duy nhất cơ sở (basis) của $E$, sai khác
(khác không) vô hướng (scalar). Điều này sẽ không nhất thiết là trường hợp nếu ta đã thực hiện không có điểm $a_{n+2}$ sao cho $a_{n+2} = p(u_{1} + \cdots  + u_{n+1})$. Khi $n = 0$, không gian xạ ảnh (projective space) bao gồm của đơn lẻ điểm, và ở đó là chỉ một xạ ảnh hệ quy chiếu (frame), cặp (,). Khi $n = 1$, không gian xạ ảnh (projective space) là đường thẳng, và xạ ảnh hệ quy chiếu (frame) bao gồm của bất kỳ ba đôi một phân biệt các điểm, $b, c$ trên điều này đường thẳng. Khi $n = 2$, không gian xạ ảnh (projective space) là mặt phẳng, và xạ ảnh hệ quy chiếu (frame) bao gồm của bất kỳ bốn phân biệt các điểm, $b, c, d$ sao cho, $b, c$ là các đỉnh của không suy biến tam giác và $d$ là không trên bất kỳ của các đường thẳng được xác định bởi các vế/cạnh của điều này tam giác. Các phần tử này các ví dụ của xạ ảnh các hệ quy chiếu được minh họa trong Hình 26.7. độc giả có thể dễ dàng tổng quát hóa đến cao hơn số chiều. Cho trước xạ ảnh hệ quy chiếu (frame) $(a_{i})_{1\le i\le n+2}$ của P(E), cho $(u_{1}, \dots  , u_{n+1})$ là cơ sở (basis) của $E$ liên kết với $(a_{i})_{1\le i\le n+2}$. Với mọi $a \in$ P(E), tồn tại một $u \in E -{0}$ sao cho
$$a = [u]_{\sim}= {\lambda u | \lambda  \in K -{0}},$$
Lớp tương đương (equivalence class) của $u$, và tập hợp
$${(x_{1}, \dots  , x_{n+1}) \in K^{n+1}| v = x_{1}u_{1} + \cdots  + x_{n+1}u_{n+1}, v \in [u]_{\sim}= a}$$
Của các tọa độ của tất cả các vectơ trong lớp tương đương (equivalence class) $[u]_{\sim}$ được gọi là tập hợp của thuần nhất các tọa độ của trên cơ sở (basis) $(u_{1}, \dots  , u_{n+1})$. Lưu ý rằng với mỗi thuần nhất tọa độ $(x_{1}, \dots  , x_{n+1})$ ta phải có $x_{i} \neq  0$ với một số $i, 1 \le i \le n + 1$, và bất kỳ hai thuần nhất các tọa độ $(x_{1}, \dots  , x_{n+1})$ và $(y_{1}, \dots  , y_{n+1})$ cho khác nhau bởi khác không vô hướng (scalar), i.e., tồn tại một $\lambda$ ̸ $= 0$ sao cho $y_{i} = \lambda x_{i}, 1 \le i \le n + 1$. Thuần nhất các tọa độ $(x_{1}, \dots  , x_{n+1})$ đôi khi được ký hiệu bởi $(x_{1}$: $\cdots$: $x_{n+1})$, chẳng hạn trong đại số hình học. Theo Mệnh đề 26.2, bất kỳ khác cơ sở (basis) $(v_{1}, \dots  , v_{n+1})$ liên kết với xạ ảnh hệ quy chiếu (frame) $(a_{i})_{1\le i\le n+2}$ các khác nhau từ $(u_{1}, \dots  , u_{n+1})$ bởi khác không vô hướng (scalar), mà suy ra rằng tập hợp của thuần nhất các tọa độ của $a \in$ P(E) trên cơ sở (basis) $(v_{1}, \dots  , v_{n+1})$ là đồng nhất đến tập hợp của thuần nhất các tọa độ của $a \in$ P(E) trên cơ sở (basis) $(u_{1}, \dots  , u_{n+1})$. Hệ quả là, ta có thể associate duy nhất tập hợp của thuần nhất các tọa độ đến mọi điểm $a \in$ P(E) đối với xạ ảnh hệ quy chiếu (frame) $(a_{i})_{1\le i\le n+2}$. Đối với điều này xạ ảnh hệ quy chiếu (frame), lưu ý rằng $a_{n+2}$ có thuần nhất các tọa độ $(1, \dots  , 1)$, và rằng $a_{i}$ có thuần nhất các tọa độ $(0, \dots  , 1, \dots  , 0)$, ở đâu $1$ là trong thứ $i$ position, ở đâu $1 \le i \le n + 1$. Ta summarize ở trên thảo luận trong sau đây định nghĩa.

<!-- PAGE 886 -->
$$0$$
$$P$$
$$Ka$$
$$1$$
$$PK$$
$$u1$$
$$a3a2$$
$$y = 1$$
$$\overline{a1}$$
$$u2$$
$$\overline{u}\overline{\infty}$$
$$2$$
$$PK$$
$$a3$$
$$a2z = 1$$
$$a1a4$$
$$u2$$
$$u1$$
$$z = 1$$
$$u\infty$$
$$u3$$
$$u2$$
$$u1$$
$$u3$$

![Figure 26.7](../../assets/ch26/fig_26_7.png)

**Hình 26.7:** xạ ảnh các hệ quy chiếu cho các không gian xạ ảnh có số chiều $1, 2$, và $3$.

> **Định nghĩa 26.4.** Cho trước không tầm thường không gian vectơ (vector space) $E$ có số chiều $n + 1$, với mọi xạ ảnh hệ quy chiếu (frame) $(a_{i})_{1\le i\le n+2}$ của P(E) và với mọi điểm $a \in$ P(E), tập hợp của thuần nhất các tọa độ của đối với $(a_{i})_{1\le i\le n+2}$ là tập hợp của $(n +$ 1)-các bộ ${(\lambda x_{1}, \dots  , \lambda x_{n+1}) \in K^{n+1}$ | $x_{i} \neq  0$ với một số $i, \lambda  \neq  0, a = p(x_{1}u_{1} + \cdots  + x_{n+1}u_{n+1})}$, ở đâu $(u_{1}, \dots  , u_{n+1})$ là bất kỳ cơ sở (basis) của $E$ liên kết với $(a_{i})_{1\le i\le n+2}$. Cho trước xạ ảnh hệ quy chiếu (frame) $(a_{i})_{1\le i\le n+2}$ cho P(E), nếu $(x_{1}, \dots  , x_{n+1})$ là thuần nhất các tọa độ của điểm $a \in$ P(E), ta viết $a = (x_{1}, \dots  , x_{n+1})$, và với slight abuse của language, ta có thể chẵn/ngay cả talk về điểm $(x_{1}, \dots  , x_{n+1})$ trong P(E) và viết $(x_{1}, \dots  , x_{n+1}) \in$ P(E). đặc biệt trường hợp của xạ ảnh đường thẳng $\mathbb{P}_{K}^{1}$ là worth examining. xạ ảnh đường thẳng $\mathbb{P}_{K}^{1}$ bao gồm của tất cả các lớp tương đương $[x, y]$ của các cặp $(x, y) \in K^{2}$ sao cho $(x, y) \neq  (0, 0)$, dưới quan hệ tương đương (equivalence relation) $\sim$ được định nghĩa sao cho
$$(x_{1}, y_{1}) \sim (x_{2}, y_{2})iff x_{2} = \lambda x_{1}andy_{2} = \lambda y_{1},$$
Với một số $\lambda  \in K -{0}$. Khi $y \neq  0$, lớp tương đương (equivalence class) của $(x, y)$ chứa representative $(xy^{-1}, 1)$, và khi $y = 0$, lớp tương đương (equivalence class) của $(x, 0)$ chứa representative $(1, 0)$.

<!-- PAGE 887 -->
Do đó, có một song ánh giữa $K$ và tập hợp của các lớp tương đương chứa một số representative của tạo thành $(x, 1)$, và ta ký hiệu lớp $[x, 1]$ bởi $x$. lớp tương đương (equivalence class) $[1, 0]$ được ký hiệu bởi $\infty$ và nó được gọi là điểm tại vô cực. Do đó, xạ ảnh đường thẳng $\mathbb{P}_{K}^{1}$ là trong song ánh với $K \cup {\infty$ }. ba các điểm $\infty = [1, 0], 0 = [0, 1]$, và $1 = [1, 1]$, tạo thành xạ ảnh hệ quy chiếu (frame) cho $\mathbb{P}_{K}^{1}$. xạ ảnh hệ quy chiếu (frame) $(\infty , 0, 1)$ là thường được gọi là chính tắc hệ quy chiếu (frame) của $\mathbb{P}_{K}^{1}$. Thuần nhất các tọa độ là cũng rất hữu ích đến handle các siêu phẳng theo các phương trình. Nếu $(a_{i})_{1\le i\le n+2}$ là xạ ảnh hệ quy chiếu (frame) cho P(E) liên kết với cơ sở (basis) $(u_{1}, \dots  , u_{n+1})$ cho $E$, khác không dạng tuyến tính (linear form) $f$ được xác định bởi $n + 1$ các vô hướng $\alpha_{1} , \dots  , \alpha_{n+1}$ (không tất cả null), và điểm $x \in$ P(E) của thuần nhất các tọa độ $(x_{1}, \dots  , x_{n+1})$ thuộc đến xạ ảnh siêu phẳng (hyperplane) P(H) của phương trình $f$ khi và chỉ khi
$$\alpha_{1} x_{1} + \cdots  + \alpha_{n+1} x_{n+1} = 0.$$
Đặc biệt, nếu P(E) là xạ ảnh mặt phẳng, đường thẳng được định nghĩa bởi phương trình của tạo thành $\alpha x + \beta y + \gamma z = 0$. Nếu P(E) là không gian xạ ảnh (projective space), mặt phẳng được định nghĩa bởi phương trình của tạo thành $\alpha x + \beta y + \gamma z + \delta w = 0$. Như ứng dụng, cho chúng ta tìm các tọa độ của giao điểm của hai phân biệt các đường thẳng trong xạ ảnh mặt phẳng P(E) (đối với một số xạ ảnh hệ quy chiếu (frame) $(a_{1}, a_{2}, a_{3}, a_{4}))$. Nếu $D$ và D' là hai các đường thẳng của các phương trình
$$\alpha x + \beta y + \gamma z = 0and\alpha' x + \beta' y + \gamma' z = 0,(*)$$
Thì $D$ và D' là phân biệt các đường thẳng khi và chỉ khi ma trận
$$\begin{pmatrix} \alpha & \beta & \gamma \\ \alpha' & \beta' & \gamma' \end{pmatrix}$$
Có hạng (rank) $2$. Ta khẳng định rằng giao $Q$ của các đường thẳng $D$ và D' có thuần nhất các tọa độ
$$(\beta \gamma' -\beta' \gamma  : \gamma \alpha' -\gamma' \alpha : \alpha \beta' -\alpha' \beta );(\dagger )$$
Nói cách khác, nó là xạ ảnh điểm tương ứng với cross-product
$$\begin{pmatrix} \alpha \\ \beta \\ \gamma \end{pmatrix} \times \begin{pmatrix} \alpha' \\ \beta' \\ \gamma' \end{pmatrix} ,$$
Như được minh họa trong Hình 26.8. Thật vậy, thuần nhất các tọa độ của giao $Q$ của $D$ và D' phải thỏa mãn simultaneously hai các phương trình (*), và vì hai các định thức
$$\alpha \beta \gamma \alpha' \beta' \gamma'$$
$$\alpha \beta \gamma and\alpha \beta \gamma$$
$$\alpha' \beta' \gamma' \alpha' \beta' \gamma'$$

<!-- PAGE 888 -->
$$D$$
$$P(E)$$
$$x$$
$$\overline{D’}$$
$$x$$
$$D$$
$$nD’nD’ xnD$$
$$nD$$

![Figure 26.8](../../assets/ch26/fig_26_8.png)

**Hình 26.8:** giao của hai xạ ảnh các đường thẳng trong xạ ảnh mặt phẳng P(E) là tích có hướng (cross product) của các chuẩn tắc/bình thường cho hai tương ứng các mặt phẳng trong $\mathbb{R}^{3}$. là không bởi vì chúng có hai bằng nhau các hàng, và vì bởi expanding các phần tử này các định thức đối với của chúng hàng thứ nhất bằng cách sử dụng Laplace expansion công thức ta thu được
$$\alpha \beta \gamma$$
$$0 =\alpha \beta \gamma = \alpha (\beta \gamma' -\beta' \gamma ) + \beta (\gamma \alpha' -\gamma' \alpha ) + \gamma (\alpha \beta' -\alpha' \beta )$$
$$\alpha' \beta' \gamma'$$
Và
$$\alpha' \beta' \gamma'$$
$$0 =\alpha \beta \gamma = \alpha' (\beta \gamma' -\beta' \gamma ) + \beta' (\gamma \alpha' -\gamma' \alpha ) + \gamma' (\alpha \beta' -\alpha' \beta ),$$
$$\alpha' \beta' \gamma'$$
Mà xác nhận rằng điểm
$$Q = (\beta \gamma' -\beta' \gamma  : \gamma \alpha' -\gamma' \alpha : \alpha \beta' -\alpha' \beta )$$
Thỏa mãn cả hai các phương trình trong (*), và do đó thuộc đến cả hai các đường thẳng $D$ và D'. Vì ma trận
$$\begin{pmatrix} \alpha & \beta & \gamma \\ \alpha' & \beta' & \gamma' \end{pmatrix}$$
Có hạng (rank) $2$, ít nhất một của các tọa độ của $Q$ là khác không, do đó $Q$ là thật vậy điểm trong xạ ảnh mặt phẳng, và nó là giao của các đường thẳng $D$ và D'. kết quả rằng ta chỉ được chứng minh cho ta sau đây tiêu chuẩn cho ba các đường thẳng $D$, D', D'' trong xạ ảnh mặt phẳng đến đi qua qua chung/phổ biến điểm (là concurrent). Trong xạ ảnh mặt phẳng,

<!-- PAGE 889 -->
Ba các đường thẳng $D$, D', D'' của các phương trình
$$\alpha x + \beta y + \gamma z = 0$$
$$\alpha' x + \beta' y + \gamma' z = 0$$
$$\alpha'' x + \beta'' y + \gamma'' z = 0$$
Là concurrent khi và chỉ khi
$$\alpha \beta \gamma$$
$$\alpha' \beta' \gamma' = 0.$$
$$\alpha'' \beta'' \gamma''$$
Ta có thể cũng tìm phương trình của duy nhất đường thẳng $D = \langle P$, P' $\rangle$ chuyển qua hai phân biệt các điểm $P = (u: v: w)$ và P' $=$ (u': v': w') của xạ ảnh mặt phẳng. Điều này đường thẳng được cho bởi phương trình
$$(vw'-v'w)x + (wu'-w'u) + (uv'-u'v)z = 0,(\dagger \dagger )$$
Và vì
$$\begin{pmatrix} u & v & w \\ u' & v' & w' \end{pmatrix}$$
Có hạng (rank) $2$ bởi vì P̸ $=$ P', ít nhất một của các tọa độ của phương trình $(\dagger \dagger$) là khác không. Nhận thấy rằng các hệ số của phương trình $(\dagger \dagger$) tương ứng với cross-product
$$\begin{pmatrix} u \\ v \\ w \end{pmatrix} \times \begin{pmatrix} u' \\ v' \\ w'' \end{pmatrix} .$$
Phương trình của đường thẳng $D = \langle P$, P' $\rangle$ phải được thỏa mãn bởi thuần nhất các tọa độ của các điểm $P$ và P'. Phương trình $(\dagger \dagger$) có thể được viết dưới dạng
$$xyz$$
$$uvw= 0,$$
$$u'v'w'$$
Và lập luận như trong trường hợp của giao của các đường thẳng chỉ ra rằng phương trình của đường thẳng chuyển qua $P$ và P' được cho bởi phương trình $(\dagger \dagger$). Thì, trong xạ ảnh mặt phẳng, ba các điểm $P = (u: v: w)$, P' $=$ (u': v': w') và P'' $=$ (u'': v'': w'') thuộc đến chung/phổ biến đường thẳng (là thẳng hàng) khi và chỉ khi
$$uvw$$
$$u'v'w'= 0.$$
$$u''v''w''$$
Tổng quát hơn, trong không gian xạ ảnh (projective space) P(E) có số chiều $n \ge 2$, nếu $n$ các điểm $P_{1}, \dots  , P_{n}$ là một cách xạ ảnh độc lập và nếu $P_{i}$ có thuần nhất các tọa độ $(u_{1}^{i}$: $\cdots$: $u_{n+1}^{i})$ (với

<!-- PAGE 890 -->
Đối với đến một số xạ ảnh hệ quy chiếu (frame) $(a_{1}, \dots  , a_{n+2}))$, thì phương trình của duy nhất siêu phẳng (hyperplane) $H$ chứa $P_{1}, \dots  , P_{n}$ được cho bởi phương trình
$$x_{1}x_{2}\cdots x_{n}x_{n+1}$$
$$u_{1}^{1}u_{2}^{1}\cdots u_{n}^{1}u_{n+1}^{1}$$
$$\vdots \vdots \ddots \vdots \vdots$$
$$= 0.$$
$$u_{1}^{n-1}u_{2}^{n-1}\cdots u_{n}^{n-1}u_{n+1}^{n-1}$$
$$u_{1}^{n}u_{2}^{n}\cdots u_{n}^{n}u_{n+1}^{n}$$
Ta cũng có sau đây mệnh đề cho một cái khác đặc trưng của xạ ảnh các hệ quy chiếu.

> **Mệnh đề 26.3.** họ $(a_{i})_{1\le i\le n+2}$ của $n+2$ các điểm là xạ ảnh hệ quy chiếu (frame) của P(E) khi và chỉ khi với mọi $i, 1 \le i \le n + 2$, họ con $(a_{j})_{j\neq i}$ là một cách xạ ảnh độc lập.

*Chứng minh.* Ta để lại như (dễ) bài tập sự kiện rằng nếu $(a_{i})_{1\le i\le n+2}$ là xạ ảnh hệ quy chiếu (frame), thì mỗi họ con $(a_{j})_{j\neq i}$ là một cách xạ ảnh độc lập. Ngược lại, chọn một số $u_{i} \in E -{0}$ sao cho $a_{i} = p(u_{i}), 1 \le i \le n + 2$. Vì $(a_{j})_{j\neq n+2}$ là một cách xạ ảnh độc lập, $(u_{1}, \dots  , u_{n+1})$ là cơ sở (basis) của $E$. Do đó, ta phải có
$$u_{n+2} = \lambda_{1} u_{1} + \cdots  + \lambda_{n+1} u_{n+1},$$
Với một số $\lambda_{i}  \in K$. Tuy nhiên, vì với mọi $i, 1 \le i \le n + 1$, họ $(a_{j})_{j\neq i}$ là một cách xạ ảnh độc lập, ta phải có $\lambda_{i}  \neq  0$, và do đó $(\lambda_{1} u_{1}, \dots  , \lambda_{n+1} u_{n+1})$ là cũng cơ sở (basis) của $E$, và vì
$$u_{n+2} = \lambda_{1} u_{1} + \cdots  + \lambda_{n+1} u_{n+1},$$
Nó cảm sinh xạ ảnh hệ quy chiếu (frame) $(a_{i})_{1\le i\le n+2}$. Hình 26.9 chỉ ra xạ ảnh hệ quy chiếu (frame) (, $b, c, d)$ trong xạ ảnh mặt phẳng. Đối với điều này xạ ảnh hệ quy chiếu (frame), các điểm, $b, c, d$ có thuần nhất các tọa độ $(1, 0, 0), (0, 1, 0), (0, 0, 1)$, và $(1, 1, 1)$. Cho ' là giao của $\langle d, a\rangle$ và $\langle b, c\rangle$, b' là giao của $\langle d, b\rangle$ và $\langle$, $c\rangle$, và c' là giao của $\langle d, c\rangle$ và $\langle$, $b\rangle$. Thì các điểm ', b', c' có thuần nhất các tọa độ $(0, 1, 1), (1, 0, 1)$, và $(1, 1, 0)$. biểu đồ được tạo thành bởi đường thẳng các đoạn thẳng $\langle$, $c'\rangle , \langle$, $b'\rangle , \langle b, b'\rangle , \langle c, c'\rangle , \langle$, $d\rangle$, và $\langle b, c\rangle$ đôi khi được gọi là một M¨obius net; xem Hilbert và Cohn-Vossen $[95]$ (Chương III, §15, trang $96)$. Nhắc lại rằng phương trình của đường thẳng (siêu phẳng (hyperplane) trong xạ ảnh mặt phẳng) theo thuần nhất các tọa độ đối với xạ ảnh hệ quy chiếu (frame) (, $b, c, d)$ được cho bởi thuần nhất phương trình của tạo thành
$$\alpha x + \beta y + \gamma z = 0,$$
Ở đâu $\alpha , \beta , \gamma$ là không tất cả không. Dễ dàng kiểm chứng được rằng các phương trình của các đường thẳng $\langle$, $b\rangle , \langle$, $c\rangle , \langle b, c\rangle$, là $z = 0, y = 0$, và $x = 0$, và các phương trình của các đường thẳng $\langle$, $d\rangle , \langle b, d\rangle$, và $\langle c, d\rangle$,

<!-- PAGE 891 -->
$$b(1,0,1)$$
$$x$$
$$=$$
$$z$$
$$(0,0,1)cz = x +$$
$$(1,0,-1)fy = y$$
$$x+$$
$$z$$
$$d(1,1,1)$$
$$,$$
$$a$$
$$0(0,1,1)x =$$
$$= y$$
$$y = z$$
$$y$$
$$z = 0$$
$$a\overline{g}\overline{b} c‘$$
$$(1,0,0)(-1,1,0)(0,1,0)(1,1,0)$$
$$x = 0$$
$$x +$$
$$y$$
$$+ z$$
$$=$$
$$0$$
$$x = y + z$$
$$e$$
$$(0,-1,1)$$
$$Figure 26.9: A projective frame (a, b, c, d).$$
Là $y = z, x = z$, và $x = y$. các phương trình của các đường thẳng $\langle$ ', $b'\rangle , \langle$ ', $c'\rangle , \langle$ b', $c'\rangle$ là $z = x + y, y = x + z$, và $x = y + z$. Nếu ta cho $e$ là giao của $\langle b, c\rangle$ và $\langle$ b', $c'\rangle , f$ là giao của $\langle$, $c\rangle$ và $\langle$ ', $c'\rangle$, và $g$ là giao của $\langle$, $b\rangle$ và $\langle$ ', $b'\rangle$, thì nó dễ dàng được thấy rằng $e, f, g$ có thuần nhất các tọa độ $(0, -1, 1), (1, 0, -1)$, và $(-1, 1, 0)$. Ví dụ, vì phương trình của đường thẳng $\langle b, c\rangle$ là $x = 0$ và phương trình của đường thẳng $\langle$ b', $c'\rangle$ là $x = y + z$, cho $x = 0$, ta thu được $z = -y$, mà tương ứng với thuần nhất các tọa độ $(0, -1, 1)$ cho $e$. các tọa độ của các điểm $e, f, g$ thỏa mãn phương trình $x + y + z = 0$, mà chỉ ra rằng chúng là thẳng hàng. Như được điểm ra trong Coxeter $[45]$ (Mệnh đề 2.41), điều này là đặc biệt trường hợp của xạ ảnh phiên bản của Desargues’s định lý (Mệnh đề 26.7) ứng dụng đến các tam giác (, $b, c)$ và (', b', c'). Thật vậy, bởi cách xây dựng, các đường thẳng $\langle$, $a'\rangle , \langle b, b'\rangle$, và $\langle c, c'\rangle$ giao nhau trong chung/phổ biến điểm $d$. đường thẳng chứa các điểm $e, f, g$ được gọi là polar đường thẳng (hoặc cơ bản đường thẳng) của $d$ đối với tam giác (, $b, c)$ (xem Pedoe $[141])$. biểu đồ cũng chỉ ra giao $g$ của $\langle$, $b\rangle$ và $\langle$ ', $b'\rangle$. không gian xạ ảnh (projective space) của các đường tròn cung cấp đẹp illustration của thuần nhất các tọa độ.

<!-- PAGE 892 -->
Cho $E$ là không gian vectơ (vector space) $(over\mathbb{R})$ bao gồm của tất cả thuần nhất các đa thức của bậc $2$ trong $x, y, z$ của tạo thành
$$ax^{2}+ ay^{2}+ bxz + cyz + dz^{2}$$
(cộng null đa thức). không gian xạ ảnh (projective space) P(E) bao gồm của tất cả các lớp tương đương
$$[P]_{\sim}= {\lambda P | \lambda  \neq  0},$$
Ở đâu P(x, $y, z)$ là khác không thuần nhất đa thức trong $E$. Ta muốn đến cho hình học interpretation của các điểm của không gian xạ ảnh (projective space) P(E). Trong thứ tự đến thực hiện do đó, chọn một số xạ ảnh hệ quy chiếu (frame) $(a_{1}, a_{2}, a_{3}, a_{4})$ cho xạ ảnh mặt phẳng $\mathbb{RP}^{2}$, và associate đến mọi $[P] \in$
$$\mathbb{RP}^{2}$$
P(E) tập con của đã biết như của nó của nó không quỹ tích (hoặc không tập hợp, hoặc variety) $V ([P])$, và được định nghĩa sao cho
$$\mathbb{RP}^{2}$$
$$V ([P]) = {a \in | P(x, y, z) = 0},$$
Ở đâu $(x, y, z)$ là thuần nhất các tọa độ cho. Như được giải thích trước đó, ta cũng sử dụng đơn giản hơn ký hiệu
$$\mathbb{RP}^{2}$$
$$V ([P]) = {(x, y, z) \in | P(x, y, z) = 0}.$$
Thực sự, trong thứ tự cho $V ([P])$ để tạo nghĩa, ta có để kiểm tra rằng $V ([P])$ không phụ thuộc vào representative được chọn trong lớp tương đương (equivalence class) $[P] = {\lambda P$ | $\lambda  \neq  0}$. Điều này là bởi vì
$$P(x, y, z) = 0iff\lambda P(x, y, z) = 0when \lambda  \neq  0.$$
Để đơn giản của ký hiệu, ta cũng ký hiệu $V ([P])$ bởi $V (P)$. Ta cũng có để kiểm tra rằng nếu $(\lambda x, \lambda y, \lambda z)$ là khác thuần nhất các tọa độ cho $a \in \mathbb{RP}^{2}$, ở đâu $\lambda  \neq  0$, thì
$$P(x, y, z) = 0iffP(\lambda x, \lambda y, \lambda z) = 0.$$
Tuy nhiên, vì P(x, $y, z)$ là thuần nhất của bậc $2$, ta có
$$P(\lambda x, \lambda y, \lambda z) = \lambda^{2} P(x, y, z),$$
Và vì $\lambda  \neq  0$,
$$P(x, y, z) = 0iff\lambda^{2} P(x, y, z) = 0.$$
Ở trên lập luận áp dụng đến bất kỳ thuần nhất đa thức $P(x_{1}, \dots  , x_{n})$ trong $n$ các biến của bất kỳ bậc $m$, vì
$$P(\lambda x_{1}, \dots  , \lambda x_{n}) = \lambda^{m} P(x_{1}, \dots  , x_{n}).$$
Do đó, ta có thể associate đến mọi $[P] \in$ P(E) đường cong $V (P)$ trong $\mathbb{RP}^{2}$. Một có thể tự hỏi tại sao ta là xét chỉ thuần nhất các đa thức của bậc $2$, và không tùy ý các đa thức của bậc $2$? thứ nhất lý do là rằng các đa thức trong $x, y, z$ của bậc $2$ thực hiện không tạo thành không gian vectơ (vector space). Ví dụ, nếu $P = x^{2} + x$ và $Q = -x^{2} + y$, đa thức $P + Q = x + y$ là không của bậc $2$. Ta có thể xét tập hợp của các đa thức của bậc $\le 2$,

<!-- PAGE 893 -->
Mà là không gian vectơ (vector space), nhưng bây giờ bài toán là rằng $V (P)$ là không nhất thiết tốt được định nghĩa!. Ví dụ, nếu P(x, $y, z) = -x^{2} + 1$, ta có
$$P(1, 0, 0) = 0andP(2, 0, 0) = -3,$$
Và vẫn chưa $(2, 0, 0) =$ 2(1, $0, 0)$, sao cho P(x, $y, z)$ lấy khác nhau các giá trị tùy thuộc trên representative được chọn trong lớp tương đương (equivalence class) $[1, 0, 0]$. Do đó, ta là đã dẫn đến đến thu hẹp chính chúng ta đến thuần nhất các đa thức. Thực sự, điều này là thường advantage nhiều hơn disadvantage, bởi vì thuần nhất các đa thức tiến tới là tốt behaved. Những gì là các đường cong $V (P)$? Một cách đến “xem” như vậy các đường cong là đến đi quay lại đến siêu phẳng (hyperplane)
$$\mathbb{RP}^{2}  \mathbb{R}^{3}$$
Mô hình của theo mặt phẳng $H$ của phương trình $z = 1$ trong. Thì vết (trace) của $V (P)$ trên $H$ là đường tròn của phương trình
$$ax^{2}+ ay^{2}+ bx + cy + d = 0.$$
Do đó, ta có thể nghĩ của P(E) như không gian xạ ảnh (projective space) của các đường tròn. Tuy nhiên, có một số các bài tập. Ví dụ, $V (P)$ có thể là rỗng! Điều này xảy ra, chẳng hạn, cho P(x, $y, z) = x^{2} + y^{2} + z^{2}$, vì phương trình
$$x^{2}+ y^{2}+ z^{2}= 0$$
Có chỉ tầm thường nghiệm $(0, 0, 0)$, mà thực hiện không tương ứng với bất kỳ điểm $in\mathbb{RP}^{2}$. Thật vậy,
$$\mathbb{R}^{3}  \mathbb{RP}^{2}$$
Chỉ khác không các vectơ trong cho các điểm trong. Nó là cũng khả dĩ/có thể rằng $V (P)$ là rút gọn đến đơn lẻ điểm, chẳng hạn khi P(x, $y, z) = x^{2} + y^{2}$, vì chỉ thuần nhất nghiệm của
$$x^{2}+ y^{2}= 0$$
Là $(0, 0, 1)$. Cũng, lưu ý rằng ánh xạ
$$[P] \mapsto V (P)$$
Là không đơn ánh (injective). Chẳng hạn, $P = x^{2} + y^{2}$ và $Q = x^{2} + 2y^{2}$ định nghĩa cùng suy biến đường tròn rút gọn đến điểm $(0, 0, 1)$. Ta cũng accept như các đường tròn hợp của hai các đường thẳng, như trong trường hợp
$$(bx + cy + dz)z = 0,$$
Ở đâu $a = 0$, và chẵn/ngay cả gấp đôi đường thẳng, như trong trường hợp
$$z^{2}= 0,$$
Ở đâu $a = b = c = 0$. gọn gàng cách đến resolve hầu hết của các bài tập này là đến switch đến thuần nhất các đa thức trên phức trường $\mathbb{C}$ và đến xét các đường cong trong $\mathbb{CP}^{2}$. Điều này là những gì được thực hiện trong đại số hình học (xem Fulton $[67]$ hoặc Harris $[90])$. Nếu P(x, $y, z)$ là thuần nhất đa thức $over\mathbb{C}$ của bậc $2$ (cộng null đa thức), nó là dễ để chỉ ra rằng $V (P)$ là luôn luôn khác rỗng, và thực ra vô hạn. Nó có thể cũng được hiển thị rằng $V (P) = V (Q)$ suy ra rằng $Q = \lambda P$ với một số $\lambda  \in \mathbb{C}$, với $\lambda  \neq  0$ (xem Samuel $[148]$, Mục 1.6, Định lý $10)$. Một cái khác advantage của switching đến

<!-- PAGE 894 -->
Phức $field\mathbb{C}$ là rằng lý thuyết của giao là cleaner. Do đó, bất kỳ hai các đường tròn rằng thực hiện không chứa chung/phổ biến đường thẳng luôn luôn giao nhau trong bốn các điểm, một số của mà có thể là bội các điểm (như trong trường hợp của tiếp tuyến các đường tròn). Điều này có thể dường như đáng ngạc nhiên, vì trong thực mặt phẳng, hai các đường tròn giao nhau trong nhiều nhất hai các điểm. Ở đâu là khác hai các điểm? Chúng turn ra là các điểm $(1, i, 0)$ và $(1, -i, 0)$, như một có thể ngay lập tức kiểm chứng. Ta có thể nghĩ của chúng như phức các điểm tại vô cực! Không chỉ là chúng tại vô cực, nhưng chúng là không thực. Không có tự hỏi ta không thể xem chúng! Ta sẽ đến quay lại đến các phần tử này các điểm, được gọi là tròn các điểm, trong Mục 26.14. Đi quay lại đến không gian vectơ (vector space) $E$ của các đường tròn $over\mathbb{R}$, nó là worth nói rằng rằng nó có thể được được hiển thị rằng nếu $V (P) = V (Q)$ chứa ít nhất hai các điểm (trong mà trường hợp, $V (P)$ là thực sự vô hạn), thì $Q = \lambda P$ với một số $\lambda  \in \mathbb{R}$ với $\lambda  \neq  0$ (xem Tisseron $[181]$, Định lý 3.6.1 và Định lý 4.7). Do đó, chẵn/ngay cả trên $\mathbb{R}$, ánh xạ
$$[P] \mapsto V (P)$$
Là đơn ánh (injective) bất cứ khi nào $V (P)$ là không rỗng cũng không rút gọn đến đơn lẻ điểm. Lưu ý rằng không gian xạ ảnh (projective space) P(E) của các đường tròn có số chiều $3$. Thực ra, nó là dễ để chỉ ra rằng ba phân biệt các điểm rằng là không thẳng hàng xác định duy nhất đường tròn (xem Samuel $[148]$, Mục 1.6). Trong đồng dạng vein, ta có thể định nghĩa không gian xạ ảnh (projective space) của các đường bậc hai (conics) P(E) ở đâu $E$ là không gian vectơ (vector space) (trên $\mathbb{R})$ bao gồm của tất cả thuần nhất các đa thức của bậc $2$ trong $x, y, z$,
$$ax^{2}+ by^{2}+ cxy + dxz + eyz + fz^{2}$$
(cộng null đa thức). các đường cong $V (P)$ là thật vậy các đường bậc hai (conics), perhaps suy biến. để xem điều này, ta có thể sử dụng siêu phẳng (hyperplane) mô hình của $\mathbb{RP}^{2}$. vết (trace) của $V (P)$ trên mặt phẳng của phương trình $z = 1$ là conic của phương trình
$$ax^{2}+ by^{2}+ cxy + dx + ey + f = 0.$$
Một cái khác cách để xem rằng $V (P)$ là conic là đến nhận thấy rằng trong $\mathbb{R}^{3}$,
$$ax^{2}+ by^{2}+ cxy + dxz + eyz + fz^{2}= 0$$
Định nghĩa nón với đỉnh $(0, 0, 0)$, và vì của nó mục bởi mặt phẳng $z = 1$ là conic, tất cả của của nó các mục bởi các mặt phẳng là các đường bậc hai (conics). Xem Hình 26.10 cho schematic illustration của xạ ảnh conic được nhúng trong $\mathbb{RP}^{2}$. ánh xạ
$$[P] \mapsto V (P)$$
Là vẫn đơn ánh (injective) khi $E$ được định nghĩa trên ground $field\mathbb{C}$ (Samuel $[148]$, Mục 1.6, Định lý $10)$, hoặc nếu $V (P)$ có ít nhất hai các điểm khi $E$ được định nghĩa trên $\mathbb{R}$ (Tisseron $[181]$, Định lý 3.6.1 và Định lý 4.7). Lưu ý rằng không gian xạ ảnh (projective space) P(E) của các đường bậc hai (conics) có số chiều $5$. Thực ra, nó có thể được được hiển thị rằng năm phân biệt các điểm, không có bốn của mà là thẳng hàng, xác định

<!-- PAGE 895 -->
$$z = 1$$
$$(1,1,1)$$
$$Step 1: Plot xy = 1 in the plane z = 1.$$
$$Step 2: Expand into a radial cone.$$
$$z = 1$$
$$(1,1,1)$$
$$z = 1$$
$$(1,1,1)$$
$$x*$$
$$x*$$
$$Step 3: Projectivize the cone.$$

![Figure 26.10](../../assets/ch26/fig_26_10.png)

**Hình 26.10:** ba bước process cho xây dựng $V (P)$ ở đâu $P$ là homogenous conic xy $= z$. Trong Bước $2$, ta chuyển đổi đến homogenous các tọa độ thông qua phép biến đổi $x \to x/z, y \to y/z$. duy nhất conic (trong số nhiều sources, xem Samuel $[148]$, Mục 1.7, Định lý $17$, hoặc Coxeter $[45]$, Định lý 6.56, ở đâu hình học cách xây dựng là cho trước trong Mục 6.6).
$$\mathbb{CP}^{2} \mathbb{RP}^{2}$$
Thực ra, nếu ta chọn xạ ảnh hệ quy chiếu (frame) $(a_{1}, a_{2}, a_{3}, a_{4})$ trong (hoặc), và nếu năm các điểm $p_{1}, p_{2}, p_{3}, p_{4}, p_{5}$ có thuần nhất các tọa độ $p_{i} = (x_{i}, y_{i}, z_{i})$ cho $i = 1, \dots  , 5$ và $(x, y, z)$ là các biến, thì nó là dễ bài tập để chỉ ra rằng phương trình của duy nhất conic $C$ chuyển qua các điểm $p_{1}, p_{2}, p_{3}, p_{4}, p_{5}$ được cho bởi
$$x^{2}xyy^{2}xzyzz^{2}$$
$$x_{1}^{2}x_{1}y_{1}y_{1}^{2}x_{1}z_{1}y_{1}z_{1}z_{1}^{2}$$
$$x_{2}^{2}x_{2}y_{2}y_{2}^{2}x_{2}z_{2}y_{2}z_{2}z_{2}^{2}$$
$$= 0.$$
$$x_{3}^{2}x_{3}y_{3}y_{3}^{2}x_{3}z_{3}y_{3}z_{3}z_{3}^{2}$$
$$x_{4}^{2}x_{4}y_{4}y_{4}^{2}x_{4}z_{4}y_{4}z_{4}z_{4}^{2}$$
$$x_{5}^{2}x_{5}y_{5}y_{5}^{2}x_{5}z_{5}y_{5}z_{5}z_{5}^{2}$$
Đa thức thu được bởi expanding ở trên định thức (determinant) theo hàng thứ nhất là thuần nhất đa thức của bậc $2$ trong các biến $x, y, z$, và nó là không không đa thức

<!-- PAGE 896 -->
Bởi vì ma trận cỡ $5 \times  6$ thu được bởi xóa hàng thứ nhất trong ma trận của định thức (determinant) có hạng (rank) $5$. Thật vậy, điều này là ma trận của hệ phương trình tuyến tính xác định sáu các hệ số của conic passign qua $p_{1}, p_{2}, p_{3}, p_{4}, p_{5}$ (sai khác một vô hướng), và vì điều này conic là duy nhất, ma trận này phải có hạng (rank) $5$. Nó là cũng thú vị để xem những gì là các đường thẳng trong không gian của các đường tròn hoặc trong không gian của các đường bậc hai (conics). Trong cả hai các trường hợp ta thu được các chùm (của các đường tròn và các đường bậc hai (conics), respectively). Cho nhiều hơn/thêm chi tiết, xem Samuel $[148]$, Sidler $[167]$, Tisseron $[181]$, Lehmann và Bkouche $[119]$, Pedoe $[141]$, Coxeter $[45, 46]$, và Veblen và Young $[189, 190]$. tổng quát hóa của không gian của xạ ảnh các đường bậc hai (conics) là không gian của xạ ảnh các mặt bậc hai P(E), ở đâu $E$ là không gian vectơ (vector space) (trên trường $K$, typically $K =\mathbb{R}$ hoặc $K =\mathbb{C})$ bao gồm của tất cả thuần nhất các đa thức $P(x_{1}, \dots  , x_{N+1})$ của bậc $2$ trong các biến $x_{1}, \dots  , x_{N+1}$, với $N \ge 3$ (cộng null đa thức). không quỹ tích $V (P)$ của $P$ được định nghĩa chỉ như trước như
$$V (P) = {(x_{1} : \cdots  : x_{N+1}) \in \mathbb{P}_{K}^{N} | P(x_{1}, \dots  , x_{N+1}) = 0}.$$
Nếu trường $K$ là algebraically đóng, đặc biệt nếu $K = \mathbb{C}$, thì $V (P) = V (Q)$ suy ra rằng tồn tại một khác không $\lambda  \in K$ sao cho $Q = \lambda P$; xem Berger $[12]$ (Chương $14$, Định lý 14.1.6.2). Một cái khác tình huống ở đâu ánh xạ $[P] \mapsto V (P)$ là đơn ánh (injective) liên quan đến khái niệm của đơn giản (hoặc chính quy) điểm của mặt bậc hai (quadric). Với mọi $a = (a_{1}$: $\cdots$: $a_{N+1}) \in \mathbb{P}_{K}^{N}$, cho $P_{xi}(a)$ là đạo hàm riêng (partial derivative) của $P$ tại cho trước bởi
$$P_{xi}(a) = \frac{\partial P}{\partial x_{i}} (a_{1}, \dots  , a_{N+1}).$$
Chặt speaking, $P_{xi}(a)$ phụ thuộc vào representative $(a_{1}, \dots  , a_{N+1}) \in K^{N+1}$ được chọn cho điểm, nhưng vì $P$ là thuần nhất của bậc $2$, với mọi khác không $\lambda  \in K$,
$$\frac{\partial P}{\partial x_{i}} (\lambda a_{1}, \dots  , \lambda a_{N+1}) = \lambda \frac{\partial P}{\partial x_{i}} (a_{1}, \dots  , a_{N+1}).$$
Do đó $P_{xi}(a)$ được định nghĩa sai khác khác không vô hướng (scalar). Đặc biệt, liệu có hay không $P_{xi}(a) = 0$ phụ thuộc chỉ điểm $a = (a_{1}$: $\cdots$: $a_{N+1}) \in \mathbb{P}_{K}^{N}$. Thì điểm $a \in V (P)$ được nói là đơn giản (hoặc chính quy) nếu
$$P_{xi}(a) \neq  0for some i, 1 \le i \le N + 1.$$
Ngược lại, nếu $P_{x1}(a) = \cdots  = P_{xN+1}(a) = 0$, ta nói rằng $a \in V (P)$ là suy biến điểm. Nếu $a \in V (P)$ là chính quy điểm, thì tiếp tuyến siêu phẳng (hyperplane) $T_{a}V (P)$ đến $V (P)$ tại là siêu phẳng (hyperplane) cho trước bởi phương trình
$$P_{x1}(a)x_{1} + \cdots  + P_{xN+1}(a)x_{N+1} = 0.$$
Nó có thể được được hiển thị rằng nếu trường $K$ là không trường $F_{2} = {0, 1}$ và nếu mặt bậc hai (quadric) $V (P)$ chứa một số chính quy điểm, thì $V (P) = V (Q)$ suy ra rằng tồn tại một khác không $\lambda  \in K$ sao cho $Q = \lambda P$; xem Samuel $[148]$ (Chương $3$, Định lý $46)$.

<!-- PAGE 897 -->
Các mặt bậc hai, xạ ảnh, afin, và Euclidean, có đã được một cách kỹ lưỡng investigated. Trong số nhiều sources, độc giả là referred đến Berger $[11]$, Samuel $[148]$, Tisseron $[181]$, Fresnel $[66]$, và Vienne $[191]$. Ta có thể cũng investigate đại số mặt phẳng các đường cong của bất kỳ bậc $m$, bởi đặt $E$ là không gian vectơ (vector space) của thuần nhất các đa thức của bậc $m$ trong $x, y, z$ (cộng null đa thức). không quỹ tích $V (P)$ của $P$ được định nghĩa chỉ như trước như
$$\mathbb{RP}^{2}$$
$$V (P) = {(x: y: z) \in | P(x, y, z) = 0}.$$
Nhận thấy rằng khi $m = 1$, vì thuần nhất các đa thức của bậc $1$ là các dạng tuyến tính, ta là quay lại đến trường hợp ở đâu $E = (\mathbb{R}^{3})^{*}$, không gian đối ngẫu (dual space) $of\mathbb{R}^{3}$, và P(E) có thể được đồng nhất với tập hợp của các đường thẳng trong $\mathbb{RP}^{2}$. Nhưng khi $m \ge 3$, things là chẵn/ngay cả tệ hơn regarding tính đơn ánh của ánh xạ $[P] \mapsto V (P)$. Chẳng hạn, cả hai $P = xy^{2}$ và $Q = x^{2}y$ định nghĩa cùng hợp của hai các đường thẳng. Nó là cần đến xét bất khả quy (irreducible) các đường cong, i.e., các đường cong rằng được định nghĩa bởi bất khả quy (irreducible) các đa thức, và đến hoạt động/công trình trên trường $\mathbb{C}$ của phức các số (nhắc lại rằng đa thức $P$ là bất khả quy (irreducible) nếu nó không thể được viết như tích $P = Q_{1}Q_{2}$ của hai các đa thức $Q_{1}, Q_{2}$ của bậc $\ge 1)$. Ta refer độc giả đến Fischer’s cuốn sách cho đẹp (và rất rõ ràng) giới thiệu đến đại số các đường cong $[63]$. tiếp theo bước là Fulton $[67]$.
$$\mathbb{RP}^{3}  \mathbb{CP}^{3}$$
Ta có thể cũng investigate đại số các mặt trong (hoặc), bởi đặt $E$ là không gian vectơ (vector space) của thuần nhất các đa thức của bậc $m$ trong bốn các biến $x, y, z, t$ (cộng null đa thức). Ta có thể cũng xét không quỹ tích của tập hợp của các phương trình
$$\mathcal{E} = {P_{1} = 0, P_{2} = 0, \dots  , P_{n} = 0},$$
Ở đâu $P_{1}, \dots  , P_{n}$ là thuần nhất các đa thức của bậc $m$ trong $x, y, z, t$, được định nghĩa như
$$\mathbb{RP}^{3}$$
$$V (\mathcal{E}) = {(x: y: z : t) \in | P_{i}(x, y, z, t) = 0, 1 \le i \le n}.$$
Điều này cách, ta có thể cũng deal với không gian các đường cong. Cuối cùng, ta có thể xét thuần nhất các đa thức $P(x_{1}, \dots  , x_{N+1})$ trong $N + 1$ các biến
$$\mathbb{RP}^{N}  \mathbb{CP}^{N}$$
Và của bậc $m$ (cộng null đa thức), và study các tập con của hoặc (hoặc tổng quát hơn của $\mathbb{P}_{K}^{N}$, cho tùy ý trường $K)$, được định nghĩa như không quỹ tích của tập hợp của các phương trình
$$\mathcal{E} = {P_{1} = 0, P_{2} = 0, \dots  , P_{n} = 0},$$
Ở đâu $P_{1}, \dots  , P_{n}$ là thuần nhất các đa thức của bậc $m$ trong các biến $x_{1}, \dots , x_{N+1}$.
$$\mathbb{RP}^{3} \mathbb{RP}^{5}$$
Ví dụ, hóa ra là tập hợp của các đường thẳng trong các dạng mặt của bậc $2$ trong (Klein mặt bậc hai (quadric)). Tuy nhiên, tất cả điều này sẽ một cách thực lấy chúng ta cũng far vào đại số hình học, và ta đơn giản refer interested độc giả đến Hulek $[100]$, Fulton $[67]$, và Harris $[90]$. Ta bây giờ xét xạ ảnh các ánh xạ.
