# Các ánh xạ tuyến tính (linear maps)


<!-- PAGE 101 -->

> **Ví dụ 3.5.** Ví dụ, đặt $A, B$ là $2 \times$ 2-các ma trận
$$A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} ,B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} ,$$
Thì
$$AB = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} ,$$
Và
$$BA = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} .$$
Do đó AB $\neq$ BA, và $AB = 0$, chẵn/ngay cả dù cả hai $A, B \neq  0$.

## 3.7 Các ánh xạ tuyến tính (linear maps)

Bây giờ rằng ta understand các không gian vectơ và cách mà đến sinh chúng, ta sẽ like là able đến biến đổi một không gian vectơ (vector space) $E$ vào một cái khác không gian vectơ (vector space) $F$. hàm giữa hai các không gian vectơ rằng bảo toàn không gian vectơ (vector space) cấu trúc được gọi là một đồng cấu của các không gian vectơ, hoặc ánh xạ tuyến tính (linear map). Các ánh xạ tuyến tính (linear maps) formalize khái niệm của tính tuyến tính của hàm. Giữ trong mind rằng các ánh xạ tuyến tính (linear maps), mà là các phép biến đổi của
$$space, are usually far more important than the spaces$$
$$themselves.$$
Trong rest của điều này mục, ta giả sử rằng tất cả các không gian vectơ là trên cho trước trường $K$ (nói $\mathbb{R})$.

> **Định nghĩa 3.18.** Cho trước hai các không gian vectơ $E$ và $F$, ánh xạ tuyến tính (linear map) giữa $E$ và $F$ là hàm $f$: $E \to F$ thỏa mãn sau đây hai các điều kiện:
$$f(x +_{E} y) = f(x) +_{F} f(y)for all x, y \in E;$$
$$f(\lambda  \cdot_{E}  x) = \lambda  \cdot_{F}  f(x)for all \lambda  \in K, x \in E.$$
Đặt $x = y = 0_{E}$ trong thứ nhất đồng nhất thức, ta thu được $f(0_{E}) = 0_{F}$. cơ bản tính chất của các ánh xạ tuyến tính (linear maps) là rằng chúng biến đổi các tổ hợp tuyến tính vào các tổ hợp tuyến tính. Cho trước bất kỳ hữu hạn họ $(u_{i})_{i\in I}$ của các vectơ trong $E$, cho trước bất kỳ họ $(\lambda_{i} )_{i\in I}$ của các vô hướng trong $K$, ta có
$$f \begin{pmatrix} \lambda_{i}  \cdot_{E} u_{i} \end{pmatrix} \sum_{i\in I}  = \sum_{i\in I}  \lambda_{i}  \cdot_{F}  f(u_{i}).$$
$$The sum \sum_{i}  \in  \lambda_{i}  \cdot_{E}  u_{i} uses addition +_{E} in E, and the sum \sum_{i}  \lambda_{i}  \cdot_{F}  f(u_{i}) uses addition in$$
$F$. $above^{I}$ đồng nhất thức được hiển thị bằng quy nạp theo |I| bằng cách sử dụng $the^{\in I}$ các tính chất của Định nghĩa 3.18. Như ta đã thực hiện khi định nghĩa các không gian vectơ, cho notational simplicity, ta thường bỏ các chỉ số dưới $E$ và $F$ trong các ký hiệu $+_{E}, +_{F}$ và $\cdot_{E} , \cdot_{F}$.

<!-- PAGE 102 -->

> **Ví dụ 3.6.**
$$\mathbb{R}^{2} \mathbb{R}^{2}$$
$1$. ánh xạ $f$: $\to$ được định nghĩa sao cho
$$x'=x -y$$
$$y'=x + y$$
Là ánh xạ tuyến tính (linear map). độc giả nên kiểm tra rằng nó là hợp thành của phép quay bởi
$$\sqrt$$
$\pi /4$ với magnification của tỉ số $\overline{2.} 2$. Với mọi không gian vectơ (vector space) $E$, đồng nhất thức ánh xạ id: $E \to E$ cho trước bởi
$$id(u) = ufor all u \in E$$
Là ánh xạ tuyến tính (linear map). Khi ta muốn là nhiều hơn/thêm precise, ta viết $id_{E}$ thay vì của id. $3$. ánh xạ $D: \mathbb{R}[X] \to \mathbb{R}[X]$ được định nghĩa sao cho
$$(DP)(X) = P' (X),$$
Ở đâu P' $(X)$ là đạo hàm của đa thức P(X), là ánh xạ tuyến tính (linear map). Nhiều hơn/thêm một cách tường minh, nếu
$$\mathbb{R}$$
$$P(X) = a_{0}X^{n}+ a_{1}X^{n-1}+ \cdots  + a_{n-2}X^{2}+ a_{n-1}X + a_{n},a_{i} \in$$
Là đa thức của bậc $n$, thì
$$(DP)(X) = na_{0}X^{n-1}+ (n -1)a_{1}X^{n-2}+ \cdots  + 2a_{n-2}X + a_{n-1}.$$
$4$. ánh xạ $\Phi$: $\mathcal{C}([a, b]) \to \mathbb{R}$ cho trước bởi
$$\Phi (f) = \int_{a}^{}  bf(t)dt,$$
$where\mathcal{C}([a, b])$ là tập hợp của liên tục các hàm được định nghĩa trên khoảng/đoạn [, $b]$, là ánh xạ tuyến tính (linear map). $5$. hàm $\langle$ -, $-\rangle$: $\mathcal{C}([a, b]) \times$ C([, $b]) \to \mathbb{R}$ cho trước bởi
$$\langle f, g\rangle = \int_{a}^{}  bf(t)g(t)dt,$$
Là tuyến tính trong mỗi của biến $f, g$. Nó cũng thỏa mãn các tính chất $\langle f, g\rangle = \langle g, f\rangle$ và $\langle f, f\rangle = 0$ khi và chỉ khi $f = 0$. Nó là ví dụ của tích vô hướng (inner product).

