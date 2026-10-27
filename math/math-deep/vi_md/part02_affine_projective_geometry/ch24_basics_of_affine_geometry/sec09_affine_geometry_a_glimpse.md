# Afin Hình học: Glimpse


<!-- PAGE 843 -->
Một cái khác điểm worth mentioning là rằng afin các song ánh bảo toàn tỉ số của các thể tích của
$$\longrightarrow$$
Parallelotopes. Thật vậy, cho trước bất kỳ cơ sở (basis) $B = (u_{1}, \dots  , u_{m})$ của không gian vectơ (vector space) $E$ liên kết với không gian afin (affine space) $E$, cho trước bất kỳ $m + 1$ độc lập afin (affinely independent) các điểm $(a_{0}, \dots  , a_{m})$, ta có thể
$$-\longrightarrow  -\longrightarrow$$
Tính định thức (determinant) $det_{B}(a_{0}a_{1}, \dots  ,a_{0}a_{m})$ w.r.t. cơ sở (basis) $B$. Với mọi song ánh (bijective) ánh xạ afin (affine map) $f$: $E \to E$, vì
$$-\longrightarrow  -\longrightarrow$$
$$det_{B} \begin{pmatrix} \longrightarrow -\longrightarrow & \longrightarrow -\longrightarrow \\ f(a_{0}a_{1}), \dots  ,f(a_{0}a_{m}) \end{pmatrix} = \det \begin{pmatrix} \longrightarrow \\ f \end{pmatrix} det_{B}(a_{0}a_{1}, \dots  ,a_{0}a_{m})$$
$$\longrightarrow$$
Và định thức (determinant) của ánh xạ tuyến tính (linear map) là nội tại (i.e., phụ thuộc chỉ trên $f$, và không trên cụ thể cơ sở (basis) $B)$, ta kết luận rằng tỉ số
$$det_{B} \begin{pmatrix} \longrightarrow -\longrightarrow & \longrightarrow -\longrightarrow \\ f(a_{0}a_{1}), \dots  ,f(a_{0}a_{m}) \\ det_{B}(-\longrightarrow a_{0}a_{1}, \dots  ,-\longrightarrow a_{0}a_{m}) \end{pmatrix} = \det$$
$$\begin{pmatrix} \longrightarrow \\ f \end{pmatrix}$$
$$-\longrightarrow  -\longrightarrow$$
Là độc lập của cơ sở (basis) $B$. Vì $det_{B}(a_{0}a_{1}, \dots  ,a_{0}a_{m})$ là thể tích của parallelotope được sinh (spanned) bởi $(a_{0}, \dots  , a_{m})$, ở đâu parallelotope được sinh (spanned) bởi bất kỳ điểm và các vectơ $(u_{1}, \dots  , u_{m})$ có unit thể tích (xem Berger $[11]$, Mục 9.12), ta xem rằng afin các song ánh bảo toàn tỉ số của các thể tích của parallelotopes. Thực ra, điều này tỉ số là độc lập của lựa chọn của parallelotopes của unit thể tích. Đặc biệt, afin các song ánh $f \in$ GA(E)
$$such that \det \begin{pmatrix} \longrightarrow \\ f \\ the \end{pmatrix} = 1 preserve volumes. These affine maps form a subgroup SA(E) of$$
GA(E) được gọi là đặc biệt afin nhóm của $E$. Ta bây giờ lấy glimpse tại afin hình học.

## 24.9 Afin Hình học: Glimpse

Trong mục này ta phát biểu và chứng minh ba cơ bản các kết quả của afin hình học. Xấp xỉ/đại khái speaking, afin hình học là study của các tính chất bất biến dưới afin các song ánh. Ta bây giờ chứng minh một của oldest và hầu hết cơ bản các kết quả của afin hình học, định lý của Thales.

> **Mệnh đề 24.10.** Cho trước bất kỳ không gian afin (affine space) $E$, nếu $H_{1}, H_{2}, H_{3}$ là bất kỳ ba phân biệt song song các siêu phẳng, và $A$ và $B$ là bất kỳ hai các đường thẳng không song song đến $H_{i}$, đặt $a_{i} = H_{i} \cap A$ và $b_{i} = H_{i} \cap B$, thì sau đây các tỉ số là bằng nhau:
$$\frac{-\longrightarrow a_{1}a_{3}}{a_{1}a_{2}} -\longrightarrow = \frac{-\longrightarrow b_{1}b_{3}}{b_{1}b_{2}} -\longrightarrow = \rho .$$
Ngược lại, với mọi điểm $d$ trên đường thẳng $A, if_{a-\longrightarrow a}^{\longrightarrow a1d} = \rho$, thì $d = a_{3}$.
$$\overline{1}\overline{2}$$

*Chứng minh.* Hình 24.22 minh họa định lý của Thales. Ta phác thảo chứng minh, để lại chi tiết
$$\longrightarrow$$
Như một bài tập. Vì $H_{1}, H_{2}, H_{3}$ là song song, chúng có cùng hướng $H$, siêu phẳng (hyperplane) $\longrightarrow \longrightarrow \longrightarrow$ trong $E$. Cho $u \in E -H$ là bất kỳ khác không vectơ sao cho $A = a_{1}+\mathbb{R} u$. Vì $A$ là không song song đến
$$\longrightarrow  \longrightarrow  \longrightarrow$$
$H$, ta có $E = H \oplus \mathbb{R} u$, và do đó ta có thể định nghĩa ánh xạ tuyến tính (linear map) $p: E \to \mathbb{R} u$, phép chiếu

<!-- PAGE 844 -->
$$b1$$
$$H_{1}a1$$
$$H_{2}$$
$$a2b2$$
$$H_{3}b3$$
$$a3$$
$$AB$$
$$Figure 24.22: The theorem of Thales.$$
$$\longrightarrow$$
Trên $\mathbb{R} u$ song song đến $H$. Điều này ánh xạ tuyến tính (linear map) cảm sinh ánh xạ afin (affine map) $f$: $E \to A$, bởi định nghĩa $f$ sao cho
$$f(b_{1} + w) = a_{1} + p(w),$$
$$\longrightarrow  \longrightarrow$$
Với mọi $w \in E$. Rõ ràng, $f(b_{1}) = a_{1}$, và vì $H_{1}, H_{2}, H_{3}$ tất cả có hướng $H$, ta cũng có $f(b_{2}) = a_{2}$ và $f(b_{3}) = a_{3}$. Vì $f$ là afin, nó bảo toàn các tỉ số, và do đó
$$\frac{-\longrightarrow a_{1}a_{3}}{a_{1}a_{2}} -\longrightarrow = \frac{-\longrightarrow b_{1}b_{3}}{b_{1}b_{2}} -\longrightarrow .$$
Điều ngược lại là immediate. Ta cũng có sau đây đơn giản mệnh đề, có chứng minh là trái như dễ bài tập.

> **Mệnh đề 24.11.** Cho trước bất kỳ không gian afin (affine space) $E$, cho trước bất kỳ hai phân biệt các điểm, $b \in E$, và với mọi afin phép vị tự (dilatation) $f$ khác nhau từ đồng nhất thức, nếu ' $=$ f(), $D = \langle$, $b\rangle$ là đường thẳng chuyển qua và $b$, và D' là đường thẳng song song đến $D$ và chuyển qua ', các mệnh đề sau đây là tương đương:
$(i)$ b' $=$ f(b);
(ii) Nếu $f$ là phép tịnh tiến, thì b' là giao của D' với đường thẳng song song đến $\langle$, $a'\rangle$ chuyển qua $b$; Nếu $f$ là phép vị tự (dilatation) của tâm $c$, thì b' $=$ D' $\cap \langle c, b\rangle$.

<!-- PAGE 845 -->
Trường hợp thứ nhất là hình bình hành luật, và trường hợp thứ hai suy ra dễ dàng từ Thales’ định lý. Cho illustration, xem Hình 24.23.
$$a’ = f(a)$$
$$a$$
$$b$$
$$D’$$
$$D$$
$$a’ = f(a)a’ = f(a)$$
$$b’ = f(b)$$
$$aa$$
$$b’ = f(b)$$
$$bb$$
$$D’cD’$$
$$DD$$

![Figure 24.23](../../assets/ch24/fig_24_23.png)

**Hình 24.23:** illustration của Mệnh đề 24.11. đáy/dưới trái biểu đồ minh họa phép tịnh tiến, trong khi đáy/dưới phải minh họa trung tâm dilation qua $c$. Ta là bây giờ ready để chứng minh hai cổ điển các kết quả của afin hình học, Pappus’s định lý và Desargues’s định lý. Thực sự, các kết quả này là các định lý của xạ ảnh hình học, và ta là phát biểu afin các phiên bản của các phần tử này quan trọng các kết quả. Có mạnh hơn các phiên bản rằng là tốt nhất được chứng minh bằng cách sử dụng xạ ảnh hình học.

> **Mệnh đề 24.12.** Cho trước bất kỳ afin mặt phẳng $E$, bất kỳ hai phân biệt các đường thẳng $D$ và D', thì với mọi phân biệt các điểm, $b, c$ trên $D$ và ', b', c' trên D', nếu, $b, c$, ', b', c' là phân biệt từ giao của $D$ và D' (nếu $D$ và D' giao nhau) và nếu các đường thẳng $\langle$, $b'\rangle$ và $\langle$ ', $b\rangle$ là song song, và các đường thẳng $\langle b, c'\rangle$ và $\langle$ b', $c\rangle$ là song song, thì các đường thẳng $\langle$, $c'\rangle$ và $\langle$ ', $c\rangle$ là song song.

*Chứng minh.* Pappus’s định lý được minh họa trong Hình 24.24. Nếu $D$ và D' là không song song, cho $d$ là của chúng giao. Cho $f$ là phép vị tự (dilatation) của tâm $d$ sao cho f() $= b$, và cho $g$ là phép vị tự (dilatation) của tâm $d$ sao cho g(b) $= c$. Vì các đường thẳng $\langle$, $b'\rangle$ và $\langle$ ', $b\rangle$ là song song, và các đường thẳng $\langle b, c'\rangle$ và $\langle$ b', $c\rangle$ là song song, theo Mệnh đề 24.11 ta có ' $=$ f(b') và b' $=$ g(c'). Tuy nhiên, ta được quan sát rằng các phép vị tự với cùng tâm giao hoán, và do đó $f \circ g = g \circ f$, và do đó, đặt $h = g \circ f$, ta thu được $c =$ h() và ' $=$ h(c'). Một lần nữa, theo Mệnh đề 24.11, các đường thẳng $\langle$, $c'\rangle$ và $\langle$ ', $c\rangle$ là song song. Nếu $D$ và D' là song song, ta sử dụng các phép tịnh tiến thay vì của các phép vị tự.

<!-- PAGE 846 -->
$$c$$
$$D$$
$$b$$
$$a$$
$$c$$
$$b$$
$$D$$
$$a$$
$$Figure 24.24: Pappus’s theorem (affine version).$$
Có một điều ngược lại đến Pappus’s định lý, mà cho ta fancier phiên bản của Pappus’s định lý, nhưng nó là dễ hơn để chứng minh nó bằng cách sử dụng xạ ảnh hình học. Nó nên được lưu ý rằng trong axiomatic các trình bày của xạ ảnh hình học, Pappus’s định lý là tương đương đến tính giao hoán của ground trường $K$ (trong trình bày trường hợp, $K =\mathbb{R})$. Ta bây giờ chứng minh afin phiên bản của Desargues’s định lý.

> **Mệnh đề 24.13.** Cho trước bất kỳ không gian afin (affine space) $E$, và cho trước bất kỳ hai các tam giác (, $b, c)$ và (', b', c'), ở đâu, $b, c$, ', b', c' là tất cả phân biệt, nếu $\langle$, $b\rangle$ và $\langle$ ', $b'\rangle$ là song song và $\langle b, c\rangle$ và $\langle$ b', $c'\rangle$ là song song, thì $\langle$, $c\rangle$ và $\langle$ ', $c'\rangle$ là song song khi và chỉ khi các đường thẳng $\langle$, $a'\rangle , \langle b, b'\rangle$, và $\langle c, c'\rangle$ là hoặc song song hoặc concurrent (i.e., giao nhau trong chung/phổ biến điểm).

*Chứng minh.* Ta chứng minh một nửa của mệnh đề, hướng trong mà nó được giả sử rằng $\langle$, $c\rangle$ và $\langle$ ', $c'\rangle$ là song song, để lại điều ngược lại như một bài tập. Vì các đường thẳng $\langle$, $b\rangle$ và $\langle$ ', $b'\rangle$ là song song, các điểm, $b$, ', b' là đồng phẳng. Do đó, hoặc $\langle$, $a'\rangle$ và $\langle b, b'\rangle$ là song song, hoặc chúng có một số giao $d$. Ta xét trường hợp thứ hai ở đâu chúng giao nhau, để lại khác trường hợp như dễ bài tập. Cho $f$ là phép vị tự (dilatation) của tâm $d$ sao cho f() $=$ '. Theo Mệnh đề 24.11, ta thu được f(b) $=$ b'. Nếu f(c) $=$ c'', một lần nữa theo Mệnh đề 24.11 hai lần, các đường thẳng $\langle b, c\rangle$ và $\langle$ b', $c''\rangle$ là song song, và các đường thẳng $\langle$, $c\rangle$ và $\langle$ ', $c''\rangle$ là song song. Từ điều này suy ra rằng c'' $=$ c'. Thật vậy, nhắc lại rằng $\langle b, c\rangle$ và $\langle$ b', $c'\rangle$ là song song, và tương tự $\langle$, $c\rangle$ và $\langle$ ', $c'\rangle$ là song song. Do đó, các đường thẳng $\langle$ b', $c''\rangle$ và $\langle$ b', $c'\rangle$ là đồng nhất, và tương tự các đường thẳng
$$\longrightarrow  \longrightarrow$$
$\langle$ ', $c''\rangle$ và $\langle$ ', $c'\rangle$ là đồng nhất. Vì 'c' và b'c' là độc lập tuyến tính (linearly independent), các phần tử này các đường thẳng có duy nhất giao, mà phải là c'' $=$ c'. hướng ở đâu nó được giả sử rằng các đường thẳng $\langle$, $a'\rangle , \langle b, b'\rangle$ và $\langle c, c'\rangle$, là hoặc song song hoặc concurrent là để lại như một bài tập (thực ra, chứng minh là khá đồng dạng).
