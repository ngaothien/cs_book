# Đối ngẫu (dual) Các chuẩn


<!-- PAGE 556 -->

## 14.7 Đối ngẫu (dual) Các chuẩn

Trong nhận xét sau đây chứng minh của Mệnh đề 9.11, ta được giải thích rằng nếu $(E, \|\|)$ và $(F, \|\|)$ là hai các không gian vectơ định chuẩn và nếu ta cho $\mathcal{L}(E; F)$ ký hiệu tập hợp tất cả liên tục (tương đương, bị chặn) các ánh xạ tuyến tính (linear maps) từ $E$ đến $F$, thì, ta có thể định nghĩa chuẩn toán tử (operator norm) (hoặc phụ thuộc chuẩn (norm)) $\|\|$ trên $\mathcal{L}(E; F)$ như sau: với mọi $f \in$ L(E; $F)$,
$$\|\|$$
$$\|f\|= \sup\in \frac{f(x)}{\|x\|} = \sup\in \|f(x)\|.$$
$$xExE$$
$$x\neq 0\|x\|=1$$
$$\mathbb{C}$$
Đặc biệt, nếu $F =$, thì $\mathcal{L}(E; F) =$ E' là không gian đối ngẫu (dual space) của $E$, và ta thu được chuẩn toán tử (operator norm) được ký hiệu bởi $\|\|_{*}$ cho trước bởi
$$\|f\|_{*}= \sup|f(x)|.$$
$$x\in E$$
$$\|x\|=1$$
Chuẩn (norm) $\|\|_{*}$ được gọi là đối ngẫu (dual) chuẩn (norm) của $\|\|$ trên E'. Bây giờ ta giả sử rằng $E$ là hữu hạn chiều Không gian Hermite (Hermitian space), trong mà trường hợp E' $= E^{*}$. Định lý 14.6 suy ra rằng với mọi dạng tuyến tính (linear form) $f \in E^{*}$, tồn tại duy nhất một vectơ $y \in E$ sao cho
$$f(x) = \langle x, y\rangle ,$$
Với mọi $x \in E$, và do đó ta có thể viết
$$\|f\|_{*}= \sup|\langle x, y\rangle |.$$
$$x\in E$$
$$\|x\|=1$$
Ở trên suggests định nghĩa chuẩn (norm) $\|\|^{D}$ trên $E$.

> **Định nghĩa 14.13.** Nếu $E$ là hữu hạn chiều Không gian Hermite (Hermitian space) và $\|\|$ là bất kỳ chuẩn (norm) trên $E$, với mọi $y \in E$ ta cho
$$\|y\|^{D}= \sup|\langle x, y\rangle |,$$
$$x\in E$$
$$\|x\|=1$$
Là đối ngẫu (dual) chuẩn (norm) của $\|\|$ (trên $E)$. Nếu $E$ là thực Không gian Euclid (Euclidean space), thì đối ngẫu (dual) chuẩn (norm) được định nghĩa bởi
$$\|y\|^{D}= \sup\langle x, y\rangle$$
$$x\in E$$
$$\|x\|=1$$
Với mọi $y \in E$. Beware rằng $\|\|$ là một cách tổng quát không Hermite chuẩn (norm) liên kết với Hermite tích vô hướng (inner product). đối ngẫu (dual) chuẩn (norm) chỉ ra lên trong lồi quy hoạch; xem Boyd và Vandenberghe $[29]$, Các chương $2, 3, 6, 9$. sự kiện rằng $\|\|^{D}$ là chuẩn (norm) suy ra từ sự kiện rằng $\|\|_{*}$ là chuẩn (norm) và có thể cũng là đã kiểm tra một cách trực tiếp. Nó là worth không rằng tam giác bất đẳng thức cho $\|\|^{D}$ đến “cho tự do,” trong nghĩa rằng nó nghiệm đúng với mọi hàm $p: E \to \mathbb{R}$.

<!-- PAGE 557 -->
$$\mathbb{R}$$

