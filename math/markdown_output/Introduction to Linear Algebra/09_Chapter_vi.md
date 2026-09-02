# **Chương 9**

# **Các Vectơ và Ma trận Phức (Complex Vectors and Matrices)**

# **Thực so với Phức (Real versus Complex)**
$\mathbb{R} = \text{đường thẳng chứa tất cả các số thực } -\infty < x < \infty \leftrightarrow \mathbb{C} = \text{mặt phẳng chứa tất cả các số phức } z = x + iy$
$|x| = \text{giá trị tuyệt đối của } x \leftrightarrow |z| = \sqrt{x^2 + y^2} = r = \text{giá trị tuyệt đối (hay mô-đun) của } z$
$1 \text{ và } -1 \text{ là nghiệm của } x^2 = 1 \leftrightarrow z = 1, w, \dots, w^{n-1} \text{ là nghiệm của } z^n = 1 \text{ với } w = e^{2\pi i / n}$
**Liên hợp phức (complex conjugate)** của $z = x + iy$ là $\bar{z} = x - iy$. $|z|^2 = x^2 + y^2 = z\bar{z}$ và $\overline{z + w} = \bar{z} + \bar{w}$.
**Dạng cực (polar form)** của $z = x + iy$ là $|z|e^{i\theta} = re^{i\theta} = r\cos\theta + ir\sin\theta$. Góc có $\tan \theta = y/x$.

$\mathbb{R}^n$: các vectơ có $n$ thành phần thực
độ dài (length): $\|x\|^2 = x_1^2 + \dots + x_n^2$
chuyển vị (transpose): $(A^T)_{ij} = A_{ji}$
tích vô hướng (dot product): $x^T y = x_1 y_1 + \dots + x_n y_n$
lý do cho $A^T$: $(Ax)^T y = x^T (A^T y)$
tính trực giao (orthogonality): $x^T y = 0$
ma trận đối xứng (symmetric matrices): $S = S^T$
$S = Q \Lambda Q^{-1} = Q \Lambda Q^T$ (với $A$ thực)
ma trận phản đối xứng (skew-symmetric matrices): $K^T = -K$
ma trận trực giao (orthogonal matrices): $Q^T = Q^{-1}$
các cột trực chuẩn (orthonormal columns): $Q^T Q = I$
$(Qx)^T(Qy) = x^T y$ và $\|Qx\| = \|x\|$

$\leftrightarrow$
$\mathbb{C}^n$: các vectơ có $n$ thành phần phức
độ dài (length): $\|z\|^2 = |z_1|^2 + \dots + |z_n|^2$
chuyển vị liên hợp (conjugate transpose): $(A^H)_{ij} = \bar{A}_{ji}$
tích vô hướng (inner product): $u^H v = \bar{u}_1 v_1 + \dots + \bar{u}_n v_n$
lý do cho $A^H$: $(Au)^H v = u^H (A^H v)$
tính trực giao (orthogonality): $u^H v = 0$
ma trận Hermitian (Hermitian matrices): $S = S^H$
$S = U \Lambda U^{-1} = U \Lambda U^H$ (với $A$ thực)
ma trận phản Hermitian (skew-Hermitian matrices): $K^H = -K$
ma trận unita (unitary matrices): $U^H = U^{-1}$
các cột trực chuẩn (orthonormal columns): $U^H U = I$
$(Ux)^H(Uy) = x^H y$ và $\|Uz\| = \|z\|$

Một phần trình bày đầy đủ về đại số tuyến tính phải bao gồm các số phức $z = x + iy$. Thậm chí khi ma trận là thực, *các giá trị riêng và vectơ riêng thường là phức*. Ví dụ: Ma trận quay $2 \times 2$ có các vectơ riêng phức $x = (1, i)$ và $x = (1, -i)$. Tôi sẽ tóm tắt Mục 9.1 và 9.2 trong vài từ khó quên này: Khi bạn lấy chuyển vị của một vectơ $v$ hoặc một ma trận $A$, *hãy lấy liên hợp của mọi phần tử* ($i$ **đổi thành** $-i$). Mục 9.3 nói về ma trận phức quan trọng nhất trong tất cả - *ma trận Fourier $F$*.

# **9.1 Số Phức (Complex Numbers)**

Bắt đầu với số ảo $i$. Mọi người đều biết rằng $x^2 = -1$ không có nghiệm thực. Khi bạn bình phương một số thực, kết quả không bao giờ âm. Vì vậy thế giới đã thống nhất về một nghiệm gọi là $i$. (Ngoại trừ các kỹ sư điện gọi nó là $j$.) Các số ảo tuân theo các quy tắc cộng và nhân bình thường, với một điểm khác biệt. *Thay thế $i^2$ bằng $-1$*.

Mục này trình bày những sự thật chính về các số phức. Đây là bài ôn tập cho một số sinh viên và là tài liệu tham khảo cho mọi người. Mọi thứ đều xuất phát từ $i^2 = -1$ và $e^{2\pi i} = 1$.

*Một số phức* (ví dụ $3 + 2i$) *là một số thực* (3) *cộng với một số ảo* (2i). Phép cộng giữ phần thực và phần ảo riêng biệt. Phép nhân sử dụng $i^2 = -1$:

| **Cộng:** | $(3 + 2i) + (3 + 2i) = 6 + 4i$            |
|------------------|-------------------------------------------|
| **Nhân:** | $(3 + 2i)(1 - i) = 3 + 2i - 2i^2 = 5 - i$ |

Nếu tôi cộng $3 + i$ với $1 - i$, kết quả là 4. Các số thực $3 + 1$ được tách biệt với các số ảo $i - i$. Chúng ta đang cộng các vectơ $(3, 1)$ và $(1, -1)$ để được $(4, 0)$.

Số $(1 + i)^2$ là $1 + i$ nhân $1 + i$. Các quy tắc cho ra kết quả đáng ngạc nhiên là $2i$:
$$(1 + i)(1 + i) = 1 + i + i + i^2 = 2i.$$

Trong mặt phẳng phức, $1 + i$ nằm ở góc $45^\circ$. Nó giống như vectơ $(1, 1)$. Khi chúng ta bình phương $1 + i$ để được $2i$, góc tăng gấp đôi thành $90^\circ$. Nếu chúng ta bình phương một lần nữa, kết quả là $(2i)^2 = -4$. Góc $90^\circ$ tăng gấp đôi thành $180^\circ$, hướng của một số thực âm.

Một số thực chỉ là một số phức $z = a + bi$, với phần ảo bằng 0: $b = 0$.

*Phần thực* là $a = \text{Re}(a + bi)$. *Phần ảo* là $b = \text{Im}(a + bi)$.

### **Mặt Phẳng Phức (The Complex Plane)**

Các số phức tương ứng với các điểm trên một mặt phẳng. Các số thực nằm dọc theo trục $x$. Các số thuần ảo nằm trên trục $y$. *Số phức $3 + 2i$ nằm ở điểm có tọa độ* $(3, 2)$. Số 0, tức là $0 + 0i$, nằm ở gốc tọa độ.

Việc cộng và trừ các số phức cũng giống như cộng và trừ các vectơ trong mặt phẳng. Thành phần thực giữ riêng biệt với thành phần ảo. Các vectơ đi từ đầu đến đuôi như bình thường. Mặt phẳng phức $\mathbb{C}^1$ giống như mặt phẳng hai chiều thông thường $\mathbb{R}^2$, ngoại trừ việc chúng ta nhân các số phức và chúng ta không nhân các vectơ.

Bây giờ đến một ý tưởng quan trọng. *Liên hợp phức của* $3 + 2i$ *là* $3 - 2i$. Liên hợp phức của $z = 1 - i$ là $\bar{z} = 1 + i$. Nói chung liên hợp của $z = a + bi$ là $\bar{z} = a - bi$. **(Một số tác giả sử dụng "dấu gạch ngang" trên con số và những người khác sử dụng "dấu sao": $z = z^*$.)** Các phần ảo của $z$ và "$\bar{z}$" có dấu ngược nhau. Trong mặt phẳng phức, $\bar{z}$ là ảnh của $z$ nằm ở phía bên kia của trục thực.

Hình 9.1: Số $z = a + bi$ tương ứng với điểm $(a, b)$ và vectơ $\begin{bmatrix} a \\ b \end{bmatrix}$.

Hai sự thật hữu ích. *Khi chúng ta nhân các liên hợp* $\bar{z}_1$ *và* $\bar{z}_2$*, chúng ta thu được liên hợp của* $z_1 z_2$. Và khi chúng ta cộng $\bar{z}_1$ và $\bar{z}_2$, chúng ta thu được liên hợp của $z_1 + z_2$:

$\bar{z}_1 + \bar{z}_2 = (3 - 2i) + (1 + i) = 4 - i$. Đây là liên hợp của $z_1 + z_2 = 4 + i$.
$\bar{z}_1 \times \bar{z}_2 = (3 - 2i) \times (1 + i) = 5 + i$. Đây là liên hợp của $z_1 \times z_2 = 5 - i$.

Việc cộng và nhân chính xác là những gì đại số tuyến tính cần. Bằng cách lấy liên hợp của $Ax = \lambda x$, khi $A$ là thực, chúng ta có một giá trị riêng khác $\bar{\lambda}$ và vectơ riêng của nó $\bar{x}$:

| Các giá trị riêng | $\lambda$ | $\text{và } \bar{\lambda}$ | $\text{Nếu } Ax = \lambda x$ | $\text{và } A \text{ là thực thì}$ | $A\bar{x} = \bar{\lambda}\bar{x}$ | (1) |
|-------------|-----------|---------------------|---------------------|----------------------|-----------------------------------|-----|

Có một điều đặc biệt xảy ra khi $z = 3 + 2i$ kết hợp với chính liên hợp phức của nó $\bar{z} = 3 - 2i$. Kết quả từ phép cộng $z + \bar{z}$ hoặc phép nhân $z\bar{z}$ luôn là số thực:

| $z + \bar{z} = \text{thực}$ | $(3 + 2i) + (3 - 2i) = 6$ (thực)                             |
|-----------------------------|--------------------------------------------------------------|
| $z\bar{z} = \text{thực}$    | $(3 + 2i) \times (3 - 2i) = 9 + 6i - 6i - 4i^2 = 13$ (thực). |

Tổng của $z = a + bi$ và liên hợp của nó $\bar{z} = a - bi$ là số thực $2a$. Tích của $z$ nhân với $\bar{z}$ là số thực $a^2 + b^2$:

| Nhân $z$ với $\bar{z}$ để thu được $|z|^2 = r^2$ | $(a + bi)(a - bi) = a^2 + b^2.$ | (2) |
|--------------------------------------------------------|---------------------------------|-----|

Bước tiếp theo với các số phức là $1/z$. Làm thế nào để chia cho $a + ib$? Ý tưởng tốt nhất là nhân trước tiên với $\bar{z}/\bar{z} = 1$. Điều đó tạo ra $z\bar{z}$ ở mẫu số, chính là $a^2 + b^2$:

| $\frac{1}{a+ib} = \frac{1}{a+ib} \frac{a-ib}{a-ib} = \frac{a-ib}{a^2+b^2}$ | $\frac{1}{3+2i} = \frac{1}{3+2i} \frac{3-2i}{3-2i} = \frac{3-2i}{13}$ |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------|

