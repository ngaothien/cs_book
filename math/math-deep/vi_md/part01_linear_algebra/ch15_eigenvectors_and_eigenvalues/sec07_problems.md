# Các bài tập


<!-- PAGE 590 -->

## 15.7 Các bài tập

Bài toán 15.1. Cho $A$ là sau đây $2 \times  2$ ma trận
$$A = \begin{pmatrix} 1 & -1 \\ 1 & -1 \end{pmatrix} .$$
$(1)$ Chứng minh rằng $A$ có trị riêng (eigenvalue) $0$ với bội (multiplicity) $2$ và rằng $A^{2} = 0$.
$(2)$ Cho $A$ là bất kỳ thực $2 \times  2$ ma trận
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} .$$
Chứng minh rằng nếu bc $> 0$, thì $A$ có hai phân biệt thực các trị riêng (eigenvalues). Chứng minh rằng nếu, $b, c, d > 0$, thì có một dương vectơ riêng (eigenvector) $u$ liên kết với lớn nhất của hai các trị riêng (eigenvalues) của $A$, mà có nghĩa là nếu $u = (u_{1}, u_{2})$, thì $u_{1} > 0$ và $u_{2} > 0$.
$(3)$ Giả sử bây giờ rằng $A$ là bất kỳ phức $2 \times  2$ ma trận như trong $(2)$. Chứng minh rằng nếu $A$ có trị riêng (eigenvalue) $0$ với bội (multiplicity) $2$, thì $A^{2} = 0$. Chứng minh rằng nếu $A$ là thực đối xứng, thì $A = 0$.
Bài toán 15.2. Cho $A$ là bất kỳ phức $n \times  n$ ma trận. Chứng minh rằng nếu $A$ có trị riêng (eigenvalue) $0$ với bội (multiplicity) $n$, thì $A^{n} = 0$. Cho ví dụ của ma trận $A$ sao cho $A^{n} = 0$ nhưng $A \neq  0$.
Bài toán 15.3. Cho $A$ là phức $2 \times  2$ ma trận, và cho $\lambda_{1}$ và $\lambda_{2}$ là các trị riêng (eigenvalues) của $A$. Chứng minh rằng nếu $\lambda_{1}  \neq  \lambda_{2}$, thì
$$- -$$
$$e^{A}= \frac{\lambda_{1} e^{\lambda2}\lambda_{2} e^{\lambda1}}{\lambda_{1}  -\lambda_{2}} I + \frac{e^{\lambda1}e^{\lambda2}}{\lambda_{1}  -\lambda_{2}} A.$$
Bài toán 15.4. Cho $A$ là thực đối xứng $2 \times  2$ ma trận
$$A = \begin{pmatrix} a & b \\ b & c \end{pmatrix} .$$
$(1)$ Chứng minh rằng các trị riêng (eigenvalues) của $A$ là thực và cho trước bởi
$$\overline{-}  - \overline{-}$$
$$\lambda_{1}  = \frac{a + c +p\overline{4}\overline{b}^{2}\overline{+ (}\overline{a}\overline{c}\overline{)}^{2}}{2} ,\lambda_{2}  = \frac{a + cp\overline{4}\overline{b}^{2}\overline{+ (}\overline{a}\overline{c}\overline{)}^{2}}{2} .$$
$(2)$ Chứng minh rằng $A$ có gấp đôi trị riêng (eigenvalue) $(\lambda_{1}  = \lambda_{2}  = a)$ khi và chỉ khi $b = 0$ và $a = c$; nghĩa là, $A$ là ma trận đường chéo (diagonal matrix).
$(3)$ Chứng minh rằng các trị riêng (eigenvalues) của $A$ là không âm khi và chỉ khi $b^{2} \le$ ac và $a + c \ge 0$.
$(4)$ Chứng minh rằng các trị riêng (eigenvalues) của $A$ là dương khi và chỉ khi $b^{2} <$ ac, $> 0$ và $c > 0$.

