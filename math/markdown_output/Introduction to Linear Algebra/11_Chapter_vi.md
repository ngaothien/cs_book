# **Chương 11**

# **Đại số Tuyến tính Số (Numerical Linear Algebra)**

**1** Mục tiêu của đại số tuyến tính số là **tốc độ (speed)**, **độ chính xác (accuracy)** và **tính ổn định (stability)**: $n > 10^3$ hoặc $10^6$.
**2** Ma trận có thể đầy, thưa, dạng dải hoặc có cấu trúc: có các thuật toán đặc biệt cho từng loại.
**3** Độ chính xác của phép khử được kiểm soát bởi **số điều kiện (condition number)** $\|A\| \|A^{-1}\|$.
**4** Quá trình Gram-Schmidt thường được tính toán bằng cách sử dụng **phép phản xạ Householder (Householder reflections)** $H = I - 2uu^T$ để tìm $Q$.
**5** Trị riêng sử dụng **các phép lặp** $QR$: $A_0 = Q_0R_0 \rightarrow R_0Q_0 = A_1 = Q_1R_1 \rightarrow \dots \rightarrow A_n$.
**6** *Phép lặp $QR$ dịch chuyển (Shifted QR)* còn tốt hơn: Dịch chuyển thành $A_k - c_kI = Q_kR_k$, dịch chuyển ngược lại $A_{k+1} = R_kQ_k + c_kI$.
**7** Phép lặp $Sx_{k+1} = b - Tx_k$ giải $(S + T)x = b$ nếu tất cả các trị riêng của $S^{-1}T$ có $|\lambda| < 1$.
**8** Các phương pháp lặp thường sử dụng **các bộ tiền điều kiện (preconditioners)** $P$. Đổi $Ax = b$ thành $PAx = Pb$ với $PA \approx I$.
**9 Gradient liên hợp (Conjugate gradients)** và **GMRES** là các phương pháp Krylov; xem Trefethen-Bau (và các văn bản khác).

### **11.1 Phép khử Gauss trong Thực hành (Gaussian Elimination in Practice)**

Đại số tuyến tính số là một cuộc đấu tranh để có được các giải pháp nhanh chóng và đồng thời cũng phải chính xác. Chúng ta cần tính hiệu quả nhưng chúng ta phải tránh sự mất ổn định. Trong phép khử Gauss, sự tự do chính (luôn có sẵn) là *hoán đổi các phương trình.* Phần này giải thích khi nào nên hoán đổi các hàng vì lợi ích của tốc độ, và khi nào nên làm điều đó vì lợi ích của độ chính xác.

Chìa khóa của độ chính xác là tránh các con số lớn không cần thiết. Thông thường điều đó đòi hỏi chúng ta phải tránh các con số nhỏ! Một phần tử trục nhỏ thường có nghĩa là các hệ số nhân lớn (vì chúng ta chia cho phần tử trục). Một kế hoạch tốt là *"chọn phần tử trục cục bộ (partial pivoting)",* để chọn phần tử trục lớn nhất hiện có trong mỗi cột mới. Chúng ta sẽ xem lý do tại sao chiến lược chọn trục này được tích hợp vào các chương trình máy tính.

Các phép hoán đổi hàng khác được thực hiện để tiết kiệm các bước khử. Trên thực tế, hầu hết các ma trận lớn đều *thưa thớt (sparse)* - hầu hết các phần tử đều là số 0. Phép khử là nhanh nhất khi các phương trình được sắp xếp *để tạo ra một dải hẹp các số khác không.* Các số 0 bên trong dải sẽ bị "lấp đầy" trong quá trình khử - những số 0 đó bị phá hủy và không giúp tiết kiệm thời gian tính toán.

Phần 11.2 nói về sự mất ổn định không thể tránh khỏi. Nó được gắn vào trong vấn đề, và độ nhạy này được đo lường bằng *"số điều kiện".* Sau đó, Phần 11.3 mô tả cách giải $Ax = b$ **bằng các phép lặp (iterations).** Thay vì khử trực tiếp, máy tính sẽ giải một phương trình dễ hơn nhiều lần. Mỗi câu trả lời $x_k$ dẫn đến dự đoán tiếp theo $x_{k+1}$. Đối với các phép lặp tốt (**phương pháp gradient liên hợp** là cực kỳ tốt), các $x_k$ hội tụ nhanh về $x = A^{-1}b$.

## **Siêu máy tính Nhanh nhất (The Fastest Supercomputer)**

Một kỷ lục siêu máy tính mới đã được IBM và Los Alamos công bố vào ngày 20 tháng 5 năm 2008. Roadrunner là cỗ máy đầu tiên đạt được một triệu tỷ ($10^{15}$) phép tính dấu phẩy động mỗi giây: *một cỗ máy petaflop.* Tiêu chuẩn cho kỷ lục thế giới này là một hệ tuyến tính dày đặc có kích thước lớn $Ax = b$: tốc độ máy tính được kiểm tra bằng đại số tuyến tính.

Cỗ máy đó đã bị ngừng hoạt động vào năm 2013! Dự án TOP500 xếp hạng 500 hệ thống máy tính mạnh nhất thế giới. Khi tôi viết trang này vào tháng 10 năm 2015, bốn vị trí đầu tiên thuộc về NUDT ở Trung Quốc, Cray và IBM ở Mỹ, và Fujitsu ở Nhật Bản. Chúng đều sử dụng hệ điều hành dựa trên LINUX. Và tất cả các bộ xử lý vectơ đều đã rớt khỏi top 500.

Nhìn về phía trước, Summit dự kiến ​​sẽ chiếm vị trí đầu tiên với 150-300 petaflops. Tổng thống Obama vừa ra lệnh phát triển hệ thống exascale (1000 petaflops). Cho đến nay, chúng ta vẫn đang tuân theo Định luật Moore về việc tăng gấp đôi cứ sau 14 tháng.

Phần mềm LAPACK thực hiện phép khử với thao tác chọn trục cục bộ (partial pivoting). Khác biệt lớn nhất so với cuốn sách này là nó tổ chức các bước để sử dụng các ma trận con lớn và không bao giờ sử dụng các số đơn lẻ. Và các bộ xử lý đồ họa (GPU) hiện nay gần như là yêu cầu bắt buộc để đạt được thành công. Thị trường trò chơi điện tử làm lu mờ thị trường điện toán khoa học và đã dẫn đến sự tăng tốc đáng kinh ngạc của các con chip.

Trước BlueGene của IBM, vấn đề then chốt là phải đếm số lượng bộ xử lý lõi tứ tiêu chuẩn mà một cỗ máy petaflop cần đến: 32.000. Kiến trúc mới sử dụng ít năng lượng hơn nhiều, nhưng thiết kế kết hợp của nó có một cái giá phải trả: mã lệnh cần ba trình biên dịch riêng biệt và các hướng dẫn rõ ràng để di chuyển tất cả dữ liệu. Xin vui lòng xem bài viết xuất sắc trên tờ *SIAM News* **(siam.org,** tháng 7 năm 2008) và bản cập nhật trên **www.lanl.gov/roadrunner.**

Tư duy của chúng ta về các phép tính ma trận được phản ánh trong **BLAS** *(Basic Linear Algebra Subroutines - Các chương trình con Đại số Tuyến tính Cơ bản)* được tối ưu hóa cao độ. Chúng đi kèm với các cấp độ 1, 2 và 3:

**Cấp độ 1** Các tổ hợp tuyến tính của các vectơ $au + v$: Khối lượng công việc $O(n)$
**Cấp độ 2** Các phép nhân ma trận-vectơ $Au + v$: Khối lượng công việc $O(n^2)$
**Cấp độ 3** Các phép nhân ma trận-ma trận $AB + C$: Khối lượng công việc $O(n^3)$

Cấp độ 1 là một bước khử (nhân hàng $j$ với $l_{ij}$ và trừ đi từ hàng $i$). Cấp độ 2 có thể khử toàn bộ một cột cùng một lúc. Một bộ giải hiệu suất cao sẽ rất phong phú về BLAS Cấp độ 3 ($AB$ có $2n^3$ flops và $2n^2$ dữ liệu, một tỷ lệ làm việc/truyền thông tin tốt).

Chính quá trình *truyền dữ liệu* và *truy xuất bộ nhớ* làm hạn chế tốc độ của xử lý song song. Bộ đệm cache tốc độ cao giữa bộ nhớ chính và bộ tính toán dấu phẩy động phải được sử dụng hết công suất! Tốc độ tối đa đòi hỏi *phương pháp ma trận khối* đối với phép khử.

Sự thay đổi lớn, đang diễn ra hiện nay, là xử lý song song ở cấp độ chip.

## **Sai số làm tròn và Việc chọn phần tử trục cục bộ (Roundoff Error and Partial Pivoting)**

Cho đến nay, bất kỳ phần tử trục nào (tất nhiên là khác 0) đều được chấp nhận. Trong thực tế, một phần tử trục nhỏ là rất nguy hiểm. Một thảm họa có thể xảy ra khi cộng các con số có kích cỡ khác nhau. Máy tính giữ một số lượng chữ số có nghĩa cố định (giả sử ba số thập phân, đối với một máy rất yếu). Tổng $10,000 + 1$ được làm tròn thành $10,000$. Số "1" bị mất hoàn toàn. Hãy xem điều đó làm thay đổi giải pháp cho bài toán này như thế nào:
| $.0001u + v = 1$ | bắt đầu với ma trận hệ số | $A = \begin{bmatrix} .0001 & 1 \\ -1 & 1 \end{bmatrix}$ |
|------------------|--------------------------------|---------------------------------------------------------|
| $-u + v = 0$     |                                |                                                         |

Nếu chúng ta chấp nhận .0001 làm phần tử trục, phép khử sẽ cộng 10.000 lần hàng 1 vào hàng 2. Sai số làm tròn để lại
| $10,000v = 10,000$ | thay vì | $10,001v = 10,001$. |
|--------------------|------------|----------------------|

Câu trả lời tính được $v = 1$ gần với giá trị thực $v = .9999$. Nhưng sau đó, phép thế ngược sẽ đưa $v = 1$ bị sai vào phương trình tìm $u$:
| $.0001u + 1 = 1$ | thay vì | $.0001u + .9999 = 1$. |
|-------------------|------------|-------------------------|

Phương trình đầu tiên cho $u = 0$. Đáp án đúng (hãy nhìn vào phương trình thứ hai) là $u = 1.000$. Bằng cách làm mất đi số "1" trong ma trận, chúng ta đã đánh mất nghiệm. *Sự thay đổi nhỏ từ 10.001 thành 10.000 đã làm thay đổi đáp án từ $u = 1$ thành $u = 0$ (lỗi 100%!).*

Nếu chúng ta hoán đổi các hàng, ngay cả máy tính yếu này cũng tìm được câu trả lời chính xác tới 3 chữ số thập phân:
| $-u + v = 0$     | $\longrightarrow$ | $-u + v = 0$ | $\longrightarrow$ | $u = 1$   |
|------------------|-------------------|--------------|-------------------|-----------|
| $.0001u + v = 1$ |                   | $v = 1$      |                   | $v = 1$.  |

Các phần tử trục ban đầu là .0001 và 10.000 — định tỷ lệ rất kém. Sau khi hoán đổi hàng, các phần tử trục chính xác là -1 và 1.0001 — định tỷ lệ tốt. Các phần tử trục được tính toán là -1 và 1 nằm sát với các giá trị chính xác. Các phần tử trục nhỏ mang đến sự bất ổn định số học, và biện pháp khắc phục là *chọn phần tử trục cục bộ (partial pivoting).* Đây là chiến lược của chúng ta khi đến và tìm kiếm phần tử trục tốt nhất có thể ở cột $k$:

*Chọn số lớn nhất ở hàng $k$ hoặc bên dưới. Hoán đổi hàng của nó với hàng $k$.*

Chiến lược *chọn phần tử trục toàn cục (complete pivoting)* cũng tìm kiếm phần tử trục lớn nhất trong các cột sau. Nó hoán đổi cả cột cũng như hàng. Chi phí này hiếm khi được biện minh là hợp lý, và tất cả các mã lệnh chính đều sử dụng việc chọn trục cục bộ. Nhân một hàng hoặc cột với một hằng số tỷ lệ cũng có thể rất đáng giá. *Nếu phương trình đầu tiên ở trên là $u + 10,000v = 10,000$ và chúng ta không định tỷ lệ lại, thì 1 trông có vẻ như một phần tử trục tốt và chúng ta sẽ bỏ qua bước hoán đổi hàng cần thiết.*

Đối với các ma trận xác định dương, việc hoán đổi hàng là *không* bắt buộc. Sẽ an toàn khi chấp nhận các phần tử trục như chúng xuất hiện. Các phần tử trục nhỏ có thể xuất hiện, nhưng ma trận sẽ không được cải thiện bởi việc hoán đổi hàng. Khi số điều kiện của nó cao, vấn đề nằm ở ma trận chứ không phải ở mã lệnh. Trong trường hợp này, đầu ra chắc chắn sẽ nhạy cảm với đầu vào.

Người đọc giờ đây đã hiểu được cách máy tính thực sự giải phương trình $Ax = b$ — *bằng phương pháp khử có chọn phần tử trục cục bộ.* So với mô tả mang tính lý thuyết — tìm $A^{-1}$ *và nhân* $A^{-1}b$ — thì các chi tiết này tốn thời gian. Nhưng trong thời gian máy tính, phép khử diễn ra nhanh hơn nhiều. Tôi tin rằng phép khử cũng là phương pháp tốt nhất để tiếp cận đại số của các không gian hàng và các không gian hạt nhân.

# **Số lượng các Phép toán: Ma trận Đầy (Operation Counts: Full Matrices)**

Đây là một câu hỏi thực tế về chi phí. *Cần bao nhiêu phép toán riêng biệt để giải $Ax = b$ bằng phép khử?* Điều này quyết định mức độ lớn của bài toán mà chúng ta có thể đảm đương được.

Đầu tiên, hãy nhìn vào $A$, nó đang dần biến thành $U$. Khi trừ đi một bội số của hàng 1 khỏi hàng 2, chúng ta thực hiện $n$ phép toán. Phép toán đầu tiên là phép chia cho phần tử trục, để tìm hệ số nhân $l$. Đối với $n - 1$ phần tử khác dọc theo hàng, phép toán là "nhân-trừ". Để cho tiện, chúng tôi tính đây là một phép toán duy nhất. Nếu bạn coi việc nhân với $l$ và trừ đi phần tử hiện có là hai phép toán riêng biệt, *hãy nhân đôi tất cả các số lượng của chúng tôi.*

Ma trận $A$ có kích thước $n \times n$. Phép đếm số lượng phép toán áp dụng cho tất cả $n - 1$ hàng bên dưới hàng đầu tiên. Như vậy cần $n$ lần $n - 1$ phép toán, hay $n^2 - n$, để tạo ra các số không bên dưới phần tử trục đầu tiên. *Kiểm tra: Tất cả $n^2$ phần tử đều bị thay đổi, ngoại trừ $n$ phần tử ở hàng đầu tiên.*

Khi phép khử xuống còn $k$ phương trình, các hàng sẽ ngắn hơn. Chúng ta chỉ cần $k^2 - k$ phép toán (thay vì $n^2 - n$) để xóa cột bên dưới phần tử trục. Điều này đúng đối với $1 \leq k \leq n$. Bước cuối cùng không yêu cầu phép toán nào ($1^2 - 1 = 0$); quá trình khử tiến đã hoàn tất. Tổng số đếm để đạt tới $U$ là tổng của $k^2 - k$ theo mọi giá trị của $k$ từ 1 đến $n$:
$$(1^2 + \dots + n^2) - (1 + \dots + n) = \frac{n(n+1)(2n+1)}{6} - \frac{n(n+1)}{2} = \frac{n^3 - n}{3}$$

