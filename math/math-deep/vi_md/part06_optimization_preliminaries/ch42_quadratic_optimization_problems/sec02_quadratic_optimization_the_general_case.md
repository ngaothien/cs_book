# Tối ưu hóa toàn phương (quadratic optimization): Tổng quát Trường hợp


<!-- PAGE 1553 -->
Sử dụng của Các nhân tử Lagrange (Lagrange multipliers) trong tối ưu hóa và variational các bài tập được thảo luận extensively trong Chương $50$. Bình phương tối thiểu (least squares) các phương pháp và Các nhân tử Lagrange (Lagrange multipliers) được sử dụng đến tackle nhiều các bài tập trong máy tính đồ họa và máy tính thị giác; xem Trucco và Verri $[184]$, Metaxas $[128]$, Jain, Katsuri, và Schunck $[103]$, Faugeras $[60]$, và Foley, van Dam, Feiner, và Hughes $[64]$.

## 42.2 Tối ưu hóa toàn phương (quadratic optimization): Tổng quát Trường hợp

Trong mục này ta đầy đủ study initiated trong Mục 42.1 và cho cần và đủ các điều kiện cho toàn phương $function_{2}^{1} x^{\top}Ax$ - $x^{\top}b$ đến có cực tiểu toàn cục (global minimum). Ta bắt đầu với sau đây đơn giản sự kiện:

> **Mệnh đề 42.4.** Nếu $A$ là khả nghịch ma trận đối xứng (symmetric matrix), thì hàm
$$f(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b$$
Có cực tiểu giá trị khi và chỉ khi $A$ ⪰ $0$, trong mà trường hợp điều này giá trị tối ưu (optimal value) là thu được cho duy nhất giá trị của $x$, cụ thể là $x^{*} = A^{-1}b$, và với
$$f(A^{-1}b) = - \frac{1}{2} b^{\top}A^{-1}b.$$

*Chứng minh.* Nhận thấy rằng
$$\frac{1}{2} (x -A^{-1}b)^{\top}A(x -A^{-1}b) = \frac{1}{2} x^{\top}Ax -x^{\top}b + \frac{1}{2} b^{\top}A^{-1}b.$$
Do đó,
$$f(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b = \frac{1}{2} (x -A^{-1}b)^{\top}A(x -A^{-1}b) - \frac{1}{2} b^{\top}A^{-1}b.$$
Nếu $A$ có một số âm trị riêng (eigenvalue), nói $-\lambda$ (với $\lambda  > 0)$, nếu ta chọn bất kỳ vectơ riêng (eigenvector) $u$ của $A$ liên kết với $\lambda$, thì với mọi $\alpha  \in \mathbb{R}$ với $\alpha  \neq  0$, nếu ta cho $x = \alpha u + A^{-1}b$, khi đó vì Au $= -\lambda u$, ta thu được
$$f(x) = \frac{1}{2} (x -A^{-1}b)^{\top}A(x -A^{-1}b) - \frac{1}{2} b^{\top}A^{-1}b$$
$$= \frac{1}{2} \alpha u^{\top}A\alpha u - \frac{1}{2} b^{\top}A^{-1}b$$
$$= - \frac{1}{2} \alpha^{2} \lambda  \|u\|_{2}^{2} - \frac{1}{2} b^{\top}A^{-1}b,$$
Và vì $\alpha$ có thể được được tạo như lớn như ta muốn và $\lambda  > 0$, ta xem rằng $f$ có không có cực tiểu. Hệ quả là, trong thứ tự cho $f$ đến có cực tiểu, ta phải có $A$ ⪰ $0$. Nếu $A$ ⪰ $0$, vì $A$ là khả nghịch, nó là xác định dương (positive definite), do đó $(x$ - $A^{-1}b)^{\top}A(x$ - $A^{-1}b) > 0$ khi và chỉ khi $x$ - $A^{-1}b \neq  0$, và rõ ràng là cực tiểu giá trị của $f$ là đạt được khi $x$ - $A^{-1}b = 0$, nghĩa là, $x = A^{-1}b$.

<!-- PAGE 1554 -->
Cho chúng ta bây giờ xét trường hợp của tùy ý ma trận đối xứng (symmetric matrix) $A$.

> **Mệnh đề 42.5.** Nếu $A$ là $n \times  n$ ma trận đối xứng (symmetric matrix), thì hàm
$$f(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b$$
Có cực tiểu giá trị khi và chỉ khi $A$ ⪰ $0$ và (I - $AA^{+})b = 0$, trong mà trường hợp điều này cực tiểu giá trị là
$$p^{*}= - \frac{1}{2} b^{\top}A^{+}b.$$
Hơn nữa, nếu $A$ được chéo hóa như $A = U^{\top} \Sigma U$ (với $U$ trực giao), thì giá trị tối ưu (optimal value)
$$\mathbb{R}^{n}$$
Là đạt được bởi tất cả $x \in$ của tạo thành
$$x = A^{+}b + U^{\top} \begin{pmatrix} 0 \\ z \end{pmatrix} ,$$
Với mọi $z \in \mathbb{R}^{n-r}$, ở đâu $r$ là hạng (rank) của $A$.

*Chứng minh.* trường hợp rằng $A$ là khả nghịch được lấy care của theo Mệnh đề 42.4, do đó ta có thể giả sử rằng $A$ là suy biến. Nếu $A$ có hạng (rank) $r < n$, thì ta có thể diagonalize $A$ như
$$A = U^{\top} \begin{pmatrix} \Sigma_{r} & 0 \\ 0 & 0 \end{pmatrix} U,$$
Ở đâu $U$ là ma trận trực giao (orthogonal matrix) và ở đâu $\Sigma_{r}$ là $r \times  r$ đường chéo ma trận khả nghịch (invertible matrix). Thì ta có
$$f(x) = \frac{1}{2} x^{\top}U^{\top} \begin{pmatrix} \Sigma_{r} & 0 \\ 0 & 0 \end{pmatrix} Ux -x^{\top}U^{\top} Ub$$
$$= \frac{1}{2} (Ux)^{\top} \begin{pmatrix} \Sigma_{r} & 0 \\ 0 & 0 \end{pmatrix} Ux -(Ux)^{\top}Ub.$$
Nếu ta viết
$$Ux = \begin{pmatrix} y \\ z \end{pmatrix} andUb = \begin{pmatrix} c \\ d \end{pmatrix} ,$$
$$\mathbb{R}^{r} \mathbb{R}^{n-r}$$
Với $y, c \in$ và $z, d \in$, ta thu được
$$f(x) = \frac{1}{2} (Ux)^{\top} \begin{pmatrix} \Sigma_{r} & 0 \\ 0 & 0 \\  \end{pmatrix} Ux -(Ux)^{\top}Ub$$
$$= \frac{1}{2} (y^{\top}z^{\top}) \begin{pmatrix} \Sigma_{r} & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} y \\ z \end{pmatrix} -(y^{\top}z^{\top}) \begin{pmatrix} c \\ d \end{pmatrix}$$
$$= \frac{1}{2} y^{\top}\Sigma_{r} y -y^{\top}c -z^{\top}d.$$

<!-- PAGE 1555 -->
Cho $y = 0$, ta thu được
$$f(x) = -z^{\top}d,$$
Do đó nếu $d \neq  0$, hàm $f$ có không có cực tiểu. Vì vậy, nếu $f$ có cực tiểu, thì $d = 0$. Tuy nhiên, $d = 0$ có nghĩa là
$$Ub = \begin{pmatrix} c \\ 0 \end{pmatrix} ,$$
Và ta biết từ Mệnh đề 23.5 rằng $b$ là trong miền giá trị (range) của $A$ (ở đây, $U$ là $V^{\top}$), mà là tương đương đến (I - $AA^{+})b = 0$. Nếu $d = 0$, thì
$$f(x) = \frac{1}{2} y^{\top}\Sigma_{r} y -y^{\top}c.$$
$$\mathbb{R}^{r} \mathbb{R}$$
Xét hàm $g: \to$ cho trước bởi
$$g(y) = \frac{1}{2} y^{\top}\Sigma_{r} y -y^{\top}c,y \in \mathbb{R}^{r}.$$
Vì
$$\begin{pmatrix} y \\ z \end{pmatrix} = U^{\top} x$$
Và $U^{\top}$ là khả nghịch (với nghịch đảo $U)$, khi $x$ các miền giá trị (range) trên $\mathbb{R}^{n}, y$ các miền giá trị (range) trên toàn bộ của $\mathbb{R}^{r}$, và vì f(x) $=$ g(y), hàm $f$ có cực tiểu khi và chỉ khi $g$ có cực tiểu. Vì $\Sigma_{r}$ là khả nghịch, theo Mệnh đề 42.4, hàm $g$ có cực tiểu $iff\Sigma_{r}$ ⪰ $0$, mà là tương đương đến $A$ ⪰ $0$. Vì vậy, ta có được chứng minh rằng nếu $f$ có cực tiểu, thì (I - $AA^{+})b = 0$ và $A$ ⪰ $0$. Ngược lại, nếu (I - $AA^{+})b = 0$, thì
$$\begin{pmatrix} I_{r} & 0 \\ 0 & I_{n-r} \end{pmatrix} \begin{pmatrix} \Sigma_{r} & 0 \\ -U^{\top} & 0 & 0 \end{pmatrix} \begin{pmatrix} \Sigma_{r}^{-1} & 0 \\ UU^{\top} & 0 & 0 \end{pmatrix} \begin{pmatrix} U \end{pmatrix} b = \begin{pmatrix} I_{r} & 0 \\ 0 & I_{n-r} \\  \end{pmatrix} \begin{pmatrix} I_{r} & 0 \\ -U^{\top} & 0 & 0 \\  \end{pmatrix} \begin{pmatrix} U \end{pmatrix} b$$
$$= U^{\top} \begin{pmatrix} 0 & 0 \\ 0 & I_{n-r} \end{pmatrix} Ub = 0,$$
Mà suy ra rằng nếu
$$Ub = \begin{pmatrix} c \\ d \end{pmatrix} ,$$
Thì $d = 0$, do đó như ở trên
$$f(x) = g(y) = \frac{1}{2} y^{\top}\Sigma_{r} y -y^{\top}c,$$
Và bởi vì $A$ ⪰ $0$, ta cũng có $\Sigma_{r}$ ⪰ $0$, do đó $g$ và $f$ có cực tiểu. Khi ở trên các điều kiện đúng, vì
$$A = U^{\top} \begin{pmatrix} \Sigma_{r} & 0 \\ 0 & 0 \end{pmatrix} U$$

<!-- PAGE 1556 -->
Là nửa xác định dương (positive semidefinite), nghịch đảo giả (pseudo-inverse) $A^{+}$ của $A$ được cho bởi
$$A^{+}= U^{\top} \begin{pmatrix} \Sigma_{r}^{-1} & 0 \\ 0 & 0 \end{pmatrix} U,$$
Và vì
$$f(x) = g(y) = \frac{1}{2} y^{\top}\Sigma_{r} y -y^{\top}c,$$
Theo Mệnh đề 42.4 cực tiểu của $g$ là đạt được khi và chỉ khi $y^{*} = \Sigma_{r}^{-1}  c$. Vì f(x) là độc lập của $z$, ta có thể chọn $z = 0$, và vì $d = 0$, cho $x^{*}$ cho trước bởi
$$Ux^{*}= \begin{pmatrix} \Sigma_{r}^{-1} c \\ 0 \end{pmatrix} andUb = \begin{pmatrix} c \\ 0 \end{pmatrix} ,$$
Ta suy ra rằng
$$x^{*}= U^{\top} \begin{pmatrix} \Sigma_{r}^{-1} c \\ 0 \end{pmatrix} = U^{\top} \begin{pmatrix} \Sigma_{r}^{-1} & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} c \\ 0 \end{pmatrix} = U^{\top} \begin{pmatrix} \Sigma_{r}^{-1} & 0 \\ 0 & 0 \end{pmatrix} Ub = A^{+}b,(*)$$
Và cực tiểu giá trị của $f$ là
$$f(x^{*}) = \frac{1}{2} (A^{+}b)^{\top}AA^{+}b -b^{\top}A^{+}b = \frac{1}{2} b^{\top}A^{+}AA^{+}b -b^{\top}A^{+}b = - \frac{1}{2} b^{\top}A^{+}b,$$
$$\mathbb{R}^{n}$$
Vì $A^{+}$ là đối xứng và $A^{+}AA^{+} = A^{+}$. Với mọi $x \in$ của tạo thành
$$x = A^{+}b + U^{\top} \begin{pmatrix} 0 \\ z \end{pmatrix} ,z \in \mathbb{R}^{n-r},$$
Vì
$$x = A^{+}b + U^{\top} \begin{pmatrix} 0 \\ z \end{pmatrix} = U^{\top} \begin{pmatrix} \Sigma_{r}^{-1} c \\ 0 \end{pmatrix} + U^{\top} \begin{pmatrix} 0 \\ z \end{pmatrix} = U^{\top} \begin{pmatrix} \Sigma_{r}^{-1} c \\ z \end{pmatrix} ,$$
Và vì f(x) là độc lập của $z$ (bởi vì f(x) $=$ g(y)), ta có
$$f(x) = f(x^{*}) = - \frac{1}{2} b^{\top}A^{+}b.$$
Bài toán của cực tiểu hóa hàm
$$f(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b$$
Trong trường hợp ở đâu ta cộng hoặc tuyến tính các ràng buộc của tạo thành $C^{\top}x = 0$ hoặc afin các ràng buộc
$$\mathbb{R}^{m}$$
Của tạo thành $C^{\top}x = t$ (ở đâu $t \in$ và $t \neq  0)$ ở đâu $C$ là một ma trận cỡ $n \times  m$ có thể được rút gọn đến không ràng buộc trường hợp bằng cách sử dụng Phân rã QR (QR-decomposition) của $C$. Cho chúng ta chỉ ra cách mà đến thực hiện điều này cho tuyến tính các ràng buộc của tạo thành $C^{\top}x = 0$.

<!-- PAGE 1557 -->
Nếu ta sử dụng QR phân rã của $C$, bởi hoán vị các cột của $C$ để tạo sure rằng thứ nhất $r$ các cột của $C$ là độc lập tuyến tính (linearly independent) (ở đâu $r =$ hạng (rank)(C)), ta có thể giả sử rằng
$$C = Q^{\top} \begin{pmatrix} R & S \\ 0 & 0 \end{pmatrix} \Pi ,$$
Ở đâu $Q$ là $n \times  n$ ma trận trực giao (orthogonal matrix), $R$ là $r \times  r$ khả nghịch tam giác trên (upper triangular) ma trận, $S$ là $r \times  (m$ - $r)$ ma trận, và $\Pi$ là hoán vị ma trận $(C$ có hạng (rank) $r)$. Thì nếu ta cho
$$x = Q^{\top} \begin{pmatrix} y \\ z \end{pmatrix} ,$$
$$\mathbb{R}^{r} \mathbb{R}^{n-r}$$
Ở đâu $y \in$ và $z \in$, thì $C^{\top}x = 0$ trở thành
$$C^{\top}x = \Pi^{\top} \begin{pmatrix} R^{\top} & 0 \\ S^{\top} & 0 \end{pmatrix} Qx = \Pi^{\top} \begin{pmatrix} R^{\top} & 0 \\ S^{\top} & 0 \end{pmatrix} \begin{pmatrix} y \\ z \end{pmatrix} = 0,$$
Mà suy ra $y = 0$, và mọi nghiệm của $C^{\top}x = 0$ là của tạo thành
$$x = Q^{\top} \begin{pmatrix} 0 \\ z \end{pmatrix} .$$
Của ta ban đầu bài toán trở thành
$$minimize \frac{1}{2} (y^{\top}z^{\top})QAQ^{\top} \begin{pmatrix} y \\ z \end{pmatrix} + (y^{\top}z^{\top})Qb$$
$$subject toy = 0, y \in \mathbb{R}^{r}, z \in \mathbb{R}^{n-r}.$$
Do đó, ràng buộc $C^{\top}x = 0$ có đã được được đơn giản hóa đến $y = 0$, và nếu ta viết
$$QAQ^{\top}= \begin{pmatrix} G_{11} & G_{12} \\ G_{21} & G_{22} \end{pmatrix} ,$$
Ở đâu $G_{11}$ là một ma trận cỡ $r \times  r$ và $G_{22}$ là $(n$ - $r) \times  (n$ - $r)$ ma trận và
$$Qb = \begin{pmatrix} b_{1} \\ b_{2} \end{pmatrix} ,b_{1} \in \mathbb{R}^{r}, b_{2} \in \mathbb{R}^{n-r},$$
Bài toán của chúng ta trở thành
$$minimize \frac{1}{2} z^{\top}G_{22}z + z^{\top}b_{2},z \in \mathbb{R}^{n-r},$$
Bài toán được giải trong Mệnh đề 42.5. Các ràng buộc của tạo thành $C^{\top}x = t$ (ở đâu $t \neq  0)$ có thể được handled trong đồng dạng cách thức. Trong trường hợp này, ta có thể giả sử rằng $C$ là một ma trận cỡ $n \times  m$ với đầy đủ hạng (rank) (sao cho $m \le n)$ và $t \in \mathbb{R}^{m}$. Thì ta sử dụng Phân rã QR (QR-decomposition) của tạo thành
$$C = P \begin{pmatrix} R \\ 0 \end{pmatrix} ,$$
