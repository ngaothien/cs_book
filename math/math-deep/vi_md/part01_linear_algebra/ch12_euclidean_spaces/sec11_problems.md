# Các bài tập


<!-- PAGE 495 -->

## 12.11 Các bài tập

Bài toán 12.1. $E$ là không gian vectơ (vector space) có số chiều $2$, và cho $(e_{1}, e_{2})$ là cơ sở (basis) của $E$. Chứng minh rằng nếu $> 0$ và $b^{2}$ - ac $< 0$, thì dạng song tuyến tính (bilinear form) được định nghĩa sao cho
$$\phi (x_{1}e_{1} + y_{1}e_{2}, x_{2}e_{1} + y_{2}e_{2}) = ax_{1}x_{2} + b(x_{1}y_{2} + x_{2}y_{1}) + cy_{1}y_{2}$$
Là Euclidean tích vô hướng (inner product).
Bài toán 12.2. Cho $\mathcal{C}[a, b]$ ký hiệu tập hợp của liên tục các hàm $f$: [, $b] \to \mathbb{R}$. Cho trước bất kỳ hai các hàm $f, g \in$ C[, $b]$, cho
$$\langle f, g\rangle = \int_{a}^{}  bf(t)g(t)dt.$$
Chứng minh rằng ở trên dạng song tuyến tính (bilinear form) là thật vậy Euclidean tích vô hướng (inner product).
Bài toán 12.3. Xét tích vô hướng (inner product)
$$\langle f, g\rangle = \int_{-}^{}  \pi f(t)g(t)dt$$
$$\pi$$
Của Bài toán 12.2 trên không gian vectơ (vector space) $\mathcal{C}[-\pi , \pi$ ]. Chứng minh rằng
$$\pi if p = q, p, q \ge 1,$$
$$\langle \sin px, \sin qx\rangle =$$
$$0if p \neq  q, p, q \ge 1,$$
$$\pi if p = q, p, q \ge 1,$$
$$\langle \cos px, \cos qx\rangle =$$
$$0if p \neq  q, p, q \ge 0,$$
$$\langle \sin px, \cos qx\rangle = 0,$$
$$for all p \ge 1 and q \ge 0, and \langle 1, 1\rangle =_{\pi}^{\pi} \int_{-}  dx = 2\pi .$$
Bài toán 12.4. Chứng minh rằng sau đây ma trận là trực giao và phản đối xứng:
$$M = \sqrt \frac{1}{\overline{3}} \begin{pmatrix} 0 & 1 & 1 & 1 \\ -1 & 0 & -1 & 1 \\ -1 & 1 & 0 & -1 \\ 1 & 1 & 1 & 0 \end{pmatrix} .$$
$$--$$
Bài toán 12.5. Cho $E$ và $F$ là hai hữu hạn Các không gian Euclid, cho $(u_{1}, \dots  , u_{n})$ là cơ sở (basis) của $E$, và cho $(v_{1}, \dots  , v_{m})$ là cơ sở (basis) của $F$. Với mọi ánh xạ tuyến tính (linear map) $f$: $E \to F$, nếu $A$ là ma trận của $f$ w.r.t. cơ sở (basis) $(u_{1}, \dots  , u_{n})$ và $B$ là ma trận của $f^{*}$ w.r.t. cơ sở (basis) $(v_{1}, \dots  , v_{m})$, nếu $G_{1}$ là Gram ma trận của tích vô hướng (inner product) trên $E$ (w.r.t. $(u_{1}, \dots  , u_{n}))$ và nếu $G_{2}$ là Gram ma trận của tích vô hướng (inner product) trên $F$ (w.r.t. $(v_{1}, \dots  , v_{m}))$, thì
$$B = G_{1}^{-1} A^{\top}G_{2}.$$