Đó là những công thức đã biết cho tổng của $n$ số đầu tiên và bình phương của chúng. Thay $n = 100$ ta được một triệu trừ đi một trăm — sau đó chia cho 3. (Điều đó chuyển thành một giây trên một máy trạm - workstation). Chúng ta sẽ bỏ qua $n$ khi so sánh với $n^3$, để đi đến kết luận chính của chúng ta:

*Số lần nhân-trừ là $\frac{1}{3}n^3$ cho phép khử tiến ($A$ thành $U$, tạo ra $L$).*

Điều đó có nghĩa là $\frac{1}{3}n^3$ phép nhân và phép trừ. Tăng gấp đôi $n$ sẽ làm tăng chi phí này lên 8 lần (vì $n$ được lập phương). 100 phương trình thì dễ dàng, 1000 thì đắt đỏ hơn, 10.000 phương trình dày đặc thì gần như là không thể. Chúng ta cần một máy tính nhanh hơn hoặc có rất nhiều số không hoặc một ý tưởng mới.

Ở vế phải của các phương trình, các bước đi nhanh hơn nhiều. Chúng tôi thao tác trên các số đơn lẻ, không phải toàn bộ hàng. *Mỗi vế phải cần chính xác $n^2$ phép toán.* Đi xuống và quay lên, chúng ta đang giải hai hệ tam giác, $Lc = b$ tiến về phía trước và $Ux = c$ lùi về phía sau. Trong phép thế ngược, ẩn số cuối cùng chỉ cần một phép chia cho phần tử trục cuối cùng. Phương trình nằm trên nó cần hai phép toán - thay thế $x_n$ và chia cho phần tử trục của *nó*. Bước thứ $k$ cần $k$ phép nhân-trừ, và tổng số cho phép thế ngược là
$$1 + 2 + \dots + n = \frac{n(n+1)}{2} \approx \frac{1}{2}n^2$$
phép toán.

Phần tiến lên cũng tương tự. *Tổng số $n^2$ chính xác bằng với số đếm cho phép nhân $A^{-1}b$!* Điều này khiến phép khử Gauss có hai lợi thế lớn so với $A^{-1}b$:
- **1 Phép khử yêu cầu $\frac{1}{3}n^3$ phép nhân-trừ, so với $n^3$ đối với $A^{-1}$.**
- **2 Nếu $A$ có dạng dải (banded) thì $L$ và $U$ cũng vậy: ngược lại $A^{-1}$ chứa đầy những số khác 0.**

#### **Ma trận Dải (Band Matrices)**

Những số lượng này được cải thiện khi $A$ có *"những số 0 tốt (good zeros)".* Một số 0 tốt là một phần tử vẫn giữ nguyên là 0 trong $L$ và $U$. *Những số 0 tốt nhất nằm ở đầu của một hàng.* Chúng không yêu cầu các bước khử (các hệ số nhân bằng không). Vì vậy chúng ta cũng tìm thấy những số 0 tốt tương tự trong $L$. Điều đó đặc biệt rõ ràng đối với *ma trận ba đường chéo (tridiagonal matrix) $A$* này (và đối với các ma trận dải trong Hình 11.1):

**Ba đường chéo (Tridiagonal) = Hai đường chéo (Bidiagonal) nhân hai đường chéo (Bidiagonal)**
$$A = \begin{bmatrix} 1 & -1 & & \\ -1 & 2 & -1 & \\ & -1 & 2 & -1 \\ & & -1 & 2 \end{bmatrix} = \begin{bmatrix} 1 & & & \\ -1 & 1 & & \\ & -1 & 1 & \\ & & -1 & 1 \end{bmatrix} \begin{bmatrix} 1 & -1 & & \\ & 1 & -1 & \\ & & 1 & -1 \\ & & & 1 \end{bmatrix} = LU$$

Hình 11.1: $A = LU$ cho một ma trận dải. Những số 0 tốt trong $A$ *vẫn là 0* trong $L$ và $U$.

Những số 0 này dẫn đến một sự thay đổi hoàn toàn trong số đếm phép toán, đối với "nửa chiều rộng dải (half-bandwidth)" $w$:

*Một ma trận dải có $a_{ij} = 0$ khi $|i - j| > w$.*

Do đó $w = 1$ đối với ma trận đường chéo, $w = 2$ đối với ma trận ba đường chéo, $w = n$ đối với ma trận đầy (dense). Chiều dài của hàng chứa trục nhiều nhất là $w$. Có không quá $w - 1$ phần tử khác không bên dưới bất kỳ phần tử trục nào. Mỗi giai đoạn của phép khử hoàn tất sau $w(w - 1)$ phép toán, và *cấu trúc dải vẫn tồn tại.* Có $n$ cột cần dọn dẹp. Do đó:

#### *Phép khử trên một ma trận dải ($A$ thành $L$ và $U$) cần ít hơn $w^2n$ phép toán.*

Đối với một ma trận dải, số lượng tỷ lệ thuận với $n$ thay vì $n^3$. Nó cũng tỷ lệ với $w^2$. Một ma trận đầy (full) có $w = n$ và chúng ta quay trở lại $n^3$. Để có con số đếm chính xác, hãy nhớ rằng chiều rộng dải sẽ giảm xuống dưới $w$ ở góc dưới cùng bên phải (không đủ không gian).

Ở vế phải của $Ax = b$, để tìm $x$ từ $b$, chi phí là khoảng $2wn$ (so với $n^2$ thông thường). *Điểm chính: Đối với ma trận dải, số lượng phép toán tỷ lệ thuận với $n$.* Quá trình này cực kỳ nhanh. Một ma trận ba đường chéo bậc 10.000 có chi phí rất rẻ, miễn là *chúng ta không tính* $A^{-1}$. Ma trận nghịch đảo đó hoàn toàn không có số 0 nào:
$$A = \begin{bmatrix} 1 & -1 & 0 & 0 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ 0 & 0 & -1 & 2 \end{bmatrix} \quad \text{có} \quad A^{-1} = U^{-1} L^{-1} = \begin{bmatrix} 4 & 3 & 2 & 1 \\ 3 & 3 & 2 & 1 \\ 2 & 2 & 2 & 1 \\ 1 & 1 & 1 & 1 \end{bmatrix}.$$

Chúng ta thực sự sẽ tệ hơn nếu biết $A^{-1}$ so với việc biết $L$ và $U$. Việc nhân với $A^{-1}$ cần đầy đủ $n^2$ bước. Việc giải $Lc = b$ và $Ux = c$ chỉ cần $2wn$.

Một cấu trúc dải là rất phổ biến trong thực tế, khi ma trận phản ánh các kết nối giữa các hàng xóm gần: $a_{13} = 0$ và $a_{14} = 0$ vì 1 không phải là hàng xóm của 3 và 4.

Chúng tôi kết thúc bằng việc đếm cho Gauss-Jordan và Gram-Schmidt-Householder:

$$A^{-1} \text{ tốn } n^3 \text{ bước nhân-trừ.} \qquad QR \text{ tốn } \frac{2}{3} n^3 \text{ bước.}$$

Trong $AA^{-1} = I$, cột thứ $j$ của $A^{-1}$ giải hệ $Ax_j = \text{cột thứ } j \text{ của } I$. Vế trái tốn $\frac{1}{3}n^3$ như thông thường. (Đây là chi phí dùng một lần! $L$ và $U$ không bị lặp lại). Sự tiết kiệm đặc biệt cho cột thứ $j$ của $I$ đến từ $j - 1$ số 0 đầu tiên của nó. Không cần thao tác nào ở vế phải cho đến khi phép khử chạm đến hàng $j$. Chi phí khử tiến (forward cost) là $\frac{1}{2}(n - j)^2$ thay vì $\frac{1}{2}n^2$. Lấy tổng theo $j$, tổng số cho phép khử tiến trên $n$ vế phải là $\frac{1}{6}n^3$. Số lượng phép nhân-trừ cuối cùng cho $A^{-1}$ là $n^3$ nếu chúng ta thực sự muốn có ma trận nghịch đảo:
$$\text{Cho } A^{-1} \quad \frac{n^3}{3} (L \text{ và } U) + \frac{n^3}{6} (\text{khử tiến}) + n \left( \frac{n^2}{2} \right) \text{ (các phép thế ngược)} = n^3. \quad (1)$$

**Trực giao hóa (Orthogonalization, từ $A$ đến $Q$):** Sự khác biệt chính so với phép khử là *mỗi hệ số nhân được quyết định bởi một tích vô hướng*. Việc đó cần $n$ phép toán, trong khi phép khử chỉ chia cho phần tử trục. Sau đó có $n$ phép toán "nhân-trừ" để loại bỏ khỏi cột $k$ hình chiếu của nó dọc theo cột $j < k$ (xem Phần 4.4). Chi phí kết hợp là $2n$ trong khi đối với phép khử là $n$. Hệ số 2 này là cái giá của tính trực giao. Chúng ta đang biến một tích vô hướng thành số 0 ở nơi mà phép khử biến một phần tử thành số 0.

**Cảnh báo** Để đánh giá một thuật toán số, việc đếm các phép toán là **chưa đủ**. Vượt ra ngoài việc "đếm số phép toán dấu phẩy động (flop counting)" là một nghiên cứu về tính ổn định (Householder chiến thắng) và luồng dữ liệu.

## Sắp xếp lại Các ma trận Thưa (Reordering Sparse Matrices)

Đối với các ma trận dải có chiều rộng không đổi $w$, thứ tự hàng là tối ưu. Nhưng đối với hầu hết các ma trận thưa trong các phép tính thực tế, chiều rộng của dải là *không bất biến* và có nhiều số 0 bên trong dải. Những số 0 đó có thể bị lấp đầy khi quá trình khử diễn ra — chúng bị mất đi. Chúng ta cần *đánh số lại các phương trình để giảm bớt sự lấp đầy (fill-in)*, và do đó đẩy nhanh phép khử.

Nói chung, chúng ta muốn di chuyển các số 0 đến các hàng và cột sớm. Dù sao thì các hàng và cột sau cũng ngắn hơn. Thuật toán "bậc tối thiểu xấp xỉ (approximate minimum degree)" trong MATLAB thưa thớt là thuật toán *tham lam (greedy)* — nó chọn hàng cần khử mà không tính đếm mọi hậu quả. Chúng ta có thể đạt đến một ma trận gần như dày đặc khi gần kết thúc, nhưng tổng số phép toán để đạt được $LU$ vẫn nhỏ hơn nhiều. Việc tìm ra giá trị tối thiểu tuyệt đối của các phần tử khác 0 trong $L$ và $U$ là một bài toán NP-khó, chi phí quá cao và thuật toán **amd** là một sự thỏa hiệp tốt.

Sự lấp đầy rất nổi tiếng khi mỗi điểm trên một lưới vuông được nối với bốn điểm lân cận gần nhất của nó. Không thể đánh số tất cả các điểm lưới sao cho các điểm lân cận ở cạnh nhau! Nếu chúng ta đánh số theo hàng của lưới, sẽ phải chờ một khoảng thời gian dài mới đi vòng được đến điểm lưới ở bên trên.
$$\begin{array}{ccc}
 j & \begin{bmatrix} 1 & 1 & 1 \\ -2 & 1 & 0 \\ -2 & 0 & 2 \end{bmatrix} & \longrightarrow & \begin{bmatrix} 1 & 1 & 1 \\ 0 & 3 & 2 \\ 0 & 2 & 4 \end{bmatrix} & j = 1 & \begin{array}{c} i = 2 \\ k = 3 \end{array} & \longrightarrow & 1 & \begin{array}{c} 2 \\ \\ \\ 3 \end{array} \\
 a_{32} = 0 & a_{32} = 2 & a_{32} = 0 & \text{trước} & a_{32} \neq 0 & \text{sau}
 \end{array}$$

Chúng ta chỉ cần *vị trí* của các phần tử khác 0, không cần giá trị chính xác của chúng. Hãy nghĩ về đồ thị của các phần tử khác 0: *Nút $i$ được nối với nút $j$ nếu $a_{ij} \neq 0$*. Hãy quan sát để thấy cách phép khử có thể tạo ra các phần tử khác 0 (các cạnh mới), điều mà chúng ta đang cố gắng tránh.

Lệnh **nnz($L$)** đếm các hệ số nhân khác 0 trong ma trận tam giác dưới $L$, lệnh **find($L$)** sẽ liệt kê chúng, và lệnh **spy($L$)** hiển thị tất cả chúng.

Mục tiêu của **colamd** và **symamd** là một thứ tự tốt hơn (hoán vị $P$) giúp giảm sự lấp đầy cho $AP$ và $P^T AP$ — bằng cách chọn *phần tử trục có ít số khác 0 nhất bên dưới nó*.

### Trực giao hóa Nhanh (Fast Orthogonalization)

Có ba cách để đạt được phép phân tích nhân tử quan trọng $A = QR$. Quá trình Gram-Schmidt hoạt động để tìm ra các vectơ trực chuẩn trong $Q$. Khi đó $R$ là ma trận tam giác trên vì thứ tự của các bước Gram-Schmidt. Bây giờ chúng ta hãy xem xét các phương pháp tốt hơn (Householder và Givens), sử dụng tích của các $Q$ đặc biệt đơn giản mà chúng ta *biết* là trực giao.

Phép khử cho ra $A = LU$, quá trình trực giao hóa cho ra $A = QR$. Chúng ta không muốn có ma trận tam giác $L$, chúng ta muốn có ma trận trực giao $Q$. $L$ là tích của các $E$ từ phép khử, với các số 1 trên đường chéo và hệ số nhân $l_{ij}$ bên dưới. $Q$ sẽ là tích của các ma trận trực giao.

Có hai ma trận trực giao đơn giản thay thế cho các $E$. **Ma trận phản xạ (reflection matrices)** $I - 2uu^T$ được đặt theo tên của Householder. **Ma trận quay mặt phẳng (plane rotation matrices)** được đặt theo tên của Givens. Ma trận đơn giản có tác dụng quay mặt phẳng $xy$ một góc $\theta$ là $Q_{21}$:
$$\begin{array}{ll}
 \text{Phép quay Givens} & Q_{21} = \begin{bmatrix} \cos \theta & -\sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{bmatrix}.
 \end{array}$$

Sử dụng $Q_{21}$ theo cách bạn đã sử dụng $E_{21}$, để tạo ra một số 0 ở vị trí $(2, 1)$. Điều đó quyết định góc $\theta$. Bill Hager đưa ra ví dụ này trong *Applied Numerical Linear Algebra (Đại số Tuyến tính Số Ứng dụng)*:
$$Q_{21}A = \begin{bmatrix} .6 & .8 & 0 \\ -.8 & .6 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 90 & -153 & 114 \\ 120 & -79 & -223 \\ 200 & -40 & 395 \end{bmatrix} = \begin{bmatrix} 150 & -155 & -110 \\ 0 & 75 & -225 \\ 200 & -40 & 395 \end{bmatrix}.$$

Số 0 được sinh ra từ $-.8(90) + .6(120)$. Không cần phải tìm $\theta$, điều chúng ta cần là $\cos \theta$:
$$\cos \theta = \frac{90}{\sqrt{90^2 + 120^2}} \quad \text{và} \quad \sin \theta = \frac{-120}{\sqrt{90^2 + 120^2}}. \quad (2)$$

