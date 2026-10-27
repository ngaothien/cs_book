# Các môđun trên Vành giao hoán (commutative ring)


<!-- PAGE 1273 -->
Chương $35$ Giới thiệu đến Các môđun; Các môđun trên PID

## 35.1 Các môđun trên Vành giao hoán (commutative ring)

Trong chương này ta giới thiệu các môđun trên vành giao hoán (commutative ring) (với unity). Sau quick overview của cơ bản các khái niệm chẳng hạn như các môđun tự do, xoắn (torsion) các môđun, và một số cơ bản các kết quả về chúng, ta focus trên sinh hữu hạn (finitely generated) các môđun trên PID và ta chứng minh cấu trúc các định lý cho điều này lớp của các môđun (các nhân tử bất biến (invariant factors) và các ước sơ cấp (elementary divisors)). Của ta chính mục tiêu là không đến cho toàn diện trình bày của các môđun, nhưng thay vì để áp dụng cấu trúc định lý đến K[X]-môđun $E_{f}$ được định nghĩa bởi ánh xạ tuyến tính (linear map) $f$ acting trên không gian vectơ hữu hạn chiều $E$, và để thu được một vài chuẩn tắc/bình thường các dạng cho $f$, bao gồm cả dạng chính tắc hữu tỷ (rational canonical form). môđun là tổng quát hóa của không gian vectơ (vector space) $E$ trên trường $K$ thu được thay thế trường $K$ bởi vành giao hoán (commutative ring) $A$ (với unity $1)$. Mặc dù một cách hình thức định nghĩa là cùng, sự kiện rằng một số khác không các phần tử của $A$ là không khả nghịch có một số serious các hệ quả. Ví dụ, nó là khả dĩ/có thể rằng $\lambda  \cdot  u = 0$ với một số khác không $\lambda  \in A$ và một số khác không $u \in E$, và môđun có thể không có dài hơn có cơ sở (basis). Cho sake của tính đầy đủ, ta cho định nghĩa của môđun, mặc dù nó là cùng như Định nghĩa 3.1 với trường $K$ được thay thế bởi vành $A$. Trong chương này, tất cả các vành dưới consideration được giả sử là giao hoán và đến có phần tử đơn vị (identity element) $1$.

> **Định nghĩa 35.1.** Cho trước vành $A$, (trái) môđun trên $A$ (hoặc A-module) là tập hợp $M$ (của các vectơ) cùng với hai các phép toán $+: M \times M \to M$ (được gọi là vectơ $addition),^{1}$ và $\cdot$: $A\times M \to M$ (được gọi là vô hướng (scalar) phép nhân) thỏa mãn sau đây các điều kiện với mọi $\alpha , \beta  \in A$ và tất cả $u, v \in M$;
(M0) $M$ là nhóm Abel (abelian group) w.r.t. $+$, với phần tử đơn vị (identity element) $0; \overline{1}\overline{The} \overline{symbol} \overline{+} \overline{is} \overline{overloaded,} \overline{since} \overline{it} \overline{denotes}$ cả hai phép cộng trong vành $A$ và phép cộng của các vectơ trong $M$. Nó là thường rõ ràng từ context mà $+$ là intended.
$$1273$$

