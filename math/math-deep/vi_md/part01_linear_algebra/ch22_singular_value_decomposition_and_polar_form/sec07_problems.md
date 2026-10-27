# Các bài tập


<!-- PAGE 764 -->

## 22.6 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ Với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$ trên Không gian Euclid (Euclidean space) $E$, các ánh xạ $f^{*} \circ f$ và $f \circ f^{*}$ là tự liên hợp (self-adjoint) và nửa xác định dương (positive semidefinite). $\bullet$ các giá trị kỳ dị (singular values) của ánh xạ tuyến tính (linear map). $\bullet$ Nửa xác định dương (positive semidefinite) và xác định dương (positive definite) tự liên hợp (self-adjoint) các ánh xạ. $\bullet$ Relationships giữa Im $f$, Ker $f$, Im $f^{*}$, và Ker $f^{*}$. $\bullet$ phân rã giá trị kỳ dị (SVD) định lý cho các ma trận vuông (Định lý 22.5). $\bullet$ SVD của ma trận. $\bullet$ phân rã cực (polar decomposition) của ma trận. $\bullet$ Weyl các bất đẳng thức. $\bullet$ phân rã giá trị kỳ dị (SVD) định lý cho $m \times  n$ các ma trận (Định lý 22.7). $\bullet$ Ky Fan k-norms, Ky Fan p-k-norms, Schatten p-norms.

## 22.7 Các bài tập

Bài toán 22.1. $(1)$ Cho $A$ là thực $n\times n$ ma trận và xét $(2n)\times$ (2n) thực ma trận đối xứng (symmetric matrix)
$$S = \begin{pmatrix} 0 & A \\ A^{\top} & 0 \end{pmatrix} .$$
Giả sử rằng $A$ có hạng (rank) $r$. Nếu $A = V \Sigma U^{\top}$ là SVD cho $A$, với $\Sigma  = diag(\sigma_{1} , \dots  , \sigma_{n}$) và $\sigma_{1}  \ge \cdots  \ge \sigma_{r}  > 0$, ký hiệu các cột của $U$ bởi $u_{k}$ và các cột của $V$ bởi $v_{k}$, chứng minh rằng
$$\sigma_{k}  is an eigenvalue of S with corresponding eigenvector \begin{pmatrix} v_{k} \\ u_{k} \end{pmatrix} for k = 1, \dots  , n, and that -\sigma_{k}$$
$$is an eigenvalue of S with corresponding eigenvector \begin{pmatrix} v_{k} \\ -u_{k} \end{pmatrix} for k = 1, \dots  , n.$$
Hint. Ta có $Au_{k} = \sigma_{k} v_{k}$ cho $k = 1, \dots  , n$. Chỉ ra rằng $A^{\top}v_{k} = \sigma_{k} u_{k}$ cho $k = 1, \dots  , n$.
$(2)$ Chứng minh rằng 2n các vectơ riêng (eigenvectors) của $S$ trong $(1)$ là đôi một trực giao. Kiểm tra rằng nếu $A$ có hạng (rank) $r$, thì $S$ có hạng (rank) 2r.
$(3)$ Bây giờ giả sử rằng $A$ là thực $m \times  n$ ma trận và xét $(m + n) \times  (m + n)$ thực ma trận đối xứng (symmetric matrix)
$$S = \begin{pmatrix} 0 & A \\ A^{\top} & 0 \end{pmatrix} .$$

