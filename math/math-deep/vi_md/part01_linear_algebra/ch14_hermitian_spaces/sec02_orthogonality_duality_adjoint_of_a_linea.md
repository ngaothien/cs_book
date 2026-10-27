# Tính trực giao, Đối ngẫu, Liên hợp (adjoint) của Ánh xạ tuyến tính (linear map)


<!-- PAGE 538 -->
Chỉ ra rằng $\phi$: $E \times  E \to \mathbb{C}$ là liên tục, và do đó, rằng $\|\|$ là liên tục. Nếu $\langle E, \phi \rangle$ là chỉ pre-Hilbertian, $\|u\|$ được gọi là một seminorm. Trong trường hợp này, điều kiện
$$\|u\|= 0impliesu = 0$$
Là không nhất thiết đúng. Tuy nhiên, Cauchy–Schwarz bất đẳng thức chỉ ra rằng nếu $\|u\| = 0$, thì $u \cdot  v = 0$ với mọi $v \in E$.
Nhận xét: Như trong trường hợp của thực các không gian vectơ, chuẩn (norm) trên phức không gian vectơ (vector space) được cảm sinh bởi một số xác định dương (positive definite) Hermite tích $\langle$ -, $-\rangle$ khi và chỉ khi nó thỏa mãn hình bình hành luật:
$$\|u + v\|^{2}+ \|u -v\|^{2}= 2(\|u\|^{2}+ \|v\|^{2}).$$
Điều này time Hermite tích là recovered bằng cách sử dụng phân cực đồng nhất thức từ Mệnh đề 14.1:
$$4\langle u, v\rangle = \|u + v\|^{2}-\|u -v\|^{2}+ i \|u + iv\|^{2}-i \|u -iv\|^{2}.$$
Nó là dễ để kiểm tra rằng $\langle u, u\rangle = \|u\|^{2}$, và
$$\langle v, u\rangle =\overline{\langle}\overline{u, v}\overline{\rangle}$$
$$\langle iu, v\rangle = i\langle u, v\rangle ,$$
Do đó nó là đủ để kiểm tra tính tuyến tính trong biến $u$, và chỉ cho thực các vô hướng. Điều này là dễ dàng được thực hiện bằng cách áp dụng chứng minh từ Mục 12.1 đến thực và imaginary phần của $\langle u, v\rangle$; chi tiết là để lại như một bài tập. Ta sẽ bây giờ basically mirror trình bày của Euclidean hình học cho trước trong Chương $12$ khá quickly, để lại ra hầu hết các chứng minh, ngoại trừ khi chúng cần là seriously amended.

## 14.2 Tính trực giao, Đối ngẫu, Liên hợp (adjoint) của Ánh xạ tuyến tính (linear map)

Trong mục này ta giả sử rằng ta là dealing với Các không gian Hermite. Ta ký hiệu Hermite tích vô hướng (inner product) bởi $u \cdot  v$ hoặc $\langle u, v\rangle$. các khái niệm của tính trực giao, họ trực giao (orthogonal family) của các vectơ, họ trực chuẩn (orthonormal family) của các vectơ, và phần bù trực giao (orthogonal complement) của tập hợp của các vectơ là unchanged từ Euclidean trường hợp (Định nghĩa 12.2). Ví dụ, tập hợp $\mathcal{C}[-\pi , \pi$ ] của liên tục các hàm $f$: $[-\pi , \pi$ ] $\to \mathbb{C}$ là Không gian Hermite (Hermitian space) dưới tích
$$\langle f, g\rangle = \int_{-}^{}  \pi f(x)\overline{g}\overline{(}\overline{x}\overline{)} dx,$$
$$\pi$$
Và họ $(e^{ikx})_{k\in Z}$ là trực giao. Các mệnh đề 12.4 và 12.5 đúng mà không có bất kỳ thay đổi. Nó là dễ để chỉ ra rằng
$$2$$
$$\sum_{i=1}^{n}  u_{i}= \sum_{i=1}^{n}  \|u_{i}\|^{2}+ \sum_{\le i<j\le}  2\mathcal{ℜ}(u_{i} \cdot  u_{j}).$$
$$1n$$

