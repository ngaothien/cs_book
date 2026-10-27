# Các bài tập


<!-- PAGE 1635 -->
Understanding complexity của tuyến tính bài toán quy hoạch, đặc biệt của thuật toán đơn hình (simplex algorithm), là vẫn ongoing. interested độc giả là referred đến Matousek và Gardner $[127]$ (Chương $5$, Mục 5.9) với một số pointers. Trong mục tiếp theo ta xét quan trọng lý thuyết các tiêu chuẩn cho xác định liệu tập hợp của các ràng buộc Ax $\le b$ và $x \ge 0$ có nghiệm hoặc không.

## 46.6 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ Suy biến và không suy biến cơ bản nghiệm chấp nhận được (feasible solution). $\bullet$ Chọn phần tử trụ bước. $\bullet$ Phần tử trụ (pivot) quy tắc. $\bullet$ Cycling. $\bullet$ Bland’s quy tắc, Dantzig’s quy tắc, steepest cạnh quy tắc, ngẫu nhiên cạnh quy tắc, lớn nhất tăng quy tắc, lexicographic quy tắc. $\bullet$ Phase I và Phase II của thuật toán đơn hình (simplex algorithm). $\bullet$ eta ma trận, eta nhân tử hóa. $\bullet$ Revised đơn hình (simplex) phương pháp. $\bullet$ Rút gọn chi phí. $\bullet$ Đầy đủ các bảng (tableaux). $\bullet$ Hirsch giả thuyết.

## 46.7 Các bài tập

Bài toán 46.1. Trong Mục 46.2 chứng minh rằng nếu Trường hợp $(A)$ phát sinh, thì cơ bản nghiệm chấp nhận được (feasible solution) $u$ là nghiệm tối ưu (optimal solution). Chứng minh rằng nếu Trường hợp (B1) phát sinh, thì bài toán quy hoạch tuyến tính (linear program) là không bị chặn. Chứng minh rằng nếu Trường hợp (B3) phát sinh, thì $(u^{+}, K^{+})$ là cơ bản nghiệm chấp nhận được (feasible solution).
Bài toán 46.2. Trong Mục 46.2 chứng minh rằng sau đây equivalences đúng:
$$Case (A) \Leftarrow \Rightarrow B = \emptyset ,Case (B) \Leftarrow \Rightarrow B \neq  \emptyset$$
$$Case (B1) \Leftarrow \Rightarrow B_{1} \neq  \emptyset$$
$$Case (B2) \Leftarrow \Rightarrow B_{2} \neq  \emptyset$$
$$Case (B3) \Leftarrow \Rightarrow B_{3} \neq  \emptyset .$$

<!-- PAGE 1636 -->
Hơn nữa, chứng minh rằng Các trường hợp $(A)$ và $(B)$, Các trường hợp (B1) và (B3), và Các trường hợp (B2) và (B3) là mutually exclusive, trong khi Các trường hợp (B1) và (B2) là không.
Bài toán 46.3. Xét bài toán quy hoạch tuyến tính (linear program) (do E.M.L. Beale):
$$maximize(3/4)x_{1} -150x_{2} + (1/50)x_{3} -6x_{4}$$
$$subject to$$
$$(1/4)x_{1} -60x_{2} -(1/25)x_{3} + 9x_{4} \le 0$$
$$(1/4)x_{1} -90x_{2} -(1/50)x_{3} + 3x_{4} \le 0$$
$$x_{3} \le 1$$
$$x_{1} \ge 0, x_{2} \ge 0, x_{3} \ge 0, x_{4} \ge 0.$$
$(1)$ Chuyển đổi ở trên bài toán quy hoạch đến tiêu chuẩn tạo thành.
$(2)$ Chỉ ra rằng nếu ta áp dụng thuật toán đơn hình (simplex algorithm) với phần tử trụ (pivot) quy tắc mà các chọn cột entering cơ sở (basis) như cột của nhỏ nhất chỉ số, thì phương pháp các chu trình.
Bài toán 46.4. Read carefully chứng minh cho trước bởi Chvatal rằng lexicographic phần tử trụ (pivot) quy tắc và Bland’s phần tử trụ (pivot) quy tắc ngăn cản cycling; xem Chvatal $[40]$ (Chương $3$, các trang 34-38).
Bài toán 46.5. Giải sau đây bài toán quy hoạch tuyến tính (linear program) (từ Chvatal $[40]$, Chương $3$, trang $44)$ bằng cách sử dụng two-phase thuật toán đơn hình (simplex algorithm):
$$maximize3x_{1} + x_{2}$$
$$subject to$$
$$x_{1} -x_{2} \le -1$$
$$-x_{1} -x_{2} \le -3$$
$$2x_{1} + x_{2} \le 4$$
$$x_{1} \ge 0, x_{2} \ge 0.$$
Bài toán 46.6. Giải sau đây bài toán quy hoạch tuyến tính (linear program) (từ Chvatal $[40]$, Chương $3$, trang $44)$ bằng cách sử dụng two-phase thuật toán đơn hình (simplex algorithm):
$$maximize3x_{1} + x_{2}$$
$$subject to$$
$$x_{1} -x_{2} \le -1$$
$$-x_{1} -x_{2} \le -3$$
$$2x_{1} + x_{2} \le 2$$
$$x_{1} \ge 0, x_{2} \ge 0.$$

<!-- PAGE 1637 -->
Bài toán 46.7. Giải sau đây bài toán quy hoạch tuyến tính (linear program) (từ Chvatal $[40]$, Chương $3$, trang $44)$ bằng cách sử dụng two-phase thuật toán đơn hình (simplex algorithm):
$$maximize3x_{1} + x_{2}$$
$$subject to$$
$$x_{1} -x_{2} \le -1$$
$$-x_{1} -x_{2} \le -3$$
$$2x_{1} -x_{2} \le 2$$
$$x_{1} \ge 0, x_{2} \ge 0.$$
Bài toán 46.8. Chỉ ra rằng sau đây bài toán quy hoạch tuyến tính (linear program) (từ Chvatal $[40]$, Chương $3$, trang $43)$ là không bị chặn.
$$maximizex_{1} + 3x_{2} -x_{3}$$
$$subject to$$
$$2x_{1} + 2x_{2} -x_{3} \le 10$$
$$3x_{1} -2x_{2} + x_{3} \le 10$$
$$x_{1} -3x_{2} + x_{3} \le 10$$
$$x_{1} \ge 0, x_{2} \ge 0, x_{3} \ge 0.$$
Hint. Thử $x_{1} = 0, x_{3} = t$, và phù hợp giá trị cho $x_{2}$.

<!-- PAGE 1638 -->
