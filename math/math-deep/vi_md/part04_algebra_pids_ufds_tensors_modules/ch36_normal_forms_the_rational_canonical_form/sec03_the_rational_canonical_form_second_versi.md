# Dạng chính tắc hữu tỷ (rational canonical form), Thứ hai Phiên bản


<!-- PAGE 1334 -->

## 36.3 Dạng chính tắc hữu tỷ (rational canonical form), Thứ hai Phiên bản

Cho chúng ta bây giờ translate Các ước sơ cấp (elementary divisors) Phân rã Định lý, Định lý 35.38, theo $E_{f}$. Ta thu được kết quả sau kết quả.

> **Định lý 36.14.** (Xích (cyclic) Phân rã Định lý, Thứ hai Phiên bản) Cho $f$: $E \to E$ là tự đồng cấu trên vectơ $K$ không gian có số chiều $n$. Thì, $E$ là tổng trực tiếp (direct sum) của của xích (cyclic) các không gian con $E_{j} = Z(u_{j}; f)$ cho $f$, sao cho đa thức tối tiểu (minimal polynomial) của $E_{j}$ là của tạo thành $p_{i}^{ni,j}$, với một số bất khả quy (irreducible) chuẩn hóa (monic) các đa thức $p_{1}, \dots  , p_{t} \in$ K[X] và một số dương các số nguyên $n_{i,j}$, sao cho với mỗi $i = 1, \dots  , t$, có một dãy của các số nguyên
$$1 \le n_{i,1}, \dots  , n_{i,1}< n_{i,2}, \dots  , n_{i,2}< \cdots  < n_{i,si}, \dots  , n_{i,si},$$
$$|{z}|{z}|{z}$$
$$mi,1mi,2mi,si$$
Với $s_{i} \ge 1$, và ở đâu $n_{i,j}$ xảy ra $m_{i,j} \ge 1$ lần, cho $j = 1, \dots  , s_{i}$. Hơn nữa, chuẩn hóa (monic) các đa thức $p_{i}$ và các số nguyên $r, t, n_{i,j}, s_{i}, m_{i,j}$ là một cách duy nhất được xác định.
$$Note that there are \mu  = \sum  m_{i,j} cyclic subspaces Z(u_{j}; f). Using bases for the cyclic$$
Các không gian con $Z(u_{j}; f)$ như trong Định lý 36.6, ta thu được sau đây định lý.

> **Định lý 36.15.** (Dạng chính tắc hữu tỷ (rational canonical form), Thứ hai Phiên bản) Cho $f$: $E \to E$ là tự đồng cấu trên vectơ $K$ không gian có số chiều $n$. Ở đó tồn tại $t$ phân biệt bất khả quy (irreducible) chuẩn hóa (monic) các đa thức $p_{1}, \dots  , p_{t} \in$ K[X] và một số dương các số nguyên $n_{i,j}$, sao cho với mỗi $i = 1, \dots  , t$, có một dãy của các số nguyên
$$1 \le n_{i,1}, \dots  , n_{i,1}< n_{i,2}, \dots  , n_{i,2}< \cdots  < n_{i,si}, \dots  , n_{i,si},$$
$$|{z}|{z}|{z}$$
$$mi,1mi,2mi,si$$
Với $s_{i} \ge 1$, và ở đâu $n_{i,j}$ xảy ra $m_{i,j} \ge 1$ lần, cho $j = 1, \dots  , s_{i}$, và có một cơ sở (basis) của $E$ sao cho ma trận $M$ của $f$ là ma trận khối (block matrix) của tạo thành
$$M = \begin{pmatrix} M_{1} & 0 & \cdots & 0 & 0 \\ 0 & M_{2} & \cdots & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & M_{\mu-1} & 0 \\ 0 & 0 & \cdots & 0 & M_{\mu} \end{pmatrix} ,$$
$$where each M_{j} is the companion matrix of some p_{i}^{ni,j}, and \mu  = \sum  m_{i,j}. The monic polyno-$$
Mials $p_{1}, \dots  , p_{t}$ và các số nguyên $r, t, n_{i,j}, s_{i}, m_{i,j}$ là một cách duy nhất được xác định các đa thức $p_{i}^{ni,j}$ được gọi là các ước sơ cấp (elementary divisors) của $f$ (và $M)$. các đa thức này là các nhân tử của đa thức tối tiểu (minimal polynomial). Ví dụ $1$ continued: Nhắc lại rằng f(x, $y, z, w) = (x + w, y + z, y + z, x + w)$ có hai không tầm thường các nhân tử bất biến (invariant factors) $q_{1} =$ x(x - $2) = q_{2}$. Do đó sơ cấp các nhân tử của $f$ là $p_{1} = x = p_{2}$ và $p_{3} = x$ - $2 = p_{4}$. Định lý 36.14 suy ra rằng
$$\mathbb{R}^{4}$$
$$= E_{1} \oplus E_{2} \oplus E_{3} \oplus E_{4},$$
