# **Chương 7**

# **Phân tích Giá trị Suy biến (The Singular Value Decomposition - SVD)**

# **7.1 Xử lý Hình ảnh bằng Đại số Tuyến tính**

**1** Một hình ảnh là một ma trận lớn chứa các giá trị thang độ xám (grayscale), một giá trị cho mỗi điểm ảnh (pixel) và màu sắc. **2** Khi các pixel lân cận có tương quan với nhau (không ngẫu nhiên), hình ảnh có thể được nén. **3** SVD phân tách bất kỳ ma trận $A$ nào thành các phần có hạng (rank) bằng 1: $uv^T = (\text{cột})(\text{hàng})$. **4** Các cột và hàng là các vectơ riêng của các ma trận đối xứng $AA^T$ và $A^T A$.

**Định lý giá trị suy biến đối với $A$ chính là định lý trị riêng đối với $A^T A$ và $AA^T$.**

Đó là một bản xem trước nhanh chóng về những gì bạn sẽ thấy trong chương này. $A$ có *hai* tập hợp các vectơ suy biến (các vectơ riêng của $A^T A$ và $AA^T$). Có *một* tập hợp các giá trị suy biến dương (bởi vì $A^T A$ có cùng các trị riêng dương như $AA^T$). $A$ thường là ma trận chữ nhật, nhưng $A^T A$ và $AA^T$ là các ma trận vuông, đối xứng và nửa xác định dương (positive semidefinite).

**Phân tích Giá trị Suy biến (SVD) phân tách bất kỳ ma trận nào thành các thành phần đơn giản.**

Mỗi phần là một vectơ cột nhân với một vectơ hàng. Một ma trận $m \times n$ có $m$ nhân $n$ phần tử (một con số lớn khi ma trận đại diện cho một hình ảnh). Nhưng một cột và một hàng chỉ có $m + n$ **thành phần, ít hơn nhiều so với** $m$ **nhân** $n$. Những phần (cột)(hàng) đó là các ma trận có kích thước đầy đủ có thể được xử lý với tốc độ cực nhanh - chúng chỉ cần $m$ cộng $n$ số.

Thật không bình thường, ứng dụng xử lý hình ảnh này của SVD lại xuất hiện trước khi phần đại số ma trận mà nó phụ thuộc vào được trình bày. Tôi sẽ bắt đầu với các hình ảnh đơn giản chỉ bao gồm một hoặc hai phần. Ngay bây giờ tôi đang coi một hình ảnh như một ma trận hình chữ nhật lớn. Các phần tử $a_{ij}$ cho biết thang độ xám của tất cả các pixel trong hình ảnh. Hãy nghĩ về một pixel như một hình vuông nhỏ, cách góc dưới bên trái $i$ bước sang ngang và $j$ bước lên trên. Thang độ xám của nó là một con số (thường là một số nguyên trong khoảng $0 \leq a_{ij} < 256 = 2^8$). Một pixel trắng hoàn toàn có $a_{ij} = 255 = 11111111$. Con số đó có tám số 1 khi máy tính viết số 255 dưới dạng ký hiệu nhị phân.

Bạn có thể thấy một hình ảnh có $m$ nhân $n$ pixel, với mỗi pixel sử dụng 8 bit (0 hoặc 1) cho thang độ xám của nó, trở thành một ma trận $m \times n$ với 256 giá trị khả dĩ cho mỗi phần tử $a_{ij}$ như thế nào.

Tóm lại, một hình ảnh là một ma trận lớn. Để sao chép nó một cách hoàn hảo, chúng ta cần $8(m)(n)$ bit thông tin. Truyền hình độ nét cao (HDTV) thường có $m = 1080$ và $n = 1920$. Thông thường có 24 khung hình mỗi giây và bạn có thể muốn xem có màu sắc (3 thang màu). Điều này đòi hỏi truyền đi $(3)(8)(49,766,400)$ bit mỗi giây. Điều đó là quá đắt đỏ và người ta không làm như vậy. Máy phát không thể theo kịp chương trình.

Khi quá trình nén được thực hiện tốt, bạn không thể nhận ra sự khác biệt so với bản gốc. *Các biên (Edges) trong hình ảnh* (sự thay đổi đột ngột về thang độ xám) là những phần khó nén nhất.

Thành công lớn trong việc nén sẽ là điều không thể nếu mỗi $a_{ij}$ là một số ngẫu nhiên độc lập. Chúng ta hoàn toàn phụ thuộc vào thực tế là *các pixel lân cận nói chung có thang độ xám tương tự nhau.* Một đường biên tạo ra một sự thay đổi đột ngột khi bạn vượt qua nó. Phim hoạt hình dễ nén hơn hình ảnh thế giới thực, với các đường biên ở khắp mọi nơi.

Đối với một video, các số $a_{ij}$ không thay đổi nhiều giữa các khung hình. **Chúng ta chỉ truyền đi những thay đổi nhỏ.** Đây là *mã hóa vi sai (difference coding)* trong chuẩn nén video H.264 (có trên trang web của cuốn sách này). Chúng ta nén từng ma trận thay đổi bằng đại số tuyến tính (và bằng "lượng tử hóa (quantization)" phi tuyến tính cho một bước chuyển đổi hiệu quả sang số nguyên trong máy tính).

Những hình ảnh tự nhiên mà chúng ta thấy hàng ngày hoàn toàn sẵn sàng và cởi mở cho việc nén - nhưng điều đó không có nghĩa là nó dễ thực hiện.

# **Các Hình ảnh có Hạng Thấp (Các Ví dụ)**

Những hình ảnh dễ nén nhất là đen toàn bộ hoặc trắng toàn bộ hoặc có một thang độ xám không đổi $g$ toàn bộ. Ma trận $A$ có cùng một số $g$ trong mọi phần tử: $a_{ij} = g$. Khi $g = 1$ và $m = n = 6$, đây là một ví dụ cực đoan về giáo điều SVD trung tâm của xử lý hình ảnh:

**Ví dụ 1** Đừng truyền
$$A = \begin{bmatrix} 1 & 1 & 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 & 1 & 1 \end{bmatrix}$$
Hãy truyền cái này $A = \begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \\ 1 \\ 1 \end{bmatrix} \begin{bmatrix} 1 & 1 & 1 & 1 & 1 & 1 \end{bmatrix}$

36 con số trở thành 12 con số. Với $300 \times 300$ pixel, 90.000 con số trở thành 600. Và nếu chúng ta định nghĩa vectơ gồm toàn số 1 (vectơ **ones**) từ trước, chúng ta chỉ cần truyền đi **một con số**. Con số đó sẽ là thang độ xám không đổi $g$ nhân với $xx^T$ để tạo ra ma trận.

Tất nhiên ví dụ đầu tiên này là cực đoan. Nhưng nó đưa ra một điểm quan trọng. Nếu có những vectơ đặc biệt như $x = \text{ones}$ có thể được định nghĩa hữu ích từ trước, thì quá trình xử lý hình ảnh có thể cực kỳ nhanh. Cuộc chiến diễn ra giữa **các cơ sở được chọn trước (preselected bases)** (cơ sở Fourier cho phép tăng tốc từ FFT) và **các cơ sở thích ứng (adaptive bases)** được xác định bởi hình ảnh. SVD tạo ra các cơ sở từ chính hình ảnh - điều này có tính thích ứng và nó có thể tốn kém.

Tôi không nói rằng SVD luôn luôn hay thường xuyên mang lại thuật toán hiệu quả nhất trong thực tế. Mục đích của những ví dụ tiếp theo này là để giảng dạy chứ không phải để sản xuất.

| **Ví dụ 2** | | $a \ a \ c \ c \ e \ e$ | | $\begin{bmatrix} 1 \\ 1 \\ 1 \\ \dots \\ 1 \end{bmatrix}$ |
|-------------|---|-------------------------|---|-----------------------------------------------------------|
| "cờ ace" | | $a \ a \ c \ c \ e \ e$ | | |
| Cờ Pháp $A$ | Đừng truyền $A =$ | $a \ a \ c \ c \ e \ e$ | Truyền $A =$ | $\begin{bmatrix} 1 \\ 1 \\ 1 \\ \dots \\ 1 \end{bmatrix} \begin{bmatrix} a & a & c & c & e & e \end{bmatrix}$ |
| Cờ Ý $A$ | | $a \ a \ c \ c \ e \ e$ | | |
| Cờ Đức $A^T$ | | $a \ a \ c \ c \ e \ e$ | | |

Lá cờ này có 3 màu nhưng nó vẫn có hạng bằng 1. Chúng ta vẫn có một cột nhân với một hàng. 36 phần tử thậm chí có thể khác nhau hoàn toàn, miễn là chúng giữ được mẫu hạng 1 đó là $A = u_1 v_1^T$. Nhưng khi hạng tăng lên $r = 2$, chúng ta cần $u_1 v_1^T + u_2 v_2^T$. Đây là một lựa chọn:

| **Ví dụ 3** | $A = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}$ | bằng $A = \begin{bmatrix} 1 \\ 1 \end{bmatrix} \begin{bmatrix} 1 & 1 \end{bmatrix} - \begin{bmatrix} 1 \\ 0 \end{bmatrix} \begin{bmatrix} 0 & 1 \end{bmatrix}$ |
|------------------------|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Hình vuông nhúng** | | |

Các số 1 và số 0 trong $A$ có thể là các khối chứa các số 1 và một khối chứa các số 0. *Chúng ta vẫn sẽ có hạng bằng 2.* Chúng ta vẫn sẽ chỉ cần hai số hạng $u_1 v_1^T$ và $u_2 v_2^T$. Một hình ảnh $6 \times 6$ sẽ được nén thành 24 con số. Một hình ảnh $N \times N$ (với $N^2$ con số) sẽ được nén thành $4N$ con số từ bốn vectơ $u_1, v_1, u_2, v_2$.

Liệu tôi đã đưa ra sự lựa chọn tốt nhất cho các chữ $u$ và chữ $v$ chưa? Đây *không phải* là lựa chọn từ SVD! Tôi nhận thấy rằng $u_1 = (1, 1)$ không trực giao với $u_2 = (1, 0)$. Và $v_1 = (1, 1)$ không trực giao với $v_2 = (0, 1)$. Lý thuyết nói rằng tính trực giao sẽ tạo ra một phần nhỏ hơn $c_2 u_2 v_2^T$. **(SVD chọn các phần có hạng 1 theo thứ tự tầm quan trọng.)**

Nếu hạng của $A$ cao hơn 2 rất nhiều, như chúng ta thường mong đợi đối với các hình ảnh thực, thì $A$ sẽ cộng lại từ nhiều phần có hạng 1. Chúng ta muốn những phần nhỏ phải thực sự nhỏ - chúng có thể bị loại bỏ mà không làm mất đi chất lượng hiển thị. Nén hình ảnh trở thành quá trình có tổn hao (lossy), nhưng nén hình ảnh tốt hầu như không thể bị phát hiện bởi hệ thống thị giác của con người.

Câu hỏi trở thành: **Các lựa chọn trực giao từ SVD là gì?**

# **Các Vectơ Riêng cho SVD**

Tôi muốn giới thiệu việc sử dụng các vectơ riêng. Nhưng các vectơ riêng của phần lớn các hình ảnh không trực giao với nhau. Hơn nữa, các vectơ riêng $x_1, x_2$ chỉ cung cấp một tập hợp các vectơ, trong khi chúng ta lại cần hai tập hợp (những chữ $u$ và những chữ $v$). Câu trả lời cho cả hai khó khăn đó chính là ý tưởng SVD:

**Sử dụng các vectơ riêng $u$ của $AA^T$ và các vectơ riêng $v$ của $A^T A$.**

Vì $AA^T$ và $A^T A$ tự động đối xứng (nhưng thường không bằng nhau!) nên những chữ $u$ sẽ là một tập trực giao và các vectơ riêng $v$ sẽ là một tập trực giao khác. Chúng ta có thể và sẽ biến tất cả chúng thành các vectơ đơn vị: $\|u_i\| = 1$ và $\|v_i\| = 1$. Khi đó ma trận hạng 2 của chúng ta sẽ là $A = \sigma_1 u_1 v_1^T + \sigma_2 u_2 v_2^T$. Độ lớn của những con số $\sigma_1$ và $\sigma_2$ sẽ quyết định liệu chúng có thể bị bỏ qua trong quá trình nén hay không. *Chúng ta giữ lại các $\sigma$ lớn, loại bỏ các $\sigma$ nhỏ.*

Các chữ $u$ từ SVD được gọi là **các vectơ suy biến trái (left singular vectors)** (các vectơ riêng đơn vị của $AA^T$). Các chữ $v$ là **các vectơ suy biến phải (right singular vectors)** (các vectơ riêng đơn vị của $A^T A$). Các chữ $\sigma$ là **các giá trị suy biến (singular values)**, là căn bậc hai của các trị riêng bằng nhau của $AA^T$ và $A^T A$:

**Các lựa chọn từ SVD** &nbsp;&nbsp;&nbsp; $AA^T u_i = \sigma_i^2 u_i$ &nbsp;&nbsp;&nbsp; $A^T A v_i = \sigma_i^2 v_i$ &nbsp;&nbsp;&nbsp; $A v_i = \sigma_i u_i$ &nbsp;&nbsp;&nbsp; (1)

Trong Ví dụ 3 (hình vuông nhúng), đây là các ma trận đối xứng $AA^T$ và $A^T A$:

$$AA^T = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix} \quad A^T A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}.$$

Định thức của chúng bằng 1, nên $\lambda_1 \lambda_2 = 1$. Các vết của chúng (tổng trên đường chéo) bằng 3:

$$\det \begin{bmatrix} 1-\lambda & 1 \\ 1 & 2-\lambda \end{bmatrix} = \lambda^2 - 3\lambda + 1 = 0 \text{ cho ta } \lambda_1 = \frac{3+\sqrt{5}}{2} \text{ và } \lambda_2 = \frac{3-\sqrt{5}}{2}.$$

$$\text{Căn bậc hai của } \lambda_1 \text{ và } \lambda_2 \text{ là } \sigma_1 = \frac{\sqrt{5}+1}{2} \text{ và } \sigma_2 = \frac{\sqrt{5}-1}{2} \text{ với } \sigma_1 \sigma_2 = 1.$$

Ma trận hạng 1 gần nhất với $A$ sẽ là $\sigma_1 u_1 v_1^T$. Sai số chỉ là $\sigma_2 \approx 0.6 = \text{tốt nhất có thể}$.

Các vectơ riêng trực chuẩn của $AA^T$ và $A^T A$ là
$$u_1 = \begin{bmatrix} 1 \\ \sigma_1 \end{bmatrix} \quad u_2 = \begin{bmatrix} \sigma_1 \\ -1 \end{bmatrix} \quad v_1 = \begin{bmatrix} \sigma_1 \\ 1 \end{bmatrix} \quad v_2 = \begin{bmatrix} 1 \\ -\sigma_1 \end{bmatrix} \text{ tất cả chia cho } \sqrt{1+\sigma_1^2}. \quad (2)$$

Mọi độc giả đều hiểu rằng trong đời thực những tính toán đó được thực hiện bởi máy tính! (Chắc chắn không phải bởi những vị giáo sư không đáng tin cậy. Tôi đã tự sửa lỗi của mình bằng cách sử dụng lệnh `svd(A)` trong MATLAB.) Và chúng ta có thể kiểm chứng rằng ma trận $A$ được khôi phục chính xác từ $\sigma_1 u_1 v_1^T + \sigma_2 u_2 v_2^T$:

$$A = \begin{bmatrix} u_1 & u_2 \end{bmatrix} \begin{bmatrix} \sigma_1 & \\ & \sigma_2 \end{bmatrix} \begin{bmatrix} v_1^T \\ v_2^T \end{bmatrix} \text{ hay đơn giản hơn là } A \begin{bmatrix} v_1 & v_2 \end{bmatrix} = \begin{bmatrix} \sigma_1 u_1 & \sigma_2 u_2 \end{bmatrix} \quad (3)$$

**Quan trọng** Điểm then chốt không phải là các hình ảnh có xu hướng có hạng thấp. **Không phải vậy**: Các hình ảnh hầu hết đều có hạng đầy đủ (full rank). Nhưng chúng có **hạng hiệu dụng thấp (low effective rank)**. Điều này có nghĩa là: Nhiều giá trị suy biến có kích thước nhỏ và có thể được đặt bằng không. *Chúng ta truyền đi một sự xấp xỉ có hạng thấp.*

**Ví dụ 4** Giả sử lá cờ có hai hình tam giác khác màu. Hình tam giác phía dưới bên trái có các số 1 và hình tam giác phía trên bên phải có các số 0. Đường chéo chính được bao gồm với các số 1. Dưới đây là ma trận hình ảnh khi $n = 4$. Nó có hạng đầy đủ $r = 4$ nên nó khả nghịch:

$$\text{Ma trận cờ hình tam giác} \quad A = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 1 & 1 & 0 \\ 1 & 1 & 1 & 1 \end{bmatrix} \quad \text{và} \quad A^{-1} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ -1 & 1 & 0 & 0 \\ 0 & -1 & 1 & 0 \\ 0 & 0 & -1 & 1 \end{bmatrix}$$

Với hạng đầy đủ, $A$ có một tập hợp đầy đủ gồm $n$ giá trị suy biến $\sigma$ (tất cả đều dương). SVD sẽ tạo ra $n$ phần $\sigma_i u_i v_i^T$ có hạng 1. Để tái tạo hoàn hảo thì cần có tất cả $n$ phần.

Trong quá trình nén, các $\sigma$ *nhỏ* có thể bị loại bỏ mà không làm suy giảm nghiêm trọng chất lượng hình ảnh. Chúng ta muốn hiểu và vẽ đồ thị các $\sigma$ đối với $n = 4$ và cũng đối với $n$ lớn. Chú ý rằng Ví dụ 3 chính là trường hợp đặc biệt $n = 2$ của Ví dụ 4 hình tam giác này.

Làm bằng tay, chúng ta bắt đầu với $AA^T$ (máy tính sẽ tiến hành theo cách khác):

$$AA^T = \begin{bmatrix} 1 & 1 & 2 & 1 \\ 1 & 2 & 2 & 3 \\ 2 & 3 & 3 & 4 \\ 1 & 2 & 2 & 4 \end{bmatrix} \text{ và } (AA^T)^{-1} = (A^{-1})^T A^{-1} = \begin{bmatrix} 2 & -1 & 0 & 0 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ 0 & 0 & -1 & 1 \end{bmatrix}. \quad (4)$$

Ma trận nghịch đảo $-1, 2, -1$ đó được bao gồm ở đây bởi vì các trị riêng của nó đều có dạng $2 - 2 \cos \theta$. Vì vậy, chúng ta biết các $\lambda$ của $AA^T$ và các $\sigma$ của $A$:

$$\lambda = \frac{1}{2 - 2 \cos \theta} = \frac{1}{4 \sin^2(\theta/2)} \quad \text{cho ta} \quad \sigma = \sqrt{\lambda} = \frac{1}{2 \sin(\theta/2)}. \quad (5)$$

$n$ góc $\theta$ khác nhau cách đều nhau, điều này khiến cho ví dụ này trở nên quá đặc biệt:
$$\theta = \frac{\pi}{2n+1}, \frac{3\pi}{2n+1}, \dots, \frac{(2n-1)\pi}{2n+1} \quad \left( n = 4 \text{ bao gồm } \theta = \frac{3\pi}{9} \text{ với } 2 \sin \frac{\theta}{2} = 1 \right).$$

