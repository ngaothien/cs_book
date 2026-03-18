# Chương 4: Lựa chọn Mô hình

Một vấn đề then chốt trong thiết kế các thuật toán học là việc chọn tập giả thuyết $H$. Đây được gọi là bài toán lựa chọn mô hình (model selection). Tập giả thuyết $H$ nên được chọn như thế nào? Một tập giả thuyết đủ phong phú hoặc phức tạp có thể chứa bộ phân loại Bayes lý tưởng. Mặt khác, việc học với một họ phức tạp như vậy trở thành nhiệm vụ rất khó. Tổng quát hơn, việc chọn $H$ chịu sự đánh đổi có thể được phân tích theo sai số ước lượng và sai số xấp xỉ.

Thảo luận của chúng ta sẽ tập trung vào trường hợp đặc biệt của phân loại nhị phân nhưng phần lớn những gì được thảo luận có thể được mở rộng trực tiếp cho các nhiệm vụ và hàm mất mát khác nhau.

## 4.1 Sai số ước lượng và xấp xỉ

Gọi $H$ là một họ hàm ánh xạ $\mathcal{X}$ tới $\{-1, +1\}$. Sai số dư (excess error) của giả thuyết $h$ được chọn từ $H$, tức hiệu giữa sai số $R(h)$ và sai số Bayes $R^*$, có thể được phân tách như sau:

$$R(h) - R^* = \underbrace{\left(R(h) - \inf_{h \in H} R(h)\right)}_{\text{ước lượng}} + \underbrace{\left(\inf_{h \in H} R(h) - R^*\right)}_{\text{xấp xỉ}}. \quad (4.1)$$

Hạng thứ nhất được gọi là **sai số ước lượng** (estimation error), hạng thứ hai là **sai số xấp xỉ** (approximation error). Sai số ước lượng phụ thuộc vào giả thuyết $h$ được chọn. Nó đo sai số của $h$ so với hạ xác (infimum) của các sai số đạt được bởi các giả thuyết trong $H$, hay so với giả thuyết tốt nhất trong lớp $h^*$ khi hạ xác đó đạt được. Lưu ý rằng định nghĩa PAC-learning bất khả tri chính xác dựa trên sai số ước lượng.

Sai số xấp xỉ đo mức độ sai số Bayes có thể được xấp xỉ tốt khi sử dụng $H$. Nó là tính chất của tập giả thuyết $H$, thước đo độ phong phú của nó. Với $H$ phức tạp hoặc phong phú hơn, sai số xấp xỉ có xu hướng nhỏ hơn với cái giá là sai số ước lượng lớn hơn.

Lựa chọn mô hình bao gồm việc chọn $H$ với sự đánh đổi thuận lợi giữa sai số xấp xỉ và ước lượng. Tuy nhiên, lưu ý rằng sai số xấp xỉ không truy cập được, vì nói chung phân phối cơ sở $D$ cần thiết để xác định $R^*$ không được biết. Ngay cả với các giả định nhiễu khác nhau, việc ước lượng sai số xấp xỉ là khó. Ngược lại, sai số ước lượng của thuật toán $A$, tức sai số ước lượng của giả thuyết $h_S$ được trả về sau khi huấn luyện trên mẫu $S$, đôi khi có thể được chặn bằng các cận khái quát hóa như được chỉ ra trong phần tiếp theo.

## 4.2 Cực tiểu hóa rủi ro thực nghiệm (ERM)

Một thuật toán chuẩn mà sai số ước lượng có thể được chặn là Cực tiểu hóa Rủi ro Thực nghiệm (ERM — Empirical Risk Minimization). ERM tìm cách cực tiểu hóa sai số trên mẫu huấn luyện:

$$h_S^{\text{ERM}} = \underset{h \in H}{\text{argmin}} \; \hat{R}_S(h). \quad (4.2)$$

**Mệnh đề 4.1** Với mọi mẫu $S$, bất đẳng thức sau đúng cho giả thuyết được ERM trả về:

$$\mathbb{P}\left[R(h_S^{\text{ERM}}) - \inf_{h \in H} R(h) > \epsilon\right] \leq \mathbb{P}\left[\sup_{h \in H} \left|R(h) - \hat{R}_S(h)\right| > \frac{\epsilon}{2}\right]. \quad (4.3)$$

**Chứng minh:** Theo định nghĩa $\inf_{h \in H} R(h)$, với mọi $\epsilon > 0$, tồn tại $h_\epsilon$ sao cho $R(h_\epsilon) \leq \inf_{h \in H} R(h) + \epsilon$. Do đó, sử dụng $\hat{R}_S(h_S^{\text{ERM}}) \leq \hat{R}_S(h_\epsilon)$, đúng theo định nghĩa thuật toán, chúng ta có thể viết

$$R(h_S^{\text{ERM}}) - \inf_{h \in H} R(h) = R(h_S^{\text{ERM}}) - R(h_\epsilon) + R(h_\epsilon) - \inf_{h \in H} R(h)$$

$$\leq R(h_S^{\text{ERM}}) - R(h_\epsilon) + \epsilon$$