<!-- PAGE 539 -->
Một cách tương tự đến trường hợp của Các không gian Euclid của hữu hạn số chiều, Hermite tích cảm sinh chính tắc song ánh (i.e., độc lập của lựa chọn của các cơ sở) giữa không gian vectơ (vector space) $E$ và không gian $E^{*}$. Điều này là một của places ở đâu liên hợp chỉ ra lên, nhưng trong trường hợp này, troubles là định thức con (minor). Cho trước Không gian Hermite (Hermitian space) $E$, với mọi vectơ $u \in E$, cho $\phi_{u}^{l}$: $E \to \mathbb{C}$ là ánh xạ được định nghĩa sao cho
$$\phi_{u}^{l} (v) =\overline{u}\overline{\cdot}\overline{v,} for all v \in E.$$
Tương tự, với mọi vectơ $v \in E$, cho $\phi_{v}^{r}$: $E \to \mathbb{C}$ là ánh xạ được định nghĩa sao cho
$$\phi_{v}^{r} (u) = u \cdot  v,for all u \in E.$$
Vì Hermite tích là tuyến tính trong của nó thứ nhất lập luận $u$, ánh xạ $\phi_{v}^{r}$ là dạng tuyến tính (linear form) trong $E^{*}$, và vì nó là nửa tuyến tính (semilinear) trong của nó thứ hai lập luận $v$, ánh xạ $\phi_{u}^{l}$ là cũng dạng tuyến tính (linear form) trong $E^{*}$. Do đó, ta có hai các ánh xạ $\flat^{l}$: $E \to E^{*}$ và $\flat^{r}$: $E \to E^{*}$, được định nghĩa sao cho
$$\flat^{l} (u) = \phi_{u}^{l} ,and\flat^{r} (v) = \phi_{v}^{r} .$$

> **Mệnh đề 14.5.** các phương trình $\phi_{u}^{l}  = \phi_{u}^{r}$ và $\flat^{l} = \flat^{r}$ đúng.

*Chứng minh.* Thật vậy, với mọi $u, v \in E$, ta có
$$\flat^{l} (u)(v) = \phi_{u}^{l} (v)$$
$$=\overline{u}\overline{\cdot}\overline{v}$$
$$= v \cdot  u$$
$$= \phi_{u}^{r} (v)$$
$$= \flat^{r} (u)(v).$$
Vì vậy, ta sử dụng ký hiệu $\phi_{u}$ cho cả hai $\phi_{u}^{l}$ và $\phi_{u}^{r}$, và $\flat$ cho cả hai $\flat^{l}$ và $\flat^{r}$.

> **Định lý 14.6.** Cho $E$ là Không gian Hermite (Hermitian space) $E$. ánh xạ $\flat$: $E \to E^{*}$ được định nghĩa sao cho
$$\flat (u) = \phi_{u}^{l}  = \phi_{u}^{r} for all u \in E$$
Là nửa tuyến tính (semilinear) và đơn ánh (injective). Khi $E$ là cũng của hữu hạn số chiều, ánh xạ $\flat$: $\overline{E} \to E^{*}$ là chính tắc đẳng cấu.

*Chứng minh.* Rằng $\flat$: $E \to E^{*}$ là nửa tuyến tính (semilinear) ánh xạ suy ra ngay lập tức từ sự kiện rằng $\flat = \flat^{r}$, và rằng Hermite tích là nửa tuyến tính (semilinear) trong của nó thứ hai lập luận. Nếu $\phi_{u}  = \phi_{v}$, thì $\phi_{u} (w) = \phi_{v} (w)$ với mọi $w \in E$, mà theo định nghĩa của $\phi_{u}$ và $\phi_{v}$ có nghĩa là
$$w \cdot  u = w \cdot  v$$
Với mọi $w \in E$, mà bởi semilinearity trên phải là tương đương đến
$$w \cdot  (v -u) = 0for all w \in E,$$
Mà suy ra rằng $u = v$, vì Hermite tích là xác định dương (positive definite). Do đó, $\flat$: $E \to E^{*}$
$$is injective. Finally, when E is of finite dimension n, \frac{E^{*}}{E} is also of dimension n, and then$$
$\flat$: $E \to E^{*}$ là song ánh (bijective). Vì $\flat$ là semilinar, ánh xạ $\flat$: $\to E^{*}$ là đẳng cấu.

