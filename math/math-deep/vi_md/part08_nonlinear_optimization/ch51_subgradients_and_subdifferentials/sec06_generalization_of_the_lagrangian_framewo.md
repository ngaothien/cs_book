# Tổng quát hóa của Hàm Lagrange (Lagrangian) Khung lý thuyết


<!-- PAGE 1897 -->

## 51.6 Tổng quát hóa của Hàm Lagrange (Lagrangian) Khung lý thuyết

Về cơ bản tất cả các kết quả được trình bày trong Mục 50.3, Mục 50.7, Mục 50.8, và Mục 50.9 về các hàm Lagrange (Lagrangian) và Hàm Lagrange (Lagrangian) đối ngẫu tổng quát hóa đến các bài toán quy hoạch liên quan đến thực sự/đúng đắn và lồi hàm mục tiêu (objective function) $J$, thực sự/đúng đắn và lồi bất đẳng thức các ràng buộc, và afin đẳng thức các ràng buộc. extra generality là rằng nó là không có dài hơn được giả sử rằng các hàm này là khả vi (differentiable). Điều này lý thuyết là một cách kỹ lưỡng được thảo luận trong Phần VI, Mục $28$, của Rockafellar $[143]$, cho các bài toán quy hoạch được gọi là thông thường lồi các bài toán quy hoạch. Ta thực hiện không có không gian đến chẵn/ngay cả phác thảo điều này lý thuyết nhưng ta sẽ spell ra một số của then chốt các kết quả.
$$\mathbb{R}^{n} \mathbb{R}$$
Ta sẽ là dealing với các bài toán quy hoạch bao gồm của hàm mục tiêu (objective function) $J$: $\to \cup {+\infty$ } mà là lồi và thực sự/đúng đắn, subject đến $m \ge 0$ bất đẳng thức contraints $\phi_{i} (v) \le 0$, và $p \ge 0$ afin đẳng thức các ràng buộc $\psi_{j} (v) = 0$. ràng buộc các hàm $\phi_{i}$ là cũng lồi và thực sự/đúng đắn, và ta giả sử rằng
$$relint(dom(J)) \subseteq relint(dom(\phi_{i} )),dom(J) \subseteq dom(\phi_{i} ),i = 1, \dots  , m.$$
Như vậy các bài toán quy hoạch được gọi là thông thường lồi các bài toán quy hoạch. Cho
$$\mathbb{R}^{n}$$
$$U = dom(J) \cap {v \in | \phi_{i} (v) \le 0, \psi_{j} (v) = 0, 1 \le i \le m, 1 \le j \le p},$$
Là tập hợp của chấp nhận được (feasible) các nghiệm. Ta là seeking các phần tử trong $u \in U$ rằng cực tiểu hóa $J$ trên $U$. suy rộng/tổng quát hóa phiên bản của Định lý 50.18 nghiệm đúng dưới ở trên các giả thiết trên $J$ và các ràng buộc $\phi_{i}$ và $\psi_{j}$, ngoại trừ rằng trong KKT các điều kiện, phương trình liên quan đến các gradien phải được thay thế bởi sau đây điều kiện liên quan đến các vi phân dưới:
$$!$$
$$0 \in \partial J + \sum_{i=1}^{m}  \lambda_{i} \phi_{i}  + \sum_{j=1}^{p}  \mu_{j} \psi_{j} (u),$$
Với $\lambda_{i}  \ge 0$ cho $i = 1, \dots  , m$ và $\mu_{j}  \in \mathbb{R}$ cho $j = 1, \dots  , p$ (ở đâu $u \in U$ và $J$ đạt của nó cực tiểu tại $u)$. Hàm Lagrange (Lagrangian) L(v, $\lambda , \nu$) của bài toán của chúng ta được định nghĩa như sau: Cho
$$\mathbb{R}^{m+p}$$
$$E_{m} = {x \in | x_{i} \ge 0, 1 \le i \le m}.$$
Thì
$$J(v) + \sum_{i}  m=1 \lambda_{i} \phi_{i} (v) + \sum  pj=1 \mu_{j} \psi_{j} (v)if (\lambda , \mu ) \in E_{m}, v \in dom(J)$$
$$$$
L(v, $\lambda , \mu$) $= -\infty$ nếu $(\lambda , \mu$) $\in / E_{m}, v \in$ dom(J)
$$+\infty if v \in /dom(J).$$
$$$$
$$\mathbb{R}_{+}^{m}\mathbb{R}^{p} \mathbb{R}^{n} \mathbb{R}$$
Cho cố định các giá trị $(\lambda , \mu$) $\in  \times$, ta cũng định nghĩa hàm $h: \to  \cup {+\infty$ } cho trước bởi
$$h(x) = J(x) + \sum_{i=1}^{m}  \lambda_{i} \phi_{i} (x) + \sum_{j=1}^{p}  \mu_{j} \psi_{j} (x),$$

