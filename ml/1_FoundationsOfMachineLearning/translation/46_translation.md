# Chương 3: Độ phức tạp Rademacher và Chiều VC

Các tập giả thuyết thường được sử dụng trong học máy là vô hạn. Nhưng các cận độ phức tạp mẫu của chương trước không mang lại thông tin khi xử lý các tập giả thuyết vô hạn. Người ta có thể hỏi liệu việc học hiệu quả từ một mẫu hữu hạn có khả thi không khi tập giả thuyết $H$ là vô hạn. Phân tích của chúng ta về họ các hình chữ nhật song song với trục (Ví dụ 2.4) chỉ ra rằng điều này thực sự khả thi ít nhất trong một số trường hợp, vì chúng ta đã chứng minh rằng lớp khái niệm vô hạn đó là PAC-learnable. Mục tiêu của chúng ta trong chương này sẽ là khái quát hóa kết quả đó và dẫn ra các đảm bảo học tổng quát cho các tập giả thuyết vô hạn.

Một ý tưởng tổng quát để làm điều này bao gồm việc quy giản trường hợp vô hạn về phân tích các tập giả thuyết hữu hạn và sau đó tiến hành như trong chương trước. Có các kỹ thuật khác nhau cho phép quy giản đó, mỗi kỹ thuật dựa trên một khái niệm phức tạp khác nhau cho họ giả thuyết. Khái niệm phức tạp đầu tiên chúng ta sẽ sử dụng là độ phức tạp Rademacher (Rademacher complexity). Điều này sẽ giúp chúng ta dẫn ra các đảm bảo học bằng các chứng minh tương đối đơn giản dựa trên bất đẳng thức McDiarmid, đồng thời thu được các cận chất lượng cao, bao gồm các cận phụ thuộc dữ liệu, mà chúng ta sẽ thường xuyên sử dụng trong các chương tiếp theo. Tuy nhiên, việc tính toán độ phức tạp Rademacher thực nghiệm là NP-hard cho một số tập giả thuyết. Do đó, chúng ta tiếp theo giới thiệu hai khái niệm tổ hợp thuần túy khác, hàm tăng trưởng (growth function) và chiều VC (VC-dimension).

Đầu tiên chúng ta liên hệ độ phức tạp Rademacher với hàm tăng trưởng và sau đó chặn hàm tăng trưởng theo chiều VC. Chiều VC thường dễ chặn hoặc ước lượng hơn. Chúng ta sẽ xem xét một loạt ví dụ cho thấy cách tính toán hoặc chặn nó, sau đó liên hệ hàm tăng trưởng và chiều VC. Điều này dẫn đến các cận khái quát hóa dựa trên chiều VC. Cuối cùng, chúng ta trình bày các cận dưới dựa trên chiều VC cho hai thiết lập khác nhau: thiết lập khả thi (realizable setting), trong đó có ít nhất một giả thuyết trong tập giả thuyết đang xem xét đạt sai số kỳ vọng bằng không, cũng như thiết lập không khả thi (non-realizable setting), trong đó không có giả thuyết nào trong tập đạt sai số kỳ vọng bằng không.

## 3.1 Độ phức tạp Rademacher

Chúng ta sẽ tiếp tục sử dụng $H$ để ký hiệu tập giả thuyết như trong các chương trước. Nhiều kết quả trong phần này là tổng quát và đúng cho hàm mất mát tùy ý $L: \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}$. Trong phần tiếp theo, $G$ sẽ thường được hiểu là họ các hàm mất mát liên kết với $H$ ánh xạ từ $Z = \mathcal{X} \times \mathcal{Y}$ tới $\mathbb{R}$:

$$G = \{g: (x, y) \mapsto L(h(x), y) : h \in H\}.$$

Tuy nhiên, các định nghĩa được đưa ra trong trường hợp tổng quát của một họ hàm $G$ ánh xạ từ không gian đầu vào tùy ý $Z$ tới $\mathbb{R}$.

Độ phức tạp Rademacher nắm bắt độ phong phú của một họ hàm bằng cách đo mức độ mà một tập giả thuyết có thể khớp nhiễu ngẫu nhiên. Sau đây là các định nghĩa hình thức của độ phức tạp Rademacher thực nghiệm và trung bình.

**Định nghĩa 3.1 (Độ phức tạp Rademacher thực nghiệm)** Gọi $G$ là một họ hàm ánh xạ từ $Z$ tới $[a, b]$ và $S = (z_1, \ldots, z_m)$ là một mẫu cố định có kích thước $m$ với các phần tử trong $Z$. Khi đó, độ phức tạp Rademacher thực nghiệm của $G$ đối với mẫu $S$ được định nghĩa là:

$$\hat{\mathfrak{R}}_S(G) = \underset{\boldsymbol{\sigma}}{\mathbb{E}}\left[\sup_{g \in G} \frac{1}{m} \sum_{i=1}^{m} \sigma_i g(z_i)\right], \quad (3.1)$$

trong đó $\boldsymbol{\sigma} = (\sigma_1, \ldots, \sigma_m)^\top$, với $\sigma_i$ là các biến ngẫu nhiên đều độc lập nhận giá trị trong $\{-1, +1\}$. Các biến ngẫu nhiên $\sigma_i$ được gọi là các biến Rademacher.

Gọi $g_S$ là vectơ các giá trị mà hàm $g$ nhận trên mẫu $S$: $g_S = (g(z_1), \ldots, g(z_m))^\top$. Khi đó, độ phức tạp Rademacher thực nghiệm có thể được viết lại:

$$\hat{\mathfrak{R}}_S(G) = \underset{\boldsymbol{\sigma}}{\mathbb{E}}\left[\sup_{g \in G} \frac{\boldsymbol{\sigma} \cdot g_S}{m}\right].$$

Tích vô hướng $\boldsymbol{\sigma} \cdot g_S$ đo tương quan của $g_S$ với vectơ nhiễu ngẫu nhiên $\boldsymbol{\sigma}$. Thượng xác $\sup_{g \in G} \frac{\boldsymbol{\sigma} \cdot g_S}{m}$ là thước đo mức độ mà lớp hàm $G$ tương quan với $\boldsymbol{\sigma}$ trên mẫu $S$. Do đó, độ phức tạp Rademacher thực nghiệm đo trung bình mức độ mà lớp hàm $G$ tương quan với nhiễu ngẫu nhiên trên $S$. Điều này mô tả độ phong phú của họ $G$: các họ $G$ phong phú hoặc phức tạp hơn có thể sinh ra nhiều vectơ $g_S$ hơn và do đó tương quan tốt hơn với nhiễu ngẫu nhiên, trung bình.

**Định nghĩa 3.2 (Độ phức tạp Rademacher)** Gọi $D$ là phân phối mà các mẫu được rút theo. Với mọi số nguyên $m \geq 1$, độ phức tạp Rademacher của $G$ là kỳ vọng của độ phức tạp Rademacher thực nghiệm trên tất cả các mẫu có kích thước $m$ được rút theo $D$:

$$\mathfrak{R}_m(G) = \underset{S \sim D^m}{\mathbb{E}}\left[\hat{\mathfrak{R}}_S(G)\right]. \quad (3.2)$$

Bây giờ chúng ta sẵn sàng trình bày các cận khái quát hóa đầu tiên dựa trên độ phức tạp Rademacher.

**Định lý 3.3** Gọi $G$ là một họ hàm ánh xạ từ $Z$ tới $[0, 1]$. Khi đó, với mọi $\delta > 0$, với xác suất ít nhất $1 - \delta$ trên phép rút mẫu i.i.d. $S$ có kích thước $m$, mỗi điều sau đây đúng cho mọi $g \in G$:

$$\mathbb{E}[g(z)] \leq \frac{1}{m} \sum_{i=1}^{m} g(z_i) + 2\mathfrak{R}_m(G) + \sqrt{\frac{\log \frac{1}{\delta}}{2m}} \quad (3.3)$$

và

$$\mathbb{E}[g(z)] \leq \frac{1}{m} \sum_{i=1}^{m} g(z_i) + 2\hat{\mathfrak{R}}_S(G) + 3\sqrt{\frac{\log \frac{2}{\delta}}{2m}}. \quad (3.4)$$

**Chứng minh:** Với mọi mẫu $S = (z_1, \ldots, z_m)$ và mọi $g \in G$, chúng ta ký hiệu $\hat{E}_S[g]$ là trung bình thực nghiệm của $g$ trên $S$: $\hat{E}_S[g] = \frac{1}{m} \sum_{i=1}^{m} g(z_i)$. Chứng minh bao gồm việc áp dụng bất đẳng thức McDiarmid cho hàm $\Phi$ được định nghĩa cho mọi mẫu $S$ bởi

$$\Phi(S) = \sup_{g \in G}\left(\mathbb{E}[g] - \hat{E}_S[g]\right). \quad (3.5)$$

Gọi $S$ và $S'$ là hai mẫu chỉ khác nhau đúng một điểm, giả sử $z_m$ trong $S$ và $z_m'$ trong $S'$. Khi đó, vì hiệu của các thượng xác không vượt quá thượng xác của hiệu, chúng ta có

$$\Phi(S') - \Phi(S) \leq \sup_{g \in G}\left(\hat{E}_S[g] - \hat{E}_{S'}[g]\right) = \sup_{g \in G} \frac{g(z_m) - g(z_m')}{m} \leq \frac{1}{m}. \quad (3.6)$$

Tương tự, chúng ta có thể thu được $\Phi(S) - \Phi(S') \leq 1/m$, do đó $|\Phi(S) - \Phi(S')| \leq 1/m$. Khi đó, theo bất đẳng thức McDiarmid, với mọi $\delta > 0$, với xác suất ít nhất $1 - \delta/2$, điều sau đúng:

$$\Phi(S) \leq \underset{S}{\mathbb{E}}[\Phi(S)] + \sqrt{\frac{\log \frac{2}{\delta}}{2m}}. \quad (3.7)$$

Tiếp theo, chúng ta chặn kỳ vọng ở vế phải như sau:

$$\underset{S}{\mathbb{E}}[\Phi(S)] = \underset{S}{\mathbb{E}}\left[\sup_{g \in G}\left(\mathbb{E}[g] - \hat{E}_S(g)\right)\right] = \underset{S}{\mathbb{E}}\left[\sup_{g \in G} \underset{S'}{\mathbb{E}}\left[\hat{E}_{S'}(g) - \hat{E}_S(g)\right]\right] \quad (3.8)$$

$$\leq \underset{S, S'}{\mathbb{E}}\left[\sup_{g \in G}\left(\hat{E}_{S'}(g) - \hat{E}_S(g)\right)\right] \quad (3.9)$$

$$= \underset{S, S'}{\mathbb{E}}\left[\sup_{g \in G} \frac{1}{m} \sum_{i=1}^{m}\left(g(z_i') - g(z_i)\right)\right] \quad (3.10)$$

$$= \underset{\boldsymbol{\sigma}, S, S'}{\mathbb{E}}\left[\sup_{g \in G} \frac{1}{m} \sum_{i=1}^{m} \sigma_i\left(g(z_i') - g(z_i)\right)\right] \quad (3.11)$$

$$\leq \underset{\boldsymbol{\sigma}, S'}{\mathbb{E}}\left[\sup_{g \in G} \frac{1}{m} \sum_{i=1}^{m} \sigma_i g(z_i')\right] + \underset{\boldsymbol{\sigma}, S}{\mathbb{E}}\left[\sup_{g \in G} \frac{1}{m} \sum_{i=1}^{m} (-\sigma_i) g(z_i)\right] \quad (3.12)$$

