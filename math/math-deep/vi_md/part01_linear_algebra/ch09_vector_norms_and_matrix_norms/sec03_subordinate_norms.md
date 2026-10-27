# Phụ thuộc Các chuẩn


<!-- PAGE 354 -->
Và
$$\|A\|_{F}^{2} = \mathrm{tr}(A^{*}A) = \mathrm{tr}(A^{*}U^{*}UA) = \|UA\|_{F}^{2} .$$
Đồng nhất thức
$$\|A\|_{F} = \|UAV \|_{F}$$
Suy ra từ trước đó hai.
$(3)$ Nó được hiển thị trong Mục 15.1 rằng vết (trace) của ma trận bằng tổng của các trị riêng (các trị riêng (eigenvalues)) của nó. Hơn nữa, $A^{*}A$ là đối xứng nửa xác định dương (positive semidefinite) (mà có nghĩa là các trị riêng (các trị riêng (eigenvalues)) của nó là không âm), do đó $\rho (A^{*}A)$ là lớn nhất trị riêng (eigenvalue) của $A^{*}A$ và
$$\rho (A^{*}A) \le \mathrm{tr}(A^{*}A) \le n\rho (A^{*}A),$$
Mà cho ta $(3)$ bằng cách lấy square các nghiệm.
Nhận xét: Chuẩn Frobenius (Frobenius norm) là cũng đã biết như Hilbert-Schmidt chuẩn (norm) hoặc Schur chuẩn (norm). Do đó nhiều nổi tiếng names liên kết với như vậy đơn giản thing!

## 9.3 Phụ thuộc Các chuẩn

Ta bây giờ cho một cái khác phương pháp cho thu được các chuẩn ma trận bằng cách sử dụng phụ thuộc các chuẩn. Thứ nhất ta cần mệnh đề rằng chỉ ra rằng trong hữu hạn chiều không gian, ánh xạ tuyến tính (linear map) được cảm sinh bởi ma trận là bị chặn, và do đó liên tục.
$$\mathbb{C}^{n}  \mathbb{R}^{n}\mathbb{C}$$

> **Mệnh đề 9.9.** Với mọi chuẩn (norm) $\|\|$ trên (hoặc), với mọi ma trận $A \in M_{n}($) (hoặc $A \in M_{n}(\mathbb{R}))$, có một thực hằng số $C_{A} \ge 0$, sao cho
$$\|Au\|\le C_{A} \|u\|,$$
$$\mathbb{C}^{n} \mathbb{R}^{n}$$
Với mọi vectơ $u \in$ (hoặc $u \in$ nếu $A$ là thực).
$$\mathbb{C}^{n}  \mathbb{R}^{n}$$

*Chứng minh.* Với mọi cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của (hoặc), với mọi vectơ $u = u_{1}e_{1} + \cdots  + u_{n}e_{n}$, ta có
$$\|Au\|= \|u_{1}A(e_{1}) + \cdots  + u_{n}A(e_{n})\|$$
$$\le |u_{1}| \|A(e_{1})\|+ \cdots  + |u_{n}| \|A(e_{n})\|$$
$$\le C_{1}(|u_{1}| + \cdots  + |u_{n}|) = C_{1} \|u\|_{1} ,$$
Ở đâu $C_{1} = max_{1\le i\le n} \|A(e_{i})\|$. Theo Định lý 9.6, các chuẩn $\|\|$ và $\|\|_{1}$ là tương đương, do đó tồn tại một hằng số $C_{2} > 0$ sao cho $\|u\|_{1} \le C_{2} \|u\|$ với mọi $u$, mà suy ra rằng
$$\|Au\|\le C_{A} \|u\|,$$
Ở đâu $C_{A} = C_{1}C_{2}$.