<!-- PAGE 1898 -->
Có effective miền xác định là dom(J) (vì ta là giả sử rằng dom(J) $\subseteq dom(\phi_{i}$), $i = 1, \dots  , m)$. Do đó h(x) $=$ L(x, $\lambda , \mu$), nhưng $h$ là hàm chỉ của $x$, do đó ta ký hiệu nó một cách khác nhau để tránh confusion (cũng, technically, L(x, $\lambda , \mu$) có thể lấy giá trị $-\infty$, nhưng $h$ thực hiện không). Vì $J$ và $\phi_{i}$ là thực sự/đúng đắn các hàm lồi và $\psi_{j}$ là afin, hàm $h$ là thực sự/đúng đắn hàm lồi (convex function). chứng minh của suy rộng/tổng quát hóa phiên bản của Định lý 50.18 có thể được thu được bởi đặt cùng nhau Định lý 28.1, Định lý 28.2, và Định lý 28.3, trong Rockafellar $[143]$. Cho sake của tính đầy đủ, ta phát biểu các phần tử này các định lý. Ở đây là Định lý 28.1.

> **Định lý 51.39.** (Định lý 28.1, Rockafellar) Cho $(P)$ là thông thường lồi bài toán quy hoạch. Cho
$$\mathbb{R}_{+}^{m}\mathbb{R}^{p}$$
$(\lambda , \mu$) $\in  \times$ là Các nhân tử Lagrange (Lagrange multipliers) sao cho cận dưới đúng (infimum) của hàm $h = J + m  \lambda_{i} \phi_{i}  + p  \mu_{j} \psi_{j}$ là hữu hạn và bằng giá trị tối ưu (optimal value) của $J$ trên $U$. Cho $D$ là
$$\sum_{i}  minimal=1 set \sum  of^{j=1} over \mathbb{R}^{n} , and let { \in {} |}. Ifis the subset of$$
$$h I =i1, \dots  , m \lambda_{i}  = 0 D_{0}  D$$
Bao gồm của các vectơ $x$ sao cho
$$\phi_{i} (x) \le 0for all i \in I$$
$$\phi_{i} (x) = 0for all i \in /I$$
$$\psi_{j} (x) = 0for all j = 1, \dots  , p,$$
Thì $D_{0}$ là tập hợp của các điểm cực tiểu hóa của $(P)$ trên $U$. Và bây giờ ở đây là Định lý 28.2.

> **Định lý 51.40.** (Định lý 28.2, Rockafellar) Cho $(P)$ là thông thường lồi bài toán quy hoạch, và cho $I \subseteq {1, \dots  , m}$ là tập con của các chỉ số của bất đẳng thức các ràng buộc rằng là không afin. Giả sử rằng giá trị tối ưu (optimal value) của $(P)$ là hữu hạn, và rằng $(P)$ có ít nhất một nghiệm chấp nhận được (feasible solution) $x \in$ relint(dom(J)) sao cho
$$\phi_{i} (x) < 0for all i \in I.$$
$$\mathbb{R}_{+}^{m}\mathbb{R}^{p}$$
Thì ở đó tồn tại một số Các nhân tử Lagrange (Lagrange multipliers) $(\lambda , \mu$) $\in  \times$ (không nhất thiết duy nhất) sao cho
() cận dưới đúng (infimum) của hàm $h = J + m  \lambda_{i} \phi_{i}  + p  \mu_{j} \psi_{j}$ là hữu hạn và bằng
$$optimal value of over. \sum_{i}  =1 \sum  j=1$$
$$J U$$
Các giả thiết của Định lý 51.40 là qualification các điều kiện trên các ràng buộc, về cơ bản Slater’s các điều kiện từ Định nghĩa 50.6.

> **Định nghĩa 51.21.** Cho $(P)$ là thông thường lồi bài toán quy hoạch, và cho $I \subseteq {1, \dots  , m}$ là tập con của các chỉ số của bất đẳng thức các ràng buộc rằng là không afin. các ràng buộc là qualified là có một nghiệm chấp nhận được (feasible solution) $x \in$ relint(dom(J)) sao cho
$$\phi_{i} (x) < 0for all i \in I.$$
Cuối cùng, ở đây là Định lý 28.3 từ Rockafellar $[143]$.

<!-- PAGE 1899 -->