$$= 2\underset{\boldsymbol{\sigma}, S}{\mathbb{E}}\left[\sup_{g \in G} \frac{1}{m} \sum_{i=1}^{m} \sigma_i g(z_i)\right] = 2\mathfrak{R}_m(G). \quad (3.13)$$

Phương trình (3.8) sử dụng sự kiện rằng các điểm trong $S'$ được lấy mẫu i.i.d. và do đó $\mathbb{E}[g] = E_{S'}[\hat{E}_{S'}(g)]$, như trong (2.3). Bất đẳng thức (3.9) đúng do tính dưới cộng (sub-additivity) của hàm thượng xác.

Trong phương trình (3.11), chúng ta giới thiệu các biến Rademacher $\sigma_i$, là các biến ngẫu nhiên đều độc lập nhận giá trị trong $\{-1, +1\}$ như trong Định nghĩa 3.2. Điều này không thay đổi kỳ vọng xuất hiện trong (3.10): khi $\sigma_i = 1$, hạng tương ứng không đổi; khi $\sigma_i = -1$, hạng tương ứng đổi dấu, tương đương với việc hoán đổi $z_i$ và $z_i'$ giữa $S$ và $S'$. Vì chúng ta đang lấy kỳ vọng trên tất cả $S$ và $S'$ có thể, việc hoán đổi này không ảnh hưởng đến kỳ vọng tổng thể.

Phương trình (3.12) đúng theo tính dưới cộng của hàm thượng xác, tức bất đẳng thức $\sup(U + V) \leq \sup(U) + \sup(V)$. Cuối cùng, (3.13) xuất phát từ định nghĩa của độ phức tạp Rademacher và sự kiện rằng các biến $\sigma_i$ và $-\sigma_i$ có cùng phân phối.

Phép quy giản về $\mathfrak{R}_m(G)$ trong phương trình (3.13) cho cận trong phương trình (3.3), sử dụng $\delta$ thay vì $\delta/2$. Để dẫn ra một cận theo $\hat{\mathfrak{R}}_S(G)$, chúng ta lưu ý rằng, theo Định nghĩa 3.1, việc thay đổi một điểm trong $S$ làm thay đổi $\hat{\mathfrak{R}}_S(G)$ nhiều nhất $1/m$. Khi đó, sử dụng lại bất đẳng thức McDiarmid, với xác suất $1 - \delta/2$ điều sau đúng:

$$\mathfrak{R}_m(G) \leq \hat{\mathfrak{R}}_S(G) + \sqrt{\frac{\log \frac{2}{\delta}}{2m}}. \quad (3.14)$$

Cuối cùng, chúng ta dùng bổ đề hợp để kết hợp các bất đẳng thức (3.7) và (3.14), cho với xác suất ít nhất $1 - \delta$:

$$\Phi(S) \leq 2\hat{\mathfrak{R}}_S(G) + 3\sqrt{\frac{\log \frac{2}{\delta}}{2m}}, \quad (3.15)$$

khớp với (3.4). $\square$

Kết quả tiếp theo liên hệ giữa độ phức tạp Rademacher thực nghiệm của tập giả thuyết $H$ và họ hàm mất mát $G$ liên kết với $H$ trong trường hợp mất mát nhị phân (zero-one loss).

**Bổ đề 3.4** Gọi $H$ là một họ hàm nhận giá trị trong $\{-1, +1\}$ và gọi $G$ là họ hàm mất mát liên kết với $H$ cho mất mát zero-one: $G = \{(x, y) \mapsto \mathbf{1}_{h(x) \neq y} : h \in H\}$. Với mọi mẫu $S = ((x_1, y_1), \ldots, (x_m, y_m))$ chứa các phần tử trong $\mathcal{X} \times \{-1, +1\}$, gọi $S_X$ là phép chiếu của nó lên $\mathcal{X}$: $S_X = (x_1, \ldots, x_m)$. Khi đó, quan hệ sau đúng giữa các độ phức tạp Rademacher thực nghiệm của $G$ và $H$:

$$\hat{\mathfrak{R}}_S(G) = \frac{1}{2}\hat{\mathfrak{R}}_{S_X}(H). \quad (3.16)$$

**Chứng minh:** Với mọi mẫu $S$, theo định nghĩa, độ phức tạp Rademacher thực nghiệm của $G$ có thể được viết:

$$\hat{\mathfrak{R}}_S(G) = \underset{\boldsymbol{\sigma}}{\mathbb{E}}\left[\sup_{h \in H} \frac{1}{m}\sum_{i=1}^{m} \sigma_i \mathbf{1}_{h(x_i) \neq y_i}\right] = \underset{\boldsymbol{\sigma}}{\mathbb{E}}\left[\sup_{h \in H} \frac{1}{m}\sum_{i=1}^{m} \sigma_i \frac{1 - y_i h(x_i)}{2}\right]$$

$$= \frac{1}{2}\underset{\boldsymbol{\sigma}}{\mathbb{E}}\left[\sup_{h \in H} \frac{1}{m}\sum_{i=1}^{m} (-\sigma_i y_i) h(x_i)\right] = \frac{1}{2}\underset{\boldsymbol{\sigma}}{\mathbb{E}}\left[\sup_{h \in H} \frac{1}{m}\sum_{i=1}^{m}\sigma_i h(x_i)\right] = \frac{1}{2}\hat{\mathfrak{R}}_{S_X}(H),$$

trong đó chúng ta sử dụng sự kiện $\mathbf{1}_{h(x_i) \neq y_i} = (1 - y_i h(x_i))/2$ và sự kiện rằng với $y_i \in \{-1, +1\}$ cố định, $\sigma_i$ và $-y_i\sigma_i$ có cùng phân phối. $\square$

Lưu ý rằng bổ đề suy ra, bằng cách lấy kỳ vọng, rằng với mọi $m \geq 1$, $\mathfrak{R}_m(G) = \frac{1}{2}\mathfrak{R}_m(H)$. Các mối liên hệ này giữa các độ phức tạp Rademacher thực nghiệm và trung bình có thể được sử dụng để dẫn ra các cận khái quát hóa cho phân loại nhị phân theo độ phức tạp Rademacher của tập giả thuyết $H$.

**Định lý 3.5 (Cận độ phức tạp Rademacher — phân loại nhị phân)** Gọi $H$ là một họ hàm nhận giá trị trong $\{-1, +1\}$ và gọi $D$ là phân phối trên không gian đầu vào $\mathcal{X}$. Khi đó, với mọi $\delta > 0$, với xác suất ít nhất $1 - \delta$ trên mẫu $S$ có kích thước $m$ được rút theo $D$, mỗi điều sau đây đúng cho mọi $h \in H$:

$$R(h) \leq \hat{R}_S(h) + \mathfrak{R}_m(H) + \sqrt{\frac{\log \frac{1}{\delta}}{2m}} \quad (3.17)$$

và

$$R(h) \leq \hat{R}_S(h) + \hat{\mathfrak{R}}_S(H) + 3\sqrt{\frac{\log \frac{2}{\delta}}{2m}}. \quad (3.18)$$

**Chứng minh:** Kết quả suy ra trực tiếp từ Định lý 3.3 và Bổ đề 3.4. $\square$

Định lý cung cấp hai cận khái quát hóa cho phân loại nhị phân dựa trên độ phức tạp Rademacher. Lưu ý rằng cận thứ hai, (3.18), phụ thuộc dữ liệu: độ phức tạp Rademacher thực nghiệm $\hat{\mathfrak{R}}_S(H)$ là hàm của mẫu cụ thể $S$ được rút. Do đó, cận này có thể đặc biệt hữu ích nếu chúng ta có thể tính $\hat{\mathfrak{R}}_S(H)$. Nhưng, làm thế nào chúng ta có thể tính độ phức tạp Rademacher thực nghiệm? Sử dụng lại sự kiện rằng $\sigma_i$ và $-\sigma_i$ có cùng phân phối, chúng ta có thể viết

$$\hat{\mathfrak{R}}_S(H) = \underset{\boldsymbol{\sigma}}{\mathbb{E}}\left[\sup_{h \in H} \frac{1}{m}\sum_{i=1}^{m}(-\sigma_i)h(x_i)\right] = -\underset{\boldsymbol{\sigma}}{\mathbb{E}}\left[\inf_{h \in H} \frac{1}{m}\sum_{i=1}^{m}\sigma_i h(x_i)\right].$$

Bây giờ, với giá trị cố định của $\boldsymbol{\sigma}$, việc tính $\inf_{h \in H} \frac{1}{m}\sum_{i=1}^{m}\sigma_i h(x_i)$ tương đương với bài toán cực tiểu hóa rủi ro thực nghiệm, được biết là khó tính toán cho một số tập giả thuyết. Do đó, trong một số trường hợp, việc tính $\hat{\mathfrak{R}}_S(H)$ có thể khó về mặt tính toán. Trong các phần tiếp theo, chúng ta sẽ liên hệ độ phức tạp Rademacher với các thước đo tổ hợp dễ tính toán hơn và cũng có giá trị độc lập cho tính hữu ích của chúng trong phân tích học trong nhiều ngữ cảnh.

## 3.2 Hàm tăng trưởng

Ở đây chúng ta sẽ chỉ ra cách độ phức tạp Rademacher có thể được chặn theo hàm tăng trưởng (growth function).

**Định nghĩa 3.6 (Hàm tăng trưởng)** Hàm tăng trưởng $\Pi_H: \mathbb{N} \to \mathbb{N}$ cho tập giả thuyết $H$ được định nghĩa bởi:

$$\forall m \in \mathbb{N}, \quad \Pi_H(m) = \max_{\{x_1, \ldots, x_m\} \subseteq \mathcal{X}} \left|\left\{(h(x_1), \ldots, h(x_m)) : h \in H\right\}\right|. \quad (3.19)$$

Nói cách khác, $\Pi_H(m)$ là số lượng tối đa các cách phân loại khác nhau mà $m$ điểm có thể được phân loại sử dụng các giả thuyết trong $H$. Mỗi cách phân loại khác nhau này được gọi là một lưỡng phân (dichotomy) và do đó, hàm tăng trưởng đếm số lưỡng phân được thực hiện bởi giả thuyết. Điều này cung cấp một thước đo khác về độ phong phú của tập giả thuyết $H$. Tuy nhiên, không giống như độ phức tạp Rademacher, thước đo này không phụ thuộc vào phân phối, nó hoàn toàn là tổ hợp.

Để liên hệ độ phức tạp Rademacher với hàm tăng trưởng, chúng ta sẽ sử dụng bổ đề Massart.

**Định lý 3.7 (Bổ đề Massart)** Gọi $A \subseteq \mathbb{R}^m$ là một tập hữu hạn, với $r = \max_{x \in A} \|x\|_2$, khi đó:

$$\underset{\boldsymbol{\sigma}}{\mathbb{E}}\left[\frac{1}{m}\sup_{x \in A} \sum_{i=1}^{m}\sigma_i x_i\right] \leq \frac{r\sqrt{2\log|A|}}{m}, \quad (3.20)$$

trong đó $\sigma_i$ là các biến ngẫu nhiên đều độc lập nhận giá trị trong $\{-1, +1\}$ và $x_1, \ldots, x_m$ là các thành phần của vectơ $x$.

**Chứng minh:** Kết quả suy ra trực tiếp từ cận trên kỳ vọng của cực đại cho bởi Hệ quả D.11 vì các biến ngẫu nhiên $\sigma_i x_i$ là độc lập và mỗi $\sigma_i x_i$ nhận giá trị trong $[-|x_i|, |x_i|]$ với $\sqrt{\sum_{i=1}^{m} x_i^2} \leq r^2$. $\square$

Sử dụng kết quả này, bây giờ chúng ta có thể chặn độ phức tạp Rademacher theo hàm tăng trưởng.

**Hệ quả 3.8** Gọi $G$ là một họ hàm nhận giá trị trong $\{-1, +1\}$. Khi đó:

$$\mathfrak{R}_m(G) \leq \sqrt{\frac{2\log \Pi_G(m)}{m}}. \quad (3.21)$$

**Chứng minh:** Với mẫu cố định $S = (x_1, \ldots, x_m)$, chúng ta ký hiệu $G|_S$ là tập các vectơ giá trị hàm $(g(x_1), \ldots, g(x_m))^\top$ trong đó $g \in G$. Vì $g \in G$ nhận giá trị trong $\{-1, +1\}$, chuẩn của các vectơ này bị chặn bởi $\sqrt{m}$. Chúng ta có thể áp dụng bổ đề Massart:

$$\mathfrak{R}_m(G) = \underset{S}{\mathbb{E}}\left[\underset{\boldsymbol{\sigma}}{\mathbb{E}}\left[\sup_{u \in G|_S} \frac{1}{m}\sum_{i=1}^{m}\sigma_i u_i\right]\right] \leq \underset{S}{\mathbb{E}}\left[\frac{\sqrt{m} \cdot \sqrt{2\log|G|_S|}}{m}\right].$$

Theo định nghĩa, $|G|_S|$ bị chặn bởi hàm tăng trưởng, do đó:

$$\mathfrak{R}_m(G) \leq \underset{S}{\mathbb{E}}\left[\frac{\sqrt{m} \cdot \sqrt{2\log \Pi_G(m)}}{m}\right] = \sqrt{\frac{2\log \Pi_G(m)}{m}},$$

hoàn tất chứng minh. $\square$

Kết hợp cận khái quát hóa (3.17) của Định lý 3.5 với Hệ quả 3.8 cho ngay cận khái quát hóa sau theo hàm tăng trưởng.

**Hệ quả 3.9 (Cận khái quát hóa hàm tăng trưởng)** Gọi $H$ là một họ hàm nhận giá trị trong $\{-1, +1\}$. Khi đó, với mọi $\delta > 0$, với xác suất ít nhất $1 - \delta$, với mọi $h \in H$,

$$R(h) \leq \hat{R}_S(h) + \sqrt{\frac{2\log \Pi_H(m)}{m}} + \sqrt{\frac{\log \frac{1}{\delta}}{2m}}. \quad (3.22)$$

Các cận hàm tăng trưởng cũng có thể được dẫn ra trực tiếp (không sử dụng cận độ phức tạp Rademacher trước). Cận kết quả khi đó có dạng:

$$\mathbb{P}\left[\left|R(h) - \hat{R}_S(h)\right| > \epsilon\right] \leq 4\Pi_H(2m) \exp\left(-\frac{m\epsilon^2}{8}\right), \quad (3.23)$$

chỉ khác (3.22) bởi các hằng số.

Việc tính toán hàm tăng trưởng không phải lúc nào cũng thuận tiện vì, theo định nghĩa, nó yêu cầu tính $\Pi_H(m)$ cho mọi $m \geq 1$. Phần tiếp theo giới thiệu một thước đo thay thế về độ phức tạp của tập giả thuyết $H$ dựa trên một đại lượng vô hướng duy nhất, mà hóa ra lại liên quan sâu sắc đến hành vi của hàm tăng trưởng.

## 3.3 Chiều VC

Ở đây, chúng ta giới thiệu khái niệm chiều VC (Vapnik-Chervonenkis dimension). Chiều VC cũng là một khái niệm tổ hợp thuần túy nhưng thường dễ tính toán hơn hàm tăng trưởng (hoặc Độ phức tạp Rademacher). Như chúng ta sẽ thấy, chiều VC là đại lượng then chốt trong học và liên quan trực tiếp đến hàm tăng trưởng.

Để định nghĩa chiều VC của tập giả thuyết $H$, trước tiên chúng ta giới thiệu khái niệm phá vỡ (shattering). Nhớ lại từ phần trước rằng, cho một tập giả thuyết $H$, một lưỡng phân (dichotomy) của tập $S$ là một trong các cách có thể gán nhãn cho các điểm của $S$ sử dụng một giả thuyết trong $H$. Một tập $S$ gồm $m \geq 1$ điểm được gọi là bị phá vỡ (shattered) bởi tập giả thuyết $H$ khi $H$ thực hiện tất cả các lưỡng phân có thể có của $S$, tức khi $\Pi_H(m) = 2^m$.

**Định nghĩa 3.10 (Chiều VC)** Chiều VC của tập giả thuyết $H$ là kích thước của tập lớn nhất có thể bị phá vỡ bởi $H$:

$$\text{VCdim}(H) = \max\{m : \Pi_H(m) = 2^m\}. \quad (3.24)$$

Lưu ý rằng, theo định nghĩa, nếu $\text{VCdim}(H) = d$, tồn tại một tập kích thước $d$ có thể bị phá vỡ. Tuy nhiên, điều này không ngụ ý rằng tất cả các tập kích thước $d$ hoặc nhỏ hơn đều bị phá vỡ và, thực tế, đây thường không phải là trường hợp.

Để minh họa thêm khái niệm này, chúng ta sẽ xem xét một loạt ví dụ về các tập giả thuyết và xác định chiều VC trong mỗi trường hợp. Để tính chiều VC, chúng ta thường chỉ ra một cận dưới cho giá trị của nó và sau đó một cận trên phù hợp. Để đưa ra cận dưới $d$ cho $\text{VCdim}(H)$, chỉ cần chỉ ra rằng một tập $S$ có lực lượng $d$ có thể bị phá vỡ bởi $H$. Để đưa ra cận trên, chúng ta cần chứng minh rằng không tập $S$ nào có lực lượng $d + 1$ có thể bị phá vỡ bởi $H$, điều này thường khó hơn.

**Ví dụ 3.11 (Các khoảng trên đường thẳng thực)** Ví dụ đầu tiên liên quan đến lớp giả thuyết của các khoảng trên đường thẳng thực. Rõ ràng chiều VC ít nhất là hai, vì tất cả bốn lưỡng phân $(+, +)$, $(-, -)$, $(+, -)$, $(-, +)$ có thể được thực hiện, như minh họa trong Hình 3.1(a). Ngược lại, theo định nghĩa của các khoảng, không tập nào gồm ba điểm có thể bị phá vỡ vì gán nhãn $(+, -, +)$ không thể được thực hiện. Do đó, $\text{VCdim}(\text{các khoảng trong } \mathbb{R}) = 2$.

**Ví dụ 3.12 (Siêu phẳng)** Xét tập các siêu phẳng trong $\mathbb{R}^2$. Đầu tiên chúng ta quan sát rằng bất kỳ ba điểm không thẳng hàng nào trong $\mathbb{R}^2$ đều có thể bị phá vỡ. Để thu được ba lưỡng phân đầu tiên, chúng ta chọn một siêu phẳng có hai điểm ở một phía và điểm thứ ba ở phía đối diện. Để thu được lưỡng phân thứ tư, chúng ta có cả ba điểm ở cùng một phía của siêu phẳng. Bốn lưỡng phân còn lại được thực hiện bằng cách đơn giản đổi dấu. Tiếp theo, chúng ta chứng minh rằng bốn điểm không thể bị phá vỡ bằng cách xem xét hai trường hợp: (i) bốn điểm nằm trên bao lồi được định nghĩa bởi bốn điểm, và (ii) ba trong bốn điểm nằm trên bao lồi và điểm còn lại ở bên trong. Trong trường hợp thứ nhất, gán nhãn dương cho một cặp đường chéo và nhãn âm cho cặp đường chéo kia không thể thực hiện được (Hình 3.2(a)). Trong trường hợp thứ hai, gán nhãn dương cho các điểm trên bao lồi và nhãn âm cho điểm nội không thể thực hiện được (Hình 3.2(b)). Do đó, $\text{VCdim}(\text{siêu phẳng trong } \mathbb{R}^2) = 3$.

Tổng quát hơn trong $\mathbb{R}^d$, chúng ta dẫn ra cận dưới bằng cách bắt đầu với tập $d + 1$ điểm trong $\mathbb{R}^d$, đặt $x_0$ là gốc tọa độ và định nghĩa $x_i$, cho $i \in \{1, \ldots, d\}$, là điểm có tọa độ thứ $i$ bằng 1 và tất cả các tọa độ khác bằng 0. Gọi $y_0, y_1, \ldots, y_d \in \{-1, +1\}$ là một tập nhãn tùy ý cho $x_0, x_1, \ldots, x_d$. Gọi $w$ là vectơ có tọa độ thứ $i$ là $y_i$. Khi đó bộ phân loại được định nghĩa bởi siêu phẳng có phương trình $w \cdot x + y_0/2 = 0$ phá vỡ $x_0, x_1, \ldots, x_d$ vì với mọi $i \in \{0, \ldots, d\}$,

$$\text{sgn}\left(w \cdot x_i + \frac{y_0}{2}\right) = \text{sgn}\left(y_i + \frac{y_0}{2}\right) = y_i. \quad (3.25)$$

Để thu được cận trên, chỉ cần chứng minh rằng không tập nào gồm $d + 2$ điểm có thể bị phá vỡ bởi các nửa không gian. Để chứng minh điều này, chúng ta sẽ sử dụng định lý tổng quát sau.

**Định lý 3.13 (Định lý Radon)** Mọi tập $X$ gồm $d + 2$ điểm trong $\mathbb{R}^d$ có thể được phân hoạch thành hai tập con $X_1$ và $X_2$ sao cho các bao lồi của $X_1$ và $X_2$ giao nhau.

**Chứng minh:** Gọi $X = \{x_1, \ldots, x_{d+2}\} \subset \mathbb{R}^d$. Sau đây là một hệ $d + 1$ phương trình tuyến tính theo $\alpha_1, \ldots, \alpha_{d+2}$:

$$\sum_{i=1}^{d+2} \alpha_i x_i = 0 \quad \text{và} \quad \sum_{i=1}^{d+2} \alpha_i = 0, \quad (3.26)$$

vì đẳng thức thứ nhất dẫn đến $d$ phương trình, mỗi phương trình cho một thành phần. Số ẩn, $d + 2$, lớn hơn số phương trình, $d + 1$, do đó hệ phương trình có nghiệm khác không $\beta_1, \ldots, \beta_{d+2}$. Vì $\sum_{i=1}^{d+2} \beta_i = 0$, cả $I_1 = \{i \in [d+2] : \beta_i > 0\}$ và $I_2 = \{i \in [d+2] : \beta_i \leq 0\}$ đều là các tập không rỗng và $X_1 = \{x_i : i \in I_1\}$ và $X_2 = \{x_i : i \in I_2\}$ tạo thành một phân hoạch của $X$. Theo phương trình cuối của (3.26), $\sum_{i \in I_1} \beta_i = -\sum_{i \in I_2} \beta_i$. Gọi $\beta = \sum_{i \in I_1} \beta_i$. Khi đó, phần đầu của (3.26) suy ra $\sum_{i \in I_1} \frac{\beta_i}{\beta} x_i = \sum_{i \in I_2} \frac{-\beta_i}{\beta} x_i$, với $\sum_{i \in I_1} \frac{\beta_i}{\beta} = \sum_{i \in I_2} \frac{-\beta_i}{\beta} = 1$, và $\frac{\beta_i}{\beta} \geq 0$ cho $i \in I_1$ và $\frac{-\beta_i}{\beta} \geq 0$ cho $i \in I_2$. Theo định nghĩa bao lồi, điều này suy ra $\sum_{i \in I_1} \frac{\beta_i}{\beta} x_i$ thuộc cả bao lồi của $X_1$ lẫn bao lồi của $X_2$. $\square$

Bây giờ, gọi $X$ là tập gồm $d + 2$ điểm. Theo Định lý Radon, nó có thể được phân hoạch thành hai tập $X_1$ và $X_2$ sao cho các bao lồi của chúng giao nhau. Quan sát rằng khi hai tập điểm $X_1$ và $X_2$ được phân tách bởi một siêu phẳng, các bao lồi của chúng cũng được phân tách bởi siêu phẳng đó. Do đó, $X_1$ và $X_2$ không thể bị phân tách bởi siêu phẳng và $X$ không bị phá vỡ. Kết hợp cận dưới và cận trên, chúng ta đã chứng minh $\text{VCdim}(\text{siêu phẳng trong } \mathbb{R}^d) = d + 1$.

**Ví dụ 3.14 (Hình chữ nhật song song trục)** Đầu tiên chúng ta chỉ ra chiều VC ít nhất bằng bốn, bằng cách xem xét bốn điểm theo mẫu hình thoi. Khi đó, rõ ràng tất cả 16 lưỡng phân đều có thể thực hiện. Ngược lại, với bất kỳ tập nào gồm năm điểm khác nhau, nếu chúng ta xây dựng hình chữ nhật song song trục nhỏ nhất chứa các điểm này, một trong năm điểm nằm bên trong hình chữ nhật. Hãy tưởng tượng chúng ta gán nhãn âm cho điểm bên trong này và nhãn dương cho bốn điểm còn lại. Không có hình chữ nhật song song trục nào có thể thực hiện gán nhãn này. Do đó, không tập nào gồm năm điểm khác nhau có thể bị phá vỡ và $\text{VCdim}(\text{hình chữ nhật song song trục}) = 4$.

**Ví dụ 3.15 (Đa giác lồi)** Chúng ta tập trung vào lớp các đa giác lồi $d$-cạnh trong mặt phẳng. Để có cận dưới, chúng ta chỉ ra rằng bất kỳ tập nào gồm $2d + 1$ điểm đều có thể bị phá vỡ. Để làm điều này, chúng ta chọn $2d + 1$ điểm nằm trên một đường tròn, và với một gán nhãn cụ thể, nếu có nhiều nhãn âm hơn nhãn dương, thì các điểm có nhãn dương được sử dụng làm đỉnh của đa giác. Ngược lại, các tiếp tuyến của các điểm âm đóng vai trò là các cạnh của đa giác. Để dẫn ra cận trên, có thể chứng minh rằng việc chọn các điểm trên đường tròn cực đại hóa số lưỡng phân có thể, và do đó $\text{VCdim}(\text{đa giác lồi } d\text{-cạnh}) = 2d + 1$. Cũng lưu ý rằng $\text{VCdim}(\text{đa giác lồi}) = +\infty$.

**Ví dụ 3.16 (Hàm sin)** Các ví dụ trước có thể gợi ý rằng chiều VC của $H$ trùng với số tham số tự do định nghĩa $H$. Ví dụ, số tham số định nghĩa siêu phẳng trùng với chiều VC của chúng. Tuy nhiên, điều này không đúng trong trường hợp tổng quát. Xét họ hàm sin sau: $\{t \mapsto \sin(\omega t) : \omega \in \mathbb{R}\}$. Các hàm sin này có thể được sử dụng để phân loại các điểm trên đường thẳng thực: một điểm được gán nhãn dương nếu nó nằm trên đường cong, nếu không thì gán nhãn âm. Mặc dù họ hàm sin này được định nghĩa qua một tham số duy nhất $\omega$, có thể chứng minh rằng $\text{VCdim}(\text{hàm sin}) = +\infty$ (bài tập 3.20).

Chiều VC của nhiều tập giả thuyết khác có thể được xác định hoặc chặn trên theo cách tương tự. Đặc biệt, chiều VC của bất kỳ không gian vectơ nào có chiều $r < \infty$ có thể được chứng minh là nhiều nhất $r$ (bài tập 3.19). Kết quả tiếp theo, được gọi là bổ đề Sauer, làm rõ mối liên hệ giữa các khái niệm hàm tăng trưởng và chiều VC.

**Định lý 3.17 (Bổ đề Sauer)** Gọi $H$ là tập giả thuyết với $\text{VCdim}(H) = d$. Khi đó, với mọi $m \in \mathbb{N}$, bất đẳng thức sau đúng:

$$\Pi_H(m) \leq \sum_{i=0}^{d} \binom{m}{i}. \quad (3.27)$$

**Chứng minh:** Chứng minh bằng quy nạp theo $m + d$. Phát biểu rõ ràng đúng cho $m = 1$ và $d = 0$ hoặc $d = 1$. Bây giờ, giả sử nó đúng cho $(m-1, d-1)$ và $(m-1, d)$. Cố định tập $S = \{x_1, \ldots, x_m\}$ với $\Pi_H(m)$ lưỡng phân và gọi $G = H|_S$ là tập các khái niệm $H$ giới hạn trên $S$.

Xét các họ sau trên $S' = \{x_1, \ldots, x_{m-1}\}$. Chúng ta định nghĩa $G_1 = G|_{S'}$ là tập các khái niệm giới hạn trên $S'$. Tiếp theo, bằng cách đồng nhất mỗi khái niệm với tập các điểm (trong $S'$ hoặc $S$) mà nó khác không, chúng ta định nghĩa $G_2 = \{g' \subseteq S' : (g' \in G) \wedge (g' \cup \{x_m\} \in G)\}$.

