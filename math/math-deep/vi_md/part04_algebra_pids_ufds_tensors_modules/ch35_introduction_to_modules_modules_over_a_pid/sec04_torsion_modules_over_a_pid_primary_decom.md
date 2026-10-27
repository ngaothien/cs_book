# Xoắn (torsion) Các môđun trên PID; Phân rã sơ cấp (primary decomposition)


<!-- PAGE 1291 -->
Và
$$\phi (\psi (u)) = \phi \overline{(1} \otimes u)$$
$$= 1u$$
$$= u,$$
Mà chỉ ra rằng $\phi$ và $\psi$ là mutual các nghịch đảo. Ta bây giờ develop lý thuyết cần đến understand cấu trúc của sinh hữu hạn (finitely generated) các môđun trên PID.

## 35.4 Xoắn (torsion) Các môđun trên PID; Sơ cấp

$$Decomposition$$
Ta bắt đầu bởi xét các môđun trên tích vành thu được từ trực tiếp phân rã, như trong Định nghĩa 32.6. Trong mục này và tiếp theo, ta closely suy ra Bourbaki $[26]$ (Chương VII). Cho $A$ là vành giao hoán (commutative ring) và cho $(\mathfrak{b}_{1}, \dots  ,\mathfrak{b}_{n})$ là các lý tưởng trong $A$ sao cho có một đẳng cấu $A \approx A/\mathfrak{b}_{1} \times  \cdots  \times  A/\mathfrak{b}_{n}$. Từ Định lý 32.17 phần $(b)$, ở đó tồn tại một số các phần tử $e_{1}, \dots  , e_{n}$ của $A$ sao cho
$$e_{i}^{2} = e_{i}$$
$$e_{i}e_{j} = 0,i \neq  j$$
$$e_{1} + \cdots  + e_{n} = 1_{A},$$
Và $\mathfrak{b}_{i} = (1_{A}$ - $e_{i})A$, cho $i, j = 1, \dots  , n$. Cho trước A-module $M$ với $A \approx A/\mathfrak{b}_{1}\times \cdots \times A/\mathfrak{b}_{n}$, cho $M_{i}$ là tập con của $M$ annihilated bởi $\mathfrak{b}_{i}$; nghĩa là,
$$M_{i} = {x \in M | bx = 0, for all b \in \mathfrak{b}_{i}}.$$
Bởi vì $\mathfrak{b}_{i}$ là lý tưởng (ideal), mỗi $M_{i}$ là môđun con của $M$. Nhận thấy rằng nếu $\lambda , \mu  \in A, b \in \mathfrak{b}_{i}$, và nếu $\lambda$ - $\mu  = b$, thì với mọi $x \in M_{i}$, vì bx $= 0$,
$$\lambda x = (\mu  + b)x = \mu x + bx = \mu x,$$
Do đó $M_{i}$ có thể được được quan điểm như $A/\mathfrak{b}_{i}-$ môđun.

> **Mệnh đề 35.15.** Cho trước vành $A \approx A/\mathfrak{b}_{1} \times  \cdots  \times  A/\mathfrak{b}_{n}$ như ở trên, A-module $M$ là tổng trực tiếp (direct sum)
$$M = M_{1} \oplus \cdots  \oplus M_{n},$$
Ở đâu $M_{i}$ là môđun con của $M$ annihilated bởi $\mathfrak{b}_{i}$.

<!-- PAGE 1292 -->