Trường hợp đặc biệt đó cho ta $\lambda = 1$ là một trị riêng của $AA^T$ khi $n = 4$. Vậy $\sigma = \sqrt{\lambda} = 1$ là một giá trị suy biến của $A$. Bạn có thể kiểm tra xem vectơ $u = (1, 1, 0, -1)$ có $AA^T u = u$ hay không (thực sự là một trường hợp đặc biệt).

Điểm quan trọng là vẽ đồ thị $n$ giá trị suy biến của $A$. Những con số đó giảm dần (không giống như các trị riêng của $A$, tất cả đều bằng 1). Nhưng sự sụt giảm là không quá dốc. Vì vậy, SVD chỉ cung cấp mức độ nén vừa phải cho lá cờ hình tam giác này. *Nén rất tốt đối với ma trận Hilbert.*

![](images/_page_377_Figure_12.jpeg)

Hình 7.1: Các giá trị suy biến của tam giác gồm các số 1 trong các Ví dụ 3-4 (khó nén) và ma trận Hilbert ác mộng $H(i, j) = (i + j - 1)^{-1}$ trong Phần 8.3: hãy nén nó lại để làm việc với nó.

Tác giả trung thành của các bạn đã tiếp tục nghiên cứu về hạng của những lá cờ. Khá nhiều lá cờ dựa trên các sọc ngang hoặc dọc. Những lá cờ đó có *hạng một - tất cả* các hàng hoặc tất cả các cột đều là bội số của vectơ *ones* $(1, 1, \dots, 1)$. Armenia, Áo, Bỉ, Bulgaria, Chad, Colombia, Ireland, Madagascar, Mali, Hà Lan, Nigeria, Romania, Nga (và nhiều nước khác) có ba sọc. Indonesia và Ba Lan có hai! Libya là trường hợp cực đoan trong những năm Gadaffi từ 1977 đến 2011 *(toàn bộ lá cờ màu xanh lá cây).*

Ở thái cực khác, nhiều lá cờ bao gồm các đường chéo. Đó có thể là các đường chéo dài như trong cờ của Anh. Hoặc chúng có thể là các đường chéo ngắn bắt nguồn từ các cạnh của một ngôi sao như trong cờ của Hoa Kỳ. Ví dụ trong phần văn bản về một tam giác chứa các số 1 cho thấy làm thế nào các ma trận cờ đó sẽ có hạng lớn. Hạng tăng lên vô cùng khi kích thước pixel trở nên nhỏ.

Các lá cờ khác có hình tròn hoặc hình lưỡi liềm hoặc các hình dạng cong khác nhau. Hạng của chúng lớn và cũng tăng lên tới vô cực. Những lá cờ này vẫn có thể nén được! Hình ảnh được nén sẽ không hoàn hảo nhưng mắt chúng ta sẽ không thấy sự khác biệt (với đủ các số hạng $\sigma_i u_i v_i^T$ từ SVD). Những ví dụ đó thực sự làm nổi bật mục đích chính của việc nén hình ảnh:

#### **Chất lượng hiển thị có thể được bảo tồn ngay cả với một sự suy giảm lớn về thứ hạng.**

Cho vui, tôi đã nhìn lại những lá cờ có hạng hữu hạn. Chúng có thể có các sọc và chúng cũng có thể có các chữ thập - miễn là các cạnh của chữ thập là nằm ngang hoặc thẳng đứng. Một số lá cờ có một đường viền mỏng xung quanh chữ thập. Đặc điểm nghệ thuật này sẽ làm tăng thứ hạng. Ngay bây giờ, nhà vô địch của tôi là quốc kỳ Hy Lạp được hiển thị dưới đây, với một chữ thập và cả các sọc. Hạng của nó là **ba** theo cách đếm của tôi (ba cột khác nhau). Tôi không thấy Quốc kỳ nào của các Bang thuộc Hoa Kỳ có hạng hữu hạn!

Người đọc có thể google "national flags" để xem sự đa dạng về thiết kế và màu sắc. Tôi sẽ rất vui khi biết bất kỳ ví dụ hạng hữu hạn nào có hạng $> 3$. Những ví dụ tốt thuộc mọi loại sẽ được đăng tải trên trang web của cuốn sách **math.mit.edu/linearalgebra** (và các lá cờ với đủ màu sắc).

![](images/_page_378_Picture_8.jpeg)

![](images/_page_378_Picture_9.jpeg)

![](images/_page_378_Picture_10.jpeg)

$$A = U\Sigma V^T = 3u_1 v_1^T + 2u_2 v_2^T + 1u_3 v_3^T$$

*Lưu ý* Giả sử tôi loại bỏ hàng cuối cùng của $A$ (toàn là số không). Khi đó $A$ là một ma trận $3 \times 4$ và $AA^T$ có kích thước $3 \times 3$ - hàng và cột thứ tư của nó sẽ biến mất. Chúng ta vẫn có các trị riêng $\lambda = 1, 4, 9$ trong $A^T A$ và $AA^T$, tạo ra cùng các giá trị suy biến $\sigma = 3, 2, 1$ trong $\Sigma$.

Việc loại bỏ hàng số không của $A$ (bây giờ là $3 \times 4$) chỉ loại bỏ hàng cuối cùng của $\Sigma$ và cũng loại bỏ hàng và cột cuối cùng của $U$. Khi đó $(3 \times 4) = U\Sigma V^T = (3 \times 3)(3 \times 4)(4 \times 4)$. SVD hoàn toàn thích ứng với các ma trận hình chữ nhật.

Một điều tốt, bởi vì các hàng và các cột của một ma trận dữ liệu $A$ thường có ý nghĩa hoàn toàn khác nhau (giống như một bảng tính spreadsheet). Nếu chúng ta có điểm cho tất cả các môn học, sẽ có một cột cho mỗi sinh viên và một hàng cho mỗi môn học: Phần tử $a_{ij}$ sẽ là điểm số. Khi đó $\sigma_1 u_1 v_1^T$ có thể có $u_1 = \text{tổ hợp môn học}$ và $v_1 = \text{tổ hợp sinh viên}$. Và $\sigma_1$ sẽ là điểm số cho các tổ hợp đó: điểm số cao nhất.

Ma trận $A$ có thể đếm tần suất của các từ khóa trong một tạp chí: Mỗi bài báo khác nhau cho mỗi cột của $A$ và một từ khác nhau cho mỗi hàng. Toàn bộ tạp chí được lập chỉ mục bởi ma trận $A$ và thông tin quan trọng nhất nằm trong $\sigma_1 u_1 v_1^T$. Khi đó $\sigma_1$ là tần suất lớn nhất cho một siêu từ (hyperword) (tổ hợp từ $u_1$) trong một siêu bài báo (hyperarticle) $v_1$.

Phần 7.3 sẽ áp dụng SVD cho tài chính, di truyền học và các công cụ tìm kiếm.

### Tính Ổn định của Giá trị Suy biến so với Tính Không ổn định của Trị riêng

Ví dụ $4 \times 4$ của $A$ cung cấp một ví dụ (một trường hợp cực đoan) về tính không ổn định của các trị riêng. **Giả sử phần tử (4,1) thay đổi rất nhỏ** từ 0 lên 1/60,000. Hạng bây giờ là 4.

$$A = \begin{bmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3 \\ 1/60000 & 0 & 0 & 0 \end{bmatrix} \quad \begin{array}{l} \text{Sự thay đổi chỉ bằng 1/60,000 đó tạo ra một} \\ \text{bước nhảy lớn hơn rất nhiều trong các trị riêng của } A \\ \lambda = 0,0,0,0 \text{ thành } \lambda = \frac{1}{10}, \frac{i}{10}, \frac{-1}{10}, \frac{-i}{10} \end{array}$$

Bốn trị riêng đã di chuyển từ số không ra một đường tròn quanh số không. Đường tròn có bán kính $1/10$ khi phần tử mới chỉ là 1/60,000. Điều này cho thấy tính không ổn định nghiêm trọng của các trị riêng khi $AA^T$ khác xa so với $A^T A$. Ở thái cực khác, nếu $A^T A = AA^T$ (một "ma trận chuẩn - normal matrix"), các vectơ riêng của $A$ trực giao với nhau và các trị riêng của $A$ hoàn toàn ổn định.

Ngược lại, **các giá trị suy biến của bất kỳ ma trận nào cũng đều ổn định**. Chúng không thay đổi nhiều hơn sự thay đổi trong $A$. Trong ví dụ này, các giá trị suy biến mới là **3, 2, 1**, và **1/60,000**. Các ma trận $U$ và $V$ vẫn giữ nguyên. Phần thứ tư mới của $A$ là $\sigma_4 u_4 v_4^T$, với mười lăm số không và phần tử nhỏ đó là $\sigma_4 = 1/60,000$.

### Các Vectơ Suy biến của $A$ và Các Vectơ Riêng của $S = A^T A$

Các phương trình (5-6) đã "chứng minh" SVD *tất cả cùng một lúc*. Các vectơ suy biến $v_i$ là các vectơ riêng $q_i$ của $S = A^T A$. Các trị riêng $\lambda_i$ của $S$ bằng với các $\sigma_i^2$ của $A$. Hạng $r$ của $S$ bằng hạng của $A$. Các phép khai triển thành vectơ riêng và vectơ suy biến hoàn toàn song song với nhau.

**$S$ đối xứng**

**Bất kỳ ma trận $A$ nào**

$$S = Q\Lambda Q^T = \lambda_1 q_1 q_1^T + \lambda_2 q_2 q_2^T + \cdots + \lambda_r q_r q_r^T$$

$$A = U\Sigma V^T = \sigma_1 u_1 v_1^T + \sigma_2 u_2 v_2^T + \cdots + \sigma_r u_r v_r^T$$

Các chữ $q$ trực chuẩn, các chữ $u$ trực chuẩn, các chữ $v$ trực chuẩn. Tuyệt đẹp.

Nhưng tôi muốn xem lại lần nữa, vì hai lý do chính đáng. Một là để khắc phục một điểm yếu trong phần trị riêng, nơi mà Chương 6 chưa được hoàn thiện. Nếu $\lambda$ là một trị riêng *kép (double eigenvalue)* của $S$, chúng ta có thể và phải tìm *hai* vectơ riêng trực chuẩn. Lý do khác là để xem cách SVD chọn ra số hạng lớn nhất $\sigma_1 u_1 v_1^T$ trước $\sigma_2 u_2 v_2^T$. Chúng ta muốn hiểu các trị riêng $\lambda$ (của $S$) và các giá trị suy biến $\sigma$ (của $A$) **từng cái một thay vì tất cả cùng một lúc**.

Bắt đầu với trị riêng lớn nhất $\lambda_1$ của $S$. Nó giải bài toán sau:

$$\lambda_1 = \text{tỷ số cực đại } \frac{x^T S x}{x^T x}. \text{ Vectơ chiến thắng là } x = q_1 \text{ với } S q_1 = \lambda_1 q_1. \quad (8)$$

So sánh với giá trị suy biến lớn nhất $\sigma_1$ của $A$. Nó giải bài toán sau:

$$\sigma_1 = \text{tỷ số cực đại } \frac{\|Ax\|}{\|x\|}. \text{ Vectơ chiến thắng là } x = v_1 \text{ với } A v_1 = \sigma_1 u_1. \quad (9)$$

"Cách tiếp cận từng cái một" này cũng áp dụng cho $\lambda_2$ và $\sigma_2$. Nhưng không phải tất cả các chữ $x$ đều được phép:

$$\lambda_2 = \text{tỷ số cực đại } \frac{x^T S x}{x^T x} \text{ trong số tất cả các } x \text{ thỏa mãn } q_1^T x = 0. \quad x = q_2 \text{ sẽ chiến thắng.} \quad (10)$$

$$\sigma_2 = \text{tỷ số cực đại } \frac{\|Ax\|}{\|x\|} \text{ trong số tất cả các } x \text{ thỏa mãn } v_1^T x = 0. \quad x = v_2 \text{ sẽ chiến thắng.} \quad (11)$$

Khi $S = A^T A$, chúng ta tìm được $\lambda_1 = \sigma_1^2$ và $\lambda_2 = \sigma_2^2$. Tại sao cách tiếp cận này lại thành công?

Bắt đầu với tỷ số $r(x) = x^T S x / x^T x$. Đây được gọi là *thương số Rayleigh (Rayleigh quotient)*. Để cực đại hóa $r(x)$, đặt các đạo hàm riêng của nó bằng 0: $\partial r / \partial x_i = 0$ cho $i = 1, \dots, n$. Những đạo hàm đó khá rắc rối và đây là kết quả: một phương trình vectơ cho $x$ chiến thắng:

$$\text{Các đạo hàm của } r(x) = \frac{x^T S x}{x^T x} \text{ bằng không khi } Sx = r(x)x. \quad (12)$$

Vì vậy $x$ chiến thắng là một vectơ riêng của $S$. Tỷ số cực đại $r(x)$ chính là trị riêng lớn nhất $\lambda_1$ của $S$. Mọi thứ đều tốt. Bây giờ chuyển sang $A$ - và chú ý đến mối liên hệ với $S = A^T A$!

$$\text{Việc cực đại hóa } \frac{\|Ax\|}{\|x\|} \text{ cũng cực đại hóa } \left( \frac{\|Ax\|}{\|x\|} \right)^2 = \frac{x^T A^T A x}{x^T x} = \frac{x^T S x}{x^T x}.$$

Vì vậy $x = v_1$ chiến thắng trong (9) cũng chính là vectơ riêng hàng đầu $q_1$ của $S = A^T A$ trong (8).

Bây giờ tôi phải giải thích tại sao $q_2$ và $v_2$ là những vectơ chiến thắng trong (10) và (11). Chúng ta biết chúng trực giao với $q_1$ và $v_1$, vì vậy chúng được cho phép tham gia trong những cuộc tranh tài đó. Các đoạn này có thể là tùy chọn đối với những độc giả chỉ muốn xem SVD trong thực tế (Phần 7.3).

Bắt đầu với bất kỳ ma trận trực giao $Q_1$ nào có $q_1$ trong cột đầu tiên của nó. $n - 1$ cột trực chuẩn còn lại chỉ cần trực giao với $q_1$. Sau đó sử dụng $Sq_1 = \lambda_1 q_1$:

$$SQ_1 = S[q_1 \ q_2 \ \dots \ q_n] = [q_1 \ q_2 \ \dots \ q_n] \begin{bmatrix} \lambda_1 & w^T \\ 0 & S_{n-1} \end{bmatrix} = Q_1 \begin{bmatrix} \lambda_1 & w^T \\ 0 & S_{n-1} \end{bmatrix}. \quad (13)$$

Nhân với $Q_1^T$, nhớ rằng $Q_1^T Q_1 = I$, và nhận ra rằng $Q_1^T SQ_1$ cũng đối xứng giống như $S$:

$$\text{Tính đối xứng của } Q_1^T SQ_1 = \begin{bmatrix} \lambda_1 & w^T \\ 0 & S_{n-1} \end{bmatrix} \text{ buộc } w = 0 \text{ và } S_{n-1}^T = S_{n-1}.$$

Yêu cầu $q_1^T x = 0$ đã thu gọn bài toán cực đại (10) xuống kích thước $n - 1$. Trị riêng lớn nhất của $S_{n-1}$ sẽ là trị riêng lớn *thứ hai* của $S$. **Đó là $\lambda_2$.** Vectơ chiến thắng trong (10) sẽ là vectơ riêng $q_2$ với $Sq_2 = \lambda_2 q_2$.

Chúng ta chỉ cần tiếp tục - hoặc sử dụng từ khóa ma thuật *quy nạp (induction)* - để tạo ra tất cả các vectơ riêng $q_1, \dots, q_n$ và các trị riêng của chúng $\lambda_1, \dots, \lambda_n$. Định lý Phổ $S = Q\Lambda Q^T$ được chứng minh ngay cả với các trị riêng lặp (repeated eigenvalues). Tất cả các ma trận đối xứng đều có thể được chéo hóa.

Tương tự, SVD được tìm ra theo từng bước một từ (9) và (11) và trở về sau. Phần 7.4 sẽ chỉ ra hình học của nó - chúng ta đang tìm kiếm các trục của một hình elip. Ở đây tôi hỏi một câu hỏi khác: **Các $\lambda$ và các $\sigma$ thực sự được tính toán như thế nào?**

### Việc tính toán các Trị riêng của $S$ và Các Giá trị Suy biến của $A$

Các giá trị suy biến $\sigma_i$ của $A$ là căn bậc hai của các trị riêng $\lambda_i$ của $S = A^T A$. Điều này kết nối SVD với một *bài toán trị riêng đối xứng (symmetric eigenvalue problem)* (rất tốt). Nhưng cuối cùng thì chúng ta không muốn nhân $A^T$ với $A$ (việc bình phương tốn nhiều thời gian: không tốt).

Ý tưởng đầu tiên là *tạo ra các số không trong $A$ và $S$ mà không làm thay đổi bất kỳ $\sigma$ và $\lambda$ nào*. Các vectơ suy biến và các vectơ riêng sẽ thay đổi - không vấn đề gì. Ma trận đồng dạng $Q^{-1}SQ$ có cùng các $\lambda$ như $S$. Nếu $Q$ là ma trận trực giao, ma trận này là $Q^T SQ$ và vẫn đối xứng.

Phần 11.3 sẽ chỉ ra cách xây dựng $Q$ từ các phép quay $2 \times 2$ sao cho $Q^T SQ$ là ma trận **đối xứng và tridiagonal (ba đường chéo)** (nhiều số không). Nhưng các phép quay không thể đi đến tận cùng để tạo ra một ma trận đường chéo. Việc thể hiện tất cả các trị riêng của $S$ cần một ý tưởng mới và nhiều công sức hơn.

Đối với SVD, điểm tương đồng với $Q^T SQ$ là gì? Bây giờ chúng ta không muốn thay đổi bất kỳ giá trị suy biến nào của $A$. Câu trả lời tự nhiên: Bạn có thể nhân $A$ với *hai ma trận trực giao khác nhau* $Q_1$ và $Q_2$. Sử dụng chúng để tạo ra các số không trong $Q_1^T A Q_2$. Các $\sigma$ không thay đổi:

$$(Q_1^T A Q_2)^T (Q_1^T A Q_2) = Q_2^T A^T A Q_2 = Q_2^T SQ_2 \text{ cho cùng } \sigma(A) \text{ và } \lambda(S).$$

Sự tự do của hai chữ $Q$ cho phép chúng ta đạt tới $Q_1^T A Q_2 =$ **ma trận bidiagonal (hai đường chéo)** (2 đường chéo). Điều này có thể so sánh một cách hoàn hảo với $Q^T SQ =$ 3 đường chéo. Thật tuyệt khi nhận thấy mối liên hệ giữa chúng: $(\text{bidiagonal})^T (\text{bidiagonal}) = \text{tridiagonal}$.

Những bước cuối cùng để đi tới một $\Lambda$ *đường chéo* và một $\Sigma$ *đường chéo* cần nhiều ý tưởng hơn. Bài toán này không thể dễ dàng, bởi vì bên dưới chúng ta đang giải $\det(S - \lambda I) = 0$ cho các đa thức bậc $n = 100$ hoặc $1000$ hoặc lớn hơn. Chắc chắn chúng ta không sử dụng những đa thức đó!

Cách ưa thích để tìm các $\lambda$ và các $\sigma$ trong LAPACK là sử dụng các ma trận trực giao đơn giản để tiệm cận $Q^T SQ = \Lambda$ và $U^T AV = \Sigma$. **Chúng ta dừng lại khi ở rất gần với $\Lambda$ và $\Sigma$.**

Cách tiếp cận 2 bước này (các số không trước) được tích hợp vào các lệnh `eig(S)` và `svd(A)`.

#### **• ÔN TẬP CÁC Ý TƯỞNG THEN CHỐT •**

- **1.** SVD phân tích thành nhân tử $A$ thành $U\Sigma V^T$, với $r$ giá trị suy biến $\sigma_1 \geq \sigma_2 \geq \dots \geq \sigma_r > 0$.
- **2.** Các con số $\sigma_1^2, \dots, \sigma_r^2$ là các trị riêng khác không của $AA^T$ và $A^T A$.
- **3.** Các cột trực chuẩn của $U$ và $V$ là các vectơ riêng của $AA^T$ và $A^T A$.
- **4.** Các cột đó chứa các cơ sở trực chuẩn cho bốn không gian con cơ bản của $A$.
- **5.** Các cơ sở đó chéo hóa ma trận: $Av_i = \sigma_i u_i$ đối với $i \leq r$. Đây là $AV = U\Sigma$.
- **6.** $A = \sigma_1 u_1 v_1^T + \dots + \sigma_r u_r v_r^T$ và $\sigma_1$ là giá trị lớn nhất của tỷ số $\|Ax\| / \|x\|$.

#### **• CÁC VÍ DỤ CÓ LỜI GIẢI •**

**7.2 A** Nhận dạng theo tên các phân tích ma trận $A$ thành tổng của các cột nhân các hàng:

- **1.** *Các cột trực giao* $u_1\sigma_1, \dots, u_r\sigma_r$ nhân với *các hàng trực chuẩn* $v_1^T, \dots, v_r^T$.
- **2.** Các cột *trực chuẩn* $q_1, \dots, q_r$ nhân với *các hàng của ma trận tam giác* $r_1^T, \dots, r_r^T$.
- **3.** Các cột của ma trận *tam giác* $l_1, \dots, l_r$ nhân với các hàng của ma trận *tam giác* $u_1^T, \dots, u_r^T$. Hạng và các pivot (phần tử trục) cùng các giá trị suy biến của $A$ đi vào bức tranh này ở đâu?

**Lời giải** Ba phép phân tích thành nhân tử này là cơ bản đối với đại số tuyến tính, dù là thuần túy hay ứng dụng:

- **1. Phân tích Giá trị Suy biến (Singular Value Decomposition)** $A = U\Sigma V^T$
- **2. Trực giao hóa Gram-Schmidt (Gram-Schmidt Orthogonalization)** $A = QR$
- **3. Khử Gauss (Gaussian Elimination)** $A = LU$

Bạn có thể muốn tách riêng các giá trị suy biến $\sigma_i$ và các chiều cao $h_i$ và các pivot $d_i$:

- **1.** $A = U\Sigma V^T$ với các vectơ đơn vị trong $U$ và $V$. *r giá trị suy biến $\sigma_i$ nằm trong $\Sigma$.*
- **2.** $A = Q H R$ với các vectơ đơn vị trong $Q$ và các số 1 trên đường chéo của $R$. *$r$ chiều cao $h_i$ nằm trong $H$.*
- **3.** $A = LDU$ với các số 1 trên đường chéo của $L$ và $U$. *$r$ pivot $d_i$ nằm trong $D$.*

Mỗi $h_i$ cho biết chiều cao của cột $i$ phía trên mặt phẳng chứa các cột từ $1$ đến $i - 1$. Thể tích của hộp $n$ chiều đầy đủ ($r = m = n$) đến từ $A = U\Sigma V^T = LDU = QHR$:

| $\det A$ | = | tích của các $\sigma$ | = | tích của các $d$ | = | tích của các $h$ |.

**7.2 B Chứng minh rằng** $\sigma_1 \geq |\lambda|_{\text{max}}$. **Giá trị suy biến lớn nhất chi phối tất cả các trị riêng.**

**Lời giải** Bắt đầu từ $A = U\Sigma V^T$. Hãy nhớ rằng việc nhân với một ma trận trực giao *không làm thay đổi độ dài:* $\|Qx\| = \|x\|$ bởi vì $\|Qx\|^2 = x^T Q^T Q x = x^T x = \|x\|^2$. Điều này áp dụng cho $Q = U$ và $Q = V^T$. Ở giữa là ma trận đường chéo $\Sigma$.

$$\|Ax\| = \|U\Sigma V^T x\| = \|\Sigma V^T x\| \leq \sigma_1 \|V^T x\| = \sigma_1 \|x\|. \quad (14)$$

Một vectơ riêng có $\|Ax\| = |\lambda| \|x\|$. Vậy (14) nói rằng $|\lambda| \|x\| \leq \sigma_1 \|x\|$. Khi đó $|\lambda| \leq \sigma_1$.

Cũng áp dụng đối với vectơ đơn vị $x = (1, 0, \dots, 0)$. Bây giờ $Ax$ là cột đầu tiên của $A$. Khi đó theo bất đẳng thức (14), cột này có độ dài $\leq \sigma_1$. Mọi phần tử đều phải có $|a_{ij}| \leq \sigma_1$.

Phương trình (14) một lần nữa cho thấy rằng *giá trị cực đại của* $\|Ax\| / \|x\|$ *bằng* $\sigma_1$.

Phần 11.2 sẽ giải thích cách mà tỷ số $\sigma_{\text{max}} / \sigma_{\text{min}}$ chi phối sai số làm tròn (roundoff error) trong việc giải $Ax = b$. MATLAB sẽ cảnh báo bạn nếu *"số điều kiện (condition number)"* này lớn. Khi đó $x$ là không đáng tin cậy.
### **Tập bài tập 7.1 (Problem Set 7.1)**

**1** Hạng $r$ của những ma trận này là bao nhiêu với các phần tử là $i$ nhân $j$ và $i$ cộng $j$? Hãy viết $A$ và $B$ dưới dạng tổng của $r$ phần $uv^T$ có hạng bằng 1. Không yêu cầu $u_1^T u_2 = v_1^T v_2 = 0$.

$$A = \begin{bmatrix} 1 & 2 & 3 & 4 \\ 2 & 4 & 6 & 8 \\ 3 & 6 & 9 & 12 \\ 4 & 8 & 12 & 16 \end{bmatrix} \quad B = \begin{bmatrix} 2 & 3 & 4 & 5 \\ 3 & 4 & 5 & 6 \\ 4 & 5 & 6 & 7 \\ 5 & 6 & 7 & 8 \end{bmatrix}$$

**2** Chúng ta thường nghĩ rằng ma trận đơn vị $I$ là càng đơn giản càng tốt. Nhưng tại sao $I$ lại hoàn toàn không thể nén được? *Hãy vẽ một lá cờ có hạng 5 với một chữ thập.*

**3** Những lá cờ này có hạng bằng 2. Hãy viết $A$ và $B$ theo bất kỳ cách nào dưới dạng $u_1 v_1^T + u_2 v_2^T$.

$$A_{\text{Thụy Điển}} = A_{\text{Phần Lan}} = \begin{bmatrix} 1 & 2 & 1 & 1 \\ 2 & 2 & 2 & 2 \\ 1 & 2 & 1 & 1 \end{bmatrix} \quad B_{\text{Benin}} = \begin{bmatrix} 1 & 2 & 2 \\ 1 & 3 & 3 \end{bmatrix}$$

**4** Bây giờ hãy tìm vết và định thức của Bài 3. Các giá trị suy biến của $B$ gần với $\sigma_1 \approx 5.28$ và $\sigma_2 \approx 0.27$. $B$ có thể nén được hay không?

**5** Sử dụng lệnh `[U, S, V] = svd(A)` để tìm hai phần trực giao $\sigma u v^T$ của $A_{\text{Thụy Điển}}$.

**6** Tìm các trị riêng và các giá trị suy biến của ma trận $A$ $2 \times 2$ này:

$$A = \begin{bmatrix} 2 & 1 \\ 4 & 2 \end{bmatrix}$$
với $A^T A = \begin{bmatrix} 20 & 10 \\ 10 & 5 \end{bmatrix}$ và $AA^T = \begin{bmatrix} 5 & 10 \\ 10 & 20 \end{bmatrix}$.

Các vectơ riêng $(1, 2)$ và $(1, -2)$ của $A$ không trực giao. Làm thế nào bạn biết các vectơ riêng $v_1, v_2$ của $A^T A$ là trực giao? Chú ý rằng $A^T A$ và $AA^T$ có cùng các trị riêng (25 và 0).

**7** Làm thế nào dạng thứ hai $AV = U\Sigma$ trong phương trình (3) được suy ra từ dạng đầu tiên $A = U\Sigma V^T$? Đó là dạng nổi tiếng nhất của SVD.

**8** Hai cột của $AV = U\Sigma$ là $Av_1 = \sigma_1 u_1$ và $Av_2 = \sigma_2 u_2$. Vì vậy chúng ta hy vọng rằng

$$Av_1 = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} \sigma_1 \\ 1 \end{bmatrix} = \sigma_1 \begin{bmatrix} 1 \\ \sigma_1 \end{bmatrix} \quad \text{và} \quad \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ -\sigma_1 \end{bmatrix} = \sigma_2 \begin{bmatrix} \sigma_1 \\ -1 \end{bmatrix}.$$