<!-- PAGE 496 -->
Bài toán 12.6. Cho $A$ là ma trận khả nghịch (invertible matrix). Chứng minh rằng nếu $A = Q_{1}R_{1} = Q_{2}R_{2}$ là hai QR-decompositions của $A$ và nếu đường chéo các phần tử (entries) của $R_{1}$ và $R_{2}$ là dương, thì $Q_{1} = Q_{2}$ và $R_{1} = R_{2}$.
Bài toán 12.7. Chứng minh rằng thứ nhất Hadamard bất đẳng thức có thể được deduced từ thứ hai Hadamard bất đẳng thức.
Bài toán 12.8. Cho $E$ là thực không gian vectơ (vector space) của hữu hạn số chiều, $n \ge 1$. Nói rằng hai các cơ sở, $(u_{1}, \dots  , u_{n})$ và $(v_{1}, \dots  , v_{n})$, của $E$ có cùng định hướng khi và chỉ khi det(P) $> 0$, ở đâu $P$ ma trận chuyển cơ sở (change of basis matrix) từ $(u_{1}, \dots  , u_{n})$ đến $(v_{1}, \dots  , v_{n})$, cụ thể là, ma trận có thứ $j$ các cột bao gồm của các tọa độ của $v_{j}$ trên cơ sở (basis) $(u_{1}, \dots  , u_{n})$.
$(1)$ Chứng minh rằng có cùng định hướng là quan hệ tương đương (equivalence relation) với hai các lớp tương đương. định hướng của không gian vectơ (vector space), $E$, là lựa chọn của bất kỳ cố định cơ sở (basis), nói $(e_{1}, \dots  , e_{n})$, của $E$. Bất kỳ khác cơ sở (basis), $(v_{1}, \dots  , v_{n})$, có cùng định hướng như $(e_{1}, \dots  , e_{n})$ (và được nói là dương hoặc trực tiếp) khi và chỉ khi det(P) $> 0$, khác nó được nói đến có opposite định hướng của $(e_{1}, \dots  , e_{n})$ (hoặc là âm hoặc indirect), ở đâu $P$ là ma trận chuyển cơ sở (change of basis matrix) từ $(e_{1}, \dots  , e_{n})$ đến $(v_{1}, \dots  , v_{n})$. được định hướng không gian vectơ (vector space) là không gian vectơ (vector space) với một số được chọn định hướng (dương cơ sở (basis)).
$(2)$ Cho $B_{1} = (u_{1}, \dots  , u_{n})$ và $B_{2} = (v_{1}, \dots  , v_{n})$ là hai các cơ sở trực chuẩn. Với mọi dãy của các vectơ, $(w_{1}, \dots  , w_{n})$, trong $E$, cho $det_{B1}(w_{1}, \dots  , w_{n})$ là định thức (determinant) của ma trận có các cột là các tọa độ của $w_{j}’s$ trên cơ sở (basis) $B_{1}$ và tương tự cho $det_{B2}(w_{1}, \dots  , w_{n})$. Chứng minh rằng nếu $B_{1}$ và $B_{2}$ có cùng định hướng, thì
$$det_{B1}(w_{1}, \dots  , w_{n}) = det_{B2}(w_{1}, \dots  , w_{n}).$$
Cho trước bất kỳ được định hướng không gian vectơ (vector space), $E$, với mọi dãy của các vectơ, $(w_{1}, \dots  , w_{n})$, trong $E$, chung/phổ biến giá trị, $det_{B}(w_{1}, \dots  , w_{n})$, với mọi dương các cơ sở trực chuẩn, $B$, của $E$ được ký hiệu là
$$\lambda_{E} (w_{1}, \dots  , w_{n})$$
Và được gọi là thể tích tạo thành của $(w_{1}, \dots  , w_{n})$.
$(3)$ Cho trước bất kỳ Euclidean được định hướng không gian vectơ (vector space), $E$, có số chiều $n$ với mọi $n$ - $1$ các vectơ, $w_{1}, \dots  , w_{n-1}$, trong $E$, kiểm tra rằng ánh xạ
$$x \mapsto \lambda_{E} (w_{1}, \dots  , w_{n-1}, x)$$
Là dạng tuyến tính (linear form). Thì chứng minh rằng tồn tại duy nhất một vectơ, được ký hiệu $w_{1} \times  \cdots  \times  w_{n-1}$, sao cho
$$\lambda_{E} (w_{1}, \dots  , w_{n-1}, x) = (w_{1} \times  \cdots  \times  w_{n-1}) \cdot  x,$$
Với mọi $x \in E$. vectơ $w_{1} \times  \cdots  \times  w_{n-1}$ được gọi là cross-product của $(w_{1}, \dots  , w_{n-1})$. Nó là
$$\mathbb{R}^{3}$$
Tổng quát hóa của cross-product trong (khi $n = 3)$.

