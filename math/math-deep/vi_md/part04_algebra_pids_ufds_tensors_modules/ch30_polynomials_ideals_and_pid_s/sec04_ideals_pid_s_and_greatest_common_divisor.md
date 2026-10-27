# Các lý tưởng, PID's, và Lớn nhất Chung/phổ biến Các ước


<!-- PAGE 1076 -->

## 30.4 Các lý tưởng, PID’s, và Lớn nhất Chung/phổ biến Các ước

Thứ nhất, ta giới thiệu cơ bản khái niệm của lý tưởng (ideal).

> **Định nghĩa 30.4.** Cho trước vành $A$, lý tưởng (ideal) của $A$ là bất kỳ khác rỗng tập con $\mathfrak{I}$ của $A$ thỏa mãn sau đây hai các tính chất:
(ID1) Nếu, $b \in \mathfrak{I}$, thì $b$ - $a \in \mathfrak{I}$.
(ID2) Nếu $a \in \mathfrak{I}$, thì ax $\in \mathfrak{I}$ với mọi $x \in A$. lý tưởng (ideal) $\mathfrak{I}$ là chính lý tưởng (ideal) nếu tồn tại một $a \in \mathfrak{I}$, được gọi là phần tử sinh, sao cho
$$\mathfrak{I} = {ax | x \in A}.$$
Đẳng thức $\mathfrak{I} = {ax$ | $x \in A}$ cũng được viết như $\mathfrak{I} =$ aA hoặc như $\mathfrak{I} = (a)$. lý tưởng (ideal) $\mathfrak{I} = (0) = {0}$ được gọi là null lý tưởng (ideal) (hoặc không lý tưởng (ideal)). lý tưởng (ideal) $\mathfrak{I}$ là lý tưởng cực đại (maximal ideal) nếu $\mathfrak{I} \neq  A$ và với mọi lý tưởng (ideal) $\mathfrak{J} \neq  A$, nếu $\mathfrak{I} \subseteq \mathfrak{J}$, thì $\mathfrak{J} = \mathfrak{I}$. lý tưởng (ideal) $\mathfrak{I}$ là lý tưởng nguyên tố (prime ideal) nếu $\mathfrak{I} \neq  A$ và nếu ab $\in \mathfrak{I}$, thì $a \in \mathfrak{I}$ hoặc $b \in \mathfrak{I}$, với mọi, $b \in A. Equivalently,\mathfrak{I}$ là lý tưởng nguyên tố (prime ideal) $if\mathfrak{I} \neq  A$ và nếu, $b \in A -\mathfrak{I}$, thì ab $\in A -\mathfrak{I}$, với mọi, $b \in A$. Nói cách khác, $A$ - $\mathfrak{I}$ là đóng dưới phép nhân và $1 \in A$ - $\mathfrak{I}$. Lưu ý rằng $if\mathfrak{I}$ là lý tưởng (ideal), $then\mathfrak{I} = A$ iff1 $\in \mathfrak{I}$. Vì theo Định nghĩa, $ideal\mathfrak{I}$ là khác rỗng, tồn tại một $a \in \mathfrak{I}$, và bởi (ID1) ta thu được $0 = a$ - $a \in \mathfrak{I}$. Thì, với mọi $a \in \mathfrak{I}$, vì $0 \in \mathfrak{I}$, bởi (ID1) ta thu được $-a \in \mathfrak{I}$. Do đó, lý tưởng (ideal) là additive nhóm con của $A$. Bởi vì của (ID2), lý tưởng (ideal) là cũng vành con. Nhận thấy rằng nếu $A$ là trường, thì $A$ chỉ có hai các lý tưởng, cụ thể là, tầm thường lý tưởng (ideal) $(0)$ và $A$ chính nó. Thật vậy, nếu $\mathfrak{I} \neq  (0)$, bởi vì mọi khác không phần tử có nghịch đảo, thì $1 \in \mathfrak{I}$, và do đó, $\mathfrak{I} = A$.

