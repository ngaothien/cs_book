# Các bài tập


<!-- PAGE 382 -->
$\bullet$ Sự hội tụ của các dãy của các vectơ trong không gian vectơ định chuẩn (normed vector space). $\bullet$ Các dãy Cauchy, phức các không gian vectơ định chuẩn, Các không gian Banach. $\bullet$ Sự hội tụ của chuỗi. Tuyệt đối sự hội tụ. $\bullet$ ma trận hàm mũ. $\bullet$ Skew các ma trận đối xứng và các ma trận trực giao.

## 9.10 Các bài tập

Bài toán 9.1. Cho $A$ là sau đây ma trận:
$$A = \begin{pmatrix} \sqrt \\ 1\sqrt & 1/ & \overline{2} \\ 1/ & \overline{2} & 3/2 \end{pmatrix} .$$
Tính toán tử 2-chuẩn (norm) $\|A\|_{2}$ của $A$.
Bài toán 9.2. Chứng minh Mệnh đề 9.3, cụ thể là rằng sau đây các bất đẳng thức đúng với mọi $\mathbb{R}^{n} \mathbb{C}^{n} x \in$ (hoặc $x \in$):
$$\|x\|_{\infty}\le \|x\|_{1} \le n\|x\|_{\infty},$$
$$\sqrt$$
$$\|x\|_{\infty}\le \|x\|_{2} \le \overline{n}\|x\|_{\infty},$$
$$\sqrt$$
$$\|x\|_{2} \le \|x\|_{1} \le \overline{n}\|x\|_{2}.$$
Bài toán 9.3. Với mọi $p \ge 1$, chứng minh rằng với mọi $x \in \mathbb{R}^{n}$,
$$lim\|x\|_{p} = \|x\|_{\infty}.$$
$$p\mapsto \infty$$
Bài toán 9.4. Cho $A$ là một ma trận cỡ $n \times  n$ mà là chặt hàng một cách đường chéo trội, mà có nghĩa là
$$|a_{i i}| > \sum_{j\neq i}  |a_{i j}|,$$
Cho $i = 1, \dots  , n$, và cho
$$$$
$$\delta  = mini|a_{i i}| - \sum_{j\neq i}  |a_{i j}|.$$
Sự kiện rằng $A$ là chặt hàng một cách đường chéo trội là tương đương đến điều kiện $\delta  > 0$.
$(1)$ Với mọi khác không vectơ $v$, chứng minh rằng
$$\|Av\|_{\infty}\ge \|v\|_{\infty}\delta .$$
Sử dụng ở trên để chứng minh rằng $A$ là khả nghịch.

<!-- PAGE 383 -->
$(2)$ Chứng minh rằng
$$A_{\infty}^{-1}

$\le \delta^{-1}$.$$ Hint. Chứng minh rằng
$$\|\|_{\infty}\|\|_{\infty}$$
$$supv\neq 0 \frac{A^{-1}v}{\|v\|_{\infty}} = supw\neq 0 \frac{w}{\|Aw\|_{\infty}} .$$
Bài toán 9.5. Cho $A$ là bất kỳ khả nghịch phức $n \times  n$ ma trận.
$$\mathbb{C}^{n} \mathbb{C}^{n} \mathbb{R}$$
$(1)$ Với mọi chuẩn vectơ (vector norm) $\|\|$ trên, chứng minh rằng hàm $\|\|_{A}$: $\to$ cho trước bởi
$$\|x\|_{A} = \|Ax\|for allx \in \mathbb{C}^{n},$$
Là chuẩn vectơ (vector norm).
$(2)$ Chứng minh rằng chuẩn toán tử (operator norm) được cảm sinh bởi $\|\|_{A}$, cũng được ký hiệu bởi $\|\|_{A}$, được cho bởi
$$\|B\|_{A} =

$ABA^{-1}$