<!-- PAGE 497 -->
Bài toán 12.9. Cho trước $p$ các vectơ $(u_{1}, \dots  , u_{p})$ trong Không gian Euclid (Euclidean space) $E$ có số chiều $n \ge p$, Gram định thức (determinant) (hoặc Gramian) của các vectơ $(u_{1}, \dots  , u_{p})$ là định thức (determinant)
$$\|u_{1}\|^{2}\langle u_{1}, u_{2}\rangle \dots \langle u_{1}, u_{p}\rangle$$
$$\langle u_{2}, u_{1}\rangle \|u_{2}\|^{2}\dots \langle u_{2}, u_{p}\rangle$$
$$Gram(u_{1}, \dots  , u_{p}) =\vdots \vdots \ddots \vdots .$$
$$\langle u_{p}, u_{1}\rangle \langle u_{p}, u_{2}\rangle \dots \|u_{p}\|^{2}$$
$(1)$ Chứng minh rằng
$$Gram(u_{1}, \dots  , u_{n}) = \lambda_{E} (u_{1}, \dots  , u_{n})^{2}.$$
Hint. Nếu $(e_{1}, \dots  , e_{n})$ là cơ sở trực chuẩn (orthonormal basis) và $A$ là ma trận của các vectơ $(u_{1}, \dots  , u_{n})$ trên cơ sở (cơ sở (basis)) này,
$$\det(A)^{2}= \det(A^{\top}A) = \det(A^{i}\cdot  A^{j}),$$
Ở đâu $A^{i}$ ký hiệu cột thứ $i$ của ma trận $A$, và $(A^{i} \cdot  A^{j})$ ký hiệu ma trận cỡ $n \times  n$ với các phần tử (entries) $A^{i} \cdot  A^{j}$.
$(2)$ Chứng minh rằng
$$\|u_{1} \times  \cdots  \times  u_{n-1}\|^{2}= Gram(u_{1}, \dots  , u_{n-1}).$$
Hint. Đặt $w = u_{1} \times  \cdots  \times  u_{n-1}$, nhận thấy rằng
$$\lambda_{E} (u_{1}, \dots  , u_{n-1}, w) = \langle w, w\rangle = \|w\|^{2},$$
Và chỉ ra rằng
$$\|w\|^{4}= \lambda_{E} (u_{1}, \dots  , u_{n-1}, w)^{2}= Gram(u_{1}, \dots  , u_{n-1}, w)$$
$$= Gram(u_{1}, \dots  , u_{n-1})\|w\|^{2}.$$
Bài toán 12.10. Cho $\phi$: $E \times  E \to \mathbb{R}$ là dạng song tuyến tính (bilinear form) trên thực không gian vectơ (vector space) $E$ của hữu hạn số chiều $n$. Cho trước bất kỳ cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $E$, cho $A = (a_{i j})$ là ma trận được định nghĩa sao cho
$$a_{i j} = \phi (e_{i}, e_{j}),$$
$1 \le i, j \le n$. Ta gọi $A$ ma trận của $\phi$ w.r.t. cơ sở (basis) $(e_{1}, \dots  , e_{n})$.
$(1)$ Với mọi hai các vectơ $x$ và $y$, nếu $X$ và $Y$ ký hiệu các vectơ cột của các tọa độ của $x$ và $y$ w.r.t. cơ sở (basis) $(e_{1}, \dots  , e_{n})$, chứng minh rằng
$$\phi (x, y) = X^{\top}AY.$$
$(2)$ Nhắc lại rằng $A$ là ma trận đối xứng (symmetric matrix) nếu $A = A^{\top}$. Chứng minh rằng $\phi$ là đối xứng nếu $A$ là ma trận đối xứng (symmetric matrix).
$(3)$ Nếu $(f_{1}, \dots  , f_{n})$ là một cái khác cơ sở (basis) của $E$ và $P$ là ma trận chuyển cơ sở (change of basis matrix) từ $(e_{1}, \dots  , e_{n})$ đến $(f_{1}, \dots  , f_{n})$, chứng minh rằng ma trận của $\phi$ w.r.t. cơ sở (basis) $(f_{1}, \dots  , f_{n})$ là
$$P^{\top} AP.$$
Chung/phổ biến hạng (rank) của tất cả các ma trận biểu diễn $\phi$ được gọi là hạng (rank) của $\phi$.

<!-- PAGE 498 -->
Bài toán 12.11. Cho $\phi$: $E \times  E \to \mathbb{R}$ là dạng song tuyến tính đối xứng trên thực không gian vectơ (vector space) $E$ của hữu hạn số chiều $n$. Hai các vectơ $x$ và $y$ được nói là liên hợp hoặc trực giao w.r.t. $\phi$ nếu $\phi (x, y) = 0$. chính mục đích của bài toán này là để chứng minh rằng có một cơ sở (basis) của các vectơ rằng là đôi một liên hợp w.r.t. $\phi$.
$(1)$ Chứng minh rằng nếu $\phi (x, x) = 0$ với mọi $x \in E$, thì $\phi$ là một cách đồng nhất null trên $E$. Ngược lại, ta có thể giả sử rằng tồn tại một vectơ $x \in E$ sao cho $\phi (x, x) \neq  0$. Sử dụng quy nạp để chứng minh rằng có một cơ sở (basis) của các vectơ $(u_{1}, \dots  , u_{n})$ rằng là đôi một liên hợp w.r.t. $\phi$. Hint. Cho quy nạp bước, tiến hành như sau. Cho $(u_{1}, e_{2}, \dots  , e_{n})$ là cơ sở (basis) của $E$, với $\phi (u_{1}, u_{1}) \neq  0$. Chứng minh rằng có các vô hướng $\lambda_{2} , \dots  , \lambda_{n}$ sao cho mỗi của các vectơ
$$v_{i} = e_{i} + \lambda_{i} u_{1}$$
Là liên hợp đến $u_{1}$ w.r.t. $\phi$, ở đâu $2 \le i \le n$, và rằng $(u_{1}, v_{2}, \dots  , v_{n})$ là cơ sở (basis).
$(2)$ Cho $(e_{1}, \dots  , e_{n})$ là cơ sở (basis) của các vectơ rằng là đôi một liên hợp w.r.t. $\phi$ và giả sử rằng chúng được thứ tự sao cho
$$\theta_{i}  \neq  0if 1 \le i \le r,$$
$$\phi (e_{i}, e_{i}) =$$
$$0if r + 1 \le i \le n,$$
Ở đâu $r$ là hạng (rank) của $\phi$. Chỉ ra rằng ma trận của $\phi$ w.r.t. $(e_{1}, \dots  , e_{n})$ là ma trận đường chéo (diagonal matrix), và rằng
$$\phi (x, y) = \sum_{i=1}^{r}  \theta_{i} x_{i}y_{i},$$
$$where x = \sum_{i}  n=1 x_{i}e_{i} and y = \sum  ni=1 y_{i}e_{i}.$$
Chứng minh rằng với mọi ma trận đối xứng (symmetric matrix) $A$, có một ma trận khả nghịch (invertible matrix) $P$ sao cho
$$P^{\top} AP = D,$$
Ở đâu $D$ là ma trận đường chéo (diagonal matrix).
$(3)$ Chứng minh rằng có một số nguyên $p, 0 \le p \le r$ (ở đâu $r$ là hạng (rank) của $\phi$), sao cho $\phi (u_{i}, u_{i}) > 0$ cho chính xác $p$ các vectơ của mọi cơ sở (basis) $(u_{1}, \dots  , u_{n})$ của các vectơ rằng là đôi một liên hợp w.r.t. $\phi$ (Sylvester’s inertia định lý). Tiến hành như sau. Giả sử rằng trong cơ sở (basis) $(u_{1}, \dots  , u_{n})$, với mọi $x \in E$, ta có
$$\phi (x, x) = \alpha_{1} x_{1}^{2} + \cdots  + \alpha_{p} x_{p}^{2} -\alpha_{p+1} x_{p+1}^{2} -\cdots  -\alpha_{r} x_{r}^{2},$$
$$where x = \sum_{i}  n=1 x_{i}u_{i}, and that in the basis (v_{1}, \dots  , v_{n}), for any x \in E, we have$$
$$\phi (x, x) = \beta_{1} y_{1}^{2} + \cdots  + \beta_{q} y_{q}^{2} -\beta_{q+1} y_{q+1}^{2} -\cdots  -\beta_{r} y_{r}^{2},$$