$$= R(h_S^{\text{ERM}}) - \hat{R}_S(h_S^{\text{ERM}}) + \hat{R}_S(h_S^{\text{ERM}}) - R(h_\epsilon) + \epsilon$$

$$\leq R(h_S^{\text{ERM}}) - \hat{R}_S(h_S^{\text{ERM}}) + \hat{R}_S(h_\epsilon) - R(h_\epsilon) + \epsilon$$

$$\leq 2\sup_{h \in H} \left|R(h) - \hat{R}_S(h)\right| + \epsilon.$$

Vì bất đẳng thức đúng cho mọi $\epsilon > 0$, nó suy ra:

$$R(h_S^{\text{ERM}}) - \inf_{h \in H} R(h) \leq 2\sup_{h \in H} \left|R(h) - \hat{R}_S(h)\right|,$$

hoàn tất chứng minh. $\square$

Vế phải của (4.3) có thể được chặn trên bằng các cận khái quát hóa trình bày trong chương trước theo độ phức tạp Rademacher, hàm tăng trưởng, hoặc chiều VC của $H$. Đặc biệt, nó có thể được chặn bởi $2e^{-2m[\epsilon - \mathfrak{R}_m(H)]^2}$. Do đó, khi $H$ có độ phức tạp Rademacher thuận lợi, ví dụ chiều VC hữu hạn, với mẫu đủ lớn, với xác suất cao, sai số ước lượng được đảm bảo nhỏ. Tuy nhiên, hiệu suất của ERM thường rất kém. Nguyên nhân là thuật toán bỏ qua độ phức tạp của tập giả thuyết $H$: trong thực tế, hoặc $H$ không đủ phức tạp, khi đó sai số xấp xỉ có thể rất lớn, hoặc $H$ rất phong phú, khi đó cận sai số ước lượng trở nên rất lỏng. Ngoài ra, trong nhiều trường hợp, việc xác định nghiệm ERM là khó tính toán. Ví dụ, tìm giả thuyết tuyến tính với sai số nhỏ nhất trên mẫu huấn luyện là NP-hard, theo chiều của không gian.

## 4.3 Cực tiểu hóa rủi ro cấu trúc (SRM)

Trong phần trước, chúng ta đã chỉ ra rằng sai số ước lượng đôi khi có thể được chặn. Nhưng, vì sai số xấp xỉ không thể ước lượng, chúng ta nên chọn $H$ như thế nào? Một cách là chọn họ $H$ rất phức tạp không có sai số xấp xỉ hoặc có sai số rất nhỏ. $H$ có thể quá phong phú để các cận khái quát hóa đúng cho $H$, nhưng giả sử chúng ta có thể phân tách $H$ thành hợp của các tập giả thuyết $H_\gamma$ có độ phức tạp tăng dần, tức $H = \bigcup_{\gamma \in \Gamma} H_\gamma$, với độ phức tạp của $H_\gamma$ tăng theo $\gamma$. Bài toán khi đó bao gồm chọn tham số $\gamma^* \in \Gamma$ và do đó tập giả thuyết $H_{\gamma^*}$ với sự đánh đổi thuận lợi nhất giữa sai số ước lượng và xấp xỉ.

Đây chính xác là ý tưởng đằng sau phương pháp **Cực tiểu hóa Rủi ro Cấu trúc** (SRM — Structural Risk Minimization). Với SRM, $H$ được giả sử có thể phân tách thành tập đếm được, do đó chúng ta viết $H = \bigcup_{k \geq 1} H_k$. Thêm nữa, các tập $H_k$ được giả sử lồng nhau: $H_k \subset H_{k+1}$ với mọi $k \geq 1$. SRM bao gồm chọn chỉ số $k^* \geq 1$ và giả thuyết ERM $h$ trong $H_{k^*}$ cực tiểu hóa cận trên sai số dư.

Cận học sau đúng cho mọi $h \in H$: với mọi $\delta > 0$, với xác suất ít nhất $1 - \delta$ trên mẫu $S$ kích thước $m$, với mọi $h \in H_k$ và $k \geq 1$,

$$R(h) \leq \hat{R}_S(h) + \mathfrak{R}_m(H_{k(h)}) + \sqrt{\frac{\log k}{m}} + \sqrt{\frac{\log \frac{2}{\delta}}{2m}}.$$

Nghiệm SRM được định nghĩa:

$$h_S^{\text{SRM}} = \underset{k \geq 1, h \in H_k}{\text{argmin}} \; \hat{R}_S(h) + \mathfrak{R}_m(H_k) + \sqrt{\frac{\log k}{m}}. \quad (4.4)$$

**Định lý 4.2 (Đảm bảo học SRM)** Với mọi $\delta > 0$, với xác suất ít nhất $1 - \delta$ trên mẫu i.i.d. $S$ kích thước $m$ từ $D^m$, sai số khái quát hóa của giả thuyết $h_S^{\text{SRM}}$ được SRM trả về bị chặn:

$$R(h_S^{\text{SRM}}) \leq \inf_{h \in H}\left(R(h) + 2\mathfrak{R}_m(H_{k(h)}) + \sqrt{\frac{\log k(h)}{m}}\right) + \sqrt{\frac{2\log \frac{3}{\delta}}{m}}.$$

