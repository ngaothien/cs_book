# Các ma trận


<!-- PAGE 95 -->

## 3.6 Các ma trận

Trong Mục 2.1 ta đã giới thiệu một cách trực quan khái niệm của ma trận. Trong mục này ta định nghĩa các ma trận một cách chính xác, và cũng giới thiệu một số các phép toán trên các ma trận. Hóa ra là các ma trận tạo thành không gian vectơ (vector space) được trang bị phép toán nhân mà là kết hợp, nhưng không giao hoán. Ta sẽ giải thích trong Mục 4.1 cách mà các ma trận có thể được được sử dụng để biểu diễn các ánh xạ tuyến tính (linear maps), được định nghĩa trong mục tiếp theo.

> **Định nghĩa 3.12.** Nếu $K =\mathbb{R}$ hoặc $K =\mathbb{C}$, một ma trận cỡ $m\times n$ trên $K$ là họ $(a_{i j})_{1\le i\le m,1\le j\le n}$ của các vô hướng trong $K$, được biểu diễn bởi mảng (array)
$$\begin{pmatrix} a_{1 1} & a_{1 2} & \dots & a_{1n} \\ a_{2 1} & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{m n} \end{pmatrix}$$
Trong trường hợp đặc biệt khi $m = 1$, ta có vectơ hàng (row vector), được biểu diễn bởi
$$(a_{1 1} \cdots  a_{1n})$$
Và trong trường hợp đặc biệt khi $n = 1$, ta có vectơ cột (column vector), được biểu diễn bởi
$$\begin{pmatrix} a_{1 1} \\ \vdots \\ a_{m1} \end{pmatrix} .$$
Trong hai trường hợp cuối này, ta thường bỏ qua chỉ số hằng $1$ (chỉ số thứ nhất trong trường hợp hàng, chỉ số thứ hai trong trường hợp cột). Tập hợp tất cả các ma trận cỡ $m \times n$ được ký hiệu bởi $M_{m,n}(K)$ hoặc $M_{m,n}$. một ma trận cỡ $n \times n$ được gọi là một ma trận vuông (square matrix) có số chiều $n$. Tập hợp tất cả các ma trận vuông có số chiều $n$ được ký hiệu bởi $M_{n}(K)$, hoặc $M_{n}$.
Nhận xét: Như đã định nghĩa, ma trận $A = (a_{i j})_{1\le i\le m,1\le j\le n}$ là họ, nghĩa là, hàm từ ${1, 2, \dots  , m} \times  {1, 2, \dots  , n}$ đến $K$. Vì vậy, không có lý do giả sử thứ tự trên các chỉ số. Do đó, ma trận $A$ có thể được biểu diễn theo nhiều cách khác nhau như mảng (array), bởi áp dụng các thứ tự khác nhau cho các hàng hoặc các cột. Tuy nhiên, nó là thông lệ (và thường thuận tiện) giả sử thứ tự tự nhiên trên các tập hợp ${1, 2, \dots  , m}$ và ${1, 2, \dots  , n}$, và để biểu diễn $A$ như mảng (array) theo thứ tự này của các hàng và các cột. Ta định nghĩa một số các phép toán trên các ma trận như sau.

<!-- PAGE 96 -->