<!-- PAGE 499 -->
$$where x = \sum_{i}  n=1 y_{i}v_{i}, with \alpha_{i}  > 0, \beta_{i}  > 0, 1 \le i \le r.$$
Giả sử rằng $p > q$ và derive một mâu thuẫn. Thứ nhất xét $x$ trong không gian con $F$ được sinh (spanned) bởi
$$(u_{1}, \dots  , u_{p}, u_{r+1}, \dots  , u_{n}),$$
Và nhận thấy rằng $\phi (x, x) \ge 0$ nếu $x \neq  0$. Tiếp theo xét $x$ trong không gian con $G$ được sinh (spanned) bởi
$$(v_{q+1}, \dots  , v_{r}),$$
Và nhận thấy rằng $\phi (x, x) < 0$ nếu $x \neq  0$. Chứng minh rằng $F \cap G$ là không tầm thường (i.e., chứa một số khác không vectơ), và derive một mâu thuẫn. Điều này suy ra rằng $p \le q$. Hoàn tất chứng minh. cặp $(p, r$ - $p)$ được gọi là signature của $\phi$.
$(4) A$ dạng song tuyến tính đối xứng $\phi$ là xác định nếu với mọi $x \in E$, nếu $\phi (x, x) = 0$, thì $x = 0$. Chứng minh rằng dạng song tuyến tính đối xứng là xác định khi và chỉ khi của nó signature là hoặc $(n, 0)$ hoặc $(0, n)$. Nói cách khác, đối xứng xác định dạng song tuyến tính (bilinear form) có hạng (rank) $n$ và là hoặc dương hoặc âm.
Bài toán 12.12. Xét $n \times  n$ các ma trận $R^{i,j}$ được định nghĩa với mọi $i, j$ với $1 \le i < j \le n$ và $n \ge 3$, sao cho chỉ khác không các phần tử (entries) là
$$R^{i,j}(i, j) = -1$$
$$R^{i,j}(i, i) = 0$$
$$R^{i,j}(j, i) = 1$$
$$R^{i,j}(j, j) = 0$$
$$R^{i,j}(k, k) = 1,1 \le k \le n, k \neq  i, j.$$
Ví dụ,
$$R^{i,j} = \begin{pmatrix} 1 \\ \ddots \\ 1 \\ 0 & 0 & \cdots & 0 & -1 \\ 0 & 1 & \cdots & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & 1 & 0 \\ 1 & 0 & \cdots & 0 & 0 \\ 1 \\ \ddots \\ 1 \end{pmatrix} .$$
$(1)$ Chứng minh rằng $R^{i,j}$ là các ma trận quay. Sử dụng các ma trận $R^{ij}$ đến tạo thành cơ sở (basis) của $n \times  n$ các ma trận phản đối xứng.

<!-- PAGE 500 -->
$(2)$ Xét $n \times  n$ các ma trận đối xứng $S^{i,j}$ được định nghĩa với mọi $i, j$ với $1 \le i < j \le n$ và $n \ge 3$, sao cho chỉ khác không các phần tử (entries) là
$$S^{i,j}(i, j) = 1$$
$$S^{i,j}(i, i) = 0$$
$$S^{i,j}(j, i) = 1$$
$$S^{i,j}(j, j) = 0$$
$$S^{i,j}(k, k) = 1,1 \le k \le n, k \neq  i, j,$$
Và nếu $i + 2 \le j$ thì $S^{i,j}(i + 1, i + 1) = -1$, khác nếu $i > 1$ và $j = i + 1$ thì $S^{i,j}(1, 1) = -1$, và nếu $i = 1$ và $j = 2$, thì $S^{i,j}(3, 3) = -1$. Ví dụ,
$$S^{i,j} = \begin{pmatrix} 1 \\ \ddots \\ 1 \\ 0 & 0 & \cdots & 0 & 1 \\ 0 & -1 & \cdots & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & 1 & 0 \\ 1 & 0 & \cdots & 0 & 0 \\ 1 \\ \ddots \\ 1 \end{pmatrix} .$$
Lưu ý rằng $S^{i,j}$ có đơn lẻ đường chéo phần tử (entry) bằng $-1$. Chứng minh rằng $S^{i,j}$ là các phép quay các ma trận. Sử dụng Bài toán 3.15 cùng với $S^{i,j}$ đến tạo thành cơ sở (basis) của $n \times  n$ các ma trận đối xứng.
$(3)$ Chứng minh rằng nếu $n \ge 3$, tập hợp tất cả các tổ hợp tuyến tính của các ma trận trong Do đó(n) là không gian $M_{n}(\mathbb{R})$ của tất cả $n \times  n$ các ma trận. Chứng minh rằng nếu $n \ge 3$ và nếu ma trận $A \in M_{n}(\mathbb{R})$ giao hoán với tất cả các phép quay các ma trận, thì $A$ giao hoán với tất cả các ma trận trong $M_{n}(\mathbb{R})$. Những gì xảy ra cho $n = 2$?
$$\mathbb{R}^{n}$$
Bài toán 12.13. $(1)$ Cho $H$ là afin siêu phẳng (hyperplane) trong cho trước bởi phương trình
$$a_{1}x_{1} + \cdots  + a_{n}x_{n} = c,$$
Với $a_{i} \neq  0$ với một số $i, 1 \le i \le n$. tuyến tính siêu phẳng (hyperplane) $H_{0}$ song song đến $H$ được cho bởi phương trình
$$a_{1}x_{1} + \cdots  + a_{n}x_{n} = 0,$$

<!-- PAGE 501 -->
$$\mathbb{R}^{n}$$
Và ta nói rằng vectơ $y \in$ là trực giao (hoặc vuông góc) đến $H$ khi và chỉ khi $y$ là trực giao đến $H_{0}$. Cho $h$ là giao của $H$ với đường thẳng qua gốc và vuông góc đến $H$. Chứng minh rằng các tọa độ của $h$ được cho bởi
$$\frac{c}{a_{1}^{2}+ \cdots  + a_{n}^{2}} (a_{1}, \dots  , a_{n}).$$
$(2)$ Với mọi điểm $p \in H$, chứng minh rằng $\|h\|\le \|p\|$. Do đó, nó là tự nhiên để định nghĩa khoảng cách d(O, $H)$ từ gốc $O$ đến siêu phẳng (hyperplane) $H$ như d(O, $H) = \|h\|$. Chứng minh rằng
$$||$$
$$d(O, H) = \frac{c}{(a_{1}^{2}+ \cdots  + a_{n}^{2}\overline{)}_{2}^{1}} .$$
$(3)$ Cho $S$ là hữu hạn tập hợp của $n \ge 3$ các điểm trong mặt phẳng $(\mathbb{R}^{2})$. Chứng minh rằng nếu với mọi cặp của phân biệt các điểm $p_{i}, p_{j} \in S$, có một thứ ba điểm $p_{k} \in S$ (phân biệt từ $p_{i}$ và $p_{j})$ sao cho $p_{i}, p_{j}, p_{k}$ thuộc đến cùng (afin) đường thẳng, thì tất cả các điểm trong $S$ thuộc đến chung/phổ biến (afin) đường thẳng. Hint. Tiến hành bởi mâu thuẫn và sử dụng minimality lập luận. Điều này là hoặc $\infty$ -khó hoặc một cách tương đối dễ, tùy thuộc cách mà bạn tiến hành!
Bài toán 12.14. (không gian của đóng các đa giác trong $\mathbb{R}^{2}$, sau Hausmann và Knutson) mở đa giác $P$ trong mặt phẳng là dãy $P = (v_{1}, \dots  , v_{n+1})$ của các điểm $v_{i} \in \mathbb{R}^{2}$ được gọi là các đỉnh (với $n \ge 1)$. đóng đa giác, cho ngắn đa giác, là mở đa giác $P = (v_{1}, \dots  , v_{n+1})$ sao cho $v_{n+1} = v_{1}$. dãy của cạnh các vectơ $(e_{1}, \dots  , e_{n})$ liên kết với mở (hoặc đóng) đa giác $P = (v_{1}, \dots  , v_{n+1})$ được định nghĩa bởi
$$e_{i} = v_{i+1} -v_{i},i = 1, \dots  , n.$$
Do đó, đóng hoặc mở đa giác cũng được định nghĩa bởi cặp $(v_{1}, (e_{1}, \dots  , e_{n}))$, với các đỉnh cho trước bởi
$$v_{i+1} = v_{i} + e_{i},i = 1, \dots  , n.$$
Nhận thấy rằng đa giác $(v_{1}, (e_{1}, \dots  , e_{n}))$ là đóng khi và chỉ khi
$$e_{1} + \cdots  + e_{n} = 0.$$
Vì mọi đa giác $(v_{1}, (e_{1}, \dots  , e_{n}))$ có thể được translated bởi $-v_{1}$, sao cho $v_{1} = (0, 0)$, ta có thể giả sử rằng của ta các đa giác là specified bởi dãy của cạnh các vectơ.
$$\mathbb{R}^{2}  \mathbb{C}$$
Nhắc lại rằng mặt phẳng là đẳng cấu đến, thông qua đẳng cấu
$$(x, y) \mapsto x + iy.$$
Ta sẽ biểu diễn mỗi cạnh vectơ $e_{k}$ bởi square của phức số $w_{k} = a_{k}+ib_{k}$. Do đó, mọi dãy của phức các số $(w_{1}, \dots  , w_{n})$ định nghĩa đa giác (cụ thể là, $(w_{1}^{2}, \dots  , w_{n}^{2}))$.