**Chứng minh:** Quan sát trước rằng, theo bổ đề hợp, bất đẳng thức tổng quát sau đúng:

$$\mathbb{P}\left[\sup_{h \in H} R(h) - F_{k(h)}(h) > \epsilon\right] = \mathbb{P}\left[\sup_{k \geq 1}\sup_{h \in H_k} R(h) - F_k(h) > \epsilon\right]$$

$$\leq \sum_{k=1}^{\infty}\mathbb{P}\left[\sup_{h \in H_k} R(h) - \hat{R}_S(h) - \mathfrak{R}_m(H_k) > \epsilon + \sqrt{\frac{\log k}{m}}\right]$$

$$\leq \sum_{k=1}^{\infty}\exp\left(-2m\left[\epsilon + \sqrt{\frac{\log k}{m}}\right]^2\right) \leq \sum_{k=1}^{\infty} e^{-2m\epsilon^2} \cdot e^{-2\log k} = e^{-2m\epsilon^2}\sum_{k=1}^{\infty}\frac{1}{k^2} = \frac{\pi^2}{6}e^{-2m\epsilon^2} \leq 2e^{-2m\epsilon^2}. \quad (4.5)$$

Tiếp theo, với hai biến ngẫu nhiên $X_1$ và $X_2$, nếu $X_1 + X_2 > \epsilon$, thì $X_1$ hoặc $X_2$ phải lớn hơn $\epsilon/2$. Sử dụng bổ đề hợp, (4.5), và $F_{k(h_S^{\text{SRM}})}(h_S^{\text{SRM}}) \leq F_{k(h)}(h)$ (đúng cho mọi $h \in H$ theo định nghĩa $h_S^{\text{SRM}}$), với mọi $h \in H$:

$$\mathbb{P}\left[R(h_S^{\text{SRM}}) - R(h) - 2\mathfrak{R}_m(H_{k(h)}) - \sqrt{\frac{\log k(h)}{m}} > \epsilon\right] \leq 3e^{-m\epsilon^2/2}.$$

Đặt vế phải bằng $\delta$ hoàn tất chứng minh. $\square$

Đảm bảo học vừa chứng minh cho SRM rất đáng chú ý. Giả sử tồn tại $h^*$ sao cho $R(h^*) = \inf_{h \in H} R(h)$. Khi đó, định lý suy ra với xác suất ít nhất $1 - \delta$:

$$R(h_S^{\text{SRM}}) \leq R(h^*) + 2\mathfrak{R}_m(H_{k(h^*)}) + \sqrt{\frac{\log k(h^*)}{m}} + \sqrt{\frac{2\log \frac{3}{\delta}}{m}}. \quad (4.6)$$

Đáng chú ý, cận này tương tự cận sai số ước lượng cho $H_{k(h^*)}$: nó chỉ khác bởi hạng $\sqrt{\log k(h^*)/m}$. Do đó, modulo hạng đó, đảm bảo cho SRM thuận lợi như khi một oracle thông báo cho chúng ta chỉ số $k(h^*)$ của tập giả thuyết chứa $h^*$.

Hơn nữa, khi $H$ đủ phong phú để $R(h^*)$ gần sai số Bayes, cận học (4.6) xấp xỉ là cận trên sai số dư của nghiệm SRM. Lưu ý rằng, nếu với một $k_0$ nào đó, sai số thực nghiệm của nghiệm ERM cho $H_{k_0}$ bằng không, đặc biệt nếu $H_{k_0}$ chứa sai số Bayes, thì ta có $\min_{h \in H_k} F_{k_0}(h) \leq \min_{h \in H_k} F_k(h)$ với mọi $k > k_0$ và chỉ hữu hạn chỉ số cần xem xét trong SRM.

Tổng quát hơn, giả sử nếu $\min_{h \in H_k} F_k(h) \leq \min_{h \in H_{k+1}} F_{k+1}(h)$ với một $k$ nào đó, thì các chỉ số lớn hơn $k+1$ không cần kiểm tra. Tính chất này có thể đúng chẳng hạn nếu sai số thực nghiệm không thể cải thiện thêm sau một chỉ số $k$ nào đó. Trong trường hợp đó, chỉ số cực tiểu $k^*$ có thể được xác định bằng tìm kiếm nhị phân (binary search) trong khoảng $[1, k_{\max}]$, với một giá trị cực đại $k_{\max}$ nào đó. Bản thân $k_{\max}$ có thể được tìm bằng cách kiểm tra $\min_{h \in H_{2^n}} F_k(h)$ cho các chỉ số tăng theo lũy thừa $2^n$, $n \geq 1$, và đặt $k_{\max} = 2^n$ với $n$ sao cho $\min_{h \in H_{2^n}} F_k(h) \leq \min_{h \in H_{2^{n+1}}} F_k(h)$. Số tính toán ERM cần thiết để tìm $k_{\max}$ thuộc $O(n) = O(\log k_{\max})$ và tương tự số tính toán ERM qua tìm kiếm nhị phân thuộc $O(\log k_{\max})$. Do đó, nếu $n$ là số nguyên nhỏ nhất sao cho $k^* < 2^n$, tổng số tính toán ERM thuộc $O(\log k^*)$.

