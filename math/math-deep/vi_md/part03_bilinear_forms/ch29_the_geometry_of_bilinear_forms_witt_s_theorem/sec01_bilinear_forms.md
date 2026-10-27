# Các dạng song tuyến tính


<!-- PAGE 1011 -->
Chương $29$ Hình học của Các dạng song tuyến tính; Witt’s Định lý; Cartan–Dieudonn´e Định lý

## 29.1 Các dạng song tuyến tính

Trong chương này, ta study cấu trúc của vectơ $K$ không gian $E$ endowed với dạng song tuyến tính không suy biến $\phi$: $E \times  E \to K$ (với mọi trường $K)$, mà có thể được được quan điểm như loại của suy rộng/tổng quát hóa tích vô hướng (inner product). Unlike trường hợp của tích vô hướng (inner product), ở đó có thể là khác không các vectơ $u \in E$ sao cho $\phi (u, u) = 0$ do đó ánh xạ $u \mapsto \phi (u, u)$ có thể không có dài hơn là interpreted như khái niệm của square độ dài (cũng, $\phi (u, u)$ có thể không là thực và dương!). Tuy nhiên, khái niệm của tính trực giao survives: ta nói rằng $u, v \in E$ là trực giao khi và chỉ khi $\phi (u, v) = 0$. Dưới một số additional các điều kiện trên $\phi$, nó là thì khả dĩ/có thể đến split $E$ vào trực giao các không gian con có một số đặc biệt các tính chất. Hóa ra là đặc biệt các trường hợp ở đâu $\phi$ là đối xứng (hoặc Hermite) hoặc skewsymmetric (hoặc skew-Hermitian) có thể được handled uniformly bằng cách sử dụng deep định lý do Witt (Witt phân rã định lý $(1936))$. Ta bắt đầu với rất tổng quát tình huống của dạng song tuyến tính (bilinear form) $\phi$: $E\times F \to K$, ở đâu $K$ là tùy ý trường, có thể của characteristric $2$. Thực sự, chẵn/ngay cả dù tại thứ nhất glance điều này có thể xuất hiện là unnecessary abstraction, hóa ra là tình huống này phát sinh trong attempting để chứng minh các tính chất của ánh xạ song tuyến tính (bilinear map) $\phi$: $E \times E \to K$, bởi vì nó có thể là cần đến thu hẹp $\phi$ đến khác nhau các không gian con $U$ và $V$ của $E$. Điều này tổng quát cách tiếp cận đã là pioneered bởi Chevalley $[37], E$. Artin $[6]$, và Bourbaki $[24]$. thứ ba source đã là major source của inspiration, và nhiều các chứng minh được lấy từ nó. Khác hữu ích references bao gồm Snapper và Troyer $[168]$, Berger $[12]$, Jacobson $[101]$, Grove $[86]$, Taylor $[180]$, và Berndt $[14]$.

> **Định nghĩa 29.1.** Cho trước hai các không gian vectơ $E$ và $F$ trên trường $K$, ánh xạ $\phi$: $E \times  F \to K$ là dạng song tuyến tính (bilinear form) khi và chỉ khi sau đây các điều kiện đúng: Với mọi $u, u_{1}, u_{2} \in E$, tất cả $v, v_{1}, v_{2} \in F$, cho
$$1011$$