Bây giờ chúng ta xử lý phần tử $(3, 1)$. Phép quay sẽ diễn ra trong các hàng và cột 3 và 1. Các số $\cos \theta$ và $\sin \theta$ được xác định từ 150 và 200, thay vì 90 và 120.
$$Q_{31}Q_{21}A = \begin{bmatrix} .6 & 0 & .8 \\ 0 & 1 & 0 \\ -.8 & 0 & .6 \end{bmatrix} \begin{bmatrix} 150 & \cdot & \cdot \\ 0 & \cdot & \cdot \\ 200 & \cdot & \cdot \end{bmatrix} = \begin{bmatrix} 250 & -125 & 250 \\ 0 & 75 & -225 \\ 0 & 100 & 325 \end{bmatrix}$$

Một bước nữa để đến $R$. Phần tử $(3, 2)$ phải biến thành số 0. Các số $\cos \theta$ và $\sin \theta$ bây giờ có được từ 75 và 100. Phép quay bây giờ nằm ở các hàng và cột 2 và 3:
$$Q_{32}Q_{31}Q_{21}A = \begin{bmatrix} 1 & 0 & 0 \\ 0 & .6 & .8 \\ 0 & -.8 & .6 \end{bmatrix} \begin{bmatrix} 250 & -125 \\ 0 & 75 \\ 0 & 100 \end{bmatrix} = \begin{bmatrix} 250 & -125 \\ 0 & 125 \\ 0 & 0 \end{bmatrix},$$

*Chúng ta đã đạt tới ma trận tam giác trên $R$.* Vậy $Q$ là gì? Di chuyển các phép quay mặt phẳng $Q_{ij}$ sang vế kia để tìm $A = QR$ — giống hệt như cách bạn di chuyển các ma trận khử $E_{ij}$ sang vế kia để tìm $A = LU$:
| $Q_{32}Q_{31}Q_{21}A = R$ | nghĩa là | $A = (Q_{21}^{-1}Q_{31}^{-1}Q_{32}^{-1})R = QR.$ | (3) |
|---------------------------|-------|--------------------------------------------------|-----|

Nghịch đảo của mỗi $Q_{ij}$ là $Q_{ij}^T$ (quay một góc $-\theta$). Nghịch đảo của $E_{ij}$ không phải là một ma trận trực giao! $LU$ và $QR$ thì tương tự nhưng $L$ và $Q$ thì không giống nhau.

Phép phản xạ Householder nhanh hơn phép quay vì mỗi phép phản xạ sẽ xóa sạch một cột hoàn chỉnh bên dưới đường chéo. Hãy quan sát cách cột đầu tiên $a_1$ của $A$ trở thành cột $r_1$ của $R$:

Độ dài không bị thay đổi, và $u_1$ có cùng hướng với $a_1 - r_1$. Chúng ta có $n - 1$ phần tử trong vectơ đơn vị $u_1$ để có được $n - 1$ số không trong $r_1$. (Các phép quay có một góc $\theta$ để có được một số không). Khi đi tới cột $k$, chúng ta có $n - k$ lựa chọn có sẵn trong vectơ đơn vị $u_k$. Điều này dẫn đến $n - k$ số 0 trong $r_k$. *Chúng ta chỉ cần lưu trữ các giá trị $u$ và $r$ để biết $Q$ và $R$ cuối cùng:*
**Nghịch đảo của $H_i$ là $H_i$**     $(H_{n-1} \dots H_1)A = R$    nghĩa là    $A = (H_1 \dots H_{n-1})R = QR$. (5)

Đây là cách LAPACK cải thiện phương pháp Gram-Schmidt của thế kỷ 19. $Q$ là trực giao *một cách chính xác (exactly)*.

Phần 11.3 giải thích cách sử dụng $A = QR$ trong một tính toán lớn khác của đại số tuyến tính - *bài toán trị riêng.* Các nhân tử $QR$ được đảo ngược để cho ra $A_1 = RQ$ cũng chính là $Q^{-1}AQ$. Vì $A_1$ đồng dạng với $A$, nên các trị riêng không thay đổi. Sau đó, $A_1$ được phân tích thành $Q_1R_1$, và đảo ngược các nhân tử cho ra $A_2$. Đáng ngạc nhiên là các phần tử bên dưới đường chéo ngày càng nhỏ hơn trong $A_1, A_2, A_3, \dots$ và chúng ta có thể nhận diện được các trị riêng. Đây là "phương pháp $QR$" cho bài toán $Ax = \lambda x$, một thành công lớn của đại số tuyến tính số.

## Tập bài tập 11.1 (Problem Set 11.1)

**1** Tìm hai phần tử trục khi có và khi không có sự hoán đổi hàng để làm tối đa hóa phần tử trục:
$$A = \begin{bmatrix} .001 & 0 \\ 1 & 1000 \end{bmatrix}.$$
Với các phép hoán đổi hàng để tối đa hóa phần tử trục, tại sao không có phần tử nào của $L$ lớn hơn 1? Tìm một ma trận $3 \times 3$ $A$ có tất cả các $|a_{ij}| \leq 1$ và $|l_{ij}| \leq 1$ nhưng phần tử trục thứ ba = 4.
**2** Tính ma trận nghịch đảo chính xác của ma trận Hilbert $A$ bằng phương pháp khử. Sau đó tính lại $A^{-1}$ bằng cách làm tròn mọi số còn ba chữ số:
**Ma trận có điều kiện xấu (Ill-conditioned matrix)**
$$A = \text{hilb}(3) = \begin{bmatrix} 1 & \frac{1}{2} & \frac{1}{3} \\ \frac{1}{2} & \frac{1}{3} & \frac{1}{4} \\ \frac{1}{3} & \frac{1}{4} & \frac{1}{5} \end{bmatrix}.$$
**3** Đối với cùng một $A$, hãy tính $\mathbf{b} = A\mathbf{x}$ với $\mathbf{x} = (1, 1, 1)$ và $\mathbf{x} = (0, 6, -3.6)$. Một thay đổi nhỏ $\Delta\mathbf{b}$ tạo ra một thay đổi lớn $\Delta\mathbf{x}$.
**4** Tìm các trị riêng (bằng máy tính) của ma trận Hilbert $8 \times 8$ $a_{ij} = 1/(i+j-1)$. Trong phương trình $A\mathbf{x} = \mathbf{b}$ với $\|\mathbf{b}\| = 1$, $\|\mathbf{x}\|$ có thể lớn tới mức nào? Nếu $\mathbf{b}$ có sai số làm tròn nhỏ hơn $10^{-16}$, điều này có thể gây ra sai số lớn tới mức nào đối với $\mathbf{x}$? Xem Phần 9.2.
**5** Đối với phép thế ngược với ma trận dải (chiều rộng $w$), hãy chỉ ra rằng số lượng phép nhân để giải $U\mathbf{x} = \mathbf{c}$ là xấp xỉ $wn$.
**6** Nếu bạn biết $L$ và $U$ và $Q$ và $R$, thì việc giải $LU\mathbf{x} = \mathbf{b}$ hay $QR\mathbf{x} = \mathbf{b}$ sẽ nhanh hơn?
**7** Hãy chứng tỏ rằng số lượng phép nhân để tìm nghịch đảo của ma trận tam giác trên kích thước $n \times n$ là khoảng $\frac{1}{6}n^3$. Sử dụng phép thế ngược trên các cột của $I$, hướng lên trên từ các số 1.
**8** Bằng cách chọn phần tử trục lớn nhất có thể ở mỗi cột (chọn trục cục bộ), hãy phân tích từng ma trận $A$ thành $PA = LU$:
$$A = \begin{bmatrix} 1 & 0 \\ 2 & 2 \end{bmatrix} \quad \text{và} \quad A = \begin{bmatrix} 1 & 0 & 1 \\ 2 & 2 & 0 \\ 0 & 2 & 0 \end{bmatrix}.$$
**9** Đặt các số 1 trên ba đường chéo trung tâm của ma trận ba đường chéo $4 \times 4$. Tìm phần bù đại số của 6 phần tử 0. Những phần tử đó khác 0 trong $A^{-1}$.
**10** (Gợi ý bởi C. Van Loan.) Tìm phân tích $LU$ và giải bằng phép khử khi $\varepsilon = 10^{-3}, 10^{-6}, 10^{-9}, 10^{-12}, 10^{-15}$:
$$\begin{bmatrix} \varepsilon & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 1 + \varepsilon \\ 2 \end{bmatrix}.$$
Giá trị $\mathbf{x}$ thực sự là $(1, 1)$. Lập một bảng để chỉ ra sai số đối với từng giá trị $\varepsilon$. Hoán đổi hai phương trình và giải lại — các sai số hầu như sẽ biến mất.
**11**
(a) Chọn $\sin \theta$ và $\cos \theta$ để tam giác hóa $A$, và tìm $R$:
| Phép quay Givens | $Q_{21}A = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} 1 & -1 \\ 3 & 5 \end{bmatrix} = \begin{bmatrix} * & * \\ 0 & * \end{bmatrix} = R.$ |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

(b) Chọn $\sin \theta$ và $\cos \theta$ để làm cho $QAQ^{-1}$ thành ma trận tam giác. Các trị riêng là gì?
**12** Khi $A$ được nhân với phép quay mặt phẳng $Q_{ij}$, những phần tử nào của $A$ bị thay đổi? Khi $Q_{ij}A$ được nhân bên phải với $Q_{ij}^{-1}$, những phần tử nào bị thay đổi bây giờ?
**13** Có bao nhiêu phép nhân và bao nhiêu phép cộng được sử dụng để tính toán $Q_{ij}A$? Việc tổ chức cẩn thận toàn bộ trình tự các phép quay cho ra $\frac{4}{3}n^3$ phép nhân và $\frac{4}{3}n^3$ phép cộng — giống như đối với $QR$ bằng các phép phản xạ và gấp đôi số lượng so với phép phân tích $LU$.

### **Các Bài toán Thử thách (Challenge Problems)**

**14 (Quay một bàn tay robot)** Robot tạo ra bất kỳ phép quay $3 \times 3$ $A$ nào từ các phép quay mặt phẳng quanh các trục $x, y, z$. Khi đó $Q_{32}Q_{31}Q_{21}A = R$, trong đó $A$ là ma trận trực giao nên $R$ chính là $I$! Ba vòng quay của robot nằm ở $A = Q_{21}^{-1}Q_{31}^{-1}Q_{32}^{-1}$. Ba góc quay này là "các góc Euler" và $\det Q = 1$ để tránh việc phản xạ. Hãy bắt đầu bằng cách chọn $\cos \theta$ và $\sin \theta$ sao cho
| $Q_{21}A = \begin{bmatrix} \cos \theta & -\sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{bmatrix} \frac{1}{3} \begin{bmatrix} -1 & 2 & 2 \\ 2 & -1 & 2 \\ 2 & 2 & -1 \end{bmatrix}$ bằng không ở vị trí $(2, 1)$. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**15** Tạo ma trận đạo hàm bậc hai $10 \times 10$ tên $K$ qua lệnh $K = \text{toeplitz}([2 \ -1 \ \text{zeros}(1, 8)])$. Hoán vị các hàng và các cột một cách ngẫu nhiên bằng $KK = K(\text{randperm}(10), \text{randperm}(10))$. Phân tích thông qua $[L, U] = \text{lu}(K)$ và $[LL, UU] = \text{lu}(KK)$, và đếm các số khác 0 qua lệnh $\text{nnz}(L)$ và $\text{nnz}(LL)$. Trong trường hợp này $L$ nằm ở trật tự ba đường chéo hoàn hảo, nhưng $LL$ thì không.
**16** Một sự sắp xếp khác đối với ma trận $K$ này là tô màu luân phiên các điểm lưới bằng màu đỏ và màu đen. Hoán vị $P$ này làm thay đổi thứ tự $1, \dots, 10$ thông thường thành $1, 3, 5, 7, 9, 2, 4, 6, 8, 10$:
| Thứ tự đỏ-đen (Red-black ordering) | $PKP^T = \begin{bmatrix} 2I & D \\ D^T & 2I \end{bmatrix}.$ | Tìm ma trận $D$. |
|--------------------|------------------------------------------------------------------|-----------------------|

Có rất nhiều thí nghiệm thú vị có thể thực hiện. Nếu bạn gửi những ý tưởng hay, chúng có thể được đưa lên trang web đại số tuyến tính math.mit.edu/linearalgebra. Tôi cũng khuyên bạn nên tìm hiểu lệnh $B = \text{sparse}(A)$, sau đó $\text{find}(B)$ sẽ liệt kê các phần tử khác 0 và $\text{lu}(B)$ sẽ phân tích $B$ bằng cách sử dụng định dạng thưa thớt đó cho $L$ và $U$. Chỉ tính toán đối với những phần tử khác không, trong khi hàm MATLAB thông thường (dense) tính toán đối với mọi số 0.
**17** Jeff Stuart đã tạo ra một hoạt động sinh viên minh họa một cách xuất sắc về điều kiện xấu:
$$\begin{bmatrix} 1 & 1.0001 \\ 1 & 1.0000 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 3.0001 + e \\ 3.0000 + E \end{bmatrix}$$
**Với các sai số**     $x = 2 - 10000(e - E)$  
**$e$ và $E$**     $y = 1 + 10000(e - E)$
Khi những phương trình đó được biểu diễn bằng những chiếc gậy dài gần như song song, một cái lắc nhẹ sẽ tạo ra một bước nhảy vọt ở điểm giao cắt $(x, y)$. Các sai số $e$ và $E$ được khuếch đại lên 10000 lần.

## 11.2 Chuẩn và Số Điều kiện (Norms and Condition Numbers)

Làm thế nào để đo lường kích thước của một ma trận? Đối với một vectơ, chiều dài là $\|\mathbf{x}\|$. Đối với một ma trận, *chuẩn (norm) là* $\|A\|$. Từ "chuẩn" này đôi khi được sử dụng cho các vectơ, thay cho chiều dài. Nó luôn được sử dụng đối với các ma trận, và có nhiều cách để đo lường $\|A\|$. Chúng ta hãy xem xét các yêu cầu trên tất cả "các chuẩn ma trận (matrix norms)" và sau đó chọn một.

Frobenius đã bình phương tất cả các giá trị $|a_{ij}|^2$ và cộng chúng lại; chuẩn $\|A\|_F$ của ông là căn bậc hai của tổng đó. Điều này coi $A$ như một vectơ dài với $n^2$ thành phần: đôi khi hữu ích, nhưng không phải là lựa chọn ở đây.

Tôi thích bắt đầu với một chuẩn vectơ hơn. Bất đẳng thức tam giác phát biểu rằng $\|\mathbf{x} + \mathbf{y}\|$ không lớn hơn $\|\mathbf{x}\| + \|\mathbf{y}\|$. Chiều dài của $2\mathbf{x}$ hoặc $-2\mathbf{x}$ được nhân đôi lên thành $2\|\mathbf{x}\|$. Những quy tắc tương tự sẽ được áp dụng cho các chuẩn ma trận:
$$\|A + B\| \leq \|A\| + \|B\| \quad \text{và} \quad \|cA\| = |c| \|A\|. \quad (1)$$

Yêu cầu thứ hai đối với chuẩn ma trận là mới, vì các ma trận có thể nhân với nhau. Chuẩn $\|A\|$ kiểm soát sự gia tăng từ $\mathbf{x}$ lên $A\mathbf{x}$, và từ $B$ lên $AB$:
$$\text{Hệ số tăng trưởng (Growth factor) } \|A\| \quad \|A\mathbf{x}\| \leq \|A\| \|\mathbf{x}\| \quad \text{và} \quad \|AB\| \leq \|A\| \|B\|. \quad (2)$$

