# Các tích tenxơ của Các môđun trên Vành giao hoán (commutative ring)


<!-- PAGE 1288 -->

## 35.3 Các tích tenxơ của Các môđun trên

$$Commutative Ring$$
Nó là khả dĩ/có thể để định nghĩa các tích tenxơ của các môđun trên vành, chỉ như trong Mục 33.2, và các kết quả của điều này mục tiếp tục đến đúng. các kết quả của Mục 33.4 cũng tiếp tục đến đúng vì chúng là based trên phổ dụng ánh xạ tính chất. Tuy nhiên, các kết quả của Mục 33.3 trên các cơ sở một cách tổng quát thất bại, ngoại trừ cho các môđun tự do. Tương tự, các kết quả của Mục 33.5 trên đối ngẫu một cách tổng quát thất bại. Các đại số tenxơ có thể được được định nghĩa cho các môđun, như trong Mục 33.6. Tenxơ đối xứng (symmetric tensor) và thay phiên các tenxơ có thể được được định nghĩa cho các môđun nhưng một lần nữa, các kết quả liên quan đến các cơ sở một cách tổng quát thất bại. Các tích tenxơ của các môđun có một số unexpected các tính chất. Ví dụ, nếu $p$ và $q$ là một cách tương đối nguyên tố các số nguyên, thì
$$\mathbb{Z}/p\mathbb{Z} \otimes_{Z} \mathbb{Z}/q\mathbb{Z} = (0).$$
Điều này là bởi vì, bởi Bezout’s đồng nhất thức, có, $b \in \mathbb{Z}$ sao cho
$$ap + bq = 1,$$
Do đó, với mọi $x \in \mathbb{Z}/p\mathbb{Z}$ và tất cả $y \in \mathbb{Z}/q\mathbb{Z}$, ta có
$$x \otimes y = ap(x \otimes y) + bq(x \otimes y)$$
$$= a(px \otimes y) + b(x \otimes qy)$$
$$= a(0 \otimes y) + b(x \otimes 0)$$
$$= 0.$$
Nó là khả dĩ/có thể đến salvage nhất định các tính chất của các tích tenxơ giữ cho các không gian vectơ bởi thu hẹp lớp của các môđun dưới consideration. Ví dụ, xạ ảnh các môđun có pretty tốt behavior w.r.t. các tích tenxơ. tự do A-module $F$, là môđun rằng có cơ sở (basis) (i.e., có một họ, $(e_{i})_{i\in I}$, của các vectơ độc lập tuyến tính (linearly independent) trong $F$ rằng sinh (span) $F)$. Xạ ảnh các môđun có nhiều tương đương các đặc trưng. Ở đây là một rằng là tốt nhất suited cho của ta cần:

> **Định nghĩa 35.7.** A-module, $P$, là xạ ảnh nếu nó là summand của môđun tự do (free module), nghĩa là, nếu có một tự do A-module, $F$, và một số A-module, $Q$, sao cho
$$F = P \oplus Q.$$
Cho trước bất kỳ A-module, $M$, ta cho $M^{*} = Hom_{A}(M, A)$ là đối ngẫu (đối ngẫu (dual)) của nó. Ta có kết quả sau mệnh đề:

> **Mệnh đề 35.11.** Với mọi finitely-generated xạ ảnh A-modules, $P$, và bất kỳ A-module, $Q$, ta có các đẳng cấu:
$$\sim$$
$$P^{**}=P$$
$$\sim  \otimes_{A}$$
$$Hom_{A}(P, Q)=P^{*} Q.$$