<!-- PAGE 540 -->
Nghịch đảo của đẳng cấu $\flat$: $\overline{E} \to E^{*}$ được ký hiệu bởi $\sharp$: $E^{*} \to \overline{E}$. Như hệ quả của đẳng cấu $\flat$: $\overline{E} \to E^{*}$ ta có kết quả sau kết quả.

> **Mệnh đề 14.7.** Nếu $E$ là Không gian Hermite (Hermitian space) của hữu hạn số chiều, thì mọi dạng tuyến tính (linear form) $f \in E^{*}$ tương ứng với duy nhất $v \in E$, sao cho
$$f(u) = u \cdot  v,for every u \in E.$$
Đặc biệt, nếu $f$ là không không tạo thành, hạt nhân (kernel) của $f$, mà là siêu phẳng (hyperplane) $H$, là một cách chính xác tập hợp của các vectơ rằng là trực giao đến $v$.
Các nhận xét: $1$. “musical ánh xạ” $\flat$: $\overline{E} \to E^{*}$ là không toàn ánh (surjective) khi $E$ có vô hạn số chiều. kết quả này có thể được salvaged bởi thu hẹp của ta attention đến liên tục các ánh xạ tuyến tính (linear maps) và bởi giả sử rằng không gian vectơ (vector space) $E$ là Không gian Hilbert (Hilbert space). $2$. Dirac’s “bra-ket” ký hiệu. Dirac invented ký hiệu widely được sử dụng trong quantum cơ học cho ký hiệu dạng tuyến tính (linear form) $\phi_{u}  = \flat (u)$ liên kết với vectơ $u \in E$ thông qua đối ngẫu được cảm sinh bởi Hermite tích vô hướng (inner product). Dirac’s proposal là đến ký hiệu các vectơ $u$ trong $E$ bởi $|u\rangle$, và gọi chúng kets; ký hiệu $|u\rangle$ là pronounced “ket u.” Cho trước hai kets (các vectơ) $|u\rangle$ và $|v\rangle$, của chúng tích vô hướng (inner product) được ký hiệu bởi
$$\langle u|v\rangle$$
(thay vì của $|u\rangle \cdot |v\rangle$). ký hiệu $\langle u|v\rangle$ cho tích vô hướng (inner product) của $|u\rangle$ và $|v\rangle$ anticipates đối ngẫu. Thật vậy, ta định nghĩa đối ngẫu (dual) (thường được gọi là liên hợp (adjoint)) bra $u$ của ket $u$, được ký hiệu bởi $\langle$ u|, như dạng tuyến tính (linear form) có giá trị trên bất kỳ ket $v$ được cho bởi tích vô hướng (inner product), do đó
$$\langle u|(|v\rangle ) = \langle u|v\rangle .$$
Do đó, bra $u = \langle$ u| là Dirac’s ký hiệu cho của ta $\flat (u)$. Vì ánh xạ $\flat$ là semi-linear, ta có
$$\langle \lambda u| =\overline{\lambda}\langle u|.$$
Bằng cách sử dụng bra-ket ký hiệu, cho trước cơ sở trực chuẩn (orthonormal basis) $(|u_{1}\rangle , \dots  , |u_{n}\rangle$), ket $v$ (vectơ) được viết như
$$|v\rangle = \sum_{i=1}^{n}  \langle v|u_{i}\rangle |u_{i}\rangle ,$$
Và tương ứng dạng tuyến tính (linear form) bra $v$ được viết như
$$\langle v| = \sum_{i=1}^{n}  \overline{\langle}\overline{v}\overline{|}\overline{u}_{i}\overline{\rangle \langle} u_{i}| = \sum_{i=1}^{n}  \langle u_{i}|v\rangle \langle u_{i}|$$
Trên đối ngẫu (dual) cơ sở (basis) $(\langle u_{1}|, \dots  , \langle u_{n}|)$. Như cute như nó trông, ta thực hiện không recommend bằng cách sử dụng Dirac ký hiệu.