<!-- PAGE 1012 -->
Tất cả $\lambda , \mu  \in K$, ta có
$$\phi (u_{1} + u_{2}, v) = \phi (u_{1}, v) + \phi (u_{2}, v)$$
$$\phi (u, v_{1} + v_{2}) = \phi (u, v_{1}) + \phi (u, v_{2})$$
$$\phi (\lambda u, v) = \lambda \phi (u, v)$$
$$\phi (u, \mu v) = \mu \phi (u, v).$$
Dạng song tuyến tính (bilinear form) như trong Định nghĩa 29.1 đôi khi được gọi là một cặp. thứ nhất hai các điều kiện suy ra rằng $\phi (0, v) = \phi (u, 0) = 0$ với mọi $u \in E$ và tất cả $v \in F$. Nếu $E = F$, nhận thấy rằng
$$\phi (\lambda u + \mu v, \lambda u + \mu v) = \lambda \phi (u, \lambda u + \mu v) + \mu \phi (v, \lambda u + \mu v)$$
$$= \lambda^{2} \phi (u, u) + \lambda \mu \phi (u, v) + \lambda \mu \phi (v, u) + \mu^{2} \phi (v, v).$$
Nếu ta cho $\lambda  = \mu  = 1$, ta thu được
$$\phi (u + v, u + v) = \phi (u, u) + \phi (u, v) + \phi (v, u) + \phi (v, v).$$
Nếu $\phi$ là đối xứng, mà có nghĩa là
$$\phi (u, v) = \phi (v, u)for all u, v \in E,$$
Thì
$$2\phi (u, v) = \phi (u + v, u + v) -\phi (u, u) -\phi (v, v).(*)$$
Hàm $\Phi$ được định nghĩa sao cho
$$\Phi (u) = \phi (u, u)u \in E,$$
Được gọi là dạng toàn phương (quadratic form) liên kết với $\phi$. Nếu trường $K$ là không của characteristic $2$, thì $\phi$ là hoàn toàn được xác định bởi của nó dạng toàn phương (quadratic form) $\Phi$. dạng song tuyến tính đối xứng $\phi$ được gọi là dạng cực (polar form) của $\Phi$. Điều này suggests sau đây định nghĩa.

> **Định nghĩa 29.2.** hàm $\Phi$: $E \to K$ là dạng toàn phương (quadratic form) trên $E$ nếu sau đây các điều kiện đúng:
$(1)$ Ta có $\Phi (\lambda u) = \lambda^{2} \Phi (u)$, với mọi $u \in E$ và tất cả $\lambda  \in E$.
$(2)$ ánh xạ $\phi'$ cho trước bởi $\phi' (u, v) = \Phi (u+v)-\Phi (u)-\Phi (v)$ là song tuyến tính. Hiển nhiên, ánh xạ $\phi'$ là đối xứng. Vì $\Phi (x + x) = \Phi$ (2x) $= 4\Phi (x)$, ta có
$$\phi' (u, u) = 2\Phi (u)u \in E.$$

<!-- PAGE 1013 -->
Nếu trường $K$ là không của characteristic $2$, thì $\phi  =^{1}\phi'$ là duy nhất dạng song tuyến tính đối xứng sao cho rằng $\phi (u, u) = \Phi (u)$ với mọi $u \in E. The^{2}$ dạng song tuyến tính (bilinear form) $\phi  =_{2}^{1}\phi'$ được gọi là dạng cực (polar form) của $\Phi$. Trong trường hợp này, có một song ánh giữa tập hợp của các dạng song tuyến tính trên $E$ và tập hợp của các dạng toàn phương trên $E$. Nếu $K$ là trường của characteristic $2$, thì $\phi'$ là thay phiên, mà có nghĩa là
$$\phi' (u, u) = 0for all u \in E.$$
Do đó nếu $K$ là trường của characteristic $2$, thì $\Phi$ không thể là recovered từ dạng song tuyến tính đối xứng $\phi'$. Nếu $(e_{1}, \dots  , e_{n})$ là cơ sở (basis) của $E$, nó là dễ để chỉ ra rằng
$$\Phi \begin{pmatrix} \lambda_{i} e_{i} \end{pmatrix} \sum_{i=1}^{n}  = \sum_{i=1}^{n}  \lambda_{i}^{2}  \Phi (e_{i}) + \sum_{i\neq j}  \lambda_{i} \lambda_{j} \phi' (e_{i}, e_{j}).$$
Điều này chỉ ra rằng dạng toàn phương (quadratic form) $\Phi$ là hoàn toàn được xác định bởi các vô hướng $\Phi (e_{i})$ và $\phi' (e_{i}, e_{j})$ (i̸ $= j)$. Hơn nữa, cho trước bất kỳ dạng song tuyến tính (bilinear form) $\psi$: $E \times  E \to K$ (không nhất thiết đối xứng) ta có thể định nghĩa dạng toàn phương (quadratic form) $\Phi$ bằng cách đặt $\Phi (x) = \psi (x, x)$, và ta ngay lập tức kiểm tra rằng dạng song tuyến tính đối xứng $\phi'$ liên kết với $\Phi$ được cho bởi $\phi' (u, v) = \psi (u, v) + \psi (v, u)$. Bằng cách sử dụng ở trên các sự kiện, nó là không khó để chứng minh rằng cho trước bất kỳ dạng toàn phương (quadratic form) $\Phi$, tồn tại một (nonsymmetric) dạng song tuyến tính (bilinear form) $\psi$ sao cho $\Phi (u) = \psi (u, u)$ với mọi $u \in E$ (xem Bourbaki $[24]$, Mục §3.4, Mệnh đề $2)$. Do đó, các dạng toàn phương là nhiều hơn/thêm tổng quát hơn đối xứng các dạng song tuyến tính (ngoại trừ trong characteristic $\neq  2)$.

