# Liên tục Các hàm, Các giới hạn


<!-- PAGE 1369 -->
$$(b) For any two open subsets, B_{1}, B_{2} \in B, for every x \in E, if x \in B_{1} \cap B_{2}, then there$$
$$is some B_{3} \in B such that x \in B_{3} and B_{3} \subseteq B_{1} \cap B_{2}. See Figure 37.15.$$
$$B$$
$$x$$
$$BU$$
$$1$$
$$\mathbb{R}^{2}$$

![Figure 37.14](../../assets/ch37/fig_37_14.png)

**Hình 37.14:** Cho trước mở tập con $U$ của và $x \in U$, tồn tại một hình cầu mở (open ball) $B$ chứa $x$ với $B \subset U$. Ở đó cũng tồn tại mở rectangle $B_{1}$ chứa $x$ với $B_{1} \subset U$.
$$x$$
$$B3$$
$$B$$
$$2$$
$$B$$
$$1$$
$$Figure 37.15: A schematic illustration of Condition (b) in Proposition 37.8.$$
Ta bây giờ xét cơ bản tính chất của tính liên tục.

## 37.3 Liên tục Các hàm, Các giới hạn


> **Định nghĩa 37.16.** Cho $(E,\mathcal{O}_{E})$ và $(F,\mathcal{O}_{F})$ là các không gian tôpô, và cho $f$: $E \to F$ là hàm. Với mọi $a \in E$, ta nói rằng $f$ là liên tục tại, nếu với mọi tập mở (open set) $V \in O_{F}$ chứa f(), tồn tại một tập mở (open set) $U \in O_{E}$ chứa, sao cho, f(U) $\subseteq V$. Xem Hình 37.16. Ta nói rằng $f$ là liên tục nếu nó là liên tục tại mọi $a \in E$. Định nghĩa lân cận (neighborhood) của $a \in E$ như bất kỳ tập con $N$ của $E$ chứa một số tập mở (open set) $O \in O$ sao cho $a \in O$. Nếu $f$ là liên tục tại và $N$ là bất kỳ lân cận (neighborhood) của f(), tồn tại một tập mở (open set) $V \subseteq N$ chứa f(), và vì $f$ là liên tục tại, tồn tại một tập mở (open set) $U$ chứa, sao cho f(U) $\subseteq V$. Vì $V \subseteq N$, tập mở (open set) $U$ là tập con của $f^{-1} (N)$

<!-- PAGE 1370 -->
$$f$$
$$Uaf(U)$$
$$f(a)$$
$$EV$$
$$F$$
$$Figure 37.16: A schematic illustration of Definition 37.16.$$
Chứa, và $f^{-1} (N)$ là lân cận (neighborhood) của. Ngược lại, nếu $f^{-1} (N)$ là lân cận (neighborhood) của bất cứ khi nào $N$ là bất kỳ lân cận (neighborhood) của f(), ta thấy ngay rằng $f$ là liên tục tại. Xem Hình 37.17.
$$f$$
$$f(U)$$
$$U$$
$$f(a)$$
$$VN$$
$$a$$
$$f  (N)-1$$
$$EF$$
$$Figure 37.17: A schematic illustration of the neighborhood condition.$$
Nó là dễ để xem rằng Định nghĩa 37.16 là tương đương đến sau đây các phát biểu.

> **Mệnh đề 37.9.** Cho $(E,\mathcal{O}_{E})$ và $(F,\mathcal{O}_{F})$ là các không gian tôpô, và cho $f$: $E \to F$ là hàm. Với mọi $a \in E$, hàm $f$ là liên tục tại $a \in E$ khi và chỉ khi với mọi lân cận (neighborhood) $N$ của f() $\in F$, thì $f^{-1} (N)$ là lân cận (neighborhood) của. hàm $f$ là liên tục trên $E$ khi và chỉ khi $f^{-1} (V$) là tập mở (open set) trong $\mathcal{O}_{E}$ với mọi tập mở (open set) $V \in O_{F}$. Nếu $E$ và $F$ là các không gian mêtric được định nghĩa bởi các mêtric $d_{E}$ và $d_{F}$, ta có thể chỉ ra dễ dàng rằng $f$ là liên tục tại khi và chỉ khi với mọi $\epsilon  > 0$, tồn tại một $\eta  > 0$, sao cho, với mọi $x \in E$,
$$if d_{E}(a, x) \le \eta , then d_{F}(f(a), f(x)) \le \epsilon .$$
Tương tự, nếu $E$ và $F$ là các không gian vectơ định chuẩn được định nghĩa bởi các chuẩn $\|\|_{E}$ và $\|\|_{F}$, ta có thể chỉ ra dễ dàng rằng $f$ là liên tục tại khi và chỉ khi

