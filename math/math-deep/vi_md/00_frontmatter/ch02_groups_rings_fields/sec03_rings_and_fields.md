# 2.3 Vành và Trường (Rings and Fields)

> **Trang gốc:** 47–54

Các nhóm $\mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}, \mathbb{Z}/n\mathbb{Z}$, và $\mathrm{M}_n(\mathbb{R})$ không chỉ là các nhóm Abel, mà chúng còn là các vành giao hoán (*commutative rings*, ngoại trừ $\mathrm{M}_n(\mathbb{R})$ khi $n \ge 2$). Hơn nữa, $\mathbb{Q}, \mathbb{R}$, và $\mathbb{C}$ là các trường (*fields*). Bây giờ chúng ta giới thiệu khái niệm vành và trường.

> **Định nghĩa 2.16 (Definition 2.16).** Một *vành* (*ring*) là một tập hợp $A$ được trang bị hai phép toán $+ : A \times A \to A$ (được gọi là *phép cộng* – *addition*) và $* : A \times A \to A$ (được gọi là *phép nhân* – *multiplication*) có các tính chất sau:
> - **(R1)** $A$ là một nhóm Abel đối với phép $+$;
> - **(R2)** $*$ có tính kết hợp và có phần tử đơn vị $1 \in A$;
> <!-- PAGE 48 -->
> - **(R3)** $*$ có tính phân phối (*distributive*) đối với phép $+$.
>
> Phần tử đơn vị đối với phép cộng được ký hiệu là $0$, và phần tử đối (nghịch đảo cộng – *additive inverse*) của $a \in A$ được ký hiệu bởi $-a$. Một cách tường minh hơn, các tiên đề của một vành là các phương trình sau đây nghiệm đúng với mọi $a, b, c \in A$:
> $$\begin{aligned}
> a + (b + c) &= (a + b) + c && \text{(tính kết hợp của $+$)} \tag{2.1} \\
> a + b &= b + a && \text{(tính giao hoán của $+$)} \tag{2.2} \\
> a + 0 &= 0 + a = a && \text{(phần tử không)} \tag{2.3} \\
> a + (-a) &= (-a) + a = 0 && \text{(phần tử đối)} \tag{2.4} \\
> a * (b * c) &= (a * b) * c && \text{(tính kết hợp của $*$)} \tag{2.5} \\
> a * 1 &= 1 * a = a && \text{(phần tử đơn vị của $*$)} \tag{2.6} \\
> (a + b) * c &= (a * c) + (b * c) && \text{(tính phân phối)} \tag{2.7} \\
> a * (b + c) &= (a * b) + (a * c) && \text{(tính phân phối)} \tag{2.8}
> \end{aligned}$$
>
> Vành $A$ được gọi là *giao hoán* (*commutative*) nếu
> $$a * b = b * a \quad \text{với mọi } a, b \in A.$$

Từ (2.7) và (2.8), ta dễ dàng thu được
$$\begin{aligned}
a * 0 &= 0 * a = 0 \tag{2.9} \\
a * (-b) &= (-a) * b = -(a * b). \tag{2.10}
\end{aligned}$$
Lưu ý rằng (2.9) suy ra nếu $1 = 0$, thì $a = 0$ với mọi $a \in A$, và do đó $A = \{0\}$. Vành $A = \{0\}$ được gọi là *vành tầm thường* (*trivial ring*). Một vành có $1 \neq 0$ được gọi là *không tầm thường* (*nontrivial*). Tích $a * b$ của hai phần tử $a, b \in A$ thường được viết gọn là $ab$.