Mặc dù hưởng đảm bảo rất thuận lợi, SRM có một số hạn chế. Thứ nhất, tính phân tách được của $H$ thành vô hạn đếm được các tập, mỗi tập có độ phức tạp Rademacher hội tụ, vẫn là giả định mạnh. Ví dụ, họ tất cả các hàm đo được không thể được viết như hợp của vô hạn đếm được các tập giả thuyết có chiều VC hữu hạn. Do đó, việc chọn $H$ hoặc các tập giả thuyết $H_k$ là thành phần then chốt của SRM. Thứ hai, và đây là bất lợi chính, phương pháp thường không khả thi về mặt tính toán: với hầu hết tập giả thuyết, giải ERM là NP-hard và SRM yêu cầu xác định nghiệm cho nhiều chỉ số $k$.

## 4.4 Kiểm định chéo (Cross-validation)

Một phương pháp thay thế cho lựa chọn mô hình, kiểm định chéo (cross-validation), bao gồm sử dụng một phần của mẫu huấn luyện làm tập kiểm định để chọn tập giả thuyết $H_k$. Điều này tương phản với mô hình SRM dựa trên cận học lý thuyết gán hình phạt cho mỗi tập giả thuyết.

Như phần trước, gọi $(H_k)_{k \geq 1}$ là dãy đếm được các tập giả thuyết có độ phức tạp tăng dần. Nghiệm kiểm định chéo (CV) thu được như sau. Gọi $S$ là mẫu i.i.d. kích thước $m$. $S$ được chia thành mẫu $S_1$ kích thước $(1-\alpha)m$ và mẫu $S_2$ kích thước $\alpha m$, với $\alpha \in (0, 1)$ thường được chọn tương đối nhỏ. $S_1$ dành cho huấn luyện, $S_2$ cho kiểm định. Với mọi $k \in \mathbb{N}$, gọi $h_{S_1,k}^{\text{ERM}}$ là nghiệm ERM trên $S_1$ sử dụng $H_k$. Giả thuyết $h_S^{\text{CV}}$ được CV trả về là nghiệm ERM $h_{S_1,k}^{\text{ERM}}$ có hiệu suất tốt nhất trên $S_2$:

$$h_S^{\text{CV}} = \underset{h \in \{h_{S_1,k}^{\text{ERM}} : k \geq 1\}}{\text{argmin}} \; \hat{R}_{S_2}(h). \quad (4.7)$$

**Mệnh đề 4.3** Với mọi $\alpha > 0$ và mọi kích thước mẫu $m \geq 1$:

$$\mathbb{P}\left[\sup_{k \geq 1}\left|R(h_{S_1,k}^{\text{ERM}}) - \hat{R}_{S_2}(h_{S_1,k}^{\text{ERM}})\right| > \epsilon + \sqrt{\frac{\log k}{\alpha m}}\right] \leq 4e^{-2\alpha m\epsilon^2}.$$

**Chứng minh:** Theo bổ đề hợp và bất đẳng thức Hoeffding (sử dụng sự kiện rằng $h_{S_1,k}^{\text{ERM}}$ cố định khi điều kiện hóa trên $S_1$ và $S_2$ độc lập với $S_1$), tổng trên $k$ cho:

$$\leq \sum_{k=1}^{\infty} \frac{2}{k^2}e^{-2\alpha m\epsilon^2} = \frac{\pi^2}{3}e^{-2\alpha m\epsilon^2} < 4e^{-2\alpha m\epsilon^2}. \quad \square$$

**Định lý 4.4 (Kiểm định chéo so với SRM)** Với mọi $\delta > 0$, với xác suất ít nhất $1 - \delta$:

$$R(h_S^{\text{CV}}) - R(h_{S_1}^{\text{SRM}}) \leq 2\sqrt{\frac{\log\max(k(h_S^{\text{CV}}), k(h_{S_1}^{\text{SRM}}))}{\alpha m}} + 2\sqrt{\frac{\log\frac{4}{\delta}}{2\alpha m}},$$

trong đó, với mọi $h$, $k(h)$ là chỉ số nhỏ nhất của tập giả thuyết chứa $h$.

**Chứng minh:** Theo Mệnh đề 4.3 và Định lý 4.2, sử dụng tính chất $h_S^{\text{CV}}$ là bộ cực tiểu, với mọi $\delta > 0$, với xác suất ít nhất $1 - \delta$:

$$R(h_S^{\text{CV}}) \leq \hat{R}_{S_2}(h_S^{\text{CV}}) + \sqrt{\frac{\log k(h_S^{\text{CV}})}{\alpha m}} + \sqrt{\frac{\log\frac{4}{\delta}}{2\alpha m}}$$

$$\leq \hat{R}_{S_2}(h_{S_1}^{\text{SRM}}) + \sqrt{\frac{\log k(h_S^{\text{CV}})}{\alpha m}} + \sqrt{\frac{\log\frac{4}{\delta}}{2\alpha m}}$$

