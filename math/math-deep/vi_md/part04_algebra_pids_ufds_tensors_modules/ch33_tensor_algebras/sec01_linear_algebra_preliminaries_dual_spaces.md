# Tuyến tính Đại số Kiến thức chuẩn bị: Đối ngẫu (dual) Các không gian và Pairings


<!-- PAGE 1168 -->

## 33.1 Tuyến tính Đại số Kiến thức chuẩn bị: Đối ngẫu (dual) Các không gian và

$$Pairings$$
Ta giả sử rằng ta là dealing với các không gian vectơ trên trường $K$. Như thông thường không gian đối ngẫu (dual space) $E^{*}$ của không gian vectơ (vector space) $E$ được định nghĩa bởi $E^{*} =$ Hom(E, $K)$. không gian đối ngẫu (dual space) $E^{*}$ là không gian vectơ (vector space) bao gồm của tất cả các ánh xạ tuyến tính (linear maps) $\omega$: $E \to K$ với các giá trị trong trường $K$. bài toán rằng đến lên thường là đến decide khi không gian $E$ là đẳng cấu đến đối ngẫu (dual) $F^{*}$ của một số khác không gian $F$ (có thể bằng $E)$. khái niệm của cặp do Pontrjagin cung cấp rất gọn gàng tiêu chuẩn.

> **Định nghĩa 33.1.** Cho trước hai các không gian vectơ $E$ và $F$ trên trường $K$, ánh xạ $\langle$ -, $-\rangle$: $E\times F \to K$ là không suy biến cặp khi và chỉ khi nó là song tuyến tính và khi và chỉ khi $\langle u, v\rangle = 0$ với mọi $v \in F$ suy ra $u = 0$, và $\langle u, v\rangle = 0$ với mọi $u \in E$ suy ra $v = 0$. không suy biến cặp cảm sinh hai các ánh xạ tuyến tính (linear maps) $\phi$: $E \to F^{*}$ và $\psi$: $F \to E^{*}$ được định nghĩa sao cho với mọi với mọi $u \in E$ và tất cả $v \in F, \phi (u)$ là dạng tuyến tính (linear form) trong $F^{*}$ và $\psi (v)$ là dạng tuyến tính (linear form) trong $E^{*}$ cho trước bởi
$$\phi (u)(y) = \langle u, y\rangle for all y \in F$$
$$\psi (v)(x) = \langle x, v\rangle for all x \in E.$$
Schematically, $\phi (u) = \langle u, -\rangle$ và $\psi (v) = \langle$ -, $v\rangle$.

> **Mệnh đề 33.1.** Với mọi không suy biến cặp $\langle$ -, $-\rangle$: $E \times F \to K$, được cảm sinh các ánh xạ $\phi$: $E \to F^{*}$ và $\psi$: $F \to E^{*}$ là tuyến tính và đơn ánh (injective). Hơn nữa, nếu $E$ và $F$ là hữu hạn dimensional, thì $\phi$: $E \to F^{*}$ và $\psi$: $F \to E^{*}$ là song ánh (bijective).

