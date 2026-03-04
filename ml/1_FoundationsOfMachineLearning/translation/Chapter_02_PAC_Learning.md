# Chương 2: Khung Học PAC (The PAC Learning Framework)

Một số câu hỏi cơ bản nảy sinh khi thiết kế và phân tích các thuật toán học từ ví dụ: Điều gì có thể học được một cách hiệu quả? Điều gì về bản chất là khó học? Cần bao nhiêu ví dụ để học thành công? Có mô hình học tổng quát nào không? Trong chương này, chúng ta bắt đầu hình thức hóa và giải quyết những câu hỏi này bằng cách giới thiệu khung học **Probably Approximately Correct (PAC)** (Có thể Đúng Xấp Xỉ). Khung PAC giúp định nghĩa lớp các khái niệm có thể học được theo số lượng điểm mẫu cần thiết để đạt được nghiệm xấp xỉ, tức **độ phức tạp mẫu (sample complexity)**, cùng với độ phức tạp về thời gian và không gian của thuật toán học, phụ thuộc vào chi phí biểu diễn tính toán của các khái niệm.

Trước tiên chúng ta mô tả khung PAC và minh họa nó, sau đó trình bày một số đảm bảo học tổng quát trong khung này khi tập giả thuyết được sử dụng là hữu hạn, cả cho **trường hợp nhất quán (consistent case)** — khi tập giả thuyết chứa khái niệm cần học — và **trường hợp không nhất quán (inconsistent case)** ngược lại.

---

## 2.1 Mô Hình Học PAC (The PAC Learning Model)

Trước tiên chúng ta giới thiệu một số định nghĩa và ký hiệu cần thiết để trình bày mô hình PAC, những ký hiệu này cũng sẽ được dùng xuyên suốt phần lớn cuốn sách.

Chúng ta ký hiệu bằng $\mathcal{X}$ tập tất cả các ví dụ hoặc trường hợp có thể. $\mathcal{X}$ đôi khi còn được gọi là **không gian đầu vào (input space)**. Tập tất cả các nhãn hoặc giá trị mục tiêu có thể được ký hiệu bằng $\mathcal{Y}$. Với mục đích của chương giới thiệu này, chúng ta sẽ giới hạn bản thân trong trường hợp $\mathcal{Y}$ được rút gọn thành hai nhãn, $\mathcal{Y} = \{0, 1\}$, tương ứng với **phân loại nhị phân (binary classification)**. Các chương sau sẽ mở rộng các kết quả này sang các thiết lập tổng quát hơn.

Một **khái niệm (concept)** $c : \mathcal{X} \to \mathcal{Y}$ là một ánh xạ từ $\mathcal{X}$ sang $\mathcal{Y}$. Vì $\mathcal{Y} = \{0, 1\}$, ta có thể đồng nhất $c$ với tập con của $\mathcal{X}$ mà trên đó nó nhận giá trị 1. Do đó, trong phần tiếp theo, chúng ta coi một khái niệm cần học tương đương với một ánh xạ từ $\mathcal{X}$ sang $\{0, 1\}$, hoặc như một tập con của $\mathcal{X}$. Ví dụ, một khái niệm có thể là tập các điểm bên trong một tam giác, hoặc hàm chỉ thị của những điểm đó. Trong những trường hợp đó, chúng ta sẽ nói ngắn gọn rằng khái niệm cần học là một tam giác. Một **lớp khái niệm (concept class)** là một tập các khái niệm mà chúng ta có thể muốn học và được ký hiệu bằng $C$. Ví dụ, đây có thể là tập tất cả các tam giác trong mặt phẳng.

Chúng ta giả sử rằng các ví dụ được phân phối độc lập và giống nhau (i.i.d.) theo một phân phối $D$ cố định nhưng không biết. Bài toán học tập được đặt ra như sau. Người học xem xét một tập cố định các khái niệm có thể $H$, gọi là **tập giả thuyết (hypothesis set)**, không nhất thiết phải trùng với $C$. Nó nhận một mẫu $S = (x_1, \ldots, x_m)$ được rút i.i.d. theo $D$ cùng với các nhãn $(c(x_1), \ldots, c(x_m))$, dựa trên một khái niệm mục tiêu cụ thể $c \in C$ cần học. Nhiệm vụ là sử dụng mẫu được gán nhãn $S$ để chọn một giả thuyết $h_S \in H$ có **lỗi khái quát hóa (generalization error)** nhỏ so với khái niệm $c$.

**Định nghĩa 2.1 (Lỗi khái quát hóa)** *Cho một giả thuyết $h \in H$, một khái niệm mục tiêu $c \in C$, và một phân phối nền tảng $D$, **lỗi khái quát hóa** hay **rủi ro (risk)** của $h$ được định nghĩa bởi*

$$R(h) = \Pr_{x \sim D}[h(x) \neq c(x)] = \mathbb{E}_{x \sim D}\bigl[\mathbf{1}_{h(x) \neq c(x)}\bigr], \tag{2.1}$$

*trong đó $\mathbf{1}_\omega$ là hàm chỉ thị của sự kiện $\omega$.*[^1]

Lỗi khái quát hóa của một giả thuyết không thể trực tiếp tiếp cận được bởi người học vì cả phân phối $D$ và khái niệm mục tiêu $c$ đều không biết. Tuy nhiên, người học có thể đo **lỗi thực nghiệm (empirical error)** của một giả thuyết trên mẫu được gán nhãn $S$.

**Định nghĩa 2.2 (Lỗi thực nghiệm)** *Cho một giả thuyết $h \in H$, một khái niệm mục tiêu $c \in C$, và một mẫu $S = (x_1, \ldots, x_m)$, **lỗi thực nghiệm** hay **rủi ro thực nghiệm (empirical risk)** của $h$ được định nghĩa bởi*

$$\hat{R}_S(h) = \frac{1}{m} \sum_{i=1}^{m} \mathbf{1}_{h(x_i) \neq c(x_i)}. \tag{2.2}$$

Như vậy, lỗi thực nghiệm của $h \in H$ là lỗi trung bình của nó trên mẫu $S$, trong khi lỗi khái quát hóa là lỗi kỳ vọng của nó dựa trên phân phối $D$. Chúng ta sẽ thấy trong chương này và các chương tiếp theo một số đảm bảo liên kết hai đại lượng này với xác suất cao, dưới một số giả thuyết tổng quát. Chúng ta có thể đã nhận thấy rằng với $h \in H$ cố định, kỳ vọng của lỗi thực nghiệm dựa trên mẫu i.i.d. $S$ bằng với lỗi khái quát hóa:

$$\mathbb{E}_{S \sim D^m}\bigl[\hat{R}_S(h)\bigr] = R(h). \tag{2.3}$$

Thật vậy, bởi tính tuyến tính của kỳ vọng và thực tế là mẫu được rút i.i.d., ta có thể viết

$$\mathbb{E}_{S \sim D^m}\bigl[\hat{R}_S(h)\bigr] = \frac{1}{m} \sum_{i=1}^{m} \mathbb{E}_{S \sim D^m}\bigl[\mathbf{1}_{h(x_i) \neq c(x_i)}\bigr] = \frac{1}{m} \sum_{i=1}^{m} \mathbb{E}_{x \sim D}\bigl[\mathbf{1}_{h(x) \neq c(x)}\bigr],$$

với mọi $x$ trong mẫu $S$. Do đó,

$$\mathbb{E}_{S \sim D^m}\bigl[\hat{R}_S(h)\bigr] = \mathbb{E}_{S \sim D^m}\bigl[\mathbf{1}_{h(x) \neq c(x)}\bigr] = \mathbb{E}_{x \sim D}\bigl[\mathbf{1}_{h(x) \neq c(x)}\bigr] = R(h).$$

Phần tiếp theo giới thiệu khung học **Probably Approximately Correct (PAC)**. Đặt $n$ là một số sao cho chi phí tính toán để biểu diễn bất kỳ phần tử $x \in \mathcal{X}$ là tối đa $O(n)$ và ký hiệu $\text{size}(c)$ là chi phí tối đa của biểu diễn tính toán của $c \in C$. Ví dụ, $x$ có thể là một vector trong $\mathbb{R}^n$, trong đó chi phí của một biểu diễn dựa trên mảng sẽ là $O(n)$. Ngoài ra, đặt $h_S$ ký hiệu giả thuyết được trả về bởi thuật toán $A$ sau khi nhận mẫu được gán nhãn $S$. Để ký hiệu đơn giản, sự phụ thuộc của $h_S$ vào $A$ không được chỉ định rõ ràng.

**Định nghĩa 2.3 (PAC-learning)** *Một lớp khái niệm $C$ được gọi là **PAC-learnable** (có thể học PAC) nếu tồn tại một thuật toán $A$ và một hàm đa thức $\text{poly}(\cdot, \cdot, \cdot, \cdot)$ sao cho với mọi $\epsilon > 0$ và $\delta > 0$, với mọi phân phối $D$ trên $\mathcal{X}$ và với mọi khái niệm mục tiêu $c \in C$, điều sau đây thỏa mãn với mọi kích thước mẫu $m \geq \text{poly}(1/\epsilon, 1/\delta, n, \text{size}(c))$:*

