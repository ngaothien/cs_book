# Liên tục Tuyến tính và Đa tuyến tính Các ánh xạ


<!-- PAGE 1421 -->
Cuối cùng ta cần để chứng minh rằng nếu $(X, d)$ là compắc, thì $(\mathcal{K}(X), D)$ là compắc. Vì ta đã biết rằng $(\mathcal{K}(X), D)$ là đầy đủ nếu $(X, d)$ là, nó là đủ để chứng minh rằng $(\mathcal{K}(X), D)$ là một cách tổng bị chặn nếu $(X, d)$ là, mà là không khó. Xét theo Định lý 37.55 và Định lý 37.54, nó là khả dĩ/có thể để định nghĩa một số khác rỗng compắc các tập con của $X$ theo cố định các điểm của ánh xạ co (contraction) các ánh xạ. Điều này có thể được được thực hiện theo iterated hàm các hệ, cho lớn lớp của fractals. Tuy nhiên, ta sẽ bỏ qua điều này topic và thay vì refer độc giả đến Edgar $[56]$. Trong Chương $38$ ta chỉ ra cách mà nhất định fractals có thể được được định nghĩa bởi iterated hàm các hệ, bằng cách sử dụng Định lý 37.55 và Định lý 37.54. Trước xét các vi phân, ta cần đến nhìn tại tính liên tục của các ánh xạ tuyến tính (linear maps).

## 37.11 Liên tục Tuyến tính và Đa tuyến tính Các ánh xạ

Nếu $E$ và $F$ là các không gian vectơ định chuẩn, ta thứ nhất đặc trưng hóa khi ánh xạ tuyến tính (linear map) $f$: $E \to F$ là liên tục.

> **Mệnh đề 37.56.** Cho trước hai các không gian vectơ định chuẩn $E$ và $F$, với mọi ánh xạ tuyến tính (linear map) $f$: $E \to F$, các điều kiện sau đây là tương đương:
$(1)$ hàm $f$ là liên tục tại $0$.
$(2)$ Có một hằng số $k \ge 0$ sao cho,
$$\|f(u)\|\le k, for every u \in E such that \|u\|\le 1.$$
$(3)$ Có một hằng số $k \ge 0$ sao cho,
$$\|f(u)\|\le k\|u\|, for every u \in E.$$
$(4)$ hàm $f$ là liên tục tại mọi điểm của $E$.

*Chứng minh.* Giả sử $(1)$. Thì với mọi $\epsilon  > 0$, tồn tại một $\eta  > 0$ sao cho, với mọi $u \in E$, nếu $\|u\|\le \eta$, thì $\|f(u)\|\le \epsilon$. Chọn $\epsilon  = 1$, sao cho tồn tại một $\eta  > 0$ sao cho, nếu $\|u\|\le \eta$, thì $\|f(u)\|\le 1$. Nếu $\|u\|\le 1$, thì $\|\eta u\|\le \eta \|u\|\le \eta$, và do đó, $\|f(\eta u)\|\le 1$, nghĩa là, $\eta \|f(u)\|\le 1$, mà suy ra $\|f(u)\|\le \eta^{-1}$. Do đó, $(2)$ nghiệm đúng với $k = \eta^{-1}$. Giả sử rằng $(2)$ nghiệm đúng. Nếu $u = 0$, thì bởi tính tuyến tính, f(0) $= 0$, và do đó $\|f(0)\|\le k\|0\|$ nghiệm đúng một cách tầm thường với mọi $k \ge 0$. Nếu $u \neq  0$, thì $\|u\| > 0$, và vì
$$\frac{u}{\|u\|} = 1,$$

