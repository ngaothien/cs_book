# Euclidean Phép chia của Các đa thức


<!-- PAGE 1074 -->
$$Given any nonnull polynomial P(X_{1}, \dots  , X_{n}) = \sum_{(}  k1,...,k\mathbb{N}(n) a_{(k1,...,kn)}X_{1}^{k1} \cdots  X_{n}^{kn}in$$
$A[X_{1}, \dots  , X_{n}]$, ở đâu $n \ge 2, P(X_{1}, \dots  , X$) có thể được $uniquely^{n)\in}$ được viết như
$$P(X_{1}, \dots  , X_{n}) = \sum^{n}  Q_{kn}(X_{1}, \dots  , X_{n-1})X_{n}^{kn} ,$$
Ở đâu mỗi đa thức $Q_{kn}(X_{1}, \dots  , X_{n-1})$ là trong $A[X_{1}, \dots  , X_{n-1}]$. Chẵn/ngay cả nếu $A$ là trường, $A[X_{1}, \dots  , X_{n-1}]$ là không trường, mà xác nhận rằng nó là hữu ích (và cần!) đến xét các đa thức trên các vành rằng là không nhất thiết các trường. Nó là không khó để chỉ ra rằng $A[X_{1}, \dots  , X_{n}]$ và $A[X_{1}, \dots  , X_{n-1}][X_{n}]$ là đẳng cấu các vành. Điều này cách, nó là thường khả dĩ/có thể để chứng minh các tính chất của các đa thức trong một vài các biến $X_{1}, \dots  , X_{n}$, bằng quy nạp theo số $n$ của các biến. Ví dụ, cho trước hai khác không các đa thức $P(X_{1}, \dots  , X_{n})$ của tổng bậc $p$ và $Q(X_{1}, \dots  , X_{n})$ của tổng bậc $q$, vì ta được giả sử rằng $A$ là miền nguyên (integral domain), ta có thể chứng minh rằng
$$deg(PQ) = deg(P) + deg(Q),$$
Và rằng $A[X_{1}, \dots  , X_{n}]$ là miền nguyên (integral domain). Tiếp theo, ta sẽ xét phép chia của các đa thức (trong một biến).

## 30.3 Euclidean Phép chia của Các đa thức

Ta biết rằng mọi tự nhiên số $n \ge 2$ có thể được được viết một cách duy nhất như tích của các lũy thừa của nguyên tố các số và rằng nguyên tố các số đóng rất quan trọng vai trò trong arithmetic. Nó sẽ là đẹp nếu mọi đa thức có thể được biểu diễn (một cách duy nhất) như tích của “bất khả quy (irreducible)” các nhân tử. Điều này là thật vậy trường hợp cho các đa thức trên trường. sự kiện rằng có một phép chia thuật toán cho tự nhiên các số là thiết yếu cho thu được nhiều của arithmetical các tính chất của tự nhiên các số. Như ta sẽ xem tiếp theo, ở đó là cũng phép chia thuật toán cho các đa thức trong [X], khi $A$ là trường.

> **Mệnh đề 30.4.** Cho $A$ là vành, cho f(X), g(X) $\in$ [X] là hai các đa thức của bậc $m =$ deg(f) và $n =$ deg(g) với f(X) $\neq  0$, và giả sử rằng dẫn đầu hệ số $a_{m}$ của f(X) là khả nghịch. Thì, ở đó tồn tại duy nhất các đa thức q(X) và r(X) trong [X] sao cho
$$g = fq + randdeg(r) < deg(f) = m.$$

*Chứng minh.* Ta thứ nhất chứng minh sự tồn tại của $q$ và $r$. Cho
$$f = a_{m}X^{m}+ a_{m-1}X^{m-1}+ \cdots  + a_{0},$$
Và
$$g = b_{n}X^{n}+ b_{n-1}X^{n-1}+ \cdots  + b_{0}.$$
Nếu $n < m$, thì cho $q = 0$ và $r = g$. Vì deg(g) $<$ deg(f) và $r = g$, ta có deg(r) $<$ deg(f).