> **Định nghĩa 30.5.** Cho trước vành $A$, với mọi hai các phần tử, $b \in A$ ta nói rằng $b$ là bội của và rằng chia hết $b$ nếu $b =$ ac với một số $c \in A$; điều này thường được ký hiệu bởi | $b$. Lưu ý rằng chính lý tưởng (ideal) () là tập hợp tất cả các bội của, và rằng chia hết $b$ khi và chỉ khi $b$ là bội của khi và chỉ khi $b \in$ () khi và chỉ khi(b) $\subseteq$ (). Lưu ý rằng mọi $a \in A$ chia hết $0$. Tuy nhiên, nó là thông lệ đến nói rằng là không ước khi và chỉ khi ac $= 0$ với một số $c \neq  0$. Với điều này quy ước, $0$ là không ước trừ khi $A = {0}$ (tầm thường vành), và $A$ là miền nguyên (integral domain) iff0 là chỉ không ước trong $A$. Cho trước, $b \in A$ với, $b \neq  0$, nếu $(a) = (b)$ thì ở đó tồn tại $c, d \in A$ sao cho $a =$ bc và $b =$ ad. Từ điều này, ta thu được $a =$ adc và $b =$ bcd, nghĩa là, (1 -dc) $= 0$ và b(1 -cd) $= 0$. Nếu $A$ là miền nguyên (integral domain), ta thu được dc $= 1$ và cd $= 1$, nghĩa là, $c$ là khả nghịch với nghịch đảo $d$. Do đó, khi $A$ là miền nguyên (integral domain), ta có $b =$ ad, với $d$ khả nghịch. điều ngược lại là hiển nhiên, nếu $b =$ ad với $d$ khả nghịch, thì $(a) = (b)$. Nó là worth recording sự kiện này như sau đây mệnh đề.

<!-- PAGE 1077 -->

> **Mệnh đề 30.5.** Nếu $A$ là miền nguyên (integral domain), với mọi, $b \in A$ với, b̸ $= 0$, ta có
$(a) = (b)$ khi và chỉ khi tồn tại một khả nghịch $d \in A$ sao cho $b =$ ad. khả nghịch phần tử $u \in A$ cũng được gọi là một unit. Cho trước hai các lý tưởng $\mathfrak{I}$ và $\mathfrak{J}$, tổng của chúng
$$\mathfrak{I} +\mathfrak{J} = {a + b | a \in \mathfrak{I}, b \in \mathfrak{J}}$$
Là rõ ràng lý tưởng (ideal). Cho trước bất kỳ khác rỗng tập con $J$ của $A$, tập hợp
$${a_{1}x_{1} + \cdots  + a_{n}x_{n} | x_{1}, \dots  , x_{n} \in A, a_{1}, \dots  , a_{n} \in J, n \ge 1}$$
Là dễ dàng được thấy là lý tưởng (ideal), và thực ra, nó là nhỏ nhất lý tưởng (ideal) chứa $J$. Nó thường được ký hiệu bởi $(J)$. Các lý tưởng đóng rất quan trọng vai trò trong study của các vành. Chúng tiến tới để chỉ ra lên everywhere. Ví dụ, chúng phát sinh một cách tự nhiên từ các đồng cấu.

> **Mệnh đề 30.6.** Cho trước bất kỳ vành đồng cấu $h: A \to B$, hạt nhân (kernel) Ker $h = {a \in A$ | h() $= 0}$ của $h$ là lý tưởng (ideal).

*Chứng minh.* Cho trước, $b \in A$, ta có, $b \in$ Ker $h$ khi và chỉ khi h() $=$ h(b) $= 0$, và vì $h$ là đồng cấu, ta thu được
$$h(b -a) = h(b) -h(a) = 0,$$
Và
$$h(ax) = h(a)h(x) = 0$$
Với mọi $x \in A$, mà chỉ ra rằng Ker $h$ là lý tưởng (ideal). Có một sort của điều ngược lại tính chất. Cho trước vành $A$ và lý tưởng (ideal) $\mathfrak{I} \subseteq A$, ta có thể định nghĩa thương vành $A/\mathfrak{I}$, và có một toàn ánh (surjective) đồng cấu $\pi$: $A \to A/\mathfrak{I}$ có hạt nhân (kernel) là một cách chính xác $\mathfrak{I}$.

> **Mệnh đề 30.7.** Cho trước bất kỳ vành $A$ và bất kỳ lý tưởng (ideal) $\mathfrak{I} \subseteq A$, quan hệ tương đương (equivalence relation) $\equiv_{I}$ được định nghĩa bởi $a \equiv_{I}  b$ khi và chỉ khi $b$ - $a \in \mathfrak{I}$ là congruence, mà có nghĩa là nếu $a_{1} \equiv_{I}  b_{1}$ và $a_{2} \equiv_{I}  b_{2}$, thì $1. a_{1} + a_{2} \equiv_{I}  b_{1} + b_{2}$, và $2. a_{1}a_{2} \equiv_{I}  b_{1}b_{2}$. Thì, tập hợp $A/\mathfrak{I}$ của các lớp tương đương modulo $\mathfrak{I}$ là vành dưới các phép toán
$$[a] + [b]=[a + b]$$
$$[a][b]=[ab].$$
Ánh xạ $\pi$: $A \to A/\mathfrak{I}$ sao cho $\pi (a) = [a]$ là toàn ánh (surjective) đồng cấu có hạt nhân (kernel) là một cách chính xác $\mathfrak{I}$.