> **Mệnh đề 14.26.** Với mọi hàm $p: E \to$, nếu ta định nghĩa $p^{D}$ bởi
$$p^{D}(x) = \sup|\langle z, x\rangle |,$$
$$p(z)=1$$
Thì ta có
$$p^{D}(x + y) \le p^{D}(x) + p^{D}(y).$$

*Chứng minh.* Ta có
$$p^{D}(x + y) = \sup|\langle z, x + y\rangle |$$
$$p(z)=1$$
$$= \sup(|\langle z, x\rangle + \langle z, y\rangle |)$$
$$p(z)=1$$
$$\le \sup(|\langle z, x\rangle | + |\langle z, y\rangle |)$$
$$p(z)=1$$
$$\le \sup|\langle z, x\rangle | + \sup|\langle z, y\rangle |$$
$$p(z)=1p(z)=1$$
$$= p^{D}(x) + p^{D}(y).$$

> **Định nghĩa 14.14.** Nếu $p: E \to \mathbb{R}$ là hàm sao cho
$(1)$ p(x) $\ge 0$ với mọi $x \in E$, và p(x) $= 0$ khi và chỉ khi $x = 0$;
$(2) p(\lambda x) = |\lambda$ |p(x), với mọi $x \in E$ và tất cả $\lambda  \in \mathbb{C}$;
$(3) p$ là liên tục, trong nghĩa rằng với một số cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $E$, hàm
$$(x_{1}, \dots  , x_{n}) \mapsto p(x_{1}e_{1} + \cdots  + x_{n}e_{n})$$
$$\mathbb{C}^{n}  \mathbb{R}$$
Từ đến là liên tục, thì ta nói rằng $p$ là pre-norm. Hiển nhiên, mọi chuẩn (norm) là pre-norm, nhưng pre-norm có thể không thỏa mãn tam giác bất đẳng thức.

> **Hệ quả 14.27.** đối ngẫu (dual) chuẩn (norm) của bất kỳ pre-norm là thực sự chuẩn (norm).

> **Mệnh đề 14.28.** Với mọi $y \in E$, ta có
$$\|y\|^{D}= \sup|\langle x, y\rangle | = \sup\mathfrak{R}\langle x, y\rangle .$$
$$x\in Ex\in E$$
$$\|x\|=1\|x\|=1$$

*Chứng minh.* Vì $E$ là hữu hạn dimensional, unit mặt cầu $S^{n-1} = {x \in E$ | $\|x\| = 1}$ là compắc, do đó tồn tại một $x_{0} \in S^{n-1}$ sao cho
$$\|y\|^{D}= |\langle x_{0}, y\rangle |.$$

<!-- PAGE 558 -->
Nếu $\langle x_{0}, y\rangle = \rho e^{i\theta}$, với $\rho  \ge 0$, thì
$$|\langle e^{-i\theta}x_{0}, y\rangle | = |e^{-i\theta}\langle x_{0}, y\rangle | = |e^{-i\theta}\rho e^{i\theta}| = \rho ,$$
Do đó
$$\|y\|^{D}= \rho  = \langle e^{-i\theta}x_{0}, y\rangle ,(*)$$
Với

$e^{-i\theta}x_{0}$

$= \|x_{0}\| = 1$. Mặt khác,
$$\mathfrak{R}\langle x, y\rangle \le |\langle x, y\rangle |,$$
Do đó bởi (*) ta thu được
$$\|y\|^{D}= \sup|\langle x, y\rangle | = \sup\mathfrak{R}\langle x, y\rangle ,$$
$$x\in Ex\in E$$
$$\|x\|=1\|x\|=1$$
Như đã khẳng định.

> **Mệnh đề 14.29.** Với mọi $x, y \in E$, ta có
$$|\langle x, y\rangle | \le \|x\|\|y\|^{D}$$
$$|\langle x, y\rangle | \le \|x\|^{D}\|y\|.$$

*Chứng minh.* Nếu $x = 0$, thì $\langle x, y\rangle = 0$ và các bất đẳng thức này là tầm thường. Nếu $x \neq  0$, vì $\|x/ \|x\|\| = 1$, theo định nghĩa của $\|y\|^{D}$, ta có
$$|\langle x/ \|x\|, y\rangle | \le \sup|\langle z, y\rangle | = \|y\|^{D},$$
$$\|z\|=1$$
Mà cho ta
$$|\langle x, y\rangle | \le \|x\|\|y\|^{D}.$$
Thứ hai bất đẳng thức nghiệm đúng bởi vì $|\langle x, y\rangle$ | $= |\langle y, x\rangle$ |. Nó là không khó để chỉ ra rằng với mọi $y \in \mathbb{C}^{n}$,
$$\|y\|_{1}^{D} = \|y\|_{\infty}$$
$$\|y\|_{\infty}^{D}= \|y\|_{1}$$
$$\|y\|_{2}^{D} = \|y\|_{2} .$$
Do đó, Euclidean chuẩn (norm) là autodual. Tổng quát hơn, sau đây mệnh đề nghiệm đúng.

> **Mệnh đề 14.30.** Nếu $p, q \ge 1$ và $1/p + 1/q = 1$, hoặc $p = 1$ và $q = \infty$, hoặc $p = \infty$ và $q = 1$, thì với mọi $y \in \mathbb{C}^{n}$, ta có
$$\|y\|_{p}^{D} = \|y\|_{q} .$$

<!-- PAGE 559 -->

*Chứng minh.* Bởi H¨older’s bất đẳng thức (Hệ quả 9.2), với mọi $x, y \in \mathbb{C}^{n}$, ta có
$$|\langle x, y\rangle | \le \|x\|_{p} \|y\|_{q} ,$$
Do đó
$$\|y\|_{p}^{D} = \sup|\langle x, y\rangle | \le \|y\|_{q} .$$
$$x\in \mathbb{C} n$$
$$\|x\|=1$$
$$p$$
Cho điều ngược lại, ta xét các trường hợp $p = 1, 1 < p < +\infty$, và $p = +\infty$. Thứ nhất giả sử $p = 1$. kết quả là hiển nhiên cho $y = 0$, do đó giả sử y̸ $= 0$. Cho trước $y$, nếu ta chọn $x_{j} = 1$ với một số chỉ số $j$ sao cho $\|y\|_{\infty} = max_{1\le i\le n} |y_{i}| = |y_{j}|$, và $x_{k} = 0$ cho k̸ $= j$, thì $|\langle x, y\rangle$ | $= |y_{j}| = \|y\|_{\infty}$, do đó $\|y\|_{1}^{D} = \|y\|_{\infty}$. Bây giờ ta turn đến trường hợp $1 < p < +\infty$. Thì ta cũng có $1 < q < +\infty$, và phương trình $1/p + 1/q = 1$ là tương đương đến pq $= p + q$, nghĩa là, p(q - $1) = q$. Chọn $z_{j} = y_{j}|y_{j}|^{q-2}$ cho $j = 1, \dots  , n$, sao cho
$$!1/p !1/p !1/p$$
$$\|z\|_{p} = \sum_{j=1}^{n}  |z_{j}|^{p}= \sum_{j=1}^{n}  |y_{j}|^{(q-1)p}= \sum_{j=1}^{n}  |y_{j}|^{q}.$$
Thì nếu $x = z/ \|z\|_{p}$, ta có
$$\sum  nj=1 z_{j}\overline{y}_{j} \sum  nj=1 y_{j}\overline{y}_{j}|y_{j}|^{q-2} \sum_{nj}  n ||^{q} !1/q$$
$$|\langle x, y\rangle | =\overline{\|}\overline{z}\overline{\|}_{p}=\overline{\|}\overline{z}\overline{\|}_{p}= \frac{y_{j}}{|^{q1/p}} =1 = \sum_{j=1}^{n}  |y_{j}|^{q}= \|y\|_{q} .$$
$$\begin{pmatrix} =1|y_{j} \end{pmatrix} \sum_{j}$$
Do đó $\|y\|_{p}^{D} = \|y\|_{q}$. Cuối cùng, nếu $p = \infty$, thì chọn $x_{j} = y_{j}/|y_{j}|$ nếu $y_{j} \neq  0$, và $x_{j} = 0$ nếu $y_{j} = 0$. Thì
$$|\langle x, y\rangle | = \sum_{yj\neq 0}^{n}  y_{j}\overline{y}_{j}/|y_{j}|= \sum_{yj\neq 0}  |y_{j}| = \|y\|_{1} .$$
Do đó $\|y\|_{\infty}^{D} = \|y\|_{1}$. Ta có thể chỉ ra rằng đối ngẫu (dual) của spectral chuẩn (norm) là vết (trace) chuẩn (norm) (hoặc nuclear chuẩn (norm)) cũng được thảo luận trong Mục 22.5. Nhắc lại từ Mệnh đề 9.11 rằng spectral chuẩn (norm) $\|A\|_{2}$ của ma trận $A$ là square nghiệm (root) của lớn nhất trị riêng (eigenvalue) của $A^{*}A$, nghĩa là, lớn nhất giá trị kỳ dị (singular value) của $A$.

> **Mệnh đề 14.31.** đối ngẫu (dual) của spectral chuẩn (norm) được cho bởi
$$\|A\|_{2}^{D} = \sigma_{1}  + \cdots  + \sigma_{r} ,$$
Ở đâu $\sigma_{1}  > \cdots  > \sigma_{r}  > 0$ là các giá trị kỳ dị (singular values) của $A \in M_{n}(\mathbb{C})$ (mà có hạng (rank) $r)$.

<!-- PAGE 560 -->

*Chứng minh.* Trong trường hợp này tích vô hướng (inner product) trên $M_{n}(\mathbb{C})$ là Frobenius tích vô hướng (inner product) $\langle A, B\rangle = tr(B^{*}A)$, và đối ngẫu (dual) chuẩn (norm) của spectral chuẩn (norm) được cho bởi
$$\|A\|_{2}^{D} = \sup{|\mathrm{tr}(A^{*}B)| | \|B\|_{2} = 1}.$$
Nếu ta nhân tử $A$ bằng cách sử dụng SVD như $A = V \Sigma U^{*}$, ở đâu $U$ và $V$ là unita và $\Sigma$ là ma trận đường chéo (diagonal matrix) có $r$ khác không các phần tử (entries) là các giá trị kỳ dị (singular values) $\sigma_{1}  > \cdots  > \sigma_{r}  > 0$, ở đâu $r$ là hạng (rank) của $A$, thì
$$|\mathrm{tr}(A^{*}B)| = |\mathrm{tr}(U\Sigma V^{*} B)| = |\mathrm{tr}(\Sigma V^{*} BU)|,$$
Do đó nếu ta chọn $B = V U^{*}$, ma trận unita (unitary matrix) sao cho $\|B\|_{2} = 1$, ta thu được
$$|\mathrm{tr}(A^{*}B)| = \mathrm{tr}(\Sigma ) = \sigma_{1}  + \cdots  + \sigma_{r} ,$$
Và do đó
$$\|A\|_{2}^{D} \ge \sigma_{1}  + \cdots  + \sigma_{r} .$$
Vì $\|B\|_{2} = 1$ và $U$ và $V$ là unita, theo Mệnh đề 9.11 ta có $\|V^{*} BU\|_{2} = \|B\|_{2} = 1$. Nếu $Z = V^{*}$ BU, theo định nghĩa của chuẩn toán tử (operator norm)
$$1 = \|Z\|_{2} = \sup{\|Zx\|_{2} | \|x\|_{2} = 1},$$
Do đó bởi chọn $x$ là chính tắc vectơ $e_{j}$, ta xem rằng $\|Z^{j}\|_{2} \le 1$ ở đâu $Z^{j}$ là cột thứ $j$ của $Z$, do đó $|z_{jj}| \le 1$, và vì
$$|\mathrm{tr}(\Sigma V^{*} BU)| = |\mathrm{tr}(\Sigma Z)| = \sum_{j=1}^{r}  \sigma_{j} z_{jj} \le \sum_{j=1}^{r}  \sigma_{j} |z_{jj}| \le \sum_{j=1}^{r}  \sigma_{j} ,$$
Và ta kết luận rằng
$$|\mathrm{tr}(\Sigma V^{*} BU)| \le \sum_{j=1}^{r}  \sigma_{j} .$$
Ở trên suy ra rằng
$$\|A\|_{2}^{D} \le \sigma_{1}  + \cdots  + \sigma_{r} ,$$
Và vì ta cũng có $\|A\|_{2}^{D} \ge \sigma_{1}  + \cdots  + \sigma_{r}$, ta kết luận rằng
$$\|A\|_{2}^{D} = \sigma_{1}  + \cdots  + \sigma_{r} ,$$
Chứng minh mệnh đề của chúng ta.