> **Định nghĩa 29.3.** Cho trước bất kỳ dạng song tuyến tính (bilinear form) $\phi$: $E \times  E \to K$ ở đâu $K$ là trường của bất kỳ characteristic, ta nói rằng $\phi$ là thay phiên nếu
$$\phi (u, u) = 0for all u \in E,$$
Và phản đối xứng nếu
$$\phi (v, u) = -\phi (u, v)for all u, v \in E.$$
Nếu $K$ là trường của bất kỳ characteristic, đồng nhất thức
$$\phi (u + v, u + v) = \phi (u, u) + \phi (u, v) + \phi (v, u) + \phi (v, v)$$
Chỉ ra rằng nếu $\phi$ là thay phiên, thì
$$\phi (v, u) = -\phi (u, v)for all u, v \in E,$$
Rằng là, $\phi$ là phản đối xứng. Ngược lại, nếu trường $K$ là không của characteristic $2$, thì phản đối xứng ánh xạ song tuyến tính (bilinear map) là thay phiên, vì $\phi (u, u) = -\phi (u, u)$ suy ra $\phi (u, u) = 0$. quan trọng hệ quả của tính song tuyến tính là rằng cặp cho ta ánh xạ tuyến tính (linear map) từ $E$ vào $F^{*}$ và ánh xạ tuyến tính (linear map) từ $F$ vào $E^{*}$ (ở đâu $E^{*} = Hom_{K}(E, K)$, đối ngẫu (dual) của $E$, là tập hợp của các ánh xạ tuyến tính (linear maps) từ $E$ đến $K$, được gọi là các dạng tuyến tính).

<!-- PAGE 1014 -->

> **Định nghĩa 29.4.** Cho trước ánh xạ song tuyến tính (bilinear map) $\phi$: $E \times  F \to K$, với mọi $u \in E$, cho $l_{\phi}(u)$ là dạng tuyến tính (linear form) trong $F^{*}$ cho trước bởi
$$l_{\phi}(u)(y) = \phi (u, y)for all y \in F,$$
Và với mọi $v \in F$, cho $r_{\phi}(v)$ là dạng tuyến tính (linear form) trong $E^{*}$ cho trước bởi
$$r_{\phi}(v)(x) = \phi (x, v)for all x \in E.$$
Bởi vì $\phi$ là song tuyến tính, các ánh xạ $l_{\phi}$: $E \to F^{*}$ và $r_{\phi}$: $F \to E^{*}$ là tuyến tính.

> **Định nghĩa 29.5.** ánh xạ song tuyến tính (bilinear map) $\phi$: $E\times F \to K$ được nói là không suy biến khi và chỉ khi sau đây các điều kiện đúng:
$(1)$ Với mọi $u \in E$, nếu $\phi (u, v) = 0$ với mọi $v \in F$, thì $u = 0$, và
$(2)$ Với mọi $v \in F$, nếu $\phi (u, v) = 0$ với mọi $u \in E$, thì $v = 0$. sau đây mệnh đề chỉ ra importance của $l_{\phi}$ và $r_{\phi}$.