<!-- PAGE 1078 -->

*Chứng minh.* Everything là trực tiếp/dễ dàng. Ví dụ, nếu $a_{1} \equiv_{I}  b_{1}$ và $a_{2} \equiv_{I}  b_{2}$, thì $b_{1} -a_{1} \in \mathfrak{I}$ và $b_{2}$ - $a_{2} \in \mathfrak{I}$. Vì $\mathfrak{I}$ là lý tưởng (ideal), ta thu được
$$(b_{1} -a_{1})b_{2} = b_{1}b_{2} -a_{1}b_{2} \in \mathfrak{I}$$
Và
$$(b_{2} -a_{2})a_{1} = a_{1}b_{2} -a_{1}a_{2} \in \mathfrak{I}.$$
Vì $\mathfrak{I}$ là lý tưởng (ideal), và do đó, additive nhóm, ta thu được
$$b_{1}b_{2} -a_{1}a_{2} \in \mathfrak{I},$$
I.e., $a_{1}a_{2} \equiv_{I}  b_{1}b_{2}$. đẳng thức Ker $\pi  =\mathfrak{I}$ nghiệm đúng bởi vì $\mathfrak{I}$ là lý tưởng (ideal).

> **Ví dụ 30.1.** $1$. Trong vành $\mathbb{Z}$, với mọi $p \in \mathbb{Z}$, subroup $p\mathbb{Z}$ là lý tưởng (ideal), và $\mathbb{Z}/p\mathbb{Z}$ là vành, vành của residues modulo $p$. vành này là trường khi và chỉ khi $p$ là nguyên tố số. $2$. thương của đa thức vành $\mathbb{R}[X]$ bởi lý tưởng nguyên tố (prime ideal) $\mathfrak{I}$ là miền nguyên (integral domain). $3$. thương của đa thức $ring\mathbb{R}[X]$ bởi cực đại $ideal\mathfrak{I}$ là trường. Ví dụ, nếu $\mathfrak{I} = (X^{2} + 1)$, chính lý tưởng (ideal) được sinh bởi $X^{2} + 1$ (mà là thật vậy cực đại
$$\mathbb{R}  \sim \mathbb{C}$$
Lý tưởng (ideal) vì $X^{2} + 1$ có không có thực các nghiệm), thì $[X]/(X^{2} + 1) =$. sau đây mệnh đề cho ta đặc trưng của nguyên tố các lý tưởng và cực đại các lý tưởng theo các thương.

> **Mệnh đề 30.8.** Cho trước vành $A$, với mọi lý tưởng (ideal) $\mathfrak{I} \subseteq A$, các tính chất sau đây đúng.
$(1)$ lý tưởng (ideal) $\mathfrak{I}$ là lý tưởng nguyên tố (prime ideal) khi và chỉ khi $A/\mathfrak{I}$ là miền nguyên (integral domain).
$(2)$ lý tưởng (ideal) $\mathfrak{I}$ là lý tưởng cực đại (maximal ideal) khi và chỉ khi $A/\mathfrak{I}$ là trường.

*Chứng minh.* $(1)$ Giả sử $that\mathfrak{I}$ là lý tưởng nguyên tố (prime ideal). $Since\mathfrak{I}$ là $prime,\mathfrak{I} \neq  A$, và do đó, $A/\mathfrak{I}$ là không tầm thường vành $(0)$. Nếu [][b] $= 0$, vì [][b] $=$ [ab], ta có ab $\in \mathfrak{I}$, và vì $\mathfrak{I}$ là nguyên tố, thì hoặc $a \in \mathfrak{I}$ hoặc $b \in \mathfrak{I}$, sao cho hoặc $[a] = 0$ hoặc $[b] = 0$. Do đó, $A/\mathfrak{I}$ là miền nguyên (integral domain). Ngược lại, giả sử rằng $A/\mathfrak{I}$ là miền nguyên (integral domain). Vì $A/\mathfrak{I}$ là không tầm thường vành, $\mathfrak{I} \neq  A$. Giả sử rằng ab $\in \mathfrak{I}$. Thì, ta có
$$\pi (ab) = \pi (a)\pi (b) = 0,$$
Mà suy ra rằng hoặc $\pi (a) = 0$ hoặc $\pi (b) = 0$, vì $A/\mathfrak{I}$ là miền nguyên (integral domain) (ở đâu $\pi$: $A \to A/\mathfrak{I}$ là thương ánh xạ). Do đó, hoặc $a \in \mathfrak{I}$ hoặc $b \in \mathfrak{I}$, và $\mathfrak{I}$ là lý tưởng nguyên tố (prime ideal).

