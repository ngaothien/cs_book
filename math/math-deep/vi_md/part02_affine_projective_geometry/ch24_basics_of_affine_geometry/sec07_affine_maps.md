# Các ánh xạ afin


<!-- PAGE 833 -->
$$\begin{pmatrix} a_{1} & b_{1} & c_{1} \\ a_{2} & b_{2} & c_{2} \\ a_{3} & b_{3} & c_{3} \end{pmatrix} \begin{pmatrix} \lambda_{0} \\ \lambda_{1} \\ \lambda_{2} \end{pmatrix} = \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \end{pmatrix} .$$
Tuy nhiên, có một bài toán khi gốc của tọa độ hệ thuộc đến mặt phẳng (, $b, c)$, vì trong trường hợp này, ma trận là không khả nghịch! Những gì ta nên một cách thực là thực hiện là để giải hệ
$$\longrightarrow \longrightarrow \longrightarrow  \longrightarrow$$
$$\lambda_{0} Oa + \lambda_{1} Ob + \lambda_{2} Oc =Ox,$$
Ở đâu $O$ là bất kỳ điểm không trong mặt phẳng (, $b, c)$. alternative là để sử dụng nhất định well-chosen cross các tích. Nó có thể được được hiển thị rằng tọa độ tỉ cự (barycentric coordinates) tương ứng với khác nhau các tỉ số của các diện tích và các thể tích; xem các bài tập.

## 24.7 Các ánh xạ afin

Tương ứng với các ánh xạ tuyến tính (linear maps) ta có khái niệm của ánh xạ afin (affine map). ánh xạ afin (affine map) được định nghĩa như ánh xạ bảo toàn các tổ hợp afin.
$$\longrightarrow  \longrightarrow$$

> **Định nghĩa 24.6.** Cho trước hai các không gian afin $E, E , +$ và E',E', $+'$, hàm $f$: $E \to$ E'
$$is an affine map iff for every family ((a_{i}, \lambda_{i} ))_{i\in I} of weighted points in E such that \sum_{i}  \in I \lambda_{i}  = 1,$$
Ta có
$$f \sum_{i\in I}  \lambda_{i} a_{i}!= \sum_{i\in I}  \lambda_{i} f(a_{i}).$$
Nói cách khác, $f$ bảo toàn các tâm tỉ cự. Các ánh xạ afin có thể được thu được từ các ánh xạ tuyến tính (linear maps) như sau. Để đơn giản của ký hiệu, cùng ký hiệu $+$ được sử dụng cho cả hai các không gian afin (thay vì của bằng cách sử dụng cả hai $+$ và $+')$.
$$\longrightarrow$$

> **Mệnh đề 24.7.** Cho trước bất kỳ điểm $a \in E$, bất kỳ điểm $b \in$ E', và bất kỳ ánh xạ tuyến tính (linear map) $h: E \to \longrightarrow$ E', ánh xạ $f$: $E \to$ E' được định nghĩa sao cho
$$f(a + v) = b + h(v)$$
Là ánh xạ afin (affine map).
$$Proof. Indeed, for any family (\lambda_{i} )_{i\in I} of scalars with \sum_{i}  \in I \lambda_{i}  = 1 and any family (v_{i})_{i\in I}, since$$
$$\sum_{i\in I}  \lambda_{i} (a + v_{i}) = a + \sum_{i\in I}  \lambda_{i} ----\longrightarrow a(a + v_{i}) = a + \sum_{i\in I}  \lambda_{i} v_{i}$$

<!-- PAGE 834 -->
Và
$$\sum_{i\in I}  \lambda_{i} (b + h(v_{i})) = b + \sum_{i\in I}  \lambda_{i} ------\longrightarrow b(b + h(v_{i})) = b + \sum_{i\in I}  \lambda_{i} h(v_{i}),$$
Ta có
$$f \sum_{i\in I}  \lambda_{i} (a + v_{i})!=fa + \sum_{i\in I}  \lambda_{i} v_{i}!$$
$$=b + h \sum_{i\in I}  \lambda_{i} v_{i}!$$
$$=b + \sum_{i\in I}  \lambda_{i} h(v_{i})$$
$$= \sum_{i\in I}  \lambda_{i} (b + h(v_{i}))$$
$$= \sum_{i\in I}  \lambda_{i} f(a + v_{i}),$$
Như đã khẳng định.
$$Note that the condition \sum_{i}  I \lambda_{i}  = 1 was implicitly used (in a hidden call to Proposition$$
24.1) trong deriving rằng
$$\sum_{i\in I}^{\in}  \lambda_{i} (a + v_{i}) = a + \sum_{i\in I}  \lambda_{i} v_{i}$$
Và
$$\sum_{i\in I}  \lambda_{i} (b + h(v_{i})) = b + \sum_{i\in I}  \lambda_{i} h(v_{i}).$$
Như nhiều hơn/thêm concrete ví dụ, ánh xạ
$$\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} \mapsto \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} + \begin{pmatrix} 3 \\ 1 \end{pmatrix}$$
Định nghĩa ánh xạ afin (affine map) $in\mathbb{A}^{2}$. Nó là “shear” theo sau bởi phép tịnh tiến. effect của điều này shear trên square (, $b, c, d)$ được hiển thị trong Hình 24.18. ảnh (image) của square (, $b, c, d)$ là hình bình hành (', b', c', d'). Cho chúng ta xét một nhiều hơn/thêm ví dụ. ánh xạ
$$\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} \mapsto \begin{pmatrix} 1 & 1 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} + \begin{pmatrix} 3 \\ 0 \end{pmatrix}$$
Là ánh xạ afin (affine map). Vì ta có thể viết
$$\sqrt$$
$$\begin{pmatrix} 1 & 1 \\ 1 & 3 \end{pmatrix} =\overline{2} \begin{pmatrix} \sqrt & \sqrt \\ \overline{2}/2 & -\sqrt{2}/2 \\ 2/2 & 2/2 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} ,$$

