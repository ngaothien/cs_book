# Tổng Trực giao Các họ, Fourier Các hệ số


<!-- PAGE 2149 -->
Phụ lục $A$ Tổng Trực giao Các họ trong Các không gian Hilbert

## .1 Tổng Trực giao Các họ (Hilbert Các cơ sở),

$$Fourier Coefficients$$
Ta kết luận của ta quick tour của Các không gian Hilbert bởi chỉ ra rằng khái niệm của cơ sở trực giao (orthogonal basis) có thể được suy rộng/tổng quát hóa đến Các không gian Hilbert. Tuy nhiên, hữu ích khái niệm là không thông thường khái niệm của cơ sở (basis), nhưng khái niệm mà là abstraction của khái niệm của Fourier chuỗi. Mọi phần tử của Không gian Hilbert (Hilbert space) là “tổng” của của nó Fourier chuỗi.

> **Định nghĩa A.1.** Cho trước Không gian Hilbert (Hilbert space) $E$, họ $(u_{k})_{k\in K}$ của khác không các vectơ là họ trực giao (orthogonal family) khi và chỉ khi $u_{k}$ là đôi một trực giao, i.e., $\langle u_{i}, u_{j}\rangle = 0$ với mọi $i \neq  j (i, j \in K)$, và họ trực chuẩn (orthonormal family) khi và chỉ khi $\langle u_{i}, u_{j}\rangle = \delta_{i, j}$, với mọi $i, j \in K$. tổng họ trực giao (orthogonal family) (hoặc hệ) hoặc Hilbert cơ sở (basis) là họ trực giao (orthogonal family) rằng là trù mật trong $E$. Điều này có nghĩa là với mọi $v \in E$, với mọi $\epsilon  > 0$, tồn tại một hữu hạn tập con $I \subseteq K$ và một số họ $(\lambda_{i} )_{i\in I}$ của phức các số, sao cho
$$v - \sum_{i\in I}  \lambda_{i} u_{i} < \epsilon .$$
Cho trước họ trực giao (orthogonal family) $(u_{k})_{k\in K}$, với mọi $v \in E$, với mọi $k \in K$, vô hướng (scalar) $c_{k} = \langle v, u_{k}\rangle /\|u_{k}\|^{2}$ được gọi là thứ $k$ Fourier hệ số của $v$ trên $(u_{k})_{k\in K}$.
Nhận xét: thuật ngữ Hilbert cơ sở (basis) là misleading bởi vì Hilbert cơ sở (basis) $(u_{k})_{k\in K}$ là không nhất thiết cơ sở (basis) trong đại số nghĩa. Thật vậy, nói chung, $(u_{k})_{k\in K}$ thực hiện không sinh (span) $E$. Một cách trực quan, nó lấy các tổ hợp tuyến tính của $u_{k}’s$ với một cách vô hạn nhiều khác không các hệ số đến sinh (span) $E$. Technically, điều này là đạt được theo các giới hạn. Trong thứ tự để tránh confusion giữa các cơ sở trong đại số nghĩa và Hilbert các cơ sở, một số các tác giả refer đến đại số các cơ sở như Hamel các cơ sở và đến tổng trực giao các họ (hoặc Hilbert các cơ sở) như Schauder các cơ sở.
$$2149$$

<!-- PAGE 2150 -->
Cho trước họ trực giao (orthogonal family) $(u_{k})_{k\in K}$, với mọi hữu hạn tập con I của $K$, ta thường gọi các tổng của
$$the form \sum_{i}  \in  \lambda u partial sums of Fourier series, and if these partial sums converge to a$$
$$limit denoted^{I} as \sum_{k}^{ii}  \in K c_{k}u_{k}, we call \sum_{k}  \in K c_{k}u_{k} a Fourier series.$$
Tuy nhiên, ta có để tạo nghĩa của như vậy các tổng! Thật vậy, khi $K$ là unordered hoặc uncountable, khái niệm của giới hạn hoặc tổng có không đã được được định nghĩa. Điều này có thể được được thực hiện như sau (cho nhiều hơn/thêm chi tiết, xem Dixmier $[52])$:

> **Định nghĩa A.2.** Cho trước không gian vectơ định chuẩn (normed vector space) $E$ (nói, Không gian Hilbert (Hilbert space)), với mọi khác rỗng chỉ số tập hợp $K$, ta nói rằng họ $(u_{k})_{k\in K}$ của các vectơ trong $E$ là khả tổng với tổng $v \in E$ khi và chỉ khi với mọi $\epsilon  > 0$, tồn tại một hữu hạn tập con I của $K$, sao cho,
$$v - \sum_{j\in J}  u_{j} < \epsilon$$
Với mọi hữu hạn tập con $J$ với $I \subseteq J \subseteq K$. Ta nói rằng họ $(u_{k})_{k\in K}$ là khả tổng khi và chỉ khi tồn tại một $v \in E$ sao cho $(u_{k})_{k\in K}$ là khả tổng với tổng $v$. họ $(u_{k})_{k\in K}$ là Cauchy họ khi và chỉ khi với mọi $\epsilon  > 0$, có một hữu hạn tập con I của $K$, sao cho,
$$\sum_{j\in J}  u_{j}


$< \epsilon$$$ for every finite subset $J$ of $K$ with I $\cap J = \emptyset$,
$$If (u_{k})_{k\in K} is summable with sum v, we usually denote v as \sum_{k}  \in K u_{k}. The following$$
Technical mệnh đề sẽ là cần thiết:

> **Mệnh đề A.1.** Cho $E$ là đầy đủ không gian vectơ định chuẩn (normed vector space) (nói, Không gian Hilbert (Hilbert space)).
$(1)$ Với mọi khác rỗng chỉ số tập hợp $K$, họ $(u_{k})_{k\in K}$ là khả tổng khi và chỉ khi nó là Cauchy họ.
$(2)$ Cho trước họ $(r_{k})_{k\in K}$ của không âm các số thực $r_{k} \ge 0$, nếu tồn tại một thực số $B > 0$
$$such that \sum_{i}  r_{i} < B for every finite subset I of K, then (r_{k})_{k\in} is summable and$$
$$\sum_{k}  \in K r_{k} = r,^{\in I} where r is least upper bound of the set of finite sums \sum_{i}^{K}  \in I r_{i} (I \subseteq K).$$

*Chứng minh.* $(1)$ Nếu $(u_{k})_{k\in K}$ là khả tổng, với mọi hữu hạn tập con I của $K$, cho
$$u_{I} = \sum_{i\in I}  u_{i}andu = \sum_{k\in K}  u_{k}$$
Với mọi $\epsilon  > 0$, tồn tại một hữu hạn tập con I của $K$ sao cho
$$\|u -u_{L}\|< \epsilon /2$$
Với mọi hữu hạn các tập con $L$ sao cho $I \subseteq L \subseteq K$. Với mọi hữu hạn tập con $J$ của $K$ sao cho I $\cap J = \emptyset$, vì $I \subseteq$ I $\cup J \subseteq K$ và I $\cup J$ là hữu hạn, ta có
$$\|u -u_{I\cup J}\|< \epsilon /2and\|u -u_{I}\|< \epsilon /2,$$

