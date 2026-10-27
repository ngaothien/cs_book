# Chinese Phần dư Định lý


<!-- PAGE 1147 -->
Với một số $p \in A$ rằng là không unit. Hơn thế nữa, theo Mệnh đề 32.1, phần tử $p$ là bất khả quy (irreducible). Định nghĩa
$$\mathfrak{B} = {a \in A | pa \in \mathfrak{A}}.$$
Rõ ràng, $\mathfrak{A} = p\mathfrak{B}, \mathfrak{B} \neq  (0), \mathfrak{A} \subseteq \mathfrak{B}$, và $\mathfrak{B}$ là lý tưởng thực sự (proper ideal). Ta khẳng định rằng $\mathfrak{A} \neq \mathfrak{B}$. Thật vậy, nếu $\mathfrak{A} = \mathfrak{B}$ đã là đúng, thì ta sẽ có $\mathfrak{A} = p\mathfrak{B} = \mathfrak{B}$, nhưng điều này là không thể vì $p$ là bất khả quy (irreducible), $A$ là UFD, và $\mathfrak{B} \neq  (0)$ (ta thu được $\mathfrak{B} = p^{m}\mathfrak{B}$ với mọi $m$, và mọi phần tử của $\mathfrak{B}$ sẽ là bội của $p^{m}$ cho arbitrarily lớn $m$, contradicting sự kiện rằng $A$ là UFD). Do đó, ta có $\mathfrak{A} \subset \mathfrak{B}$, và vì $\mathfrak{A}$ là cực đại phần tử của $\mathcal{F}$, ta phải có $\mathfrak{B} \in F/$. Tuy nhiên, $\mathfrak{B} \in F/$ có nghĩa là $\mathfrak{B}$ là chính lý tưởng (ideal), và do đó, $\mathfrak{A} = p\mathfrak{B}$ là cũng chính lý tưởng (ideal), một mâu thuẫn. Nhận thấy rằng ở trên chứng minh chỉ ra rằng Mệnh đề 32.13 cũng nghiệm đúng dưới giả định rằng mọi lý tưởng nguyên tố (prime ideal) là chính.

## 32.2 Chinese Phần dư Định lý

Trong mục này, mà là bit của interlude, ta chứng minh cơ bản kết quả về các thương của giao hoán các vành bởi các tích của các lý tưởng rằng là đôi một một cách tương đối nguyên tố. kết quả này có các ứng dụng trong số lý thuyết và trong cấu trúc định lý cho sinh hữu hạn (finitely generated) các môđun trên PID, mà sẽ được trình bày sau này.

> **Định nghĩa 32.3.** Cho trước hai các lý tưởng $\mathfrak{a}$ và $\mathfrak{b}$ của vành $A$, ta định nghĩa lý tưởng (ideal) $\mathfrak{ab}$ như tập hợp tất cả hữu hạn các tổng của tạo thành
$$a_{1}b_{1} + \cdots  + a_{k}b_{k},a_{i} \in \mathfrak{a}, b_{i} \in \mathfrak{b}.$$
Tổng quát hơn, nếu $\mathfrak{a}_{1}, \dots  ,\mathfrak{a}_{n}$ là $n \ge 2$ các lý tưởng của $A$, lý tưởng (ideal) $\mathfrak{a}_{1} \cdots \mathfrak{a}_{n}$ là tập hợp của hữu hạn các tổng
$$\sum_{j}  k=1 a_{1}^{j} \cdots  a_{n}^{j}, where a_{i}^{j} \in \mathfrak{a}_{i} for i = 1, \dots  , n and j = 1, \dots  , k.$$
Độc giả nên kiểm tra $that\mathfrak{ab} and\mathfrak{a}_{1} \cdots \mathfrak{a}_{n}$ là thật vậy các lý tưởng. Quan sát $that\mathfrak{ab} \subseteq \mathfrak{a}$ và $\mathfrak{ab} \subseteq \mathfrak{b}$, sao cho
$$\mathfrak{ab} \subseteq \mathfrak{a} \cap \mathfrak{b}.$$
Nói chung đẳng thức thực hiện không đúng. Tuy nhiên ta có kết quả sau kết quả.

> **Mệnh đề 32.14.** Cho trước vành $A$ và hai các lý tưởng $\mathfrak{a}$ và $\mathfrak{b}$ trong $A$, nếu
$$\mathfrak{a} +\mathfrak{b} = A,$$
Thì ta có
$$\mathfrak{ab} =\mathfrak{a} \cap \mathfrak{b}.$$

<!-- PAGE 1148 -->

*Chứng minh.* Nếu $\mathfrak{a} +\mathfrak{b} = A$, tồn tại một $a \in \mathfrak{a}$ và một số $b \in \mathfrak{b}$ sao cho
$$a + b = 1,$$
Do đó với mọi $x \in \mathfrak{a} \cap \mathfrak{b}$, ta có
$$x = xa + xb,$$
Mà chỉ ra rằng $x \in \mathfrak{ab}$.

