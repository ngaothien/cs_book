# Hàm mũ Ánh xạ exp2mu-:6muplus1musu(2)SU(2)


<!-- PAGE 613 -->
Nó là dễ để kiểm tra rằng bất cứ khi nào ta được tính square nghiệm (root), nếu ta đã có được chọn âm dấu thay vì của dương dấu, ta sẽ thu được quaternion $-q$. Tuy nhiên, cả hai $q$ và $-q$ xác định cùng phép quay $r_{q}$. ở trên thảo luận liên quan đến các trường hợp tr(R) $\neq  -1$ và tr(R) $= -1$ là reminiscent của quy trình cho việc tìm lôgarit của ma trận quay (rotation matrix) bằng cách sử dụng Rodrigues công thức (xem Mục 12.7). Điều này là không đáng ngạc nhiên, bởi vì nếu
$$B = \begin{pmatrix} 0 & -u_{3} & u_{2} \\ u_{3} & 0 & -u_{1} \\ u_{2} & u_{1} & 0 \end{pmatrix}$$
$$-$$
Và nếu ta viết $\theta  = p\overline{u}_{1}^{2} \overline{+}\overline{u}_{2}^{2} \overline{+}\overline{u}_{3}^{2}$ (với $0 \le \theta  \le 2\pi$), thì Rodrigues công thức nói rằng rằng
$$-$$
$$e^{B}= I + \frac{\sin \theta}{\theta} B + \frac{(1cos \theta )}{\theta^{2}} B^{2},\theta  \neq  0,$$
Với $e^{0} =$ I. Nó là dễ để kiểm tra rằng $tr(e^{B}) = 1+2$ cos $\theta$. Thì nó là dễ bài tập để kiểm tra rằng quaternion $q$ tương ứng với phép quay $R = e^{B}$ (với $B \neq  0)$ được cho bởi
$$$$
$$q =\cos \begin{pmatrix} \theta \\ 2 \end{pmatrix} , \sin \begin{pmatrix} \theta \\ 2 \end{pmatrix} \begin{pmatrix} u_{1}, u_{2}, u_{3} \\ \theta & \overline{\theta} & \overline{\theta} \end{pmatrix} .$$
Do đó phương pháp cho việc tìm lôgarit của phép quay $R$ là về cơ bản cùng như phương pháp cho việc tìm quaternion định nghĩa $R$.
$$\mathbb{R}^{4}$$
Nhận xét: Geometrically, nhóm SU(2) là đồng phôi đến 3-mặt cầu $S^{3}$ trong,
$$\mathbb{R}^{4}$$
$$S^{3}= {(x, y, z, t) \in | x^{2}+ y^{2}+ z^{2}+ t^{2}= 1}.$$
Tuy nhiên, vì hạt nhân (kernel) của toàn ánh (surjective) đồng cấu $r$: SU(2) $\to$ Do đó(3) là ${I, -I}$, như không gian tôpô (topological space), Do đó(3) là đồng phôi đến thương của $S^{3}$ thu được bởi đồng nhất antipodal các điểm $(x, y, z, t)$ và -(x, $y, z, t)$. Điều này không gian thương (quotient space) là (thực) không gian xạ ảnh (projective space) $\mathbb{RP}^{3}  \mathbb{RP}^{3}$, và nó là nhiều hơn/thêm phức tạp hơn $S^{3}$. không gian $S^{3}$ là simply-connected, nhưng là không.

## 16.5 Hàm mũ Ánh xạ exp: \mathfrak{su}(2) \đến SU(2)

Cho trước bất kỳ ma trận $A \in \mathfrak{su}(2)$, với
$$A = \begin{pmatrix} iu_{1} & u_{2} + iu_{3} \\ -u_{2} + iu_{3} & -iu_{1} \end{pmatrix} ,$$
Nó là dễ để kiểm tra rằng
$$A^{2}= -\theta^{2} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} ,$$
Với $\theta  = p\overline{u}_{1}^{2} \overline{+}\overline{u}_{2}^{2} \overline{+}\overline{u}_{3}^{2}$. Thì ta có kết quả sau công thức có chứng minh là rất đồng dạng đến chứng minh của công thức cho trước trong Mệnh đề 9.23.

<!-- PAGE 614 -->

