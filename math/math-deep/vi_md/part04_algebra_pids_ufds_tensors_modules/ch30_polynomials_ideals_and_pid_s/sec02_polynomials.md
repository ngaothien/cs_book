# Các đa thức


<!-- PAGE 1068 -->
$M$ sao cho M(i) $= k_{i}$ với mọi $i, 1 \le i \le n$, được ký hiệu bởi $k_{1} \cdot  1 + \cdots  + k_{n} \cdot  n$, hoặc nhiều hơn/thêm đơn giản, bởi $(k_{1}, \dots  , k_{n})$, và $deg(k_{1} \cdot  1 + \cdots  + k_{n} \cdot  n) = k_{1} + \cdots  + k_{n}$ là kích thước hoặc bậc của $M$. Tập hợp tất cả các đa tập hợp trên I được ký hiệu bởi $\mathbb{N}^{(I)}$, và khi $I = {1, \dots  , n}$, bởi $\mathbb{N}^{(n)}$. Một cách trực quan, thứ tự của các phần tử của đa tập hợp (multiset) là irrelevant, nhưng bội (multiplicity) của mỗi phần tử là relevant, trái với các tập hợp. Mọi $i \in$ I được đồng nhất với đa tập hợp (multiset) $M_{i}$ như vậy
$$\mathbb{N}^{(1)}$$
Rằng $M_{i}(i) = 1$ và $M_{i}(j) = 0$ cho $j \neq  i$. Khi $I = {1}$, tập hợp của các đa tập hợp $k \cdot  1$ có thể được đồng nhất với $\mathbb{N}$ và ${1}^{*}$. Ta sẽ ký hiệu $k \cdot  1$ đơn giản bởi $k$.
$$\mathbb{N}^{(n)}$$
 Tuy nhiên, beware rằng khi $n \ge 2$, tập hợp của các đa tập hợp không thể được đồng nhất với tập hợp của các chuỗi trong ${1, \dots  , n}^{*}$, bởi vì đa tập hợp (multiset) hợp là giao hoán, nhưng concatenation của các chuỗi trong ${1, \dots  , n}^{*}$ là không giao hoán khi $n \ge 2$. Điều này là bởi vì trong đa tập hợp (multiset) $k_{1} \cdot  1 + \cdots  + k_{n} \cdot  n$, thứ tự là irrelevant, trong khi đó trong chuỗi, thứ tự là relevant. Ví dụ, $2 \cdot  1 + 3 \cdot  2 = 3 \cdot  2 + 2 \cdot  1$, nhưng $11222 \neq  22211$, như các chuỗi trên ${1, 2}$.
$$\mathbb{N}^{(n)}  \mathbb{N}^{n}$$
Nevertherless, và tập hợp của được thứ tự các bộ $n$ dưới component-wise phép cộng là đẳng cấu dưới ánh xạ
$$k_{1} \cdot  1 + \cdots  + k_{n} \cdot  n \mapsto (k_{1}, \dots  , k_{n}).$$
Do đó, vì ký hiệu $(k_{1}, \dots  , k_{n})$ là ít hơn cumbersome rằng $k_{1} \cdot  1 + \cdots  + k_{n} \cdot  n$, nó sẽ là preferred. Ta chỉ có đến nhớ rằng thứ tự của $k_{i}$ là một cách thực irrelevant.
$$\mathbb{N}^{(I)}  \mathbb{N}^{I}$$
 Nhưng khi I là vô hạn, beware rằng và tập hợp của được thứ tự các bộ $I$ là không đẳng cấu. Ta là bây giờ ready để định nghĩa các đa thức.

## 30.2 Các đa thức

Ta bắt đầu với các đa thức trong một biến.