> **Định nghĩa 32.4.** Cho trước vành $A$, hai $ideals\mathfrak{a} and\mathfrak{b}$ của $A$ rằng thỏa mãn $condition\mathfrak{a}+\mathfrak{b} = A$ được nói là coprime hoặc comaximal. Ta định nghĩa đồng cấu $\phi$: $A \to A/\mathfrak{a} \times  A/\mathfrak{b}$ bởi
$$\phi (x) = (\overline{x}_{a}\overline{, x}_{b}),$$
$where\overline{x}_{a}$ là lớp tương đương (equivalence class) của $x modulo\mathfrak{a}$ (resp. $\overline{x}_{b}$ là lớp tương đương (equivalence class) của $x$ modulo $\mathfrak{b})$. Nhắc lại rằng lý tưởng (ideal) $\mathfrak{a}$ định nghĩa quan hệ tương đương (equivalence relation) $\equiv_{a}$ trên $A$ cho trước bởi
$$x \equiv_{a}  yiffx -y \in \mathfrak{a},$$
Và rằng $A/\mathfrak{a}$ là thương vành của các lớp tương đương $\overline{x}_{a}$, ở đâu $x \in A$, và tương tự cho $A/\mathfrak{b}$. Đôi khi, ta cũng viết $x \equiv y$ (mod $\mathfrak{a})$ cho $x \equiv_{a}  y$. Rõ ràng, hạt nhân (kernel) của đồng cấu $\phi$ là $\mathfrak{a} \cap \mathfrak{b}$. Nếu ta giả sử rằng $\mathfrak{a} +\mathfrak{b} = A$, thì Ker $(\phi$) $=\mathfrak{a} \cap \mathfrak{b} =\mathfrak{ab}$, và bởi vì $\phi$ có hằng số giá trị trên các lớp tương đương modulo $\mathfrak{ab}$, ánh xạ $\phi$ cảm sinh thương đồng cấu
$$\theta : A/\mathfrak{ab} \to A/\mathfrak{a} \times  A/\mathfrak{b}$$
Cho trước bởi $\theta (\overline{x}) = \phi (x)$, như được minh họa trong sau đây biểu đồ:
$$A\overline{J} A/\mathfrak{ab}$$
$$\overline{J}^{\pi}\overline{J}$$
$$\overline{J} J$$
$$JJ$$
$$JJ\theta$$
$$\phi JJ$$
$$%$$
$$A/\mathfrak{a} \times  A/\mathfrak{b}.$$
Bởi vì Ker $(\phi$) $=\mathfrak{ab}$, đồng cấu $\theta$ là đơn ánh (injective). Chinese phần dư định lý nói rằng rằng $\theta$ là đẳng cấu.

> **Định lý 32.15.** Cho trước vành giao hoán (commutative ring) $A$, cho $\mathfrak{a}$ và $\mathfrak{b}$ là bất kỳ hai các lý tưởng của $A$ sao cho $\mathfrak{a} +\mathfrak{b} = A$. Thì đồng cấu $\theta$: $A/\mathfrak{ab} \to A/\mathfrak{a} \times  A/\mathfrak{b}$ là đẳng cấu.

*Chứng minh.* Ta đã đã chỉ ra rằng $\theta$ là đơn ánh (injective), do đó ta cần để chứng minh rằng $\theta$ là toàn ánh (surjective). Cho trước bất kỳ $\overline{y} \in A/\mathfrak{a}$ và bất kỳ $\overline{z} \in A/\mathfrak{b}$, thứ nhất ta cần để chứng minh rằng với mọi lựa chọn của representative

<!-- PAGE 1149 -->
$y$ trong equivalence $class\overline{y}$ và của representative $z$ trong equivalence $class\overline{z}$, tồn tại một $x \in A$ sao cho
$$x \equiv y(\mathrm{mod} \mathfrak{a})$$
$$x \equiv z(\mathrm{mod} \mathfrak{b}).$$
Thì ta cũng cần để chỉ ra rằng nếu x' là nghiệm thu được cho một cái khác lựa chọn của representative y' trong equivalence $class\overline{y}$ và representative z' trong equivalence $class\overline{z}$, ta có x' $\equiv_{ab}  x$. Vì $\mathfrak{a} +\mathfrak{b} = A$, ở đó tồn tại một số $a \in \mathfrak{a}$ và một số $b \in \mathfrak{b}$ sao cho
$$a + b = 1.$$
Nếu ta cho
$$x = az + by,$$
Vì $a \in \mathfrak{a}$ ta có
$$x = az + by \equiv_{a}  by \equiv_{a}  (1 -a)y \equiv_{a}  y -ay \equiv_{a}  y,$$
Và tương tự vì $b \in \mathfrak{b}$
$$x = az + by \equiv_{b}  az \equiv_{b}  (1 -b)z \equiv_{b}  z -bz \equiv_{b}  z,$$
Mà chỉ ra rằng $x =$ az $+$ bởi hoạt động. Cho một cái khác lựa chọn của các phần tử ' $\in \mathfrak{a}$ và b' $\in \mathfrak{b}$ sao cho ' $+$ b' $= 1$ và của representative y' trong lớp tương đương (equivalence class) $\overline{y}$ và representative z' trong lớp tương đương (equivalence class) $\overline{z}$, ta cần để chỉ ra x' $\equiv_{ab}  x$ sao cho $\theta (\overline{x}) = \phi (x)$ được xác định tốt (well-defined). ở trên phép tính chỉ ra rằng x' $=$ 'z' $+$ b'y' là nghiệm của hệ
$$x'\equiv y'(\mathrm{mod} \mathfrak{a})$$
$$x'\equiv z'(\mathrm{mod} \mathfrak{b}).$$
Vì ta cũng có
$$x \equiv y(\mathrm{mod} \mathfrak{a})$$
$$x \equiv z(\mathrm{mod} \mathfrak{b}),$$
Y' $\equiv_{a}  y$, và z' $\equiv_{b}  z$, ta thu được
$$x'-x \equiv y'-y \equiv 0(\mathrm{mod} \mathfrak{a})$$
$$x'-x \equiv z'-z \equiv 0(\mathrm{mod} \mathfrak{b}),$$
Do đó x' - $x \in \mathfrak{a} \cap \mathfrak{b} =\mathfrak{ab}$, cụ thể là x' $\equiv_{ab}  x$.

