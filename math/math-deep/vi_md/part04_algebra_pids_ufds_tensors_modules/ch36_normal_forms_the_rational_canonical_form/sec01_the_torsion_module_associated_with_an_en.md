# Môđun xoắn (torsion module) Liên kết với Tự đồng cấu


<!-- PAGE 1319 -->
Chương $36$ Dạng chính tắc hữu tỷ (rational canonical form) và Khác Chuẩn tắc/bình thường Các dạng

## 36.1 Môđun xoắn (torsion module) Liên kết với Endo-

$$morphism$$
Ta đã thấy trong Mục 7.7 rằng cho trước ánh xạ tuyến tính (linear map) $f$: $E \to E$ từ vectơ $K$ không gian $E$ vào chính nó, ta có thể định nghĩa vô hướng (scalar) phép nhân $\cdot$: K[X] $\times  E \to E$ rằng làm cho $E$ vào K]X]-môđun. Nếu $E$ là hữu hạn chiều, điều này K[X]-môđun được ký hiệu bởi $E_{f}$ là môđun xoắn (torsion module), và chính các kết quả của điều này chương cho quan trọng tổng trực tiếp (direct sum) các phân rã của $E$ vào các không gian con bất biến dưới $f$. Nhắc lại rằng cho trước bất kỳ đa thức p(X) $= a_{0}X^{n} + a_{1}X^{n-1} + \cdots  + a_{n}$ với các hệ số trong trường $K$, ta định nghĩa ánh xạ tuyến tính (linear map) p(f): $E \to E$ bởi
$$p(f) = a_{0}f^{n}+ a_{1}f^{n-1}+ \cdots  + a_{n}id,$$
Ở đâu $f^{k} = f \circ \cdots  \circ f$, k-fold hợp thành của $f$ với chính nó. Lưu ý rằng
$$p(f)(u) = a_{0}f^{n} (u) + a_{1}f^{n-1} (u) + \cdots  + a_{n}u,$$
Với mọi vectơ $u \in E$. Thì, ta định nghĩa vô hướng (scalar) phép nhân $\cdot$: K[X] $\times  E \to E$ bởi các đa thức như sau: với mọi đa thức p(X) $\in$ K[X], với mọi $u \in E$,
$$p(X) \cdot  u = p(f)(u).^{1}$$
Nó là dễ để kiểm chứng rằng điều này vô hướng (scalar) phép nhân thỏa mãn axioms M1, M2, M3, M4:
$$p \cdot  (u + v) = p \cdot  u + p \cdot  v$$
$$(p + q) \cdot  u = p \cdot  u + q \cdot  u$$
$$(pq) \cdot  u = p \cdot  (q \cdot  u)$$
$$1 \cdot  u = u,$$
$\overline{1}\overline{If} \overline{necessary} \overline{to} \overline{avoid} \overline{confusion,} \overline{we} \overline{use}$ khái niệm p(X) $\cdot_{f}  u$ thay vì của p(X) $\cdot  u$.
$$1319$$

