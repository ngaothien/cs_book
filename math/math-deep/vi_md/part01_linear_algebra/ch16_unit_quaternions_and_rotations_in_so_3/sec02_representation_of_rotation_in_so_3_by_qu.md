# Biểu diễn của Phép quay trong Do đó(3) Bởi Các quaternion trong SU(2)


<!-- PAGE 603 -->
Cũng nhận thấy rằng
$$X^{*}= \begin{pmatrix} a -ib & -(c + id) \\ c -id & a + ib \end{pmatrix} = a1 -bi -cj -dk.$$
Điều này suy ra rằng nếu $X \neq  0$, thì $X$ là khả nghịch và nghịch đảo của nó được cho bởi
$$X^{-1}= (a^{2}+ b^{2}+ c^{2}+ d^{2})^{-1}X^{*}.$$
Hệ quả là, nó có thể được được kiểm chứng rằng $\mathbb{H}$ là skew trường (không giao hoán trường). Nó là cũng thực không gian vectơ (vector space) có số chiều $4$ với cơ sở (basis) $(1, i, j, k)$; do đó như không gian vectơ (vector space), $\mathbb{H}$ là đẳng cấu đến $\mathbb{R}^{4}$.

> **Định nghĩa 16.2.** concise ký hiệu cho quaternion $X$ được định nghĩa bởi $\alpha  = a +$ ib và $\beta  = c +$ id là
$$X = [a, (b, c, d)].$$
$$We call a the scalar part of X and (b, c, d) \frac{the}{X.} vector part of \frac{X.}{X} With this notation,$$
$X^{*} = [a$, -(b, $c, d)]$, mà là thường được ký hiệu bởi quaternion được gọi là liên hợp của $X$. Nếu $q$ là quaternion đơn vị (unit quaternion), thì $\overline{q}$ là multiplicative nghịch đảo của $q$.

## 16.2 Biểu diễn của Các phép quay trong Do đó(3) bởi Quater-

$$nions in SU(2)$$
Then chốt đến biểu diễn của các phép quay trong Do đó(3) bởi các quaternion đơn vị là nhất định đồng cấu nhóm (group homomorphism) được gọi là liên hợp (adjoint) biểu diễn của SU(2). để định nghĩa điều này ánh xạ, thứ nhất ta định nghĩa thực không gian vectơ (vector space) $\mathfrak{su}(2)$ của skew Các ma trận Hermite.

> **Định nghĩa 16.3.** (thực) không gian vectơ (vector space) $\mathfrak{su}(2)$ của $2 \times  2$ skew Các ma trận Hermite với không vết (trace) được cho bởi
$$$$
$$\mathfrak{su}(2) = \begin{pmatrix} ix & y + iz \\ -y + iz & -ix \end{pmatrix} (x, y, z) \in \mathbb{R}^{3}.$$
Nhận thấy rằng với mọi ma trận $A \in \mathfrak{su}(2)$, ta có $A^{*} = -A$, nghĩa là, $A$ là skew Hermite, và rằng tr() $= 0$.

> **Định nghĩa 16.4.** liên hợp (adjoint) biểu diễn của nhóm SU(2) là đồng cấu nhóm (group homomorphism) Ad: SU(2) $\to GL(\mathfrak{su}(2))$ được định nghĩa sao cho với mọi $q \in$ SU(2), với
$$q = \begin{pmatrix} \alpha & \beta \\ -\beta & \overline{\alpha} \end{pmatrix} \in SU(2),$$
Ta có
$$Ad_{q}(A) = qAq^{*},A \in \mathfrak{su}(2),$$
Ở đâu $q^{*}$ là nghịch đảo của $q$ (vì SU(2) là unita nhóm) và được cho bởi
$$q^{*}= \begin{pmatrix} \overline{\alpha} & -\beta \\ \beta & \alpha \end{pmatrix} .$$