<!-- PAGE 1079 -->
$(2)$ Giả sử rằng $\mathfrak{I}$ là lý tưởng cực đại (maximal ideal). Như trong $(1), A/\mathfrak{I}$ là không tầm thường vành $(0)$. Cho $[a] \neq  0$ trong $A/\mathfrak{I}$. Ta cần để chứng minh rằng [] có multiplicative nghịch đảo. Vì $[a] \neq  0$, ta có $a \in / \mathfrak{I}$. Cho $\mathfrak{I}_{a}$ là lý tưởng (ideal) được sinh bởi $\mathfrak{I}$ và. Ta có
$$\mathfrak{I} \subseteq \mathfrak{I}_{a}and\mathfrak{I} \neq \mathfrak{I}_{a},$$
Vì $a \in / \mathfrak{I}$, và vì $\mathfrak{I}$ là cực đại, điều này suy ra rằng
$$\mathfrak{I}_{a} = A.$$
Tuy nhiên, ta biết rằng
$$\mathfrak{I}_{a} = {ax + h | x \in A, h \in \mathfrak{I}},$$
Và do đó, tồn tại một $x \in A$ sao cho
$$ax + h = 1,$$
Mà chứng tỏ rằng [][x] $= [1]$, như mong muốn. Ngược lại, giả sử rằng $A/\mathfrak{I}$ là trường. Một lần nữa, vì $A/\mathfrak{I}$ là không tầm thường vành, $\mathfrak{I} \neq  A$. Cho $\mathfrak{J}$ là bất kỳ lý tưởng thực sự (proper ideal) sao cho $\mathfrak{I} \subseteq \mathfrak{J}$, và giả sử rằng $\mathfrak{I} \neq  \mathfrak{J}$. Do đó, tồn tại một $j \in \mathfrak{J}$ - $\mathfrak{I}$, và vì Ker $\pi  = \mathfrak{I}$, ta có $\pi (j) \neq  0$. Vì $A/\mathfrak{I}$ là trường và $\pi$ là toàn ánh (surjective), tồn tại một $k \in A$ sao cho $\pi (j)\pi (k) = 1$, mà suy ra rằng
$$jk -1 = i$$
Với một số $i \in \mathfrak{I}$, và vì $\mathfrak{I} \subset \mathfrak{J}$ và $\mathfrak{J}$ là lý tưởng (ideal), suy ra rằng $1 =$ jk - $i \in \mathfrak{J}$, chỉ ra rằng $\mathfrak{J} = A$, một mâu thuẫn. Vì vậy, $\mathfrak{I} =\mathfrak{J}$, và $\mathfrak{I}$ là lý tưởng cực đại (maximal ideal). Như hệ quả, ta thu được kết quả sau hữu ích kết quả. Nó emphasizes importance của cực đại các lý tưởng.

> **Hệ quả 30.9.** Cho trước bất kỳ vành $A$, mọi lý tưởng cực đại (maximal ideal) $\mathfrak{I}$ trong $A$ là lý tưởng nguyên tố (prime ideal).

*Chứng minh.* Nếu $\mathfrak{I}$ là lý tưởng cực đại (maximal ideal), thì, theo Mệnh đề 30.8, thương vành $A/\mathfrak{I}$ là trường. Tuy nhiên, trường là miền nguyên (integral domain), và theo Mệnh đề 30.8 $(again),\mathfrak{I}$ là lý tưởng nguyên tố (prime ideal). Nhận thấy rằng vành $A$ là miền nguyên (integral domain) khi và chỉ khi(0) là lý tưởng nguyên tố (prime ideal). Điều này là ví dụ của lý tưởng nguyên tố (prime ideal) mà là không lý tưởng cực đại (maximal ideal), như ngay lập tức được thấy trong $A =\mathbb{Z}$, ở đâu $(p)$ là lý tưởng cực đại (maximal ideal) với mọi nguyên tố số $p$.  $A$ ít hơn hiển nhiên ví dụ của lý tưởng nguyên tố (prime ideal) mà là không lý tưởng cực đại (maximal ideal) là lý tưởng (ideal) $(X)$ trong vành của các đa thức $\mathbb{Z}[X]$. Thật vậy, $(X, 2)$ là cũng lý tưởng nguyên tố (prime ideal), nhưng $(X)$ là một cách thực sự/đúng đắn được chứa trong $(X, 2)$. lý tưởng (ideal) $(X)$ là tập hợp tất cả các đa thức của tạo thành XQ(X) với mọi Q(X) $\in \mathbb{Z}[X]$, nói cách khác tập hợp tất cả các đa thức $in\mathbb{Z}[X]$ với hằng số số hạng bằng $0$, và lý tưởng (ideal) $(X, 2)$ là tập hợp tất cả các đa thức của tạo thành
$$XQ_{1}(X) + 2Q_{2}(X),Q_{1}(X), Q_{2}(X) \in \mathbb{Z}[X],$$