> **Định nghĩa 3.19.** Cho trước ánh xạ tuyến tính (linear map) $f$: $E \to F$, ta định nghĩa ảnh (ảnh (image)) của nó (hoặc miền giá trị (range)) Im $f =$ f(E), như tập hợp
$$\mathrm{Im} f = {y \in F | (\exists x \in E)(y = f(x))},$$
Và hạt nhân (hạt nhân (kernel)) của nó (hoặc không gian hạch (nullspace)) Ker $f = f^{-1} (0_{F})$, như tập hợp
$$\mathrm{Ker} f = {x \in E | f(x) = 0_{F}}.$$

<!-- PAGE 103 -->
Đạo hàm ánh xạ $D: \mathbb{R}[X] \to \mathbb{R}[X]$ từ Ví dụ 3.6(3) có hạt nhân (kernel) hằng số các đa thức, do đó Ker $D =\mathbb{R}$. Nếu ta xét đạo hàm thứ hai $D \circ D: \mathbb{R}[X] \to \mathbb{R}[X]$, thì hạt nhân (kernel) của $D \circ D$ bao gồm của tất cả các đa thức của bậc $\le 1$. ảnh (image) của $D: \mathbb{R}[X] \to \mathbb{R}[X]$
$$\mathbb{R}$$
Là thực sự $[X]$ chính nó, bởi vì mọi đa thức P(X) $= a_{0}X^{n} + \cdots  + a_{n-1}X + a_{n}$ của bậc $n$ là đạo hàm của đa thức Q(X) của bậc $n + 1$ cho trước bởi
$$Q(X) = a_{0} \frac{X^{n+1}}{n + 1} + \cdots  + a_{n-1} \frac{X^{2}}{2} + a_{n}X.$$
Mặt khác, nếu ta xét thu hẹp của $D$ đến không gian vectơ (vector space) $\mathbb{R}[X]_{n}$ của các đa thức của bậc $\le n$, thì hạt nhân (kernel) của $D$ là vẫn $\mathbb{R}$, nhưng ảnh (image) của $D$ là $\mathbb{R}[X]_{n-1}$, không gian vectơ (vector space) của các đa thức của bậc $\le n$ - $1$.

> **Mệnh đề 3.19.** Cho trước ánh xạ tuyến tính (linear map) $f$: $E \to F$, các tính chất sau đây đúng.
$(1)$ tập hợp Im $f$ là không gian con của $F$.
$(2)$ tập hợp Ker $f$ là không gian con của $E$.
$(3)$ ánh xạ tuyến tính (linear map) $f$: $E \to F$ là đơn ánh (injective) khi và chỉ khi Ker $f = (0_{E})$ (ở đâu $(0_{E})$ là tầm thường không gian con ${0_{E}})$.