Điều này dẫn đến một cách tự nhiên để định nghĩa $\|A\|$, chuẩn của một ma trận:
$$\text{Chuẩn của } A \text{ là tỷ số lớn nhất } \frac{\|A\mathbf{x}\|}{\|\mathbf{x}\|}: \quad \|A\| = \max_{\mathbf{x} \neq \mathbf{0}} \frac{\|A\mathbf{x}\|}{\|\mathbf{x}\|}. \quad (3)$$

$\|A\mathbf{x}\|/\|\mathbf{x}\|$ không bao giờ lớn hơn $\|A\|$ (giá trị cực đại của nó). Điều này nói lên rằng $\|A\mathbf{x}\| \leq \|A\| \|\mathbf{x}\|$.

**Ví dụ 1** Nếu $A$ là ma trận đơn vị $I$, các tỷ số là $\|\mathbf{x}\|/\|\mathbf{x}\|$. Do đó $\|I\| = 1$. Nếu $A$ là ma trận trực giao $Q$, các chiều dài một lần nữa được giữ nguyên: $\|Q\mathbf{x}\| = \|\mathbf{x}\|$. Các tỷ số vẫn cho ra $\|Q\| = 1$. Một ma trận trực giao $Q$ rất tốt để tính toán: các sai số không tăng lên.

**Ví dụ 2** Chuẩn của ma trận đường chéo là phần tử lớn nhất của nó (dùng các giá trị tuyệt đối):
$$A = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix} \quad \text{có chuẩn } \|A\| = 3. \quad \text{Vectơ riêng } \mathbf{x} = \begin{bmatrix} 0 \\ 1 \end{bmatrix} \quad \text{cho } A\mathbf{x} = 3\mathbf{x}.$$
Trị riêng là 3. Đối với $A$ này (nhưng không phải mọi $A$), trị riêng lớn nhất bằng với chuẩn.

*Đối với một ma trận đối xứng xác định dương, chuẩn là* $\|A\| = \lambda_{\max}(A)$.

Hãy chọn $\mathbf{x}$ là vectơ riêng với trị riêng lớn nhất. Khi đó $\|A\mathbf{x}\|/\|\mathbf{x}\|$ bằng $\lambda_{\max}$. Vấn đề là không có $\mathbf{x}$ nào khác có thể làm cho tỷ số lớn hơn. Ma trận là $A = Q\Lambda Q^T$, và các ma trận trực giao $Q$ và $Q^T$ giữ nguyên chiều dài. Vậy tỷ số cần cực đại hóa thực sự là $\|\Lambda\mathbf{x}\|/\|\mathbf{x}\|$. Chuẩn là trị riêng lớn nhất trên đường chéo $\Lambda$.

**Các ma trận đối xứng** Giả sử $A$ đối xứng nhưng không xác định dương. $A = Q\Lambda Q^T$ vẫn đúng. Khi đó chuẩn là giá trị lớn nhất trong các $|\lambda_1|, |\lambda_2|, \dots, |\lambda_n|$. Chúng tôi lấy các giá trị tuyệt đối, bởi vì chuẩn chỉ liên quan đến chiều dài. Đối với một vectơ riêng $\|Ax\| = \|\lambda x\| = |\lambda|$ nhân với $\|x\|$. Giá trị $x$ mang lại tỷ số lớn nhất là vectơ riêng của cực đại $|\lambda|$.

**Các ma trận không đối xứng** Nếu $A$ không đối xứng, các trị riêng của nó có thể không đo lường được kích thước thực của nó. *Chuẩn có thể lớn hơn mọi trị riêng.* Một ví dụ rất không đối xứng có $\lambda_1 = \lambda_2 = 0$ nhưng chuẩn của nó không phải là không:
$$\|A\| > \lambda_{\max} \quad A = \begin{bmatrix} 0 & 2 \\ 0 & 0 \end{bmatrix} \quad \text{có chuẩn} \quad \|A\| = \max_{x \neq 0} \frac{\|Ax\|}{\|x\|} = 2.$$

Vectơ $x = (0, 1)$ cho ra $Ax = (2, 0)$. Tỷ lệ của các chiều dài là $2/1$. Đây là tỷ lệ lớn nhất $\|A\|$, mặc dù $x$ không phải là một vectơ riêng.

Chính *ma trận đối xứng* $A^T A$, chứ không phải ma trận không đối xứng $A$, có vectơ riêng $x = (0, 1)$. Chuẩn thực sự được quyết định bởi *trị riêng lớn nhất của $A^T A$:*

*Chuẩn của $A$ (dù đối xứng hay không) là căn bậc hai của $\lambda_{\max}(A^T A)$:*
$$\|A\|^2 = \max_{x \neq 0} \frac{\|Ax\|^2}{\|x\|^2} = \max_{x \neq 0} \frac{x^T A^T A x}{x^T x} = \lambda_{\max}(A^T A). \quad (4)$$

Ví dụ không đối xứng với $\lambda_{\max}(A) = 0$ lại có $\lambda_{\max}(A^T A) = 4$:
$$A = \begin{bmatrix} 0 & 2 \\ 0 & 0 \end{bmatrix} \text{ dẫn tới } A^T A = \begin{bmatrix} 0 & 0 \\ 0 & 4 \end{bmatrix} \text{ với } \lambda_{\max} = 4. \text{ Vậy nên chuẩn là } \|A\| = \sqrt{4}.$$

**Đối với bất kỳ $A$ nào** Hãy chọn $x$ là vectơ riêng của $A^T A$ với trị riêng lớn nhất $\lambda_{\max}$. Tỷ số trong phương trình (4) là $x^T A^T A x = x^T (\lambda_{\max}) x$ chia cho $x^T x$. Biểu thức này bằng $\lambda_{\max}$.

Không có $x$ nào có thể mang lại một tỷ số lớn hơn. Ma trận đối xứng $A^T A$ có các trị riêng $\lambda_1, \dots, \lambda_n$ và các vectơ riêng trực chuẩn $q_1, q_2, \dots, q_n$. Mọi $x$ đều là một tổ hợp của những vectơ đó. Thử tổ hợp này vào tỷ số và hãy nhớ rằng $q_i^T q_j = 0$:

$$\frac{x^T A^T A x}{x^T x} = \frac{(c_1 q_1 + \dots + c_n q_n)^T (c_1 \lambda_1 q_1 + \dots + c_n \lambda_n q_n)}{(c_1 q_1 + \dots + c_n q_n)^T (c_1 q_1 + \dots + c_n q_n)} = \frac{c_1^2 \lambda_1 + \dots + c_n^2 \lambda_n}{c_1^2 + \dots + c_n^2}.$$

Tỷ số lớn nhất $\lambda_{\max}$ đạt được khi tất cả các giá trị $c$ đều bằng không, ngoại trừ giá trị nhân với $\lambda_{\max}$.

**Lưu ý 1** Tỷ số trong phương trình (4) là *thương số Rayleigh (Rayleigh quotient)* cho ma trận đối xứng $A^T A$. Giá trị cực đại của nó là trị riêng lớn nhất $\lambda_{\max}(A^T A)$. Tỷ số cực tiểu là $\lambda_{\min}(A^T A)$. Nếu bạn thay bất kỳ vectơ $x$ nào vào thương số Rayleigh $x^T A^T A x / x^T x$, bạn được đảm bảo sẽ nhận được một số nằm giữa $\lambda_{\min}(A^T A)$ và $\lambda_{\max}(A^T A)$.

**Lưu ý 2** Chuẩn $\|A\|$ bằng *giá trị suy biến lớn nhất (largest singular value)* $\sigma_{\max}$ của $A$. Các giá trị suy biến $\sigma_1, \dots, \sigma_r$ là căn bậc hai của các trị riêng dương của $A^T A$. Vậy nên chắc chắn $\sigma_{\max} = (\lambda_{\max})^{1/2}$. Vì $U$ và $V$ là trực giao trong phân tích $A = U\Sigma V^T$, chuẩn là $\|A\| = \sigma_{\max}$.

### Số Điều kiện của $A$ (The Condition Number of $A$)

Phần 9.1 đã chỉ ra rằng sai số làm tròn có thể rất nghiêm trọng. Một số hệ thống rất nhạy cảm, một số khác thì không nhạy cảm bằng. Độ nhạy với sai số được đo bằng *số điều kiện*. Đây là chương đầu tiên trong cuốn sách chủ ý đưa ra các sai số. Chúng ta muốn ước tính xem chúng thay đổi $x$ bao nhiêu.

Phương trình gốc là $Ax = b$. Giả sử vế phải được đổi thành $b + \Delta b$ do làm tròn hoặc sai số đo lường. Khi đó giải pháp được đổi thành $x + \Delta x$. Mục tiêu của chúng ta là ước tính thay đổi $\Delta x$ trong nghiệm từ thay đổi $\Delta b$ trong phương trình. Phép trừ cho ra *phương trình sai số (error equation)* $A(\Delta x) = \Delta b$:
$$\text{Trừ } Ax = b \text{ từ } A(x + \Delta x) = b + \Delta b \text{ để tìm ra } A(\Delta x) = \Delta b. \quad (5)$$

Sai số là $\Delta x = A^{-1}\Delta b$. Nó sẽ lớn khi $A^{-1}$ lớn (khi đó $A$ gần như suy biến). Sai số $\Delta x$ đặc biệt lớn khi $\Delta b$ chỉ theo hướng xấu nhất — hướng bị khuếch đại nhiều nhất bởi $A^{-1}$. *Sai số tồi tệ nhất có* $\|\Delta x\| = \|A^{-1}\| \|\Delta b\|$.

Cận sai số (error bound) $\|A^{-1}\|$ này có một nhược điểm nghiêm trọng. Nếu ta nhân $A$ với 1000, thì $A^{-1}$ bị chia cho 1000. Ma trận trông có vẻ tốt hơn một nghìn lần. Nhưng một phép định tỷ lệ lại (rescaling) đơn giản không thể thay đổi thực tế của bài toán. Đúng là $\Delta x$ sẽ bị chia cho 1000, nhưng nghiệm chính xác $x = A^{-1}b$ cũng sẽ bị như vậy. *Sai số tương đối (relative error)* $\|\Delta x\|/\|x\|$ sẽ giữ nguyên. Chính sự thay đổi tương đối ở $x$ này mới là thứ cần được so sánh với sự thay đổi tương đối ở $b$.

Việc so sánh các sai số tương đối bây giờ sẽ dẫn đến "số điều kiện" $c = \|A\| \|A^{-1}\|$. Nhân $A$ với 1000 không làm thay đổi con số này, bởi vì $A^{-1}$ bị chia cho 1000 và số điều kiện $c$ vẫn giữ nguyên. Nó đo lường độ nhạy của $Ax = b$.

*Sai số nghiệm nhỏ hơn hoặc bằng $c = \|A\| \|A^{-1}\|$ lần sai số bài toán:*
$$\text{Số điều kiện } c \quad \frac{\|\Delta x\|}{\|x\|} \leq c \frac{\|\Delta b\|}{\|b\|}. \quad (6)$$

*Nếu sai số bài toán là $\Delta A$ (sai số ở $A$ thay vì ở $b$), thì $c$ vẫn kiểm soát $\Delta x$:*
$$\text{Sai số } \Delta A \text{ trong } A \quad \frac{\|\Delta x\|}{\|x + \Delta x\|} \leq c \frac{\|\Delta A\|}{\|A\|}. \quad (7)$$

**Chứng minh** Phương trình ban đầu là $b = Ax$. Phương trình sai số (5) là $\Delta x = A^{-1}\Delta b$. Áp dụng tính chất quan trọng $\|Ax\| \leq \|A\|\|x\|$ của chuẩn ma trận:
$$\|b\| \leq \|A\| \|x\| \quad \text{và} \quad \|\Delta x\| \leq \|A^{-1}\| \|\Delta b\|.$$
Nhân các vế trái với nhau để được $\|b\| \|\Delta x\|$, và nhân các vế phải để được $c\|x\| \|\Delta b\|$. Chia cả hai vế cho $\|b\| \|x\|$. Vế trái bây giờ là sai số tương đối $\|\Delta x\|/\|x\|$. Vế phải bây giờ là giới hạn trên trong phương trình (6).

Cùng một số điều kiện $c = \|A\| \|A^{-1}\|$ sẽ xuất hiện khi sai số nằm trong ma trận. Chúng ta có $\Delta A$ thay vì $\Delta b$ trong phương trình sai số:
Trừ $Ax = b$ từ $(A + \Delta A)(x + \Delta x) = b$ để tìm ra $A(\Delta x) = -(\Delta A)(x + \Delta x)$.
Nhân phương trình cuối với $A^{-1}$ và lấy các chuẩn để đi tới phương trình (7):
$$\|\Delta x\| \leq \|A^{-1}\| \|\Delta A\| \|x + \Delta x\| \quad \text{hoặc} \quad \frac{\|\Delta x\|}{\|x + \Delta x\|} \leq \|A\| \|A^{-1}\| \frac{\|\Delta A\|}{\|A\|}.$$

**Kết luận** Các sai số đi vào theo hai cách. Chúng bắt đầu với một sai số $\Delta A$ hoặc $\Delta b$ — một ma trận sai hoặc một vế phải $b$ sai. Sai số bài toán này được khuếch đại (nhiều hoặc ít) thành sai số nghiệm $\Delta x$. Sai số đó bị giới hạn, tương đối so với chính $x$, bởi số điều kiện $c$.

Sai số $\Delta b$ phụ thuộc vào việc làm tròn của máy tính và vào các phép đo lường ban đầu của $b$. Sai số $\Delta A$ cũng phụ thuộc vào các bước khử. Các phần tử trục nhỏ có xu hướng tạo ra các sai số lớn trong $L$ và $U$. Khi đó $L + \Delta L$ nhân với $U + \Delta U$ bằng $A + \Delta A$. Khi $\Delta A$ hoặc số điều kiện rất lớn, sai số $\Delta x$ có thể không thể chấp nhận được.

**Ví dụ 3** Khi $A$ là đối xứng, $c = \|A\| \|A^{-1}\|$ đến từ các trị riêng:
$$A = \begin{bmatrix} 6 & 0 \\ 0 & 2 \end{bmatrix} \text{ có chuẩn 6.} \quad A^{-1} = \begin{bmatrix} \frac{1}{6} & 0 \\ 0 & \frac{1}{2} \end{bmatrix} \text{ có chuẩn } \frac{1}{2}.$$
Ma trận $A$ này là đối xứng xác định dương. Chuẩn của nó là $\lambda_{\max} = 6$. Chuẩn của $A^{-1}$ là $1/\lambda_{\min} = \frac{1}{2}$. Nhân các chuẩn ta được số điều kiện $\|A\| \|A^{-1}\| = \lambda_{\max}/\lambda_{\min}$:
$$\text{Số điều kiện cho ma trận } A \text{ xác định dương} \quad c = \frac{\lambda_{\max}}{\lambda_{\min}} = \frac{6}{2} = 3.$$

**Ví dụ 4** Giữ nguyên ma trận $A$ này, với các trị riêng 6 và 2. Để làm cho $x$ nhỏ, hãy chọn $b$ dọc theo vectơ riêng thứ nhất $(1, 0)$. Để làm cho $\Delta x$ lớn, hãy chọn $\Delta b$ dọc theo vectơ riêng thứ hai $(0, 1)$. Khi đó $x = \frac{1}{6}b$ và $\Delta x = \frac{1}{2}\Delta b$. Tỷ số $\|\Delta x\|/\|x\|$ chính xác bằng $c = 3$ lần tỷ số $\|\Delta b\|/\|b\|$.

Điều này chứng tỏ rằng sai số xấu nhất được phép bởi số điều kiện $\|A\| \|A^{-1}\|$ thực sự có thể xảy ra. Đây là một quy tắc kinh nghiệm (rule of thumb) hữu ích, đã được kiểm chứng bằng thực nghiệm đối với phép khử Gauss: *Máy tính có thể mất $\log c$ chữ số thập phân vì sai số làm tròn.*

### **Tập bài tập 11.2 (Problem Set 11.2)**

**1** Tìm các chuẩn $\|A\| = \lambda_{\max}$ và số điều kiện $c = \lambda_{\max}/\lambda_{\min}$ của các ma trận xác định dương này:
| $\begin{bmatrix} .5 & 0 \\ 0 & 2 \end{bmatrix}$ | $\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$ | $\begin{bmatrix} 3 & 1 \\ 1 & 1 \end{bmatrix}$ |
|-------------------------------------------------|------------------------------------------------|------------------------------------------------|

**2** Tìm các chuẩn và các số điều kiện từ căn bậc hai của $\lambda_{\max}(A^T A)$ và $\lambda_{\min}(A^T A)$. Khi thiếu tính xác định dương ở $A$, chúng ta đi đến $A^T A$!
| $\begin{bmatrix} -2 & 0 \\ 0 & 2 \end{bmatrix}$ | $\begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}$ | $\begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix}$ |
|-------------------------------------------------|------------------------------------------------|-------------------------------------------------|

**3** Giải thích hai bất đẳng thức này từ các định nghĩa (3) của $\|A\|$ và $\|B\|$:
$$\|ABx\| \leq \|A\| \|Bx\| \leq \|A\| \|B\| \|x\|.$$
Từ tỷ số của $\|ABx\|$ với $\|x\|$, hãy suy ra rằng $\|AB\| \leq \|A\| \|B\|$. Đây là chìa khóa để sử dụng các chuẩn ma trận. Chuẩn của $A^n$ không bao giờ lớn hơn $\|A\|^n$.
**4** Sử dụng $\|AA^{-1}\| \leq \|A\| \|A^{-1}\|$ để chứng minh rằng số điều kiện ít nhất bằng 1.
**5** Tại sao $I$ là ma trận đối xứng xác định dương duy nhất có $\lambda_{\max} = \lambda_{\min} = 1$? Khi đó các ma trận khác duy nhất có $\|A\| = 1$ và $\|A^{-1}\| = 1$ phải có $A^T A = I$. Đó là các ma trận \_\_\_\_\_\_\_\_\_\_: có điều kiện hoàn hảo.
**6** Các ma trận trực giao có chuẩn $\|Q\| = 1$. Nếu $A = QR$ hãy chỉ ra rằng $\|A\| \leq \|R\|$ và cũng có $\|R\| \leq \|A\|$. Vậy thì $\|A\| = \|Q\| \|R\|$. Tìm một ví dụ về $A = LU$ với $\|A\| < \|L\| \|U\|$.
**7** (a) Bất đẳng thức nổi tiếng nào cho $\|(A + B)x\| \leq \|Ax\| + \|Bx\|$ với mọi $x$?
(b) Tại sao định nghĩa (3) của chuẩn ma trận dẫn đến $\|A + B\| \leq \|A\| + \|B\|$?
**8** Chỉ ra rằng nếu $\lambda$ là bất kỳ trị riêng nào của $A$, thì $|\lambda| \leq \|A\|$. Bắt đầu từ $Ax = \lambda x$.
**9** *"Bán kính phổ (spectral radius)"* $\rho(A) = |\lambda_{\max}|$ là giá trị tuyệt đối lớn nhất của các trị riêng. Hãy chỉ ra bằng các ví dụ $2 \times 2$ rằng cả $\rho(A + B) \leq \rho(A) + \rho(B)$ và $\rho(AB) \leq \rho(A)\rho(B)$ đều có thể *sai*. Bán kính phổ không được chấp nhận như một chuẩn.
**10** (a) Giải thích tại sao $A$ và $A^{-1}$ có cùng số điều kiện.
(b) Giải thích tại sao $A$ và $A^T$ có cùng chuẩn, dựa trên $\lambda(A^T A)$ và $\lambda(AA^T)$.
**11** Ướ ước lượng số điều kiện của ma trận có điều kiện xấu $A = \begin{bmatrix} 1 & 1 \\ 1 & 1.0001 \end{bmatrix}$.
**12** Tại sao định thức của $A$ không tốt để làm chuẩn? Tại sao nó không tốt để làm số điều kiện?
**13** (Gợi ý bởi C. Moler và C. Van Loan.) Tính $b - Ay$ và $b - Az$ khi
| $b = \begin{bmatrix} .217 \\ .254 \end{bmatrix}$ | $A = \begin{bmatrix} .780 & .563 \\ .913 & .659 \end{bmatrix}$ | $y = \begin{bmatrix} .341 \\ -.087 \end{bmatrix}$ | $z = \begin{bmatrix} .999 \\ -1.0 \end{bmatrix}$ |
|--------------------------------------------------|--------------------------------------------------|---------------------------------------------------|--------------------------------------------------|

Liệu $y$ có gần việc giải $Ax = b$ hơn $z$ không? Trả lời theo hai cách: So sánh *phần dư (residual)* $b - Ay$ với $b - Az$. Sau đó so sánh $y$ và $z$ với giá trị $x$ đúng bằng $(1, -1)$. Cả hai câu trả lời đều có thể đúng. Đôi khi chúng ta muốn có phần dư nhỏ, đôi khi là sai số $\Delta x$ nhỏ.
**14** (a) Tính định thức của $A$ trong Bài 13. Tính $A^{-1}$.
(b) Nếu có thể hãy tính $\|A\|$ và $\|A^{-1}\|$ và chỉ ra rằng $c > 10^6$.

**Các Bài 15–19 bàn về các chuẩn vectơ khác ngoài chuẩn thông thường $\|\mathbf{x}\| = \sqrt{\mathbf{x}^T \mathbf{x}}$.**

**15** "Chuẩn $\ell^1$" và "chuẩn $\ell^\infty$" của $x = (x_1, \dots, x_n)$ là
$$\|\mathbf{x}\|_1 = |x_1| + \cdots + |x_n| \quad \text{và} \quad \|\mathbf{x}\|_\infty = \max_{1 \leq i \leq n} |x_i|.$$
Tính các chuẩn $\|\mathbf{x}\|_1$ và $\|\mathbf{x}\|_\infty$ và $\|\mathbf{x}\|$ của hai vectơ này trong $\mathbf{R}^5$:
| $\mathbf{x} = (1, 1, 1, 1, 1)$ | $\mathbf{x} = (.1, .7, .3, .4, .5).$ |
|--------------------------------|--------------------------------------|

**16** Chứng minh rằng $\|\mathbf{x}\|_\infty \leq \|\mathbf{x}\| \leq \|\mathbf{x}\|_1$. Chứng minh từ bất đẳng thức Schwarz rằng các tỷ số $\|\mathbf{x}\|_1/\|\mathbf{x}\|_\infty$ và $\|\mathbf{x}\|_1/\|\mathbf{x}\|$ không bao giờ lớn hơn $\sqrt{n}$. Vectơ $(x_1, \dots, x_n)$ nào cho các tỷ số bằng $\sqrt{n}$?
**17** Mọi chuẩn vectơ đều phải thỏa mãn *bất đẳng thức tam giác.* Chứng minh rằng
| $\|\mathbf{x} + \mathbf{y}\|_\infty \leq \|\mathbf{x}\|_\infty + \|\mathbf{y}\|_\infty$ | và | $\|\mathbf{x} + \mathbf{y}\|_1 \leq \|\mathbf{x}\|_1 + \|\mathbf{y}\|_1$ |
|-----------------------------------------------------------------------------------------|-----|--------------------------------------------------------------------------|

**18** Các chuẩn vectơ cũng phải thỏa mãn $\|cx\| = |c| \|x\|$. Chuẩn phải luôn dương ngoại trừ khi $x = 0$. Những cái nào trong số này là chuẩn cho các vectơ $(x_1, x_2)$ trong $\mathbf{R}^2$?
$$\|\mathbf{x}\|_A = |x_1| + 2|x_2| \quad \|\mathbf{x}\|_B = \min (|x_1|, |x_2|)$$
| $\|\mathbf{x}\|_C = \|\mathbf{x}\| + \|\mathbf{x}\|_\infty$ | $\|\mathbf{x}\|_D = \|A\mathbf{x}\|$ | (câu trả lời này phụ thuộc vào $A$). |
|-------------------------------------------------------------|--------------------------------------|--------------------------------|

# **Các Bài toán Thử thách (Challenge Problems)**

**19** Chứng minh rằng $\mathbf{x}^T \mathbf{y} \leq \|\mathbf{x}\|_1 \|\mathbf{y}\|_\infty$ bằng cách chọn các thành phần $y_i = \pm 1$ để làm cho $\mathbf{x}^T \mathbf{y}$ lớn nhất có thể.
**20** Các trị riêng của ma trận hiệu (difference matrix) $-1, 2, -1$ $K$ là $\lambda = 2 - 2\cos(j\pi/(n+1))$. Ước tính $\lambda_{\min}$ và $\lambda_{\max}$ và $c = \text{cond}(K) = \lambda_{\max}/\lambda_{\min}$ khi $n$ tăng: $c \approx Cn^2$ với hằng số $C$ bằng bao nhiêu?
Kiểm tra ước lượng này với lệnh **eig(K)** và **cond(K)** cho $n = 10, 100, 1000$.

### **11.3 Các Phương pháp Lặp và Tiền điều kiện (Iterative Methods and Preconditioners)**

Cho đến nay, cách tiếp cận của chúng ta đối với hệ $Ax = b$ là trực tiếp. Chúng ta chấp nhận $A$ như khi nó đến. Chúng ta tấn công nó bằng phép khử với sự hoán đổi hàng. Bây giờ chúng ta xem xét **các phương pháp lặp, thay thế $A$ bằng một ma trận đơn giản hơn $S$**. Hiệu số $T = S - A$ được chuyển sang vế phải của phương trình. Bài toán trở nên dễ giải hơn, với $S$ thay vì $A$. Nhưng có một cái giá phải trả — *hệ thống đơn giản hơn phải được giải đi giải lại nhiều lần.*

Một phương pháp lặp rất dễ được phát minh ra. Chỉ cần chia nhỏ $A$ (một cách cẩn thận) thành $S - T$.
| <b>Viết lại <math display="block">Ax = b</math></b> | $Sx = Tx + b$ | (1) |
|----------------------------------------------------|--------------|-----|

Tính mới mẻ là giải (1) bằng phép lặp. Mỗi dự đoán $x_k$ dẫn đến $x_{k+1}$ tiếp theo:
| <b>Phép lặp thuần túy (Pure iteration)</b> | $Sx_{k+1} = Tx_k + \mathbf{b}$ | (2) |
|-----------------------|--------------------------------|-----|

Bắt đầu với bất kỳ $x_0$ nào. Sau đó giải $Sx_1 = Tx_0 + b$. Tiếp tục với $Sx_2 = Tx_1 + b$. Một trăm lần lặp là rất phổ biến — thường là nhiều hơn thế. Dừng lại khi (và nếu!) $x_{k+1}$ đủ gần với $x_k$ — hoặc khi **phần dư (residual)** $r_k = b - Ax_k$ gần bằng không. Hy vọng của chúng ta là tiến gần đến nghiệm đúng, nhanh hơn so với bằng phương pháp khử. Khi các $x_k$ hội tụ, giới hạn $x_\infty$ của chúng có giải phương trình (1): $Sx_\infty = Tx_\infty + b$ có nghĩa là $Ax_\infty = b$.

Hai mục tiêu của việc tách $A = S - T$ là *tốc độ mỗi bước* và *sự hội tụ nhanh*. Tốc độ của mỗi bước phụ thuộc vào $S$ và tốc độ hội tụ phụ thuộc vào $S^{-1}T$:
**1** Phương trình (2) phải dễ giải đối với $x_{k+1}$. *"Bộ tiền điều kiện (preconditioner)"* $S$ có thể là phần đường chéo hoặc phần ma trận tam giác của $A$. Một cách nhanh chóng là dùng $S = L_0U_0$, nơi các nhân tử đó có nhiều số không so với $A = LU$ chính xác. Đây là *"phép phân tích LU không hoàn chỉnh (incomplete LU)".*
**2** Độ chênh lệch $x - x_k$ (đây là sai số $e_k$) phải tiến nhanh về số 0. Lấy phương trình (1) trừ đi phương trình (2) sẽ triệt tiêu $b$, và để lại *phương trình cho sai số $e_k$:*
| Phương trình sai số (Error equation) | $Se_{k+1} = Te_k$ | có nghĩa là | $e_{k+1} = S^{-1}Te_k$ | (3) |
|----------------|-------------------|-------------|------------------------|-----|

Ở mỗi bước, sai số được nhân với $S^{-1}T$. Nếu $S^{-1}T$ nhỏ, thì lũy thừa của nó sẽ nhanh chóng tiến về không. Nhưng "nhỏ" là thế nào?

Sự phân tách cực đoan là $S = A$ và $T = 0$. Khi đó bước đầu tiên của vòng lặp là phương trình ban đầu $Ax = b$. Sự hội tụ là hoàn hảo và $S^{-1}T$ bằng không. Nhưng chi phí của bước đó là điều chúng ta muốn tránh. Việc chọn $S$ là một cuộc chiến giữa tốc độ mỗi bước (một ma trận $S$ đơn giản) và tốc độ hội tụ ($S$ gần với $A$). Dưới đây là một số lựa chọn cho $S$:
**J**  $S =$ phần đường chéo của $A$ (phép lặp được gọi là *phương pháp Jacobi*)
**GS** $S =$ phần tam giác dưới của $A$ bao gồm cả đường chéo (*phương pháp Gauss-Seidel*)
**ILU** $S =$ gần đúng của $L$ nhân gần đúng của $U$ (*phương pháp LU không hoàn chỉnh*)

Câu hỏi đầu tiên của chúng ta là đại số tuyến tính thuần túy: *Khi nào các $x_k$ hội tụ về $x$?* Câu trả lời hé lộ ra giá trị $|\lambda|_{\max}$ chi phối sự hội tụ. Trong các ví dụ về Jacobi và Gauss-Seidel, chúng ta sẽ tính *"bán kính phổ (spectral radius)"* $|\lambda|_{\max}$ này. Nó là trị riêng lớn nhất của *ma trận lặp $B = S^{-1}T$.*

# **Bán kính phổ $\rho(B)$ Kiểm soát Sự Hội tụ (The Spectral Radius $\rho(B)$ Controls Convergence)**

Phương trình (3) là $e_{k+1} = S^{-1}Te_k$. Mỗi bước lặp nhân sai số với cùng một ma trận $B = S^{-1}T$. Sai số sau $k$ bước là $e_k = B^ke_0$. *Sai số tiến đến không nếu các lũy thừa của $B = S^{-1}T$ tiến đến không.* Thật tuyệt vời khi thấy cách các trị riêng của $B$ — đặc biệt là trị riêng lớn nhất — kiểm soát các lũy thừa ma trận $B^k$.

Các lũy thừa $B^k$ tiến về không khi và chỉ khi mọi trị riêng của $B$ có $|\lambda| < 1$. *Tốc độ hội tụ được kiểm soát bởi bán kính phổ của $B$: $\rho = \max |\lambda(B)|$.*

