# Nghịch đảo Các ma trận và Các định thức


<!-- PAGE 236 -->
Vì $det(e_{1}, \dots  , e_{n}) = 1$. Bây giờ đặt
$$\begin{pmatrix} v_{1} \\ v_{2} \\ \vdots \\ v_{n} \end{pmatrix} = B \begin{pmatrix} e_{1} \\ e_{2} \\ \vdots \\ e_{n} \end{pmatrix} ,$$
Ta thu được
$$\det(v_{1}, \dots  , v_{n}) = \det(B),$$
Và vì
$$\begin{pmatrix} w_{1} \\ w_{2} \\ \vdots \\ w_{n} \end{pmatrix} = A \begin{pmatrix} v_{1} \\ v_{2} \\ \vdots \\ v_{n} \end{pmatrix} ,$$
Ta thu được
$$\det(w_{1}, \dots  , w_{n}) = \det(A) \det(v_{1}, \dots  , v_{n}) = \det(A) \det(B).$$
Nó nên được lưu ý rằng tất cả các kết quả của điều này mục, sai khác bây giờ, cũng đúng khi $K$ là vành giao hoán (commutative ring) và không nhất thiết trường. Ta có thể bây giờ đặc trưng hóa khi một ma trận cỡ $n\times n$ $A$ là khả nghịch theo định thức (định thức (determinant)) của nó det().

## 7.4 Nghịch đảo Các ma trận và Các định thức

Trong tiếp theo hai các mục, $K$ là vành giao hoán (commutative ring) và khi cần thiết trường.

> **Định nghĩa 7.7.** Cho $K$ là vành giao hoán (commutative ring). Cho trước ma trận $A \in M_{n}(K)$, cho $A = (b_{i j})$
$$e$$
Là ma trận được định nghĩa sao cho
$$b_{i j} = (-1)^{i+j}\det(A_{j i}),$$
Phần bù đại số (cofactor) của $a_{j i}$. ma trận $A$ được gọi là adjugate của $A$, và mỗi ma trận $A_{j i}$ được gọi là
$$e$$
Định thức con (minor) của ma trận $A$. Ví dụ, nếu
$$A = \begin{pmatrix} 1 & 1 & 1 \\ 2 & -2 & -2 \\ 3 & 3 & 3 \end{pmatrix} ,$$
$$-$$

<!-- PAGE 237 -->
Ta có
$$-2-2



11$$
$$b_{11} = \det(A_{11}) = = 12b_{12} = -\det(A_{21}) = - = 6$$
$$3-33-3$$
$$11



2-2$$
$$b_{13} = \det(A_{31}) = = 0b_{21} = -\det(A_{12}) = - = 0$$
$$-2-23-3$$
$$11



11$$
$$b_{22} = \det(A_{22}) = = -6b_{23} = -\det(A_{32}) = - = 4$$
$$3-32-2$$
$$2-2



11$$
$$b_{31} = \det(A_{13}) = = 12b_{32} = -\det(A_{23}) = - = 0$$
$$3333$$
$$11$$
$$b_{33} = \det(A_{33}) = = -4,$$
$$2-2$$
Ta tìm rằng
$$Ae = \begin{pmatrix} 12 & 6 & 0 \\ 0 & -6 & 4 \\ 12 & 0 & 4 \end{pmatrix} .$$
$$-$$
 Lưu ý reversal của các chỉ số trong
$$b_{i j} = (-1)^{i+j}\det(A_{j i}).$$
Do đó, $A$ là chuyển vị (transpose) của ma trận của các phần bù đại số (cofactor) của các phần tử của $A. e$ Ta có kết quả sau mệnh đề.

> **Mệnh đề 7.10.** Cho $K$ là vành giao hoán (commutative ring). Với mọi ma trận $A \in M_{n}(K)$, ta có
$$AA =AA = \det(A)I_{n}.$$
$$e e$$
Hệ quả là, $A$ là khả nghịch khi và chỉ khi det() là khả nghịch, và nếu do đó, $A^{-1} = (det(A))^{-1}A$.
$$e$$

