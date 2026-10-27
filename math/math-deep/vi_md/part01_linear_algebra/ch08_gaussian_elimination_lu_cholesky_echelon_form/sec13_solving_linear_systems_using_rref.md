# Việc giải Các hệ phương trình tuyến tính Bằng cách sử dụng RREF


<!-- PAGE 312 -->

## 8.13 Việc giải Các hệ phương trình tuyến tính Bằng cách sử dụng RREF

Thứ nhất ta có kết quả sau đơn giản kết quả.
$$\mathbb{R}^{m}$$

> **Mệnh đề 8.20.** Cho $A$ là bất kỳ ma trận cỡ $m \times  n$ và cho $b \in$ là bất kỳ vectơ. Nếu hệ Ax $= b$ có nghiệm, thì tập hợp $Z$ của tất cả các nghiệm của hệ này là tập hợp
$$Z = x_{0} + \mathrm{Ker} (A) = {x_{0} + x | Ax = 0},$$
$$\mathbb{R}^{n}$$
Ở đâu $x_{0} \in$ là bất kỳ nghiệm của hệ Ax $= b$, mà có nghĩa là $Ax_{0} = b (x_{0}$ được gọi là
$$\mathbb{R}^{n}$$
Đặc biệt nghiệm hoặc cụ thể nghiệm), và ở đâu Ker $(A) = {x \in$ | Ax $= 0}$, tập hợp của các nghiệm của thuần nhất hệ liên kết với Ax $= b$.