*Chứng minh.* Cho $i = 1, \dots  , n$, cho $p_{i}$: $M \to M$ là ánh xạ cho trước bởi
$$p_{i}(x) = e_{i}x,x \in M.$$
Ánh xạ $p_{i}$ là rõ ràng tuyến tính, và bởi vì của các tính chất được thỏa mãn bởi $e_{i}s$, ta có
$$p_{i}^{2} = p_{i}$$
$$p_{i}p_{j} = 0,i \neq  j$$
$$p_{1} + \cdots  + p_{n} = id.$$
Điều này chỉ ra rằng $p_{i}$ là các phép chiếu, và theo Mệnh đề 6.8 (mà cũng nghiệm đúng cho các môđun), ta có tổng trực tiếp (direct sum)
$$M = p_{1}(M) \oplus \cdots  \oplus p_{n}(M) = e_{1}M \oplus \cdots  \oplus e_{n}M.$$
Nó vẫn còn để chỉ ra rằng $M_{i} = e_{i}M$. Vì $(1$ - $e_{i})e_{i} = e_{i}$ - $e_{i}^{2} = e_{i}$ - $e_{i} = 0$, ta xem rằng $e_{i}M$ là annihilated bởi $\mathfrak{b}_{i} = (1$ - $e_{i})A$. Hơn nữa, cho i̸ $= j$, với mọi $x \in M$, ta có $(1$ - $e_{i})e_{j}x = (e_{j}$ - $e_{i}e_{j})x = e_{j}x$, do đó không có khác không phần tử của $e_{j}M$ là annihilated bởi $1$ - $e_{i}$, và do đó không annihilated bởi $\mathfrak{b}_{i}$. Suy ra rằng $e_{i}M = M_{i}$, như đã khẳng định.

> **Định nghĩa 35.8.** Cho trước A-module $M$, với mọi khác không $\alpha  \in A$, cho
$$M(\alpha ) = {x \in M | \alpha x = 0},$$
Môđun con của $M$ annihilated bởi $\alpha$. Nếu $\alpha$ chia hết $\beta$, thì $M(\alpha$) $\subseteq M(\beta$), do đó ta có thể định nghĩa
$$M_{\alpha} = \bigcup_{n\ge1}  M(\alpha^{n} ) = {x \in M | (\exists n \ge 1)(\alpha^{n} x = 0)},$$
Môđun con của $M$ bao gồm của tất cả các phần tử của $M$ annihilated bởi một số lũy thừa của $\alpha$. Nếu $N$ là bất kỳ môđun con của $M$, rõ ràng là
$$N_{\alpha} = M \cap M_{\alpha}.$$
Nhắc lại rằng trong PID, bất khả quy (irreducible) phần tử cũng được gọi là một nguyên tố phần tử.

> **Định nghĩa 35.9.** Nếu $A$ là PID và $p$ là nguyên tố phần tử trong $A$, ta nói rằng môđun $M$ là p-primary nếu $M = M_{p}$.

> **Mệnh đề 35.16.** Cho $M$ là môđun trên PID $A$. Với mọi khác không $\alpha  \in A$, nếu
$$\alpha  = up_{1}^{n1} \cdots  p_{r}^{nr}$$
Là nhân tử hóa của $\alpha$ vào nguyên tố các nhân tử (ở đâu $u$ là unit), thì môđun $M(\alpha$) annihilated bởi $\alpha$ là tổng trực tiếp (direct sum)
$$M(\alpha ) = M(p_{1}^{n1} ) \oplus \cdots  \oplus M(p_{r}^{nr} ).$$
Hơn nữa, phép chiếu từ $M(\alpha$) lên $M(p_{i}^{ni}$) là của tạo thành $x \mapsto \gamma_{i} x$, với một số $\gamma_{i}  \in A$, và
$$M(p_{i}^{ni} ) = M(\alpha ) \cap M_{pi}.$$

<!-- PAGE 1293 -->

