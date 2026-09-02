# **Chương 3**

# **Không Gian Vectơ và Không Gian Con (Vector Spaces and Subspaces)**

# **3.1 Các Không Gian của Vectơ (Spaces of Vectors)**

- **1** Không gian $n$-chiều tiêu chuẩn $\mathbf{R}^n$ chứa tất cả các vectơ cột thực có $n$ thành phần.
- **2** Nếu $v$ và $w$ nằm trong một **không gian vectơ (vector space)** $S$, mọi tổ hợp tuyến tính $cv + dw$ đều phải nằm trong $S$.
- **3** Các "vectơ" trong $S$ có thể là các ma trận hoặc các hàm số của $x$. Không gian 1-điểm $Z$ chỉ gồm vectơ $x = \mathbf{0}$.
- **4** Một **không gian con (subspace)** của $\mathbf{R}^n$ là một không gian vectơ nằm bên trong $\mathbf{R}^n$. *Ví dụ:* Đường thẳng $y = 3x$ nằm bên trong $\mathbf{R}^2$.
- **5** **Không gian cột (column space)** của $A$ chứa tất cả các tổ hợp của các cột của $A$: một không gian con của $\mathbf{R}^m$.
- **6** Không gian cột chứa tất cả các vectơ $Ax$. Vì vậy hệ phương trình $Ax = b$ giải được khi $b$ nằm trong $C(A)$.

Đối với một người mới bắt đầu, các tính toán ma trận liên quan đến rất nhiều con số. Đối với bạn, chúng liên quan đến các vectơ. Các cột của $Ax$ và $AB$ là các tổ hợp tuyến tính của $n$ vectơ - các cột của $A$. Chương này chuyển từ các con số và vectơ lên cấp độ hiểu biết thứ ba (cấp độ cao nhất). Thay vì các cột riêng lẻ, chúng ta xem xét các "không gian" của các vectơ. Nếu không nhìn thấy các *không gian vectơ* và đặc biệt là các *không gian con* của chúng, bạn chưa hiểu được mọi thứ về $Ax = b$.

Bởi vì chương này đi sâu hơn một chút, nó có vẻ khó hơn một chút. Điều đó là tự nhiên. Chúng ta đang nhìn vào bên trong các tính toán, để tìm thấy toán học. Công việc của tác giả là làm cho nó rõ ràng. Chương này kết thúc với *"Định Lý Cơ Bản Của Đại Số Tuyến Tính" (Fundamental Theorem of Linear Algebra)*.

Chúng ta bắt đầu với các không gian vectơ quan trọng nhất. Chúng được ký hiệu là $\mathbf{R}^1, \mathbf{R}^2, \mathbf{R}^3, \mathbf{R}^4, \dots$. Mỗi không gian $\mathbf{R}^n$ bao gồm toàn bộ một tập hợp các vectơ. $\mathbf{R}^5$ chứa tất cả các vectơ cột có năm thành phần. Điều này được gọi là "không gian 5-chiều" (5-dimensional space).

**ĐỊNH NGHĨA** *Không gian $\mathbf{R}^n$ bao gồm tất cả các vectơ cột $v$ có $n$ thành phần.* Các thành phần của $v$ là các số thực, đó là lý do cho chữ cái $\mathbf{R}$. Một vectơ có $n$ thành phần là các số phức nằm trong không gian $\mathbf{C}^n$.

Không gian vectơ $\mathbf{R}^2$ được biểu diễn bởi mặt phẳng $xy$ thông thường. Mỗi vectơ $v$ trong $\mathbf{R}^2$ có hai thành phần. Từ *"không gian"* yêu cầu chúng ta nghĩ về tất cả những vectơ đó - toàn bộ mặt phẳng. Mỗi vectơ cung cấp các tọa độ $x$ và $y$ của một điểm trong mặt phẳng: $v = (x, y)$.

Tương tự các vectơ trong $\mathbf{R}^3$ tương ứng với các điểm $(x, y, z)$ trong không gian ba chiều. Không gian một chiều $\mathbf{R}^1$ là một đường thẳng (giống như trục $x$). Như trước đây, chúng ta in các vectơ dưới dạng một cột giữa hai dấu ngoặc vuông, hoặc dọc theo một dòng sử dụng các dấu phẩy và ngoặc đơn:

$$\begin{bmatrix} 4 \\ \pi \end{bmatrix} \text{ nằm trong } \mathbf{R}^2, \quad (1, 1, 0, 1, 1) \text{ nằm trong } \mathbf{R}^5, \quad \begin{bmatrix} 1+i \\ 1-i \end{bmatrix} \text{ nằm trong } \mathbf{C}^2.$$

Điều tuyệt vời về đại số tuyến tính là nó xử lý không gian năm chiều một cách dễ dàng. Chúng ta không vẽ các vectơ, chúng ta chỉ cần năm con số (hoặc $n$ con số).

Để nhân $v$ với 7, hãy nhân mỗi thành phần với 7. Ở đây 7 là một "vô hướng" (scalar). Để cộng các vectơ trong $\mathbf{R}^5$, cộng từng phần tử tương ứng của chúng lại với nhau. Hai phép toán vectơ thiết yếu này diễn ra *bên trong không gian vectơ*, và chúng tạo ra các *tổ hợp tuyến tính:*

*Chúng ta có thể cộng các vectơ bất kỳ trong $\mathbf{R}^n$, và chúng ta có thể nhân bất kỳ vectơ $v$ nào với bất kỳ vô hướng $c$ nào.*

"Bên trong không gian vectơ" có nghĩa là *kết quả vẫn nằm trong không gian đó.* Nếu $v$ là vectơ trong $\mathbf{R}^4$ với các thành phần 1, 0, 0, 1, thì $2v$ là vectơ trong $\mathbf{R}^4$ với các thành phần 2, 0, 0, 2. (Trong trường hợp này 2 là vô hướng.) Một loạt toàn bộ các tính chất có thể được xác minh trong $\mathbf{R}^n$. Luật giao hoán là $v + w = w + v$; luật phân phối là $c(v + w) = cv + cw$. Có một "vectơ không" duy nhất thỏa mãn $\mathbf{0} + v = v$. Đó là ba trong số tám điều kiện được liệt kê ở đầu phần bài tập.

Tám điều kiện này được yêu cầu đối với mọi không gian vectơ. Có những vectơ khác với các vectơ cột, và có những không gian vectơ khác với $\mathbf{R}^n$, và tất cả các không gian vectơ đều phải tuân theo tám quy tắc hợp lý đó.

*Một không gian vectơ thực (real vector space) là một tập hợp các "vectơ" cùng với các quy tắc cho phép cộng vectơ và phép nhân với các số thực.* Phép cộng và phép nhân phải tạo ra các vectơ nằm trong không gian đó. Và tám điều kiện phải được thỏa mãn (điều này thường không thành vấn đề). Dưới đây là ba không gian vectơ khác ngoài $\mathbf{R}^n$:

$\mathbf{M}$ Không gian vectơ chứa *tất cả* các ma trận thực $2 \times 2$.
$\mathbf{F}$ Không gian vectơ chứa *tất cả* các hàm số thực $f(x)$.
$\mathbf{Z}$ Không gian vectơ chỉ bao gồm một *vectơ không (zero vector)* duy nhất.

Trong $\mathbf{M}$ các "vectơ" thực chất là các ma trận. Trong $\mathbf{F}$ các vectơ là các hàm số. Trong $\mathbf{Z}$ phép cộng duy nhất là $\mathbf{0} + \mathbf{0} = \mathbf{0}$. Trong mỗi trường hợp, chúng ta có thể cộng: các ma trận với các ma trận, các hàm số với các hàm số, vectơ không với vectơ không. Chúng ta có thể nhân một ma trận với 4 hoặc một hàm số với 4 hoặc vectơ không với 4. Kết quả vẫn nằm trong $\mathbf{M}$ hoặc $\mathbf{F}$ hoặc $\mathbf{Z}$. Cả tám điều kiện đều dễ dàng được kiểm tra.

Không gian hàm số $\mathbf{F}$ là vô hạn chiều. Một không gian hàm số nhỏ hơn là $\mathbf{P}$, hay $\mathbf{P}_n$, chứa tất cả các đa thức $a_0 + a_1 x + \dots + a_n x^n$ bậc $n$.

Không gian $\mathbf{Z}$ là không chiều (theo bất kỳ định nghĩa hợp lý nào về số chiều). $\mathbf{Z}$ là không gian vectơ nhỏ nhất có thể. Chúng ta ngần ngại gọi nó là $\mathbf{R}^0$, có nghĩa là không có thành phần nào - bạn có thể nghĩ rằng không có vectơ nào. Không gian vectơ $\mathbf{Z}$ chứa chính xác *một vectơ* (số không). Không có không gian nào có thể tồn tại mà không có vectơ không đó. Mỗi không gian có vectơ không của riêng nó - ma trận không, hàm số không, vectơ $(0, 0, 0)$ trong $\mathbf{R}^3$.

![](images/_page_134_Diagram_3.jpeg)

Hình 3.1: Không gian ma trận "bốn-chiều" $\mathbf{M}$. Không gian "không-chiều" $\mathbf{Z}$.

## **Không Gian Con (Subspaces)**

Tại những thời điểm khác nhau, chúng tôi sẽ yêu cầu bạn coi các ma trận và các hàm số như là các vectơ. Nhưng ở mọi thời điểm, những vectơ mà chúng ta cần nhất là các vectơ cột thông thường. Chúng là các vectơ có $n$ thành phần - nhưng *có lẽ không phải tất cả* các vectơ có $n$ thành phần. Có những không gian vectơ quan trọng *nằm bên trong $\mathbf{R}^n$.* Đó là những *không gian con* của $\mathbf{R}^n$.

Bắt đầu với không gian ba chiều thông thường $\mathbf{R}^3$. Chọn một mặt phẳng đi qua gốc tọa độ $(0, 0, 0)$. *Mặt phẳng đó tự bản thân nó là một không gian vectơ.* Nếu chúng ta cộng hai vectơ trong mặt phẳng, tổng của chúng cũng nằm trong mặt phẳng đó. Nếu chúng ta nhân một vectơ trong mặt phẳng với 2 hoặc -5, nó vẫn nằm trong mặt phẳng đó. Một mặt phẳng trong không gian ba chiều không phải là $\mathbf{R}^2$ (mặc dù nó trông giống như $\mathbf{R}^2$). Các vectơ có ba thành phần và chúng thuộc về $\mathbf{R}^3$. Mặt phẳng là một không gian vectơ *bên trong* $\mathbf{R}^3$.

Điều này minh họa một trong những ý tưởng cơ bản nhất trong đại số tuyến tính. Mặt phẳng đi qua $(0, 0, 0)$ là một *không gian con* của không gian vectơ toàn phần $\mathbf{R}^3$.

**ĐỊNH NGHĨA** Một *không gian con* của một không gian vectơ là một tập hợp các vectơ (bao gồm cả $\mathbf{0}$) thỏa mãn hai yêu cầu: *Nếu $v$ và $w$ là các vectơ trong không gian con đó và $c$ là bất kỳ vô hướng nào, thì*

(i) $v + w$ nằm trong không gian con
(ii) $cv$ nằm trong không gian con.

Nói cách khác, tập hợp các vectơ này "đóng" (closed) dưới phép cộng $v + w$ và phép nhân $cv$ (và $dw$). Những phép toán đó để lại cho chúng ta một vectơ bên trong không gian con. Chúng ta cũng có thể thực hiện phép trừ, bởi vì $-w$ nằm trong không gian con và tổng của nó với $v$ là $v - w$. Tóm lại, *tất cả các tổ hợp tuyến tính đều ở trong không gian con.*

Tất cả các phép toán này tuân theo quy tắc của không gian mẹ, do đó tám điều kiện bắt buộc tự động được đáp ứng. Chúng ta chỉ cần kiểm tra yêu cầu về tổ hợp tuyến tính cho một không gian con.

Sự thật đầu tiên: *Mọi không gian con đều chứa vectơ không.* Mặt phẳng trong $\mathbf{R}^3$ phải đi qua $(0, 0, 0)$. Chúng tôi đề cập đến điều này riêng biệt, để nhấn mạnh thêm, nhưng nó suy ra trực tiếp từ quy tắc **(ii)**. Chọn $c = 0$, và quy tắc yêu cầu $0v$ phải nằm trong không gian con.

Các mặt phẳng không chứa gốc tọa độ đều thất bại trong những bài kiểm tra này. Những mặt phẳng đó không phải là các không gian con.

*Các đường thẳng đi qua gốc tọa độ cũng là các không gian con.* Khi chúng ta nhân với 5, hoặc cộng hai vectơ trên đường thẳng, chúng ta vẫn ở trên đường thẳng đó. Nhưng đường thẳng phải đi qua $(0, 0, 0)$.

Một không gian con khác là toàn bộ $\mathbf{R}^3$. Toàn bộ không gian là một không gian con *(của chính nó).* Dưới đây là danh sách tất cả các không gian con có thể có của $\mathbf{R}^3$:

- (L) Bất kỳ đường thẳng nào qua $(0, 0, 0)$
- (P) Bất kỳ mặt phẳng nào qua $(0, 0, 0)$
- ($\mathbf{R}^3$) Toàn bộ không gian
- (Z) Vectơ đơn lẻ $(0, 0, 0)$

Nếu chúng ta cố gắng chỉ giữ lại một *phần* của một mặt phẳng hay một đường thẳng, các yêu cầu cho một không gian con sẽ không đúng nữa. Hãy nhìn vào những ví dụ này trong $\mathbf{R}^2$ - chúng không phải là các không gian con.

**Ví dụ 1** Chỉ giữ lại những vectơ $(x, y)$ có các thành phần là dương hoặc bằng không (đây là một góc phần tư của mặt phẳng). Vectơ $(2, 3)$ được bao gồm nhưng $(-2, -3)$ thì không. Vậy nên quy tắc **(ii)** bị vi phạm khi chúng ta cố gắng nhân với $c = -1$. *Góc phần tư mặt phẳng không phải là một không gian con.*

**Ví dụ 2** Bao gồm cả các vectơ có cả hai thành phần đều là số âm. Bây giờ chúng ta có hai góc phần tư mặt phẳng đối đỉnh. Yêu cầu **(ii)** được thỏa mãn; chúng ta có thể nhân với bất kỳ số $c$ nào. Nhưng quy tắc **(i)** bây giờ lại thất bại. Tổng của $v = (2, 3)$ và $w = (-3, -2)$ là $(-1, 1)$, nằm bên ngoài các góc phần tư mặt phẳng này. *Hai góc phần tư mặt phẳng không tạo thành một không gian con.*

Các quy tắc **(i)** và **(ii)** liên quan đến phép cộng vectơ $v + w$ và phép nhân với các vô hướng $c$ và $d$. Các quy tắc có thể được kết hợp thành một yêu cầu duy nhất - *quy tắc cho các không gian con:*

*Một không gian con chứa $v$ và $w$ phải chứa tất cả các tổ hợp tuyến tính $cv + dw$.*

**Ví dụ 3** Bên trong không gian vectơ $\mathbf{M}$ của tất cả các ma trận $2 \times 2$, dưới đây là hai không gian con:

- (U) Tất cả các ma trận tam giác trên $\begin{bmatrix} a & b \\ 0 & d \end{bmatrix}$
- (D) Tất cả các ma trận đường chéo $\begin{bmatrix} a & 0 \\ 0 & d \end{bmatrix}$.

Cộng hai ma trận bất kỳ trong U, và tổng của chúng nằm trong U. Cộng các ma trận đường chéo, và tổng của chúng là đường chéo. Trong trường hợp này D cũng là một không gian con của U! Tất nhiên ma trận không luôn nằm trong những không gian con này, khi mà $a, b,$ và $d$ đều bằng không. Z luôn là một không gian con.

Các bội số của ma trận đơn vị $I$ cũng tạo thành một không gian con. $2I + 3I$ nằm trong không gian con này, và $3$ lần $4I$ cũng vậy. Các ma trận $cI$ tạo thành một "đường thẳng ma trận" bên trong $\mathbf{M}$ và U và D.

Bản thân ma trận $I$ có phải là một không gian con không? Chắc chắn là không. Chỉ có ma trận không mới như vậy. Tâm trí bạn sẽ phát minh ra nhiều không gian con của các ma trận $2 \times 2$ hơn nữa - hãy viết chúng ra cho Bài Tập 5.

### **Không Gian Cột (Column Space) của $A$**

Các không gian con quan trọng nhất được gắn trực tiếp với một ma trận $A$. Chúng ta đang cố gắng giải $Ax = b$. Nếu $A$ không khả nghịch, hệ phương trình giải được đối với một số vế phải $b$ và không giải được đối với các $b$ khác. Chúng ta muốn mô tả các vế phải $b$ tốt - tức là các vectơ mà *có thể* được viết thành ma trận $A$ nhân với một vectơ $x$ nào đó. Những $b$ đó tạo thành *"không gian cột"* của $A$.

Hãy nhớ rằng $Ax$ là một tổ hợp các cột của $A$. Để có được mọi $b$ khả thi, chúng ta sử dụng mọi $x$ khả thi. Bắt đầu với các cột của $A$ và *lấy tất cả các tổ hợp tuyến tính của chúng. Điều này tạo ra không gian cột của A.* Nó **là một không gian vectơ được tạo thành bởi các vectơ cột.**

$C(A)$ chứa không chỉ $n$ cột của $A$, mà còn chứa tất cả các tổ hợp của chúng là $Ax$.

**ĐỊNH NGHĨA** *Không gian cột* bao gồm *tất cả các tổ hợp tuyến tính của các cột*. Những tổ hợp đó là tất cả các vectơ có thể có của $Ax$. Chúng lấp đầy không gian cột $C(A)$.

Không gian cột này là cực kỳ quan trọng đối với toàn bộ cuốn sách, và đây là lý do tại sao. *Giải hệ $Ax = b$ có nghĩa là biểu diễn $b$ dưới dạng một tổ hợp của các cột.* Vế phải $b$ phải nằm *trong không gian cột* được sinh ra bởi $A$ ở vế trái, nếu không sẽ vô nghiệm!

*Hệ $Ax = b$ giải được khi và chỉ khi $b$ nằm trong không gian cột của $A$.*

Khi $b$ nằm trong không gian cột, nó là một tổ hợp của các cột. Các hệ số trong tổ hợp đó mang lại cho chúng ta một nghiệm $x$ cho hệ $Ax = b$.

Giả sử $A$ là một ma trận $m \times n$. Các cột của nó có $m$ thành phần (chứ không phải $n$). Do đó các cột thuộc về $\mathbf{R}^m$. *Không gian cột của A là một không gian con của $\mathbf{R}^m$ (không phải $\mathbf{R}^n$).* Tập hợp tất cả các tổ hợp cột $Ax$ thỏa mãn các quy tắc (i) và (ii) cho một không gian con: Khi chúng ta cộng các tổ hợp tuyến tính hoặc nhân với các vô hướng, chúng ta vẫn tạo ra các tổ hợp của các cột. Từ "không gian con" được biện minh *bởi việc lấy tất cả các tổ hợp tuyến tính.*

Đây là một ma trận $3 \times 2$ là $A$, có không gian cột là một không gian con của $\mathbf{R}^3$. Không gian cột của $A$ là một mặt phẳng trong Hình 3.2. Với chỉ 2 cột, $C(A)$ không thể là toàn bộ $\mathbf{R}^3$.

#### **Ví dụ 4**

$$Ax \text{ là } \begin{bmatrix} 1 & 0 \\ 4 & 3 \\ 2 & 3 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \text{ đó là } x_1 \begin{bmatrix} 1 \\ 4 \\ 2 \end{bmatrix} + x_2 \begin{bmatrix} 0 \\ 3 \\ 3 \end{bmatrix}.$$

Không gian cột của tất cả các tổ hợp của hai cột này *lấp đầy một mặt phẳng trong* $\mathbf{R}^3$. Chúng ta đã vẽ một $b$ cụ thể (một tổ hợp của các cột). Vectơ $b = Ax$ này nằm trên mặt phẳng. Mặt phẳng có độ dày bằng 0, do đó hầu hết các vế phải $b$ trong $\mathbf{R}^3$ đều *không* nằm trong không gian cột. Đối với hầu hết các $b$, hệ 3 phương trình 2 ẩn của chúng ta vô nghiệm.

![](images/_page_137_Figure_2.jpeg)

Hình 3.2: Không gian cột $C(A)$ là một mặt phẳng chứa hai cột. $Ax = b$ giải được khi $b$ nằm trên mặt phẳng đó. Khi đó $b$ là một tổ hợp của các cột.

Tất nhiên $(0, 0, 0)$ nằm trong không gian cột. Mặt phẳng đi qua gốc tọa độ. Chắc chắn có một nghiệm cho $Ax = \mathbf{0}$. Nghiệm đó, luôn luôn có sẵn, là $x = \mathbf{0}$.

Xin nhắc lại, các vế phải $b$ có thể đạt được chính xác là các vectơ nằm trong không gian cột. Một khả năng là chính cột đầu tiên - lấy $x_1 = 1$ và $x_2 = 0$. Một tổ hợp khác là cột thứ hai - lấy $x_1 = 0$ và $x_2 = 1$. Cấp độ hiểu biết mới là việc nhìn thấy *tất cả* các tổ hợp - toàn bộ không gian con được sinh ra bởi hai cột đó.

**Ký hiệu** Không gian cột của $A$ được ký hiệu là $C(A)$. Bắt đầu với các cột và lấy tất cả các tổ hợp tuyến tính của chúng. Chúng ta có thể nhận được toàn bộ $\mathbf{R}^m$ hoặc chỉ là một không gian con.

**Quan trọng** Thay vì các cột trong $\mathbf{R}^m$, chúng ta có thể bắt đầu với một tập hợp $\mathbf{S}$ bất kỳ gồm các vectơ trong một không gian vectơ $\mathbf{V}$. Để có được một *không gian con* $\mathbf{SS}$ của $\mathbf{V}$, chúng ta lấy *tất cả các tổ hợp* của các vectơ trong tập hợp đó:

$\mathbf{S}$ = tập hợp các vectơ trong $\mathbf{V}$ (có thể *không phải* là một không gian con)
$\mathbf{SS}$ = tất cả các tổ hợp của các vectơ trong $\mathbf{S}$ (chắc chắn là một không gian con)
$\mathbf{SS}$ = tất cả $c_1 v_1 + \dots + c_n v_n$ = **không gian con của $\mathbf{V}$** được "sinh ra (spanned)" bởi $\mathbf{S}$

Khi $\mathbf{S}$ là tập hợp các cột, $\mathbf{SS}$ là không gian cột. Khi chỉ có một vectơ khác không duy nhất $v$ trong $\mathbf{S}$, không gian con $\mathbf{SS}$ là đường thẳng đi qua $v$. *Luôn luôn* $\mathbf{SS}$ *là không gian con nhỏ nhất chứa* $\mathbf{S}$. Đây là một cách cơ bản để tạo ra các không gian con và chúng ta sẽ quay trở lại với nó.

Xin nhắc lại: Các cột "sinh ra (span)" không gian cột.

**Không gian con $\mathbf{SS}$ là "không gian sinh (span)" của $\mathbf{S}$, chứa tất cả các tổ hợp của các vectơ trong $\mathbf{S}$.**

**Ví dụ 5** Mô tả các không gian cột (chúng là các không gian con của $\mathbf{R}^2$) cho

| $I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ | và | $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$ | và | $B = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 0 \end{bmatrix}$ |
|----------------------------------------------------|-----|----------------------------------------------------|-----|------------------------------------------------------------|
|----------------------------------------------------|-----|----------------------------------------------------|-----|------------------------------------------------------------|

**Giải** Không gian cột của $I$ là *toàn bộ không gian* $\mathbf{R}^2$. Mọi vectơ đều là một tổ hợp các cột của $I$. Bằng ngôn ngữ không gian vectơ, $C(I)$ là $\mathbf{R}^2$.

Không gian cột của $A$ chỉ là một đường thẳng. Cột thứ hai $(2, 4)$ là một bội số của cột thứ nhất $(1, 2)$. Các vectơ đó khác nhau, nhưng chúng ta đang tập trung vào các *không gian* vectơ. Không gian cột chứa $(1, 2)$ và $(2, 4)$ và tất cả các vectơ khác $(c, 2c)$ dọc theo đường thẳng đó. Phương trình $Ax = b$ chỉ giải được khi $b$ nằm trên đường thẳng đó.

Đối với ma trận thứ ba (có ba cột), không gian cột $C(B)$ là toàn bộ $\mathbf{R}^2$. Mọi $b$ đều có thể đạt được. Vectơ $b = (5, 4)$ là cột 2 cộng cột 3, do đó $x$ có thể là $(0, 1, 1)$. Cùng vectơ $(5, 4)$ đó cũng là $2(\text{cột 1}) + \text{cột 3}$, nên một $x$ khác có thể là $(2, 0, 1)$. Ma trận này có cùng không gian cột với $I$ - bất kỳ $b$ nào cũng được cho phép. Nhưng bây giờ $x$ có thêm các thành phần và có nhiều nghiệm hơn - nhiều tổ hợp hơn mang lại $b$.

Phần tiếp theo tạo ra một không gian vectơ $N(A)$, để mô tả tất cả các nghiệm của $Ax = 0$. Phần này đã tạo ra không gian cột $C(A)$, để mô tả tất cả các vế phải $b$ có thể đạt được.

#### **• ÔN TẬP CÁC Ý TƯỞNG CHÍNH (REVIEW OF THE KEY IDEAS) •**

- **1.** $\mathbf{R}^n$ chứa tất cả các vectơ cột có $n$ thành phần thực.
- **2.** $\mathbf{M}$ (các ma trận $2 \times 2$) và $\mathbf{F}$ (các hàm số) và $\mathbf{Z}$ (chỉ riêng vectơ không) là các không gian vectơ.
- **3.** Một không gian con chứa $v$ và $w$ phải chứa tất cả các tổ hợp của chúng $cv + dw$.
- **4.** Các tổ hợp của các cột của $A$ tạo thành *không gian cột $C(A)$*. Khi đó không gian cột được "sinh ra (spanned)" bởi các cột.
- **5.** $Ax = b$ có một nghiệm chính xác khi $b$ nằm trong không gian cột của $A$. **$C(A)$ = tất cả các tổ hợp của các cột = tất cả các vectơ $Ax$.**

#### **• CÁC VÍ DỤ ĐÃ GIẢI (WORKED EXAMPLES) •**

**3.1 A** Chúng ta được cho ba vectơ khác nhau $b_1, b_2, b_3$. Hãy xây dựng một ma trận sao cho các phương trình $Ax = b_1$ và $Ax = b_2$ giải được, nhưng $Ax = b_3$ không giải được. Làm thế nào bạn có thể quyết định xem điều này có khả thi hay không? Làm thế nào bạn có thể xây dựng $A$?

**Giải** Chúng ta muốn có $b_1$ và $b_2$ nằm trong không gian cột của $A$. Khi đó $Ax = b_1$ và $Ax = b_2$ sẽ giải được. *Cách nhanh nhất là lấy $b_1$ và $b_2$ làm hai cột của $A$.* Khi đó các nghiệm là $x = (1, 0)$ và $x = (0, 1)$.

Đồng thời, chúng ta không muốn $Ax = b_3$ giải được. Vì vậy, đừng làm cho không gian cột lớn hơn nữa! Chỉ giữ lại các cột $b_1$ và $b_2$, câu hỏi là:

| Có giải được $Ax = \begin{bmatrix} b_1 & b_2 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = b_3$ không? | $b_3$ có phải là một tổ hợp của $b_1$ và $b_2$ không? |
|------------------------------------------------------------------------------------------------------------|---------------------------------------------|
|------------------------------------------------------------------------------------------------------------|---------------------------------------------|

Nếu câu trả lời là *không*, chúng ta có ma trận $A$ mong muốn. Nếu câu trả lời là *có*, thì việc xây dựng $A$ là *không thể*. Khi không gian cột chứa $b_1$ và $b_2$, nó sẽ phải chứa tất cả các tổ hợp tuyến tính của chúng. Vậy nên $b_3$ nhất thiết sẽ nằm trong không gian cột đó và $Ax = b_3$ nhất thiết sẽ giải được.

**3.1 B** Mô tả một không gian con $\mathbf{S}$ của mỗi không gian vectơ $\mathbf{V}$, và sau đó là một không gian con $\mathbf{SS}$ của $\mathbf{S}$.

$\mathbf{V}_1$ = tất cả các tổ hợp của $(1, 1, 0, 0)$ và $(1, 1, 1, 0)$ và $(1, 1, 1, 1)$
$\mathbf{V}_2$ = tất cả các vectơ vuông góc với $u = (1, 2, 1)$, vậy nên $u \cdot v = 0$
$\mathbf{V}_3$ = tất cả các ma trận đối xứng $2 \times 2$ (một không gian con của $\mathbf{M}$)
$\mathbf{V}_4$ = tất cả các nghiệm của phương trình $d^4y / dx^4 = 0$ (một không gian con của $\mathbf{F}$)

Mô tả mỗi $\mathbf{V}$ theo hai cách: *"Tất cả các tổ hợp của..."* *"Tất cả các nghiệm của phương trình..."*

**Giải** $\mathbf{V}_1$ bắt đầu với ba vectơ. Một không gian con $\mathbf{S}$ đến từ tất cả các tổ hợp của hai vectơ đầu tiên $(1, 1, 0, 0)$ và $(1, 1, 1, 0)$. Một không gian con $\mathbf{SS}$ của $\mathbf{S}$ đến từ tất cả các bội số $(c, c, 0, 0)$ của vectơ đầu tiên. Quá nhiều khả năng.

Một không gian con $\mathbf{S}$ của $\mathbf{V}_2$ là đường thẳng đi qua $(1, -1, 1)$. Đường thẳng này vuông góc với $u$. Vectơ $x = (0, 0, 0)$ nằm trong $\mathbf{S}$ và tất cả các bội số của nó $cx$ cho ra không gian con nhỏ nhất $\mathbf{SS} = \mathbf{Z}$.

Các ma trận đường chéo là một không gian con $\mathbf{S}$ của các ma trận đối xứng. Các bội số $cI$ là một không gian con $\mathbf{SS}$ của các ma trận đường chéo.

$\mathbf{V}_4$ chứa tất cả các đa thức bậc ba $y = a + bx + cx^2 + dx^3$, với $d^4y / dx^4 = 0$. Các đa thức bậc hai cho ta một không gian con $\mathbf{S}$. Các đa thức bậc nhất là một lựa chọn cho $\mathbf{SS}$. Các hằng số có thể là $\mathbf{SSS}$.

Trong cả bốn phần, chúng ta đều có thể chọn $\mathbf{S} = \mathbf{V}$ chính nó, và $\mathbf{SS} = $ không gian con không $\mathbf{Z}$.

Mỗi $\mathbf{V}$ có thể được mô tả như *tất cả các tổ hợp của*... và như *tất cả các nghiệm của*...:

$\mathbf{V}_1$ = tất cả các tổ hợp của 3 vectơ $\quad \mathbf{V}_1$ = tất cả các nghiệm của $v_1 - v_2 = 0$
$\mathbf{V}_2$ = tất cả các tổ hợp của $(1, 0, -1)$ và $(1, -1, 1) \quad \mathbf{V}_2$ = tất cả các nghiệm của $u \cdot v = 0$.
$\mathbf{V}_3$ = tất cả các tổ hợp của $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$, $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$, $\begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix} \quad \mathbf{V}_3$ = tất cả các nghiệm của ma trận $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$ với $b = c$
$\mathbf{V}_4$ = tất cả các tổ hợp của $1, x, x^2, x^3 \quad \mathbf{V}_4$ = tất cả các nghiệm của $d^4y / dx^4 = 0$.

### **Bài Tập 3.1 (Problem Set 3.1)**

**Các bài tập đầu tiên từ 1-8 là về các không gian vectơ nói chung. Các vectơ trong những không gian đó không nhất thiết phải là các vectơ cột. Trong định nghĩa của một** *không gian vectơ,* **phép cộng vectơ** $x + y$ **và phép nhân vô hướng** $cx$ **phải tuân theo tám quy tắc sau:**

- (1) $x + y = y + x$
- (2) $x + (y + z) = (x + y) + z$
- (3) Tồn tại duy nhất một "vectơ không" sao cho $x + 0 = x$ với mọi $x$
- (4) Với mỗi $x$, tồn tại một vectơ duy nhất $-x$ sao cho $x + (-x) = 0$
- (5) 1 nhân với $x$ bằng $x$
- (6) $(c_1 c_2)x = c_1(c_2 x)$
- (7) $c(x + y) = cx + cy$
- (8) $(c_1 + c_2)x = c_1 x + c_2 x$.

- (1) đến (4) nói về phép cộng $x + y$
- (5) đến (6) nói về phép nhân vô hướng $cx$
- (7) đến (8) liên kết chúng với nhau