*Chứng minh.* Giả sử rằng hệ Ax $= b$ là giải được và cho $x_{0}$ và $x_{1}$ là bất kỳ hai các nghiệm sao cho $Ax_{0} = b$ và $Ax_{1} = b$. Trừ phương trình thứ nhất từ thứ hai, ta thu được
$$A(x_{1} -x_{0}) = 0,$$
Mà có nghĩa là $x_{1}$ - $x_{0} \in$ Ker $(A)$. Vì vậy, $Z \subseteq x_{0} +$ Ker $(A)$, ở đâu $x_{0}$ là đặc biệt nghiệm của Ax $= b$. Ngược lại, nếu $Ax_{0} = b$, thì với mọi $z \in$ Ker $(A)$, ta có Az $= 0$, và do đó
$$A(x_{0} + z) = Ax_{0} + Az = b + 0 = b,$$
Mà chỉ ra rằng $x_{0} +$ Ker $(A) \subseteq Z$. Vì vậy, $Z = x_{0} +$ Ker $(A)$. Cho trước hệ phương trình tuyến tính Ax $= b$, rút gọn ma trận mở rộng (augmented matrix) $(A, b)$ đến của nó dạng bậc thang theo hàng (row echelon form) (', b'). Như ta đã chỉ ra trước, hệ Ax $= b$ có nghiệm khi và chỉ khi b' chứa không có phần tử trụ (pivot). Giả sử rằng điều này là trường hợp. Thì, nếu (', b') có $r$ các phần tử trụ, mà có nghĩa là ' có $r$ các phần tử trụ vì b' có không có phần tử trụ (pivot), ta biết rằng thứ nhất $r$ các cột của $I_{m}$ xuất hiện trong '. Ta có thể hoán vị các cột của ' và renumber các biến trong $x$ một cách tương ứng sao cho thứ nhất $r$ các cột của $I_{m}$ match thứ nhất $r$ các cột của ', và thì của ta rút gọn bậc thang ma trận là của tạo thành $(R$, b') với
$$R = \begin{pmatrix} I_{r} & F \\ 0_{m-r,r} & 0_{m-r,n-r} \end{pmatrix}$$
Và
$$b'= \begin{pmatrix} d \\ 0_{m-r} \end{pmatrix} ,$$
Ở đâu $F$ là $r \times  (n$ - $r)$ ma trận và $d \in \mathbb{R}^{r}$. Lưu ý rằng $R$ có $m$ - $r$ không các hàng. Thì bởi vì
$$\begin{pmatrix} I_{r} & F \\ 0_{m-r,r} & 0_{m-r,n-r} \end{pmatrix} \begin{pmatrix} d \\ 0_{n-r} \end{pmatrix} = \begin{pmatrix} d \\ 0_{m-r} \end{pmatrix} = b',$$

<!-- PAGE 313 -->
Ta xem rằng
$$x_{0} = \begin{pmatrix} d \\ 0_{n-r} \end{pmatrix}$$
Là đặc biệt nghiệm của Rx $=$ b', và do đó đến Ax $= b$. Nói cách khác, ta thu được đặc biệt nghiệm bởi assigning thứ nhất $r$ các thành phần của b' đến phần tử trụ (pivot) các biến và đặt nonpivot các biến (tự do các biến) đến không. Đây là một ví dụ của trước đó cách xây dựng được lấy từ Kumpel và Thorpe $[110]$. hệ phương trình tuyến tính
$$x_{1} -x_{2} + x_{3} + x_{4} -2x_{5} = -1$$
$$-2x_{1} + 2x_{2} -x_{3} + x_{5} = 2$$
$$x_{1} -x_{2} + 2x_{3} + 3x_{4} -5x_{5} = -1,$$
Được biểu diễn bởi ma trận mở rộng (augmented matrix)
$$(A, b) = \begin{pmatrix} 1 & -1 & 1 & 1 & -2 & -1 \\ -2 & 2 & -1 & 0 & 1 & 2 \\ 1 & 1 & 2 & 3 & 5 & 1 \end{pmatrix} ,$$
$$---$$
Ở đâu $A$ là một ma trận cỡ $3 \times  5$. độc giả nên tìm rằng dạng bậc thang theo hàng (row echelon form) của hệ này là
$$(A', b') = \begin{pmatrix} 1 & -1 & 0 & -1 & 1 & -1 \\ 0 & 0 & 1 & 2 & -3 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{pmatrix} .$$
Ma trận cỡ $3 \times  5$ ' có hạng (rank) $2$. Ta hoán vị thứ hai và thứ ba các cột (mà là tương đương đến interchanging các biến $x_{2}$ và $x_{3})$ đến tạo thành
$$R = \begin{pmatrix} I_{2} & F \\ 0_{1,2} & 0_{1,3} \end{pmatrix} ,F = \begin{pmatrix} -1 & -1 & 1 \\ 0 & 2 & -3 \end{pmatrix} .$$
Thì đặc biệt nghiệm đến điều này hệ phương trình tuyến tính được cho bởi
$$x_{0} = \begin{pmatrix} d \\ 0_{3} \end{pmatrix} = \begin{pmatrix} -1 \\ 0 \\ 0_{3} \end{pmatrix} .$$
Ta có thể cũng tìm cơ sở (basis) của hạt nhân (kernel) (không gian hạch (nullspace)) của $A$ bằng cách sử dụng $F$. Nếu $x = (u, v)$ là trong
$$\mathbb{R}^{r} \mathbb{R}^{n-r}$$
Hạt nhân (kernel) của $A$, với $u \in$ và $v \in$, thì $x$ là cũng trong hạt nhân (kernel) của $R$, mà có nghĩa là Rx $= 0$; nghĩa là,
$$\begin{pmatrix} I_{r} & F \\ 0_{m-r,r} & 0_{m-r,n-r} \end{pmatrix} \begin{pmatrix} u \\ v \end{pmatrix} = \begin{pmatrix} u + Fv \\ 0_{m-r} \end{pmatrix} = \begin{pmatrix} 0_{r} \\ 0_{m-r} \end{pmatrix} .$$
Vì vậy, $u =$ -Fv, và Ker $(A)$ bao gồm của tất cả các vectơ của tạo thành
$$\begin{pmatrix} -Fv \\ v \end{pmatrix} = \begin{pmatrix} -F \\ I_{n-r} \end{pmatrix} v,$$

<!-- PAGE 314 -->
Với mọi tùy ý $v \in \mathbb{R}^{n-r}$. Suy ra rằng $n$ - $r$ các cột của ma trận
$$N = \begin{pmatrix} -F \\ I_{n-r} \end{pmatrix}$$
Tạo thành cơ sở (basis) của hạt nhân (kernel) của $A$. Điều này là bởi vì $N$ chứa ma trận đơn vị (identity matrix) $I_{n-r}$ như ma trận con, do đó các cột của $N$ là độc lập tuyến tính (linearly independent). Trong tóm tắt, nếu $N^{1}, \dots  , N^{n-r}$ là các cột của $N$, thì tổng quát nghiệm của phương trình Ax $= b$ được cho bởi
$$x = \begin{pmatrix} d \\ 0_{n-r} \end{pmatrix} + x_{r+1}N^{1}+ \cdots  + x_{n}N^{n-r},$$
Ở đâu $x_{r+1}, \dots  , x_{n}$ là tự do variables; nghĩa là, nonpivot các biến. Đi quay lại đến ví dụ của chúng ta từ Kumpel và Thorpe $[110]$, ta xem rằng
$$N = \begin{pmatrix} -F \\ I_{3} \end{pmatrix} = \begin{pmatrix} 1 & 1 & -1 \\ 0 & -2 & 3 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} .$$
Vì trước đó ta permuted thứ hai và cột thứ ba, hàng $2$ và hàng $3$ cần là swapped do đó tổng quát nghiệm theo ban đầu các biến được cho bởi
$$x = \begin{pmatrix} -1 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} + x_{3} \begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} + x_{4} \begin{pmatrix} 1 \\ 0 \\ -2 \\ 1 \\ 0 \end{pmatrix} + x_{5} \begin{pmatrix} -1 \\ 0 \\ 3 \\ 0 \\ 1 \end{pmatrix} .$$
Trong tổng quát trường hợp ở đâu các cột tương ứng với các phần tử trụ là mixed với các cột tương ứng với tự do các biến, ta tìm đặc biệt nghiệm như sau. Cho $i_{1} < \cdots  < i_{r}$ là các chỉ số của các cột tương ứng với các phần tử trụ. Assign $b_{k}'$ đến phần tử trụ (pivot) biến $x_{ik}$ cho $k = 1, \dots  , r$, và tập hợp tất cả khác các biến đến $0$. để tìm cơ sở (basis) của hạt nhân (kernel), ta tạo thành $n$ - $r$ các vectơ $N^{k}$ thu được như sau. Cho $j_{1} < \cdots  < j_{n-r}$ là các chỉ số của các cột tương ứng với tự do các biến. Với mọi cột $j_{k}$ tương ứng với tự do biến $(1 \le k \le n -r)$, tạo thành vectơ $N^{k}$ được định nghĩa sao cho các phần tử (entries) $N_{i}^{k}, \dots  , N_{i}^{k}$ bằng các âm của thứ nhất $r$ các phần tử (entries) trong cột $j_{k}$ (flip dấu của $these^{1} entries);^{r}$ cho $N_{jk}^{k}  = 1$, và tập hợp tất cả khác các phần tử (entries) đến không. Schematically, nếu cột của chỉ số $j_{k}$ (tương ứng với tự do biến $x_{jk})$ là
$$\begin{pmatrix} \alpha_{1} \\ \vdots \\ \alpha_{r} \\ 0 \\ \vdots \\ 0 \end{pmatrix} ,$$

