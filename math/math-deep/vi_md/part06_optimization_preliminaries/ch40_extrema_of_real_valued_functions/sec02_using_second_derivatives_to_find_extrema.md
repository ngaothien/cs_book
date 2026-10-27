# Bằng cách sử dụng Thứ hai Các đạo hàm để tìm Các cực trị


<!-- PAGE 1506 -->

## 40.2 Bằng cách sử dụng Thứ hai Các đạo hàm để tìm Các cực trị

Cho sake của brevity, ta xét chỉ trường hợp của địa phương các cực tiểu; tương tự các kết quả là thu được cho địa phương các cực đại (thay thế $J$ bởi $-J$, vì $max_{u}$ J(u) $= -min_{u}$ -J(u)). Ta bắt đầu với cần điều kiện cho không ràng buộc cực tiểu địa phương (local minimum).

> **Mệnh đề 40.5.** Cho $E$ là không gian vectơ định chuẩn (normed vector space) và cho $J$: $\Omega \to \mathbb{R}$ là hàm, với $\Omega$ một số mở tập con của $E$. Nếu hàm $J$ là khả vi (differentiable) trong $\Omega$, nếu $J$ có đạo hàm thứ hai $D^{2}J(u)$ tại một số điểm $u \in \Omega$, và nếu $J$ có cực tiểu địa phương (local minimum) tại $u$, thì
$$D^{2}J(u)(w, w) \ge 0for all w \in E.$$

*Chứng minh.* Chọn bất kỳ khác không vectơ $w \in E$. Vì $\Omega$ là mở, cho $t$ nhỏ đủ, $u +$ tw $\in \Omega$ và J(u $+$ tw) $\ge$ J(u), do đó tồn tại một mở khoảng/đoạn $I \subseteq \mathbb{R}$ sao cho
$$u + tw \in \Omega andJ(u + tw) \ge J(u)$$
Với mọi $t \in$ I. Bằng cách sử dụng Taylor–Young công thức và sự kiện rằng ta phải có dJ(u) $= 0$ vì $J$ có cực tiểu địa phương (local minimum) tại $u$, ta thu được
$$t^{2} \| \epsilon$$
$$0 \le J(u + tw) -J(u) =2 D^{2}J(u)(w, w) + t^{2}w\|^{2}(tw),$$
Với $lim_{t\mapsto0} \epsilon$ (tw) $= 0$, mà suy ra rằng
$$D^{2}J(u)(w, w) \ge 0.$$
Vì lập luận nghiệm đúng với mọi $w \in E$ (một cách tầm thường nếu $w = 0)$, mệnh đề được chứng minh. Một nên là cautioned rằng không có điều ngược lại đến trước đó mệnh đề. Ví dụ, hàm $f$: $x \mapsto x^{3}$ có không có cực tiểu địa phương (local minimum) tại $0$, vẫn chưa df(0) $= 0$ và $D^{2}f(0)(u, v) = 0$.
$$\mathbb{R}^{2} \mathbb{R}$$
Tương tự, độc giả nên kiểm tra rằng hàm $f$: $\to$ cho trước bởi
$$f(x, y) = x^{2}-3y^{3}$$
Có không có cực tiểu địa phương (local minimum) tại $(0, 0)$; vẫn chưa df(0, $0) = 0$ vì df(x, $y) =$ (2x, $-9y^{2})$, và cho $u = (u_{1}, u_{2}), D^{2}f(0$, 0)(u, $u) = 2u_{1}^{2} \ge 0$ vì
$$D^{2}f(x, y)(u, u) = \begin{pmatrix} u_{1} & u_{2} \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 0 & -18y \end{pmatrix} \begin{pmatrix} u_{1} \\ u_{2} \end{pmatrix} .$$
Xem Hình 40.3. Khi $E = \mathbb{R}^{n}$, Mệnh đề 40.5 nói rằng rằng cần điều kiện cho có cực tiểu địa phương (local minimum) là rằng Hessian $\nabla^{2}$ J(u) là nửa xác định dương (positive semidefinite) (nó là luôn luôn đối xứng). Ta bây giờ cho đủ các điều kiện cho sự tồn tại của cực tiểu địa phương (local minimum).

<!-- PAGE 1507 -->

![Figure 40.3](../../assets/ch40/fig_40_3.png)

**Hình 40.3:** đồ thị của f(x, $y) = x^{2}$ - $3y^{3}$. Lưu ý rằng $(0, 0)$ không cực trị địa phương (local extremum) despite sự kiện rằng df(0, $0) = 0$.

> **Định lý 40.6.** Cho $E$ là không gian vectơ định chuẩn (normed vector space), cho $J$: $\Omega \to \mathbb{R}$ là hàm với $\Omega$ một số mở tập con của $E$, và giả sử rằng $J$ là khả vi (differentiable) trong $\Omega$ và rằng dJ(u) $= 0$ tại một số điểm $u \in \Omega$. Các tính chất sau đây đúng:
$(1)$ Nếu $D^{2}J(u)$ tồn tại và nếu tồn tại một số $\alpha  \in \mathbb{R}$ sao cho $\alpha  > 0$ và
$$D^{2}J(u)(w, w) \ge \alpha  \|w\|^{2}for all w \in E,$$
Thì $J$ có chặt cực tiểu địa phương (local minimum) tại $u$.
$(2)$ Nếu $D^{2}J(v)$ tồn tại với mọi $v \in \Omega$ và nếu có một hình cầu $B \subseteq \Omega$ được tâm tại $u$ sao cho
$$D^{2}J(v)(w, w) \ge 0for all v \in B and all w \in E,$$
Thì $J$ có cực tiểu địa phương (local minimum) tại $u$.