<!-- PAGE 2151 -->
Và vì
$$\|u_{I\cup J} -u_{I}\|\le \|u_{I\cup J} -u\|+ \|u -u_{I}\|$$
Và $u_{I\cup J}$ - $u_{I} = u_{J}$ vì I $\cap J = \emptyset$, ta thu được
$$\|u_{J}\|= \|u_{I\cup J} -u_{I}\|< \epsilon ,$$
Mà là điều kiện cho $(u_{k})_{k\in K}$ là Cauchy họ. Ngược lại, giả sử rằng $(u_{k})_{k\in K}$ là Cauchy họ. Ta định nghĩa một cách quy nạp giảm dãy $(X_{n})$ của các tập con của $E$, mỗi của diameter nhiều nhất $1/n$, như sau: Cho $n = 1$, vì $(u_{k})_{k\in K}$ là Cauchy họ, tồn tại một hữu hạn tập con $J_{1}$ của $K$ sao cho
$$\|u_{J}\|< 1/2$$
Với mọi hữu hạn tập con $J$ của $K$ với $J_{1} \cap J = \emptyset$. Ta chọn một số hữu hạn tập con $J_{1}$ với ở trên tính chất, và ta cho $I_{1} = J_{1}$ và
$$X_{1} = {u_{I} | I_{1} \subseteq I \subseteq K, I finite}.$$
Cho $n \ge 1$, tồn tại một hữu hạn tập con $J_{n+1}$ của $K$ sao cho
$$\|u_{J}\|< 1/(2n + 2)$$
Với mọi hữu hạn tập con $J$ của $K$ với $J_{n+1} \cap J = \emptyset$. Ta chọn một số hữu hạn tập con $J_{n+1}$ với ở trên tính chất, và ta cho $I_{n+1} = I_{n} \cup J_{n+1}$ và
$$X_{n+1} = {u_{I} | I_{n+1} \subseteq I \subseteq K, I finite}.$$
Vì $I_{n} \subseteq I_{n+1}$, hiển nhiên là $X_{n+1} \subseteq X_{n}$ với mọi $n \ge 1$. Ta cần để chứng minh rằng mỗi $X_{n}$ có diameter nhiều nhất $1/n$. Vì $J_{n}$ đã được chọn sao cho
$$\|u_{J}\|< 1/(2n)$$
Với mọi hữu hạn tập con $J$ của $K$ với $J_{n} \cap J = \emptyset$, và vì $J_{n} \subseteq I_{n}$, nó là cũng đúng rằng
$$\|u_{J}\|< 1/(2n)$$
Với mọi hữu hạn tập con $J$ của $K$ với $I_{n} \cap J = \emptyset$ (vì $I_{n} \cap J = \emptyset$ và $J_{n} \subseteq I_{n}$ suy ra rằng $J_{n} \cap J = \emptyset$). Thì với mọi hai hữu hạn các tập con $J, L$ sao cho $I_{n} \subseteq J, L \subseteq K$, ta có
$$\|u_{J-In}\|< 1/(2n)and\|u_{L-In}\|< 1/(2n),$$
Và vì
$$\|u_{J} -u_{L}\|\le \|u_{J} -u_{In}\|+ \|u_{In} -u_{L}\|= \|u_{J-In}\|+ \|u_{L-In}\|,$$
Ta thu được
$$\|u_{J} -u_{L}\|< 1/n,$$

