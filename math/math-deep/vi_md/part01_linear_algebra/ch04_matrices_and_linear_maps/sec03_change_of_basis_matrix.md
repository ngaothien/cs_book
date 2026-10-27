# Ma trận chuyển cơ sở (change of basis matrix)


<!-- PAGE 136 -->
Trên cơ sở (basis) $(u_{1}, \dots  , u_{n})$. Vì $\phi$ được biểu diễn bởi vectơ cột (column vector) $\lambda^{\top}$ trên đối ngẫu (dual) cơ sở (basis) $(v_{1}^{*}, \dots  , v_{m}^{*})$, ta xem rằng $f^{\top}(\phi$) được biểu diễn bởi vectơ cột (column vector)
$$(\lambda A)^{\top}= A^{\top}\lambda^{\top}$$
Trên đối ngẫu (dual) cơ sở (basis) $(u_{1}^{*}, \dots  , u_{n}^{*})$. ma trận định nghĩa $f^{\top}$ trên đối ngẫu (dual) các cơ sở $(v_{1}^{*}, \dots  , v_{m}^{*})$ và $(u_{1}^{*}, \dots  , u_{n}^{*})$ là thật vậy $A^{\top}$. Conceptually, ta sẽ chỉ ra sau này (xem Mục 30.1) rằng ánh xạ tuyến tính (linear map) $f^{\top}$: $F^{*} \to E^{*}$ được định nghĩa bởi
$$f^{\top} (\phi ) = \phi  \circ f,$$
Với mọi $\phi  \in F^{*}$ (nhớ rằng $\phi$: $F \to K$, do đó composing $f$: $E \to F$ và $\phi$: $F \to K$ cho ta dạng tuyến tính (linear form) $\phi  \circ f$: $E \to K)$.

## 4.3 Ma trận chuyển cơ sở (change of basis matrix)

Nó là quan trọng đến nhận thấy rằng đẳng cấu $M$: Hom(E, $F) \to M_{n,p}$ cho trước theo Mệnh đề 4.2 phụ thuộc vào lựa chọn của các cơ sở $(u_{1}, \dots  , u_{p})$ và $(v_{1}, \dots  , v_{n})$, và tương tự cho đẳng cấu $M$: Hom(E, $E) \to M_{n}$, mà phụ thuộc vào lựa chọn của cơ sở (basis) $(u_{1}, \dots  , u_{n})$. Do đó, nó sẽ là hữu ích đến biết cách mà chuyển cơ sở (change of basis) affects biểu diễn của ánh xạ tuyến tính (linear map) $f$: $E \to F$ như ma trận. sau đây đơn giản mệnh đề là cần thiết.

> **Mệnh đề 4.3.** Cho $E$ là không gian vectơ (vector space), và cho $(u_{1}, \dots  , u_{n})$ là cơ sở (basis) của $E$. Với mọi
$$family (v_{1}, \dots  , v_{n}), let P = (a_{i j}) be the matrix defined such that v_{j} = \sum_{i}  n=1 a_{i j}u_{i}. The matrix$$
$P$ là khả nghịch khi và chỉ khi $(v_{1}, \dots  , v_{n})$ là cơ sở (basis) của $E$.

*Chứng minh.* Lưu ý rằng ta có $P =$ M(f), ma trận (đối với cơ sở (basis) $(u_{1}, \dots  , u_{n}))$ liên kết với duy nhất ánh xạ tuyến tính (linear map) $f$: $E \to E$ sao cho $f(u_{i}) = v_{i}$. Vì $E$ có số chiều $n$, theo Mệnh đề 3.20, $f$ là đơn ánh (injective) $iff(v_{1}, \dots  , v_{n})$ là độc lập tuyến tính (linearly independent) khi và chỉ khi $(v_{1}, \dots  , v_{n})$ là cơ sở (basis) của $E$ khi và chỉ khi $f$ là song ánh (bijective). Giả sử rằng $P =$ M(f) là khả nghịch. Ta có f(x) $= 0$ khi và chỉ khi M(f)M(x) $=$ PM(x) $= 0$, mà suy ra (bằng cách nhân cả hai các vế/cạnh bởi $P^{-1}$) rằng M(x) $= 0$, và do đó $x = 0$. Theo Mệnh đề 3.19, $f$ là đơn ánh (injective), và do đó cũng song ánh (bijective), và do đó $(v_{1}, \dots  , v_{n})$ là cơ sở (basis) của $E$. Ngược lại, giả sử rằng $(v_{1}, \dots  , v_{n})$ là cơ sở (basis) của $E$, mà suy ra rằng $f$ là đẳng cấu. Hơn nữa, hiển nhiên là ma trận đơn vị (identity matrix) $I_{n}$ là ma trận liên kết với đồng nhất thức id: $E \to E$ w.r.t. bất kỳ cơ sở (basis). Vì $f$ là đẳng cấu, $f \circ f^{-1} = f^{-1} \circ f =$ id, và theo Mệnh đề 4.2, ta thu được $M(f)M(f^{-1}$) $= M(f^{-1}$)M(f) $= I_{n}$, chỉ ra rằng $P$ là khả nghịch và rằng $M(f^{-1}$) $= P^{-1}$. quan trọng hệ quả của Mệnh đề 4.3 cho ta sau đây tiêu chuẩn cho ma trận vuông (square matrix) là khả nghịch. Điều này tiêu chuẩn đã là đã được chứng minh trong Mệnh đề 3.16 nhưng Mệnh đề 4.3 cho ta shorter chứng minh.

<!-- PAGE 137 -->

> **Mệnh đề 4.4.** ma trận vuông (square matrix) $A \in M_{n}(K)$ là khả nghịch khi và chỉ khi của nó các cột $(A^{1}, \dots  , A^{n})$ là độc lập tuyến tính (linearly independent).

*Chứng minh.* Thứ nhất giả sử rằng $A$ là khả nghịch. Nếu $\lambda_{1} A^{1} + \cdots  + \lambda_{n} A^{n} = 0$ với một số $\lambda_{1} , \dots  , \lambda_{n}  \in K$, thì
$$A\lambda  = \lambda_{1} A^{1}+ \cdots  + \lambda_{n} A^{n}= 0,$$
Ở đâu $\lambda$ là vectơ cột (column vector) $\lambda  = (\lambda_{1} , \dots  , \lambda_{n}$). Vì $A$ có nghịch đảo $A^{-1}$, bằng cách nhân cả hai vế của phương trình $A\lambda  = 0$ bởi $A^{-1}$ ta thu được
$$A^{-1}A\lambda  = I_{n}\lambda  = \lambda  = A^{-1}0 = 0,$$
Mà chỉ ra rằng các cột $(A^{1}, \dots  , A^{n})$ là độc lập tuyến tính (linearly independent). Ngược lại, giả sử rằng các cột $(A^{1}, \dots  , A^{n})$ là độc lập tuyến tính (linearly independent). Vì không gian vectơ (vector space) $E = K^{n}$ có số chiều $n$, các vectơ $(v_{1}, \dots  , v_{n}) = (A^{1}, \dots  , A^{n})$ tạo thành cơ sở (basis) của $K^{n}$. Theo Định nghĩa, ma trận $A$ được định nghĩa bởi biểu diễn mỗi vectơ $v_{j} = A^{j}$ như
$$n$$
$$linear combination A^{j}= \sum_{i}  a_{ij}e_{i}, where (e_{1}, \dots  , e_{n}) is the canonical basis of K^{n}, and$$
Vì $(v_{1}, \dots  , v_{n})$ là $basis,^{=1}$ theo Mệnh đề 4.3, ma trận $A$ là khả nghịch. Mệnh đề 4.3 suggests sau đây định nghĩa.