**1** Giả sử $(x_1, x_2) + (y_1, y_2)$ được định nghĩa là $(x_1 + y_2, x_2 + y_1)$. Với phép nhân thông thường $cx = (cx_1, cx_2)$, điều kiện nào trong tám điều kiện không được thỏa mãn?
**2** Giả sử phép nhân $cx$ được định nghĩa là tạo ra $(cx_1, 0)$ thay vì $(cx_1, cx_2)$. Với phép cộng thông thường trong $\mathbf{R}^2$, tám điều kiện có được thỏa mãn không?
**3** (a) Những quy tắc nào bị vi phạm nếu chúng ta chỉ giữ lại các số dương $x > 0$ trong $\mathbf{R}^1$? Mọi giá trị $c$ phải được cho phép. Nửa đường thẳng không phải là một không gian con.
- (b) Các số dương với $x + y$ và $cx$ được định nghĩa lại để bằng tích $xy$ thông thường và $x^c$ thì sẽ thỏa mãn tám quy tắc. Kiểm tra quy tắc 7 khi $c = 3, x = 2, y = 1$. (Lúc đó $x + y = 2$ và $cx = 8$.) Con số nào đóng vai trò là "vectơ không"?
**4** Ma trận $A = \begin{bmatrix} 2 & 2 \\ 2 & 2 \end{bmatrix}$ (giả định theo hình dạng ma trận in mờ trong sách) là một "vectơ" trong không gian $\mathbf{M}$ của tất cả các ma trận $2 \times 2$. Hãy viết ra vectơ không trong không gian này, vectơ $\frac{1}{2}A$, và vectơ $-A$. Những ma trận nào nằm trong không gian con nhỏ nhất chứa $A$?
**5** (a) Mô tả một không gian con của $\mathbf{M}$ chứa $A = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ nhưng không chứa $B = \begin{bmatrix} 0 & 0 \\ 0 & -1 \end{bmatrix}$.
- (b) Nếu một không gian con của $\mathbf{M}$ chứa cả $A$ và $B$, nó có bắt buộc phải chứa $I$ không?
- (c) Mô tả một không gian con của $\mathbf{M}$ không chứa các ma trận đường chéo khác không.
**6** Các hàm số $f(x) = x^2$ và $g(x) = 5x$ là các "vectơ" trong $\mathbf{F}$. Đây là không gian vectơ của tất cả các hàm số thực. (Các hàm số được xác định với $-\infty < x < \infty$.) Tổ hợp $3f(x) - 4g(x)$ là hàm số $h(x) =$ \_\_.
**7** Quy tắc nào bị phá vỡ nếu việc nhân $f(x)$ với $c$ tạo ra hàm số $f(cx)$? Giữ nguyên phép cộng thông thường $f(x) + g(x)$.
**8** Nếu tổng của các "vectơ" $f(x)$ và $g(x)$ được định nghĩa là hàm hợp $f(g(x))$, thì "vectơ không" là $g(x) = x$. Giữ nguyên phép nhân vô hướng thông thường $cf(x)$ và tìm ra hai quy tắc bị phá vỡ.

**Các câu hỏi 9-18 là về "các yêu cầu đối với không gian con":** $x + y$ và $cx$ (và sau đó là tất cả các tổ hợp tuyến tính $cx + dy$) vẫn nằm trong không gian con.

- **9** Một yêu cầu có thể được đáp ứng trong khi yêu cầu kia lại thất bại. Hãy chứng minh điều này bằng cách tìm
  - (a) Một tập hợp các vectơ trong $\mathbf{R}^2$ mà $x + y$ nằm trong tập hợp nhưng $\frac{1}{2}x$ có thể nằm ngoài.
- (b) Một tập hợp các vectơ trong $\mathbf{R}^2$ (khác với hai góc phần tư mặt phẳng) mà mọi $cx$ nằm trong tập hợp nhưng $x + y$ có thể nằm ngoài.
**10** Những tập hợp con nào sau đây của $\mathbf{R}^3$ thực sự là các không gian con?
  - (a) Mặt phẳng các vectơ $(b_1, b_2, b_3)$ với $b_1 = b_2$.
  - (b) Mặt phẳng các vectơ với $b_1 = 1$.
  - (c) Các vectơ với $b_1 b_2 b_3 = 0$.
  - (d) Tất cả các tổ hợp tuyến tính của $v = (1, 4, 0)$ và $w = (2, 2, 2)$.
  - (e) Tất cả các vectơ thỏa mãn $b_1 + b_2 + b_3 = 0$.
- (f) Tất cả các vectơ với $b_1 \le b_2 \le b_3$.
**11** Mô tả không gian con nhỏ nhất của không gian ma trận $\mathbf{M}$ chứa
- (a) $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ và $\begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$
- (b) $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$
- (c) $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ và $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$.
- **12** Cho $P$ là mặt phẳng trong $\mathbf{R}^3$ có phương trình $x + y - 2z = 4$. Gốc tọa độ $(0, 0, 0)$ không nằm trong $P$! Tìm hai vectơ trong $P$ và kiểm tra rằng tổng của chúng không nằm trong $P$.
**13** Cho $P_0$ là mặt phẳng đi qua $(0, 0, 0)$ song song với mặt phẳng $P$ ở trên. Phương trình của $P_0$ là gì? Tìm hai vectơ trong $P_0$ và kiểm tra rằng tổng của chúng nằm trong $P_0$.
**14** Các không gian con của $\mathbf{R}^3$ là các mặt phẳng, đường thẳng, chính $\mathbf{R}^3$, hoặc $\mathbf{Z}$ chỉ chứa $(0, 0, 0)$.
  - (a) Mô tả ba loại không gian con của $\mathbf{R}^2$.
  - (b) Mô tả tất cả các không gian con của $\mathbf{D}$, không gian các ma trận đường chéo $2 \times 2$.

- **15** (a) Giao của hai mặt phẳng đi qua $(0, 0, 0)$ có thể là một \_\_ trong $\mathbf{R}^3$ nhưng nó cũng có thể là một \_\_. Nó không thể là $\mathbf{Z}$!
- (b) Giao của một mặt phẳng đi qua $(0, 0, 0)$ với một đường thẳng đi qua $(0, 0, 0)$ có thể là một \_\_ nhưng nó cũng có thể là một \_\_.
- (c) Nếu $\mathbf{S}$ và $\mathbf{T}$ là các không gian con của $\mathbf{R}^5$, hãy chứng minh rằng giao $\mathbf{S} \cap \mathbf{T}$ của chúng là một không gian con của $\mathbf{R}^5$. Ở đây $\mathbf{S} \cap \mathbf{T}$ bao gồm các vectơ cùng nằm trong cả hai không gian con. *Hãy kiểm tra rằng $x + y$ và $cx$ đều nằm trong $\mathbf{S} \cap \mathbf{T}$ nếu $x$ và $y$ nằm trong cả hai không gian đó.*
**16** Giả sử $P$ là một mặt phẳng qua $(0, 0, 0)$ và $L$ là một đường thẳng qua $(0, 0, 0)$. Không gian vectơ nhỏ nhất chứa cả $P$ và $L$ hoặc là \_\_ hoặc là \_\_.
**17** (a) Chứng minh rằng tập hợp các ma trận *khả nghịch* trong $\mathbf{M}$ không phải là một không gian con.
- (b) Chứng minh rằng tập hợp các ma trận *suy biến (singular)* trong $\mathbf{M}$ không phải là một không gian con.
**18** Đúng hay sai (kiểm tra phép cộng trong mỗi trường hợp bằng một ví dụ):
  - (a) Các ma trận đối xứng trong $\mathbf{M}$ (với $A^T = A$) tạo thành một không gian con.
  - (b) Các ma trận phản đối xứng trong $\mathbf{M}$ (với $A^T = -A$) tạo thành một không gian con.
  - (c) Các ma trận không đối xứng trong $\mathbf{M}$ (với $A^T \neq A$) tạo thành một không gian con.

**Các câu hỏi 19-27 là về các không gian cột $C(A)$ và phương trình $Ax = b$.**
**19** Mô tả các không gian cột (đường thẳng hoặc mặt phẳng) của các ma trận cụ thể sau:

| $A = \begin{bmatrix} 1 & 2 \\ 0 & 0 \\ 0 & 0 \end{bmatrix}$ | và | $B = \begin{bmatrix} 1 & 0 \\ 0 & 2 \\ 0 & 0 \end{bmatrix}$ | và | $C = \begin{bmatrix} 1 & 0 \\ 2 & 0 \\ 0 & 0 \end{bmatrix}$ |
|-------------------------------------------------------------|-----|-------------------------------------------------------------|-----|-------------------------------------------------------------|
|-------------------------------------------------------------|-----|-------------------------------------------------------------|-----|-------------------------------------------------------------|

**20** Đối với những vế phải nào (tìm một điều kiện trên $b_1, b_2, b_3$) thì những hệ phương trình này giải được?

| (a) | $\begin{bmatrix} 1 & 4 & 2 \\ 2 & 8 & 4 \\ -1 & -4 & -2 \end{bmatrix}$ | $\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix}$ | (b) | $\begin{bmatrix} 1 & 4 \\ 2 & 9 \\ -1 & -4 \end{bmatrix}$ | $\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix}$ |
|-----|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----|-----------------------------------------------------------|----------------------------------------------------------------------------------------------|
|-----|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----|-----------------------------------------------------------|----------------------------------------------------------------------------------------------|

**21** Cộng hàng 1 của $A$ vào hàng 2 tạo ra $B$. Cộng cột 1 vào cột 2 tạo ra $C$. Một tổ hợp các cột của ($B$ hay $C$?) cũng là một tổ hợp các cột của $A$. Hai ma trận nào có cùng không gian cột?

| $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$ | và | $B = \begin{bmatrix} 1 & 2 \\ 3 & 6 \end{bmatrix}$ | và | $C = \begin{bmatrix} 1 & 3 \\ 2 & 3 \end{bmatrix}$ |
|----------------------------------------------------|-----|----------------------------------------------------|-----|----------------------------------------------------|
|----------------------------------------------------|-----|----------------------------------------------------|-----|----------------------------------------------------|

$$\begin{bmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix} \quad \text{và} \quad \begin{bmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix}$$

**22** Đối với các vectơ $(b_1, b_2, b_3)$ nào thì các hệ phương trình này có nghiệm?

- **23** (Khuyên làm) Nếu chúng ta thêm một cột phụ $b$ vào một ma trận $A$, thì không gian cột sẽ trở nên lớn hơn trừ khi \_\_. Hãy đưa ra một ví dụ mà không gian cột trở nên lớn hơn và một ví dụ mà nó không lớn hơn. Tại sao phương trình $Ax = b$ giải được chính xác khi không gian cột *không* trở nên lớn hơn - tức là không gian cột của $A$ và $[A \ b]$ là giống hệt nhau?
**24** Các cột của $AB$ là các tổ hợp của các cột của $A$. Điều này có nghĩa là: *Không gian cột của $AB$ được chứa trong (có thể bằng với) không gian cột của A.* Hãy cho một ví dụ mà không gian cột của $A$ và $AB$ không bằng nhau.
**25** Giả sử $Ax = b$ và $Ay = b^*$ đều giải được. Khi đó $Az = b + b^*$ giải được. $z$ là gì? Điều này chuyển ngữ thành: Nếu $b$ và $b^*$ nằm trong không gian cột $C(A)$, thì $b + b^*$ cũng nằm trong $C(A)$.
**26** Nếu $A$ là bất kỳ ma trận $5 \times 5$ khả nghịch nào, thì không gian cột của nó là \_\_. Tại sao?
**27** Đúng hay sai (đưa ra một phản ví dụ nếu sai):
  - (a) Các vectơ $b$ không nằm trong không gian cột $C(A)$ tạo thành một không gian con.
  - (b) Nếu $C(A)$ chỉ chứa vectơ không, thì $A$ là ma trận không.
  - (c) Không gian cột của $2A$ bằng không gian cột của $A$.
- (d) Không gian cột của $A - I$ bằng không gian cột của $A$ (hãy kiểm tra điều này).
**28** Xây dựng một ma trận $3 \times 3$ có không gian cột chứa $(1, 1, 0)$ và $(1, 0, 1)$ nhưng không chứa $(1, 1, 1)$. Xây dựng một ma trận $3 \times 3$ có không gian cột chỉ là một đường thẳng.
**29** Nếu hệ phương trình $9 \times 12$ $Ax = b$ có thể giải được với mọi $b$, thì $C(A) =$ \_\_.

### **Các Bài Toán Thử Thách (Challenge Problems)**

- **30** Giả sử $\mathbf{S}$ và $\mathbf{T}$ là hai không gian con của một không gian vectơ $\mathbf{V}$.
  - (a) **Định nghĩa:** **Tổng $\mathbf{S} + \mathbf{T}$** chứa tất cả các tổng $s + t$ của một vectơ trong $\mathbf{S}$ và một vectơ $t$ trong $\mathbf{T}$. Chứng minh rằng $\mathbf{S} + \mathbf{T}$ thỏa mãn các yêu cầu (phép cộng và phép nhân vô hướng) cho một không gian vectơ.
- (b) Nếu $\mathbf{S}$ và $\mathbf{T}$ là các đường thẳng trong $\mathbf{R}^m$, sự khác biệt giữa $\mathbf{S} + \mathbf{T}$ và $\mathbf{S} \cup \mathbf{T}$ là gì? Tập hợp hợp (union) đó chứa tất cả các vectơ từ $\mathbf{S}$ hoặc $\mathbf{T}$ hoặc cả hai. Hãy giải thích câu nói này: *Không gian sinh (span) của $\mathbf{S} \cup \mathbf{T}$ là $\mathbf{S} + \mathbf{T}$.* (Phần 3.5 sẽ quay trở lại với từ "span" này.)
**31** Nếu $\mathbf{S}$ là không gian cột của $A$ và $\mathbf{T}$ là $C(B)$, thì $\mathbf{S} + \mathbf{T}$ là không gian cột của ma trận $M$ nào? Các cột của $A$ và $B$ và $M$ đều nằm trong $\mathbf{R}^m$. (Tôi không nghĩ $A + B$ luôn luôn là một $M$ đúng.)
**32** Chứng minh rằng các ma trận $A$ và $\begin{bmatrix} A & AB \end{bmatrix}$ (có các cột phụ) có cùng không gian cột. Nhưng hãy tìm một ma trận vuông với $C(A^2)$ nhỏ hơn $C(A)$. Điểm quan trọng: Một ma trận $A$ cấp $n \times n$ có $C(A) = \mathbf{R}^n$ chính xác khi $A$ là một ma trận \_\_.

# **3.2 Không Gian Không (The Nullspace) của $A$: Giải $Ax = 0$ và $Rx = 0$**

**Không gian không (nullspace)** $N(A)$ trong $\mathbf{R}^n$ chứa tất cả các nghiệm $x$ của $Ax = 0$. Điều này bao gồm $x = 0$.
Phép khử (từ $A$ sang $U$ sang $R$) không làm thay đổi không gian không: $N(A) = N(U) = N(R)$.
**Dạng bậc thang rút gọn theo hàng (reduced row echelon form)** $R = \text{rref}(A)$ có tất cả các phần tử xoay = 1, với các số 0 ở trên và dưới.
Nếu cột $j$ của $R$ là tự do (không có phần tử xoay), thì có một *"nghiệm đặc biệt" (special solution)* cho $Ax = 0$ với $x_j = 1$.
Số lượng phần tử xoay = số lượng hàng khác không trong $R$ = **hạng (rank)** $r$. Có $n - r$ cột tự do.
Mọi ma trận với $m < n$ đều có các nghiệm khác không cho $Ax = 0$ trong không gian không của nó.

Phần này là về không gian con chứa tất cả các nghiệm của $Ax = 0$. Ma trận $A$ kích thước $m \times n$ có thể là ma trận vuông hoặc chữ nhật. Vế phải là $b = 0$. *Một nghiệm ngay lập tức là $x = 0$.* Đối với các ma trận khả nghịch, đây là nghiệm duy nhất. Đối với các ma trận khác, không khả nghịch, có những nghiệm khác không cho $Ax = 0$. *Mỗi nghiệm $x$ thuộc về không gian không của A.*

Phép khử sẽ tìm ra tất cả các nghiệm và xác định không gian con rất quan trọng này.

# *Không gian không (nullspace) N(A) bao gồm tất cả các nghiệm của Ax = 0. Các vectơ x này nằm trong* $\mathbf{R}^n$.

Hãy kiểm tra xem các vectơ nghiệm có tạo thành một không gian con hay không. Giả sử $x$ và $y$ nằm trong không gian không (điều này có nghĩa là $Ax = \mathbf{0}$ và $Ay = \mathbf{0}$). Các quy tắc của phép nhân ma trận cho ta $A(x + y) = \mathbf{0} + \mathbf{0}$. Các quy tắc cũng cho ta $A(cx) = c\mathbf{0}$. Các vế phải vẫn bằng không. Do đó $x + y$ và $cx$ cũng nằm trong không gian không $N(A)$. Vì chúng ta có thể cộng và nhân mà không rời khỏi không gian không, nó là một không gian con.

Xin nhắc lại: Các vectơ nghiệm $x$ có $n$ thành phần. Chúng là các vectơ trong $\mathbf{R}^n$, do đó *không gian không là một không gian con của $\mathbf{R}^n$.* Không gian cột $C(A)$ là một không gian con của $\mathbf{R}^m$.

**Ví dụ 1** Mô tả không gian không của $A = \begin{bmatrix} 1 & 2 \\ 3 & 6 \end{bmatrix}$. Ma trận này là suy biến!

**Giải** Áp dụng phép khử cho các phương trình tuyến tính $Ax = 0$:

| $x_1 + 2x_2 = 0$  | $\rightarrow$ | $x_1 + 2x_2 = 0$          |
|-------------------|---------------|---------------------------|
| $3x_1 + 6x_2 = 0$ |               | $\mathbf{0} = \mathbf{0}$ |

Thực sự chỉ có một phương trình. Phương trình thứ hai là phương trình đầu tiên nhân với 3. Theo hình ảnh hàng (row picture), đường thẳng $x_1 + 2x_2 = 0$ giống hệt với đường thẳng $3x_1 + 6x_2 = 0$. Đường thẳng đó là không gian không $N(A)$. Nó chứa tất cả các nghiệm $(x_1, x_2)$.

Để mô tả các nghiệm của $Ax = 0$, đây là một cách hiệu quả. Chọn một điểm trên đường thẳng (một *"nghiệm đặc biệt"*). Sau đó tất cả các điểm trên đường thẳng đều là các bội số của điểm này. Chúng ta chọn thành phần thứ hai là $x_2 = 1$ (một lựa chọn đặc biệt). Từ phương trình $x_1 + 2x_2 = 0$, thành phần đầu tiên phải là $x_1 = -2$. **Nghiệm đặc biệt là** $s = (-2, 1)$.

**Nghiệm đặc biệt** 
$$As = \mathbf{0}$$
Không gian không của $A = \begin{bmatrix} 1 & 2 \\ 3 & 6 \end{bmatrix}$ chứa tất cả các bội số của $s = \begin{bmatrix} -2 \\ 1 \end{bmatrix}$.

Đây là cách tốt nhất để mô tả không gian không, bằng cách tính toán các nghiệm đặc biệt cho $Ax = \mathbf{0}$. **Nghiệm này đặc biệt vì chúng ta thiết lập biến tự do thành $x_2 = 1$.**

### *Không gian không của A bao gồm tất cả các tổ hợp của các nghiệm đặc biệt của Ax = 0.*

**Ví dụ 2** $x + 2y + 3z = 0$ đến từ ma trận $1 \times 3$ là $A = \begin{bmatrix} 1 & 2 & 3 \end{bmatrix}$. Khi đó $Ax = 0$ tạo ra một mặt phẳng. Tất cả các vectơ trên mặt phẳng đều vuông góc với $(1, 2, 3)$. *Mặt phẳng đó là không gian không của A.* Có hai biến tự do $y$ và $z$: Đặt thành $0$ và $1$.

$$\begin{bmatrix} 1 & 2 & 3 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = 0 \text{ có hai nghiệm đặc biệt } s_1 = \begin{bmatrix} -2 \\ 1 \\ 0 \end{bmatrix} \text{ và } s_2 = \begin{bmatrix} -3 \\ 0 \\ 1 \end{bmatrix}.$$

Những vectơ $s_1$ và $s_2$ này nằm trên mặt phẳng $x + 2y + 3z = 0$. Tất cả các vectơ trên mặt phẳng đều là các tổ hợp của $s_1$ và $s_2$.

Lưu ý điều gì đặc biệt ở $s_1$ và $s_2$. *Hai thành phần cuối cùng là "tự do" và chúng ta chọn chúng một cách đặc biệt là $1, 0$ và $0, 1$.* Sau đó các thành phần đầu tiên $-2$ và $-3$ được xác định bởi phương trình $Ax = 0$.

Các nghiệm của $x + 2y + 3z = 6$ cũng nằm trên một mặt phẳng, nhưng mặt phẳng đó không phải là một không gian con. Vectơ $x = \mathbf{0}$ chỉ là một nghiệm nếu $b = \mathbf{0}$. Phần 3.3 sẽ chỉ ra cách các nghiệm của $Ax = b$ (nếu có bất kỳ nghiệm nào) bị dịch chuyển đi khỏi gốc tọa độ không bởi một nghiệm cụ thể.

Hai bước chính của phần này là **(1)** rút gọn $A$ về dạng **bậc thang theo hàng (row echelon form)** $R$ và **(2)** tìm các **nghiệm đặc biệt cho** $Ax = \mathbf{0}$.

Hiển thị trên trang 138 cho thấy các ma trận $A$ và $R$ kích thước $4 \times 5$, với 3 phần tử xoay.

Các phương trình $Ax = \mathbf{0}$ và cả $Rx = \mathbf{0}$ có $5 - 3 = 2$ nghiệm đặc biệt $s_1$ và $s_2$.

#### **Cột Phần Tử Xoay và Cột Tự Do (Pivot Columns and Free Columns)**

Cột đầu tiên của $A = \begin{bmatrix} 1 & 2 & 3 \end{bmatrix}$ chứa phần tử xoay duy nhất, do đó thành phần đầu tiên của $x$ là *không tự do.* **Các thành phần tự do tương ứng với các cột không có phần tử xoay.** Sự lựa chọn đặc biệt (một hoặc không) chỉ dành cho các biến tự do trong các nghiệm đặc biệt.

**Ví dụ 3** Tìm các không gian không của $A, B, C$ và hai nghiệm đặc biệt cho $Cx = \mathbf{0}$.

$$A = \begin{bmatrix} 1 & 2 \\ 3 & 8 \end{bmatrix} \quad B = \begin{bmatrix} A \\ 2A \end{bmatrix} = \begin{bmatrix} 1 & 2 \\ 3 & 8 \\ 2 & 4 \\ 6 & 16 \end{bmatrix} \quad C = \begin{bmatrix} A & 2A \end{bmatrix} = \begin{bmatrix} 1 & 2 & 2 & 4 \\ 3 & 8 & 6 & 16 \end{bmatrix}.$$

(Lưu ý trong bản gốc có $2A$ nhưng in thành 3 4 cho B, tôi sửa theo đúng $2A$)

**Giải** Phương trình $Ax = 0$ chỉ có nghiệm không $x = 0$. *Không gian không là* $\mathbf{Z}$. Nó chỉ chứa điểm duy nhất $x = 0$ trong $\mathbf{R}^2$. Sự thật này đến từ phép khử:

| $Ax = \begin{bmatrix} 1 & 2 \\ 3 & 8 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$ cho ra $\begin{bmatrix} 1 & 2 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$ và $\begin{bmatrix} x_1 = 0 \\ x_2 = 0 \end{bmatrix}$. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

$A$ khả nghịch. Không có nghiệm đặc biệt. Cả hai cột của ma trận này đều có các phần tử xoay.

Ma trận chữ nhật $B$ có cùng không gian không $\mathbf{Z}$. Hai phương trình đầu tiên trong $Bx = 0$ lại yêu cầu $x = 0$. Hai phương trình cuối cùng cũng sẽ buộc $x = 0$. Khi chúng ta thêm các phương trình phụ (cung cấp thêm các hàng), không gian không chắc chắn không thể trở nên lớn hơn. Các hàng bổ sung áp đặt nhiều điều kiện hơn đối với các vectơ $x$ trong không gian không.

Ma trận chữ nhật $C$ thì khác. Nó có thêm các cột thay vì thêm các hàng. Vectơ nghiệm $x$ có *bốn* thành phần. Phép khử sẽ tạo ra các phần tử xoay ở hai cột đầu tiên của $C$, nhưng **hai cột cuối cùng của $C$ và $U$ là "tự do". Chúng không có phần tử xoay:**

| Trừ $3 \times (\text{hàng 1})$ | $C = \begin{bmatrix} 1 & 2 & 2 & 4 \\ 3 & 8 & 6 & 16 \end{bmatrix}$ | trở thành $U = \begin{bmatrix} 1 & 2 & 2 & 4 \\ 0 & 2 & 0 & 4 \\ \uparrow & \uparrow & \uparrow & \uparrow \end{bmatrix}$ |              |
|--------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|--------------|
| khỏi hàng 2 của $C$ |                                                   | các cột phần tử xoay                                                                                                           | các cột tự do |

Đối với các biến tự do $x_3$ và $x_4$, chúng ta đưa ra những lựa chọn đặc biệt của các số 1 và số 0. Lần thứ nhất $x_3 = 1, x_4 = 0$ và lần thứ hai $x_3 = 0, x_4 = 1$. Các biến phần tử xoay $x_1$ và $x_2$ được xác định bởi phương trình $Ux = 0$ (hoặc $Cx = 0$ hoặc cuối cùng là $Rx = 0$). Chúng ta nhận được hai nghiệm đặc biệt trong không gian không của $C$. Đây cũng là không gian không của $U$: phép khử không làm thay đổi các nghiệm.

| $Cs_1 = 0$ | $s_1 = \begin{bmatrix} -2 \\ 0 \\ 1 \\ 0 \end{bmatrix}$ |
|-------|-----------|
| $Us_1 = 0$ | $s_2 = \begin{bmatrix} 0 \\ -2 \\ 0 \\ 1 \end{bmatrix}$ |
| +---  | các biến phần tử xoay |
| +---  | các biến tự do |

#### **Dạng Bậc Thang Rút Gọn Theo Hàng (Reduced Row Echelon Form)** $R$

Khi $A$ là ma trận chữ nhật, phép khử sẽ không dừng lại ở ma trận tam giác trên $U$. Chúng ta có thể tiếp tục làm cho ma trận này đơn giản hơn, theo hai cách. Những bước này đưa chúng ta đến dạng ma trận $R$ tốt nhất:

- **1.** *Tạo ra các số không phía trên các phần tử xoay.* **Sử dụng các hàng phần tử xoay để khử hướng lên trên trong $R$.**
- **2.** *Tạo ra các số 1 ở các phần tử xoay.* **Chia toàn bộ hàng phần tử xoay cho phần tử xoay của nó.**

Những bước đó không làm thay đổi vectơ không ở vế phải của phương trình. Không gian không giữ nguyên: $N(A) = N(U) = N(R)$. Không gian không này trở nên dễ nhìn thấy nhất khi chúng ta đạt tới *dạng bậc thang rút gọn theo hàng $R = \text{rref}(A)$. Các cột phần tử xoay của $R$ chứa $I$.*

| Dạng rút gọn $R$ | $U = \begin{bmatrix} 1 & 2 & 2 & 4 \\ 0 & 2 & 0 & 4 \end{bmatrix}$ | trở thành | $R = \begin{bmatrix} 1 & 0 & 2 & 0 \\ 0 & 1 & 0 & 2 \\ \uparrow & \uparrow & \uparrow & \uparrow \end{bmatrix}$ |
|------------------|--------------------------------------------------------------------|---------|----------------------------------------------------------------------------------------------------------|
|                  |                                                                    |         |                                                                                                                                  |

Tôi đã trừ hàng 2 của $U$ khỏi hàng 1. Sau đó tôi nhân hàng 2 với $\frac{1}{2}$ để thu được phần tử xoay = 1. Bây giờ **(cột tự do 3) = 2 (cột phần tử xoay 1)**, vì vậy $-2$ xuất hiện trong $s_1 = (-2, 0, 1, 0)$. Các nghiệm đặc biệt dễ tìm hơn rất nhiều từ hệ rút gọn $Rx = 0$. Ở mỗi cột tự do của $R$, tôi đổi tất cả các dấu để tìm $s$. Nghiệm đặc biệt thứ hai $s_2 = (0, -2, 0, 1)$.

Trước khi chuyển sang các ma trận $A$ kích thước $m \times n$ và không gian không $N(A)$ cùng các nghiệm đặc biệt của chúng, cho phép tôi lặp lại một nhận xét. Đối với nhiều ma trận, nghiệm duy nhất của $Ax = 0$ là $x = 0$. Không gian không của chúng $N(A) = \mathbf{Z}$ chỉ chứa vectơ không đó: *không có* các nghiệm đặc biệt. Khi đó, tổ hợp duy nhất của các cột sinh ra $b = 0$ chính là "tổ hợp không" (zero combination). Nghiệm cho $Ax = 0$ là tầm thường (chỉ là $x = 0$) nhưng ý tưởng này thì không tầm thường.

Trường hợp không gian không $\mathbf{Z}$ bằng 0 này có tầm quan trọng lớn nhất. Nó nói rằng các cột của $A$ là **độc lập (independent).** Không có tổ hợp nào của các cột tạo ra vectơ không (ngoại trừ tổ hợp không). Tất cả các cột đều có phần tử xoay, và không có cột nào là tự do. Bạn sẽ gặp lại ý tưởng về tính độc lập này...

#### **Các Biến Phần Tử Xoay và Các Biến Tự Do trong Ma Trận Bậc Thang** $R$

$$A = \begin{bmatrix} p & p & f & p & f \\ | & | & | & | & | \\ | & | & | & | & | \\ | & | & | & | & | \\ | & | & | & | & | \end{bmatrix} \quad R = \begin{bmatrix} 1 & 0 & a & 0 & c \\ 0 & 1 & b & 0 & d \\ 0 & 0 & 0 & 1 & e \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix} \quad s_1 = \begin{bmatrix} -a \\ -b \\ 1 \\ 0 \\ 0 \end{bmatrix} \quad s_2 = \begin{bmatrix} -c \\ -d \\ 0 \\ -e \\ 1 \end{bmatrix}$$

- 3 cột phần tử xoay $p$ chứa ma trận đơn vị $I$ trong các cột phần tử xoay. Các nghiệm đặc biệt $Rs_1 = 0$ và $Rs_2 = 0$.
- 2 cột tự do $f$ chứa $F$ trong các cột tự do. Lấy các phần tử từ $-a$ đến $-e$ từ $R$ để được bộc lộ bởi $R$.
- 3 phần tử xoay: hạng $r = 3$. $Rs = 0$ nghĩa là $As = 0$.

$R$ cho thấy rõ ràng: *cột* $3 = a(\text{cột } 1) + b(\text{cột } 2)$. Điều tương tự cũng phải đúng đối với $A$. Nghiệm đặc biệt $s_1$ lặp lại tổ hợp đó vì vậy $(-a, -b, 1, 0, 0)$ có $Rs_1 = 0$. Không gian không của $A =$ Không gian không của $R =$ tất cả các tổ hợp của $s_1$ và $s_2$.

Dưới đây là các bước cho một ma trận $4 \times 7$ ở dạng *bậc thang rút gọn theo hàng $R$* với ba phần tử xoay:

$R = \begin{bmatrix} 1 & 0 & x & x & x & 0 \\ 0 & 1 & x & x & x & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix}$ (cột cuối có thể là cột 7 tự do tuỳ thuộc bài gốc)

<b>Ba biến phần tử xoay</b> $x_1, x_2, x_6$
<b>Bốn biến tự do</b> $x_3, x_4, x_5, x_7$
<b>Bốn nghiệm đặc biệt</b> $s$ trong $N(R)$
<b>Các hàng và cột phần tử xoay chứa $I$</b>


**Câu hỏi** Không gian cột và không gian không của ma trận $R$ này là gì?

*Câu trả lời* Các cột của $R$ có bốn thành phần nên chúng nằm trong $\mathbf{R}^4$. (Không phải trong $\mathbf{R}^3$!) Thành phần thứ tư của mọi cột đều bằng không. Mọi tổ hợp của các cột — mọi vectơ trong không gian cột — đều có thành phần thứ tư bằng không. *Không gian cột $C(R)$ bao gồm tất cả các vectơ có dạng $(b_1, b_2, b_3, 0)$.* Đối với các vectơ đó, chúng ta có thể giải phương trình $Rx = b$.

Không gian không $N(R)$ là một không gian con của $\mathbf{R}^7$. Các nghiệm của $Rx = 0$ là tất cả các tổ hợp của bốn nghiệm đặc biệt - một nghiệm *cho mỗi biến tự do:*

- **1.** Các cột 3, 4, 5, 7 không có phần tử xoay. Do đó bốn biến tự do là $x_3, x_4, x_5, x_7$.
- **2.** Thiết lập một biến tự do bằng 1 và đặt ba biến tự do còn lại bằng 0.
- **3.** Để tìm $s$, giải $Rx = 0$ để tìm các biến phần tử xoay $x_1, x_2, x_6$.

Việc đếm các phần tử xoay dẫn đến một định lý cực kỳ quan trọng. Giả sử $A$ có số cột nhiều hơn số hàng. *Với $n > m$, có ít nhất một biến tự do.* Hệ phương trình $Ax = 0$ có ít nhất một nghiệm đặc biệt. Nghiệm này *khác không!*

Giả sử $Ax = 0$ có số ẩn nhiều hơn số phương trình ($n > m$, nhiều cột hơn hàng). Phải có ít nhất một cột tự do. **Khi đó $Ax = \mathbf{0}$ có các nghiệm khác không.**

*Một ma trận rộng và ngắn ($n > m$) luôn luôn có các vectơ khác không trong không gian không của nó.* Phải có ít nhất $n - m$ biến tự do, vì số lượng phần tử xoay không thể vượt quá $m$. (Ma trận chỉ có $m$ hàng, và một hàng không bao giờ có hai phần tử xoay.) Tất nhiên một hàng có thể *không có* phần tử xoay nào, điều này đồng nghĩa với một biến tự do bổ sung. Nhưng đây là điểm chính: Khi có một biến tự do, nó có thể được đặt bằng 1. Khi đó phương trình $Ax = 0$ có ít nhất một đường thẳng chứa các nghiệm khác không.

*Không gian không là một không gian con. "Số chiều" (dimension) của nó là số lượng các biến tự do.* Ý tưởng trung tâm này - *số chiều* của một không gian con - được định nghĩa và giải thích trong chương này.

#### **Hạng Của Một Ma Trận (The Rank of a Matrix)**

Các con số $m$ và $n$ cho biết kích thước của một ma trận - nhưng không nhất thiết là *kích thước thực sự (true size)* của một hệ tuyến tính. Một phương trình giống như $0 = 0$ không nên được tính vào. Nếu có hai hàng giống hệt nhau trong $A$, thì hàng thứ hai sẽ biến mất trong phép khử. Ngoài ra nếu hàng 3 là một tổ hợp của các hàng 1 và 2, thì hàng 3 sẽ trở thành toàn số không trong ma trận tam giác $U$ và dạng bậc thang rút gọn $R$. Chúng ta không muốn đếm các hàng gồm toàn số không. *Kích thước thực sự của A được cho bởi hạng của nó.*

#### ĐỊNH NGHĨA VỀ HẠNG (DEFINITION OF RANK) *Hạng của A là số lượng các phần tử xoay. Con số này là r.*