<!-- PAGE 1320 -->
Với mọi $p, q \in$ K[X] và tất cả $u, v \in E$. Do đó, với điều này mới vô hướng (scalar) phép nhân, $E$ là K[X]-môđun được ký hiệu bởi $E_{f}$. Nếu $p = \lambda$ là chỉ vô hướng (scalar) trong $K$ (đa thức của bậc $0)$, thì
$$\lambda  \cdot  u = (\lambda id)(u) = \lambda u,$$
Mà có nghĩa là $K$ acts trên $E$ bởi vô hướng (scalar) phép nhân như trước. Nếu p(X) $= X$ (đơn thức $X)$, thì
$$X \cdot  u = f(u).$$
Vì $K$ là trường, vành K[X] là PID. Nếu $E$ là hữu hạn chiều, nói có số chiều $n$, vì $K$ là vành con của K[X] và vì $E$ là sinh hữu hạn (finitely generated) trên $K$, K[X]-môđun $E_{f}$ là sinh hữu hạn (finitely generated) trên K[X]. Hơn nữa, $E_{f}$ là môđun xoắn (torsion module). Điều này suy ra từ Cayley-Hamilton Định lý (Định lý 7.15), nhưng điều này có thể cũng được hiển thị trong sơ cấp cách thức như sau. không gian Hom(E, $E)$ của các ánh xạ tuyến tính (linear maps) của $E$ vào chính nó là không gian vectơ (vector space) có số chiều $n^{2}$, vì vậy $n^{2}+1$ các ánh xạ tuyến tính (linear maps)
$$id, f, f^{2} , \dots  , f^{n2}$$
Là phụ thuộc tuyến tính (linearly dependent), mà cho ta khác không đa thức $q$ sao cho q(f) $= 0$. Ta có thể bây giờ translate các khái niệm được định nghĩa cho các môđun vào các khái niệm cho các tự đồng cấu của các không gian vectơ. $1$. Đến nói rằng $U$ là môđun con của $E_{f}$ có nghĩa là $U$ là không gian con của $E$ bất biến dưới $f$; nghĩa là, f(U) $\subseteq U. 2$. Đến nói rằng $V$ là xích (cyclic) môđun con của $E_{f}$ có nghĩa là tồn tại một vectơ $u \in V$, sao cho $V$ được sinh (spanned) bởi $(u$, f(u), $\dots  , f^{k} (u), \dots$). Nếu $E$ có hữu hạn số chiều $n$, thì $V$ được sinh (spanned) bởi $(u$, f(u), $\dots  , f^{k} (u))$ với một số $k \le n -1$. Ta nói rằng $V$ là xích (cyclic) không gian con cho $f$ với phần tử sinh $u$. Đôi khi, $V$ được ký hiệu bởi Z(u; $f). 3$. Đến nói rằng lý tưởng (ideal) $\mathfrak{a} =$ (p(X)) (với p(X) chuẩn hóa (monic) đa thức) là linh hóa tử (annihilator) của môđun con $V$ có nghĩa là p(f)(u) $= 0$ với mọi $u \in V$, và ta gọi $p$ đa thức tối tiểu (minimal polynomial) của $V$. $4$. Giả sử $E_{f}$ là xích (cyclic) và cho $\mathfrak{a} = (q)$ là của nó linh hóa tử (annihilator), ở đâu
$$q(X) = X^{n}+ a_{n-1}X^{n-1}+ \cdots  + a_{1}X + a_{0}.$$
Thì, tồn tại một vectơ $u$ sao cho $(u$, f(u), $\dots  , f^{k} (u))$ sinh (span) $E_{f}$, và bởi vì $q$ là đa thức tối tiểu (minimal polynomial) của $E_{f}$, ta phải có $k =$ n-1. sự kiện rằng q(f) $= 0$ suy ra rằng
$$f^{n} (u) = -a_{0}u -a_{1}f(u) -\cdots  -a_{n-1}f^{n-1} (u),$$

<!-- PAGE 1321 -->
Và do đó $f$ được biểu diễn bởi sau đây ma trận đã biết như companion ma trận của q(X):
$$U = \begin{pmatrix} 0 & 0 & 0 & \cdots & 0 & -a_{0} \\ 1 & 0 & 0 & \cdots & 0 & -a_{1} \\ 0 & 1 & 0 & \cdots & 0 & -a_{2} \\ \vdots & \ddots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \ddots & 0 & -a_{n-2} \\ 0 & 0 & 0 & 1 & a_{n-1} \end{pmatrix} .$$
$$\cdots -$$
Nó là dễ bài tập để chứng minh rằng đa thức đặc trưng (characteristic polynomial) $\chi_{U} (X)$ của $U$ cho quay lại q(X):
$$\chi_{U} (X) = q(X).$$
Ta sẽ cần sau đây mệnh đề để đặc trưng hóa khi hai các ánh xạ tuyến tính (linear maps) là đồng dạng.

> **Mệnh đề 36.1.** Cho $f$: $E \to E$ và f': E' $\to$ E' là hai các ánh xạ tuyến tính (linear maps) trên các không gian vectơ $E$ và E'. ánh xạ tuyến tính (linear map) $g: E \to$ E' có thể được được quan điểm như ánh xạ tuyến tính (linear map) giữa K[X]-các môđun $E_{f}$ và $E_{f'}$ khi và chỉ khi
$$g \circ f = f'\circ g.$$