> **Định lý 51.41.** (Định lý 28.3, Rockafellar) Cho $(P)$ là thông thường lồi bài toán quy hoạch. Nếu $\mathbb{R}^{n} \mathbb{R}_{+}^{m} \mathbb{R}^{p} x \in$ và $(\lambda , \mu$) $\in  \times$, thì $(\lambda , \mu$) và $x$ có tính chất rằng
() cận dưới đúng (infimum) của hàm $h = J + m  \lambda_{i} \phi_{i}  + p  \mu_{j} \psi_{j}$ là hữu hạn và bằng
$$optimal value of over, and \sum_{i}  =1 \sum  j=1$$
$$J U$$
$(b)$ vectơ $x$ là nghiệm tối ưu (optimal solution) của $(P)$ (do đó $x \in U)$, khi và chỉ khi $(x, \lambda , \mu$) là điểm yên ngựa (saddle point) của Hàm Lagrange (Lagrangian) L(x, $\lambda , \mu$) của $(P)$. Hơn thế nữa, điều kiện này nghiệm đúng khi và chỉ khi sau đây KKT các điều kiện đúng:
$(1) \lambda  \in \mathbb{R}_{+}^{m}, \phi_{i} (x) \le 0$, và $\lambda_{i} \phi_{i} (x) = 0$ cho $i = 1, \dots  , m$.
$(2) \psi_{j} (x) = 0$ cho $j = 1, \dots  , p$.
$$(3) 0 \in \partial J(x) + \sum_{i}  m=1 \lambda_{i} \partial \phi_{i} (x) + \sum  pj=1 \mu_{j} \partial \psi_{j} (x).$$
Nhận thấy rằng theo Định lý 51.40, nếu giá trị tối ưu (optimal value) của $(P)$ là hữu hạn và nếu các ràng buộc là qualified, thì Điều kiện () của Định lý 51.41 nghiệm đúng cho $(\lambda , \mu$). Hệ quả là ta thu được kết quả sau hệ quả của Định lý 51.41 attributed đến Kuhn và Tucker, mà là một của chính các kết quả của lý thuyết. Nó là suy rộng/tổng quát hóa phiên bản của Định lý 50.18.

> **Định lý 51.42.** (Định lý 28.3.1, Rockafellar) Cho $(P)$ là thông thường lồi bài toán quy hoạch thỏa mãn giả thiết của Định lý 51.40, mà có nghĩa là giá trị tối ưu (optimal value) của $(P)$ là
$$\mathbb{R}^{n}$$
Hữu hạn, và rằng các ràng buộc là qualified. Trong thứ tự rằng vectơ $x \in$ là nghiệm tối ưu (optimal solution) đến $(P)$, nó là cần và đủ rằng ở đó tồn tại Các nhân tử Lagrange (Lagrange multipliers) $(\lambda , \mu$) $\in \mathbb{R}_{+}^{m} \mathbb{R}^{p} \times$ sao cho $(x, \lambda , \mu$) là điểm yên ngựa (saddle point) của L(x, $\lambda , \mu$). Tương đương, $x$ là nghiệm tối ưu (optimal solution) của $(P)$ khi và chỉ khi ở đó tồn tại Các nhân tử Lagrange (Lagrange multipliers) $(\lambda , \mu$) $\in \mathbb{R}_{+}^{m} \times  \mathbb{R}^{p}$, mà, cùng với $x$, thỏa mãn KKT các điều kiện từ Định lý 51.41. Định lý 51.42 có đến thực hiện với sự tồn tại của nghiệm tối ưu (optimal solution) cho $(P)$, nhưng nó thực hiện không nói anything về giá trị tối ưu (optimal value) của $(P)$. để thiết lập như vậy kết quả, ta cần khái niệm của đối ngẫu (dual) hàm. đối ngẫu (dual) hàm $G$ được định nghĩa bởi
$$G(\lambda , \mu ) = \inf L(v, \lambda , \mu ).$$
$$v\in \mathbb{R} n$$
Nó là hàm lõm (concave function) (do đó $-G$ là lồi) mà có thể lấy các giá trị $\pm \infty$. Lưu ý rằng cực đại hóa $G$, mà là tương đương đến cực tiểu hóa $-G$, chạy vào troubles nếu $G(\lambda , \mu$) $= +\infty$ với một số $\lambda , \mu$, nhưng rằng $G(\lambda , \mu$) $= -\infty$ thực hiện không gây ra bài toán. Tại thứ nhất glance, điều này dường như counterintuitive, nhưng nhớ rằng $G$ là lõm, không lồi. Nó là $-G$ rằng là lồi, và $-\infty$ và $+\infty$ thu được flipped. Thì suy rộng/tổng quát hóa và mạnh hơn phiên bản của Định lý 50.19(2) cũng nghiệm đúng. chứng minh có thể được thu được bởi đặt cùng nhau Hệ quả 28.3.1, Định lý 28.4, và Hệ quả 28.4.1, trong Rockafellar $[143]$. Cho sake của tính đầy đủ, ta phát biểu sau đây các kết quả từ Rockafellar $[143]$.
