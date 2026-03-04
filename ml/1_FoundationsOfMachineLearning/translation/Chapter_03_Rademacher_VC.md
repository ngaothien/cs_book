# Chương 3: Độ Phức Tạp Rademacher và VC-Dimension (Rademacher Complexity and VC-Dimension)

Trong chương trước, ta đã trình bày các biên khái quát hóa cho tập giả thuyết hữu hạn. Trong chương này, ta sẽ trình bày các biên khái quát hóa phụ thuộc vào **độ phức tạp** của tập giả thuyết — cụ thể là **độ phức tạp Rademacher** (Rademacher complexity), **hàm tăng trưởng** (growth function) và **VC-dimension** — các khái niệm cơ bản trong lý thuyết học máy.

## 3.1 Độ phức tạp Rademacher (Rademacher complexity)

Phần này giới thiệu khái niệm độ phức tạp Rademacher, một thước đo độ phong phú của họ hàm dựa trên khả năng khớp với nhiễu ngẫu nhiên.

Cho $H$ là tập giả thuyết gồm các hàm $h: X \to Y$ và $L: Y \times Y \to \mathbb{R}$ là hàm mất mát. Ta xét họ hàm mất mát liên kết:

$$G = \{g: (x, y) \mapsto L(h(x), y) : h \in H\}$$

**Định nghĩa 3.1 (Độ phức tạp Rademacher thực nghiệm — Empirical Rademacher complexity)**. Cho $G$ là họ hàm ánh xạ từ $Z$ sang $[a, b]$ và $S = (z_1, \ldots, z_m)$ là mẫu cố định kích thước $m$. Độ phức tạp Rademacher thực nghiệm của $G$ đối với mẫu $S$:

$$\hat{R}_S(G) = \underset{\sigma}{\mathbb{E}}\left[\sup_{g \in G} \frac{1}{m} \sum_{i=1}^{m} \sigma_i g(z_i)\right] \tag{3.1}$$

trong đó $\sigma = (\sigma_1, \ldots, \sigma_m)^\top$ với $\sigma_i$ là các biến ngẫu nhiên đều độc lập nhận giá trị trong $\{-1, +1\}$, gọi là **biến Rademacher** (Rademacher variables).

Tích vô hướng $\sigma \cdot g_S$ đo **tương quan** (correlation) giữa $g_S$ và vector nhiễu ngẫu nhiên $\sigma$. Supremum $\sup_{g \in G} \frac{\sigma \cdot g_S}{m}$ đo mức họ $G$ tương quan với $\sigma$ trên $S$. Họ phong phú/phức tạp hơn có thể tương quan tốt hơn với nhiễu ngẫu nhiên.

**Định nghĩa 3.2 (Độ phức tạp Rademacher — Rademacher complexity)**. Cho $D$ là phân phối rút mẫu. Với mọi $m \geq 1$:

$$R_m(G) = \underset{S \sim D^m}{\mathbb{E}}[\hat{R}_S(G)] \tag{3.2}$$

**Định lý 3.3 (Biên dựa trên Rademacher)**. Cho $G$ là họ hàm ánh xạ từ $Z$ sang $[0, 1]$. Với mọi $\delta > 0$, với xác suất ít nhất $1 - \delta$ trên mẫu i.i.d. $S$ kích thước $m$, với mọi $g \in G$:

$$\mathbb{E}[g(z)] \leq \frac{1}{m}\sum_{i=1}^{m} g(z_i) + 2R_m(G) + \sqrt{\frac{\log\frac{1}{\delta}}{2m}} \tag{3.3}$$

$$\mathbb{E}[g(z)] \leq \frac{1}{m}\sum_{i=1}^{m} g(z_i) + 2\hat{R}_S(G) + 3\sqrt{\frac{\log\frac{2}{\delta}}{2m}} \tag{3.4}$$

**Chứng minh**: Định nghĩa $\Phi(S) = \sup_{g \in G}(\mathbb{E}[g] - \hat{E}_S[g])$. Bước thay mẫu ghost $S'$:

$$\mathbb{E}[\Phi(S)] = \mathbb{E}_S\left[\sup_{g \in G}(\mathbb{E}[g] - \hat{E}_S[g])\right] \leq \mathbb{E}_{S, S'}\left[\sup_{g \in G}(\hat{E}_{S'}[g] - \hat{E}_S[g])\right]$$

Đưa biến Rademacher $\sigma_i$ vào (không thay đổi kỳ vọng do tính đối xứng) và dùng tính dưới-cộng (sub-additivity) của supremum:

$$\mathbb{E}[\Phi(S)] \leq 2\underset{\sigma, S}{\mathbb{E}}\left[\sup_{g \in G} \frac{1}{m}\sum_{i=1}^{m} \sigma_i g(z_i)\right] = 2R_m(G) \tag{3.13}$$

Áp dụng bất đẳng thức McDiarmid ($|\Phi(S) - \Phi(S')| \leq 1/m$ khi thay 1 điểm) cho lần lượt $\Phi(S)$ và $R_m(G)$, sau đó dùng biên hợp. $\square$

**Bổ đề 3.4**. Cho $H$ là họ hàm nhận giá trị trong $\{-1, +1\}$ và $G$ là họ hàm mất mát zero-one liên kết. Khi đó:

$$\hat{R}_S(G) = \frac{1}{2}\hat{R}_{S_X}(H) \tag{3.16}$$

**Định lý 3.5 (Biên Rademacher cho phân loại nhị phân)**. Cho $H$ là họ hàm nhận giá trị $\{-1, +1\}$. Với mọi $\delta > 0$, với xác suất ít nhất $1 - \delta$, với mọi $h \in H$:

$$R(h) \leq \hat{R}_S(h) + R_m(H) + \sqrt{\frac{\log\frac{1}{\delta}}{2m}} \tag{3.17}$$

$$R(h) \leq \hat{R}_S(h) + \hat{R}_S(H) + 3\sqrt{\frac{\log\frac{2}{\delta}}{2m}} \tag{3.18}$$

## 3.2 Hàm tăng trưởng (Growth function)

**Hàm tăng trưởng** (growth function) $\Pi_H(m)$ đo số lượng **phân đôi** (dichotomies) tối đa mà $H$ có thể tạo ra trên $m$ điểm:

$$\Pi_H(m) = \max_{S \subseteq X, |S| = m} |H|_S| \tag{3.19}$$

trong đó $|H|_S|$ là số vector nhãn phân biệt mà $H$ gán cho $S$. Ta luôn có $\Pi_H(m) \leq 2^m$.

**Bổ đề Massart**. Cho $A \subseteq \mathbb{R}^m$ hữu hạn với $r = \max_{x \in A} \|x\|_2$. Khi đó:

$$\underset{\sigma}{\mathbb{E}}\left[\sup_{x \in A} \sum_{i=1}^{m} \sigma_i x_i\right] \leq r\sqrt{2\log|A|}$$

**Hệ quả 3.8 (Biên Rademacher qua hàm tăng trưởng)**. Cho $H$ nhận giá trị $\{-1, +1\}$:

$$R_m(G) \leq \sqrt{\frac{2\log\Pi_G(m)}{m}} \tag{3.21}$$

**Hệ quả 3.9 (Biên khái quát hóa qua hàm tăng trưởng)**. Với mọi $\delta > 0$, xác suất ít nhất $1 - \delta$, mọi $h \in H$:

$$R(h) \leq \hat{R}_S(h) + \sqrt{\frac{2\log\Pi_H(m)}{m}} + \sqrt{\frac{\log\frac{1}{\delta}}{2m}} \tag{3.22}$$

## 3.3 VC-dimension

**Phá vỡ (Shattering)**: Tập $S$ gồm $m \geq 1$ điểm bị **phá vỡ** bởi $H$ khi $H$ thực hiện tất cả $2^m$ phân đôi có thể, tức $\Pi_H(m) = 2^m$.

**Định nghĩa 3.10 (VC-dimension)**. VC-dimension của $H$ là kích thước tập lớn nhất có thể bị phá vỡ:

$$\text{VCdim}(H) = \max\{m : \Pi_H(m) = 2^m\} \tag{3.24}$$

### Các ví dụ

**Ví dụ 3.11 (Khoảng trên đường thẳng thực)**. Mọi hai điểm đều có thể bị phá vỡ. Không có tập ba điểm nào bị phá vỡ vì nhãn $(+, -, +)$ không thể thực hiện. $\text{VCdim}(\text{intervals in } \mathbb{R}) = 2$.

*Hình 3.1: VC-dimension của khoảng trên đường thẳng thực.*

**Ví dụ 3.12 (Siêu phẳng — Hyperplanes)**. Trong $\mathbb{R}^2$: ba điểm không thẳng hàng bất kỳ có thể bị phá vỡ. Bốn điểm không thể bị phá vỡ (hai trường hợp: bốn điểm trên bao lồi, hoặc một điểm bên trong).

*Hình 3.2: Phân đôi không thể thực hiện cho bốn điểm dùng siêu phẳng trong $\mathbb{R}^2$.*

Tổng quát trong $\mathbb{R}^d$: cận dưới — chọn $d+1$ điểm $x_0 = 0, x_i = e_i$. Với $w$ có tọa độ thứ $i$ bằng $y_i$, siêu phẳng $w \cdot x + y_0/2 = 0$ phá vỡ các điểm này:

$$\text{sgn}\left(w \cdot x_i + \frac{y_0}{2}\right) = y_i \tag{3.25}$$

Cận trên — dùng **Định lý Radon** (Theorem 3.13): mọi tập $d+2$ điểm trong $\mathbb{R}^d$ có thể phân hoạch thành $X_1, X_2$ sao cho bao lồi giao nhau → không thể tách bởi siêu phẳng.

$$\text{VCdim}(\text{hyperplanes in } \mathbb{R}^d) = d + 1$$

**Ví dụ 3.14 (Hình chữ nhật thẳng hàng trục)**. Bốn điểm hình thoi bị phá vỡ. Năm điểm: điểm bên trong có nhãn ngược → không thể. $\text{VCdim} = 4$.

*Hình 3.3: VC-dimension của hình chữ nhật thẳng hàng trục.*

**Ví dụ 3.15 (Đa giác lồi — Convex Polygons)**. Đa giác lồi $d$ cạnh: $\text{VCdim} = 2d+1$. Đa giác lồi tổng quát: $\text{VCdim} = +\infty$.

*Hình 3.4: Đa giác lồi $d$ cạnh phá vỡ $2d+1$ điểm.  
Hình 3.5: Hàm sine dùng cho phân loại.*

**Ví dụ 3.16 (Hàm Sine)**. Họ hàm $\{t \mapsto \sin(\omega t): \omega \in \mathbb{R}\}$. Chỉ có **một tham số** $\omega$ nhưng $\text{VCdim} = +\infty$. Cho thấy VC-dimension **không nhất thiết** bằng số tham số.

### Bổ đề Sauer (Sauer's lemma)

**Định lý 3.17 (Bổ đề Sauer)**. Cho $\text{VCdim}(H) = d$. Với mọi $m \in \mathbb{N}$:

$$\Pi_H(m) \leq \sum_{i=0}^{d} \binom{m}{i} \tag{3.27}$$

**Chứng minh**: Quy nạp theo $m + d$. Cố định $S = \{x_1, \ldots, x_m\}$ với $G = H|_S$. Xét $S_0 = \{x_1, \ldots, x_{m-1}\}$. Định nghĩa $G_1 = G|_{S_0}$ và $G_2 = \{g' \subseteq S_0 : g' \in G \wedge g' \cup \{x_m\} \in G\}$. Có $|G_1| + |G_2| = |G|$.

*Hình 3.6: Minh họa cách xây dựng $G_1$ và $G_2$.*

Vì $\text{VCdim}(G_1) \leq d$ và $\text{VCdim}(G_2) \leq d-1$, theo giả thuyết quy nạp:

$$|G| = |G_1| + |G_2| \leq \sum_{i=0}^{d}\binom{m-1}{i} + \sum_{i=0}^{d-1}\binom{m-1}{i} = \sum_{i=0}^{d}\binom{m}{i} \quad \square$$

**Hệ quả 3.18**. Nếu $\text{VCdim}(H) = d$ thì với $m \geq d$:

$$\Pi_H(m) \leq \left(\frac{em}{d}\right)^d = O(m^d) \tag{3.28}$$

Hàm tăng trưởng chỉ có hai hành vi: $O(m^d)$ (khi $d < +\infty$) hoặc $2^m$ (khi $d = +\infty$).

**Hệ quả 3.19 (Biên khái quát hóa dựa trên VC-dimension)**. Cho $\text{VCdim}(H) = d$, với xác suất ít nhất $1 - \delta$, mọi $h \in H$:

$$R(h) \leq \hat{R}_S(h) + \sqrt{\frac{2d\log\frac{em}{d}}{m}} + \sqrt{\frac{\log\frac{1}{\delta}}{2m}} \tag{3.29}$$

Dạng tổng quát nhấn mạnh tỉ số $m/d$:

$$R(h) \leq \hat{R}_S(h) + O\left(\sqrt{\frac{\log(m/d)}{m/d}}\right) \tag{3.30}$$

## 3.4 Cận dưới (Lower bounds)

**Định lý 3.20 (Cận dưới, trường hợp thực hiện được — realizable case)**. Cho $\text{VCdim}(H) = d > 1$. Với mọi $m \geq 1$ và mọi thuật toán $A$, tồn tại phân phối $D$ trên $X$ và hàm mục tiêu $f \in H$ sao cho:

$$\mathbb{P}_{S \sim D^m}\left[R_D(h_S, f) > \frac{d-1}{32m}\right] \geq \frac{1}{100} \tag{3.31}$$

**Chứng minh** (ý tưởng): Chọn $X = \{x_0, \ldots, x_{d-1}\}$ bị phá vỡ bởi $H$. Thiết kế $D$: $\mathbb{P}[x_0] = 1 - 8\epsilon$, $\mathbb{P}[x_i] = 8\epsilon/(d-1)$. Đối với nhãn phân phối đều $f \sim U$ (tất cả đều trong $H$ vì $X$ bị phá vỡ):

$$\underset{f \sim U}{\mathbb{E}}[R_D(h_S, f)] \geq 2\epsilon \tag{3.33}$$

Dùng Fubini → tồn tại $f_0$ cụ thể. Kết hợp với biên Chernoff nhân tính → $\epsilon = (d-1)/(32m)$. $\square$

**Định lý 3.23 (Cận dưới, trường hợp không thực hiện được — non-realizable case)**. Cho $\text{VCdim}(H) = d > 1$. Với mọi $m \geq 1$ và thuật toán $A$, tồn tại phân phối $D$ trên $X \times \{0, 1\}$:

$$\mathbb{P}_{S \sim D^m}\left[R_D(h_S) - \inf_{h \in H} R_D(h) > \sqrt{\frac{d}{320m}}\right] \geq \frac{1}{64} \tag{3.41}$$

Tương đương, độ phức tạp mẫu thỏa $m \geq \frac{d}{320\epsilon^2}$.

## 3.5 Ghi chú chương (Chapter notes)

Độ phức tạp Rademacher được giới thiệu bởi Koltchinskii (2001) và Bartlett & Mendelson (2002). VC-dimension do Vapnik và Chervonenkis (1971) đề xuất, là một trong những khái niệm trung tâm của lý thuyết học thống kê. Bổ đề Sauer được chứng minh độc lập bởi Sauer (1972), Shelah (1972) và Perles & Shelah. Cận dưới dựa trên phương pháp xác suất (probabilistic method) của Erdős. Kết quả cận dưới do Ehrenfeucht et al. (1989) và Anthony & Bartlett (1999).

## 3.6 Bài tập (Exercises)

**3.1** Chứng minh bổ đề Massart.

**3.2** Chỉ ra $\hat{R}_S(G) \leq \hat{R}_S(G')$ nếu $G \subseteq G'$.

**3.3** Tính $\hat{R}_S(G)$ khi $G = \{g\}$ — một hàm duy nhất.

**3.4** Chứng minh tính chất co lại (contraction) cho Rademacher: nếu $\phi$ là $L$-Lipschitz thì $\hat{R}_S(\phi \circ G) \leq L \cdot \hat{R}_S(G)$.

**3.5** Tính VC-dimension của lớp khái niệm "dải" (strips) $\{x : a \leq x \leq b\}$ trong $\mathbb{R}$.

**3.6** Tính VC-dimension của tập các hình tròn đồng tâm trong $\mathbb{R}^2$.

**3.7** Tính VC-dimension của lớp hình tròn tổng quát (không đồng tâm) trong $\mathbb{R}^2$.

**3.8** Tính VC-dimension của đa giác lồi $k$ cạnh.

**3.9–3.10** Biên trực tiếp qua hàm tăng trưởng.

**3.11** Chứng minh chi tiết Định lý 3.23 (cận dưới, non-realizable).

**3.12–3.13** Tính Rademacher complexity cho các họ hàm tuyến tính.

**3.14** Chứng minh Rademacher cho hàm có biên $[a, b]$ tổng quát.

**3.15–3.16** Mối liên hệ giữa VC-dimension và số tham số.

**3.17** Cho $H$ với VC-dimension $d$ hữu hạn. Chứng minh $H$ PAC-learnable.

**3.18** $\text{VCdim}(H_1 \cup H_2) \leq ?$

**3.19** Chứng minh VCdim của không gian vector chiều $r$ tối đa $r$.

**3.20** Chứng minh $\text{VCdim}(\sin(\omega t)) = +\infty$.

**3.21** VC-dimension của mạng nơ-ron. Cho mạng với $W$ trọng số: $\text{VCdim} \leq O(W\log W)$.
