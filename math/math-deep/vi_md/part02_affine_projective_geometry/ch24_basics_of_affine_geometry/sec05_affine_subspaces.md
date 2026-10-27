# Afin Các không gian con


<!-- PAGE 821 -->
$$c$$
$$g_{1}$$
$$ab$$
$$c$$
$$g_{2}$$
$$ab$$
$$Figure 24.11: Barycenters, g_{1} =_{4}^{1} a +_{4}^{1} b +_{2}^{1} c,g_{2} = -a + b + c$$
$$\mathbb{A}\mathbb{A}^{2}$$
Là xác định tốt (well-defined) tổ hợp afin (affine combination). Thì, ta có thể định nghĩa đường cong $F$: $\to$ sao cho
$$F(t) = (1 -t)^{3}a + 3t(1 -t)^{2}b + 3t^{2}(1 -t) c + t^{3}d.$$
Như vậy đường cong được gọi là một B´ezier đường cong, và (, $b, c, d)$ được gọi là của nó control các điểm. Lưu ý rằng đường cong các đi qua qua và $d$, nhưng một cách tổng quát không qua $b$ và $c$. Nó có thể được sbown rằng bất kỳ điểm F(t) trên đường cong có thể được được xây dựng bằng cách sử dụng thuật toán performing afin nội suy các bước (de Casteljau thuật toán).

## 24.5 Afin Các không gian con

Trong tuyến tính đại số, (tuyến tính) không gian con có thể được được đặc trưng hóa như khác rỗng tập con của không gian vectơ (vector space) đóng dưới các tổ hợp tuyến tính. Trong các không gian afin, khái niệm tương ứng với khái niệm của (tuyến tính) không gian con là khái niệm của không gian con afin (affine subspace). Nó là tự nhiên để định nghĩa không gian con afin (affine subspace) như tập con của không gian afin (affine space) đóng dưới các tổ hợp afin.
$$\longrightarrow$$

> **Định nghĩa 24.3.** Cho trước không gian afin (affine space) $E, E , +$, tập con $V$ của $E$ là không gian con afin (affine subspace) (của $\longrightarrow$
$$E,E , +) if for every family of weighted points ((a_{i}, \lambda_{i} ))_{i\in I} in V such that \sum_{i}  \in I \lambda_{i}  = 1,$$
$$the barycenter \sum_{i}  \in I \lambda_{i} a_{i} belongs to V .$$
Không gian con afin (affine subspace) cũng được gọi là một phẳng bởi một số các tác giả. Theo Định nghĩa 24.3, rỗng tập hợp là một cách tầm thường không gian con afin (affine subspace), và mọi giao của afin các không gian con là không gian con afin (affine subspace).