<!-- PAGE 1274 -->
(M1) $\alpha  \cdot  (u + v) = (\alpha  \cdot  u) + (\alpha  \cdot  v)$;
(M2) $(\alpha  + \beta$) $\cdot  u = (\alpha  \cdot  u) + (\beta  \cdot  u)$;
(M3) $(\alpha$ * $\beta$) $\cdot  u = \alpha  \cdot  (\beta  \cdot  u)$;
(M4) $1 \cdot  u = u$. Cho trước $\alpha  \in A$ và $v \in M$, phần tử $\alpha  \cdot  v$ cũng được ký hiệu bởi $\alpha v$. vành $A$ là thường được gọi là vành của các vô hướng. Trừ khi specified ngược lại hoặc trừ khi ta là dealing với một vài khác nhau các vành, trong rest của điều này chương, ta giả sử rằng tất cả A-modules được định nghĩa đối với cố định vành $A$. Do đó, ta sẽ refer đến A-module đơn giản như môđun. Từ (M0), môđun luôn luôn chứa null vectơ $0$, và do đó là khác rỗng. Từ (M1), ta thu được $\alpha  \cdot  0 = 0$, và $\alpha  \cdot  (-v) = -(\alpha  \cdot  v)$. Từ (M2), ta thu được $0 \cdot  v = 0$, và $(-\alpha$) $\cdot  v = -(\alpha  \cdot  v)$. vành $A$ chính nó có thể được được quan điểm như môđun trên chính nó, phép cộng của các vectơ đang là phép cộng trong vành, và phép nhân bởi vô hướng (scalar) đang là phép nhân trong vành. Khi vành $A$ là trường, A-module là không gian vectơ (vector space). Khi $A =\mathbb{Z}, a \mathbb{Z}-module$ là chỉ nhóm Abel (abelian group), với action cho trước bởi
$$0 \cdot  u = 0,$$
$$n \cdot  u = u + \cdots  + u,n > 0$$
$$|{z}$$
$$n$$
$$n \cdot  u = -(-n) \cdot  u,n < 0.$$
Tất cả các định nghĩa từ Mục 3.4, các tổ hợp tuyến tính, sự độc lập tuyến tính (linear independence) và sự phụ thuộc tuyến tính (linear dependence), các không gian con renamed như các môđun con, áp dụng unchanged đến các môđun. Mệnh đề 3.6 cũng nghiệm đúng cho môđun được sinh (spanned) bởi tập hợp của các vectơ. định nghĩa của cơ sở (basis) (Định nghĩa 3.6) cũng áp dụng đến các môđun, nhưng chỉ kết quả từ Mục 3.5 rằng nghiệm đúng cho các môđun là Mệnh đề 3.14. Không may là, nó là dài hơn đúng rằng mọi môđun có cơ sở (basis). Ví dụ, với mọi khác không số nguyên $n \in \mathbb{Z}$, $\mathbb{Z}-module \mathbb{Z}/n\mathbb{Z}$ có không có cơ sở (basis) vì $n \cdot \overline{x} = 0$ với mọi $\overline{x} \in \mathbb{Z}/n\mathbb{Z}$. Tương tự, $\mathbb{Q}$, như $a \mathbb{Z}-module$, có không có cơ sở (basis). Bất kỳ hai phân biệt khác không các phần tử $p_{1}/q_{1}$ và $p_{2}/q_{2}$ là phụ thuộc tuyến tính (linearly dependent), vì
$$(p_{2}q_{1}) \begin{pmatrix} p_{1} \\ q_{1} \end{pmatrix} -(p_{1}q_{2}) \begin{pmatrix} p_{2} \\ q_{2} \end{pmatrix} = 0.$$
Hơn nữa, $\mathbb{Z}-module \mathbb{Q}$ là không sinh hữu hạn (finitely generated). Cho nếu ${p_{1}/q_{1}, \cdots  p_{n}/q_{n}} \subset \mathbb{Q}$ được sinh $\mathbb{Q}$, thì với mọi $x = r/s \in \mathbb{Q}$, ta có
$$c_{1} \frac{p_{1}}{q_{1}} + \cdots  + c_{n} \frac{p_{n}}{q_{n}} = \frac{r}{s} ,$$

<!-- PAGE 1275 -->
Ở đâu $c_{i} \in \mathbb{Z}$ cho $i = 1, \dots  , n$. trái hand vế/cạnh của trước đó đường thẳng là tương đương đến
$$\frac{c_{1}p_{1}q_{2} q_{n} + + c_{n}p_{n}q_{1} q_{n-1}}{q_{1}q_{2} \cdots  q_{n}} \cdots  \cdots  \cdots ,$$
Ở đâu numerator là phần tử của lý tưởng (ideal) trong $\mathbb{Z}$ được sinh (spanned) bởi $(c_{1}, c_{2}, \cdots  , c_{n})$. Vì $\mathbb{Z}$ là PID, tồn tại $a \in \mathbb{Z}$ sao cho () là lý tưởng (ideal) được sinh (spanned) bởi $(c_{1}, c_{2}, \cdots  , c_{n})$. Do đó
$$c_{1} \frac{p_{1}}{q_{1}} + \cdots  + c_{n} \frac{p_{n}}{q_{n}} = \frac{ma}{q_{1}q_{2} \cdots  q_{n}} = \frac{r}{s} ,$$
Ở đâu $m \in \mathbb{Z}$. Tập hợp
$$\frac{a}{q_{1}q_{2} \cdots  q_{n}} = \frac{a_{1}}{b} ,(a_{1}, b) = 1.$$
Thì nếu $\mathbb{Q}$ đã là sinh hữu hạn (finitely generated) $\mathbb{Z}-module$, ta suy ra rằng với mọi $x \in \mathbb{Q}$
$$ma_{1}$$
$$x = \frac{r}{s} =\overline{b} ,$$
Bất cứ khi nào $a_{1}/b$ là cố định hữu tỷ số, rõ ràng một mâu thuẫn. (Đặc biệt cho $x = 1/p$ ở đâu $p$ là cố định nguyên tố $p > b$. Nếu $ma_{1}/b = 1/p$, thì $ma_{1} \in \mathbb{Z}$ với $ma_{1} = b_{1}/p$, impossiblity vì $(b_{1}, p) = 1$ và $p > b_{1}.)$ Định nghĩa 3.11 có thể được suy rộng/tổng quát hóa đến các vành và cho ta các môđun tự do.

