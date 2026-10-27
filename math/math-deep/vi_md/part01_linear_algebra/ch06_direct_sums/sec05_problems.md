# Các bài tập


<!-- PAGE 210 -->
Ta kiểm chứng được ngay rằng nếu $H$ là siêu phẳng (hyperplane) trong $E$ được định nghĩa bởi khác không dạng tuyến tính (linear form) $\phi$ sao cho $H =$ Ker $\phi$, thì với mọi khác không $\alpha  \in K$, dạng tuyến tính (linear form) $\alpha \phi$ là khác không dạng tuyến tính (linear form) rằng cũng định nghĩa $H$, nghĩa là, $H =$ Ker $\alpha \phi$. sự kiện này với phần thứ hai của Mệnh đề 6.22 chỉ ra rằng siêu phẳng (hyperplane) $H$ trong $E$ được định nghĩa bởi một chiều không gian con của đối ngẫu (dual) $E^{*}$ của $E$ bao gồm của tất cả các dạng tuyến tính rằng triệt tiêu trên $H$ (bao gồm cả không dạng tuyến tính (linear form)). Điều này là instance của đối ngẫu.

## 6.4 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ Trực tiếp các tích, các tổng, các tổng trực tiếp. $\bullet$ Các phép chiếu. $\bullet$ cơ bản phương trình
$$\dim(E) = \dim(\mathrm{Ker} f) + \dim(\mathrm{Im} f) = \dim(\mathrm{Ker} f) + rk(f)$$
(Mệnh đề 6.16). $\bullet$ Grassmann’s quan hệ
$$\dim(U) + \dim(V ) = \dim(U + V ) + \dim(U \cap V ).$$
$\bullet$ các đặc trưng của song ánh (bijective) ánh xạ tuyến tính (linear map) $f$: $E \to F. \bullet$ Hạng (rank) của ma trận.

## 6.5 Các bài tập

Bài toán 6.1. Cho $V$ và $W$ là hai các không gian con của không gian vectơ (vector space) $E$. Chứng minh rằng nếu $V \cup W$ là không gian con của $E$, thì hoặc $V \subseteq W$ hoặc $W \subseteq V$.
Bài toán 6.2. Chứng minh rằng với mọi không gian vectơ (vector space) $E$, nếu $f$: $E \to E$ là lũy đẳng (idempotent) ánh xạ tuyến tính (linear map), i.e., $f \circ f = f$, thì ta có tổng trực tiếp (direct sum)
$$E = \mathrm{Ker} f \oplus \mathrm{Im} f,$$
Sao cho $f$ là phép chiếu lên ảnh (ảnh (image)) của nó Im $f$.
Bài toán 6.3. Cho $U_{1}, \dots  , U_{p}$ là bất kỳ $p \ge 2$ các không gian con của một số không gian vectơ (vector space) $E$ và nhắc lại rằng ánh xạ tuyến tính (linear map)
$$a: U_{1} \times  \cdots  \times  U_{p} \to E$$

<!-- PAGE 211 -->
Được cho bởi
$$a(u_{1}, \dots  , u_{p}) = u_{1} + \cdots  + u_{p},$$
Với $u_{i} \in U_{i}$ cho $i = 1, \dots  , p$.
$(1)$ Nếu ta cho $Z_{i} \subseteq U_{1} \times  \cdots  \times  U_{p}$ là cho trước bởi
$$



