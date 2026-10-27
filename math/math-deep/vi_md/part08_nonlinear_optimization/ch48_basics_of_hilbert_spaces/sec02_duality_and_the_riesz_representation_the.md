# Đối ngẫu và Riesz Biểu diễn Định lý


<!-- PAGE 1694 -->
Vì vậy, các nghiệm của ban đầu bình phương tối thiểu (least-squares) bài toán là một cách chính xác các nghiệm của so-called chuẩn tắc/bình thường các phương trình
$$A^{\top}Ax = A^{\top}b,$$
Discovered bởi Gauss và Legendre xung quanh $1800$. Ta cũng được chứng minh rằng chuẩn tắc/bình thường các phương trình luôn luôn có nghiệm. một cách tính toán, nó là tốt nhất không để giải chuẩn tắc/bình thường các phương trình một cách trực tiếp, và thay vì, để sử dụng các phương pháp chẳng hạn như Phân rã QR (QR-decomposition) (ứng dụng đến $A)$ hoặc SVD-decomposition (trong tạo thành của nghịch đảo giả (pseudo-inverse)). Ta sẽ đến quay lại đến điều này điểm sau này. Ở đây là một cái khác quan trọng hệ quả của Mệnh đề 48.7.

> **Hệ quả 48.8.** Với mọi liên tục khác không ánh xạ tuyến tính (linear map) $h: E \to \mathbb{C}$, null không gian
$$H = \mathrm{Ker} h = {u \in E | h(u) = 0} = h^{-1}(0)$$
Là đóng siêu phẳng (hyperplane) $H$, và do đó, $H^{\perp}$ là không gian con có số chiều một sao cho $E = H\oplus H^{\perp}$. ở trên suggests định nghĩa không gian đối ngẫu (dual space) của $E$ như tập hợp tất cả liên tục các ánh xạ $h: E \to \mathbb{C}$.
Nhận xét: Nếu $h: E \to \mathbb{C}$ là ánh xạ tuyến tính (linear map) mà là không liên tục, thì nó có thể được được hiển thị rằng siêu phẳng (hyperplane) $H =$ Ker $h$ là trù mật trong $E$! Do đó, $H^{\perp}$ là rút gọn đến tầm thường không gian con
$$\mathbb{R}^{n}  \mathbb{C}^{n}$$
${0}$. Điều này đi chống lại của ta trực giác của những gì siêu phẳng (hyperplane) trong (hoặc) là, và warns chúng ta không đến trust của ta “vật lý” trực giác cũng nhiều khi dealing với vô hạn số chiều. Hệ quả là, ánh xạ $\flat$: $E \to E^{*}$ đã giới thiệu trong Mục 14.2 (xem chỉ sau Định nghĩa 48.4 ở dưới) là không toàn ánh (surjective), vì các dạng tuyến tính của tạo thành $u \mapsto \langle u, v\rangle$ (với một số cố định vectơ $v \in E)$ là liên tục (tích vô hướng (inner product) là liên tục).

## 48.2 Đối ngẫu và Riesz Biểu diễn Định lý

Ta bây giờ chỉ ra rằng bởi redefining không gian đối ngẫu (dual space) của Không gian Hilbert (Hilbert space) như tập hợp của liên tục các dạng tuyến tính trên $E$ ta recover Định lý 14.6.

> **Định nghĩa 48.4.** Cho trước Không gian Hilbert (Hilbert space) $E$, ta định nghĩa không gian đối ngẫu (dual space) E' của $E$ như vectơ
$$\mathbb{C}$$
Không gian của tất cả liên tục các dạng tuyến tính $h: E \to$. Các ánh xạ trong E' cũng được gọi là bị chặn tuyến tính các toán tử, bị chặn tuyến tính các phiếm hàm, hoặc đơn giản các toán tử hoặc các phiếm hàm. Như trong Mục 14.2, với mọi $u, v \in E$, ta định nghĩa các ánh xạ $\phi_{u}^{l}$: $E \to \mathbb{C}$ và $\phi_{v}^{r}$: $E \to \mathbb{C}$ sao cho
$$\phi_{u}^{l} (v) =\overline{\langle}\overline{u, v}\overline{\rangle},$$
Và
$$\phi_{v}^{r} (u) = \langle u, v\rangle .$$

