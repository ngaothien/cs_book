# Đếm được thứ hai (second-countable) và Khả ly Các không gian


<!-- PAGE 1397 -->

![Figure 37.36](../../assets/ch37/fig_37_36.png)

**Hình 37.36:** bốn giai đoạn illustration của cách mà mặt phẳng $xy$ là wrapped xung quanh unit mặt cầu được tâm tại $(0, 0, 1)$. Khi được hoàn tất tất cả của mặt cầu được phủ ngoại trừ điểm $(0, 0, 2). (V_{i})_{i\in(I-{i0})}$, là mở phủ của $K_{0}$. Vì $K_{0}$ là compắc, có một hữu hạn mở phủ con (subcover), $(V_{j})_{j\in J}$, của $K_{0}$, và do đó, $(U_{j})_{j\in J\cup {i0}}$ là hữu hạn mở phủ của $E_{\omega}$. Cho chúng ta chỉ ra rằng $E_{\omega}$ là Hausdorff. Cho trước bất kỳ hai các điểm,, $b \in E_{\omega}$, nếu cả hai, $b \in E$, vì $E$ là Hausdorffand mọi tập mở (open set) trong $\mathcal{O}$ là tập mở (open set) trong $\mathcal{O}_{\omega}$, ở đó tồn tại rời nhau các tập mở, $U, V$ (trong $\mathcal{O})$, sao cho $a \in U$ và $b \in V$. Nếu $b = \omega$, vì $E$ là một cách địa phương compắc, tồn tại một tập compắc (compact set), $K$, chứa tập mở (open set), $U$, chứa và thì, $U$ và $V = (E -K)\cup {\omega$ } là rời nhau các tập mở (trong $\mathcal{O}_{\omega})$ sao cho $a \in U$ và $b \in V$. không gian $E$ là không gian con của $E_{\omega}$ bởi vì với mọi tập mở (open set), $U$, trong $\mathcal{O}_{\omega}$, hoặc $U \in O$ và $E \cap U = U$ là mở trong $E$, hoặc $U = (E$ - $K) \cup {\omega$ }, ở đâu $K$ là compắc trong $E$, và do đó, $U \cap E = E$ - $K$, mà là mở trong $E$, vì $K$ là compắc trong $E$ và do đó, đóng (vì $E$ là Hausdorff). Cuối cùng, nếu $E$ là không compắc, với mọi compắc tập con, $K$, của $E, E$ - $K$ là khác rỗng và do đó, với mọi tập mở (open set), $U = (E-K)\cup {\omega$ }, chứa $\omega$, ta có $U \cap E \neq  \emptyset$, mà chỉ ra rằng $\omega  \in \overline{E}$ và do đó, rằng $\overline{E} = E_{\omega}$.

## 37.6 Đếm được thứ hai (second-countable) và Khả ly Các không gian

Trong studying các mặt và các đa tạp, quan trọng tính chất là sự tồn tại của đếm được cơ sở (basis) cho tôpô. Thật vậy tính chất này, trong số khác things, các đảm bảo sự tồn tại của các tam giác phân của các đa tạp, và sự kiện rằng đa tạp (manifold) là mêtric hóa được.

<!-- PAGE 1398 -->
$$\omega$$
$$(0,0,1)$$
$$y$$
$$O$$
$$xE$$
$$\omega$$
$$(0,0,1)$$
$$y$$
$$KE-K$$
$$x$$

![Figure 37.37](../../assets/ch37/fig_37_37.png)

**Hình 37.37:** hai các loại của các tập mở liên kết với Alexandroff compactification của mặt phẳng $xy$. thứ nhất loại/kiểu của tập mở (open set) thực hiện không bao gồm $\omega$, i.e. bắc cực, trong khi thứ hai loại/kiểu của tập mở (open set) chứa $\omega$.

> **Định nghĩa 37.33.** không gian tôpô (topological space) $E$ được gọi là đếm được thứ hai (second-countable) nếu có một đếm được cơ sở (basis) cho của nó tôpô, i.e., nếu có một đếm được họ, $(U_{i})_{i\ge0}$, của các tập mở sao cho mọi tập mở (open set) của $E$ là hợp của các tập mở $U_{i}$.
$$\mathbb{R}^{n}$$
Nó là dễ dàng được thấy rằng là đếm được thứ hai (second-countable) và tổng quát hơn, rằng mọi không gian vectơ định chuẩn (normed vector space) của hữu hạn số chiều là đếm được thứ hai (second-countable). Tổng quát hơn, không gian mêtric (metric space) là secondcountable khi và chỉ khi nó là khả ly, rất hữu ích tính chất rằng nghiệm đúng với mọi của các không gian rằng ta sẽ xét trong thực tế.

