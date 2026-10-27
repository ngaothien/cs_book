# Kronecker Tích Cách xây dựng của Haar Các ma trận


<!-- PAGE 160 -->
Dãy $u^{0} = (10, 15, 5, -2, 1, 3, 1, 1) u^{1} = (10 + 15, 10$ - $15, 5, -2, 1, 3, 1, 1) = (25, -5, 5, -2, 1, 3, 1, 1) u^{2} = (25 + 5, 25$ - $5, -5 + (-2), -5$ - $(-2), 1, 3, 1, 1) = (30, 20, -7, -3, 1, 3, 1, 1) u^{3} = (30 + 1, 30$ - $1, 20 + 3, 20$ - $3, -7 + 1, -7$ - $1, -3 + 1, -3$ - $1)$
$$= (31, 29, 23, 17, -6, -8, -2, -4),$$
Mà cho quay lại $u = (31, 29, 23, 17, -6, -8, -2, -4)$.

## 5.3 Kronecker Tích Cách xây dựng của Haar Các ma trận

Ở đó là một cái khác đệ quy phương pháp cho xây dựng Haar ma trận $W_{n}$ có số chiều $2^{n}$ rằng làm cho nó clearer tại sao các cột của $W_{n}$ là đôi một trực giao, và tại sao ở trên các thuật toán là thật vậy đúng (mà nobody dường như để chứng minh!). Nếu ta split $W_{n}$ vào hai ma trận cỡ $2^{n} \times  2^{n-1}$, thì thứ hai ma trận chứa cuối cùng $2^{n-1}$ các cột của $W_{n}$ có rất đơn giản cấu trúc: nó bao gồm của vectơ
$$(1, -1, 0, \dots  , 0)$$
$$|{z}$$
$$2n$$
Và $2^{n-1}$ - $1$ shifted copies của nó, như được minh họa ở dưới cho $n = 3$:
$$\begin{pmatrix} 1 & 0 & 0 & 0 \\ -1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & -1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$-$$
Nhận thấy rằng ma trận này có thể được thu được từ ma trận đơn vị (identity matrix) $I_{2n-1}$, trong ví dụ của chúng ta
$$I_{4} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} ,$$
Bởi tạo thành ma trận cỡ $2^{n} \times  2^{n-1}$ thu được bằng cách thay thế mỗi $1$ bởi vectơ cột (column vector)
$$\begin{pmatrix} 1 \\ -1 \end{pmatrix}$$

<!-- PAGE 161 -->
Và mỗi không bởi vectơ cột (column vector)
$$\begin{pmatrix} 0 \\ 0 \end{pmatrix} .$$
Bây giờ thứ nhất một nửa của $W_{n}$, nghĩa là ma trận bao gồm của thứ nhất $2^{n-1}$ các cột của $W_{n}$, có thể được thu được từ $W_{n-1}$ bởi tạo thành ma trận cỡ $2^{n} \times 2^{n-1}$ thu được bằng cách thay thế mỗi $1$ bởi vectơ cột (column vector)
$$\begin{pmatrix} 1 \\ 1 \end{pmatrix} ,$$
Mỗi $-1$ bởi vectơ cột (column vector)
$$\begin{pmatrix} -1 \\ -1 \end{pmatrix} ,$$
Và mỗi không bởi vectơ cột (column vector)
$$\begin{pmatrix} 0 \\ 0 \end{pmatrix} .$$
Cho $n = 3$, thứ nhất một nửa của $W_{3}$ là ma trận
$$\begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 1 & 1 & 0 \\ 1 & 1 & -1 & 0 \\ 1 & 1 & -1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & -1 & 0 & 1 \\ 1 & -1 & 0 & -1 \\ 1 & 1 & 0 & 1 \end{pmatrix}$$
$$--$$
Mà là thật vậy thu được từ
$$W_{2} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 1 & -1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & 0 & 1 \end{pmatrix}$$
$$--$$
Bằng cách sử dụng process rằng ta chỉ được mô tả. ma trận này manipulations có thể được được mô tả một cách thuận tiện bằng cách sử dụng tích phép toán trên các ma trận đã biết như Kronecker tích.

> **Định nghĩa 5.4.** Cho trước một ma trận cỡ $m\times n$ $A = (a_{ij})$ và một ma trận cỡ $p\times q$ $B = (b_{ij})$, Kronecker tích (hoặc tích tenxơ (tensor product)) $A \otimes B$ của $A$ và $B$ là mp $\times$ nq ma trận
$$A \otimes B = \begin{pmatrix} a_{11}B & a_{12}B & \cdots & a_{1n}B \\ a_{21}B & a_{22}B & \cdots & a_{2n}B \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1}B & a_{m2}B & \cdots & a_{mn}B \end{pmatrix} .$$
