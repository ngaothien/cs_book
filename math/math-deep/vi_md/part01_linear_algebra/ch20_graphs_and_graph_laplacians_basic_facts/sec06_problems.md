# Các bài tập


<!-- PAGE 734 -->
$\bullet$ Được chuẩn hóa toán tử Laplace của đồ thị (graph Laplacian). $\bullet$ Spectral đồ thị lý thuyết. $\bullet$ Đồ thị clustering bằng cách sử dụng được chuẩn hóa cuts.

## 20.6 Các bài tập

Bài toán 20.1. Tìm chưa chuẩn hóa Laplacian của đồ thị biểu diễn tam giác và của đồ thị biểu diễn square.
Bài toán 20.2. Xét đầy đủ đồ thị $K_{m}$ trên $m \ge 2$ các nút.
$(1)$ Chứng minh rằng được chuẩn hóa Laplacian $L_{sym}$ của $K$ là
$$L_{sym} = \begin{pmatrix} 1 & -1/(m -1) & \dots & -1/(m -1) & -1/(m -1) \\ -1/(m -1) & 1 & \dots & -1/(m -1) & -1/(m -1) \\ \vdots & \ddots & \ddots & \ddots & \vdots \\ -1/(m -1) & -1/(m -1) & \dots & 1 & -1/(m -1) \\ -1/(m -1) & -1/(m -1) & \dots & -1/(m -1) & 1 \end{pmatrix} .$$
$(2)$ Chứng minh rằng đa thức đặc trưng (characteristic polynomial) của $L_{sym}$ là
$$\lambda  -11/(m -1)\dots 1/(m -1)1/(m -1)$$
$$1/(m -1)\lambda  -1\dots 1/(m -1)1/(m -1)$$
$$m-1$$
$$\vdots \ddots \ddots \ddots \vdots$$
$$= \lambda \begin{pmatrix} m \\ \lambda  - \\ m -1 \end{pmatrix} .$$
$$1/(m -1)1/(m -1)\dots \lambda  -11/(m -1)$$
$$1/(m -1)1/(m -1)\dots 1/(m -1)\lambda  -1$$
Hint. Thứ nhất trừ cột thứ hai từ thứ nhất, nhân tử $\lambda$ - $m/(m$ - $1)$, và thì cộng hàng thứ nhất đến thứ hai. Repeat điều này process. Bạn sẽ kết thúc/cuối lên với định thức (determinant)
$$\lambda  -1/(m -1)1$$
$$.$$
$$1/(m -1)\lambda  -1$$
Bài toán 20.3. Xét đầy đủ bipartite đồ thị $K_{m,n}$ trên $m + n \ge 3$ các nút, với các cạnh giữa mỗi của thứ nhất $m \ge 1$ các nút đến mỗi của cuối cùng $n \ge 1$ các nút. Chứng minh rằng các trị riêng (eigenvalues) của được chuẩn hóa Laplacian $L_{sym}$ của $K_{m,n}$ là $0, 1$ với bội (multiplicity) $m + n$ - $2$, và $2$.
Bài toán 20.4. Cho $G$ là đồ thị với tập hợp của các nút $V$ với $m \ge 2$ các phần tử, mà không có isolated các nút, và cho $L_{sym} = D^{-1/2}LD^{-1/2}$ là của nó được chuẩn hóa Laplacian (với $L$ của nó chưa chuẩn hóa Laplacian).

<!-- PAGE 735 -->
$$\mathbb{R}^{V}$$
$(1)$ Với mọi $y \in$, xét Rayleigh tỉ số
$$R = \frac{y^{\top}L_{sym} y}{y^{\top}y} .$$
Chứng minh rằng nếu $x = D^{-1/2}y$, thì
$$\sum_{u\sim v}  (x(u) -x(v))^{2}$$
$$R = \frac{x^{\top}Lx}{(D^{1/2}x)^{\top}D^{1/2}x} = \sum_{v}  d_{v}x(v)^{2}.$$
$(2)$ Chứng minh rằng thứ hai trị riêng (eigenvalue) $\nu_{2}$ của $L_{sym}$ được cho bởi
$$\sum_{u\sim v}  (x(u) -x(v))^{2}$$
$$\nu_{2}  =\min.$$
$$1\top Dx=0,x\neq 0 \sum_{v}  d_{v}x(v)^{2}$$
$(3)$ Chứng minh rằng lớn nhất trị riêng (eigenvalue) $\nu_{m}$ của $L_{sym}$ được cho bởi
$$\sum_{u\sim v}  (x(u) -x(v))^{2}$$
$$\nu_{m}  = \max.$$
$$x\neq 0 \sum_{v}  d_{v}x(v)^{2}$$
Bài toán 20.5. Cho $G$ là đồ thị với tập hợp của các nút $V$ với $m \ge 2$ các phần tử, mà không có isolated các nút. Nếu $0 = \nu_{1}  \le \nu_{1}  \le \dots  \le \nu_{m}$ là các trị riêng (eigenvalues) của $L_{sym}$, chứng minh các tính chất sau đây:
$(1)$ Ta có $\nu_{1}  + \nu_{2}  + \cdots  + \nu_{m}  = m$.
$(2)$ Ta có $\nu_{2}  \le m/(m -1)$, với đẳng thức giữ khi và chỉ khi $G = K_{m}$, đầy đủ đồ thị trên $m$ các nút.
$(3)$ Ta có $\nu_{m}  \ge m/(m$ - $1)$.
$(4)$ Nếu $G$ là không đầy đủ đồ thị, thì $\nu_{2}  \le 1$ Hint. Nếu và $b$ là nonadjacent các nút, xét hàm $x$ cho trước bởi
$$d_{b}if v = a$$
$$$$
$$$$
$$x(v) =-d_{a}if v = b$$
$$0if v \neq  a, b,$$
$$$$
Và sử dụng Bài toán 20.4(2).

<!-- PAGE 736 -->
$(5)$ Chứng minh rằng $\nu_{m}  \le 2$. Chứng minh rằng $\nu_{m}  = 2$ khi và chỉ khi underlying đồ thị của $G$ chứa không tầm thường liên thông bipartite thành phần. Hint. Sử dụng Bài toán 20.4(3).
$(6)$ Chứng minh rằng nếu $G$ là liên thông, thì $\nu_{2}  > 0$.
Bài toán 20.6. Cho $G$ là đồ thị với tập hợp của các nút $V$ với $m \ge 2$ các phần tử, mà không có
$$isolated nodes. Let vol(G) = \sum_{v}  \in V d_{v} and let$$
$$\overline{x} = \sum_{v}  \frac{d_{v}x(v)}{vol(G)} .$$
Chứng minh rằng
$$\sum_{u\sim v}  (x(u) -x(v))^{2}$$
$$\nu_{2}  = \min .$$
$$x\neq 0 \sum_{v}  d_{v}(x(v) -\overline{x})^{2}$$
Bài toán 20.7. Cho $G$ là liên thông bipartite đồ thị. Chứng minh rằng nếu $\nu$ là trị riêng (eigenvalue) của $L_{sym}$, thì $2$ - $\nu$ là cũng trị riêng (eigenvalue) của $L_{sym}$.
Bài toán 20.8. Chứng minh Mệnh đề 20.7.
