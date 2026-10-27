# Sinh hữu hạn (finitely generated) Các môđun trên PID


<!-- PAGE 1297 -->

## 35.5 Sinh hữu hạn (finitely generated) Các môđun trên PID; Bất biến

$$Factor Decomposition$$
Có một vài các cách của thu được phân rã của sinh hữu hạn (finitely generated) môđun như tổng trực tiếp (direct sum) của xích (cyclic) các môđun. Một cách đến tiến hành là đến thứ nhất sử dụng Phân rã sơ cấp (primary decomposition) Định lý và thì để chỉ ra cách mà mỗi sơ cấp môđun $M_{p}$ là tổng trực tiếp (direct sum) của xích (cyclic) các môđun của tạo thành $A/(p^{n})$. Điều này là cách tiếp cận theo sau bởi Lang $[113]$ (Chương III, mục $7)$, trong số những cái khác. Ta ưu tiên để sử dụng mệnh đề rằng produces cụ thể cơ sở (basis) cho môđun con của sinh hữu hạn (finitely generated) môđun tự do (free module), bởi vì nó cho ta nhiều hơn/thêm information. Điều này là cách tiếp cận theo sau trong Dummitt và Foote $[55]$ (Chương $12)$ và Bourbaki $[26]$ (Chương VII). chứng minh rằng ta trình bày là do Pierre Samuel.

> **Mệnh đề 35.23.** Cho $F$ là sinh hữu hạn (finitely generated) môđun tự do (free module) trên PID $A$, và cho $M$ là bất kỳ môđun con của $F$. Thì, $M$ là môđun tự do (free module) và có một cơ sở (basis) $(e_{1}$,..., $e_{n})$ của $F$, một số $q \le n$, và một số khác không các phần tử $a_{1}, \dots  , a_{q} \in A$, sao cho $(a_{1}e_{1}, \dots  , a_{q}e_{q})$ là cơ sở (basis) của $M$ và $a_{i}$ chia hết $a_{i+1}$ với mọi $i$, với $1 \le i \le q$ - $1$.

