# Các bài tập


<!-- PAGE 174 -->

## 5.8 Các bài tập

Bài toán 5.1. (Haar extravaganza) Xét ma trận
$$W_{3,3} = \begin{pmatrix} 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 & -1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & -1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$-$$
$(1)$ Chỉ ra rằng cho trước bất kỳ vectơ $c = (c_{1}, c_{2}, c_{3}, c_{4}, c_{5}, c_{6}, c_{7}, c_{8})$, kết quả $W_{3,3}c$ của áp dụng $W_{3,3}$ đến $c$ là
$$W_{3,3}c = (c_{1} + c_{5}, c_{1} -c_{5}, c_{2} + c_{6}, c_{2} -c_{6}, c_{3} + c_{7}, c_{3} -c_{7}, c_{4} + c_{8}, c_{4} -c_{8}),$$
Bước cuối cùng trong reconstructing vectơ từ của nó Haar các hệ số.
$(2)$ Chứng minh rằng nghịch đảo của $W_{3,3}$ là $(1/2)W_{3,3}^{\top}$. Chứng minh rằng các cột và các hàng của $W_{3,3}$ là trực giao.
$(3)$ Cho $W_{3,2}$ và $W_{3,1}$ là sau đây các ma trận:
$$W_{3,2} = \begin{pmatrix} 1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ 1 & 0 & -1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & -1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \end{pmatrix} ,W_{3,1} = \begin{pmatrix} 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ 1 & -1 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \end{pmatrix} .$$
Chỉ ra rằng cho trước bất kỳ vectơ $c = (c_{1}, c_{2}, c_{3}, c_{4}, c_{5}, c_{6}, c_{7}, c_{8})$, kết quả $W_{3,2}c$ của áp dụng $W_{3,2}$ đến $c$ là
$$W_{3,2}c = (c_{1} + c_{3}, c_{1} -c_{3}, c_{2} + c_{4}, c_{2} -c_{4}, c_{5}, c_{6}, c_{7}, c_{8}),$$
Bước thứ hai trong reconstructing vectơ từ của nó Haar các hệ số, và kết quả $W_{3,1}c$ của áp dụng $W_{3,1}$ đến $c$ là
$$W_{3,1}c = (c_{1} + c_{2}, c_{1} -c_{2}, c_{3}, c_{4}, c_{5}, c_{6}, c_{7}, c_{8}),$$
Bước thứ nhất trong reconstructing vectơ từ của nó Haar các hệ số. Kết luận rằng
$$W_{3,3}W_{3,2}W_{3,1} = W_{3},$$

<!-- PAGE 175 -->
Haar ma trận
$$W_{3} = \begin{pmatrix} 1 & 1 & 1 & 0 & 1 & 0 & 0 & 0 \\ 1 & 1 & 1 & 0 & -1 & 0 & 0 & 0 \\ 1 & 1 & -1 & 0 & 0 & 1 & 0 & 0 \\ 1 & 1 & -1 & 0 & 0 & -1 & 0 & 0 \\ 1 & -1 & 0 & 1 & 0 & 0 & 1 & 0 \\ 1 & -1 & 0 & 1 & 0 & 0 & -1 & 0 \\ 1 & -1 & 0 & -1 & 0 & 0 & 0 & 1 \\ 1 & 1 & 0 & 1 & 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$---$$
Hint. Thứ nhất kiểm tra rằng
$$W_{3,2}W_{3,1} = \begin{pmatrix} W_{2} & 0_{4,4} \\ 0_{4,4} & I_{4} \end{pmatrix} ,$$
Ở đâu
$$W_{2} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 1 & -1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & 0 & 1 \end{pmatrix} .$$
$$--$$
$(4)$ Chứng minh rằng các cột và các hàng của $W_{3,2}$ và $W_{3,1}$ là trực giao. Suy ra từ điều này rằng các cột của $W_{3}$ là trực giao, và các hàng của $W_{3}^{-1}$ là trực giao. Là các hàng của $W_{3}$ trực giao? Là các cột của $W_{3}^{-1}$ trực giao? Tìm nghịch đảo của $W_{3,2}$ và nghịch đảo của $W_{3,1}$.
Bài toán 5.2. Điều này là continuation của Bài toán 5.1.
$(1)$ Với mọi $n \ge 2$, ma trận cỡ $2^{n} \times  2^{n}$ $W_{n,n}$ là thu được tạo thành hai các hàng
$$1, 0, \dots  , 0, 1, 0, \dots  , 0$$
$$|{z}|{z}$$
$$2n-12n-1$$
$$1, 0, \dots  , 0, -1, 0, \dots  , 0$$
$$|{z}|{z}$$
$$2n-12n-1$$
Bởi shifting chúng $2^{n-1}$ - $1$ lần trên đến phải bởi inserting không trên trái mỗi time. Cho trước bất kỳ vectơ $c = (c_{1}, c_{2}, \dots  , c_{2n})$, chỉ ra rằng $W_{n,n}c$ là kết quả của bước cuối cùng trong process của reconstructing vectơ từ của nó Haar các hệ số $c$. Chứng minh rằng $W_{n,n}^{-1}  = (1/2)W_{n,n}^{\top}$, và rằng các cột và các hàng của $W_{n,n}$ là trực giao.
$(2)$ Cho trước một ma trận cỡ $m \times  n$ $A = (a_{ij})$ và một ma trận cỡ $p \times  q$ $B = (b_{ij})$, Kronecker tích (hoặc tích tenxơ (tensor product)) $A \otimes B$ của $A$ và $B$ là mp $\times$ nq ma trận
$$A \otimes B = \begin{pmatrix} a_{11}B & a_{12}B & \cdots & a_{1n}B \\ a_{21}B & a_{22}B & \cdots & a_{2n}B \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1}B & a_{m2}B & \cdots & a_{mn}B \end{pmatrix} .$$

