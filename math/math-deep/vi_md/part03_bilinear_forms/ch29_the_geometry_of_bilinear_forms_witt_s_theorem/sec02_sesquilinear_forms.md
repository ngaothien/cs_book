# Các dạng nửa tuyến tính


<!-- PAGE 1019 -->

## 29.2 Các dạng nửa tuyến tính

$$In \frac{order}{\lambda ,} to accomodate Hermitian forms, we assume that some involutive automorphism,$$
$\lambda  \mapsto$ của trường $K$ là cho trước. Điều này tự đẳng cấu của $K$ thỏa mãn các tính chất sau đây:
$$\overline{(}\overline{\lambda}\overline{+}\overline{\mu}\overline{) =}\overline{\lambda} +\overline{\mu}$$
$$\overline{(}\overline{\lambda \mu}\overline{) =}\overline{\lambda  \mu}$$
$$\overline{\lambda} = \lambda .$$
Vì bất kỳ trường tự đẳng cấu các ánh xạ multiplicative unit $1$ đến chính nó, ta có $\overline{1 = 1.}$ Nếu tự đẳng cấu $\lambda  \mapsto \overline{\lambda}$ là đồng nhất thức, thì ta là trong tiêu chuẩn tình huống của dạng song tuyến tính (bilinear form). Khi $K =\mathbb{C}$ (phức các số), thì ta thường chọn tự đẳng cấu của $\mathbb{C}$ là liên hợp; cụ thể là, ánh xạ
$$a + ib \mapsto a -ib.$$

> **Định nghĩa 29.8.** Cho trước hai các không gian vectơ $E$ và $F$ trên trường $K$ với involutive tự đẳng cấu $\lambda  \mapsto \overline{\lambda}$, ánh xạ $\phi$: $E \times  F \to K$ là (phải) dạng nửa tuyến tính (sesquilinear form) khi và chỉ khi sau đây các điều kiện đúng: Với mọi $u, u_{1}, u_{2} \in E$, tất cả $v, v_{1}, v_{2} \in F$, với mọi $\lambda , \mu  \in K$, ta có
$$\phi (u_{1} + u_{2}, v) = \phi (u_{1}, v) + \phi (u_{2}, v)$$
$$\phi (u, v_{1} + v_{2}) = \phi (u, v_{1}) + \phi (u, v_{2})$$
$$\phi (\lambda u, v) = \lambda \phi (u, v)$$
$$\phi (u, \mu v) =\overline{\mu \phi}(u, v).$$
Một lần nữa, $\phi (0, v) = \phi (u, 0) = 0$. Nếu $E = F$, thì ta có
$$\phi (\lambda u + \mu v, \lambda u + \mu v) = \lambda \phi (u, \lambda u + \mu v) + \mu \phi (v, \lambda u + \mu v)$$
$$=\overline{\lambda \lambda \phi}(u, u) +\overline{\lambda \mu \phi}(u, v) +\overline{\lambda \mu \phi}(v, u) +\overline{\mu \mu \phi}(v, v).$$
Nếu ta cho $\lambda  = \mu  = 1$ và thì $\lambda  = 1, \mu  = -1$, ta thu được
$$\phi (u + v, u + v) = \phi (u, u) + \phi (u, v) + \phi (v, u) + \phi (v, v)$$
$$\phi (u -v, u -v) = \phi (u, u) -\phi (u, v) -\phi (v, u) + \phi (v, v),$$
Do đó bởi phép trừ, ta thu được
$$2(\phi (u, v) + \phi (v, u)) = \phi (u + v, u + v) -\phi (u -v, u -v)for u, v \in E.$$
Nếu ta thay thế $v$ bởi $\lambda v$ (với $\lambda  \neq  0)$, ta thu được
$$2(\overline{\lambda \phi}(u, v) + \lambda \phi (v, u)) = \phi (u + \lambda v, u + \lambda v) -\phi (u -\lambda v, u -\lambda v),$$

