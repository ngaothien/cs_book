# Các bài tập


<!-- PAGE 621 -->
$\bullet$ (thực) không gian vectơ (vector space) $\mathfrak{su}(2)$ của $2 \times  2$ Các ma trận Hermite với không vết (trace). $\bullet$ đồng cấu nhóm (group homomorphism) $r$: SU(2) $\to$ Do đó(3); Ker $(r) = {+I, -I}. \bullet$ ma trận biểu diễn $R_{q}$ của phép quay $r_{q}$ được cảm sinh bởi quaternion đơn vị (unit quaternion) $q. \bullet$ Tính toàn ánh của đồng cấu $r$: SU(2) $\to$ Do đó(3). $\bullet$ hàm mũ ánh xạ exp: $\mathfrak{su}(2) \to$ SU(2). $\bullet$ Tính toàn ánh của hàm mũ ánh xạ exp: $\mathfrak{su}(2) \to$ SU(2). $\bullet$ Việc tìm lôgarit của quaternion. $\bullet$ Quaternion nội suy. $\bullet$ Shoemake’s slerp nội suy công thức. $\bullet$ Các mục $s$: Do đó(3) $\to$ SU(2) của $r$: SU(2) $\to$ Do đó(3).

## 16.9 Các bài tập

Bài toán 16.1. Kiểm chứng quaternion các đồng nhất thức
$$i^{2}= j^{2}= k^{2}= ijk = -1,$$
$$ij = -ji = k,$$
$$jk = -kj = i,$$
$$ki = -ik = j.$$
Bài toán 16.2. Kiểm tra rằng với mọi quaternion $X =$ a1 $+$ bi $+$ cj $+$ dk, ta có
$$XX^{*}= X^{*}X = (a^{2}+ b^{2}+ c^{2}+ d^{2})1.$$
Kết luận rằng nếu $X \neq  0$, thì $X$ là khả nghịch và nghịch đảo của nó được cho bởi
$$X^{-1}= (a^{2}+ b^{2}+ c^{2}+ d^{2})^{-1}X^{*}.$$
Bài toán 16.3. Cho trước bất kỳ hai các quaternion $X = a1+bi+cj+dk$ và $Y = a'1+b'i+c'j+d'k$, chứng minh rằng
$$XY = (aa'-bb'-cc'-dd')1 + (ab'+ ba'+ cd'-dc')i$$
$$+ (ac'+ ca'+ db'-bd')j + (ad'+ da'+ bc'-cb')k.$$
Cũng chứng minh rằng nếu $X = [a, U]$ và $Y =$ [', U' ], quaternion tích $XY$ có thể được biểu diễn dưới dạng
$$XY = [aa'-U \cdot  U', aU'+ a'U + U \times  U'].$$

<!-- PAGE 622 -->
Bài toán 16.4. Cho Ad: SU(2) $\to GL(\mathfrak{su}(2))$ là ánh xạ được định nghĩa sao cho với mọi $q \in$ SU(2),
$$Ad_{q}(A) = qAq^{*},A \in \mathfrak{su}(2),$$
Ở đâu $q^{*}$ là nghịch đảo của $q$ (vì SU(2) là unita nhóm) Chứng minh rằng ánh xạ $Ad_{q}$ là khả nghịch ánh xạ tuyến tính (linear map) từ $\mathfrak{su}(2)$ đến chính nó và rằng Ad là đồng cấu nhóm (group homomorphism).
Bài toán 16.5. Chứng minh rằng mọi Ma trận Hermite (Hermitian matrix) với không vết (trace) là của tạo thành $x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1}$, với
$$\sigma_{1}  = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} ,\sigma_{2}  = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} ,\sigma_{3}  = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} .$$
Kiểm tra rằng $i = i\sigma_{3} , j = i\sigma_{2}$, và rằng $k = i\sigma_{1}$.
Bài toán 16.6. Nếu
$$B = \begin{pmatrix} 0 & -u_{3} & u_{2} \\ u_{3} & 0 & -u_{1} \\ u_{2} & u_{1} & 0 \end{pmatrix} ,$$
$$-$$
Và nếu ta viết $\theta  = p\overline{u}_{1}^{2} \overline{+}\overline{u}_{2}^{2} \overline{+}\overline{u}_{3}^{2}$ (với $0 \le \theta  \le \pi$), thì Rodrigues công thức nói rằng rằng
$$-$$
$$e^{B}= I + \frac{\sin \theta}{\theta} B + \frac{(1cos \theta )}{\theta^{2}} B^{2},\theta  \neq  0,$$
Với $e^{0} =$ I. Kiểm tra rằng $tr(e^{B}) = 1 + 2$ cos $\theta$. Chứng minh rằng quaternion $q$ tương ứng với phép quay $R = e^{B}$ (với $B \neq  0)$ được cho bởi
$$$$
$$q =\cos \begin{pmatrix} \theta \\ 2 \end{pmatrix} , \sin \begin{pmatrix} \theta \\ 2 \end{pmatrix} \begin{pmatrix} u_{1}, u_{2}, u_{3} \\ \theta & \overline{\theta} & \overline{\theta} \end{pmatrix} .$$
Bài toán 16.7. Với mọi ma trận $A \in \mathfrak{su}(2)$, với
$$A = \begin{pmatrix} iu_{1} & u_{2} + iu_{3} \\ -u_{2} + iu_{3} & -iu_{1} \end{pmatrix} ,$$
Chứng minh rằng nếu ta viết $\theta  = p\overline{u}_{1}^{2} \overline{+}\overline{u}_{2}^{2} \overline{+}\overline{u}_{3}^{2}$, thì
$$e^{A}= \cos \theta I + \frac{\sin \theta}{\theta} A,\theta  \neq  0,$$
Và $e^{0} =$ I. Kết luận rằng $e^{A}$ là quaternion đơn vị (unit quaternion) biểu diễn phép quay của góc $2\theta$ và trục $(u_{1}, u_{2}, u_{3})$ (hoặc I khi $\theta  = k\pi , k \in \mathbb{Z})$.
Bài toán 16.8. Viết Matlab bài toán quy hoạch cài đặt phương pháp của Mục 16.4 cho việc tìm quaternion đơn vị (unit quaternion) tương ứng với ma trận quay (rotation matrix).
Bài toán 16.9. Chỉ ra rằng có một rất đơn giản phương pháp cho producing trực chuẩn
$$\mathbb{R}^{4}$$
Hệ quy chiếu (frame) trong có vectơ thứ nhất là bất kỳ cho trước khác không vectơ (, $b, c, d)$.