Phương trình đầu tiên cần $\sigma_1 + 1 = \sigma_1^2$ và phương trình thứ hai cần $1 - \sigma_1 = -\sigma_2$. Những điều đó có đúng không?

**9** Các lệnh MATLAB `A = rand(20, 40)` và `B = randn(20, 40)` tạo ra các ma trận ngẫu nhiên $20 \times 40$. Các phần tử của $A$ nằm giữa 0 và 1 với xác suất đồng đều. Các phần tử của $B$ có phân bố xác suất "hình chuông" chuẩn. Sử dụng lệnh `svd`, hãy tìm và vẽ đồ thị các giá trị suy biến của chúng từ $\sigma_1$ đến $\sigma_{20}$. Tại sao chúng lại có 20 giá trị $\sigma$?

# **7.2 Các Cơ sở và Các Ma trận trong SVD**

**1** SVD tạo ra **các cơ sở trực chuẩn (orthonormal basis)** của các chữ $v$ và các chữ $u$ cho bốn không gian con cơ bản.
**2** Sử dụng những cơ sở đó, $A$ trở thành một ma trận đường chéo $\Sigma$ và $Av_i = \sigma_i u_i$: $\sigma_i = \text{giá trị suy biến}.$
**3** Việc chéo hóa bằng hai cơ sở $A = U\Sigma V^T$ thường có nhiều thông tin hơn so với $A = X \Lambda X^{-1}$.
**4** $U\Sigma V^T$ phân tách $A$ thành các ma trận hạng 1 $\sigma_1 u_1 v_1^T + \dots + \sigma_r u_r v_r^T$. $\sigma_1 u_1 v_1^T$ là phần lớn nhất!

Phân tích Giá trị Suy biến là một điểm nổi bật của đại số tuyến tính. $A$ là bất kỳ ma trận $m \times n$ nào, vuông hoặc chữ nhật. Hạng của nó là $r$. Chúng ta sẽ chéo hóa $A$ này, nhưng không phải bằng $X^{-1} A X$. Các vectơ riêng trong $X$ có ba vấn đề lớn: Chúng thường không trực giao, không phải lúc nào cũng có đủ các vectơ riêng, và $Ax = \lambda x$ đòi hỏi $A$ phải là ma trận vuông. Các *vectơ suy biến* của $A$ giải quyết hoàn hảo tất cả những vấn đề đó.

Hãy để tôi mô tả những gì chúng ta mong muốn từ SVD: **các cơ sở đúng cho bốn không gian con.** Sau đó, tôi sẽ viết về các bước để tìm những vectơ cơ sở đó **theo thứ tự quan trọng.**

Cái giá chúng ta phải trả là phải có **hai tập hợp vectơ suy biến**, các chữ $u$ và các chữ $v$. Các chữ $u$ nằm trong $\mathbb{R}^m$ và các chữ $v$ nằm trong $\mathbb{R}^n$. Chúng sẽ là các cột của một ma trận $m \times m$ $U$ và một ma trận $n \times n$ $V$. Trước tiên, tôi sẽ mô tả SVD theo ngôn ngữ của các vectơ cơ sở đó. Sau đó tôi cũng có thể mô tả SVD theo ngôn ngữ của các ma trận trực giao $U$ và $V$.

(sử dụng vectơ) Các chữ $u$ và các chữ $v$ cung cấp cơ sở cho bốn không gian con cơ bản:
$u_1, \dots, u_r$ là một cơ sở trực chuẩn cho **không gian cột**.
$u_{r+1}, \dots, u_m$ là một cơ sở trực chuẩn cho **không gian null trái** $N(A^T)$.
$v_1, \dots, v_r$ là một cơ sở trực chuẩn cho **không gian hàng**.
$v_{r+1}, \dots, v_n$ là một cơ sở trực chuẩn cho **không gian null** $N(A)$.

Hơn cả tính trực giao, các vectơ cơ sở này chéo hóa ma trận $A$:

| "$A$ được chéo hóa" | $Av_1 = \sigma_1 u_1$ | $Av_2 = \sigma_2 u_2$ | $\dots$ | $Av_r = \sigma_r u_r$ | (1) |
|---------------------|-----------------------|-----------------------|---------|-----------------------|-----|

Những **giá trị suy biến** $\sigma_1$ đến $\sigma_r$ đó sẽ là các số dương: $\sigma_i$ *là độ dài của* $Av_i$. Các $\sigma$ đi vào một ma trận đường chéo mà các phần tử khác đều bằng không. Ma trận đó là $\Sigma$.

(sử dụng ma trận) Vì các chữ $u$ là trực chuẩn, ma trận $U_r$ với $r$ cột đó có $U_r^T U_r = I$. Vì các chữ $v$ là trực chuẩn, ma trận $V_r$ có $V_r^T V_r = I$. Khi đó các phương trình $Av_i = \sigma_i u_i$ cho chúng ta biết theo từng cột rằng $AV_r = U_r \Sigma_r$:

| $(m \times n)(n \times r)$ | $A \left[ v_1 \cdots v_r \right] = \left[ u_1 \cdots u_r \right] \left[ \begin{array}{c} \sigma_1 \\ \vdots \\ \sigma_r \end{array} \right]$ |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| $A V_r = U_r \Sigma_r$     | |
| $(m \times r)(r \times r)$ | |

Đây là trọng tâm của SVD, nhưng còn nhiều hơn thế. Những chữ $v$ và chữ $u$ đó giải quyết được không gian hàng và không gian cột của $A$. Chúng ta có thêm $n - r$ chữ $v$ và $m - r$ chữ $u$ nữa, từ không gian null $N(A)$ và không gian null trái $N(A^T)$. Chúng tự động trực giao với các chữ $v$ và chữ $u$ đầu tiên (bởi vì toàn bộ các không gian null là trực giao). Bây giờ chúng ta đưa tất cả các chữ $v$ và chữ $u$ vào $V$ và $U$, để các ma trận này trở thành *vuông. Chúng ta vẫn có $AV = U\Sigma$.*

| $(m \times n)(n \times n)$ | $A \left[ v_1 \cdots v_r \cdots v_n \right] = \left[ u_1 \cdots u_r \cdots u_m \right] \Sigma$ | (3) |
|----------------------------|----------------------------------------------------------------------------------------------------|-----|
| $AV$ bằng $U\Sigma$        | | |
| $(m \times m)(m \times n)$ | | |

$\Sigma$ mới có kích thước $m \times n$. Nó chỉ là ma trận $r \times r$ trong phương trình (2) với thêm $m - r$ hàng không (zero rows) và $n - r$ cột không (zero columns). Sự thay đổi thực sự nằm ở hình dạng của $U$ và $V$. Đó là các ma trận vuông và $V^{-1} = V^T$. Vậy $AV = U\Sigma$ trở thành $A = U\Sigma V^T$. Đây là *Phân tích Giá trị Suy biến*. Tôi có thể nhân các cột $u_i \sigma_i$ từ $U\Sigma$ với các hàng của $V^T$:

| SVD | $A = U\Sigma V^T = u_1\sigma_1 v_1^T + \dots + u_r\sigma_r v_r^T$ | (4) |
|-----|-------------------------------------------------------------------|-----|

Phương trình (2) là một "SVD thu gọn" với các cơ sở cho không gian hàng và không gian cột. Phương trình (3) là SVD đầy đủ bao gồm cả các không gian null. Cả hai đều tách $A$ thành cùng $r$ ma trận $u_i \sigma_i v_i^T$ có hạng bằng 1. Cột nhân hàng là cách thứ tư để nhân các ma trận.

Chúng ta sẽ thấy rằng mỗi $\sigma_i^2$ là một trị riêng của $A^T A$ và cũng của $AA^T$. Khi chúng ta đặt các giá trị suy biến theo thứ tự giảm dần, $\sigma_1 \geq \sigma_2 \geq \dots \geq \sigma_r > 0$, việc phân tách trong phương trình (4) mang lại $r$ phần hạng 1 của $A$ *theo thứ tự quan trọng*. Điều này rất quan trọng.

**Ví dụ 1** Khi nào thì $A = U\Sigma V^T$ (giá trị suy biến) *giống* với $X\Lambda X^{-1}$ (trị riêng)?

**Lời giải** $A$ cần các vectơ riêng trực chuẩn để cho phép $X = U = V$. $A$ cũng cần các trị riêng $\lambda \geq 0$ nếu $\Lambda = \Sigma$. Vậy $A$ phải là một *ma trận đối xứng nửa xác định dương (hoặc xác định dương)*. Chỉ khi đó $A = X\Lambda X^{-1}$ vốn cũng là $Q\Lambda Q^T$ mới trùng khớp với $A = U\Sigma V^T$.

**Ví dụ 2** Nếu $A = x y^T$ (hạng 1) với các vectơ đơn vị $x$ và $y$, thì SVD của $A$ là gì?

**Lời giải** SVD thu gọn trong (2) chính xác là $x y^T$, với hạng $r = 1$. Nó có $u_1 = x$ và $v_1 = y$ và $\sigma_1 = 1$. Đối với SVD đầy đủ, hãy hoàn thiện $u_1 = x$ thành một cơ sở trực chuẩn của các chữ $u$, và hoàn thiện $v_1 = y$ thành một cơ sở trực chuẩn của các chữ $v$. Không có $\sigma$ nào mới, chỉ có $\sigma_1 = 1$.

#### **Chứng minh cho SVD**

Chúng ta cần chỉ ra làm thế nào những chữ $u$ và chữ $v$ tuyệt vời đó có thể được cấu trúc. Các chữ $v$ sẽ là **các vectơ riêng trực chuẩn của** $A^T A$. Điều này phải đúng bởi vì chúng ta đang nhắm tới

$$A^T A = (U\Sigma V^T)^T (U\Sigma V^T) = V\Sigma^T U^T U\Sigma V^T = V\Sigma^T \Sigma V^T. \quad (5)$$

Ở bên phải, bạn thấy ma trận vectơ riêng $V$ cho ma trận đối xứng (nửa) xác định dương $A^T A$. Và $(\Sigma^T \Sigma)$ phải là ma trận trị riêng của $(A^T A)$: Mỗi $\sigma_i^2$ là một $\lambda(A^T A)$!

Bây giờ $Av_i = \sigma_i u_i$ cho chúng ta biết các vectơ đơn vị $u_1$ đến $u_r$. Đây là phương trình then chốt (1). Điểm thiết yếu - toàn bộ lý do mà SVD thành công - là những vectơ đơn vị $u_1$ đến $u_r$ này tự động trực giao với nhau *(bởi vì các chữ $v$ trực giao):*

| Bước then chốt<br>$i \neq j$ | $u_i^T u_j = \left( \frac{Av_i}{\sigma_i} \right)^T \left( \frac{Av_j}{\sigma_j} \right) = \frac{v_i^T A^T A v_j}{\sigma_i \sigma_j} = \frac{\sigma_j^2}{\sigma_i \sigma_j} v_i^T v_j = 0.$ |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Các chữ $v$ là các vectơ riêng của $A^T A$ (đối xứng). Chúng trực giao và bây giờ các chữ $u$ cũng trực giao. *Thực ra những chữ $u$ đó sẽ là các vectơ riêng của $AA^T$.*

