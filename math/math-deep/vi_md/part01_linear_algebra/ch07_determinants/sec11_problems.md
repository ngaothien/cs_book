# Các bài tập


<!-- PAGE 251 -->

## 7.10 Further Readings

Kỹ lưỡng các trình bày của material được phủ trong Chương 3–6 và $7$ có thể được tìm thấy trong Strang $[176, 175]$, Lax $[117]$, Lang $[113]$, Artin $[7]$, Mac Lane và Birkhoff[122], Hoffman và Kunze $[97]$, Dummit và Foote $[55]$, Bourbaki $[25, 26]$, Van Der Waerden $[185]$, Serre $[162]$, Horn và Johnson $[98]$, và Bertin $[15]$. Các phần tử này các khái niệm của tuyến tính đại số là một cách đẹp đặt để sử dụng trong cổ điển hình học, xem Berger $[11, 12]$, Tisseron $[181]$ và Dieudonn´e $[49]$.

## 7.11 Các bài tập

Bài toán 7.1. Chứng minh rằng mọi phép chuyển vị có thể được viết dưới dạng tích của cơ bản các phép chuyển vị.
$$\mathbb{R}^{2}$$
Bài toán 7.2. $(1)$ Cho trước hai các vectơ trong của các tọa độ $(c_{1}-a_{1}, c_{2}-a_{2})$ và $(b_{1}-a_{1}, b_{2}-a_{2})$, chứng minh rằng chúng là phụ thuộc tuyến tính (linearly dependent) khi và chỉ khi
$$a_{1}b_{1}c_{1}$$
$$a_{2}b_{2}c_{2}= 0.$$
$$111$$
$$\mathbb{R}^{3}$$
$(2)$ Cho trước ba các vectơ trong của các tọa độ $(d_{1}-a_{1}, d_{2}-a_{2}, d_{3}-a_{3}), (c_{1}-a_{1}, c_{2}-a_{2}, c_{3}-a_{3})$, và $(b_{1}$ - $a_{1}, b_{2}$ - $a_{2}, b_{3}$ - $a_{3})$, chứng minh rằng chúng là phụ thuộc tuyến tính (linearly dependent) khi và chỉ khi
$$a_{1}b_{1}c_{1}d_{1}$$
$$a_{2}b_{2}c_{2}d_{2}$$
$$= 0.$$
$$a_{3}b_{3}c_{3}d_{3}$$
$$1111$$
Bài toán 7.3. Cho $A$ là $(m + n) \times  (m + n)$ ma trận khối (block matrix) (trên bất kỳ trường $K)$ cho trước bởi
$$A = \begin{pmatrix} A_{1} & A_{2} \\ 0 & A_{4} \end{pmatrix} ,$$
Ở đâu $A_{1}$ là một ma trận cỡ $m \times  m$, $A_{2}$ là một ma trận cỡ $m \times  n$, và $A_{4}$ là một ma trận cỡ $n \times  n$. Chứng minh rằng det() $= det(A_{1}) det(A_{4})$. Sử dụng ở trên kết quả để chứng minh rằng nếu $A$ là tam giác trên (upper triangular) $n\times n$ ma trận, thì det() $= a_{11}a_{22} \cdots  a_{nn}$.
Bài toán 7.4. Chứng minh rằng nếu $n \ge 3$, thì
$$\det \begin{pmatrix} 1 + x_{1}y_{1} & 1 + x_{1}y_{2} & \cdots & 1 + x_{1}y_{n} \\ 1 + x_{2}y_{1} & 1 + x_{2}y_{2} & \cdots & 1 + x_{2}y_{n} \\ \vdots & \vdots & \vdots & \vdots \\ 1 + x_{n}y_{1} & 1 + x_{n}y_{2} & \cdots & 1 + x_{n}y_{n} \end{pmatrix} = 0.$$

