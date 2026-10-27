# Đối xứng Các đại số


<!-- PAGE 1225 -->
Rõ ràng, $\eta_{\odot} (S^{n}(E))$ là tập hợp của symmetrized các tenxơ trong $E^{\otimes n}$. Nếu ta xét ánh xạ $S = \eta_{\odot} \circ \pi$: $E^{\otimes n} \longrightarrow E^{\otimes n}$ ở đâu $\pi$ là toàn ánh $\pi$: $E^{\otimes n} \to S^{n}(E)$, nó là dễ để kiểm tra rằng $S \circ S = S$. Vì vậy, $S$ là phép chiếu, và bởi tuyến tính đại số, ta biết rằng
$$E^{\otimes n}= S(E^{\otimes n}) \oplus \mathrm{Ker} S = \eta_{\odot} (S^{n}(E)) \oplus \mathrm{Ker} S.$$
Hóa ra là Ker $S = E^{\otimes n}\cap \mathfrak{I} =$ Ker $\pi , where\mathfrak{I}$ là hai phía lý tưởng (ideal) của T(E) được sinh bởi tất cả các tenxơ của tạo thành $u \otimes v$ - $v \otimes u \in E^{\otimes2}$ (ví dụ, xem Knapp $[107]$, Phụ lục $A)$. Vì vậy, $\eta_{\odot}$ là đơn ánh (injective),
$$E^{\otimes n}= \eta_{\odot} (S^{n}(E)) \oplus (E^{\otimes n}\cap \mathfrak{I}) = \eta_{\odot} (S^{n}(E)) \oplus \mathrm{Ker} \pi ,$$
Và tenxơ đối xứng (symmetric tensor) lũy thừa $S^{n}(E)$ là một cách tự nhiên được nhúng vào $E^{\otimes n}$.

## 33.13 Đối xứng Các đại số

Như trong trường hợp của các tenxơ, ta có thể pack cùng nhau tất cả đối xứng các lũy thừa $S^{n}(V$) vào đại số.

> **Định nghĩa 33.25.** Cho trước không gian vectơ (vector space) $V$, không gian
$$S(V ) =MS^{m}(V ),$$
$$m\ge 0$$
Được gọi là tenxơ đối xứng (symmetric tensor) đại số của $V$. Ta có thể thích nghi những gì ta đã thực hiện trong Mục 33.6 cho tổng quát tenxơ các lũy thừa đến đối xứng các tenxơ nhưng vì ta đã có đại số T(V), ta có thể tiến hành faster. Nếu $\mathfrak{I}$ là hai phía lý tưởng (ideal) được sinh bởi tất cả các tenxơ của tạo thành $u \otimes v$ - $v \otimes u \in V^{\otimes2}$, ta tập hợp
$$S^{\bullet}(V ) = T(V )/\mathfrak{I}.$$
Nhận thấy rằng vì lý tưởng (ideal) $\mathfrak{I}$ được sinh bởi các phần tử trong $V^{\otimes2}$, mọi tenxơ trong $\mathfrak{I}$ là tổ hợp tuyến tính (linear combination) của các tenxơ của tạo thành $\omega_{1}  \otimes (u \otimes v -v \otimes u) \otimes \omega_{2}$, với $\omega_{1}  \in V^{\otimes n1}$ và $\omega_{2}  \in V^{\otimes n2}$ với một số $n_{1}, n_{2} \in \mathbb{N}$, mà suy ra rằng
$$\mathfrak{I} =M(\mathfrak{I} \cap V^{\otimes m} ).$$
$$m\ge 0$$
Thì, $S^{\bullet}(V$) automatically inherits phép toán nhân mà là giao hoán, và vì T(V) là graded, nghĩa là
$$T(V ) =MV^{\otimes m} ,$$
$$m\ge 0$$
Ta có
$$S^{\bullet}(V ) =MV^{\otimes m} /(\mathfrak{I} \cap V^{\otimes m} ).$$
$$m\ge 0$$

