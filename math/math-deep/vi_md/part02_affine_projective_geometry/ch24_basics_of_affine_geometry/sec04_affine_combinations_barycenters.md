# Các tổ hợp afin, Các tâm tỉ cự


<!-- PAGE 816 -->
$$2 + (y + v)2$$
$$(x + u, y + v, (x + u))$$
$$P$$
$$(x, y, x  2+ y2 )$$
$$(u,v$$
$$)$$
$$(x, y)$$
$$(x + u, y + v)$$

![Figure 24.7](../../assets/ch24/fig_24_7.png)

**Hình 24.7:** paraboloid của revolution $P$ được quan điểm như hai chiều không gian afin (affine space).
$$\longrightarrow$$
Vì $a = a +$ aa và bởi (A1) $a = a + 0$, bởi (A3) ta thu được
$$\longrightarrow$$
$$aa = 0.$$
Do đó, đặt $a = c$ trong Chasles’s đồng nhất thức, ta thu được
$$\longrightarrow \longrightarrow$$
$$ba = -ab.$$
Cho trước bất kỳ bốn các điểm, $b, c, d \in E$, vì bởi Chasles’s đồng nhất thức
$$\longrightarrow  \longrightarrow  \longrightarrow  \longrightarrow  \longrightarrow$$
$$ab +bc =ad +dc =ac,$$
Ta có hình bình hành luật
$$\longrightarrow  \longrightarrow \longrightarrow  \longrightarrow$$
$$ab =dciffbc =ad.$$

## 24.4 Các tổ hợp afin, Các tâm tỉ cự

Cơ bản khái niệm trong tuyến tính đại số là rằng của tổ hợp tuyến tính (linear combination). tương ứng khái niệm trong afin hình học là rằng của tổ hợp afin (affine combination), cũng được gọi là tâm tỉ cự (barycenter). Tuy nhiên, có một bài toán với naive cách tiếp cận liên quan đến tọa độ hệ, như ta đã thấy trong Mục 24.1. Vì bài toán này là lý do cho giới thiệu các tổ hợp afin, tại risk của boring nhất định độc giả, ta cho một cái khác ví dụ chỉ ra những gì đi sai nếu ta là không careful trong định nghĩa các tổ hợp tuyến tính của các điểm.
$$\mathbb{R}^{2}$$
Xét như không gian afin (affine space), dưới của nó tự nhiên tọa độ hệ với gốc $O = (0, 0)$
$$and basis vectors \begin{pmatrix} 1 \\ 0 \end{pmatrix} and \begin{pmatrix} 0 \\ 1 \end{pmatrix} . Given any two points a = (a_{1}, a_{2}) and b = (b_{1}, b_{2}), it is$$

<!-- PAGE 817 -->
$$\longrightarrow$$
$$EE$$
$$b$$
$$\longrightarrow$$
$$ab$$
$$ac \frac{\longrightarrow ac}{\longrightarrow}$$
$$bc$$
$$Figure 24.8: Points and corresponding vectors in affine geometry.$$
Tự nhiên để định nghĩa tổ hợp afin (affine combination) $\lambda a + \mu b$ như điểm của các tọa độ
$$(\lambda a_{1} + \mu b_{1}, \lambda a_{2} + \mu b_{2}).$$
Do đó, khi $a = (-1, -1)$ và $b = (2, 2)$, điểm $a + b$ là điểm $c = (1, 1)$. Cho chúng ta bây giờ xét mới tọa độ hệ đối với gốc $c = (1, 1)$ (và cùng cơ sở (basis) các vectơ). Điều này time, các tọa độ của là $(-2, -2)$, các tọa độ của $b$ là $(1, 1)$, và điểm $a+b$ là điểm $d$ của các tọa độ $(-1, -1)$. Tuy nhiên, rõ ràng là điểm $d$ là đồng nhất đến gốc $O = (0, 0)$ của tọa độ thứ nhất hệ. tình huống này được minh họa trong Hình 24.9.
$$b = (1,1)$$
$$b = (2,2)$$
$$c =  a + b = (1,1)$$
$$\overline{c}$$
$$\overline{O = (0,0)}\overline{d = a + b = (-1,-1)}$$
$$a = (-1,-1)a = (-2, -2)$$
$$Figure 24.9: The example from the beginning of Section 24.4.$$
Do đó, $a + b$ tương ứng với hai khác nhau các điểm tùy thuộc trên mà tọa độ hệ được sử dụng cho của nó phép tính!

<!-- PAGE 818 -->
Điều này chỉ ra rằng một số extra điều kiện là cần thiết trong thứ tự cho các tổ hợp afin để tạo nghĩa. Hóa ra là nếu các vô hướng tổng sai khác $1$, định nghĩa là nội tại, như sau đây mệnh đề chỉ ra.