<!-- PAGE 1020 -->
Và bởi combining ở trên hai các phương trình, ta thu được
$$2(\lambda  -\overline{\lambda})\phi (u, v) = \lambda \phi (u + v, u + v) -\lambda \phi (u -v, u -v)$$
$$-\phi (u + \lambda v, u + \lambda v) + \phi (u -\lambda v, u -\lambda v).(*)$$
Nếu tự đẳng cấu $\lambda  \mapsto \overline{\lambda}$ là không đồng nhất thức, thì tồn tại một $\lambda  \in K$ sao cho $\lambda -\overline{\lambda} \neq  0$, và nếu $K$ là không của characteristic $2$, thì ta xem rằng dạng nửa tuyến tính (sesquilinear form) $\phi$ là hoàn toàn được xác định bởi của nó thu hẹp đến đường chéo (rằng là, tập hợp của các giá trị ${\phi (u, u)$ | $u \in E})$. Trong trường hợp đặc biệt khi $K =\mathbb{C}$, ta có thể chọn $\lambda  = i$, và ta thu được $4\phi (u, v) = \phi (u + v, u + v)$ - $\phi (u$ - $v, u$ - $v) + i\phi (u + \lambda v, u + \lambda v)$ - $i\phi (u$ - $\lambda v, u$ - $\lambda v)$.
Nhận xét: Nếu tự đẳng cấu $\lambda  \mapsto \overline{\lambda}$ là đồng nhất thức, thì nói chung $\phi$ là không được xác định bởi giá trị của nó trên đường chéo, trừ khi $\phi$ là đối xứng. Trong nửa tuyến tính (sesquilinear) đặt, hóa ra là sau đây hai các trường hợp là của interest: $1$. Ta có
$$\phi (v, u) =\overline{\phi}\overline{(}\overline{u, v}\overline{)},for all u, v \in E,$$
Trong mà trường hợp ta nói rằng $\phi$ là Hermite. Trong trường hợp đặc biệt khi $K = \mathbb{C}$ và involutive tự đẳng cấu là liên hợp, ta xem rằng $\phi (u, u) \in \mathbb{R}$, cho $u \in E. 2$. Ta có
$$\phi (v, u) = -\overline{\phi}\overline{(}\overline{u, v}\overline{)},for all u, v \in E,$$
Trong mà trường hợp ta nói rằng $\phi$ là skew-Hermitian. Ta được quan sát rằng trong characteristic khác nhau từ $2$, dạng nửa tuyến tính (sesquilinear form) được xác định bởi của nó thu hẹp đến đường chéo. Cho Hermite và skew-Hermitian các dạng, ta có kết quả sau loại của điều ngược lại.

> **Mệnh đề 29.8.** Nếu $\phi$ là khác không Hermite hoặc skew-Hermitian tạo thành và nếu $\phi (u, u) = 0$ với mọi $u \in E$, thì $K$ là của characteristic $2$ và tự đẳng cấu $\lambda  \mapsto \overline{\lambda}$ là đồng nhất thức.

*Chứng minh.* Ta cho chứng minh trong Hermite trường hợp, skew-Hermitian trường hợp đang là để lại như một bài tập. Giả sử rằng $\phi$ là thay phiên. Từ đồng nhất thức
$$\phi (u + v, u + v) = \phi (u, u) + \phi (u, v) +\overline{\phi}\overline{(}\overline{u, v}\overline{) +} \phi (v, v),$$
Ta thu được
$$\phi (u, v) = -\overline{\phi}\overline{(}\overline{u, v}\overline{)} for all u, v \in E.$$
Vì $\phi$ là không không tạo thành, ở đó tồn tại một số khác không các vectơ $u, v \in E$ sao cho $\phi (u, v) = 1$. Với mọi $\lambda  \in K$, ta có
$$\lambda \phi (u, v) = \phi (\lambda u, v) = -\overline{\phi}\overline{(}\overline{\lambda u, v}\overline{) =} -\overline{\lambda  \phi}\overline{(}\overline{u, v}\overline{)},$$