<!-- PAGE 176 -->
Nó có thể được được hiển thị (và bạn có thể sử dụng các phần tử này các sự kiện mà không có chứng minh) rằng $\otimes$ là kết hợp và rằng
$$(A \otimes B)(C \otimes D) = AC \otimes BD$$
$$(A \otimes B)^{\top}= A^{\top}\otimes B^{\top},$$
Bất cứ khi nào AC và BD là tốt được định nghĩa. Kiểm tra rằng
$$W_{n,n} = \begin{pmatrix} 1 \\ I_{2n-1}\otimes & 1 \end{pmatrix} \begin{pmatrix} 1 \\ I_{2n-1}\otimes & -1 \end{pmatrix} \begin{pmatrix}\end{pmatrix} ,$$
Và rằng
$$W_{n} = \begin{pmatrix} 1 \\ W_{n-1} \otimes & 1 \end{pmatrix} \begin{pmatrix} 1 \\ I_{2n-1}\otimes & -1 \end{pmatrix} \begin{pmatrix}\end{pmatrix} .$$
Sử dụng ở trên đến reprove rằng
$$W_{n,n}W_{n,n}^{\top}  = 2I_{2n}.$$
Cho
$$B_{1} = 2 \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$$
Và cho $n \ge 1$,
$$B_{n+1} = 2 \begin{pmatrix} B_{n} & 0 \\ 0 & I_{2n} \end{pmatrix} .$$
Chứng minh rằng
$$W_{n}^{\top}  W_{n} = B_{n},for all n \ge 1.$$
$(3)$ ma trận $W_{n,i}$ là thu được từ ma trận $W_{i,i} (1 \le i \le n$ - $1)$ như sau:
$$W_{n,i} = \begin{pmatrix} W_{i,i} & 0_{2i,2n-2i} \\ 0_{2n-2i,2i} & I_{2n-2i} \end{pmatrix} .$$
Nó bao gồm của bốn các khối, ở đâu $0_{2i,2n-2i}$ và $0_{2n-2i,2i}$ là các ma trận của các không điểm và $I_{2n-2i}$ là ma trận đơn vị (identity matrix) có số chiều $2^{n}$ - $2^{i}$. Giải thích những gì $W_{n,i}$ thực hiện đến $c$ và chứng minh rằng
$$W_{n,n}W_{n,n-1} \cdots  W_{n,1} = W_{n},$$
Ở đâu $W_{n}$ là Haar ma trận có số chiều $2^{n}$. Hint. Sử dụng quy nạp trên $k$, với giả thiết quy nạp (induction hypothesis)
$$W_{n,k}W_{n,k-1} \cdots  W_{n,1} = \begin{pmatrix} W_{k} & 0_{2k,2n-2k} \\ 0_{2n-2k,2k} & I_{2n-2k} \end{pmatrix} .$$

<!-- PAGE 177 -->
Chứng minh rằng các cột và các hàng của $W_{n,k}$ là trực giao, và sử dụng điều này để chứng minh rằng các cột của $W_{n}$ và các hàng của $W_{n}^{-1}$ là trực giao. Là các hàng của $W_{n}$ trực giao? Là các cột của $W_{n}^{-1}$ trực giao? Chứng minh rằng
$$W_{n,k}^{-1}  = \begin{pmatrix} 1W_{k,k}^{\top} & 0_{2k,2n-2k} \\ 0_{2n-2k,2k}^{2} & I_{2n-2k} \end{pmatrix} .$$
Bài toán 5.3. Chứng minh rằng nếu $H$ là Ma trận Hadamard (Hadamard matrix) có số chiều $n$, thì ma trận khối (block matrix) có số chiều 2n,
$$\begin{pmatrix} H & H \\ H & -H \end{pmatrix} ,$$
Là Ma trận Hadamard (Hadamard matrix).
Bài toán 5.4. Plot các đồ thị của tám Walsh các hàm Wal(k, $t)$ cho $k = 0, 1, \dots  , 7$.
Bài toán 5.5. Mô tả đệ quy thuật toán để tính tích $H_{2m} x$ của Sylvester– Ma trận Hadamard (Hadamard matrix) $H_{2m}$ bởi vectơ $x \in \mathbb{R}^{2m}$ rằng sử dụng $m$ đệ quy gọi.

<!-- PAGE 178 -->