Với mọi $n \times  n$ matrixB,$$ where $\|ABA^{-1}\|$ uses the operator norm induced by $\|\|$.
$$\mathbb{C}^{n}$$
Bài toán 9.6. Cho ví dụ của chuẩn (norm) trên và của thực ma trận $A$ sao cho
$$\|A\|_{R} < \|A\|,$$
Ở đâu $\|-\|_{R}$ và $\|-\|$ là toán tử các chuẩn liên kết với chuẩn vectơ (vector norm) $\|-\|$. Hint. Điều này có thể đã được thực hiện cho $n = 2$.
Bài toán 9.7. Cho $\|\|$ là bất kỳ chuẩn toán tử (operator norm). Cho trước khả nghịch $n \times  n$ ma trận $A$, nếu $c = 1/(2 \|A^{-1}\|)$, thì với mọi $n \times  n$ ma trận $H$, nếu $\|H\|\le c$, thì $A + H$ là khả nghịch. Hơn nữa, chỉ ra rằng nếu $\|H\|\le c$, thì $\|(A + H)^{-1}\|\le 1/c$.
Bài toán 9.8. Cho $A$ là bất kỳ ma trận cỡ $m\times n$ và cho $\lambda  \in \mathbb{R}$ là bất kỳ dương thực số $\lambda  > 0$.
$(1)$ Chứng minh rằng $A^{\top}A + \lambda I_{n}$ và $AA^{\top} + \lambda I_{m}$ là khả nghịch.
$(2)$ Chứng minh rằng
$$A^{\top}(AA^{\top}+ \lambda I_{m})^{-1}= (A^{\top}A + \lambda I_{n})^{-1}A^{\top}.$$
Nhận xét: các biểu thức ở trên tương ứng với ma trận cho mà hàm
$$\Phi (x) = (Ax -b)^{\top}(Ax -b) + \lambda x^{\top}x$$
Đạt được cực tiểu. Nó chỉ ra lên trong máy học (learning) (hạt nhân (kernel) các phương pháp).
Bài toán 9.9. Cho $Z$ là $q \times  p$ thực ma trận. Chứng minh rằng nếu $I_{p}$ - $Z^{\top}Z$ là xác định dương (positive definite), thì ma trận cỡ $(p + q) \times  (p + q)$
$$S = \begin{pmatrix} I_{p} & Z^{\top} \\ Z & I_{q} \end{pmatrix}$$
Là đối xứng xác định dương (SPD).

<!-- PAGE 384 -->
Bài toán 9.10. Chứng minh rằng với mọi thực hoặc phức ma trận vuông (square matrix) $A$, ta có
$$\|A\|_{2}^{2} \le \|A\|_{1} \|A\|_{\infty},$$
Ở đâu ở trên các chuẩn là toán tử các chuẩn. Hint. Sử dụng Mệnh đề 9.11 (trong số khác things, nó chỉ ra rằng $\|A\|_{1} =$

$A_{\infty}^{\top}$

).
Bài toán 9.11. Chỉ ra rằng ánh xạ $A \mapsto \rho (A)$ (ở đâu $\rho (A)$ là bán kính phổ (spectral radius) của $A)$ là không chuẩn (norm) cũng không chuẩn ma trận (matrix norm). Đặc biệt, tìm hai ma trận cỡ $2 \times  2$ $A$ và $B$ sao cho
$$\rho (A + B) > \rho (A) + \rho (B) = 0and\rho (AB) > \rho (A)\rho (B) = 0.$$
Bài toán 9.12. Định nghĩa ánh xạ $A \mapsto$ M() (được định nghĩa trên $n\times n$ thực hoặc phức $n\times n$ các ma trận) bởi
$$M(A) = \max{|a_{ij}| | 1 \le i, j \le n}.$$
$(1)$ Chứng minh rằng
$$M(AB) \le nM(A)M(B)$$
Với mọi $n \times  n$ các ma trận $A$ và $B$.
$(2)$ Cho counter-example của bất đẳng thức
$$M(AB) \le M(A)M(B).$$
$(3)$ Chứng minh rằng ánh xạ $A \mapsto \|A\|_{M}$ cho trước bởi
$$\|A\|_{M} = nM(A) = n \max{|a_{ij}| | 1 \le i, j \le n}$$
Là chuẩn ma trận (matrix norm).
Bài toán 9.13. Cho $S$ là thực đối xứng xác định dương (SPD) ma trận.
$(1)$ Sử dụng Nhân tử hóa Cholesky (Cholesky factorization) để chứng minh rằng tồn tại một tam giác trên (upper-triangular) ma trận $C$, duy nhất nếu của nó đường chéo các phần tử là chặt dương, sao cho $S = C^{\top}C$.
$(2)$ Với mọi $x \in \mathbb{R}^{n}$, định nghĩa
$$\|x\|_{S} = (x^{\top}Sx)^{1/2}.$$
Chứng minh rằng
$$\|x\|_{S} = \|Cx\|_{2} ,$$
Và rằng ánh xạ $x \mapsto \|x\|_{S}$ là chuẩn (norm).
Bài toán 9.14. Cho $A$ là thực $2 \times  2$ ma trận
$$A = \begin{pmatrix} a_{1 1} & a_{1 2} \\ a_{2 1} & a_{2 2} \end{pmatrix} .$$

