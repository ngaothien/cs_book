# được trực tiếp Các đồ thị, Undirected Các đồ thị, được trọng số Các đồ thị


<!-- PAGE 716 -->
$R^{\top}R =$ I và tương ứng drawing được gọi là một trực giao drawing. điều kiện này cũng các quy tắc ra tầm thường drawings. Thì ta chứng minh chính định lý về đồ thị drawings (Định lý 21.2), mà về cơ bản nói rằng rằng ma trận $R$ của mong muốn đồ thị drawing là constituted bởi $n$ các vectơ riêng (eigenvectors) của $L$ liên kết với nhỏ nhất khác không $n$ các trị riêng (eigenvalues) của $L$. Ta cho số các ví dụ của đồ thị drawings, nhiều của mà là borrowed hoặc được điều chỉnh từ Spielman $[169]$.

## 20.1 được trực tiếp Các đồ thị, Undirected Các đồ thị, Liên thuộc

$$Matrices, Adjacency Matrices, Weighted Graphs$$

> **Định nghĩa 20.1.** được trực tiếp đồ thị là cặp $G = (V, E)$, ở đâu $V = {v_{1}, \dots  , v_{m}}$ là tập hợp của các nút hoặc các đỉnh, và $E \subseteq V \times  V$ là tập hợp của được thứ tự các cặp của phân biệt các nút (rằng là, các cặp $(u, v) \in V \times  V$ với $u \neq  v)$, được gọi là các cạnh. Cho trước bất kỳ cạnh $e = (u, v)$, ta cho s(e) $= u$ là source của $e$ và t(e) $= v$ là target của $e$.
Nhận xét: Vì cạnh là cặp $(u, v)$ với $u \neq  v$, self-loops là không được phép. Cũng, ở đó là nhiều nhất một cạnh từ nút $u$ đến nút $v$. Như vậy các đồ thị đôi khi được gọi là đơn giản các đồ thị. ví dụ của được trực tiếp đồ thị được hiển thị trong Hình 20.2.
$$e_{1}$$
$$v_{1}v_{2}$$
$$e_{5}$$
$$e_{2}e_{3}e_{4}$$
$$v_{5}$$
$$e_{6}$$
$$v_{3}v_{4}$$
$$\overline{e}_{7}$$
$$Figure 20.2: Graph G_{1}.$$

> **Định nghĩa 20.2.** Với mọi nút $v \in V$, bậc d(v) của $v$ là số của các cạnh để lại hoặc entering $v$:
$$d(v) = |{u \in V | (v, u) \in E or (u, v) \in E}|.$$
Ta abbreviate $d(v_{i})$ như $d_{i}$. ma trận bậc (degree matrix), D(G), là ma trận đường chéo (diagonal matrix)
$$D(G) = \mathrm{diag}(d_{1}, \dots  , d_{m}).$$

<!-- PAGE 717 -->
Ví dụ, cho đồ thị $G_{1}$, ta có
$$D(G_{1}) = \begin{pmatrix} 2 & 0 & 0 & 0 & 0 \\ 0 & 4 & 0 & 0 & 0 \\ 0 & 0 & 3 & 0 & 0 \\ 0 & 0 & 0 & 3 & 0 \\ 0 & 0 & 0 & 0 & 2 \end{pmatrix} .$$
Trừ khi confusion phát sinh, ta viết $D$ thay vì của D(G).

