# Các đại số ngoài


<!-- PAGE 1243 -->
$$n n$$
$$As the  right hand side is an alternating map, we get a unique linear map \bigwedge  \eta : \bigwedge  (E) \to$$
$E^{\otimes n}$ tạo ra sau đây biểu đồ giao hoán.
$$E^{n}\overline{H}^{\iota\wedge}\overline{H}\overline{H}/ \bigwedge  n(E)$$
$$HH$$
$$HHn \eta$$
$$\eta HH# \bigwedge_{\otimes n}$$
$$E.$$
$$n$$
$$Clearly, \bigwedge_{n}  \eta (^{n} \bigwedge  (E))  is the set of antisymmetrized tensors in E^{\otimes n}. If we consider the map$$
$$A = ( \bigwedge  \eta ) \circ \pi : E^{\otimes n}\longrightarrow E^{\otimes n}, it is easy to check that A \circ A = A. Therefore, A is a$$
Phép chiếu, và bởi tuyến tính đại số, ta biết rằng
$$nn$$
$$^^$$
$$E^{\otimes n}= A(E^{\otimes n}) \oplus \mathrm{Ker} A =\eta ((E)) \oplus \mathrm{Ker} A.$$
Hóa ra là Ker $A = E^{\otimes n} \cap \mathfrak{I}_{a} =$ Ker $\pi$, ở đâu $\mathfrak{I}_{a}$ là hai phía lý tưởng (ideal) của T(E) được sinh bởi tất cả các tenxơ của tạo thành $u \otimes u \in E^{\otimes2}$ (ví dụ, xem Knapp $[107]$, Phụ lục
$$n$$
$$A). Therefore, \bigwedge  \eta  is injective,$$
$$nnnn$$
$$^^ ^^$$
$$E^{\otimes n}=\eta ((E)) \oplus (E^{\otimes n}\cap \mathfrak{I}_{a}) =\eta ((E)) \oplus \mathrm{Ker} \pi ,$$
$$and the exterior tensor power \bigwedge  n(E) is naturally embedded into E^{\otimes n}.$$

## 34.5 Các đại số ngoài

$$As in the case of symmetric tensors, we can pack together all the exterior powers \bigwedge  n(V ) into$$
Đại số.

> **Định nghĩa 34.5.** Gieven bất kỳ không gian vectơ (vector space) $V$, không gian vectơ (vector space)
$$m$$
$$^(V ) =M^(V )$$
$$m\ge 0$$
Được gọi là đại số ngoài (exterior algebra) (hoặc Grassmann đại số) của $V$.
$$To make \bigwedge  (V ) into an algebra, we mimic the procedure used for symmetric  powers. If$$
$\mathfrak{I}_{a}$ là hai phía lý tưởng (ideal) được sinh bởi tất cả các tenxơ của tạo thành $u \otimes u \in V^{\otimes2}$, ta tập hợp
$$\bullet$$
$$^(V ) = T(V )/\mathfrak{I}_{a}.$$
$$Then \bigwedge  \bullet (V ) automatically inherits a multiplication operation, called wedge product, and$$
Vì T(V) là graded, nghĩa là
$$T(V ) =MV^{\otimes m} ,$$
$$m\ge 0$$

<!-- PAGE 1244 -->
Ta có
$$\bullet$$
$$^(V ) =MV^{\otimes m} /(\mathfrak{I}_{a} \cap V^{\otimes m} ).$$
$$m\ge 0$$
Tuy nhiên, nó là dễ để kiểm tra rằng
$$m$$
$$^ \sim  \mathfrak{I}_{a} \cap$$
$$(V )= V^{\otimes m}/(V^{\otimes m}),$$
Do đó
$$\bullet$$
$$^ \sim ^$$
$$(V )=(V ).$$
Khi $V$ có hữu hạn số chiều $d$, ta thực sự có hữu hạn tổng trực tiếp (direct sum) (coproduct)
$$dm$$
$$^(V ) =M^(V ),$$
$$m=0$$
$$and since each \bigwedge  m(V ) has dimension_{m}^{d} \begin{pmatrix}\end{pmatrix} , we deduce that$$
$$^$$
$$\dim((V )) = 2^{d}= 2^{\dim(V)}.$$
$$The multiplication, \wedge : \bigwedge  m(V )\times^{n} \bigwedge  (V ) \to \bigwedge  m+n(V ), is skew-symmetric in the following$$
Precise nghĩa:
$$Proposition 34.12. For all \alpha  \in \bigwedge  m(V ) and all \beta  \in \bigwedge  n(V ), we have$$
$$\beta  \wedge \alpha  = (-1)^{mn}\alpha  \wedge \beta .$$