<!-- PAGE 1226 -->
Tuy nhiên, nó là dễ để kiểm tra rằng
$$\sim  \mathfrak{I} \cap$$
$$S^{m}(V )= V^{\otimes m}/(V^{\otimes m}),$$
Do đó
$$\sim$$
$$S^{\bullet}(V )= S(V ).$$
Khi $V$ là của hữu hạn số chiều $n$, S(V) tương ứng với đại số của các đa thức với các hệ số trong $K$ trong $n$ các biến (điều này có thể được được thấy từ Mệnh đề 33.38). Khi $V$ là của vô hạn số chiều và $(u_{i})_{i\in I}$ là cơ sở (basis) của $V$, đại số S(V) tương ứng với đại số của các đa thức trong một cách vô hạn nhiều các biến trong I. Những gì’s đẹp về tenxơ đối xứng (symmetric tensor) đại số S(V) là rằng nó cung cấp nội tại định nghĩa của đa thức đại số trong bất kỳ tập hợp của I các biến. Nó là cũng dễ để xem rằng S(V) thỏa mãn sau đây phổ dụng ánh xạ tính chất.

> **Mệnh đề 33.40.** Cho trước bất kỳ giao hoán K-algebra $A$, với mọi ánh xạ tuyến tính (linear map) $f$: $V \to A$, tồn tại duy nhất một K-algebra đồng cấu $\overline{f}\overline{:}$ S(V) $\to A$ sao cho
$$f =\overline{f} \circ i,$$
Như trong biểu đồ ở dưới.
$$VS(V )$$
$$\overline{E}^{i}\overline{E}$$
$$\overline{E} E$$
$$EE$$
$$EE$$
$$fE^{f}"$$
$$A$$
Nhận xét: Nếu $E$ là hữu hạn dimensional, nhắc lại đẳng cấu $\mu$: $S^{n}(E^{*}) \longrightarrow Sym^{n}(E; K)$ được định nghĩa như tuyến tính mở rộng của ánh xạ cho trước bởi
$$\mu (v_{1}^{*} \odot \cdots  \odot v_{n}^{*})(u_{1}, \dots  , u_{n}) = \sum_{\sigma\in Sn}  v_{\sigma(1)}^{*}(u_{1}) \cdots  v_{\sigma(n)}^{*}(u_{n}).$$
Bây giờ ta có cũng phép toán nhân $S^{m}(E^{*}) \times  S^{n}(E^{*}) \longrightarrow S^{m+n}(E^{*})$. sau đây câu hỏi thì phát sinh: Có thể ta định nghĩa phép nhân $Sym^{m}(E; K) \times  Sym^{n}(E; K) \longrightarrow Sym^{m+n}(E; K)$ một cách trực tiếp trên đối xứng đa tuyến tính các dạng, sao cho sau đây biểu đồ giao hoán?
$$\odot  /$$
$$S^{m}(E^{*}) \times  S^{n}(E^{*})S^{m+n}(E^{*})$$
$$\mu m\times \mu n\mu m+n$$
$$Sym^{m}(E; K) \times  Sym^{n}(E; K)\cdot  /Sym^{m+n}(E; K)$$

<!-- PAGE 1227 -->
Câu trả lời là yes! nghiệm là để định nghĩa điều này phép nhân sao cho cho $f \in Sym^{m}(E; K)$ và $g \in Sym^{n}(E; K)$,
$$(f \cdot  g)(u_{1}, \dots  , u_{m+n}) = \sum_{shuffle(}  f(u_{\sigma(1)}, \dots  , u_{\sigma(m)})g(u_{\sigma(m+1)}, \dots  , u_{\sigma(m+n)}),(*)$$
$$\sigma \in m,n)$$
Ở đâu shuffle(m, $n)$ bao gồm của tất cả $(m$, n)-“shuffles;” rằng là, các hoán vị $\sigma$ của ${1, \dots  m + n}$ sao cho $\sigma (1) < \cdots  < \sigma (m)$ và $\sigma (m + 1) < \cdots  < \sigma (m + n)$. Nhận thấy rằng $(m$, n)-shuffle là hoàn toàn được xác định bởi dãy $\sigma (1) < \cdots  < \sigma (m)$. Ví dụ, giả sử $m = 2$ và $n = 1$. Cho trước $v_{1}^{*}, v_{2}^{*}, v_{3}^{*} \in E^{*}$, phép nhân cấu trúc trên $S(E^{*})$ suy ra rằng $(v_{1}^{*} \odot v_{2}^{*}) \cdot  v_{3}^{*} = v_{1}^{*} \odot v_{2}^{*} \odot v_{3}^{*} \in S^{3}(E^{*})$. Hơn nữa, cho $u_{1}, u_{2}, u_{3}, \in E$,
$$\mu_{3} (v_{1}^{*} \odot v_{2}^{*} \odot v_{3}^{*})(u_{1}, u_{2}, u_{3}) = \sum_{\sigma\in S3}  v_{\sigma(1)}^{*}(u_{1})v_{\sigma(2)}^{*}(u_{2})v_{\sigma(3)}^{*}(u_{3})$$
$$= v_{1}^{*}(u_{1})v_{2}^{*}(u_{2})v_{3}^{*}(u_{3}) + v_{1}^{*}(u_{1})v_{3}^{*}(u_{2})v_{2}^{*}(u_{3})$$
$$+ v_{2}^{*}(u_{1})v_{1}^{*}(u_{2})v_{3}^{*}(u_{3}) + v_{2}^{*}(u_{1})v_{3}^{*}(u_{2})v_{1}^{*}(u_{3})$$
$$+ v_{3}^{*}(u_{1})v_{1}^{*}(u_{2})v_{2}^{*}(u_{3}) + v_{3}^{*}(u_{1})v_{2}^{*}(u_{2})v_{1}^{*}(u_{3}).$$
Bây giờ $(2$, 1)- shuffles của ${1, 2, 3}$ là sau đây ba các hoán vị, cụ thể là
$$\begin{pmatrix} 1 & 2 & 3 \\ 1 & 2 & 3 \end{pmatrix} , \begin{pmatrix} 1 & 2 & 3 \\ 1 & 3 & 2 \end{pmatrix} , \begin{pmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \end{pmatrix} .$$
$\sim  \odot  \sim$ * Nếu $f = \mu_{2} (v_{1}^{*} v_{2}^{*})$ và $g = \mu (v^{*})$, thì () suy ra rằng
$$(f \cdot  g)(u_{1}, u_{2}, u_{3}) = \sum_{shuffle(2}^{13}  f(u_{\sigma(1)}, u_{\sigma(2)})g(u_{\sigma(3)})$$
$$\sigma \in ,1)$$
$$= f(u_{1}, u_{2})g(u_{3}) + f(u_{1}, u_{3})g(u_{2}) + f(u_{2}, u_{3})g(u_{1})$$
$$= \mu_{2} (v_{1}^{*} \odot v_{2}^{*})(u_{1}, u_{2})\mu_{1} (v_{3}^{*})(u_{3}) + \mu_{2} (v_{1}^{*} \odot v_{2}^{*})(u_{1}, u_{3})\mu_{1} (v_{3}^{*})(u_{2})$$
$$+ \mu_{2} (v_{1}^{*} \odot v_{2}^{*})(u_{2}, u_{3})\mu_{1} (v_{3}^{*})(u_{1})$$
$$= (v_{1}^{*}(u_{1})v_{2}^{*}(u_{2}) + v_{2}^{*}(u_{1})v_{1}^{*}(u_{2}))v_{3}^{*}(u_{3})$$
$$+ (v_{1}^{*}(u_{1})v_{2}^{*}(u_{3}) + v_{2}^{*}(u_{1})v_{1}^{*}(u_{3}))v_{3}^{*}(u_{2})$$
$$+ (v_{1}^{*}(u_{2})v_{2}^{*}(u_{3}) + v_{2}^{*}(u_{2})v_{1}^{*}(u_{3}))v_{3}^{*}(u_{1})$$
$$= \mu_{3} (v_{1}^{*} \odot v_{2}^{*} \odot v_{3}^{*})(u_{1}, u_{2}, u_{3}).$$
Ta để lại nó như một bài tập cho độc giả để kiểm chứng Phương trình (*) cho tùy ý không âm các số nguyên $m$ và $n$. Một cái khác hữu ích chính tắc đẳng cấu (của K-algebras) là cho trước ở dưới.

> **Mệnh đề 33.41.** Với mọi hai các không gian vectơ $E$ và $F$, có một chính tắc đẳng cấu (của K-algebras)
$$\oplus  \sim  \otimes$$
$$S(EF)= S(E)S(F).$$
