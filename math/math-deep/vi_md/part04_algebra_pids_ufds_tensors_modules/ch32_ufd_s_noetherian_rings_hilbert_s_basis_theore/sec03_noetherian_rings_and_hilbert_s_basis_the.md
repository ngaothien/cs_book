# Các vành Noether và Hilbert's Cơ sở (basis) Định lý


<!-- PAGE 1157 -->
Và cho $k \neq  i$,
$$e_{k}a = e_{k}e_{i}\alpha_{i}  = 0,$$
$$which shows that a = e_{1}a + \cdots  + e_{n}a = 0, so \mathfrak{a}_{i} \cap \bigoplus_{j}  \neq i \mathfrak{a}_{j} = {0} for i = 1, \dots  , n. Thus we$$
Có tổng trực tiếp (direct sum) $A =\mathfrak{a}_{1} \oplus \cdots  \oplus \mathfrak{a}_{n}$.
$(4)$ Vì $\mathfrak{a}_{i} = e_{i}A$ là lý tưởng (ideal) và $A =\mathfrak{a}_{1} \oplus \cdots  \oplus \mathfrak{a}_{n} = e_{1}A \oplus \cdots  \oplus e_{n}A$, ta thu được $\mathfrak{b} =\mathfrak{b} \cap A =\mathfrak{b} \cap \mathfrak{a}_{1} \oplus \cdots  \oplus \mathfrak{b} \cap \mathfrak{a}_{n} =\mathfrak{b} \cap e_{1}A \oplus \cdots  \oplus \mathfrak{b} \cap e_{n}A = e_{1}\mathfrak{b} \oplus \cdots  \oplus e_{n}\mathfrak{b}$, ở đâu mỗi $\mathfrak{b} \cap e_{i}A = e_{i}\mathfrak{b}$ là lý tưởng (ideal).
$(5)$ Vì mỗi $e_{i}$ là khác không lũy đẳng (idempotent) và vành là giao hoán, mỗi $e_{i}A$ là khác không lý tưởng (ideal). chứng minh ở trên chỉ ra rằng ta có tổng trực tiếp (direct sum) $A =\mathfrak{a}_{1} \oplus \cdots  \oplus \mathfrak{a}_{n}$ chỉ sử dụng các tính chất của $e_{i}$ được phát biểu trong $(1)$, do đó nó cũng áp dụng trong $(5)$. Vì ta có tổng trực tiếp (direct sum) $A =\mathfrak{a}_{1} \oplus \cdots  \oplus \mathfrak{a}_{n}$, ta có các phép chiếu $\pi_{i}$: $A \to \mathfrak{a}_{i}$, và ta kiểm tra ngay lập tức rằng ánh xạ $\theta$ cho trước bởi $\theta (a) = (\pi_{1} (a), \dots  , \pi_{n}$ ()) là đẳng cấu $\theta$: $A \to \mathfrak{a}_{1} \times  \cdots  \times \mathfrak{a}_{n}$.
Nhận xét: Chẵn/ngay cả nếu các vành $A_{i}$ là không giao hoán, vì $e_{i}(a_{1}, \dots  , a_{n}) = (a_{1}, \dots  , a_{n})e_{i}$ với mọi $(a_{1}, \dots  , a_{n}) \in A_{1} \times  \cdots  \times  A_{n}$ và tất cả $i = 1, \dots  , n$, ta cũng có
$$e_{i}a = ae_{i},1 \le i \le n,$$
Với mọi $a \in A$. Ta nói rằng $e_{i}$ là trung tâm các lũy đẳng (idempotent). Suy ra rằng Mệnh đề 32.18 cũng nghiệm đúng cho nonncommutative các vành với đồng nhất thức. Nó nên cũng được lưu ý rằng nếu $n \ge 2$ và $e_{1}, \dots  , e_{n} \in A$ là khác không và thỏa mãn các tính chất trong $(1)$, thì chúng là phân biệt và noninvertible. Đặc biệt, $e_{i} \neq  1$. Thật vậy, nếu $e_{i} = e_{j}$ với một số $i \neq  j$, thì
$$e_{i} = e_{i}^{2} = e_{i}e_{j} = 0,$$
Contradicting sự kiện rằng $e_{i} \neq  0$. Nếu $e_{i}$ là khả nghịch, từ $e_{i}e_{j} = 0$ cho $i \neq  j$, ta suy ra rằng $e_{j} = 0$, một mâu thuẫn. Vì $1$ là khả nghịch, $e_{i} \neq  1$. Hệ quả là, khác không các lý tưởng $\mathfrak{a}_{i} = e_{i}A$ là thực sự/đúng đắn các lý tưởng. Ngược lại, ở đó sẽ là một số $a \in A$ sao cho $e_{i}a = 1$, do đó $e_{i}$ sẽ là khả nghịch, một mâu thuẫn.