> **Định nghĩa 4.3.** Cho trước không gian vectơ (vector space) $E$ có số chiều $n$, với mọi hai các cơ sở $(u_{1}, \dots  , u_{n})$ và $(v_{1}, \dots  , v_{n})$ của $E$, cho $P = (a_{i j})$ là ma trận khả nghịch (invertible matrix) được định nghĩa sao cho
$$v_{j} = \sum_{i=1}^{n}  a_{i j}u_{i},$$
Mà là cũng ma trận của đồng nhất thức id: $E \to E$ đối với các cơ sở $(v_{1}, \dots  , v_{n})$ và $(u_{1}, \dots  , u_{n})$, trong rằng thứ tự. Thật vậy, ta biểu diễn mỗi $id(v_{j}) = v_{j}$ trên cơ sở (basis) $(u_{1}, \dots  , u_{n})$. các hệ số $a_{1j}, a_{2j}, \dots  , a_{nj}$ của $v_{j}$ trên cơ sở (basis) $(u_{1}, \dots  , u_{n})$ tạo thành cột thứ $j$ của ma trận $P$ được hiển thị dưới đây:
$$v_{1}v_{2}\dots v_{n}$$
$$u_{1}$$
$$u_{2}\vdots \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \dots & a_{nn} \end{pmatrix} .$$
$$u_{n}$$
Ma trận $P$ được gọi là ma trận chuyển cơ sở (change of basis matrix) từ $(u_{1}, \dots  , u_{n})$ đến $(v_{1}, \dots  , v_{n})$. Rõ ràng, ma trận chuyển cơ sở (change of basis matrix) từ $(v_{1}, \dots  , v_{n})$ đến $(u_{1}, \dots  , u_{n})$ là $P^{-1}$. Vì $P = (a_{i j})$ là ma trận của đồng nhất thức id: $E \to E$ đối với các cơ sở $(v_{1}, \dots  , v_{n})$ và

<!-- PAGE 138 -->
$(u_{1}, \dots  , u_{n})$, cho trước bất kỳ vectơ $x \in E$, nếu $x = x_{1}u_{1} + \cdots  + x_{n}u_{n}$ trên cơ sở (basis) $(u_{1}, \dots  , u_{n})$ và $x = x_{1}'v_{1} + \cdots  + x_{n}'v_{n}$ trên cơ sở (basis) $(v_{1}, \dots  , v_{n})$, từ Mệnh đề 4.2, ta có
$$\begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix} = \begin{pmatrix} a_{1 1} & \dots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{n1} & \dots & a_{n n} \end{pmatrix} \begin{pmatrix} x_{1}' \\ \vdots \\ x_{n}' \end{pmatrix} ,$$
Chỉ ra rằng old các tọa độ $(x_{i})$ của $x$ (trên $(u_{1}, \dots  , u_{n}))$ được biểu diễn theo mới các tọa độ $(x_{i}')$ của $x$ (trên $(v_{1}, \dots  , v_{n}))$. sự kiện này có thể dường như sai, nhưng nó là đúng như ta có thể reassure chính chúng ta bởi thực hiện sau đây phép tính. Giả sử rằng $n = 2$, sao cho
$$v_{1} = a_{11}u_{1} + a_{21}u_{2}$$
$$v_{2} = a_{12}u_{1} + a_{22}u_{2},$$
Và ma trận của chúng ta là
$$A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} .$$
Cùng vectơ $x$ được viết như
$$x = x_{1}u_{1} + x_{2}u_{2} = x_{1}'v_{1} + x_{2}'v_{2},$$
Do đó bằng cách thế các biểu thức cho $v_{1}$ và $v_{2}$ như các tổ hợp tuyến tính của $u_{1}$ và $u_{2}$, ta thu được
$$x_{1}u_{1} + x_{2}u_{2} = x_{1}'v_{1} + x_{2}'v_{2}$$
$$= x_{1}'(a_{11}u_{1} + a_{21}u_{2}) + x_{2}'(a_{12}u_{1} + a_{22}u_{2})$$
$$= (a_{11}x_{1}' + a_{12}x_{2}')u_{1} + (a_{21}x_{1}' + a_{22}x_{2}')u_{2},$$
Và vì $u_{1}$ và $u_{2}$ là độc lập tuyến tính (linearly independent), ta phải có
$$x_{1} = a_{11}x_{1}' + a_{12}x_{2}'$$
$$x_{2} = a_{21}x_{1}' + a_{22}x_{2}',$$
Cụ thể là
$$\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} \begin{pmatrix} x_{1}' \\ x_{2}' \end{pmatrix} ,$$
Như đã khẳng định. Nếu các vectơ $u_{1}, \dots  , u_{n}$ và các vectơ $v_{1}, \dots  , v_{n}$ là các vectơ trong $K^{n}$, thì ta có thể tạo thành ma trận cỡ $n \times  n$ $U = (u_{1} \cdots  u_{n})$ có các cột là $u_{1}, \dots  , u_{n}$ và ma trận cỡ $n \times  n$ $V = (v_{1} \cdots  v_{n})$ có các cột là $v_{1}, \dots  , v_{n}$. Thì ta có thể biểu diễn chuyển cơ sở (change of basis) $P$ từ $(u_{1}, \dots  , u_{n})$ đến $(v_{1}, \dots  , v_{n})$ theo $U$ và $V$. Indeeed, phương trình
$$v_{j} = \sum_{i=1}^{n}  a_{ij}u_{i}$$

<!-- PAGE 139 -->
Có thể được được biểu diễn trong ma trận tạo thành như
$$v_{j} = UA^{j},$$
Ở đâu
$$A^{j} = \begin{pmatrix} a_{1j} \\ \vdots \\ a_{ij} \\ \vdots \\ a_{n1} \end{pmatrix}$$
Là cột thứ $j$ của $P$, do đó ta thu được
$$V = UP,$$
Mà cho ta
$$P = U^{-1} V.$$
Bây giờ ta mặt painful task của assigning “tốt” ký hiệu incorporating các cơ sở $\mathcal{U} = (u_{1}, \dots  , u_{n})$ và $\mathcal{V} = (v_{1}, \dots  , v_{n})$ vào ký hiệu cho ma trận chuyển cơ sở (change of basis matrix) từ $\mathcal{U}$ đến $\mathcal{V}$. Bởi vì ma trận chuyển cơ sở (change of basis matrix) từ $\mathcal{U}$ đến $\mathcal{V}$ là ma trận của đồng nhất thức ánh xạ $id_{E}$ đối với các cơ sở $\mathcal{V}$ và $\mathcal{U}$ trong rằng thứ tự, ta có thể ký hiệu nó bởi $M_{V,U}(id)$ (Meyer $[129]$ sử dụng ký hiệu $[I]_{V,U})$. Ta ưu tiên để sử dụng abbreviation cho $M_{V,U}(id)$.

> **Định nghĩa 4.4.** ma trận chuyển cơ sở (change of basis matrix) từ $\mathcal{U}$ đến $\mathcal{V}$ được ký hiệu là
$$P_{V,U}.$$
Lưu ý rằng
$$P_{U,V} = P_{V,U}^{-1} .$$
Thì, nếu ta viết $x_{U} = (x_{1}, \dots  , x_{n})$ cho old các tọa độ của $x$ đối với cơ sở (basis) $\mathcal{U}$ và $x_{V} = (x_{1}', \dots  , x_{n}')$ cho mới các tọa độ của $x$ đối với cơ sở (basis) $\mathcal{V}$, ta có
$$x_{U} = P_{V,U} x_{V},x_{V} = P_{V,U}^{-1}  x_{U}.$$
Ở trên có thể nhìn backward, nhưng nhớ rằng ma trận $M_{U,V}(f)$ lấy input được biểu diễn trên cơ sở (basis) $\mathcal{U}$ đến output được biểu diễn trên cơ sở (basis) $\mathcal{V}$. Hệ quả là, $P_{V,U}$ lấy input được biểu diễn trên cơ sở (basis) $\mathcal{V}$ đến output được biểu diễn trên cơ sở (basis) $\mathcal{U}$, và $x_{U} = P_{V,U} x_{V}$ matches điều này điểm của quan điểm!  Beware rằng một số các tác giả (chẳng hạn như Artin $[7])$ định nghĩa ma trận chuyển cơ sở (change of basis matrix) từ $\mathcal{U}$ đến $\mathcal{V}$ như $P_{U,V} = P_{V,U}^{-1}$. Dưới điều này điểm của quan điểm, old cơ sở (basis) $\mathcal{U}$ được biểu diễn theo mới cơ sở (basis) $\mathcal{V}$. Ta tìm điều này bit unnatural. Cũng, trong thực tế, nó dường như rằng mới cơ sở (basis) là thường được biểu diễn theo old cơ sở (basis), thay vì khác cách xung quanh.

<!-- PAGE 140 -->
Vì ma trận $P = P_{V,U}$ các biểu diễn mới cơ sở (basis) $(v_{1}, \dots  , v_{n})$ theo old cơ sở (basis) $(u_{1}, \dots , u_{n})$, ta nhận thấy rằng các tọa độ $(x_{i})$ của vectơ $x$ biến thiên trong opposite hướng của chuyển cơ sở (change of basis). Cho điều này lý do, các vectơ đôi khi được nói là contravariant. Tuy nhiên, điều này biểu thức thực hiện không tạo nghĩa! Thật vậy, vectơ trong nội tại đại lượng rằng không phụ thuộc vào cụ thể cơ sở (basis). Những gì làm cho nghĩa là rằng các tọa độ của vectơ biến thiên trong contravariant cách thức. Cho chúng ta xét một số concrete các ví dụ của thay đổi của các cơ sở.

> **Ví dụ 4.1.** Cho $E = F =\mathbb{R}^{2}$, với $u_{1} = (1, 0), u_{2} = (0, 1), v_{1} = (1, 1)$ và $v_{2} = (-1, 1)$. ma trận chuyển cơ sở (change of basis matrix) $P$ từ cơ sở (basis) $\mathcal{U} = (u_{1}, u_{2})$ đến cơ sở (basis) $\mathcal{V} = (v_{1}, v_{2})$ là
$$P = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$$
Và nghịch đảo của nó là
$$P^{-1}= \begin{pmatrix} 1/2 & 1/2 \\ -1/2 & 1/2 \end{pmatrix} .$$
Old các tọa độ $(x_{1}, x_{2})$ đối với $(u_{1}, u_{2})$ được biểu diễn theo mới các tọa độ $(x_{1}', x_{2}')$ đối với $(v_{1}, v_{2})$ bởi
$$\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} x_{1}' \\ x_{2}' \end{pmatrix} ,$$
Và mới các tọa độ $(x_{1}', x_{2}')$ đối với $(v_{1}, v_{2})$ được biểu diễn theo old các tọa độ $(x_{1}, x_{2})$ đối với $(u_{1}, u_{2})$ bởi
$$\begin{pmatrix} x_{1}' \\ x_{2}' \end{pmatrix} = \begin{pmatrix} 1/2 & 1/2 \\ -1/2 & 1/2 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} .$$

> **Ví dụ 4.2.** Cho $E = F =\mathbb{R}[x]_{3}$ là tập hợp của các đa thức của bậc nhiều nhất $3$, và xét $bases\mathcal{U} = (1, x, x^{2}, x^{3}) and\mathcal{V} = (B_{0}^{3}(x), B_{1}^{3}(x), B_{2}^{3}(x), B_{3}^{3}(x))$, ở đâu $B_{0}^{3}(x), B_{1}^{3}(x), B_{2}^{3}(x), B_{3}^{3}(x)$ là Bernstein các đa thức của bậc $3$, cho trước bởi $B_{0}^{3}(x) = (1$ - $x)^{3} B_{1}^{3}(x) =$ 3(1 - $x)^{2}x B_{2}^{3}(x) =$ 3(1 - $x)x^{2} B_{3}^{3}(x) = x^{3}$. Bởi expanding Bernstein các đa thức, ta tìm rằng ma trận chuyển cơ sở (change of basis matrix) $P_{V,U}$ được cho bởi
$$P_{V,U} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ -3 & 3 & 0 & 0 \\ 3 & -6 & 3 & 0 \\ 1 & 3 & 3 & 1 \end{pmatrix} .$$
$$--$$
Ta cũng tìm rằng nghịch đảo của $P_{V,U}$ là
$$P_{V,U}^{-1}  = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1/3 & 0 & 0 \\ 1 & 2/3 & 1/3 & 0 \\ 1 & 1 & 1 & 1 \end{pmatrix} .$$
