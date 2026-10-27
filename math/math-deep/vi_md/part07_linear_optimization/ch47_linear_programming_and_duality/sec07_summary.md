# Tóm tắt


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