Theo định nghĩa, $|G_1| + |G_2| = |G|$. Vì $\text{VCdim}(G_1) \leq \text{VCdim}(G) \leq d$, theo giả thuyết quy nạp: $|G_1| \leq \Pi_{G_1}(m-1) \leq \sum_{i=0}^{d} \binom{m-1}{i}$.

Hơn nữa, theo định nghĩa $G_2$, nếu tập $Z \subseteq S'$ bị phá vỡ bởi $G_2$, thì $Z \cup \{x_m\}$ bị phá vỡ bởi $G$. Do đó, $\text{VCdim}(G_2) \leq \text{VCdim}(G) - 1 = d - 1$, và theo giả thuyết quy nạp: $|G_2| \leq \sum_{i=0}^{d-1} \binom{m-1}{i}$.

Do đó:

$$|G| = |G_1| + |G_2| \leq \sum_{i=0}^{d} \binom{m-1}{i} + \sum_{i=0}^{d-1} \binom{m-1}{i} = \sum_{i=0}^{d} \left[\binom{m-1}{i} + \binom{m-1}{i-1}\right] = \sum_{i=0}^{d} \binom{m}{i},$$

hoàn tất chứng minh quy nạp. $\square$

Ý nghĩa của bổ đề Sauer có thể được thấy qua Hệ quả 3.18, đáng chú ý cho thấy hàm tăng trưởng chỉ thể hiện hai loại hành vi: hoặc $\text{VCdim}(H) = d < +\infty$, trong trường hợp đó $\Pi_H(m) = O(m^d)$, hoặc $\text{VCdim}(H) = +\infty$, trong trường hợp đó $\Pi_H(m) = 2^m$.