Định nghĩa đó mang tính toán học (computational), và tôi muốn nói thêm về hạng $r$. Ma trận $R$ cuối cùng sẽ có $r$ hàng khác không. Bắt đầu với một ví dụ $3 \times 4$ có hạng $r = 2$:

| Bốn cột | $A = \begin{bmatrix} 1 & 1 & 2 & 4 \\ 1 & 2 & 2 & 5 \\ 1 & 3 & 2 & 6 \end{bmatrix}$ | $R = \begin{bmatrix} 1 & 0 & 2 & 3 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$ |
|--------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
|--------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|

Hai cột đầu tiên của $A$ là $(1, 1, 1)$ và $(1, 2, 3)$, đi theo hai hướng khác nhau. Chúng sẽ là các cột phần tử xoay (được bộc lộ bởi $R$). Cột thứ ba $(2, 2, 2)$ là một bội số của cột đầu tiên. Chúng ta sẽ không thấy một phần tử xoay trong cột thứ ba đó. Cột thứ tư $(4, 5, 6)$ là tổng của ba cột đầu tiên. Cột thứ tư đó cũng sẽ không có phần tử xoay. Hạng của $A$ và $R$ là 2.

Mọi "cột tự do" đều là một tổ hợp của các cột phần tử xoay trước đó. Chính các nghiệm đặc biệt $s$ nói cho chúng ta biết những tổ hợp đó:

$$\begin{aligned} \text{Cột } 3 &= \mathbf{2} \text{ (cột 1)} + \mathbf{0} \text{ (cột 2)} & s_1 &= (-\mathbf{2}, -\mathbf{0}, 1, 0) \\ \text{Cột } 4 &= \mathbf{3} \text{ (cột 1)} + \mathbf{1} \text{ (cột 2)} & s_2 &= (-\mathbf{3}, -\mathbf{1}, 0, 1) \end{aligned}$$

Các con số $2, 0$ trong cột 3 của $R$ xuất hiện trong $s_1$ (với các dấu bị đảo ngược). Và các con số $3, 1$ trong cột 4 của $R$ xuất hiện trong $s_2$ (với các dấu bị đảo ngược thành $-3, -1$).

## Hạng Một (Rank One)

Các ma trận có **hạng một (rank one)** chỉ có **một phần tử xoay**. Khi phép khử tạo ra số không ở cột đầu tiên, nó tạo ra số không ở tất cả các cột. Mỗi hàng là một bội số của hàng phần tử xoay. Đồng thời, mỗi cột là một bội số của cột phần tử xoay!

$$\text{Ma trận hạng một} \quad A = \begin{bmatrix} \mathbf{1} & 3 & 10 \\ \mathbf{2} & 6 & 20 \\ \mathbf{3} & 9 & 30 \end{bmatrix} \quad \longrightarrow \quad R = \begin{bmatrix} \mathbf{1} & 3 & 10 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}.$$

Không gian cột của một ma trận hạng một là "một chiều" (one-dimensional). Ở đây tất cả các cột đều nằm trên đường thẳng đi qua $\mathbf{u} = (1, 2, 3)$. Các cột của $A$ là $\mathbf{u}$ và $3\mathbf{u}$ và $10\mathbf{u}$. Đặt những con số đó vào hàng $\mathbf{v}^T = \begin{bmatrix} \mathbf{1} & 3 & 10 \end{bmatrix}$ và bạn sẽ có dạng hạng một đặc biệt $A = \mathbf{uv}^T$:

$$A = \text{cột nhân hàng} = \mathbf{uv}^T \quad \begin{bmatrix} \mathbf{1} & 3 & 10 \\ 2 & 6 & 20 \\ 3 & 9 & 30 \end{bmatrix} = \begin{bmatrix} \mathbf{1} \\ \mathbf{2} \\ \mathbf{3} \end{bmatrix} \begin{bmatrix} \mathbf{1} & 3 & 10 \end{bmatrix}$$

Với hạng một, phương trình $A\mathbf{x} = \mathbf{0}$ rất dễ hiểu. Phương trình đó $\mathbf{u}(\mathbf{v}^T\mathbf{x}) = \mathbf{0}$ dẫn chúng ta đến $\mathbf{v}^T\mathbf{x} = \mathbf{0}$. Tất cả các vectơ $\mathbf{x}$ trong không gian không (nullspace) đều phải trực giao với $\mathbf{v}$ nằm trong không gian hàng. Đây là hình học khi $r = 1$: **không gian hàng = đường thẳng, không gian không = mặt phẳng vuông góc**.

**Ví dụ 4** Khi tất cả các hàng đều là bội số của một hàng phần tử xoay, hạng là $r = 1$:

$$\begin{bmatrix} \mathbf{1} & 3 & 4 \\ 2 & 6 & 8 \end{bmatrix} \text{ và } \begin{bmatrix} \mathbf{0} & 3 \\ \mathbf{0} & 5 \end{bmatrix} \text{ và } \begin{bmatrix} 5 \\ 2 \end{bmatrix} \text{ và } \begin{bmatrix} 6 & 6 \end{bmatrix} \text{ tất cả đều có hạng 1.}$$

Đối với những ma trận đó, ma trận bậc thang rút gọn theo hàng $R = \mathbf{rref}(A)$ có thể được kiểm tra bằng mắt:

$$R = \begin{bmatrix} \mathbf{1} & 3 & 4 \\ 0 & 0 & 0 \end{bmatrix} \text{ và } \begin{bmatrix} \mathbf{0} & 1 \\ \mathbf{0} & 0 \end{bmatrix} \text{ và } \begin{bmatrix} 1 \\ 0 \end{bmatrix} \text{ và } \begin{bmatrix} 1 & 1 \end{bmatrix} \text{ chỉ có một phần tử xoay.}$$

Định nghĩa thứ hai của chúng ta về hạng sẽ ở một cấp độ cao hơn. Nó giải quyết toàn bộ các hàng và toàn bộ các cột - các vectơ chứ không chỉ là các con số. Tất cả ba ma trận $A$ và $U$ và $R$ đều có $r$ **hàng độc lập**.

$A$ và $U$ và $R$ cũng có $r$ **cột độc lập** (các cột phần tử xoay). Mục 3.4 sẽ nói về việc các hàng hoặc các cột độc lập với nhau có nghĩa là gì.

Định nghĩa thứ ba về hạng, ở cấp độ cao nhất của đại số tuyến tính, sẽ giải quyết các *không gian* của các vectơ. *Hạng r là "số chiều" của không gian cột. Nó cũng là số chiều của không gian hàng.* Điều tuyệt vời là $n - r$ **là số chiều của không gian không.**

#### **• ÔN TẬP CÁC Ý TƯỞNG CHÍNH (REVIEW OF THE KEY IDEAS) •**

- **1.** Không gian không $N(A)$ là một không gian con của $\mathbf{R}^n$. Nó chứa tất cả các nghiệm của $Ax = 0$.
- **2.** Phép khử trên $A$ tạo ra một ma trận rút gọn theo hàng $R$ với các cột phần tử xoay và các cột tự do.
- **3.** Mỗi cột tự do dẫn đến một nghiệm đặc biệt. Biến tự do đó bằng 1, các biến khác bằng 0.
- **4.** *Hạng r* của $A$ là số lượng các phần tử xoay. Tất cả các phần tử xoay đều là các số 1 trong $R = \text{rref}(A)$.
- **5.** Nghiệm tổng quát của $Ax = 0$ là một tổ hợp của $n - r$ nghiệm đặc biệt.
- **6.** $A$ luôn luôn có một cột tự do nếu $n > m$, cho ra một *nghiệm khác không* cho $Ax = \mathbf{0}$.

#### **• CÁC VÍ DỤ ĐÃ GIẢI (WORKED EXAMPLES) •**

**3.2 A** Tại sao $A$ và $R$ có cùng không gian không nếu $EA = R$ và $E$ khả nghịch?

**Giải** Nếu $Ax = 0$ thì $Rx = EAx = E0 = 0$

| Nếu $Rx = 0$ thì | $Ax = E^{-1}Rx = E^{-1}0 = 0$ |
|------------------|-------------------------------|
|                  |                               |

$A$ và $R$ cũng có cùng không gian hàng và cùng hạng.

**3.2 B** Hãy tạo ra một ma trận $R$ kích thước $3 \times 4$ mà các nghiệm đặc biệt của phương trình $Rx = 0$ là $s_1$ và $s_2$:

$$s_1 = \begin{bmatrix} -3 \\ 1 \\ 0 \\ 0 \end{bmatrix} \quad \text{và} \quad s_2 = \begin{bmatrix} -2 \\ 0 \\ -6 \\ 1 \end{bmatrix} \quad \text{cột phần tử xoay 1 và 3} \\ \text{biến tự do } x_2 \text{ và } x_4$$

Mô tả tất cả các ma trận $A$ có thể có với không gian không $N(A)$ = tất cả các tổ hợp của $s_1$ và $s_2$ này.

**Giải** Ma trận rút gọn $R$ có các phần tử xoay = 1 ở các cột 1 và 3. Không có phần tử xoay thứ ba, do đó hàng 3 của $R$ gồm toàn số không. Các cột tự do 2 và 4 sẽ là các tổ hợp của các cột phần tử xoay: $3, 0, 2, 6$ trong $R$ đến từ $-3, -0, -2, -6$ trong $s_1$ và $s_2$. **Mọi** $A = ER$.

Mọi ma trận $3 \times 4$ đều có ít nhất một nghiệm đặc biệt. *Những ma trận này có hai nghiệm đặc biệt.*

| $R = \begin{bmatrix} 1 & 3 & 0 & 2 \\ 0 & 0 & 1 & 6 \\ 0 & 0 & 0 & 0 \end{bmatrix}$ | có | $Rs_1 = \mathbf{0}$ | và | $Rs_2 = \mathbf{0}.$ |
|-------------------------------------------------------------------------------------|-----|---------------------|-----|----------------------|
|-------------------------------------------------------------------------------------|-----|---------------------|-----|----------------------|

**3.2 C** Tìm dạng ma trận rút gọn theo hàng $R$ và hạng $r$ của $A$ và $B$ (những giá trị này phụ thuộc vào $c$). Các cột phần tử xoay của $A$ là những cột nào? Các nghiệm đặc biệt là gì?

| Tìm các nghiệm đặc biệt | $A = \begin{bmatrix} 1 & 2 & 1 \\ 3 & 6 & 3 \\ 4 & 8 & c \end{bmatrix}$ | và | $B = \begin{bmatrix} c & c \\ c & c \end{bmatrix}$ |
|------------------------|-------------------------------------------------------------------------|-----|----------------------------------------------------|
|------------------------|-------------------------------------------------------------------------|-----|----------------------------------------------------|

**Giải** Ma trận $A$ có hàng 2 = 3 (hàng 1). Hạng của $A$ là $r = 2$ *trừ khi* $c = 4$. Hàng 3 - 4 (hàng 1) kết thúc bằng $c - 4$. Các phần tử xoay nằm ở cột 1 và cột 3. Biến thứ hai $x_2$ là tự do. Chú ý dạng của $R$: Hàng 3 đã di chuyển lên thành hàng 2.
(Ghi chú: Lỗi OCR ở bản gốc: "Row 4 - 4 (row 1) ends inc - 4" và các đoạn vô nghĩa sau đó. Ta dịch phần đúng: Hàng 3 trừ đi 4 lần hàng 1 kết thúc bằng $c - 4$. Các phần tử xoay nằm ở cột 1 và 3. Biến thứ hai $x_2$ là tự do. Chú ý dạng của $R$: Hàng 3 đã di chuyển lên thành hàng 2).

Hai phần tử xoay để lại một biến tự do $x_2$. Nhưng khi $c = 4$, phần tử xoay duy nhất nằm ở cột 1 (hạng một). Các biến thứ hai và thứ ba là tự do, tạo ra hai nghiệm đặc biệt:

| $c \neq 4$ | Nghiệm đặc biệt $(-2, 1, 0)$ | $c = 4$ | Một nghiệm đặc biệt khác $(-1, 0, 1)$ |
|------------|-------------------------------|---------|---------------------------------------|
|            |                               |         |                                       |

Ma trận $2 \times 2$ là $B = \begin{bmatrix} c & c \\ c & c \end{bmatrix}$ có hạng $r = 1$ *trừ khi $c = 0$*, khi đó hạng là không!

| $c \neq 0$ | $R = \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}$ | $c = 0$ | $R = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$ | và không gian không = $\mathbf{R}^2$. |
|------------|----------------------------------------------------|---------|----------------------------------------------------|----------------------------------|
|            |                                                    |         |                                                    |                                  |

### **Bài Tập 3.2 (Problem Set 3.2)**

**1** Rút gọn $A$ và $B$ về các dạng ma trận bậc thang (echelon forms) $U$ của chúng. Các biến nào là tự do?

Rút gọn $A$ và $B$ về các dạng ma trận bậc thang tam giác $U$ của chúng. Chúng ta có $A = \begin{bmatrix} 1 & 2 & 2 & 4 & 6 \\ 1 & 2 & 3 & 6 & 9 \\ 0 & 0 & 1 & 2 & 3 \end{bmatrix}$ và $B = \begin{bmatrix} 2 & 4 & 2 \\ 0 & 4 & 4 \\ 0 & 8 & 8 \end{bmatrix}$.

**2** Đối với các ma trận trong Bài Tập 1, hãy tìm một nghiệm đặc biệt cho mỗi biến tự do. (Thiết lập biến tự do bằng 1. Thiết lập các biến tự do khác bằng không.)
**3** Bằng các thao tác hàng tiếp theo trên mỗi $U$ ở Bài Tập 1, hãy tìm dạng bậc thang rút gọn $R$. *Đúng hay sai kèm theo lý do:* Không gian không của $R$ bằng không gian không của $U$.
**4** Đối với cùng các ma trận $A$ và $B$ đó, hãy tìm các nghiệm đặc biệt cho $Ax = 0$ và $Bx = 0$. Đối với một ma trận kích thước $m \times n$, số lượng biến phần tử xoay cộng với số lượng biến tự do bằng \_\_. Đây là **Định Lý Đếm (Counting Theorem)**: $r + (n - r) = n$.

| (a) | $A = \begin{bmatrix} -1 & 3 & 5 \\ -2 & 6 & 10 \end{bmatrix}$ | (b) | $B = \begin{bmatrix} -1 & 3 & 5 \\ -2 & 6 & 10 \end{bmatrix}$ |
|-----|---------------------------------------------------------------|-----|---------------------------------------------------------------|
|-----|---------------------------------------------------------------|-----|---------------------------------------------------------------|

### Các câu hỏi 5-14 là về các biến tự do và các biến phần tử xoay.

- **5** Đúng hay sai (kèm theo lý do nếu đúng hoặc ví dụ để chứng minh nó sai):
  - (a) Một ma trận vuông không có các biến tự do.
  - (b) Một ma trận khả nghịch không có các biến tự do.
  - (c) Một ma trận $m \times n$ không có nhiều hơn $n$ biến phần tử xoay.
  - (d) Một ma trận $m \times n$ không có nhiều hơn $m$ biến phần tử xoay.
**6** Đặt càng nhiều số 1 càng tốt vào một ma trận bậc thang $4 \times 7$ $U$ mà các cột phần tử xoay của nó là
- (a) 2, 4, 5 (b) 1, 3, 6, 7 (c) 4 và 6.
**7** Đặt càng nhiều số 1 càng tốt vào một ma trận bậc thang *rút gọn* $4 \times 8$ $R$ sao cho các cột tự do là
- (a) 2, 4, 5, 6 (b) 1, 3, 6, 7, 8.
**8** Giả sử cột 4 của một ma trận $3 \times 5$ chứa toàn số không. Khi đó $x_4$ chắc chắn là một biến \_\_. Nghiệm đặc biệt cho biến này là vectơ $x =$ \_\_.
**9** Giả sử cột đầu tiên và cột cuối cùng của một ma trận $3 \times 5$ giống nhau (không phải bằng không). Khi đó \_\_ là một biến tự do. Tìm nghiệm đặc biệt cho biến này.
**10** Giả sử một ma trận $m \times n$ có $r$ phần tử xoay. Số lượng các nghiệm đặc biệt là \_\_. Không gian không chỉ chứa $x = 0$ khi $r =$ \_\_. Không gian cột là toàn bộ $\mathbf{R}^m$ khi $r =$ \_\_.
**11** Không gian không của một ma trận $5 \times 5$ chỉ chứa $x = 0$ khi ma trận có \_\_ phần tử xoay. Không gian cột là $\mathbf{R}^5$ khi có \_\_ phần tử xoay. Giải thích tại sao.
**12** Phương trình $x - 3y - z = 0$ xác định một mặt phẳng trong $\mathbf{R}^3$. Ma trận $A$ trong phương trình này là gì? Các biến nào là tự do? Các nghiệm đặc biệt là \_\_ và \_\_.
**13** (Khuyên làm) Mặt phẳng $x - 3y - z = 12$ song song với $x - 3y - z = 0$. Một điểm cụ thể trên mặt phẳng này là $(12, 0, 0)$. Tất cả các điểm trên mặt phẳng đều có dạng

$$\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 12 \\ 0 \\ 0 \end{bmatrix} + y \begin{bmatrix} 3 \\ 1 \\ 0 \end{bmatrix} + z \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}.$$ (sửa lỗi in trong sách cho đúng dạng nghiệm)

**14** Giả sử cột 1 + cột 3 + cột 5 = 0 trong một ma trận $4 \times 5$ có bốn phần tử xoay. Cột nào không có phần tử xoay? Nghiệm đặc biệt là gì? Mô tả $N(A)$.

Các câu hỏi 15-22 yêu cầu các ma trận (nếu có thể) với các tính chất cụ thể.

**15** Xây dựng một ma trận sao cho $N(A)$ = tất cả các tổ hợp của $(2, 2, 1, 0)$ và $(3, 1, 0, 1)$.
**16** Xây dựng $A$ sao cho $N(A)$ = tất cả các bội số của $(4, 3, 2, 1)$. Hạng của nó là \_\_.

- **17** Xây dựng một ma trận có không gian cột chứa $(1, 1, 5)$ và $(0, 3, 1)$ và có không gian không chứa $(1, 1, 2)$.
**18** Xây dựng một ma trận có không gian cột chứa $(1, 1, 0)$ và $(0, 1, 1)$ và có không gian không chứa $(1, 0, 1)$ và $(0, 0, 1)$.
**19** Xây dựng một ma trận có không gian cột chứa $(1, 1, 1)$ và có không gian không là đường thẳng của các bội số của $(1, 1, 1, 1)$.
**20** Xây dựng một ma trận $2 \times 2$ có không gian không bằng không gian cột của nó. Điều này là có thể.
**21** Tại sao không có ma trận $3 \times 3$ nào có không gian không bằng không gian cột của nó?
**22** Nếu $AB = 0$ thì không gian cột của $B$ được chứa trong \_\_ của $A$. Tại sao?
**23** Dạng rút gọn $R$ của một ma trận $3 \times 3$ với các phần tử được chọn ngẫu nhiên hầu như chắc chắn sẽ là \_\_. Ma trận $R$ nào gần như chắc chắn sẽ xảy ra nếu ma trận ngẫu nhiên $A$ là $4 \times 3$?
**24** Chứng minh bằng ví dụ rằng ba khẳng định này nói chung là *sai:*
  - (a) $A$ và $A^T$ có cùng không gian không.
  - (b) $A$ và $A^T$ có cùng các biến tự do.
  - (c) Nếu $R$ là dạng rút gọn $\text{rref}(A)$ thì $R^T$ là $\text{rref}(A^T)$.
**25** Nếu $N(A)$ = tất cả các bội số của $x = (2, 1, 0, 1)$, thì $R$ là gì và hạng của nó là bao nhiêu?
**26** Nếu các nghiệm đặc biệt cho $Rx = 0$ nằm trong các cột của các ma trận không gian không $N$ này, hãy đi ngược lại để tìm các hàng khác không của các ma trận rút gọn $R$:

| $N = \begin{bmatrix} 2 & 3 \\ 1 & 0 \\ 0 & 1 \end{bmatrix}$ | và | $N = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$ | và | $N = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$ | (rỗng $3 \times 1$). |
|-------------------------------------------------------------|-----|-------------------------------------------------|-----|-------------------------------------------------|-----------------|
|-------------------------------------------------------------|-----|-------------------------------------------------|-----|-------------------------------------------------|-----------------|

- **27** (a) Năm ma trận rút gọn $R$ $2 \times 2$ mà các phần tử của chúng chỉ toàn là 0 và 1 là gì?

- (b) Tám ma trận $1 \times 3$ chỉ chứa các số 0 và 1 là những ma trận nào? Có phải tất cả tám ma trận đó đều là các ma trận bậc thang rút gọn $R$ không?
**28** Giải thích tại sao $A$ và $-A$ luôn luôn có cùng dạng bậc thang rút gọn $R$.
**29** Nếu $A$ kích thước $4 \times 4$ và khả nghịch, hãy mô tả không gian không của ma trận $4 \times 8$ $B = \begin{bmatrix} A & A \end{bmatrix}$.
**30** Không gian không $N(C)$ liên hệ như thế nào với các không gian $N(A)$ và $N(B)$, nếu $C = \begin{bmatrix} A \\ B \end{bmatrix}$? (Ghi chú: Sửa lỗi OCR của bản gốc $C = [1]$ thành dạng block ma trận hợp lý cho bài toán).
**31** Tìm các dạng bậc thang rút gọn theo hàng $R$ và hạng của các ma trận này:
  - (a) Ma trận $3 \times 4$ có tất cả các phần tử đều bằng 4.
  - (b) Ma trận $3 \times 4$ với $a_{ij} = i + j - 1$.
  - (c) Ma trận $3 \times 4$ với $a_{ij} = (-1)^j$.

**32** Định luật Dòng điện Kirchhoff (Kirchhoff's Current Law) $A^Ty = 0$ nói rằng *dòng điện đi vào = dòng điện đi ra* tại mỗi nút. Tại nút 1 điều này là $y_3 = y_1 + y_4$. Hãy viết bốn phương trình cho Định luật Kirchhoff tại bốn nút (các mũi tên chỉ chiều dương của mỗi $y$). Rút gọn $A^T$ về $R$ và tìm ba nghiệm đặc biệt trong không gian không của $A^T$ (ma trận $4 \times 6$).

![](images/_page_154_Diagram_3.jpeg)

- **33** Khẳng định nào sau đây đưa ra định nghĩa đúng về *hạng* của $A$?
  - (a) Số lượng các hàng khác không trong $R$.
  - (b) Số lượng các cột trừ đi tổng số lượng các hàng. 
  - (c) Số lượng các cột trừ đi số lượng các cột tự do. 
  - (d) Số lượng các số 1 trong ma trận $R$.
**34** Tìm ma trận rút gọn $R$ cho mỗi (khối) ma trận sau:

| $A = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 3 \\ 2 & 4 & 6 \end{bmatrix}$ | $B = \begin{bmatrix} A & A \end{bmatrix}$ | $C = \begin{bmatrix} A & A \\ A & 0 \end{bmatrix}$ |
|-------------------------------------------------------------------------|-------------------|----------------------------------------------------|
|-------------------------------------------------------------------------|-------------------|----------------------------------------------------|

**35** Giả sử tất cả các biến phần tử xoay xuất hiện *ở cuối* thay vì ở đầu. Mô tả tất cả bốn khối trong dạng bậc thang rút gọn (khối $B$ phải là $r \times r$):

$$R = \begin{bmatrix} A & B \\ C & D \end{bmatrix}.$$

**36** (Bài toán ngớ ngẩn) Mô tả tất cả các ma trận $2 \times 3$ $A_1$ và $A_2$, với các dạng bậc thang theo hàng $R_1$ và $R_2$, sao cho $R_1 + R_2$ là dạng bậc thang theo hàng của $A_1 + A_2$. Có đúng là $R_1 = A_1$ và $R_2 = A_2$ trong trường hợp này không? $R_1 - R_2$ có bằng $\text{rref}(A_1 - A_2)$ không?

**37** Nếu $A$ có $r$ cột phần tử xoay, làm sao bạn biết rằng $A^T$ có $r$ cột phần tử xoay? Đưa ra một ví dụ $3 \times 3$ với các số lượng cột phần tử xoay (pivcol) khác nhau đối với $A$ và $A^T$.

**38** Các nghiệm đặc biệt của $Rx = 0$ và $y^TR = 0$ đối với những $R$ này là gì?

Ma trận không gian không $N$ chứa các nghiệm đặc biệt là gì?

| $R =$ | $\begin{bmatrix} 0 & 0 & 2 & 3 \\ 0 & 1 & 4 & 5 \\ 0 & 0 & 0 & 0 \end{bmatrix}$ | $R = \begin{bmatrix} 0 & 1 & 2 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$ |
|-------|---------------------------------------------------------------------------------|-------------------------------------------------------------------------|
|       |                                                                                 |                                                                         |

**39** Điền vào các ma trận này sao cho chúng có hạng 1:

$$A = \begin{bmatrix} 1 & 2 & 4 \\ 2 & & \\ 4 & & \end{bmatrix} \quad \text{và} \quad B = \begin{bmatrix} 9 & & \\ 1 & 6 & -3 \\ 2 & 6 & -3 \end{bmatrix} \quad \text{và} \quad M = \begin{bmatrix} a & b \\ c & \end{bmatrix}.$$

**40** Nếu $A$ là một ma trận $m \times n$ với hạng $r = 1$, các cột của nó là bội số của một cột và các hàng của nó là bội số của một hàng. Không gian cột là một \_\_ trong $\mathbf{R}^m$. Không gian không là một \_\_ trong $\mathbf{R}^n$. Ma trận không gian không $N$ có hình dạng \_\_.
**41** Chọn các vectơ $u$ và $v$ sao cho $A = uv^T =$ cột nhân hàng:

| $A = \begin{bmatrix} 3 & 6 & 6 \\ 1 & 2 & 2 \\ 4 & 8 & 8 \end{bmatrix}$ | và | $A = \begin{bmatrix} 2 & 2 & 6 & 4 \\ -1 & -1 & -3 & -2 \end{bmatrix}$ |
|-------------------------------------------------------------------------|-----|------------------------------------------------------------------------|
|-------------------------------------------------------------------------|-----|------------------------------------------------------------------------|

*$A = uv^T$ là dạng tự nhiên của mọi ma trận có hạng r = 1.*

**42** Nếu $A$ là một ma trận hạng một, thì hàng thứ hai của $R$ là \_\_. Cho một ví dụ.

Các Bài toán 43-45 là về các ma trận con $r \times r$ khả nghịch bên trong $A$.

**43** *Nếu A có hạng r, thì nó có một ma trận con $r \times r$ S khả nghịch.* Bỏ đi $m - r$ hàng và $n - r$ cột để tìm một ma trận con $S$ khả nghịch bên trong $A, B$, và $C$. Bạn có thể giữ lại các hàng phần tử xoay và các cột phần tử xoay:

| $A = \begin{bmatrix} 1 & 2 & 3 \\ 1 & 2 & 4 \end{bmatrix}$ | $B = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix}$ | $C = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 1 \end{bmatrix}$ |
|------------------------------------------------------------|------------------------------------------------------------|-------------------------------------------------------------------------|
|------------------------------------------------------------|------------------------------------------------------------|-------------------------------------------------------------------------|

**44** Giả sử $P$ chỉ chứa $r$ cột phần tử xoay của một ma trận $m \times n$. Giải thích tại sao ma trận con $m \times r$ $P$ này có hạng $r$.
**45** Chuyển vị $P$ trong Bài tập 44. Tìm $r$ cột phần tử xoay của $P^T$ (là $r \times m$). Bằng cách chuyển vị trở lại, thao tác này tạo ra một ma trận con $r \times r$ khả nghịch $S$ bên trong $P$ và $A$:

| Cho $A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 2 & 4 & 7 \end{bmatrix}$ | tìm $P$ ($3 \times 2$) và sau đó là $S$ khả nghịch ($2 \times 2$). |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
|-----------------------------------------------------------------------------|---------------------------------------------------------|

**Các Bài toán 46-51** chứng minh **rằng** $\text{rank}(AB)$ **không lớn hơn** $\text{rank}(A)$ **hoặc** $\text{rank}(B)$.

**46** Tìm hạng của $AB$ và $AC$ (ma trận hạng một nhân với ma trận hạng một):

| $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$ | và | $B = \begin{bmatrix} 2 & 1 & 4 \\ 3 & 1.5 & 6 \end{bmatrix}$ | và | $C = \begin{bmatrix} 1 & b \\ c & bc \end{bmatrix}$ |
|----------------------------------------------------|-----|--------------------------------------------------------------|-----|-----------------------------------------------------|
|----------------------------------------------------|-----|--------------------------------------------------------------|-----|-----------------------------------------------------|

**47** Ma trận hạng một $uv^T$ nhân ma trận hạng một $wz^T$ bằng $uz^T$ nhân con số \_\_. Tích số $uv^Twz^T$ này cũng có hạng một trừ khi \_\_ $= 0$.

- **48** (a) Giả sử cột $j$ của $B$ là một tổ hợp của các cột trước đó của $B$. Chứng minh rằng cột $j$ của $AB$ cũng là chính tổ hợp đó của các cột trước đó của $AB$. Do đó $AB$ không thể có các cột phần tử xoay mới, vậy $\text{rank}(AB) \leq \text{rank}(B)$.
  - (b) Tìm $A_1$ và $A_2$ sao cho $\text{rank}(A_1B) = 1$ và $\text{rank}(A_2B) = 0$ đối với $B = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$. 
**49** Bài tập 48 đã chứng minh rằng $\text{rank}(AB) \leq \text{rank}(B)$. Khi đó cùng một lập luận sẽ cho $\text{rank}(B^TA^T) \leq \text{rank}(A^T)$. Làm thế nào bạn suy ra được $\text{rank}(AB) \leq \text{rank}(A)$?
**50** *(Quan trọng)* Giả sử $A$ và $B$ là các ma trận $n \times n$, và $AB = I$. Hãy chứng minh từ $\text{rank}(AB) \leq \text{rank}(A)$ rằng hạng của $A$ là $n$. Vì vậy $A$ khả nghịch và $B$ phải là ma trận nghịch đảo hai phía của nó (Phần 2.5). Do đó $BA = I$ *(điều này không quá hiển nhiên!).*
**51** Nếu $A$ là $2 \times 3$ và $B$ là $3 \times 2$ và $AB = I$, hãy chứng minh từ hạng của nó rằng $BA \neq I$. Hãy cho một ví dụ về $A$ và $B$ với $AB = I$. Với $m < n$, một nghịch đảo phải (right inverse) không phải là nghịch đảo trái (left inverse).
**52** Giả sử $A$ và $B$ có *cùng* dạng ma trận bậc thang rút gọn theo hàng $R$.
  - (a) Chứng minh rằng $A$ và $B$ có cùng không gian không và cùng không gian hàng.
  - (b) Chúng ta biết $E_1A = R$ và $E_2B = R$. Vì vậy $A$ bằng một ma trận \_\_ nhân với $B$.
**53** Biểu diễn $A$ và sau đó là $B$ dưới dạng tổng của hai ma trận hạng một:

| rank = 2 | $A = \begin{bmatrix} 1 & 1 & 0 \\ 1 & 1 & 4 \\ 1 & 1 & 8 \end{bmatrix}$ | $B = \begin{bmatrix} 2 & 2 \\ 2 & 3 \end{bmatrix}$ |
|----------|-------------------------------------------------------------------------|----------------------------------------------------|
|----------|-------------------------------------------------------------------------|----------------------------------------------------|

**54** Trả lời các câu hỏi tương tự như trong Ví Dụ Đã Giải **3.2 C** đối với

| $A = \begin{bmatrix} 1 & 1 & 2 & 2 \\ 2 & 2 & 4 & 4 \\ 1 & c & 2 & 2 \end{bmatrix}$ | và | $B = \begin{bmatrix} 1-c & 2 \\ 0 & 2-c \end{bmatrix}$ |
|-------------------------------------------------------------------------------------|-----|--------------------------------------------------------|
|-------------------------------------------------------------------------------------|-----|--------------------------------------------------------|

**55** Ma trận không gian không $N$ (chứa các nghiệm đặc biệt) của $A, B, C$ là gì?

| Ma trận khối | $A = \begin{bmatrix} I & I \end{bmatrix}$ | và | $B = \begin{bmatrix} I & I \\ 0 & 0 \end{bmatrix}$ | và | $C = \begin{bmatrix} I & I & I \end{bmatrix}$ |
|----------------|---------------|-----|----------------------------------------------------|-----|-------------------|
|----------------|---------------|-----|----------------------------------------------------|-----|-------------------|

**56** *Sự thật thú vị: Mỗi ma trận $m \times n$ hạng $r$ đều có thể phân tích thành (ma trận kích thước $m \times r$) nhân với (ma trận kích thước $r \times n$):*

$$A = (\text{các cột phần tử xoay của } A) \times (r \text{ hàng đầu tiên của } R) = (\mathbf{COL})(\mathbf{ROW}).$$

Hãy viết ma trận $3 \times 4$ $A$ toàn số một thành tích của ma trận $3 \times 1$ từ các cột phần tử xoay và ma trận $1 \times 4$ từ $R$.

# Bài Tập Thử Thách (Challenge Problems)

**57** Giả sử $A$ là một ma trận $m \times n$ hạng $r$. Dạng bậc thang rút gọn của nó là $R$. Hãy mô tả chính xác ma trận $Z$ (hình dạng của nó và tất cả các phần tử của nó) đến từ việc *chuyển vị dạng ma trận bậc thang rút gọn theo hàng của $R^T$:*

| $R = \text{rref}(A)$ | và | $Z = (\text{rref}(A^T))^T$ |
|----------------------|-----|----------------------------|
|                      |     |                            |

**58** (Khuyên làm) Giả sử $R$ kích thước $m \times n$ hạng $r$, với các cột phần tử xoay ở trước:

$$R = \begin{bmatrix} I & F \\ 0 & 0 \end{bmatrix}.$$

