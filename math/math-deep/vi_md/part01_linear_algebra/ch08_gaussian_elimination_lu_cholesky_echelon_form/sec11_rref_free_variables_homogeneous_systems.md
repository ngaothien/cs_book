# RREF, Tự do Các biến, Thuần nhất Các hệ


<!-- PAGE 307 -->

## 8.11 RREF, Tự do Các biến, và Homogenous Tuyến tính

$$Systems$$
Cho trước hệ của tạo thành Ax $= b$, ta có thể áp dụng reduction quy trình đến ma trận mở rộng (augmented matrix) $(A, b)$ để thu được rút gọn hàng bậc thang ma trận (', b') sao cho hệ 'x $=$ b' có cùng các nghiệm như ban đầu hệ Ax $= b$. advantage của rút gọn hệ 'x $=$ b' là rằng có một đơn giản test để kiểm tra liệu hệ này là giải được, và để tìm các nghiệm của nó nếu nó là giải được. Thật vậy, nếu bất kỳ hàng của ma trận ' là không và nếu tương ứng phần tử (entry) trong b' là khác không, thì nó là phần tử trụ (pivot) và ta có “phương trình”
$$0 = 1,$$
Mà có nghĩa là hệ 'x $=$ b' có không có nghiệm. Mặt khác, nếu không có phần tử trụ (pivot) trong b', thì với mọi hàng $i$ trong mà $b_{i}'$ ̸ $= 0$, tồn tại một cột $j$ trong ' ở đâu phần tử (entry) trên hàng $i$ là $1$ (phần tử trụ (pivot)). Hệ quả là, ta có thể assign tùy ý các giá trị đến biến $x_{k}$ nếu cột $k$ thực hiện không chứa phần tử trụ (pivot), và thì giải cho phần tử trụ (pivot) các biến. Ví dụ, nếu ta xét rút gọn hàng bậc thang ma trận
$$(A', b') = \begin{pmatrix} 1 & 6 & 0 & 1 & 0 \\ 0 & 0 & 1 & 2 & 0 \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix} ,$$
Không có nghiệm đến 'x $=$ b' bởi vì phương trình thứ ba là $0 = 1$. Mặt khác, rút gọn hệ
$$(A', b') = \begin{pmatrix} 1 & 6 & 0 & 1 & 1 \\ 0 & 0 & 1 & 2 & 3 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$$
Có các nghiệm. Ta có thể chọn các biến $x_{2}, x_{4}$ tương ứng với nonpivot các cột arbitrarily, và thì giải cho $x_{3}$ (bằng cách sử dụng phương trình thứ hai) và $x_{1}$ (bằng cách sử dụng phương trình thứ nhất). ở trên lập luận chứng minh sau đây định lý:

> **Định lý 8.16.** Cho trước bất kỳ hệ Ax $= b$ ở đâu $A$ là một ma trận cỡ $m \times  n$, nếu ma trận mở rộng (augmented matrix) $(A, b)$ là rút gọn hàng bậc thang ma trận, thì hệ Ax $= b$ có nghiệm khi và chỉ khi không có phần tử trụ (pivot) trong $b$. Trong rằng trường hợp, tùy ý giá trị có thể được assigned đến biến $x_{j}$ nếu cột $j$ thực hiện không chứa phần tử trụ (pivot).

> **Định nghĩa 8.7.** Nonpivot các biến là thường được gọi là tự do các biến. Đặt Mệnh đề 8.14 và Định lý 8.16 cùng nhau ta thu được tiêu chuẩn đến decide liệu hệ Ax $= b$ có nghiệm: Chuyển đổi augmented hệ $(A, b)$ đến hàng rút gọn bậc thang ma trận (', b') và kiểm tra liệu b' có không có phần tử trụ (pivot).