<!-- PAGE 1695 -->
Thực ra, $\phi_{u}^{l}  = \phi_{u}^{r}$, và bởi vì tích vô hướng (inner product) $\langle$ -, $-\rangle$ là liên tục, hiển nhiên là $\phi_{v}^{r}$ là liên tục và tuyến tính, sao cho $\phi_{v}^{r}  \in$ E'. để đơn giản hóa ký hiệu, ta viết $\phi_{v}$ thay vì của $\phi_{v}^{r}$. Định lý 14.6 là suy rộng/tổng quát hóa đến Các không gian Hilbert như sau.

> **Mệnh đề 48.9.** (Riesz biểu diễn định lý) Cho $E$ là Không gian Hilbert (Hilbert space). Thì ánh xạ $\flat$: $E \to$ E' được định nghĩa sao cho
$$\flat (v) = \phi_{v} ,$$
Là nửa tuyến tính (semilinear), liên tục, và song ánh (bijective). Hơn nữa, với mọi liên tục ánh xạ tuyến tính (linear map) $\psi  \in$ E', nếu $u \in E$ là duy nhất vectơ sao cho
$$\psi (v) = \langle v, u\rangle for all v \in E,$$
Thì ta có $\|\psi \| = \|u\|$, ở đâu
$$|$$
$$|



$$
$$\|\psi \|= \sup \frac{\psi (v)}{\|v\|} v \in E, v \neq  0.$$

*Chứng minh.* chứng minh là basically đồng nhất đến chứng minh của Định lý 14.6, ngoại trừ rằng khác nhau lập luận là cần thiết cho tính toàn ánh của $\flat$: $E \to$ E', vì $E$ có thể không là hữu hạn dimensional. Với mọi khác không tuyến tính toán tử $h \in$ E', siêu phẳng (hyperplane) $H =$ Ker $h = h^{-1}(0)$ là đóng không gian con của $E$, và theo Mệnh đề 48.7, $H^{\perp}$ là không gian con có số chiều một sao cho $E = H \oplus H^{\perp}$. Thì chọn bất kỳ khác không vectơ $w \in H^{\perp}$, nhận thấy rằng $H$ là cũng hạt nhân (kernel) của tuyến tính toán tử $\phi_{w}$, với
$$\phi_{w} (u) = \langle u, w\rangle ,$$
Và do đó, vì bất kỳ hai khác không các dạng tuyến tính định nghĩa cùng siêu phẳng (hyperplane) phải là tỷ lệ, tồn tại một khác không vô hướng (scalar) $\lambda  \in \mathbb{C}$ sao cho $h = \lambda \phi_{w}$. Nhưng khi đó, $h = \overline{\phi}_{\lambda w}$, chứng minh rằng $\flat$: $E \to$ E' là toàn ánh (surjective). Bởi Cauchy–Schwarz bất đẳng thức ta có
$$|\psi (v)| = |\langle v, u\rangle | \le \|v\|\|u\|,$$
Do đó theo định nghĩa của $\|\psi \|$ ta thu được
$$\|\psi \|\le \|u\|.$$
Hiển nhiên $\psi  = 0$ khi và chỉ khi $u = 0$ do đó giả sử $u \neq  0$. Ta có
$$\|u\|^{2}= \langle u, u\rangle = \psi (u) \le \|\psi \|\|u\|,$$
Mà cho ta $\|u\|\le \|\psi \|$, và vì vậy $\|\psi \| = \|u\|$, như đã khẳng định. Mệnh đề 48.9 là đã biết như Riesz biểu diễn định lý hoặc “Little Riesz Định lý.” Nó chỉ ra rằng tích vô hướng (inner product) trên Không gian Hilbert (Hilbert space) cảm sinh tự nhiên nửa tuyến tính (semilinear) đẳng cấu giữa $E$ và đối ngẫu (đối ngẫu (dual)) của nó E' (tương đương, tuyến tính đẳng cấu giữa $\overline{E}$ và E'). đẳng cấu này là phép đẳng cự (isometry) (nó là bảo toàn chuẩn (norm)).