> **Ví dụ 2.11 (Example 2.11).**
> 1. Các nhóm cộng $\mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}$ là các vành giao hoán.
> 2. Với mọi số nguyên dương $n \in \mathbb{N}$, nhóm $\mathbb{Z}/n\mathbb{Z}$ là một nhóm dưới phép cộng. Ta cũng có thể định nghĩa một phép toán nhân bởi
>    $$\overline{a} \cdot \overline{b} = \overline{ab} = \overline{ab \bmod n},$$
>    với mọi $a, b \in \mathbb{Z}$. Bạn đọc sẽ dễ dàng kiểm tra được rằng các tiên đề của vành đều được thỏa mãn, với $\overline{0}$ là phần tử không và $\overline{1}$ là phần tử đơn vị nhân. Vành thu được được ký hiệu bởi $\mathbb{Z}/n\mathbb{Z}$.[^2]
> 3. Nhóm $\mathbb{R}[X]$ gồm các đa thức một biến với hệ số thực là một vành dưới phép nhân đa thức. Đây là một vành giao hoán.
> <!-- PAGE 49 -->
> 4. Cho $d$ là một số nguyên dương bất kỳ. Nếu $d$ không chia hết cho bất kỳ số nguyên nào có dạng $m^2$, với $m \in \mathbb{N}$ và $m \ge 2$, thì ta nói $d$ là *số nguyên không chứa chính phương* (*square-free*). Ví dụ, $d = 1, 2, 3, 5, 6, 7, 10$ là các số square-free, nhưng $4, 8, 9, 12$ không phải là square-free. Nếu $d$ là một số nguyên square-free bất kỳ và $d \ge 2$, thì tập hợp các số thực
>    $$\mathbb{Z}[\sqrt{d}] = \{a + b\sqrt{d} \in \mathbb{R} \mid a, b \in \mathbb{Z}\}$$
>    là một vành giao hoán. Nếu $z = a + b\sqrt{d} \in \mathbb{Z}[\sqrt{d}]$, ta viết $\overline{z} = a - b\sqrt{d}$. Chú ý rằng $z\overline{z} = a^2 - db^2$.
> 5. Tương tự, nếu $d \ge 1$ là một số nguyên dương square-free, thì tập hợp các số phức
>    $$\mathbb{Z}[\sqrt{-d}] = \{a + ib\sqrt{d} \in \mathbb{C} \mid a, b \in \mathbb{Z}\}$$
>    là một vành giao hoán. Nếu $z = a + ib\sqrt{d} \in \mathbb{Z}[\sqrt{-d}]$, ta viết $\overline{z} = a - ib\sqrt{d}$. Chú ý rằng $z\overline{z} = a^2 + db^2$. Trường hợp $d = 1$ là một ví dụ nổi tiếng từng được Gauss nghiên cứu, và $\mathbb{Z}[\sqrt{-1}]$, còn được ký hiệu là $\mathbb{Z}[i]$, được gọi là vành các *số nguyên Gauss* (*Gaussian integers*).
> 6. Nhóm các ma trận cấp $n \times n$ là $\mathrm{M}_n(\mathbb{R})$ lập thành một vành dưới phép nhân ma trận. Tuy nhiên, đây không phải là một vành giao hoán.
> 7. Nhóm $\mathcal{C}(a, b)$ gồm các hàm liên tục $f : (a, b) \to \mathbb{R}$ là một vành dưới phép toán $f \cdot g$ được định nghĩa sao cho
>    $$(f \cdot g)(x) = f(x)g(x)$$
>    với mọi $x \in (a, b)$.

> **Định nghĩa 2.17 (Definition 2.17).** Cho một vành $A$, với mọi phần tử $a \in A$, nếu tồn tại một phần tử $b \in A$ sao cho $b \neq 0$ và $ab = 0$, thì ta nói $a$ là một *ước của không* (*zero divisor*). Một vành $A$ là một *miền nguyên* (*integral domain* hay *entire ring*) nếu $0 \neq 1$, $A$ giao hoán, và $ab = 0$ kéo theo $a = 0$ hoặc $b = 0$, với mọi $a, b \in A$. Nói cách khác, một miền nguyên là một vành giao hoán không tầm thường và không có ước của không nào ngoài $0$.