Cuối cùng, chúng ta hoàn thiện các chữ $v$ và chữ $u$ thành $n$ chữ $v$ và $m$ chữ $u$ bằng bất kỳ cơ sở trực chuẩn nào cho các không gian null $N(A)$ và $N(A^T)$. Chúng ta đã tìm được $V$ và $\Sigma$ và $U$ trong $A = U\Sigma V^T$.

### **Một Ví dụ về SVD**

Dưới đây là một ví dụ để chỉ ra việc tính toán cả ba ma trận trong $A = U\Sigma V^T$.

**Ví dụ 3** Tìm các ma trận $U, \Sigma, V$ cho $A = \begin{bmatrix} 3 & 0 \\ 4 & 5 \end{bmatrix}$. Hạng là $r = 2$.

Với hạng 2, $A$ này có các giá trị suy biến dương $\sigma_1$ và $\sigma_2$. Chúng ta sẽ thấy rằng $\sigma_1$ lớn hơn $\lambda_{\text{max}} = 5$, và $\sigma_2$ nhỏ hơn $\lambda_{\text{min}} = 3$. Bắt đầu với $A^T A$ và $AA^T$:

$$A^T A = \begin{bmatrix} 25 & 20 \\ 20 & 25 \end{bmatrix} \quad AA^T = \begin{bmatrix} 9 & 12 \\ 12 & 41 \end{bmatrix}.$$

Những ma trận đó có cùng vết (50) và cùng các trị riêng $\sigma_1^2 = 45$ và $\sigma_2^2 = 5$. Các căn bậc hai là $\sigma_1 = \sqrt{45}$ và $\sigma_2 = \sqrt{5}$. Khi đó $\sigma_1 \sigma_2 = 15$ và đây chính là định thức của $A$.

Một bước then chốt là tìm các vectơ riêng của $A^T A$ (với các trị riêng 45 và 5):

$$\begin{bmatrix} 25 & 20 \\ 20 & 25 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \end{bmatrix} = 45 \begin{bmatrix} 1 \\ 1 \end{bmatrix} \quad \begin{bmatrix} 25 & 20 \\ 20 & 25 \end{bmatrix} \begin{bmatrix} -1 \\ 1 \end{bmatrix} = 5 \begin{bmatrix} -1 \\ 1 \end{bmatrix}$$

Sau đó $v_1$ và $v_2$ là những vectơ riêng trực giao đó được thay đổi tỷ lệ về độ dài 1. Chia cho $\sqrt{2}$.

**Các vectơ suy biến phải**
$$v_1 = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ 1 \end{bmatrix} \quad v_2 = \frac{1}{\sqrt{2}} \begin{bmatrix} -1 \\ 1 \end{bmatrix}$$

**Các vectơ suy biến trái** $\quad u_i = \frac{Av_i}{\sigma_i}$

Bây giờ tính $Av_1$ và $Av_2$, chúng sẽ là $\sigma_1 u_1 = \sqrt{45} u_1$ và $\sigma_2 u_2 = \sqrt{5} u_2$:

$$Av_1 = \frac{3}{\sqrt{2}} \begin{bmatrix} 1 \\ 3 \end{bmatrix} = \sqrt{45} \frac{1}{\sqrt{10}} \begin{bmatrix} 1 \\ 3 \end{bmatrix} = \sigma_1 u_1$$
$$Av_2 = \frac{1}{\sqrt{2}} \begin{bmatrix} -3 \\ 1 \end{bmatrix} = \sqrt{5} \frac{1}{\sqrt{10}} \begin{bmatrix} -3 \\ 1 \end{bmatrix} = \sigma_2 u_2$$

Phép chia cho $\sqrt{10}$ làm cho $u_1$ và $u_2$ trực chuẩn. Khi đó $\sigma_1 = \sqrt{45}$ và $\sigma_2 = \sqrt{5}$ như mong đợi. Phân tích Giá trị Suy biến của $A$ là $U$ nhân $\Sigma$ nhân $V^T$.

$$U = \frac{1}{\sqrt{10}} \begin{bmatrix} 1 & -3 \\ 3 & 1 \end{bmatrix} \quad \Sigma = \begin{bmatrix} \sqrt{45} & 0 \\ 0 & \sqrt{5} \end{bmatrix} \quad V = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix}. \quad (7)$$

$U$ và $V$ chứa các cơ sở trực chuẩn cho không gian cột và không gian hàng (cả hai không gian đều chỉ là $\mathbb{R}^2$). Thành tựu thực sự là hai cơ sở đó chéo hóa $A$: $AV$ bằng $U\Sigma$. Ma trận $A$ tách thành một tổ hợp của hai ma trận hạng 1, các cột nhân với các hàng:

$$\sigma_1 u_1 v_1^T + \sigma_2 u_2 v_2^T = \frac{\sqrt{45}}{\sqrt{20}} \begin{bmatrix} 1 & 1 \\ 3 & 3 \end{bmatrix} + \frac{\sqrt{5}}{\sqrt{20}} \begin{bmatrix} 3 & -3 \\ -1 & 1 \end{bmatrix} = \begin{bmatrix} 3 & 0 \\ 4 & 5 \end{bmatrix} = A.$$

### Một Ma trận Cực đoan

Dưới đây là một ví dụ lớn hơn, khi các chữ $u$ và các chữ $v$ chỉ là các cột của ma trận đơn vị. Vì vậy các tính toán rất dễ dàng, nhưng hãy để mắt đến *thứ tự của các cột*. Ma trận $A$ bị lệch nghiêm trọng (hoàn toàn là ma trận tam giác). Tất cả các trị riêng của nó đều bằng không. $AA^T$ không gần với $A^T A$. Các ma trận $U$ và $V$ sẽ là các ma trận hoán vị giúp khắc phục những vấn đề này một cách thích hợp.

$$A = \begin{bmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$
các trị riêng $\lambda = 0, 0, 0, 0$ tất cả đều bằng không!
chỉ có một vectơ riêng $(1, 0, 0, 0)$
các giá trị suy biến $\sigma = 3, 2, 1$
các vectơ suy biến là các cột của $I$

$A^T A$ và $AA^T$ là các ma trận đường chéo (với các vectơ riêng dễ dàng, nhưng theo thứ tự khác nhau):

$$A^T A = \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 4 & 0 \\ 0 & 0 & 0 & 9 \end{bmatrix} \quad AA^T = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 4 & 0 & 0 \\ 0 & 0 & 9 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

Các vectơ riêng của chúng (các chữ $u$ cho $AA^T$ và các chữ $v$ cho $A^T A$) đi theo thứ tự giảm dần $\sigma_1^2 > \sigma_2^2 > \sigma_3^2$ của các trị riêng. Những trị riêng đó là $\sigma^2 = 9, 4, 1$.

$$U = \begin{bmatrix} 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} \quad \Sigma = \begin{bmatrix} 3 & 0 & 0 & 0 \\ 0 & 2 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix} \quad V = \begin{bmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{bmatrix}$$

Các cột đầu tiên $u_1$ và $v_1$ có các số 1 ở vị trí 3 và 4. Khi đó $u_1 \sigma_1 v_1^T$ chọn ra con số lớn nhất $A_{34} = 3$ trong ma trận $A$ ban đầu. Ba ma trận hạng 1 trong SVD xuất phát (đối với ví dụ cực đoan này) chính xác từ các số 3, 2, 1 trong $A$.

#### **Tập bài tập 7.2 (Problem Set 7.2)**

**1** Tìm các trị riêng của những ma trận này. Sau đó tìm các giá trị suy biến từ $A^T A$:

$$A = \begin{bmatrix} 0 & 4 \\ 0 & 0 \end{bmatrix} \quad A = \begin{bmatrix} 0 & 4 \\ 1 & 0 \end{bmatrix}$$

Đối với mỗi $A$, hãy xây dựng $V$ từ các vectơ riêng của $A^T A$ và $U$ từ các vectơ riêng của $AA^T$. Kiểm tra xem $A = U\Sigma V^T$ có đúng không.

**2** Tìm $A^T A$ và $V$ và $\Sigma$ và $u_i = Av_i/\sigma_i$ và SVD đầy đủ:

$$A = \begin{bmatrix} 2 & 2 \\ -1 & 1 \end{bmatrix} = U\Sigma V^T.$$

**3** Trong Bài 2, hãy chứng tỏ rằng $AA^T$ là ma trận đường chéo. Các vectơ riêng của nó $u_1, u_2$ là \_\_. Các trị riêng của nó $\sigma_1^2, \sigma_2^2$ là \_\_. Các hàng của $A$ trực giao với nhau nhưng chúng không \_\_. Do đó các cột của $A$ không trực giao.

**4** Tính $A^T A$ và $AA^T$ và các trị riêng cùng các vectơ riêng đơn vị của chúng cho $V$ và $U$.

| Ma trận chữ nhật | $A = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}$ |
|--------------------|------------------------------------------------------------|

Kiểm tra $AV = U\Sigma$ (điều này quyết định các dấu $\pm$ trong $U$). $\Sigma$ có cùng hình dạng với $A$: $2 \times 3$.

**5** (a) Không gian hàng của $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$ là 1 chiều. Tìm $v_1$ trong không gian hàng và $u_1$ trong không gian cột. $u_1$ là gì? Tại sao không có $u_2$?
(b) Chọn $v_2$ và $u_2$ trong $U$ và $V$. Khi đó $A = U\Sigma V^T = u_1\sigma_1 v_1^T$ (chỉ có một số hạng).

**6** Thay SVD vào cho $A$ và $A^T$ để chứng minh rằng $A^T A$ có các trị riêng trong $\Sigma^T \Sigma$ và $AA^T$ có các trị riêng trong $\Sigma \Sigma^T$. Vì ma trận đường chéo $\Sigma^T \Sigma$ có cùng các phần tử khác không như $\Sigma \Sigma^T$, chúng ta lại thấy rằng $A^T A$ và $AA^T$ có cùng các trị riêng khác không.

**7** Nếu $(A^T A)v = \sigma^2 v$, nhân với $A$. *Di chuyển các dấu ngoặc đơn để được* $(AA^T)Av = \sigma^2(Av)$. Nếu $v$ là một vectơ riêng của $A^T A$, thì \_\_ là một vectơ riêng của $AA^T$.

**8** Tìm các trị riêng và các vectơ riêng đơn vị $v_1, v_2$ của $A^T A$. Sau đó tìm $u_1 = Av_1/\sigma_1$:

| $A = \begin{bmatrix} 1 & 2 \\ 3 & 6 \end{bmatrix}$ và $A^T A = \begin{bmatrix} 10 & 20 \\ 20 & 40 \end{bmatrix}$ và $AA^T = \begin{bmatrix} 5 & 15 \\ 15 & 45 \end{bmatrix}$. |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Xác minh rằng $u_1$ là một vectơ riêng đơn vị của $AA^T$. Hoàn thành các ma trận $U, \Sigma, V$.

| SVD | $\begin{bmatrix} 1 & 2 \\ 3 & 6 \end{bmatrix} = \begin{bmatrix} u_1 & u_2 \end{bmatrix} \begin{bmatrix} \sigma_1 & 0 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} v_1 & v_2 \end{bmatrix}^T$ |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**9** Viết các cơ sở trực chuẩn cho bốn không gian con cơ bản của $A$ này.

**10** (a) Tại sao vết của $A^T A$ lại bằng tổng bình phương của tất cả các phần tử $a_{ij}^2$? Trong Ví dụ 3, nó bằng 50.
(b) Đối với mọi ma trận hạng 1, tại sao $\sigma_1^2 = \text{tổng bình phương của tất cả các } a_{ij}^2$?

**11** Tìm các trị riêng và các vectơ riêng đơn vị của $A^T A$ và $AA^T$. Giữ mỗi $Av = \sigma u$. Sau đó cấu trúc phân tích giá trị suy biến và xác minh rằng $A$ bằng $U\Sigma V^T$.

| Ma trận Fibonacci | $A = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}$ |
|------------------|----------------------------------------------------|

**12** Sử dụng phần svd trong demo **eigshow** của MATLAB để tìm các chữ $v$ đó bằng đồ thị.

**13** Nếu $A = U\Sigma V^T$ là một ma trận vuông khả nghịch thì $A^{-1} = $ \_\_\_\_\_\_\_\_\_\_\_\_\_. Kiểm tra $A^{-1}A$. Điều này chứng tỏ rằng *các giá trị suy biến của* $A^{-1}$ *là* $1/\sigma_i$. *Lưu ý:* Giá trị suy biến lớn nhất của $A^{-1}$ do đó là $1/\sigma_{\text{min}}(A)$. Trị riêng lớn nhất $|\lambda(A^{-1})|_{\text{max}}$ là $1/|\lambda(A)|_{\text{min}}$. Theo phương trình (14) thì $\sigma_{\text{min}}(A) \leq |\lambda(A)|_{\text{min}}$.

**14** Giả sử $u_1, \dots, u_n$ và $v_1, \dots, v_n$ là các cơ sở trực chuẩn của $\mathbb{R}^n$. Hãy xây dựng ma trận $A = U\Sigma V^T$ biến đổi mỗi $v_j$ thành $u_j$ để cho $Av_1 = u_1, \dots, Av_n = u_n$.

**15** Cấu trúc ma trận hạng 1 có $Av = 12u$ cho $v = \frac{1}{2}(1, 1, 1, 1)$ và $u = \frac{1}{3}(2, 2, 1)$. Giá trị suy biến duy nhất của nó là $\sigma_1 = $ \_\_.

**16** Giả sử $A$ có các cột trực giao $w_1, w_2, \dots, w_n$ với độ dài là $\sigma_1, \sigma_2, \dots, \sigma_n$. $U, \Sigma$, và $V$ trong SVD là gì?

**17** Giả sử $A$ là ma trận đối xứng $2 \times 2$ với các vectơ riêng đơn vị $u_1$ và $u_2$. Nếu các trị riêng của nó là $\lambda_1 = 3$ và $\lambda_2 = -2$, các ma trận $U, \Sigma, V^T$ trong SVD của nó là gì?

**18** Nếu $A = QR$ với một ma trận trực giao $Q$, thì SVD của $A$ gần như giống hệt với SVD của $R$. Ma trận nào trong số ba ma trận $U, \Sigma, V$ bị thay đổi do $Q$?

**19** Giả sử $A$ khả nghịch (với $\sigma_1 > \sigma_2 > 0$). Hãy thay đổi $A$ bằng *một ma trận nhỏ nhất có thể* để tạo ra một ma trận suy biến $A_0$. Gợi ý: $U$ và $V$ không thay đổi:

$$\text{Từ } A = \begin{bmatrix} u_1 & u_2 \end{bmatrix} \begin{bmatrix} \sigma_1 & \\ & \sigma_2 \end{bmatrix} \begin{bmatrix} v_1 & v_2 \end{bmatrix}^T \text{ hãy tìm } A_0 \text{ gần nhất.}$$

**20** Tìm các giá trị suy biến của $A$ từ lệnh `svd(A)` hoặc tính bằng tay.

$$A = \begin{bmatrix} 1 & 0 \\ 100 & 1 \end{bmatrix}. \text{ Tại sao } \sigma_2 = \frac{1}{\sigma_1} \text{ đối với ma trận này?}$$

**21** Tại sao SVD của $A + I$ không đơn giản là sử dụng $\Sigma + I$?

**22** Nếu $A = U\Sigma V^T$ thì $Q_1 A Q_2^T = (Q_1 U) \Sigma (Q_2 V)^T$. Tại sao bất kỳ ma trận trực giao $Q_1$ và $Q_2$ nào cũng để lại $Q_1 U =$ ma trận trực giao và $Q_2 V =$ ma trận trực giao? Khi đó $\Sigma$ **không thấy sự thay đổi nào trong các giá trị suy biến**: $Q_1 A Q_2^T$ có cùng các $\sigma$ như $A$.

**23** Nếu $Q$ là một ma trận trực giao, tại sao tất cả các giá trị suy biến của nó đều bằng 1?

**24** (a) Tìm giá trị lớn nhất của $\frac{x^T S x}{x^T x} = \frac{3x_1^2 + 2x_1 x_2 + 3x_2^2}{x_1^2 + x_2^2}$. Ma trận $S$ là gì?
(b) Tìm giá trị lớn nhất của $\frac{(x_1 + 4x_2)^2}{x_1^2 + x_2^2}$. Đối với ma trận $A$ nào thì điều này bằng $\frac{\|Ax\|^2}{\|x\|^2}$?

**25** **Các giá trị nhỏ nhất** của các tỷ số $\frac{x^T S x}{x^T x}$ và $\frac{\|Ax\|^2}{\|x\|^2}$ là gì? Chúng ta nên lấy $x$ là những vectơ riêng nào của $S$? Có phải $x$ luôn là một vectơ riêng của $A$?

**26** Mọi ma trận $A = U\Sigma V^T$ đều biến **các đường tròn thành các hình elip**. $AV = U\Sigma$ nói rằng các bán kính $v_1$ và $v_2$ của đường tròn đi tới các bán trục (semi-axes) $\sigma_1 u_1$ và $\sigma_2 u_2$ của hình elip. Vẽ đường tròn và hình elip cho $\theta = 30^\circ$:

$$V = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \quad U = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \quad \Sigma = \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix}.$$

Phần 7.4 sẽ bắt đầu với một hình ảnh SVD quan trọng đối với các ma trận $2 \times 2$:
$A = (\text{quay})(\text{kéo giãn})(\text{quay})$. Với tính đối xứng $S = (\text{quay})(\text{kéo giãn})(\text{quay ngược lại})$.

**27** Bài toán này tìm kiếm tất cả các ma trận $A$ với một không gian cột cho trước trong $\mathbb{R}^m$ và một không gian hàng cho trước trong $\mathbb{R}^n$. Giả sử $c_1, \dots, c_r$ và $b_1, \dots, b_r$ là các cơ sở cho hai không gian đó. Biến chúng thành các cột của $C$ và $B$. Mục tiêu là chứng tỏ rằng $A$ có dạng sau:
$A = CMB^T$ với một ma trận khả nghịch $r \times r$ $M$. Gợi ý: Bắt đầu từ $A = U\Sigma V^T$.
$r$ cột đầu tiên của $U$ và $V$ phải được kết nối với $C$ và $B$ bằng các ma trận khả nghịch, bởi vì chúng chứa các cơ sở cho cùng không gian cột (trong $U$) và không gian hàng (trong $V$).

# **7.3 Phân tích Thành phần Chính (PCA bằng SVD)**

**1** Dữ liệu thường đi kèm trong một ma trận: $n$ mẫu và $m$ phép đo cho mỗi mẫu.
**2** Lấy trung tâm cho mỗi hàng của ma trận $A$ bằng cách trừ đi giá trị trung bình từ mỗi phép đo.
**3** SVD tìm kiếm các tổ hợp của dữ liệu chứa nhiều thông tin nhất.
**4** Giá trị suy biến lớn nhất $\sigma_1 \leftrightarrow$ phương sai lớn nhất $\leftrightarrow$ thông tin lớn nhất trong $u_1$.

Phần này giải thích một ứng dụng chính của SVD đối với thống kê và phân tích dữ liệu. Các ví dụ của chúng ta sẽ đến từ di truyền học con người, nhận dạng khuôn mặt và tài chính. Vấn đề là để hiểu được một ma trận dữ liệu (data matrix = các phép đo) lớn. Đối với mỗi mẫu trong $n$ mẫu, chúng ta đang đo lường $m$ biến. Ma trận dữ liệu $A_0$ có $n$ cột và $m$ hàng.

