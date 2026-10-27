# Cực đại hóa Toàn phương Hàm trên Unit Mặt cầu


<!-- PAGE 1558 -->
Ở đâu $P$ là trực giao $n\times n$ ma trận và $R$ là $m\times m$ khả nghịch tam giác trên (upper triangular) ma trận. Nếu ta viết
$$x = P \begin{pmatrix} y \\ z \end{pmatrix} ,$$
$$\mathbb{R}^{m} \mathbb{R}^{n-m}$$
Ở đâu $y \in$ và $z \in$, phương trình $C^{\top}x = t$ trở thành
$$(R^{\top}0)P^{\top} x = t,$$
Rằng là,
$$(R^{\top}0) \begin{pmatrix} y \\ z \end{pmatrix} = t,$$
Mà cho ta
$$R^{\top}y = t.$$
Vì $R$ là khả nghịch, ta thu được $y = (R^{\top})^{-1}t$, và thì nó là dễ để xem rằng của ta ban đầu bài toán rút gọn đến không ràng buộc bài toán theo ma trận $P^{\top}$ AP; chi tiết là để lại như một bài tập.

## 42.3 Cực đại hóa Toàn phương Hàm trên

$$Unit Sphere$$
Trong mục này ta thảo luận khác nhau tối ưu hóa toàn phương (quadratic optimization) các bài tập một cách hầu hết phát sinh từ máy tính thị giác (ảnh (image) segmentation và contour nhóm). các bài tập này có thể được rút gọn đến sau đây cơ bản tối ưu hóa bài toán: cho trước $n \times  n$ thực ma trận đối xứng (symmetric matrix) $A$
$$maximizex^{\top}Ax$$
$$subject tox^{\top}x = 1, x \in \mathbb{R}^{n}.$$
Xét theo Mệnh đề 23.10, cực đại giá trị của $x^{\top}Ax$ trên unit mặt cầu bằng lớn nhất trị riêng (eigenvalue) $\lambda_{1}$ của ma trận $A$, và nó là đạt được với mọi unit vectơ riêng (eigenvector) $u_{1}$ liên kết với $\lambda_{1}$. Tương tự, cực tiểu giá trị của $x^{\top}Ax$ trên unit mặt cầu bằng nhỏ nhất trị riêng (eigenvalue) $\lambda_{n}$ của ma trận $A$, và nó là đạt được với mọi unit vectơ riêng (eigenvector) $u_{n}$ liên kết với $\lambda_{n}$. biến thể của ở trên bài toán thường encountered trong máy tính thị giác bao gồm trong cực tiểu hóa $x^{\top}Ax$ trên ellipsoid cho trước bởi phương trình của tạo thành
$$x^{\top}Bx = 1,$$
Ở đâu $B$ là đối xứng xác định dương (SPD) ma trận. Vì $B$ là xác định dương (positive definite), nó có thể được được chéo hóa như
$$B = QDQ^{\top},$$

<!-- PAGE 1559 -->
Ở đâu $Q$ là ma trận trực giao (orthogonal matrix) và $D$ là ma trận đường chéo (diagonal matrix),
$$D = \mathrm{diag}(d_{1}, \dots  , d_{n}),$$
Với $d_{i} > 0$, cho $i = 1, \dots  , n$. Nếu ta định nghĩa các ma trận $B^{1/2}$ và $B^{-1/2}$ bởi
$$B^{1/2}= Q \mathrm{diag} \begin{pmatrix} p\overline{d}_{1}, \dots  ,p\overline{d}_{n} \end{pmatrix} Q^{\top}$$
Và
$$B^{-1/2}= Q \mathrm{diag} \begin{pmatrix} 1/p\overline{d}_{1}, \dots  , 1/p\overline{d}_{n} \end{pmatrix} Q^{\top},$$
Rõ ràng là các ma trận này là đối xứng, rằng $B^{-1/2}BB^{-1/2} =$ I, và rằng $B^{1/2}$ và $B^{-1/2}$ là mutual các nghịch đảo. Thì nếu ta tạo thay đổi của biến
$$x = B^{-1/2}y,$$
Phương trình $x^{\top}Bx = 1$ trở thành $y^{\top}y = 1$, và tối ưu hóa bài toán
$$minimizex^{\top}Ax$$
$$subject tox^{\top}Bx = 1, x \in \mathbb{R}^{n},$$
Là tương đương đến bài toán
$$minimizey^{\top}B^{-1/2}AB^{-1/2}y$$
$$subject toy^{\top}y = 1, y \in \mathbb{R}^{n},$$
Ở đâu $y = B^{1/2}x$ và $B^{-1/2}AB^{-1/2}$ là đối xứng. phức phiên bản của của ta cơ bản tối ưu hóa bài toán trong mà $A$ là Ma trận Hermite (Hermitian matrix) cũng phát sinh trong máy tính thị giác. Cụ thể là, cho trước $n \times  n$ phức Ma trận Hermite (Hermitian matrix) $A$,
$$maximizex^{*}Ax$$
$$subject tox^{*}x = 1, x \in \mathbb{C}^{n}.$$
Một lần nữa theo Mệnh đề 23.10, cực đại giá trị của $x^{*}Ax$ trên unit mặt cầu bằng lớn nhất trị riêng (eigenvalue) $\lambda_{1}$ của ma trận $A$, và nó là đạt được với mọi unit vectơ riêng (eigenvector) $u_{1}$ liên kết với $\lambda_{1}$.
Nhận xét: Nó là worth điểm ra rằng nếu $A$ là ma trận phản Hermite (skew-Hermitian matrix), nghĩa là, nếu $A^{*} = -A$, thì $x^{*}Ax$ là thuần túy imaginary hoặc không. Thật vậy, vì $z = x^{*}Ax$ là vô hướng (scalar), ta có $z^{*} =\overline{z}$ (liên hợp của $z)$, do đó ta có
$$\overline{x}^{*}\overline{Ax} = (x^{*}Ax)^{*}= x^{*}A^{*}x = -x^{*}Ax,$$
Do đó $\overline{x}^{*}\overline{Ax} + x^{*}Ax = 2Re(x^{*}Ax) = 0$, mà có nghĩa là $x^{*}Ax$ là thuần túy imaginary hoặc không.