> **Ví dụ 2.12 (Example 2.12).**
> 1. Các vành $\mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}$ là các miền nguyên.
> 2. Vành $\mathbb{R}[X]$ gồm các đa thức một biến với hệ số thực là một miền nguyên.
> 3. Với mọi số nguyên dương $n \in \mathbb{N}$, ta có vành $\mathbb{Z}/n\mathbb{Z}$. Chú ý rằng nếu $n$ là hợp số (*composite*), thì vành này có các ước của không. Ví dụ, nếu $n = 4$, thì ta có
>    $$2 \cdot 2 \equiv 0 \pmod{4}.$$
>    Bạn đọc hãy tự chứng minh rằng $\mathbb{Z}/n\mathbb{Z}$ là một miền nguyên khi và chỉ khi $n$ là số nguyên tố (sử dụng Mệnh đề 2.17).
> <!-- PAGE 50 -->
> 4. Nếu $d$ là một số nguyên dương square-free và $d \ge 2$, thì vành $\mathbb{Z}[\sqrt{d}]$ là một miền nguyên. Tương tự, nếu $d \ge 1$ là một số nguyên dương square-free, thì vành $\mathbb{Z}[\sqrt{-d}]$ là một miền nguyên. Việc tìm các phần tử khả nghịch của những vành này là một bài toán rất thú vị.
> 5. Vành các ma trận cấp $n \times n$ là $\mathrm{M}_n(\mathbb{R})$ có các ước của không.

Một đồng cấu giữa các vành là một ánh xạ bảo toàn phép cộng và phép nhân (cùng với $0$ và $1$).

> **Định nghĩa 2.18 (Definition 2.18).** Cho hai vành $A$ và $B$, một *đồng cấu* (*homomorphism*) giữa $A$ và $B$ là một hàm $h : A \to B$ thỏa mãn các điều kiện sau với mọi $x, y \in A$:
> $$\begin{aligned}
> h(x + y) &= h(x) + h(y) \\
> h(xy) &= h(x)h(y) \\
> h(0) &= 0 \\
> h(1) &= 1.
> \end{aligned}$$

Thực ra, bởi vì $B$ là một nhóm dưới phép cộng, $h(0) = 0$ tự động suy ra từ
$$h(x + y) = h(x) + h(y).$$

> **Ví dụ 2.13 (Example 2.13).**
> 1. Nếu $A$ là một vành, với mọi số nguyên $n \in \mathbb{Z}$ và với mọi $a \in A$, ta định nghĩa $n \cdot a$ bởi
>    $$n \cdot a = \underbrace{a + \dots + a}_{n}$$
>    nếu $n \ge 0$ (với $0 \cdot a = 0$) và
>    $$n \cdot a = -(-n) \cdot a$$
>    nếu $n < 0$. Khi đó, ánh xạ $h : \mathbb{Z} \to A$ cho bởi
>    $$h(n) = n \cdot 1_A$$
>    là một đồng cấu vành (trong đó $1_A$ là phần tử đơn vị nhân của $A$).
> 2. Cho số thực bất kỳ $\lambda \in \mathbb{R}$, ánh xạ tính giá trị (*evaluation map*) $\eta_\lambda : \mathbb{R}[X] \to \mathbb{R}$ được định nghĩa bởi
>    $$\eta_\lambda(f(X)) = f(\lambda)$$
>    với mọi đa thức $f(X) \in \mathbb{R}[X]$ là một đồng cấu vành.

> **Định nghĩa 2.19 (Definition 2.19).** Một đồng cấu vành $h : A \to B$ là một *đẳng cấu* (*isomorphism*) khi và chỉ khi tồn tại một đồng cấu vành $g : B \to A$ sao cho $g \circ h = \mathrm{id}_A$ và $h \circ g = \mathrm{id}_B$. Một đẳng cấu từ một vành vào chính nó được gọi là một *tự đẳng cấu* (*automorphism*).