*Chứng minh.* $(1)$ Bằng cách sử dụng công thức của Taylor–Young, với mọi vectơ $w$ nhỏ đủ, ta có thể viết
$$\epsilon$$
$$J(u + w) -J(u) = \frac{1}{2} D^{2}J(u)(w, w) + \|w\|^{2}(w)$$
$$\ge \begin{pmatrix} 1 \\ \alpha  + \epsilon (w) \\ 2 \end{pmatrix} \|w\|^{2}$$
Với $lim_{w\mapsto0} \epsilon (w) = 0$. Hệ quả là nếu ta chọn $r > 0$ nhỏ đủ rằng $|\epsilon$ (w)| $< \alpha /2$ với mọi $w$ với $\|w\| < r$, thì J(u $+ w) >$ J(u) với mọi $u + w \in B$, ở đâu $B$ là hình cầu mở (open ball) của tâm $u$ và bán kính $r$. Điều này chứng tỏ rằng $J$ có địa phương chặt cực tiểu tại $u$.

<!-- PAGE 1508 -->
$(2)$ công thức của Taylor–Maclaurin chỉ ra rằng với mọi $u + w \in B$, ta có
$$J(u + w) = J(u) + \frac{1}{2} D^{2}J(v)(w, w) \ge J(u),$$
Với một số $v \in (u, u+w)$ (nhắc lại rằng $(u, u+w) = {(1-\lambda )(u+w)+\lambda (u+w)$ | $0 < \lambda  < 1})$. Có không có các điều ngược lại của hai assertions của Định lý 40.6. Tuy nhiên, có một điều kiện trên $D^{2}J(u)$ rằng suy ra điều kiện của Phần $(1)$. Vì điều kiện này là dễ hơn đến phát biểu khi $E =\mathbb{R}^{n}$, ta bắt đầu với trường hợp này. Nhắc lại rằng $n\times n$ ma trận đối xứng (symmetric matrix) $A$ là xác định dương (positive definite) nếu $x^{\top}Ax > 0$ với mọi $x \in \mathbb{R}^{n}-{0}$. Đặc biệt, $A$ phải là khả nghịch.

> **Mệnh đề 40.7.** Với mọi ma trận đối xứng (symmetric matrix) $A$, nếu $A$ là xác định dương (positive definite), thì tồn tại một $\alpha  > 0$ sao cho
$$x^{\top}Ax \ge \alpha  \|x\|^{2}for all x \in \mathbb{R}^{n}.$$
$$\mathbb{R}^{n}  \mathbb{R}^{n}$$

*Chứng minh.* Chọn bất kỳ chuẩn (norm) trong (nhắc lại rằng tất cả các chuẩn trên là tương đương). Vì unit
$$\mathbb{R}^{n}$$
Mặt cầu $S^{n-1} = {x \in$ | $\|x\| = 1}$ là compắc và vì hàm f(x) $= x^{\top}Ax$ là không bao giờ không trên $S^{n-1}$, hàm $f$ có cực tiểu $\alpha  > 0$ trên $S^{n-1}$. Bằng cách sử dụng thông thường mẹo/kỹ thuật rằng
$$\mathbb{R}^{n}$$
$x = \|x\|(x/ \|x\|)$ với mọi khác không vectơ $x \in$ và sự kiện rằng bất đẳng thức của mệnh đề là tầm thường cho $x = 0$, từ
$$x^{\top}Ax \ge \alpha for all x with \|x\|= 1,$$
Ta thu được
$$x^{\top}Ax \ge \alpha  \|x\|^{2}for all x \in \mathbb{R}^{n},$$
Như đã khẳng định. Ta có thể combine Định lý 40.6 và Mệnh đề 40.7 để thu được hữu ích đủ điều kiện cho sự tồn tại của chặt cực tiểu địa phương (local minimum). Thứ nhất cho chúng ta giới thiệu một số thuật ngữ.

> **Định nghĩa 40.6.** Cho trước hàm $J$: $\Omega \to \mathbb{R}$ như trước, nói rằng điểm $u \in \Omega$ là không suy biến tới hạn/quan trọng điểm nếu dJ(u) $= 0$ và nếu Ma trận Hesse (Hessian matrix) $\nabla^{2}$ J(u) là khả nghịch.

> **Mệnh đề 40.8.** Cho $J$: $\Omega \to \mathbb{R}$ là hàm được định nghĩa trên một số mở tập con $\Omega \subseteq \mathbb{R}^{n}$. Nếu $J$ là khả vi (differentiable) trong $\Omega$ và nếu một số điểm $u \in \Omega$ là không suy biến tới hạn/quan trọng điểm sao cho $\nabla^{2}$ J(u) là xác định dương (positive definite), thì $J$ có chặt cực tiểu địa phương (local minimum) tại $u$.
Nhận xét: Nó là khả dĩ/có thể đến tổng quát hóa Mệnh đề 40.8 đến vô hạn chiều các không gian bởi việc tìm phù hợp tổng quát hóa của khái niệm của không suy biến tới hạn/quan trọng điểm. một cách thứ nhất, ta giả sử rằng $E$ là Không gian Banach (Banach space) (đầy đủ không gian vectơ định chuẩn (normed vector space)). Thì ta định nghĩa
$$\mathbb{R}$$
Đối ngẫu (dual) E' của $E$ như tập hợp của liên tục các dạng tuyến tính trên $E$, sao cho E' $= \mathcal{L}(E$;). Sau đây Lang, ta sử dụng ký hiệu E' cho không gian của liên tục các dạng tuyến tính để tránh confusion