<!-- PAGE 1560 -->
Đặc biệt, nếu $A$ là thực ma trận và nếu $A$ là phản đối xứng, thì
$$x^{\top}Ax = 0.$$
Do đó, với mọi thực ma trận (đối xứng hoặc không),
$$x^{\top}Ax = x^{\top}H(A)x,$$
Ở đâu H() $= (A + A^{\top})/2$, đối xứng phần của $A$. Có các tình huống trong mà nó là cần đến cộng tuyến tính các ràng buộc đến bài toán của cực đại hóa toàn phương hàm trên mặt cầu. bài toán này đã là hoàn toàn được giải bởi Golub $[81] (1973)$. bài toán là sau đây: cho trước $n \times  n$ thực ma trận đối xứng (symmetric matrix) $A$ và một ma trận cỡ $n \times  p$ $C$,
$$minimizex^{\top}Ax$$
$$subject tox^{\top}x = 1, C^{\top}x = 0, x \in \mathbb{R}^{n}.$$
Như trong Mục 42.2, Golub chỉ ra rằng tuyến tính ràng buộc $C^{\top}x = 0$ có thể được được khử như sau: nếu ta sử dụng QR phân rã của $C$, bởi hoán vị các cột, ta có thể giả sử rằng
$$C = Q^{\top} \begin{pmatrix} R & S \\ 0 & 0 \end{pmatrix} \Pi ,$$
Ở đâu $Q$ là trực giao $n\times n$ ma trận, $R$ là $r \times r$ khả nghịch tam giác trên (upper triangular) ma trận, và $S$ là $r \times  (p$ - $r)$ ma trận (giả sử $C$ có hạng (rank) $r)$. Nếu ta cho
$$x = Q^{\top} \begin{pmatrix} y \\ z \end{pmatrix} ,$$
$$\mathbb{R}^{r} \mathbb{R}^{n-r}$$
Ở đâu $y \in$ và $z \in$, thì $C^{\top}x = 0$ trở thành
$$\Pi^{\top} \begin{pmatrix} R^{\top} & 0 \\ S^{\top} & 0 \end{pmatrix} Qx = \Pi^{\top} \begin{pmatrix} R^{\top} & 0 \\ S^{\top} & 0 \end{pmatrix} \begin{pmatrix} y \\ z \end{pmatrix} = 0,$$
Mà suy ra $y = 0$, và mọi nghiệm của $C^{\top}x = 0$ là của tạo thành
$$x = Q^{\top} \begin{pmatrix} 0 \\ z \end{pmatrix} .$$
Của ta ban đầu bài toán trở thành
$$minimize(y^{\top}z^{\top})QAQ^{\top} \begin{pmatrix} y \\ z \end{pmatrix}$$
$$subject toz^{\top}z = 1, z \in \mathbb{R}^{n-r},$$
$$y = 0, y \in \mathbb{R}^{r}.$$