> **Mệnh đề 29.1.** Cho trước ánh xạ song tuyến tính (bilinear map) $\phi$: $E \times  F \to K$, các tính chất sau đây đúng:
() ánh xạ $l_{\phi}$ là đơn ánh (injective) khi và chỉ khi Tính chất $(1)$ của Định nghĩa 29.5 nghiệm đúng.
$(b)$ ánh xạ $r_{\phi}$ là đơn ánh (injective) khi và chỉ khi Tính chất $(2)$ của Định nghĩa 29.5 nghiệm đúng.
$(c)$ dạng song tuyến tính (bilinear form) $\phi$ là không suy biến và khi và chỉ khi $l_{\phi}$ và $r_{\phi}$ là đơn ánh (injective).
$(d)$ Nếu dạng song tuyến tính (bilinear form) $\phi$ là không suy biến và nếu $E$ và $F$ có hữu hạn số chiều, thì dim(E) $=$ dim(F), và $l_{\phi}$: $E \to F^{*}$ và $r_{\phi}$: $F \to E^{*}$ là tuyến tính các đẳng cấu.

*Chứng minh.* () Giả sử rằng $(1)$ của Định nghĩa 29.5 nghiệm đúng. Nếu $l_{\phi}(u) = 0$, thì $l_{\phi}(u)$ là dạng tuyến tính (linear form) có giá trị là $0$ với mọi $y$; nghĩa là,
$$l_{\phi}(u)(y) = \phi (u, y) = 0for all y \in F,$$
Và bởi $(1)$ của Định nghĩa 29.5, ta phải có $u = 0$. Vì vậy, $l_{\phi}$ là đơn ánh (injective). Ngược lại, nếu $l_{\phi}$ là đơn ánh (injective), và nếu
$$l_{\phi}(u)(y) = \phi (u, y) = 0for all y \in F,$$
Thì $l_{\phi}(u)$ là không tạo thành, và bởi tính đơn ánh của $l_{\phi}$, ta thu được $u = 0$; nghĩa là, $(1)$ của Định nghĩa 29.5 nghiệm đúng.
$(b)$ chứng minh là thu được bởi swapping các đối số/lập luận của $\phi$.
$(c)$ Điều này suy ra từ () và $(b)$.
$(d)$ Nếu $E$ và $F$ là hữu hạn dimensional, thì dim(E) $= dim(E^{*})$ và dim(F) $= dim(F^{*}$). Vì $\phi$ là không suy biến, $l_{\phi}$: $E \to F^{*}$ và $r_{\phi}$: $F \to E^{*}$ là đơn ánh (injective), do đó dim(E) $\le dim(F^{*}$) $=$ dim(F) và dim(F) $\le dim(E^{*}) =$ dim(E), mà suy ra rằng
$$\dim(E) = \dim(F),$$
Và do đó, $l_{\phi}$: $E \to F^{*}$ và $r_{\phi}$: $F \to E^{*}$ là song ánh (bijective).

<!-- PAGE 1015 -->
Như hệ quả của Mệnh đề 29.1, ta có kết quả sau đặc trưng của không suy biến ánh xạ song tuyến tính (bilinear map). chứng minh là để lại như một bài tập.

> **Mệnh đề 29.2.** Cho trước ánh xạ song tuyến tính (bilinear map) $\phi$: $E \times  F \to K$, nếu $E$ và $F$ có cùng hữu hạn số chiều, thì các tính chất sau đây là tương đương:
$(1)$ ánh xạ $l_{\phi}$ là đơn ánh (injective).
$(2)$ ánh xạ $l_{\phi}$ là toàn ánh (surjective).
$(3)$ ánh xạ $r_{\phi}$ là đơn ánh (injective).
$(4)$ ánh xạ $r_{\phi}$ là toàn ánh (surjective).
$(5)$ dạng song tuyến tính (bilinear form) $\phi$ là không suy biến. Nhận thấy rằng theo chính tắc cặp giữa $E^{*}$ và $E$ cho trước bởi
$$\langle f, u\rangle = f(u),f \in E^{*}, u \in E,$$
(và chính tắc cặp giữa $F^{*}$ và $F)$, ta có
$$\phi (u, v) = \langle l_{\phi}(u), v\rangle = \langle r_{\phi}(v), u\rangle u \in E, v \in F.$$