*Thử nghiệm cho sự hội tụ là $|\lambda|_{\max} < 1$.* Trị riêng thực phải nằm giữa -1 và 1. Trị riêng phức $\lambda = a + ib$ phải có $|\lambda|^2 = a^2 + b^2 < 1$. Bán kính phổ "rho" là khoảng cách lớn nhất từ $0$ tới các trị riêng của $B = S^{-1}T$. Giá trị này là $\rho = |\lambda|_{\max}$.

Để thấy tại sao $|\lambda|_{\max} < 1$ là điều kiện cần thiết, giả sử sai số xuất phát $e_0$ tình cờ lại là một vectơ riêng của $B$. Sau một bước, sai số là $Be_0 = \lambda e_0$. Sau $k$ bước, sai số là $B^k e_0 = \lambda^k e_0$. Nếu chúng ta bắt đầu với một vectơ riêng, chúng ta tiếp tục với vectơ riêng đó — và *hệ số $\lambda^k$ chỉ tiến về không khi $|\lambda| < 1$.* Điều kiện này được yêu cầu đối với mọi trị riêng.

Để thấy tại sao $|\lambda|_{\max} < 1$ là đủ để sai số tiến đến không, giả sử $e_0$ là một tổ hợp của các vectơ riêng:
| $e_0 = c_1 x_1 + \dots + c_n x_n$ | dẫn đến | $e_k = c_1(\lambda_1)^k x_1 + \dots + c_n(\lambda_n)^k x_n$ | (4) |
|-----------------------------------|----------|-------------------------------------------------------------|--|

Đây chính là điểm cốt lõi của vectơ riêng! Khi chúng ta nhân với $B$, mỗi vectơ riêng $x_i$ được nhân với $\lambda_i$. Nếu tất cả $|\lambda_i| < 1$ thì phương trình (4) đảm bảo rằng $e_k$ tiến về không.
| Ví dụ 1 | $B = \begin{bmatrix} .6 & .5 \\ .6 & .5 \end{bmatrix}$ | có $\lambda_{\max} = 1.1$ | $B' = \begin{bmatrix} .6 & 1.1 \\ 0 & .5 \end{bmatrix}$ | có $\lambda_{\max} = .6$ |
|-----------|--------------------------------------------------------|----------------------------|---------------------------------------------------------|---------------------------|

$B^2$ bằng $1.1$ lần $B$. Khi đó $B^3$ bằng $(1.1)^2$ lần $B$. Lũy thừa của $B$ sẽ bùng nổ. Hãy đối chiếu với các lũy thừa của $B'$. Ma trận $(B')^k$ có $(.6)^k$ và $(.5)^k$ trên đường chéo của nó. Các phần tử ngoài đường chéo cũng chứa $\rho^k = (.6)^k$, giá trị thiết lập tốc độ hội tụ.

**Lưu ý** Khi có quá ít vectơ riêng, phương trình (4) không đúng. Chúng ta chuyển sang *dạng Jordan* khi thiếu các vectơ riêng và ma trận $B$ không thể chéo hóa được:
| Dạng Jordan (Jordan form) $J$ | $B = MJM^{-1}$ | và | $B^k = MJ^kM^{-1}$. | (5) |
|-----------------|----------------|-----|----------------------|-----|

Phần 8.3 chỉ ra cách $J$ và $J^k$ được tạo thành từ "các khối" với một trị riêng lặp lại:
| Các lũy thừa của một khối $2 \times 2$ trong $J$ là | $\begin{bmatrix} \lambda & 1 \\ 0 & \lambda \end{bmatrix}^k = \begin{bmatrix} \lambda^k & k\lambda^{k-1} \\ 0 & \lambda^k \end{bmatrix}$ |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|

Nếu $|\lambda| < 1$ thì các lũy thừa này tiến về không. Hệ số phụ $k$ từ một trị riêng kép bị lấn át bởi hệ số đang giảm dần $\lambda^{k-1}$. Điều này áp dụng cho mọi khối:

**Dù có thể chéo hóa hay không: Sự hội tụ $B^k \rightarrow 0$ và tốc độ của nó phụ thuộc vào $\rho = |\lambda|_{\max} < 1$.**

### Phương pháp Jacobi so với Gauss-Seidel

Bây giờ chúng ta giải một bài toán $2 \times 2$ cụ thể bằng cách phân tách $A$. Hãy chú ý đến con số $|\lambda|_{\max}$ đó.
$$Ax = b \quad \begin{array}{l} 2u - v = 4 \\ -u + 2v = -2 \end{array} \quad \text{có nghiệm} \quad \begin{bmatrix} u \\ v \end{bmatrix} = \begin{bmatrix} 2 \\ 0 \end{bmatrix}. \quad (6)$$

Sự phân tách đầu tiên là **phương pháp Jacobi**. Giữ lại *đường chéo* của $A$ ở vế trái (đây là $S$). Chuyển phần ngoài đường chéo của $A$ sang vế phải (đây là $T$). Sau đó lặp:
| <b>Phép lặp Jacobi (Jacobi iteration)</b> | $Sx_{k+1} = Tx_k + b$ | $\begin{array}{l} 2u_{k+1} = v_k + 4 \\ 2v_{k+1} = u_k - 2. \end{array}$ |
|-------------------------|-----------------------|--------------------------------------------------------------------------|

Bắt đầu từ $u_0 = v_0 = 0$. Bước đầu tiên tìm được $u_1 = 2$ và $v_1 = -1$. Tiếp tục:
$$\begin{bmatrix} 0 \\ 0 \end{bmatrix} \quad \begin{bmatrix} 2 \\ -1 \end{bmatrix} \quad \begin{bmatrix} 3/2 \\ 0 \end{bmatrix} \quad \begin{bmatrix} 2 \\ -1/4 \end{bmatrix} \quad \begin{bmatrix} 15/8 \\ 0 \end{bmatrix} \quad \begin{bmatrix} 2 \\ -1/16 \end{bmatrix} \quad \text{tiến về} \quad \begin{bmatrix} 2 \\ 0 \end{bmatrix}.$$

Điều này cho thấy sự hội tụ. Tại các bước 1, 3, 5, thành phần thứ hai là $-1, -1/4, -1/16$. Chúng giảm đi 4 lần sau mỗi hai bước. Phương trình sai số là $Se_{k+1} = Te_k$:
$$\text{Phương trình sai số} \quad \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} e_{k+1} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} e_k \quad \text{hay} \quad e_{k+1} = \begin{bmatrix} 0 & \frac{1}{2} \\ \frac{1}{2} & 0 \end{bmatrix} e_k. \quad (7)$$

Ma trận cuối cùng $S^{-1}T$ đó có các trị riêng là $\frac{1}{2}$ và $-\frac{1}{2}$. Vậy bán kính phổ của nó là $\rho(B) = \frac{1}{2}$:
$$B = S^{-1}T = \begin{bmatrix} 0 & \frac{1}{2} \\ \frac{1}{2} & 0 \end{bmatrix} \quad \text{có} \quad |\lambda|_{\max} = \frac{1}{2} \quad \text{và} \quad \begin{bmatrix} 0 & \frac{1}{2} \\ \frac{1}{2} & 0 \end{bmatrix}^2 = \begin{bmatrix} \frac{1}{4} & 0 \\ 0 & \frac{1}{4} \end{bmatrix}.$$

Hai bước nhân sai số chính xác với $\frac{1}{4}$, trong ví dụ đặc biệt này. Thông điệp quan trọng là đây: Phương pháp Jacobi hoạt động tốt khi đường chéo chính của $A$ lớn so với phần ngoài đường chéo. Phần đường chéo là $S$, phần còn lại là $-T$. Chúng ta muốn đường chéo chiếm ưu thế.

Trị riêng $\lambda = \frac{1}{2}$ là nhỏ bất thường. Mười vòng lặp giảm sai số đi $2^{10} = 1024$ lần. Điển hình hơn và tốn kém hơn là $|\lambda|_{\max} = .99$ hoặc $.999$.

**Phương pháp Gauss-Seidel** giữ lại toàn bộ phần tam giác dưới của $A$ làm $S$:
$$\begin{array}{lll} \text{Gauss-Seidel} & 2u_{k+1} & = v_k + 4 \\ & -u_{k+1} + 2v_{k+1} & = -2 \end{array} \quad \text{hay} \quad \begin{array}{l} u_{k+1} = \frac{1}{2}v_k + 2 \\ v_{k+1} = \frac{1}{2}u_{k+1} - 1. \end{array} \quad (8)$$

Hãy chú ý sự thay đổi. Giá trị $u_{k+1}$ mới từ phương trình đầu tiên được sử dụng *ngay lập tức* trong phương trình thứ hai. Với phương pháp Jacobi, chúng ta đã lưu lại $u_k$ cũ cho đến khi hoàn thành toàn bộ bước lặp. Với Gauss-Seidel, các giá trị mới được đưa vào ngay lập tức và $u_k$ cũ bị hủy. Điều này cắt giảm một nửa bộ nhớ. Nó cũng tăng tốc độ lặp (thường là vậy). Và nó không tốn kém hơn so với phương pháp Jacobi.

Kiểm tra vòng lặp bắt đầu từ một điểm khởi đầu khác $u_0 = 0$ và $v_0 = -1$:
| $\begin{bmatrix} 0 \\ -1 \end{bmatrix}$ | $\begin{bmatrix} 3/2 \\ -1/4 \end{bmatrix}$ | $\begin{bmatrix} 15/8 \\ -1/16 \end{bmatrix}$ | $\begin{bmatrix} 63/32 \\ -1/64 \end{bmatrix}$ | tiến về | $\begin{bmatrix} 2 \\ 0 \end{bmatrix}$ |
|-----------------------------------------|---------------------------------------------|-----------------------------------------------|------------------------------------------------|------------|----------------------------------------|

Các sai số ở thành phần thứ nhất là $2, 1/2, 1/8, 1/32$. Các sai số ở thành phần thứ hai là $-1, -1/4, -1/16, -1/32$. Chúng ta chia cho 4 trong một bước chứ không phải hai bước. *Gauss-Seidel nhanh gấp đôi so với Jacobi.* Chúng ta có $\rho_{GS} = (\rho_J)^2$ khi $A$ là ma trận ba đường chéo xác định dương:
| $S = \begin{bmatrix} 2 & 0 \\ -1 & 2 \end{bmatrix} \quad \text{và} \quad T = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} \quad \text{và} \quad S^{-1}T = \begin{bmatrix} 0 & \frac{1}{2} \\ 0 & \frac{1}{4} \end{bmatrix}.$ |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Các trị riêng của Gauss-Seidel là $0$ và $\frac{1}{4}$. Hãy so sánh với $\frac{1}{2}$ và $-\frac{1}{2}$ đối với Jacobi.

Chỉ cần thêm một chút nữa chúng ta có thể mô tả *phương pháp nới lỏng quá mức liên tiếp (successive overrelaxation method - SOR).* Ý tưởng mới là đưa thêm một tham số $\omega$ (omega) vào vòng lặp. Sau đó chọn con số $\omega$ này để làm cho bán kính phổ của $S^{-1}T$ nhỏ nhất có thể.

Viết lại $Ax = b$ thành $\omega Ax = \omega b$. Ma trận $S$ trong **SOR** có đường chéo giống như $A$ ban đầu, nhưng bên dưới đường chéo chúng ta sử dụng $\omega A$. Ở vế phải, $T$ là $S - \omega A$:
| SOR | $2u_{k+1} = (2 - 2\omega)u_k + \omega v_k + 4\omega$ \\ $-\omega u_{k+1} + 2v_{k+1} = (2 - 2\omega)v_k - 2\omega$ | (9) |
|-----|------------------------------------------------------------------------------------------------------------------------|-----|

Nghe có vẻ phức tạp hơn đối với chúng ta, nhưng máy tính vẫn chạy nhanh như thường. SOR giống như Gauss-Seidel, với một số $\omega$ có thể điều chỉnh. Giá trị $\omega$ tốt nhất làm cho nó chạy nhanh hơn.

Tôi sẽ ghi lại ma trận kiểm tra có giá trị nhất cỡ $n$. Đó là ma trận ba đường chéo $-1, 2, -1$ mang tên $K$ mà chúng ta yêu thích. Đường chéo là $2I$. Bên dưới và bên trên là các số $-1$. Ví dụ của chúng ta có $n = 2$, dẫn đến $\cos \frac{\pi}{3} = \frac{1}{2}$ với tư cách là trị riêng Jacobi tìm thấy ở trên. Đặc biệt lưu ý rằng giá trị $|\lambda|_{\max}$ này được bình phương đối với Gauss-Seidel:

Các phép phân tách ma trận $-1, 2, -1$ $K$ cỡ $n$ tạo ra các trị riêng này của $B$:
**Jacobi** ($S$ = ma trận $0, 2, 0$): $S^{-1}T$ có $|\lambda|_{\max} = \cos \frac{\pi}{n+1}$
**Gauss-Seidel** ($S$ = ma trận $-1, 2, 0$): $S^{-1}T$ có $|\lambda|_{\max} = \left( \cos \frac{\pi}{n+1} \right)^2$
**SOR** (với $\omega$ tốt nhất): $S^{-1}T$ có $|\lambda|_{\max} = \left( \cos \frac{\pi}{n+1} \right)^2 / \left( 1 + \sin \frac{\pi}{n+1} \right)^2$.

Cho tôi nói rõ: Đối với ma trận $-1, 2, -1$, bạn không nên sử dụng bất kỳ phương pháp lặp nào trong số này! Phép khử trên một ma trận ba đường chéo là rất nhanh (thu được $LU$ chính xác). Các vòng lặp được dành cho một ma trận thưa thớt lớn có các phần tử khác 0 nằm xa đường chéo trung tâm. Chúng tạo ra nhiều phần tử khác 0 hơn trong $L$ và $U$ chính xác. Sự lấp đầy (**fill-in**) này là lý do tại sao phép khử trở nên tốn kém.

Chúng ta đề cập thêm một phương pháp phân tách nữa. Ý tưởng của phép *"phân tích LU không hoàn chỉnh"* là đặt các phần tử khác 0 nhỏ trong $L$ và $U$ *trở về số không.* Điều này để lại các ma trận tam giác $L_0$ và $U_0$ vẫn mang tính thưa thớt. Việc phân tách có $S = L_0 U_0$ ở vế trái. Mỗi bước diễn ra nhanh chóng:
| LU không hoàn chỉnh (Incomplete LU) | $L_0 U_0 x_{k+1} = (L_0 U_0 - A)x_k + b.$ |
|---------------|----------------------------------------|

Ở vế phải, chúng ta thực hiện phép nhân ma trận-vectơ thưa. Đừng nhân $L_0$ với $U_0$, đó là những ma trận. Hãy nhân $x_k$ với $U_0$ và sau đó nhân vectơ thu được với $L_0$. Ở vế trái, chúng ta thực hiện phép thế tiến và thế ngược. Nếu $L_0 U_0$ gần với $A$, thì $|\lambda|_{\max}$ sẽ nhỏ. Một vài vòng lặp sẽ cho ra một câu trả lời sát nút.

# **Multigrid và Conjugate Gradients (Gradient Liên hợp)**

Tôi không thể để lại ấn tượng rằng Jacobi và Gauss-Seidel là những phương pháp tuyệt vời. Nhìn chung, phần "tần số thấp" của sai số suy giảm rất chậm và cần rất nhiều vòng lặp. Dưới đây là hai ý tưởng quan trọng mang lại sự cải thiện to lớn. Phương pháp đa lưới (**Multigrid**) có thể giải các bài toán cỡ $n$ trong $O(n)$ bước. Với một bộ tiền điều kiện tốt, gradient liên hợp (**conjugate gradients**) trở thành một trong những thuật toán phổ biến và mạnh mẽ nhất trong đại số tuyến tính số.