> **Định nghĩa 3.13.** Cho trước hai ma trận cỡ $m \times  n$ $A = (a_{i j})$ và $B = (b_{i j})$, ta định nghĩa của chúng tổng $A + B$ như ma trận $C = (c_{i j})$ sao cho $c_{i j} = a_{i j} + b_{i j}$; nghĩa là,
$$\begin{pmatrix} a_{1 1} & a_{1 2} & \dots & a_{1n} \\ a_{2 1} & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{m n} \end{pmatrix} + \begin{pmatrix} b_{1 1} & b_{1 2} & \dots & b_{1n} \\ b_{2 1} & b_{2 2} & \dots & b_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ b_{m1} & b_{m2} & \dots & b_{m n} \end{pmatrix}$$
$$= \begin{pmatrix} a_{1 1} + b_{1 1} & a_{1 2} + b_{1 2} & \dots & a_{1n} + b_{1n} \\ a_{2 1} + b_{2 1} & a_{2 2} + b_{2 2} & \dots & a_{2n} + b_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} + b_{m1} & a_{m2} + b_{m2} & \dots & a_{m n} + b_{m n} \end{pmatrix} .$$
Với mọi ma trận $A = (a_{i j})$, ta cho $-A$ là ma trận $(-a_{i j})$. Cho trước vô hướng (scalar) $\lambda  \in K$, ta định nghĩa ma trận $\lambda A$ như ma trận $C = (c_{i j})$ sao cho $c_{i j} = \lambda a_{i j}$; nghĩa là
$$\lambda \begin{pmatrix} a_{1 1} & a_{1 2} & \dots & a_{1n} \\ a_{2 1} & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{m n} \end{pmatrix} = \begin{pmatrix} \lambda a_{1 1} & \lambda a_{1 2} & \dots & \lambda a_{1n} \\ \lambda a_{2 1} & \lambda a_{2 2} & \dots & \lambda a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ \lambda a_{m1} & \lambda a_{m2} & \dots & \lambda a_{m n} \end{pmatrix} .$$
Cho trước các ma trận cỡ $m \times  n$ $A = (a_{i k})$ và các ma trận cỡ $n \times  p$ $B = (b_{k j})$, ta định nghĩa của chúng tích $AB$ như ma trận cỡ $m \times  p$ $C = (c_{i j})$ sao cho
$$c_{i j} = \sum_{k=1}^{n}  a_{i k}b_{k j},$$
Cho $1 \le i \le m$, và $1 \le j \le p$. Trong tích $AB = C$ được hiển thị dưới đây
$$\begin{pmatrix} a_{1 1} & a_{1 2} & \dots & a_{1n} \\ a_{2 1} & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{m n} \end{pmatrix} \begin{pmatrix} b_{1 1} & b_{1 2} & \dots & b_{1p} \\ b_{2 1} & b_{2 2} & \dots & b_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ b_{n1} & b_{n2} & \dots & b_{n p} \end{pmatrix} = \begin{pmatrix} c_{1 1} & c_{1 2} & \dots & c_{1p} \\ c_{2 1} & c_{2 2} & \dots & c_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ c_{m1} & c_{m2} & \dots & c_{m p} \end{pmatrix} ,$$
Lưu ý rằng phần tử (entry) của chỉ số $i$ và $j$ của ma trận $AB$ thu được bằng cách nhân các ma trận $A$ và $B$ có thể được đồng nhất với tích của ma trận hàng tương ứng với hàng thứ $i$ của $A$ với ma trận cột tương ứng với cột thứ $j$ của $B$:
$$(a_{i1} \cdots  a_{i n}) \begin{pmatrix} b_{1j} \\ \vdots \\ b_{n j} \end{pmatrix} = \sum_{k=1}^{n}  a_{i k}b_{k j}.$$

<!-- PAGE 97 -->

> **Định nghĩa 3.14.** ma trận vuông (square matrix) $I_{n}$ có số chiều $n$ chứa $1$ trên đường chéo và $0$ ở mọi nơi khác được gọi là ma trận đơn vị (identity matrix). Nó được ký hiệu bởi
$$I_{n} = \begin{pmatrix} 1 & 0 & \dots & 0 \\ 0 & 1 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & 1 \end{pmatrix}$$

> **Định nghĩa 3.15.** Cho trước một ma trận cỡ $m \times  n$ $A = (a_{i j})$, của nó chuyển vị (transpose) $A^{\top} = (a_{j i}^{\top})$, là ma trận cỡ $n \times m$ sao cho $a_{j i}^{\top} = a_{i j}$, với mọi $i, 1 \le i \le m$, và tất cả $j, 1 \le j \le n$. chuyển vị (transpose) của ma trận $A$ đôi khi được ký hiệu bởi $A^{t}$, hoặc chẵn/ngay cả bởi $^{t}$. Lưu ý rằng chuyển vị (transpose) $A^{\top}$ của ma trận $A$ có tính chất rằng hàng thứ $j$ của $A^{\top}$ là cột thứ $j$ của $A$. Nói cách khác, phép chuyển vị hoán đổi các hàng và các cột của ma trận. Đây là một ví dụ. Nếu $A$ là ma trận cỡ $5 \times  6$
$$A = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 & 6 \\ 7 & 1 & 2 & 3 & 4 & 5 \\ 8 & 7 & 1 & 2 & 3 & 4 \\ 9 & 8 & 7 & 1 & 2 & 3 \\ 10 & 9 & 8 & 7 & 1 & 2 \end{pmatrix} ,$$
Thì $A^{\top}$ là ma trận cỡ $6 \times  5$
$$A^{\top}= \begin{pmatrix} 1 & 7 & 8 & 9 & 10 \\ 2 & 1 & 7 & 8 & 9 \\ 3 & 2 & 1 & 7 & 8 \\ 4 & 3 & 2 & 1 & 7 \\ 5 & 4 & 3 & 2 & 1 \\ 6 & 5 & 4 & 3 & 2 \end{pmatrix} .$$
Nhận xét sau đây sẽ là hữu ích sau này khi ta thảo luận SVD. Cho trước bất kỳ ma trận cỡ $m \times  n$ $A$ và bất kỳ ma trận cỡ $n \times  p$ $B$, nếu ta ký hiệu các cột của $A$ bởi $A^{1}, \dots  , A^{n}$ và các hàng của $B$ bởi $B_{1}, \dots  , B_{n}$, thì ta có
$$AB = A^{1}B_{1} + \cdots  + A^{n}B_{n}.$$
Với mọi ma trận vuông (square matrix) $A$ có số chiều $n$, ta kiểm chứng được ngay rằng $AI_{n} = I_{n}A = A$.
Nhận xét: Nếu $C$ là một ma trận cỡ $n \times  1$ (vectơ cột (column vector)) và $R$ là một ma trận cỡ $1 \times  n$ (vectơ hàng (row vector)), thì ma trận cỡ $n \times  n$ $CR$ đôi khi được gọi là một tích ngoài (outer product).