> **Mệnh đề 29.3.** Cho trước ánh xạ song tuyến tính (bilinear map) $\phi$: $E \times  F \to K$, nếu $\phi$ là không suy biến và $E$ và $F$ là hữu hạn chiều, thì dim(E) $=$ dim(F) $= n$, và với mọi cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $E$, có một cơ sở (basis) $(f_{1}, \dots  , f_{n})$ của $F$ sao cho $\phi (e_{i}, f_{j}) = \delta_{ij}$, với mọi $i, j = 1, \dots  , n$.

*Chứng minh.* Vì $\phi$ là không suy biến, theo Mệnh đề 29.1 ta có dim(E) $=$ dim(F) $= n$, và theo Mệnh đề 29.2, ánh xạ tuyến tính (linear map) $r_{\phi}$ là song ánh (bijective). Thì, nếu $(e_{1}^{*}, \dots  , e_{n}^{*})$ là đối ngẫu (dual) cơ sở (basis) (trong $E^{*})$ của cơ sở (basis) $(e_{1}, \dots  , e_{n})$, các vectơ $(f_{1}, \dots  , f_{n})$ cho trước bởi $f_{i} = r_{\phi}^{-1} (e_{i}^{*}$) tạo thành cơ sở (basis) của $F$, và ta có
$$\phi (e_{i}, f_{j}) = \langle r_{\phi}(f_{j}), e_{i}\rangle = \langle e_{i}^{*} , e_{j}\rangle = \delta_{ij} ,$$
Như đã khẳng định. Nếu $E = F$ và $\phi$ là đối xứng, thì ta có kết quả sau thú vị kết quả.

> **Định lý 29.4.** Cho trước bất kỳ dạng song tuyến tính (bilinear form) $\phi$: $E\times E \to K$ với dim(E) $= n$, nếu $\phi$ là đối xứng (có thể suy biến) và $K$ thực hiện không có characteristic $2$, thì có một cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $E$ sao cho $\phi (e_{i}, e_{j}) = 0$, với mọi $i \neq  j$.

*Chứng minh.* Ta tiến hành bằng quy nạp theo $n \ge 0$, sau đây chứng minh do Chevalley. base trường hợp $n = 0$ là tầm thường. Cho quy nạp bước, giả sử rằng $n \ge 1$ và rằng giả thiết quy nạp (induction hypothesis) nghiệm đúng với mọi các không gian vectơ có số chiều n-1. Nếu $\phi (u, v) = 0$ với mọi $u, v \in E$, thì phát biểu nghiệm đúng một cách tầm thường. Ngược lại, vì $K$ thực hiện không có characteristic $2$, phương trình
$$2\phi (u, v) = \phi (u + v, u + v) -\phi (u, u) -\phi (v, v)(*)$$