<!-- PAGE 385 -->
$(1)$ Chứng minh rằng squares của các giá trị kỳ dị (singular values) $\sigma_{1}  \ge \sigma_{2}$ của $A$ là các nghiệm của toàn phương phương trình
$$X^{2}-\mathrm{tr}(A^{\top}A)X + | \det(A)|^{2}= 0.$$
$(2)$ Nếu ta cho
$$\mu (A) = \frac{a_{1 1}^{2}+ a_{1 2}^{2}+ a_{2 1}^{2}+ a_{2 2}^{2}}{2|a_{1 1}a_{2 2} -a_{1 2}a_{2 1}|} ,$$
Chứng minh rằng
$$cond_{2}(A) = \frac{\sigma_{1}}{\sigma_{2}} = \mu (A) + (\mu (A)^{2}-1)^{1/2}.$$
$(3)$ Xét tập con $\mathcal{S}$ của $2 \times  2$ các ma trận khả nghịch có các phần tử (entries) $a_{i j}$ là các số nguyên sao cho $0 \le a_{ij} \le 100$. Chứng minh rằng các hàm $cond_{2}(A)$ và $\mu (A)$ đạt tới cực đại trên $set\mathcal{S}$ cho cùng các giá trị của $A$. Kiểm tra rằng cho ma trận
$$A_{m} = \begin{pmatrix} 100 & 99 \\ 99 & 98 \end{pmatrix}$$
Ta có
$$\mu (A_{m}) = 19, 603det(A_{m}) = -1$$
Và
$$cond_{2}(A_{m}) \approx 39, 206.$$
$(4)$ Chứng minh rằng với mọi $A \in S$, nếu | det()| $\ge 2$ thì $\mu (A) \le 10, 000$. Kết luận rằng cực đại của $\mu (A)$ trên $\mathcal{S}$ là đạt được cho các ma trận sao cho det() $= \pm 1$. Chứng minh rằng việc tìm các ma trận rằng cực đại hóa $\mu$ trên $\mathcal{S}$ là tương đương đến việc tìm một số các số nguyên $n_{1}, n_{2}, n_{3}, n_{4}$ sao cho
$$0 \le n_{4} \le n_{3} \le n_{2} \le n_{1} \le 100$$
$$+ 99_{2} + 99_{2} + 98_{2}$$
$$n_{1}^{2} + n_{2}^{2} + n_{3}^{2} + n_{4}^{2} \ge 100^{2}= 39, 206$$
$$|n_{1}n_{4} -n_{2}n_{3}| = 1.$$
Bạn có thể sử dụng mà không có chứng minh rằng sự kiện rằng chỉ nghiệm đến ở trên các ràng buộc là đa tập hợp (multiset)
$${100, 99, 99, 98}.$$
$(5)$ Suy ra từ phần $(4)$ rằng các ma trận trong $\mathcal{S}$ cho mà $\mu$ có cực đại giá trị là
$$A_{m} = \begin{pmatrix} 100 & 99 \\ 99 & 98 \end{pmatrix} \begin{pmatrix} 98 & 99 \\ 99 & 100 \end{pmatrix} \begin{pmatrix} 99 & 100 \\ 98 & 99 \end{pmatrix} \begin{pmatrix} 99 \\ 98 \\ 100 & 99 \end{pmatrix}$$
Và kiểm tra rằng $\mu$ có cùng giá trị cho các ma trận này. Kết luận rằng
$$\max cond_{2}(A) = cond_{2}(A_{m}).$$
$$A\in S$$

