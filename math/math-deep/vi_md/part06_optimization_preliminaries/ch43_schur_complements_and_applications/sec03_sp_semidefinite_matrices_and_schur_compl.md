# SP Nửa xác định Các ma trận và Các phần bù Schur


<!-- PAGE 1569 -->
Một cái khác phiên bản của Mệnh đề 43.3 bằng cách sử dụng Phần bù Schur (Schur complement) của $A$ thay vì của Phần bù Schur (Schur complement) của $C$ cũng nghiệm đúng. chứng minh sử dụng nhân tử hóa của $M$ bằng cách sử dụng Phần bù Schur (Schur complement) của $A$ (xem Mục 43.1).

> **Mệnh đề 43.4.** Với mọi ma trận đối xứng (symmetric matrix) $M$ của tạo thành
$$M = \begin{pmatrix} A & B \\ B^{\top} & C \end{pmatrix} ,$$
Nếu $A$ là khả nghịch thì các tính chất sau đây đúng:
$(1) M$ ≻ $0$ khi và chỉ khi $A$ ≻ $0$ và $C$ - $B^{\top}A^{-1}B$ ≻ $0$.
$(2)$ Nếu $A$ ≻ $0$, thì $M$ ⪰ $0$ khi và chỉ khi $C$ - $B^{\top}A^{-1}B$ ⪰ $0$. Ở đây là illustration của Mệnh đề 43.4(2). Xét phi tuyến toàn phương ràng buộc
$$(Ax + b)^{\top}(Ax + b) \le c^{\top}x + d,$$
$$\mathbb{R}\mathbb{R}^{n} \mathbb{R}$$
Đã là $A \in M_{n}($), $x, b, c \in$ và $d \in$. Vì hiển nhiên $I = I_{n}$ là khả nghịch và I ≻ $0$, ta có
$$\begin{pmatrix} I & Ax + b \\ (Ax + b)^{\top} & c^{\top}x + d \end{pmatrix} ⪰0$$
Khi và chỉ khi $c^{\top}x + d$ - (Ax $+ b)^{\top}(Ax + b)$ ⪰ $0$ khi và chỉ khi(Ax $+ b)^{\top}(Ax + b) \le c^{\top}x + d$, vì ma trận (vô hướng (scalar)) $c^{\top}x + d$ - (Ax $+ b)^{\top}(Ax + b)$ là Phần bù Schur (Schur complement) của I trong ở trên ma trận. mẹo/kỹ thuật của bằng cách sử dụng Các phần bù Schur đến chuyển đổi phi tuyến bất đẳng thức các ràng buộc vào tuyến tính các ràng buộc trên các ma trận đối xứng liên quan đến nửa xác định thứ tự ⪰ được sử dụng extensively đến chuyển đổi phi tuyến các bài tập vào nửa xác định các bài toán quy hoạch; xem Boyd và Vandenberghe $[29]$. Khi $C$ là suy biến (hoặc $A$ là suy biến), nó là vẫn khả dĩ/có thể để đặc trưng hóa khi ma trận đối xứng (symmetric matrix) $M$ như ở trên là nửa xác định dương (positive semidefinite), nhưng điều này đòi hỏi bằng cách sử dụng phiên bản của Phần bù Schur (Schur complement) liên quan đến nghịch đảo giả (pseudo-inverse) của $C$, cụ thể là $A$ - $BC^{+}B^{\top}$ (hoặc Phần bù Schur (Schur complement), $C$ - $B^{\top}A^{+}B$, của $A)$. Ta sử dụng tiêu chuẩn của Mệnh đề 42.5, mà cho ta biết chúng ta khi toàn phương hàm của $form_{2}^{1} x^{\top}Px$ - $x^{\top}b$ có cực tiểu và những gì điều này tối ưu giá trị là (ở đâu $P$ là ma trận đối xứng (symmetric matrix)).

## 43.3 Đối xứng Nửa xác định dương (positive semidefinite) Các ma trận và