<!-- PAGE 1080 -->
Mà là chỉ tập hợp tất cả các đa thức trong $\mathbb{Z}[X]$ có hằng số số hạng là của tạo thành 2c với một số $c \in \mathbb{Z}$. lý tưởng (ideal) $(X)$ là thật vậy một cách thực sự/đúng đắn được chứa trong lý tưởng (ideal) $(X, 2)$. Nếu P(X)Q(X) $\in (X, 2)$, cho là hằng số số hạng trong P(X) và cho $b$ là hằng số số hạng trong Q(X). Vì P(X)Q(X) $\in (X, 2)$, ta phải có ab $=$ 2c với một số $c \in \mathbb{Z}$, và vì $2$ là nguyên tố, hoặc là chia hết bởi $2$ hoặc $b$ là chia hết bởi $2$. Suy ra rằng hoặc P(X) $\in (X, 2)$ hoặc Q(X) $\in (X, 2)$, mà chỉ ra rằng $(X, 2)$ là lý tưởng nguyên tố (prime ideal).

> **Định nghĩa 30.6.** miền nguyên (integral domain) trong mà mọi lý tưởng (ideal) là chính lý tưởng (ideal) được gọi là một chính vành hoặc miền nguyên lý tưởng chính (PID), cho ngắn, PID. vành $\mathbb{Z}$ là PID. Điều này là hệ quả của sự tồn tại của (Euclidean) phép chia thuật toán. Như ta sẽ xem tiếp theo, khi $K$ là trường, vành K[X] là cũng chính vành.  Tuy nhiên, khi $n \ge 2$, vành $K[X_{1}, \dots  , X_{n}]$ là không chính. Ví dụ, trong vành K[X, $Y$ ], lý tưởng (ideal) $(X, Y$) được sinh bởi $X$ và $Y$ là không chính. Thứ nhất, vì $(X, Y$) là tập hợp tất cả các đa thức của tạo thành $Xq_{1} + Y q_{2}$, ở đâu $q_{1}, q_{2} \in$ K[X, $Y$ ], ngoại trừ khi $Xq_{1} + Y q_{2} = 0$, ta có $deg(Xq_{1} + Y q_{2}) \ge 1$. Do đó, $1 \in / (X, Y$). Bây giờ nếu ở đó đã là một số $p \in$ K[X, $Y$ ] sao cho $(X, Y$) $= (p)$, vì $1 \in / (X, Y$), ta phải có deg(p) $\ge 1$. Nhưng ta sẽ cũng có $X = pq_{1}$ và $Y = pq_{2}$, với một số $q_{1}, q_{2} \in$ K[X, $Y$ ]. Vì deg(X) $=$ deg(Y) $= 1$, điều này là không thể. Chẵn/ngay cả dù K[X, $Y$ ] là không chính vành, phù hợp phiên bản của duy nhất nhân tử hóa theo bất khả quy (irreducible) các nhân tử nghiệm đúng. vành K[X, $Y$ ] (và tổng quát hơn $K[X_{1}, \dots  , X_{n}])$ là những gì được gọi là một miền nhân tử hóa duy nhất (UFD), cho ngắn, UFD, hoặc giai thừa vành. Từ điều này điểm cho đến khi Định nghĩa 30.11, ta xét các đa thức trong một biến trên trường $K$.
Nhận xét: Mặc dù ta đã được chứng minh phần $(1)$ của Mệnh đề 30.10 trong nhiều hơn/thêm tổng quát tình huống ở trên, ta reprove nó trong trường hợp đặc biệt của các đa thức. Điều này có thể offend purists, nhưng hầu hết độc giả sẽ probably không mind.

> **Mệnh đề 30.10.** Cho $K$ là trường. Các tính chất sau đây đúng:
$(1)$ Với mọi hai khác không các đa thức $f, g \in$ K[X], $(f) = (g)$ khi và chỉ khi tồn tại một $\lambda  \neq  0$ trong $K$ sao cho $g = \lambda f$.
$(2)$ Với mọi khác không lý tưởng (ideal) $\mathfrak{I}$ trong K[X], tồn tại duy nhất một chuẩn hóa (monic) đa thức $f \in$ K[X] sao cho $\mathfrak{I} = (f)$.