<!-- PAGE 2152 -->
$$which \frac{proves}{X_{n+1}} that \frac{\delta (}{X_{n},} X_{n}) \le 1/n. Now if we consider the sequence of closed sets (\overline{X}_{n}), we$$
$$still have  \subseteq  and by Proposition 48.4, \infty \delta ( \frac{\overline{X}_{n})}{X_{n}} = \delta (X_{n}) \le 1/n, which means that$$
$$lim_{n\to \infty}\delta (X_{n}) = 0, and by Proposition 48.4, \bigcap_{n}  =1  consists of a single element u. We$$
Khẳng định rằng $u$ là tổng của họ $(u_{k})_{k\in K}$. Với mọi $\epsilon  > 0$, tồn tại một $n \ge 1$ sao cho $n > 2/\epsilon$, và vì $u \in \overline{X}_{m}$ với mọi $m \ge 1$, tồn tại một hữu hạn tập con $J_{0}$ của $K$ sao cho $I_{n} \subseteq J_{0}$ và
$$\|u -u_{J0}\|< \epsilon /2,$$
Ở đâu $I_{n}$ là hữu hạn tập con của $K$ liên quan trong định nghĩa của $X_{n}$. Tuy nhiên, vì $\delta (X_{n}) \le 1/n$, với mọi hữu hạn tập con $J$ của $K$ sao cho $I_{n} \subseteq J$, ta có
$$\|u_{J} -u_{J0}\|\le 1/n < \epsilon /2,$$
Và vì
$$\|u -u_{J}\|\le \|u -u_{J0}\|+ \|u_{J0} -u_{J}\|,$$
Ta thu được
$$\|u -u_{J}\|< \epsilon$$
Với mọi hữu hạn tập con $J$ của $K$ với $I_{n} \subseteq J$, mà chứng tỏ rằng $u$ là tổng của họ $(u_{k})_{k\in K}$.
$$(2) Since every finite sum \sum_{i}  \in I r_{i} is bounded by the uniform bound B, the set of these$$
Hữu hạn các tổng có least trên cận $r \le B$. Với mọi $\epsilon  > 0$, vì $r$ là least trên cận
$$of the finite sums \sum_{i}  \in I r_{i} (where I finite, I \subseteq K), there is some finite I \subseteq K such that$$
$$r - \sum_{i\in I}  r_{i} < \epsilon ,$$
Và vì $r_{k} \ge 0$ với mọi $k \in K$, ta có
$$\sum_{i\in I}  r_{i} \le \sum_{j\in J}  r_{j}$$
Bất cứ khi nào $I \subseteq J$, mà chỉ ra rằng
$$r - \sum_{j\in J}  r_{j} \le r - \sum_{i\in I}  r_{i} < \epsilon$$
Với mọi hữu hạn tập con $J$ sao cho $I \subseteq J \subseteq K$, chứng minh rằng $(r_{k})_{k\in K}$ là khả tổng với tổng
$$\sum_{k}  \in K r_{k} = r.$$

<!-- PAGE 2153 -->
Nhận xét: khái niệm của summability suy ra rằng tổng của họ $(u_{k})_{k\in K}$ là độc lập của bất kỳ thứ tự trên $K$. Trong điều này nghĩa nó là loại của “giao hoán summability.” Chính xác hơn, nó là dễ để chỉ ra rằng với mọi song ánh $\phi$: $K \to K$ (một cách trực quan, reordering của $K)$, họ $(u_{k})_{k\in K}$ là khả tổng khi và chỉ khi họ $(u_{l})_{l\in\phi(K)}$ là khả tổng, và nếu do đó, chúng có cùng tổng. sau đây mệnh đề cho một số của chính các tính chất của Fourier các hệ số. Trong số khác things, nhiều nhất countably nhiều của Fourier hệ số có thể là khác không, và riêng các tổng của Fourier chuỗi hội tụ. Cho trước họ trực giao (orthogonal family) $(u_{k})_{k\in K}$, ta cho $U_{k} = \mathbb{C} u_{k}$, và $p_{Uk}$: $E \to U_{k}$ là phép chiếu của $E$ lên $U_{k}$.

