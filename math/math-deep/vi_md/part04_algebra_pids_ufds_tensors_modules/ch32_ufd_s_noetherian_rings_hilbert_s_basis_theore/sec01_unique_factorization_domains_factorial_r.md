# Duy nhất Nhân tử hóa Các miền (Giai thừa Các vành)


<!-- PAGE 1133 -->
Chương $32$ UFD’s, Các vành Noether, Hilbert’s Cơ sở (basis) Định lý

## 32.1 Duy nhất Nhân tử hóa Các miền (Giai thừa Các vành)

Ta đã thấy trong Mục 30.5 rằng nếu $K$ là trường, thì mọi khác không đa thức trong K[X] có thể được được nhân tử như tích của bất khả quy (irreducible) các nhân tử, và rằng như vậy nhân tử hóa là về cơ bản duy nhất. cùng tính chất nghiệm đúng cho vành $K[X_{1}, \dots  , X_{n}]$ ở đâu $n \ge 2$, nhưng khác nhau chứng minh là cần thiết. lý do tại sao duy nhất nhân tử hóa nghiệm đúng cho $K[X_{1}, \dots  , X_{n}]$ là rằng nếu $A$ là miền nguyên (integral domain) cho mà duy nhất nhân tử hóa nghiệm đúng trong một số phù hợp nghĩa, thì tính chất của duy nhất nhân tử hóa lifts đến đa thức vành [X]. Như vậy các vành được gọi là giai thừa các vành, hoặc duy nhất nhân tử hóa các miền. bước thứ nhất nếu để định nghĩa khái niệm của bất khả quy (irreducible) phần tử trong miền nguyên (integral domain), và thì để định nghĩa giai thừa vành. Nếu sẽ turn ra rằng trong giai thừa vành, bất kỳ khác không phần tử là bất khả quy (irreducible) (hoặc nguyên tố) khi và chỉ khi chính lý tưởng (ideal) () là lý tưởng nguyên tố (prime ideal). Nhắc lại rằng cho trước vành $A$, unit là bất kỳ khả nghịch phần tử (w.r.t. phép nhân). tập hợp của units của $A$ được ký hiệu bởi $A^{*}$. Nó là multiplicative nhóm con của $A$, với đồng nhất thức $1$. Cũng, cho trước, $b \in A$, nhắc lại rằng chia hết $b$ nếu $b =$ ac với một số $c \in A$; tương đương, chia hết $b$ khi và chỉ khi
$(b) \subseteq$ (). Bất kỳ khác không $a \in A$ là chia hết bởi bất kỳ unit $u$, vì $a = u(u^{-1}a)$. quan hệ “ chia hết b,” thường được ký hiệu bởi | $b$, là reflexive và transitive, và do đó, preorder trên $A-{0}$.

> **Định nghĩa 32.1.** Cho $A$ là miền nguyên (integral domain). Một số phần tử $a \in A$ là bất khả quy (irreducible) nếu $a \neq  0, a \in / A^{*}$ (là không unit), và bất cứ khi nào $a =$ bc, thì hoặc $b$ hoặc $c$ là unit (ở đâu $b, c \in A)$. Tương đương, $a \in A$ là khả quy nếu $a = 0$, hoặc $a \in A^{*}$ (là unit), hoặc $a =$ bc ở đâu $b, c \in / A^{*}$ (, $b$ là cả hai noninvertible) và $b, c \neq  0$. Nhận thấy rằng nếu $a \in A$ là bất khả quy (irreducible) và $u \in A$ là unit, thì ua là cũng bất khả quy (irreducible). một cách tổng quát, nếu $a \in A, a \neq  0$, và $u$ là unit, thì và ua được nói là liên kết. Điều này là quan hệ tương đương (equivalence relation) trên khác không các phần tử của $A$ được cảm sinh bởi divisibility preorder.
$$1133$$

<!-- PAGE 1134 -->
Sau đây đơn giản mệnh đề cho đủ điều kiện cho phần tử $a \in A$ là bất khả quy (irreducible).

> **Mệnh đề 32.1.** Cho $A$ là miền nguyên (integral domain). Với mọi $a \in A$ với $a \neq  0$, nếu chính lý tưởng (ideal) () là lý tưởng nguyên tố (prime ideal), thì là bất khả quy (irreducible).

*Chứng minh.* Nếu () là nguyên tố, thì $(a) \neq  A$ và là không unit. Giả sử rằng $a =$ bc. Thì, bc $\in$ (), và vì () là nguyên tố, hoặc $b \in$ () hoặc $c \in$ (). Xét trường hợp ở đâu $b \in$ (), khác trường hợp đang là đồng dạng. Thì, $b =$ ax với một số $x \in A$. Hệ quả là,
$$a = bc = axc,$$
Và vì $A$ là miền nguyên (integral domain) và $a \neq  0$, ta thu được
$$1 = xc,$$
Mà chứng tỏ rằng $c = x^{-1}$ là unit. Nó nên được lưu ý rằng điều ngược lại của Mệnh đề 32.1 là một cách tổng quát sai. Tuy nhiên, nó nghiệm đúng cho giai thừa các vành, được định nghĩa tiếp theo.

> **Định nghĩa 32.2.** giai thừa vành hoặc miền nhân tử hóa duy nhất (UFD) (UFD) (hoặc duy nhất nhân tử hóa vành) là miền nguyên (integral domain) $A$ sao cho sau đây hai các tính chất đúng:
$(1)$ Với mọi khác không $a \in A$, nếu $a \in / A^{*}$ (là không unit), thì có thể được được nhân tử như tích
$$a = a_{1} \cdots  a_{m}$$
Ở đâu mỗi $a_{i} \in A$ là bất khả quy (irreducible) $(m \ge 1)$.
$(2)$ Với mọi khác không $a \in A$, nếu $a \in / A^{*}$ (là không unit) và nếu
$$a = a_{1} \cdots  a_{m} = b_{1} \cdots  b_{n}$$
Ở đâu $a_{i} \in A$ và $b_{j} \in A$ là bất khả quy (irreducible), thì $m = n$ và có một hoán vị $\sigma$ của ${1, \dots  , m}$ và một số units $u_{1}, \dots  , u_{m} \in A^{*}$ sao cho $a_{i} = u_{i}b_{\sigma(i)}$ với mọi $i, 1 \le i \le m$.

> **Ví dụ 32.1.** vành $\mathbb{Z}$ của các số nguyên nếu typical ví dụ của UFD. Cho trước trường $K$, đa thức vành K[X] là UFD. Tổng quát hơn, ta sẽ chỉ ra sau này rằng mọi PID là UFD (xem Định lý 32.12). Do đó, đặc biệt, $\mathbb{Z}[X]$ là UFD. Tuy nhiên, ta để lại như một bài tập
$$\mathbb{Z}$$
Để chứng minh rằng lý tưởng (ideal) (2X, $X^{2})$ được sinh bởi 2X và $X^{2}$ là không chính, và do đó, $[X]$ là không PID. Thứ nhất, ta chứng minh rằng điều kiện $(2)$ trong Định nghĩa 32.2 là tương đương đến thông thường “Euclidean” điều kiện.

<!-- PAGE 1135 -->
$$\sqrt$$
Có tích phân các miền rằng là không UFD’s. Ví dụ, vành con $\mathbb{Z}[ \overline{-}\overline{5]}$ của $\mathbb{C}$  $\sqrt$ bao gồm của phức các số của tạo thành $a +$ bi $\overline{5}$ ở đâu, $b \in \mathbb{Z}$ là không UFD. Thật vậy, ta có
$$\sqrt\sqrt$$
$$9 = 3 \cdot  3 = (2 + i\overline{5)(2} -i\overline{5)},$$
$$\sqrt\sqrt$$
Và nó có thể được được hiển thị rằng $3, 2 + i \overline{5,}$ và $2 -i \overline{5$ là $irreducible,}$ và rằng units là $\pm 1$.
$$\sqrt$$
Tính duy nhất điều kiện $(2)$ không thỏa mãn và $\mathbb{Z}[ \overline{-}\overline{5]}$ là không UFD.
$$\sqrt$$
Nhận xét: Cho $d \in \mathbb{Z}$ với $d < 0$, nó là đã biết rằng vành của các số nguyên $of\mathbb{Q}( \overline{d})$ là UFD khi và chỉ khi $d$ là một của chín các nguyên tố, $d = -1, -2, -3, -7$, -11, -19, -43, -67 và -163. Điều này là khó định lý rằng đã là conjectured bởi Gauss nhưng không được chứng minh cho đến khi $1966$, một cách độc lập bởi Stark và Baker. Heegner đã có published chứng minh của kết quả này trong $1952$ nhưng ở đó đã là một số doubt về của nó validity. Sau việc tìm his chứng minh, Stark reexamined Heegner’s chứng minh và concluded rằng nó đã là về cơ bản đúng sau tất cả. Trong sharp contrast, $d$ là dương số nguyên,
$$problem of determining which of the rings of integers of \mathbb{Q}(\sqrt \frac{when}{d} ) are UFD’s, is still open. It$$
$$\sqrt$$
Có thể cũng được hiển thị rằng $d < 0$, thì vành $\mathbb{Z}[ \overline{d}]$ là UFD khi và chỉ khi $d = -1$ hoặc $d = -2$. Nếu
$$d \equiv 1 (\mathrm{mod} 4), then \mathbb{Z}[\sqrt \frac{if}{d]} is never a UFD. For more details about these remarkable results,$$
Xem Stark $[170]$ (Chương $8)$.