> **Định nghĩa 35.2.** Cho trước vành giao hoán (commutative ring) $A$ và bất kỳ (khác rỗng) tập hợp $I$, cho $A^{(I)}$ là tập con của cartesian tích $A^{I}$ bao gồm của tất cả các họ $(\lambda_{i} )_{i\in I}$ với hữu hạn hỗ trợ/giá (support) của các vô hướng trong $A.^{2}$ Ta định nghĩa phép cộng và phép nhân bởi vô hướng (scalar) như sau:
$$(\lambda_{i} )_{i\in I} + (\mu_{i} )_{i\in I} = (\lambda_{i}  + \mu_{i} )_{i\in I},$$
Và
$$\lambda  \cdot  (\mu_{i} )_{i\in I} = (\lambda \mu_{i} )_{i\in I}.$$
Ta kiểm chứng được ngay rằng phép cộng và phép nhân bởi vô hướng (scalar) là tốt được định nghĩa. Do đó, $A^{(I)}$ là môđun. Hơn nữa, bởi vì các họ với hữu hạn hỗ trợ/giá (support) được xét, họ $(e_{i})_{i\in I}$ của các vectơ $e_{i}$, được định nghĩa sao cho $(e_{i})_{j} = 0$ nếu $j \neq  i$ và $(e_{i})_{i} = 1$, là rõ ràng cơ sở (basis) của môđun $A^{(I)}$. Khi $I = {1, \dots  , n}$, ta ký hiệu $A^{(I)}$ bởi $A^{n}$. hàm $\iota$: I $\to A^{(I)}$, sao cho $\iota (i) = e_{i}$ với mọi $i \in$ I, là rõ ràng đơn ánh.

> **Định nghĩa 35.3.** A-module $M$ là tự do khi và chỉ khi nó có cơ sở (basis). môđun $A^{(I)}$ là môđun tự do (free module). Tất cả các định nghĩa từ Mục 3.7 áp dụng đến các môđun, các ánh xạ tuyến tính (linear maps), hạt nhân (kernel), ảnh (image), ngoại trừ định nghĩa của hạng (rank), mà có được định nghĩa một cách khác nhau. Các mệnh đề 3.19, 3.20, 3.21, và $\overline{2} \overline{Where} \overline{A}^{I} \overline{denotes} \overline{the} \overline{set} \overline{of} \overline{all} \overline{functions}$ từ I đến $A$.

<!-- PAGE 1276 -->
3.22 đúng cho các môđun. Tuy nhiên, khác các mệnh đề thực hiện không tổng quát hóa đến các môđun. định nghĩa của đẳng cấu tổng quát hóa đến các môđun. Hệ quả là, môđun là tự do khi và chỉ khi nó là đẳng cấu đến môđun của tạo thành $A^{(I)}$. Mục 3.8 tổng quát hóa đến các môđun. Cho trước môđun con $N$ của môđun $M$, ta có thể định nghĩa thương môđun $M/N$. Nếu $\mathfrak{a}$ là lý tưởng (ideal) trong $A$ và nếu $M$ là A-module, ta định nghĩa $\mathfrak{a} M$ như tập hợp của hữu hạn các tổng của tạo thành
$$a_{1}m_{1} + \cdots  + a_{k}m_{k},a_{i} \in \mathfrak{a}, m_{i} \in M.$$
Ta kiểm chứng được ngay rằng $\mathfrak{a} M$ là môđun con của $M$. một cách thú vị, phần của Định lý 3.12 rằng khẳng định rằng bất kỳ hai các cơ sở của không gian vectơ (vector space) có cùng cardinality nghiệm đúng cho các môđun. Một cách để chứng minh sự kiện này là đến “đi qua” đến không gian vectơ (vector space) bởi thương process.

> **Định lý 35.1.** Với mọi môđun tự do (free module) $M$, bất kỳ hai các cơ sở của $M$ có cùng cardinality. Chứng minh phác thảo. Ta cho lập luận cho hữu hạn các cơ sở, nhưng nó cũng nghiệm đúng cho vô hạn các cơ sở. mẹo/kỹ thuật là đến chọn bất kỳ lý tưởng cực đại (maximal ideal) $\mathfrak{m}$ trong $A$ (có sự tồn tại là guaranteed theo Định lý C.3). Thì, $A/\mathfrak{m}$ là trường, và $M/\mathfrak{m} M$ có thể được được tạo vào không gian vectơ (vector space) trên $A/\mathfrak{m}$; ta để lại chi tiết như một bài tập. Nếu $(u_{1}, \dots  , u_{n})$ là cơ sở (basis) của $M$, thì nó là dễ để xem rằng ảnh (image) của cơ sở (cơ sở (basis)) này là cơ sở (basis) của không gian vectơ (vector space) $M/\mathfrak{m} M$. Theo Định lý 3.12, số $n$ của các phần tử trong bất kỳ cơ sở (basis) của $M/\mathfrak{m} M$ là bất biến, do đó bất kỳ hai các cơ sở của $M$ phải có cùng số của các phần tử.