$$
$$Z_{i} = \begin{pmatrix} u_{1}, \dots  , u_{i-1}, - & u_{j}, u_{i+1}, \dots  , u_{p} \\ i \end{pmatrix} \sum_{j=1,j\neq}^{p}  \sum_{j=1,j\neq}^{p}  u_{j} \in U_{i} \cap \begin{pmatrix} U_{j} \\ i \end{pmatrix} \sum_{j=1,j\neq}^{p}  ,$$
$$i$$
Cho $i = 1, \dots  , p$, thì chứng minh rằng
$$\mathrm{Ker} a = Z_{1} = \cdots  = Z_{p}.$$
$$In general, for any given i, the condition U_{i} \cap \sum_{j}  = (0) does not necessarily$$
$$\begin{pmatrix} p & U_{j} \\ =1,j\neq i \end{pmatrix}$$
Suy ra rằng $Z_{i} = (0)$. Do đó, cho  
$$Z = \begin{pmatrix} u_{1}, \dots  , u_{i-1}, u_{i}, u_{i+1}, \dots  , u_{p} \end{pmatrix} u_{i} = - \sum_{j=1,j\neq}^{p}  u_{j}, u_{i} \in U_{i} \cap \begin{pmatrix} U_{j} \\ i \end{pmatrix} \sum_{j=1,j\neq}^{p}  , 1 \le i \le p.$$
$$i$$
Vì Ker $a = Z_{1} = \cdots  = Z_{p}$, ta có $Z =$ Ker. Chứng minh rằng nếu
$$U_{i} \cap \begin{pmatrix} U_{j} \\ i \end{pmatrix} \sum_{j=1,j\neq}^{p}  = (0)1 \le i \le p,$$
Thì $Z =$ Ker $a = (0)$.
$(2)$ Chứng minh rằng $U_{1} + \cdots  + U_{p}$ là tổng trực tiếp (direct sum) khi và chỉ khi
$$U_{i} \cap \begin{pmatrix} U_{j} \\ i \end{pmatrix} \sum_{j=1,j\neq}^{p}  = (0)1 \le i \le p.$$
Bài toán 6.4. Giả sử rằng $E$ là hữu hạn chiều, và cho $f_{i}$: $E \to E$ là bất kỳ $p \ge 2$ các ánh xạ tuyến tính (linear maps) sao cho
$$f_{1} + \cdots  + f_{p} = id_{E}.$$
Chứng minh rằng các tính chất sau đây là tương đương:
$(1) f_{i}^{2}  = f_{i}, 1 \le i \le p$.
$(2) f_{j} \circ f_{i} = 0$, với mọi $i \neq  j, 1 \le i, j \le p$. Hint. Sử dụng Bài toán 6.2.

<!-- PAGE 212 -->
Cho $U_{1}, \dots  , U_{p}$ là bất kỳ $p \ge 2$ các không gian con của một số không gian vectơ (vector space) $E$. Chứng minh rằng $U_{1} + \cdots  + U_{p}$ là tổng trực tiếp (direct sum) khi và chỉ khi
$$U_{i} \cap \begin{pmatrix} U_{j} \end{pmatrix} \sum_{j=1}^{i-1}  = (0),i = 2, \dots  , p.$$
Bài toán 6.5. Cho trước bất kỳ không gian vectơ (vector space) $E$, ánh xạ tuyến tính (linear map) $f$: $E \to E$ là phép đối hợp (involution) nếu $f \circ f =$ id.
$(1)$ Chứng minh rằng phép đối hợp (involution) $f$ là khả nghịch. Những gì là nghịch đảo của nó?
$(2)$ Cho $E_{1}$ và $E_{-1}$ là các không gian con của $E$ được định nghĩa như sau:
$$E_{1} = {u \in E | f(u) = u}$$
$$E_{-1} = {u \in E | f(u) = -u}.$$
Chứng minh rằng ta có tổng trực tiếp (direct sum)
$$E = E_{1} \oplus E_{-1}.$$
Hint. Với mọi $u \in E$, viết
$$-$$
$$u = \frac{u + f(u)}{2} + \frac{uf(u)}{2} .$$
$(3)$ Nếu $E$ là hữu hạn chiều và $f$ là phép đối hợp (involution), chứng minh rằng tồn tại một cơ sở (basis) của $E$ đối với mà ma trận của $f$ là của tạo thành
$$I_{k,n-k} = \begin{pmatrix} I_{k} & 0 \\ 0 & -I_{n-k} \end{pmatrix} ,$$
Ở đâu $I_{k}$ là $k \times  k$ ma trận đơn vị (identity matrix) (tương tự cho $I_{n-k})$ và $k = dim(E_{1})$. Có thể bạn cho hình học interpretation của action của $f$ (especially khi $k = n$ - $1)$?
Bài toán 6.6. một ma trận cỡ $n \times  n$ $H$ là trên Hessenberg nếu $h_{jk} = 0$ với mọi $(j, k)$ sao cho $j$ - $k \ge 0$. trên Ma trận Hessenberg là unreduced nếu $h_{i+1i} \neq  0$ cho $i = 1, \dots  , n$ - $1$. Chứng minh rằng nếu $H$ là suy biến unreduced trên Ma trận Hessenberg, thì dim(Ker $(H)) = 1$.
Bài toán 6.7. Cho $A$ là bất kỳ ma trận cỡ $n \times  k$.
$(1)$ Chứng minh rằng ma trận cỡ $k \times  k$ $A^{\top}A$ và ma trận $A$ có cùng không gian hạch (nullspace). Sử dụng điều này để chứng minh rằng $rank(A^{\top}A) =$ hạng (rank)(). Tương tự, chứng minh rằng ma trận cỡ $n \times  n$ $AA^{\top}$ và ma trận $A^{\top}$ có cùng không gian hạch (nullspace), và kết luận rằng $rank(AA^{\top}) = rank(A^{\top})$. Ta sẽ chứng minh sau này rằng $rank(A^{\top}) =$ hạng (rank)().
$$\mathbb{R}^{n}$$
$(2)$ Cho $a_{1}, \dots  , a_{k}$ là $k$ các vectơ độc lập tuyến tính (linearly independent) trong $(1 \le k \le n)$, và cho $A$ là ma trận cỡ $n \times  k$ có cột thứ $i$ là $a_{i}$. Chứng minh rằng $A^{\top}A$ có hạng (rank) $k$, và rằng nó là khả nghịch. Cho $P = A(A^{\top}A)^{-1}A^{\top}$ (một ma trận cỡ $n \times  n$). Chứng minh rằng
$$P^{2}= P$$
$$P^{\top} = P.$$