> **Mệnh đề 32.2.** Cho $A$ là miền nguyên (integral domain) thỏa mãn điều kiện $(1)$ trong Định nghĩa 32.2. Thì, điều kiện $(2)$ trong Định nghĩa 32.2 là tương đương đến sau đây điều kiện: (2') Nếu $a \in A$ là bất khả quy (irreducible) và chia hết tích bc, ở đâu $b, c \in A$ và $b, c \neq  0$, thì hoặc chia hết $b$ hoặc chia hết $c$.

*Chứng minh.* Thứ nhất, giả sử rằng $(2)$ nghiệm đúng. Cho bc $=$ ad, ở đâu $d \in A, d \neq  0$. Nếu $b$ là unit, thì
$$c = adb^{-1},$$
Và $c$ là chia hết bởi. đồng dạng lập luận áp dụng đến $c$. Do đó, ta có thể giả sử rằng $b$ và $c$ là không units. Xét theo $(1)$, ta có thể viết
$$b = p_{1} \cdots  p_{m}andc = p_{m+1} \cdots  q_{m+n},$$
Ở đâu $p_{i} \in A$ là bất khả quy (irreducible). Vì bc $=$ ad, là bất khả quy (irreducible), và $b, c$ là không units, $d$ không thể là unit. Xét theo $(1)$, ta có thể viết
$$d = q_{1} \cdots  q_{r},$$
Ở đâu $q_{i} \in A$ là bất khả quy (irreducible). Do đó,
$$p_{1} \cdots  p_{m}p_{m+1} \cdots  p_{m+n} = aq_{1} \cdots  q_{r},$$
Ở đâu tất cả các nhân tử liên quan là bất khả quy (irreducible). Bởi $(2)$, ta phải có
$$a = u_{i0}p_{i0}$$

<!-- PAGE 1136 -->
Với một số unit $u_{i0} \in A$ và một số chỉ số $i_{0}, 1 \le i_{0} \le m + n$. Hệ quả là, nếu $1 \le i_{0} \le m$, thì chia hết $b$, và nếu $m + 1 \le i_{0} \le m + n$, thì chia hết $c$. Điều này chứng tỏ rằng (2') nghiệm đúng. Bây giờ ta giả sử rằng (2') nghiệm đúng. Giả sử rằng
$$a = a_{1} \cdots  a_{m} = b_{1} \cdots  b_{n},$$
Ở đâu $a_{i} \in A$ và $b_{j} \in A$ là bất khả quy (irreducible). Không mất tính tổng quát (without loss of generality), ta có thể giả sử rằng $m \le n$. Ta tiến hành bằng quy nạp theo $m$. Nếu $m = 1$,
$$a_{1} = b_{1} \cdots  b_{n},$$
Và vì $a_{1}$ là bất khả quy (irreducible), $u = b_{1} \cdots  b_{i-1}b_{i+1}b_{n}$ phải là unit với một số $i, 1 \le i \le n$. Do đó,
$(2)$ nghiệm đúng với $n = 1$ và $a_{1} = b_{i}u$. Giả sử rằng $m > 1$ và rằng giả thiết quy nạp (induction hypothesis) nghiệm đúng cho $m$ - $1$. Vì
$$a_{1}a_{2} \cdots  a_{m} = b_{1} \cdots  b_{n},$$
$a_{1}$ chia hết $b_{1} \cdots  b_{n}$, và xét theo (2'), $a_{1}$ chia hết một số $b_{j}$. Vì $a_{1}$ và $b_{j}$ là bất khả quy (irreducible), ta phải có $b_{j} = u_{j}a_{1}$, ở đâu $u_{j} \in A$ là unit. Vì $A$ là miền nguyên (integral domain),
$$a_{1}a_{2} \cdots  a_{m} = b_{1} \cdots  b_{j-1}u_{j}a_{1}b_{j+1} \cdots  b_{n}$$
Suy ra rằng
$$a_{2} \cdots  a_{m} = (u_{j}b_{1}) \cdots  b_{j-1}b_{j+1} \cdots  b_{n},$$
Và theo giả thiết quy nạp, $m$ - $1 = n$ - $1$ và $a_{i} = v_{i}b_{\tau(i)}$ với một số units $v_{i} \in A$ và một số song ánh $\tau$ giữa ${2, \dots  , m}$ và ${1, \dots  , j -1, j + 1, \dots  , m}$. Tuy nhiên, song ánh $\tau$ mở rộng đến hoán vị $\sigma$ của ${1, \dots  , m}$ bởi đặt $\sigma (1) = j$, và kết quả nghiệm đúng bởi đặt $v_{1} = u_{j}^{-1}$. Như hệ quả của Mệnh đề 32.2. ta thu được điều ngược lại của Mệnh đề 32.1.

> **Mệnh đề 32.3.** Cho $A$ là giai thừa vành. Với mọi $a \in A$ với $a \neq  0$, chính lý tưởng (ideal)
() là lý tưởng nguyên tố (prime ideal) khi và chỉ khi là bất khả quy (irreducible).

*Chứng minh.* Xét theo Mệnh đề 32.1, ta chỉ có để chứng minh rằng nếu $a \in A$ là bất khả quy (irreducible), thì chính lý tưởng (ideal) () là lý tưởng nguyên tố (prime ideal). Thật vậy, nếu bc $\in$ (), thì chia hết bc, và theo Mệnh đề 32.2, tính chất (2') suy ra rằng hoặc chia hết $b$ hoặc chia hết $c$, nghĩa là, hoặc $b \in$ () hoặc $c \in$ (), mà có nghĩa là () là nguyên tố. Bởi vì Mệnh đề 32.3 nghiệm đúng, trong UFD, bất khả quy (irreducible) phần tử là thường được gọi là nguyên tố. Trong UFD $A$, mọi khác không phần tử $a \in A$ rằng là không unit có thể được biểu diễn dưới dạng tích $a = a_{1} \cdots  a_{n}$ của bất khả quy (irreducible) các phần tử $a_{i}$, và bởi tính chất $(2)$, số $n$ của các nhân tử chỉ phụ thuộc vào, nghĩa là, nó là cùng với mọi các nhân tử hóa vào bất khả quy (irreducible) các nhân tử. Ta agree rằng điều này số là $0$ cho unit.
Nhận xét: Nếu $A$ là UFD, ta có thể phát biểu nhân tử hóa các tính chất sao cho chúng cũng áp dụng đến units:

<!-- PAGE 1137 -->
$(1)$ Với mọi khác không $a \in A$, có thể được được nhân tử như tích
$$a = ua_{1} \cdots  a_{m}$$
Ở đâu $u \in A^{*} (u$ là unit) và mỗi $a_{i} \in A$ là bất khả quy (irreducible) $(m \ge 0)$.
$(2)$ Với mọi khác không $a \in A$, nếu
$$a = ua_{1} \cdots  a_{m} = vb_{1} \cdots  b_{n}$$
Ở đâu $u, v \in A^{*} (u, v$ là units) và $a_{i} \in A$ và $b_{j} \in A$ là bất khả quy (irreducible), thì $m = n$, và nếu $m = n = 0$ thì $u = v$, khác nếu $m \ge 1$, thì có một hoán vị $\sigma$ của ${1, \dots  , m}$ và một số units $u_{1}, \dots  , u_{m} \in A^{*}$ sao cho $a_{i} = u_{i}b_{\sigma(i)}$ với mọi $i, 1 \le i \le m$. Ta là bây giờ ready để chứng minh rằng nếu $A$ là UFD, thì đa thức vành [X] là cũng UFD. Thứ nhất, nhận thấy rằng units của [X] là chỉ units của $A$. sự kiện rằng khác không và nonunit các đa thức trong [X] nhân tử như các tích của bất khả quy (irreducible) các đa thức là dễ hơn để chứng minh hơn tính duy nhất. Ta sẽ chỉ ra trong chứng minh của Định lý 32.10 rằng ta có thể tiến hành bằng quy nạp theo các cặp $(m, n)$ ở đâu $m$ là bậc của f(X) và $n$ là hoặc $0$ nếu hệ số $f_{m}$ của $X^{m}$ trong f(X) là unit của $n$ là $f_{m}$ là tích của $n$ bất khả quy (irreducible) các phần tử. Cho tính duy nhất của nhân tử hóa, theo Mệnh đề 32.2, nó là đủ để chứng minh rằng điều kiện (2') nghiệm đúng. Điều này là little nhiều hơn/thêm khó/tinh tế. Có một vài các chứng minh, nhưng chúng tất cả liên quan đến pretty Bổ đề do Gauss. Thứ nhất, lưu ý sau đây tầm thường sự kiện. Cho trước vành $A$, với mọi $a \in A, a \neq  0$, nếu chia hết mọi hệ số của một số khác không đa thức f(X) $\in$ [X], thì chia hết f(X). Nếu $A$ là miền nguyên (integral domain), ta thu được sau đây điều ngược lại.

> **Mệnh đề 32.4.** Cho $A$ là miền nguyên (integral domain). Với mọi $a \in A$, ̸ $= 0$, nếu chia hết khác không đa thức f(X) $\in$ [X], thì chia hết mọi hệ số của f(X).

*Chứng minh.* Giả sử rằng f(X) $=$ ag(X), với một số g(X) $\in$ [X]. Vì ̸ $= 0$ và $A$ là tích phân vành, f(X) và g(X) có cùng bậc $m$, và vì với mọi $i (0 \le i \le m)$ hệ số của $X^{i}$ trong f(X) bằng hệ số của $X^{i}$ trong ag(x), ta có $f_{i} = ag_{i}$, và bất cứ khi nào $f_{i} \neq  0$, ta xem rằng chia hết $f_{i}$.

> **Bổ đề 32.5.** (Gauss’s bổ đề) Cho $A$ là UFD. Với mọi $a \in A$, nếu là bất khả quy (irreducible) và chia hết tích f(X)g(X) của hai các đa thức f(X), g(X) $\in$ [X], thì hoặc chia hết f(X) hoặc chia hết g(X).

*Chứng minh.* Cho f(X) $= f_{m}X^{m} + \cdots  + f_{i}X^{i} + \cdots  + f_{0}$ và g(X) $= g_{n}X^{n} + \cdots  + g_{j}X^{j} + \cdots  + g_{0}$. Giả sử rằng chia hết không f(X) cũng không g(X). Bởi (dễ) điều ngược lại của Mệnh đề 32.4, tồn tại một $i (0 \le i \le m)$ sao cho thực hiện không chia $f_{i}$, và tồn tại một $j (0 \le j \le n)$

<!-- PAGE 1138 -->
Sao cho thực hiện không chia $g_{j}$. Chọn $i$ và $j$ tối tiểu sao cho thực hiện không chia $f_{i}$ và thực hiện không chia $g_{j}$. hệ số $c_{i+j}$ của $X^{i+j}$ trong f(X)g(X) là
$$c_{i+j} = f_{0}g_{i+j} + f_{1}g_{i+j-1} + \cdots  + f_{i}g_{j} + \cdots  + f_{i+j}g_{0}$$
(đặt $f_{h} = 0$ nếu $h > m$ và $g_{k} = 0$ nếu $k > n)$. Từ lựa chọn của $i$ và $j$, không thể chia $f_{i}g_{j}$, vì đang là bất khả quy (irreducible), bởi (2') của Mệnh đề 32.2, sẽ chia $f_{i}$ hoặc $g_{j}$. Tuy nhiên, bởi lựa chọn của $i$ và $j$, chia hết mọi khác khác không số hạng trong tổng cho $c_{i+j}$, và vì là bất khả quy (irreducible) và chia hết f(X)g(X), theo Mệnh đề 32.4, chia hết $c_{i+j}$, mà suy ra rằng chia hết $f_{i}g_{j}$, một mâu thuẫn. Do đó, hoặc chia hết f(X) hoặc chia hết g(X). Như hệ quả, ta thu được sau đây mệnh đề.

> **Mệnh đề 32.6.** Cho $A$ là UFD. Với mọi $a \in A$, ̸ $= 0$, nếu chia hết tích f(X)g(X) của hai các đa thức f(X), g(X) $\in$ [X] và f(X) là bất khả quy (irreducible) và của bậc ít nhất $1$, thì chia hết g(X).

*Chứng minh.* Mệnh đề là tầm thường là là unit. Ngược lại, $a = a_{1} \cdots  a_{m}$ ở đâu $a_{i} \in A$ là bất khả quy (irreducible). Bằng cách sử dụng quy nạp và áp dụng Bổ đề 32.5, ta kết luận rằng chia hết g(X). Ta bây giờ chỉ ra rằng Bổ đề 32.5 cũng áp dụng đến trường hợp ở đâu là bất khả quy (irreducible) đa thức. Điều này đòi hỏi little excursion liên quan đến phân số trường $F$ của $A$.
Nhận xét: Nếu $A$ là UFD, nó là khả dĩ/có thể để chứng minh tính duy nhất điều kiện $(2)$ cho [X] một cách trực tiếp mà không có bằng cách sử dụng phân số trường của $A$, xem Malliavin $[123]$, Chương $3$. Cho trước miền nguyên (integral domain) $A$, ta có thể xây dựng trường $F$ sao cho mọi phần tử của $F$ là của tạo thành $a/b$, ở đâu, $b \in A, b \neq  0$, bằng cách sử dụng về cơ bản phương pháp cho xây dựng trường $\mathbb{Q}$ của hữu tỷ các số từ vành $\mathbb{Z}$ của các số nguyên.

> **Mệnh đề 32.7.** Cho $A$ là miền nguyên (integral domain).
$(1)$ Có một trường $F$ và đơn ánh (injective) vành đồng cấu $i: A \to F$ sao cho mọi phần tử của $F$ là của tạo thành $i(a)i(b)^{-1}$, ở đâu, $b \in A, b \neq  0$.
$(2)$ Với mọi trường $K$ và mọi đơn ánh (injective) vành đồng cấu $h: A \to K$, có một
(duy nhất) trường đồng cấu $h: F \to K$ sao cho
$$b$$
$$h(i(a)i(b)^{-1}) = h(a)h(b)^{-1}$$
$$b$$
Với mọi, $b \in A, b \neq  0$.
$(3)$ trường $F$ trong $(1)$ là duy nhất sai khác một đẳng cấu (up to isomorphism).

<!-- PAGE 1139 -->

*Chứng minh.* $(1)$ Xét nhị phân quan hệ $\simeq$ trên $A \times  (A -{0})$ được định nghĩa như sau:
$$(a, b) \simeq (a', b')iff ab'= a'b.$$
Nó là dễ dàng được thấy rằng $\simeq$ là quan hệ tương đương (equivalence relation). Lưu ý rằng sự kiện rằng $A$ là miền nguyên (integral domain) được sử dụng để chứng minh transitivity. lớp tương đương (equivalence class) của (, $b)$ được ký hiệu bởi $a/b$. Rõ ràng, $(0, b) \simeq (0, 1)$ với mọi $b \in A$, và ta ký hiệu lớp của $(0, 1)$ cũng bởi $0$. lớp tương đương (equivalence class) $a/1$ của (, $1)$ cũng được ký hiệu bởi. Ta định nghĩa phép cộng và phép nhân trên $A \times  (A -{0})$ như sau:
$$(a, b) + (a', b') = (ab'+ a'b, bb'),$$
$$(a, b) \cdot  (a', b') = (aa', bb').$$
Dễ dàng kiểm chứng được rằng $\simeq$ là congruential w.r.t. $+$ và $\cdot$, mà có nghĩa là $+$ và $\cdot$ là xác định tốt (well-defined) trên các lớp tương đương modulo $\simeq$. Khi, $b \neq  0$, nghịch đảo của $a/b$ là $b/a$, và dễ dàng kiểm chứng được rằng $F$ là trường. ánh xạ $i: A \to F$ được định nghĩa sao cho i() $= a/1$ là đơn ánh của $A$ vào $F$ và rõ ràng
$$\frac{a}{b} = i(a)i(b)^{-1}.$$
$(2)$ Cho trước đơn ánh (injective) vành đồng cấu $h: A \to K$ vào trường $K$,
$$\frac{a}{b} = \frac{a'}{b'} iff ab' = a'b,$$
Mà suy ra rằng
$$h(a)h(b') = h(a')h(b),$$
Và vì $h$ là đơn ánh (injective) và $b$, b' $\neq  0$, ta thu được
$$h(a)h(b)^{-1}= h(a')h(b')^{-1}.$$
Do đó, có một ánh xạ $h: F \to K$ sao cho
$$b$$
$$h(a/b) =h(i(a)i(b)^{-1}) = h(a)h(b)^{-1}$$
$$b b$$
Với mọi, $b \in A, b \neq  0$, và nó là dễ dàng đã kiểm tra rằng $h$ là trường đồng cấu. ánh xạ $h$
$$b b$$
Là rõ ràng duy nhất.
$(3)$ tính duy nhất của $F$ sai khác một đẳng cấu (up to isomorphism) suy ra từ $(2)$, và là để lại như một bài tập. trường $F$ cho trước theo Mệnh đề 32.7 được gọi là phân số trường của $A$, và nó được ký hiệu bởi Frac(). Đặc biệt, cho trước miền nguyên (integral domain) $A$, vì $A[X_{1}, \dots  , X_{n}]$ là cũng miền nguyên (integral domain), ta có thể tạo thành phân số trường của đa thức vành $A[X_{1}, \dots  , X_{n}]$, được ký hiệu bởi $F(X_{1}, \dots  , X_{n})$, ở đâu $F =$ Frac() là phân số trường của $A$. Nó cũng được gọi là trường

<!-- PAGE 1140 -->
Của hữu tỷ các hàm trên $F$, mặc dù thuật ngữ là bit misleading, vì các phần tử của $F(X_{1}, \dots  , X_{n})$ chỉ định nghĩa các hàm khi dominator là khác không. Ta bây giờ có sau đây then chốt bổ đề mà chỉ ra rằng nếu đa thức f(X) là khả quy trên F[X] ở đâu $F$ là phân số trường của $A$, thì f(X) là đã khả quy trên [X].

> **Bổ đề 32.8.** Cho $A$ là UFD và cho $F$ là phân số trường của $A$. Với mọi khác không đa thức f(X) $\in$ [X] của bậc $m$, nếu f(X) là không tích của hai các đa thức của bậc chặt nhỏ hơn hơn $m$, thì f(X) là bất khả quy (irreducible) trong F[X].

*Chứng minh.* Giả sử rằng f(X) là khả quy trong F[X] và rằng f(X) là không null cũng không unit. Thì,
$$f(X) = G(X)H(X),$$
Ở đâu G(X), H(X) $\in$ F[X] là các đa thức của bậc $p, q \ge 1$. Cho là tích của denominators của các hệ số của G(X), và $b$ tích của denominators của các hệ số của H(X). Thì,, b̸ $= 0, g_{1}(X) =$ aG(X) $\in$ [X] có bậc $p \ge 1, h_{1}(X) =$ bH(X) $\in$ [X] có bậc $q \ge 1$, và
$$abf(X) = g_{1}(X)h_{1}(X).$$
Cho $c =$ ab. Nếu $c$ là unit, thì f(X) là cũng khả quy trong [X]. Ngược lại, $c = c_{1} \cdots  c_{n}$, ở đâu $c_{i} \in A$ là bất khả quy (irreducible). Ta bây giờ sử dụng quy nạp trên $n$ để chứng minh rằng
$$f(X) = g(X)h(X),$$
Với một số các đa thức g(X) $\in$ [X] của bậc $p \ge 1$ và h(X) $\in$ [X] của bậc $q \ge 1$. Nếu $n = 1$, vì $c = c_{1}$ là bất khả quy (irreducible), theo Bổ đề 32.5, hoặc $c$ chia hết $g_{1}(X)$ hoặc $c$ chia hết $h_{1}(X)$. Nói rằng $c$ chia hết $g_{1}(X)$, khác trường hợp đang là đồng dạng. Thì, $g_{1}(X) =$ cg(X) với một số g(X) $\in$ [X] của bậc $p \ge 1$, và vì [X] là tích phân vành, ta thu được
$$f(X) = g(X)h_{1}(X),$$
Chỉ ra rằng f(X) là khả quy trong [X]. Nếu $n > 1$, vì
$$c_{1} \cdots  c_{n}f(X) = g_{1}(X)h_{1}(X),$$
$c_{1}$ chia hết $g_{1}(X)h_{1}(X)$, và như ở trên, hoặc $c_{1}$ chia hết $g_{1}(X)$ hoặc $c$ chia hết $h_{1}(X)$. Trong hoặc trường hợp, ta thu được
$$c_{2} \cdots  c_{n}f(X) = g_{2}(X)h_{2}(X)$$
Với một số các đa thức $g_{2}(X) \in$ [X] của bậc $p \ge 1$ và $h_{2}(X) \in$ [X] của bậc $q \ge 1$. Theo giả thiết quy nạp, ta thu được
$$f(X) = g(X)h(X),$$
Với một số các đa thức g(X) $\in$ [X] của bậc $p \ge 1$ và h(X) $\in$ [X] của bậc $q \ge 1$, chỉ ra rằng f(X) là khả quy trong [X].

<!-- PAGE 1141 -->
Cuối cùng, ta có thể chứng minh rằng (2') nghiệm đúng.

> **Bổ đề 32.9.** Cho $A$ là UFD. Cho trước bất kỳ ba khác không các đa thức f(X), g(X), h(X) $\in$ [X], nếu f(X) là bất khả quy (irreducible) và f(X) chia hết tích g(X)h(X), thì hoặc f(X) chia hết g(X) hoặc f(X) chia hết h(X).

*Chứng minh.* Nếu f(X) có bậc $0$, thì kết quả suy ra từ Bổ đề 32.5. Do đó, ta có thể giả sử rằng bậc của f(X) là $m \ge 1$. Cho $F$ là phân số trường của $A$. Theo Bổ đề 32.8, f(X) là cũng bất khả quy (irreducible) trong F[X]. Vì F[X] là UFD (theo Định lý 30.17), hoặc f(X) chia hết g(X) hoặc f(X) chia hết h(X), trong F[X]. Giả sử rằng f(X) chia hết g(X), khác trường hợp đang là đồng dạng. Thì,
$$g(X) = f(X)G(X),$$
Với một số G(X) $\in$ F[X]. Nếu là tích denominators của các hệ số của $G$, ta có
$$ag(X) = q_{1}(X)f(X),$$
Ở đâu $q_{1}(X) =$ aG(X) $\in$ [X]. Nếu là unit, ta xem rằng f(X) chia hết g(X). Ngược lại, $a = a_{1} \cdots  a_{n}$, ở đâu $a_{i} \in A$ là bất khả quy (irreducible). Ta chứng minh bằng quy nạp theo $n$ rằng
$$g(X) = q(X)f(X)$$
Với một số q(X) $\in$ [X]. Nếu $n = 1$, vì f(X) là bất khả quy (irreducible) và của bậc $m \ge 1$ và
$$a_{1}g(X) = q_{1}(X)f(X),$$
Theo Bổ đề 32.5, $a_{1}$ chia hết $q_{1}(X)$. Do đó, $q_{1}(X) = a_{1}q(X)$ ở đâu q(X) $\in$ [X]. Vì [X] là miền nguyên (integral domain), ta thu được
$$g(X) = q(X)f(X),$$
Và f(X) chia hết g(X). Nếu $n > 1$, từ
$$a_{1} \cdots  a_{n}g(X) = q_{1}(X)f(X),$$
Ta lưu ý rằng $a_{1}$ chia hết $q_{1}(X)f(X)$, và như trong trước đó trường hợp, $a_{1}$ chia hết $q_{1}(X)$. Do đó, $q_{1}(X) = a_{1}q_{2}(X)$ ở đâu $q_{2}(X) \in$ [X], và ta thu được
$$a_{2} \cdots  a_{n}g(X) = q_{2}(X)f(X).$$
Theo giả thiết quy nạp, ta thu được
$$g(X) = q(X)f(X)$$
Với một số q(X) $\in$ [X], và f(X) chia hết g(X). Ta cuối cùng thu được sự kiện rằng [X] là UFD khi $A$ là.

<!-- PAGE 1142 -->

> **Định lý 32.10.** Nếu $A$ là UFD thì đa thức vành [X] là cũng UFD.

*Chứng minh.* Như ta được nói trước đó, nhân tử hóa tính chất $(1)$ là dễ hơn để chứng minh hơn tính duy nhất. Giả sử rằng f(X) có bậc $m$ và cho $f_{m}$ là hệ số của $X^{m}$ trong f(X). Hoặc $f_{m}$ là unit hoặc nó là tích của $n \ge 1$ bất khả quy (irreducible) các phần tử. Nếu $f_{m}$ là unit ta tập hợp $n = 0$. Ta tiến hành bằng quy nạp theo cặp $(m, n)$, bằng cách sử dụng well-founded thứ tự trên các cặp, i.e.,
$$(m, n) \le (m', n')$$
Khi và chỉ khi hoặc $m <$ m', hoặc $m =$ m' và $n <$ n'. Nếu f(X) là khác không đa thức của bậc $0$ mà là không unit, thì f(X) $\in A$, và f(X) $= f_{m} = a_{1} \cdots  a_{n}$ với một số bất khả quy (irreducible) $a_{i} \in A$, vì $A$ là UFD. Điều này chứng minh base trường hợp. Nếu f(X) có bậc $m > 0$ và f(X) là khả quy, thì
$$f(X) = g(X)h(X),$$
Ở đâu g(X) và h(X) có bậc $p, q \le m$ và là không units. Có hai các trường hợp.
$(1) f_{m}$ là unit (do đó $n = 0)$. Nếu do đó, vì $f_{m} = g_{p}h_{q}$ (ở đâu $g_{p}$ là hệ số của $X^{p}$ trong g(X) và $h_{q}$ là hệ số của $X^{q}$ trong h(X)), thì $g_{p}$ và $h_{q}$ là cả hai units. Ta khẳng định rằng $p, q \ge 1$. Ngược lại, $p = 0$ hoặc $q = 0$, nhưng khi đó hoặc g(X) $= g_{0}$ là unit hoặc h(X) $= h_{0}$ là unit, một mâu thuẫn. Bây giờ, vì $m = p + q$ và $p, q \ge 1$, ta có $p, q < m$ do đó $(p, 0) < (m, 0)$ và $(q, 0) < (m, 0)$, và theo giả thiết quy nạp, cả hai g(X) và h(X) có thể được viết dưới dạng các tích của bất khả quy (irreducible) các nhân tử, do đó do đó có thể f(X).
$(2) f_{m}$ là không unit, nói $f_{m} = a_{1} \cdots  a_{n}$ ở đâu $a_{1}, \dots  , a_{n}$ là bất khả quy (irreducible) và $n \ge 1$.
$$(a) If p, q < m, then (p, n_{1}) < (m, n) and (q, n_{2}) < (m, n) where n_{1} is the number of$$
$$irreducible factors of g_{p} or n_{1} = 0 if g_{p} is irreducible, and similarly n_{2} is the number$$
$$of irreducible factors of h_{p} or n_{2} = 0 if h_{p} is irreducible (note that n_{1}, n_{2} \le n and$$
$$it is possible that n_{1} = n if h_{q} is irreducible or n_{2} = n if g_{p} is irreducible). By the$$
$$induction hypothesis, g(X) and h(X) can be written as products of irreducible$$
$$polynomials, thus so can f(X).$$
$$(b) If p = 0 and q = m, then g(X) = g_{p} and by hypothesis g_{p} is not a unit. Since$$
$$f_{m} = a_{1} \cdots  a_{n} = g_{p}h_{q} and g_{p} is not a unit, either h_{q} is not a unit in which case, by$$
$$the uniqueness of the number of irreducible elements in the decomposition of f_{m}$$
$$(since A is a UFD), h_{q} is the product of n_{2} < n irreducible elements, or n_{2} = 0$$
$$if h_{q} is irreducible. Since n \ge 1, this implies that (m, n_{2}) < (m, n), and by the$$
$$induction hypothesis h(X) can be written as products of irreducible polynomials.$$
$$Since g_{p} \in A is not a unit, it can also be written as a product of irreducible$$
$$elements, thus so can f(X).$$
$$The case where p = m and q = 0 is similar to the previous case.$$

<!-- PAGE 1143 -->
Tính chất (2') suy ra theo Bổ đề 32.9. Theo Mệnh đề 32.2, [X] là UFD. Như hệ quả của Định lý 32.10 và bằng cách sử dụng quy nạp, ta lưu ý rằng với mọi trường $K$, đa thức vành $K[X_{1}, \dots  , X_{n}]$ là UFD. Cho sake của tính đầy đủ, ta sẽ chứng minh rằng mọi PID là UFD. Thứ nhất, ta ôn tập/tổng quan khái niệm của ước chung lớn nhất (gcd) và đặc trưng của ước chung lớn nhất (gcd)’s trong PID. Cho trước miền nguyên (integral domain) $A$, với mọi hai các phần tử, $b \in A$,, $b \neq  0$, ta nói rằng $d \in A (d \neq  0)$ là lớn nhất chung/phổ biến ước (ước chung lớn nhất (gcd)) của và $b$ nếu
$(1) d$ chia hết cả hai và $b$.
$(2)$ Với mọi $h \in A (h \neq  0)$, nếu $h$ chia hết cả hai và $b$, thì $h$ chia hết $d$. Ta cũng nói rằng và $b$ là một cách tương đối nguyên tố nếu $1$ là ước chung lớn nhất (gcd) của và $b$. Lưu ý rằng và $b$ là một cách tương đối nguyên tố khi và chỉ khi mọi ước chung lớn nhất (gcd) của và $b$ là unit. Nếu $A$ là PID, thì ước chung lớn nhất (gcd)’s được đặc trưng hóa như sau.

> **Mệnh đề 32.11.** Cho $A$ là PID.
$(1)$ Với mọi, $b, d \in A$ (, $b, d \neq  0), d$ là ước chung lớn nhất (gcd) của và $b$ khi và chỉ khi
$$(d) = (a, b) = (a) + (b),$$
I.e., $d$ sinh ra chính lý tưởng (ideal) được sinh bởi và $b$.
$(2)$ (Bezout đồng nhất thức) Hai khác không các phần tử, $b \in A$ là một cách tương đối nguyên tố khi và chỉ khi có một số $x, y \in A$ sao cho
$$ax + by = 1.$$

*Chứng minh.* $(1)$ Nhắc lại rằng lý tưởng (ideal) được sinh bởi và $b$ là tập hợp
$$(a) + (b) = aA + bA = {ax + by | x, y \in A}.$$
Thứ nhất, giả sử rằng $d$ là ước chung lớn nhất (gcd) của và $b$. Nếu do đó, $a \in$ Ad, $b \in$ Ad, và do đó, $(a) \subseteq (d)$ và
$(b) \subseteq (d)$, sao cho
$$(a) + (b) \subseteq (d).$$
Vì $A$ là PID, tồn tại một $t \in A, t \neq  0$, sao cho
$$(a) + (b) = (t),$$
Và do đó, $(a) \subseteq (t)$ và $(b) \subseteq (t)$, mà có nghĩa là $t$ chia hết cả hai và $b$. Vì $d$ là ước chung lớn nhất (gcd) của và $b, t$ phải chia $d$. Nhưng khi đó,
$$(d) \subseteq (t) = (a) + (b),$$

<!-- PAGE 1144 -->
Và do đó, $(d) = (a) + (b)$. Giả sử bây giờ rằng
$$(d) = (a) + (b) = (a, b).$$
Vì $(a) \subseteq (d)$ và $(b) \subseteq (d), d$ chia hết cả hai và $b$. Giả sử rằng $t$ chia hết cả hai và $b$, sao cho $(a) \subseteq (t)$ và $(b) \subseteq (t)$. Thì,
$$(d) = (a) + (b) \subseteq (t),$$
Mà có nghĩa là $t$ chia hết $d$, và $d$ là thật vậy ước chung lớn nhất (gcd) của và $b$.
$(2)$ Bởi $(1)$, nếu và $b$ là một cách tương đối nguyên tố, thì
$$(1) = (a) + (b),$$
Mà cho ta kết quả. Ngược lại, nếu
$$ax + by = 1,$$
Thì
$$(1) = (a) + (b),$$
Và $1$ là ước chung lớn nhất (gcd) của và $b$. Cho trước hai khác không các phần tử, $b \in A$, nếu là bất khả quy (irreducible) phần tử và thực hiện không chia $b$, thì và $b$ là một cách tương đối nguyên tố. Thật vậy, nếu $d$ là không unit và $d$ chia hết cả hai và $b$, thì $a =$ dp và $b =$ dq ở đâu $p$ phải là unit, sao cho
$$b = ap^{-1}q,$$
Và chia hết $b$, một mâu thuẫn.

> **Định lý 32.12.** Cho $A$ là vành. Nếu $A$ là PID, thì $A$ là UFD.

*Chứng minh.* Thứ nhất, ta chứng minh rằng mọi khác không phần tử rằng là không unit có thể được được nhân tử như tích của bất khả quy (irreducible) các phần tử. Cho $\mathcal{S}$ là tập hợp của không tầm thường chính các lý tưởng () sao cho $a \neq  0$ là không unit và không thể được nhân tử như tích của bất khả quy (irreducible) các phần tử (đặc biệt, là không bất khả quy (irreducible)). Giả sử rằng $\mathcal{S}$ là khác rỗng. Ta khẳng định rằng mọi ascending dây chuyền/xích trong $\mathcal{S}$ là hữu hạn. Ngược lại, xét vô hạn ascending dây chuyền/xích
$$(a_{1}) \subset (a_{2}) \subset \cdots  \subset (a_{n}) \subset \cdots  .$$
Ta kiểm chứng được ngay rằng
$$\bigcup_{n\ge1}  (a_{n})$$
Là lý tưởng (ideal) trong $A$. Vì $A$ là PID,
$$\bigcup_{n\ge1}  (a_{n}) = (a)$$

<!-- PAGE 1145 -->
Với một số $a \in A$. Tuy nhiên, ở đó phải là một số $n$ sao cho $a \in (a_{n})$, và do đó,
$$(a_{n}) \subseteq (a) \subseteq (a_{n}),$$
Và dây chuyền/xích stabilizes tại $(a_{n})$. Hệ quả là, có cực đại các lý tưởng $in\mathcal{S}$. Cho () là lý tưởng cực đại (maximal ideal) $in\mathcal{S}$. Thì, với mọi lý tưởng (ideal) $(d)$ sao cho
$$(a) \subset (d)and(a) \neq  (d),$$
Ta phải có $d \in S/$, vì ngược lại () sẽ không là lý tưởng cực đại (maximal ideal) trong $\mathcal{S}$. Nhận thấy rằng là không bất khả quy (irreducible), vì $(a) \in S$, và do đó,
$$a = bc$$
Với một số $b, c \in A$, ở đâu không $b$ cũng không $c$ là unit. Thì,
$$(a) \subseteq (b)and(a) \subseteq (c).$$
Nếu $(a) = (b)$, thì $b =$ au với một số $u \in A$, và thì
$$a = auc,$$
Sao cho
$$1 = uc,$$
Vì $A$ là miền nguyên (integral domain), và do đó, $c$ là unit, một mâu thuẫn. Do đó, $(a) \neq  (b)$, và tương tự, $(a) \neq  (c)$. Nhưng khi đó, bởi trước đó nhận xét $b \in S/$ và $c \in S/$, và vì và $b$ là không units, cả hai $b$ và $c$ nhân tử như các tích của bất khả quy (irreducible) các phần tử và do đó thực hiện $a =$ bc, một mâu thuẫn. Điều này suy ra rằng $\mathcal{S} = \emptyset$, do đó mọi khác không phần tử rằng là không unit có thể được được nhân tử như tích của bất khả quy (irreducible) các phần tử để chứng minh tính duy nhất của các nhân tử hóa, ta sử dụng Mệnh đề 32.2. Giả sử rằng là bất khả quy (irreducible) và rằng chia hết bc. Nếu thực hiện không chia $b$, bởi trước đó nhận xét, và $b$ là một cách tương đối nguyên tố, và theo Mệnh đề 32.11, có một số $x, y \in A$ sao cho
$$ax + by = 1.$$
Do đó,
$$acx + bcy = c,$$
Và vì chia hết bc, ta xem rằng phải chia $c$, như mong muốn. Do đó, ta thu được một cái khác justification của sự kiện rằng $\mathbb{Z}$ là UFD và rằng nếu $K$ là trường, thì K[X] là UFD. Nó nên cũng được lưu ý rằng trong UFD, ước chung lớn nhất (gcd)’s của khác không các phần tử luôn luôn tồn tại. Thật vậy, điều này là tầm thường nếu hoặc $b$ là unit, và ngược lại, ta có thể viết
$$a = p_{1} \cdots  p_{m}andb = q_{1} \cdots  q_{n}$$

<!-- PAGE 1146 -->
Ở đâu $p_{i}, q_{j} \in A$ là bất khả quy (irreducible), và tích của chung/phổ biến các nhân tử của và $b$ là ước chung lớn nhất (gcd) của và $b$ (nó là $1$ là có không có chung/phổ biến các nhân tử). Ta kết luận điều này mục trên UFD’s bởi chứng minh mệnh đề đặc trưng hóa khi UFD là PID. chứng minh là không tầm thường và làm cho sử dụng của Zorn’s bổ đề (một vài lần).

> **Mệnh đề 32.13.** Cho $A$ là vành rằng là UFD, và không trường. Thì, $A$ là PID khi và chỉ khi mọi khác không lý tưởng nguyên tố (prime ideal) là cực đại.

*Chứng minh.* Giả sử rằng $A$ là PID rằng là không trường. Xét bất kỳ khác không lý tưởng nguyên tố (prime ideal), $(p)$, và chọn bất kỳ lý tưởng thực sự (proper ideal) $\mathfrak{A}$ trong $A$ sao cho
$$(p) \subseteq \mathfrak{A}.$$
Vì $A$ là PID, $ideal\mathfrak{A}$ là chính lý tưởng (ideal), $so\mathfrak{A} = (q)$, và $since\mathfrak{A}$ là thực sự/đúng đắn khác không lý tưởng (ideal), $q \neq  0$ và $q$ là không unit. Vì
$$(p) \subseteq (q),$$
$q$ chia hết $p$, và ta có $p = qp_{1}$ với một số $p_{1} \in A$. Bây giờ, theo Mệnh đề 32.1, vì $p \neq  0$ và $(p)$ là lý tưởng nguyên tố (prime ideal), $p$ là bất khả quy (irreducible). Nhưng khi đó, vì $p = qp_{1}$ và $p$ là bất khả quy (irreducible), $p_{1}$ phải là unit (vì $q$ là không unit), mà suy ra rằng
$$(p) = (q);$$
Rằng là, $(p)$ là lý tưởng cực đại (maximal ideal). Ngược lại, ta giả sử rằng mọi khác không lý tưởng nguyên tố (prime ideal) là cực đại. Thứ nhất, ta chứng minh rằng mọi lý tưởng nguyên tố (prime ideal) là chính. Điều này là hiển nhiên cho $(0)$. Nếu $\mathfrak{A}$ là khác không lý tưởng nguyên tố (prime ideal), thì, bởi giả thiết, nó là cực đại. Vì $\mathfrak{A} \neq  (0)$, tồn tại một khác không phần tử $a \in \mathfrak{A}$. Vì $\mathfrak{A}$ là cực đại, là không unit, và vì $A$ là UFD, có một nhân tử hóa $a = a_{1} \cdots  a_{n}$ của vào bất khả quy (irreducible) các phần tử. Vì $\mathfrak{A}$ là nguyên tố, ta có $a_{i} \in \mathfrak{A}$ với một số $i$. Bây giờ, theo Mệnh đề 32.3, vì $a_{i}$ là bất khả quy (irreducible), lý tưởng (ideal) $(a_{i})$ là nguyên tố, và do đó, bởi giả thiết, $(a_{i})$ là cực đại. Vì $(a_{i}) \subseteq \mathfrak{A}$ và $(a_{i})$ là cực đại, ta thu được $\mathfrak{A} = (a_{i})$. Tiếp theo, giả sử rằng $A$ là không PID. Định nghĩa tập hợp, $\mathcal{F}$, bởi
$$\mathcal{F} = {\mathfrak{A} |\mathfrak{A} \subseteq A,\mathfrak{A} is not a principal ideal}.$$
Vì $A$ là không PID, tập hợp $\mathcal{F}$ là khác rỗng. Cũng, độc giả sẽ dễ dàng kiểm tra rằng mọi dây chuyền/xích trong $\mathcal{F}$ là bị chặn trong $\mathcal{F}$. Thật vậy, với mọi dây chuyền/xích $(\mathfrak{A} )_{\in I}$ của các lý tưởng trong $\mathcal{F}$ nó là không khó đến
$$verify that \bigcup_{i}  \mathfrak{A}_{i} is an ideal which is not principal, so \bigcup^{ii}  \mathfrak{A}_{i} \in F. Then, by Zorn’s lemma$$
(Bổ đề $C.1),^{\in I}$ tập hợp $\mathcal{F}$ có một số cực đại phần tử, $\mathfrak{A}.^{i\in I}$ Rõ ràng, $\mathfrak{A} \neq  (0)$ là lý tưởng thực sự (proper ideal) (vì $A = (1))$, và $\mathfrak{A}$ là không nguyên tố, vì ta chỉ đã chỉ ra rằng nguyên tố các lý tưởng là chính. Thì, theo Định lý C.3, tồn tại một lý tưởng cực đại (maximal ideal), $\mathfrak{M}$, sao cho $\mathfrak{A} \subset \mathfrak{M}$. Tuy nhiên, lý tưởng cực đại (maximal ideal) là nguyên tố, và ta có được hiển thị rằng lý tưởng nguyên tố (prime ideal) là chính. Do đó,
$$\mathfrak{A} \subseteq (p),$$
