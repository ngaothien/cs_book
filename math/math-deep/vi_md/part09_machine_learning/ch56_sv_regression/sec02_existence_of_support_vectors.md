# Sự tồn tại của Hỗ trợ/giá (support) Các vectơ


<!-- PAGE 2118 -->
Mà cho ta
$$p_{m} \ge \frac{\nu m}{2} .$$
Đồng dạng lập luận áp dụng nếu $\mu_{i}  > 0$.
$(3)$ Điều này suy ra ngay lập tức từ $(1)$. Mệnh đề 56.2 cho ta các cận trên $\nu$, cụ thể là
$$ 2 2$$
$$\max \frac{2p_{f}}{m} , \frac{q_{f}}{m} \le \nu  \le \min \frac{2p_{m}}{m} , \frac{q_{m}}{m} ,$$
Với $p_{f} \le p_{m}, q_{f} \le q_{m}, p_{f} + q_{f} \le m$ và $p_{m} + q_{m} \le m$. Cũng, $p_{f} = q_{f} = 0$ có nghĩa là $\epsilon$ -dải phẳng (slab) là wide đủ sao cho có không có các sai số (không có các điểm chặt bên ngoài dải phẳng (slab)). Nhận thấy rằng nhỏ giá trị của $\nu$ các giữ $p_{f}$ và $q_{f}$ nhỏ, mà là đạt được nếu $\epsilon$ -dải phẳng (slab) là wide. lớn giá trị của $\nu$ cho phép $p_{m}$ và $q_{m}$ là fairly lớn, mà là đạt được nếu $\epsilon$ -dải phẳng (slab) là narrow. Do đó nhỏ hơn $\nu$ là, wider $\epsilon$ -dải phẳng (slab) là, và lớn hơn $\nu$ là, narrower $\epsilon$ -dải phẳng (slab) là.

## 56.2 Sự tồn tại của Hỗ trợ/giá (support) Các vectơ

