# Hai chiều Bài toán: Elastic Membrane


<!-- PAGE 702 -->
$$y$$
$$w_{i}^{0}$$
$$w_{0}^{1}w_{j}^{1}w_{N+1}^{1}$$
$$x$$
$$0ihjh1$$
$$Figure 19.4: The basis functions w_{i}^{0} and w_{j}^{1}$$

## 19.2 Hai chiều Bài toán: Elastic

$$Membrane$$
Xét elastic membrane attached đến round contour có phép chiếu trên $(x_{1}, x_{2})-$ mặt phẳng là biên (boundary) $\Gamma$ của mở, liên thông, bị chặn miền $\Omega$ trong $(x_{1}, x_{2})-plane$, như được minh họa trong Hình 19.5. Nói cách khác, ta quan điểm membrane như mặt bao gồm của tập hợp của các điểm $(x, z)$ cho trước bởi phương trình của tạo thành
$$z = u(x),$$
Với $x = (x_{1}, x_{2}) \in \overline{\Omega$,} ở đâu $u: \overline{\Omega} \to \mathbb{R}$ là một số một cách đủ chính quy hàm, và ta nghĩ của u(x) như đứng displacement của điều này membrane. Ta giả sử rằng điều này membrane là dưới action của đứng buộc $\tau$ f(x)dx trên mỗi mặt phần tử trong ngang mặt phẳng (ở đâu $\tau$ là tension của membrane). bài toán là

<!-- PAGE 703 -->
$$\tau f(x)dx$$
$$g(y)$$
$$u(x)$$
$$x_{2}$$
$$\Omega$$
$$dxx$$
$$y$$
$$x_{1}\Gamma$$
$$Figure 19.5: An elastic membrane$$
Để tìm đứng displacement $u$ như hàm của $x$, cho $x \in \overline{\Omega$.} Nó có thể được được hiển thị (dưới một số các giả định trên $\Omega , \Gamma$, và $f)$, rằng u(x) được cho bởi PDE với biên (boundary) điều kiện, của tạo thành
$$-\Delta u(x) = f(x),x \in \Omega$$
$$u(x) = g(x),x \in \Gamma ,$$
$$where g: \Gamma  \to \mathbb{R} represents \frac{the}{(\Omega ).} height of the contour of the membrane. We are looking for$$
Hàm $u$ trong $C^{2}(\Omega$) $\cap C^{1}$ toán tử $\Delta$ là Laplacian, và nó được cho bởi
$$\Delta u(x) = \frac{\partial^{2} u}{\partial x_{1}^{2}} (x) + \frac{\partial^{2} u}{\partial x_{2}^{2}} (x).$$
Điều này là ví dụ của biên (boundary) bài toán, vì nghiệm $u$ của PDE phải thỏa mãn điều kiện u(x) $=$ g(x) trên biên (boundary) của miền xác định $\Omega$. ở trên phương trình là đã biết như Poisson’s phương trình, và khi $f = 0$ như Laplace’s phương trình. Nó có thể được được chứng minh rằng nếu dữ liệu $f, g$ và $\Gamma$ là một cách đủ trơn (smooth), thì bài toán có duy nhất nghiệm. để thu được yếu formulation của bài toán, thứ nhất ta có để tạo biên (boundary) điều kiện thuần nhất, mà có nghĩa là g(x) $= 0$ trên $\Gamma$. Hóa ra là $g$ có thể được được mở rộng đến toàn bộ của $\overline{\Omega as}$ một số một cách đủ trơn (smooth) hàm $h$, do đó ta có thể nhìn cho nghiệm của tạo thành
$$b$$
$u$ - $h$, nhưng để đơn giản, ta giả sử rằng contour của $\Omega$ lies trong mặt phẳng song song đến $b (x_{1}, x_{2})-$ mặt phẳng, sao cho $g = 0$. Ta cho $V$ là không gian con của $C^{2}(\Omega$) $\cap C^{1}\overline{(\Omega$)} bao gồm của các hàm $v$ sao cho $v = 0$ trên $\Gamma$.

<!-- PAGE 704 -->
Như trước, ta nhân PDE bởi test hàm $v \in V$, thu được
$$-\Delta u(x)v(x) = f(x)v(x),$$
Và ta “integrate bởi các phần.” Trong trường hợp này, điều này có nghĩa là ta sử dụng phiên bản của Stokes công thức đã biết như Xanh lục’s thứ nhất đồng nhất thức, mà nói rằng rằng
$$\int_{\Omega}  -\Delta u v dx = \int_{\Omega}  (grad u) \cdot  (grad v) dx - \int_{\Gamma}  (grad u) \cdot  n vd\sigma$$
(ở đâu $n$ ký hiệu outward điểm unit chuẩn tắc/bình thường đến mặt). Bởi vì $v = 0$ trên $\Gamma$,
$$integral \int_{\Gamma}  drops out, and we get an equation of the form$$
$$a(u, v) =f(v)for all v \in V,$$
$$e$$
Ở đâu là dạng song tuyến tính (bilinear form) cho trước bởi
$$a(u, v) = \int_{\Omega}  \begin{pmatrix} \partial u \\ \partial v & \partial u\partial v \\ + \\ \partial x_{1}\partial x_{1} & \partial x_{2}\partial x_{2} \end{pmatrix} dx$$
Và $f$ là dạng tuyến tính (linear form) cho trước bởi
$$e \int_{\Omega}$$
$$f(v) =fvdx.$$
$$e$$
Ta thu được cùng phương trình như trong mục 19.2, nhưng trên tập hợp của các hàm được định nghĩa trên hai chiều miền xác định. Như trước, ta có thể chọn hữu hạn chiều không gian con $V_{a}$ của $V$ và xét rời rạc bài toán đối với $V_{a}$. Một lần nữa, nếu ta chọn cơ sở (basis) $(w_{1}, \dots  , w_{n})$ của $V_{a}$, vectơ $u = u_{1}w_{1} + \cdots  + u_{n}w_{n}$ là nghiệm của Yếu Formulation của bài toán của chúng ta khi và chỉ khi $u = (u_{1}, \dots  , u_{n})$ là nghiệm của hệ phương trình tuyến tính
$$Au = b,$$
Với $A = (a(w_{i}, w_{j}))$ và $b = (f(w_{j}))$. Tuy nhiên, các tích phân rằng cho các phần tử (entries) trong $A$ và
$$e$$
$b$ là nhiều nhiều hơn/thêm phức tạp. cách tiếp cận đến deal với bài toán này là phương pháp của hữu hạn các phần tử. ý tưởng là đến cũng discretize biên (boundary) đường cong $\Gamma$. Nếu ta giả sử rằng $\Gamma$ là polygonal đường thẳng, thì ta có thể triangulate miền xác định $\Omega$, và thì ta xét các không gian của các hàm mà là từng khúc được định nghĩa trên các tam giác của tam giác phân của $\Omega$. đơn giản nhất các hàm là từng khúc afin và nhìn like tents erected ở trên các nhóm của các tam giác. Một lần nữa, ta có thể định nghĩa base các hàm với nhỏ hỗ trợ/giá (support), sao cho ma trận $A$ là ba đường chéo bởi các khối. hữu hạn phần tử phương pháp là vast subject và nó được trình bày trong nhiều các cuốn sách của khác nhau các bậc của difficulty và obscurity. Cho chúng ta đơn giản phát biểu ba quan trọng requirements của hữu hạn phần tử phương pháp:
