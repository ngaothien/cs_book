# Laplacian Các ma trận của Các đồ thị


<!-- PAGE 723 -->

## 20.2 Laplacian Các ma trận của Các đồ thị

Cho chúng ta bắt đầu với được trực tiếp các đồ thị, mặc dù như ta sẽ xem, các toán tử Laplace của đồ thị là một cách cơ bản liên kết với undirected đồ thị. then chốt mệnh đề ở dưới chỉ ra cách mà cho trước undirected đồ thị $G$, với mọi định hướng $\sigma$ của $G, B^{\sigma}(B^{\sigma})^{\top}$ relates đến ma trận kề (adjacency matrix) $A$ (ở đâu $B^{\sigma}$ là ma trận liên thuộc (incidence matrix) của được trực tiếp đồ thị $G^{\sigma})$. Ta reproduce chứng minh trong Gallier $[72]$ (xem cũng Godsil và Royle $[80])$.

> **Mệnh đề 20.2.** Cho trước bất kỳ undirected đồ thị $G$, với mọi định hướng $\sigma$ của $G$, nếu $B^{\sigma}is$ ma trận liên thuộc (incidence matrix) của được trực tiếp đồ thị $G^{\sigma}, A$ là ma trận kề (adjacency matrix) của $G^{\sigma}$, và $D$ là ma trận bậc (degree matrix) sao cho $D_{i i} = d(v_{i})$, thì
$$B^{\sigma}(B^{\sigma})^{\top}= D -A.$$
Hệ quả là, $L = B^{\sigma}(B^{\sigma})^{\top}$ là độc lập của định hướng $\sigma$ của $G$, và D-A là đối xứng và nửa xác định dương (positive semidefinite); nghĩa là, các trị riêng (eigenvalues) của $D$ - $A$ là thực và không âm.

*Chứng minh.* phần tử (entry) $B^{\sigma}(B^{\sigma})_{i j}^{\top}$ là tích vô hướng (inner product) của hàng thứ $i$ $b_{i}^{\sigma}$, và hàng thứ $j$ $b_{j}^{\sigma}$ của $B^{\sigma}$. Nếu $i = j$, thì như
$$+1if s(e_{k}) = v_{i}$$
$$$$
$$$$
$$b_{i k}^{\sigma} =-1if t(e_{k}) = v_{i}$$
$$0otherwise$$
$$$$
Ta xem rằng $b_{i}^{\sigma} \cdot  b_{i}^{\sigma} = d(v_{i})$. Nếu $i \neq  j$, thì $b_{i}^{\sigma} \cdot  b_{j}^{\sigma}$ ̸ $= 0$ khi và chỉ khi tồn tại một cạnh $e_{k}$ với $s(e_{k}) = v_{i}$ và $t(e_{k}) = v_{j}$ hoặc vice-versa (mà là mutually exclusive các trường hợp, vì $G^{\sigma}$ phát sinh bởi orienting undirected đồ thị), trong mà trường hợp, $b_{i}^{\sigma} \cdot  b_{j}^{\sigma} = -1$. Vì vậy,
$$B^{\sigma}(B^{\sigma})^{\top}= D -A,$$
Như đã khẳng định. Với mọi $x \in \mathbb{R}^{m}$, ta có
$$x^{\top}Lx = x^{\top}B^{\sigma}(B^{\sigma})^{\top}x = ((B^{\sigma})^{\top}x)^{\top}(B^{\sigma})^{\top}x =

$(B^{\sigma})^{\top}x_{2}^{2}$

$\ge$ 0,$$ since the Euclidean norm $\|\|_{2}$ is positive (definite). Therefore, $L = B^{\sigma}(B^{\sigma})^{\đỉnh/trên}$ là nửa xác định dương (positive semidefinite). Nó là well-known rằng thực ma trận đối xứng (symmetric matrix) là nửa xác định dương (positive semidefinite) khi và chỉ khi các trị riêng (các trị riêng (eigenvalues)) của nó là không âm.

> **Định nghĩa 20.15.** ma trận $L = B^{\sigma}(B^{\sigma})^{\top} = D$ - $A$ được gọi là (chưa chuẩn hóa) toán tử Laplace của đồ thị (graph Laplacian) của đồ thị $G^{\sigma}$. (chưa chuẩn hóa) toán tử Laplace của đồ thị (graph Laplacian) của undirected đồ thị $G = (V, E)$ được định nghĩa bởi
$$L = D -A.$$

<!-- PAGE 724 -->
Ví dụ, toán tử Laplace của đồ thị (graph Laplacian) của đồ thị $G_{1}$ là
$$L = \begin{pmatrix} 2 & -1 & -1 & 0 & 0 \\ -1 & 4 & -1 & -1 & -1 \\ -1 & -1 & 3 & -1 & 0 \\ 0 & -1 & -1 & 3 & -1 \\ 0 & 1 & 0 & 1 & 2 \end{pmatrix} .$$
$$--$$
Nhận thấy rằng mỗi hàng của $L$ các tổng đến không (bởi vì $(B^{\sigma})^{\top}1 = 0)$. Hệ quả là, vectơ $1$ là trong không gian hạch (nullspace) của $L$.
Các nhận xét: $1$. Với unoriented phiên bản của ma trận liên thuộc (incidence matrix) (xem Định nghĩa 20.8), nó có thể được được hiển thị rằng
$$BB^{\top}= D + A.$$
$2$. Như được điểm ra bởi Evangelos Chatzipantazis, Mệnh đề 20.2 trong mà ma trận liên thuộc (incidence matrix) $B^{\sigma}$ được thay thế bởi ma trận liên thuộc (incidence matrix) $B$ của bất kỳ tùy ý được trực tiếp đồ thị $G$ thực hiện không đúng. bài toán là rằng như vậy các đồ thị có thể có cả hai các cạnh $(v_{i}, v_{j})$ và $(v_{j}, v_{i})$ giữa hai phân biệt các nút $v_{i}$ và $v_{j}$, và hệ quả là, tích vô hướng (inner product) $b_{i} \cdot  b_{j} = -2$ thay vì của $-1$. đơn giản phản ví dụ được cho bởi được trực tiếp đồ thị với ba các đỉnh và bốn các cạnh có ma trận liên thuộc (incidence matrix) được cho bởi
$$B = \begin{pmatrix} 1 & -1 & 0 & -1 \\ -1 & 1 & -1 & 0 \\ 0 & 0 & 1 & 1 \end{pmatrix} .$$
Ta có
$$BB^{\top}= \begin{pmatrix} 3 & -2 & -1 \\ -2 & 3 & -1 \\ 1 & 1 & 2 \end{pmatrix} \neq \begin{pmatrix} 3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} = D -A.$$
$$--$$
Tự nhiên tổng quát hóa của khái niệm của toán tử Laplace của đồ thị (graph Laplacian) đến được trọng số các đồ thị là điều này:

> **Định nghĩa 20.16.** Cho trước bất kỳ được trọng số đồ thị $G = (V, W)$ với $V = {v_{1}, \dots  , v_{m}}$,
(chưa chuẩn hóa) toán tử Laplace của đồ thị (graph Laplacian) L(G) của $G$ được định nghĩa bởi
$$L(G) = D(G) -W,$$
Ở đâu D(G) $= diag(d_{1}, \dots  , d_{m})$ là ma trận bậc (degree matrix) của $G$ (ma trận đường chéo (diagonal matrix)), với
$$d_{i} = \sum_{j=1}^{m}  w_{i j}.$$
Như thông thường, trừ khi confusion phát sinh, ta viết $D$ thay vì của D(G) và $L$ thay vì của L(G).

<!-- PAGE 725 -->
$$\mathbb{R}^{V} \mathbb{R}^{V}$$
Toán tử Laplace của đồ thị (graph Laplacian) có thể được interpreted như ánh xạ tuyến tính (linear map) từ đến chính nó. Với mọi $x \in$, ta có
$$(Lx)_{i} = \sum_{j\sim i}  w_{ij}(x_{i} -x_{j}).$$
Nó là rõ ràng từ phương trình $L = D$ - $W$ rằng mỗi hàng của $L$ các tổng đến $0$, do đó vectơ $1$ là không gian hạch (nullspace) của $L$, nhưng nó là ít hơn hiển nhiên rằng $L$ là nửa xác định dương (positive semidefinite). Một cách để chứng minh nó là đến tổng quát hóa slightly khái niệm của ma trận liên thuộc (incidence matrix).

