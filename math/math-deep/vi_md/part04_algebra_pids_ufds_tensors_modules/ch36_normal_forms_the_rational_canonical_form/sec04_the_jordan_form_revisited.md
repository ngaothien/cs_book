# Dạng Jordan (Jordan form) Revisited


<!-- PAGE 1335 -->
$$\sim \mathbb{R} \sim \mathbb{R} \sim \mathbb{R} -$$
Ở đâu $E_{1} = Z(u_{1}, f) = [X]/(X), E_{2} = Z(u_{2}, f) = [X]/(X), E_{3} = Z(u_{3}, f) = [X]/(X$
$$\sim  \mathbb{R} -$$
$2)$, và $E_{4} = Z(u_{4}, f) = [X]/(X 2)$. các không gian con $E_{1}$ và $E_{2}$ tương ứng với onedimensional các không gian được sinh (spanned) bởi các vectơ riêng (eigenvectors) liên kết với trị riêng (eigenvalue) $0$, trong khi $E_{3}$ và $E_{4}$ tương ứng với một chiều các không gian được sinh (spanned) bởi các vectơ riêng (eigenvectors) liên kết với trị riêng (eigenvalue) $2$. Nếu ta cho $u_{1} = (-1, 0, 0, 1), u_{2} = (0, -1, 1, 0), u_{3} = (1, 0, 0, 1)$ và $u_{4} = (0, 1, 1, 0)$, Định lý 36.15 cho
$$\begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix} ,$$
$$\mathbb{R}^{4}$$
Như dạng chính tắc hữu tỷ (rational canonical form) liên kết với xích (cyclic) phân rã $= E_{1} \oplus E_{2} \oplus E_{3} \oplus E_{4}$. Như ta được điểm trước đó, unlike sự đồng dạng các bất biến, các ước sơ cấp (elementary divisors) có thể thay đổi khi ta đi qua đến trường mở rộng. Ta sẽ bây giờ xét đặc biệt trường hợp ở đâu tất cả bất khả quy (irreducible) các đa thức $p_{i}$ là của tạo thành $X$ - $\lambda_{i}$; rằng là, khi là các trị riêng (eigenvalues) của $f$ thuộc đến $K$. Trong trường hợp này, ta tìm một lần nữa Dạng Jordan (Jordan form).

## 36.4 Dạng Jordan (Jordan form) Revisited

Trong mục này, ta giả sử rằng tất cả các nghiệm của đa thức tối tiểu (minimal polynomial) của $f$ thuộc đến $K$. Điều này sẽ là trường hợp nếu $K$ là algebraically đóng. bất khả quy (irreducible) các đa thức $p_{i}$ của Định lý 36.14 là các đa thức $X$ - $\lambda_{i}$, cho phân biệt các trị riêng (eigenvalues) $\lambda_{i}$ của $f$. Thì, mỗi xích (cyclic) không gian con $Z(u_{j}; f)$ có đa thức tối tiểu (minimal polynomial) của tạo thành $(X$ - $\lambda )^{m}$, với một số trị riêng (eigenvalue) $\lambda$ của $f$ và một số $m \ge 1$. Hóa ra là bằng cách chọn phù hợp cơ sở (basis) cho xích (cyclic) không gian con $Z(u_{j}; f)$, ma trận của thu hẹp của $f$ đến $Z(u_{j}; f)$ là Khối Jordan (Jordan block).

> **Mệnh đề 36.16.** Cho $E$ là hữu hạn chiều vectơ $K$ không gian và cho $f$: $E \to E$ là ánh xạ tuyến tính (linear map). Nếu $E$ là xích (cyclic) K[X]-môđun và nếu $(X$ - $\lambda )^{n}$ là đa thức tối tiểu (minimal polynomial) của $f$, thì có một cơ sở (basis) của $E$ của tạo thành
$$((f -\lambda id)^{n-1}(u), (f -\lambda id)^{n-2}(u), \dots  , (f -\lambda id)(u), u),$$
Với một số $u \in E$. Đối với cơ sở (cơ sở (basis)) này, ma trận của $f$ là Khối Jordan (Jordan block)
$$J_{n}(\lambda ) = \begin{pmatrix} \lambda & 1 & 0 & \cdots & 0 \\ 0 & \lambda & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \ddots & \vdots \\ 0 & 0 & 0 & \ddots & 1 \\ 0 & 0 & 0 & \lambda \end{pmatrix} .$$
$$\cdots$$

<!-- PAGE 1336 -->

