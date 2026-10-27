# Các bài tập


<!-- PAGE 1854 -->

## 50.15 Các bài tập

Bài toán 50.1. Chứng minh $(3)$ và $(4)$ của Mệnh đề 50.11.
Bài toán 50.2. Giả sử rằng trong Định lý 50.17, $V = \mathbb{R}^{n}, J$ là elliptic và các ràng buộc $\phi_{i}$ là của tạo thành
$$\sum_{j=1}^{n}  c_{ij}v_{j} \le d_{i},$$
Rằng là, afin. Chứng minh rằng Bài toán $(P_{\mu})$ có duy nhất nghiệm mà là liên tục trong $\mu$.
Bài toán 50.3. $(1)$ Chứng minh rằng tập hợp của saddle các điểm của hàm $L: \Omega \times  M \to \mathbb{R}$ là của tạo thành $V_{0} \times  M_{0}$, với một số $V_{0} \subseteq \Omega$ và một số $M_{0} \subseteq M$.
$(2)$ Giả sử rằng $\Omega$ và $M$ là lồi các tập con của một số các không gian vectơ định chuẩn, giả sử rằng với mọi cố định $v \in \Omega$ ánh xạ
$$\mu  \mapsto L(v, \mu )is concave,$$
Và với mọi cố định $\mu  \in M$ ánh xạ
$$v \mapsto L(v, \mu )is convex.$$
Chứng minh rằng $V_{0} \times  M_{0}$ là lồi.
$(3)$ Chứng minh rằng nếu với mọi cố định $\mu  \in M$ ánh xạ
$$v \mapsto L(v, \mu )is strictly convex,$$
Thì $V_{0}$ có hầu hết một phần tử.
Bài toán 50.4. Chứng minh rằng liên hợp của hàm $f$ cho trước bởi f(X) $=$ log $det(X^{-1})$, ở đâu $X$ là $n \times  n$ đối xứng xác định dương (SPD) ma trận, là
$$f^{*} (Y ) = \log \det((-Y )^{-1}) -n,$$
Ở đâu $Y$ là $n \times  n$ đối xứng âm xác định ma trận.
Bài toán 50.5. (Từ Boyd và Vandenberghe $[29]$, Bài toán 5.12) Cho trước một ma trận cỡ $m \times  n$ $A$ và bất kỳ vectơ $b \in \mathbb{R}^{n}$, xét bài toán
$$minimize- \sum_{i=1}^{m}  \log(b_{i} -a_{i}x)$$
$$subject to Ax < b,$$
Ở đâu $a_{i}$ là hàng thứ $i$ của $A$. Điều này được gọi là analytic tâm bài toán. Nó có thể được được hiển thị
$$\mathbb{R}^{n}$$
Rằng bài toán có duy nhất nghiệm khi và chỉ khi mở đa diện ${x \in$ | Ax $< b}$ là khác rỗng và bị chặn.

<!-- PAGE 1855 -->
$(1)$ Chứng minh rằng cần và đủ các điều kiện cho bài toán đến có nghiệm tối ưu (optimal solution) là
$$Ax < b, \sum_{i=1}^{m}  \frac{a_{i}^{\top}}{b_{i} -a_{x}x} = 0.$$
$(2)$ Derive đối ngẫu (dual) bài toán quy hoạch cho ở trên bài toán quy hoạch. Hint. Thứ nhất giới thiệu mới các biến $y_{i}$ và các phương trình $y_{i} = b_{i}$ - $a_{i}x$.
Bài toán 50.6. (Từ Boyd và Vandenberghe $[29]$, Bài toán 5.13) $A$ Boolean bài toán quy hoạch tuyến tính (linear program) là sau đây tối ưu hóa bài toán:
$$minimizec^{\top}x$$
$$subject to Ax \le b$$
$$x_{i} \in {0, 1}, i = 1, \dots  , n,$$
$$\mathbb{R}^{n} \mathbb{R}^{m}\mathbb{R}^{n}$$
Ở đâu $A$ là một ma trận cỡ $m \times  n$, $c \in$ và $b \in$. sự kiện rằng các nghiệm $x \in$ là có ràng buộc đến có các tọa độ $x_{i}$ lấy các giá trị $0$ hoặc $1$ làm cho nó khó bài toán. ở trên bài toán có thể được được phát biểu như bài toán quy hoạch với toàn phương các ràng buộc:
$$minimizec^{\top}x$$
$$subject to Ax \le b$$
$$x_{i}(1 -x_{i}) = 0, i = 1, \dots  , n.$$
$(1)$ Derive Đối ngẫu Lagrange (Lagrangian dual) của ở trên bài toán quy hoạch.
$(2) A$ cách đến xấp xỉ nghiệm của Boolean bài toán quy hoạch tuyến tính (linear program) là đến xét của nó tuyến tính relaxation ở đâu các ràng buộc $x_{i} \in {0, 1}$ được thay thế bởi tuyến tính các ràng buộc $0 \le x_{i} \le 1$:
$$minimizec^{\top}x$$
$$subject to Ax \le b$$
$$0 \le x_{i} \le 1, i = 1, \dots  , n.$$
Tìm đối ngẫu (dual) bài toán quy hoạch tuyến tính (linear program) của ở trên bài toán quy hoạch tuyến tính (linear program). Chỉ ra rằng các cực đại của đối ngẫu (dual) các bài toán quy hoạch trong $(1)$ và $(2)$ là cùng.

<!-- PAGE 1856 -->
