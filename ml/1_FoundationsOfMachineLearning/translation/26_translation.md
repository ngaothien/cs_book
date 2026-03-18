# Chương 2: Khung học PAC (The PAC Learning Framework)

Một số câu hỏi cơ bản nảy sinh khi thiết kế và phân tích các thuật toán học từ ví dụ: Những gì có thể được học một cách hiệu quả? Những gì vốn dĩ khó để học? Cần bao nhiêu ví dụ để học thành công? Có một mô hình học tổng quát hay không? Trong chương này, chúng ta bắt đầu hình thức hóa và giải quyết các câu hỏi này bằng cách giới thiệu khung học **Xấp xỉ Đúng với Xác suất Cao** (Probably Approximately Correct — PAC).

Khung PAC giúp định nghĩa lớp các khái niệm có thể học được dựa trên số lượng điểm mẫu cần thiết để đạt được một lời giải xấp xỉ — độ phức tạp mẫu (sample complexity), cùng với độ phức tạp thời gian và không gian của thuật toán học, phụ thuộc vào chi phí biểu diễn tính toán của các khái niệm.

Đầu tiên, chúng ta mô tả khung PAC và minh họa nó, sau đó trình bày một số đảm bảo học tổng quát trong khung này khi tập giả thuyết được sử dụng là hữu hạn, bao gồm cả trường hợp nhất quán (consistent) — khi tập giả thuyết chứa khái niệm cần học — và trường hợp ngược lại — trường hợp không nhất quán (inconsistent).

## 2.1 Mô hình học PAC

Đầu tiên, chúng ta giới thiệu một số định nghĩa và ký hiệu cần thiết để trình bày mô hình PAC, các ký hiệu này cũng sẽ được sử dụng xuyên suốt phần lớn cuốn sách.

Chúng ta ký hiệu $\mathcal{X}$ là tập tất cả các ví dụ hoặc thực thể có thể có. $\mathcal{X}$ đôi khi còn được gọi là không gian đầu vào (input space). Tập tất cả các nhãn hoặc giá trị mục tiêu có thể có được ký hiệu là $\mathcal{Y}$. Trong chương giới thiệu này, chúng ta sẽ giới hạn ở trường hợp $\mathcal{Y}$ chỉ có hai nhãn, $\mathcal{Y} = \{0, 1\}$, tương ứng với bài toán gọi là phân loại nhị phân (binary classification). Các chương sau sẽ mở rộng các kết quả này cho các thiết lập tổng quát hơn.

Một khái niệm (concept) $c: \mathcal{X} \to \mathcal{Y}$ là một ánh xạ từ $\mathcal{X}$ tới $\mathcal{Y}$. Vì $\mathcal{Y} = \{0, 1\}$, chúng ta có thể đồng nhất $c$ với tập con của $\mathcal{X}$ mà trên đó $c$ nhận giá trị 1. Do đó, trong phần tiếp theo, chúng ta sẽ sử dụng tương đương một khái niệm cần học như một ánh xạ từ $\mathcal{X}$ tới $\{0, 1\}$, hoặc như một tập con của $\mathcal{X}$. Ví dụ, một khái niệm có thể là tập các điểm nằm trong một tam giác hoặc hàm chỉ thị của các điểm đó. Trong những trường hợp như vậy, chúng ta sẽ nói ngắn gọn rằng khái niệm cần học là một tam giác. Một lớp khái niệm (concept class) là một tập hợp các khái niệm mà chúng ta có thể muốn học và được ký hiệu là $C$. Ví dụ, đó có thể là tập tất cả các tam giác trong mặt phẳng.

Chúng ta giả sử rằng các ví dụ được phân phối độc lập và đồng nhất (i.i.d.) theo một phân phối $D$ cố định nhưng chưa biết. Bài toán học sau đó được phát biểu như sau. Bộ học xem xét một tập cố định các khái niệm có thể có $H$, được gọi là tập giả thuyết (hypothesis set), không nhất thiết phải trùng với $C$. Nó nhận một mẫu $S = (x_1, \ldots, x_m)$ được rút i.i.d. theo $D$ cùng với các nhãn $(c(x_1), \ldots, c(x_m))$, được xác định dựa trên một khái niệm mục tiêu cụ thể $c \in C$ cần học. Tác vụ sau đó là sử dụng mẫu có nhãn $S$ để chọn một giả thuyết $h_S \in H$ có sai số khái quát hóa (generalization error) nhỏ đối với khái niệm $c$. Sai số khái quát hóa của một giả thuyết $h \in H$, còn được gọi là rủi ro (risk) hoặc sai số thực (true error) (hay đơn giản là sai số) của $h$, được ký hiệu là $R(h)$ và được định nghĩa như sau.

**Định nghĩa 2.1 (Sai số khái quát hóa)** Cho một giả thuyết $h \in H$, một khái niệm mục tiêu $c \in C$, và một phân phối nền $D$, sai số khái quát hóa hay rủi ro của $h$ được định nghĩa bởi

$$R(h) = \underset{x \sim D}{\mathbb{P}}[h(x) \neq c(x)] = \underset{x \sim D}{\mathbb{E}}\left[\mathbf{1}_{h(x) \neq c(x)}\right], \quad (2.1)$$

trong đó $\mathbf{1}_\omega$ là hàm chỉ thị (indicator function) của sự kiện $\omega$.

Sai số khái quát hóa của một giả thuyết không thể được bộ học truy cập trực tiếp vì cả phân phối $D$ lẫn khái niệm mục tiêu $c$ đều chưa biết. Tuy nhiên, bộ học có thể đo sai số thực nghiệm (empirical error) của một giả thuyết trên mẫu có nhãn $S$.

**Định nghĩa 2.2 (Sai số thực nghiệm)** Cho một giả thuyết $h \in H$, một khái niệm mục tiêu $c \in C$, và một mẫu $S = (x_1, \ldots, x_m)$, sai số thực nghiệm hay rủi ro thực nghiệm của $h$ được định nghĩa bởi

$$\hat{R}_S(h) = \frac{1}{m} \sum_{i=1}^{m} \mathbf{1}_{h(x_i) \neq c(x_i)}. \quad (2.2)$$

Do đó, sai số thực nghiệm của $h \in H$ là sai số trung bình của nó trên mẫu $S$, trong khi sai số khái quát hóa là sai số kỳ vọng của nó dựa trên phân phối $D$. Chúng ta sẽ thấy trong chương này và các chương tiếp theo một số đảm bảo liên hệ hai đại lượng này với xác suất cao, dưới một số giả định tổng quát. Chúng ta có thể lưu ý ngay rằng đối với một $h \in H$ cố định, kỳ vọng của sai số thực nghiệm dựa trên một mẫu i.i.d. $S$ bằng sai số khái quát hóa:

$$\underset{S \sim D^m}{\mathbb{E}}\left[\hat{R}_S(h)\right] = R(h). \quad (2.3)$$

Thật vậy, theo tính tuyến tính của kỳ vọng và sự kiện rằng mẫu được rút i.i.d., chúng ta có thể viết

$$\underset{S \sim D^m}{\mathbb{E}}\left[\hat{R}_S(h)\right] = \frac{1}{m} \sum_{i=1}^{m} \underset{S \sim D^m}{\mathbb{E}}\left[\mathbf{1}_{h(x_i) \neq c(x_i)}\right] = \frac{1}{m} \sum_{i=1}^{m} \underset{S \sim D^m}{\mathbb{E}}\left[\mathbf{1}_{h(x) \neq c(x)}\right],$$

với mọi $x$ trong mẫu $S$. Do đó,

$$\underset{S \sim D^m}{\mathbb{E}}\left[\hat{R}_S(h)\right] = \underset{S \sim D^m}{\mathbb{E}}\left[\mathbf{1}_{h(x) \neq c(x)}\right] = \underset{x \sim D}{\mathbb{E}}\left[\mathbf{1}_{h(x) \neq c(x)}\right] = R(h).$$

Sau đây là phần giới thiệu khung học Xấp xỉ Đúng với Xác suất Cao (PAC). Gọi $n$ là một số sao cho chi phí tính toán để biểu diễn bất kỳ phần tử $x \in \mathcal{X}$ nào là nhiều nhất $O(n)$ và ký hiệu $\text{size}(c)$ là chi phí tối đa của biểu diễn tính toán của $c \in C$. Ví dụ, $x$ có thể là một vectơ trong $\mathbb{R}^n$, mà chi phí của biểu diễn dựa trên mảng sẽ là $O(n)$. Ngoài ra, gọi $h_S$ là giả thuyết được thuật toán $A$ trả về sau khi nhận mẫu có nhãn $S$. Để ký hiệu đơn giản, sự phụ thuộc của $h_S$ vào $A$ không được chỉ rõ.