Trong trường hợp $a^2 + b^2 = 1$, điều này có nghĩa là $(a + ib)^{-1}$ là $a - ib$. *Trên vòng tròn đơn vị,* **$1/z$ bằng $\bar{z}$**. Sau này chúng ta sẽ nói: $1/e^{i\theta}$ là $e^{-i\theta}$. Hãy sử dụng khoảng cách $r$ và góc $\theta$ để nhân và chia.

# **Dạng Cực (The Polar Form) $re^{i\theta}$**

Căn bậc hai của $a^2 + b^2$ là $|z|$. Đây là *giá trị tuyệt đối* (hoặc *mô-đun*) của số $z = a + ib$. Căn bậc hai $|z|$ cũng được viết là $r$, bởi vì nó là khoảng cách từ $0$ đến $z$. *Số thực $r$ trong dạng cực cho biết kích thước của số phức $z$:*

| Giá trị tuyệt đối của $z = a + ib$ | $|z| = \sqrt{a^2 + b^2}$. | **Đây được gọi là $r$.** |
|------------------------------------|----------------------------|---------------------------------------|
| Giá trị tuyệt đối của $z = 3 + 2i$ | $|z| = \sqrt{3^2 + 2^2}$. | Đây là $r = \sqrt{13}$.             |

Phần còn lại của dạng cực là góc $\theta$. Góc cho $z = 5$ là $\theta = 0$ (vì $z$ này là số thực và dương). Góc cho $z = 3i$ là $\pi/2$ radian. Góc cho một số âm $z = -9$ là $\pi$ radian. *Góc sẽ tăng gấp đôi khi bình phương số đó.* Dạng cực rất tuyệt vời cho việc nhân các số phức (nhưng không tốt cho phép cộng).

Khi khoảng cách là $r$ và góc là $\theta$, lượng giác cho hai cạnh còn lại của tam giác. Phần thực (dọc theo cạnh đáy) là $a = r \cos \theta$. Phần ảo (lên hoặc xuống) là $b = r \sin \theta$. Đặt chúng lại với nhau, và dạng chữ nhật trở thành dạng cực $re^{i\theta}$.

| Con số | $z = a + ib$ | $\text{cũng là}$ | $z = r \cos \theta + ir \sin \theta$ | Đây là $re^{i\theta}$ |
|------------|--------------|-------------------|--------------------------------------|------------------------|

*Lưu ý:* $\cos \theta + i \sin \theta$ có giá trị tuyệt đối $r = 1$ *vì* $\cos^2 \theta + \sin^2 \theta = 1$. Do đó $\cos \theta + i \sin \theta$ nằm trên vòng tròn bán kính 1 - *vòng tròn đơn vị*.

**Ví dụ 1** Tìm $r$ và $\theta$ cho $z = 1 + i$ và cũng cho số liên hợp $\bar{z} = 1 - i$.

**Giải** Giá trị tuyệt đối là như nhau cho $z$ và $\bar{z}$. Nó là $r = \sqrt{1^2 + 1^2} = \sqrt{2}$:
| $z^2 = 1^2 + 1^2 = 2$ | và cũng | $\bar{z}^2 = 1^2 + (-1)^2 = 2$. |
|-------------------------|----------|------------------------------------|

Khoảng cách từ tâm là $r = \sqrt{2}$. Còn về góc $\theta$ thì sao? Số $1 + i$ nằm ở điểm $(1, 1)$ trong mặt phẳng phức. Góc tới điểm đó là $\pi / 4$ radian hay $45^\circ$. Cosin là $1/\sqrt{2}$ và sin là $1/\sqrt{2}$. Việc kết hợp $r$ và $\theta$ mang lại $z = 1 + i$:
$$r \cos \theta + ir \sin \theta = \sqrt{2} \left( \frac{1}{\sqrt{2}} \right) + i\sqrt{2} \left( \frac{1}{\sqrt{2}} \right) = 1 + i.$$

Góc tới số liên hợp $1 - i$ có thể là dương hoặc âm. Chúng ta có thể đi tới $7\pi / 4$ radian tương đương với $315^\circ$. Hoặc chúng ta có thể đi *ngược lại qua một góc âm*, tới $-\pi / 4$ radian hay $-45^\circ$. *Nếu $z$ ở góc $\theta$, thì số liên hợp $\bar{z}$ của nó ở $2\pi - \theta$ và cũng ở $-\theta$.*

Chúng ta có thể tự do cộng thêm $2\pi$ hoặc $4\pi$ hoặc $-2\pi$ vào bất kỳ góc nào! Những vòng này đi đủ một vòng tròn nên điểm cuối cùng là giống nhau. Điều này giải thích tại sao có vô số sự lựa chọn cho $\theta$. Thông thường chúng ta chọn góc giữa $0$ và $2\pi$. Nhưng $-\theta$ rất hữu ích cho số liên hợp $\bar{z}$. Và $1 = e^0 = e^{2\pi i}$.

#### **Lũy thừa và Tích: Dạng Cực (Powers and Products: Polar Form)**

Việc tính toán $(1 + i)^2$ và $(1 + i)^8$ nhanh nhất là ở dạng cực. Dạng đó có $r = \sqrt{2}$ và $\theta = \pi / 4$ (hoặc $45^\circ$). Nếu chúng ta bình phương giá trị tuyệt đối để được $r^2 = 2$, và nhân đôi góc để được $2\theta = \pi / 2$ (hoặc $90^\circ$), chúng ta có $(1 + i)^2$. Đối với lũy thừa bậc tám chúng ta cần $r^8$ và $8\theta$:
$$(1 + i)^8 = r^8 = 2 \cdot 2 \cdot 2 \cdot 2 = 16 \text{ và } 8\theta = 8 \cdot \frac{\pi}{4} = 2\pi.$$

Điều này có nghĩa là: $(1 + i)^8$ có giá trị tuyệt đối 16 và góc $2\pi$. *Vì vậy* $(1 + i)^8 = 16$.

Lũy thừa rất dễ dàng ở dạng cực. Việc nhân các số phức cũng vậy.

| Lũy thừa bậc $n$ của | $z = r(\cos \theta + i \sin \theta)$ | $\text{là}$ | $z^n = r^n(\cos n\theta + i \sin n\theta)$. | (3) |
|-------------------------|--------------------------------------|------|----------------------------------------------|-----|

Trong trường hợp đó $z$ tự nhân với chính nó. Để nhân $z$ với $z'$, *nhân các $r$ với nhau và cộng các góc:*
$$(\cos \theta + i \sin \theta) \text{ nhân với } r'(\cos \theta' + i \sin \theta') = rr'(\cos(\theta + \theta') + i \sin(\theta + \theta')). \quad (4)$$

Một cách để hiểu điều này là bằng lượng giác. Tại sao chúng ta lại thu được góc nhân đôi $2\theta$ cho $z^2$?
$$(\cos \theta + i \sin \theta) \times (\cos \theta + i \sin \theta) = \cos^2 \theta + i^2 \sin^2 \theta + 2i \sin \theta \cos \theta.$$

Phần thực $\cos^2 \theta - \sin^2 \theta$ là $\cos 2\theta$. Phần ảo $2 \sin \theta \cos \theta$ là $\sin 2\theta$. Đó là các công thức "góc nhân đôi". Chúng cho thấy $\theta$ trong $z$ trở thành $2\theta$ trong $z^2$.

Có một cách thứ hai để hiểu quy tắc cho $z^n$. Nó sử dụng công thức kỳ diệu duy nhất trong mục này. Hãy nhớ rằng $\cos \theta + i \sin \theta$ có giá trị tuyệt đối là 1. Cosin được tạo thành từ các lũy thừa chẵn, bắt đầu với $1 - \frac{1}{2}\theta^2$. Sin được tạo thành từ các lũy thừa lẻ, bắt đầu với $\theta - \frac{1}{6}\theta^3$. Sự thật đẹp đẽ là $e^{i\theta}$ kết hợp cả hai chuỗi đó thành $\cos \theta + i \sin \theta$:

| $e^x = 1 + x + \frac{1}{2}x^2 + \frac{1}{6}x^3 + \dots$ | $\text{trở thành}$ | $e^{i\theta} = 1 + i\theta + \frac{1}{2}i^2\theta^2 + \frac{1}{6}i^3\theta^3 + \dots$ |
|----------------------------------------------------------|---------|----------------------------------------------------------------------------------------|

Viết $-1$ thay cho $i^2$ để thấy $1 - \frac{1}{2}\theta^2$. *Số phức $e^{i\theta}$ là* $\cos \theta + i \sin \theta$:

| *Công thức Euler* | $e^{i\theta} = \cos \theta + i \sin \theta$ | $\text{cho ra}$ | $z = r \cos \theta + ir \sin \theta = re^{i\theta}$ | (5) |
|------------------------|---------------------------------------------|-------|-----------------------------------------------------|---------------|

Sự lựa chọn đặc biệt $\theta = 2\pi$ cho $\cos 2\pi + i \sin 2\pi$ chính là 1. Bằng một cách nào đó chuỗi vô hạn $e^{2\pi i} = 1 + 2\pi i + \frac{1}{2}(2\pi i)^2 + \dots$ cộng lại thành 1.

