# Điều kiện Các số của Các ma trận


<!-- PAGE 364 -->
Lưu ý rằng đẳng thức là một cách tổng quát không khả dĩ/có thể; xét ma trận
$$A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} ,$$
Cho mà $\rho (A) = 0 < \|A\|$, vì $A \neq  0$.

## 9.5 Điều kiện Các số của Các ma trận

Không may là, ở đó tồn tại các hệ phương trình tuyến tính Ax $= b$ có các nghiệm là không stable dưới nhỏ perturbations của hoặc $b$ hoặc $A$. Ví dụ, xét hệ
$$\begin{pmatrix} 10 & 7 & 8 & 7 \\ 7 & 5 & 6 & 5 \\ 8 & 6 & 10 & 9 \\ 7 & 5 & 9 & 10 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \\ x_{4} \end{pmatrix} = \begin{pmatrix} 32 \\ 23 \\ 33 \\ 31 \end{pmatrix} .$$
Độc giả nên kiểm tra rằng nó có nghiệm $x = (1, 1, 1, 1)$. Nếu ta perturb slightly vế phải như $b + \Delta b$, ở đâu
$$\Delta b = \begin{pmatrix} 0.1 \\ -0.1 \\ 0.1 \\ 0.1 \end{pmatrix} ,$$
$$-$$
Ta thu được mới hệ
$$\begin{pmatrix} 10 & 7 & 8 & 7 \\ 7 & 5 & 6 & 5 \\ 8 & 6 & 10 & 9 \\ 7 & 5 & 9 & 10 \end{pmatrix} \begin{pmatrix} x_{1} + \Delta x_{1} \\ x_{2} + \Delta x_{2} \\ x_{3} + \Delta x_{3} \\ x_{4} + \Delta x_{4} \end{pmatrix} = \begin{pmatrix} 32.1 \\ 22.9 \\ 33.1 \\ 30.9 \end{pmatrix} .$$
Mới nghiệm hóa ra là $x + \Delta x =$ (9.2, -12.6, 4.5, -1.1), ở đâu
$$\Delta x = (9.2, -12.6, 4.5, -1.1) -(1, 1, 1, 1) = (8.2, -13.6, 3.5, -2.1).$$
Thì tương đối sai số của dữ liệu theo one-norm,
$$\|\|_{1}$$
$$\frac{\Delta b}{\|b\|_{1}} = \frac{0.4}{119} = \frac{4}{1190} \approx \frac{1}{300} ,$$
Produces tương đối sai số trong input
$$\|\|_{1}$$
$$\frac{\Delta x}{\|x\|_{1}} = \frac{27.4}{4} \approx 7.$$
Do đó tương đối sai số của thứ tự $1/300$ trong dữ liệu produces tương đối sai số của thứ tự $7/1$ trong nghiệm, mà biểu diễn amplification của tương đối sai số của thứ tự $2100$.

<!-- PAGE 365 -->
Bây giờ cho chúng ta perturb ma trận slightly, thu được mới hệ
$$\begin{pmatrix} 10 & 7 & 8.1 & 7.2 \\ 7.08 & 5.04 & 6 & 5 \\ 8 & 5.98 & 9.98 & 9 \\ 6.99 & 4.99 & 9 & 9.98 \end{pmatrix} \begin{pmatrix} x_{1} + \Delta x_{1} \\ x_{2} + \Delta x_{2} \\ x_{3} + \Delta x_{3} \\ x_{4} + \Delta x_{4} \end{pmatrix} = \begin{pmatrix} 32 \\ 23 \\ 33 \\ 31 \end{pmatrix} .$$
Điều này time nghiệm là $x + \Delta x =$ (-81, $137$, -34, $22)$. Một lần nữa nhỏ thay đổi trong dữ liệu alters kết quả khá drastically. Vẫn chưa ban đầu hệ là đối xứng, có định thức (determinant) $1$, và có số nguyên các phần tử (entries). bài toán là rằng ma trận của hệ là một cách xấu được điều kiện, khái niệm rằng ta sẽ bây giờ giải thích. Cho trước ma trận khả nghịch (invertible matrix) $A$, thứ nhất giả sử rằng ta perturb $b$ đến $b+\Delta b$, và cho chúng ta analyze thay đổi giữa hai chính xác các nghiệm $x$ và $x + \Delta x$ của hai các hệ
$$Ax = b$$
$$A(x + \Delta x) = b + \Delta b.$$
Ta cũng giả sử rằng ta có một số chuẩn (norm) $\|\|$ và ta sử dụng chuẩn ma trận phụ thuộc (subordinate matrix norm) trên các ma trận. Từ
$$Ax = b$$
$$Ax + A\Delta x = b + \Delta b,$$
Ta thu được
$$\Delta x = A^{-1}\Delta b,$$
Và ta kết luận rằng
$$\|\Delta x\|\le

