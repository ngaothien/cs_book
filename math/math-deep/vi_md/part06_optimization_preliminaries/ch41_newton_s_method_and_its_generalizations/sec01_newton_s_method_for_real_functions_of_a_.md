# Phương pháp Newton (Newton's method) cho Thực Các hàm của Thực Lập luận


<!-- PAGE 1523 -->
Chương $41$ Newton’s Phương pháp và Của nó Các tổng quát hóa Trong Chương $40$ ta investigated bài toán của xác định khi hàm $J$: $\Omega \to \mathbb{R}$ được định nghĩa trên một số mở tập con $\Omega$ của không gian vectơ định chuẩn (normed vector space) $E$ có cực trị địa phương (local extremum). Mệnh đề 40.1 cho cần điều kiện khi $J$ là khả vi (differentiable): nếu $J$ có cực trị địa phương (local extremum) tại $u \in \Omega$, thì ta phải có
$$J'(u) = 0.$$
Do đó ta là đã dẫn đến đến bài toán của việc tìm các không điểm của đạo hàm
$$J': \Omega \to E',$$
$$\mathbb{R} \mathbb{R}$$
Ở đâu E' $= \mathcal{L}(E$;) là tập hợp của tuyến tính liên tục các hàm từ $E$ đến; rằng là, đối ngẫu (dual) của $E$, như đã định nghĩa trong nhận xét sau Mệnh đề 40.8. Điều này dẫn đến chúng ta đến xét bài toán trong nhiều hơn/thêm tổng quát tạo thành, cụ thể là, cho trước hàm $f$: $\Omega \to Y$ từ mở tập con $\Omega$ của không gian vectơ định chuẩn (normed vector space) $X$ đến không gian vectơ định chuẩn (normed vector space) $Y$, tìm
$(i)$ Đủ các điều kiện mà đảm bảo sự tồn tại của không của hàm $f$; nghĩa là, phần tử $a \in \Omega$ sao cho f() $= 0$.
(ii) thuật toán cho approximating như vậy, nghĩa là, dãy $(x_{k})$ của các điểm của $\Omega$ có giới hạn là. Trong chương này ta thảo luận Newton’s phương pháp và một số của nó các tổng quát hóa đến cho (riêng) các câu trả lời đến Các bài tập $(i)$ và (ii).

## 41.1 Newton’s Phương pháp cho Thực Các hàm của Thực

$$Argument$$
Khi $X = Y =\mathbb{R}$, ta có thể sử dụng Newton’s phương pháp để tìm không của hàm $f$: $\Omega \to \mathbb{R}$. Ta chọn một số ban đầu phần tử $x_{0} \in \mathbb{R}$ “close đủ” đến không của $f$, và ta định nghĩa dãy
$$1523$$

<!-- PAGE 1524 -->
$(x_{k})$ bởi
$$x_{k+1} = x_{k} - \frac{f(x_{k})}{f'(x_{k})} ,$$
Với mọi $k \ge 0$, miễn là/được cung cấp rằng f' $(x_{k}) \neq  0$. ý tưởng là để định nghĩa $x_{k+1}$ như giao của trục $x$ với tiếp tuyến đường thẳng đến đồ thị của hàm $x \mapsto$ f(x) tại điểm $(x_{k}, f(x_{k}))$. Thật vậy, phương trình của điều này tiếp tuyến đường thẳng là
$$y -f(x_{k}) = f' (x_{k})(x -x_{k}),$$
Và của nó giao với trục $x$ là thu được cho $y = 0$, mà cho ta
$$x = x_{k} - \frac{f(x_{k})}{f'(x_{k})} ,$$
Như đã khẳng định. Xem Hình 41.1.
$$(x,f(       )x)$$
$$kk$$
$$(xk+1,f(        )x)$$
$$k+1$$
$$\overline{x}\overline{x}\overline{k+1}\overline{x}$$
$$k+2k$$
$$Figure 41.1: The construction of two stages in Newton’s method.$$

> **Ví dụ 41.1.** Nếu $\alpha  > 0$ và f(x) $= x^{2}$ - $\alpha$, Newton’s phương pháp cho ta dãy
$$x_{k+1} = \frac{1}{2} \begin{pmatrix} \alpha \\ x_{k} + \\ x_{k} \end{pmatrix}$$
$$\sqrt \sqrt$$
Để tính square nghiệm (root) $\overline{\alpha}$ của $\alpha$. Nó có thể được được hiển thị rằng phương pháp hội tụ đến $\overline{\alpha}$ với mọi $x_{0} > 0$; xem Bài toán 41.1. Thực sự, phương pháp cũng hội tụ khi $x_{0} < 0$! Tìm ra những gì là giới hạn.
