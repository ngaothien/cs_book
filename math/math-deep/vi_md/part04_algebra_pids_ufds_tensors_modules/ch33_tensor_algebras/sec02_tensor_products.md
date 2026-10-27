# Các tích tenxơ


<!-- PAGE 1174 -->
$$\mathbb{R}^{2}\mathbb{R}^{2} \mathbb{R}$$
Ta demonstrate cách mà để tính toán tr(f) ở đâu $f$: $\times \to$ với $f((x_{1}, y_{1}), (x_{2}, y_{2})) = x_{1}x_{2}+2x_{2}y_{1}+3x_{1}y_{2}-y_{1}y_{2}$. Dưới tiêu chuẩn cơ sở (basis) $for\mathbb{R}^{2}$, dạng song tuyến tính (bilinear form) $f$ được biểu diễn như
$$\begin{pmatrix} x_{1} & y_{1} \end{pmatrix} \begin{pmatrix} 1 & 3 \\ 2 & -1 \end{pmatrix} \begin{pmatrix} x_{2} \\ y_{2} \end{pmatrix} .$$
Vì trong trình bày trường hợp $G = I_{2}$, ma trận này biểu diễn chỉ ra rằng
$$\top$$
$$f^{\natural} = \begin{pmatrix} 1 & 3 \\ 2 & -1 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix} ,$$
Và do đó
$$\mathrm{tr}(f) = \mathrm{tr}(f^{\natural} ) = \mathrm{tr} \begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix} = 0.$$
Ta sẽ cũng cần sau đây mệnh đề để chỉ ra rằng khác nhau các họ là độc lập tuyến tính (linearly independent).

> **Mệnh đề 33.4.** Cho $E$ và $F$ là hai không tầm thường các không gian vectơ và cho $(u_{i})_{i\in I}$ là bất kỳ họ của các vectơ $u_{i} \in E$. họ $(u_{i})_{i\in I}$ là độc lập tuyến tính (linearly independent) khi và chỉ khi với mọi họ $(v_{i})_{i\in I}$ của các vectơ $v_{i} \in F$, tồn tại một ánh xạ tuyến tính (linear map) $f$: $E \to F$ sao cho $f(u_{i}) = v_{i}$ với mọi $i \in$ I.

*Chứng minh.* Để lại như một bài tập.

## 33.2 Các tích tenxơ

Thứ nhất ta định nghĩa các tích tenxơ, và thì ta chứng minh của chúng sự tồn tại và tính duy nhất sai khác một đẳng cấu (up to isomorphism).

> **Định nghĩa 33.4.** Cho $K$ là cho trước trường, và cho $E_{1}, \dots  , E_{n}$ là $n \ge 2$ cho trước các không gian vectơ. Với mọi không gian vectơ (vector space) $F$, ánh xạ $f$: $E_{1} \times  \cdots  \times  E_{n} \to F$ là đa tuyến tính khi và chỉ khi nó là tuyến tính trong mỗi của của nó argument; nghĩa là,
$$f(u_{1}, \dots  u_{i1}, v + w, u_{i+1}, \dots  , u_{n})=f(u_{1}, \dots  u_{i1}, v, u_{i+1}, \dots  , u_{n})$$
$$+ f(u_{1}, \dots  u_{i1}, w, u_{i+1}, \dots  , u_{n})$$
$$f(u_{1}, \dots  u_{i1}, \lambda v, u_{i+1}, \dots  , u_{n})=\lambda f(u_{1}, \dots  u_{i1}, v, u_{i+1}, \dots  , u_{n}),$$
Với mọi $u_{j} \in E_{j} (j \neq  i)$, tất cả $v, w \in E_{i}$ và tất cả $\lambda  \in K$, cho $i = 1 \dots  , n$. tập hợp của đa tuyến tính các ánh xạ như ở trên các dạng không gian vectơ (vector space) được ký hiệu $L(E_{1}, \dots  , E_{n}; F)$ hoặc $Hom(E_{1}, \dots  , E_{n}; F)$. Khi $n = 1$, ta có không gian vectơ (vector space) của các ánh xạ tuyến tính (linear maps) L(E, $F)$ (cũng được ký hiệu Hom(E, $F))$. (là rất precise, ta viết $Hom_{K}(E_{1}, \dots  , E_{n}; F)$ và $Hom_{K}(E, F).)$

<!-- PAGE 1175 -->

> **Định nghĩa 33.5.** tích tenxơ (tensor product) của $n \ge 2$ các không gian vectơ $E_{1}, \dots  , E_{n}$ là không gian vectơ (vector space) $T$ cùng với ánh xạ đa tuyến tính (multilinear map) $\phi$: $E_{1} \times  \cdots  \times  E_{n} \to T$, sao cho với mọi không gian vectơ (vector space) $F$ và với mọi ánh xạ đa tuyến tính (multilinear map) $f$: $E_{1}\times \cdots \times E_{n} \to F$, tồn tại duy nhất một ánh xạ tuyến tính (linear map) $f_{\otimes}: T \to F$ với
$$f(u_{1}, \dots  , u_{n}) = f_{\otimes}(\phi (u_{1}, \dots  , u_{n})),$$
Với mọi $u_{1} \in E_{1}, \dots  , u_{n} \in E_{n}$, hoặc cho ngắn
$$f = f_{\otimes}\circ \phi .$$
Tương đương, tồn tại duy nhất một ánh xạ tuyến tính (linear map) $f_{\otimes}$ sao cho sau đây biểu đồ giao hoán.
$$\phi  /$$
$$E_{1} \times  \cdots  \times  E_{n}T$$
$$NN$$
$$NN$$
$$NN$$
$$NN$$
$$NN$$
$$fN^{f\otimes}&$$
$$F$$
Ở trên tính chất được gọi là phổ dụng ánh xạ tính chất của tích tenxơ (tensor product) $(T, \phi$). Ta chỉ ra rằng bất kỳ hai các tích tenxơ $(T_{1}, \phi_{1}$) và $(T_{2}, \phi_{2}$) cho $E_{1}, \dots  , E_{n}$, là đẳng cấu.

