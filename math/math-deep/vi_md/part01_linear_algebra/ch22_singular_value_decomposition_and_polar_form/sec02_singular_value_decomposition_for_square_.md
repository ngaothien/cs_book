# Phân rã giá trị kỳ dị (SVD) cho Các ma trận vuông


<!-- PAGE 753 -->
Vì
$$\dim(\mathrm{Im} f) = n -\dim(\mathrm{Ker} f)$$
Và
$$\dim(\mathrm{Im} f^{*} ) = n -\dim((\mathrm{Im} f^{*} )^{\perp}),$$
Từ
$$\mathrm{Ker} f = (\mathrm{Im} f^{*} )^{\perp}$$
Ta cũng có
$$\dim(\mathrm{Ker} f) = \dim((\mathrm{Im} f^{*} )^{\perp}),$$
Từ mà ta thu được
$$\dim(\mathrm{Im} f) = \dim(\mathrm{Im} f^{*} ).$$
Vì
$$\dim(\mathrm{Ker} (f^{*} \circ f)) + \dim(\mathrm{Im} (f^{*} \circ f)) = \dim(E),$$
Ker $(f^{*} \circ f) =$ Ker $f$ và Ker $f =$ (Im $f^{*} )^{\perp}$, ta thu được
$$\dim((\mathrm{Im} f^{*} )^{\perp}) + \dim(\mathrm{Im} (f^{*} \circ f)) = \dim(E).$$
Vì
$$\dim((\mathrm{Im} f^{*} )^{\perp}) + \dim(\mathrm{Im} f^{*} ) = \dim(E),$$
Ta suy ra rằng
$$\dim(\mathrm{Im} f^{*} ) = \dim(\mathrm{Im} (f^{*} \circ f)).$$
Đồng dạng chứng minh chỉ ra rằng
$$\dim(\mathrm{Im} f) = \dim(\mathrm{Im} (f \circ f^{*} )).$$
Hệ quả là, $f, f^{*} , f^{*} \circ f$, và $f \circ f^{*}$ có cùng hạng (rank).

## 22.2 Phân rã giá trị kỳ dị (SVD) cho

$$Square Matrices$$
Ta sẽ bây giờ chứng minh rằng mọi ma trận vuông (square matrix) có SVD. Mạnh hơn các kết quả có thể được thu được nếu ta thứ nhất xét dạng cực (polar form) và thì derive SVD từ nó (có tính duy nhất các tính chất của phân rã cực (polar decomposition)). Cho của ta các mục đích, tính duy nhất các kết quả là không như quan trọng do đó ta content chính chúng ta với sự tồn tại các kết quả, có các chứng minh là đơn giản hơn. Độc giả interested trong nhiều hơn/thêm tổng quát treatment là referred đến Gallier $[73]$. early history của phân rã giá trị kỳ dị (SVD) được mô tả trong fascinating paper bởi Stewart $[171]$. SVD là do Beltrami và Camille Jordan một cách độc lập $(1873, 1874)$. Gauss là grandfather của tất cả điều này, cho his hoạt động/công trình trên bình phương tối thiểu (least squares) $(1809, 1823)$ (nhưng Legendre cũng published paper trên bình phương tối thiểu (least squares)!). Thì đến Sylvester, Schmidt, và

<!-- PAGE 754 -->
Hermann Weyl. Sylvester’s hoạt động/công trình đã là apparently “opaque.” He gave tính toán phương pháp để tìm SVD. Schmidt’s hoạt động/công trình một cách thực có đến thực hiện với tích phân các phương trình và đối xứng và asymmetric các hạt nhân $(1907)$. Weyl’s hoạt động/công trình có đến thực hiện với perturbation lý thuyết $(1912)$. Autonne came lên với phân rã cực (polar decomposition) $(1902, 1915)$. Eckart và Young được mở rộng SVD đến rectangular các ma trận $(1936, 1939)$.