> **Định nghĩa 14.15.** Cho trước bất kỳ phức ma trận $n \times  n$ ma trận $A$ của hạng (rank) $r$, của nó nuclear chuẩn (norm) (hoặc vết (trace) chuẩn (norm)) được cho bởi
$$\|A\|_{N} = \sigma_{1}  + \cdots  + \sigma_{r} .$$

<!-- PAGE 561 -->
Nuclear chuẩn (norm) có thể được suy rộng/tổng quát hóa đến $m \times  n$ các ma trận (xem Mục 22.5). nuclear chuẩn (norm) $\sigma_{1}  + \cdots  + \sigma_{r}$ của một ma trận cỡ $m \times  n$ $A$ (ở đâu $r$ là hạng (rank) của $A)$ được ký hiệu bởi $\|A\|_{N}$. nuclear chuẩn (norm) đóng quan trọng vai trò trong ma trận đầy đủ hóa. bài toán là điều này. Cho trước ma trận $A_{0}$ với missing các phần tử (entries) (missing dữ liệu), một sẽ like đến fill trong missing các phần tử (entries) trong $A_{0}$ để thu được ma trận $A$ của tối tiểu hạng (rank). Ví dụ, xét các ma trận
$$A_{0} = \begin{pmatrix} 1 & 2 \\ * & * \end{pmatrix} ,B_{0} = \begin{pmatrix} 1 & * \\ * & 4 \end{pmatrix} ,C_{0} = \begin{pmatrix} 1 & 2 \\ 3 & * \end{pmatrix} .$$
Tất cả có thể được completed với hạng (rank) $1$. Cho $A_{0}$, sử dụng bất kỳ bội của $(1, 2)$ cho hàng thứ hai. Cho $B_{0}$, sử dụng bất kỳ các số $b$ và $c$ sao cho bc $= 4$. Cho $C_{0}$, chỉ khả năng là $d = 6$. nổi tiếng ví dụ của bài toán này là Netflix competition. ratings của $m$ films bởi $n$ viewers đi vào $A_{0}$. Nhưng customers didn’t xem tất cả movies. Nhiều ratings đã là missing. Những phần tử đó đã có là predicted bởi recommender hệ. nuclear chuẩn (norm) gave tốt nghiệm rằng cần thiết là adjusted cho human psychology. Vì hạng (rank) của ma trận là không chuẩn (norm), trong thứ tự để giải ma trận đầy đủ hóa bài toán ta có thể sử dụng sau đây “lồi relaxation.” Cho $A_{0}$ là incomplete $m \times  n$ ma trận: Cực tiểu hóa $\|A\|_{N}$ subject đến $A = A_{0}$ trong đã biết các phần tử (entries). ở trên bài toán có đã được extensively studied, đặc biệt bởi Cand`es và Recht. Xấp xỉ/đại khái, chúng đã chỉ ra rằng nếu $A$ là một ma trận cỡ $n \times  n$ của hạng (rank) $r$ và $K$ các phần tử (entries) là đã biết trong $A$, thì nếu $K$ là lớn đủ $(K > Cn^{5/4}r$ log $n)$, với cao probability, recovery của $A$ là perfect. Xem Strang $[177]$ cho chi tiết (Mục III.5). Ta close điều này mục bởi phát biểu sau đây đối ngẫu định lý.

> **Định lý 14.32.** Nếu $E$ là hữu hạn chiều Không gian Hermite (Hermitian space), thì với mọi chuẩn (norm) $\|\|$ trên $E$, ta có
$$\|y\|^{DD}= \|y\|$$
Với mọi $y \in E$.

*Chứng minh.* Theo Mệnh đề 14.29, ta có
$$|\langle x, y\rangle | \le \|x\|^{D}\|y\|,$$
Do đó ta thu được
$$\|y\|^{DD}=\sup|\langle x, y\rangle | \le \|y\|,for all y \in E.$$
$$\|x\|D=1$$
Nó vẫn còn để chứng minh rằng
$$\|y\|\le \|y\|^{DD},for all y \in E.$$
Các chứng minh của sự kiện này có thể được tìm thấy trong Horn và Johnson $[98]$ (Mục 5.5), và trong Serre $[162]$ (Chương $7)$. chứng minh làm cho sử dụng của sự kiện rằng khác rỗng, đóng, tập lồi (convex set) có tựa/hỗ trợ siêu phẳng (hyperplane) qua mỗi của biên (biên (boundary)) của nó các điểm, kết quả đã biết như Minkowski’s

<!-- PAGE 562 -->
Bổ đề. Cho hình học interpretation của tựa/hỗ trợ siêu phẳng (hyperplane) xem Hình 14.1. kết quả này là hệ quả của Hahn–Banach định lý; xem Gallier $[73]$. Ta cho chứng minh trong trường hợp ở đâu $E$ là thực Không gian Euclid (Euclidean space). Một số định thức con (minor) modifications có được tạo khi dealing với phức các không gian vectơ và là để lại như một bài tập.
$$x$$

![Figure 14.1](../../assets/ch14/fig_14_1.png)

**Hình 14.1:** cam tiếp tuyến mặt phẳng là tựa/hỗ trợ siêu phẳng (hyperplane) đến unit hình cầu trong $\mathbb{R}^{3}$ vì điều này hình cầu là hoàn toàn được chứa trong “một vế/cạnh” của tiếp tuyến mặt phẳng. Vì unit hình cầu $B = {z \in E$ | $\|z\|\le 1}$ là đóng và lồi, Minkowski bổ đề nói rằng với mọi $x$ sao cho $\|x\| = 1$, có một ánh xạ afin (affine map) $g$ của tạo thành
$$g(z) = \langle z, w\rangle -\langle x, w\rangle$$
Với $\|w\| = 1$, sao cho g(x) $= 0$ và g(z) $\le 0$ với mọi $z$ sao cho $\|z\|\le 1$. Thì rõ ràng là
$$\sup\langle z, w\rangle = \langle x, w\rangle ,$$
$$\|z\|=1$$
Và do đó
$$\|w\|^{D}= \langle x, w\rangle .$$
Suy ra rằng
$$\langle \rangle$$
$$\|x\|^{DD}\ge \langle w/ \|w\|^{D}, x\rangle = \frac{x, w}{\|w\|^{D}} = 1 = \|x\|$$
Với mọi $x$ sao cho $\|x\| = 1$. Bởi homogeneity, điều này là đúng với mọi $y \in E$, mà các đầy đủ chứng minh trong thực trường hợp. Khi $E$ là phức không gian vectơ (vector space), ta có đến quan điểm unit hình cầu $B$
$$\mathbb{R}^{2n}$$
Như đóng tập lồi (convex set) trong và ta sử dụng sự kiện rằng ở đó là thực ánh xạ afin (affine map) của tạo thành
$$g(z) = \mathfrak{R}\langle z, w\rangle -\mathfrak{R}\langle x, w\rangle$$
Sao cho g(x) $= 0$ và g(z) $\le 0$ với mọi $z$ với $\|z\| = 1$, sao cho $\|w\|^{D} = \mathfrak{R}\langle x, w\rangle$. Nhiều hơn/thêm chi tiết trên đối ngẫu (dual) các chuẩn và unitarily bất biến các chuẩn có thể được tìm thấy trong Horn và Johnson $[98]$ (Các chương $5$ và $7)$.