Về mặt đồ thị, các cột của $A_0$ là $n$ điểm trong $\mathbb{R}^m$. Sau khi chúng ta trừ đi giá trị trung bình của mỗi hàng để được $A$, $n$ điểm này thường tập trung dọc theo một đường thẳng hoặc gần với một mặt phẳng (hoặc một không gian con có số chiều thấp khác của $\mathbb{R}^m$). Đường thẳng, mặt phẳng hoặc không gian con đó là gì?

Hãy để tôi bắt đầu bằng một bức tranh thay vì những con số. Với $m = 2$ biến như tuổi và chiều cao, $n$ điểm nằm trong mặt phẳng $\mathbb{R}^2$. Trừ đi độ tuổi và chiều cao trung bình để lấy trung tâm cho dữ liệu. Nếu $n$ điểm đã được đưa về trung tâm tập trung dọc theo một đường thẳng, *làm thế nào đại số tuyến tính sẽ tìm ra đường thẳng đó?*

$A$ là $2 \times n$ (không gian null lớn)
$AA^T$ là $2 \times 2$ (ma trận nhỏ)
$A^T A$ là $n \times n$ (ma trận lớn)
Hai giá trị suy biến $\sigma_1 > \sigma_2 > 0$

Hình 7.2: Các điểm dữ liệu trong $A$ thường nằm gần một đường thẳng trong $\mathbb{R}^2$ hoặc một không gian con trong $\mathbb{R}^m$.

Hãy để tôi đi cẩn thận hơn trong việc xây dựng ma trận dữ liệu. Bắt đầu với các phép đo trong $A_0$: dữ liệu mẫu (sample data). Tìm giá trị trung bình (mean) $\mu_1, \mu_2, \dots, \mu_m$ của mỗi hàng. *Trừ mỗi giá trị trung bình $\mu_i$ từ hàng $i$ để lấy trung tâm (center) cho dữ liệu.* Giá trị trung bình dọc theo mỗi hàng hiện là số không, đối với ma trận đã được lấy trung tâm $A$. Vì vậy điểm $(0,0)$ trong Hình 7.2 giờ đây là trung tâm thực sự của $n$ điểm.

"Ma trận hiệp phương sai mẫu (sample covariance matrix)" được định nghĩa bởi
$$S = \frac{AA^T}{n-1}.$$

$A$ hiển thị khoảng cách $a_{ij} - \mu_i$ từ mỗi phép đo đến trung bình hàng $\mu_i$.
$(AA^T)_{11}$ và $(AA^T)_{22}$ **hiển thị tổng bình phương các khoảng cách (phương sai mẫu $s_1^2, s_2^2$).**
$(AA^T)_{12}$ hiển thị **hiệp phương sai mẫu (sample covariance)** $s_{12} = (\text{hàng 1 của } A) \cdot (\text{hàng 2 của } A)$.

Phương sai là một con số then chốt xuyên suốt thống kê học. Điểm thi trung bình $\mu = 85$ cho bạn biết đó là một bài kiểm tra tốt. Phương sai $s^2 = 25$ (độ lệch chuẩn $s = 5$) có nghĩa là hầu hết các điểm số đều nằm trong khoảng $80$: tập trung sát nhau. Một phương sai mẫu $s^2 = 225$ ($s = 15$) có nghĩa là các điểm số bị phân tán rộng. Chương 12 giải thích về các phương sai.

*Hiệp phương sai* của bài thi toán và bài thi lịch sử là một tích vô hướng của các hàng đó trong $A$, với các điểm số trung bình đã được trừ đi. Hiệp phương sai dưới 0 có nghĩa là: Một môn mạnh khi môn kia yếu. Hiệp phương sai cao có nghĩa là: Cả hai đều mạnh hoặc cả hai đều yếu.

Chúng ta chia cho $n-1$ thay vì $n$ vì những lý do mà các nhà thống kê hiểu rõ nhất. Họ cho tôi biết rằng một bậc tự do (degree of freedom) đã được sử dụng bởi giá trị trung bình, để lại $n-1$. (Tôi nghĩ kế hoạch tốt nhất là đồng ý với họ.) Trong mọi trường hợp $n$ phải là một con số lớn để tin cậy vào các số liệu thống kê. Vì các hàng của $A$ có $n$ phần tử, nên các số trong $AA^T$ có kích thước tăng lên xấp xỉ $n$ và việc chia cho $n-1$ giữ cho chúng ổn định.

### **Ví dụ 1 Sáu điểm toán và lịch sử (chú ý giá trị trung bình bằng 0 ở mỗi hàng)**

| $\mathbf{A} = \begin{bmatrix} 3 & -4 & 7 & 1 & -4 & -3 \\ 7 & -6 & 8 & -1 & -1 & -7 \end{bmatrix}$ có hiệp phương sai mẫu $\mathbf{S} = \frac{\mathbf{A}\mathbf{A}^T}{5} = \begin{bmatrix} 20 & 25 \\ 25 & 40 \end{bmatrix}$. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Hai hàng của $A$ có tương quan cao với nhau: $s_{12} = 25$. Môn toán trên trung bình đi kèm với môn lịch sử trên trung bình. Việc đổi tất cả các dấu trong hàng 2 sẽ tạo ra *hiệp phương sai âm* $s_{12} = -25$. Lưu ý rằng $S$ có vết và định thức dương; $AA^T$ là ma trận xác định dương.

Các trị riêng của $S$ ở khoảng 57 và 3. Vì vậy phần hạng 1 đầu tiên $\sqrt{57} u_1 v_1^T$ lớn hơn nhiều so với phần thứ hai $\sqrt{3} u_2 v_2^T$. **Vectơ riêng hàng đầu** $u_1$ **chỉ ra phương hướng mà bạn nhìn thấy trong biểu đồ phân tán (scatter graph) của Hình 7.2.** Vectơ riêng đó gần với $u_1 = (0.6, 0.8)$ và phương hướng trong biểu đồ gần như cho ta một tam giác vuông $6 - 8 - 10$ hoặc $3 - 4 - 5$.

**SVD của $A$ (dữ liệu được lấy trung tâm) cho thấy phương hướng chủ đạo (dominant direction) trong biểu đồ phân tán.**

Vectơ suy biến thứ hai $u_2$ vuông góc với $u_1$. Giá trị suy biến thứ hai $\sigma_2 \approx \sqrt{3}$ đo lường sự lan truyền ngang qua đường thẳng chủ đạo. Nếu các điểm dữ liệu trong $A$ rơi chính xác trên một đường thẳng (phương $u_1$), thì $\sigma_2$ sẽ bằng 0. Thực ra khi đó sẽ chỉ có $\sigma_1$.

# **Những Yếu tố Cốt lõi của Phân tích Thành phần Chính (PCA)**

PCA cung cấp một cách để hiểu một biểu đồ dữ liệu trong không gian $m$ chiều, với $m = \text{số lượng các biến được đo}$ (ở đây là tuổi và chiều cao). Trừ đi tuổi và chiều cao trung bình ($m = 2$ cho $n$ mẫu) để lấy trung tâm cho ma trận dữ liệu $A$ có kích thước $m \times n$. *Mối liên hệ quan trọng với đại số tuyến tính* nằm ở các giá trị suy biến và các vectơ suy biến của $A$. Những giá trị đó xuất phát từ các trị riêng $\lambda = \sigma^2$ và các vectơ riêng $u$ của ma trận hiệp phương sai mẫu $S = AA^T / (n - 1)$.

- Phương sai tổng (total variance) trong dữ liệu là tổng của tất cả các trị riêng và của các phương sai mẫu $s^2$: **Phương sai tổng** $T = \sigma_1^2 + \dots + \sigma_m^2 = s_1^2 + \dots + s_m^2 = \text{vết (tổng đường chéo)}.$
- Vectơ riêng đầu tiên $u_1$ của $S$ chỉ theo phương hướng có ý nghĩa nhất của dữ liệu. Phương hướng đó giải thích (hoặc *accounts for*) một phần $\sigma_1^2/T$ của phương sai tổng.
- Vectơ riêng tiếp theo $u_2$ (trực giao với $u_1$) giải thích một phần nhỏ hơn $\sigma_2^2/T$.
- Dừng lại khi các phần này nhỏ đi. Bạn đã có được $R$ phương hướng giải thích phần lớn dữ liệu. $n$ điểm dữ liệu nằm rất gần một không gian con $R$ chiều với cơ sở $u_1$ tới $u_R$. Các chữ $u$ này là các **thành phần chính (principal components)** trong không gian $m$ chiều.
- $R$ là "hạng hiệu dụng (effective rank)" của $A$. Hạng thực sự $r$ có lẽ là $m$ hoặc $n$: ma trận hạng đầy đủ.

# **Bình phương Tối thiểu Vuông góc (Perpendicular Least Squares)**

Có thể không nhiều người nhận ra rằng đường thẳng tốt nhất trong Hình 7.2 (đường thẳng theo phương $u_1$) cũng giải quyết một bài toán về *bình phương tối thiểu vuông góc* (perpendicular least squares = hồi quy trực giao (orthogonal regression)):

**Tổng bình phương các khoảng cách từ các điểm tới đường thẳng là nhỏ nhất.**

*Chứng minh* Phân tách mỗi cột $a_j$ của $A$ thành các thành phần của nó dọc theo đường thẳng $u_1$ và đường thẳng $u_2$:

| Tam giác vuông | $\sum_{j=1}^n \|a_j\|^2 = \sum_{j=1}^n (a_j^T u_1)^2 + \sum_{j=1}^n (a_j^T u_2)^2$ | (1) |

Tổng ở bên trái được cố định bởi các điểm dữ liệu $a_j$ (các cột của $A$). Tổng đầu tiên ở bên phải là $u_1^T AA^T u_1$. Vì vậy khi chúng ta cực đại hóa tổng đó trong PCA bằng cách chọn vectơ riêng $u_1$, chúng ta cực tiểu hóa tổng thứ hai. Tổng thứ hai đó (bình phương các khoảng cách từ các điểm dữ liệu tới đường thẳng tốt nhất) là nhỏ nhất đối với bài toán bình phương tối thiểu vuông góc.

Bài toán bình phương tối thiểu thông thường (ordinary least squares) ở Chương 4 đã đi đến một phương trình tuyến tính $A^T Ax = A^T b$ bằng cách sử dụng *các khoảng cách thẳng đứng (vertical distances)* tới đường thẳng tốt nhất. PCA tạo ra một bài toán trị riêng cho $u_1$ bằng cách sử dụng *các khoảng cách vuông góc (perpendicular distances).* "Bình phương tối thiểu toàn phần (total least squares)" sẽ cho phép có các sai số trong $A$ cũng như trong $b$.

# **Ma trận Tương quan Mẫu (The Sample Correlation Matrix)**

Phân tích dữ liệu hoạt động chủ yếu với $A$ (dữ liệu đã được lấy trung tâm). Nhưng các phép đo trong $A$ có thể có các đơn vị khác nhau như inch và pound và năm và đô la. Việc thay đổi một bộ đơn vị (từ inch sang mét hoặc từ năm sang giây) sẽ có ảnh hưởng lớn tới hàng đó của $A$ và $S$. Nếu việc thu phóng kích thước (scaling) là một vấn đề, **chúng ta đổi từ ma trận hiệp phương sai $S$ sang ma trận tương quan (correlation matrix) $C$**:

Một ma trận đường chéo $D$ thu phóng lại $A$. Mỗi hàng của $DA$ có độ dài bằng $\sqrt{n-1}$.

**Ma trận tương quan mẫu** $C = D AA^T D / (n - 1)$ **có các số 1 trên đường chéo của nó.**

Chương 12 về Xác suất và Thống kê sẽ giới thiệu ma trận hiệp phương sai *kỳ vọng (expected)* $V$ và ma trận tương quan *kỳ vọng* (với các số 1 trên đường chéo). Chúng sử dụng các xác suất thay vì các phép đo thực tế. Ma trận hiệp phương sai *dự đoán* sự lan truyền của các phép đo trong tương lai xung quanh giá trị trung bình của chúng, trong khi $A$ và các hiệp phương sai mẫu $S$ cùng với ma trận tương quan đã thu phóng $C = DSD$ sử dụng dữ liệu thực. Tất cả đều rất quan trọng - một mối liên hệ lớn giữa thống kê và đại số tuyến tính của các ma trận xác định dương và SVD.

# **Sự Biến dị Di truyền ở Châu Âu (Genetic Variation in Europe)**

Chúng ta có thể theo dõi những thay đổi trong quần thể con người bằng cách quan sát các bộ gen (genomes). Để quản lý lượng dữ liệu khổng lồ, một cách tốt để xem biến dị di truyền là từ các SNP. Các alen (alleles) không phổ biến (các bazơ A/C/T/G trong một cặp từ cha và mẹ) được đếm bởi SNP:

**SNP** = 0 Không có sự thay đổi nào từ bazơ phổ biến trong quần thể đó : kiểu gen (genotype) bình thường
**SNP** = 1 Cặp bazơ cho thấy một sự thay đổi so với cặp thông thường
**SNP** = 2 Cả hai bazơ đều là alen ít phổ biến hơn

Ma trận chưa lấy trung tâm $A_0$ có một cột cho mỗi người và một hàng cho mỗi cặp bazơ. Các phần tử chủ yếu là 0, một số là 1, không nhiều là 2. Chúng ta không kiểm tra tất cả 3 tỷ cặp. Sau khi trừ đi các giá trị trung bình hàng từ $A_0$, các vectơ riêng của $AA^T$ cho thấy những điều cực kỳ tiết lộ. **Trong Hình 7.3, các vectơ suy biến đầu tiên của** $A$ **gần như tái tạo lại một bản đồ của Châu Âu.**

Điều này có nghĩa là: Các SNP từ Pháp và Đức và Ý khá khác nhau. Thậm chí từ các vùng nói tiếng Pháp, tiếng Đức và tiếng Ý của Thụy Sĩ, những "snip" (SNP) đó cũng khác nhau! Chỉ có Tây Ban Nha và Bồ Đào Nha là bị nhầm lẫn (confounded) một cách đáng ngạc nhiên và khó tách biệt hơn. Thường thì, DNA của một cá nhân tiết lộ nơi sinh của người đó trong vòng 300 km hoặc 200 dặm. Một sự pha trộn của thế hệ ông bà thường đặt đứa cháu ở vị trí giữa các nguồn gốc của họ.

![](images/_page_394_Figure_3.jpeg)

Hình 7.3: *Nature* (2008) Novembre và cộng sự: vol. 456 tr.98-101/doc:10.1038/nature07331.

Thông điệp quan trọng là gì? Nếu chúng ta kiểm tra các bộ gen để hiểu cách chúng tương quan với các căn bệnh, chúng ta không được quên sự biến dị không gian của chúng. Nếu không điều chỉnh cho yếu tố địa lý, những gì trông có vẻ có ý nghĩa về mặt y học có thể rất gây hiểu lầm. *Confounding (Nhiễu/Gây bối rối)* là một vấn đề nghiêm trọng trong di truyền học y khoa mà PCA và di truyền học quần thể có thể giúp giải quyết - nhằm loại bỏ các tác động do yếu tố địa lý vốn không có tầm quan trọng về mặt y học.

Trên thực tế, "thống kê không gian (spatial statistics)" là một thế giới phức tạp. *Ví dụ:* Mọi ma trận với 3 đường chéo gồm 1, $C$, 1 đều cho thấy một sự ảnh hưởng không đáng ngạc nhiên của các nước láng giềng kề sát nhau (từ các số 1). Nhưng các vectơ suy biến của nó có các dao động sin và cos đi ngang qua bản đồ, độc lập với $C$. Bạn có thể nghĩ đó là những biến dị thực sự giống như sóng nhưng chúng có thể vô nghĩa.

Có lẽ thống kê tạo ra nhiều tranh luận hơn là toán học? Việc thu gọn dữ liệu lớn thành một *"P-value"* nhỏ, đơn lẻ có thể mang tính chỉ dẫn hoặc có thể vô cùng lừa đảo. Cụm từ *P-value (Giá trị P)* xuất hiện trong nhiều bài báo. $P$ là viết tắt của xác suất (probability) mà một quan sát nhất quán với *giả thuyết không (null hypothesis = cơ hội ngẫu nhiên thuần túy).* Nếu bạn nhìn thấy 5 lần ngửa liên tiếp, xác suất là $P = 1/32$ rằng điều này đến một cách ngẫu nhiên từ một đồng xu công bằng (hoặc $P = 2/32$ nếu quan sát của bạn được coi là 5 lần ngửa hoặc 5 lần sấp liên tiếp). Thường thì, một P-value dưới $0.05$ làm cho giả thuyết không trở nên đáng ngờ - có lẽ một kẻ gian lận đang tung đồng xu. Như ở đây, các P-value không phải là những chỉ dẫn đáng tin cậy nhất trong thống kê - nhưng chúng cực kỳ tiện lợi.

# **Khuôn mặt riêng (Eigenfaces)**

Việc nhận dạng các khuôn mặt thoạt nhìn dường như không phụ thuộc vào đại số tuyến tính. Nhưng một ứng dụng ban đầu và được quảng bá rộng rãi của SVD là dành cho việc **nhận dạng khuôn mặt.** Chúng ta không nén một hình ảnh, chúng ta đang xác định nó.

Kế hoạch là bắt đầu với một "tập huấn luyện (training set)" $A_0$ gồm $n$ hình ảnh của rất nhiều loại khuôn mặt khác nhau. Mỗi hình ảnh trở thành một vectơ rất dài bằng cách xếp chồng tất cả các giá trị thang độ xám (grayscales) của pixel thành một cột. Sau đó $A_0$ phải được lấy trung tâm: trừ đi giá trị trung bình của mỗi *cột* trong $A_0$ để đạt được $A$.

Vectơ suy biến $v_1$ của $A$ này cho chúng ta biết tổ hợp các khuôn mặt đã biết giúp nhận dạng tốt nhất một khuôn mặt mới. Sau đó $v_2$ cho chúng ta biết tổ hợp tốt nhất tiếp theo.

Có lẽ chúng ta sẽ sử dụng $R$ vectơ tốt nhất $v_1, \dots, v_R$ với các giá trị suy biến lớn nhất $\sigma_1 \geq \dots \geq \sigma_R$ của $A$. Chúng giúp xác định các khuôn mặt mới chính xác hơn bất kỳ $R$ vectơ nào khác. Có lẽ $R = 100$ **eigenfaces** $Av$ đó sẽ nắm bắt gần như toàn bộ phương sai trong tập huấn luyện. $R$ eigenfaces đó trải ra (span) "không gian khuôn mặt (face space)".

Kế hoạch tấn công này được đề xuất bởi Matthew Turk và Alex Pentland. Nó phát triển từ đề xuất của Sirovich và Kirby trong việc sử dụng PCA để nén các hình ảnh khuôn mặt. Tôi đã học được nhiều điều từ phần mô tả của Jeff Jauregui trên Web. Tóm tắt của ông là thế này: **PCA cung cấp một cơ chế để nhận dạng sự tương đồng hình học/đo sáng thông qua các phương tiện đại số.** Ông đã tập hợp thành phần chính đầu tiên (vectơ suy biến đầu tiên) vào trong eigenface đầu tiên. Tất nhiên giá trị trung bình của mỗi cột đã được cộng trở lại, nếu không bạn sẽ không nhìn thấy một khuôn mặt nào cả!