> **Định nghĩa 35.4.** chung/phổ biến số của các phần tử trong bất kỳ cơ sở (basis) của môđun tự do (free module) được gọi là số chiều (hoặc hạng (rank)) của môđun tự do (free module). Một nên realize rằng khái niệm của sự độc lập tuyến tính (linear independence) trong môđun là little khó/tinh tế. Theo định nghĩa, one-element dãy $(u)$ bao gồm của đơn lẻ khác không vectơ là độc lập tuyến tính (linearly independent) nếu với mọi $\lambda  \in A$, nếu $\lambda u = 0$ thì $\lambda  = 0$. Tuy nhiên, có các môđun tự do rằng chứa khác không các vectơ rằng là không độc lập tuyến tính (linearly independent)! Ví dụ, vành $A = \mathbb{Z}/6\mathbb{Z}$ được quan điểm như môđun trên chính nó có cơ sở (basis) $(1)$, nhưng zero-divisors, chẳng hạn như $2$ hoặc $4$, là không độc lập tuyến tính (linearly independent). Bằng cách sử dụng language đã giới thiệu trong Định nghĩa 35.5, môđun tự do (free module) có thể có xoắn (torsion) các phần tử. Có cũng nonfree các môđun sao cho mọi khác không vectơ là độc lập tuyến tính (linearly independent), chẳng hạn như $\mathbb{Q}$ trên $\mathbb{Z}$. Tất cả các định nghĩa từ Mục 4.1 về các ma trận áp dụng đến các môđun tự do, và do đó thực hiện tất cả các mệnh đề. Tương tự, tất cả các định nghĩa từ Mục 6.1 về các tổng trực tiếp và trực tiếp các tích áp dụng đến các môđun. Tất cả các mệnh đề rằng thực hiện không liên quan đến mở rộng các cơ sở vẫn đúng. quan trọng Mệnh đề 6.15 survives trong sau đây tạo thành.

<!-- PAGE 1277 -->

> **Mệnh đề 35.2.** Cho $f$: $E \to F$ là toàn ánh (surjective) ánh xạ tuyến tính (linear map) giữa hai A-modules với $F$ môđun tự do (free module). Cho trước bất kỳ cơ sở (basis) $(v_{1}, \dots  , v_{r})$ của $F$, với mọi $r$ các vectơ $u_{1}, \dots  , u_{r} \in E$ sao cho $f(u_{i}) = v_{i}$ cho $i = 1, \dots  , r$, các vectơ $(u_{1}, \dots  , u_{r})$ là độc lập tuyến tính (linearly independent) và môđun $E$ là tổng trực tiếp (direct sum)
$$E = \mathrm{Ker} (f) \oplus U,$$
Ở đâu $U$ là tự do môđun con của $E$ được sinh (spanned) bởi cơ sở (basis) $(u_{1}, \dots  , u_{r})$.

*Chứng minh.* Chọn bất kỳ $w \in E$, viết f(w) trên cơ sở (basis) $(v_{1}, \dots  , v_{r})$ như f(w) $= a_{1}v_{1} + \cdots  + a_{r}v_{r}$, và cho $u = a_{1}u_{1} + \cdots  + a_{r}u_{r}$. Nhận thấy rằng
$$f(w -u) = f(w) -f(u)$$
$$= a_{1}v_{1} + \cdots  + a_{r}v_{r} -(a_{1}f(u_{1}) + \cdots  + a_{r}f(u_{r}))$$
$$= a_{1}v_{1} + \cdots  + a_{r}v_{r} -(a_{1}v_{1} + \cdots  + a_{r}v_{r})$$
$$= 0.$$
Vì vậy, $h = w$ - $u \in$ Ker $(f)$, và vì $w = h + u$ với $h \in$ Ker $(f)$ và $u \in U$, ta có $E =$ Ker $(f) + U$. Nếu $u = a_{1}u_{1} + \cdots  + a_{r}u_{r} \in U$ cũng thuộc đến Ker $(f)$, thì
$$0 = f(u) = f(a_{1}u_{1} + \cdots  + a_{r}u_{r}) = a_{1}v_{1} + \cdots  + a_{r}v_{r},$$
Và vì $(v_{1}, \dots  , v_{r})$ là cơ sở (basis), $a_{i} = 0$ cho $i = 1, \dots  , r$, mà chỉ ra rằng Ker $(f) \cap U = (0)$. Vì vậy, ta có tổng trực tiếp (direct sum)
$$E = \mathrm{Ker} (f) \oplus U.$$
Cuối cùng, nếu
$$a_{1}u_{1} + \cdots  + a_{r}u_{r} = 0,$$
Ở trên lập luận chỉ ra rằng $a_{i} = 0$ cho $i = 1, \dots  , r$, do đó $(u_{1}, \dots  , u_{r})$ là độc lập tuyến tính (linearly independent). Vì vậy, môđun $U$ là môđun tự do (free module). Một nên là biết rằng nếu ta có tổng trực tiếp (direct sum) của các môđun
$$U = U_{1} \oplus \cdots  \oplus U_{m},$$
Mọi vectơ $u \in U$ có thể được được viết là duy nhất cách như
$$u = u_{1} + \cdots  + u_{m},$$
Với $u_{i} \in U_{i}$ nhưng, unlike trường hợp của các không gian vectơ, điều này thực hiện không suy ra rằng bất kỳ $m$ khác không các vectơ $(u_{1}, \dots  , u_{m})$ là độc lập tuyến tính (linearly independent). Ví dụ, ta có tổng trực tiếp (direct sum)
$$\mathbb{Z}/2\mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}$$