<!-- PAGE 835 -->
$$d= (5,2)c= (6,2)$$
$$d = (0,1)c = (1,1)$$
$$a\overline{= (3,1)}\overline{b}= (4,1)$$
$$\overline{a = (0,0)} b = (1,0)$$
$$Figure 24.18: The effect of a shear.$$
Điều này ánh xạ afin (affine map) là hợp thành của shear, theo sau bởi phép quay của góc $\pi /4$, theo sau bởi
$$\sqrt$$
Magnification của tỉ số $\overline{2,}$ theo sau bởi phép tịnh tiến. effect của ánh xạ này trên square (, $b, c, d)$ được hiển thị trong Hình 24.19. ảnh (image) của square (, $b, c, d)$ là hình bình hành (', b', c', d').
$$c= (5,4)$$
$$‘= (4,3)$$
$$d$$
$$d = (0,1)c= (1,1)$$
$$b= (4,1)$$
$$\overline{a = (0,0)}\overline{b = (1,0)} a= (3,0)$$
$$Figure 24.19: The effect of an affine map.$$
Sau đây mệnh đề chỉ ra điều ngược lại của những gì ta chỉ đã chỉ ra. Mọi ánh xạ afin (affine map) được xác định bởi ảnh (image) của bất kỳ điểm và ánh xạ tuyến tính (linear map).
$$\longrightarrow  \longrightarrow$$

> **Mệnh đề 24.8.** Cho trước ánh xạ afin (affine map) $f$: $E \to$ E', tồn tại duy nhất một ánh xạ tuyến tính (linear map) $f$: $E \to \longrightarrow$ E' sao cho
$$\longrightarrow$$
$$f(a + v) = f(a) +f (v),$$
$$\longrightarrow$$
Với mọi $a \in E$ và mọi $v \in E$.

*Chứng minh.* Cho $a \in E$ là bất kỳ điểm trong $E$. Ta khẳng định rằng ánh xạ được định nghĩa sao cho
$$\longrightarrow  --------\longrightarrow$$
$$f (v) =f(a)f(a + v)$$

