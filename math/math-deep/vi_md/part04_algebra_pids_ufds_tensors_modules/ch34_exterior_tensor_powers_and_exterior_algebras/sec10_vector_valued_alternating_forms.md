# Nhận giá trị vectơ (vector-valued) Thay phiên Các dạng


<!-- PAGE 1267 -->
Ngược lại, giả sử rằng dim(U $\cap V$) $\ge 1$. Chọn cơ sở (basis) $(w_{1}, \dots  , w_{r})$ của $W = U \cap V$, và mở rộng cơ sở (cơ sở (basis)) này đến cơ sở (basis) $(w_{1}, \dots  , w_{r}, w_{r+1}, \dots  , w_{p})$ của $U$ và đến cơ sở (basis) $(w_{1}, \dots  , w_{r}, w_{p+1}, \dots , w_{p+q-r})$ của $V$. Theo Hệ quả 34.26, $(u_{1}, \dots  , u_{p})$ là cũng cơ sở (basis) của $U$, do đó
$$u_{1} \wedge \cdots  \wedge u_{p} = a w_{1} \wedge \cdots  \wedge w_{r} \wedge w_{r+1} \wedge \cdots  \wedge w_{p}$$
Với một số $a \in K$, và $(v_{1}, \dots  , v_{q})$ là cũng cơ sở (basis) của $V$, do đó
$$v_{1} \wedge \cdots  \wedge v_{q} = b w_{1} \cdots  \wedge w_{r} \wedge w_{p+1} \wedge \cdots  \wedge w_{p+q-r}$$
Với một số $b \in K$, và do đó
$$u \wedge v = u_{1} \wedge \cdots  \wedge u_{p} \wedge v_{1} \wedge \cdots  \wedge v_{q} = 0$$
Vì nó chứa một số repeated $w_{i}$, với $1 \le i \le r$. Như ứng dụng của Mệnh đề 34.31, xét hai xạ ảnh các đường thẳng $D_{1}$ và $D_{2}$ trong $\mathbb{RP}^{3}$, mà có nghĩa là $D_{1}$ và $D_{2}$ tương ứng với hai 2-các mặt phẳng trong $\mathbb{R}^{4}$, và do đó theo Mệnh đề
$$\mathbb{RP}(_{2}^{4})^{-1} \mathbb{RP}^{5}$$
34.30, đến hai các điểm trong $=$. Các phần tử này hai các điểm tương ứng với 2-các vectơ
$$z = a_{1,2}e_{1} \wedge e_{2} + a_{1,3}e_{1} \wedge e_{3} + a_{1,4}e_{1} \wedge e_{4} + a_{2,3}e_{2} \wedge e_{3} + a_{2,4}e_{2} \wedge e_{4} + a_{3,4}e_{3} \wedge e_{4}$$
Và z' $= a_{1,2}'e_{1} \wedge e_{2} + a_{1,3}'e_{1} \wedge e_{3} + a_{1,4}'e_{1} \wedge e_{4} + a_{2,3}'e_{2} \wedge e_{3} + a_{2,4}'e_{2} \wedge e_{4} + a_{3,4}'e_{3} \wedge e_{4}$ có Pl¨ucker các tọa độ, (ở đâu $a_{i,j} = \lambda_{ij}$), thỏa mãn phương trình
$$\lambda_{12} \lambda_{34}  -\lambda_{13} \lambda_{24}  + \lambda_{14} \lambda_{23}  = 0$$
Của Klein mặt bậc hai (quadric), và $D_{1}$ và $D_{2}$ giao nhau khi và chỉ khi $z \wedge$ z' $= 0$ khi và chỉ khi
$$a_{1,2}a_{3,4}' -a_{1,3}a_{3,4}' + a_{1,4}a_{2,3}' + a_{2,3}a_{1,4}' -a_{2,4}a_{1,3}' + a_{3,4}a_{1,2}' = 0.$$
Nhận thấy rằng cho $D_{1}$ cố định, điều này là tuyến tính điều kiện. sự kiện này là rất helpful cho việc giải các bài tập liên quan đến các giao của các đường thẳng. nổi tiếng bài toán là để tìm cách mà nhiều các đường thẳng $in\mathbb{RP}^{3}$ meet bốn cho trước các đường thẳng nói chung position. câu trả lời là nhiều nhất $2$.

