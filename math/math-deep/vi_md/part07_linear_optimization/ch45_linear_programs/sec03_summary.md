# Tóm tắt


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