<!-- PAGE 502 -->
Biểu diễn này là many-to-one: các dãy $(\pm w_{1}, \dots  , \pm w_{n})$ mô tả cùng đa giác. Đến mọi dãy của phức các số $(w_{1}, \dots  , w_{n})$, ta associate cặp của các vectơ (, $b)$, với, $b \in \mathbb{R}^{n}$, sao cho nếu $w_{k} = a_{k} + ib_{k}$, thì
$$a = (a_{1}, \dots  , a_{n}),b = (b_{1}, \dots  , b_{n}).$$
Ánh xạ
$$(w_{1}, \dots  , w_{n}) \mapsto (a, b)$$
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
Là rõ ràng song ánh, do đó ta có thể cũng biểu diễn các đa giác bởi các cặp của các vectơ (, $b) \in \times$.
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
$(1)$ Chứng minh rằng đa giác $P$ được biểu diễn bởi cặp của các vectơ (, $b) \in \times$ là đóng khi và chỉ khi $a \cdot  b = 0$ và $\|a\|_{2} = \|b\|_{2}$.
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
$(2)$ Cho trước đa giác $P$ được biểu diễn bởi cặp của các vectơ (, $b) \in \times$, độ dài l(P) của đa giác $P$ được định nghĩa bởi l(P) $= |w_{1}|^{2} + \cdots  + |w_{n}|^{2}$, với $w_{k} = a_{k} + ib_{k}$. Chứng minh rằng
$$l(P) = \|a\|_{2}^{2} + \|b\|_{2}^{2} .$$
Suy ra từ () và $(b)$ rằng mọi đóng đa giác của độ dài $2$ với $n$ các cạnh được biểu diễn bởi một ma trận cỡ $n \times  2$ $A$ sao cho $A^{\top}A =$ I.
Nhận xét: không gian của tất cả $n \times  2$ thực các ma trận $A$ sao cho $A^{\top}A =$ I là không gian đã biết như Stiefel đa tạp (manifold) S(2, $n)$.
$(3)$ Nhắc lại rằng trong $\mathbb{R}^{2}$, phép quay của góc $\theta$ specified bởi ma trận
$$R_{\theta} = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$$
Được biểu diễn theo phức các số bởi ánh xạ
$$z \mapsto ze^{i\theta}.$$
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
Cho $P$ là đa giác được biểu diễn bởi cặp của các vectơ (, $b) \in \times$. Chứng minh rằng đa giác $R_{\theta}(P)$ thu được bằng cách áp dụng phép quay $R_{\theta}$ đến mọi đỉnh $w_{k}^{2} = (a_{k} + ib_{k})^{2}$ của $P$ là specified bởi cặp của các vectơ
$$(\cos(\theta /2)a -\sin(\theta /2)b, \sin(\theta /2)a + \cos(\theta /2)b) = \begin{pmatrix} a_{1} & b_{1} \\ a_{2} & b_{2} \\ \vdots & \vdots \\ a_{n} & b_{n} \end{pmatrix} \begin{pmatrix} \cos(\theta /2) & \sin(\theta /2) \\ -\sin(\theta /2) & \cos(\theta /2) \end{pmatrix} .$$
$(4)$ phép đối xứng (reflection) $\rho_{x}$ về trục $x$ tương ứng với ánh xạ
$$z \mapsto \overline{z,}$$