<!-- PAGE 51 -->

Giống như trong trường hợp đẳng cấu nhóm, đồng cấu $g$ là duy nhất và được ký hiệu bởi $h^{-1}$, đồng thời dễ dàng chứng minh được rằng một đồng cấu vành song ánh $h : A \to B$ là một đẳng cấu.

> **Định nghĩa 2.20 (Definition 2.20).** Cho một vành $A$, một tập con $A'$ của $A$ là một *vành con* (*subring*) của $A$ nếu $A'$ là một nhóm con của $A$ (dưới phép cộng), đóng kín dưới phép nhân, và chứa phần tử $1$.

Ví dụ, ta có dãy bao hàm sau đây, trong đó mỗi vành ở bên trái dấu bao hàm là một vành con của vành ở bên phải dấu bao hàm:
$$\mathbb{Z} \subseteq \mathbb{Q} \subseteq \mathbb{R} \subseteq \mathbb{C}.$$
Vành $\mathbb{Z}$ là một vành con của cả $\mathbb{Z}[\sqrt{d}]$ lẫn $\mathbb{Z}[\sqrt{-d}]$, vành $\mathbb{Z}[\sqrt{d}]$ là một vành con của $\mathbb{R}$ và vành $\mathbb{Z}[\sqrt{-d}]$ là một vành con của $\mathbb{C}$.

Nếu $h : A \to B$ là một đồng cấu vành, thì dễ dàng chỉ ra rằng với mọi vành con $A'$, ảnh $h(A')$ là một vành con của $B$, và với mọi vành con $B'$ của $B$, nghịch ảnh $h^{-1}(B')$ là một vành con của $A$.

Tương tự như đối với nhóm, hạt nhân (*kernel*) của một đồng cấu vành $h : A \to B$ được định nghĩa bởi
$$\operatorname{Ker} h = \{a \in A \mid h(a) = 0\}.$$
Giống hệt như trong trường hợp của nhóm, ta có tiêu chuẩn sau đây cho tính đơn ánh của một đồng cấu vành. Phép chứng minh hoàn toàn giống với chứng minh cho nhóm.

> **Mệnh đề 2.18 (Proposition 2.18).** Nếu $h : A \to B$ là một đồng cấu vành, thì $h : A \to B$ là đơn ánh khi và chỉ khi $\operatorname{Ker} h = \{0\}$. (Ta cũng viết $\operatorname{Ker} h = (0)$.)

Hạt nhân của một đồng cấu vành là một nhóm con Abel của nhóm cộng $A$, nhưng nhìn chung nó không phải là một vành con của $A$, bởi vì nó có thể không chứa phần tử đơn vị nhân $1$. Tuy nhiên, nó thỏa mãn tính chất đóng kín mạnh hơn sau đây dưới phép nhân:
$$ab \in \operatorname{Ker} h \quad \text{và} \quad ba \in \operatorname{Ker} h \quad \text{với mọi } a \in \operatorname{Ker} h \text{ và mọi } b \in A.$$
Điều này là do nếu $h(a) = 0$, thì với mọi $b \in A$ ta có
$$h(ab) = h(a)h(b) = 0h(b) = 0 \quad \text{và} \quad h(ba) = h(b)h(a) = h(b)0 = 0.$$

> **Định nghĩa 2.21 (Definition 2.21).** Cho một vành $A$, một nhóm con cộng $I$ của $A$ thỏa mãn tính chất dưới đây
> $$ab \in I \quad \text{và} \quad ba \in I \quad \text{với mọi } a \in I \text{ và mọi } b \in A \tag{$*_{\text{ideal}}$}$$
> được gọi là một *iđêan hai phía* (*two-sided ideal*). Nếu $A$ là một vành giao hoán, ta gọi đơn giản là một *iđêan* (*ideal*).