<!-- PAGE 591 -->
Bài toán 15.5. Tìm các trị riêng (eigenvalues) của các ma trận
$$A = \begin{pmatrix} 3 & 0 \\ 1 & 1 \end{pmatrix} ,B = \begin{pmatrix} 1 & 1 \\ 0 & 3 \end{pmatrix} ,C = A + B = \begin{pmatrix} 4 & 1 \\ 1 & 4 \end{pmatrix} .$$
Kiểm tra rằng các trị riêng (eigenvalues) của $A + B$ là không bằng các tổng của các trị riêng (eigenvalues) của $A$ cộng các trị riêng (eigenvalues) của $B$.
Bài toán 15.6. Cho $A$ là thực đối xứng $n\times n$ ma trận và $B$ là thực đối xứng xác định dương (SPD) $n \times  n$ ma trận. Ta sẽ like để giải suy rộng/tổng quát hóa trị riêng (eigenvalue) bài toán: tìm $\lambda  \in \mathbb{R}$ và $u \neq  0$ sao cho
$$Au = \lambda Bu.(*)$$
$(1)$ Sử dụng Phân rã Cholesky (Cholesky decomposition) $B = CC^{\top}$ để chỉ ra rằng $\lambda$ và $u$ là các nghiệm của suy rộng/tổng quát hóa trị riêng (eigenvalue) bài toán (*) khi và chỉ khi $\lambda$ và $v$ là các nghiệm của (thông thường) trị riêng (eigenvalue) bài toán
$$C^{-1}A(C^{\top})^{-1}v = \lambda v,with v = C^{\top}u.$$
Kiểm tra rằng $C^{-1}A(C^{\top})^{-1}$ là đối xứng.
$(2)$ Chứng minh rằng nếu $Au_{1} = \lambda_{1} Bu_{1}, Au_{2} = \lambda_{2} Bu_{2}$, với $u_{1} \neq  0, u_{2} \neq  0$ và $\lambda_{1}  \neq  \lambda_{2}$, thì $u_{1}^{\top} Bu_{2} = 0$.
$(3)$ Chứng minh rằng $B^{-1}A$ và $C^{-1}A(C^{\top})^{-1}$ có cùng các trị riêng (eigenvalues).
Bài toán 15.7. dãy của Fibonacci các số, $0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, \dots$, được cho bởi recurrence
$$F_{n+2} = F_{n+1} + F_{n},$$
Với $F_{0} = 0$ và $F_{1} = 1$. Trong ma trận tạo thành, ta có thể viết
$$\begin{pmatrix} F_{n+1} \\ F_{n} \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} F_{n} \\ F_{n-1} \end{pmatrix} ,n \ge 1, \begin{pmatrix} F_{1} \\ F_{0} \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} .$$
$(1)$ Chỉ ra rằng
$$1^{n}$$
$$\begin{pmatrix} F_{n+1} \\ F_{n} \end{pmatrix} = \begin{pmatrix} 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} .$$
$(2)$ Chứng minh rằng các trị riêng (eigenvalues) của ma trận
$$A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$$
Là
$$\pm$$
$$\lambda  = \frac{1\sqrt{5}}{2} .$$
Số
$$\phi  = \frac{1 +\sqrt{5}}{2}$$