*Chứng minh.* các ánh xạ $\phi$: $E \to F^{*}$ và $\psi$: $F \to E^{*}$ là tuyến tính bởi vì $u, v \mapsto \langle u, v\rangle$ là song tuyến tính. Giả sử rằng $\phi (u) = 0$. Điều này có nghĩa là $\phi$ (u)(y) $= \langle u, y\rangle = 0$ với mọi $y \in F$, và như của ta cặp là không suy biến, ta phải có $u = 0$. Tương tự, $\psi$ là đơn ánh (injective). Nếu $E$ và $F$ là hữu hạn dimensional, thì dim(E) $= dim(E^{*})$ và dim(F) $= dim(F^{*}$). Tuy nhiên, tính đơn ánh của $\phi$ và $\psi$ suy ra rằng rằng dim(E) $\le dim(F^{*}$) và dim(F) $\le dim(E^{*})$. Hệ quả là dim(E) $\le$ dim(F) và dim(F) $\le$ dim(E), do đó dim(E) $=$ dim(F). Vì vậy, dim(E) $= dim(F^{*}$) và $\phi$ là song ánh (bijective) (và tương tự dim(F) $= dim(E^{*})$ và $\psi$ là song ánh (bijective)). Mệnh đề 33.1 chỉ ra rằng khi $E$ và $F$ là hữu hạn dimensional, không suy biến cặp cảm sinh chính tắc các đẳng cấu $\phi$: $E \to F^{*}$ và $\psi$: $F \to E^{*}$; nghĩa là, các đẳng cấu rằng không phụ thuộc vào lựa chọn của các cơ sở. quan trọng đặc biệt trường hợp là trường hợp ở đâu $E = F$ và ta có tích vô hướng (inner product) (đối xứng, xác định dương (positive definite) dạng song tuyến tính (bilinear form)) trên $E$.
Nhận xét: Khi ta sử dụng số hạng “chính tắc đẳng cấu,” ta có nghĩa rằng như vậy đẳng cấu được định nghĩa một cách độc lập của bất kỳ lựa chọn của các cơ sở. Ví dụ, nếu $E$ là hữu hạn dimensional không gian vectơ (vector space) và $(e_{1}, \dots  , e_{n})$ là bất kỳ cơ sở (basis) của $E$, ta có đối ngẫu (dual) cơ sở (basis) $(e_{1}^{*}, \dots  , e_{n}^{*})$ của $E^{*}$ (ở đâu, $e_{i}^{*} (e_{j}) = \delta_{i j}$), và do đó ánh xạ $e_{i} \mapsto e_{i}^{*}$ là đẳng cấu giữa $E$ và $E^{*}$. đẳng cấu này là không chính tắc.

<!-- PAGE 1169 -->
Mặt khác, có hai quan trọng các trường hợp ở đâu ta có chính tắc các đẳng cấu cho không gian vectơ (vector space) $E$ của hữu hạn số chiều.
$(1)$ cặp $\langle$ -, $-\rangle$: $E^{*} \times  E \to K$ cho trước bởi
$$\langle \omega , u\rangle = \omega (u),\omega  \in E^{*}, u \in E,$$
Cụ thể là việc tính giá trị tại $u$. Điều này cặp cảm sinh đẳng cấu $\psi$: $E \to E^{**}$ cho trước bởi
$$\psi (u)(\omega ) = \langle \omega , u\rangle = \omega (u),\omega  \in E^{*}, u \in E.$$