*Chứng minh.* $(1)$ Nếu $(f) = (g)$, có một số khác không các đa thức $q_{1}, q_{2} \in$ K[X] sao cho $g = fq_{1}$ và $f = gq_{2}$. Do đó, ta có $f = fq_{1}q_{2}$, mà suy ra f(1 - $q_{1}q_{2}) = 0$. Vì $K$ là trường, theo Mệnh đề 30.1, K[X] có không có không ước, và vì ta được giả sử $f \neq  0$, ta phải có $q_{1}q_{2} = 1$. Tuy nhiên, nếu hoặc $q_{1}$ hoặc $q_{2}$ là không hằng số, theo Mệnh đề 30.1 một lần nữa, $deg(q_{1}q_{2}) = deg(q_{1}) + deg(q_{2}) \ge 1$, contradicting $q_{1}q_{2} = 1$, vì deg(1) $= 0$. Do đó, cả hai $q_{1}, q_{2} \in K -{0}$, và $(1)$ nghiệm đúng với $\lambda  = q_{1}$. Trong khác hướng, hiển nhiên là $g = \lambda f$ suy ra rằng $(f) = (g)$.

<!-- PAGE 1081 -->
$(2)$ Vì ta là giả sử $that\mathfrak{I}$ là không null lý tưởng (ideal), tồn tại một đa thức của nhỏ nhất bậc trong $\mathfrak{I}$, và vì $K$ là trường, bởi phù hợp phép nhân bởi vô hướng (scalar), ta có thể tạo sure rằng đa thức này là chuẩn hóa (monic). Do đó, cho $f$ là chuẩn hóa (monic) đa thức của nhỏ nhất bậc trong $\mathfrak{I}$. Bởi (ID2), rõ ràng là $(f) \subseteq \mathfrak{I}$. Bây giờ, cho $g \in \mathfrak{I}$. Bằng cách sử dụng Euclidean thuật toán, ở đó tồn tại duy nhất $q, r \in$ K[X] sao cho
$$g = qf + randdeg(r) < deg(f).$$
Nếu r̸ $= 0$, tồn tại một $\lambda$ ̸ $= 0$ trong $K$ sao cho $\lambda r$ là chuẩn hóa (monic) đa thức, và vì $\lambda r = \lambda g$ - $\lambda$ qf, với $f, g \in \mathfrak{I}$, bởi (ID1) và (ID2), ta có $\lambda r \in \mathfrak{I}$, ở đâu $deg(\lambda r) <$ deg(f) và $\lambda r$ là chuẩn hóa (monic) đa thức, contradicting minimality của bậc của $f$. Do đó, $r = 0$, và $g \in (f)$. tính duy nhất của chuẩn hóa (monic) đa thức $f$ suy ra từ $(1)$. Mệnh đề 30.10 chỉ ra rằng K[X] là chính vành khi $K$ là trường. Ta bây giờ investigate sự tồn tại của lớn nhất chung/phổ biến ước (ước chung lớn nhất (gcd)) cho hai khác không các đa thức. Cho trước bất kỳ hai khác không các đa thức $f, g \in$ K[X], nhắc lại rằng $f$ chia hết $g$ nếu $g =$ fq với một số $q \in$ K[X].

> **Định nghĩa 30.7.** Cho trước bất kỳ hai khác không các đa thức $f, g \in$ K[X], đa thức $d \in$ K[X] là lớn nhất chung/phổ biến ước của $f$ và $g$ (cho ngắn, ước chung lớn nhất (gcd) của $f$ và $g)$ nếu $d$ chia hết $f$ và $g$ và bất cứ khi nào $h \in$ K[X] chia hết $f$ và $g$, thì $h$ chia hết $d$. Ta nói rằng $f$ và $g$ là một cách tương đối nguyên tố nếu $1$ là ước chung lớn nhất (gcd) của $f$ và $g$. Lưu ý rằng $f$ và $g$ là một cách tương đối nguyên tố khi và chỉ khi tất cả của của chúng ước chung lớn nhất (gcd)’s là các hằng số (các vô hướng trong $K)$, hoặc tương đương, nếu $f, g$ có không có ước $q$ của bậc deg(q) $\ge 1$.  Đặc biệt, lưu ý rằng $f$ và $g$ là một cách tương đối nguyên tố khi $f$ là khác không hằng số đa thức (vô hướng (scalar) $\lambda  \neq  0$ trong $K)$ và $g$ là bất kỳ khác không đa thức. Ta có thể đặc trưng hóa ước chung lớn nhất (gcd)’s của các đa thức như sau.

