# Hạt nhân (kernel) PCA


<!-- PAGE 1961 -->
Cũng, nếu $\kappa$: $X \times  X \to \mathbb{R}$ là thực đối xứng xác định dương (SPD) hạt nhân (kernel), thì ta xem ngay lập tức rằng Định lý 53.8 nghiệm đúng với $H_{0}$ thực Không gian Euclid (Euclidean space) và $H$ thực Không gian Hilbert (Hilbert space). ⊛ Nhận xét: Nếu $X = G$, ở đâu $G$ là một cách địa phương compắc nhóm, thì hàm $p: G \to \mathbb{C}$ (không nhất thiết liên tục) là nửa xác định dương (positive semidefinite) nếu với mọi $s_{1}, \dots  , s_{n} \in G$ và tất cả $\xi_{1} , \dots  , \xi_{n}  \in \mathbb{C}$, ta có
$$\sum_{j,k=1}^{n}  p(s_{j}^{-1} s_{k})\xi_{k} \overline{\xi}_{j} \ge 0.$$
Do đó nếu ta định nghĩa $\kappa$: $G \times  G \to \mathbb{C}$ bởi
$$\kappa (s, t) = p(t^{-1}s),$$
Thì $\kappa$ là nhân xác định dương (positive definite kernel) trên $G$. Nếu $p$ là liên tục, thì nó là đã biết rằng $p$ phát sinh từ unita biểu diễn $U$: $G \to$ U(H) của nhóm $G$ trong Không gian Hilbert (Hilbert space) $H$ với tích vô hướng (inner product) $\langle$ -, $-\rangle$ (đồng cấu với nhất định tính liên tục tính chất), trong nghĩa rằng tồn tại một vectơ $x_{0} \in H$ sao cho
$$p(s) = \langle U(s)(x_{0}), x_{0}\rangle ,for all s \in G.$$
Vì U(s) là unita các toán tử trên $H$,
$$p(t^{-1}s) = \langle U(t^{-1}s)(x_{0}), x_{0}\rangle = \langle U(t^{-1})(U(s)(x_{0})), x_{0}\rangle$$
$$= \langle U(t)^{*}(U(s)(x_{0})), x_{0}\rangle = \langle U(s)(x_{0}), U(t)(x_{0})\rangle ,$$
Mà chỉ ra rằng
$$\kappa (s, t) = \langle U(s)(x_{0}), U(t)(x_{0})\rangle ,$$
Do đó ánh xạ $\phi$: $G \to H$ cho trước bởi
$$\phi (s) = U(s)(x_{0})$$
Là đặc trưng (feature) ánh xạ vào đặc trưng (feature) không gian $H$. định lý này là do Gelfand và Raikov $(1943)$. chứng minh của Định lý 53.8 là về cơ bản đồng nhất đến phần của Godement’s chứng minh của ở trên kết quả về correspondence giữa các hàm của dương loại/kiểu và unita các biểu diễn; xem Helgason $[93]$, Chương IV, Định lý 1.5. Định lý 53.8 là little nhiều hơn/thêm tổng quát vì nó thực hiện không giả sử rằng $X$ là nhóm, nhưng khi $G$ là nhóm, đặc trưng (feature) ánh xạ phát sinh từ unita biểu diễn.

## 53.4 Hạt nhân (kernel) PCA

Như ứng dụng của hạt nhân (kernel) các hàm, ta thảo luận tổng quát hóa của phương pháp của phân tích thành phần chính (PCA) (PCA). Giả sử ta có tập hợp của dữ liệu $S = {x_{1}, \dots  , x_{n}}$ trong một số input không gian $\mathcal{X}$, và pretend rằng ta có phép nhúng (embedding) $\phi$: $\mathcal{X} \to F$ của $\mathcal{X}$ trong (thực) đặc trưng (feature) không gian $(F, \langle$ -, $-\rangle$), nhưng rằng ta chỉ có access đến hạt nhân (kernel) hàm $\kappa (x, y) = \langle \phi (x), \phi (y)\rangle$. Ta sẽ like đến thực hiện PCA giải tích/phân tích trên tập hợp $\phi (S) = {\phi (x_{1}), \dots  , \phi (x_{n})}$. Có hai obstacles:

<!-- PAGE 1962 -->
$(1)$ Ta cần đến tâm dữ liệu và tính trong các tích của các cặp của được tâm dữ liệu. Chính xác hơn, nếu trọng tâm của $\phi (S)$ là
$$\mu  = \frac{1}{n} (\phi (x_{1}) + \cdots  + \phi (x_{n})),$$
Thì ta cần để tính trong các tích $\langle \phi (x)$ - $\mu , \phi (y)$ - $\mu \rangle$.
$$\mathbb{R}^{d}$$
$(2)$ Ta giả sử rằng $F =$ với tiêu chuẩn Euclidean tích vô hướng (inner product) và rằng dữ liệu các điểm $\phi (x_{i})$ được biểu diễn như các vectơ hàng $X_{i}$ của một ma trận cỡ $n \times  d$ $X$ (như nó là thông lệ). Thì trong các tích $\kappa (x_{i}, x_{j}) = \langle \phi (x_{i}), \phi (x_{j})\rangle$ được cho bởi hạt nhân (kernel) ma trận $K = XX^{\top}$. Là biết rằng với biểu diễn này, trong biểu thức $\langle \phi (x_{i}), \phi (x_{j})\rangle , \phi (x_{i})$ là $d$ chiều vectơ cột (column vector), trong khi $\phi (x_{i}) = X_{i}^{\top}$. Tuy nhiên, thành phần thứ $j$ $(Y_{k})_{j}$ của chính thành phần $Y_{k}$ (được quan điểm như $n$ chiều vectơ cột (column vector)) được cho bởi phép chiếu của $X_{j} = X_{j} -\mu$ lên hướng $u_{k}$ (quan điểm $\mu$ như
$$b$$
$d$ chiều vectơ hàng (row vector)), mà là unit vectơ riêng (eigenvector) của ma trận $(X$ - $\mu )^{\top}(X$ - $\mu$) (ở đâu $X = X$ - $\mu$ là ma trận có hàng thứ $j$ là $X_{j} = X_{j}$ - $\mu$), được cho bởi trong
$$b b$$
Tích
$$\langle X_{j} -\mu , u_{k}\rangle = (Y_{k})_{j};$$
Xem Định nghĩa 23.2 và Định lý 23.11. bài toán là rằng ta biết những gì ma trận $(X$ - $\mu )(X$ - $\mu )^{\top}$ là từ $(1)$, bởi vì nó có thể được được biểu diễn theo $K$, nhưng ta không’t biết những gì $(X$ - $\mu )^{\top}(X$ - $\mu$) là bởi vì ta không’t có access đến $X = X$ - $\mu$.
$$b$$
Cả hai difficulties là dễ dàng overcome. Cho $(1)$ ta có
$$*+$$
$$\langle \phi (x) -\mu , \phi (y) -\mu \rangle =\phi (x) - \frac{1}{n} \sum_{k=1}^{n}  \phi (x_{k}), \phi (y) - \frac{1}{n} \sum_{k=1}^{n}  \phi (x_{k})$$
$$= \kappa (x, y) - \frac{1}{n} \sum_{i=1}^{n}  \kappa (x, x_{i}) - \frac{1}{n} \sum_{j=1}^{n}  \kappa (x_{j}, y) + \frac{1}{n^{2}} \sum_{i,j=1}^{n}  \kappa (x_{i}, x_{j}).$$
Cho $(2)$, nếu $K$ là hạt nhân (kernel) ma trận $K = (\kappa (x_{i}, x_{j}))$, thì hạt nhân (kernel) ma trận $K$ tương ứng
$$b$$
Đến hạt nhân (kernel) hàm $\kappa$ cho trước bởi
$$b$$
$$\kappa (x, y) = \langle \phi (x) -\mu , \phi (y) -\mu \rangle$$
$$b$$
Có thể được được biểu diễn theo $K$. Cho $1$ là vectơ cột (column vector) (có số chiều $n)$ có các phần tử (entries) là tất cả $1$. Thì $11^{\top}$ là ma trận cỡ $n \times  n$ có các phần tử (entries) là tất cả $1$. Nếu $A$ là một ma trận cỡ $n \times  n$, thì $1^{\top}A$ là vectơ hàng (row vector) bao gồm của các tổng của các cột của $A$, A1 là vectơ cột (column vector) bao gồm của các tổng của các hàng của $A$, và $1^{\top}A1$ là tổng của tất cả các phần tử (entries) trong $A$. Thì nó là dễ để xem rằng hạt nhân (kernel) ma trận tương ứng với hạt nhân (kernel) hàm $\kappa$ được cho bởi
$$b$$
$$Kb = K - \frac{1}{n} 11^{\top}K - \frac{1}{n} K11^{\top}+ \frac{1}{n^{2}} (1^{\top}K1)11^{\top}.$$