<!-- PAGE 1696 -->
Nhận xét: Nhiều các cuốn sách trên quantum cơ học sử dụng so-called Dirac ký hiệu đến ký hiệu objects trong Không gian Hilbert (Hilbert space) $E$ và các toán tử trong đối ngẫu (đối ngẫu (dual)) của nó không gian E'. Trong Dirac ký hiệu, phần tử của $E$ được ký hiệu là như $|x\rangle$, và phần tử của E' được ký hiệu là như $\langle$ t|. vô hướng (scalar) tích được ký hiệu là như $\langle$ t| $\cdot  |x\rangle$. Điều này sử dụng đẳng cấu giữa $E$ và E', ngoại trừ rằng tích vô hướng (inner product) được giả sử là semi-linear trên trái thay vì trên phải. Mệnh đề 48.9 cho phép chúng ta để định nghĩa liên hợp (adjoint) của ánh xạ tuyến tính (linear map), như trong Hermite trường hợp (xem Mệnh đề 14.8). Thực sự, ta có thể chứng minh slightly nhiều hơn/thêm tổng quát kết quả mà được sử dụng trong tối ưu hóa lý thuyết. Nếu $\phi$: $E\times E \to \mathbb{C}$ là nửa tuyến tính (sesquilinear) ánh xạ trên không gian vectơ định chuẩn (normed vector space) $(E, \|\|)$, thì Mệnh đề 37.59 là ngay lập tức được điều chỉnh để chứng minh rằng $\phi$ là liên tục khi và chỉ khi tồn tại một hằng số $k \ge 0$ sao cho
$$|\phi (u, v)| \le k \|u\|\|v\|for all u, v \in E.$$
Do đó ta định nghĩa $\|\phi \|$ như trong Định nghĩa 37.42 bởi
$$\|\phi \|= \sup {|\phi (x, y)| | \|x\|\le 1, \|y\|\le 1, x, y \in E} .$$

> **Mệnh đề 48.10.** Cho trước Không gian Hilbert (Hilbert space) $E$, với mọi liên tục nửa tuyến tính (sesquilinear) ánh xạ $\phi$: $E \times E \to \mathbb{C}$, tồn tại duy nhất một liên tục ánh xạ tuyến tính (linear map) $f_{\phi}$: $E \to E$, sao cho
$$\phi (u, v) = \langle u, f_{\phi}(v)\rangle for all u, v \in E.$$
Ta cũng có $\|f_{\phi}\| = \|\phi \|$. Nếu $\phi$ là Hermite, thì $f_{\phi}$ là tự liên hợp (self-adjoint), nghĩa là
$$\langle u, f_{\phi}(v)\rangle = \langle f_{\phi}(u), v\rangle for all u, v \in E.$$

*Chứng minh.* chứng minh được điều chỉnh từ Rudin $[146]$ (Định lý 12.8). để định nghĩa hàm $f_{\phi}$, ta tiến hành như sau. Với mọi cố định $v \in E$, định nghĩa ánh xạ tuyến tính (linear map) $\phi_{v}$ bởi
$$\phi_{v} (u) = \phi (u, v)for all u \in E.$$
Vì $\phi$ là liên tục, $\phi_{v}$ là liên tục. Do đó theo Mệnh đề 48.9, tồn tại duy nhất một vectơ trong $E$ rằng ta ký hiệu $f_{\phi}(v)$ sao cho
$$\phi_{v} (u) = \langle u, f_{\phi}(v)\rangle for all u \in E,$$
Và $\|f_{\phi}(v)\| = \|\phi_{v} \|$. Cho chúng ta kiểm tra rằng ánh xạ $v \mapsto f_{\phi}(v)$ là tuyến tính. Ta có
$$\phi (u, v_{1} + v_{2}) = \phi (u, v_{1}) + \phi (u, v_{2})\phi  is additive$$
$$= \langle u, f_{\phi}(v_{1})\rangle + \langle u, f_{\phi}(v_{2})\rangle by definition of f_{\phi}$$
$$= \langle u, f_{\phi}(v_{1}) + f_{\phi}(v_{2})\rangle \langle -, -\rangle is additive$$

<!-- PAGE 1697 -->
Với mọi $u \in E$, và vì $f_{\phi}(v_{1}+v_{2})$ là duy nhất vectơ sao cho $\phi (u, v_{1}+v_{2}) = \langle u, f_{\phi}(v_{1}+v_{2})\rangle$ với mọi $u \in E$, ta phải có
$$f_{\phi}(v_{1} + v_{2}) = f_{\phi}(v_{1}) + f_{\phi}(v_{2}).$$
Với mọi $\lambda  \in \mathbb{C}$ ta có
$$\phi (u, \lambda v) =\overline{\lambda \phi}(u, v)\phi  is sesquilinear$$
$$=\overline{\lambda}\langle u, f_{\phi}(v)\rangle by definition of f_{\phi}$$
$$= \langle u, \lambda f_{\phi}(v)\rangle \langle -, -\rangle is sesquilinear$$
Với mọi $u \in E$, và vì $f_{\phi}(\lambda v)$ là duy nhất vectơ sao cho $\phi (u, \lambda v) = \langle u, f_{\phi}(\lambda v)\rangle$ với mọi $u \in E$, ta phải có
$$f_{\phi}(\lambda v) = \lambda f_{\phi}(v).$$
Vì vậy $f_{\phi}$ là tuyến tính. Thì theo định nghĩa của $\|\phi \|$, ta có
$$|\phi_{v} (u)| = |\phi (u, v)| \le \|\phi \|\|u\|\|v\|,$$
Mà chỉ ra rằng $\|\phi_{v} \|\le \|\phi \|\|v\|$. Vì $\|f_{\phi}(v)\| = \|\phi_{v} \|$, ta có
$$\|f_{\phi}(v)\|\le \|\phi \|\|v\|,$$
Mà chỉ ra rằng $f_{\phi}$ là liên tục và rằng $\|f_{\phi}\|\le \|\phi \|$. Nhưng bởi Cauchy–Schwarz bất đẳng thức ta cũng có
$$|\phi (u, v)| = |\langle u, f_{\phi}(v)\rangle | \le \|u\|\|f_{\phi}(v)\|\le \|u\|\|f_{\phi}\|\|v\|,$$
Do đó $\|\phi \|\le \|f_{\phi}\|$, và do đó
$$\|f_{\phi}\|= \|\phi \|.$$
Nếu $\phi$ là Hermite, $\phi (v, u) =\overline{\phi}\overline{(}\overline{u, v}\overline{),}$ do đó
$$\langle f_{\phi}(u), v\rangle =\overline{\langle}\overline{v, f}_{\phi}\overline{(}\overline{u}\overline{)}\overline{\rangle}=\overline{\phi}\overline{(}\overline{v, u}\overline{) =} \phi (u, v) = \langle u, f_{\phi}(v)\rangle ,$$
Mà chỉ ra rằng $f_{\phi}$ là tự liên hợp (self-adjoint).

> **Mệnh đề 48.11.** Cho trước Không gian Hilbert (Hilbert space) $E$, với mọi liên tục ánh xạ tuyến tính (linear map) $f$: $E \to E$, tồn tại duy nhất một liên tục ánh xạ tuyến tính (linear map) $f^{*}$: $E \to E$, sao cho
$$\langle f(u), v\rangle = \langle u, f^{*} (v)\rangle for all u, v \in E,$$
Và ta có $\|f^{*} \| = \|f\|$. ánh xạ $f^{*}$ được gọi là liên hợp (adjoint) của $f$.