Hóa ra là với mọi vành $A$ và mọi iđêan hai phía $I$, tập hợp $A/I$ gồm các lớp ghép cộng $a + I$ (với $a \in A$) lập thành một vành được gọi là *vành thương* (*quotient ring*). Khi đó ta có kết quả tương tự với Mệnh đề 2.12 dưới đây, cũng được gọi là *định lý đẳng cấu thứ nhất* (*first isomorphism theorem*).

<!-- PAGE 52 -->

> **Mệnh đề 2.19 (Proposition 2.19).** Cho một đồng cấu vành $h : A \to B$, hai vành $A/\operatorname{Ker} h$ và $\operatorname{Im} h = h(A)$ là đẳng cấu với nhau.

Một trường (*field*) là một vành giao hoán $K$ mà trong đó $K - \{0\}$ là một nhóm dưới phép nhân.

> **Định nghĩa 2.22 (Definition 2.22).** Một tập hợp $K$ là một *trường* (*field*) nếu nó là một vành và các tính chất sau đây thỏa mãn:
> - **(F1)** $0 \neq 1$;
> - **(F2)** Với mọi $a \in K$, nếu $a \neq 0$, thì $a$ có phần tử nghịch đảo đối với phép $*$;
> - **(F3)** $*$ có tính giao hoán.

Đặt $K^* = K - \{0\}$. Chú ý rằng (F1) và (F2) tương đương với việc $K^*$ là một nhóm đối với phép $*$ với phần tử đơn vị $1$. Nếu $*$ không giao hoán nhưng (F1) và (F2) thỏa mãn, ta nói rằng ta có một *thể* hay *trường không giao hoán* (*skew field* hoặc *noncommutative field*).

Lưu ý rằng chúng ta đang giả định phép toán $*$ của một trường là giao hoán. Quy ước này không phải lúc nào cũng được mọi tác giả áp dụng chung, nhưng vì phép $*$ sẽ giao hoán đối với hầu hết các trường mà chúng ta gặp, nên ta đưa luôn điều kiện này vào trong định nghĩa.

> **Ví dụ 2.14 (Example 2.14).**
> 1. Các vành $\mathbb{Q}$, $\mathbb{R}$, và $\mathbb{C}$ là các trường.
> 2. Tập hợp các phân thức (hình thức) $f(X)/g(X)$ của các đa thức $f(X), g(X) \in \mathbb{R}[X]$, trong đó $g(X)$ không phải là đa thức không, là một trường.
> 3. Vành $\mathcal{C}(a, b)$ gồm các hàm liên tục $f : (a, b) \to \mathbb{R}$ sao cho $f(x) \neq 0$ với mọi $x \in (a, b)$ có các phần tử khả nghịch nhân trong $\mathcal{C}(a, b)$ (trong bản gốc tác giả nêu làm ví dụ về tính khả nghịch của các hàm không triệt tiêu trên $(a, b)$).
> 4. Sử dụng Mệnh đề 2.17, dễ thấy rằng vành $\mathbb{Z}/p\mathbb{Z}$ là một trường khi và chỉ khi $p$ là số nguyên tố.
> 5. Nếu $d$ là một số nguyên dương square-free và $d \ge 2$, tập hợp
>    $$\mathbb{Q}(\sqrt{d}) = \{a + b\sqrt{d} \in \mathbb{R} \mid a, b \in \mathbb{Q}\}$$
>    là một trường. Nếu $z = a + b\sqrt{d} \in \mathbb{Q}(\sqrt{d})$ và $\overline{z} = a - b\sqrt{d}$, thì dễ dàng kiểm tra được rằng nếu $z \neq 0$, thì $z^{-1} = \overline{z}/(z\overline{z})$.
> 6. Tương tự, nếu $d \ge 1$ là một số nguyên dương square-free, tập hợp các số phức
>    $$\mathbb{Q}(\sqrt{-d}) = \{a + ib\sqrt{d} \in \mathbb{C} \mid a, b \in \mathbb{Q}\}$$
>    là một trường. Nếu $z = a + ib\sqrt{d} \in \mathbb{Q}(\sqrt{-d})$ và $\overline{z} = a - ib\sqrt{d}$, thì dễ dàng kiểm tra được rằng nếu $z \neq 0$, thì $z^{-1} = \overline{z}/(z\overline{z})$.

