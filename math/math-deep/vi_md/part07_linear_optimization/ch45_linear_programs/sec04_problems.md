# Các bài tập


<!-- PAGE 1601 -->
Mọi ràng buộc $a_{i}x \ge b_{i}$ được thay thế bởi ràng buộc $-a_{i}x \le -b_{i}$. Mọi đẳng thức ràng buộc $a_{i}x = b_{i}$ được thay thế bởi hai các ràng buộc $a_{i}x \le b_{i}$ và $-a_{i}x \le -b_{i}$. Nếu có $n$ các biến $x_{i}$, ta create $n$ mới các biến $y_{i}$ và $n$ mới các biến $z_{i}$ và thay thế mọi biến $x_{i}$ bởi $y_{i} -z_{i}$. Ta cũng cộng 2n các ràng buộc $y_{i} \ge 0$ và $z_{i} \ge 0$. Nếu các ràng buộc được cho bởi các bất đẳng thức Ax $\le b$, ta bây giờ có các ràng buộc cho trước bởi
$$\begin{pmatrix} A & -A \end{pmatrix} \begin{pmatrix} y \\ z \end{pmatrix} \le b,y \ge 0, z \ge 0.$$
Ta thay thế hàm mục tiêu (objective function) cx bởi cy - cz.
Nhận xét: Ta cũng đã chỉ ra rằng ta có thể thay thế bất đẳng thức các ràng buộc Ax $\le b$ bởi đẳng thức các ràng buộc Ax $= b$, bằng cách cộng bù/lỏng các biến có ràng buộc là không âm.

## 45.3 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ Bài toán quy hoạch tuyến tính (linear program). $\bullet$ Hàm mục tiêu (objective function), các ràng buộc. $\bullet$ Nghiệm chấp nhận được (feasible solution). $\bullet$ Bị chặn và không bị chặn các bài toán quy hoạch tuyến tính. $\bullet$ Nghiệm tối ưu (optimal solution), tối ưu. $\bullet$ Bù/lỏng các biến, bài toán quy hoạch tuyến tính (linear program) trong tiêu chuẩn tạo thành. $\bullet$ Cơ bản nghiệm chấp nhận được (feasible solution). $\bullet$ Cơ sở (basis) của biến. $\bullet$ Cơ bản, nonbasic chỉ số, cơ bản, nonbasic biến. $\bullet$ Đỉnh, mặt, cạnh, facet.

## 45.4 Các bài tập

Bài toán 45.1. Chuyển đổi sau đây bài toán quy hoạch đến tiêu chuẩn tạo thành:
$$maximizex_{1} + x_{2}$$
$$subject to$$
$$x_{2} -x_{1} \le 1$$
$$x_{1} + 6x_{2} \le 15$$
$$-4x_{1} + x_{2} \ge 10.$$

<!-- PAGE 1602 -->
Bài toán 45.2. Chuyển đổi sau đây bài toán quy hoạch đến tiêu chuẩn tạo thành:
$$maximize3x_{1} -2x_{2}$$
$$subject to$$
$$2x_{1} -x_{2} \le 4$$
$$x_{1} + 3x_{2} \ge 5$$
$$x_{2} \ge 0.$$
Bài toán 45.3. khái niệm của cơ bản nghiệm chấp nhận được (feasible solution) cho các bài toán quy hoạch tuyến tính ở đâu các ràng buộc là của tạo thành Ax $\le b, x \ge 0$ được định nghĩa như sau. cơ bản nghiệm chấp nhận được (feasible solution) của (tổng quát) bài toán quy hoạch tuyến tính (linear program) với $n$ các biến là nghiệm chấp nhận được (feasible solution) cho mà một số $n$ độc lập tuyến tính (linearly independent) các ràng buộc đúng với đẳng thức. Chứng minh rằng định nghĩa của cơ bản nghiệm chấp nhận được (feasible solution) cho các bài toán quy hoạch tuyến tính trong tiêu chuẩn tạo thành là đặc biệt trường hợp của ở trên định nghĩa.
Bài toán 45.4. Xét bài toán quy hoạch tuyến tính (linear program)
$$maximizex_{1} + x_{2}$$
$$subject to$$
$$x_{1} + x_{2} \le 1.$$
Chỉ ra rằng không có cái nào của tối ưu các nghiệm là cơ bản.
$$\mathbb{R}^{n+1}$$
Bài toán 45.5. tiêu chuẩn n-simplex là tập con $\Delta^{n}$ của cho trước bởi
$$\mathbb{R}^{n+1}$$
$$\Delta^{n} = {(x_{1}, \dots  , x_{n+1}) \in | x_{1} + \cdots  + x_{n+1} = 1, x_{i} \ge 0, 1 \le i \le n + 1}.$$
$(1)$ Chứng minh rằng $\Delta^{n}$ là lồi và rằng nó là bao lồi (convex hull) của $n+1$ các vectơ $e_{1}, \dots  e_{n+1}$, ở đâu $e_{i}$ là thứ $i$ chính tắc unit cơ sở (basis) vectơ, $i = 1, \dots  , n + 1$.
$(2)$ Chứng minh rằng $\Delta^{n}$ là giao của $n + 1$ một nửa các không gian và xác định các siêu phẳng định nghĩa các phần tử này các nửa không gian.
Nhận xét: thể tích dưới tiêu chuẩn đơn hình (simplex) $\Delta^{n}$ là $1/(n + 1)$!.
$$\mathbb{R}^{n}$$
Bài toán 45.6. $n$ chiều cross-polytope là tập con $XP_{n}$ của cho trước bởi
$$\mathbb{R}^{n}$$
$$XP_{n} = {(x_{1}, \dots  , x_{n}) \in | |x_{1}| + \cdots  + |x_{n}| \le 1}.$$
$(1)$ Chứng minh rằng $XP_{n}$ là lồi và rằng nó là bao lồi (convex hull) của 2n các vectơ $\pm e_{i}$, ở đâu $e_{i}$ là thứ $i$ chính tắc unit cơ sở (basis) vectơ, $i = 1, \dots  , n$.
$(2)$ Chứng minh rằng $XP_{n}$ là giao của $2^{n}$ một nửa các không gian và xác định các siêu phẳng định nghĩa các phần tử này các nửa không gian.
Nhận xét: thể tích của $XP_{n}$ là $2^{n}/n$!.

<!-- PAGE 1603 -->
$$\mathbb{R}^{n}$$
Bài toán 45.7. $n$ chiều hypercube là tập con $C_{n}$ của cho trước bởi
$$\mathbb{R}^{n}$$
$$C_{n} = {(x_{1}, \dots  , x_{n}) \in | |x_{i}| \le 1, 1 \le i \le n}.$$
$(1)$ Chứng minh rằng $C_{n}$ là lồi và rằng nó là bao lồi (convex hull) của $2^{n}$ các vectơ $(\pm 1, \dots  , \pm 1), i = 1, \dots  , n$.
$(2)$ Chứng minh rằng $C_{n}$ là giao của 2n một nửa các không gian và xác định các siêu phẳng định nghĩa các phần tử này các nửa không gian.
Nhận xét: thể tích của $C_{n}$ là $2^{n}$.

<!-- PAGE 1604 -->