**Hệ quả 3.18** Gọi $H$ là tập giả thuyết với $\text{VCdim}(H) = d$. Khi đó với mọi $m \geq d$,

$$\Pi_H(m) \leq \left(\frac{em}{d}\right)^d = O(m^d). \quad (3.28)$$

**Chứng minh:** Chứng minh bắt đầu bằng cách sử dụng bổ đề Sauer. Bất đẳng thức đầu tiên nhân mỗi hạng với hệ số lớn hơn hoặc bằng một vì $m \geq d$, trong khi bất đẳng thức thứ hai thêm các hạng không âm vào tổng.

$$\Pi_H(m) \leq \sum_{i=0}^{d}\binom{m}{i} \leq \sum_{i=0}^{d}\binom{m}{i}\left(\frac{m}{d}\right)^{d-i} \leq \sum_{i=0}^{m}\binom{m}{i}\left(\frac{m}{d}\right)^{d-i} = \left(\frac{m}{d}\right)^d \sum_{i=0}^{m}\binom{m}{i}\left(\frac{d}{m}\right)^i = \left(\frac{m}{d}\right)^d\left(1 + \frac{d}{m}\right)^m \leq \left(\frac{m}{d}\right)^d e^d.$$

Sau khi đơn giản biểu thức bằng định lý nhị thức, bất đẳng thức cuối suy từ bất đẳng thức tổng quát $(1 - x) \leq e^{-x}$. $\square$

Mối quan hệ rõ ràng vừa được thiết lập giữa chiều VC và hàm tăng trưởng kết hợp với Hệ quả 3.9 dẫn ngay đến các cận khái quát hóa sau dựa trên chiều VC.

**Hệ quả 3.19 (Cận khái quát hóa chiều VC)** Gọi $H$ là một họ hàm nhận giá trị trong $\{-1, +1\}$ với chiều VC bằng $d$. Khi đó, với mọi $\delta > 0$, với xác suất ít nhất $1 - \delta$, với mọi $h \in H$:

$$R(h) \leq \hat{R}_S(h) + \sqrt{\frac{2d\log\frac{em}{d}}{m}} + \sqrt{\frac{\log\frac{1}{\delta}}{2m}}. \quad (3.29)$$

Do đó, dạng của cận khái quát hóa này là

$$R(h) \leq \hat{R}_S(h) + O\left(\sqrt{\frac{\log(m/d)}{m/d}}\right), \quad (3.30)$$

nhấn mạnh tầm quan trọng của tỷ lệ $m/d$ cho khái quát hóa. Định lý cung cấp một trường hợp khác của nguyên lý Dao cạo Occam trong đó tính đơn giản được đo bằng chiều VC nhỏ hơn.

Các cận chiều VC có thể được dẫn ra trực tiếp mà không sử dụng cận trung gian độ phức tạp Rademacher, kết hợp bổ đề Sauer với (3.23) dẫn đến cận xác suất cao:

$$R(h) \leq \hat{R}_S(h) + \sqrt{\frac{8d\log\frac{2em}{d} + 8\log\frac{4}{\delta}}{m}},$$

có dạng tổng quát của (3.30). Hệ số $\log$ chỉ đóng vai trò nhỏ trong các cận này. Phân tích tinh tế hơn có thể được sử dụng để loại bỏ hệ số đó.

## 3.4 Cận dưới

Trong phần trước, chúng ta đã trình bày một số cận trên về sai số khái quát hóa. Ngược lại, phần này cung cấp các cận dưới về sai số khái quát hóa của bất kỳ thuật toán học nào theo chiều VC của tập giả thuyết được sử dụng. Các cận dưới này được chứng minh bằng cách tìm cho mọi thuật toán một phân phối 'xấu'. Vì thuật toán học là tùy ý, sẽ khó để chỉ rõ phân phối cụ thể đó. Thay vào đó, chỉ cần chứng minh sự tồn tại của nó một cách không xây dựng. Ở mức cao, kỹ thuật chứng minh được sử dụng để đạt được điều này là phương pháp xác suất (probabilistic method) của Paul Erdős. Trong ngữ cảnh các chứng minh sau, đầu tiên một cận dưới được đưa ra cho sai số kỳ vọng trên các tham số định nghĩa các phân phối. Từ đó, cận dưới được chứng minh là đúng cho ít nhất một bộ tham số, tức một phân phối.