> **Mệnh đề 33.5.** Cho trước bất kỳ hai các tích tenxơ $(T_{1}, \phi_{1}$) và $(T_{2}, \phi_{2}$) cho $E_{1}, \dots  , E_{n}$, có một đẳng cấu $h: T_{1} \to T_{2}$ sao cho
$$\phi_{2}  = h \circ \phi_{1} .$$

*Chứng minh.* Focusing trên $(T_{1}, \phi_{1}$), ta có ánh xạ đa tuyến tính (multilinear map) $\phi_{2}$: $E_{1} \times  \cdots  \times  E_{n} \to T_{2}$, và do đó tồn tại duy nhất một ánh xạ tuyến tính (linear map) $(\phi_{2} )_{\otimes}: T_{1} \to T_{2}$ với
$$\phi_{2}  = (\phi_{2} )_{\otimes}\circ \phi_{1}$$
Như được minh họa bởi sau đây giao hoán biểu đồ.
$$/$$
$$E_{1} \times  \cdots  \times  E_{n}^{\phi1}T_{1}$$
$$MM$$
$$MM$$
$$MM$$
$$MM(\phi )$$
$$MM2\otimes$$
$$\phi 2MM$$
$$&$$
$$T_{2}$$
Tương tự, focusing bây giờ trên trên $(T_{2}, \phi_{2}$), ta có ánh xạ đa tuyến tính (multilinear map) $\phi_{1}$: $E_{1} \times  \cdots  \times  E_{n} \to T_{1}$, và do đó tồn tại duy nhất một ánh xạ tuyến tính (linear map) $(\phi_{1} )_{\otimes}: T_{2} \to T_{1}$ với
$$\phi_{1}  = (\phi_{1} )_{\otimes}\circ \phi_{2}$$

<!-- PAGE 1176 -->
Như được minh họa bởi sau đây giao hoán biểu đồ.
$$/$$
$$E_{1} \times  \cdots  \times  E_{n}^{\phi2}T_{2}$$
$$MM$$
$$MM$$
$$MM$$
$$MM(\phi )$$
$$MM1\otimes$$
$$\phi 1MM$$
$$&$$
$$T_{1}$$
Đặt các phần tử này các biểu đồ cùng nhau, ta thu được giao hoán các biểu đồ
$$T_{1}$$
$$q8$$
$$qq$$
$$\phi qq$$
$$q^{1}q$$
$$qq(\phi 2)\otimes$$
$$qq$$
$$/$$
$$E_{1} \times  \cdots  \times  E_{n}^{\phi2}T_{2}$$
$$MM$$
$$MM$$
$$MM$$
$$MM(\phi )$$
$$MM1\otimes$$
$$\phi 1MM$$
$$&$$
$$T_{1}$$
Và
$$8T_{2}$$
$$pp$$
$$pp$$
$$pp$$
$$pp(\phi )$$
$$pp^{\phi2}1\otimes$$
$$pp$$
$$E_{1} \times  \cdots  \times  E_{n}^{\phi1} /T_{1}$$
$$NN$$
$$NN$$
$$NN$$
$$NN(\phi )$$
$$\phi NN2\otimes$$
$$2N&$$
$$T_{2},$$
Mà có nghĩa là
$$\phi_{1}  = (\phi_{1} )_{\otimes}\circ (\phi_{2} )_{\otimes}\circ \phi_{1} and\phi_{2}  = (\phi_{2} )_{\otimes}\circ (\phi_{1} )_{\otimes}\circ \phi_{2} .$$
Mặt khác, focusing trên $(T_{1}, \phi_{1}$), ta có ánh xạ đa tuyến tính (multilinear map) $\phi_{1}$: $E_{1} \times  \cdots  \times  E_{n} \to T_{1}$, nhưng duy nhất ánh xạ tuyến tính (linear map) $h: T_{1} \to T_{1}$ với
$$\phi_{1}  = h \circ \phi_{1}$$
Là $h =$ id, như được minh họa bởi sau đây giao hoán biểu đồ
$$E_{1} \times  \cdots  \times  E_{n}^{\phi1} /T_{1}$$
$$NN$$
$$NN$$
$$NN$$
$$NNid$$
$$\phi NN$$
$$1N&$$
$$T_{1},$$
Và vì $(\phi_{1} )_{\otimes} \circ (\phi_{2} )_{\otimes}$ là tuyến tính như hợp thành của các ánh xạ tuyến tính (linear maps), ta phải có
$$(\phi_{1} )_{\otimes}\circ (\phi_{2} )_{\otimes}= id.$$

