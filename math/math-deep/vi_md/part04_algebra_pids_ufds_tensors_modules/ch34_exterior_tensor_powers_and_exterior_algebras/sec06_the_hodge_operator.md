# Hodge *-Toán tử


<!-- PAGE 1247 -->
$$Proposition 34.14. When E is finite dimensional, the maps \mu : \bigwedge  n(E^{*}) \longrightarrow Alt^{n}(E; K)$$
Được cảm sinh bởi tuyến tính các mở rộng của các ánh xạ cho trước bởi
$$\mu (v_{1}^{*} \wedge \cdots  \wedge v_{n}^{*})(u_{1}, \dots  , u_{n}) = \det(v_{j}^{*}(u_{i}))$$
$$yield a canonical isomorphism of algebras \mu : \bigwedge  (E^{*}) \longrightarrow Alt(E), where the multiplication in$$
Alt(E) được định nghĩa bởi các ánh xạ $\wedge$: $Alt^{m}(E; K) \times  Alt^{n}(E; K) \longrightarrow Alt^{m+n}(E; K)$, với
$$(f \wedge g)(u_{1}, \dots  , u_{m+n}) = \sum_{shuffle(}  sgn(\sigma ) f(u_{\sigma(1)}, \dots  , u_{\sigma(m)})g(u_{\sigma(m+1)}, \dots  , u_{\sigma(m+n)}),$$
$$\sigma \in m,n)$$
Ở đâu shuffle(m, $n)$ bao gồm của tất cả $(m$, n)-“shuffles,” rằng là, các hoán vị $\sigma$ của ${1, \dots  m+n}$ sao cho $\sigma (1) < \cdots  < \sigma (m)$ và $\sigma (m + 1) < \cdots  < \sigma (m + n)$.
$$Remark: The algebra \bigwedge  (E) is a graded algebra. Given two graded algebras E and F, we$$
Có thể tạo mới tích tenxơ (tensor product) $E \otimes F$, ở đâu $E \otimes F$ bằng $E \otimes F$ như không gian vectơ (vector space),
$$b b$$
Nhưng với skew-commutative phép nhân cho trước bởi
$$(a \otimes b) \wedge (c \otimes d) = (-1)^{deg(b)deg(c)}(ac) \otimes (bd),$$
Ở đâu $a \in E^{m}, b \in F^{p} , c \in E^{n}, d \in F^{q}$. Thì, nó có thể được được hiển thị rằng
$$^ \oplus  \sim ^\otimes ^$$
$$(EF)=(E)(F).$$
$$b$$

## 34.6 Hodge *-Toán tử

Trong thứ tự để định nghĩa tổng quát hóa của Laplacian rằng áp dụng đến vi phân các dạng trên Riemannian đa tạp (manifold), ta cần để định nghĩa các đẳng cấu
$$kn-k$$
$$^V \longrightarrow ^V,$$
Với mọi Euclidean không gian vectơ (vector space) $V$ có số chiều $n$ và bất kỳ $k$, với $0 \le k \le n$. Nếu $\langle$ -, $-\rangle$
$$k$$
$$denotes the inner product on V , we define an inner product on \bigwedge  V , denoted \langle -, -\rangle_{\wedge} , by$$
Đặt
$$\langle u_{1} \wedge \cdots  \wedge u_{k}, v_{1} \wedge \cdots  \wedge v_{k}\rangle_{\wedge} = \det(\langle u_{i}, v_{j}\rangle ),$$
Với mọi $u_{i}, v_{i} \in V$, và mở rộng $\langle$ -, $-\rangle_{\wedge}$ bởi tính song tuyến tính.
$$k$$
$$It is easy to show that if (e_{1}, \dots  , e_{n}) is an orthonormal basis of V , then the basis of \bigwedge  V$$
Bao gồm của $e_{I}$ (ở đâu $I = {i_{1}, \dots  , i_{k}}$, với $1 \le i_{1} < \cdots  < i_{k} \le n)$ là trực chuẩn
$$k$$
$$basis of \bigwedge  V . Since the inner product on V induces an inner product on V_{*} V^{*} (recall that$$
$$\langle \omega_{1} , \omega_{2} \rangle = \langle \omega_{1}^{\sharp} , \omega_{2}^{\sharp} \rangle , for all \omega_{1} , \omega_{2}  \in V^{*} ), we also get an inner product on \bigwedge  k .$$