$$\leq R(h_{S_1}^{\text{SRM}}) + \sqrt{\frac{\log k(h_S^{\text{CV}})}{\alpha m}} + \sqrt{\frac{\log k(h_{S_1}^{\text{SRM}})}{\alpha m}} + 2\sqrt{\frac{\log\frac{4}{\delta}}{2\alpha m}}$$

$$\leq R(h_{S_1}^{\text{SRM}}) + 2\sqrt{\frac{\log\max(k(h_S^{\text{CV}}), k(h_{S_1}^{\text{SRM}}))}{\alpha m}} + 2\sqrt{\frac{\log\frac{4}{\delta}}{2\alpha m}}. \quad \square$$

Đảm bảo học vừa chứng minh cho thấy, với xác suất cao, sai số khái quát hóa của nghiệm CV cho mẫu kích thước $m$ gần với nghiệm SRM cho mẫu kích thước $(1-\alpha)m$. Với $\alpha$ tương đối nhỏ, điều này gợi ý đảm bảo tương tự SRM. Tuy nhiên, trong một số chế độ bất lợi, thuật toán huấn luyện trên $(1-\alpha)m$ điểm có thể có hiệu suất kém hơn đáng kể so với huấn luyện trên $m$ điểm. Do đó, cận gợi ý sự đánh đổi: $\alpha$ nên được chọn đủ nhỏ để tránh các chế độ bất lợi nhưng đủ lớn để vế phải nhỏ.

## 4.5 Kiểm định chéo $n$-fold

Trong thực tế, lượng dữ liệu có nhãn thường quá nhỏ để dành riêng mẫu kiểm định vì điều đó sẽ để lại lượng dữ liệu huấn luyện không đủ. Thay vào đó, phương pháp được áp dụng rộng rãi gọi là **kiểm định chéo $n$-fold** được sử dụng để khai thác dữ liệu có nhãn cho cả lựa chọn mô hình và huấn luyện.

Gọi $\theta$ là vectơ tham số tự do của thuật toán. Với giá trị $\theta$ cố định, phương pháp bao gồm trước tiên phân hoạch ngẫu nhiên mẫu $S$ gồm $m$ ví dụ có nhãn thành $n$ mẫu con, gọi là các fold. Fold thứ $i$ là mẫu có nhãn $((x_{i1}, y_{i1}), \ldots, (x_{im_i}, y_{im_i}))$ kích thước $m_i$. Với mọi $i \in [n]$, thuật toán được huấn luyện trên tất cả trừ fold thứ $i$ để sinh giả thuyết $h_i$, và hiệu suất của $h_i$ được kiểm tra trên fold thứ $i$. Giá trị $\theta$ được đánh giá dựa trên sai số trung bình của các giả thuyết $h_i$, gọi là **sai số kiểm định chéo**:

$$\hat{R}_{\text{CV}}(\theta) = \frac{1}{n}\sum_{i=1}^{n}\frac{1}{m_i}\sum_{j=1}^{m_i}\underbrace{L(h_i(x_{ij}), y_{ij})}_{\text{sai số của } h_i \text{ trên fold thứ } i}.$$

Các fold thường được chọn có kích thước bằng nhau, tức $m_i = m/n$ với mọi $i \in [n]$.

$n$ nên được chọn như thế nào? Sự lựa chọn phù hợp chịu sự đánh đổi. Với $n$ lớn, mỗi mẫu huấn luyện có kích thước $m(1 - 1/n)$, gần $m$, và tất cả mẫu huấn luyện khá tương tự. Đồng thời, fold thứ $i$ dùng đo sai số tương đối nhỏ, do vậy sai số CV có xu hướng có độ lệch nhỏ nhưng phương sai lớn. Ngược lại, giá trị $n$ nhỏ hơn dẫn đến mẫu huấn luyện đa dạng hơn nhưng kích thước nhỏ hơn đáng kể so với $m$. Trong chế độ này, sai số CV có phương sai nhỏ hơn nhưng độ lệch lớn hơn.

Trong ứng dụng, $n$ thường được chọn là 5 hoặc 10. Kiểm định chéo $n$-fold được sử dụng cho lựa chọn mô hình như sau. Dữ liệu có nhãn đầy đủ được chia thành mẫu huấn luyện và mẫu test. Mẫu huấn luyện kích thước $m$ sau đó được dùng tính sai số CV $\hat{R}_{\text{CV}}(\theta)$ cho một số ít giá trị $\theta$ có thể. Tham số $\theta$ được đặt bằng giá trị $\theta_0$ sao cho $\hat{R}_{\text{CV}}(\theta)$ nhỏ nhất và thuật toán được huấn luyện với $\theta_0$ trên toàn bộ mẫu huấn luyện kích thước $m$. Hiệu suất được đánh giá trên mẫu test.