> **Định nghĩa 30.2.** Cho trước vành $A$, ta định nghĩa tập hợp $\mathcal{P}_{A}(1)$ của các đa thức trên $A$ trong một biến như tập hợp của các hàm $P$: $\mathbb{N} \to A$ sao cho P(k) $\neq  0$ cho một cách hữu hạn nhiều $k \in \mathbb{N}$. đa thức sao cho P(k) $= 0$ với mọi $k \in \mathbb{N}$ là null (hoặc không) đa thức và nó được ký hiệu bởi $0$. Ta định nghĩa phép cộng của các đa thức, phép nhân bởi vô hướng (scalar), và phép nhân của các đa thức, như sau: Cho trước bất kỳ ba các đa thức $P, Q, R \in P_{A}(1)$, đặt $a_{k} =$ P(k), $b_{k} =$ Q(k), và $c_{k} =$ R(k), với mọi $k \in \mathbb{N}$, ta định nghĩa $R = P + Q$ sao cho
$$c_{k} = a_{k} + b_{k},$$
$R = \lambda P$ sao cho
$$c_{k} = \lambda a_{k},$$
Ở đâu $\lambda  \in A$,

<!-- PAGE 1069 -->
Và $R = PQ$ sao cho
$$c_{k} = \sum_{i+j=k}  a_{i}b_{j}.$$
Ta định nghĩa đa thức $e_{k}$ sao cho $e_{k}(k) = 1$ và $e_{k}(i) = 0$ cho $i \neq  k$. Ta cũng ký hiệu $e_{0}$ bởi $1$ khi $k = 0$. Cho trước đa thức $P$, $a_{k} =$ P(k) $\in A$ được gọi là các hệ số của $P$. Nếu $P$ là không null đa thức, có một lớn nhất $n \ge 0$ sao cho $a_{n} \neq  0$ (và do đó, $a_{k} = 0$ với mọi $k > n)$ được gọi là bậc của $P$ và được ký hiệu bởi deg(P). Thì, $P$ được viết một cách duy nhất như
$$P = a_{0}e_{0} + a_{1}e_{1} + \cdots  + a_{n}e_{n}.$$
Khi $P$ là null đa thức, ta cho deg(P) $= -\infty$. Có một đơn ánh của $A into\mathcal{P}_{A}(1)$ cho trước bởi ánh xạ $a \mapsto$ a1 (nhắc lại rằng $1$ ký hiệu $e_{0})$. Ở đó là cũng đơn ánh của $\mathbb{N}$ vào $\mathcal{P}_{A}(1)$ cho trước bởi ánh xạ $k \mapsto e_{k}$. Nhận thấy rằng $e_{k} = e_{1}^{k}$ (với $e_{1}^{0} = e_{0} = 1)$. Trong thứ tự đến alleviate ký hiệu, ta thường ký hiệu $e_{1}$ bởi $X$, và ta gọi $X$ biến (hoặc indeterminate). Thì, $e_{k} = e_{1}^{k}$ được ký hiệu bởi $X^{k}$. Áp dụng điều này ký hiệu, cho trước khác không đa thức $P$ của bậc $n$, nếu P(k) $= a_{k}, P$ được ký hiệu bởi
$$P = a_{0} + a_{1}X + \cdots  + a_{n}X^{n},$$
Hoặc bởi
$$P = a_{n}X^{n}+ a_{n-1}X^{n-1}+ \cdots  + a_{0},$$
Nếu điều này là nhiều hơn/thêm thuận tiện (thứ tự của các số hạng thực hiện không matter anyway). Đôi khi, nó sẽ cũng là thuận tiện đến viết đa thức như
$$P = a_{0}X^{n}+ a_{1}X^{n-1}+ \cdots  + a_{n}.$$
Tập hợp $\mathcal{P}_{A}(1)$ cũng được ký hiệu bởi [X] và đa thức $P$ có thể được ký hiệu bởi P(X). Trong ký hiệu các đa thức, ta sẽ sử dụng cả hai upper-case và lower-case letters, thường, $P, Q, R, S, p, q, r, s$, nhưng cũng $f, g, h$, etc., nếu cần thiết (như dài như không có ambiguities phát sinh). Cho trước khác không đa thức $P$ của bậc $n$, khác không hệ số $a_{n}$ được gọi là dẫn đầu hệ số của $P$. hệ số $a_{0}$ được gọi là hằng số số hạng của $P$. đa thức của tạo thành $a_{k}X^{k}$ được gọi là một đơn thức. Ta nói rằng $a_{k}X^{k}$ xảy ra trong $P$ nếu $a_{k}$ ̸ $= 0$. khác không đa thức $P$ của bậc $n$ được gọi là một chuẩn hóa (monic) đa thức (hoặc unita đa thức, hoặc chuẩn hóa (monic)) nếu $a_{n} = 1$, ở đâu $a_{n}$ là của nó dẫn đầu hệ số, và như vậy đa thức có thể được viết dưới dạng
$$P = X^{n}+ a_{n-1}X^{n-1}+ \cdots  + a_{0}orP = X^{n}+ a_{1}X^{n-1}+ \cdots  + a_{n}.$$
 lựa chọn của biến $X$ đến ký hiệu $e_{1}$ là tiêu chuẩn practice, nhưng ở đó là không có gì đặc biệt về $X$. Ta có thể có được chọn $Y , Z$, hoặc bất kỳ khác ký hiệu, như dài như không có ambiguities phát sinh.

