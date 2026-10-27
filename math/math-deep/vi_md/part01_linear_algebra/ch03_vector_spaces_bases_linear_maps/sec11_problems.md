# Các bài tập


<!-- PAGE 117 -->
$\bullet$ khái niệm của ánh xạ tuyến tính (linear map). $\bullet$ ảnh (image) Im $f$ (hoặc miền giá trị (range)) của ánh xạ tuyến tính (linear map) $f. \bullet$ hạt nhân (kernel) Ker $f$ (hoặc không gian hạch (nullspace)) của ánh xạ tuyến tính (linear map) $f. \bullet$ hạng (rank) rk(f) của ánh xạ tuyến tính (linear map) $f. \bullet$ ảnh (image) và hạt nhân (kernel) của ánh xạ tuyến tính (linear map) là các không gian con. ánh xạ tuyến tính (linear map) là đơn ánh (injective) khi và chỉ khi hạt nhân (hạt nhân (kernel)) của nó là tầm thường không gian $(0)$ (Mệnh đề 3.19). $\bullet$ duy nhất homomorphic mở rộng tính chất của các ánh xạ tuyến tính (linear maps) đối với các cơ sở (Mệnh đề 3.20). $\bullet$ Các không gian thương. $\bullet$ không gian vectơ (vector space) của các ánh xạ tuyến tính (linear maps) $Hom_{K}(E, F). \bullet$ Các dạng tuyến tính (covectors) và không gian đối ngẫu (dual space) $E^{*}. \bullet$ Tọa độ các dạng. $\bullet$ sự tồn tại của đối ngẫu (dual) các cơ sở (trong hữu hạn số chiều).

## 3.11 Các bài tập

Bài toán 3.1. Cho $H$ là tập hợp của $3 \times  3$ tam giác trên (upper triangular) các ma trận cho trước bởi
$$$$
$$H = \begin{pmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix} | a, b, c \in \mathbb{R}.$$
$$$$
$(1)$ Chứng minh rằng $H$ với nhị phân phép toán của phép nhân ma trận (matrix multiplication) là nhóm; tìm một cách tường minh nghịch đảo của mọi ma trận trong $H$. Là $H$ Abel (giao hoán)?
$(2)$ Cho trước hai các nhóm $G_{1}$ và $G_{2}$, nhắc lại rằng đồng cấu nếu hàm $\phi$: $G_{1} \to G_{2}$ sao cho
$$\phi (ab) = \phi (a)\phi (b),a, b \in G_{1}.$$
Chứng minh rằng $\phi (e_{1}) = e_{2}$ (ở đâu $e_{i}$ là phần tử đơn vị (identity element) của $G_{i})$ và rằng
$$\phi (a^{-1}) = (\phi (a))^{-1},a \in G_{1}.$$
$(3)$ Cho $S^{1}$ là unit đường tròn, nghĩa là
$$S^{1}= {e^{i\theta}= \cos \theta  + i \sin \theta  | 0 \le \theta  < 2\pi },$$