<!-- PAGE 213 -->
Những gì là ma trận $P$ khi $k = 1$?
$(3)$ Chứng minh rằng ảnh (image) của $P$ là không gian con $V$ được sinh (spanned) bởi $a_{1}, \dots  , a_{k}$, hoặc tương đương
$$\mathbb{R}^{n} \mathbb{R}^{k}$$
Tập hợp tất cả các vectơ trong của tạo thành Ax, với $x \in$. Chứng minh rằng không gian hạch (nullspace) $U$ của $P$ là
$$\mathbb{R}^{n}$$
Tập hợp của các vectơ $u \in$ sao cho $A^{\top}u = 0$. Có thể bạn cho hình học interpretation của $U$?
$$\mathbb{R}^{n}$$
Kết luận rằng $P$ là phép chiếu của lên không gian con $V$ được sinh (spanned) bởi $a_{1}, \dots  , a_{k}$, và rằng
$$\mathbb{R}^{n}$$
$$= U \oplus V.$$
$$\mathbb{R}^{2}$$
Bài toán 6.8. phép quay $R_{\theta}$ trong mặt phẳng được cho bởi ma trận
$$R_{\theta} = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} .$$
$(1)$ Sử dụng Matlab để chỉ ra action của phép quay $R_{\theta}$ trên đơn giản hình chẳng hạn như tam giác hoặc rectangle, cho khác nhau các giá trị của $\theta$, bao gồm cả $\theta  = \pi /6, \pi /4, \pi /3, \pi /2$.
$(2)$ Chứng minh rằng $R_{\theta}$ là khả nghịch và rằng nghịch đảo của nó là $R_{-\theta}$.
$(3)$ Với mọi hai các phép quay $R_{\alpha}$ và $R_{\beta}$, chứng minh rằng
$$R_{\beta} \circ R_{\alpha} = R_{\alpha} \circ R_{\beta} = R_{\alpha+\beta}.$$
Sử dụng (2)-(3) để chứng minh rằng các phép quay trong mặt phẳng tạo thành nhóm giao hoán (commutative group) được ký hiệu Do đó(2).
$$\mathbb{R}^{2}$$
Bài toán 6.9. Xét ánh xạ afin (affine map) $R_{\theta ,(a1,a2)}$ trong cho trước bởi
$$\begin{pmatrix} y_{1} \\ y_{2} \end{pmatrix} = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} + \begin{pmatrix} a_{1} \\ a_{2} \end{pmatrix} .$$
$(1)$ Chứng minh rằng nếu $\theta  \neq  k2\pi$, với $k \in \mathbb{Z}$, thì $R_{\theta ,(a1,a2)}$ có duy nhất cố định điểm $(c_{1}, c_{2})$, nghĩa là, tồn tại duy nhất một điểm $(c_{1}, c_{2})$ sao cho
$$\begin{pmatrix} c_{1} \\ c_{2} \end{pmatrix} = R_{\theta ,(a1,a2)} \begin{pmatrix} c_{1} \\ c_{2} \end{pmatrix} ,$$
Và điều này cố định điểm được cho bởi
$$\begin{pmatrix} c_{1} \\ c_{2} \end{pmatrix} = \frac{1}{2 \sin(\theta /2)} \begin{pmatrix} \cos(\pi /2 -\theta /2) & -\sin(\pi /2 -\theta /2) \\ \sin(\pi /2 -\theta /2) & \cos(\pi /2 -\theta /2) \end{pmatrix} \begin{pmatrix} a_{1} \\ a_{2} \end{pmatrix} .$$
$(2)$ Trong điều này câu hỏi ta vẫn giả sử rằng $\theta$ ̸ $= k2\pi$, với $k \in \mathbb{Z}$. Bởi translating tọa độ hệ với gốc $(0, 0)$ đến mới tọa độ hệ với gốc $(c_{1}, c_{2})$, mà