> **Mệnh đề 16.7.** Với mọi ma trận $A \in \mathfrak{su}(2)$, với
$$A = \begin{pmatrix} iu_{1} & u_{2} + iu_{3} \\ -u_{2} + iu_{3} & -iu_{1} \end{pmatrix} ,$$
Nếu ta viết $\theta  = p\overline{u}_{1}^{2} \overline{+}\overline{u}_{2}^{2} \overline{+}\overline{u}_{3}^{2}$, thì
$$e^{A}= \cos \theta I + \frac{\sin \theta}{\theta} A,\theta  \neq  0,$$
Và $e^{0} =$ I. Vì vậy, bởi thảo luận tại kết thúc/cuối của trước đó mục, $e^{A}$ là quaternion đơn vị (unit quaternion) biểu diễn phép quay của góc $2\theta$ và trục $(u_{1}, u_{2}, u_{3})$ (hoặc I khi $\theta  = k\pi , k \in \mathbb{Z})$. ở trên công thức chỉ ra rằng ta có thể giả sử rằng $0 \le \theta  \le \pi$. Mệnh đề 16.7 chỉ ra rằng hàm mũ cho ta ánh xạ exp: $\mathfrak{su}(2) \to$ SU(2). Nó là tương tự của hàm mũ ánh xạ exp: $\mathfrak{so}(3) \to$ Do đó(3).
Nhận xét: $Because\mathfrak{so}(3) and\mathfrak{su}(2)$ là thực các không gian vectơ có số chiều $3$, chúng là đẳng cấu, và nó là dễ để xây dựng đẳng cấu. Thực ra, $\mathfrak{so}(3)$ và $\mathfrak{su}(2)$ là đẳng cấu như Lie các đại số, mà có nghĩa là có một tuyến tính đẳng cấu bảo toàn Lie bracket $[A, B] = AB$ - $BA$. Tuy nhiên, như được quan sát trước đó, các nhóm SU(2) và Do đó(3) là không đẳng cấu. tương đương, nhưng thường nhiều hơn/thêm thuận tiện, công thức là thu được bởi giả sử rằng $u = (u_{1}, u_{2}, u_{3})$ là unit vectơ, tương đương det() $= 1$, trong mà trường hợp $A^{2} = -I$, do đó ta có
$$e^{\theta A}= \cos \theta I + \sin \theta A.$$
Bằng cách sử dụng quaternion ký hiệu, điều này là read như
$$e^{\theta A}= [\cos \theta , \sin \theta  u].$$

> **Mệnh đề 16.8.** hàm mũ ánh xạ exp: $\mathfrak{su}(2) \to$ SU(2) là toàn ánh (surjective)

*Chứng minh.* Ta cho thuật toán để tìm lôgarit $A \in \mathfrak{su}(2)$ của quaternion đơn vị (unit quaternion)
$$q = \begin{pmatrix} \alpha & \beta \\ -\beta & \overline{\alpha} \end{pmatrix}$$
Với $\alpha  = a +$ bi và $\beta  = c +$ id. Nếu $q =$ I (i.e. $a = 1)$, thì $A = 0$. Nếu $q = -I$ (i.e. $a = -1)$, thì
$$A = \pm \pi \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix} .$$

<!-- PAGE 615 -->
Ngược lại, $a \neq  \pm 1$ và $(b, c, d) \neq  (0, 0, 0)$, và ta là seeking một số $A = \theta B \in \mathfrak{su}(2)$ với det(B) $= 1$ và $0 < \theta  < \pi$, sao cho, theo Mệnh đề 16.7,
$$q = e^{\theta B}= \cos \theta I + \sin \theta B.$$
Cho
$$B = \begin{pmatrix} iu_{1} & u_{2} + iu_{3} \\ -u_{2} + iu_{3} & -iu_{1} \end{pmatrix} ,$$
Với $u = (u_{1}, u_{2}, u_{3})$ unit vectơ. Ta phải có
$$a = \cos \theta ,e^{\theta B}-(e^{\theta B})^{*}= q -q^{*}.$$
Vì $0 < \theta  < \pi$, ta có sin $\theta  \neq  0$, và
$$2 \sin \theta \begin{pmatrix} iu_{1} & u_{2} + iu_{3} \\ -u_{2} + iu_{3} & -iu_{1} \end{pmatrix} = \begin{pmatrix} \alpha  -\overline{\alpha} & 2\beta \\ -2\beta & \overline{\alpha} -\alpha \end{pmatrix} .$$
Do đó, ta thu được
$$u_{1} = \frac{1}{\sin} \theta  b,u_{2} + iu_{3} = \frac{1}{\sin \theta} (c + id);$$
Rằng là,
$$\cos \theta  = a(0 < \theta  < \pi )$$
$$(u_{1}, u_{2}, u_{3}) = \frac{1}{\sin \theta} (b, c, d).$$
Vì $a^{2}+b^{2}+c^{2}+d^{2} = 1$ và $a =$ cos $\theta$, vectơ $(b, c, d)/$ sin $\theta$ là unit vectơ. Hơn nữa nếu quaternion $q$ là của tạo thành $q =$ [cos $\theta$, sin $\theta u]$ ở đâu $u = (u_{1}, u_{2}, u_{3})$ là unit vectơ (với $0 < \theta  < \pi$), thì
$$A = \theta \begin{pmatrix} iu_{1} & u_{2} + iu_{3} \\ -u_{2} + iu_{3} & -iu_{1} \end{pmatrix} (*_{\log})$$
Là lôgarit của $q$. Nhận thấy rằng không chỉ là hàm mũ ánh xạ exp: $\mathfrak{su}(2) \to$ SU(2) toàn ánh (surjective), nhưng ở trên chứng minh chỉ ra rằng nó là đơn ánh (injective) trên hình cầu mở (open ball)
$${\theta B \in \mathfrak{su}(2) | \det(B) = 1, 0 \le \theta  < \pi }.$$
Cũng, unlike tình huống ở đâu trong việc tính toán lôgarit của ma trận quay (rotation matrix) $R \in$ Do đó(3) ta cần thiết đến treat trường hợp ở đâu tr(R) $= -1$ (góc của phép quay là $\pi$) trong đặc biệt cách, việc tính toán lôgarit của quaternion (ngoài $\pm$ I) thực hiện không đòi hỏi bất kỳ trường hợp giải tích/phân tích; không có đặc biệt trường hợp là cần thiết khi góc của phép quay là $\pi$.