<!-- PAGE 541 -->
Sự tồn tại của đẳng cấu $\flat$: $\overline{E} \to E^{*}$ là then chốt đến sự tồn tại của liên hợp (adjoint) các ánh xạ. Thật vậy, Định lý 14.6 cho phép chúng ta để định nghĩa liên hợp (adjoint) của ánh xạ tuyến tính (linear map) trên Không gian Hermite (Hermitian space). Cho $E$ là Không gian Hermite (Hermitian space) của hữu hạn số chiều $n$, và cho $f$: $E \to E$ là ánh xạ tuyến tính (linear map). Với mọi $u \in E$, ánh xạ
$$v \mapsto \overline{u}\overline{\cdot}\overline{f}\overline{(}\overline{v}\overline{)}$$
Là rõ ràng dạng tuyến tính (linear form) trong $E^{*}$, và theo Định lý 14.6, tồn tại duy nhất một vectơ trong $E$ được ký hiệu bởi $f^{*} (u)$, sao cho
$$\overline{f}^{*} \overline{(}\overline{u}\overline{)}\overline{\cdot}\overline{v} =\overline{u}\overline{\cdot}\overline{f}\overline{(}\overline{v}\overline{)},$$
Rằng là,
$$f^{*} (u) \cdot  v = u \cdot  f(v),for every v \in E.$$
Sau đây mệnh đề chỉ ra rằng ánh xạ $f^{*}$ là tuyến tính.

> **Mệnh đề 14.8.** Cho trước Không gian Hermite (Hermitian space) $E$ của hữu hạn số chiều, với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$ tồn tại duy nhất một ánh xạ tuyến tính (linear map) $f^{*}$: $E \to E$ sao cho
$$f^{*} (u) \cdot  v = u \cdot  f(v),for all u, v \in E.$$

*Chứng minh.* Careful inspection của chứng minh của Mệnh đề 12.8 reveals rằng nó áp dụng unchanged. chỉ potential bài toán là trong chứng minh rằng $f^{*} (\lambda u) = \lambda f^{*} (u)$, nhưng everything lấy place trong thứ nhất lập luận của Hermite tích, và ở đó, ta có tính tuyến tính.

> **Định nghĩa 14.6.** Cho trước Không gian Hermite (Hermitian space) $E$ của hữu hạn số chiều, với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$, duy nhất ánh xạ tuyến tính (linear map) $f^{*}$: $E \to E$ sao cho
$$f^{*} (u) \cdot  v = u \cdot  f(v),for all u, v \in E$$
Cho trước theo Mệnh đề 14.8 được gọi là liên hợp (adjoint) của $f$ (w.r.t. đến Hermite tích). sự kiện rằng
$$v \cdot  u =\overline{u}\overline{\cdot}\overline{v}$$
Suy ra rằng liên hợp (adjoint) $f^{*}$ của $f$ cũng được đặc trưng hóa bởi
$$f(u) \cdot  v = u \cdot  f^{*} (v),$$
Với mọi $u, v \in E$. Cho trước hai Các không gian Hermite $E$ và $F$, ở đâu Hermite tích trên $E$ được ký hiệu bởi $\langle$ -, $-\rangle_{1}$ và Hermite tích trên $F$ được ký hiệu bởi $\langle$ -, $-\rangle_{2}$, cho trước bất kỳ ánh xạ tuyến tính (linear map) $f$: $E \to F$, ta kiểm chứng được ngay rằng chứng minh của Mệnh đề 14.8 có thể được được điều chỉnh để chỉ ra rằng tồn tại duy nhất một ánh xạ tuyến tính (linear map) $f^{*}$: $F \to E$ sao cho
$$\langle f(u), v\rangle_{2}  = \langle u, f^{*} (v)\rangle_{1}$$
Với mọi $u \in E$ và tất cả $v \in F$. ánh xạ tuyến tính (linear map) $f^{*}$ cũng được gọi là liên hợp (adjoint) của $f$. Như trong Euclidean trường hợp, các tính chất sau đây ngay lập tức suy ra từ định nghĩa của liên hợp (adjoint) ánh xạ.

