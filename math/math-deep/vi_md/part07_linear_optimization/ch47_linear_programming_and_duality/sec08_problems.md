# Các bài tập


<!-- PAGE 1674 -->
Một cách quan trọng $(x_{1}, x_{2}, x_{3}, x_{4}) = (1/3, 0, 1/3, 2)$ là nghiệm tối ưu (optimal solution) cho của ta ban đầu bài toán quy hoạch tuyến tính (linear program) và cung cấp giá trị tối ưu (optimal value) của $-10/3$. gốc-đối ngẫu (primal-dual) thuật toán cho quy hoạch tuyến tính (linear programming) không’t dường như là favorite phương pháp để giải các bài toán quy hoạch tuyến tính nowadays. Nhưng nó là quan trọng bởi vì của nó cơ bản nguyên lý, để sử dụng bị thu hẹp (đơn giản hơn) bài toán gốc (primal problem) liên quan đến hàm mục tiêu (objective function) với cố định các trọng số, cụ thể là $1$, và bài toán đối ngẫu (dual problem) đến cung cấp feedback đến gốc (primal) bởi improving hàm mục tiêu (objective function) của đối ngẫu (dual), có đã dẫn đến đến toàn bộ lớp của combinatorial các thuật toán (thường xấp xỉ các thuật toán) based trên gốc-đối ngẫu (primal-dual) paradigm. độc giả sẽ thu được taste của điều này loại của thuật toán bởi consulting Papadimitriou và Steiglitz $[139]$, ở đâu nó được giải thích cách mà cổ điển các thuật toán chẳng hạn như Dijkstra’s thuật toán cho ngắn nhất đường đi bài toán, và Ford và Fulkerson’s thuật toán cho max flow có thể được derived từ gốc-đối ngẫu (primal-dual) paradigm.

## 47.7 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ Chặt tách siêu phẳng (hyperplane). $\bullet$ Farkas–Minkowski mệnh đề. $\bullet$ Farkas bổ đề, phiên bản I, Farkas bổ đề, phiên bản II. $\bullet$ Khoảng cách của điểm đến tập con. $\bullet$ Đối ngẫu (dual) bài toán quy hoạch tuyến tính (linear program), gốc (primal) bài toán quy hoạch tuyến tính (linear program). $\bullet$ Đối ngẫu (dual) các biến, gốc (primal) các biến. $\bullet$ Độ bù lỏng (complementary slackness) các điều kiện. $\bullet$ Đối ngẫu (dual) thuật toán đơn hình (simplex algorithm). $\bullet$ Gốc-đối ngẫu (primal-dual) thuật toán. $\bullet$ Bị thu hẹp gốc (primal) bài toán quy hoạch tuyến tính (linear program).

## 47.8 Các bài tập

$$\mathbb{R}^{d}$$
Bài toán 47.1. Cho $(v_{1}, \dots  , v_{n})$ là dãy của $n$ các vectơ trong và cho $V$ là ma trận cỡ $d \times  n$ có cột thứ $j$ là $v_{j}$. Chứng minh equivalence của sau đây hai các phát biểu:
() Không có không tầm thường dương sự phụ thuộc tuyến tính (linear dependence) trong số $v_{j}$, mà có nghĩa là không có khác không vectơ, $y = (y_{1}, \dots  , y_{n}) \in \mathbb{R}^{n}$, với $y_{j} \ge 0$ cho $j = 1, \dots  , n$, sao cho
$$y_{1}v_{1} + \cdots  + y_{n}v_{n} = 0$$
Hoặc tương đương, $V y = 0$.