<!-- PAGE 1016 -->
Chỉ ra rằng tồn tại một khác không vectơ $e_{1} \in E$ sao cho $\phi (e_{1}, e_{1}) \neq  0$ vì ngược lại $\phi$ sẽ triệt tiêu với mọi $u, v \in E$. Ta khẳng định rằng tập hợp
$$H = {v \in E | \phi (e_{1}, v) = 0}$$
Có số chiều $n$ - $1$, và rằng $e_{1} \in / H$. Điều này là bởi vì
$$H = \mathrm{Ker} (l_{\phi}(e_{1})),$$
Ở đâu $l_{\phi}(e_{1})$ là dạng tuyến tính (linear form) trong $E^{*}$ được xác định bởi $e_{1}$. Vì $\phi (e_{1}, e_{1}) \neq  0$, ta có $e_{1} \in / H$, dạng tuyến tính (linear form) $l_{\phi}(e_{1})$ là không không tạo thành, và do đó hạt nhân (hạt nhân (kernel)) của nó là siêu phẳng (hyperplane) $H$ (không gian con có số chiều $n$ - $1)$. Vì dim(H) $= n$ - $1$ và $e_{1} \in / H$, ta có tổng trực tiếp (direct sum)
$$E = H \oplus Ke_{1}.$$
Theo giả thiết quy nạp ứng dụng đến $H$, ta thu được cơ sở (basis) $(e_{2}, \dots  , e_{n})$ của các vectơ trong $H$ sao cho $\phi (e_{i}, e_{j}) = 0$, với mọi $i \neq  j$ với $2 \le i, j \le n$. Vì $\phi (e_{1}, v) = 0$ với mọi $v \in H$ và vì $\phi$ là đối xứng, ta cũng có $\phi (v, e_{1}) = 0$ với mọi $v \in H$, do đó ta thu được cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $E$ sao cho $\phi (e_{i}, e_{j}) = 0$, với mọi $i \neq  j$. Nếu $E$ và $F$ là hữu hạn chiều các không gian vectơ và nếu $(e_{1}, \dots  , e_{m})$ là cơ sở (basis) của $E$ và $(f_{1}, \dots  , f_{n})$ là cơ sở (basis) của $F$ thì tính song tuyến tính của $\phi$ cho ta
$$\phi \begin{pmatrix} x_{i}e_{i}, & y_{j}f_{j} \end{pmatrix} \sum_{i=1}^{m}  \sum_{j=1}^{n}  = \sum_{i=1j}^{m}  \sum_{=1}^{n}  x_{i}\phi (e_{i}, f_{j})y_{j}.$$
Điều này chỉ ra rằng $\phi$ là hoàn toàn được xác định bởi ma trận cỡ $n \times  m$ $M = (m_{ij})$ với $m_{ij} = \phi (e_{j}, f_{i})$, và trong ma trận tạo thành, ta có
$$\phi (x, y) = x^{\top}M^{\top} y = y^{\top}Mx,$$
Ở đâu $x$ và $y$ là các vectơ cột liên kết với $(x_{1}, \dots  , x_{m}) \in K^{m}$ và $(y_{1}, \dots  , y_{n}) \in K^{n}$. Như trong Mục 12.1, ta là committing slight abuse của ký hiệu của đặt $x$ ký hiệu
$$both the vector x = \sum_{i}  n=1 x_{i}e_{i} and the column vector associated with (x_{1}, \dots  , x_{n}) (and$$
Tương tự cho $y)$.

> **Định nghĩa 29.6.** Nếu $(e_{1}, \dots  , e_{m})$ là cơ sở (basis) của $E$ và $(f_{1}, \dots  , f_{n})$ là cơ sở (basis) của $F$, với mọi dạng song tuyến tính (bilinear form) $\phi$: $E \times  F \to K$, ma trận cỡ $n \times  m$ $M = (m_{ij})$ cho trước bởi $m_{ij} = \phi (e_{j}, f_{i})$ cho $i = 1, \dots  , n$ và $j = 1, \dots  , m$ được gọi là ma trận của $\phi$ đối với các cơ sở $(e_{1}, \dots  , e_{m})$ và $(f_{1}, \dots  , f_{n})$. sau đây sự kiện là dễ dàng được chứng minh.

> **Mệnh đề 29.5.** Nếu $m =$ dim(E) $=$ dim(F) $= n$, thì $\phi$ là không suy biến khi và chỉ khi ma trận $M$ là khả nghịch khi và chỉ khi det(M) $\neq  0$.

