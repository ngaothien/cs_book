# Các hệ của Các phương trình tuyến tính và Các định thức


<!-- PAGE 239 -->
Và ta có
$$\begin{pmatrix} 1 & 1 & 1 \\ 2 & -2 & -2 \\ 3 & 3 & 3 \end{pmatrix} \begin{pmatrix} 12 & 6 & 0 \\ 0 & -6 & 4 \\ 12 & 0 & 4 \end{pmatrix} = 24 \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$
$$--$$
Với det() $= 24$. Khi $K$ là trường, phần tử $a \in K$ là khả nghịch khi và chỉ khi $a \neq  0$. Trong trường hợp này, phần thứ hai của mệnh đề có thể được được phát biểu như $A$ là khả nghịch khi và chỉ khi det() $\neq  0$. Lưu ý trong chuyển rằng phương pháp này của việc tính toán nghịch đảo của ma trận là thường không thực tế.

## 7.5 Các hệ của Các phương trình tuyến tính và Các định thức

Ta bây giờ xét một số các ứng dụng của các định thức đến sự độc lập tuyến tính (linear independence) và đến việc giải các hệ của các phương trình tuyến tính. Mặc dù các kết quả này đúng cho các ma trận trên nhất định các vành, của chúng các chứng minh đòi hỏi nhiều hơn/thêm sophisticated các phương pháp. Vì vậy, ta giả sử một lần nữa rằng $K$ là trường (thường, $K =\mathbb{R}$ hoặc $K =\mathbb{C})$. Cho $A$ là một ma trận cỡ $n \times n$, $x$ các vectơ cột của các biến, và $b$ một cái khác vectơ cột (column vector), và cho $A^{1}, \dots  , A^{n}$ ký hiệu các cột của $A$. Nhận thấy rằng hệ của các phương trình Ax $= b$,
$$\begin{pmatrix} a_{1 1} & a_{1 2} & \dots & a_{1n} \\ a_{2 1} & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \dots & a_{n n} \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ \vdots \\ x_{n} \end{pmatrix} = \begin{pmatrix} b_{1} \\ b_{2} \\ \vdots \\ b_{n} \end{pmatrix}$$
Là tương đương đến
$$x_{1}A^{1}+ \cdots  + x_{j}A^{j}+ \cdots  + x_{n}A^{n}= b,$$
Vì phương trình tương ứng với hàng thứ $i$ là trong cả hai các trường hợp
$$a_{i1}x_{1} + \cdots  + a_{i j}x_{j} + \cdots  + a_{i n}x_{n} = b_{i}.$$
Thứ nhất ta đặc trưng hóa sự độc lập tuyến tính (linear independence) của các vectơ cột của ma trận $A$ theo định thức (định thức (determinant)) của nó.

> **Mệnh đề 7.11.** Cho trước một ma trận cỡ $n \times n$ $A$ trên trường $K$, các cột $A^{1}, \dots  , A^{n}$ của $A$ là phụ thuộc tuyến tính (linearly dependent) khi và chỉ khi det() $= det(A^{1}, \dots  , A^{n}) = 0$. Tương đương, $A$ có hạng (rank) $n$ khi và chỉ khi det() $\neq  0$.

*Chứng minh.* Thứ nhất giả sử rằng các cột $A^{1}, \dots  , A^{n}$ của $A$ là phụ thuộc tuyến tính (linearly dependent). Thì có $x_{1}, \dots  , x_{n} \in K$, sao cho
$$x_{1}A^{1}+ \cdots  + x_{j}A^{j}+ \cdots  + x_{n}A^{n}= 0,$$

<!-- PAGE 240 -->
Ở đâu $x_{j} \neq  0$ với một số $j$. Nếu ta tính $det(A^{1}, \dots  , x_{1}A^{1} + \cdots  + x_{j}A^{j} + \cdots  + x_{n}A^{n}, \dots  , A^{n}) = det(A^{1}, \dots  , 0, \dots  , A^{n}) = 0$, ở đâu $0$ xảy ra trong thứ $j$ position. Bởi tính đa tuyến tính, tất cả các số hạng chứa hai đồng nhất các cột $A^{k}$ cho $k \neq  j$ triệt tiêu, và ta thu được
$$\det(A^{1}, \dots  , x_{1}A^{1}+ \cdots  + x_{j}A^{j}+ \cdots  + x_{n}A^{n}, \dots  , A^{n}) = x_{j} \det(A^{1}, \dots  , A^{n}) = 0.$$
Vì $x_{j} \neq  0$ và $K$ là trường, ta phải có $det(A^{1}, \dots  , A^{n}) = 0$. Ngược lại, ta chỉ ra rằng nếu các cột $A^{1}, \dots  , A^{n}$ của $A$ là độc lập tuyến tính (linearly independent), thì $det(A^{1}, \dots  , A^{n})̸ = 0$. Nếu các cột $A^{1}, \dots  , A^{n}$ của $A$ là độc lập tuyến tính (linearly independent), thì chúng tạo thành cơ sở (basis) của $K^{n}$, và ta có thể biểu diễn tiêu chuẩn cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $K^{n}$ theo $A^{1}, \dots  , A^{n}$. Do đó, ta có
$$\begin{pmatrix} e_{1} \\ e_{2} \\ \vdots \\ e_{n} \end{pmatrix} = \begin{pmatrix} b_{1 1} & b_{1 2} & \dots & b_{1n} \\ b_{2 1} & b_{2 2} & \dots & b_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ b_{n1} & b_{n2} & \dots & b_{n n} \end{pmatrix} \begin{pmatrix} A^{1} \\ A^{2} \\ \vdots \\ A^{n} \end{pmatrix} ,$$
Với một số ma trận $B = (b_{i j})$, và theo Mệnh đề 7.8, ta thu được
$$\det(e_{1}, \dots  , e_{n}) = \det(B) \det(A^{1}, \dots  , A^{n}),$$
Và vì $det(e_{1}, \dots  , e_{n}) = 1$, điều này suy ra rằng $det(A^{1}, \dots  , A^{n}) \neq  0$ (và det(B) $\neq  0)$. Cho thứ hai assertion, nhắc lại rằng hạng (rank) của ma trận bằng cực đại số của các cột độc lập tuyến tính, và conclusion là rõ ràng. Ta bây giờ đặc trưng hóa khi hệ của các phương trình tuyến tính của tạo thành Ax $= b$ có duy nhất nghiệm.

> **Mệnh đề 7.12.** Cho trước một ma trận cỡ $n \times n$ $A$ trên trường $K$, các tính chất sau đây đúng:
$(1)$ Với mọi vectơ cột (column vector) $b$, tồn tại duy nhất một vectơ cột (column vector) $x$ sao cho Ax $= b$ khi và chỉ khi chỉ nghiệm đến Ax $= 0$ là tầm thường vectơ $x = 0$, khi và chỉ khi det() $\neq  0$.
$(2)$ Nếu det() $\neq  0$, duy nhất nghiệm của Ax $= b$ được cho bởi các biểu thức
$$x_{j} = \frac{\det(A^{1}, \dots  , A^{j-1}, b, A^{j+1}, \dots  , A^{n})}{\det(A^{1}, \dots  , A^{j-1}, A^{j}, A^{j+1}, \dots  , A^{n})} ,$$
Đã biết như Cramer’s các quy tắc.
$(3)$ hệ của các phương trình tuyến tính Ax $= 0$ có khác không nghiệm khi và chỉ khi det() $= 0$.
