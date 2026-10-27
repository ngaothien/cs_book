# Phương pháp Newton (Newton's method) Cho Việc tìm Cực tiểu


<!-- PAGE 1737 -->
Phương pháp được xác định bởi lớn nhất và nhỏ nhất các trị riêng (eigenvalues) của $A$. Strang các thảo luận điều này vấn đề trong trường hợp của một ma trận cỡ $2 \times  2$. Sự hội tụ là một cách đáng kể accelerated. Một cái khác phương pháp là đã biết như Nesterov acceleration. Trong phương pháp này,
$$u_{k+1} = u_{k} + \beta (u_{k} -u_{k-1}) -\rho \nabla J_{uk+\gamma(uk-uk-1)},$$
Ở đâu $\beta , \rho , \gamma$ là các tham số. Cho chi tiết, xem Strang $[177]$ (Chương VI, Mục $4)$. Lax cũng các thảo luận khác các phương pháp trong mà bước $\rho_{k}$ được chọn bằng cách sử dụng các nghiệm của Chebyshev các đa thức; xem Lax $[117]$, Chương $17$, Các mục 2–4. biến thể của Newton’s phương pháp được mô tả trong Mục 41.2 có thể được được sử dụng để tìm cực tiểu của hàm thuộc đến nhất định lớp của chặt các hàm lồi. phương pháp này là đặc biệt trường hợp của trường hợp ở đâu chuẩn (norm) được cảm sinh bởi đối xứng xác định dương (SPD) ma trận $P$, cụ thể là $P = \nabla^{2}$ J(x), Hessian của $J$ tại $x$.

## 49.9 Newton’s Phương pháp Cho Việc tìm Cực tiểu

$$\mathbb{R} \mathbb{R}^{n}$$
Nếu $J$: $\Omega \to$ là hàm lồi (convex function) được định nghĩa trên một số mở tập con $\Omega$ của mà là hai lần khả vi (differentiable) và nếu của nó Hessian $\nabla^{2}$ J(x) là đối xứng xác định dương (SPD) với mọi $x \in \Omega$, thì theo Mệnh đề 40.12(2), hàm $J$ là lồi chặt (strictly convex). Trong trường hợp này, với mọi $x \in \Omega$, ta có toàn phương chuẩn (norm) được cảm sinh bởi $P = \nabla^{2}$ J(x) như đã định nghĩa trong mục trước, cho trước bởi
$$\|u\|_{\nabla2J(x)} = (u^{\top}\nabla^{2} J(x) u)^{1/2}.$$
Hạ nhanh nhất (steepest descent) hướng cho điều này toàn phương chuẩn (norm) được cho bởi
$$d_{nt} = -(\nabla^{2} J(x))^{-1}\nabla J_{x}.$$
Chuẩn (norm) của $d_{nt}$ cho toàn phương chuẩn (norm) được định nghĩa bởi $\nabla^{2}$ J(x) được cho bởi
$$(d_{nt}^{\top}\nabla^{2} J(x) d_{nt})^{1/2}= \begin{pmatrix} -(\nabla J_{x})^{\top}(\nabla^{2} J(x))^{-1}\nabla^{2} J(x)(-(\nabla^{2} J(x))^{-1}\nabla J_{x} \\ ( & J_{x})^{\top}( & J(x))^{-1} & J_{x}^{1/2} . \end{pmatrix} )^{1/2}$$
$$= \begin{pmatrix} \nabla & \nabla^{2} & \nabla \\ \mathbb{R} \end{pmatrix}$$

> **Định nghĩa 49.9.** Cho trước hàm $J$: $\Omega \to$ như ở trên, với mọi $x \in \Omega$, Newton bước $d_{nt}$ được định nghĩa bởi
$$d_{nt} = -(\nabla^{2} J(x))^{-1}\nabla J_{x},$$
Và Newton decrement $\lambda (x)$ được định nghĩa bởi
$$.$$
$$\lambda (x) = \begin{pmatrix} (\nabla J_{x})^{\top}(\nabla^{2} J(x))^{-1}\nabla \end{pmatrix} J_{x}^{1/2}$$
Nhận thấy rằng
$$\langle \nabla J_{x}, d_{nt}\rangle = (\nabla J_{x})^{\top}(-(\nabla^{2} J(x))^{-1}\nabla J_{x}) = -\lambda (x)^{2}.$$