<!-- PAGE 1177 -->
Tương tự, ta có giao hoán biểu đồ
$$E_{1} \times  \cdots  \times  E_{n}^{\phi2} /T_{2}$$
$$NN$$
$$NN$$
$$NN$$
$$NNid$$
$$\phi NN$$
$$2N&$$
$$T_{2},$$
Và ta phải có
$$(\phi_{2} )_{\otimes}\circ (\phi_{1} )_{\otimes}= id.$$
Điều này chỉ ra rằng $(\phi_{1} )_{\otimes}$ và $(\phi_{2} )_{\otimes}$ là nghịch đảo các ánh xạ tuyến tính (linear maps), và do đó, $(\phi_{2} )_{\otimes}: T_{1} \to T_{2}$ là đẳng cấu giữa $T_{1}$ và $T_{2}$. Bây giờ rằng ta có được hiển thị rằng các tích tenxơ là duy nhất sai khác một đẳng cấu (up to isomorphism), ta cho cách xây dựng rằng produces chúng. Các tích tenxơ là thu được từ tự do các không gian vectơ bởi thương process, do đó cho chúng ta bắt đầu bởi mô tả cách xây dựng của tự do không gian vectơ (vector space) được sinh bởi tập hợp. Để đơn giản giả sử rằng của ta tập hợp $I$ là hữu hạn, nói
$$I = {♥, ♦, ♠, ♣}.$$
Cách xây dựng hoạt động với mọi trường $K$ (và thực ra với mọi vành giao hoán (commutative ring) $A$, trong mà trường hợp ta thu được tự do A-module được sinh bởi I). Giả sử rằng $K = \mathbb{R}$. tự do không gian vectơ (vector space) được sinh bởi I là tập hợp tất cả hình thức các tổ hợp tuyến tính của tạo thành
$$a♥+ b♦+ c♠+ d♣,$$
Với, $b, c, d \in \mathbb{R}$. Nó được giả sử rằng thứ tự của các số hạng thực hiện không matter. Ví dụ,
$$2♥-5♦+ 3♠= -5♦+ 2♥+ 3♠.$$
Phép cộng và phép nhân bởi vô hướng (scalar) là được định nghĩa như sau: $(a_{1}♥ + b_{1}♦ + c_{1}♠ + d_{1}♣) + (a_{2}♥ + b_{2}♦ + c_{2}♠ + d_{2}♣)$
$$= (a_{1} + a_{2})♥+ (b_{1} + b_{2})♦+ (c_{1} + c_{2})♠+ (d_{1} + d_{2})♣,$$
Và
$$\alpha  \cdot  (a♥+ b♦+ c♠+ d♣) = \alpha a♥+ \alpha b♦+ \alpha c♠+ \alpha d♣,$$
Với mọi, $b, c, d, \alpha  \in \mathbb{R}$. Với các phần tử này các phép toán, ta kiểm chứng được ngay rằng ta thu được
$$\mathbb{R}^{(I)} \mathbb{R}^{(I)}$$
Không gian vectơ (vector space) được ký hiệu. tập hợp $I$ có thể được được quan điểm như được nhúng trong bởi đơn ánh $\iota$ cho trước bởi
$$\iota (♥) = 1♥,\iota (♦) = 1♦,\iota (♠) = 1♠,\iota (♣) = 1♣.$$
$\mathbb{R}^{(I)}$ Do đó, có thể được được quan điểm như không gian vectơ (vector space) với đặc biệt cơ sở (basis) $I = {♥$, ♦, ♠, $♣}$. Trong của ta $\mathbb{R}^{(I)}  \mathbb{R}^{4}$ trường hợp, là isomorophic đến.

