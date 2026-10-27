# Tối ưu hóa Các bài tập; Cơ bản Thuật ngữ


<!-- PAGE 1703 -->
Chương $49$ Tổng quát Các kết quả của Tối ưu hóa Lý thuyết Điều này chương là devoted đến một số tổng quát các kết quả của tối ưu hóa lý thuyết. chính theme là để tìm đủ các điều kiện rằng đảm bảo rằng hàm mục tiêu (objective function) có cực tiểu mà là đạt được. Ta định nghĩa khái niệm của hàm bức (coercive function). hầu hết tổng quát kết quả là Định lý 49.2, mà áp dụng đến bức (coercive) hàm lồi (convex function) trên lồi tập con của khả ly Không gian Hilbert (Hilbert space). Trong trường hợp đặc biệt của bức (coercive) toàn phương phiếm hàm, ta thu được Lions– Stampacchia định lý (Định lý 49.6), và Lax–Milgram định lý (Định lý 49.7). Ta định nghĩa elliptic các phiếm hàm, mà tổng quát hóa toàn phương các hàm được định nghĩa bởi đối xứng xác định dương (SPD) các ma trận. Ta định nghĩa hạ gradien (gradient descent) các phương pháp, và thảo luận của chúng sự hội tụ. hạ gradien (gradient descent) phương pháp trông cho descent hướng và bước nhảy (stepsize) tham số, mà là thu được hoặc bằng cách sử dụng chính xác đường thẳng search hoặc backtracking đường thẳng search. popular kỹ thuật để tìm search hướng là hạ nhanh nhất (steepest descent). Ngoài hạ nhanh nhất (steepest descent) cho Euclidean chuẩn (norm), ta thảo luận hạ nhanh nhất (steepest descent) cho tùy ý chuẩn (norm). Ta cũng xét đặc biệt trường hợp của hạ nhanh nhất (steepest descent), Newton’s phương pháp. phương pháp này hội tụ faster hơn khác hạ gradien (gradient descent) các phương pháp, nhưng nó là khá expensive vì nó đòi hỏi việc tính toán và storing Hessians. Ta cũng trình bày phương pháp của liên hợp các gradien và chứng minh của nó tính đúng đắn. Ta ngắn gọn thảo luận phương pháp của gradien phép chiếu và hình phạt (penalty) phương pháp trong trường hợp của có ràng buộc optima.

## 49.1 Tối ưu hóa Các bài tập; Cơ bản Thuật ngữ

Chính mục tiêu của tối ưu hóa lý thuyết là để xây dựng các thuật toán để tìm các nghiệm (thường xấp xỉ) của các bài tập của tạo thành
$$findu$$
$$such that u \in U and J(u) = \inf J(v),$$
$$v\in U$$
Ở đâu $U$ là cho trước tập con của (thực) không gian vectơ (vector space) $V$ (có thể vô hạn dimensional) và $J$: $\Omega \to \mathbb{R}$ là hàm được định nghĩa trên một số mở tập con $\Omega$ của $V$ sao cho $U \subseteq \Omega$.
$$1703$$