*Chứng minh.* mệnh đề là tầm thường khi $M = {0}$, do đó giả sử rằng $M$ là không tầm thường. Chọn một số cơ sở (basis) $(u_{1}, \dots  , u_{n})$ cho $F$. Cho L(F, $A)$ là tập hợp của các dạng tuyến tính trên $F$. Với mọi $f \in$ L(F, $A)$, ta kiểm chứng được ngay rằng f(M) là lý tưởng (ideal) trong $A$. Do đó, f(M) $= a_{h}A$, với một số $a_{h} \in A$, vì mọi lý tưởng (ideal) trong $A$ là chính lý tưởng (ideal). Vì $A$ là PID, bất kỳ khác rỗng họ của các lý tưởng trong $A$ có cực đại phần tử, do đó cho $f$ là ánh xạ tuyến tính (linear map) sao cho $a_{h}A$ là lý tưởng cực đại (maximal ideal) trong $A$. Cho $\pi_{i}$: $F \to A$ là thứ $i$ phép chiếu, i.e., $\pi_{i}$ được định nghĩa sao cho $\pi_{i} (x_{1}u_{1} + \cdots  + x_{n}u_{n}) = x_{i}$. Rõ ràng là $\pi_{i}$ là ánh xạ tuyến tính (linear map), và vì $M$ là không tầm thường, một của $\pi_{i} (M)$ là không tầm thường, và $a_{h} \neq  0$. Tồn tại một e' $\in M$ sao cho f(e') $= a_{h}$. Ta khẳng định rằng, với mọi $g \in$ L(F, $A)$, phần tử $a_{h} \in A$ chia hết g(e'). Thật vậy, nếu $d$ là ước chung lớn nhất (gcd) của $a_{h}$ và g(e'), bởi B´ezout đồng nhất thức, ta có thể viết
$$d = ra_{h} + sg(e'),$$
Với một số $r, s \in A$, và do đó
$$d = rf(e') + sg(e') = (rf + sg)(e').$$
Tuy nhiên, rf $+$ sg $\in$ L(F, $A)$, và do đó,
$$a_{h}A \subseteq dA \subseteq (rf + sg)(M),$$
Vì $d$ chia hết $a_{h}$, và bởi maximality của $a_{h}A$, ta phải có $a_{h}A =$ dA, mà suy ra rằng $d = a_{h}$, và do đó, $a_{h}$ chia hết g(e'). Đặc biệt, $a_{h}$ chia hết mỗi $\pi_{i}$ (e') và cho $\pi_{i}$ (e') $= a_{h}b_{i}$, với $b_{i} \in A$. Cho $e = b_{1}u_{1} + \cdots  + b_{n}u_{n}$. Lưu ý rằng
$$e'= \pi_{1} (e')u_{1} + \cdots  + \pi_{n} (e')u_{n} = a_{h}b_{1}u_{1} + \cdots  + a_{h}b_{n}u_{n},$$

<!-- PAGE 1298 -->
Và do đó, e' $= a_{h}e$. Vì $a_{h} =$ f(e') $= f(a_{h}e) = a_{h}f(e)$, và vì $a_{h} \neq  0$, ta phải có f(e) $= 1$. Tiếp theo, ta khẳng định rằng
$$F = Ae \oplus f^{-1} (0)$$
Và
$$M = Ae'\oplus (M \cap f^{-1}(0)),$$
Với e' $= a_{h}e$. Thật vậy, mọi $x \in F$ có thể được viết dưới dạng
$$x = f(x)e + (x -f(x)e),$$
Và vì f(e) $= 1$, ta có f(x - f(x)e) $=$ f(x) - f(x)f(e) $=$ f(x) - f(x) $= 0$. Do đó, $F =$ Ae $+ f^{-1} (0)$. Tương tự, với mọi $x \in M$, ta có f(x) $= ra_{h}$, với một số $r \in A$, và do đó,
$$x = f(x)e + (x -f(x)e) = ra_{h}e + (x -f(x)e) = re'+ (x -f(x)e),$$
Ta vẫn có $x$ - f(x)e $\in f^{-1}(0)$, và rõ ràng, $x$ - f(x)e $= x$ - $ra_{h}e = x$ - re' $\in M$, vì e' $\in M$. Do đó, $M =$ Ae' $+ (M \cap f^{-1}(0))$. để chứng minh rằng ta có tổng trực tiếp (direct sum), nó là đủ để chứng minh rằng Ae $\cap f^{-1} (0) = {0}$. Với mọi $x =$ re $\in$ Ae, nếu f(x) $= 0$, thì f(re) $=$ rf(e) $= r = 0$, vì f(e) $= 1$ và, do đó, $x = 0$. Vì vậy, các tổng là các tổng trực tiếp. Ta có thể bây giờ chứng minh rằng $M$ là môđun tự do (free module) bằng quy nạp theo kích thước, $q$, của cực đại độc lập tuyến tính (linearly independent) họ cho $M$. Nếu $q = 0$, kết quả là tầm thường. Ngược lại, vì
$$M = Ae'\oplus (M \cap f^{-1}(0)),$$
Rõ ràng là $M \cap f^{-1} (0)$ là môđun con của $F$ và rằng mọi cực đại độc lập tuyến tính (linearly independent) họ trong $M \cap f^{-1} (0)$ có nhiều nhất $q$ - $1$ các phần tử. Theo giả thiết quy nạp, $M \cap f^{-1} (0)$ là môđun tự do (free module), và bằng cách cộng e' đến cơ sở (basis) của $M \cap f^{-1}(0)$, ta thu được cơ sở (basis) cho $M$, vì tổng là trực tiếp. phần thứ hai được hiển thị bằng quy nạp theo số chiều $n$ của $F$. trường hợp $n = 0$ là tầm thường. Ngược lại, vì
$$F = Ae \oplus f^{-1} (0),$$
Và vì, bởi trước đó lập luận, $f^{-1} (0)$ là cũng tự do, $f^{-1} (0)$ có số chiều $n$ - $1$. Theo giả thiết quy nạp ứng dụng đến của nó môđun con $M \cap f^{-1} (0)$, có một cơ sở (basis) $(e_{2}, \dots  , e_{n})$ của $f^{-1} (0)$, một số $q \le n$, và một số khác không các phần tử $a_{2}, \dots  , a_{q} \in A$, sao cho, $(a_{2}e_{2}, \dots  , a_{q}e_{q})$ là cơ sở (basis) của $M \cap f^{-1} (0)$, và $a_{i}$ chia hết $a_{i+1}$ với mọi $i$, với $2 \le i \le q$ - $1$. Cho $e_{1} = e$, và $a_{1} = a_{h}$, như ở trên. Rõ ràng là $(e_{1}, \dots  , e_{n})$ là cơ sở (basis) của $F$, và rằng rằng $(a_{1}e_{1}, \dots  , a_{q}e_{q})$

<!-- PAGE 1299 -->
Là cơ sở (basis) của $M$, vì các tổng là trực tiếp, và e' $= a_{1}e_{1} = a_{h}e$. Nó vẫn còn để chỉ ra rằng $a_{1}$ chia hết $a_{2}$. Xét ánh xạ tuyến tính (linear map) $g: F \to A$ sao cho $g(e_{1}) = g(e_{2}) = 1$, và $g(e_{i}) = 0$, với mọi $i$, với $3 \le i \le n$. Ta có $a_{h} = a_{1} = g(a_{1}e_{1}) =$ g(e') $\in$ g(M), và do đó $a_{h}A \subseteq$ g(M). Vì $a_{h}A$ là cực đại, ta phải có g(M) $= a_{h}A = a_{1}A$. Vì $a_{2} = g(a_{2}e_{2}) \in$ g(M), ta có $a_{2} \in a_{1}A$, mà chỉ ra rằng $a_{1}$ chia hết $a_{2}$. Ta cần sau đây cơ bản mệnh đề.

> **Mệnh đề 35.24.** Với mọi vành giao hoán (commutative ring) $A$, nếu $F$ là tự do A-module và nếu $(e_{1}, \dots  , e_{n})$ là cơ sở (basis) của $F$, với mọi các phần tử $a_{1}, \dots  , a_{n} \in A$, có một đẳng cấu
$$F/(Aa_{1}e_{1} \oplus \cdots  \oplus Aa_{n}e_{n}) \approx (A/a_{1}A) \oplus \cdots  \oplus (A/a_{n}A).$$

*Chứng minh.* Cho $\sigma$: $F \to A/(a_{1}A) \oplus \cdots  \oplus A/(a_{n}A)$ là ánh xạ tuyến tính (linear map) cho trước bởi
$$\sigma (x_{1}e_{1} + \cdots  + x_{n}e_{n}) = (\overline{x}_{1}\overline{, \dots  , x}_{n}),$$
Ở đâu $\overline{x}_{i}$ là lớp tương đương (equivalence class) của $x_{i}$ trong $A/a_{i}A$. ánh xạ $\sigma$ là rõ ràng toàn ánh (surjective), và hạt nhân (hạt nhân (kernel)) của nó bao gồm của tất cả các vectơ $x_{1}e_{1} + \cdots  + x_{n}e_{n}$ sao cho $x_{i} \in a_{i}A$, cho $i = 1, \dots  , n$, mà có nghĩa là
$$\mathrm{Ker} (\sigma ) = Aa_{1}e_{1} \oplus \cdots  \oplus Aa_{n}e_{n}.$$
Vì $M/Ker (\sigma$) là đẳng cấu đến $Im(\sigma$), ta thu được mong muốn đẳng cấu. Ta có thể bây giờ chứng minh sự tồn tại phần của cấu trúc định lý cho sinh hữu hạn (finitely generated) các môđun trên PID.

> **Định lý 35.25.** Cho $M$ là sinh hữu hạn (finitely generated) không tầm thường A-module, ở đâu $A$ PID. Thì, $M$ là đẳng cấu đến tổng trực tiếp (direct sum) của xích (cyclic) các môđun
$$M \approx A/\mathfrak{a}_{1} \oplus \cdots  \oplus A/\mathfrak{a}_{m},$$
Ở đâu $\mathfrak{a}_{i}$ là thực sự/đúng đắn các lý tưởng của $A$ (có thể không) sao cho
$$\mathfrak{a}_{1} \subseteq \mathfrak{a}_{2} \subseteq \cdots  \subseteq \mathfrak{a}_{m} \neq  A.$$
Chính xác hơn, nếu $\mathfrak{a}_{1} = \cdots  =\mathfrak{a}_{r} = (0)$ và $(0) \neq \mathfrak{a}_{r+1} \subseteq \cdots  \subseteq \mathfrak{a}_{m} \neq  A$, thì
$$M \approx A^{r}\oplus (A/\mathfrak{a}_{r+1} \oplus \cdots  \oplus A/\mathfrak{a}_{m}),$$
Ở đâu $A/\mathfrak{a}_{r+1} \oplus \cdots  \oplus A/\mathfrak{a}_{m}$ là xoắn (torsion) môđun con của $M$. môđun $M$ là tự do khi và chỉ khi $r = m$, và torsion-module khi và chỉ khi $r = 0$. Trong latter trường hợp, linh hóa tử (annihilator) của $M$ là $\mathfrak{a}_{1}$.

<!-- PAGE 1300 -->

*Chứng minh.* Vì $M$ là sinh hữu hạn (finitely generated) và không tầm thường, có một toàn ánh (surjective) đồng cấu $\phi$: $A^{n} \to M$ với một số $n \ge 1$, và $M$ là đẳng cấu đến $A^{n}/Ker (\phi$). Vì Ker $(\phi$) là môđun con của môđun tự do (free module) $A^{n}$, theo Mệnh đề 35.23, Ker $(\phi$) là môđun tự do (free module) và có một cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $A^{n}$ và một số khác không các phần tử $a_{1}, \dots  , a_{q} (q \le n)$ sao cho $(a_{1}e_{1}, \dots  , a_{q}e_{q})$ là cơ sở (basis) của Ker $(\phi$) và $a_{1}$ | $a_{2}$ | $\cdots$ | $a_{q}$. Cho $a_{q+1} = \dots  = a_{n} = 0$. Theo Mệnh đề 35.24, ta có đẳng cấu
$$A^{n}/\mathrm{Ker} (\phi ) \approx A/a_{1}A \oplus \cdots  \oplus A/a_{n}A.$$
Bất cứ khi nào $a_{i}$ là unit, nhân tử $A/a_{i}A = (0)$, do đó ta có thể được ta ra units. Cho $r = n$ - $q$, và cho $s \in \mathbb{N}$ là nhỏ nhất chỉ số sao cho $a_{s+1}$ là không unit. Lưu ý rằng $s = 0$ có nghĩa là có không có units. Cũng, như $M \neq  (0), s < n$. Thì,
$$M \approx A^{n}/\mathrm{Ker} (\phi ) \approx A/a_{s+1}A \oplus \cdots  \oplus A/a_{n}A.$$
Cho $m = r + q$ - $s = n$ - $s$. Thì, ta có dãy
$$a_{s+1}, \dots  , a_{q}, a_{q+1}, \dots  , a_{n},$$
$$|{z}|{z}$$
$$q-sr=n-q$$
Ở đâu $a_{s+1}$ | $a_{s+2}$ | $\cdots$ | $a_{q}$ là khác không và nonunits và $a_{q+1} = \cdots  = a_{n} = 0$, do đó ta định nghĩa $m$ các lý tưởng $\mathfrak{a}_{i}$ như sau:
$$($$
$$(0)if 1 \le i \le r$$
$$\mathfrak{a}_{i} =$$
$$a_{r+q+1-i}Aif r + 1 \le i \le m.$$
Với các phần tử này các định nghĩa, các lý tưởng $\mathfrak{a}_{i}$ là thực sự/đúng đắn các lý tưởng và ta có
$$\mathfrak{a}_{i} \subseteq \mathfrak{a}_{i+1},i = 1, \dots  , m -1.$$
Khi $r = 0$, vì $a_{s+1}$ | $a_{s+2}$ | $\cdots$ | $a_{n}$, rõ ràng là $\mathfrak{a}_{1} = a_{n}A$ là linh hóa tử (annihilator) của $M$. khác các phát biểu của định lý là rõ ràng.

> **Ví dụ 35.1.** Đây là một ví dụ của Định lý 35.25. Cho $M$ là $a\mathbb{Z}-module$ với các phần tử sinh ${e_{1}, e_{2}, e_{3}, e_{4}}$ subject đến các quan hệ $6e_{3} = 0, 2e_{4} = 0$. Thì
$$\sim \mathbb{Z} \oplus \mathbb{Z} \oplus \mathbb{Z}\mathbb{Z} \oplus \mathbb{Z}\mathbb{Z}$$
$$M=/6/2,$$
Ở đâu
$$\mathfrak{a}_{1} = (0),\mathfrak{a}_{2} = (0),\mathfrak{a}_{3} = (6),\mathfrak{a}_{4} = (2).$$

<!-- PAGE 1301 -->
Tự nhiên số $r$ được gọi là tự do hạng (rank) hoặc Betti số của môđun $M$. các phần tử sinh $\alpha_{1} , \dots  , \alpha_{m}$ của các lý tưởng $\mathfrak{a}_{1}, \dots  ,\mathfrak{a}_{m}$ (được định nghĩa sai khác unit) là thường được gọi là các nhân tử bất biến (invariant factors) của $M$ (trong ký hiệu của Định lý 35.25, các phần tử sinh của các lý tưởng $\mathfrak{a}_{1}, \dots  ,\mathfrak{a}_{m}$ được ký hiệu bởi $a_{q}, \dots  , a_{s+1}, s \le q)$. Như các hệ quả của Định lý 35.25, ta thu được một lần nữa sau đây các sự kiện được thiết lập trong Mục 35.1: $1$. sinh hữu hạn (finitely generated) môđun trên PID là tổng trực tiếp (direct sum) của của nó môđun xoắn (torsion module) và môđun tự do (free module). $2$. sinh hữu hạn (finitely generated) không xoắn (torsion-free) môđun trên PID là tự do. Hóa ra là các lý tưởng $\mathfrak{a}_{1} \subseteq \mathfrak{a}_{2} \subseteq \cdots  \subseteq \mathfrak{a}_{m}$ ̸ $= A$ là một cách duy nhất được xác định bởi môđun $M$. Tính duy nhất các chứng minh tìm thấy trong hầu hết các cuốn sách tiến tới là intricate và không rất trực quan. ngắn nhất chứng minh rằng ta là biết của là từ Bourbaki $[26]$ (Chương VII, Mục $4)$, và sử dụng wedge các tích. sau đây preliminary các kết quả là cần thiết.

> **Mệnh đề 35.26.** Nếu $A$ là vành giao hoán (commutative ring) và nếu $\mathfrak{a}_{1}, \dots  ,\mathfrak{a}_{m}$ là các lý tưởng của $A$, thì có một đẳng cấu
$$A/\mathfrak{a}_{1} \otimes \cdots  \otimes A/\mathfrak{a}_{m} \approx A/(\mathfrak{a}_{1} + \cdots  +\mathfrak{a}_{m}).$$
Phác thảo của chứng minh. Ta tiến hành bằng quy nạp theo $m$. Cho $m = 2$, ta định nghĩa ánh xạ $\phi$: $A/\mathfrak{a}_{1} \times  A/\mathfrak{a}_{2} \to A/(\mathfrak{a}_{1} +\mathfrak{a}_{2})$ bởi
$$\phi (\overline{a, b}) = ab(\mathrm{mod} \mathfrak{a}_{1} +\mathfrak{a}_{2}).$$
Nó là xác định tốt (well-defined) bởi vì nếu ' $= a + a_{1}$ và b' $= b + a_{2}$ với $a_{1} \in \mathfrak{a}_{1}$ và $a_{2} \in \mathfrak{a}_{2}$, thì
$$a'b'= (a + a_{1})(b + a_{2}) = ab + ba_{1} + aa_{2} + a_{1}a_{2},$$
Và do đó
$$a'b'\equiv ab(\mathrm{mod} \mathfrak{a}_{1} +\mathfrak{a}_{2}).$$
Nó là cũng rõ ràng rằng ánh xạ này là song tuyến tính, do đó nó cảm sinh ánh xạ tuyến tính (linear map) $\phi$: $A/\mathfrak{a}_{1} \otimes A/\mathfrak{a}_{2} \to A/(\mathfrak{a}_{1} +\mathfrak{a}_{2})$ sao cho $\phi (\overline{a} \otimes \overline{b}) =$ ab (mod $\mathfrak{a}_{1} +\mathfrak{a}_{2})$. Tiếp theo, nhận thấy rằng bất kỳ tùy ý tenxơ
$$\overline{a}_{1} \otimes \overline{b}_{1} + \cdots  +\overline{a}_{n} \otimes \overline{b}_{n}$$
Trong $A/\mathfrak{a}_{1} \otimes A/\mathfrak{a}_{2}$ có thể được được viết lại như
$$\overline{1} \otimes (\overline{a}_{1}\overline{b}_{1} + \cdots  +\overline{a}_{n}\overline{b}_{n}),$$
Mà là của tạo thành $\overline{1} \otimes \overline{s}$, với $s \in A$. Ta có thể sử dụng sự kiện này để chỉ ra rằng $\phi$ là đơn ánh (injective) và toàn ánh (surjective), và do đó đẳng cấu.

<!-- PAGE 1302 -->
Ví dụ, nếu $\phi \overline{(1} \otimes \overline{s}) = 0$, bởi vì $\phi \overline{(1} \otimes \overline{s}) = s$ (mod $\mathfrak{a}_{1} +\mathfrak{a}_{2})$, ta có $s \in \mathfrak{a}_{1} +\mathfrak{a}_{2}$, do đó ta có thể viết $s = a + b$ với $a \in \mathfrak{a}_{1}$ và $b \in \mathfrak{a}_{2}$. Thì
$$\overline{1} \otimes \overline{s}\overline{= 1} \otimes \overline{a}\overline{+}\overline{b}$$
$$\overline{= 1} \otimes (\overline{a} +\overline{b})$$
$$\overline{= 1} \otimes \overline{a}\overline{+ 1} \otimes \overline{b}$$
$$=\overline{a} \otimes \overline{1 + 1} \otimes \overline{b}$$
$$= 0 + 0 = 0,$$
Vì $a \in \mathfrak{a}_{1}$ và $b \in \mathfrak{a}_{2}$, mà chứng minh tính đơn ánh. Nhắc lại rằng đại số ngoài (exterior algebra) của A-module $M$ được định nghĩa bởi
$$k$$
$$^M =M^(M).$$
$$k\ge 0$$

> **Mệnh đề 35.27.** Nếu $A$ là vành giao hoán (commutative ring), thì với mọi $n$ các môđun $M_{i}$, có một đẳng cấu
$$nn$$
$$^(MM_{i}) \approx O^M_{i}.$$
$$i=1i=1$$
Chứng minh có thể được tìm thấy trong Bourbaki $[25]$ (Chương III, Mục $7$, Không có $7$, Mệnh đề $10)$.

> **Mệnh đề 35.28.** Cho $A$ là vành giao hoán (commutative ring) và cho $\mathfrak{a}_{1}, \dots  ,\mathfrak{a}_{n}$ là $n$ các lý tưởng của $A$. Nếu môđun $M$ là tổng trực tiếp (direct sum) của $n$ xích (cyclic) các môđun
$$M = A/\mathfrak{a}_{1} \oplus \cdots  \oplus A/\mathfrak{a}_{n},$$
$$p$$
$$then for every p > 0, the exterior power \bigwedge  M is isomorphic to the direct sum of the modules$$
$A/\mathfrak{a}_{H}$, ở đâu $H$ các miền giá trị (range) trên tất cả các tập con $H \subseteq {1, \dots  , n}$ với $p$ các phần tử, và với
$$\mathfrak{a}_{H} = \sum_{h\in H}  \mathfrak{a}_{h}.$$

*Chứng minh.* Nếu $u_{i}$ là ảnh (image) của $1$ trong $A/\mathfrak{a}_{i}$, thì $A/\mathfrak{a}_{i}$ bằng $Au_{i}$. Theo Mệnh đề 35.27, ta có
$$n$$
$$^M \approx O^(Au_{i}).$$
$$i=1$$
Ta cũng có
$$k$$
$$^(Au_{i}) =M^(Au_{i}) \approx A \oplus Au_{i},$$
$$k\ge 0$$

<!-- PAGE 1303 -->
Vì $au_{i} \wedge bu_{i} = 0$, và suy ra rằng
$$p$$
$$^M \approx M(Au_{k1}) \otimes \cdots  \otimes (Au_{kp}).$$
$$H\subseteq {1,...,n}$$
$$H={k1,...,kp}$$
Tuy nhiên, theo Mệnh đề 35.26, ta có
$$(Au_{k1}) \otimes \cdots  \otimes (Au_{kp}) = A/\mathfrak{a}_{k1} \otimes \cdots  \otimes A/\mathfrak{a}_{kp} \approx A/(\mathfrak{a}_{k1} + \cdots  +\mathfrak{a}_{kp}) = A/\mathfrak{a}_{H}.$$
Vì vậy,
$$p$$
$$^M \approx MA/\mathfrak{a}_{H},$$
$$H\subseteq {1,...,n}$$
$$|H|=p$$
Như đã khẳng định. Ví dụ 35.1 continued: Nhắc lại rằng $M$ là $\mathbb{Z}-module$ được sinh bởi ${e_{1}, e_{2}, e_{3}, e_{4}}$ subject đến $6e_{3} = 0, 2e_{2} = 0$. Thì
$$1$$
$$^M = span{e_{1}, e_{2}, e_{3}, e_{4}}$$
$$2$$
$$^M = span{e_{1} \wedge e_{2}, e_{1} \wedge e_{3}, e_{1} \wedge e_{4}, e_{2} \wedge e_{3}, e_{2} \wedge e_{4}, e_{3} \wedge e_{4}}$$
$$3$$
$$^M = span{e_{1} \wedge e_{2} \wedge e_{3}, e_{1} \wedge e_{2} \wedge e_{4}, e_{1} \wedge e_{3} \wedge e_{4}, e_{2} \wedge e_{3} \wedge e_{4}}$$
$$3$$
$$^M = span{e_{1} \wedge e_{2} \wedge e_{3} \wedge e_{4}}.$$
Vì $6e_{3} = 0$, mỗi phần tử của ${e_{1} \wedge e_{3}, e_{2} \wedge e_{3}, e_{1} \wedge e_{2} \wedge e_{3}}$ là annihilated bởi $6\mathbb{Z} = (6)$. Vì $2e_{4} = 0$, mỗi phần tử của ${e_{1}\wedge e_{4}, e_{2}\wedge e_{4}, e_{3}\wedge e_{4}, e_{1}\wedge e_{2}\wedge e_{4}, e_{1}\wedge e_{3}\wedge e_{4}, e_{2}\wedge e_{3}\wedge e_{4}, e_{1}\wedge e_{2}\wedge e_{3}\wedge e_{4}}$ là annihilated bởi $2\mathbb{Z} = (2)$. Ta có được hiển thị rằng
$$\sim \mathbb{Z} \oplus \mathbb{Z} \oplus \mathbb{Z} \oplus \mathbb{Z}$$
$$M=/(6)/(2),$$
Ở đâu $\mathfrak{a}_{1} = (0) =\mathfrak{a}_{2}, \mathfrak{a}_{3} =$ (6),và $\mathfrak{a}_{4} = (2)$. Thì Mệnh đề 35.28 suy ra rằng $1 ^  \sim \mathbb{Z} \mathfrak{a}_{1} \oplus \mathbb{Z} \mathfrak{a}_{2} \oplus \mathbb{Z} \mathfrak{a}_{3} \oplus \mathbb{Z} \mathfrak{a}_{4} \mathbb{Z} \oplus \mathbb{Z} \oplus \mathbb{Z}  \oplus \mathbb{Z}$
$$M=//// =/(6)/(2)$$
$2 ^  \sim \mathbb{Z} \mathfrak{a}_{1} \mathfrak{a}_{2}  \oplus \mathbb{Z} \mathfrak{a}_{1} \mathfrak{a}_{3}  \oplus \mathbb{Z} \mathfrak{a}_{1} \mathfrak{a}_{4}  \oplus \mathbb{Z} \mathfrak{a}_{2} \mathfrak{a}_{3}  \oplus \mathbb{Z} \mathfrak{a}_{2} \mathfrak{a}_{3}$
$$M=/( +)/( +)/( +)/( +)/( +)$$
$$\oplus \mathbb{Z}/(\mathfrak{a}_{3} +\mathfrak{a}_{4}) =\mathbb{Z} \oplus \mathbb{Z}/(6) \oplus \mathbb{Z}/(2) \oplus \mathbb{Z}/(6) \oplus \mathbb{Z}/(2) \oplus \mathbb{Z}/(2)$$
$3 ^  \sim \mathbb{Z} \mathfrak{a}_{1} \mathfrak{a}_{2} \mathfrak{a}_{3}  \oplus \mathbb{Z} \mathfrak{a}_{1} \mathfrak{a}_{2} \mathfrak{a}_{4}  \oplus \mathbb{Z} \mathfrak{a}_{1} \mathfrak{a}_{3} \mathfrak{a}_{4}  \oplus \mathbb{Z} \mathfrak{a}_{1} \mathfrak{a}_{3} \mathfrak{a}_{4}$
$$M=/( + +)/( + +)/( + +)/( + +)$$
$$=\mathbb{Z}/(6) \oplus \mathbb{Z}/(2) \oplus \mathbb{Z}/(2) \oplus \mathbb{Z}(2)$$
$4 ^  \sim \mathbb{Z} \mathfrak{a}_{1} \mathfrak{a}_{2} \mathfrak{a}_{3} \mathfrak{a}_{4} \mathbb{Z}$
$$M=/( + + +) =/(2).$$

<!-- PAGE 1304 -->
Khi các lý tưởng $\mathfrak{a}_{i}$ tạo thành dây chuyền/xích của inclusions $\mathfrak{a}_{1} \subseteq \cdots  \subseteq \mathfrak{a}_{n}$, ta thu được sau đây đáng chú ý kết quả.

> **Mệnh đề 35.29.** Cho $A$ là vành giao hoán (commutative ring) và cho $\mathfrak{a}_{1}, \dots  ,\mathfrak{a}_{n}$ là $n$ các lý tưởng của $A$ sao cho $\mathfrak{a}_{1} \subseteq \mathfrak{a}_{2} \subseteq \cdots  \subseteq \mathfrak{a}_{n}$. Nếu môđun $M$ là tổng trực tiếp (direct sum) của $n$ xích (cyclic) các môđun
$$M = A/\mathfrak{a}_{1} \oplus \cdots  \oplus A/\mathfrak{a}_{n},$$
$$p$$
$$then for every p withp  1 \le p \le n, the ideal \mathfrak{a}_{p} is the annihilatorp  of the exterior power \bigwedge  M.$$
$$If \mathfrak{a}_{n} \neq  A, then \bigwedge  M \neq  (0) for p = 1, \dots  , n, and \bigwedge  M = (0) for p > n.$$

*Chứng minh.* Với ký hiệu của Mệnh đề 35.28, ta có $\mathfrak{a}_{H} =\mathfrak{a}_{max(H)}$, ở đâu max(H) là lớn nhất phần tử trong tập hợp $H$. Vì max(H) $\ge p$ với mọi tập con với $p$ các phần tử và vì max(H) $= p$ khi $H = {1, \dots  , p}$, ta xem rằng
$$\mathfrak{a}_{p} = \bigcap_{\subseteq {1,...,n}  \mathfrak{a}_{H}.$$
$$H}$$
$$|H|=p$$
Theo Mệnh đề 35.28, ta có
$$p$$
$$^M \approx MA/\mathfrak{a}_{H}$$
$$H\subseteq {1,...,n}$$
$$|H|=p$$
$$p$$
$$which proves that \mathfrak{a}_{p} is indeed the annihilator of \bigwedge  M. The rest is clear.$$
Ví dụ 35.1 continued: Nhắc lại rằng $M$ là $\mathbb{Z}-module$ được sinh bởi ${e_{1}, e_{2}, e_{3}, e_{4}}$ subject đến $6e_{3} = 0, 2e_{2} = 0$. Thì
$$1$$
$$^M = span{e_{1}, e_{2}, e_{3}, e_{4}}$$
$$2$$
$$^M = span{e_{1} \wedge e_{2}, e_{1} \wedge e_{3}, e_{1} \wedge e_{4}, e_{2} \wedge e_{3}, e_{2} \wedge e_{4}, e_{3} \wedge e_{4}}$$
$$3$$
$$^M = span{e_{1} \wedge e_{2} \wedge e_{3}, e_{1} \wedge e_{2} \wedge e_{4}, e_{1} \wedge e_{3} \wedge e_{4}, e_{2} \wedge e_{3} \wedge e_{4}}$$
$$3$$
$$^M = span{e_{1} \wedge e_{2} \wedge e_{3} \wedge e_{4}}.$$
Vì $e_{1}$ và $e_{2}$ là tự do, $e_{1} \wedge e_{2}$ là cũng tự do. Vì $6e_{3} = 0$, mỗi phần tử của ${e_{1} \wedge e_{3}, e_{2} \wedge e_{3}, e_{1} \wedge e_{2} \wedge e_{3}}$ là annihilated bởi $6\mathbb{Z} = (6)$. Vì $2e_{4} = 0$, mỗi phần tử của ${e_{1} \wedge e_{4}, e_{2} \wedge e_{4}, e_{3} \wedge e_{4}, e_{1} \wedge e_{2} \wedge e_{4}, e_{1} \wedge e_{3} \wedge e_{4}, e_{2} \wedge e_{3} \wedge e_{4}, e_{1} \wedge e_{2} \wedge e_{3} \wedge e_{4}}$ là annihilated bởi $2\mathbb{Z} = (2)$.

<!-- PAGE 1305 -->
Thì
$$1$$
$$Ann(^M) = Ann e_{1} = (0)$$
$$2$$
$$Ann(^M) = Ann e_{1} \wedge e_{2} = (0)$$
$$3$$
$$Ann(^M) = Ann e_{1} \wedge e_{2} \wedge e_{3} = (6)$$
$$4$$
$$Ann(^M) = Ann e_{1} \wedge e_{2} \wedge e_{3} \wedge e_{4} = (2),$$
Và Mệnh đề 35.29 cung cấp một cái khác verification của
$$\sim \mathbb{Z} \oplus \mathbb{Z} \oplus \mathbb{Z} \oplus \mathbb{Z}$$
$$M=/(6)/(2).$$
Propostion 35.29 ngay lập tức suy ra sau đây then chốt sự kiện.

> **Mệnh đề 35.30.** Cho $A$ là vành giao hoán (commutative ring) và cho $\mathfrak{a}_{1}, \dots  ,\mathfrak{a}_{m}$ là $m$ các lý tưởng của $A$ và $\mathfrak{a}_{1}', \dots  ,\mathfrak{a}_{n}'$ là $n$ các lý tưởng của $A$ sao cho $\mathfrak{a}_{1} \subseteq \mathfrak{a}_{2} \subseteq \cdots  \subseteq \mathfrak{a}_{m} \neq  A$ và $\mathfrak{a}_{1}' \subseteq \mathfrak{a}_{2}' \subseteq \cdots  \subseteq \mathfrak{a}_{n}'$ ̸ $= A$ Nếu ta có đẳng cấu
$$A/\mathfrak{a}_{1} \oplus \cdots  \oplus A/\mathfrak{a}_{m} \approx A/\mathfrak{a}_{1}' \oplus \cdots  \oplus A/\mathfrak{a}_{n}',$$
Thì $m = n$ và $\mathfrak{a}_{i} =\mathfrak{a}_{i}'$ cho $i = 1, \dots  , n$. Mệnh đề 35.30 cho ta tính duy nhất của phân rã trong Định lý 35.25.

> **Định lý 35.31.** (Các nhân tử bất biến (invariant factors) Phân rã) Cho $M$ là sinh hữu hạn (finitely generated) không tầm thường A-module, ở đâu $A$ PID. Thì, $M$ là đẳng cấu đến tổng trực tiếp (direct sum) của xích (cyclic) các môđun
$$M \approx A/\mathfrak{a}_{1} \oplus \cdots  \oplus A/\mathfrak{a}_{m},$$
Ở đâu $\mathfrak{a}_{i}$ là thực sự/đúng đắn các lý tưởng của $A$ (có thể không) sao cho
$$\mathfrak{a}_{1} \subseteq \mathfrak{a}_{2} \subseteq \cdots  \subseteq \mathfrak{a}_{m} \neq  A.$$
Chính xác hơn, nếu $\mathfrak{a}_{1} = \cdots  =\mathfrak{a}_{r} = (0)$ và $(0) \neq \mathfrak{a}_{r+1} \subseteq \cdots  \subseteq \mathfrak{a}_{m} \neq  A$, thì
$$M \approx A^{r}\oplus (A/\mathfrak{a}_{r+1} \oplus \cdots  \oplus A/\mathfrak{a}_{m}),$$
Ở đâu $A/\mathfrak{a}_{r+1} \oplus \cdots  \oplus A/\mathfrak{a}_{m}$ là xoắn (torsion) môđun con của $M$. môđun $M$ là tự do khi và chỉ khi $r = m$, và torsion-module khi và chỉ khi $r = 0$. Trong latter trường hợp, linh hóa tử (annihilator) của $M$ là $\mathfrak{a}_{1}$. Hơn nữa, số nguyên $r$ và các lý tưởng $\mathfrak{a}_{1} \subseteq \mathfrak{a}_{2} \subseteq \cdots  \subseteq \mathfrak{a}_{m} \neq  A$ là một cách duy nhất được xác định bởi $M$.

*Chứng minh.* Theo Định lý 35.7, vì $M_{tor} = A/\mathfrak{a}_{r+1} \oplus \cdots  \oplus A/\mathfrak{a}_{m}$, ta biết rằng số chiều $r$ của tự do summand chỉ phụ thuộc vào $M$. tính duy nhất của dãy của các lý tưởng suy ra từ Mệnh đề 35.30.

<!-- PAGE 1306 -->
Xét theo tính duy nhất phần của Định lý 35.31, ta tạo sau đây định nghĩa.

> **Định nghĩa 35.12.** Cho trước sinh hữu hạn (finitely generated) môđun $M$ trên PID $A$ như trong Định lý 35.31, các lý tưởng $\mathfrak{a}_{i} = \alpha_{i} A$ được gọi là các nhân tử bất biến (invariant factors) của $M$. các phần tử sinh $\alpha_{i}$ của các lý tưởng này (một cách duy nhất được định nghĩa sai khác unit) cũng được gọi là các nhân tử bất biến (invariant factors) của $M$. Mệnh đề 35.23 có thể được sharpened như sau:

> **Mệnh đề 35.32.** Cho $F$ là sinh hữu hạn (finitely generated) môđun tự do (free module) trên PID $A$, và cho $M$ là bất kỳ môđun con của $F$. Thì, $M$ là môđun tự do (free module) và có một cơ sở (basis) $(e_{1}$,..., $e_{n})$ của $F$, một số $q \le n$, và một số khác không các phần tử $a_{1}, \dots  , a_{q} \in A$, sao cho $(a_{1}e_{1}, \dots  , a_{q}e_{q})$ là cơ sở (basis) của $M$ và $a_{i}$ chia hết $a_{i+1}$ với mọi $i$, với $1 \le i \le q$ - $1$. Hơn nữa, môđun tự do (free module) M' với cơ sở (basis) $(e_{1}, \dots  , e_{q})$ và các lý tưởng $a_{1}A, \dots  , a_{q}A$ là một cách duy nhất được xác định bởi $M$; thương môđun M' $/M$ là môđun xoắn (torsion module) của $F/M$, và ta có đẳng cấu
$$M' /M \approx A/a_{1}A \oplus \cdots  \oplus A/a_{q}A.$$

*Chứng minh.* Vì $a_{i} \neq  0$ cho $i = 1, \dots  , q$, nhận thấy rằng
$$M'= {x \in F | (\exists \beta  \in A, \beta  \neq  0)(\beta x \in M)},$$
Mà chỉ ra rằng $M'/M$ là môđun xoắn (torsion module) của $F/M$. Vì vậy, M' là một cách duy nhất được xác định. Vì
$$M = Aa_{1}e_{1} \oplus \cdots  \oplus Aa_{q}e_{q},$$
Theo Mệnh đề 35.24 ta có đẳng cấu
$$M' /M \approx A/a_{1}A \oplus \cdots  \oplus A/a_{q}A.$$
Bây giờ, nó là khả dĩ/có thể rằng thứ nhất $s$ các phần tử $a_{i}$ là units, trong mà trường hợp $A/a_{i}A = (0)$, do đó ta có thể khử như vậy các nhân tử và ta thu được
$$M' /M \approx A/a_{s+1}A \oplus \cdots  \oplus A/a_{q}A,$$
Với $a_{q}A \subseteq a_{q-1}A \subseteq \cdots  \subseteq a_{s+1}A \neq  A$. Theo Mệnh đề 35.30, $q$ - $s$ và các lý tưởng $a_{j}A$ là một cách duy nhất được xác định cho $j = s + 1, \dots  , q$, và vì $a_{1}A = \cdots  = a_{s}A = A$, $q$ các lý tưởng $a_{i}A$ là một cách duy nhất được xác định. các lý tưởng $a_{1}A, \dots  , a_{q}A$ của Mệnh đề 35.32 được gọi là các nhân tử bất biến (invariant factors) của $M$ đối với $F$. Chúng nên không là confused với các nhân tử bất biến (invariant factors) của môđun $M$. Hóa ra là $a_{1}, \dots  , a_{q}$ có thể cũng được tính theo ước chung lớn nhất (gcd)’s của các định thức con (minor) của nhất định ma trận. Nhắc lại rằng nếu $X$ là một ma trận cỡ $m \times  n$, thì $k \times  k$ định thức con (minor) của $X$ là định thức (determinant) của bất kỳ ma trận cỡ $k\times k$ thu được bởi chọn $k$ các cột của $X$, và thì $k$ các hàng từ các phần tử này $k$ các cột.

<!-- PAGE 1307 -->

> **Mệnh đề 35.33.** Cho $F$ là môđun tự do (free module) của hữu hạn số chiều trên PID, $(u_{1}, \dots  , u_{n})$ là cơ sở (basis) của $F, M$ là môđun con của $F$, và $(x_{1}, \dots  , x_{m})$ là tập hợp của các phần tử sinh của $M$. Nếu $a_{1}A, \dots  , a_{q}A$ là các nhân tử bất biến (invariant factors) của $M$ đối với $F$ như trong Mệnh đề 35.32, thì cho $k = 1, \dots  , q$, tích $a_{1} \cdots  a_{k}$ là ước chung lớn nhất (gcd) của $k \times  k$ các định thức con (minor) của ma trận cỡ $n \times  m$ $X_{U}$ có các cột là các tọa độ của $x_{j}$ trên $u_{i}$.

*Chứng minh.* Mệnh đề 35.23 chỉ ra rằng $M \subseteq a_{1}F$. Hệ quả là, các tọa độ của bất kỳ phần tử của $M$ là các bội của $a_{1}$. Mặt khác, ta biết rằng có một dạng tuyến tính (linear form) $f$ cho mà $a_{1}A$ là lý tưởng cực đại (maximal ideal) và một số e' $\in M$ sao cho f(e') $= a_{1}$. Nếu ta viết e' như tổ hợp tuyến tính (linear combination) của $x_{i}$, ta xem rằng $a_{1}$ thuộc đến lý tưởng (ideal) được sinh (spanned) bởi các tọa độ của $x_{i}$ trên cơ sở (basis) $(u_{1}, \dots  , u_{n})$. Vì các tọa độ này là tất cả các bội của $a_{1}$, suy ra rằng $a_{1}$ là của chúng ước chung lớn nhất (gcd), mà chứng minh trường hợp $k = 1$.
$$k$$
$$For any k \ge 2, consider the exterior power \bigwedge  M.Using the notationk  of the proof$$
$$of Proposition 35.23, the module M has the basis (a_{1}e_{1}, \dots  , a_{q}e_{q}), so \bigwedge  M has a basis$$
Bao gồm của các phần tử của tạo thành
$$a_{i1}e_{i1} \wedge \cdots  \wedge a_{ik}e_{ik} = a_{i1} \cdots  a_{ik} e_{i1} \wedge \cdots  \wedge e_{ik},$$
Với mọi các dãy $(i_{1}, \dots  , i_{k})$ sao cho $1 \le i_{1} < i_{2} < \cdots  < i_{k} \le q$. Tuy nhiên, các vectơ
$$k k k$$
$$e_{i1} \wedge \cdots  \wedge e_{ik} form a basis of \bigwedge  F. Thus, the  map from \bigwedge  M into \bigwedge  F induced  by the$$
$$inclusion M \subseteq F defines an isomorphism of \bigwedge  kM onto the submodule of \bigwedge_{i}  kF having the$$
Các phần tử $a_{i1} \cdots  a_{ik} e_{i1} \wedge \cdots  \wedge e_{ik}$ như cơ sở (basis). Vì $a_{j}$ là bội của cho $i < j$, các tích $a_{i1} \cdots  a_{ik}$ là tất cả các bội của $\delta_{k}  = a_{1} \cdots  a_{k}$, và một của các phần tử này bằng $\delta_{k}$. lập luận được sử dụng cho $k = 1$ chỉ ra rằng $\delta_{k}$ là ước chung lớn nhất (gcd) của tập hợp của các tọa độ của bất kỳ tập sinh (spanning set) của $k M k F k F$
$$\bigwedge  over any basis of \bigwedge_{k}  . If we pick as basis of \bigwedge_{i1}  the wedge products u_{i1} \wedge \cdots  \wedge u_{ik},$$
$$and as generators of \bigwedge  M the wedge products x \wedge \cdots  \wedge x_{ik}, it is easy to see that the$$
Các tọa độ của $x_{i1} \wedge \cdots  \wedge x_{ik}$ là thật vậy các định thức mà là $k \times  k$ các định thức con (minor) của ma trận $X_{U}$. Mệnh đề 35.33 cho ta $a_{1}, \dots  , a_{q}$ (sai khác units) như sau: Thứ nhất, $a_{1}$ là ước chung lớn nhất (gcd) của các phần tử (entries) trong $X_{U}$. Có được tính $a_{1}, \dots  , a_{k}$, cho $b_{k} = a_{1} \cdots  , a_{k}$, tính $b_{k+1} = a_{1} \cdots  a_{k}a_{k+1}$ như ước chung lớn nhất (gcd) của tất cả $(k + 1) \times  (k + 1)$ các định thức con (minor) của $X_{U}$, và thì $a_{k+1}$ là thu được bằng cách chia $b_{k+1}$ bởi $b_{k}$ (nhắc lại rằng PID là miền nguyên (integral domain)). Ta cũng có sau đây thú vị kết quả về các ánh xạ tuyến tính (linear maps) giữa các môđun tự do trên PID.

> **Mệnh đề 35.34.** Cho $A$ là PID, cho $F$ là môđun tự do (free module) có số chiều $n$, F' là môđun tự do (free module) có số chiều $m$, và $f$: $F \to$ F' là ánh xạ tuyến tính (linear map) từ $F$ đến F'. Thì, ở đó tồn tại cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $F$, cơ sở (basis) $(e_{1}', \dots  , e_{m}')$ của F', và một số khác không các phần tử $\alpha_{1} , \dots  \alpha_{r}  \in A$ sao cho
$$($$
$$\alpha_{i} e_{i}'if 1 \le i \le r$$
$$f(e_{i}) =$$
$$0if r + 1 \le i \le n,$$

<!-- PAGE 1308 -->
Và $\alpha_{1}$ | $\alpha_{2}$ | $\cdots$ | $\alpha_{r}$. Hơn nữa, các lý tưởng $\alpha_{1} A, \dots  , \alpha_{r} A$ là các nhân tử bất biến (invariant factors) của f(F) với đối với F'.

*Chứng minh.* Cho $F_{0}$ là hạt nhân (kernel) của $f$. Vì M' $=$ f(F) là môđun con của môđun tự do (free module) F', nó là tự do, và tương tự $F_{0}$ là tự do như môđun con của môđun tự do (free module) $F$ (theo Mệnh đề 35.23). Theo Mệnh đề 35.2, ta có
$$F = F_{0} \oplus F_{1},$$
Ở đâu $F_{1}$ là môđun tự do (free module), và thu hẹp của $f$ đến $F_{1}$ là đẳng cấu lên M' $=$ f(F). Mệnh đề 35.32 ứng dụng đến F' và M' cho ta cơ sở (basis) $(e_{1}', \dots  , e_{m}')$ của F' sao cho $(\alpha_{1} e_{1}', \dots  , \alpha_{r} e_{r}')$ là cơ sở (basis) của M', ở đâu $\alpha_{1} A, \dots  , \alpha_{r} A$ là các nhân tử bất biến (invariant factors) cho M' đối với F'. Vì thu hẹp của $f$ đến $F_{1}$ là và đẳng cấu, có một cơ sở (basis) $(e_{1}, \dots  , e_{r})$ của $F_{1}$ sao cho
$$f(e_{i}) = \alpha_{i} e_{i}',i = 1, \dots  , r.$$
Ta có thể mở rộng cơ sở (cơ sở (basis)) này đến cơ sở (basis) của $F$ bởi chọn cơ sở (basis) của $F_{0}$ (môđun tự do (free module)), mà cho ta mong muốn kết quả. ma trận phiên bản của Mệnh đề 35.34 là sau đây mệnh đề.

> **Mệnh đề 35.35.** Nếu $X$ là một ma trận cỡ $m\times n$ của hạng (rank) $r$ trên PID $A$, thì ở đó tồn tại một số khả nghịch $n \times  n$ ma trận $P$, một số khả nghịch $m \times  m$ ma trận $Q$, và một ma trận cỡ $m \times  n$ $D$ của tạo thành
$$D = \begin{pmatrix} \alpha_{1} & 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & \alpha_{2} & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ \cdots \\ 0 & 0 & \cdots & \alpha_{r} & 0 & \cdots & 0 \\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ \cdots \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$$
$$\cdots \cdots$$
Với một số khác không $\alpha_{i}  \in A$, sao cho
$(1) \alpha_{1}$ | $\alpha_{2}$ | $\cdots$ | $\alpha_{r}$,
$(2) X = QDP^{-1}$, và
$(3)$ $\alpha_{i} s$ là một cách duy nhất được xác định sai khác unit. các lý tưởng $\alpha_{1} A, \dots  , \alpha_{r} A$ được gọi là các nhân tử bất biến (invariant factors) của ma trận $X$. Nhắc lại rằng hai ma trận cỡ $m \times  n$ $X$ và $Y$ là tương đương khi và chỉ khi
$$Y = QXP^{-1} ,$$
Với một số các ma trận khả nghịch, $P$ và $Q$. Thì, Mệnh đề 35.35 suy ra sau đây sự kiện.

<!-- PAGE 1309 -->

> **Mệnh đề 35.36.** hai ma trận cỡ $m \times  n$ $X$ và $Y$ là tương đương khi và chỉ khi chúng có cùng các nhân tử bất biến (invariant factors). Nếu $X$ là ma trận của ánh xạ tuyến tính (linear map) $f$: $F \to$ F' đối với một số cơ sở (basis) $(u_{1}, \dots  , u_{n})$ của $F$ và một số cơ sở (basis) $(u_{1}', \dots  , u_{m}')$ của F', thì các cột của $X$ là các tọa độ của $f(u_{j})$ trên $u_{i}'$, ở đâu $f(u_{j})$ sinh f(F), do đó Mệnh đề 35.33 áp dụng và cho ta kết quả sau đây:

> **Mệnh đề 35.37.** Nếu $X$ là một ma trận cỡ $m \times  n$ hoặc hạng (rank) $r$ trên PID $A$, và nếu $\alpha_{1} A, \dots  , \alpha_{r} A$ là của nó các nhân tử bất biến (invariant factors), thì $\alpha_{1}$ là ước chung lớn nhất (gcd) của các phần tử (entries) trong $X$, và cho $k = 2, \dots  , r$, tích $\alpha_{1}  \cdots  \alpha_{k}$ là ước chung lớn nhất (gcd) của tất cả $k \times  k$ các định thức con (minor) của $X$. Có các thuật toán cho chuyển đổi ma trận $X$ trên PID đến tạo thành $X = QDP^{-1}$ như được mô tả trong Mệnh đề 35.35. Cho Euclidean các miền, điều này có thể được đạt được bằng cách sử dụng sơ cấp hàng và cột các phép toán P(i, $k), E_{i,j;\beta}$, và $E_{i,\lambda}$ được mô tả trong Chương $8$, ở đâu ta đòi hỏi vô hướng (scalar) $\lambda$ được sử dụng trong $E_{i,\lambda}$ là unit. Cho tùy ý PID, một cái khác loại của sơ cấp ma trận (chứa một số $2 \times  2$ ma trận con ngoài đường chéo các phần tử (entries)) là cần thiết. Các phần tử này các quy trình liên quan đến việc tính toán ước chung lớn nhất (gcd)’s và sử dụng Bezout đồng nhất thức đến mimic phép chia. Như vậy các phương pháp được trình bày trong $D$. Serre $[162]$, Jacobson $[101]$, và Van Der Waerden $[185]$, và được phác thảo trong Artin $[7]$. Ta mô tả và justify một vài của các phương pháp này trong Mục 36.5. Mệnh đề 35.32 có sau đây hai các ứng dụng. Thứ nhất, xét một cách hữu hạn được trình bày môđun $M$ trên PID cho trước bởi một số $m \times  n$ ma trận $R$. Theo Mệnh đề 35.35, ma trận $R$ có thể được được chéo hóa như $R = QDP^{-1}$ ở đâu $D$ là ma trận đường chéo (diagonal matrix). Thì, ta xem rằng $M$ có trình bày với $m$ các phần tử sinh và $r$ các quan hệ của tạo thành
$$\alpha_{i} e_{i} = 0,$$
Ở đâu $\alpha_{i}  \neq  0$ và $\alpha_{1}$ | $\alpha_{2}$ | $\cdots$ | $\alpha_{r}$. Cho thứ hai ứng dụng, cho $F$ là môđun tự do (free module) với cơ sở (basis) $(e_{1}, \dots  , e_{n})$, và cho $M$ là môđun con của $F$ được sinh bởi $m$ các vectơ $v_{1}, \dots  , v_{m}$ trong $F$. môđun $M$ có thể được được quan điểm như tập hợp của các tổ hợp tuyến tính của các cột của ma trận cỡ $n\times m$ cũng được ký hiệu $M$ bao gồm của các tọa độ của các vectơ $v_{1}, \dots  , v_{m}$ trên cơ sở (basis) $(e_{1}, \dots  , e_{n})$. Thì theo Mệnh đề 35.35, ma trận $R$ có thể được được chéo hóa như $R = QDP^{-1}$ ở đâu $D$ là ma trận đường chéo (diagonal matrix). các cột của $Q$ tạo thành cơ sở (basis) $(e_{1}', \dots  , e_{n}')$ của $F$, và vì $RP = QD$, khác không các cột của $RP$ tạo thành cơ sở (basis) $(a_{1}e_{1}', \dots  , a_{q}e_{q}')$ của $M$. Khi vành $A$ là Euclidean miền xác định, Định lý 36.18 chỉ ra rằng $P$ và $Q$ là các tích của sơ cấp hàng và cột các phép toán. Đặc biệt, khi $A = \mathbb{Z}$, trong mà các trường hợp của ta $\mathbb{Z}-modules$ là các nhóm Abel, ta có thể tìm $P$ và $Q$ bằng cách sử dụng Euclidean phép chia.
$$\mathbb{Z} \mathbb{Z}^{n}$$
Nếu $A =$, sinh hữu hạn (finitely generated) môđun con $M$ của được gọi là một lattice. Nó là cho trước như tập hợp của tích phân các tổ hợp tuyến tính của hữu hạn tập hợp của tích phân các vectơ.

<!-- PAGE 1310 -->
Đây là một ví dụ được lấy từ Artin $[7]$ (Chương $12$, Mục $4)$. Cho $F$ là tự do $\mathbb{Z}-module \mathbb{Z}^{2}$, và cho $M$ là lattice được sinh bởi các cột của ma trận
$$R = \begin{pmatrix} 2 & -1 \\ 1 & 2 \end{pmatrix} .$$
Các cột $(u_{1}, u_{2})$ của $R$ là độc lập tuyến tính (linearly independent), nhưng chúng là không cơ sở (basis) của $\mathbb{Z}^{2}$. Ví dụ, trong thứ tự để thu được $e_{1}$ như tổ hợp tuyến tính (linear combination) của các cột này, ta sẽ cần để giải hệ phương trình tuyến tính
$$2x -y = 1$$
$$x + 2y = 0.$$
Từ phương trình thứ hai, ta thu được $x =$ -2y, mà cho ta
$$-5y = 1.$$
Nhưng, $y = -1/5$ là không số nguyên. Ta để lại nó như một bài tập để kiểm tra rằng
$$\begin{pmatrix} 1 & 0 \\ -3 & 1 \end{pmatrix} \begin{pmatrix} 2 & -1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 5 \end{pmatrix} ,$$
Mà có nghĩa là
$$\begin{pmatrix} 2 & -1 \\ 1 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 5 \end{pmatrix} \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix} ,$$
Do đó $R = QDP^{-1}$ với
$$Q = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix} ,D = \begin{pmatrix} 1 & 0 \\ 0 & 5 \end{pmatrix} ,P = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} .$$
$$\mathbb{Z}^{2}$$
Mới cơ sở (basis) $(u_{1}', u_{2}')$ cho bao gồm của các cột của $Q$ và mới cơ sở (basis) cho $M$ bao gồm của các cột $(u_{1}', 5u_{2}')$ của $QD$, ở đâu
$$QD = \begin{pmatrix} 1 & 0 \\ 3 & 5 \end{pmatrix} .$$
Picture của lattice và của nó các phần tử sinh $(u_{1}, u_{2})$ và của cùng lattice với mới cơ sở (basis) $(u_{1}', 5u_{2}')$ được hiển thị trong Hình 35.1, ở đâu lattice các điểm là displayed như stars. bất biến nhân tử phân rã của sinh hữu hạn (finitely generated) môđun $M$ trên PID $A$ cho trước theo Định lý 35.31 nói rằng rằng
$$M_{tor} \approx A/\mathfrak{a}_{r+1} \oplus \cdots  \oplus A/\mathfrak{a}_{m},$$
Tổng trực tiếp (direct sum) của xích (cyclic) các môđun, với (0)̸ $= \mathfrak{a}_{r+1} \subseteq \cdots  \subseteq \mathfrak{a}_{m}$ ̸ $= A$. Bằng cách sử dụng Chinese Phần dư Định lý (Định lý 32.16), ta có thể further decompose mỗi môđun $A/\alpha_{i} A$ vào tổng trực tiếp (direct sum) của các môđun của tạo thành $A/p^{n}A$, ở đâu $p$ là nguyên tố trong $A$.

<!-- PAGE 1311 -->
$$**$$
$$****$$
* * * *
$$**$$
$$****$$
$$**$$
$$****$$
* * * *
$$**$$
$$****$$
$$Figure 35.1: Diagonalization applied to a lattice$$

> **Định lý 35.38.** (Các ước sơ cấp (elementary divisors) Phân rã) Cho $M$ là sinh hữu hạn (finitely generated) không tầm thường A-module, ở đâu $A$ PID. Thì, $M$ là đẳng cấu đến tổng trực tiếp (direct sum) $A^{r} \oplus M_{tor}$, ở đâu $A^{r}$ là môđun tự do (free module) và ở đâu môđun xoắn (torsion module) $M_{tor}$ là tổng trực tiếp (direct sum) của xích (cyclic) các môđun của tạo thành $A/p_{i}^{ni,j}$, với một số các nguyên tố $p_{1}, \dots  , p_{t} \in A$ và một số dương các số nguyên $n_{i,j}$, sao cho với mỗi $i = 1, \dots  , t$, có một dãy của các số nguyên
$$1 \le n_{i,1}, \dots  , n_{i,1}< n_{i,2}, \dots  , n_{i,2}< \cdots  < n_{i,si}, \dots  , n_{i,si},$$
$$|{z}|{z}|{z}$$
$$mi,1mi,2mi,si$$
Với $s_{i} \ge 1$, và ở đâu $n_{i,j}$ xảy ra $m_{i,j} \ge 1$ lần, cho $j = 1, \dots  , s_{i}$. Hơn nữa, bất khả quy (irreducible) các phần tử $p_{i}$ và các số nguyên $r, t, n_{i,j}, s_{i}, m_{i,j}$ là một cách duy nhất được xác định.