Trường hợp đặc biệt $n = m$ được gọi là **kiểm định chéo leave-one-out**, vì mỗi lần lặp chỉ một thực thể bị loại bỏ khỏi mẫu huấn luyện. Sai số leave-one-out trung bình là ước lượng xấp xỉ không thiên lệch của sai số trung bình của thuật toán. Nói chung, sai số leave-one-out rất tốn kém, vì cần huấn luyện $m$ lần trên mẫu kích thước $m - 1$, nhưng với một số thuật toán nó có cách tính toán rất hiệu quả (bài tập 11.9).

## 4.6 Thuật toán dựa trên chính quy hóa

Một họ rộng lớn các thuật toán lấy cảm hứng từ SRM là **thuật toán dựa trên chính quy hóa** (regularization-based algorithm). Phương pháp bao gồm chọn họ $H$ rất phức tạp là hợp không đếm được của các tập giả thuyết lồng nhau $H_\gamma$: $H = \bigcup_{\gamma > 0} H_\gamma$. $H$ thường được chọn trù mật trong không gian hàm liên tục trên $\mathcal{X}$. Ví dụ, $H$ có thể được chọn là tập tất cả hàm tuyến tính trong không gian chiều cao và $H_\gamma$ là tập con có chuẩn bị chặn bởi $\gamma$: $H_\gamma = \{x \mapsto w \cdot \Phi(x) : \|w\| \leq \gamma\}$.

Mở rộng SRM cho hợp không đếm được gợi ý chọn $h$ dựa trên bài toán tối ưu:

$$\underset{\gamma > 0, h \in H_\gamma}{\text{argmin}} \; \hat{R}_S(h) + \text{pen}(\gamma, m),$$

trong đó $\text{pen}(\gamma, m) = \mathfrak{R}_m(H_\gamma) + \sqrt{\log\gamma/m}$. Thường tồn tại hàm $\mathcal{R}: H \to \mathbb{R}$ sao cho bài toán tối ưu ràng buộc có thể được viết tương đương:

$$\underset{h \in H}{\text{argmin}} \; \hat{R}_S(h) + \lambda\mathcal{R}(h),$$

với $\lambda > 0$. $\mathcal{R}(h)$ được gọi là **hạng chính quy hóa** và $\lambda > 0$ được xem như siêu tham số. Với hầu hết thuật toán, $\mathcal{R}(h)$ được chọn là hàm tăng của $\|h\|$ cho một chuẩn nào đó. Giá trị $\lambda$ lớn hơn phạt thêm các giả thuyết phức tạp, trong khi $\lambda$ gần hoặc bằng không, hạng chính quy hóa không có hiệu lực và thuật toán trùng với ERM. Trong thực tế, $\lambda$ thường được chọn qua kiểm định chéo.

Khi hạng chính quy hóa được chọn là $\|h\|^p$ với $p \geq 1$, nó là hàm lồi. Tuy nhiên, với mất mát zero-one, hạng thứ nhất của hàm mục tiêu không lồi, khiến bài toán tối ưu khó tính toán. Trong thực tế, hầu hết thuật toán dựa trên chính quy hóa sử dụng cận trên lồi của mất mát zero-one và thay hạng thực nghiệm zero-one bằng giá trị thực nghiệm của mất mát thay thế lồi (convex surrogate). Bài toán tối ưu kết quả là lồi và do đó có nghiệm hiệu quả hơn SRM.

## 4.7 Mất mát thay thế lồi

Các đảm bảo sai số ước lượng đã trình bày đúng cho ERM hoặc SRM. Tuy nhiên, với nhiều tập $H$, bao gồm hàm tuyến tính, giải ERM là NP-hard chủ yếu vì hàm mất mát zero-one không lồi. Phương pháp phổ biến là sử dụng hàm mất mát thay thế lồi chặn trên mất mát zero-one.

Các giả thuyết là hàm giá trị thực $h: \mathcal{X} \to \mathbb{R}$. Dấu của $h$ định nghĩa bộ phân loại nhị phân $f_h$:

$$f_h(x) = \begin{cases} +1 & \text{nếu } h(x) \geq 0 \\ -1 & \text{nếu } h(x) < 0. \end{cases}$$

Với mọi $x \in \mathcal{X}$, gọi $\eta(x) = \mathbb{P}[y = +1 | x]$. Bộ phân loại Bayes gán nhãn $+1$ cho $x$ khi $\eta(x) \geq 1/2$. Nó được dẫn xuất bởi hàm cho điểm Bayes (Bayes scoring function):

$$h^*(x) = \eta(x) - \frac{1}{2}. \quad (4.9)$$

**Bổ đề 4.5** Sai số dư của giả thuyết $h: \mathcal{X} \to \mathbb{R}$ có thể được biểu diễn:

$$R(h) - R^* = 2\underset{x \sim D_X}{\mathbb{E}}\left[|h^*(x)| \cdot \mathbf{1}_{h(x)h^*(x) \leq 0}\right].$$

**Chứng minh:** Với mọi $h$:

$$R(h) = \underset{x \sim D_X}{\mathbb{E}}\left[\eta(x)\mathbf{1}_{h(x)<0} + (1-\eta(x))\mathbf{1}_{h(x) \geq 0}\right] = \underset{x \sim D_X}{\mathbb{E}}\left[2h^*(x)\mathbf{1}_{h(x)<0} + (1-\eta(x))\right].$$