<!-- PAGE 1963 -->
Giả sử $X = X$ - $\mu$ có hạng (rank) $r$. Đến overcome thứ hai bài toán, lưu ý rằng nếu
$$b$$
$$X = V DU^{\top}$$
$$b$$
Là SVD cho $X$, thì
$$b$$
$$X^{\top}= UD^{\top}V^{\top}$$
$$b$$
Là SVD cho $X^{\top}$, và $r\times r$ ma trận con của $D^{\top}$ bao gồm của thứ nhất $r$ các hàng và $r$ các cột
$$b$$
Của $D^{\top}$ (và $D)$, là đường chéo $\Sigma_{r}$ ma trận bao gồm của các giá trị kỳ dị (singular values) $\sigma_{1}  \ge \cdots  \ge \sigma_{r}$ của $X$, do đó ta có thể biểu diễn ma trận $U_{r}$ bao gồm của thứ nhất $r$ các cột $u_{k}$ của $U$ theo ma trận cỡ $b$ $V_{r}$ bao gồm của thứ nhất $r$ các cột $v_{k}$ của $V (1 \le k \le r)$ như
$$U_{r} =X^{\top}V_{r}\Sigma_{r}^{-1}  .$$
$$b$$
Hơn nữa, $\sigma_{1}^{2}  \ge \cdots  \ge \sigma_{r}^{2}$ là khác không các trị riêng (eigenvalues) của $K = XX^{\top}$, và các cột của
$$b b b$$
$V_{r}$ là tương ứng unit các vectơ riêng (eigenvectors) của $K$. Từ
$$b$$
$$U_{r} =X^{\top}V_{r}\Sigma_{r}^{-1}$$
$$b$$
Cột thứ $k$ $u_{k}$ của $U_{r}$ (mà là unit vectơ riêng (eigenvector) của $X^{\top}X$ liên kết với trị riêng (eigenvalue)
$$bb$$
$\sigma_{k}^{2}$) được cho bởi
$$[$$
$$u_{k} = \sum_{i=1}^{n}  \sigma_{k}^{-1}  (v_{k})_{i} bX_{i}^{\top} = \sum_{i=1}^{n}  \sigma_{k}^{-1}  (v_{k})_{i}\phi (x_{i}),1 \le k \le r,$$
$$[$$
Do đó phép chiếu của $\phi (x)$ lên $u_{k}$ được cho bởi
$$*+$$
$$[[ [$$
$$\langle \phi (x), u_{k}\rangle =\phi (x), \sum_{i=1}^{n}  \sigma_{k}^{-1}  (v_{k})_{i}\phi (x_{i})$$
$$= \sum_{i=1}^{n}  \sigma_{k}^{-1}  (v_{k}) \bigoplus_{i}  \phi [(x), \phi [(x_{i})E= \sum_{i=1}^{n}  \sigma_{k}^{-1}  (v_{k})_{i}\kappa (x, x_{i}).$$
$$b$$
Vì vậy, thành phần thứ $j$ của chính thành phần $Y_{k}$ trong chính hướng $u_{k}$ được cho bởi
$$(Y_{k})_{j} = \langle X_{j} -\mu , u_{k}\rangle = \sum_{i=1}^{n}  \sigma_{k}^{-1}  (v_{k})_{i}\kappa b(x_{j}, x_{i}) = \sum_{i=1}^{n}  \sigma_{k}^{-1}  (v_{k})_{i} bK_{ij}.$$
Tổng quát hóa của hạt nhân (kernel) PCA đến tổng quát phép nhúng (embedding) $\phi$: $\mathcal{X} \to F$ của $\mathcal{X}$ trong (thực) đặc trưng (feature) không gian $(F, \langle$ -, $-\rangle$) (ở đâu $F$ là không bị thu hẹp là bằng nhau $to\mathbb{R}^{d})$ với hạt nhân (kernel) ma trận $K$ cho trước bởi
$$K_{ij} = \langle \phi (x_{i}), \phi (x_{j})\rangle ,$$
Đi như sau.