> **Định nghĩa 33.2.** ánh xạ song tuyến tính (bilinear map) eval: $E^{*}\times E \to K$, cũng được ký hiệu $\delta_{1}^{1}$: $E^{*}\times E \to K$, cho trước bởi
$$eval(\omega , u) = \delta_{1}^{1} (\omega , u) = \omega (u),\omega  \in E^{*}, u \in E,$$
Là việc tính giá trị ánh xạ hoặc Kronecker delta, và với mọi $u \in E$, dạng tuyến tính (linear form) $eval_{u} \in E^{**}$ được cho bởi
$$eval_{u}(\omega ) = eval(\omega , u) = \omega (u),\omega  \in E^{*}.(eval)$$
Do đó, ta xem rằng rằng đẳng cấu $\psi$: $E \to E^{**}$ được cho bởi
$$\psi (u) = eval_{u},u \in E.$$
$(2)$ Nếu $\langle$ -, $-\rangle$ là tích vô hướng (inner product) trên thực không gian vectơ (vector space) $E$, thì Mệnh đề 33.1 chỉ ra rằng không suy biến cặp $\langle$ -, $-\rangle$ trên $E\times E$ cảm sinh chính tắc đẳng cấu giữa $E$ và $E^{*}$. đẳng cấu này là thường được ký hiệu $\flat$: $E \to E^{*}$, và ta thường viết $u^{\flat}$ cho $\flat (u)$, với $u \in E$. Schematically, $u^{\flat} = \langle u, -\rangle$. nghịch đảo của $\flat$ được ký hiệu là $\sharp$: $E^{*} \to E$, và cho trước bất kỳ dạng tuyến tính (linear form) $\omega  \in E^{*}$, ta thường viết $\omega^{\sharp}$ cho $\sharp (\omega$). Schematically, $\omega  = \langle \omega^{\sharp} , -\rangle$. Cho trước bất kỳ cơ sở (basis), $(e_{1}, \dots  , e_{n})$ của $E$ (không nhất thiết trực chuẩn), cho $(g_{ij})$ là $n \times$ n- ma trận cho trước bởi $g_{ij} = \langle e_{i}, e_{j}\rangle$ (Gram ma trận của tích vô hướng (inner product)). Nhắc lại rằng đối ngẫu (dual) cơ sở (basis) $(e_{1}^{*}, \dots  , e_{n}^{*})$ của $E^{*}$ bao gồm của tọa độ các dạng $e_{i}^{*} \in E^{*}$, mà được đặc trưng hóa bởi các tính chất sau đây:
$$e_{i}^{*} (e_{j}) = \delta_{ij} ,1 \le i, j \le n.$$
Nghịch đảo của Gram ma trận $(g_{ij})$ là thường được ký hiệu bởi $(g^{ij})$ (bởi raising các chỉ số). tradition của raising và thấp hơn các chỉ số là pervasive trong literature trên các tenxơ. Nó là thật vậy hữu ích đến có một số notational quy ước đến distinguish giữa các vectơ và các dạng tuyến tính (cũng được gọi là one-forms hoặc covectors). thông thường quy ước là rằng các tọa độ
$$of vectors are written using superscripts, as in u = \sum_{i}  n=1 u^{i}e_{i}, and coordinates of one-forms$$
$$are written using subscripts, as in \omega  = \sum_{i}  n=1 \omega_{i} e_{i}^{*} . Actually, since vectors are indexed with$$
Các chỉ số dưới, one-forms được chỉ số với các chỉ số trên, do đó $e_{i}^{*}$ nên được viết như $e^{i}$. motivation là rằng phép lấy tổng các dấu có thể thì được bỏ qua, theo Einstein phép lấy tổng quy ước. Theo điều này quy ước, bất cứ khi nào phép lấy tổng biến (như vậy

<!-- PAGE 1170 -->
Như $i)$ xuất hiện cả hai như chỉ số dưới và superscript trong biểu thức, nó được giả sử rằng nó là
$$involved in a summation. For example the sum \sum_{i}  n=1 u^{i}e_{i} is abbreviated as$$
$$u^{i}e_{i},$$
$$n$$
$$and the sum \sum_{i}  =1 \omega_{i} e^{i}is abbreviated as$$
$$\omega_{i} e^{i}.$$
Trong điều này văn bản ta sẽ typically chỉ sử dụng Einstein phép lấy tổng quy ước cho các tenxơ. các ánh xạ $\flat$ và $\sharp$ có thể được được mô tả một cách tường minh theo Gram ma trận của tích vô hướng (inner product) và nghịch đảo của nó.

> **Mệnh đề 33.2.** Với mọi thực không gian vectơ (vector space) $E$, cho trước cơ sở (basis) $(e_{1}, \dots  , e_{n})$ cho $E$ và đối ngẫu (đối ngẫu (dual)) của nó cơ sở (basis) $(e_{1}^{*}, \dots  , e_{n}^{*})$ cho $E^{*}$, với mọi tích vô hướng (inner product) $\langle$ -, $-\rangle$ trên $E$, nếu $(g$) là của nó Gram ma trận, với
$$g_{ij} = \langle e_{i}, e_{j}\rangle , and (g^{ij}) is its inverse, then for every vector u = \sum_{j}^{ij}  n=1 u^{j}e_{j} \in E and every$$
$$one-form \omega  = \sum_{i}  n=1 \omega_{i} e_{i}^{*} \in E^{*}, we have$$
$$u^{\flat}= \sum_{i=1}^{n}  (u^{\flat})_{i}e_{i}^{*} ,with(u^{\flat})_{i} = \sum_{j=1}^{n}  g_{ij}u^{j},$$
Và
$$\omega^{\sharp} = \sum_{i=1}^{n}  (\omega^{\sharp} )^{i}e_{i},with(\omega^{\sharp} )^{i}= \sum_{j=1}^{n}  g^{ij}\omega_{j} .$$
$$Proof. For every u = \sum_{j}  n=1 u^{j}e_{j}, since u^{\flat}(v) = \langle u, v\rangle for all v \in E and the Gram matrix is$$
Đối xứng, ta có
$$u^{\flat}(e_{i}) = \langle u, e_{i}\rangle = \sum_{j=1}^{n}  u^{j}e_{j}, e_{i}= \sum_{j=1}^{n}  u^{j}\langle e_{j}, e_{i}\rangle = \sum_{j=1}^{n}  g_{ij}u^{j},$$
Do đó ta thu được
$$u^{\flat}= \sum_{i=1}^{n}  (u^{\flat})_{i}e_{i}^{*} ,with(u^{\flat})_{i} = \sum_{j=1}^{n}  g_{ij}u^{j}.$$
$$If we write \omega  \in E^{*}as \omega  = \sum_{i}  n=1 \omega_{i} e_{i}^{*} and \omega^{\sharp} \in E as \omega^{\sharp} = \sum_{\sharp}  nj=1(\omega^{\sharp} )^{j}e_{j}, since$$
$$\omega_{i}  = \omega (e_{i}) = \langle \omega^{\sharp} , e_{i}\rangle = \sum_{j=1}^{n}  (\omega^{\sharp} )^{j}g_{ij} = \sum_{j=1}^{n}  g_{ij}(\omega )^{j},1 \le i \le n,$$
Ta thu được
$$(\omega^{\sharp} )^{i} = \sum_{j=1}^{n}  g^{ij}\omega_{j} ,$$
Ở đâu $(g^{ij})$ là nghịch đảo của ma trận $(g_{ij})$.