<!-- PAGE 1150 -->
Định lý 32.15 có thể được suy rộng/tổng quát hóa đến bất kỳ (hữu hạn) số của các lý tưởng.

> **Định lý 32.16.** (Chinese phần dư định lý) Cho trước vành giao hoán (commutative ring) $A$, cho $\mathfrak{a}_{1}, \dots  ,\mathfrak{a}_{n}$ là bất kỳ $n \ge 2$ các lý tưởng của $A$ sao cho $\mathfrak{a}_{i} +\mathfrak{a}_{j} = A$ với mọi i̸ $= j$. Thì đồng cấu $\theta$: $A/\mathfrak{a}_{1} \cdots \mathfrak{a}_{n} \to A/\mathfrak{a}_{1} \times  \cdots  \times  A/\mathfrak{a}_{n}$ là đẳng cấu.

*Chứng minh.* ánh xạ $\theta$: $A/\mathfrak{a}_{1} \cap \cdots  \cap \mathfrak{a}_{n} \to A/\mathfrak{a}_{1} \times  \cdots  \times  A/\mathfrak{a}_{n}$ được cảm sinh bởi đồng cấu $\phi$: $A \to A/\mathfrak{a}_{1} \times  \cdots  \times  A/\mathfrak{a}_{n}$ cho trước bởi
$$\phi (x) = (\overline{x}_{a1}\overline{, \dots  , x}_{an})$$
Như được minh họa ở dưới:
$$A\overline{O} A/\mathfrak{a}_{1} \cap \cdots  \cap \mathfrak{a}_{n}$$
$$\overline{O}\overline{O}^{\pi}$$
$$\overline{O}\overline{O}$$
$$OO$$
$$OO$$
$$OO\theta$$
$$\phi OO$$
$$O'$$
$$A/\mathfrak{a}_{1} \times  \cdots  \times  A/\mathfrak{a}_{n}.$$
Rõ ràng, Ker $(\phi$) $=\mathfrak{a}_{1} \cap \cdots  \cap \mathfrak{a}_{n}$, do đó $\theta$ là xác định tốt (well-defined) và đơn ánh (injective). Ta cần để chứng minh rằng
$$\mathfrak{a}_{1} \cap \cdots  \cap \mathfrak{a}_{n} =\mathfrak{a}_{1} \cdots \mathfrak{a}_{n}$$
Và rằng $\theta$ là toàn ánh (surjective). Ta tiến hành bởi quy nạp. trường hợp $n = 2$ là Định lý 32.15. Bởi quy nạp, giả sử rằng
$$\mathfrak{a}_{2} \cap \cdots  \cap \mathfrak{a}_{n} =\mathfrak{a}_{2} \cdots \mathfrak{a}_{n}.$$
Ta khẳng định rằng
$$\mathfrak{a}_{1} +\mathfrak{a}_{2} \cdots \mathfrak{a}_{n} = A.$$
Thật vậy, vì $\mathfrak{a}_{1} +\mathfrak{a}_{i} = A$ cho $i = 2, \dots  , n$, ở đó tồn tại một số $a_{i} \in \mathfrak{a}_{1}$ và một số $b_{i} \in \mathfrak{a}_{i}$ sao cho
$$a_{i} + b_{i} = 1,i = 2, \dots  , n,$$
Và bằng cách nhân các phương trình này, ta thu được
$$(a_{2} + b_{2}) \cdots  (a_{n} + b_{n}) = 1,$$
Và do đó
$$a + b_{2} \cdots  b_{n} = 1,$$
Ở đâu là tổng của các số hạng mỗi chứa một số $a_{j}$ như nhân tử, do đó $a \in \mathfrak{a}_{1}$ và $b_{2} \cdots  b_{n} \in \mathfrak{a}_{2} \cdots \mathfrak{a}_{n}$, mà chỉ ra rằng
$$\mathfrak{a}_{1} +\mathfrak{a}_{2} \cdots \mathfrak{a}_{n} = A,(*)$$
Như đã khẳng định. Suy ra rằng
$$\mathfrak{a}_{1} \cap \mathfrak{a}_{2} \cap \cdots  \cap \mathfrak{a}_{n} =\mathfrak{a}_{1} \cap (\mathfrak{a}_{2} \cdots \mathfrak{a}_{n}) =\mathfrak{a}_{1}\mathfrak{a}_{2} \cdots \mathfrak{a}_{n}.$$