<!-- PAGE 1021 -->
Và vì $\phi (u, v) = 1$, ta thu được
$$\lambda  = -\overline{\lambda} for all \lambda  \in K.$$
Cho $\lambda  = 1$, ta thu được $1 = -1$, mà có nghĩa là $K$ có characterictic $2$. Nhưng khi đó
$$\lambda  = -\overline{\lambda} =\overline{\lambda} for all \lambda  \in K,$$
Do đó tự đẳng cấu $\lambda  \mapsto \overline{\lambda}$ là đồng nhất thức. định nghĩa của các ánh xạ tuyến tính (linear maps) $l_{\phi}$ và $r_{\phi}$ đòi hỏi nhỏ twist do tự đẳng cấu $\lambda  \mapsto \overline{\lambda}$.
$$\frac{Definition}{\lambda ,} 29.9. Given a vector space \frac{E}{E} over a field K with an involutive automorphism$$
$\lambda  \mapsto$ ta định nghĩa vectơ $K$ không gian như $E$ với của nó nhóm Abel (abelian group) cấu trúc, nhưng với vô hướng (scalar) phép nhân cho trước bởi
$$(\lambda , u) \mapsto \overline{\lambda u.}$$
Cho trước hai vectơ $K$ các không gian $E$ và $F$, nửa tuyến tính (semilinear) ánh xạ $f$: $E \to F$ là hàm, sao cho với mọi $u, v \in E$, với mọi $\lambda  \in K$, ta có
$$f(u + v) = f(u) + f(v)$$
$$f(\lambda u) =\overline{\lambda f}(u).$$
$$Because \overline{\lambda} = \lambda , observe that a \frac{function}{E} f : E \to F is semilinear iff it is a linear map$$
$$f : \overline{E} \to F \frac{.}{E.} The K-vector spaces E and are isomorphic, since any basis (e_{i})_{i\in I} of E is also$$
Cơ sở (basis) của các ánh xạ $l_{\phi}$ và $r_{\phi}$ được định nghĩa như sau: Với mọi $u \in E$, cho $l_{\phi}(u)$ là dạng tuyến tính (linear form) trong $F^{*}$ được định nghĩa sao cho
$$l_{\phi}(u)(y) =\overline{\phi}\overline{(}\overline{u, y}\overline{)} for all y \in F,$$
Và với mọi $v \in F$, cho $r_{\phi}(v)$ là dạng tuyến tính (linear form) trong $E^{*}$ được định nghĩa sao cho
$$r_{\phi}(v)(x) = \phi (x, v)for all x \in E.$$
Độc giả nên kiểm tra rằng bởi vì ta được sử dụng $\overline{\phi}\overline{(}\overline{u, y}\overline{)}$ trong định nghĩa của $l_{\phi}(u)(y)$,
$$function \frac{l_{\phi}}{E} (u) is indeed a linear form in F^{*} . It \frac{is}{F} also easy to check that l_{\phi} is a linear$$
Ánh xạ $l_{\phi}$: $\to F^{*}$, và rằng $r_{\phi}$ là ánh xạ tuyến tính (linear map) $r_{\phi}$: $\to E^{*}$ (tương đương, $l_{\phi}$: $E \to F^{*}$ và $r_{\phi}$: $F \to E^{*}$ là nửa tuyến tính (semilinear)). khái niệm của không suy biến dạng nửa tuyến tính (sesquilinear form) là đồng nhất đến khái niệm cho các dạng song tuyến tính. Cho convenience của độc giả, ta repeat định nghĩa.

> **Định nghĩa 29.10.** nửa tuyến tính (sesquilinear) ánh xạ $\phi$: $E \times  F \to K$ được nói là không suy biến khi và chỉ khi sau đây các điều kiện đúng:

<!-- PAGE 1022 -->
$(1)$ Với mọi $u \in E$, nếu $\phi (u, v) = 0$ với mọi $v \in F$, thì $u = 0$, và
$(2)$ Với mọi $v \in F$, nếu $\phi (u, v) = 0$ với mọi $u \in E$, thì $v = 0$. Mệnh đề 29.1 translates vào sau đây mệnh đề. chứng minh là để lại như một bài tập.