<!-- PAGE 118 -->
Và cho $\phi$ là hàm cho trước bởi
$$\phi \begin{pmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{pmatrix} = (a, c, e^{ib}).$$
Chứng minh rằng $\phi$ là toàn ánh (surjective) hàm lên $G = \mathbb{R} \times  \mathbb{R} \times  S^{1}$, và rằng nếu ta định nghĩa phép nhân trên tập hợp này bởi
$$(x_{1}, y_{1}, u_{1}) \cdot  (x_{2}, y_{2}, u_{2}) = (x_{1} + x_{2}, y_{1} + y_{2}, e^{ix1y2}u_{1}u_{2}),$$
Thì $G$ là nhóm và $\phi$ là đồng cấu nhóm (group homomorphism) từ $H$ lên $G$.
$(4)$ hạt nhân (kernel) của đồng cấu $\phi$: $G_{1} \to G_{2}$ được định nghĩa như
$$\mathrm{Ker} (\phi ) = {a \in G_{1} | \phi (a) = e_{2}}.$$
Tìm một cách tường minh hạt nhân (kernel) của $\phi$ và chỉ ra rằng nó là nhóm con của $H$.
Bài toán 3.2. Với mọi $m \in \mathbb{Z}$ với $m > 0$, tập con $m\mathbb{Z} = {mk$ | $k \in \mathbb{Z}}$ là Abel nhóm con của $\mathbb{Z}$. Kiểm tra điều này.
$(1)$ Cho đẳng cấu nhóm (group isomorphism) (khả nghịch đồng cấu) từ $m\mathbb{Z}$ đến $\mathbb{Z}$.
$(2)$ Kiểm tra rằng inclusion ánh xạ $i: m\mathbb{Z} \to \mathbb{Z}$ cho trước bởi i(mk) $=$ mk là đồng cấu nhóm (group homomorphism). Chứng minh rằng nếu $m \ge 2$ thì không có đồng cấu nhóm (group homomorphism) $p: \mathbb{Z} \to m\mathbb{Z}$ sao cho $p \circ i =$ id.
Nhận xét: ở trên chỉ ra rằng các nhóm Abel thất bại đến có một số của các tính chất của các không gian vectơ. Ta sẽ chỉ ra sau này rằng ánh xạ tuyến tính (linear map) thỏa mãn điều kiện $p\circ i =$ id luôn luôn tồn tại.
Bài toán 3.3. Cho $E =\mathbb{R} \times \mathbb{R}$, và định nghĩa phép cộng phép toán
$$(x_{1}, y_{1}) + (x_{2}, y_{2}) = (x_{1} + x_{2}, y_{1}, +y_{2}),x_{1}, x_{2}, y_{1}, y_{2} \in \mathbb{R},$$
Và phép toán nhân $\cdot$: $\mathbb{R} \times  E \to E$ bởi
$$\lambda  \cdot  (x, y) = (\lambda x, y),\lambda , x, y \in \mathbb{R}.$$
Chỉ ra rằng $E$ với ở trên các phép toán $+$ và $\cdot$ là không không gian vectơ (vector space). Mà của axioms là violated?
Bài toán 3.4. $(1)$ Chứng minh rằng axioms của các không gian vectơ suy ra rằng
$$\alpha  \cdot  0 = 0$$
$$0 \cdot  v = 0$$
$$\alpha  \cdot  (-v) = -(\alpha  \cdot  v)$$
$$(-\alpha ) \cdot  v = -(\alpha  \cdot  v),$$

<!-- PAGE 119 -->
Với mọi $v \in E$ và tất cả $\alpha  \in K$, ở đâu $E$ là không gian vectơ (vector space) trên $K$.
$(2)$ Với mọi $\lambda  \in \mathbb{R}$ và mọi $x = (x_{1}, \dots  , x_{n}) \in \mathbb{R}^{n}$, định nghĩa $\lambda x$ bởi
$$\lambda x = \lambda (x_{1}, \dots  , x_{n}) = (\lambda x_{1}, \dots  , \lambda x_{n}).$$
$$\mathbb{R}^{n}$$
Nhắc lại rằng mọi vectơ $x = (x_{1}, \dots  , x_{n}) \in$ có thể được được viết một cách duy nhất như
$$x = x_{1}e_{1} + \cdots  + x_{n}e_{n},$$
$$\mathbb{R}\mathbb{R}^{n}$$
Ở đâu $e_{i} = (0, \dots  , 0, 1, 0, \dots  , 0)$, với đơn lẻ $1$ trong position $i$. Với mọi phép toán $\cdot$: $\times \to \mathbb{R}^{n}$, nếu $\cdot$ thỏa mãn Axiom (V1) của không gian vectơ (vector space), thì chứng minh rằng với mọi $\alpha  \in \mathbb{R}$, ta có
$$\alpha  \cdot  x = \alpha  \cdot  (x_{1}e_{1} + \cdots  + x_{n}e_{n}) = \alpha  \cdot  (x_{1}e_{1}) + \cdots  + \alpha  \cdot  (x_{n}e_{n}).$$
Kết luận rằng $\cdot$ là hoàn toàn được xác định bởi của nó action trên một chiều các không gian con của $\mathbb{R}^{n}$ được sinh (spanned) bởi $e_{1}, \dots  , e_{n}$.
$$\mathbb{R}\mathbb{R}^{n} \mathbb{R}^{n}$$
$(3)$ Sử dụng $(2)$ để định nghĩa các phép toán $\cdot$: $\times \to$ rằng thỏa mãn Axioms (V1–V3), nhưng cho mà Axiom V4 không thỏa mãn.
$$\mathbb{R}\mathbb{R}^{n} \mathbb{R}^{n}$$
$(4)$ Với mọi phép toán $\cdot$: $\times \to$, chứng minh rằng nếu $\cdot$ thỏa mãn Axioms (V2–V3), thì với mọi hữu tỷ số $r \in \mathbb{Q}$ và mọi vectơ $x \in \mathbb{R}^{n}$, ta có
$$r \cdot  x = r(1 \cdot  x).$$
$$\mathbb{R}^{n}$$
Trong ở trên phương trình, $1 \cdot  x$ là một số vectơ $(y_{1}, \dots  , y_{n}) \in$ không nhất thiết bằng $x = (x_{1}, \dots  , x_{n})$, và
$$r(1 \cdot  x) = (ry_{1}, \dots  , ry_{n}),$$
Như trong Phần $(2)$.
$$\mathbb{Q}\mathbb{R}^{n} \mathbb{R}^{n}$$
Sử dụng $(4)$ để kết luận rằng bất kỳ phép toán $\cdot$: $\times \to$ rằng thỏa mãn Axioms (V1–V3)
$$\mathbb{R}^{n}$$
Là hoàn toàn được xác định bởi action của $1$ trên một chiều các không gian con của được sinh (spanned) bởi $e_{1}, \dots  , e_{n}$.
Bài toán 3.5. Cho $A_{1}$ là sau đây ma trận:
$$A_{1} = \begin{pmatrix} 2 & 3 & 1 \\ 1 & 2 & -1 \\ 3 & 5 & 1 \end{pmatrix} .$$
$$--$$
Chứng minh rằng các cột của $A_{1}$ là độc lập tuyến tính (linearly independent). Tìm các tọa độ của vectơ $x = (6, 2, -7)$ trên cơ sở (basis) bao gồm của các vectơ cột của $A_{1}$.
Bài toán 3.6. Cho $A_{2}$ là sau đây ma trận:
$$A_{2} = \begin{pmatrix} 1 & 2 & 1 & 1 \\ 2 & 3 & 2 & 3 \\ -1 & 0 & 1 & -1 \\ 2 & 1 & 3 & 0 \end{pmatrix} .$$
$$--$$
Biểu diễn thứ tư cột của $A_{2}$ như tổ hợp tuyến tính (linear combination) của thứ nhất ba các cột của $A_{2}$. Là vectơ $x = (7, 14, -1, 2)$ tổ hợp tuyến tính (linear combination) của các cột của $A_{2}$?

<!-- PAGE 120 -->
Bài toán 3.7. Cho $A_{3}$ là sau đây ma trận:
$$A_{3} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 2 \\ 1 & 2 & 3 \end{pmatrix} .$$
Chứng minh rằng các cột của $A_{1}$ là độc lập tuyến tính (linearly independent). Tìm các tọa độ của vectơ $x = (6, 9, 14)$ trên cơ sở (basis) bao gồm của các vectơ cột của $A_{3}$.
Bài toán 3.8. Cho $A_{4}$ là sau đây ma trận:
$$A_{4} = \begin{pmatrix} 1 & 2 & 1 & 1 \\ 2 & 3 & 2 & 3 \\ -1 & 0 & 1 & -1 \\ 2 & 1 & 4 & 0 \end{pmatrix} .$$
$$--$$
Chứng minh rằng các cột của $A_{4}$ là độc lập tuyến tính (linearly independent). Tìm các tọa độ của vectơ $x = (7, 14, -1, 2)$ trên cơ sở (basis) bao gồm của các vectơ cột của $A_{4}$.
Bài toán 3.9. Xét sau đây Haar ma trận
$$H = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 1 & -1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & 0 & 1 \end{pmatrix} .$$
$$--$$
Chứng minh rằng các cột của $H$ là độc lập tuyến tính (linearly independent). Hint. Tính tích $H^{\top}H$.
Bài toán 3.10. Xét sau đây Ma trận Hadamard (Hadamard matrix)
$$H_{4} = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & -1 & 1 & -1 \\ 1 & 1 & -1 & -1 \\ 1 & 1 & 1 & 1 \end{pmatrix} .$$
$$--$$
Chứng minh rằng các cột của $H_{4}$ là độc lập tuyến tính (linearly independent). Hint. Tính tích $H_{4}^{\top} H_{4}$.
Bài toán 3.11. Trong việc giải bài toán này, thực hiện không sử dụng các định thức.
$(1)$ Cho $(u_{1}, \dots  , u_{m})$ và $(v_{1}, \dots  , v_{m})$ là hai các họ của các vectơ trong một số không gian vectơ (vector space) $E$. Giả sử rằng mỗi $v_{i}$ là tổ hợp tuyến tính (linear combination) của $u_{j}s$, sao cho
$$v_{i} = a_{i1}u_{1} + \cdots  + a_{i m}u_{m},1 \le i \le m,$$

<!-- PAGE 121 -->
Và rằng ma trận $A = (a_{i j})$ là tam giác trên (upper-triangular) ma trận, mà có nghĩa là nếu $1 \le j < i \le m$, thì $a_{i j} = 0$. Chứng minh rằng nếu $(u_{1}, \dots  , u_{m})$ là độc lập tuyến tính (linearly independent) và nếu tất cả đường chéo các phần tử (entries) của $A$ là khác không, thì $(v_{1}, \dots  , v_{m})$ là cũng độc lập tuyến tính (linearly independent). Hint. Sử dụng quy nạp trên $m$.
$(2)$ Cho $A = (a_{i j})$ là tam giác trên (upper-triangular) ma trận. Chứng minh rằng nếu tất cả đường chéo các phần tử (entries) của $A$ là khác không, thì $A$ là khả nghịch và nghịch đảo $A^{-1}$ của $A$ là cũng tam giác trên (upper-triangular). Hint. Sử dụng quy nạp trên $m$. Chứng minh rằng nếu $A$ là khả nghịch, thì tất cả đường chéo các phần tử (entries) của $A$ là khác không.
$(3)$ Chứng minh rằng nếu các họ $(u_{1}, \dots  , u_{m})$ và $(v_{1}, \dots  , v_{m})$ là related như trong $(1)$, thì $(u_{1}, \dots  , u_{m})$ là độc lập tuyến tính (linearly independent) $iff(v_{1}, \dots  , v_{m})$ là độc lập tuyến tính (linearly independent).
Bài toán 3.12. Trong việc giải bài toán này, thực hiện không sử dụng các định thức. Xét ma trận cỡ $n \times  n$
$$A = \begin{pmatrix} 1 & 2 & 0 & 0 & \dots & 0 & 0 \\ 0 & 1 & 2 & 0 & \dots & 0 & 0 \\ 0 & 0 & 1 & 2 & \dots & 0 & 0 \\ \vdots & \vdots & \ddots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & \dots & 0 & 1 & 2 & 0 \\ 0 & 0 & \dots & 0 & 0 & 1 & 2 \\ 0 & 0 & \dots & 0 & 0 & 0 & 1 \end{pmatrix} .$$
$(1)$ Tìm nghiệm $x = (x_{1}, \dots  , x_{n})$ của hệ phương trình tuyến tính
$$Ax = b,$$
Cho
$$b = \begin{pmatrix} b_{1} \\ b_{2} \\ \vdots \\ b_{n} \end{pmatrix} .$$
$(2)$ Chứng minh rằng ma trận $A$ là khả nghịch và tìm của nó nghịch đảo $A^{-1}$. Cho trước rằng số của atoms trong universe là estimated là $\le 10^{82}$, compare kích thước của các hệ số nghịch đảo của $A$ đến $10^{82}$, nếu $n \ge 300$.
$(3)$ Giả sử $b$ là perturbed bởi nhỏ lượng $\delta b$ (lưu ý rằng $\delta b$ là vectơ). Tìm mới nghiệm của hệ
$$A(x + \delta x) = b + \delta b,$$
Ở đâu $\delta x$ là cũng vectơ. Trong trường hợp ở đâu $b = (0, \dots  , 0, 1)$, và $\delta b = (0, \dots  , 0, \epsilon$), chỉ ra rằng
$$|(\delta x)_{1}| = 2^{n-1}|\epsilon |.$$

<!-- PAGE 122 -->
(ở đâu $(\delta x)_{1}$ là thành phần thứ nhất của $\delta x)$.
$(4)$ Chứng minh rằng $(A$ - $I)^{n} = 0$.
Bài toán 3.13. một ma trận cỡ $n \times  n$ $N$ là lũy linh (nilpotent) nếu tồn tại một số nguyên $r \ge 1$ sao cho $N^{r} = 0$.
$(1)$ Chứng minh rằng nếu $N$ là lũy linh (nilpotent) ma trận, thì ma trận $I$ - $N$ là khả nghịch và
$$(I -N)^{-1}= I + N + N^{2}+ \cdots  + N^{r-1}.$$
$(2)$ Tính nghịch đảo của sau đây ma trận $A$ bằng cách sử dụng $(1)$:
$$A = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 0 & 1 & 2 & 3 & 4 \\ 0 & 0 & 1 & 2 & 3 \\ 0 & 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix} .$$
Bài toán 3.14. $(1)$ Cho $A$ là một ma trận cỡ $n \times  n$. Nếu $A$ là khả nghịch, chứng minh rằng với mọi $x \in \mathbb{R}^{n}$, nếu Ax $= 0$, thì $x = 0$.
$(2)$ Cho $A$ là một ma trận cỡ $m \times  n$ và cho $B$ là một ma trận cỡ $n \times  m$. Chứng minh rằng $I_{m}$ - $AB$ là khả nghịch khi và chỉ khi $I_{n}$ - $BA$ là khả nghịch. Hint. Nếu với mọi $x \in \mathbb{R}^{n}$, Mx $= 0$ suy ra rằng $x = 0$, thì $M$ là khả nghịch.
Bài toán 3.15. Xét sau đây $n \times  n$ ma trận, cho $n \ge 3$:
$$B = \begin{pmatrix} 1 & -1 & -1 & -1 & \cdots & -1 & -1 \\ 1 & -1 & 1 & 1 & \cdots & 1 & 1 \\ 1 & 1 & -1 & 1 & \cdots & 1 & 1 \\ 1 & 1 & 1 & -1 & \cdots & 1 & 1 \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ 1 & 1 & 1 & 1 & \cdots & -1 & 1 \\ 1 & 1 & 1 & 1 & \cdots & 1 & -1 \end{pmatrix}$$
$(1)$ Nếu ta ký hiệu các cột của $B$ bởi $b_{1}, \dots  , b_{n}$, chứng minh rằng
$$(n -3)b_{1} -(b_{2} + \cdots  + b_{n}) = 2(n -2)e_{1}$$
$$b_{1} -b_{2} = 2(e_{1} + e_{2})$$
$$b_{1} -b_{3} = 2(e_{1} + e_{3})$$
$$\vdots \vdots$$
$$b_{1} -b_{n} = 2(e_{1} + e_{n}),$$