$$\Pr_{S \sim D^m}[R(h_S) \leq \epsilon] \geq 1 - \delta. \tag{2.4}$$

*Nếu $A$ còn chạy trong thời gian $\text{poly}(1/\epsilon, 1/\delta, n, \text{size}(c))$, thì $C$ được gọi là **efficiently PAC-learnable** (có thể học PAC hiệu quả). Khi thuật toán $A$ như vậy tồn tại, nó được gọi là **PAC-learning algorithm** (thuật toán học PAC) cho $C$.*

Như vậy, một lớp khái niệm $C$ là PAC-learnable nếu giả thuyết trả về bởi thuật toán sau khi quan sát một số điểm đa thức theo $1/\epsilon$ và $1/\delta$ là **xấp xỉ đúng (approximately correct)** (lỗi tối đa $\epsilon$) với **xác suất cao (high probability)** (ít nhất $1 - \delta$), điều này biện minh cho thuật ngữ PAC. Tham số $\delta > 0$ được dùng để định nghĩa **độ tin cậy (confidence)** $1 - \delta$ và $\epsilon > 0$ định nghĩa **độ chính xác (accuracy)** $1 - \epsilon$. Lưu ý rằng nếu thời gian chạy của thuật toán là đa thức theo $1/\epsilon$ và $1/\delta$, thì kích thước mẫu $m$ cũng phải là đa thức nếu thuật toán nhận toàn bộ mẫu.

Một số điểm chính của định nghĩa PAC đáng được nhấn mạnh. Thứ nhất, khung PAC là một **mô hình không phụ thuộc phân phối (distribution-free model)**: không có giả thiết cụ thể nào về phân phối $D$ mà từ đó các ví dụ được rút. Thứ hai, mẫu huấn luyện và các ví dụ kiểm thử dùng để định nghĩa lỗi đều được rút theo cùng phân phối $D$. Đây là giả thiết tự nhiên và cần thiết để khái quát hóa có thể thực hiện được trong trường hợp tổng quát. Nó có thể được nới lỏng để bao gồm các bài toán thích nghi miền thuận lợi. Cuối cùng, khung PAC giải quyết câu hỏi về khả năng học được cho một lớp khái niệm $C$ chứ không phải một khái niệm cụ thể. Lưu ý rằng lớp khái niệm $C$ được biết đến với thuật toán, nhưng tất nhiên khái niệm mục tiêu $c \in C$ là chưa biết.

Trong nhiều trường hợp, đặc biệt khi biểu diễn tính toán của các khái niệm không được thảo luận rõ ràng hoặc là đơn giản, chúng ta có thể bỏ qua sự phụ thuộc đa thức vào $n$ và $\text{size}(c)$ trong định nghĩa PAC và chỉ tập trung vào **độ phức tạp mẫu (sample complexity)**.

Bây giờ chúng ta minh họa PAC-learning với một bài toán học cụ thể.

**Ví dụ 2.4 (Học hình chữ nhật căn chỉnh theo trục)** Xét trường hợp tập các trường hợp là các điểm trong mặt phẳng, $\mathcal{X} = \mathbb{R}^2$, và lớp khái niệm $C$ là tập tất cả các hình chữ nhật căn chỉnh theo trục nằm trong $\mathbb{R}^2$. Như vậy, mỗi khái niệm $c$ là tập các điểm bên trong một hình chữ nhật căn chỉnh theo trục cụ thể. Bài toán học gồm việc xác định với lỗi nhỏ một hình chữ nhật căn chỉnh theo trục mục tiêu sử dụng mẫu huấn luyện được gán nhãn. Chúng ta sẽ chỉ ra rằng lớp khái niệm của các hình chữ nhật căn chỉnh theo trục là PAC-learnable.

Hình 2.1 minh họa bài toán. $R$ biểu diễn hình chữ nhật căn chỉnh theo trục mục tiêu và $R'$ là một giả thuyết. Như có thể thấy từ hình, các vùng lỗi của $R'$ được tạo thành bởi vùng bên trong hình chữ nhật $R$ nhưng bên ngoài hình chữ nhật $R'$ và vùng bên trong $R'$ nhưng bên ngoài hình chữ nhật $R$. Vùng đầu tiên tương ứng với **âm tính giả (false negatives)**, tức là các điểm được gán nhãn 0 hoặc âm bởi $R'$, nhưng thực tế là dương hoặc được gán nhãn 1. Vùng thứ hai tương ứng với **dương tính giả (false positives)**, tức là các điểm được gán nhãn dương bởi $R'$ nhưng thực tế được gán nhãn âm.

Để chỉ ra rằng lớp khái niệm là PAC-learnable, chúng ta mô tả một thuật toán PAC-learning đơn giản $A$. Cho một mẫu được gán nhãn $S$, thuật toán gồm việc trả về hình chữ nhật căn chỉnh theo trục chật nhất $R' = R_S$ chứa các điểm được gán nhãn 1. Hình 2.2 minh họa giả thuyết được trả về bởi thuật toán. Theo định nghĩa, $R_S$ không tạo ra bất kỳ dương tính giả nào, vì các điểm của nó phải được bao gồm trong khái niệm mục tiêu $R$. Do đó, vùng lỗi của $R_S$ được bao gồm trong $R$.

Đặt $R \in C$ là một khái niệm mục tiêu. Cố định $\epsilon > 0$. Đặt $\Pr[R]$ ký hiệu khối lượng xác suất của vùng được định nghĩa bởi $R$, tức là xác suất mà một điểm được rút ngẫu nhiên theo $D$ nằm trong $R$. Vì các lỗi được tạo ra bởi thuật toán của chúng ta chỉ có thể do các điểm nằm bên trong $R$, chúng ta có thể giả sử rằng $\Pr[R] > \epsilon$; nếu không, lỗi của $R_S$ nhỏ hơn hoặc bằng $\epsilon$ bất kể mẫu huấn luyện $S$ nhận được.

Bây giờ, vì $\Pr[R] > \epsilon$, chúng ta có thể định nghĩa bốn vùng hình chữ nhật $r_1, r_2, r_3$, và $r_4$ dọc theo các cạnh của $R$, mỗi vùng có xác suất ít nhất $\epsilon/4$. Những vùng này có thể được xây dựng bằng cách bắt đầu với hình chữ nhật đầy đủ $R$ và sau đó giảm kích thước bằng cách di chuyển một cạnh càng nhiều càng tốt trong khi giữ khối lượng phân phối ít nhất $\epsilon/4$. Hình 2.3 minh họa định nghĩa của các vùng này.