<!-- PAGE 765 -->
Giả sử rằng $A$ có hạng (rank) $r$. Nếu $A = V \Sigma U^{\top}$ là SVD cho $A$, chứng minh rằng $\sigma_{k}$ là trị riêng (eigenvalue)
$$of S with corresponding eigenvector \begin{pmatrix} v_{k} \\ u_{k} \end{pmatrix} for k = 1, \dots  , r, and that -\sigma_{k}  is an eigenvalue of$$
$$S with corresponding eigenvector \begin{pmatrix} v_{k} \\ -u_{k} \end{pmatrix} for k = 1, \dots  , r.$$
Tìm còn lại $m + n$ - 2r các vectơ riêng (eigenvectors) của $S$ liên kết với trị riêng (eigenvalue) $0$.
$(4)$ Chứng minh rằng các phần tử này $m + n$ các vectơ riêng (eigenvectors) của $S$ là đôi một trực giao.
Bài toán 22.2. Cho $A$ là thực $m \times  n$ ma trận của hạng (rank) $r$.
$(1)$ Xét $(m + n) \times  (m + n)$ thực ma trận đối xứng (symmetric matrix)
$$S = \begin{pmatrix} 0 & A \\ A^{\top} & 0 \end{pmatrix}$$
Và chứng minh rằng
$$\begin{pmatrix} I_{m} & z^{-1}A \\ 0 & I_{n} \end{pmatrix} \begin{pmatrix} zI \\ -A \\ -^{m}A^{\top} & zI_{n} \end{pmatrix} = \begin{pmatrix} zI_{m} -z^{-1}AA^{\top} & 0 \\ -A^{\top} & zI_{n} \end{pmatrix} .(*)$$
Sử dụng Phương trình (*) để chứng minh rằng nếu nếu $n \ge m$, thì
$$\det(zI_{m+n} -S) = z^{n-m}\det(z^{2}I_{m} -AA^{\top}).$$
Hoán vị hai các ma trận trên lefthand vế/cạnh của Phương trình (*) để thu được một cái khác phương trình và sử dụng phương trình này để chứng minh rằng nếu $m \ge n$, thì
$$\det(zI_{m+n} -S) = z^{m-n}\det(z^{2}I_{n} -A^{\top}A).$$
$(2)$ Chứng minh rằng các trị riêng (eigenvalues) của $S$ là $\pm \sigma_{1} , \dots  , \pm \sigma_{r}$, với $m + n$ - 2r additional các không điểm.
Bài toán 22.3. Cho $B$ là thực bidiagonal ma trận của tạo thành
$$B = \begin{pmatrix} a_{1} & b_{1} & 0 & \cdots & 0 \\ 0 & a_{2} & b_{2} & \ddots & 0 \\ \vdots & \ddots & \ddots & \ddots & \vdots \\ 0 & \cdots & 0 & a_{n-1} & b_{n-1} \\ 0 & 0 & 0 & a_{n} \end{pmatrix} .$$
$$\cdots$$
Cho $A$ là (2n) $\times$ (2n) ma trận đối xứng (symmetric matrix)
$$A = \begin{pmatrix} 0 \\ B^{\top} \\ B & 0 \end{pmatrix} ,$$
Và cho $P$ là hoán vị ma trận cho trước bởi $P = [e_{1}, e_{n+1}, e_{2}, e_{n+2}, \cdots  , e_{n}, e_{2n}]$.

<!-- PAGE 766 -->
$(1)$ Chứng minh rằng $T = P^{\top}$ AP là đối xứng ba đường chéo (2n) $\times$ (2n) ma trận với không chính đường chéo của tạo thành
$$T = \begin{pmatrix} 0 & a_{1} & 0 & 0 & 0 & 0 & \cdots & 0 \\ a_{1} & 0 & b_{1} & 0 & 0 & 0 & \cdots & 0 \\ 0 & b_{1} & 0 & a_{2} & 0 & 0 & \cdots & 0 \\ 0 & 0 & a_{2} & 0 & b_{2} & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \ddots & \ddots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & a_{n-1} & 0 & b_{n-1} & 0 \\ 0 & 0 & 0 & \cdots & 0 & b_{n-1} & 0 & a_{n} \\ 0 & 0 & 0 & \cdots & 0 & 0 & a_{n} & 0 \end{pmatrix} .$$
$(2)$ Chứng minh rằng nếu $x_{i}$ là unit vectơ riêng (eigenvector) cho trị riêng (eigenvalue) $\lambda_{i}$ của $T$, thì $\lambda_{i}  = \pm \sigma_{i}$ ở đâu $\sigma_{i}$ là giá trị kỳ dị (singular value) của $B$, và rằng
$$Px_{i} =\sqrt \frac{1}{\overline{2}} \begin{pmatrix} u_{i} \\ \pm v_{i} \end{pmatrix} ,$$
Ở đâu $u_{i}$ là unit các vectơ riêng (eigenvectors) của $B^{\top}B$ và $v_{i}$ là unit các vectơ riêng (eigenvectors) của $BB^{\top}$.
Bài toán 22.4. Tìm SVD của ma trận
$$A = \begin{pmatrix} 0 & 2 & 0 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{pmatrix} .$$
$$\mathbb{R}^{n}$$
Bài toán 22.5. Cho $u, v \in$ là hai khác không các vectơ, và cho $A = uv^{\top}$ là tương ứng hạng (rank) $1$ ma trận. Chứng minh rằng khác không giá trị kỳ dị (singular value) của $A$ là $\|u\|_{2} \|v\|_{2}$.
Bài toán 22.6. Cho $A$ là $n\times n$ thực ma trận. Chứng minh rằng nếu $\sigma_{1} , \dots  , \sigma_{n}$ là các giá trị kỳ dị (singular values) của $A$, thì $\sigma_{1}^{3} , \dots  , \sigma_{n}^{3}$ là các giá trị kỳ dị (singular values) của $AA^{\top}A$.
Bài toán 22.7. Cho $A$ là thực $n \times  n$ ma trận.
$(1)$ Chứng minh rằng lớn nhất giá trị kỳ dị (singular value) $\sigma_{1}$ của $A$ được cho bởi
$$\|\|_{2}$$
$$\sigma_{1}  = supx\neq 0 \frac{Ax}{\|x\|_{2}} ,$$
Và rằng điều này cận trên đúng (supremum) là đạt được tại $x = u_{1}$, cột thứ nhất trong $U$ trong SVD $A = V \Sigma U^{\top}$.
$(2)$ Mở rộng ở trên kết quả đến thực $m \times  n$ các ma trận.
Bài toán 22.8. Cho $A$ là thực $m \times  n$ ma trận. Chứng minh rằng nếu $B$ là bất kỳ ma trận con của $A$ (bởi giữ $M \le m$ các hàng và $N \le n$ các cột của $A)$, thì $(\sigma_{1} )_{B} \le (\sigma_{1} )_{A}$ (ở đâu $(\sigma_{1} )_{A}$ là lớn nhất giá trị kỳ dị (singular value) của $A$ và tương tự cho $(\sigma_{1} )_{B})$.

<!-- PAGE 767 -->
Bài toán 22.9. Cho $A$ là thực $n \times  n$ ma trận.
$(1)$ Giả sử $A$ là khả nghịch. Chứng minh rằng nếu $A = Q_{1}S_{1} = Q_{2}S_{2}$ là hai polar các phân rã của $A$, thì $Q_{1} = Q_{2}$ và $S_{1} = S_{2}$. Hint. $A^{\top}A = S_{1}^{2} = S_{2}^{2}$, với $S_{1}$ và $S_{2}$ đối xứng xác định dương (SPD). Thì sử dụng Bài toán 17.7.
$(2)$ Bây giờ giả sử rằng $A$ là suy biến. Chứng minh rằng nếu $A = Q_{1}S_{1} = Q_{2}S_{2}$ là hai polar các phân rã của $A$, thì $S_{1} = S_{2}$, nhưng $Q_{1}$ có thể không là bằng $Q_{2}$.
Bài toán 22.10. $(1)$ Cho $A$ là bất kỳ khả nghịch (thực) $n \times  n$ ma trận. Chứng minh rằng với mọi SVD, $A = V DU^{\top}$ của $A$, tích $V U^{\top}$ là cùng (i.e., nếu $V_{1}DU_{1}^{\top} = V_{2}DU_{2}^{\top}$, thì $V_{1}U_{1}^{\top}  = V_{2}U_{2}^{\top}$). Những gì thực hiện $V U^{\top}$ có đến thực hiện với dạng cực (polar form) của $A$?
$(2)$ Cho trước bất kỳ khả nghịch (thực) $n \times  n$ ma trận, $A$, chứng minh rằng tồn tại duy nhất một ma trận trực giao (orthogonal matrix), $Q \in$ O(n), sao cho $\|A$ - $Q\|_{F}$ là tối tiểu (dưới Chuẩn Frobenius (Frobenius norm)). Thực ra, chứng minh rằng $Q = V U^{\top}$, ở đâu $A = V DU^{\top}$ là SVD của $A$. Hơn thế nữa, nếu det() $> 0$, chỉ ra rằng $Q \in$ Do đó(n). Những gì có thể bạn nói nếu $A$ là suy biến (i.e., non-invertible)?
Bài toán 22.11. $(1)$ Chứng minh rằng cho bất kỳ ma trận cỡ $n \times  n$ $A$ và bất kỳ ma trận trực giao (orthogonal matrix) $Q$, ta có
$$\max{\mathrm{tr}(QA) | Q \in O(n)} = \sigma_{1}  + \cdots  + \sigma_{n} ,$$
Ở đâu $\sigma_{1}  \ge \cdots  \ge \sigma_{n}$ là các giá trị kỳ dị (singular values) của $A$. Hơn nữa, điều này cực đại là đạt được bởi $Q = UV^{\top}$, ở đâu $A = V \Sigma U^{\top}$ là bất kỳ SVD cho $A$.
$(2)$ Bằng cách áp dụng ở trên kết quả với $A = X^{\top}Z$ và $Q = R$, suy ra kết quả sau đây: với mọi hai cố định $n \times  k$ các ma trận $X$ và $Z$, cực tiểu của tập hợp
$${\|X -ZR\|_{F} | R \in O(k)}$$
Là đạt được bởi $R = UV^{\top}$ với mọi SVD phân rã $V \Sigma U^{\top} = X^{\top}Z$ của $X^{\top}Z$.
Nhận xét: bài toán của việc tìm ma trận trực giao (orthogonal matrix) $R$ sao cho $ZR$ đến như close như khả dĩ/có thể đến $X$ được gọi là trực giao Procrustes bài toán; xem Strang $[177]$ (Mục IV.9) cho history của bài toán này.

<!-- PAGE 768 -->