<!-- PAGE 1151 -->
Cho chúng ta bây giờ chứng minh rằng $\theta$ là toàn ánh (surjective) bởi quy nạp. trường hợp $n = 2$ là Định lý 32.15. Nếu $n \ge 3$, cho trước bất kỳ $\overline{x}_{i} \in A/\mathfrak{a}_{i}$ cho $i = 1, \dots  , n$, thứ nhất ta cần để chứng minh rằng với mọi lựa chọn $x_{i}$ của representative trong lớp tương đương (equivalence class) $\overline{x}_{i}$, tồn tại một $x \in A$ sao cho
$$x \equiv x_{i}(\mathrm{mod} \mathfrak{a}_{i}),i = 1, \dots  , n$$
Thì ta cần để chứng minh rằng nếu x' là bất kỳ khác nghiệm thu được bằng cách sử dụng khác representatives
$$-$$
$x_{i}'$ trong các lớp $\overline{x}_{i}$, thì x' $x \in \mathfrak{a}_{1} \cdots \mathfrak{a}_{n}$. Thứ nhất, áp dụng Định lý 32.15 đến $\mathfrak{a}_{1}$ và $\mathfrak{a}_{2} \cdots \mathfrak{a}_{n}$, ta có thể tìm $y_{1} \in A$ sao cho
$$y_{1} \equiv 1(\mathrm{mod} \mathfrak{a}_{1})$$
$$y_{1} \equiv 0(\mathrm{mod} \mathfrak{a}_{2} \cdots \mathfrak{a}_{n}).$$
Theo giả thiết quy nạp, ta có thể tìm $y_{2}, \dots  , y_{n} \in A$ sao cho với mọi $i, j$ với $2 \le i, j \le n$,
$$y_{i} \equiv 1(\mathrm{mod} \mathfrak{a}_{i})$$
$$y_{i} \equiv 0(\mathrm{mod} \mathfrak{a}_{j}),j \neq  i.$$
Nhận thấy rằng $y_{i} \equiv 0$ (mod $\mathfrak{a}_{j})$ với mọi $j \neq  i$ với $2 \le i, j \le n$ là tương đương đến
$$y_{j} \equiv 0(\mathrm{mod} \mathfrak{a}_{i})for all j \neq  i with 2 \le i, j \le n.$$
Ta khẳng định rằng
$$x = x_{1}y_{1} + x_{2}y_{2} + \cdots  + x_{n}y_{n}$$
Hoạt động. Thật vậy, cho $i = 2, \dots  , n$ và mọi số hạng $x_{j}y_{j}$ với $j \neq  i$ và $2 \le j \le n$ trong tổng $x_{2}y_{2} + \cdots  + x_{i}y_{i} + \cdots  + x_{n}y_{n}$, ta có $x_{j}y_{j} \equiv 0$ (mod $\mathfrak{a}_{i})$ vì $y_{j} \equiv 0$ (mod $\mathfrak{a}_{i})$ với mọi $j \neq  i$ với $2 \le i, j \le n$, và $x_{i}y_{i} \equiv x_{i}$ (mod $\mathfrak{a}_{i})$ vì $y_{i} \equiv 1$ (mod $\mathfrak{a}_{i})$, do đó ta thu được
$$x \equiv x_{1}y_{1} + x_{i}(\mathrm{mod} \mathfrak{a}_{i}),i = 2, \dots  , n.(**)$$
Vì $\mathfrak{a}_{2} \cdots \mathfrak{a}_{n} \subseteq \mathfrak{a}_{i}$ cho $i = 2, \dots  , n$ và $y_{1} \equiv 0$ (mod $\mathfrak{a}_{2} \cdots \mathfrak{a}_{n})$, ta có
$$x_{1}y_{1} \equiv 0(\mathrm{mod} \mathfrak{a}_{i}),i = 2, \dots  , n$$
Và phương trình (**) rút gọn đến
$$x \equiv x_{i}(\mathrm{mod} \mathfrak{a}_{i}),i = 2, \dots  , n.$$
Cho $i = 1$, ta thu được
$$x \equiv x_{1}(\mathrm{mod} \mathfrak{a}_{1}),$$
Vì vậy
$$x \equiv x_{i}(\mathrm{mod} \mathfrak{a}_{i}),i = 1, \dots  , n.$$
Ta vẫn để chứng minh rằng nếu x' là bất kỳ khác nghiệm thu được bằng cách sử dụng khác các nghiệm $y_{i}'$ và
$$-$$
Khác representatives $x_{i}'$ trong các lớp $\overline{x}_{i}$, thì x' $x \in \mathfrak{a}_{1} \cdots \mathfrak{a}_{n}$.