$$Schur Complements$$
Ta bây giờ trả về đến của ta ban đầu bài toán, đặc trưng hóa khi ma trận đối xứng (symmetric matrix)
$$M = \begin{pmatrix} A & B \\ B^{\top} & C \end{pmatrix}$$

<!-- PAGE 1570 -->
Là nửa xác định dương (positive semidefinite). Do đó, ta muốn đến biết khi hàm
$$f(x, y) = (x^{\top}y^{\top}) \begin{pmatrix} A & B \\ B^{\top} & C \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = x^{\top}Ax + 2x^{\top}By + y^{\top}Cy$$
Có cực tiểu đối với cả hai $x$ và $y$. Nếu ta đúng $y$ hằng số, Mệnh đề 42.5 suy ra rằng f(x, $y)$ có cực tiểu khi và chỉ khi $A$ ⪰ $0$ và (I - $AA^{+})By = 0$, và thì cực tiểu giá trị là
$$f(x^{*}, y) = -y^{\top}B^{\top}A^{+}By + y^{\top}Cy = y^{\top}(C -B^{\top}A^{+}B)y.$$
Vì ta muốn f(x, $y)$ là uniformly bị chặn từ ở dưới với mọi $x, y$, ta phải có (I - $AA^{+})B = 0$. Bây giờ $f(x^{*}, y)$ có cực tiểu khi và chỉ khi $C$ - $B^{\top}A^{+}B$ ⪰ $0$. Vì vậy, ta có được thiết lập rằng f(x, $y)$ có cực tiểu trên tất cả $x, y$ khi và chỉ khi
$$A ⪰0,(I -AA^{+})B = 0,C -B^{\top}A^{+}B ⪰0.$$
Đồng dạng lập luận áp dụng nếu ta thứ nhất cực tiểu hóa đối với $y$ và thì đối với $x$, nhưng điều này time, Phần bù Schur (Schur complement) $A$ - $BC^{+}B^{\top}$ của $C$ là liên quan. Đặt tất cả các phần tử này các sự kiện cùng nhau, ta thu được của ta chính kết quả:

> **Định lý 43.5.** Cho trước bất kỳ ma trận đối xứng (symmetric matrix)
$$M = \begin{pmatrix} A & B \\ B^{\top} & C \end{pmatrix}$$
Các điều kiện sau đây là tương đương:
$(1) M$ ⪰ $0 (M$ là nửa xác định dương (positive semidefinite)).
$(2) A$ ⪰ $0$, (I - $AA^{+})B = 0, C$ - $B^{\top}A^{+}B$ ⪰ $0$.
$(3) C$ ⪰ $0$, (I - $CC^{+})B^{\top} = 0, A$ - $BC^{+}B^{\top}$ ⪰ $0$. Nếu $M$ ⪰ $0$ như trong Định lý 43.5, thì nó là dễ để kiểm tra rằng ta có kết quả sau các nhân tử hóa (bằng cách sử dụng sự kiện rằng $A^{+}AA^{+} = A^{+}$ và $C^{+}CC^{+} = C^{+})$:
$$\begin{pmatrix} A & B \\ B^{\top} & C \end{pmatrix} = \begin{pmatrix} I & BC^{+} \\ 0 & I \end{pmatrix} \begin{pmatrix} A -BC^{+}B^{\top} & 0 \\ 0 & C \end{pmatrix} \begin{pmatrix} I & 0 \\ C^{+}B^{\top} & I \end{pmatrix}$$
Và
$$\begin{pmatrix} A & B \\ B^{\top} & C \end{pmatrix} = \begin{pmatrix} I & 0 \\ B^{\top}A^{+} & I \end{pmatrix} \begin{pmatrix} A & 0 \\ 0 & C -B^{\top}A^{+}B \end{pmatrix} \begin{pmatrix} I & A^{+}B \\ 0 & I \end{pmatrix} .$$