<!-- PAGE 604 -->
Một cần để kiểm chứng rằng ánh xạ $Ad_{q}$ là khả nghịch ánh xạ tuyến tính (linear map) $from\mathfrak{su}(2)$ đến chính nó, và rằng Ad là đồng cấu nhóm (group homomorphism), mà là dễ đến thực hiện.
$$\mathbb{R}^{3}  \mathbb{H}$$
Trong thứ tự đến associate phép quay $\rho_{q}$ (trong Do đó(3)) đến $q$, ta cần đến embed vào như thuần túy các quaternion, bởi
$$\psi (x, y, z) = \begin{pmatrix} ix & y + iz \\ -y + iz & -ix \end{pmatrix} ,(x, y, z) \in \mathbb{R}^{3}.$$
Thì $q$ định nghĩa ánh xạ $\rho_{q}$ (trên $\mathbb{R}^{3})$ cho trước bởi
$$\rho_{q} (x, y, z) = \psi^{-1} (q\psi (x, y, z)q^{*}).$$
Vì vậy, modulo đẳng cấu $\psi$, ánh xạ tuyến tính (linear map) $\rho_{q}$ là tuyến tính đẳng cấu $Ad_{q}$. Thực ra, hóa ra là $\rho_{q}$ là phép quay (và do đó là $Ad_{q})$, mà ta sẽ chứng minh một cách ngắn. Do đó, biểu diễn của các phép quay trong Do đó(3) bởi các quaternion đơn vị là chỉ liên hợp (adjoint) biểu diễn của SU(2); ảnh (ảnh (image)) của nó là nhóm con của $GL(\mathfrak{su}(2))$ đẳng cấu đến Do đó(3).
$$\mathbb{R}^{3}$$
Technically, nó là bit đơn giản hơn đến embed trong (thực) các không gian vectơ của Các ma trận Hermite với không vết (trace),
$$$$
$$\begin{pmatrix} x & z -iy \\ z + iy & -x \end{pmatrix} x, y, z \in \mathbb{R}.$$
Vì ma trận $\psi (x, y, z)$ là skew-Hermitian, ma trận $-i\psi (x, y, z)$ là Hermite, và ta có
$$-i\psi (x, y, z) = \begin{pmatrix} x & z -iy \\ z + iy & -x \end{pmatrix} = x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1} ,$$
Ở đâu $\sigma_{1} , \sigma_{2} , \sigma_{3}$ là Pauli spin các ma trận
$$\sigma_{1}  = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} ,\sigma_{2}  = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} ,\sigma_{3}  = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} .$$
Các ma trận của tạo thành $x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1}$ là Các ma trận Hermite với không vết (trace). Nó là dễ để xem rằng mọi $2 \times  2$ Ma trận Hermite (Hermitian matrix) với không vết (trace) phải là của tạo thành này. (nhận thấy rằng $(i\sigma_{1} , i\sigma_{2} , i\sigma_{3}$) các dạng cơ sở (basis) của $\mathfrak{su}(2)$. Cũng, $i = i\sigma_{3} , j = i\sigma_{2} , k = i\sigma_{1}$.) Bây giờ, nếu $A = x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1}$ là Hermite $2 \times  2$ ma trận với không vết (trace), ta có
$$(qAq^{*})^{*}= qA^{*}q^{*}= qAq^{*},$$
Do đó $qAq^{*}$ là cũng Hermite, và
$$\mathrm{tr}(qAq^{*}) = \mathrm{tr}(Aq^{*}q) = \mathrm{tr}(A),$$
Và $qAq^{*}$ cũng có không vết (trace). Vì vậy, ánh xạ $A \mapsto qAq^{*}$ bảo toàn Các ma trận Hermite với không vết (trace). Ta cũng có
$$\det(x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1} ) = \det \begin{pmatrix} x & z -iy \\ z + iy & -x \end{pmatrix} = -(x^{2}+ y^{2}+ z^{2}),$$

<!-- PAGE 605 -->
Và
$$\det(qAq^{*}) = \det(q) \det(A) \det(q^{*}) = \det(A) = -(x^{2}+ y^{2}+ z^{2}).$$
$$\mathbb{R}^{3}$$
Ta có thể embed vào không gian của Các ma trận Hermite với không vết (trace) bởi
$$\phi (x, y, z) = x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1} .$$
Lưu ý rằng
$$\phi  = -i\psi and\phi^{-1} = i\psi^{-1} .$$
$$\mathbb{R}^{3}$$

> **Định nghĩa 16.5.** quaternion đơn vị (unit quaternion) $q \in$ SU(2) cảm sinh ánh xạ $r_{q}$ trên bởi
$$r_{q}(x, y, z) = \phi^{-1} (q\phi (x, y, z)q^{*}) = \phi^{-1} (q(x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1} )q^{*}).$$
Ánh xạ $r_{q}$ là rõ ràng tuyến tính vì $\phi$ là tuyến tính.