> **Mệnh đề A.2.** Cho $E$ là Không gian Hilbert (Hilbert space), $(u_{k})_{k\in K}$ họ trực giao (orthogonal family) trong $E$, và $V$ bao đóng (closure) của không gian con được sinh bởi $(u_{k})_{k\in K}$. Các tính chất sau đây đúng:
$(1)$ Với mọi $v \in E$, với mọi hữu hạn tập con $I \subseteq K$, ta có
$$\sum_{i\in I}  |c_{i}|^{2}\le \|v\|^{2},$$
Ở đâu $c_{k}$ là Fourier các hệ số của $v$.
$(2)$ Với mọi vectơ $v \in E$, nếu $(c_{k})_{k\in K}$ là Fourier các hệ số của $v$, các điều kiện sau đây là tương đương:
(2a) $v \in V$
$$(2b) The family (c_{k}u_{k})_{k\in K} is summable and v = \sum_{2k}  c_{k}u_{k}.$$
$$(2c) The family (|c_{k}|^{2})_{k\in K} is summable and \|v\|= \sum_{k}^{\in K}  \in K |c_{k}|^{2};$$
$(3)$ họ $(|c_{k}|^{2})_{k\in K}$ là khả tổng, và ta có Bessel bất đẳng thức:
$$\sum_{k\in K}  |c_{k}|^{2}\le \|v\|^{2}.$$
Hệ quả là, nhiều nhất countably nhiều của $c_{k}$ có thể là khác không. họ
$$(c_{k}u_{k})_{k\in K} forms a Cauchy family, and thus, the Fourier series \sum_{k}  \in K c_{k}u_{k} converges$$
$$in E to some vector u = \sum_{k}  \in K c_{k}u_{k}. Furthermore, u = p_{V} (v).$$
Xem Hình.1.

*Chứng minh.* $(1)$ Cho
$$u_{I} = \sum_{i\in I}  c_{i}u_{i}$$

<!-- PAGE 2154 -->
$$v, uk$$
$$form c  =$$
$$v=\Sigma_{ckuk} k\overline{2}$$
$$u$$
$$k       Kek$$
$$\overline{V = span(u  )}\overline{k}$$
$$(i.)$$
$$E$$
$$v$$
$$v, uk$$
$$form c  =$$
$$u = \Sigma_{ckuk}  k\overline{2}$$
$$u$$
$$k       Kek$$
$$\overline{V = span(u  )}\overline{k}$$
$$(ii.)$$
$$E$$
**Hình A.1:** schematic illustration của Mệnh đề.2. Hình $(i.)$ minh họa Điều kiện (2b), trong khi Hình (ii.) minh họa Điều kiện $(3)$. Lưu ý $E$ là tím oval và $V$ là magenta oval. Trong cả hai các trường hợp, lấy vectơ của $E$, tạo thành Fourier các hệ số $c_{k}$, thì tạo thành
$$the Fourier series \sum_{k}  c_{k}u_{k}. Condition (2b) ensures v equals its Fourier series since v \in V .$$
Tuy nhiên, nếu $v \in / V ,^{\in K}$ Fourier chuỗi thực hiện không bằng nhau $v$. Eventually, ta sẽ discover rằng $V = E$, mà suy ra rằng rằng Fourier chuỗi hội tụ đến của nó vectơ $v$. với mọi hữu hạn tập con I của $K$. Ta khẳng định rằng $v -u_{I}$ là trực giao đến $u_{i}$ với mọi $i \in$ I. Thật vậy,
$$*+$$
$$\langle v -u_{I}, u_{i}\rangle =v - \sum_{j\in I}  c_{j}u_{j}, u_{i}$$
$$= \langle v, u_{i}\rangle - \sum_{j\in I}  c_{j} \langle u_{j}, u_{i}\rangle$$
$$= \langle v, u_{i}\rangle -c_{i}\|u_{i}\|^{2}$$
$$= \langle v, u_{i}\rangle -\langle v, u_{i}\rangle = 0,$$