*Chứng minh.* Cho trước bất kỳ $x, y \in$ Im $f$, có một số $u, v \in E$ sao cho $x =$ f(u) và $y =$ f(v), và với mọi $\lambda , \mu  \in \mathbb{R}$, ta có
$$f(\lambda u +_{E} \mu v) = \lambda f(u) +_{F} \mu f(v) = \lambda x +_{F} \mu y,$$
Và do đó, $\lambda x +_{F} \mu y \in$ Im $f$, chỉ ra rằng Im $f$ là không gian con của $F$. Cho trước bất kỳ $x, y \in$ Ker $f$, ta có f(x) $= 0_{F}$ và f(y) $= 0_{F}$, và do đó,
$$f(\lambda x +_{E} \mu y) = \lambda f(x) +_{F} \mu f(y) = 0_{F},$$
Rằng là, $\lambda x +_{E} \mu y \in$ Ker $f$, chỉ ra rằng Ker $f$ là không gian con của $E$. Thứ nhất, giả sử rằng Ker $f = (0_{E})$. Ta cần để chứng minh rằng f(x) $=$ f(y) suy ra rằng $x = y$. Tuy nhiên, nếu f(x) $=$ f(y), thì f(x) $-_{F}$ f(y) $= 0_{F}$, và bởi tính tuyến tính của $f$ ta thu được f(x $-_{E} y) = 0_{F}$. Bởi vì Ker $f = (0_{E})$, ta phải có $x -_{E} y = 0_{E}$, nghĩa là $x = y$, do đó $f$ là đơn ánh (injective). Ngược lại, giả sử rằng $f$ là đơn ánh (injective). Nếu $x \in$ Ker $f$, nghĩa là f(x) $= 0_{F}$, vì $f(0_{E}) = 0_{F}$ ta có f(x) $= f(0_{E})$, và bởi tính đơn ánh, $x = 0_{E}$, mà chứng tỏ rằng Ker $f = (0_{E})$. Vì vậy, $f$ là đơn ánh (injective) khi và chỉ khi Ker $f = (0_{E})$. Vì theo Mệnh đề 3.19, ảnh (image) Im $f$ của ánh xạ tuyến tính (linear map) $f$ là không gian con của $F$, ta có thể định nghĩa hạng (rank) rk(f) của $f$ như số chiều của Im $f$.

> **Định nghĩa 3.20.** Cho trước ánh xạ tuyến tính (linear map) $f$: $E \to F$, hạng (rank) rk(f) của $f$ là số chiều của ảnh (image) Im $f$ của $f$.

<!-- PAGE 104 -->
Cơ bản tính chất của các cơ sở trong không gian vectơ (vector space) là rằng chúng cho phép định nghĩa của các ánh xạ tuyến tính (linear maps) như duy nhất homomorphic các mở rộng, như được hiển thị trong sau đây mệnh đề.

> **Mệnh đề 3.20.** Cho trước bất kỳ hai các không gian vectơ $E$ và $F$, cho trước bất kỳ cơ sở (basis) $(u_{i})_{i\in I}$ của $E$, cho trước bất kỳ khác họ của các vectơ $(v_{i})_{i\in I}$ trong $F$, các tính chất sau đây đúng.
$(1)$ Tồn tại duy nhất một ánh xạ tuyến tính (linear map) $f$: $E \to F$ sao cho $f(u_{i}) = v_{i}$ với mọi $i \in$ I.
$(2)$ ánh xạ $f$ là đơn ánh (injective) khi và chỉ khi $(v_{i})_{i\in I}$ là độc lập tuyến tính (linearly independent).
$(3)$ ánh xạ $f$ là toàn ánh (surjective) khi và chỉ khi $(v_{i})_{i\in I}$ sinh ra $F$.

*Chứng minh.* Nếu như vậy ánh xạ tuyến tính (linear map) $f$: $E \to F$ tồn tại, vì $(u_{i})_{i\in I}$ là cơ sở (basis) của $E$, mọi vectơ $x \in E$ có thể được viết một cách duy nhất như tổ hợp tuyến tính (linear combination)
$$x = \sum_{i\in I}  x_{i}u_{i},$$
Và bởi tính tuyến tính, ta phải có
$$f(x) = \sum_{i\in I}  x_{i}f(u_{i}) = \sum_{i\in I}  x_{i}v_{i}.$$
Định nghĩa hàm $f$: $E \to F$, bởi đặt
$$f(x) = \sum_{i\in I}  x_{i}v_{i},x = \sum_{i\in I}  x_{i}u_{i},(\dagger )$$
Với một số duy nhất các tọa độ $(x_{i})_{i\in I}$ của $x$. để chứng minh rằng $f$ như đã định nghĩa bởi $(\dagger$) là tuyến tính nó suffices để chứng minh rằng
$$f(\lambda x + \mu y) = \lambda f(x) + \mu f(y)$$
Với mọi $x, y \in E$ và tất cả $\lambda , \mu  \in \mathbb{R}$. Vì $(u_{i})_{i\in I}$ là cơ sở (basis) của $E$, ta có
$$x = \sum_{i\in I}  x_{i}u_{i},y = \sum_{i\in I}  y_{i}u_{i},$$
Với một số duy nhất các tọa độ $(x_{i})_{i\in I}$ của $x$ và $(y_{i})_{i\in I}$ của $y$, và bởi $(\dagger$) ta có
$$f(x) = \sum_{i\in I}  x_{i}v_{i},f(y) = \sum_{i\in I}  y_{i}v_{i},$$
$$and since \sum_{i\in I}  \sum_{i\in I}$$
$$\lambda x + \mu y = \lambda \begin{pmatrix} x_{i}u_{i} \end{pmatrix} + \mu \begin{pmatrix} y_{i}u_{i} \end{pmatrix} = \sum_{i\in I}  (\lambda x_{i} + \mu y_{i})u_{i},$$