> **Mệnh đề 16.1.** Với mọi quaternion đơn vị (unit quaternion) $q \in$ SU(2), ánh xạ tuyến tính (linear map) $r_{q}$ là trực giao, nghĩa là, $r_{q} \in$ O(3).

*Chứng minh.* Vì
$$-\|(x, y, z)\|^{2}= -(x^{2}+ y^{2}+ z^{2}) = \det(x\sigma^{3} + y\sigma^{2} + z\sigma_{1} ) = \det(\phi (x, y, z)),$$
Ta có
$$-\|r_{q}(x, y, z)\|^{2}= \det(\phi (r_{q}(x, y, z))) = \det(q(x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1} )q^{*})$$
$$= \det(x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1} ) = -

$(x, y, z)^{2}$

,$$ and we deduce that $r_{q}$ is an isometry. Thus, $r_{q} \in$ O(3). In fact, $r_{q}$ is a rotation, and we can show this by finding the fixed points of $r_{q}$. Let $q$ là quaternion đơn vị (unit quaternion) của tạo thành
$$q = \begin{pmatrix} \alpha & \beta \\ -\beta & \overline{\alpha} \end{pmatrix}$$
$$\mathbb{R}$$
Với $\alpha  = a +$ ib, $\beta  = c +$ id, và $a^{2} + b^{2} + c^{2} + d^{2} = 1$ (, $b, c, d \in$). Nếu $b = c = d = 0$, thì $q =$ I và $r_{q}$ là đồng nhất thức do đó ta có thể giả sử rằng $(b, c, d) \neq (0, 0, 0)$.

> **Mệnh đề 16.2.** Nếu $(b, c, d) \neq  (0, 0, 0)$, thì cố định các điểm của $r_{q}$ là các nghiệm $(x, y, z)$ của hệ phương trình tuyến tính
$$-dy + cz = 0$$
$$cx -by = 0$$
$$dx -bz = 0.$$
Điều này hệ phương trình tuyến tính có không tầm thường nghiệm $(b, c, d)$ và có hạng (rank) $2$. Vì vậy, $r_{q}$ có trị riêng (eigenvalue) $1$ với bội (multiplicity) $1$, và $r_{q}$ là phép quay có trục được xác định bởi $(b, c, d)$.

<!-- PAGE 606 -->

*Chứng minh.* Ta có $r_{q}(x, y, z) = (x, y, z)$ khi và chỉ khi
$$\phi^{-1} (q(x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1} )q^{*}) = (x, y, z)$$
Khi và chỉ khi
$$q(x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1} )q^{*}= \phi (x, y, z),$$
Và vì
$$\phi (x, y, z) = x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1}  = A$$
Với
$$A = \begin{pmatrix} x & z -iy \\ z + iy & -x \end{pmatrix} ,$$
Ta xem rằng $r_{q}(x, y, z) = (x, y, z)$ khi và chỉ khi
$$qAq^{*}= AiffqA = Aq.$$
Ta có
$$qA = \begin{pmatrix} \alpha & \beta \\ -\beta & \overline{\alpha} \end{pmatrix} \begin{pmatrix} x & z -iy \\ z + iy & -x \end{pmatrix} = \begin{pmatrix} \alpha x + \beta z + i\beta y & \alpha z -i\alpha y -\beta x \\ -\beta x +\overline{\alpha z} +\overline{i\alpha y} & -\beta z + i\beta y -\overline{\alpha x} \end{pmatrix}$$
Và
$$Aq = \begin{pmatrix} x & z -iy \\ z + iy & -x \end{pmatrix} \begin{pmatrix} \alpha & \beta \\ -\beta & \overline{\alpha} \end{pmatrix} = \begin{pmatrix} \alpha x -\overline{\beta z} +\overline{i\beta y} & \beta x +\overline{\alpha z} -\overline{i\alpha y} \\ \alpha z + i\alpha y + \beta x & \beta z + i\beta y -\overline{\alpha x} \end{pmatrix} .$$
Bởi equating qA và Aq, ta thu được
$$i(\beta  -\overline{\beta})y + (\beta  +\overline{\beta})z = 0$$
$$2\beta x + i(\alpha  -\overline{\alpha})y + (\overline{\alpha} -\alpha )z = 0$$
$$2\overline{\beta x} + i(\alpha  -\overline{\alpha})y + (\alpha  -\overline{\alpha})z = 0$$
$$i(\beta  -\overline{\beta})y + (\beta  +\overline{\beta})z = 0.$$
Thứ nhất và thứ tư phương trình là đồng nhất và phương trình thứ ba là thu được bởi conjugating thứ hai, do đó ở trên hệ rút gọn đến
$$i(\beta  -\overline{\beta})y + (\beta  +\overline{\beta})z = 0$$
$$2\beta x + i(\alpha  -\overline{\alpha})y + (\overline{\alpha} -\alpha )z = 0.$$
Thay thế $\alpha$ bởi $a +$ ib và $\beta$ bởi $c +$ id, ta thu được
$$-dy + cz = 0$$
$$cx -by + i(dx -bz) = 0,$$