$A^{-1}$

$\|\Delta b\|$$$
$$\|b\|\le \|A\|\|x\|.$$
Hệ quả là, tương đối sai số trong kết quả $\|\Delta x\|/ \|x\|$ là bị chặn theo tương đối sai số $\|\Delta b\|/ \|b\|$ trong dữ liệu như sau:
$$\|\|\|\|$$
$$\frac{\Delta x}{\|x\|} \le \begin{pmatrix} \|A\| & A^{-1} \end{pmatrix} \frac{\Delta b}{\|b\|} .$$
Bây giờ ta giả sử rằng $A$ là perturbed đến $A+\Delta A$, và cho chúng ta analyze thay đổi giữa chính xác các nghiệm của hai các hệ
$$Ax = b$$
$$(A + \Delta A)(x + \Delta x) = b.$$
Phương trình thứ hai cho ta Ax $+ A\Delta x + \Delta$ (x $+ \Delta x) = b$, và bằng cách trừ phương trình thứ nhất ta thu được
$$\Delta x = -A^{-1}\Delta A(x + \Delta x).$$

<!-- PAGE 366 -->
Suy ra rằng
$$\|\Delta x\|\le

$A^{-1}$

$\|\Delta A\|\|x + \Delta x\|,$$$ mà có thể được được viết lại như
$$\|\|\|\|$$
$$\frac{\Delta x}{\|x + \Delta x\|} \le \begin{pmatrix} \|A\| & A^{-1} \end{pmatrix} \frac{\Delta A}{\|A\|} .$$
Nhận thấy rằng ở trên lập luận là hợp lệ chẵn/ngay cả nếu ma trận $A + \Delta A$ là suy biến, như dài như $x + \Delta x$ là nghiệm của thứ hai hệ. Hơn nữa, nếu $\|\Delta A\|$ là nhỏ đủ, nó là không unreasonable đến kỳ vọng rằng tỉ số $\|\Delta x\|/ \|x + \Delta x\|$ là close đến $\|\Delta x\|/ \|x\|$. Điều này sẽ được tạo nhiều hơn/thêm precise sau này. Trong tóm tắt, với mỗi của hai perturbations, ta xem rằng tương đối sai số trong kết quả là bị chặn bởi tương đối sai số trong dữ liệu, được nhân số $\|A\|\|A^{-1}\|$. Thực ra, điều này nhân tử hóa ra là tối ưu và điều này suggests sau đây định nghĩa:

> **Định nghĩa 9.11.** Với mọi chuẩn ma trận phụ thuộc (subordinate matrix norm) $\|\|$, với mọi ma trận khả nghịch (invertible matrix) $A$, số
$$cond(A) = \|A\|

$A^{-1}$$$ is called the condition number of $A$ relative to $\|\|$. The condition number cond(A) measures the sensitivity of the linear system Ax $= b$ to variations in the data $b$ and $A$; đặc trưng (feature) referred đến như điều kiện của hệ. Do đó, khi ta nói rằng rằng hệ phương trình tuyến tính là ill-conditioned, ta có nghĩa rằng số điều kiện (condition number) của ma trận của nó là lớn. Ta có thể sharpen trước đó giải tích/phân tích như sau:

> **Mệnh đề 9.14.** Cho $A$ là ma trận khả nghịch (invertible matrix) và cho $x$ và $x + \Delta x$ là các nghiệm của các hệ phương trình tuyến tính
$$Ax = b$$
$$A(x + \Delta x) = b + \Delta b.$$
Nếu $b \neq  0$, thì bất đẳng thức
$$\|\|\|\|$$
$$\frac{\Delta x}{\|x\|} \le cond(A) \frac{\Delta b}{\|b\|}$$
Nghiệm đúng và là tốt nhất khả dĩ/có thể. Điều này có nghĩa là cho cho trước ma trận $A$, ở đó tồn tại một số các vectơ $b \neq  0$ và $\Delta b \neq  0$ cho mà đẳng thức nghiệm đúng.

*Chứng minh.* Ta đã được chứng minh bất đẳng thức. Bây giờ, bởi vì $\|\|$ là chuẩn ma trận phụ thuộc (subordinate matrix norm), ở đó tồn tại một số các vectơ $x \neq  0$ và $\Delta b \neq  0$ cho mà
$$A^{-1}\Delta b

$=$

$A^{-1}$

$\|\Delta b\|and\|Ax\|= \|A\|\|x\|.$$$

<!-- PAGE 367 -->

> **Mệnh đề 9.15.** Cho $A$ là ma trận khả nghịch (invertible matrix) và cho $x$ và $x + \Delta x$ là các nghiệm của hai các hệ
$$Ax = b$$
$$(A + \Delta A)(x + \Delta x) = b.$$
Nếu $b \neq  0$, thì bất đẳng thức
$$\|\|\|\|$$
$$\frac{\Delta x}{\|x + \Delta x\|} \le cond(A) \frac{\Delta A}{\|A\|}$$
Nghiệm đúng và là tốt nhất khả dĩ/có thể. Điều này có nghĩa là cho trước ma trận $A$, ở đó tồn tại vectơ $b \neq  0$ và ma trận $\Delta A \neq  0$ cho mà đẳng thức nghiệm đúng. Hơn nữa, nếu $\|\Delta A\|$ là nhỏ đủ (chẳng hạn, nếu $\|\Delta A\| < 1/ \|A^{-1}\|)$, ta có
$$\|\|\|\|$$
$$\frac{\Delta x}{\|x\|} \le cond(A) \frac{\Delta A}{\|A\|} (1 + O(\|\Delta A\|));$$
Thực ra, ta có
$$\|\|\|\|$$
$$\frac{\Delta x}{\|x\|} \le cond(A) \frac{\Delta A}{\|A\|} \begin{pmatrix} 1 \\ 1 -\|A^{-1}\|\|\Delta A\| \end{pmatrix} .$$

*Chứng minh.* thứ nhất bất đẳng thức có đã đã được được chứng minh. để chỉ ra rằng đẳng thức có thể được đạt được, cho $w$ là bất kỳ vectơ sao cho $w \neq  0$ và
$$A^{-1}w

$=$

$A^{-1}$

$\|w\|,$$$ and let $\beta \neq 0$ là bất kỳ thực số. Bây giờ các vectơ
$$\Delta x = -\beta A^{-1}w$$
$$x + \Delta x = w$$
$$b = (A + \beta I)w$$
Và ma trận
$$\Delta A = \beta I$$
Sastisfy các phương trình
$$Ax = b$$
$$(A + \Delta A)(x + \Delta x) = b$$
$$\|\Delta x\|= |\beta |

$A^{-1}w$

$= \|\Delta A\|$

$A^{-1}$

$\|x + \Delta x\|.$$$ Finally we can pick $\beta$  so that $-\beta$  is not equal to any of the eigenvalues of $A$, so that $A + \Delta = + \beta$ I is invertible and $b$ là là khác không.

<!-- PAGE 368 -->
Nếu $\|\Delta A\| < 1/ \|A^{-1}\|$, thì
$$A^{-1}\Delta A

$\le$

$A^{-1}$

$\|\Delta A\|<$ 1,$$ so by Proposition 9.12, the matrix $I + ^{-1}\Delta $ là khả nghịch và
$$(I + A^{-1}\Delta A)^{-1}

$\le \frac{1}{1 -\|A^{-1}\Delta A\|} \le \frac{1}{1 -\|A^{-1}\|\|\Delta A\|}$.$$ Nhắc lại rằng ta được chứng minh trước đó rằng
$$\Delta x = -A^{-1}\Delta A(x + \Delta x),$$
Và bằng cách cộng $x$ đến cả hai các vế/cạnh và di chuyển vế phải đến vế trái cho ta
$$(I + A^{-1}\Delta A)(x + \Delta x) = x,$$
Và do đó
$$x + \Delta x = (I + A^{-1}\Delta A)^{-1}x,$$
Mà cho ta
$$\Delta x = ((I + A^{-1}\Delta A)^{-1}-I)x = (I + A^{-1}\Delta A)^{-1}(I -(I + A^{-1}\Delta A))x$$
$$= -(I + A^{-1}\Delta A)^{-1}A^{-1}(\Delta A)x.$$
Từ điều này và
$$(I + A^{-1}\Delta A)^{-1}

$\le \frac{1}{1 -\|A^{-1}\|\|\Delta A\|}$,$$ ta thu được
$$\|\|\|\|$$
$$\|\Delta x\|\le \frac{A^{-1}\Delta A}{1 -\|A^{-1}\|\|\Delta A\|} \|x\|,$$
Mà có thể được viết dưới dạng
$$\|\|\|\|$$
$$\frac{\Delta x}{\|x\|} \le cond(A) \frac{\Delta A}{\|A\|} \begin{pmatrix} 1 \\ 1 -\|A^{-1}\|\|\Delta A\| \end{pmatrix} ,$$
Mà là loại của bất đẳng thức rằng ta đã là seeking.
Nhận xét: Nếu $A$ và $b$ là perturbed simultaneously, sao cho ta thu được “perturbed” hệ
$$(A + \Delta A)(x + \Delta x) = b + \Delta b,$$
Nó có thể được được hiển thị rằng nếu $\|\Delta A\| < 1/ \|A^{-1}\|$ (và $b \neq  0)$, thì
$$\|\|$$
$$\frac{\Delta x}{\|x\|} \le \frac{cond(A)}{1 -\|A^{-1}\|\|\Delta A\|} \begin{pmatrix} \|\Delta A\| & \|\Delta b\| \\ + \\ \|A\| & \|b\| \end{pmatrix} ;$$

<!-- PAGE 369 -->
Xem Demmel $[48]$, Mục 2.2 và Horn và Johnson $[98]$, Mục 5.8. Ta bây giờ danh sách một số các tính chất của điều kiện các số và hình ra những gì cond() là trong trường hợp của spectral chuẩn (norm) (chuẩn ma trận (matrix norm) được cảm sinh bởi $\|\|_{2})$. Thứ nhất, ta cần đến giới thiệu rất quan trọng nhân tử hóa của các ma trận, phân rã giá trị kỳ dị (SVD), cho ngắn, SVD. Nó có thể được được hiển thị (xem Mục 22.2) rằng cho trước bất kỳ ma trận cỡ $n \times  n$ $A \in M_{n}(\mathbb{C})$, ở đó tồn tại hai các ma trận unita $U$ và $V$, và thực ma trận đường chéo (diagonal matrix) $\Sigma  = diag(\sigma_{1} , \dots  , \sigma_{n}$), với $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{n}  \ge 0$, sao cho
$$A = V \Sigma U^{*} .$$

> **Định nghĩa 9.12.** Cho trước phức $n \times  n$ ma trận $A$, bộ ba $(U, V, \Sigma$) sao cho $A = V \Sigma U^{*}$, ở đâu $U$ và $V$ là $n \times  n$ các ma trận unita và $\Sigma  = diag(\sigma_{1} , \dots  , \sigma_{n}$) là ma trận đường chéo (diagonal matrix) của thực các số $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{n}  \ge 0$, được gọi là một suy biến phân rã (cho ngắn SVD) của $A$. Nếu $A$ là thực ma trận, thì $U$ và $V$ là các ma trận trực giao không âm các số $\sigma_{1} , \dots  , \sigma_{n}$ được gọi là các giá trị kỳ dị (singular values) của $A$. nhân tử hóa $A = V \Sigma U^{*}$ suy ra rằng
$$A^{*}A = U\Sigma^{2} U^{*} andAA^{*}= V \Sigma^{2} V^{*} ,$$
Mà chỉ ra rằng $\sigma_{1}^{2} , \dots  , \sigma_{n}^{2}$ là các trị riêng (eigenvalues) của cả hai $A^{*}A$ và $AA^{*}$, rằng các cột của $U$ là tương ứng các vectơ riêng (eigenvectors) cho $A^{*}A$, và rằng các cột của $V$ là tương ứng các vectơ riêng (eigenvectors) cho $AA^{*}$. Vì $\sigma_{1}^{2}$ là lớn nhất trị riêng (eigenvalue) của $A^{*}A$ (và $AA^{*})$, lưu ý rằng $p\overline{\rho}\overline{(}\overline{A}^{*}\overline{A}\overline{) =} p\overline{\rho}\overline{(}\overline{AA}^{*}\overline{) =} \sigma_{1}$.