<!-- PAGE 1738 -->
Nếu $\nabla J_{x} \neq  0$, ta có $\lambda (x) \neq  0$, do đó $\langle \nabla J_{x}, d_{nt}\rangle < 0$, và $d_{nt}$ là thật vậy descent hướng. số $\langle \nabla J_{x}, d_{nt}\rangle$ là hằng số rằng chỉ ra lên during backtracking đường thẳng search. đẹp đặc trưng (feature) của Newton bước và của Newton decrement là rằng chúng là afin bất biến. Điều này có nghĩa là nếu $T$ là ma trận khả nghịch (invertible matrix) và nếu ta định nghĩa $g$ bởi g(y) $=$ J(Ty), nếu Newton bước liên kết với $J$ được ký hiệu bởi $d_{J,nt}$ và tương tự Newton bước liên kết với $g$ được ký hiệu bởi $d_{g,nt}$, thì nó được hiển thị trong Boyd và Vandenberghe $[29]$ (Mục 9.5.1) rằng
$$d_{g,nt} = T^{-1} d_{J,nt},$$
Và do đó
$$x + d_{J,nt} = T(y + d_{g,nt}).$$
Đồng dạng các tính chất áp dụng đến Newton decrement. Newton’s phương pháp bao gồm của sau đây các bước: Cho trước bắt đầu điểm $u_{0} \in$ dom(J) và tolerance $\epsilon  > 0$ thực hiện: repeat
$(1)$ Tính Newton bước và decrement $d_{nt,k} = -(\nabla^{2} J(u_{k}))^{-1}\nabla J_{uk}$ và $\lambda (u_{k})^{2} = (\nabla J_{uk})^{\top}(\nabla^{2} J(u_{k}))^{-1}\nabla J_{uk}$.
$(2)$ Stopping tiêu chuẩn. quit nếu $\lambda (u_{k})^{2}/2 \le \epsilon$.
$(3)$ Đường thẳng Search. Perform chính xác hoặc backtracking đường thẳng search để tìm $\rho_{k}$.
$(4)$ Update. $u_{k+1} = u_{k} + \rho_{k} d_{nt,k}$. Nhận thấy rằng điều này là về cơ bản descent quy trình của Mục 49.8 bằng cách sử dụng Newton bước như search hướng, ngoại trừ rằng stopping tiêu chuẩn là đã kiểm tra chỉ sau việc tính toán search hướng, thay vì sau update (rất định thức con (minor) difference). sự hội tụ của Newton’s phương pháp là một cách kỹ lưỡng analyzed trong Boyd và Vandenberghe $[29]$ (Mục 9.5.3). Điều này giải tích/phân tích được tạo dưới sau đây các giả định:
$(1)$ hàm $J$: $\Omega \to \mathbb{R}$ là hàm lồi (convex function) được định nghĩa trên một số mở tập con $\Omega$ của $\mathbb{R}^{n}$ mà là hai lần khả vi (differentiable) và của nó Hessian $\nabla^{2}$ J(x) là đối xứng xác định dương (SPD) với mọi $x \in \Omega$. Điều này suy ra rằng có hai các hằng số $m > 0$ và $M > 0$ sao cho mI $⪯\nabla^{2}$ J(x) ⪯ MI với mọi $x \in \Omega$, mà có nghĩa là các trị riêng (eigenvalues) của $\nabla^{2}$ J(x) thuộc đến $[m, M]$.
$(2)$ Hessian là Lipschitzian, mà có nghĩa là tồn tại một $L \ge 0$ sao cho
$$\nabla^{2} J(x) -\nabla^{2} J(y)_{2} \le L \|x, y\|_{2}for all x, y \in \Omega .$$
Hóa ra là các vòng lặp của Newton’s phương pháp fall vào hai phases, tùy thuộc liệu $\|\nabla J_{uk}\|_{2} \ge \eta$ hoặc $\|\nabla J_{uk}\|_{2} < \eta$, ở đâu $\eta$ là số mà phụ thuộc vào $m, L$, và hằng số $\alpha$ được sử dụng trong backtracking đường thẳng search, và $\eta  \le m^{2}/L$.

<!-- PAGE 1739 -->
$(1)$ thứ nhất phase, được gọi là damped Newton phase, xảy ra trong khi $\|\nabla J_{uk}\|_{2} \ge \eta$. During điều này phase, quy trình có thể chọn bước kích thước $\rho_{k}  = t < 1$, và tồn tại một hằng số $\gamma  > 0$ sao cho
$$J(u_{k+1}) -J(u_{k}) \le -\gamma .$$
$(2)$ thứ hai phase, được gọi là quadratically convergent phase hoặc thuần túy Newton phase, xảy ra trong khi $\|\nabla J_{uk}\|_{2} < \eta$. During điều này phase, bước kích thước $\rho_{k}  = t = 1$ là luôn luôn được chọn, và ta có
$$2$$
$$\frac{L}{2m^{2}} \nabla J_{uk+12} \le \begin{pmatrix} L \\ \|\nabla J_{uk}\|_{2} \\ 2m^{2} \end{pmatrix} .(*_{1})$$
Nếu ta ký hiệu tối tiểu giá trị của $f$ bởi $p^{*}$, thì số của damped Newton các bước là nhiều nhất
$$\frac{J(u_{0})p^{*}}{\gamma} -.$$
Phương trình $(*_{1})$ và sự kiện rằng $\eta  \le m^{2}/L$ chỉ ra rằng nếu $\|\nabla J_{uk}\|_{2} < \eta$, thì

$\nabla J_{uk+12} < \eta$. Nó suy ra bởi quy nạp rằng với mọi $\ell \ge k$, ta có
$$2$$
$$\frac{L}{2m^{2}} \nabla J_{u\ell+12} \le \begin{pmatrix} L \\ \|\nabla J_{u\ell}\|_{2} \\ 2m^{2} \end{pmatrix} ,(*_{2})$$
Và do đó (vì $\eta  \le m^{2}/L$ và $\|\nabla J_{uk}\|_{2} < \eta$, ta có $(L/m^{2}) \|\nabla J_{uk}\|_{2} < (L/m^{2})\eta  \le 1)$, do đó
$$2\ell -k$$
$$1^{2\ell-k}$$
$$\frac{L}{2m^{2}} \|\nabla J_{u\ell}\|_{2} \le \begin{pmatrix} L \\ \|\nabla J_{uk}\|_{2} \\ 2m^{2} \end{pmatrix} \le \begin{pmatrix} \overline{2} \end{pmatrix} ,\ell \ge k.(*_{3})$$
Nó được hiển thị trong Boyd và Vandenberghe $[29]$ (Mục 9.1.2) rằng giả thiết mI $⪯\nabla^{2}$ J(x) suy ra rằng
$$J(x) -p^{*}\le \frac{1}{2m} \|\nabla J_{x}\|_{2}^{2}x \in \Omega .$$
Hệ quả là, bởi $(*_{3})$, ta có
$$1^{2\ell-k+1}$$
$$J(u_{\ell}) -p^{*}\le \frac{1}{2m} \|\nabla J_{u\ell}\|_{2}^{2} \le \frac{2m^{3}}{L^{2}} \begin{pmatrix} \overline{2} \end{pmatrix} .(*_{4})$$
Phương trình $(*_{4})$ chỉ ra rằng sự hội tụ during quadratically sự hội tụ phase là rất fast. Nếu ta cho
$$\epsilon_{0}  = \frac{2m^{3}}{L^{2}} ,$$
Thì Phương trình $(*_{4})$ suy ra rằng ta phải có $J(u_{\ell})$ - $p^{*} \le \epsilon$ sau không có nhiều hơn
$$log_{2} log_{2}(\epsilon_{0} /\epsilon )$$

<!-- PAGE 1740 -->
Các vòng lặp. số hạng $log_{2} log_{2}(\epsilon_{0} /\epsilon$) grows extremely slowly như $\epsilon$ đi đến không, và cho thực tế các mục đích nó có thể được được xét hằng số, nói năm hoặc sáu (sáu các vòng lặp cho accuracy của về $\epsilon  \approx 5 \cdot  10^{-20}\epsilon_{0}$). Trong tóm tắt, số của Newton các vòng lặp cần thiết để tìm cực tiểu của $J$ là một cách xấp xỉ bị chặn bởi
$$\frac{J(u_{0})p^{*}}{\gamma} -+ 6.$$
Các ví dụ của ứng dụng của Newton’s phương pháp và further thảo luận của của nó efficiency là cho trước trong Boyd và Vandenberghe $[29]$ (Mục 9.5.4). Basically, Newton’s phương pháp có faster sự hội tụ tốc độ hơn gradien hoặc hạ nhanh nhất (steepest descent). Của nó chính disadvantage là chi phí cho tạo thành và storing Hessian, và của việc tính toán Newton bước, mà đòi hỏi việc giải hệ phương trình tuyến tính. Có hai major shortcomings của sự hội tụ giải tích/phân tích của Newton’s phương pháp như được phác thảo ở trên. thứ nhất là pracical một. complexity estimates liên quan đến các hằng số $m, M$, và $L$, mà là hầu như không bao giờ đã biết trong thực tế. Kết quả là, cận trên số của các bước cần thiết là hầu như không bao giờ đã biết specifically. thứ hai shortcoming là rằng mặc dù Newton’s phương pháp chính nó là afin bất biến, giải tích/phân tích của sự hội tụ là rất nhiều phụ thuộc trên lựa chọn của tọa độ hệ. Nếu tọa độ hệ là đã thay đổi, các hằng số $m, M, L$ cũng thay đổi. Điều này có thể được được quan điểm như aesthetic bài toán, nhưng nó sẽ là đẹp nếu giải tích/phân tích của sự hội tụ độc lập của afin thay đổi của các tọa độ có thể là cho trước. Nesterov và Nemirovski discovered điều kiện trên các hàm rằng cho phép affineinvariant sự hội tụ giải tích/phân tích. tính chất này, được gọi là self-concordance, là không may là không rất trực quan.

> **Định nghĩa 49.10.** (riêng) hàm lồi (convex function) $f$ được định nghĩa trên $\mathbb{R}$ là tự tương hợp (self-concordant) nếu
$$|f''' (x)| \le 2(f'' (x))^{3/2}for all x \in \mathbb{R}.$$
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
(riêng) hàm lồi (convex function) $f$ được định nghĩa trên là tự tương hợp (self-concordant) nếu với mọi khác không $v \in$ và tất cả $x \in \mathbb{R}^{n}$, hàm $t \mapsto$ J(x $+$ tv) là tự tương hợp (self-concordant). Afin và lồi toàn phương các hàm là hiển nhiên tự tương hợp (self-concordant), vì f''' $= 0$. Có nhiều nhiều hơn/thêm thú vị tự tương hợp (self-concordant) các hàm, ví dụ, hàm $X \mapsto$ -log det(X), ở đâu $X$ là đối xứng xác định dương (SPD) ma trận. Self-concordance được thảo luận extensively trong Boyd và Vandenberghe $[29]$ (Mục 9.6). chính điểm của self-concordance là rằng tọa độ system-invariant chứng minh của sự hội tụ có thể được cho trước cho nhất định lớp của lồi chặt (strictly convex) tự tương hợp (self-concordant) các hàm. chứng minh này là cho trước trong Boyd và Vandenberghe $[29]$ (Mục 9.6.4). Cho trước bắt đầu giá trị $u_{0}$, ta giả sử
$$\mathbb{R}^{n}$$
Rằng sublevel tập hợp ${x \in$ | J(x) $\le J(u_{0})}$ là đóng và rằng $J$ là bị chặn ở dưới. Thì có hai các tham số $\eta$ và $\gamma$ như trước, nhưng tùy thuộc chỉ trên các tham số $\alpha , \beta$ liên quan trong đường thẳng search, sao cho:
