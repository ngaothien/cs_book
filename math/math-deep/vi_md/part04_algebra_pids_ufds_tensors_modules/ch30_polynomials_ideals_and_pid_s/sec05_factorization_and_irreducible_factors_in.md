# Nhân tử hóa và Bất khả quy (irreducible) Các nhân tử trong K[X]


<!-- PAGE 1084 -->
Ngoài ra, $d \neq  0$, và $d$ là duy nhất sai khác phép nhân bởi khác không vô hướng (scalar) trong $K$. Hệ quả là của Mệnh đề 30.15, một số các đa thức $f_{1}, \dots  , f_{n} \in$ K[X] là một cách tương đối nguyên tố khi và chỉ khi ở đó tồn tại $u_{1}, \dots  , u_{n} \in$ K[X] sao cho
$$u_{1}f_{1} + \cdots  + u_{n}f_{n} = 1.$$
Đồng nhất thức
$$u_{1}f_{1} + \cdots  + u_{n}f_{n} = 1$$
Của phần $(2)$ của Mệnh đề 30.15 cũng được gọi là Bezout đồng nhất thức. Ta bây giờ xét nhân tử hóa của các đa thức của đơn lẻ biến vào bất khả quy (irreducible) các nhân tử.

## 30.5 Nhân tử hóa và Bất khả quy (irreducible) Các nhân tử trong K[X]


> **Định nghĩa 30.9.** Cho trước trường $K$, đa thức $p \in$ K[X] là bất khả quy (irreducible) hoặc indecomposable hoặc nguyên tố nếu deg(p) $\ge 1$ và nếu $p$ là không chia hết bởi bất kỳ đa thức $q \in$ K[X] sao cho $1 \le$ deg(q) $<$ deg(p). Tương đương, $p$ là bất khả quy (irreducible) nếu deg(p) $\ge 1$ và nếu $p = q_{1}q_{2}$, thì hoặc $q_{1} \in K$ hoặc $q_{2} \in K$ (và của course, $q_{1} \neq  0, q_{2} \neq  0)$.

> **Ví dụ 30.2.** Mọi đa thức aX $+ b$ của bậc $1$ là bất khả quy (irreducible). Trên trường $\mathbb{R}$, đa thức $X^{2} + 1$ là bất khả quy (irreducible) (tại sao?), nhưng $X^{3} + 1$ là không bất khả quy (irreducible), vì
$$X^{3}+ 1 = (X + 1)(X^{2}-X + 1).$$
$$\mathbb{R}$$
Đa thức $X^{2}$ - $X + 1$ là bất khả quy (irreducible) trên (tại sao?). Nó sẽ dường như rằng $X^{4} + 1$ là bất khả quy (irreducible) trên $\mathbb{R}$, nhưng thực ra,
$$\sqrt\sqrt$$
$$X^{4}+ 1 = (X^{2}-\overline{2} X + 1)(X^{2}+\overline{2} X + 1).$$
$$\mathbb{Q}$$
Tuy nhiên, xét theo ở trên nhân tử hóa, $X^{4} + 1$ là bất khả quy (irreducible) trên. Nó có thể được được hiển thị rằng bất khả quy (irreducible) các đa thức $over\mathbb{R}$ là các đa thức của bậc $1$, hoặc các đa thức của bậc $2$ của tạo thành $aX^{2} +$ bX $+ c$, cho mà $b^{2}$ - 4ac $< 0$ (i.e., những phần tử đó có không có thực các nghiệm). Điều này là không dễ để chứng minh! Trên phức các số $\mathbb{C}$, chỉ bất khả quy (irreducible) các đa thức là những phần tử đó của bậc $1$. Điều này là phiên bản của sự kiện thường referred đến như “Cơ bản định lý của Đại số”, hoặc, như French đôi khi nói, như “d’Alembert’s định lý”! Ta đã được quan sát rằng với mọi hai khác không các đa thức $f, g \in$ K[X], $f$ chia hết $g$ khi và chỉ khi
$(g) \subseteq (f)$. Xét theo định nghĩa của lý tưởng cực đại (maximal ideal) cho trước trong Định nghĩa 30.4, ta bây giờ chứng minh rằng đa thức $p \in$ K[X] là bất khả quy (irreducible) khi và chỉ khi(p) là lý tưởng cực đại (maximal ideal) trong K[X].

> **Mệnh đề 30.16.** đa thức $p \in$ K[X] là bất khả quy (irreducible) khi và chỉ khi $(p)$ là lý tưởng cực đại (maximal ideal) trong K[X].

<!-- PAGE 1085 -->

*Chứng minh.* Vì K[X] là miền nguyên (integral domain), với mọi khác không các đa thức $p, q \in$ K[X], deg(pq) $=$ deg(p) $+$ deg(q), và do đó, $(p) \neq$ K[X] khi và chỉ khi deg(p) $\ge 1$. Giả sử rằng $p \in$ K[X] là bất khả quy (irreducible). Vì mọi lý tưởng (ideal) trong K[X] là chính lý tưởng (ideal), mọi lý tưởng (ideal) trong K[X] là của tạo thành $(q)$, với một số $q \in$ K[X]. Nếu $(p) \subseteq (q)$, với deg(q) $\ge 1$, thì $q$ chia hết $p$, và vì $p \in$ K[X] là bất khả quy (irreducible), điều này suy ra rằng $p = \lambda q$ với một số $\lambda  \neq  0$ trong $K$, và do đó, $(p) = (q)$. Do đó, $(p)$ là lý tưởng cực đại (maximal ideal). Ngược lại, giả sử rằng $(p)$ là lý tưởng cực đại (maximal ideal). Thì, như ta đã chỉ ra ở trên, deg(p) $\ge 1$, và nếu $q$ chia hết $p$, với deg(q) $\ge 1$, thì $(p) \subseteq (q)$, và vì $(p)$ là lý tưởng cực đại (maximal ideal), điều này suy ra rằng $(p) = (q)$, mà có nghĩa là $p = \lambda q$ với một số $\lambda  \neq  0$ trong $K$, và do đó, $p$ là bất khả quy (irreducible). Cho $p \in$ K[X] là bất khả quy (irreducible). Thì, với mọi khác không đa thức $g \in$ K[X], hoặc $p$ và $g$ là một cách tương đối nguyên tố, hoặc $p$ chia hết $g$. Thật vậy, nếu $d$ là bất kỳ ước chung lớn nhất (gcd) của $p$ và $g$, nếu $d$ là hằng số, thì $p$ và $g$ là một cách tương đối nguyên tố, và nếu không, bởi vì $p$ là bất khả quy (irreducible), ta có $d = \lambda p$ với một số $\lambda  \neq  0$ trong $K$, và do đó, $p$ chia hết $g$. Hệ quả là, nếu $p, q \in$ K[X] là cả hai bất khả quy (irreducible), thì hoặc $p$ và $q$ là một cách tương đối nguyên tố, hoặc $p = \lambda q$ với một số $\lambda  \neq  0$ trong $K$. Đặc biệt, nếu $p, q \in$ K[X] là cả hai bất khả quy (irreducible) chuẩn hóa (monic) các đa thức và $p \neq  q$, thì $p$ và $q$ là một cách tương đối nguyên tố. Ta bây giờ chứng minh (duy nhất) nhân tử hóa của các đa thức vào bất khả quy (irreducible) các nhân tử.

> **Định lý 30.17.** Cho trước bất kỳ trường $K$, với mọi khác không đa thức
$$f = a_{d}X^{d}+ a_{d-1}X^{d-1}+ \cdots  + a_{0}$$
Của bậc $d =$ deg(f) $\ge 1$ trong K[X], tồn tại duy nhất một tập hợp ${\langle p_{1}, k_{1}\rangle , \dots  , \langle p_{m}, k_{m}\rangle$ } sao cho
$$f = a_{d}p_{1}^{k1} \cdots  p_{m}^{km} ,$$
Ở đâu $p_{i} \in$ K[X] là phân biệt bất khả quy (irreducible) chuẩn hóa (monic) các đa thức, $k_{i}$ là (không nhất thiết phân biệt) các số nguyên, và $m \ge 1, k_{i} \ge 1$.

