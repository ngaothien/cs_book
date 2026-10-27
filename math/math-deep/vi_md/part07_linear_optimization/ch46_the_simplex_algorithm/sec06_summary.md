# Tóm tắt


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
