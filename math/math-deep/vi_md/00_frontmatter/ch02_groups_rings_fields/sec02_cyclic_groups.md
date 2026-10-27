# 2.2 Nhóm Cyclic (Cyclic Groups)

> **Trang gốc:** 44–47

Cho một nhóm $G$ với phần tử đơn vị $1$, với mọi phần tử $g \in G$ và với mọi số tự nhiên $n \in \mathbb{N}$, ta định nghĩa $g^n$ như sau:
$$\begin{aligned}
g^0 &= 1 \\
g^{n+1} &= g \cdot g^n.
\end{aligned}$$
<!-- PAGE 45 -->
Với mọi số nguyên $n \in \mathbb{Z}$, ta định nghĩa $g^n$ bởi
$$g^n = \begin{cases} g^n & \text{nếu } n \ge 0 \\ (g^{-1})^{(-n)} & \text{nếu } n < 0. \end{cases}$$
Các tính chất sau đây dễ dàng được kiểm chứng:
$$\begin{aligned}
g^i \cdot g^j &= g^{i+j} \\
(g^i)^{-1} &= g^{-i} \\
g^i \cdot g^j &= g^j \cdot g^i,
\end{aligned}$$
với mọi $i, j \in \mathbb{Z}$.

Định nghĩa tập con $\langle g \rangle$ của $G$ bởi
$$\langle g \rangle = \{g^n \mid n \in \mathbb{Z}\}.$$
Mệnh đề sau đây được dành làm bài tập.

> **Mệnh đề 2.14 (Proposition 2.14).** Cho một nhóm $G$, với mọi phần tử $g \in G$, tập hợp $\langle g \rangle$ là nhóm con Abel nhỏ nhất của $G$ chứa $g$.

> **Định nghĩa 2.13 (Definition 2.13).** Một nhóm $G$ được gọi là *nhóm cyclic* (*cyclic*) khi và chỉ khi tồn tại một phần tử $g \in G$ sao cho $G = \langle g \rangle$. Một phần tử $g \in G$ có tính chất này được gọi là một *phần tử sinh* (*generator*) của $G$.

Nhóm Klein bốn phần tử $V$ trong Ví dụ 2.7 là nhóm Abel, nhưng không phải là nhóm cyclic. Điều này là do $V$ có bốn phần tử, nhưng tất cả các phần tử khác phần tử đơn vị đều có cấp bằng $2$.

Các nhóm cyclic đều là các nhóm thương của $\mathbb{Z}$. Để chứng minh điều này, ta sử dụng một tính chất cơ bản của $\mathbb{Z}$. Nhắc lại rằng với mọi $n \in \mathbb{Z}$, ta dùng $n\mathbb{Z}$ để ký hiệu tập hợp các bội của $n$,
$$n\mathbb{Z} = \{nk \mid k \in \mathbb{Z}\}.$$

> **Mệnh đề 2.15 (Proposition 2.15).** Mọi nhóm con $H$ của $\mathbb{Z}$ đều có dạng $H = n\mathbb{Z}$ với một số tự nhiên $n \in \mathbb{N}$ nào đó.

*Chứng minh (Proof).* Nếu $H$ là nhóm tầm thường $\{0\}$, ta đặt $n = 0$. Nếu $H$ không tầm thường, thì với mọi phần tử khác không $m \in H$, ta cũng có $-m \in H$ và một trong hai số $m$ hoặc $-m$ phải dương; do đó gọi $n$ là số nguyên dương nhỏ nhất trong $H$. Theo Mệnh đề 2.14, $n\mathbb{Z}$ là nhóm con nhỏ nhất của $H$ chứa $n$. Với mọi $m \in H$ mà $m \neq 0$, ta có thể viết
$$m = nq + r, \quad \text{với } 0 \le r < n.$$
Bây giờ, vì $n\mathbb{Z} \subseteq H$ nên ta có $nq \in H$, và vì $m \in H$ nên ta suy ra $r = m - nq \in H$. Tuy nhiên, $0 \le r < n$, mâu thuẫn với tính nhỏ nhất của $n$ nếu $r > 0$, vì vậy $r = 0$, và $H = n\mathbb{Z}$. $\square$