<!-- PAGE 1422 -->
Ta có
$$$$
$$f \frac{u}{\|u\|} \le k,$$
Mà suy ra rằng
$$\|f(u)\|\le k\|u\|.$$
Do đó, $(3)$ nghiệm đúng. Nếu $(3)$ nghiệm đúng, thì với mọi $u, v \in E$, ta có
$$\|f(v) -f(u)\|= \|f(v -u)\|\le k\|v -u\|.$$
Nếu $k = 0$, thì $f$ là không hàm, và tính liên tục là hiển nhiên. Ngược lại, nếu $k > 0$, với mọi $\epsilon  > 0$, nếu $\|v$ - $u\|\le_{k}^{\epsilon}$, thì $\|f(v$ - $u)\|\le \epsilon$, mà chỉ ra tính liên tục tại mọi $u \in E$. Cuối cùng, hiển nhiên là $(4)$ suy ra $(1)$. Trong số khác things, Mệnh đề 37.56 chỉ ra rằng ánh xạ tuyến tính (linear map) là liên tục khi và chỉ khi ảnh (image) của unit (đóng) hình cầu là bị chặn. Vì liên tục ánh xạ tuyến tính (linear map) thỏa mãn điều kiện $\|f(u)\|\le k\|u\|$ (với một số $k \ge 0)$, nó là cũng liên tục đều (uniformly continuous). Nếu $E$ và $F$ là các không gian vectơ định chuẩn, tập hợp tất cả liên tục các ánh xạ tuyến tính (linear maps) $f$: $E \to F$ được ký hiệu bởi $\mathcal{L}(E; F)$. Bằng cách sử dụng Mệnh đề 37.56, ta có thể định nghĩa chuẩn (norm) $on\mathcal{L}(E; F)$ mà làm cho nó vào không gian vectơ định chuẩn (normed vector space). định nghĩa này có đã đã được cho trước trong Chương $9$ (Định nghĩa 9.8) nhưng cho độc giả’s convenience, ta repeat nó ở đây.

> **Định nghĩa 37.41.** Cho trước hai các không gian vectơ định chuẩn $E$ và $F$, với mọi liên tục ánh xạ tuyến tính (linear map) $f$: $E \to F$, ta định nghĩa chuẩn toán tử (operator norm) $\|f\|$ của $f$ như
$$\|f\|= \inf {k \ge 0 | \|f(x)\|\le k\|x\|, for all x \in E} = \sup {\|f(x)\|| \|x\|\le 1} .$$
Từ Định nghĩa 37.41, với mọi liên tục ánh xạ tuyến tính (linear map) $f \in$ L(E; $F)$, ta có
$$\|f(x)\|\le \|f\|\|x\|,$$
Với mọi $x \in E$. Nó là dễ để kiểm chứng rằng $\mathcal{L}(E; F)$ là không gian vectơ định chuẩn (normed vector space) dưới chuẩn (norm) của Định nghĩa 37.41. Hơn nữa, nếu $E, F, G$, là các không gian vectơ định chuẩn, và $f$: $E \to F$ và $g: F \to G$ là liên tục các ánh xạ tuyến tính (linear maps), ta có
$$\|g \circ f\|\le \|g\|\|f\|.$$
$$\mathbb{R}^{n}  \mathbb{C}^{n}$$
Ta có thể bây giờ chỉ ra rằng khi $E =$ hoặc $E =$, với bất kỳ của các chuẩn $\|\|_{1}, \|\|_{2}$, hoặc $\|\|_{\infty}$, thì mọi ánh xạ tuyến tính (linear map) $f$: $E \to F$ là liên tục.
$$\mathbb{R}^{n} \mathbb{C}^{n}$$

> **Mệnh đề 37.57.** Nếu $E =$ hoặc $E =$, với bất kỳ của các chuẩn $\|\|_{1}, \|\|_{2}$, hoặc $\|\|_{\infty}$, và $F$ là bất kỳ không gian vectơ định chuẩn (normed vector space), thì mọi ánh xạ tuyến tính (linear map) $f$: $E \to F$ là liên tục.

<!-- PAGE 1423 -->
$$\mathbb{R}^{n}  \mathbb{C}^{n}$$

