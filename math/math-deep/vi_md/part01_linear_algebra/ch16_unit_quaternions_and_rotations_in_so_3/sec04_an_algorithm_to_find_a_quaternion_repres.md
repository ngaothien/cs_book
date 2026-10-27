# Thuật toán để tìm Quaternion Biểu diễn Phép quay


<!-- PAGE 610 -->

> **Mệnh đề 16.5.** ma trận biểu diễn $r_{q}$ là
$$R_{q} = \begin{pmatrix} a^{2}+ b^{2}-c^{2}-d^{2} & 2bc -2ad & 2ac + 2bd \\ 2bc + 2ad & a^{2}-b^{2}+ c^{2}-d^{2} & -2ab + 2cd \\ 2ac + 2bd & 2ab + 2cd & a^{2} & b^{2} & c^{2}+ d^{2} \end{pmatrix} .$$
$$---$$
Vì $a^{2} + b^{2} + c^{2} + d^{2} = 1$, ma trận này có thể cũng được viết như
$$R_{q} = \begin{pmatrix} 2a^{2}+ 2b^{2}-1 & 2bc -2ad & 2ac + 2bd \\ 2bc + 2ad & 2a^{2}+ 2c^{2}-1 & -2ab + 2cd \\ 2ac + 2bd & 2ab + 2cd & 2a^{2}+ 2d^{2} & 1 \end{pmatrix} .$$
$$--$$
Ở trên là ma trận quay (rotation matrix) trong Euler tạo thành được cảm sinh bởi quaternion $q$, mà là ma trận tương ứng với $\rho_{q}$. Điều này là bởi vì
$$\phi  = -i\psi ,\phi^{-1} = i\psi^{-1} ,$$
Do đó $r_{q}(x, y, z) = \phi^{-1} (q\phi (x, y, z)q^{*}) = i\psi^{-1} (q(-i\psi (x, y, z))q^{*}) = \psi^{-1} (q\psi (x, y, z)q^{*}) = \rho_{q} (x, y, z)$, và do đó $r_{q} = \rho_{q}$. Ta đã chỉ ra rằng mọi quaternion đơn vị (unit quaternion) $q \in$ SU(2) cảm sinh phép quay $r_{q} \in$ Do đó(3), nhưng nó là không hiển nhiên rằng mọi phép quay có thể được biểu diễn bởi quaternion. Điều này có thể được hiển thị trong khác nhau các cách. Một cách đến là sử dụng sự kiện rằng mọi phép quay trong Do đó(3) là hợp thành của hai reflec-
$$\mathbb{R}^{3}$$
Tions, và rằng mọi phép đối xứng (reflection) $\sigma$ của có thể được biểu diễn bởi quaternion $q$, trong nghĩa rằng
$$\sigma (x, y, z) = -\phi^{-1} (q\phi (x, y, z)q^{*}).$$
Lưu ý presence của âm dấu. Điều này là phương pháp được sử dụng trong Gallier $[73]$ (Chương $9)$.

## 16.4 Thuật toán để tìm Quaternion Biểu diễn

$$a Rotation$$

> **Định lý 16.6.** đồng cấu $r$: SU(2) $\to$ Do đó(3) là toàn ánh (surjective). Ở đây là algorithmic phương pháp để tìm quaternion đơn vị (unit quaternion) $q$ biểu diễn ma trận quay (rotation matrix) $R$, mà cung cấp chứng minh của Định lý 16.6. Cho
$$\mathbb{R}$$
$$q = \begin{pmatrix} a + ib & c + id \\ -(c -id) & a -ib \end{pmatrix} ,a^{2}+ b^{2}+ c^{2}+ d^{2}= 1, a, b, c, d \in .$$

