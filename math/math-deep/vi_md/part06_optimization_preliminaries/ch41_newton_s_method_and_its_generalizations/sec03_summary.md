# Tóm tắt


<!-- PAGE 1534 -->
$$\mathbb{R}^{n}$$
Ở đâu $\nabla J(x_{k})$ là gradien của $J$ tại $x_{k}$ (ở đây, ta đồng nhất E' với). Đặc biệt, Newton’s ban đầu phương pháp chọn $A_{k} =$ J'', và vòng lặp bước là của tạo thành
$$x_{k+1} = x_{k} -(\nabla^{2} J(x_{k}))^{-1}\nabla J(x_{k}),k \ge 0,$$
Ở đâu $\nabla^{2} J(x_{k})$ là Hessian của $J$ tại $x_{k}$.

> **Ví dụ 41.3.** Cho chúng ta áp dụng Newton’s ban đầu phương pháp đến hàm $J$ cho trước bởi J(x) $= 1$ - - $x^{3}$ 4x. Ta có J'(x) $= x^{2} 4$ và J''(x) $=$ 2x, do đó Newton bước được cho bởi $\overline{3}$
$$-$$
$$x_{k+1} = x_{k} - \frac{x_{k}^{2}4}{2x_{k}} = \frac{1}{2} \begin{pmatrix} 4 \\ x_{k} + \\ x_{k} \end{pmatrix} .$$
Điều này là dãy của Ví dụ 41.1 để tính square nghiệm (root) của $4$. Bắt đầu với bất kỳ $x_{0} > 0$ nó hội tụ rất quickly đến $2$. Như được nhận xét trong Ciarlet $[41]$ (Mục 7.5), suy rộng/tổng quát hóa Newton các phương pháp có rất wide miền giá trị (range) của applicability. Ví dụ, khác nhau các phiên bản của hạ gradien (gradient descent) các phương pháp có thể được được quan điểm như instances của Newton phương pháp. Xem Mục 49.9 cho ví dụ. Newton’s phương pháp cũng đóng quan trọng vai trò trong lồi tối ưu hóa, đặc biệt, interior-point các phương pháp. biến thể của Newton’s phương pháp dealing với đẳng thức các ràng buộc có đã được developed. Ta refer độc giả đến Boyd và Vandenberghe $[29]$, Các chương $10$ và $11$, cho toàn diện trình bày của các phần tử này topics.

## 41.3 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ Newton’s phương pháp cho các hàm $f$: $\mathbb{R} \to \mathbb{R}. \bullet$ Suy rộng/tổng quát hóa Newton các phương pháp. $\bullet$ Newton-Kantorovich định lý.

## 41.4 Các bài tập

Bài toán 41.1. Nếu $\alpha  > 0$ và f(x) $= x^{2}$ - $\alpha$, Newton’s phương pháp cho ta dãy
$$x_{k+1} = \frac{1}{2} \begin{pmatrix} \alpha \\ x_{k} + \\ x_{k} \end{pmatrix}$$
$$\sqrt$$
Để tính square nghiệm (root) $\overline{\alpha}$ của $\alpha$.