<!-- PAGE 607 -->
Mà cho ta các phương trình
$$-dy + cz = 0$$
$$cx -by = 0$$
$$dx -bz = 0.$$
Điều này hệ phương trình tuyến tính có không tầm thường nghiệm $(b, c, d)$ và ma trận của hệ này là
$$\begin{pmatrix} 0 & -d & c \\ c & -b & 0 \\ d & 0 & b \end{pmatrix} .$$
$$-$$
Vì $(b, c, d) \neq  (0, 0, 0)$, ma trận này luôn luôn có $2 \times  2$ ma trận con mà là không suy biến, do đó nó có hạng (rank) $2$, và hệ quả là hạt nhân (hạt nhân (kernel)) của nó là một chiều không gian được sinh (spanned) bởi $(b, c, d)$. Vì vậy, $r_{q}$ có trị riêng (eigenvalue) $1$ với bội (multiplicity) $1$. Nếu ta đã có $det(r_{q}) = -1$, thì các trị riêng (eigenvalues) của $r_{q}$ sẽ là hoặc $(-1, 1, 1)$ hoặc $(-1, e^{i\theta}, e^{-i\theta})$ với $\theta$ ̸ $= k2\pi$ (với $k \in \mathbb{Z})$, contradicting sự kiện rằng $1$ là trị riêng (eigenvalue) với bội (multiplicity) $1$. Vì vậy, $r_{q}$ là phép quay; thực ra, của nó trục được xác định bởi $(b, c, d)$. Trong tóm tắt, $q \mapsto r_{q}$ là ánh xạ $r$ từ SU(2) đến Do đó(3).

> **Định lý 16.3.** ánh xạ $r$: SU(2) $\to$ Do đó(3) là đồng cấu có hạt nhân (kernel) là ${I, -I}$.

*Chứng minh.* ánh xạ này là đồng cấu, bởi vì nếu $q_{1}, q_{2} \in$ SU(2), thì
$$r_{q2}(r_{q1}(x, y, z)) = \phi^{-1} (q_{2}\phi (r_{q1}(x, y, z))q_{2}^{*})$$
$$= \phi^{-1} (q_{2}\phi (\phi^{-1} (q_{1}\phi (x, y, z)q_{1}^{*}))q_{2}^{*})$$
$$= \phi^{-1} ((q_{2}q_{1})\phi (x, y, z)(q_{2}q_{1})^{*})$$
$$= r_{q2q1}(x, y, z).$$
Phép tính rằng đã chỉ ra rằng nếu $(b, c, d) \neq  (0, 0, 0)$, thì $r_{q}$ có trị riêng (eigenvalue) $1$ với bội (multiplicity) $1$ suy ra sau đây: nếu $r_{q} = I_{3}$, cụ thể là $r_{q}$ có trị riêng (eigenvalue) $1$ với bội (multiplicity) $3$, thì $(b, c, d) = (0, 0, 0)$. Nhưng khi đó $a = \pm 1$, và do đó $q = \pm I_{2}$. Vì vậy, hạt nhân (kernel) của đồng cấu $r$: SU(2) $\to$ Do đó(3) là ${I, -I}$.
Nhận xét: Perhaps quickest cách để chỉ ra rằng $r$ các ánh xạ SU(2) vào Do đó(3) là đến nhận thấy rằng ánh xạ $r$ là liên tục. Thì, vì nó là đã biết rằng SU(2) là liên thông, ảnh (ảnh (image)) của nó bởi $r$ lies trong liên thông thành phần của I, cụ thể là Do đó(3). Mệnh đề 16.2 đã chỉ ra rằng nếu $u = (b, c, d) \neq  (0, 0, 0)$, thì $r_{q}$ là phép quay có trục được xác định bởi $u = (b, c, d)$. góc $\theta$ của điều này phép quay có thể cũng được xác định. Kết quả sau đây được chứng minh trong Gallier $[73]$ (Chương $9)$.