<!-- PAGE 214 -->
Có nghĩa là nếu $(x_{1}, x_{2})$ là các tọa độ đối với tiêu chuẩn gốc $(0, 0)$ và nếu $(x_{1}', x_{2}')$ là các tọa độ đối với mới gốc $(c_{1}, c_{2})$, ta có
$$x_{1} = x_{1}' + c_{1}$$
$$x_{2} = x_{2}' + c_{2}$$
Và tương tự cho $(y_{1}, y_{2})$ và $(y_{1}', y_{2}')$, thì chỉ ra rằng
$$\begin{pmatrix} y_{1} \\ y_{2} \end{pmatrix} = R_{\theta ,(a1,a2)} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix}$$
Trở thành
$$\begin{pmatrix} y_{1}' \\ y_{2}' \end{pmatrix} = R_{\theta} \begin{pmatrix} x_{1}' \\ x_{2}' \end{pmatrix} .$$
Kết luận rằng đối với mới gốc $(c_{1}, c_{2})$, ánh xạ afin (affine map) $R_{\theta ,(a1,a2)}$ trở thành phép quay $R_{\theta}$. Ta nói rằng $R_{\theta ,(a1,a2)}$ là phép quay của tâm $(c_{1}, c_{2})$.
$(3)$ Sử dụng Matlab để chỉ ra action của ánh xạ afin (affine map) $R_{\theta ,(a1,a2)}$ trên đơn giản hình chẳng hạn như tam giác hoặc rectangle, cho $\theta  = \pi /3$ và khác nhau các giá trị của $(a_{1}, a_{2})$. Display tâm $(c_{1}, c_{2})$ của phép quay. Những gì loại của các phép biến đổi tương ứng với $\theta  = k2\pi$, với $k \in \mathbb{Z}$?
$(4)$ Chứng minh rằng nghịch đảo của $R_{\theta ,(a1,a2)}$ là của tạo thành $R_{-\theta ,(b1,b2)}$, và tìm $(b_{1}, b_{2})$ theo $\theta$ và $(a_{1}, a_{2})$.
$(5)$ Cho trước hai các ánh xạ afin $R_{\alpha ,(a1,a2)}$ và $R_{\beta ,(b1,b2)}$, chứng minh rằng
$$R_{\beta ,(b1,b2)} \circ R_{\alpha ,(a1,a2)} = R_{\alpha+\beta ,(t1,t2)}$$
Với một số $(t_{1}, t_{2})$, và tìm $(t_{1}, t_{2})$ theo $\beta , (a_{1}, a_{2})$ và $(b_{1}, b_{2})$. Chẵn/ngay cả trong trường hợp ở đâu $(a_{1}, a_{2}) = (0, 0)$, chứng minh rằng nói chung
$$R_{\beta ,(b1,b2)} \circ R_{\alpha} \neq  R_{\alpha} \circ R_{\beta ,(b1,b2)}.$$
Sử dụng (4)-(5) để chỉ ra rằng các ánh xạ afin của mặt phẳng được định nghĩa trong bài toán này tạo thành nonabelian nhóm được ký hiệu SE(2). Chứng minh rằng $R_{\beta ,(b1,b2)} \circ R_{\alpha ,(a1,a2)}$ là không phép tịnh tiến (có thể đồng nhất thức) khi và chỉ khi $\alpha  +\beta  \neq  k2\pi$, với mọi $k \in \mathbb{Z}$. Tìm của nó tâm của phép quay khi $(a_{1}, a_{2}) = (0, 0)$. Nếu $\alpha +\beta  = k2\pi$, thì $R_{\beta ,(b1,b2)} \circ R_{\alpha ,(a1,a2)}$ là thuần túy phép tịnh tiến. Tìm phép tịnh tiến vectơ của $R_{\beta ,(b1,b2)} \circ R_{\alpha ,(a1,a2)}$.
$$\mathbb{R}^{n}$$
Bài toán 6.10. (Afin các không gian con) $A$ tập con $\mathcal{A}$ của được gọi là một không gian con afin (affine subspace) nếu hoặc
$$\mathbb{R}^{n}  \mathbb{R}^{n}$$
$\mathcal{A} = \emptyset$, hoặc tồn tại một vectơ $a \in$ và một số không gian con $U$ của sao cho
$$\mathcal{A} = a + U = {a + u | u \in U}.$$