<!-- PAGE 822 -->
$$\mathbb{R}^{2}$$
Như ví dụ, xét tập con $U$ của được định nghĩa bởi
$$\mathbb{R}^{2}$$
$$U =(x, y) \in | ax + by = c,$$
I.e., tập hợp của các nghiệm của phương trình
$$ax + by = c,$$
Ở đâu nó được giả sử rằng $a \neq  0$ hoặc $b \neq  0$. Cho trước bất kỳ $m$ các điểm $(x_{i}, y_{i}) \in U$ và bất kỳ $m$ các vô hướng $\lambda_{i}$ sao cho $\lambda_{1}  + \cdots  + \lambda_{m}  = 1$, ta khẳng định rằng
$$\sum_{i=1}^{m}  \lambda_{i} (x_{i}, y_{i}) \in U.$$
Thật vậy, $(x_{i}, y_{i}) \in U$ có nghĩa là
$$ax_{i} + by_{i} = c,$$
Và nếu ta nhân cả hai vế của phương trình này bởi $\lambda_{i}$ và cộng lên thu được $m$ các phương trình, ta thu được
$$\sum_{i=1}^{m}  (\lambda_{i} ax_{i} + \lambda_{i} by_{i}) = \sum_{i=1}^{m}  \lambda_{i} c,$$
Và vì $\lambda_{1}  + \cdots  + \lambda_{m}  = 1$, ta thu được
$$a \sum_{i=1}^{m}  \lambda_{i} x_{i}!+ b \sum_{i=1}^{m}  \lambda_{i} y_{i}!= \sum_{i=1}^{m}  \lambda_{i} !c = c,$$
Mà chỉ ra rằng
$$!$$
$$\sum_{i=1}^{m}  \lambda_{i} x_{i}, \sum_{i=1}^{m}  \lambda_{i} y_{i}= \sum_{i=1}^{m}  \lambda_{i} (x_{i}, y_{i}) \in U.$$
Do đó, $U$ là không gian con afin (affine subspace) của $\mathbb{A}^{2}$. Thực ra, nó là chỉ thông thường đường thẳng trong $\mathbb{A}^{2}$.
$$\mathbb{R}^{2}$$
Hóa ra là $U$ là closely related đến tập con của được định nghĩa bởi
$$\longrightarrow$$
$$U =(x, y) \in \mathbb{R}^{2}| ax + by = 0,$$
I.e., tập hợp của các nghiệm của thuần nhất phương trình
$$ax + by = 0$$
Thu được bằng cách đặt vế phải của ax $+$ bởi $= c$ đến không. Thật vậy, với mọi $m$ các vô hướng $\lambda_{i}$, cùng phép tính như ở trên cho ta rằng
$$\longrightarrow$$
$$\sum_{i=1}^{m}  \lambda_{i} (x_{i}, y_{i}) \in U ,$$

<!-- PAGE 823 -->
$$U$$
$$\longrightarrow$$
$$U$$
$$Figure 24.12: An affine line U and its direction.$$
Điều này time mà không có bất kỳ thu hẹp trên $\lambda_{i}$, vì vế phải của phương trình là
$$\longrightarrow  \longrightarrow$$
Null. Do đó, $U$ là không gian con của $\mathbb{R}^{2}$. Thực ra, $U$ là một chiều, và nó là chỉ thông thường đường thẳng trong $\mathbb{R}^{2}$. Điều này đường thẳng có thể được đồng nhất với đường thẳng chuyển qua gốc của $\mathbb{A}^{2}$, đường thẳng rằng là song song đến đường thẳng $U$ của phương trình ax $+$ bởi $= c$, như được minh họa trong Hình 24.12. Bây giờ, nếu $(x_{0}, y_{0})$ là bất kỳ điểm trong $U$, ta khẳng định rằng
$$\longrightarrow$$
$$U = (x_{0}, y_{0}) +U ,$$
Ở đâu
$$\longrightarrow n\longrightarrow o$$
$$(x_{0}, y_{0}) +U =(x_{0} + u_{1}, y_{0} + u_{2}) | (u_{1}, u_{2}) \in U.$$
$$\longrightarrow \longrightarrow$$
Thứ nhất, $(x_{0}, y_{0}) + U \subseteq U$, vì $ax_{0} + by_{0} = c$ và $au_{1} + bu_{2} = 0$ với mọi $(u_{1}, u_{2}) \in U$. Thứ hai, nếu $(x, y) \in U$, thì ax $+$ bởi $= c$, và vì ta cũng có $ax_{0} + by_{0} = c$, bởi phép trừ, ta thu được
$$a(x -x_{0}) + b(y -y_{0}) = 0,$$
$$\longrightarrow  \longrightarrow$$
Mà chỉ ra rằng $(x$ - $x_{0}, y$ - $y_{0}) \in U$, và do đó $(x, y) \in (x_{0}, y_{0}) + U$. Do đó, ta cũng có
$$\longrightarrow  \longrightarrow$$
$U \subseteq (x_{0}, y_{0}) + U$, và $U = (x_{0}, y_{0}) + U$. ở trên ví dụ chỉ ra rằng afin đường thẳng $U$ được định nghĩa bởi phương trình
$$ax + by = c$$
$$\longrightarrow$$
Là thu được bởi “translating” song song đường thẳng $U$ của phương trình
$$ax + by = 0$$