<!-- PAGE 592 -->
Được gọi là golden tỉ số. Chỉ ra rằng các trị riêng (eigenvalues) của $A$ là $\phi$ và $-\phi^{-1}$.
$(3)$ Chứng minh rằng $A$ được chéo hóa như
$$A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} =\sqrt \frac{1}{\overline{5}} \begin{pmatrix} \phi & -\phi^{-1} \\ 1 & 1 \end{pmatrix} \begin{pmatrix} \phi & 0 \\ 0 & -\phi^{-1} \end{pmatrix} \begin{pmatrix} 1 & \phi^{-1} \\ -1 & \phi \end{pmatrix} .$$
Chứng minh rằng
$$\begin{pmatrix} F_{n+1} \\ F_{n} \end{pmatrix} =\sqrt \frac{1}{\overline{5}} \begin{pmatrix} \phi & -\phi^{-1} \\ 1 & 1 \end{pmatrix} \begin{pmatrix} \phi^{n} \\ -(-\phi^{-1} )^{n} \end{pmatrix} ,$$
Và do đó
$$" !!#$$
$$- \overline{5}^{n} -\overline{5}^{n}$$
$$F_{n} =\sqrt \frac{1}{\overline{5}} (\phi^{n} (-\phi^{-1} )^{n}) =\sqrt \frac{1}{\overline{5}} \frac{1 +\sqrt}{2} - \frac{1\sqrt}{2} ,n \ge 0.$$
Bài toán 15.8. Cho $A$ là một ma trận cỡ $n \times  n$. Với mọi tập con I của ${1, \dots  , n}$, cho $A_{I,I}$ là ma trận thu được từ $A$ bởi thứ nhất chọn các cột có các chỉ số thuộc đến I, và thì các hàng có các chỉ số cũng thuộc đến I. Chứng minh rằng
$$\tau_{k} (A) = \sum_{\subseteq {1,...,n}  \det(A_{I,I}).$$
$$I}$$
$$|I|=k$$
Bài toán 15.9. $(1)$ Xét ma trận
$$A = \begin{pmatrix} 0 & 0 & -a_{3} \\ 1 & 0 & -a_{2} \\ 0 & 1 & a_{1} \end{pmatrix} .$$
$$-$$
Chứng minh rằng đa thức đặc trưng (characteristic polynomial) $\chi_{A} (z) =$ det(zI - $A)$ của $A$ được cho bởi
$$\chi_{A} (z) = z^{3}+ a_{1}z^{2}+ a_{2}z + a_{3}.$$
$(2)$ Xét ma trận
$$A = \begin{pmatrix} 0 & 0 & 0 & -a_{4} \\ 1 & 0 & 0 & -a_{3} \\ 0 & 1 & 0 & -a_{2} \\ 0 & 0 & 1 & a_{1} \end{pmatrix} .$$
$$-$$
Chứng minh rằng đa thức đặc trưng (characteristic polynomial) $\chi_{A} (z) =$ det(zI - $A)$ của $A$ được cho bởi
$$\chi_{A} (z) = z^{4}+ a_{1}z^{3}+ a_{2}z^{2}+ a_{3}z + a_{4}.$$

<!-- PAGE 593 -->
$(3)$ Xét ma trận cỡ $n \times  n$ (được gọi là companion ma trận)
$$A = \begin{pmatrix} 0 & 0 & 0 & \cdots & 0 & -a_{n} \\ 1 & 0 & 0 & \cdots & 0 & -a_{n-1} \\ 0 & 1 & 0 & \cdots & 0 & -a_{n-2} \\ \vdots & \ddots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \ddots & 0 & -a_{2} \\ 0 & 0 & 0 & 1 & a_{1} \end{pmatrix} .$$
$$\cdots -$$
Chứng minh rằng đa thức đặc trưng (characteristic polynomial) $\chi_{A} (z) =$ det(zI - $A)$ của $A$ được cho bởi
$$\chi_{A} (z) = z^{n}+ a_{1}z^{n-1}+ a_{2}z^{n-2}+ \cdots  + a_{n-1}z + a_{n}.$$
Hint. Sử dụng quy nạp. Giải thích tại sao việc tìm các nghiệm của đa thức (với thực hoặc phức các hệ số) và việc tìm các trị riêng (eigenvalues) của (thực hoặc phức) ma trận là tương đương các bài tập, trong nghĩa rằng nếu ta có phương pháp cho việc giải một của các bài tập này, thì ta có phương pháp để giải khác.
Bài toán 15.10. Cho $A$ là phức $n \times  n$ ma trận. Chứng minh rằng nếu $A$ là khả nghịch và nếu các trị riêng (eigenvalues) của $A$ là $(\lambda_{1} , \dots  , \lambda_{n}$), thì các trị riêng (eigenvalues) của $A^{-1}$ là $(\lambda_{1}^{-1}  , \dots  , \lambda_{n}^{-1}$). Chứng minh rằng nếu $u$ là vectơ riêng (eigenvector) của $A$ cho $\lambda_{i}$, thì $u$ là vectơ riêng (eigenvector) của $A^{-1}$ cho $\lambda_{i}^{-1}$.
Bài toán 15.11. Chứng minh rằng mọi phức ma trận là giới hạn của dãy của chéo hóa được (diagonalizable) các ma trận rằng có phân biệt các trị riêng (eigenvalues).
Bài toán 15.12. Xét sau đây ba đường chéo $n \times  n$ các ma trận
$$A = \begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ \ddots & \ddots & \ddots \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{pmatrix} ,S = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ \ddots & \ddots & \ddots \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix} .$$
Nhận thấy rằng $A =$ 2I - $S$ và chỉ ra rằng các trị riêng (eigenvalues) của $A$ là $\lambda_{k}  = 2$ - $\mu_{k}$, ở đâu $\mu_{k}$ là các trị riêng (eigenvalues) của $S$.
$(2)$ Bằng cách sử dụng Bài toán 10.6, chứng minh rằng các trị riêng (eigenvalues) của ma trận $A$ được cho bởi
$$\lambda_{k}  = 4 \sin^{2} \begin{pmatrix} k\pi \\ 2(n + 1) \end{pmatrix} ,k = 1, \dots  , n.$$
Chỉ ra rằng $A$ là đối xứng xác định dương (SPD).
$(3)$ Tìm số điều kiện (condition number) của $A$ đối với 2-chuẩn (norm).
$(4)$ Chỉ ra rằng vectơ riêng (eigenvector) $(y_{1}^{(k)} , \dots  , y_{n}^{(k)}$) liên kết wih trị riêng (eigenvalue) $\lambda_{k}$ được cho bởi
$$y_{j}^{(k)}= \sin \begin{pmatrix} kj\pi \\ n + 1 \end{pmatrix} ,j = 1, \dots  , n.$$