*Chứng minh.* Vì $E$ là xích (cyclic) K[X]-môđun, tồn tại một $u \in E$ sao cho $E$ được sinh bởi $u$, f(u), $f^{2} (u), \dots$, mà có nghĩa là mọi vectơ trong $E$ là của tạo thành p(f)(u), với một số đa thức, p(X). Ta khẳng định rằng $u$, f(u), $\dots  , f^{n-2} (u), f^{n-1} (u)$ sinh $E$, mà suy ra rằng số chiều của $E$ là nhiều nhất $n$. Điều này là bởi vì nếu p(X) là bất kỳ đa thức của bậc ít nhất $n$, thì ta có thể chia p(X) bởi $(X$ - $\lambda )^{n}$, thu được
$$p = (X -\lambda )^{n}q + r,$$
Ở đâu $0 \le$ deg(r) $< n$, và như $(X$ - $\lambda )^{n}$ annihilates $E$, ta thu được
$$p(f)(u) = r(f)(u),$$
Mà có nghĩa là mọi vectơ của tạo thành p(f)(u) với p(X) của bậc $\ge n$ là thực sự tổ hợp tuyến tính (linear combination) của $u$, f(u), $\dots  , f^{n-2} (u), f^{n-1} (u)$. Ta khẳng định rằng các vectơ
$$u, (f -\lambda id)(u), \dots  , (f -\lambda id)^{n-2}(u)(f -\lambda id)^{n-1}(u)$$
Là độc lập tuyến tính (linearly independent). Thật vậy, nếu ta đã có không tầm thường tổ hợp tuyến tính (linear combination)
$$a_{0}(f -\lambda id)^{n-1}(u) + a_{1}(f -\lambda id)^{n-2}(u) + \cdots  + a_{n-2}(f -\lambda id)(u) + a_{n-1}u = 0,$$
Thì đa thức
$$a_{0}(X -\lambda )^{n-1}+ a_{1}(X -\lambda )^{n-2}+ \cdots  + a_{n-2}(X -\lambda ) + a_{n-1}$$
Của bậc nhiều nhất $n$ - $1$ sẽ annihilate $E$, contradicting sự kiện rằng $(X$ - $\lambda )^{n}$ là đa thức tối tiểu (minimal polynomial) của $f$ (và do đó, của nhỏ nhất bậc). Hệ quả là, như số chiều của $E$ là nhiều nhất $n$,
$$((f -\lambda id)^{n-1}(u), (f -\lambda id)^{n-2}(u), \dots  , (f -\lambda id)(u), u),$$
Là cơ sở (basis) của $E$ và vì $u$, f(u), $\dots  , f^{n-2} (u), f^{n-1} (u)$ sinh (span) $E$,
$$(u, f(u), \dots  , f^{n-2} (u), f^{n-1} (u))$$
Là cũng cơ sở (basis) của $E$. Cho chúng ta xem cách mà $f$ acts trên cơ sở (basis)
$$((f -\lambda id)^{n-1}(u), (f -\lambda id)^{n-2}(u), \dots  , (f -\lambda id)(u), u).$$
Nếu ta viết $f = f$ - $\lambda$ id $+ \lambda$ id, như $(f$ - $\lambda id)^{n}$ annihilates $E$, ta thu được
$$f((f -\lambda id)^{n-1}(u)) = (f -\lambda id)^{n}(u) + \lambda (f -\lambda id)^{n-1}(u) = \lambda (f -\lambda id)^{n-1}(u)$$
Và
$$f((f -\lambda id)^{k}(u)) = (f -\lambda id)^{k+1}(u) + \lambda (f -\lambda id)^{k}(u),0 \le k \le n -2.$$
Nhưng điều này có nghĩa là một cách chính xác rằng ma trận của $f$ trong cơ sở (cơ sở (basis)) này là Khối Jordan (Jordan block) $J_{n}(\lambda$).

<!-- PAGE 1337 -->
Cơ sở (basis)
$$((f -\lambda id)^{n-1}(u), (f -\lambda id)^{n-2}(u), \dots  , (f -\lambda id)(u), u),$$
Miễn là/được cung cấp theo Mệnh đề 36.16 là đã biết như Jordan dây chuyền/xích. Lưu ý rằng $(f$ - $\lambda id)^{n-1}(u)$ là vectơ riêng (eigenvector) cho $f$. để xây dựng Jordan dây chuyền/xích, ta phải tìm $u$ mà là suy rộng/tổng quát hóa vectơ riêng (eigenvector) của $f$. Điều này được thực hiện bởi thứ nhất việc tìm vectơ riêng (eigenvector) $x_{1}$ của $f$ và một cách đệ quy việc giải
$$\mathbb{R}^{3} \mathbb{R}^{3}$$
Hệ $(f$ - $\lambda id)x_{i+1} = x_{i}$ cho $i \le 1 \le n$ - $1$. Ví dụ giả sử $f$: $\to$ ở đâu f(x, $y, z) = (x + y + z, y + z, z)$. Theo tiêu chuẩn cơ sở (basis), ma trận biểu diễn
$$for f is M = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix} . By using M, it is readily verified that the minimal polynomial$$
$f$ các bằng nhau đa thức đặc trưng (characteristic polynomial), cụ thể là $(X$ - $1)^{3}$. Do đó $f$ có trị riêng (eigenvalue) $\lambda  = 1$ với repeated ba lần. để tìm vectơ riêng (eigenvector) $x_{1}$ liên kết với $\lambda  = 1$, ta giải hệ $(M$ - $I)x_{1} = 0$, hoặc tương đương
$$\begin{pmatrix} 0 & 1 & 1 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} .$$
$$Thus y = z = 0 with x = 1 solves this system to provide the eigenvector x_{1} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} . We$$
Tiếp theo giải hệ $(M$ - $I)x_{2} = x_{1}$, cụ thể là
$$\begin{pmatrix} 0 & 1 & 1 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} ,$$
$$which implies that z = 0 and y = 1. Hence x_{2} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} will work. To finish constructing our$$
Jordan dây chuyền/xích, ta phải giải hệ $(M$ - $I)x_{3} = x_{2}$, cụ thể là
$$\begin{pmatrix} 0 & 1 & 1 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} ,$$
$$from which we see that z = 1, y = 0, and x_{3} = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} . By setting x_{3} = u, we form the basis$$
$$((f -\lambda id)^{2}(u), (f -\lambda id)^{1}(u), \dots  , (f -\lambda id)(u), u) = (x_{1}, x_{2}, x_{3}).$$