<!-- PAGE 355 -->
Mệnh đề 9.9 nói rằng rằng mọi ánh xạ tuyến tính (linear map) trên hữu hạn chiều không gian là bị chặn. Điều này suy ra rằng mọi ánh xạ tuyến tính (linear map) trên hữu hạn chiều không gian là liên tục. Thực sự, nó là không khó để chỉ ra rằng ánh xạ tuyến tính (linear map) trên không gian vectơ định chuẩn (normed vector space) $E$ là bị chặn khi và chỉ khi nó là liên tục, regardless của số chiều của $E$. Mệnh đề 9.9 suy ra rằng với mọi ma trận $A \in M_{n}(\mathbb{C})$ (hoặc $A \in M_{n}(\mathbb{R}))$,
$$\|\|$$
$$\sup\in \mathbb{C} n \frac{Ax}{\|x\|} \le C_{A}.$$
$$x$$
$$x\neq 0$$
Vì $\|\lambda u\| = |\lambda$ | $\|u\|$, với mọi khác không vectơ $x$, ta có
$$\|\| \|\|\| \|\|\|$$
$$\frac{Ax}{\|x\|} = \frac{xA(x/x)}{\|x\|} = \|A(x/ \|x\|)\|,$$
Mà suy ra rằng
$$\|\|$$
$$\sup\in \mathbb{C} n \frac{Ax}{\|x\|} = \sup\in \mathbb{C} n\|Ax\|.$$
$$xx$$
$$x\neq 0\|x\|=1$$
Tương tự
$$\|\|$$
$$\sup\in \mathbb{R} n \frac{Ax}{\|x\|} = \sup\in \mathbb{R} n\|Ax\|.$$
$$xx$$
$$x\neq 0\|x\|=1$$
Ở trên considerations justify sau đây định nghĩa.

> **Định nghĩa 9.8.** Nếu $\|\|$ là bất kỳ chuẩn (norm) trên $\mathbb{C}^{n}$, ta định nghĩa hàm $\|\|_{op}$ trên $M_{n}(\mathbb{C})$ bởi
$$\|\|$$
$$\|A\|_{op} = \sup\in \mathbb{C} n \frac{Ax}{\|x\|} = \sup\in \mathbb{C} n\|Ax\|.$$
$$xx$$
$$x\neq 0\|x\|=1$$
Hàm $A \mapsto \|A\|_{op}$ được gọi là chuẩn ma trận phụ thuộc (subordinate matrix norm) hoặc chuẩn toán tử (operator norm) được cảm sinh bởi chuẩn (norm) $\|\|$. Một cái khác ký hiệu cho chuẩn toán tử (operator norm) của ma trận $A$ (đặc biệt, được sử dụng bởi Horn và Johnson $[98])$, là ||||||. Nó là dễ để kiểm tra rằng hàm $A \mapsto \|A\|_{op}$ là thật vậy chuẩn (norm), và theo Định nghĩa, nó thỏa mãn tính chất
$$\|Ax\|\le \|A\|_{op} \|x\|,for all x \in \mathbb{C}^{n}.$$
Chuẩn (norm) $\|\|_{op}$ trên $M_{n}(\mathbb{C})$ thỏa mãn ở trên tính chất được nói là phụ thuộc đến chuẩn vectơ (vector norm) $\|\|$ trên $\mathbb{C}^{n}$. Hệ quả là của ở trên bất đẳng thức, ta có
$$\|ABx\|\le \|A\|_{op} \|Bx\|\le \|A\|_{op} \|B\|_{op} \|x\|,$$