<!-- PAGE 594 -->
Bài toán 15.13. Xét sau đây thực ba đường chéo đối xứng $n \times  n$ ma trận
$$A = \begin{pmatrix} c & 1 & 0 \\ 1 & c & 1 \\ \ddots & \ddots & \ddots \\ 1 & c & 1 \\ 0 & 1 & c \end{pmatrix} .$$
$(1)$ Bằng cách sử dụng Bài toán 10.6, chứng minh rằng các trị riêng (eigenvalues) của ma trận $A$ được cho bởi
$$\lambda_{k}  = c + 2 \cos \begin{pmatrix} k\pi \\ n + 1 \end{pmatrix} ,k = 1, \dots  , n.$$
$(2)$ Tìm điều kiện trên $c$ sao cho $A$ là xác định dương (positive definite). Nó được thỏa mãn bởi $c = 4$?
Bài toán 15.14. Cho $A$ là một ma trận cỡ $m \times  n$ và $B$ là một ma trận cỡ $n \times  m$ (trên $\mathbb{C})$.
$(1)$ Chứng minh rằng
$$\det(I_{m} -AB) = \det(I_{n} -BA).$$
Hint. Xét các ma trận
$$X = \begin{pmatrix} I_{m} & A \\ B & I_{n} \end{pmatrix} andY = \begin{pmatrix} I \\ 0 \\ -^{m}B & I_{n} \end{pmatrix} .$$
$(2)$ Chứng minh rằng
$$\lambda^{n} \det(\lambda I_{m} -AB) = \lambda^{m} \det(\lambda I_{n} -BA).$$
Hint. Xét các ma trận
$$X = \begin{pmatrix} \lambda I_{m} & A \\ B & I_{n} \end{pmatrix} andY = \begin{pmatrix} I \\ 0 \\ -^{m}B & \lambda I_{n} \end{pmatrix} .$$
Suy ra rằng $AB$ và BA có cùng khác không các trị riêng (eigenvalues) với cùng bội (multiplicity).
Bài toán 15.15. mục đích của bài toán này là để chứng minh rằng đa thức đặc trưng (characteristic polynomial) của ma trận
$$A = \begin{pmatrix} 1 & 2 & 3 & 4 & \cdots & n \\ 2 & 3 & 4 & 5 & \cdots & n + 1 \\ 3 & 4 & 5 & 6 & \cdots & n + 2 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ n & n + 1 & n + 2 & n + 3 & \cdots & 2n -1 \end{pmatrix}$$
Là
$$P_{A}(\lambda ) = \lambda^{n-2} \begin{pmatrix} 1 & - \\ \lambda^{2} -n^{2}\lambda  - & n^{2}(n^{2} & 1) \\ 12 \end{pmatrix} .$$