## 34.10 Nhận giá trị vectơ (vector-valued) Thay phiên Các dạng

Mục đích của điều này mục là đến trình bày technical kiến thức nền tảng cần thiết đến understand nhận giá trị vectơ (vector-valued) vi phân các dạng, đặc biệt trong trường hợp của Lie các nhóm ở đâu vi phân các dạng lấy các giá trị của chúng trong Lie đại số phát sinh một cách tự nhiên. Trong mục này không gian vectơ (vector space) $E$ được giả sử đến có hữu hạn số chiều. Ta biết rằng
$$n \sim$$
$$there is a canonical isomorphism \bigwedge  (E^{*})= Alt^{n}(E; K) between alternating n-forms and$$

<!-- PAGE 1268 -->
Thay phiên đa tuyến tính các ánh xạ. Như trong trường hợp của tổng quát các tenxơ, các đẳng cấu miễn là/được cung cấp bởi Các mệnh đề 34.5, 33.19, và 34.10, cụ thể là
$$\sim$$
$$Alt^{n}(E; F)=Hom \begin{pmatrix} n \\ ^(E), F \\ * \end{pmatrix}$$
$$\sim \otimes$$
$$Hom \begin{pmatrix} n \\ ^(E), F \\ n \end{pmatrix} = \begin{pmatrix} n \\ ^(E) \end{pmatrix} F$$
$$*n$$
$$\sim ^$$
$$\begin{pmatrix} ^(E) \end{pmatrix} =(E^{*})$$
Cho chính tắc đẳng cấu
$$\sim \otimes$$
$$Alt^{n}(E; F)= \begin{pmatrix} n \\ ^(E^{*}) \end{pmatrix} F$$
Mà ta record như hệ quả.

> **Hệ quả 34.32.** Với mọi hữu hạn chiều vecgtor không gian $E$ và bất kỳ không gian vectơ (vector space) $F$, ta có chính tắc đẳng cấu
$$\sim \otimes$$
$$Alt^{n}(E; F)= \begin{pmatrix} n \\ ^(E^{*}) \end{pmatrix} F.$$
Lưu ý rằng $F$ có thể có vô hạn số chiều. đẳng cấu này cho phép chúng ta đến quan điểm các tenxơ
$$in \bigwedge  n(E^{*})\otimes F as vector-valued alternating forms, a point of view that is useful in differential$$
$$geometry. If (f_{1}, \dots  , f_{r}) is a basis of F, every tensor \omega  \in \bigwedge  n(E^{*}) \otimes F can be written as$$
Một số tổ hợp tuyến tính (linear combination)
$$\omega  = \sum_{i=1}^{r}  \alpha_{i}  \otimes f_{i},$$
$$with \alpha_{i}  \in \bigwedge  n(E^{*}).We also let$$
$$n!$$
$$^(E; F) =M^(E^{*})\otimes F = \begin{pmatrix} ^(E) \end{pmatrix} \otimes F.$$
$$n=0$$
Cho trước ba các không gian vectơ, $F, G, H$, nếu ta có một số ánh xạ song tuyến tính (bilinear map) $\Phi$: $F \times  G \to H$, thì ta có thể định nghĩa phép toán nhân
$$\wedge_{\Phi}  :^(E; F) \times ^(E; G) \to ^(E; H)$$
Như sau: Với mọi cặp $(m, n)$, ta định nghĩa phép nhân
$$! !$$
$$\wedge_{\Phi}  : \begin{pmatrix} m \\ ^(E^{*}) \end{pmatrix} \otimes F\times \begin{pmatrix} n \\ ^(E^{*}) \end{pmatrix} \otimes G\longrightarrow \begin{pmatrix} m+n \\ ^(E^{*}) \end{pmatrix} \otimes H$$