*Chứng minh.* Thứ nhất, giả sử $g$ là K[X]-tuyến tính. Thì, ta có
$$g(p \cdot_{f}  u) = p \cdot_{f'}  g(u)$$
Với mọi $p \in$ K[X] và tất cả $u \in E$, do đó cho $p = X$ ta thu được
$$g(p \cdot_{f}  u) = g(X \cdot_{f}  u) = g(f(u))$$
Và
$$p \cdot_{f'}  g(u) = X \cdot_{f'}  g(u) = f' (g(u)),$$
Mà có nghĩa là $g \circ f =$ f' $\circ g$. Ngược lại, nếu $g \circ f =$ f' $\circ g$, ta chứng minh bởi quy nạp rằng
$$g \circ f^{n}= f^{'n}\circ g,for all n \ge 1.$$
Thật vậy, ta có
$$g \circ f^{n+1}= g \circ f^{n}\circ f$$
$$= f^{'n}\circ g \circ f$$
$$= f^{'n}\circ f'\circ g$$
$$= f^{'n+1}\circ g,$$

<!-- PAGE 1322 -->
$$establishing the induction step. It follows that for any polynomial p(X) = \sum_{k}  n=0 a_{k}X^{k}, we$$
Có
$$g(p(X) \cdot_{f}  u) = g \begin{pmatrix} a_{k}f^{k}(u) \end{pmatrix} \sum_{k=0}^{n}$$
$$= \sum_{k=0}^{n}  a_{k}g \circ f^{k} (u)$$
$$= \sum_{k=0}^{n}  a_{k}f^{'k}\circ g(u)$$
$$= \begin{pmatrix} a_{k}f^{'k} \end{pmatrix} \sum_{k=0}^{n}  (g(u))$$
$$= p(X) \cdot_{f'}  g(u),$$
Do đó, $g$ là thật vậy K[X]-tuyến tính.

> **Định nghĩa 36.1.** Ta nói rằng các ánh xạ tuyến tính (linear maps) $f$: $E \to E$ và f': E' $\to$ E' là đồng dạng khi và chỉ khi có một đẳng cấu $g: E \to$ E' sao cho
$$f'= g \circ f \circ g^{-1},$$
Hoặc tương đương,
$$g \circ f = f'\circ g.$$
Thì, Mệnh đề 36.1 chỉ ra sau đây sự kiện:

> **Mệnh đề 36.2.** Với ký hiệu của Mệnh đề 36.1, hai các ánh xạ tuyến tính (linear maps) $f$ và f' là đồng dạng khi và chỉ khi $g$ là đẳng cấu giữa $E_{f}$ và $E_{f'}'$. Sau này, ta sẽ xem rằng đẳng cấu của sinh hữu hạn (finitely generated) xoắn (torsion) các môđun có thể được được đặc trưng hóa theo các nhân tử bất biến (invariant factors), và điều này sẽ là translated vào đặc trưng của sự đồng dạng của các ánh xạ tuyến tính (linear maps) theo so-called sự đồng dạng các bất biến. Nếu $f$ và f' được biểu diễn bởi các ma trận $A$ và ' trên các cơ sở của $E$ và E', thì $f$ và f' là đồng dạng khi và chỉ khi các ma trận $A$ và ' là đồng dạng (có một ma trận khả nghịch (invertible matrix) $P$ sao cho ' $= PAP^{-1})$. Đồng dạng các ma trận (và các tự đồng cấu) có cùng đa thức đặc trưng (characteristic polynomial). Hóa ra là có một hữu ích relationship giữa $E_{f}$ và môđun K[X] $\otimes_{K}  E$. Nhận thấy rằng ánh xạ $\cdot$: K[X] $\times  E \to E$ cho trước bởi
$$p \cdot  u = p(f)(u)$$
Là K-bilinear, do đó nó cho ta $K$-tuyến tính ánh xạ $\sigma$: K[X] $\otimes_{K}  E \to E$ sao cho
$$\sigma (p \otimes u) = p \cdot  u = p(f)(u).$$

<!-- PAGE 1323 -->
Ta biết từ Mục 35.6 rằng K[X] $\otimes_{K}  E$ là K[X]-môđun (thu được từ inclusion $K \subseteq$ K[X]), mà ta sẽ ký hiệu bởi E[X]. Vì $E$ là không gian vectơ (vector space), E[X] là tự do K[X]-môđun, và nếu $(u_{1}, \dots  , u_{n})$ là cơ sở (basis) của $E$, thì $(1 \otimes u_{1}, \dots  , 1 \otimes u_{n})$ là cơ sở (basis) của E[X]. tự do K[X]-môđun E[X] là không như phức tạp như nó trông. Trên cơ sở (basis) $(1 \otimes u_{1}, \dots  , 1 \otimes u_{n})$, mọi phần tử $z \in$ E[X] có thể được được viết một cách duy nhất như
$$z = p_{1}(1 \otimes u_{1}) + \cdots  + p_{n}(1 \otimes u_{n}) = p_{1} \otimes u_{1} + \cdots  + p_{n} \otimes u_{n},$$
Ở đâu $p_{1}, \dots  , p_{n}$ là các đa thức trong K[X]. Cho notational simplicity, ta có thể viết
$$z = p_{1}u_{1} + \cdots  + p_{n}u_{n},$$
Ở đâu $p_{1}, \dots  , p_{n}$ được quan điểm như các hệ số trong K[X]. Với điều này ký hiệu, ta xem rằng E[X] là đẳng cấu đến $(K[X])^{n}$, mà là dễ đến understand. Nhận thấy rằng $\sigma$ là K[X]-tuyến tính, bởi vì
$$\sigma (q(p \otimes u)) = \sigma ((qp) \otimes u)$$
$$= (qp) \cdot  u$$
$$= q(f)(p(f)(u))$$
$$= q \cdot  (p(f)(u))$$
$$= q \cdot  \sigma (p \otimes u).$$
Vì vậy, $\sigma$ là ánh xạ tuyến tính (linear map) của K[X]-các môđun, $\sigma$: E[X] $\to E_{f}$. Bằng cách sử dụng của ta được đơn giản hóa ký hiệu, nếu $z = p_{1}u_{1} + \cdots  + p_{n}u_{n} \in$ E[X], thì
$$\sigma (z) = p_{1}(f)(u_{1}) + \cdots  + p_{n}(f)(u_{n}),$$
Mà tương đương với đến plugging $f$ cho $X$ và evaluating. Tương tự, $f$ là K[X]-ánh xạ tuyến tính (linear map) của $E_{f}$, bởi vì
$$f(p \cdot  u) = f(p(f)(u))$$
$$= (fp(f))(u)$$
$$= p(f)(f(u))$$
$$= p \cdot  f(u),$$
Ở đâu ta được sử dụng sự kiện rằng fp(f) $=$ p(f)f bởi vì p(f) là đa thức trong $f$. Theo Mệnh đề 35.40, ánh xạ tuyến tính (linear map) $f$: $E \to E$ cảm sinh K[X]-ánh xạ tuyến tính (linear map) $\overline{f}\overline{:}$ E[X] $\to$ E[X] sao cho
$$\overline{f}(p \otimes u) = p \otimes f(u).$$
Nhận thấy rằng ta có
$$f(\sigma (p \otimes u)) = f(p(f)(u)) = p(f)(f(u))$$

<!-- PAGE 1324 -->
Và
$$\sigma (\overline{f}(p \otimes u)) = \sigma (p \otimes f(u)) = p(f)(f(u)),$$
Do đó ta thu được
$$\sigma  \circ \overline{f} = f \circ \sigma .(*)$$
Bằng cách sử dụng của ta được đơn giản hóa ký hiệu,
$$\overline{f}(p_{1}u_{1} + \cdots  + p_{n}u_{n}) = p_{1}f(u_{1}) + \cdots  + p_{n}f(u_{n}).$$
Định nghĩa K[X]-ánh xạ tuyến tính (linear map) $\psi$: E[X] $\to$ E[X] bởi
$$\psi (p \otimes u) = (Xp) \otimes u -p \otimes f(u).$$
Nhận thấy rằng $\psi  = X1_{E[X]} -\overline{f}$, mà ta abbreviate như $X1-\overline{f}$. Bằng cách sử dụng của ta được đơn giản hóa ký hiệu
$$\psi (p_{1}u_{1} + \cdots  + p_{n}u_{n}) = Xp_{1}u_{1} + \cdots  + Xp_{n}u_{n} -(p_{1}f(u_{1}) + \cdots  + p_{n}f(u_{n})).$$
Nó nên được lưu ý rằng everything ta đã thực hiện trong Mục 36.1 áp dụng đến các môđun trên vành giao hoán (commutative ring) $A$, ngoại trừ cho các phát biểu rằng giả sử rằng [X] là PID. Do đó, nếu $M$ là A-module, ta có thể định nghĩa [X]-các môđun $M_{f}$ và M[X] $=$ [X] $\otimes_{A}  M$, ngoại trừ rằng $M_{f}$ là một cách tổng quát không môđun xoắn (torsion module), và tất cả các kết quả đã chỉ ra ở trên đúng. Thì, ta có kết quả sau đáng chú ý kết quả.

> **Định lý 36.3.** (Characteristic Dãy) Cho $A$ là vành và cho $E$ là A-module. sau đây dãy của [X]-các ánh xạ tuyến tính (linear maps) là chính xác:
$$E/\psi  E/\sigma  E_{f}/ 0/$$
$$0[X][X].$$
Điều này có nghĩa là $\psi$ là đơn ánh (injective), $\sigma$ là toàn ánh (surjective), và rằng $Im(\psi$) $=$ Ker $(\sigma$). Hệ quả là, $E_{f}$ là đẳng cấu đến thương của E[X] bởi Im(X1 - $\overline{f})$.

*Chứng minh.* Bởi vì $\sigma (1 \otimes u) = u$ với mọi $u \in E$, ánh xạ $\sigma$ là toàn ánh (surjective). Ta có
$$\sigma (X(p \otimes u)) = X \cdot  \sigma (p \otimes u)$$
$$= f(\sigma (p \otimes u)),$$
Mà chỉ ra rằng
$$\sigma  \circ X1 = f \circ \sigma  = \sigma  \circ \overline{f,}$$
Bằng cách sử dụng (*). Điều này suy ra rằng
$$\sigma  \circ \psi  = \sigma  \circ (X1 -\overline{f})$$
$$= \sigma  \circ X1 -\sigma  \circ \overline{f}$$
$$= \sigma  \circ \overline{f} -\sigma  \circ \overline{f} = 0,$$

<!-- PAGE 1325 -->
Và do đó, $Im(\psi$) $\subseteq$ Ker $(\sigma$). Nó vẫn còn để chứng minh rằng Ker $(\sigma$) $\subseteq Im(\psi$). Vì các đơn thức $X^{k}$ tạo thành cơ sở (basis) của [X], theo Mệnh đề 35.13 (với các vai trò của $M$ và $N$ exchanged), mọi $z \in$ E[X] $=$ [X] $\otimes_{A}  E$ có duy nhất biểu thức như
$$z = \sum_{k}  X^{k}\otimes u_{k},$$
Cho họ $(u_{k})$ của hữu hạn hỗ trợ/giá (support) của $u_{k} \in E$. Nếu $z \in$ Ker $(\sigma$), thì
$$0 = \sigma (z) = \sum_{k}  f^{k} (u_{k}),$$
Mà cho phép chúng ta đến viết
$$z = \sum_{k}  X^{k}\otimes u_{k} -1 \otimes 0$$
$$= \sum_{k}  X^{k} \otimes u_{k} -1 \otimes \begin{pmatrix} f^{k}(u_{k}) \end{pmatrix} \sum_{k}$$
$$= \sum_{k}  (X^{k}\otimes u_{k} -1 \otimes f^{k}(u_{k}))$$
$$= \sum_{k}  (X^{k}(1 \otimes u_{k}) -\overline{f}^{k}(1 \otimes u_{k}))$$
$$= \sum_{k}  (X^{k}1 -\overline{f}^{k})(1 \otimes u_{k}).$$
Bây giờ, X1 và $\overline{f}$ giao hoán, vì
$$(X1 \circ \overline{f})(p \otimes u) = (X1)(p \otimes f(u))$$
$$= (Xp) \otimes f(u)$$
Và
$$(\overline{f} \circ X1)(p \otimes u) =\overline{f}((Xp) \otimes u)$$
$$= (Xp) \otimes f(u),$$
Do đó ta có thể viết
$$X^{k}1 -\overline{f}^{k}= (X1 -\overline{f}) \begin{pmatrix} (X1)^{j}\overline{f}^{k-j-1} \end{pmatrix} \sum_{j=0}^{k-1}  ,$$
Và
$$z = (X1 -\overline{f}) \begin{pmatrix}  \\ (X1)^{j}\overline{f}^{k-j-1} \end{pmatrix} \sum_{k}  \begin{pmatrix} (1 \otimes u_{k}) \end{pmatrix} \sum_{j=0}^{k-1}  ,$$

<!-- PAGE 1326 -->
Mà chỉ ra rằng $z = \psi (y)$ với một số $y \in$ E[X]. Cuối cùng, ta chứng minh rằng $\psi$ là đơn ánh (injective) như sau. Ta có
$$\psi (z) = \psi \begin{pmatrix} X^{k}\otimes u_{k} \\  \end{pmatrix} \sum_{k}$$
$$= (X1 -\overline{f}) \begin{pmatrix} X^{k}\otimes u_{k} \end{pmatrix} \sum_{k}$$
$$= \sum_{k}  X^{k+1}\otimes (u_{k} -f(u_{k+1})),$$
Ở đâu $(u_{k})$ là họ của hữu hạn hỗ trợ/giá (support) của $u_{k} \in E$. Nếu $\psi (z) = 0$, thì
$$\sum_{k}  X^{k+1}\otimes (u_{k} -f(u_{k+1})) = 0,$$
Và bởi vì $X^{k}$ tạo thành cơ sở (basis) của [X], ta phải có
$$u_{k} -f(u_{k+1}) = 0,for all k.$$
Vì $(u_{k})$ có hữu hạn hỗ trợ/giá (support), có một lớn nhất $k$, nói $m+1$ sao cho $u_{m+1} = 0$, và thì từ
$$u_{k} = f(u_{k+1}),$$
Ta suy ra rằng $u_{k} = 0$ với mọi $k$. Vì vậy, $z = 0$, và $\psi$ là đơn ánh (injective).
Nhận xét: chính xác dãy của Định lý 36.3 cho ta trình bày của $M_{f}$. Vì [X] là tự do A-module, $A[X]\otimes_{A} M$ là tự do A-module, nhưng $A[X]\otimes_{A} M$ là một cách tổng quát không tự do [X]-môđun. Tuy nhiên, nếu $M$ là môđun tự do (free module), thì M[X] là tự do [X]-môđun, vì nếu $(u_{i})_{i\in I}$ là cơ sở (basis) cho $M$, thì $(1 \otimes u_{i})_{i\in I}$ là cơ sở (basis) cho M[X]. Điều này cho phép chúng ta để định nghĩa characterisctic đa thức $\chi_{f} (X)$ của tự đồng cấu của môđun tự do (free module) $M$ như
$$\chi_{f} (X) = \det(X1 -\overline{f}).$$
Lưu ý rằng đến có đúng định nghĩa, ta cần để định nghĩa định thức (determinant) của ánh xạ tuyến tính (linear map) cho phép indeterminate $X$ như vô hướng (scalar), và điều này là những gì định nghĩa của M[X] đạt được (trong số khác things). Định lý 36.3 có thể được sử dụng để cho ngắn chứng minh của Cayley-Hamilton Định lý, xem Bourbaki $[25]$ (Chương III, Mục $8$, Mệnh đề $20)$. Mệnh đề 7.10 là vẫn then chốt ingredient của chứng minh.