<!-- PAGE 1704 -->
Là rất rõ ràng, $inf_{v\in U}$ J(v) ký hiệu lớn nhất thấp hơn cận của tập hợp của thực các số ${J(u)$ | $u \in U}$. để tạo sure rằng ta là trên firm grounds, cho chúng ta ôn tập/tổng quan các khái niệm của lớn nhất thấp hơn cận và least trên cận của tập hợp của thực các số. Cho $X$ là bất kỳ khác rỗng tập con của $\mathbb{R}$. tập hợp LB(X) của thấp hơn các cận của $X$ được định nghĩa như
$$LB(X) = {b \in \mathbb{R} | b \le x for all x \in X}.$$
Nếu tập hợp $X$ là không bị chặn ở dưới, mà có nghĩa là với mọi $r \in \mathbb{R}$ tồn tại một $x \in X$ sao cho $x < r$, thì LB(X) là rỗng. Ngược lại, nếu LB(X) là khác rỗng, vì nó là bị chặn ở trên bởi mọi phần tử của $X$, bởi cơ bản tính chất của thực các số, tập hợp LB(X) có lớn nhất phần tử được ký hiệu inf $X$. thực số inf $X$ là do đó lớn nhất thấp hơn cận của $X$. Nói chung, inf $X$ thực hiện không thuộc đến $X$, nhưng nếu nó thực hiện, thì nó là least phần tử của $X$. Nếu LB(X) $= \emptyset$, thì $X$ là không bị chặn ở dưới và inf $X$ là undefined. Trong trường hợp này (với abuse của ký hiệu), ta viết
$$\inf X = -\infty .$$
Bởi quy ước, khi $X = \emptyset$ ta tập hợp
$$\inf \emptyset = +\infty .$$
Ví dụ, nếu $X = {x \in \mathbb{R}$ | $x \le 0}$, thì LB(X) $= \emptyset$. Mặt khác, nếu $X = {1/n$ | $n \in \mathbb{N} -{0}}$, thì LB(X) $= {x \in \mathbb{R}$ | $x \le 0}$ và inf $X = 0$, mà là không trong $X$. Tương tự, tập hợp UB(X) của trên các cận của $X$ được cho bởi
$$UB(X) = {u \in \mathbb{R} | x \le u for all x \in X}.$$
Nếu $X$ là không bị chặn ở trên, thì UB(X) $= \emptyset$. Ngược lại, nếu UB(X) $\neq  \emptyset$, thì nó có least phần tử được ký hiệu sup $X$. Do đó sup $X$ là least trên cận của $X$. Nếu sup $X \in X$, thì nó là lớn nhất phần tử của $X$. Nếu UB(X) $= \emptyset$, thì
$$\sup X = +\infty .$$
Bởi quy ước, khi $X = \emptyset$ ta tập hợp
$$\sup \emptyset = -\infty .$$
Ví dụ, nếu $X = {x \in \mathbb{R}$ | $x \ge 0}$, thì UB(X) $= \emptyset$. Mặt khác, nếu $X = {1$ - $1/n$ | $n \in \mathbb{N} -{0}}$, thì UB(X) $= {x \in \mathbb{R}$ | $x \ge 1}$ và sup $X = 1$, mà là không trong $X$. phần tử $inf_{v\in U}$ J(v) là chỉ $inf{J(v)$ | $v \in U}$. ký hiệu $J^{*}$ là thường được sử dụng đến ký hiệu $inf_{v\in U}$ J(v). Nếu hàm $J$ là không bị chặn ở dưới, mà có nghĩa là với mọi $r \in \mathbb{R}$, tồn tại một $u \in U$ sao cho J(u) $< r$, thì
$$\inf J(v) = -\infty ,$$
$$v\in U$$

<!-- PAGE 1705 -->
Và ta nói rằng của ta cực tiểu hóa bài toán có không có nghiệm, hoặc rằng nó là không bị chặn (ở dưới). Ví dụ, nếu $V = \Omega = \mathbb{R}, U = {x \in \mathbb{R}$ | $x \le 0}$, và J(x) $= x$, thì hàm J(x) là không bị chặn ở dưới và $inf_{v\in U}$ J(v) $= -\infty$. vấn đề là rằng $J^{*}$ có thể không thuộc đến ${J(u)$ | $u \in U}$, nghĩa là, nó có thể không là đạt được bởi một số phần tử $u \in U$, và việc giải ở trên bài toán bao gồm trong việc tìm một số $u \in U$ rằng đạt được giá trị $J^{*}$ trong nghĩa rằng J(u) $= J^{*}$. Nếu không có như vậy $u \in U$ tồn tại, một lần nữa ta nói rằng của ta cực tiểu hóa bài toán có không có nghiệm. cực tiểu hóa bài toán
$$findu$$
$$such that u \in U and J(u) = \inf J(v)$$
$$v\in U$$
Là thường được trình bày trong sau đây nhiều hơn/thêm informal cách:
$$minimizeJ(v)$$
$$( Problem M)$$
$$subject to v \in U.$$
Vectơ $u \in U$ sao cho J(u) $= inf_{v\in U}$ J(v) là thường được gọi là điểm cực tiểu hóa của $J$ trên $U$. Một số các tác giả ký hiệu tập hợp của các điểm cực tiểu hóa của $J$ trên $U$ bởi arg $min_{v\in U}$ J(v) và viết
$$u \in arg minJ(v)$$
$$v\in U$$
Đến biểu diễn rằng $u$ là như vậy điểm cực tiểu hóa. Khi như vậy điểm cực tiểu hóa là duy nhất, lạm dụng ký hiệu, điều này duy nhất điểm cực tiểu hóa $u$ được ký hiệu bởi
$$u = arg minJ(v).$$
$$v\in U$$
Ta ưu tiên không để sử dụng điều này ký hiệu, mặc dù nó dường như đến có invaded literature. Nếu ta cần để cực đại hóa thay vì cực tiểu hóa hàm, thì ta thử để tìm một số $u \in U$ sao cho
$$J(u) = supJ(v).$$
$$v\in U$$
Ở đây $sup_{v\in U}$ J(v) là least trên cận của tập hợp ${J(u)$ | $u \in U}$. Một số các tác giả ký hiệu tập hợp của maximizers của $J$ trên $U$ bởi arg $max_{v\in U}$ J(v).
Nhận xét: Một số các tác giả định nghĩa được mở rộng nhận giá trị thực (real-valued) hàm như hàm $f$: $\Omega \to \mathbb{R}$ mà được phép đến lấy giá trị $-\infty$ hoặc chẵn/ngay cả $+\infty$ với một số của của nó các đối số/lập luận. Mặc dù điều này có thể là thuận tiện đến deal với các tình huống ở đâu ta cần đến xét $inf_{v\in U}$ J(v) hoặc $sup_{v\in U}$ J(v), như vậy “các hàm” là một cách thực riêng các hàm và ta ưu tiên không để sử dụng khái niệm của được mở rộng nhận giá trị thực (real-valued) hàm.