> **Định nghĩa 3.16.** Với mọi ma trận vuông (square matrix) $A$ có số chiều $n$, nếu ma trận $B$ sao cho $AB = BA = I_{n}$ tồn tại, thì nó là duy nhất, và nó được gọi là nghịch đảo của $A$. ma trận $B$ cũng được ký hiệu bởi $A^{-1}$. ma trận khả nghịch (invertible matrix) cũng được gọi là một ma trận không suy biến (nonsingular matrix), và ma trận rằng là không khả nghịch được gọi là một ma trận suy biến (singular matrix).

<!-- PAGE 98 -->
Kết quả sau đây là tương tự ma trận của Mệnh đề 3.23.

> **Mệnh đề 3.15.** Nếu ma trận vuông (square matrix) $A \in M_{n}(K)$ có nghịch đảo trái (left inverse), nghĩa là ma trận $B$ sao cho $BA = I_{n}$, hoặc nghịch đảo phải (right inverse), nghĩa là ma trận $C$ sao cho $AC = I_{n}$, thì $A$ là thực sự khả nghịch. Hơn nữa, $B = A^{-1}$ và $C = A^{-1}$.

*Chứng minh.* Mệnh đề 3.15 suy ra từ Mệnh đề 3.23 và sự kiện rằng các ma trận biểu diễn các ánh xạ tuyến tính (linear maps). Ta cũng có thể đưa ra chứng minh trực tiếp như sau. Giả sử rằng có một ma trận $B$ sao cho $BA = I_{n}$. Điều này suy ra rằng các cột $A^{1}, \dots  , A^{n}$ của $A$ là độc lập tuyến tính (linearly independent), bởi vì nếu
$$A\lambda  = \lambda_{1} A^{1}+ \cdots  + \lambda_{n} A^{n}= 0,$$
Ở đâu $\lambda  \in K^{n}$ là vectơ cột (column vector)
$$\lambda  = \begin{pmatrix} \lambda_{1} \\ \vdots \\ \lambda_{n} \end{pmatrix} ,$$
Với một số $\lambda_{1} , \dots  , \lambda_{n}  \in K$, bằng cách nhân cả hai vế của phương trình $A\lambda  = 0$ bởi $B$ ta thu được
$$BA\lambda  = I_{n}\lambda  = \lambda  = B0 = 0,$$
Do đó $\lambda  = 0$. Khi đó vì $(A^{1}, \dots  , A^{n})$ là $n$ các vectơ độc lập tuyến tính (linearly independent) trong $K^{n}$, theo Mệnh đề 3.13(3), chúng tạo thành cơ sở (basis) của $K^{n}$. Hệ quả là, với mọi vectơ $b \in K^{n}$, tồn tại duy nhất một vectơ cột (column vector) $(x_{1}, \dots  , x_{n}) \in K^{n}$ sao cho
$$Ax = x_{1}A^{1}+ \cdots  + x_{n}A^{n}= b,$$
Ở đâu $x$ là vectơ cột (column vector)
$$x = \begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix} .$$
Do đó ta có thể giải $n$ các phương trình
$$Ax^{j}= e_{j},1 \le j \le n,$$
Ở đâu $e_{j} = (0, \dots  , 0, 1, 0, \dots  , 0)$ là vectơ cơ sở chính tắc thứ $j$ trong $K^{n}$. các phương trình này cho phương trình ma trận
$$AX = I_{n},$$
Ở đâu $X = (x^{1} \cdots  x^{n})$ là ma trận cỡ $n \times  n$ có cột thứ $j$ là $x^{j}$. Hệ quả là, $X$ là nghịch đảo phải (right inverse) của $A$. Bây giờ $A$ có nghịch đảo trái (left inverse) $B$ và nghịch đảo phải (right inverse) $X$, do đó theo Mệnh đề 2.2, ta có $X = B$, do đó $A$ là khả nghịch và nghịch đảo của nó bằng $B$. Bây giờ ta giả sử rằng có một ma trận $C$ sao cho $AC = I_{n}$. Ta có thể lặp lại chứng minh trước đó với $C$ đóng vai trò của $A$ và $A$ đóng vai trò của $B$ để kết luận rằng $C$ là khả nghịch và rằng $C^{-1} = A$. Nhưng khi đó $C^{-1}$ là khả nghịch với nghịch đảo $C$, và vì $C = (C^{-1})^{-1} = A^{-1}$, ta kết luận rằng $A$ là khả nghịch và rằng nghịch đảo của nó bằng $C$.