Do đó:

$$R(h) - R(h^*) = \underset{x \sim D_X}{\mathbb{E}}\left[2h^*(x)(\mathbf{1}_{h(x) \leq 0} - \mathbf{1}_{h^*(x) \leq 0})\right] = 2\underset{x \sim D_X}{\mathbb{E}}\left[|h^*(x)|\mathbf{1}_{h(x)h^*(x) \leq 0}\right]. \quad \square$$

Gọi $\Phi: \mathbb{R} \to \mathbb{R}$ là hàm lồi và không giảm sao cho $\mathbf{1}_{u \leq 0} \leq \Phi(-u)$ với mọi $u \in \mathbb{R}$. $\Phi$-loss của hàm $h$ tại $(x, y)$ là $\Phi(-yh(x))$ và mất mát kỳ vọng:

$$L_\Phi(h) = \underset{(x,y) \sim D}{\mathbb{E}}\left[\Phi(-yh(x))\right] = \underset{x \sim D_X}{\mathbb{E}}\left[\eta(x)\Phi(-h(x)) + (1-\eta(x))\Phi(h(x))\right]. \quad (4.10)$$

Vì $\mathbf{1}_{yh(x) \leq 0} \leq \Phi(-yh(x))$, ta có $R(h) \leq L_\Phi(h)$. Định nghĩa $h_\Phi^*$ là nghiệm Bayes cho $L_\Phi$: $h_\Phi^*(x) = \text{argmin}_{u} [\eta(x)\Phi(-u) + (1-\eta(x))\Phi(u)]$.

**Mệnh đề 4.6** Gọi $\Phi$ lồi, không giảm, khả vi tại 0 với $\Phi'(0) > 0$. Khi đó bộ cực tiểu $\Phi$ định nghĩa bộ phân loại Bayes: $h_\Phi^*(x) > 0$ khi và chỉ khi $h^*(x) > 0$ và $h^*(x) = 0$ khi và chỉ khi $h_\Phi^*(x) = 0$, suy ra $L_\Phi^* = R^*$.

**Chứng minh:** Cố định $x \in \mathcal{X}$. Nếu $\eta(x) = 0$ thì $h^*(x) = -1/2$ và $h_\Phi^*(x) = -\infty$, do đó $h^*(x)$ và $h_\Phi^*(x)$ có cùng dấu. Tương tự, nếu $\eta(x) = 1$ thì $h^*(x) = 1/2$ và $h_\Phi^*(x) = +\infty$, và $h^*(x)$ và $h_\Phi^*(x)$ có cùng dấu.

Gọi $u^*$ là bộ cực tiểu định nghĩa $h_\Phi^*(x)$. $u^*$ là bộ cực tiểu của $u \mapsto L_\Phi(x, u)$ khi và chỉ khi dưới vi phân của hàm đó tại $u^*$ chứa 0, tức vì $\partial L_\Phi(x, u^*) = -\eta(x)\partial\Phi(-u^*) + (1-\eta(x))\partial\Phi(u^*)$, khi và chỉ khi tồn tại $v_1 \in \partial\Phi(-u^*)$ và $v_2 \in \partial\Phi(u^*)$ sao cho

$$\eta(x)v_1 = (1 - \eta(x))v_2. \quad (4.11)$$

Nếu $u^* = 0$, theo tính khả vi của $\Phi$ tại 0, ta có $v_1 = v_2 = \Phi'(0) > 0$ và do đó $\eta(x) = 1/2$, tức $h^*(x) = 0$. Ngược lại, nếu $h^*(x) = 0$, tức $\eta(x) = 1/2$, thì theo định nghĩa ta có $h_\Phi^*(x) = 0$. Vậy, $h^*(x) = 0$ khi và chỉ khi $h_\Phi^*(x) = 0$ khi và chỉ khi $\eta(x) = 1/2$.

Bay giờ giả sử $\eta(x)$ không thuộc $\{0, 1, 1/2\}$. Trước tiên chúng ta chứng minh với mọi $u_1, u_2 \in \mathbb{R}$ với $u_1 < u_2$, và mọi lựa chọn dưới gradient tại $u_1$ và $u_2$, $v_1 \in \partial\Phi(u_1)$ và $v_2 \in \partial\Phi(u_2)$, ta có $v_1 \leq v_2$. Theo định nghĩa dưới gradient tại $u_1$ và $u_2$, các bất đẳng thức sau đúng:

$$\Phi(u_2) - \Phi(u_1) \geq v_1(u_2 - u_1), \quad \Phi(u_1) - \Phi(u_2) \geq v_2(u_1 - u_2).$$

Cộng hai bất đẳng thức này cho $v_2(u_2 - u_1) \geq v_1(u_2 - u_1)$ và do đó $v_2 \geq v_1$ vì $u_1 < u_2$.