<!-- PAGE 215 -->
Ta định nghĩa số chiều $dim(\mathcal{A})$ của $\mathcal{A}$ như số chiều dim(U) của $U$.
$(1)$ Nếu $\mathcal{A} = a + U$, tại sao là $a \in A$? Những gì là afin các không gian con có số chiều $0$? Những gì là afin các không gian con có số chiều $1$ (bắt đầu với $\mathbb{R}^{2})$? Những gì là afin các không gian con có số chiều $2$ (bắt đầu với $\mathbb{R}^{3})$? Chứng minh rằng bất kỳ khác rỗng không gian con afin (affine subspace) là đóng dưới các tổ hợp afin.
$(2)$ Chứng minh rằng nếu $\mathcal{A} = a + U$ là bất kỳ khác rỗng không gian con afin (affine subspace), thì $\mathcal{A} = b + U$ với mọi $b \in A$.
$$\mathbb{R}^{n}$$
$(3)$ Cho $\mathcal{A}$ là bất kỳ khác rỗng tập con của đóng dưới các tổ hợp afin. Với mọi $a \in A$, chứng minh rằng
$$\mathbb{R}^{n}$$
$$U_{a} = {x -a \in | x \in A}$$
$$\mathbb{R}^{n}$$
Là (tuyến tính) không gian con của sao cho
$$\mathcal{A} = a + U_{a}.$$
Chứng minh rằng $U_{a}$ không phụ thuộc vào lựa chọn của $a \in A$; nghĩa là, $U_{a} = U_{b}$ với mọi, $b \in A$. Thực ra, chứng minh rằng
$$\mathbb{R}^{n}$$
$$U_{a} = U = {y -x \in | x, y \in A},for all a \in A,$$
Và do đó
$$\mathcal{A} = a + U,for any a \in A.$$
Nhận xét: không gian con $U$ được gọi là hướng của $\mathcal{A}$.
$(4)$ Hai khác rỗng afin $subspaces\mathcal{A} and\mathcal{B}$ được nói là song song khi và chỉ khi chúng có cùng hướng. Chứng minh rằng rằng nếu ̸ $=\mathcal{B}$ và $\mathcal{A}$ và $\mathcal{B}$ là song song, thì $A \cap B = \emptyset$.
Nhận xét: ở trên chỉ ra rằng afin các không gian con behave khá một cách khác nhau từ tuyến tính các không gian con.
Bài toán 6.11. (Afin các hệ quy chiếu và các ánh xạ afin) Với mọi vectơ $v = (v_{1}, \dots  , v_{n}) \in \mathbb{R}^{n}$, cho $\mathbb{R}^{n+1} \mathbb{R}^{n+1} v \in$ là vectơ $v = (v_{1}, \dots  , v_{n}, 1)$. Tương đương, $v = (v_{1}, \dots  ,v_{n+1}) \in$ là $b  b  b b  b$ vectơ được định nghĩa bởi
$$($$
$$v_{i}if 1 \le i \le n,$$
$$v_{i} =$$
$$b1if i = n + 1.$$
$$\mathbb{R}^{n}$$
$(1)$ Với mọi $m + 1$ các vectơ $(u_{0}, u_{1}, \dots  , u_{m})$ với $u_{i} \in$ và $m \le n$, chứng minh rằng nếu $m$ các vectơ $(u_{1}$ - $u_{0}, \dots  , u_{m}$ - $u_{0})$ là độc lập tuyến tính (linearly independent), thì $m + 1$ các vectơ $(u_{0}, \dots  ,u_{m})$
$$b b$$
Là độc lập tuyến tính (linearly independent).
$(2)$ Chứng minh rằng nếu $m + 1$ các vectơ $(u_{0}, \dots  ,u_{m})$ là độc lập tuyến tính (linearly independent), thì với mọi
$$b b$$
Lựa chọn của $i$, với $0 \le i \le m$, $m$ các vectơ $u_{j}$ - $u_{i}$ cho $j \in {0, \dots  , m}$ với $j$ - $i \neq  0$ là độc lập tuyến tính (linearly independent).

<!-- PAGE 216 -->
Bất kỳ $m + 1$ các vectơ $(u_{0}, u_{1}, \dots  , u_{m})$ sao cho $m + 1$ các vectơ $(u_{0}, \dots  ,u_{m})$ là một cách tuyến tính
$$b b$$
Độc lập được nói là độc lập afin (affinely independent). Từ $(1)$ và $(2)$, vectơ $(u_{0}, u_{1}, \dots  , u_{m})$ là độc lập afin (affinely independent) khi và chỉ khi với mọi bất kỳ lựa chọn của $i$, với $0 \le i \le m$, $m$ các vectơ $u_{j}$ - $u_{i}$ cho $j \in {0, \dots  , m}$ với $j$ - $i \neq  0$ là độc lập tuyến tính (linearly independent). Nếu $m = n$, ta nói rằng $n + 1$ độc lập afin (affinely independent) các vectơ $(u_{0}, u_{1}, \dots  , u_{n})$ tạo thành hệ quy chiếu afin (affine frame) của $\mathbb{R}^{n}$.
$(3)$ nếu $(u_{0}, u_{1}, \dots  , u_{n})$ là hệ quy chiếu afin (affine frame) của $\mathbb{R}^{n}$, thì chứng minh rằng với mọi vectơ $v \in \mathbb{R}^{n}$, tồn tại duy nhất một $(n+1)-tuple (\lambda_{0} , \lambda_{1} , \dots  , \lambda_{n}$) $\in \mathbb{R}^{n+1}$, với $\lambda_{0}  +\lambda_{1}  +\cdots +\lambda_{n}  = 1$, sao cho
$$v = \lambda_{0} u_{0} + \lambda_{1} u_{1} + \cdots  + \lambda_{n} u_{n}.$$
Các vô hướng $(\lambda_{0} , \lambda_{1} , \dots  , \lambda_{n}$) được gọi là barycentric (hoặc afin) các tọa độ của $v$ w.r.t. hệ quy chiếu afin (affine frame) $(u_{0}, u_{1}, \dots  , u_{n})$. Nếu ta viết $e_{i} = u_{i}$ - $u_{0}$, cho $i = 1, \dots  , n$, thì chứng minh rằng ta có
$$v = u_{0} + \lambda_{1} e_{1} + \cdots  + \lambda_{n} e_{n},$$
$$\mathbb{R}^{n}$$
Và vì $(e_{1}, \dots  , e_{n})$ là cơ sở (basis) của (bởi $(1)$ & $(2))$, bộ $n$ $(\lambda_{1} , \dots  , \lambda_{n}$) bao gồm của tiêu chuẩn các tọa độ của $v$ - $u_{0}$ trên cơ sở (basis) $(e_{1}, \dots  , e_{n})$.
$$\mathbb{R}^{n}  \mathbb{R}^{n}$$
Ngược lại, với mọi vectơ $u_{0} \in$ và với mọi cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của, cho $u_{i} = u_{0} + e_{i}$ cho $i = 1, \dots  , n$. Chứng minh rằng $(u_{0}, u_{1}, \dots  , u_{n})$ là hệ quy chiếu afin (affine frame) của $\mathbb{R}^{n}$, và với mọi $v \in \mathbb{R}^{n}$, nếu
$$v = u_{0} + x_{1}e_{1} + \cdots  + x_{n}e_{n},$$
$$\mathbb{R}^{n}$$
Với $(x_{1}, \dots  , x_{n}) \in$ (duy nhất), thì
$$v = (1 -(x_{1} + \cdots  + x_{x}))u_{0} + x_{1}u_{1} + \cdots  + x_{n}u_{n},$$
Sao cho $(1-(x_{1} +\cdots +x_{x})), x_{1}, \cdots  , x_{n})$, là tọa độ tỉ cự (barycentric coordinates) của $v$ w.r.t. hệ quy chiếu afin (affine frame) $(u_{0}, u_{1}, \dots  , u_{n})$. ở trên chỉ ra rằng có một tương ứng một-một (bijection) giữa afin các hệ quy chiếu $(u_{0}, \dots , u_{n})$ và các cặp $(u_{0}, (e_{1}, \dots  , e_{n}))$, với $(e_{1}, \dots  , e_{n})$ cơ sở (basis). Cho trước hệ quy chiếu afin (affine frame) $(u_{0}, \dots  , u_{n})$, ta thu được cơ sở (basis) $(e_{1}, \dots  , e_{n})$ với $e_{i} = u_{i} -u_{0}$, cho $i = 1, \dots  , n$; cho trước cặp $(u_{0}, (e_{1}, \dots , e_{n}))$ ở đâu $(e_{1}, \dots  , e_{n})$ là cơ sở (basis), ta thu được hệ quy chiếu afin (affine frame) $(u_{0}, \dots  , u_{n})$, với $u_{i} = u_{0} + e_{i}$, cho $i = 1, \dots  , n$. Ở đó là cũng tương ứng một-một (bijection) giữa tọa độ tỉ cự (barycentric coordinates) w.r.t. hệ quy chiếu afin (affine frame) $(u_{0}, \dots  , u_{n})$ và tiêu chuẩn các tọa độ w.r.t. cơ sở (basis) $(e_{1}, \dots  , e_{n})$. barycentric cordinates $(\lambda_{0} , \lambda_{1} , \dots  , \lambda_{n}$) của $v$ (với $\lambda_{0}  + \lambda_{1}  + \cdots  + \lambda_{n}  = 1)$ cho tiêu chuẩn các tọa độ $(\lambda_{1} , \dots  , \lambda_{n}$) của $v$ - $u_{0}$; tiêu chuẩn các tọa độ $(x_{1}, \dots  , x_{n})$ của $v$ - $u_{0}$ cho tọa độ tỉ cự (barycentric coordinates) $(1$ - $(x_{1} + \cdots  + x_{n}), x_{1}, \dots  , x_{n})$ của $v$.
$(4)$ Nhắc lại rằng ánh xạ afin (affine map) là ánh xạ $f$: $E \to F$ giữa các không gian vectơ rằng bảo toàn các tổ hợp afin; nghĩa là,
$$f \sum_{i=1}^{m}  \lambda_{i} u_{i}!= \sum_{i=1}^{m}  \lambda_{i} f(u_{i}),$$