<!-- PAGE 1171 -->
Trong trường hợp đặc biệt khi $(e_{1}, \dots  , e_{n})$ là cơ sở trực chuẩn (orthonormal basis), Gram ma trận là ma trận đơn vị (identity matrix), do đó $(u^{\flat})_{i} = u^{i}$ và $(\omega^{\sharp} )^{i} = \omega_{i}$, do đó ánh xạ $\flat$ có effect của thấp hơn (flattening!) các chỉ số, và ánh xạ $\sharp$ có effect của raising (sharpening!) các chỉ số. Ở đây là tường minh ví dụ của Mệnh đề 33.2. Cho $(e_{1}, e_{2})$ là cơ sở (basis) của $E$ sao cho
$$\langle e_{1}, e_{1}\rangle = 1,\langle e_{1}, e_{2}\rangle = 2,\langle e_{2}, e_{2}\rangle = 5.$$
Thì
$$g = \begin{pmatrix} 1 & 2 \\ 2 & 5 \end{pmatrix} ,g^{-1}= \begin{pmatrix} 5 & -2 \\ -2 & 1 \end{pmatrix} .$$
Tập hợp $u = u^{1}e_{1} + u^{2}e_{2}$ và nhận thấy rằng
$$u^{\flat}(e_{1}) = \langle u^{1}e_{1} + u^{2}e_{2}, e_{1}\rangle = \langle e_{1}, e_{1}\rangle u^{1}+ \langle e_{2}, e_{1}\rangle u^{2}= g_{11}u^{1}+ g_{12}u^{2}= u^{1}+ 2u^{2}$$
$$u^{\flat}(e_{2}) = \langle u^{1}e_{1} + u^{2}e_{2}, e_{2}\rangle = \langle e_{1}, e_{2}\rangle u^{1}+ \langle e_{2}, e_{2}\rangle u^{2}= g_{21}u^{1}+ g_{22}u^{2}= 2u^{1}+ 5u^{2},$$
Mà trong turn suy ra rằng
$$+ 2 + 5$$
$$u^{\flat}= u^{\flat}(e_{1})e_{1}^{*} + u^{\flat}(e_{2})e_{2}^{*} = (u^{1}u^{2})e_{1}^{*} + (2u^{1}u^{2})e_{2}^{*}.$$
Cho trước $\omega  = \omega_{1} e_{1}^{*} + \omega_{2} e_{2}^{*}$, ta tính toán $\omega^{\sharp} = (\omega^{\sharp} )^{1}e_{1} + (\omega^{\sharp} )^{2}e_{2}$ từ sau đây hai tuyến tính các đẳng thức:
$$\omega_{1}  = \omega (e_{1}) = \langle \omega^{\sharp} , e_{1}\rangle = \langle (\omega^{\sharp} )^{1}e_{1} + (\omega^{\sharp} )^{2}e_{2}, e_{1}\rangle$$
$$= \langle e_{1}, e_{1}\rangle (\omega^{\sharp} )^{1}+ \langle e_{2}, e_{1}\rangle (\omega^{\sharp} )^{2}= (\omega^{\sharp} )^{1}+ 2(\omega^{\sharp} )^{2}= g_{11}(\omega^{\sharp} )^{1}+ g_{12}(\omega^{\sharp} )^{2}$$
$$\omega_{2}  = \omega (e_{2}) = \langle \omega^{\sharp} , e_{2}\rangle = \langle (\omega^{\sharp} )^{1}e_{1} + (\omega^{\sharp} )^{2}e_{2}, e_{2}\rangle$$
$$= \langle e_{1}, e_{2}\rangle (\omega^{\sharp} )^{1}+ \langle e_{2}, e_{2}\rangle (\omega^{\sharp} )^{2}= 2(\omega^{\sharp} )^{1}+ 5(\omega^{\sharp} )^{2}= g_{21}(\omega^{\sharp} )^{1}+ g_{22}(\omega^{\sharp} )^{2}.$$
Các phần tử này các đẳng thức là ngắn gọn được viết như
$$\begin{pmatrix} \omega_{1} \\ \omega_{2} \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 2 & 5 \end{pmatrix} \begin{pmatrix} (\omega^{\sharp} )^{1} \\ (\omega^{\sharp} )^{2} \end{pmatrix} = g \begin{pmatrix} (\omega^{\sharp} )^{1} \\ (\omega^{\sharp} )^{2} \end{pmatrix} .$$
Thì
$$\begin{pmatrix} (\omega^{\sharp} )^{1} \\ (\omega^{\sharp} )^{2} \end{pmatrix} = g^{-1} \begin{pmatrix} \omega_{1} \\ \omega_{2} \end{pmatrix} = \begin{pmatrix} 5 & -2 \\ -2 & 1 \end{pmatrix} \begin{pmatrix} \omega_{1} \\ \omega_{2} \end{pmatrix} ,$$
Mà trong turn suy ra
$$(\omega^{\sharp} )^{1}= 5\omega_{1}  -2\omega_{2} ,(\omega^{\sharp} )^{2}= -2\omega_{1}  + \omega_{2} ,$$
I.e.
$$\omega^{\sharp} = (5\omega_{1}  -2\omega_{2} )e_{1} + (-2\omega_{1}  + \omega_{2} )e_{2}.$$