<!-- PAGE 824 -->
Chuyển qua gốc. Thực ra, cho trước bất kỳ điểm $(x_{0}, y_{0}) \in U$,
$$\longrightarrow$$
$$U = (x_{0}, y_{0}) +U .$$
Tổng quát hơn, nó là dễ để chứng minh sau đây sự kiện. Cho trước bất kỳ ma trận cỡ $m \times  n$ $A$ và bất kỳ
$$\mathbb{R}^{m} \mathbb{R}^{n}$$
Vectơ $b \in$, tập con $U$ của được định nghĩa bởi
$$\mathbb{R}^{n}$$
$$U = {x \in | Ax = b}$$
Là không gian con afin (affine subspace) của $\mathbb{A}^{n}$. Thực sự, nhận thấy rằng Ax $= b$ nên một cách thực được viết như $Ax^{\top} = b$, là consistent với của ta quy ước rằng các điểm được biểu diễn bởi các vectơ hàng. Ta có thể cũng sử dụng boldface ký hiệu cho các vectơ cột, trong mà trường hợp phương trình được viết như Ax $= b$. Cho sake của cực tiểu hóa lượng của ký hiệu, ta stick đến đơn giản hơn (vẫn chưa incorrect) ký hiệu Ax $= b$. Nếu ta xét tương ứng thuần nhất phương trình Ax $= 0$, tập hợp
$$\longrightarrow$$
$$U = {x \in \mathbb{R}^{n}| Ax = 0}$$
Là không gian con của $\mathbb{R}^{n}$, và với mọi $x_{0} \in U$, ta có
$$\longrightarrow$$
$$U = x_{0} +U .$$
Điều này là tổng quát tình huống. Afin các không gian con có thể được được đặc trưng hóa theo các không gian con của $\longrightarrow E$. Cho $V$ là khác rỗng tập con của $E$. Với mọi họ $(a_{1}, \dots  , a_{n})$ trong $V$, với mọi họ $(\lambda_{1} , \dots  , \lambda_{n}$) của các vô hướng, và với mọi điểm $a \in V$, nhận thấy rằng $x \in E$ cho trước bởi
$$x = a + \sum_{i=1}^{n}  \lambda_{i} \longrightarrow aa_{i}$$
Là tâm tỉ cự (barycenter) của họ của được trọng số các điểm
$$\begin{pmatrix} (a_{1}, \lambda_{1} ), \dots  , (a_{n}, \lambda_{n} ),a, 1 - & \lambda_{i} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \sum_{i=1}^{n}  ,$$
Vì
$$\sum_{i=1}^{n}  \lambda_{i}  + \begin{pmatrix} 1 - & \lambda_{i} \end{pmatrix} \sum_{i=1}^{n}  = 1.$$
$$\longrightarrow  \longrightarrow  \longrightarrow$$
Cho trước bất kỳ điểm $a \in E$ và bất kỳ tập con $V$ của $E$, cho $a + V$ ký hiệu sau đây tập con của $E$:
$$\longrightarrow n\longrightarrow o$$
$$a +V =a + v | v \in V.$$
$$\longrightarrow$$

> **Mệnh đề 24.2.** Cho $E, E , +$ là không gian afin (affine space).