## 32.3 Các vành Noether và Hilbert’s Cơ sở (basis) Định lý

Cho trước (giao hoán) vành $A$ (với unit phần tử $1)$, lý tưởng (ideal) $\mathfrak{A} \subseteq A$ được nói là sinh hữu hạn (finitely generated) nếu tồn tại một hữu hạn tập hợp ${a_{1}, \dots  , a_{n}}$ của các phần tử từ $\mathfrak{A}$ sao cho
$$\mathfrak{A} = (a_{1}, \dots  , a_{n}) = {\lambda_{1} a_{1} + \cdots  + \lambda_{n} a_{n} | \lambda_{i}  \in A, 1 \le i \le n}.$$
Nếu $K$ là trường, hóa ra là mọi đa thức lý tưởng (ideal) $\mathfrak{A}$ trong $K[X_{1}, \dots  , X_{m}]$ là sinh hữu hạn (finitely generated). sự kiện này do Hilbert và đã biết như Hilbert’s cơ sở (basis) định lý, có rất quan trọng

<!-- PAGE 1158 -->
Các hệ quả. Ví dụ, trong đại số hình học, một là interested trong không quỹ tích của tập hợp của polyomial các phương trình, i.e., tập hợp, $V (\mathcal{P})$, của các bộ $n$ $(\lambda_{1} , \dots  , \lambda_{n}$) $\in K^{n}$ sao cho
$$P_{i}(\lambda_{1} , \dots  , \lambda_{n} ) = 0$$
Với mọi các đa thức $P_{i}(X_{1}, \dots  , X_{n})$ trong một số cho trước họ, $\mathcal{P} = (P_{i})_{i\in I}$. Tuy nhiên, rõ ràng là
$$V (\mathcal{P}) = V (\mathfrak{A}),$$
$where\mathfrak{A}$ là lý tưởng (ideal) được sinh $by\mathcal{P}$. Thì, Hilbert’s cơ sở (basis) định lý nói rằng rằng $V (\mathfrak{A})$ là thực sự được định nghĩa bởi hữu hạn số của các đa thức (bất kỳ tập hợp của các phần tử sinh của $\mathfrak{A})$, chẵn/ngay cả nếu $\mathcal{P}$ là vô hạn. tính chất rằng mọi lý tưởng (ideal) trong vành là sinh hữu hạn (finitely generated) là tương đương đến khác tự nhiên các tính chất, một của mà là so-called ascending dây chuyền/xích điều kiện, abbreviated.c.c. Trước chứng minh Hilbert’s cơ sở (basis) định lý, ta explore equivalence của các điều kiện này.

> **Định nghĩa 32.7.** Cho $A$ là vành giao hoán (commutative ring) với unit $1$. Ta nói rằng $A$ thỏa mãn ascending dây chuyền/xích điều kiện, cho ngắn,.c.c, nếu với mọi ascending dây chuyền/xích của các lý tưởng
$$\mathfrak{A}_{1} \subseteq \mathfrak{A}_{2} \subseteq \cdots  \subseteq \mathfrak{A}_{i} \subseteq \cdots  ,$$
Tồn tại một số nguyên $n \ge 1$ sao cho
$$\mathfrak{A}_{i} =\mathfrak{A}_{n}for alli \ge n + 1.$$
Ta nói rằng $A$ thỏa mãn cực đại điều kiện nếu mọi khác rỗng họ $C$ của các lý tưởng trong $A$ có cực đại phần tử, i.e., tồn tại một $ideal\mathfrak{A} \in C$ mà là không được chứa trong bất kỳ khác lý tưởng (ideal) trong $C$.