**Định nghĩa 2.3 (Tính PAC-learnable)** Một lớp khái niệm $C$ được gọi là PAC-learnable nếu tồn tại một thuật toán $A$ và một hàm đa thức $\text{poly}(\cdot, \cdot, \cdot, \cdot)$ sao cho với mọi $\epsilon > 0$ và $\delta > 0$, với mọi phân phối $D$ trên $\mathcal{X}$ và với mọi khái niệm mục tiêu $c \in C$, điều sau đây đúng với mọi kích thước mẫu $m \geq \text{poly}(1/\epsilon, 1/\delta, n, \text{size}(c))$:

$$\underset{S \sim D^m}{\mathbb{P}}[R(h_S) \leq \epsilon] \geq 1 - \delta. \quad (2.4)$$

Nếu $A$ còn chạy trong thời gian $\text{poly}(1/\epsilon, 1/\delta, n, \text{size}(c))$, thì $C$ được gọi là PAC-learnable hiệu quả. Khi một thuật toán $A$ như vậy tồn tại, nó được gọi là thuật toán PAC-learning cho $C$.

Một lớp khái niệm $C$ do đó là PAC-learnable nếu giả thuyết mà thuật toán trả về sau khi quan sát một số điểm đa thức theo $1/\epsilon$ và $1/\delta$ là xấp xỉ đúng (sai số nhiều nhất $\epsilon$) với xác suất cao (ít nhất $1 - \delta$), điều này lý giải cho thuật ngữ PAC. Tham số $\delta > 0$ được sử dụng để định nghĩa độ tin cậy $1 - \delta$ và $\epsilon > 0$ là độ chính xác $1 - \epsilon$. Lưu ý rằng nếu thời gian chạy của thuật toán là đa thức theo $1/\epsilon$ và $1/\delta$, thì kích thước mẫu $m$ cũng phải là đa thức nếu toàn bộ mẫu được thuật toán nhận.

Một số điểm chính của định nghĩa PAC đáng được nhấn mạnh. Thứ nhất, khung PAC là một mô hình không phụ thuộc phân phối (distribution-free model): không có giả định cụ thể nào được đưa ra về phân phối $D$ từ đó các ví dụ được rút. Thứ hai, mẫu huấn luyện và các ví dụ kiểm thử được sử dụng để định nghĩa sai số được rút theo cùng phân phối $D$. Đây là một giả định tự nhiên và cần thiết để khái quát hóa có thể thực hiện được nói chung. Giả định này có thể được nới lỏng để bao gồm các bài toán điều chỉnh miền (domain adaptation) thuận lợi. Cuối cùng, khung PAC xử lý câu hỏi về khả năng học được cho một lớp khái niệm $C$ chứ không phải một khái niệm cụ thể. Lưu ý rằng lớp khái niệm $C$ được thuật toán biết, nhưng tất nhiên khái niệm mục tiêu $c \in C$ thì không biết.

Trong nhiều trường hợp, đặc biệt khi biểu diễn tính toán của các khái niệm không được thảo luận rõ ràng hoặc là hiển nhiên, chúng ta có thể bỏ qua sự phụ thuộc đa thức vào $n$ và $\text{size}(c)$ trong định nghĩa PAC và chỉ tập trung vào độ phức tạp mẫu.

Bây giờ chúng ta minh họa PAC-learning bằng một bài toán học cụ thể.

**Ví dụ 2.4 (Học các hình chữ nhật song song với trục — Learning axis-aligned rectangles)** Xét trường hợp tập các thực thể là các điểm trong mặt phẳng, $\mathcal{X} = \mathbb{R}^2$, và lớp khái niệm $C$ là tập tất cả các hình chữ nhật song song với trục nằm trong $\mathbb{R}^2$. Do đó, mỗi khái niệm $c$ là tập các điểm nằm trong một hình chữ nhật song song với trục cụ thể. Bài toán học bao gồm việc xác định với sai số nhỏ một hình chữ nhật song song với trục mục tiêu bằng cách sử dụng mẫu huấn luyện có nhãn. Chúng ta sẽ chứng minh rằng lớp khái niệm của các hình chữ nhật song song với trục là PAC-learnable.

> **Hình 2.1:** Khái niệm mục tiêu $R$ và giả thuyết khả dĩ $R'$. Các hình tròn biểu diễn các thực thể huấn luyện. Hình tròn xanh là điểm được gán nhãn 1, vì nó nằm trong hình chữ nhật $R$. Các điểm khác là đỏ và được gán nhãn 0.

Hình 2.1 minh họa bài toán. $R$ biểu diễn một hình chữ nhật song song với trục mục tiêu và $R'$ là một giả thuyết. Như có thể thấy từ hình, các vùng sai số của $R'$ được tạo bởi diện tích nằm trong hình chữ nhật $R$ nhưng ngoài hình chữ nhật $R'$ và diện tích nằm trong $R'$ nhưng ngoài hình chữ nhật $R$. Diện tích thứ nhất tương ứng với các âm tính giả (false negatives), tức là các điểm được $R'$ gán nhãn là 0 hoặc âm tính, nhưng thực tế là dương tính hoặc được gán nhãn 1. Diện tích thứ hai tương ứng với các dương tính giả (false positives), tức là các điểm được $R'$ gán nhãn dương tính nhưng thực tế được gán nhãn âm tính.

Để chứng minh rằng lớp khái niệm này là PAC-learnable, chúng ta mô tả một thuật toán PAC-learning đơn giản $A$. Cho một mẫu có nhãn $S$, thuật toán bao gồm việc trả về hình chữ nhật song song với trục chặt nhất $R' = R_S$ chứa các điểm được gán nhãn 1.

> **Hình 2.2:** Minh họa giả thuyết $R' = R_S$ được thuật toán trả về.

Theo định nghĩa, $R_S$ không tạo ra bất kỳ dương tính giả nào, vì các điểm của nó phải được bao gồm trong khái niệm mục tiêu $R$. Do đó, vùng sai số của $R_S$ được chứa trong $R$.

Gọi $R \in C$ là một khái niệm mục tiêu. Cố định $\epsilon > 0$. Gọi $\mathbb{P}[R]$ là khối lượng xác suất của vùng được định nghĩa bởi $R$, tức là xác suất mà một điểm được rút ngẫu nhiên theo $D$ rơi vào trong $R$. Vì các sai số do thuật toán của chúng ta gây ra chỉ có thể do các điểm rơi vào trong $R$, chúng ta có thể giả sử $\mathbb{P}[R] > \epsilon$; nếu không, sai số của $R_S$ nhỏ hơn hoặc bằng $\epsilon$ bất kể mẫu huấn luyện $S$ nào nhận được.

Bây giờ, vì $\mathbb{P}[R] > \epsilon$, chúng ta có thể định nghĩa bốn vùng hình chữ nhật $r_1, r_2, r_3$ và $r_4$ dọc theo các cạnh của $R$, mỗi vùng có xác suất ít nhất $\epsilon/4$. Các vùng này có thể được xây dựng bằng cách bắt đầu với toàn bộ hình chữ nhật $R$ rồi giảm kích thước bằng cách di chuyển một cạnh nhiều nhất có thể trong khi vẫn giữ khối lượng phân phối ít nhất $\epsilon/4$.

> **Hình 2.3:** Minh họa các vùng $r_1, \ldots, r_4$.

Gọi $l, r, b$ và $t$ là bốn giá trị thực định nghĩa $R$: $R = [l, r] \times [b, t]$. Khi đó, ví dụ, hình chữ nhật bên trái $r_4$ được định nghĩa bởi $r_4 = [l, s_4] \times [b, t]$, với $s_4 = \inf\{s : \mathbb{P}[[l, s] \times [b, t]] \geq \epsilon/4\}$. Không khó để thấy rằng xác suất của vùng $r_4' = [l, s_4) \times [b, t]$ thu được từ $r_4$ bằng cách loại bỏ cạnh ngoài cùng bên phải là nhiều nhất $\epsilon/4$. Các vùng $r_1, r_2, r_3$ và $r_1', r_2', r_3'$ được định nghĩa tương tự.