<!-- PAGE 99 -->
Bằng cách sử dụng Mệnh đề 2.3 (hoặc mimicking các phép tính trong chứng minh của nó), ta lưu ý rằng nếu $A$ và $B$ là hai $n \times  n$ các ma trận khả nghịch, thì AB là cũng khả nghịch và $(AB)^{-1} = B^{-1}A^{-1}$. quan trọng tiêu chuẩn cho ma trận vuông (square matrix) là khả nghịch được phát biểu tiếp theo. Một cái khác chứng minh là miễn là/được cung cấp trong Mệnh đề 4.4.

> **Mệnh đề 3.16.** ma trận vuông (square matrix) $A \in M_{n}(K)$ là khả nghịch khi và chỉ khi của nó các cột $(A^{1}, \dots  , A^{n})$ là độc lập tuyến tính (linearly independent).

*Chứng minh.* Nếu $A$ là khả nghịch, thì đặc biệt nó có nghịch đảo trái (left inverse) $A^{-1}$, do đó phần thứ nhất của chứng minh của Mệnh đề 3.15 với $B = A^{-1}$ chứng tỏ rằng các cột $(A^{1}, \dots  , A^{n})$ của $A$ là độc lập tuyến tính (linearly independent). sự kiện này cũng được chứng minh như phần của chứng minh của Mệnh đề 4.4. Ngược lại, giả sử rằng các cột $(A^{1}, \dots  , A^{n})$ của $A$ là độc lập tuyến tính (linearly independent). phần thứ hai của chứng minh của Mệnh đề 3.15 chỉ ra rằng $A$ là khả nghịch. Một cái khác hữu ích tiêu chuẩn cho ma trận vuông (square matrix) là khả nghịch được phát biểu tiếp theo.

> **Mệnh đề 3.17.** ma trận vuông (square matrix) $A \in M_{n}(K)$ là khả nghịch khi và chỉ khi với mọi $x \in K^{n}$, phương trình Ax $= 0$ suy ra rằng $x = 0$.

*Chứng minh.* Nếu $A$ là khả nghịch và nếu Ax $= 0$, thì bằng cách nhân cả hai vế của phương trình $x = 0$ bởi $A^{-1}$, ta thu được
$$A^{-1}Ax = I_{n}x = x = A^{-1}0 = 0.$$
Ngược lại, với mọi $x = (x_{1}, \dots  , x_{n}) \in K^{n}$, vì
$$Ax = x_{1}A^{1}+ \cdots  + x_{n}A^{n},$$
Điều kiện Ax $= 0$ suy ra $x = 0$ là tương đương đến sự độc lập tuyến tính (linear independence) của các cột $(A^{1}, \dots  , A^{n})$ của $A$. Theo Mệnh đề 3.16, ma trận $A$ là khả nghịch. Ta kiểm chứng được ngay rằng tập hợp $M_{m,n}(K)$ của $m \times  n$ các ma trận là không gian vectơ (vector space) dưới phép cộng của các ma trận và phép nhân của ma trận bởi vô hướng (scalar).