<!-- PAGE 1070 -->
Một cách hình thức, định nghĩa của $\mathcal{P}_{A}(1)$ có không có gì đến thực hiện với $X$. lý do cho bằng cách sử dụng $X$ là đơn giản convenience. Thật vậy, nó là nhiều hơn/thêm thuận tiện đến viết đa thức như $P = a_{0} + a_{1}X + \cdots  + a_{n}X^{n}$ thay vì như $P = a_{0}e_{0} + a_{1}e_{1} + \cdots  + a_{n}e_{n}$. Ta có kết quả sau đơn giản nhưng then chốt mệnh đề.

> **Mệnh đề 30.1.** Cho trước hai khác không các đa thức P(X) $= a_{0}+a_{1}X +\cdots +a_{m}X^{m}$ của bậc $m$ và Q(X) $= b_{0} + b_{1}X + \cdots  + b_{n}X^{n}$ của bậc $n$, nếu hoặc $a_{m}$ hoặc $b_{n}$ là không không ước, thì $a_{m}b_{n} \neq  0$, và do đó, PQ $\neq  0$ và
$$deg(PQ) = deg(P) + deg(Q).$$
Đặc biệt, nếu $A$ là miền nguyên (integral domain), thì [X] là miền nguyên (integral domain).

*Chứng minh.* Vì hệ số của $X^{m+n}$ trong PQ là $a_{m}b_{n}$, và vì ta được giả sử rằng hoặc $a_{m}$ hoặc $a_{n}$ là không không ước, ta có $a_{m}b_{n} \neq  0$, và do đó, PQ $\neq  0$ và
$$deg(PQ) = deg(P) + deg(Q).$$
Thì, hiển nhiên là [X] là miền nguyên (integral domain). Dễ dàng kiểm chứng được rằng [X] là vành giao hoán (commutative ring), với multiplicative đồng nhất thức $1X^{0} = 1$. Nó là cũng dễ dàng được kiểm chứng rằng [X] thỏa mãn tất cả các điều kiện của Định nghĩa 3.1, nhưng [X] là không không gian vectơ (vector space), vì $A$ là không nhất thiết trường. cấu trúc thỏa mãn axioms của Định nghĩa 3.1 khi $K$ là vành (và không nhất thiết trường) được gọi là một môđun. Các môđun thất bại đến có một số của đẹp các tính chất rằng các không gian vectơ có, và do đó, chúng là khó hơn đến study. Ví dụ, có các môđun rằng thực hiện không có cơ sở (basis). Ta postpone study của các môđun cho đến khi Chương $35$. Tuy nhiên, khi vành $A$ là trường, [X] là không gian vectơ (vector space). Nhưng chẵn/ngay cả khi $A$ là chỉ vành, họ của các đa thức $(X^{k})_{k\in N}$ là cơ sở (basis) của [X], vì mọi đa thức P(X) có thể được được viết trong duy nhất cách như P(X) $= a_{0} + a_{1}X + \cdots  + a_{n}X^{n}$ (với P(X) $= 0$ khi P(X) là null đa thức). Do đó, [X] là môđun tự do (free module). Tiếp theo, ta muốn để định nghĩa khái niệm của evaluating đa thức P(X) tại một số $\alpha  \in A$. Cho điều này, ta cần mệnh đề.