<!-- PAGE 611 -->
Thứ nhất nhận thấy rằng vết (trace) của $R_{q}$ được cho bởi
$$\mathrm{tr}(R_{q}) = 3a^{2}-b^{2}-c^{2}-d^{2},$$
Nhưng vì $a^{2} + b^{2} + c^{2} + d^{2} = 1$, ta thu được $tr(R_{q}) = 4a^{2}$ - $1$, do đó
$$a^{2}= \frac{\mathrm{tr}(R_{q}) + 1}{4} .$$
Nếu $R \in$ Do đó(3) là bất kỳ ma trận quay (rotation matrix) và nếu ta viết
$$R = \begin{pmatrix} r_{11} & r_{12} & r_{13} \\ r_{21} & r_{22} & r_{23} \\ r_{31} & r_{32} & r_{33}, \end{pmatrix}$$
Ta là nhìn cho quaternion đơn vị (unit quaternion) $q \in$ SU(2) sao cho $R_{q} = R$. Vì vậy, ta phải có
$$a^{2}= \frac{\mathrm{tr}(R) + 1}{4} .$$
Ta cũng biết rằng
$$\mathrm{tr}(R) = 1 + 2 \cos \theta ,$$
Ở đâu $\theta  \in [0, \pi$ ] là góc của phép quay $R$, do đó ta thu được
$$a^{2}= \frac{\cos \theta  + 1}{2} = \cos^{2} \begin{pmatrix} \theta \\ 2 \end{pmatrix} ,$$
Mà suy ra rằng
$$|a| = \cos \begin{pmatrix} \theta \\ 2 \end{pmatrix} (0 \le \theta  \le \pi ).$$
Lưu ý rằng ta có thể giả sử rằng $\theta  \in [0, \pi$ ], bởi vì nếu $\pi  \le \theta  \le 2\pi$, thì $\theta$ - $2\pi  \in [-\pi , 0]$, và thì phép quay của góc $\theta$ - $2\pi$ và trục được xác định bởi vectơ $(b, c, d)$ là cùng như phép quay của góc $2\pi$ - $\theta  \in [0, \pi$ ] và trục được xác định bởi vectơ -(b, $c, d)$. Có hai các trường hợp. Trường hợp $1$. tr(R) $\neq  -1$, hoặc tương đương $\theta  \neq  \pi$. Trong điều này trường hợp $a \neq  0$. Chọn
$$a = \frac{p\overline{\mathrm{tr}(}\overline{R}\overline{) + 1}}{2} .$$
Thì bởi equating $R$ - $R^{\top}$ và $R_{q}$ - $R_{q}^{\top}$, ta thu được
$$4ab = r_{32} -r_{23}$$
$$4ac = r_{13} -r_{31}$$
$$4ad = r_{21} -r_{12},$$

<!-- PAGE 612 -->
Mà cho ta
$$-  -  -$$
$$b = \frac{r_{32}r_{23}}{4a} ,c = \frac{r_{13}r_{31}}{4a} ,d = \frac{r_{21}r_{12}}{4a} .$$
Trường hợp $2$. tr(R) $= -1$, hoặc tương đương $\theta  = \pi$. Trong điều này trường hợp $a = 0$. Bởi equating $R + R^{\top}$ và $R_{q} + R_{q}^{\top}$, ta thu được
$$4bc = r_{21} + r_{12}$$
$$4bd = r_{13} + r_{31}$$
$$4cd = r_{32} + r_{23}.$$
Bởi equating đường chéo các số hạng của $R$ và $R_{q}$, ta cũng thu được
$$b^{2}= \frac{1 + r_{11}}{2}$$
$$c^{2}= \frac{1 + r_{22}}{2}$$
$$d^{2}= \frac{1 + r_{33}}{2} .$$
Vì $q \neq  0$ và $a = 0$, ít nhất một của $b, c, d$ là khác không. Nếu $b \neq  0$, cho
$$b = \frac{\sqrt{1 +}\overline{r}_{11}}{\overline{2}} \sqrt,$$
Và xác định $c, d$ bằng cách sử dụng
$$4bc = r_{21} + r_{12}$$
$$4bd = r_{13} + r_{31}.$$
Nếu $c \neq  0$, cho
$$c = \frac{\sqrt{1 +}\overline{r}_{22}}{\overline{2}} \sqrt,$$
Và xác định $b, d$ bằng cách sử dụng
$$4bc = r_{21} + r_{12}$$
$$4cd = r_{32} + r_{23}.$$
Nếu $d \neq  0$, cho
$$d = \frac{\sqrt{1 +}\overline{r}_{33}}{\overline{2}} \sqrt,$$
Và xác định $b, c$ bằng cách sử dụng
$$4bd = r_{13} + r_{31}$$
$$4cd = r_{32} + r_{23}.$$