Đặt $l, r, b$, và $t$ là bốn giá trị thực định nghĩa $R$: $R = [l, r] \times [b, t]$. Thì ví dụ, hình chữ nhật bên trái $r_4$ được định nghĩa bởi $r_4 = [l, s_4] \times [b, t]$, với $s_4 = \inf\{s : \Pr[[l, s] \times [b, t]] \geq \epsilon/4\}$. Không khó để thấy rằng xác suất của vùng $\tilde{r}_4 = [l, s_4[ \times [b, t]$ thu được từ $r_4$ bằng cách loại trừ cạnh ngoài cùng bên phải là tối đa $\epsilon/4$. $r_1, r_2, r_3$ và $\tilde{r}_1, \tilde{r}_2, \tilde{r}_3$ được định nghĩa theo cách tương tự.

Quan sát rằng nếu $R_S$ gặp tất cả bốn vùng này $r_i$, $i \in [4]$, thì vì nó là một hình chữ nhật, nó sẽ có một cạnh trong mỗi vùng này (lập luận hình học). Vùng lỗi của nó, là phần của $R$ mà nó không bao phủ, do đó được bao gồm trong hợp các vùng $\tilde{r}_i$, $i \in [4]$, và không thể có khối lượng xác suất nhiều hơn $\epsilon$.

Bằng phản chứng, nếu $R(R_S) > \epsilon$, thì $R_S$ phải bỏ lỡ ít nhất một trong các vùng $r_i$, $i \in [4]$. Kết quả là, ta có thể viết

$$\Pr_{S \sim D^m}[R(R_S) > \epsilon] \leq \Pr_{S \sim D^m}\left[\bigcup_{i=1}^{4}\{R_S \cap r_i = \emptyset\}\right]$$

$$\leq \sum_{i=1}^{4} \Pr_{S \sim D^m}[\{R_S \cap r_i = \emptyset\}] \quad \text{(bởi bất đẳng thức hội)}$$

$$\leq 4(1 - \epsilon/4)^m \quad \text{(vì } \Pr[r_i] \geq \epsilon/4\text{)}$$

$$\leq 4\exp(-m\epsilon/4), \tag{2.5}$$

trong đó ở bước cuối chúng ta sử dụng bất đẳng thức tổng quát $1 - x \leq e^{-x}$ hợp lệ với mọi $x \in \mathbb{R}$. Với mọi $\delta > 0$, để đảm bảo rằng $\Pr_{S \sim D^m}[R(R_S) > \epsilon] \leq \delta$, ta có thể áp đặt

$$4\exp(-\epsilon m/4) \leq \delta \iff m \geq \frac{4}{\epsilon} \log \frac{4}{\delta}. \tag{2.6}$$

Như vậy, với mọi $\epsilon > 0$ và $\delta > 0$, nếu kích thước mẫu $m$ lớn hơn $\frac{4}{\epsilon} \log \frac{4}{\delta}$, thì $\Pr_{S \sim D^m}[R(R_S) > \epsilon] \leq \delta$. Hơn nữa, chi phí tính toán của biểu diễn các điểm trong $\mathbb{R}^2$ và các hình chữ nhật căn chỉnh theo trục, có thể được định nghĩa bởi bốn góc của chúng, là hằng số. Điều này chứng minh rằng lớp khái niệm của các hình chữ nhật căn chỉnh theo trục là PAC-learnable và độ phức tạp mẫu của PAC-learning hình chữ nhật căn chỉnh theo trục là $O\!\left(\frac{1}{\epsilon} \log \frac{1}{\delta}\right)$.

Một cách tương đương để trình bày các kết quả độ phức tạp mẫu như (2.6), mà chúng ta sẽ thường thấy xuyên suốt cuốn sách này, là đưa ra một **cận khái quát hóa (generalization bound)**. Một cận khái quát hóa phát biểu rằng với xác suất ít nhất $1 - \delta$, $R(R_S)$ bị cận trên bởi một đại lượng nào đó phụ thuộc vào kích thước mẫu $m$ và $\delta$. Để đạt được điều này, ta chỉ cần đặt $\delta$ bằng cận trên được suy ra trong (2.5), tức là $\delta = 4\exp(-m\epsilon/4)$ và giải cho $\epsilon$. Điều này cho kết quả là với xác suất ít nhất $1 - \delta$, lỗi của thuật toán bị cận như sau:

$$R(R_S) \leq \frac{4}{m} \log \frac{4}{\delta}. \tag{2.7}$$

Các thuật toán PAC-learning khác có thể được xem xét cho ví dụ này. Một lựa chọn thay thế là trả về hình chữ nhật căn chỉnh theo trục lớn nhất không chứa các điểm âm, chẳng hạn. Bằng chứng về PAC-learning vừa trình bày cho hình chữ nhật căn chỉnh theo trục chật nhất có thể dễ dàng được chuyển thể sang phân tích các thuật toán khác như vậy.

Lưu ý rằng tập giả thuyết $H$ mà chúng ta xem xét trong ví dụ này trùng với lớp khái niệm $C$ và lực lượng của nó là vô hạn. Tuy nhiên, bài toán đã có một bằng chứng đơn giản về PAC-learning. Chúng ta có thể đặt câu hỏi liệu một bằng chứng tương tự có thể áp dụng sẵn sàng cho các lớp khái niệm tương tự khác không. Điều này không đơn giản vì lập luận hình học cụ thể được sử dụng trong bằng chứng là trọng yếu. Việc mở rộng bằng chứng sang các lớp khái niệm khác như vòng tròn không đồng tâm là không tầm thường (xem bài tập 2.4). Do đó, chúng ta cần một kỹ thuật bằng chứng tổng quát hơn và các kết quả tổng quát hơn. Hai phần tiếp theo cung cấp cho chúng ta những công cụ như vậy trong trường hợp tập giả thuyết hữu hạn.

---

[^1]: Việc chọn $R$ thay vì $E$ để ký hiệu lỗi tránh nhầm lẫn có thể xảy ra với ký hiệu kỳ vọng và được biện minh thêm bởi thực tế là thuật ngữ *rủi ro (risk)* cũng được sử dụng trong học máy và thống kê để chỉ lỗi.

---

## 2.2 Đảm Bảo Cho Tập Giả Thuyết Hữu Hạn — Trường Hợp Nhất Quán (Guarantees for Finite Hypothesis Sets — Consistent Case)

Trong ví dụ về hình chữ nhật căn chỉnh theo trục mà chúng ta đã xem xét, giả thuyết $h_S$ được trả về bởi thuật toán luôn **nhất quán (consistent)**, tức là không có lỗi nào trên mẫu huấn luyện $S$. Trong phần này, chúng ta trình bày một cận độ phức tạp mẫu tổng quát, hoặc tương đương, một cận khái quát hóa, cho các giả thuyết nhất quán, trong trường hợp lực lượng $|H|$ của tập giả thuyết là hữu hạn. Vì chúng ta xem xét các giả thuyết nhất quán, chúng ta sẽ giả sử rằng khái niệm mục tiêu $c$ nằm trong $H$.

**Định lý 2.5 (Cận học — $H$ hữu hạn, trường hợp nhất quán)** *Đặt $H$ là một tập hữu hạn các hàm ánh xạ từ $\mathcal{X}$ sang $\mathcal{Y}$. Đặt $A$ là thuật toán mà với mọi khái niệm mục tiêu $c \in H$ và mẫu i.i.d. $S$ trả về một giả thuyết nhất quán $h_S$: $\hat{R}_S(h_S) = 0$. Thì với mọi $\epsilon, \delta > 0$, bất đẳng thức $\Pr_{S \sim D^m}[R(h_S) \leq \epsilon] \geq 1 - \delta$ thỏa mãn nếu*

$$m \geq \frac{1}{\epsilon}\left(\log |H| + \log \frac{1}{\delta}\right). \tag{2.8}$$

*Kết quả về độ phức tạp mẫu này có phát biểu tương đương như sau dưới dạng cận khái quát hóa: với mọi $\epsilon, \delta > 0$, với xác suất ít nhất $1 - \delta$,*

$$R(h_S) \leq \frac{1}{m}\left(\log |H| + \log \frac{1}{\delta}\right). \tag{2.9}$$

**Chứng minh:** Cố định $\epsilon > 0$. Chúng ta không biết giả thuyết nhất quán $h_S \in H$ nào được chọn bởi thuật toán $A$. Giả thuyết này còn phụ thuộc vào mẫu huấn luyện $S$. Do đó, chúng ta cần đưa ra một **cận hội tụ đồng đều (uniform convergence bound)**, tức là một cận áp dụng cho tập tất cả các giả thuyết nhất quán, mà điều này tiên nhiên bao gồm $h_S$. Như vậy, chúng ta sẽ cận xác suất mà một $h \in H$ nào đó nhất quán và có lỗi lớn hơn $\epsilon$. Với mọi $\epsilon > 0$, định nghĩa $H_\epsilon$ bởi $H_\epsilon = \{h \in H : R(h) > \epsilon\}$. Xác suất để một giả thuyết $h \in H_\epsilon$ nhất quán trên mẫu huấn luyện $S$ được rút i.i.d., tức là không có lỗi trên bất kỳ điểm nào trong $S$, có thể được cận như sau:

$$\Pr\bigl[\hat{R}_S(h) = 0\bigr] \leq (1 - \epsilon)^m.$$

Như vậy, bởi bất đẳng thức hội (union bound), điều sau đây thỏa mãn:

$$\Pr\bigl[\exists h \in H_\epsilon : \hat{R}_S(h) = 0\bigr] = \Pr\bigl[\hat{R}_S(h_1) = 0 \vee \cdots \vee \hat{R}_S(h_{|H_\epsilon|}) = 0\bigr]$$

$$\leq \sum_{h \in H_\epsilon} \Pr\bigl[\hat{R}_S(h) = 0\bigr] \quad \text{(bất đẳng thức hội)}$$

$$\leq \sum_{h \in H_\epsilon} (1 - \epsilon)^m \leq |H|(1 - \epsilon)^m \leq |H|e^{-m\epsilon}.$$

Đặt vế phải bằng $\delta$ và giải cho $\epsilon$ kết thúc chứng minh. $\square$

Định lý chỉ ra rằng khi tập giả thuyết $H$ là hữu hạn, một thuật toán nhất quán $A$ là thuật toán PAC-learning, vì độ phức tạp mẫu được cho bởi (2.8) được chi phối bởi một đa thức trong $1/\epsilon$ và $1/\delta$. Như được chỉ ra bởi (2.9), lỗi khái quát hóa của các giả thuyết nhất quán bị cận trên bởi một số hạng giảm theo hàm của kích thước mẫu $m$. Đây là một sự thật tổng quát: như mong đợi, các thuật toán học được lợi từ các tập huấn luyện được gán nhãn lớn hơn. Tuy nhiên, tốc độ giảm $O(1/m)$ được đảm bảo bởi định lý này là đặc biệt thuận lợi.

Cái giá phải trả cho việc đưa ra một thuật toán nhất quán là sử dụng một tập giả thuyết $H$ lớn hơn chứa các khái niệm mục tiêu. Tất nhiên, cận trên (2.9) tăng theo $|H|$. Tuy nhiên, sự phụ thuộc đó chỉ là logarithmics. Lưu ý rằng số hạng $\log |H|$, hoặc số hạng liên quan $\log_2 |H|$ khác nó một hệ số hằng, có thể được hiểu là số bit cần thiết để biểu diễn $H$. Do đó, đảm bảo khái quát hóa của định lý được kiểm soát bởi tỷ lệ giữa số lượng bit này, $\log_2 |H|$, và kích thước mẫu $m$.

Bây giờ chúng ta sử dụng định lý 2.5 để phân tích PAC-learning với các lớp khái niệm khác nhau.

**Ví dụ 2.6 (Hội của các literal Boolean)** Xét học lớp khái niệm $C_n$ của các hội (conjunction) của tối đa $n$ literal Boolean $x_1, \ldots, x_n$. Một **literal Boolean** là hoặc một biến $x_i$, $i \in [n]$, hoặc phủ định của nó $\bar{x}_i$. Với $n = 4$, một ví dụ là hội: $x_1 \wedge \bar{x}_2 \wedge x_4$, trong đó $\bar{x}_2$ ký hiệu phủ định của literal Boolean $x_2$. $(1, 0, 0, 1)$ là một ví dụ dương cho khái niệm này trong khi $(1, 0, 0, 0)$ là một ví dụ âm.

Quan sát rằng với $n = 4$, một ví dụ dương $(1, 0, 1, 0)$ ngụ ý rằng khái niệm mục tiêu không thể chứa các literal $\bar{x}_1$ và $\bar{x}_3$ và không thể chứa các literal $x_2$ và $x_4$. Ngược lại, một ví dụ âm không có nhiều thông tin như vậy vì không biết bit nào trong số $n$ bit của nó là sai. Một thuật toán đơn giản để tìm một giả thuyết nhất quán do đó dựa trên các ví dụ dương và bao gồm: với mỗi ví dụ dương $(b_1, \ldots, b_n)$ và $i \in [n]$, nếu $b_i = 1$ thì $\bar{x}_i$ bị loại trừ khỏi các literal có thể trong lớp khái niệm và nếu $b_i = 0$ thì $x_i$ bị loại trừ. Hội của tất cả các literal chưa bị loại trừ do đó là một giả thuyết nhất quán với mục tiêu. Hình 2.4 cho thấy một mẫu huấn luyện mẫu cũng như một giả thuyết nhất quán cho trường hợp $n = 6$.

Chúng ta có $|H| = |C_n| = 3^n$, vì mỗi literal có thể được bao gồm dương, với phủ định, hoặc không được bao gồm. Thay vào cận độ phức tạp mẫu cho các giả thuyết nhất quán cho kết quả sau cho mọi $\epsilon > 0$ và $\delta > 0$:

$$m \geq \frac{1}{\epsilon}\left((\log 3)n + \log \frac{1}{\delta}\right). \tag{2.10}$$

Như vậy, lớp các hội của tối đa $n$ literal Boolean là PAC-learnable. Lưu ý rằng độ phức tạp tính toán cũng là đa thức, vì chi phí huấn luyện mỗi ví dụ là $O(n)$. Với $\delta = 0.02$, $\epsilon = 0.1$, và $n = 10$, cận trở thành $m \geq 149$. Như vậy, với mẫu được gán nhãn ít nhất 149 ví dụ, cận đảm bảo độ chính xác 90% với độ tin cậy ít nhất 98%.

**Ví dụ 2.7 (Lớp khái niệm vũ trụ)** Xét tập $\mathcal{X} = \{0, 1\}^n$ tất cả các vector Boolean có $n$ thành phần, và đặt $U_n$ là lớp khái niệm được tạo thành bởi tất cả các tập con của $\mathcal{X}$. Lớp khái niệm này có PAC-learnable không? Để đảm bảo một giả thuyết nhất quán, lớp giả thuyết phải bao gồm lớp khái niệm, do đó $|H| \geq |U_n| = 2^{(2^n)}$. Định lý 2.5 đưa ra cận độ phức tạp mẫu sau:

$$m \geq \frac{1}{\epsilon}\left((\log 2)2^n + \log \frac{1}{\delta}\right). \tag{2.11}$$

Ở đây, số mẫu huấn luyện cần thiết là hàm mũ trong $n$, là chi phí biểu diễn một điểm trong $\mathcal{X}$. Do đó, PAC-learning không được đảm bảo bởi định lý. Thực ra, không khó để chỉ ra rằng lớp khái niệm vũ trụ này là không PAC-learnable.

**Ví dụ 2.8 (Công thức DNF $k$-số hạng)** Một **công thức dạng chuẩn tách rời (disjunctive normal form — DNF)** là một công thức được viết dưới dạng tách rời (disjunction) của nhiều số hạng, mỗi số hạng là một hội của các literal Boolean. Một **$k$-term DNF** là một công thức DNF được định nghĩa bởi tách rời của $k$ số hạng, mỗi số hạng là hội của tối đa $n$ literal Boolean. Như vậy, với $k = 2$ và $n = 3$, một ví dụ về $k$-term DNF là $(x_1 \wedge x_2 \wedge x_3) \vee (x_1 \wedge \bar{x}_3)$.

Lớp $C$ các công thức $k$-term DNF có PAC-learnable không? Lực lượng của lớp là $3^{nk}$, vì mỗi số hạng là hội của tối đa $n$ biến và có $3^n$ hội như vậy, như đã thấy trước đây. Tập giả thuyết $H$ phải chứa $C$ để nhất quán có thể, do đó $|H| \geq 3^{nk}$. Định lý 2.5 đưa ra cận độ phức tạp mẫu sau:

$$m \geq \frac{1}{\epsilon}\left((\log 3)nk + \log \frac{1}{\delta}\right), \tag{2.12}$$

là đa thức. Tuy nhiên, có thể chỉ ra bằng cách rút gọn từ bài toán tô màu đồ thị 3 màu (graph 3-coloring) rằng bài toán học $k$-term DNF, ngay cả với $k = 3$, là không PAC-learnable hiệu quả, trừ khi $\text{RP}$, lớp độ phức tạp của các bài toán có nghiệm quyết định đa thức ngẫu nhiên, trùng với $\text{NP}$ ($\text{RP} = \text{NP}$), điều thường được cho là không phải trường hợp. Như vậy, trong khi kích thước mẫu cần thiết để học $k$-term DNF chỉ là đa thức, PAC-learning hiệu quả của lớp này là không thể nếu $\text{RP} \neq \text{NP}$.

**Ví dụ 2.9 (Công thức $k$-CNF)** Một **công thức dạng chuẩn hội (conjunctive normal form — CNF)** là một hội của các tách rời. Một **$k$-CNF** là một biểu thức có dạng $T_1 \wedge \ldots \wedge T_j$ với độ dài $j \in \mathbb{N}$ tùy ý và mỗi số hạng $T_i$ là tách rời của tối đa $k$ thuộc tính Boolean.

Bài toán học công thức $k$-CNF có thể được rút gọn về bài toán học hội của các literal Boolean, mà như đã thấy trước đây, là một lớp khái niệm PAC-learnable. Điều này có thể được thực hiện với chi phí giới thiệu $(2n)^k$ biến mới $Y_{u_1, \ldots, u_k}$ sử dụng phép song ánh sau:

$$(u_1, \ldots, u_k) \to Y_{u_1, \ldots, u_k}, \tag{2.13}$$

trong đó $u_1, \ldots, u_k$ là các literal Boolean trên các biến gốc $x_1, \ldots, x_n$. Giá trị của $Y_{u_1, \ldots, u_k}$ được xác định bởi $Y_{u_1, \ldots, u_k} = u_1 \vee \cdots \vee u_k$. Sử dụng ánh xạ này, mẫu huấn luyện ban đầu có thể được chuyển đổi thành một mẫu được định nghĩa theo các biến mới và bất kỳ công thức $k$-CNF nào trên các biến gốc đều có thể được viết dưới dạng một hội theo các biến $Y_{u_1, \ldots, u_k}$. Việc rút gọn này về PAC-learning của hội các literal Boolean có thể ảnh hưởng đến phân phối ban đầu của các ví dụ, nhưng đây không phải là vấn đề vì trong khung PAC không có giả thiết nào về phân phối. Do đó, sử dụng phép biến đổi này, khả năng PAC-learnable của hội các literal Boolean ngụ ý khả năng PAC-learnable của công thức $k$-CNF.

Tuy nhiên, đây là một kết quả đáng ngạc nhiên, vì bất kỳ công thức $k$-term DNF nào cũng có thể được viết dưới dạng công thức $k$-CNF. Thật vậy, sử dụng tính kết hợp, một $k$-term DNF $T_1 \vee \cdots \vee T_k$ với $T_i = u_{i,1} \wedge \cdots \wedge u_{i,n_i}$ cho $i \in [k]$ có thể được viết lại thành công thức $k$-CNF thông qua

$$\bigvee_{i=1}^{k} u_{i,1} \wedge \cdots \wedge u_{i,n_i} = \bigwedge_{j_1 \in [n_1], \ldots, j_k \in [n_k]} u_{1,j_1} \vee \cdots \vee u_{k,j_k}.$$

Để minh họa việc viết lại này trong một trường hợp cụ thể, quan sát rằng ví dụ:

$$(u_1 \wedge u_2 \wedge u_3) \vee (v_1 \wedge v_2 \wedge v_3) = \bigwedge_{i,j=1}^{3} (u_i \vee v_j).$$

Nhưng, như chúng ta đã thấy trước đây, các công thức $k$-term DNF là không PAC-learnable hiệu quả nếu $\text{RP} \neq \text{NP}$! Điều gì có thể giải thích sự không nhất quán rõ ràng này? Vấn đề là việc chuyển đổi thành $k$-term DNF một công thức $k$-CNF mà chúng ta đã học (tương đương với $k$-term DNF) nhìn chung là không khả thi trong thời gian đa thức (intractable) nếu $\text{RP} \neq \text{NP}$.

Ví dụ này tiết lộ một số khía cạnh chính của PAC-learning, bao gồm chi phí biểu diễn một khái niệm và việc lựa chọn tập giả thuyết. Với một lớp khái niệm cố định, việc học có thể không khả thi hay khả thi tùy thuộc vào lựa chọn biểu diễn.

---

## 2.3 Đảm Bảo Cho Tập Giả Thuyết Hữu Hạn — Trường Hợp Không Nhất Quán (Guarantees for Finite Hypothesis Sets — Inconsistent Case)

Trong trường hợp tổng quát nhất, có thể không có giả thuyết nào trong $H$ nhất quán với mẫu huấn luyện được gán nhãn. Thực ra, đây là trường hợp điển hình trong thực tế, khi các bài toán học có thể phần nào khó khăn hoặc các lớp khái niệm phức tạp hơn tập giả thuyết được sử dụng bởi thuật toán học. Tuy nhiên, các giả thuyết không nhất quán với số lỗi nhỏ trên mẫu huấn luyện có thể hữu ích và, như chúng ta sẽ thấy, có thể được hưởng lợi từ các đảm bảo thuận lợi dưới một số giả thuyết. Phần này trình bày các đảm bảo học chính xác cho trường hợp không nhất quán này và tập giả thuyết hữu hạn.

Để suy ra các đảm bảo học trong thiết lập tổng quát hơn này, chúng ta sẽ sử dụng **bất đẳng thức Hoeffding (Hoeffding's inequality)** (định lý D.2) hoặc hệ quả sau, liên kết lỗi khái quát hóa và lỗi thực nghiệm của một giả thuyết đơn.

**Hệ quả 2.10** Cố định $\epsilon > 0$. Thì với mọi giả thuyết $h : \mathcal{X} \to \{0, 1\}$, các bất đẳng thức sau đây thỏa mãn:

$$\Pr_{S \sim D^m}\bigl[\hat{R}_S(h) - R(h) \geq \epsilon\bigr] \leq \exp(-2m\epsilon^2) \tag{2.14}$$

$$\Pr_{S \sim D^m}\bigl[\hat{R}_S(h) - R(h) \leq -\epsilon\bigr] \leq \exp(-2m\epsilon^2). \tag{2.15}$$

Bởi bất đẳng thức hội, điều này ngụ ý bất đẳng thức hai phía sau:

$$\Pr_{S \sim D^m}\bigl[|\hat{R}_S(h) - R(h)| \geq \epsilon\bigr] \leq 2\exp(-2m\epsilon^2). \tag{2.16}$$

**Chứng minh:** Kết quả suy ra ngay từ định lý D.2. $\square$

Đặt vế phải của (2.16) bằng $\delta$ và giải cho $\epsilon$ ngay bán ra cận sau cho một giả thuyết đơn.

**Hệ quả 2.11 (Cận khái quát hóa — giả thuyết đơn)** Cố định một giả thuyết $h : \mathcal{X} \to \{0, 1\}$. Thì với mọi $\delta > 0$, bất đẳng thức sau đây thỏa mãn với xác suất ít nhất $1 - \delta$:

$$R(h) \leq \hat{R}_S(h) + \sqrt{\frac{\log \frac{2}{\delta}}{2m}}. \tag{2.17}$$

Ví dụ sau minh họa hệ quả này trong một trường hợp đơn giản.

**Ví dụ 2.12 (Tung đồng xu)** Hãy tưởng tượng tung một đồng xu lệch đầu xuất hiện với xác suất $p$, và đặt giả thuyết của chúng ta là giả thuyết luôn đoán mặt sấp. Thì tỷ lệ lỗi thực là $R(h) = p$ và tỷ lệ lỗi thực nghiệm $\hat{R}_S(h) = \hat{p}$, trong đó $\hat{p}$ là xác suất thực nghiệm của mặt ngửa dựa trên mẫu huấn luyện được rút i.i.d. Do đó, hệ quả 2.11 đảm bảo với xác suất ít nhất $1 - \delta$ rằng

$$|p - \hat{p}| \leq \sqrt{\frac{\log \frac{2}{\delta}}{2m}}. \tag{2.18}$$

Do đó, nếu chúng ta chọn $\delta = 0.02$ và sử dụng mẫu kích thước 500, với xác suất ít nhất 98%, chất lượng xấp xỉ sau được đảm bảo cho $\hat{p}$:

$$|p - \hat{p}| \leq \sqrt{\frac{\log(100)}{1000}} \approx 0.048. \tag{2.19}$$

Có thể áp dụng trực tiếp hệ quả 2.11 để cận lỗi khái quát hóa của giả thuyết $h_S$ được trả về bởi thuật toán học khi huấn luyện trên mẫu $S$ không? Không, vì $h_S$ không phải là một giả thuyết cố định, mà là một biến ngẫu nhiên phụ thuộc vào mẫu huấn luyện $S$ được rút. Cũng lưu ý rằng không giống trường hợp giả thuyết cố định mà kỳ vọng của lỗi thực nghiệm là lỗi khái quát hóa (phương trình (2.3)), lỗi khái quát hóa $R(h_S)$ là một biến ngẫu nhiên và nhìn chung khác với kỳ vọng $\mathbb{E}[\hat{R}_S(h_S)]$, là một hằng số.

Như vậy, cũng như trong bằng chứng cho trường hợp nhất quán, chúng ta cần suy ra một cận hội tụ đồng đều, tức là một cận thỏa mãn với xác suất cao cho tất cả các giả thuyết $h \in H$.

**Định lý 2.13 (Cận học — $H$ hữu hạn, trường hợp không nhất quán)** *Đặt $H$ là một tập giả thuyết hữu hạn. Thì với mọi $\delta > 0$, với xác suất ít nhất $1 - \delta$, bất đẳng thức sau đây thỏa mãn:*

$$\forall h \in H, \quad R(h) \leq \hat{R}_S(h) + \sqrt{\frac{\log |H| + \log \frac{2}{\delta}}{2m}}. \tag{2.20}$$

**Chứng minh:** Đặt $h_1, \ldots, h_{|H|}$ là các phần tử của $H$. Sử dụng bất đẳng thức hội và áp dụng hệ quả 2.11 cho mỗi giả thuyết cho:

$$\Pr\bigl[\exists h \in H \: |\hat{R}_S(h) - R(h)| > \epsilon\bigr]$$

$$= \Pr\bigl[|\hat{R}_S(h_1) - R(h_1)| > \epsilon \vee \ldots \vee |\hat{R}_S(h_{|H|}) - R(h_{|H|})| > \epsilon\bigr]$$

$$\leq \sum_{h \in H} \Pr\bigl[|\hat{R}_S(h) - R(h)| > \epsilon\bigr]$$

$$\leq 2|H|\exp(-2m\epsilon^2).$$

Đặt vế phải bằng $\delta$ kết thúc chứng minh. $\square$

Như vậy, với tập giả thuyết hữu hạn $H$,

$$R(h) \leq \hat{R}_S(h) + O\!\left(\sqrt{\frac{\log_2 |H|}{m}}\right).$$

Như đã được chỉ ra, $\log_2 |H|$ có thể được hiểu là số bit cần thiết để biểu diễn $H$. Một số nhận xét tương tự như những nhận xét đã đưa ra về cận khái quát hóa trong trường hợp nhất quán có thể được đưa ra ở đây: kích thước mẫu $m$ lớn hơn đảm bảo khái quát hóa tốt hơn, và cận tăng theo $|H|$ nhưng chỉ logarithmically. Nhưng ở đây, cận là hàm kém thuận lợi hơn của $\frac{\log_2 |H|}{m}$; nó biến thiên theo căn bậc hai của số hạng này. Đây không phải là cái giá nhỏ: để có cùng đảm bảo như trong trường hợp nhất quán, cần một mẫu được gán nhãn lớn hơn theo bậc hai.

Lưu ý rằng cận gợi ý tìm kiếm sự đánh đổi giữa việc giảm lỗi thực nghiệm và kiểm soát kích thước của tập giả thuyết: một tập giả thuyết lớn hơn bị phạt bởi số hạng thứ hai nhưng có thể giúp giảm lỗi thực nghiệm, tức là số hạng đầu tiên. Nhưng, với lỗi thực nghiệm tương tự, nó gợi ý sử dụng tập giả thuyết nhỏ hơn. Điều này có thể được xem như một phiên bản của nguyên lý gọi là **Dao cạo Occam (Occam's Razor)** được đặt theo tên nhà thần học William of Occam: *Đa số không nên được đặt ra mà không cần thiết*, cũng được diễn đạt lại là *giải thích đơn giản nhất là tốt nhất*. Trong bối cảnh này, nó có thể được biểu đạt như sau: Khi mọi thứ khác bằng nhau, tập giả thuyết đơn giản hơn (nhỏ hơn) là tốt hơn.

---

## 2.4 Tổng Quát (Generalities)

Trong phần này chúng ta sẽ thảo luận một số khía cạnh tổng quát của kịch bản học, mà để đơn giản, chúng ta đã bỏ qua trong thảo luận của các phần trước.

### 2.4.1 Kịch Bản Tất Định và Ngẫu Nhiên (Deterministic versus Stochastic Scenarios)

Trong kịch bản tổng quát nhất của học có giám sát, phân phối $D$ được định nghĩa trên $\mathcal{X} \times \mathcal{Y}$, và dữ liệu huấn luyện là mẫu được gán nhãn $S$ được rút i.i.d. theo $D$:

$$S = ((x_1, y_1), \ldots, (x_m, y_m)).$$

Bài toán học là tìm một giả thuyết $h \in H$ với lỗi khái quát hóa nhỏ

$$R(h) = \Pr_{(x,y) \sim D}[h(x) \neq y] = \mathbb{E}_{(x,y) \sim D}[\mathbf{1}_{h(x) \neq y}].$$

Kịch bản tổng quát hơn này được gọi là **kịch bản ngẫu nhiên (stochastic scenario)**. Trong thiết lập này, nhãn đầu ra là hàm xác suất của đầu vào. Kịch bản ngẫu nhiên nắm bắt nhiều bài toán thực tế trong đó nhãn của một điểm đầu vào không duy nhất. Ví dụ, nếu chúng ta muốn dự đoán giới tính dựa trên các cặp đầu vào được tạo thành bởi chiều cao và cân nặng của một người, thì nhãn thường không duy nhất. Với hầu hết các cặp, cả nam và nữ đều là giới tính có thể. Với mỗi cặp cố định, sẽ có một phân phối xác suất về nhãn là nam.

Phần mở rộng tự nhiên của khung PAC-learning sang thiết lập này được gọi là **agnostic PAC-learning**.

**Định nghĩa 2.14 (Agnostic PAC-learning)** *Đặt $H$ là tập giả thuyết. $A$ là thuật toán agnostic PAC-learning nếu tồn tại một hàm đa thức $\text{poly}(\cdot, \cdot, \cdot, \cdot)$ sao cho với mọi $\epsilon > 0$ và $\delta > 0$, với mọi phân phối $D$ trên $\mathcal{X} \times \mathcal{Y}$, điều sau đây thỏa mãn với mọi kích thước mẫu $m \geq \text{poly}(1/\epsilon, 1/\delta, n, \text{size}(c))$:*

$$\Pr_{S \sim D^m}\left[R(h_S) - \min_{h \in H} R(h) \leq \epsilon\right] \geq 1 - \delta. \tag{2.21}$$

*Nếu $A$ còn chạy trong thời gian $\text{poly}(1/\epsilon, 1/\delta, n)$, thì nó được gọi là thuật toán agnostic PAC-learning hiệu quả.*

Khi nhãn của một điểm có thể được xác định duy nhất bởi một số hàm đo được $f : \mathcal{X} \to \mathcal{Y}$ (với xác suất một), thì kịch bản được gọi là **tất định (deterministic)**. Trong trường hợp đó, ta chỉ cần xem xét phân phối $D$ trên không gian đầu vào. Mẫu huấn luyện được thu thập bằng cách rút $(x_1, \ldots, x_m)$ theo $D$ và các nhãn được thu thập thông qua $f$: $y_i = f(x_i)$ với mọi $i \in [m]$. Nhiều bài toán học có thể được hình thức hóa trong kịch bản tất định này.

Trong các phần trước, cũng như trong hầu hết tài liệu được trình bày trong cuốn sách này, chúng ta đã giới hạn trình bày của mình trong kịch bản tất định để đơn giản. Tuy nhiên, với tất cả tài liệu này, phần mở rộng sang kịch bản ngẫu nhiên sẽ đơn giản đối với người đọc.

### 2.4.2 Lỗi Bayes và Nhiễu (Bayes Error and Noise)

Trong trường hợp tất định, theo định nghĩa, tồn tại một hàm mục tiêu $f$ với không có lỗi khái quát hóa: $R(h) = 0$. Trong trường hợp ngẫu nhiên, có một lỗi tối thiểu khác không cho bất kỳ giả thuyết nào.

**Định nghĩa 2.15 (Lỗi Bayes)** *Cho một phân phối $D$ trên $\mathcal{X} \times \mathcal{Y}$, **lỗi Bayes** $R^*$ được định nghĩa là giá trị infimum của các lỗi đạt được bởi các hàm đo được $h : \mathcal{X} \to \mathcal{Y}$:*

$$R^* = \inf_{h \text{ đo được}} R(h). \tag{2.22}$$

*Một giả thuyết $h$ với $R(h) = R^*$ được gọi là **giả thuyết Bayes (Bayes hypothesis)** hay **bộ phân loại Bayes (Bayes classifier)**.*

Theo định nghĩa, trong trường hợp tất định, ta có $R^* = 0$, nhưng trong trường hợp ngẫu nhiên, $R^* \neq 0$. Rõ ràng, bộ phân loại Bayes $h_\text{Bayes}$ có thể được định nghĩa theo các xác suất có điều kiện là:

$$\forall x \in \mathcal{X}, \quad h_\text{Bayes}(x) = \operatorname*{argmax}_{y \in \{0,1\}} \Pr[y | x]. \tag{2.23}$$

Lỗi trung bình được tạo ra bởi $h_\text{Bayes}$ tại $x \in \mathcal{X}$ là $\min\{\Pr[0|x], \Pr[1|x]\}$, và đây là lỗi tối thiểu có thể. Điều này dẫn đến định nghĩa nhiễu sau.

**Định nghĩa 2.16 (Nhiễu)** *Cho một phân phối $D$ trên $\mathcal{X} \times \mathcal{Y}$, **nhiễu** tại điểm $x \in \mathcal{X}$ được định nghĩa bởi*

$$\text{noise}(x) = \min\{\Pr[1|x], \Pr[0|x]\}. \tag{2.24}$$

*Nhiễu trung bình hay nhiễu liên quan đến $D$ là $\mathbb{E}[\text{noise}(x)]$.*

Như vậy, nhiễu trung bình chính xác là lỗi Bayes: $\text{noise} = \mathbb{E}[\text{noise}(x)] = R^*$. Nhiễu là một đặc điểm của bài toán học, chỉ mức độ khó của nó. Một điểm $x \in \mathcal{X}$ mà $\text{noise}(x)$ gần bằng $1/2$ đôi khi được gọi là nhiễu và tất nhiên là thách thức cho dự đoán chính xác.

---

## 2.5 Phụ Chú Chương (Chapter Notes)

Khung học PAC được giới thiệu bởi Valiant [1984]. Cuốn sách của Kearns và Vazirani [1994] là tài liệu tham khảo xuất sắc đề cập đến hầu hết các khía cạnh của PAC-learning và một số câu hỏi nền tảng khác trong học máy. Ví dụ về học hình chữ nhật căn chỉnh theo trục của chúng ta, cũng được thảo luận trong tài liệu tham khảo đó, ban đầu là do Blumer et al. [1989].

Khung học PAC là một khung tính toán vì nó tính đến chi phí của các biểu diễn tính toán và độ phức tạp thời gian của thuật toán học. Nếu chúng ta bỏ qua các khía cạnh tính toán, nó tương tự với khung học được xem xét trước đó bởi Vapnik và Chervonenkis [xem Vapnik, 2000].

Định nghĩa về nhiễu được trình bày trong chương này có thể được tổng quát hóa sang các hàm mất mát tùy ý (xem bài tập 2.14).

Nguyên lý Dao cạo Occam được viện dẫn trong nhiều bối cảnh khác nhau, chẳng hạn như trong ngôn ngữ học để biện minh cho tính ưu việt của một tập quy tắc hay cú pháp. Độ phức tạp Kolmogorov có thể được xem là khung tương ứng trong lý thuyết thông tin. Trong bối cảnh các đảm bảo học được trình bày trong chương này, nguyên lý gợi ý chọn giải thích tiết kiệm nhất (tập giả thuyết có lực lượng nhỏ nhất). Chúng ta sẽ thấy trong các phần tiếp theo các ứng dụng khác của nguyên lý này với các khái niệm đơn giản hay phức tạp khác nhau.

---

## 2.6 Bài Tập (Exercises)

**2.1 Biến thể hai-oracle của mô hình PAC.** Giả sử rằng các ví dụ dương và âm bây giờ được rút từ hai phân phối riêng biệt $D_+$ và $D_-$. Để đạt độ chính xác $(1 - \epsilon)$, thuật toán học phải tìm một giả thuyết $h$ sao cho:

$$\Pr_{x \sim D_+}[h(x) = 0] \leq \epsilon \quad \text{và} \quad \Pr_{x \sim D_-}[h(x) = 1] \leq \epsilon. \tag{2.25}$$

Như vậy, giả thuyết phải có lỗi nhỏ trên cả hai phân phối. Đặt $C$ là một lớp khái niệm tùy ý và $H$ là không gian giả thuyết tùy ý. Đặt $h_0$ và $h_1$ biểu diễn các hàm hằng số 0 và hằng số 1, tương ứng. Chứng minh rằng $C$ là PAC-learnable hiệu quả sử dụng $H$ trong mô hình PAC tiêu chuẩn (một-oracle) nếu và chỉ nếu nó là PAC-learnable hiệu quả sử dụng $H \cup \{h_0, h_1\}$ trong mô hình PAC hai-oracle này.

**2.2 PAC-learning siêu hình chữ nhật.** Một siêu hình chữ nhật căn chỉnh theo trục trong $\mathbb{R}^n$ là một tập có dạng $[a_1, b_1] \times \ldots \times [a_n, b_n]$. Chỉ ra rằng các siêu hình chữ nhật căn chỉnh theo trục là PAC-learnable bằng cách mở rộng bằng chứng được đưa ra trong Ví dụ 2.4 cho trường hợp $n = 2$.

**2.3 Vòng tròn đồng tâm.** Đặt $\mathcal{X} = \mathbb{R}^2$ và xét tập các khái niệm có dạng $c = \{(x, y) : x^2 + y^2 \leq r^2\}$ cho một số thực $r$ nào đó. Chỉ ra rằng lớp này có thể được $(\epsilon, \delta)$-PAC-learned từ dữ liệu huấn luyện kích thước $m \geq (1/\epsilon)\log(1/\delta)$.

**2.4 Vòng tròn không đồng tâm.** Đặt $\mathcal{X} = \mathbb{R}^2$ và xét tập các khái niệm có dạng $c = \{x \in \mathbb{R}^2 : \|x - x_0\| \leq r\}$ cho một điểm $x_0 \in \mathbb{R}^2$ và số thực $r$ nào đó. Gertrude, một nhà nghiên cứu học máy đang học, cố gắng chỉ ra rằng lớp khái niệm này có thể được $(\epsilon, \delta)$-PAC-learned với độ phức tạp mẫu $m \geq (3/\epsilon)\log(3/\delta)$, nhưng cô gặp khó khăn với bằng chứng của mình. Ý tưởng của cô là thuật toán học sẽ chọn vòng tròn nhỏ nhất nhất quán với dữ liệu huấn luyện. Cô đã vẽ ba vùng $r_1, r_2, r_3$ xung quanh rìa của khái niệm $c$, với mỗi vùng có xác suất $\epsilon/3$ (xem hình 2.5(a)). Cô muốn lập luận rằng nếu lỗi khái quát hóa lớn hơn hoặc bằng $\epsilon$, thì một trong các vùng này phải bị bỏ lỡ bởi dữ liệu huấn luyện, và do đó sự kiện này sẽ xảy ra với xác suất tối đa $\delta$. Bạn có thể cho Gertrude biết phương pháp của cô có hiệu quả không? (Gợi ý: Bạn có thể muốn sử dụng hình 2.5(b) trong giải của mình.)

**2.5 Tam giác.** Đặt $\mathcal{X} = \mathbb{R}^2$ với cơ sở trực chuẩn $(e_1, e_2)$, và xét tập các khái niệm được định nghĩa bởi vùng bên trong tam giác vuông $ABC$ với hai cạnh song song với các trục, với $\overrightarrow{AB}/\|\overrightarrow{AB}\| = e_1$ và $\overrightarrow{AC}/\|\overrightarrow{AC}\| = e_2$, và $\|\overrightarrow{AB}\|/\|\overrightarrow{AC}\| = \alpha$ cho một $\alpha \in \mathbb{R}^+$ nào đó. Chỉ ra, sử dụng các phương pháp tương tự như những phương pháp được sử dụng trong chương cho hình chữ nhật căn chỉnh theo trục, rằng lớp này có thể được $(\epsilon, \delta)$-PAC-learned từ dữ liệu huấn luyện kích thước $m \geq (3/\epsilon)\log(3/\delta)$. (Gợi ý: Bạn có thể xem xét sử dụng hình 2.6 trong giải của mình.)

**2.6 Học trong sự hiện diện của nhiễu — hình chữ nhật.** Trong ví dụ 2.4, chúng ta đã chỉ ra rằng lớp khái niệm của các hình chữ nhật căn chỉnh theo trục là PAC-learnable. Bây giờ xét trường hợp các điểm huấn luyện nhận được bởi người học chịu nhiễu sau: các điểm được gán nhãn âm không bị ảnh hưởng bởi nhiễu nhưng nhãn của một điểm huấn luyện dương ngẫu nhiên bị lật thành âm với xác suất $\eta \in (0, \frac{1}{2})$. Giá trị chính xác của tỷ lệ nhiễu $\eta$ không được biết bởi người học nhưng một cận trên $\eta' \leq \eta' < 1/2$ được cung cấp cho họ. Chỉ ra rằng thuật toán trả về hình chữ nhật chật nhất chứa các điểm dương vẫn có thể PAC-learn các hình chữ nhật căn chỉnh theo trục trong sự hiện diện của nhiễu này. Để làm như vậy, bạn có thể tiến hành theo các bước sau:

(a) Sử dụng ký hiệu tương tự như trong ví dụ 2.4, giả sử rằng $\Pr[R] > \epsilon$. Giả sử rằng $R(R') > \epsilon$. Đưa ra cận trên về xác suất mà $R'$ bỏ lỡ vùng $r_j$, $j \in [4]$ theo $\epsilon$ và $\eta'$.

(b) Dùng điều đó để đưa ra cận trên về $\Pr[R(R') > \epsilon]$ theo $\epsilon$ và $\eta'$ và kết luận bằng cách đưa ra cận độ phức tạp mẫu.

**2.7 Học trong sự hiện diện của nhiễu — trường hợp tổng quát.** Trong câu hỏi này, chúng ta sẽ tìm kiếm một kết quả tổng quát hơn so với câu hỏi trước. Chúng ta xét một tập giả thuyết hữu hạn $H$, giả sử rằng khái niệm mục tiêu nằm trong $H$, và áp dụng mô hình nhiễu sau: nhãn của một điểm huấn luyện nhận được bởi người học bị thay đổi ngẫu nhiên với xác suất $\eta \in (0, \frac{1}{2})$. Giá trị chính xác của tỷ lệ nhiễu $\eta$ không được biết bởi người học nhưng một cận trên $\eta'$ được cung cấp với $\eta \leq \eta' < 1/2$.

(a) Với mọi $h \in H$, đặt $d(h)$ ký hiệu xác suất mà nhãn của một điểm huấn luyện nhận được bởi người học không đồng ý với nhãn được cho bởi $h$. Đặt $h^*$ là giả thuyết mục tiêu, chỉ ra rằng $d(h^*) = \eta$.

(b) Tổng quát hơn, chỉ ra rằng với mọi $h \in H$, $d(h) = \eta + (1 - 2\eta)R(h)$, trong đó $R(h)$ ký hiệu lỗi khái quát hóa của $h$.

(c) Cố định $\epsilon > 0$ cho câu hỏi này và tất cả các câu hỏi tiếp theo. Sử dụng các câu hỏi trước để chỉ ra rằng nếu $R(h) > \epsilon$, thì $d(h) - d(h^*) \geq \epsilon'$, trong đó $\epsilon' = \epsilon(1 - 2\eta')$.

(d) Với mọi giả thuyết $h \in H$ và mẫu $S$ kích thước $m$, đặt $\hat{d}(h)$ ký hiệu tỷ lệ các điểm trong $S$ có nhãn không đồng ý với các nhãn được cho bởi $h$. Chúng ta sẽ xét thuật toán $L$ mà, sau khi nhận $S$, trả về giả thuyết $h_S$ với số điểm không đồng ý nhỏ nhất (do đó $\hat{d}(h_S)$ nhỏ nhất). Để chỉ ra PAC-learning cho $L$, chúng ta sẽ chỉ ra rằng với mọi $h$, nếu $R(h) > \epsilon$, thì với xác suất cao $\hat{d}(h) \geq \hat{d}(h^*)$. Trước tiên, chỉ ra rằng với mọi $\delta > 0$, với xác suất ít nhất $1 - \delta/2$, với $m \geq \frac{2}{\epsilon'^2}\log\frac{2}{\delta}$, điều sau đây thỏa mãn:
$$\hat{d}(h^*) - d(h^*) \leq \epsilon'/2.$$

(e) Thứ hai, chỉ ra rằng với mọi $\delta > 0$, với xác suất ít nhất $1 - \delta/2$, với $m \geq \frac{2}{\epsilon'^2}(\log|H| + \log\frac{2}{\delta})$, điều sau đây thỏa mãn với mọi $h \in H$:
$$d(h) - \hat{d}(h) \leq \epsilon'/2.$$

(f) Cuối cùng, chỉ ra rằng với mọi $\delta > 0$, với xác suất ít nhất $1 - \delta$, với $m \geq \frac{2}{\epsilon^2(1-2\eta')^2}(\log|H| + \log\frac{2}{\delta})$, điều sau đây thỏa mãn với mọi $h \in H$ mà $R(h) > \epsilon$: $\hat{d}(h) - \hat{d}(h^*) \geq 0$.

(Gợi ý: sử dụng $\hat{d}(h) - \hat{d}(h^*) = [\hat{d}(h) - d(h)] + [d(h) - d(h^*)] + [d(h^*) - \hat{d}(h^*)]$ và sử dụng các câu hỏi trước để cận dưới mỗi ba số hạng này.)

**2.8 Học khoảng.** Đưa ra một thuật toán PAC-learning cho lớp khái niệm $C$ được tạo thành bởi các khoảng đóng $[a, b]$ với $a, b \in \mathbb{R}$.

**2.9 Học hội của các khoảng.** Đưa ra một thuật toán PAC-learning cho lớp khái niệm $C_2$ được tạo thành bởi hội của hai khoảng đóng, tức là $[a, b] \cup [c, d]$, với $a, b, c, d \in \mathbb{R}$. Mở rộng kết quả của bạn để suy ra một thuật toán PAC-learning cho lớp khái niệm $C_p$ được tạo thành bởi hội của $p \geq 1$ khoảng đóng, tức là $[a_1, b_1] \cup \cdots \cup [a_p, b_p]$, với $a_k, b_k \in \mathbb{R}$ với $k \in [p]$. Độ phức tạp thời gian và mẫu của thuật toán của bạn là bao nhiêu theo hàm của $p$?

**2.10 Giả thuyết nhất quán.** Trong chương này, chúng ta đã chỉ ra rằng với tập giả thuyết hữu hạn $H$, một thuật toán học nhất quán $A$ là thuật toán PAC-learning. Ở đây, chúng ta xét một câu hỏi nghịch đảo. Đặt $Z$ là một tập hữu hạn gồm $m$ điểm được gán nhãn. Giả sử rằng bạn được cho một thuật toán PAC-learning $A$. Chỉ ra rằng bạn có thể sử dụng $A$ và một mẫu huấn luyện hữu hạn $S$ để tìm trong thời gian đa thức một giả thuyết $h \in H$ nhất quán với $Z$, với xác suất cao. (Gợi ý: bạn có thể chọn một phân phối $D$ thích hợp trên $Z$ và đưa ra một điều kiện trên $R(h)$ để $h$ nhất quán.)

**2.11 Luật thượng viện.** Với các câu hỏi quan trọng, Tổng thống Mouth dựa vào lời khuyên của chuyên gia. Ông chọn một cố vấn thích hợp từ một tập hợp $H = 2{,}800$ chuyên gia.

(a) Giả sử rằng các luật được đề xuất theo cách ngẫu nhiên độc lập và giống nhau theo một phân phối $D$ được xác định bởi một nhóm thượng nghị sĩ không biết. Giả sử rằng Tổng thống Mouth có thể tìm và chọn một thượng nghị sĩ chuyên gia từ $H$ đã nhất quán bỏ phiếu với đa số cho $m = 200$ luật cuối cùng. Đưa ra cận về xác suất mà thượng nghị sĩ đó dự đoán sai về phiếu bầu toàn cầu cho một luật tương lai. Giá trị của cận với độ tin cậy 95% là gì?

(b) Giả sử bây giờ rằng Tổng thống Mouth có thể tìm và chọn một thượng nghị sĩ chuyên gia từ $H$ đã nhất quán bỏ phiếu với đa số trừ $m' = 20$ trong số $m = 200$ luật cuối cùng. Giá trị của cận mới là gì?

**2.12 Cận Bayesian.** Đặt $H$ là một tập giả thuyết đếm được của các hàm ánh xạ $\mathcal{X}$ sang $\{0, 1\}$ và đặt $p$ là một thước đo xác suất trên $H$. Thước đo xác suất này biểu diễn xác suất tiên nghiệm trên lớp giả thuyết, tức là xác suất mà một giả thuyết cụ thể được chọn bởi thuật toán học. Sử dụng bất đẳng thức Hoeffding để chỉ ra rằng với mọi $\delta > 0$, với xác suất ít nhất $1 - \delta$, bất đẳng thức sau đây thỏa mãn:

$$\forall h \in H, \quad R(h) \leq \hat{R}_S(h) + \sqrt{\frac{\frac{1}{\log p(h)} + \log \frac{1}{\delta}}{2m}}. \tag{2.26}$$

So sánh kết quả này với cận được đưa ra trong trường hợp không nhất quán cho tập giả thuyết hữu hạn (Gợi ý: bạn có thể sử dụng $\delta' = p(h)\delta$ làm tham số độ tin cậy trong bất đẳng thức Hoeffding).

**2.13 Học với tham số không biết.** Trong ví dụ 2.9, chúng ta đã chỉ ra rằng lớp khái niệm $k$-CNF là PAC-learnable. Tuy nhiên, lưu ý rằng thuật toán học được cho $k$ là đầu vào. PAC-learning có thể thực hiện được ngay cả khi $k$ không được cung cấp không? Tổng quát hơn, xét một họ các lớp khái niệm $\{C_s\}_s$ trong đó $C_s$ là tập các khái niệm trong $C$ có kích thước tối đa $s$. Giả sử chúng ta có một thuật toán PAC-learning $A$ có thể được sử dụng để học bất kỳ lớp khái niệm $C_s$ nào khi $s$ được cho. Có thể chuyển đổi $A$ thành một thuật toán PAC-learning $B$ không yêu cầu biết $s$ không? Đây là mục tiêu chính của bài toán này.

Để thực hiện điều này, trước tiên chúng ta giới thiệu một phương pháp kiểm tra một giả thuyết $h$, với xác suất cao. Cố định $\epsilon > 0$, $\delta > 0$, và $i \geq 1$ và định nghĩa kích thước mẫu $n$ bởi $n = \frac{32}{\epsilon^2}[i\log 2 + \log\frac{2}{\delta}]$. Giả sử chúng ta rút một mẫu i.i.d. $S$ kích thước $n$ theo một phân phối $D$ không biết nào đó. Chúng ta sẽ nói rằng một giả thuyết $h$ được **chấp nhận (accepted)** nếu nó tạo ra tối đa $\frac{3}{4}\epsilon$ lỗi trên $S$ và bị **từ chối (rejected)** nếu không. Như vậy, $h$ được chấp nhận nếu và chỉ nếu $\hat{R}_S(h) \leq \frac{3}{4}\epsilon$.

(a) Giả sử rằng $R(h) \geq \epsilon$. Sử dụng cận Chernoff (nhân) để chỉ ra rằng trong trường hợp đó $\Pr_{S \sim D^n}[h \text{ được chấp nhận}] \leq \frac{\delta}{2^{i+1}}$.

(b) Giả sử rằng $R(h) \leq \epsilon/2$. Sử dụng cận Chernoff (nhân) để chỉ ra rằng trong trường hợp đó $\Pr_{S \sim D^n}[h \text{ bị từ chối}] \leq \frac{\delta}{2^{i+1}}$.

(c) Thuật toán $B$ được định nghĩa như sau: chúng ta bắt đầu với $i = 1$ và, tại mỗi vòng $i \geq 1$, chúng ta đoán tham số kích thước $s$ là $\hat{s} = \lfloor 2^{(i-1)/\log\frac{2}{\delta}} \rfloor$. Chúng ta rút một mẫu $S$ kích thước $n$ (phụ thuộc vào $i$) để kiểm tra giả thuyết $h_i$ được trả về bởi $A$ khi nó được huấn luyện với mẫu kích thước $S_A(\epsilon/2, 1/2, \hat{s})$, tức là độ phức tạp mẫu của $A$ cho độ chính xác yêu cầu $\epsilon/2$, độ tin cậy $1/2$, và kích thước $\hat{s}$ (chúng ta bỏ qua kích thước biểu diễn của mỗi ví dụ ở đây). Nếu $h_i$ được chấp nhận, thuật toán dừng và trả về $h_i$, ngược lại nó tiến đến vòng lặp tiếp theo. Chỉ ra rằng nếu tại vòng lặp $i$, ước lượng $\hat{s}$ lớn hơn hoặc bằng $s$, thì $\Pr[h_i \text{ được chấp nhận}] \geq 3/8$.

(d) Chỉ ra rằng xác suất $B$ không dừng sau $j = \lceil\log\frac{2}{\delta} / \log\frac{8}{5}\rceil$ vòng lặp với $\hat{s} \geq s$ là tối đa $\delta/2$.

(e) Chỉ ra rằng với $i \geq \lceil 1 + (\log_2 s)\log\frac{2}{\delta}\rceil$, bất đẳng thức $\hat{s} \geq s$ thỏa mãn.

(f) Chỉ ra rằng với xác suất ít nhất $1 - \delta$, thuật toán $B$ dừng sau tối đa $j' = \lceil 1 + (\log_2 s)\log\frac{2}{\delta}\rceil + j$ vòng lặp và trả về một giả thuyết với lỗi tối đa $\epsilon$.

**2.14** Trong bài tập này, chúng ta tổng quát hóa khái niệm nhiễu sang trường hợp của hàm mất mát tùy ý $L : \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}_+$.

(a) Biện minh cho định nghĩa nhiễu tại điểm $x \in \mathcal{X}$ sau đây:
$$\text{noise}(x) = \min_{y' \in \mathcal{Y}} \mathbb{E}[L(y, y') | x].$$
Giá trị của $\text{noise}(x)$ trong kịch bản tất định là gì? Định nghĩa có khớp với định nghĩa được đưa ra trong chương này cho phân loại nhị phân không?

(b) Chỉ ra rằng nhiễu trung bình trùng với lỗi Bayes (mất mát tối thiểu đạt được bởi một hàm đo được).

