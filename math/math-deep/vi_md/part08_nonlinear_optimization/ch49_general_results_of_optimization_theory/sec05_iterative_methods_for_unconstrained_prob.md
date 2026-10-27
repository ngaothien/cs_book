# Các phương pháp lặp cho Không ràng buộc Các bài tập


<!-- PAGE 1721 -->
$$\mathbb{R}^{n} \mathbb{R}$$

> **Hệ quả 49.10.** Nếu $J$: $\to$ là toàn phương hàm cho trước bởi
$$J(v) = \frac{1}{2} \langle Av, v\rangle -\langle b, v\rangle$$
Thì
$$\langle \nabla^{2} J_{u}(w), w\rangle \le \lambda_{n}  \|w\|^{2}$$
Ở đâu $\lambda_{n}$ là lớn nhất trị riêng (eigenvalue) của $A$; ở trên sự kiện sẽ là hữu ích sau này. Tương tự, cho trước toàn phương phiếm hàm $J$ được định nghĩa trên Không gian Hilbert (Hilbert space) $V$, ở đâu
$$J(v) = \frac{1}{2} a(v, v) -h(v),$$
Theo Định lý 49.8 $(4)$, phiếm hàm $J$ là elliptic khi và chỉ khi tồn tại một $\alpha  > 0$ sao cho
$$\langle \nabla^{2} J_{u}(v), v\rangle = a(v, v) \ge \alpha  \|v\|^{2}for all v \in V .$$
Điều này là một cách chính xác giả thiết $(*_{\alpha})$ được sử dụng trong Định lý 49.4.

## 49.5 Các phương pháp lặp cho Không ràng buộc

$$Problems$$
Ta sẽ bây giờ mô tả các phương pháp cho việc giải không ràng buộc cực tiểu hóa các bài tập, nghĩa là, việc tìm cực tiểu (hoặc các cực tiểu) của các hàm $J$ trên toàn bộ không gian $V$. các phương pháp này là lặp, mà có nghĩa là cho trước một số ban đầu vectơ $u_{0}$, ta xây dựng dãy $(u_{k})_{k\ge0}$ rằng hội tụ đến cực tiểu $u$ của hàm $J$. then chốt bước là định nghĩa $u_{k+1}$ từ $u_{k}$, và thứ nhất ý tưởng là để rút gọn bài toán đến đơn giản hơn bài toán, cụ thể là cực tiểu hóa của hàm của đơn lẻ (thực) biến. Cho điều này, ta cần hai perform hai các bước:
$(1)$ Tìm descent hướng tại $u_{k}$, mà là một số khác không vectơ $d_{k}$ mà là thường được xác định từ gradien của $J$ tại khác nhau các điểm. descent hướng $d_{k}$ phải thỏa mãn bất đẳng thức $\langle \nabla J_{uk}, d_{k}\rangle < 0$.
$(2)$ Chính xác đường thẳng search: Tìm cực tiểu của thu hẹp của hàm $J$ dọc theo đường thẳng qua $u_{k}$ và song song đến hướng $d_{k}$. Điều này có nghĩa là việc tìm thực $\rho_{k}  \in \mathbb{R}$ (tùy thuộc trên $u_{k}$ và $d_{k})$ sao cho
$$J(u_{k} + \rho_{k} d_{k}) = \inf J(u_{k} + \rho d_{k}).$$
$$\rho \in \mathbb{R}$$
Typically, $\rho_{k}  > 0$. bài toán này chỉ thành công nếu $\rho_{k}$ là duy nhất, trong mà trường hợp ta tập hợp
$$u_{k+1} = u_{k} + \rho_{k} d_{k}.$$
Bước này là thường được gọi là đường thẳng search hoặc đường thẳng cực tiểu hóa, và $\rho_{k}$ được gọi là bước nhảy (stepsize) tham số. Xem Hình 49.1.

<!-- PAGE 1722 -->
$$J (uk)$$
$$J (uk+1)$$
$$J (u+\rho dk)$$
$$k$$
$$ukdk+1$$
$$uk+1d$$
$$k$$
$$J (uk+1)J (u)$$
$$k+2$$
$$\mathbb{R}^{2} \mathbb{R}$$

![Figure 49.1](../../assets/ch49/fig_49_1.png)

**Hình 49.1:** Cho $J$: $\to$ là hàm có đồ thị được biểu diễn bởi hồng mặt. Cho trước điểm $u_{k}$ trong mặt phẳng $xy$, và hướng $d_{k}$, ta tính toán thứ nhất $u_{k+1}$ và thì $u_{k+2}$.

> **Mệnh đề 49.11.** Nếu $J$ là toàn phương elliptic phiếm hàm của tạo thành
$$J(v) = \frac{1}{2} a(v, v) -h(v),$$
Thì cho trước $d_{k}$, tồn tại duy nhất một $\rho_{k}$ việc giải đường thẳng search trong Bước $(2)$.