> **Hệ quả 9.16.** spectral chuẩn (norm) $\|A\|_{2}$ của ma trận $A$ bằng lớn nhất giá trị kỳ dị (singular value) của $A$. Tương đương, spectral chuẩn (norm) $\|A\|_{2}$ của ma trận $A$ bằng $\ell^{\infty}$ -chuẩn (norm) của vectơ của nó của các giá trị kỳ dị (singular values),
$$\|A\|_{2} = \max \sigma_{i}  = \|(\sigma_{1} , \dots  , \sigma_{n} )\|_{\infty}.$$
$$1\le i\le n$$
Vì Chuẩn Frobenius (Frobenius norm) của ma trận $A$ được định nghĩa bởi $\|A\|_{F} = p\overline{tr(}\overline{A}^{*}\overline{A}\overline{)}$ và vì
$$\mathrm{tr}(A^{*}A) = \sigma_{1}^{2}  + \cdots  + \sigma_{n}^{2}$$
Ở đâu $\sigma_{1}^{2} , \dots  , \sigma_{n}^{2}$ là các trị riêng (eigenvalues) của $A^{*}A$, ta xem rằng
$$\|A\|_{F} = (\sigma_{1}^{2}  + \cdots  + \sigma_{n}^{2} )^{1/2}= \|(\sigma_{1} , \dots  , \sigma_{n} )\|_{2} .$$

> **Hệ quả 9.17.** Chuẩn Frobenius (Frobenius norm) của ma trận được cho bởi $\ell^{2}$ -chuẩn (norm) của vectơ của nó của các giá trị kỳ dị (singular values); $\|A\|_{F} = \|(\sigma_{1} , \dots  , \sigma_{n} )\|_{2}$.

<!-- PAGE 370 -->
Trong trường hợp của ma trận chuẩn tắc (normal matrix), nếu $\lambda_{1} , \dots  , \lambda_{n}$ là (phức) các trị riêng (eigenvalues) của $A$, ta đã chỉ ra trong chứng minh của Mệnh đề 9.11 rằng các trị riêng (eigenvalues) của $A^{*}A = AA^{*}$ là $(|\lambda_{1} |^{2}, \dots  , |\lambda_{n} |^{2})$, do đó các giá trị kỳ dị (singular values) của $A$ là
$$\sigma_{i}  = |\lambda_{i} |,1 \le i \le n.$$

> **Mệnh đề 9.18.** Với mọi ma trận khả nghịch (invertible matrix) $A \in M_{n}(\mathbb{C})$, các tính chất sau đây đúng: $(1)$
$$cond(A) \ge 1,$$
$$cond(A) = cond(A^{-1})$$
$$cond(\alpha A) = cond(A)for all \alpha  \in \mathbb{C} -{0}.$$
$(2)$ Nếu $cond_{2}(A)$ ký hiệu số điều kiện (condition number) của $A$ đối với spectral chuẩn (norm), thì
$$cond_{2}(A) = \frac{\sigma_{1}}{\sigma_{n}} ,$$
Ở đâu $\sigma_{1}  \ge \cdots  \ge \sigma_{n}$ là các giá trị kỳ dị (singular values) của $A$.
$(3)$ Nếu ma trận $A$ là chuẩn tắc/bình thường, thì
$$||$$
$$cond_{2}(A) = \frac{\lambda_{1}}{|\lambda_{n} |} ,$$
Ở đâu $\lambda_{1} , \dots  , \lambda_{n}$ là các trị riêng (eigenvalues) của $A$ sorted sao cho $|\lambda_{1}$ | $\ge \cdots  \ge |\lambda_{n}$ |.
$(4)$ Nếu $A$ là unita hoặc ma trận trực giao (orthogonal matrix), thì
$$cond_{2}(A) = 1.$$
$(5)$ số điều kiện (condition number) $cond_{2}(A)$ là bất biến dưới unita các phép biến đổi, mà có nghĩa là
$$cond_{2}(A) = cond_{2}(UA) = cond_{2}(AV ),$$
Với mọi các ma trận unita $U$ và $V$.