<!-- PAGE 1278 -->
Ở đâu $\mathbb{Z}/2\mathbb{Z}$ được quan điểm như $a \mathbb{Z}-modules$, nhưng $(1, 0)$ và $(0, 1)$ là không độc lập tuyến tính (linearly independent), vì
$$2(1, 0) + 2(0, 1) = (0, 0).$$
Hữu ích sự kiện là rằng mọi môđun là thương của một số môđun tự do (free module). Thật vậy, nếu $M$ là A-module, chọn bất kỳ tập sinh (spanning set) $I$ cho $M$ (như vậy tập hợp tồn tại, ví dụ, $I = M)$, và xét duy nhất đồng cấu $\phi$: $A^{(I)} \to M$ mở rộng đồng nhất thức hàm từ I đến chính nó. Thì ta có đẳng cấu $A^{(I)}/Ker (\phi$) $\approx M$. Đặc biệt, nếu $M$ là sinh hữu hạn (finitely generated), ta có thể chọn I là hữu hạn tập hợp của các phần tử sinh, trong mà trường hợp ta thu được đẳng cấu $A^{n}/Ker (\phi$) $\approx M$, với một số tự nhiên số $n$. sinh hữu hạn (finitely generated) môđun đôi khi được gọi là một môđun của hữu hạn loại/kiểu. trường hợp $n = 1$ là của cụ thể interest. môđun $M$ được nói là xích (cyclic) nếu nó được sinh bởi đơn lẻ phần tử. Trong điều này trường hợp $M =$ Ax, với một số $x \in M$. Ta có ánh xạ tuyến tính (linear map) $m_{x}$: $A \to M$ cho trước bởi $a \mapsto$ ax với mọi $a \in A$, và nó là hiển nhiên toàn ánh (surjective) vì $M =$ Ax. Vì hạt nhân (kernel) $\mathfrak{a} =$ Ker $(m_{x})$ của $m_{x}$ là lý tưởng (ideal) trong $A$, ta thu được đẳng cấu $A/\mathfrak{a} \approx$ Ax. Ngược lại, với mọi lý tưởng (ideal) $\mathfrak{a}$ của $A$, nếu $M = A/\mathfrak{a}$, ta xem rằng $M$ được sinh bởi ảnh (image) $x$ của $1$ trong $M$, do đó $M$ là xích (cyclic) môđun. lý tưởng (ideal) $\mathfrak{a} =$ Ker $(m_{x})$ là tập hợp tất cả $a \in A$ sao cho ax $= 0$. Điều này được gọi là linh hóa tử (annihilator) của $x$, và nó là đặc biệt trường hợp của sau đây nhiều hơn/thêm tổng quát tình huống.

> **Định nghĩa 35.5.** Nếu $M$ là bất kỳ A-module, với mọi tập con $S$ của $M$, tập hợp tất cả $a \in A$ sao cho ax $= 0$ với mọi $x \in S$ được gọi là linh hóa tử (annihilator) của $S$, và nó được ký hiệu bởi Ann(S). Nếu $S = {x}$, ta viết Ann(x) thay vì của $Ann({x})$. khác không phần tử $x \in M$ được gọi là một xoắn (torsion) phần tử khi và chỉ khi Ann(x) $\neq  (0)$. tập hợp bao gồm của tất cả xoắn (torsion) các phần tử trong $M$ và $0$ được ký hiệu bởi $M_{tor}$. Ta kiểm chứng được ngay rằng Ann(S) là lý tưởng (ideal) của $A$, và theo Định nghĩa,
$$M_{tor} = {x \in M | (\exists a \in A, a \neq  0)(ax = 0)}.$$
Nếu vành có không các ước, thì tập hợp tất cả xoắn (torsion) các phần tử trong A-module $M$ có thể không là môđun con của $M$. Ví dụ, nếu $M = A =\mathbb{Z}/6\mathbb{Z}$, thì $M_{tor} = {2, 3, 4}$, nhưng $3 + 4 = 1$ là không xoắn (torsion) phần tử. Cũng, môđun tự do (free module) có thể không là không xoắn (torsion-free) bởi vì ở đó có thể là xoắn (torsion) các phần tử, như ví dụ của $\mathbb{Z}/6\mathbb{Z}$ như môđun tự do (free module) trên chính nó chỉ ra. Tuy nhiên, nếu $A$ là miền nguyên (integral domain), thì môđun tự do (free module) là không xoắn (torsion-free) và $M_{tor}$ là môđun con của $M$. (Nhắc lại rằng miền nguyên (integral domain) là giao hoán).

> **Mệnh đề 35.3.** Nếu $A$ là miền nguyên (integral domain), thì với mọi A-module $M$, tập hợp $M_{tor}$ của xoắn (torsion) các phần tử trong $M$ là môđun con của $M$.