<!-- PAGE 1698 -->

*Chứng minh.* chứng minh được điều chỉnh từ Rudin $[146]$ (Mục 12.9). Bởi Cauchy–Schwarz bất đẳng thức, vì
$$|\langle x, y\rangle | \le \|x\|\|y\|,$$
Ta xem rằng nửa tuyến tính (sesquilinear) ánh xạ $(x, y) \mapsto \langle x, y\rangle$ trên $E \times  E$ là liên tục. Cho $\phi$: $E \times  E \to \mathbb{C}$ là nửa tuyến tính (sesquilinear) ánh xạ cho trước bởi
$$\phi (u, v) = \langle f(u), v\rangle for all u, v \in E.$$
Vì $f$ là liên tục và tích vô hướng (inner product) $\langle$ -, $-\rangle$ là liên tục, điều này là ánh xạ liên tục (continuous map). Theo Mệnh đề 48.10, tồn tại duy nhất một ánh xạ tuyến tính (linear map) $f^{*}$: $E \to E$ sao cho
$$\langle f(u), v\rangle = \phi (u, v) = \langle u, f^{*} (v)\rangle for all u, v \in E,$$
Với $\|f^{*} \| = \|\phi \|$. Ta có thể cũng chứng minh rằng $\|\phi \| = \|f\|$. Thứ nhất, theo định nghĩa của $\|\phi \|$ ta có
$$\|\phi \|= \sup {|\phi (x, y)| | \|x\|\le 1, \|y\|\le 1}$$
$$= \sup {|\langle f(x), y\rangle | | \|x\|\le 1, \|y\|\le 1}$$
$$\le \sup {\|f(x)\|\|y\|| \|x\|\le 1, \|y\|\le 1}$$
$$\le \sup {\|f(x)\|| \|x\|\le 1}$$
$$= \|f\|.$$
Trong khác hướng ta có
$$\|f(x)\|^{2}= \langle f(x), f(x)\rangle = \phi (x, f(x)) \le \|\phi \|\|x\|\|f(x)\|,$$
Và nếu f(x) $\neq  0$ ta thu được $\|f(x)\|\le \|\phi \|\|x\|$. bất đẳng thức này nghiệm đúng một cách tầm thường nếu f(x) $= 0$, do đó ta kết luận rằng $\|f\|\le \|\phi \|$. Vì vậy ta có
$$\|\phi \|= \|f\|,$$
Như đã khẳng định, và hệ quả là $\|f^{*} \| = \|\phi \| = \|f\|$. Nó là dễ để chỉ ra rằng liên hợp (adjoint) thỏa mãn các tính chất sau đây:
$$(f + g)^{*}= f^{*} + g^{*}$$
$$(\lambda f)^{*}=\overline{\lambda f}^{*}$$
$$(f \circ g)^{*}= g^{*}\circ f^{*}$$
$$f^{**} = f.$$
Một có thể cũng chỉ ra rằng $\|f^{*} \circ f\| = \|f\|^{2}$ (xem Rudin $[146]$, Mục 12.9). Như trong Hermite trường hợp, cho trước hai Các không gian Hilbert $E$ và $F$, ở trên các kết quả có thể được được điều chỉnh để chỉ ra rằng với mọi ánh xạ tuyến tính (linear map) $f$: $E \to F$, tồn tại duy nhất một ánh xạ tuyến tính (linear map) $f^{*}$: $F \to E$ sao cho
$$\langle f(u), v\rangle_{2}  = \langle u, f^{*} (v)\rangle_{1}$$
Với mọi $u \in E$ và tất cả $v \in F$. ánh xạ tuyến tính (linear map) $f^{*}$ cũng được gọi là liên hợp (adjoint) của $f$.