<!-- PAGE 1675 -->
$(b)$ Tồn tại một vectơ, $c \in \mathbb{R}^{d}$, sao cho $c^{\top}V > 0$, mà có nghĩa là $c^{\top}v_{j} > 0$, cho $j = 1, \dots  , n$.
Bài toán 47.2. Kiểm tra rằng đối ngẫu (dual) trong cực đại hóa tạo thành (D'') của Đối ngẫu (dual) Bài toán quy hoạch (D') (mà là đối ngẫu (dual) của $(P)$ trong cực đại hóa tạo thành),
$$maximize-b^{\top}y^{\top}$$
$$subject to-A^{\top}y^{\top}\le -c^{\top}and y^{\top}\ge 0,$$
Ở đâu $y \in (\mathbb{R}^{m})^{*}$, cho quay lại Gốc (primal) Bài toán quy hoạch $(P)$.
Bài toán 47.3. Trong Tổng quát Bài toán quy hoạch tuyến tính (linear program) $(P)$ với $n$ gốc (primal) các biến $x_{1}, \dots  , x_{n}$ và
$$objective function \sum_{j}  n=1 c_{j}x_{j} (to be maximized), the m constraints are of the form$$
$$\sum_{j=1}^{n}  a_{ij}x_{j} \le b_{i},$$
$$\sum_{j=1}^{n}  a_{ij}x_{j} \ge b_{i},$$
$$\sum_{j=1}^{n}  a_{ij}x_{j} = b_{i},$$
Cho $i = 1, \dots  , m$, và các biến $x_{j}$ thỏa mãn bất đẳng thức của tạo thành
$$x_{j} \ge 0,$$
$$x_{j} \le 0,$$
$$x_{j} \in \mathbb{R},$$
Cho $j = 1, \dots  , n$. Nếu $y_{1}, \dots  , y_{m}$ là đối ngẫu (dual) các biến, chỉ ra rằng đối ngẫu (dual) bài toán quy hoạch của bài toán quy hoạch tuyến tính (linear program) trong tiêu chuẩn tạo thành tương đương đến $(P)$ là tương đương đến bài toán quy hoạch tuyến tính (linear program) có
$$objective function is \sum_{i}  m=1 y_{i}b_{i} (to be minimized) and whose constraints are determined as$$
Suy ra:
$$$$
$$ \sum_{i=1m}^{m}  a_{ij}y_{i} \ge c_{j}$$
$$$$
$$x_{j} \ge 0$$
$$$$
$$$$
$$$$
$$ifx_{j} \le \mathbb{R} 0,then \sum_{i=1m}  a_{ij}y_{i} \le c_{j},$$
$$x_{j} \in $$
$$$$
$$$$
$$$$
$$ \sum_{i=1}  a_{ij}y_{i} = c_{j}$$
$$$$

<!-- PAGE 1676 -->
Và
$$$$
$$ \sum_{j=1}^{n}  a_{ij}x_{j} \le b_{i}$$
$$$$
$$$$
$$y_{i} \ge 0$$
$$$$
$$$$
$$$$
$$if \sum_{j=1}^{n}  a_{ij}x_{j} \ge b_{i},theny_{i} \le 0.$$
$$y_{i} \in \mathbb{R}$$
$$$$
$$$$
$$$$
$$$$
$$$$
$$ \sum_{j=1}^{n}  a_{ij}x_{j} = b_{i}$$
$$$$
Bài toán 47.4. Áp dụng quy trình của Bài toán 47.3 để chỉ ra rằng đối ngẫu (dual) của (tổng quát) bài toán quy hoạch tuyến tính (linear program)
$$maximize3x_{1} + 2x_{2} + 5x_{3}$$
$$subject to$$
$$5x_{1} + 3x_{2} + x_{3} = -8$$
$$4x_{1} + 2x_{2} + 8x_{3} \le 23$$
$$6x_{1} + 7x_{2} + 3x_{3} \ge 1$$
$$x_{1} \le 4, x_{3} \ge 0$$
Là (tổng quát) bài toán quy hoạch tuyến tính (linear program):
$$minimize-8y_{1} + 23y_{2} -y_{3} + 4y_{4}$$
$$subject to$$
$$5y_{1} + 4y_{2} -6y_{3} + y_{4} = 3$$
$$3y_{1} + 2y_{2} -7y_{3} = 2$$
$$y_{1} + 8y_{2} -3y_{3} \ge 5$$
$$y_{2}, y_{3}, y_{4} \ge 0.$$
Bài toán 47.5. $(1)$ Chứng minh rằng đối ngẫu (dual) của (tổng quát) bài toán quy hoạch tuyến tính (linear program)
$$maximizecx$$
$$subject toAx = b and x \in \mathbb{R}^{n}$$
Là
$$minimizeyb$$
$$subject toyA = c and y \in \mathbb{R}^{m}.$$
$(2)$ Chứng minh rằng đối ngẫu (dual) của (tổng quát) bài toán quy hoạch tuyến tính (linear program)
$$maximizecx$$
$$subject toAx \ge b and x \ge 0$$

<!-- PAGE 1677 -->
Là
$$minimizeyb$$
$$subject toyA \ge c and y \le 0.$$
Bài toán 47.6. Sử dụng độ bù lỏng (complementary slackness) các điều kiện đến confirm rằng
$$x_{1} = 2, x_{2} = 4, x_{3} = 0, x_{4} = 0, x_{5} = 7, x_{6} = 0$$
Là nghiệm tối ưu (optimal solution) của sau đây bài toán quy hoạch tuyến tính (linear program) (từ Chavatal $[40]$, Chương $5)$:
$$maximize18x_{1} -7x_{2} + 12x_{3} + 5x_{4} + 8x_{6}$$
$$subject to$$
$$2x_{1} -6x_{2} + 2x_{3} + 7x_{4} + 3x_{5} + 8x_{6} \le 1$$
$$-3x_{1} -x_{2} + 4x_{3} -3x_{4} + x_{5} + 2x_{6} \le -2$$
$$8x_{1} -3x_{2} + 5x_{3} -2x_{4} + 2x_{6} \le 4$$
$$4x_{1} + 8x_{3} + 7x_{4} -x_{5} + 3x_{6} \le 1$$
$$5x_{1} + 2x_{2} -3x_{3} + 6x_{4} -2x_{5} -x_{6} \le 5$$
$$x_{1}, x_{2}, x_{3}, x_{4}, x_{5}, x_{6} \ge 0.$$
Bài toán 47.7. Kiểm tra carefully rằng đối ngẫu (dual) đơn hình (simplex) phương pháp là tương đương đến đơn hình (simplex) phương pháp ứng dụng đến đối ngẫu (dual) bài toán quy hoạch trong cực đại hóa tạo thành.

<!-- PAGE 1678 -->