- (a) Hình dạng của bốn khối đó là gì?
- (b) Tìm một *nghịch đảo phải (right-inverse) B* với $RB = I$ nếu $r = m$. Các khối số không đã biến mất. 
- (c) Tìm một *nghịch đảo trái (left-inverse) C* với $CR = I$ nếu $r = n$. Khối $F$ và cột $0$ đã biến mất.
- (d) Dạng ma trận bậc thang rút gọn theo hàng của $R^T$ (với các hình dạng) là gì?
- (e) Dạng ma trận bậc thang rút gọn theo hàng của $R^TR$ (với các hình dạng) là gì?
**59** Tôi nghĩ rằng dạng bậc thang rút gọn của $R^TR$ luôn luôn là $R$ (ngoại trừ các hàng số không thừa). Bạn có thể làm một ví dụ khi $R$ kích thước $2 \times 3$ không? Sau này chúng ta sẽ chỉ ra rằng $A^TA$ luôn luôn có cùng không gian không giống như $A$ (một sự thật quý giá). 
**60** Giả sử bạn cho phép các phép toán *cột* sơ cấp trên $A$ cũng như các phép toán hàng sơ cấp (những phép toán đưa về $R$). "Dạng rút gọn theo hàng-và-cột" đối với một ma trận $m \times n$ hạng $r$ là gì?

# **Phép Khử: Bức Tranh Lớn (Elimination: The Big Picture)**

Trang này giải thích phép khử ở cấp độ vectơ và cấp độ không gian con, khi $A$ được rút gọn thành $R$. Bạn đã biết các bước và tôi sẽ không lặp lại chúng. Phép khử bắt đầu bằng phần tử xoay đầu tiên. Nó di chuyển từng cột một (từ trái sang phải) và từng hàng một (từ trên xuống dưới). Khi di chuyển, phép khử trả lời hai câu hỏi:

#### **Câu hỏi 1: Cột này có phải là một tổ hợp của các cột trước đó hay không?**

Nếu cột có chứa một phần tử xoay, câu trả lời là không. Các cột phần tử xoay "độc lập" với các cột trước đó. Nếu cột 4 không có phần tử xoay, nó là một tổ hợp của các cột 1, 2, 3.

### **Câu hỏi 2: Hàng này có phải là một tổ hợp của các hàng trước đó hay không?**

Nếu hàng có chứa một phần tử xoay, câu trả lời là không. Các hàng phần tử xoay "độc lập" với các hàng trước đó. Nếu hàng 3 kết thúc không có phần tử xoay nào, nó là một hàng số không và nó được chuyển xuống dưới cùng của $R$.

Tôi thấy thật đáng kinh ngạc khi chỉ một lần đi qua ma trận lại trả lời được cả hai câu hỏi. Thực ra lần đi qua đó đạt tới ma trận bậc thang tam giác $U$, không phải là ma trận bậc thang rút gọn $R$. Sau đó việc rút gọn từ $U$ xuống $R$ đi từ dưới lên trên. $U$ cho biết những cột nào là các tổ hợp của các cột trước đó (các phần tử xoay bị thiếu). Sau đó $R$ *nói cho chúng ta biết những tổ hợp đó là gì.*

Nói cách khác, $R$ **cho chúng ta biết các nghiệm đặc biệt của** $Ax = \mathbf{0}$. Chúng ta có thể đi đến $R$ từ $A$ bằng các bước khử và hoán đổi hàng khác nhau, nhưng nó sẽ luôn luôn là cùng một $R$ (bởi vì các nghiệm đặc biệt được quyết định bởi $A$). Trong ngôn ngữ sắp tới, $R$ tiết lộ một "cơ sở" (basis) cho ba không gian con cơ bản (fundamental subspaces):

**Không gian cột (column space)** của $A$ - chọn các cột phần tử xoay của $A$ làm cơ sở.

**Không gian hàng (row space)** của $A$ - chọn các hàng khác không của $R$ làm cơ sở.

**Không gian không (nullspace)** của $A$ - chọn các nghiệm đặc biệt của $Rx = 0$ (và $Ax = 0$).

Chúng ta học được từ phép khử con số duy nhất quan trọng nhất - **hạng** $r$. Con số đó đếm các cột phần tử xoay và các hàng phần tử xoay. Khi đó $n - r$ đếm số lượng các cột tự do và các nghiệm đặc biệt.

Tôi đề cập rằng việc rút gọn $\begin{bmatrix} A & I \end{bmatrix}$ thành $\begin{bmatrix} R & E \end{bmatrix}$ sẽ nói cho bạn biết nhiều điều hơn về $A$ - trên thực tế là hầu như mọi thứ (bao gồm cả $EA = R$). Ma trận $E$ lưu giữ một bản ghi, mặt khác sẽ bị mất, của phép khử từ $A$ sang $R$. Khi $A$ là ma trận vuông và khả nghịch, $R$ là $I$ và $E$ là $A^{-1}$.

### 3.3 Nghiệm Toàn Diện Của $Ax = b$

1. **Nghiệm toàn diện của $Ax = b$**: $x = (\text{một nghiệm cụ thể } x_p) + (\text{bất kỳ } x_n \text{ trong không gian không})$.
2. Phép khử trên $\begin{bmatrix} A & b \end{bmatrix}$ dẫn đến $\begin{bmatrix} R & d \end{bmatrix}$. Khi đó $Ax = b$ tương đương với $Rx = d$.
3. $Ax = b$ và $Rx = d$ chỉ có thể giải được khi tất cả các hàng số không của $R$ đều có các số không tương ứng ở $d$.
4. Khi $Rx = d$ giải được, một nghiệm rất cụ thể $x_p$ có tất cả các biến tự do bằng không.
5. $A$ có **hạng cột đầy đủ (full column rank)** $r = n$ khi không gian không của nó $N(A) = \text{vectơ không: không có biến tự do}$.
6. $A$ có **hạng hàng đầy đủ (full row rank)** $r = m$ khi không gian cột $C(A)$ là $\mathbf{R}^m$: $Ax = b$ luôn giải được.
7. Bốn trường hợp là $r = m = n$ ($A$ khả nghịch) và $r = m < n$ (mọi $Ax = b$ đều giải được) và $r = n < m$ ($Ax = b$ có 1 hoặc 0 nghiệm) và $r < m, r < n$ (0 hoặc $\infty$ nghiệm).

Phần trước đã giải hoàn toàn phương trình $Ax = 0$. Phép khử chuyển đổi bài toán thành $Rx = 0$. Các biến tự do được gán những giá trị đặc biệt (một và không). Sau đó các biến phần tử xoay được tìm bằng phép thế ngược. Chúng ta đã không chú ý đến vế phải $b$ bởi vì nó vẫn bằng không. Nghiệm $x$ nằm trong không gian không của $A$.

Bây giờ $b$ không phải là số không. Các phép toán hàng trên vế trái cũng phải tác động lên vế phải. $Ax = b$ được rút gọn thành một hệ đơn giản hơn $Rx = d$ với cùng các nghiệm. Một cách để tổ chức việc đó là **thêm $b$ như một cột bổ sung của ma trận**. Tôi sẽ “mở rộng” $A$ với vế phải $(b_1, b_2, b_3) = (1, 6, 7)$ để tạo ra **ma trận mở rộng (augmented matrix)** $\begin{bmatrix} A & b \end{bmatrix}$:

$$\begin{bmatrix} 1 & 3 & 0 & 2 \\ 0 & 0 & 1 & 4 \\ 1 & 3 & 1 & 6 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} = \begin{bmatrix} 1 \\ 6 \\ 7 \end{bmatrix} \quad \begin{array}{l} \text{có ma trận} \\ \text{mở rộng} \\ \text{là} \end{array} \quad \begin{bmatrix} 1 & 3 & 0 & 2 & 1 \\ 0 & 0 & 1 & 4 & 6 \\ 1 & 3 & 1 & 6 & 7 \end{bmatrix} = \begin{bmatrix} A & b \end{bmatrix}.$$

Khi chúng ta áp dụng các bước khử thông thường cho $A$, để đạt tới $R$, chúng ta cũng áp dụng chúng cho $b$.

Trong ví dụ này, chúng ta trừ hàng 1 khỏi hàng 3. Sau đó chúng ta trừ hàng 2 khỏi hàng 3. Điều này tạo ra một hàng số không trong $R$, và nó biến $b$ thành một vế phải mới $d = (1, 6, 0)$:

$$\begin{bmatrix} 1 & 3 & 0 & 2 \\ 0 & 0 & 1 & 4 \\ 0 & 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} = \begin{bmatrix} 1 \\ 6 \\ 0 \end{bmatrix} \quad \begin{array}{l} \text{có ma trận} \\ \text{mở rộng} \\ \text{là} \end{array} \quad \begin{bmatrix} 1 & 3 & 0 & 2 & 1 \\ 0 & 0 & 1 & 4 & 6 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix} = \begin{bmatrix} R & d \end{bmatrix}.$$

Số không cuối cùng đó là cốt yếu. Phương trình thứ ba đã trở thành $0 = 0$. Vì vậy các phương trình có thể giải được. Trong ma trận $A$ ban đầu, hàng thứ nhất cộng hàng thứ hai bằng hàng thứ ba. Nếu các phương trình là nhất quán (consistent), điều này cũng phải đúng ở vế phải của các phương trình! Tính chất vô cùng quan trọng của vế phải $b$ là $1 + 6 = 7$. Điều đó dẫn đến $0 = 0$.

Dưới đây là các ma trận mở rộng tương tự cho một $b = (b_1, b_2, b_3)$ tổng quát:

$$\begin{bmatrix} A & b \end{bmatrix} = \begin{bmatrix} 1 & 3 & 0 & 2 & b_1 \\ 0 & 0 & 1 & 4 & b_2 \\ 1 & 3 & 1 & 6 & b_3 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 3 & 0 & 2 & b_1 \\ 0 & 0 & 1 & 4 & b_2 \\ 0 & 0 & 0 & 0 & b_3 - b_1 - b_2 \end{bmatrix} = \begin{bmatrix} R & d \end{bmatrix}$$

Bây giờ chúng ta chỉ nhận được $0 = 0$ ở phương trình thứ ba nếu $b_3 - b_1 - b_2 = 0$. Tức là $b_1 + b_2 = b_3$.

# **Một Nghiệm Cụ Thể (One Particular Solution)** $Ax_p = b$

Để có một nghiệm dễ dàng $x_p$, *hãy chọn các biến tự do bằng không:* $x_2 = x_4 = 0$. Khi đó hai phương trình khác không cho ta hai biến phần tử xoay $x_1 = 1$ và $x_3 = 6$. Nghiệm cụ thể của chúng ta cho $Ax = b$ (và cả $Rx = d$) là $x_p = (1, 0, 6, 0)$. Nghiệm cụ thể này là nghiệm tôi thích nhất: *các biến tự do = không, các biến phần tử xoay lấy từ d.* Phương pháp này luôn luôn hoạt động.

**Để một nghiệm tồn tại, các hàng số không trong $R$ cũng phải bằng số không ở trong $d$. Bởi vì $I$ nằm trong các hàng phần tử xoay và các cột phần tử xoay của $R$, các biến phần tử xoay trong $x_p$ cụ thể đến từ $d$:**

$$Rx_p = \begin{bmatrix} 1 & 3 & 0 & 2 \\ 0 & 0 & 1 & 4 \\ 0 & 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \\ 6 \\ 0 \end{bmatrix} = \begin{bmatrix} 1 \\ 6 \\ 0 \end{bmatrix} = \begin{bmatrix} \text{Các biến phần tử xoay 1, 6} \\ \text{Các biến tự do 0, 0} \\ \text{Nghiệm } x_p = (1, 0, 6, 0) \end{bmatrix}.$$

Hãy chú ý cách chúng ta *chọn* các biến tự do (bằng không) và *giải* tìm các biến phần tử xoay. Sau khi rút gọn hàng về $R$, các bước đó diễn ra nhanh chóng. Khi các biến tự do bằng không, các biến phần tử xoay của $x_p$ đã được nhìn thấy trong vectơ vế phải $d$.

| $x_{\text{particular}}$ | *Nghiệm cụ thể giải*                 | $Ax_p = b$.   |
|-------------------------|-------------------------------------------------------|--------------|
| $x_{\text{nullspace}}$  | *$n - r$ nghiệm đặc biệt giải* | $Ax_n = 0$. |

Nghiệm cụ thể đó là $(1, 0, 6, 0)$. Hai nghiệm đặc biệt (không gian không) của $Rx = 0$ đến từ hai cột tự do của $R$, bằng cách đảo ngược dấu của 3, 2, và 4. *Xin hãy chú ý cách tôi viết nghiệm toàn diện $x_p + x_n$ cho $Ax = b$:*

**Nghiệm toàn diện**  
 một $x_p$
 nhiều $x_n$ 

$$x = x_p + x_n = \begin{bmatrix} 1 \\ 0 \\ 6 \\ 0 \end{bmatrix} + x_2 \begin{bmatrix} -3 \\ 1 \\ 0 \\ 0 \end{bmatrix} + x_4 \begin{bmatrix} -2 \\ 0 \\ -4 \\ 1 \end{bmatrix},$$

*Câu hỏi* Giả sử $A$ là một ma trận vuông khả nghịch, $m = n = r$. Thế thì $x_p$ và $x_n$ là gì? *Trả lời* Nghiệm cụ thể là nghiệm *duy nhất* $x_p = A^{-1}b$. Không có nghiệm đặc biệt hay biến tự do nào. $R = I$ không có hàng số không. Vectơ duy nhất trong không gian không là $x_n = 0$. Nghiệm toàn diện là $x = x_p + x_n = A^{-1}b + 0$.

Chúng ta đã không đề cập đến không gian không trong Chương 2, bởi vì $A$ khả nghịch và $N(A)$ chỉ chứa vectơ không. Việc rút gọn đi từ $\begin{bmatrix} A & b \end{bmatrix}$ đến $\begin{bmatrix} I & A^{-1}b \end{bmatrix}$. Ma trận $A$ được rút gọn hoàn toàn về $I$. Khi đó $Ax = b$ trở thành $x = A^{-1}b$ chính là $d$. Ở đây nó là một trường hợp đặc biệt, nhưng các ma trận vuông khả nghịch là những ma trận chúng ta thấy thường xuyên nhất trong thực tế. Vì vậy chúng có chương riêng ở đầu sách.

Đối với các ví dụ nhỏ, chúng ta có thể rút gọn $\begin{bmatrix} A & b \end{bmatrix}$ thành $\begin{bmatrix} R & d \end{bmatrix}$. Đối với một ma trận lớn, MATLAB làm điều đó tốt hơn. Một nghiệm cụ thể (không nhất thiết phải là của chúng ta) là $x = A \backslash b$ bằng dấu gạch chéo ngược (backslash). Dưới đây là một ví dụ với *hạng cột đầy đủ (full column rank).* Cả hai cột đều có phần tử xoay.

**Ví dụ 1** Tìm điều kiện đối với $(b_1, b_2, b_3)$ để $Ax = b$ giải được, nếu

| $A = \begin{bmatrix} 1 & 1 \\ 1 & 2 \\ -2 & -3 \end{bmatrix}$ | và | $b = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix}$ |
|---------------------------------------------------------------|-----|-------------------------------------------------------|
|---------------------------------------------------------------|-----|-------------------------------------------------------|

Điều kiện này đặt $b$ vào không gian cột của $A$. Tìm nghiệm toàn diện $x = x_p + x_n$.
*Giải* Sử dụng ma trận mở rộng, với cột phụ $b$ của nó. Trừ hàng 1 của $\begin{bmatrix} A & b \end{bmatrix}$ khỏi hàng 2. Sau đó cộng 2 lần hàng 1 vào hàng 3 để đạt tới $\begin{bmatrix} R & d \end{bmatrix}$:

| $\begin{bmatrix} 1 & 1 & b_1 \\ 1 & 2 & b_2 \\ -2 & -3 & b_3 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 1 & b_1 \\ 0 & 1 & b_2 - b_1 \\ 0 & -1 & b_3 + 2b_1 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 0 & 2b_1 - b_2 \\ 0 & 1 & b_2 - b_1 \\ 0 & 0 & b_3 + b_1 + b_2 \end{bmatrix}$ |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
(Ghi chú: Sửa lại lỗi tính toán trong sách bản gốc ở phép tính hàng: $-3 + 2(1) = -1$, $b_3 + 2b_1$; sau đó cộng hàng 2 vào hàng 3 thì được vế phải là $(b_3 + 2b_1) + (b_2 - b_1) = b_3 + b_1 + b_2$.)

Phương trình cuối cùng là $0 = 0$ với điều kiện là $b_3 + b_1 + b_2 = 0$. Đây là điều kiện để đặt $b$ vào không gian cột. Khi đó $Ax = b$ sẽ giải được. Các hàng của $A$ cộng lại thành hàng số không. Vì vậy để nhất quán (consistency) (đây là các phương trình!) các thành phần của $b$ cũng phải cộng lại bằng không.

Ví dụ này không có biến tự do vì $n - r = 2 - 2 = 0$. Do đó không có các nghiệm đặc biệt. Nghiệm không gian không là $x_n = 0$. Nghiệm cụ thể cho $Ax = b$ và $Rx = d$ nằm ở phần trên của cột $d$ cuối cùng:

| Nghiệm duy nhất của $Ax = b$ | $x = x_p + x_n = \begin{bmatrix} 2b_1 - b_2 \\ b_2 - b_1 \end{bmatrix} + \begin{bmatrix} 0 \\ 0 \end{bmatrix}$ |
|---------------------------|----------------------------------------------------------------------------------------------------------------|
|---------------------------|----------------------------------------------------------------------------------------------------------------|

Nếu $b_3 + b_1 + b_2$ khác không, thì không có nghiệm cho $Ax = b$ ($x_p$ và $x$ không tồn tại).

Ví dụ này là điển hình của một trường hợp cực kỳ quan trọng: $A$ có *hạng cột đầy đủ.* Mọi cột đều có một phần tử xoay. *Hạng là r = n.* Ma trận cao và mỏng ($m \geq n$). Việc rút gọn hàng đặt $I$ ở trên cùng, khi $A$ được rút gọn thành $R$ với hạng $n$:

| Hạng cột đầy đủ | $R = \begin{bmatrix} I \\ 0 \end{bmatrix} = \begin{bmatrix} n & \text{ma trận đơn vị} \\ m - n & \text{hàng số không} \end{bmatrix}$ | (1) |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------|-----|
|------------------|---------------------------------------------------------------------------------------------------------------------------------------|-----|

Không có các cột tự do hoặc các biến tự do. Không gian không là $\mathbf{Z} = \{\text{vectơ không}\}$.

Chúng ta sẽ tập hợp lại các cách khác nhau để nhận ra loại ma trận này.

Mọi ma trận $A$ có **hạng cột đầy đủ** ($r = n$) đều có tất cả các tính chất sau:

- **1.** Tất cả các cột của $A$ đều là các cột phần tử xoay.
- **2.** Không có biến tự do hoặc nghiệm đặc biệt nào.
- **3.** Không gian không $N(A)$ chỉ chứa vectơ không $x = 0$.
- **4.** Nếu $Ax = b$ có nghiệm (có thể không có) thì nó chỉ có *một nghiệm duy nhất.*

Theo ngôn ngữ cốt lõi của phần tiếp theo, **ma trận $A$ này có các cột độc lập.** $Ax = 0$ chỉ xảy ra khi $x = 0$. Trong Chương 4, chúng ta sẽ thêm một thực tế nữa vào danh sách: *Ma trận vuông $A^TA$ là khả nghịch khi hạng bằng n.*

Trong trường hợp này, không gian không của $A$ (và $R$) đã thu hẹp lại thành vectơ không. Nghiệm của $Ax = b$ là *duy nhất* (nếu nó tồn tại). Sẽ có $m - n$ hàng số không trong $R$. Vì vậy có $m - n$ điều kiện đối với $b$ để có $0 = 0$ ở những hàng đó, và $b$ nằm trong không gian cột. Với hạng cột đầy đủ, $Ax = b$ có *một* nghiệm hoặc *không có* nghiệm ($m > n$ là hệ xác định quá mức/overdetermined).

# **Nghiệm Toàn Diện (The Complete Solution)**

Trường hợp cực đoan còn lại là hạng hàng đầy đủ (full row rank). Bây giờ $Ax = b$ có *một hoặc vô số* nghiệm. Trong trường hợp này $A$ phải *ngắn và rộng ($m \leq n$). Một ma trận có hạng hàng đầy đủ nếu r = m. "Các hàng độc lập với nhau."* Mọi hàng đều có một phần tử xoay, và đây là một ví dụ.

**Ví dụ 2** Hệ $Ax = b$ này có $n = 3$ ẩn số nhưng chỉ có $m = 2$ phương trình:

| Hạng hàng đầy đủ | $x$ | $+$ | $y$  | $+$ | $z$ | $=$ | $3$ | $(\text{hạng } r = m = 2)$ |
|---------------|-----|-----|------|-----|-----|-----|-----|----------------------------|
|               | $x$ | $+$ | $2y$ | $-$ | $z$ | $=$ | $4$ |                            |

Đây là hai mặt phẳng trong không gian $xyz$. Hai mặt phẳng này không song song nên chúng cắt nhau tại một đường thẳng. Đường thẳng các nghiệm này chính xác là những gì phép khử sẽ tìm ra. *Nghiệm cụ thể sẽ là một điểm trên đường thẳng. Việc cộng thêm các vectơ không gian không $x_n$ sẽ di chuyển chúng ta dọc theo đường thẳng trong Hình 3.3.* Khi đó $x = x_p + x_n$ cho toàn bộ đường thẳng các nghiệm.

![](images/_page_162_Diagram_12.jpeg)

Hình 3.3: Nghiệm toàn diện = *một* nghiệm cụ thể + *tất cả* các nghiệm không gian không.

Chúng ta tìm $x_p$ và $x_n$ bằng phép khử trên $\begin{bmatrix} A & b \end{bmatrix}$. Trừ hàng 1 khỏi hàng 2 và sau đó trừ hàng 2 khỏi hàng 1:

$$\begin{bmatrix} 1 & 1 & 1 & 3 \\ 1 & 2 & -1 & 4 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 1 & 1 & 3 \\ 0 & 1 & -2 & 1 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 0 & 3 & 2 \\ 0 & 1 & -2 & 1 \end{bmatrix} = \begin{bmatrix} R & d \end{bmatrix}.$$
(Sửa lỗi OCR của bản gốc thành $1 \quad 2 \quad -1 \quad 4$)

*Nghiệm cụ thể có biến tự do $x_3 = 0$.* Nghiệm đặc biệt có $x_3 = 1$:

$x_{\text{cụ thể}}$ đến trực tiếp từ $d$ ở vế phải: $x_p = (2, 1, 0)$

$x_{\text{đặc biệt}}$ đến từ cột thứ ba (cột tự do) của $R$: $s = (-3, 2, 1)$

Thật khôn ngoan khi kiểm tra xem $x_p$ và $s$ có thỏa mãn các phương trình ban đầu $Ax_p = b$ và $As = 0$ hay không:

$2 + 1 = 3$ và $2 + 2(1) = 4$
$-3 + 2 + 1 = 0$ và $-3 + 2(2) - 1 = 0$

Nghiệm không gian không $x_n$ là một bội số bất kỳ của $s$. Nó di chuyển dọc theo đường thẳng các nghiệm, bắt đầu từ $x_{\text{cụ thể}}$. *Xin chú ý lại một lần nữa cách viết câu trả lời:*

| Nghiệm toàn diện | $x = x_p + x_n = \begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix} + x_3 \begin{bmatrix} -3 \\ 2 \\ 1 \end{bmatrix}$ |
|-------------------|--------------------------------------------------------------------------------------------------------------|
|-------------------|--------------------------------------------------------------------------------------------------------------|

Đường thẳng các nghiệm này được vẽ trong Hình 3.3. Một điểm bất kỳ trên đường thẳng *có thể* được chọn làm nghiệm cụ thể. Chúng ta đã chọn điểm có $x_3 = 0$.

Nghiệm cụ thể *không* được nhân với một hằng số tùy ý! Nghiệm đặc biệt thì cần hằng số đó, và bạn hiểu tại sao - để tạo ra tất cả các $x_n$ trong không gian không.

Bây giờ chúng ta tóm tắt trường hợp ngắn và rộng này của *hạng hàng đầy đủ.* Nếu $m < n$ phương trình $Ax = b$ là **xác định thiếu (underdetermined)** (có nhiều nghiệm).

Mọi ma trận $A$ có *hạng hàng đầy đủ ($r = m$)* đều có tất cả các tính chất sau:

- **1.** Tất cả các hàng đều có các phần tử xoay, và $R$ **không có hàng số không.**
- **2.** $Ax = b$ có một **nghiệm cho mọi vế phải** $b$.
- **3.** Không gian cột là toàn bộ không gian $\mathbf{R}^m$.
- **4.** Có $n - r = n - m$ nghiệm đặc biệt trong không gian không của $A$.

Trong trường hợp này với $m$ phần tử xoay, các hàng là *"độc lập tuyến tính".* Vì vậy các cột của $A^T$ là độc lập tuyến tính. Không gian không của $A^T$ là vectơ không.

Chúng ta đã sẵn sàng cho định nghĩa về tính độc lập tuyến tính, ngay khi chúng ta tóm tắt bốn khả năng - phụ thuộc vào hạng. Chú ý cách $r, m, n$ là những con số quan trọng.

*Bốn khả năng đối với các phương trình tuyến tính phụ thuộc vào hạng r*

- $r = m$ và $r = n$: Vuông và khả nghịch. $Ax = b$ có 1 nghiệm.
- $r = m$ và $r < n$: Ngắn và rộng. $Ax = b$ có $\infty$ nghiệm.
- $r < m$ và $r = n$: Cao và mỏng. $Ax = b$ có $0$ hoặc $1$ nghiệm.
- $r < m$ và $r < n$: Hạng không đầy đủ. $Ax = b$ có $0$ hoặc $\infty$ nghiệm.

Ma trận $R$ được rút gọn sẽ rơi vào cùng loại với ma trận $A$. Trong trường hợp các cột phần tử xoay tình cờ nằm ở trước, chúng ta có thể hiển thị bốn khả năng này đối với $R$. Để $Rx = d$ (và $Ax = b$ ban đầu) giải được, $d$ phải kết thúc bằng $m - r$ số không. $F$ là phần tự do của $R$.

| Bốn loại cho $R$ | $\begin{bmatrix} I \end{bmatrix}$       | $\begin{bmatrix} I & F \end{bmatrix}$   | $\begin{bmatrix} I \\ 0 \end{bmatrix}$ | $\begin{bmatrix} I & F \\ 0 & 0 \end{bmatrix}$ |
|--------------------|-------------|-------------|----------------------------------------|------------------------------------------------|
| Các hạng tương ứng | $r = m = n$ | $r = m < n$ | $r = n < m$                            | $r < m, r < n$                                 |

Trường hợp 1 và 2 có hạng hàng đầy đủ $r = m$. Trường hợp 1 và 3 có hạng cột đầy đủ $r = n$. Trường hợp 4 là tổng quát nhất về mặt lý thuyết và nó ít phổ biến nhất trong thực tế.

#### **• ÔN TẬP CÁC Ý TƯỞNG CHÍNH (REVIEW OF THE KEY IDEAS) •**

- **1.** Hạng $r$ là số lượng các phần tử xoay. Ma trận $R$ có $m - r$ hàng số không.
- **2.** $Ax = b$ giải được khi và chỉ khi $m - r$ phương trình cuối cùng rút gọn thành $0 = 0$.
- **3.** Một nghiệm cụ thể $x_p$ có tất cả các biến tự do bằng không.
- **4.** Các biến phần tử xoay được xác định sau khi các biến tự do được chọn.
- **5.** Hạng cột đầy đủ $r = n$ nghĩa là không có biến tự do: có một nghiệm hoặc không có.
- **6.** Hạng hàng đầy đủ $r = m$ nghĩa là có một nghiệm nếu $m = n$ hoặc có vô số nghiệm nếu $m < n$.

#### **• CÁC VÍ DỤ ĐÃ GIẢI (WORKED EXAMPLES) •**

**3.3 A** Câu hỏi này kết nối phép khử **(các cột phần tử xoay và phép thế ngược)** với **không gian cột-không gian không-hạng-khả năng giải được** (bức tranh ở cấp độ cao hơn). $A$ có hạng 2:

|          | $x_1 + 2x_2 + 3x_3 + 5x_4 = b_1$   |
|----------|------------------------------------|
| $Ax = b$ | $2x_1 + 4x_2 + 8x_3 + 12x_4 = b_2$ |
|          | $3x_1 + 6x_2 + 7x_3 + 13x_4 = b_3$ |
(Sửa lại hệ số của phương trình thứ hai cho khớp với ma trận giải ở dưới)

- **1.** Rút gọn $\begin{bmatrix} A & b \end{bmatrix}$ thành $\begin{bmatrix} U & c \end{bmatrix}$, để $Ax = b$ trở thành một hệ tam giác $Ux = c$.
- **2.** Tìm điều kiện đối với $b_1, b_2, b_3$ để $Ax = b$ có một nghiệm.
- **3.** Mô tả không gian cột của $A$. Là mặt phẳng nào trong $\mathbf{R}^3$?
- **4.** Mô tả không gian không của $A$. Là những nghiệm đặc biệt nào trong $\mathbf{R}^4$?
- **5.** Rút gọn $\begin{bmatrix} U & c \end{bmatrix}$ thành $\begin{bmatrix} R & d \end{bmatrix}$: Các nghiệm đặc biệt từ $R$, nghiệm cụ thể từ $d$.
- **6.** Tìm một nghiệm cụ thể cho $Ax = (0, 6, -6)$ và sau đó là nghiệm toàn diện.

#### **Giải**

- **1.** Các hệ số nhân trong phép khử là $2$ và $3$ và $-1$. Chúng đưa $\begin{bmatrix} A & b \end{bmatrix}$ thành $\begin{bmatrix} U & c \end{bmatrix}$.

| $\begin{bmatrix} 1 & 2 & 3 & 5 & b_1 \\ 2 & 4 & 8 & 12 & b_2 \\ 3 & 6 & 7 & 13 & b_3 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 2 & 3 & 5 & b_1 \\ 0 & 0 & 2 & 2 & b_2 - 2b_1 \\ 0 & 0 & -2 & -2 & b_3 - 3b_1 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 2 & 3 & 5 & b_1 \\ 0 & 0 & 2 & 2 & b_2 - 2b_1 \\ 0 & 0 & 0 & 0 & b_3 + b_2 - 5b_1 \end{bmatrix}$ |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

- **2.** Phương trình cuối cùng cho thấy điều kiện để có thể giải được là $b_3 + b_2 - 5b_1 = 0$. Khi đó $0 = 0$.
- **3.** Mô tả thứ nhất: Không gian cột là mặt phẳng chứa tất cả các tổ hợp của các cột phần tử xoay $(1, 2, 3)$ và $(3, 8, 7)$. Các phần tử xoay nằm ở cột 1 và 3. Mô tả thứ hai: Không gian cột chứa tất cả các vectơ có $b_3 + b_2 - 5b_1 = 0$. Điều đó làm cho $Ax = b$ giải được, vì vậy $b$ nằm trong không gian cột. *Tất cả các cột của $A$ đều vượt qua bài kiểm tra này $b_3 + b_2 - 5b_1 = 0$. Đây là phương trình cho mặt phẳng trong mô tả thứ nhất!*
- **4.** Các nghiệm đặc biệt có các biến tự do $x_2 = 1, x_4 = 0$ và sau đó $x_2 = 0, x_4 = 1$:

| **Các nghiệm đặc biệt cho $Ax = 0$** | $s_1 = \begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix}$ | $s_2 = \begin{bmatrix} -2 \\ 0 \\ -1 \\ 1 \end{bmatrix}$ |
|-----------------------------------------------------------------|--|--|
| **Thế ngược trong $Ux = 0$**                 |  |  |
| **hoặc đảo ngược dấu của 2, 2, 1 trong $R$**             |  |  |

Không gian không $N(A)$ trong $\mathbf{R}^4$ chứa tất cả các $x_n = c_1s_1 + c_2s_2$.

- **5.** Trong ma trận rút gọn $R$, cột thứ ba thay đổi từ $(3, 2, 0)$ trong $U$ thành $(0, 1, 0)$. Vế phải $c = (0, 6, 0)$ trở thành $d = (-9, 3, 0)$ hiển thị $-9$ và $3$ trong $x_p$:

| $\begin{bmatrix} U & c \end{bmatrix} = \begin{bmatrix} 1 & 2 & 3 & 5 & 0 \\ 0 & 0 & 2 & 2 & 6 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix} \longrightarrow \begin{bmatrix} R & d \end{bmatrix} =$ | $\begin{bmatrix} 1 & 2 & 0 & 2 & -9 \\ 0 & 0 & 1 & 1 & 3 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$ |
|-------------|-----------------------------------------------------------------------------------------------------------------------|
|-------------|-----------------------------------------------------------------------------------------------------------------------|

- **6.** Một nghiệm cụ thể $x_p$ có các biến tự do = không. Thế ngược vào $Ux = c$:

| Nghiệm cụ thể cho $Ax_p = b$       | $-9$ |
|-----------------------------------------|------|
| Mang $-9$ và 3 từ vectơ $d$    | $0$  |
| Các biến tự do $x_2$ và $x_4$ bằng không | $3$  |
|                                         | $0$  |

Nghiệm toàn diện cho $Ax = (0, 6, -6)$ là $x = x_p + x_n = x_p + c_1s_1 + c_2s_2$.

**3.3 B** Giả sử bạn có thông tin này về các nghiệm của $Ax = b$ đối với một $b$ cụ thể. Điều đó nói cho bạn biết gì về $m$ và $n$ và $r$ (và chính $A$)? Và có thể là về $b$.

1. Có chính xác một nghiệm.
2. Tất cả các nghiệm của $Ax = b$ đều có dạng $x = \begin{bmatrix} 2 \\ 1 \end{bmatrix} + c \begin{bmatrix} 1 \\ 1 \end{bmatrix}$.
3. Không có nghiệm nào.
4. Tất cả các nghiệm của $Ax = b$ đều có dạng $x = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} + c \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}$.
5. Có vô số nghiệm.

**Giải** Trong trường hợp 1, với chính xác một nghiệm, $A$ phải có hạng cột đầy đủ $r = n$. Không gian không của $A$ chỉ chứa vectơ không. Bắt buộc $m \geq n$.