<!-- PAGE 503 -->
Có ma trận là,
$$\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} .$$
Chứng minh rằng đa giác $\rho_{x} (P)$ thu được bằng cách áp dụng phép đối xứng (reflection) $\rho_{x}$ đến mọi đỉnh $w_{k}^{2} = (a_{k} + ib_{k})^{2}$ của $P$ là specified bởi cặp của các vectơ
$$(a, -b) = \begin{pmatrix} a_{1} & b_{1} \\ a_{2} & b_{2} \\ \vdots & \vdots \\ a_{n} & b_{n} \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} .$$
$(5)$ Cho $Q \in$ O(2) là bất kỳ phép đẳng cự (isometry) sao cho det(Q) $= -1$ (phép đối xứng (reflection)). Chứng minh rằng có một phép quay $R_{-\theta} \in$ Do đó(2) sao cho
$$Q = \rho_{x}  \circ R_{-\theta}.$$
Chứng minh rằng phép đẳng cự (isometry) $Q$, mà được cho bởi ma trận
$$Q = \begin{pmatrix} \cos \theta & \sin \theta \\ \sin \theta & -\cos \theta \end{pmatrix} ,$$
Là phép đối xứng (reflection) về đường thẳng tương ứng với góc $\theta /2$ (đường thẳng của phương trình $y = tan(\theta /2)x)$. Chứng minh rằng đa giác Q(P) thu được bằng cách áp dụng phép đối xứng (reflection) $Q = \rho_{x}  \circ R_{-\theta}$ đến mọi đỉnh $w_{k}^{2} = (a_{k} + ib_{k})^{2}$ của $P$, là specified bởi cặp của các vectơ
$$(\cos(\theta /2)a + \sin(\theta /2)b, \sin(\theta /2)a -\cos(\theta /2)b) = \begin{pmatrix} a_{1} & b_{1} \\ a_{2} & b_{2} \\ \vdots & \vdots \\ a_{n} & b_{n} \end{pmatrix} \begin{pmatrix} \cos(\theta /2) & \sin(\theta /2) \\ \sin(\theta /2) & -\cos(\theta /2) \end{pmatrix} .$$
$(6)$ Định nghĩa quan hệ tương đương (equivalence relation) $\sim$ trên S(2, $n)$ sao cho nếu $A_{1}, A_{2} \in$ S(2, $n)$ là bất kỳ $n\times 2$ các ma trận sao cho $A_{1}^{\top} A_{1} = A_{2}^{\top} A_{2} =$ I, thì
$$A_{1} \sim A_{2}iff A_{2} = A_{1}Qfor some Q \in O(2).$$
Chứng minh rằng thương G(2, $n) =$ S(2, $n)/ \sim$ là trong song ánh với tập hợp tất cả 2-dimensional các không gian con (các mặt phẳng) của $\mathbb{R}^{n}$. không gian G(2, $n)$ được gọi là một Grassmannian đa tạp (manifold). Chứng minh rằng sai khác các phép tịnh tiến và các phép đẳng cự trong O(2) (các phép quay và các phép đối xứng), n-sided đóng các đa giác của độ dài $2$ được biểu diễn bởi các mặt phẳng trong G(2, $n)$.