> **Mệnh đề 30.11.** Cho $K$ là trường và cho $f, g \in$ K[X] là bất kỳ hai khác không các đa thức. Với mọi đa thức $d \in$ K[X], các tính chất sau đây là tương đương:
$(1)$ đa thức $d$ là ước chung lớn nhất (gcd) của $f$ và $g$.
$(2)$ đa thức $d$ chia hết $f$ và $g$ và ở đó tồn tại $u, v \in$ K[X] sao cho
$$d = uf + vg.$$
$(3)$ các lý tưởng $(f), (g)$, và $(d)$ thỏa mãn phương trình
$$(d) = (f) + (g).$$
Ngoài ra, $d \neq  0$, và $d$ là duy nhất sai khác phép nhân bởi khác không vô hướng (scalar) trong $K$.

<!-- PAGE 1082 -->

*Chứng minh.* Cho trước bất kỳ hai khác không các đa thức $u, v \in$ K[X], nhận thấy rằng $u$ chia hết $v$ khi và chỉ khi(v) $\subseteq (u)$. Bây giờ, $(2)$ có thể được restated như $(f) \subseteq (d), (g) \subseteq (d)$, và $d \in (f) + (g)$, mà là tương đương đến
$(d) = (f) + (g)$, cụ thể là $(3)$. Nếu $(2)$ nghiệm đúng, vì $d =$ uf $+$ vg, bất cứ khi nào $h \in$ K[X] chia hết $f$ và $g$, thì $h$ chia hết $d$, và $d$ là ước chung lớn nhất (gcd) của $f$ và $g$. Giả sử rằng $d$ là ước chung lớn nhất (gcd) của $f$ và $g$. Thì, vì $d$ chia hết $f$ và $d$ chia hết $g$, ta có
$(f) \subseteq (d)$ và $(g) \subseteq (d)$, và do đó $(f) + (g) \subseteq (d)$, và $(f) + (g)$ là khác rỗng vì $f$ và $g$ là khác không. Theo Mệnh đề 30.10, tồn tại một chuẩn hóa (monic) đa thức $d_{1} \in$ K[X] sao cho $(d_{1}) = (f) + (g)$. Thì, $d_{1}$ chia hết cả hai $f$ và $g$, và vì $d$ là ước chung lớn nhất (gcd) của $f$ và $g$, thì $d_{1}$ chia hết $d$, mà chỉ ra rằng $(d) \subseteq (d_{1}) = (f) + (g)$. Hệ quả là, $(f) + (g) = (d)$, và $(3)$ nghiệm đúng. Vì $(d) = (f) + (g)$ và $f$ và $g$ là khác không, phần cuối cùng của mệnh đề là hiển nhiên. Hệ quả là của Mệnh đề 30.11, hai khác không các đa thức $f, g \in$ K[X] là một cách tương đối nguyên tố khi và chỉ khi ở đó tồn tại $u, v \in$ K[X] sao cho
$$uf + vg = 1.$$
Đồng nhất thức
$$d = uf + vg$$
Của phần $(2)$ của Mệnh đề 30.11 là thường được gọi là Bezout đồng nhất thức. Ta derive nhiều hơn/thêm hữu ích các hệ quả của Mệnh đề 30.11.

> **Mệnh đề 30.12.** Cho $K$ là trường và cho $f, g \in$ K[X] là bất kỳ hai khác không các đa thức. Với mọi ước chung lớn nhất (gcd) $d \in$ K[X] của $f$ và $g$, các tính chất sau đây đúng:
$(1)$ Với mọi khác không đa thức $q \in$ K[X], đa thức dq là ước chung lớn nhất (gcd) của fq và gq.
$(2)$ Với mọi khác không đa thức $q \in$ K[X], nếu $q$ chia hết $f$ và $g$, thì $d/q$ là ước chung lớn nhất (gcd) của $f/q$ và $g/q$.

*Chứng minh.* $(1)$ Theo Mệnh đề 30.11 $(2), d$ chia hết $f$ và $g$, và ở đó tồn tại $u, v \in$ K[X], sao cho
$$d = uf + vg.$$
Thì, dq chia hết fq và gq, và
$$dq = ufq + vgq.$$
Theo Mệnh đề 30.11 $(2)$, dq là ước chung lớn nhất (gcd) của fq và gq. chứng minh của $(2)$ là đồng dạng. sau đây mệnh đề được sử dụng thường.