> **Mệnh đề 24.1.** Cho trước không gian afin (affine space) $E$, cho $(a_{i})_{i\in I}$ là họ của các điểm trong $E$, và cho $(\lambda_{i} )_{i\in I}$ là họ của các vô hướng. Với mọi hai các điểm, $b \in E$, các tính chất sau đây đúng:
$$(1) If \sum_{i}  \in I \lambda_{i}  = 1, then\longrightarrow \longrightarrow$$
$$a + \sum_{i\in I}  \lambda_{i} aa_{i} = b + \sum_{i\in I}  \lambda_{i} ba_{i}.$$
$$(2) If \sum_{i}  \in I \lambda_{i}  = 0, then\longrightarrow \longrightarrow$$
$$\sum_{i\in I}  \lambda_{i} aa_{i} = \sum_{i\in I}  \lambda_{i} ba_{i}.$$

*Chứng minh.* $(1)$ Bởi Chasles’s đồng nhất thức (xem Mục 24.3), ta có
$$a + \sum_{i\in I}  \lambda_{i} \longrightarrow aa_{i} = a + \sum_{i\in I}  \lambda_{i} (\longrightarrow ab + \longrightarrow ba_{i})$$
$$= a + \sum_{i\in I}  \longrightarrow ab + \sum_{i\in I}  \lambda_{i} \longrightarrow ba_{i}$$
$$\begin{pmatrix} \lambda_{i} \end{pmatrix}$$
$$= a + \longrightarrow ab + \sum_{i\in I}  \lambda_{i} \longrightarrow ba_{i}since \sum_{i}  \lambda_{i}  = 1$$
$$\in I$$
$$= b + \sum_{i\in I}  \lambda_{i} \longrightarrow ba_{i}since b = a + \longrightarrow ab.$$
$$\mathbb{A}^{2}$$
Illustration của điều này phép tính trong là miễn là/được cung cấp bởi Hình 24.10.
$(2)$ Ta cũng có
$$\sum_{i\in I}  \lambda_{i} \longrightarrow aa_{i}= \sum_{i\in I}  \lambda_{i} (\longrightarrow ab + \longrightarrow ba_{i})$$
$$= \sum_{i\in I}  \longrightarrow ab + \sum_{i\in I}  \lambda_{i} \longrightarrow ba_{i}$$
$$\begin{pmatrix} \lambda_{i} \\ \longrightarrow \end{pmatrix}$$
$$= \sum_{i\in I}  \lambda_{i} ba_{i},$$
$$since \sum_{i}  \in I \lambda_{i}  = 0.$$
Do đó, theo Mệnh đề 24.1, với mọi họ của các điểm $(a_{i})_{i\in I}$ trong $E$, với mọi họ $(\lambda_{i} )_{i\in I}$ của
$$scalars such that \sum_{i}  \in I \lambda_{i}  = 1, the point$$
$$x = a + \sum_{i\in I}  \lambda_{i} \longrightarrow aa_{i}$$

<!-- PAGE 819 -->
$$a$$
$$a2$$
$$2$$
$$\overline{a}\overline{a}$$
$$2\overline{b} \overline{a}$$
$$2a$$
$$\overline{a} \overline{a} a3$$
$$33aa$$
$$a\overline{a}\overline{a} a$$
$$11$$
$$1$$
$$\overline{a}\overline{a}$$
$$\overline{i}\overline{ab}$$
$$a$$
$$i\overline{b}\overline{a}$$
$$a$$
$$\overline{ab} i\overline{b}\overline{a} 3$$
$$1$$
$$bb$$
$$Figure 24.10: Part (1) of Proposition 24.1.$$
Là độc lập của lựa chọn của gốc $a \in E$. tính chất này motivates sau đây định nghĩa.

> **Định nghĩa 24.2.** Với mọi họ của các điểm $(a_{i})_{i\in I}$ trong $E$, với mọi họ $(\lambda_{i} )_{i\in I}$ của các vô hướng như vậy
$$that \sum_{i}  \in I \lambda_{i}  = 1, and for any a \in E, the point$$
$$a + \sum_{i\in I}  \lambda_{i} \longrightarrow aa_{i}$$
(mà là độc lập của $a \in E$, theo Mệnh đề 24.1) được gọi là tâm tỉ cự (barycenter) (hoặc barycentric tổ hợp, hoặc tổ hợp afin (affine combination)) của các điểm $a_{i}$ assigned các trọng số $\lambda_{i}$, và nó được ký hiệu bởi
$$\sum_{i\in I}  \lambda_{i} a_{i}.$$
Trong dealing với các tâm tỉ cự, nó là thuận tiện đến giới thiệu khái niệm của được trọng số điểm, mà là chỉ cặp $(a, \lambda$), ở đâu $a \in E$ là điểm, và $\lambda  \in \mathbb{R}$ là vô hướng (scalar). Thì, cho trước họ
$$of weighted points ((a_{i}, \lambda_{i} ))_{i\in I}, where \sum_{i}  \lambda_{i}  = 1, we also say that the point \sum_{i}  \in I \lambda_{i} a_{i} is$$
Tâm tỉ cự (barycenter) của họ của $weighted^{\in I}$ các điểm $((a_{i}, \lambda_{i} ))_{i\in I}$. Lưu ý rằng tâm tỉ cự (barycenter) $x$ của họ của được trọng số các điểm $((a_{i}, \lambda_{i} ))_{i\in I}$ là duy nhất điểm sao cho
$$\longrightarrow \longrightarrow$$
$$ax = \sum_{i\in I}  \lambda_{i} aa_{i}for every a \in E,$$
Và đặt $a = x$, điểm $x$ là duy nhất điểm sao cho
$$\sum_{i\in I}  \lambda_{i} \longrightarrow xa_{i} = 0.$$

