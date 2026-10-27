# Sự hội tụ của Hạ gradien (gradient descent) với Biến Bước nhảy (stepsize)


<!-- PAGE 1731 -->
49.5. Geometrically điều này quy trình tương ứng với giao nhau mặt phẳng -8x $+$ 12y $= -8$ với ellipsoid J(x, $y) =_{2}^{3}x^{2} +$ 2xy $+ 3y^{2}$ - 2x $+$ 8y đến tạo thành parabolic đường cong f(x) $= 25/6x^{2} -2/3x -4$, và thì locating x-coordinate của của nó đỉnh mà xảy ra khi f' $(x) = 0$, i.e khi $x = 2/25$; xem Hình 49.6. Sau $31$ các vòng lặp, điều này quy trình stabi-

![Figure 49.6](../../assets/ch49/fig_49_6.png)

**Hình 49.6:** Hai các quan điểm của giao giữa mặt phẳng -8x $+$ 12y $= -8$ và ellipsoid J(x, $y) =_{2}^{3}x^{2} +$ 2xy $+ 3y^{2}$ - 2x $+$ 8y. điểm $u_{k+1}$ là cực tiểu của parabolic giao. lizes đến điểm $(2, -2)$, mà như ta biết, là duy nhất cực tiểu của toàn phương ellipsoid
$$+ 2 -$$
J(x, $y) =_{2}^{3}x^{2}$ xy $+ 3y^{2}$ 2x $+$ 8y. chứng minh của sự hội tụ của gradien phương pháp với backtracking đường thẳng search, dưới giả thiết rằng $J$ là lồi chặt (strictly convex), là cho trước trong Boyd và Vandenberghe[29] (Mục 9.3.1). Nhiều hơn/thêm chi tiết trên phương pháp này và hạ nhanh nhất (steepest descent) phương pháp cho Euclidean chuẩn (norm) có thể cũng là tìm thấy trong Boyd và Vandenberghe $[29]$ (Mục 9.3).

## 49.7 Sự hội tụ của Hạ gradien (gradient descent) với Biến

$$Stepsize$$
Ta bây giờ cho đủ điều kiện cho gradien phương pháp với biến bước nhảy (stepsize) tham số đến hội tụ. Ngoài đòi hỏi $J$ là elliptic phiếm hàm, ta cộng Lipschitz

<!-- PAGE 1732 -->
Điều kiện trên gradien của $J$. Điều này time không gian $V$ có thể được vô hạn dimensional.

> **Mệnh đề 49.14.** Cho $J$: $V \to \mathbb{R}$ là một cách liên tục khả vi (differentiable) phiếm hàm được định nghĩa trên Không gian Hilbert (Hilbert space) $V$. Giả sử tồn tại hai các hằng số $\alpha  > 0$ và $M > 0$ sao cho
$$\langle \nabla J_{v} -\nabla J_{u}, v -u\rangle \ge \alpha  \|v -u\|^{2}for all u, v \in V ,$$
Và Lipschitz điều kiện
$$\|\nabla J_{v} -\nabla J_{u}\|\le M \|v -u\|for all u, v \in V .$$
Nếu tồn tại hai thực các số, $b \in \mathbb{R}$ sao cho
$$0 < a \le \rho_{k}  \le b \le \frac{2\alpha}{M^{2}} for all k \ge 0,$$
Thì gradien phương pháp với biến bước nhảy (stepsize) tham số hội tụ. Hơn nữa, tồn tại một hằng số $\beta  > 0$ (tùy thuộc trên $\alpha , M$,, $b)$ sao cho
$$\beta  < 1and\|u_{k} -u\|\le \beta^{k} \|u_{0} -u\|,$$
Ở đâu $u \in V$ là duy nhất cực tiểu của $J$.