> **Định nghĩa 20.17.** Cho trước được trọng số đồ thị $G = (V, W)$, với $V = {v_{1}, \dots  , v_{m}}$, nếu ${e_{1}, \dots , e_{n}}$ là các cạnh của underlying đồ thị của $G$ (nhắc lại rằng ${v_{i}, v_{j}}$ là cạnh của điều này đồ thị khi và chỉ khi $w_{ij} > 0)$, với mọi được định hướng đồ thị $G^{\sigma}$ thu được bởi cho định hướng đến underlying đồ thị của $G$, ma trận liên thuộc (incidence matrix) $B^{\sigma}$ của $G^{\sigma}$ là ma trận cỡ $m \times  n$ có các phần tử (entries) $b_{i j}$ được cho bởi
$$\sqrt$$
$$+\overline{w}_{ij}if s(e_{j}) = v_{i}$$
$$\sqrt$$
$$$$
$$b_{i j} =-\overline{w}_{ij}if t(e_{j}) = v_{i}$$
$$0otherwise.$$
$$$$
Ví dụ, cho trước trọng số ma trận
$$W = \begin{pmatrix} 0 & 3 & 6 & 3 \\ 3 & 0 & 0 & 3 \\ 6 & 0 & 0 & 3 \\ 3 & 3 & 3 & 0 \end{pmatrix} ,$$
Ma trận liên thuộc (incidence matrix) $B$ tương ứng với định hướng của underlying đồ thị của $W$ ở đâu cạnh $(i, j)$ được định hướng một cách dương khi và chỉ khi $i < j$ là
$$B = \begin{pmatrix} 1.7321 & 2.4495 & 1.7321 & 0 & 0 \\ -1.7321 & 0 & 0 & 1.7321 & 0 \\ 0 & -2.4495 & 0 & 0 & 1.7321 \\ 0 & 0 & 1.7321 & 1.7321 & 1.7321 \end{pmatrix} .$$
$$---$$
Độc giả nên kiểm chứng rằng $BB^{\top} = D$ - $W$. Điều này là đúng nói chung, xem Mệnh đề 20.3. Nó là dễ để xem rằng Mệnh đề 20.1 áp dụng đến underlying đồ thị của $G$. Với mọi được định hướng đồ thị $G^{\sigma}$ thu được từ underlying đồ thị của $G$, hạng (rank) của ma trận liên thuộc (incidence matrix) $B^{\sigma}$ bằng m-c, ở đâu $c$ là số của liên thông các thành phần của underlying đồ thị của $G$, và ta có $(B^{\sigma})^{\top}1 = 0$. Ta cũng có sau đây phiên bản của Mệnh đề 20.2 có chứng minh là ngay lập tức được điều chỉnh.

> **Mệnh đề 20.3.** Cho trước bất kỳ được trọng số đồ thị $G = (V, W)$ với $V = {v_{1}, \dots  , v_{m}}$, nếu $B^{\sigma}$ là ma trận liên thuộc (incidence matrix) của bất kỳ được định hướng đồ thị $G^{\sigma}$ thu được từ underlying đồ thị của $G$ và $D$ là ma trận bậc (degree matrix) của $G$, thì
$$B^{\sigma}(B^{\sigma})^{\top}= D -W = L.$$

<!-- PAGE 726 -->
Hệ quả là, $B^{\sigma}(B^{\sigma})^{\top}$ là độc lập của định hướng của underlying đồ thị của $G$ và $L = D$ - $W$ là đối xứng và nửa xác định dương (positive semidefinite); nghĩa là, các trị riêng (eigenvalues) của $L = D$ - $W$ là thực và không âm. Một cái khác cách để chứng minh rằng $L$ là nửa xác định dương (positive semidefinite) là đến tính giá trị dạng toàn phương (quadratic form) $x^{\top}Lx$.

> **Mệnh đề 20.4.** Với mọi $m \times  m$ ma trận đối xứng (symmetric matrix) $W = (w_{ij})$, nếu ta cho $L = D$ - $W$
$$where D is the degree matrix associated with W (that is, d_{i} = \sum_{j}  m=1 w_{ij}), then we have$$
$$x^{\top}Lx = \frac{1}{2} \sum_{i,j=1}^{m}  w_{i j}(x_{i} -x_{j})^{2}for all x \in \mathbb{R}^{m}.$$
Hệ quả là, $x^{\top}Lx$ không phụ thuộc vào đường chéo các phần tử (entries) trong $W$, và nếu $w_{i j} \ge 0$ với mọi $i, j \in {1, \dots  , m}$, thì $L$ là nửa xác định dương (positive semidefinite).

*Chứng minh.* Ta có
$$x^{\top}Lx = x^{\top}Dx -x^{\top}Wx$$
$$= \sum_{i=1}^{m}  d_{i}x_{i}^{2} - \sum_{i,j=1}^{m}  w_{i j}x_{i}x_{j}$$
$$!$$
$$= \frac{1}{2} \sum_{i=1}^{m}  d_{i}x_{i}^{2} -2 \sum_{i,j=1}^{m}  w_{i j}x_{i}x_{j} + \sum_{i=1}^{m}  d_{i}x_{i}^{2}$$
$$= \frac{1}{2} \sum_{i,j=1}^{m}  w_{i j}(x_{i} -x_{j})^{2}.$$
Hiển nhiên, đại lượng trên vế phải không phụ thuộc vào đường chéo các phần tử (entries) trong $W$, và nếu $w_{i j} \ge 0$ với mọi $i, j$, thì điều này đại lượng là không âm. Mệnh đề 20.4 ngay lập tức suy ra sau đây các sự kiện: Với mọi được trọng số đồ thị $G = (V, W), 1$. các trị riêng (eigenvalues) $0 = \lambda_{1}  \le \lambda_{2}  \le \dots  \le \lambda_{m}$ của $L$ là thực và không âm, và có một cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors) của $L. 2$. nhỏ nhất trị riêng (eigenvalue) $\lambda_{1}$ của $L$ bằng $0$, và $1$ là tương ứng vectơ riêng (eigenvector). Hóa ra là số chiều của không gian hạch (nullspace) của $L$ (không gian riêng (eigenspace) của $0)$ bằng số của liên thông các thành phần của underlying đồ thị của $G$.