**Định lý 3.20 (Cận dưới, trường hợp khả thi)** Gọi $H$ là tập giả thuyết với chiều VC $d > 1$. Khi đó, với mọi $m \geq 1$ và mọi thuật toán học $A$, tồn tại một phân phối $D$ trên $\mathcal{X}$ và một hàm mục tiêu $f \in H$ sao cho

$$\underset{S \sim D^m}{\mathbb{P}}\left[R_D(h_S, f) > \frac{d-1}{32m}\right] \geq 1/100. \quad (3.31)$$

**Chứng minh:** Gọi $X = \{x_0, x_1, \ldots, x_{d-1}\} \subseteq \mathcal{X}$ là tập bị phá vỡ bởi $H$. Với mọi $\epsilon > 0$, chúng ta chọn $D$ sao cho giá của nó giới hạn trong $X$ và một điểm ($x_0$) có xác suất rất cao ($1 - 8\epsilon$), với phần còn lại của khối lượng xác suất phân bố đều giữa các điểm khác:

$$\mathbb{P}_D[x_0] = 1 - 8\epsilon \quad \text{và} \quad \forall i \in [d-1], \; \mathbb{P}_D[x_i] = \frac{8\epsilon}{d-1}. \quad (3.32)$$

Với định nghĩa này, hầu hết các mẫu sẽ chứa $x_0$ và, vì $X$ bị phá vỡ, $A$ cơ bản không thể làm tốt hơn việc tung đồng xu khi xác định nhãn của điểm $x_i$ không nằm trong tập huấn luyện.

Chúng ta giả sử không mất tính tổng quát rằng $A$ không mắc sai số trên $x_0$. Với mẫu $S$, chúng ta gọi $\bar{S}$ là tập các phần tử rơi vào $\{x_1, \ldots, x_{d-1}\}$, và gọi $\mathcal{S}$ là tập các mẫu $S$ kích thước $m$ sao cho $|\bar{S}| \leq (d-1)/2$. Cố định mẫu $S \in \mathcal{S}$, và xét phân phối đều $U$ trên tất cả các gán nhãn $f: X \to \{0, 1\}$, tất cả đều thuộc $H$ vì tập bị phá vỡ. Khi đó, cận dưới sau đúng:

$$\underset{f \sim U}{\mathbb{E}}[R_D(h_S, f)] = \sum_f \sum_{x \in X} \mathbf{1}_{h_S(x) \neq f(x)} \mathbb{P}[x]\mathbb{P}[f] \geq \sum_f \sum_{x \notin \bar{S}} \mathbf{1}_{h_S(x) \neq f(x)} \mathbb{P}[x]\mathbb{P}[f]$$

$$= \sum_{x \notin \bar{S}} \left(\sum_f \mathbf{1}_{h_S(x) \neq f(x)}\mathbb{P}[f]\right)\mathbb{P}[x] = \frac{1}{2}\sum_{x \notin \bar{S}} \mathbb{P}[x] \geq \frac{1}{2} \cdot \frac{d-1}{2} \cdot \frac{8\epsilon}{d-1} = 2\epsilon. \quad (3.33)$$

Cận dưới đầu tiên đúng vì chúng ta loại bỏ các hạng không âm khi chỉ xét $x \notin \bar{S}$ thay vì tất cả $x$ trong $X$. Đẳng thức tiếp theo đúng vì chúng ta lấy kỳ vọng trên $f \in H$ phân bố đều và $H$ phá vỡ $X$. Cận dưới cuối đúng do định nghĩa $D$ và $\mathcal{S}$, phần sau suy ra $|X - \bar{S}| \geq (d-1)/2$.

Vì (3.33) đúng cho mọi $S \in \mathcal{S}$, nó cũng đúng trên kỳ vọng: $\mathbb{E}_{S \in \mathcal{S}}[\mathbb{E}_{f \sim U}[R_D(h_S, f)]] \geq 2\epsilon$. Theo định lý Fubini, các kỳ vọng có thể hoán đổi:

$$\underset{f \sim U}{\mathbb{E}}\left[\underset{S \in \mathcal{S}}{\mathbb{E}}\left[R_D(h_S, f)\right]\right] \geq 2\epsilon. \quad (3.34)$$

Điều này suy ra $\mathbb{E}_{S \in \mathcal{S}}[R_D(h_S, f_0)] \geq 2\epsilon$ cho ít nhất một gán nhãn $f_0 \in H$. Phân tách kỳ vọng thành hai phần và sử dụng $R_D(h_S, f_0) \leq \mathbb{P}_D[X - \{x_0\}]$, dẫn đến:

$$\underset{S \in \mathcal{S}}{\mathbb{P}}[R_D(h_S, f_0) \geq \epsilon] \geq \frac{1}{7}. \quad (3.35)$$

Do đó, xác suất trên tất cả các mẫu $S$ có thể được chặn dưới:

$$\underset{S}{\mathbb{P}}[R_D(h_S, f_0) \geq \epsilon] \geq \underset{S \in \mathcal{S}}{\mathbb{P}}[R_D(h_S, f_0) \geq \epsilon] \cdot \mathbb{P}[\mathcal{S}] \geq \frac{1}{7}\mathbb{P}[\mathcal{S}]. \quad (3.36)$$

Theo cận Chernoff nhân (Định lý D.4), với $\epsilon = (d-1)/(32m)$ và $\gamma = 1$, $\mathbb{P}[\mathcal{S}] \geq 7\delta$ cho $\delta \leq 0.01$. Do đó $\mathbb{P}_S[R_D(h_S, f_0) \geq \epsilon] \geq \delta$. $\square$

Định lý cho thấy rằng với mọi thuật toán $A$, tồn tại một phân phối 'xấu' trên $\mathcal{X}$ và một hàm mục tiêu $f$ mà sai số của giả thuyết được $A$ trả về là một hằng số nhân $d/m$ với một xác suất hằng số. Điều này chứng minh thêm vai trò then chốt của chiều VC trong học. Kết quả suy ra đặc biệt rằng PAC-learning trong trường hợp khả thi là không khả thi khi chiều VC vô hạn.

Lưu ý rằng chứng minh cho thấy một kết quả mạnh hơn phát biểu của định lý: phân phối $D$ được chọn độc lập với thuật toán $A$. Bây giờ chúng ta trình bày một định lý cho cận dưới trong trường hợp không khả thi. Hai bổ đề sau sẽ cần thiết cho chứng minh.

**Bổ đề 3.21** Gọi $\alpha$ là biến ngẫu nhiên phân bố đều nhận giá trị trong $\{\alpha_-, \alpha_+\}$, với $\alpha_- = 1/2 - \epsilon/2$ và $\alpha_+ = 1/2 + \epsilon/2$, và gọi $S$ là mẫu gồm $m \geq 1$ biến ngẫu nhiên $X_1, \ldots, X_m$ nhận giá trị trong $\{0, 1\}$ và được rút i.i.d. theo phân phối $D_\alpha$ xác định bởi $\mathbb{P}_{D_\alpha}[X = 1] = \alpha$. Gọi $h$ là hàm từ $\mathcal{X}^m$ tới $\{\alpha_-, \alpha_+\}$, khi đó:

$$\underset{\alpha}{\mathbb{E}}\left[\underset{S \sim D_\alpha^m}{\mathbb{P}}[h(S) \neq \alpha]\right] \geq \Phi(2\lceil m/2\rceil, \epsilon), \quad (3.39)$$

trong đó $\Phi(m, \epsilon) = \frac{1}{4}\left(1 - \sqrt{1 - \exp\left(-\frac{m\epsilon^2}{1-\epsilon^2}\right)}\right)$ cho mọi $m$ và $\epsilon$.

**Bổ đề 3.22** Gọi $Z$ là biến ngẫu nhiên nhận giá trị trong $[0, 1]$. Khi đó, với mọi $\gamma \in [0, 1)$,

$$\mathbb{P}[Z > \gamma] \geq \frac{\mathbb{E}[Z] - \gamma}{1 - \gamma} > \mathbb{E}[Z] - \gamma. \quad (3.40)$$

**Định lý 3.23 (Cận dưới, trường hợp không khả thi)** Gọi $H$ là tập giả thuyết với chiều VC $d > 1$. Khi đó, với mọi $m \geq 1$ và mọi thuật toán học $A$, tồn tại một phân phối $D$ trên $\mathcal{X} \times \{0, 1\}$ sao cho:

$$\underset{S \sim D^m}{\mathbb{P}}\left[R_D(h_S) - \inf_{h \in H} R_D(h) > \sqrt{\frac{d}{320m}}\right] \geq 1/64. \quad (3.41)$$

Tương đương, với mọi thuật toán học, độ phức tạp mẫu thỏa mãn

$$m \geq \frac{d}{320\epsilon^2}. \quad (3.42)$$

**Chứng minh:** Gọi $X = \{x_1, \ldots, x_d\} \subseteq \mathcal{X}$ là tập bị phá vỡ bởi $H$. Với mọi $\alpha \in [0, 1]$ và mọi vectơ $\boldsymbol{\sigma} = (\sigma_1, \ldots, \sigma_d)^\top \in \{-1, +1\}^d$, chúng ta định nghĩa phân phối $D_{\boldsymbol{\sigma}}$ trên $X \times \{0, 1\}$:

$$\forall i \in [d], \quad \mathbb{P}_{D_{\boldsymbol{\sigma}}}[(x_i, 1)] = \frac{1}{d}\left(\frac{1}{2} + \frac{\sigma_i \alpha}{2}\right). \quad (3.43)$$

Do đó, nhãn của mỗi điểm $x_i$, $i \in [d]$, tuân theo phân phối $\mathbb{P}_{D_{\boldsymbol{\sigma}}}[\cdot | x_i]$, phân phối của đồng xu lệch trong đó độ lệch được xác định bởi dấu của $\sigma_i$ và biên độ $\alpha$. Để xác định nhãn có khả năng nhất của mỗi điểm $x_i$, thuật toán học cần ước lượng $\mathbb{P}_{D_{\boldsymbol{\sigma}}}[1|x_i]$ với độ chính xác tốt hơn $\alpha$. Để làm điều này khó hơn, $\alpha$ và $\boldsymbol{\sigma}$ sẽ được chọn dựa trên thuật toán, yêu cầu $\Omega(1/\alpha^2)$ thực thể của mỗi điểm $x_i$ trong mẫu huấn luyện.

Rõ ràng, bộ phân loại Bayes $h^*_{D_{\boldsymbol{\sigma}}}$ được định nghĩa bởi $h^*_{D_{\boldsymbol{\sigma}}}(x_i) = \text{argmax}_{y \in \{0,1\}} \mathbb{P}[y|x_i] = \mathbf{1}_{\sigma_i > 0}$ cho mọi $i \in [d]$. Bộ phân loại $h^*_{D_{\boldsymbol{\sigma}}}$ thuộc $H$ vì $X$ bị phá vỡ. Với mọi $h \in H$,

$$R_{D_{\boldsymbol{\sigma}}}(h) - R_{D_{\boldsymbol{\sigma}}}(h^*_{D_{\boldsymbol{\sigma}}}) = \frac{\alpha}{d}\sum_{x \in X} \mathbf{1}_{h(x) \neq h^*_{D_{\boldsymbol{\sigma}}}(x)}. \quad (3.44)$$