<!-- PAGE 820 -->
Trong vật lý các số hạng, tâm tỉ cự (barycenter) là tâm của mass của họ của được trọng số các điểm
$$((a_{i}, \lambda_{i} ))_{i\in I} (where the masses have been normalized, so that \sum_{i}  \in I \lambda_{i}  = 1, and negative$$
Masses được phép).
Các nhận xét:
$(1)$ Vì tâm tỉ cự (barycenter) của họ $((a_{i}, \lambda_{i} ))_{i\in I}$ của được trọng số các điểm được định nghĩa cho các họ
$$(\lambda_{i} )_{i\in I} of scalars with finite support (and such that \sum_{i}  \lambda_{i}  = 1), we might as well$$
Giả sử rằng I là hữu hạn. Thì, với mọi $m \ge 2$, nó là $easy^{\in I}$ để chứng minh rằng tâm tỉ cự (barycenter) của $m$ được trọng số các điểm có thể được thu được bởi repeated các phép tính của các tâm tỉ cự của hai được trọng số các điểm.
$(2)$ kết quả này vẫn nghiệm đúng, miễn là/được cung cấp rằng trường $K$ có ít nhất ba phân biệt các phần tử, nhưng chứng minh là trickier!
$$\longrightarrow$$
$$(3) When \sum_{i}  \lambda  = 0, the vector \sum  i\in I \lambda_{i} aa_{i} does not depend on the point a, and we may$$
$$denote it^{\in I} by \sum_{i}^{i}  \in I \lambda_{i} a_{i}. This observation will be used to define a vector space in which$$
Các tổ hợp tuyến tính của cả hai các điểm và các vectơ tạo nghĩa, regardless của giá trị của
$$\sum_{i}  \in I \lambda_{i} .$$
Hình 24.11 minh họa hình học cách xây dựng của các tâm tỉ cự $g_{1}$ và $g_{2}$ của
$$weighted points \begin{pmatrix} a,_{4}^{1} \\ can \end{pmatrix} , \begin{pmatrix} b,_{4}^{1} \end{pmatrix} , and \begin{pmatrix} c,_{2}^{1} \end{pmatrix} , and (a, -1), (b, 1), and (c, 1).$$
Điểm $g_{1}$ được xây dựng geometrically như giữa của đoạn thẳng joining $c$ đến $middle_{2}^{1} a +_{2}^{1} b$ của đoạn thẳng (, $b)$, vì
$$g_{1} = \frac{1}{2} \begin{pmatrix} 1 & 1 \\ a + & b \\ 2 & 2 \end{pmatrix} + \frac{1}{2} c.$$
Điểm $g_{2}$ có thể được được xây dựng geometrically như điểm sao cho $middle_{2}^{1} b +_{2}^{1} c$ của đoạn thẳng $(b, c)$ là giữa của đoạn thẳng (, $g_{2})$, vì
$$g_{2} = -a + 2 \begin{pmatrix} 1 & 1 \\ b + & c \\ 2 & 2 \end{pmatrix} .$$
Sau này, ta sẽ xem rằng đa thức đường cong có thể được được định nghĩa như tập hợp của các tâm tỉ cự của cố định số của các điểm. Ví dụ, cho (, $b, c, d)$ là dãy của các điểm trong $\mathbb{A}^{2}$. Nhận thấy rằng
$$(1 -t)^{3}+ 3t(1 -t)^{2}+ 3t^{2}(1 -t) + t^{3}= 1,$$
Vì tổng trên vế trái là thu được bởi expanding $(t + (1$ - $t))^{3} = 1$ bằng cách sử dụng nhị thức công thức. Do đó,
$$(1 -t)^{3}a + 3t(1 -t)^{2}b + 3t^{2}(1 -t) c + t^{3}d$$