<!-- PAGE 252 -->
Bài toán 7.5. Chứng minh rằng
$$14916$$
$$491625$$
$$= 0.$$
$$9162536$$
$$16253649$$
Bài toán 7.6. Xét $n \times  n$ ma trận đối xứng (symmetric matrix)
$$A = \begin{pmatrix} 1 & 2 & 0 & 0 & \dots & 0 & 0 \\ 2 & 5 & 2 & 0 & \dots & 0 & 0 \\ 0 & 2 & 5 & 2 & \dots & 0 & 0 \\ \vdots & \vdots & \ddots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & \dots & 2 & 5 & 2 & 0 \\ 0 & 0 & \dots & 0 & 2 & 5 & 2 \\ 0 & 0 & \dots & 0 & 0 & 2 & 5 \end{pmatrix} .$$
$(1)$ Tìm tam giác trên (upper-triangular) ma trận $R$ sao cho $A = R^{\top}R$.
$(2)$ Chứng minh rằng det() $= 1$.
$(3)$ Xét dãy
$$p_{0}(\lambda ) = 1$$
$$p_{1}(\lambda ) = 1 -\lambda$$
$$p_{k}(\lambda ) = (5 -\lambda )p_{k-1}(\lambda ) -4p_{k-2}(\lambda )2 \le k \le n.$$
Chứng minh rằng
$$\det(A -\lambda I) = p_{n}(\lambda ).$$
Nhận xét: Nó có thể được được hiển thị rằng $p_{n}(\lambda$) có $n$ phân biệt (thực) các nghiệm và rằng các nghiệm của $p_{k}(\lambda$) tách các nghiệm của $p_{k+1}(\lambda$).
Bài toán 7.7. Cho $B$ là ma trận cỡ $n \times  n$ $(n \ge 3)$ cho trước bởi
$$B = \begin{pmatrix} 1 & -1 & -1 & -1 & \cdots & -1 & -1 \\ 1 & -1 & 1 & 1 & \cdots & 1 & 1 \\ 1 & 1 & -1 & 1 & \cdots & 1 & 1 \\ 1 & 1 & 1 & -1 & \cdots & 1 & 1 \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ 1 & 1 & 1 & 1 & \cdots & -1 & 1 \\ 1 & 1 & 1 & 1 & \cdots & 1 & -1 \end{pmatrix} .$$
Chứng minh rằng
$$\det(B) = (-1)^{n}(n -2)2^{n-1}.$$

<!-- PAGE 253 -->
Bài toán 7.8. Cho trước trường $K$ (nói $K = \mathbb{R}$ hoặc $K = \mathbb{C})$, cho trước bất kỳ hai các đa thức p(X), q(X) $\in$ K[X], ta nói rằng rằng q(X) chia hết p(X) (và rằng p(X) là bội của q(X)) khi và chỉ khi tồn tại một đa thức s(X) $\in$ K[X] sao cho
$$p(X) = q(X)s(X).$$
Trong trường hợp này ta nói rằng q(X) là nhân tử của p(X), và nếu q(X) có bậc ít nhất một, ta nói rằng q(X) là không tầm thường nhân tử của p(X). Cho f(X) và g(X) là hai các đa thức trong K[X] với
$$f(X) = a_{0}X^{m}+ a_{1}X^{m-1}+ \cdots  + a_{m}$$
Của bậc $m \ge 1$ và
$$g(X) = b_{0}X^{n}+ b_{1}X^{n-1}+ \cdots  + b_{n}$$
Của bậc $n \ge 1$ (với $a_{0}, b_{0} \neq  0)$. Bạn sẽ cần kết quả sau đây mà bạn cần không chứng minh: Hai các đa thức f(X) và g(X) với deg(f) $= m \ge 1$ và deg(g) $= n \ge 1$ có một số chung/phổ biến không tầm thường nhân tử khi và chỉ khi ở đó tồn tại hai khác không các đa thức p(X) và q(X) sao cho
$$fp = gq,$$
Với deg(p) $\le n$ - $1$ và deg(q) $\le m$ - $1$.
$(1)$ Cho $\mathcal{P}_{m}$ ký hiệu không gian vectơ (vector space) của tất cả các đa thức trong K[X] của bậc nhiều nhất $m$ - $1$, và cho $T$: $\mathcal{P}_{n} \times  P_{m} \to P_{m+n}$ là ánh xạ cho trước bởi
$$T(p, q) = fp + gq,p \in P_{n}, q \in P_{m},$$
Ở đâu $f$ và $g$ là một số cố định các đa thức của bậc $m \ge 1$ và $n \ge 1$. Chứng minh rằng ánh xạ $T$ là tuyến tính.
$(2)$ Chứng minh rằng $T$ là không đơn ánh (injective) khi và chỉ khi $f$ và $g$ có chung/phổ biến không tầm thường nhân tử.
$(3)$ Chứng minh rằng $f$ và $g$ có không tầm thường chung/phổ biến nhân tử khi và chỉ khi R(f, $g) = 0$, ở đâu R(f, $g)$ là định thức (determinant) cho trước bởi
$$a_{0}a_{1}\cdots \cdots a_{m}0\cdots \cdots \cdots \cdots 0$$
$$0a_{0}a_{1}\cdots \cdots a_{m}0\cdots \cdots \cdots 0$$
$$\cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots$$
$$\cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots$$
$$\cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots$$
$$R(f, g) =\cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots .$$
$$0\cdots \cdots \cdots \cdots 0a_{0}a_{1}\cdots \cdots a_{m}$$
$$b_{0}b_{1}\cdots \cdots \cdots \cdots \cdots b_{n}0\cdots 0$$
$$0b_{0}b_{1}\cdots \cdots \cdots \cdots \cdots b_{n}0\cdots$$
$$\cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots$$
$$0\cdots 0b_{0}b_{1}\cdots \cdots \cdots \cdots \cdots b_{n}$$