<!-- PAGE 1269 -->
Bởi
$$\omega  \wedge_{\Phi}  \eta  = (\alpha  \otimes f) \wedge_{\Phi}  (\beta  \otimes g) = (\alpha  \wedge \beta ) \otimes \Phi (f, g).$$
Như trong Mục 34.5 (sau đây $H$. Cartan $[35])$, ta có thể cũng định nghĩa phép nhân
$$\wedge_{\Phi}  : Alt^{m}(E; F) \times  Alt^{n}(E; G) \longrightarrow Alt^{m+n}(E; H)$$
Một cách trực tiếp trên thay phiên đa tuyến tính các ánh xạ như sau: Cho $f \in Alt^{m}(E; F)$ và $g \in Alt^{n}(E; G)$,
$$(f \wedge_{\Phi}  g)(u_{1}, \dots  , u_{m+n}) = \sum_{shuffle(}  sgn(\sigma ) \Phi \begin{pmatrix} f(u_{\sigma(1)}, \dots  , u_{\sigma(m)}), g(u_{\sigma(m+1)}, \dots  , u_{\sigma(m+n)}) \end{pmatrix} ,$$
$$\sigma \in m,n)$$
Ở đâu shuffle(m, $n)$ bao gồm của tất cả $(m$, n)-“shuffles;” rằng là, các hoán vị $\sigma$ của ${1, \dots  m + n}$ sao cho $\sigma (1) < \cdots  < \sigma (m)$ và $\sigma (m + 1) < \cdots  < \sigma (m + n)$. đặc biệt trường hợp của interest là trường hợp ở đâu $F = G = H$ là Lie đại số và $\Phi$ (, $b) = [a, b]$
$$is the Lie bracket of F. In this case, using a basis (f_{1}, \dots  , f_{r}) of F, if we write \omega  = \sum_{i}  \alpha_{i} \otimes f_{i}$$
$$and \eta  = \sum_{j}  \beta_{j}  \otimes f_{j}, we have$$
$$\omega  \wedge_{\Phi}  \eta  = [\omega , \eta ] = \sum_{i,j}  \alpha_{i}  \wedge \beta_{j}  \otimes [f_{i}, f_{j}].$$
Nó là thông lệ đến ký hiệu $\omega \wedge_{\Phi} \eta$ bởi $[\omega , \eta$ ] (không may là, bracket ký hiệu là overloaded). Hệ quả là,
$$[\eta , \omega ] = (-1)^{mn+1}[\omega , \eta ].$$
Nói chung không nhiều có thể được được nói về $\wedge_{\Phi}$, trừ khi $\Phi$ có một số additional các tính chất. Đặc biệt, $\wedge_{\Phi}$ là một cách tổng quát không kết hợp. Ta bây giờ sử dụng nhận giá trị vectơ (vector-valued) thay phiên các dạng đến tổng quát hóa cả hai $\mu$ ánh xạ của Mệnh đề 34.14 và tổng quát hóa Mệnh đề 33.19 bởi định nghĩa ánh xạ
$$n!$$
$$\mu_{F}  :^(E^{*})\otimes F \longrightarrow Alt^{n}(E; F)$$
Trên các phần tử sinh bởi
$$\mu_{F} ((v_{1}^{*} \wedge \cdots  \wedge v_{n}^{*}) \otimes f)(u_{1}, \dots  , u_{n}) = (\det(v_{j}^{*}(u_{i}))f,$$
Với $v_{1}^{*}, \dots  , v_{n}^{*} \in E^{*}, u_{1}, \dots  , u_{n} \in E$, và $f \in F$.

> **Mệnh đề 34.33.** ánh xạ
$$n!$$
$$\mu_{F}  :^(E^{*})\otimes F \longrightarrow Alt^{n}(E; F)$$
Được định nghĩa như ở trên là chính tắc đẳng cấu với mọi $n \ge 0$. Hơn nữa, cho trước bất kỳ ba
$$vector spaces, F, G, H, and any bilinear map \Phi : F \times  G \to H, for all \omega  \in (^{n} \bigwedge  (E^{*})) \otimes F and$$
$$all \eta  \in (^{n} \bigwedge  (E^{*})) \otimes G,$$
$$\mu_{H} (\omega  \wedge_{\Phi}  \eta ) = \mu_{F} (\omega ) \wedge_{\Phi}  \mu_{G} (\eta ).$$

<!-- PAGE 1270 -->
$$Proof. Since we already know that ( \bigwedge  (E^{*}))\otimes F and Alt^{n}(E; F) are isomorphic, it is enough$$
$$to show that \mu_{F}  maps some basis of (^{n} \bigwedge_{\in J}^{n}  (E^{*})) \otimes F to linearly independent elements. Pick$$
Một số các cơ sở $(e_{1}, \dots  , e_{p})$ trong $E$ và $(f_{j})_{j}$ trong $F$. Thì ta biết rằng các vectơ $e_{I}^{*} \otimes f_{j}$, ở đâu
$$I \subseteq {1, \dots  , p} and |I| = n, form a basis of (^{n} \bigwedge  (E^{*})) \otimes F. If we have a linear dependence$$
$$\sum_{I,j}  \lambda_{I,j} \mu_{F} (e_{I}^{*} \otimes f_{j}) = 0,$$
Áp dụng ở trên tổ hợp đến mỗi $(e_{i1}, \dots  , e_{in}) (I = {i_{1}, \dots  , i_{n}}, i_{1} < \cdots  < i_{n})$, ta thu được tổ hợp tuyến tính (linear combination)
$$\sum_{j}  \lambda_{I,j} f_{j} = 0,$$
Và bởi sự độc lập tuyến tính (linear independence) của $f_{j}’s$, ta thu được $\lambda_{I,j}  = 0$ với mọi I và tất cả $j$. Vì vậy, $\mu_{F} (e_{I}^{*} \otimes f_{j})$ là độc lập tuyến tính (linearly independent), và ta được thực hiện. phần thứ hai của mệnh đề là đã kiểm tra bằng cách sử dụng đơn giản phép tính. sau đây mệnh đề sẽ là hữu ích trong dealing với nhận giá trị vectơ (vector-valued) vi phân các dạng.
$$Proposition 34.34. If (e_{1}, \dots  , e_{p}) is any basis of E, then every element \omega  \in (^{n} \bigwedge  (E^{*})) \otimes F$$
Có thể được được viết trong duy nhất cách như
$$\omega  = \sum_{I}  e_{I}^{*} \otimes f_{I},f_{I} \in F,$$
Ở đâu $e_{I}^{*}$ được định nghĩa như trong Mục 34.2.
$$Proof. Since, by Proposition 34.7, the e_{I}^{*} form a basis of \bigwedge  n(E^{*}), elements of the form e_{I}^{*} \otimes f$$
$$span (^{n} \bigwedge  (E^{*})) \otimes F.Now if we apply \mu_{F} (\omega ) to (e_{i1}, \dots  , e_{in}), where I = {i_{1}, \dots  , i_{n}} \subseteq$$
${1, \dots  , p}$, ta thu được
$$\mu_{F} (\omega )(e_{i1}, \dots  , e_{in}) = \mu_{F} (e_{I}^{*} \otimes f_{I})(e_{i1}, \dots  , e_{in}) = f_{I}.$$
Vì vậy, $f_{I}$ là một cách duy nhất được xác định bởi $f$. Mệnh đề 34.34 có thể cũng là formulated theo thay phiên đa tuyến tính các ánh xạ, sự kiện rằng sẽ là hữu ích đến deal với vi phân các dạng.

> **Hệ quả 34.35.** Định nghĩa tích $\cdot$: $Alt^{n}(E;\mathbb{R}) \times  F \to Alt^{n}(E; F)$ như sau: Với mọi $\omega  \in Alt^{n}(E;\mathbb{R})$ và tất cả $f \in F$,
$$(\omega  \cdot  f)(u_{1}, \dots  , u) = \omega (u_{1}, \dots  , u_{n})f,$$
$$for all u_{1}, \dots  , u_{n} \in E. Then for every \omega  \in (^{n} \bigwedge^{n}  (E^{*})) \otimes F of the form$$
$$\omega  = u_{1}^{*} \wedge \cdots  \wedge u_{n}^{*} \otimes f,$$
Ta có
$$\mu_{F} (u_{1}^{*} \wedge \cdots  \wedge u_{n}^{*} \otimes f) = \mu_{F} (u_{1}^{*} \wedge \cdots  \wedge u_{n}^{*}) \cdot  f.$$