*Chứng minh.* Bởi giả thiết phiếm hàm $J$ là elliptic, do đó theo Định lý 49.8(2) nó có duy nhất cực tiểu $u$ được đặc trưng hóa bởi sự kiện rằng $\nabla J_{u} = 0$. Khi đó vì $u_{k+1} = u_{k} -\rho_{k} \nabla J_{uk}$, ta có thể viết
$$u_{k+1} -u = (u_{k} -u) -\rho_{k} (\nabla J_{uk} -\nabla J_{u}).(*)$$
Bằng cách sử dụng các bất đẳng thức
$$\langle \nabla J_{uk} -\nabla J_{u}, u_{k} -u\rangle \ge \alpha  \|u_{k} -u\|^{2}$$
Và
$$\|\nabla J_{uk} -\nabla J_{u}\|\le M \|u_{k} -u\|,$$
Và giả sử rằng $\rho_{k}  > 0$, suy ra rằng
$$\|u_{k+1} -u\|^{2}= \|u_{k} -u\|^{2}-2\rho_{k} \langle \nabla J_{uk} -\nabla J_{u}, u_{k} -u\rangle + \rho_{k}^{2}  \|\nabla J_{uk} -\nabla J_{u}\|^{2}$$
$$\le \begin{pmatrix} 1 -2\alpha \rho_{k}  + M^{2}\rho_{k}^{2} \end{pmatrix} \|u_{k} -u\|^{2}.$$
Xét hàm
$$T(\rho ) = M^{2}\rho^{2} -2\alpha \rho  + 1.$$
Của nó đồ thị là parabol giao nhau trục $y$ tại $y = 1$ cho $\rho  = 0$, nó có cực tiểu cho $\rho  = \alpha /M^{2}$, và nó cũng có giá trị $y = 1$ cho $\rho  = 2\alpha /M^{2}$; xem Hình 49.7. Vì vậy nếu ta chọn, $b$ và $\rho_{k}$ sao cho
$$0 < a \le \rho_{k}  \le b < \frac{2\alpha}{M^{2}} ,$$

<!-- PAGE 1733 -->
Ta đảm bảo rằng cho $\rho  \in$ [, $b]$ ta có
$$T(\rho )^{1/2}= (M^{2} \rho^{2} -2\alpha \rho  + 1)^{1/2}\le (\max{T(a), T(b)})^{1/2}= \beta  < 1.$$
Thì bởi quy nạp ta thu được
$$\|u_{k+1} -u\|\le \beta^{k+1} \|u_{0} -u\|,$$
Mà chứng minh sự hội tụ.
$$y = 1$$
$$(0,1)$$
$$(\overline{\alpha},1 -\overline{\alpha})$$
$$\overline{M}\overline{2}\overline{M}\overline{2}$$
$$\overline{\alpha}\overline{2}\overline{\alpha}$$
$$a\overline{2} b\overline{2}$$
$$\overline{M}\overline{M}$$
$$Figure 49.7: The parabola T(\rho ) used in the proof of Proposition 49.14.$$
Các nhận xét: Trong chứng minh của Mệnh đề 49.14, nó là sự kiện rằng $V$ là đầy đủ mà đóng then chốt vai trò. Nếu $J$ là hai lần khả vi (differentiable), giả thiết
$$\|\nabla J_{v} -\nabla J_{u}\|\le M \|v -u\|for all u, v \in V$$
Có thể được biểu diễn dưới dạng
$$\sup

$\nabla^{2} J_{v}$

$\le$ M.$$
$$v\in V$$
Trong trường hợp của toàn phương elliptic phiếm hàm được định nghĩa trên $\mathbb{R}^{n}$,
$$J(v) = \langle Av, v\rangle -\langle b, v\rangle ,$$
Trên cận $2\alpha /M^{2}$ có thể được được cải thiện. Trong trường hợp này ta có
$$\nabla J_{v} = Av -b,$$
Và ta biết rằng $\alpha  = \lambda_{1}$ và $M = \lambda_{n}$ thực hiện job, ở đâu $\lambda_{1}$ là nhỏ nhất trị riêng (eigenvalue) của $A$ và $\lambda_{n}$ là lớn nhất trị riêng (eigenvalue) của $A$. Do đó ta có thể chọn, $b$ sao cho
$$0 < a \le \rho_{k}  \le b < \frac{2\lambda_{1}}{\lambda_{n}^{2}} .$$