<!-- PAGE 356 -->
Với mọi $x \in \mathbb{C}^{n}$, mà suy ra rằng
$$\|AB\|_{op} \le \|A\|_{op} \|B\|_{op}for all A, B \in M_{n}(\mathbb{C}),$$
Chỉ ra rằng $A \mapsto \|A\|_{op}$ là chuẩn ma trận (matrix norm) (nó là submultiplicative). Nhận thấy rằng chuẩn toán tử (operator norm) cũng được định nghĩa bởi
$$\|A\|_{op} = \inf{\lambda  \in \mathbb{R} | \|Ax\|\le \lambda  \|x\|, for all x \in \mathbb{C}^{n}}.$$
Vì hàm $x \mapsto \|Ax\|$ là liên tục (bởi vì | $\|Ay\|-\|Ax\|| \le \|Ay$ - $Ax\|\le$
$$\mathbb{C}^{n}$$
$C_{A} \|x$ - $y\|)$ và unit mặt cầu $S^{n-1} = {x \in$ | $\|x\| = 1}$ là compắc, tồn tại một $\mathbb{C}^{n} x \in$ sao cho $\|x\| = 1$ và
$$\|Ax\|= \|A\|_{op} .$$
$$\mathbb{C}^{n}$$
Tương đương, tồn tại một $x \in$ sao cho $x \neq  0$ và
$$\|Ax\|= \|A\|_{op} \|x\|.$$
Hệ quả là ta có thể thay thế sup bởi max trong định nghĩa của $\|A\|_{op}$ (và inf bởi min), cụ thể là
$$\|A\|_{op} = \max\|Ax\|.$$
$$x\in \mathbb{C} n$$
$$\|x\|=1$$
Định nghĩa của chuẩn toán tử (operator norm) cũng suy ra rằng
$$\|I\|_{op} = 1.$$
Ở trên chỉ ra rằng Chuẩn Frobenius (Frobenius norm) là không chuẩn ma trận phụ thuộc (subordinate matrix norm) cho $n \ge 2$ (tại sao?). Nếu $\|\|$ là chuẩn vectơ (vector norm) $on\mathbb{C}^{n}$, chuẩn toán tử (operator norm) $\|\|_{op}$ rằng nó cảm sinh áp dụng đến các ma trận trong $M_{n}(\mathbb{C})$. Nếu ta là careful đến ký hiệu các vectơ và các ma trận sao cho không có confusion phát sinh, ví dụ, bằng cách sử dụng thấp hơn trường hợp letters cho các vectơ và trên trường hợp letters cho các ma trận, nó nên là rõ ràng rằng $\|A\|_{op}$ là chuẩn toán tử (operator norm) của ma trận $A$ và rằng $\|x\|$ là chuẩn vectơ (vector norm) của $x$. Hệ quả là, sau đây chung/phổ biến practice đến alleviate ký hiệu, ta sẽ bỏ chỉ số dưới “op” và đơn giản viết $\|A\|$ thay vì của $\|A\|_{op}$. khái niệm của phụ thuộc chuẩn (norm) có thể được slightly suy rộng/tổng quát hóa.

> **Định nghĩa 9.9.** Nếu $K =\mathbb{R}$ hoặc $K =\mathbb{C}$, với mọi chuẩn (norm) $\|\|$ trên $M_{m,n}(K)$, và với mọi hai các chuẩn $\|\|_{a}$ trên $K^{n}$ và $\|\|_{b}$ trên $K^{m}$, ta nói rằng chuẩn (norm) $\|\|$ là phụ thuộc đến các chuẩn $\|\|_{a}$ và $\|\|_{b}$ nếu
$$\|Ax\|_{b} \le \|A\|\|x\|_{a}for all A \in M_{m,n}(K) and all x \in K^{n}.$$

<!-- PAGE 357 -->
Nhận xét: Với mọi chuẩn (norm) $\|\|$ trên $\mathbb{C}^{n}$, ta có thể định nghĩa hàm $\|\|_{R}$ trên $M_{n}(\mathbb{R})$ bởi
$$\|\|$$
$$\|A\|_{R} = \sup\in \mathbb{R} n \frac{Ax}{\|x\|} = \sup\in \mathbb{R} n\|Ax\|.$$
$$xx$$
$$x\neq 0\|x\|=1$$
Hàm $A \mapsto \|A\|_{R}$ là chuẩn ma trận (matrix norm) trên $M_{n}(\mathbb{R})$, và
$$\|A\|_{R} \le \|A\|,$$
Với mọi thực các ma trận $A \in M_{n}(\mathbb{R})$. Tuy nhiên, nó là khả dĩ/có thể để xây dựng các chuẩn vectơ $\|\| on\mathbb{C}^{n}$ và thực các ma trận $A$ sao cho
$$\|A\|_{R} < \|A\|.$$
Trong thứ tự để tránh điều này loại của difficulties, ta định nghĩa phụ thuộc các chuẩn ma trận trên $M_{n}(\mathbb{C})$. Luckily, hóa ra là $\|A\|_{R} = \|A\|$ cho các chuẩn vectơ, $\|\|_{1} , \|\|_{2}$, và $\|\|_{\infty}$. Ta bây giờ chứng minh Mệnh đề 9.7 cho thực các chuẩn ma trận.