<!-- PAGE 595 -->
$(1)$ Chứng minh rằng đa thức đặc trưng (characteristic polynomial) $P_{A}(\lambda$) được cho bởi
$$P_{A}(\lambda ) = \lambda^{n-2} P(\lambda ),$$
Với
$$\lambda  -1-2-3-4\cdots -n + 3-n + 2-n + 1-n$$
$$-\lambda  -1\lambda  -1-1-1\cdots -1-1-1-1$$
$$1-210\cdots 0000$$
$$01-21\cdots 0000$$
$$\vdots \vdots \ddots \ddots \ddots \vdots \vdots \vdots \vdots$$
$$P(\lambda ) =.$$
$$\ddots$$
$$00001000$$
$$\ddots$$
$$0000-2100$$
$$0000\cdots 1-210$$
$$0000\cdots 01-21$$
$(2)$ Chứng minh rằng tổng của các nghiệm $\lambda_{1} , \lambda_{2}$ của (bậc hai) đa thức $P(\lambda$) là
$$\lambda_{1}  + \lambda_{2}  = n^{2}.$$
Bài toán là do đó để tính tích $\lambda_{1} \lambda_{2}$ của các phần tử này các nghiệm. Chứng minh rằng
$$\lambda_{1} \lambda_{2}  = P(0).$$
$(3)$ bài toán là bây giờ đến tính giá trị $d_{n} =$ P(0), ở đâu
$$-1-2-3-4\cdots -n + 3-n + 2-n + 1-n$$
$$-1-1-1-1\cdots -1-1-1-1$$
$$1-210\cdots 0000$$
$$01-21\cdots 0000$$
$$\vdots \vdots \ddots \ddots \ddots \vdots \vdots \vdots \vdots$$
$$d_{n} =$$
$$\ddots$$
$$00001000$$
$$\ddots$$
$$0000-2100$$
$$0000\cdots 1-210$$
$$0000\cdots 01-21$$
I suggest sau đây chiến lược: cancel ra phần tử thứ nhất trong hàng $1$ và hàng $2$ bằng cách cộng phù hợp bội của hàng $3$ đến hàng $1$ và hàng $2$, và thì trừ hàng $2$ từ hàng $1$.

<!-- PAGE 596 -->
Thực hiện điều này hai lần. Bạn sẽ chú ý rằng thứ nhất hai các phần tử (entries) trên hàng $1$ và thứ nhất hai các phần tử (entries) trên hàng $2$ thay đổi, nhưng rest của ma trận trông cùng, ngoại trừ rằng số chiều là rút gọn. Điều này suggests đặt lên recurrence liên quan đến các phần tử (entries) $u_{k}, v_{k}, x_{k}, y_{k}$ trong định thức (determinant)
$$u_{k}x_{k}-3-4\cdots -n + k -3-n + k -2-n + k -1-n + k$$
$$v_{k}y_{k}-1-1\cdots -1-1-1-1$$
$$1-210\cdots 0000$$
$$01-21\cdots 0000$$
$$\vdots \vdots \ddots \ddots \ddots \vdots \vdots \vdots \vdots$$
$D_{k} =$,
$$\ddots$$
$$00001000$$
$$\ddots$$
$$0000-2100$$
$$0000\cdots 1-210$$
$$0000\cdots 01-21$$
Bắt đầu với $k = 0$, với
$$u_{0} = -1,v_{0} = -1,x_{0} = -2,y_{0} = -1,$$
Và kết thúc/cuối với $k = n$ - $2$, sao cho
$$u_{n-3}x_{n-3}-3$$
$$u_{n-2}x_{n-2}$$
$$d_{n} = D_{n-2} =v_{n-3}y_{n-3}-1= .$$
$$v_{n-2}y_{n-2}$$
$$1-21$$
Chứng minh rằng ta có recurrence các quan hệ
$$\begin{pmatrix} u_{k+1} \\ v_{k+1} \\ x_{k+1} \\ y_{k+1} \end{pmatrix} = \begin{pmatrix} 2 & -2 & 1 & -1 \\ 0 & 2 & 0 & 1 \\ -1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix} \begin{pmatrix} u_{k} \\ v_{k} \\ x_{k} \\ y_{k} \end{pmatrix} + \begin{pmatrix} 0 \\ 0 \\ -2 \\ 1 \end{pmatrix} .$$
$$--$$
Các phần tử này xuất hiện là nasty afin recurrence các quan hệ, do đó ta sẽ sử dụng mẹo/kỹ thuật đến chuyển đổi điều này ánh xạ afin (affine map) đến ánh xạ tuyến tính (linear map).
$(4)$ Xét ánh xạ tuyến tính (linear map) cho trước bởi
$$\begin{pmatrix} u_{k+1} \\ v_{k+1} \\ x_{k+1} \\ y_{k+1} \\ 1 \end{pmatrix} = \begin{pmatrix} 2 & -2 & 1 & -1 & 0 \\ 0 & 2 & 0 & 1 & 0 \\ -1 & 1 & 0 & 0 & -2 \\ 0 & -1 & 0 & 0 & -1 \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} u_{k} \\ v_{k} \\ x_{k} \\ y_{k} \\ 1 \end{pmatrix} ,$$