**Lưu ý** PCA được so sánh với NMF trong một bức thư hấp dẫn gửi *Nature* (Lee và Seung, tập 401, 21 tháng 10 năm 1999). Phân tích Ma trận Không âm (Nonnegative Matrix Factorization - NMF) không cho phép các phần tử âm vốn luôn xuất hiện trong các vectơ suy biến $v$. Vì vậy mọi thứ đều được cộng dồn - điều này cần nhiều vectơ hơn nhưng chúng thường có ý nghĩa hơn.

![](images/_page_395_Picture_9.jpeg)

Hình 7.4: Các eigenfaces chọn ra đường chân tóc (hairline) và miệng và mắt và hình dáng.

### **Các ứng dụng của Eigenfaces**

Việc sử dụng thương mại đầu tiên của tính năng nhận diện khuôn mặt bằng PCA là dành cho cơ quan thực thi pháp luật và an ninh. Một cuộc thử nghiệm ban đầu tại Super Bowl 35 ở Tampa đã tạo ra phản ứng rất tiêu cực từ đám đông! Thử nghiệm này diễn ra mà không có sự hay biết của người hâm mộ. Báo chí bắt đầu gọi nó là "Snooper Bowl". Tôi không nghĩ rằng ý tưởng eigenface ban đầu vẫn được sử dụng cho mục đích thương mại (ngay cả một cách bí mật).

Các ứng dụng mới của phương pháp SVD đã đến với các bài toán nhận dạng khác: Eigenvoices (Giọng nói riêng), Eigengaits (Dáng đi riêng), Eigeneyes (Mắt riêng), Eigenexpressions (Biểu cảm riêng). Tôi biết điều này từ Matthew Turk (hiện đang ở Santa Barbara, ban đầu là sinh viên cao học tại MIT. Cậu ấy kể với tôi rằng cậu ấy từng học lớp của tôi). Các eigenfaces nguyên bản trong luận văn của cậu ấy gặp vấn đề về tính toán cho phép quay (rotation) và thu phóng (scaling) và ánh sáng trong các hình ảnh khuôn mặt. Nhưng những ý tưởng then chốt vẫn tiếp tục tồn tại.

Cuối cùng, face space là phi tuyến tính. Vì vậy cuối cùng chúng ta muốn có PCA phi tuyến (nonlinear PCA).

# **Giảm Bậc Mô hình (Model Order Reduction)**

Đối với một bài toán động quy mô lớn, chi phí tính toán có thể trở nên không thể quản lý được. "Động (Dynamic)" có nghĩa là nghiệm $u(t)$ tiến hóa theo thời gian. Dòng chảy chất lỏng, các phản ứng hóa học, sự truyền sóng, sự phát triển sinh học, các hệ thống điện tử, những bài toán này có ở khắp mọi nơi. **Một mô hình rút gọn (reduced model) cố gắng xác định các trạng thái quan trọng của hệ thống.** Từ một bài toán rút gọn, chúng ta tính toán thông tin cần thiết với chi phí thấp hơn nhiều.

Giảm bậc mô hình (Model reduction) thực sự là một phương pháp tính toán quan trọng. Nhiều ý tưởng hay đã được đề xuất để làm giảm bài toán lớn ban đầu. Một ý tưởng đơn giản và thường hữu ích là chụp các "ảnh chụp nhanh (snapshots)" của luồng (flow), đưa chúng vào một ma trận $A$, tìm các thành phần chính (các vectơ suy biến trái của $A$), và làm việc trong không gian con nhỏ hơn nhiều của chúng:

Một **snapshot** là một vectơ cột mô tả trạng thái của hệ thống.
Nó có thể là một phép xấp xỉ cho một trạng thái thực tế điển hình $u(t^*)$.
Từ $n$ snapshots, xây dựng một ma trận $A$ có các cột trải ra một phạm vi các trạng thái hữu ích.

Bây giờ tìm $R$ vectơ suy biến trái đầu tiên $u_1$ tới $u_R$ của $A$. Chúng là một cơ sở cho một Phân tích Trực giao Thích hợp (**POD** - Proper Orthogonal Decomposition). Trong thực tế chúng ta chọn $R$ sao cho

| Phương sai $\approx$ Năng lượng (Energy) | $\sigma_1^2 + \dots + \sigma_R^2$ là | 99% hoặc 99.9% của $\sigma_1^2 + \dots + \sigma_n^2$ |
|---------------------------|--------------------------------------|---------------------------------------------------|

Các vectơ này tạo thành một cơ sở tối ưu cho việc tái cấu trúc các snapshots trong $A$. Nếu những snapshots đó được chọn lựa tốt, thì các tổ hợp của $u_1$ tới $u_R$ sẽ gần với nghiệm chính xác $u(t)$ đối với các thời điểm $t$ và tham số $p$ mong muốn.

Phụ thuộc rất nhiều vào các snapshots! *SIAM Review* năm 2015 bao gồm một bài khảo sát xuất sắc của Beiner, Gugercin và Willcox. SVD nén dữ liệu cũng như nén hình ảnh.

### **Tìm kiếm trên Web**

Chúng tôi tin rằng Google tạo ra thứ hạng (rankings) thông qua một bước đi (walk) đi theo các liên kết web. Khi bước đi này đi tới một trang thường xuyên, thứ hạng sẽ cao. Tần suất truy cập cho ra vectơ riêng hàng đầu ($\lambda = 1$) của "ma trận Web (Web matrix)" - bài toán trị riêng lớn nhất từng được giải.

*Ma trận Markov đó có hơn 3 tỷ hàng và cột, từ 3 tỷ trang web.*

Nhiều kỹ thuật quan trọng là những bí mật được giữ kín của Google. Có lẽ họ bắt đầu với một vectơ riêng trước đó dưới dạng một phép xấp xỉ ban đầu, và họ chạy thuật toán random walk (bước đi ngẫu nhiên) rất nhanh. Để có thứ hạng cao, bạn muốn có nhiều liên kết (links) từ các trang web quan trọng.

Đây là một ứng dụng của SVD đối với các công cụ tìm kiếm web. Khi bạn tra Google một từ, bạn nhận được một danh sách các trang web theo thứ tự tầm quan trọng. Bạn có thể thử gõ "four subspaces".

Thuật toán HITS là một đề xuất ban đầu nhằm tạo ra danh sách được xếp hạng đó. Nó bắt đầu với khoảng 200 trang web được tìm thấy từ một chỉ mục (index) các từ khóa. Sau đó, chúng tôi *chỉ nhìn vào các liên kết giữa các trang web đó.* Công cụ tìm kiếm dựa trên liên kết (link-based) nhiều hơn là dựa trên nội dung (content-based).

Bắt đầu với 200 trang web đó và tất cả các trang web liên kết đến chúng cũng như tất cả các trang web mà chúng liên kết đến. Đó là danh sách của chúng ta, cần được sắp xếp theo thứ tự. Tầm quan trọng có thể được đo lường bằng số liên kết đi ra (links out) và số liên kết đi vào (links in).

- **1.** Trang web đó có thể là một *cơ sở tham chiếu (authority): Các liên kết đi vào* từ nhiều trang web. Đặc biệt là từ các trung tâm (hubs).
- **2.** Trang web đó có thể là một *trung tâm (hub): Các liên kết đi ra* tới nhiều trang web trong danh sách. Đặc biệt là tới các cơ sở tham chiếu.

Chúng ta muốn có các con số $x_1, \dots, x_N$ để xếp hạng các authorities và $y_1, \dots, y_N$ để xếp hạng các hubs. Bắt đầu với một phép đếm đơn giản: $x_i^0$ và $y_i^0$ đếm các liên kết đi vào và đi ra khỏi trang web $i$.

Mấu chốt là đây: *Một authority tốt có liên kết từ các trang web quan trọng* (như hubs). Liên kết từ các trường đại học có trọng lượng nặng hơn liên kết từ bạn bè. *Một hub tốt được liên kết tới các trang web quan trọng* (như authorities). Thật không may là một liên kết tới **amazon.com** lại có ý nghĩa hơn một liên kết tới **wellesleycambridge.com.** Các phép đếm thô (raw counts) $x^0$ và $y^0$ được cập nhật thành $x^1$ và $y^1$ bằng cách tính đến các liên kết *tốt* (đo lường chất lượng của chúng bằng $x^0$ và $y^0$):

**Authority / Hub**
$$x_i^1 / y_i^1 = \text{Cộng các } y_j^0 / x_j^0$$
cho tất cả các liên kết **vào** $i$ / **ra** khỏi $i$ (2)

Trong ngôn ngữ ma trận, chúng là $x^1 = A^T y^0$ và $y^1 = A x^0$. Ma trận $A$ chứa các số 1 và số 0, với $a_{ij} = 1$ khi $i$ liên kết tới $j$. Theo ngôn ngữ đồ thị, $A$ là một "ma trận kề (adjacency matrix)" cho Web (một ma trận khổng lồ). $x^1$ và $y^1$ mới cung cấp các thứ hạng tốt hơn, nhưng chưa phải là tốt nhất. Thực hiện thêm một bước giống như (2), để đạt tới $x^2$ và $y^2$ từ $A^T A x^0$ và $AA^T y^0$:

| Authority | $x^2 = A^T y^1 = A^T A x^0$ | Hub | $y^2 = A x^1 = A A^T y^0$ |
|-----------|-----------------------------|-----|-------------------------|

Trong hai bước, chúng chúng ta đang nhân với $A^T A$ và $AA^T$. Hai mươi bước sẽ nhân với $(A^T A)^{10}$ và $(AA^T)^{10}$. **Khi chúng ta lấy lũy thừa, trị riêng lớn nhất $\sigma_1^2$ bắt đầu chiếm ưu thế.** Các vectơ $x$ và $y$ dóng hàng (line up) với các vectơ riêng hàng đầu $v_1$ và $u_1$ của $A^T A$ và $AA^T$. Chúng ta đang tính toán các số hạng cao nhất trong SVD, bằng **phương pháp lũy thừa (power method)** sẽ được thảo luận trong Phần 11.3. Thật tuyệt vời khi đại số tuyến tính giúp chúng ta hiểu được Web.

Thuật toán HITS này được mô tả trong tờ *Scientific American* năm 1999 (ngày 16 tháng 6). Nhưng tôi không nghĩ rằng SVD được đề cập ở đó. . . Cuốn sách xuất sắc của Langville và Meyer, *Google's PageRank and Beyond*, giải thích chi tiết về khoa học của các công cụ tìm kiếm.

# **PCA trong Tài chính: Động lực học của Lãi suất (The Dynamics of Interest Rates)**

Toán học của tài chính liên tục áp dụng đại số tuyến tính và PCA. Chúng ta chọn một ứng dụng: **đường cong lợi suất (yield curve) đối với chứng khoán Kho bạc.** "Lợi suất (yield)" là lãi suất được trả cho trái phiếu (bonds) hoặc kỳ phiếu (notes) hoặc tín phiếu (bills). Tỷ lệ đó phụ thuộc vào thời gian đáo hạn (time to maturity). Đối với các trái phiếu dài hạn (từ 3 năm đến 20 năm), lãi suất tăng theo độ dài. Cục Dự trữ Liên bang (Federal Reserve) điều chỉnh lợi suất ngắn hạn để làm chậm lại hoặc kích thích nền kinh tế. Đây là *đường cong lợi suất*, được sử dụng bởi các nhà quản lý rủi ro, các nhà giao dịch và các nhà đầu tư.

Đây là dữ liệu cho 6 ngày làm việc đầu tiên của năm 2001 - mỗi cột là một đường cong lợi suất cho các khoản đầu tư vào một ngày cụ thể. Thời gian đáo hạn là "kỳ hạn (tenor)". Sáu cột bên trái là lãi suất, thay đổi từng ngày. Năm cột bên phải là những *chênh lệch về lãi suất giữa các ngày*, với giá trị khác biệt trung bình đã được trừ khỏi mỗi hàng. **Đây là ma trận được lấy trung tâm $A$ với các hàng của nó cộng lại bằng 0.** Một ứng dụng trong thế giới thực có thể bắt đầu với 252 ngày làm việc thay vì 5 hoặc 6 ngày (một năm thay vì một tuần).

**Bảng 1. Lợi suất Kho bạc Hoa Kỳ (U.S. Treasury Yields): 6 Ngày và 5 Chênh lệch Hàng ngày Đã Lấy Trung tâm**

| Kỳ hạn (Tenor) | Lợi suất Kho bạc Hoa Kỳ năm 2001 | Ma trận $A$ tính bằng Điểm cơ bản (0.01%) |
|-------|----------------------------|------------------------------------------------------------|
| 3MO   | 5.87, 5.69, 5.37, 5.12, 5.19, 5.24 | -5.4, -19.4, -12.4, 19.6, 17.6 |
| 6MO   | 5.58, 5.44, 5.20, 4.98, 5.03, 5.11 | -4.6, -14.6, -12.6, 14.4, 17.4 |
| 1YR   | 5.11, 5.04, 4.82, 4.60, 4.61, 4.71 | 1.0, -14.0, -14.0, 9.0, 18.0 |
| 2YR   | 4.87, 4.92, 4.77, 4.56, 4.54, 4.64 | 9.6, -10.4, -16.4, 2.6, 14.0 |
| 3YR   | 4.82, 4.92, 4.78, 4.57, 4.55, 4.65 | 13.4, -10.6, -17.6, 1.4, 13.4 |
| 5YR   | 4.76, 4.94, 4.82, 4.66, 4.65, 4.73 | 18.6, -11.4, -15.4, -0.4, 8.6 |
| 7YR   | 4.97, 5.18, 5.07, 4.93, 4.94, 4.98 | 20.8, -11.2, -14.2, 0.8, 3.8 |
| lOYR  | 4.92, 5.14, 5.03, 4.93, 4.94, 4.98 | 20.8, -12.2, -11.2, -0.2, 2.8 |
| 20YR  | 5.46, 5.62, 5.56, 5.50, 5.52, 5.53 | 14.6, -7.4, -7.4, 0.6, -0.4 |

Với năm cột, chúng ta có thể mong đợi năm giá trị suy biến. Nhưng năm vectơ cột cộng lại bằng vectơ không (bởi vì mọi hàng của $A$ đều cộng lại bằng 0 sau khi lấy trung tâm). Do đó $S = AA^T / (5-1)$ có bốn trị riêng khác 0 $\lambda_1 > \lambda_2 > \lambda_3 > \lambda_4$. Đây là các giá trị suy biến $\sigma_i$ và các bình phương của chúng $\sigma_i^2$ cùng với các phần tỷ lệ của phương sai tổng $T = \sigma_1^2 + \dots + \sigma_4^2 = \text{vết của } S$ được "giải thích" bởi mỗi thành phần chính (mỗi vectơ riêng $u_i$ của $S$).

| | $\sigma_i$ | $\sigma_i^2$ | $\sigma_i^2/T$ |
|---|---|---|---|
| Thành phần chính $u_1$ | 36.39 | 1323.9 | .7536 |
| Thành phần chính $u_2$ | 19.93 | 397.2 | .2261 |

| Thành phần chính $u_3$ | 5.85 | 34.2 | .0195 |
| Thành phần chính $u_4$ | 1.19 | 1.4 | .0008 |
| Thành phần chính $u_5$ | 0.00 | 0.0 | .0000 |
| | Tổng $T$ | = 1756.7 | 1.0000 |

Một "biểu đồ điểm vỡ (scree plot)" vẽ đồ thị các phân số $\sigma_i^2 / T$ đó đang giảm nhanh về 0. Trong một bài toán lớn hơn, bạn thường thấy sự sụt giảm nhanh chóng theo sau bởi một phần phẳng hơn ở dưới cùng (gần $\sigma_i^2 = 0$). Việc xác định vị trí điểm khuỷu tay (elbow) giữa hai phần đó (các thành phần chính - PC có ý nghĩa và không có ý nghĩa) là rất quan trọng.

Chúng ta cũng hướng tới việc hiểu từng thành phần chính. Các vectơ suy biến $u_i$ của $A$ đó là các vectơ riêng của $S$. Các phần tử trong những vectơ đó là các *"trọng số (loadings)".* Đây là $u_1$ tới $u_5$ đối với ví dụ đường cong lợi suất này (với $Su_5 = 0$).

| | $u_1$ | $u_2$ | $u_3$ | $u_4$ | $u_5$ |
|---|---|---|---|---|---|
| 3MO | 0.383 | 0.529 | -0.478 | 0.060 | 0.084 |
| 6MO | 0.336 | 0.436 | -0.046 | 0.210 | -0.263 |
| 1YR | 0.358 | 0.263 | 0.225 | -0.491 | 0.237 |
| 2YR | 0.352 | -0.028 | 0.460 | 0.096 | 0.242 |
| 3YR | 0.371 | -0.131 | 0.430 | 0.258 | -0.555 |
| 5YR | 0.349 | -0.293 | 0.117 | -0.188 | 0.446 |
| 7YR | 0.323 | -0.365 | -0.228 | 0.459 | 0.081 |
| 10YR | 0.297 | -0.378 | -0.351 | -0.579 | -0.470 |
| 20YR | 0.184 | -0.280 | -0.361 | 0.227 | 0.268 |

Năm $u$ đó là trực chuẩn. Chúng cung cấp các cơ sở cho không gian cột 4 chiều của $A$ và không gian không 1 chiều của $A^T$. Chúng có ý nghĩa tài chính gì?

$u_1$ đo lường trung bình có trọng số của các thay đổi hàng ngày trong 9 lợi suất
$u_2$ đo lường sự thay đổi hàng ngày của mức chênh lệch lợi suất (yield spread) giữa trái phiếu dài hạn và ngắn hạn
$u_3$ cho thấy các thay đổi hàng ngày của độ cong (curvature) (trái phiếu ngắn hạn và dài hạn so với trung hạn)

Những đồ thị này cho thấy chín trọng số trên $u_1, u_2, u_3$ ở trên, từ 3 tháng đến 20 năm.

![](images/_page_399_Picture_7.jpeg)

![](images/_page_399_Figure_8.jpeg)

Đầu ra từ một đoạn mã (code) điển hình (được viết bằng R) sẽ bao gồm thêm hai bảng nữa - những bảng này sẽ được đưa lên trang web của cuốn sách. Một bảng sẽ cho thấy các vectơ suy biến *phải* $v_i$ của $A$. Đây là các vectơ riêng của $A^T A$. Chúng tỷ lệ với các vectơ $A^T u$. Chúng có 5 thành phần và cho thấy sự chuyển động của các lợi suất và các chênh lệch ngắn hạn-dài hạn trong tuần.

Phương sai tổng $T = 1756.7$ (vết của $S$, $\sigma_1^2 + \sigma_2^2 + \sigma_3^2 + \sigma_4^2$) cũng là tổng của các phần tử trên đường chéo của $S$. Đó là các phương sai mẫu của các hàng trong $A$. Chúng đây: $s_1^2 + \dots + s_9^2 = 313.3 + 225.8 + 199.5 + 172.3 + 195.8 + 196.8 + 193.7 + 178.7 + 80.8 = 1756.7$. Mỗi $s_i^2$ đều nhỏ hơn $\sigma_1^2$. Và $1756.7$ cũng là vết của $A^T A / (n - 1)$: các phương sai cột.

Lưu ý rằng Phần 7.3 về PCA này đang làm việc với các *hàng* đã được lấy trung tâm trong $A$. Trong một số ứng dụng (như tài chính), ma trận thường được chuyển vị và các *cột* được lấy trung tâm. Khi đó ma trận hiệp phương sai mẫu $S$ sử dụng $A^T A$, và các $v$ là các thành phần chính quan trọng hơn. Đại số tuyến tính với các diễn giải thực tế cho chúng ta biết rất nhiều điều.

# **Tập bài tập 7.3 (Problem Set 7.3)**

**1** Giả sử $A_0$ chứa 2 phép đo này của 5 mẫu:

$$A_0 = \begin{bmatrix} 5 & 4 & 3 & 2 & 1 \\ -1 & 1 & 0 & 1 & -1 \end{bmatrix}$$

Tìm giá trị trung bình của mỗi hàng và trừ đi nó để tạo ra ma trận đã lấy trung tâm $A$. Tính ma trận hiệp phương sai mẫu $S = AA^T / (n - 1)$ và tìm các trị riêng $\lambda_1$ và $\lambda_2$ của nó. Đường thẳng nào đi qua gốc tọa độ gần nhất với 5 mẫu trong các cột của $A$?

**2** Thực hiện các bước của Bài 1 cho ma trận $A_0$ có kích thước 2 x 6 này:

$$A_0 = \begin{bmatrix} 1 & 0 & 1 & 0 & 1 & 0 \\ 1 & 2 & 3 & 3 & 2 & 1 \end{bmatrix}$$

**3** Các phương sai mẫu $s_1^2, s_2^2$ và hiệp phương sai mẫu $s_{12}$ là các phần tử của $S$. $S$ là gì (sau khi trừ đi các giá trị trung bình) khi $A_0 = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$? $\sigma_1$ là gì?

**4** Từ các vectơ riêng của $S = AA^T$, tìm đường thẳng (hướng $u_1$ qua điểm trung tâm) và sau đó là mặt phẳng (các hướng $u_1, u_2$) gần nhất với bốn điểm này trong không gian ba chiều

$$A = \begin{bmatrix} 1 & -1 & 0 & 0 \\ 0 & 0 & 2 & -2 \\ 1 & 1 & -1 & -1 \end{bmatrix}.$$

**5** Từ ma trận hiệp phương sai mẫu $S$ này, tìm ma trận tương quan $DSD$ với các số 1 dọc theo đường chéo chính của nó. $D$ là một ma trận đường chéo dương tạo ra các số 1 đó.

$$S = \begin{bmatrix} 4 & 2 & 0 \\ 2 & 4 & 1 \\ 0 & 1 & 1 \end{bmatrix}$$

**6** Chọn ma trận đường chéo $D$ tạo ra $DSD$ và tìm các hệ số tương quan $c_{ij}$:

$$S = \begin{bmatrix} s_1^2 & s_{12} & s_{13} \\ s_{12} & s_2^2 & s_{23} \\ s_{13} & s_{23} & s_3^2 \end{bmatrix} \quad DSD = \begin{bmatrix} 1 & c_{12} & c_{13} \\ c_{12} & 1 & c_{23} \\ c_{13} & c_{23} & 1 \end{bmatrix}.$$

**7** Giả sử $A_0$ là một ma trận kích thước 5 x 10 với điểm trung bình của 5 khóa học trong 10 năm. Bạn sẽ tạo ra ma trận đã lấy trung tâm $A$ và ma trận hiệp phương sai mẫu $S$ như thế nào? Khi bạn tìm được vectơ riêng hàng đầu của $S$, nó cho bạn biết điều gì?

# **7.4 Hình học của SVD (The Geometry of the SVD)**

**1** Một ma trận vuông điển hình $A = U \Sigma V^T$ được phân tích thành (phép quay) (phép co giãn) (phép quay). **2** Hình học cho thấy cách $A$ biến đổi các vectơ $x$ trên một đường tròn thành các vectơ $Ax$ trên một hình elip. **3 Chuẩn (norm)** của $A$ là $\|A\| = \sigma_1$. Giá trị suy biến này là hệ số tăng trưởng cực đại của nó $\|Ax\| / \|x\|$. **4 Phân tích cực (Polar decomposition)** phân tích $A$ thành $QS$: phép quay $Q = UV^T$ nhân với phép co giãn $S = V \Sigma V^T$. **5 Nghịch đảo giả (pseudoinverse)** $A^+ = V \Sigma^+ U^T$ đưa $Ax$ trong không gian cột trở lại $x$ trong không gian hàng.

SVD tách một ma trận thành ba bước: (**trực giao**) x (**đường chéo**) x (**trực giao**). Các từ ngữ thông thường có thể diễn đạt hình học đằng sau nó: (**phép quay**) x (**phép co giãn**) x (**phép quay**). $U \Sigma V^T x$ bắt đầu bằng phép quay đối với $V^T x$. Sau đó $\Sigma$ co giãn vectơ đó thành $\Sigma V^T x$, và $U$ quay nó thành $Ax = U \Sigma V^T x$. Đây là hình ảnh.

![](images/_page_401_Diagram_5.jpeg)

![](images/_page_401_Picture_6.jpeg)

Hình 7.5: $U$ và $V$ là các phép quay và có thể có phép phản xạ. $\Sigma$ co giãn hình tròn thành hình elip.

Phải thừa nhận rằng, hình ảnh này áp dụng cho một ma trận 2 x 2. Và không phải mọi ma trận 2 x 2, bởi vì $U$ và $V$ đã không cho phép một phép phản xạ - cả ba ma trận đều có định thức $> 0$. $A$ này sẽ phải có thể nghịch đảo bởi vì cả ba bước đều được hiển thị là có thể nghịch đảo:

$$\begin{bmatrix} a & b \\ c & d \end{bmatrix} = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} \sigma_1 & 0 \\ 0 & \sigma_2 \end{bmatrix} \begin{bmatrix} \cos \phi & \sin \phi \\ -\sin \phi & \cos \phi \end{bmatrix} = U \Sigma V^T. \quad (1)$$

Bốn con số $a, b, c, d$ trong ma trận $A$ dẫn đến bốn con số $\theta, \sigma_1, \sigma_2, \phi$ trong SVD của nó.

Hình ảnh này sẽ dẫn chúng ta tới ba ý tưởng gọn gàng trong đại số ma trận:

**1 Chuẩn (norm)** $\|A\|$ **của một ma trận - hệ số tăng trưởng cực đại của nó.** **2 Phân tích cực** $A = QS$ - $Q$ trực giao nhân với $S$ xác định dương. **3 Nghịch đảo giả** $A^+$ - nghịch đảo tốt nhất khi ma trận $A$ không thể nghịch đảo.

#### **Chuẩn của một Ma trận (The Norm of a Matrix)**

**Nếu** tôi chọn một con số quan trọng nhất trong hình ảnh, thì đó là $\sigma_1$. Con số đó là *hệ số tăng trưởng cực đại của bất kỳ vectơ $x$ nào.* **Nếu** bạn đi theo vectơ $v_1$ ở bên trái, bạn thấy nó quay tới $(1, 0)$ và co giãn thành $(\sigma_1, 0)$ và cuối cùng quay tới $\sigma_1 u_1$. Câu lệnh $Av_1 = \sigma_1 u_1$ chính xác là phương trình SVD. Giá trị suy biến lớn nhất $\sigma_1$ này là *"chuẩn"* của ma trận $A$.

| Chuẩn $\|A\|$ là tỷ số lớn nhất $\frac{\|Ax\|}{\|x\|}$ | $\|A\| = \max_{x \neq 0} \frac{\|Ax\|}{\|x\|} = \sigma_1$ | (2) |
|--------------------------------------------------------------|-----------------------------------------------------------|-----|

MATLAB sử dụng `norm(x)` cho độ dài vectơ và cùng từ ngữ đó `norm(A)` cho các chuẩn ma trận. Các ký hiệu toán học có dấu gạch dọc kép: $\|x\|$ và $\|A\|$. Ở đây $\|x\|$ có nghĩa là độ dài tiêu chuẩn của một vectơ với $\|x\|^2 = |x_1|^2 + \dots + |x_n|^2$. Chuẩn ma trận xuất phát từ chuẩn vectơ này khi $x = v_1$ và $Ax = \sigma_1 u_1$ và $\|Ax\| / \|x\| = \sigma_1 = \text{tỷ số lớn nhất} = \|A\|$.

Hai tính chất có giá trị của con số `norm(A)` đó xuất phát trực tiếp từ định nghĩa của nó:

| Bất đẳng thức tam giác | $\|A + B\| \leq \|A\| + \|B\|$ | Bất đẳng thức tích | $\|AB\| \leq \|A\| \|B\|$ | (3) |
|---------------------|--------------------------------|--------------------|---------------------------|-----|

Định nghĩa (2) cho biết rằng $\|Ax\| \leq \|A\| \|x\|$ đối với mọi vectơ $x$. Đó là điều mà chúng ta biết! Khi đó bất đẳng thức tam giác đối với các vectơ dẫn đến bất đẳng thức tam giác đối với các ma trận:

| Đối với các vectơ | $\|(A + B)x\| \leq \|Ax\| + \|Bx\| \leq \|A\| \|x\| + \|B\| \|x\|$ |
|-------------|--------------------------------------------------------------------|

Chia điều này cho $\|x\|$. Lấy giá trị cực đại trên toàn bộ các $x$. Khi đó $\|A+ B\| \leq \|A\| + \|B\|.$

Bất đẳng thức tích đến một cách nhanh chóng từ $\|AB x\| \leq \|A\| \|Bx\| \leq \|A\| \|B\| \|x\|$. Lại một lần nữa chia cho $\|x\|$. Lấy giá trị cực đại trên toàn bộ các $x$. Kết quả là $\|AB\| \leq \|A\| \|B\|.$

**Ví dụ 1** Một ma trận hạng một $A = uv^T$ là dạng cơ bản nhất mà chúng ta có thể có được. Nó có một trị riêng khác 0 $\lambda_1$ và một giá trị suy biến khác 0 $\sigma_1$. Gọn gàng thay, vectơ riêng của nó là $u$ và các vectơ suy biến (trái và phải) của nó là $u$ và $v$.

| Vectơ riêng | $Au = (uv^T)u = u(v^Tu) = \lambda_1 u$ | Nên $\lambda_1 = v^Tu$ |
|-------------|----------------------------------------|-----------------------|

**Vectơ suy biến** $A^T Av = (vu^T)(uv^T)v = v(u^Tu)(v^Tv) = \sigma_1^2 v$. Nên $\sigma_1 = \|u\| \|v\|$. Điều này làm cho bạn cảm thấy hài lòng khi $|\lambda_1| \leq \sigma_1$ chính xác là bất đẳng thức Schwarz $|v^T u| \leq \|u\| \|v\|$.

*Làm thế nào chúng ta biết rằng* $|\lambda_1| \leq \sigma_1$? Vectơ riêng cho $Ax = \lambda_1 x$ sẽ cho tỷ số $\|Ax\| / \|x\| = \|\lambda_1 x\| / \|x\|$ là bằng $|\lambda_1|$. Tỷ số lớn nhất $\sigma_1$ không thể nhỏ hơn $|\lambda_1|$.

Liệu có đúng là $|\lambda_2| \leq \sigma_2$ không? **Không.** Điều đó hoàn toàn sai. Thực tế, một ma trận 2 x 2 sẽ có $|\det A| = |\lambda_1 \lambda_2| = \sigma_1 \sigma_2$. Trong trường hợp này, $|\lambda_1| \leq \sigma_1$ sẽ buộc $|\lambda_2| \geq \sigma_2$.

**Ma trận hạng $k$ gần nhất với $A$ là $A_k = \sigma_1 u_1 v_1^T + \dots + \sigma_k u_k v_k^T$**

Đây là thực tế then chốt trong phép xấp xỉ ma trận: Định lý Eckart-Young-Mirsky nói rằng

$$\|A - B\| \geq \|A - A_k\| = \sigma_{k+1} \text{ đối với mọi ma trận } B \text{ có hạng } k.$$

Đối với tôi, điều này hoàn thành Định lý Cơ bản của Đại số Tuyến tính. Các $v$ và các $u$ cung cấp các cơ sở trực chuẩn cho bốn không gian con cơ bản, và $k$ cái $v$ và $u$ và $\sigma$ đầu tiên cung cấp phép xấp xỉ ma trận tốt nhất cho $A$.

### **Phân tích Cực (Polar Decomposition) $A = QS$**

**Mọi số phức $x + iy$ đều có dạng cực $r e^{i\theta}$.** Một con số $r \geq 0$ nhân với một con số $e^{i\theta}$ trên vòng tròn đơn vị. Chúng ta có $x + iy = r \cos \theta + ir \sin \theta = r(\cos \theta + i \sin \theta) = r e^{i\theta}$. Hãy nghĩ về những con số này như các ma trận 1 x 1. Khi đó $e^{i\theta}$ là một *ma trận trực giao* $Q$ và $r \geq 0$ là một *ma trận nửa xác định dương* (gọi nó là $S$). *Phân tích cực* mở rộng cùng ý tưởng đó sang các ma trận $n \times n$: trực giao nhân với nửa xác định dương, $A = QS$.

Mọi ma trận vuông thực đều có thể được phân tích thành $A = QS$, trong đó $Q$ *trực giao* và $S$ *đối xứng nửa xác định dương*. Nếu $A$ có thể nghịch đảo, $S$ xác định dương.

Để chứng minh, chúng ta chỉ cần chèn $V^T V = I$ vào giữa SVD:

$$\text{Phân tích cực} \quad A = U \Sigma V^T = (UV^T)(V \Sigma V^T) = (Q)(S). \quad (4)$$

Nhân tử đầu tiên $UV^T$ là $Q$. Tích của các ma trận trực giao là trực giao. Nhân tử thứ hai $V \Sigma V^T$ là $S$. Nó là nửa xác định dương bởi vì các trị riêng của nó nằm trong $\Sigma$.

Nếu $A$ có thể nghịch đảo thì $\Sigma$ và $S$ cũng có thể nghịch đảo. **$S$ là căn bậc hai đối xứng xác định dương của $A^T A$**, bởi vì $S^2 = V \Sigma^2 V^T = A^T A$. Do đó các trị riêng của $S$ chính là các giá trị suy biến của $A$. Các vectơ riêng của $S$ chính là các vectơ suy biến $v$ của $A$.

Cũng có một phân tích cực $A = KQ$ theo trình tự ngược lại. $Q$ vẫn như cũ nhưng bây giờ $K = U \Sigma U^T$. Khi đó $K$ là căn bậc hai đối xứng xác định dương của $AA^T$.

**Ví dụ 2** Ví dụ SVD trong Phần 7.2 là $A = \begin{bmatrix} 3 & 0 \\ 4 & 5 \end{bmatrix} = U \Sigma V^T$. Tìm các nhân tử $Q$ và $S$ (phép quay và phép co giãn) trong phân tích cực $A = QS$.

**Lời giải** Tôi sẽ chỉ cần sao chép các ma trận $U$ và $\Sigma$ và $V$ từ Phần 7.2:


$$Q = UV^T = \frac{1}{\sqrt{20}} \begin{bmatrix} 1 & -3 \\ 3 & 1 \end{bmatrix} \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} = \frac{1}{\sqrt{20}} \begin{bmatrix} 4 & -2 \\ 2 & 4 \end{bmatrix} = \frac{1}{\sqrt{5}} \begin{bmatrix} 2 & -1 \\ 1 & 2 \end{bmatrix}$$

$$S = V\Sigma V^T = \frac{\sqrt{5}}{2} \begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix} = \sqrt{5} \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}. \text{ Khi đó } A = QS.$$

Trong cơ học, phân tích cực tách *phép quay* (trong $Q$) khỏi *phép co giãn* (trong $S$). Các trị riêng của $S$ cung cấp các hệ số co giãn giống như trong Hình 7.5. Các vectơ riêng của $S$ cung cấp các hướng co giãn (các trục chính của hình elip). Ma trận trực giao $Q$ bao gồm cả hai phép quay $U$ và $V^T$.

Đây là một sự thật về các phép quay. $Q = UV^T$ là **ma trận trực giao gần nhất** đối với $A$. $Q$ này làm cho chuẩn $\|Q - A\|$ càng nhỏ càng tốt. Điều đó tương ứng với sự thật là $e^{i\theta}$ là con số trên vòng tròn đơn vị gần nhất với $re^{i\theta}$.

SVD cho chúng ta biết một sự thật thậm chí còn quan trọng hơn về các ma trận suy biến (singular matrices) gần nhất:

**Ma trận suy biến gần nhất $A_0$ đối với $A$ đến bằng cách thay đổi giá trị $\sigma_{\min}$ nhỏ nhất thành 0.**

Vì vậy $\sigma_{\min}$ đang đo khoảng cách từ $A$ tới trạng thái suy biến. Đối với ma trận trong Ví dụ 2, khoảng cách đó là $\sigma_{\min} = \sqrt{5}$. Nếu tôi thay đổi $\sigma_{\min}$ thành 0, điều này sẽ loại bỏ phần cuối cùng (nhỏ nhất) trong $A = \sigma_1 u_1 v_1^T + \sigma_2 u_2 v_2^T$. Khi đó chỉ có ma trận hạng một (suy biến!) $\sigma_1 u_1 v_1^T$ sẽ bị bỏ lại: gần nhất với $A$. Sự thay đổi nhỏ nhất đã có chuẩn $\sigma_2 = \sqrt{5}$ (*nhỏ hơn 3*).

Trong thực hành tính toán, chúng ta thường loại bỏ một $\sigma$ rất nhỏ. Làm việc với các ma trận suy biến thì tốt hơn là đến quá gần số 0 mà không nhận ra.

**Nghịch đảo giả (The Pseudoinverse) $A^+$**

Bằng cách chọn các cơ sở tốt, $A$ nhân với $v_i$ trong không gian hàng để cho ra $\sigma_i u_i$ trong không gian cột. $A^{-1}$ phải thực hiện điều ngược lại! Nếu $A v = \sigma u$ thì $A^{-1} u = v/\sigma$. Các giá trị suy biến của $A^{-1}$ là $1/\sigma$, giống hệt như các trị riêng của $A^{-1}$ là $1/\lambda$. Các cơ sở bị đảo ngược. Các $u$ nằm trong không gian hàng của $A^{-1}$, các $v$ nằm trong không gian cột.

Cho đến thời điểm này chúng ta hẳn đã thêm "nếu $A^{-1}$ tồn tại". Bây giờ chúng ta không làm thế nữa. Một ma trận mà nhân với $u_i$ để tạo ra $v_i/\sigma_i$ có tồn tại. Nó là nghịch đảo giả $A^+$:

$$\text{Nghịch đảo giả của } A = A^+ = V\Sigma^+U^T = \begin{bmatrix} v_1 & \cdots & v_r & \cdots & v_n \end{bmatrix} \begin{bmatrix} \sigma_1^{-1} & & & \\ & \ddots & & \\ & & \sigma_r^{-1} & \\ & & & 0 \end{bmatrix} \begin{bmatrix} u_1 & \cdots & u_r & \cdots & u_m \end{bmatrix}^T$$

*Nghịch đảo giả* $A^+$ là một ma trận $n \times m$. Nếu $A^{-1}$ tồn tại (chúng ta lại nói lại điều đó), thì $A^+$ giống hệt như $A^{-1}$. Trong trường hợp đó $m = n = r$ và chúng ta đang nghịch đảo $U \Sigma V^T$ để lấy $V \Sigma^{-1} U^T$. Ký hiệu mới $A^+$ là cần thiết khi $r < m$ hoặc $r < n$. Khi đó $A$ không có nghịch đảo hai phía, nhưng nó có một *nghịch đảo giả* $A^+$ với cùng hạng $r$ đó:

$$A^+ u_i = \frac{1}{\sigma_i} v_i \quad \text{đối với } i \leq r \quad \text{và} \quad A^+ u_i = 0 \quad \text{đối với } i > r.$$

Các vectơ $u_1, \dots, u_r$ trong không gian cột của $A$ đi ngược lại về $v_1, \dots, v_r$ trong không gian hàng. Các vectơ khác $u_{r+1}, \dots, u_m$ nằm trong không gian không trái, và $A^+$ gửi chúng về 0. Khi chúng ta biết chuyện gì xảy ra với tất cả những vectơ cơ sở đó, chúng ta biết $A^+$.