> **Mệnh đề 32.19.** vành $A$ thỏa mãn.c.c khi và chỉ khi nó thỏa mãn cực đại điều kiện.

*Chứng minh.* Giả sử rằng $A$ thực hiện không thỏa mãn.c.c. Thì, có một vô hạn chặt ascending dãy của các lý tưởng
$$\mathfrak{A}_{1} \subset \mathfrak{A}_{2} \subset \cdots  \subset \mathfrak{A}_{i} \subset \cdots  ,$$
Và họ $C = {\mathfrak{A}_{i}}$ có không có cực đại phần tử. Ngược lại, giả sử rằng $A$ thỏa mãn.c.c. Cho $C$ là khác rỗng họ của các lý tưởng Vì $C$ là khác rỗng, ta có thể chọn một số lý tưởng (ideal) $\mathfrak{A}_{1}$ trong $C$. Nếu $\mathfrak{A}_{1}$ là không cực đại, thì tồn tại một lý tưởng (ideal) $\mathfrak{A}_{2}$ trong $C$ sao cho
$$\mathfrak{A}_{1} \subset \mathfrak{A}_{2}.$$
Bằng cách sử dụng điều này process, nếu $C$ có không có cực đại phần tử, ta có thể định nghĩa bởi quy nạp vô hạn chặt tăng dãy
$$\mathfrak{A}_{1} \subset \mathfrak{A}_{2} \subset \cdots  \subset \mathfrak{A}_{i} \subset \cdots  .$$
Tuy nhiên,.c.c. suy ra rằng như vậy dãy không thể tồn tại. Vì vậy, $C$ có cực đại phần tử.

<!-- PAGE 1159 -->
Có được hiển thị rằng.c.c. điều kiện là tương đương đến cực đại điều kiện, ta bây giờ chứng minh rằng.c.c. điều kiện là tương đương đến sự kiện rằng mọi lý tưởng (ideal) là sinh hữu hạn (finitely generated).

> **Mệnh đề 32.20.** vành $A$ thỏa mãn.c.c khi và chỉ khi mọi lý tưởng (ideal) là sinh hữu hạn (finitely generated).

*Chứng minh.* Giả sử rằng mọi lý tưởng (ideal) là sinh hữu hạn (finitely generated). Xét ascending dãy của các lý tưởng
$$\mathfrak{A}_{1} \subseteq \mathfrak{A}_{2} \subseteq \cdots  \subseteq \mathfrak{A}_{i} \subseteq \cdots  .$$
$$Observe that \mathfrak{A} = \bigcup_{i}  \mathfrak{A}_{i} is also an ideal.By hypothesis, \mathfrak{A} has a finite generating set$$
${a_{1}, \dots  , a_{n}}$. Theo định nghĩa của $\mathfrak{A}$, mỗi $a_{i}$ thuộc đến một số $\mathfrak{A}_{ji}$, và vì $\mathfrak{A}_{i}$ tạo thành ascending dây chuyền/xích, tồn tại một $m$ sao cho $a_{i} \in \mathfrak{A}_{m}$ cho $i = 1, \dots  , n$. Nhưng khi đó,
$$\mathfrak{A}_{i} =\mathfrak{A}_{m}$$
Với mọi $i \ge m + 1$, và.c.c. nghiệm đúng. Ngược lại, giả sử rằng.c.c. nghiệm đúng. $Let\mathfrak{A}$ là bất kỳ lý tưởng (ideal) trong $A$ và xét họ $C$ của subideals của $\mathfrak{A}$ rằng là sinh hữu hạn (finitely generated). họ $C$ là khác rỗng, vì $(0)$ là subideal của $\mathfrak{A}$. Theo Mệnh đề 32.19, họ $C$ có một số cực đại phần tử, nói $\mathfrak{B}$. Với mọi $a \in \mathfrak{A}$, lý tưởng (ideal) $\mathfrak{B} + (a)$ (ở đâu $\mathfrak{B} + (a) = {b + \lambda$ | $b \in \mathfrak{B}, \lambda  \in A})$ là cũng sinh hữu hạn (finitely generated) (vì $\mathfrak{B}$ là sinh hữu hạn (finitely generated)), và bởi maximality, ta có
$$\mathfrak{B} =\mathfrak{B} + (a).$$
Do đó, ta thu được $a \in \mathfrak{B}$ với mọi $a \in \mathfrak{A}$, và do đó, $\mathfrak{A} =\mathfrak{B}$, và $\mathfrak{A}$ là sinh hữu hạn (finitely generated).