<!-- PAGE 1248 -->

> **Định nghĩa 34.6.** định hướng của không gian vectơ (vector space) $V$ có số chiều $n$ được cho bởi lựa chọn của một số cơ sở (basis) $(e_{1}, \dots  , e_{n})$. Ta nói rằng cơ sở (basis) $(u_{1}, \dots  , u_{n})$ của $V$ là một cách dương được định hướng khi và chỉ khi $det(u_{1}, \dots  , u_{n}) > 0$ (ở đâu $det(u_{1}, \dots  , u_{n})$ ký hiệu định thức (determinant) của ma trận có cột thứ $j$ bao gồm của các tọa độ của $u_{j}$ trên cơ sở (basis) $(e_{1}, \dots  , e_{n}))$, ngược lại nó là một cách âm được định hướng. được định hướng không gian vectơ (vector space) là không gian vectơ (vector space) $V$ cùng với định hướng của $V$. Nếu $V$ được định hướng bởi cơ sở (basis) $(e_{1}, \dots  , e_{n})$, thì $V^{*}$ được định hướng bởi đối ngẫu (dual) cơ sở (basis) $(e_{1}^{*}, \dots  , e_{n}^{*})$. Nếu $\sigma$ là bất kỳ hoán vị của ${1, \dots  , n}$, thì cơ sở (basis) $(e_{\sigma(1)}, \dots  , e_{\sigma(n)})$ có dương định hướng khi và chỉ khi signature $sgn(\sigma$) của hoán vị $\sigma$ là chẵn/ngay cả. Nếu $V$ được định hướng không gian vectơ (vector space) có số chiều $n$, thì ta có thể định nghĩa tuyến tính đẳng cấu
$$kn-k$$
$$*:^V \to ^V,$$
Được gọi là Hodge *-toán tử. sự tồn tại của điều này toán tử là guaranteed bởi sau đây mệnh đề.

> **Mệnh đề 34.15.** Cho $V$ là bất kỳ được định hướng Euclidean không gian vectơ (vector space) có định hướng là cho trước
$$k$$
$$by some chosen orthonormal basis (en, \dots  , e_{n}-k ). For any alternating tensor \alpha  \in \bigwedge  V , there$$
$$is a unique alternating tensor *\alpha  \in \bigwedge^{1}  V such that$$
$$\alpha  \wedge \beta  = \langle *\alpha , \beta \rangle_{\wedge} e_{1} \wedge \cdots  \wedge e_{n}$$
$$n-k$$
$$for all \beta  \in \bigwedge  V . The alternating tensor *\alpha  is independent of the choice of the positive$$
Cơ sở trực chuẩn (orthonormal basis) $(e_{1}, \dots  , e_{n})$.
$$n n$$
$$Proof. Since \bigwedge  V has dimension 1,k  the alternating tensor e_{1} \wedge \cdots  \wedge n-k e_{n} is an basis  of \bigwedge  V .$$
$$It follows that for any fixed \alpha  \in \bigwedge  V , the linear map \lambda_{\alpha}  from \bigwedge  V to \bigwedge  V given by$$
$$\lambda_{\alpha} (\beta ) = \alpha  \wedge \beta$$
Là của tạo thành
$$\lambda_{\alpha} (\beta ) = f_{\alpha}(\beta ) e_{1} \wedge \cdots  \wedge e_{n}$$
$$for some linear form  f_{\alpha} \in \begin{pmatrix} n-k V^{*} \\ aunique \end{pmatrix} \bigwedge  . But then, by the duality induced by the inner product$$
$$\langle -, -\rangle on \bigwedge  n-kV , there is   vector *\alpha  \in \bigwedge  n-kV such that$$
$$n-k$$
$$f_{\lambda}(\beta ) = \langle *\alpha , \beta \rangle_{\wedge} for all \beta  \in \bigwedge  V ,$$
Mà suy ra rằng
$$\alpha  \wedge \beta  = \lambda_{\alpha} (\beta ) = f_{\alpha}(\beta ) e_{1} \wedge \cdots  \wedge e_{n} = \langle *\alpha , \beta \rangle_{\wedge} e_{1} \wedge \cdots  \wedge e_{n},$$
Như đã khẳng định. Nếu $(e_{1}', \dots  , e_{n}')$ là bất kỳ khác một cách dương được định hướng cơ sở trực chuẩn (orthonormal basis), theo Mệnh đề 34.2, $e_{1}' \wedge \cdots  \wedge e_{n}' =$ det(P) $e_{1} \wedge \cdots  \wedge e_{n} = e_{1} \wedge \cdots  \wedge e_{n}$, vì det(P) $= 1$ ở đâu $P$ là chuyển cơ sở (change of basis) từ $(e_{1}, \dots  , e_{n})$ đến $(e_{1}', \dots  , e_{n}')$ và cả hai các cơ sở là một cách dương được định hướng.