Nếu $u^* > 0$, thì $-u^* < u^*$. Theo tính chất vừa chứng minh, điều này suy ra $v_1 \leq v_2$. Ta không thể có $v_1 = v_2 \neq 0$ vì (4.11) khi đó suy ra $\eta(x) = 1/2$. Ta cũng không thể có $v_1 = v_2 = 0$ vì theo tính chất vừa chứng minh, ta phải có $\Phi'(0) \leq v_2$ và do đó $v_2 > 0$. Vậy, ta phải có $v_1 < v_2$ với $v_2 > 0$, và theo (4.11), điều này suy ra $\eta(x) > 1 - \eta(x)$, tức $h^*(x) > 0$.

Ngược lại, nếu $h^*(x) > 0$ thì $\eta(x) > 1 - \eta(x)$. Ta không thể có $v_1 = v_2 = 0$ hoặc $v_1 = v_2 \neq 0$ như đã chứng minh. Vậy, vì $\eta(x) \neq 1$, theo (4.11), điều này suy ra $v_1 < v_2$. Ta không thể có $u^* < -u^*$ vì theo tính chất vừa chứng minh, điều đó suy ra $v_2 \leq v_1$. Vậy, ta phải có $-u^* \leq u^*$, tức $u^* \geq 0$, và cụ thể hơn $u^* > 0$ vì như đã chứng minh, $u^* = 0$ suy ra $h^*(x) = 0$. $\square$

**Định lý 4.7** Gọi $\Phi$ lồi và không giảm. Giả sử tồn tại $s \geq 1$ và $c > 0$ sao cho với mọi $x \in \mathcal{X}$:

$$\left|\eta(x) - \frac{1}{2}\right|^s \leq c^s\left[L_\Phi(x, 0) - L_\Phi(x, h_\Phi^*(x))\right].$$

Khi đó, với mọi giả thuyết $h$, sai số dư bị chặn:

$$R(h) - R^* \leq 2c\left[L_\Phi(h) - L_\Phi^*\right]^{1/s}.$$

**Chứng minh:** Theo Bổ đề 4.5, bất đẳng thức Jensen, giả định, và bất đẳng thức lồi $\Phi(-2h^*(x)h(x)) \leq L_\Phi(x, h(x))$ (theo (4.12)):

$$R(h) - R^* \leq 2c\underset{x}{\mathbb{E}}\left[L_\Phi(x, h(x)) - L_\Phi(x, h_\Phi^*(x))\right]^{1/s} = 2c\left[L_\Phi(h) - L_\Phi^*\right]^{1/s}. \quad \square$$

Định lý cho thấy, khi giả định đúng, sai số dư của $h$ có thể được chặn trên theo $\Phi$-loss dư. Giả định của định lý đúng đặc biệt cho:

- **Mất mát bản lề (Hinge loss):** $\Phi(u) = \max(0, 1+u)$, với $s=1$, $c=1/2$.
- **Mất mát hàm mũ (Exponential loss):** $\Phi(u) = \exp(u)$, với $s=2$, $c=1/\sqrt{2}$.
- **Mất mát logistic (Logistic loss):** $\Phi(u) = \log_2(1+e^u)$, với $s=2$, $c=1/\sqrt{2}$.

Chúng cũng đúng cho mất mát bình phương và mất mát bản lề bình phương (bài tập 4.2 và 4.3).

## 4.8 Ghi chú chương

Kỹ thuật cực tiểu hóa rủi ro cấu trúc (SRM) là do Vapnik [1998]. Hạng phạt gốc do Vapnik sử dụng dựa trên chiều VC. Phiên bản SRM với hạng phạt dựa trên độ phức tạp Rademacher mà chúng ta trình bày dẫn đến đảm bảo học phụ thuộc dữ liệu tinh tế hơn. Một lý thuyết lựa chọn mô hình thay thế — Cực tiểu hóa Rủi ro Bỏ phiếu (VRM) — được phát triển bởi Cortes, Mohri, và Syed [2014]. Định lý 4.7 là do Zhang [2003a].

## 4.9 Bài tập

**4.1** Với mọi tập giả thuyết $H$, chứng minh:

$$\underset{S \sim D^m}{\mathbb{E}}\left[\hat{R}_S(h_S^{\text{ERM}})\right] \leq \inf_{h \in H} R(h) \leq \underset{S \sim D^m}{\mathbb{E}}\left[R(h_S^{\text{ERM}})\right]. \quad (4.13)$$

**4.2** Chứng minh với mất mát bình phương $\Phi(u) = (1+u)^2$, Định lý 4.7 đúng với $s=2$, $c=1/2$, suy ra $R(h) - R^* \leq [L_\Phi(h) - L_\Phi^*]^{1/2}$.

**4.3** Chứng minh với mất mát bản lề bình phương $\Phi(u) = \max(0, 1+u)^2$, Định lý 4.7 đúng với $s=2$, $c=1/2$.

**4.4** Với hàm mất mát $\mathbf{1}_{yh(x) \leq 0}$: (a) Định nghĩa bộ phân loại Bayes và hàm cho điểm Bayes $h^*$. (b) Biểu diễn sai số dư theo $h^*$. (c) Đưa ra đối đẳng Định lý 4.7.

**4.5** Các câu hỏi tương tự với mất mát $\mathbf{1}_{yh(x) < 0}$.