<!-- PAGE 504 -->
Bài toán 12.15. $(1)$ Tìm hai các ma trận đối xứng, $A$ và $B$, sao cho $AB$ là không đối xứng.
$(2)$ Tìm hai các ma trận $A$ và $B$ sao cho
$$e^{A}e^{B}\neq  e^{A+B}.$$
Hint. Thử
$$A = \pi \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix} andB = \pi \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix} ,$$
$$-$$
Và sử dụng Rodrigues công thức.
$(3)$ Tìm một số các ma trận vuông $A, B$ sao cho $AB \neq$ BA, vẫn chưa
$$e^{A}e^{B}= e^{A+B}.$$
Hint. Nhìn cho $2 \times  2$ các ma trận với không vết (trace) và sử dụng Bài toán 9.15.
Bài toán 12.16. Cho trước trường $K$ và bất kỳ khác rỗng tập hợp $I$, cho $K^{(I)}$ là tập con của cartesian tích $K^{I}$ bao gồm của tất cả các hàm $\lambda$: I $\to K$ với hữu hạn hỗ trợ/giá (support), mà có nghĩa là $\lambda (i) = 0$ với mọi nhưng một cách hữu hạn nhiều $i \in$ I. Ta thường ký hiệu hàm được định nghĩa bởi $\lambda$ như $(\lambda_{i} )_{i\in I}$, và gọi là họ được chỉ số bởi I. Ta định nghĩa phép cộng và phép nhân bởi vô hướng (scalar) như sau:
$$(\lambda_{i} )_{i\in I} + (\mu_{i} )_{i\in I} = (\lambda_{i}  + \mu_{i} )_{i\in I},$$
Và
$$\alpha  \cdot  (\mu_{i} )_{i\in I} = (\alpha \mu_{i} )_{i\in I}.$$
$(1)$ Kiểm tra rằng $K^{(I)}$ là không gian vectơ (vector space).
$(2)$ Nếu I là bất kỳ khác rỗng tập con, với mọi $i \in$ I, ta ký hiệu bởi $e_{i}$ họ $(e_{j})_{j\in I}$ được định nghĩa sao cho
$$($$
$$1if j = i$$
$$e_{j} =$$
$$0if j \neq  i.$$
Chứng minh rằng họ $(e_{i})_{i\in I}$ là độc lập tuyến tính (linearly independent) và sinh ra $K^{(I)}$, sao cho nó là cơ sở (basis) của $K^{(I)}$ được gọi là cơ sở chính tắc (canonical basis) của $K^{(I)}$. Khi I là hữu hạn, nói của cardinality $n$, thì chứng minh rằng $K^{(I)}$ là đẳng cấu đến $K^{n}$.
$(3)$ hàm $\iota$: I $\to K^{(I)}$, sao cho $\iota (i) = e_{i}$ với mọi $i \in$ I, là rõ ràng đơn ánh. Với mọi khác không gian vectơ (vector space) $F$, với mọi hàm $f$: I $\to F$, chứng minh rằng tồn tại duy nhất một ánh xạ tuyến tính (linear map) $\overline{f}\overline{:} K^{(I)} \to F$, sao cho
$$f =\overline{f} \circ \iota ,$$
Như trong sau đây giao hoán biểu đồ:
$$I\overline{C} K^{(I)}.$$
$$\overline{C}^{\iota}\overline{C}$$
$$CC$$
$$CC$$
$$CC^{f}$$
$$f!$$
$$F$$

<!-- PAGE 505 -->
Ta gọi không gian vectơ (vector space) $K^{(I)}$ không gian vectơ (vector space) một cách tự do được sinh bởi tập hợp $I$.
Bài toán 12.17. (Một số pitfalls của vô hạn số chiều) Cho $E$ là không gian vectơ (vector space) một cách tự do được sinh bởi tập hợp của tự nhiên các số, $\mathbb{N} = {0, 1, 2, \dots$ }, và cho $(e_{0}, e_{1}, e_{2}, \dots  , e_{n}, \dots$) là của nó cơ sở chính tắc (canonical basis). Ta định nghĩa hàm $\phi$ sao cho
$$\delta_{ij} if i, j \ge 1,$$
$$$$
$$$$
$$1if i = j = 0,$$
$$$$
$$\phi (e_{i}, e_{j}) =$$
$$1/2^{j}if i = 0, j \ge 1,$$
$$$$
$$$$
$$1/2^{i}if i \ge 1, j = 0,$$
$$$$
$$and we extend \phi  by bilinearity to a function \phi : E\times E \to K. This means that if u = \sum_{i}  \in \mathbb{N} \lambda_{i} e_{i}$$
$$and v = \sum_{j}  \in \mathbb{N} \mu_{j} e_{j}, then$$
$$\phi \begin{pmatrix} \lambda_{i} e_{i}, & \mu_{j} e_{j} \end{pmatrix} \sum_{i\in N}  \sum_{j\in N}  = \sum_{i,j\in N}  \lambda_{i} \mu_{j} \phi (e_{i}, e_{j}),$$
Nhưng nhớ rằng $\lambda_{i}  \neq  0$ và $\mu_{j}  \neq  0$ chỉ cho một cách hữu hạn nhiều các chỉ số $i, j$.
$(1)$ Chứng minh rằng $\phi$ là xác định dương (positive definite), sao cho nó là tích vô hướng (inner product) trên $E$. Những gì sẽ xảy ra nếu ta đã thay đổi $1/2^{j}$ đến $1$ (hoặc bất kỳ hằng số)?
$(2)$ Cho $H$ là không gian con của $E$ được sinh (spanned) bởi họ $(e_{i})_{i\ge1}$, siêu phẳng (hyperplane) trong $E$. Tìm $H^{\perp}$ và $H^{\perp \perp}$, và chứng minh rằng
$$H \neq  H^{\perp \perp}.$$
$(3)$ Cho $U$ là không gian con của $E$ được sinh (spanned) bởi họ $(e_{2i})_{i\ge1}$, và cho $V$ là không gian con của $E$ được sinh (spanned) bởi họ $(e_{2i-1})_{i\ge1}$. Chứng minh rằng
$$U^{\perp} = V$$
$$V^{\perp} = U$$
$$U^{\perp \perp} = U$$
$$V^{\perp \perp} = V,$$
Vẫn chưa
$$(U \cap V )^{\perp}\neq  U^{\perp}+ V^{\perp}$$
Và
$$(U + V )^{\perp \perp}\neq  U + V.$$
Nếu $W$ là không gian con được sinh (spanned) bởi $e_{0}$ và $e_{1}$, chứng minh rằng
$$(W \cap H)^{\perp}\neq  W^{\perp}+ H^{\perp}.$$

<!-- PAGE 506 -->
$(4)$ Xét không gian đối ngẫu (dual space) $E^{*}$ của $E$, và cho $(e_{i}^{*} )_{i\in N}$ là họ của đối ngẫu (dual) các dạng của cơ sở (basis) $(e_{i})_{i\in N}$. Kiểm tra rằng họ $(e_{i}^{*} )_{i\in N}$ là độc lập tuyến tính (linearly independent).
$(5)$ Cho $f \in E^{*}$ là dạng tuyến tính (linear form) được định nghĩa bởi
$$f(e_{i}) = 1for all i \in \mathbb{N}.$$
Chứng minh rằng $f$ là không trong không gian con được sinh (spanned) bởi $e_{i}^{*}$. Nếu $F$ là không gian con của $E^{*}$ được sinh (spanned) bởi $e_{i}^{*}$ và $f$, tìm $F^{0}$ và $F^{00}$, và chứng minh rằng
$$F \neq  F^{00} .$$