> **Mệnh đề 9.10.** Với mọi chuẩn ma trận (matrix norm) $\|\|$ trên $M_{n}(\mathbb{R})$ và với mọi square $n \times  n$ ma trận $A \in M_{n}(\mathbb{R})$, ta có
$$\rho (A) \le \|A\|.$$

*Chứng minh.* Ta suy ra chứng minh trong Denis Serre’s cuốn sách $[162]$. Nếu $A$ là thực ma trận, bài toán là rằng các vectơ riêng (eigenvectors) liên kết với trị riêng (eigenvalue) của cực đại môđun/độ lớn có thể là phức. Ta sử dụng mẹo/kỹ thuật based trên sự kiện rằng với mọi ma trận $A$ (thực hoặc phức),
$$\rho (A^{k}) = (\rho (A))^{k},$$
Mà là để lại như một bài tập (sử dụng Mệnh đề 15.7 mà chỉ ra rằng nếu $(\lambda_{1} , \dots  , \lambda_{n}$) là (không nhất thiết phân biệt) các trị riêng (eigenvalues) của $A$, thì $(\lambda_{1}^{k} , \dots  , \lambda_{n}^{k}$) là các trị riêng (eigenvalues) của $A^{k}$, cho $k \ge 1)$.
$$\mathbb{C}^{n}$$
Chọn bất kỳ phức chuẩn ma trận (matrix norm) $\|\|_{c}$ trên (ví dụ, Chuẩn Frobenius (Frobenius norm), hoặc bất kỳ chuẩn ma trận phụ thuộc (subordinate matrix norm) được cảm sinh bởi chuẩn (norm) $on\mathbb{C}^{n})$. thu hẹp của $\|\|_{c}$ đến thực các ma trận là thực chuẩn (norm) rằng ta cũng ký hiệu bởi $\|\|_{c}$. Bây giờ theo Định lý 9.6, vì $M_{n}(\mathbb{R})$ có hữu hạn số chiều $n^{2}$, tồn tại một hằng số $C > 0$ sao cho
$$\|B\|_{c} \le C \|B\|,for allB \in M_{n}(\mathbb{R}).$$
Hơn nữa, với mọi $k \ge 1$ và với mọi thực $n\times n$ ma trận $A$, theo Mệnh đề 9.7, $\rho (A^{k}) \le A_{c}^{k}$

, và bởi vì $\|\|$ là chuẩn ma trận (matrix norm),

$A^{k}$

$\le \|A\|^{k}$, do đó ta có
$$\le  ,$$
$$(\rho (A))^{k}= \rho (A^{k}) \le

$A_{c}^{k}$

$\le C$

$A^{k}$

$C \|A\|^{k}$$$ for all $k \ge 1$. Suy ra rằng
$$\rho (A) \le C^{1/k}\|A\|,for allk \ge 1.$$

<!-- PAGE 358 -->
Tuy nhiên bởi vì $C > 0$, ta có $lim_{k\mapsto \infty} C^{1/k} = 1$ (ta có $lim_{k\mapsto \infty k}^{1}$ log(C) $= 0)$. Vì vậy, ta kết luận rằng
$$\rho (A) \le \|A\|,$$
Như mong muốn. Ta bây giờ xác định một cách tường minh những gì là phụ thuộc các chuẩn ma trận liên kết với các chuẩn vectơ $\|\|_{1} , \|\|_{2}$, và $\|\|_{\infty}$.

> **Mệnh đề 9.11.** Với mọi ma trận vuông (square matrix) $A = (a_{ij}) \in M_{n}(\mathbb{C})$, ta có
$$\|A\|_{1} = \sup\in \mathbb{C} n\|Ax\|_{1} = maxj \sum_{i=1}^{n}  |a_{ij}|$$
$$x$$
$$\|x\|=1$$
$$1$$
$$\|A\|_{\infty}=\sup\in \mathbb{C} n\|Ax\|_{\infty}= maxi \sum_{j=1}^{n}  |a_{ij}|$$
$$x$$
$$\|x\|=1$$
$$\infty$$
$$\|A\|_{2} = \sup\|Ax\|_{2} =p\overline{\rho}\overline{(}\overline{A}^{*}\overline{A}\overline{) =} p\overline{\rho}\overline{(}\overline{AA}^{*}\overline{)}.$$
$$x\in \mathbb{C} n$$
$$\|x\|=1$$
$$2$$
Lưu ý rằng $\|A\|_{1}$ là cực đại của $\ell^{1}$ -các chuẩn của các cột của $A$ và $\|A\|_{\infty}$ là cực đại của $\ell^{1}$ -các chuẩn của các hàng của $A$. Hơn nữa, $\|A^{*}\|_{2} = \|A\|_{2}$, chuẩn (norm) $\|\|_{2}$ là unitarily bất biến, mà có nghĩa là
$$\|A\|_{2} = \|UAV \|_{2}$$
Với mọi các ma trận unita $U, V$, và nếu $A$ là ma trận chuẩn tắc (normal matrix), thì $\|A\|_{2} = \rho (A)$.

*Chứng minh.* Với mọi vectơ $u$, ta có
$$\|Au\|_{1} = \sum_{i}  \sum_{j}  a_{ij}u_{j} \le \sum_{j}  |u_{j}| \sum_{i}  |a_{ij}| \le \begin{pmatrix} \max & |a_{ij}| \\ j \end{pmatrix} \sum_{i}  \|u\|_{1} ,$$
Mà suy ra rằng
$$\|A\|_{1} \le maxj \sum_{i=1}^{n}  |a_{ij}|.$$
Nó vẫn còn để chỉ ra rằng đẳng thức có thể được đạt được. Cho điều này cho $j_{0}$ là một số chỉ số sao cho
$$maxj \sum_{i}  |a_{ij}| = \sum_{i}  |a_{ij0}|,$$
Và cho $u_{i} = 0$ với mọi $i \neq  j_{0}$ và $u_{j0} = 1$. Trong đồng dạng cách, ta có
$$\|Au\|_{\infty}= maxi \sum_{j}  a_{ij}u_{j} \le \begin{pmatrix} \max & |a_{ij}| \\ i \end{pmatrix} \sum_{j}  \|u\|_{\infty},$$

