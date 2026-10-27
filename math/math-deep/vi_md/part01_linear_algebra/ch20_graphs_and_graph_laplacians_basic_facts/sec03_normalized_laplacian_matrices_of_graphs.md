# Được chuẩn hóa Laplacian Các ma trận của Các đồ thị


<!-- PAGE 727 -->

> **Mệnh đề 20.5.** Cho $G = (V, W)$ được trọng số đồ thị. số $c$ của liên thông các thành phần $K_{1}, \dots  , K_{c}$ của underlying đồ thị của $G$ bằng số chiều của không gian hạch (nullspace) của $L$, mà bằng bội (multiplicity) của trị riêng (eigenvalue) $0$. Hơn nữa, không gian hạch (nullspace) của $L$ có cơ sở (basis) bao gồm của indicator các vectơ của liên thông các thành phần của $G$, nghĩa là, các vectơ $(f_{1}, \dots  , f_{m})$ sao cho $f_{j} = 1$ khi và chỉ khi $v_{j} \in K_{i}$ và $f_{j} = 0$ ngược lại.

*Chứng minh.* Vì $L = BB^{\top}$ cho ma trận liên thuộc (incidence matrix) $B$ liên kết với bất kỳ được định hướng đồ thị thu được từ $G$, và vì $L$ và $B^{\top}$ có cùng không gian hạch (nullspace), theo Mệnh đề 20.1, số chiều của không gian hạch (nullspace) của $L$ bằng số $c$ của liên thông các thành phần của $G$ và indicator các vectơ của liên thông các thành phần của $G$ tạo thành cơ sở (basis) của Ker $(L)$. Mệnh đề 20.5 suy ra rằng nếu underlying đồ thị của $G$ là liên thông, thì thứ hai trị riêng (eigenvalue) $\lambda_{2}$ của $L$ là chặt dương. Đáng chú ý, trị riêng (eigenvalue) $\lambda_{2}$ chứa nhiều information về đồ thị $G$ (giả sử rằng $G = (V, E)$ là undirected đồ thị). Điều này đã là thứ nhất discovered bởi Fiedler trong $1973$, và cho điều này lý do, $\lambda_{2}$ là thường referred đến như Fiedler số. Cho nhiều hơn/thêm trên các tính chất của Fiedler số, xem Godsil và Royle $[80]$ (Chương $13)$ và Chung $[39]$. Tổng quát hơn, phổ (spectrum) $(0, \lambda_{2} , \dots  , \lambda_{m}$) của $L$ chứa nhiều information về combinatorial cấu trúc của đồ thị $G$. Leverage của điều này information là object của spectral đồ thị lý thuyết.

## 20.3 Được chuẩn hóa Laplacian Các ma trận của Các đồ thị

Hóa ra được chuẩn hóa các biến thể của toán tử Laplace của đồ thị (graph Laplacian) là cần thiết, especially trong các ứng dụng đến đồ thị clustering. Các phần tử này các biến thể tạo nghĩa chỉ nếu $G$ có không có isolated các đỉnh.

> **Định nghĩa 20.18.** Cho trước được trọng số đồ thị $G = (V, W)$, đỉnh $u \in V$ là isolated nếu nó là không incident đến bất kỳ khác đỉnh. Điều này có nghĩa là mọi hàng của $W$ chứa một số chặt dương phần tử (entry). Nếu $G$ có không có isolated các đỉnh, thì ma trận bậc (degree matrix) $D$ chứa dương các phần tử (entries), do đó nó là khả nghịch và $D^{-1/2}$ làm cho nghĩa; cụ thể là
$$D^{-1/2}= \mathrm{diag}(d_{1}^{-1/2}, \dots  , d_{m}^{-1/2}),$$
Và tương tự với mọi thực exponent $\alpha$.

> **Định nghĩa 20.19.** Cho trước bất kỳ được trọng số được trực tiếp đồ thị $G = (V, W)$ với không có isolated đỉnh và với $V = {v_{1}, \dots  , v_{m}}$, (được chuẩn hóa) các toán tử Laplace của đồ thị $L_{sym}$ và $L_{rw}$ của $G$ được định nghĩa bởi
$$L_{sym} = D^{-1/2}LD^{-1/2}= I -D^{-1/2}WD^{-1/2}$$
$$L_{rw} = D^{-1}L = I -D^{-1}W.$$

<!-- PAGE 728 -->
Nhận thấy rằng Laplacian $L_{sym} = D^{-1/2}LD^{-1/2}$ là ma trận đối xứng (symmetric matrix) (bởi vì $L$ và $D^{-1/2}$ là đối xứng) và rằng
$$L_{rw} = D^{-1/2}L_{sym}D^{1/2}.$$
Lý do cho ký hiệu $L_{rw}$ là rằng ma trận này là closely related đến ngẫu nhiên walk trên đồ thị $G$.

> **Ví dụ 20.1.** Như ví dụ, các ma trận $L_{sym}$ và $L_{rw}$ liên kết với đồ thị $G_{1}$ là
$$L_{sym} = \begin{pmatrix} 1.0000 & -0.3536 & -0.4082 & 0 & 0 \\ -0.3536 & 1.0000 & -0.2887 & -0.2887 & -0.3536 \\ -0.4082 & -0.2887 & 1.0000 & -0.3333 & 0 \\ 0 & -0.2887 & -0.3333 & 1.0000 & -0.4082 \\ 0 & 0.3536 & 0 & 0.4082 & 1.0000 \end{pmatrix}$$
$$--$$
Và
$$L_{rw} = \begin{pmatrix} 1.0000 & -0.5000 & -0.5000 & 0 & 0 \\ -0.2500 & 1.0000 & -0.2500 & -0.2500 & -0.2500 \\ -0.3333 & -0.3333 & 1.0000 & -0.3333 & 0 \\ 0 & -0.3333 & -0.3333 & 1.0000 & -0.3333 \\ 0 & 0.5000 & 0 & 0.5000 & 1.0000 \end{pmatrix} .$$
$$--$$
Vì chưa chuẩn hóa Laplacian $L$ có thể được viết dưới dạng $L = BB^{\top}$, ở đâu $B$ là ma trận liên thuộc (incidence matrix) của bất kỳ được định hướng đồ thị thu được từ underlying đồ thị của $G = (V, W)$, nếu ta cho
$$B_{sym} = D^{-1/2}B,$$
Ta thu được
$$L_{sym} = B_{sym}B_{sym}^{\top}.$$
Đặc biệt, với mọi suy biến phân rã $B_{sym} = U\Sigma V^{\top}$ của $B_{sym}$ (với $U$ $m \times  m$ ma trận trực giao (orthogonal matrix), $\Sigma$ “đường chéo” $m\times n$ ma trận của các giá trị kỳ dị (singular values), và $V$ $n\times n$ ma trận trực giao (orthogonal matrix)), các trị riêng (eigenvalues) của $L_{sym}$ là squares của đỉnh/trên $m$ các giá trị kỳ dị (singular values) của $B_{sym}$, và các vectơ trong $U$ là trực chuẩn các vectơ riêng (eigenvectors) của $L_{sym}$ đối với các trị riêng (các trị riêng (eigenvalues)) này (squares của đỉnh/trên $m$ đường chéo các phần tử (entries) của $\Sigma$). Việc tính toán SVD của $B_{sym}$ một cách tổng quát cho ta nhiều hơn/thêm accurate các kết quả hơn diagonalizing $L_{sym}$, especially khi $L_{sym}$ có các trị riêng (eigenvalues) với cao bội (multiplicity). Có đơn giản relationships giữa các trị riêng (eigenvalues) và các vectơ riêng (eigenvectors) của $L_{sym}$, và $L_{rw}$. Ở đó là cũng đơn giản relationship với suy rộng/tổng quát hóa trị riêng (eigenvalue) bài toán Lx $= \lambda$ Dx.

> **Mệnh đề 20.6.** Cho $G = (V, W)$ được trọng số đồ thị mà không có isolated các đỉnh. các toán tử Laplace của đồ thị, $L, L_{sym}$, và $L_{rw}$ thỏa mãn các tính chất sau đây:

<!-- PAGE 729 -->
$(1)$ ma trận $L_{sym}$ là đối xứng và nửa xác định dương (positive semidefinite). Thực ra,
$$!2$$
$$x^{\top}L_{sym}x = \frac{1}{2} \sum_{i,j=1}^{m}  w_{i j}\sqrt \frac{x_{i}}{\overline{d}_{i}} - \frac{x_{j}}{p\overline{d}_{j}} for all x \in \mathbb{R}^{m}.$$
$(2)$ được chuẩn hóa các toán tử Laplace của đồ thị $L_{sym}$ và $L_{rw}$ có cùng phổ (spectrum) $(0 = \nu_{1}  \le \nu_{2}  \le \dots  \le \nu_{m}$), và vectơ $u \neq  0$ là vectơ riêng (eigenvector) của $L_{rw}$ cho $\lambda$ khi và chỉ khi $D^{1/2}u$ là vectơ riêng (eigenvector) của $L_{sym}$ cho $\lambda$.
$(3)$ các toán tử Laplace của đồ thị $L$ và $L_{sym}$ là đối xứng và nửa xác định dương (positive semidefinite).
$(4) A$ vectơ $u \neq  0$ là nghiệm của suy rộng/tổng quát hóa trị riêng (eigenvalue) bài toán Lu $= \lambda$ Du khi và chỉ khi $D^{1/2}u$ là vectơ riêng (eigenvector) của $L_{sym}$ cho trị riêng (eigenvalue) $\lambda$ khi và chỉ khi $u$ là vectơ riêng (eigenvector) của $L_{rw}$ cho trị riêng (eigenvalue) $\lambda$.
$(5)$ các toán tử Laplace của đồ thị, $L$ và $L_{rw}$ có cùng không gian hạch (nullspace). Với mọi vectơ $u$, ta có $u \in$ Ker $(L)$ khi và chỉ khi $D^{1/2}u \in$ Ker $(L_{sym})$.
$(6)$ vectơ $1$ là trong không gian hạch (nullspace) của $L_{rw}$, và $D^{1/2}1$ là trong không gian hạch (nullspace) của $L_{sym}$.
$(7)$ Với mọi trị riêng (eigenvalue) $\nu_{i}$ của được chuẩn hóa toán tử Laplace của đồ thị (graph Laplacian) $L_{sym}$, ta có $0 \le \nu_{i}  \le 2$. Hơn nữa, $\nu_{m}  = 2$ khi và chỉ khi underlying đồ thị của $G$ chứa không tầm thường liên thông bipartite thành phần.
$(8)$ Nếu $m \ge 2$ và nếu underlying đồ thị của $G$ là không đầy đủ $graph,^{1}$ thì $\nu_{2}  \le 1$. Hơn nữa underlying đồ thị của $G$ là đầy đủ đồ thị khi và chỉ khi $\nu_{2}  =_{m-1}^{m}$.
$(9)$ Nếu $m \ge 2$ và nếu underlying đồ thị của $G$ là liên thông, thì $\nu_{2}  > 0$.
$(10)$ Nếu $m \ge 2$ và nếu underlying đồ thị của $G$ có không có isolated các đỉnh, thì $\nu_{m}  \ge_{m-1}^{m}$.

*Chứng minh.* $(1)$ Ta có $L_{sym} = D^{-1/2}LD^{-1/2}$, và $D^{-1/2}$ là đối xứng ma trận khả nghịch (invertible matrix) (vì nó là khả nghịch ma trận đường chéo (diagonal matrix)). Nó là well-known sự kiện của tuyến tính đại số rằng nếu $B$ là ma trận khả nghịch (invertible matrix), thì ma trận $S$ là đối xứng, nửa xác định dương (positive semidefinite) khi và chỉ khi $BSB^{\top}$ là đối xứng, nửa xác định dương (positive semidefinite). Vì $L$ là đối xứng, nửa xác định dương (positive semidefinite), do đó là $L_{sym} = D^{-1/2}LD^{-1/2}$. công thức
$$!2$$
$$x^{\top}L_{sym}x = \frac{1}{2} \sum_{i,j=1}^{m}  w_{i j}\sqrt \frac{x_{i}}{\overline{d}_{i}} - \frac{x_{j}}{p\overline{d}_{j}} for all x \in \mathbb{R}^{m}$$
Suy ra ngay lập tức từ Mệnh đề 20.4 bằng cách thay thế $x$ bởi $D^{-1/2}x$, và cũng chỉ ra rằng $L_{sym}$ là nửa xác định dương (positive semidefinite).
$(2)$ Vì
$$L_{rw} = D^{-1/2}L_{sym}D^{1/2},$$
$\overline{1}\overline{Recall} \overline{that} \overline{an} \overline{undirected} \overline{graph} \overline{is} \overline{complete}$ nếu với mọi hai phân biệt các nút $u, v$, có một cạnh ${u, v}$.

