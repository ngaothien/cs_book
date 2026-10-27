# Tóm tắt


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
