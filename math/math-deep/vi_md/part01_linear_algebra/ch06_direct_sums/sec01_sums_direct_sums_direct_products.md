# Các tổng, Các tổng trực tiếp, Trực tiếp Các tích


<!-- PAGE 179 -->
Chương $6$ Các tổng trực tiếp Trong chương này tất cả các không gian vectơ được định nghĩa trên tùy ý trường $K$. Cho sake của concreteness, độc giả có thể safely giả sử rằng $K =\mathbb{R}$.

## 6.1 Các tổng, Các tổng trực tiếp, Trực tiếp Các tích

Có một số hữu ích các cách của tạo thành mới các không gian vectơ từ older các một, đặc biệt, trực tiếp các tích và các tổng trực tiếp. Regarding các tổng trực tiếp, có một tinh tế điểm, mà là rằng nếu ta attempt để định nghĩa tổng trực tiếp (direct sum) $E$ `F of two vector spaces using the cartesian product $E \times  F$, we don’t quite get the right notion because elements of $E \times  F$ are ordered pairs, but we want $E$ `F $= F$ `E. Thus, we want to think of the elements of $E$ `F như unordrered các cặp của các phần tử. Nó là khả dĩ/có thể đến thực hiện do đó bởi xét tổng trực tiếp (direct sum) của họ $(E_{i})_{i\in {1,2}}$, và tổng quát hơn của họ $(E_{i})_{i\in I}$. Để đơn giản, ta bắt đầu bởi xét trường hợp ở đâu $I = {1, 2}$.

> **Định nghĩa 6.1.** Cho trước họ $(E_{i})_{i\in {1,2}}$ của hai các không gian vectơ, ta định nghĩa (external)
$$E$$
Tổng trực tiếp (direct sum) $E_{1}$ ` (hoặc coproduct) của họ $(E_{i})_{i\in {1,2}}$ như tập hợp
$$2$$
$$E_{1}aE_{2} = {{\langle 1, u\rangle , \langle 2, v\rangle } | u \in E_{1}, v \in E_{2}},$$
Với phép cộng
$${\langle 1, u_{1}\rangle , \langle 2, v_{1}\rangle } + {\langle 1, u_{2}\rangle , \langle 2, v_{2}\rangle } = {\langle 1, u_{1} + u_{2}\rangle , \langle 2, v_{1} + v_{2}\rangle },$$
Và vô hướng (scalar) phép nhân
$$\lambda {\langle 1, u\rangle , \langle 2, v\rangle } = {\langle 1, \lambda u\rangle , \langle 2, \lambda v\rangle }.$$
$$E E$$
Ta định nghĩa các đơn ánh $in_{1}$: $E_{1} \to E_{1}$ `  and $in_{2}$ : $E_{2} \to E_{1}$ ` như các ánh xạ tuyến tính (linear maps)
$$22$$
Được định nghĩa sao cho,
$$in_{1}(u) = {\langle 1, u\rangle , \langle 2, 0\rangle },$$
Và
$$in_{2}(v) = {\langle 1, 0\rangle , \langle 2, v\rangle }.$$
$$179$$

<!-- PAGE 180 -->
Lưu ý rằng
$$E_{2}aE_{1} = {{\langle 2, v\rangle , \langle 1, u\rangle } | v \in E_{2}, u \in E_{1}} = E_{1}aE_{2}.$$
$$E$$
Do đó, mọi member ${\langle 1, u\rangle , \langle 2, v\rangle$ } của $E_{1}$ ` có thể được được quan điểm như unordered cặp bao gồm
$$2$$
Của hai các vectơ $u$ và $v$, tagged với chỉ số $1$ và $2$, respectively.
$$E$$
$$Remark: In fact, E_{1}`2 is just the product \prod_{i}  \in {1,2} E_{i} of the family (E_{i})_{i\in {1,2}}.$$
 Điều này là không là confused với cartesian tích $E_{1} \times E_{2}$. không gian vectơ (vector space) $E_{1} \times E_{2}$ là tập hợp tất cả được thứ tự các cặp $\langle u, v\rangle$, ở đâu $u \in E_{1}$, và $v \in E_{2}$, với phép cộng và phép nhân bởi vô hướng (scalar) được định nghĩa sao cho
$$\langle u_{1}, v_{1}\rangle + \langle u_{2}, v_{2}\rangle = \langle u_{1} + u_{2}, v_{1} + v_{2}\rangle ,$$
$$\lambda \langle u, v\rangle = \langle \lambda u, \lambda v\rangle .$$
$$There is a bijection between \prod_{i}  E_{i} and E_{1} \times  E_{2}, but as we just saw, elements of$$
$$\prod_{i}  \in { E_{i} are certain sets. The^{\in {1,2}} product E_{1} \times  \cdots  \times  E_{n} of any number of vector spaces$$
$can^{1,2}}$ cũng được định nghĩa. Ta sẽ thực hiện điều này một cách ngắn. sau đây tính chất nghiệm đúng.
$$E$$

> **Mệnh đề 6.1.** Cho trước bất kỳ hai các không gian vectơ, $E_{1}$ và $E_{2}$, tập hợp $E_{1}$ ` là không gian vectơ (vector space). Với mọi cặp của các ánh xạ tuyến tính (linear maps), $f$: $E_{1} \to G$ và $g: E_{2} \to G$, ở đó là $a^{2}$ duy nhất tuyến tính
$$E$$
Ánh xạ, $f + g: E_{1}$ ` $\to G$, sao cho $(f + g) \circ in_{1} = f$ và $(f + g) \circ in_{2} = g$, như trong sau đây $diagram:^{2}$
$$E_{1}P$$
$$PP$$
$$PP$$
$$PP$$
$$P^{f}P$$
$$inPP$$
$$1PP$$
$$EPP$$
$$P'$$
$$f+g /$$
$$E_{1}`7G$$
$$2\overline{n}\overline{n}$$
$$\overline{n}\overline{n}$$
$$nn$$
$$nn$$
$$innn_{g}$$
$$2nn$$
$$nn$$
$$nn$$
$$E_{2}$$