Trong trường hợp 2, $A$ phải có $n = 2$ cột (và $m$ là tùy ý). Với $\begin{bmatrix} 1 \\ 1 \end{bmatrix}$ nằm trong không gian không của $A$, cột 2 là *phủ định (negative)* của cột 1. Ngoài ra $A \neq 0$: hạng là 1. Với $x = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$ là một nghiệm, $b = 2(\text{cột 1}) + (\text{cột 2})$. Sự lựa chọn của tôi cho $x_p$ sẽ là $(1, 0)$.

Trong trường hợp 3, chúng ta chỉ biết rằng $b$ không nằm trong không gian cột của $A$. Hạng của $A$ phải nhỏ hơn $m$. Tôi đoán chúng ta biết $b \neq 0$, nếu không thì $x = 0$ sẽ là một nghiệm.

Trong trường hợp 4, $A$ phải có $n = 3$ cột. Với $(1, 0, 1)$ nằm trong không gian không của $A$, cột 3 là phủ định của cột 1. Cột 2 *không được* là một bội số của cột 1, nếu không không gian không sẽ chứa một nghiệm đặc biệt khác. Vì vậy hạng của $A$ là $3 - 1 = 2$. Bắt buộc $A$ có $m \geq 2$ hàng. Vế phải $b$ là cột 1 + cột 2.

Trong trường hợp 5 với vô số nghiệm, không gian không phải chứa các vectơ khác không. Hạng $r$ phải nhỏ hơn $n$ (không phải hạng cột đầy đủ), và $b$ phải nằm trong không gian cột của $A$. Chúng ta không biết liệu mọi $b$ có nằm trong không gian cột hay không, nên chúng ta không biết liệu $r = m$ hay không.

**3.3 C** Tìm nghiệm toàn diện $x = x_p + x_n$ bằng phép khử tiến trên $\begin{bmatrix} A & b \end{bmatrix}$:

$$\begin{bmatrix} 1 & 2 & 1 & 0 \\ 2 & 4 & 4 & 8 \\ 4 & 8 & 6 & 8 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} = \begin{bmatrix} 4 \\ 2 \\ 10 \end{bmatrix}.$$

Tìm các số $y_1, y_2, y_3$ sao cho $y_1(\text{hàng 1}) + y_2(\text{hàng 2}) + y_3(\text{hàng 3}) = \text{hàng số không}$. Kiểm tra xem $b = (4, 2, 10)$ có thỏa mãn điều kiện $y_1b_1 + y_2b_2 + y_3b_3 = 0$ hay không. Tại sao đây lại là điều kiện để các phương trình có thể giải được và $b$ nằm trong không gian cột?

**Giải** Phép khử tiến trên $\begin{bmatrix} A & b \end{bmatrix}$ tạo ra một hàng số không trong $\begin{bmatrix} U & c \end{bmatrix}$. Phương trình thứ ba trở thành $0 = 0$ và các phương trình là nhất quán (và có thể giải được):

$$\begin{bmatrix} 1 & 2 & 1 & 0 & 4 \\ 2 & 4 & 4 & 8 & 2 \\ 4 & 8 & 6 & 8 & 10 \end{bmatrix} \longrightarrow \begin{bmatrix} 1 & 2 & 1 & 0 & 4 \\ 0 & 0 & 2 & 8 & -6 \\ 0 & 0 & 2 & 8 & -6 \end{bmatrix} \longrightarrow \begin{bmatrix} 1 & 2 & 1 & 0 & 4 \\ 0 & 0 & 2 & 8 & -6 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}.$$

Cột 1 và cột 3 chứa các phần tử xoay. Các biến $x_2$ và $x_4$ là tự do. Nếu chúng ta thiết lập chúng bằng không, chúng ta có thể giải (thế ngược) để tìm nghiệm cụ thể hoặc chúng ta tiếp tục để tìm $R$.

$Rx = d$ cho thấy rằng nghiệm cụ thể với các biến tự do = 0 là $x_p = (7, 0, -3, 0)$.

$$\begin{bmatrix} 1 & 2 & 1 & 0 & 4 \\ 0 & 0 & 2 & 8 & -6 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix} \longrightarrow \begin{bmatrix} 1 & 2 & 1 & 0 & 4 \\ 0 & 0 & 1 & 4 & -3 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix} \longrightarrow \begin{bmatrix} 1 & 2 & 0 & -4 & 7 \\ 0 & 0 & 1 & 4 & -3 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$$

Đối với phần không gian không $x_n$ với $b = 0$, hãy thiết lập các biến tự do $x_2, x_4$ lần lượt là 1, 0 và 0, 1:

| Các nghiệm đặc biệt | $s_1 = (-2, 1, 0, 0)$ | **và** | $s_2 = (4, 0, -4, 1)$ |
|-------------------|---------------------|----------------|--------------------|
|                   |                     |                |                    |

Khi đó nghiệm toàn diện của $Ax = b$ (và $Rx = d$) là $x_{\text{toàn diện}} = x_p + c_1s_1 + c_2s_2$. Các hàng của $A$ tạo ra hàng số không từ $2(\text{hàng 1}) + 1(\text{hàng 2}) - 1(\text{hàng 3}) = (0, 0, 0, 0)$.

Vậy $y = (2, 1, -1)$. Tổ hợp tương tự cho $b = (4, 2, 10)$ cho kết quả $2(4) + 1(2) - 1(10) = 0$.

**Nếu** một tổ hợp của các hàng (ở vế trái) cho ra hàng số không, thì cùng một tổ hợp đó phải cho ra số không ở vế phải. Tất nhiên rồi! *Nếu không thì không có nghiệm.*

Sau này chúng ta sẽ nói lại điều này bằng những từ ngữ khác: **Nếu** mọi cột của $A$ vuông góc với $y = (2, 1, -1)$, thì bất kỳ tổ hợp $b$ nào của những cột đó cũng phải vuông góc với $y$. Nếu không thì $b$ không nằm trong không gian cột và $Ax = b$ không thể giải được.

Và một lần nữa: **Nếu** $y$ nằm trong không gian không của $A^T$ thì $y$ phải vuông góc với mọi $b$ trong không gian cột của $A$. Chỉ là nhìn về phía trước thôi...

### **Bài Tập 3.3 (Problem Set 3.3)**

**1** (Khuyên làm) Thực hiện sáu bước của Ví Dụ Đã Giải **3.3 A** để mô tả không gian cột và không gian không của $A$ và nghiệm toàn diện của $Ax = b$:

| $A = \begin{bmatrix} 2 & 4 & 6 & 4 \\ 2 & 5 & 7 & 6 \\ 2 & 3 & 5 & 2 \end{bmatrix}$ | $b = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix} = \begin{bmatrix} 4 \\ 3 \\ 5 \end{bmatrix}$ |
|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|

**2** Thực hiện sáu bước tương tự cho ma trận $A$ này với hạng một. Bạn sẽ tìm thấy *hai* điều kiện đối với $b_1, b_2, b_3$ để $Ax = b$ giải được. Cùng với nhau, hai điều kiện này đặt $b$ vào không gian \_\_ (hai mặt phẳng tạo ra một đường thẳng):

| $A = \begin{bmatrix} 1 \\ 3 \\ 2 \end{bmatrix} \begin{bmatrix} 2 & 1 & 3 \end{bmatrix} = \begin{bmatrix} 2 & 1 & 3 \\ 6 & 3 & 9 \\ 4 & 2 & 6 \end{bmatrix}$ | $b = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix} = \begin{bmatrix} 10 \\ 30 \\ 20 \end{bmatrix}$ |
|---------------------------------------------------------------------|-------------------------------------------------------|
|---------------------------------------------------------------------|-------------------------------------------------------|

**Các câu hỏi 3-15 là về nghiệm của $Ax = b$. Thực hiện theo các bước trong sách giáo trình để tìm $x_p$ và $x_n$. Bắt đầu từ ma trận mở rộng với cột cuối cùng là $b$.**

**3** Viết nghiệm toàn diện dưới dạng $x_p$ cộng với một bội số bất kỳ của $s$ trong không gian không:

$$x + 3y + 3z = 1$$

$$2x + 6y + 9z = 5$$

$$-x - 3y + 3z = 5.$$

**4** Tìm nghiệm toàn diện (còn được gọi là *nghiệm tổng quát (general solution)*) cho

$$\begin{bmatrix} 1 & 3 & 1 & 2 \\ 2 & 6 & 4 & 8 \\ 0 & 0 & 2 & 4 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \\ t \end{bmatrix} = \begin{bmatrix} 1 \\ 3 \\ 1 \end{bmatrix}.$$

**5** Dưới điều kiện nào đối với $b_1, b_2, b_3$ thì hệ phương trình này giải được? Đưa $b$ vào làm cột thứ tư trong phép khử. Tìm tất cả các nghiệm khi điều kiện đó thỏa mãn:

- $x + 2y - 2z = b_1$
- $2x + 5y - 4z = b_2$
- $4x + 9y - 8z = b_3$

**6** Điều kiện nào đối với $b_1, b_2, b_3, b_4$ làm cho mỗi hệ có thể giải được? Tìm $x$ trong trường hợp đó:

$$\begin{bmatrix} 1 & 2 \\ 2 & 4 \\ 2 & 5 \\ 3 & 9 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \\ b_4 \end{bmatrix} \quad \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 7 \\ 2 & 5 & 6 \\ 3 & 9 & 12 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \\ b_4 \end{bmatrix}.$$

**7** Chỉ ra bằng phép khử rằng $(b_1, b_2, b_3)$ nằm trong không gian cột nếu $b_3 - 2b_2 + 4b_1 = 0$.

$$A = \begin{bmatrix} 1 & 3 & 1 \\ 3 & 8 & 2 \\ 2 & 4 & 0 \end{bmatrix}.$$

Tổ hợp nào của các hàng của $A$ cho ra hàng số không?

**8** Những vectơ $(b_1, b_2, b_3)$ nào nằm trong không gian cột của $A$? Những tổ hợp nào của các hàng của $A$ cho ra số không? (a) $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \\ 3 & 6 \end{bmatrix}$ (b) $A = \begin{bmatrix} 1 & 1 & 2 \\ 2 & 2 & 4 \\ 3 & 3 & 6 \end{bmatrix}$.

**9** (a) Ví Dụ Đã Giải **3.3 A** đã đạt tới $\begin{bmatrix} U & c \end{bmatrix}$ từ $\begin{bmatrix} A & b \end{bmatrix}$. Đặt các hệ số nhân vào $L$ và kiểm tra xem $LU$ có bằng $A$ và $Lc$ có bằng $b$ không.
(b) Kết hợp các cột phần tử xoay của $A$ với các số $-9$ và $3$ trong nghiệm cụ thể $x_p$. Tổ hợp tuyến tính đó là gì và tại sao?

**10** Cấu trúc một hệ 2 x 3 $Ax = b$ với nghiệm cụ thể $x_p = (2, 4, 0)$ và nghiệm thuần nhất (homogeneous solution) $x_n = \text{bội số bất kỳ của } (1, 1, 1)$.

**11** Tại sao một hệ 1 x 3 không thể có $x_p = (2, 4, 0)$ và $x_n = \text{bội số bất kỳ của } (1, 1, 1)$?

**12** (a) Nếu $Ax = b$ có hai nghiệm $x_1$ và $x_2$, hãy tìm hai nghiệm cho $Ax = 0$.
(b) Sau đó tìm một nghiệm khác cho $Ax = 0$ và một nghiệm khác cho $Ax = b$.

**13** Giải thích tại sao những điều này đều sai:
(a) Nghiệm toàn diện là một tổ hợp tuyến tính bất kỳ của $x_p$ và $x_n$.
(b) Một hệ $Ax = b$ có nhiều nhất một nghiệm cụ thể.
(c) Nghiệm $x_p$ với tất cả các biến tự do bằng không là nghiệm ngắn nhất (độ dài $\|x\|$ nhỏ nhất). Tìm một phản ví dụ 2 x 2.
(d) Nếu $A$ khả nghịch thì không có nghiệm $x_n$ nào trong không gian không.

**14** Giả sử cột 5 của $U$ không có phần tử xoay. Khi đó $x_5$ là một biến \_\_\_\_\_. Vectơ không (là) (không là) nghiệm duy nhất của $Ax = 0$. Nếu $Ax = b$ có một nghiệm, thì nó có \_\_\_\_\_ nghiệm.

**15** Giả sử hàng 3 của $U$ không có phần tử xoay. Khi đó hàng đó là \_\_\_\_\_. Phương trình $Ux = c$ chỉ có thể giải được với điều kiện \_\_\_\_\_. Phương trình $Ax = b$ (là) (không là) (có thể không là) giải được.

**Các câu hỏi 16–20 là về các ma trận "hạng đầy đủ" $r = m$ hoặc $r = n$.**

**16** Hạng lớn nhất có thể có của một ma trận 3 x 5 là \_\_\_\_\_. Khi đó có một phần tử xoay trong mỗi \_\_\_\_\_ của $U$ và $R$. Nghiệm của $Ax = b$ (luôn tồn tại) (là duy nhất). Không gian cột của $A$ là \_\_\_\_\_. Một ví dụ là $A = \underline{\hspace{1cm}}$.

**17** Hạng lớn nhất có thể có của một ma trận 6 x 4 là \_\_\_\_\_. Khi đó có một phần tử xoay trong mỗi \_\_\_\_\_ của $U$ và $R$. Nghiệm của $Ax = b$ (luôn tồn tại) (là duy nhất). Không gian không của $A$ là \_\_\_\_\_. Một ví dụ là $A = \underline{\hspace{1cm}}$.

**18** Tìm bằng phép khử hạng của $A$ và cả hạng của $A^T$:

$$A = \begin{bmatrix} 1 & 4 & 0 \\ 2 & 11 & 5 \\ -1 & 2 & 10 \end{bmatrix} \quad \text{và} \quad A = \begin{bmatrix} 1 & 0 & 1 \\ 1 & 1 & 2 \\ 1 & 1 & q \end{bmatrix} \quad (\text{hạng phụ thuộc vào } q).$$

**19** Tìm hạng của $A$ và cả của $A^T A$ và cả của $AA^T$:

$$A = \begin{bmatrix} 1 & 1 & 5 \\ 1 & 0 & 1 \end{bmatrix} \quad \text{và} \quad A = \begin{bmatrix} 2 & 0 \\ 1 & 1 \\ 1 & 2 \end{bmatrix}.$$

**20** Rút gọn $A$ về dạng bậc thang $U$ của nó. Sau đó tìm một ma trận tam giác $L$ sao cho $A = LU$.

$$A = \begin{bmatrix} 3 & 4 & 1 & 0 \\ 6 & 5 & 2 & 1 \end{bmatrix} \quad \text{và} \quad A = \begin{bmatrix} 1 & 0 & 1 & 0 \\ 2 & 2 & 0 & 3 \\ 0 & 6 & 5 & 4 \end{bmatrix}.$$

**21** Tìm nghiệm toàn diện dưới dạng $x_p + x_n$ cho các hệ hạng đầy đủ này:

(a) $x + y + z = 4$
(b) $x + y + z = 4$
$\quad x - y + z = 4.$

**22** Nếu $Ax = b$ có vô số nghiệm, tại sao $Ax = B$ (vế phải mới) lại không thể chỉ có một nghiệm duy nhất? $Ax = B$ có thể không có nghiệm nào không?

**23** Chọn số $q$ để (nếu có thể) các hạng là (a) 1, (b) 2, (c) 3:

| $A = \begin{bmatrix} 6 & 4 & 2 \\ -3 & -2 & -1 \\ 9 & 6 & q \end{bmatrix}$ | và | $B = \begin{bmatrix} 3 & 1 & 3 \\ q & 2 & q \end{bmatrix}$ |
|----------------------------------------------------------------------------|-----|------------------------------------------------------------|
|----------------------------------------------------------------------------|-----|------------------------------------------------------------|

**24** Đưa ra các ví dụ về các ma trận $A$ mà số lượng các nghiệm của $Ax = b$ là

(a) 0 hoặc 1, tùy thuộc vào $b$ (b) $\infty$, bất kể $b$ (c) 0 hoặc $\infty$, tùy thuộc vào $b$ (d) 1, bất kể $b$.

**25** Viết ra tất cả các mối quan hệ đã biết giữa $r$ và $m$ và $n$ nếu $Ax = b$ có

(a) không có nghiệm cho một số $b$
(b) vô số nghiệm cho mọi $b$
(c) chính xác một nghiệm cho một số $b$, không có nghiệm cho các $b$ khác
(d) chính xác một nghiệm cho mọi $b$.

#### **Các câu hỏi 26-33 là về phép khử Gauss-Jordan (lên trên cũng như xuống dưới) và ma trận bậc thang rút gọn $R$.**

**26** Tiếp tục phép khử từ $U$ đến $R$. Chia các hàng cho các phần tử xoay để các phần tử xoay mới đều là 1. Sau đó tạo ra các số không *bên trên* các phần tử xoay đó để đạt tới $R$:

| $U = \begin{bmatrix} 2 & 4 & 4 \\ 0 & 3 & 6 \\ 0 & 0 & 0 \end{bmatrix}$ | và | $U = \begin{bmatrix} 2 & 4 & 4 \\ 0 & 3 & 6 \\ 0 & 0 & 5 \end{bmatrix}$ |
|-------------------------------------------------------------------------|-----|-------------------------------------------------------------------------|
|-------------------------------------------------------------------------|-----|-------------------------------------------------------------------------|

**27** Nếu $A$ là một ma trận tam giác, thì khi nào $R = \text{rref}(A)$ bằng $I$?

**28** Áp dụng phép khử Gauss-Jordan cho $Ux = 0$ và $Ux = c$. Đạt tới $Rx = 0$ và $Rx = d$:

$$\begin{bmatrix} U & 0 \end{bmatrix} = \begin{bmatrix} 1 & 2 & 3 & 0 \\ 0 & 0 & 4 & 0 \end{bmatrix} \quad \text{và} \quad \begin{bmatrix} U & c \end{bmatrix} = \begin{bmatrix} 1 & 2 & 3 & 5 \\ 0 & 0 & 4 & 8 \end{bmatrix}.$$

Giải $Rx = 0$ để tìm $x_n$ (biến tự do của nó là $x_2 = 1$). Giải $Rx = d$ để tìm $x_p$ (biến tự do của nó là $x_2 = 0$).

**29** Áp dụng phép khử Gauss-Jordan để rút gọn về $Rx = 0$ và $Rx = d$:

| $\begin{bmatrix} U & 0 \end{bmatrix} = \begin{bmatrix} 3 & 0 & 6 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$ và $\begin{bmatrix} U & c \end{bmatrix} = \begin{bmatrix} 3 & 0 & 6 & 0 \\ 0 & 0 & 2 & 4 \\ 0 & 0 & 0 & 5 \end{bmatrix}$ |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Giải $Ux = 0$ hoặc $Rx = 0$ để tìm $x_n$ (biến tự do = 1). Các nghiệm của $Rx = d$ là gì?

**30** Rút gọn về $Ux = c$ (phép khử Gauss) và sau đó là $Rx = d$ (Gauss-Jordan):

$$Ax = \begin{bmatrix} 1 & 0 & 2 & 3 \\ 1 & 3 & 2 & 0 \\ 2 & 0 & 4 & 9 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} = \begin{bmatrix} 2 \\ 5 \\ 10 \end{bmatrix} = b.$$

Tìm một nghiệm cụ thể $x_p$ và tất cả các nghiệm thuần nhất $x_n$.

**31** Tìm các ma trận $A$ và $B$ với tính chất đã cho hoặc giải thích tại sao bạn không thể:

(a) Nghiệm duy nhất của
$$Ax = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$$
là $x = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$.

(b) Nghiệm duy nhất của
$$Bx = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$
là $x = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$.

**32** Tìm phân tích $LU$ của $A$ và nghiệm toàn diện của $Ax = b$:

$$A = \begin{bmatrix} 1 & 3 & 3 \\ 1 & 4 & 6 \\ 2 & 4 & 6 \\ 1 & 1 & 5 \end{bmatrix} \quad \text{và} \quad b = \begin{bmatrix} 1 \\ 3 \\ 6 \\ 5 \end{bmatrix} \quad \text{và sau đó} \quad b = \begin{bmatrix} 0 \\ 1 \\ 0 \\ 0 \end{bmatrix}.$$

**33** Nghiệm toàn diện của
$$Ax = \begin{bmatrix} 1 \\ 3 \end{bmatrix}$$
là $x = \begin{bmatrix} 1 \\ 0 \end{bmatrix} + c \begin{bmatrix} 0 \\ 1 \end{bmatrix}$. Tìm $A$.

# Thử thách (Challenge Problems)

**34** (Khuyên làm!) Giả sử bạn biết rằng ma trận 3 x 4 $A$ có các vectơ $s = (2, 3, 1, 0)$ là nghiệm đặc biệt duy nhất của $Ax = 0$.
(a) *Hạng* của $A$ và nghiệm toàn diện của $Ax = 0$ là gì?
(b) Dạng bậc thang rút gọn theo hàng chính xác $R$ của $A$ là gì?
(c) Làm sao bạn biết rằng $Ax = b$ có thể giải được cho mọi $b$?

**35** Giả sử $K$ là ma trận sai phân bậc hai 9 x 9 (các số 2 trên đường chéo, các số -1 trên đường chéo bên trên và cả bên dưới). Giải phương trình $Kx = b = (10, \dots, 10)$. Nếu bạn vẽ đồ thị $x_1, \dots, x_9$ phía trên các điểm $1, \dots, 9$ trên trục x, tôi nghĩ chín điểm sẽ nằm trên một parabol.

**36** Giả sử $Ax = b$ và $Cx = b$ có cùng các nghiệm (toàn diện) cho mọi $b$. Có đúng là $A$ bằng $C$ không?

**37** Mô tả không gian cột của một ma trận bậc thang rút gọn theo hàng $R$.

# **3.4 Sự Độc Lập, Cơ Sở và Số Chiều (Independence, Basis and Dimension)**

**1 Các cột độc lập (Independent columns)** của A: Nghiệm duy nhất của $Ax = \mathbf{0}$ là $x = \mathbf{0}$. Không gian không là $Z$.
**2 Các vectơ độc lập:** Tổ hợp bằng không duy nhất $c_1v_1 + \dots + c_kv_k = 0$ có tất cả các $c = 0$.
**3** Một ma trận với $m < n$ có **các cột phụ thuộc (dependent columns):** Có ít nhất $n - m$ biến tự do / nghiệm đặc biệt.
**4** Các vectơ $v_1, \dots, v_k$ **sinh ra không gian (span the space)** $S$ nếu $S = \text{tất cả các tổ hợp của các } v$.
**5** Các vectơ $v_1, \dots, v_k$ là một **cơ sở (basis)** cho $S$ nếu chúng độc lập và chúng sinh ra $S$.
**6** **Số chiều (dimension) của một không gian** $S$ là số lượng các vectơ trong mọi cơ sở cho $S$.
**7** Nếu $A$ là 4 x 4 và khả nghịch, các cột của nó là một cơ sở cho $\mathbf{R}^4$. Số chiều của $\mathbf{R}^4$ là 4.

Phần quan trọng này nói về kích thước thực sự của một không gian con. Có $n$ cột trong một ma trận $m \times n$. Nhưng "số chiều" thực sự của không gian cột không nhất thiết phải là $n$. Số chiều được đo bằng cách đếm *các cột độc lập - và* chúng ta phải nói rõ điều đó có nghĩa là gì. Chúng ta sẽ thấy rằng *số chiều thực sự của không gian cột chính là hạng r.*

Ý tưởng về sự độc lập áp dụng cho bất kỳ các vectơ $v_1, \dots, v_n$ nào trong bất kỳ không gian vectơ nào. Hầu hết phần này tập trung vào các không gian con mà chúng ta biết và sử dụng --- đặc biệt là không gian cột và không gian không của $A$. Trong phần cuối, chúng ta cũng nghiên cứu "các vectơ" không phải là các vectơ cột. Chúng có thể là các ma trận và các hàm số; chúng có thể độc lập tuyến tính (hoặc phụ thuộc). Trước tiên là các ví dụ chính sử dụng các vectơ cột.

Mục tiêu là để hiểu về một *cơ sở:* **các vectơ độc lập "sinh ra không gian".**

**Mọi vectơ trong không gian là một tổ hợp duy nhất của các vectơ cơ sở.**

Chúng ta đang ở trọng tâm của môn học, và chúng ta không thể tiếp tục mà không có một cơ sở. Bốn ý tưởng cốt yếu trong phần này (với những gợi ý đầu tiên về ý nghĩa của chúng) là:

- **1. Các vectơ độc lập (Independent vectors)**
- **2. Sinh ra một không gian (Spanning a space)**
- **3. Cơ sở cho một không gian (Basis for a space)**
- **4. Số chiều của một không gian (Dimension of a space)** *(không có vectơ thừa) (đủ vectơ để tạo ra phần còn lại) (không quá nhiều cũng không quá ít) (số lượng các vectơ trong một cơ sở)*

### **Sự Độc Lập Tuyến Tính (Linear Independence)**

Định nghĩa đầu tiên của chúng ta về sự độc lập không quá thông thường, nhưng bạn đã sẵn sàng cho nó.

**ĐỊNH NGHĨA** Các cột của $A$ là *độc lập tuyến tính* khi nghiệm duy nhất của $Ax = 0$ là $x = 0$. *Không có tổ hợp $Ax$ nào khác của các cột cho ra vectơ không.*

Các cột độc lập khi không gian không $N(A)$ chỉ chứa vectơ không. Hãy để tôi minh họa sự độc lập (và phụ thuộc) tuyến tính với ba vectơ trong $\mathbf{R}^3$:

- **1.** Nếu ba vectơ *không* nằm trong cùng một mặt phẳng, chúng độc lập. Không có tổ hợp nào của $v_1, v_2, v_3$ trong Hình 3.4 cho ra số không ngoại trừ $0v_1 + 0v_2 + 0v_3$.
- **2.** Nếu ba vectơ $w_1, w_2, w_3$ *nằm trong cùng một mặt phẳng,* chúng phụ thuộc.

![](images/_page_174_Diagram_4.jpeg)

Hình 3.4: Các vectơ độc lập $v_1, v_2, v_3$. Chỉ có $0v_1 + 0v_2 + 0v_3$ mới cho ra vectơ $\mathbf{0}$. Các vectơ phụ thuộc $w_1, w_2, w_3$. Tổ hợp $w_1 - w_2 + w_3$ là $(0, 0, 0)$.

Ý tưởng này về sự độc lập áp dụng cho 7 vectơ trong không gian 12 chiều. Nếu chúng là các cột của $A$, và độc lập, không gian không chỉ chứa $x = 0$. Không có vectơ nào trong số đó là một tổ hợp của sáu vectơ còn lại.

Bây giờ chúng ta chọn những từ ngữ khác để diễn đạt cùng một ý tưởng. Định nghĩa sau đây về sự độc lập sẽ áp dụng cho bất kỳ dãy vectơ nào trong bất kỳ không gian vectơ nào. Khi các vectơ là các cột của $A$, hai định nghĩa nói chính xác cùng một điều.

**ĐỊNH NGHĨA** Dãy các vectơ $v_1, \dots, v_n$ là *độc lập tuyến tính* nếu tổ hợp duy nhất cho ra vectơ không là $0v_1 + 0v_2 + \dots + 0v_n$.

#### **Sự độc lập tuyến tính**

$x_1v_1 + x_2v_2 + \dots + x_nv_n = 0$ chỉ xảy ra khi tất cả các $x$ đều bằng không. (1)

Nếu một tổ hợp cho ra $\mathbf{0}$, khi các $x$ không phải tất cả đều bằng không, các vectơ đó là *phụ thuộc.*

*Cách nói đúng:* "Dãy các vectơ là độc lập tuyến tính." *Cách nói tắt được chấp nhận:* "Các vectơ độc lập." *Cách nói không thể chấp nhận:* "Ma trận độc lập."

Một dãy các vectơ hoặc là phụ thuộc hoặc là độc lập. Chúng có thể được kết hợp lại để cho ra vectơ không (với các $x$ khác không) hoặc là không thể. Vì vậy câu hỏi then chốt là: Những tổ hợp nào của các vectơ cho ra số không? Chúng ta bắt đầu với một số ví dụ nhỏ trong $\mathbf{R}^2$:

- (a) Các vectơ $(1, 0)$ và $(0, 1)$ độc lập.
- (b) Các vectơ $(1, 0)$ và $(1, 0.00001)$ độc lập.
- (c) Các vectơ $(1, 1)$ và $(-1, -1)$ là *phụ thuộc.*
- (d) Các vectơ $(1, 1)$ và $(0, 0)$ là *phụ thuộc* do có vectơ không.
- (e) Trong $\mathbf{R}^2$, ba vectơ bất kỳ $(a, b)$ và $(c, d)$ và $(e, f)$ đều *phụ thuộc.*

Về mặt hình học, $(1, 1)$ và $(-1, -1)$ nằm trên một đường thẳng đi qua gốc tọa độ. Chúng phụ thuộc. Để sử dụng định nghĩa, hãy tìm các số $x_1$ và $x_2$ sao cho $x_1(1, 1) + x_2(-1, -1) = (0, 0)$. Việc này giống như giải phương trình $Ax = \mathbf{0}$:

| $\begin{bmatrix} 1 & -1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$ | với $x_1 = 1$ và $x_2 = 1$. |
|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------|

Các cột phụ thuộc chính xác khi *có một vectơ khác không nằm trong không gian không.*

Nếu một trong các $v$ là vectơ không, sự độc lập không có cơ hội xảy ra. Tại sao không?

Ba vectơ trong $\mathbf{R}^2$ không thể độc lập! Một cách để thấy điều này: ma trận $A$ với ba cột đó phải có một biến tự do và do đó có một nghiệm đặc biệt cho $Ax = 0$. Một cách khác: Nếu hai vectơ đầu độc lập, một tổ hợp nào đó sẽ tạo ra vectơ thứ ba. Xem phần được tô sáng thứ hai bên dưới.

Bây giờ chuyển sang ba vectơ trong $\mathbf{R}^3$. Nếu một trong số chúng là một bội số của một vectơ khác, những vectơ này phụ thuộc. Nhưng bài kiểm tra đầy đủ liên quan đến cả ba vectơ cùng một lúc. Chúng ta đặt chúng vào một ma trận và cố gắng giải $Ax = 0$.

**Ví dụ 1** Các cột của ma trận $A$ này phụ thuộc. $Ax = \mathbf{0}$ có một nghiệm khác không:

| $Ax = \begin{bmatrix} 1 & 0 & 3 \\ 2 & 1 & 5 \\ 1 & 0 & 3 \end{bmatrix} \begin{bmatrix} -3 \\ 1 \\ 1 \end{bmatrix}$ | là | $-3 \begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix} + 1 \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} + 1 \begin{bmatrix} 3 \\ 5 \\ 3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$ |
|--------------------------------------------------------------------------|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|--------------------------------------------------------------------------|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Hạng chỉ là $r = 2$. *Các cột độc lập tạo ra hạng cột đầy đủ $r = n = 3$.*

Trong ma trận đó, các hàng cũng phụ thuộc. Hàng 1 trừ đi hàng 3 là hàng số không. Đối với một *ma trận vuông,* chúng ta sẽ chứng minh rằng các cột phụ thuộc ngụ ý các hàng phụ thuộc.

**Câu hỏi** Làm thế nào để tìm ra nghiệm đó cho $Ax = \mathbf{0}$? Cách thức có hệ thống là phép khử.

| $A = \begin{bmatrix} 1 & 0 & 3 \\ 2 & 1 & 5 \\ 1 & 0 & 3 \end{bmatrix}$ | rút gọn thành $R = \begin{bmatrix} 1 & 0 & 3 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{bmatrix}$ |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------|

Nghiệm $x = (-3, 1, 1)$ chính xác là nghiệm đặc biệt. Nó cho thấy cột tự do (cột 3) là một tổ hợp của các cột phần tử xoay như thế nào. Điều đó giết chết sự độc lập!

**Hạng cột đầy đủ** Các cột của $A$ độc lập chính xác khi hạng $r = n$. Có $n$ phần tử xoay và không có biến tự do. Chỉ có $x = \mathbf{0}$ nằm trong không gian không.

Một trường hợp có tầm quan trọng đặc biệt bởi vì nó rõ ràng ngay từ đầu. Giả sử bảy cột có năm thành phần mỗi cột ($m = 5$ nhỏ hơn $n = 7$). Khi đó các cột *phải phụ thuộc.* Bảy vectơ bất kỳ từ $\mathbf{R}^5$ đều phụ thuộc. Hạng của $A$ không thể lớn hơn 5. Không thể có nhiều hơn năm phần tử xoay trong năm hàng. $Ax = \mathbf{0}$ có ít nhất $7 - 5 = 2$ biến tự do, vì vậy nó có các nghiệm khác không - điều đó có nghĩa là các cột phụ thuộc.

Bất kỳ tập hợp nào gồm $n$ vectơ trong $\mathbf{R}^m$ đều phải phụ thuộc tuyến tính nếu $n > m$. Loại ma trận này có nhiều cột hơn hàng - nó ngắn và rộng. Các cột chắc chắn phụ thuộc nếu $n > m$, bởi vì $Ax = 0$ có một nghiệm khác không.

Các cột có thể phụ thuộc hoặc có thể độc lập nếu $n \leq m$. Phép khử sẽ tiết lộ $r$ cột phần tử xoay. *Chính r cột phần tử xoay đó là độc lập.*

*Lưu ý* Một cách khác để mô tả sự phụ thuộc tuyến tính là như sau: *"Một vectơ là một tổ hợp của các vectơ khác."* Nghe có vẻ rõ ràng. Tại sao chúng ta không nói điều này ngay từ đầu? Định nghĩa của chúng ta dài hơn: *"Một tổ hợp nào đó cho ra vectơ không, khác với tổ hợp tầm thường với mọi $x = 0$."* Chúng ta phải loại trừ cách dễ dàng để có được vectơ không. Tổ hợp tầm thường của các số không đó khiến mọi tác giả đau đầu. Nếu một vectơ là một tổ hợp của các vectơ khác, vectơ đó có hệ số $x = 1$.