> **Định nghĩa 32.8.** vành giao hoán (commutative ring) $A$ (với unit $1)$ được gọi là noetherian nếu nó thỏa mãn.c.c. điều kiện. noetherian miền xác định là vành Noether (Noetherian ring) rằng là cũng miền xác định. Theo Mệnh đề 32.19 và Mệnh đề 32.20, vành Noether (Noetherian ring) có thể cũng được định nghĩa như vành rằng hoặc thỏa mãn cực đại tính chất hoặc sao cho mọi lý tưởng (ideal) là sinh hữu hạn (finitely generated). chứng minh của Hilbert’s cơ sở (basis) định lý sẽ tạo sử dụng sau đây bổ đề:

> **Bổ đề 32.21.** Cho $A$ là (giao hoán) vành. Với mọi lý tưởng (ideal) $\mathfrak{A}$ trong [X], với mọi $i \ge 0$, cho $L_{i}(\mathfrak{A})$ ký hiệu tập hợp của các phần tử của $A$ bao gồm của $0$ và của các hệ số của $X^{i}$ trong tất cả các đa thức f(X) $\in \mathfrak{A}$ mà là của bậc $i$. Thì, $L_{i}(\mathfrak{A})’s$ tạo thành ascending dây chuyền/xích của các lý tưởng trong $A$. Hơn nữa, nếu $\mathfrak{B}$ là bất kỳ lý tưởng (ideal) của [X] sao cho $\mathfrak{A} \subseteq \mathfrak{B}$ và nếu $L_{i}(\mathfrak{A}) = L_{i}(\mathfrak{B})$ với mọi $i \ge 0$, thì $\mathfrak{A} =\mathfrak{B}$.

*Chứng minh.* Rằng $L_{i}(\mathfrak{A})$ là lý tưởng (ideal) và rằng $L_{i}(\mathfrak{A}) \subseteq L_{i+1}(\mathfrak{A})$ suy ra từ sự kiện rằng nếu f(X) $\in \mathfrak{A}$ và g(X) $\in \mathfrak{A}$, thì f(X) $+$ g(X), $\lambda$ f(X), và Xf(X) tất cả thuộc đến $\mathfrak{A}$. Bây giờ, cho g(X) là bất kỳ đa thức trong $\mathfrak{B}$, và giả sử rằng g(X) có bậc $n$. Vì $L_{n}(\mathfrak{A}) = L_{n}(\mathfrak{B})$, tồn tại một đa thức $f_{n}(X)$ trong $\mathfrak{A}$, của bậc $n$, sao cho g(X) - $f_{n}(X)$ là của bậc nhiều nhất $n$ - $1$. Bây giờ, vì $\mathfrak{A} \subseteq \mathfrak{B}$, đa thức g(X) - $f_{n}(X)$ thuộc đến $\mathfrak{B}$. Bằng cách sử dụng điều này process, ta có thể