<!-- PAGE 1249 -->
$$k n-k$$
$$Definition 34.7. The operator *from \bigwedge  V to \bigwedge  V defined by Proposition 34.15 is$$
Được gọi là Hodge *-toán tử. Obseve rằng Hodge *-toán tử là tuyến tính.
$$The Hodge *-operator is defined in terms of the orthonormal basis elements of \bigwedge  V as$$
Suy ra: Với mọi tăng dãy $(i_{1}, \dots  , i_{k})$ của các phần tử $i_{p} \in {1, \dots  , n}$, nếu $(j_{1}, \dots  , j_{n-k})$ là tăng dãy của các phần tử $j_{q} \in {1, \dots  , n}$ sao cho
$${i_{1}, \dots  , i_{k}} \cup {j_{1}, \dots  , j_{n-k}} = {1, \dots  , n},$$
Thì
$$*(e_{i1} \wedge \cdots  \wedge e_{ik}) = sign(i_{1}, \dots  i_{k}, j_{1}, \dots  , j_{n-k}) e_{j1} \wedge \cdots  \wedge e_{jn-k}.$$
Đặc biệt, cho $k = 0$ và $k = n$, ta có
$$*(1)=e_{1} \wedge \cdots  \wedge e_{n}$$
$$*(e_{1} \wedge \cdots  \wedge e_{n})=1.$$
Ví dụ, nếu $n = 3$, ta có
$$*e_{1} = e_{2} \wedge e_{3}$$
$$*e_{2} = -e_{1} \wedge e_{3}$$
$$*e_{3} = e_{1} \wedge e_{2}$$
$$*(e_{1} \wedge e_{2}) = e_{3}$$
$$*(e_{1} \wedge e_{3}) = -e_{2}$$
$$*(e_{2} \wedge e_{3}) = e_{1}.$$
$$The Hodge *-operators *: \bigwedge  Vk  \to \bigwedge  n-Vk  induce a linear map *: \bigwedge  (V ) \to \bigwedge  (V ). We$$
$$also have Hodge *-operators *: \bigwedge^{k}  V^{*} \to \bigwedge^{n-k}  V^{*} .$$
$$The following proposition shows that the linear map *: \bigwedge  (V ) \to \bigwedge  (V ) is an isomorphism.$$

> **Mệnh đề 34.16.** Nếu $V$ là bất kỳ được định hướng không gian vectơ (vector space) có số chiều $n$, với mọi $k$ với $0 \le k \le n$, ta có
$(i)$ ** $= (-id)^{k(n-k)}$.
$$k$$
$$(ii) \langle x, y\rangle_{\wedge} = *(x \wedge *y) = *(y \wedge *x), for all x, y \in \bigwedge  V .$$

*Chứng minh.* $(1)$ Cho $(e_{i})_{i}^{n}$ là cơ sở trực chuẩn (orthonormal basis) của $V$. Nó là đủ để kiểm tra đồng nhất thức trên cơ sở (basis) các phần tử. $We^{=1}$ có
$$*(e_{i1} \wedge \cdots  \wedge e_{ik}) = sign(i_{1}, \dots  i_{k}, j_{1}, \dots  , j_{n-k}) e_{j1} \wedge \cdots  \wedge e_{jn-k}$$