<!-- PAGE 825 -->
$$\longrightarrow$$
$$EE$$
$$\longrightarrow$$
$$aV$$
$$\longrightarrow$$
$$V = a +V$$
$$Figure 24.13: An affine subspace V and its direction .$$
$(1) A$ khác rỗng tập con $V$ của $E$ là không gian con afin (affine subspace) khi và chỉ khi với mọi điểm $a \in V$, tập hợp
$$\longrightarrow \longrightarrow$$
$$V_{a} = {ax | x \in V }$$
$$\longrightarrow  \longrightarrow$$
Là không gian con của $E$. Hệ quả là, $V = a + V_{a}$. Hơn nữa,
$$\longrightarrow \longrightarrow$$
$$V = {xy | x, y \in V }$$
$$\longrightarrow  \longrightarrow  \longrightarrow  \longrightarrow$$
Là không gian con của $E$ và $V_{a} = V$ với mọi $a \in E$. Do đó, $V = a + V$.
$$\longrightarrow  \longrightarrow  \longrightarrow$$
$(2)$ Với mọi không gian con $V$ của $E$ và với mọi $a \in E$, tập hợp $V = a + V$ là không gian con afin (affine subspace).

*Chứng minh.* chứng minh là trực tiếp/dễ dàng, và được bỏ qua. Nó là cũng cho trước trong Gallier $[71]$.
$$\longrightarrow$$
Đặc biệt, khi $E$ là tự nhiên không gian afin (affine space) liên kết với không gian vectơ (vector space) $E$,
$$\longrightarrow$$
Mệnh đề 24.2 chỉ ra rằng mọi không gian con afin (affine subspace) của $E$ là của tạo thành $u + U$, cho không gian con $\longrightarrow  \longrightarrow  \longrightarrow U$ của $E$. các không gian con của $E$ là afin các không gian con của $E$ rằng chứa $0$.
$$\longrightarrow$$
Không gian con $V$ liên kết với không gian con afin (affine subspace) $V$ được gọi là hướng của $V$. Nó là
$$\times  \longrightarrow  \times  \longrightarrow  \longrightarrow$$
Cũng rõ ràng rằng ánh xạ $+: V V \to V$ được cảm sinh bởi $+: E E \to E$ confers đến $V, V , +$ afin cấu trúc. Hình 24.13 minh họa khái niệm của không gian con afin (affine subspace).
$$\longrightarrow$$
Bởi số chiều của không gian con $V$, ta có nghĩa số chiều của $V$. không gian con afin (affine subspace) có số chiều $1$ được gọi là một đường thẳng, và không gian con afin (affine subspace) có số chiều $2$ được gọi là một mặt phẳng. không gian con afin (affine subspace) của đối chiều (codimension) $1$ được gọi là một siêu phẳng (hyperplane) (nhắc lại rằng không gian con $F$ của không gian vectơ (vector space) $E$ có đối chiều (codimension) $1$ khi và chỉ khi tồn tại một không gian con $G$ có số chiều $1$ sao cho $E = F \oplus G$, tổng trực tiếp (direct sum) của $F$ và $G$, xem Strang $[176]$ hoặc Lang $[113])$.