*Chứng minh.* Nếu $A = (b_{i j})$ và $AA = (c_{i j})$, ta biết rằng phần tử (entry) $c_{i j}$ trong hàng $i$ và cột $j$ của $AA$
$$e e e$$
Là
$$c_{i j} = a_{i1}b_{1j} + \cdots  + a_{i k}b_{k j} + \cdots  + a_{i n}b_{n j},$$
Mà bằng
$$a_{i1}(-1)^{j+1}\det(A_{j1}) + \cdots  + a_{i n}(-1)^{j+n}\det(A_{j n}).$$
Nếu $j = i$, thì ta recognize biểu thức của expansion của det() theo hàng thứ $i$:
$$c_{i i} = \det(A) = a_{i1}(-1)^{i+1}\det(A_{i1}) + \cdots  + a_{i n}(-1)^{i+n}\det(A_{i n}).$$
Nếu j̸ $= i$, ta có thể tạo thành ma trận ' bằng cách thay thế hàng thứ $j$ của $A$ bởi hàng thứ $i$ của $A$. Bây giờ ma trận $A_{j k}$ thu được bởi xóa hàng $j$ và cột $k$ từ $A$ bằng ma trận

<!-- PAGE 238 -->
$A_{j k}'$ thu được bởi xóa hàng $j$ và cột $k$ từ ', vì $A$ và ' chỉ khác nhau bởi hàng thứ $j$. Do đó,
$$\det(A_{j k}) = \det(A_{j k}'),$$
Và ta có
$$\det($$
$$c_{i j} = a_{i1}(-1)^{j+1}\det(A_{j1}') + \cdots  + a_{i n}(-1)^{j+n}A_{j n}').$$
Tuy nhiên, điều này là expansion của det(') theo hàng thứ $j$, vì hàng thứ $j$ của ' bằng hàng thứ $i$ của $A$. Hơn nữa, vì ' có hai đồng nhất các hàng $i$ và $j$, bởi vì det là thay phiên ánh xạ của các hàng (xem trước đó nhận xét), ta có det(') $= 0$. Do đó, ta có được hiển thị rằng $c_{i i} =$ det(), và $c_{i j} = 0$, khi $j \neq  i$, và do đó
$$AA = \det(A)I_{n}.$$
$$e$$
Nó là cũng hiển nhiên từ định nghĩa của $A$, rằng
$$e$$
$$A^{\top}=A^{\top}.$$
$$ef$$
Thì áp dụng phần thứ nhất của lập luận đến $A^{\top}$, ta có
$$A^{\top}A^{\top}= \det(A^{\top})I_{n},$$
$$f$$
Và vì $det(A^{\top}) =$ det(), $A^{\top} = A^{\top}$, và $(AA)^{\top} = A^{\top}A^{\top}$, ta thu được
$$efee$$
$$\det(A)I_{n} = A^{\top}A^{\top}= A^{\top}A^{\top}= (AA)^{\top},$$
$$fee$$
Rằng là,
$$(AA)^{\top}= \det(A)I_{n},$$
$$e$$
Mà cho ta
$$AA = \det(A)I_{n},$$
$$e$$
Vì $I_{n}^{\top} = I_{n}$. Điều này chứng tỏ rằng
$$AA =AA = \det(A)I_{n}.$$
$$e e$$
Hệ quả là, nếu det() là khả nghịch, ta có $A^{-1} = (det(A))^{-1}A$. Ngược lại, nếu $A$ là
$$e$$
Khả nghịch, từ $AA^{-1} = I_{n}$, theo Mệnh đề 7.9, ta có det() $det(A^{-1}) = 1$, và det() là khả nghịch. Ví dụ, ta đã thấy trước đó rằng
$$A = \begin{pmatrix} 1 & 1 & 1 \\ 2 & -2 & -2 \\ 3 & 3 & 3 \end{pmatrix} andAe = \begin{pmatrix} 12 & 6 & 0 \\ 0 & -6 & 4 \\ 12 & 0 & 4 \end{pmatrix} ,$$
$$--$$