<!-- PAGE 1083 -->

> **Mệnh đề 30.13.** (Euclid’s mệnh đề) Cho $K$ là trường và cho $f, g, h \in$ K[X] là bất kỳ khác không các đa thức. Nếu $f$ chia hết gh và $f$ là một cách tương đối nguyên tố đến $g$, thì $f$ chia hết $h$.

*Chứng minh.* Từ Mệnh đề 30.11, $f$ và $g$ là một cách tương đối nguyên tố khi và chỉ khi ở đó tồn tại một số các đa thức $u, v \in$ K[X] sao cho
$$uf + vg = 1.$$
Thì, ta có
$$ufh + vgh = h,$$
Và vì $f$ chia hết gh, nó chia hết cả hai ufh và vgh, và do đó, $f$ chia hết $h$.

> **Mệnh đề 30.14.** Cho $K$ là trường và cho $f, g_{1}, \dots  , g_{m} \in$ K[X] là một số khác không các đa thức. Nếu $f$ và $g_{i}$ là một cách tương đối nguyên tố với mọi $i, 1 \le i \le m$, thì $f$ và $g_{1} \cdots  g_{m}$ là một cách tương đối nguyên tố.

*Chứng minh.* Ta tiến hành bằng quy nạp theo $m$. trường hợp $m = 1$ là tầm thường. Cho $h = g_{2} \cdots  g_{m}$. Theo giả thiết quy nạp, $f$ và $h$ là một cách tương đối nguyên tố. Cho $d$ là ước chung lớn nhất (gcd) của $f$ và $g_{1}h$. Ta khẳng định rằng $d$ là một cách tương đối nguyên tố đến $g_{1}$. Ngược lại, $d$ và $g_{1}$ sẽ có một số nonconstant ước chung lớn nhất (gcd) $d_{1}$ mà sẽ chia cả hai $f$ và $g_{1}$, contradicting sự kiện rằng $f$ và $g_{1}$ là một cách tương đối nguyên tố. Bây giờ, theo Mệnh đề 30.13, vì $d$ chia hết $g_{1}h$ và $d$ và $g_{1}$ là một cách tương đối nguyên tố, $d$ chia hết $h = g_{2} \cdots  g_{m}$. Nhưng khi đó, $d$ là ước của $f$ và $h$, và vì $f$ và $h$ là một cách tương đối nguyên tố, $d$ phải là hằng số, và $f$ và $g_{1} \cdots  g_{m}$ là một cách tương đối nguyên tố. Định nghĩa 30.7 là suy rộng/tổng quát hóa đến bất kỳ hữu hạn số của các đa thức như sau.

> **Định nghĩa 30.8.** Cho trước bất kỳ khác không các đa thức $f_{1}, \dots  , f_{n} \in$ K[X], ở đâu $n \ge 2$, đa thức $d \in$ K[X] là lớn nhất chung/phổ biến ước của $f_{1}, \dots  , f_{n}$ (cho ngắn, ước chung lớn nhất (gcd) của $f_{1}, \dots  , f_{n})$ nếu $d$ chia hết mỗi $f_{i}$ và bất cứ khi nào $h \in$ K[X] chia hết mỗi $f_{i}$, thì $h$ chia hết $d$. Ta nói rằng $f_{1}, \dots  , f_{n}$ là một cách tương đối nguyên tố nếu $1$ là ước chung lớn nhất (gcd) của $f_{1}, \dots  , f_{n}$. Dễ dàng chứng minh được rằng Mệnh đề 30.11 có thể được suy rộng/tổng quát hóa đến bất kỳ hữu hạn số của các đa thức, và tương tự cho của nó relevant các hệ quả. chi tiết là để lại như một bài tập.

> **Mệnh đề 30.15.** Cho $K$ là trường và cho $f_{1}, \dots  , f_{n} \in$ K[X] là bất kỳ $n \ge 2$ khác không các đa thức. Với mọi đa thức $d \in$ K[X], các tính chất sau đây là tương đương:
$(1)$ đa thức $d$ là ước chung lớn nhất (gcd) của $f_{1}, \dots  , f_{n}$.
$(2)$ đa thức $d$ chia hết mỗi $f_{i}$ và ở đó tồn tại $u_{1}, \dots  , u_{n} \in$ K[X] sao cho
$$d = u_{1}f_{1} + \cdots  + u_{n}f_{n}.$$
$(3)$ các lý tưởng $(f_{i})$, và $(d)$ thỏa mãn phương trình
$$(d) = (f_{1}) + \cdots  + (f_{n}).$$