*Chứng minh.* Theo Định lý 35.31, ta đã biết rằng $M \approx A^{r} \oplus M_{tor}$, ở đâu $r$ là một cách duy nhất được xác định, và ở đâu
$$M_{tor} \approx A/\mathfrak{a}_{r+1} \oplus \cdots  \oplus A/\mathfrak{a}_{m},$$
Tổng trực tiếp (direct sum) của xích (cyclic) các môđun, với $(0) \neq \mathfrak{a}_{r+1} \subseteq \cdots  \subseteq \mathfrak{a}_{m} \neq  A$. Thì, $each\mathfrak{a}_{i}$ là chính lý tưởng (ideal) của tạo thành $\alpha_{i} A$, ở đâu $\alpha_{i}$ ̸ $= 0$ và $\alpha_{i}$ là không unit. Bằng cách sử dụng Chinese Phần dư Định lý (Định lý 32.16), nếu ta nhân tử $\alpha_{i}$ vào nguyên tố các nhân tử như
$$\alpha_{i}  = up_{1}^{k1} \cdots  p_{h}^{kh} ,$$
Với $k_{j} \ge 1$, ta thu được đẳng cấu
$$A/\alpha_{i} A \approx A/p_{1}^{k1} A \oplus \cdots  \oplus A/p_{h}^{kh} A.$$