<!-- PAGE 105 -->
Bởi $(\dagger$),
$$f(\lambda x + \mu y) = f \begin{pmatrix} (\lambda x_{i} + \mu y_{i})u_{i} \end{pmatrix} \sum_{i\in I}  = \sum_{i\in I}  (\lambda x_{i} + \mu y_{i})v_{i}$$
$$= \lambda \begin{pmatrix} x_{i}v_{i} \end{pmatrix} \sum_{i\in I}  + \mu \begin{pmatrix} y_{i}v_{i} \end{pmatrix} \sum_{i\in I}  = \lambda f(x) + \mu f(y),$$
Chứng minh rằng $f$ là tuyến tính. ánh xạ $f$ là duy nhất bởi $(\dagger$), và hiển nhiên, $f(u_{i}) = v_{i}$. Bây giờ giả sử rằng $f$ là đơn ánh (injective). Cho $(\lambda )_{i\in I}$ là bất kỳ họ của các vô hướng, và giả sử rằng
$$\sum_{i\in I}^{i}  \lambda_{i} v_{i} = 0.$$
Vì $v_{i} = f(u_{i})$ với mọi $i \in$ I, ta có
$$f \begin{pmatrix} \lambda_{i} u_{i} \end{pmatrix} \sum_{i\in I}  = \sum_{i\in I}  \lambda_{i} f(u_{i}) = \sum_{i\in I}  \lambda_{i} v_{i} = 0.$$
Vì $f$ là đơn ánh (injective) khi và chỉ khi Ker $f = (0)$, ta có
$$\sum_{i\in I}  \lambda_{i} u_{i} = 0,$$
Và vì $(u_{i})_{i\in I}$ là cơ sở (basis), ta có $\lambda_{i}  = 0$ với mọi $i \in$ I, mà chỉ ra rằng $(v_{i})_{i\in I}$ là độc lập tuyến tính (linearly independent). Ngược lại, giả sử rằng $(v_{i})_{i\in I}$ là độc lập tuyến tính (linearly independent). Vì $(u_{i})_{i\in I}$ là cơ sở (basis)
$$of E, every vector x \in E is a linear combination x = \sum_{i}  \in I \lambda_{i} u_{i} of (u_{i})_{i\in I}. If$$
$$f(x) = f \begin{pmatrix} \lambda_{i} u_{i} \end{pmatrix} \sum_{i\in I}  = 0,$$
$$then \sum_{i\in I}$$
$$\sum_{i\in I}  \lambda_{i} v_{i} = \sum_{i\in I}  \lambda_{i} f(u_{i}) = f \begin{pmatrix} \lambda_{i} u_{i} \end{pmatrix} = 0,$$
Và $\lambda_{i}  = 0$ với mọi $i \in$ I bởi vì $(v_{i})_{i\in I}$ là độc lập tuyến tính (linearly independent), mà có nghĩa là $x = 0$. Vì vậy, Ker $f = (0)$, mà suy ra rằng $f$ là đơn ánh (injective). phần ở đâu $f$ là toàn ánh (surjective) là trái như đơn giản bài tập. Trong trường hợp đặc biệt khi $E = K^{n}$ và $F = K^{m}$, ở đó là một cái khác chứng minh của Mệnh đề 3.20 theo các ma trận bằng cách sử dụng Mệnh đề 3.16. Trong trường hợp này, các vectơ $u_{1}, \dots  , u_{n}$ trong $K^{n}$ định nghĩa một ma trận cỡ $n \times  n$ $U = (u_{1} \cdots  u_{n})$ có cột thứ $j$ là $u_{j}$ và các vectơ $v_{1}, \dots  , v_{n}$ trong $K^{m}$ định nghĩa một ma trận cỡ $m \times  n$ $V = (v_{1} \cdots  v_{n})$ có cột thứ $j$ là $v_{j}$. Nếu $A$ là ma trận của ánh xạ tuyến tính (linear map) $f$: $K^{n} \to K^{m}$ (đối với chính tắc các cơ sở của $K^{n}$ và $K^{m})$ mà phải thỏa mãn các điều kiện $f(u_{j}) = v_{j}$ cho $j = 1, \dots  , n$, thì ta phải có
$$Au_{j} = v_{j},1 \le j \le n,$$

<!-- PAGE 106 -->
Mà là tương đương đến
$$AU = V,$$
Và vì $(u_{1}, \dots  , u_{n})$ là độc lập tuyến tính (linearly independent), chúng tạo thành cơ sở (basis) của $K^{n}$, do đó theo Mệnh đề 3.16 ma trận $U$ là khả nghịch và ta suy ra rằng $A$ được xác định bởi phương trình
$$A = V U^{-1} .$$
$$\mathbb{R}^{3} \mathbb{R}^{2}$$
Hình 3.11 cung cấp illustration của Mệnh đề 3.20 khi $E =$ và $V =$
$$f$$
$$3F =R2$$
$$E = R$$
$$u = (0,0,1)3$$
$$v = (1,1)1$$
$$v = (-1,1)2$$
$$\overline{u = (0,1,0)} 2\overline{v = (1,0)}$$
$$3$$
$$u  = (1,0,0)1$$
$$defining f$$
$$f(u )-f(u )$$
$$12$$
$$\overline{2f(u  )} 3$$
$$f is not injective$$