<!-- PAGE 254 -->
Ở trên định thức (determinant) được gọi là resultant của $f$ và $g$. Lưu ý rằng ma trận của resultant là một ma trận cỡ $(n + m) \times  (n + m)$, với hàng thứ nhất (liên quan đến $a_{i}s)$ xảy ra $n$ lần, mỗi time shifted trên đến phải bởi một cột, và $(n +$ 1)th hàng (liên quan đến $b_{j}s)$ xảy ra $m$ lần, mỗi time shifted trên đến phải bởi một cột. Hint. Biểu diễn ma trận của $T$ trên một số phù hợp cơ sở (basis).
$(4)$ Tính resultant trong sau đây ba các trường hợp:
() $m = n = 1$, và viết f(X) $=$ aX $+ b$ và g(X) $=$ cX $+ d$.
$(b) m = 1$ và $n \ge 2$ tùy ý.
$(c)$ f(X) $= aX^{2} +$ bX $+ c$ và g(X) $=$ 2aX $+ b$.
$(5)$ Tính resultant của f(X) $= X^{3} +$ pX $+ q$ và g(X) $= 3X^{2} + p$, và
$$f(X) = a_{0}X^{2}+ a_{1}X + a_{2}$$
$$g(X) = b_{0}X^{2}+ b_{1}X + b_{2}.$$
Trong trường hợp thứ hai, bạn nên thu được
$$4R(f, g) = (2a_{0}b_{2} -a_{1}b_{1} + 2a_{2}b_{0})^{2}-(4a_{0}a_{2} -a_{1}^{2})(4b_{0}b_{2} -b_{1}^{2}).$$
Bài toán 7.9. Cho $A, B, C, D$ là $n \times  n$ thực hoặc phức các ma trận.
$(1)$ Chứng minh rằng nếu $A$ là khả nghịch và nếu $AC = CA$, thì
$$\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} = \det(AD -CB).$$
$(2)$ Chứng minh rằng nếu $H$ là $n \times  n$ Ma trận Hadamard (Hadamard matrix) $(n \ge 2)$, thì | det(H)| $= n^{n/2}$.
$(3)$ Chứng minh rằng nếu $H$ là $n \times  n$ Ma trận Hadamard (Hadamard matrix) $(n \ge 2)$, thì
$$\det \begin{pmatrix} H & H \\ H & -H \end{pmatrix} = (2n)^{n}.$$
Bài toán 7.10. Tính tích của sau đây các định thức
$$a-b-c-dx-y-z-t$$
$$ba-dcyx-tz$$
$$cda-bztx-y$$
$$d-cbat-zyx$$
Để chứng minh sau đây đồng nhất thức (do Euler): $(a^{2} + b^{2} + c^{2} + d^{2})(x^{2} + y^{2} + z^{2} + t^{2}) =$ (ax $+$ bởi $+$ cz $+ dt)^{2} +$ (ay - bx $+$ ct - $dz)^{2}$
$$+ (az -bt -cx + dy)^{2}+ (at + bz -cy -dx)^{2}.$$