<!-- PAGE 1561 -->
Do đó ràng buộc $C^{\top}x = 0$ có đã được được đơn giản hóa đến $y = 0$, và nếu ta viết
$$QAQ^{\top}= \begin{pmatrix} G_{11} & G_{12} \\ G_{12}^{\top} & G_{22} \end{pmatrix} ,$$
Bài toán của chúng ta trở thành
$$minimizez^{\top}G_{22}z$$
$$subject toz^{\top}z = 1, z \in \mathbb{R}^{n-r},$$
Tiêu chuẩn trị riêng (eigenvalue) bài toán.
Nhận xét: Có một cách của việc tìm các trị riêng (eigenvalues) của $G_{22}$ mà thực hiện không đòi hỏi QRfactorization của $C$. Nhận thấy rằng nếu ta cho
$$J = \begin{pmatrix} 0 & 0 \\ 0 & I_{n-r} \end{pmatrix} ,$$
Thì
$$JQAQ^{\top}J = \begin{pmatrix} 0 & 0 \\ 0 & G_{22} \end{pmatrix} ,$$
Và nếu ta tập hợp
$$P = Q^{\top}JQ,$$
Thì
$$PAP = Q^{\top}JQAQ^{\top}JQ.$$
Bây giờ, $Q^{\top}JQAQ^{\top}JQ$ và $JQAQ^{\top}J$ có cùng các trị riêng (eigenvalues), do đó PAP và $JQAQ^{\top}J$ cũng có cùng các trị riêng (eigenvalues). Suy ra rằng các nghiệm của của ta tối ưu hóa bài toán là trong số các trị riêng (eigenvalues) của $K = PAP$, và ít nhất $r$ của những phần tử đó là $0$. Bằng cách sử dụng sự kiện rằng $CC^{+}$ là phép chiếu lên miền giá trị (range) của $C$, ở đâu $C^{+}$ là nghịch đảo giả (pseudo-inverse) của $C$, nó có thể cũng được hiển thị rằng
$$P = I -CC^{+},$$
Phép chiếu lên hạt nhân (kernel) của $C^{\top}$. Do đó $P$ có thể được được tính một cách trực tiếp theo $C$. Đặc biệt, khi $n \ge p$ và $C$ có đầy đủ hạng (rank) (các cột của $C$ là độc lập tuyến tính (linearly independent)), thì ta biết rằng $C^{+} = (C^{\top}C)^{-1}C^{\top}$ và
$$P = I -C(C^{\top}C)^{-1}C^{\top}.$$
Sự kiện này được sử dụng bởi Cour và Shi $[42]$ và một cách ẩn bởi Yu và Shi $[198]$. bài toán của cộng afin các ràng buộc của tạo thành $N^{\top} x = t$, ở đâu $t \neq  0$, cũng đến lên trong thực tế. Tại thứ nhất glance, bài toán này có thể không dường như khó hơn hơn tuyến tính bài toán trong mà $t = 0$, nhưng nó là. bài toán này đã là extensively studied trong paper bởi Gander, Golub, và von Matt $[78] (1989)$.

<!-- PAGE 1562 -->
Gander, Golub, và von Matt xét sau đây bài toán: Cho trước $(n+m)\times (n+m)$ thực ma trận đối xứng (symmetric matrix) $A$ (với $n > 0)$, một ma trận cỡ $(n+m)\times m$ $N$ với đầy đủ hạng (rank), và khác không
$$\mathbb{R}^{m}



$<$$$ vector $t \in$ with $(N^{\đỉnh/trên})^{+}t 1$ (where $(N^{\đỉnh/trên})^{+}$ denotes the pseudo-inverse of $N^{\đỉnh/trên})$,
$$minimizex^{\top}Ax$$
$$subject tox^{\top}x = 1, N^{\top} x = t, x \in \mathbb{R}^{n+m}.$$
Điều kiện

$(N^{\top})^{+}t$

$< 1$ các đảm bảo rằng bài toán có nghiệm và là không tầm thường. các tác giả bắt đầu bởi chứng minh rằng afin ràng buộc $N^{\top} x = t$ có thể được được khử. Một cách đến thực hiện do đó là để sử dụng QR phân rã của $N$. Nếu
$$N = P \begin{pmatrix} R \\ 0 \end{pmatrix} ,$$
Ở đâu $P$ là trực giao $(n + m) \times  (n + m)$ ma trận và $R$ là $m \times  m$ khả nghịch tam giác trên (upper triangular) ma trận, thì nếu ta nhận thấy rằng
$$x^{\top}Ax = x^{\top}PP^{\top} APP^{\top} x,$$
$$N^{\top} x = (R^{\top}0)P^{\top} x = t,$$
$$x^{\top}x = x^{\top}PP^{\top} x = 1,$$
Và nếu ta viết
$$P^{\top} AP = \begin{pmatrix} B & \Gamma^{\top} \\ \Gamma & C \end{pmatrix} ,$$
Ở đâu $B$ là $m \times  m$ ma trận đối xứng (symmetric matrix), $C$ là $n \times  n$ ma trận đối xứng (symmetric matrix), $\Gamma$ là một ma trận cỡ $m \times  n$, và
$$P^{\top} x = \begin{pmatrix} y \\ z \end{pmatrix} ,$$
$$\mathbb{R}^{m} \mathbb{R}^{n}$$
Với $y \in$ và $z \in$, ta thì thu được
$$x^{\top}Ax = y^{\top}By + 2z^{\top}\Gamma y + z^{\top}Cz,$$
$$R^{\top}y = t,$$
$$y^{\top}y + z^{\top}z = 1.$$
Do đó
$$y = (R^{\top})^{-1}t,$$
Và nếu ta viết
$$s^{2}= 1 -y^{\top}y > 0$$
Và
$$b = \Gamma y,$$