*Chứng minh.* Thứ nhất nhận thấy rằng vì $M(\alpha$) là annihilated bởi $\alpha$, ta có thể quan điểm $M(\alpha$) như $A/(\alpha$)- môđun. Bởi Chinese phần dư định lý (Định lý 32.16) ứng dụng đến các lý tưởng $(up_{1}^{n1}$) $= (p_{1}^{n1}$), $(p_{2}^{n2}$), $\dots  , (p_{r}^{nr}$), ta có đẳng cấu
$$A/(\alpha ) \approx A/(p_{1}^{n1} ) \times  \cdots  \times  A/(p_{r}^{nr} ).$$
Vì ta cũng có các đẳng cấu
$$A/(p_{i}^{ni} ) \approx (A/(\alpha ))/((p_{i}^{ni} )/(\alpha )),$$
Ta có thể áp dụng Mệnh đề 35.15, và ta thu được tổng trực tiếp (direct sum)
$$M(\alpha ) = N_{1} \oplus \cdots  \oplus N_{r},$$
Ở đâu $N_{i}$ là $A/(\alpha$)-môđun con của $M(\alpha$) annihilated bởi $(p_{i}^{ni} )/(\alpha$), và các phép chiếu lên $N_{i}$ là của tạo thành được phát biểu trong mệnh đề. Tuy nhiên, $N_{i}$ là chỉ A-module $M(p_{i}^{ni}$) annihilated bởi $p_{i}^{ni}$, bởi vì mọi khác không phần tử của $(p_{i}^{ni} )/(\alpha$) là lớp tương đương (equivalence class) modulo $(\alpha$) của tạo thành $\overline{ap}_{i}^{ni}$ với một số khác không $a \in A$, và theo Định nghĩa, $x \in N_{i}$ khi và chỉ khi
$$0 =\overline{ap}_{i}^{ni} x = ap_{i}^{ni} x,for all a \in A -{0},$$
Đặc biệt cho $a = 1$, mà suy ra rằng $x \in M(p_{i}^{ni}$). inclusion $M(p_{i}^{ni}$) $\subseteq M(\alpha$) $\cap M_{pi}$ là rõ ràng. Ngược lại, chọn $x \in M(\alpha$) $\cap M_{pi}$, mà có nghĩa là $\alpha x = 0$ và $p_{i}^{s}x = 0$ với một số $s \ge 1$. Nếu $s < n_{i}$, ta được thực hiện, do đó giả sử $s \ge n_{i}$. Vì $p_{i}^{ni}$ là ước chung lớn nhất (gcd) của $\alpha$ và $p_{i}^{s}$, bởi Bezout, ta có thể viết
$$p_{i}^{ni} = \lambda p_{i}^{s} + \mu \alpha$$
Với một số $\lambda , \mu  \in A$, và thì $p_{i}^{ni} x = \lambda p_{i}^{s}x + \mu \alpha x = 0$, mà chỉ ra rằng $x \in M(p_{i}^{ni}$), như mong muốn. Đây là một ví dụ của Mệnh đề 35.16. Cho $M = \mathbb{Z}/60\mathbb{Z}$, ở đâu $M$ được xét như $a \mathbb{Z}-module$. phần tử trong $M$ được ký hiệu bởi $\overline{x}$, ở đâu $x$ là số nguyên với $0 \le x \le 59$. Cho $\alpha  = 6$ và định nghĩa
$$M(6) = {\overline{x} \in M | 6\overline{x}\overline{= 0}} = {\overline{0},\overline{10},\overline{20},\overline{30},\overline{40},\overline{50}}.$$
Vì $6 = 2 \cdot  3$, Mệnh đề 35.16 suy ra rằng M(6) $=$ M(2) $\oplus$ M(3), ở đâu
$$M(2) = {\overline{x} \in M | 2\overline{x}\overline{= 0}} = {\overline{0},\overline{30}}$$
$$M(3) = {\overline{x} \in M | 3\overline{x}\overline{= 0}} = {\overline{0},\overline{20},\overline{40}}.$$
Nhắc lại rằng nếu $M$ là môđun xoắn (torsion module) trên vành $A$ mà là miền nguyên (integral domain), thì mọi hữu hạn tập hợp của các phần tử $x_{1}, \dots  , x_{n}$ trong $M$ là annihilated bởi $a = a_{1} \cdots  a_{n}$, ở đâu mỗi $a_{i}$ annihilates $x_{i}$. Vì $A$ là PID, ta có thể chọn tập hợp $P$ của bất khả quy (irreducible) các phần tử của $A$ sao cho mọi khác không nonunit của $A$ có duy nhất nhân tử hóa sai khác unit. Thì, ta có kết quả sau cấu trúc định lý cho xoắn (torsion) các môđun mà nghiệm đúng chẵn/ngay cả cho các môđun rằng là không sinh hữu hạn (finitely generated).