<!-- PAGE 2155 -->
Vì $\langle u_{j}, u_{i}\rangle = 0$ với mọi $i \neq  j$ và $c_{i} = \langle v, u_{i}\rangle /\|u_{i}\|^{2}$. Hệ quả là, ta có
$$\|v\|^{2}=v - \sum_{i\in I}  c_{i}u_{i} + \sum_{i\in I}  c_{i}u_{i}^{2}$$
$$=v - \sum_{i\in I}  c_{i}u_{i}^{2}+ \sum_{i\in I}  c_{i}u_{i}^{2}$$
$$=v - \sum_{i\in I}  c_{i}u_{i}^{2}+ \sum_{i\in I}  |c_{i}|^{2},$$
Vì $u_{i}$ là đôi một trực giao, nghĩa là,
$$\|v\|^{2}=v - \sum_{i\in I}  c_{i}u_{i}^{2}+ \sum_{i\in I}  |c_{i}|^{2}.$$
Do đó,
$$\sum_{i\in I}  |c_{i}|^{2}\le \|v\|^{2},$$
Như đã khẳng định.
$(2)$ Ta chứng minh dây chuyền/xích của implications $(a) \Rightarrow (b) \Rightarrow (c) \Rightarrow$ ().
$(a) \Rightarrow (b)$: Nếu $v \in V$, vì $V$ là bao đóng (closure) của không gian con được sinh (spanned) bởi $(u_{k})_{k\in K}$, với mọi $\epsilon  > 0$, tồn tại một hữu hạn tập con I của $K$ và một số họ $(\lambda_{i} )_{i\in I}$ của phức các số, sao cho
$$v - \sum_{i\in I}  \lambda_{i} u_{i} < \epsilon .$$
Bây giờ với mọi hữu hạn tập con $J$ của $K$ sao cho $I \subseteq J$, ta có
$$v - \sum_{i\in I}  \lambda_{i} u_{i}^{2}=v - \sum_{j\in J}  c_{j}u_{j} + \sum_{j\in J}  c_{j}u_{j} - \sum_{i\in I}  \lambda_{i} u_{i}^{2}$$
$$=v - \sum_{j\in J}  c_{j}u_{j}^{2}+ \sum_{j\in J}  c_{j}u_{j} - \sum_{i\in I}  \lambda_{i} u_{i}^{2},$$
$$since I \subseteq J and the u_{j} (with j \in J) are orthogonal to v - \sum_{j}  \in J c_{j}u_{j} by the argument in (1),$$
Mà chỉ ra rằng
$$v - \sum_{j\in J}  c_{j}u_{j} \le v - \sum_{i\in I}  \lambda_{i} u_{i} < \epsilon ,$$
Và do đó, rằng họ $(c_{k}u_{k})_{k\in K}$ là khả tổng với tổng $v$, sao cho
$$v = \sum_{k\in K}  c_{k}u_{k}.$$

<!-- PAGE 2156 -->
$$(b) \Rightarrow (c): If v = \sum_{k}  \in K c_{k}u_{k}, then for every \epsilon  > 0, there some finite subset I of K, such$$
Rằng
$$\sqrt$$
$$v - \sum_{j\in J}  c_{j}u_{j} <\overline{\epsilon ,}$$
Với mọi hữu hạn tập con $J$ của $K$ sao cho $I \subseteq J$, và vì ta được chứng minh trong $(1)$ rằng
$$\|v\|^{2}=v - \sum_{j\in J}  c_{j}u_{j}^{2}+ \sum_{j\in J}  |c_{j}|^{2},$$
Ta thu được
$$\|v\|^{2}- \sum_{j\in J}  |c_{j}|^{2}< \epsilon ,$$
Mà chứng tỏ rằng $(|c_{k}|^{2})_{k\in K}$ là khả tổng với tổng $\|v\|^{2}$.
$(c) \Rightarrow$ (): Cuối cùng, nếu $(|c_{k}|^{2})_{k\in K}$ là khả tổng với tổng $\|v\|^{2}$, với mọi $\epsilon  > 0$, tồn tại một hữu hạn tập con I của $K$ sao cho
$$\|v\|^{2}- \sum_{j\in J}  |c_{j}|^{2}< \epsilon^{2}$$
Với mọi hữu hạn tập con $J$ của $K$ sao cho $I \subseteq J$, và một lần nữa, bằng cách sử dụng sự kiện rằng
$$\|v\|^{2}=v - \sum_{j\in J}  c_{j}u_{j}^{2}+ \sum_{j\in J}  |c_{j}|^{2},$$
Ta thu được
$$v - \sum_{j\in J}  c_{j}u_{j} < \epsilon ,$$
$$which proves that (c_{k}u_{k})_{k\in K} is summable with sum \sum_{k}  \in K c_{k}u_{k} = v, and v \in V .$$
$$(3) Since \sum_{k\in Ki}  \in I |c_{i}|^{2}\le \|v\|^{2}for every finite subset I of K, by Proposition A.1(2), the$$
Họ $(|c_{k}|^{2})$ là khả tổng. Bessel bất đẳng thức
$$\sum_{k\in K}  |c_{k}|^{2}\le \|v\|^{2}$$
$$is an obvious consequence of the inequality \sum_{i}  |c_{i}|^{2}\le \|v\|^{2}(for every finite I \subseteq K). Now$$
Với mọi tự nhiên số $n \ge 1$, nếu $K_{n}$ là $the^{\in I}$ tập con của $K$ bao gồm của tất cả $c_{k}$ sao cho $|c_{k}| \ge 1/n$, số của các phần tử trong $K_{n}$ là nhiều nhất
$$\sum_{k\in Kn}  |nc_{k}|^{2}\le n^{2} \sum_{k\in K}  |c_{k}|^{2}\le n^{2}\|v\|^{2},$$
Mà là hữu hạn, và do đó, nhiều nhất đếm được số của $c_{k}$ có thể là khác không.