> **Định nghĩa 20.3.** Cho trước được trực tiếp đồ thị $G = (V, E)$, với mọi hai các nút $u, v \in V$, đường đi từ $u$ đến $v$ là dãy của các nút $(v_{0}, v_{1}, \dots  , v_{k})$ sao cho $v_{0} = u, v_{k} = v$, và $(v_{i}, v_{i+1})$ là cạnh trong $E$ với mọi $i$ với $0 \le i \le k$ - $1$. số nguyên $k$ là độ dài của đường đi. đường đi là đóng nếu $u = v$. đồ thị $G$ là một cách mạnh liên thông nếu với mọi hai phân biệt các nút $u, v \in V$, có một đường đi từ $u$ đến $v$ và có một đường đi từ $v$ đến $u$.
Nhận xét: thuật ngữ walk là thường được sử dụng thay vì của đường đi, word đường đi đang là reserved đến trường hợp ở đâu các nút $v_{i}$ là tất cả phân biệt, ngoại trừ rằng $v_{0} = v_{k}$ khi đường đi là đóng. nhị phân quan hệ trên $V \times  V$ được định nghĩa sao cho $u$ và $v$ là related khi và chỉ khi có một đường đi từ $u$ đến $v$ và có một đường đi từ $v$ đến $u$ là quan hệ tương đương (equivalence relation) có các lớp tương đương được gọi là một cách mạnh liên thông các thành phần của $G$.

> **Định nghĩa 20.4.** Cho trước được trực tiếp đồ thị $G = (V, E)$, với $V = {v_{1}, \dots  , v_{m}}$, nếu $E = {e_{1}, \dots  , e_{n}}$, thì ma trận liên thuộc (incidence matrix) B(G) của $G$ là ma trận cỡ $m \times  n$ có các phần tử (entries) $b_{i j}$ được cho bởi
$$+1if s(e_{j}) = v_{i}$$
$$$$
$$$$
$$b_{i j} =-1if t(e_{j}) = v_{i}$$
$$0otherwise.$$
$$$$
Ở đây là ma trận liên thuộc (incidence matrix) của đồ thị $G_{1}$:
$$B = \begin{pmatrix} 1 & 1 & 0 & 0 & 0 & 0 & 0 \\ -1 & 0 & -1 & -1 & 1 & 0 & 0 \\ 0 & -1 & 1 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 1 & 0 & -1 & -1 \\ 0 & 0 & 0 & 0 & 1 & 1 & 0 \end{pmatrix} .$$
$$-$$
Nhận thấy rằng mọi cột của ma trận liên thuộc (incidence matrix) chứa chính xác hai khác không các phần tử (entries), $+1$ và $-1$. Một lần nữa, trừ khi confusion phát sinh, ta viết $B$ thay vì của B(G). Khi được trực tiếp đồ thị có $m$ các nút $v_{1}, \dots  , v_{m}$ và $n$ các cạnh $e_{1}, \dots  , e_{n}$, vectơ $x \in \mathbb{R}^{m}$ có thể được được quan điểm như hàm $x: V \to \mathbb{R}$ assigning giá trị $x_{i}$ đến nút $v_{i}$. Dưới điều này
$$\mathbb{R}^{m}  \mathbb{R}^{V} \mathbb{R}^{n}$$
Interpretation, được quan điểm như. Tương tự, vectơ $y \in$ có thể được được quan điểm như hàm

<!-- PAGE 718 -->
$$a$$
$$v_{1}v_{2}$$
$$e$$
$$bcdv_{5}$$
$$f$$
$$v_{3}v_{4}$$
$$g$$
$$Figure 20.3: The undirected graph G_{2}.$$
Trong $\mathbb{R}^{E}$. Điều này điểm của quan điểm là thường hữu ích. Ví dụ, ma trận liên thuộc (incidence matrix) $B$ có thể được
$$\mathbb{R}^{E}  \mathbb{R}^{V}$$
Interpreted như ánh xạ tuyến tính (linear map) từ đến, biên (boundary) ánh xạ, và $B^{\top}$ có thể được interpreted
$$\mathbb{R}^{V}  \mathbb{R}^{E}$$
Như ánh xạ tuyến tính (linear map) từ đến, coboundary ánh xạ.
Nhận xét: Một số các tác giả adopt opposite quy ước của dấu trong định nghĩa ma trận liên thuộc (incidence matrix), mà có nghĩa là của chúng ma trận liên thuộc (incidence matrix) là $-B$. Undirected các đồ thị là thu được từ được trực tiếp các đồ thị bởi forgetting định hướng của các cạnh.