*Chứng minh.* Thứ nhất, ta chứng minh sự tồn tại của như vậy nhân tử hóa bằng quy nạp theo $d =$ deg(f). Rõ ràng, nó là đủ để chứng minh kết quả cho chuẩn hóa (monic) các đa thức $f$ của bậc $d =$ deg(f) $\ge 1$. Nếu $d = 1$, thì $f = X + a_{0}$, mà là bất khả quy (irreducible) chuẩn hóa (monic) đa thức. Giả sử $d \ge 2$, và giả sử giả thiết quy nạp (induction hypothesis) với mọi chuẩn hóa (monic) các đa thức của bậc $< d$. Xét tập hợp $S$ của tất cả chuẩn hóa (monic) các đa thức $g$ sao cho deg(g) $\ge 1$ và $g$ chia hết $f$. Vì $f \in S$, tập hợp $S$ là khác rỗng, và do đó, $S$ chứa một số chuẩn hóa (monic) đa thức $p_{1}$ của tối tiểu bậc. Vì $deg(p_{1}) \ge 1$, chuẩn hóa (monic) đa thức $p_{1}$ phải là bất khả quy (irreducible). Ngược lại ta sẽ có $p_{1} = g_{1}g_{2}$, với một số chuẩn hóa (monic) các đa thức $g_{1}, g_{2}$ sao cho $deg(p_{1}) > deg(g_{1}) \ge 1$ và $deg(p_{1}) > deg(g_{2}) \ge 1$, và vì $p_{1}$ chia $f$, thì $g_{1}$ sẽ chia $f$, contradicting minimality của bậc của $p_{1}$. Do đó, ta có $f = p_{1}q$, với một số bất khả quy (irreducible) chuẩn hóa (monic) đa thức $p_{1}$, với $q$ cũng chuẩn hóa (monic). Vì $deg(p_{1}) \ge 1$, ta có deg(q) $<$ deg(f), và ta có thể áp dụng giả thiết quy nạp (induction hypothesis) đến $q$. Do đó, ta thu được nhân tử hóa của mong muốn tạo thành.

<!-- PAGE 1086 -->
Ta bây giờ chứng minh tính duy nhất. Giả sử rằng
$$f = a_{d}p_{1}^{k1} \cdots  p_{m}^{km} ,$$
Và
$$f = a_{d}q_{1}^{h1} \cdots  q_{n}^{hn} .$$
Do đó, ta có
$$a_{d}p_{1}^{k1} \cdots  p_{m}^{km} = a_{d}q_{1}^{h1} \cdots  q_{n}^{hn} .$$
Ta chứng minh rằng $m = n, p_{i} = q_{i}$ và $h_{i} = k_{i}$, với mọi $i$, với $1 \le i \le n$. chứng minh tiến hành bằng quy nạp theo $h_{1} + \cdots  + h_{n}$. Nếu $h_{1} + \cdots  + h_{n} = 1$, thì $n = 1$ và $h_{1} = 1$. Thì, vì K[X] là miền nguyên (integral domain), ta có
$$p_{1}^{k1} \cdots  p_{m}^{km} = q_{1},$$
Và vì $q_{1}$ và $p_{i}$ là bất khả quy (irreducible) chuẩn hóa (monic), ta phải có $m = 1$ và $p_{1} = q_{1}$. Nếu $h_{1} + \cdots  + h_{n} \ge 2$, vì K[X] là miền nguyên (integral domain) và vì $h_{1} \ge 1$, ta có
$$p_{1}^{k1} \cdots  p_{m}^{km} = q_{1}q,$$
Với
$$q = q_{1}^{h1-1}\cdots  q_{n}^{hn} ,$$
Ở đâu $(h_{1}$ - $1) + \cdots  + h_{n} \ge 1$ (và $q_{1}^{h1-1} = 1$ nếu $h_{1} = 1)$. Bây giờ, nếu $q_{1}$ là không bằng bất kỳ của $p_{i}$, bởi trước đó nhận xét, $q_{1}$ và $p_{i}$ là một cách tương đối nguyên tố, và theo Mệnh đề 30.14, $q_{1}$ và $p_{1}^{k1} \cdots  p_{m}^{km}$ là một cách tương đối nguyên tố. Nhưng điều này mâu thuẫn với sự kiện là $q_{1}$ chia hết $p_{1}^{k1} \cdots  p_{m}^{km}$. Do đó, $q_{1}$ bằng một của $p_{i}$. Không mất tính tổng quát (without loss of generality), ta có thể giả sử rằng $q_{1} = p_{1}$. Thì, vì K[X] là miền nguyên (integral domain), ta có
$$p_{1}^{k1-1}\cdots  p_{m}^{km} = q_{1}^{h1-1}\cdots  q_{n}^{hn} ,$$
Ở đâu $p_{1}^{k1-1} = 1$ nếu $k_{1} = 1$, và $q_{1}^{h1-1} = 1$ nếu $h_{1} = 1$. Bây giờ, $(h_{1}$ - $1) + \cdots  + h_{n} < h_{1} + \cdots  + h_{n}$, và ta có thể áp dụng giả thiết quy nạp (induction hypothesis) để kết luận rằng $m = n, p_{i} = q_{i}$ và $h_{i} = k_{i}$, với $1 \le i \le n$. ở trên considerations về duy nhất nhân tử hóa vào bất khả quy (irreducible) các nhân tử có thể được được mở rộng hầu như mà không có thay đổi đến nhiều hơn/thêm tổng quát các vành đã biết như Euclidean các miền. Trong như vậy các vành, một số abstract phiên bản của phép chia định lý được giả sử đến đúng.