Gọi $U$ là phân phối đều trên $\{-1, +1\}^d$. Theo (3.44) và qua phân tích bằng Bổ đề 3.21 (sử dụng tính lồi của $\Phi(\cdot, \alpha)$ và bất đẳng thức Jensen), ta có:

$$\underset{\substack{\boldsymbol{\sigma} \sim U \\ S \sim D_{\boldsymbol{\sigma}}^m}}{\mathbb{E}}\left[\frac{1}{\alpha}\left[R_{D_{\boldsymbol{\sigma}}}(h_S) - R_{D_{\boldsymbol{\sigma}}}(h^*_{D_{\boldsymbol{\sigma}}})\right]\right] \geq \Phi(m/d + 1, \alpha).$$

Vì kỳ vọng trên $\boldsymbol{\sigma}$ bị chặn dưới bởi $\Phi(m/d + 1, \alpha)$, phải tồn tại $\boldsymbol{\sigma} \in \{-1, +1\}^d$ thỏa bất đẳng thức (3.45). Theo Bổ đề 3.22, chọn $\alpha = 8\epsilon/(1 - 8\delta)$ và phân tích các điều kiện, ta thu được $\epsilon^2 \leq \frac{1}{320(m/d)}$ là điều kiện đủ, hoàn tất chứng minh. $\square$

Định lý cho thấy rằng với mọi thuật toán $A$, trong trường hợp không khả thi, tồn tại một phân phối 'xấu' trên $\mathcal{X} \times \{0, 1\}$ sao cho sai số của giả thuyết được $A$ trả về là một hằng số nhân $\sqrt{d/m}$ với một xác suất hằng số. Chiều VC xuất hiện như một đại lượng then chốt trong học tại thiết lập tổng quát này. Đặc biệt, với chiều VC vô hạn, PAC-learning bất khả tri không khả thi.

## 3.6 Bài tập

**3.1 Hàm tăng trưởng của các khoảng trong $\mathbb{R}$.** Gọi $H$ là tập các khoảng trong $\mathbb{R}$. Chiều VC của $H$ là 2. Tính hệ số phá vỡ $\Pi_H(m)$, $m \geq 0$. So sánh kết quả với cận tổng quát cho hàm tăng trưởng.

**3.2 Hàm tăng trưởng và độ phức tạp Rademacher của hàm ngưỡng trong $\mathbb{R}$.** Gọi $H$ là họ của các hàm ngưỡng trên đường thẳng thực: $H = \{x \mapsto \mathbf{1}_{x \leq \theta} : \theta \in \mathbb{R}\} \cup \{x \mapsto \mathbf{1}_{x \geq \theta} : \theta \in \mathbb{R}\}$. Đưa ra cận trên cho hàm tăng trưởng $\Pi_m(H)$. Sử dụng để dẫn ra cận trên cho $\mathfrak{R}_m(H)$.

**3.3 Hàm tăng trưởng của tổ hợp tuyến tính.** Một gán nhãn phân tách tuyến tính (linearly separable labeling) của tập $X$ gồm các vectơ trong $\mathbb{R}^d$ là một phân loại $X$ thành hai tập $X^+$ và $X^-$ với $X^+ = \{x \in X : w \cdot x > 0\}$ và $X^- = \{x \in X : w \cdot x < 0\}$ cho một $w \in \mathbb{R}^d$ nào đó. Gọi $X = \{x_1, \ldots, x_m\}$ là tập con của $\mathbb{R}^d$.

(a) Gọi $\{X^+, X^-\}$ là một lưỡng phân của $X$ và gọi $x_{m+1} \in \mathbb{R}^d$. Chứng minh rằng $\{X^+ \cup \{x_{m+1}\}, X^-\}$ và $\{X^+, X^- \cup \{x_{m+1}\}\}$ phân tách tuyến tính được bởi siêu phẳng đi qua gốc khi và chỉ khi $\{X^+, X^-\}$ phân tách tuyến tính được bởi siêu phẳng đi qua gốc và $x_{m+1}$.

(b) Gọi $X = \{x_1, \ldots, x_m\}$ là tập con của $\mathbb{R}^d$ sao cho mọi tập con $k$ phần tử với $k \leq d$ là độc lập tuyến tính. Khi đó, chứng minh rằng số gán nhãn phân tách tuyến tính của $X$ là $C(m, d) = 2\sum_{k=0}^{d-1}\binom{m-1}{k}$. *(Gợi ý: chứng minh bằng quy nạp rằng $C(m+1, d) = C(m, d) + C(m, d-1)$.)*

(c) Gọi $f_1, \ldots, f_p$ là $p$ hàm ánh xạ $\mathbb{R}^d$ tới $\mathbb{R}$. Định nghĩa $F$ là họ bộ phân loại dựa trên tổ hợp tuyến tính của các hàm này:

$$F = \left\{x \mapsto \text{sgn}\left(\sum_{k=1}^{p} a_k f_k(x)\right) : a_1, \ldots, a_p \in \mathbb{R}\right\}.$$

Định nghĩa $\Psi$ bởi $\Psi(x) = (f_1(x), \ldots, f_p(x))$. Giả sử tồn tại $x_1, \ldots, x_m \in \mathbb{R}^d$ sao cho mọi tập con $p$ phần tử của $\{\Psi(x_1), \ldots, \Psi(x_m)\}$ độc lập tuyến tính. Khi đó, chứng minh rằng

$$\Pi_F(m) = 2\sum_{i=0}^{p-1}\binom{m-1}{i}.$$

**3.4 Cận dưới cho hàm tăng trưởng.** Chứng minh rằng bổ đề Sauer (Định lý 3.17) là chặt, tức với mọi tập $X$ gồm $m > d$ phần tử, chứng minh rằng tồn tại lớp giả thuyết $H$ có chiều VC bằng $d$ sao cho $\Pi_H(m) = \sum_{i=0}^{d}\binom{m}{i}$.

**3.5 Cận trên Rademacher tinh tế hơn.** Chứng minh rằng cận trên tinh tế hơn cho độ phức tạp Rademacher của họ $G$ có thể cho bằng $\mathbb{E}_S[\Pi(G, S)]$, trong đó $\Pi(G, S)$ là số cách gán nhãn các điểm trong mẫu $S$.

**3.6 Lớp giả thuyết đơn.** Xét tập giả thuyết tầm thường $H = \{h_0\}$.

(a) Chứng minh rằng $\mathfrak{R}_m(H) = 0$ với mọi $m > 0$.

(b) Sử dụng xây dựng tương tự chứng minh bổ đề Massart (Định lý 3.7) là chặt.

**3.7 Lớp giả thuyết hai hàm.** Gọi $H$ là tập giả thuyết gồm hai hàm: $H = \{h_{-1}, h_{+1}\}$ và gọi $S = (x_1, \ldots, x_m) \subseteq \mathcal{X}$ là mẫu kích thước $m$.

(a) Giả sử $h_{-1}$ là hàm hằng nhận giá trị $-1$ và $h_{+1}$ là hàm hằng nhận giá trị $+1$. Chiều VC $d$ của $H$ là bao nhiêu? Chặn trên độ phức tạp Rademacher thực nghiệm $\hat{\mathfrak{R}}_S(H)$. *(Gợi ý: biểu diễn $\hat{\mathfrak{R}}_S(H)$ theo giá trị tuyệt đối của tổng các biến Rademacher và áp dụng bất đẳng thức Jensen.)* So sánh cận với $\sqrt{d/m}$.

(b) Giả sử $h_{-1}$ là hàm hằng nhận giá trị $-1$ và $h_{+1}$ là hàm nhận giá trị $-1$ mọi nơi trừ tại $x_1$ nơi nó nhận giá trị $+1$. Chiều VC $d$ của $H$ là bao nhiêu? Tính độ phức tạp Rademacher thực nghiệm $\hat{\mathfrak{R}}_S(H)$.

**3.8 Đẳng thức Rademacher.** Cố định $m \geq 1$. Chứng minh các đẳng thức sau với mọi $\alpha \in \mathbb{R}$ và hai tập giả thuyết $H$ và $H'$ gồm các hàm ánh xạ từ $\mathcal{X}$ tới $\mathbb{R}$:

(a) $\mathfrak{R}_m(\alpha H) = |\alpha|\mathfrak{R}_m(H)$.

(b) $\mathfrak{R}_m(H + H') = \mathfrak{R}_m(H) + \mathfrak{R}_m(H')$.