<!-- PAGE 1289 -->
Chứng minh phác thảo. Ta chỉ xét thứ hai đẳng cấu. Vì $P$ là xạ ảnh, ta có một số A-modules, $P_{1}, F$, với
$$P \oplus P_{1} = F,$$
Ở đâu $F$ là một số môđun tự do (free module). Bây giờ, ta biết rằng với mọi A-modules, $U, V, W$, ta có
$$Hom_{A}(U \oplus V, W) \sim = Hom_{A}(U, W) \prod  Hom_{A}(V, W) \sim = Hom_{A}(U, W) \oplus Hom_{A}(V, W),$$
Do đó
$$\oplus   \sim  \oplus  \sim$$
$$P^{*}P_{1}^{*}= F^{*},Hom_{A}(P, Q)Hom_{A}(P_{1}, Q)= Hom_{A}(F, Q).$$
Bởi tenxơ với $Q$ và bằng cách sử dụng sự kiện rằng tenxơ distributes w.r.t. coproducts, ta thu được
$$\otimes_{A}  \oplus   \otimes_{A}  \sim \oplus  \otimes_{A}  \sim \otimes_{A}$$
$$(P^{*} Q)(P_{1}^{*} Q)= (P^{*}P_{1}^{*} ) Q= F^{*} Q.$$
Bây giờ, chứng minh của Mệnh đề 33.19 đi qua bởi vì $F$ là tự do và sinh hữu hạn (finitely generated), do đó
$$\otimes_{A}  \oplus   \otimes_{A}  \sim \otimes_{A}  \longrightarrow  \sim  \oplus$$
$\alpha_{\otimes}$: $(P^{*}  Q) (P_{1}^{*}  Q) = F^{*}  Q Hom_{A}(F, Q) = Hom_{A}(P, Q) Hom_{A}(P_{1}, Q)$ là đẳng cấu và như $\alpha_{\otimes}$ các ánh xạ $P^{*} \otimes_{A} Q$ đến $Hom_{A}(P, Q)$, nó cho ta đẳng cấu giữa các phần tử này hai các không gian.
$$\otimes_{A}  \sim$$
Đẳng cấu $\alpha_{\otimes}$: $P^{*}  Q = Hom_{A}(P, Q)$ của Mệnh đề 35.11 là vẫn cho trước bởi
$$\alpha_{\otimes} (u^{*}\otimes f)(x) = u^{*}(x)f,u^{*}\in P^{*} , f \in Q, x \in P.$$
Nó là thuận tiện đến giới thiệu việc tính giá trị ánh xạ, $Ev_{x}$: $P^{*} \otimes_{A}  Q \to Q$, được định nghĩa với mọi $x \in P$ bởi
$$Ev_{x}(u^{*}\otimes f) = u^{*}(x)f,u^{*}\in P^{*} , f \in Q.$$
Ta sẽ cần sau đây tổng quát hóa của phần $(4)$ của Mệnh đề 33.13.

> **Mệnh đề 35.12.** Cho trước bất kỳ hai các họ của A-modules $(M_{i})_{i\in I}$ và $(N_{j})_{j\in J}$ (ở đâu I và $J$ là hữu hạn chỉ số các tập hợp), ta có đẳng cấu
$$\begin{pmatrix} MM_{i} \\ i\in I \end{pmatrix} \otimes \begin{pmatrix} MM_{j} \\ j\in I \end{pmatrix} \approx M(M_{i} \otimes N_{j}).$$
$$(i,j)\in I\times J$$
Mệnh đề 35.12 cũng nghiệm đúng cho vô hạn chỉ số các tập hợp.

> **Mệnh đề 35.13.** Cho $M$ và $N$ là hai A-module với $N$ môđun tự do (free module), và chọn bất kỳ cơ sở (basis) $(v_{1}, \dots  , v_{n})$ cho $N$. Thì, mọi phần tử của $M \otimes N$ có thể được biểu diễn trong duy nhất cách như tổng của tạo thành
$$u_{1} \otimes v_{1} + \cdots  + u_{n} \otimes v_{n},u_{i} \in M,$$
Sao cho $M \otimes N$ là đẳng cấu đến $M^{n}$ (như A-module).

<!-- PAGE 1290 -->