> **Định lý 22.5.** (Phân rã giá trị kỳ dị (SVD)) Với mọi thực $n\times n$ ma trận $A$ có hai các ma trận trực giao $U$ và $V$ và ma trận đường chéo (diagonal matrix) $D$ sao cho $A = V DU^{\top}$, ở đâu $D$ là của tạo thành
$$D = \begin{pmatrix} \sigma_{1} & \dots \\ \sigma_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & \sigma_{n} \end{pmatrix} ,$$
Ở đâu $\sigma_{1} , \dots  , \sigma_{r}$ là các giá trị kỳ dị (singular values) của $A$, i.e., (dương) square các nghiệm của khác không các trị riêng (eigenvalues) của $A^{\top}A$ và $A A^{\top}$, và $\sigma_{r+1}  = \cdots  = \sigma_{n}  = 0$. các cột của $U$ là các vectơ riêng (eigenvectors) của $A^{\top}A$, và các cột của $V$ là các vectơ riêng (eigenvectors) của $A A^{\top}$.

*Chứng minh.* Vì $A^{\top}A$ là ma trận đối xứng (symmetric matrix), thực ra, nửa xác định dương (positive semidefinite) ma trận, tồn tại một ma trận trực giao (orthogonal matrix) $U$ sao cho
$$A^{\top}A = UD^{2}U^{\top} ,$$
Với $D = diag(\sigma_{1} , \dots  , \sigma_{r} , 0, \dots  , 0)$, ở đâu $\sigma_{1}^{2} , \dots  , \sigma_{r}^{2}$ là khác không các trị riêng (eigenvalues) của $A^{\top}A$, và ở đâu $r$ là hạng (rank) của $A$; nghĩa là, $\sigma_{1} , \dots  , \sigma_{r}$ là các giá trị kỳ dị (singular values) của $A$. Suy ra rằng
$$U^{\top} A^{\top}AU = (AU)^{\top}AU = D^{2},$$
Và nếu ta cho $f_{j}$ là cột thứ $j$ của $AU$ cho $j = 1, \dots  , n$, thì ta có
$$\langle f_{i}, f_{j}\rangle = \sigma_{i}^{2}  \delta_{ij} ,1 \le i, j \le r$$
Và
$$f_{j} = 0,r + 1 \le j \le n.$$
Nếu ta định nghĩa $(v_{1}, \dots  , v_{r})$ bởi
$$v_{j} = \sigma_{j}^{-1}  f_{j},1 \le j \le r,$$
Thì ta có
$$\langle v_{i}, v_{j}\rangle = \delta_{ij} ,1 \le i, j \le r,$$
Do đó đầy đủ $(v_{1}, \dots  , v_{r})$ vào cơ sở trực chuẩn (orthonormal basis) $(v_{1}, \dots  , v_{r}, v_{r+1}, \dots  , v_{n})$ (ví dụ, bằng cách sử dụng Gram–Schmidt). Bây giờ vì $f_{j} = \sigma_{j} v_{j}$ cho $j = 1 \dots  , r$, ta có
$$\langle v_{i}, f_{j}\rangle = \sigma_{j} \langle v_{i}, v_{j}\rangle = \sigma_{j} \delta_{i,j} ,1 \le i \le n, 1 \le j \le r$$

<!-- PAGE 755 -->
Và vì $f_{j} = 0$ cho $j = r + 1, \dots  , n$,
$$\langle v_{i}, f_{j}\rangle = 01 \le i \le n, r + 1 \le j \le n.$$
Nếu $V$ là ma trận có các cột là $v_{1}, \dots  , v_{n}$, thì $V$ là trực giao và ở trên các phương trình chứng minh rằng
$$V^{\top} AU = D,$$
Mà cho ta $A = V DU^{\top}$, như cần thiết. phương trình $A = V DU^{\top}$ suy ra rằng
$$A^{\top}A = UD^{2}U^{\top} ,AA^{\top}= V D^{2}V^{\top} ,$$
Mà chỉ ra rằng $A^{\top}A$ và $AA^{\top}$ có cùng các trị riêng (eigenvalues), rằng các cột của $U$ là các vectơ riêng (eigenvectors) của $A^{\top}A$, và rằng các cột của $V$ là các vectơ riêng (eigenvectors) của $AA^{\top}$.