*Chứng minh.* Cho $(e_{1}, \dots  , e_{n})$ là tiêu chuẩn cơ sở (basis) của (đồng dạng chứng minh áp dụng đến). Xét theo Mệnh đề 9.3, nó là đủ để chứng minh mệnh đề cho chuẩn (norm)
$$\|x\|_{\infty}= \max{|x_{i}| | 1 \le i \le n}.$$
Ta có,
$$\|f(v) -f(u)\|= \|f(v -u)\|=f( \sum_{1\le i\le n}  (v_{i} -u_{i})e_{i}) = \sum_{1\le i\le n}  (v_{i} -u_{i})f(e_{i}) ,$$
Và do đó,
$$\|f(v) -f(u)\|\le \begin{pmatrix} \|f(e_{i})\| \end{pmatrix} \sum_{1\le i\le n}  1max\le i\le n |v_{i} -u_{i}| = \begin{pmatrix} \|f(e_{i})\| \end{pmatrix} \sum_{1\le i\le n}  \|v -u\|_{\infty}.$$
Bởi lập luận được sử dụng trong Mệnh đề 37.56 để chứng minh rằng $(3)$ suy ra $(4), f$ là liên tục. Thực sự, ta được chứng minh trong Định lý 9.6 rằng nếu $E$ là không gian vectơ (vector space) của hữu hạn số chiều, thì bất kỳ hai các chuẩn là tương đương, sao cho chúng định nghĩa cùng tôpô. sự kiện này cùng với Mệnh đề 37.57 chứng minh sau đây:

> **Định lý 37.58.** Nếu $E$ là không gian vectơ (vector space) của hữu hạn số chiều (trên $\mathbb{R}$ hoặc $\mathbb{C})$, thì tất cả các chuẩn là tương đương (định nghĩa cùng tôpô). Hơn nữa, với mọi không gian vectơ định chuẩn (normed vector space) $F$, mọi ánh xạ tuyến tính (linear map) $f$: $E \to F$ là liên tục.  Nếu $E$ là không gian vectơ định chuẩn (normed vector space) của vô hạn số chiều, ánh xạ tuyến tính (linear map) $f$: $E \to F$ có thể không là liên tục. Như ví dụ, cho $E$ là vô hạn không gian vectơ (vector space) của tất cả các đa thức trên $\mathbb{R}$. Cho
$$\|P(X)\|= \max |P(x)|.$$
$$0\le x\le 1$$
Ta để lại như một bài tập để chỉ ra rằng điều này là thật vậy chuẩn (norm). Cho $F = \mathbb{R}$, và cho $f$: $E \to F$ là ánh xạ được định nghĩa sao cho, f(P(X)) $=$ P(3). Rõ ràng là $f$ là tuyến tính. Xét dãy của các đa thức
$$P_{n}(X) = \begin{pmatrix} X^{n} \\ \overline{2} \end{pmatrix} .$$
$$It is clear that \|P_{n}\| \begin{pmatrix} =_{2}^{1n} \end{pmatrix} , and thus, the sequence P_{n} has the null polynomial as a limit.$$
Tuy nhiên, ta có
$$3^{n}$$
$$f(P_{n}(X)) = P_{n}(3) = \begin{pmatrix} \overline{2} \end{pmatrix} ,$$
Và dãy $f(P_{n}(X))$ diverges đến $+\infty$. Hệ quả là, xét theo Mệnh đề 37.15 $(1), f$ là không liên tục.

<!-- PAGE 1424 -->
Ta bây giờ xét tính liên tục của đa tuyến tính các ánh xạ. Ta treat một cách tường minh song tuyến tính các ánh xạ, tổng quát trường hợp đang là trực tiếp/dễ dàng mở rộng.

> **Mệnh đề 37.59.** Cho trước các không gian vectơ định chuẩn $E, F$ và $G$, với mọi ánh xạ song tuyến tính (bilinear map) $f$: $E \times F \to G$, các điều kiện sau đây là tương đương:
$(1)$ hàm $f$ là liên tục tại $\langle 0, 0\rangle$. $2)$ Có một hằng số $k \ge 0$ sao cho,
$$\|f(u, v)\|\le k, for all u \in E, v \in F such that \|u\|, \|v\|\le 1.$$
$3)$ Có một hằng số $k \ge 0$ sao cho,
$$\|f(u, v)\|\le k\|u\|\|v\|, for all u \in E, v \in F.$$
$4)$ hàm $f$ là liên tục tại mọi điểm của $E \times  F$.