<!-- PAGE 255 -->
Bài toán 7.11. Cho $A$ là một ma trận cỡ $n \times  n$ với số nguyên các phần tử (entries). Chứng minh rằng $A^{-1}$ tồn tại và có số nguyên các phần tử (entries) khi và chỉ khi det() $= \pm 1$.
Bài toán 7.12. Cho $A$ là $n \times  n$ thực hoặc phức ma trận.
$(1)$ Chứng minh rằng nếu $A^{\top} = -A (A$ là phản đối xứng) và nếu $n$ là lẻ, thì det() $= 0$.
$(2)$ Chứng minh rằng
$$0abc$$
$$-a0de$$
$$= (af -be + dc)^{2}.$$
$$-b-d0f$$
$$-c-e-f0$$
Bài toán 7.13. Cauchy ma trận là ma trận của tạo thành
$$\begin{pmatrix} 1 & 1 & \cdots & 1 \\ \lambda_{1}  -\sigma_{1} & \lambda_{1}  -\sigma_{2} & \lambda_{1}  -\sigma_{n} \\ 1 & 1 & \cdots & 1 \\ \lambda_{2}  -\sigma_{1} & \lambda_{2}  -\sigma_{2} & \lambda_{2}  -\sigma_{n} \\ \vdots & \vdots & \vdots & \vdots \\ 1 & 1 & \cdots & 1 \end{pmatrix}$$
$$\lambda_{n}  -\sigma_{1} \lambda_{n}  -\sigma_{2} \lambda_{n}  -\sigma_{n}$$
Ở đâu $\lambda_{i}  \neq  \sigma_{j}$, với mọi $i, j$, với $1 \le i, j \le n$. Chứng minh rằng định thức (determinant) $C_{n}$ của Cauchy ma trận như ở trên được cho bởi
$$C_{n} = \frac{(\lambda_{i} \lambda_{j} )(\sigma_{j} \sigma_{i} )}{(\lambda_{i}  -\sigma_{j} )} \prod_{i}  n \prod_{ni=1j}  i- - -.$$
$$\prod^{=2}  \prod_{j}^{=11}  n=1$$
Bài toán 7.14. Cho $(\alpha_{1} , \dots  , \alpha_{m+1}$) là dãy của đôi một phân biệt các vô hướng trong $\mathbb{R}$ và cho $(\beta_{1} , \dots  , \beta_{m+1}$) là bất kỳ dãy của các vô hướng trong $\mathbb{R}$, không nhất thiết phân biệt.
$(1)$ Chứng minh rằng tồn tại duy nhất một đa thức $P$ của bậc nhiều nhất $m$ sao cho
$$P(\alpha_{i} ) = \beta_{i} ,1 \le i \le m + 1.$$
Hint. Remember Vandermonde!
$(2)$ Cho $L_{i}(X)$ là đa thức của bậc $m$ cho trước bởi
$$(X -\alpha_{1} ) \cdots  (X -\alpha_{i-1} )(X -\alpha_{i+1} ) \cdots  (X -\alpha_{m+1} )$$
$$L_{i}(X) =,1 \le i \le m + 1.$$
$$(\alpha_{i}  -\alpha_{1} ) \cdots  (\alpha_{i}  -\alpha_{i-1} )(\alpha_{i}  -\alpha_{i+1} ) \cdots  (\alpha_{i}  -\alpha_{m+1} )$$
Các đa thức $L_{i}(X)$ là đã biết như Lagrange đa thức interpolants. Chứng minh rằng
$$L_{i}(\alpha_{j} ) = \delta_{i j} 1 \le i, j \le m + 1.$$

<!-- PAGE 256 -->
Chứng minh rằng
$$P(X) = \beta_{1} L_{1}(X) + \cdots  + \beta_{m+1} L_{m+1}(X)$$
Là duy nhất đa thức của bậc nhiều nhất $m$ sao cho
$$P(\alpha_{i} ) = \beta_{i} ,1 \le i \le m + 1.$$
$(3)$ Chứng minh rằng $L_{1}(X), \dots  , L_{m+1}(X)$ là độc lập tuyến tính (linearly independent), và rằng chúng tạo thành cơ sở (basis) của tất cả các đa thức của bậc nhiều nhất $m$. Cách mà là $1$ (hằng số đa thức $1)$ được biểu diễn trên cơ sở (basis) $(L_{1}(X), \dots  , L_{m+1}(X))$? Cho biểu thức của mọi đa thức P(X) của bậc nhiều nhất $m$ trên cơ sở (basis) $(L_{1}(X), \dots  , L_{m+1}(X))$.
$(4)$ Chứng minh rằng đối ngẫu (dual) cơ sở (basis) $(L_{1}^{*}, \dots  , L_{m+1}^{*})$ của cơ sở (basis) $(L_{1}(X), \dots  , L_{m+1}(X))$ bao gồm của các dạng tuyến tính $L_{i}^{*}$ cho trước bởi
$$L_{i}^{*} (P) = P(\alpha_{i} ),$$
Với mọi đa thức $P$ của bậc nhiều nhất $m$; điều này là đơn giản việc tính giá trị tại $\alpha_{i}$.