> **Mệnh đề 30.2.** Cho $A, B$ là hai các vành và cho $h: A \to B$ là vành đồng cấu. Với mọi $\beta  \in B$, tồn tại duy nhất một vành đồng cấu $\phi$: [X] $\to B$ mở rộng $h$ sao cho $\phi (X) = \beta$, như trong sau đây biểu đồ (ở đâu ta ký hiệu bởi $h+\beta$ ánh xạ $h+\beta$: $A\cup {X} \to B$ sao cho $(h + \beta )(a) =$ h() với mọi $a \in A$ và $(h + \beta )(X) = \beta$):
$$A \cup {X}\iota A[X]$$
$$LL$$
$$LL$$
$$LL$$
$$LL$$
$$h+\beta LL^{\phi}$$
$$%$$
$$B$$

<!-- PAGE 1071 -->

*Chứng minh.* Cho $\phi (0) = 0$, và với mọi nonull đa thức P(X) $= a_{0} + a_{1}X + \cdots  + a_{n}X^{n}$, cho
$$\phi (P(X)) = h(a_{0}) + h(a_{1})\beta  + \cdots  + h(a_{n})\beta^{n} .$$
Dễ dàng kiểm chứng được rằng $\phi$ là duy nhất đồng cấu $\phi$: [X] $\to B$ mở rộng $h$ sao cho $\phi (X) = \beta$. Lấy $A = B$ trong Mệnh đề 30.2 và $h: A \to A$ đồng nhất thức, với mọi $\beta  \in A$, tồn tại duy nhất một đồng cấu $\phi_{\beta}$: [X] $\to A$ sao cho $\phi_{\beta} (X) = \beta$, và với mọi đa thức P(X), ta viết $\phi_{\beta}$ (P(X)) như $P(\beta$) và ta gọi $P(\beta$) giá trị của P(X) tại $X = \beta$. Do đó, ta có thể định nghĩa hàm $P_{A}$: $A \to A$ sao cho $P_{A}(\beta$) $= P(\beta$), với mọi $\beta  \in A$. hàm này được gọi là đa thức hàm được cảm sinh bởi $P$. Tổng quát hơn, $P_{B}$ có thể được được định nghĩa với mọi (giao hoán) vành $B$ sao cho $A \subseteq B$. Nói chung, nó là khả dĩ/có thể rằng $P_{A} = Q_{A}$ cho phân biệt các đa thức $P, Q$. Ta sẽ xem một cách ngắn các điều kiện cho mà ánh xạ $P \mapsto P_{A}$ là đơn ánh (injective). Đặc biệt, điều này là đúng cho $A = \mathbb{R}$ (nói chung, bất kỳ vô hạn miền nguyên (integral domain)). Ta bây giờ định nghĩa các đa thức trong $n$ các biến.