<!-- PAGE 2157 -->
Vì $(|c_{k}|^{2})_{k\in K}$ là khả tổng với tổng $c$, theo Mệnh đề.1(1) ta biết rằng với mọi $\epsilon  > 0$, tồn tại một hữu hạn tập con I của $K$ sao cho
$$\sum_{j\in J}  |c_{j}|^{2}< \epsilon^{2}$$
Với mọi hữu hạn tập con $J$ của $K$ sao cho I $\cap J = \emptyset$. Vì
$$\sum_{j\in J}  c_{j}u_{j}^{2}= \sum_{j\in J}  |c_{j}|^{2},$$
Ta thu được
$$\sum_{j\in J}  c_{j}u_{j}


$< \epsilon$.$$ This proves that $(c_{k}u_{k})_{k\trong K}$ là Cauchy họ, mà, theo Mệnh đề.1(1), suy ra rằng
$$(c_{k}u_{k})_{k\in K} is summable since E is complete. Thus, the Fourier series \sum_{k}  \in K c_{k}u_{k} is summable,$$
Với tổng của nó được ký hiệu $u \in V$.
$$Since \sum_{k}  \in K c_{k}u_{k} is summable with sum u, for every \epsilon  > 0, there is some finite subset I_{1}$$
Của $K$ sao cho
$$u - \sum_{j\in J}  c_{j}u_{j} < \epsilon$$
Với mọi hữu hạn tập con $J$ của $K$ sao cho $I_{1} \subseteq J$. Bởi tam giác bất đẳng thức, với mọi hữu hạn tập con I của $K$,
$$u -v \le u - \sum_{i\in I}  c_{i}u_{i} + \sum_{i\in I}  c_{i}u_{i} -v.$$
$$By (2), every w \in V is the sum of its Fourier series \sum_{k}  \in K \lambda_{k} u_{k}, and for every \epsilon  > 0, there$$
Là một số hữu hạn tập con $I_{2}$ của $K$ sao cho
$$w - \sum_{j\in J}  \lambda_{j} u_{j} < \epsilon$$
Với mọi hữu hạn tập con $J$ của $K$ sao cho $I_{2} \subseteq J$. Bởi tam giác bất đẳng thức, với mọi hữu hạn tập con I của $K$,
$$v - \sum_{i\in I}  \lambda_{i} u_{i} \le \|v -w\|+w - \sum_{i\in I}  \lambda_{i} u_{i}.$$
Đặt $I = I_{1} \cup I_{2}$, vì ta đã chỉ ra trong $(2)$ rằng
$$v - \sum_{i\in I}  c_{i}u_{i} \le v - \sum_{i\in I}  \lambda_{i} u_{i}$$
