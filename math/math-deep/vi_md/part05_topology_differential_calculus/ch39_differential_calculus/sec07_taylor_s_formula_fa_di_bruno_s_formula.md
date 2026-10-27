# Taylor's công thức, Faà di Bruno's công thức


<!-- PAGE 1481 -->
Ở đâu $\alpha_{1}  + \alpha_{2}  + \cdots  + \alpha_{n}  = m$. Nếu ta ký hiệu $(\alpha_{1} , \dots  , \alpha_{n}$) đơn giản bởi $\alpha$, thì ta ký hiệu
$$\cdots$$
$$\alpha 1\alpha 2\alpha n$$
$$\begin{pmatrix} \partial \\ \partial x_{1} \end{pmatrix} \begin{pmatrix} \partial \\ \partial x_{2} \end{pmatrix} \begin{pmatrix} \partial \\ \partial x_{n} \end{pmatrix} f$$
Bởi
$$\alpha$$
$$\partial^{\alpha} f,or \begin{pmatrix} \partial \\ \partial x \end{pmatrix} f.$$
Nếu $\alpha  = (\alpha_{1} , \dots  , \alpha_{n}$), ta cho $|\alpha$ | $= \alpha_{1}  + \alpha_{2}  + \cdots  + \alpha_{n} , \alpha$! $= \alpha_{1}$! $\cdots  \alpha_{n}$!, và nếu $h = (h_{1}, \dots  , h_{n})$, ta ký hiệu $h_{1}^{\alpha1} \cdots  h_{n}^{\alpha n}$ bởi $h^{\alpha}$. Trong mục tiếp theo, ta survey khác nhau các phiên bản của Taylor’s công thức.

## 39.7 Taylor’s công thức, Fa` di Bruno’s công thức

Ta thảo luận, mà không có các chứng minh, một vài các phiên bản của Taylor’s công thức. các giả thiết cần thiết trong mỗi phiên bản trở thành một cách tăng mạnh hơn. thứ nhất phiên bản có thể được được quan điểm như tổng quát hóa
$$\longrightarrow \longrightarrow \longrightarrow$$
Của khái niệm của đạo hàm. Cho trước $m$-tuyến tính ánh xạ $f$: $E^{m} \to F$, với mọi vectơ $h \in E$, ta abbreviate
$$f(h, \dots  , h)$$
$$| {z }$$
$$m$$
Bởi $f(h^{m})$. phiên bản của Taylor’s công thức cho trước tiếp theo là đôi khi referred đến như công thức của Taylor–Young.

> **Định lý 39.23.** (Taylor–Young) Cho trước hai được chuẩn (norm) các không gian afin $E$ và $F$, với mọi mở tập con $A \subseteq E$, với mọi hàm $f$: $A \to F$, với mọi $a \in A$, nếu $D^{k}f$ tồn tại trong $A$ với mọi $k, 1 \le k \le m$ - $1$, và nếu $D^{m}f(a)$ tồn tại, thì ta có:
$$f(a + h) = f(a) + \frac{1}{1!} D^{1}f(a)(h) + \cdots  + \frac{1}{m!} D^{m}f(a)(h^{m}) + \|h\|^{m}\epsilon (h),$$
Với mọi $h$ sao cho $a + h \in A$, và ở đâu $lim_{h\to0, h\neq 0} \epsilon (h) = 0$. ở trên phiên bản của Taylor’s công thức có các ứng dụng đến study của tương đối các cực đại (hoặc các cực tiểu) của nhận giá trị thực (real-valued) các hàm. Nó cũng được sử dụng đến study địa phương các tính chất của các đường cong và các mặt. tiếp theo phiên bản của Taylor’s công thức có thể được được quan điểm như tổng quát hóa của Mệnh đề 39.12. Nó đôi khi được gọi là Taylor công thức với Lagrange phần dư hoặc suy rộng/tổng quát hóa có nghĩa giá trị định lý.

<!-- PAGE 1482 -->

