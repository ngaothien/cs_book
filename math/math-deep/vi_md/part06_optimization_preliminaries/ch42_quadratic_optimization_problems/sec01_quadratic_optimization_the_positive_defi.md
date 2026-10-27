# Tối ưu hóa toàn phương (quadratic optimization): Xác định dương (positive definite) Trường hợp


<!-- PAGE 1543 -->
Chương $42$ Tối ưu hóa toàn phương (quadratic optimization) Các bài tập Trong chương này ta xét hai các lớp của tối ưu hóa toàn phương (quadratic optimization) các bài tập rằng xuất hiện frequently trong kỹ thuật và trong máy tính khoa học (especially trong máy tính thị giác): $1$. Cực tiểu hóa
$$Q(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b$$
Trên tất cả $x \in \mathbb{R}^{n}$, hoặc subject đến tuyến tính hoặc afin các ràng buộc. $2$. Cực tiểu hóa
$$Q(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b$$
Trên unit mặt cầu. Trong cả hai các trường hợp, $A$ là ma trận đối xứng (symmetric matrix). Ta cũng seek cần và đủ các điều kiện cho $Q$ đến có cực tiểu toàn cục (global minimum).

## 42.1 Tối ưu hóa toàn phương (quadratic optimization): Dương

$$Definite Case$$
Nhiều các bài tập trong vật lý và kỹ thuật có thể được được phát biểu như cực tiểu hóa của một số năng lượng hàm, với hoặc mà không có các ràng buộc. Thật vậy, nó là cơ bản nguyên lý của cơ học rằng nature acts do đó như để cực tiểu hóa năng lượng. Hơn nữa, nếu vật lý hệ là trong stable phát biểu của equilibrium, thì năng lượng trong rằng phát biểu nên là tối tiểu. Ví dụ, nhỏ hình cầu placed trên đỉnh/trên của mặt cầu là trong unstable equilibrium position. nhỏ motion gây ra hình cầu đến roll xuống. Mặt khác, hình cầu placed bên trong và tại đáy/dưới của mặt cầu là trong stable equilibrium position bởi vì potential năng lượng là tối tiểu. đơn giản nhất loại của năng lượng hàm là toàn phương hàm. Như vậy các hàm có thể được một cách thuận tiện được định nghĩa trong tạo thành
$$Q(x) = x^{\top}Ax -x^{\top}b,$$
$$1543$$

<!-- PAGE 1544 -->
Ở đâu $A$ là đối xứng $n \times  n$ ma trận và $x, b$, là các vectơ trong $\mathbb{R}^{n}$, được quan điểm như các vectơ cột. Thực sự, cho các lý do rằng sẽ là rõ ràng một cách ngắn, nó được ưu tiên hơn đến đặt $factor_{2}^{1}$ trong trước của toàn phương số hạng, sao cho
$$Q(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b.$$
Câu hỏi là, dưới những gì các điều kiện (trên $A)$ thực hiện Q(x) có cực tiểu toàn cục (global minimum), preferably duy nhất? Ta cho đầy đủ câu trả lời đến ở trên câu hỏi trong hai các giai đoạn: $1$. Trong mục này ta chỉ ra rằng nếu $A$ là đối xứng xác định dương (SPD), thì Q(x) có duy nhất cực tiểu toàn cục (global minimum) một cách chính xác khi
$$Ax = b.$$
$2$. Trong Mục 42.2 ta cho cần và đủ các điều kiện trong tổng quát trường hợp, theo nghịch đảo giả (pseudo-inverse) của $A$. Ta bắt đầu với ma trận phiên bản của Định nghĩa 22.2.

> **Định nghĩa 42.1.** đối xứng xác định dương (SPD) ma trận là ma trận có các trị riêng (eigenvalues) là chặt dương, và đối xứng nửa xác định dương (positive semidefinite) ma trận là ma trận có các trị riêng (eigenvalues) là không âm. Tương đương các tiêu chuẩn là cho trước trong sau đây mệnh đề.

> **Mệnh đề 42.1.** Cho trước bất kỳ Không gian Euclid (Euclidean space) $E$ có số chiều $n$, các tính chất sau đây đúng:
$(1)$ Mọi tự liên hợp (self-adjoint) ánh xạ tuyến tính (linear map) $f$: $E \to E$ là xác định dương (positive definite) khi và chỉ khi
$$\langle f(x), x\rangle > 0$$
Với mọi $x \in E$ với $x \neq  0$.
$(2)$ Mọi tự liên hợp (self-adjoint) ánh xạ tuyến tính (linear map) $f$: $E \to E$ là nửa xác định dương (positive semidefinite) khi và chỉ khi
$$\langle f(x), x\rangle \ge 0$$
Với mọi $x \in E$.

*Chứng minh.* $(1)$ Thứ nhất giả sử rằng $f$ là xác định dương (positive definite). Nhắc lại rằng mọi tự liên hợp (self-adjoint) ánh xạ tuyến tính (linear map) có cơ sở trực chuẩn (orthonormal basis) $(e_{1}, \dots  , e_{n})$ của các vectơ riêng (eigenvectors), và cho $\lambda_{1} , \dots  , \lambda_{n}$ là tương ứng các trị riêng (eigenvalues). Đối với cơ sở (cơ sở (basis)) này, với mọi $x = x_{1}e_{1} + \cdots  + x_{n}e_{n} \neq  0$, ta có
$$\langle f(x), x\rangle = \bigoplus  f \begin{pmatrix} x_{i}e_{i} \end{pmatrix} \sum_{i=1}^{n}  , \sum_{i=1}^{n}  x_{i}e_{i}E= \bigoplus  \sum_{i=1}^{n}  \lambda_{i} x_{i}e_{i}, \sum_{i=1}^{n}  x_{i}e_{i}E= \sum_{i=1}^{n}  \lambda_{i} x_{i}^{2} ,$$

<!-- PAGE 1545 -->
Mà là chặt dương, vì $\lambda_{i}  > 0$ cho $i = 1, \dots  , n$, và $x_{i}^{2} > 0$ với một số $i$, vì $x \neq  0$. Ngược lại, giả sử rằng
$$\langle f(x), x\rangle > 0$$
Với mọi $x \neq  0$. Thì cho $x = e_{i}$, ta thu được
$$\langle f(e_{i}), e_{i}\rangle = \langle \lambda_{i} e_{i}, e_{i}\rangle = \lambda_{i} ,$$
Và do đó $\lambda_{i}  > 0$ với mọi $i = 1, \dots  , n$.
$(2)$ Như trong $(1)$, ta có
$$\langle f(x), x\rangle = \sum_{i=1}^{n}  \lambda_{i} x_{i}^{2} ,$$
Và vì $\lambda_{i}  \ge 0$ cho $i = 1, \dots  , n$ bởi vì $f$ là nửa xác định dương (positive semidefinite), ta có $\langle$ f(x), $x\rangle \ge 0$, như đã khẳng định. điều ngược lại là như trong $(1)$ ngoại trừ rằng ta thu được chỉ $\lambda_{i}  \ge 0$ vì $\langle f(e_{i}), e_{i}\rangle \ge 0$. Một số đặc biệt ký hiệu là thông lệ (especially trong trường của lồi tối ưu hóa) đến biểu diễn rằng ma trận đối xứng (symmetric matrix) là xác định dương (positive definite) hoặc nửa xác định dương (positive semidefinite).

> **Định nghĩa 42.2.** Cho trước bất kỳ $n \times  n$ ma trận đối xứng (symmetric matrix) $A$ ta viết $A$ ⪰ $0$ nếu $A$ là nửa xác định dương (positive semidefinite) và ta viết $A$ ≻ $0$ nếu $A$ là xác định dương (positive definite).
Nhận xét: Nó nên được lưu ý rằng ta có thể định nghĩa quan hệ
$$A ⪰B$$
Giữa bất kỳ hai ma trận cỡ $n \times  n$ (đối xứng hoặc không) khi và chỉ khi $A -B$ là đối xứng nửa xác định dương (positive semidefinite). Nó là dễ để kiểm tra rằng quan hệ này là thực sự riêng thứ tự trên các ma trận, được gọi là nửa xác định dương (positive semidefinite) nón thứ tự; cho chi tiết, xem Boyd và Vandenberghe $[29]$, Mục 2.4. Nếu $A$ là đối xứng xác định dương (SPD), nó là dễ dàng đã kiểm tra rằng $A^{-1}$ là cũng đối xứng xác định dương (SPD). Cũng, nếu $C$ là đối xứng xác định dương (SPD) $m\times m$ ma trận và $A$ là một ma trận cỡ $m\times n$ của hạng (rank) $n$ (và do đó $m \ge n$ và ánh xạ $x \mapsto$ Ax là đơn ánh (injective)), thì $A^{\top}CA$ là đối xứng xác định dương (SPD). Ta có thể bây giờ chứng minh rằng
$$Q(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b$$
Có cực tiểu toàn cục (global minimum) khi $A$ là đối xứng xác định dương (SPD).

> **Mệnh đề 42.2.** Cho trước toàn phương hàm
$$Q(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b,$$
Nếu $A$ là đối xứng xác định dương (SPD), thì Q(x) có duy nhất cực tiểu toàn cục (global minimum) cho nghiệm $x_{0} = A^{-1}b$ của hệ phương trình tuyến tính Ax $= b$. cực tiểu giá trị của Q(x) là
$$Q(A^{-1}b) = - \frac{1}{2} b^{\top}A^{-1}b.$$

<!-- PAGE 1546 -->

*Chứng minh.* Vì $A$ là xác định dương (positive definite), nó là khả nghịch vì các trị riêng (các trị riêng (eigenvalues)) của nó là tất cả chặt dương. Cho $x_{0} = A^{-1}b$, và tính Q(y) - $Q(x_{0})$ với mọi $y \in \mathbb{R}^{n}$. Vì $Ax_{0} = b$, ta thu được
$$Q(y) -Q(x_{0}) = \frac{1}{2} y^{\top}Ay -y^{\top}b - \frac{1}{2} x_{0}^{\top} Ax_{0} + x_{0}^{\top} b$$
$$= \frac{1}{2} y^{\top}Ay -y^{\top}Ax_{0} + \frac{1}{2} x_{0}^{\top} Ax_{0}$$
$$= \frac{1}{2} (y -x_{0})^{\top}A(y -x_{0}).$$
Vì $A$ là xác định dương (positive definite), cuối cùng biểu thức là không âm, và do đó
$$Q(y) \ge Q(x_{0})$$
Với mọi $y \in \mathbb{R}^{n}$, mà chứng tỏ rằng $x_{0} = A^{-1}b$ là cực tiểu toàn cục (global minimum) của Q(x). đơn giản phép tính cho ta
$$Q(A^{-1}b) = - \frac{1}{2} b^{\top}A^{-1}b.$$
Các nhận xét:
$(1)$ toàn phương hàm Q(x) là cũng cho trước bởi
$$Q(x) = \frac{1}{2} x^{\top}Ax -b^{\top}x,$$
Nhưng định nghĩa bằng cách sử dụng $x^{\top}b$ là nhiều hơn/thêm thuận tiện cho chứng minh của Mệnh đề 42.2.
$(2)$ Nếu Q(x) chứa hằng số số hạng $c \in \mathbb{R}$, sao cho
$$Q(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b + c,$$
Chứng minh của Mệnh đề 42.2 vẫn chỉ ra rằng Q(x) có duy nhất cực tiểu toàn cục (global minimum) cho $x = A^{-1}b$, nhưng tối tiểu giá trị là
$$Q(A^{-1}b) = - \frac{1}{2} b^{\top}A^{-1}b + c.$$
Do đó khi năng lượng hàm Q(x) của hệ được cho bởi toàn phương hàm
$$Q(x) = \frac{1}{2} x^{\top}Ax -x^{\top}b,$$
Ở đâu $A$ là đối xứng xác định dương (SPD), việc tìm cực tiểu toàn cục (global minimum) của Q(x) là tương đương đến việc giải hệ phương trình tuyến tính Ax $= b$. Đôi khi, nó là hữu ích đến recast tuyến tính bài toán Ax $= b$ như variational bài toán (việc tìm cực tiểu của một số năng lượng hàm). Tuy nhiên, rất thường, cực tiểu hóa bài toán đến với extra các ràng buộc rằng phải được thỏa mãn với mọi admissible các nghiệm.

<!-- PAGE 1547 -->

> **Ví dụ 42.1.** Chẳng hạn, ta có thể muốn để cực tiểu hóa toàn phương hàm
$$Q(x_{1}, x_{2}) = \frac{1}{2}$$
$$\begin{pmatrix} x_{1}^{2}+ x_{2}^{2} \end{pmatrix}$$
Subject đến ràng buộc
$$2x_{1} -x_{2} = 5.$$
Nghiệm cho mà $Q(x_{1}, x_{2})$ là cực tiểu là không có dài hơn $(x_{1}, x_{2}) = (0, 0)$, nhưng thay vì, $(x_{1}, x_{2}) = (2, -1)$, như sẽ được hiển thị sau này.
$$\mathbb{R}^{3}$$
Geometrically, đồ thị của hàm được định nghĩa bởi $z = Q(x_{1}, x_{2})$ trong là paraboloid của revolution $P$ với trục của revolution Oz. ràng buộc
$$2x_{1} -x_{2} = 5$$
Tương ứng với đứng mặt phẳng $H$ song song đến trục $z$ và chứa đường thẳng của phương trình $2x_{1}$ - $x_{2} = 5$ trong mặt phẳng $xy$. Do đó, như được minh họa bởi Hình 42.1, có ràng buộc cực tiểu của $Q$ là located trên parabol rằng là giao của paraboloid $P$ với mặt phẳng $H$. đẹp cách để giải có ràng buộc cực tiểu hóa các bài tập của ở trên loại là để sử dụng phương pháp của Các nhân tử Lagrange (Lagrange multipliers) được thảo luận trong Mục 40.1. Nhưng thứ nhất cho chúng ta định nghĩa một cách chính xác những gì loại của cực tiểu hóa các bài tập ta intend để giải.

> **Định nghĩa 42.3.** toàn phương có ràng buộc cực tiểu hóa bài toán bao gồm trong cực tiểu hóa toàn phương hàm
$$Q(x) = \frac{1}{2} x^{\top}A^{-1}x -b^{\top}x$$
Subject đến tuyến tính các ràng buộc
$$B^{\top}x = f,$$
Ở đâu $A^{-1}$ là $m \times  m$ đối xứng xác định dương (SPD) ma trận, $B$ là một ma trận cỡ $m \times  n$ của hạng (rank) $n$
$$\mathbb{R}^{m} \mathbb{R}^{n}$$
(sao cho $m \ge n)$, và ở đâu $b, x \in$ (được quan điểm như các vectơ cột), và $f \in$ (được quan điểm như vectơ cột (column vector)). lý do cho bằng cách sử dụng $A^{-1}$ thay vì của $A$ là rằng có ràng buộc cực tiểu hóa bài toán có interpretation như tập hợp của equilibrium các phương trình trong mà ma trận rằng phát sinh một cách tự nhiên là $A$ (xem Strang $[175])$. Vì $A$ và $A^{-1}$ là cả hai đối xứng xác định dương (SPD), điều này không’t tạo bất kỳ difference, nhưng nó dường như được ưu tiên hơn đến stick đến Strang’s ký hiệu. Trong Ví dụ 42.1 ta có $m = 2, n = 1$,
$$A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_{2},b = \begin{pmatrix} 0 \\ 0 \end{pmatrix} ,B = \begin{pmatrix} 2 \\ -1 \end{pmatrix} ,f = 5.$$
Như được giải thích trong Mục 40.1, phương pháp của Các nhân tử Lagrange (Lagrange multipliers) bao gồm trong incorporating $n$ các ràng buộc $B^{\top}x = f$ vào toàn phương hàm Q(x), bởi giới thiệu extra các biến

<!-- PAGE 1548 -->
$$Figure 42.1: Two views of the constrained optimization problem Q(x_{1}, x_{2}) =_{2}^{1} \begin{pmatrix} x_{1}^{2}+ x_{2}^{2} \\ vertexof \end{pmatrix}$$
Subject đến ràng buộc $2x_{1}$ - $x_{2} = 5$. cực tiểu $(x_{1}, x_{2}) = (2, -1)$ là parabolic đường cong được tạo thành giao của magenta phẳng ràng buộc với bowl shaped mặt. $\lambda  = (\lambda_{1} , \dots  , \lambda_{n}$) được gọi là Các nhân tử Lagrange (Lagrange multipliers), một với mỗi ràng buộc. Ta tạo thành Hàm Lagrange (Lagrangian)
$$L(x, \lambda ) = Q(x) + \lambda^{\top} (B^{\top}x -f) = \frac{1}{2} x^{\top}A^{-1}x -(b -B\lambda )^{\top}x -\lambda^{\top} f.$$
Ta biết từ Định lý 40.2 rằng cần điều kiện cho của ta có ràng buộc tối ưu hóa bài toán đến có nghiệm là rằng $\nabla$ L(x, $\lambda$) $= 0$. Vì
$$\frac{\partial L}{\partial x} (x, \lambda ) = A^{-1}x -(b -B\lambda )$$
$$\frac{\partial L}{\partial \lambda} (x, \lambda ) = B^{\top}x -f,$$
Ta thu được hệ của các phương trình tuyến tính
$$A^{-1}x + B\lambda  = b,$$
$$B^{\top}x = f,$$
Mà có thể được được viết trong ma trận tạo thành như
$$\begin{pmatrix} A^{-1} & B \\ B^{\top} & 0 \end{pmatrix} \begin{pmatrix} x \\ \lambda \end{pmatrix} = \begin{pmatrix} b \\ f \end{pmatrix} .$$

<!-- PAGE 1549 -->
Ta sẽ chứng minh trong Mệnh đề 42.3 ở dưới rằng của ta có ràng buộc cực tiểu hóa bài toán có duy nhất nghiệm thực sự cho trước bởi ở trên hệ. Lưu ý rằng ma trận của hệ này là đối xứng. Ta giải nó như sau. Eliminating $x$ từ phương trình thứ nhất
$$A^{-1}x + B\lambda  = b,$$
Ta thu được
$$x = A(b -B\lambda ),$$
Và thế vào phương trình thứ hai, ta thu được
$$B^{\top}A(b -B\lambda ) = f,$$
Rằng là,
$$B^{\top}AB\lambda  = B^{\top}Ab -f.$$
Tuy nhiên, bởi trước đó nhận xét, vì $A$ là đối xứng xác định dương (SPD) và các cột của $B$ là độc lập tuyến tính (linearly independent), $B^{\top}AB$ là đối xứng xác định dương (SPD), và do đó khả nghịch. Do đó ta thu được nghiệm
$$\lambda  = (B^{\top}AB)^{-1}(B^{\top}Ab -f),x = A(b -B\lambda ).$$
Lưu ý rằng điều này cách của việc giải hệ đòi hỏi việc giải cho Các nhân tử Lagrange (Lagrange multipliers) thứ nhất. Đặt $e = b$ - $B\lambda$, ta cũng lưu ý rằng hệ
$$\begin{pmatrix} A^{-1} & B \\ B^{\top} & 0 \end{pmatrix} \begin{pmatrix} x \\ \lambda \end{pmatrix} = \begin{pmatrix} b \\ f \end{pmatrix}$$
Là tương đương đến hệ
$$e = b -B\lambda ,$$
$$x = Ae,$$
$$B^{\top}x = f.$$
Latter hệ được gọi là equilibrium các phương trình bởi Strang $[175]$. Thật vậy, Strang chỉ ra rằng equilibrium các phương trình của nhiều vật lý các hệ có thể được đặt trong ở trên tạo thành. Điều này bao gồm spring-mass các hệ, electrical networks và trusses, mà là các cấu trúc được xây dựng từ elastic bars. Trong mỗi trường hợp, $x, e, b, A, \lambda , f$, và $K = B^{\top}AB$ có vật lý interpretation. ma trận $K = B^{\top}AB$ là thường được gọi là stiffness ma trận. Một lần nữa, độc giả là referred đến Strang $[175]$. Trong thứ tự để chứng minh rằng của ta có ràng buộc cực tiểu hóa bài toán có duy nhất nghiệm, ta tiến hành để chứng minh rằng có ràng buộc cực tiểu hóa của Q(x) subject đến $B^{\top}x = f$ là tương đương đến không ràng buộc cực đại hóa của một cái khác hàm $-G(\lambda$). Ta thu được $G(\lambda$) bởi cực tiểu hóa Hàm Lagrange (Lagrangian) L(x, $\lambda$) treated như hàm của $x$ alone. hàm $-G(\lambda$) là đối ngẫu (dual)

<!-- PAGE 1550 -->
Hàm của Hàm Lagrange (Lagrangian) L(x, $\lambda$). Ở đây ta là encountering đặc biệt trường hợp của khái niệm của đối ngẫu (dual) hàm được định nghĩa trong Mục 50.7. Vì $A^{-1}$ là đối xứng xác định dương (SPD) và
$$L(x, \lambda ) = \frac{1}{2} x^{\top}A^{-1}x -(b -B\lambda )^{\top}x -\lambda^{\top} f,$$
Theo Mệnh đề 42.2 cực tiểu toàn cục (global minimum) (đối với $x)$ của L(x, $\lambda$) là thu được cho nghiệm $x$ của
$$A^{-1}x = b -B\lambda ,$$
Rằng là, khi
$$x = A(b -B\lambda ),$$
Và cực tiểu của L(x, $\lambda$) là
$$minx L(x, \lambda ) = - \frac{1}{2} (B\lambda  -b)^{\top}A(B\lambda  -b) -\lambda^{\top} f.$$
Đặt
$$G(\lambda ) = \frac{1}{2} (B\lambda  -b)^{\top}A(B\lambda  -b) + \lambda^{\top} f,$$
Ta sẽ chỉ ra trong Mệnh đề 42.3 rằng nghiệm của có ràng buộc cực tiểu hóa của Q(x) subject đến $B^{\top}x = f$ là tương đương đến không ràng buộc cực đại hóa của $-G(\lambda$). Điều này là đặc biệt trường hợp của đối ngẫu được thảo luận trong Mục 50.7. Của course, vì ta được cực tiểu hóa L(x, $\lambda$) đối với $x$, ta có
$$L(x, \lambda ) \ge -G(\lambda )$$
Với mọi $x$ và tất cả $\lambda$. Tuy nhiên, khi ràng buộc $B^{\top}x = f$ nghiệm đúng, L(x, $\lambda$) $=$ Q(x), và do đó với mọi admissible $x$, mà có nghĩa là $B^{\top}x = f$, ta có
$$\min Q(x) \ge \max-G(\lambda ).$$
$$x\lambda$$
Trong thứ tự để chứng minh rằng duy nhất cực tiểu của có ràng buộc bài toán Q(x) subject đến $B^{\top}x = f$ là duy nhất cực đại của $-G(\lambda$), ta tính Q(x) $+ G(\lambda$).

> **Mệnh đề 42.3.** toàn phương có ràng buộc cực tiểu hóa bài toán của Định nghĩa 42.3 có duy nhất nghiệm $(x, \lambda$) cho trước bởi hệ
$$\begin{pmatrix} A^{-1} & B \\ B^{\top} & 0 \end{pmatrix} \begin{pmatrix} x \\ \lambda \end{pmatrix} = \begin{pmatrix} b \\ f \end{pmatrix} .$$
Hơn nữa, thành phần $\lambda$ của ở trên nghiệm là duy nhất giá trị cho mà $-G(\lambda$) là cực đại.

<!-- PAGE 1551 -->

*Chứng minh.* Như ta suggested trước đó, cho chúng ta tính Q(x) $+ G(\lambda$), giả sử rằng ràng buộc $B^{\top}x = f$ nghiệm đúng. Eliminating $f$, vì $b^{\top}x = x^{\top}b$ và $\lambda^{\top} B^{\top}x = x^{\top}B\lambda$, ta thu được
$$Q(x) + G(\lambda ) = \frac{1}{2} x^{\top}A^{-1}x -b^{\top}x + \frac{1}{2} (B\lambda  -b)^{\top}A(B\lambda  -b) + \lambda^{\top} f$$
$$= \frac{1}{2} (A^{-1}x + B\lambda  -b)^{\top}A(A^{-1}x + B\lambda  -b).$$
Vì $A$ là xác định dương (positive definite), cuối cùng biểu thức là không âm. Thực ra, nó là null khi và chỉ khi
$$A^{-1}x + B\lambda  -b = 0,$$
Rằng là,
$$A^{-1}x + B\lambda  = b.$$
Nhưng khi đó duy nhất có ràng buộc cực tiểu của Q(x) subject đến $B^{\top}x = f$ bằng duy nhất cực đại của $-G(\lambda$) chính xác khi $B^{\top}x = f$ và $A^{-1}x + B\lambda  = b$, mà chứng minh mệnh đề. Ta có thể confirm rằng cực đại của $-G(\lambda$), hoặc tương đương cực tiểu của
$$G(\lambda ) = \frac{1}{2} (B\lambda  -b)^{\top}A(B\lambda  -b) + \lambda^{\top} f,$$
Tương ứng với giá trị của $\lambda$ thu được bởi việc giải hệ
$$\begin{pmatrix} A^{-1} & B \\ B^{\top} & 0 \end{pmatrix} \begin{pmatrix} x \\ \lambda \end{pmatrix} = \begin{pmatrix} b \\ f \end{pmatrix} .$$
Thật vậy, vì
$$G(\lambda ) = \frac{1}{2} \lambda^{\top} B^{\top}AB\lambda  -\lambda^{\top} B^{\top}Ab + \lambda^{\top} f + \frac{1}{2} b^{\top}b,$$
Và $B^{\top}AB$ là đối xứng xác định dương (SPD), theo Mệnh đề 42.2, cực tiểu toàn cục (global minimum) của $G(\lambda$) là thu được khi
$$B^{\top}AB\lambda  -B^{\top}Ab + f = 0,$$
Rằng là, $\lambda  = (B^{\top}AB)^{-1}(B^{\top}Ab$ - $f)$, như ta tìm thấy trước đó.
Các nhận xét:
$(1)$ Có một tạo thành của đối ngẫu đi trên trong tình huống này. có ràng buộc cực tiểu hóa của Q(x) subject đến $B^{\top}x = f$ được gọi là bài toán gốc (primal problem), và không ràng buộc cực đại hóa của $-G(\lambda$) được gọi là bài toán đối ngẫu (dual problem). Đối ngẫu là sự kiện được phát biểu slightly loosely như
$$\min Q(x) = \max-G(\lambda ).$$
$$x\lambda$$
Tổng quát treatment của đối ngẫu trong có ràng buộc cực tiểu hóa các bài tập là cho trước trong Mục 50.7.

<!-- PAGE 1552 -->
Nhắc lại rằng $e = b$ - $B\lambda$, vì
$$G(\lambda ) = \frac{1}{2} (B\lambda  -b)^{\top}A(B\lambda  -b) + \lambda^{\top} f,$$
Ta có thể cũng viết
$$G(\lambda ) = \frac{1}{2} e^{\top}Ae + \lambda^{\top} f.$$
Điều này biểu thức thường biểu diễn tổng potential năng lượng của hệ. Một lần nữa, nghiệm tối ưu (optimal solution) là một rằng cực tiểu hóa potential năng lượng (và do đó các cực đại hóa $-G(\lambda$)).
$(2)$ Ta kiểm chứng được ngay rằng các phương trình của Mệnh đề 42.3 là tương đương đến các phương trình phát biểu rằng các đạo hàm riêng của Hàm Lagrange (Lagrangian) L(x, $\lambda$) là null:
$$\frac{\partial L}{\partial x_{i}} = 0,i = 1, \dots  , m,$$
$$\frac{\partial L}{\partial \lambda_{j}} = 0,j = 1, \dots  , n.$$
Do đó, có ràng buộc cực tiểu của Q(x) subject đến $B^{\top}x = f$ là cực trị của Hàm Lagrange (Lagrangian) L(x, $\lambda$). Như ta đã chỉ ra trong Mệnh đề 42.3, điều này cực trị tương ứng với simultaneously cực tiểu hóa L(x, $\lambda$) đối với $x$ và cực đại hóa L(x, $\lambda$) đối với $\lambda$. Geometrically, như vậy điểm là điểm yên ngựa (saddle point) cho L(x, $\lambda$). Saddle các điểm được thảo luận trong Mục 50.7.
$(3)$ Các nhân tử Lagrange (Lagrange multipliers) đôi khi có tự nhiên vật lý có nghĩa. Ví dụ, trong spring-mass hệ chúng tương ứng với nút displacements. Trong một số tổng quát nghĩa, Các nhân tử Lagrange (Lagrange multipliers) là correction các số hạng cần thiết đến thỏa mãn equilibrium các phương trình và price paid cho các ràng buộc. Cho nhiều hơn/thêm chi tiết, xem Strang $[175]$. Đi quay lại đến có ràng buộc cực tiểu hóa của $Q(x_{1}, x_{2}) =_{2}^{1} (x_{1}^{2} + x_{2}^{2})$ subject đến
$$2x_{1} -x_{2} = 5,$$
Hàm Lagrange (Lagrangian) là
$$L(x_{1}, x_{2}, \lambda ) = \frac{1}{2} \begin{pmatrix} x_{1}^{2}+ x_{2}^{2} \\ Lagrangian \end{pmatrix} + \lambda (2x_{1} -x_{2} -5),$$
Và các phương trình phát biểu rằng có điểm yên ngựa (saddle point) là
$$x_{1} + 2\lambda  = 0,$$
$$x_{2} -\lambda  = 0,$$
$$2x_{1} -x_{2} -5 = 0.$$
Ta thu được nghiệm $(x_{1}, x_{2}, \lambda$) $= (2, -1, -1)$.