<!-- PAGE 359 -->
Mà suy ra rằng
$$\|A\|_{\infty}\le maxi \sum_{j=1}^{n}  |a_{ij}|.$$
Đến đạt được đẳng thức, cho $i_{0}$ là một số chỉ số sao cho
$$maxi \sum_{j}  |a_{ij}| = \sum_{j}  |a_{i0j}|.$$
Độc giả nên kiểm tra rằng vectơ cho trước bởi
$$(\overline{a} ij$$
$$\overline{0} if a_{i0j} \neq  0$$
$$u_{j} =\overline{|}\overline{a}\overline{i}\overline{j}\overline{|}$$
$$1^{0}if a_{i0j} = 0$$
Hoạt động. Ta có
$$\|A\|_{2}^{2} = \sup\|Ax\|_{2}^{2} = supx^{*}A^{*}Ax.$$
$$x\in \mathbb{C} nx\in \mathbb{C} n$$
$$x*x=1x*x=1$$
Vì ma trận $A^{*}A$ là đối xứng, nó có thực các trị riêng (eigenvalues) và nó có thể được được chéo hóa đối với ma trận unita (unitary matrix). Các phần tử này các sự kiện có thể được được sử dụng để chứng minh rằng hàm $x \mapsto x^{*}A^{*}Ax$ có cực đại trên mặt cầu $x^{*}x = 1$ bằng lớn nhất trị riêng (eigenvalue) của $A^{*}A$, cụ thể là, $\rho (A^{*}A)$. Ta postpone chứng minh cho đến khi ta thảo luận optimizing toàn phương các hàm. Vì vậy,
$$\|A\|_{2} =p\overline{\rho}\overline{(}\overline{A}^{*}\overline{A}\overline{)}.$$
Cho sử dụng bây giờ chứng minh rằng $\rho (A^{*}A) = \rho (AA^{*})$. Thứ nhất giả sử rằng $\rho (A^{*}A) > 0$. Trong trường hợp này, tồn tại một vectơ riêng (eigenvector) $u (\neq  0)$ sao cho
$$A^{*}Au = \rho (A^{*}A)u,$$
Và vì $\rho (A^{*}A) > 0$, ta phải có Au $\neq  0$. Vì Au $\neq  0$,
$$AA^{*}(Au) = A(A^{*}Au) = \rho (A^{*}A)Au$$
Mà có nghĩa là $\rho (A^{*}A)$ là trị riêng (eigenvalue) của $AA^{*}$, và do đó
$$\rho (A^{*}A) \le \rho (AA^{*}).$$
Bởi vì $(A^{*})^{*} = A$, bằng cách thay thế $A$ bởi $A^{*}$, ta thu được
$$\rho (AA^{*}) \le \rho (A^{*}A),$$
Và do đó $\rho (A^{*}A) = \rho (AA^{*})$.

<!-- PAGE 360 -->
Nếu $\rho (A^{*}A) = 0$, thì ta phải có $\rho (AA^{*}) = 0$, vì ngược lại bởi trước đó lập luận ta sẽ có $\rho (A^{*}A) = \rho (AA^{*}) > 0$. Do đó, trong tất cả trường hợp
$$\|A\|_{2}^{2} = \rho (A^{*}A) = \rho (AA^{*}) = \|A^{*}\|_{2}^{2} .$$
Với mọi các ma trận unita $U$ và $V$, nó là dễ bài tập để chứng minh rằng $V^{*} A^{*}AV$ và $A^{*}A$ có cùng các trị riêng (eigenvalues), do đó
$$\|A\|_{2}^{2} = \rho (A^{*}A) = \rho (V^{*} A^{*}AV ) = \|AV \|_{2}^{2} ,$$
Và cũng
$$\|A\|_{2}^{2} = \rho (A^{*}A) = \rho (A^{*}U^{*}UA) = \|UA\|_{2}^{2} .$$
Cuối cùng, nếu $A$ là ma trận chuẩn tắc (normal matrix) $(AA^{*} = A^{*}A)$, nó có thể được được hiển thị rằng tồn tại một ma trận unita (unitary matrix) $U$ sao cho
$$A = UDU^{*} ,$$
Ở đâu $D = diag(\lambda_{1} , \dots  , \lambda_{n}$) là ma trận đường chéo (diagonal matrix) bao gồm của các trị riêng (eigenvalues) của $A$, và do đó
$$A^{*}A = (UDU^{*} )^{*}UDU^{*} = UD^{*}U^{*} UDU^{*} = UD^{*}DU^{*} .$$
Tuy nhiên, $D^{*}D = diag(|\lambda_{1} |^{2}, \dots  , |\lambda_{n} |^{2})$, mà chứng tỏ rằng các trị riêng (eigenvalues) của $A^{*}A = AA^{*}$ là $(|\lambda_{1} |^{2}, \dots  , |\lambda_{n} |^{2})$, và do đó,
$$\rho (A^{*}A) = \rho (D^{*}D) = \max|\lambda_{i} |^{2}= (\rho (A))^{2},$$
$$i$$
Sao cho $\|A\|_{2} = \rho (A)$.

> **Định nghĩa 9.10.** Cho $A = (a_{ij}) \in M_{n}(\mathbb{C})$, chuẩn (norm) $\|A\|_{2}$ là thường được gọi là spectral chuẩn (norm). Nhận thấy rằng Tính chất $(3)$ của Mệnh đề 9.8 nói rằng rằng
$$\sqrt$$
$$\|A\|_{2} \le \|A\|_{F} \le \overline{n} \|A\|_{2} ,$$
Mà chỉ ra rằng Chuẩn Frobenius (Frobenius norm) là trên cận trên spectral chuẩn (norm). Chuẩn Frobenius (Frobenius norm) là nhiều dễ hơn để tính hơn spectral chuẩn (norm). độc giả sẽ kiểm tra rằng ở trên chứng minh vẫn nghiệm đúng nếu ma trận $A$ là thực (thay đổi unita đến trực giao), confirming sự kiện rằng $\|A\|_{R} = \|A\|$ cho các chuẩn vectơ $\|\|_{1} , \|\|_{2}$, và $\|\|_{\infty}$. Nó là cũng dễ để kiểm chứng rằng chứng minh đi qua cho rectangular $m\times n$ các ma trận, với cùng các công thức. Tương tự, Chuẩn Frobenius (Frobenius norm) cho trước bởi
$$1/2$$
$$\|A\|_{F} = \begin{pmatrix} |a_{ij}|^{2} \end{pmatrix} \sum_{i=1j}^{m}  \sum_{=1}^{n}  =p\overline{\mathrm{tr}(}\overline{A}^{*}\overline{A}\overline{) =} p\overline{\mathrm{tr}(}\overline{AA}^{*}\overline{)}$$
Là cũng chuẩn (norm) trên rectangular các ma trận. Cho các phần tử này các chuẩn, bất cứ khi nào AB làm cho nghĩa, ta có
$$\|AB\|\le \|A\|\|B\|.$$

<!-- PAGE 361 -->
$$Remark: It can be shown that for any two real numbers p, q \ge 1 such that \frac{1}{p} + \frac{1}{q} = 1, we$$
Có $\|A^{*}\|_{q} = \|A\|_{p} = sup{\mathfrak{R}(y^{*}Ax)$ | $\|x\|_{p} = 1, \|y\|_{q} = 1} = sup{|\langle$ Ax, $y\rangle$ | | $\|x\|_{p} = 1, \|y\|_{q} = 1}$, ở đâu $\|A^{*}\|_{q}$ và $\|A\|_{p}$ là toán tử các chuẩn.
Nhận xét: Cho $(E, \|\|)$ và $(F, \|\|)$ là hai các không gian vectơ định chuẩn (để đơn giản của ký hiệu, ta sử dụng cùng ký hiệu $\|\|$ cho các chuẩn trên $E$ và $F$; điều này nên không gây ra bất kỳ confusion). Nhắc lại rằng hàm $f$: $E \to F$ là liên tục nếu với mọi $a \in E$, với mọi $\epsilon  > 0$, tồn tại một $\eta  > 0$ sao cho với mọi $x \in E$,
$$if\|x -a\|\le \eta then\|f(x) -f(a)\|\le \epsilon .$$
Nó là không khó để chỉ ra rằng ánh xạ tuyến tính (linear map) $f$: $E \to F$ là liên tục khi và chỉ khi tồn tại một hằng số $C \ge 0$ sao cho
$$\|f(x)\|\le C \|x\|for all x \in E.$$
Nếu do đó, ta nói rằng $f$ là bị chặn (hoặc tuyến tính bị chặn toán tử). Ta cho $\mathcal{L}(E; F)$ ký hiệu tập hợp tất cả liên tục (tương đương, bị chặn) các ánh xạ tuyến tính (linear maps) từ $E$ đến $F$. Thì ta có thể định nghĩa chuẩn toán tử (operator norm) (hoặc phụ thuộc chuẩn (norm)) $\|\|$ trên $\mathcal{L}(E; F)$ như sau: với mọi $f \in$ L(E; $F)$,
$$\|\|$$
$$\|f\|= \sup\in \frac{f(x)}{\|x\|} = \sup\in \|f(x)\|,$$
$$xExE$$
$$x\neq 0\|x\|=1$$
Hoặc tương đương bởi
$$\|f\|= \inf{\lambda  \in \mathbb{R} | \|f(x)\|\le \lambda  \|x\|, for all x \in E}.$$
Ở đây bởi vì $E$ có thể là vô hạn chiều, sup có thể’t được thay thế bởi max và inf có thể’t được thay thế bởi min. Nó là không khó để chỉ ra rằng ánh xạ $f \mapsto \|f\|$ là chuẩn (norm) trên $\mathcal{L}(E; F)$ thỏa mãn tính chất
$$\|f(x)\|\le \|f\|\|x\|$$
Với mọi $x \in E$, và rằng nếu $f \in$ L(E; $F)$ và $g \in$ L(F; $G)$, thì
$$\|g \circ f\|\le \|g\|\|f\|.$$
Toán tử các chuẩn đóng quan trọng vai trò trong phiếm hàm giải tích/phân tích, especially khi các không gian $E$ và $F$ là đầy đủ.