*Chứng minh.* Nếu $x, y \in M$ là xoắn (torsion) các phần tử $(x, y \neq  0)$, thì ở đó tồn tại một số khác không các phần tử, $b \in A$ sao cho ax $= 0$ và bởi $= 0$. Vì $A$ là miền nguyên (integral domain), ab $\neq  0$, và thì với mọi $\lambda , \mu  \in A$, ta có
$$ab(\lambda x + \mu y) = b\lambda ax + a\mu by = 0.$$

<!-- PAGE 1279 -->
Vì vậy, $M_{tor}$ là môđun con của $M$. môđun $M_{tor}$ được gọi là xoắn (torsion) môđun con của $M$. Nếu $M_{tor} = (0)$, thì ta nói rằng $M$ là không xoắn (torsion-free), và nếu $M = M_{tor}$, thì ta nói rằng $M$ là môđun xoắn (torsion module). Nếu $M$ là không sinh hữu hạn (finitely generated), thì nó là khả dĩ/có thể rằng $M_{tor}$ ̸ $= 0$, vẫn chưa linh hóa tử (annihilator) của $M_{tor}$ là rút gọn đến $0$. Ví dụ, cho lấy $\mathbb{Z}-module$
$$\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z} \times \mathbb{Z}/5\mathbb{Z} \times  \cdots  \times \mathbb{Z}/p\mathbb{Z} \times  \cdots  ,$$
Ở đâu $p$ các miền giá trị (range) trên tập hợp của các nguyên tố. Gọi điều này môđun $M$ và tập hợp của các nguyên tố $P$. Nhận thấy rằng $M$ được sinh bởi ${\alpha_{p} }_{p\in P}$, ở đâu $\alpha_{p}$ là bộ có chỉ khác không phần tử (entry) là $\overline{1}_{p}$, phần tử sinh của $\mathbb{Z}/p\mathbb{Z}$, i.e.,
$$\alpha_{p}  \overline{= (0},\overline{0},\overline{0}, \cdots  ,\overline{1}_{p},\overline{0}, \cdots  ),\mathbb{Z}/p\mathbb{Z} = {n \cdot \overline{1}_{p}}_{n=0}^{p-1}.$$
Nói cách khác, $M$ là không sinh hữu hạn (finitely generated). Hơn nữa, vì $p\cdot \overline{1}_{p} \overline{= 0$, ta $have} {\alpha_{p} }_{p\in P} \subset M_{tor}$. Tuy nhiên, bởi vì $p$ các miền giá trị (range) trên tất cả các nguyên tố, chỉ khả dĩ/có thể khác không linh hóa tử (annihilator) của ${\alpha_{p} }_{p\in P}$ sẽ là tích của tất cả các nguyên tố. Do đó $Ann({\alpha_{p} }_{p\in P}) = (0)$. Bởi vì của tập con containment, ta kết luận rằng $Ann(M_{tor}) = (0)$. Tuy nhiên, nếu $M$ là sinh hữu hạn (finitely generated), nó là không khả dĩ/có thể rằng $M_{tor} \neq  0$, vẫn chưa linh hóa tử (annihilator) của $M_{tor}$ là rút gọn đến $0$, vì nếu $x_{1}, \dots  , x_{n}$ sinh $M$ và nếu $a_{1}, \dots  , a_{n}$ annihilate $x_{1}, \dots  , x_{n}$, thì $a_{1} \cdots  a_{n}$ annihilates mọi phần tử của $M$.

> **Mệnh đề 35.4.** Nếu $A$ là miền nguyên (integral domain), thì với mọi A-module $M$, thương môđun $M/M_{tor}$ là xoắn (torsion) tự do.

*Chứng minh.* Cho $\overline{x}$ là phần tử của $M/M_{tor}$ và giả sử rằng $\overline{ax} = 0$ với một số $a \neq  0$ trong $A$. Điều này có nghĩa là ax $\in M_{tor}$, do đó tồn tại một $b \neq  0$ trong $A$ sao cho bax $= 0$. Vì, $b \neq  0$ và $A$ là miền nguyên (integral domain), ba $\neq  0$, do đó $x \in M_{tor}$, mà có nghĩa là $\overline{x} = 0$. Nếu $A$ là miền nguyên (integral domain) và nếu $F$ là tự do A-module với cơ sở (basis) $(u_{1}, \dots  , u_{n})$, thì $F$ có thể được được nhúng trong vectơ $K$ không gian $F_{K}$ đẳng cấu đến $K^{n}$, ở đâu $K =$ Frac() là phân số trường của $A$. Tương tự, bất kỳ môđun con $M$ của $F$ được nhúng vào không gian con $M_{K}$ của $F_{K}$. Lưu ý rằng bất kỳ các vectơ độc lập tuyến tính (linearly independent) $(u_{1}, \dots  , u_{m})$ trong A-module $M$ vẫn là độc lập tuyến tính (linearly independent) trong không gian vectơ (vector space) $M_{K}$, bởi vì bất kỳ sự phụ thuộc tuyến tính (linear dependence) trên $K$ là của tạo thành
$$\frac{a_{1}}{b_{1}} u_{1} + \cdots  + \frac{a_{m}}{b_{m}} u_{m} = 0$$
Với một số $a_{i}, b_{i} \in A$, với $b_{1} \cdots  b_{m}$ ̸ $= 0$, do đó nếu ta nhân bởi $b_{1} \cdots  b_{m}$ ̸ $= 0$, ta thu được sự phụ thuộc tuyến tính (linear dependence) trong A-module $M$. Thì ta xem rằng cực đại số của các vectơ độc lập tuyến tính (linearly independent) trong A-module $M$ là nhiều nhất $n$. cực đại số của các vectơ độc lập tuyến tính (linearly independent) trong sinh hữu hạn (finitely generated) môđun con của môđun tự do (free module) (trên miền nguyên (integral domain)) được gọi là hạng (rank) của môđun $M$. Nếu $(u_{1}, \dots  , u_{m})$ là độc lập tuyến tính (linearly independent) ở đâu