*Chứng minh.* Điều này là bởi vì, theo Mệnh đề 49.3, ta có
$$J(u_{k} + \rho d_{k}) = \frac{\rho^{2}}{2} a(d_{k}, d_{k}) + \rho \langle \nabla J_{uk}, d_{k}\rangle + J(u_{k}),$$
Và vì $a(d_{k}, d_{k}) > 0$ (bởi vì $J$ là elliptic), ở trên hàm của $\rho$ có duy nhất cực tiểu khi đạo hàm của nó là không, cụ thể là
$$\rho  a(d_{k}, d_{k}) + \langle \nabla J_{uk}, d_{k}\rangle = 0.$$
Vì Bước $(2)$ là thường cũng một cách chi phí, alternative là
$(3)$ Backtracking đường thẳng search: Chọn hai các hằng số $\alpha$ và $\beta$ sao cho $0 < \alpha  < 1/2$ và $0 < \beta  < 1$, và tập hợp $t = 1$. Cho trước descent hướng $d_{k}$ tại $u_{k} \in$ dom(J), trong khi $J(u_{k} + td_{k}) > J(u_{k}) + \alpha t\langle \nabla J_{uk}, d_{k}\rangle$ thực hiện $t := \beta t; \rho_{k}  = t; u_{k+1} = u_{k} + \rho_{k} d_{k}$.

<!-- PAGE 1723 -->
Vì $d_{k}$ là descent hướng, ta phải có $\langle \nabla J_{uk}, d_{k}\rangle < 0$, do đó cho $t$ nhỏ đủ điều kiện $J(u_{k} + td_{k}) \le J(u_{k}) + \alpha t\langle \nabla J_{uk}, d_{k}\rangle$ sẽ đúng và search sẽ dừng. Nó có thể được được hiển thị rằng exit bất đẳng thức $J(u_{k} + td_{k}) \le J(u_{k}) + \alpha t\langle \nabla J_{uk}, d_{k}\rangle$ nghiệm đúng với mọi $t \in (0, t_{0}]$, với một số $t_{0} > 0$. Do đó backtracking đường thẳng search các dừng với bước độ dài $\rho_{k}$ rằng thỏa mãn $\rho_{k}  = 1$ hoặc $\rho_{k}  \in (\beta t_{0}, t_{0}]$. Care có là exercised sao cho $u_{k} + \rho_{k} d_{k} \in$ dom(J). Cho nhiều hơn/thêm chi tiết, xem Boyd và Vandenberghe $[29]$ (Mục 9.2). Ta bây giờ xét một của đơn giản nhất các phương pháp cho chọn các hướng của descent trong trường hợp ở đâu $V = \mathbb{R}^{n}$, mà là đến chọn các hướng của tọa độ các trục trong xích (cyclic) cách thức. Như vậy phương pháp được gọi là phương pháp của relaxation. Nếu ta viết
$$u_{k} = (u_{1}^{k}, u_{2}^{k}, \dots  , u_{n}^{k}),$$
Thì các thành phần $u_{i}^{k+1}$ của $u_{k+1}$ được tính theo $u_{k}$ bởi việc giải từ đỉnh/trên xuống sau đây hệ của các phương trình:
$$J(u_{1}^{k+1}, u_{2}^{k}, u_{3}^{k}, \dots  , u_{n}^{k}) = \inf J(\lambda , u_{2}^{k}, u_{3}^{k}, \dots  , u_{n}^{k})$$
$$\lambda \in \mathbb{R}$$
$$J(u_{1}^{k+1}, u_{2}^{k+1}, u_{3}^{k}, \dots  , u_{n}^{k}) = \inf J(u_{1}^{k+1}, \lambda , u_{3}^{k}, \dots  , u_{n}^{k})$$
$$\lambda \in \mathbb{R}$$
$$\vdots$$
$$J(u_{1}^{k+1}, \dots  , u_{n-1}^{k+1}, u_{n}^{k+1}) = \inf J(u_{1}^{k+1}, \dots  , u_{n-1}^{k+1}, \lambda ).$$
$$\lambda \in \mathbb{R}$$
Một cái khác và nhiều hơn/thêm informative cách đến viết ở trên hệ là để định nghĩa các vectơ $u_{k;i}$ bởi
$$u_{k;0} = (u_{1}^{k}, u_{2}^{k}, \dots  , u_{n}^{k})$$
$$u_{k;1} = (u_{1}^{k+1}, u_{2}^{k}, \dots  , u_{n}^{k})$$
$$\vdots$$
$$u_{k;i} = (u_{1}^{k+1}, \dots  , u_{i}^{k+1}, u_{i+1}^{k}, \dots  , u_{n}^{k})$$
$$\vdots$$
$$u_{k;n} = (u_{1}^{k+1}, u_{2}^{k+1}, \dots  , u_{n}^{k+1}).$$
Lưu ý rằng $u_{k;0} = u_{k}$ và $u_{k;n} = u_{k+1}$. Thì của ta cực tiểu hóa bài toán có thể được viết dưới dạng
$$J(u_{k;1}) = \inf J(u_{k;0} + \lambda e_{1})$$
$$\lambda \in \mathbb{R}$$
$$\vdots$$
$$J(u_{k;i}) = \inf J(u_{k;i-1} + \lambda e_{i})$$
$$\lambda \in \mathbb{R}$$
$$\vdots$$
$$J(u_{k;n}) = \inf J(u_{k;n-1} + \lambda e_{n}),$$
$$\lambda \in \mathbb{R}$$