<!-- PAGE 1371 -->
Với mọi $\epsilon  > 0$, tồn tại một $\eta  > 0$, sao cho, với mọi $x \in E$,
$$if \|x -a\|_{E} \le \eta , then \|f(x) -f(a)\|_{F} \le \epsilon .$$
Nó là worth không rằng tính liên tục là tôpô khái niệm, trong nghĩa rằng tương đương các mêtric (hoặc tương đương các chuẩn) định nghĩa chính xác cùng khái niệm của tính liên tục.

> **Định nghĩa 37.17.** Nếu $(E,\mathcal{O}_{E})$ và $(F,\mathcal{O}_{F})$ là các không gian tôpô, và $f$: $E \to F$ là hàm, với mọi khác rỗng tập con $A \subseteq E$ của $E$, ta nói rằng $f$ là liên tục trên $A$ nếu thu hẹp của $f$ đến $A$ là liên tục đối với $(A,\mathcal{U})$ và $(F,\mathcal{O}_{F})$, ở đâu $\mathcal{U}$ là không gian con tôpô được cảm sinh bởi $\mathcal{O}_{E}$ trên $A$. Cho trước tích $E_{1}\times \cdots \times E_{n}$ của các không gian tôpô, như thông thường, ta cho $\pi_{i}$: $E_{1}\times \cdots \times E_{n} \to E_{i}$ là phép chiếu hàm sao cho, $\pi_{i} (x_{1}, \dots  , x_{n}) = x_{i}$. Ta kiểm chứng được ngay rằng mỗi $\pi_{i}$ là liên tục. Cho trước không gian tôpô (topological space) $(E,\mathcal{O})$, ta nói rằng điểm $a \in E$ là isolated nếu ${a}$ là tập mở (open set) trong $\mathcal{O}$. Thì nếu $(E,\mathcal{O}_{E})$ và $(F,\mathcal{O}_{F})$ là các không gian tôpô, bất kỳ hàm $f$: $E \to F$ là liên tục tại mọi isolated điểm $a \in E$. Trong rời rạc tôpô, mọi điểm là isolated. Trong không tầm thường không gian vectơ định chuẩn (normed vector space) $(E, \|\|)$ (với E̸ $= {0})$, không có điểm là isolated. để chỉ ra điều này, ta chỉ ra rằng mọi hình cầu mở (open ball) $B_{0}(u, \rho$,) chứa một số các vectơ khác nhau từ $u$. Thật vậy, vì $E$ là không tầm thường, tồn tại một $v \in E$ sao cho $v \neq  0$, và do đó $\lambda  = \|v\| > 0$ (bởi (N1)). Cho
$$w = u + \frac{\rho}{\lambda  + 1} v.$$
Vì $v \neq  0$ và $\rho  > 0$, ta có $w \neq  u$. Thì,
$$\|w -u\|= \frac{\rho}{\lambda  + 1} v = \frac{\rho \lambda}{\lambda  + 1} < \rho ,$$
Mà chỉ ra rằng $\|w$ - $u\| < \rho$, cho $w \neq  u$. sau đây mệnh đề là dễ dàng được hiển thị.

> **Mệnh đề 37.10.** Cho trước các không gian tôpô $(E,\mathcal{O}_{E}), (F,\mathcal{O}_{F})$, và $(G,\mathcal{O}_{G})$, và hai các hàm $f$: $E \to F$ và $g: F \to G$, nếu $f$ là liên tục tại $a \in E$ và $g$ là liên tục tại f() $\in F$, thì $g \circ f$: $E \to G$ là liên tục tại $a \in E$. Cho trước $n$ các không gian tôpô $(F_{i},\mathcal{O}_{i})$, với mọi hàm $f$: $E \to F_{1} \times  \cdots  \times  F_{n}$, thì $f$ là liên tục tại $a \in E$ khi và chỉ khi mọi $f_{i}$: $E \to F_{i}$ là liên tục tại, ở đâu $f_{i} = \pi_{i}  \circ f$. Một có thể cũng chỉ ra rằng trong không gian mêtric (metric space) $(E, d)$, khoảng cách $d: E\times E \to \mathbb{R}$ là liên tục, ở đâu $E \times  E$ có tích tôpô. Bởi tam giác bất đẳng thức, ta có
$$d(x, y) \le d(x, x_{0}) + d(x_{0}, y_{0}) + d(y_{0}, y) = d(x_{0}, y_{0}) + d(x_{0}, x) + d(y_{0}, y)$$