<!-- PAGE 542 -->

> **Mệnh đề 14.9.**
$(1)$ Với mọi ánh xạ tuyến tính (linear map) $f$: $E \to F$, ta có
$$f^{**} = f.$$
$(2)$ Với mọi hai các ánh xạ tuyến tính (linear maps) $f, g: E \to F$ và bất kỳ vô hướng (scalar) $\lambda  \in \mathbb{R}$:
$$(f + g)^{*}= f^{*} + g^{*}$$
$$(\lambda f)^{*}=\overline{\lambda f}^{*} .$$
$(3)$ Nếu $E, F, G$ là Các không gian Hermite với respective trong các tích $\langle$ -, $-\rangle_{1} , \langle$ -, $-\rangle_{2}$, và $\langle$ -, $-\rangle_{3}$, và nếu $f$: $E \to F$ và $g: F \to G$ là hai các ánh xạ tuyến tính (linear maps), thì
$$(g \circ f)^{*}= f^{*} \circ g^{*}.$$
Như trong Euclidean trường hợp, ánh xạ tuyến tính (linear map) $f$: $E \to E$ (ở đâu $E$ là hữu hạn chiều Không gian Hermite (Hermitian space)) là tự liên hợp (self-adjoint) nếu $f = f^{*}$. ánh xạ $f$ là nửa xác định dương (positive semidefinite) khi và chỉ khi
$$\langle f(x), x\rangle \ge 0all x \in E;$$
Xác định dương (positive definite) khi và chỉ khi
$$\langle f(x), x\rangle > 0all x \in E, x \neq  0.$$
Thú vị hệ quả của Mệnh đề 14.3 là rằng nửa xác định dương (positive semidefinite) ánh xạ tuyến tính (linear map) phải là tự liên hợp (self-adjoint). Thực ra, ta có thể chứng minh slightly nhiều hơn/thêm tổng quát kết quả.

> **Mệnh đề 14.10.** Cho trước bất kỳ hữu hạn chiều Không gian Hermite (Hermitian space) $E$ với Hermite tích $\langle$ -, $-\rangle$, với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$, nếu $\langle$ f(x), $x\rangle \in \mathbb{R}$ với mọi $x \in E$, thì $f$ là tự liên hợp (self-adjoint). Đặc biệt, bất kỳ nửa xác định dương (positive semidefinite) ánh xạ tuyến tính (linear map) $f$: $E \to E$ là tự liên hợp (self-adjoint).

*Chứng minh.* Vì $\langle$ f(x), $x\rangle \in \mathbb{R}$ với mọi $x \in E$, ta có
$$\langle f(x), x\rangle =\overline{\langle}\overline{f}\overline{(}\overline{x}\overline{)}\overline{, x}\overline{\rangle}$$
$$= \langle x, f(x)\rangle$$
$$= \langle f^{*} (x), x\rangle ,$$
Do đó ta có
$$\langle (f -f^{*} )(x), x\rangle = 0all x \in E,$$
Và Mệnh đề 14.3 suy ra rằng $f$ - $f^{*} = 0$. Beware rằng Mệnh đề 14.10 là sai nếu $E$ là thực Không gian Euclid (Euclidean space). Như trong Euclidean trường hợp, Định lý 14.6 có thể được được sử dụng để chỉ ra rằng bất kỳ Không gian Hermite (Hermitian space) của hữu hạn số chiều có cơ sở trực chuẩn (orthonormal basis). chứng minh là unchanged.