<!-- PAGE 315 -->
Thì vectơ $N^{k}$ được cho bởi
$$1$$
$$\vdots$$
$$i_{1} -1$$
$$i_{1}$$
$$i_{1} + 1$$
$$\vdots$$
$$i_{r} -1 \begin{pmatrix} 0 \\ \vdots \\ 0 \\ -\alpha_{1} \\ 0 \\ \vdots \\ 0 \\ -\alpha_{r} \\ 0 \\ \vdots \\ 0 \\ 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}$$
$$i_{r}.$$
$$i_{r} + 1$$
$$\vdots$$
$$j_{k} -1$$
$$j_{k}$$
$$j_{k} + 1$$
$$\vdots$$
$$n$$
Presence của $1$ trong position $j_{k}$ các đảm bảo rằng $N^{1}, \dots  , N^{n-r}$ là độc lập tuyến tính (linearly independent). Như illustration của ở trên phương pháp, xét bài toán của việc tìm cơ sở (basis) của không gian con $V$ của $n \times  n$ các ma trận $A \in M_{n}(\mathbb{R})$ thỏa mãn các tính chất sau đây: $1$. tổng của các phần tử (entries) trong mọi hàng có cùng giá trị (nói $c_{1}); 2$. tổng của các phần tử (entries) trong mọi cột có cùng giá trị (nói $c_{2})$. Hóa ra là $c_{1} = c_{2}$ và rằng 2n-2 các phương trình tương ứng với ở trên các điều kiện là độc lập tuyến tính (linearly independent). Ta để lại chứng minh của các phần tử này các sự kiện như thú vị bài tập. Nó có thể được được hiển thị bằng cách sử dụng đối ngẫu định lý (Định lý 11.4) rằng số chiều của không gian $V$ của các ma trận satisying ở trên các phương trình là $n^{2}$ - (2n - $2)$. Cho chúng ta xét trường hợp $n = 4$. Có $6$ các phương trình, và không gian $V$ có số chiều $10$. các phương trình là
$$a_{11} + a_{12} + a_{13} + a_{14} -a_{21} -a_{22} -a_{23} -a_{24} = 0$$
$$a_{21} + a_{22} + a_{23} + a_{24} -a_{31} -a_{32} -a_{33} -a_{34} = 0$$
$$a_{31} + a_{32} + a_{33} + a_{34} -a_{41} -a_{42} -a_{43} -a_{44} = 0$$
$$a_{11} + a_{21} + a_{31} + a_{41} -a_{12} -a_{22} -a_{32} -a_{42} = 0$$
$$a_{12} + a_{22} + a_{32} + a_{42} -a_{13} -a_{23} -a_{33} -a_{43} = 0$$
$$a_{13} + a_{23} + a_{33} + a_{43} -a_{14} -a_{24} -a_{34} -a_{44} = 0,$$