<!-- PAGE 1294 -->

> **Định lý 35.17.** (Phân rã sơ cấp (primary decomposition) Định lý) Cho $M$ là torsion-module trên PID. Với mọi bất khả quy (irreducible) phần tử $p \in P$, cho $M_{p}$ là môđun con của $M$ annihilated bởi một số lũy thừa của $p$. Thì, $M$ là (có thể vô hạn) tổng trực tiếp (direct sum)
$$M =MM_{p}.$$
$$p\in P$$

*Chứng minh.* Vì $M$ là torsion-module, với mọi $x \in M$, tồn tại một $\alpha  \in A$ sao cho $x \in M(\alpha$). Theo Mệnh đề 35.16, nếu $\alpha  = up_{1}^{n1} \cdots  p_{r}^{nr}$ là nhân tử hóa của $\alpha$ vào nguyên tố các nhân tử (ở đâu $u$ là unit), thì môđun $M(\alpha$) là tổng trực tiếp (direct sum)
$$M(\alpha ) = M(p_{1}^{n1} ) \oplus \cdots  \oplus M(p_{r}^{nr} ).$$
Điều này có nghĩa là $x$ có thể được viết dưới dạng
$$x = \sum_{p\in P}  x_{p},x_{p} \in M_{p},$$
Với chỉ một cách hữu hạn nhiều $x_{p}$ khác không. Nếu
$$\sum_{p\in P}  x_{p} = \sum_{p\in P}  y_{p}$$
Với mọi $p \in P$, với chỉ một cách hữu hạn nhiều $x_{p}$ và $y_{p}$ khác không, thì $x_{p}$ và $y_{p}$ là annihilated bởi một số chung/phổ biến khác không phần tử $a \in A$, do đó $x_{p}, y_{p} \in$ M(). Theo Mệnh đề 35.16, ta phải có $x_{p} = y_{p}$ với mọi $p$, mà chứng tỏ rằng ta có tổng trực tiếp (direct sum). Rõ ràng là nếu $p$ và p' là hai bất khả quy (irreducible) các phần tử sao cho $p =$ lên' với một số unit $u$, thì $M_{p} = M_{p'}$. Vì vậy, $M_{p}$ chỉ phụ thuộc vào lý tưởng (ideal) $(p)$.

> **Định nghĩa 35.10.** Cho trước torsion-module $M$ trên PID, các môđun $M_{p}$ liên kết với bất khả quy (irreducible) các phần tử trong $P$ được gọi là p-primary các thành phần của $M$. p-primary các thành phần của môđun xoắn (torsion module) một cách duy nhất xác định môđun, như được hiển thị bởi tiếp theo mệnh đề.

> **Mệnh đề 35.18.** Hai xoắn (torsion) các môđun $M$ và $N$ trên PID là đẳng cấu khi và chỉ khi với mọi mọi bất khả quy (irreducible) phần tử $p \in P$, p-primary các thành phần $M_{p}$ và $N_{p}$ của $M$ và $N$ là đẳng cấu.

*Chứng minh.* Cho $f$: $M \to N$ là đẳng cấu. Với mọi $p \in P$, ta có $x \in M_{p}$ khi và chỉ khi $p^{k}x = 0$ với một số $k \ge 1$, do đó
$$0 = f(p^{k}x) = p^{k}f(x),$$
Mà chỉ ra rằng f(x) $\in N_{p}$. Vì vậy, $f$ các thu hẹp đến ánh xạ tuyến tính (linear map) $f$ | $M_{p}$ từ $M_{p}$ đến $N_{p}$. Vì $f$ là đẳng cấu, ta cũng có ánh xạ tuyến tính (linear map) $f^{-1}: M \to N$, và của ta trước đó

<!-- PAGE 1295 -->
Lập luận chỉ ra rằng $f^{-1}$ các thu hẹp đến ánh xạ tuyến tính (linear map) $f^{-1}$ | $N_{p}$ từ $N_{p}$ đến $M_{p}$. Nhưng, $f$ | $M_{p}$ và $f^{-1}$ | $N_{p}$ là mutual các nghịch đảo, do đó $M_{p}$ và $N_{p}$ là đẳng cấu. Ngược lại, nếu $M_{p} \approx N$ với mọi $p \in P$, theo Định lý 35.17, ta thu được đẳng cấu giữa
$$M = \bigoplus_{p}  \in P M_{p} and N = \bigoplus^{p}  p\in P N_{p}.$$
Xét theo Mệnh đề 35.18, tổng trực tiếp (direct sum) của Định lý 35.17 theo của nó p-primary các thành phần được gọi là chính tắc phân rã sơ cấp (primary decomposition) của $M$. Nếu $M$ là sinh hữu hạn (finitely generated) torsion-module, thì Định lý 35.17 lấy sau đây tạo thành.

> **Định lý 35.19.** (Phân rã sơ cấp (primary decomposition) Định lý cho sinh hữu hạn (finitely generated) xoắn (torsion) các môđun) Cho $M$ là sinh hữu hạn (finitely generated) torsion-module trên PID $A$. Nếu Ann(M) $= (a)$ và nếu $a = up_{1}^{n1} \cdots  p_{r}^{nr}$ là nhân tử hóa của vào nguyên tố các nhân tử, thì $M$ là hữu hạn tổng trực tiếp (direct sum)
$$r$$
$$M =MM(p_{i}^{ni} ).$$
$$i=1$$
Hơn nữa, phép chiếu của $M$ trên $M(p_{i}^{ni}$) là của tạo thành $x \mapsto \gamma_{i} x$, với một số $\gamma_{i}  \in A$.

*Chứng minh.* Điều này là immediate hệ quả của Mệnh đề 35.16. Định lý 35.19 áp dụng khi $A =\mathbb{Z}$. Trong trường hợp này, $M$ là sinh hữu hạn (finitely generated) xoắn (torsion) nhóm Abel (abelian group), và định lý nói rằng rằng như vậy nhóm là tổng trực tiếp (direct sum) của hữu hạn số của các nhóm có các phần tử có thứ tự một số lũy thừa của nguyên tố số $p$. Đặc biệt, xét $\mathbb{Z}-module \mathbb{Z}/10\mathbb{Z}$ ở đâu
$$\mathbb{Z}/10\mathbb{Z} = {\overline{0},\overline{1},\overline{2},\overline{3},\overline{4},\overline{5},\overline{6},\overline{7},\overline{8},\overline{9}}.$$
Rõ ràng $\mathbb{Z}/10\mathbb{Z}$ được sinh bởi $\overline{1}$ và Ann $(\mathbb{Z}/10\mathbb{Z}) = 10$. Định lý 35.19 suy ra rằng
$$\mathbb{Z}/10\mathbb{Z} = M(2) \oplus M(5),$$
Ở đâu
$$M(2) = {\overline{x} \in M | 2\overline{x}\overline{= 0}} = {\overline{0},\overline{5}}$$
$$M(5) = {\overline{x} \in M | 5\overline{x}\overline{= 0}} = {\overline{0},\overline{2},\overline{4},\overline{6},\overline{8}}.$$
Định lý 35.17 có một vài hữu ích các hệ quả.

> **Mệnh đề 35.20.** Nếu $M$ là môđun xoắn (torsion module) trên PID, với mọi môđun con $N$ của $M$, ta có tổng trực tiếp (direct sum)
$$N =MN \cap M_{p}.$$
$$p\in P$$

*Chứng minh.* Dễ dàng kiểm chứng được rằng $N \cap M_{p}$ là p-primary thành phần của $N$.

<!-- PAGE 1296 -->

> **Mệnh đề 35.21.** Nếu $M$ là môđun xoắn (torsion module) trên PID, môđun con $N$ của $M$ là trực tiếp nhân tử của $M$ khi và chỉ khi $N_{p}$ là trực tiếp nhân tử của $M_{p}$ với mọi bất khả quy (irreducible) phần tử $p \in A$.

*Chứng minh.* Điều này là bởi vì nếu $N$ và N' là hai các môđun con của $M$, ta có $M = N \oplus$ N' khi và chỉ khi, theo Mệnh đề 35.20, $M_{p} = N_{p} \oplus N_{p}'$ với mọi bất khả quy (irreducible) các phần tử $p \in A$.

> **Định nghĩa 35.11.** A-module $M$ được nói là semi-simple khi và chỉ khi với mọi môđun con $N$ của $M$, tồn tại một môđun con N' của $M$ sao cho $M = N \oplus$ N'.

> **Mệnh đề 35.22.** Cho $A$ là PID mà là không trường, và cho $M$ là bất kỳ A-module. Thì $M$ là semi-simple khi và chỉ khi nó là môđun xoắn (torsion module) và nếu $M_{p} =$ M(p) với mọi bất khả quy (irreducible) phần tử $p \in A$ (nói cách khác, nếu $x \in M$ là annihilated bởi lũy thừa của $p$, thì nó là đã annihilated bởi $p)$.

*Chứng minh.* Giả sử rằng $M$ là semi-simple. Cho $x \in M$ và chọn bất kỳ bất khả quy (irreducible) phần tử $p \in A$. Thì, môđun con pAx có supplement $N$ sao cho
$$M = pAx \oplus N,$$
Do đó ta có thể viết $x =$ pax $+ y$, với một số $y \in N$ và một số $a \in A$. Nhưng khi đó,
$$y = (1 -pa)x,$$
Và vì $p$ là bất khả quy (irreducible), $p$ là không unit, do đó $1$ - pa $\neq  0$. Nhận thấy rằng
$$p(1 -ap)x = py \in pAx \cap N = (0).$$
Vì p(1 - ap) $\neq  0, x$ là xoắn (torsion) phần tử, và do đó $M$ là môđun xoắn (torsion module). ở trên lập luận chỉ ra rằng
$$p(1 -ap)x = 0,$$
Mà suy ra rằng px $= ap^{2}x$, và bởi quy nạp,
$$px = a^{n}p^{n+1}x,for all n \ge 1.$$
Nếu ta chọn $x$ trong $M_{p}$, thì tồn tại một $m \ge 1$ sao cho $p^{m}x = 0$, và ta kết luận rằng
$$px = 0.$$
Vì vậy, $M_{p} =$ M(p), như đã khẳng định. Ngược lại, giả sử rằng $M$ là torsion-module và rằng $M_{p} =$ M(p) với mọi bất khả quy (irreducible) phần tử $p \in A$. Theo Mệnh đề 35.21, nó là đủ để chứng minh rằng môđun annihilated bởi bất khả quy (irreducible) phần tử là semi-simple. Điều này là bởi vì như vậy môđun là không gian vectơ (vector space) trên trường $A/(p)$ (nhắc lại rằng trong PID, lý tưởng (ideal) $(p)$ là cực đại khi và chỉ khi $p$ là bất khả quy (irreducible)), và trong không gian vectơ (vector space), mọi không gian con có supplement. Định lý 35.19 chỉ ra rằng sinh hữu hạn (finitely generated) môđun xoắn (torsion module) là tổng trực tiếp (direct sum) của p-primary các môđun $M_{p}$. Ta có thể thực hiện tốt hơn. Trong mục tiếp theo ta chỉ ra rằng mỗi sơ cấp môđun $M_{p}$ là tổng trực tiếp (direct sum) của xích (cyclic) các môđun của tạo thành $A/(p^{n})$.