<!-- PAGE 1734 -->
Vì $u_{k+1} = u_{k}$ - $\rho_{k} \nabla J_{uk}$ và $\nabla J_{uk} = Au_{k}$ - $b$, ta có
$$u_{k+1} -u = (u_{k} -u) -\rho_{k} (Au_{k} -Au) = (I -\rho_{k} A)(u_{k} -u),$$
Do đó ta thu được
$$\|u_{k+1} -u\|\le \|I -\rho_{k} A\|_{2} \|u_{k} -u\|.$$
Tuy nhiên, vì I - $\rho_{k} A$ là ma trận đối xứng (symmetric matrix), $\|I$ - $\rho_{k} A\|_{2}$ là lớn nhất tuyệt đối giá trị của các trị riêng (các trị riêng (eigenvalues)) của nó, do đó
$$\|I -\rho_{k} A\|_{2} \le \max{|1 -\rho_{k} \lambda_{1} |, |1 -\rho_{k} \lambda_{n} |}.$$
Hàm
$$\mu (\rho ) = \max{|1 -\rho \lambda_{1} |, |1 -\rho \lambda_{n} |}$$
Là từng khúc afin hàm, và nó là dễ để xem rằng nếu ta chọn, $b$ sao cho
$$0 < a \le \rho_{k}  \le b < \frac{2}{\lambda_{n}} ,$$
Thì
$$\max \mu (\rho ) \le \max{\mu (a), \mu (b)} < 1.$$
$$\rho \in [a,b]$$
Vì vậy, trên cận $2\lambda_{1} /\lambda_{n}^{2}$ có thể được được thay thế bởi $2/\lambda_{n}$, mà là typically nhiều lớn hơn. “tốt” chọn cho $\rho_{k}$ là $2/(\lambda_{1}  + \lambda_{n}$) (như opposed đến $\lambda_{1} /\lambda_{n}^{2}$ cho thứ nhất phiên bản). Trong trường hợp này
$$-$$
$$|1 -\rho_{k} \lambda_{1} | = |1 -\rho_{k} \lambda_{n} | = \frac{\lambda_{n} \lambda_{1}}{\lambda_{n}  + \lambda_{1}} ,$$
Do đó ta thu được
$$-\lambda  - -$$
$$\beta  = \frac{\lambda_{n} \lambda_{1}}{\lambda_{n}  + \lambda_{1}} \overline{=}_{\lambda}^{\lambda n1} \frac{1}{+ 1} \overline{n}  = \frac{cond_{2}(A)1}{cond_{2}(A) + 1} ,$$
$$\overline{\lambda}\overline{1}$$
Ở đâu $cond_{2}(A) = \lambda_{n} /\lambda_{1}$ là số điều kiện (condition number) của ma trận $A$ đối với spectral chuẩn (norm). Do đó ta xem rằng lớn hơn số điều kiện (condition number) của $A$ là, slower sự hội tụ của phương pháp sẽ là. Điều này là không đáng ngạc nhiên vì ta đã biết rằng các hệ phương trình tuyến tính liên quan đến ill-conditioned các ma trận (các ma trận với lớn số điều kiện (condition number)) là problematic và prone đến số tính mất ổn định. Một cách đến deal với bài toán này là để sử dụng phương pháp đã biết như preconditioning. Ta chỉ được mô tả hầu hết cơ bản hạ gradien (gradient descent) các phương pháp. Có numerous các biến thể, và ta chỉ mention một vài của các phương pháp này. phương pháp của scaling bao gồm trong bằng cách sử dụng $-\rho_{k} D_{k}\nabla J_{uk}$ như descent hướng, ở đâu $D_{k}$ là một số suitably được chọn đối xứng xác định dương (SPD) ma trận. Trong gradien phương pháp với extrapolation, $u_{k+1}$ được xác định bởi
$$u_{k+1} = u_{k} -\rho_{k} \nabla J_{uk} + \beta_{k} (u_{k} -u_{k-1}).$$