*Chứng minh.* Định nghĩa
$$(f + g)({\langle 1, u\rangle , \langle 2, v\rangle }) = f(u) + g(v),$$
Với mọi $u \in E_{1}$ và $v \in E_{2}$. Ta kiểm chứng được ngay rằng $f + g$ là duy nhất ánh xạ tuyến tính (linear map) với cần thiết các tính chất.
$$E$$
Ta đã được lưu ý rằng $E_{1}$ ` là trong song ánh với $E_{1} \times  E_{2}$. Nếu ta định nghĩa các phép chiếu
$$E E2$$
$\pi_{1}$: $E_{1}$ `  $\to E_{1}$ and $\pi_{2}$  : $E_{1}$ ` $\to E_{2}$, sao cho
$$22$$
$$\pi_{1} ({\langle 1, u\rangle , \langle 2, v\rangle }) = u,$$
Và
$$\pi_{2} ({\langle 1, u\rangle , \langle 2, v\rangle }) = v,$$
Ta có kết quả sau mệnh đề.

<!-- PAGE 181 -->

> **Mệnh đề 6.2.** Cho trước bất kỳ hai các không gian vectơ, $E_{1}$ và $E_{2}$, với mọi cặp của các ánh xạ tuyến tính (linear maps),
$$E$$
$f$: $D \to E_{1}$ và $g: D \to E_{2}$, tồn tại duy nhất một ánh xạ tuyến tính (linear map), $f \times  g: D \to E_{1}$ `, sao cho
$$2$$
$\pi_{1}  \circ (f \times  g) = f$ và $\pi_{2}  \circ (f \times  g) = g$, như trong sau đây biểu đồ:
$$7E_{1}$$
$$nn$$
$$nn$$
$$nn$$
$$nn$$
$$n^{f}n\pi 1$$
$$n_{f\times g}n$$
$$nn E$$
$$nn$$
$$D\overline{P} E_{1}`$$
$$\overline{P}\overline{P} 2$$
$$\overline{P}\overline{P}$$
$$PP$$
$$PP$$
$$PP\pi$$
$$gPP2$$
$$PP$$
$$P($$
$$E_{2}$$

*Chứng minh.* Định nghĩa
$$(f \times  g)(w) = {\langle 1, f(w)\rangle , \langle 2, g(w)\rangle },$$
Với mọi $w \in D$. Ta kiểm chứng được ngay rằng $f \times  g$ là duy nhất ánh xạ tuyến tính (linear map) với cần thiết các tính chất.
Nhận xét: Nó là peculiarity của tuyến tính đại số rằng các tổng trực tiếp và các tích của hữu hạn các họ là đẳng cấu. Tuy nhiên, điều này là không có dài hơn đúng cho các tích và các tổng của vô hạn các họ. Khi $U, V$ là các không gian con của không gian vectơ (vector space) $E$, đặt $i_{1}$: $U \to E$ và $i_{2}$: $V \to E$ là inclusion các ánh xạ, nếu $U$ `V is isomomorphic to $E$ under the map $i_{1} + i_{2}$ given by Proposition 6.1, we say that $E$ is a direct sum of $U$ and $V$ , and we write $E = U$ `V (với slight abuse của ký hiệu, vì $E$ và $U$ `V là chỉ đẳng cấu). Nó là cũng thuận tiện để định nghĩa tổng $U_{1} + \cdots  + U_{p}$ và internal tổng trực tiếp (direct sum) $U_{1} \oplus \cdots  \oplus U_{p}$ của bất kỳ số của các không gian con của $E$.

> **Định nghĩa 6.2.** Cho trước $p \ge 2$ các không gian vectơ $E_{1}, \dots  , E_{p}$, tích $F = E_{1} \times  \cdots  \times  E_{p}$ có thể được được tạo vào không gian vectơ (vector space) bởi định nghĩa phép cộng và vô hướng (scalar) phép nhân như sau:
$$(u_{1}, \dots  , u_{p}) + (v_{1}, \dots  , v_{p}) = (u_{1} + v_{1}, \dots  , u_{p} + v_{p})$$
$$\lambda (u_{1}, \dots  , u_{p}) = (\lambda u_{1}, \dots  , \lambda u_{p}),$$
Với mọi $u_{i}, v_{i} \in E_{i}$ và tất cả $\lambda  \in \mathbb{R}$. không vectơ của $E_{1} \times  \cdots  \times  E_{p}$ là bộ $p$
$$( 0, \dots  , 0),$$
$$| {z }$$
$$p$$
Ở đâu thứ $i$ không là không vectơ của $E_{i}$. Với ở trên phép cộng và phép nhân, không gian vectơ (vector space) $F = E_{1} \times  \cdots  \times  E_{p}$ được gọi là trực tiếp tích của các không gian vectơ $E_{1}, \dots  , E_{p}$. Như đặc biệt trường hợp, khi $E_{1} = \cdots  = E_{p} =\mathbb{R}$, ta tìm một lần nữa không gian vectơ (vector space) $F =\mathbb{R}^{p}$. phép chiếu các ánh xạ $pr_{i}$: $E_{1} \times  \cdots  \times  E_{p} \to E_{i}$ cho trước bởi
$$pr_{i}(u_{1}, \dots  , u_{p}) = u_{i}$$

<!-- PAGE 182 -->
Là rõ ràng tuyến tính. Tương tự, các ánh xạ $in_{i}$: $E_{i} \to E_{1} \times  \cdots  \times  E_{p}$ cho trước bởi
$$in_{i}(u_{i}) = (0, \dots  , 0, u_{i}, 0, \dots  , 0)$$
Là đơn ánh (injective) và tuyến tính. Nếu $dim(E_{i}) = n_{i}$ và nếu $(e_{1}^{i}, \dots  , e_{ni}^{i})$ là cơ sở (basis) của $E_{i}$ cho $i = 1, \dots  , p$, thì nó là dễ để xem rằng $n_{1} + \cdots  + n_{p}$ các vectơ
$$(e_{1}^{1}, 0, \dots  , 0),\dots  ,(e_{n1}^{1}, 0, \dots  , 0),$$
$$\vdots \vdots \vdots$$
$$(0, \dots  , 0, e_{1}^{i}, 0, \dots  , 0),\dots  ,(0, \dots  , 0, e_{ni}^{i}, 0, \dots  , 0),$$
$$\vdots \vdots \vdots$$
$$(0, \dots  , 0, e_{1}^{p}),\dots  ,(0, \dots  , 0, e_{np}^{p})$$
Tạo thành cơ sở (basis) của $E_{1} \times  \cdots  \times  E_{p}$, và do đó
$$\dim(E_{1} \times  \cdots  \times  E_{p}) = \dim(E_{1}) + \cdots  + \dim(E_{p}).$$
Cho chúng ta bây giờ xét không gian vectơ (vector space) $E$ và $p$ các không gian con $U_{1}, \dots  , U_{p}$ của $E$. Ta có ánh xạ
$$a: U_{1} \times  \cdots  \times  U_{p} \to E$$
Cho trước bởi
$$a(u_{1}, \dots  , u_{p}) = u_{1} + \cdots  + u_{p},$$
Với $u_{i} \in U_{i}$ cho $i = 1, \dots  , p$. Rõ ràng là ánh xạ này là tuyến tính, và do đó ảnh (ảnh (image)) của nó là không gian con của $E$ được ký hiệu bởi
$$U_{1} + \cdots  + U_{p}$$
Và được gọi là tổng của các không gian con $U_{1}, \dots  , U_{p}$. Theo Định nghĩa,
$$U_{1} + \cdots  + U_{p} = {u_{1} + \cdots  + u_{p} | u_{i} \in U_{i}, 1 \le i \le p},$$
Và ta kiểm chứng được ngay rằng $U_{1} + \cdots  + U_{p}$ là nhỏ nhất không gian con của $E$ chứa $U_{1}, \dots  , U_{p}$. Điều này cũng suy ra rằng $U_{1} + \cdots  + U_{p}$ không phụ thuộc vào thứ tự của các nhân tử $U_{i}$; đặc biệt,
$$U_{1} + U_{2} = U_{2} + U_{1}.$$

> **Định nghĩa 6.3.** Với mọi không gian vectơ (vector space) $E$ và bất kỳ $p \ge 2$ các không gian con $U_{1}, \dots  , U_{p}$ của $E$, nếu ánh xạ được định nghĩa ở trên là đơn ánh (injective), thì tổng $U_{1} + \cdots  + U_{p}$ được gọi là một tổng trực tiếp (direct sum) và nó được ký hiệu bởi
$$U_{1} \oplus \cdots  \oplus U_{p}.$$
Không gian $E$ là tổng trực tiếp (direct sum) của các không gian con $U_{i}$ nếu
$$E = U_{1} \oplus \cdots  \oplus U_{p}.$$

<!-- PAGE 183 -->
Như trong trường hợp của tổng, $U_{1} \oplus U_{2} = U_{2} \oplus U_{1}$. Nếu ánh xạ là đơn ánh (injective), thì theo Mệnh đề 3.19 ta có Ker $a =$ {($0, \dots  , 0)}$ ở đâu
$$| {z }$$
Mỗi $0$ là không vectơ của $E$, mà có nghĩa là nếu $u_{i} \in U_{i}$ cho $i = 1, \dots  , p and^{p}$ nếu
$$u_{1} + \cdots  + u_{p} = 0,$$
Thì $(u_{1}, \dots  , u_{p}) = (0, \dots  , 0)$, nghĩa là, $u_{1} = 0, \dots  , u_{p} = 0$.

> **Mệnh đề 6.3.** Nếu ánh xạ: $U_{1} \times \cdots \times U_{p} \to E$ là đơn ánh (injective), thì mọi $u \in U_{1} +\cdots +U_{p}$ có duy nhất biểu thức như tổng
$$u = u_{1} + \cdots  + u_{p},$$
Với $u_{i} \in U_{i}$, cho $i = 1, \dots  , p$.

*Chứng minh.* Nếu
$$u = v_{1} + \cdots  + v_{p} = w_{1} + \cdots  + w_{p},$$
Với $v_{i}, w_{i} \in U_{i}$, cho $i = 1, \dots  , p$, thì ta có
$$w_{1} -v_{1} + \cdots  + w_{p} -v_{p} = 0,$$
Và vì $v_{i}, w_{i} \in U_{i}$ và mỗi $U_{i}$ là không gian con, $w_{i} -v_{i} \in U_{i}$. tính đơn ánh của suy ra rằng $w_{i}-v_{i} = 0$, nghĩa là, $w_{i} = v_{i}$ cho $i = 1, \dots  , p$, mà chỉ ra tính duy nhất của phân rã của $u$.

> **Mệnh đề 6.4.** Nếu ánh xạ: $U_{1} \times  \cdots  \times  U_{p} \to E$ là đơn ánh (injective), thì bất kỳ $p$ khác không các vectơ $u_{1}, \dots  , u_{p}$ với $u_{i} \in U_{i}$ là độc lập tuyến tính (linearly independent).

*Chứng minh.* để xem điều này, giả sử rằng
$$\lambda_{1} u_{1} + \cdots  + \lambda_{p} u_{p} = 0$$
Với một số $\lambda_{i}  \in \mathbb{R}$. Vì $u_{i} \in U_{i}$ và $U_{i}$ là không gian con, $\lambda_{i} u_{i} \in U_{i}$, và tính đơn ánh của suy ra rằng $\lambda_{i} u_{i} = 0$, cho $i = 1, \dots  , p$. Vì $u_{i} \neq  0$, ta phải có $\lambda_{i}  = 0$ cho $i = 1, \dots  , p$; nghĩa là, $u_{1}, \dots  , u_{p}$ với $u_{i} \in U_{i}$ và $u_{i} \neq  0$ là độc lập tuyến tính (linearly independent). Nhận thấy rằng nếu là đơn ánh (injective), thì ta phải có $U_{i} \cap U_{j} = (0)$ bất cứ khi nào $i \neq  j$. Tuy nhiên,
$$\mathbb{R}^{2}$$
Điều kiện này là một cách tổng quát không đủ nếu $p \ge 3$. Ví dụ, nếu $E =$ và $U_{1}$ đường thẳng được sinh (spanned) bởi $e_{1} = (1, 0), U_{2}$ là đường thẳng được sinh (spanned) bởi $d = (1, 1)$, và $U_{3}$ là đường thẳng được sinh (spanned) bởi $e_{2} = (0, 1)$, thì $U_{1}\cap U_{2} = U_{1}\cap U_{3} = U_{2}\cap U_{3} = {(0, 0)}$, nhưng $U_{1}+U_{2} = U_{1}+U_{3} = U_{2}+U_{3} =\mathbb{R}^{2}$, do đó $U_{1} + U_{2} + U_{3}$ là không tổng trực tiếp (direct sum). Ví dụ, $d$ được biểu diễn trong hai khác nhau các cách như
$$d = (1, 1) = (1, 0) + (0, 1) = e_{1} + e_{2}.$$

<!-- PAGE 184 -->
Xem Hình 6.1.
$$U3U$$
$$2$$
$$e(1,1)$$
$$2$$
$$\overline{e1} U1$$
$$Figure 6.1: The linear subspaces U_{1}, U_{2}, and U_{3} illustrated as lines in \mathbb{R}^{2}.$$
Như trong trường hợp của tổng, $U_{1} \oplus U_{2} = U_{2} \oplus U_{1}$. Nhận thấy rằng khi ánh xạ là đơn ánh (injective), thì nó là tuyến tính đẳng cấu giữa $U_{1} \times  \cdots  \times  U_{p}$ và $U_{1} \oplus \cdots  \oplus U_{p}$. difference là rằng $U_{1} \times  \cdots  \times  U_{p}$ được định nghĩa chẵn/ngay cả nếu các không gian $U_{i}$ là không được giả sử là các không gian con của một số chung/phổ biến không gian. Nếu $E$ là tổng trực tiếp (direct sum) $E = U_{1} \oplus \cdots \oplus U_{p}$, vì bất kỳ $p$ khác không các vectơ $u_{1}, \dots  , u_{p}$ với $u_{i} \in U_{i}$ là độc lập tuyến tính (linearly independent), nếu ta chọn cơ sở (basis) $(u_{k})_{k\in Ij}$ trong $U_{j}$ cho $j = 1, \dots  , p$, thì $(u_{i})_{i\in I}$ với $I = I_{1} \cup \cdots  \cup I_{p}$ là cơ sở (basis) của $E$. Một cách trực quan, $E$ là split vào $p$ độc lập các không gian con. Ngược lại, cho trước cơ sở (basis) $(u_{i})_{i\in I}$ của $E$, nếu ta phân hoạch chỉ số tập hợp $I$ như $I = I_{1} \cup \cdots  \cup I_{p}$, thì mỗi họ con $(u_{k})_{k\in Ij}$ sinh ra một số không gian con $U_{j}$ của $E$, và ta kiểm chứng được ngay rằng ta có tổng trực tiếp (direct sum)
$$E = U_{1} \oplus \cdots  \oplus U_{p}.$$

> **Định nghĩa 6.4.** Cho $f$: $E \to E$ là ánh xạ tuyến tính (linear map). Với mọi không gian con $U$ của $E$, nếu f(U) $\subseteq U$ ta nói rằng $U$ là bất biến dưới $f$. Giả sử rằng $E$ là hữu hạn chiều, tổng trực tiếp (direct sum) $E = U_{1} \oplus \cdots  \oplus U_{p}$, và rằng mỗi $U_{j}$ là bất biến dưới $f$. Nếu ta chọn cơ sở (basis) $(u_{i})_{i\in I}$ như ở trên với $I = I_{1} \cup \cdots  \cup I_{p}$ và với mỗi $(u_{k})_{k\in Ij}$ cơ sở (basis) của $U_{j}$, vì mỗi $U_{j}$ là bất biến dưới $f$, ảnh (image) $f(u_{k})$ của mọi cơ sở (basis) vectơ $u_{k}$ với $k \in I_{j}$ thuộc đến $U_{j}$, do đó ma trận $A$ biểu diễn $f$ trên cơ sở (basis) $(u_{i})_{i\in I}$ là khối ma trận đường chéo (diagonal matrix) của tạo thành
$$A = \begin{pmatrix} A_{1} \\ A_{2} \\ \ddots \\ A_{p} \end{pmatrix} ,$$

<!-- PAGE 185 -->
Với mỗi khối $A_{j}$ $d_{j} \times  d_{j}-matrix$ với $d_{j} = dim(U_{j})$ và tất cả khác các phần tử (entries) bằng $0$. Nếu $d_{j} = 1$ cho $j = 1, \dots  , p$, ma trận $A$ là ma trận đường chéo (diagonal matrix). Có tự nhiên các đơn ánh từ mỗi $U_{i}$ đến $E$ được ký hiệu bởi $in_{i}$: $U_{i} \to E$. Bây giờ, nếu $p = 2$, nó là dễ để xác định hạt nhân (kernel) của ánh xạ: $U_{1} \times  U_{2} \to E$. Ta có
$$a(u_{1}, u_{2}) = u_{1} + u_{2} = 0iffu_{1} = -u_{2}, u_{1} \in U_{1}, u_{2} \in U_{2},$$
Mà suy ra rằng
$$\mathrm{Ker} a = {(u, -u) | u \in U_{1} \cap U_{2}}.$$
Bây giờ, $U_{1} \cap U_{2}$ là không gian con của $E$ và ánh xạ tuyến tính (linear map) $u \mapsto (u, -u)$ là rõ ràng đẳng cấu giữa $U_{1} \cap U_{2}$ và Ker, do đó Ker là đẳng cấu đến $U_{1} \cap U_{2}$. Hệ quả là, ta thu được kết quả sau đây:

> **Mệnh đề 6.5.** Cho trước bất kỳ không gian vectơ (vector space) $E$ và bất kỳ hai các không gian con $U_{1}$ và $U_{2}$, tổng $U_{1} + U_{2}$ là tổng trực tiếp (direct sum) khi và chỉ khi $U_{1} \cap U_{2} = (0)$. thú vị illustration của khái niệm của tổng trực tiếp (direct sum) là phân rã của ma trận vuông (square matrix) vào của nó đối xứng phần và của nó phản đối xứng phần. Nhắc lại rằng một ma trận cỡ $n \times  n$ $A \in M_{n}$ là đối xứng nếu $A^{\top} = A$, skew -đối xứng nếu $A^{\top} = -A$. Rõ ràng là $s$
$$S(n) = {A \in M_{n} | A^{\top}= A}andSkew(n) = {A \in M_{n} | A^{\top}= -A}$$
Là các không gian con của $M_{n}$, và rằng S(n) $\cap$ Skew(n) $= (0)$. Nhận thấy rằng với mọi ma trận $A \in M_{n}$, ma trận H() $= (A + A^{\top})/2$ là đối xứng và ma trận S() $= (A$ - $A^{\top})/2$ là skewsymmetric. Vì
$$A = H(A) + S(A) = \frac{A + A^{\top}}{2} + \frac{AA^{\top}}{2} -,$$
Ta xem rằng $M_{n} = S(n)+Skew(n)$, và vì $S(n)\cap$ Skew(n) $= (0)$, ta có tổng trực tiếp (direct sum)
$$M_{n} = S(n) \oplus Skew(n).$$
Nhận xét: không gian vectơ (vector space) Skew(n) của các ma trận phản đối xứng cũng được ký hiệu bởi $\mathfrak{so}(n)$. Nó là Lie đại số của nhóm Do đó(n). Mệnh đề 6.5 có thể được suy rộng/tổng quát hóa đến bất kỳ $p \ge 2$ các không gian con tại expense của ký hiệu. chứng minh của sau đây mệnh đề là để lại như một bài tập.

> **Mệnh đề 6.6.** Cho trước bất kỳ không gian vectơ (vector space) $E$ và bất kỳ $p \ge 2$ các không gian con $U_{1}, \dots  , U_{p}$, các tính chất sau đây là tương đương:
$(1)$ tổng $U_{1} + \cdots  + U_{p}$ là tổng trực tiếp (direct sum).

<!-- PAGE 186 -->
$(2)$ Ta có
$$U_{i} \cap \begin{pmatrix} U_{j} \\ i \end{pmatrix} \sum_{j=1,j\neq}^{p}  = (0),i = 1, \dots  , p.$$
$(3)$ Ta có
$$U_{i} \cap \begin{pmatrix} U_{j} \end{pmatrix} \sum_{j=1}^{i-1}  = (0),i = 2, \dots  , p.$$
Bởi vì của đẳng cấu
$$U_{1} \times  \cdots  \times  U_{p} \approx U_{1} \oplus \cdots  \oplus U_{p},$$
Ta có

