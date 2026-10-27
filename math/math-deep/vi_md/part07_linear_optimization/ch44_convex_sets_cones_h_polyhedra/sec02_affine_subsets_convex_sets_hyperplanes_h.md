# Afin Các tập con, Các tập lồi, Các siêu phẳng, Các nửa không gian


<!-- PAGE 1577 -->
Ta cho ngắn gọn giới thiệu đến các phần tử này topics. Như reward, ta cung cấp một vài các tiêu chuẩn cho testing liệu hệ của các bất đẳng thức
$$Ax \le b, x \ge 0$$
Có nghiệm hoặc không theo các phiên bản của Farkas bổ đề (xem Mệnh đề 50.3 và Mệnh đề 47.4). Thì ta cho đầy đủ chứng minh của đối ngẫu mạnh (strong duality) định lý cho quy hoạch tuyến tính (linear programming) (xem Định lý 47.7). Ta cũng thảo luận độ bù lỏng (complementary slackness) các điều kiện và chỉ ra rằng chúng có thể được exploited đến design thuật toán cho việc giải bài toán quy hoạch tuyến tính (linear program) rằng sử dụng cả hai bài toán gốc (primal problem) và đối ngẫu (đối ngẫu (dual)) của nó. thuật toán này đã biết như gốc (primal) đối ngẫu (dual) thuật toán, mặc dù không được sử dụng nhiều nowadays, có đã được source của inspiration cho toàn bộ lớp của xấp xỉ các thuật toán cũng đã biết như gốc (primal) đối ngẫu (dual) các thuật toán. Ta hope rằng điều này chương và tiếp theo ba sẽ là motivation cho học (learning) nhiều hơn/thêm về quy hoạch tuyến tính (linear programming), lồi tối ưu hóa, nhưng cũng lồi hình học. “bible” trong lồi tối ưu hóa là Boyd và Vandenberghe $[29]$, và một của tốt nhất sources cho lồi hình học là Ziegler $[201]$. Điều này là khá advanced văn bản, do đó độc giả có thể muốn đến bắt đầu với Gallier $[74]$.

## 44.2 Afin Các tập con, Các tập lồi, Afin Các siêu phẳng,

$$Half-Spaces$$
$$\mathbb{R}^{n}$$
Ta quan điểm như bao gồm của các vectơ cột $(n\times 1$ các ma trận). Như thông thường, các vectơ hàng biểu diễn
$$\mathbb{R}^{n} \mathbb{R}$$
Các dạng tuyến tính, nghĩa là các ánh xạ tuyến tính (linear maps) $\phi$: $\to$, trong nghĩa rằng vectơ hàng (row vector) $y$ (một ma trận cỡ $1 \times  n$) biểu diễn dạng tuyến tính (linear form) $\phi$ nếu $\phi (x) =$ yx với mọi $x \in \mathbb{R}^{n}$. Ta ký hiệu không gian của các dạng tuyến tính (các vectơ hàng) bởi $(\mathbb{R}^{n})^{*}$.
$$\mathbb{R}^{n}$$
Nhắc lại rằng tổ hợp tuyến tính (linear combination) của các vectơ trong là biểu thức
$$\lambda_{1} x_{1} + \cdots  + \lambda_{m} x_{m}$$
$$\mathbb{R}^{n}  \mathbb{R}$$
Ở đâu $x_{1}, \dots  , x_{m} \in$ và ở đâu $\lambda_{1} , \dots  , \lambda_{m}$ là tùy ý các vô hướng trong. Cho trước dãy của các vectơ $S = (x_{1}, \dots  , x_{m})$ với $x_{i} \in \mathbb{R}^{n}$, tập hợp tất cả các tổ hợp tuyến tính của các vectơ trong $S$ là nhỏ nhất (tuyến tính) không gian con chứa $S$ được gọi là tuyến tính sinh (span) của $S$, và được ký hiệu sinh (span)(S).
$$\mathbb{R}^{n}  \mathbb{R}^{n}$$
Không gian con tuyến tính của là bất kỳ khác rỗng tập con của đóng dưới các tổ hợp tuyến tính.
$$\mathbb{R}^{n}$$