*Chứng minh.* các tính chất trong $(1)$ là immediate các hệ quả của các tính chất của phụ thuộc các chuẩn ma trận. Đặc biệt, $AA^{-1} =$ I suy ra
$$1 = \|I\|\le \|A\|

$A^{-1}$

$=$ cond().$$
$(2)$ Ta đã chỉ ra trước đó rằng $\|A\|_{2}^{2} = \rho (A^{*}A)$, mà là square của môđun/độ lớn của lớn nhất trị riêng (eigenvalue) của $A^{*}A$. Vì ta chỉ đã thấy rằng các trị riêng (eigenvalues) của $A^{*}A$ là $\sigma_{1}^{2}  \ge \cdots  \ge \sigma_{n}^{2}$, ở đâu $\sigma_{1} , \dots  , \sigma_{n}$ là các giá trị kỳ dị (singular values) của $A$, ta có
$$\|A\|_{2} = \sigma_{1} .$$

<!-- PAGE 371 -->
Bây giờ nếu $A$ là khả nghịch, thì $\sigma_{1}  \ge \cdots  \ge \sigma_{n}  > 0$, và nó là dễ để chỉ ra rằng các trị riêng (eigenvalues) của $(A^{*}A)^{-1}$ là $\sigma_{n}^{-2} \ge \cdots  \ge \sigma_{1}^{-2}$, mà chỉ ra rằng
$$A_{2}^{-1}

$= \sigma_{n}^{-1}$,$$ và do đó
$$cond_{2}(A) = \frac{\sigma_{1}}{\sigma_{n}} .$$
$(3)$ Điều này suy ra từ sự kiện rằng cho ma trận chuẩn tắc (normal matrix) $A$, các giá trị kỳ dị (singular values) được cho bởi $\sigma_{i}  = |\lambda_{i}$ |, $1 \le i \le n$.
$$\frac{(4)If}{\rho (A^{*}A} A is a unitary matrix, then A^{*}A = \frac{AA^{*}=I}{\rho (AA^{*}} , so \rho (A^{*}A) = 1, and \|A\|_{2} =$$
$p$) $= 1$. Ta cũng có $\|A^{-1}\|_{2} = \|A^{*}\|_{2} = p$) $= 1$, và do đó cond() $= 1$.
$(5)$ Điều này suy ra ngay lập tức từ unita tính bất biến của spectral chuẩn (norm). Mệnh đề 9.18 $(4)$ chỉ ra rằng unita và trực giao các phép biến đổi là rất wellconditioned, và Phần $(5)$ chỉ ra rằng unita các phép biến đổi bảo toàn số điều kiện (condition number). Trong thứ tự để tính $cond_{2}(A)$, ta cần để tính đỉnh/trên và đáy/dưới các giá trị kỳ dị (singular values) của $A$, mà có thể là khó. bất đẳng thức
$$\sqrt$$
$$\|A\|_{2} \le \|A\|_{F} \le \overline{n} \|A\|_{2} ,$$
Có thể là hữu ích trong thu được xấp xỉ của $cond_{2}(A) = \|A\|_{2} \|A^{-1}\|_{2}$, nếu $A^{-1}$ có thể được được xác định.
Nhận xét: Có một thú vị hình học đặc trưng của $cond_{2}(A)$. Nếu $\theta (A)$ ký hiệu least góc giữa các vectơ Au và Av như $u$ và $v$ miền giá trị (range) trên tất cả các cặp của trực chuẩn các vectơ, thì nó có thể được được hiển thị rằng
$$cond_{2}(A) = cot(\theta (A)/2)).$$
Do đó nếu $A$ là gần như suy biến, thì ở đó sẽ là một số trực chuẩn cặp $u, v$ sao cho Au và Av là gần như song song; góc $\theta (A)$ sẽ là nhỏ và $cot(\theta (A)/2))$ sẽ là lớn. Cho nhiều hơn/thêm chi tiết, xem Horn và Johnson $[98]$ (Mục 5.8 và Mục 7.4). Nó nên được lưu ý rằng nói chung (nếu $A$ là không ma trận chuẩn tắc (normal matrix)) ma trận có thể có rất lớn số điều kiện (condition number) chẵn/ngay cả nếu tất cả các trị riêng (các trị riêng (eigenvalues)) của nó là đồng nhất! Ví dụ, nếu ta xét ma trận cỡ $n \times  n$
$$A = \begin{pmatrix} 1 & 2 & 0 & 0 & \dots & 0 & 0 \\ 0 & 1 & 2 & 0 & \dots & 0 & 0 \\ 0 & 0 & 1 & 2 & \dots & 0 & 0 \\ \vdots & \vdots & \ddots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & \dots & 0 & 1 & 2 & 0 \\ 0 & 0 & \dots & 0 & 0 & 1 & 2 \\ 0 & 0 & \dots & 0 & 0 & 0 & 1 \end{pmatrix} ,$$