> **Định lý 39.24.** (Suy rộng/tổng quát hóa có nghĩa giá trị định lý) Cho $E$ và $F$ là hai được chuẩn (norm) các không gian afin, cho $A$ là mở tập con của $E$, và cho $f$: $A \to F$ là hàm trên $A$. Cho trước bất kỳ
$$\longrightarrow$$
$a \in A$ và bất kỳ $h \neq  0$ trong $E$, nếu đóng đoạn thẳng [, $a + h]$ được chứa trong $A, D^{k}f$ tồn tại trong $A$ với mọi $k, 1 \le k \le m, D^{m+1}f(x)$ tồn tại tại mọi điểm $x$ của mở đoạn thẳng ], $a + h[$, và
$$\max

$D^{m+1}f(x)$

$\le$ M,$$
$$x\in (a,a+h)$$
Với một số $M \ge 0$, thì
$$\|\|^{m+1}$$
$$f(a + h) -f(a) - \begin{pmatrix} 1 & 1 \\ D^{1}f(a)(h) + \cdots  + & D^{m}f(a)(h^{m}) \\ 1! & m! \end{pmatrix} \le M \frac{h}{(m + 1)!} .$$
$$--\longrightarrow \longrightarrow$$
Như hệ quả, nếu $L: E^{m+1} \to F$ là liên tục $(m +$ 1)-ánh xạ tuyến tính (linear map), thì $\| \|^{m+1}$
$$f(a + h) -f(a) - \begin{pmatrix} 1 & 1 & L(h^{m+1}) \\ D^{1}f(a)(h) + \cdots  + & D^{m}f(a)(h^{m}) + \\ 1! & m! & (m + 1)! \end{pmatrix} \le M \frac{h}{(m + 1)!} ,$$
Ở đâu $M = max_{x\in(a,a+h)} \|D^{m+1}f(x)$ - $L\|$. ở trên định lý đôi khi được phát biểu dưới slightly mạnh hơn giả định rằng $f$ là $C^{m}-function$ trên $A$. Nếu $f$: $A \to \mathbb{R}$ là nhận giá trị thực (real-valued) hàm, Định lý 39.24 có thể được refined little bit. Điều này phiên bản là thường được gọi là công thức của Taylor–MacLaurin.

> **Định lý 39.25.** (Taylor–MacLaurin) Cho $E$ được chuẩn (norm) không gian afin (affine space), cho $A$ là mở tập con của $E$, và cho $f$: $A \to \mathbb{R}$ là nhận giá trị thực (real-valued) hàm trên $A$. Cho trước bất kỳ $a \in A$ và bất kỳ
$$\longrightarrow$$
$h \neq  0$ trong $E$, nếu đóng đoạn thẳng [, $a + h]$ được chứa trong $A$, nếu $D^{k}f$ tồn tại trong $A$ với mọi $k, 1 \le k \le m$, và $D^{m+1}f(x)$ tồn tại tại mọi điểm $x$ của mở đoạn thẳng ], $a + h[$, thì tồn tại một $\theta  \in \mathbb{R}$, với $0 < \theta  < 1$, sao cho
$$f(a + h) = f(a) + \frac{1}{1!} D^{1}f(a)(h) + \cdots  + \frac{1}{m!} D^{m}f(a)(h^{m}) + \frac{1}{(m + 1)!} D^{m+1}f(a + \theta h)(h^{m+1}).$$

> **Ví dụ 39.17.** Đi quay lại đến hàm $f$ của Ví dụ 39.14 cho trước bởi f() $=$ log det(), ta biết từ Ví dụ 39.16 rằng
$$D^{m}f(A)(X_{1}, \dots  , X_{m}) = (-1)^{m-1} \sum_{\in Sm-}  \mathrm{tr}(A^{-1}X_{1}A^{-1}X_{\sigma(1)+1} \cdots  A^{-1}X_{\sigma(m-1)+1})(*)$$
$$\sigma 1$$
Với mọi $m \ge 1$, với $A \in GL^{+}(n,\mathbb{R})$. Nếu ta tạo mạnh hơn giả định rằng $A$ là đối xứng xác định dương (SPD), thì với mọi khác đối xứng xác định dương (SPD) ma trận $B$, vì đối xứng xác định dương (SPD) các ma trận tạo thành tập lồi (convex set), các ma trận $A + \theta (B -A) = (1 -\theta )A + \theta B$ là cũng đối xứng xác định dương (SPD) cho $\theta  \in [0, 1]$. Định lý 39.25 áp dụng với $H = B$ - $A$ (ma trận đối xứng (symmetric matrix)), và bằng cách sử dụng (*), ta thu được
$$ -$$
$$+$$
$$\log \det(A + H) = \log \det(A) + trA^{-1}H - \frac{1}{2} (A^{-1}H)^{2} \cdots  + \frac{(1)^{m-1}}{m} (A^{-1}H)^{m}$$
$$-$$
$$+ \frac{(1)^{m}}{m} + 1 ((A + \theta H)^{-1}H)^{m+1},$$

<!-- PAGE 1483 -->
Với một số $\theta$ sao cho $0 < \theta  < 1$. Đặc biệt, nếu $A =$ I, với mọi ma trận đối xứng (symmetric matrix) $H$ sao cho I $+ H$ là đối xứng xác định dương (SPD), ta thu được
$$ -$$
$$+$$
$$\log \det(I + H) = trH - \frac{1}{2} H^{2} \cdots  + \frac{(1)^{m-1}}{m} H^{m}$$
$$+ \frac{(1)^{m}}{m} - + 1 ((I + \theta H)^{-1}H)^{m+1},$$
Với một số $\theta$ sao cho $0 < \theta  < 1$. Trong trường hợp đặc biệt khi $n = 1$, ta có $I = 1, H$ là thực sao cho $1 + H > 0$ và vết (trace) hàm là đồng nhất thức, do đó ta recognize riêng tổng của chuỗi cho $x \mapsto$ log(1 $+ x)$,
$$+ -$$
$$\log(1 + H) = H - \frac{1}{2} H^{2} \cdots  + \frac{(1)^{m-1}}{m} H^{m}$$
$$-$$
$$+ \frac{(1)^{m}}{m} + 1 (1 + \theta H)^{-(m+1)}H^{m+1}.$$
Ta cũng mention cho “toán học culture,” phiên bản với tích phân phần dư, trong trường hợp của nhận giá trị thực (real-valued) hàm. Điều này là thường được gọi là Taylor’s công thức với tích phân phần dư.

> **Định lý 39.26.** (Taylor’s công thức với tích phân phần dư) Cho $E$ được chuẩn (norm) không gian afin (affine space), cho $A$ là mở tập con của $E$, và cho $f$: $A \to \mathbb{R}$ là nhận giá trị thực (real-valued) hàm trên $A$. Cho trước bất kỳ
$$\longrightarrow$$
$a \in A$ và bất kỳ $h \neq  0$ trong $E$, nếu đóng đoạn thẳng [, $a + h]$ được chứa trong $A$, và nếu $f$ là $C^{m+1}-function$ trên $A$, thì ta có
$$f(a + h) = f(a) + \frac{1}{1!} D^{1}f(a)(h) + \cdots  + \frac{1}{m!} D^{m}f(a)(h^{m})$$
$$+ \int_{0}^{}  1 \frac{(1t)^{m}}{m!} -hD^{m+1}f(a + th)(h^{m+1})idt.$$
Advantage của ở trên công thức là rằng nó cho tường minh phần dư. Ta bây giờ examine ngắn gọn tình huống ở đâu $E$ là của hữu hạn số chiều $n$, và $(a_{0}, (e_{1}, \dots  , e_{n}))$ là hệ quy chiếu (frame) cho $E$. Trong trường hợp này, ta thu được nhiều hơn/thêm tường minh biểu thức cho biểu thức
$$\sum_{i=0}^{k=m}  \frac{1}{k!} D^{k}f(a)(h^{k})$$
Liên quan trong tất cả các phiên bản của Taylor’s công thức, ở đâu bởi quy ước, $D^{0}f(a)(h^{0}) =$ f(). Nếu $h = h_{1}e_{1} + \cdots  + h_{n}e_{n}$, thì ta có
$$\cdots$$
$$\sum_{k=0}^{k=m}  \frac{1}{k!} D^{k}f(a)(h^{k}) = \sum_{\cdot \cdot \cdot+kn}  \frac{h_{1}^{k1} h_{n}^{kn}}{k_{1}! \cdots  k_{n}!} \cdots k1knf(a),$$
$$k+\le m \begin{pmatrix} \partial \\ \partial x_{1} \end{pmatrix} \begin{pmatrix} \partial \\ \partial x_{n} \end{pmatrix}$$
$$1$$

<!-- PAGE 1484 -->
Mà, bằng cách sử dụng abbreviated ký hiệu đã giới thiệu tại kết thúc/cuối của Mục 39.6, có thể cũng được viết như
$$\sum_{k=0}^{k=m}  \frac{1}{k!} D^{k}f(a)(h^{k}) = \sum_{|\alpha|\le m}  \frac{h^{\alpha}}{\alpha !} \partial^{\alpha} f(a).$$
Advantange của ở trên ký hiệu là rằng nó là cùng như ký hiệu được sử dụng khi $n = 1$, i.e., khi $E = \mathbb{R}$ (hoặc $E = \mathbb{C})$. Thật vậy, trong trường hợp này, Taylor–MacLaurin công thức reads như:
$$f(a + h) = f(a) + \frac{h}{1!} D^{1}f(a) + \cdots  + \frac{h^{m}}{m} ! D^{m}f(a) + \frac{h^{m+1}}{(m + 1)!} D^{m+1}f(a + \theta h),$$
Với một số $\theta  \in \mathbb{R}$, với $0 < \theta  < 1$, ở đâu $D^{k}f(a)$ là giá trị của đạo hàm thứ $k$ của $f$ tại (và do đó, như ta có đã được nói một vài lần, điều này là thứ $k$-thứ tự vectơ đạo hàm, mà là chỉ vô hướng (scalar), vì $F =\mathbb{R})$. Trong ở trên công thức, các giả định là rằng $f$: [, $a + h] \to \mathbb{R}$ là $C^{m}-function$ trên [, $a + h]$, và rằng $D^{m+1}f(x)$ tồn tại với mọi $x \in$ (, $a + h)$. Taylor’s công thức là hữu ích đến study địa phương các tính chất của các đường cong và các mặt. Trong trường hợp của đường cong, ta xét hàm $f$: $[r, s] \to F$ từ đóng khoảng/đoạn $[r, s]$ của $\mathbb{R}$ đến một số không gian afin (affine space) $F$, các đạo hàm $D^{k}f(a)(h^{k})$ tương ứng với các vectơ $h^{k}D^{k}f(a)$, ở đâu $D^{k}f(a)$ là vectơ thứ $k$ đạo hàm của $f$ tại (mà là một cách thực $D^{k}f(a)(1, \dots  , 1))$, và với mọi $a \in (r, s)$, Định lý 39.23 cho ta sau đây công thức:
$$f(a + h) = f(a) + \frac{h}{1!} D^{1}f(a) + \cdots  + \frac{h^{m}}{m} ! D^{m}f(a) + h^{m}\epsilon (h),$$
Với mọi $h$ sao cho $a + h \in (r, s)$, và ở đâu $lim_{h\to0, h\neq 0} \epsilon (h) = 0$.
$$\mathbb{R}^{n} \mathbb{R}$$
Trong trường hợp của các hàm $f$: $\to$, nó là thuận tiện đến có các công thức cho Taylor– Young công thức và Taylor–MacLaurin công thức theo gradien và Hessian.
$$\mathbb{R}^{n}$$
Nhắc lại rằng gradien $\nabla$ f() của $f$ tại $a \in$ là vectơ cột (column vector)
$$\nabla f(a) = \begin{pmatrix} \partial f \\ (a) \\ \partial x_{1} \\ \partial f \\ (a) \\ \partial x_{2} \\ \vdots \\ \partial f \\ (a) \\ \partial x_{n} \end{pmatrix} ,$$
Và rằng
$$f' (a)(u) = Df(a)(u) = \nabla f(a) \cdot  u,$$
$$\mathbb{R}^{n}$$
Với mọi $u \in$ (ở đâu $\cdot$ có nghĩa là tích vô hướng (inner product)). ở trên phương trình chỉ ra rằng hướng của gradien $\nabla$ f() là hướng của cực đại tăng của hàm $f$ tại và rằng

<!-- PAGE 1485 -->
$\|\nabla f(a)\|$ là tốc độ của thay đổi của $f$ trong của nó hướng của cực đại tăng. Điều này là lý do tại sao các phương pháp của “hạ gradien (gradient descent)” chọn hướng opposite đến gradien (ta là cố gắng để cực tiểu hóa $f)$.
$$\mathbb{R}^{n}$$
Ma trận Hesse (Hessian matrix) $\nabla^{2}$ f() của $f$ tại $a \in$ là $n \times  n$ ma trận đối xứng (symmetric matrix)
$$\nabla^{2} f(a) = \begin{pmatrix} \partial^{2} f & \partial^{2} f & \partial^{2} f \\ (a) & (a) & \dots & (a) \\ \partial x_{1}^{2} & \partial x_{1}\partial x_{2} & \partial x_{1}\partial x_{n} \\ \partial^{2} f & \partial^{2} f & \partial^{2} f \\ (a) & (a) & \dots & (a) \\ \partial x_{1}\partial x_{2} & \partial x_{2}^{2} & \partial x_{2}\partial x_{n} \\ \vdots & \vdots & \ddots & \vdots \\ \partial^{2} f & \partial^{2} f & \partial^{2} f \\ (a) & (a) & \dots & (a) \\ \partial x_{1}\partial x_{n} & \partial x_{2}\partial x_{n} & \partial x_{n}^{2} \end{pmatrix} ,$$
Và ta có
$$D^{2}f(a)(u, v) = u^{\top}\nabla^{2} f(a) v = u \cdot  \nabla^{2} f(a)v = \nabla^{2} f(a)u \cdot  v,$$
Với mọi $u, v \in \mathbb{R}^{n}$. Thì, ta có kết quả sau ba formulations của công thức của Taylor– Young của thứ tự $2$:
$$\epsilon$$
$$f(a + h) = f(a) + Df(a)(h) + \frac{1}{2} D^{2}f(a)(h, h) + \|h\|^{2}(h)$$
$$f(a + h) = f(a) + \nabla f(a) \cdot  h + \frac{1}{2} (h \cdot  \nabla^{2} f(a)h) + (h \cdot  h)\epsilon (h)$$
$$f(a + h) = f(a) + (\nabla f(a))^{\top}h + \frac{1}{2} (h^{\top}\nabla^{2} f(a) h) + (h^{\top}h)\epsilon (h).$$
Với $lim_{h\mapsto0} \epsilon (h) = 0$. Một nên giữ trong mind rằng chỉ thứ nhất công thức là nội tại (i.e., không phụ thuộc vào lựa chọn của cơ sở (basis)), trong khi đó khác hai phụ thuộc vào cơ sở (basis) và tích vô hướng (inner product) được chọn trên $\mathbb{R}^{n}$. Như một bài tập, độc giả nên viết đồng dạng các công thức cho Taylor–MacLaurin công thức của thứ tự $2$. Một cái khác ứng dụng của Taylor’s công thức là derivation của công thức mà cho m- th đạo hàm của hợp thành của hai các hàm, thường đã biết như “Fa` di Bruno’s công thức.” công thức này là hữu ích khi dealing với hình học tính liên tục của splines các đường cong và các mặt.

> **Mệnh đề 39.27.** Cho trước bất kỳ được chuẩn (norm) không gian afin (affine space) $E$, với mọi hàm $f$: $\mathbb{R} \to \mathbb{R}$ và bất kỳ hàm $g: \mathbb{R} \to E$, với mọi $a \in \mathbb{R}$, đặt $b =$ f(), $f^{(i)} (a) = D^{i}f(a)$, và $g^{(i)}(b) = D^{i}g(b)$, với mọi $m \ge 1$, nếu $f^{(i)}$ () và $g^{(i)}(b)$ tồn tại với mọi $i, 1 \le i \le m$, thì $(g\circ f)^{(m)}(a) = D^{m}(g\circ$ f)() tồn tại và được cho bởi sau đây công thức:
$$)^{i1})^{im}$$
$$(g \circ f)^{(m)}(a) = \sum_{0\le j\le m}  \sum_{2+\cdot \cdot \cdot+i}  \frac{m!}{i_{1}! \cdots  i_{m}!} g^{(j)}(b) \begin{pmatrix} f^{(1)}(a \\ 1! \end{pmatrix} \cdots \begin{pmatrix} f^{(m)}(a \\ m! \end{pmatrix} .$$
$$i1+im=j$$
$$i1+2i2+\cdot \cdot \cdot +mim=m$$
$$i1,i2,\cdot \cdot \cdot  ,im\ge 0$$