<!-- PAGE 1250 -->
Và $**(e_{i1} \wedge \cdots  \wedge e_{ik}) = sign(i_{1}, \dots  i_{k}, j_{1}, \dots  , j_{n-k}) *(e_{j1} \wedge \cdots  \wedge e_{jn-k})$
$$= sign(i_{1}, \dots  i_{k}, j_{1}, \dots  , j_{n-k}) sign(j_{1}, \dots  , j_{n-k}, i_{1}, \dots  i_{k}) e_{i1} \wedge \cdots  \wedge e_{ik}.$$
Nó là dễ để xem rằng
$$sign(i_{1}, \dots  i_{k}, j_{1}, \dots  , j_{n-k}) sign(j_{1}, \dots  , j_{n-k}, i_{1}, \dots  i_{k}) = (-1)^{k(n-k)},$$
Mà cho ta
$$**(e_{i1} \wedge \cdots  \wedge e_{ik}) = (-1)^{k(n-k)}e_{i1} \wedge \cdots  \wedge e_{ik},$$
Như đã khẳng định.
(ii) Các phần tử này các đồng nhất thức là dễ dàng đã kiểm tra trên cơ sở (basis) các phần tử; xem Jost $[104]$, Chương $2$, Bổ đề 2.1.1. Đặc biệt cho
$$k$$
$$x = e_{i1} \wedge \cdots  \wedge e_{ik},y = e_{ij} \wedge \cdots  \wedge e_{ij},x, y \in ^V,$$
Ở đâu $(e_{i})_{i=1}^{n}$ là cơ sở trực chuẩn (orthonormal basis) của $V$. Nếu $x \neq  y, \langle x, y\rangle_{\wedge} = 0$ vì tồn tại một $e_{ip}$ của $x$ không bằng bất kỳ $e_{jq}$ của $y$ bởi orthonormality của cơ sở (basis), điều này có nghĩa là $p^{th}$ hàng của $(\langle e_{il}, e_{js}\rangle$) bao gồm hoàn toàn của các không. Cũng $x \neq  y$ suy ra rằng $y \wedge$ *x $= 0$ vì
$$*x = sign(i_{1}, \dots  i_{k}, l_{1}, \dots  , l_{n-k})e_{l1} \wedge \cdots  \wedge e_{\ln-k},$$
Ở đâu $e_{ls}$ là cùng như một số $e_{p}$ trong $y$. đồng dạng lập luận chỉ ra rằng nếu $x \neq  y, x \wedge$ *y $= 0$. Do đó bây giờ giả sử $x = y$. Thì
$$*(e_{i1} \wedge \cdots  \wedge e_{ik} \wedge *(e_{i1} \wedge \cdots  \wedge e_{ik})) = *(e_{1} \wedge e_{2} \cdots  \wedge e_{n})$$
$$= 1 = \langle x, x\rangle_{\wedge} .$$
Nó là khả dĩ/có thể đến biểu diễn *(1) theo bất kỳ cơ sở (basis) (không nhất thiết trực chuẩn) của $V$.

> **Mệnh đề 34.17.** Nếu $V$ là bất kỳ hữu hạn chiều được định hướng không gian vectơ (vector space), với mọi cơ sở (basis) $(v_{!}, \dots  , v_{n})$ của $V$, ta có
$$*(1) = \frac{1}{pdet(\langle v_{i}, v_{j}\rangle )} v_{1} \wedge \cdots  \wedge v_{n}.$$

*Chứng minh.* Nếu $(e_{1}, \dots  , e_{n})$ là cơ sở trực chuẩn (orthonormal basis) của $V$ và $(v_{1}, \dots  , v_{n})$ là bất kỳ khác cơ sở (basis) của $V$, thì
$$\langle v_{1} \wedge \cdots  \wedge v_{n}, v_{1} \wedge \cdots  \wedge v_{n}\rangle_{\wedge} = \det(\langle v_{i}, v_{j}\rangle ),$$
Và vì
$$v_{1} \wedge \cdots  \wedge v_{n} = \det(A) e_{1} \wedge \cdots  \wedge e_{n}$$