> **Định nghĩa 30.3.** Cho trước $n \ge 1$ và vành $A$, tập hợp $\mathcal{P}_{A}(n)$ của các đa thức trên $A$ trong $n$
$$\mathbb{N}^{(n)}$$
Các biến là tập hợp của các hàm $P$: $\to A$ sao cho $P(k_{1}, \dots  , k_{n}) \neq  0$ cho một cách hữu hạn nhiều $(k_{1}, \dots  , k_{n}) \in \mathbb{N}^{(n)}$. đa thức sao cho $P(k_{1}, \dots  , k_{n}) = 0$ với mọi $(k_{1}, \dots  , k_{n})$ là null (hoặc không) đa thức và nó được ký hiệu bởi $0$. Ta định nghĩa phép cộng của các đa thức, phép nhân bởi vô hướng (scalar), và phép nhân của các đa thức, như sau: Cho trước bất kỳ ba các đa thức $P, Q, R \in P_{A}(n)$, đặt $a_{(k1,...,kn)} = P(k_{1}, \dots  , k_{n}), b_{(k1,...,kn)} = Q(k_{1}, \dots  , k_{n}), c_{(k1,...,kn)} = R(k_{1}, \dots  , k_{n})$, với mọi $(k_{1}, \dots  , k_{n}) \in \mathbb{N}^{(n)}$, ta định nghĩa $R = P + Q$ sao cho
$$c_{(k1,...,kn)} = a_{(k1,...,kn)} + b_{(k1,...,kn)},$$
$R = \lambda P$, ở đâu $\lambda  \in A$, sao cho
$$c_{(k1,...,kn)} = \lambda a_{(k1,...,kn)},$$
Và $R = PQ$, sao cho
$$c_{(k1,...,kn)} = \sum_{1,...,jn}  a_{(i1,...,in)}b_{(j1,...,jn)}.$$
$$(i1,...,in)+(j)=(k1,...,kn)$$
Với mọi $(k_{1}, \dots  , k_{n}) \in \mathbb{N}^{(n)}$, ta cho $e_{(k1,...,kn)}$ là đa thức sao cho
$$e_{(k1,...,kn)}(k_{1}, \dots  , k_{n}) = 1ande_{(k1,...,kn)}(h_{1}, \dots  , h_{n}) = 0,$$
Cho $(h_{1}, \dots  , h_{n})̸ = (k_{1}, \dots  , k_{n})$. Ta cũng ký hiệu $e_{(0,...,0)}$ bởi $1$. Cho trước đa thức $P$, $a_{(k1,...,kn)} = P(k_{1}, \dots  , k_{n}) \in A$, được gọi là các hệ số của $P$. Nếu $P$ là không null đa thức, có một lớn nhất $d \ge 0$ sao cho $a_{(k1,...,kn)} = 0$ với một số $(k_{1}, \dots  , k_{n}) \in \mathbb{N}^{(n)}$, với $d =$
$$̸$$
$k_{1} + \cdots  + k_{n}$, được gọi là tổng bậc của $P$ và được ký hiệu bởi deg(P). Thì, $P$ được viết một cách duy nhất như
$$P = \sum_{,...,kn)\in}  a_{(k1,...,kn)}e_{(k1,...,kn)}.$$
$$(k\mathbb{N}(n)$$
$$1$$
Khi $P$ là null đa thức, ta cho deg(P) $= -\infty$.

<!-- PAGE 1072 -->
Có một đơn ánh của $A into\mathcal{P}_{A}(n)$ cho trước bởi ánh xạ $a \mapsto$ a1 (ở đâu $1$ ký hiệu $e_{(0,...,0)})$.
$$\mathbb{N}^{(n)}$$
Ở đó là cũng đơn ánh của $into\mathcal{P}_{A}(n)$ cho trước bởi ánh xạ $(h_{1}, \dots  , h_{n}) \mapsto e_{(h1,...,hn)}$. Lưu ý rằng $e_{(h1,...,hn)}e_{(k1,...,kn)} = e_{(h1+k1,...,hn+kn)}$. Trong thứ tự đến alleviate ký hiệu, cho $X_{1}, \dots  , X_{n}$ là $n$ phân biệt các biến và ký hiệu $e_{(0,...,0,1,0...,0)}$, ở đâu $1$ xảy ra trong position $i$, bởi $X_{i}$ (ở đâu $1 \le i \le n)$. Với điều này quy ước, xét theo $e_{(h1,...,hn)}e_{(k1,...,kn)} = e_{(h1+k1,...,hn+kn)}$, đa thức $e_{(k1,...,kn)}$ được ký hiệu bởi $X_{1}^{k1} \cdots  X_{n}^{kn}$ (với $e_{(0,...,0)} = X_{1}^{0} \cdots  X_{n}^{0} = 1)$ và nó được gọi là một primitive đơn thức. Thì, $P$ cũng được viết như
$$P = \sum_{,...,kn)\in}  a_{(k1,...,kn)}X_{1}^{k1} \cdots  X_{n}^{kn} .$$
$$(k\mathbb{N}(n)$$
$$1$$
Ta cũng ký hiệu $\mathcal{P}_{A}(n)$ bởi $A[X_{1}, \dots  , X_{n}]$. đa thức $P \in A[X_{1}, \dots  , X_{n}]$ cũng được ký hiệu bởi $P(X_{1}, \dots  , X_{n})$. Như trong trường hợp $n = 1$, ở đó là không có gì đặc biệt về lựa chọn của $X_{1}, \dots  , X_{n}$ như các biến (hoặc indeterminates). Nó là chỉ convenience. Sau tất cả, cách xây dựng $of\mathcal{P}_{A}(n)$ có không có gì đến thực hiện với $X_{1}, \dots  , X_{n}$. Cho trước khác không đa thức $P$ của bậc $d$, khác không các hệ số $a_{(k1,...,kn)}$ ̸ $= 0$ sao cho $d = k_{1} + \cdots  + k_{n}$ được gọi là dẫn đầu các hệ số của $P$. đa thức của tạo thành $a_{(k1,...,kn)}X_{1}^{k1} \cdots  X_{n}^{kn}$ được gọi là một đơn thức. Lưu ý rằng $deg(a_{(k1,...,kn)}X_{1}^{k1} \cdots  X_{n}^{kn}$) $= k_{1}+\cdots +k_{n}$. Cho trước đa thức
$$P = \sum_{,...,kn)\in}  a_{(k1,...,kn)}X_{1}^{k1} \cdots  X_{n}^{kn} ,$$
$$(k\mathbb{N}(n)$$
$$1$$
Đơn thức $a_{(k1,...,kn)}X_{1}^{k1} \cdots  X_{n}^{kn}$ xảy ra trong đa thức $P$ nếu $a_{(k1,...,kn)} \neq  0$. đa thức
$$P = \sum_{,...,kn)\in}  a_{(k1,...,kn)}X_{1}^{k1} \cdots  X_{n}^{kn}$$
$$(k\mathbb{N}(n)$$
$$1$$
Là thuần nhất của bậc $d$ nếu
$$deg(X_{1}^{k1} \cdots  X_{n}^{kn} ) = d,$$
Với mọi đơn thức $a_{(k1,...,kn)}X_{1}^{k1} \cdots  X_{n}^{kn}$ xảy ra trong $P$. Nếu $P$ là đa thức của tổng bậc $d$, rõ ràng là $P$ có thể được được viết một cách duy nhất như
$$P = P^{(0)}+ P^{(1)}+ \cdots  + P^{(d)},$$
Ở đâu $P^{(i)}$ là tổng của tất cả các đơn thức của bậc $i$ xảy ra trong $P$, ở đâu $0 \le i \le d$. Dễ dàng kiểm chứng được rằng $A[X_{1}, \dots  , X_{n}]$ là vành giao hoán (commutative ring), với multiplicative đồng nhất thức $1X_{1}^{0} \cdots  X_{n}^{0} = 1$. Nó là cũng dễ dàng được kiểm chứng rằng [X] là môđun. Khi $A$ là trường, [X] là không gian vectơ (vector space). Chẵn/ngay cả khi $A$ là chỉ vành, họ của các đa thức
$$(X_{1}^{k1} \cdots  X_{n}^{kn} )_{(k1,...,kn)\in N(n)}$$

<!-- PAGE 1073 -->
Là cơ sở (basis) của $A[X_{1}, \dots  , X_{n}]$, vì mọi đa thức $P(X_{1}, \dots  , X_{n})$ có thể được được viết trong duy nhất cách như
$$P(X_{1}, \dots  , X_{n}) = \sum_{,...,kn)\in}  a_{(k1,...,kn)}X_{1}^{k1} \cdots  X_{n}^{kn} .$$
$$(k\mathbb{N}(n)$$
$$1$$
Do đó, $A[X_{1}, \dots  , X_{n}]$ là môđun tự do (free module).
Nhận xét: cách xây dựng của Định nghĩa 30.3 có thể được ngay lập tức được mở rộng đến tùy ý tập hợp $I$, và không chỉ $I = {1, \dots  , n}$. Nó có thể cũng là ứng dụng đến các vị nhóm (monoid) nhiều hơn/thêm tổng quát $that\mathbb{N}^{(I)}$. Mệnh đề 30.2 là suy rộng/tổng quát hóa như sau.

> **Mệnh đề 30.3.** Cho $A, B$ là hai các vành và cho $h: A \to B$ là vành đồng cấu. Với mọi $\beta  = (\beta_{1} , \dots  , \beta_{n}$) $\in B^{n}$, tồn tại duy nhất một vành đồng cấu $\phi$: $A[X_{1}, \dots  , X_{n}] \to B$ mở rộng $h$ sao cho $\phi (X_{i}) = \beta_{i} , 1 \le i \le n$, như trong sau đây biểu đồ (ở đâu ta ký hiệu bởi $h + \beta$ ánh xạ $h + \beta$: $A \cup {X_{1}, \dots  , X_{n}} \to B$ sao cho $(h + \beta )(a) =$ h() với mọi $a \in A$ và $(h + \beta )(X_{i}) = \beta_{i} , 1 \le i \le n)$:
$$A \cup {X_{1}, \dots  , X_{n}}\iota A[X_{1}, \dots  , X_{n}]$$
$$TTT$$
$$TTT$$
$$TTT$$
$$TT\phi$$
$$TTT$$
$$h+\beta TTT$$
$$)$$
$$B$$