*Multigrid* Giải quyết các vấn đề nhỏ hơn với các lưới thô hơn. Mỗi vòng lặp sẽ rẻ hơn và nhanh hơn. Sau đó nội suy giữa các giá trị lưới thô để có được một khởi đầu nhanh chóng đối với bài toán kích thước đầy đủ. Multigrid có thể đi xuống 4 cấp độ và quay trở lại.

*Gradient liên hợp (Conjugate gradients)* Một vòng lặp thông thường như $x_{k+1} = x_k - Ax_k + b$ liên quan đến phép nhân với $A$ ở mỗi bước. Nếu $A$ là ma trận thưa, điều này không quá tốn kém: $Ax_k$ là việc chúng ta sẵn sàng làm. Nó bổ sung thêm một vectơ cơ sở vào "không gian Krylov" đang phát triển, nơi chứa các kết quả xấp xỉ của chúng ta. Nhưng $x_{k+1}$ **không phải là tổ hợp tốt nhất** của $x_0, Ax_0, \dots, A^k x_0$. Các vòng lặp thông thường thì đơn giản nhưng khác xa so với tối ưu.

Phương pháp gradient liên hợp chọn **tổ hợp tốt nhất** $x_k$ tại mọi bước. Chi phí tăng thêm (ngoài một phép nhân với $A$) là không lớn. Chúng ta sẽ đưa ra các bước lặp CG, nhấn mạnh rằng phương pháp này được tạo ra cho một *ma trận đối xứng xác định dương.* Khi $A$ không đối xứng, một lựa chọn tốt là GMRES. Khi $A = A^T$ không xác định dương, có MINRES. Cả một thế giới của các phương pháp lặp năng lực cao đã được tạo ra xoay quanh ý tưởng đưa ra những lựa chọn tối ưu cho mỗi $x_k$ tiếp theo.

Sách giáo khoa *Computational Science and Engineering* của tôi mô tả multigrid và CG chi tiết hơn nhiều. Trong số các cuốn sách về đại số tuyến tính số, cuốn Trefethen-Bau rất phổ biến (những cuốn khác cũng rất tuyệt vời). Cuốn Golub-Van Loan thì ở một trình độ cao hơn.

Tập bài tập tái hiện lại năm bước trong mỗi chu kỳ gradient liên hợp từ $x_{k-1}$ tới $x_k$. Chúng ta tính giá trị xấp xỉ mới $x_k$, phần dư mới $r_k = b - Ax_k$, và hướng tìm kiếm mới $d_k$ để tiếp tục dò $x_{k+1}$ tiếp theo.

Tôi đã viết các bước đó cho ma trận $A$ ban đầu. Nhưng một **bộ tiền điều kiện** $S$ có thể làm cho sự hội tụ diễn ra nhanh hơn nhiều. Phương trình ban đầu của chúng ta là $Ax = b$. Phương trình được tiền điều kiện là $S^{-1}Ax = S^{-1}b$. Những thay đổi nhỏ trong mã lệnh sẽ tạo ra *phương pháp gradient liên hợp tiền điều kiện (preconditioned conjugate gradient method) — một phương pháp lặp hàng đầu để giải các hệ thống xác định dương.*

Đối thủ lớn nhất là phương pháp khử trực tiếp, với các phương trình được sắp xếp lại để tận dụng tối đa lợi thế của các số 0 trong $A$. Đánh bại Gauss là điều không hề dễ dàng.

## Các Phương pháp Lặp đối với Trị riêng (Iterative Methods for Eigenvalues)

Chúng ta chuyển từ $Ax = b$ sang $Ax = \lambda x$. Các phép lặp là một lựa chọn đối với các phương trình tuyến tính. Chúng là điều kiện bắt buộc đối với các bài toán trị riêng. Trị riêng của một ma trận $n \times n$ là nghiệm của một đa thức bậc $n$. Định thức của $A - \lambda I$ bắt đầu bằng $(-\lambda)^n$. Cuốn sách này không được phép để lại ấn tượng rằng các trị riêng nên được tính theo cách đó! Việc làm việc từ $\det(A - \lambda I) = 0$ là một *cách tiếp cận rất tồi* — ngoại trừ khi $n$ nhỏ.

Với $n > 4$, không có công thức nào để giải $\det(A - \lambda I) = 0$. Tệ hơn nữa, các $\lambda$ có thể rất không ổn định và nhạy cảm. Tốt hơn nhiều là nên làm việc với chính $A$, dần dần biến nó thành ma trận đường chéo hoặc tam giác. (Khi đó các trị riêng sẽ xuất hiện trên đường chéo.) Có sẵn các mã máy tính tốt trong thư viện LAPACK — các chương trình con đơn lẻ được cung cấp miễn phí trên [www.netlib.org/lapack](http://www.netlib.org/lapack). Thư viện này kết hợp các phiên bản LINPACK và EISPACK trước đó, với nhiều cải tiến (để sử dụng các phép toán ma trận-ma trận trong Cấp độ 3 BLAS). Nó là một tập hợp các chương trình Fortran 77 cho đại số tuyến tính trên các máy tính hiệu suất cao. Đối với máy tính của bạn và của tôi, một gói ma trận chất lượng cao là tất cả những gì chúng ta cần. Đối với các siêu máy tính có tính năng xử lý song song, hãy chuyển sang ScaLAPACK và phương pháp khử khối (block elimination).

Chúng ta sẽ thảo luận ngắn gọn về phương pháp lũy thừa và phương pháp $QR$ (được chọn bởi LAPACK) để tính các trị riêng. Không có ý nghĩa gì khi đưa ra chi tiết đầy đủ của các mã lệnh.

**1 Các phương pháp lũy thừa (Power methods) và phương pháp lũy thừa nghịch đảo (inverse power methods).** Bắt đầu với bất kỳ vectơ $u_0$ nào. Nhân với $A$ để tìm $u_1$. Nhân với $A$ một lần nữa để tìm $u_2$. Nếu $u_0$ là tổ hợp của các vectơ riêng, thì $A$ sẽ nhân từng vectơ riêng $x_i$ với $\lambda_i$. Sau $k$ bước chúng ta có $(\lambda_i)^k$:
$$u_k = A^k u_0 = c_1(\lambda_1)^k x_1 + \cdots + c_n(\lambda_n)^k x_n. \quad (10)$$

Khi phương pháp lũy thừa tiếp tục, *trị riêng lớn nhất bắt đầu thống trị*. Các vectơ $u_k$ hướng về vectơ riêng chiếm ưu thế $x_1$ đó. Chúng ta đã thấy điều này đối với các ma trận Markov:
$$A = \begin{bmatrix} .9 & .3 \\ .1 & .7 \end{bmatrix} \quad \text{có} \quad \lambda_{\max} = 1 \quad \text{với vectơ riêng} \quad \begin{bmatrix} .75 \\ .25 \end{bmatrix}.$$
Bắt đầu với $u_0$ và nhân với $A$ ở mỗi bước:
$$u_0 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad u_1 = \begin{bmatrix} .9 \\ .1 \end{bmatrix}, \quad u_2 = \begin{bmatrix} .84 \\ .16 \end{bmatrix} \quad \text{đang tiến về} \quad u_\infty = \begin{bmatrix} .75 \\ .25 \end{bmatrix}.$$

Tốc độ hội tụ phụ thuộc vào *tỷ số* của trị riêng lớn thứ hai $\lambda_2$ so với trị riêng lớn nhất $\lambda_1$. Chúng ta không muốn $\lambda_1$ nhỏ, chúng ta muốn $\lambda_2/\lambda_1$ nhỏ. Ở đây $\lambda_2 = .6$ và $\lambda_1 = 1$, cho một tốc độ tốt. Đối với các ma trận lớn, thường xảy ra trường hợp $|\lambda_2/\lambda_1|$ rất gần với 1. Khi đó phương pháp lũy thừa quá chậm.

Có cách nào để tìm trị riêng *nhỏ nhất* — cái thường quan trọng nhất trong các ứng dụng không? Có, bằng phương pháp lũy thừa *nghịch đảo*: Nhân $u_0$ với $A^{-1}$ thay vì $A$. Vì chúng ta không bao giờ muốn tính $A^{-1}$, chúng ta thực sự giải $Au_1 = u_0$. Bằng cách lưu lại các nhân tử $LU$, bước tiếp theo $Au_2 = u_1$ diễn ra nhanh chóng. Bước $k$ giải hệ $Au_k = u_{k-1}$:

**Phương pháp lũy thừa nghịch đảo (Inverse power method)**
$$u_k = A^{-k} u_0 = \frac{c_1 x_1}{(\lambda_1)^k} + \cdots + \frac{c_n x_n}{(\lambda_n)^k}. \quad (11)$$

Bây giờ trị riêng *nhỏ nhất* $\lambda_{\min}$ đang nắm quyền kiểm soát. Khi nó rất nhỏ, hệ số $1/\lambda_{\min}^k$ sẽ lớn. Để đạt tốc độ cao, chúng ta làm cho $\lambda_{\min}$ nhỏ hơn nữa bằng cách tịnh tiến ma trận thành $A - \lambda^* I$.

Phép tịnh tiến đó không làm thay đổi các vectơ riêng. ($\lambda^*$ có thể lấy từ đường chéo của $A$, tốt hơn nữa là một thương số Rayleigh $x^T A x / x^T x$). Nếu $\lambda^*$ gần với $\lambda_{\min}$ thì $(A - \lambda^* I)^{-1}$ có trị riêng rất lớn $(\lambda_{\min} - \lambda^*)^{-1}$. Mỗi *bước lũy thừa nghịch đảo được dịch chuyển* nhân vectơ riêng với số lớn này, và vectơ riêng đó sẽ nhanh chóng thống trị.

**2 Phương pháp QR (The QR Method)** Đây là một thành tựu lớn trong đại số tuyến tính số. Sáu mươi năm trước, các phép tính trị riêng diễn ra chậm và không chính xác. Chúng ta thậm chí còn không nhận ra rằng giải $\det(A - \lambda I) = 0$ là một phương pháp tồi. Jacobi trước đó đã gợi ý rằng $A$ nên dần dần được chuyển thành dạng tam giác — khi đó các trị riêng sẽ tự động xuất hiện trên đường chéo. Ông đã sử dụng các phép quay $2 \times 2$ để tạo ra các số 0 ngoài đường chéo. (Thật không may, các số 0 trước đó có thể trở lại thành một số khác 0. Nhưng phương pháp của Jacobi đã có sự trở lại một phần với các máy tính song song). *Phương pháp QR* hiện là phương pháp dẫn đầu trong các phép tính trị riêng.

Bước cơ bản là phân tích ma trận $A$, ma trận mà chúng ta muốn có các trị riêng, thành $QR$. Hãy nhớ từ quá trình Gram-Schmidt (Phần 4.4) rằng $Q$ có các cột trực chuẩn và $R$ là ma trận tam giác. Đối với các trị riêng, ý tưởng then chốt là: *Đảo ngược vị trí của Q và R*. Ma trận mới (có cùng các $\lambda$) là $A_1 = RQ$. Các trị riêng không thay đổi trong $RQ$ bởi vì $A = QR$ đồng dạng với $A_1 = Q^{-1} AQ$:
$$A_1 = RQ \text{ có cùng các } \lambda \quad QRx = \lambda x \quad \text{cho ra} \quad RQ(Q^{-1}x) = \lambda(Q^{-1}x). \quad (12)$$

Quá trình này tiếp tục. Phân tích ma trận mới $A_1$ thành $Q_1 R_1$. Sau đó đảo ngược các nhân tử thành $R_1 Q_1$. Đây là ma trận đồng dạng $A_2$ và một lần nữa không có sự thay đổi nào về các trị riêng. Điều ngạc nhiên là, các trị riêng đó bắt đầu xuất hiện trên đường chéo. Không lâu sau, phần tử cuối cùng của $A_4$ đã giữ một trị riêng chính xác. Trong trường hợp đó, chúng ta loại bỏ hàng và cột cuối cùng và tiếp tục với một ma trận nhỏ hơn để tìm ra trị riêng tiếp theo.

Hai ý tưởng bổ sung khiến phương pháp này thành công. Một là tịnh tiến ma trận theo một bội số của $I$, trước khi phân tích thành $QR$. Khi đó $RQ$ được tịnh tiến trở lại để tạo ra $A_{k+1}$:
Phân tích $A_k - c_k I$ thành $Q_k R_k$. Ma trận tiếp theo là $A_{k+1} = R_k Q_k + c_k I$.
$A_{k+1}$ có cùng các trị riêng với $A_k$, và giống như ma trận ban đầu $A_0 = A$. Một phép dịch chuyển tốt sẽ chọn $c$ ở gần một trị riêng (chưa biết). Trị riêng đó xuất hiện chính xác hơn trên đường chéo của $A_{k+1}$ — điều này cho chúng ta biết một số $c$ tốt hơn cho bước tiếp theo tới $A_{k+2}$.

Ý tưởng thứ hai là lấy được các số không ngoài đường chéo trước khi phương pháp $QR$ bắt đầu. Một bước khử $E$ sẽ làm được việc đó, hoặc một phép quay Givens, nhưng đừng quên $E^{-1}$ (nếu không $\lambda$ sẽ thay đổi):
$$EAE^{-1} = \begin{bmatrix} 1 & & \\ & 1 & \\ & & -1 \\ & & & 1 \end{bmatrix} \begin{bmatrix} 1 & 2 & 3 \\ 1 & 4 & 5 \\ 1 & 6 & 7 \end{bmatrix} \begin{bmatrix} 1 & & \\ & 1 & \\ & & 1 \\ 1 & & 1 \end{bmatrix} = \begin{bmatrix} 1 & 5 & 3 \\ 1 & 9 & 5 \\ 0 & 4 & 2 \end{bmatrix}. \text{ Cùng các } \lambda.$$

Chúng ta phải giữ lại các số khác 0 gồm 1 và 4 dọc theo *một đường chéo phụ (subdiagonal)*. Các phép $E$ thêm nữa có thể loại bỏ chúng, nhưng $E^{-1}$ sẽ điền chúng trở lại. Đây là "ma trận Hessenberg" (một đường chéo phụ khác 0). Các số 0 ở góc dưới cùng bên trái sẽ vẫn là số 0 xuyên suốt phương pháp $QR$. Số lượng phép toán đối với mỗi phép phân tách $QR$ giảm từ $O(n^3)$ xuống $O(n^2)$.

Golub và Van Loan đưa ra ví dụ này về một bước $QR$ dịch chuyển trên một ma trận Hessenberg. Phép dịch chuyển là $7I$, trừ 7 từ tất cả các phần tử trên đường chéo của $A$ (sau đó cộng trở lại đối với $A_1$):
$$A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 0 & .001 & 7 \end{bmatrix} \quad \text{dẫn tới} \quad A_1 = \begin{bmatrix} -.54 & 1.69 & 0.835 \\ .31 & 6.53 & -6.656 \\ 0 & .00002 & 7.012 \end{bmatrix}.$$

Việc phân tích $A - 7I$ thành $QR$ cho ra $A_1 = RQ + 7I$. Hãy chú ý đến con số rất nhỏ $.00002$. Phần tử đường chéo $7.012$ gần như là một trị riêng chính xác của $A_1$, và do đó cũng là của $A$. Một bước $QR$ khác trên $A_1$ với mức dịch chuyển $7.012I$ sẽ mang lại độ chính xác tuyệt vời.

Để tìm một vài trị riêng của một ma trận thưa thớt lớn, tôi sẽ tìm đến **ARPACK**. Các bài toán 25-27 mô tả phép lặp Arnoldi chuyên thực hiện việc trực giao hóa cơ sở — mỗi bước chỉ có ba số hạng khi $A$ là đối xứng. Ma trận sẽ trở thành ma trận *ba đường chéo (tridiagonal)*: một sự khởi đầu tuyệt vời để tính toán các trị riêng.

# **Tập bài tập 11.3 (Problem Set 11.3)**

**Các Bài 1–12 nói về các phương pháp lặp cho $Ax = b$.**

**1** Thay đổi $Ax = b$ thành $x = (I - A)x + b$. $S$ và $T$ cho phép phân tách này là gì? Ma trận $S^{-1}T$ nào kiểm soát sự hội tụ của $x_{k+1} = (I - A)x_k + b$?
**2** Nếu $\lambda$ là một trị riêng của $A$, thì \_\_\_\_\_\_\_ là một trị riêng của $B = I - A$. Các trị riêng thực của $B$ có giá trị tuyệt đối nhỏ hơn 1 nếu các trị riêng thực của $A$ nằm giữa \_\_\_\_\_\_\_ và \_\_\_\_\_\_\_.
**3** Hãy chỉ ra tại sao vòng lặp $x_{k+1} = (I - A)x_k + b$ không hội tụ đối với $A = \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}$.
**4** Tại sao chuẩn của $B^k$ không bao giờ lớn hơn $\|B\|^k$? Khi đó $\|B\| < 1$ đảm bảo rằng các lũy thừa $B^k$ tiến đến không (sự hội tụ). Không có gì ngạc nhiên vì $|\lambda|_{\max}$ ở dưới $\|B\|$.
**5** Nếu $A$ bị suy biến thì mọi phép phân tách $A = S - T$ đều phải thất bại. Từ $Ax = 0$ hãy chỉ ra rằng $S^{-1}Tx = x$. Vì vậy ma trận $B = S^{-1}T$ này có $\lambda = 1$ và gặp thất bại.
**6** Thay đổi các số 2 thành số 3 và tìm các trị riêng của $S^{-1}T$ đối với phương pháp Jacobi:
$$Sx_{k+1} = Tx_k + b \quad \text{là} \quad \begin{bmatrix} 3 & 0 \\ 0 & 3 \end{bmatrix} x_{k+1} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} x_k + b.$$
**7** Tìm các trị riêng của $S^{-1}T$ cho phương pháp Gauss-Seidel áp dụng vào Bài 6:
| $\begin{bmatrix} 3 & 0 \\ -1 & 3 \end{bmatrix} x_{k+1} = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} x_k + b.$ |
|-----------------------------------------------------------------------------------------------------------------|