<!-- PAGE 1160 -->
Định nghĩa bởi quy nạp dãy của các đa thức $f_{n+i}(X) \in \mathfrak{A}$, sao cho mỗi $f_{n+i}(X)$ là hoặc không hoặc có bậc $n$ - $i$, và
$$g(X) -(f_{n}(X) + f_{n+1}(X) + \cdots  + f_{n+i}(X))$$
Là của bậc nhiều nhất $n$ - $i$ - $1$. Lưu ý rằng điều này cuối cùng đa thức phải là không khi $i = n$, và do đó, g(X) $\in \mathfrak{A}$. Ta bây giờ chứng minh Hilbert’s cơ sở (basis) định lý. chứng minh là substantially Hilbert’s ban đầu chứng minh. slightly shorter chứng minh có thể được cho trước nhưng nó là không như transparent như Hilbert’s chứng minh (xem nhận xét chỉ sau chứng minh của Định lý 32.22, và Zariski và Samuel $[200]$, Chương IV, Mục $1$, Định lý $1)$.

> **Định lý 32.22.** (Hilbert’s cơ sở (basis) định lý) Nếu $A$ là vành Noether (Noetherian ring), thì [X] là cũng vành Noether (Noetherian ring).

*Chứng minh.* Cho $\mathfrak{A}$ là bất kỳ lý tưởng (ideal) trong [X], và ký hiệu bởi $\mathcal{L}$ tập hợp của các phần tử của $A$ bao gồm của $0$ và của tất cả các hệ số của highest bậc các số hạng của tất cả các đa thức trong $\mathfrak{A}$. Nhận thấy rằng
$$\mathcal{L} = \bigcup_{i}  L_{i}(\mathfrak{A}).$$
Do đó, $\mathcal{L}$ là lý tưởng (ideal) trong $A$ (điều này có thể cũng được chứng minh một cách trực tiếp). Vì $A$ là noetherian, $\mathcal{L}$ là sinh hữu hạn (finitely generated), và cho ${a_{1}, \dots  , a_{n}}$ là tập hợp của các phần tử sinh của $\mathcal{L}$. Cho $f_{1}(X), \dots  , f_{n}(X)$ là các đa thức trong $\mathfrak{A}$ có respectively $a_{1}, \dots  , a_{n}$ như highest bậc số hạng các hệ số. các đa thức này sinh $ideal\mathfrak{B}$. Cho $q$ là cực đại của các bậc của $f_{i}(X)’s$. Bây giờ, chọn bất kỳ đa thức g(X) $\in \mathfrak{A}$ của bậc $d \ge q$, và cho $aX^{d}$ là của nó số hạng của highest bậc. Vì $a \in L$, ta có
$$a = \lambda_{1} a_{1} + \cdots  + \lambda_{n} a_{n},$$
Với một số $\lambda_{i}  \in A$. Xét đa thức
$$g_{1}(X) = \sum_{i=1}^{n}  \lambda_{i} f_{i}(X)X^{d-di},$$
Ở đâu $d_{i}$ là bậc của $f_{i}(X)$. Bây giờ, g(X) - $g_{1}(X)$ là đa thức trong $\mathfrak{A}$ của bậc nhiều nhất $d$ - $1$. Bởi repeating điều này quy trình, ta thu được dãy của các đa thức $g_{i}(X)$ trong $\mathfrak{B}$, có chặt giảm các bậc, và sao cho đa thức
$$g(X) -(g_{1}(X) + \cdots  + g_{i}(X))$$
Là của bậc nhiều nhất $d$ - $i$. đa thức này phải là của bậc nhiều nhất $q$ - $1$ như soon như $i = d$ - $q + 1$. Do đó, ta được chứng minh rằng mọi đa thức trong $\mathfrak{A}$ của bậc $d \ge q$ thuộc đến $\mathfrak{B}$. Nó vẫn còn đến lấy care của các đa thức trong $\mathfrak{A}$ của bậc nhiều nhất $q$ - $1$. Vì $A$ là noetherian, mỗi lý tưởng (ideal) $L_{i}(\mathfrak{A})$ là sinh hữu hạn (finitely generated), và cho ${a_{i1}, \dots  , a_{ini}}$ là tập hợp của các phần tử sinh