<!-- PAGE 836 -->
$$\longrightarrow  \longrightarrow  \longrightarrow \longrightarrow$$
Với mọi $v \in E$ là ánh xạ tuyến tính (linear map) $f$: $E \to$ E'. Thật vậy, ta có thể viết
$$a + \lambda v = \lambda (a + v) + (1 -\lambda )a,$$
$$----\longrightarrow$$
$$\longrightarrow$$
Vì $a + \lambda v = a + \lambda$ ($+ v) + (1$ - $\lambda$)aa, và cũng
$$a + u + v = (a + u) + (a + v) -a,$$
$$----\longrightarrow  ----\longrightarrow$$
$$\longrightarrow$$
Vì $a + u + v = a +$ ($+ u) +$ ($+ v)$ - aa. Vì $f$ bảo toàn các tâm tỉ cự, ta thu được
$$f(a + \lambda v) = \lambda f(a + v) + (1 -\lambda )f(a).$$
$$If we recall that x = \sum_{i}  \in I \lambda_{i} a_{i} is the barycenter of a family ((a_{i}, \lambda_{i} ))_{i\in I} of weighted points$$
$$(with \sum_{i}  \in I \lambda_{i}  = 1) iff\longrightarrow \longrightarrow$$
$$bx = \sum_{i\in I}  \lambda_{i} ba_{i}for every b \in E,$$
Ta thu được
$$---------\longrightarrow --------\longrightarrow ----\longrightarrow --------\longrightarrow$$
$$f(a)f(a + \lambda v) = \lambda f(a)f(a + v) + (1 -\lambda )f(a)f(a) = \lambda f(a)f(a + v),$$
$$\longrightarrow \longrightarrow$$
Chỉ ra rằng $f (\lambda v) = \lambda f (v)$. Ta cũng có
$$f(a + u + v) = f(a + u) + f(a + v) -f(a),$$
Từ mà ta thu được
$$-----------\longrightarrow  --------\longrightarrow  --------\longrightarrow$$
$$f(a)f(a + u + v) =f(a)f(a + u) +f(a)f(a + v),$$
$$\longrightarrow  \longrightarrow  \longrightarrow  \longrightarrow$$
Chỉ ra rằng $f (u + v) = f (u) + f (v)$. Hệ quả là, $f$ là ánh xạ tuyến tính (linear map). Với mọi khác điểm $b \in E$, vì
$$\longrightarrow  ----\longrightarrow  \longrightarrow$$
$$\longrightarrow$$
$$b + v = a +ab + v = a +a(a + v) -aa +ab,$$
$b + v = (a + v)$ - $a + b$, và vì $f$ bảo toàn các tâm tỉ cự, ta thu được
$$f(b + v) = f(a + v) -f(a) + f(b),$$
Mà suy ra rằng
$$-------\longrightarrow -------\longrightarrow ----\longrightarrow  ----\longrightarrow$$
$$f(b)f(b + v)=f(b)f(a + v) -f(b)f(a) +f(b)f(b),$$
$$----\longrightarrow  -------\longrightarrow$$
$$=f(a)f(b) +f(b)f(a + v),$$
$$--------\longrightarrow$$
$$=f(a)f(a + v).$$
$-------\longrightarrow  --------\longrightarrow  \longrightarrow$ Do đó, f(b)f(b $+ v) =$ f()f($+ v)$, mà chỉ ra rằng định nghĩa của $f$ thực hiện không phụ thuộc
$$\longrightarrow  \longrightarrow$$
Trên lựa chọn của $a \in E$. sự kiện rằng $f$ là duy nhất là hiển nhiên: Ta phải có $f (v) = --------\longrightarrow$ f()f($+ v)$.