<!-- PAGE 623 -->
Bài toán 16.10. Cho $i, j$, và $k$, là unit các vectơ của các tọa độ $(1, 0, 0), (0, 1, 0)$, và $(0, 0, 1)$ trong $\mathbb{R}^{3}$.
$(1)$ Mô tả geometrically các phép quay được định nghĩa bởi sau đây các quaternion:
$$p = (0, i),q = (0, j).$$
Chứng minh rằng interpolant $Z(\lambda$) $= p(p^{-1}q)^{\lambda}$ được cho bởi
$$Z(\lambda ) = (0, \cos(\lambda \pi /2)i + \sin(\lambda \pi /2)j) .$$
Mô tả geometrically những gì điều này phép quay là.
$(2)$ Repeat Câu hỏi $(1)$ với các phép quay được định nghĩa bởi các quaternion
$$p = \frac{1}{2} , \frac{\sqrt{3}}{2} i!,q = (0, j).$$
Chứng minh rằng interpolant $Z(\lambda$) được cho bởi
$$!$$
$$1$$
$$Z(\lambda ) =2 \cos(\lambda \pi /2), \frac{\sqrt{3}}{2} \cos(\lambda \pi /2)i + \sin(\lambda \pi /2)j.$$
Mô tả geometrically những gì điều này phép quay là.
$(3)$ Repeat Câu hỏi $(1)$ với các phép quay được định nghĩa bởi các quaternion
$$p = \begin{pmatrix} 1 & 1 \\ \sqrt,\sqrt i \\ \overline{2} & \overline{2} \end{pmatrix} ,q = \begin{pmatrix} 1 \\ 0,\sqrt(i + j) \\ \overline{2} \end{pmatrix} .$$
Chứng minh rằng interpolant $Z(\lambda$) được cho bởi
$$11$$
$Z(\lambda$) $= \sqrt2 cos(\lambda \pi /3)$ - $\sqrt6 sin(\lambda \pi /3)$,
$$\sqrt\sqrt 2$$
$$(1/\overline{2 \cos(}\lambda \pi /3) + 1/\overline{6 \sin(}\lambda \pi /3))i +\sqrt6 \sin(\lambda \pi /3)j.$$
Bài toán 16.11. Chứng minh rằng
$$w \times  (u \times  v) = (w \cdot  v)u -(u \cdot  w)v.$$
Kết luận rằng
$$u \times  (u \times  v) = (u \cdot  v)u -(u \cdot  u)v.$$

<!-- PAGE 624 -->