<!-- PAGE 597 -->
Và chỉ ra rằng của nó action trên $u_{k}, v_{k}, x_{k}, y_{k}$ là cùng như afin action của Phần $(3)$. Sử dụng Matlab để tìm các trị riêng (eigenvalues) của ma trận
$$T = \begin{pmatrix} 2 & -2 & 1 & -1 & 0 \\ 0 & 2 & 0 & 1 & 0 \\ -1 & 1 & 0 & 0 & -2 \\ 0 & -1 & 0 & 0 & -1 \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix} .$$
Bạn sẽ là stunned! Cho $N$ là ma trận cho trước bởi
$$N = T -I.$$
Chứng minh rằng
$$N^{4}= 0.$$
Sử dụng điều này để chứng minh rằng
$$+$$
$$T^{k} = I + kN + \frac{1}{2} k(k -1)N^{2} \frac{1}{6} k(k -1)(k -2)N^{3},$$
Với mọi $k \ge 0$.
$(5)$ Chứng minh rằng
$$k$$
$$\begin{pmatrix} u_{k} \\ v_{k} \\ x_{k} \\ y_{k} \\ 1 \end{pmatrix} = T^{k} \begin{pmatrix} -1 \\ -1 \\ -2 \\ -1 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 & -2 & 1 & -1 & 0 \\ 0 & 2 & 0 & 1 & 0 \\ -1 & 1 & 0 & 0 & -2 \\ 0 & -1 & 0 & 0 & -1 \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} -1 \\ -1 \\ -2 \\ -1 \\ 1 \end{pmatrix} ,$$
Cho $k \ge 0$. Chứng minh rằng
$$T^{k}  = \begin{pmatrix} k + 1 & -k(k + 1) & k & -k^{2} & 1(k -1)k(2k -7) \\ \overline{6} \\ 0 & k + 1 & 0 & k & -_{2}^{1}(k -1)k \\ -k & k^{2} & 1 -k & (k -1)k & -_{3}^{1}k((k -6)k + 11) \\ 0 & -k & 0 & 1 -k & 1(k -3)k \\ \overline{2} \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix} ,$$
Và do đó rằng
$$\begin{pmatrix} u_{k} \\ v_{k} \\ x_{k} \\ y_{k} \end{pmatrix} = \begin{pmatrix} 1(2k^{3} + 3k^{2} -5k -6) \\ \overline{6} \\ -_{2}^{1}(k^{2} + 3k + 2) \\ 1(-k^{3} + k -6) \\ \overline{3} \\ 1(k^{2} + k & 2) \end{pmatrix} ,$$
$$-$$
$$\overline{2}$$

<!-- PAGE 598 -->
Và rằng
$$u_{k}x_{k}$$
$$- -$$
$$v_{k}y_{k} = -1 - \frac{7}{3} k - \frac{23}{12} k^{2} \frac{2}{3} k^{3} \frac{1}{12} k^{4}.$$
Hệ quả là, chứng minh rằng amazingly
$$-$$
$$d_{n} = D_{n-2} = - \frac{1}{12} n^{2}(n^{2}1).$$
$(6)$ Chứng minh rằng đa thức đặc trưng (characteristic polynomial) của $A$ là thật vậy
$$P_{A}(\lambda ) = \lambda^{n-2} \begin{pmatrix} 1 & - \\ \lambda^{2} -n^{2}\lambda  - & n^{2}(n^{2} & 1) \\ 12 \end{pmatrix} .$$
Sử dụng ở trên để chỉ ra rằng hai khác không các trị riêng (eigenvalues) của $A$ là
$$\sqrt!$$
$$\lambda  = \frac{n}{2} n \pm \frac{\sqrt{3}}{3} \overline{4}\overline{n}^{2} \overline{-}\overline{1}.$$
Âm trị riêng (eigenvalue) $\lambda_{1}$ có thể cũng được biểu diễn như
$$-r$$
$$\lambda_{1}  = n^{2} \frac{(32\sqrt{3)}}{6} 1 - \frac{\overline{1}}{4n^{2}} .$$
Sử dụng điều này biểu thức đến giải thích sau đây hiện tượng: nếu ta cộng bất kỳ số greater hơn hoặc bằng $(2/25)n^{2}$ đến mọi đường chéo phần tử (entry) của $A$ ta thu được ma trận khả nghịch (invertible matrix). Những gì về $0.077351n^{2}$? Thử nó!
Bài toán 15.16. Cho $A$ là đối xứng ba đường chéo ma trận cỡ $n \times n$
$$A = \begin{pmatrix} b_{1} & c_{1} \\ c_{1} & b_{2} & c_{2} \\ c_{2} & b_{3} & c_{3} \\ \ddots & \ddots & \ddots \\ c_{n-2} & b_{n-1} & c_{n-1} \\ c_{n-1} & b_{n} \end{pmatrix} ,$$
Ở đâu nó được giả sử rằng $c_{i} \neq  0$ với mọi $i, 1 \le i \le n$ - $1$, và cho $A_{k}$ là $k \times$ k-submatrix bao gồm của thứ nhất $k$ các hàng và các cột của $A, 1 \le k \le n$. Ta định nghĩa các đa thức $P_{k}(x)$ như sau: $(0 \le k \le n)$.
$$P_{0}(x) = 1,$$
$$P_{1}(x) = b_{1} -x,$$
$$P_{k}(x) = (b_{k} -x)P_{k-1}(x) -c_{k-1}^{2}P_{k-2}(x),$$

<!-- PAGE 599 -->
Ở đâu $2 \le k \le n$.
$(1)$ Chứng minh các tính chất sau đây:
$(i) P_{k}(x)$ là đa thức đặc trưng (characteristic polynomial) của $A_{k}$, ở đâu $1 \le k \le n$.
(ii) $lim_{x\to -\infty} P_{k}(x) = +\infty$, ở đâu $1 \le k \le n$.
(iii) Nếu $P_{k}(x) = 0$, thì $P_{k-1}(x)P_{k+1}(x) < 0$, ở đâu $1 \le k \le n$ - $1$.
(iv) $P_{k}(x)$ có $k$ phân biệt thực các nghiệm rằng tách $k + 1$ các nghiệm của $P_{k+1}(x)$, ở đâu $1 \le k \le n$ - $1$.
$(2)$ Cho trước bất kỳ thực số $\mu  > 0$, với mọi $k, 1 \le k \le n$, định nghĩa hàm $sg_{k}(\mu$) như sau:
$$sign of P_{k}(\mu )if P_{k}(\mu ) \neq  0,$$
$$sg_{k}(\mu ) =$$
$$sign of P_{k-1}(\mu )if P_{k}(\mu ) = 0.$$
Ta encode dấu của dương số như $+$, và dấu của âm số như -. Thì cho E(k, $\mu$) được thứ tự danh sách
$$E(k, \mu ) = \langle +, sg_{1}(\mu ), sg_{2}(\mu ), \dots  , sg_{k}(\mu )\rangle ,$$
Và cho N(k, $\mu$) là số thay đổi của dấu giữa liên tiếp các dấu trong E(k, $\mu$). Chứng minh rằng $sg_{k}(\mu$) được xác định tốt (well-defined) và rằng N(k, $\mu$) là số của các nghiệm $\lambda$ của $P_{k}(x)$ sao cho $\lambda  < \mu$.
Nhận xét: ở trên có thể được được sử dụng để tính các trị riêng (eigenvalues) của (ba đường chéo) ma trận đối xứng (symmetric matrix) (phương pháp của Givens-Householder).

<!-- PAGE 600 -->
