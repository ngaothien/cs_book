# Mở rộng của Vành của Các vô hướng


<!-- PAGE 1313 -->
Tổng của hai khác không thực sự/đúng đắn các môđun con của $M$. Cho chứng minh, xem Bourbaki $[26]$ (Chương VII, Mục $4$, Không có. $8$, Mệnh đề $8)$. Định lý 35.38 chỉ ra rằng sinh hữu hạn (finitely generated) môđun trên PID là tổng trực tiếp (direct sum) của indecomposable các môđun. Trong Chương $36$ ta áp dụng cấu trúc các định lý cho sinh hữu hạn (finitely generated) (xoắn (torsion)) các môđun đến K[X]-môđun $E_{f}$ liên kết với tự đồng cấu $f$ trên không gian vectơ (vector space) $E$. Thứ nhất, ta cần đến understand process của mở rộng của vành của các vô hướng.

## 35.6 Mở rộng của Vành của Các vô hướng

Cần để mở rộng vành của các vô hướng phát sinh, đặc biệt khi dealing với các trị riêng (eigenvalues). Thứ nhất ta cần để định nghĩa cách mà đến thu hẹp vô hướng (scalar) phép nhân đến vành con. tình huống là rằng ta có hai các vành $A$ và $B$, B-module $M$, và vành đồng cấu $\rho$: $A \to B$. đặc biệt trường hợp rằng phát sinh thường là rằng $A$ là vành con của $B (B$ có thể là trường) và $\rho$ là inclusion ánh xạ. Thì ta có thể tạo $M$ vào A-module bởi định nghĩa vô hướng (scalar) phép nhân $\cdot$: $A \times  M \to M$ như sau.

> **Định nghĩa 35.14.** Cho trước hai các vành $A$ và $B$ và vành đồng cấu $\rho$: $A \to B$, bất kỳ B- môđun $M$ có thể được tạo vào A-module được ký hiệu bởi $\rho_{*} (M)$, bởi định nghĩa vô hướng (scalar) phép nhân bởi bất kỳ phần tử của $A$ như sau:
$$a \cdot  x = \rho (a)x,for all a \in A and all x \in M.$$
Đặc biệt, quan điểm $B$ như B-module, ta thu được A-module $\rho_{*} (B)$. Nếu $M$ và $N$ là hai B-modules và nếu $f$: $M \to N$ là $B$-tuyến tính ánh xạ, ánh xạ $f$ là đồng cấu $f$: $\rho_{*} (M) \to \rho_{*} (N)$ của các nhóm Abel $\rho_{*} (M)$ và $\rho_{*} (N)$. ánh xạ này là cũng $A$-tuyến tính, bởi vì với mọi $u \in M$ và tất cả $a \in A$, theo định nghĩa của vô hướng (scalar) phép nhân bởi các phần tử của $A$, ta có
$$f(a \cdot  u) = f(\rho (a)u) = \rho (a)f(u) = a \cdot  f(u).$$
Ánh xạ $f$: $\rho_{*} (M) \to \rho_{*} (N)$ được quan điểm như $A$-tuyến tính ánh xạ được ký hiệu bởi $\rho_{*} (f)$. Như các đồng cấu của các nhóm Abel, các ánh xạ $f$: $M \to N$ và $\rho_{*} (f): \rho_{*} (M) \to \rho_{*} (N)$ là đồng nhất, nhưng $f$ là $B$-tuyến tính ánh xạ trong khi đó $\rho_{*} (f)$ là $A$-tuyến tính ánh xạ. Bây giờ ta có thể mô tả process của vô hướng (scalar) mở rộng. Cho trước bất kỳ A-module $M$, ta tạo $\rho_{*} (B) \otimes_{A}  M$ vào (trái) B-module như sau: với mọi $\beta  \in B$, cho $\mu_{\beta}$: $\rho_{*} (B) \times  M \to \rho_{*} (B) \otimes_{A}  M$ là cho trước bởi
$$\mu_{\beta} (\beta' , x) = (\beta \beta' ) \otimes x.$$
Ánh xạ $\mu_{\beta}$ là song tuyến tính do đó nó cảm sinh ánh xạ tuyến tính (linear map) $\mu_{\beta}$: $\rho_{*} (B) \otimes_{A}  M \to \rho_{*} (B) \otimes_{A}  M$ sao cho
$$\mu_{\beta} (\beta' \otimes x) = (\beta \beta' ) \otimes x.$$

<!-- PAGE 1314 -->
Nếu ta định nghĩa vô hướng (scalar) phép nhân $\cdot$: $B \times  (\rho_{*} (B) \otimes_{A}  M) \to \rho_{*} (B) \otimes_{A}  M$ bởi
$$\beta  \cdot  z = \mu_{\beta} (z),for all \beta  \in B and all z \in \rho_{*} (B) \otimes_{A}  M,$$
Thì nó là dễ để kiểm tra rằng axioms M1, M2, M3, M4 đúng. Cho chúng ta kiểm tra M2 và M3. Ta có
$$\mu_{\beta1+\beta2} (\beta' \otimes x) = (\beta_{1}  + \beta_{2} )\beta' \otimes x$$
$$= (\beta_{1} \beta' + \beta_{2} \beta' ) \otimes x$$
$$= \beta_{1} \beta' \otimes x + \beta_{2} \beta' \otimes x$$
$$= \mu_{\beta1} (\beta' \otimes x) + \mu_{\beta2} (\beta' \otimes x)$$
Và
$$\mu_{\beta1\beta2} (\beta' \otimes x) = \beta_{1} \beta_{2} \beta' \otimes x$$
$$= \mu_{\beta1} (\beta_{2} \beta' \otimes x)$$
$$= \mu_{\beta1} (\mu_{\beta2} (\beta' \otimes x)).$$

> **Định nghĩa 35.15.** Cho trước hai các vành $A$ và $B$ và vành đồng cấu $\rho$: $A \to B$, với mọi A-module $M$, với vô hướng (scalar) phép nhân bởi các phần tử của $B$ cho trước bởi
$$\beta  \cdot  (\beta' \otimes x) = (\beta \beta' ) \otimes x,\beta , \beta' \in B, x \in M,$$
Tích tenxơ (tensor product) $\rho_{*} (B) \otimes_{A}  M$ là B-module được ký hiệu bởi $\rho^{*} (M)$, hoặc $M_{(B)}$ khi $\rho$ là inclusion của $A$ vào $B$. B-module $\rho^{*} (M)$ đôi khi được gọi là môđun được cảm sinh từ $M$ bởi mở rộng đến $B$ của vành của các vô hướng qua $\rho$. Ở đây là cụ thể ví dụ của Định nghĩa 35.15. Cho $A =\mathbb{R}, B =\mathbb{C}$ và $\rho$ là inclusion ánh xạ của $\mathbb{R}$ vào $\mathbb{C}$, i.e. $\rho$: $\mathbb{R} \to \mathbb{C}$ với $\rho (a) = a$ cho $a \in \mathbb{R}$. Cho $M$ là $\mathbb{R}-module$. trường $\mathbb{C}$ là $a \mathbb{C}-module$, và khi ta thu hẹp vô hướng (scalar) phép nhân bởi các vô hướng $\lambda  \in \mathbb{R}$, ta thu được $\mathbb{R}-module \rho_{*} (\mathbb{C})$ (mà, như nhóm Abel (abelian group), là chỉ $\mathbb{C})$. Tạo thành $\rho_{*} (\mathbb{C}) \otimes_{R}  M$. Điều này là
$$an \mathbb{R}-module where typical elements have the form \sum_{i}  n=1 a_{i}(z_{i} \otimes m_{i}), a_{i} \in \mathbb{R}, z_{i} \in \mathbb{C}, and$$
$m_{i} \in M$. Vì
$$a_{i}(z_{i} \otimes m_{i}) = a_{i}z_{i} \otimes m_{i}$$
Và vì $a_{i}z_{i} \in \mathbb{C}$ và bất kỳ phần tử của $\mathbb{C}$ là thu được điều này cách (cho $a_{i} = 1)$, các phần tử của $\rho_{*} (\mathbb{C}) \otimes_{R}  M$ có thể được viết dưới dạng
$$\sum_{i=1}^{n}  z_{i} \otimes m_{i},z_{i} \in \mathbb{C}, m_{i} \in M.$$
Ta muốn để tạo $\rho_{*} (\mathbb{C}) \otimes_{R}  M$ vào $a \mathbb{C}-module$, được ký hiệu $\rho^{*} (M)$, và do đó phải mô tả
$$how a complex number \beta  acts on \sum_{i}  n z_{i} \otimes m_{i}. By linearity, it is enough to determine how$$
$\beta  = u +$ iv acts trên phần tử sinh $z \otimes m^{=1}$, ở đâu $z = x +$ iy và $m \in M$. action được cho bởi
$$\beta  \cdot  (z \otimes m) = \beta z \otimes m = (u + iv)(x + iy) \otimes m = (ux -vy + i(uy + vx)) \otimes m,$$

<!-- PAGE 1315 -->
Vì phức phép nhân chỉ làm cho nghĩa trên $\mathbb{C}$. Ta khẳng định rằng $\rho^{*} (M)$ là đẳng cấu đến $\mathbb{C}-module M \times  M$ với phép cộng được định nghĩa bởi
$$(u_{1}, v_{1}) + (u_{2}, v_{2}) = (u_{1} + u_{2}, v_{1} + v_{2})$$
Và vô hướng (scalar) phép nhân bởi $\lambda  + i\mu  \in \mathbb{C}$ như
$$(\lambda  + i\mu ) \cdot  (u, v) = (\lambda u -\mu v, \lambda v + \mu u).$$
Định nghĩa ánh xạ $\alpha_{0}$: $\rho_{*} (\mathbb{C}) \times  M \to M \times  M$ bởi
$$\alpha_{0} (\lambda  + i\mu , u) = (\lambda u, \mu u).$$
Nó là dễ để kiểm tra rằng $\alpha_{0}  is\mathbb{R}-linear$, do đó ta thu được $an\mathbb{R}-linear$ ánh xạ $\alpha$: $\rho_{*} (\mathbb{C})\otimes_{R} M \to M \times M$ sao cho
$$\alpha ((\lambda  + i\mu ) \otimes u) = (\lambda u, \mu u).$$
Ta cũng định nghĩa ánh xạ $\beta$: $M \times  M \to \rho_{*} (\mathbb{C}) \otimes_{R}  M$ bởi
$$\beta (u, v) = 1 \otimes u + i \otimes v.$$
Một lần nữa, rõ ràng là ánh xạ này là $\mathbb{R}-linear$. Ta có thể bây giờ kiểm tra rằng $\alpha$ và $\beta$ là mutual các nghịch đảo. Ta có
$$\alpha (\beta (u, v)) = \alpha (1 \otimes u + i \otimes v) = \alpha (1 \otimes u) + \alpha (i \otimes v) = (u, 0) + (0, v) = (u, v),$$
Và trên các phần tử sinh, $\beta (\alpha ((\lambda  + i\mu$) $\otimes u)) = \beta (\lambda u, \mu u) = 1 \otimes \lambda u + i \otimes \mu u = \lambda  \otimes u + i\mu  \otimes u = (\lambda  + i\mu$) $\otimes u$. Vì vậy, $\rho_{*} (\mathbb{C}) \otimes_{R}  M$ và $M \times  M$ là đẳng cấu $as\mathbb{R}-module$. Tuy nhiên, đẳng cấu $\alpha$ là cũng đẳng cấu của $\mathbb{C}-modules$. Điều này là bởi vì trong $\rho_{*} (\mathbb{C}) \otimes_{R}  M$, trên các phần tử sinh ta có
$$(\lambda  + i\mu ) \cdot  ((x + iy) \otimes u) = (\lambda  + i\mu )(x + iy) \otimes u = (\lambda x -\mu y + i(\lambda y + \mu x)) \otimes u,$$
Do đó
$$\alpha ((\lambda  + i\mu ) \cdot  ((x + iy) \otimes u) = \alpha ((\lambda x -\mu y + i(\lambda y + \mu x)) \otimes u)$$
$$= ((\lambda x -\mu y)u, (\lambda y + \mu x)u),$$
Và theo định nghĩa của vô hướng (scalar) phép nhân bởi các phần tử của $\mathbb{C}$ trên $M \times  M$
$$(\lambda  + i\mu ) \cdot  \alpha ((x + iy) \otimes u) = (\lambda  + i\mu ) \cdot  (xu, yu) = ((\lambda x -\mu y)u, (\lambda y + \mu x)u).$$
Vì vậy, $\alpha$ là đẳng cấu giữa $\mathbb{C}-modules \rho^{*} (M) = \rho_{*} (\mathbb{C}) \otimes_{R}  M$ và $M \times  M$. ở trên process của vành mở rộng có thể cũng là ứng dụng đến các ánh xạ tuyến tính (linear maps). Ta có kết quả sau mệnh đề có chứng minh là cho trước trong Bourbaki $[25]$ (Chương II, Mục $5$, Mệnh đề $1)$.

<!-- PAGE 1316 -->

> **Mệnh đề 35.39.** Cho trước vành homomomorphism $\rho$: $A \to B$ và cho trước bất kỳ A-module $M$, ánh xạ $\phi$: $M \to \rho_{*} (\rho^{*} (M))$ cho trước bởi $\phi (x) = 1 \otimes_{A}  x$ là $A$-tuyến tính và $\phi (M)$ sinh ra B-module $\rho^{*} (M)$. Với mọi B-module $N$, và với mọi $A$-tuyến tính ánh xạ $f$: $M \to \rho_{*} (N)$, tồn tại duy nhất một $B$-tuyến tính ánh xạ
$$\overline{f}\overline{:} \rho^{*} (M) \to N$$
Sao cho
$$\rho_{*} (\overline{f}) \circ \phi  = f$$
Như trong sau đây giao hoán biểu đồ
$$M\rho_{*} (\rho^{*} (M))$$
$$\overline{J}^{\phi}\overline{J}$$
$$\overline{J} J$$
$$JJ$$
$$JJ\rho (\overline{f})$$
$$fJJ*$$
$$$$$
$$\rho_{*} (N)$$
Hoặc tương đương,
$$\overline{f}(1 \otimes_{A}  x) = f(x),for all x \in M.$$
Hệ quả là của Mệnh đề 35.39, ta thu được kết quả sau kết quả.

> **Mệnh đề 35.40.** Cho trước vành homomomorphism $\rho$: $A \to B$, với mọi hai A-modules $M$
$$and N, for every A \frac{-linear}{f} map f : M \to N, there is a unique B-linear map \rho^{*} (f): \rho^{*} (M) \to$$
$\rho^{*} (N)$ (cũng được ký hiệu) cho trước bởi
$$\rho^{*} (f) = id_{B} \otimes f,$$
Sao cho sau đây diagam giao hoán:
$$M^{\phi M}\rho_{*} (\rho^{*} (M))$$
$$f\rho (\rho *(f))$$
$$*$$
$$N_{\phi N}  /\rho_{*} (\rho^{*} (N))$$

*Chứng minh.* Áp dụng Mệnh đề 35.40 đến $A$-tuyến tính ánh xạ $\phi_{N}  \circ f$. Nếu $S$ sinh ra môđun $M$, rõ ràng là $\phi (S)$ sinh ra $\rho^{*} (M)$. Đặc biệt, nếu $M$ là sinh hữu hạn (finitely generated), do đó nếu $\rho^{*} (M)$. Các cơ sở của $M$ cũng mở rộng đến các cơ sở của $\rho^{*} (M)$.

> **Mệnh đề 35.41.** Cho trước vành homomomorphism $\rho$: $A \to B$, với mọi A-module $M$, nếu $(u_{1}, \dots  , u_{n})$ là cơ sở (basis) của $M$, thì $(\phi (u_{1}), \dots  , \phi (u_{n}))$ là cơ sở (basis) của $\rho^{*} (M)$, ở đâu $\phi$ là $A$-tuyến tính ánh xạ $\phi$: $M \to \rho_{*} (\rho^{*} (M))$ cho trước bởi $\phi (x) = 1 \otimes_{A}  x$. Hơn nữa, nếu $\rho$ là đơn ánh (injective), thì do đó là $\phi$.

*Chứng minh.* thứ nhất assertion suy ra ngay lập tức từ Mệnh đề 35.13, vì nó khẳng định rằng mọi phần tử $z$ của $\rho^{*} (M) = \rho_{*} (B) \otimes_{A}  M$ có thể được được viết trong duy nhất cách như
$$z = b_{1} \otimes u_{1} + \cdots  + b_{n} \otimes u_{n} = b_{1}(1 \otimes u_{1}) + \cdots  + b_{n}(1 \otimes u_{n}),$$

<!-- PAGE 1317 -->
Và $\phi (u_{i}) = 1 \otimes u_{i}$. Tiếp theo, nếu $\rho$ là đơn ánh (injective), theo định nghĩa của vô hướng (scalar) phép nhân trong A-module $\rho_{*} (\rho^{*} (M))$, ta có $\phi (a_{1}u_{1} + \cdots  + a_{n}u_{n}) = 0$ khi và chỉ khi
$$\rho (a_{1})\phi (u_{1}) + \cdots  + \rho (a_{n})\phi (u_{n}) = 0,$$
Và vì $(\phi (u_{1}), \dots  , \phi (u_{n}))$ là cơ sở (basis) của $\rho^{*} (M)$, ta phải có $\rho (a_{i}) = 0$ cho $i = 1, \dots  , n$, mà (bởi tính đơn ánh của $\rho$) suy ra rằng $a_{i} = 0$ cho $i = 1, \dots  , n$. Vì vậy, $\phi$ là đơn ánh (injective). Đặc biệt, nếu $A$ là vành con của $B$, thì $\rho$ là inclusion ánh xạ và Mệnh đề 35.41 chỉ ra rằng cơ sở (basis) của $M$ trở thành cơ sở (basis) của $M_{(B)}$ và rằng $M$ được nhúng vào $M_{(B)}$. Nó là cũng dễ để xem rằng nếu $M$ và $N$ là hai tự do A-modules và $f$: $M \to N$ là ánh xạ tuyến tính (linear map) rep-
$$resented by the matrix \frac{X}{f} with respect to some bases (u_{1}, \dots  , u_{n}) of M and (v_{1}, \dots  , v_{m}) of N,$$
Thì $B$-tuyến tính ánh xạ cũng được biểu diễn bởi ma trận $X$ trên các cơ sở $(\phi (u_{1}), \dots  , \phi (u_{n}))$ và $(\phi (v_{1}), \dots  , \phi (v_{m}))$. Mệnh đề 35.41 cho ta một cái khác chứng minh của sự kiện rằng bất kỳ hai các cơ sở của tự do A-module có cùng cardinality. Thật vậy, nếu $\mathfrak{m}$ là lý tưởng cực đại (maximal ideal) trong vành $A$, thì ta có thương vành đồng cấu $\pi$: $A \to A/\mathfrak{m}$, và ta thu được $A/\mathfrak{m}-module \pi^{*} (M)$. Nếu $M$ là tự do, bất kỳ cơ sở (basis) $(u_{1}, \dots  , u_{n})$ của $M$ trở thành cơ sở (basis) $(\phi (u_{1}), \dots  , \phi (u_{n}))$ của $\pi^{*} (M)$; nhưng $A/\mathfrak{m}$ là trường, do đó số chiều $n$ là một cách duy nhất được xác định. Điều này lập luận cũng áp dụng đến vô hạn cơ sở (basis) $(u_{i})_{i\in I}$. Nhận thấy rằng theo Mệnh đề 35.14, ta có đẳng cấu
$$\pi^{*} (M) = (A/\mathfrak{m}) \otimes_{A}  M \approx M/\mathfrak{m} M,$$
Do đó $M/\mathfrak{m} M$ là không gian vectơ (vector space) trên trường $A/\mathfrak{m}$, mà là lập luận được sử dụng trong Định lý 35.1.

> **Mệnh đề 35.42.** Cho trước vành homomomorphism $\rho$: $A \to B$, với mọi hai A-modules $M$ và $N$, tồn tại duy nhất một đẳng cấu
$$\rho^{*} (M) \otimes_{B}  \rho^{*} (N) \approx \rho^{*} (M \otimes_{A}  N),$$
Sao cho $(1 \otimes u) \otimes (1 \otimes v) \mapsto 1 \otimes (u \otimes v)$, với mọi $u \in M$ và tất cả $v \in N$. chứng minh sử dụng các đồng nhất thức từ Mệnh đề 33.13. Nó là không khó nhưng nó đòi hỏi little gymnastic; tốt bài tập cho độc giả.

<!-- PAGE 1318 -->