> **Định nghĩa 37.34.** không gian tôpô (topological space) $E$ là khả ly nếu nó chứa một số đếm được tập con $S$ mà là trù mật trong $X$, nghĩa là, $\overline{S} = E$. Nhận thấy rằng theo Mệnh đề 37.4, tập con $S$ của $E$ là trù mật trong $E$ khi và chỉ khi mọi khác rỗng mở tập con của $E$ chứa một số phần tử của $S$. (mêtric) không gian $\mathbb{R}$ là khả ly bởi vì $\mathbb{Q}$ là đếm được trù mật tập con của $\mathbb{R}$. Tương tự, $\mathbb{C}  \mathbb{Q}^{n}  \mathbb{R}^{n}  \mathbb{R}^{n}$ là khả ly. Nói chung, là trù mật trong, do đó là khả ly, và tương tự, mọi hữu hạn chiều không gian vectơ định chuẩn (normed vector space) trên $\mathbb{R}$ (hoặc $\mathbb{C})$ là khả ly. Cho các không gian mêtric, ta có kết quả sau hữu ích kết quả.

> **Mệnh đề 37.37.** Nếu $E$ là không gian mêtric (metric space), thì $E$ là đếm được thứ hai (second-countable) khi và chỉ khi $E$ là khả ly.

<!-- PAGE 1399 -->

*Chứng minh.* Nếu $\mathcal{B} = (B_{n})$ là đếm được cơ sở (basis) cho tôpô của $E$, thì với mọi tập hợp $S$ thu được bởi chọn một số điểm $s_{n}$ trong $B_{n}$, vì mọi khác rỗng mở tập con $U$ của $E$ là hợp của một số của $B_{n}$, giao $U \cap S$ là khác rỗng, và do đó $S$ là trù mật trong $E$. Ngược lại, giả sử rằng có một đếm được tập con $S = (s_{n})$ của $E$ mà là trù mật trong $E$. Ta khẳng định rằng đếm được họ $\mathcal{B}$ của mở các hình cầu $B_{0}(s_{n}, 1/m) (m \in \mathbb{N}, m > 0)$ là cơ sở (basis) cho tôpô của $E$. Với mọi $x \in E$ và mọi $r > 0$, tồn tại một $m > 0$ sao cho $1/m < r/2$, và một số $n$ sao cho $s_{n} \in B_{0}(x, 1/m)$. Suy ra rằng $x \in B_{0}(s_{n}, 1/m)$. Với mọi $y \in B_{0}(s_{n}, 1/m)$, ta có
$$d(x, y) \le d(x, s_{n}) + d(s_{n}, y) \le 2/m < r,$$
Do đó $B_{0}(s_{n}, 1/m) \subseteq B_{0}(x, r)$, mà theo Mệnh đề 37.8() suy ra rằng $\mathcal{B}$ là cơ sở (basis) cho tôpô của $E$.

> **Mệnh đề 37.38.** Nếu $E$ là compắc không gian mêtric (metric space), thì $E$ là khả ly.

*Chứng minh.* Với mọi $n > 0$, họ của mở các hình cầu của bán kính $1/n$ các dạng mở phủ của $E$,
$$and since E is compact, there is a finite subset A_{n} of E such that E = \bigcup_{a}  B_{0}(a_{i}, 1/n).$$
Nó là dễ để xem rằng điều này là tương đương đến điều kiện d(x, $A_{n}) < 1/n for^{i\in An}$ tất cả $x \in E$. Cho
$$A = \bigcup_{n}  \ge 1 A_{n}. Then A is countable, and for evey x \in E, we have$$
$$d(x, A) \le d(x, A_{n}) < \frac{1}{n} ,for all n \ge 1,$$
Mà suy ra rằng d(x, $A) = 0$; nghĩa là, $A$ là trù mật trong $E$. sau đây định lý do Uryshon cho rất hữu ích đủ điều kiện cho không gian tôpô (topological space) là mêtric hóa được.

> **Định lý 37.39.** (Urysohn metrization định lý) Nếu không gian tôpô (topological space) $E$ là chính quy và đếm được thứ hai (second-countable), thì nó là mêtric hóa được. chứng minh của Định lý 37.39 có thể được tìm thấy trong Munkres $[135]$ (Chương $4$, Định lý 34.1). Như hệ quả của Định lý 37.39, mọi (đếm được thứ hai (second-countable)) đa tạp (manifold), và do đó mọi Lie nhóm, là mêtric hóa được. sau đây technical kết quả chỉ ra rằng một cách địa phương compắc mêtric hóa được không gian mà là cũng khả ly có thể được biểu diễn dưới dạng hợp của đếm được monotonic dãy của compắc các tập con. Điều này cho chúng ta phương pháp cho generalizing khác nhau các tính chất của compắc các không gian mêtric đến một cách địa phương compắc các không gian mêtric của ở trên loại.