*Chứng minh.* Nó là đồng dạng đến rằng của Mệnh đề 37.56, với nhỏ subtlety trong chứng minh rằng $(3)$ suy ra $(4)$, cụ thể là rằng hai khác nhau $\eta$ ’s rằng là không độc lập là cần thiết. Ngược lại đến liên tục các ánh xạ tuyến tính (linear maps), mà phải là liên tục đều (uniformly continuous), khác không liên tục song tuyến tính các ánh xạ là không liên tục đều (uniformly continuous). Cho $f$: $E \times  F \to G$ là liên tục ánh xạ song tuyến tính (bilinear map) sao cho f(, $b) \neq  0$ với một số $a \in E$ và một số $b \in F$. Xét các dãy $(u_{n})$ và $(v_{n})$ (với $n \ge 1)$ cho trước bởi
$$u_{n} = (x_{n}, y_{n}) = (na, nb)$$
$$v_{n} = (x_{n}', y_{n}') = \begin{pmatrix}  & 1 \\ n + \\ n \end{pmatrix} \begin{pmatrix}  & 1 \\ a, & n + \\ n \end{pmatrix} \begin{pmatrix} b \end{pmatrix} .$$
Hiển nhiên
$$\|v_{n} -u_{n}\|\le \frac{1}{n} (\|a\|+ \|b\|),$$
Do đó $lim_{n\mapsto \infty} \|v_{n}$ - $u_{n}\| = 0$. Mặt khác
$$f(x_{n}', y_{n}') -f(x_{n}, y_{n}) = \begin{pmatrix} 1 \\ 2 + \\ n^{2} \end{pmatrix} f(a, b),$$
Và do đó $lim_{n\mapsto \infty} \|f(x_{n}', y_{n}')$ - $f(x_{n}, y_{n})\| = 2 \|f(a, b)\|̸ = 0$, mà chỉ ra rằng $f$ là không liên tục đều (uniformly continuous), bởi vì nếu điều này đã là trường hợp, điều này giới hạn sẽ là không. Nếu $E, F$, và $G$, là các không gian vectơ định chuẩn, ta ký hiệu tập hợp tất cả liên tục song tuyến tính các ánh xạ $f$: $E \times  F \to G$ bởi $\mathcal{L}_{2}(E, F; G)$. Bằng cách sử dụng Mệnh đề 37.59, ta có thể định nghĩa chuẩn (norm) trên $\mathcal{L}_{2}(E, F; G)$ mà làm cho nó vào không gian vectơ định chuẩn (normed vector space).

<!-- PAGE 1425 -->

> **Định nghĩa 37.42.** Cho trước các không gian vectơ định chuẩn $E, F$, và $G$, với mọi liên tục ánh xạ song tuyến tính (bilinear map) $f$: $E \times  F \to G$, ta định nghĩa chuẩn (norm) $\|f\|$ của $f$ như
$$\|f\|= \inf {k \ge 0 | \|f(x, y)\|\le k\|x\|\|y\|, for all x \in E, y \in F}$$
$$= \sup {\|f(x, y)\|| \|x\|, \|y\|\le 1} .$$
Từ Định nghĩa 37.41, với mọi liên tục ánh xạ song tuyến tính (bilinear map) $f \in L_{2}(E, F; G)$, ta có
$$\|f(x, y)\|\le \|f\|\|x\|\|y\|,$$
Với mọi $x, y \in E$. Nó là dễ để kiểm chứng rằng $\mathcal{L}_{2}(E, F; G)$ là không gian vectơ định chuẩn (normed vector space) dưới chuẩn (norm) của Định nghĩa 37.42. Cho trước ánh xạ song tuyến tính (bilinear map) $f$: $E \times  F \to G$, với mọi $u \in E$, ta thu được ánh xạ tuyến tính (linear map) được ký hiệu fu: $F \to G$, được định nghĩa sao cho, fu(v) $=$ f(u, $v)$. Hơn nữa, vì
$$\|f(x, y)\|\le \|f\|\|x\|\|y\|,$$
Rõ ràng là fu là liên tục. Ta có thể thì xét ánh xạ $\phi$: $E \to$ L(F; $G)$, được định nghĩa sao cho, $\phi (u) =$ fu, với mọi $u \in E$, hoặc tương đương, sao cho,
$$\phi (u)(v) = f(u, v).$$
Thực sự, nó là dễ để chỉ ra rằng $\phi$ là tuyến tính và liên tục, và rằng $\|\phi \| = \|f\|$. Do đó, $f \mapsto \phi$ định nghĩa ánh xạ $from\mathcal{L}_{2}(E, F; G) to\mathcal{L}(E;\mathcal{L}(F; G))$. Ta có thể cũng đi quay lại $from\mathcal{L}(E;\mathcal{L}(F; G))$ đến $\mathcal{L}_{2}(E, F; G)$. Ta summarize tất cả điều này trong sau đây mệnh đề.