<!-- PAGE 1152 -->
Nhưng một cái khác nghiệm x' $= x_{1}'y_{1}' + x_{2}'y_{2}' + \cdots  + x_{n}'y_{n}'$ thỏa mãn hệ của các phương trình
$$x'\equiv x_{i}'(\mathrm{mod} \mathfrak{a}_{i}),i = 1, \dots  , n,$$
Và vì $x_{i}' \equiv_{ai}  x_{i}$ và
$$x \equiv x_{i}'(\mathrm{mod} \mathfrak{a}_{i}),i = 1, \dots  , n,$$
Ta thu được
$$x'-x \equiv 0(\mathrm{mod} \mathfrak{a}_{i}),i = 1, \dots  , n,$$
Do đó x' - $x \in \mathfrak{a}_{1} \cap \cdots  \cap \mathfrak{a}_{n} =\mathfrak{a}_{1} \cdots \mathfrak{a}_{n}$, như mong muốn. Một cái khác chứng minh sử dụng phương trình
$$\mathfrak{a}_{1} +\mathfrak{a}_{2} \cdots \mathfrak{a}_{n} = A$$
Được chứng minh trước đó, mà cũng nghiệm đúng với mọi $i$, cụ thể là
$$\mathfrak{a}_{i} + \prod_{=1,j\neq}^{n}  \mathfrak{a}_{j} = A,1 \le i \le n.$$
$$ji$$
$$Pick any a_{i} \in \mathfrak{a}_{i} and any b_{i} \in \prod_{j}  n=1,j\neq i \mathfrak{a}_{j} such that a_{i} + b_{i} = 1, 1 \le i \le n. We claim that$$
$$x = b_{1}x_{1} + \cdots  + b_{n}x_{n}$$
Thỏa mãn hệ của các phương trình
$$x \equiv x_{i}(\mathrm{mod} \mathfrak{a}_{i}),i = 1, \dots  , n.$$
Điều này là bởi vì với mỗi $i$ với $1 \le i \le n$,
$$x = b_{1}x_{1} + \cdots  + b_{i}x_{i} + \cdots  + b_{n}x_{n} = b_{1}x_{1} + \cdots  + (1 -a_{i})x_{i} + \cdots  + b_{n}x_{n}$$
$$= x_{i} + b_{1}x_{1} + \cdots  + b_{i-1}x_{i-1} -a_{i}x_{i} + b_{i+1}x_{i+1} + \cdots  + b_{n}x_{n},$$
$$but b_{k} \in \prod_{j}  n=1,j\neq k \mathfrak{a}_{j} for all k, \prod_{j}  n=1,j\neq k \mathfrak{a}_{j} \subseteq \mathfrak{a}_{i} if k \neq  i, and a_{i} \in \mathfrak{a}_{i}, so$$
$$x \equiv x_{i}(\mathrm{mod} \mathfrak{a}_{i}),i = 1, \dots  , n.$$
$n$
$$If x'= b_{1}'x_{1}' + \cdots  + b_{i}'x_{i}' + \cdots  + b_{n}'x_{n}' for another choice of a_{i}' \in \mathfrak{a}_{i}, b_{i}' \in \prod_{j}  =1,j\neq i \mathfrak{a}_{j}, and x_{i}' in$$
Lớp tương đương (equivalence class) $\overline{x}_{i}$, ta có các phương trình
$$x'\equiv x_{i}'(\mathrm{mod} \mathfrak{a}_{i}),i = 1, \dots  , n,$$
Và vì $x_{i}' \equiv x_{i}$ (mod $\mathfrak{a}_{i})$ cho $i = 1, \dots  , n$, ta suy ra rằng
$$x'-x \equiv x_{i}' -x_{i} \equiv 0(\mathrm{mod} \mathfrak{a}_{i}),i = 1, \dots  , n,$$
Do đó như trước, x' - $x \in \mathfrak{a}_{1} \cdots \mathfrak{a}_{n}$, như mong muốn.

<!-- PAGE 1153 -->
Cổ điển phiên bản của Chinese phần dư định lý là trường hợp ở đâu $A = \mathbb{Z}$ và ở đâu các lý tưởng $\mathfrak{a}_{i}$ được định nghĩa bởi $n$ đôi một một cách tương đối nguyên tố các số nguyên $m_{1}, \dots  , m_{n}$. Bởi Bezout đồng nhất thức, vì $m_{i}$ và $m_{j}$ là một cách tương đối nguyên tố bất cứ khi nào i̸ $= j$, ở đó tồn tại một số $u_{i}, u_{j} \in \mathbb{Z}$ sao cho $u_{i}m_{i} + u_{j}m_{j} = 1$, và do đó $m_{i}\mathbb{Z} + m_{j}\mathbb{Z} = \mathbb{Z}$. Trong trường hợp này, ta thu được đẳng cấu
$$\mathbb{Z}/(m_{1} \cdots  m_{n})\mathbb{Z} \approx \prod_{i=1}^{n}  \mathbb{Z}/m_{i}\mathbb{Z}.$$
Đặc biệt, nếu $m$ là số nguyên greater hơn $1$ và
$$m = \prod_{i}  p_{i}^{ri}$$
Là nhân tử hóa của nó vào nguyên tố các nhân tử, thì
$$\mathbb{Z}/m\mathbb{Z} \approx \prod_{i}  \mathbb{Z}/p_{i}^{ri} \mathbb{Z}.$$
Trong trước đó tình huống ở đâu các số nguyên $m_{1}, \dots  , m_{n}$ là đôi một một cách tương đối nguyên tố, nếu ta viết $m = m_{1} \cdots  m_{n}$ và $m_{i}' = m/m_{i}$ cho $i = 1 \dots  , n$, thì $m_{i}$ và $m_{i}'$ là một cách tương đối nguyên tố, và do đó $m_{i}'$ có nghịch đảo modulo $m_{i}$. Nếu $t_{i}$ là như vậy nghịch đảo, sao cho
$$m_{i}'t_{i} \equiv 1(\mathrm{mod} m_{i}),$$
Thì nó là không khó để chỉ ra rằng với mọi $a_{1}, \dots  , a_{n} \in \mathbb{Z}$,
$$x = a_{1}t_{1}m_{1}' + \cdots  + a_{n}t_{n}m_{n}'$$
Thỏa mãn congruences
$$x \equiv a_{i}(\mathrm{mod} m_{i}),i = 1, \dots  , n.$$
Định lý 32.16 có thể được được sử dụng để đặc trưng hóa các vành đẳng cấu đến hữu hạn các tích của thương các vành. Như vậy các vành đóng vai trò trong cấu trúc định lý cho xoắn (torsion) các môđun trên PID.