> **Mệnh đề 6.7.** Nếu $E$ là bất kỳ không gian vectơ (vector space), với mọi (hữu hạn chiều) các không gian con $U_{1}, \dots , U_{p}$ của $E$, ta có
$$\dim(U_{1} \oplus \cdots  \oplus U_{p}) = \dim(U_{1}) + \cdots  + \dim(U_{p}).$$
Nếu $E$ là tổng trực tiếp (direct sum)
$$E = U_{1} \oplus \cdots  \oplus U_{p},$$
Vì mọi $u \in E$ có thể được được viết trong duy nhất cách như
$$u = u_{1} + \cdots  + u_{p}$$
Với $u_{i} \in U_{i}$ cho $i = 1 \dots  , p$, ta có thể định nghĩa các ánh xạ $\pi_{i}$: $E \to U_{i}$, được gọi là các phép chiếu, bởi
$$\pi_{i} (u) = \pi_{i} (u_{1} + \cdots  + u_{p}) = u_{i}.$$
Nó là dễ để kiểm tra rằng các ánh xạ này là tuyến tính và thỏa mãn các tính chất sau đây:
$$($$
$$\pi_{i} if i = j$$
$$\pi_{j}  \circ \pi_{i}  =$$
$$0if i \neq  j,$$
$$\pi_{1}  + \cdots  + \pi_{p}  = id_{E}.$$
Ví dụ, trong trường hợp của tổng trực tiếp (direct sum)
$$M_{n} = S(n) \oplus Skew(n),$$
Phép chiếu lên S(n) được cho bởi
$$\pi_{1} (A) = H(A) = \frac{A + A^{\top}}{2} ,$$

<!-- PAGE 187 -->
Và phép chiếu lên Skew(n) được cho bởi
$$\pi_{2} (A) = S(A) = \frac{AA^{\top}}{2} -.$$
Rõ ràng, $H(A)+S(A) = A$, H(H()) $=$ H(), S(S()) $=$ S(), và H(S()) $=$ S(H()) $= 0$. hàm $f$ sao cho $f \circ f = f$ được nói là lũy đẳng (idempotent). Do đó, các phép chiếu $\pi_{i}$ là lũy đẳng (idempotent). Ngược lại, sau đây mệnh đề có thể được được hiển thị:

> **Mệnh đề 6.8.** Cho $E$ là không gian vectơ (vector space). Với mọi $p \ge 2$ các ánh xạ tuyến tính (linear maps) $f_{i}$: $E \to E$, nếu
$$($$
$$f_{i}if i = j$$
$$f_{j} \circ f_{i} =$$
$$0if i \neq  j,$$
$$f_{1} + \cdots  + f_{p} = id_{E},$$
Thì nếu ta cho $U_{i} = f_{i}(E)$, ta có tổng trực tiếp (direct sum)
$$E = U_{1} \oplus \cdots  \oplus U_{p}.$$
Ta cũng có sau đây mệnh đề đặc trưng hóa lũy đẳng (idempotent) các ánh xạ tuyến tính (linear maps) có chứng minh là cũng để lại như một bài tập.

> **Mệnh đề 6.9.** Với mọi không gian vectơ (vector space) $E$, nếu $f$: $E \to E$ là lũy đẳng (idempotent) ánh xạ tuyến tính (linear map), i.e., $f \circ f = f$, thì ta có tổng trực tiếp (direct sum)
$$E = \mathrm{Ker} f \oplus \mathrm{Im} f,$$
Sao cho $f$ là phép chiếu lên ảnh (ảnh (image)) của nó Im $f$. Ta bây giờ cho định nghĩa của tổng trực tiếp (direct sum) với mọi tùy ý khác rỗng chỉ số tập hợp $I$. Thứ nhất, cho chúng ta nhắc lại khái niệm của tích của họ $(E )_{\in I}$. Cho trước họ của các tập hợp $(E_{i})_{i\in I}$, của nó
$$product \prod_{i}  E_{i}, is the set of all functions f : I \to \bigcup_{i}^{ii}  E_{i}, such that, f(i) \in E_{i}, for every$$
$i \in$ I. Nó $is^{\in I}$ một của nhiều các phiên bản của axiom $of^{\in I}$ lựa chọn, rằng, nếu $E_{i} \neq  \emptyset$ với mọi $i \in$ I,
$$then \prod_{i}  E_{i} \neq  \emptyset . A member f \in \prod_{ii}  E_{i}, is often denoted as (f_{i})_{i\in I}. For every i \in I, we$$
$$have the^{\in I} projection \pi_{i}  : \prod_{i}  \in I E_{i} \to E^{\in I}, defined such that, \pi_{i} ((f_{i})_{i\in I}) = f_{i}. We now define$$
Các tổng trực tiếp.

> **Định nghĩa 6.5.** Cho I là bất kỳ khác rỗng tập hợp, và cho $(E_{i})_{i\in I}$ là họ của các không gian vectơ. (external) tổng trực tiếp (direct sum) ` $E$ (hoặc coproduct) của họ $(E_{i})_{i\in I}$ được định nghĩa như sau:
$$i\in$$
$$`i\in I E_{i} consists of all f \in \prod_{i}^{Ii}  E_{i}, which have finite support, and addition and multi-$$
Plication bởi vô hướng (scalar) là $defined^{\in I}$ như sau:
$$(f_{i})_{i\in I} + (g_{i})_{i\in I} = (f_{i} + g_{i})_{i\in I},$$
$$\lambda (f_{i})_{i\in I} = (\lambda f_{i})_{i\in I}.$$
Ta cũng có đơn ánh các ánh xạ $in_{i}$: $E_{i} \to$ ` $E_{i}$, được định nghĩa sao cho, $in_{i}(x) = (f_{i})_{i\in I}$, ở đâu
$$i\in I$$
$f_{i} = x$, và $f_{j} = 0$, với mọi $j \in$ (I $-{i})$.

<!-- PAGE 188 -->
Sau đây mệnh đề là hiển nhiên tổng quát hóa của Mệnh đề 6.1.

> **Mệnh đề 6.10.** Cho I là bất kỳ khác rỗng tập hợp, cho $(E_{i})_{i\in I}$ là họ của các không gian vectơ, và cho $G$ là bất kỳ không gian vectơ (vector space). tổng trực tiếp (direct sum) ` $E_{i}$ là không gian vectơ (vector space), và với mọi họ $(h_{i})_{i\in I}$ của các ánh xạ tuyến tính (linear maps) $h_{i}$: $E_{i} \to G$, ở đó là $a^{i\in I}$ duy nhất ánh xạ tuyến tính (linear map)
$$\begin{pmatrix} h_{i} \end{pmatrix} \sum_{i\in I}  :aE_{i} \to G,$$
$$i\in I$$
$$such that, ( \sum_{i}  \in I h_{i}) \circ in_{i} = h_{i}, for every i \in I.$$
Các nhận xét:
$(1)$ Một có thể tự hỏi tại sao tổng trực tiếp (direct sum) ` $E_{i}$ bao gồm của familes của hữu hạn hỗ trợ/giá (support)
$$i\in$$
Thay vì của tùy ý các họ; trong khác $words,^{I}$ tại sao didn’t ta định nghĩa tổng trực tiếp (direct sum) của
$$the family (E_{i})_{i\in I} as \prod_{i}  E_{i}? The product space \prod_{i}  E_{i} with addition and scalar$$
Phép nhân được định nghĩa $as^{\in I}$ ở trên là cũng vectơ $space^{\in I}$ nhưng bài toán là rằng bất kỳ
$$linear map bh: \prod_{i}  \in I E_{i} \to G such that bh \circ in = h_{i} for all \in I must be given by$$
$$bh((u_{i})_{\in I}) = \sum_{i\in I}^{i}  h_{i}(u_{i}),$$
Và nếu I là vô hạn, tổng trên vế phải là vô hạn, và do đó undefined! Nếu I
$$is finite then \prod_{i}  \in I E_{i} and `i\in I E_{i} are isomorphic.$$
$(2)$ Khi $E_{i} = E$, với mọi $i \in$ I, ta ký hiệu ` $E_{i}$ bởi $E^{(I)}$. Đặc biệt, khi $E_{i} = K$, với mọi $i \in$ I, ta tìm không gian vectơ (vector space) $K^{(I)i\in I}of$ Định nghĩa 3.11. Ta cũng có sau đây cơ bản mệnh đề về đơn ánh (injective) hoặc toàn ánh (surjective) các ánh xạ tuyến tính (linear maps).

> **Mệnh đề 6.11.** Cho $E$ và $F$ là các không gian vectơ, và cho $f$: $E \to F$ là ánh xạ tuyến tính (linear map). Nếu $f$: $E \to F$ là đơn ánh (injective), thì có một toàn ánh (surjective) ánh xạ tuyến tính (linear map) $r: F \to E$ được gọi là phép co rút (retraction), sao cho $r \circ f = id_{E}$. Xem Hình 6.2. Nếu $f$: $E \to F$ là toàn ánh (surjective), thì có một đơn ánh (injective) ánh xạ tuyến tính (linear map) $s: F \to E$ được gọi là mục, sao cho $f \circ s = id_{F}$. Xem Hình 6.3.

*Chứng minh.* Cho $(u_{i})_{i\in I}$ là cơ sở (basis) của $E$. Vì $f$: $E \to F$ là đơn ánh (injective) ánh xạ tuyến tính (linear map), theo Mệnh đề 3.20, $(f(u_{i}))_{i\in I}$ là độc lập tuyến tính (linearly independent) trong $F$. Theo Định lý 3.8, có một cơ sở (basis) $(v_{j})_{j\in J}$ của $F$, ở đâu $I \subseteq J$, và ở đâu $v_{i} = f(u_{i})$, với mọi $i \in$ I. Theo Mệnh đề 3.20, ánh xạ tuyến tính (linear map) $r: F \to E$ có thể được được định nghĩa sao cho $r(v_{i}) = u_{i}$, với mọi $i \in$ I, và $r(v_{j}) = w$ với mọi $j \in (J$ - I), ở đâu $w$ là bất kỳ cho trước vectơ trong $E$, nói $w = 0$. Vì $r(f(u_{i})) = u_{i}$ với mọi $i \in$ I, theo Mệnh đề 3.20, ta có $r \circ f = id_{E}$. Bây giờ, giả sử rằng $f$: $E \to F$ là toàn ánh (surjective). Cho $(v_{j})_{j\in J}$ là cơ sở (basis) của $F$. Vì $f$: $E \to F$ là toàn ánh (surjective), với mọi $v_{j} \in F$, tồn tại một $u_{j} \in E$ sao cho $f(u_{j}) = v_{j}$. Vì $(v_{j})_{j\in J}$ là cơ sở (basis) của $F$, theo Mệnh đề 3.20, tồn tại duy nhất một ánh xạ tuyến tính (linear map) $s: F \to E$ sao cho $s(v_{j}) = u_{j}$. Cũng, vì $f(s(v_{j})) = v_{j}$, theo Mệnh đề 3.20 (một lần nữa), ta phải có $f \circ s = id_{F}$. điều ngược lại của Mệnh đề 6.11 là hiển nhiên.