<!-- PAGE 46 -->

Cho một nhóm cyclic bất kỳ $G$, với mọi phần tử sinh $g$ của $G$, ta có thể định nghĩa một ánh xạ $\phi : \mathbb{Z} \to G$ bởi $\phi(m) = g^m$. Vì $g$ sinh ra $G$ nên ánh xạ này là toàn ánh. Ánh xạ $\phi$ hiển nhiên là một đồng cấu nhóm; gọi $H = \operatorname{Ker} \phi$ là hạt nhân của nó. Theo nhận xét trước đó, $H = n\mathbb{Z}$ với một số $n \in \mathbb{Z}$ nào đó, do đó theo định lý đẳng cấu thứ nhất, ta thu được một đẳng cấu
$$\overline{\phi} : \mathbb{Z}/n\mathbb{Z} \longrightarrow G$$
từ nhóm thương $\mathbb{Z}/n\mathbb{Z}$ lên $G$. Hiển nhiên, nếu $G$ có cấp hữu hạn, thì $|G| = n$. Tóm lại, ta có kết quả sau đây.

> **Mệnh đề 2.16 (Proposition 2.16).** Mọi nhóm cyclic $G$ hoặc đẳng cấu với $\mathbb{Z}$, hoặc đẳng cấu với $\mathbb{Z}/n\mathbb{Z}$ với một số tự nhiên $n > 0$ nào đó. Trong trường hợp thứ nhất, ta nói $G$ là một *nhóm cyclic vô hạn* (*infinite cyclic group*), và trong trường hợp thứ hai, ta nói $G$ là một *nhóm cyclic cấp $n$* (*cyclic group of order $n$*).

Nhóm thương $\mathbb{Z}/n\mathbb{Z}$ bao gồm các lớp ghép $m + n\mathbb{Z} = \{m + nk \mid k \in \mathbb{Z}\}$, với $m \in \mathbb{Z}$, tức là các lớp tương đương của $\mathbb{Z}$ dưới quan hệ tương đương $\equiv$ được định nghĩa sao cho
$$x \equiv y \quad \text{khi và chỉ khi} \quad x - y \in n\mathbb{Z} \quad \text{khi và chỉ khi} \quad x \equiv y \pmod{n}.$$
Ta cũng ký hiệu lớp tương đương $x + n\mathbb{Z}$ của $x$ bởi $\overline{x}$, hoặc nếu muốn chính xác hơn thì bởi $[x]_n$. Phép toán nhóm được cho bởi
$$\overline{x} + \overline{y} = \overline{x + y}.$$
Với mọi $x \in \mathbb{Z}$, tồn tại một phần tử đại diện duy nhất, $x \bmod n$ (số dư không âm của phép chia $x$ cho $n$) trong lớp $\overline{x}$ của $x$, sao cho $0 \le x \bmod n \le n - 1$. Vì lý do này, ta thường đồng nhất $\mathbb{Z}/n\mathbb{Z}$ với tập hợp $\{0, \dots, n - 1\}$. Để chặt chẽ hơn, ta có thể trang bị cho $\{0, \dots, n - 1\}$ một cấu trúc nhóm bằng cách định nghĩa phép toán $+_n$ sao cho
$$x +_n y = (x + y) \bmod n.$$
Khi đó, dễ thấy rằng $\{0, \dots, n - 1\}$ cùng phép toán $+_n$ là một nhóm có phần tử đơn vị $0$ đẳng cấu với $\mathbb{Z}/n\mathbb{Z}$.

Ta cũng có thể định nghĩa một phép toán nhân $\cdot$ trên $\mathbb{Z}/n\mathbb{Z}$ như sau:
$$\overline{a} \cdot \overline{b} = \overline{ab} = \overline{ab \bmod n}.$$
Khi đó, dễ dàng kiểm tra được rằng $\cdot$ có tính giao hoán, tính kết hợp, rằng $\overline{1}$ là phần tử đơn vị đối với $\cdot$, và rằng $\cdot$ có tính phân phối (*distributive*) ở cả bên trái lẫn bên phải đối với phép cộng. Điều này làm cho $\mathbb{Z}/n\mathbb{Z}$ trở thành một vành giao hoán (*commutative ring*). Ta thường lược bỏ dấu chấm và viết $\overline{a}\,\overline{b}$ thay vì $\overline{a} \cdot \overline{b}$.