> **Định nghĩa 20.5.** đồ thị (hoặc undirected đồ thị) là cặp $G = (V, E)$, ở đâu $V = {v_{1}, \dots  , v_{m}}$ là tập hợp của các nút hoặc các đỉnh, và $E$ là tập hợp của two-element các tập con của $V$ (rằng là, các tập con ${u, v}$, với $u, v \in V$ và $u \neq  v)$, được gọi là các cạnh.
Nhận xét: Vì cạnh là tập hợp ${u, v}$, ta có $u \neq  v$, do đó self-loops là không được phép. Cũng, với mọi tập hợp của các nút ${u, v}$, ở đó là nhiều nhất một cạnh giữa $u$ và $v$. Như trong trường hợp của được trực tiếp các đồ thị, như vậy các đồ thị đôi khi được gọi là đơn giản các đồ thị. ví dụ của đồ thị được hiển thị trong Hình 20.3.

> **Định nghĩa 20.6.** Với mọi nút $v \in V$, bậc d(v) của $v$ là số của các cạnh incident đến $v$:
$$d(v) = |{u \in V | {u, v} \in E}|.$$
Ma trận bậc (degree matrix) D(G) (hoặc đơn giản, $D)$ được định nghĩa như trong Định nghĩa 20.2.

> **Định nghĩa 20.7.** Cho trước (undirected) đồ thị $G = (V, E)$, với mọi hai các nút $u, v \in V$, đường đi từ $u$ đến $v$ là dãy của các nút $(v_{0}, v_{1}, \dots  , v_{k})$ sao cho $v_{0} = u, v_{k} = v$, và ${v_{i}, v_{i+1}}$ là cạnh trong $E$ với mọi $i$ với $0 \le i \le k$ - $1$. số nguyên $k$ là độ dài của đường đi. đường đi là đóng nếu $u = v$. đồ thị $G$ là liên thông nếu với mọi hai phân biệt các nút $u, v \in V$, có một đường đi từ $u$ đến $v$.

<!-- PAGE 719 -->
Nhận xét: thuật ngữ walk hoặc dây chuyền/xích là thường được sử dụng thay vì của đường đi, word đường đi đang là reserved đến trường hợp ở đâu các nút $v_{i}$ là tất cả phân biệt, ngoại trừ rằng $v_{0} = v_{k}$ khi đường đi là đóng. nhị phân quan hệ trên $V \times V$ được định nghĩa sao cho $u$ và $v$ là related khi và chỉ khi có một đường đi từ $u$ đến $v$ là quan hệ tương đương (equivalence relation) có các lớp tương đương được gọi là liên thông các thành phần của $G$. khái niệm của ma trận liên thuộc (incidence matrix) cho undirected đồ thị là không như hữu ích như trong trường hợp của được trực tiếp các đồ thị

