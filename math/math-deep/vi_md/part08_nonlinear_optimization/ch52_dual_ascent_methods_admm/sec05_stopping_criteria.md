# Stopping Các tiêu chuẩn


<!-- PAGE 1926 -->
Hệ quả là ta tìm rằng
$$- -$$
$$x^{k+3}= z^{k+2}+ \frac{1}{\rho} \lambda^{k+2} \frac{1}{\rho} = x^{k+2} \frac{1}{\rho} .$$
Bởi quy nạp, ta thu được
$$x^{k+3}= x^{2}- \frac{k + 1}{\rho} ,for all k \ge 0,$$
Mà chỉ ra rằng $x^{k+3}$ đi đến $-\infty$ khi $k$ đi đến vô cực, và vì $x^{k+2} = z^{k+2}$, tương tự $z^{k+3}$ đi đến $-\infty$ khi $k$ đi đến vô cực.

## 52.5 Stopping Các tiêu chuẩn

Đi quay lại đến Bất đẳng thức (A2),
$$p^{k+1}-p^{*}\le -(\lambda^{k+1} )^{\top}r^{k+1}-\rho (B(z^{k+1}-z^{k}))^{\top}(-r^{k+1}+ B(z^{k+1}-z^{*})),(A2)$$
Bằng cách sử dụng sự kiện rằng $Ax^{*} + Bz^{*}$ - $c = 0$ và $r^{k+1} = Ax^{k+1} + Bz^{k+1}$ - $c$, ta có
$$-r^{k+1}+ B(z^{k+1}-z^{*}) = -Ax^{k+1}-Bz^{k+1}+ c + B(z^{k+1}-z^{*})$$
$$= -Ax^{k+1}+ c -Bz^{*}$$
$$= -Ax^{k+1}+ Ax^{*}= -A(x^{k+1}-x^{*}),$$
Do đó (A2) có thể được được viết lại như
$$p^{k+1}-p^{*}\le -(\lambda^{k+1} )^{\top}r^{k+1}+ \rho (B(z^{k+1}-z^{k}))^{\top}A(x^{k+1}-x^{*}),$$
Hoặc tương đương như
$$p^{k+1}-p^{*}\le -(\lambda^{k+1} )^{\top}r^{k+1}+ (x^{k+1}-x^{*})^{\top}\rho A^{\top}B(z^{k+1}-z^{k}).(s_{1})$$
Ta định nghĩa đối ngẫu (dual) phần dư (residual) như
$$s^{k+1}= \rho A^{\top}B(z^{k+1}-z^{k}),$$
Đại lượng $r^{k+1} = Ax^{k+1} + Bz^{k+1}$ - $c$ đang là gốc (primal) phần dư (residual). Thì $(s_{1})$ có thể được viết dưới dạng
$$p^{k+1}-p^{*}\le -(\lambda^{k+1} )^{\top}r^{k+1}+ (x^{k+1}-x^{*})^{\top}s^{k+1}.(s)$$
Bất đẳng thức $(s)$ chỉ ra rằng khi các phần dư $r^{k}$ và $s^{k}$ là nhỏ, thì $p^{k}$ là close đến $p^{*}$ từ ở dưới. Vì $x^{*}$ là unknown, ta có thể’t sử dụng bất đẳng thức này, nhưng nếu ta có guess rằng -

$\le x^{k} x^{*} d$, thì bằng cách sử dụng Cauchy–Schwarz ta thu được
$$+



.$$
$$p^{k+1}-p^{*}\le \lambda^{k+1} r^{k+1} ds^{k+1}$$