*Chứng minh.* Cho $\phi (0) = 0$, và với mọi nonull đa thức
$$P(X_{1}, \dots  , X_{n}) = \sum_{,...,kn)\in}  a_{(k1,...,kn)}X_{1}^{k1} \cdots  X_{n}^{kn} ,$$
$$(k\mathbb{N}(n)$$
$$1$$
Cho
$$\phi (P(X_{1}, \dots  , X_{n})) = \sum  h(a_{(k1,...,kn)})\beta_{1}^{k1}  \cdots  \beta_{n}^{kn}  .$$
Dễ dàng kiểm chứng được rằng $\phi$ là duy nhất đồng cấu $\phi$: $A[X_{1}, \dots  , X_{n}] \to B$ mở rộng $h$ sao cho $\phi (X_{i}) = \beta_{i}$. Lấy $A = B$ trong Mệnh đề 30.3 và $h: A \to A$ đồng nhất thức, với mọi $\beta_{1} , \dots  , \beta_{n}  \in A$, tồn tại duy nhất một đồng cấu $\phi$: $A[X_{1}, \dots  , X_{n}] \to A$ sao cho $\phi (X_{i}) = \beta_{i}$, và với mọi đa thức $P(X_{1}, \dots  , X_{n})$, ta viết $\phi (P(X_{1}, \dots  , X_{n}))$ như $P(\beta_{1} , \dots  , \beta_{n}$) và ta gọi $P(\beta_{1} , \dots  , \beta_{n}$) giá trị của $P(X_{1}, \dots  , X_{n})$ tại $X_{1} = \beta_{1} , \dots  , X_{n} = \beta_{n}$. Do đó, ta có thể định nghĩa hàm $P_{A}$: $A^{n} \to A$ sao cho $P_{A}(\beta_{1} , \dots  , \beta_{n}$) $= P(\beta_{1} , \dots  , \beta_{n}$), với mọi $\beta_{1} , \dots  , \beta_{n}  \in A$. hàm này được gọi là đa thức hàm được cảm sinh bởi $P$. Tổng quát hơn, $P_{B}$ có thể được được định nghĩa với mọi (giao hoán) vành $B$ sao cho $A \subseteq B$. Như trong trường hợp của đơn lẻ biến, nó là khả dĩ/có thể rằng $P_{A} = Q_{A}$ cho phân biệt các đa thức $P, Q$. Ta sẽ xem một cách ngắn rằng ánh xạ $P \mapsto P_{A}$ là đơn ánh (injective) khi $A = \mathbb{R}$ (nói chung, bất kỳ vô hạn miền nguyên (integral domain)).
