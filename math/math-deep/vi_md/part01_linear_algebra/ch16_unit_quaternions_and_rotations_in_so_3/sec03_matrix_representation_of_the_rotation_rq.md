# Ma trận Biểu diễn của Phép quay rq


<!-- PAGE 608 -->

> **Định lý 16.4.** Cho $r$: SU(2) $\to$ Do đó(3) là đồng cấu của Định nghĩa 16.5. Với mọi quaternion đơn vị (unit quaternion)
$$q = \begin{pmatrix} a + ib & c + id \\ -(c -id) & a -ib \end{pmatrix} ,$$
Ta có $r_{q} = I_{3}$ khi và chỉ khi $u = (b, c, d) = 0$ khi và chỉ khi || $= 1$. Nếu $u \neq  0$, thì hoặc $a = 0$ và $r_{q}$ là phép quay bởi $\pi$ xung quanh trục của phép quay được xác định bởi vectơ $u = (b, c, d)$, hoặc $0 <$ || $< 1$ và $r_{q}$ là phép quay xung quanh trục của phép quay được xác định bởi vectơ $u = (b, c, d)$ và góc của phép quay $\theta  \neq  \pi$ với $0 < \theta  < 2\pi$, được cho bởi
$$\|\|$$
$$\tan(\theta /2) = \frac{u}{a} .$$
Ở đây ta là giả sử rằng cơ sở (basis) $(w_{1}, w_{2})$ có đã được được chọn trong mặt phẳng trực giao đến $u = (b, c, d)$ sao cho $(w_{1}, w_{2}, u)$ là một cách dương được định hướng, nghĩa là, $det(w_{1}, w_{2}, u) > 0$ (ở đâu $w_{1}, w_{2}, u$ được biểu diễn trên cơ sở chính tắc (canonical basis) $(e_{1}, e_{2}, e_{3})$, mà được chọn để định nghĩa dương định hướng).
Nhận xét: Dưới định hướng được định nghĩa ở trên, ta có
$$\cos(\theta /2) = a,0 < \theta  < 2\pi .$$
Lưu ý rằng điều kiện $0 < \theta  < 2\pi$ suy ra rằng $\theta$ là một cách duy nhất được xác định bởi ở trên phương trình. Điều này là không trường hợp nếu ta chọn $\pi$ sao cho $-\pi  < \theta  < \pi$ vì cả hai $\theta$ và $-\theta$ thỏa mãn phương trình, và điều này chỉ ra tại sao điều kiện $0 < \theta  < 2\pi$ được ưu tiên hơn. Nếu $0 <$ $< 1$, thì $0 < \theta  < \pi$, và nếu $-1 <$ $< 0$, thì $\pi  < \theta  < 2\pi$. Trong trường hợp thứ hai, $r_{q}$ là cũng phép quay của trục $-u$ và của góc $-(2\pi$ - $\theta$) $= \theta$ - $2\pi$ với $0 < 2\pi$ - $\theta  < \pi$, nhưng điều này time định hướng của mặt phẳng trực giao đến $-u = (b, c, d)$ là opposite định hướng từ trước. Điều này định hướng được cho bởi $(w_{2}, w_{1})$, sao cho $(w_{2}, w_{1}, -u)$ có dương định hướng. Vì các quaternion $q$ và $-q$ định nghĩa cùng phép quay, ta có thể giả sử rằng $> 0$, trong mà trường hợp $0 < \theta  < \pi$, nhưng ta có đến nhớ rằng nếu $< 0$ và nếu ta chọn $-q$ thay vì của $q$, vectơ định nghĩa trục của phép quay trở thành $-u$, mà tương đương với đến flipping định hướng của mặt phẳng trực giao đến trục của phép quay. ánh xạ $r$ là toàn ánh (surjective), nhưng điều này là không hiển nhiên. Ta sẽ trả về đến điều này điểm sau việc tìm ma trận biểu diễn $r_{q}$ một cách tường minh.

## 16.3 Ma trận Biểu diễn của Phép quay r

$$q$$
Cho trước quaternion đơn vị (unit quaternion) $q$ của tạo thành
$$q = \begin{pmatrix} \alpha & \beta \\ -\beta & \overline{\alpha} \end{pmatrix}$$