Quan sát rằng nếu $R_S$ giao với tất cả bốn vùng $r_i$, $i \in [4]$, thì vì nó là một hình chữ nhật, nó sẽ có một cạnh trong mỗi vùng này (lập luận hình học). Diện tích sai số của nó, tức là phần của $R$ mà nó không bao phủ, do đó được chứa trong hợp của các vùng $r_i'$, $i \in [4]$, và không thể có khối lượng xác suất lớn hơn $\epsilon$.

Theo phản chứng (contraposition), nếu $R(R_S) > \epsilon$, thì $R_S$ phải bỏ lỡ ít nhất một trong các vùng $r_i$, $i \in [4]$. Kết quả là, chúng ta có thể viết

$$\underset{S \sim D^m}{\mathbb{P}}[R(R_S) > \epsilon] \leq \underset{S \sim D^m}{\mathbb{P}}\left[\bigcup_{i=1}^{4} \{R_S \cap r_i = \emptyset\}\right] \quad (2.5)$$
$$\leq \sum_{i=1}^{4} \underset{S \sim D^m}{\mathbb{P}}[\{R_S \cap r_i = \emptyset\}] \quad \text{(theo bổ đề hợp)}$$
$$\leq 4(1 - \epsilon/4)^m \quad \text{(vì } \mathbb{P}[r_i] \geq \epsilon/4\text{)}$$
$$\leq 4 \exp(-m\epsilon/4),$$

trong đó ở bước cuối chúng ta đã sử dụng bất đẳng thức tổng quát $1 - x \leq e^{-x}$ đúng với mọi $x \in \mathbb{R}$. Với mọi $\delta > 0$, để đảm bảo $\mathbb{P}_{S \sim D^m}[R(R_S) > \epsilon] \leq \delta$, chúng ta có thể áp đặt

$$4 \exp(-\epsilon m / 4) \leq \delta \iff m \geq \frac{4}{\epsilon} \log \frac{4}{\delta}. \quad (2.6)$$

Do đó, với mọi $\epsilon > 0$ và $\delta > 0$, nếu kích thước mẫu $m$ lớn hơn $\frac{4}{\epsilon} \log \frac{4}{\delta}$, thì $\mathbb{P}_{S \sim D^m}[R(R_S) > \epsilon] \leq \delta$. Hơn nữa, chi phí tính toán của biểu diễn các điểm trong $\mathbb{R}^2$ và các hình chữ nhật song song với trục, có thể được định nghĩa bởi bốn góc của chúng, là hằng số. Điều này chứng minh rằng lớp khái niệm của các hình chữ nhật song song với trục là PAC-learnable và độ phức tạp mẫu của PAC-learning các hình chữ nhật song song với trục là $O\left(\frac{1}{\epsilon} \log \frac{1}{\delta}\right)$.

Một cách tương đương để trình bày các kết quả về độ phức tạp mẫu như (2.6), mà chúng ta sẽ thường thấy xuyên suốt cuốn sách, là đưa ra một cận khái quát hóa (generalization bound). Một cận khái quát hóa phát biểu rằng với xác suất ít nhất $1 - \delta$, $R(R_S)$ được chặn trên bởi một đại lượng phụ thuộc vào kích thước mẫu $m$ và $\delta$. Để có được điều này, chỉ cần đặt $\delta$ bằng cận trên được dẫn ra trong (2.5), tức là $\delta = 4 \exp(-m\epsilon/4)$ và giải theo $\epsilon$. Điều này cho rằng với xác suất ít nhất $1 - \delta$, sai số của thuật toán bị chặn như sau:

$$R(R_S) \leq \frac{4}{m} \log \frac{4}{\delta}. \quad (2.7)$$

Các thuật toán PAC-learning khác có thể được xem xét cho ví dụ này. Một phương án thay thế là trả về hình chữ nhật song song với trục lớn nhất không chứa các điểm âm tính. Chứng minh PAC-learning vừa trình bày cho hình chữ nhật song song với trục chặt nhất có thể dễ dàng thích ứng cho phân tích các thuật toán khác tương tự.

Lưu ý rằng tập giả thuyết $H$ mà chúng ta xem xét trong ví dụ này trùng với lớp khái niệm $C$ và lực lượng (cardinality) của nó là vô hạn. Tuy nhiên, bài toán vẫn có một chứng minh PAC-learning đơn giản. Vậy chúng ta có thể hỏi liệu một chứng minh tương tự có thể dễ dàng áp dụng cho các lớp khái niệm tương tự khác hay không. Điều này không hoàn toàn đơn giản vì lập luận hình học cụ thể được sử dụng trong chứng minh là then chốt. Việc mở rộng chứng minh cho các lớp khái niệm khác như các đường tròn không đồng tâm là không tầm thường (xem bài tập 2.4). Do đó, chúng ta cần một kỹ thuật chứng minh tổng quát hơn và các kết quả tổng quát hơn. Hai phần tiếp theo cung cấp cho chúng ta các công cụ như vậy trong trường hợp tập giả thuyết hữu hạn.

## 2.2 Đảm bảo cho tập giả thuyết hữu hạn — trường hợp nhất quán

Trong ví dụ về các hình chữ nhật song song với trục mà chúng ta đã xem xét, giả thuyết $h_S$ được thuật toán trả về luôn nhất quán (consistent), tức là nó không mắc sai số nào trên mẫu huấn luyện $S$. Trong phần này, chúng ta trình bày một cận tổng quát về độ phức tạp mẫu, hoặc tương đương là một cận khái quát hóa, cho các giả thuyết nhất quán, trong trường hợp lực lượng $|H|$ của tập giả thuyết là hữu hạn. Vì chúng ta xem xét các giả thuyết nhất quán, chúng ta sẽ giả sử rằng khái niệm mục tiêu $c$ nằm trong $H$.

**Định lý 2.5 (Cận học — $H$ hữu hạn, trường hợp nhất quán)** Gọi $H$ là một tập hữu hạn các hàm ánh xạ từ $\mathcal{X}$ tới $\mathcal{Y}$. Gọi $A$ là một thuật toán mà với mọi khái niệm mục tiêu $c \in H$ và mẫu i.i.d. $S$ trả về một giả thuyết nhất quán $h_S$: $\hat{R}_S(h_S) = 0$. Khi đó, với mọi $\epsilon, \delta > 0$, bất đẳng thức $\mathbb{P}_{S \sim D^m}[R(h_S) \leq \epsilon] \geq 1 - \delta$ đúng nếu

$$m \geq \frac{1}{\epsilon}\left(\log |H| + \log \frac{1}{\delta}\right). \quad (2.8)$$

Kết quả về độ phức tạp mẫu này có phát biểu tương đương sau đây dưới dạng một cận khái quát hóa: với mọi $\epsilon, \delta > 0$, với xác suất ít nhất $1 - \delta$,

$$R(h_S) \leq \frac{1}{m}\left(\log |H| + \log \frac{1}{\delta}\right). \quad (2.9)$$

**Chứng minh:** Cố định $\epsilon > 0$. Chúng ta không biết giả thuyết nhất quán $h_S \in H$ nào được thuật toán $A$ chọn. Giả thuyết này phụ thuộc thêm vào mẫu huấn luyện $S$. Do đó, chúng ta cần đưa ra một cận hội tụ đều (uniform convergence bound), tức là một cận đúng cho tập tất cả các giả thuyết nhất quán, và theo hệ quả bao gồm cả $h_S$. Vì vậy, chúng ta sẽ chặn xác suất mà một $h \in H$ nào đó sẽ nhất quán và có sai số lớn hơn $\epsilon$. Với mọi $\epsilon > 0$, định nghĩa $H_\epsilon$ bởi $H_\epsilon = \{h \in H : R(h) > \epsilon\}$. Xác suất mà một giả thuyết $h$ trong $H_\epsilon$ nhất quán trên mẫu huấn luyện $S$ được rút i.i.d., tức là nó không mắc sai số nào trên bất kỳ điểm nào trong $S$, có thể được chặn như sau:

$$\mathbb{P}[\hat{R}_S(h) = 0] \leq (1 - \epsilon)^m.$$

Do đó, theo bổ đề hợp (union bound), điều sau đúng:

$$\mathbb{P}\left[\exists h \in H_\epsilon : \hat{R}_S(h) = 0\right] = \mathbb{P}\left[\hat{R}_S(h_1) = 0 \vee \cdots \vee \hat{R}_S(h_{|H_\epsilon|}) = 0\right]$$
$$\leq \sum_{h \in H_\epsilon} \mathbb{P}\left[\hat{R}_S(h) = 0\right] \quad \text{(bổ đề hợp)}$$
$$\leq \sum_{h \in H_\epsilon} (1 - \epsilon)^m \leq |H|(1 - \epsilon)^m \leq |H| e^{-m\epsilon}.$$

Đặt vế phải bằng $\delta$ và giải theo $\epsilon$ hoàn tất chứng minh. $\square$

Định lý cho thấy rằng khi tập giả thuyết $H$ là hữu hạn, một thuật toán nhất quán $A$ là một thuật toán PAC-learning, vì độ phức tạp mẫu cho bởi (2.8) bị chi phối bởi một đa thức theo $1/\epsilon$ và $1/\delta$. Như được chỉ ra bởi (2.9), sai số khái quát hóa của các giả thuyết nhất quán được chặn trên bởi một hạng tử giảm theo hàm của kích thước mẫu $m$. Đây là một sự thật tổng quát: như kỳ vọng, các thuật toán học được hưởng lợi từ các mẫu huấn luyện có nhãn lớn hơn. Tốc độ giảm $O(1/m)$ được đảm bảo bởi định lý này, tuy nhiên, là đặc biệt thuận lợi.

Cái giá phải trả cho việc đưa ra một thuật toán nhất quán là sử dụng một tập giả thuyết $H$ lớn hơn chứa các khái niệm mục tiêu. Tất nhiên, cận trên (2.9) tăng theo $|H|$. Tuy nhiên, sự phụ thuộc đó chỉ là logarit. Lưu ý rằng hạng tử $\log |H|$, hoặc hạng tử liên quan $\log_2 |H|$ chỉ khác bởi một hằng số, có thể được giải thích là số bit cần thiết để biểu diễn $H$. Do đó, đảm bảo khái quát hóa của định lý được kiểm soát bởi tỷ lệ giữa số bit này, $\log_2 |H|$, và kích thước mẫu $m$.

Bây giờ chúng ta sử dụng Định lý 2.5 để phân tích PAC-learning với các lớp khái niệm khác nhau.

**Ví dụ 2.6 (Hội các literal Boolean — Conjunction of Boolean literals)** Xét việc học lớp khái niệm $C_n$ của các hội (conjunction) gồm nhiều nhất $n$ literal Boolean $x_1, \ldots, x_n$. Một literal Boolean là một biến $x_i$, $i \in [n]$, hoặc phủ định của nó $\bar{x}_i$. Với $n = 4$, một ví dụ là phép hội: $x_1 \wedge \bar{x}_2 \wedge x_4$, trong đó $\bar{x}_2$ ký hiệu phủ định của literal Boolean $x_2$. $(1, 0, 0, 1)$ là một ví dụ dương cho khái niệm này trong khi $(1, 0, 0, 0)$ là một ví dụ âm.

Quan sát rằng với $n = 4$, một ví dụ dương $(1, 0, 1, 0)$ ngụ ý rằng khái niệm mục tiêu không thể chứa các literal $\bar{x}_1$ và $\bar{x}_3$ và không thể chứa các literal $x_2$ và $x_4$. Ngược lại, một ví dụ âm không mang nhiều thông tin vì không biết bit nào trong $n$ bit của nó là không chính xác. Một thuật toán đơn giản để tìm một giả thuyết nhất quán dựa trên các ví dụ dương và bao gồm việc sau: với mỗi ví dụ dương $(b_1, \ldots, b_n)$ và $i \in [n]$, nếu $b_i = 1$ thì $\bar{x}_i$ bị loại bỏ như một literal khả dĩ trong lớp khái niệm và nếu $b_i = 0$ thì $x_i$ bị loại bỏ. Phép hội của tất cả các literal chưa bị loại bỏ do đó là một giả thuyết nhất quán với mục tiêu.

> **Hình 2.4:** Mỗi trong sáu hàng đầu tiên của bảng biểu diễn một ví dụ huấn luyện với nhãn của nó, + hoặc −, được chỉ ra ở cột cuối cùng. Hàng cuối cùng chứa 0 (tương ứng 1) ở cột $i \in [6]$ nếu mục thứ $i$ là 0 (tương ứng 1) cho tất cả các ví dụ dương. Nó chứa "?" nếu cả 0 lẫn 1 đều xuất hiện ở mục thứ $i$ cho một số ví dụ dương. Do đó, với mẫu huấn luyện này, giả thuyết được thuật toán nhất quán mô tả trong văn bản trả về là $\bar{x}_1 \wedge x_2 \wedge x_5 \wedge x_6$.

Chúng ta có $|H| = |C_n| = 3^n$, vì mỗi literal có thể được bao gồm ở dạng dương, ở dạng phủ định, hoặc không được bao gồm. Thay thế vào cận độ phức tạp mẫu cho các giả thuyết nhất quán cho cận độ phức tạp mẫu sau với mọi $\epsilon > 0$ và $\delta > 0$:

$$m \geq \frac{1}{\epsilon}\left((\log 3)n + \log \frac{1}{\delta}\right). \quad (2.10)$$

Do đó, lớp các hội gồm nhiều nhất $n$ literal Boolean là PAC-learnable. Lưu ý rằng độ phức tạp tính toán cũng là đa thức, vì chi phí huấn luyện trên mỗi ví dụ là $O(n)$. Với $\delta = 0.02$, $\epsilon = 0.1$, và $n = 10$, cận trở thành $m \geq 149$. Do đó, với một mẫu có nhãn ít nhất 149 ví dụ, cận đảm bảo độ chính xác 90% với độ tin cậy ít nhất 98%.

**Ví dụ 2.7 (Lớp khái niệm phổ quát — Universal concept class)** Xét tập $\mathcal{X} = \{0, 1\}^n$ của tất cả các vectơ Boolean với $n$ thành phần, và gọi $U_n$ là lớp khái niệm được tạo bởi tất cả các tập con của $\mathcal{X}$. Lớp khái niệm này có PAC-learnable không? Để đảm bảo một giả thuyết nhất quán, lớp giả thuyết phải bao gồm lớp khái niệm, do đó $|H| \geq |U_n| = 2^{(2^n)}$. Định lý 2.5 cho cận độ phức tạp mẫu sau:

$$m \geq \frac{1}{\epsilon}\left((\log 2)2^n + \log \frac{1}{\delta}\right). \quad (2.11)$$

Ở đây, số lượng mẫu huấn luyện cần thiết là lũy thừa theo $n$, đó là chi phí của biểu diễn một điểm trong $\mathcal{X}$. Do đó, PAC-learning không được định lý đảm bảo. Thực tế, không khó để chứng minh rằng lớp khái niệm phổ quát này không phải là PAC-learnable.

**Ví dụ 2.8 (Công thức DNF $k$ hạng — $k$-term DNF formulae)** Một công thức dạng chuẩn tắc tuyển (DNF — Disjunctive Normal Form) là một công thức được viết dưới dạng phép tuyển (disjunction) của nhiều hạng tử, mỗi hạng tử là một phép hội của các literal Boolean. Một $k$-term DNF là một công thức DNF được định nghĩa bởi phép tuyển của $k$ hạng tử, mỗi hạng tử là một phép hội gồm nhiều nhất $n$ literal Boolean. Do đó, với $k = 2$ và $n = 3$, một ví dụ của $k$-term DNF là $(x_1 \wedge \bar{x}_2 \wedge x_3) \vee (x_1 \wedge x_3)$.

Lớp $C$ của các công thức $k$-term DNF có phải là PAC-learnable không? Lực lượng của lớp là $3^{nk}$, vì mỗi hạng tử là một phép hội gồm nhiều nhất $n$ biến và có $3^n$ phép hội như vậy, như đã thấy trước đó. Tập giả thuyết $H$ phải chứa $C$ để tính nhất quán có thể xảy ra, do đó $|H| \geq 3^{nk}$. Định lý 2.5 cho cận độ phức tạp mẫu sau:

$$m \geq \frac{1}{\epsilon}\left((\log 3)nk + \log \frac{1}{\delta}\right), \quad (2.12)$$