<!-- PAGE 543 -->

> **Mệnh đề 14.11.** Cho trước bất kỳ không tầm thường Không gian Hermite (Hermitian space) $E$ của hữu hạn số chiều $n \ge 1$, có một cơ sở trực chuẩn (orthonormal basis) $(u_{1}, \dots  , u_{n})$ cho $E$. Gram–Schmidt trực chuẩn hóa quy trình cũng áp dụng đến Các không gian Hermite của hữu hạn số chiều, mà không có bất kỳ thay đổi từ Euclidean trường hợp!

> **Mệnh đề 14.12.** Cho trước không tầm thường Không gian Hermite (Hermitian space) $E$ của hữu hạn số chiều $n \ge 1$, từ bất kỳ cơ sở (basis) $(e_{1}, \dots  , e_{n})$ cho $E$ ta có thể xây dựng cơ sở trực chuẩn (orthonormal basis) $(u_{1}, \dots  , u_{n})$ cho $E$ với tính chất rằng với mọi $k, 1 \le k \le n$, các họ $(e_{1}, \dots  , e_{k})$ và $(u_{1}, \dots  , u_{k})$ sinh cùng không gian con.
Nhận xét: các nhận xét được tạo sau Mệnh đề 12.10 cũng áp dụng ở đây, ngoại trừ rằng trong Phân rã QR (QR-decomposition), $Q$ là ma trận unita (unitary matrix). Hệ quả là của Mệnh đề 12.9 (hoặc Mệnh đề 14.12), cho trước bất kỳ Không gian Hermite (Hermitian space) của hữu hạn số chiều $n$, nếu $(e_{1}, \dots  , e_{n})$ là cơ sở trực chuẩn (orthonormal basis) cho $E$, thì với mọi hai các vectơ $u = u_{1}e_{1} + \cdots  + u_{n}e_{n}$ và $v = v_{1}e_{1} + \cdots  + v_{n}e_{n}$, Hermite tích $u \cdot  v$ được biểu diễn như
$$u \cdot  v = (u_{1}e_{1} + \cdots  + u_{n}e_{n}) \cdot  (v_{1}e_{1} + \cdots  + v_{n}e_{n}) = \sum_{i=1}^{n}  u_{i}\overline{v}_{i},$$
Và chuẩn (norm) $\|u\|$ như
$$1/2$$
$$\|u\|= \|u_{1}e_{1} + \cdots  + u_{n}e_{n}\|= \begin{pmatrix} |u_{i}|^{2} \end{pmatrix} \sum_{i=1}^{n}  .$$
Sự kiện rằng Không gian Hermite (Hermitian space) luôn luôn có cơ sở trực chuẩn (orthonormal basis) suy ra rằng bất kỳ Gram ma trận $G$ có thể được viết dưới dạng
$$G = Q^{*}Q,$$
Với một số ma trận khả nghịch (invertible matrix) $Q$. Thật vậy, ta biết rằng trong ma trận chuyển cơ sở (change of basis matrix), Gram ma trận $G$ trở thành G' $= P^{*}GP$. Nếu cơ sở (basis) tương ứng với G' là trực chuẩn, thì G' $=$ I, do đó $G = (P^{-1} )^{*}P^{-1}$. Mệnh đề 12.11 cũng nghiệm đúng unchanged.

> **Mệnh đề 14.13.** Cho trước bất kỳ không tầm thường Không gian Hermite (Hermitian space) $E$ của hữu hạn số chiều $n \ge 1$, với mọi không gian con $F$ có số chiều $k$, phần bù trực giao (orthogonal complement) $F^{\perp}$ của $F$ có số chiều $n$ - $k$, và $E = F \oplus F^{\perp}$. Hơn nữa, ta có $F^{\perp \perp} = F$.