> **Định nghĩa 44.1.** tổ hợp afin (affine combination) của các vectơ trong là biểu thức
$$\lambda_{1} x_{1} + \cdots  + \lambda_{m} x_{m}$$
$$\mathbb{R}^{n}  \mathbb{R}$$
Ở đâu $x_{1}, \dots  , x_{m} \in$ và ở đâu $\lambda_{1} , \dots  , \lambda_{m}$ là các vô hướng trong thỏa mãn điều kiện
$$\lambda_{1}  + \cdots  + \lambda_{m}  = 1.$$
Cho trước dãy của các vectơ $S = (x_{1}, \dots  , x_{m})$ với $x_{i} \in \mathbb{R}^{n}$, tập hợp tất cả các tổ hợp afin của các vectơ trong $S$ là nhỏ nhất không gian con afin (affine subspace) chứa $S$ được gọi là afin bao (hull) của $S$ và được ký hiệu aff(S).

<!-- PAGE 1578 -->
$$(a)(b)$$
$$Figure 44.1: (a) A convex set; (b) A nonconvex set$$
$$\mathbb{R}^{n}  \mathbb{R}^{n}$$

> **Định nghĩa 44.2.** không gian con afin (affine subspace) $A$ của là bất kỳ tập con của đóng dưới các tổ hợp afin. Nếu $A$ là khác rỗng không gian con afin (affine subspace) $of\mathbb{R}^{n}$, thì nó có thể được được hiển thị rằng $V_{A} = {a-b$ |, $b \in A}$
$$\mathbb{R}^{n}$$
Là không gian con tuyến tính của và rằng
$$A = a + V_{A} = {a + v | v \in V_{A}}$$
Với mọi $a \in A$; xem Gallier $[73]$ (Mục 2.5).

> **Định nghĩa 44.3.** Cho trước không gian con afin (affine subspace) $A$, tuyến tính không gian $V_{A} = {a$ - $b$ |, $b \in A}$ được gọi là hướng của $A$. số chiều của khác rỗng không gian con afin (affine subspace) $A$ là số chiều của của nó hướng $V_{A}$.

> **Định nghĩa 44.4.** Lồi các tổ hợp là các tổ hợp afin $\lambda_{1} x_{1} +\cdots +\lambda_{m} x_{m}$ thỏa mãn extra điều kiện rằng $\lambda_{i}  \ge 0$ cho $i = 1, \dots  , m$. tập lồi (convex set) được định nghĩa như sau.
$$\mathbb{R}^{n}$$

> **Định nghĩa 44.5.** tập con $V$ của là lồi nếu với mọi hai các điểm, $b \in V$, ta có $c \in V$ với mọi điểm $c = (1$ - $\lambda )a + \lambda b$, với $0 \le \lambda  \le 1 (\lambda  \in \mathbb{R})$. Cho trước bất kỳ hai các điểm, $b$, ký hiệu [, $b]$ là thường được sử dụng đến ký hiệu đường thẳng đoạn thẳng giữa và $b$, nghĩa là,
$$\mathbb{R}^{n}$$
$$[a, b] = {c \in | c = (1 -\lambda )a + \lambda b, 0 \le \lambda  \le 1},$$
Và do đó tập hợp $V$ là lồi nếu [, $b] \subseteq V$ với mọi hai các điểm, $b \in V (a = b$ được phép). số chiều của tập lồi (convex set) $V$ là số chiều của của nó afin bao (hull) aff(). rỗng tập hợp là một cách tầm thường lồi, mọi one-point tập hợp ${a}$ là lồi, và toàn bộ afin $\mathbb{R}^{n}$ không gian là lồi. Hiển nhiên là giao của bất kỳ họ (hữu hạn hoặc vô hạn) của các tập lồi là lồi.

<!-- PAGE 1579 -->

> **Định nghĩa 44.6.** Cho trước bất kỳ (khác rỗng) tập con $S of\mathbb{R}^{n}$, nhỏ nhất tập lồi (convex set) chứa $S$ được ký hiệu bởi conv(S) và được gọi là bao lồi (convex hull) của $S$ (nó là giao của tất cả các tập lồi chứa $S)$. Nó là thiết yếu không chỉ đến có tốt understanding của conv(S), nhưng đến cũng có tốt các phương pháp cho việc tính toán nó. Ta có kết quả sau đơn giản nhưng then chốt kết quả.

> **Mệnh đề 44.1.** Với mọi họ $S = (a_{i})_{i\in I}$ của các điểm trong $\mathbb{R}^{n}$, tập hợp $V$ của lồi combi-
$$nations \sum_{i}  \in I \lambda_{i} a_{i} (where \sum_{i}  \in I \lambda_{i}  = 1 and \lambda_{i}  \ge 0) is the convex hull conv(S) of S = (a_{i})_{i\in I}.$$
Nó là tự nhiên đến tự hỏi liệu Mệnh đề 44.1 có thể được sharpened trong hai các hướng:
$(1)$ Là nó khả dĩ/có thể đến có cố định cận trên số của các điểm liên quan trong lồi các tổ hợp? $(2)$ Là nó cần đến xét lồi các tổ hợp của tất cả các điểm, hoặc là nó khả dĩ/có thể đến xét chỉ tập con với đặc biệt các tính chất? câu trả lời là yes trong cả hai các trường hợp. Trong Trường hợp $1$, Carath´eodory’s định lý khẳng định rằng nó là đủ đến xét lồi các tổ hợp của $n + 1$ các điểm. Ví dụ, trong mặt phẳng $\mathbb{R}^{2}$, bao lồi (convex hull) của tập hợp $S$ của các điểm là hợp của tất cả các tam giác (phần trong (interior) các điểm included) với các đỉnh trong $S$. Trong Trường hợp $2$, định lý của Krein và Milman khẳng định rằng tập lồi (convex set) rằng là cũng compắc là bao lồi (convex hull) của của nó extremal các điểm (cho trước tập lồi (convex set) $S$, điểm $a \in S$ là extremal nếu $S -{a}$ là cũng lồi). Ta sẽ không chứng minh các phần tử này các định lý ở đây, nhưng ta invite độc giả đến consult Gallier $[74]$ hoặc Berger $[12]$. Các tập lồi cũng phát sinh như các nửa không gian cut ra bởi afin các siêu phẳng.
$$\mathbb{R}^{n} \mathbb{R}\mathbb{R}^{n}$$

> **Định nghĩa 44.7.** afin tạo thành $\phi$: $\to$ được định nghĩa bởi một số dạng tuyến tính (linear form) $c \in$ ($)^{*}$ và một số vô hướng (scalar) $\beta  \in \mathbb{R}$ sao cho
$$\phi (x) = cx + \beta for all x \in \mathbb{R}^{n}.$$
Nếu $c \neq  0$, afin tạo thành $\phi$ specified bởi $(c, \beta$) định nghĩa afin siêu phẳng (hyperplane) (cho ngắn siêu phẳng (hyperplane)) $H(\phi$) cho trước bởi
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
$$H(\phi ) = {x \in | \phi (x) = 0} = {x \in | cx + \beta  = 0},$$
Và hai (đóng) các nửa không gian
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
$$H_{+}(\phi ) = {x \in | \phi (x) \ge 0} = {x \in | cx + \beta  \ge 0},$$
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
$$H_{-}(\phi ) = {x \in | \phi (x) \le 0} = {x \in | cx + \beta  \le 0}.$$
Khi $\beta  = 0$, ta gọi $H$ tuyến tính siêu phẳng (hyperplane). Cả hai $H_{+}(\phi$) và $H_{-}(\phi$) là lồi và $H = H_{+}(\phi$) $\cap H_{-}(\phi$).
$$\mathbb{R}^{2} \mathbb{R}$$
Ví dụ, $\phi$: $\to$ với $\phi (x, y) =$ 2x $+ y + 3$ là afin tạo thành định nghĩa đường thẳng
$$\mathbb{R}^{3} \mathbb{R}$$
Cho trước bởi phương trình $y =$ -2x - $3$. Một cái khác ví dụ của afin tạo thành là $\phi$: $\to$
