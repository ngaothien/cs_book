# Các đại số tenxơ


<!-- PAGE 1199 -->

## 33.6 Các đại số tenxơ

Của ta mục tiêu là để định nghĩa không gian vectơ (vector space) T(V) thu được bằng cách lấy tổng trực tiếp (direct sum) của các tích tenxơ
$$V \otimes \cdots  \otimes V,$$
$$|{z}$$
$$m$$
Và để định nghĩa phép toán nhân trên T(V) mà làm cho T(V) vào đại số cấu trúc được gọi là đại số. đại số T(V) thỏa mãn phổ dụng tính chất được phát biểu trong Mệnh đề 33.21, mà làm cho nó “tự do đại số” được sinh bởi không gian vectơ (vector space) $V$.

> **Định nghĩa 33.9.** tích tenxơ (tensor product)
$$V \otimes \cdots  \otimes V$$
$$|{z}$$
$$m$$
Cũng được ký hiệu như
$$m$$
$$OVorV^{\otimes m}$$
Và được gọi là thứ $m$ tenxơ lũy thừa của $V$ (với $V^{\otimes1} = V$, và $V^{\otimes0} = K)$. Ta có thể pack tất cả tenxơ các lũy thừa của $V$ vào “big” không gian vectơ (vector space)
$$T(V ) =MV^{\otimes m} ,$$
$$m\ge 0$$
$$denoted T^{\bullet} (V ) or \bigotimes  V to avoid confusion with the tangent bundle.$$
Điều này là thú vị object bởi vì ta có thể định nghĩa phép toán nhân trên nó mà làm cho nó vào đại số. Khi $V$ là của hữu hạn số chiều $n$, ta có thể chọn một số cơ sở (basis) $(e_{1} \dots  , e_{n})$ của $V$, và thì mọi tenxơ $\omega  \in$ T(V) có thể được biểu diễn dưới dạng tổ hợp tuyến tính (linear combination) của các số hạng của tạo thành $e_{i1} \otimes \cdots \otimes e_{ik}$, ở đâu $(i_{1}, \dots  , i_{k})$ là bất kỳ dãy của các phần tử từ tập hợp ${1, \dots  , n}$. Ta có thể nghĩ của các tenxơ $e_{i1} \otimes \cdots \otimes e_{ik}$ như các đơn thức trong noncommuting các biến $e_{1}, \dots  , e_{n}$. Do đó không gian T(V) tương ứng với đại số của các đa thức với các hệ số trong $K$ trong $n$ noncommuting các biến. Cho chúng ta ôn tập/tổng quan định nghĩa của đại số trên trường. Cho $K$ ký hiệu bất kỳ (giao hoán) trường, mặc dù cho của ta các mục đích, ta có thể giả sử rằng $K = \mathbb{R}$ (và occasionally, $K = \mathbb{C})$. Vì ta sẽ chỉ là dealing với kết hợp các đại số với multiplicative unit, ta chỉ định nghĩa các đại số của điều này loại.

> **Định nghĩa 33.10.** Cho trước trường $K$, K-algebra là vectơ $K$ không gian $A$ cùng với song tuyến tính phép toán $\cdot$: $A\times A \to A$, được gọi là phép nhân, mà làm cho $A$ vào vành với unity $1$ (hoặc $1_{A}$, khi ta muốn là rất precise). Điều này có nghĩa là $\cdot$ là kết hợp và rằng có một multiplicative phần tử đơn vị (identity element) $1$ sao cho $1 \cdot  a = a \cdot  1 = a$, với mọi $a \in A$. Cho trước hai

<!-- PAGE 1200 -->
K-algebras $A$ và $B$, K-algebra đồng cấu $h: A \to B$ là ánh xạ tuyến tính (linear map) rằng là cũng vành đồng cấu, với $h(1_{A}) = 1_{B}$; nghĩa là,
$$h(a_{1} \cdot  a_{2}) = h(a_{1}) \cdot  h(a_{2})for all a_{1}, a_{2} \in A$$
$$h(1_{A}) = 1_{B}.$$
Tập hợp của K-algebra các đồng cấu giữa $A$ và $B$ được ký hiệu là $Hom_{alg}(A, B)$. Ví dụ, vành $M_{n}(K)$ của tất cả $n \times  n$ các ma trận trên trường $K$ là K-algebra. Có một hiển nhiên khái niệm của lý tưởng (ideal) của K-algebra.

> **Định nghĩa 33.11.** Cho $A$ là K-algebra. lý tưởng (ideal) $\mathfrak{A} \subseteq A$ là không gian con tuyến tính của $A$ rằng là cũng hai phía lý tưởng (ideal) đối với phép nhân trong $A$; điều này có nghĩa là với mọi $a \in \mathfrak{A}$ và tất cả $\alpha , \beta  \in A$, ta có $\alpha a\beta  \in \mathfrak{A}$. Nếu trường $K$ là understood, ta thường đơn giản nói đại số thay vì của K-algebra. Ta sẽ like để định nghĩa phép toán nhân trên T(V) mà làm cho nó vào K- đại số. Như
$$T(V ) =MV^{\otimes i} ,$$
$$i\ge 0$$
Với mọi $i \ge 0$, có một tự nhiên đơn ánh $\iota_{n}$: $V^{\otimes n} \to$ T(V), và đặc biệt, đơn ánh $\iota_{0}$: $K \to$ T(V). multiplicative unit $1$ của T(V) là ảnh (image) $\iota_{0} (1)$ trong T(V) của unit $1$ của trường $K$. Vì mọi $v \in$ T(V) có thể được biểu diễn dưới dạng hữu hạn tổng
$$v = \iota_{n1} (v_{1}) + \cdots  + \iota_{nk} (v_{k}),$$
Ở đâu $v_{i} \in V^{\otimes ni}$ và $n_{i}$ là tự nhiên các số với $n_{i} \neq  n_{j}$ nếu $i \neq  j$, để định nghĩa phép nhân trong T(V), bằng cách sử dụng tính song tuyến tính, nó là đủ để định nghĩa phép nhân các phép toán $\sim \cdot$: $V^{\otimes m} \times  V^{\otimes n} \longrightarrow V^{\otimes(m+n)}$, mà, bằng cách sử dụng các đẳng cấu $V^{\otimes n} = \iota_{n} (V^{\otimes n})$, cho phép nhân các phép toán $\cdot$: $\iota_{m} (V^{\otimes m}) \times  \iota_{n} (V^{\otimes n}) \longrightarrow \iota_{m+n} (V^{\otimes(m+n)})$. Thứ nhất, cho $\omega_{1}  \in V^{\otimes m}$ và $\omega_{2}  \in V^{\otimes n}$, ta cho
$$\omega_{1}  \cdot  \omega_{2}  = \omega_{1}  \otimes \omega_{2} .$$
Điều này định nghĩa ánh xạ song tuyến tính (bilinear map) do đó nó định nghĩa phép nhân $V^{\otimes m} \times  V^{\otimes n} \longrightarrow V^{\otimes m} \otimes V^{\otimes n}$. Điều này là không khá những gì ta muốn, nhưng có một chính tắc đẳng cấu
$$\sim$$
$$V^{\otimes m}\otimes V^{\otimes n}= V^{\otimes(m+n)}$$
Mà cho ta mong muốn phép nhân $\cdot$: $V^{\otimes m} \times  V^{\otimes n} \longrightarrow V^{\otimes(m+n)}$.
$$\sim$$
Đẳng cấu $V^{\otimes m} \otimes V^{\otimes n} = V^{\otimes(m+n)}$ có thể được được thiết lập bởi quy nạp bằng cách sử dụng
$$\otimes  \otimes  \sim  \otimes  \otimes  \ge$$
Đẳng cấu $(E F) G = E F G$. Thứ nhất ta chứng minh bằng quy nạp theo $m 2$ rằng
$$\sim$$
$$V^{\otimes(m-1)}\otimes V= V^{\otimes m},$$

<!-- PAGE 1201 -->
Và thì bằng quy nạp theo $n \ge 1$ hơn
$$\sim$$
$$V^{\otimes m}\otimes V^{\otimes n}= V^{\otimes(m+n)}.$$
Trong tóm tắt phép nhân $V^{\otimes m} \times  V^{\otimes n} \longrightarrow V^{\otimes(m+n)}$ được định nghĩa sao cho
$$(v_{1} \otimes \cdots  \otimes v_{m}) \cdot  (w_{1} \otimes \cdots  \otimes w_{n}) = v_{1} \otimes \cdots  \otimes v_{m} \otimes w_{1} \otimes \cdots  \otimes w_{n}.$$
(Điều này có được tạo chặt chẽ bằng cách sử dụng các đẳng cấu liên quan đến tính kết hợp của các tích tenxơ, cho chi tiết, xem Jacobson $[102]$, Mục 3.9, hoặc Bertin $[15]$, Chương $4$, Mục $2.)$

> **Định nghĩa 33.12.** Cho trước vectơ $K$ không gian $V$ (không nhất thiết hữu hạn dimensional), không gian vectơ (vector space)
$$T(V ) =MV^{\otimes m}$$
$$m\ge 0$$
$$denoted T^{\bullet}(V ) or \bigotimes  V equipped with the multiplication operations V^{\otimes m}\times V^{\otimes n}\longrightarrow V^{\otimes(m+n)}$$
Được định nghĩa ở trên được gọi là đại số tenxơ (tensor algebra) của $V$.
Nhận xét: Nó là quan trọng đến lưu ý rằng phép nhân trong T(V) là không giao hoán. Cũng, trong tất cả rigor, unit $1$ của T(V) là không bằng $1$, unit của trường $K$. Tuy nhiên, xét theo đơn ánh $\iota_{0}$: $K \to$ T(V), cho sake của notational simplicity, ta sẽ ký hiệu $1$ bởi $1$. Tổng quát hơn, xét theo các đơn ánh $\iota_{n}$: $V^{\otimes n} \to$ T(V), ta đồng nhất các phần tử của $V^{\otimes n}$ với của chúng các ảnh trong T(V). đại số T(V) thỏa mãn phổ dụng ánh xạ tính chất mà chỉ ra rằng nó là duy nhất sai khác một đẳng cấu (up to isomorphism). Để đơn giản của ký hiệu, cho $i: V \to$ T(V) là tự nhiên đơn ánh của $V$ vào T(V).
$$Proposition 33.21. Given any \frac{K}{f :} -algebra A, for any linear map f : V \to A, there is a$$
Duy nhất K-algebra đồng cấu T(V) $\to A$ sao cho
$$f =\overline{f} \circ i,$$
Như trong biểu đồ ở dưới.
$$VT(V )$$
$$\overline{E}^{i}\overline{E}$$
$$\overline{E} E$$
$$EE$$
$$EE$$
$$fE^{f}"$$
$$A$$

*Chứng minh.* Trái bài tập (sử dụng Định lý 33.6). chứng minh có thể được tìm thấy trong Knapp $[107]$ (Phụ lục $A$, Mệnh đề.14) hoặc Bertin $[15]$ (Chương $4$, Định lý 2.4). Mệnh đề 33.21 suy ra rằng có một tự nhiên đẳng cấu
$$\sim$$
$$Hom_{alg}(T(V ), A)= Hom(V, A),$$
Ở đâu đại số $A$ trên vế phải được quan điểm như không gian vectơ (vector space). Mệnh đề 33.21 cũng có sau đây hệ quả.

<!-- PAGE 1202 -->

> **Mệnh đề 33.22.** Cho trước ánh xạ tuyến tính (linear map) $h: V_{1} \to V_{2}$ giữa hai các vectơ các không gian $V_{1}, V_{2}$ trên trường $K$, tồn tại duy nhất một K-algebra đồng cấu $\otimes h: T(V_{1}) \to T(V_{2})$ tạo ra sau đây biểu đồ giao hoán.
$$i1$$
$$V_{1}T(V_{1})$$
$$h\otimes h$$
$$i2  /$$
$$V_{2}T(V_{2}).$$
Hầu hết các đại số của interest phát sinh cũng vậy-được chọn các thương của đại số tenxơ (tensor algebra) T(V). Điều này
$$is true for the exterior algebra \bigwedge  (V ) (also called Grassmann algebra), where we take the$$
Thương của T(V) modulo lý tưởng (ideal) được sinh bởi tất cả các phần tử của tạo thành $v \otimes v$, ở đâu $v \in V$,và cho đối xứng đại số Sym(V), ở đâu ta lấy thương của T(V) modulo lý tưởng (ideal) được sinh bởi tất cả các phần tử của tạo thành $v \otimes w$ - $w \otimes v$, ở đâu $v, w \in V$. Các đại số chẳng hạn như T(V) là graded trong nghĩa rằng có một dãy của các không gian con $V^{\otimes n} \subseteq$ T(V) sao cho
$$T(V ) =MV^{\otimes n} ,$$
$$k\ge 0$$
Và phép nhân $\otimes$ behaves tốt w.r.t. grading, i.e., $\otimes$: $V^{\otimes m} \times  V^{\otimes n} \to V^{\otimes(m+n)}$.

> **Định nghĩa 33.13.** K-algebra $E$ được nói là graded đại số khi và chỉ khi có một dãy của các không gian con $E^{n} \subseteq E$ sao cho
$$E =ME^{n},$$
$$k\ge 0$$
(với $E^{0} = K)$ và phép nhân $\cdot$ các đối với grading; nghĩa là, $\cdot$: $E^{m} \times  E^{n} \to E^{m+n}$. Các phần tử trong $E^{n}$ được gọi là thuần nhất các phần tử của hạng (rank) (hoặc bậc) $n$. Nếu $E$ và $F$ là hai K-algebras, ta biết rằng của chúng tích tenxơ (tensor product) $E \otimes F$ tồn tại như không gian vectơ (vector space). Ta có thể tạo $E \otimes F$ vào đại số cũng vậy. Thật vậy, ta có ánh xạ đa tuyến tính (multilinear map)
$$E \times  F \times  E \times  F \longrightarrow E \otimes F$$
Cho trước bởi (, $b, c, d) \mapsto$ (ac) $\otimes$ (bd), ở đâu ac là tích của và $c$ trong $E$ và bd là tích của $b$ và $d$ trong $F$. Bởi phổ dụng ánh xạ tính chất, ta thu được ánh xạ tuyến tính (linear map),
$$E \otimes F \otimes E \otimes F \longrightarrow E \otimes F.$$
Bằng cách sử dụng đẳng cấu
$$\otimes  \otimes  \otimes  \sim  \otimes  \otimes  \otimes$$
$$EFEF= (EF)(EF),$$
Ta thu được ánh xạ tuyến tính (linear map)
$$(E \otimes F) \otimes (E \otimes F) \longrightarrow E \otimes F,$$
Và do đó ánh xạ song tuyến tính (bilinear map),
$$(E \otimes F) \times  (E \otimes F) \longrightarrow E \otimes F$$