> **Định nghĩa 3.17.** các ma trận cỡ $m \times n$ $E_{ij} = (e_{h k})$, được định nghĩa sao cho $e_{i j} = 1$, và $e_{h k} = 0$, nếu $h \neq  i$ hoặc $k \neq  j$; nói cách khác, $(i$, j)-phần tử (entry) bằng $1$ và tất cả khác các phần tử (entries) là $0$. Ở đây là $E_{ij}$ các ma trận cho $m = 2$ và $n = 3$:
$$E_{11} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} ,E_{12} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} ,E_{13} = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$
$$E_{21} = \begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix} ,E_{22} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} ,E_{23} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} .$$

<!-- PAGE 100 -->
Rõ ràng là mọi ma trận $A = (a_{i j}) \in M_{m,n}(K)$ có thể được được viết trong duy nhất cách như
$$A = \sum_{i=1j}^{m}  \sum_{=1}^{n}  a_{i j}E_{ij}.$$
Do đó, họ $(E_{ij})_{1\le i\le m,1\le j\le n}$ là cơ sở (basis) của không gian vectơ (vector space) $M_{m,n}(K)$, mà có số chiều mn.
Nhận xét: Định nghĩa 3.12 và Định nghĩa 3.13 cũng tạo perfect nghĩa khi $K$ là (giao hoán) vành thay vì trường. Trong điều này nhiều hơn/thêm tổng quát đặt, khung lý thuyết của các không gian vectơ là cũng narrow, nhưng ta có thể xét các cấu trúc trên vành giao hoán (commutative ring) $A$ thỏa mãn tất cả axioms của Định nghĩa 3.1. Như vậy các cấu trúc được gọi là các môđun. lý thuyết của các môđun là (nhiều) nhiều hơn/thêm phức tạp hơn rằng của các không gian vectơ. Ví dụ, các môđun thực hiện không luôn luôn có cơ sở (basis), và khác các tính chất giữ cho các không gian vectơ thường thất bại cho các môđun. Khi môđun có cơ sở (basis), nó được gọi là một môđun tự do (free module). Ví dụ, khi $A$ là vành giao hoán (commutative ring), cấu trúc $A^{n}$ là môđun sao cho các vectơ $e_{i}$, với $(e_{i})_{i} = 1$ và $(e_{i})_{j} = 0$ cho $j \neq  i$, tạo thành cơ sở (basis) của $A^{n}$. Nhiều các tính chất của các không gian vectơ vẫn đúng cho $A^{n}$. Do đó, $A^{n}$ là môđun tự do (free module). Như một cái khác ví dụ, khi $A$ là vành giao hoán (commutative ring), $M_{m,n}(A)$ là môđun tự do (free module) với cơ sở (basis) $(E_{i,j})_{1\le i\le m,1\le j\le n}$. Các đa thức trên vành giao hoán (commutative ring) cũng tạo thành môđun tự do (free module) của vô hạn số chiều. các tính chất được liệt kê trong Mệnh đề 3.18 là dễ dàng được kiểm chứng, mặc dù một số của các phép tính là bit tẻ nhạt/dài dòng. nhiều hơn/thêm conceptual chứng minh là cho trước trong Mệnh đề 4.1.

> **Mệnh đề 3.18.** $(1)$ Cho trước bất kỳ các ma trận $A \in M_{m,n}(K), B \in M_{n,p}(K)$, và $C \in M_{p,q}(K)$, ta có
$$(AB)C = A(BC);$$
Rằng là, phép nhân ma trận (matrix multiplication) là kết hợp.
$(2)$ Cho trước bất kỳ các ma trận $A, B \in M_{m,n}(K)$, và $C, D \in M_{n,p}(K)$, với mọi $\lambda  \in K$, ta có
$$(A + B)C = AC + BC$$
$$A(C + D) = AC + AD$$
$$(\lambda A)C = \lambda (AC)$$
$$A(\lambda C) = \lambda (AC),$$
Sao cho phép nhân ma trận (matrix multiplication) $\cdot$: $M_{m,n}(K) \times  M_{n,p}(K) \to M_{m,p}(K)$ là song tuyến tính. các tính chất của Mệnh đề 3.18 cùng với sự kiện rằng $AI_{n} = I_{n}A = A$ với mọi square $n\times n$ các ma trận chỉ ra rằng $M_{n}(K)$ là vành với unit $I_{n}$ (thực ra, kết hợp đại số). Điều này là không giao hoán vành với không các ước, như được hiển thị bởi sau đây ví dụ.