<!-- PAGE 1280 -->
$m$ là hạng (rank) của $m$, thì với mọi khác không $v \in M$, có một số, $a_{1}, \dots  , a_{m} \in A$, không tất cả không, sao cho
$$av = a_{1}u_{1} + \cdots  + a_{m}u_{m}.$$
Ta phải có ̸ $= 0$, vì ngược lại, sự độc lập tuyến tính (linear independence) của $u_{i}$ sẽ suy ra rằng $a_{1} = \cdots  = a_{m} = 0$, contradicting sự kiện rằng, $a_{1}, \dots  , a_{m} \in A$ là không tất cả không. Không may là, nói chung, không xoắn (torsion-free) môđun là không tự do. Cho $example,\mathbb{Q}$ như $a\mathbb{Z}-module$ là không xoắn (torsion-free) nhưng không tự do. Nếu ta thu hẹp chính chúng ta đến sinh hữu hạn (finitely generated) các môđun trên PID’s, thì như vậy các môđun split như tổng trực tiếp (direct sum) của của chúng môđun xoắn (torsion module) với môđun tự do (free module), và môđun xoắn (torsion module) có đẹp phân rã theo xích (cyclic) các môđun. sau đây mệnh đề chỉ ra rằng trên PID, các môđun con của môđun tự do (free module) là tự do. Có khác nhau các cách của chứng minh kết quả này. Ta cho chứng minh do Lang $[113]$ (xem Chương III, Mục $7)$.

> **Mệnh đề 35.5.** Nếu $A$ là PID và nếu $F$ là tự do A-module có số chiều $n$, thì mọi môđun con $M$ của $F$ là môđun tự do (free module) có số chiều nhiều nhất $n$.

*Chứng minh.* Cho $(u_{1}, \dots  , u_{n})$ là cơ sở (basis) của $F$, và cho $M_{r} = M \cap (Au_{1} \oplus \cdots \oplus Au_{r})$, giao của $M$ với môđun tự do (free module) được sinh bởi $(u_{1}, \dots  , u_{r})$, cho $r = 1, \dots  , n$. Ta chứng minh bằng quy nạp theo $r$ rằng mỗi $M_{r}$ là tự do và có số chiều nhiều nhất $r$. Vì $M = M_{r}$ với một số $r$, điều này sẽ chứng minh kết quả của chúng ta. Xét $M_{1} = M \cap Au_{1}$. Nếu $M_{1} = (0)$, ta được thực hiện. Ngược lại cho
$$\mathfrak{a} = {a \in A | au_{1} \in M}.$$
Nó là ngay lập tức được kiểm chứng $that\mathfrak{a}$ là lý tưởng (ideal), và vì $A$ là $PID,\mathfrak{a} = a_{1}A$, với một số $a_{1} \in A$. Vì ta là giả sử rằng $M_{1}$ ̸ $= (0)$, ta có $a_{1}$ ̸ $= 0$, và $a_{1}u_{1} \in M$. Nếu $x \in M_{1}$, thì $x = au_{1}$ với một số $a \in A$, do đó $a \in a_{1}A$, và do đó $a = ba_{1}$ với một số $b \in A$. Suy ra rằng $M_{1} = Aa_{1}u_{1}$, mà là tự do. Giả sử một cách quy nạp rằng $M_{r}$ là tự do có số chiều nhiều nhất $r < n$, và cho
$$\mathfrak{a} = {a \in A | (\exists b_{1} \in A) \cdots  (\exists b_{r} \in A)(b_{1}u_{1} + \cdots  + b_{r}u_{r} + au_{r+1} \in M)}.$$
Ta kiểm chứng được ngay rằng $\mathfrak{a}$ là lý tưởng (ideal), và vì $A$ là PID, $\mathfrak{a} = a_{r+1}A$, với một số $a_{r+1} \in A$. Nếu $a_{r+1} = 0$, thì $M_{r+1} = M_{r}$, và ta được thực hiện. Nếu $a_{r+1} \neq  0$, thì tồn tại một $v_{1} \in Au_{1} \oplus \cdots  \oplus Au_{r}$ sao cho
$$w = v_{1} + a_{r+1}u_{r+1} \in M.$$
Với mọi $x \in M_{r+1}$, tồn tại một $v \in Au_{1}\oplus \cdots \oplus Au_{r}$ và một số $a \in A$ sao cho $x = v+au_{r+1}$. Thì, $a \in a_{r+1}A$, do đó tồn tại một $b \in A$ sao cho $a = ba_{r+1}$. Hệ quả là
$$x -bw = v -bv_{1} \in M_{r},$$