<!-- PAGE 372 -->
Hóa ra là $cond_{2}(A) \ge 2^{n-1}$. cổ điển ví dụ của ma trận với rất lớn số điều kiện (condition number) là Hilbert ma trận $H^{(n)}$, ma trận cỡ $n \times  n$ với
$$H_{ij}^{(n)}= \begin{pmatrix} 1 \\ i + j -1 \end{pmatrix} .$$
Ví dụ, khi $n = 5$,
$$H^{(5)} = \begin{pmatrix} 1_{2}^{1} & 1 & 1 & 1 \\ \overline{3} & \overline{4} & \overline{5} \\ 1 & 1 & 1 & 1 & 1 \\ \overline{2} & \overline{3} & \overline{4} & \overline{5} & \overline{6} \\ 1 & 1 & 1 & 1 & 1 \\ \overline{3} & \overline{4} & \overline{5} & \overline{6} & \overline{7} \\ 1 & 1 & 1 & 1 & 1 \\ \overline{4} & \overline{5} & \overline{6} & \overline{7} & \overline{8} \\ 1 & 1 & 1 & 1 & 1 \end{pmatrix} .$$
$$\overline{5}\overline{6}\overline{7}\overline{8}\overline{9}$$
Nó có thể được được hiển thị rằng
$$cond_{2}(H^{(5)}) \approx 4.77 \times  10^{5}.$$
Hilbert đã giới thiệu các ma trận này trong $1894$ trong khi studying bài toán trong xấp xỉ lý thuyết. Hilbert ma trận $H^{(n)}$ là đối xứng xác định dương (SPD). closed-form công thức có thể được cho trước cho định thức (định thức (determinant)) của nó (nó là đặc biệt tạo thành của so-called Cauchy định thức (determinant)); xem
Bài toán 9.15. nghịch đảo của $H^{(n)}$ có thể cũng được tính một cách tường minh; xem Bài toán 9.15. Nó có thể được được hiển thị rằng
$$\sqrt\sqrt$$
$$cond_{2}(H^{(n)}) = O((1 +\overline{2)}^{4n}/\overline{n}).$$
Đi quay lại đến ma trận của chúng ta
$$A = \begin{pmatrix} 10 & 7 & 8 & 7 \\ 7 & 5 & 6 & 5 \\ 8 & 6 & 10 & 9 \\ 7 & 5 & 9 & 10 \end{pmatrix} ,$$
Mà là đối xứng xác định dương (SPD) ma trận, nó có thể được được hiển thị rằng các trị riêng (các trị riêng (eigenvalues)) của nó, mà trong trường hợp này là cũng của nó các giá trị kỳ dị (singular values) bởi vì $A$ là SPD, là
$$\lambda_{1}  \approx 30.2887 > \lambda_{2}  \approx 3.858 > \lambda_{3}  \approx 0.8431 > \lambda_{4}  \approx 0.01015,$$
Sao cho
$$cond_{2}(A) = \frac{\lambda_{1}}{\lambda_{4}} \approx 2984.$$
Độc giả nên kiểm tra rằng cho perturbation của vế phải $b$ được sử dụng trước đó, tương đối các sai số $\|\Delta x\|/\|x\|$ và $\|\Delta x\|/\|x\|$ thỏa mãn bất đẳng thức
$$\|\|\|\|$$
$$\frac{\Delta x}{\|x\|} \le cond(A) \frac{\Delta b}{\|b\|}$$
Và đến close đến đẳng thức.