*Chứng minh.* Vì $N$ là tự do với cơ sở (basis) $(v_{1}, \dots  , v_{n})$, ta có đẳng cấu
$$N \approx Av_{1} \oplus \cdots  \oplus Av_{n}.$$
Theo Mệnh đề 35.12, ta thu được đẳng cấu
$$M \otimes N \approx M \otimes (Av_{1} \oplus \cdots  \oplus Av_{n}) \approx (M \otimes Av_{1}) \oplus \cdots  \oplus (M \otimes Av_{n}).$$
Bởi vì $(v_{1}, \dots  , v_{n})$ là cơ sở (basis) của $N$, mỗi $v_{j}$ là không xoắn (torsion-free) do đó ánh xạ $a \mapsto av_{j}$ là đẳng cấu của $A$ lên $Av_{j}$, và bởi vì $M \otimes A \approx M$, ta có đẳng cấu
$$M \otimes N \approx (M \otimes A) \oplus \cdots  \oplus (M \otimes A) \approx M \oplus \cdots  \oplus M = M^{n} ,$$
Như đã khẳng định. Mệnh đề 35.13 cũng nghiệm đúng cho vô hạn cơ sở (basis) $(v_{j})_{j\in J}$ của $N$. Hiển nhiên, phiên bản của Mệnh đề 35.13 cũng nghiệm đúng nếu $M$ là tự do và $N$ là tùy ý. tiếp theo mệnh đề sẽ là cũng là cần thiết.

> **Mệnh đề 35.14.** Cho trước bất kỳ A-module $M$ và bất kỳ lý tưởng (ideal) $\mathfrak{a}$ trong $A$, có một đẳng cấu
$$(A/\mathfrak{a}) \otimes_{A}  M \approx M/\mathfrak{a} M$$
Cho trước bởi ánh xạ $(\overline{a} \otimes u) \mapsto$ au (mod $\mathfrak{a} M)$, với mọi $\overline{a} \in A/\mathfrak{a}$ và tất cả $u \in M$. Phác thảo của chứng minh. Xét ánh xạ $\phi$: $(A/\mathfrak{a}) \times  M \to M/\mathfrak{a} M$ cho trước bởi
$$\phi (\overline{a, u}) = au(\mathrm{mod} \mathfrak{a} M)$$
Với mọi $\overline{a} \in A/\mathfrak{a}$ và tất cả $u \in M$. Nó là ngay lập tức đã kiểm tra rằng $\phi$ là xác định tốt (well-defined) bởi vì au (mod $\mathfrak{a} M)$ không phụ thuộc vào representative $a \in A$ được chọn trong lớp tương đương (equivalence class) $\overline{a}$, và $\phi$ là song tuyến tính. Vì vậy, $\phi$ cảm sinh ánh xạ tuyến tính (linear map) $\phi$: $(A/\mathfrak{a}) \otimes M \to M/\mathfrak{a} M$, sao cho $\phi (\overline{a} \otimes u) =$ au (mod $\mathfrak{a} M)$. Ta cũng định nghĩa ánh xạ $\psi$: $M \to (A/\mathfrak{a}) \otimes M$ bởi
$$\psi (u\overline{) = 1} \otimes u.$$
Vì $\mathfrak{a} M$ được sinh bởi các vectơ của tạo thành au với $a \in \mathfrak{a}$ và $u \in M$, và vì
$$\psi (au\overline{) = 1} \otimes au =\overline{a} \otimes u = 0 \otimes u = 0,$$
Ta xem rằng $\mathfrak{a} M \subseteq$ Ker $(\psi$), do đó $\psi$ cảm sinh ánh xạ tuyến tính (linear map) $\psi$: $M/\mathfrak{a} M \to (A/\mathfrak{a}) \otimes M$. Ta có
$$\psi (\phi (\overline{a} \otimes u)) = \psi (au)$$
$$\overline{= 1} \otimes au$$
$$=\overline{a} \otimes u$$