<!-- PAGE 826 -->
Ta nói rằng hai afin các không gian con $U$ và $V$ là song song nếu của chúng các hướng là đồng nhất.
$$\longrightarrow  \longrightarrow  \longrightarrow  \longrightarrow$$
Tương đương, vì $U = V$, ta có $U = a + U$ và $V = b + U$ với mọi $a \in U$ và bất kỳ
$$\longrightarrow$$
$b \in V$, và do đó $V$ là thu được từ $U$ bởi phép tịnh tiến ab. Nói chung, khi ta talk về $n$ các điểm $a_{1}, \dots  , a_{n}$, ta có nghĩa dãy $(a_{1}, \dots  , a_{n})$, và không tập hợp ${a_{1}, \dots  , a_{n}}$ ($a_{i}’s$ cần không là phân biệt).
$$\longrightarrow$$
Theo Mệnh đề 24.2, đường thẳng là specified bởi điểm $a \in E$ và khác không vectơ $v \in E$, i.e., đường thẳng là tập hợp tất cả các điểm của tạo thành $a + \lambda v$, cho $\lambda  \in \mathbb{R}$.
$$\longrightarrow  \longrightarrow$$
Ta nói rằng ba các điểm, $b, c$ là thẳng hàng nếu các vectơ ab và ac là phụ thuộc tuyến tính (linearly dependent). Nếu hai của các điểm, $b, c$ là phân biệt, nói $a \neq  b$, thì tồn tại duy nhất một $\lambda  \in \mathbb{R}$ như vậy $\longrightarrow \longrightarrow$ rằng ac $= \lambda$ ab, và ta định nghĩa $ratio_{-\to ab}^{-\to ac} = \lambda$.
$$\longrightarrow$$
Mặt phẳng là specified bởi điểm $a \in E$ và hai các vectơ độc lập tuyến tính (linearly independent) $u, v \in E$, i.e., mặt phẳng là tập hợp tất cả các điểm của tạo thành $a + \lambda u + \mu v$, cho $\lambda , \mu  \in \mathbb{R}$.
$$\longrightarrow  \longrightarrow  \longrightarrow$$
Ta nói rằng bốn các điểm, $b, c, d$ là đồng phẳng nếu các vectơ ab, ac, và ad là phụ thuộc tuyến tính (linearly dependent). Các siêu phẳng sẽ được đặc trưng hóa little sau này.
$$\longrightarrow$$

> **Mệnh đề 24.3.** Cho trước không gian afin (affine space) $E, E , +$, với mọi họ $(a_{i})_{i\in I}$ của các điểm trong
$$E, the set V of barycenters \sum_{i}  \in I \lambda_{i} a_{i} (where \sum_{i}  \in I \lambda_{i}  = 1) is the smallest affine subspace$$
Chứa $(a_{i})_{i\in I}$.
$$Proof. If (a_{i})_{i\in I} is empty, then V = \emptyset , because of the condition \sum_{i}  \lambda_{i}  = 1. If (a_{i})_{i\in I} is$$
Khác rỗng, thì nhỏ nhất không gian con afin (affine subspace) chứa $(a_{i})_{i\in I} must^{\in I}$ chứa tập hợp $V$ của
$$barycenters \sum_{i}  \lambda_{i} a_{i}, and thus, it is enough to show that V is closed under affine combina-$$
Tions, mà $is^{\in I}$ ngay lập tức được kiểm chứng. Cho trước khác rỗng tập con $S$ của $E$, nhỏ nhất không gian con afin (affine subspace) của $E$ được sinh bởi $S$ là thường được ký hiệu bởi $\langle S\rangle$. Ví dụ, đường thẳng specified bởi hai phân biệt các điểm và $b$ được ký hiệu bởi $\langle$, $b\rangle$, hoặc chẵn/ngay cả (, $b)$, và tương tự cho các mặt phẳng, etc.
Các nhận xét:
$(1)$ Vì nó có thể được được hiển thị rằng tâm tỉ cự (barycenter) của $n$ được trọng số các điểm có thể được thu được bởi repeated các phép tính của các tâm tỉ cự của hai được trọng số các điểm, khác rỗng tập con $V$ của $E$ là không gian con afin (affine subspace) khi và chỉ khi với mọi hai các điểm, $b \in V$, tập hợp $V$ chứa tất cả barycentric các tổ hợp của và $b$. Nếu $V$ chứa ít nhất hai các điểm, thì $V$ là không gian con afin (affine subspace) khi và chỉ khi với mọi hai phân biệt các điểm, $b \in V$, tập hợp $V$ chứa đường thẳng được xác định bởi và $b$, nghĩa là, tập hợp tất cả các điểm $(1$ - $\lambda )a + \lambda b, \lambda  \in \mathbb{R}$.
$(2)$ kết quả này vẫn nghiệm đúng nếu trường $K$ có ít nhất ba phân biệt các phần tử, nhưng chứng minh là trickier!