*Chứng minh.* Vì $v \wedge u = -u \wedge v$ với mọi $u, v \in V$, Mệnh đề 34.12 suy ra bởi quy nạp. Vì $\alpha  \wedge \alpha  = 0$ với mọi đơn giản (cũng được gọi là phân rã được) tenxơ $\alpha  = u_{1} \wedge \cdots  \wedge u_{n}$, nó
$$seems natural to infer that \alpha  \wedge \alpha  = 0 for every tensor \alpha  \in \bigwedge  (V ). If we consider the case$$
Ở đâu dim(V) $\le 3$, ta có thể thật vậy chứng minh ở trên assertion. Tuy nhiên, nếu dim(V) $\ge 4$, ở trên sự kiện là một cách tổng quát sai! Ví dụ, khi dim(V) $= 4$, nếu $(u_{1}, u_{2}, u_{3}, u_{4})$ là cơ sở (basis) cho $V$, cho $\alpha  = u_{1} \wedge u_{2} + u_{3} \wedge u_{4}$, ta kiểm tra rằng
$$\alpha  \wedge \alpha  = 2u_{1} \wedge u_{2} \wedge u_{3} \wedge u_{4},$$
$$m$$
$$which is nonzero. However, if \alpha  \in \bigwedge  E with m odd, since m^{2}is also odd, we have$$
$$\alpha  \wedge \alpha  = (-1)^{m2}\alpha  \wedge \alpha  = -\alpha  \wedge \alpha ,$$
Do đó thật vậy $\alpha  \wedge \alpha  = 0$ (nếu $K$ là không trường của characteristic $2)$.

<!-- PAGE 1245 -->
Ở trên thảo luận suggests rằng nó có thể là hữu ích đến biết khi thay phiên tenxơ
$$is simple (decomposable). We will show in Section 34.7 that for tensors \alpha  \in \bigwedge  2(V ), \alpha \wedge \alpha  = 0$$
Khi và chỉ khi $\alpha$ là đơn giản. tổng quát tiêu chuẩn cho decomposability có thể được cho trước theo một số các phép toán đã biết như trái hook và phải hook (cũng được gọi là phần trong (interior) các tích); xem Mục 34.7.
$$It is easy to see that \bigwedge  (V ) satisfies the following universal mapping property.$$
$$Proposition 34.13. Given any K-algebra A, for any linear \frac{map}{f :} f : V \to A, if (f(v))^{2}= 0$$
$$for all v \in V , then there is a unique K-algebra homomorphism \bigwedge  (V ) \to A so that$$
$$f =\overline{f} \circ i,$$
Như trong biểu đồ ở dưới.
$$V\overline{F}^{i}\overline{F}\overline{F} F \bigwedge  (V )$$
$$FF$$
$$FF$$
$$fF^{f}"$$
$$A$$
$$When E is finite-dimensional, recall the isomorphism \mu : \bigwedge  n(E^{*}) \longrightarrow Alt^{n}(E; K), defined$$
Như tuyến tính mở rộng của ánh xạ cho trước bởi
$$\mu (v_{1}^{*} \wedge \cdots  \wedge v_{n}^{*})(u_{1}, \dots  , u_{n}) = \det(v_{j}^{*}(u_{i})).$$
$$Now, we have also a multiplication operation \bigwedge  m(E^{*}) \times \bigwedge  n(E^{*}) \longrightarrow \bigwedge  m+n(E^{*}). The fol-$$
Thấp câu hỏi thì phát sinh: Có thể ta định nghĩa phép nhân $Alt^{m}(E; K) \times  Alt^{n}(E; K) \longrightarrow Alt^{m+n}(E; K)$ một cách trực tiếp trên thay phiên đa tuyến tính các dạng, sao cho sau đây biểu đồ giao hoán?
$$\bigwedge  m(E^{*}) \times \bigwedge_{\mu m\times}  n(E^{*})\wedge / \bigwedge  m+n(E^{*})$$
$$\mu n\mu m+n$$
$$Alt^{m}(E; K) \times  Alt^{n}(E; K)\wedge  /Alt^{m+n}(E; K)$$
Như trong đối xứng trường hợp, câu trả lời là yes! nghiệm là để định nghĩa điều này phép nhân sao cho, cho $f \in Alt^{m}(E; K)$ và $g \in Alt^{n}(E; K)$,
$$(f \wedge g)(u_{1}, \dots  , u_{m+n}) = \sum_{shuffle(}  sgn(\sigma ) f(u_{\sigma(1)}, \dots  , u_{\sigma(m)})g(u_{\sigma(m+1)}, \dots  , u_{\sigma(m+n)}), (**)$$
$$\sigma \in m,n)$$
Ở đâu shuffle(m, $n)$ bao gồm của tất cả $(m$, n)-“shuffles;” rằng là, các hoán vị $\sigma$ của ${1, \dots  m + n}$ sao cho $\sigma (1) < \cdots  < \sigma (m)$ và $\sigma (m+1) < \cdots  < \sigma (m+n)$. Ví dụ, khi $m = n = 1$, ta có
$$(f \wedge g)(u, v) = f(u)g(v) -g(u)f(v).$$