đây là đa thức. Tuy nhiên, có thể chứng minh bằng quy giản từ bài toán tô màu đồ thị bằng 3 màu (graph 3-coloring problem) rằng bài toán học $k$-term DNF, ngay cả với $k = 3$, không phải là PAC-learnable hiệu quả, trừ khi RP — lớp phức tạp của các bài toán có thuật toán quyết định ngẫu nhiên thời gian đa thức — trùng với NP ($\text{RP} = \text{NP}$), điều này thường được phỏng đoán là không đúng. Do đó, mặc dù kích thước mẫu cần thiết để học các công thức $k$-term DNF chỉ là đa thức, PAC-learning hiệu quả của lớp này là không khả thi nếu $\text{RP} \neq \text{NP}$.

**Ví dụ 2.9 (Công thức $k$-CNF — $k$-CNF formulae)** Một công thức dạng chuẩn tắc hội (CNF — Conjunctive Normal Form) là một phép hội của các phép tuyển. Một công thức $k$-CNF là một biểu thức có dạng $T_1 \wedge \ldots \wedge T_j$ với độ dài $j \in \mathbb{N}$ tùy ý và mỗi hạng tử $T_i$ là một phép tuyển gồm nhiều nhất $k$ thuộc tính Boolean.

Bài toán học các công thức $k$-CNF có thể được quy giản thành bài toán học các hội Boolean literal, mà như đã thấy, là một lớp khái niệm PAC-learnable. Điều này có thể được thực hiện bằng cách giới thiệu $(2n)^k$ biến mới $Y_{u_1, \ldots, u_k}$ sử dụng song ánh sau:

$$(u_1, \ldots, u_k) \to Y_{u_1, \ldots, u_k}, \quad (2.13)$$

trong đó $u_1, \ldots, u_k$ là các literal Boolean trên các biến ban đầu $x_1, \ldots, x_n$. Giá trị của $Y_{u_1, \ldots, u_k}$ được xác định bởi $Y_{u_1, \ldots, u_k} = u_1 \vee \cdots \vee u_k$. Sử dụng ánh xạ này, mẫu huấn luyện ban đầu có thể được chuyển đổi thành một mẫu được định nghĩa theo các biến mới và bất kỳ công thức $k$-CNF nào trên các biến ban đầu có thể được viết như một phép hội trên các biến $Y_{u_1, \ldots, u_k}$. Phép quy giản này về PAC-learning của các hội Boolean literal có thể ảnh hưởng đến phân phối ban đầu của các ví dụ, nhưng điều này không phải là vấn đề vì trong khung PAC không có giả định nào về phân phối. Do đó, sử dụng phép biến đổi này, tính PAC-learnability của các hội Boolean literal suy ra tính PAC-learnability của các công thức $k$-CNF.

Đây là một kết quả đáng ngạc nhiên, vì bất kỳ công thức $k$-term DNF nào cũng có thể được viết dưới dạng một công thức $k$-CNF. Thật vậy, sử dụng tính kết hợp, một $k$-term DNF $T_1 \vee \cdots \vee T_k$ với $T_i = u_{i,1} \wedge \cdots \wedge u_{i,n_i}$ cho $i \in [k]$ có thể được viết lại thành một công thức $k$-CNF:

$$\bigvee_{i=1}^{k} u_{i,1} \wedge \cdots \wedge u_{i,n_i} = \bigwedge_{j_1 \in [n_1], \ldots, j_k \in [n_k]} u_{1,j_1} \vee \cdots \vee u_{k,j_k}.$$

Để minh họa phép viết lại này trong trường hợp cụ thể, quan sát ví dụ:

$$(u_1 \wedge u_2 \wedge u_3) \vee (v_1 \wedge v_2 \wedge v_3) = \bigwedge_{i,j=1}^{3} (u_i \vee v_j).$$

Nhưng, như chúng ta đã thấy trước đó, các công thức $k$-term DNF không phải là PAC-learnable hiệu quả nếu $\text{RP} \neq \text{NP}$! Điều gì có thể giải thích mâu thuẫn rõ ràng này? Vấn đề là việc chuyển đổi ngược từ một công thức $k$-CNF mà chúng ta đã học (tương đương với một $k$-term DNF) thành một $k$-term DNF nói chung là không khả thi nếu $\text{RP} \neq \text{NP}$.

Ví dụ này cho thấy một số khía cạnh then chốt của PAC-learning, bao gồm chi phí biểu diễn của một khái niệm và sự lựa chọn tập giả thuyết. Với một lớp khái niệm cố định, việc học có thể trở nên bất khả thi hoặc khả thi tùy thuộc vào sự lựa chọn biểu diễn.

## 2.3 Đảm bảo cho tập giả thuyết hữu hạn — trường hợp không nhất quán

Trong trường hợp tổng quát nhất, có thể không có giả thuyết nào trong $H$ nhất quán với mẫu huấn luyện có nhãn. Thực tế, đây là trường hợp thường gặp trong thực tiễn, khi các bài toán học có thể hơi khó hoặc các lớp khái niệm phức tạp hơn tập giả thuyết được thuật toán học sử dụng. Tuy nhiên, các giả thuyết không nhất quán với số lượng sai số nhỏ trên mẫu huấn luyện có thể hữu ích và, như chúng ta sẽ thấy, có thể được hưởng lợi từ các đảm bảo thuận lợi dưới một số giả định. Phần này trình bày các đảm bảo học chính xác cho trường hợp không nhất quán này và các tập giả thuyết hữu hạn.

Để dẫn ra các đảm bảo học trong thiết lập tổng quát hơn này, chúng ta sẽ sử dụng bất đẳng thức Hoeffding (Định lý D.2) hoặc hệ quả sau đây, liên hệ sai số khái quát hóa và sai số thực nghiệm của một giả thuyết đơn lẻ.

**Hệ quả 2.10** Cố định $\epsilon > 0$. Khi đó, với mọi giả thuyết $h: \mathcal{X} \to \{0, 1\}$, các bất đẳng thức sau đúng:

$$\underset{S \sim D^m}{\mathbb{P}}\left[\hat{R}_S(h) - R(h) \geq \epsilon\right] \leq \exp(-2m\epsilon^2) \quad (2.14)$$

$$\underset{S \sim D^m}{\mathbb{P}}\left[\hat{R}_S(h) - R(h) \leq -\epsilon\right] \leq \exp(-2m\epsilon^2). \quad (2.15)$$

Theo bổ đề hợp, điều này suy ra bất đẳng thức hai phía sau:

$$\underset{S \sim D^m}{\mathbb{P}}\left[\left|\hat{R}_S(h) - R(h)\right| \geq \epsilon\right] \leq 2\exp(-2m\epsilon^2). \quad (2.16)$$

**Chứng minh:** Kết quả suy ra trực tiếp từ Định lý D.2. $\square$

Đặt vế phải của (2.16) bằng $\delta$ và giải theo $\epsilon$ cho ngay cận sau cho một giả thuyết đơn lẻ.

**Hệ quả 2.11 (Cận khái quát hóa — giả thuyết đơn lẻ)** Cố định một giả thuyết $h: \mathcal{X} \to \{0, 1\}$. Khi đó, với mọi $\delta > 0$, bất đẳng thức sau đúng với xác suất ít nhất $1 - \delta$:

$$R(h) \leq \hat{R}_S(h) + \sqrt{\frac{\log \frac{2}{\delta}}{2m}}. \quad (2.17)$$

Ví dụ sau minh họa hệ quả này trong một trường hợp đơn giản.

**Ví dụ 2.12 (Tung đồng xu — Tossing a coin)** Tưởng tượng tung một đồng xu lệch mà mặt ngửa xuất hiện với xác suất $p$, và gọi giả thuyết của chúng ta là giả thuyết luôn đoán mặt sấp. Khi đó tỷ lệ sai số thực là $R(h) = p$ và tỷ lệ sai số thực nghiệm $\hat{R}_S(h) = \hat{p}$, trong đó $\hat{p}$ là xác suất thực nghiệm của mặt ngửa dựa trên mẫu huấn luyện được rút i.i.d. Do đó, hệ quả 2.11 đảm bảo với xác suất ít nhất $1 - \delta$ rằng

$$|p - \hat{p}| \leq \sqrt{\frac{\log \frac{2}{\delta}}{2m}}. \quad (2.18)$$

Vì thế, nếu chúng ta chọn $\delta = 0.02$ và sử dụng một mẫu có kích thước 500, với xác suất ít nhất 98%, chất lượng xấp xỉ sau được đảm bảo cho $\hat{p}$:

$$|p - \hat{p}| \leq \sqrt{\frac{\log(10)}{1000}} \approx 0.048. \quad (2.19)$$