<!-- PAGE 1372 -->
Và
$$d(x_{0}, y_{0}) \le d(x_{0}, x) + d(x, y) + d(y, y_{0}) = d(x, y) + d(x_{0}, x) + d(y_{0}, y).$$
Hệ quả là,
$$|d(x, y) -d(x_{0}, y_{0})| \le d(x_{0}, x) + d(y_{0}, y),$$
Mà chứng tỏ rằng $d$ là liên tục tại $(x_{0}, y_{0})$. Thực ra điều này chỉ ra rằng $d$ là liên tục đều (uniformly continuous); xem Định nghĩa 37.36. Cho trước bất kỳ khác rỗng tập con $A$ của $E$, theo Mệnh đề 37.2, ánh xạ $x \mapsto$ d(x, $A)$ là liên tục (thực ra, uniformy liên tục). Tương tự, cho không gian vectơ định chuẩn (normed vector space) $(E, \|\|)$, chuẩn (norm) $\|\|: E \to \mathbb{R}$ là (uniformly) liên tục. Cho trước hàm $f$: $E_{1} \times  \cdots  \times  E_{n} \to F$, ta có thể fix $n$ - $1$ của các đối số/lập luận, nói $a_{1}, \dots  , a_{i-1}, a_{i+1}, \dots  , a_{n}$, và quan điểm $f$ như hàm của còn lại lập luận,
$$x_{i} \mapsto f(a_{1}, \dots  , a_{i-1}, x_{i}, a_{i+1}, \dots  , a_{n}),$$
Ở đâu $x_{i} \in E_{i}$. Nếu $f$ là liên tục, rõ ràng là mỗi $f_{i}$ là liên tục.  Một nên là careful rằng điều ngược lại là sai! Ví dụ, xét hàm $f$: $\mathbb{R} \times \mathbb{R} \to \mathbb{R}$, được định nghĩa sao cho,
$$f(x, y) = \frac{xy}{x^{2}+ y^{2}} if (x, y) \neq  (0, 0), andf(0, 0) = 0.$$
Hàm $f$ là liên tục trên $\mathbb{R} \times \mathbb{R} -{(0, 0)}$, nhưng trên đường thẳng $y =$ mx, với $m \neq  0$, ta có f(x, $y) =_{1+}^{m}$ ̸ $= 0$, và do đó, trên điều này đường thẳng, f(x, $y)$ thực hiện không cách tiếp cận $0$ khi $(x, y)$ các cách tiếp cận $(0, 0).^{m2}$ Xem Hình 37.18.

![Figure 37.18](../../assets/ch37/fig_37_18.png)

**Hình 37.18:** đồ thị của f(x, $y) =_{x2}^{xy}$ cho $(x, y) \neq  (0, 0)$. đáy/dưới của điều này đồ thị, mà chỉ ra cách tiếp cận dọc theo $line^{+y2} y = -x$, thực hiện không có $z$ giá trị của $0$. sau đây mệnh đề là hữu ích cho chỉ ra rằng nhận giá trị thực (real-valued) các hàm là liên tục.

<!-- PAGE 1373 -->

> **Mệnh đề 37.11.** Nếu $E$ là không gian tôpô (topological space), và $(\mathbb{R}$, |x-y|) các số thực dưới tiêu chuẩn tôpô, với mọi hai các hàm $f$: $E \to \mathbb{R}$ và $g: E \to \mathbb{R}$, với mọi $a \in E$, với mọi $\lambda  \in \mathbb{R}$, nếu $f$ và $g$ là liên tục tại, thì $f +g, \lambda f, f \cdot g$, là liên tục tại, và $f/g$ là liên tục tại nếu g() $\neq  0$.

*Chứng minh.* Để lại như một bài tập. Bằng cách sử dụng Mệnh đề 37.11, ta có thể chỉ ra dễ dàng rằng mọi thực đa thức hàm là liên tục. khái niệm của đẳng cấu của các không gian tôpô được định nghĩa như sau.

