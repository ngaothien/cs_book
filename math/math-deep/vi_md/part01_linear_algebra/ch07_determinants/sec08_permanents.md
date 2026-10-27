# Permanents


<!-- PAGE 247 -->
Và vì $B$ là ma trận có các phần tử (entries) là các đa thức trong K[X], nó làm cho nghĩa đến nhân trên
$$e$$
Trái bởi $B$ và ta thu được
$$e$$
$$Be \cdot  B \cdot \begin{pmatrix} e_{1} \\ e_{2} \\ \vdots \\ e_{n} \end{pmatrix} = (BB e) \cdot \begin{pmatrix} e_{1} \\ e_{2} \\ \vdots \\ e_{n} \end{pmatrix} = P_{A}I \cdot \begin{pmatrix} e_{1} \\ e_{2} \\ \vdots \\ e_{n} \end{pmatrix} = Be \cdot \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix} ;$$
Rằng là,
$$P_{A} \cdot  e_{j} = 0,j = 1, \dots  , n,$$
Mà chứng tỏ rằng $P_{A}(f) = 0$, như đã khẳng định. Nếu $K$ là trường, thì đa thức đặc trưng (characteristic polynomial) của ánh xạ tuyến tính (linear map) $f$: $E \to E$ là độc lập của cơ sở (basis) $(e_{1}, \dots  , e_{n})$ được chọn trong $E$. để chứng minh điều này, nhận thấy rằng ma trận của $f$ trên một cái khác cơ sở (basis) sẽ là của tạo thành $P^{-1}$ AP, với một số inverible ma trận $P$, và thì
$$\det(XI -P^{-1} AP) = \det(XP^{-1} IP -P^{-1} AP)$$
$$= \det(P^{-1} (XI -A)P)$$
$$= \det(P^{-1} ) \det(XI -A) \det(P)$$
$$= \det(XI -A).$$
Vì vậy, đa thức đặc trưng (characteristic polynomial) của ánh xạ tuyến tính (linear map) là nội tại đến $f$, và nó được ký hiệu bởi $P_{f}$. các không điểm (các nghiệm) của đa thức đặc trưng (characteristic polynomial) của ánh xạ tuyến tính (linear map) $f$ được gọi là các trị riêng (eigenvalues) của $f$. Chúng đóng quan trọng vai trò trong lý thuyết và các ứng dụng. Ta sẽ đến quay lại đến điều này topic sau này.

## 7.8 Permanents

Nhắc lại rằng tường minh công thức cho định thức (determinant) của một ma trận cỡ $n \times  n$ là
$$\det(A) = \sum_{\pi\in Sn}  \epsilon (\pi )a_{\pi(1) 1} \cdots  a_{\pi(n)n}.$$
Nếu ta bỏ dấu $\epsilon (\pi$) của mọi hoán vị từ ở trên công thức, ta thu được đại lượng đã biết như permanent:
$$per(A) = \sum_{\pi\in Sn}  a_{\pi(1) 1} \cdots  a_{\pi(n)n}.$$
Permanents và các định thức đã là investigated như early như $1812$ bởi Cauchy. Nó là rõ ràng từ ở trên định nghĩa rằng permanent là đa tuyến tính đối xứng tạo thành. Ta cũng có
$$per(A) = per(A^{\top}),$$

<!-- PAGE 248 -->
Và sau đây unsigned phiên bản của Laplace expansion công thức:
$$per(A) = a_{i1}per(A_{i1}) + \cdots  + a_{i j}per(A_{i j}) + \cdots  + a_{i n}per(A_{i n}),$$
Cho $i = 1, \dots  , n$. Tuy nhiên, unlike các định thức mà có rõ ràng hình học interpretation như được dấu các thể tích, permanents thực hiện không có bất kỳ tự nhiên hình học interpretation. Hơn nữa, các định thức có thể được evaluated efficiently, ví dụ bằng cách sử dụng conversion đến hàng rút gọn bậc thang tạo thành, nhưng việc tính toán permanent là khó. Permanents turn ra đến có khác nhau combinatorial interpretations. Một của các phần tử này là theo perfect matchings của bipartite các đồ thị mà ta bây giờ thảo luận. Xem Định nghĩa 20.5 cho định nghĩa của undirected đồ thị. bipartite (undirected) đồ thị $G = (V, E)$ là đồ thị có tập hợp của các nút $V$ có thể được được phân hoạch vào hai khác rỗng rời nhau các tập con $V_{1}$ và $V_{2}$, sao cho mọi cạnh $e \in E$ có một endpoint trong $V_{1}$ và một endpoint trong $V_{2}$. ví dụ của bipartite đồ thị với $14$ các nút được hiển thị trong Hình 7.3; của nó các nút được phân hoạch vào hai các tập hợp ${x_{1}, x_{2}, x_{3}, x_{4}, x_{5}, x_{6}, x_{7}}$ và ${y_{1}, y_{2}, y_{3}, y_{4}, y_{5}, y_{6}, y_{7}}$.
$$y_{1}y_{2}y_{3}y_{4}y_{5}y_{6}y_{7}$$
$$x_{1}x_{2}x_{3}x_{4}x_{5}x_{6}x_{7}$$
$$Figure 7.3: A bipartite graph G.$$
Matching trong đồ thị $G = (V, E)$ (bipartite hoặc không) là tập hợp $M$ của đôi một non-adjacent các cạnh, mà có nghĩa là không có hai các cạnh trong $M$ share chung/phổ biến đỉnh. perfect matching là matching sao cho mọi nút trong $V$ là incident đến một số cạnh trong matching $M$ (mọi nút trong $V$ là endpoint của một số cạnh trong $M)$. Hình 7.4 chỉ ra perfect matching (trong đỏ) trong bipartite đồ thị $G$. Hiển nhiên, perfect matching trong bipartite đồ thị có thể tồn tại chỉ nếu tập hợp của nó của các nút có phân hoạch trong hai các khối của bằng nhau kích thước, nói ${x_{1}, \dots  , x_{m}}$ và ${y_{1}, \dots  , y_{m}}$. Thì có một song ánh giữa perfect matchings và các song ánh $\pi$: ${x_{1}, \dots  , x_{m}} \to {y_{1}, \dots  , y_{m}}$ sao cho $\pi (x_{i}) = y_{j}$ khi và chỉ khi có một cạnh giữa $x_{i}$ và $y_{j}$. Bây giờ mọi bipartite đồ thị $G$ với phân hoạch của của nó các nút vào hai các tập hợp của bằng nhau kích thước như ở trên được biểu diễn bởi một ma trận cỡ $m \times  m$ $A = (a_{ij})$ sao cho $a_{ij} = 1$ khi và chỉ khi có một cạnh giữa $x_{i}$ và $y_{j}$, và $a_{ij} = 0$ ngược lại. Bằng cách sử dụng interpretation của perfect matchings như