<!-- PAGE 1246 -->
Khi $m = 1$ và $n \ge 2$, kiểm tra rằng
$$(f \wedge g)(u_{1}, \dots  , u_{m+1}) = \sum_{i=1}^{m+1}  (-1)^{i-1}f(u_{i})g(u_{1}, \dots  , u_{i}b, \dots  , u_{m+1}),$$
Ở đâu hat trên lập luận $u_{i}$ có nghĩa là nó nên được bỏ qua. Ở đây là một cái khác tường minh ví dụ. Giả sử $m = 2$ và $n = 1$. Cho trước $v_{1}^{*}, v_{2}^{*}, v  \in E^{*}$,
$$the multiplication structure on \bigwedge  (E^{*}) implies that (v_{1}^{*} \wedge v_{2}^{*}) \cdot  v_{3}^{*} = v_{1}^{*} \wedge v_{2}^{*} \wedge v_{3}^{*} \in \bigwedge^{3*}  3(E^{*}).$$
Hơn nữa, cho $u_{1}, u_{2}, u_{3}, \in E$,
$$\mu_{3} (v_{1}^{*} \wedge v_{2}^{*} \wedge v_{3}^{*})(u_{1}, u_{2}, u_{3}) = \sum_{\sigma\in S3}  sgn(\sigma )v_{\sigma(1)}^{*}(u_{1})v_{\sigma(2)}^{*}(u_{2})v_{\sigma(3)}^{*}(u_{3})$$
$$= v_{1}^{*}(u_{1})v_{2}^{*}(u_{2})v_{3}^{*}(u_{3}) -v_{1}^{*}(u_{1})v_{3}^{*}(u_{2})v_{2}^{*}(u_{3})$$
$$-v_{2}^{*}(u_{1})v_{1}^{*}(u_{2})v_{3}^{*}(u_{3}) + v_{2}^{*}(u_{1})v_{3}^{*}(u_{2})v_{1}^{*}(u_{3})$$
$$+ v_{3}^{*}(u_{1})v_{1}^{*}(u_{2})v_{2}^{*}(u_{3}) -v_{3}^{*}(u_{1})v_{2}^{*}(u_{2})v_{1}^{*}(u_{3}).$$
Bây giờ $(2$, 1)- shuffles của ${1, 2, 3}$ là sau đây ba các hoán vị, cụ thể là
$$\begin{pmatrix} 1 & 2 & 3 \\ 1 & 2 & 3 \end{pmatrix} , \begin{pmatrix} 1 & 2 & 3 \\ 1 & 3 & 2 \end{pmatrix} , \begin{pmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \end{pmatrix} .$$
$\sim  \wedge  \sim$ ** Nếu $f = \mu_{2} (v_{1}^{*} v_{2}^{*})$ và $g = \mu_{1} (v_{3}^{*})$, thì () suy ra rằng
$$(f \cdot  g)(u_{1}, u_{2}, u_{3}) = \sum_{shuffle(2}  sgn(\sigma )f(u_{\sigma(1)}, u_{\sigma(2)})g(u_{\sigma(3)})$$
$$\sigma \in ,1)$$
$$= f(u_{1}, u_{2})g(u_{3}) -f(u_{1}, u_{3})g(u_{2}) + f(u_{2}, u_{3})g(u_{1})$$
$$= \mu_{2} (v_{1}^{*} \wedge v_{2}^{*})(u_{1}, u_{2})\mu_{1} (v_{3}^{*})(u_{3}) -\mu_{2} (v_{1}^{*} \wedge v_{2}^{*})(u_{1}, u_{3})\mu_{1} (v_{3}^{*})(u_{2})$$
$$+ \mu_{2} (v_{1}^{*} \wedge v_{2}^{*})(u_{2}, u_{3})\mu_{1} (v_{3}^{*})(u_{1})$$
$$= (v_{1}^{*}(u_{1})v_{2}^{*}(u_{2}) -v_{2}^{*}(u_{1})v_{1}^{*}(u_{2}))v_{3}^{*}(u_{3})$$
$$-(v_{1}^{*}(u_{1})v_{2}^{*}(u_{3}) -v_{2}^{*}(u_{1})v_{1}^{*}(u_{3}))v_{3}^{*}(u_{2})$$
$$+ (v_{1}^{*}(u_{2})v_{2}^{*}(u_{3}) -v_{2}^{*}(u_{2})v_{1}^{*}(u_{3}))v_{3}^{*}(u_{1})$$
$$= \mu_{3} (v_{1}^{*} \wedge v_{2}^{*} \wedge v_{3}^{*})(u_{1}, u_{2}, u_{3}).$$
Kết quả là của tất cả điều này, tổng trực tiếp (direct sum)
$$Alt(E) =MAlt^{n}(E; K)$$
$$n\ge 0$$
$$is an algebra under the above multiplication, and this algebra is isomorphic to \bigwedge  (E^{*}). For$$
Record ta phát biểu