> **Định nghĩa 37.18.** Cho $(E,\mathcal{O}_{E})$ và $(F,\mathcal{O}_{F})$ là các không gian tôpô, và cho $f$: $E \to F$ là hàm. Ta nói rằng $f$ là phép đồng phôi (homeomorphism) giữa $E$ và $F$ nếu $f$ là song ánh (bijective), và cả hai $f$: $E \to F$ và $f^{-1}: F \to E$ là liên tục.  Một nên là careful rằng song ánh (bijective) hàm liên tục (continuous function) $f$: $E \to F$ là không nhất thiết phép đồng phôi (homeomorphism). Ví dụ, nếu $E = \mathbb{R}$ với rời rạc tôpô, và $F = \mathbb{R}$ với tiêu chuẩn tôpô, đồng nhất thức là không phép đồng phôi (homeomorphism). Một cái khác thú vị ví dụ
$$\mathbb{R}\mathbb{R}^{2}$$
Liên quan đến parametric đường cong là cho trước ở dưới. Cho $L:  \to$ là hàm, được định nghĩa sao cho,
$$L_{1}(t) = \frac{t(1 + t^{2})}{1 + t^{4}} ,$$
$$L_{2}(t) = \frac{t(1t^{2})}{1 + t^{4}} - .$$
Nếu ta nghĩ của (x(t), y(t)) $= (L_{1}(t), L_{2}(t))$ như hình học điểm trong $\mathbb{R}^{2}$, tập hợp của các điểm (x(t), y(t)) thu được bởi đặt $t$ biến thiên $in\mathbb{R}$ từ $-\infty$ đến $+\infty$, định nghĩa đường cong có hình dạng của “hình tám,” với self-intersection tại gốc, được gọi là “lemniscate của Bernoulli.” Xem Hình 37.19. ánh xạ $L$ là liên tục, và thực ra song ánh (bijective), nhưng của nó nghịch đảo $L^{-1}$ là không liên tục. Thật vậy, khi ta cách tiếp cận gốc trên branch của đường cong trong trên trái góc phần tư (i.e., các điểm sao cho, $x \le 0, y \ge 0)$, thì $t$ đi đến $-\infty$, và khi ta cách tiếp cận gốc trên branch của đường cong trong thấp hơn phải góc phần tư (i.e., các điểm sao cho, $x \ge 0, y \le 0)$, thì $t$ đi đến $+\infty$.
$$Figure 37.19: The lemniscate of Bernoulli.$$

<!-- PAGE 1374 -->
Ta cũng ôn tập/tổng quan khái niệm của giới hạn của dãy. Cho trước bất kỳ tập hợp $E$, dãy là bất kỳ hàm $x: \mathbb{N} \to E$, thường được ký hiệu bởi $(x_{n})_{n\in N}$, hoặc $(x_{n})_{n\ge0}$, hoặc chẵn/ngay cả bởi $(x_{n})$.

> **Định nghĩa 37.19.** Cho trước không gian tôpô (topological space) $(E,\mathcal{O})$, ta nói rằng dãy $(x_{n})_{n\in N}$ hội tụ đến một số $a \in E$ nếu với mọi tập mở (open set) $U$ chứa, tồn tại một $n_{0} \ge 0$, sao cho, $x_{n} \in U$, với mọi $n \ge n_{0}$. Ta cũng nói rằng là giới hạn của $(x_{n})_{n\in N}$. Xem Hình 37.20.
$$an0+2$$
$$an0+1$$
$$an0$$
$$a$$
$$U$$
$$an$$
$$E$$
$$Figure 37.20: A schematic illustration of Definition 37.19.$$
Khi $E$ là không gian mêtric (metric space) với mêtric $d$, nó là dễ để chỉ ra rằng điều này là tương đương đến sự kiện rằng, với mọi $\epsilon  > 0$, tồn tại một $n_{0} \ge 0$, sao cho, $d(x_{n}, a) \le \epsilon$, với mọi $n \ge n_{0}$. Khi $E$ là không gian vectơ định chuẩn (normed vector space) với chuẩn (norm) $\|\|$, nó là dễ để chỉ ra rằng điều này là tương đương đến sự kiện rằng, với mọi $\epsilon  > 0$, tồn tại một $n_{0} \ge 0$, sao cho, $\|x_{n}$ - $a\|\le \epsilon$, với mọi $n \ge n_{0}$. sau đây mệnh đề chỉ ra importance của Hausdorff separation axiom.