Ta bây giờ xét vấn đề của sự tồn tại của hỗ trợ/giá (support) các vectơ. Ta sẽ chỉ ra rằng trong generic trường hợp, với mọi nghiệm tối ưu (optimal solution) cho mà $\epsilon  > 0$, tồn tại một hỗ trợ/giá (support) vectơ trên xanh lam lề (margin) và một số hỗ trợ/giá (support) vectơ trên đỏ lề (margin). Ở đây generic có nghĩa là có một nghiệm tối ưu (optimal solution) với một số $\nu  < (m$ - $1)/m$. Nếu dữ liệu tập hợp $(X, y)$ là tốt fit bởi một số afin hàm f(x) $= w^{\top}x + b$, trong nghĩa rằng cho nhiều các cặp $(x_{i}, y_{i})$ ta có $y_{i} = w^{\top}x_{i} + b$ và $\ell^{1}$ -sai số
$$\sum_{i=1}^{m}  |w^{\top}x_{i} + b -y_{i}|$$
Là nhỏ, thì nghiệm tối ưu (optimal solution) có thể có $\epsilon  = 0$. Geometrically, nhiều các điểm $(x_{i}, y_{i})$ thuộc đến siêu phẳng (hyperplane) $H_{w,b}$. tình huống trong mà $\epsilon  = 0$ tương ứng với cực tiểu hóa $\ell^{1}$ -sai số với toàn phương penalization của $w$. Điều này là sort của đối ngẫu (dual) của lasso. sự kiện rằng afin hàm f(x) $= w^{\top}x + b$ fits perfectly nhiều các điểm tương ứng với sự kiện rằng $\ell^{1}$ -cực tiểu hóa tiến tới đến encourage sparsity. Trong trường hợp này, nếu $C$ được chọn cũng nhỏ, nó là khả dĩ/có thể rằng tất cả các điểm là các sai số (mặc dù “nhỏ”) và có không có hỗ trợ/giá (support) các vectơ. Nhưng nếu $C$ là lớn đủ, nghiệm sẽ là thưa (sparse) và ở đó sẽ là nhiều hỗ trợ/giá (support) các vectơ trên siêu phẳng (hyperplane) $H_{w,b}$. Cho $E_{\lambda} = {i \in {1, \dots  , m}$ | $\xi_{i}  > 0}, E_{\mu} = {j \in {1, \dots  , m}$ | $\xi_{j}'  > 0}, p_{sf} = |E_{\lambda}|$ và $q_{sf} = |E_{\mu}|$. Hiển nhiên, $E_{\lambda}$ và $E_{\mu}$ là rời nhau. Cho trước bất kỳ thực các số $u, v, x, y$, nếu $max{u, v} < min{x, y}$, thì $u < x$ và $v < y$. Điều này là bởi vì $u, v \le max{u, v} < min{x, y} \le x, y$.

<!-- PAGE 2119 -->

> **Mệnh đề 56.3.** Nếu $\nu  < (m$ - $1)/m$, thì $p_{f} < ⌊m/2⌋$ và $q_{f} < ⌊m/2⌋$.

*Chứng minh.* Theo Mệnh đề 56.2, $max{2p_{f}/m, 2q_{f}/m} \le \nu$. Nếu $m$ là chẵn/ngay cả, nói $m =$ 2k, thì
$$2p_{f}/m = 2p_{f}/(2k) \le \nu  < (m -1)/m = (2k -1)/2k,$$
Do đó $2p_{f} <$ 2k - $1$, mà suy ra $p_{f} < k = ⌊m/2⌋$. đồng dạng lập luận chỉ ra rằng $q_{f} < k = ⌊m/2⌋$. Nếu $m$ là lẻ, nói $m =$ 2k $+ 1$, thì
$$2p_{f}/m = 2p_{f}/(2k + 1) \le \nu  < (m -1)/m = 2k/(2k + 1),$$
Do đó $2p_{f} <$ 2k, mà suy ra $p_{f} < k = ⌊m/2⌋$. đồng dạng lập luận chỉ ra rằng $q_{f} < k = ⌊m/2⌋$. Vì $p_{sf} \le p_{f}$ và $q_{sf} \le q_{f}$, ta cũng có $p_{sf} < ⌊m/2⌋$ và $q_{sf} < ⌊m/2⌋$. Điều này suy ra rằng ${1, \dots  , m} -(E_{\lambda} \cup E_{\mu})$ chứa ít nhất hai các phần tử và có các ràng buộc tương ứng với ít nhất hai $i \in / (E_{\lambda} \cup E_{\mu})$ (trong mà trường hợp $\xi_{i}  = \xi_{i}'  = 0)$, của tạo thành
$$w^{\top}x_{i} + b -y_{i} \le \epsilon i \in /(E_{\lambda} \cup E_{\mu})$$
$$-w^{\top}x_{i} -b + y_{i} \le \epsilon i \in /(E_{\lambda} \cup E_{\mu}).$$
Nếu $w^{\top}x_{i} + b$ - $y_{i} = \epsilon$ với một số $i \in / (E_{\lambda} \cup E_{\mu})$ và $-w^{\top}x_{j}$ - $b + y_{j} = \epsilon$ với một số $j \in / (E_{\lambda} \cup E_{\mu})$ với $i \neq  j$, thì ta có xanh lam hỗ trợ/giá (support) vectơ và đỏ hỗ trợ/giá (support) vectơ. Ngược lại, ta chỉ ra cách mà đến sửa đổi $b$ và $\epsilon$ để thu được nghiệm tối ưu (optimal solution) với xanh lam hỗ trợ/giá (support) vectơ và đỏ hỗ trợ/giá (support) vectơ.

> **Mệnh đề 56.4.** Với mọi nghiệm tối ưu (optimal solution) $(w, b, \epsilon , \xi , \xi'$) với $w \neq  0$ và $\epsilon  > 0$, nếu
$$\nu  < (m -1)/m$$
Và nếu hoặc không có $x_{i}$ là xanh lam hỗ trợ/giá (support) vectơ hoặc không có $x_{i}$ là đỏ hỗ trợ/giá (support) vectơ, thì ở đó là một cái khác nghiệm tối ưu (optimal solution) (cho cùng $w)$ với một số $i_{0}$ sao cho $\xi_{i0}  = 0$ và $w^{\top}x_{i0}+b-y_{i0} = \epsilon$, và tồn tại một $j_{0}$ sao cho $\xi_{j0}'  = 0$ và $-w^{\top}x_{j0}$ - $b + y_{j0} = \epsilon$; nói cách khác, một số $x_{i0}$ là xanh lam hỗ trợ/giá (support) vectơ và một số $x_{j0}$ là đỏ hỗ trợ/giá (support) vectơ (với $i_{0} \neq  j_{0})$. Nếu tất cả các điểm $(x_{i}, y_{i})$ rằng là không các sai số lie trên một của lề (margin) các siêu phẳng, thì có một nghiệm tối ưu (optimal solution) cho mà $\epsilon  = 0$.

*Chứng minh.* Theo Mệnh đề 56.3 nếu $\nu  < (m$ - $1)/m$, thì $p_{f} < ⌊m/2⌋$ và $q_{f} < ⌊m/2⌋$, do đó sau đây các ràng buộc đúng:
$$w^{\top}x_{i} + b -y_{i} = \epsilon  + \xi_{i} \xi_{i}  > 0i \in E_{\lambda}$$
$$-w^{\top}x_{j} -b + y_{j} = \epsilon  + \xi_{j}' \xi_{j}'  > 0j \in E_{\mu}$$
$$w^{\top}x_{i} + b -y_{i} \le \epsilon i \in /(E_{\lambda} \cup E_{\mu})$$
$$-w^{\top}x_{i} -b + y_{i} \le \epsilon i \in /(E_{\lambda} \cup E_{\mu}),$$

<!-- PAGE 2120 -->
Ở đâu $|{1, \dots  , m}$ - $(E_{\lambda} \cup E_{\mu})| \ge 2$. Nếu của ta nghiệm tối ưu (optimal solution) thực hiện không có xanh lam hỗ trợ/giá (support) vectơ và đỏ hỗ trợ/giá (support) vectơ, thì hoặc $w^{\top}x_{i} +b-y_{i} < \epsilon$ với mọi $i \in / (E_{\lambda} \cup E_{\mu})$ hoặc $-w^{\top}x_{i} -b+y_{i} < \epsilon$ với mọi $i \in / (E_{\lambda} \cup E_{\mu})$. Trường hợp $1$. Ta có
$$w^{\top}x_{i} + b -y_{i} < \epsilon i \in /(E_{\lambda} \cup E_{\mu})$$
$$-w^{\top}x_{i} -b + y_{i} \le \epsilon i \in /(E_{\lambda} \cup E_{\mu}).$$
Có hai subcases. Trường hợp 1a. Giả sử rằng tồn tại một $j \in / (E_{\lambda} \cup E_{\mu})$ sao cho $-w^{\top}x_{j}$ - $b + y_{j} = \epsilon$. Của ta chiến lược là đến giảm $\epsilon$ và tăng $b$ bởi nhỏ lượng $\theta$ trong như vậy cách rằng một số bất đẳng thức $w^{\top}x_{i} + b$ - $y_{i} < \epsilon$ trở thành phương trình với một số $i \in / (E_{\lambda} \cup E_{\mu})$. Geometrically, điều này tương đương với đến raising tách siêu phẳng (hyperplane) $H_{w,b}$ và giảm chiều rộng của dải phẳng (slab), giữ đỏ lề (margin) siêu phẳng (hyperplane) unchanged. Xem Hình 56.7.
$$\xi ‘$$
$$i0$$
$$є =$$
$$red support vector b +$$
$$x -z +$$
$$wT$$
$$є$$
$$є$$
$$b = 0$$
$$x -z +$$
$$w T  = 0$$
$$b - є$$
$$x -z +$$
$$wT$$
$$no blue support vector\xi$$
$$i$$
$$\xi ‘) = 0$$
$$i(є-\theta$$
$$\theta ) +$$
$$red support vector(b+$$
$$-z +$$
$$є- \theta w T x$$
$$) = 0$$
$$b+ \theta$$
$$z + ($$
$$wT  x -$$
$$є- \theta$$
$$-\theta )= 0$$
$$) - (є$$
$$b+\theta$$
$$-z + ($$
$$blue support vectorwT  x$$
$$T$$
$$\xi +2 \theta$$
$$i$$

![Figure 56.7](../../assets/ch56/fig_56_7.png)

**Hình 56.7:** Trong điều này illustration các điểm trong phạm vi $\epsilon$ -tube được ký hiệu bởi mở các đường tròn. Trong ban đầu, trên trái configuration, không có xanh lam hỗ trợ/giá (support) vectơ. Bởi raising hồng tách siêu phẳng (hyperplane) và giảm chiều rộng của dải phẳng (slab), ta kết thúc/cuối lên với xanh lam hỗ trợ/giá (support) vectơ. các bất đẳng thức suy ra rằng
$$-\epsilon  \le w^{\top}x_{i} + b -y_{i} < \epsilon .$$
Cho chúng ta chọn $\theta$ sao cho
$$\theta  = (1/2) \min{\epsilon  -w^{\top}x_{i} -b + y_{i} | i \in /(E_{\lambda} \cup E_{\mu})}.$$

<!-- PAGE 2121 -->
Của ta các giả thiết suy ra rằng $\theta  > 0$, và ta có $\theta  \le \epsilon$, bởi vì $(1/2)(\epsilon  -w^{\top}x_{i} -b + y_{i}) \le \epsilon$ là tương đương đến $\epsilon$ - $w^{\top}x_{i}$ - $b + y_{i} \le 2\epsilon$ mà là tương đương đến $-w^{\top}x_{i}$ - $b + y_{i} \le \epsilon$, mà nghiệm đúng với mọi $i \in / (E_{\lambda} \cup E_{\mu})$ bởi giả thiết. Ta có thể viết
$$w^{\top}x_{i} + b + \theta  -y_{i} = \epsilon  -\theta  + \xi_{i}  + 2\theta \xi_{i}  > 0i \in E_{\lambda}$$
$$-w^{\top}x_{j} -(b + \theta ) + y_{j} = \epsilon  -\theta  + \xi_{j}' \xi_{j}'  > 0j \in E_{\mu}$$
$$w^{\top}x_{i} + b + \theta  -y_{i} \le \epsilon  -\theta i \in /(E_{\lambda} \cup E_{\mu})$$
$$-w^{\top}x_{i} -(b + \theta ) + y_{i} \le \epsilon  -\theta i \in /(E_{\lambda} \cup E_{\mu}).$$
Bởi giả thiết
$$-w^{\top}x_{j} -(b + \theta ) + y_{j} = \epsilon  -\theta for some j \in /(E_{\lambda} \cup E_{\mu})$$
Và bởi lựa chọn của $\theta$,
$$w^{\top}x_{i} + b + \theta  -y_{i} = \epsilon  -\theta for some i \in /(E_{\lambda} \cup E_{\mu}).$$
Giá trị của $C > 0$ là irrelevant trong sau đây lập luận do đó ta có thể giả sử rằng $C = 1$. mới giá trị của hàm mục tiêu (objective function) là
$$\omega (\theta ) = \frac{1}{2} w^{\top}w + \nu (\epsilon  -\theta ) + \frac{1}{m} \sum_{i\in E\lambda}  \sum_{j\in E\mu}$$
$$\begin{pmatrix} (\xi_{i}  + 2\theta ) + & \xi_{j}' \\  & 2 \end{pmatrix}$$
$$= \frac{1}{2} w^{\top}w + \nu \epsilon  + \frac{1}{m} \sum_{i\in E\lambda}  \sum_{j\in E\mu}  - \begin{pmatrix} p_{sf} \\ \nu  - \\ m \end{pmatrix} \theta .$$
$$\begin{pmatrix} \xi_{i}  + & \xi_{j}' \end{pmatrix}$$
Theo Mệnh đề 56.2 ta có
$$ 2$$
$$\max \frac{2p_{f}}{m} , \frac{q_{f}}{m} \le \nu$$
Và $p_{sf} \le p_{f}$ và $q_{sf} \le q_{f}$, mà suy ra rằng
$$\nu  - \frac{2p_{sf}}{m} \ge 0,(*_{1})$$
Và do đó $\omega (\theta$) $\le \omega (0)$. Nếu bất đẳng thức $(*_{1})$ là chặt, thì điều này contradicts tính tối ưu của ban đầu nghiệm. Vì vậy, $\nu  = 2p_{sf}/m, \omega (\theta$) $= \omega (0)$ và $(w, b + \theta , \epsilon$ - $\theta , \xi  + 2\theta , \xi'$) là nghiệm tối ưu (optimal solution) sao cho
$$w^{\top}x_{i} + b + \theta  -y_{i} = \epsilon  -\theta$$
$$-w^{\top}x_{j} -(b + \theta ) + y_{j} = \epsilon  -\theta$$
Với một số $i, j \in / (E_{\lambda} \cup E_{\mu})$ với $i \neq  j$.

<!-- PAGE 2122 -->
Nhận thấy rằng exceptional trường hợp trong mà $\theta  = \epsilon$ có thể phát sinh. Trong trường hợp này tất cả các điểm $(x_{i}, y_{i})$ rằng là không các sai số (chặt bên ngoài $\epsilon$ -dải phẳng (slab)) là trên đỏ lề (margin) siêu phẳng (hyperplane). trường hợp này có thể chỉ phát sinh nếu $\nu  = 2p_{sf}/m$. Trường hợp 1b. Ta có $-w^{\top}x_{i} -b + y_{i} < \epsilon$ với mọi $i \in / (E_{\lambda} \cup E_{\mu})$. Của ta chiến lược là đến giảm $\epsilon$ và tăng các sai số bởi nhỏ $\theta$ trong như vậy cách rằng một số bất đẳng thức trở thành phương trình với một số $i \in / (E_{\lambda} \cup E_{\mu})$. Geometrically, điều này tương ứng với giảm chiều rộng của dải phẳng (slab), giữ tách siêu phẳng (hyperplane) unchanged. Xem Các hình 56.8 và 56.9. Thì ta là rút gọn đến Trường hợp 1a hoặc Trường hợp 2a.
$$\xi ‘no red support vector$$
$$i0$$
$$є =$$
$$b +$$
$$x -z +$$
$$wT$$
$$є$$
$$є$$
$$b = 0$$
$$x -z +$$
$$w T = 0$$
$$b - є$$
$$x -z +$$
$$wT$$
$$no blue support vector$$
$$\xi i$$
$$\xi + \theta ‘$$
$$i$$
$$) = 0$$
$$Case 1ared support vector(є-\theta$$
$$b +$$
$$є- \theta -z +$$
$$w T x$$
$$b = 0$$
$$x -z +$$
$$є- \theta wT$$
$$)= 0$$
$$(є-\theta$$
$$+ b -$$
$$Tx -z$$
$$w$$
$$Tno blue support vector$$
$$\xi i+ \theta$$

![Figure 56.8](../../assets/ch56/fig_56_8.png)

**Hình 56.8:** Trong điều này illustration các điểm trong phạm vi $\epsilon$ -tube được ký hiệu bởi mở các đường tròn. Trong ban đầu, trên trái configuration, không có xanh lam hỗ trợ/giá (support) vectơ và không có đỏ hỗ trợ/giá (support) vectơ. Bởi giảm chiều rộng của dải phẳng (slab), ta kết thúc/cuối lên với đỏ hỗ trợ/giá (support) vectơ và rút gọn đến Trường hợp 1a. Ta có
$$w^{\top}x_{i} + b -y_{i} = \epsilon  + \xi_{i} \xi_{i}  > 0i \in E_{\lambda}$$
$$-w^{\top}x_{j} -b + y_{j} = \epsilon  + \xi_{j}' \xi_{j}'  > 0j \in E_{\mu}$$
$$w^{\top}x_{i} + b -y_{i} < \epsilon i \in /(E_{\lambda} \cup E_{\mu})$$
$$-w^{\top}x_{i} -b + y_{i} < \epsilon i \in /(E_{\lambda} \cup E_{\mu}).$$
Cho chúng ta chọn $\theta$ sao cho
$$\theta  = \min{\epsilon  -(w^{\top}x_{i} + b -y_{i}), \epsilon  + w^{\top}x_{i} + b -y_{i} | i \in /(E_{\lambda} \cup E_{\mu})},$$

<!-- PAGE 2123 -->
$$\xi ‘$$
$$ino red support vector$$
$$є = 0$$
$$b +$$
$$x -z +$$
$$wT$$
$$є$$
$$є$$
$$= 0$$
$$+ b$$
$$x -z$$
$$w T = 0$$
$$b - є$$
$$x -z +$$
$$wT$$
$$no blue support vector\xi$$
$$i$$
$$\xi + \theta ‘$$
$$ino red support vector$$
$$) = 0$$
$$Case 2a(є-\theta$$
$$b +$$
$$є- \theta -z +$$
$$w T x$$
$$= 0$$
$$+ b$$
$$є- \theta T x -z$$
$$w$$
$$)= 0$$
$$(є-\theta$$
$$+ b -$$
$$Tx -z$$
$$w$$
$$blue support vector$$
$$\xi i+ \theta$$

![Figure 56.9](../../assets/ch56/fig_56_9.png)

**Hình 56.9:** Trong điều này illustration các điểm trong phạm vi $\epsilon$ -tube được ký hiệu bởi mở các đường tròn. Trong ban đầu, trên trái configuration, không có xanh lam hỗ trợ/giá (support) vectơ và không có đỏ hỗ trợ/giá (support) vectơ. Bởi giảm chiều rộng của dải phẳng (slab), ta kết thúc/cuối lên với xanh lam hỗ trợ/giá (support) vectơ và rút gọn đến Trường hợp 2a. Của ta các giả thiết suy ra rằng $0 < \theta  < \epsilon$. Ta có thể viết
$$w^{\top}x_{i} + b -y_{i} = \epsilon  -\theta  + \xi_{i}  + \theta \xi_{i}  > 0i \in E_{\lambda}$$
$$-w^{\top}x_{j} -b + y_{j} = \epsilon  -\theta  + \xi_{j}'  + \theta \xi_{j}'  > 0j \in E_{\mu}$$
$$w^{\top}x_{i} + b -y_{i} \le \epsilon  -\theta i \in /(E_{\lambda} \cup E_{\mu})$$
$$-w^{\top}x_{i} -b + y_{i} \le \epsilon  -\theta i \in /(E_{\lambda} \cup E_{\mu}),$$
Và bởi lựa chọn của $\theta$, hoặc
$$w^{\top}x_{i} + b -y_{i} = \epsilon  -\theta for some i \in /(E_{\lambda} \cup E_{\mu})$$
Hoặc
$$-w^{\top}x_{i} -b + y_{i} = \epsilon  -\theta for some i \in /(E_{\lambda} \cup E_{\mu}).$$
Mới giá trị của hàm mục tiêu (objective function) là
$$\omega (\theta ) = \frac{1}{2} w^{\top}w + \nu (\epsilon  -\theta ) + \frac{1}{m} \sum_{i\in E\lambda}  \sum_{j\in E\mu}$$
$$\begin{pmatrix} (\xi_{i}  + \theta ) + & (\xi_{j}' + \theta ) \\  & p_{sf}+ \end{pmatrix}$$
$$= \frac{1}{2} w^{\top}w + \nu \epsilon  + \frac{1}{m} \sum_{i\in E\lambda}  \sum_{j\in E\mu}  - \begin{pmatrix} q_{sf} \\ \nu  - \\ m \end{pmatrix} \theta .$$
$$\begin{pmatrix} \xi_{i}  + & \xi_{j}' \end{pmatrix}$$

<!-- PAGE 2124 -->
Vì $max{2p_{f}/m, 2q_{f}/m} \le \nu$ suy ra rằng $(p_{f} + q_{f})/m \le \nu$ và $p_{sf} \le p_{f}, q_{sf} \le q_{f}$, ta có
$$\nu  - \frac{p_{sf}+ q_{sf}}{m} \ge 0,(*_{2})$$
Và do đó $\omega (\theta$) $\le \omega (0)$. Nếu bất đẳng thức $(*_{2})$ là chặt, thì điều này contradicts tính tối ưu của ban đầu nghiệm. Vì vậy, $\nu  = (p_{sf} + q_{sf})/m, \omega (\theta$) $= \omega (0)$ và $(w, b, \epsilon$ - $\theta , \xi  + \theta , \xi' + \theta$) là nghiệm tối ưu (optimal solution) sao cho hoặc
$$w^{\top}x_{i} + b -y_{i} = \epsilon  -\theta for some i \in /(E_{\lambda} \cup E_{\mu})$$
Hoặc
$$-w^{\top}x_{i} -b + y_{i} = \epsilon  -\theta for some i \in /(E_{\lambda} \cup E_{\mu}).$$
Ta là bây giờ rút gọn đến Trường hợp 1a hoặc hoặc Trường hợp 2a. Trường hợp $2$. Ta có
$$w^{\top}x_{i} + b -y_{i} \le \epsilon i \in /(E_{\lambda} \cup E_{\mu})$$
$$-w^{\top}x_{i} -b + y_{i} < \epsilon i \in /(E_{\lambda} \cup E_{\mu}).$$
Một lần nữa có hai subcases. Trường hợp 2a. Giả sử rằng tồn tại một $i \in / (E_{\lambda} \cup E_{\mu})$ sao cho $w^{\top}x_{i} + b$ - $y_{i} = \epsilon$. Của ta chiến lược là đến giảm $\epsilon$ và giảm $b$ bởi nhỏ lượng $\theta$ trong như vậy cách rằng một số bất đẳng thức $-w^{\top}x_{j}$ - $b + y_{j} < \epsilon$ trở thành phương trình với một số $j \in / (E_{\lambda} \cup E_{\mu})$. Geometrically, điều này tương đương với đến thấp hơn tách siêu phẳng (hyperplane) $H_{w,b}$ và giảm chiều rộng của dải phẳng (slab), giữ xanh lam lề (margin) siêu phẳng (hyperplane) unchanged. Xem Hình 56.10. các bất đẳng thức suy ra rằng
$$-\epsilon  < w^{\top}x_{i} + b -y_{i} \le \epsilon .$$
Cho chúng ta chọn $\theta$ sao cho
$$\theta  = (1/2) \min{\epsilon  -(-w^{\top}x_{i} -b + y_{i}) | i \in /(E_{\lambda} \cup E_{\mu})}.$$
Của ta các giả thiết suy ra rằng $\theta  > 0$, và ta có $\theta  \le \epsilon$, bởi vì $(1/2)(\epsilon -(-w^{\top}x_{i}-b+y_{i})) \le \epsilon$ là tương đương đến $\epsilon$ - $(-w^{\top}x_{i}$ - $b + y_{i}) \le 2\epsilon$ mà là tương đương đến $w^{\top}x_{i} + b$ - $y_{i} \le \epsilon$ mà nghiệm đúng với mọi $i \in / (E_{\lambda} \cup E_{\mu})$ bởi giả thiết. Ta có thể viết
$$w^{\top}x_{i} + b -\theta  -y_{i} = \epsilon  -\theta  + \xi_{i} \xi_{i}  > 0i \in E_{\lambda}$$
$$-w^{\top}x_{j} -(b -\theta ) + y_{j} = \epsilon  -\theta  + \xi_{j}'  + 2\theta \xi_{j}'  > 0j \in E_{\mu}$$
$$w^{\top}x_{i} + b -\theta  -y_{i} \le \epsilon  -\theta i \in /(E_{\lambda} \cup E_{\mu})$$
$$-w^{\top}x_{i} -(b -\theta ) + y_{i} \le \epsilon  -\theta i \in /(E_{\lambda} \cup E_{\mu}).$$

<!-- PAGE 2125 -->
$$\xi ‘no red support vector$$
$$i0$$
$$є =$$
$$b +$$
$$x -z +$$
$$wT$$
$$є$$
$$є$$
$$b = 0$$
$$x -z +$$
$$w T  = 0$$
$$blue support vectorb - є$$
$$x -z +$$
$$wT$$
$$\xi i$$
$$\xi +2 \theta ‘$$
$$i = 0$$
$$(є-\theta )$$
$$\theta ) +$$
$$(b-$$
$$-z +$$
$$є- \theta red support vectorw T x$$
$$)= 0$$
$$b- \theta$$
$$є- \theta z + ($$
$$w T x -0$$
$$- (є-\theta )=$$
$$blue support vectorb- \theta )$$
$$-z + ($$
$$wT  x$$
$$\xi i$$

![Figure 56.10](../../assets/ch56/fig_56_10.png)

**Hình 56.10:** Trong điều này illustration các điểm trong phạm vi $\epsilon$ -tube được ký hiệu bởi mở các đường tròn. Trong ban đầu, trên trái configuration, không có đỏ hỗ trợ/giá (support) vectơ. Bởi thấp hơn hồng tách siêu phẳng (hyperplane) và giảm chiều rộng của dải phẳng (slab), ta kết thúc/cuối lên với đỏ hỗ trợ/giá (support) vectơ. Bởi giả thiết
$$w^{\top}x_{i} + (b -\theta ) -y_{i} = \epsilon  -\theta for some i \in /(E_{\lambda} \cup E_{\mu}),$$
Và bởi lựa chọn của $\theta$,
$$-w^{\top}x_{j} -(b -\theta ) + y_{j} = \epsilon  -\theta for some j \in /(E_{\lambda} \cup E_{\mu}).$$
Mới giá trị của hàm mục tiêu (objective function) là
$$\omega (\theta ) = \frac{1}{2} w^{\top}w + \nu (\epsilon  -\theta ) + \frac{1}{m} \sum_{i\in E\lambda}  \sum_{j\in E\mu}$$
$$\begin{pmatrix} \xi_{i}  + & (\xi_{j}' + 2\theta ) \\  & 2 \end{pmatrix}$$
$$= \frac{1}{2} w^{\top}w + \nu \epsilon  + \frac{1}{m} \sum_{i\in E\lambda}  \sum_{j\in E\mu}  - \begin{pmatrix} q_{sf} \\ \nu  - \\ m \end{pmatrix} \theta .$$
$$\begin{pmatrix} \xi_{i}  + & \xi_{j}' \end{pmatrix}$$
Rest của chứng minh là đồng dạng ngoại trừ rằng $2p_{sf}/m$ được thay thế bởi $2q_{sf}/m$. Nhận thấy rằng exceptional trường hợp trong mà $\theta  = \epsilon$ có thể phát sinh. Trong trường hợp này tất cả các điểm $(x_{i}, y_{i})$ rằng là không các sai số (chặt bên ngoài $\epsilon$ -dải phẳng (slab)) là trên xanh lam lề (margin) siêu phẳng (hyperplane). trường hợp này có thể chỉ phát sinh nếu $\nu  = 2q_{sf}/m$. Trường hợp 2b. Ta có $w^{\top}x_{i} + b$ - $y_{i} < \epsilon$ với mọi $i \in / (E_{\lambda} \cup E_{\mu})$. Vì ta cũng được giả sử rằng $-w^{\top}x_{i} -b+y_{i} < \epsilon$ với mọi $i \in / (E_{\lambda} \cup E_{\mu})$, Trường hợp 2b là đồng nhất đến Trường hợp 1b và ta được thực hiện.

<!-- PAGE 2126 -->
Chứng minh của Mệnh đề 56.4 reveals rằng có ba tới hạn/quan trọng các giá trị cho $\nu$:
$$\frac{2p_{sf}}{m} , \frac{2q_{sf}}{m} , \frac{p_{sf}+ q_{sf}}{m} .$$
Các giá trị này có thể được tránh được bởi đòi hỏi chặt bất đẳng thức
$$ 2$$
$$\max \frac{2p_{sf}}{m} , \frac{q_{sf}}{m} < \nu .$$
Thì sau đây hệ quả nghiệm đúng.

> **Định lý 56.5.** Với mọi nghiệm tối ưu (optimal solution) $(w, b, \epsilon , \xi , \xi'$) với $w \neq  0$ và $\epsilon  > 0$, nếu
$$ 2$$
$$\max \frac{2p_{sf}}{m} , \frac{q_{sf}}{m} < \nu  < (m -1)/m,$$
Thì một số $x_{i0}$ là xanh lam hỗ trợ/giá (support) vectơ và một số $x_{j0}$ là đỏ hỗ trợ/giá (support) vectơ (với $i_{0} \neq  j_{0})$.

*Chứng minh.* Ta tiến hành bởi mâu thuẫn. Giả sử rằng với mọi nghiệm tối ưu (optimal solution) với $w \neq  0$ và $\epsilon  > 0$ không có $x_{i}$ là xanh lam hỗ trợ/giá (support) vectơ hoặc không có $x_{i}$ là đỏ hỗ trợ/giá (support) vectơ. Vì $\nu  < (m$ - $1)/m$, Mệnh đề 56.4 nghiệm đúng, do đó ở đó là một cái khác nghiệm tối ưu (optimal solution). Nhưng vì tới hạn/quan trọng các giá trị của $\nu$ là tránh được, chứng minh của Mệnh đề 56.4 chỉ ra rằng giá trị của hàm mục tiêu (objective function) cho điều này mới nghiệm tối ưu (optimal solution) là chặt nhỏ hơn hơn ban đầu giá trị tối ưu (optimal value), một mâu thuẫn.
Nhận xét: Nếu nghiệm tối ưu (optimal solution) có $\epsilon  = 0$, thì tùy thuộc trên giá trị của $C$ ở đó có thể không là bất kỳ hỗ trợ/giá (support) các vectơ, hoặc nhiều. Nếu gốc (primal) có nghiệm tối ưu (optimal solution) với $w \neq  0$ và $\epsilon  > 0$, thì bởi $(*_{w})$ và vì
$$\sum_{i=1}^{m}  \lambda_{i}  - \sum_{i=1}^{m}  \mu_{i}  = 0and\lambda_{i} \mu_{i}  = 0,$$
Ở đó là $i_{0}$ sao cho $\lambda_{i0}  > 0$ và một số $j_{0} \neq  i_{0}$ sao cho $\mu_{j0}  > 0$. Dưới nhẹ giả thiết được gọi là Tiêu chuẩn Lề (margin) Giả thiết rằng tồn tại một $i_{0}$ sao cho $0 < \alpha_{i0}  <^{C}$ và tồn tại một $j_{0} \neq  i_{0}$ sao cho $0 < \mu_{j0}  <^{C}$, nói cách khác có một xanh lam $support^{m}$ vectơ của loại/kiểu $1$ và có một đỏ hỗ trợ/giá (support) $vector^{m}$ của loại/kiểu $1$, thì bởi (*) ta có $\xi_{i0}  = 0, \xi_{j0}'  = 0$, và ta có hai các phương trình
$$w^{\top}x_{i0} + b -y_{i0} = \epsilon$$
$$-w^{\top}x_{j0} -b + y_{j0} = \epsilon ,$$

<!-- PAGE 2127 -->
Do đó $b$ và $\epsilon$ có thể được được tính. Đặc biệt,
$$b = \frac{1}{2} \begin{pmatrix} y_{i0}+ y_{j0}-w^{\top}(x_{i0}+ x_{j0}) \end{pmatrix}$$
$$\epsilon  = \frac{1}{2} \begin{pmatrix} y_{j0}-y_{i0}+ w^{\top}(x_{i0}-x_{j0}) \end{pmatrix} .$$
Hàm f(x) $= w^{\top}x + b$ (thường được gọi là hồi quy estimate) được cho bởi
$$f(x) = \sum_{i=1}^{m}  (\mu_{i}  -\lambda_{i} )x_{i}^{\top} x + b.$$
Trong thực tế, do số inaccurracy, nó là phức tạp đến viết máy tính bài toán quy hoạch rằng sẽ chọn hai phân biệt các chỉ số như ở trên. Nó được ưu tiên hơn để tính danh sách $I_{\lambda}$ của các chỉ số $i$ sao cho $0 < \lambda_{i}  < C/m$ và danh sách $I_{\mu}$ của các chỉ số $j$ sao cho $0 < \mu_{j}  < C/m$. Thì nó là dễ để xem rằng
$$b = \begin{pmatrix}\end{pmatrix} \sum_{\in I\lambda}  \begin{pmatrix}\end{pmatrix} \sum_{0\in I\mu}  \begin{pmatrix}\end{pmatrix} \begin{pmatrix}\end{pmatrix} \sum_{\in I\lambda}  \begin{pmatrix}\end{pmatrix} \sum_{0\in I\mu}  /2$$
$$\begin{pmatrix}  &  &  &  &  &  &  &  &  \\ y_{i0} & /|I_{\lambda}| + & y_{j0} & /|I_{\mu}| -w^{\top} & x_{i0} & /|I_{\lambda}| + & x_{j0} & /|I_{\mu}| \\ i0 & j & i0 & j \\  &  &  &  &  &  &  &  &  \\ y_{j0} & /|I_{\mu}| - & y_{i0} & /|I_{\lambda}| + w^{\top} & x_{i0} & /|I_{\lambda}| - & x_{j0} & /|I_{\mu}| \\ j & i0 & i0 & j \end{pmatrix}$$
$$\epsilon  = \begin{pmatrix}\end{pmatrix} \sum_{0\in I\mu}  \begin{pmatrix}\end{pmatrix} \sum_{\in I\lambda}  \begin{pmatrix}\end{pmatrix} \begin{pmatrix}\end{pmatrix} \sum_{\in I\lambda}  \begin{pmatrix}\end{pmatrix} \sum_{0\in I\mu}  /2.$$
Các phần tử này các công thức là một cách số nhiều nhiều hơn/thêm stable, nhưng ta vẫn có là cautious đến tập hợp phù hợp tolerance các nhân tử đến decide liệu $\lambda_{i}  > 0$ và $\lambda_{i}  < C/m$ (và tương tự cho $\mu_{i}$). Kết quả sau đây cho đủ các điều kiện cho biểu diễn $\epsilon$ theo đơn lẻ hỗ trợ/giá (support) vectơ.

> **Mệnh đề 56.6.** Với mọi nghiệm tối ưu (optimal solution) $(w, b, \epsilon , \xi , \xi'$) với $w \neq  0$ và $\epsilon  > 0$, nếu
$$ 2$$
$$\max \frac{2p_{sf}}{m} , \frac{q_{sf}}{m} < \nu  < (m -1)/m,$$
Thì $\epsilon$ và $b$ được xác định từ nghiệm $(\lambda , \mu$) của đối ngẫu (dual) theo đơn lẻ hỗ trợ/giá (support) vectơ. Chứng minh phác thảo. Nếu ta biểu diễn rằng khoảng cách đối ngẫu (duality gap) là không ta thu được kết quả sau phương trình biểu diễn $\epsilon$ theo $b$:
$$C \begin{pmatrix} p_{f}+ q_{f} \\ \nu  - \\ m \end{pmatrix} \epsilon  = - \begin{pmatrix} \lambda^{\top} & \mu^{\top} \\  \end{pmatrix} P \begin{pmatrix} \lambda \\ \mu \end{pmatrix} - \begin{pmatrix} y^{\top} & -y^{\top} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$- \frac{C}{m} \begin{pmatrix}  \\ w^{\top} & x_{i} - & x_{j} \end{pmatrix} \begin{pmatrix} - & y_{i} + & y_{j}+ (p_{f}-q_{f})b \end{pmatrix} \sum_{i\in K\lambda}  \sum_{j\in K\mu}  \sum_{i\in K\lambda}  \sum_{j\in K\mu}  .$$