<!-- PAGE 1178 -->
Chính xác cùng cách xây dựng hoạt động với mọi trường $K$, và ta thu được không gian vectơ (vector space) được ký hiệu bởi $K^{(I)}$ và đơn ánh $\iota$: I $\to K^{(I)}$. chính lý do tại sao tự do không gian vectơ (vector space) $K^{(I)}$ trên tập hợp $I$ là thú vị là rằng nó thỏa mãn phổ dụng ánh xạ tính chất. Điều này có nghĩa là với mọi không gian vectơ (vector space) $F$ (trên
$$field K), \frac{any}{h} function  h: I \to F, where F is considered just a set, has a unique linear$$
Mở rộng: $K^{(I)} \to F$. Bởi mở rộng, ta có nghĩa rằng $\overline{h}(i) =$ h(i) với mọi $i \in$ I, hoặc nhiều hơn/thêm một cách chặt chẽ rằng $h =\overline{h} \circ \iota$. Ví dụ, nếu $I = {♥$, ♦, ♠, $♣}, K =\mathbb{R}$, và $F =\mathbb{R}^{3}$, hàm $h$ cho trước bởi
$$h(♥) = (1, 1, 1),h) = (1, 1, 0),h(♠) = (1, 0, 0),h(♣) = (0, 0 -1)$$
$$has a unique linear extension \frac{(♦}{h} : \mathbb{R}^{(I)} \mathbb{R}^{3} to the free vector space \mathbb{R}^{(I)}, given by$$
$$\overline{h}(a♥+ b♦+ c♠+ d♣) = \frac{\to}{ah} (♥) +\overline{bh}(♦) +\overline{ch}(♠) +\overline{dh}(♣)$$
$$= ah(♥) + bh(♦) + ch(♠) + dh(♣)$$
$$= a(1, 1, 1) + b(1, 1, 0) + c(1, 0, 0) + d(0, 0, -1)$$
$$= (a + b + c, a + b, a -d).$$
Đến tổng quát hóa cách xây dựng của tự do không gian vectơ (vector space) đến vô hạn các tập hợp I, ta nhận thấy rằng hình thức tổ hợp tuyến tính (linear combination) ♥ $+$ b♦ $+$ c♠ $+$ d♣ có thể được được quan điểm như hàm $f$: I $\to \mathbb{R}$ cho trước bởi
$$f(♥) = a,f(♦) = b,f(♠) = c,f(♣) = d,$$
Ở đâu, $b, c, d \in \mathbb{R}$. Tổng quát hơn, ta có thể thay thế $\mathbb{R}$ bởi bất kỳ trường $K$. Nếu I là hữu hạn, thì tập hợp tất cả như vậy các hàm là không gian vectơ (vector space) dưới từng điểm phép cộng và từng điểm vô hướng (scalar) phép nhân. Nếu I là vô hạn, vì phép cộng và vô hướng (scalar) phép nhân chỉ làm cho nghĩa cho hữu hạn các vectơ, ta đòi hỏi rằng của ta các hàm $f$: I $\to K$ lấy giá trị $0$ ngoại trừ cho có thể một cách hữu hạn nhiều các đối số/lập luận. Ta có thể nghĩ của như vậy các hàm như vô hạn các dãy $(f_{i})_{i\in I}$ của các phần tử $f_{i}$ của $K$ được chỉ số bởi I, với chỉ một cách hữu hạn nhiều khác không $f_{i}$. formalization của cách xây dựng này đi như sau. Cho trước bất kỳ tập hợp $I$ được quan điểm như chỉ số tập hợp, cho $K^{(I)}$ là tập hợp tất cả các hàm $f$: I $\to K$ sao cho f(i) $\neq  0$ chỉ cho một cách hữu hạn nhiều $i \in$ I. Như thông thường, ký hiệu như vậy hàm bởi $(f_{i})_{i\in I}$; nó là họ của hữu hạn hỗ trợ/giá (support). Ta tạo $K^{(I)}$ vào không gian vectơ (vector space) bởi định nghĩa phép cộng và vô hướng (scalar) phép nhân bởi
$$(f_{i}) + (g_{i})=(f_{i} + g_{i})$$
$$\lambda (f_{i})=(\lambda f_{i}).$$
Họ $(e_{i})_{i\in I}$ được định nghĩa sao cho $(e_{i})_{j} = 0$ nếu j̸ $= i$ và $(e_{i})_{i} = 1$. Nó là cơ sở (basis) của không gian vectơ (vector space) $K^{(I)}$, sao cho mọi $w \in K^{(I)}$ có thể được một cách duy nhất được viết như hữu hạn tổ hợp tuyến tính (linear combination) của $e_{i}$. Ở đó là cũng đơn ánh $\iota$: I $\to K^{(I)}$ sao cho $\iota (i) = e_{i}$ với mọi $i \in$ I. Hơn nữa, nó là dễ để chỉ ra rằng với mọi không gian vectơ (vector space) $F$, và với mọi hàm

<!-- PAGE 1179 -->
$h$: I $\to F$, tồn tại duy nhất một ánh xạ tuyến tính (linear map) $\overline{h}: K^{(I)} \to F$ sao cho $h =\overline{h} \circ \iota$, như trong sau đây biểu đồ.
$$I /K^{(I)}$$
$$\overline{C}\overline{C}^{\iota}$$
$$\overline{C} C$$
$$CC$$
$$CC$$
$$hC^{h}!$$
$$F$$

> **Định nghĩa 33.6.** không gian vectơ (vector space) $(K^{(I)}, \iota$) được xây dựng như ở trên từ tập hợp $I$ được gọi là tự do không gian vectơ (vector space) được sinh bởi I (hoặc trên I). tính giao hoán của ở trên biểu đồ được gọi là phổ dụng ánh xạ tính chất của tự do không gian vectơ (vector space) $(K^{(I)}, \iota$) trên I. Bằng cách sử dụng chứng minh kỹ thuật của Mệnh đề 33.5, nó là không khó để chứng minh rằng bất kỳ hai các không gian vectơ thỏa mãn ở trên phổ dụng ánh xạ tính chất là đẳng cấu. Ta có thể bây giờ trả về đến cách xây dựng của các tích tenxơ. Để đơn giản xét hai các không gian vectơ $E_{1}$ và $E_{2}$. Whatever $E_{1} \otimes E_{2}$ và $\phi$: $E_{1} \times  E_{2} \to E_{1} \otimes E_{2}$ là, vì $\phi$ được giả sử là song tuyến tính, ta phải có
$$\phi (u_{1} + u_{2}, v_{1}) = \phi (u_{1}, v_{1}) + \phi (u_{2}, v_{1})$$
$$\phi (u_{1}, v_{1} + v_{2}) = \phi (u_{1}, v_{1}) + \phi (u_{1}, v_{2})$$
$$\phi (\lambda u_{1}, v_{1}) = \lambda \phi (u_{1}, v_{1})$$
$$\phi (u_{1}, \mu v_{1}) = \mu \phi (u_{1}, v_{1})$$
Với mọi $u_{1}, u_{2} \in E_{1}$, tất cả $v_{1}, v_{2} \in E_{2}$, và tất cả $\lambda , \mu  \in K$. Vì $E_{1} \otimes E_{2}$ phải thỏa mãn phổ dụng ánh xạ tính chất của Định nghĩa 33.5, ta có thể muốn để định nghĩa $E_{1} \otimes E_{2}$ như tự do không gian vectơ (vector space) $K^{(E1\times E2)}$ được sinh bởi $I = E_{1} \times E_{2}$ và cho $\phi$ là đơn ánh của $E_{1} \times E_{2}$ vào $K^{(E1\times E2)}$. bài toán là rằng trong $K^{(E1\times E2)}$, các vectơ sao cho
$$(u_{1} + u_{2}, v_{1})and(u_{1}, v_{1}) + (u_{2}, v_{2})$$
Là khác nhau, khi chúng nên một cách thực là cùng, vì $\phi$ là song tuyến tính. Vì $K^{(E1\times E2)}$ là tự do, có không có các quan hệ trong số các phần tử sinh và vectơ này không gian là cũng big cho của ta mục đích. remedy là đơn giản: lấy thương của tự do không gian vectơ (vector space) $K^{(E1\times E2)}$ bởi không gian con $N$ được sinh bởi các vectơ của tạo thành
$$(u_{1} + u_{2}, v_{1}) -(u_{1}, v_{1}) -(u_{2}, v_{1})$$
$$(u_{1}, v_{1} + v_{2}) -(u_{1}, v_{1}) -(u_{1}, v_{2})$$
$$(\lambda u_{1}, v_{1}) -\lambda (u_{1}, v_{1})$$
$$(u_{1}, \mu v_{1}) -\mu (u_{1}, v_{1}).$$
Thì, nếu ta cho $E_{1} \otimes E_{2}$ là không gian thương (quotient space) $K^{(E1\times E2)}/N$ và cho $\phi$ là thương ánh xạ, điều này buộc $\phi$ là song tuyến tính. Kiểm tra rằng $(K^{(E1\times E2)}/N, \phi$) thỏa mãn phổ dụng ánh xạ tính chất là trực tiếp/dễ dàng. Ở đây là chi tiết cách xây dựng.

<!-- PAGE 1180 -->

> **Định lý 33.6.** Cho trước $n \ge 2$ các không gian vectơ $E_{1}, \dots  , E_{n}$, tích tenxơ (tensor product) $(E_{1} \otimes \cdots  \otimes E_{n}, \phi$) cho $E_{1}, \dots  , E_{n}$ có thể được được xây dựng. Hơn nữa, ký hiệu $\phi (u_{1}, \dots  , u_{n})$ như $u_{1} \otimes \cdots  \otimes u_{n}$, tích tenxơ (tensor product) $E_{1} \otimes \cdots  \otimes E_{n}$ được sinh bởi các vectơ $u_{1} \otimes \cdots  \otimes u_{n}$, ở đâu $u_{1} \in E_{1}, \dots  , u_{n} \in E_{n}$, và với mọi ánh xạ đa tuyến tính (multilinear map) $f$: $E_{1} \times  \cdots  \times  E_{n} \to F$, duy nhất ánh xạ tuyến tính (linear map) $f_{\otimes}: E_{1} \otimes \cdots  \otimes E_{n} \to F$ sao cho $f = f_{\otimes} \circ \phi$ được định nghĩa bởi
$$f_{\otimes}(u_{1} \otimes \cdots  \otimes u_{n}) = f(u_{1}, \dots  , u_{n})$$
Trên các phần tử sinh $u_{1} \otimes \cdots  \otimes u_{n}$ của $E_{1} \otimes \cdots  \otimes E_{n}$.

*Chứng minh.* Thứ nhất ta áp dụng cách xây dựng của tự do không gian vectơ (vector space) đến cartesian tích $I = E_{1}\times \cdots \times E_{n}$, thu được tự do không gian vectơ (vector space) $M = K^{(I)}$ trên $I = E_{1}\times \cdots \times E_{n}$. Vì mọi cơ sở (basis) phần tử sinh $e_{i} \in M$ là một cách duy nhất liên kết với một số bộ $n$ $i = (u_{1}, \dots  , u_{n}) \in E_{1} \times  \cdots  \times  E_{n}$, ta ký hiệu $e_{i}$ bởi $(u_{1}, \dots  , u_{n})$. Tiếp theo cho $N$ là không gian con của $M$ được sinh bởi các vectơ của sau đây loại/kiểu:
$$(u_{1}, \dots  , u_{i} + v_{i}, \dots  , u_{n}) -(u_{1}, \dots  , u_{i}, \dots  , u_{n}) -(u_{1}, \dots  , v_{i}, \dots  , u_{n}),$$
$$(u_{1}, \dots  , \lambda u_{i}, \dots  , u_{n}) -\lambda (u_{1}, \dots  , u_{i}, \dots  , u_{n}).$$
Ta cho $E_{1} \otimes \cdots  \otimes E_{n}$ là thương $M/N$ của tự do không gian vectơ (vector space) $M$ bởi $N, \pi$: $M \to M/N$ là thương ánh xạ, và tập hợp
$$\phi  = \pi  \circ \iota .$$
Bởi cách xây dựng, $\phi$ là đa tuyến tính, và vì $\pi$ là toàn ánh (surjective) và $\iota (i) = e_{i}$ sinh $M$, sự kiện rằng mỗi $i$ là của tạo thành $i = (u_{1}, \dots  , u_{n}) \in E_{1} \times  \cdots  \times  E_{n}$ suy ra rằng $\phi (u_{1}, \dots  , u_{n})$ sinh $M/N$. Do đó, nếu ta ký hiệu $\phi (u_{1}, \dots  , u_{n})$ như $u_{1} \otimes \cdots  \otimes u_{n}$, không gian $E_{1} \otimes \cdots  \otimes E_{n}$ được sinh bởi các vectơ $u_{1} \otimes \cdots  \otimes u_{n}$, với $u_{i} \in E_{i}$. Nó vẫn còn để chỉ ra rằng $(E_{1} \otimes \cdots  \otimes E_{n}, \phi$) thỏa mãn phổ dụng ánh xạ tính chất. Đến điều này kết thúc/cuối, ta bắt đầu bởi chứng minh có một ánh xạ $h$ sao cho $f = h \circ \phi$. Vì $M = K^{(E1\times \cdot \cdot \cdot \times En)}$ là tự do trên $I = E_{1} \times  \cdots  \times  E_{n}$, tồn tại duy nhất một ánh xạ tuyến tính (linear map) $\overline{f}\overline{:} K^{(E1\times \cdot \cdot \cdot \times En)} \to F$, sao cho
$$f =\overline{f} \circ \iota ,$$
Như trong biểu đồ ở dưới.
$$\iota  /$$
$$E_{1} \times  \cdots  \times  E_{n}K^{(E1\times \cdot \cdot \cdot \times En)}= M$$
$$SSS$$
$$SSS$$
$$SSS$$
$$SSS\overline{f}$$
$$SSS$$
$$fSSS$$
$$)$$
$$F$$
Bởi vì $f$ là đa tuyến tính, lưu ý rằng ta phải có $\overline{f}(w) = 0$ với mọi $w \in N$; ví dụ, trên phần tử sinh
$$(u_{1}, \dots  , u_{i} + v_{i}, \dots  , u_{n}) -(u_{1}, \dots  , u_{i}, \dots  , u_{n}) -(u_{1}, \dots  , v_{i}, \dots  , u_{n})$$

<!-- PAGE 1181 -->
Ta có
$$\overline{f}((u_{1}, \dots  , u_{i} + v_{i}, \dots  , u_{n}) -(u_{1}, \dots  , u_{i}, \dots  , u_{n}) -(u_{1}, \dots  , v_{i}, \dots  , u_{n}))$$
$$= f(u_{1}, \dots  , u_{i} + v_{i}, \dots  , u_{n}) -f(u_{1}, \dots  , u_{i}, \dots  , u_{n}) -f(u_{1}, \dots  , v_{i}, \dots  , u_{n})$$
$$= f(u_{1}, \dots  , u_{i}, \dots  , u_{n}) + f(u_{1}, \dots  , v_{i}, \dots  , u_{n}) -f(u_{1}, \dots  , u_{i}, \dots  , u_{n})$$
$$-f(u_{1}, \dots  , v_{i}, \dots  , u_{n})$$
$$= 0.$$
$$But then, \overline{f}\overline{:} M \to F \frac{factors}{f} through M/N, which means that there is a unique linear map$$
$h: M/N \to F$ sao cho $= h \circ \pi$ tạo ra sau đây biểu đồ giao hoán
$$M /M/N$$
$$\overline{E}^{\pi}\overline{E}$$
$$\overline{E} E$$
$$EE$$
$$EE$$
$$\overline{f} E^{h}"$$
$$F,$$
$$by defining h([z]) = \overline{f}(z) for \frac{every}{f} z \in M, where [z] denotes the equivalence class in M/N$$
Của $z \in M$. Thật vậy, sự kiện rằng triệt tiêu trên $N$ insures rằng $h$ được xác định tốt (well-defined) trên $M/N$, và nó là rõ ràng tuyến tính theo Định nghĩa. Vì $f =\overline{f} \circ \iota$, từ phương trình $\overline{f} = h \circ \pi$, bởi composing trên phải với $\iota$, ta thu được
$$f =\overline{f} \circ \iota  = h \circ \pi  \circ \iota  = h \circ \phi ,$$
Như trong sau đây giao hoán biểu đồ.
$$K$$
$$m^{\times \cdot \cdot \cdot \times En)}6RR$$
$$mm^{(E1}RR$$
$$mmRR$$
$$mmR^{\pi}R$$
$$m^{\iota}mRR$$
$$mRR$$
$$mmRR$$
$$mm($$
$$E_{1} \times  \cdots  \times  E_{n}\overline{f} K^{(E1\times \cdot \cdot \cdot \times En)}/N$$
$$RRllllllllllllll$$
$$RR$$
$$RR$$
$$RR$$
$$RR$$
$$RR$$
$$fRRh$$
$$R(ul$$
$$F$$
Ta bây giờ chứng minh tính duy nhất của $h$. Với mọi ánh xạ tuyến tính (linear map) $f_{\otimes}: E_{1} \otimes \cdots  \otimes E_{n} \to F$ sao cho $f = f_{\otimes} \circ \phi$, vì các vectơ $u_{1} \otimes \cdots  \otimes u_{n}$ sinh $E_{1} \otimes \cdots  \otimes E_{n}$ và vì $\phi (u_{1}, \dots  , u_{n}) = u_{1} \otimes \cdots  \otimes u_{n}$, ánh xạ $f_{\otimes}$ là một cách duy nhất được định nghĩa bởi
$$f_{\otimes}(u_{1} \otimes \cdots  \otimes u_{n}) = f(u_{1}, \dots  , u_{n}).$$
Vì $f = h \circ \phi$, ánh xạ $h$ là duy nhất, và ta cho $f_{\otimes} = h$. ánh xạ $\phi$ từ $E_{1} \times  \cdots  \times  E_{n}$ đến $E_{1} \otimes \cdots  \otimes E_{n}$ là thường được ký hiệu bởi $\iota_{\otimes}$, sao cho
$$\iota_{\otimes} (u_{1}, \dots  , u_{n}) = u_{1} \otimes \cdots  \otimes u_{n}.$$

<!-- PAGE 1182 -->
Những gì là quan trọng về Định lý 33.6 là không do đó nhiều cách xây dựng chính nó nhưng sự kiện rằng nó produces tích tenxơ (tensor product) với phổ dụng ánh xạ tính chất đối với đa tuyến tính các ánh xạ. Thật vậy, Định lý 33.6 cho ta chính tắc đẳng cấu
$$\otimes \cdots  \otimes  \sim$$
$$L(E_{1}E_{n}, F)= L(E_{1}, \dots  , E_{n}; F)$$
Giữa không gian vectơ (vector space) của các ánh xạ tuyến tính (linear maps) $L(E_{1} \otimes \cdots  \otimes E_{n}, F)$, và không gian vectơ (vector space) của đa tuyến tính các ánh xạ $\mathcal{L}(E_{1}, \dots  , E_{n}; F)$, thông qua ánh xạ tuyến tính (linear map) $-\circ \phi$ được định nghĩa bởi
$$h \mapsto h \circ \phi ,$$
Ở đâu $h \in L(E_{1} \otimes \cdots  \otimes E_{n}, F)$. Thật vậy, $h \circ \phi$ là rõ ràng đa tuyến tính, và vì theo Định lý 33.6, với mọi ánh xạ đa tuyến tính (multilinear map) $f \in L(E_{1}, \dots  , E_{n}; F)$, tồn tại duy nhất một ánh xạ tuyến tính (linear map) $f_{\otimes} \in L(E_{1} \otimes \cdots  \otimes E_{n}, F)$ sao cho $f = f_{\otimes} \circ \phi$, ánh xạ $-\circ \phi$ là song ánh (bijective). Như matter của sự kiện, nghịch đảo của nó là ánh xạ
$$f \mapsto f_{\otimes}.$$
Ta record sự kiện này như sau đây mệnh đề.

> **Mệnh đề 33.7.** Cho trước tích tenxơ (tensor product) $(E_{1} \otimes \cdots  \otimes E_{n}, \phi$), ánh xạ tuyến tính (linear map) $h \mapsto h \circ \phi$ là chính tắc đẳng cấu
$$\otimes \cdots  \otimes  \sim$$
$$L(E_{1}E_{n}, F)= L(E_{1}, \dots  , E_{n}; F)$$
Giữa không gian vectơ (vector space) của các ánh xạ tuyến tính (linear maps) $L(E_{1}\otimes \cdots \otimes E_{n}, F)$, và không gian vectơ (vector space) của đa tuyến tính các ánh xạ $\mathcal{L}(E_{1}, \dots  , E_{n}; F)$. Bằng cách sử dụng “Hom” ký hiệu, ở trên chính tắc đẳng cấu được viết
$$\otimes \cdots  \otimes  \sim$$
$$Hom(E_{1}E_{n}, F)= Hom(E_{1}, \dots  , E_{n}; F).$$
Các nhận xét:
$(1)$ là rất precise, vì tích tenxơ (tensor product) phụ thuộc vào trường $K$, ta nên chỉ số dưới ký hiệu $\otimes$ với $K$ và viết
$$E_{1} \otimes_{K}  \cdots  \otimes_{K}  E_{n}.$$
Tuy nhiên, ta thường bỏ qua chỉ số dưới $K$ trừ khi confusion có thể phát sinh.
$(2)$ Cho $F = K$, base trường, Mệnh đề 33.7 cho ta chính tắc đẳng cấu giữa không gian vectơ (vector space) $L(E_{1} \otimes \cdots  \otimes E_{n}, K)$, và không gian vectơ (vector space) của đa tuyến tính các dạng $\mathcal{L}(E_{1}, \dots  , E_{n}; K)$. Tuy nhiên, $L(E_{1} \otimes \cdots \otimes E_{n}, K)$ là không gian đối ngẫu (dual space) $(E_{1} \otimes \cdots \otimes E_{n})^{*}$, và do đó không gian vectơ (vector space) của đa tuyến tính các dạng $\mathcal{L}(E_{1}, \dots  , E_{n}; K)$ là một cách chính tắc đẳng cấu đến $(E_{1} \otimes \cdots  \otimes E_{n})^{*}$. Vì đẳng cấu này được sử dụng thường, ta record nó như sau đây mệnh đề.

<!-- PAGE 1183 -->

> **Mệnh đề 33.8.** Cho trước tích tenxơ (tensor product) $E_{1} \otimes \cdots \otimes E_{n}$,, có một chính tắc đẳng cấu
$$\sim  \otimes \cdots  \otimes$$
$$L(E_{1}, \dots  , E_{n}; K)= (E_{1}E_{n})^{*}$$
Giữa không gian vectơ (vector space) của đa tuyến tính các ánh xạ $\mathcal{L}(E_{1}, \dots  , E_{n}; K)$ và đối ngẫu (dual) $(E_{1} \otimes \cdots  \otimes E_{n})^{*}$ của tích tenxơ (tensor product) $E_{1} \otimes \cdots  \otimes E_{n}$. sự kiện rằng ánh xạ $\phi$: $E_{1} \times  \cdots  \times  E_{n} \to E_{1} \otimes \cdots  \otimes E_{n}$ là đa tuyến tính, có thể cũng được biểu diễn như sau: $u_{1} \otimes \cdots  \otimes (v_{i} + w_{i}) \otimes \cdots  \otimes u_{n} = (u_{1} \otimes \cdots  \otimes v_{i} \otimes \cdots  \otimes u_{n}) + (u_{1} \otimes \cdots  \otimes w_{i} \otimes \cdots  \otimes u_{n}), u_{1} \otimes \cdots  \otimes (\lambda u_{i}) \otimes \cdots  \otimes u_{n} = \lambda (u_{1} \otimes \cdots  \otimes u_{i} \otimes \cdots  \otimes u_{n})$. Của course, điều này là chỉ những gì ta được muốn!

> **Định nghĩa 33.7.** Các tenxơ trong $E_{1} \otimes \cdots  \otimes E_{n}$ được gọi là n-tensors, và các tenxơ của tạo thành $u_{1} \otimes \cdots  \otimes u_{n}$, ở đâu $u_{i} \in E_{i}$ được gọi là đơn giản (hoặc phân rã được) n-tensors. Những phần tử đó n-tensors rằng là không đơn giản là thường được gọi là compound n-tensors. Không chỉ thực hiện các tích tenxơ act trên các không gian, nhưng chúng cũng act trên các ánh xạ tuyến tính (linear maps) (chúng là functors).

> **Mệnh đề 33.9.** Cho trước hai các ánh xạ tuyến tính (linear maps) $f$: $E \to$ E' và $g: F \to$ F', tồn tại duy nhất một ánh xạ tuyến tính (linear map)
$$f \otimes g: E \otimes F \to E'\otimes F'$$
Sao cho
$$(f \otimes g)(u \otimes v) = f(u) \otimes g(v),$$
Với mọi $u \in E$ và tất cả $v \in F$.

*Chứng minh.* Ta có thể định nghĩa $h: E \times  F \to$ E' $\otimes$ F' bởi
$$h(u, v) = f(u) \otimes g(v).$$
Ta kiểm chứng được ngay rằng $h$ là song tuyến tính, và do đó nó cảm sinh duy nhất ánh xạ tuyến tính (linear map)
$$f \otimes g: E \otimes F \to E'\otimes F'$$
Tạo ra sau đây biểu đồ giao hoán
$$\iota \otimes  /$$
$$E \times  FE \otimes F$$
$$L\overline{L}$$
$$\overline{L} L$$
$$LL$$
$$LLf\otimes g$$
$$hLL$$
$$&$$
$$E'\otimes F',$$
Sao cho $(f \otimes$ g)(u $\otimes v) =$ f(u) $\otimes$ g(v), với mọi $u \in E$ và tất cả $v \in F$.

<!-- PAGE 1184 -->

> **Định nghĩa 33.8.** ánh xạ tuyến tính (linear map) $f \otimes g: E \otimes F \to$ E' $\otimes$ F' cho trước theo Mệnh đề 33.9 được gọi là tích tenxơ (tensor product) của $f$: $E \to$ E' và $g: F \to$ F'. Một cái khác cách để định nghĩa $f \otimes g$ tiến hành như sau. Cho trước hai các ánh xạ tuyến tính (linear maps) $f$: $E \to$ E' và $g: F \to$ F', ánh xạ $f \times  g$ là ánh xạ tuyến tính (linear map) từ $E \times  F$ đến E' $\times$ F' cho trước bởi
$$(f \times  g)(u, v) = (f(u), g(v)),for all u \in E and all v \in F.$$
Thì ánh xạ $h$ trong chứng minh của Mệnh đề 33.9 được cho bởi $h = \iota_{\otimes}' \circ (f \times  g)$, và $f \otimes g$ là duy nhất ánh xạ tuyến tính (linear map) tạo ra sau đây biểu đồ giao hoán.
$$\iota \otimes  /$$
$$E \times  FE \otimes F$$
$$f\times gf\otimes g$$
$$/$$
$$E'\times  F_{\iota'}'E'\otimes F'$$
$$\otimes$$
Nhận xét: ký hiệu $f \otimes g$ là potentially ambiguous, bởi vì Hom(E, $F)$ và Hom(E', F') là các không gian vectơ, do đó ta có thể tạo thành tích tenxơ (tensor product) Hom(E, $F)\otimes$ Hom(E', F') mà chứa các phần tử cũng được ký hiệu $f \otimes g$. để tránh confusion, thứ nhất loại của tích tenxơ (tensor product) của các ánh xạ tuyến tính (linear maps) được định nghĩa trong Mệnh đề 33.9 (mà cho ta ánh xạ tuyến tính (linear map) trong Hom(E $\otimes F$, E' $\otimes$ F')) có thể được được ký hiệu bởi T(f, $g)$. Nếu ta ký hiệu tích tenxơ (tensor product) $E \otimes F$ bởi T(E, $F)$, điều này ký hiệu làm cho nó clearer rằng $T$ là bifunctor. Nếu $E$, E' và $F$, F' là hữu hạn dimensional, bởi chọn các cơ sở nó là không khó để chỉ ra rằng ánh xạ được cảm sinh bởi $f \otimes g \mapsto$ T(f, $g)$ là đẳng cấu
$$\sim$$
$$Hom(E, F) \otimes Hom(E', F')= Hom(E \otimes F, E'\otimes F').$$

> **Mệnh đề 33.10.** Giả sử ta có các ánh xạ tuyến tính (linear maps) $f$: $E \to$ E', $g: F \to$ F', f': E' $\to$ E'' và g': F' $\to$ F''. Thì sau đây đồng nhất thức nghiệm đúng:
$$(f'\circ f) \otimes (g'\circ g) = (f'\otimes g') \circ (f \otimes g).(*)$$

*Chứng minh.* Ta có giao hoán biểu đồ
$$\iota \otimes  /$$
$$E \times  FE \otimes F$$
$$f\times gf\otimes g$$
$$\iota '$$
$$E'\times  F' \otimes  E'/\otimes F'$$
$$f'\times g'f'\otimes g'$$
$$/$$
$$E''\times  F''E''\otimes F'',$$
$$\overline{\iota}\overline{''}$$
$$\otimes$$
Và do đó giao hoán biểu đồ.
$$\iota \otimes  /$$
$$E \times  FE \otimes F$$
$$(f'\times g')\circ (f\times g)(f'\otimes g')\circ (f\otimes g)$$
$$/$$
$$E''\times  F_{\iota''}''E''\otimes F''$$
$$\otimes$$

<!-- PAGE 1185 -->
Ta cũng có giao hoán biểu đồ.
$$\iota \otimes  /$$
$$E \times  FE \otimes F$$
$$(f'\circ f)\times (g'\circ g)(f'\circ f)\otimes (g'\circ g)$$
$$/$$
$$E''\times  F''E''\otimes F''.$$
$$\overline{\iota}\overline{''}$$
$$\otimes$$
Vì ta ngay lập tức kiểm chứng rằng
$$(f'\circ f) \times  (g'\circ g) = (f'\times  g') \circ (f \times  g),$$
Bởi tính duy nhất của ánh xạ giữa $E \otimes F$ và E'' $\otimes$ F'' trong ở trên biểu đồ, ta kết luận rằng
$$(f'\circ f) \otimes (g'\circ g) = (f'\otimes g') \circ (f \otimes g),$$
Như đã khẳng định. ở trên công thức (*) cho ta sau đây hữu ích sự kiện.

> **Mệnh đề 33.11.** Nếu $f$: $E \to$ E' và $g: F \to$ F' là các đẳng cấu, thì $f \otimes g: E \otimes F \to$ E' $\otimes$ F' là cũng đẳng cấu.

*Chứng minh.* Nếu $f^{-1}$: E' $\to E$ là nghịch đảo của $f$: $E \to$ E' và $g^{-1}$: F' $\to F$ là nghịch đảo của $g: F \to$ F', thì $f^{-1} \otimes g^{-1}$: E' $\otimes$ F' $\to E \otimes F$ là nghịch đảo của $f \otimes g: E \otimes F \to$ E' $\otimes$ F', mà được hiển thị như sau:
$$(f \otimes g) \circ (f^{-1}\otimes g^{-1}) = (f \circ f^{-1}) \otimes (g \circ g^{-1})$$
$$= id_{E'} \otimes id_{F'}$$
$$= id_{E'\otimes F'},$$
Và
$$(f^{-1}\otimes g^{-1}) \circ (f \otimes g) = (f^{-1}\circ f) \otimes (g^{-1}\circ g)$$
$$= id_{E} \otimes id_{F}$$
$$= id_{E\otimes F}.$$
Vì vậy, $f \otimes g: E \otimes F \to$ E' $\otimes$ F' là đẳng cấu. tổng quát hóa đến tích tenxơ (tensor product) $f_{1} \otimes \cdots  \otimes f_{n}$ của $n \ge 3$ các ánh xạ tuyến tính (linear maps) $f_{i}$: $E_{i} \to F_{i}$ là immediate, và trái đến độc giả.