Bây giờ nhân $e^{i\theta}$ với $e^{i\theta'}$. Các góc cộng lại vì cùng một lý do mà các số mũ cộng lại:
| | | | | |
|---------------|---------------|----------------|---------------|---------------|
| $e^2$         | $\text{nhân với}$         | $e^3$          | $\text{là}$            | $e^5$         |
|               | $\text{nhân với}$         | $e^{i\theta'}$  | $\text{nhân với}$         | $e^{i\theta}$ |
|               | $\text{là}$            | $e^{i(\theta + \theta')}$ |               |               |

Các lũy thừa $(re^{i\theta})^n$ bằng $r^n e^{in\theta}$. Chúng nằm trên vòng tròn đơn vị khi $r = 1$ và $r^n = 1$. Khi đó chúng ta tìm thấy $n$ số khác nhau có lũy thừa bậc $n$ bằng 1:
Đặt $w = e^{2\pi i/n}$. Các lũy thừa bậc $n$ của $1, w, w^2, \dots, w^{n-1}$ đều bằng 1.

Chúng là các "căn bậc $n$ của 1". Chúng giải phương trình $z^n = 1$. Chúng cách đều nhau xung quanh vòng tròn đơn vị trong Hình 9.2b, nơi mà góc quay $2\pi$ được chia cho $n$. Nhân các góc của chúng với $n$ để lấy lũy thừa bậc $n$. Điều đó cho $w^n = e^{2\pi i}$ là 1. Tương tự $(w^2)^n = e^{4\pi i} = 1$. Mỗi con số đó, khi lấy lũy thừa bậc $n$, đều đi vòng quanh vòng tròn đơn vị để về 1.

$n$ nghiệm này của 1 là những con số then chốt cho xử lý tín hiệu. Biến đổi Fourier Rời rạc sử dụng $w = e^{2\pi i/n}$ và các lũy thừa của nó. Mục 9.3 chỉ ra cách phân tích một vectơ (một tín hiệu) thành $n$ tần số bằng Biến đổi Fourier Nhanh.

Hình 9.2: (a) $e^{i\theta}$ nhân $e^{i\theta'}$ là $e^{i(\theta + \theta')}$. (b) Lũy thừa bậc $n$ của $e^{2\pi i/n}$ là $e^{2\pi i} = 1$.

#### **■ ÔN TẬP CÁC Ý TƯỞNG THEN CHỐT (REVIEW OF THE KEY IDEAS) ■**

- **1.** Cộng $a+ ib$ với $c + id$ giống như cộng $(a, b) + (c, d)$. Sử dụng $i^2 = -1$ để nhân.
- **2.** Liên hợp của $z = a + bi = re^{i\theta}$ là $\bar{z} = z^* = a - bi = re^{-i\theta}$.
- **3.** $z$ nhân $\bar{z}$ là $re^{i\theta}$ nhân $re^{-i\theta}$. Kết quả là $r^2 = |z|^2 = a^2 + b^2$ (số thực).
- **4.** Lũy thừa và tích rất dễ dàng ở dạng cực $z = re^{i\theta}$. *Nhân* các $r$ và *cộng* các $\theta$.

# **Tập bài tập 9.1 (Problem Set 9.1)**

**Các câu hỏi 1-8 nói về các phép toán trên số phức.**

**1** Cộng và nhân mỗi cặp số phức:
(a) $2 + i, 2 - i$ (b) $-1 + i, -1 + i$ (c) $\cos \theta + i \sin \theta, \cos \theta - i \sin \theta$
**2** Xác định vị trí các điểm này trên mặt phẳng phức. Đơn giản hóa chúng nếu cần thiết:
(a) $2 + i$ (b) $(2 + i)^2$ (c) $\frac{1}{2 + i}$ (d) $\left| 2 + i \right|$
**3** Tìm giá trị tuyệt đối $r = |z|$ của bốn số này. Nếu $\theta$ là góc cho $6 - 8i$, thì góc cho ba số còn lại là bao nhiêu?
(a) $6 - 8i$ (b) $(6 - 8i)^2$ (c) $\frac{1}{6 - 8i}$ (d) $(6 + 8i)^2$
**4** Nếu $|z| = 2$ và $|w| = 3$ thì $|z \times w| = \_\_$ và $|z + w| \leq \_\_$ và $|z / w| = \_\_$ và $|z - w| \leq \_\_$.
**5** Tìm $a + ib$ cho các số ở các góc $30^\circ, 60^\circ, 90^\circ, 120^\circ$ trên vòng tròn đơn vị. Nếu $w$ là số ở $30^\circ$, hãy kiểm tra rằng $w^2$ ở $60^\circ$. Lũy thừa nào của $w$ bằng 1?
**6** Nếu $z = r \cos \theta + ir \sin \theta$ thì $1 / z$ có giá trị tuyệt đối \_\_ và góc \_\_. Dạng cực của nó là \_\_. Nhân $z \times 1/z$ để được 1.
**7** Phép nhân phức $M = (a + bi)(c + di)$ là một phép nhân thực $2 \times 2$
$$\begin{bmatrix} a & -b \\ b & a \end{bmatrix} \begin{bmatrix} c \\ d \end{bmatrix} = \begin{bmatrix} \_ \\ \_ \end{bmatrix}.$$
Vế phải chứa các phần thực và phần ảo của $M$. Hãy kiểm tra với $M = (1 + 3i)(1 - 3i)$.
**8** $A = A_1 + iA_2$ là một ma trận phức $n \times n$ và $b = b_1 + ib_2$ là một vectơ phức. Nghiệm của $Ax = b$ là $x_1 + ix_2$. Viết $Ax = b$ dưới dạng một hệ số thực có kích thước $2n$:
| Phức $n \times n$ | $\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} b_1 \\ b_2 \end{bmatrix}$ |
|--------------------|---------------------------------------------------------------------------------------|
| Thực $2n \times 2n$  |                                                                                       |

**Các câu hỏi 9-16 nói về liên hợp** $\bar{z} = a - ib = re^{-i\theta} = z^*$.

**9** Viết xuống liên hợp phức của mỗi số bằng cách đổi $i$ thành $-i$:
(a) $2 - i$ (b) $(2 - i)(1 - i)$ (c) $e^{i\pi/2}$ (chính là $i$)
(d) $e^{i\pi} = -1$ (e) $\frac{1}{2i\pi}$ (f) $i^{103} = \_\_$
**10** Tổng $z + \bar{z}$ luôn là \_\_. Hiệu $z - \bar{z}$ luôn là \_\_. Giả sử $z \neq 0$. Tích $z \times \bar{z}$ luôn là \_\_. Tỷ số $z / \bar{z}$ có giá trị tuyệt đối \_\_.
**11** Đối với một ma trận thực, liên hợp của $Ax = \lambda x$ là $A\bar{x} = \bar{\lambda}\bar{x}$. Điều này chứng minh hai điều: $\bar{\lambda}$ là một giá trị riêng khác và $\bar{x}$ là vectơ riêng của nó. Tìm các giá trị riêng $\lambda, \bar{\lambda}$ và các vectơ riêng $x, \bar{x}$ của $A = \begin{bmatrix} a & b \\ -b & a \end{bmatrix}$.
**12** Các giá trị riêng của một ma trận thực $2 \times 2$ có từ công thức bậc hai:
$$\det \begin{bmatrix} a - \lambda & b \\ c & d - \lambda \end{bmatrix} = \lambda^2 - (a + d)\lambda + (ad - bc) = 0$$
cho ra hai giá trị riêng $\lambda = \left[ (a + d) \pm \sqrt{(a + d)^2 - 4(ad - bc)} \right] / 2$.
(a) Nếu $a = b = d = 1$, các giá trị riêng là phức khi $c$ là \_\_.
(b) Các giá trị riêng là gì khi $ad = bc$?
**13** Trong Bài 12 các giá trị riêng không phải là số thực khi $(\text{vết})^2 = (a + d)^2$ nhỏ hơn \_\_. Chứng minh rằng các $\lambda$ là số thực khi $bc > 0$.
**14** Một ma trận phản đối xứng thực ($A^T = -A$) có các giá trị riêng thuần ảo. Chứng minh thứ nhất: Nếu $Ax = \lambda x$ thì nhân khối (block multiplication) cho ra
| $\begin{bmatrix} 0 & A \\ -A & 0 \end{bmatrix} \begin{bmatrix} x \\ ix \end{bmatrix} = i\lambda \begin{bmatrix} x \\ ix \end{bmatrix}$ |
|----------------------------------------------------------------------------------------------------------------------------------------|
Ma trận khối này là đối xứng. Các giá trị riêng của nó phải là \_\_! Vì vậy $\lambda$ là \_\_.

**Các câu hỏi 15-22 nói về dạng $re^{i\theta}$ của số phức $r \cos \theta + ir \sin \theta$.**

**15** Viết các số này dưới dạng Euler $re^{i\theta}$. Sau đó bình phương mỗi số:
(a) $1 + \sqrt{3}i$ (b) $\cos 2\theta + i \sin 2\theta$ (c) $-7i$ (d) $5 - 5i$.
**16** (Một câu hỏi yêu thích) Tìm giá trị tuyệt đối và góc cho $z = \sin \theta + i \cos \theta$ (cẩn thận). Xác định vị trí $z$ này trong mặt phẳng phức. Nhân $z$ với $\cos \theta - i \sin \theta$ để được \_\_.
**17** Vẽ tất cả tám nghiệm của $z^8 = 1$ trong mặt phẳng phức. Dạng chữ nhật $a + ib$ của nghiệm $z = w = \exp(-2\pi i/8)$ là gì?
**18** Xác định vị trí các căn bậc ba của $1$ trong mặt phẳng phức. Xác định vị trí các căn bậc ba của $-1$. Cùng với nhau chúng là các căn bậc sáu của \_\_.
**19** Bằng cách so sánh $e^{3i\theta} = \cos 3\theta + i \sin 3\theta$ với $(e^{i\theta})^3 = (\cos \theta + i \sin \theta)^3$, hãy tìm các công thức "góc nhân ba" cho $\cos 3\theta$ và $\sin 3\theta$ theo $\cos \theta$ và $\sin \theta$.
**20** Giả sử số liên hợp $\bar{z}$ bằng với nghịch đảo $1/z$. Tất cả các $z$ có thể có là gì?
**21** (a) Tại sao cả $e^{i\pi}$ và $i^e$ đều có giá trị tuyệt đối 1?
(b) Trong mặt phẳng phức hãy đặt các ngôi sao gần các điểm $e^{i\pi}$ và $i^e$.
(c) Số $i^e$ có thể là $(e^{i\pi/2})^e$ hoặc $(e^{5i\pi/2})^e$. Chúng có bằng nhau không?
**22** Vẽ các đường đi của các số này từ $t = 0$ đến $t = 2\pi$ trong mặt phẳng phức:
(a) $e^{it}$

# **9.2 Ma trận Hermitian và Ma trận Unita (Hermitian and Unitary Matrices)**

Thông điệp chính của mục này có thể được trình bày trong một câu: *Khi bạn chuyển vị một vectơ phức $z$ hoặc ma trận $A$, hãy lấy luôn cả liên hợp phức.* Đừng dừng lại ở $z^T$ hoặc $A^T$. Đảo ngược dấu của tất cả các phần ảo. Từ một vectơ cột với $z_j = a_j + ib_j$, vectơ hàng tốt lành $z^T$ là *chuyển vị liên hợp (conjugate transpose)* với các thành phần $a_j - ib_j$:

| Chuyển vị liên hợp | $\bar{z}^T = [\bar{z}_1 \ \cdots \ \bar{z}_n] = [a_1 - ib_1 \ \cdots \ a_n - ib_n]$ | (1) |
|---------------------|-------------------------------------------------------------------------------------|-----|

Đây là một lý do để chuyển sang $\bar{z}$. Bình phương độ dài của một vectơ thực là $x_1^2 + \dots + x_n^2$. Bình phương độ dài của một vectơ phức *không phải là* $z_1^2 + \dots + z_n^2$. Với định nghĩa sai đó, độ dài của $(1, i)$ sẽ là $1^2 + i^2 = 0$. Một vectơ khác không sẽ có độ dài bằng 0 - không ổn. Các vectơ khác sẽ có độ dài là số phức. Thay vì $(a + bi)^2$ chúng ta muốn $a^2 + b^2$, là *bình phương giá trị tuyệt đối*. Đây là $(a + bi)$ nhân với $(a - bi)$.

Đối với mỗi thành phần chúng ta muốn $z_j$ nhân $\bar{z}_j$, chính là $|z_j|^2 = a_j^2 + b_j^2$. Điều đó xuất hiện khi các thành phần của $\bar{z}$ nhân với các thành phần của $z$:

Bình phương độ dài
$$[\bar{z}_1 \ \cdots \ \bar{z}_n] \begin{bmatrix} z_1 \\ \vdots \\ z_n \end{bmatrix} = |z_1|^2 + \dots + |z_n|^2. \text{ Đây là } \bar{z}^T z = \|z\|^2. \quad (2)$$

Bây giờ bình phương độ dài của $(1, i)$ là $1^2 + |i|^2 = 2$. Độ dài là $\sqrt{2}$. Bình phương độ dài của $(1 + i, 1 - i)$ là 4. Các vectơ duy nhất có độ dài bằng không là các vectơ không.

Độ dài $\|z\|$ là căn bậc hai của $\bar{z}^T z = z^H z = |z_1|^2 + \dots + |z_n|^2$.

Trước khi đi xa hơn chúng ta thay thế hai ký hiệu bằng một ký hiệu. Thay vì dấu gạch ngang cho liên hợp và $T$ cho chuyển vị, chúng ta chỉ sử dụng chỉ số trên $H$. Do đó $\bar{z}^T = z^H$. Đây là "$z$ Hermitian", *chuyển vị liên hợp* của $z$. Từ mới được phát âm là "Her-mee-shan". Ký hiệu mới cũng áp dụng cho các ma trận: Chuyển vị liên hợp của một ma trận $A$ là $A^H$.

Một ký hiệu phổ biến khác là $A^*$. Lệnh chuyển vị `'` trong MATLAB tự động lấy các liên hợp phức (`z'` là $z^H = \bar{z}^T$ và `A'` là $A^H = \bar{A}^T$).

$$A^H \text{ là "A Hermitian"} \quad \text{Nếu } A = \begin{bmatrix} 1 & i \\ 0 & 1+i \end{bmatrix} \quad \text{thì } A^H = \begin{bmatrix} 1 & 0 \\ -i & 1-i \end{bmatrix}.$$

## **Tích vô hướng phức (Complex Inner Products)**

Đối với các vectơ thực, bình phương độ dài là $x^T x$ - *tích vô hướng của $x$ với chính nó*. Đối với các vectơ phức, bình phương độ dài là $z^H z$. Sẽ rất đáng mong đợi nếu $z^H z$ là tích vô hướng của $z$ với chính nó. Để làm cho điều đó xảy ra, tích vô hướng phức nên sử dụng chuyển vị liên hợp (không chỉ là chuyển vị). Điều này không có ảnh hưởng gì tới các vectơ thực.

**ĐỊNH NGHĨA** Tích vô hướng của các vectơ thực hoặc phức $u$ và $v$ là $u^H v$:
$$u^H v = \begin{bmatrix} \bar{u}_1 & \cdots & \bar{u}_n \end{bmatrix} \begin{bmatrix} v_1 \\ \vdots \\ v_n \end{bmatrix} = \bar{u}_1 v_1 + \dots + \bar{u}_n v_n. \quad (3)$$

Với các vectơ phức, $u^H v$ khác với $v^H u$. *Thứ tự của các vectơ bây giờ rất quan trọng.* Thực tế $v^H u = \bar{v}_1 u_1 + \dots + \bar{v}_n u_n$ là liên hợp phức của $u^H v$. Chúng ta phải chấp nhận một vài sự bất tiện vì mục đích lớn hơn.

**Ví dụ 1** Tích vô hướng của $u = \begin{bmatrix} 1 \\ i \end{bmatrix}$ với $v = \begin{bmatrix} i \\ 1 \end{bmatrix}$ là $\begin{bmatrix} 1 & -i \end{bmatrix} \begin{bmatrix} i \\ 1 \end{bmatrix} = i - i = 0$.

Ví dụ 1 thật đáng ngạc nhiên. Những vectơ $(1, i)$ và $(i, 1)$ đó trông không có vẻ vuông góc. Nhưng chúng thực sự như vậy. *Tích vô hướng bằng không vẫn có nghĩa là các vectơ (phức) trực giao với nhau.* Tương tự, vectơ $(1, i)$ trực giao với vectơ $(1, -i)$. Tích vô hướng của chúng là $1 - 1$. Chúng ta đang nhận được chính xác giá trị không cho tích vô hướng - nơi mà chúng ta sẽ sai lầm nhận được không cho độ dài của $(1, i)$ nếu chúng ta quên lấy liên hợp.

**Lưu ý** Chúng ta đã chọn lấy liên hợp của vectơ đầu tiên $u$. Một số tác giả chọn vectơ thứ hai $v$. Tích vô hướng phức của họ sẽ là $u^T \bar{v}$. Tôi nghĩ đó là một sự lựa chọn tự do.

*Tích vô hướng của $Au$ với $v$ bằng với tích vô hướng của $u$ với $A^H v$:*
| **$A^H$ cũng được gọi là ma trận "liên hợp (adjoint)" của $A$** | $(Au)^H v = u^H (A^H v).$ | (4) |
|----------------------------------------------------------------------------------------|---------------------------|-----|

Liên hợp của $Au$ là $\bar{A}\bar{u}$. Chuyển vị $\bar{A}\bar{u}$ cho ra $\bar{u}^T \bar{A}^T$ như bình thường. Đây là $u^H A^H$. Mọi thứ đáng lẽ phải hoạt động, đều hoạt động. Quy tắc cho $H$ đến từ quy tắc cho $T$. Chúng ta liên tục sử dụng sự thật rằng $(a - ib)(c - id)$ là liên hợp của $(a + ib)(c + id)$.

*Chuyển vị liên hợp của $AB$ là*
$$(AB)^H = B^H A^H$$

#### **Ma trận Hermitian (Hermitian Matrices)** $S = S^H$

Trong số các ma trận thực, *ma trận đối xứng* tạo thành lớp đặc biệt quan trọng nhất: $S = S^T$. Chúng có các giá trị riêng thực và các vectơ riêng trực giao nằm trong một ma trận trực giao $Q$. Mọi ma trận đối xứng thực đều có thể được viết dưới dạng $S = Q\Lambda Q^{-1}$ và cũng như $S = Q\Lambda Q^T$ (bởi vì $Q^{-1} = Q^T$). Tất cả những điều này suy ra từ $S^T = S$, khi $S$ là thực.

Trong số các ma trận phức, lớp đặc biệt chứa các **ma trận Hermitian**: $S = S^H$. Điều kiện đối với các phần tử là $s_{ij} = \overline{s_{ji}}$. Trong trường hợp này chúng ta nói rằng "$S$ là Hermitian". *Mọi ma trận đối xứng thực đều là Hermitian*, bởi vì việc lấy liên hợp của nó không có ảnh hưởng gì. Ma trận tiếp theo cũng là Hermitian, $S = S^H$:

**Ví dụ 2** $S = \begin{bmatrix} 2 & 3 - 3i \\ 3 + 3i & 5 \end{bmatrix}$ Đường chéo chính phải là số thực vì $s_{ii} = \overline{s_{ii}}$. Nằm đối xứng qua nó là các số liên hợp $3 + 3i$ và $3 - 3i$.

Ví dụ này sẽ minh họa ba tính chất thiết yếu của tất cả các ma trận Hermitian.

**1. Nếu $S = S^H$ và $z$ là bất kỳ vectơ cột thực hoặc phức nào, số $z^H S z$ là số thực.**

Chứng minh nhanh: $z^H S z$ chắc chắn là $1 \times 1$. Lấy chuyển vị liên hợp của nó:
$$(z^H S z)^H = z^H S^H (z^H)^H \quad \text{chính là } z^H S z \text{ một lần nữa.}$$

Vì vậy số $z^H S z$ bằng với liên hợp của nó và phải là số thực. Dưới đây là "năng lượng" $z^H S z$ đó:
$$\begin{bmatrix} \bar{z}_1 & \bar{z}_2 \end{bmatrix} \begin{bmatrix} 2 & 3 - 3i \\ 3 + 3i & 5 \end{bmatrix} \begin{bmatrix} z_1 \\ z_2 \end{bmatrix} = 2\bar{z}_1 z_1 + 5\bar{z}_2 z_2 + (3 - 3i)\bar{z}_1 z_2 + (3 + 3i)z_1 \bar{z}_2.$$
(đường chéo) (đường chéo) (ngoài đường chéo)

Các số hạng $2|z_1|^2$ và $5|z_2|^2$ từ đường chéo đều là số thực. Các số hạng ngoài đường chéo là liên hợp của nhau - vì vậy tổng của chúng là số thực. (Các phần ảo triệt tiêu nhau khi chúng ta cộng lại.) Toàn bộ biểu thức $z^H S z$ là số thực, và điều này sẽ làm cho $\lambda$ là số thực.

**2. Mọi giá trị riêng của một ma trận Hermitian đều là số thực.**

**Chứng minh** Giả sử $Sz = \lambda z$. Nhân cả hai vế với $z^H$ để được $z^H S z = \lambda z^H z$. Ở vế trái, $z^H S z$ là số thực. Ở vế phải, $z^H z$ là bình phương độ dài, là số thực và dương. Vì vậy tỷ số $\lambda = z^H S z / z^H z$ là một số thực. (Điều phải chứng minh)

Ví dụ trên có các giá trị riêng $\lambda = 8$ và $\lambda = -1$, là số thực vì $S = S^H$:
$$\begin{vmatrix} 2 - \lambda & 3 - 3i \\ 3 + 3i & 5 - \lambda \end{vmatrix} = \lambda^2 - 7\lambda + 10 - |3 + 3i|^2 \\ = \lambda^2 - 7\lambda + 10 - 18 = (\lambda - 8)(\lambda + 1).$$

**3. Các vectơ riêng của một ma trận Hermitian trực giao với nhau** (khi chúng tương ứng với các giá trị riêng khác nhau). Nếu $Sz = \lambda z$ và $Sy = \beta y$ thì $y^H z = 0$.

**Chứng minh** Nhân $Sz = \lambda z$ ở bên trái với $y^H$. Nhân $y^H S^H = \beta y^H$ ở bên phải với $z$:
$$y^H S z = \lambda y^H z \quad \text{và} \quad y^H S^H z = \beta y^H z. \quad (5)$$

Các vế trái bằng nhau nên $\lambda y^H z = \beta y^H z$. Khi đó $y^H z$ phải bằng 0.

Các vectơ riêng trực giao với nhau trong ví dụ của chúng ta với $\lambda = 8$ và $\beta = -1$:
$$(S - 8I)z = \begin{bmatrix} -6 & 3 - 3i \\ 3 + 3i & -3 \end{bmatrix} \begin{bmatrix} z_1 \\ z_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \quad \text{và} \quad z = \begin{bmatrix} 1 \\ 1 + i \end{bmatrix}$$
$$(S + I)y = \begin{bmatrix} 3 & 3 - 3i \\ 3 + 3i & 6 \end{bmatrix} \begin{bmatrix} y_1 \\ y_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \quad \text{và} \quad y = \begin{bmatrix} 1 - i \\ -1 \end{bmatrix}.$$

| Các vectơ riêng trực giao | $y^H z = \begin{bmatrix} 1 + i & -1 \end{bmatrix} \begin{bmatrix} 1 \\ 1 + i \end{bmatrix} = 0.$ |
|-------------------------|---------------------------------------------------------------------|

Những vectơ riêng này có bình phương độ dài $1^2 + 1^2 + 1^2 = 3$. Sau khi chia cho $\sqrt{3}$ chúng là các vectơ đơn vị. Chúng đã trực giao, bây giờ chúng *trực chuẩn*. Chúng đi vào các cột của *ma trận vectơ riêng $X$*, làm chéo hóa $S$.

Khi $S$ là thực và đối xứng, $X$ là $Q$ - một ma trận trực giao. Bây giờ $S$ là phức và Hermitian. Các vectơ riêng của nó là phức và trực chuẩn. *Ma trận vectơ riêng $X$ giống như $Q$, nhưng là phức:* $Q^H Q = I$. Chúng ta gán cho $Q$ một cái tên mới "unita (unitary)" nhưng vẫn gọi nó là $Q$.

# **Ma trận Unita (Unitary Matrices)**

*Ma trận unita $Q$* là một ma trận vuông (phức) có *các cột trực chuẩn*.

| Ma trận unita làm chéo hóa $S$: | $Q = \frac{1}{\sqrt{3}} \begin{bmatrix} 1 & 1 - i \\ 1 + i & -1 \end{bmatrix}$ |
|----------------------------------------|--------------------------------------------------------------------------------|

$Q$ này cũng là một ma trận Hermitian. Tôi đã không kỳ vọng điều đó! Ví dụ này gần như quá hoàn hảo. Chúng ta sẽ thấy rằng các giá trị riêng của $Q$ này phải là 1 và -1.

Kiểm tra ma trận cho các cột trực chuẩn thực là $Q^T Q = I$. Các tích vô hướng bằng 0 xuất hiện ngoài đường chéo. Trong trường hợp phức, $Q^T$ trở thành $Q^H$. Các cột thể hiện chúng là trực chuẩn khi $Q^H$ nhân với $Q$. Các tích vô hướng lấp đầy $Q^H Q = I$:

*Mọi ma trận $Q$ có các cột trực chuẩn đều có* $Q^H Q = I$.
*Nếu $Q$ là ma trận vuông, nó là một ma trận unita. Khi đó* $Q^H = Q^{-1}$.

Giả sử $Q$ (với các cột trực chuẩn) nhân với bất kỳ $z$ nào. Độ dài vectơ giữ nguyên, bởi vì $z^H Q^H Q z = z^H z$. Nếu $z$ là một vectơ riêng của $Q$ chúng ta biết thêm điều gì đó: *Các giá trị riêng của các ma trận unita (và trực giao) $Q$ đều có giá trị tuyệt đối* $|\lambda| = 1$.

Nếu $Q$ là ma trận unita thì $\|Qz\| = \|z\|$. Do đó $Qz = \lambda z$ dẫn đến $|\lambda| = 1$.

Ví dụ $2 \times 2$ của chúng ta vừa là Hermitian ($Q = Q^H$) vừa là unita ($Q^{-1} = Q^H$). Điều đó có nghĩa là các giá trị riêng là số thực và nó có nghĩa là $|\lambda| = 1$. Một số thực với $|\lambda| = 1$ chỉ có hai khả năng: *Các giá trị riêng là 1 hoặc -1*. Vết của $Q$ bằng 0 nên $\lambda = 1$ và $\lambda = -1$.

**Ví dụ 3** *Ma trận Fourier* $3 \times 3$ nằm trong Hình 9.3. Nó có phải là Hermitian không? Nó có phải là unita không? $F_3$ chắc chắn là đối xứng. Nó bằng với chuyển vị của nó. Nhưng nó không bằng với chuyển vị liên hợp của nó - nó *không phải là Hermitian*. Nếu bạn đổi $i$ thành $-i$, bạn nhận được một ma trận khác.

$$\text{Ma trận Fourier} \quad F = \frac{1}{\sqrt{3}} \begin{bmatrix} 1 & 1 & 1 \\ 1 & e^{2\pi i/3} & e^{4\pi i/3} \\ 1 & e^{4\pi i/3} & e^{2\pi i/3} \end{bmatrix}.$$

Hình 9.3: Các căn bậc ba của 1 đi vào ma trận Fourier $F = F_3$.

$F$ có phải là ma trận unita không? *Có*. Bình phương độ dài của mỗi cột là $\frac{1}{3}(1 + 1 + 1)$ (vectơ đơn vị). Cột đầu tiên trực giao với cột thứ hai bởi vì $1 + e^{2\pi i/3} + e^{4\pi i/3} = 0$. Đây là tổng của ba con số được đánh dấu trong Hình 9.3.

Hãy chú ý đến tính đối xứng của hình vẽ. Nếu bạn quay nó $120^\circ$, ba điểm nằm ở cùng vị trí. Do đó tổng $S$ của chúng cũng ở cùng vị trí! Tổng duy nhất có thể ở cùng vị trí sau phép quay $120^\circ$ là $S = 0$.

Cột 2 của $F$ có trực giao với cột 3 không? Tích vô hướng của chúng trông giống như
$$\frac{1}{3}(1 + e^{6\pi i/3} + e^{6\pi i/3}) = \frac{1}{3}(1 + 1 + 1).$$
Điều này không bằng không. Kết quả này là sai vì chúng ta đã quên lấy liên hợp phức. Tích vô hướng phức sử dụng $H$ chứ không phải $T$:
$$(\text{cột } 2)^H(\text{cột } 3) = \frac{1}{3}(1 \cdot 1 + e^{-2\pi i/3}e^{4\pi i/3} + e^{-4\pi i/3}e^{2\pi i/3}) \\ = \frac{1}{3}(1 + e^{2\pi i/3} + e^{-2\pi i/3}) = 0.$$
Vì vậy chúng ta thực sự có tính trực giao. *Kết luận: $F$ là một ma trận unita.*

Mục tiếp theo sẽ nghiên cứu các ma trận Fourier $n \times n$. Trong số tất cả các ma trận unita phức, đây là những ma trận quan trọng nhất. Khi chúng ta nhân một vectơ với $F$, chúng ta đang tính toán *Biến đổi Fourier Rời rạc (Discrete Fourier Transform)* của nó. Khi chúng ta nhân với $F^{-1}$, chúng ta đang tính toán *biến đổi ngược*. Tính chất đặc biệt của các ma trận unita là $F^{-1} = F^H$. Biến đổi ngược chỉ khác biệt bằng cách đổi $i$ thành $-i$:

| Đổi $i$ thành $-i$ | $F^{-1} = F^H = \frac{1}{\sqrt{3}} \begin{bmatrix} 1 & 1 & 1 \\ 1 & e^{-2\pi i/3} & e^{-4\pi i/3} \\ 1 & e^{-4\pi i/3} & e^{-2\pi i/3} \end{bmatrix}$ |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|

Mọi người làm việc với $F$ đều nhận ra giá trị của nó. Mục cuối cùng của chương này sẽ tập hợp lại giải tích Fourier và số phức và đại số tuyến tính.

### **Tập bài tập 9.2 (Problem Set 9.2)**

**1** Tìm độ dài của $u = (1 + i, 1 - i, 1 + 2i)$ và $v = (i, i, i)$. Tìm $u^H v$ và $v^H u$.
**2** Tính $A^H A$ và $A A^H$. Cả hai đều là ma trận \_\_:
$$A = \begin{bmatrix} i & 1 & i \\ 1 & i & i \end{bmatrix}.$$
**3** Giải $Az = 0$ để tìm một vectơ $z$ trong không gian không của $A$ ở Bài 2. Chứng minh rằng $z$ trực giao với các cột của $A^H$. Chứng minh rằng $z$ *không* trực giao với các cột của $A^T$. *Không gian hàng tốt không còn là* $C(A^T)$. **Bây giờ nó là $C(A^H)$.**
**4** Bài 3 chỉ ra rằng bốn không gian con cơ bản là $C(A)$ và $N(A)$ và \_\_ và \_\_. Số chiều của chúng vẫn là $r$ và $n - r$ và $r$ và $m - r$. Chúng vẫn là các không gian con trực giao. *Ký hiệu $H$ thay thế cho $T$.*
**5** (a) Chứng minh rằng $A^H A$ luôn là một ma trận Hermitian.
(b) Nếu $Az = 0$ thì $A^H Az = 0$. Nếu $A^H Az = 0$, nhân với $z^H$ để chứng minh rằng $Az = 0$. Không gian không của $A$ và $A^H A$ là \_\_. Do đó $A^H A$ là một ma trận Hermitian khả nghịch khi không gian không của $A$ chỉ chứa $z = 0$.
**6** Đúng hay sai (đưa ra lý do nếu đúng hoặc một ví dụ phản chứng nếu sai):
(a) Nếu $A$ là một ma trận thực thì $A + iI$ có thể nghịch đảo.
(b) Nếu $S$ là một ma trận Hermitian thì $S + iI$ có thể nghịch đảo.
(c) Nếu $Q$ là một ma trận unita thì $Q + iI$ có thể nghịch đảo.
**7** Khi bạn nhân một ma trận Hermitian với một số thực $c$, thì $cS$ có còn là Hermitian không? Chứng minh rằng $iS$ là phản Hermitian (skew-Hermitian) khi $S$ là Hermitian. Các ma trận Hermitian $3 \times 3$ là một không gian con miễn là "các vô hướng" là số thực.
**8** $P$ thuộc những lớp ma trận nào: khả nghịch, Hermitian, unita?
$$P = \begin{bmatrix} 0 & i & 0 \\ 0 & 0 & i \\ i & 0 & 0 \end{bmatrix}.$$
Tính $P^2, P^3$, và $P^{100}$. Các giá trị riêng của $P$ là gì?
**9** Tìm các vectơ riêng đơn vị của $P$ trong Bài 8, và đặt chúng vào các cột của một ma trận unita $Q$. Tính chất nào của $P$ làm cho các vectơ riêng này trực giao?
**10** Viết ma trận luân hoàn $3 \times 3$ $C = 2I + 5P$. Nó có cùng các vectơ riêng với $P$ trong Bài 8. Tìm các giá trị riêng của nó.
**11** Nếu $Q$ và $U$ là các ma trận unita, hãy chứng minh rằng $Q^{-1}$ là unita và $QU$ cũng là unita. Bắt đầu từ $Q^H Q = I$ và $U^H U = I$.
**12** Làm sao bạn biết rằng định thức của mọi ma trận Hermitian là số thực?
**13** Ma trận $A^H A$ không chỉ là Hermitian mà còn là xác định dương, khi các cột của $A$ độc lập. Chứng minh: $z^H A^H Az$ là số dương nếu $z$ khác không bởi vì \_\_.
**14** Chéo hóa các ma trận Hermitian này để đạt đến $S = Q \Lambda Q^H$:
| $S = \begin{bmatrix} 0 & 1-i \\ i+1 & 1 \end{bmatrix}$ | $\text{và}$ | $S = \begin{bmatrix} 2 & 1+i \\ i-1 & 3 \end{bmatrix}$ |
|--------------------------------------------------------|-----|--------------------------------------------------------|
**15** Chéo hóa ma trận phản Hermitian này để đạt đến $K = Q \Lambda Q^H$. Tất cả các $\lambda$ là \_\_:
$$K = \begin{bmatrix} 0 & -1+i \\ 1+i & i \end{bmatrix}.$$
**16** Chéo hóa ma trận trực giao này để đạt đến $U = Q \Lambda Q^H$. Bây giờ tất cả các $\lambda$ là \_\_:
$$U = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}.$$
**17** Chéo hóa ma trận unita này để đạt đến $U = Q \Lambda Q^H$. Một lần nữa tất cả các $\lambda$ là \_\_:
$$U = \frac{1}{\sqrt{3}} \begin{bmatrix} 1 & 1-i \\ 1+i & -1 \end{bmatrix}.$$
**18** Nếu $v_1, \dots, v_n$ là một cơ sở trực chuẩn cho $\mathbb{C}^n$, ma trận với những cột đó là ma trận \_\_. Chứng minh rằng bất kỳ vectơ $z$ nào cũng bằng $(v_1^H z)v_1 + \dots + (v_n^H z)v_n$.
**19** $v = (1, i, 1), w = (i, 1, 0)$ và $z = \_\_$ là một cơ sở trực giao cho \_\_.
**20** Nếu $S = A + iB$ là một ma trận Hermitian, các phần thực và phần ảo của nó có đối xứng không?
**21** Số chiều (phức) của $\mathbb{C}^n$ là \_\_. Tìm một cơ sở không thực cho $\mathbb{C}^n$.
**22** Mô tả tất cả các ma trận Hermitian và ma trận unita kích thước $1 \times 1$ và $2 \times 2$.
**23** Các giá trị riêng của $A^H$ liên quan như thế nào với các giá trị riêng của ma trận vuông $A$?
**24** Nếu $u^H u = 1$ hãy chứng minh rằng $I - 2uu^H$ là Hermitian và cũng là unita. Ma trận hạng một $uu^H$ là hình chiếu lên đường thẳng nào trong $\mathbb{C}^n$?
**25** Nếu $A + iB$ là một ma trận unita ($A$ và $B$ là thực) hãy chứng minh rằng $Q = \begin{bmatrix} A & -B \\ B & A \end{bmatrix}$ là một ma trận trực giao.
**26** Nếu $A + iB$ là Hermitian ($A$ và $B$ là thực) hãy chứng minh rằng $\begin{bmatrix} A & -B \\ B & A \end{bmatrix}$ là đối xứng.
**27** Chứng minh rằng nghịch đảo của một ma trận Hermitian cũng là Hermitian (chuyển vị liên hợp $S^{-1} S = I$).
**28** Một ma trận với các vectơ riêng trực chuẩn có dạng $N = Q \Lambda Q^{-1} = Q \Lambda Q^H$. *Chứng minh rằng $N N^H = N^H N$.* Những $N$ này chính là các ma trận chuẩn tắc (normal matrices). Các ví dụ là ma trận Hermitian, phản Hermitian, và ma trận unita. Xây dựng một ma trận chuẩn tắc $2 \times 2$ từ $Q \Lambda Q^H$ bằng cách chọn các giá trị riêng phức trong $\Lambda$.

# **9.3 Biến đổi Fourier Nhanh (The Fast Fourier Transform)**

Nhiều ứng dụng của đại số tuyến tính cần thời gian để phát triển. Không dễ để giải thích chúng trong một giờ. Giáo viên và tác giả phải lựa chọn giữa việc hoàn thiện lý thuyết và thêm các ứng dụng mới. Thường thì lý thuyết giành chiến thắng, nhưng mục này là một ngoại lệ. Nó giải thích thuật toán số trị có giá trị nhất trong thế kỷ qua.

*Chúng ta muốn nhân nhanh với $F$ và $F^{-1}$, ma trận Fourier và nghịch đảo của nó.* Điều này đạt được nhờ Biến đổi Fourier Nhanh. Một tích thông thường $Fc$ sử dụng $n^2$ phép nhân ( $F$ có $n^2$ phần tử). FFT chỉ cần $n \times \frac{1}{2} \log_2 n$. Chúng ta sẽ thấy như thế nào.

FFT đã cách mạng hóa quá trình xử lý tín hiệu. Toàn bộ các ngành công nghiệp được tăng tốc nhờ một ý tưởng này. Các kỹ sư điện là những người đầu tiên biết được sự khác biệt - họ thực hiện biến đổi Fourier của bạn ngay khi họ gặp bạn (nếu bạn là một hàm số). Ý tưởng của Fourier là biểu diễn $f$ như một tổng của các sóng hài $c_k e^{ikx}$. Hàm số được nhìn thấy trong *không gian tần số (frequency space)* thông qua các hệ số $c_k$, thay vì *không gian vật lý (physical space)* thông qua các giá trị của nó $f(x)$. Quá trình chuyển đổi qua lại giữa các $c$ và $f$ là nhờ biến đổi Fourier. Chuyển đổi nhanh là nhờ FFT.

### **Căn của đơn vị và Ma trận Fourier (Roots of Unity and the Fourier Matrix)**

Các phương trình bậc hai có hai nghiệm (hoặc một nghiệm kép). Phương trình bậc $n$ có $n$ nghiệm (tính cả các nghiệm lặp). Đây là Định lý Cơ bản của Đại số, và để làm cho nó đúng chúng ta phải cho phép các nghiệm phức. Mục này nói về phương trình rất đặc biệt $z^n = 1$. Các nghiệm $z$ là các "căn bậc $n$ của 1". Chúng là $n$ điểm cách đều nhau quanh vòng tròn đơn vị trong mặt phẳng phức.

Hình 9.4 hiển thị tám nghiệm của $z^8 = 1$. Khoảng cách giữa chúng là $\frac{1}{8} (360^\circ) = 45^\circ$. Căn đầu tiên nằm ở $45^\circ$ hoặc $\theta = 2\pi/8$ radian. *Nó là số phức* $w = e^{i\theta} = e^{i2\pi/8}$. Chúng ta gọi con số này là $w_8$ để nhấn mạnh rằng nó là một căn bậc 8. Bạn có thể viết nó dưới dạng $\cos \frac{2\pi}{8}$ và $\sin \frac{2\pi}{8}$, nhưng đừng làm vậy. Bảy căn bậc 8 còn lại là $w^2, w^3, \dots, w^7$, đi vòng quanh vòng tròn. Các lũy thừa của $w$ ở dạng cực là tốt nhất, vì chúng ta chỉ làm việc với các góc $\frac{2\pi}{8}, \frac{4\pi}{8}, \dots, \frac{16\pi}{8} = 2\pi$. 8 góc đó tính bằng độ là $45^\circ, 90^\circ, 135^\circ, \dots, 360^\circ$.

Hình 9.4: Tám nghiệm của $z^8 = 1$ là $1, w, w^2, \dots, w^7$ với $w = (1 + i)/\sqrt{2}$.

Các căn bậc bốn của 1 cũng có trong hình vẽ. Chúng là $i, -1, -i, 1$. Góc bây giờ là $2\pi/4$ hay $90^\circ$. Căn đầu tiên $w_4 = e^{2\pi i/4}$ không là gì khác ngoài $i$. Ngay cả các căn bậc hai của 1 cũng được nhìn thấy, với $w_2 = e^{i2\pi/2} = -1$. Đừng coi thường những căn bậc hai $1$ và $-1$ đó. Ý tưởng đằng sau FFT là đi từ một ma trận Fourier **$8 \times 8$** (chứa các lũy thừa của $w_8$) đến ma trận **$4 \times 4$** dưới đây (với các lũy thừa của $w_4 = i$). Cùng một ý tưởng đi từ 4 xuống 2. Bằng cách khai thác các kết nối từ $F_8$ xuống $F_4$ và lên đến $F_{16}$ (và xa hơn nữa), FFT làm cho phép nhân với $F_{1024}$ trở nên rất nhanh.

Chúng ta mô tả *ma trận Fourier*, đầu tiên cho $n = 4$. Các hàng của nó chứa các lũy thừa của $1$ và $w$ và $w^2$ và $w^3$. Đây là các căn bậc bốn của 1, và các lũy thừa của chúng đi theo một trật tự đặc biệt.

| **Ma trận Fourier** | $F = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & w & w^2 & w^3 \\ 1 & w^2 & w^4 & w^6 \\ 1 & w^3 & w^6 & w^9 \end{bmatrix} = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & i & -1 & -i \\ 1 & -1 & 1 & -1 \\ 1 & -i & -1 & i \end{bmatrix}$ |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Ma trận này đối xứng ($F = F^T$). Nó *không* Hermitian. Đường chéo chính của nó không phải là số thực. Nhưng $\frac{1}{2}F$ là một *ma trận unita*, nghĩa là $(\frac{1}{2}F^H)(\frac{1}{2}F) = I$:

| Các cột của $F$ cho | $F^H F = 4I$. | Nghịch đảo của nó là $\frac{1}{4} F^H$ chính là | $F^{-1} = \frac{1}{4} \bar{F}$. |
|-------------------------|----------------|-------------------------------------------|---------------------------------------|

Nghịch đảo thay đổi từ $w = i$ thành $\bar{w} = -i$. Điều đó đưa chúng ta từ $F$ đến $\bar{F}$. Khi Biến đổi Fourier Nhanh mang lại một cách tính nhanh để nhân với $F$, nó cũng làm điều tương tự cho $\bar{F}$ và $F^{-1}$.

Mỗi cột có độ dài $\sqrt{n}$. Vì vậy các ma trận unita là $Q = F/\sqrt{n}$ và $Q^{-1} = \bar{F}/\sqrt{n}$. Chúng ta tránh $\sqrt{n}$ và chỉ sử dụng $F$ và $F^{-1} = \bar{F}/n$. Điểm chính yếu là nhân $F$ với $c_0, c_1, c_2, c_3$:

| Điểm số 4 | $\begin{bmatrix} y_0 \\ y_1 \\ y_2 \\ y_3 \end{bmatrix} = Fc = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & w & w^2 & w^3 \\ 1 & w^2 & w^4 & w^6 \\ 1 & w^3 & w^6 & w^9 \end{bmatrix} \begin{bmatrix} c_0 \\ c_1 \\ c_2 \\ c_3 \end{bmatrix}$ | (1) |
|---------|------------------------------------------------------------------------------------------------------------|-----|

Đầu vào là bốn hệ số phức $c_0, c_1, c_2, c_3$. Đầu ra là bốn giá trị hàm $y_0, y_1, y_2, y_3$. Đầu ra thứ nhất $y_0 = c_0 + c_1 + c_2 + c_3$ là giá trị của chuỗi Fourier $\sum c_k e^{ikx}$ tại $x = 0$. *Đầu ra thứ hai là giá trị của chuỗi $\sum c_k e^{ikx}$ tại $x = 2\pi/4$:*
$$y_1 = c_0 + c_1 e^{i2\pi/4} + c_2 e^{i4\pi/4} + c_3 e^{i6\pi/4} = c_0 + c_1 w + c_2 w^2 + c_3 w^3.$$

Đầu ra thứ ba và thứ tư $y_2$ và $y_3$ là các giá trị của $\sum c_k e^{ikx}$ tại $x = 4\pi/4$ và $x = 6\pi/4$. Đây là các chuỗi Fourier *hữu hạn*! *Chúng chứa $n = 4$ số hạng và chúng được đánh giá tại $n = 4$ điểm.* Những điểm đó $x = 0, 2\pi/4, 4\pi/4, 6\pi/4$ cách đều nhau.

Điểm tiếp theo sẽ là $x = 8\pi/4$ chính là $2\pi$. Khi đó chuỗi quay trở lại $y_0$, bởi vì $e^{2\pi i}$ giống như $e^0 = 1$. Mọi thứ quay vòng với chu kỳ 4. Trong thế giới này $2 + 2$ là $0$ bởi vì $(w^2)(w^2) = w^0 = 1$. Chúng ta tuân theo quy ước rằng *$j$ và $k$ đi từ $0$ đến $n-1$* (thay vì $1$ đến $n$). "Hàng thứ không" và "cột thứ không" của $F$ chứa toàn các số 1.

Ma trận Fourier $n \times n$ chứa các lũy thừa của $w = e^{2\pi i/n}$:
$$F_n c = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & w & w^2 & w^{n-1} \\ 1 & w^2 & w^4 & w^{2(n-1)} \\ \vdots & \vdots & \vdots & \vdots \\ 1 & w^{n-1} & w^{2(n-1)} & w^{(n-1)^2} \end{bmatrix} \begin{bmatrix} c_0 \\ c_1 \\ c_2 \\ \vdots \end{bmatrix} = \begin{bmatrix} y_0 \\ y_1 \\ y_2 \\ \vdots \end{bmatrix} = y. \quad (2)$$

$F_n$ là đối xứng nhưng không Hermitian. *Các cột của nó trực giao*, và $F_n \bar{F}_n = nI$. *Khi đó $F_n^{-1}$ là $\bar{F}_n / n$.* Nghịch đảo chứa các lũy thừa của $\bar{w}_n = e^{-2\pi i/n}$. Nhìn vào quy luật trong $F$:

#### *Phần tử ở hàng $j$, cột $k$ là $w^{jk}$. Hàng không và cột không chứa $w^0 = 1$.*

Khi chúng ta nhân $c$ với $F_n$, chúng ta lấy tổng của chuỗi tại $n$ điểm. *Khi chúng ta nhân $y$ với $F_n^{-1}$, chúng ta tìm thấy các hệ số $c$ từ các giá trị hàm $y$.* Trong MATLAB lệnh đó là `c = fft(y)`. Ma trận $F$ đi từ "không gian tần số" sang "không gian vật lý".

*Lưu ý quan trọng.* Nhiều tác giả thích làm việc với $w = e^{-2\pi i/N}$, đây là *liên hợp phức* của $w$ của chúng ta. (Họ thường sử dụng chữ omega trong tiếng Hy Lạp, và tôi sẽ làm điều đó để giữ hai lựa chọn riêng biệt.) Với lựa chọn này, ma trận DFT của họ chứa các lũy thừa của $\omega$ chứ không phải $w$. Nó là $\bar{F}$, liên hợp của $F$ của chúng ta. $\bar{F}$ đi từ không gian vật lý sang không gian tần số.

$\bar{F}$ là một sự lựa chọn hoàn toàn hợp lý! MATLAB sử dụng $\omega = e^{-2\pi i/N}$. Ma trận DFT `fft(eye(N))` chứa các lũy thừa của con số này $\omega = \bar{w}$. **Ma trận Fourier $F$ với các $w$ sẽ tái tạo $y$ từ $c$. Ma trận $\bar{F}$ với các $\omega$ tính toán các hệ số Fourier bằng `fft(y)`.** *Cũng quan trọng không kém.* Khi một hàm $f(x)$ có chu kỳ $2\pi$, và chúng ta đổi $x$ thành $e^{i\theta}$, hàm được xác định xung quanh vòng tròn đơn vị (nơi $z = e^{i\theta}$). Biến đổi Fourier Rời rạc giống hệt như phép nội suy. Tìm đa thức $p(z) = c_0 + c_1 z + \dots + c_{n-1} z^{n-1}$ khớp với $n$ giá trị $f_0, \dots, f_{n-1}$:

| Nội suy | Tìm $c_0, \dots, c_{n-1}$ sao cho $p(z) = f$ tại $n$ điểm $z = 1, \dots, w^{n-1}$ |
|---------------|-------------------------------------------------------------------------------------|

Ma trận Fourier chính là ma trận Vandermonde để nội suy tại những $n$ điểm đặc biệt đó.

# **Một bước của Biến đổi Fourier Nhanh (One Step of the Fast Fourier Transform)**

Chúng ta muốn nhân $F$ với $c$ càng nhanh càng tốt. Thông thường một ma trận nhân một vectơ mất $n^2$ phép nhân riêng biệt - ma trận có $n^2$ phần tử. Bạn có thể nghĩ rằng không thể làm tốt hơn được. (Nếu ma trận có các phần tử bằng không thì các phép nhân có thể được bỏ qua. Nhưng ma trận Fourier không có số không nào!) Bằng cách sử dụng quy luật đặc biệt $w^{jk}$ cho các phần tử của nó, $F$ có thể được phân tích thành nhân tử theo một cách tạo ra nhiều số không. Đây là **FFT**.

*Ý tưởng then chốt là kết nối $F_n$ với ma trận Fourier kích thước một nửa $F_{n/2}$.* Giả sử $n$ là một lũy thừa của 2 (ví dụ $n = 2^{10} = 1024$). Chúng ta sẽ kết nối $F_{1024}$ với *hai bản sao của* $F_{512}$.

Khi $n = 4$, chìa khóa nằm ở mối quan hệ giữa $F_4$ và hai bản sao của $F_2$:
$$F_4 = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & i & -1 & -i \\ 1 & -1 & 1 & -1 \\ 1 & -i & -1 & i \end{bmatrix} \quad \text{và} \quad \begin{bmatrix} F_2 & \\ & F_2 \end{bmatrix} = \begin{bmatrix} 1 & 1 & & \\ 1 & -1 & & \\ & & 1 & 1 \\ & & 1 & -1 \end{bmatrix}.$$

Ở bên trái là $F_4$, không có số không nào. Ở bên phải là một ma trận có một nửa là số không. Công việc bị cắt giảm một nửa. Nhưng khoan đã, những ma trận đó không giống nhau. Chúng ta cần hai ma trận thưa và đơn giản để hoàn thành việc phân tích nhân tử của FFT:
$$\text{Các nhân tử cho FFT} \quad F_4 = \begin{bmatrix} 1 & & 1 & \\ & 1 & & i \\ 1 & & -1 & \\ & & 1 & -i \end{bmatrix} \begin{bmatrix} 1 & 1 & & \\ 1 & -1 & & \\ & & 1 & 1 \\ & & 1 & -1 \end{bmatrix} \begin{bmatrix} 1 & & & \\ & & 1 & \\ & 1 & & \\ & & & 1 \end{bmatrix}. \quad (3)$$

Ma trận cuối cùng là một phép hoán vị. Nó đặt các $c$ chẵn ($c_0$ và $c_2$) lên trước các $c$ lẻ ($c_1$ và $c_3$). Ma trận ở giữa thực hiện các biến đổi kích thước một nửa $F_2$ và $F_2$ trên các $c$ chẵn và các $c$ lẻ. Ma trận ở bên trái kết hợp hai đầu ra kích thước một nửa - theo cách tạo ra đầu ra kích thước đầy đủ chính xác $y = F_4 c$.

Cùng một ý tưởng áp dụng khi $n = 1024$ và $m = \frac{1}{2}n = 512$. Con số $w$ là $e^{2\pi i/1024}$. Nó nằm ở góc $\theta = 2\pi/1024$ trên vòng tròn đơn vị. Ma trận Fourier $F_{1024}$ chứa đầy các lũy thừa của $w$. Bước đầu tiên của FFT là sự phân tích nhân tử vĩ đại được phát hiện bởi Cooley và Tukey (và được tiên đoán trước vào năm 1805 bởi Gauss):
$$F_{1024} = \begin{bmatrix} I_{512} & D_{512} \\ I_{512} & -D_{512} \end{bmatrix} \begin{bmatrix} F_{512} & \\ & F_{512} \end{bmatrix} \begin{bmatrix} \text{hoán vị} \\ \text{chẵn-lẻ} \end{bmatrix}. \quad (4)$$

$I_{512}$ là ma trận đơn vị. $D_{512}$ là ma trận đường chéo với các phần tử $(1, w, \dots, w^{511})$. Hai bản sao của $F_{512}$ là những gì chúng ta mong đợi. Đừng quên rằng chúng sử dụng căn bậc 512 của đơn vị (không là gì khác ngoài $w^2!!$). Ma trận hoán vị tách vectơ đầu vào $c$ thành các phần chẵn và lẻ $c' = (c_0, c_2, \dots, c_{1022})$ và $c'' = (c_1, c_3, \dots, c_{1023})$.

Dưới đây là các công thức đại số nói lên điều tương tự như việc phân tích nhân tử của $F_{1024}$:

**(Một bước của FFT)** Đặt $m = \frac{1}{2}n$. $m$ thành phần đầu tiên và $m$ thành phần cuối cùng của $y = F_n c$ kết hợp các biến đổi kích thước một nửa $y' = F_m c'$ và $y'' = F_m c''$. Phương trình (4) cho thấy bước này đi từ $n$ xuống $m = n/2$ dưới dạng $Iy' + Dy''$ và $Iy' - Dy''$:
$$\begin{aligned} y_j &= y'_j + (w_n)^j y''_j, \quad j = 0, \dots, m-1 \\ y_{j+m} &= y'_j - (w_n)^j y''_j, \quad j = 0, \dots, m-1. \end{aligned} \quad (5)$$

Tách $c$ thành $c'$ và $c''$, biến đổi chúng bằng $F_m$ thành $y'$ và $y''$, sau đó (5) tái tạo $y$.

Các công thức đó đến từ việc tách $c_0 \dots, c_{n-1}$ thành $c_{2k}$ chẵn và $c_{2k+1}$ lẻ: $w$ là $w_n$.
$$y = F_n c \quad y_j = \sum_{k=0}^{n-1} w^{jk} c_k = \sum_{k=0}^{m-1} w^{2jk} c_{2k} + \sum_{k=0}^{m-1} w^{j(2k+1)} c_{2k+1} \text{ với } m = \frac{1}{2}n. \quad (6)$$

Các $c$ chẵn đi vào $c' = (c_0, c_2, \dots)$ và các $c$ lẻ đi vào $c'' = (c_1, c_3, \dots)$. Sau đó đến các biến đổi $F_m c'$ và $F_m c''$. **Chìa khóa là $w_n^2 = w_m$.** Điều này cho ra $w_n^{2jk} = w_m^{jk}$.

**Viết lại (6)** $y_j = \sum (w_m)^{jk} c'_k + (w_n)^j \sum (w_m)^{jk} c''_k = y'_j + (w_n)^j y''_j$. (7)

Đối với $j \geq m$, dấu trừ trong (5) đến từ việc đặt nhân tử chung $(w_n)^m = -1$ ra khỏi $(w_n)^j$.

MATLAB dễ dàng tách các $c$ chẵn khỏi các $c$ lẻ và nhân với $w_n^j$. Chúng ta sử dụng `conj(F)` hoặc tương đương là biến đổi ngược của MATLAB `ifft`, bởi vì `ifft` dựa trên $\omega = \bar{w} = e^{-2\pi i/n}$. Bài 16 chỉ ra rằng $F$ và `conj(F)` được liên kết bằng cách hoán vị các hàng.

| **Bước FFT**                                | $y' = \text{ifft}(c(0 : 2 : n - 2)) * n/2;$                                         |
|------------------------------------------------|-------------------------------------------------------------------------------------|
| **từ $n$ xuống $n/2$** | $y'' = \text{ifft}(c(1 : 2 : n - 1)) * n/2;$                                        |
| **trong MATLAB**                               | $d = w.^{\wedge}(0 : n/2 - 1)';$<br>$y = [y' + d .* y''; y' - d .* y''];$ |

Sơ đồ luồng (flow graph) cho thấy $c'$ và $c''$ đi qua $F_2$ kích thước một nửa. Những bước đó được gọi là "bướm (butterflies)", từ hình dạng của chúng. Sau đó các đầu ra $y'$ và $y''$ được kết hợp (nhân $y''$ với $1, i$ từ $D$ và cũng với $-1, -i$ từ $-D$) để tạo ra $y = F_4 c$.

Việc rút gọn từ $F_n$ xuống hai $F_m$ gần như cắt giảm một nửa công việc - bạn nhìn thấy các số không trong phân tích nhân tử của ma trận. Việc rút gọn đó tốt nhưng chưa phải là tuyệt vời. Ý tưởng đầy đủ của **FFT** mạnh mẽ hơn nhiều. Nó tiết kiệm nhiều hơn một nửa thời gian.

**FFT Toàn phần bằng Đệ quy (The Full FFT by Recursion)**

Nếu bạn đã đọc đến đây, có lẽ bạn đã đoán được điều gì sẽ đến tiếp theo. Chúng ta đã rút gọn $F_n$ xuống $F_{n/2}$. **Tiếp tục xuống $F_{n/4}$.** Mỗi $F_{512}$ dẫn đến $F_{256}$. Sau đó 256 dẫn đến 128. **Đó là đệ quy.**

Đệ quy là một nguyên lý cơ bản của nhiều thuật toán nhanh. Dưới đây là bước 2 với bốn bản sao của $F_{256}$ và $D$ (256 lũy thừa của $\omega_{512}$). Các phần tử chẵn của các phần tử chẵn $c_0, c_4, c_8, \dots$ đi trước:
$$\begin{bmatrix} F_{512} \\ & F_{512} \end{bmatrix} = \begin{bmatrix} I & D & & \\ I & -D & & \\ & & I & D \\ & & I & -D \end{bmatrix} \begin{bmatrix} F & & & \\ & F & & \\ & & F & \\ & & & F \end{bmatrix} \begin{bmatrix} \text{chọn} & 0, 4, 8, \dots \\ \text{chọn} & 2, 6, 10, \dots \\ \text{chọn} & 1, 5, 9, \dots \\ \text{chọn} & 3, 7, 11, \dots \end{bmatrix}.$$

Chúng ta sẽ đếm các phép nhân riêng biệt, để xem chúng ta tiết kiệm được bao nhiêu. Trước khi FFT được phát minh, số đếm thông thường là $n^2 = (1024)^2$. Đây là khoảng một triệu phép nhân. Tôi không nói rằng chúng mất nhiều thời gian. Chi phí trở nên lớn khi chúng ta có rất, rất nhiều biến đổi phải làm - điều thường thấy. Khi đó sự tiết kiệm nhờ FFT cũng rất lớn:

*Số đếm cuối cùng cho kích thước $n = 2^\ell$ được giảm từ $n^2$ xuống $\frac{1}{2}n\ell$.*

Con số 1024 là $2^{10}$, nên $\ell = 10$. Số đếm ban đầu là $(1024)^2$ giảm xuống còn $5 \times 1024$. Mức độ tiết kiệm là một hệ số bằng 200. Một triệu được giảm xuống còn năm nghìn. Đó là lý do tại sao FFT đã cách mạng hóa xử lý tín hiệu.

Dưới đây là lý luận đằng sau $\frac{1}{2}n\ell$. Có $\ell$ cấp độ, đi từ $n = 2^\ell$ xuống $n = 1$. Mỗi cấp độ có $n/2$ phép nhân từ đường chéo của $D$, để ráp lại các đầu ra kích thước một nửa từ cấp độ thấp hơn. Điều này mang lại số đếm cuối cùng là $\frac{1}{2}n\ell$, tức là $\frac{1}{2} n \log_2 n$.

Một lưu ý cuối cùng về thuật toán đáng chú ý này. Có một quy luật tuyệt vời cho thứ tự các $c$ đi vào FFT, sau tất cả các hoán vị chẵn-lẻ. Viết các số từ $0$ đến $n - 1$ ở dạng nhị phân (như 00, 01, 10, 11 đối với $n = 4$). Đảo ngược thứ tự của các chữ số đó: 00, 10, 01, 11. Điều đó cho **thứ tự bit đảo ngược (bit-reversed order) 0, 2, 1, 3** với chẵn trước lẻ (Xem Bài 17). Hình ảnh hoàn chỉnh cho thấy các $c$ theo thứ tự đảo ngược bit, $\ell = \log_2 n$ bước của đệ quy, và đầu ra cuối cùng $y_0, \dots, y_{n-1}$ chính là $F_n$ nhân $c$.

Chương này kết thúc bằng ý tưởng rất nền tảng đó, một ma trận nhân một vectơ.

### **Tập bài tập 9.3 (Problem Set 9.3)**

**1** Nhân ba ma trận trong phương trình (3) và so sánh với $F$. Ở 6 phần tử nào bạn cần biết rằng $i^2 = -1$?
**2** Nghịch đảo ba nhân tử trong phương trình (3) để tìm ra cách phân tích nhân tử nhanh của $F^{-1}$.
**3** $F$ là đối xứng. Vậy hãy chuyển vị phương trình (3) để tìm một Biến đổi Fourier Nhanh mới!
**4** Tất cả các phần tử trong phân tích nhân tử của $F_6$ liên quan đến các lũy thừa của $w_6 =$ căn bậc sáu của 1:
$$F_6 = \begin{bmatrix} I & D \\ I & -D \end{bmatrix} \begin{bmatrix} F_3 & \\ & F_3 \end{bmatrix} \begin{bmatrix} P \end{bmatrix}.$$
Viết các ma trận này với $1, w_6, w_6^2$ trong $D$ và $w_3 = w_6^2$ trong $F_3$. Hãy nhân chúng!
**5** Nếu $v = (1, 0, 0, 0)$ và $w = (1, 1, 1, 1)$, hãy chứng minh rằng $Fv = w$ và $Fw = 4v$. Do đó $F^{-1}w = v$ và $F^{-1}v = \_\_$.
**6** $F_2$ là gì và $F_4$ là gì đối với ma trận Fourier $4 \times 4$?
**7** Đưa vectơ $c = (1, 0, 1, 0)$ qua ba bước của FFT để tìm $y = Fc$. Làm tương tự cho $c = (0, 1, 0, 1)$.
**8** Tính $y = F_8 c$ bằng ba bước FFT cho $c = (1, 0, 1, 0, 1, 0, 1, 0)$. Lặp lại phép tính cho $c = (0, 1, 0, 1, 0, 1, 0, 1)$.
**9** Nếu $w = e^{2\pi i/64}$ thì $w^2$ và $\sqrt{w}$ nằm trong số các căn bậc \_\_\_\_\_ và \_\_\_\_\_ của 1.
**10** (a) Vẽ tất cả các căn bậc sáu của 1 trên vòng tròn đơn vị. Chứng minh chúng cộng lại bằng không.
(b) Ba căn bậc ba của 1 là gì? Chúng có cộng lại bằng không không?
**11** Các cột của ma trận Fourier $F$ là các *vectơ riêng* của hoán vị vòng quanh (cyclic permutation) $P$ (xem Mục 8.3). Nhân $PF$ để tìm các giá trị riêng $\lambda_1, \lambda_2, \lambda_3, \lambda_4$:
$$\begin{bmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & i & -1 & -i \\ 1 & -1 & 1 & -1 \\ 1 & -i & -1 & i \end{bmatrix} = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & i & -1 & -i \\ 1 & -1 & 1 & -1 \\ 1 & -i & -1 & i \end{bmatrix} \begin{bmatrix} \lambda_1 & & & \\ & \lambda_2 & & \\ & & \lambda_3 & \\ & & & \lambda_4 \end{bmatrix}.$$
Đây là $PF = F\Lambda$ hay $P = F\Lambda F^{-1}$. Ma trận vectơ riêng (thường là $X$) chính là $F$.
**12** Phương trình $\det(P - \lambda I) = 0$ là $\lambda^4 = 1$. Điều này chứng tỏ lại rằng các giá trị riêng là $\lambda = \_\_\_\_\_$. Hoán vị $P$ nào có các giá trị riêng = căn bậc ba của 1?
**13** (a) Hai vectơ riêng của $C$ là $(1, 1, 1, 1)$ và $(1, i, i^2, i^3)$. Tìm các giá trị riêng $e$.
$$\begin{bmatrix} c_0 & c_1 & c_2 & c_3 \\ c_3 & c_0 & c_1 & c_2 \\ c_2 & c_3 & c_0 & c_1 \\ c_1 & c_2 & c_3 & c_0 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \end{bmatrix} = e_1 \begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \end{bmatrix} \quad \text{và} \quad C \begin{bmatrix} 1 \\ i \\ i^2 \\ i^3 \end{bmatrix} = e_2 \begin{bmatrix} 1 \\ i \\ i^2 \\ i^3 \end{bmatrix}.$$
(b) $P = F\Lambda F^{-1}$ ngay lập tức cho ra $P^2 = F\Lambda^2 F^{-1}$ và $P^3 = F\Lambda^3 F^{-1}$. Khi đó $C = c_0 I + c_1 P + c_2 P^2 + c_3 P^3 = F(c_0 I + c_1 \Lambda + c_2 \Lambda^2 + c_3 \Lambda^3) F^{-1} = F E F^{-1}$. Ma trận $E$ trong ngoặc đó là ma trận đường chéo. Nó chứa các \_\_\_\_\_ của $C$.
**14** Tìm các giá trị riêng của ma trận "chu kỳ (periodic)" $-1, 2, -1$ từ $E = 2I - \Lambda - \Lambda^3$, với các giá trị riêng của $P$ trong $\Lambda$. Các số $-1$ ở các góc làm cho ma trận này trở thành chu kỳ:
$$C = \begin{bmatrix} 2 & -1 & 0 & -1 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ -1 & 0 & -1 & 2 \end{bmatrix} \quad \text{có } c_0 = 2, c_1 = -1, c_2 = 0, c_3 = -1.$$
**15** **Tích chập nhanh (Fast convolution) = Phép nhân nhanh với $C$:** Để nhân $C$ với một vectơ $x$, chúng ta thay vào đó có thể nhân $F(E(F^{-1}x))$. Cách trực tiếp sử dụng $n^2$ phép nhân riêng biệt. Biết $E$ và $F$, cách thứ hai chỉ sử dụng $n \log_2 n + n$ phép nhân. Có bao nhiêu phép nhân đến từ $E$, bao nhiêu từ $F$, và bao nhiêu từ $F^{-1}$?
**16** **Chú ý.** Tại sao hàng $i$ của $\bar{F}$ lại giống hàng $N - i$ của $F$ (được đánh số từ $0$ đến $N - 1$)?
**17** *Thứ tự đảo ngược bit* của các số $0, 1, \dots, 7$ là gì? Viết tất cả chúng ở dạng nhị phân (cơ số 2) như $000, 001, \dots, 111$ và đảo ngược thứ tự từng cái. 8 con số bây giờ là \_\_\_\_\_.