> **Định nghĩa 32.5.** Cho trước $n$ các vành $A_{1}, \dots  , A_{n} (n \ge 2)$, nhắc lại rằng tích vành $A = A_{1} \times  \cdots  \times  A_{n}$ là vành trong mà phép cộng và phép nhân được định nghĩa componenwise. Rằng là,
$$(a_{1}, \dots  , a_{n}) + (b_{1}, \dots  , b_{n}) = (a_{1} + b_{1}, \dots  , a_{n} + b_{n})$$
$$(a_{1}, \dots  , a_{n}) \cdot  (b_{1}, \dots  , b_{n}) = (a_{1}b_{1}, \dots  , a_{n}b_{n}).$$
Additive đồng nhất thức là $0_{A} = (0, \dots  , 0)$ và multiplicative đồng nhất thức là $1_{A} = (1, \dots  , 1)$. Cho $i = 1, \dots  , n$, ta có thể định nghĩa phần tử $e_{i} \in A$ như sau:
$$e_{i} = (0, \dots  , 0, 1, 0, \dots  , 0),$$
Ở đâu $1$ xảy ra trong position $i$.

<!-- PAGE 1154 -->
Nhận thấy rằng các tính chất sau đây đúng với mọi $i, j = 1, \dots  , n$:
$$e_{i}^{2} = e_{i}$$
$$e_{i}e_{j} = 0,i \neq  j$$
$$e_{1} + \cdots  + e_{n} = 1_{A}.$$
Cũng, với mọi phần tử $a = (a_{1}, \dots  , a_{n}) \in A$, ta có
$$e_{i}a = (0, \dots  , 0, a_{i}, 0, \dots  , 0) = pr_{i}(a),$$
Ở đâu $pr_{i}$ là phép chiếu của $A$ lên $A_{i}$. Hệ quả là
$$\mathrm{Ker} (pr_{i}) = (1_{A} -e_{i})A.$$

> **Định nghĩa 32.6.** Cho trước vành giao hoán (commutative ring) $A$, trực tiếp phân rã của $A$ là dãy $(\mathfrak{b}_{1}, \dots  ,\mathfrak{b}_{n}) (n \ge 2)$ của các lý tưởng trong $A$ sao cho có một đẳng cấu $A \approx A/\mathfrak{b}_{1} \times \cdots \times A/\mathfrak{b}_{n}$. sau đây định lý cho hữu ích các điều kiện đặc trưng hóa trực tiếp các phân rã của vành.

> **Định lý 32.17.** Cho $A$ là vành giao hoán (commutative ring) và cho $(\mathfrak{b}_{1}, \dots  ,\mathfrak{b}_{n})$ là dãy của các lý tưởng trong $A (n \ge 2)$. Các điều kiện sau đây là tương đương:
() dãy $(\mathfrak{b}_{1}, \dots  ,\mathfrak{b}_{n})$ là trực tiếp phân rã của $A$.
$(b)$ Ở đó tồn tại một số khác không các phần tử $e_{1}, \dots  , e_{n}$ của $A$ sao cho
$$e_{i}^{2} = e_{i}$$
$$e_{i}e_{j} = 0,i \neq  j$$
$$e_{1} + \cdots  + e_{n} = 1_{A},$$
Và $\mathfrak{b}_{i} = (1_{A}$ - $e_{i})A$, cho $i, j = 1, \dots  , n$.
$(c)$ Ta có $\mathfrak{b}_{i} +\mathfrak{b}_{j} = A$ với mọi $i \neq  j$, và $\mathfrak{b}_{1} \cdots \mathfrak{b}_{n} = (0)$.
$(d)$ Ta có $\mathfrak{b}_{i} +\mathfrak{b}_{j} = A$ với mọi $i \neq  j$, và $\mathfrak{b}_{1} \cap \cdots  \cap \mathfrak{b}_{n} = (0)$.