<!-- PAGE 308 -->
Nhận xét: Khi viết bài toán quy hoạch cài đặt hàng reduction, ta có thể dừng khi cột cuối cùng của ma trận $A$ là đạt tới. Trong trường hợp này, test liệu hệ Ax $= b$ là giải được là rằng row-reduced ma trận ' có không có không hàng của chỉ số $i > r$ sao cho $b_{i}'$ ̸ $= 0$ (ở đâu $r$ là số của các phần tử trụ, và b' là row-reduced vế phải). Nếu ta có thuần nhất hệ Ax $= 0$, mà có nghĩa là $b = 0$, của course $x = 0$ là luôn luôn nghiệm, nhưng Định lý 8.16 suy ra rằng nếu hệ Ax $= 0$ có nhiều hơn/thêm các biến hơn các phương trình, thì nó có một số khác không nghiệm (ta gọi nó không tầm thường nghiệm).

> **Mệnh đề 8.17.** Cho trước bất kỳ thuần nhất hệ Ax $= 0$ của $m$ các phương trình trong $n$ các biến,
$$\mathbb{R}^{n}$$
Nếu $m < n$, thì có một khác không vectơ $x \in$ sao cho Ax $= 0$.

*Chứng minh.* Chuyển đổi ma trận $A$ đến rút gọn hàng bậc thang ma trận '. Ta biết rằng Ax $= 0$ khi và chỉ khi 'x $= 0$. Nếu $r$ là số của các phần tử trụ của ', ta phải có $r \le m$, do đó theo Định lý 8.16 ta có thể assign tùy ý các giá trị đến $n$ - $r > 0$ nonpivot các biến và ta thu được không tầm thường các nghiệm. Định lý 8.16 có thể cũng được sử dụng để đặc trưng hóa khi ma trận vuông (square matrix) là khả nghịch. Thứ nhất, lưu ý sau đây đơn giản nhưng quan trọng sự kiện: Nếu square $n \times  n$ ma trận $A$ là hàng rút gọn bậc thang ma trận, thì hoặc $A$ là đồng nhất thức hoặc đáy/dưới hàng của $A$ là không.

> **Mệnh đề 8.18.** Cho $A$ là ma trận vuông (square matrix) có số chiều $n$. Các điều kiện sau đây là tương đương:
() ma trận $A$ có thể được rút gọn đến đồng nhất thức bởi dãy của các phép biến đổi sơ cấp trên hàng.
$(b)$ ma trận $A$ là tích của sơ cấp các ma trận.
$(c)$ ma trận $A$ là khả nghịch.
$(d)$ hệ của thuần nhất các phương trình Ax $= 0$ có chỉ tầm thường nghiệm $x = 0$.

*Chứng minh.* Thứ nhất ta chứng minh rằng () suy ra $(b)$. Nếu () có thể được rút gọn đến đồng nhất thức bởi dãy của hàng các phép toán $E_{1}, \dots  , E_{p}$, điều này có nghĩa là $E_{p} \cdots  E_{1}A =$ I. Vì mỗi $E_{i}$ là khả nghịch, ta thu được
$$A = E_{1}^{-1}\cdots  E_{p}^{-1} ,$$
Ở đâu mỗi $E_{i}^{-1}$ là cũng sơ cấp hàng phép toán, do đó $(b)$ nghiệm đúng. Bây giờ nếu $(b)$ nghiệm đúng, vì các phép biến đổi sơ cấp trên hàng là khả nghịch, $A$ là khả nghịch và $(c)$ nghiệm đúng. Nếu $A$ là khả nghịch, ta đã được quan sát rằng thuần nhất hệ Ax $= 0$ có chỉ tầm thường nghiệm $x = 0$, bởi vì từ Ax $= 0$, ta thu được $A^{-1}Ax = A^{-1}0$; nghĩa là, $x = 0$. Nó vẫn còn để chứng minh rằng $(d)$ suy ra () và cho điều này ta chứng minh contrapositive: nếu () thực hiện không đúng, thì $(d)$ thực hiện không đúng. Bằng cách sử dụng của ta cơ bản nhận xét về rút gọn các ma trận vuông, nếu $A$ thực hiện không rút gọn đến đồng nhất thức, thì $A$ rút gọn đến hàng bậc thang ma trận ' có đáy/dưới hàng là không. Nói ' $= PA$,

<!-- PAGE 309 -->
Ở đâu $P$ là tích của các phép biến đổi sơ cấp trên hàng. Bởi vì đáy/dưới hàng của ' là không, hệ 'x $= 0$ có nhiều nhất $n$ - $1$ không tầm thường các phương trình, và theo Mệnh đề 8.17, hệ này có không tầm thường nghiệm $x$. Nhưng khi đó, Ax $= P^{-1}$ 'x $= 0$ với $x \neq  0$, contradicting sự kiện rằng hệ Ax $= 0$ được giả sử đến có chỉ tầm thường nghiệm. Vì vậy, $(d)$ suy ra () và chứng minh là đầy đủ. Mệnh đề 8.18 cho ta phương pháp cho việc tính toán nghịch đảo của ma trận khả nghịch (invertible matrix) $A$: rút gọn $A$ đến đồng nhất thức bằng cách sử dụng các phép biến đổi sơ cấp trên hàng, thu được
$$E_{p} \cdots  E_{1}A = I.$$
Nhân cả hai các vế/cạnh bởi $A^{-1}$ ta thu được
$$A^{-1}= E_{p} \cdots  E_{1}.$$
Từ thực tế điểm của quan điểm, ta có thể xây dựng lên tích $E_{p} \cdots  E_{1}$ bởi rút gọn đến dạng bậc thang theo hàng (row echelon form) augmented $n \times$ 2n ma trận $(A, I_{n})$ thu được bằng cách cộng $n$ các cột của ma trận đơn vị (identity matrix) đến $A$. Điều này là chỉ một cái khác cách của performing Gauss–Jordan quy trình. Đây là một ví dụ: cho chúng ta tìm nghịch đảo của ma trận
$$A = \begin{pmatrix} 5 & 4 \\ 6 & 5 \end{pmatrix} .$$
Ta tạo thành $2 \times  4$ ma trận khối (block matrix)
$$(A, I) = \begin{pmatrix} 5 & 4 & 1 & 0 \\ 6 & 5 & 0 & 1 \end{pmatrix}$$
Và áp dụng các phép biến đổi sơ cấp trên hàng để rút gọn $A$ đến đồng nhất thức. Ví dụ:
$$(A, I) = \begin{pmatrix} 5 & 4 & 1 & 0 \\ 6 & 5 & 0 & 1 \end{pmatrix} \longrightarrow \begin{pmatrix} 5 & 4 & 1 & 0 \\ 1 & 1 & -1 & 1 \end{pmatrix}$$
Bằng cách trừ hàng $1$ từ hàng $2$,
$$\begin{pmatrix} 5 & 4 & 1 & 0 \\ 1 & 1 & -1 & 1 \end{pmatrix} \longrightarrow \begin{pmatrix} 1 & 0 & 5 & -4 \\ 1 & 1 & -1 & 1 \end{pmatrix}$$
Bằng cách trừ $4 \times$ hàng $2$ từ hàng $1$,
$$\begin{pmatrix} 1 & 0 & 5 & -4 \\ 1 & 1 & -1 & 1 \end{pmatrix} \longrightarrow \begin{pmatrix} 1 & 0 & 5 & -4 \\ 0 & 1 & -6 & 5 \end{pmatrix} = (I, A^{-1}),$$
Bằng cách trừ hàng $1$ từ hàng $2$. Do đó
$$A^{-1}= \begin{pmatrix} 5 & -4 \\ -6 & 5 \end{pmatrix} .$$
Mệnh đề 8.18 có thể cũng được sử dụng đến cho sơ cấp chứng minh của sự kiện rằng nếu ma trận vuông (square matrix) $A$ có nghịch đảo trái (left inverse) $B$ (resp. nghịch đảo phải (right inverse) $B)$, sao cho $BA =$ I (resp. $AB =$ I), thì $A$ là khả nghịch và $A^{-1} = B$. Điều này là thú vị bài tập, thử nó!