<!-- PAGE 837 -->
$$\longrightarrow  \longrightarrow \longrightarrow$$
Duy nhất ánh xạ tuyến tính (linear map) $f$: $E \to$ E' cho trước theo Mệnh đề 24.8 được gọi là ánh xạ tuyến tính (linear map) liên kết với ánh xạ afin (affine map) $f$. Lưu ý rằng điều kiện
$$\longrightarrow$$
$$f(a + v) = f(a) +f (v),$$
$$\longrightarrow$$
Với mọi $a \in E$ và mọi $v \in E$, có thể được được phát biểu tương đương như
$$\longrightarrow ----\longrightarrow  \longrightarrow$$
$$\longrightarrow \longrightarrow$$
$$f(x) = f(a) +f (ax),orf(a)f(x) =f (ax),$$
Với mọi, $x \in E$. Mệnh đề 24.8 chỉ ra rằng với mọi ánh xạ afin (affine map) $f$: $E \to$ E', có các điểm
$$\longrightarrow  \longrightarrow \longrightarrow$$
$a \in E, b \in$ E', và duy nhất ánh xạ tuyến tính (linear map) $f$: $E \to$ E', sao cho
$$\longrightarrow$$
$$f(a + v) = b +f (v),$$
$$\longrightarrow  \longrightarrow$$
Với mọi $v \in E$ (chỉ cho $b =$ f(), với mọi $a \in E)$. Các ánh xạ afin cho mà $f$ là đồng nhất thức
$$\longrightarrow$$
Ánh xạ được gọi là các phép tịnh tiến. Thật vậy, nếu $f =$ id,
$$\longrightarrow  --\longrightarrow$$
$$\longrightarrow  \longrightarrow  \longrightarrow  \longrightarrow$$
$$f(x)=f(a) +f (ax) = f(a) +ax = x +xa +af(a) +ax$$
$$--\longrightarrow  --\longrightarrow$$
$$\longrightarrow \longrightarrow$$
$$=x +xa +af(a) -xa = x +af(a),$$
Và do đó
$$--\longrightarrow  --\longrightarrow$$
$$xf(x) =af(a),$$
$$--\longrightarrow$$
Mà chỉ ra rằng $f$ là phép tịnh tiến được cảm sinh bởi vectơ af() (mà không phụ thuộc vào). Vì ánh xạ afin (affine map) bảo toàn các tâm tỉ cự, và vì không gian con afin (affine subspace) $V$ là đóng dưới barycentric các tổ hợp, ảnh (image) f(V) của $V$ là không gian con afin (affine subspace) trong E'. Do đó, ví dụ, ảnh (image) của đường thẳng là điểm hoặc đường thẳng, và ảnh (image) của mặt phẳng là hoặc điểm, đường thẳng, hoặc mặt phẳng. Dễ dàng kiểm chứng được rằng hợp thành của hai các ánh xạ afin là ánh xạ afin (affine map). Cũng, cho trước các ánh xạ afin $f$: $E \to$ E' và $g$: E' $\to$ E'', ta có
$$\longrightarrow$$
$$g(f(a + v)) = g \begin{pmatrix} \longrightarrow \\ f(a) +f(v) \end{pmatrix} = g(f(a)) +g \begin{pmatrix} \longrightarrow \\ f(v) \end{pmatrix} ,$$
$$-\longrightarrow  \longrightarrow \longrightarrow$$
Mà chỉ ra rằng $g \circ f = g \circ f$. Nó là dễ để chỉ ra rằng ánh xạ afin (affine map) $f$: $E \to$ E' là đơn ánh (injective) $\longrightarrow  \longrightarrow \longrightarrow \longrightarrow  \longrightarrow \longrightarrow$ khi và chỉ khi $f$: $E \to$ E' là đơn ánh (injective), và rằng $f$: $E \to$ E' là toàn ánh (surjective) khi và chỉ khi $f$: $E \to$ E' là toàn ánh (surjective).
$$\longrightarrow  \longrightarrow \longrightarrow$$
Ánh xạ afin (affine map) $f$: $E \to$ E' là hằng số khi và chỉ khi $f$: $E \to$ E' là null (hằng số) ánh xạ tuyến tính (linear map) bằng nhau
$$\longrightarrow$$
Đến $0$ với mọi $v \in E$. Nếu $E$ là không gian afin (affine space) có số chiều $m$ và $(a_{0}, a_{1}, \dots  , a_{m})$ là hệ quy chiếu afin (affine frame) cho $E$, thì với mọi khác không gian afin (affine space) $F$ và với mọi dãy $(b_{0}, b_{1}, \dots  , b_{m})$ của $m + 1$ các điểm trong $F$, ở đó