*Chứng minh.* Giả sử (). Vì ta có đẳng cấu $A \approx A/\mathfrak{b}_{1} \times  \cdots  \times  A/\mathfrak{b}_{n}$, ta có thể đồng nhất $A$ với $A/\mathfrak{b}_{1} \times  \cdots  \times  A/\mathfrak{b}_{n}$, và $\mathfrak{b}_{i}$ với Ker $(pr_{i})$. Thì, $e_{1}, \dots  , e_{n}$ là các phần tử được định nghĩa chỉ trước Định nghĩa 32.6. Như được lưu ý, $\mathfrak{b}_{i} =$ Ker $(pr_{i}) = (1_{A}$ - $e_{i})A$. Điều này chứng minh $(b)$. Giả sử $(b)$. Vì $\mathfrak{b}_{i} = (1_{A}$ - $e_{i})A$ và $A$ là vành với unit $1_{A}$, ta có $1_{A}$ - $e_{i} \in \mathfrak{b}_{i}$ cho $i = 1, \dots  , n$. Với mọi $i \neq  j$, ta cũng có $e_{i}(1_{A}$ - $e_{j}) = e_{i}$ - $e_{i}e_{j} = e_{i}$, do đó (bởi vì $\mathfrak{b}_{j}$ là

<!-- PAGE 1155 -->
Lý tưởng (ideal)), $e_{i} \in \mathfrak{b}_{j}$, và do đó, $1_{A} = 1_{A}$ - $e_{i} + e_{i} \in \mathfrak{b}_{i} +\mathfrak{b}_{j}$, mà chỉ ra rằng $\mathfrak{b}_{i} +\mathfrak{b}_{j} = A$ với mọi $i \neq  j$. Hơn nữa, với mọi $x_{i} \in A$, với $1 \le i \le n$, vì $e_{i}e_{j} = 0$ với mọi $i \neq  j$, ta có
$$\prod_{i=1}^{n}  x_{i}(1_{A} -e_{i}) = \begin{pmatrix} x_{i} \end{pmatrix} \prod_{i=1}^{n}  \prod_{i=1}^{n}  (1_{A} -e_{i})$$
$$= \begin{pmatrix} x_{i} \end{pmatrix} \prod_{i=1}^{n}  (1_{A} - \sum_{i=1}^{n}  e_{i})$$
$$= 0,$$
Mà chứng tỏ rằng $\mathfrak{b}_{1} \cdots \mathfrak{b}_{n} = (0)$. Do đó, $(c)$ nghiệm đúng. equivalence của $(c)$ và $(d)$ suy ra từ chứng minh của Định lý 32.16. sự kiện rằng $(c)$ suy ra () là immediate hệ quả của Định lý 32.16. Ở đây là ví dụ của Định lý 32.17.

> **Ví dụ 32.2.** Lấy vành giao hoán (commutative ring) của residue các lớp mod $30$, cụ thể là
$$A :=\mathbb{Z}/30\mathbb{Z} = {\overline{i}}_{i=0}^{29}.$$
Cho
$$\mathfrak{b}_{1} = 2\mathbb{Z}/30\mathbb{Z} := {2\overline{i}}_{i=0}^{14}$$
$$\mathfrak{b}_{2} = 3\mathbb{Z}/30\mathbb{Z} := {3\overline{i}}_{i=0}^{9}$$
$$\mathfrak{b}_{3} = 5\mathbb{Z}/30\mathbb{Z} := {5\overline{i}}_{i=0}^{5}.$$
Mỗi $\mathfrak{b}_{i}$ là lý tưởng (ideal) trong $\mathbb{Z}/30\mathbb{Z}$. Hơn nữa
$$\mathbb{Z}/30\mathbb{Z} = (\mathbb{Z}/30\mathbb{Z})/(2\mathbb{Z}/30\mathbb{Z}) \times  (\mathbb{Z}/30\mathbb{Z})/(3\mathbb{Z}/30\mathbb{Z}) \times  (\mathbb{Z}/30\mathbb{Z})/(5\mathbb{Z}/30\mathbb{Z}),$$
Ở đâu
$$e_{1} = (1, 0, 0) \to \overline{15},e_{2} = (0, 1, 0) \to \overline{10},e_{3} = (0, 0, 1) \to \overline{6},$$
Vì
$$\overline{15}^{2}\overline{= 15},\overline{10}^{2}\overline{= 10},\overline{6}^{2}\overline{= 6}$$
$$\overline{15 10 = 15 6 = 10 6 = 0},\overline{15 + 10 + 6 = 1}.$$
Nhận thấy rằng $\overline{15}$ tương ứng với $\overline{1} \in (\mathbb{Z}/30\mathbb{Z})/(2\mathbb{Z}/30\mathbb{Z}), \overline{10}$ tương ứng với $\overline{1} \in (\mathbb{Z}/30\mathbb{Z})/ (3\mathbb{Z}/30\mathbb{Z})$, trong khi $\overline{6}$ tương ứng với $\overline{1} \in (\mathbb{Z}/30\mathbb{Z})/(5\mathbb{Z}/30\mathbb{Z})$. sau đây cấu trúc định lý cho giao hoán các vành đẳng cấu đến tích vành là cũng rất hữu ích. Xem Bourbaki $[26]$ Chương I, Mục 8(10) và Lafon $[112]$, Chương II, Mục 3(1).

<!-- PAGE 1156 -->

> **Mệnh đề 32.18.** Cho $A_{1}, \dots  , A_{n} (n \ge 2)$ và $A$ là giao hoán các vành (với đồng nhất thức) và giả sử rằng ta có đẳng cấu $\theta$: $A \to A_{1} \times  \cdots  \times  A_{n}$. Viết $0_{n} = (0, \dots  , 0)$, và cho $i = 1, \dots  , n$, định nghĩa phần tử $e_{i} \in A_{1} \times  \cdots  \times  A_{n}$ như
$$e_{i} = (0, \dots  , 0, 1, 0, \dots  , 0),$$
Ở đâu $1$ xảy ra trong position $i$. Thì cho $e_{i} = \theta^{-1} (e_{i}) and\mathfrak{a}_{i} = e_{i}A = \theta^{-1} (e_{i}(A_{1}\times \cdots \times A_{n}))$, cho $i = 1, \dots  , n$. Các tính chất sau đây đúng.
$(1)$ các phần tử $e_{i} \in A$ là khác không các lũy đẳng (idempotent) sao cho với mọi $i, j = 1, \dots  , n$,
$$e_{i}^{2} = e_{i}$$
$$e_{i}e_{j} = 0,i \neq  j$$
$$e_{1} + \cdots  + e_{n} = 1_{A}.$$
$(2) \mathfrak{a}_{i} = e_{i}A$ là khác không lý tưởng (ideal) cho $i = 1, \dots  , n$. vành $\mathfrak{a}_{i}$ có đồng nhất thức $e_{i}$ và là đẳng cấu đến $A_{i}$ cho $i = 1, \dots  , n$.
$(3)$ vành $A$ là tổng trực tiếp (direct sum) $A =\mathfrak{a}_{1} \oplus \cdots  \oplus \mathfrak{a}_{n} = e_{1}A \oplus \cdots  \oplus e_{n}A$.
$(4)$ Với mọi lý tưởng (ideal) $\mathfrak{b}$ trong $R$, ta có $\mathfrak{b} = \mathfrak{b} \cap \mathfrak{a}_{1} \oplus \cdots  \oplus \mathfrak{b} \cap \mathfrak{a}_{n} = e_{1}\mathfrak{b} \oplus \cdots  \oplus e_{n}\mathfrak{b}$ và $\mathfrak{b} \cap \mathfrak{a}_{i} = e_{i}\mathfrak{b}$ là lý tưởng (ideal) cho $i = 1, \dots  , n$.
$(5)$ Cho $A$ là vành giao hoán (commutative ring) với đồng nhất thức và giả sử rằng ở đó tồn tại $n \ge 2$ khác không các phần tử $e_{i} \in A$ thỏa mãn các tính chất trong $(1)$. Thì mỗi $\mathfrak{a}_{i} = e_{i}A$ là khác không lý tưởng (ideal) trong $A$ và vành với đồng nhất thức $e_{i}$ cho $i = 1, \dots  , n$, và vành $A$ là tổng trực tiếp (direct sum) $A =\mathfrak{a}_{1} \oplus \cdots  \oplus \mathfrak{a}_{n} = e_{1}A \oplus \cdots  \oplus e_{n}A$. Có một đẳng cấu $\theta$: $A \to \mathfrak{a}_{1} \times  \cdots  \times \mathfrak{a}_{n}$. Phác thảo của chứng minh. các tính chất trong $(1)$ đúng bởi vì chúng là dễ dàng đã kiểm tra cho $e_{i}$ trong $A_{1} \times  \cdots  \times  A_{n}$, và tranferred quay lại đến $A$ bằng cách sử dụng nghịch đảo đẳng cấu $\theta^{-1}$. Ví dụ, trong $A_{1} \times  \cdots  \times  A_{n}$, ta có $e_{i}e_{j} = 0_{n}$ nếu $i \neq  j$, và
$$e_{i}e_{j} = \theta^{-1} (\theta (e_{i}e_{j})) = \theta^{-1} (\theta (e_{i})\theta (e_{j})) = \theta^{-1} (e_{i}e_{j}) = \theta^{-1} (0_{n}) = 0.$$
Để chứng minh $(2)$, ta nhận thấy rằng $e_{i}(A_{1} \times  \cdots  \times  A_{n}) = {(0, \dots  , a_{1}, \dots  , 0)$ | $a_{i} \in A_{i}}$ là lý tưởng (ideal) trong $A_{1} \times  \cdots  \times  A_{n}$ và vành các đồng cấu ánh xạ các lý tưởng đến các lý tưởng. Theo Định nghĩa, $e_{i}$ là đồng nhất thức của $\mathfrak{a}_{i} = e_{i}A$, và vì $A_{i}$ là đẳng cấu đến ${(0, \dots  , a_{i}, \dots  , 0)$ | $a_{i} \in A_{i}}$ bởi ánh xạ $a_{i} \mapsto (0, \dots  , a_{i}, \dots  , 0)$ và $\theta^{-1}$ là đẳng cấu giữa ${(0, \dots  , a_{i}, \dots  , 0)$ | $a_{i} \in A_{i}}$ và $\mathfrak{a}_{i}$, bởi hợp thành ta có đẳng cấu giữa $A_{i}$ và $\mathfrak{a}_{i}$.
$(3)$ Từ $(1)$, vì $e_{1} + \cdots  + e_{n} = 1_{A}$, với mọi $a \in A$, ta có $a = e_{1}a + \cdots  + e_{n}a$, với $e_{i}a \in \mathfrak{a}_{i}$, do đó $A =\mathfrak{a}_{1} + \cdots  +\mathfrak{a}_{n}$.
$$If a \in \mathfrak{a}_{i} \cap \bigoplus_{kj}  \mathfrak{a}_{j} then a = e_{i}\alpha_{i}  = \sum  j\neq i e_{j}\alpha_{j}  with \alpha_{i} , \alpha_{j}  \in A, and since e_{i}e_{j} = 0 for all$$
$i \neq  j$ và $e_{k}e  =^{\neq i} e_{k}$ với mọi $k$ (bởi $(1))$,
$$e_{i}a = e \sum_{ij\neq i}  e_{j}\alpha_{j}  = \sum_{j\neq i}  e_{i}e_{j}\alpha_{j}  = 0,$$