<!-- PAGE 123 -->
Ở đâu $e_{1}, \dots  , e_{n}$ là cơ sở chính tắc (canonical basis) các vectơ của $\mathbb{R}^{n}$.
$(2)$ Chứng minh rằng $B$ là khả nghịch và rằng của nó nghịch đảo $A = (a_{ij})$ được cho bởi
$$-$$
$$a_{11} = \frac{(n3)}{2(n -2)} ,a_{i1} = - \frac{1}{2(n -2)} 2 \le i \le n$$
Và
$$-$$
$$a_{ii} = - \frac{(n3)}{2(n -2)} ,2 \le i \le n$$
$$a_{ji} = \frac{1}{2(n -2)} ,2 \le i \le n, j \neq  i.$$
$(3)$ Chỉ ra rằng $n$ đường chéo $n \times  n$ các ma trận $D_{i}$ được định nghĩa sao cho đường chéo các phần tử (entries) của $D_{i}$ là bằng nhau các phần tử (entries) (từ đỉnh/trên xuống) của cột thứ $i$ của $B$ tạo thành cơ sở (basis) của không gian của $n \times  n$ các ma trận đường chéo (các ma trận với các không điểm everywhere ngoại trừ có thể trên đường chéo). Ví dụ, khi $n = 4$, ta có
$$D_{1} = ,$$
$$\begin{pmatrix} 1 & 0 & 0 & 0 & -1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & -1 & 0 & 0 \\ 0 & 0 & 1 & 0 & D_{2}=0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 \\ -1 & 0 & 0 & 0 & -1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & -1 & 0, & D_{4}=0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 \end{pmatrix}$$
$$D_{3} = .$$
$$-$$
Bài toán 3.16. Cho trước bất kỳ ma trận cỡ $m\times n$ $A$ và bất kỳ ma trận cỡ $n\times p$ $B$, nếu ta ký hiệu các cột của $A$ bởi $A^{1}, \dots  , A^{n}$ và các hàng của $B$ bởi $B_{1}, \dots  , B_{n}$, chứng minh rằng
$$AB = A^{1}B_{1} + \cdots  + A^{n}B_{n}.$$
Bài toán 3.17. Cho $f$: $E \to F$ là ánh xạ tuyến tính (linear map) mà là cũng song ánh (nó là đơn ánh (injective) và toàn ánh (surjective)). Chứng minh rằng nghịch đảo hàm $f^{-1}: F \to E$ là tuyến tính.
Bài toán 3.18. Cho trước hai các vectơ các không gian $E$ và $F$, cho $(u_{i})_{i\in I}$ là bất kỳ cơ sở (basis) của $E$ và cho $(v_{i})_{i\in I}$ là bất kỳ họ của các vectơ trong $F$. Chứng minh rằng duy nhất ánh xạ tuyến tính (linear map) $f$: $E \to F$ sao cho $f(u_{i}) = v_{i}$ với mọi $i \in$ I là toàn ánh (surjective) $iff(v_{i})_{i\in I}$ sinh ra $F$.
Bài toán 3.19. Cho $f$: $E \to F$ là ánh xạ tuyến tính (linear map) với dim(E) $= n$ và dim(F) $= m$. Chứng minh rằng $f$ có hạng (rank) $1$ khi và chỉ khi $f$ được biểu diễn bởi một ma trận cỡ $m \times  n$ của tạo thành
$$A = uv^{\top}$$
Với $u$ khác không vectơ cột (column vector) có số chiều $m$ và $v$ khác không vectơ cột (column vector) có số chiều $n$.

<!-- PAGE 124 -->
Bài toán 3.20. Tìm không tầm thường sự phụ thuộc tuyến tính (linear dependence) trong số các dạng tuyến tính $\phi_{1} (x, y, z) =$ 2x - $y +$ 3z, $\phi_{2} (x, y, z) =$ 3x - 5y $+ z, \phi_{3} (x, y, z) =$ 4x - 7y $+ z$.
Bài toán 3.21. Chứng minh rằng các dạng tuyến tính $\phi_{1} (x, y, z) = x +$ 2y $+ z, \phi_{2} (x, y, z) =$ 2x $+$ 3y $+$ 3z, $\phi_{3} (x, y, z) =$ 3x $+$ 7y $+ z$ là độc lập tuyến tính (linearly independent). Biểu diễn dạng tuyến tính (linear form) $\phi (x, y, z) = x+y+z$ như tổ hợp tuyến tính (linear combination) của $\phi_{1} , \phi_{2} , \phi_{3}$.