<!-- PAGE 217 -->
$$for all u_{1} \dots  , u_{m} \in E and all \lambda_{i}  \in K such that \sum_{i}  m=1 \lambda_{i}  = 1.$$
$$\mathbb{R}^{n} \mathbb{R}^{m}$$
Cho $(u_{0}, \dots  , u_{n})$ là bất kỳ hệ quy chiếu afin (affine frame) trong và cho $(v_{0}, \dots  , v_{n})$ là bất kỳ các vectơ trong. Chứng minh
$$\mathbb{R}^{n} \mathbb{R}^{m}$$
Rằng tồn tại duy nhất một ánh xạ afin (affine map) $f$: $\to$ sao cho
$$f(u_{i}) = v_{i},i = 0, \dots  , n.$$
$$\mathbb{R}^{n}$$
$(5)$ Cho $(a_{0}, \dots  , a_{n})$ là bất kỳ hệ quy chiếu afin (affine frame) trong và cho $(b_{0}, \dots  , b_{n})$ là bất kỳ $n + 1$ các điểm trong $\mathbb{R}^{n}$. Chứng minh rằng tồn tại duy nhất một $(n + 1) \times  (n + 1)$ ma trận
$$A = \begin{pmatrix} B & w \\ 0 & 1 \end{pmatrix}$$
Tương ứng với duy nhất ánh xạ afin (affine map) $f$ sao cho
$$f(a_{i}) = b_{i},i = 0, \dots  , n,$$
Trong nghĩa rằng
$$Aa_{i} =b_{i},i = 0, \dots  , n,$$
$$b b$$
Và rằng $A$ được cho bởi
$$.$$
$$A = \begin{pmatrix} bb_{0} & bb_{1} & \cdots & bb_{n} \\ bottomrowofA \end{pmatrix} \begin{pmatrix} a_{0} & a_{1} & \cdots \\ b & b & b \end{pmatrix} a_{n}^{-1}$$
Tạo sure để chứng minh rằng là $(0, \dots  , 0, 1)$. Trong trường hợp đặc biệt khi $(a_{0}, \dots  , a_{n})$ là chính tắc hệ quy chiếu afin (affine frame) với $a_{i} = e_{i+1}$ cho $i = 0, \dots  , n$ - $1$ và $a_{n} = (0, \dots  , 0)$ (ở đâu $e_{i}$ là vectơ cơ sở chính tắc thứ $i$), chỉ ra rằng
$$\begin{pmatrix} a_{0} & a_{1} & \cdots & a_{n} \\ b & b & b \end{pmatrix} = \begin{pmatrix} 1 & 0 & \cdots & 0 & 0 \\ 0 & 1 & \cdots & 0 & 0 \\ \vdots & \vdots & \ddots & 0 & 0 \\ 0 & 0 & \cdots & 1 & 0 \\ 1 & 1 & \cdots & 1 & 1 \end{pmatrix}$$
Và
$$a_{n}^{-1} = \begin{pmatrix} 1 & 0 & \cdots & 0 & 0 \\ 0 & 1 & \cdots & 0 & 0 \\ \vdots & \vdots & \ddots & 0 & 0 \\ 0 & 0 & \cdots & 1 & 0 \\ -1 & -1 & \cdots & -1 & 1 \end{pmatrix} .$$
$$\begin{pmatrix} a_{0} & a_{1} & \cdots \\ b & b & b \end{pmatrix}$$
Ví dụ, khi $n = 2$, nếu ta viết $b_{i} = (x_{i}, y_{i})$, thì ta có
$$A = \begin{pmatrix} x_{1} & x_{2} & x_{3} \\ y_{1} & y_{2} & y_{3} \\ 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 1 & 1 \end{pmatrix} = \begin{pmatrix} x_{1} -x_{3} & x_{2} -x_{3} & x_{3} \\ y_{1} -y_{3} & y_{2} -y_{3} & y_{3} \\ 0 & 0 & 1 \end{pmatrix} .$$
$$--$$

<!-- PAGE 218 -->
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
$(6)$ Nhắc lại rằng khác rỗng afin $subspace\mathcal{A}$ của là bất kỳ khác rỗng tập con của đóng
$$\mathbb{R}^{n} \mathbb{R}^{m}$$
Dưới các tổ hợp afin. Với mọi ánh xạ afin (affine map) $f$: $\to$, với mọi không gian con afin (affine subspace) $\mathcal{A}$ của $\mathbb{R}^{n}$, và bất kỳ không gian con afin (affine subspace) $\mathcal{B}$ của $\mathbb{R}^{m}$, chứng minh rằng $f(\mathcal{A})$ là không gian con afin (affine subspace) của $\mathbb{R}^{m}$, và rằng $f^{-1} (\mathcal{B})$ là không gian con afin (affine subspace) của $\mathbb{R}^{n}$.