> **Mệnh đề 37.12.** Cho trước không gian tôpô (topological space) $(E,\mathcal{O})$, nếu Hausdorff separation axiom nghiệm đúng, thì mọi dãy có nhiều nhất một giới hạn.

*Chứng minh.* Để lại như một bài tập. Nó là worth không rằng khái niệm của giới hạn là tôpô, trong nghĩa rằng dãy hội tụ đến giới hạn $b$ khi và chỉ khi nó hội tụ đến cùng giới hạn $b$ trong bất kỳ tương đương mêtric (và tương tự cho tương đương các chuẩn). Nếu $E$ là không gian mêtric (metric space) và nếu $A$ là tập con của $E$, có một thuận tiện cách của chỉ ra rằng điểm $x \in E$ thuộc đến bao đóng (closure) $\overline{A}$ của $A$ theo các dãy.

> **Mệnh đề 37.13.** Cho trước bất kỳ không gian mêtric (metric space) $(E, d)$, với mọi tập con $A$ của $E$ và bất kỳ điểm $x \in E$, ta có $x \in \overline{A}$ khi và chỉ khi có một dãy $(a_{n})$ của các điểm $a_{n} \in A$ hội tụ đến $x$.

<!-- PAGE 1375 -->

*Chứng minh.* Nếu dãy $(a_{n})$ của các điểm $a_{n} \in A$ hội tụ đến $x$, thì với mọi mở tập con $U$
$$of E containing x, there is some \frac{n_{0}}{A.} such that a_{n} \in U for all n \ge n_{0}, so U \cap A \neq  \emptyset , and$$
Mệnh đề 37.4 suy ra rằng $x$
$$Conversely, assume that x \in \frac{\in}{A.} Then for every n \ge 1, consider the open ball B_{0}(x, 1/n).$$
Theo Mệnh đề 37.4, ta có $B_{0}(x, 1/n) \cap A \neq  \emptyset$, do đó ta có thể chọn một số $a_{n} \in B_{0}(x, 1/n) \cap A$. Điều này, cách, ta định nghĩa dãy $(a_{n})$ của các điểm trong $A$, và bởi cách xây dựng d(x, $a_{n}) < 1/n$ với mọi $n \ge 1$, do đó dãy $(a_{n})$ hội tụ đến $x$. Ta vẫn cần một nhiều hơn/thêm khái niệm của giới hạn cho các hàm.

> **Định nghĩa 37.20.** Cho $(E,\mathcal{O}_{E})$ và $(F,\mathcal{O}_{F})$ là các không gian tôpô, cho $A$ là một số khác rỗng tập con của $E$, và cho $f$: $A \to F$ là hàm. Với mọi $a \in \overline{A}$ và bất kỳ $b \in F$, ta nói rằng f(x) các cách tiếp cận $b$ như $x$ các cách tiếp cận với các giá trị trong $A$ nếu với mọi tập mở (open set) $V \in O_{F}$ chứa $b$, tồn tại một tập mở (open set) $U \in O_{E}$ chứa, sao cho, f(U $\cap A) \subseteq V$. Xem Hình 37.21. Điều này được ký hiệu bởi
$$lim f(x) = b.$$
$$x\to a,x\in A$$
$$f$$
$$f(U     A)h$$
$$a$$
$$bb$$
$$UV$$
$$A$$
$$E$$
$$F$$
$$Figure 37.21: A schematic illustration of Definition 37.20.$$
Thứ nhất, lưu ý rằng theo Mệnh đề 37.4, vì $a \in \overline{A}$, với mọi tập mở (open set) $U$ chứa, ta có $U \cap A \neq  \emptyset$, và định nghĩa là không tầm thường. Cũng, chẵn/ngay cả nếu $a \in A$, giá trị f() của $f$ tại đóng không có vai trò trong định nghĩa này. Khi $E$ và $F$ là không gian mêtric (metric space) với các mêtric $d_{E}$ và $d_{F}$, nó có thể được được hiển thị dễ dàng rằng định nghĩa có thể được được phát biểu như sau: Với mọi $\epsilon  > 0$, tồn tại một $\eta  > 0$, sao cho, với mọi $x \in A$,
$$if d_{E}(x, a) \le \eta , then d_{F}(f(x), b) \le \epsilon .$$
Khi $E$ và $F$ là các không gian vectơ định chuẩn với các chuẩn $\|\|_{E}$ và $\|\|_{F}$, nó có thể được được hiển thị dễ dàng rằng định nghĩa có thể được được phát biểu như sau:

<!-- PAGE 1376 -->
Với mọi $\epsilon  > 0$, tồn tại một $\eta  > 0$, sao cho, với mọi $x \in A$,
$$if \|x -a\|_{E} \le \eta , then \|f(x) -b\|_{F} \le \epsilon .$$
Ta có kết quả sau kết quả relating tính liên tục tại điểm và trước đó khái niệm.

> **Mệnh đề 37.14.** Cho $(E,\mathcal{O}_{E})$ và $(F,\mathcal{O}_{F})$ là hai các không gian tôpô, và cho $f$: $E \to F$ là hàm. Với mọi $a \in E$, hàm $f$ là liên tục tại khi và chỉ khi f(x) các cách tiếp cận f() khi $x$ các cách tiếp cận (với các giá trị trong $E)$.

*Chứng minh.* Trái như tầm thường bài tập. Một cái khác quan trọng mệnh đề relating khái niệm của sự hội tụ của dãy đến tính liên tục, được phát biểu mà không có chứng minh.

> **Mệnh đề 37.15.** Cho $(E,\mathcal{O}_{E})$ và $(F,\mathcal{O}_{F})$ là hai các không gian tôpô, và cho $f$: $E \to F$ là hàm.
$(1)$ Nếu $f$ là liên tục, thì với mọi dãy $(x_{n})_{n\in N}$ trong $E$, nếu $(x_{n})$ hội tụ đến, thì $(f(x_{n}))$ hội tụ đến f().
$(2)$ Nếu $E$ là không gian mêtric (metric space), và $(f(x_{n}))$ hội tụ đến f() bất cứ khi nào $(x_{n})$ hội tụ đến, với mọi dãy $(x_{n})_{n\in N}$ trong $E$, thì $f$ là liên tục. đặc biệt trường hợp của Định nghĩa 37.20 sẽ được sử dụng khi $E$ và $F$ là (không tầm thường) các không gian vectơ định chuẩn với các chuẩn $\|\|_{E}$ và $\|\|_{F}$. Cho $U$ là bất kỳ khác rỗng mở tập con của $E$. Ta đã chỉ ra trước đó rằng $E$ có không có isolated các điểm và rằng mọi tập hợp ${v}$ là đóng, với mọi $v \in E$. Vì $E$ là không tầm thường, với mọi $v \in U$, có một không tầm thường hình cầu mở (open ball) được chứa trong $U$ (mở
$$ball not reduced \frac{to}{A.} its center). Then, for every v \in U, A = U -{v} is open and nonempty,$$
Và rõ ràng, $v \in$ Với mọi $v \in U$, nếu f(x) các cách tiếp cận $b$ khi $x$ các cách tiếp cận $v$ với các giá trị trong $A = U -{v}$, ta nói rằng f(x) các cách tiếp cận $b$ khi $x$ các cách tiếp cận $v$ với các giá trị $\neq  v$ trong $U$. Điều này được ký hiệu bởi
$$lim f(x) = b.$$
$$x\to v,x\in U,x\neq v$$
Nhận xét: Variations của ở trên trường hợp chỉ ra lên trong sau đây trường hợp: $E =\mathbb{R}$, và $F$ là một số tùy ý không gian tôpô (topological space). Cho $A$ là một số khác rỗng tập con của $\mathbb{R}$, và cho $f$: $A \to F$ là một số hàm. Với mọi $a \in A$, ta nói rằng $f$ là liên tục trên phải tại nếu
$$lim f(x) = f(a).$$
$$x\to a,x\in A\cap [a, +\infty )$$
Ta có thể định nghĩa tính liên tục trên trái tại trong đồng dạng cách thức. Cho chúng ta xét một cái khác variation. Cho $A$ là một số khác rỗng tập con $of\mathbb{R}$, và cho $f$: $A \to F$ là một số hàm. Với mọi $a \in A$, ta nói rằng $f$ có discontinuity của thứ nhất loại tại nếu
$$lim f(x) = f(a_{-})$$
$$x\to a,x\in A\cap (-\infty ,a)$$
