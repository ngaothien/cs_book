# Grassmann-Plücker's Các phương trình và Grassmannians


<!-- PAGE 1264 -->

## 34.9 Grassmann-Pl¨ucker’s Các phương trình và

$$⊛$$
$$Grassmannian Manifolds$$
Ta suy ra lập luận được điều chỉnh từ Bourbaki $[25]$ (Chương III, §11, Mục $13)$. Cho $E$ là không gian vectơ (vector space) của số chiều $n$, cho $(e_{1}, \dots  , e_{n})$ là cơ sở (basis) của $E$, và cho $(e_{1}^{*}, \dots  , e_{n}^{*})$
$$p$$
$$be its dual basis.Our objective is to determine whether a nonzero vector⌟ z \in \bigwedge  E is$$
Phân rã được. Theo Mệnh đề 34.27, vectơ $z$ là phân rã được $iff(u^{*} z) \wedge z = 0$ với mọi
$$p-1 p-1$$
$$u^{*}\in \bigwedge  E^{*}. We can let u^{*}range over a basis of \bigwedge  E^{*}, and then the conditions are$$
$$(e_{H}^{*} ⌟z) \wedge z = 0$$
$$⌟p+1 E$$
$$for all H \subseteq {1, \dots  , n}, with |H| = p -1. Since (e_{H}^{*} z) \wedge z \in \bigwedge  , this is equivalent to$$
$$\langle e_{J}^{*}, (e_{H}^{*} ⌟z) \wedge z\rangle = 0$$
Với mọi $H, J \subseteq {1, \dots  , n}$, với |H| $= p$ - $1$ và |J| $= p + 1$. Thì, với mọi I, I' $\subseteq {1, \dots  , n}$ với |I| $=$ |I'| $= p$, Các công thức $(2)$ và $(4)$ của Mệnh đề 34.18 chỉ ra rằng
$$\langle e_{J}^{*}, (e_{H}^{*} ⌟e_{I}) \wedge e_{I'}\rangle = 0,$$
Trừ khi tồn tại một $i \in {1, \dots  , n}$ sao cho
$$I -H = {i},J -I'= {i}.$$
Trong trường hợp này, $I = H \cup {i}$ và I' $= J -{i}$, và bằng cách sử dụng Các công thức $(2)$ và $(4)$ của Mệnh đề 34.18, ta có $\langle e_{J}^{*}, (e_{H}^{*}$ ⌟ $e_{H\cup {i}}) \wedge e_{J-{i}}\rangle = \langle e_{J}^{*}, \rho_{{i},H} e_{i} \wedge e_{J-{i}}\rangle = \langle e_{J}^{*}, \rho_{{i},H} \rho_{{i},J-{i}} e_{J}\rangle = \rho_{{i},H} \rho_{{i},J-{i}}$. Nếu ta cho
$$\epsilon_{i,J,H}  = \rho_{{i},H} \rho_{{i},J-{i}} ,$$
Ta có $\epsilon_{i,J,H}  = +1$ nếu tính chẵn lẻ của số của $j \in J$ sao cho $j < i$ là cùng như tính chẵn lẻ của số của $h \in H$ sao cho $h < i$, và $\epsilon_{i,J,H}  = -1$ ngược lại. Cuối cùng ta thu được kết quả sau tiêu chuẩn theo toàn phương các phương trình (Pl¨ucker’s các phương trình) cho decomposability của thay phiên tenxơ.
$$p E$$
$$Proposition 34.29. (Grassmann-Pl¨ucker’s Equations) For z = \sum_{I}  \lambda_{I} e_{I} \in \bigwedge  , the con-$$
Ditions cho $z \neq  0$ là phân rã được là
$$\sum_{i\in J-H}  \epsilon_{i,J,H} \lambda_{H\cup {i}} \lambda_{J-{i}}  = 0,$$
Với $\epsilon_{i,J,H}  = \rho_{{i},H} \rho_{{i},J-{i}}$, với mọi $H, J \subseteq {1, \dots  , n}$ sao cho |H| $= p -1$, |J| $= p + 1$, và tất cả $i \in J$ - $H$.

<!-- PAGE 1265 -->
Bằng cách sử dụng ở trên tiêu chuẩn, nó là tốt bài tập đến reprove rằng nếu dim(E) $= n$, thì mọi
$$tensor in \bigwedge  n-1(E) is decomposable. We already proved this fact as a corollary of Proposition$$
34.23.
$$p E$$
$$Given any z = \sum_{I}  \lambda_{I} e_{I} \in \bigwedge  where \dim(E) = n, the family of scalars (\lambda_{I} ) (with$$
$I = {i_{1} < \cdots  < i_{p}} \subseteq {1, \dots  , n}$ được liệt kê trong tăng thứ tự) được gọi là Pl¨ucker các tọa độ của z. Grassmann-Pl¨ucker’s các phương trình cho cần và đủ các điều kiện với mọi khác không $z$ là phân rã được. Ví dụ, khi dim(E) $= n = 4$ và $p = 2$, các phương trình này rút gọn đến đơn lẻ phương trình
$$\lambda_{12} \lambda_{34}  -\lambda_{13} \lambda_{24}  + \lambda_{14} \lambda_{23}  = 0.$$
Tuy nhiên, nó nên được lưu ý rằng các phương trình cho trước theo Mệnh đề 34.29 là không độc lập nói chung. Ta là bây giờ trong position để chứng minh rằng Grassmannian G(p, $n)$ có thể được được nhúng trong
$$\mathbb{RP}(_{p}^{n})^{-1}$$
Không gian xạ ảnh (projective space), Với mọi $n \ge 1$ và bất kỳ $k$ với $1 \le p \le n$, nhắc lại rằng Grassmannian G(p, $n)$ là
$$\mathbb{R}^{n}$$
Tập hợp của tất cả tuyến tính $p$ chiều các không gian con của (cũng được gọi là p-planes). Bất kỳ $p$ chiều
$$\mathbb{R}^{n}  \mathbb{R}^{n}$$
Không gian con $U$ của được sinh (spanned) bởi $p$ các vectơ độc lập tuyến tính (linearly independent) $u_{1}, \dots  , u_{p}$ trong; viết $U = span(u_{1}, \dots  , u_{k})$. Theo Mệnh đề 34.8, $(u_{1}, \dots  , u_{p})$ là độc lập tuyến tính (linearly independent) khi và chỉ khi $u_{1}\wedge \cdots \wedge u_{p} \neq 0$. Nếu $(v_{1}, \dots  , v_{p})$ là bất kỳ khác các vectơ độc lập tuyến tính (linearly independent) sinh $U$, thì ta có
$$v_{j} = \sum_{i=1}^{p}  a_{ij}u_{i},1 \le j \le p,$$
Với một số $a_{ij} \in \mathbb{R}$, và theo Mệnh đề 34.2
$$v_{1} \wedge \cdots  \wedge v_{p} = \det(A) u_{1} \wedge \cdots  \wedge u_{p},$$
$$\mathbb{RP}(_{p}^{n})^{-1}$$
Ở đâu $A = (a_{ij})$. Hệ quả là, ta có thể định nghĩa ánh xạ $i_{G}$: G(p, $n) \to$ sao cho với mọi k-plane $U$, với mọi cơ sở (basis) $(u_{1}, \dots  , u_{p})$ của $U$,
$$i_{G}(U) = [u_{1} \wedge \cdots  \wedge u_{p}],$$
$$\mathbb{RP}(_{p}^{n})^{-1} \mathbb{R}(_{p}^{n})$$
Điểm của cho trước bởi một chiều không gian con của được sinh (spanned) bởi $u_{1} \wedge \cdots \wedge u_{p}$.
$$\mathbb{RP}(_{p}^{n})^{-1}$$

> **Mệnh đề 34.30.** ánh xạ $i_{G}$: G(p, $n) \to$ là đơn ánh (injective).

*Chứng minh.* Cho $U$ và $V$ là bất kỳ hai p-planes và giả sử rằng $i_{G}(U) = i_{G}(V$). Điều này có nghĩa là có một cơ sở (basis) $(u_{1}, \dots  , u_{p})$ của $U$ và cơ sở (basis) $(v_{1}, \dots  , v_{p})$ của $V$ sao cho
$$v_{1} \wedge \cdots  \wedge v_{p} = c u_{1} \wedge \cdots  \wedge u_{p}$$

<!-- PAGE 1266 -->
$$\mathbb{R}   \mathbb{R}^{n}$$
Với một số khác không $c \in$. ở trên suy ra rằng nhỏ nhất các không gian con $W$ và W' của
$$p p$$
$$such that u_{1} \wedge \cdots  \wedge u_{p} \in \bigwedge  W and v_{1} \wedge \cdots  \wedge v_{p} \in \bigwedge_{1}  W' are identical, so W = W' . By$$
Hệ quả 34.26, điều này nhỏ nhất không gian con $W$ có cả hai $(u , \dots  , u_{p})$ và $(v_{1}, \dots  , v_{p})$ như các cơ sở, do đó $v_{j}$ là các tổ hợp tuyến tính của $u_{i}$ (và vice-versa), và $U = V$.
$$p\mathbb{R}^{n}$$
$$Since any nonzero z \in \bigwedge  can be uniquely written as$$
$$z = \sum_{I}  \lambda_{I} e_{I}$$
$$\mathbb{RP}(_{p}^{n})^{-1}$$
Theo của nó Pl¨ucker các tọa độ $(\lambda_{I}$), mọi điểm của được định nghĩa bởi Pl¨ucker
$$\mathbb{RP}(_{p}^{n})^{-1}$$
Các tọa độ $(\lambda_{I}$) được quan điểm như thuần nhất các tọa độ. các điểm của tương ứng với một chiều các không gian liên kết với phân rã được thay phiên p-tensors là các điểm có các tọa độ thỏa mãn Grassmann-Pl¨ucker’s các phương trình của Mệnh đề 34.29.
$$\mathbb{RP}(_{p}^{n})^{-1}$$
Vì vậy, ánh xạ $i_{G}$ embeds Grassmannian G(p, $n)$ như đại số variety trong được định nghĩa bởi các phương trình của bậc $2$. Ta có thể thay thế trường $\mathbb{R}$ bởi $\mathbb{C}$ trong ở trên lập luận và ta thu được phép nhúng (embedding) của
$$\mathbb{CP}(_{p}^{n})^{-1}$$
Phức Grassmannian $G_{C}(p, n)$ như đại số variety trong được định nghĩa bởi các phương trình của bậc $2$. Đặc biệt, nếu $n = 4$ và $p = 2$, phương trình
$$\lambda_{12} \lambda_{34}  -\lambda_{13} \lambda_{24}  + \lambda_{14} \lambda_{23}  = 0$$
$$\mathbb{CP}^{5}$$
Là thuần nhất phương trình của mặt bậc hai (quadric) trong đã biết như Klein mặt bậc hai (quadric). các điểm trên điều này mặt bậc hai (quadric) là trong tương ứng một-một (bijection) với các đường thẳng trong $\mathbb{CP}^{3}$. Ở đó là cũng đơn giản đại số tiêu chuẩn đến decide liệu nhỏ nhất các không gian con $U$ và $V$ liên kết với hai khác không phân rã được các vectơ $u_{1} \wedge \cdots  \wedge u_{p}$ và $v_{1} \wedge \cdots  \wedge v_{q}$ có không tầm thường giao.

> **Mệnh đề 34.31.** Cho $E$ là bất kỳ $n$ chiều không gian vectơ (vector space) trên trường $K$, và cho $U$ và $V$ là nhỏ nhất các không gian con của $E$ liên kết với hai khác không phân rã được các vectơ
$$p q$$
$$u = u_{1} \wedge \cdots  \wedge u_{p} \in \bigwedge  U and v = v_{1} \wedge \cdots  \wedge v_{q} \in \bigwedge  V . The following properties hold:$$
$(1)$ Ta có $U \cap V = (0)$ khi và chỉ khi $u \wedge v \neq  0$.
$(2)$ Nếu $U \cap V = (0)$, thì $U + V$ là least không gian con liên kết với $u \wedge v$.

*Chứng minh.* Giả sử $U \cap V = (0)$. Ta biết theo Hệ quả 34.26 rằng $(u_{1}, \dots  , u_{p})$ là cơ sở (basis) của $U$ và $(v_{1}, \dots  , v_{q})$ là cơ sở (basis) của $V$. Vì $U \cap V = (0), (u_{1}, \dots  , u_{p}, v_{1}, \dots  , v_{q})$ là cơ sở (basis) của $U +V$, và theo Mệnh đề 34.8, ta có
$$u \wedge v = u_{1} \wedge \cdots  \wedge u_{p} \wedge v_{1} \wedge \cdots  \wedge v_{q} \neq  0.$$
Điều này cũng chứng minh $(2)$.