<!-- PAGE 838 -->
Là duy nhất ánh xạ afin (affine map) $f$: $E \to F$ sao cho $f(a_{i}) = b_{i}$, cho $0 \le i \le m$. Thật vậy, $f$ phải là sao cho
$$f(\lambda_{0} a_{0} + \cdots  + \lambda_{m} a_{m}) = \lambda_{0} b_{0} + \cdots  + \lambda_{m} b_{m},$$
Ở đâu $\lambda_{0} +\cdots +\lambda_{m}  = 1$, và điều này định nghĩa duy nhất ánh xạ afin (affine map) trên tất cả của $E$, vì $(a_{0}, a_{1}, \dots  , a_{m})$ là hệ quy chiếu afin (affine frame) cho $E$. Bằng cách sử dụng afin các hệ quy chiếu, các ánh xạ afin có thể được biểu diễn theo các ma trận. Ta giải thích cách mà ánh xạ afin (affine map) $f$: $E \to E$ được biểu diễn đối với hệ quy chiếu (frame) $(a_{0}, \dots  , a_{n})$ trong $E$, nhiều hơn/thêm tổng quát trường hợp ở đâu ánh xạ afin (affine map) $f$: $E \to F$ được biểu diễn đối với hai afin các hệ quy chiếu $(a_{0}, \dots  , a_{n})$ trong $E$ và $(b_{0}, \dots  , b_{m})$ trong $F$ đang là tương tự. Vì
$$\longrightarrow$$
$$f(a_{0} + x) = f(a_{0}) +f (x)$$
$$\longrightarrow$$
Với mọi $x \in E$, ta có
$$-------\longrightarrow  ---\longrightarrow  \longrightarrow$$
$$a_{0}f(a_{0} + x) =a_{0}f(a_{0}) +f (x).$$
$$---\longrightarrow  -------\longrightarrow$$
Vì $x, a_{0}f(a_{0})$, và $a_{0}f(a_{0} + x)$, có thể được biểu diễn dưới dạng
$$-\longrightarrow -\longrightarrow$$
$$x=x_{1}a_{0}a_{1} + \cdots  + x_{n}a_{0}a_{n},$$
$$---\longrightarrow$$
$$-\longrightarrow -\longrightarrow$$
$$a_{0}f(a_{0})=b_{1}a_{0}a_{1} + \cdots  + b_{n}a_{0}a_{n},$$
$$-------\longrightarrow$$
$$-\longrightarrow -\longrightarrow$$
$$a_{0}f(a_{0} + x)=y_{1}a_{0}a_{1} + \cdots  + y_{n}a_{0}a_{n},$$
$$\longrightarrow -\longrightarrow  -\longrightarrow$$
Nếu $A = (a_{i j})$ là ma trận cỡ $n\times n$ của ánh xạ tuyến tính (linear map) $f$ trên cơ sở (basis) $(a_{0}a_{1}, \dots  ,a_{0}a_{n})$, đặt $x, y$, và $b$ ký hiệu các vectơ cột của các thành phần $(x_{1}, \dots  , x_{n}), (y_{1}, \dots  , y_{n})$, và $(b_{1}, \dots  , b_{n})$,
$$-------\longrightarrow  ---\longrightarrow  \longrightarrow$$
$$a_{0}f(a_{0} + x) =a_{0}f(a_{0}) +f (x)$$
Là tương đương đến
$$y = Ax + b.$$
Lưu ý rằng $b \neq  0$ trừ khi $f(a_{0}) = a_{0}$. Do đó, $f$ là một cách tổng quát không phép biến đổi tuyến tính, trừ khi nó có cố định điểm, i.e., có một điểm $a_{0}$ sao cho $f(a_{0}) = a_{0}$. vectơ $b$ là “phép tịnh tiến phần” của ánh xạ afin (affine map). Các ánh xạ afin thực hiện không luôn luôn có cố định điểm. Hiển nhiên, khác không các phép tịnh tiến có không có cố định điểm. ít hơn tầm thường ví dụ được cho bởi ánh xạ afin (affine map)
$$\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} \mapsto \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} + \begin{pmatrix} 1 \\ 0 \end{pmatrix} .$$
Ánh xạ này là phép đối xứng (reflection) về trục $x$ theo sau bởi phép tịnh tiến dọc theo trục $x$. ánh xạ afin (affine map)
$$\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} \mapsto \begin{pmatrix} \sqrt \\ \sqrt1 & - & \overline{3} \\ 3/4 & 1/4 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} + \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$