> **Định nghĩa 20.8.** Cho trước đồ thị $G = (V, E)$, với $V = {v_{1}, \dots  , v_{m}}$, nếu $E = {e_{1}, \dots  , e_{n}}$, thì ma trận liên thuộc (incidence matrix) B(G) của $G$ là ma trận cỡ $m \times  n$ có các phần tử (entries) $b_{i j}$ được cho bởi
$$($$
$$+1if e_{j} = {v_{i}, v_{k}} for some k$$
$$b_{i j} =$$
$$0otherwise.$$
Unlike trường hợp của được trực tiếp các đồ thị, các phần tử (entries) trong ma trận liên thuộc (incidence matrix) của đồ thị (undirected) là không âm. Ta thường viết $B$ thay vì của B(G).

> **Định nghĩa 20.9.** Nếu $G = (V, E)$ được trực tiếp hoặc undirected đồ thị, cho trước nút $u \in V$, bất kỳ nút $v \in V$ sao cho có một cạnh $(u, v)$ trong được trực tiếp trường hợp hoặc ${u, v}$ trong undirected trường hợp được gọi là kề nhau đến $u$, và ta thường sử dụng ký hiệu
$$u \sim v.$$
Nhận thấy rằng nhị phân quan hệ $\sim$ là đối xứng khi $G$ là undirected đồ thị, nhưng nói chung nó là không đối xứng khi $G$ được trực tiếp đồ thị. khái niệm của ma trận kề (adjacency matrix) là basically cùng cho được trực tiếp hoặc undirected các đồ thị.

> **Định nghĩa 20.10.** Cho trước được trực tiếp hoặc undirected đồ thị $G = (V, E)$, với $V = {v_{1}, \dots  , v_{m}}$, ma trận kề (adjacency matrix) (G) của $G$ là đối xứng $m \times  m$ ma trận $(a_{i j})$ sao cho
$(1)$ Nếu $G$ được trực tiếp, thì
$$($$
$$1if there is some edge (v_{i}, v_{j}) \in E or some edge (v_{j}, v_{i}) \in E$$
$$a_{i j} =$$
$$0otherwise.$$
$(2)$ Khác nếu $G$ là undirected, thì
$$($$
$$1if there is some edge {v_{i}, v_{j}} \in E$$
$$a_{i j} =$$
$$0otherwise.$$

<!-- PAGE 720 -->
Như thông thường, trừ khi confusion phát sinh, ta viết $A$ thay vì của (G). Ở đây là ma trận kề (adjacency matrix) của cả hai các đồ thị $G_{1}$ và $G_{2}$:
$$A = \begin{pmatrix} 0 & 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 1 & 1 \\ 1 & 1 & 0 & 1 & 0 \\ 0 & 1 & 1 & 0 & 1 \\ 0 & 1 & 0 & 1 & 0 \end{pmatrix} .$$
Nếu $G = (V, E)$ là undirected đồ thị, ma trận kề (adjacency matrix) $A$ của $G$ có thể được được quan điểm như
$$\mathbb{R}^{V}  \mathbb{R}^{V} \mathbb{R}^{m}$$
Ánh xạ tuyến tính (linear map) từ đến, sao cho với mọi $x \in$, ta có
$$(Ax)_{i} = \sum_{j\sim i}  x_{j};$$
Rằng là, giá trị của Ax tại $v_{i}$ là tổng của các giá trị của $x$ tại các nút $v_{j}$ kề nhau đến $v_{i}$. ma trận kề (adjacency matrix) có thể được được quan điểm như diffusion toán tử. Điều này nhận xét cho ta hình học
$$\mathbb{R}^{m}$$
Interpretation của những gì nó có nghĩa là cho vectơ $x \in$ là vectơ riêng (eigenvector) của $A$ liên kết với một số trị riêng (eigenvalue) $\lambda$; ta phải có
$$\lambda x_{i} = \sum_{j\sim i}  x_{j},i = 1, \dots  , m,$$
Mà có nghĩa là tổng của các giá trị của $x$ assigned đến các nút $v_{j}$ kề nhau đến $v_{i}$ bằng $\lambda$ lần giá trị của $x$ tại $v_{i}$.

> **Định nghĩa 20.11.** Cho trước bất kỳ undirected đồ thị $G = (V, E)$, định hướng của $G$ là hàm $\sigma$: $E \to V \times  V$ assigning source và target đến mọi cạnh trong $E$, mà có nghĩa là với mọi cạnh ${u, v} \in E$, hoặc $\sigma ({u, v}) = (u, v)$ hoặc $\sigma ({u, v}) = (v, u)$. được định hướng đồ thị $G^{\sigma}$ thu được từ $G$ bằng cách áp dụng định hướng $\sigma$ được trực tiếp đồ thị $G^{\sigma} = (V, E^{\sigma})$, với $E^{\sigma} = \sigma (E)$. Kết quả sau đây chỉ ra cách mà số của liên thông các thành phần của undirected đồ thị là related đến hạng (rank) của ma trận liên thuộc (incidence matrix) của bất kỳ được định hướng đồ thị thu được từ $G$.

> **Mệnh đề 20.1.** Cho $G = (V, E)$ là bất kỳ undirected đồ thị với $m$ các đỉnh, $n$ các cạnh, và $c$ liên thông các thành phần. Với mọi định hướng $\sigma$ của $G$, nếu $B$ là ma trận liên thuộc (incidence matrix) của được định hướng đồ thị $G^{\sigma}$, thì $c =$ dim(Ker $(B^{\top}))$, và $B$ có hạng (rank) $m$ - $c$. Hơn nữa, không gian hạch (nullspace) của $B^{\top}$ có cơ sở (basis) bao gồm của indicator các vectơ của liên thông các thành phần của $G$; nghĩa là, các vectơ $(z_{1}, \dots  , z_{m})$ sao cho $z_{j} = 1$ khi và chỉ khi $v_{j}$ là trong thành phần thứ $i$ $K_{i}$ của $G$, và $z_{j} = 0$ ngược lại.

*Chứng minh.* (Sau Godsil và Royle $[80]$, Mục 8.3). sự kiện rằng hạng (rank)(B) $= m$ - $c$ sẽ được chứng minh cuối cùng.
$$\mathbb{R}^{m}$$
Cho chúng ta chứng minh rằng hạt nhân (kernel) của $B^{\top}$ có số chiều $c$. vectơ $z \in$ thuộc đến hạt nhân (kernel) của $B^{\top}$ khi và chỉ khi $B^{\top}z = 0$ khi và chỉ khi $z^{\top}B = 0$. Xét theo định nghĩa của $B$, với mọi cạnh ${v_{i}, v_{j}}$

<!-- PAGE 721 -->
Của $G$, cột của $B$ tương ứng với được định hướng cạnh $\sigma ({v_{i}, v_{j}})$ có không các phần tử (entries) ngoại trừ cho $a +1$ và $a -1$ trong position $i$ và position $j$ hoặc vice-versa, do đó ta có
$$z_{i} = z_{j}.$$
Dễ quy nạp trên độ dài của đường đi chỉ ra rằng nếu có một đường đi từ $v_{i}$ đến $v_{j}$ trong $G$ (unoriented), thì $z_{i} = z_{j}$. Vì vậy, $z$ có hằng số giá trị trên bất kỳ liên thông thành phần của $G$. Suy ra rằng mọi vectơ $z \in$ Ker $(B^{\top})$ có thể được được viết một cách duy nhất như tổ hợp tuyến tính (linear combination)
$$z = \lambda_{1} z^{1}+ \cdots  + \lambda_{c} z^{c},$$
Ở đâu vectơ $z^{i}$ tương ứng với thứ $i$ liên thông thành phần $K_{i}$ của $G$ và được định nghĩa sao cho
$$($$
$$1iffv_{j} \in K_{i}$$
$$z_{j}^{i} =$$
$$0otherwise.$$
Điều này chỉ ra rằng dim(Ker $(B^{\top})) = c$, và rằng Ker $(B^{\top})$ có cơ sở (basis) bao gồm của indicator các vectơ. Vì $B^{\top}$ là một ma trận cỡ $n \times  m$, ta có
$$m = \dim(\mathrm{Ker} (B^{\top})) + \mathrm{rank}(B^{\top}),$$
Và vì ta chỉ được chứng minh rằng dim(Ker $(B^{\top})) = c$, ta thu được $rank(B^{\top}) = m$ - $c$. Vì $B$ và $B^{\top}$ có cùng hạng (rank), hạng (rank)(B) $= m$ - $c$, như đã khẳng định.

> **Định nghĩa 20.12.** Sau đây chung/phổ biến practice, ta ký hiệu bởi $1$ (cột) vectơ (có số chiều $m)$ có các thành phần là tất cả bằng $1$. Vì mọi cột của $B$ chứa đơn lẻ $+1$ và đơn lẻ $-1$, các hàng của $B^{\top}$ tổng đến không, mà có thể được biểu diễn dưới dạng
$$B^{\top}1 = 0.$$
Theo Mệnh đề 20.1, đồ thị $G$ là liên thông khi và chỉ khi $B$ có hạng (rank) m-1 khi và chỉ khi không gian hạch (nullspace) của $B^{\top}$ là một chiều không gian được sinh (spanned) bởi $1$. Trong nhiều các ứng dụng, khái niệm của đồ thị cần là suy rộng/tổng quát hóa đến capture trực quan ý tưởng rằng hai các nút $u$ và $v$ là linked với bậc của certainty (hoặc strength). Do đó, ta assign không âm trọng số $w_{i j}$ đến cạnh ${v_{i}, v_{j}}$; nhỏ hơn $w_{i j}$ là, weaker là link (hoặc sự đồng dạng) giữa $v_{i}$ và $v_{j}$, và greater $w_{i j}$ là, mạnh hơn là link (hoặc sự đồng dạng) giữa $v_{i}$ và $v_{j}$.

> **Định nghĩa 20.13.** được trọng số đồ thị là cặp $G = (V, W)$, ở đâu $V = {v_{1}, \dots  , v_{m}}$ là tập hợp của các nút hoặc các đỉnh, và $W$ là ma trận đối xứng (symmetric matrix) được gọi là trọng số ma trận, sao cho $w_{i j} \ge 0$ với mọi $i, j \in {1, \dots  , m}$, và $w_{i i} = 0$ cho $i = 1, \dots  , m$. Ta nói rằng tập hợp ${v_{i}, v_{j}}$ là cạnh khi và chỉ khi $w_{i j} > 0$. tương ứng (undirected) đồ thị $(V, E)$ với $E = {{v_{i}, v_{j}}$ | $w_{i j} > 0}$, được gọi là underlying đồ thị của $G$.

<!-- PAGE 722 -->
Nhận xét: Vì $w_{i i} = 0$, các phần tử này các đồ thị có không có self-loops. Ta có thể nghĩ của ma trận $W$ như suy rộng/tổng quát hóa ma trận kề (adjacency matrix). trường hợp ở đâu $w_{i j} \in {0, 1}$ là tương đương đến khái niệm của đồ thị như trong Định nghĩa 20.5. Ta có thể nghĩ của trọng số $w_{i j}$ của cạnh ${v_{i}, v_{j}}$ như bậc của sự đồng dạng (hoặc affinity) trong ảnh (image), hoặc chi phí trong network. ví dụ của được trọng số đồ thị được hiển thị trong Hình 20.4. thickness của cạnh tương ứng với magnitude của của nó trọng số.
$$Figure 20.4: A weighted graph.$$

> **Định nghĩa 20.14.** Cho trước được trọng số đồ thị $G = (V, W)$, với mọi nút $v_{i} \in V$, bậc $d(v_{i})$ của $v_{i}$ là tổng của các trọng số của các cạnh kề nhau đến $v_{i}$:
$$d(v_{i}) = \sum_{j=1}^{m}  w_{i j}.$$
Lưu ý rằng trong ở trên tổng, chỉ các nút $v_{j}$ sao cho có một cạnh ${v_{i}, v_{j}}$ có khác không contribution. Như vậy các nút được nói là kề nhau đến $v_{i}$, và ta viết $v_{i} \sim v_{j}$. ma trận bậc (degree matrix) D(G) (hoặc đơn giản, $D)$ được định nghĩa như trước, cụ thể là bởi D(G) $= diag(d(v_{1}), \dots  , d(v_{m}))$.
$$\mathbb{R}^{V} \mathbb{R}^{m}$$
Trọng số ma trận $W$ có thể được được quan điểm như ánh xạ tuyến tính (linear map) từ đến chính nó. Với mọi $x \in$, ta có
$$(Wx)_{i} = \sum_{j\sim i}  w_{ij}x_{j};$$
Rằng là, giá trị của Wx tại $v_{i}$ được trọng số tổng của các giá trị của $x$ tại các nút $v_{j}$ kề nhau đến $v_{i}$. Nhận thấy rằng W1 là (cột) vectơ $(d(v_{1}), \dots  , d(v_{m}))$ bao gồm của các bậc của các nút của đồ thị. Ta bây giờ định nghĩa hầu hết quan trọng khái niệm của điều này chương: Laplacian ma trận của đồ thị. Thực sự, như ta sẽ xem, nó đến trong một vài flavors.
