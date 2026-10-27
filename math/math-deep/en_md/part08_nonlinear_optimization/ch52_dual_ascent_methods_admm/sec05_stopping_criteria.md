# Stopping Criteria


<!-- PAGE 1926 -->
Consequently we find that
$$- -$$
$$x^{k+3}= z^{k+2}+ \frac{1}{\rho} \lambda^{k+2} \frac{1}{\rho} = x^{k+2} \frac{1}{\rho} .$$
By induction, we obtain
$$x^{k+3}= x^{2}- \frac{k + 1}{\rho} ,for all k \ge 0,$$
which shows that $x^{k+3}$ goes to $-\infty$ when $k$ goes to infinity, and since $x^{k+2} = z^{k+2}$, similarly $z^{k+3}$ goes to $-\infty$ when $k$ goes to infinity.

## 52.5 Stopping Criteria

Going back to Inequality (A2),
$$p^{k+1}-p^{*}\le -(\lambda^{k+1} )^{\top}r^{k+1}-\rho (B(z^{k+1}-z^{k}))^{\top}(-r^{k+1}+ B(z^{k+1}-z^{*})),(A2)$$
using the fact that $Ax^{*} + Bz^{*}$ - $c = 0$ and $r^{k+1} = Ax^{k+1} + Bz^{k+1}$ - $c$, we have
$$-r^{k+1}+ B(z^{k+1}-z^{*}) = -Ax^{k+1}-Bz^{k+1}+ c + B(z^{k+1}-z^{*})$$
$$= -Ax^{k+1}+ c -Bz^{*}$$
$$= -Ax^{k+1}+ Ax^{*}= -A(x^{k+1}-x^{*}),$$
so (A2) can be rewritten as
$$p^{k+1}-p^{*}\le -(\lambda^{k+1} )^{\top}r^{k+1}+ \rho (B(z^{k+1}-z^{k}))^{\top}A(x^{k+1}-x^{*}),$$
or equivalently as
$$p^{k+1}-p^{*}\le -(\lambda^{k+1} )^{\top}r^{k+1}+ (x^{k+1}-x^{*})^{\top}\rho A^{\top}B(z^{k+1}-z^{k}).(s_{1})$$
We define the dual residual as
$$s^{k+1}= \rho A^{\top}B(z^{k+1}-z^{k}),$$
the quantity $r^{k+1} = Ax^{k+1} + Bz^{k+1}$ - $c$ being the primal residual. Then $(s_{1})$ can be written as
$$p^{k+1}-p^{*}\le -(\lambda^{k+1} )^{\top}r^{k+1}+ (x^{k+1}-x^{*})^{\top}s^{k+1}.(s)$$
Inequality $(s)$ shows that when the residuals $r^{k}$ and $s^{k}$ are small, then $p^{k}$ is close to $p^{*}$ from below. Since $x^{*}$ is unknown, we can’t use this inequality, but if we have a guess that -

$\le x^{k} x^{*} d$, then using Cauchy–Schwarz we obtain
$$+



.$$
$$p^{k+1}-p^{*}\le \lambda^{k+1} r^{k+1} ds^{k+1}$$