Vấn đề là, định nghĩa của chúng ta không chọn ra một vectơ cụ thể nào là có tội. Tất cả các cột của $A$ đều được đối xử như nhau. Chúng ta xem xét $Ax = \mathbf{0}$, và nó có một nghiệm khác không hoặc không có. Cuối cùng, điều đó tốt hơn là hỏi xem cột cuối cùng (hoặc cột đầu tiên, hoặc một cột ở giữa) có phải là một tổ hợp của các cột khác hay không.

# **Các Vectơ Sinh Ra Một Không Gian Con (Vectors that Span a Subspace)**

Không gian con đầu tiên trong cuốn sách này là không gian cột. Bắt đầu với các cột $v_1, \dots, v_n$, không gian con được lấp đầy bằng cách bao gồm tất cả các tổ hợp $x_1v_1 + \dots + x_nv_n$. *Không gian cột bao gồm tất cả các tổ hợp $Ax$ của các cột.* Bây giờ chúng ta giới thiệu từ duy nhất "sinh ra (span)" để mô tả điều này: Không gian cột được *sinh ra* bởi các cột.

#### **ĐỊNH NGHĨA** Một tập hợp các vectơ *sinh ra* một không gian nếu các tổ hợp tuyến tính của chúng lấp đầy không gian đó.

#### *Các cột của một ma trận sinh ra không gian cột của nó. Chúng có thể phụ thuộc.*

**Ví dụ 2** $v_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ và $v_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$ sinh ra toàn bộ không gian hai chiều $\mathbf{R}^2$.

**Ví dụ 3** $v_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, v_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}, v_3 = \begin{bmatrix} 4 \\ 7 \end{bmatrix}$ cũng sinh ra toàn bộ không gian $\mathbf{R}^2$.

**Ví dụ 4** $w_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ và $w_2 = \begin{bmatrix} -1 \\ -1 \end{bmatrix}$ chỉ sinh ra một đường thẳng trong $\mathbf{R}^2$. Bản thân $w_1$ cũng vậy.

Hãy nghĩ về hai vectơ xuất phát từ $(0, 0, 0)$ trong không gian 3 chiều. Nói chung chúng sinh ra một mặt phẳng. Tâm trí bạn lấp đầy mặt phẳng đó bằng cách lấy các tổ hợp tuyến tính. Về mặt toán học, bạn biết các khả năng khác: hai vectơ có thể sinh ra một đường thẳng, ba vectơ có thể sinh ra toàn bộ $\mathbf{R}^3$, hoặc chỉ một mặt phẳng. Thậm chí có thể ba vectơ chỉ sinh ra một đường thẳng, hoặc mười vectơ chỉ sinh ra một mặt phẳng. Chúng chắc chắn không độc lập!

Các cột sinh ra không gian cột. Đây là một không gian con mới - không gian *được sinh ra bởi các hàng. Các tổ hợp của các hàng tạo ra "không gian hàng" (row space).*

**ĐỊNH NGHĨA** *Không gian hàng* của một ma trận là không gian con của $\mathbf{R}^n$ được sinh ra bởi các hàng.

*Không gian hàng của $A$ là $C(A^T)$. Nó là không gian cột của $A^T$.*

Các hàng của một ma trận $m \times n$ có $n$ thành phần. Chúng là các vectơ trong $\mathbf{R}^n$ - hoặc chúng sẽ như vậy nếu chúng được viết dưới dạng vectơ cột. Có một cách nhanh chóng để sửa điều đó: *Chuyển vị ma trận.* Thay vì các hàng của $A$, hãy nhìn vào các cột của $A^T$. Cùng những con số, nhưng bây giờ nằm trong không gian cột $C(A^T)$. Không gian hàng này của $A$ là một không gian con của $\mathbf{R}^n$.

**Ví dụ 5** Mô tả không gian cột và không gian hàng của $A$.

| $A = \begin{bmatrix} 1 & 4 \\ 2 & 7 \\ 3 & 5 \end{bmatrix}$ và $A^T = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 7 & 5 \end{bmatrix}$. Ở đây $m = 3$ và $n = 2$. |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|

Không gian cột của $A$ là mặt phẳng trong $\mathbf{R}^3$ được sinh ra bởi hai cột của $A$. *Không gian hàng của $A$ được sinh ra bởi ba hàng của $A$* (chính là các cột của $A^T$). Không gian hàng này là toàn bộ $\mathbf{R}^2$. Hãy nhớ: Các hàng nằm trong $\mathbf{R}^n$ sinh ra không gian hàng. Các cột nằm trong $\mathbf{R}^m$ sinh ra không gian cột. Cùng những con số, các vectơ khác nhau, các không gian khác nhau.

# **Một Cơ Sở Cho Một Không Gian Vectơ (A Basis for a Vector Space)**

Hai vectơ không thể sinh ra toàn bộ $\mathbf{R}^3$, ngay cả khi chúng độc lập. Bốn vectơ không thể độc lập, ngay cả khi chúng sinh ra $\mathbf{R}^3$. Chúng ta muốn *đủ các vectơ độc lập để sinh ra không gian* (và không thừa). Một *"cơ sở"* là vừa đúng.

**ĐỊNH NGHĨA** Một *cơ sở* cho một không gian vectơ là một dãy các vectơ có hai tính chất:

*Các vectơ cơ sở độc lập tuyến tính và chúng sinh ra không gian.*

Sự kết hợp các tính chất này là cơ bản đối với đại số tuyến tính. Mọi vectơ $v$ trong không gian là một tổ hợp của các vectơ cơ sở, bởi vì chúng sinh ra không gian. Hơn thế nữa, tổ hợp tạo ra $v$ là *duy nhất,* bởi vì các vectơ cơ sở $v_1, \dots, v_n$ là độc lập:

**Có một và chỉ một cách duy nhất để viết $v$ dưới dạng một tổ hợp của các vectơ cơ sở.**

**Lý do:** Giả sử $v = a_1v_1 + \dots + a_nv_n$ và cũng có $v = b_1v_1 + \dots + b_nv_n$. Bằng phép trừ, $(a_1 - b_1)v_1 + \dots + (a_n - b_n)v_n$ là vectơ không. Từ sự độc lập của các $v$, mỗi $a_i - b_i = 0$. Do đó $a_i = b_i$, và không có hai cách để tạo ra $v$.

**Ví dụ 6** Các cột của $I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ tạo ra "cơ sở chuẩn" (standard basis) cho $\mathbf{R}^2$.

Các vectơ cơ sở 
$$i = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$$
và $j = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$ là độc lập. Chúng sinh ra $\mathbf{R}^2$.

Mọi người đều nghĩ đến cơ sở này đầu tiên. Vectơ $i$ đi ngang và $j$ đi thẳng lên. Các cột của ma trận đơn vị 3 x 3 là cơ sở chuẩn $i, j, k$. Các cột của ma trận đơn vị $n \times n$ cho ra **"cơ sở chuẩn"** cho $\mathbf{R}^n$.

Bây giờ chúng ta tìm thấy nhiều cơ sở khác (vô số). Cơ sở không phải là duy nhất!

**Ví dụ 7** (Quan trọng) Các cột của *mọi ma trận $n \times n$ khả nghịch* đều tạo thành một cơ sở cho $\mathbf{R}^n$:

| **Ma trận khả nghịch**       | $A = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix}$ | **Ma trận suy biến**           | $A = \begin{bmatrix} 1 & 0 & 1 \\ 1 & 1 & 2 \\ 1 & 1 & 2 \end{bmatrix}$ |
|--------------------------------|-------------------------------------------------------------------------|----------------------------------|-------------------------------------------------------------------------|
| Các cột độc lập            |                                                                         | Các cột phụ thuộc                | $A = \begin{bmatrix} 1 & 0 & 1 \\ 1 & 1 & 2 \\ 1 & 1 & 2 \end{bmatrix}$ |
| Không gian cột là $\mathbf{R}^3$ |                                                                         | Không gian cột $\neq \mathbf{R}^3$ |                                                                         |

Nghiệm duy nhất của $Ax = 0$ là $x = A^{-1}0 = 0$. Các cột độc lập. Chúng sinh ra toàn bộ không gian $\mathbf{R}^n$ - bởi vì mọi vectơ $b$ đều là một tổ hợp của các cột. $Ax = b$ luôn có thể được giải bằng $x = A^{-1}b$. Bạn có thấy cách mọi thứ liên kết với nhau đối với các ma trận khả nghịch không? Đây là nó trong một câu:

Các vectơ $v_1, \dots, v_n$ là một *cơ sở cho* $\mathbf{R}^n$ chính xác khi chúng là *các cột của một ma trận $n \times n$ khả nghịch.* Do đó $\mathbf{R}^n$ có vô số cơ sở khác nhau.

Khi các cột phụ thuộc, chúng ta chỉ giữ lại *các cột phần tử xoay* - hai cột đầu tiên của $A$ (suy biến) ở trên, với hai phần tử xoay của nó. Chúng độc lập và chúng sinh ra không gian cột.

*Các cột phần tử xoay của $A$ là một cơ sở cho không gian cột của nó.* Các hàng phần tử xoay của $A$ là một cơ sở cho không gian hàng của nó. Các hàng phần tử xoay của dạng bậc thang $R$ của nó cũng vậy.

**Ví dụ 8** Ma trận này không khả nghịch. Các cột của nó không phải là cơ sở cho bất kỳ cái gì!

| **Một cột phần tử xoay**                   | $A = \begin{bmatrix} 2 & 4 \\ 3 & 6 \end{bmatrix}$ | rút gọn thành $R = \begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix}$. |
|-------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------|
| **Một hàng phần tử xoay ($r = 1$)** |                                                    | (Sửa lại lỗi $R$ trong bản gốc từ 0 3 thành 0 0)                                                                |

Cột 1 của $A$ là cột phần tử xoay. Một mình cột đó là một cơ sở cho không gian cột của nó. Cột thứ hai của $A$ sẽ là một cơ sở khác. Bất kỳ bội số khác không nào của cột đó cũng vậy. Không thiếu các cơ sở. Một sự lựa chọn xác định là các cột phần tử xoay.

Lưu ý rằng cột phần tử xoay $(1, 0)$ của $R$ này kết thúc bằng số không. Cột đó là một cơ sở cho không gian cột của $R$, nhưng nó không thuộc không gian cột của $A$. Không gian cột của $A$ và $R$ là khác nhau. Các cơ sở của chúng là khác nhau. (Số chiều của chúng giống nhau.)

Không gian hàng của $A$ *giống* với không gian hàng của $R$. Nó chứa $(2, 4)$ và $(1, 2)$ và tất cả các bội số khác của những vectơ đó. Như thường lệ, có vô số cơ sở để lựa chọn. Một sự lựa chọn tự nhiên là chọn các hàng khác không của $R$ (các hàng có phần tử xoay). Vì vậy ma trận $A$ với hạng một này chỉ có một vectơ trong cơ sở:

| Cơ sở cho không gian cột: | $\begin{bmatrix} 2 \\ 3 \end{bmatrix}$ | Cơ sở cho không gian hàng: | $\begin{bmatrix} 1 \\ 2 \end{bmatrix}$ |
|-----------------------------|----------------------------------------|--------------------------|----------------------------------------|
|-----------------------------|----------------------------------------|--------------------------|----------------------------------------|

Chương tiếp theo sẽ quay lại những cơ sở này cho không gian cột và không gian hàng. Đầu tiên chúng ta hài lòng với những ví dụ mà tình huống rõ ràng (và ý tưởng về cơ sở vẫn còn mới mẻ). Ví dụ tiếp theo lớn hơn nhưng vẫn rõ ràng.

**Ví dụ 9** Tìm các cơ sở cho không gian cột và không gian hàng của ma trận hạng hai này:

$$R = \begin{bmatrix} 1 & 2 & 0 & 3 \\ 0 & 0 & 1 & 4 \\ 0 & 0 & 0 & 0 \end{bmatrix}.$$

Cột 1 và 3 là các cột phần tử xoay. Chúng là một cơ sở cho không gian cột (của $R$!). Các vectơ trong không gian cột đó đều có dạng $b = (x, y, 0)$. Không gian cột của $R$ là *"mặt phẳng xy"* bên trong toàn bộ không gian $xyz$ 3 chiều. Mặt phẳng đó không phải là $\mathbf{R}^3$, nó là một không gian con của $\mathbf{R}^3$. Các cột 2 và 3 cũng là một cơ sở cho cùng không gian cột đó. Những cặp cột nào của $R$ *không phải* là cơ sở cho không gian cột của nó?

Không gian hàng của $R$ là một không gian con của $\mathbf{R}^4$. Cơ sở đơn giản nhất cho không gian hàng đó là hai hàng khác không của $R$. Hàng thứ ba (vectơ không) cũng nằm trong không gian hàng. Nhưng nó không nằm trong một *cơ sở* cho không gian hàng. Các vectơ cơ sở phải độc lập.

#### **Câu hỏi** Cho năm vectơ trong $\mathbf{R}^7$, *làm thế nào bạn tìm được một cơ sở cho không gian mà chúng sinh ra?*

*Trả lời 1* Biến chúng thành các hàng của $A$, và khử để tìm các hàng khác không của $R$. *Trả lời 2* Đặt năm vectơ vào các cột của $A$. Khử để tìm các cột phần tử xoay (của $A$, không phải $R$). Những cột phần tử xoay đó là một cơ sở cho không gian cột.

Một cơ sở khác có thể có nhiều vectơ hơn, hoặc ít hơn không? Đây là một câu hỏi cốt yếu với một câu trả lời tốt: *Không. Tất cả các cơ sở của một không gian vectơ đều chứa cùng một số lượng vectơ.*

*Số lượng vectơ, trong bất kỳ và mọi cơ sở, là "số chiều" của không gian.*

### **Số Chiều Của Một Không Gian Vectơ (Dimension of a Vector Space)**

Chúng ta phải chứng minh những gì vừa được phát biểu. Có nhiều lựa chọn cho các vectơ cơ sở, nhưng *số lượng* các vectơ cơ sở không thay đổi.

Nếu $v_1, \dots, v_m$ và $w_1, \dots, w_n$ đều là các cơ sở cho cùng một không gian vectơ, thì $m = n$.

*Chứng minh* Giả sử rằng có nhiều $w$ hơn $v$. Từ $n > m$, chúng ta muốn đạt tới một sự mâu thuẫn. Các $v$ là một cơ sở, vì vậy $w_1$ phải là một tổ hợp của các $v$. Nếu $w_1$ bằng $a_{11}v_1 + \dots + a_{m1}v_m$, đây là cột đầu tiên của một phép nhân ma trận $VA$:

| Mỗi $w$ là một tổ hợp của các $v$ | $W = \begin{bmatrix} w_1 & w_2 & \dots & w_n \end{bmatrix} = \begin{bmatrix} v_1 & \dots & v_m \end{bmatrix}$ | $\begin{bmatrix} a_{11} & \dots & a_{1n} \\ \vdots & & \vdots \\ a_{m1} & \dots & a_{mn} \end{bmatrix} = VA$ |
|-----------------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
|-----------------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|

Chúng ta không biết từng $a_{ij}$, nhưng chúng ta biết hình dạng của $A$ (nó là $m \times n$). Vectơ thứ hai $w_2$ cũng là một tổ hợp của các $v$. Các hệ số trong tổ hợp đó lấp đầy cột thứ hai của $A$. Điểm mấu chốt là $A$ có một hàng cho mỗi $v$ và một cột cho mỗi $w$. $A$ là một ma trận ngắn và rộng, vì chúng ta đã giả sử $n > m$. Vậy $Ax = 0$ *có một nghiệm khác không.*

$Ax = 0$ cho $VAx = 0$ tức là $Wx = 0$. *Một tổ hợp của các $w$ cho ra số không!* Khi đó các $w$ không thể là một cơ sở - giả thiết $n > m$ của chúng ta là **không thể** đối với hai cơ sở.

Nếu $m > n$, chúng ta hoán đổi các $v$ và $w$ và lặp lại các bước tương tự. Cách duy nhất để tránh một sự mâu thuẫn là phải có $m = n$. Điều này hoàn thành chứng minh rằng $m = n$.

Số lượng các vectơ cơ sở phụ thuộc vào không gian - không phụ thuộc vào một cơ sở cụ thể. Con số là như nhau cho mọi cơ sở, và nó đếm số "bậc tự do" (degrees of freedom) trong không gian. Số chiều của không gian $\mathbf{R}^n$ là $n$. Bây giờ chúng ta cũng giới thiệu từ quan trọng *số chiều* cho các không gian vectơ khác.

**ĐỊNH NGHĨA** *Số chiều của một không gian* là *số lượng các vectơ* trong mọi cơ sở.

Điều này khớp với trực giác của chúng ta. Đường thẳng đi qua $v = (1, 5, 2)$ có số chiều là một. Nó là một không gian con với một vectơ $v$ duy nhất này trong cơ sở của nó. Vuông góc với đường thẳng đó là mặt phẳng $x + 5y + 2z = 0$. Mặt phẳng này có số chiều là 2. Để chứng minh điều đó, chúng ta tìm một cơ sở $(-5, 1, 0)$ và $(-2, 0, 1)$. Số chiều là 2 vì cơ sở chứa hai vectơ.

Mặt phẳng là không gian không của ma trận $A = \begin{bmatrix} 1 & 5 & 2 \end{bmatrix}$, ma trận này có hai biến tự do. Các vectơ cơ sở $(-5, 1, 0)$ và $(-2, 0, 1)$ của chúng ta là các "nghiệm đặc biệt" cho $Ax = 0$. Phần tiếp theo chỉ ra rằng $n - r$ nghiệm đặc biệt luôn luôn cho *một cơ sở cho không gian không. $C(A)$* có số chiều $r$ và không gian không $N(A)$ có số chiều $n - r$.

*Lưu ý về ngôn ngữ của đại số tuyến tính* Chúng ta không bao giờ nói "hạng của một không gian" hay "số chiều của một cơ sở" hay "cơ sở của một ma trận". Những thuật ngữ đó không có ý nghĩa. Đó là *số chiều của không gian cột* thì bằng *hạng của ma trận.*

## **Các Cơ Sở Cho Các Không Gian Ma Trận và Không Gian Hàm Số (Bases for Matrix Spaces and Function Spaces)**

Các từ "sự độc lập" và "cơ sở" và "số chiều" hoàn toàn không bị giới hạn ở các vectơ cột. Chúng ta có thể hỏi liệu ba ma trận $A_1, A_2, A_3$ có độc lập hay không. Khi chúng nằm trong không gian của tất cả các ma trận 3 x 4, một tổ hợp nào đó có thể cho ra ma trận không. Chúng ta cũng có thể hỏi về số chiều của toàn bộ không gian ma trận 3 x 4. (Đó là 12).

Trong phương trình vi phân, $d^2y/dx^2 = y$ có một không gian các nghiệm. Một cơ sở là $y = e^x$ và $y = e^{-x}$. Đếm các hàm số cơ sở cho ra số chiều là 2 cho không gian của tất cả các nghiệm. (Số chiều là 2 vì đạo hàm bậc hai).

Không gian ma trận và không gian hàm số có thể trông hơi lạ sau $\mathbf{R}^n$. Nhưng theo một cách nào đó, bạn chưa hiểu đúng các ý tưởng về cơ sở và số chiều cho đến khi bạn có thể áp dụng chúng cho những "vectơ" không phải là vectơ cột.

Không gian ma trận (Matrix spaces) Không gian vectơ $\mathbf{M}$ chứa tất cả các ma trận 2 x 2. Số chiều của nó là 4.

| Một cơ sở là | $A_1, A_2, A_3, A_4 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}$ |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|              | (Sửa lại $A_3, A_4$ trong bản gốc cho đúng với cơ sở chuẩn)                                                                                                                                                                                                                                                             |

Những ma trận đó là độc lập tuyến tính. Chúng ta không nhìn vào các cột của chúng, mà là toàn bộ ma trận. Các tổ hợp của bốn ma trận đó có thể tạo ra bất kỳ ma trận nào trong $\mathbf{M}$, vì vậy chúng sinh ra không gian:

| Mọi $A$ là sự kết hợp | $c_1A_1 + c_2A_2 + c_3A_3 + c_4A_4 = \begin{bmatrix} c_1 & c_2 \\ c_3 & c_4 \end{bmatrix} = A$ |
|--------------------|------------------------------------------------------------------------------------------------|
| của các ma trận cơ sở |                                                                                                |

$A$ là số không chỉ khi các $c$ đều bằng không - điều này chứng minh sự độc lập của $A_1, A_2, A_3, A_4$.

Ba ma trận $A_1, A_2, A_4$ là một cơ sở cho một không gian con - các ma trận tam giác trên. Số chiều của nó là 3. $A_1$ và $A_4$ là một cơ sở cho các ma trận đường chéo. Cơ sở cho các ma trận đối xứng là gì? Giữ lại $A_1$ và $A_4$, và đưa vào $A_2 + A_3$.

Để đẩy vấn đề này xa hơn, hãy nghĩ về không gian của tất cả các ma trận $n \times n$. Một cơ sở khả dĩ sử dụng các ma trận chỉ có một phần tử khác không duy nhất (phần tử đó là 1). Có $n^2$ vị trí cho số 1 đó, vì vậy có $n^2$ ma trận cơ sở:

Số chiều của toàn bộ không gian ma trận $n \times n$ là $n^2$.

Số chiều của không gian con các ma trận *tam giác trên* là $\frac{1}{2}n^2 + \frac{1}{2}n$.

Số chiều của không gian con các ma trận *đường chéo* là $n$.

Số chiều của không gian con các ma trận *đối xứng* là $\frac{1}{2}n^2 + \frac{1}{2}n$ (tại sao?).

Không gian hàm số (Function spaces) Các phương trình $d^2y/dx^2 = 0$ và $d^2y/dx^2 = -y$ và $d^2y/dx^2 = y$ liên quan đến đạo hàm bậc hai. Trong giải tích, chúng ta giải để tìm các hàm số $y(x)$:

| $y'' = 0$  | được giải bởi bất kỳ hàm bậc nhất nào $y = cx + d$          |
|------------|--------------------------------------------------------|
| $y'' = -y$ | được giải bởi bất kỳ tổ hợp nào $y = c \sin x + d \cos x$ |
| $y'' = y$  | được giải bởi bất kỳ tổ hợp nào $y = ce^x + de^{-x}$.    |

Không gian nghiệm đó cho $y'' = -y$ có hai hàm số cơ sở: $\sin x$ và $\cos x$. Không gian cho $y'' = 0$ có $x$ và $1$. Nó là "không gian không" của đạo hàm bậc hai! Số chiều là 2 trong mỗi trường hợp (đây là các phương trình bậc hai).

Các nghiệm của $y'' = 2$ không tạo thành một không gian con - vế phải $b = 2$ không bằng không. Một nghiệm cụ thể là $y(x) = x^2$. Nghiệm toàn diện là $y(x) = x^2 + cx + d$. Tất cả các hàm số đó thỏa mãn $y'' = 2$. Lưu ý nghiệm cụ thể cộng với hàm số bất kỳ $cx + d$ nằm trong không gian không. Một phương trình vi phân tuyến tính giống như một phương trình ma trận tuyến tính $Ax = b$. Nhưng chúng ta giải nó bằng giải tích thay vì đại số tuyến tính.

Chúng ta kết thúc ở đây với không gian $\mathbf{Z}$ chỉ chứa vectơ không. Số chiều của không gian này là *không (zero). Tập hợp rỗng (empty set)* (không chứa vectơ nào) *là một cơ sở cho* $\mathbf{Z}$. Chúng ta không bao giờ có thể cho phép vectơ không nằm trong một cơ sở, bởi vì khi đó sự độc lập tuyến tính sẽ bị mất.

#### **• ÔN TẬP CÁC Ý TƯỞNG CHÍNH (REVIEW OF THE KEY IDEAS) •**

- **1.** Các cột của $A$ *độc lập* nếu $x = \mathbf{0}$ là nghiệm duy nhất của $Ax = \mathbf{0}$.
- **2.** Các vectơ $v_1, \dots, v_r$ *sinh ra* một không gian nếu các tổ hợp của chúng lấp đầy không gian đó.
- **3.** *Một cơ sở bao gồm các vectơ độc lập tuyến tính sinh ra không gian.* Mọi vectơ trong không gian là một tổ hợp *duy nhất* của các vectơ cơ sở.
- **4.** Tất cả các cơ sở cho một không gian đều có cùng một số lượng vectơ. Số lượng vectơ này trong một cơ sở là *số chiều* của không gian.
- **5.** Các cột phần tử xoay là một cơ sở cho không gian cột. Số chiều là $r$.

#### **• CÁC VÍ DỤ ĐÃ GIẢI (WORKED EXAMPLES) •**

**3.4 A** Bắt đầu với các vectơ $v_1 = (1, 2, 0)$ và $v_2 = (2, 3, 0)$. **(a)** Chúng có độc lập tuyến tính không? **(b)** Chúng có phải là một cơ sở cho bất kỳ không gian nào không? **(c)** Chúng sinh ra không gian $\mathbf{V}$ nào? **(d)** Số chiều của $\mathbf{V}$ là bao nhiêu? **(e)** Những ma trận $A$ nào có $\mathbf{V}$ là không gian cột của chúng? **(f)** Những ma trận nào có $\mathbf{V}$ là không gian không của chúng? **(g)** Mô tả tất cả các vectơ $v_3$ hoàn thành một cơ sở $v_1, v_2, v_3$ cho $\mathbf{R}^3$.

#### **Giải**

- **(a)** $v_1$ và $v_2$ độc lập - tổ hợp duy nhất để cho ra $\mathbf{0}$ là $0v_1 + 0v_2$.
- **(b)** Có, chúng là một cơ sở cho không gian mà chúng sinh ra.
- **(c)** Không gian $\mathbf{V}$ đó chứa tất cả các vectơ $(x, y, 0)$. Đó là mặt phẳng $xy$ trong $\mathbf{R}^3$.
- **(d)** Số chiều của $\mathbf{V}$ là 2 vì cơ sở chứa hai vectơ.
- **(e)** $\mathbf{V}$ này là không gian cột của bất kỳ ma trận $3 \times n$ nào có hạng 2, nếu mọi cột là một tổ hợp của $v_1$ và $v_2$. Đặc biệt, $A$ có thể chỉ có các cột $v_1$ và $v_2$.
- **(f)** $\mathbf{V}$ này là không gian không của bất kỳ ma trận $m \times 3$ nào $B$ có hạng 1, nếu mọi hàng là một bội số của $(0, 0, 1)$. Đặc biệt lấy $B = \begin{bmatrix} 0 & 0 & 1 \end{bmatrix}$. Khi đó $Bv_1 = \mathbf{0}$ và $Bv_2 = \mathbf{0}$.
- **(g)** Một vectơ thứ ba bất kỳ $v_3 = (a, b, c)$ sẽ hoàn thành một cơ sở cho $\mathbf{R}^3$ với điều kiện $c \neq 0$.

**3.4 B** Bắt đầu với ba vectơ độc lập $w_1, w_2, w_3$. Lấy các tổ hợp của những vectơ đó để tạo ra $v_1, v_2, v_3$. Viết các tổ hợp dưới dạng ma trận là $V = WB$:

| $v_1 = w_1 + 2w_2$        | tức là | $\begin{bmatrix} v_1 & v_2 & v_3 \end{bmatrix} = \begin{bmatrix} w_1 & w_2 & w_3 \end{bmatrix}$ | $\begin{bmatrix} 1 & 1 & 0 \\ 2 & 2 & 1 \\ 0 & 1 & c \end{bmatrix}$ |
|--------------------------|----------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|

| $v_2 = w_1 + 2w_2 + w_3$ |          |                                                                                                 |                                                                     |
| $v_3 = w_2 + cw_3$       |          |                                                                                                 |                                                                     |

Bài kiểm tra đối với $B$ để xem liệu $V = WB$ có các cột độc lập hay không là gì? Nếu $c \neq 1$, hãy chỉ ra rằng $v_1, v_2, v_3$ là độc lập tuyến tính. Nếu $c = 1$, hãy chỉ ra rằng các $v$ là *phụ thuộc* tuyến tính.

**Giải** Bài kiểm tra đối với $V$ về sự độc lập của các cột của nó nằm trong định nghĩa đầu tiên của chúng ta: *Không gian không của $V$ chỉ được chứa vectơ không.* Khi đó $x = (0, 0, 0)$ là tổ hợp duy nhất của các cột cho ra $Vx = \text{vectơ không}$.

Nếu $c = 1$ trong bài toán của chúng ta, chúng ta có thể thấy *sự phụ thuộc* theo hai cách. Đầu tiên, $v_1 + v_3$ sẽ giống với $v_2$. (Nếu bạn cộng $w_1 + 2w_2$ với $w_2 + w_3$, bạn nhận được $w_1 + 2w_2 + w_3$ chính là $v_2$). Nói cách khác $v_1 - v_2 + v_3 = \mathbf{0}$ - điều này nói rằng các $v$ không độc lập.

Cách khác là nhìn vào không gian không của $B$. Nếu $c = 1$, vectơ $x = (1, -1, 1)$ nằm trong không gian không đó, và $Bx = \mathbf{0}$. Khi đó chắc chắn $WBx = \mathbf{0}$, cũng chính là $Vx = \mathbf{0}$. Vì vậy các $v$ phụ thuộc. $x = (1, -1, 1)$ cụ thể này từ không gian không một lần nữa cho chúng ta biết rằng $v_1 - v_2 + v_3 = \mathbf{0}$.

Bây giờ giả sử $c \neq 1$. Khi đó ma trận $B$ là khả nghịch. Vì vậy nếu $x$ là *bất kỳ vectơ khác không nào*, chúng ta biết rằng $Bx$ là khác không. Vì các $w$ được cho là độc lập, chúng ta biết thêm rằng $WBx$ là khác không. Vì $V = WB$, điều này nói rằng $x$ *không* nằm trong không gian không của $V$. Nói cách khác, $v_1, v_2, v_3$ độc lập.

Quy tắc chung là "các $v$ độc lập từ các $w$ độc lập khi $B$ là khả nghịch". Và nếu các vectơ này nằm trong $\mathbf{R}^3$, chúng không chỉ độc lập - chúng còn là một cơ sở cho $\mathbf{R}^3$. *"Cơ sở của các $v$ từ cơ sở của các $w$ khi ma trận chuyển đổi cơ sở $B$ là khả nghịch."*

**3.4 C** *(Ví dụ quan trọng)* Giả sử $v_1, \dots, v_n$ là một cơ sở cho $\mathbf{R}^n$ và ma trận $n \times n$ $A$ là khả nghịch. Hãy chỉ ra rằng $Av_1, \dots, Av_n$ cũng là một cơ sở cho $\mathbf{R}^n$.

**Giải** Trong *ngôn ngữ ma trận:* Đặt các vectơ cơ sở $v_1, \dots, v_n$ vào các cột của một ma trận khả nghịch(!) $V$. Khi đó $Av_1, \dots, Av_n$ là các cột của $AV$. Vì $A$ khả nghịch nên $AV$ cũng khả nghịch và các cột của nó tạo thành một cơ sở.

Trong *ngôn ngữ vectơ:* Giả sử $c_1Av_1 + \dots + c_nAv_n = \mathbf{0}$. Đây là $Av = \mathbf{0}$ với $v = c_1v_1 + \dots + c_nv_n$. Nhân với $A^{-1}$ để đạt tới $v = \mathbf{0}$. Theo sự độc lập tuyến tính của các $v$, tất cả các $c_i = 0$. Điều này cho thấy các $Av$ là độc lập.

Để chỉ ra rằng các $Av$ sinh ra $\mathbf{R}^n$, hãy giải $c_1Av_1 + \dots + c_nAv_n = b$, điều này giống như $c_1v_1 + \dots + c_nv_n = A^{-1}b$. Vì các $v$ là một cơ sở, phương trình này phải giải được.

## **Bài Tập 3.4 (Problem Set 3.4)**

**Các câu hỏi 1-10 là về sự độc lập tuyến tính và phụ thuộc tuyến tính.**

**1** Hãy chỉ ra rằng $v_1, v_2, v_3$ độc lập nhưng $v_1, v_2, v_3, v_4$ phụ thuộc:

| $v_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$ | $v_2 = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$ | $v_3 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$ | $v_4 = \begin{bmatrix} 2 \\ 3 \\ 4 \end{bmatrix}$ |
|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|

Giải $c_1v_1 + c_2v_2 + c_3v_3 + c_4v_4 = \mathbf{0}$ hay $Ax = \mathbf{0}$. Các $v$ đi vào các cột của $A$.

**2** (Khuyên làm) Tìm số lượng lớn nhất có thể có của các vectơ độc lập trong số

$$v_1 = \begin{bmatrix} 1 \\ -1 \\ 0 \\ 0 \end{bmatrix}, \quad v_2 = \begin{bmatrix} 1 \\ 0 \\ -1 \\ 0 \end{bmatrix}, \quad v_3 = \begin{bmatrix} 1 \\ 0 \\ 0 \\ -1 \end{bmatrix}, \quad v_4 = \begin{bmatrix} 0 \\ 1 \\ -1 \\ 0 \end{bmatrix}, \quad v_5 = \begin{bmatrix} 0 \\ 1 \\ 0 \\ -1 \end{bmatrix}, \quad v_6 = \begin{bmatrix} 0 \\ 0 \\ 1 \\ -1 \end{bmatrix}$$
(Sửa lại thành phần thứ 4 của $v_6$ cho hợp lý với số chiều không gian là 4)

**3** Chứng minh rằng nếu $a = 0$ hoặc $d = 0$ hoặc $f = 0$ (3 trường hợp), các cột của $U$ phụ thuộc:

$$U = \begin{bmatrix} a & b & c \\ 0 & d & e \\ 0 & 0 & f \end{bmatrix}.$$

**4** Nếu $a, d, f$ trong Câu hỏi 3 đều khác không, hãy chỉ ra rằng nghiệm duy nhất của $Ux = \mathbf{0}$ là $x = \mathbf{0}$. Khi đó ma trận tam giác trên $U$ có các cột độc lập.

**5** Quyết định sự phụ thuộc hay độc lập của
(a) các vectơ $(1, 3, 2)$ và $(2, 1, 3)$ và $(3, 2, 1)$
(b) các vectơ $(1, -3, 2)$ và $(2, 1, -3)$ và $(-3, 2, 1)$.

**6** Chọn ba cột độc lập của $U$. Sau đó thực hiện hai lựa chọn khác. Làm tương tự đối với $A$.