<!-- PAGE 316 -->
Và tương ứng ma trận là
$$A = \begin{pmatrix} 1 & 1 & 1 & 1 & -1 & -1 & -1 & -1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & -1 & -1 & -1 & -1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & -1 & -1 & -1 & -1 \\ 1 & -1 & 0 & 0 & 1 & -1 & 0 & 0 & 1 & -1 & 0 & 0 & 1 & -1 & 0 & 0 \\ 0 & 1 & -1 & 0 & 0 & 1 & -1 & 0 & 0 & 1 & -1 & 0 & 0 & 1 & -1 & 0 \\ 0 & 0 & 1 & 1 & 0 & 0 & 1 & 1 & 0 & 0 & 1 & 1 & 0 & 0 & 1 & 1 \end{pmatrix} .$$
$$----$$
Kết quả của performing reduction đến dạng bậc thang theo hàng (row echelon form) cho ta sau đây ma trận trong rref:
$$U = \begin{pmatrix} 1 & 0 & 0 & 0 & 0 & -1 & -1 & -1 & 0 & -1 & -1 & -1 & 2 & 1 & 1 & 1 \\ 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & -1 & 0 & -1 & -1 \\ 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & -1 & -1 & 0 & -1 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & -1 & -1 & -1 & 0 \\ 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & -1 & -1 & -1 & -1 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \end{pmatrix}$$
$$----$$
Danh sách pivlist của các chỉ số của phần tử trụ (pivot) các biến và danh sách freelist của các chỉ số của tự do các biến được cho bởi
$$pivlist = (1, 2, 3, 4, 5, 9),$$
$$freelist = (6, 7, 8, 10, 11, 12, 13, 14, 15, 16).$$
Sau áp dụng thuật toán để tìm cơ sở (basis) của hạt nhân (kernel) của $U$, ta tìm sau đây $16 \times  10$ ma trận
$$BK = \begin{pmatrix} 1 & 1 & 1 & 1 & 1 & 1 & -2 & -1 & -1 & -1 \\ -1 & 0 & 0 & -1 & 0 & 0 & 1 & 0 & 1 & 1 \\ 0 & -1 & 0 & 0 & -1 & 0 & 1 & 1 & 0 & 1 \\ 0 & 0 & -1 & 0 & 0 & -1 & 1 & 1 & 1 & 0 \\ -1 & -1 & -1 & 0 & 0 & 0 & 1 & 1 & 1 & 1 \\ 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & -1 & -1 & -1 & 1 & 1 & 1 & 1 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \end{pmatrix} .$$
Độc giả nên kiểm tra rằng rằng trong mỗi cột $j$ của $BK$, lowest bold $1$ thuộc đến hàng có chỉ số là phần tử thứ $j$ trong freelist, và rằng trong mỗi cột $j$ của $BK$,

<!-- PAGE 317 -->
Các dấu của các phần tử (entries) có các chỉ số thuộc đến pivlist là flipped các dấu của $6$ các phần tử (entries) trong cột $U$ tương ứng với chỉ số thứ $j$ trong freelist. Ta có thể bây giờ read offfrom BK $4 \times  4$ các ma trận rằng tạo thành cơ sở (basis) của $V$: mọi cột của $BK$ tương ứng với ma trận có các hàng có đã được concatenated. Ta thu được sau đây $10$ các ma trận:
$$M_{1} = \begin{pmatrix} 1 & -1 & 0 & 0 \\ -1 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} ,M_{2} = \begin{pmatrix} 1 & 0 & -1 & 0 \\ -1 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} ,M_{3} = \begin{pmatrix} 1 & 0 & 0 & -1 \\ -1 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} ,$$
$$M_{4} = \begin{pmatrix} 1 & -1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ -1 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} ,M_{5} = \begin{pmatrix} 1 & 0 & -1 & 0 \\ 0 & 0 & 0 & 0 \\ -1 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} ,M_{6} = \begin{pmatrix} 1 & 0 & 0 & -1 \\ 0 & 0 & 0 & 0 \\ -1 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix} ,$$
$$M_{7} =,M_{8} = \begin{pmatrix} -1 & 0 & 1 & 1 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix} ,M_{9} = \begin{pmatrix} -1 & 1 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{pmatrix} ,$$
$$\begin{pmatrix} -2 & 1 & 1 & 1 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ -1 & 1 & 1 & 0 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$
$M_{10} =$. Nhắc lại rằng magic square là ma trận vuông (square matrix) rằng thỏa mãn hai các điều kiện về tổng của các phần tử (entries) trong mỗi hàng và trong mỗi cột là cùng số, và cũng additional hai các ràng buộc rằng chính descending và chính ascending các đường chéo cộng sai khác điều này chung/phổ biến số. Hơn nữa, các phần tử (entries) là cũng cần thiết là dương các số nguyên. Cho $n = 4$, additional hai các phương trình là
$$a_{22} + a_{33} + a_{44} -a_{12} -a_{13} -a_{14} = 0$$
$$a_{41} + a_{32} + a_{23} -a_{11} -a_{12} -a_{13} = 0,$$
Và $8$ các phương trình phát biểu rằng ma trận là magic square là độc lập tuyến tính (linearly independent). Một lần nữa, bởi chạy hàng phép khử, ta thu được cơ sở (basis) của “suy rộng/tổng quát hóa magic squares” có các phần tử (entries) là không bị thu hẹp là dương các số nguyên. Ta tìm cơ sở (basis) của $8$ các ma trận. Cho $n = 3$, ta tìm cơ sở (basis) của $3$ các ma trận. magic square được nói là chuẩn tắc/bình thường nếu các phần tử (các phần tử (entries)) của nó là một cách chính xác các số nguyên $1, 2 \dots  , n^{2}$. Khi đó vì tổng của các phần tử (các phần tử (entries)) này là
$$1 + 2 + 3 + \cdots  + n^{2}= \frac{n^{2}(n^{2} + 1)}{2} ,$$