> **Định nghĩa 30.10.** Euclidean miền xác định (hoặc Euclidean vành) là miền nguyên (integral domain) $A$ sao cho tồn tại một hàm $\phi$: $A \to \mathbb{N}$ với sau đây tính chất: Với mọi, $b \in A$ với $b \neq  0$, có một số $q, r \in A$ sao cho
$$a = bq + rand\phi (r) < \phi (b).$$

<!-- PAGE 1087 -->
Lưu ý rằng cặp $(q, r)$ là không nhất thiết duy nhất. Thực sự, duy nhất nhân tử hóa nghiệm đúng trong chính lý tưởng (ideal) các miền (PID’s), xem Định lý 32.12. Như được hiển thị dưới đây, mọi Euclidean miền xác định là PID, và do đó, duy nhất nhân tử hóa nghiệm đúng cho Euclidean các miền.

> **Mệnh đề 30.18.** Mọi Euclidean miền xác định $A$ là PID.

*Chứng minh.* Cho $\mathfrak{I}$ là khác không lý tưởng (ideal) trong $A$. Thì, tập hợp
$${\phi (a) | a \in \mathfrak{I}}$$
Là khác rỗng, và do đó, có nhỏ nhất phần tử $m$. Cho $b$ là bất kỳ (khác không) phần tử của $\mathfrak{I}$ sao cho $m = \phi (b)$. Ta khẳng định rằng $\mathfrak{I} = (b)$. Cho trước bất kỳ $a \in \mathfrak{I}$, ta có thể viết
$$a = bq + r$$
Với một số $q, r \in A$, với $\phi (r) < \phi (b)$. Vì $b \in \mathfrak{I}$ và $\mathfrak{I}$ là lý tưởng (ideal), ta cũng có bq $\in \mathfrak{I}$, và vì, bq $\in \mathfrak{I}$ và $\mathfrak{I}$ là lý tưởng (ideal), thì $r \in \mathfrak{I}$ với $\phi (r) < \phi (b) = m$, contradicting minimality của $m$. Do đó, $r = 0$ và $a \in (b)$. Nhưng khi đó,
$$\mathfrak{I} \subseteq (b),$$
Và vì $b \in \mathfrak{I}$, ta thu được
$$\mathfrak{I} = (b),$$
Và $A$ là PID. Như hệ quả của Mệnh đề 30.18, $ring\mathbb{Z}$ là Euclidean miền xác định (bằng cách sử dụng hàm $\phi (a) =$ ||) và do đó, PID. Nếu $K$ là trường, hàm $\phi$ trên K[X] được định nghĩa sao cho
$$0$$
$$if f = 0,$$
$$\phi (f) =$$
$$deg(f) + 1if f \neq  0,$$
Chỉ ra rằng K[X] là Euclidean miền xác định.

> **Ví dụ 30.3.** nhiều hơn/thêm thú vị ví dụ của Euclidean miền xác định là $ring\mathbb{Z}[i]$ của Gaussian các số nguyên, i.e., vành con của $\mathbb{C}$ bao gồm của tất cả phức các số của tạo thành $a +$ ib, ở đâu, $b \in \mathbb{Z}$. Bằng cách sử dụng hàm $\phi$ được định nghĩa sao cho
$$\phi (a + ib) = a^{2}+ b^{2},$$
Ta để lại nó như thú vị bài tập để chứng minh rằng $\mathbb{Z}[i]$ là Euclidean miền xác định.  Không mọi PID là Euclidean vành.