> **Mệnh đề 29.9.** Cho trước nửa tuyến tính (sesquilinear) ánh xạ $\phi$: $E \times  F \to K$, các tính chất sau đây đúng:
() ánh xạ $l_{\phi}$ là đơn ánh (injective) khi và chỉ khi Tính chất $(1)$ của Định nghĩa 29.10 nghiệm đúng.
$(b)$ ánh xạ $r_{\phi}$ là đơn ánh (injective) khi và chỉ khi Tính chất $(2)$ của Định nghĩa 29.10 nghiệm đúng.
$(c)$ dạng nửa tuyến tính (sesquilinear form) $\phi$ là không suy biến và khi và chỉ khi $l_{\phi}$ và $r_{\phi}$ là đơn ánh (injective).
$$(d) If the sesquillinear form \phi  is nondegenerate and \frac{if}{F} E and F have finite dimensions,$$
Thì dim(E) $=$ dim(F), và $l_{\phi}$: $\overline{E} \to F^{*}$ và $r_{\phi}$: $\to E^{*}$ là tuyến tính các đẳng cấu. Các mệnh đề 29.2 và 29.3 cũng tổng quát hóa đến các dạng nửa tuyến tính. Ta cũng có sau đây phiên bản của Định lý 29.4, có chứng minh là để lại như một bài tập.

> **Định lý 29.10.** Cho trước bất kỳ dạng nửa tuyến tính (sesquilinear form) $\phi$: $E \times  E \to K$ với dim(E) $= n$, nếu $\phi$ là Hermite và $K$ thực hiện không có characteristic $2$, thì có một cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $E$ sao cho $\phi (e_{i}, e_{j}) = 0$, với mọi $i \neq  j$. Như trong Mục 29.1, nếu $E$ và $F$ là hữu hạn chiều các không gian vectơ và nếu $(e_{1}, \dots  , e_{m})$ là cơ sở (basis) của $E$ và $(f_{1}, \dots  , f_{n})$ là cơ sở (basis) của $F$ thì sesquilinearity của $\phi$ cho ta
$$\phi \begin{pmatrix} x_{i}e_{i}, & y_{j}f_{j} \end{pmatrix} \sum_{i=1}^{m}  \sum_{j=1}^{n}  = \sum_{i=1j}^{m}  \sum_{=1}^{n}  x_{i}\phi (e_{i}, f_{j})\overline{y}_{j}.$$
Điều này chỉ ra rằng $\phi$ là hoàn toàn được xác định bởi ma trận cỡ $n \times  m$ $M = (m_{ij})$ với $m_{ij} = \phi (e_{j}, f_{i})$, và trong ma trận tạo thành, ta có
$$\phi (x, y) = x^{\top}M^{\top} \overline{y} = y^{*}Mx,$$
Ở đâu $x$ và $\overline{y}$ là các vectơ cột liên kết với $(x_{1}, \dots  , x_{m}) \in K^{m}$ và $(\overline{y}_{1}\overline{, \dots  , y}_{n}) \in K^{n}$, và $y^{*} = \overline{y}^{\top}$. Như trước đó, ta là committing slight abuse của ký hiệu của đặt $x$
$$denote both the vector x = \sum_{i}  n=1 x_{i}e_{i} and the column vector associated with (x_{1}, \dots  , x_{n})$$
(và tương tự cho $y)$.

> **Định nghĩa 29.11.** Nếu $(e_{1}, \dots  , e_{m})$ là cơ sở (basis) của $E$ và $(f_{1}, \dots  , f_{n})$ là cơ sở (basis) của $F$, với mọi dạng nửa tuyến tính (sesquilinear form) $\phi$: $E \times  F \to K$, ma trận cỡ $n \times  m$ $M = (m_{ij})$ cho trước bởi $m_{ij} = \phi (e_{j}, f_{i})$ cho $i = 1, \dots  , n$ và $j = 1, \dots  , m$ được gọi là ma trận của $\phi$ đối với các cơ sở $(e_{1}, \dots  , e_{m})$ và $(f_{1}, \dots  , f_{n})$.