> **Ví dụ 22.4.** Ở đây là đơn giản ví dụ của cách mà để sử dụng chứng minh của Định lý 22.5 để thu được
$$an SVD decomposition.Let A = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} .Then A^{\top}= \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} , A^{\top}A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} , and$$
$$AA^{\top}= \begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix} . A simple calculation shows that the eigenvalues of A^{\top}A are 2 and 0, and$$
$$for the eigenvalue 2, a unit eigenvector is \begin{pmatrix} \sqrt \\ 1/\sqrt{2} \\ 1/ & 2 \end{pmatrix} , while a unit eigenvector for the eigenvalue$$
$$\sqrt$$
$$0 is \begin{pmatrix} \sqrt \\ 1/\sqrt{2} \\ -1/\sqrt2 \\ 1/ & 2 \end{pmatrix} . Observe that the singular values are \sigma_{1}  =\overline{2} and \sigma_{2}  = 0. Furthermore,$$
$$U = \begin{pmatrix} \sqrt \\ \sqrt & 1/\sqrt{2} \\ 1/ & 2 & -1/ & 2 \end{pmatrix} = U^{\top} . To determine V , the proof of Theorem 22.5 tells us to first$$
Tính toán
$$AU = \begin{pmatrix} \sqrt \\ \overline{2} & 0 \\ 0 & 0 \end{pmatrix} ,$$
Và thì tập hợp
$$\sqrt$$
$$v_{1} = (1/\overline{2)} \begin{pmatrix} \sqrt \\ \overline{2} \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} .$$
Một lần $v_{1}$ được xác định, vì $\sigma_{2}  = 0$, ta có freedom đến chọn $v_{2}$ sao cho $(v_{1}, v_{2})$
$$forms an orthonormal basis for\mathbb{R}^{2}. Naturally, we chose v_{2} = \begin{pmatrix} 0 \\ 1 \end{pmatrix} and set V = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} . The$$
Các cột của $V$ là unit các vectơ riêng (eigenvectors) của $AA^{\top}$, nhưng việc tìm $V$ bởi việc tính toán unit các vectơ riêng (eigenvectors) của $AA^{\top}$ thực hiện không đảm bảo rằng các vectơ này là consistent với $U$ sao cho $A = V \Sigma U^{\top}$. Do đó một có để sử dụng AU thay vì. Ta để lại nó đến độc giả để kiểm tra rằng
$$A = V \begin{pmatrix} \sqrt \\ \overline{2} & 0 \\ 0 & 0 \end{pmatrix} U^{\top} .$$
Định lý 22.5 suggests sau đây định nghĩa.

<!-- PAGE 756 -->