<!-- PAGE 53 -->

> **Định nghĩa 2.23 (Definition 2.23).** Một *đồng cấu* (*homomorphism*) $h : K_1 \to K_2$ giữa hai trường $K_1$ và $K_2$ đơn giản là một đồng cấu giữa hai vành $K_1$ và $K_2$.

Tuy nhiên, bởi vì $K_1^*$ và $K_2^*$ là các nhóm dưới phép nhân, một đồng cấu giữa các trường bắt buộc phải là đơn ánh (*injective*).

*Chứng minh (Proof).* Trước hết, chú ý rằng với mọi $x \neq 0$,
$$1 = h(1) = h(x x^{-1}) = h(x)h(x^{-1})$$
và
$$1 = h(1) = h(x^{-1} x) = h(x^{-1})h(x),$$
do đó $h(x) \neq 0$ và
$$h(x^{-1}) = h(x)^{-1}.$$
Nhưng khi đó, nếu $h(x) = 0$, ta buộc phải có $x = 0$. Hệ quả là $h$ là đơn ánh. $\square$

> **Định nghĩa 2.24 (Definition 2.24).** Một đồng cấu trường $h : K_1 \to K_2$ là một *đẳng cấu* (*isomorphism*) khi và chỉ khi tồn tại một đồng cấu $g : K_2 \to K_1$ sao cho $g \circ h = \mathrm{id}_{K_1}$ và $h \circ g = \mathrm{id}_{K_2}$. Một đẳng cấu từ một trường vào chính nó được gọi là một *tự đẳng cấu* (*automorphism*).

Khi đó, giống như trong trường hợp của vành, $g$ là duy nhất và được ký hiệu bởi $h^{-1}$, đồng thời một đồng cấu trường song ánh $h : K_1 \to K_2$ là một đẳng cấu.

> **Định nghĩa 2.25 (Definition 2.25).** Vì mọi đồng cấu $h : K_1 \to K_2$ giữa hai trường đều là đơn ánh, ảnh $h(K_1)$ của $K_1$ là một *trường con* (*subfield*) của $K_2$. Ta nói rằng $K_2$ là một *mở rộng trường* (*extension*) của $K_1$.

Ví dụ, $\mathbb{R}$ là một mở rộng của $\mathbb{Q}$ và $\mathbb{C}$ là một mở rộng của $\mathbb{R}$. Các trường $\mathbb{Q}(\sqrt{d})$ và $\mathbb{Q}(\sqrt{-d})$ là các mở rộng của $\mathbb{Q}$, trường $\mathbb{R}$ là một mở rộng của $\mathbb{Q}(\sqrt{d})$ và trường $\mathbb{C}$ là một mở rộng của $\mathbb{Q}(\sqrt{-d})$.

> **Định nghĩa 2.26 (Definition 2.26).** Một trường $K$ được gọi là *đóng đại số* (*algebraically closed*) nếu mọi đa thức khác hằng $p(X)$ với hệ số trong $K$ đều có ít nhất một nghiệm (*root*) trong $K$; nghĩa là tồn tại một phần tử $a \in K$ sao cho $p(a) = 0$.

Có thể chứng minh rằng mọi trường $K$ đều có một mở rộng tối tiểu $\Omega$ đóng đại số, được gọi là một *bao đóng đại số* (*algebraic closure*) của $K$. Ví dụ, $\mathbb{C}$ là bao đóng đại số của $\mathbb{R}$. Bao đóng đại số của $\mathbb{Q}$ được gọi là *trường các số đại số* (*field of algebraic numbers*). Trường này bao gồm tất cả các số phức là nghiệm của một đa thức có hệ số trong $\mathbb{Q}$.