> **Mệnh đề 37.40.** Cho $E$ là một cách địa phương compắc không gian mêtric (metric space). Các tính chất sau đây là tương đương:
$(1)$ Ở đó là dãy $(U_{n})_{n\ge0}$ của mở các tập con sao cho với mọi $n \in \mathbb{N}, U_{n} \subseteq U_{n+1}, \overline{U}_{n}$ là
$$compact, \frac{a}{U_{n}} \subseteq , and .$$
$$U_{n+1} E = \bigcup_{n}  \ge 0 U_{n} = \bigcup  n\ge 0 \overline{U}_{n}$$

<!-- PAGE 1400 -->
$(2)$ không gian $E$ là hợp của đếm được họ của compắc các tập con của $E$.
$(3)$ không gian $E$ là khả ly.
$$Proof. We \frac{show}{U_{n}} (1) implies (2), (2) implies (3), and (3) implies (1). Obviously, (1) implies$$
$(2)$ vì là compắc.
$$If (2) holds, then E = \bigcup_{n}  \ge 0 K_{n}, for some compact subsets K_{n}. By Proposition 37.38,$$
Mỗi compắc tập con $K_{n}$ là khả ly, do đó cho $S_{n}$ là đếm được trù mật tập con của $K_{n}$, Thì
$$S = \bigcup_{n}  \ge 0 S_{n} is a countable dense subset of E, since$$
$$E = \bigcup_{n\ge0}  K_{n} \subseteq \bigcup_{n\ge0}  \overline{S}_{n} \subseteq \overline{S} \subseteq E.$$
Hệ quả là $(3)$ nghiệm đúng. Nếu $(3)$ nghiệm đúng, cho $S = {s_{n}}$ là đếm được trù mật tập con của $E$. Theo Mệnh đề 37.37, không gian $E$ có đếm được $basis\mathcal{B}$ của các tập mở $O_{n}$. Vì $E$ là một cách địa phương compắc, với mọi $x \in E$, tồn tại một compắc lân cận (neighborhood) $W_{x}$ chứa $x$, và theo Mệnh đề 37.8, ở đó một số
$$\frac{index}{O_{n(x)}} n(x) such that x \in O_{n(x)} \subseteq W_{x}. Since W_{x} is a compact neighborhood, we deduce that$$
Là compắc. Hệ quả là, có một họ con $of\mathcal{B}$ bao gồm của mở các tập con $O_{i}$ như vậy $that\overline{O}_{i}$ là compắc, mà là đếm được cơ sở (basis) cho tôpô của $E$, do đó ta có thể giả sử rằng ta thu hẹp của ta attention đến cơ sở (cơ sở (basis)) này. Ta định nghĩa dãy $(U_{n})_{n\ge1}$ của mở các tập con của $E$ bởi quy nạp như sau: Tập hợp $U_{1} = O_{1}$, và cho
$$U_{n+1} = O_{n+1} \cup V_{r}(\overline{U}_{n}),$$
Ở đâu $r > 0$ được chọn do đó $that\overline{V}_{r}\overline{(}\overline{U}_{n}\overline{)$ là compắc, mà là khả dĩ/có thể bởi $Proposition}$ 37.35. Ta ngay lập tức kiểm tra rằng $U_{n}$ thỏa mãn $(1)$ của Mệnh đề 37.40. Nó có thể cũng được hiển thị rằng nếu $E$ là một cách địa phương compắc không gian rằng có đếm được cơ sở (basis), thì $E_{\omega}$ cũng có đếm được cơ sở (basis) (và thực ra, là mêtric hóa được). Ta cũng có sau đây tính chất.

> **Mệnh đề 37.41.** Cho trước đếm được thứ hai (second-countable) không gian tôpô (topological space) $E$, mọi mở phủ $(U_{i})_{i\in I}$, của $E$ chứa một số đếm được phủ con (subcover).

*Chứng minh.* Cho $(O_{n})_{n\ge0}$ là đếm được cơ sở (basis) cho tôpô. Thì tất cả các tập hợp $O_{n}$ được chứa trong một số $U_{i}$ có thể được arranged vào đếm được dãy con, $(\Omega_{m} )_{m\ge0}$, của $(O_{n})_{n\ge0}$ và với mọi $\Omega_{m}$, tồn tại một $U_{im}$ sao cho $\Omega_{m}  \subseteq U_{im}$. Hơn nữa, mọi $U_{i}$ là một số hợp của các tập hợp $\Omega_{j}$, và do đó, mọi $a \in E$ thuộc đến một số $\Omega_{j}$, mà chỉ ra rằng $(\Omega_{m} )_{m\ge0}$ là đếm được mở phủ con (subcover) của $(U_{i})_{i\in I}$. Như immediate hệ quả của Mệnh đề 37.41, một cách địa phương liên thông đếm được thứ hai (second-countable) không gian có countably nhiều liên thông các thành phần.