Liệu chúng ta có thể áp dụng trực tiếp hệ quả 2.11 để chặn sai số khái quát hóa của giả thuyết $h_S$ được một thuật toán học trả về khi huấn luyện trên mẫu $S$ không? Không, vì $h_S$ không phải là một giả thuyết cố định, mà là một biến ngẫu nhiên phụ thuộc vào mẫu huấn luyện $S$ được rút. Cũng lưu ý rằng không giống như trường hợp giả thuyết cố định mà kỳ vọng của sai số thực nghiệm là sai số khái quát hóa (phương trình (2.3)), sai số khái quát hóa $R(h_S)$ là một biến ngẫu nhiên và nói chung khác với kỳ vọng $\mathbb{E}[\hat{R}_S(h_S)]$, vốn là một hằng số.

Do đó, giống như trong chứng minh cho trường hợp nhất quán, chúng ta cần dẫn ra một cận hội tụ đều, tức là một cận đúng với xác suất cao cho tất cả các giả thuyết $h \in H$.

**Định lý 2.13 (Cận học — $H$ hữu hạn, trường hợp không nhất quán)** Gọi $H$ là một tập giả thuyết hữu hạn. Khi đó, với mọi $\delta > 0$, với xác suất ít nhất $1 - \delta$, bất đẳng thức sau đúng:

$$\forall h \in H, \quad R(h) \leq \hat{R}_S(h) + \sqrt{\frac{\log |H| + \log \frac{2}{\delta}}{2m}}. \quad (2.20)$$

**Chứng minh:** Gọi $h_1, \ldots, h_{|H|}$ là các phần tử của $H$. Sử dụng bổ đề hợp và áp dụng hệ quả 2.11 cho mỗi giả thuyết ta có:

$$\mathbb{P}\left[\exists h \in H : \left|\hat{R}_S(h) - R(h)\right| > \epsilon\right]$$
$$= \mathbb{P}\left[\left(\left|\hat{R}_S(h_1) - R(h_1)\right| > \epsilon\right) \vee \cdots \vee \left(\left|\hat{R}_S(h_{|H|}) - R(h_{|H|})\right| > \epsilon\right)\right]$$
$$\leq \sum_{h \in H} \mathbb{P}\left[\left|\hat{R}_S(h) - R(h)\right| > \epsilon\right] \leq 2|H| \exp(-2m\epsilon^2).$$

Đặt vế phải bằng $\delta$ hoàn tất chứng minh. $\square$

Do đó, với một tập giả thuyết hữu hạn $H$,

$$R(h) \leq \hat{R}_S(h) + O\left(\sqrt{\frac{\log_2 |H|}{m}}\right).$$

Như đã chỉ ra, $\log_2 |H|$ có thể được hiểu là số bit cần thiết để biểu diễn $H$. Một số nhận xét tương tự như đã nêu đối với cận khái quát hóa trong trường hợp nhất quán có thể được đưa ra ở đây: kích thước mẫu $m$ lớn hơn đảm bảo khái quát hóa tốt hơn, và cận tăng theo $|H|$, nhưng chỉ theo logarit.

Tuy nhiên, ở đây, cận là một hàm kém thuận lợi hơn của $\frac{\log_2 |H|}{m}$; nó biến thiên theo căn bậc hai của hạng tử này. Đây không phải là cái giá nhỏ: với $|H|$ cố định, để đạt được đảm bảo tương tự như trong trường hợp nhất quán, cần một mẫu có nhãn lớn hơn bậc hai.