> **Định nghĩa 2.27 (Definition 2.27).** Cho một trường $K$ và một tự đẳng cấu $h : K \to K$ của $K$, dễ dàng kiểm tra được rằng tập hợp
> $$\operatorname{Fix}(h) = \{a \in K \mid h(a) = a\}$$
> gồm các phần tử của $K$ bất động dưới $h$ là một trường con của $K$, được gọi là *trường bất động bởi $h$* (*field fixed by $h$*).

<!-- PAGE 54 -->

Ví dụ, nếu $d \ge 2$ là số nguyên square-free, thì ánh xạ $c : \mathbb{Q}(\sqrt{d}) \to \mathbb{Q}(\sqrt{d})$ được cho bởi
$$c(a + b\sqrt{d}) = a - b\sqrt{d}$$
là một tự đẳng cấu của $\mathbb{Q}(\sqrt{d})$, và $\operatorname{Fix}(c) = \mathbb{Q}$.

Nếu $K$ là một trường, ta có đồng cấu vành $h : \mathbb{Z} \to K$ cho bởi $h(n) = n \cdot 1$. Nếu $h$ là đơn ánh, thì $K$ chứa một bản sao của $\mathbb{Z}$, và vì nó là một trường nên nó chứa một bản sao của $\mathbb{Q}$. Trong trường hợp này, ta nói $K$ có *đặc số $0$* (*characteristic $0$*). Nếu $h$ không phải là đơn ánh, thì $h(\mathbb{Z})$ là một vành con của $K$, và do đó là một miền nguyên; hạt nhân của $h$ là một nhóm con của $\mathbb{Z}$, nên theo Mệnh đề 2.15 nó phải có dạng $p\mathbb{Z}$ với một số $p \ge 1$ nào đó. Theo định lý đẳng cấu thứ nhất, $h(\mathbb{Z})$ đẳng cấu với $\mathbb{Z}/p\mathbb{Z}$ với $p \ge 1$. Nhưng khi đó, $p$ bắt buộc phải là số nguyên tố vì $\mathbb{Z}/p\mathbb{Z}$ là một miền nguyên khi và chỉ khi nó là một trường, tức khi và chỉ khi $p$ là số nguyên tố. Số nguyên tố $p$ này được gọi là *đặc số* (*characteristic*) của $K$, và ta cũng nói rằng $K$ có *đặc số hữu hạn* (*finite characteristic*).

> **Định nghĩa 2.28 (Definition 2.28).** Nếu $K$ là một trường, thì một trong hai trường hợp sau xảy ra:
> 1. $n \cdot 1 \neq 0$ với mọi số nguyên $n \ge 1$, trong trường hợp đó ta nói $K$ có *đặc số $0$* (*characteristic $0$*), hoặc
> 2. Tồn tại một số nguyên tố nhỏ nhất $p$ sao cho $p \cdot 1 = 0$, được gọi là *đặc số* (*characteristic*) của $K$, và ta nói $K$ có *đặc số hữu hạn* (*finite characteristic*).

Một trường $K$ có đặc số $0$ chứa một bản sao của $\mathbb{Q}$, do đó là trường vô hạn. Như chúng ta sẽ thấy trong Mục 8.10, một trường hữu hạn luôn có đặc số $p$ khác không. Tuy nhiên, cũng tồn tại những trường vô hạn có đặc số khác không.

[^2]: Ký hiệu $\mathbb{Z}_n$ đôi khi được sử dụng thay cho $\mathbb{Z}/n\mathbb{Z}$, nhưng nó trùng với ký hiệu cho các số nguyên $n$-adic (*$n$-adic integers*) nên chúng tôi ưu tiên không sử dụng ký hiệu đó.