<!-- PAGE 1017 -->
Như ta sẽ xem sau này, hầu hết các dạng song tuyến tính rằng ta sẽ encounter là tương đương đến một có ma trận là của sau đây tạo thành: $1. I_{n}, -I_{n}. 2$. Nếu $p + q = n$, với $p, q \ge 1$,
$$I_{p,q} = \begin{pmatrix} I_{p} & 0 \\ 0 & -I_{q} \end{pmatrix}$$
$3$. Nếu $n =$ 2m,
$$J_{m.m} = \begin{pmatrix} 0 & I_{m} \\ -I_{m} & 0 \end{pmatrix}$$
$4$. Nếu $n =$ 2m,
$$A_{m,m} = I_{m.m}J_{m.m} = \begin{pmatrix} 0 & I_{m} \\ I_{m} & 0 \end{pmatrix} .$$
Nếu ta tạo thay đổi của các cơ sở cho trước bởi các ma trận $P$ và $Q$, sao cho $x =$ Px' và $y =$ Qy', thì mới ma trận biểu diễn $\phi$ là $P^{\top}$ MQ. Đặc biệt, nếu $E = F$ và cùng cơ sở (basis) được sử dụng, thì mới ma trận là $P^{\top}$ MP. Điều này chỉ ra rằng nếu $\phi$ là không suy biến, thì định thức (determinant) của $\phi$ được xác định sai khác square phần tử. Nhận thấy rằng nếu $\phi$ là dạng song tuyến tính đối xứng $(E = F)$ và nếu $K$ thực hiện không có characteristic $2$, thì theo Định lý 29.4, có một cơ sở (basis) của $E$ đối với mà ma trận $M$ biểu diễn $\phi$ là ma trận đường chéo (diagonal matrix). Nếu $K =\mathbb{R}$ hoặc $K =\mathbb{C}$, điều này cho phép chúng ta đến phân loại hoàn toàn đối xứng các dạng song tuyến tính. Nhắc lại rằng $\Phi (u) = \phi (u, u)$ với mọi $u \in E$.

> **Mệnh đề 29.6.** Cho trước bất kỳ dạng song tuyến tính (bilinear form) $\phi$: $E \times  E \to K$ với dim(E) $= n$, nếu $\phi$ là đối xứng và $K$ thực hiện không có characteristic $2$, thì có một cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $E$ sao cho
$$\Phi \begin{pmatrix} x_{i}e_{i} \end{pmatrix} \sum_{i=1}^{n}  = \sum_{i=1}^{r}  \lambda_{i} x_{i}^{2} ,$$
Với một số $\lambda_{i}  \in K -{0}$ và với $r \le n$. Hơn nữa, nếu $K = \mathbb{C}$, thì có một cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $E$ sao cho
$$\Phi \begin{pmatrix} x_{i}e_{i} \end{pmatrix} \sum_{i=1}^{n}  = \sum_{i=1}^{r}  x_{i}^{2} ,$$
Và nếu $K =\mathbb{R}$, thì có một cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $E$ sao cho
$$\Phi \begin{pmatrix} x_{i}e_{i} \end{pmatrix} \sum_{i=1}^{n}  = \sum_{i=1}^{p}  x_{i}^{2} - \sum_{i=p+1}^{p+q}  x_{i}^{2} ,$$
Với $0 \le p, q$ và $p + q \le n$.

<!-- PAGE 1018 -->

*Chứng minh.* thứ nhất phát biểu là trực tiếp hệ quả của Định lý 29.4. Nếu $K = \mathbb{C}$, thì mọi $\lambda_{i}$ có square nghiệm (root) $\mu_{i}$, và nếu thay thế $e_{i}$ bởi $e_{i}/\mu_{i}$, ta thu được mong muốn tạo thành. Nếu $K =\mathbb{R}$, thì có hai các trường hợp: $1$. Nếu $\lambda_{i}  > 0$, cho $\mu_{i}$ là dương square nghiệm (root) của $\lambda_{i}$ và thay thế $e_{i}$ bởi $e_{i}/\mu_{i}$. $2$. Nếu $\lambda_{i}  < 0$, et $\mu_{i}$ là dương square nghiệm (root) của $-\lambda_{i}$ và thay thế $e_{i}$ bởi $e_{i}/\mu_{i}$. Trong không suy biến trường hợp, các ma trận tương ứng với phức và thực trường hợp là, $I_{n}, -I_{n}$, và $I_{p,q}$. Nhận thấy rằng thứ hai phát biểu của Mệnh đề 29.6 nghiệm đúng trong bất kỳ trường trong mà mọi phần tử có square nghiệm (root). Trong trường hợp $K = \mathbb{R}$, ta có thể chỉ ra rằng(p, $q)$ chỉ phụ thuộc vào $\phi$.