<!-- PAGE 609 -->
$$\mathbb{R}$$
Với $\alpha  = a +$ ib, $\beta  = c +$ id, và $a^{2} + b^{2} + c^{2} + d^{2} = 1$ (, $b, c, d \in$), để tìm ma trận biểu diễn phép quay $r_{q}$ ta cần để tính
$$q(x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1} )q^{*}= \begin{pmatrix} \alpha & \beta \\ -\beta & \overline{\alpha} \end{pmatrix} \begin{pmatrix} x & z -iy \\ z + iy & -x \end{pmatrix} \begin{pmatrix} \overline{\alpha} & -\beta \\ \beta & \alpha \end{pmatrix} .$$
Thứ nhất, ta có
$$\begin{pmatrix} x & z -iy \\ z + iy & -x \end{pmatrix} \begin{pmatrix} \overline{\alpha} & -\beta \\ \beta & \alpha \end{pmatrix} = \begin{pmatrix} \overline{x\alpha} +\overline{z\beta} -\overline{iy\beta} & -x\beta  + z\alpha  -iy\alpha \\ \overline{z\alpha} +\overline{iy\alpha} -x\beta & -z\beta  -iy\beta  -x\alpha \end{pmatrix} .$$
Tiếp theo, ta có
$$\begin{pmatrix} \alpha & \beta \\ -\beta & \overline{\alpha} \end{pmatrix} \begin{pmatrix} \overline{x\alpha} +\overline{z\beta} -\overline{iy\beta} & -x\beta  + z\alpha  -iy\alpha \\ \overline{z\alpha} +\overline{iy\alpha} -x\beta & -z\beta  -iy\beta  -x\alpha \end{pmatrix} =$$
$$!$$
$$(\overline{\alpha \alpha} - \frac{\overline{\beta \beta}}{\overline{\alpha \beta x}} )x + i(\overline{\alpha \beta}  -\overline{\alpha \beta})y + ( -\overline{\alpha \beta} \frac{+}{\beta^{2}} \overline{\alpha \beta})z-2\alpha \beta x -i(\alpha^{2} + \beta^{2} ) \frac{y}{\alpha \beta} + (\alpha^{2} - \frac{\beta^{2}}{\alpha \beta} )z$$
$-2  + i(\overline{\alpha}^{2} +\overline{\beta}^{2})y + (\overline{\alpha}^{2} )z -(\overline{\alpha \alpha}$ - $\overline{\beta \beta})x$ - $i(\overline{\alpha \beta}$ - $)y$ - ($+\overline{\alpha \beta})z$ Vì $\alpha  = a +$ ib và $\beta  = c +$ id, với, $b, c, d \in \mathbb{R}$, ta có
$$\overline{\alpha \alpha} -\overline{\beta \beta} = a^{2}+ b^{2}-c^{2}-d^{2}$$
$$i(\overline{\alpha \beta} -\overline{\alpha \beta}) = 2(bc -ad)$$
$$\overline{\alpha \beta} +\overline{\alpha \beta} = 2(ac + bd)$$
$$-\alpha \beta  = -ac + bd -i(ad + bc)$$
$$-i(\alpha^{2} + \beta^{2} ) = 2(ab + cd) -i(a^{2}-b^{2}+ c^{2}-d^{2})$$
$$\alpha^{2} -\beta^{2} = a^{2}-b^{2}-c^{2}+ d^{2}+ i2(ab -cd).$$
Bằng cách sử dụng ở trên, ta thu được $(\overline{\alpha \alpha}$ - $\overline{\beta \beta})x + i(\overline{\alpha \beta}$ - $\overline{\alpha \beta})y + (\overline{\alpha \beta} +\overline{\alpha \beta})z = (a^{2} + b^{2}$ - $c^{2}$ - $d^{2})x +$ 2(bc - ad)y $+$ 2(ac $+$ bd)z, và - $2\alpha \beta x$ - $i(\alpha^{2} + \beta^{2} )y + (\alpha^{2}$ - $\beta^{2} )z =$ 2(-ac $+$ bd)x $+$ 2(ab $+$ cd)y $+ (a^{2}$ - $b^{2}$ - $c^{2} + d^{2})z$
$$-i[2(ad + bc)x + (a^{2}-b^{2}+ c^{2}-d^{2})y + 2(-ab + cd)z].$$
Nếu ta viết
$$q(x\sigma_{3}  + y\sigma_{2}  + z\sigma_{1} )q^{*}= \begin{pmatrix} x' & z'-iy' \\ z'+ iy' & -x' \end{pmatrix} ,$$
Ta thu được
$$x'= (a^{2}+ b^{2}-c^{2}-d^{2})x + 2(bc -ad)y + 2(ac + bd)z$$
$$y'= 2(ad + bc)x + (a^{2}-b^{2}+ c^{2}-d^{2})y + 2(-ab + cd)z$$
$$z'= 2(-ac + bd)x + 2(ab + cd)y + (a^{2}-b^{2}-c^{2}+ d^{2})z.$$
Trong tóm tắt, ta được chứng minh kết quả sau đây.