<!-- PAGE 1172 -->
Tích vô hướng (inner product) $\langle$ -, $-\rangle$ trên $E$ cảm sinh tích vô hướng (inner product) trên $E^{*}$ được ký hiệu $\langle$ -, $-\rangle_{E*}$, và cho trước bởi
$$\langle \omega_{1} , \omega_{2} \rangle_{E*} = \langle \omega_{1}^{\sharp} , \omega_{2}^{\sharp} \rangle ,for all \omega_{1} , \omega_{2}  \in E^{*}.$$
Thì ta có
$$\langle u^{\flat}, v^{\flat}\rangle_{E*} = \langle (u^{\flat})^{\sharp}, (v^{\flat})^{\sharp}\rangle = \langle u, v\rangle for allu, v \in E.$$
Nếu $(e_{1}, \dots  , e_{n})$ là cơ sở (basis) của $E$ và $g_{ij} = \langle e_{i}, e_{j}\rangle$, như
$$(e_{i}^{*} )^{\sharp}= \sum_{k=1}^{n}  g^{ik}e_{k},$$
Dễ phép tính chỉ ra rằng
$$\langle e_{i}^{*} , e_{j}^{*}\rangle_{E*} = \langle (e_{i}^{*} )^{\sharp}, (e_{j}^{*})^{\sharp}\rangle = g^{ji}= g^{ij};$$
Rằng là, trong cơ sở (basis) $(e_{1}^{*}, \dots  , e_{n}^{*})$, tích vô hướng (inner product) trên $E^{*}$ được biểu diễn bởi ma trận $(g^{ij})$, nghịch đảo của ma trận $(g_{ij})$. tích vô hướng (inner product) trên hữu hạn dimensional thực không gian vectơ (vector space) cũng cho ta chính tắc đẳng cấu giữa không gian Hom(E, $E;\mathbb{R})$ của các dạng song tuyến tính trên $E$, và không gian Hom(E, $E)$ của các ánh xạ tuyến tính (linear maps) từ $E$ đến chính nó. Bằng cách sử dụng đẳng cấu này, ta có thể định nghĩa vết (trace) của dạng song tuyến tính (bilinear form) trong nội tại cách thức. Điều này kỹ thuật được sử dụng trong vi phân hình học, ví dụ, để định nghĩa divergence của vi phân one-form.