> **Định nghĩa 22.3.** bộ ba $(U, D, V$) sao cho $A = V D U^{\top}$, ở đâu $U$ và $V$ là trực giao và $D$ là ma trận đường chéo (diagonal matrix) có các phần tử (entries) là không âm (nó là nửa xác định dương (positive semidefinite)) được gọi là một phân rã giá trị kỳ dị (SVD) (SVD) của $A$. Nếu $D = diag(\sigma_{1} , \dots  , \sigma_{n}$), nó là thông lệ giả sử rằng $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{n}$. Matlab command cho việc tính toán SVD $A = V DU^{\top}$ của ma trận $A$ là $[V, D, U] =$ svd(). chứng minh của Định lý 22.5 chỉ ra rằng có hai các cơ sở trực chuẩn $(u_{1}, \dots  , u_{n})$ và $(v_{1}, \dots  , v_{n})$, ở đâu $(u_{1}, \dots  , u_{n})$ là các vectơ riêng (eigenvectors) của $A^{\top}A$ và $(v_{1}, \dots  , v_{n})$ là các vectơ riêng (eigenvectors) của $AA^{\top}$. Hơn nữa, $(u_{1}, \dots  , u_{r})$ là cơ sở trực chuẩn (orthonormal basis) của Im $A^{\top}, (u_{r+1}, \dots  , u_{n})$ là cơ sở trực chuẩn (orthonormal basis) của Ker $A, (v_{1}, \dots  , v_{r})$ là cơ sở trực chuẩn (orthonormal basis) của Im $A$, và $(v_{r+1}, \dots  , v_{n})$ là cơ sở trực chuẩn (orthonormal basis) của Ker $A^{\top}$. Bằng cách sử dụng nhận xét được tạo trong Chương $4$, nếu ta ký hiệu các cột của $U$ bởi $u_{1}, \dots  , u_{n}$ và các cột của $V$ bởi $v_{1}, \dots  , v_{n}$, thì ta có thể viết
$$A = V D U^{\top} = \sigma_{1} v_{1}u_{1}^{\top} + \cdots  + \sigma_{r} v_{r}u_{r}^{\top} ,$$
Với $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{r}$. Hệ quả là, nếu $r$ là nhiều nhỏ hơn hơn $n$ (ta viết $r \ll n)$, ta xem rằng $A$ có thể được reconstructed từ $U$ và $V$ bằng cách sử dụng nhiều nhỏ hơn số của các phần tử. Điều này ý tưởng sẽ được sử dụng đến cung cấp “hạng thấp (low-rank)” các xấp xỉ của ma trận. ý tưởng là đến giữ chỉ $k$ đỉnh/trên các giá trị kỳ dị (singular values) với một số phù hợp $k \ll r$ cho mà $\sigma_{k+1} , \dots  , \sigma_{r}$ là rất nhỏ.
Các nhận xét:
$(1)$ Trong Strang $[176]$ các ma trận $U, V, D$ được ký hiệu bởi $U = Q_{2}, V = Q_{1}$, và $D = \Sigma$, và SVD được viết như $A = Q_{1}\Sigma Q_{2}^{\top}$. Điều này có advantage rằng $Q_{1}$ đến trước $Q_{2}$ trong $A = Q_{1}\Sigma Q_{2}^{\top}$. Điều này có disadvantage rằng $A$ các ánh xạ các cột của $Q_{2}$ (các vectơ riêng (eigenvectors) của $A^{\top}A)$ đến các bội của các cột của $Q_{1}$ (các vectơ riêng (eigenvectors) của $A A^{\top})$.
$(2)$ Các thuật toán cho thực sự việc tính toán SVD của ma trận được trình bày trong Golub và Van Loan $[83]$, Demmel $[48]$, và Trefethen và Bau $[182]$, ở đâu SVD và của nó các ứng dụng cũng được thảo luận khá extensively.
$(3)$ Nếu $A$ là ma trận đối xứng (symmetric matrix), thì nói chung, không có SVD $V \Sigma U^{\top}$ của $A$ với $V = U$. Tuy nhiên, nếu $A$ là nửa xác định dương (positive semidefinite), thì các trị riêng (eigenvalues) của $A$ là không âm, và do đó khác không các trị riêng (eigenvalues) của $A$ bằng các giá trị kỳ dị (singular values) của $A$ và SVDs của $A$ là của tạo thành
$$A = V \Sigma V^{\top} .$$
$(4)$ SVD cũng áp dụng đến phức các ma trận. Trong trường hợp này, với mọi phức $n\times n$ ma trận $A$, có hai các ma trận unita $U$ và $V$ và ma trận đường chéo (diagonal matrix) $D$ sao cho
$$A = V D U^{*} ,$$
Ở đâu $D$ là ma trận đường chéo (diagonal matrix) bao gồm của thực các phần tử (entries) $\sigma_{1} , \dots  , \sigma_{n}$, ở đâu $\sigma_{1}  \ge \cdots  \ge \sigma_{r}$ là các giá trị kỳ dị (singular values) của $A$, i.e., dương square các nghiệm của khác không các trị riêng (eigenvalues) của $A^{*}A$ và $A A^{*}$, và $\sigma_{r+1}  = \dots  = \sigma_{n}  = 0$.