<!-- PAGE 1075 -->
Nếu $n \ge m$, ta tiến hành bằng quy nạp theo $n$. Nếu $n = 0$, thì $g = b_{0}, m = 0, f = a_{0} \neq  0$, và ta cho $q = a_{0}^{-1} b_{0}$ và $r = 0$. Vì deg(r) $=$ deg(0) $= -\infty$ và deg(f) $= deg(a_{0}) = 0$ bởi vì $a_{0} \neq  0$, ta có deg(r) $<$ deg(f). Nếu $n \ge 1$, vì $n \ge m$, lưu ý rằng $g_{1}(X) =$ g(X) - $b_{n}a_{m}^{-1} X^{n-m}f(X)$
$$+ +$$
$$= b_{n}X^{n}+ b_{n-1}X^{n-1}+ \cdots  + b_{0} -b_{n}a_{m}^{-1} X^{n-m}(a_{m}X^{m} a_{m-1}X^{m-1} \cdots  + a_{0})$$
Là đa thức của bậc $deg(g_{1}) < n$, vì các số hạng $b_{n}X^{n}$ và $b_{n}a_{m}^{-1} X^{n-m}a_{m}X^{m}$ của bậc $n$ cancel ra. Bây giờ, vì $deg(g_{1}) < n$, theo giả thiết quy nạp, ta có thể tìm $q_{1}$ và $r$ sao cho
$$g_{1} = fq_{1} + randdeg(r) < deg(f) = m,$$
Và do đó,
$$g_{1}(X) = g(X) -b_{n}a_{m}^{-1} X^{n-m}f(X) = f(X)q_{1}(X) + r(X),$$
$$+$$
Từ mà, đặt q(X) $= b_{n}a_{m}^{-1} X^{n-m}  q_{1}(X)$, ta thu được
$$g = fq + randdeg(r) < m = deg(f).$$
Ta bây giờ chứng minh tính duy nhất. Nếu
$$g = fq_{1} + r_{1} = fq_{2} + r_{2},$$
Với $deg(r_{1}) <$ deg(f) và $deg(r_{2}) <$ deg(f), ta thu được
$$f(q_{1} -q_{2}) = r_{2} -r_{1}.$$
Nếu $q_{2} -q_{1} \neq  0$, vì dẫn đầu hệ số $a_{m}$ của $f$ là khả nghịch, theo Mệnh đề 30.1, ta có
$$deg(r_{2} -r_{1}) = deg(f(q_{1} -q_{2})) = deg(f) + deg(q_{2} -q_{1}),$$
Và do đó, $deg(r_{2}-r_{1}) \ge$ deg(f), mà mâu thuẫn với sự kiện là $deg(r_{1}) <$ deg(f) và $deg(r_{2}) <$ deg(f). Do đó, $q_{1} = q_{2}$, và thì cũng $r_{1} = r_{2}$. Nó nên được lưu ý rằng chứng minh của Mệnh đề 30.4 thực sự cung cấp thuật toán cho việc tìm thương $q$ và phần dư $r$ của phép chia của $g$ bởi $f$. thuật toán này được gọi là Euclidean thuật toán, hoặc phép chia thuật toán. Lưu ý rằng phép chia của $g$ bởi $f$ là luôn luôn khả dĩ/có thể khi $f$ là chuẩn hóa (monic) đa thức, vì $1$ là khả nghịch. Cũng, khi $A$ là trường, $a_{m} \neq  0$ là luôn luôn khả nghịch, và do đó, phép chia có thể luôn luôn là performed. Ta nói rằng $f$ chia hết $g$ khi $r = 0$ trong kết quả của phép chia $g =$ fq $+ r$. Ta bây giờ draw một số quan trọng các hệ quả của sự tồn tại của Euclidean thuật toán.