<!-- PAGE 839 -->
Có thể cũng được viết như
$$\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} \mapsto \begin{pmatrix} 2 & 0 \\ 0 & 1/2 \end{pmatrix} \begin{pmatrix} \sqrt \\ \sqrt1/2 & - & \overline{3}/2 \\ 3/2 & 1/2 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} + \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$
Mà chỉ ra rằng nó là hợp thành của phép quay của góc $\pi /3$, theo sau bởi stretch (bởi nhân tử của $2$ dọc theo trục $x$, và bởi nhân tử $of^{1}$ dọc theo trục $y$), theo sau bởi phép tịnh tiến. Nó là dễ để chỉ ra rằng điều này ánh xạ afin (affine map) có $a^{2}$ duy nhất cố định điểm. Mặt khác, ánh xạ afin (affine map)
$$\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} \mapsto \begin{pmatrix} 8 \\ /5 & -6/5 \\ 3/10 & 2/5 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} + \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$
Có không có cố định điểm, chẵn/ngay cả dù
$$\begin{pmatrix} 8 \\ /5 & -6/5 \\ 3/10 & 2/5 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 1/2 \end{pmatrix} \begin{pmatrix} 4/5 & -3/5 \\ 3/5 & 4/5 \end{pmatrix} ,$$
Và thứ hai ma trận là phép quay của góc $\theta$ sao cho cos $\theta  =_{5}^{4}$ và sin $\theta  =_{5}^{3}$.
$$\longrightarrow$$
Để đơn giản hóa ký hiệu, cho trước bất kỳ hai các điểm $x, y$, cho chúng ta ký hiệu vectơ xy bởi $y$ - $x$ và ánh xạ tuyến tính (linear map) asociated với ánh xạ afin (affine map) $f$ bởi $h$. lý do cho bằng cách sử dụng các gốc và $b$ là rằng nó cho chúng ta nhiều hơn/thêm flexibility. Đặc biệt, ta có thể chọn $b =$ f(), và thì $f$ behaves like ánh xạ tuyến tính (linear map) đối với các gốc và $b =$ f(). Khi $E = F$, nếu tồn tại một $a \in E$ sao cho f() $= a$ (là cố định điểm của $f)$, thì ta có thể chọn $b = a$. Thì bởi vì f() $= a$, ta thu được
$$v = f(u) = f(a + u -a) = f(a) + h(u -a) = a + h(u -a),$$
Rằng là
$$v -a = h(u -a).$$
Đối với mới gốc, nếu ta định nghĩa $x$ và $y$ bởi
$$x = u -a$$
$$y = v -a,$$
Thì ta thu được
$$y = h(x).$$
Vì vậy, $f$ một cách thực behaves like ánh xạ tuyến tính (linear map), nhưng đối với mới gốc (không tiêu chuẩn gốc $0)$. Điều này là trường hợp của phép quay xung quanh trục rằng thực hiện không đi qua qua gốc. Ta bây giờ mô tả mẹo/kỹ thuật mà cho phép chúng ta đến incorporate phép tịnh tiến phần $d$ vào ma trận $A$. Điều này mẹo/kỹ thuật là rất hữu ích trong kinematics và dynamics, ở đâu $A$ là ma trận quay (rotation matrix). Như vậy các ánh xạ afin được gọi là cứng motions.

<!-- PAGE 840 -->
Ta định nghĩa ma trận cỡ $(m + 1) \times  (n + 1)$ ' thu được bởi thứ nhất cộng $d$ như $(n +$ 1)th cột và thì $(0, \dots  , 0, 1)$ như $(m +$ 1)th hàng:
$$| {z }$$
$$n$$
$$A'= \begin{pmatrix} A & d \\ 0_{n} & 1 \end{pmatrix} .$$
Rõ ràng là
$$\begin{pmatrix} y \\ 1 \end{pmatrix} = \begin{pmatrix} A & d \\ 0_{n} & 1 \end{pmatrix} \begin{pmatrix} x \\ 1 \end{pmatrix}$$
Khi và chỉ khi
$$y = Ax + d.$$
$$\mathbb{R}^{n}$$
Điều này tương đương với đến xét điểm $x \in$ như điểm $(x, 1)$ trong (afin) siêu phẳng (hyperplane) $H_{n+1} \mathbb{R}^{n+1}$ trong của phương trình $x_{n+1} = 1$. Thì ánh xạ afin (affine map) là thu hẹp đến siêu phẳng (hyperplane) $H_{n+1}$
$$\mathbb{R}^{n+1}  \mathbb{R}^{m+1}$$
Của ánh xạ tuyến tính (linear map) $f$ từ đến tương ứng với ma trận ' mà các ánh xạ $H_{n+1}$
$$b$$
Vào $H_{m+1} (f(H_{n+1}) \subseteq H_{m+1})$. Hình 24.20 minh họa điều này process cho $n = 2$.
$$b$$
$$x_{3}$$
$$(x_{1},x_{2}, 1)$$
$$H_{3} : x_{3} = 1$$
$$x_{2}$$
$$x = ( x_{1},x_{2})$$
$$x_{1}$$
$$\mathbb{R}^{n}  \mathbb{R}^{n+1}$$
$$Figure 24.20: Viewingas a hyperplane in(n = 2)$$
Ví dụ, ánh xạ
$$\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} \mapsto \begin{pmatrix} 1 & 1 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} + \begin{pmatrix} 3 \\ 0 \end{pmatrix}$$
$$\mathbb{R}^{3}$$
Định nghĩa ánh xạ afin (affine map) $f$ mà được biểu diễn trong bởi
$$\begin{pmatrix} x_{1} \\ x_{2} \\ 1 \end{pmatrix} \mapsto \begin{pmatrix} 1 & 1 & 3 \\ 1 & 3 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ 1 \end{pmatrix} .$$