Lưu ý rằng cận gợi ý việc tìm kiếm sự đánh đổi giữa việc giảm sai số thực nghiệm và kiểm soát kích thước tập giả thuyết: một tập giả thuyết lớn hơn bị phạt bởi hạng tử thứ hai nhưng có thể giúp giảm sai số thực nghiệm, tức hạng tử thứ nhất. Nhưng, với sai số thực nghiệm tương tự, nó gợi ý nên sử dụng một tập giả thuyết nhỏ hơn. Điều này có thể được xem là một trường hợp của cái gọi là nguyên lý Dao cạo Occam (Occam's Razor), được đặt theo tên nhà thần học William xứ Occam: *Tính đa dạng không nên được đặt ra khi không cần thiết*, cũng được diễn đạt lại là *lời giải thích đơn giản nhất là tốt nhất*. Trong ngữ cảnh này, nó có thể được diễn đạt như sau: Với mọi thứ khác như nhau, một tập giả thuyết đơn giản (nhỏ) hơn là tốt hơn.

## 2.4 Tổng quát

Trong phần này, chúng ta sẽ thảo luận một số khía cạnh tổng quát của kịch bản học, mà để đơn giản, chúng ta đã bỏ qua trong phần thảo luận ở các phần trước.

### 2.4.1 Kịch bản tất định so với kịch bản ngẫu nhiên

Trong kịch bản tổng quát nhất của học có giám sát, phân phối $D$ được định nghĩa trên $\mathcal{X} \times \mathcal{Y}$, và dữ liệu huấn luyện là một mẫu có nhãn $S$ được rút i.i.d. theo $D$:

$$S = ((x_1, y_1), \ldots, (x_m, y_m)).$$

Bài toán học là tìm một giả thuyết $h \in H$ có sai số khái quát hóa nhỏ:

$$R(h) = \underset{(x,y) \sim D}{\mathbb{P}}[h(x) \neq y] = \underset{(x,y) \sim D}{\mathbb{E}}\left[\mathbf{1}_{h(x) \neq y}\right].$$

Kịch bản tổng quát hơn này được gọi là kịch bản ngẫu nhiên (stochastic scenario). Trong thiết lập này, nhãn đầu ra là một hàm xác suất của đầu vào. Kịch bản ngẫu nhiên nắm bắt nhiều bài toán thực tế trong đó nhãn của một điểm đầu vào không phải là duy nhất. Ví dụ, nếu chúng ta muốn dự đoán giới tính dựa trên các cặp đầu vào được tạo bởi chiều cao và cân nặng của một người, thì nhãn thường sẽ không duy nhất. Với hầu hết các cặp, cả nam và nữ đều là các giới tính khả dĩ. Với mỗi cặp cố định, sẽ có một phân phối xác suất của nhãn là nam.

Sự mở rộng tự nhiên của khung PAC-learning sang thiết lập này được gọi là PAC-learning bất khả tri (agnostic PAC-learning).

**Định nghĩa 2.14 (PAC-learning bất khả tri)** Gọi $H$ là một tập giả thuyết. $A$ là một thuật toán PAC-learning bất khả tri nếu tồn tại một hàm đa thức $\text{poly}(\cdot, \cdot, \cdot, \cdot)$ sao cho với mọi $\epsilon > 0$ và $\delta > 0$, với mọi phân phối $D$ trên $\mathcal{X} \times \mathcal{Y}$, điều sau đúng với mọi kích thước mẫu $m \geq \text{poly}(1/\epsilon, 1/\delta, n, \text{size}(c))$:

$$\underset{S \sim D^m}{\mathbb{P}}\left[R(h_S) - \min_{h \in H} R(h) \leq \epsilon\right] \geq 1 - \delta. \quad (2.21)$$

Nếu $A$ còn chạy trong thời gian $\text{poly}(1/\epsilon, 1/\delta, n)$, thì nó được gọi là một thuật toán PAC-learning bất khả tri hiệu quả.

Khi nhãn của một điểm có thể được xác định duy nhất bởi một hàm đo được $f: \mathcal{X} \to \mathcal{Y}$ (với xác suất một), thì kịch bản được gọi là tất định (deterministic). Trong trường hợp đó, chỉ cần xem xét một phân phối $D$ trên không gian đầu vào. Mẫu huấn luyện được thu bằng cách rút $(x_1, \ldots, x_m)$ theo $D$ và các nhãn được thu qua $f$: $y_i = f(x_i)$ với mọi $i \in [m]$. Nhiều bài toán học có thể được phát biểu trong kịch bản tất định này.

Trong các phần trước, cũng như trong phần lớn tài liệu được trình bày trong cuốn sách này, chúng ta đã giới hạn trình bày ở kịch bản tất định vì mục đích đơn giản. Tuy nhiên, với tất cả tài liệu này, sự mở rộng sang kịch bản ngẫu nhiên nên là trực tiếp đối với người đọc.

### 2.4.2 Sai số Bayes và nhiễu

Trong trường hợp tất định, theo định nghĩa, tồn tại một hàm mục tiêu $f$ không có sai số khái quát hóa: $R(f) = 0$. Trong trường hợp ngẫu nhiên, có một sai số tối thiểu khác không cho bất kỳ giả thuyết nào.

**Định nghĩa 2.15 (Sai số Bayes)** Cho một phân phối $D$ trên $\mathcal{X} \times \mathcal{Y}$, sai số Bayes $R^*$ được định nghĩa là cận dưới lớn nhất (infimum) của các sai số đạt được bởi các hàm đo được $h: \mathcal{X} \to \mathcal{Y}$:

$$R^* = \inf_{\substack{h \\ h \text{ đo được}}} R(h). \quad (2.22)$$

Một giả thuyết $h$ với $R(h) = R^*$ được gọi là giả thuyết Bayes hay bộ phân loại Bayes (Bayes classifier).

Theo định nghĩa, trong trường hợp tất định, chúng ta có $R^* = 0$, nhưng trong trường hợp ngẫu nhiên, $R^* \neq 0$. Rõ ràng, bộ phân loại Bayes $h_{\text{Bayes}}$ có thể được định nghĩa theo các xác suất có điều kiện:

$$\forall x \in \mathcal{X}, \quad h_{\text{Bayes}}(x) = \underset{y \in \{0, 1\}}{\text{argmax}} \; \mathbb{P}[y | x]. \quad (2.23)$$

Sai số trung bình mà $h_{\text{Bayes}}$ gây ra trên $x \in \mathcal{X}$ do đó là $\min\{\mathbb{P}[0|x], \mathbb{P}[1|x]\}$, và đây là sai số tối thiểu có thể có. Điều này dẫn đến định nghĩa sau về nhiễu.

**Định nghĩa 2.16 (Nhiễu — Noise)** Cho một phân phối $D$ trên $\mathcal{X} \times \mathcal{Y}$, nhiễu tại điểm $x \in \mathcal{X}$ được định nghĩa bởi

$$\text{noise}(x) = \min\{\mathbb{P}[1|x], \mathbb{P}[0|x]\}. \quad (2.24)$$

Nhiễu trung bình hoặc nhiễu liên kết với $D$ là $\mathbb{E}[\text{noise}(x)]$.

Do đó, nhiễu trung bình chính xác là sai số Bayes: $\text{noise} = \mathbb{E}[\text{noise}(x)] = R^*$. Nhiễu là một đặc trưng của tác vụ học chỉ ra mức độ khó khăn của nó. Một điểm $x \in \mathcal{X}$ mà $\text{noise}(x)$ gần bằng $1/2$ đôi khi được gọi là nhiễu (noisy) và tất nhiên là một thách thức cho việc dự đoán chính xác.

## 2.5 Ghi chú chương

Khung học PAC được Valiant [1984] giới thiệu. Cuốn sách của Kearns và Vazirani [1994] là một tài liệu tham khảo xuất sắc xử lý hầu hết các khía cạnh của PAC-learning và một số câu hỏi nền tảng khác trong học máy. Ví dụ của chúng ta về học các hình chữ nhật song song với trục, cũng được thảo luận trong tài liệu đó, ban đầu được Blumer et al. [1989] đưa ra.

Khung học PAC là một khung tính toán vì nó tính đến chi phí của các biểu diễn tính toán và độ phức tạp thời gian của thuật toán học. Nếu chúng ta bỏ qua các khía cạnh tính toán, nó tương tự với khung học được Vapnik và Chervonenkis xem xét trước đó [xem Vapnik, 2000]. Định nghĩa về nhiễu được trình bày trong chương này có thể được khái quát hóa cho các hàm mất mát tùy ý (xem bài tập 2.14).

Nguyên lý Dao cạo Occam được viện dẫn trong nhiều ngữ cảnh khác nhau, chẳng hạn như trong ngôn ngữ học để biện minh cho tính ưu việt của một tập hợp các quy tắc hoặc cú pháp. Độ phức tạp Kolmogorov có thể được xem là khung tương ứng trong lý thuyết thông tin. Trong ngữ cảnh của các đảm bảo học được trình bày trong chương này, nguyên lý gợi ý việc chọn lời giải thích tiết kiệm nhất (tập giả thuyết có lực lượng nhỏ nhất). Chúng ta sẽ thấy trong các phần tiếp theo các ứng dụng khác của nguyên lý này với các khái niệm khác nhau về tính đơn giản hoặc phức tạp.

## 2.6 Bài tập

**2.1 Biến thể hai bộ tiên tri (oracle) của mô hình PAC.** Giả sử rằng các ví dụ dương và âm bây giờ được rút từ hai phân phối riêng biệt $D_+$ và $D_-$. Với độ chính xác $(1 - \epsilon)$, thuật toán học phải tìm một giả thuyết $h$ sao cho:

$$\underset{x \sim D_+}{\mathbb{P}}[h(x) = 0] \leq \epsilon \quad \text{và} \quad \underset{x \sim D_-}{\mathbb{P}}[h(x) = 1] \leq \epsilon. \quad (2.25)$$

Do đó, giả thuyết phải có sai số nhỏ trên cả hai phân phối. Gọi $C$ là lớp khái niệm bất kỳ và $H$ là không gian giả thuyết bất kỳ. Gọi $h_0$ và $h_1$ lần lượt là các hàm luôn bằng 0 và luôn bằng 1. Chứng minh rằng $C$ là PAC-learnable hiệu quả sử dụng $H$ trong mô hình PAC tiêu chuẩn (một bộ tiên tri) khi và chỉ khi nó là PAC-learnable hiệu quả sử dụng $H \cup \{h_0, h_1\}$ trong mô hình PAC hai bộ tiên tri này.

**2.2 PAC-learning các siêu hình chữ nhật.** Một siêu hình chữ nhật song song với trục trong $\mathbb{R}^n$ là một tập có dạng $[a_1, b_1] \times \ldots \times [a_n, b_n]$. Chứng minh rằng các siêu hình chữ nhật song song với trục là PAC-learnable bằng cách mở rộng chứng minh đã cho trong Ví dụ 2.4 cho trường hợp $n = 2$.

**2.3 Đường tròn đồng tâm.** Gọi $\mathcal{X} = \mathbb{R}^2$ và xét tập các khái niệm có dạng $c = \{(x, y) : x^2 + y^2 \leq r^2\}$ cho một số thực $r$ nào đó. Chứng minh rằng lớp này có thể được $(\epsilon, \delta)$-PAC-learned từ dữ liệu huấn luyện có kích thước $m \geq (1/\epsilon) \log(1/\delta)$.

**2.4 Đường tròn không đồng tâm.** Gọi $\mathcal{X} = \mathbb{R}^2$ và xét tập các khái niệm có dạng $c = \{x \in \mathbb{R}^2 : \|x - x_0\| \leq r\}$ cho một điểm $x_0 \in \mathbb{R}^2$ và số thực $r$ nào đó. Gertrude, một nhà nghiên cứu học máy đầy tham vọng, cố gắng chứng minh rằng lớp khái niệm này có thể được $(\epsilon, \delta)$-PAC-learned với độ phức tạp mẫu $m \geq (3/\epsilon) \log(3/\delta)$, nhưng cô ấy gặp khó khăn với chứng minh. Ý tưởng của cô ấy là thuật toán học sẽ chọn đường tròn nhỏ nhất nhất quán với dữ liệu huấn luyện. Cô ấy đã vẽ ba vùng $r_1, r_2, r_3$ quanh rìa khái niệm $c$, mỗi vùng có xác suất $\epsilon/3$ (xem Hình 2.5(a)). Cô ấy muốn lập luận rằng nếu sai số khái quát hóa lớn hơn hoặc bằng $\epsilon$, thì một trong các vùng này phải bị dữ liệu huấn luyện bỏ lỡ, và do đó sự kiện này sẽ xảy ra với xác suất nhiều nhất $\delta$. Bạn có thể cho Gertrude biết cách tiếp cận của cô ấy có hoạt động không? *(Gợi ý: Bạn có thể muốn sử dụng Hình 2.5(b) trong lời giải).*

**2.5 Tam giác.** Gọi $\mathcal{X} = \mathbb{R}^2$ với cơ sở trực chuẩn $(e_1, e_2)$, và xét tập các khái niệm được định nghĩa bởi diện tích bên trong một tam giác vuông $ABC$ với hai cạnh song song với các trục, với $\vec{AB}/\|\vec{AB}\| = e_1$ và $\vec{AC}/\|\vec{AC}\| = e_2$, và $\|\vec{AB}\|/\|\vec{AC}\| = \alpha$ cho một số thực dương $\alpha \in \mathbb{R}_+$. Chứng minh, sử dụng các phương pháp tương tự như các phương pháp đã dùng trong chương cho các hình chữ nhật song song với trục, rằng lớp này có thể được $(\epsilon, \delta)$-PAC-learned từ dữ liệu huấn luyện có kích thước $m \geq (3/\epsilon) \log(3/\delta)$. *(Gợi ý: Bạn có thể xem xét sử dụng Hình 2.6 trong lời giải).*

**2.6 Học với nhiễu — hình chữ nhật.** Trong Ví dụ 2.4, chúng ta đã chứng minh rằng lớp khái niệm của các hình chữ nhật song song với trục là PAC-learnable. Xét bây giờ trường hợp các điểm huấn luyện mà bộ học nhận được chịu nhiễu sau: các điểm được gán nhãn âm không bị ảnh hưởng bởi nhiễu nhưng nhãn của một điểm huấn luyện dương được đổi ngẫu nhiên thành âm với xác suất $\eta \in (0, 1/2)$. Giá trị chính xác của tỷ lệ nhiễu $\eta$ không được bộ học biết nhưng một cận trên $\eta'$ được cung cấp với $\eta \leq \eta' < 1/2$. Chứng minh rằng thuật toán trả về hình chữ nhật chặt nhất chứa các điểm dương vẫn có thể PAC-learn các hình chữ nhật song song với trục khi có nhiễu.

**2.7 Học với nhiễu — trường hợp tổng quát.** Trong câu hỏi này, chúng ta tìm kiếm một kết quả tổng quát hơn câu hỏi trước. Chúng ta xét một tập giả thuyết hữu hạn $H$, giả sử rằng khái niệm mục tiêu nằm trong $H$, và áp dụng mô hình nhiễu sau: nhãn của một điểm huấn luyện mà bộ học nhận được bị thay đổi ngẫu nhiên với xác suất $\eta \in (0, 1/2)$. Giá trị chính xác của tỷ lệ nhiễu $\eta$ không được bộ học biết nhưng một cận trên $\eta'$ được cung cấp với $\eta \leq \eta' < 1/2$.

(a) Với mọi $h \in H$, gọi $d(h)$ là xác suất mà nhãn của một điểm huấn luyện mà bộ học nhận được không đồng ý với nhãn cho bởi $h$. Gọi $h^*$ là giả thuyết mục tiêu, chứng minh rằng $d(h^*) = \eta$.

(b) Tổng quát hơn, chứng minh rằng với mọi $h \in H$, $d(h) = \eta + (1 - 2\eta)R(h)$, trong đó $R(h)$ là sai số khái quát hóa của $h$.

(c) Cố định $\epsilon > 0$ cho câu này và tất cả các câu tiếp theo. Sử dụng các câu trước để chứng minh rằng nếu $R(h) > \epsilon$, thì $d(h) - d(h^*) \geq \epsilon'$, trong đó $\epsilon' = \epsilon(1 - 2\eta')$.

(d)–(f) *(Các phần tiếp theo yêu cầu chứng minh PAC-learning cho thuật toán $L$ trả về giả thuyết $h_S$ có số bất đồng nhỏ nhất, với cận mẫu $m \geq \frac{2}{\epsilon^2(1-2\eta')^2}\left(\log |H| + \log \frac{2}{\delta}\right)$.)*

**2.8 Học các khoảng.** Đưa ra một thuật toán PAC-learning cho lớp khái niệm $C$ được tạo bởi các khoảng đóng $[a, b]$ với $a, b \in \mathbb{R}$.

**2.9 Học hợp của các khoảng.** Đưa ra một thuật toán PAC-learning cho lớp khái niệm $C_2$ được tạo bởi hợp của hai khoảng đóng, tức $[a, b] \cup [c, d]$, với $a, b, c, d \in \mathbb{R}$. Mở rộng kết quả để dẫn ra một thuật toán PAC-learning cho lớp khái niệm $C_p$ được tạo bởi hợp của $p \geq 1$ khoảng đóng, tức $[a_1, b_1] \cup \cdots \cup [a_p, b_p]$, với $a_k, b_k \in \mathbb{R}$ cho $k \in [p]$. Độ phức tạp thời gian và mẫu của thuật toán là bao nhiêu theo hàm của $p$?

**2.10 Các giả thuyết nhất quán.** Trong chương này, chúng ta đã chứng minh rằng với tập giả thuyết hữu hạn $H$, một thuật toán học nhất quán $A$ là một thuật toán PAC-learning. Ở đây, chúng ta xem xét câu hỏi ngược lại. Gọi $Z$ là một tập hữu hạn gồm $m$ điểm có nhãn. Giả sử bạn được cho một thuật toán PAC-learning $A$. Chứng minh rằng bạn có thể sử dụng $A$ và một mẫu huấn luyện hữu hạn $S$ để tìm trong thời gian đa thức một giả thuyết $h \in H$ nhất quán với $Z$, với xác suất cao.

**2.11 Luật pháp thượng viện.** Đối với các vấn đề quan trọng, Tổng thống Mouth dựa vào lời khuyên của chuyên gia. Ông ấy chọn một cố vấn phù hợp từ bộ sưu tập $H = 2{,}800$ chuyên gia.

(a) Giả sử rằng các đạo luật được đề xuất một cách ngẫu nhiên độc lập và đồng nhất theo một phân phối $D$ được xác định bởi một nhóm thượng nghị sĩ chưa biết. Giả sử rằng Tổng thống Mouth có thể tìm và chọn một thượng nghị sĩ chuyên gia trong $H$ đã bỏ phiếu nhất quán với đa số trong $m = 200$ đạo luật gần nhất. Đưa ra một cận trên xác suất mà thượng nghị sĩ đó dự đoán sai cuộc bỏ phiếu toàn cầu cho một đạo luật tương lai. Giá trị của cận với độ tin cậy 95% là bao nhiêu?

(b) Giả sử bây giờ Tổng thống Mouth có thể tìm và chọn một thượng nghị sĩ chuyên gia trong $H$ đã bỏ phiếu nhất quán với đa số cho tất cả trừ $m' = 20$ trong số $m = 200$ đạo luật gần nhất. Giá trị của cận mới là bao nhiêu?

**2.12 Cận Bayes.** Gọi $H$ là một tập giả thuyết đếm được của các hàm ánh xạ $\mathcal{X}$ tới $\{0, 1\}$ và gọi $p$ là một độ đo xác suất trên $H$. Độ đo xác suất này biểu diễn xác suất tiên nghiệm trên lớp giả thuyết. Sử dụng bất đẳng thức Hoeffding để chứng minh rằng với mọi $\delta > 0$, với xác suất ít nhất $1 - \delta$, bất đẳng thức sau đúng:

$$\forall h \in H, \quad R(h) \leq \hat{R}_S(h) + \sqrt{\frac{\log \frac{1}{p(h)} + \log \frac{1}{\delta}}{2m}}. \quad (2.26)$$

So sánh kết quả này với cận đã cho trong trường hợp không nhất quán cho tập giả thuyết hữu hạn.

**2.13 Học với tham số chưa biết.** Trong Ví dụ 2.9, chúng ta đã chứng minh rằng lớp khái niệm $k$-CNF là PAC-learnable. Tuy nhiên, lưu ý rằng thuật toán được cung cấp $k$ như đầu vào. PAC-learning có khả thi ngay cả khi $k$ không được cung cấp không? *(Bài toán mở rộng về việc chuyển đổi thuật toán $A$ cần biết tham số $s$ thành thuật toán $B$ không cần biết $s$.)*

**2.14** Trong bài tập này, chúng ta khái quát hóa khái niệm nhiễu cho trường hợp hàm mất mát tùy ý $L: \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}_+$.

(a) Biện minh cho định nghĩa sau về nhiễu tại điểm $x \in \mathcal{X}$:

$$\text{noise}(x) = \min_{y' \in \mathcal{Y}} \underset{y}{\mathbb{E}}[L(y, y') | x].$$

Giá trị của $\text{noise}(x)$ trong kịch bản tất định là bao nhiêu? Định nghĩa có khớp với định nghĩa đã cho trong chương này cho phân loại nhị phân không?

(b) Chứng minh rằng nhiễu trung bình trùng với sai số Bayes (mất mát tối thiểu đạt được bởi một hàm đo được).