> **Mệnh đề 37.60.** Cho $E, F, G$ là ba các không gian vectơ định chuẩn. ánh xạ $f \mapsto \phi$, từ $\mathcal{L}_{2}(E, F; G)$ đến $\mathcal{L}(E;\mathcal{L}(F; G))$, được định nghĩa sao cho, với mọi $f \in L_{2}(E, F; G)$,
$$\phi (u)(v) = f(u, v),$$
Là đẳng cấu của các không gian vectơ, và hơn nữa, $\|\phi \| = \|f\|$. Như hệ quả của Mệnh đề 37.60, ta thu được sau đây mệnh đề mà sẽ là hữu ích khi ta định nghĩa bậc hai các đạo hàm.

> **Mệnh đề 37.61.** Cho $E, F$ là các không gian vectơ định chuẩn. ánh xạ app từ $\mathcal{L}(E; F) \times  E$ đến $F$, được định nghĩa sao cho, với mọi $f \in$ L(E; $F)$, với mọi $u \in E$,
$$app(f, u) = f(u),$$
Là liên tục ánh xạ song tuyến tính (bilinear map).

<!-- PAGE 1426 -->
Nhận xét: Nếu $E$ và $F$ là không tầm thường, nó có thể được được hiển thị rằng $\|app\| = 1$. Nó có thể cũng được hiển thị rằng hợp thành
$$\circ : \mathcal{L}(E; F) \times  L(F; G) \to L(E; G),$$
Là song tuyến tính và liên tục. ở trên các mệnh đề và định nghĩa tổng quát hóa đến tùy ý n-multilinear các ánh xạ, với $n \ge 2$. Mệnh đề 37.59 mở rộng trong hiển nhiên cách đến bất kỳ n-ánh xạ đa tuyến tính (multilinear map) $f$: $E_{1} \times \cdots \times E_{n} \to F$, nhưng điều kiện $(3)$ trở thành: Có một hằng số $k \ge 0$ sao cho,
$$\|f(u_{1}, \dots  , u_{n})\|\le k\|u_{1}\|\cdots  \|u_{n}\|, for all u_{1} \in E_{1}, \dots  , u_{n} \in E_{n}.$$
Định nghĩa 37.42 cũng mở rộng dễ dàng đến
$$\|f\|= \inf {k \ge 0 | \|f(x_{1}, \dots  , x_{n})\|\le k\|x_{1}\|\cdots  \|x_{n}\|, for all x_{i} \in E_{i}, 1 \le i \le n}$$
$$= \sup {\|f(x_{1}, \dots  , x_{n})\|| \|x_{n}\|, \dots  , \|x_{n}\|\le 1} .$$
Mệnh đề 37.60 là cũng dễ dàng được mở rộng, và ta thu được đẳng cấu giữa liên tục n-multilinear các ánh xạ trong $\mathcal{L}_{n}(E_{1}, \dots  , E_{n}; F)$, và liên tục các ánh xạ tuyến tính (linear maps) trong
$$\mathcal{L}(E_{1};\mathcal{L}(E_{2}; \dots  ;\mathcal{L}(E_{n}; F)))$$
Hiển nhiên mở rộng của Mệnh đề 37.61 cũng nghiệm đúng.

> **Định nghĩa 37.43.** không gian vectơ định chuẩn (normed vector space) $(E, \|\|) over\mathbb{R} (or\mathbb{C})$ mà là không gian mêtric đầy đủ cho khoảng cách d(u, $v) = \|v$ - $u\|$, được gọi là một Không gian Banach (Banach space). sau đây định lý là then chốt kết quả của lý thuyết của Các không gian Banach worth chứng minh.

> **Định lý 37.62.** Nếu $E$ và $F$ là các không gian vectơ định chuẩn, và nếu $F$ là Không gian Banach (Banach space), thì $\mathcal{L}(E; F)$ là Không gian Banach (Banach space) (với chuẩn toán tử (operator norm)).