$$U = \begin{bmatrix} 2 & 3 & 7 & 1 \\ 0 & 2 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix} \quad \text{và} \quad A = \begin{bmatrix} 2 & 3 & 4 & 1 \\ 0 & 2 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 4 & 6 & 8 & 2 \end{bmatrix}.$$

**7** Nếu $w_1, w_2, w_3$ là các vectơ độc lập, hãy chỉ ra rằng các hiệu số $v_1 = w_2 - w_3$ và $v_2 = w_1 - w_3$ và $v_3 = w_1 - w_2$ là *phụ thuộc.* Tìm một tổ hợp của các $v$ cho ra số không. Ma trận $A$ nào trong $\begin{bmatrix} v_1 & v_2 & v_3 \end{bmatrix} = \begin{bmatrix} w_1 & w_2 & w_3 \end{bmatrix}A$ là suy biến?

**8** Nếu $w_1, w_2, w_3$ là các vectơ độc lập, hãy chỉ ra rằng các tổng $v_1 = w_2 + w_3$ và $v_2 = w_1 + w_3$ và $v_3 = w_1 + w_2$ là *độc lập.* (Viết $c_1v_1 + c_2v_2 + c_3v_3 = \mathbf{0}$ theo các $w$. Tìm và giải các phương trình đối với các $c$, để chỉ ra rằng chúng bằng không).

**9** Giả sử $v_1, v_2, v_3, v_4$ là các vectơ trong $\mathbf{R}^3$.
(a) Bốn vectơ này phụ thuộc bởi vì \_\_.
(b) Hai vectơ $v_1$ và $v_2$ sẽ phụ thuộc nếu \_\_.
(c) Các vectơ $v_1$ và $(0, 0, 0)$ phụ thuộc bởi vì \_\_.

**10** Tìm hai vectơ độc lập trên mặt phẳng $x + 2y - 3z - t = 0$ trong $\mathbf{R}^4$. Sau đó tìm ba vectơ độc lập. Tại sao không phải là bốn? Mặt phẳng này là không gian không của ma trận nào?

**Các câu hỏi 11-14 là về không gian được *sinh ra* bởi một tập hợp các vectơ. Lấy tất cả các tổ hợp tuyến tính của các vectơ.**

**11** Mô tả không gian con của $\mathbf{R}^3$ (nó là một đường thẳng hay mặt phẳng hay $\mathbf{R}^3$?) được sinh ra bởi
(a) hai vectơ $(1, 1, -1)$ và $(-1, -1, 1)$
(b) ba vectơ $(0, 1, 1)$ và $(1, 1, 0)$ và $(0, 0, 0)$
(c) tất cả các vectơ trong $\mathbf{R}^3$ có các thành phần là số nguyên
(d) tất cả các vectơ có các thành phần dương.

**12** Vectơ $b$ nằm trong không gian con được sinh ra bởi các cột của $A$ khi \_\_ có một nghiệm. Vectơ $c$ nằm trong không gian hàng của $A$ khi \_\_ có một nghiệm. *Đúng hay sai:* Nếu vectơ không nằm trong không gian hàng, các hàng đó phụ thuộc.

**13** Tìm số chiều của 4 không gian này. Hai không gian nào là giống nhau? (a) không gian cột của $A$, (b) không gian cột của $U$, (c) không gian hàng của $A$, (d) không gian hàng của $U$:

$$A = \begin{bmatrix} 1 & 1 & 0 \\ 1 & 3 & 1 \\ 3 & 1 & -1 \end{bmatrix} \quad \text{và} \quad U = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 0 \end{bmatrix}$$

**14** $v + w$ và $v - w$ là các tổ hợp của $v$ và $w$. Viết $v$ và $w$ dưới dạng các tổ hợp của $v + w$ và $v - w$. Hai cặp vectơ \_\_ cùng một không gian. Khi nào chúng là một cơ sở cho cùng một không gian?

**Các câu hỏi 15-25 là về các yêu cầu đối với một cơ sở.**

**15** Nếu $v_1, \dots, v_n$ độc lập tuyến tính, không gian mà chúng sinh ra có số chiều là \_\_. Những vectơ này là một \_\_ cho không gian đó. Nếu các vectơ là các cột của một ma trận $m \times n$, thì $m$ là \_\_ hơn $n$. Nếu $m = n$, ma trận đó là \_\_.

**16** Tìm một cơ sở cho mỗi không gian con này của $\mathbf{R}^4$:
(a) Tất cả các vectơ có các thành phần bằng nhau.
(b) Tất cả các vectơ có tổng các thành phần bằng không.
(c) Tất cả các vectơ vuông góc với $(1, 1, 0, 0)$ và $(1, 0, 1, 1)$.
(d) Không gian cột và không gian không của $I$ ($4 \times 4$).

**17** Tìm ba cơ sở khác nhau cho không gian cột của $U = \begin{bmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$. Sau đó tìm hai cơ sở khác nhau cho không gian hàng của $U$.
(Ma trận $U$ được suy luận từ văn bản bị lỗi "6 1 6  5", tôi dùng ma trận ví dụ phổ biến cho rref).

**18** Giả sử $v_1, v_2, \dots, v_6$ là sáu vectơ trong $\mathbf{R}^4$.
(a) Những vectơ đó (chắc chắn)(chắc chắn không)(có thể không) sinh ra $\mathbf{R}^4$.
(b) Những vectơ đó (chắc chắn)(chắc chắn không)(có thể) độc lập tuyến tính.
(c) Bốn vectơ bất kỳ trong số đó (chắc chắn)(chắc chắn không)(có thể) là một cơ sở cho $\mathbf{R}^4$.

**19** Các cột của $A$ là $n$ vectơ từ $\mathbf{R}^m$. Nếu chúng độc lập tuyến tính, hạng của $A$ là bao nhiêu? Nếu chúng sinh ra $\mathbf{R}^m$, hạng là bao nhiêu? Nếu chúng là một cơ sở cho $\mathbf{R}^m$, thì sao? *Nhìn về phía trước:* Hạng $r$ đếm số lượng các cột \_\_.

**20** Tìm một cơ sở cho mặt phẳng $x - 2y + 3z = 0$ trong $\mathbf{R}^3$. Sau đó tìm một cơ sở cho giao tuyến của mặt phẳng đó với mặt phẳng $xy$. Sau đó tìm một cơ sở cho tất cả các vectơ vuông góc với mặt phẳng.

**21** Giả sử các cột của một ma trận $5 \times 5$ $A$ là một cơ sở cho $\mathbf{R}^5$.
(a) Phương trình $Ax = \mathbf{0}$ chỉ có nghiệm $x = \mathbf{0}$ bởi vì \_\_.
(b) Nếu $b$ nằm trong $\mathbf{R}^5$ thì $Ax = b$ giải được bởi vì các vectơ cơ sở \_\_ $\mathbf{R}^5$.

Kết luận: $A$ khả nghịch. Hạng của nó là 5. Các hàng của nó cũng là một cơ sở cho $\mathbf{R}^5$.

**22** Giả sử $S$ là một không gian con 5 chiều của $\mathbf{R}^6$. Đúng hay sai (cho ví dụ nếu sai):
(a) Mọi cơ sở cho $S$ đều có thể được mở rộng thành một cơ sở cho $\mathbf{R}^6$ bằng cách thêm một vectơ nữa.
(b) Mọi cơ sở cho $\mathbf{R}^6$ đều có thể được rút gọn thành một cơ sở cho $S$ bằng cách loại bỏ một vectơ.

**23** $U$ có được từ $A$ bằng cách trừ hàng 1 khỏi hàng 3:

| $A = \begin{bmatrix} 1 & 3 & 2 \\ 0 & 1 & 1 \\ 1 & 3 & 2 \end{bmatrix}$ | và | $U = \begin{bmatrix} 1 & 3 & 2 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{bmatrix}$ |
|-------------------------------------------------------------------------|-----|-------------------------------------------------------------------------|
|-------------------------------------------------------------------------|-----|-------------------------------------------------------------------------|

Tìm các cơ sở cho hai không gian cột. Tìm các cơ sở cho hai không gian hàng. Tìm các cơ sở cho hai không gian không. Không gian nào giữ nguyên trong phép khử?

**24** Đúng hay sai (đưa ra một lý do chính đáng):
(a) Nếu các cột của một ma trận phụ thuộc, thì các hàng cũng vậy.
(b) Không gian cột của một ma trận $2 \times 2$ giống như không gian hàng của nó.
(c) Không gian cột của một ma trận $2 \times 2$ có cùng số chiều với không gian hàng của nó.
(d) Các cột của một ma trận là một cơ sở cho không gian cột.

**25** Đối với những số $c$ và $d$ nào thì các ma trận này có hạng 2?

| $A = \begin{bmatrix} 1 & 2 & 5 & 0 & 5 \\ 0 & 2 & c & 2 & 2 \\ 0 & 0 & 0 & d & 2 \end{bmatrix}$ | và | $B = \begin{bmatrix} c & d \\ d & c \end{bmatrix}$ |
|-------------------------------------------------------------------------------------------------|-----|----------------------------------------------------|
|-------------------------------------------------------------------------------------------------|-----|----------------------------------------------------|

#### **Các câu hỏi 26-30 là về các không gian mà "vectơ" là ma trận.**

**26** Tìm một cơ sở (và số chiều) cho mỗi không gian con này của các ma trận $3 \times 3$:
(a) Tất cả các ma trận đường chéo.
(b) Tất cả các ma trận đối xứng ($A^T = A$).
(c) Tất cả các ma trận phản đối xứng (skew-symmetric) ($A^T = -A$).

**27** Xây dựng sáu ma trận bậc thang $3 \times 3$ độc lập tuyến tính $U_1, \dots, U_6$.

**28** Tìm một cơ sở cho không gian của tất cả các ma trận $2 \times 3$ có các cột cộng lại bằng không. Tìm một cơ sở cho không gian con có các hàng cũng cộng lại bằng không.

**29** Không gian con nào của các ma trận $3 \times 3$ được sinh ra (lấy tất cả các tổ hợp) bởi
(a) các ma trận khả nghịch?
(b) các ma trận hạng một?
(c) ma trận đơn vị?

**30** Tìm một cơ sở cho không gian các ma trận $2 \times 3$ có không gian không chứa $(2, 1, 1)$.

#### **Các câu hỏi 31-35 là về các không gian mà "vectơ" là hàm số.**

**31** (a) Tìm tất cả các hàm số thỏa mãn $dy/dx = 0$.
(b) Chọn một hàm số cụ thể thỏa mãn $dy/dx = 3$.
(c) Tìm tất cả các hàm số thỏa mãn $dy/dx = 3$.

**32** Không gian cosin $\mathbf{F}_3$ chứa tất cả các tổ hợp $y(x) = A \cos x + B \cos 2x + C \cos 3x$. Tìm một cơ sở cho không gian con với $y(0) = 0$.

**33** Tìm một cơ sở cho không gian các hàm số thỏa mãn
(a) $\frac{dy}{dx} - 2y = 0$
(b) $\frac{dy}{dx} + y = 0$

**34** Giả sử $y_1(x), y_2(x), y_3(x)$ là ba hàm số khác nhau của $x$. Không gian vectơ mà chúng sinh ra có thể có số chiều là 1, 2, hoặc 3. Đưa ra một ví dụ về $y_1, y_2, y_3$ để minh họa cho mỗi khả năng.

**35** Tìm một cơ sở cho không gian các đa thức $p(x)$ có bậc $\leq 3$. Tìm một cơ sở cho không gian con với $p(1) = 0$.

**36** Tìm một cơ sở cho không gian $\mathbf{S}$ của các vectơ $(a, b, c, d)$ với $a + c + d = 0$ và cả cho không gian $\mathbf{T}$ với $a + b = 0$ và $c = 2d$. Số chiều của giao $\mathbf{S} \cap \mathbf{T}$ là bao nhiêu?

**37** Nếu $AS = SA$ đối với *ma trận dịch chuyển (shift matrix)* $S$, hãy chỉ ra rằng $A$ phải có dạng đặc biệt này:

| Nếu | $\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix} \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix}$ | thì $A = \begin{bmatrix} a & b & c \\ 0 & a & b \\ 0 & 0 & a \end{bmatrix}$ |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|

"Không gian con của các ma trận giao hoán với phép dịch chuyển $S$ có số chiều là \_\_."

**38** Những cái nào sau đây là các cơ sở cho $\mathbf{R}^3$?
(a) $(1, 2, 0)$ và $(0, 1, -1)$
(b) $(1, 1, -1)$, $(2, 3, 4)$, $(4, 1, -1)$, $(0, 1, -1)$
(c) $(1, 2, 2)$, $(-1, 2, 1)$, $(0, 8, 0)$
(d) $(1, 2, 2)$, $(-1, 2, 1)$, $(0, 8, 6)$

**39** Giả sử $A$ là ma trận $5 \times 4$ với hạng 4. Chỉ ra rằng $Ax = b$ không có nghiệm khi ma trận $5 \times 5$ $\begin{bmatrix} A & b \end{bmatrix}$ là khả nghịch. Chỉ ra rằng $Ax = b$ giải được khi $\begin{bmatrix} A & b \end{bmatrix}$ là suy biến.

**40** (a) Tìm một cơ sở cho tất cả các nghiệm của $d^4y/dx^4 = y(x)$.
(b) Tìm một nghiệm cụ thể của $d^4y/dx^4 = y(x) + 1$. Tìm nghiệm toàn diện.

# **Thử thách (Challenge Problems)**

**41** Hãy viết ma trận đơn vị $3 \times 3$ dưới dạng một tổ hợp của năm ma trận hoán vị còn lại! Sau đó chỉ ra rằng năm ma trận đó là độc lập tuyến tính. (Giả sử một tổ hợp cho ra $c_1P_1 + \dots + c_5P_5 = \text{ma trận không}$, và kiểm tra các thành phần để chứng minh rằng từ $c_1$ đến $c_5$ tất cả đều phải bằng không). Năm ma trận hoán vị là một cơ sở cho không gian con các ma trận $3 \times 3$ có tổng các hàng và các cột đều bằng nhau.

**42** Chọn $x = (x_1, x_2, x_3, x_4)$ trong $\mathbf{R}^4$. Nó có 24 sự sắp xếp lại giống như $(x_2, x_1, x_3, x_4)$ và $(x_4, x_3, x_1, x_2)$. 24 vectơ đó, bao gồm cả chính $x$, sinh ra một không gian con $\mathbf{S}$. Tìm các vectơ $x$ cụ thể để số chiều của $\mathbf{S}$ là: (a) không, (b) một, (c) ba, (d) bốn.

**43** Các phần giao và các tổng có $\dim(\mathbf{V}) + \dim(\mathbf{W}) = \dim(\mathbf{V} \cap \mathbf{W}) + \dim(\mathbf{V} + \mathbf{W})$.
Bắt đầu với một cơ sở $u_1, \dots, u_r$ cho phần giao $\mathbf{V} \cap \mathbf{W}$. Mở rộng bằng $v_1, \dots, v_s$ để thành một cơ sở cho $\mathbf{V}$, và riêng biệt bằng $w_1, \dots, w_t$ để thành một cơ sở cho $\mathbf{W}$. Chứng minh rằng các $u, v$ và $w$ cùng nhau là *độc lập.* Số chiều sẽ là $(r + s) + (r + t) = r + (r + s + t)$ như mong muốn.

**44** Mike Artin đã đề xuất một cách chứng minh gọn gàng ở mức độ cao hơn cho công thức số chiều đó trong Bài tập 43. Từ tất cả các đầu vào $v$ trong $\mathbf{V}$ và $w$ trong $\mathbf{W}$, "phép biến đổi tổng" tạo ra $v + w$. Những đầu ra đó lấp đầy không gian $\mathbf{V} + \mathbf{W}$. Không gian không chứa tất cả các cặp $v = u, w = -u$ cho các vectơ $u$ trong $\mathbf{V} \cap \mathbf{W}$. (Khi đó $v + w = u - u = \mathbf{0}$). Vậy $\dim(\mathbf{V} + \mathbf{W}) + \dim(\mathbf{V} \cap \mathbf{W})$ bằng $\dim(\mathbf{V}) + \dim(\mathbf{W})$ (*số chiều đầu vào từ $\mathbf{V}$ và $\mathbf{W}$*) theo Định lý Đếm.

*số chiều của đầu ra + số chiều của không gian không = số chiều của đầu vào.*

*Bài toán* Đối với một ma trận $m \times n$ hạng $r$, 3 số chiều đó là bao nhiêu? Đầu ra = không gian cột. Câu hỏi này sẽ được trả lời trong Mục 3.5, bạn có thể làm điều đó ngay bây giờ không?

**45** Bên trong $\mathbf{R}^n$, giả sử $\dim(\mathbf{V}) + \dim(\mathbf{W}) > n$. Chỉ ra rằng một số vectơ khác không nằm trong cả $\mathbf{V}$ và $\mathbf{W}$.

**46** Giả sử $A$ là ma trận $10 \times 10$ và $A^2 = \mathbf{0}$ (ma trận không). Vì vậy $A$ nhân với mỗi cột của $A$ để cho ra vectơ không. Điều này có nghĩa là không gian cột của $A$ được chứa trong \_\_. Nếu $A$ có hạng $r$, các không gian con đó có số chiều là $r \leq 10 - r$. Vì vậy hạng là $r \leq 5$.

# **3.5 Số Chiều Của Bốn Không Gian Con (Dimensions of the Four Subspaces)**

**1** Không gian cột $C(A)$ và không gian hàng $C(A^T)$ đều có *số chiều là $r$* (hạng của $A$).
**2** Không gian không $N(A)$ có *số chiều là $n - r$.* Không gian không bên trái $N(A^T)$ có *số chiều là $m - r$.*
**3** Phép khử tạo ra các cơ sở cho không gian hàng và không gian không của $A$: Chúng giống với $R$.
**4** Phép khử thường làm thay đổi không gian cột và không gian không bên trái (nhưng số chiều không thay đổi).
**5 Các ma trận hạng một:** $A = uv^T = \text{cột nhân với hàng}$: $C(A)$ có cơ sở $u$, $C(A^T)$ có cơ sở $v$.

Định lý chính trong chương này kết nối *hạng* và *số chiều.* *Hạng* của một ma trận là số lượng các phần tử xoay. *Số chiều* của một không gian con là số lượng các vectơ trong một cơ sở. Chúng ta đếm các phần tử xoay hoặc chúng ta đếm các vectơ cơ sở. *Hạng của $A$ tiết lộ số chiều của tất cả bốn không gian con cơ bản.* Dưới đây là các không gian con, bao gồm cả không gian mới.

Hai không gian con đến trực tiếp từ $A$, và hai không gian kia từ $A^T$:

#### *Bốn Không Gian Con Cơ Bản (Four Fundamental Subspaces)*

- 1. *Không gian hàng* là $C(A^T)$, một không gian con của $\mathbf{R}^n$.
- 2. *Không gian cột* là $C(A)$, một không gian con của $\mathbf{R}^m$.
- **3.** *Không gian không* là $N(A)$, một không gian con của $\mathbf{R}^n$.
- **4.** *Không gian không bên trái* là $N(A^T)$, một không gian con của $\mathbf{R}^m$. Đây là không gian mới của chúng ta.

Trong cuốn sách này, không gian cột và không gian không đã đến trước. Chúng ta biết khá rõ về $C(A)$ và $N(A)$. Bây giờ hai không gian con còn lại tiến lên. Không gian hàng chứa tất cả các tổ hợp của các hàng. *Không gian hàng này của $A$ là không gian cột của $A^T$.*

Đối với không gian không bên trái, chúng ta giải $A^Ty = \mathbf{0}$ - hệ đó có kích thước $n \times m$. *Đây là không gian không của $A^T$.* Các vectơ $y$ nằm ở phía *bên trái* của $A$ khi phương trình được viết thành $y^TA = \mathbf{0}^T$. Các ma trận $A$ và $A^T$ thường khác nhau. Không gian cột và không gian không của chúng cũng vậy. Nhưng những không gian đó được kết nối theo một cách tuyệt đối đẹp đẽ.

Phần 1 của Định lý Cơ bản tìm số chiều của bốn không gian con. Một sự thật nổi bật: *Không gian hàng và không gian cột có cùng số chiều $r$.* Con số $r$ này là **hạng** của ma trận. Sự thật quan trọng khác liên quan đến hai không gian không:

*$N(A)$ và $N(A^T)$ có số chiều $n - r$ và $m - r$, để tạo thành đủ $n$ và $m$.* (Sửa lại bản gốc $rn - r$ thành $m - r$ cho hợp lý)

Phần 2 của Định lý Cơ bản sẽ mô tả cách bốn không gian con khớp với nhau (hai trong $\mathbf{R}^n$ và hai trong $\mathbf{R}^m$). Điều đó hoàn thành "cách đúng đắn" để hiểu mọi $Ax = b$. Hãy kiên trì - bạn đang làm toán học thực sự.

# **Bốn Không Gian Con Cho $R$ (The Four Subspaces for $R$)**

Giả sử $A$ được rút gọn thành dạng bậc thang theo hàng $R$ của nó. Đối với dạng đặc biệt đó, bốn không gian con rất dễ xác định. Chúng ta sẽ tìm một cơ sở cho mỗi không gian con và kiểm tra số chiều của nó. Sau đó chúng ta theo dõi xem các không gian con thay đổi như thế nào (hai trong số chúng không thay đổi!) khi chúng ta nhìn lại $A$. Điểm chính là *bốn số chiều là như nhau đối với $A$ và $R$.*

Làm một ví dụ $3 \times 5$ cụ thể, hãy nhìn vào bốn không gian con cho ma trận bậc thang $R$ này:

| $m = 3$ | $R = \begin{bmatrix} 1 & 3 & 0 & 0 & 7 \\ 0 & 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$ | các hàng phần tử xoay 1 và 2    |
|---------|-------------------------------------------------------------------------------------------------|-----------------------|
| $n = 5$ |                                                                                                 |                       |
| $r = 2$ |                                                                                                 | các cột phần tử xoay 1 và 4 |

Hạng của ma trận này là $r = 2$ *(hai phần tử xoay).* Lần lượt xét bốn không gian con.

### 1. *Không gian hàng* của $R$ có số chiều là 2, khớp với hạng.

**Lý do:** Hai hàng đầu tiên là một cơ sở. Không gian hàng chứa các tổ hợp của cả ba hàng, nhưng hàng thứ ba (hàng số không) không thêm gì mới. Vì vậy hàng 1 và 2 sinh ra không gian hàng $C(R^T)$.

Các hàng phần tử xoay 1 và 2 là độc lập. Điều đó rõ ràng đối với ví dụ này, và nó luôn luôn đúng. Nếu chúng ta chỉ nhìn vào các cột phần tử xoay, chúng ta thấy ma trận đơn vị $r \times r$. Không có cách nào để kết hợp các hàng của nó để cho ra hàng số không (ngoại trừ tổ hợp với tất cả các hệ số đều bằng không). Vì vậy $r$ hàng phần tử xoay là một cơ sở cho không gian hàng.

#### *Số chiều của không gian hàng là hạng $r$. Các hàng khác không của $R$ tạo thành một cơ sở.*

#### **2.** *Không gian cột* của $R$ cũng có số chiều $r = 2$.

**Lý do:** Các cột phần tử xoay 1 và 4 tạo thành một cơ sở cho $C(R)$. Chúng độc lập vì chúng bắt đầu bằng ma trận đơn vị $r \times r$. Không có tổ hợp nào của các cột phần tử xoay đó có thể cho ra cột số không (ngoại trừ tổ hợp với tất cả các hệ số đều bằng không). Và chúng cũng sinh ra không gian cột. Mọi cột khác (tự do) đều là một tổ hợp của các cột phần tử xoay. Thực ra các tổ hợp mà chúng ta cần chính là ba nghiệm đặc biệt!

Cột 2 là 3 (cột 1). Nghiệm đặc biệt là
$$(-3, 1, 0, 0, 0).$$
Cột 3 là 0 (cột 1) + 0 (cột 4). Nghiệm đặc biệt là $(0, 0, 1, 0, 0)$. (Sửa lại bản gốc 5 (cột 1) thành 0 vì cột 3 là cột 0)
Cột 5 là 7 (cột 1) + 2 (cột 4). Nghiệm đặc biệt đó là $(-7, 0, 0, -2, 1)$.

Các cột phần tử xoay độc lập, và chúng sinh ra không gian, vì vậy chúng là một cơ sở cho $C(R)$.

*Số chiều của không gian cột là hạng $r$. Các cột phần tử xoay tạo thành một cơ sở.*

3. *Không gian không* của $R$ có số chiều $n - r = 5 - 2$. Có $n - r = 3$ biến tự do. Ở đây $x_2, x_3, x_5$ là tự do (không có phần tử xoay trong các cột đó). Chúng tạo ra ba nghiệm đặc biệt cho $Rx = \mathbf{0}$. Gán một biến tự do bằng 1, và giải để tìm $x_1$ và $x_4$.

$$s_2 = \begin{bmatrix} -3 \\ 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}, \quad s_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \\ 0 \end{bmatrix}, \quad s_5 = \begin{bmatrix} -7 \\ 0 \\ 0 \\ -2 \\ 1 \end{bmatrix}, \quad \begin{aligned} Rx &= \mathbf{0} \text{ có} \\ &\text{nghiệm toàn diện là} \\ x &= x_2 s_2 + x_3 s_3 + x_5 s_5 \\ &\text{Không gian không có số chiều là 3.} \end{aligned}$$
(Sửa lại $s_3$ từ $\begin{bmatrix} -5 \\ 0 \\ 1 \\ 0 \\ 0 \end{bmatrix}$ thành $\begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \\ 0 \end{bmatrix}$ cho khớp với ma trận R)

**Lý do:** Có một nghiệm đặc biệt cho mỗi biến tự do. Với $n$ biến và $r$ phần tử xoay, còn lại $n - r$ biến tự do và các nghiệm đặc biệt. Các nghiệm đặc biệt độc lập, bởi vì chúng chứa ma trận đơn vị ở các hàng 2, 3, 5. Vì vậy $N(R)$ có số chiều $n - r$.

*Không gian không có số chiều $n - r$. Các nghiệm đặc biệt tạo thành một cơ sở.*

**4.** *Không gian không của* $R^T$ *(không gian không bên trái của $R$)* có số chiều $m - r = 3 - 2$.

**Lý do:** Phương trình $R^Ty = \mathbf{0}$ tìm kiếm các tổ hợp của các cột của $R^T$ (các hàng của $R$) cho ra số không. Phương trình này $R^Ty = \mathbf{0}$ hay $y^TR = \mathbf{0}^T$ là

|                 | $y_1 \begin{bmatrix} 1 & 3 & 0 & 0 & 7 \end{bmatrix}$  |  |  |  |     |
|-----------------|------------------------|--|--|--|-----|
| Không gian không bên trái  |                        |  |  |  |     |
| Tổ hợp     | $+y_2 \begin{bmatrix} 0 & 0 & 0 & 1 & 2 \end{bmatrix}$ |  |  |  | (1) |
| của các hàng bằng không | $+y_3 \begin{bmatrix} 0 & 0 & 0 & 0 & 0 \end{bmatrix}$ |  |  |  |     |
|                 | $= \begin{bmatrix} 0 & 0 & 0 & 0 & 0 \end{bmatrix}$      |  |  |  |     |
(Sửa lại ma trận hàng 1 cho đúng với ma trận R $\begin{bmatrix} 1 & 3 & 0 & 0 & 7 \end{bmatrix}$ thay vì $\begin{bmatrix} 1 & 3 & 5 & 0 & 2 \end{bmatrix}$)

Các nghiệm $y_1, y_2, y_3$ khá rõ ràng. Chúng ta cần $y_1 = 0$ và $y_2 = 0$. Biến $y_3$ là tự do (nó có thể là bất cứ thứ gì). **Không gian không của $R^T$ chứa tất cả các vectơ** $y = (0, 0, y_3)$.

Trong tất cả các trường hợp $R$ kết thúc với $m - r$ hàng số không. Mọi tổ hợp của $m - r$ hàng này đều cho ra số không. Đây là *những* tổ hợp duy nhất của các hàng của $R$ cho ra số không, bởi vì các hàng phần tử xoay là độc lập tuyến tính. Vì vậy $y$ trong không gian không bên trái có $y_1 = 0, \dots, y_r = 0$.

*Nếu $A$ có kích thước $m \times n$ với hạng $r$, không gian không bên trái của nó có số chiều $m - r$.*

Tại sao đây là một "không gian không *bên trái*"? Lý do là $R^Ty = \mathbf{0}$ có thể được chuyển vị thành $y^TR = \mathbf{0}^T$. Bây giờ $y^T$ là một vectơ hàng ở *bên trái* của $R$. Bạn thấy các $y$ trong phương trình (1) đang nhân với các hàng. Không gian con này đến thứ tư, và một số sách đại số tuyến tính bỏ qua nó - nhưng điều đó đã bỏ lỡ vẻ đẹp của toàn bộ chủ đề này.

*Trong $\mathbf{R}^n$, không gian hàng và không gian không có số chiều $r$ và $n - r$ (cộng lại bằng $n$). Trong $\mathbf{R}^m$, không gian cột và không gian không bên trái có số chiều $r$ và $m - r$ (tổng là $m$).*

# **Bốn Không Gian Con Cho $A$ (The Four Subspaces for $A$)**

Chúng ta vẫn còn một công việc phải làm. *Số chiều của các không gian con đối với $A$ giống như đối với $R$.* Công việc là giải thích tại sao. $A$ bây giờ là bất kỳ ma trận nào rút gọn được thành $R = \text{rref}(A)$.

| $A$ này rút gọn thành $R$ | $A = \begin{bmatrix} 1 & 3 & 5 & 0 & 7 \\ 0 & 0 & 0 & 1 & 2 \\ 1 & 3 & 5 & 1 & 9 \end{bmatrix}$ | Lưu ý $C(A) \neq C(R)!$ | $2$ |
|-------------------------|-------------------------------------------------------------------------------------------------|--------------------------|-----|
|                         |                                                                                                 |                          |     |
|                         |                                                                                                 |                          |     |
(Ở đây sách thay đổi ma trận $A$ so với ma trận $R$ ở trên một chút, nhưng vẫn giữ nguyên hạng $r=2$)

![](images/_page_193_Diagram_5.jpeg)

Hình 3.5: Số chiều của Bốn Không Gian Con Cơ Bản (cho $R$ và cho $A$).

#### **1** *$A$ có cùng không gian hàng như $R$.* **Cùng số chiều $r$ và cùng cơ sở.**

*Lý do:* Mọi hàng của **A** là một tổ hợp của các hàng của **R.** Hơn nữa mọi hàng của **R** là một tổ hợp của các hàng của **A.** Phép khử thay đổi các hàng, nhưng không thay đổi *các không gian* hàng.

Vì $A$ có cùng không gian hàng với $R$, chúng ta có thể chọn **r** hàng đầu tiên của $R$ làm một cơ sở. Hoặc chúng ta có thể chọn $r$ hàng thích hợp của **A** ban đầu. Chúng có thể không phải lúc nào cũng là **r** hàng *đầu tiên* của $A$, bởi vì những hàng đó có thể phụ thuộc. **r** hàng tốt của $A$ là những hàng cuối cùng trở thành các hàng phần tử xoay trong **R**.

### **2** *Không gian cột của $A$ có số chiều là* **r.** *Hạng cột bằng hạng hàng.*

### *Định lý Hạng (Rank Theorem): Số lượng các cột độc lập = số lượng các hàng độc lập.*

*Lý do sai:* "$A$ và $R$ có cùng không gian cột." Điều này là sai. *Các cột của $R$* thường kết thúc bằng các số không. Các cột của $A$ không thường kết thúc bằng các số không. Khi đó $C(A)$ không phải là $C(R)$.

*Lý do đúng:* Những tổ hợp *giống nhau* của các cột cho ra số không (hoặc khác không) đối với $A$ và $R$. Phụ thuộc trong $A \Leftrightarrow$ phụ thuộc trong $R$. Nói cách khác: $Ax = \mathbf{0}$ *chính xác khi $Rx = \mathbf{0}$.* Các không gian cột là khác nhau, nhưng *số chiều* của chúng giống nhau - bằng $r$.

*Kết luận* $r$ cột phần tử xoay của $A$ là một cơ sở cho không gian cột $C(A)$ *của nó*.

### **3** *$A$ có cùng không gian không như $R$.* **Cùng số chiều $n - r$ và cùng cơ sở.**

*Lý do:* Các bước khử không làm thay đổi các nghiệm. Các nghiệm đặc biệt là một cơ sở cho không gian không này (như chúng ta luôn biết). Có $n - r$ biến tự do, vì vậy số chiều của không gian không là $n - r$. Đây là **Định lý Đếm (Counting Theorem)**: $r + (n - r)$ bằng $n$.

(**số chiều của không gian cột**) + (**số chiều của không gian không**) = **số chiều của** $\mathbf{R}^n$.

#### 4 *Không gian không bên trái của $A$* (không gian không của $A^T$) *có số chiều $m - r$.*

*Lý do: $A^T$* cũng là một ma trận tốt như $A$. Khi chúng ta biết các số chiều cho mọi $A$, chúng ta cũng biết chúng cho $A^T$. Không gian cột của nó đã được chứng minh là có số chiều $r$. Vì $A^T$ có kích thước $n \times m$, "toàn bộ không gian" bây giờ là $\mathbf{R}^m$. Quy tắc đếm đối với $A$ là $r + (n - r) = n$. Quy tắc đếm đối với $A^T$ là $r + (m - r) = m$. Bây giờ chúng ta có tất cả các chi tiết của một định lý lớn:

#### *Định lý Cơ Bản Của Đại Số Tuyến Tính (Fundamental Theorem of Linear Algebra),* **Phần 1**

*Không gian cột và không gian hàng đều có số chiều $r$.*

*Các không gian không có số chiều $n - r$ và $m - r$.*

Bằng cách tập trung vào *các không gian* vectơ, không phải vào từng con số hay vectơ riêng lẻ, chúng ta nhận được những quy tắc rõ ràng này. Bạn sẽ sớm coi chúng là điều hiển nhiên - cuối cùng chúng bắt đầu trông có vẻ rõ ràng. Nhưng nếu bạn viết ra một ma trận $11 \times 17$ với 187 phần tử khác không, tôi không nghĩ hầu hết mọi người sẽ thấy tại sao những sự thật này là đúng:

| Hai sự thật then chốt | $\dim(C(A)) = \dim(C(A^T)) = \text{hạng của } A$<br>$\dim(C(A)) + \dim(N(A)) = 17.$ |
|---------------|--------------------------------------------------------------------------------------------------------------|
|---------------|--------------------------------------------------------------------------------------------------------------|

**Ví dụ 1** $A = \begin{bmatrix} 1 & 2 & 3 \end{bmatrix}$ có $m = 1$ và $n = 3$ và hạng $r = 1$.

Không gian hàng là một đường thẳng trong $\mathbf{R}^3$. Không gian không là mặt phẳng $Ax = x_1 + 2x_2 + 3x_3 = 0$. Mặt phẳng này có số chiều là 2 (chính là $3 - 1$). Các số chiều cộng lại là $1 + 2 = 3$.

Các cột của ma trận $1 \times 3$ này nằm trong $\mathbf{R}^1$! Không gian cột là toàn bộ $\mathbf{R}^1$. Không gian không bên trái chỉ chứa vectơ không. Nghiệm duy nhất của $A^Ty = \mathbf{0}$ là $y = \mathbf{0}$, không có bội số nào khác của $\begin{bmatrix} 1 & 2 & 3 \end{bmatrix}$ cho ra hàng số không. Do đó $N(A^T)$ là $\mathbf{Z}$, không gian không (zero space) có số chiều là 0 (chính là $m - r$). Trong $\mathbf{R}^m$, số chiều của $C(A)$ và $N(A^T)$ cộng lại là $1 + 0 = 1$.

**Ví dụ 2**    
$$A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix}$$
 có $m = 2$ với $n = 3$ và hạng $r = 1$.

Không gian hàng là cùng đường thẳng đi qua $(1, 2, 3)$. Không gian không phải là cùng mặt phẳng $x_1 + 2x_2 + 3x_3 = 0$. Các số chiều của đường thẳng và mặt phẳng vẫn cộng lại là $1 + 2 = 3$.

Tất cả các cột đều là bội số của cột đầu tiên $\begin{bmatrix} 1 \\ 2 \end{bmatrix}$. Hai lần hàng đầu tiên trừ đi hàng thứ hai là hàng số không. Do đó $A^Ty = \mathbf{0}$ có nghiệm $y = (2, -1)$. Không gian cột và không gian không bên trái là **hai đường thẳng vuông góc** trong $\mathbf{R}^2$. Các số chiều $1 + 1 = 2$.

Không gian cột = đường thẳng đi qua $\begin{bmatrix} 1 \\ 2 \end{bmatrix}$ Không gian không bên trái = đường thẳng đi qua $\begin{bmatrix} 2 \\ -1 \end{bmatrix}$.

Nếu $A$ có ba hàng giống nhau, hạng của nó là \_\_. Hai trong số các $y$ trong không gian không bên trái của nó là gì?

#### *Các $y$ trong không gian không bên trái kết hợp các hàng để cho ra hàng số không.*

**Ví dụ 3** Bạn đã gần hoàn thành ba chương với những phương trình bịa ra, và điều này không thể kéo dài mãi được. Đây là một ví dụ tốt hơn về năm phương trình (một phương trình cho mỗi cạnh trong Hình 3.6). Năm phương trình có bốn ẩn số (một cho mỗi nút). Ma trận trong $Ax = b$ là một **ma trận liên thuộc (incidence matrix).** Ma trận $A$ này có $1$ và $-1$ trên mỗi hàng.

| Các hiệu số $Ax = b$       | $-x_1$ | $+x_2$ |        |        | $= b_1$ |         |
|----------------------------|--------|--------|--------|--------|---------|---------|
| dọc theo các cạnh 1, 2, 3, 4, 5 | $-x_1$ |        | $+x_3$ |        | $= b_2$ |         |
| giữa các nút 1, 2, 3, 4    |        | $-x_2$ | $+x_3$ |        | $= b_3$ | (3)     |
|                            |        | $-x_2$ |        | $+x_4$ | $= b_4$ |         |
|                            |        |        | $-x_3$ | $+x_4$ | $= b_5$ |
(Sửa lại phương trình thứ 4 và 5 cho khớp với ma trận A)

Nếu bạn hiểu bốn không gian con cơ bản cho ma trận này *(không gian cột và không gian không cho $A$ và $A^T$)* bạn đã nắm bắt được những ý tưởng trung tâm của đại số tuyến tính.

(Sửa lại biểu diễn ma trận theo phương trình trên)
$$A = \begin{bmatrix} -1 & 1 & 0 & 0 \\ -1 & 0 & 1 & 0 \\ 0 & -1 & 1 & 0 \\ 0 & -1 & 0 & 1 \\ 0 & 0 & -1 & 1 \end{bmatrix}$$

Hình 3.6: Một "đồ thị" (graph) với 5 cạnh và 4 nút. $A$ là ma trận liên thuộc $5 \times 4$ của nó.

**Không gian không** $N(A)$ Để tìm không gian không, chúng ta đặt $b = \mathbf{0}$. Khi đó phương trình đầu tiên nói rằng $x_1 = x_2$. Phương trình thứ hai là $x_3 = x_1$. Phương trình 4 là $x_2 = x_4$. *Tất cả bốn ẩn số* $x_1, x_2, x_3, x_4$ *đều có cùng giá trị* $c$. Các vectơ $x = (c, c, c, c)$ lấp đầy không gian không của $A$.

Không gian không đó là một đường thẳng trong $\mathbf{R}^4$. Nghiệm đặc biệt $x = (1, 1, 1, 1)$ là một cơ sở cho $N(A)$. Số chiều của $N(A)$ là 1 (một vectơ trong cơ sở). *Hạng của $A$ phải là 3, vì* $n - r = 4 - 3 = 1$. Bây giờ chúng ta biết số chiều của tất cả bốn không gian con.

Không gian cột $C(A)$ Phải có $r = 3$ cột độc lập. Cách nhanh nhất là nhìn vào 3 cột đầu tiên. Cách có hệ thống là tìm $R = \text{rref}(A)$.

| Các cột | $\begin{bmatrix} -1 & 1 & 0 \\ -1 & 0 & 1 \\ 0 & -1 & 1 \\ 0 & -1 & 0 \\ 0 & 0 & -1 \end{bmatrix}$ | $R =$ | Dạng bậc thang | $= \begin{bmatrix} 1 & 0 & 0 & -1 \\ 0 & 1 & 0 & -1 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$ |
|---------|----|----|-------|--------------|
| 1, 2, 3 |  |  |  | rút gọn theo hàng |
| của A    |  |  |  |              |

Từ $R$, một lần nữa chúng ta lại thấy nghiệm đặc biệt $x = (1, 1, 1, 1)$. 3 cột đầu tiên là cơ sở, cột thứ tư là tự do. Để tạo ra một cơ sở cho $C(A)$ chứ không phải $C(R)$, chúng ta quay lại các cột 1, 2, 3 của $A$. Không gian cột có số chiều $r = 3$.

Không gian hàng $C(A^T)$ Số chiều lại phải là $r = 3$. Nhưng 3 hàng đầu tiên của $A$ *không độc lập:* hàng 3 = hàng 2 - hàng 1. Do đó hàng 3 trở thành số không trong phép khử, và hàng 3 được hoán đổi với hàng 4. *Ba hàng độc lập đầu tiên là hàng 1, 2, 4.* Ba hàng đó là một cơ sở (một cơ sở khả dĩ) cho không gian hàng.

Tôi nhận thấy rằng các cạnh 1, 2, 3 tạo thành một vòng lặp (loop) trong hình vẽ: Các hàng 1, 2, 3 phụ thuộc. Các cạnh 1, 2, 4 tạo thành một cây (tree) trong hình vẽ. Cây không có vòng lặp! Các hàng 1, 2, 4 độc lập.

Không gian không bên trái $N(A^T)$ Bây giờ chúng ta giải $A^Ty = \mathbf{0}$. Các tổ hợp của các hàng cho ra số không. Chúng ta đã nhận thấy rằng hàng 3 = hàng 2 - hàng 1, vì vậy một nghiệm là $y = (1, -1, 1, 0, 0)$. Tôi sẽ nói: $y$ đó đến từ việc đi theo vòng lặp phía trên trong hình vẽ. Một $y$ khác đến từ việc đi quanh vòng lặp phía dưới và nó là $y = (0, 0, -1, 1, -1)$: *hàng* 3 = *hàng* 4 - *hàng* 5. Hai $y$ đó độc lập, chúng giải $A^Ty = \mathbf{0}$, và số chiều của $N(A^T)$ là $m - r = 5 - 3 = 2$. Vậy là chúng ta có một cơ sở cho không gian không bên trái.

Bạn có thể hỏi làm thế nào mà các "vòng lặp" và các "cây" lại chui vào bài toán này. Điều đó không cần phải xảy ra. Chúng ta có thể đã sử dụng phép khử để giải $A^Ty = \mathbf{0}$. Ma trận $4 \times 5$ $A^T$ sẽ có ba cột phần tử xoay 1, 2, 4 và hai cột tự do 3, 5. Có hai nghiệm đặc biệt và không gian không của $A^T$ có số chiều là hai: $m - r = 5 - 3 = 2$. Nhưng các *vòng lặp* và các *cây* xác định các *hàng phụ thuộc* và các *hàng độc lập* một cách đẹp đẽ. Chúng ta sử dụng chúng trong Mục 10.1 cho mọi ma trận liên thuộc giống như $A$ này.

Các phương trình $Ax = b$ cho các "điện áp" $x_1, x_2, x_3, x_4$ tại bốn nút. Các phương trình $A^Ty = \mathbf{0}$ cho các "dòng điện" $y_1, y_2, y_3, y_4, y_5$ trên năm cạnh. Hai phương trình này là Định luật Điện áp Kirchhoff và Định luật Dòng điện Kirchhoff. Những từ đó áp dụng cho một mạng lưới điện. Nhưng những ý tưởng đằng sau những từ đó áp dụng cho khắp các lĩnh vực kỹ thuật và khoa học và kinh tế và kinh doanh.

Đồ thị là *mô hình quan trọng nhất trong toán học ứng dụng rời rạc.* Bạn thấy đồ thị ở khắp mọi nơi: những con đường, đường ống, dòng máu, não bộ, Web, nền kinh tế của một quốc gia hoặc thế giới. Chúng ta có thể hiểu được các ma trận $A$ và $A^T$ của chúng.

# **Các Ma Trận Hạng Một (Rank One Matrices) (Ôn Tập)**

Giả sử mọi hàng đều là một bội số của hàng đầu tiên. Đây là một ví dụ điển hình:

$$\begin{bmatrix} 2 & 3 & 7 & 8 \\ 2a & 3b & 7a & 8a \\ 2b & 3b & 7b & 8b \end{bmatrix} = \begin{bmatrix} 1 \\ a \\ b \end{bmatrix} \begin{bmatrix} 2 & 3 & 7 & 8 \end{bmatrix} = uv^T$$
(Sửa lại cột 2 thành $3a, 3b$ cho đúng)
$$\begin{bmatrix} 2 & 3 & 7 & 8 \\ 2a & 3a & 7a & 8a \\ 2b & 3b & 7b & 8b \end{bmatrix} = \begin{bmatrix} 1 \\ a \\ b \end{bmatrix} \begin{bmatrix} 2 & 3 & 7 & 8 \end{bmatrix} = uv^T$$

Bên trái là một ma trận có ba hàng. Nhưng *không gian* hàng của nó chỉ có số chiều = 1. Vectơ hàng $v^T = \begin{bmatrix} 2 & 3 & 7 & 8 \end{bmatrix}$ cho chúng ta biết một cơ sở cho không gian hàng đó. *Hạng hàng là $1$.*

Bây giờ hãy nhìn vào các cột. "Hạng cột bằng hạng hàng, đó là $1$." Tất cả các cột của ma trận phải là các bội số của một cột. Bạn có thấy rằng quy tắc then chốt này của đại số tuyến tính là đúng không? Vectơ cột $u = (1, a, b)$ được nhân với $2, 3, 7, 8$. Vectơ khác không $u$ đó là một cơ sở cho không gian cột. *Hạng cột cũng là $1$.*

**Mọi ma trận hạng một đều là một cột nhân với một hàng**      
$$A = uv^T$$

# **Ma Trận Hạng Hai = Hạng Một cộng Hạng Một (Rank Two Matrices = Rank One plus Rank One)**

Đây là một ma trận $A$ có hạng $r = 2$. Chúng ta không thể thấy ngay $r$ từ $A$. Vì vậy chúng ta rút gọn ma trận bằng các phép toán hàng thành $R = \text{rref}(A)$. Một ma trận khử $E$ nào đó đơn giản hóa $A$ thành $EA = R$. Sau đó ma trận nghịch đảo $C = E^{-1}$ kết nối $R$ trở lại với $A = CR$.

Bạn đã biết điểm chính rồi: **$R$ có cùng không gian hàng như $A$.**

| Hạng 2 | $A = \begin{bmatrix} 1 & 0 & 3 \\ 1 & 1 & 7 \\ 4 & 2 & 20 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 4 & 2 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 3 \\ 0 & 1 & 4 \\ 0 & 0 & 0 \end{bmatrix} = CR.$ | (4) |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|

Không gian hàng của $R$ rõ ràng có hai vectơ cơ sở $v_1^T = \begin{bmatrix} 1 & 0 & 3 \end{bmatrix}$ và $v_2^T = \begin{bmatrix} 0 & 1 & 4 \end{bmatrix}$. Vì vậy không gian hàng (y như vậy!) của $A$ cũng có cơ sở này: *hạng hàng* = 2. Việc nhân $C$ với $R$ nói rằng hàng 3 của $A$ là $4v_1^T + 2v_2^T$.

**Bây giờ hãy nhìn vào các cột.** Các cột phần tử xoay của $R$ rõ ràng là $(1, 0, 0)$ và $(0, 1, 0)$. Do đó các cột phần tử xoay của $A$ cũng nằm ở các cột 1 và 2: $u_1 = (1, 1, 4)$ và $u_2 = (0, 1, 2)$. Lưu ý rằng $C$ có cùng hai cột đầu tiên đó! Điều đó đã được đảm bảo vì việc nhân với hai cột của ma trận đơn vị (trong $R$) sẽ không làm thay đổi các cột phần tử xoay $u_1$ và $u_2$.

Khi bạn đưa các chữ cái vào cho các cột và các hàng, bạn thấy **hạng 2 = hạng 1 + hạng 1**.

Ma trận $A$ Hạng hai
$$A = \begin{bmatrix} u_1 & u_2 & u_3 \end{bmatrix} \begin{bmatrix} v_1^T \\ v_2^T \\ \text{hàng số không} \end{bmatrix} = u_1v_1^T + u_2v_2^T = (\text{hạng 1}) + (\text{hạng 1}).$$


Bạn đã thấy bước cuối cùng đó chưa? Tôi đã nhân các ma trận bằng cách sử dụng **các cột nhân với các hàng.** Điều đó là hoàn hảo cho bài toán này. *Mọi ma trận hạng $r$ đều là tổng của $r$ ma trận hạng một:* Các cột phần tử xoay của $A$ nhân với các hàng khác không của $R$. Hàng $\begin{bmatrix} 0 & 0 & 0 \end{bmatrix}$ đơn giản là biến mất.

Các cột phần tử xoay $u_1$ và $u_2$ là một cơ sở cho không gian cột, điều mà bạn đã biết.

#### **• ÔN TẬP CÁC Ý TƯỞNG CHÍNH (REVIEW OF THE KEY IDEAS) •**

- **1.** $r$ hàng phần tử xoay của $R$ là một cơ sở cho các không gian hàng của $R$ và $A$ (cùng một không gian).
- **2.** $r$ cột phần tử xoay của $A$(!) là một cơ sở cho không gian cột $C(A)$ của nó.
- **3.** Sau đó $n - r$ nghiệm đặc biệt là một cơ sở cho các không gian không của $A$ và $R$ (cùng một không gian).
- **4.** Nếu $EA = R$, thì $m - r$ hàng cuối cùng của $E$ là một cơ sở cho không gian không bên trái của $A$.

*Lưu ý về bốn không gian con* Định lý Cơ bản trông giống như đại số thuần túy, nhưng nó có những ứng dụng rất quan trọng. Điều tôi yêu thích là các mạng lưới trong Chương 10 (thường tôi đi tới Mục 10.1 cho bài giảng tiếp theo của mình). Phương trình đối với $y$ trong không gian không bên trái là $A^Ty = \mathbf{0}$:

*Dòng chảy vào một nút bằng dòng chảy ra. Định luật Dòng điện Kirchhoff là "phương trình cân bằng" (balance equation).*

Đây hẳn là phương trình quan trọng nhất trong toán học ứng dụng. Tất cả các mô hình trong khoa học và kỹ thuật và kinh tế đều liên quan đến sự cân bằng - của lực hoặc dòng nhiệt hoặc điện tích hoặc động lượng hoặc tiền bạc. Phương trình cân bằng đó, cộng với Định luật Hooke hoặc Định luật Ohm hoặc một định luật nào đó kết nối "thế năng" với "dòng chảy", mang đến một khuôn khổ rõ ràng cho toán học ứng dụng.

Sách giáo khoa của tôi về *Khoa học Máy tính và Kỹ thuật (Computational Science and Engineering)* phát triển khuôn khổ đó, cùng với các thuật toán để giải các phương trình: Sai phân hữu hạn, phần tử hữu hạn, các phương pháp phổ, các phương pháp lặp, và đa lưới (multigrid).

#### **• CÁC VÍ DỤ ĐÃ GIẢI (WORKED EXAMPLES) •**

**3.5 A** Đặt bốn số $1$ vào một ma trận $5 \times 6$ gồm toàn số không, giữ cho số chiều của *không gian hàng* của nó càng nhỏ càng tốt. Mô tả tất cả các cách để làm cho số chiều của *không gian cột* của nó càng nhỏ càng tốt. Mô tả tất cả các cách để làm cho số chiều của *không gian không* của nó càng nhỏ càng tốt. Làm thế nào để làm cho *tổng các số chiều của tất cả bốn không gian con nhỏ?*

**Giải** Hạng là 1 nếu bốn số 1 đi vào cùng một hàng, hoặc vào cùng một cột. Chúng cũng có thể đi vào *hai hàng và hai cột* (ví dụ $a_{ii} = a_{ij} = a_{ji} = a_{jj} = 1$). Vì không gian cột và không gian hàng luôn có cùng số chiều, điều này trả lời hai câu hỏi đầu tiên: Số chiều là 1.

Không gian không có số chiều nhỏ nhất có thể của nó là $6 - 4 = 2$ khi hạng là $r = 4$. Để đạt được hạng 4, các số 1 phải đi vào bốn hàng khác nhau và bốn cột khác nhau.

**Bạn không thể làm gì về tổng** $r + (n-r) + r + (m-r) = n + m$. Nó sẽ là $6 + 5 = 11$ bất kể các số 1 được đặt như thế nào. Tổng là 11 ngay cả khi không có bất kỳ số 1 nào...

Nếu tất cả các phần tử khác của $A$ đều là số 2 thay vì số 0, những câu trả lời này thay đổi như thế nào?

**3.5 B** Sự thật: Tất cả các hàng của $AB$ là các tổ hợp của các hàng của $B$. Do đó không gian hàng của $AB$ được chứa trong (có thể bằng) không gian hàng của $B$. **Hạng $(AB) \leq$ hạng $(B)$.** Tất cả các cột của $AB$ là các tổ hợp của các cột của $A$. Do đó không gian cột của
$AB$ được chứa trong (có thể bằng) không gian cột của $A$. **Hạng $(AB) \leq$ hạng $(A)$.** Nếu chúng ta nhân với một ma trận *khả nghịch*, hạng sẽ không thay đổi. Hạng không thể giảm xuống,
bởi vì khi chúng ta nhân với ma trận nghịch đảo, hạng không thể nhảy ngược lên.

### **Bài Tập 3.5 (Problem Set 3.5)**

**1** (a) Nếu một ma trận $7 \times 9$ có hạng 5, số chiều của bốn không gian con là bao nhiêu? Tổng của tất cả bốn số chiều là bao nhiêu?
(b) Nếu một ma trận $3 \times 4$ có hạng 3, không gian cột và không gian không bên trái của nó là gì?

**2** Tìm các cơ sở và các số chiều cho bốn không gian con liên kết với $A$ và $B$:

| $A = \begin{bmatrix} 1 & 2 & 4 \\ 2 & 4 & 8 \end{bmatrix}$ | và | $B = \begin{bmatrix} 1 & 2 & 4 \\ 2 & 5 & 8 \end{bmatrix}$ |
|---------------------------------------------------|-----|---------------------------------------------------|

**3** Tìm một cơ sở cho mỗi không gian trong bốn không gian con liên kết với $A$:

| $A = \begin{bmatrix} 0 & 1 & 2 & 3 & 4 \\ 0 & 1 & 2 & 4 & 6 \\ 0 & 0 & 0 & 1 & 2 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix} \begin{bmatrix} 0 & 1 & 2 & 3 & 4 \\ 0 & 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$ |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**4** Xây dựng một ma trận với tính chất được yêu cầu hoặc giải thích tại sao điều này là không thể:
(a) Không gian cột chứa $\begin{bmatrix} 1 \\ 2 \\ -3 \end{bmatrix}$ và $\begin{bmatrix} 2 \\ -3 \\ 5 \end{bmatrix}$, không gian hàng chứa $\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$ và $\begin{bmatrix} 2 \\ 3 \\ 4 \end{bmatrix}$. (Sửa lại số theo dự đoán)
(b) Không gian cột có cơ sở $\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$, không gian không có cơ sở $\begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix}$. (Sửa lại số theo dự đoán)
(c) Số chiều của không gian không = 1 + số chiều của không gian không bên trái.
(d) Không gian không chứa $\begin{bmatrix} 1 \\ 2 \\ 1 \\ 2 \end{bmatrix}$, không gian cột chứa $\begin{bmatrix} 1 \\ 2 \\ 1 \\ 2 \end{bmatrix}$. (Sửa lại số theo dự đoán)
(e) Không gian hàng = không gian cột, không gian không $\neq$ không gian không bên trái.

**5** Nếu $\mathbf{V}$ là không gian con được sinh ra bởi $(1, 1, 1)$ và $(2, 1, 0)$, tìm một ma trận $A$ có $\mathbf{V}$ là không gian hàng của nó. Tìm một ma trận $B$ có $\mathbf{V}$ là không gian không của nó. Nhân $AB$.

**6** Không sử dụng phép khử, tìm các số chiều và các cơ sở cho bốn không gian con đối với

| $A = \begin{bmatrix} 0 & 3 & 3 & 3 \\ 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 1 \end{bmatrix}$ | và | $B = \begin{bmatrix} 1 \\ 4 \\ 5 \end{bmatrix}$ |
|-------------------------------------------------------------------------------------|-----|-------------------------------------------------|
|-------------------------------------------------------------------------------------|-----|-------------------------------------------------|

**7** Giả sử ma trận $3 \times 3$ $A$ là khả nghịch. Hãy viết ra các cơ sở cho bốn không gian con đối với $A$, và cả đối với ma trận $3 \times 6$ $B = \begin{bmatrix} A & A \end{bmatrix}$. (Cơ sở cho $\mathbf{Z}$ là tập rỗng).

**8** Các số chiều của bốn không gian con đối với $A, B$, và $C$ là gì, nếu $I$ là ma trận đơn vị $3 \times 3$ và $0$ là ma trận không $3 \times 2$?

| $A = \begin{bmatrix} I & 0 \end{bmatrix}$ | và | $B = \begin{bmatrix} I & I \\ 0^T & 0^T \end{bmatrix}$ | và | $C = \begin{bmatrix} 0 \end{bmatrix}$. |
|---------------|-----|--------------------------------------------------------|-----|-------------|
|               |     |                                                        |     |             |

**9** Những không gian con nào là giống nhau đối với các ma trận có kích thước khác nhau này?

| (a) $\begin{bmatrix} A \end{bmatrix}$ và $\begin{bmatrix} A \\ A \end{bmatrix}$ | (b) $\begin{bmatrix} A \\ A \end{bmatrix}$ và $\begin{bmatrix} A & A \\ A & A \end{bmatrix}$ |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------|
|------------------------------------------------------|-----------------------------------------------------------------------------------------------|

Chứng minh rằng cả ba ma trận đó đều có *cùng hạng $r$.*

**10** Nếu các thành phần của một ma trận $3 \times 3$ được chọn ngẫu nhiên giữa 0 và 1, thì những số chiều có khả năng xảy ra nhất của bốn không gian con là bao nhiêu? Điều gì xảy ra nếu ma trận ngẫu nhiên là $3 \times 5$?

**11** (Quan trọng) $A$ là một ma trận $m \times n$ hạng $r$. Giả sử có những vế phải $b$ mà $Ax = b$ *không có nghiệm.*
(a) Tất cả các bất đẳng thức ($<$ hoặc $\leq$) phải đúng giữa $m, n$, và $r$ là gì?
(b) Làm thế nào bạn biết rằng $A^Ty = \mathbf{0}$ có các nghiệm khác $y = \mathbf{0}$?

**12** Xây dựng một ma trận có $(1, 1, 0)$ và $(0, 2, 0)$ làm cơ sở cho không gian hàng và không gian cột của nó. Tại sao đây không thể là một cơ sở cho không gian hàng và không gian không?

**13** Đúng hay sai (với một lý do hoặc một phản ví dụ):
(a) Nếu $m = n$ thì không gian hàng của $A$ bằng không gian cột.
(b) Các ma trận $A$ và $-A$ chia sẻ chung cùng bốn không gian con.
(c) Nếu $A$ và $B$ chia sẻ chung cùng bốn không gian con thì $A$ là một bội số của $B$.

**14** Không cần tính $A$, tìm các cơ sở cho bốn không gian con cơ bản của nó:

| $A = \begin{bmatrix} 1 & 0 & 0 \\ 6 & 1 & 0 \\ 9 & 8 & 1 \end{bmatrix} \begin{bmatrix} 1 & 2 & 3 & 4 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 1 & 2 \end{bmatrix}$ |
|-------------------------------------------------------------------------------------------------------------------------------------------------|
|-------------------------------------------------------------------------------------------------------------------------------------------------|

**15** Nếu bạn hoán đổi hai hàng đầu tiên của $A$, những không gian con nào trong bốn không gian con giữ nguyên? Nếu $v = (1, 2, 3, 4)$ nằm trong không gian không bên trái của $A$, hãy viết ra một vectơ trong không gian không bên trái của ma trận mới sau khi hoán đổi hàng.

**16** *Giải thích tại sao $v = (1, 0, -1)$ không thể vừa là một hàng của $A$ và vừa nằm trong không gian không.*

**17** Mô tả bốn không gian con của $\mathbf{R}^3$ liên kết với

| $A = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}$ | và | $I + A = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}$ |
|-------------------------------------------------------------------------|-----|-----------------------------------------------------------------------------|
|-------------------------------------------------------------------------|-----|-----------------------------------------------------------------------------|
(Sửa lại $I+A$ từ $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}$ thành đúng phép cộng ma trận)

**18** (Không gian không bên trái) Thêm cột thừa $b$ và rút gọn $A$ về dạng bậc thang:

| $\begin{bmatrix} A & b \end{bmatrix} = \begin{bmatrix} 2 & 3 & b_1 \\ 5 & 6 & b_2 \\ 7 & 8 & b_3 \end{bmatrix} \rightarrow \begin{bmatrix} 2 & 3 & b_1 \\ 0 & -1.5 & b_2 - 2.5b_1 \\ 0 & 0 & b_3 - 2b_2 + b_1 \end{bmatrix}$ |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
(Sửa lại phép toán khử hàng 2 và 3 cho đúng)

Một tổ hợp của các hàng của $A$ đã tạo ra hàng số không. Đó là tổ hợp nào? (Nhìn vào $b_3 - 2b_2 + b_1$ ở vế phải). Những vectơ nào nằm trong không gian không của $A^T$ và những vectơ nào nằm trong không gian không của $A$?

**19** Làm theo phương pháp của Bài tập 18, rút gọn $A$ về dạng bậc thang và tìm kiếm các hàng số không. Cột $b$ cho biết bạn đã lấy những tổ hợp nào của các hàng:

$$(a) \quad \begin{bmatrix} 1 & 2 & b_1 \\ 3 & 4 & b_2 \\ 4 & 6 & b_3 \end{bmatrix} \quad (b) \quad \begin{bmatrix} 1 & 2 & b_1 \\ 2 & 3 & b_2 \\ 2 & 4 & b_3 \\ 2 & 5 & b_4 \end{bmatrix}.$$

Từ cột $b$ sau phép khử, hãy đọc ra $m - r$ vectơ cơ sở trong không gian không bên trái. Những $y$ đó là các tổ hợp của các hàng cho ra các hàng số không ở dạng bậc thang.

**20** (a) Kiểm tra xem các nghiệm của $Ax = \mathbf{0}$ có vuông góc với các hàng của $A$ hay không:

| $A = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 0 & 3 & 1 \end{bmatrix} \begin{bmatrix} 4 & 2 & 0 & 0 \\ 0 & 0 & 1 & 3 \\ 0 & 0 & 0 & 0 \end{bmatrix} = ER.$ |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|

(b) Có bao nhiêu nghiệm độc lập đối với $A^Ty = \mathbf{0}$? Tại sao $y^T = \text{hàng 3 của } E^{-1}$?

**21** Giả sử $A$ là tổng của hai ma trận hạng một: $A = uv^T + wz^T$.
(a) Những vectơ nào sinh ra không gian cột của $A$?
(b) Những vectơ nào sinh ra không gian hàng của $A$?
(c) Hạng nhỏ hơn 2 nếu \_\_ hoặc nếu \_\_.
(d) Tính $A$ và hạng của nó nếu $u = z = (1, 0, 0)$ và $v = w = (0, 0, 1)$.

**22** Xây dựng $A = uv^T + wz^T$ có không gian cột có cơ sở là $(1, 2, 4), (2, 2, 1)$, và có không gian hàng có cơ sở là $(1, 0), (1, 1)$. Viết $A$ dưới dạng $(3 \times 2)$ nhân với $(2 \times 2)$.

**23** Không cần nhân các ma trận, tìm các cơ sở cho không gian hàng và không gian cột của $A$:

$$A = \begin{bmatrix} 1 & 2 \\ 4 & 5 \\ 2 & 7 \end{bmatrix} \begin{bmatrix} 3 & 0 & 3 \\ 1 & 1 & 2 \end{bmatrix}.$$

Làm thế nào bạn biết từ những hình dạng này rằng $A$ không thể khả nghịch?

**24** (Quan trọng) $A^Ty = d$ giải được khi $d$ nằm trong không gian con nào trong bốn không gian con? Nghiệm $y$ là duy nhất khi \_\_ chỉ chứa vectơ không.

**25** Đúng hay sai (với một lý do hoặc một phản ví dụ):
(a) $A$ và $A^T$ có cùng số lượng các phần tử xoay.
(b) $A$ và $A^T$ có cùng không gian không bên trái.
(c) Nếu không gian hàng bằng không gian cột thì $A^T = A$.
(d) Nếu $A^T = -A$ thì không gian hàng của $A$ bằng không gian cột.

**26** Nếu cho trước $a, b, c$ với $a \neq 0$, bạn sẽ chọn $d$ như thế nào để $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$ có hạng 1? Tìm một cơ sở cho không gian hàng và không gian không. Chứng minh chúng vuông góc!

**27** Tìm hạng của ma trận bàn cờ đam (checkerboard) $8 \times 8$ $B$ và ma trận bàn cờ vua (chess) $C$:

$B = \begin{bmatrix} 1 & 0 & 1 & 0 & 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 & 0 & 1 & 0 & 1 \\ 1 & 0 & 1 & 0 & 1 & 0 & 1 & 0 \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ 0 & 1 & 0 & 1 & 0 & 1 & 0 & 1 \end{bmatrix}$ và $C = \begin{bmatrix} r & n & b & q & k & b & n & r \\ p & p & p & p & p & p & p & p \\ & \text{bốn hàng số không} & \\ p & p & p & p & p & p & p & p \\ r & n & b & q & k & b & n & r \end{bmatrix}$

Các số $r, n, b, q, k, p$ đều khác nhau. Tìm các cơ sở cho không gian hàng và không gian không bên trái của $B$ và $C$. Bài toán thử thách: Tìm một cơ sở cho không gian không của $C$.

**28** Trò chơi tic-tac-toe (caro 3x3) có thể được hoàn thành (5 số một và 4 số không trong $A$) sao cho hạng$(A) = 2$ nhưng không bên nào bỏ qua nước đi chiến thắng không?

### **Thử thách (Challenge Problems)**

**29** Nếu $A = uv^T$ là một ma trận $2 \times 2$ hạng 1, hãy vẽ lại Hình 3.5 để thể hiện rõ Bốn Không Gian Con Cơ Bản. Nếu $B$ tạo ra cùng bốn không gian con đó, mối quan hệ chính xác của $B$ đối với $A$ là gì?

**30** $\mathbf{M}$ là không gian của các ma trận $3 \times 3$. Nhân mọi ma trận $X$ trong $\mathbf{M}$ với

| $A = \begin{bmatrix} 1 & 0 & -1 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix}$ | Lưu ý: $A \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$ |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|

(a) Những ma trận $X$ nào dẫn đến $AX = \text{ma trận không}$?
(b) Những ma trận nào có dạng $AX$ với một ma trận $X$ nào đó?

(a) tìm "không gian không" của phép toán $AX$ đó và (b) tìm "không gian cột". Số chiều của hai không gian con đó của $\mathbf{M}$ là bao nhiêu? Tại sao các số chiều cộng lại bằng $(n-r) + r = 9$?

**31** Giả sử các ma trận $m \times n$ $A$ và $B$ có *cùng bốn không gian con.* Nếu cả hai đều ở dạng bậc thang rút gọn theo hàng, hãy chứng minh rằng $F$ phải bằng $G$:

$$A = \begin{bmatrix} I & F \\ 0 & 0 \end{bmatrix} \quad B = \begin{bmatrix} I & G \\ 0 & 0 \end{bmatrix}.$$
