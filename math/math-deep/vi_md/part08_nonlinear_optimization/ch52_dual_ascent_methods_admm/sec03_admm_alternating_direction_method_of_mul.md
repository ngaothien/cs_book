# ADMM: Phương pháp đổi hướng nhân tử (ADMM)


<!-- PAGE 1914 -->
Như một bài tập, độc giả nên kiểm chứng rằng tăng đối ngẫu (dual ascent) (với $\alpha^{k} = \rho$) cho ta các phương trình
$$x^{k+1}= \frac{\lambda^{k}}{2\beta}$$
$$y^{k+1}= - \frac{\lambda^{k}}{\beta}$$
$$\lambda^{k+1} = \begin{pmatrix} 2\rho \\ 1 + \\ \beta \end{pmatrix} \lambda^{k} ,$$
Và do đó phương pháp diverges, ngoại trừ cho $\lambda^{0} = 0$, mà là nghiệm tối ưu (optimal solution). phương pháp của các nhân tử hội tụ dưới các điều kiện rằng là far nhiều hơn/thêm tổng quát hơn tăng đối ngẫu (dual ascent). Tuy nhiên, phép cộng của hình phạt (penalty) số hạng có âm effect rằng chẵn/ngay cả nếu $J$ là khả ly, thì Hàm Lagrange (Lagrangian) $L_{\rho}$ là không khả ly. Do đó cơ bản phương pháp của các nhân tử không thể được sử dụng cho phân rã và là không parallelizable. tiếp theo phương pháp deals với bài toán của separability.

## 52.3 ADMM: Thay phiên Hướng Phương pháp của

$$Multipliers$$
Phương pháp đổi hướng nhân tử (ADMM), cho ngắn ADMM, combines decomposability của tăng đối ngẫu (dual ascent) với superior sự hội tụ các tính chất của phương pháp của các nhân tử. Nó có thể được được quan điểm như xấp xỉ của phương pháp của các nhân tử, nhưng nó là một cách tổng quát superior. ý tưởng là đến split hàm $J$ vào hai độc lập các phần, như J(x, $z) =$ f(x) $+$ g(z), và đến xét Cực tiểu hóa Bài toán $(P_{admm})$,
$$minimizef(x) + g(z)$$
$$subject to Ax + Bz = c,$$
Với một số $p \times  n$ ma trận $A$, một số $p \times  m$ ma trận $B$, và với $x \in \mathbb{R}^{n}, z \in \mathbb{R}^{m}$, và $c \in \mathbb{R}^{p}$. Ta cũng giả sử rằng $f$ và $g$ là lồi. Further các điều kiện sẽ được cộng sau này. Như trong phương pháp của các nhân tử, ta tạo thành augmented Hàm Lagrange (Lagrangian)
$$L_{\rho}(x, z, \lambda ) = f(x) + g(z) + \lambda^{\top} (Ax + Bz -c) + (\rho /2) \|Ax + Bz -c\|_{2}^{2} ,$$
$$\mathbb{R}^{p}$$
Với $\lambda  \in$ và với một số $\rho  > 0$. Cho trước một số ban đầu các giá trị $(z^{0}, \lambda^{0}$), ADMM phương pháp bao gồm của sau đây lặp các bước:
$$x^{k+1}= arg minL_{\rho}(x, z^{k}, \lambda^{k} )$$
$$x$$
$$z^{k+1}= arg minL_{\rho}(x^{k+1}, z, \lambda^{k} )$$
$$z$$
$$\lambda^{k+1} = \lambda^{k} + \rho (Ax^{k+1}+ Bz^{k+1}-c).$$

<!-- PAGE 1915 -->
Thay vì của performing cực tiểu hóa bước jointly trên $x$ và $z$, như phương pháp của các nhân tử sẽ trong bước
$$(x^{k+1}, z^{k+1}) = arg minL_{\rho}(x, z, \lambda^{k} ),$$
$$x,z$$
ADMM thứ nhất performs x-minimization bước, và thì z-minimization bước. Do đó $x$ và $z$ là updated trong thay phiên hoặc sequential cách thức, mà accounts cho số hạng thay phiên hướng. thuật toán phát biểu trong ADMM là $(z^{k}, \lambda^{k}$), trong nghĩa rằng $(z^{k+1}, \lambda^{k+1}$) là hàm của $(z^{k}, \lambda^{k}$). biến $x^{k+1}$ là phụ biến mà được sử dụng để tính $z^{k+1}$ từ $(z^{k}, \lambda^{k}$). các vai trò của $x$ và $z$ là không khá đối xứng, vì update của $x$ được thực hiện trước update của $\lambda$. Bởi switching $x$ và $z, f$ và $g$ và $A$ và $B$, ta thu được biến thể của ADMM trong mà thứ tự của x-update bước và z-update bước là reversed.