![Figure 3.11](../../assets/ch03/fig_3_11.png)

**Hình 3.11:** Cho trước $u_{1} = (1, 0, 0), u_{2} = (0, 1, 0), u_{3} = (0, 0, 1)$ và $v_{1} = (1, 1), v_{2} = (-1, 1)$,
$$\mathbb{R}^{3} \mathbb{R}^{2}$$
$v_{3} = (1, 0)$, định nghĩa duy nhất ánh xạ tuyến tính (linear map) $f$: $\to$ bởi $f(u_{1}) = v_{1}, f(u_{2}) = v_{2}$, và $f(u_{3}) = v_{3}$. ánh xạ này là toàn ánh (surjective) nhưng không đơn ánh (injective) vì $f(u_{1}$ - $u_{2}) = f(u_{1})$ - $f(u_{2}) = (1, 1)$ - $(-1, 1) = (2, 0) = 2f(u_{3}) = f(2u_{3})$. Bởi phần thứ hai của Mệnh đề 3.20, đơn ánh (injective) ánh xạ tuyến tính (linear map) $f$: $E \to F$ sends cơ sở (basis) $(u_{i})_{i\in I}$ đến độc lập tuyến tính (linearly independent) họ $(f(u_{i}))_{i\in I}$ của $F$, mà là cũng cơ sở (basis) khi $f$ là song ánh (bijective). Cũng, khi $E$ và $F$ có cùng hữu hạn số chiều $n, (u_{i})_{i\in I}$ là cơ sở (basis) của $E$, và $f$: $E \to F$ là đơn ánh (injective), thì $(f(u_{i}))_{i\in I}$ là cơ sở (basis) của $F$ (theo Mệnh đề 3.9). Ta có thể bây giờ chỉ ra rằng không gian vectơ (vector space) $K^{(I)}$ của Định nghĩa 3.11 có phổ dụng tính chất rằng tương đương với đến nói rằng rằng $K^{(I)}$ là không gian vectơ (vector space) một cách tự do được sinh bởi I. Nhắc lại rằng $\iota$: I $\to K^{(I)}$, sao cho $\iota (i) = e_{i}$ với mọi $i \in$ I, là đơn ánh từ I đến $K^{(I)}$.

> **Mệnh đề 3.21.** Cho trước bất kỳ tập hợp $I$, với mọi không gian vectơ (vector space) $F$, và với mọi hàm $f$: I $\to F$, tồn tại duy nhất một ánh xạ tuyến tính (linear map) $\overline{f}\overline{:} K^{(I)} \to F$, sao cho
$$f =\overline{f} \circ \iota ,$$
Như trong sau đây biểu đồ:
$$I\overline{C} K^{(I)}$$
$$\overline{C}^{\iota}\overline{C}$$
$$CC$$
$$CC$$
$$CC^{f}$$
$$f!$$
$$F$$

<!-- PAGE 107 -->

*Chứng minh.* Nếu như vậy ánh xạ tuyến tính (linear map) $\overline{f}\overline{:} K^{(I)} \to F$ tồn tại, vì $f =\overline{f} \circ \iota$, ta phải có
$$f(i) =\overline{f}(\iota (i)) =\overline{f}(e_{i}),$$
$$for every i \in I. However, the family (e_{i})_{i\in I} is a basis of K^{(I)}, and \frac{(}{f :} f(i))_{i\in I}  is a family of$$
Các vectơ trong $F$, và theo Mệnh đề 3.20, tồn tại duy nhất một ánh xạ tuyến tính (linear map) $K^{(I)} \to F$ sao cho
$$\overline{f}(e_{i}) = f(i) \frac{for}{f} every i \in I, which proves the existence and uniqueness of a linear map \overline{f}$$
Sao cho $f =  \circ \iota$. sau đây đơn giản mệnh đề là cũng hữu ích.

> **Mệnh đề 3.22.** Cho trước bất kỳ hai các không gian vectơ $E$ và $F$, với $F$ không tầm thường, cho trước bất kỳ họ $(u_{i})_{i\in I}$ của các vectơ trong $E$, các tính chất sau đây đúng:
$(1)$ họ $(u_{i})_{i\in I}$ sinh ra $E$ khi và chỉ khi với mọi họ của các vectơ $(v_{i})_{i\in I}$ trong $F$, ở đó là nhiều nhất một ánh xạ tuyến tính (linear map) $f$: $E \to F$ sao cho $f(u_{i}) = v_{i}$ với mọi $i \in$ I.
$(2)$ họ $(u_{i})_{i\in I}$ là độc lập tuyến tính (linearly independent) khi và chỉ khi với mọi họ của các vectơ $(v_{i})_{i\in I}$ trong $F$, tồn tại một ánh xạ tuyến tính (linear map) $f$: $E \to F$ sao cho $f(u_{i}) = v_{i}$ với mọi $i \in$ I.

*Chứng minh.* $(1)$ Nếu ở đó là bất kỳ ánh xạ tuyến tính (linear map) $f$: $E \to F$ sao cho $f(u_{i}) = v_{i}$ với mọi $i \in$ I, vì $(u_{i})_{i\in I}$ sinh ra $E$, mọi vectơ $x \in E$ có thể được viết dưới dạng một số tổ hợp tuyến tính (linear combination)
$$x = \sum_{i\in I}  x_{i}u_{i},$$
Và bởi tính tuyến tính, ta phải có
$$f(x) = \sum_{i\in I}  x_{i}f(u_{i}) = \sum_{i\in I}  x_{i}v_{i}.$$
Điều này chỉ ra rằng $f$ là duy nhất nếu nó tồn tại. Ngược lại, giả sử rằng $(u_{i})_{i\in I}$ thực hiện không sinh $E$. Vì $F$ là không tầm thường, tồn tại một một số vectơ $y \in F$ sao cho $y \neq  0$. Vì $(u_{i})_{i\in I}$ thực hiện không sinh $E$, tồn tại một vectơ $w \in E$ rằng là không trong không gian con được sinh bởi $(u_{i})_{i\in I}$. Theo Định lý 3.12, có một độc lập tuyến tính (linearly independent) họ con $(u_{i})_{i\in I0}$ của $(u_{i})_{i\in I}$ sinh cùng không gian con. Vì bởi giả thiết, $w \in E$ là không trong không gian con được sinh bởi $(u_{i})_{i\in I0}$, theo Bổ đề 3.7 và theo Định lý 3.12 một lần nữa, có một cơ sở (basis) $(e_{j})_{j\in I0\cup J}$ của $E$, sao cho $e_{i} = u_{i}$ với mọi $i \in I_{0}$, và $w = e_{j0}$ với một số $j_{0} \in J$. Đặt $(v_{i})_{i\in I}$ là họ trong $F$ sao cho $v_{i} = 0$ với mọi $i \in$ I, định nghĩa $f$: $E \to F$ là hằng số ánh xạ tuyến tính (linear map) với giá trị $0$, ta có ánh xạ tuyến tính (linear map) sao cho $f(u_{i}) = 0$ với mọi $i \in$ I. Theo Mệnh đề 3.20, tồn tại duy nhất một ánh xạ tuyến tính (linear map) $g: E \to F$ sao cho g(w) $= y$, và $g(e_{j}) = 0$ với mọi $j \in (I_{0} \cup J) -{j_{0}}$. Theo định nghĩa của cơ sở (basis) $(e_{j})_{j\in I0\cup J}$ của $E$, ta có $g(u_{i}) = 0$ với mọi $i \in$ I, và vì $f \neq  g$, điều này mâu thuẫn với sự kiện là ở đó là nhiều nhất một như vậy ánh xạ. Xem Hình 3.12.
$(2)$ Nếu họ $(u_{i})_{i\in I}$ là độc lập tuyến tính (linearly independent), thì theo Định lý 3.12, $(u_{i})_{i\in I}$ có thể được được mở rộng đến cơ sở (basis) của $E$, và conclusion suy ra theo Mệnh đề 3.20. Ngược lại, giả sử

<!-- PAGE 108 -->
$$3F =R2$$
$$w = (0,0,1)E = R$$
$$\overline{u = (0,1,0)} 2$$
$$u  = (1,0,0)1$$
$$defining f as the zero$$
$$g(w) = y$$
$$3F =R2$$
$$w = (0,0,1)E = R$$
$$\overline{u = (0,1,0)} 2\overline{y = (1,0)}$$
$$u  = (1,0,0)1defining g$$
$$\mathbb{R}^{3}  \mathbb{R}^{2}$$

![Figure 3.12](../../assets/ch03/fig_3_12.png)

**Hình 3.12:** Cho $E =$ và $F =$. các vectơ $u_{1} = (1, 0, 0), u_{2} = (0, 1, 0)$ thực hiện không
$$\mathbb{R}^{3}$$
Sinh vì cả hai không ánh xạ và ánh xạ $g$, ở đâu g(0, $0, 1) = (1, 0)$, send peach mặt phẳng $xy$ đến gốc. rằng $(u_{i})_{i\in I}$ là phụ thuộc tuyến tính (linearly dependent). Thì tồn tại một họ $(\lambda_{i} )_{i\in I}$ của các vô hướng (không tất cả không) sao cho
$$\sum_{i\in I}  \lambda_{i} u_{i} = 0.$$
Bởi giả định, với mọi khác không vectơ $y \in F$, với mọi $i \in$ I, tồn tại một ánh xạ tuyến tính (linear map) $f_{i}$: $E \to F$, sao cho $f_{i}(u_{i}) = y$, và $f_{i}(u_{j}) = 0$, cho $j \in$ I $-{i}$. Thì ta sẽ thu được
$$0 = f_{i}( \sum_{i\in I}  \lambda_{i} u_{i}) = \sum_{i\in I}  \lambda_{i} f_{i}(u_{i}) = \lambda_{i} y,$$
Và vì $y \neq  0$, điều này suy ra $\lambda_{i}  = 0$ với mọi $i \in$ I. Do đó, $(u_{i})_{i\in I}$ là độc lập tuyến tính (linearly independent). Cho trước các không gian vectơ $E, F$, và $G$, và các ánh xạ tuyến tính (linear maps) $f$: $E \to F$ và $g: F \to G$, dễ dàng kiểm chứng được rằng hợp thành $g \circ f$: $E \to G$ của $f$ và $g$ là ánh xạ tuyến tính (linear map).

> **Định nghĩa 3.21.** ánh xạ tuyến tính (linear map) $f$: $E \to F$ là đẳng cấu khi và chỉ khi có một ánh xạ tuyến tính (linear map) $g: F \to E$, sao cho
$$g \circ f = id_{E}andf \circ g = id_{F}.(*)$$

<!-- PAGE 109 -->
Ánh xạ $g$ trong Định nghĩa 3.21 là duy nhất. Điều này là bởi vì nếu $g$ và $h$ cả hai thỏa mãn $g\circ f = id_{E}, f \circ g = id_{F}, h \circ f = id_{E}$, và $f \circ h = id_{F}$, thì
$$g = g \circ id_{F} = g \circ (f \circ h) = (g \circ f) \circ h = id_{E} \circ h = h.$$
Ánh xạ $g$ thỏa mãn (*) ở trên được gọi là nghịch đảo của $f$ và nó cũng được ký hiệu bởi $f^{-1}$. Nhận thấy rằng Mệnh đề 3.20 chỉ ra rằng nếu $F =\mathbb{R}^{n}$, thì ta thu được đẳng cấu giữa bất kỳ không gian vectơ (vector space) $E$ có số chiều |J| $= n$ và $\mathbb{R}^{n}$. Mệnh đề 3.20 cũng suy ra rằng nếu $E$ và $F$ là hai các không gian vectơ, $(u_{i})_{i\in I}$ là cơ sở (basis) của $E$, và $f$: $E \to F$ là ánh xạ tuyến tính (linear map) mà là đẳng cấu, thì họ $(f(u_{i}))_{i\in I}$ là cơ sở (basis) của $F$. Một có thể kiểm chứng rằng nếu $f$: $E \to F$ là song ánh (bijective) ánh xạ tuyến tính (linear map), thì của nó nghịch đảo $f^{-1}: F \to E$, như hàm, là cũng ánh xạ tuyến tính (linear map), và do đó $f$ là đẳng cấu. Một cái khác hữu ích hệ quả của Mệnh đề 3.20 là điều này:

> **Mệnh đề 3.23.** Cho $E$ là không gian vectơ (vector space) của hữu hạn số chiều $n \ge 1$ và cho $f$: $E \to E$ là bất kỳ ánh xạ tuyến tính (linear map). Các tính chất sau đây đúng:
$(1)$ Nếu $f$ có nghịch đảo trái (left inverse) $g$, nghĩa là, nếu $g$ là ánh xạ tuyến tính (linear map) sao cho $g \circ f =$ id, thì $f$ là đẳng cấu và $f^{-1} = g$.
$(2)$ Nếu $f$ có nghịch đảo phải (right inverse) $h$, nghĩa là, nếu $h$ là ánh xạ tuyến tính (linear map) sao cho $f \circ h =$ id, thì $f$ là đẳng cấu và $f^{-1} = h$.

*Chứng minh.* $(1)$ phương trình $g \circ f =$ id suy ra rằng $f$ là đơn ánh (injective); điều này là tiêu chuẩn kết quả về các hàm (nếu f(x) $=$ f(y), thì g(f(x)) $=$ g(f(y)), mà suy ra rằng $x = y$ vì $g \circ f =$ id). Cho $(u_{1}, \dots  , u_{n})$ là bất kỳ cơ sở (basis) của $E$. Theo Mệnh đề 3.20, vì $f$ là đơn ánh (injective), $(f(u_{1}), \dots  , f(u_{n}))$ là độc lập tuyến tính (linearly independent), và vì $E$ có số chiều $n$, theo Mệnh đề 3.13(3), nó là cơ sở (basis) của $E$. Thì $f$ là song ánh (bijective), và bởi trước đó nhận xét nghịch đảo của nó là ánh xạ tuyến tính (linear map). Ta cũng có
$$g = g \circ id = g \circ (f \circ f^{-1}) = (g \circ f) \circ f^{-1}= id \circ f^{-1}= f^{-1}.$$
$(2)$ phương trình $f \circ h =$ id suy ra rằng $f$ là toàn ánh (surjective); điều này là tiêu chuẩn kết quả về các hàm (với mọi $y \in E$, ta có f(h(y)) $= y)$. Cho $(u_{1}, \dots  , u_{n})$ là bất kỳ cơ sở (basis) của $E$. Theo Mệnh đề 3.20, vì $f$ là toàn ánh (surjective), $(f(u_{1}), \dots  , f(u_{n}))$ sinh ra $E$, và vì $E$ có số chiều $n$, theo Mệnh đề 3.13(4), nó là cơ sở (basis) của $E$ Thì $f$ là song ánh (bijective), và bởi trước đó nhận xét nghịch đảo của nó là ánh xạ tuyến tính (linear map). Ta cũng có
$$h = id \circ h = (f^{-1}\circ f) \circ h = f^{-1}\circ (f \circ h) = f^{-1}\circ id = f^{-1}.$$
Điều này các đầy đủ chứng minh. Cho độc giả’s convenience ta compile khác nhau các tiêu chuẩn rằng ta được thiết lập (và một vài nhiều hơn/thêm) cho ma trận vuông (square matrix) là khả nghịch.

<!-- PAGE 110 -->

> **Mệnh đề 3.24.** Cho $A \in M_{n}(K)$ là ma trận vuông (square matrix) trên trường $K$ (trong hầu hết các trường hợp $K =\mathbb{R}$ hoặc $K =\mathbb{C})$. ma trận $A$ là khả nghịch khi và chỉ khi bất kỳ của các tính chất sau đây đúng.
$(1)$ phương trình Ax $= 0$ chỉ có tầm thường nghiệm $x = 0$.
$(2)$ Với mọi $b \in K^{n}$, phương trình Ax $= b$ có ít nhất một nghiệm $x \in K^{n}$.
$(3)$ Có một ma trận $B \in M_{n}(K)$ sao cho $BA = I_{n}$ (nghịch đảo trái (left inverse)). Trong điều này trường hợp $A^{-1} = B$.
$(4)$ Có một ma trận $C \in M_{n}(K)$ sao cho $AC = I_{n}$ (nghịch đảo phải (right inverse)). Trong điều này trường hợp $A^{-1} = C$.
$(5)$ ánh xạ tuyến tính (linear map) $x \mapsto$ Ax là đơn ánh (injective).
$(6)$ ánh xạ tuyến tính (linear map) $x \mapsto$ Ax là toàn ánh (surjective).
$(7)$ các cột của $A$ là độc lập tuyến tính (linearly independent).
$(8)$ các cột của $A$ sinh (span) $K^{n}$.
$(9)$ det() $\neq  0$ (xem Mệnh đề 7.10).
$(10)$ Khi Phép khử Gauss (Gaussian elimination) là performed trên $A$, tất cả các phần tử trụ là khác không (Định lý 8.1).
$(11)$ Khi chuyển đổi $A$ đến của nó rref (dạng bậc thang rút gọn theo hàng (RREF)) bằng cách sử dụng các phép biến đổi sơ cấp trên hàng, ma trận đơn vị (identity matrix) là thu được (Mệnh đề 8.18).
$(12)$ chuyển vị (transpose) $A^{\top}$ của $A$ là khả nghịch.

> **Định nghĩa 3.22.** Tập hợp tất cả các ánh xạ tuyến tính (linear maps) giữa hai các không gian vectơ $E$ và $F$ được ký hiệu bởi Hom(E, $F)$ hoặc bởi $\mathcal{L}(E; F)$ (ký hiệu $\mathcal{L}(E; F)$ là thường reserved đến tập hợp của liên tục các ánh xạ tuyến tính (linear maps), ở đâu $E$ và $F$ là các không gian vectơ định chuẩn). Khi ta muốn là nhiều hơn/thêm precise và specify trường $K$ trên mà các không gian vectơ $E$ và $F$ được định nghĩa ta viết $Hom_{K}(E, F)$. tập hợp Hom(E, $F)$ là không gian vectơ (vector space) dưới các phép toán được định nghĩa trong Ví dụ 3.1, cụ thể là
$$(f + g)(x) = f(x) + g(x)$$
Với mọi $x \in E$, và
$$(\lambda f)(x) = \lambda f(x)$$
Với mọi $x \in E$. điểm worth kiểm tra carefully là rằng $\lambda f$ là thật vậy ánh xạ tuyến tính (linear map), mà sử dụng tính giao hoán của * trong trường $K$ (typically, $K =\mathbb{R}$ hoặc $K =\mathbb{C})$. Thật vậy, ta có
$$(\lambda f)(\mu x) = \lambda f(\mu x) = \lambda \mu f(x) = \mu \lambda f(x) = \mu (\lambda f)(x).$$
Khi $E$ và $F$ có hữu hạn số chiều, không gian vectơ (vector space) Hom(E, $F)$ cũng có hữu hạn số chiều, như ta sẽ xem một cách ngắn.