(c) $\mathfrak{R}_m(\{\max(h, h') : h \in H, h' \in H'\}) \leq \mathfrak{R}_m(H) + \mathfrak{R}_m(H')$, trong đó $\max(h, h')$ ký hiệu hàm $x \mapsto \max_{x \in \mathcal{X}}(h(x), h'(x))$. *(Gợi ý: bạn có thể sử dụng đẳng thức $\max(a, b) = \frac{1}{2}[a + b + |a - b|]$ đúng với mọi $a, b \in \mathbb{R}$ và bổ đề co rút Talagrand (xem Bổ đề 5.7).)*

**3.9 Độ phức tạp Rademacher của giao khái niệm.** Gọi $H_1$ và $H_2$ là hai họ hàm ánh xạ $\mathcal{X}$ tới $\{0, 1\}$ và gọi $H = \{h_1 h_2 : h_1 \in H_1, h_2 \in H_2\}$. Chứng minh rằng độ phức tạp Rademacher thực nghiệm của $H$ cho mọi mẫu $S$ kích thước $m$ có thể được chặn:

$$\hat{\mathfrak{R}}_S(H) \leq \hat{\mathfrak{R}}_S(H_1) + \hat{\mathfrak{R}}_S(H_2).$$

*(Gợi ý: sử dụng hàm Lipschitz $x \mapsto \max(0, x - 1)$ và bổ đề co rút Talagrand.)*

Sử dụng kết quả này để chặn độ phức tạp Rademacher $\mathfrak{R}_m(U)$ của họ $U$ các giao hai khái niệm $c_1$ và $c_2$ với $c_1 \in C_1$ và $c_2 \in C_2$ theo các độ phức tạp Rademacher của $C_1$ và $C_2$.

**3.10 Độ phức tạp Rademacher của vectơ dự đoán.** Gọi $S = (x_1, \ldots, x_m)$ là mẫu kích thước $m$ và cố định $h: \mathcal{X} \to \mathbb{R}$.

(a) Ký hiệu $u$ là vectơ dự đoán của $h$ cho $S$: $u = [h(x_1), \ldots, h(x_m)]^\top$. Đưa ra cận trên cho độ phức tạp Rademacher thực nghiệm $\hat{\mathfrak{R}}_S(H)$ của $H = \{h, -h\}$ theo $\|u\|_2$. *(Gợi ý: biểu diễn $\hat{\mathfrak{R}}_S(H)$ theo kỳ vọng giá trị tuyệt đối và áp dụng bất đẳng thức Jensen.)* Giả sử $h(x_i) \in \{0, -1, +1\}$ với mọi $i \in [m]$. Biểu diễn cận theo thước đo thưa thớt $n = |\{i : h(x_i) \neq 0\}|$. Cận trên cho các giá trị cực trị của thước đo thưa thớt là bao nhiêu?

(b) Gọi $F$ là họ hàm ánh xạ $\mathcal{X}$ tới $\mathbb{R}$. Đưa ra cận trên cho độ phức tạp Rademacher thực nghiệm của $F + h = \{f + h : f \in F\}$ và của $F \pm h = (F + h) \cup (F - h)$ theo $\hat{\mathfrak{R}}_S(F)$ và $\|u\|_2$.

**3.11 Độ phức tạp Rademacher của mạng nơ-ron chính quy hóa.** Gọi không gian đầu vào là $\mathcal{X} = \mathbb{R}^{n_1}$. Trong bài này, chúng ta xét họ mạng nơ-ron chính quy hóa được định nghĩa bởi tập hàm ánh xạ $\mathcal{X}$ tới $\mathbb{R}$ sau:

$$H = \left\{x \mapsto \sum_{j=1}^{n_2} w_j \sigma(u_j \cdot x) : \|w\|_1 \leq \Lambda', \|u_j\|_2 \leq \Lambda, \forall j \in [n_2]\right\},$$

trong đó $\sigma$ là hàm $L$-Lipschitz. Ví dụ, $\sigma$ có thể là hàm sigmoid, vốn là 1-Lipschitz.

(a) Chứng minh rằng $\hat{\mathfrak{R}}_S(H) = \frac{\Lambda'}{m}\mathbb{E}_\sigma\left[\sup_{\|u\|_2 \leq \Lambda}\left|\sum_{i=1}^{m}\sigma_i \sigma(u \cdot x_i)\right|\right]$.

(b) Sử dụng dạng sau của bổ đề Talagrand đúng cho mọi tập giả thuyết $H$ và hàm $L$-Lipschitz $\Phi$:

$$\frac{1}{m}\mathbb{E}_\sigma\left[\sup_{h \in H}\left|\sum_{i=1}^{m}\sigma_i(\Phi \circ h)(x_i)\right|\right] \leq \frac{L}{m}\mathbb{E}_\sigma\left[\sup_{h \in H}\left|\sum_{i=1}^{m}\sigma_i h(x_i)\right|\right],$$

để chặn trên $\hat{\mathfrak{R}}_S(H)$ theo độ phức tạp Rademacher thực nghiệm của $H'$, trong đó $H'$ được định nghĩa bởi

$$H' = \{x \mapsto s(u \cdot x) : \|u\|_2 \leq \Lambda, s \in \{-1, +1\}\}.$$

(c) Sử dụng bất đẳng thức Cauchy-Schwarz để chứng minh rằng

$$\hat{\mathfrak{R}}_S(H') = \frac{\Lambda}{m}\mathbb{E}_\sigma\left[\left\|\sum_{i=1}^{m}\sigma_i x_i\right\|_2\right].$$

(d) Sử dụng bất đẳng thức $\mathbb{E}_v[\|v\|_2] \leq \sqrt{\mathbb{E}_v[\|v\|_2^2]}$, đúng theo bất đẳng thức Jensen, để chặn trên $\hat{\mathfrak{R}}_S(H')$.

(e) Giả sử với mọi $x \in S$, $\|x\|_2 \leq r$ cho một $r > 0$ nào đó. Sử dụng các câu trước để dẫn ra cận trên cho độ phức tạp Rademacher của $H$ theo $r$.

**3.12 Độ phức tạp Rademacher.** Giáo sư Jesetoo tuyên bố tìm được cận tốt hơn cho độ phức tạp Rademacher của mọi tập giả thuyết $H$ gồm các hàm nhận giá trị trong $\{-1, +1\}$, theo chiều VC $\text{VCdim}(H)$ của nó. Cận của ông có dạng $\mathfrak{R}_m(H) \leq O\left(\frac{\text{VCdim}(H)}{m}\right)$. Bạn có thể chứng minh rằng tuyên bố của Giáo sư Jesetoo không thể đúng không? *(Gợi ý: xét tập giả thuyết $H$ chỉ gồm hai hàm đơn giản.)*

**3.13 Chiều VC của hợp $k$ khoảng.** Chiều VC của tập con đường thẳng thực tạo bởi hợp $k$ khoảng là gì?

**3.14 Chiều VC của tập giả thuyết hữu hạn.** Chứng minh rằng chiều VC của tập giả thuyết hữu hạn $H$ nhiều nhất là $\log_2 |H|$.

**3.15 Chiều VC của tập con.** Chiều VC của tập các tập con $I_\alpha$ của đường thẳng thực được tham số hóa bởi một tham số duy nhất $\alpha$: $I_\alpha = [\alpha, \alpha + 1] \cup [\alpha + 2, +\infty)$ là gì?

**3.16 Chiều VC của hình vuông và tam giác song song trục.**

(a) Chiều VC của hình vuông song song trục trong mặt phẳng là bao nhiêu?

(b) Xét các tam giác vuông trong mặt phẳng với hai cạnh kề góc vuông đều song song với các trục và góc vuông ở góc dưới bên trái. Chiều VC của họ này là bao nhiêu?

**3.17 Chiều VC của quả cầu đóng trong $\mathbb{R}^n$.** Chứng minh rằng chiều VC của tập tất cả các quả cầu đóng trong $\mathbb{R}^n$, tức các tập có dạng $\{x \in \mathbb{R}^n : \|x - x_0\|_2 \leq r\}$ cho một $x_0 \in \mathbb{R}^n$ và $r \geq 0$ nào đó, nhỏ hơn hoặc bằng $n + 2$.

**3.18 Chiều VC của ellipsoid.** Chiều VC của tập tất cả các ellipsoid trong $\mathbb{R}^n$ là bao nhiêu?

**3.19 Chiều VC của không gian vectơ hàm thực.** Gọi $F$ là không gian vectơ chiều hữu hạn gồm các hàm thực trên $\mathbb{R}^n$, $\dim(F) = r < \infty$. Gọi $H$ là tập các giả thuyết:

$$H = \{\{x : f(x) \geq 0\} : f \in F\}.$$

Chứng minh rằng $d$, chiều VC của $H$, là hữu hạn và $d \leq r$. *(Gợi ý: chọn tập tùy ý gồm $m = r + 1$ điểm và xét ánh xạ tuyến tính $u: F \to \mathbb{R}^m$ được định nghĩa bởi $u(f) = (f(x_1), \ldots, f(x_m))$.)*

**3.20 Chiều VC của hàm sin.** Xét họ hàm sin (Ví dụ 3.16): $\{x \to \sin(\omega x) : \omega \in \mathbb{R}\}$.

(a) Chứng minh rằng với mọi $x \in \mathbb{R}$, các điểm $x, 2x, 3x$ và $4x$ không thể bị phá vỡ bởi họ hàm sin này.

(b) Chứng minh rằng chiều VC của họ hàm sin là vô hạn. *(Gợi ý: chứng minh rằng $\{2^{-i} : i \leq m\}$ có thể bị phá vỡ với mọi $m > 0$.)*

**3.21 Chiều VC của hợp nửa không gian.** Đưa ra cận trên cho chiều VC của lớp giả thuyết mô tả bởi hợp $k$ nửa không gian.

**3.22 Chiều VC của giao nửa không gian.** Xét lớp $C_k$ các giao lồi $k$ nửa không gian. Đưa ra cận dưới và cận trên cho $\text{VCdim}(C_k)$.

**3.23 Chiều VC của giao khái niệm.**

(a) Gọi $C_1$ và $C_2$ là hai lớp khái niệm. Chứng minh rằng với mọi lớp khái niệm $C = \{c_1 \cap c_2 : c_1 \in C_1, c_2 \in C_2\}$,

$$\Pi_C(m) \leq \Pi_{C_1}(m)\Pi_{C_2}(m). \quad (3.53)$$

(b) Gọi $C$ là lớp khái niệm có chiều VC bằng $d$ và gọi $C_s$ là lớp khái niệm tạo bởi tất cả các giao $s$ khái niệm từ $C$, $s \geq 1$. Chứng minh rằng chiều VC của $C_s$ bị chặn bởi $2ds\log_2(3s)$. *(Gợi ý: chứng minh rằng $\log_2(3x) < 9x/(2e)$ với mọi $x \geq 2$.)*

**3.24 Chiều VC của hợp khái niệm.** Gọi $A$ và $B$ là hai tập hàm ánh xạ từ $\mathcal{X}$ tới $\{0, 1\}$, và giả sử cả $A$ và $B$ đều có chiều VC hữu hạn, với $\text{VCdim}(A) = d_A$ và $\text{VCdim}(B) = d_B$. Gọi $C = A \cup B$ là hợp của $A$ và $B$.

(a) Chứng minh rằng với mọi $m$, $\Pi_C(m) \leq \Pi_A(m) + \Pi_B(m)$.

(b) Sử dụng bổ đề Sauer để chứng minh rằng với $m \geq d_A + d_B + 2$, $\Pi_C(m) < 2^m$, và đưa ra cận cho chiều VC của $C$.

**3.25 Chiều VC của hiệu đối xứng.** Với hai tập $A$ và $B$, gọi $A \Delta B$ là hiệu đối xứng của $A$ và $B$, tức $A \Delta B = (A \cup B) - (A \cap B)$. Gọi $H$ là họ không rỗng các tập con của $\mathcal{X}$ có chiều VC hữu hạn. Gọi $A$ là một phần tử của $H$ và định nghĩa $H \Delta A = \{X \Delta A : X \in H\}$. Chứng minh rằng

$$\text{VCdim}(H \Delta A) = \text{VCdim}(H).$$

**3.26 Hàm đối xứng.** Một hàm $h: \{0, 1\}^n \to \{0, 1\}$ gọi là đối xứng nếu giá trị của nó được xác định duy nhất bởi số lượng bit 1 trong đầu vào. Gọi $C$ là tập tất cả các hàm đối xứng.

(a) Xác định chiều VC của $C$.

(b) Đưa ra cận dưới và cận trên cho độ phức tạp mẫu của bất kỳ thuật toán PAC-learning nhất quán nào cho $C$.

(c) Lưu ý rằng bất kỳ giả thuyết $h \in C$ nào có thể được biểu diễn bởi vectơ $(y_0, y_1, \ldots, y_n) \in \{0, 1\}^{n+1}$, trong đó $y_i$ là giá trị của $h$ trên các ví dụ có chính xác $i$ bit 1. Thiết kế một thuật toán học nhất quán cho $C$ dựa trên biểu diễn này.

**3.27 Chiều VC của mạng nơ-ron.** Gọi $C$ là lớp khái niệm trên $\mathbb{R}^r$ có chiều VC bằng $d$. Một mạng nơ-ron $C$ với một lớp trung gian là một khái niệm được định nghĩa trên $\mathbb{R}^n$ có thể được biểu diễn bởi đồ thị có hướng phi chu trình, trong đó các nút đầu vào ở dưới cùng và mỗi nút khác được gán nhãn với một khái niệm $c \in C$.

Đầu ra của mạng nơ-ron cho vectơ đầu vào $(x_1, \ldots, x_n)$ thu được như sau. Đầu tiên, mỗi trong $n$ nút đầu vào được gán giá trị $x_i \in \mathbb{R}$ tương ứng. Tiếp theo, giá trị tại nút $u$ ở lớp cao hơn được gán nhãn $c$ thu được bằng cách áp $c$ lên giá trị các nút đầu vào có cạnh kết thúc tại $u$. Vì $c$ nhận giá trị trong $\{0, 1\}$, giá trị tại $u$ nằm trong $\{0, 1\}$. Giá trị tại nút đỉnh hoặc nút đầu ra thu được tương tự.

(a) Gọi $H$ là tập tất cả các mạng nơ-ron định nghĩa như trên với $k \geq 2$ nút nội. Chứng minh rằng hàm tăng trưởng $\Pi_H(m)$ có thể được chặn trên theo tích các hàm tăng trưởng của các tập giả thuyết định nghĩa tại mỗi lớp trung gian.

(b) Sử dụng kết quả trên để chặn trên chiều VC của mạng nơ-ron $C$. *(Gợi ý: bạn có thể sử dụng hệ quả $m = 2x\log_2(xy) \Rightarrow m > x\log_2(ym)$ đúng cho $m \geq 1$ và $x, y > 0$ với $xy > 4$.)*

(c) Gọi $C$ là họ lớp khái niệm được định nghĩa bởi hàm ngưỡng $C = \{\text{sgn}(\sum_{j=1}^{r}w_j x_j) : w \in \mathbb{R}^r\}$. Đưa ra cận trên cho chiều VC của $H$ theo $k$ và $r$.

**3.28 Chiều VC của tổ hợp lồi.** Gọi $H$ là họ hàm ánh xạ từ không gian đầu vào $\mathcal{X}$ tới $\{-1, +1\}$ và gọi $T$ là số nguyên dương. Đưa ra cận trên cho chiều VC của họ hàm $F_T$ định nghĩa bởi

$$F = \left\{\text{sgn}\left(\sum_{t=1}^{T}\alpha_t h_t\right) : h_t \in H, \alpha_t \geq 0, \sum_{t=1}^{T}\alpha_t \leq 1\right\}.$$

*(Gợi ý: bạn có thể sử dụng bài tập 3.27 và lời giải.)*

**3.29 Chiều VC vô hạn.**

(a) Chứng minh rằng nếu lớp khái niệm $C$ có chiều VC vô hạn thì nó không PAC-learnable.

(b) Trong kịch bản PAC-learning tiêu chuẩn, thuật toán học nhận tất cả ví dụ trước rồi tính giả thuyết. Trong thiết lập đó, PAC-learning các lớp khái niệm có chiều VC vô hạn là không khả thi như đã thấy ở câu trước.

Bây giờ hãy tưởng tượng kịch bản khác trong đó thuật toán học có thể luân phiên giữa rút thêm ví dụ và tính toán. Mục tiêu của bài này là chứng minh rằng PAC-learning khi đó có thể khả thi cho một số lớp khái niệm có chiều VC vô hạn.

Xét ví dụ trường hợp đặc biệt của lớp khái niệm $C$ gồm tất cả các tập con của số tự nhiên. Giáo sư Vitres có ý tưởng cho giai đoạn đầu của thuật toán $L$ PAC-learning $C$. Trong giai đoạn đầu, $L$ rút đủ số điểm $m$ sao cho xác suất rút một điểm vượt quá giá trị cực đại $M$ quan sát được là nhỏ với độ tin cậy cao. Bạn có thể hoàn thành ý tưởng của Giáo sư Vitres bằng cách mô tả giai đoạn hai của thuật toán sao cho nó PAC-learn $C$ không? Mô tả cần đi kèm với chứng minh rằng $L$ có thể PAC-learn $C$.

**3.30 Cận khái quát hóa chiều VC — trường hợp khả thi.** Trong bài tập này chúng ta chứng minh rằng cận cho trong Hệ quả 3.19 có thể được cải thiện thành $O(d\log(m/d)/m)$ trong trường hợp khả thi. Giả sử chúng ta ở trường hợp khả thi, tức khái niệm mục tiêu nằm trong lớp giả thuyết $H$. Chúng ta sẽ chứng minh rằng nếu giả thuyết $h$ nhất quán với mẫu $S \sim D^m$ thì với mọi $\epsilon > 0$ sao cho $m\epsilon \geq 8$

$$\mathbb{P}[R(h) > \epsilon] \leq 2\left[\frac{2em}{d}\right]^d 2^{-m\epsilon/2}. \quad (3.54)$$

(a) Gọi $H_S \subseteq H$ là tập con các giả thuyết nhất quán với mẫu $S$, gọi $\hat{R}_S(h)$ là sai số thực nghiệm đối với mẫu $S$ và định nghĩa $S'$ là mẫu độc lập khác được rút từ $D^m$. Chứng minh rằng bất đẳng thức sau đúng cho mọi $h_0 \in H_S$:

$$\mathbb{P}\left[\sup_{h \in H_S}|\hat{R}_S(h) - \hat{R}_{S'}(h)| > \frac{\epsilon}{2}\right] \geq \mathbb{P}\left[B(m, \epsilon) > \frac{m\epsilon}{2}\right]\mathbb{P}[R(h_0) > \epsilon],$$

trong đó $B(m, \epsilon)$ là biến ngẫu nhiên nhị thức với tham số $(m, \epsilon)$. *(Gợi ý: chứng minh và sử dụng sự kiện $\mathbb{P}[\hat{R}_S(h) \geq \epsilon/2] \geq \mathbb{P}[\hat{R}_S(h) > \epsilon/2 \wedge R(h) > \epsilon]$.)*

(b) Chứng minh rằng $\mathbb{P}[B(m, \epsilon) > m\epsilon/2] \geq 1/2$. Sử dụng bất đẳng thức này cùng kết quả từ (a) để chứng minh rằng với mọi $h_0 \in H_S$

$$\mathbb{P}[R(h_0) > \epsilon] \leq 2\mathbb{P}\left[\sup_{h \in H_S}|\hat{R}_S(h) - \hat{R}_{S'}(h)| > \frac{\epsilon}{2}\right].$$

(c) Thay vì rút hai mẫu, chúng ta có thể rút một mẫu $T$ kích thước $2m$ rồi phân chia ngẫu nhiên đều thành $S$ và $S'$. Vế phải của phần (b) khi đó có thể viết lại:

$$\mathbb{P}\left[\sup_{h \in H_S}|\hat{R}_S(h) - \hat{R}_{S'}(h)| > \frac{\epsilon}{2}\right] = \underset{T \sim D^{2m}: T \to [S, S']}{\mathbb{P}}\left[\exists h \in H : \hat{R}_S(h) = 0 \wedge \hat{R}_{S'}(h) > \frac{\epsilon}{2}\right].$$

Gọi $h_0$ là giả thuyết sao cho $\hat{R}_T(h_0) > \epsilon/2$ và gọi $l > m\epsilon/2$ là tổng số sai số $h_0$ mắc trên $T$. Chứng minh rằng xác suất tất cả $l$ sai số rơi vào $S'$ được chặn trên bởi $2^{-l}$.

(d) Phần (b) suy ra rằng với mọi $h \in H$

$$\underset{T \sim D^{2m}: T \to (S, S')}{\mathbb{P}}\left[\hat{R}_S(h) = 0 \wedge \hat{R}_{S'}(h) > \frac{\epsilon}{2} \;\middle|\; \hat{R}_T(h_0) > \frac{\epsilon}{2}\right] \leq 2^{-l}.$$

Sử dụng cận này để chứng minh rằng với mọi $h \in H$

$$\underset{T \sim D^{2m}: T \to (S, S')}{\mathbb{P}}\left[\hat{R}_S(h) = 0 \wedge \hat{R}_{S'}(h) > \frac{\epsilon}{2}\right] \leq 2^{-\epsilon m/2}.$$

(e) Hoàn tất chứng minh bất đẳng thức (3.54) bằng cách sử dụng bổ đề hợp để chặn trên $\mathbb{P}_{T \sim D^{2m}: T \to (S, S')}[\exists h \in H : \hat{R}_S(h) = 0 \wedge \hat{R}_{S'}(h) > \epsilon/2]$. Chứng minh rằng chúng ta có thể đạt cận khái quát hóa xác suất cao bậc $O(d\log(m/d)/m)$.

**3.31 Cận khái quát hóa dựa trên số phủ.** Gọi $H$ là họ hàm ánh xạ $\mathcal{X}$ tới tập con $Y \subseteq \mathbb{R}$ của số thực. Với mọi $\epsilon > 0$, số phủ $N(H, \epsilon)$ của $H$ cho chuẩn $L_\infty$ là $k \in \mathbb{N}$ nhỏ nhất sao cho $H$ có thể được phủ bởi $k$ quả cầu bán kính $\epsilon$, tức tồn tại $\{h_1, \ldots, h_k\} \subseteq H$ sao cho với mọi $h \in H$, tồn tại $i \leq k$ với $\|h - h_i\|_\infty = \max_{x \in \mathcal{X}} |h(x) - h_i(x)| \leq \epsilon$. Đặc biệt, khi $H$ là tập compact, phủ hữu hạn có thể được trích từ phủ của $H$ bởi quả cầu bán kính $\epsilon$ và do đó $N(H, \epsilon)$ hữu hạn.

Số phủ cung cấp thước đo cho độ phức tạp của lớp hàm: số phủ càng lớn, họ hàm càng phong phú. Mục tiêu của bài này là minh họa điều đó bằng cách chứng minh cận học trong trường hợp mất mát bình phương. Gọi $D$ là phân phối trên $\mathcal{X} \times Y$ theo đó các ví dụ có nhãn được rút. Khi đó, sai số khái quát hóa của $h \in H$ cho mất mát bình phương được định nghĩa bởi $R(h) = \mathbb{E}_{(x,y) \sim D}[(h(x) - y)^2]$ và sai số thực nghiệm cho mẫu có nhãn $S = ((x_1, y_1), \ldots, (x_m, y_m))$ bởi $\hat{R}_S(h) = \frac{1}{m}\sum_{i=1}^{m}(h(x_i) - y_i)^2$. Chúng ta giả sử $H$ bị chặn, tức tồn tại $M > 0$ sao cho $|h(x) - y| \leq M$ với mọi $(x, y) \in \mathcal{X} \times Y$. Cận khái quát hóa được chứng minh trong bài này là:

$$\underset{S \sim D^m}{\mathbb{P}}\left[\sup_{h \in H}|R(h) - \hat{R}_S(h)| \geq \epsilon\right] \leq N\left(H, \frac{\epsilon}{8M}\right) \cdot 2\exp\left(-\frac{m\epsilon^2}{2M^4}\right). \quad (3.55)$$

Chứng minh dựa trên các bước sau.

(a) Gọi $L_S = R(h) - \hat{R}_S(h)$, chứng minh rằng với mọi $h_1, h_2 \in H$ và mọi mẫu có nhãn $S$, bất đẳng thức sau đúng:

$$|L_S(h_1) - L_S(h_2)| \leq 4M\|h_1 - h_2\|_\infty.$$

(b) Giả sử $H$ có thể được phủ bởi $k$ tập con $B_1, \ldots, B_k$, tức $H = B_1 \cup \ldots \cup B_k$. Khi đó, chứng minh rằng với mọi $\epsilon > 0$, cận trên sau đúng:

$$\underset{S \sim D^m}{\mathbb{P}}\left[\sup_{h \in H}|L_S(h)| \geq \epsilon\right] \leq \sum_{i=1}^{k}\underset{S \sim D^m}{\mathbb{P}}\left[\sup_{h \in B_i}|L_S(h)| \geq \epsilon\right].$$

(c) Cuối cùng, gọi $k = N(H, \epsilon/(8M))$ và gọi $B_1, \ldots, B_k$ là các quả cầu bán kính $\epsilon/(8M)$ có tâm $h_1, \ldots, h_k$ phủ $H$. Sử dụng phần (a) để chứng minh rằng với mọi $i \in [k]$,

$$\underset{S \sim D^m}{\mathbb{P}}\left[\sup_{h \in B_i}|L_S(h)| \geq \epsilon\right] \leq \underset{S \sim D^m}{\mathbb{P}}\left[|L_S(h_i)| \geq \frac{\epsilon}{2}\right],$$

và áp dụng bất đẳng thức Hoeffding (Định lý D.2) để chứng minh (3.55).