> **Ví dụ 52.4.** Cho chúng ta reconsider bài toán của Ví dụ 52.2 để giải nó bằng cách sử dụng ADMM. Ta formulate bài toán như
$$minimize2x + z^{2}$$
$$subject to 2x -z = 0,$$
Với f(x) $=$ 2x và g(z) $= z^{2}$. augmented Hàm Lagrange (Lagrangian) được cho bởi
$$L_{\rho}(x, z, \lambda ) = 2x + z^{2}+ 2\lambda x -\lambda z + 2\rho x^{2}-2\rho xz + \frac{\rho}{2} z^{2}.$$
ADMM các bước là như sau. x-update là
$$x^{k+1}= arg minx \begin{pmatrix} 2\rho x^{2}-2\rho xz^{k}+ 2\lambda^{k} x + 2x \end{pmatrix} ,$$
Và vì điều này là toàn phương hàm trong $x$, của nó cực tiểu là đạt được khi đạo hàm của ở trên hàm (đối với $x)$ là không, cụ thể là
$$- -$$
$$x^{k+1}= \frac{1}{2} z^{k} \frac{1}{2\rho} \lambda^{k} \frac{1}{2\rho} .(1)$$
Z-update là
$$z^{k+1}= arg minz \begin{pmatrix} \rho & - \\ z^{2}+ & z^{2} & 2\rho x^{k+1}z -\lambda^{k} z \\ 2 \end{pmatrix} ,$$
Và như cho x-step, cực tiểu là đạt được khi đạo hàm của ở trên hàm (đối với $z)$ là không, cụ thể là
$$z^{k+1}= \frac{2\rho x^{k+1}}{\rho  + 2} + \frac{\lambda^{k}}{\rho  + 2} .(2)$$
$\lambda$ -update là
$$\lambda^{k+1} = \lambda^{k} + \rho (2x^{k+1}-z^{k+1}).(3)$$

<!-- PAGE 1916 -->
Thế phải hand vế/cạnh của $(1)$ cho $x^{k+1}$ trong $(2)$ cho ta
$$z^{k+1}= \frac{\rho z^{k}}{\rho  + 2} - \frac{1}{\rho  + 2} .(4)$$
Bằng cách sử dụng $(2)$, ta thu được
$$2x^{k+1}-z^{k+1}= \frac{4x^{k+1}}{\rho  + 2} - \frac{\lambda^{k}}{\rho  + 2} ,(5)$$
Và thì bằng cách sử dụng $(3)$ ta thu được
$$\lambda^{k+1} = \frac{2\lambda^{k}}{\rho  + 2} + \frac{4\rho x^{k+1}}{\rho  + 2} .(6)$$
Thế phải hand vế/cạnh của $(1)$ cho $x^{k+1}$ trong $(6)$, ta thu được
$$\lambda^{k+1} = \frac{2\rho z^{k}}{\rho  + 2} - \frac{2}{\rho  + 2} .(7)$$
Phương trình $(7)$ chỉ ra rằng $z^{k}$ xác định $\lambda^{k+1}$, và Phương trình $(1)$ cho $k+2$, dọc theo với Phương trình $(4)$, chỉ ra rằng $z^{k}$ cũng xác định $x^{k+2}$. Đặc biệt, ta tìm rằng
$$- -$$
$$x^{k+2}= \frac{1}{2} z^{k+1} \frac{1}{2\rho} \lambda^{k+1} \frac{1}{2\rho}$$
$$-$$
$$= \frac{(\rho 2)z^{k}}{2(\rho  + 2)} - \frac{1}{\rho  + 2} .$$
Do đó là suffices để tìm giới hạn của dãy $(z^{k})$. Vì ta đã biết từ Ví dụ 52.2 rằng điều này giới hạn là $-1/2$, bằng cách sử dụng $(4)$, ta viết
$$z^{k+1}= - \frac{1}{2} + \frac{\rho z^{k}}{\rho  + 2} - \frac{1}{\rho  + 2} + \frac{1}{2} = - \frac{1}{2} + \frac{\rho}{\rho  + 2} \begin{pmatrix} 1 \\ + z^{k} \\ 2 \end{pmatrix} .$$
Bởi quy nạp, ta suy ra rằng
$$k+1$$
$$z^{k+1}= - \frac{1}{2} + \begin{pmatrix} \rho \\ \rho  + 2 \end{pmatrix} \begin{pmatrix} 1 \\ + z^{0} \\ 2 \end{pmatrix} ,$$
Và vì $\rho  > 0$, ta có $\rho /(\rho  + 2) < 1$, do đó giới hạn của dãy $(z^{k+1})$ là thật vậy $-1/2$, và hệ quả là giới hạn của $(\lambda^{k+1}$) là $-1$ và giới hạn của $x^{k+2}$ là $-1/4$. Cho ADMM là thực tế, x-minimization bước và z-minimization bước có là doable efficiently. Nó là thường thuận tiện đến viết ADMM updates theo scaled đối ngẫu (dual) biến $\mu  = (1/\rho )\lambda$. Nếu ta định nghĩa phần dư (residual) như
$$r = Ax + bz -c,$$