<!-- PAGE 1281 -->
Và do đó $x = x$ - bw $+$ bw với $x$ - bw $\in M_{r}$, mà chỉ ra rằng
$$M_{r+1} = M_{r} + Aw.$$
Mặt khác, nếu $u \in M_{r} \cap$ Aw, khi đó vì $w = v_{1} + a_{r+1}u_{r+1}$ ta có
$$u = bv_{1} + ba_{r+1}u_{r+1},$$
Với một số $b \in A$, với $u, v_{1} \in Au_{1} \oplus \cdots  \oplus Au_{r}$, và nếu $b \neq  0$, điều này cho ta không tầm thường tổ hợp tuyến tính (linear combination)
$$bv_{1} -u + ba_{r+1}u_{r+1} = 0,$$
Contradicting sự kiện rằng $(u_{1}, \dots  , u_{r+1})$ là độc lập tuyến tính (linearly independent). Vì vậy,
$$M_{r+1} = M_{r} \oplus Aw,$$
Mà chỉ ra rằng $M_{r+1}$ là tự do có số chiều nhiều nhất $r + 1$. sau đây hai các ví dụ chỉ ra tại sao giả thiết của Mệnh đề 35.5 đòi hỏi $A$ là PID. Thứ nhất xét $6\mathbb{Z} = {\overline{0},\overline{1},\overline{2},\overline{3},\overline{4},\overline{5}}$ như tự do $6\mathbb{Z}-module$ với phần tử sinh $\overline{1.}$ $6\mathbb{Z}-$ môđun con ${\overline{0},\overline{2},\overline{4}}$ là không tự do, chẵn/ngay cả dù nó được sinh bởi $\overline{2}$ vì $\overline{3} \cdot \overline{2 = 0.}$ Mệnh đề 35.5 không thỏa mãn vì $6\mathbb{Z}$ là không chẵn/ngay cả miền nguyên (integral domain). Tiếp theo $consider\mathbb{Z}[X]$ như $free\mathbb{Z}[X]-module$ với phần tử sinh $1$. Ta khẳng định lý tưởng (ideal)
$$(2, X) = {2p(X) + Xq(X) | p(X), q(X) \in \mathbb{Z}[X]},$$
Là không tự do $\mathbb{Z}[X]-module$. Thật vậy bất kỳ hai khác không các phần tử của $(2, X)$, nói s(X) và t(X), là phụ thuộc tuyến tính (linearly dependent) vì t(X)s(X) - s(X)t(X) $= 0$. Một lần một lần nữa Mệnh đề 35.5 không thỏa mãn vì $\mathbb{Z}[X]$ là không PID. Xem Ví dụ 32.1. Mệnh đề 35.5 suy ra rằng nếu $M$ là sinh hữu hạn (finitely generated) môđun trên PID, thì bất kỳ môđun con $N$ của $M$ là cũng sinh hữu hạn (finitely generated). Thật vậy, nếu $(u_{1}, \dots  , u_{n})$ sinh $M$, thì ta có toàn ánh $\phi$: $A^{n} \to M$ từ môđun tự do (free module) $A^{n}$ lên $M$. nghịch đảo ảnh (image) $\phi^{-1} (N)$ của $N$ là môđun con của môđun tự do (free module) $A^{n}$, vì vậy theo Mệnh đề 35.5, $\phi^{-1} (N)$ là tự do và sinh hữu hạn (finitely generated). Điều này suy ra rằng $N$ là sinh hữu hạn (finitely generated) (và rằng nó có số của các phần tử sinh $\le n)$. Ta có thể cũng chứng minh rằng sinh hữu hạn (finitely generated) không xoắn (torsion-free) môđun trên PID là thực sự tự do. Ta sẽ cho một cái khác chứng minh của sự kiện này sau này, nhưng sau đây chứng minh là instructive.

> **Mệnh đề 35.6.** Nếu $A$ là PID và nếu $M$ là sinh hữu hạn (finitely generated) môđun mà là torsionfree, thì $M$ là tự do.

*Chứng minh.* Cho $(y_{1}, \dots  , y_{n})$ là một số các phần tử sinh cho $M$, và cho $(u_{1}, \dots  , u_{m})$ là cực đại dãy con của $(y_{1}, \dots  , y_{n})$ mà là độc lập tuyến tính (linearly independent). Nếu $m = n$, ta được thực hiện. Ngược lại, do maximality của $m$, cho $i = 1, \dots  , n$, tồn tại một $a_{i}$ ̸ $= 0$ sao cho sao cho