<!-- PAGE 1706 -->
Trong hầu hết các trường hợp, $U$ được định nghĩa như tập hợp của các nghiệm của hữu hạn các tập hợp của các ràng buộc, hoặc đẳng thức các ràng buộc $\phi_{i} (v) = 0$, hoặc bất đẳng thức các ràng buộc $\phi_{i} (v) \le 0$, ở đâu $\phi_{i}$: $\Omega \to \mathbb{R}$ là một số cho trước các hàm. hàm $J$ là thường được gọi là phiếm hàm của tối ưu hóa bài toán. Điều này là slightly lẻ thuật ngữ, nhưng nó là justified nếu $V$ là hàm không gian. sau đây các câu hỏi phát sinh một cách tự nhiên:
$(1)$ Các kết quả concerning sự tồn tại và tính duy nhất của nghiệm cho Bài toán $(M)$. Trong mục tiếp theo ta phát biểu đủ các điều kiện hoặc trên miền xác định $U$ hoặc trên hàm $J$ rằng đảm bảo sự tồn tại của nghiệm.
$(2)$ đặc trưng của khả dĩ/có thể các nghiệm của Bài toán $M$. Các phần tử này là các điều kiện với mọi phần tử $u \in U$ là nghiệm của bài toán. Như vậy các điều kiện thường liên quan đến đạo hàm $dJ_{u}$ của $J$, và có thể các đạo hàm của các hàm $\phi_{i}$ định nghĩa $U$. Một số của các điều kiện này trở thành đủ khi các hàm $\phi_{i}$ là lồi,
$(3)$ effective cách xây dựng của các thuật toán, typically lặp các thuật toán rằng xây dựng dãy $(u_{k})_{k\ge1}$ của các phần tử của $U$ có giới hạn là nghiệm $u \in U$ của bài toán của chúng ta. Nó là thì cần đến understand khi và cách mà quickly như vậy các dãy hội tụ. Hạ gradien (gradient descent) các phương pháp fall dưới điều này category. Như tổng quát quy tắc, không ràng buộc các bài tập (cho mà $U = \Omega = V$) là (nhiều) dễ hơn đến deal với hơn có ràng buộc các bài tập (ở đâu $U \neq  V$). material của điều này chương là heavily inspired bởi Ciarlet $[41]$. Trong chương này nó được giả sử rằng $V$ là thực không gian vectơ (vector space) với tích vô hướng (inner product) $\langle$ -, $-\rangle$. Nếu $V$ là vô hạn dimensional, thì ta giả sử rằng nó là thực Không gian Hilbert (Hilbert space) (nó là đầy đủ). Như thông thường, ta viết $\|u\| = \langle u, u\rangle^{1/2}$ cho chuẩn (norm) liên kết với tích vô hướng (inner product) $\langle$ -, $-\rangle$. độc giả có thể muốn đến ôn tập/tổng quan Mục 48.1, especially phép chiếu bổ đề và Riesz biểu diễn định lý. Như matter của thuật ngữ, nếu $U$ được định nghĩa bởi bất đẳng thức và đẳng thức các ràng buộc như
$$U = {v \in \Omega | \phi_{i} (v) \le 0, i = 1, \dots  , m, \psi_{j} (v) = 0, j = 1, \dots  , p},$$
Nếu $J$ và tất cả các hàm $\phi_{i}$ và $\psi_{j}$ là afin, bài toán được nói là tuyến tính (hoặc bài toán quy hoạch tuyến tính (linear program)), và ngược lại phi tuyến. Nếu $J$ là của tạo thành
$$J(v) = \langle Av, v\rangle -\langle b, v\rangle$$
Ở đâu $A$ là khác không đối xứng nửa xác định dương (positive semidefinite) ma trận và các ràng buộc là afin, bài toán được gọi là một toàn phương quy hoạch bài toán. Nếu tích vô hướng (inner product) $\langle$ -, $-\rangle$ là tiêu chuẩn Euclidean tích vô hướng (inner product), $J$ cũng được biểu diễn như
$$J(v) = v^{\top}Av -b^{\top}v.$$