<!-- PAGE 386 -->
$(6)$ Giải hệ
$$\begin{pmatrix} 100 & 99 \\ 99 & 98 \\ by \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} = \begin{pmatrix} 199 \\ 197 \end{pmatrix} .$$
Perturb vế phải $b$
$$\Delta b = \begin{pmatrix} -0.0097 \\ 0.0106 \end{pmatrix}$$
Và giải mới hệ
$$A_{m}y = b + \Delta b$$
Ở đâu $y = (y_{1}, y_{2})$. Kiểm tra rằng
$$\Delta x = y -x = \begin{pmatrix} 2 \\ -2.0203 \end{pmatrix} .$$
Tính $\|x\|_{2}, \|\Delta x\|_{2}, \|b\|_{2}, \|\Delta b\|_{2}$, và estimate
$$c = \| \frac{\Delta x}{\|x\|_{2}} \|_{2} \begin{pmatrix} \|\Delta b \\ \|b\|_{2} \end{pmatrix} \|_{2}^{-1}.$$
Kiểm tra rằng
$$c \approx cond_{2}(A_{m}) \approx 39, 206.$$
Bài toán 9.15. Xét thực $2 \times  2$ ma trận với không vết (trace) của tạo thành
$$A = \begin{pmatrix} a & b \\ c & -a \end{pmatrix} .$$
$(1)$ Chứng minh rằng
$$A^{2}= (a^{2}+ bc)I_{2} = -\det(A)I_{2}.$$
Nếu $a^{2} +$ bc $= 0$, chứng minh rằng
$$e^{A}= I_{2} + A.$$
$(2)$ Nếu $a^{2} +$ bc $< 0$, cho $\omega  > 0$ là sao cho $\omega^{2} = (a^{2} +$ bc). Chứng minh rằng
$$e^{A} = \cos \omega  I_{2} + \frac{-\sin \omega}{\omega} A.$$
$(3)$ Nếu $a^{2} +$ bc $> 0$, cho $\omega  > 0$ là sao cho $\omega^{2} = a^{2} +$ bc. Chứng minh rằng
$$e^{A} = cosh \omega  I_{2} + \frac{sinh \omega}{\omega} A.$$
$(3)$ Chứng minh rằng trong tất cả các trường hợp
$$\det \begin{pmatrix} e^{A} \end{pmatrix} = 1andtr(A) \ge -2.$$
$(4)$ Chứng minh rằng ở đó tồn tại một số thực $2 \times  2$ ma trận $B$ với det(B) $= 1$ sao cho không có thực $2 \times  2$ ma trận $A$ với không vết (trace) sao cho $e^{A} = B$.

<!-- PAGE 387 -->
Bài toán 9.16. Nhắc lại rằng Hilbert ma trận được cho bởi
$$H_{ij}^{(n)}= \begin{pmatrix} 1 \\ i + j -1 \end{pmatrix} .$$
$(1)$ Chứng minh rằng
$$\cdots  -$$
$$\det(H^{(n)}) = \frac{(1!2! (n1)!)^{4}}{1!2! \cdots  (2n -1)!} ,$$
Do đó reciprocal của số nguyên. Hint. Sử dụng Bài toán 7.13.
$(2)$ Amazingly, các phần tử (entries) của nghịch đảo của $H^{(n)}$ là các số nguyên. Chứng minh rằng $(H^{(n)})^{-1} = (\alpha_{ij}$), với
$$2^{2}$$
$$\alpha_{ij}  = (-1)^{i+j}(i + j -1) \begin{pmatrix} n + i -1 \\ n -j \end{pmatrix} \begin{pmatrix} n + j -1 \\ n -i \end{pmatrix} \begin{pmatrix} i + j - \\ i -1 \end{pmatrix} .$$

<!-- PAGE 388 -->