> **Mệnh đề 2.17 (Proposition 2.17).** Cho số nguyên bất kỳ $n \ge 1$, với mọi $a \in \mathbb{Z}$, lớp thặng dư $\overline{a} \in \mathbb{Z}/n\mathbb{Z}$ khả nghịch đối với phép nhân khi và chỉ khi $\gcd(a, n) = 1$.

<!-- PAGE 47 -->

*Chứng minh (Proof).* Nếu $\overline{a}$ có nghịch đảo là $\overline{b}$ trong $\mathbb{Z}/n\mathbb{Z}$, thì $\overline{a}\,\overline{b} = \overline{1}$, nghĩa là
$$ab \equiv 1 \pmod{n},$$
tức là $ab = 1 + nk$ với một số $k \in \mathbb{Z}$ nào đó; đây chính là đẳng thức Bézout (*Bézout identity*)
$$ab - nk = 1$$
và suy ra $\gcd(a, n) = 1$. Ngược lại, nếu $\gcd(a, n) = 1$, thì theo đẳng thức Bézout tồn tại $u, v \in \mathbb{Z}$ sao cho
$$au + nv = 1,$$
do đó $au = 1 - nv$, nghĩa là
$$au \equiv 1 \pmod{n},$$
tức là $\overline{a}\,\overline{u} = \overline{1}$, vậy $\overline{a}$ khả nghịch trong $\mathbb{Z}/n\mathbb{Z}$. $\square$

> **Định nghĩa 2.14 (Definition 2.14).** Nhóm (dưới phép nhân) gồm các phần tử khả nghịch của vành $\mathbb{Z}/n\mathbb{Z}$ được ký hiệu bởi $(\mathbb{Z}/n\mathbb{Z})^*$. Lưu ý rằng nhóm này là nhóm Abel và chỉ được định nghĩa khi $n \ge 2$.

Hàm $\phi$ Euler (*Euler $\phi$-function*) đóng một vai trò quan trọng trong lý thuyết về các nhóm $(\mathbb{Z}/n\mathbb{Z})^*$.

> **Định nghĩa 2.15 (Definition 2.15).** Cho số nguyên dương bất kỳ $n \ge 1$, *hàm $\phi$ Euler* (*Euler $\phi$-function* hay *Euler totient function*) được định nghĩa sao cho $\phi(n)$ là số lượng các số nguyên $a$, với $1 \le a \le n$, nguyên tố cùng nhau (*relatively prime*) với $n$; nghĩa là thỏa mãn $\gcd(a, n) = 1$.[^1]

Khi đó, theo Mệnh đề 2.17, ta thấy rằng nhóm $(\mathbb{Z}/n\mathbb{Z})^*$ có cấp bằng $\phi(n)$.

Với $n = 2$, $(\mathbb{Z}/2\mathbb{Z})^* = \{1\}$, tức nhóm tầm thường. Với $n = 3$, $(\mathbb{Z}/3\mathbb{Z})^* = \{1, 2\}$, và với $n = 4$, ta có $(\mathbb{Z}/4\mathbb{Z})^* = \{1, 3\}$. Cả hai nhóm này đều đẳng cấu với nhóm $\{-1, 1\}$. Vì $\gcd(a, n) = 1$ với mọi $a \in \{1, \dots, n - 1\}$ khi và chỉ khi $n$ là số nguyên tố, nên theo Mệnh đề 2.17 ta thấy rằng $(\mathbb{Z}/n\mathbb{Z})^* = \mathbb{Z}/n\mathbb{Z} - \{0\}$ khi và chỉ khi $n$ là số nguyên tố.

[^1]: Chúng ta cho phép $a = n$ để bao hàm cả trường hợp đặc biệt $n = 1$.