> **Mệnh đề 33.3.** Nếu $\langle$ -, $-\rangle$ là tích vô hướng (inner product) trên hữu hạn dimensional thực không gian vectơ (vector space) $E$, thì với mọi dạng song tuyến tính (bilinear form) $f$: $E \times  E \to \mathbb{R}$, tồn tại duy nhất một ánh xạ tuyến tính (linear map) $f^{\natural}$: $E \to E$ sao cho
$$f(u, v) = \langle f^{\natural} (u), v\rangle ,for all u, v \in E.$$
Ánh xạ $f \mapsto f^{\natural}$ là tuyến tính đẳng cấu giữa Hom(E, $E; K)$ và Hom(E, $E)$. Hơn nữa, với mọi cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $E$, nếu $A = (f(e_{i}, e_{j}))$ là ma trận biểu diễn $f, G = (g_{ij} = \langle e_{i}, e_{j}\rangle$) đối xứng Gram ma trận biểu diễn tích vô hướng (inner product) $\langle$ -, $-\rangle$, và $B = (b_{ij})$ ma trận biểu diễn $f^{\natural}$, thì
$$B = G^{-1}A^{\top}.$$

*Chứng minh.* Với mọi $g \in$ Hom(E, $E)$, ánh xạ cho trước bởi
$$f(u, v) = \langle g(u), v\rangle ,u, v \in E,$$
Là rõ ràng song tuyến tính. Nó là cũng rõ ràng rằng ở trên định nghĩa ánh xạ tuyến tính (linear map) từ Hom(E, $E)$ đến Hom(E, $E; K)$. ánh xạ này là đơn ánh (injective), bởi vì nếu f(u, $v) = 0$ với mọi $u, v \in E$, như $\langle$ -, $-\rangle$ là tích vô hướng (inner product), ta thu được g(u) $= 0$ với mọi $u \in E$. Hơn nữa, cả hai các không gian Hom(E, $E)$ và Hom(E, $E; K)$ có cùng số chiều, do đó của ta ánh xạ tuyến tính (linear map) là đẳng cấu.

<!-- PAGE 1173 -->
Vì cột thứ $j$ của $B$ xác định $f^{\natural} (e_{j})$ bởi
$$f^{\natural} (e_{j}) = \sum_{k=1}^{n}  b_{kj}e_{k},$$
Bằng cách sử dụng sự kiện rằng Gram ma trận $G$ là đối xứng, ta có
$$*+$$
$$a_{ji} = f(e_{j}, e_{i}) =f^{\natural} (e_{j}), e_{i}= \sum_{k=1}^{n}  b_{kj}e_{k}, e_{i}$$
$$= \sum_{k=1}^{n}  b_{kj}\langle e_{k}, e_{i}\rangle = \sum_{k=1}^{n}  b_{kj}g_{ki} = \sum_{k=1}^{n}  g_{ik}b_{kj}.$$
Các phương trình
$$a_{ji} = \sum_{k=1}^{n}  g_{ik}b_{kj}$$
Là tương đương đến $GB = A^{\top}$, và do đó
$$B = G^{-1}A^{\top},$$
Như đã khẳng định. Nếu $(e_{1}, \dots  , e_{n})$ là cơ sở trực chuẩn (orthonormal basis) của $E$, thì ta kiểm tra ngay lập tức rằng vết (trace) của ánh xạ tuyến tính (linear map) $g$ (mà là độc lập của lựa chọn của cơ sở (basis)) được cho bởi
$$\mathrm{tr}(g) = \sum_{i=1}^{n}  \langle g(e_{i}), e_{i}\rangle ,$$
Ở đâu $n =$ dim(E).

> **Định nghĩa 33.3.** Ta định nghĩa vết (trace) của dạng song tuyến tính (bilinear form) $f$ bởi
$$\mathrm{tr}(f) = \mathrm{tr}(f^{\natural} ).$$
Từ Mệnh đề 33.3, tr(f) được cho bởi
$$\mathrm{tr}(f) = \sum_{i=1}^{n}  f(e_{i}, e_{i}),$$
Với mọi cơ sở trực chuẩn (orthonormal basis) $(e_{1}, \dots  , e_{n})$ của $E$. Ta có thể cũng kiểm tra một cách trực tiếp rằng ở trên biểu thức là độc lập của lựa chọn của cơ sở trực chuẩn (orthonormal basis).