<!-- PAGE 1312 -->
Điều này suy ra rằng $M_{tor}$ là tổng trực tiếp (direct sum) của các môđun của tạo thành $A/p_{i}^{ni,j}$, với một số các nguyên tố $p_{i} \in A$. để chứng minh tính duy nhất, nhận thấy rằng $p_{i}-primary$ thành phần của $M_{tor}$ là tổng trực tiếp (direct sum)
$$(A/p_{i}^{ni,1}A)^{mi,1}\oplus \cdots  \oplus (A/p_{i}^{ni,si}A)^{mi,si},$$
Và các phần tử này là một cách duy nhất được xác định. Vì $n_{i,1} < \cdots  < n_{i,si}$, ta có
$$p_{i}^{ni,si}A \subseteq \cdots  \subseteq p_{i}^{ni,1}A \neq  A,$$
Mệnh đề 35.30 suy ra rằng bất khả quy (irreducible) các phần tử $p_{i}$ và $n_{i,j}, s_{i}$, và $m_{i,j}$ là duy nhất. Xét theo Định lý 35.38, ta tạo sau đây định nghĩa.

> **Định nghĩa 35.13.** Cho trước sinh hữu hạn (finitely generated) môđun $M$ trên PID $A$ như trong Định lý 35.38, các lý tưởng $p_{i}^{ni,j}A$ được gọi là các ước sơ cấp (elementary divisors) của $M$, và $m_{i,j}$ là của chúng các bội. lý tưởng (ideal) $(0)$ cũng được xét là sơ cấp ước và $r$ là của nó bội (multiplicity).
Nhận xét: Định lý 35.38 chỉ ra cách mà các ước sơ cấp (elementary divisors) là thu được từ các nhân tử bất biến (invariant factors): các ước sơ cấp (elementary divisors) là nguyên tố lũy thừa các nhân tử của các nhân tử bất biến (invariant factors). Ngược lại, ta có thể thu được các nhân tử bất biến (invariant factors) từ các ước sơ cấp (elementary divisors). Ta có thể giả sử rằng $M$ là môđun xoắn (torsion module). Cho
$$m = \max{m_{i,1} + \cdots  + m_{i,si}},$$
$$1\le i\le t$$
Và xây dựng ma trận cỡ $t \times  m$ $C = (c_{ij})$ có hàng thứ $i$ là dãy
$$n_{i,si}, \dots  , n_{i,si}, \dots  , n_{i,2}, \dots  , n_{i,2}, n_{i,1}, \dots  , n_{i,1}, 0, \dots  , 0,$$
$$|{z}|{z}|{z}$$
$$mi,simi,2mi,1$$
Padded với 0’s nếu cần để tạo nó của độ dài $m$. Thì, thứ $j$ bất biến nhân tử là
$$\alpha_{j} A = p_{1}^{c1j} p_{2}^{c2j} \cdots  p_{t}^{ctj} A.$$
Nhận thấy rằng bởi vì cột cuối cùng chứa ít nhất một nguyên tố, $\alpha_{i}$ là không units, và $\alpha_{m}$ | $\alpha_{m-1}$ | $\cdots$ | $\alpha_{1}$, sao cho $\alpha_{1} A \subseteq \cdots  \subseteq \alpha_{m-1} A \subseteq \alpha_{m} A \neq  A$, như mong muốn. Từ tính toán điểm của quan điểm, việc tìm các ước sơ cấp (elementary divisors) là thường một cách thực tế không thể, bởi vì nó đòi hỏi nhân tử. Ví dụ, nếu $A =$ K[X] ở đâu $K$ là trường, chẳng hạn như $K =\mathbb{R}$ hoặc $K =\mathbb{C}$, nhân tử tương đương với đến việc tìm các nghiệm của đa thức, nhưng bởi Galois lý thuyết, nói chung, điều này là không algorithmically doable. Mặt khác, các nhân tử bất biến (invariant factors) có thể được được tính bằng cách sử dụng sơ cấp hàng và cột các phép toán. Nó có thể cũng được hiển thị rằng $A$ và các môđun của tạo thành $A/p^{n}A$ là indecomposable (với $n > 0)$. môđun $M$ được nói là indecomposable nếu $M$ không thể được viết như trực tiếp