<!-- PAGE 730 -->
Các ma trận $L_{sym}$ và $L_{rw}$ là đồng dạng, mà suy ra rằng chúng có cùng phổ (spectrum). Thực ra, vì $D^{1/2}$ là khả nghịch,
$$L_{rw}u = D^{-1}Lu = \lambda u$$
Khi và chỉ khi
$$D^{-1/2}Lu = \lambda D^{1/2}u$$
Khi và chỉ khi
$$D^{-1/2}LD^{-1/2}D^{1/2}u = L_{sym}D^{1/2}u = \lambda D^{1/2}u,$$
Mà chỉ ra rằng vectơ $u \neq  0$ là vectơ riêng (eigenvector) của $L_{rw}$ cho $\lambda$ khi và chỉ khi $D^{1/2}u$ là vectơ riêng (eigenvector) của $L_{sym}$ cho $\lambda$.
$(3)$ Ta đã biết rằng $L$ và $L_{sym}$ là nửa xác định dương (positive semidefinite).
$(4)$ Vì $D^{-1/2}$ là khả nghịch, ta có
$$Lu = \lambda Du$$
Khi và chỉ khi
$$D^{-1/2}Lu = \lambda D^{1/2}u$$
Khi và chỉ khi
$$D^{-1/2}LD^{-1/2}D^{1/2}u = L_{sym}D^{1/2}u = \lambda D^{1/2}u,$$
Mà chỉ ra rằng vectơ $u \neq  0$ là nghiệm của suy rộng/tổng quát hóa trị riêng (eigenvalue) bài toán Lu $= \lambda$ Du khi và chỉ khi $D^{1/2}u$ là vectơ riêng (eigenvector) của $L_{sym}$ cho trị riêng (eigenvalue) $\lambda$. phần thứ hai của phát biểu suy ra từ $(2)$.
$(5)$ Vì $D^{-1}$ là khả nghịch, ta có Lu $= 0$ khi và chỉ khi $D^{-1}Lu = L_{rw}u = 0$. Tương tự, vì $D^{-1/2}$ là khả nghịch, ta có Lu $= 0$ khi và chỉ khi $D^{-1/2}LD^{-1/2}D^{1/2}u = 0$ khi và chỉ khi $D^{1/2}u \in$ Ker $(L_{sym})$.
$(6)$ Vì L1 $= 0$, ta thu được $L_{rw}1 = D^{-1}L1 = 0$. Rằng $D^{1/2}1$ là trong không gian hạch (nullspace) của $L_{sym}$ suy ra từ $(2)$. Các tính chất (7)–(10) được chứng minh trong Chung $[39]$ (Chương $1)$. các trị riêng (eigenvalues) các ma trận $L_{sym}$ và $L_{rw}$ từ Ví dụ 20.1 là
$$0, 7257, 1.1667, 1.5, 1.6076.$$
Mặt khác, các trị riêng (eigenvalues) của chưa chuẩn hóa Laplacian cho $G_{1}$ là
$$0, 1.5858, 3, 4.4142, 5.$$
Nhận xét: Nhận thấy rằng mặc dù các ma trận $L_{sym}$ và $L_{rw}$ có cùng phổ (spectrum), ma trận $L_{rw}$ là một cách tổng quát không đối xứng, trong khi đó $L_{sym}$ là đối xứng. phiên bản của Mệnh đề 20.5 cũng nghiệm đúng cho các toán tử Laplace của đồ thị $L_{sym}$ và $L_{rw}$. Điều này suy ra dễ dàng từ sự kiện rằng Mệnh đề 20.1 áp dụng đến underlying đồ thị của được trọng số đồ thị. chứng minh là để lại như một bài tập.