*Chứng minh.* Cho $(f)_{n\ge1}$ là Dãy Cauchy (Cauchy sequence) của liên tục các ánh xạ tuyến tính (linear maps) $f_{n}$: $E \to F$. Ta tiến hành trong một vài các bước. Bước $1$. Định nghĩa từng điểm giới hạn $f$: $E \to F$ của dãy $(f_{n})_{n\ge1}$. Vì $(f)_{n\ge1}$ là Dãy Cauchy (Cauchy sequence), với mọi $\epsilon  > 0$, tồn tại một $N > 0$ sao cho $\|f_{m}$ - $f_{n}\| < \epsilon$ với mọi $m, n \ge N$. Vì $\|\|$ là chuẩn toán tử (operator norm), ta suy ra rằng với mọi $u \in E$, ta có $\|f_{m}(u)$ - $f_{n}(u)\| = \|(f_{m}$ - $f_{n})(u)\|\le \|f_{m}$ - $f_{n}\|\|u\|\le \epsilon  \|u\|$ với mọi $m, n \ge N$, nghĩa là,
$$\|f_{m}(u) -f_{n}(u)\|\le \epsilon  \|u\|for all m, n \ge N.(*_{1})$$

<!-- PAGE 1427 -->
Nếu $u = 0$, thì $f_{m}(0) = f_{n}(0) = 0$ với mọi $m, n$, do đó dãy $(f_{n}(0))$ là Dãy Cauchy (Cauchy sequence) trong $F$ hội tụ đến $0$. Nếu $u \neq  0$, bằng cách thay thế $\epsilon$ bởi $\epsilon / \|u\|$, ta xem rằng dãy $(f_{n}(u))$ là Dãy Cauchy (Cauchy sequence) trong $F$. Vì $F$ là đầy đủ, dãy $(f_{n}(u))$ có giới hạn mà ta ký hiệu bởi f(u). Điều này định nghĩa của ta candidate giới hạn hàm $f$ bởi
$$f(u) = limf_{n}(u).$$
$$n\mapsto \infty$$
Nó vẫn còn để chứng minh rằng $1. f$ là tuyến tính. $2. f$ là continous. $3. f$ là giới hạn của $(f_{n})$ cho chuẩn toán tử (operator norm). Bước $2$. hàm $f$ là tuyến tính. Nhắc lại rằng trong không gian vectơ định chuẩn (normed vector space), phép cộng và phép nhân bởi cố định vô hướng (scalar) là liên tục (vì $\|u + v\|\le \|u\| + \|v\|$ và $\|\lambda u\|\le |\lambda$ | $\|u\|)$. Do đó theo định nghĩa của $f$ và vì $f_{n}$ là tuyến tính ta có
$$f(u + v) = limf_{n}(u + v)by definition of f$$
$$n\mapsto \infty$$
$$= lim(f_{n}(u) + f_{n}(v))by linearity of f_{n}$$
$$n\mapsto \infty$$
$$= limf_{n}(u) + limf_{n}(v)since + is continuous$$
$$n\mapsto \infty n\mapsto \infty$$
$$= f(u) + f(v)by definition of f.$$
Tương tự,
$$f(\lambda u) = limf_{n}(\lambda u)by definition of f$$
$$n\mapsto \infty$$
$$= lim\lambda f_{n}(u)by linearity of f_{n}$$
$$n\mapsto \infty$$
$$= \lambda  limf_{n}(u)by continuity of scalar multiplication$$
$$n\mapsto \infty$$
$$= \lambda f(u)by definition of f.$$
Vì vậy, $f$ là tuyến tính. Bước $3$. hàm $f$ là liên tục. Vì $(f_{n})_{n\ge1}$ là Dãy Cauchy (Cauchy sequence), với mọi $\epsilon  > 0$, tồn tại một $N > 0$ sao cho $\|f_{m}$ - $f_{n}\| < \epsilon$ với mọi $m, n \ge N$. Vì $f_{m} = f_{n} + f_{m}$ - $f_{n}$, ta thu được $\|f_{m}\|\le \|f_{n}\| + \|f_{m}$ - $f_{n}\|$, mà suy ra rằng
$$\|f_{m}\|\le \|f_{n}\|+ \epsilon for all m, n \ge N.(*_{2})$$