> **Định nghĩa 29.7.** Cho $\phi$: $E \times E \to \mathbb{R}$ là bất kỳ đối xứng thực dạng song tuyến tính (bilinear form). Với mọi không gian con $U$ của $E$, ta nói rằng $\phi$ là xác định dương (positive definite) trên $U$ khi và chỉ khi $\phi (u, u) > 0$ với mọi khác không $u \in U$, và ta nói rằng $\phi$ là âm xác định trên $U$ khi và chỉ khi $\phi (u, u) < 0$ với mọi khác không $u \in U$. Thì, cho
$$r = \max{\dim(U) | U \subseteq E, \phi  is positive definite on U}$$
Và cho
$$s = \max{\dim(U) | U \subseteq E, \phi  is negative definite on U}$$

> **Mệnh đề 29.7.** (Sylvester’s inertia luật) Cho trước bất kỳ dạng song tuyến tính đối xứng $\phi$: $E\times E \to \mathbb{R}$ với dim(E) $= n$, với mọi cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $E$ sao cho
$$\Phi \begin{pmatrix} x_{i}e_{i} \end{pmatrix} \sum_{i=1}^{n}  = \sum_{i=1}^{p}  x_{i}^{2} - \sum_{i=p+1}^{p+q}  x_{i}^{2} ,$$
Với $0 \le p, q$ và $p + q \le n$, các số nguyên $p, q$ phụ thuộc chỉ trên $\phi$; thực ra, $p = r$ và $q = s$, với $r$ và $s$ như đã định nghĩa ở trên.

*Chứng minh.* Nếu ta cho $U$ là không gian con được sinh (spanned) bởi $(e_{1}, \dots  , e_{p})$, thì $\phi$ là xác định dương (positive definite) trên $U$, do đó $r \ge p$. Tương tự, nếu ta cho $V$ là không gian con được sinh (spanned) bởi $(e_{p+1}, \dots  , e_{p+q})$, thì $\phi$ là âm xác định trên $V$, do đó $s \ge q$. Tiếp theo, nếu $W_{1}$ là bất kỳ không gian con của cực đại số chiều sao cho $\phi$ là xác định dương (positive definite) trên $W_{1}$, và nếu ta cho V' là không gian con được sinh (spanned) bởi $(e_{p+1}, \dots  , e_{n})$, thì $\phi (u, u) \le 0$ trên V', do đó $W_{1} \cap$ V' $= (0)$, mà suy ra rằng $dim(W_{1}) +$ dim(V') $\le n$, và do đó, $r + n$ - $p \le n$; nghĩa là, $r \le p$. Tương tự, nếu $W_{2}$ là bất kỳ không gian con của cực đại số chiều sao cho $\phi$ là âm xác định trên $W_{2}$, và nếu ta cho U' là không gian con được sinh (spanned) bởi $(e_{1}, \dots  , e_{p}, e_{p+q+1}, \dots  , e_{n})$, thì $\phi (u, u) \ge 0$ trên U', do đó $W_{2} \cap$ U' $= (0)$, mà suy ra rằng $s + n$ - $q \le n$; nghĩa là, $s \le q$. Vì vậy, $p = r$ và $q = s$, như đã khẳng định Các phần tử này cuối cùng hai các kết quả có thể được suy rộng/tổng quát hóa đến được thứ tự các trường. Ví dụ, xem Snapper và Troyer $[168]$, Artin $[6]$, và Bourbaki $[24]$.