**8** Đối với bất kỳ ma trận $2 \times 2$ $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$ nào, hãy chỉ ra rằng $|\lambda|_{\max}$ bằng $|bc/ad|$ đối với Gauss-Seidel và $|bc/ad|^{1/2}$ đối với Jacobi. Chúng ta cần $ad \neq 0$ để ma trận $S$ có thể nghịch đảo được.
**9** Viết một mã máy tính (MATLAB hoặc phần mềm khác) cho phương pháp Gauss-Seidel. Bạn có thể định nghĩa $S$ và $T$ từ $A$, hoặc thiết lập vòng lặp trực tiếp từ các phần tử $a_{ij}$. Hãy kiểm tra nó trên các ma trận $-1, 2, -1$ $A$ cỡ $10, 20, 50$ với $b = (1, 0, \dots, 0)$.
**10** Vòng lặp Gauss-Seidel tại thành phần $i$ sử dụng các thành phần sớm hơn của $x^{\text{new}}$:
$$\text{Gauss-Seidel} \quad x_i^{\text{new}} = x_i^{\text{old}} + \frac{1}{a_{ii}} \left( b_i - \sum_{j=1}^{i-1} a_{ij} x_j^{\text{new}} - \sum_{j=1}^n a_{ij} x_j^{\text{old}} \right).$$
Nếu mọi $x_i^{\text{new}} = x_i^{\text{old}}$ thì điều này cho thấy giải pháp $x$ chính xác như thế nào? Công thức thay đổi ra sao đối với phương pháp Jacobi? Đối với SOR, hãy chèn $\omega$ ra ngoài dấu ngoặc.
**11** Chia phương trình (10) cho $\lambda_1^k$ và giải thích tại sao $|\lambda_2/\lambda_1|^k$ kiểm soát sự hội tụ của phương pháp lũy thừa. Xây dựng một ma trận $A$ mà ở đó phương pháp này *không hội tụ*.
**12** Ma trận Markov $A = \begin{bmatrix} .9 & .3 \\ .1 & .7 \end{bmatrix}$ có $\lambda = 1$ và $.6$, và phương pháp lũy thừa $u_k = A^k u_0$ hội tụ về $\begin{bmatrix} .75 \\ .25 \end{bmatrix}$. Tìm các vectơ riêng của $A^{-1}$. Phương pháp lũy thừa nghịch đảo $u_{-k} = A^{-k} u_0$ hội tụ về cái gì (sau khi bạn nhân với $.6^k$)?
**13** Ma trận ba đường chéo cỡ $n - 1$ với các đường chéo $-1, 2, -1$ có các trị riêng $\lambda_j = 2 - 2\cos(j\pi/n)$. Tại sao các trị riêng nhỏ nhất xấp xỉ $(j\pi/n)^2$? Phương pháp lũy thừa nghịch đảo hội tụ ở tốc độ $\lambda_1/\lambda_2 \approx 1/4$.
**14** Đối với $A = \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}$ áp dụng phương pháp lũy thừa $u_{k+1} = Au_k$ ba lần, bắt đầu với $u_0 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$. Phương pháp lũy thừa đang hội tụ tới vectơ riêng nào?
**15** Đối với ma trận $-1, 2, -1$ $A$, áp dụng phương pháp lũy thừa *nghịch đảo* $u_{k+1} = A^{-1}u_k$ ba lần với cùng một $u_0$. Các $u_k$ đang tiến tới vectơ riêng nào?
**16** Trong phương pháp $QR$ đối với trị riêng khi $A$ được tịnh tiến để khiến $A_{22} = 0$, chỉ ra rằng phần tử ở vị trí $(2, 1)$ giảm từ $\sin \theta$ ở $A = QR$ xuống $-\sin^3 \theta$ ở $RQ$. (Hãy tính $R$ và $RQ$.) Sự "hội tụ bậc ba (cubic convergence)" này làm cho phương pháp thành công:
$$A = \begin{bmatrix} \cos \theta & \sin \theta \\ \sin \theta & 0 \end{bmatrix} = QR = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} 1 & ? \\ 0 & ? \end{bmatrix}$$
**17** Nếu $A$ là ma trận trực giao, phép phân tách $QR$ của nó có $Q =$ \_\_\_\_\_\_\_ và $R =$ \_\_\_\_\_\_\_. Suy ra $RQ =$ \_\_\_\_\_\_\_. Đây là một trong những ví dụ hiếm hoi mà phương pháp $QR$ không đi đến đâu.
**18** Phương pháp $QR$ được tịnh tiến phân tích $A - cI$ thành $QR$. Chỉ ra rằng ma trận tiếp theo $A_1 = RQ + cI$ bằng $Q^{-1}AQ$. Vì vậy $A_1$ có các trị riêng \_\_\_\_\_\_\_\_ như $A$ (nhưng $A_1$ gần với dạng tam giác hơn).
**19** Khi $A = A^T$, "phương pháp Lanczos" tìm ra các giá trị $a$ và $b$ cùng các $q$ trực chuẩn sao cho $Aq_j = b_{j-1}q_{j-1} + a_jq_j + b_jq_{j+1}$ (với $q_0 = \mathbf{0}$). Nhân với $q_j^T$ để tìm một công thức cho $a_j$. Phương trình nói rằng $AQ = QT$ với $T$ là một ma trận ba đường chéo.
**20** Phương trình trong Bài 19 phát triển từ vòng lặp này với $b_0 = 1$ và $r_0 =$ bất kỳ $q_1$ nào:
$$q_{j+1} = r_j/b_j; \quad j = j+1; \quad a_j = q_j^T Aq_j; \quad r_j = Aq_j - b_{j-1}q_{j-1} - a_jq_j; \quad b_j = \|r_j\|.$$
Hãy viết một đoạn mã và kiểm tra nó trên ma trận $-1, 2, -1$ $A$. $Q^T Q$ nên bằng $I$.

**21** Giả sử $A$ là ma trận *ba đường chéo và đối xứng trong phương pháp QR*. Từ $A_1 = Q^{-1}AQ$ hãy chỉ ra rằng $A_1$ là đối xứng. Viết $A_1 = RAR^{-1}$ để chứng tỏ rằng $A_1$ cũng là ma trận ba đường chéo. (Nếu phần dưới của $A_1$ được chứng minh là ba đường chéo thì theo tính đối xứng phần trên cũng vậy). Các ma trận ba đường chéo đối xứng là cách tốt nhất để bắt đầu trong phương pháp QR.

**Các Bài toán 22–25 trình bày hai phép lặp cơ bản. Mỗi bước liên quan đến $Aq$ hoặc $Ad$.**

**Điểm mấu chốt đối với các ma trận lớn là phép nhân ma trận-vectơ diễn ra nhanh hơn nhiều so với phép nhân ma trận-ma trận.** Một cấu trúc quan trọng bắt đầu bằng một vectơ $b$. Phép nhân lặp lại sẽ tạo ra $Ab$, $A^2b$, $\dots$ nhưng những vectơ đó khác xa với trực giao. **Phép lặp Arnoldi ("Arnoldi iteration")** tạo ra một cơ sở trực chuẩn $q_1, q_2, \dots$ cho cùng một không gian bằng ý tưởng Gram-Schmidt: *trực giao hóa mỗi $Aq_n$ mới theo các vectơ $q_1, \dots, q_{n-1}$ trước đó*. "Không gian Krylov" sinh bởi $b$, $Ab$, $\dots$, $A^{n-1}b$ khi đó có một cơ sở tốt hơn nhiều là $q_1, \dots, q_n$.

Dưới đây, ở dạng mã giả (pseudocode), là hai trong số các thuật toán quan trọng nhất trong đại số tuyến tính số: Arnoldi mang lại một cơ sở tốt và CG đưa ra một ước lượng tốt cho $x = A^{-1}b$.
| <b>Phép lặp Arnoldi (Arnoldi Iteration)</b>                                                                                                                                                                                 | <b>Phép lặp Gradient Liên hợp cho <math>A</math> Xác định Dương (Conjugate Gradient Iteration for Positive Definite <math>A</math>)</b>                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| $q_1 = b/\|b\|$<br><b>for</b> $n = 1$ <b>to</b> $N - 1$<br>$v = Aq_n$<br><b>for</b> $j = 1$ <b>to</b> $n$<br>$h_{jn} = q_j^T v$<br>$v = v - h_{jn}q_j$<br>$h_{n+1,n} = \|v\|$<br>$q_{n+1} = v/h_{n+1,n}$ | $x_0 = 0, r_0 = b, d_0 = r_0$<br><b>for</b> $n = 1$ <b>to</b> $N$<br>$\alpha_n = (r_{n-1}^T r_{n-1})/(d_{n-1}^T Ad_{n-1})$ độ dài bước đi (step length) $x_{n-1}$ tới $x_n$<br>$x_n = x_{n-1} + \alpha_n d_{n-1}$ nghiệm gần đúng (approximate solution)<br>$r_n = r_{n-1} - \alpha_n Ad_{n-1}$ phần dư mới (new residual) $b - Ax_n$<br>$\beta_n = (r_n^T r_n)/(r_{n-1}^T r_{n-1})$ sự cải thiện bước này (improvement this step)<br>$d_n = r_n + \beta_n d_{n-1}$ hướng tìm kiếm tiếp theo (next search direction)<br>% Chú ý: chỉ 1 phép nhân ma trận-vectơ $Aq$ và $Ad$ |

Đối với các gradient liên hợp, các phần dư $r_n$ là trực giao và các hướng tìm kiếm là trực giao với $A$ ($A$-orthogonal): tất cả các $d_j^T Ad_k = 0$. Vòng lặp giải $Ax = b$ bằng cách thu nhỏ tối đa sai số $e^T Ae$ trên mọi vectơ trong *không gian Krylov* = nhịp (span) của $b$, $Ab$, $\dots$, $A^{n-1}b$. Đây là một thuật toán tuyệt vời.

**22** Đối với ma trận đường chéo $A = \text{diag}([1 \ 2 \ 3 \ 4])$ và vectơ $b = (1, 1, 1, 1)$, hãy thực hiện một bước Arnoldi để tìm các vectơ trực chuẩn $q_1$ và $q_2$.
**23** Phương pháp của Arnoldi là tìm $Q$ sao cho $AQ = QH$ (theo từng cột một):
$$AQ = \begin{bmatrix} Aq_1 & \cdots & Aq_N \end{bmatrix} = \begin{bmatrix} q_1 & \cdots & q_N \end{bmatrix} \begin{bmatrix} h_{11} & h_{12} & \cdot & h_{1N} \\ h_{21} & h_{22} & \cdot & h_{2N} \\ 0 & h_{32} & \cdot & \cdot \\ 0 & 0 & \cdot & h_{NN} \end{bmatrix} = QH$$
$H$ là một "ma trận Hessenberg" với một đường chéo phụ (subdiagonal) khác không. Đây là sự thật cốt lõi khi $A$ là đối xứng: *Ma trận Hessenberg $H = Q^{-1}AQ = Q^T AQ$ là ma trận đối xứng và do đó nó là ma trận ba đường chéo.* Giải thích câu đó.
**24** Ma trận ba đường chéo $H$ này (khi $A$ là đối xứng) tạo ra **phép lặp Lanczos (Lanczos iteration):**
**Chỉ ba số hạng**     
$$q_{j+1} = (Aq_j - h_{j,j}q_j - h_{j-1,j}q_{j-1})/h_{j+1,j}$$
Từ $H = Q^{-1}AQ$, tại sao các trị riêng của $H$ lại giống với các trị riêng của $A$? Đối với các ma trận lớn, "phương pháp Lanczos" tính toán các trị riêng đứng đầu bằng cách dừng lại ở một ma trận ba đường chéo $H_k$ nhỏ hơn. Phương pháp $QR$ trong tài liệu được áp dụng để tính toán các trị riêng của $H_k$.
**25** Áp dụng phương pháp gradient liên hợp để giải $Ax = b =$ **ones(100, 1)**, trong đó $A$ là ma trận hiệu bậc hai $-1, 2, -1$ $A =$ **toeplitz([2 -1 zeros(1, 98)])**. Vẽ đồ thị cho $x_{10}$ và $x_{20}$ từ CG, cùng với nghiệm chính xác $x$. (100 thành phần của nó là $x_i = (ih - i^2 h^2)/2$ với $h = 1/101$. Lệnh "plot(i, x(i))" sẽ cho ra một hình parabol.)
**26** Đối với ma trận không đối xứng, bán kính phổ $\rho = \max |\lambda_i|$ không phải là một chuẩn. Nhưng với $n$ lớn, $\|A^n\|$ vẫn tăng trưởng hay phân rã giống như $\rho^n$. Hãy so sánh các con số đó đối với $A =$ [1 1; 0 1.1] bằng cách sử dụng lệnh **norm**.
$A^n \rightarrow 0$ khi và chỉ khi $\rho < 1$. Khi $A = S^{-1}T$, đây là chìa khóa cho sự hội tụ.