Chú ý nghịch đảo giả của ma trận đường chéo $\Sigma$. Mỗi $\sigma$ trong $\Sigma$ được thay thế bằng $\sigma^{-1}$ trong $\Sigma^+$. Tích $\Sigma^+ \Sigma$ gần với ma trận đơn vị nhất mà chúng ta có thể đạt được. Nó là một ma trận chiếu, $\Sigma^+ \Sigma$ một phần là $I$ và phần còn lại là 0. Chúng ta có thể nghịch đảo các $\sigma$, nhưng chúng ta không thể làm gì với các hàng và cột số 0. Ví dụ này có $\sigma_1 = 2$ và $\sigma_2 = 3$:

$$\Sigma^+\Sigma = \begin{bmatrix} 1/2 & 0 & 0 \\ 0 & 1/3 & 0 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{bmatrix} = \begin{bmatrix} I & 0 \\ 0 & 0 \end{bmatrix}.$$

![](images/_page_405_Diagram_2.jpeg)

Hình 7.6: $Ax^+$ trong không gian cột trở về $A^+ Ax^+ = x^+$ trong không gian hàng.

**Cố gắng đạt được** 
$AA^{-1} = A^{-1}A = I$
$AA^+$ = ma trận chiếu lên không gian cột của $A$
$A^+ A$ = ma trận chiếu lên không gian hàng của $A$

**Ví dụ 3** Mọi ma trận hạng một đều là một cột nhân với một hàng. Với các vectơ đơn vị $u$ và $v$, đó là $A = \sigma_1 u v^T$. Nghịch đảo giả của nó là $A^+ = v u^T / \sigma_1$. Tích $AA^+$ là $uu^T$, hình chiếu lên đường thẳng đi qua $u$. Tích $A^+ A$ là $vv^T$.

**Ví dụ 4** Tìm nghịch đảo giả của $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$. Ma trận này không thể nghịch đảo. Hạng là 1. Giá trị suy biến duy nhất là $\sigma_1 = 2$. Giá trị đó được nghịch đảo thành $1/2$ trong $\Sigma^+$ (cũng có hạng 1).

$$A^+ = V\Sigma^+U^T = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} 1/2 & 0 \\ 0 & 0 \end{bmatrix} \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}^T = \frac{1}{4} \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}.$$

$A^+$ cũng có hạng 1. Không gian cột của nó luôn là không gian hàng của $A$.

### **Bình phương Tối thiểu với Các Cột Phụ thuộc (Least Squares with Dependent Columns)**

Ma trận $A$ với bốn số 1 đó đã xuất hiện ở Phần 4.3 về bình phương tối thiểu. Nó đã phá vỡ yêu cầu về các cột độc lập. Ma trận xuất hiện khi chúng ta thực hiện hai phép đo, cả hai tại thời điểm $t = 1$. Đường thẳng gần nhất đi giữa nửa chừng các phép đo 3 và 1, nhưng không có cách nào để quyết định về độ dốc của đường thẳng tốt nhất.

Trong ngôn ngữ ma trận, $A^T A$ bị suy biến. Phương trình $A^T A \widehat{x} = A^T b$ **có vô số nghiệm.** Nghịch đảo giả cho chúng ta một cách để chọn ra một "nghiệm tốt nhất" $x^+ = A^+ b$. Hãy để tôi lặp lại $Ax = b$ không thể giải được và $A^T A \widehat{x} = A^T b$ có vô số nghiệm:

| $Ax = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 3 \\ 1 \end{bmatrix} = b$ | $A^T A \widehat{x} = \begin{bmatrix} 2 & 2 \\ 2 & 2 \end{bmatrix} \begin{bmatrix} \widehat{x}_1 \\ \widehat{x}_2 \end{bmatrix} = \begin{bmatrix} 4 \\ 4 \end{bmatrix} = A^T b$ |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Bất kỳ vectơ $x = (1 + c, 1 - c)$ nào cũng sẽ giải được những phương trình chuẩn tắc (normal equations) $A^T A x = A^T b$ đó. Mục đích của nghịch đảo giả là chọn ra một nghiệm $x = x^+$.

$$x^+ = A^+ b = (1, 1)$$
là nghiệm ngắn nhất đối với $A^T A \widehat{x} = A^T b$ và $A \widehat{x} = p$.

Bạn có thể thấy rằng $x^+ = (1, 1)$ ngắn hơn bất kỳ nghiệm $x = (1 + c, 1 - c)$ nào khác. Bình phương độ dài của $x$ là $(1 + c)^2 + (1 - c)^2 = 2 + 2c^2$. Lựa chọn ngắn nhất là $c = 0$. Điều đó mang lại nghiệm $x^+ = (1, 1)$ trong không gian hàng của $A$.

Hình học cho chúng ta biết những gì $A^+$ nên làm: Đưa không gian cột của $A$ trở lại không gian hàng. Cả hai không gian đều có chiều là $r$. Khử đi vectơ sai số $e$ trong không gian không trái.

Nghịch đảo giả $A^+$ và nghiệm tốt nhất $x^+$ này là điều cốt yếu trong thống kê, bởi vì các thí nghiệm thường có một ma trận với các cột phụ thuộc cũng như các hàng phụ thuộc.

#### **• ÔN TẬP CÁC Ý TƯỞNG THEN CHỐT • (REVIEW OF THE KEY IDEAS)**

- **1.** Hình elip của các vectơ $Ax$ có các trục dọc theo các vectơ suy biến $u_i$.
- **2.** Chuẩn ma trận $\|A\| = \sigma_1$ xuất phát từ độ dài vectơ: Cực đại hóa $\|Ax\| / \|x\|$.
- **3.** Ma trận có thể nghịch đảo = (ma trận trực giao) (ma trận xác định dương): $A = QS$.
- **4.** Mọi $A = U \Sigma V^T$ đều có một nghịch đảo giả $A^+ = V \Sigma^+ U^T$ giúp gửi $N(A^T)$ tới $0$.

#### **• CÁC VÍ DỤ CÓ LỜI GIẢI • (WORKED EXAMPLES)**

**7.4 A** Nếu $A$ có hạng $n$ (hạng cột đầy đủ - full column rank) thì nó có một **nghịch đảo trái (left inverse)** $L = (A^T A)^{-1} A^T$. Ma trận $L$ này mang lại $LA = I$. Hãy giải thích tại sao nghịch đảo giả là $A^+ = L$ trong trường hợp này.

Nếu $A$ có hạng $m$ (hạng hàng đầy đủ - full row rank) thì nó có một **nghịch đảo phải (right inverse)** $R = A^T(AA^T)^{-1}$. Ma trận $R$ này mang lại $AR = I$. Hãy giải thích tại sao nghịch đảo giả là $A^+ = R$ trong trường hợp này.

Tìm $L$ cho $A_1$ và tìm $R$ cho $A_2$. Tìm $A^+$ cho cả ba ma trận $A_1, A_2, A_3$:

| $A_1 = \begin{bmatrix} 2 \\ 2 \end{bmatrix}$ | $A_2 = \begin{bmatrix} 2 & 2 \end{bmatrix}$ | $A_3 = \begin{bmatrix} 2 & 2 \\ 1 & 1 \end{bmatrix}$ |
|----------------------------------------------|------------------------------------------------------|------------------------------------------------------|

**Lời giải** Nếu $A$ có các cột độc lập thì $A^T A$ có thể nghịch đảo - đây là điểm then chốt của Phần 4.2. Chắc chắn $L = (A^T A)^{-1} A^T$ nhân với $A$ sẽ cho ra $LA = I$: một nghịch đảo trái.

$AL = A(A^T A)^{-1} A^T$ là ma trận chiếu (Phần 4.2) lên không gian cột. Do đó $L$ đáp ứng các yêu cầu đối với $A^+$: $LA$ và $AL$ là các hình chiếu lên $C(A)$ và $C(A^T)$.

Nếu $A$ có hạng $m$ (hạng hàng đầy đủ) thì $AA^T$ có thể nghịch đảo. Chắc chắn $A$ nhân với $R = A^T(AA^T)^{-1}$ sẽ cho ra $AR = I$. Theo trình tự ngược lại, $RA = A^T(AA^T)^{-1} A$ là ma trận chiếu lên không gian hàng (không gian cột của $A^T$). Do đó $R$ bằng với nghịch đảo giả $A^+$.

Ví dụ $A_1$ có hạng cột đầy đủ (đối với $L$) và $A_2$ có hạng hàng đầy đủ (đối với $R$):

$$A_1^+ = (A_1^T A_1)^{-1} A_1^T = \frac{1}{8} \begin{bmatrix} 2 & 2 \end{bmatrix} \quad A_2^+ = A_2^T (A_2 A_2^T)^{-1} = \frac{1}{8} \begin{bmatrix} 2 \\ 2 \end{bmatrix}.$$

Chú ý $A_1^+ A_1 = [1]$ và $A_2 A_2^+ = [1]$. Nhưng $A_3$ không có nghịch đảo trái hay nghịch đảo phải. **Hạng của nó không đầy đủ. Nghịch đảo giả của nó đưa không gian cột của $A_3$ trở về không gian hàng.**

$$A_3^+ = \begin{bmatrix} 2 & 2 \\ 1 & 1 \end{bmatrix}^+ = \frac{v_1 u_1^T}{\sigma_1} = \frac{1}{10} \begin{bmatrix} 2 & 1 \\ 2 & 1 \end{bmatrix}.$$

## **Tập bài tập 7.4 (Problem Set 7.4)**

**Các bài tập 1–4 tính toán và sử dụng SVD của một ma trận cụ thể (không thể nghịch đảo).**

**1** (a) Tính $A^T A$ và các trị riêng của nó cùng với các vectơ riêng đơn vị $v_1$ và $v_2$. Tìm $\sigma_1$.

$$\text{Ma trận hạng một} \quad A = \begin{bmatrix} 1 & 2 \\ 3 & 6 \end{bmatrix}$$

(b) Tính $AA^T$ và các trị riêng của nó cùng với các vectơ riêng đơn vị $u_1$ và $u_2$.

(c) Xác minh rằng $Av_1 = \sigma_1 u_1$. Đưa các con số vào $A = U \Sigma V^T$ (đây là SVD).

**2** (a) Từ các $u$ và các $v$ trong Bài 1, hãy viết ra các cơ sở trực chuẩn cho bốn không gian con cơ bản của ma trận $A$ này.

(b) Mô tả tất cả các ma trận có cùng bốn không gian con đó. Các bội số của $A$?

**3** Từ $U$, $V$, và $\Sigma$ trong Bài 1 hãy tìm ma trận trực giao $Q = UV^T$ và ma trận đối xứng $S = V \Sigma V^T$. Xác minh phân tích cực $A = QS$. $S$ này chỉ là nửa xác định vì \_\_\_\_\_. Kiểm tra $S^2 = A$.

**4** Tính nghịch đảo giả $A^+ = V \Sigma^+ U^T$. Ma trận đường chéo $\Sigma^+$ chứa $1/\sigma_1$. Đổi tên bốn không gian con (cho $A$) trong Hình 7.6 thành bốn không gian con cho $A^+$. Tính các hình chiếu $A^+ A$ và $AA^+$ lên không gian hàng và không gian cột của $A$.

### **Các bài tập 5-9 nói về SVD của một ma trận có thể nghịch đảo.**

**5** Tính $A^T A$ và các trị riêng của nó cùng với các vectơ riêng đơn vị $v_1$ và $v_2$. Các giá trị suy biến $\sigma_1$ và $\sigma_2$ đối với ma trận $A$ này là gì?

$$A = \begin{bmatrix} 3 & 3 \\ -1 & 1 \end{bmatrix}$$

**6** $AA^T$ có cùng các trị riêng $\sigma_1^2$ và $\sigma_2^2$ giống như $A^T A$. Tìm các vectơ riêng đơn vị $u_1$ và $u_2$. Đưa các con số vào SVD:

$$A = \begin{bmatrix} 3 & 3 \\ -1 & 1 \end{bmatrix} = \begin{bmatrix} u_1 & u_2 \end{bmatrix} \begin{bmatrix} \sigma_1 & 0 \\ 0 & \sigma_2 \end{bmatrix} \begin{bmatrix} v_1 & v_2 \end{bmatrix}^T$$

**7** Trong Bài 6, nhân các cột với các hàng để cho thấy rằng $A = \sigma_1 u_1 v_1^T + \sigma_2 u_2 v_2^T$. Chứng minh từ $A = U \Sigma V^T$ rằng mọi ma trận hạng $r$ đều là tổng của $r$ ma trận hạng một. 

**8** Từ $U$, $V$, và $\Sigma$ hãy tìm ma trận trực giao $Q = UV^T$ và ma trận đối xứng $K = U \Sigma U^T$. Xác minh phân tích cực theo trình tự ngược lại $A = K Q$. 

**9** Nghịch đảo giả của $A$ này giống hệt như \_\_ bởi vì \_\_.

# **Các bài tập 10-11 tính toán và sử dụng SVD của một ma trận chữ nhật 1 x 3.**

**10** Tính $A^T A$ và $AA^T$ và các trị riêng cùng các vectơ riêng đơn vị của chúng khi ma trận là $A = \begin{bmatrix} 3 & 4 & 0 \end{bmatrix}$. Các giá trị suy biến của $A$ là gì? 

**11** Đưa các con số vào phân tích giá trị suy biến của $A$:

$$A = \begin{bmatrix} 3 & 4 & 0 \end{bmatrix} = \begin{bmatrix} u_1 \end{bmatrix} \begin{bmatrix} \sigma_1 & 0 & 0 \end{bmatrix} \begin{bmatrix} v_1 & v_2 & v_3 \end{bmatrix}^T$$


Đưa các con số vào nghịch đảo giả $V \Sigma^+ U^T$ của $A$. *Tính* $AA^+$ *và* $A^+A$:

| Nghịch đảo giả | $A^+ = \begin{bmatrix} v_1 & v_2 & v_3 \end{bmatrix} \begin{bmatrix} 1/\sigma_1 \\ 0 \\ 0 \end{bmatrix} \begin{bmatrix} u_1 \end{bmatrix}^T.$ |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**12** Ma trận $2 \times 3$ duy nhất không có phần tử cơ sở (pivots) và không có giá trị suy biến nào là ma trận nào? $\Sigma$ cho ma trận đó là gì? $A^+$ là ma trận 0, nhưng hình dáng (shape) của nó là gì? 

**13** Nếu $\det A= 0$ tại sao $\det A^+ = 0$? Nếu $A$ có hạng $r$, tại sao $A^+$ có hạng $r$? 

**14** Đối với các vectơ trong vòng tròn đơn vị $\|x\| = 1$, các vectơ $y = Ax$ trong hình elip sẽ có $\|A^{-1}y\| = 1$. Hình elip này có các trục dọc theo các vectơ suy biến với độ dài = $\sigma_1, \dots, \sigma_r$ (như trong Hình 7.5). Khai triển $\|A^{-1}y\|^2 = 1$ cho $A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$.

Các bài tập 15-18 nêu bật các tính chất chính của $A^+$ và $x^+ = A^+ b$.

**15** Tất cả các ma trận trong bài toán này đều có hạng một. Vectơ $b$ là $(b_1, b_2)$,

| $A = \begin{bmatrix} 2 & 2 \\ 1 & 1 \end{bmatrix}$ | $AA^T = \begin{bmatrix} 8 & 4 \\ 4 & 2 \end{bmatrix}$ | $A^T A = \begin{bmatrix} 5 & 5 \\ 5 & 5 \end{bmatrix}$ | $A^+ = \frac{1}{10} \begin{bmatrix} 2 & 1 \\ 2 & 1 \end{bmatrix}$ |
|----------------------------------------------------|-------------------------------------------------------|--------------------------------------------------------|------------------------------------------------------|

- (a) Phương trình $A^T Ax = A^T b$ có nhiều nghiệm vì $A^T A$ là \_\_.
- (b) Xác minh rằng $x^+ = A^+ b = \frac{1}{10}(2b_1+b_2, 2b_1+b_2)$ giải được $A^T Ax^+ = A^T b$.
- (c) Cộng $(1, -1)$ vào $x^+$ đó để có được một nghiệm khác cho $A^T Ax = A^T b$. Chứng minh rằng $\|x\|^2 = \|x^+\|^2 + 2$, và $x^+$ là ngắn nhất. 

**16** Vectơ $x^+ = A^+ b$ là nghiệm ngắn nhất có thể có cho $A^T Ax= A^T b$. Lý do: Hiệu số $x - x^+$ nằm trong không gian không của $A^T A$. Đây cũng là không gian không của $A$, trực giao với $x^+$. Hãy giải thích làm thế nào để suy ra $\|x\|^2 = \|x^+\|^2 + \|x - x^+\|^2$. 

**17** Mọi $b$ trong $\mathbb{R}^m$ là $p + e$. Đây là phần không gian cột cộng với phần không gian không trái. Mọi $x$ trong $\mathbb{R}^n$ là $x^+ + x_n$. Đây là phần không gian hàng cộng với phần không gian không. Khi đó $AA^+ e =$

| $A^+ p =$ | $A^+ e =$ | $A^+ Ax^+ =$ | $A^+ Ax_n =$ |
|-----------|-----------|--------------|--------------|

**18** Tìm $A^+$ và $A^+ A$ và $AA^+$ và $x^+$ cho ma trận $A = U\Sigma V^T$ này và những vectơ $b$ này:

| $A = \begin{bmatrix} 3 \\ 4 \end{bmatrix} = \begin{bmatrix} .6 & -.8 \\ .8 & .6 \end{bmatrix} \begin{bmatrix} 5 \\ 0 \end{bmatrix} [1]$ | $b = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$ và $b = \begin{bmatrix} -4 \\ 3 \end{bmatrix}$ . |
|-----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|

**19** Một ma trận $2 \times 2$ tổng quát $A$ được xác định bởi bốn con số. Nếu là ma trận tam giác, nó được xác định bởi ba con số. Nếu là đường chéo, bởi hai con số. Nếu là một phép quay, bởi một con số. Nếu là một vectơ riêng đơn vị, cũng bởi một con số. Hãy kiểm tra xem tổng số đếm có phải là bốn cho mỗi cách phân tích của $A$ không:

**Bốn con số trong** $LU$, $LDU$, $QR$, $U\Sigma V^T$, $X\Lambda X^{-1}$.

**20** Tiếp theo Bài 18, kiểm tra xem $LDL^T$ và $Q\Lambda Q^T$ có được xác định bởi ba con số không. Điều này là đúng vì lúc này ma trận là \_\_. 

**21** Từ $A$ và $A^+$ hãy chứng tỏ rằng $A^+ A$ là đúng và $(A^+ A)^2 = A^+ A =$ ma trận chiếu. 

**22** Mỗi cặp vectơ suy biến $v$ và $u$ có $Av = \sigma u$ và $A^T u = \sigma v$. Hãy chỉ ra rằng vectơ ghép $\begin{bmatrix} u \\ v \end{bmatrix}$ là một vectơ riêng của ma trận khối đối xứng $M = \begin{bmatrix} 0 & A \\ A^T & 0 \end{bmatrix}$. SVD của $A$ tương đương với việc chéo hóa ma trận đối xứng $M$ đó.

| $A = \sum_1^r \sigma_i u_i v_i^T$ | $A^+ = \sum_1^r \frac{v_i u_i^T}{\sigma_i}$ | $A^+ A = \sum_1^r v_i v_i^T$ | $AA^+ = \sum_1^r u_i u_i^T$ |
|-----------------------------------|---------------------------------------------|------------------------------|-----------------------------|


