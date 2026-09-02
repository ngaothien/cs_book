# **Chương 6**

# **Trị riêng và Vectơ riêng (Eigenvalues and Eigenvectors)**

# **6.1 Giới thiệu về Trị riêng (Introduction to Eigenvalues)**

Một **vectơ riêng (eigenvector)** $x$ nằm dọc theo cùng một đường thẳng với $Ax$: $Ax = \lambda x$. **Trị riêng (eigenvalue)** là $\lambda$. Nếu $Ax = \lambda x$ thì $A^2 x = \lambda^2 x$ và $A^{-1}x = \lambda^{-1} x$ và $(A + cI)x = (\lambda + c)x$: cùng một $x$. Nếu $Ax = \lambda x$ thì $(A - \lambda I)x = \mathbf{0}$ và $A - \lambda I$ suy biến và **$\det(A - \lambda I) = 0$.** $n$ trị riêng. Kiểm tra các $\lambda$ bằng $\det A = (\lambda_1)(\lambda_2)\dots(\lambda_n)$ và tổng đường chéo $a_{11} + a_{22} + \dots + a_{nn} = \text{tổng các } \lambda$. Các phép chiếu (Projections) có $\lambda = 1$ và $0$. Phép phản xạ (Reflections) có $1$ và $-1$. Các phép quay (Rotations) có $e^{i\theta}$ và $e^{-i\theta}$: *số phức!*

Chương này bước vào một phần mới của đại số tuyến tính. Phần đầu tiên nói về $Ax = b$: sự cân bằng và trạng thái ổn định. Bây giờ phần thứ hai nói về **sự thay đổi.** Thời gian bắt đầu xuất hiện - thời gian liên tục trong một phương trình vi phân $du/dt = Au$ hoặc các bước thời gian trong một phương trình sai phân $u_{k+1} = Au_k$. Những phương trình đó KHÔNG được giải bằng phương pháp khử.

Ý tưởng cốt lõi là tránh mọi sự phức tạp do ma trận $A$ tạo ra. Giả sử vectơ nghiệm $u(t)$ luôn giữ hướng của một vectơ cố định $x$. Khi đó chúng ta chỉ cần tìm một số (thay đổi theo thời gian) nhân với $x$. Một con số thì dễ tính toán hơn là một vectơ. **Chúng ta muốn tìm các "vectơ riêng"** $x$ **không thay đổi hướng khi bạn nhân với** $A$.

Một mô hình tốt xuất phát từ các lũy thừa $A, A^2, A^3, \dots$ của một ma trận. Giả sử bạn cần tính lũy thừa bậc một trăm $A^{100}$. Các cột của nó rất gần với *vectơ riêng* $(.6, .4)$:

| $A, A^2, A^3 = \begin{bmatrix} .8 & .3 \\ .2 & .7 \end{bmatrix}$ | $\begin{bmatrix} .70 & .45 \\ .30 & .55 \end{bmatrix}$ | $\begin{bmatrix} .650 & .525 \\ .350 & .475 \end{bmatrix}$ | $A^{100} \approx \begin{bmatrix} .6000 & .6000 \\ .4000 & .4000 \end{bmatrix}$ |
|------------------------------------------------------------------|--------------------------------------------------------|------------------------------------------------------------|--------------------------------------------------------------------------------|

$A^{100}$ được tìm ra bằng cách sử dụng các *trị riêng* của $A$, chứ không phải bằng cách nhân 100 ma trận lại với nhau. Những trị riêng đó (ở đây là $\lambda = 1$ và $1/2$) là một cách thức mới để nhìn vào trung tâm của một ma trận.

Để giải thích các trị riêng, trước tiên chúng ta giải thích các vectơ riêng. Hầu hết các vectơ đều thay đổi hướng khi chúng được nhân với $A$. *Một số vectơ đặc biệt $x$ có cùng hướng với $Ax$. Đó là các "vectơ riêng".* Nhân một vectơ riêng với $A$, và vectơ $Ax$ nhận được là một con số $\lambda$ nhân với vectơ $x$ ban đầu.

#### **Phương trình cơ bản là** $Ax = \lambda x$. **Số $\lambda$ là một trị riêng của** $A$.

Trị riêng $\lambda$ cho biết vectơ đặc biệt $x$ bị kéo giãn, co lại, đảo chiều hay không thay đổi khi nó được nhân với $A$. Chúng ta có thể tìm thấy $\lambda = 2$ hoặc $1/2$ hoặc $-1$ hoặc $1$. Trị riêng $\lambda$ cũng có thể bằng không! Khi đó $Ax = 0x$ có nghĩa là vectơ riêng $x$ này nằm trong không gian null (nullspace).

Nếu $A$ là ma trận đơn vị, mọi vectơ đều thỏa mãn $Ax = x$. Tất cả các vectơ đều là vectơ riêng của $I$. Tất cả các trị riêng "lambda" đều là $\lambda = 1$. Nói một cách nhẹ nhàng thì điều này rất bất thường. Hầu hết các ma trận $2 \times 2$ có *hai* hướng vectơ riêng và *hai* trị riêng. Chúng ta sẽ chỉ ra rằng $\det(A - \lambda I) = 0$.

Phần này sẽ giải thích cách tính các $x$ và các $\lambda$. Nó có thể được đưa vào sớm trong khóa học vì chúng ta chỉ cần dùng định thức của ma trận $2 \times 2$. Hãy để tôi sử dụng $\det(A - \lambda I) = 0$ để tìm các trị riêng cho ví dụ đầu tiên này, sau đó sẽ chứng minh nó một cách đàng hoàng ở phương trình (3).

**Ví dụ 1** Ma trận $A$ có hai trị riêng $\lambda = 1$ và $\lambda = 1/2$. Hãy xem xét $\det(A - \lambda I)$:

$$\det(A - \lambda I) = \begin{vmatrix} .8 - \lambda & .3 \\ .2 & .7 - \lambda \end{vmatrix} = \lambda^2 - \frac{3}{2}\lambda + \frac{1}{2} = (\lambda - 1) \left( \lambda - \frac{1}{2} \right).$$

Tôi đã phân tích phương trình bậc hai thành $\lambda - 1$ nhân với $\lambda - 1/2$, để thấy hai trị riêng $\lambda = 1$ và $\lambda = 1/2$. Đối với những con số này, ma trận $A - \lambda I$ trở nên *suy biến* (định thức bằng không). Các vectơ riêng $x_1$ và $x_2$ nằm trong không gian null của $A - I$ và $A - \frac{1}{2}I$.

$(A - I)x_1 = \mathbf{0}$ chính là $Ax_1 = x_1$ và vectơ riêng đầu tiên là $(.6, .4)$.

$(A - \frac{1}{2}I)x_2 = \mathbf{0}$ chính là $Ax_2 = \frac{1}{2}x_2$ và vectơ riêng thứ hai là $(1, -1)$.

| $x_1 = \begin{bmatrix} .6 \\ .4 \end{bmatrix}$ | và | $Ax_1 = \begin{bmatrix} .8 & .3 \\ .2 & .7 \end{bmatrix} \begin{bmatrix} .6 \\ .4 \end{bmatrix} = x_1$ | ($Ax = x$ nghĩa là $\lambda_1 = 1$) |
|------------------------------------------------|-----|--------------------------------------------------------------------------------------------------------|-----------------------------------------|

$$x_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix} \quad \text{và} \quad Ax_2 = \begin{bmatrix} .8 & .3 \\ .2 & .7 \end{bmatrix} \begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} .5 \\ -.5 \end{bmatrix} \quad (\text{đây là } \frac{1}{2} x_2 \text{ nên } \lambda_2 = \frac{1}{2}).$$

Nếu $x_1$ lại được nhân với $A$, chúng ta vẫn nhận được $x_1$. Mọi lũy thừa của $A$ sẽ cho $A^n x_1 = x_1$. Nhân $x_2$ với $A$ sẽ cho kết quả $\frac{1}{2}x_2$, và nếu chúng ta nhân lại chúng ta sẽ nhận được $(\frac{1}{2})^2$ nhân $x_2$.

*Khi $A$ được bình phương, các vectơ riêng giữ nguyên. Các trị riêng được bình phương.*

Quy luật này tiếp tục diễn ra, vì các vectơ riêng luôn giữ nguyên hướng của riêng chúng (Hình 6.1) và không bao giờ trộn lẫn. Các vectơ riêng của $A^{100}$ vẫn là $x_1$ và $x_2$. Các trị riêng của $A^{100}$ là $1^{100} = 1$ và $(1/2)^{100} =$ một số rất nhỏ.

Các vectơ khác thì thay đổi hướng. Nhưng tất cả các vectơ khác đều là tổ hợp của hai vectơ riêng. Cột đầu tiên của $A$ là tổ hợp $x_1 + (.2)x_2$:

| Phân tách thành các vectơ riêng | $\begin{bmatrix} .8 \\ .2 \end{bmatrix} = x_1 + (.2)x_2 = \begin{bmatrix} .6 \\ .4 \end{bmatrix} + \begin{bmatrix} .2 \\ -.2 \end{bmatrix} \cdot (1)$ |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sau đó nhân với $A$       |                                                                                                                                                       |

![Sơ đồ hiển thị hai phép chiếu song song của các vectơ Ax1 và Ax2 lên các vectơ Ax và Ax2.](images/_page_300_Diagram_12.jpeg)
![Hình minh họa các phép chiếu](images/_page_300_Figure_13.jpeg)

Hình 6.1: Các vectơ riêng giữ nguyên hướng của chúng. $A^2 x = \lambda^2 x$ với $\lambda^2 = 1^2$ và $(.5)^2$.

Khi chúng ta nhân riêng cho $x_1$ và $(.2)x_2$, $A$ sẽ nhân $x_2$ với trị riêng của nó là $1/2$:

| Nhân mỗi $x_i$ với $\lambda_i$ | $A \begin{bmatrix} .8 \\ .2 \end{bmatrix}$ | là | $x_1 + \frac{1}{2}(.2)x_2 = \begin{bmatrix} .6 \\ .4 \end{bmatrix} + \begin{bmatrix} .1 \\ -.1 \end{bmatrix} = \begin{bmatrix} .7 \\ .3 \end{bmatrix}$ |
|------------------------------------|--------------------------------------------|----|--------------------------------------------------------------------------------------------------------------------------------------------------------|

*Mỗi vectơ riêng được nhân với trị riêng của nó,* khi chúng ta nhân với $A$. Tại mỗi bước $x_1$ không thay đổi và $x_2$ được nhân với $(1/2)$, do đó 99 bước sẽ cho ra số cực kỳ nhỏ $(1/2)^{99}$:

$$A^{99} \begin{bmatrix} .8 \\ .2 \end{bmatrix} \quad \text{thực chất là} \quad x_1 + (.2)\left(\frac{1}{2}\right)^{99} x_2 = \begin{bmatrix} .6 \\ .4 \end{bmatrix} + \begin{bmatrix} \text{vectơ} \\ \text{rất} \\ \text{nhỏ} \end{bmatrix}.$$

Đây là cột đầu tiên của $A^{100}$. Con số ban đầu chúng ta viết là $.6000$ không chính xác hoàn toàn. Chúng ta đã bỏ qua $(.2)(1/2)^{99}$, con số sẽ không xuất hiện trong 30 chữ số thập phân đầu tiên.

Vectơ riêng $x_1$ là một "trạng thái ổn định" không thay đổi (bởi vì $\lambda_1 = 1$). Vectơ riêng $x_2$ là một "thành phần suy giảm" gần như biến mất (bởi vì $\lambda_2 = .5$). Lũy thừa của $A$ càng cao, các cột của nó càng tiến sát tới trạng thái ổn định.

Ma trận $A$ cụ thể này là một *ma trận Markov (Markov matrix)*. Trị riêng lớn nhất của nó là $\lambda = 1$. Vectơ riêng $x_1 = (.6, .4)$ của nó là *trạng thái ổn định* - mà tất cả các cột của $A^k$ sẽ tiến gần tới. Phần 10.3 cho thấy cách các ma trận Markov xuất hiện khi bạn thực hiện tìm kiếm bằng Google.

*Đối với ma trận chiếu $P$, chúng ta có thể thấy khi nào $Px$ song song với $x$.* Các vectơ riêng cho $\lambda = 1$ và $\lambda = 0$ lần lượt lấp đầy không gian cột và không gian null. Không gian cột không di chuyển ($Px = x$). Không gian null chuyển về 0 ($Px = 0x$).

**Ví dụ 2** Ma trận chiếu 
$$P = \begin{bmatrix} .5 & .5 \\ .5 & .5 \end{bmatrix}$$
có các trị riêng $\lambda = 1$ và $\lambda = 0$.

Các vectơ riêng của nó là $x_1 = (1, 1)$ và $x_2 = (1, -1)$. Đối với các vectơ đó, $Px_1 = x_1$ (trạng thái ổn định) và $Px_2 = \mathbf{0}$ (không gian null). Ví dụ này minh họa các ma trận Markov, ma trận suy biến và (quan trọng nhất) ma trận đối xứng. Tất cả đều có các $\lambda$ và $x$ đặc biệt:

1. **1. Ma trận Markov:** Mỗi cột của $P$ có tổng bằng 1, nên $\lambda = 1$ là một trị riêng.
2. **2.** $P$ **suy biến,** nên $\lambda = 0$ là một trị riêng.
3. **3.** $P$ **đối xứng,** nên các vectơ riêng của nó $(1, 1)$ và $(1, -1)$ vuông góc với nhau.

Các trị riêng duy nhất của một ma trận chiếu là 0 và 1. Các vectơ riêng cho $\lambda = 0$ (nghĩa là $Px = 0x$) lấp đầy không gian null. Các vectơ riêng cho $\lambda = 1$ (nghĩa là $Px = x$) lấp đầy không gian cột. Không gian null được chiếu về 0. Không gian cột chiếu lên chính nó. Phép chiếu giữ lại không gian cột và phá hủy không gian null:

| Chiếu từng phần | $v = \begin{bmatrix} 1 \\ -1 \end{bmatrix} + \begin{bmatrix} 2 \\ 2 \end{bmatrix}$ | chiếu thành | $Pv = \begin{bmatrix} 0 \\ 0 \end{bmatrix} + \begin{bmatrix} 2 \\ 2 \end{bmatrix}$ |
|-------------------|------------------------------------------------------------------------------------|---------------|------------------------------------------------------------------------------------|

Các phép chiếu có $\lambda = 0$ và $1$. Các ma trận hoán vị có tất cả $|\lambda| = 1$. Ma trận tiếp theo $R$ là một ma trận phản xạ (reflection) và đồng thời là một ma trận hoán vị. $R$ cũng có các trị riêng đặc biệt.

**Ví dụ 3** Ma trận phản xạ $R = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ có trị riêng $1$ và $-1$.

Vectơ riêng $(1, 1)$ không thay đổi dưới $R$. Vectơ riêng thứ hai là $(1, -1)$ - các dấu của nó bị đảo ngược bởi $R$. Một ma trận không có phần tử âm nào vẫn có thể có một trị riêng âm! Các vectơ riêng của $R$ giống hệt của $P$, bởi vì *phản xạ = 2(phép chiếu) - I*:

| $R = 2P - I$ | $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} = 2 \begin{bmatrix} .5 & .5 \\ .5 & .5 \end{bmatrix} - \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}.$ | (2) |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-----|

*Khi một ma trận được dịch đi một lượng $I$, mỗi $\lambda$ bị thay đổi thêm 1.* Các vectơ riêng không thay đổi.

**Phương trình cho Trị riêng**

Đối với ma trận chiếu, chúng ta tìm thấy các $\lambda$ và các $x$ bằng hình học: $Px = x$ và $Px = \mathbf{0}$. Đối với các ma trận khác, chúng ta sử dụng định thức và đại số tuyến tính. *Đây là phép tính then chốt trong chương - gần như* mọi ứng dụng đều bắt đầu bằng việc giải $Ax = \lambda x$.

**Đầu tiên chuyển $\lambda x$ sang vế trái.** Viết phương trình $Ax = \lambda x$ thành $(A - \lambda I)x = \mathbf{0}$. Ma trận $A - \lambda I$ nhân vectơ riêng $x$ bằng vectơ không. *Các vectơ riêng tạo nên không gian null của $A - \lambda I$.* Khi chúng ta biết một trị riêng $\lambda$, chúng ta tìm vectơ riêng bằng cách giải $(A - \lambda I)x = \mathbf{0}$.

Trị riêng trước tiên. Nếu $(A - \lambda I)x = \mathbf{0}$ có nghiệm khác không, $A - \lambda I$ không khả nghịch. *Định thức của $A - \lambda I$ phải bằng không.* Đây là cách để nhận diện một trị riêng $\lambda$:

**Trị riêng:** Số $\lambda$ là một trị riêng của $A$ khi và chỉ khi $A - \lambda I$ suy biến.

| Phương trình cho các trị riêng | $\det(A - \lambda I) = 0.$ | (3) |
|------------------------------|----------------------------|-----|

*"Đa thức đặc trưng (characteristic polynomial)"* $\det(A - \lambda I)$ này chỉ chứa $\lambda$, không chứa $x$. Khi $A$ là $n \times n$, phương trình (3) có bậc $n$. Khi đó $A$ có $n$ trị riêng (có thể bị lặp!) Mỗi $\lambda$ dẫn đến các $x$:

**Đối với mỗi trị riêng $\lambda$, giải $(A - \lambda I)x = \mathbf{0}$ hoặc $Ax = \lambda x$ để tìm một vectơ riêng $x$.**

**Ví dụ 4** $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$ đã bị suy biến (định thức bằng không). Hãy tìm các $\lambda$ và các $x$ của nó.

Khi $A$ bị suy biến, $\lambda = 0$ là một trong các trị riêng. Phương trình $Ax = 0x$ có nghiệm. Chúng là các vectơ riêng cho $\lambda = 0$. Nhưng $\det(A - \lambda I) = 0$ là cách để tìm *tất cả* các $\lambda$ và các $x$. Luôn lấy $A$ trừ đi $\lambda I$:

| Trừ $\lambda$ trên đường chéo chính để tìm | $A - \lambda I = \begin{bmatrix} 1 - \lambda & 2 \\ 2 & 4 - \lambda \end{bmatrix}$ | (4) |
|----------------------------------------------|------------------------------------------------------------------------------------|-----|

*Lấy định thức "$ad - bc$" của ma trận $2 \times 2$ này.* Từ $1 - \lambda$ nhân $4 - \lambda$, phần "$ad$" là $\lambda^2 - 5\lambda + 4$. Phần "$bc$", không chứa $\lambda$, là $2$ nhân $2$.

$$\det \begin{bmatrix} 1 - \lambda & 2 \\ 2 & 4 - \lambda \end{bmatrix} = (1 - \lambda)(4 - \lambda) - (2)(2) = \lambda^2 - 5\lambda. \quad (5)$$

*Đặt định thức này* $\lambda^2 - 5\lambda$ *bằng 0.* Một nghiệm là $\lambda = 0$ (đúng như dự đoán, vì $A$ suy biến). Phân tích thành $\lambda$ nhân $\lambda - 5$, nghiệm còn lại là $\lambda = 5$:

| $\det(A - \lambda I) = \lambda^2 - 5\lambda = 0$ | cho ra các trị riêng | $\lambda_1 = 0$ | và | $\lambda_2 = 5$ |
|--------------------------------------------------|------------------------|-----------------|-----|-----------------|

Bây giờ tìm các vectơ riêng. Giải $(A - \lambda I)x = \mathbf{0}$ riêng lẻ cho $\lambda_1 = 0$ và $\lambda_2 = 5$:

$$(A - 0I)\mathbf{x} = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix} \begin{bmatrix} y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \text{ mang lại một vectơ riêng } \begin{bmatrix} y \\ z \end{bmatrix} = \begin{bmatrix} 2 \\ -1 \end{bmatrix} \text{ cho } \lambda_1 = 0$$

$$(A - 5I)\mathbf{x} = \begin{bmatrix} -4 & 2 \\ 2 & -1 \end{bmatrix} \begin{bmatrix} y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \text{ mang lại một vectơ riêng } \begin{bmatrix} y \\ z \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \end{bmatrix} \text{ cho } \lambda_2 = 5.$$

Các ma trận $A - 0I$ và $A - 5I$ đều bị suy biến (vì $0$ và $5$ là các trị riêng). Các vectơ riêng $(2, -1)$ và $(1, 2)$ nằm trong các không gian null: $(A - \lambda I)x = \mathbf{0}$ chính là $Ax = \lambda x$.

Chúng ta cần nhấn mạnh: *Không có gì đặc biệt về $\lambda = 0$.* Giống như mọi con số khác, $0$ có thể là một trị riêng và có thể không. Nếu $A$ suy biến, các vectơ riêng cho $\lambda = 0$ lấp đầy không gian null: $Ax = 0x = \mathbf{0}$. Nếu $A$ khả nghịch, $0$ không phải là một trị riêng. Chúng ta dịch $A$ bằng một bội số của $I$ để *làm cho nó suy biến.*

Trong ví dụ này, ma trận dịch $A - 5I$ bị suy biến và $5$ là trị riêng thứ hai.

**Tóm tắt** Để giải bài toán trị riêng cho một ma trận $n \times n$, hãy làm theo các bước sau:

1. **1.** *Tính định thức của $A - \lambda I$.* Với $\lambda$ được trừ dọc theo đường chéo chính, định thức này bắt đầu bằng $\lambda^n$ hoặc $-\lambda^n$. Nó là một đa thức của $\lambda$ bậc $n$.
2. **2.** *Tìm nghiệm của đa thức này,* bằng cách giải $\det(A - \lambda I) = 0$. Các nghiệm là $n$ trị riêng của $A$. Chúng làm cho $A - \lambda I$ suy biến.
3. **3.** Đối với mỗi trị riêng $\lambda$, *giải $(A - \lambda I)x = \mathbf{0}$ để tìm một vectơ riêng $x$.*

Một lưu ý về các vectơ riêng của ma trận $2 \times 2$. Khi $A - \lambda I$ suy biến, cả hai hàng đều là bội số của một vectơ $(a, b)$. *Vectơ riêng là bất kỳ bội số nào của $(b, -a)$.* Ví dụ trên có:

$\lambda = 0$: các hàng của $A - 0I$ theo hướng $(1, 2)$; vectơ riêng theo hướng $(2, -1)$.
$\lambda = 5$: các hàng của $A - 5I$ theo hướng $(-4, 2)$; vectơ riêng theo hướng $(2, 4)$.

Trước đó chúng ta đã viết vectơ riêng cuối cùng đó là $(1, 2)$. Cả $(1, 2)$ và $(2, 4)$ đều đúng. Có nguyên một *đường thẳng các vectơ riêng* - bất kỳ bội số khác không nào của $x$ đều tốt như $x$. Lệnh `eig(A)` của MATLAB chia cho độ dài, để làm cho vectơ riêng thành một vectơ đơn vị.

Chúng ta phải thêm một lời cảnh báo. Một số ma trận $2 \times 2$ chỉ có *một* đường thẳng các vectơ riêng. Điều này chỉ có thể xảy ra khi hai trị riêng bằng nhau. (Mặt khác, $A = I$ có các trị riêng bằng nhau và vô số vectơ riêng.) Nếu không có đủ một tập hợp các vectơ riêng, chúng ta không có một cơ sở. Chúng ta không thể viết mọi vectơ $v$ dưới dạng tổ hợp của các vectơ riêng. Theo ngôn ngữ của phần tiếp theo, *chúng ta không thể chéo hóa một ma trận mà không có $n$ vectơ riêng độc lập.*

# **Định thức và Vết (Determinant and Trace)**

Tin xấu trước: Nếu bạn cộng một hàng của $A$ vào hàng khác, hoặc đổi chỗ các hàng, các trị riêng thường thay đổi. *Phép khử không bảo toàn các $\lambda$.* Ma trận tam giác $U$ có các trị riêng *của nó* nằm dọc theo đường chéo - chúng chính là các phần tử chốt (pivots). Nhưng chúng không phải là các trị riêng của $A$! Trị riêng bị thay đổi khi hàng 1 được cộng vào hàng 2:

| $U = \begin{bmatrix} 1 & 3 \\ 0 & 0 \end{bmatrix}$ | có $\lambda = 0$ và $\lambda = 1$; | $A = \begin{bmatrix} 1 & 3 \\ 2 & 6 \end{bmatrix}$ | có $\lambda = 0$ và $\lambda = 7$. |
|----------------------------------------------------|---------------------------------------|----------------------------------------------------|---------------------------------------|

Tin tốt thứ hai: Tích $\lambda_1 \times \lambda_2$ và tổng $\lambda_1 + \lambda_2$ có thể được tìm thấy nhanh chóng từ ma trận. Đối với $A$ này, tích là 0 nhân 7. Điều đó khớp với định thức (bằng 0). Tổng các trị riêng là $0 + 7$. Điều đó khớp với tổng dọc theo đường chéo chính (**vết (trace)** là $1 + 6$). Những cách kiểm tra nhanh này luôn luôn đúng:

> *Tích của $n$ trị riêng bằng với định thức. Tổng của $n$ trị riêng bằng với tổng của $n$ phần tử trên đường chéo.*

Tổng của các phần tử dọc theo đường chéo chính được gọi là *vết (trace)* của $A$:

| $\lambda_1 + \lambda_2 + \dots + \lambda_n = \mathbf{vết (trace)} = a_{11} + a_{22} + \dots + a_{nn}$ . | (6) |
|-----------------------------------------------------------------------------------------------------|-----|

Những phép kiểm tra này rất hữu ích. Chúng được chứng minh trong các Bài tập 16-17 và một lần nữa ở phần tiếp theo. Chúng không loại bỏ sự vất vả khi tính các $\lambda$. Nhưng khi tính toán sai, chúng thường báo cho chúng ta biết. Để tính các $\lambda$ chính xác, hãy quay lại giải $\det(A - \lambda I) = 0$.

Vết và định thức *thực sự* cho biết tất cả mọi thứ khi ma trận là $2 \times 2$. Chúng ta không bao giờ muốn tính sai chúng! Ở đây vết = 3 và định thức = 2, nên các trị riêng là $\lambda = 1$ và $2$:

$$A = \begin{bmatrix} 1 & 9 \\ 0 & 2 \end{bmatrix} \quad \text{hoặc} \quad \begin{bmatrix} 3 & 1 \\ -2 & 0 \end{bmatrix} \quad \text{hoặc} \quad \begin{bmatrix} 7 & -3 \\ 10 & -4 \end{bmatrix}. \quad (7)$$

Và đây là một câu hỏi về các ma trận tốt nhất để tìm trị riêng: *ma trận tam giác.*

**Tại sao các trị riêng của một ma trận tam giác lại nằm dọc theo đường chéo của nó?**

### **Trị riêng ảo (Imaginary Eigenvalues)**

Một mẩu tin nữa (không quá tệ). Các trị riêng có thể không phải là số thực.

**Ví dụ 5** *Phép quay $90^\circ$ $Q = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ không có vectơ riêng thực nào. Các trị riêng của nó là $\lambda_1 = i$ và $\lambda_2 = -i$. Khi đó $\lambda_1 + \lambda_2 = \mathbf{vết} = 0$ và $\lambda_1\lambda_2 = \mathbf{định \ thức} = 1$.*

Sau một phép quay, *không có vectơ thực nào* $Qx$ giữ nguyên hướng giống $x$ ($x = \mathbf{0}$ là vô dụng). Không thể có vectơ riêng, trừ phi chúng ta đi tới *số ảo*. Và chúng ta sẽ làm vậy.

Để thấy $i = \sqrt{-1}$ có thể giúp ích thế nào, hãy xem xét $Q^2$ chính là $-I$. Nếu $Q$ là phép quay $90^\circ$, thì $Q^2$ là phép quay $180^\circ$. Trị riêng của nó là $-1$ và $-1$. (Chắc chắn $-Ix = -1x$). Việc bình phương $Q$ sẽ bình phương mỗi $\lambda$, vì vậy chúng ta phải có $\lambda^2 = -1$. *Các trị riêng của ma trận quay $90^\circ$ $Q$ là $i$ và $-i$, bởi vì $i^2 = -1$.*

Những $\lambda$ này được tìm ra như thông thường từ $\det(Q - \lambda I) = 0$. Phương trình này cho $\lambda^2 + 1 = 0$. Các nghiệm của nó là $i$ và $-i$. Chúng ta cũng gặp số ảo $i$ trong các vectơ riêng:

| **Các vectơ riêng phức (Complex eigenvectors)** | $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 1 \\ i \end{bmatrix} = -i \begin{bmatrix} 1 \\ i \end{bmatrix}$ | và | $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} i \\ 1 \end{bmatrix} = i \begin{bmatrix} i \\ 1 \end{bmatrix}$ |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------|-----|-------------------------------------------------------------------------------------------------------------------------------|

Bằng một cách nào đó, những vectơ phức $x_1 = (1, i)$ và $x_2 = (i, 1)$ này vẫn giữ hướng của chúng khi chúng bị quay. Đừng hỏi tôi tại sao. Ví dụ này nêu lên một điểm cực kỳ quan trọng là các ma trận thực có thể dễ dàng có các trị riêng và vectơ riêng phức. Các trị riêng cụ thể $i$ và $-i$ cũng minh họa hai thuộc tính đặc biệt của $Q$:

1. **1.** $Q$ là một ma trận trực giao (orthogonal matrix) do đó giá trị tuyệt đối của mỗi $\lambda$ là $|\lambda| = 1$.
2. **2.** $Q$ là một ma trận phản xứng (skew-symmetric matrix) do đó mỗi $\lambda$ là số ảo thuần túy.

Một ma trận đối xứng ($S^T = S$) có thể được so sánh với một số thực. Một ma trận phản xứng ($A^T = -A$) có thể được so sánh với một số ảo. Một ma trận trực giao ($Q^T Q = I$) tương ứng với một số phức có $|\lambda| = 1$. Đối với các trị riêng của $S$, $A$ và $Q$, đó không chỉ là sự tương đồng - chúng là những sự thật sẽ được chứng minh trong Phần 6.4.

Các vectơ riêng cho tất cả các ma trận đặc biệt này đều vuông góc với nhau. Bằng cách nào đó $(i, 1)$ và $(1, i)$ vuông góc với nhau (Chương 9 giải thích tích vô hướng của các vectơ phức).

### **Trị riêng của $AB$ và $A + B$**

Dự đoán đầu tiên về trị riêng của $AB$ không đúng. Trị riêng $\lambda$ của $A$ nhân với trị riêng $\beta$ của $B$ thông thường *không* mang lại một trị riêng của $AB$:

| Phép chứng minh sai | $ABx = A\beta x = \beta Ax = \beta\lambda x.$ | (8) |
|-------------|-----------------------------------------------|-----|

Dường như $\beta$ nhân $\lambda$ là một trị riêng. Khi $x$ là một vectơ riêng của cả $A$ và $B$, phép chứng minh này đúng. *Sai lầm là kỳ vọng rằng $A$ và $B$ tự động chia sẻ cùng một vectơ riêng $x$.* Thông thường thì không. Các vectơ riêng của $A$ thường không phải là các vectơ riêng của $B$. $A$ và $B$ có thể có toàn bộ các trị riêng bằng không trong khi $1$ là một trị riêng của $AB$:

| $A = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ | và | $B = \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}$ ; | khi đó | $AB = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ | và | $A + B = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ . |
|----------------------------------------------------|-----|------------------------------------------------------|------|-----------------------------------------------------|-----|----------------------------------------------------------|

Vì lý do tương tự, trị riêng của $A + B$ thông thường không phải là $\lambda + \beta$. Ở đây $\lambda + \beta = 0$ trong khi $A + B$ có các trị riêng $1$ và $-1$. (Ít nhất là chúng cộng lại bằng không.)

Phép chứng minh sai chỉ ra điều đúng đắn. Giả sử $x$ thực sự là một vectơ riêng cho cả $A$ và $B$. Khi đó chúng ta có $ABx = \lambda\beta x$ và $BAx = \lambda\beta x$. Khi chia sẻ tất cả $n$ vectơ riêng, chúng ta *có thể* nhân các trị riêng lại. Phép thử $AB = BA$ cho các vectơ riêng chia sẻ là quan trọng trong cơ học lượng tử - tạm dừng một lát để đề cập đến ứng dụng này của đại số tuyến tính:

$A$ và $B$ chia sẻ cùng $n$ vectơ riêng độc lập khi và chỉ khi $AB = BA$.

**Nguyên lý bất định Heisenberg (Heisenberg's uncertainty principle)** Trong cơ học lượng tử, ma trận vị trí $P$ và ma trận động lượng $Q$ không giao hoán. Thực tế $QP - PQ = I$ (chúng là các ma trận vô hạn). Để có $Px = \mathbf{0}$ đồng thời với $Qx = \mathbf{0}$ sẽ yêu cầu $x = Ix = \mathbf{0}$. Nếu chúng ta biết chính xác vị trí, chúng ta không thể cũng biết chính xác động lượng. Bài tập 36 dẫn xuất nguyên lý bất định Heisenberg $\|Px\| \|Qx\| \ge \frac{1}{2} \|x\|^2$.

## **■ ÔN TẬP CÁC Ý TƯỞNG CHÍNH (REVIEW OF THE KEY IDEAS) ■**

1. **1.** $Ax = \lambda x$ có nghĩa là các vectơ riêng $x$ giữ nguyên hướng khi nhân với $A$.
2. **2.** $Ax = \lambda x$ cũng có nghĩa là $\det(A - \lambda I) = 0$. Điều này xác định $n$ trị riêng.
3. **3.** Các trị riêng của $A^2$ và $A^{-1}$ là $\lambda^2$ và $\lambda^{-1}$, với cùng các vectơ riêng đó.
4. **4.** Tổng của các $\lambda$ bằng tổng dọc theo đường chéo chính của $A$ (*vết*). Tích của các $\lambda$ bằng định thức của $A$.
5. **5.** Phép chiếu $P$, phản xạ $R$, phép quay $90^\circ$ $Q$ có các trị riêng đặc biệt $1, 0, -1, i, -i$. Ma trận suy biến có $\lambda = 0$. Ma trận tam giác có các $\lambda$ trên đường chéo của chúng.
6. **6.** *Các tính chất đặc biệt của ma trận dẫn đến các trị riêng và vectơ riêng đặc biệt.* Đó là một chủ đề chính của chương này (nó được thâu tóm trong một bảng ở phần cuối cùng).

## **■ CÁC VÍ DỤ CÓ LỜI GIẢI (WORKED EXAMPLES) ■**

**6.1 A** Tìm các trị riêng và vectơ riêng của $A$ và $A^2$ và $A^{-1}$ và $A + 4I$:

$$A = \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix} \quad \text{và} \quad A^2 = \begin{bmatrix} 5 & -4 \\ -4 & 5 \end{bmatrix}.$$

Kiểm tra vết $\lambda_1 + \lambda_2 = 4$ và định thức $\lambda_1\lambda_2 = 3$.

**Lời giải** Các trị riêng của $A$ xuất phát từ $\det(A - \lambda I) = 0$:

$$A = \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix} \quad \det(A - \lambda I) = \begin{vmatrix} 2 - \lambda & -1 \\ -1 & 2 - \lambda \end{vmatrix} = \lambda^2 - 4\lambda + 3 = 0.$$

Phương trình này phân tích thành $(\lambda - 1)(\lambda - 3) = 0$ nên các trị riêng của $A$ là $\lambda_1 = 1$ và $\lambda_2 = 3$. Đối với vết, tổng $2 + 2$ khớp với $1 + 3$. Định thức $3$ khớp với tích $\lambda_1\lambda_2$.

Các vectơ riêng thu được một cách riêng lẻ bằng cách giải $(A - \lambda I)x = \mathbf{0}$, cũng chính là $Ax = \lambda x$:

$$\boldsymbol{\lambda} = \mathbf{1}: \quad (A - I)\boldsymbol{x} = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \text{ mang lại vectơ riêng } \boldsymbol{x}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$$

$$\boldsymbol{\lambda} = \mathbf{3}: \quad (A - 3I)\boldsymbol{x} = \begin{bmatrix} -1 & -1 \\ -1 & -1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \text{ mang lại vectơ riêng } \boldsymbol{x}_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$$

$A^2$ và $A^{-1}$ và $A + 4I$ giữ *nguyên các vectơ riêng giống $A$*. Các trị riêng của chúng là $\lambda^2$ và $\lambda^{-1}$ và $\lambda + 4$:

Hãy kiểm tra quy tắc này trong Ví dụ 1 nơi ma trận Markov có $\lambda = 1$ và $1/2$.

**17** Tổng của các phần tử trên đường chéo (gọi là *vết*) bằng tổng của các trị riêng:

| $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ | có | $\det(A - \lambda I) = \lambda^2 - (a+d)\lambda + ad - bc = 0.$ |
|----------------------------------------------------|-----|-----------------------------------------------------------------|

Công thức bậc hai cho các trị riêng $\lambda = (a + d + r) / 2$ và $\lambda = \_\_\_$. Tổng của chúng là \_\_\_ . Nếu $A$ có $\lambda_1 = 3$ và $\lambda_2 = 4$ thì $\det(A - \lambda I) = \_\_\_$.

**18** Nếu $A$ có $\lambda_1 = 4$ và $\lambda_2 = 5$ thì $\det(A - \lambda I) = (\lambda - 4)(\lambda - 5) = \lambda^2 - 9\lambda + 20$. Hãy tìm ba ma trận có vết $a + d = 9$, định thức $20$ và $\lambda = 4, 5$.

**19** Ma trận $3 \times 3$ $B$ được biết là có các trị riêng $0, 1, 2$. Thông tin này đủ để tìm ba điều sau (hãy đưa ra đáp án nếu có thể):
(a) hạng của $B$
(b) định thức của $B^T B$
(c) các trị riêng của $B^T B$
(d) các trị riêng của $(B^2 + I)^{-1}$.

**20** Chọn các hàng cuối cùng của $A$ và $C$ để cho các trị riêng $4, 7$ và $1, 2, 3$:

| Các ma trận đồng hành (Companion matrices) | $A = \begin{bmatrix} 0 & 1 \\ * & * \end{bmatrix}$ | $C = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ * & * & * \end{bmatrix}$ |
|--------------------|----------------------------------------------------|-------------------------------------------------------------|

**21** *Các trị riêng của $A$ bằng các trị riêng của $A^T$.* Đó là vì $\det(A - \lambda I)$ bằng $\det(A^T - \lambda I)$. Điều đó đúng bởi vì \_\_ . Hãy chỉ ra bằng một ví dụ rằng các vectơ riêng của $A$ và $A^T$ *không* giống nhau.

**22** Xây dựng bất kỳ ma trận Markov $3 \times 3$ $M$ nào: các phần tử dương dọc theo mỗi cột cộng lại bằng 1. Chứng minh rằng $M^T (1, 1, 1)^T = (1, 1, 1)^T$. Theo Bài tập 21, $\lambda = 1$ cũng là một trị riêng của $M$. Câu hỏi thử thách: Một ma trận Markov suy biến $3 \times 3$ có vết bằng $1/2$ có những trị riêng nào?

**23** Tìm ba ma trận $2 \times 2$ có $\lambda_1 = \lambda_2 = 0$. Vết bằng không và định thức bằng không. $A$ có thể không phải là ma trận không nhưng hãy kiểm tra xem $A^2 = 0$.

**24** Ma trận này suy biến với hạng 1. Hãy tìm ba trị riêng và ba vectơ riêng:

$$A = \begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix} \begin{bmatrix} 2 & 1 & 2 \end{bmatrix} = \begin{bmatrix} 2 & 1 & 2 \\ 4 & 2 & 4 \\ 2 & 1 & 2 \end{bmatrix}.$$

**25** Giả sử $A$ và $B$ có cùng các trị riêng $\lambda_1, \dots, \lambda_n$ với cùng các vectơ riêng độc lập $x_1, \dots, x_n$. Khi đó $A = B$. *Lý do:* Mọi vectơ $x$ đều là tổ hợp $c_1 x_1 + \dots + c_n x_n$. Vậy $Ax$ là gì? $Bx$ là gì?

**26** Khối $B$ có các trị riêng $1, 2$ và khối $C$ có các trị riêng $3, 4$ và khối $D$ có các trị riêng $5, 7$. Tìm các trị riêng của ma trận $4 \times 4$ $A$:

$$A = \begin{bmatrix} B & C \\ \mathbf{0} & D \end{bmatrix} = \begin{bmatrix} 0 & 1 & 3 & 0 \\ -2 & 3 & 0 & 4 \\ 0 & 0 & 6 & 1 \\ 0 & 0 & 1 & 6 \end{bmatrix}$$

**27** Tìm hạng và bốn trị riêng của $A$ và $C$:

$$A = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 \end{bmatrix} \quad \text{và} \quad C = \begin{bmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 1 \\ 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \end{bmatrix}.$$

**28** Lấy $A$ trước đó trừ đi $I$. Tìm các $\lambda$ và sau đó là các định thức của

$$B = A - I = \begin{bmatrix} 0 & 1 & 1 & 1 \\ 1 & 0 & 1 & 1 \\ 1 & 1 & 0 & 1 \\ 1 & 1 & 1 & 0 \end{bmatrix} \quad \text{và} \quad C = I - A = \begin{bmatrix} 0 & -1 & -1 & -1 \\ -1 & 0 & -1 & -1 \\ -1 & -1 & 0 & -1 \\ -1 & -1 & -1 & 0 \end{bmatrix}.$$

**29** (Ôn tập) Tìm các trị riêng của $A$, $B$, và $C$:

$$A = \begin{bmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{bmatrix} \quad \text{và} \quad B = \begin{bmatrix} 0 & 0 & 1 \\ 0 & 2 & 0 \\ 3 & 0 & 0 \end{bmatrix} \quad \text{và} \quad C = \begin{bmatrix} 2 & 2 & 2 \\ 2 & 2 & 2 \\ 2 & 2 & 2 \end{bmatrix}.$$

**30** Khi $a + b = c + d$, hãy chứng minh rằng $(1, 1)$ là một vectơ riêng và tìm cả hai trị riêng:

$$A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}.$$

**31** Nếu chúng ta đổi chỗ hàng 1 và hàng 2, cũng như cột 1 và cột 2, các trị riêng không thay đổi. Tìm các vectơ riêng của $A$ và $B$ đối với $\lambda = 11$. Hạng bằng một cho $\lambda_2 = \lambda_3 = 0$.

$$A = \begin{bmatrix} 1 & 2 & 1 \\ 3 & 6 & 3 \\ 4 & 8 & 4 \end{bmatrix} \quad \text{và} \quad B = PAP^T = \begin{bmatrix} 6 & 3 & 3 \\ 2 & 1 & 1 \\ 8 & 4 & 4 \end{bmatrix}.$$

**32** Giả sử $A$ có các trị riêng $0, 3, 5$ với các vectơ riêng độc lập $u, v, w$.
1. Đưa ra một cơ sở cho không gian null và một cơ sở cho không gian cột.
2. Tìm một nghiệm cụ thể cho $Ax = v + w$. Tìm tất cả các nghiệm.
3. $Ax = u$ không có nghiệm. Nếu nó có thì \_\_\_\_\_ sẽ nằm trong không gian cột.

### **Bài tập thử thách (Challenge Problems)**

**33** Chứng minh rằng $u$ là một vectơ riêng của ma trận $2 \times 2$ hạng một $A = uv^T$. Tìm cả hai trị riêng của $A$. Kiểm tra xem $\lambda_1 + \lambda_2$ có khớp với vết $u_1v_1 + u_2v_2$ không.

**34** Tìm các trị riêng của ma trận hoán vị $P$ này từ $\det(P - \lambda I) = 0$. Các vectơ nào không thay đổi bởi phép hoán vị này? Chúng là các vectơ riêng cho $\lambda = 1$. Bạn có thể tìm thêm ba vectơ riêng nữa không?

$$P = \begin{bmatrix} 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{bmatrix}.$$

**35** Có sáu ma trận hoán vị $3 \times 3$ $P$. Những con số nào có thể là *định thức* của $P$? Những số nào có thể là các *phần tử chốt (pivots)*? Những số nào có thể là *vết* của $P$? Bốn *con số* nào có thể là trị riêng của $P$, như trong Bài tập 15?

**36 (Nguyên lý bất định Heisenberg - Heisenberg's Uncertainty Principle)** $AB - BA = I$ có thể xảy ra cho các ma trận vô hạn với $A = A^T$ và $B = -B^T$. Khi đó

$$x^T x = x^T A B x - x^T B A x \le 2 \|Ax\| \|Bx\|.$$

Hãy giải thích bước cuối cùng bằng cách sử dụng bất đẳng thức Schwarz $|u^T v| \le \|u\| \|v\|$. Khi đó bất đẳng thức Heisenberg cho biết $\|Ax\|/\|x\|$ nhân $\|Bx\|/\|x\|$ ít nhất bằng $1/2$. Thật không thể làm cho cả sai số vị trí và sai số động lượng đều rất nhỏ.

**37** Tìm một ma trận quay $2 \times 2$ (không phải $I$) có $A^3 = I$. Các trị riêng của nó phải thỏa mãn $\lambda^3 = 1$. Chúng có thể là $e^{2\pi i/3}$ và $e^{-2\pi i/3}$. Vết và định thức là gì?

**38** (a) Tìm các trị riêng và vectơ riêng của $A$. Chúng phụ thuộc vào $c$:

$$A = \begin{bmatrix} .4 & 1-c \\ .6 & c \end{bmatrix}.$$

(b) Chứng minh rằng $A$ chỉ có một đường thẳng các vectơ riêng khi $c = 1.6$.
(c) Đây là một ma trận Markov khi $c = .8$. Khi đó $A^n$ sẽ tiến sát đến ma trận $A^\infty$ nào?

### **Eigshow trong MATLAB (Eigshow in MATLAB)**

Có một bản demo trong MATLAB (chỉ cần gõ **eigshow**), hiển thị bài toán trị riêng cho ma trận $2 \times 2$. Nó bắt đầu với vectơ đơn vị $x = (1, 0)$. *Chuột làm cho vectơ này di chuyển vòng quanh đường tròn đơn vị.* Đồng thời màn hình hiển thị $Ax$, có màu sắc và cũng đang di chuyển. Có thể $Ax$ đi trước $x$. Có thể $Ax$ đi sau $x$. *Đôi khi $Ax$ song song với $x$.*

Tại khoảnh khắc song song đó, $Ax = \lambda x$ (tại $x_1$ và $x_2$ ở hình thứ hai).

![Hình 27](images/_page_312_Figure_27.jpeg)
Đây không phải là các vectơ riêng

![Hình 29](images/_page_312_Figure_29.jpeg)
$Ax$ thẳng hàng với $x$ tại các vectơ riêng

Trị riêng $\lambda$ chính là độ dài của $Ax$, khi vectơ riêng đơn vị $x$ thẳng hàng. Các lựa chọn cài sẵn cho $A$ minh họa ba khả năng: 0, 1, hoặc 2 vectơ thực mà tại đó $Ax$ cắt qua $x$.

Các trục của hình elip là **các vectơ suy biến (singular vectors)** trong Phần 7.4—và là các vectơ riêng nếu $A^T = A$.

# **6.2 Chéo hóa ma trận (Diagonalizing a Matrix)**

1. **1.** Các cột của $AX = X\Lambda$ là $Ax_k = \lambda_k x_k$. Ma trận trị riêng $\Lambda$ là ma trận đường chéo.
2. **2.** $n$ vectơ riêng độc lập trong $X$ chéo hóa $A$: **$A = X\Lambda X^{-1}$** và **$\Lambda = X^{-1}AX$**
3. **3.** Ma trận vectơ riêng $X$ cũng chéo hóa mọi lũy thừa $A^k$: **$A^k = X\Lambda^k X^{-1}$**
4. **4.** Giải $u_{k+1} = Au_k$ bởi $u_k = A^k u_0 = X\Lambda^k X^{-1} u_0 = c_1(\lambda_1)^k x_1 + \dots + c_n(\lambda_n)^k x_n$
5. **5. Không có các trị riêng bằng nhau $\implies$** $X$ khả nghịch và $A$ có thể được chéo hóa. **Có các trị riêng bằng nhau $\implies$** $A$ *có thể* có quá ít các vectơ riêng độc lập. Khi đó $X^{-1}$ thất bại.
6. **6.** Mọi ma trận $C = B^{-1}AB$ đều có **cùng các trị riêng** giống như $A$. Những ma trận $C$ này **"đồng dạng" (similar)** với $A$.

Khi $x$ là một vectơ riêng, nhân với $A$ chỉ là nhân với một số $\lambda$: $Ax = \lambda x$. Tất cả mọi khó khăn của ma trận đều bị quét sạch. Thay vì một hệ thống kết nối qua lại, chúng ta có thể theo dõi riêng biệt từng vectơ riêng. Nó giống như việc có một *ma trận đường chéo*, không có sự kết nối ngoài đường chéo. Lũy thừa 100 của một ma trận đường chéo thì dễ dàng tính được.

Trọng tâm của phần này rất trực tiếp. *Ma trận $A$ chuyển thành một ma trận đường chéo* $\Lambda$ *khi chúng ta sử dụng các vectơ riêng đúng cách.* Đây là dạng ma trận của ý tưởng then chốt của chúng ta. Chúng ta bắt đầu ngay bằng phép tính thiết yếu đó. Trang tiếp theo sẽ giải thích tại sao $AX = X\Lambda$.

**Chéo hóa (Diagonalization)** Giả sử ma trận $n \times n$ $A$ có $n$ vectơ riêng độc lập tuyến tính $x_1, \dots, x_n$. Đặt chúng vào các cột của một *ma trận vectơ riêng $X$.* Khi đó $X^{-1}AX$ chính là *ma trận trị riêng* $\Lambda$:

Ma trận vectơ riêng $X$
Ma trận trị riêng $\Lambda$

$$X^{-1}AX = \Lambda = \begin{bmatrix} \lambda_1 & & & \\ & \lambda_2 & & \\ & & \ddots & \\ & & & \lambda_n \end{bmatrix}. \quad (1)$$

Ma trận $A$ được "chéo hóa". Chúng ta sử dụng chữ lambda viết hoa cho ma trận trị riêng, bởi vì các chữ $\lambda$ thường (các trị riêng) nằm trên đường chéo của nó.

**Ví dụ 1** $A$ này là ma trận tam giác nên các trị riêng của nó nằm trên đường chéo: $\lambda = 1$ và $\lambda = 6$.

| **Các vectơ riêng đi vào $X$** | $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$ | $\begin{bmatrix} 1 \\ 1 \end{bmatrix}$ | $\begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix}$ | $\begin{bmatrix} 1 & 5 \\ 0 & 6 \end{bmatrix}$ | $\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ | $=$ | $\begin{bmatrix} 1 & 0 \\ 0 & 6 \end{bmatrix}$ |                       |
|------------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|-----------------------|--------------------------------------------------------------------------|-----------------------|
|                                                            |                                                          |                                                          | **$X^{-1}$**                                               | **$A$**                                                    | **$X$** | **$=$**                                                    | **$\Lambda$** |

Nói cách khác $A = X\Lambda X^{-1}$. Hãy xem $A^2 = (X\Lambda X^{-1})(X\Lambda X^{-1})$. Vậy $A^2$ **chính là** $X\Lambda^2 X^{-1}$.

> *$A^2$ có cùng các vectơ riêng trong $X$ và các trị riêng được bình phương trong* $\Lambda^2$.

**Tại sao** $AX = X\Lambda$? $A$ nhân với các vectơ riêng của nó, tức là các cột của $X$. Cột đầu tiên của $AX$ là $Ax_1$. Nó bằng $\lambda_1 x_1$. Mỗi cột của $X$ được nhân với trị riêng của nó:

$$A \text{ nhân với } X \quad AX = A \begin{bmatrix} x_1 & \dots & x_n \end{bmatrix} = \begin{bmatrix} \lambda_1 x_1 & \dots & \lambda_n x_n \end{bmatrix}$$

Thủ thuật ở đây là tách ma trận $AX$ này thành $X$ nhân $\Lambda$:

$$X \text{ nhân với } \Lambda \quad \begin{bmatrix} \lambda_1 x_1 & \dots & \lambda_n x_n \end{bmatrix} = \begin{bmatrix} x_1 & \dots & x_n \end{bmatrix} \begin{bmatrix} \lambda_1 & & & \\ & \lambda_2 & & \\ & & \ddots & \\ & & & \lambda_n \end{bmatrix} = X \Lambda.$$

Hãy giữ các ma trận đó theo đúng thứ tự! Khi đó $\lambda_1$ nhân với cột đầu tiên $x_1$, như được chỉ ra. Quá trình chéo hóa đã hoàn tất, và chúng ta có thể viết $AX = X\Lambda$ theo hai cách hay:

| $AX = X\Lambda$ | tức là | $X^{-1}AX = \Lambda$ | hoặc | $A = X\Lambda X^{-1}$ | (2) |
|-----------------|----|----------------------|----|-----------------------|-----|

Ma trận $X$ có nghịch đảo, vì các cột của nó (các vectơ riêng của $A$) được giả định là độc lập tuyến tính. *Không có $n$ vectơ riêng độc lập, chúng ta không thể chéo hóa.*

$A$ và $\Lambda$ có cùng các trị riêng $\lambda_1, \dots, \lambda_n$. Các vectơ riêng thì khác nhau. Công việc của các vectơ riêng ban đầu $x_1, \dots, x_n$ là để chéo hóa $A$. Các vectơ riêng đó trong $X$ tạo ra $A = X\Lambda X^{-1}$. Bạn sẽ sớm nhận thấy sự đơn giản, tầm quan trọng và ý nghĩa của chúng. Lũy thừa bậc $k$ sẽ là $A^k = X\Lambda^k X^{-1}$ cực kỳ dễ tính:

$$A^k = (X \Lambda X^{-1})(X \Lambda X^{-1}) \dots (X \Lambda X^{-1}) = X \Lambda^k X^{-1}.$$

| **Các lũy thừa của $A$** | $\begin{bmatrix} 1 & 5 \\ 0 & 6 \end{bmatrix}^k = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 1^k & 0 \\ 0 & 6^k \end{bmatrix} \begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 6^k - 1 \\ 0 & 6^k \end{bmatrix} = A^k$ |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| $A^2$ có các trị riêng $1^2 = 1$ và $3^2 = 9$ | $A^{-1}$ có $\frac{1}{1}$ và $\frac{1}{3}$ | $A + 4I$ có $\frac{1}{3} + 4 = \frac{7}{3}$ |
|-----------------------------------------------|----------------------------------------------|----------------------------------------------|

Lưu ý cho các phần sau: $A$ có các *vectơ riêng trực giao* (Phần 6.4 về ma trận đối xứng). $A$ có thể được *chéo hóa* vì $\lambda_1 \neq \lambda_2$ (Phần 6.2). $A$ *đồng dạng* với bất kỳ ma trận $2 \times 2$ nào có trị riêng $1$ và $3$ (Phần 6.2). $A$ là một *ma trận xác định dương* (Phần 6.5) vì $A = A^T$ và các $\lambda$ đều dương.

**6.1 B** **Làm thế nào bạn có thể ước lượng các trị riêng của bất kỳ ma trận $A$ nào?** Gershgorin đã đưa ra câu trả lời này.

Mọi trị riêng của $A$ đều phải "gần" với ít nhất một trong các phần tử $a_{ii}$ trên đường chéo chính. Để $\lambda$ được coi là "gần $a_{ii}$" có nghĩa là $|a_{ii} - \lambda|$ không lớn hơn **tổng** $R_i$ **của tất cả các $|a_{ij}|$ khác trong hàng** $i$ **đó của ma trận.** Khi đó $R_i = \sum_{j \neq i} |a_{ij}|$ là bán kính của một đường tròn có tâm tại $a_{ii}$.

**Mọi $\lambda$ đều nằm trong đường tròn xung quanh một hoặc nhiều phần tử trên đường chéo** $a_{ii}$: $|a_{ii} - \lambda| \le R_i$.

Lập luận như sau. Nếu $\lambda$ là một trị riêng, thì $A - \lambda I$ không khả nghịch. Khi đó $A - \lambda I$ không thể có đường chéo trội (xem Phần 2.5). Do đó ít nhất một phần tử trên đường chéo $a_{ii} - \lambda$ *không lớn hơn* tổng $R_i$ của tất cả các phần tử còn lại $|a_{ij}|$ (chúng ta lấy giá trị tuyệt đối!) trong hàng $i$.

**Ví dụ 1.** Mọi trị riêng $\lambda$ của $A$ này rơi vào một hoặc cả hai **vòng tròn Gershgorin:** Các tâm là $a$ và $d$, bán kính là $R_1 = |b|$ và $R_2 = |c|$.

| $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ | Vòng tròn thứ nhất:  | $ |\lambda - a|  \le  |b| $ |
|----------------------------------------------------|----------------|--------------------------|
|                                                    | Vòng tròn thứ hai: | $ |\lambda - d|  \le  |c| $ |

Đó là những vòng tròn trong mặt phẳng phức, vì $\lambda$ chắc chắn có thể là số phức.

**Ví dụ 2.** Tất cả các trị riêng của $A$ này nằm trong một đường tròn bán kính $R = 3$ xung quanh *một hoặc nhiều* phần tử trên đường chéo $d_1$, $d_2$, $d_3$:

| $A = \begin{bmatrix} d_1 & 1 & 2 \\ 2 & d_2 & 1 \\ -1 & 2 & d_3 \end{bmatrix}$ | $ |\lambda - d_1|  \le 1 + 2 = R_1$<br>$ |\lambda - d_2|  \le 2 + 1 = R_2$<br>$ |\lambda - d_3|  \le 1 + 2 = R_3$ |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|

**6.1 C** Tìm các trị riêng và vectơ riêng của ma trận đối xứng $3 \times 3$ $S$ này:

| Ma trận đối xứng      |       |      |      |     |
|-----------------------|-------|------|------|-----|
| Ma trận suy biến       | $S =$ | $-1$ | $-1$ | $0$ |
| Vết $1 + 2 + 1 = 4$ |       | $0$  | $-1$ | $1$ |

**Lời giải** Vì tất cả các hàng của $S$ cộng lại bằng không, vectơ $x = (1, 1, 1)$ cho $Sx = \mathbf{0}$. Đây là một vectơ riêng cho $\lambda = 0$. Để tìm $\lambda_2$ và $\lambda_3$, tôi sẽ tính định thức $3 \times 3$:

$$
\begin{align*}
\det(S - \lambda I) &= \begin{vmatrix} 1 - \lambda & -1 & 0 \\ -1 & 2 - \lambda & -1 \\ 0 & -1 & 1 - \lambda \end{vmatrix} \\
&= (1 - \lambda)(2 - \lambda)(1 - \lambda) - (1 - \lambda) - (1 - \lambda) \\
&= (1 - \lambda)[(2 - \lambda)(1 - \lambda) - 2] \\
&= (1 - \lambda)(-\lambda)(3 - \lambda)
\end{align*}
$$

Ba nhân tử đó cho $\lambda = 0, 1, 3$. Mỗi trị riêng tương ứng với một vectơ riêng (hoặc một đường thẳng các vectơ riêng):

| $x_1 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$ | $Sx_1 = \mathbf{0}x_1$ | $x_2 = \begin{bmatrix} 1 \\ 0 \\ -1 \end{bmatrix}$ | $Sx_2 = \mathbf{1}x_2$ | $x_3 = \begin{bmatrix} 1 \\ -2 \\ 1 \end{bmatrix}$ | $Sx_3 = \mathbf{3}x_3$ |
|--------------------------------------------------------|------------------------|----------------------------------------------------|------------------------|----------------------------------------------------|------------------------|

Tôi lại nhận thấy rằng các vectơ riêng vuông góc với nhau khi $S$ đối xứng. Chúng ta đã may mắn tìm được $\lambda = 0, 1, 3$. Đối với một ma trận lớn hơn, tôi sẽ sử dụng `eig(A)` và không bao giờ đụng đến các định thức.

Lệnh đầy đủ `[X, E] = eig(A)` sẽ tạo ra các vectơ riêng đơn vị trong các cột của $X$.

# **Bài tập 6.1 (Problem Set 6.1)**

**1** Ví dụ ở đầu chương có các lũy thừa của ma trận $A$ này:

| $A = \begin{bmatrix} .70 & .45 \\ .30 & .55 \end{bmatrix}$ | và | $A^\infty = \begin{bmatrix} .6 & .6 \\ .4 & .4 \end{bmatrix}$ |
|------------------------------------------------------------|-----|---------------------------------------------------------------|

Hãy tìm các trị riêng của các ma trận này. Tất cả các lũy thừa đều có cùng các vectơ riêng.
(a) Từ $A$, chứng minh cách một phép hoán vị hàng có thể tạo ra các trị riêng khác nhau.
(b) Tại sao một trị riêng bằng không *không* bị thay đổi bởi các bước của phép khử?

**2** Tìm các trị riêng và các vectơ riêng của hai ma trận này:

| $A = \begin{bmatrix} 1 & 4 \\ 2 & 3 \end{bmatrix}$ | và | $A + I = \begin{bmatrix} 2 & 4 \\ 2 & 4 \end{bmatrix}$ |
|----------------------------------------------------|-----|--------------------------------------------------------|

$A + I$ có các vectơ riêng \_\_\_ giống $A$. Các trị riêng của nó \_\_\_ đi 1.

**3** Tính các trị riêng và vectơ riêng của $A$ và $A^{-1}$. Kiểm tra vết!

| $A = \begin{bmatrix} 0 & 2 \\ 1 & 1 \end{bmatrix}$ | và | $A^{-1} = \begin{bmatrix} -1/2 & 1 \\ 1/2 & 0 \end{bmatrix}$ |
|----------------------------------------------------|-----|--------------------------------------------------------------|

$A^{-1}$ có các vectơ riêng \_\_\_ giống $A$. Khi $A$ có các trị riêng $\lambda_1$ và $\lambda_2$, nghịch đảo của nó có các trị riêng \_\_ .

**4** Tính các trị riêng và vectơ riêng của $A$ và $A^2$:

| $A = \begin{bmatrix} -1 & 3 \\ 2 & 0 \end{bmatrix}$ | và | $A^2 = \begin{bmatrix} 7 & -3 \\ -2 & 6 \end{bmatrix}$ |
|-----------------------------------------------------|-----|--------------------------------------------------------|

$A^2$ có các \_\_\_ giống $A$. Khi $A$ có các trị riêng $\lambda_1$ và $\lambda_2$, $A^2$ có các trị riêng \_\_ . Trong ví dụ này, tại sao lại là $\lambda_1 + \lambda_2 = -1$ và $\lambda_1\lambda_2 = -6$?

**5** Tìm các trị riêng của $A$ và $B$ (dễ dàng đối với các ma trận tam giác) và $A + B$:

$$A = \begin{bmatrix} 3 & 0 \\ 1 & 1 \end{bmatrix} \quad \text{và} \quad B = \begin{bmatrix} 1 & 1 \\ 0 & 3 \end{bmatrix} \quad \text{và} \quad A + B = \begin{bmatrix} 4 & 1 \\ 1 & 4 \end{bmatrix}.$$

Các trị riêng của $A + B$ (*bằng với*)(*không bằng với*) các trị riêng của $A$ cộng với các trị riêng của $B$.

**6** Tìm các trị riêng của $A$ và $B$ và $AB$ và $BA$:

| $A = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}$ | và | $B = \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix}$ | và | $AB = \begin{bmatrix} 1 & 2 \\ 1 & 3 \end{bmatrix}$ | và | $BA = \begin{bmatrix} 3 & 2 \\ 1 & 1 \end{bmatrix}$ |
|----------------------------------------------------|-----|----------------------------------------------------|-----|-----------------------------------------------------|-----|-----------------------------------------------------|

(a) Các trị riêng của $AB$ có bằng các trị riêng của $A$ nhân với các trị riêng của $B$ không?
(b) Các trị riêng của $AB$ có bằng các trị riêng của $BA$ không?

**7** Phép khử tạo ra $A = LU$. Các trị riêng của $U$ nằm trên đường chéo của nó; chúng là các \_\_ . Các trị riêng của $L$ nằm trên đường chéo của nó; tất cả chúng đều bằng \_\_ . Các trị riêng của $A$ không giống với \_\_ .

**8** (a) Nếu bạn biết $x$ là một vectơ riêng, cách để tìm $\lambda$ là \_\_ .
(b) Nếu bạn biết $\lambda$ là một trị riêng, cách để tìm $x$ là \_\_ .

**9** Bạn làm gì với phương trình $Ax = \lambda x$, để chứng minh (a), (b), và (c)?
(a) $\lambda^2$ là một trị riêng của $A^2$, như ở Bài tập 4.
(b) $\lambda^{-1}$ là một trị riêng của $A^{-1}$, như ở Bài tập 3.
(c) $\lambda + 1$ là một trị riêng của $A + I$, như ở Bài tập 2.

**10** Tìm các trị riêng và vectơ riêng cho cả hai ma trận Markov $A$ và $A^\infty$ này. Giải thích từ các đáp án đó tại sao $A^{100}$ gần với $A^\infty$:

$$A = \begin{bmatrix} .6 & .2 \\ .4 & .2 \end{bmatrix} \quad \text{và} \quad A^\infty = \begin{bmatrix} 1/3 & 1/3 \\ 2/3 & 2/3 \end{bmatrix}.$$

**11** Đây là một sự thật kỳ lạ về ma trận $2 \times 2$ với các trị riêng $\lambda_1 \neq \lambda_2$: Các cột của $A - \lambda_1 I$ là bội số của vectơ riêng $x_2$. Có ý tưởng nào giải thích tại sao điều này lại xảy ra không?

**12** Tìm ba vectơ riêng cho ma trận $P$ này (các ma trận chiếu có $\lambda = 1$ và $0$):

| Ma trận chiếu | $P = \begin{bmatrix} .2 & .4 & .3 \\ .4 & .3 & .2 \\ .3 & .2 & .4 \end{bmatrix}$ |
|-------------------|----------------------------------------------------------------------------------|

Nếu hai vectơ riêng cùng chung một $\lambda$, thì tất cả các tổ hợp tuyến tính của chúng cũng vậy. Hãy tìm một vectơ riêng của $P$ mà không có thành phần nào bằng không.

**13** Từ vectơ đơn vị $u = (1/2, 1/2, 1/2, 1/2)$, xây dựng ma trận chiếu hạng một $P = uu^T$. Ma trận này có $P^2 = P$ bởi vì $u^T u = 1$.
(a) $Pu = u$ xuất phát từ $(uu^T)u = u(\_\_)$. Khi đó $u$ là một vectơ riêng với $\lambda = 1$.
(b) Nếu $v$ vuông góc với $u$, chứng minh rằng $Pv = \mathbf{0}$. Khi đó $\lambda = 0$.
(c) Tìm ba vectơ riêng độc lập của $P$ tất cả đều có trị riêng $\lambda = 0$.

**14** Giải $\det(Q - \lambda I) = 0$ bằng công thức bậc hai để đạt được $\lambda = \cos \theta \pm i \sin \theta$:

| $Q = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}$ | quay mặt phẳng $xy$ theo góc $\theta$. Không có $\lambda$ thực nào. |
|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------|

Tìm các vectơ riêng của $Q$ bằng cách giải $(Q - \lambda I)x = \mathbf{0}$. Sử dụng $i^2 = -1$.

**15** Mọi ma trận hoán vị đều giữ nguyên $x = (1, 1, \dots, 1)$. Khi đó $\lambda = 1$. Tìm hai $\lambda$ nữa (có thể là số phức) cho các phép hoán vị này, từ $\det(P - \lambda I) = 0$:

| $P = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{bmatrix}$ | và | $P = \begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix}$ |
|-------------------------------------------------------------------------|-----|-------------------------------------------------------------------------|

**16 Định thức của $A$ bằng tích** $\lambda_1\lambda_2\dots\lambda_n$. Bắt đầu bằng đa thức $\det(A - \lambda I)$ được tách thành $n$ nhân tử của nó (luôn luôn có thể). Sau đó đặt $\lambda = 0$:

| $\det(A - \lambda I) = (\lambda_1 - \lambda)(\lambda_2 - \lambda) \dots (\lambda_n - \lambda)$ | suy ra $\det A =$ |
|-------------------------------------------------------------------------------------------------|------------|

*Với $k = 1$ ta có $A$. Với $k = 0$ ta có $A^0 = I$ (và $\Lambda^0 = I$). Với $k = -1$ ta có $A^{-1}$.* Bạn có thể thấy $A^2 = \begin{bmatrix} 1 & 35 \\ 0 & 36 \end{bmatrix}$ khớp với công thức đó như thế nào khi $k = 2$.

Dưới đây là bốn nhận xét nhỏ trước khi chúng ta sử dụng lại $\Lambda$ trong Ví dụ 2.

**Nhận xét 1** Giả sử các trị riêng $\lambda_1, \dots, \lambda_n$ đều khác nhau. Khi đó tự động các vectơ riêng $x_1, \dots, x_n$ độc lập với nhau. Ma trận vectơ riêng $X$ sẽ *khả nghịch. Bất kỳ ma trận nào không có trị riêng lặp lại đều có thể được chéo hóa.*

**Nhận xét 2** *Chúng ta có thể nhân các vectơ riêng với bất kỳ hằng số khác không nào.* $A(cx) = \lambda(cx)$ vẫn đúng. Trong Ví dụ 1, chúng ta có thể chia $x = (1, 1)$ cho $\sqrt{2}$ để tạo ra một vectơ đơn vị.

MATLAB và hầu như tất cả các đoạn mã khác đều tạo ra các vectơ riêng có độ dài $\|x\| = 1$.

**Nhận xét 3** Các vectơ riêng trong $X$ có cùng thứ tự với các trị riêng trong $\Lambda$. Để đảo ngược thứ tự trong $\Lambda$, hãy đặt vectơ riêng $(1, 1)$ trước $(1, 0)$ trong $X$:

| Thứ tự mới $6, 1$ | $\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$ | $\begin{bmatrix} 1 & 5 \\ 0 & 6 \end{bmatrix}$ | $\begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}$ | $= \begin{bmatrix} 6 & 0 \\ 0 & 1 \end{bmatrix}$ | $= \Lambda_{\text{mới}}$ |
|----------------|-------------------------------------------------|------------------------------------------------|------------------------------------------------|--------------------------------------------------|--------------------------|

Để chéo hóa $A$ chúng ta *phải* sử dụng ma trận vectơ riêng. Từ $X^{-1}AX = \Lambda$ chúng ta biết rằng $AX = X\Lambda$. Giả sử cột đầu tiên của $X$ là $x$. Khi đó cột đầu tiên của $AX$ và $X\Lambda$ là $Ax$ và $\lambda_1 x$. Để chúng bằng nhau, $x$ phải là một vectơ riêng.

**Nhận xét 4** (cảnh báo nhắc lại đối với các trị riêng lặp lại) Một số ma trận có quá ít vectơ riêng. *Những ma trận đó không thể được chéo hóa.* Đây là hai ví dụ:

| Không thể chéo hóa | $A = \begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix}$ | và | $B = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ |
|--------------------|-----------------------------------------------------|-----|----------------------------------------------------|

Tình cờ các trị riêng của chúng là $0$ và $0$. Không có gì đặc biệt về $\lambda = 0$, vấn đề nằm ở sự lặp lại của $\lambda$. Mọi vectơ riêng của ma trận thứ nhất đều là bội số của $(1, 1)$:

| **Chỉ có một đường thẳng vectơ riêng** | $Ax = 0x$ | có nghĩa là | $\begin{bmatrix} 1 & -1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} x \\ x \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$ | và | $x = c \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ |
|--------------------------------------|-----------|-------|------------------------------------------------------------------------------------------------------------------------------|-----|----------------------------------------------|

Không có vectơ riêng thứ hai, nên ma trận $A$ bất thường này không thể được chéo hóa.

Những ma trận đó là những ví dụ tốt nhất để kiểm tra bất kỳ phát biểu nào về các vectơ riêng. Trong nhiều câu hỏi đúng/sai, ma trận không thể chéo hóa dẫn đến kết quả *sai.*

Hãy nhớ rằng không có sự kết nối nào giữa tính khả nghịch và tính chéo hóa:

*Tính khả nghịch* liên quan đến *trị riêng* ($\lambda = 0$ hoặc $\lambda \neq 0$).

*Tính chéo hóa* liên quan đến *vectơ riêng* (quá ít hoặc đủ cho $X$).

Mỗi trị riêng có ít nhất một vectơ riêng! $A - \lambda I$ bị suy biến. Nếu $(A - \lambda I)x = \mathbf{0}$ dẫn bạn đến $x = \mathbf{0}$, $\lambda$ *không phải* là một trị riêng. Hãy tìm kiếm lỗi trong việc giải **$\det(A - \lambda I) = 0$**.

**Các vectơ riêng ứng với $n$ trị riêng $\lambda$ khác nhau thì độc lập. Khi đó chúng ta có thể chéo hóa $A$.**

**$x$ độc lập từ các $\lambda$ khác nhau** Các vectơ riêng $x_1, \dots, x_j$ tương ứng với các trị riêng phân biệt (tất cả đều khác nhau) là độc lập tuyến tính. Một ma trận $n \times n$ có $n$ trị riêng khác nhau (không có các $\lambda$ lặp lại) chắc chắn có thể chéo hóa được.

*Chứng minh* Giả sử $c_1 x_1 + c_2 x_2 = \mathbf{0}$. Nhân với $A$ để tìm $c_1 \lambda_1 x_1 + c_2 \lambda_2 x_2 = \mathbf{0}$. Nhân với $\lambda_2$ để tìm $c_1 \lambda_2 x_1 + c_2 \lambda_2 x_2 = \mathbf{0}$. Bây giờ trừ hai phương trình đó cho nhau:

**Phép trừ còn lại**
$$(\lambda_1 - \lambda_2)c_1 x_1 = \mathbf{0}$$
. Do đó $c_1 = 0$.

Vì các $\lambda$ khác nhau và $x_1 \neq \mathbf{0}$, chúng ta buộc phải đi đến kết luận rằng $c_1 = 0$. Tương tự $c_2 = 0$. Chỉ có tổ hợp với $c_1 = c_2 = 0$ mới cho $c_1 x_1 + c_2 x_2 = \mathbf{0}$. Vì vậy các vectơ riêng $x_1$ và $x_2$ phải độc lập.

Phép chứng minh này mở rộng trực tiếp cho $j$ vectơ riêng. Giả sử $c_1 x_1 + \dots + c_j x_j = \mathbf{0}$. Nhân với $A$, nhân với $\lambda_j$, và trừ. Việc này sẽ nhân $x_j$ với $\lambda_j - \lambda_j = 0$, và $x_j$ biến mất. Bây giờ nhân với $A$ và nhân với $\lambda_{j-1}$ và trừ. Việc này loại bỏ $x_{j-1}$. Cuối cùng chỉ còn lại $x_1$:

Chúng ta đi đến $(\lambda_1 - \lambda_2) \dots (\lambda_1 - \lambda_j)c_1 x_1 = \mathbf{0}$ điều này bắt buộc $c_1 = 0$. (3)

Tương tự mọi $c_i = 0$. Khi các $\lambda$ đều khác nhau, các vectơ riêng là độc lập. Một tập hợp đầy đủ các vectơ riêng có thể đi vào các cột của ma trận vectơ riêng $X$.

**Ví dụ 2 (Các lũy thừa của $A$)** Ma trận Markov $A = \begin{bmatrix} .8 & .3 \\ .7 & .4 \end{bmatrix}$ trong phần trước có $\lambda_1 = 1$ và $\lambda_2 = .5$. Dưới đây là $A = X\Lambda X^{-1}$ với những trị riêng đó nằm trong đường chéo $\Lambda$:

$$\text{Ví dụ Markov} \quad \begin{bmatrix} .8 & .3 \\ .7 & .4 \end{bmatrix} = \begin{bmatrix} .6 & 1 \\ .4 & -1 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 0 & .5 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ .4 & -.6 \end{bmatrix} = X\Lambda X^{-1}.$$

Các vectơ riêng $(.6, .4)$ và $(1, -1)$ nằm trong các cột của $X$. Chúng cũng là các vectơ riêng của $A^2$. Hãy xem cách $A^2$ có cùng $X$, và *ma trận trị riêng của $A^2$ là $\Lambda^2$*:

Cùng $X$ cho $A^2$

$$A^2 = X\Lambda X^{-1}X\Lambda X^{-1} = X\Lambda^2 X^{-1}. \quad (4)$$

Chỉ cần tiếp tục, và bạn sẽ thấy lý do tại sao các lũy thừa cao $A^k$ tiếp cận một "trạng thái ổn định":

$$\text{Các lũy thừa của } A \quad A^k = X\Lambda^k X^{-1} = \begin{bmatrix} .6 & 1 \\ .4 & -1 \end{bmatrix} \begin{bmatrix} 1^k & 0 \\ 0 & (.5)^k \end{bmatrix} \begin{bmatrix} 1 & 1 \\ .4 & -.6 \end{bmatrix}.$$

Khi $k$ ngày càng lớn, $(.5)^k$ ngày càng nhỏ. Trong giới hạn nó biến mất hoàn toàn. Giới hạn đó là $A^\infty$:

$$\text{Giới hạn } k \rightarrow \infty \quad A^\infty = \begin{bmatrix} .6 & 1 \\ .4 & -1 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ .4 & -.6 \end{bmatrix} = \begin{bmatrix} .6 & .6 \\ .4 & .4 \end{bmatrix}.$$

Giới hạn có vectơ riêng $x_1$ ở cả hai cột. Chúng ta đã thấy $A^\infty$ này ở ngay trang đầu tiên của Chương 6. Bây giờ chúng ta thấy nó đến từ các lũy thừa giống như $A^{100} = X\Lambda^{100}X^{-1}$.

**Câu hỏi**
**Khi nào $A^k \rightarrow$ ma trận không?**

**Trả lời**
**Khi tất cả $|\lambda| < 1$.**

### **Ma trận đồng dạng (Similar Matrices): Cùng các trị riêng**

Giả sử ma trận trị riêng $\Lambda$ được cố định. Khi chúng ta thay đổi ma trận vectơ riêng $X$, chúng ta nhận được cả một họ ma trận $A = X\Lambda X^{-1}$ khác nhau—tất cả đều có cùng trị riêng trong $\Lambda$. Tất cả các ma trận $A$ đó (có cùng $\Lambda$) được gọi là **đồng dạng (similar)**.

Ý tưởng này mở rộng cho các ma trận không thể chéo hóa. Một lần nữa chúng ta chọn một ma trận không đổi $C$ (không nhất thiết là $\Lambda$). Và chúng ta xét toàn bộ họ ma trận $A = BCB^{-1}$, cho phép tất cả các ma trận khả nghịch $B$. Một lần nữa những ma trận $A$ và $C$ này được gọi là **đồng dạng**.

Chúng ta đang sử dụng $C$ thay vì $\Lambda$ vì $C$ có thể không phải là ma trận đường chéo. Chúng ta đang sử dụng $B$ thay vì $X$ vì các cột của $B$ có thể không phải là các vectơ riêng. Chúng ta chỉ yêu cầu rằng $B$ có nghịch đảo — các cột của nó có thể chứa bất kỳ cơ sở nào cho $\mathbf{R}^n$. Sự thật then chốt về các ma trận đồng dạng vẫn đúng. **Các ma trận đồng dạng $A$ và $C$ có cùng các trị riêng.**

### **Tất cả các ma trận $A = BCB^{-1}$ đều "đồng dạng". Tất cả chúng đều có chung các trị riêng của $C$.**

*Chứng minh* Giả sử $Cx = \lambda x$. Khi đó $BCB^{-1}$ có cùng trị riêng $\lambda$ với vectơ riêng mới $Bx$:

| **Cùng một $\lambda$** | $(BCB^{-1})(Bx) = BCx = B\lambda x = \lambda(Bx)$ . | (5) |
|--------------------------------------------------|-----------------------------------------------------|-----|

Một ma trận $C$ cố định tạo ra một họ các ma trận đồng dạng $BCB^{-1}$, cho phép tất cả các $B$. Khi $C$ là ma trận đơn vị, "họ" đó rất nhỏ. Thành viên duy nhất là $BIB^{-1} = I$. Ma trận đơn vị là ma trận có thể chéo hóa duy nhất có tất cả các trị riêng $\lambda = 1$.

Họ này lớn hơn khi $\lambda = 1$ và $1$ *với chỉ một vectơ riêng* (không thể chéo hóa). Ma trận $C$ đơn giản nhất là *dạng Jordan - sẽ được phát triển trong Phần 8.3*. Tất cả các ma trận $A$ đồng dạng đều có hai tham số $r$ và $s$, không đồng thời bằng 0: luôn có định thức bằng $1$ và vết bằng $2$.

$$C = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \implies \text{dạng Jordan cho ra } A = BCB^{-1} = \begin{bmatrix} 1 - rs & r^2 \\ -s^2 & 1 + rs \end{bmatrix}. \quad (6)$$

Đối với một ví dụ quan trọng, tôi sẽ chọn các trị riêng $\lambda = 1$ và $0$ (không lặp lại!). Bây giờ toàn bộ họ này đều có thể chéo hóa với cùng ma trận trị riêng $\Lambda$. Chúng ta có được mọi ma trận $2 \times 2$ có các trị riêng $1$ và $0$. Vết bằng $1$ và định thức bằng $0$:

| Tất cả <br>đồng dạng | $\Lambda = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ | $A = \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}$ | hoặc | $A = \begin{bmatrix} .5 & .5 \\ .5 & .5 \end{bmatrix}$ | hoặc bất kỳ $A = \frac{xy^T}{y^T x}$ |
|----------------|----------------------------------------------------------|----------------------------------------------------|----|--------------------------------------------------------|-------------------------------|

Họ này chứa tất cả các ma trận có $A^2 = A$, bao gồm $A = \Lambda$ khi $B = I$. Khi $A$ đối xứng, đây cũng là các ma trận chiếu. Các trị riêng $1$ và $0$ làm cho cuộc sống dễ dàng hơn.

#### **Dãy số Fibonacci (Fibonacci Numbers)**

Chúng tôi đưa ra một ví dụ nổi tiếng, nơi các trị riêng cho biết các số Fibonacci tăng nhanh như thế nào. *Mỗi số Fibonacci mới là tổng của hai số $F$ trước đó*:

| *Dãy số* | 0, 1, 1, 2, 3, 5, 8, 13, ... | *đến từ* | $F_{k+2} = F_{k+1} + F_k$ |
|---------------------|------------------------------|-------------------|---------------------------|

Những con số này xuất hiện trong vô số các ứng dụng tuyệt vời. Cây cối phát triển theo mô hình xoắn ốc, và một cây lê có $8$ mầm mọc ra cho mỗi $3$ vòng xoắn. Đối với một cây liễu, những con số đó có thể là $13$ và $5$. Nhà vô địch là một bông hoa hướng dương của Daniel O'Connell, có $233$ hạt trong $144$ vòng lặp. Đó là các số Fibonacci $F_{13}$ và $F_{12}$. Vấn đề của chúng ta thì cơ bản hơn.

*Bài toán: Tìm số Fibonacci $F_{100}$.* Cách chậm là áp dụng quy tắc $F_{k+2} = F_{k+1} + F_k$ từng bước một. Bằng cách cộng $F_6 = 8$ vào $F_7 = 13$ chúng ta đạt được $F_8 = 21$. Cuối cùng chúng ta đến được $F_{100}$. Đại số tuyến tính đưa ra một cách tốt hơn.

Chìa khóa là bắt đầu với một phương trình ma trận $u_{k+1} = Au_k$. Đó là một quy tắc *một bước* đối với các vectơ, trong khi Fibonacci đưa ra một quy tắc hai bước cho vô hướng. Chúng ta khớp những quy tắc đó bằng cách đưa hai số Fibonacci vào một vectơ. Sau đó bạn sẽ thấy ma trận $A$.

**Mỗi bước nhân với** $A = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}$. Sau 100 bước chúng ta đạt tới $u_{100} = A^{100}u_0$:

$$\mathbf{u}_0 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad \mathbf{u}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \quad \mathbf{u}_2 = \begin{bmatrix} 2 \\ 1 \end{bmatrix}, \quad \mathbf{u}_3 = \begin{bmatrix} 3 \\ 2 \end{bmatrix}, \quad \dots, \quad \mathbf{u}_{100} = \begin{bmatrix} F_{101} \\ F_{100} \end{bmatrix}.$$

Bài toán này hoàn toàn phù hợp với các trị riêng. Trừ $\lambda$ khỏi đường chéo của $A$:

| $A - \lambda I = \begin{bmatrix} 1-\lambda & 1 \\ 1 & -\lambda \end{bmatrix}$ | dẫn đến | $\det(A - \lambda I) = \lambda^2 - \lambda - 1.$ |
|-------------------------------------------------------------------------------|----------|--------------------------------------------------|

| Đặt $u_k = \begin{bmatrix} F_{k+1} \\ F_k \end{bmatrix}$ . Quy tắc $F_{k+2} = F_{k+1} + F_k$ chính là $u_{k+1} = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix} u_k$ . | (7) |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|

Phương trình $\lambda^2 - \lambda - 1 = 0$ được giải bằng công thức bậc hai $(-b \pm \sqrt{b^2 - 4ac}) / 2a$:

| Các trị riêng | $\lambda_1 = \frac{1 + \sqrt{5}}{2} \approx 1.618$ | và | $\lambda_2 = \frac{1 - \sqrt{5}}{2} \approx -.618.$ |
|-------------|---------------------------------------------------|----|-----------------------------------------------------|



Các trị riêng này dẫn đến các vectơ riêng $x_1 = (\lambda_1, 1)$ và $x_2 = (\lambda_2, 1)$. Bước 2 tìm tổ hợp của các vectơ riêng đó tạo ra $u_0 = (1, 0)$:

$$\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \frac{1}{\lambda_1 - \lambda_2} \left( \begin{bmatrix} \lambda_1 \\ 1 \end{bmatrix} - \begin{bmatrix} \lambda_2 \\ 1 \end{bmatrix} \right) \quad \text{hoặc} \quad u_0 = \frac{x_1 - x_2}{\lambda_1 - \lambda_2}. \quad (8)$$

Bước 3 nhân $u_0$ với $A^{100}$ để tìm $u_{100}$. Các vectơ riêng $x_1$ và $x_2$ luôn tách biệt! Chúng được nhân với $(\lambda_1)^{100}$ và $(\lambda_2)^{100}$:

| 100 bước từ $u_0$ | $u_{100} = \frac{(\lambda_1)^{100} x_1 - (\lambda_2)^{100} x_2}{\lambda_1 - \lambda_2}.$ | (9) |
|----------------------|------------------------------------------------------------------------------------------|-----|

Chúng ta muốn $F_{100} = \text{thành phần thứ hai của } u_{100}$. Thành phần thứ hai của $x_1$ và $x_2$ là $1$. Hiệu số giữa $\lambda_1 = (1 + \sqrt{5})/2$ và $\lambda_2 = (1 - \sqrt{5})/2$ là $\sqrt{5}$. Và $\lambda_2^{100} \approx 0$.

$$\text{Số Fibonacci thứ 100} = \frac{\lambda_1^{100} - \lambda_2^{100}}{\lambda_1 - \lambda_2} = \text{số nguyên gần nhất với } \frac{1}{\sqrt{5}} \left( \frac{1 + \sqrt{5}}{2} \right)^{100}. \quad (10)$$

Mọi $F_k$ đều là số nguyên. Tỷ số $F_{101} / F_{100}$ phải rất gần với tỷ số giới hạn $(1 + \sqrt{5})/2$. Người Hy Lạp gọi con số này là *"tỷ lệ vàng" (golden mean).* Vì một số lý do, một hình chữ nhật với các cạnh $1.618$ và $1$ trông đặc biệt duyên dáng.

# **Các lũy thừa của ma trận (Matrix Powers) $A^k$**

Ví dụ của Fibonacci là một phương trình sai phân điển hình $u_{k+1} = Au_k$. *Mỗi bước nhân với $A$.* Nghiệm là $u_k = A^k u_0$. Chúng ta muốn làm rõ cách chéo hóa ma trận đem lại một cách nhanh chóng để tính $A^k$ và tìm $u_k$ trong ba bước.

Ma trận vectơ riêng $X$ tạo ra $A = X\Lambda X^{-1}$. Đây là một phép phân tích ma trận, giống như $A = LU$ hay $A = QR$. Phép phân tích mới này hoàn toàn phù hợp để tính các lũy thừa, bởi vì *mỗi khi* **$X^{-1}$** *nhân với $X$ chúng ta nhận được $I$:*

| Lũy thừa của $A$ | $A^k u_0 = (X \Lambda X^{-1}) \dots (X \Lambda X^{-1}) u_0 = X \Lambda^k X^{-1} u_0$ |
|---------------|---------------------------------------------------------------------------------------|

Tôi sẽ tách $X \Lambda^k X^{-1} u_0$ thành ba bước cho thấy các trị riêng hoạt động như thế nào:

1. **1.** Viết $u_0$ dưới dạng một tổ hợp $c_1 x_1 + \dots + c_n x_n$ của các vectơ riêng. Khi đó $c = X^{-1}u_0$.
2. **2.** Nhân mỗi vectơ riêng $x_i$ với $(\lambda_i)^k$. Bây giờ chúng ta có $\Lambda^k X^{-1} u_0$.
3. **3.** Cộng các phần $c_i (\lambda_i)^k x_i$ lại với nhau để tìm nghiệm $u_k = A^k u_0$. Đây chính là $X\Lambda^k X^{-1} u_0$.

| Nghiệm cho $u_{k+1} = Au_k$ | $u_k = A^k u_0 = c_1(\lambda_1)^k x_1 + \dots + c_n(\lambda_n)^k x_n$ | (11) |
|-------------------------------|------------------------------------------------------------------------|------|

Trong ngôn ngữ ma trận, $A^k$ bằng $(X\Lambda X^{-1})^k$, cũng chính là $X$ nhân $\Lambda^k$ nhân $X^{-1}$. Ở Bước 1, các vectơ riêng trong $X$ dẫn đến các $c$ trong tổ hợp $u_0 = c_1 x_1 + \dots + c_n x_n$:

**Bước 1**
$$u_0 = \begin{bmatrix} x_1 & \dots & x_n \end{bmatrix} \begin{bmatrix} c_1 \\ \vdots \\ c_n \end{bmatrix}$$
. Điều này có nghĩa là $u_0 = Xc$. (12)

Các hệ số trong Bước 1 là $c = X^{-1}u_0$. Sau đó Bước 2 nhân với $\Lambda^k$. Kết quả cuối cùng $u_k = \sum c_i(\lambda_i)^k x_i$ ở Bước 3 là tích của $X$ và $\Lambda^k$ và $X^{-1}u_0$:

$$A^k \mathbf{u}_0 = X \Lambda^k X^{-1} \mathbf{u}_0 = X \Lambda^k \mathbf{c} = \begin{bmatrix} x_1 & \dots & x_n \end{bmatrix} \begin{bmatrix} (\lambda_1)^k & & \\ & \ddots & \\ & & (\lambda_n)^k \end{bmatrix} \begin{bmatrix} c_1 \\ \vdots \\ c_n \end{bmatrix}. \quad (13)$$

Kết quả này chính xác là $u_k = c_1(\lambda_1)^k x_1 + \dots + c_n(\lambda_n)^k x_n$. Nó giải quyết được $u_{k+1} = Au_k$.

**Ví dụ 3** Bắt đầu từ $u_0 = (1, 0)$. Tính $A^k u_0$ cho ma trận Fibonacci nhanh hơn này:

$$A = \begin{bmatrix} 1 & 2 \\ 1 & 0 \end{bmatrix} \quad \text{có} \quad \lambda_1 = 2 \quad \text{và} \quad x_1 = \begin{bmatrix} 2 \\ 1 \end{bmatrix}, \quad \lambda_2 = -1 \quad \text{và} \quad x_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}.$$

Ma trận này giống như Fibonacci ngoại trừ quy tắc được đổi thành $F_{k+2} = F_{k+1} + 2F_k$. Những số mới bắt đầu bằng $0, 1, 1, 3$. Chúng tăng nhanh hơn vì $\lambda = 2$.

Tìm $u_k = A^k u_0$ trong 3 bước $u_0 = c_1 x_1 + c_2 x_2$ và $u_k = c_1(\lambda_1)^k x_1 + c_2(\lambda_2)^k x_2$

**Bước 1** $u_0 = \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \frac{1}{3} \begin{bmatrix} 2 \\ 1 \end{bmatrix} + \frac{1}{3} \begin{bmatrix} 1 \\ -1 \end{bmatrix}$ nên $c_1 = c_2 = \frac{1}{3}$

**Bước 2** Nhân hai phần với $(\lambda_1)^k = 2^k$ và $(\lambda_2)^k = (-1)^k$

**Bước 3** Kết hợp các vectơ riêng $c_1(\lambda_1)^k x_1$ và $c_2(\lambda_2)^k x_2$ thành $u_k$:

$$u_k = A^k u_0 \quad u_k = \frac{1}{3} 2^k \begin{bmatrix} 2 \\ 1 \end{bmatrix} + \frac{1}{3} (-1)^k \begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} F_{k+1} \\ F_k \end{bmatrix}.$$

Con số mới là $F_k = (2^k - (-1)^k)/3$. Sau $0, 1, 1, 3$ là $F_4 = 15/3 = 5$.

Đằng sau những ví dụ số này ẩn chứa một ý tưởng cơ bản: **Hãy đi theo các vectơ riêng.** Trong Phần 6.3, đây là mối liên kết mang tính sống còn từ đại số tuyến tính đến phương trình vi phân ($\lambda^k$ sẽ trở thành $e^{\lambda t}$). Chương 8 sẽ chứng kiến ý tưởng tương tự như việc "biến đổi sang một cơ sở vectơ riêng". Ví dụ tốt nhất là một **chuỗi Fourier**, được xây dựng từ các vectơ riêng $e^{ikx}$ của $d/dx$.

## **Ma trận không thể chéo hóa (Nondiagonalizable Matrices) (Tùy chọn)**

Giả sử $\lambda$ là một trị riêng của $A$. Chúng ta khám phá ra sự thật đó theo hai cách:

1. **1. Vectơ riêng (hình học)** Có những nghiệm khác không đối với $Ax = \lambda x$.
2. **2. Trị riêng (đại số)** Định thức của $A - \lambda I$ bằng không.

Con số $\lambda$ có thể là một trị riêng đơn (simple eigenvalue) hoặc một trị riêng bội (multiple eigenvalue), và chúng muốn biết **bội số (multiplicity)** của nó. Hầu hết các trị riêng có bội số $M = 1$ (các trị riêng đơn). Khi đó chỉ có một đường thẳng vectơ riêng, và $\det(A - \lambda I)$ không có nhân tử kép.

Đối với các ma trận ngoại lệ, một trị riêng có thể bị **lặp lại (repeated)**. Khi đó có hai cách khác nhau để đếm bội số của nó. Luôn luôn có $\text{GM} \le \text{AM}$ đối với mỗi $\lambda$:

1. **1. (Bội số hình học = Geometric Multiplicity = GM)** Đếm số lượng **các vectơ riêng độc lập** ứng với $\lambda$. Khi đó GM là số chiều của không gian null của $A - \lambda I$.
2. **2. (Bội số đại số = Algebraic Multiplicity = AM)** AM đếm **số lần lặp lại của $\lambda$** trong số các trị riêng. Hãy xem xét $n$ nghiệm của $\det(A - \lambda I) = 0$.

Nếu $A$ có $\lambda = 4, 4, 4$, thì trị riêng đó có $\text{AM} = 3$ và $\text{GM} = 1, 2$, hoặc $3$.

Ma trận $A$ sau đây là ví dụ tiêu chuẩn về vấn đề rắc rối này. Trị riêng của nó $\lambda = 0$ bị lặp lại. Nó là một trị riêng kép ($\text{AM} = 2$) với chỉ một vectơ riêng ($\text{GM} = 1$).

$$\text{AM} = 2 \quad A = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} \text{ có } \det(A - \lambda I) = \begin{vmatrix} -\lambda & 1 \\ 0 & -\lambda \end{vmatrix} = \lambda^2. \quad \lambda = 0, 0 \text{ nhưng } 1 \text{ vectơ riêng}$$

"Đáng lẽ" phải có hai vectơ riêng, vì $\lambda^2 = 0$ có nghiệm kép. Nhân tử kép $\lambda^2$ làm cho $\text{AM} = 2$. Nhưng chỉ có duy nhất một vectơ riêng $x = (1, 0)$ và $\text{GM} = 1$. *Sự thiếu hụt các vectơ riêng này khi $\text{GM}$ nhỏ hơn $\text{AM}$ có nghĩa là $A$ không thể được chéo hóa.*

Ba ma trận sau đây đều có cùng sự thiếu hụt các vectơ riêng. Trị riêng lặp lại của chúng là $\lambda = 5$. Các vết là $10$ và các định thức là $25$:

| $A = \begin{bmatrix} 5 & 1 \\ 0 & 5 \end{bmatrix}$ | và | $A = \begin{bmatrix} 6 & -1 \\ 1 & 4 \end{bmatrix}$ | và | $A = \begin{bmatrix} 7 & 2 \\ -2 & 3 \end{bmatrix}$ |
|----------------------------------------------------|-----|-----------------------------------------------------|-----|-----------------------------------------------------|

Tất cả các ma trận này đều có $\det(A - \lambda I) = (\lambda - 5)^2$. Bội số đại số là $\text{AM} = 2$. Nhưng mỗi ma trận $A - 5I$ có hạng $r = 1$. Bội số hình học là $\text{GM} = 1$. Chỉ có một đường thẳng các vectơ riêng cho $\lambda = 5$, và các ma trận này không thể chéo hóa được.

#### **■ ÔN TẬP CÁC Ý TƯỞNG CHÍNH (REVIEW OF THE KEY IDEAS) ■**

1. **1.** Nếu $A$ có $n$ vectơ riêng độc lập $x_1, \dots, x_n$, chúng sẽ đi vào các cột của $X$.

| $A$ được chéo hóa bởi $X$ | $X^{-1}AX = \Lambda$ | và | $A = X\Lambda X^{-1}$ |
|----------------------------|----------------------|-----------|-----------------------|

2. **2.** Các lũy thừa của $A$ là $A^k = X\Lambda^k X^{-1}$. Các vectơ riêng trong $X$ không thay đổi.
3. **3.** Các trị riêng của $A^k$ là $(\lambda_1)^k, \dots, (\lambda_n)^k$ trong ma trận $\Lambda^k$.
4. **4.** Nghiệm cho $u_{k+1} = Au_k$ bắt đầu từ $u_0$ là $u_k = A^k u_0 = X\Lambda^k X^{-1} u_0$:

| $u_k = c_1(\lambda_1)^k x_1 + \dots + c_n(\lambda_n)^k x_n$ | với điều kiện | $u_0 = c_1 x_1 + \dots + c_n x_n$ |
|--------------------------------------------------------------|----------|------------------------------------|

Điều này cho thấy các Bước 1, 2, 3 (các $c$ lấy từ $X^{-1}u_0$, $\lambda^k$ lấy từ $\Lambda^k$, và $x$ lấy từ $X$)

5. **5.** $A$ có thể được chéo hóa nếu mọi trị riêng đều có đủ các vectơ riêng ($\text{GM} = \text{AM}$).

#### **■ CÁC VÍ DỤ CÓ LỜI GIẢI (WORKED EXAMPLES) ■**

**6.2 A** **Dãy số Lucas (Lucas numbers)** giống hệt dãy số Fibonacci ngoại trừ chúng bắt đầu bằng $L_1 = 1$ và $L_2 = 3$. Sử dụng cùng quy tắc $L_{k+2} = L_{k+1} + L_k$, các số Lucas tiếp theo là $4, 7, 11, 18$. Hãy chứng minh rằng số Lucas $L_{100}$ là $\lambda_1^{100} + \lambda_2^{100}$.

**Lời giải** $u_{k+1} = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix} u_k$ giống hệt đối với Fibonacci, bởi vì $L_{k+2} = L_{k+1} + L_k$ là cùng một quy tắc (với các giá trị khởi đầu khác nhau). Phương trình trở thành một hệ $2 \times 2$:

$$\text{Đặt } u_k = \begin{bmatrix} L_{k+1} \\ L_k \end{bmatrix}. \quad \text{Quy tắc } L_{k+2} = L_{k+1} + L_k \quad \text{chính là } u_{k+1} = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix} u_k.$$

Các trị riêng và vectơ riêng của $A = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}$ vẫn bắt nguồn từ $\lambda^2 = \lambda + 1$:

$$\lambda_1 = \frac{1 + \sqrt{5}}{2} \quad \text{và} \quad x_1 = \begin{bmatrix} \lambda_1 \\ 1 \end{bmatrix} \quad \lambda_2 = \frac{1 - \sqrt{5}}{2} \quad \text{và} \quad x_2 = \begin{bmatrix} \lambda_2 \\ 1 \end{bmatrix}.$$

Bây giờ giải $c_1 x_1 + c_2 x_2 = u_1 = (3, 1)$. Nghiệm là $c_1 = \lambda_1$ và $c_2 = \lambda_2$. Kiểm tra:

$$\lambda_1 x_1 + \lambda_2 x_2 = \begin{bmatrix} \lambda_1^2 + \lambda_2^2 \\ \lambda_1 + \lambda_2 \end{bmatrix} = \begin{bmatrix} \text{vết của } A^2 \\ \text{vết của } A \end{bmatrix} = \begin{bmatrix} 3 \\ 1 \end{bmatrix} = u_1$$

$u_{100} = A^{99} u_1$ cho chúng ta biết các số Lucas $(L_{101}, L_{100})$. Các thành phần thứ hai của các vectơ riêng $x_1$ và $x_2$ là $1$, do đó thành phần thứ hai của $u_{100}$ là đáp án chúng ta muốn:

$$\text{Số Lucas} \quad L_{100} = c_1 \lambda_1^{99} + c_2 \lambda_2^{99} = \lambda_1^{100} + \lambda_2^{100}.$$

Dãy Lucas khởi đầu nhanh hơn dãy Fibonacci, và kết thúc lớn hơn một hệ số gần bằng $\sqrt{5}$.

**6.2 B** Tìm ma trận nghịch đảo và các trị riêng cũng như định thức của ma trận $A$ này:

$$A = 5 * \text{eye}(4) - \text{ones}(4) = \begin{bmatrix} 4 & -1 & -1 & -1 \\ -1 & 4 & -1 & -1 \\ -1 & -1 & 4 & -1 \\ -1 & -1 & -1 & 4 \end{bmatrix}.$$

Hãy mô tả một ma trận vectơ riêng $X$ mang lại $X^{-1} A X = \Lambda$.

**Lời giải** Các trị riêng của ma trận toàn số 1 (all-ones matrix) là gì? Hạng của nó chắc chắn bằng $1$, nên ba trị riêng là $\lambda = 0, 0, 0$. Vết của nó bằng $4$, nên trị riêng còn lại là $\lambda = 4$. Lấy $5I$ trừ đi ma trận toàn số 1 này để nhận được ma trận $A$ của chúng ta:




**Trừ các trị riêng 4, 0, 0 khỏi 5, 5, 5, 5. Các trị riêng của $A$ là 1, 5, 5, 5.**

Định thức của $A$ là 125, tích của bốn trị riêng đó. Vectơ riêng cho $\lambda = 1$ là $x = (1, 1, 1, 1)$ hoặc $(c, c, c, c)$. Các vectơ riêng khác vuông góc với $x$ (vì $A$ đối xứng). Ma trận vectơ riêng $X$ đẹp nhất là ma trận Hadamard trực giao đối xứng $H$. Hệ số $\frac{1}{2}$ tạo ra các vectơ cột đơn vị.

$$\text{Các vectơ riêng trực chuẩn} \quad X = H = \frac{1}{2} \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & -1 & 1 & -1 \\ 1 & 1 & -1 & -1 \\ 1 & -1 & -1 & 1 \end{bmatrix} = H^T = H^{-1}.$$

Các trị riêng của $A^{-1}$ là $1, \frac{1}{5}, \frac{1}{5}, \frac{1}{5}$. Các vectơ riêng không thay đổi nên $A^{-1} = H\Lambda^{-1}H^{-1}$. Ma trận nghịch đảo gọn gàng một cách đáng ngạc nhiên:

$$A^{-1} = \frac{1}{5} * (\mathbf{eye}(4) + \mathbf{ones}(4)) = \frac{1}{5} \begin{bmatrix} 2 & 1 & 1 & 1 \\ 1 & 2 & 1 & 1 \\ 1 & 1 & 2 & 1 \\ 1 & 1 & 1 & 2 \end{bmatrix}$$

$A$ là sự thay đổi hạng-1 (rank-one change) từ $5I$. Vì vậy $A^{-1}$ là sự thay đổi hạng-1 từ $I/5$.

Trong một đồ thị có 5 nút, định thức 125 đếm số lượng "cây khung" (spanning trees - những cây chạm đến tất cả các nút). *Cây không có chu trình (loops)* (đồ thị và cây nằm trong Phần 10.1).

Với 6 nút, ma trận $6 * \text{eye}(5) - \text{ones}(5)$ có 5 trị riêng $1, 6, 6, 6, 6$.

### **Bài tập 6.2 (Problem Set 6.2)**

**Các câu hỏi từ 1-7 nói về các ma trận trị riêng và vectơ riêng $A$ và $X$.**

**1** (a) Phân tích hai ma trận này thành $A = X\Lambda X^{-1}$:

$$A = \begin{bmatrix} 1 & 2 \\ 0 & 3 \end{bmatrix} \quad \text{và} \quad A = \begin{bmatrix} 1 & 1 \\ 3 & 3 \end{bmatrix}.$$

(b) Nếu
$$A = X\Lambda X^{-1}$$
 thì $A^3 = X\Lambda^3 X^{-1}$ và $A^{-1} = X\Lambda^{-1} X^{-1}$.

**2** Nếu $A$ có $\lambda_1 = 2$ với vectơ riêng $x_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ và $\lambda_2 = 5$ với $x_2 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$, sử dụng $X\Lambda X^{-1}$ để tìm $A$. Không có ma trận nào khác có cùng các $\lambda$ và $x$.
**3** Giả sử $A = X\Lambda X^{-1}$. Ma trận trị riêng của $A + 2I$ là gì? Ma trận vectơ riêng là gì? Kiểm tra xem $A + 2I = X(\Lambda + 2I)X^{-1}$.
**4** Đúng hay sai: Nếu các cột của $X$ (các vectơ riêng của $A$) độc lập tuyến tính, thì
  - (a) $A$ khả nghịch (b) $A$ có thể chéo hóa
  - (c) $X$ khả nghịch (d) $X$ có thể chéo hóa.
**5** Nếu các vectơ riêng của $A$ là các cột của $I$, thì $A$ là ma trận \_\_. Nếu ma trận vectơ riêng $X$ là tam giác, thì $X^{-1}$ là tam giác. Hãy chứng minh rằng $A$ cũng là ma trận tam giác.
**6** Mô tả tất cả các ma trận $X$ làm chéo hóa ma trận $A$ này (tìm tất cả các vectơ riêng):

$$A = \begin{bmatrix} 4 & 0 \\ 1 & 2 \end{bmatrix}.$$

Sau đó mô tả tất cả các ma trận làm chéo hóa $A^{-1}$.
**7** Viết ra ma trận tổng quát nhất có các vectơ riêng $\begin{bmatrix} 1 \\ 1 \end{bmatrix}$ và $\begin{bmatrix} 1 \\ -1 \end{bmatrix}$.

### Các câu hỏi từ 8-10 nói về số Fibonacci và số Gibonacci.

**8** Chéo hóa ma trận Fibonacci bằng cách hoàn thành $X^{-1}$:

$$\begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} \lambda_1 & \lambda_2 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{bmatrix} \begin{bmatrix} \dots & \dots \\ \dots & \dots \end{bmatrix}$$

Thực hiện phép nhân $X\Lambda^k X^{-1} \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ để tìm thành phần thứ hai của nó. Đây là số Fibonacci thứ $k$: $F_k = (\lambda_1^k - \lambda_2^k) / (\lambda_1 - \lambda_2)$.

**9** Giả sử $G_{k+2}$ là *trung bình* của hai số trước đó $G_{k+1}$ và $G_k$:

| $G_{k+2} = \frac{1}{2}G_{k+1} + \frac{1}{2}G_k$ | hay | $\begin{bmatrix} G_{k+2} \\ G_{k+1} \end{bmatrix} = \begin{bmatrix} A \end{bmatrix} \begin{bmatrix} G_{k+1} \\ G_k \end{bmatrix}$ |
|-------------------------------------------------|----|-----------------------------------------------------------------------------------------------------------------------------------|
| $G_{k+1} = G_{k+1}$                             |    |                                                                                                                                   |

  - (a) Tìm các trị riêng và vectơ riêng của $A$.
  - (b) Tìm giới hạn khi $n \to \infty$ của các ma trận $A^n = X\Lambda^n X^{-1}$.
  - (c) Nếu $G_0 = 0$ và $G_1 = 1$, chứng minh rằng các số Gibonacci tiến tới \_\_.

**10** Chứng minh rằng cứ mỗi ba số Fibonacci trong $0, 1, 1, 2, 3, \dots$ thì có một số chẵn.

#### Các câu hỏi 11-14 nói về khả năng chéo hóa.

**11** Đúng hay sai: Nếu các trị riêng của $A$ là $2, 2, 5$ thì ma trận chắc chắn
  - (a) khả nghịch (b) có thể chéo hóa (c) không thể chéo hóa.
**12** Đúng hay sai: Nếu các vectơ riêng duy nhất của $A$ là các bội số của $(1, 4)$ thì $A$ có
  - (a) không có nghịch đảo (b) một trị riêng lặp lại (c) không có phép chéo hóa $X\Lambda X^{-1}$.
**13** Hoàn thành các ma trận này để $\det A = 25$. Sau đó kiểm tra xem $\lambda = 5$ có lặp lại không vì vết là $10$ nên định thức của $A - \lambda I$ là $(\lambda - 5)^2$. Tìm một vectơ riêng thỏa mãn $Ax = 5x$. Các ma trận này sẽ không thể chéo hóa được vì không có đường thẳng vectơ riêng thứ hai.

| $A = \begin{bmatrix} 8 & \dots \\ \dots & 2 \end{bmatrix}$ | và | $A = \begin{bmatrix} 9 & 4 \\ \dots & 1 \end{bmatrix}$ | và | $A = \begin{bmatrix} 10 & 5 \\ -5 & \dots \end{bmatrix}$ |
|-------------------------------------------|-----|----------------------------------------------------|-----|------------------------------------------------------|

**14** Ma trận $A = \begin{bmatrix} 3 & 1 \\ 0 & 3 \end{bmatrix}$ không thể chéo hóa vì hạng của $A - 3I$ bằng $1$. Hãy thay đổi một phần tử để làm cho $A$ có thể chéo hóa. Bạn có thể thay đổi những phần tử nào?

#### Các câu hỏi 15-19 nói về lũy thừa của ma trận.

**15** $A^k = X\Lambda^k X^{-1}$ tiến tới ma trận không khi $k \to \infty$ nếu và chỉ nếu mọi $\lambda$ đều có giá trị tuyệt đối nhỏ hơn 1. Ma trận nào trong số các ma trận này có $A^k \to 0$?

| $A_1 = \begin{bmatrix} .6 & .9 \\ .4 & .7 \end{bmatrix}$ | và | $A_2 = \begin{bmatrix} .6 & .9 \\ .1 & .6 \end{bmatrix}$ |
|----------------------------------------------------------|-----|----------------------------------------------------------|

**16** (Khuyên làm) Tìm $\Lambda$ và $X$ để chéo hóa $A_1$ trong Bài 15. Giới hạn của $A^k$ khi $k \to \infty$ là gì? Giới hạn của $X\Lambda^k X^{-1}$ là gì? Trong các cột của ma trận giới hạn này, bạn sẽ thấy \_\_.
**17** Tìm $\Lambda$ và $X$ để chéo hóa $A_2$ trong Bài 15. $(A_2)^{10} u_0$ bằng bao nhiêu đối với những $u_0$ này?

$$u_0 = \begin{bmatrix} 3 \\ 1 \end{bmatrix} \quad \text{và} \quad u_0 = \begin{bmatrix} 3 \\ -1 \end{bmatrix} \quad \text{và} \quad u_0 = \begin{bmatrix} 6 \\ 0 \end{bmatrix}.$$

**18** Chéo hóa $A$ và tính $X\Lambda^k X^{-1}$ để chứng minh công thức này cho $A^k$:

| $A = \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}$ | có | $A^k = \frac{1}{2} \begin{bmatrix} 1+3^k & 1-3^k \\ 1-3^k & 1+3^k \end{bmatrix}$ |
|------------------------------------------------------|-----|----------------------------------------------------------------------------------|

**19** Chéo hóa $B$ và tính $X\Lambda^k X^{-1}$ để chứng minh công thức này cho $B^k$:

| $B = \begin{bmatrix} 5 & 1 \\ 0 & 4 \end{bmatrix}$ | có | $B^k = \begin{bmatrix} 5^k & 5^k - 4^k \\ 0 & 4^k \end{bmatrix}$ |
|----------------------------------------------------|-----|------------------------------------------------------------------|

**20** Giả sử $A = X\Lambda X^{-1}$. Lấy định thức để chứng minh $\det A = \det \Lambda = \lambda_1\lambda_2 \dots \lambda_n$. Phép chứng minh nhanh này chỉ hoạt động khi $A$ có thể \_\_.
**21** Hãy chứng minh rằng vết $XY =$ vết $YX$, bằng cách cộng các phần tử trên đường chéo của $XY$ và $YX$:

| $X = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ | và | $Y = \begin{bmatrix} q & r \\ s & t \end{bmatrix}$ |
|----------------------------------------------------|-----|----------------------------------------------------|

Bây giờ hãy chọn $Y$ là $\Lambda X^{-1}$. Khi đó $X\Lambda X^{-1}$ có cùng vết với $\Lambda X^{-1}X = \Lambda$. Điều này chứng minh rằng *vết của $A$ bằng vết của $\Lambda$ = tổng các trị riêng.*

**22** $AB - BA = I$ là không thể vì vế trái có vết = 0 trong khi vế phải có vết = $n$. Nhưng hãy tìm một

$$AB - BA = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$$
 có vết bằng không.

**23** Nếu $A = X\Lambda X^{-1}$, hãy chéo hóa ma trận khối $B = \begin{bmatrix} A & 0 \\ 0 & 2A \end{bmatrix}$. Tìm các ma trận trị riêng và vectơ riêng (khối) của nó.
**24** Hãy xét tất cả các ma trận $A$ kích thước $4 \times 4$ được chéo hóa bởi cùng một ma trận vectơ riêng $X$ cố định. Chứng minh rằng các ma trận $A$ này tạo thành một không gian con ($cA$ và $A_1 + A_2$ có cùng $X$ này). Không gian con này là gì khi $X = I$? Số chiều của nó là bao nhiêu?
**25** Giả sử $A^2 = A$. Ở vế trái $A$ nhân với mỗi cột của $A$. Không gian con nào trong bốn không gian con của chúng ta chứa các vectơ riêng với $\lambda = 1$? Không gian con nào chứa các vectơ riêng với $\lambda = 0$? Từ số chiều của các không gian con đó, $A$ có một tập hợp đầy đủ các vectơ riêng độc lập. Vì vậy một ma trận với $A^2 = A$ có thể được chéo hóa.

**26** (Khuyên làm) Giả sử $Ax = \lambda x$. Nếu $\lambda = 0$ thì $x$ nằm trong không gian null. Nếu $\lambda \neq 0$ thì $x$ nằm trong không gian cột. Những không gian đó có số chiều là $(n - r) + r = n$. Vậy tại sao không phải mọi ma trận vuông đều có $n$ vectơ riêng độc lập tuyến tính?
**27** Các trị riêng của $A$ là 1 và 9, và các trị riêng của $B$ là -1 và 9:

| $A = \begin{bmatrix} 5 & 4 \\ 4 & 5 \end{bmatrix}$ | và | $B = \begin{bmatrix} 4 & 5 \\ 5 & 4 \end{bmatrix}$ |
|----------------------------------------------------|-----|----------------------------------------------------|

Tìm một căn bậc hai ma trận của $A$ từ $R = X\sqrt{\Lambda} X^{-1}$. Tại sao không có căn bậc hai ma trận thực nào của $B$?

**28** Nếu $A$ và $B$ có cùng các $\lambda$ với cùng các vectơ riêng độc lập, thì sự phân tích của chúng thành $X\Lambda X^{-1}$ là như nhau. Do đó $A = B$.
**29** Giả sử cùng một $X$ chéo hóa cả $A$ và $B$. Chúng có *cùng các vectơ riêng* trong $A = X\Lambda_1 X^{-1}$ và $B = X\Lambda_2 X^{-1}$. Hãy chứng minh rằng $AB = BA$.
**30** (a) Nếu $A = \begin{bmatrix} a & b \\ 0 & d \end{bmatrix}$ thì định thức của $A - \lambda I$ là $(\lambda - a)(\lambda - d)$. Hãy kiểm tra "Định lý Cayley-Hamilton" rằng $(A - aI)(A - dI) = \text{ma trận không}$.
- (b) Kiểm tra Định lý Cayley-Hamilton trên ma trận $A = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}$ của Fibonacci. Định lý dự đoán rằng $A^2 - A - I = 0$, vì đa thức $\det(A - \lambda I)$ là $\lambda^2 - \lambda - 1$.
**31** Thay $A = X\Lambda X^{-1}$ vào tích $(A - \lambda_1 I)(A - \lambda_2 I) \dots (A - \lambda_n I)$ và giải thích tại sao kết quả là ma trận không. Chúng ta đang thay thế ma trận $A$ cho số $\lambda$ trong đa thức $p(\lambda) = \det(A - \lambda I)$. *Định lý Cayley-Hamilton* nói rằng tích này luôn luôn là $p(A) = \text{ma trận không}$, ngay cả khi $A$ không thể chéo hóa.
**32** Nếu $A = \begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix}$ và $AB = BA$, hãy chứng minh rằng $B = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ cũng là một ma trận đường chéo. $B$ có cùng các vectơ riêng với $A$ nhưng các trị riêng khác nhau. Những ma trận đường chéo $B$ này tạo thành một không gian con hai chiều của không gian ma trận. $AB - BA = 0$ đưa ra bốn phương trình cho các ẩn $a, b, c, d$ — hãy tìm hạng của ma trận $4 \times 4$.
**33** Các lũy thừa $A^k$ tiến tới 0 nếu tất cả $|\lambda_i| < 1$ và chúng bùng nổ nếu bất kỳ $|\lambda_i| > 1$. Peter Lax đưa ra những ví dụ ấn tượng này trong cuốn sách *Linear Algebra* của ông:

$$A = \begin{bmatrix} 3 & 2 \\ 1 & 4 \end{bmatrix} \quad B = \begin{bmatrix} 3 & 2 \\ -5 & -3 \end{bmatrix} \quad C = \begin{bmatrix} 5 & 7 \\ -3 & -4 \end{bmatrix} \quad D = \begin{bmatrix} 5 & 6.9 \\ -3 & -4 \end{bmatrix}$$

$$\|A^{1024}\| > 10^{700} \quad B^{1024} = I \quad C^{1024} = -C \quad \|D^{1024}\| < 10^{-78}$$

Tìm các trị riêng $\lambda = e^{i\theta}$ của $B$ và $C$ để chứng minh $B^4 = I$ và $C^3 = -I$.

## Các bài toán thử thách (Challenge Problems)

**34** Lũy thừa bậc $n$ của phép quay một góc $\theta$ chính là phép quay một góc $n\theta$:

$$A^n = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}^n = \begin{bmatrix} \cos n\theta & -\sin n\theta \\ \sin n\theta & \cos n\theta \end{bmatrix}.$$

Hãy chứng minh công thức tuyệt vời đó bằng cách chéo hóa $A = X\Lambda X^{-1}$. Các vectơ riêng (các cột của $X$) là $(1, i)$ và $(i, 1)$. Bạn cần biết công thức Euler $e^{i\theta} = \cos \theta + i\sin \theta$.

**35** Chuyển vị của $A = X\Lambda X^{-1}$ là $A^T = (X^{-1})^T \Lambda X^T$. Các vectơ riêng trong $A^T \mathbf{y} = \lambda \mathbf{y}$ là các cột của ma trận $(X^{-1})^T$ đó. Chúng thường được gọi là **các vectơ riêng trái (left eigenvectors) của $A$**, bởi vì $\mathbf{y}^T A = \lambda \mathbf{y}^T$. Bạn nhân các ma trận như thế nào để tìm công thức này cho $A$?

**Tổng các ma trận hạng-1** $A = X\Lambda X^{-1} = \lambda_1 \mathbf{x}_1 \mathbf{y}_1^T + \dots + \lambda_n \mathbf{x}_n \mathbf{y}_n^T$.

**36** Nghịch đảo của $A = \mathbf{eye}(n) + \mathbf{ones}(n)$ là $A^{-1} = \mathbf{eye}(n) + C * \mathbf{ones}(n)$. Hãy nhân $AA^{-1}$ để tìm số $C$ đó (phụ thuộc vào $n$).

**37** Giả sử $A_1$ và $A_2$ là các ma trận $n \times n$ khả nghịch. Ma trận $B$ nào cho thấy $A_2 A_1 = B(A_1 A_2)B^{-1}$? Khi đó $A_2 A_1$ đồng dạng với $A_1 A_2$: *có cùng các trị riêng*.

**38 Khi nào một ma trận $A$ đồng dạng với ma trận trị riêng $\Lambda$ của nó?**
$A$ và $\Lambda$ luôn luôn có cùng các trị riêng. Nhưng sự đồng dạng đòi hỏi một ma trận $B$ với $A = B\Lambda B^{-1}$. Khi đó $B$ là ma trận \_\_\_\_\_ và $A$ phải có $n$ \_\_\_\_\_ độc lập.

**39** (Pavel Grinfeld) Không cần viết ra bất kỳ tính toán nào, bạn có thể tìm các trị riêng của ma trận này không? Bạn có thể tìm lũy thừa bậc 2017 là $A^{2017}$ không?

$$A = \begin{bmatrix} 110 & 55 & -164 \\ 42 & 21 & -62 \\ 88 & 44 & -131 \end{bmatrix}.$$

**Nếu $A$ là $m \times n$ và $B$ là $n \times m$, thì $AB$ và $BA$ có cùng các trị riêng khác không.**

*Chứng minh.* Bắt đầu với đẳng thức này giữa các ma trận vuông (có thể kiểm tra dễ dàng). Các ma trận thứ nhất và thứ ba là nghịch đảo của nhau. "Ma trận kích thước" hiển thị hình dạng của tất cả các khối.

$$\begin{bmatrix} I & -A \\ 0 & I \end{bmatrix} \begin{bmatrix} AB & 0 \\ B & 0 \end{bmatrix} \begin{bmatrix} I & A \\ 0 & I \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ B & BA \end{bmatrix} \quad \begin{bmatrix} m \times m & m \times n \\ n \times m & n \times n \end{bmatrix}$$

Phương trình $D^{-1} ED = F$ này nói rằng $F$ đồng dạng với $E$ — chúng có cùng $m+n$ trị riêng.

$$E = \begin{bmatrix} AB & 0 \\ B & 0 \end{bmatrix} \text{ có } m \text{ trị riêng của } AB, \text{ cộng thêm } n \text{ số không}$$

$$F = \begin{bmatrix} 0 & 0 \\ B & BA \end{bmatrix} \text{ có } n \text{ trị riêng của } BA, \text{ cộng thêm } m \text{ số không}$$

Vậy $AB$ và $BA$ có cùng các trị riêng ngoại trừ $|n - m|$ số không. Wow.

Nếu $A = \begin{bmatrix} 1 & 1 \end{bmatrix}$ và $B = A^T$ thì $A^T A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$ (chú ý $\lambda = 2$ và $0$) và $AA^T = \begin{bmatrix} 2 \end{bmatrix}$.

# **6.3 Hệ phương trình vi phân (Systems of Differential Equations)**

**1** Nếu $Ax = \lambda x$ thì $u(t) = e^{\lambda t}x$ sẽ giải được $\frac{du}{dt} = Au$. Mỗi $\lambda$ và $x$ cho ra một nghiệm $e^{\lambda t}x$.
**2** $A$ **ổn định (stable)** và $u(t) \to 0$ và $e^{At} \to 0$ khi tất cả các trị riêng của $A$ có phần thực $< 0$.
**3 Ma trận mũ (Matrix exponential)** $e^{At} = I + At + \dots + \frac{(At)^n}{n!} + \dots = X e^{\Lambda t} X^{-1}$ nếu $A$ có thể chéo hóa.
**4 Phương trình bậc hai (Second order equation)** $y'' + By' + Cy = 0$ tương đương với hệ $\frac{d}{dt}\begin{bmatrix} y \\ y' \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -C & -B \end{bmatrix} \begin{bmatrix} y \\ y' \end{bmatrix}$.

Các trị riêng, vectơ riêng và $A = X\Lambda X^{-1}$ là hoàn hảo cho các lũy thừa ma trận $A^k$. Chúng cũng hoàn hảo cho các phương trình vi phân $du/dt = Au$. Phần này phần lớn là đại số tuyến tính, nhưng để đọc nó bạn cần một kiến thức từ giải tích: *Đạo hàm của $e^{\lambda t}$ là $\lambda e^{\lambda t}$.* Điểm mấu chốt của phần này là: **Để chuyển đổi các phương trình vi phân hệ số hằng số thành đại số tuyến tính.**

Các phương trình thông thường $\frac{du}{dt} = u$ và $\frac{du}{dt} = \lambda u$ được giải bằng các hàm mũ:

| $\frac{du}{dt} = u$ sinh ra $u(t) = Ce^t$ | $\frac{du}{dt} = \lambda u$ sinh ra $u(t) = Ce^{\lambda t}$ | (1) |
|--------------------------------------------|--------------------------------------------------------------|-----|

Tại thời điểm $t = 0$, những nghiệm đó bao gồm $e^0 = 1$. Vì vậy cả hai đều rút gọn thành $u(0) = C$. "Giá trị ban đầu" này cho chúng ta biết lựa chọn đúng cho $C$. **Các nghiệm bắt đầu từ giá trị $u(0)$ tại thời điểm $t = 0$ là $u(t) = u(0)e^t$ và $u(t) = u(0)e^{\lambda t}$.**

Chúng ta vừa giải một bài toán $1 \times 1$. Đại số tuyến tính chuyển sang $n \times n$. Ẩn số là một vectơ $\mathbf{u}$ (bây giờ được in đậm). Nó bắt đầu từ vectơ ban đầu $\mathbf{u}(0)$, được cho trước. Hệ $n$ phương trình chứa một ma trận vuông $A$. Chúng ta mong đợi $n$ số mũ $e^{\lambda t}$ trong $\mathbf{u}(t)$, từ $n$ trị riêng $\lambda$:

| Hệ $n$ phương trình | $\frac{du}{dt} = Au$ | bắt đầu từ vectơ $u(0) = \begin{bmatrix} u_1(0) \\ \vdots \\ u_n(0) \end{bmatrix}$ | tại $t = 0$ . (2) |
|-------------------------|----------------------|--------------------------------------------------------------------------------------------|------------------|

Những phương trình vi phân này là *tuyến tính*. Nếu $u(t)$ và $v(t)$ là nghiệm, thì $Cu(t) + Dv(t)$ cũng vậy. Chúng ta sẽ cần $n$ hằng số như $C$ và $D$ để khớp với $n$ thành phần của $u(0)$. Công việc đầu tiên của chúng ta là tìm $n$ "nghiệm mũ thuần túy" $u = e^{\lambda t}x$ bằng cách sử dụng $Ax = \lambda x$.

Lưu ý rằng $A$ là một ma trận *không đổi*. Trong các phương trình tuyến tính khác, $A$ thay đổi khi $t$ thay đổi. Trong các phương trình phi tuyến, $A$ thay đổi khi $u$ thay đổi. Chúng ta không có những khó khăn đó, $du/dt = Au$ là "tuyến tính với các hệ số không đổi". Những phương trình đó và chỉ những phương trình đó mới là những phương trình vi phân mà chúng ta sẽ chuyển đổi trực tiếp sang đại số tuyến tính. Đây là chìa khóa:

*Giải các phương trình tuyến tính hệ số không đổi bằng các hàm mũ $e^{\lambda t}x$, khi $Ax = \lambda x$.*

# **Cách giải $\frac{du}{dt} = Au$**

Nghiệm mũ thuần túy của chúng ta sẽ là $e^{\lambda t}$ nhân với một vectơ cố định $x$. Bạn có thể đoán rằng $\lambda$ là một trị riêng của $A$, và $x$ *là vectơ riêng*. Thay $u(t) = e^{\lambda t}x$ vào phương trình $du/dt = Au$ để chứng minh bạn đúng. Hệ số $e^{\lambda t}$ sẽ bị triệt tiêu để còn lại $\lambda x = Ax$:

| **Chọn $u = e^{\lambda t} x$ khi $Ax = \lambda x$** | $\frac{du}{dt} = \lambda e^{\lambda t} x$ | khớp với | $Au = A e^{\lambda t} x$ | (3) |
|-------------------------------------------------------------------------------------------------|-------------------------------------------|-------------|-------------------------|-----|

Tất cả các thành phần của nghiệm đặc biệt này $u = e^{\lambda t}x$ đều có chung $e^{\lambda t}$. Nghiệm tăng lên khi $\lambda > 0$. Nó giảm đi khi $\lambda < 0$. Nếu $\lambda$ là một số phức, phần thực của nó quyết định sự tăng hay giảm. Phần ảo $\omega$ tạo ra sự dao động $e^{i\omega t}$ giống như sóng sin.

**Ví dụ 1** Giải
$$\frac{du}{dt} = Au = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} u$$
 bắt đầu từ $u(0) = \begin{bmatrix} 4 \\ 2 \end{bmatrix}$.

Đây là phương trình vectơ cho $u$. Nó chứa hai phương trình vô hướng cho các thành phần $y$ và $z$. Chúng được "ghép cặp với nhau" vì ma trận $A$ không phải là ma trận đường chéo:

$$\frac{du}{dt} = Au \implies \frac{d}{dt} \begin{bmatrix} y \\ z \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} y \\ z \end{bmatrix} \quad \text{có nghĩa là} \quad \frac{dy}{dt} = z \quad \text{và} \quad \frac{dz}{dt} = y.$$

Ý tưởng của các vectơ riêng là kết hợp các phương trình đó theo một cách để quay trở lại bài toán $1 \times 1$. Các tổ hợp $y + z$ và $y - z$ sẽ làm được điều đó. Cộng và trừ các phương trình:

| $\frac{d}{dt}(y+z) = z+y$ | và | $\frac{d}{dt}(y-z) = -(y-z).$ |
|---------------------------|-----|-------------------------------|

Tổ hợp $y + z$ tăng lên như $e^t$, vì nó có $\lambda = 1$. Tổ hợp $y - z$ giảm đi như $e^{-t}$, vì nó có $\lambda = -1$. Điểm mấu chốt là: Chúng ta không cần phải tung hứng các phương trình ban đầu $du/dt = Au$ để tìm kiếm những tổ hợp đặc biệt này. Các vectơ riêng và trị riêng của $A$ sẽ làm việc đó cho chúng ta.

Ma trận $A$ này có các trị riêng 1 và -1. Các vectơ riêng $x$ là $(1, 1)$ và $(1, -1)$. Các nghiệm mũ thuần túy $u_1$ và $u_2$ có dạng $e^{\lambda t}x$ với $\lambda_1 = 1$ và $\lambda_2 = -1$:

| $u_1(t) = e^{\lambda_1 t} x_1 = e^t \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ | và | $u_2(t) = e^{\lambda_2 t} x_2 = e^{-t} \begin{bmatrix} 1 \\ -1 \end{bmatrix}$ | (4) |
|---------------------------------------------------------------------------|-----|-------------------------------------------------------------------------------|-----|

Lưu ý: Những $u$ này thỏa mãn $Au_1 = u_1$ và $Au_2 = -u_2$, giống hệt như $x_1$ và $x_2$. Các hệ số $e^t$ và $e^{-t}$ thay đổi theo thời gian. Những hệ số đó cho $du_1/dt = u_1 = Au_1$ và $du_2/dt = -u_2 = Au_2$. **Chúng ta có hai nghiệm cho $\frac{du}{dt} = Au$.** Để tìm tất cả các nghiệm khác, **hãy nhân những nghiệm đặc biệt đó với bất kỳ số nào $C$ và $D$ rồi cộng lại:**

Nghiệm hoàn chỉnh với các hằng số $C$ và $D$: $\quad u(t) = C e^t \begin{bmatrix} 1 \\ 1 \end{bmatrix} + D e^{-t} \begin{bmatrix} 1 \\ -1 \end{bmatrix} \quad (5)$

Với hai hằng số $C$ và $D$ này, chúng ta có thể khớp bất kỳ vectơ bắt đầu nào $u(0) = (u_1(0), u_2(0))$. Đặt $t = 0$ và $e^0 = 1$. Ví dụ 1 yêu cầu giá trị ban đầu là $u(0) = (4, 2)$:

$$u(0) \text{ quyết định } C, D \implies C \begin{bmatrix} 1 \\ 1 \end{bmatrix} + D \begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 4 \\ 2 \end{bmatrix} \quad \text{cho ta } C = 3 \quad \text{và} \quad D = 1.$$

Với $C = 3$ và $D = 1$ trong nghiệm (5), bài toán giá trị ban đầu đã được giải quyết hoàn toàn. Ba bước giải $u_{k+1} = Au_k$ trước đây bây giờ sẽ giải $\frac{du}{dt} = Au$:

1. **1.** Viết $u(0)$ dưới dạng một **tổ hợp** $c_1 x_1 + \dots + c_n x_n$ **của các vectơ riêng của $A$**.
2. **2.** Nhân mỗi vectơ riêng $x_i$ với **hệ số tăng trưởng (growth factor) của nó** $e^{\lambda_i t}$.
3. **3.** Nghiệm là cùng một tổ hợp của các nghiệm thuần túy $e^{\lambda_i t}x$ đó:

$$\frac{du}{dt} = Au \implies u(t) = c_1 e^{\lambda_1 t} x_1 + \dots + c_n e^{\lambda_n t} x_n. \quad (6)$$

*Trường hợp ngoại trừ:* Nếu hai $\lambda$ bằng nhau, với chỉ một vectơ riêng, một nghiệm khác là cần thiết. (Nó sẽ là $te^{\lambda t}x$.) Bước 1 cần chéo hóa $A = X\Lambda X^{-1}$: một cơ sở của $n$ vectơ riêng.

**Ví dụ 2** Giải $du/dt = Au$ khi biết các trị riêng $\lambda = 1, 2, 3$ của $A$:

| **Ví dụ điển hình** | $\frac{du}{dt} = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 2 & 1 \\ 0 & 0 & 3 \end{bmatrix} u$ | bắt đầu từ $u(0) = \begin{bmatrix} 9 \\ 7 \\ 4 \end{bmatrix}$ . |
|--------------------------------------------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| **Phương trình cho $u$** | | |
| **Điều kiện ban đầu $u(0)$** | | |

Các vectơ riêng là $x_1 = (1, 0, 0)$ và $x_2 = (1, 1, 0)$ và $x_3 = (1, 1, 1)$.

**Bước 1** Vectơ $u(0) = (9, 7, 4)$ là $2x_1 + 3x_2 + 4x_3$. Do đó $(c_1, c_2, c_3) = (2, 3, 4)$.

**Bước 2** Các hệ số $e^{\lambda t}$ cho ra các nghiệm mũ $e^t x_1$ và $e^{2t} x_2$ và $e^{3t} x_3$.

**Bước 3** Tổ hợp bắt đầu từ $u(0)$ là $u(t) = 2e^t x_1 + 3e^{2t} x_2 + 4e^{3t} x_3$.

Các hệ số 2, 3, 4 đến từ việc giải phương trình tuyến tính $c_1 x_1 + c_2 x_2 + c_3 x_3 = u(0)$:

$$\begin{bmatrix} x_1 & x_2 & x_3 \end{bmatrix} \begin{bmatrix} c_1 \\ c_2 \\ c_3 \end{bmatrix} = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 2 \\ 3 \\ 4 \end{bmatrix} = \begin{bmatrix} 9 \\ 7 \\ 4 \end{bmatrix} \quad \text{chính là } Xc = u(0). \quad (7)$$

Bây giờ bạn đã có ý tưởng cơ bản — làm thế nào để giải $du/dt = Au$. Phần còn lại của phần này sẽ tiến xa hơn. Chúng ta giải các phương trình có chứa đạo hàm *bậc hai*, vì chúng phát sinh rất thường xuyên trong các ứng dụng. Chúng ta cũng quyết định xem $u(t)$ tiến tới 0 hay bùng nổ hay chỉ dao động.

Vào cuối phần sẽ xuất hiện *ma trận mũ (matrix exponential)* $e^{At}$. Công thức ngắn gọn $e^{At}u(0)$ giải phương trình $du/dt = Au$ theo cùng cách mà $A^k u_0$ giải phương trình $u_{k+1} = Au_k$. Ví dụ 3 sẽ cho thấy "phương trình sai phân" giúp giải phương trình vi phân như thế nào.

Tất cả những bước này đều sử dụng các $\lambda$ và $x$. Phần này giải quyết các bài toán hệ số không đổi biến thành đại số tuyến tính. Nó làm sáng tỏ các phương trình vi phân đơn giản nhất nhưng quan trọng nhất này - có nghiệm hoàn toàn dựa trên các hệ số tăng trưởng $e^{\lambda t}$.

### **Phương trình bậc hai (Second Order Equations)**

**Phương trình quan trọng nhất trong cơ học là** $my'' + by' + ky = 0$. Số hạng đầu tiên là khối lượng $m$ nhân với gia tốc $a = y''$. Số hạng $ma$ này cân bằng với lực $F$ (đó là *Định luật Newton*). Lực này bao gồm lực cản $-by'$ và lực đàn hồi $-ky$, tỷ lệ với khoảng cách dịch chuyển. Đây là một phương trình bậc hai vì nó chứa đạo hàm bậc hai $y'' = d^2 y / dt^2$. Nó vẫn là phương trình tuyến tính với các hệ số không đổi $m, b, k$.

Trong một khóa học phương trình vi phân, phương pháp giải là thay $y = e^{\lambda t}$. Mỗi đạo hàm của $y$ đưa xuống một hệ số $\lambda$. Chúng ta muốn $y = e^{\lambda t}$ giải được phương trình:

| $m \frac{d^2 y}{dt^2} + b \frac{dy}{dt} + ky = 0$ | trở thành | $(m\lambda^2 + b\lambda + k)e^{\lambda t} = 0.$ | (8) |
|---------------------------------------------------|---------|-------------------------------------------------|-----|

Mọi thứ phụ thuộc vào $m\lambda^2 + b\lambda + k = 0$. Phương trình đối với $\lambda$ này có hai nghiệm $\lambda_1$ và $\lambda_2$. Khi đó phương trình đối với $y$ có hai nghiệm thuần túy $y_1 = e^{\lambda_1 t}$ và $y_2 = e^{\lambda_2 t}$. Các tổ hợp của chúng $c_1 y_1 + c_2 y_2$ cho ra nghiệm tổng quát trừ phi $\lambda_1 = \lambda_2$.

Trong một khóa học đại số tuyến tính, chúng ta mong đợi các ma trận và các trị riêng. Do đó, chúng ta biến phương trình vô hướng (với $y''$) thành một *phương trình vectơ cho $y$ và $y'$:* chỉ có đạo hàm bậc nhất. Giả sử khối lượng $m = 1$. Hai phương trình cho $u = (y, y')$ tạo ra $du/dt = Au$:

| $dy/dt = y'$         | chuyển thành | $\frac{d}{dt} \begin{bmatrix} y \\ y' \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -k & -b \end{bmatrix} \begin{bmatrix} y \\ y' \end{bmatrix} = Au.$ | $(9)$ |
|----------------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------|-------|
| $dy'/dt = -ky - by'$ |             |                                                                                                                                         |       |

Phương trình đầu tiên $dy/dt = y'$ là tầm thường (nhưng đúng). Phương trình thứ hai là phương trình (8) kết nối $y''$ với $y'$ và $y$. Cùng với nhau, chúng kết nối $u'$ với $u$. Vì vậy chúng ta giải $u' = Au$ bằng các trị riêng của $A$:

$$A - \lambda I = \begin{bmatrix} -\lambda & 1 \\ -k & -b - \lambda \end{bmatrix}$$
 có định thức $\lambda^2 + b\lambda + k = 0$.

**Phương trình cho các $\lambda$ hoàn toàn giống với (8)! Nó vẫn là $\lambda^2 + b\lambda + k = 0$, vì $m = 1$.** Các nghiệm $\lambda_1$ và $\lambda_2$ bây giờ là *các trị riêng của $A$*. Các vectơ riêng và nghiệm là

$$x_1 = \begin{bmatrix} 1 \\ \lambda_1 \end{bmatrix}, \quad x_2 = \begin{bmatrix} 1 \\ \lambda_2 \end{bmatrix}, \quad u(t) = c_1 e^{\lambda_1 t} \begin{bmatrix} 1 \\ \lambda_1 \end{bmatrix} + c_2 e^{\lambda_2 t} \begin{bmatrix} 1 \\ \lambda_2 \end{bmatrix}.$$

Thành phần đầu tiên của $u(t)$ có $y = c_1 e^{\lambda_1 t} + c_2 e^{\lambda_2 t}$ — cùng một nghiệm như trước. Nó không thể là thứ gì khác. Trong thành phần thứ hai của $u(t)$, bạn nhìn thấy vận tốc $dy/dt$. Bài toán vectơ hoàn toàn nhất quán với bài toán vô hướng. Ma trận $A$ kích thước $2 \times 2$ được gọi là *ma trận đồng hành (companion matrix) — một người đồng hành* với phương trình bậc hai với $y''$.

### **Ví dụ 3** *Chuyển động quanh một vòng tròn với $y'' + y = 0$ và $y = \cos t$*

Đây là phương trình chủ đạo (master equation) của chúng ta với khối lượng $m = 1$ và độ cứng $k = 1$ và $d = 0$: không có lực cản. Thay $y = e^{\lambda t}$ vào $y'' + y = 0$ để đạt được $\lambda^2 + 1 = 0$. *Các nghiệm là* $\lambda = i$ *và* $\lambda = -i$. Khi đó một nửa của $e^{it} + e^{-it}$ cho ta nghiệm $y = \cos t$.

Dưới dạng một hệ bậc nhất, các giá trị ban đầu $y(0) = 1, y'(0) = 0$ đi vào $u(0) = (1, 0)$:

| Sử dụng $y'' = -y$ | $\frac{du}{dt} = \frac{d}{dt} \begin{bmatrix} y \\ y' \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix} \begin{bmatrix} y \\ y' \end{bmatrix} = Au.$ | (10) |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|------|

Các trị riêng của $A$ một lần nữa lại giống hệt nhau $\lambda = i$ và $\lambda = -i$ (không có gì ngạc nhiên). $A$ phản đối xứng với các vectơ riêng $x_1 = (1, i)$ và $x_2 = (1, -i)$. Tổ hợp khớp với $u(0) = (1, 0)$ là $\frac{1}{2}(x_1 + x_2)$. Bước 2 nhân các $x$ với $e^{it}$ và $e^{-it}$. Bước 3 kết hợp các dao động thuần túy thành $u(t)$ để tìm ra $y = \cos t$ đúng như dự kiến:

$$\mathbf{u}(t) = \frac{1}{2}e^{it} \begin{bmatrix} 1 \\ i \end{bmatrix} + \frac{1}{2}e^{-it} \begin{bmatrix} 1 \\ -i \end{bmatrix} = \begin{bmatrix} \cos t \\ -\sin t \end{bmatrix}. \quad \text{Đây là } \begin{bmatrix} y(t) \\ y'(t) \end{bmatrix}.$$

Tất cả đều tốt. Vectơ $u = (\cos t, -\sin t)$ đi quanh một vòng tròn (Hình 6.3). Bán kính bằng 1 vì $\cos^2 t + \sin^2 t = 1$.

# **Phương trình sai phân (Difference Equations) (tùy chọn)**

Để hiển thị một vòng tròn trên màn hình, hãy thay thế $y'' = -y$ bằng một *phương trình sai phân*. Dưới đây là ba lựa chọn sử dụng $Y(t + \Delta t) - 2Y(t) + Y(t - \Delta t)$. Chia cho $(\Delta t)^2$ để xấp xỉ $y''$.

| F | Tiến (Forward) từ thời điểm $n$ | (11 F) |
|---|----------------------------------|--------|
| C | Ở giữa (Centered) tại thời gian $n$ | $\frac{Y_{n+1} - 2Y_n + Y_{n-1}}{(\Delta t)^2}$ (11 C) |
| B | Lùi (Backward) tới thời điểm $n+1$ | (11 B) |

Hình 6.3 cho thấy phương trình chính xác $y(t) = \cos t$ hoàn thành một vòng tròn tại $t = 2\pi$. Ba phương pháp sai phân *không* hoàn thành một vòng tròn hoàn hảo trong 32 bước thời gian có độ dài $\Delta t = 2\pi / 32$. Những hình ảnh đó sẽ được giải thích bằng các trị riêng:

### **Tiến** $|\lambda| > 1$ **(xoắn ốc ra ngoài) Trung tâm** $|\lambda| = 1$ **(tốt nhất) Lùi** $|\lambda| < 1$ **(xoắn ốc vào trong)**

Các phương trình 2 bước (11) rút gọn thành các hệ 1 bước $U_{n+1} = A U_n$. Thay vì $u = (y, y')$, ẩn rời rạc là $U_n = (Y_n, Z_n)$. Chúng ta thực hiện **n** bước thời gian $\Delta t$ bắt đầu từ $U_0$:

| Tiến<br>(11F) | $Y_{n+1} = Y_n + \Delta t Z_n$ | trở thành | $U_{n+1} = \begin{bmatrix} 1 & \Delta t \\ -\Delta t & 1 \end{bmatrix} \begin{bmatrix} Y_n \\ Z_n \end{bmatrix} = A U_n$ | (12) |
|------------------|--------------------------------|---------|--------------------------------------------------------------------------------------------------------------------------|------|

Đó giống như $Y' = Z$ và $Z' = -Y$. Chúng là các phương trình bậc nhất liên quan đến các thời điểm $n$ và $n+1$. Việc loại bỏ $Z$ sẽ mang lại phương trình "tiến" bậc hai (11 F).

Câu hỏi của tôi rất đơn giản. *Các điểm $(Y_n, Z_n)$ có nằm trên vòng tròn* $Y^2 + Z^2 = 1$ *không?* Không, chúng đang lớn dần đến vô cùng trong Hình 6.3. *Chúng ta đang lấy các lũy thừa* $A^n$ *chứ không phải* $e^{At}$, *vì vậy chúng ta kiểm tra độ lớn* $|\lambda|$ *chứ không phải phần thực của các trị riêng.*

| Các trị riêng của $A$ | $\lambda = 1 \pm i\Delta t$ | Khi đó $ |\lambda|  > 1$ và $(Y_n, Z_n)$ xoắn ốc ra ngoài |
|--------------------|-----------------------------|---------------------------------------------------|

Hình 6.3: Đồ thị chính xác $u = (\cos t, -\sin t)$ trên một vòng tròn. **Euler tiến xoắn ốc ra ngoài** (32 bước).

Sự lựa chọn lùi trong (11 B) sẽ làm điều ngược lại trong Hình 6.4. Chú ý ma trận $A$ mới:

| Lùi | $Y_{n+1} = Y_n + \Delta t Z_{n+1}$ | là | $\begin{bmatrix} 1 & -\Delta t \\ \Delta t & 1 \end{bmatrix} \begin{bmatrix} Y_{n+1} \\ Z_{n+1} \end{bmatrix} = \begin{bmatrix} Y_n \\ Z_n \end{bmatrix} = U_n$ | (13) |
|----------|------------------------------------|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
|          | $Z_{n+1} = Z_n - \Delta t Y_{n+1}$ |    |                                                                                                                                                                 |      |

Ma trận đó có các trị riêng $1 \pm i\Delta t$. Nhưng chúng ta *nghịch đảo* nó để đạt được $U_{n+1}$ từ $U_n$. Do đó $| \lambda | < 1$ giải thích tại sao *nghiệm xoắn ốc vào trong* đến $(0,0)$ đối với sai phân lùi.

Ở phía bên phải của Hình 6.4, bạn thấy 32 bước với lựa chọn *trung tâm*. Nghiệm ở gần với vòng tròn (Bài 28) nếu $\Delta t < 2$. Đây là **phương pháp nhảy ếch (leapfrog method)**, được sử dụng liên tục. Sai phân bậc hai $Y_{n+1} - 2Y_n + Y_{n-1}$ "nhảy qua" giá trị trung tâm $Y_n$ trong (11).

Đây là cách một nhà hóa học theo dõi chuyển động của các phân tử (động lực học phân tử dẫn đến những tính toán khổng lồ). Khoa học tính toán rất sống động vì một phương trình vi phân có thể được thay thế bằng nhiều phương trình sai phân - một số không ổn định, một số ổn định, một số trung tính. Bài 30 có phương pháp thứ tư (rất tốt) hoàn toàn nằm ngay trên vòng tròn.

Kỹ thuật thực tế và vật lý thực tế xử lý các hệ thống (không chỉ là một khối lượng duy nhất tại một điểm). Ẩn $y$ là một vectơ. Hệ số của $y''$ là một *ma trận khối lượng (mass matrix) $M$*, với $n$ khối lượng. Hệ số của $y$ là một *ma trận độ cứng (stiffness matrix) $K$*, không phải là một số $k$. Hệ số của $y'$ là một ma trận cản, có thể bằng không.

Phương trình vectơ $My'' + Ky = f$ là một phần quan trọng của cơ học tính toán. Nó được kiểm soát bởi các trị riêng của $M^{-1}K$ trong $Kx = \lambda Mx$.

Hình 6.4: Sai phân lùi xoắn ốc vào trong. Nhảy ếch ở gần vòng tròn chính xác.

## **Sự ổn định của ma trận $2 \times 2$ (Stability of 2 by 2 Matrices)**

Đối với việc giải $du/dt = Au$, có một câu hỏi cơ bản. *Nghiệm có tiến đến $u = 0$ khi $t \to \infty$ không?* Bài toán có *ổn định*, bằng cách tiêu tán năng lượng không? Một nghiệm chứa $e^t$ là không ổn định. Sự ổn định phụ thuộc vào các trị riêng của $A$.

Nghiệm hoàn chỉnh $u(t)$ được xây dựng từ các nghiệm thuần túy $e^{\lambda t}x$. **Nếu** trị riêng $\lambda$ là số thực, chúng ta biết chính xác khi nào $e^{\lambda t}$ sẽ tiến đến 0: *Số $\lambda$ phải âm.* **Nếu** trị riêng là một số phức $\lambda = r + is$, *phần thực $r$ phải âm.* Khi $e^{\lambda t}$ tách thành $e^{rt}e^{ist}$, hệ số $e^{ist}$ có giá trị tuyệt đối cố định bằng 1:

| $e^{ist} = \cos st + i \sin st$ | có | $|e^{ist}|^2 = \cos^2 st + \sin^2 st = 1$ |
|---------------------------------|-----|-------------------------------------------|

Phần thực của $\lambda$ kiểm soát sự tăng trưởng ($r > 0$) hoặc suy giảm ($r < 0$).

Câu hỏi đặt ra là: *Những ma trận nào có các trị riêng âm?* Nói chính xác hơn, khi nào thì *tất cả các phần thực của $\lambda$ đều âm?* Các ma trận $2 \times 2$ cho phép một câu trả lời rõ ràng.

**Sự ổn định** $A$ là *ổn định* và $u(t) \to 0$ khi tất cả các trị riêng $\lambda$ có *phần thực âm*. Ma trận $2 \times 2$ $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ phải vượt qua hai bài kiểm tra:

| | Vết (trace) $T = a + d$ phải âm. |
|-|-------------------------------------------------|
| | Định thức (determinant) $D = ad - bc$ phải dương. |

**Lý do** **Nếu** các $\lambda$ là số thực và âm, tổng của chúng là âm. Đây là vết $T$. Tích của chúng là dương. Đây là định thức $D$. Lập luận này cũng đi theo hướng ngược lại. **Nếu** $D = \lambda_1 \lambda_2$ là dương, thì $\lambda_1$ và $\lambda_2$ có cùng dấu. **Nếu** $T = \lambda_1 + \lambda_2$ là âm, dấu đó sẽ là âm. Chúng xuất chúng ta có thể kiểm tra $T$ và $D$.

**Nếu** các $\lambda$ là số phức, chúng phải có dạng $r + is$ và $r - is$. Nếu không $T$ và $D$ sẽ không phải là số thực. Định thức $D$ tự động dương, vì $(r + is)(r - is) = r^2 + s^2$. Vết $T$ là $r + is + r - is = 2r$. Do đó một vết $T$ âm có nghĩa là phần thực $r$ âm và ma trận ổn định. Q.E.D.

Hình 6.5 cho thấy parabol $T^2 = 4D$ phân tách các $\lambda$ thực khỏi các $\lambda$ phức. Việc giải $\lambda^2 - T\lambda + D = 0$ liên quan đến căn bậc hai $\sqrt{T^2 - 4D}$. Căn này là số thực bên dưới parabol và là số ảo bên trên nó. Vùng ổn định là *góc phần tư phía trên bên trái* của hình nơi vết $T$ âm và định thức $D$ dương.

Hình 6.5: Ma trận $2 \times 2$ ổn định ($u(t) \to 0$) khi **vết (trace) < 0** và **định thức (det) > 0.**

# **Ma trận mũ (The Exponential of a Matrix)**

*Chúng ta muốn viết nghiệm $u(t)$ dưới dạng mới* $e^{At}u(0)$. Đầu tiên chúng ta phải giải thích ý nghĩa của $e^{At}$, với một ma trận ở phần mũ. Để định nghĩa $e^{At}$ cho các ma trận, chúng ta sao chép $e^x$ đối với các số.

Định nghĩa trực tiếp của $e^x$ là bằng chuỗi vô hạn $1 + x + \frac{1}{2}x^2 + \frac{1}{6}x^3 + \dots$. Khi bạn đổi $x$ thành một ma trận vuông $At$, chuỗi này định nghĩa ma trận mũ $e^{At}$:

| Ma trận mũ $e^{At}$ | $e^{At} = I + At + \frac{1}{2}(At)^2 + \frac{1}{6}(At)^3 + \dots$ | (14) |
|------------------------|-------------------------------------------------------------|------|
| Đạo hàm theo $t$ của nó là $A e^{At}$ | $A + A^2 t + \frac{1}{2}A^3 t^2 + \dots = A e^{At}$ | |
| Các trị riêng của nó là $e^{\lambda t}$ | $\left(I + At + \frac{1}{2}(At)^2 + \dots \right)x = \left( 1 + \lambda t + \frac{1}{2}(\lambda t)^2 + \dots \right)x$ | |

Số chia cho $(At)^n$ là "$n$ giai thừa". Nó là $n! = (1)(2)\dots(n-1)(n)$. Các giai thừa sau 1, 2, 6 là $4! = 24$ và $5! = 120$. Chúng tăng lên rất nhanh. Chuỗi này luôn hội tụ và đạo hàm của nó luôn là $A e^{At}$. Do đó $e^{At}u(0)$ giải phương trình vi phân bằng một công thức nhanh chóng — ngay cả *khi thiếu vectơ riêng.*

Tôi sẽ sử dụng chuỗi này trong Ví dụ 4, để xem nó hoạt động như thế nào với một vectơ riêng bị thiếu. Nó **sẽ tạo ra $t e^{\lambda t}$**. Trước tiên hãy để tôi đạt tới $X e^{\Lambda t} X^{-1}$ trong trường hợp tốt (có thể chéo hóa).

Chương này nhấn mạnh cách tìm $u(t) = e^{At}u(0)$ bằng cách chéo hóa. Giả sử $A$ có $n$ vectơ riêng độc lập, nên nó có thể chéo hóa. Thay $A = X\Lambda X^{-1}$ vào chuỗi của $e^{At}$. Bất cứ khi nào $X\Lambda X^{-1} X\Lambda X^{-1}$ xuất hiện, hãy triệt tiêu $X^{-1}X$ ở giữa:

| Sử dụng chuỗi | $e^{At} = I + X\Lambda X^{-1}t + \frac{1}{2}(X\Lambda X^{-1}t)(X\Lambda X^{-1}t) + \dots$ |
|----------------|-------------------------------------------------------------------------------------------|
| Đặt thừa số $X$ và $X^{-1}$ | $= X \left[ I + \Lambda t + \frac{1}{2}(\Lambda t)^2 + \dots \right] X^{-1}$ | (15) |

$e^{At}$ được chéo hóa!
$$e^{At} = X e^{\Lambda t} X^{-1}.$$

$e^{At}$ có cùng ma trận vectơ riêng $X$ như $A$. Khi đó $\Lambda$ là một ma trận đường chéo và $e^{\Lambda t}$ cũng vậy. Các số $e^{\lambda_i t}$ nằm trên đường chéo. Nhân $X e^{\Lambda t} X^{-1} u(0)$ để nhận ra $u(t)$:

$$e^{At} \mathbf{u}(0) = X e^{\Lambda t} X^{-1} \mathbf{u}(0) = \begin{bmatrix} x_1 & \cdots & x_n \end{bmatrix} \begin{bmatrix} e^{\lambda_1 t} & & & \\ & e^{\lambda_2 t} & & \\ & & \ddots & \\ & & & e^{\lambda_n t} \end{bmatrix} \begin{bmatrix} c_1 \\ \vdots \\ c_n \end{bmatrix}. \quad (16)$$

Nghiệm $e^{At}u(0)$ này là cùng một đáp án thu được trong phương trình (6) từ ba bước:

- **1.** $u(0) = c_1 x_1 + \dots + c_n x_n = Xc$. Ở đây chúng ta cần $n$ vectơ riêng độc lập.
- **2.** Nhân mỗi $x_i$ với hệ số tăng trưởng của nó $e^{\lambda_i t}$ để theo nó tiến về phía trước theo thời gian.
- **3.** Dạng tốt nhất của $e^{At}u(0)$ là $u(t) = c_1 e^{\lambda_1 t}x_1 + \dots + c_n e^{\lambda_n t}x_n. \quad (17)$

**Ví dụ 4** Khi bạn thay $y = e^{\lambda t}$ vào $y'' - 2y' + y = 0$, bạn nhận được một phương trình có **nghiệm kép:** $\lambda^2 - 2\lambda + 1 = 0$ là $(\lambda - 1)^2 = 0$ với $\lambda = 1, 1$. Một khóa học phương trình vi phân sẽ đề xuất $e^t$ và $te^t$ làm hai nghiệm độc lập. Ở đây chúng ta khám phá lý do tại sao.

Đại số tuyến tính rút gọn $y'' - 2y' + y = 0$ thành một phương trình vectơ cho $u = (y, y')$:

$$\frac{d}{dt} \begin{bmatrix} y \\ y' \end{bmatrix} = \begin{bmatrix} y' \\ 2y' - y \end{bmatrix} \text{ chính là } \frac{du}{dt} = Au = \begin{bmatrix} 0 & 1 \\ -1 & 2 \end{bmatrix} u. \quad (18)$$

$A$ có **nghiệm kép $\lambda = 1, 1$** (với vết = 2 và định thức $A$ = 1). Các vectơ riêng duy nhất là bội số của $x = (1, 1)$. *Không thể chéo hóa được, $A$* chỉ có một đường thẳng vectơ riêng. Vì vậy chúng ta tính $e^{At}$ từ định nghĩa của nó dưới dạng một chuỗi:

| Chuỗi ngắn | $e^{At} = e^{It} e^{(A-I)t} = e^t [I + (A - I)t]$ | (19) |
|--------------|---------------------------------------------------|------|

Chuỗi "vô hạn" cho $e^{(A-I)t}$ đó kết thúc nhanh chóng vì $(A - I)^2$ là ma trận không! Bạn có thể thấy $te^t$ trong phương trình (19). Thành phần đầu tiên của $e^{At} u(0)$ là đáp án $y(t)$ của chúng ta:

$$\begin{bmatrix} y \\ y' \end{bmatrix} = e^t \left( I + \begin{bmatrix} -1 & 1 \\ -1 & 1 \end{bmatrix} t \right) \begin{bmatrix} y(0) \\ y'(0) \end{bmatrix} \implies y(t) = e^t y(0) - te^t y(0) + te^t y'(0).$$

**Ví dụ 5** Sử dụng chuỗi vô hạn để tìm $e^{At}$ cho $A = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}$. Chú ý rằng $A^4 = I$:

| $A = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}$ | $A^2 = \begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}$ | $A^3 = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ | $A^4 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ |
|-------------------------------------------------|----------------------------------------------------|-----------------------------------------------|--------------------------------------------------|

$A^5, A^6, A^7, A^8$ sẽ là một sự lặp lại của $A, A^2, A^3, A^4$. Góc trên bên phải có $1, 0, -1, 0$ lặp đi lặp lại trong các lũy thừa của $A$. Khi đó $t - \frac{1}{6}t^3$ bắt đầu chuỗi vô hạn cho $e^{At}$ ở góc trên bên phải đó, và $1 - \frac{1}{2}t^2$ bắt đầu ở góc trên bên trái:

$$e^{At} = I + At + \frac{1}{2}(At)^2 + \frac{1}{6}(At)^3 + \dots = \begin{bmatrix} 1 - \frac{1}{2}t^2 + \dots & t - \frac{1}{6}t^3 + \dots \\ -t + \frac{1}{6}t^3 + \dots & 1 - \frac{1}{2}t^2 + \dots \end{bmatrix}.$$

Hàng đầu tiên của ma trận $e^{At}$ đó cho thấy chuỗi vô hạn cho cosin và sin!

$$A = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}, \quad e^{At} = \begin{bmatrix} \cos t & \sin t \\ -\sin t & \cos t \end{bmatrix}. \quad (20)$$

$A$ là một ma trận phản đối xứng ($A^T = -A$). Ma trận mũ của nó $e^{At}$ là một ma trận trực giao. Các trị riêng của $A$ là $i$ và $-i$. Các trị riêng của $e^{At}$ là $e^{it}$ và $e^{-it}$. Ba quy tắc:

**1** $e^{At}$ *luôn có nghịch đảo là* $e^{-At}$. **2** *Các trị riêng của $e^{At}$ luôn là* $e^{\lambda t}$. **3** *Khi $A$ là phản đối xứng, $e^{At}$ là ma trận trực giao. Nghịch đảo = chuyển vị =* $e^{-At}$.

Phản đối xứng (antisymmetric) cũng giống như "lệch đối xứng" (skew-symmetric). Những ma trận đó có các trị riêng thuần ảo như $i$ và $-i$. Khi đó $e^{At}$ có các trị riêng như $e^{it}$ và $e^{-it}$. Giá trị tuyệt đối của chúng là 1: tính ổn định trung tính, dao động thuần túy, năng lượng được bảo toàn. Vậy $\|u(t)\| = \|u(0)\|$.

Ví dụ cuối cùng của chúng ta có một ma trận tam giác $A$. Khi đó ma trận vectơ riêng $X$ là ma trận tam giác. $X^{-1}$ và $e^{At}$ cũng vậy. Bạn sẽ thấy hai dạng của nghiệm: một tổ hợp các vectơ riêng và dạng rút gọn $e^{At}u(0)$.

**Ví dụ 6** Giải $du/dt = Au = \begin{bmatrix} 1 & 1 \\ 0 & 2 \end{bmatrix} u$ bắt đầu từ $u(0) = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ tại $t = 0$.

**Lời giải** Các trị riêng 1 và 2 nằm trên đường chéo của $A$ (vì $A$ là ma trận tam giác). Các vectơ riêng là $(1, 0)$ và $(1, 1)$. Vectơ bắt đầu $u(0)$ là $x_1 + x_2$ nên $c_1 = c_2 = 1$. Khi đó $u(t)$ là cùng một tổ hợp các hàm mũ thuần túy (không có $t e^{\lambda t}$ khi $\lambda = 1$ và $2$):

| Nghiệm cho $u' = Au$ | $u(t) = e^t \begin{bmatrix} 1 \\ 0 \end{bmatrix} + e^{2t} \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ |
|-----------------------|-------------------------------------------------------------------------------------------------|

Đó là dạng rõ ràng nhất. Nhưng dạng ma trận với $e^{At}$ tạo ra $u(t)$ cho mọi $u(0)$:

| $u(t) = X e^{\Lambda t} X^{-1} u(0)$ là $\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} e^t & 0 \\ 0 & e^{2t} \end{bmatrix} \begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix} u(0) = \begin{bmatrix} e^t & e^{2t} - e^t \\ 0 & e^{2t} \end{bmatrix} u(0).$ |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

*Ma trận cuối cùng đó là $e^{At}$.* Nó rất đẹp vì $A$ là ma trận tam giác. Tình huống cũng giống như đối với $Ax = b$ và các ma trận nghịch đảo. Chúng ta không cần $A^{-1}$ để tìm $x$, và chúng ta không cần $e^{At}$ để giải $du/dt = Au$. Nhưng đối với những công thức giải nhanh, $A^{-1}b$ và $e^{At}u(0)$ là vô địch.

#### **• ÔN TẬP CÁC Ý TƯỞNG CHÍNH •**

- **1.** Phương trình $u' = Au$ tuyến tính với các hệ số không đổi trong $A$. Bắt đầu từ $u(0)$.
- **2.** Nghiệm của nó thường là một tổ hợp của các hàm mũ, liên quan đến mọi $\lambda$ và $x$:

**Các vectơ riêng độc lập**
$$u(t) = c_1 e^{\lambda_1 t} x_1 + \dots + c_n e^{\lambda_n t} x_n$$

- **3.** Các hằng số $c_1, \dots, c_n$ được xác định bởi $u(0) = c_1 x_1 + \dots + c_n x_n = Xc$.
- **4.** $u(t)$ tiến về 0 **(tính ổn định)** nếu mọi $\lambda$ có phần thực âm: Tất cả $e^{\lambda t} \to 0$.
- **5.** Các nghiệm có dạng rút gọn $u(t) = e^{At}u(0)$, với ma trận mũ $e^{At}$.
- **6.** Các phương trình với $y''$ rút gọn thành $u' = Au$ bằng cách kết hợp $y$ và $y'$ vào vectơ $u$.

#### **• CÁC VÍ DỤ CÓ LỜI GIẢI •**

**6.3 A** Giải $y'' + 4y' + 3y = 0$ bằng cách thay $e^{\lambda t}$ và cũng bằng đại số tuyến tính.

**Lời giải** Việc thay $y = e^{\lambda t}$ mang lại $(\lambda^2 + 4\lambda + 3)e^{\lambda t} = 0$. Phương trình bậc hai đó phân tích thành $\lambda^2 + 4\lambda + 3 = (\lambda + 1)(\lambda + 3) = 0$. Do đó $\lambda_1 = -1$ và $\lambda_2 = -3$. Các nghiệm thuần túy là $y_1 = e^{-t}$ và $y_2 = e^{-3t}$. Nghiệm hoàn chỉnh $y = c_1 y_1 + c_2 y_2$ tiến tới không.

Để sử dụng đại số tuyến tính, chúng ta đặt $u = (y, y')$. Khi đó phương trình vectơ là $u' = Au$:

$$\frac{du}{dt} = \begin{bmatrix} 0 & 1 \\ -3 & -4 \end{bmatrix} u.$$

$A$ này là một "ma trận đồng hành" (companion matrix) và các trị riêng của nó một lần nữa lại là -1 và -3:

| Cùng phương trình bậc hai | $\det(A - \lambda I) = \begin{vmatrix} -\lambda & 1 \\ -3 & -4 - \lambda \end{vmatrix} = \lambda^2 + 4\lambda + 3 = 0.$ |
|----------------|-------------------------------------------------------------------------------------------------------------------------|

Các vectơ riêng của $A$ là $(1, \lambda_1)$ và $(1, \lambda_2)$. Bằng cách nào đi nữa, sự phân rã trong $y(t)$ đến từ $e^{-t}$ và $e^{-3t}$. Với hệ số không đổi, giải tích dẫn đến đại số tuyến tính $Ax = \lambda x$.

**Lưu ý** Trong đại số tuyến tính, mối nguy hiểm nghiêm trọng là thiếu vectơ riêng. Các vectơ riêng $(1, \lambda_1)$ và $(1, \lambda_2)$ của chúng ta sẽ giống nhau nếu $\lambda_1 = \lambda_2$. Khi đó chúng ta không thể chéo hóa $A$. Trong trường hợp này chúng ta chưa có hai nghiệm độc lập cho $du/dt = Au$.

Trong phương trình vi phân, mối nguy hiểm cũng là một $\lambda$ bị lặp lại. Sau $y = e^{\lambda t}$, một nghiệm thứ hai phải được tìm thấy. Hóa ra nó là $y = te^{\lambda t}$. Nghiệm "không thuần túy" (với một $t$ thừa) này xuất hiện trong ma trận mũ $e^{At}$. Ví dụ 4 đã cho thấy cách thức.

**6.3 B** Tìm các trị riêng và vectơ riêng của $A$. Sau đó viết $u(0) = (0, 2\sqrt{2}, 0)$ thành một tổ hợp của các vectơ riêng. Giải cả hai phương trình $u' = Au$ và $u'' = Au$:

$$\frac{du}{dt} = \begin{bmatrix} -2 & 1 & 0 \\ 1 & -2 & 1 \\ 0 & 1 & -2 \end{bmatrix} u \quad \text{và} \quad \frac{d^2u}{dt^2} = \begin{bmatrix} -2 & 1 & 0 \\ 1 & -2 & 1 \\ 0 & 1 & -2 \end{bmatrix} u \quad \text{với} \quad \frac{du}{dt}(0) = 0.$$

$u' = Au$ giống như phương trình truyền nhiệt $\partial u / \partial t = \partial^2 u / \partial x^2$.

Nghiệm của nó $u(t)$ sẽ suy giảm ($A$ có các trị riêng âm).

$u'' = Au$ giống như phương trình truyền sóng $\partial^2 u / \partial t^2 = \partial^2 u / \partial x^2$.

Nghiệm của nó sẽ dao động (căn bậc hai của $\lambda$ là số ảo).

**Lời giải** Các trị riêng và vectơ riêng đến từ $\det(A - \lambda I) = 0$:

$$\det(A - \lambda I) = \begin{vmatrix} -2 - \lambda & 1 & 0 \\ 1 & -2 - \lambda & 1 \\ 0 & 1 & -2 - \lambda \end{vmatrix} = (-2 - \lambda)[(-2 - \lambda)^2 - 2] = 0.$$

Một trị riêng là $\lambda = -2$, khi $-2 - \lambda$ bằng không. Thừa số còn lại là $\lambda^2 + 4\lambda + 2$, vì vậy các trị riêng khác (cũng là số thực và âm) là $\lambda = -2 \pm \sqrt{2}$. Tìm các vectơ riêng:

$$\lambda = -2 \quad (A + 2I)x = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} \quad \text{cho } x_1 = \begin{bmatrix} 1 \\ 0 \\ -1 \end{bmatrix}$$

$$\lambda = -2 - \sqrt{2} \quad (A - \lambda I)x = \begin{bmatrix} \sqrt{2} & 1 & 0 \\ 1 & \sqrt{2} & 1 \\ 0 & 1 & \sqrt{2} \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} \quad \text{cho } x_2 = \begin{bmatrix} 1 \\ -\sqrt{2} \\ 1 \end{bmatrix}$$

$$\lambda = -2 + \sqrt{2} \quad (A - \lambda I)x = \begin{bmatrix} -\sqrt{2} & 1 & 0 \\ 1 & -\sqrt{2} & 1 \\ 0 & 1 & -\sqrt{2} \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} \quad \text{cho } x_3 = \begin{bmatrix} 1 \\ \sqrt{2} \\ 1 \end{bmatrix}$$

Các vectơ riêng *trực giao* với nhau (được chứng minh trong Phần 6.4 đối với mọi ma trận đối xứng). Cả ba $\lambda_i$ đều âm. Ma trận $A$ này là *xác định âm (negative definite)* và $e^{At}$ suy giảm đến 0 (sự ổn định).

Vectơ xuất phát $u(0) = (0, 2\sqrt{2}, 0)$ là $x_3 - x_2$. Nghiệm là $u(t) = e^{\lambda_3 t} x_3 - e^{\lambda_2 t} x_2$.

**Phương trình truyền nhiệt** Trong Hình 6.6a, nhiệt độ tại tâm bắt đầu ở $2\sqrt{2}$. Nhiệt khuếch tán vào các ô kề cạnh và sau đó tới các ô bên ngoài (được giữ đóng băng ở $0^\circ$). Tốc độ dòng nhiệt giữa các ô là sự chênh lệch nhiệt độ. Từ ô 2, nhiệt chảy sang trái và phải ở tốc độ $u_1 - u_2$ và $u_3 - u_2$. Vậy dòng nhiệt chảy ra là $u_1 - 2u_2 + u_3$ trong hàng thứ hai của $Au$.

**Phương trình truyền sóng** $d^2u/dt^2 = Au$ có cùng các vectơ riêng $x$. Nhưng bây giờ các trị riêng $\lambda$ dẫn đến **các dao động** $e^{i\omega t} x$ và $e^{-i\omega t} x$. Các tần số (frequencies) đến từ $\omega^2 = -\lambda$:

$$\frac{d^2}{dt^2}(e^{i\omega t} x) = A(e^{i\omega t} x) \quad \text{trở thành} \quad (i\omega)^2 e^{i\omega t} x = \lambda e^{i\omega t} x \quad \text{và} \quad \omega^2 = -\lambda.$$

Có hai căn bậc hai của $-\lambda$, vì vậy chúng ta có $e^{i\omega t} x$ và $e^{-i\omega t} x$. Với ba vectơ riêng, điều này tạo ra sáu nghiệm cho $u'' = Au$. Một tổ hợp sẽ khớp với sáu thành phần của $u(0)$ và $u'(0)$. Vì $u' = 0$ trong bài toán này, $e^{i\omega t} x$ và $e^{-i\omega t} x$ tạo ra $2 \cos \omega t \, x$.

Hình 6.6: Nhiệt khuếch tán ra khỏi ô 2 (trái). Sóng truyền đi từ ô 2 (phải).

**6.3 C** Giải bốn phương trình $da/dt = 0, db/dt = a, dc/dt = 2b, dz/dt = 3c$ theo thứ tự đó bắt đầu từ $u(0) = (a(0), b(0), c(0), z(0))$. Giải cùng những phương trình này bằng ma trận mũ trong $u(t) = e^{At}u(0)$.

**Bốn phương trình** $\lambda = \mathbf{0}, \mathbf{0}, \mathbf{0}, \mathbf{0}$
$$\frac{d}{dt} \begin{bmatrix} a \\ b \\ c \\ z \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 2 & 0 & 0 \\ 0 & 0 & 3 & 0 \end{bmatrix} \begin{bmatrix} a \\ b \\ c \\ z \end{bmatrix} \quad \text{là} \quad \frac{du}{dt} = Au.$$

**Các trị riêng nằm trên đường chéo**

Đầu tiên tìm $A^2, A^3, A^4$ và $e^{At} = I + At + \frac{1}{2}(At)^2 + \frac{1}{6}(At)^3$. Tại sao chuỗi dừng lại? Tại sao $(e^A)(e^A) = (e^{2A})$ là đúng? **Luôn luôn $e^{As}$ nhân $e^{At}$ bằng $e^{A(s+t)}$.**

**Lời giải 1** Tích phân $da/dt = 0$, sau đó $db/dt = a$, sau đó $dc/dt = 2b$ và $dz/dt = 3c$:

$$a(t) = a(0)$$
$$b(t) = ta(0) + b(0)$$
$$c(t) = t^2a(0) + 2tb(0) + c(0)$$
$$z(t) = t^3a(0) + 3t^2b(0) + 3tc(0) + z(0)$$
Ma trận $4 \times 4$ đang nhân với $a(0), b(0), c(0), z(0)$ để tạo ra $a(t), b(t), c(t), z(t)$ phải là cùng một $e^{At}$ như dưới đây.

**Lời giải 2** Các lũy thừa của $A$ (tam giác thực sự) tất cả đều bằng 0 sau $A^3$.

$$A = \begin{bmatrix} 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 2 & 0 & 0 \\ 0 & 0 & 3 & 0 \end{bmatrix} \quad A^2 = \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 2 & 0 & 0 & 0 \\ 0 & 6 & 0 & 0 \end{bmatrix} \quad A^3 = \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 6 & 0 & 0 & 0 \end{bmatrix} \quad A^4 = \mathbf{0}$$

Các đường chéo dịch xuống ở mỗi bước. Do đó chuỗi cho $e^{At}$ dừng lại sau bốn số hạng:

**Cùng $e^{At}$ như trong Lời giải 1**
$$e^{At} = I + At + \frac{(At)^2}{2} + \frac{(At)^3}{6} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ t & 1 & 0 & 0 \\ t^2 & 2t & 1 & 0 \\ t^3 & 3t^2 & 3t & 1 \end{bmatrix}$$

Bình phương của $e^A$ là $e^{2A}$. Nhưng $e^A e^B$ và $e^B e^A$ và $e^{A+B}$ có thể hoàn toàn khác nhau.

# **Tập bài tập 6.3 (Problem Set 6.3)**

**1** Tìm hai $\lambda$ và $x$ sao cho $u = e^{\lambda t}x$ giải phương trình

$$\frac{d\mathbf{u}}{dt} = \begin{bmatrix} 4 & 3 \\ 0 & 1 \end{bmatrix} \mathbf{u}.$$

Tổ hợp nào $u = c_1 e^{\lambda_1 t} x_1 + c_2 e^{\lambda_2 t} x_2$ bắt đầu từ $u(0) = (5, -2)$?

**2** Giải Bài tập 1 cho $u = (y, z)$ bằng phép thế ngược (back substitution), $z$ trước $y$:

| Giải $\frac{dz}{dt} = z$ từ $z(0) = -2$. | Sau đó giải $\frac{dy}{dt} = 4y + 3z$ từ $y(0) = 5$. |
|----------------------------------------------|--------------------------------------------------------|

Nghiệm cho $y$ sẽ là một tổ hợp của $e^{4t}$ và $e^t$. Các $\lambda$ là 4 và 1.

- **3** (a) Nếu mỗi cột của $A$ có tổng bằng 0, tại sao $\lambda = 0$ là một trị riêng?
  - (b) Với đường chéo âm và các phần tử ngoài đường chéo dương có tổng bằng không, $u' = Au$ sẽ là một phương trình Markov "liên tục". Tìm các trị riêng và vectơ riêng, và *trạng thái ổn định (steady state)* khi $t \to \infty$:

| Giải | $\frac{du}{dt} = \begin{bmatrix} -2 & 3 \\ 2 & -3 \end{bmatrix} u$ với $u(0) = \begin{bmatrix} 4 \\ 1 \end{bmatrix}$. $u(\infty)$ là gì? |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------|

**4** Một cánh cửa được mở giữa các phòng chứa $v(0) = 30$ người và $w(0) = 10$ người. Sự di chuyển giữa các phòng tỉ lệ thuận với hiệu $v - w$:

| $\frac{dv}{dt} = w - v$ | và | $\frac{dw}{dt} = v - w$ |
|-------------------------|-----|-------------------------|

Chứng minh rằng tổng $v + w$ là không đổi (40 người). Tìm ma trận trong $du/dt = Au$ cùng các trị riêng và vectơ riêng của nó. $v$ và $w$ tại $t = 1$ và $t = \infty$ là bao nhiêu?

**5** Đảo ngược sự khuếch tán của con người trong Bài 4 thành $du/dt = -Au$:

| $\frac{dv}{dt} = v - w$ | và | $\frac{dw}{dt} = w - v$ |
|-------------------------|-----|-------------------------|

Tổng $v + w$ vẫn không đổi. Các $\lambda$ bị thay đổi như thế nào bây giờ khi $A$ được đổi thành $-A$? Nhưng hãy chứng minh rằng $v(t)$ tăng lên vô cực từ $v(0) = 30$.

**6** $A$ có các trị riêng thực nhưng $B$ có các trị riêng phức:

$$A = \begin{bmatrix} a & 1 \\ 1 & a \end{bmatrix} \quad B = \begin{bmatrix} b & -1 \\ 1 & b \end{bmatrix} \quad (a \text{ và } b \text{ là các số thực})$$

Tìm các điều kiện đối với $a$ và $b$ để mọi nghiệm của $du/dt = Au$ và $dv/dt = Bv$ tiến đến 0 khi $t \to \infty$: $\text{Re }\lambda < 0$ đối với mọi trị riêng.

**7** Giả sử $P$ là ma trận chiếu lên đường thẳng $45^\circ$ $y = x$ trong $\mathbb{R}^2$. Các trị riêng của nó là gì? Nếu $du/dt = -Pu$ (chú ý dấu trừ) bạn có thể tìm giới hạn của $u(t)$ tại $t = \infty$ bắt đầu từ $u(0) = (3, 1)$ không?

**8** Quần thể thỏ cho thấy sự tăng trưởng nhanh (từ $6r$) nhưng bị sói ăn thịt (từ $-2w$). Quần thể sói luôn tăng trong mô hình này ($-w^2$ sẽ kiểm soát sói):

| $\frac{dr}{dt} = 6r - 2w$ | và | $\frac{dw}{dt} = 2r + w.$ |
|---------------------------|-----|---------------------------|

Tìm các trị riêng và vectơ riêng. Nếu $r(0) = w(0) = 30$ thì quần thể tại thời điểm $t$ là bao nhiêu? Sau một thời gian dài, tỉ lệ thỏ trên sói là bao nhiêu?

**9** (a) Viết $(4, 0)$ dưới dạng một tổ hợp $c_1 x_1 + c_2 x_2$ của hai vectơ riêng này của $A$:

| $\begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix} \begin{bmatrix} 1 \\ i \end{bmatrix} = i \begin{bmatrix} 1 \\ i \end{bmatrix}$ | $\begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix} \begin{bmatrix} 1 \\ -i \end{bmatrix} = -i \begin{bmatrix} 1 \\ -i \end{bmatrix}$ |
|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|

- (b) Nghiệm của $du/dt = Au$ bắt đầu từ $(4, 0)$ là $c_1 e^{it} x_1 + c_2 e^{-it} x_2$. Thay $e^{it} = \cos t + i \sin t$ và $e^{-it} = \cos t - i \sin t$ để tìm $u(t)$.

### Các câu hỏi 10-13 rút gọn các phương trình bậc hai thành các hệ bậc nhất cho $(y, y')$.

**10** Tìm $A$ để thay đổi phương trình vô hướng $y'' = 5y' + 4y$ thành một phương trình vectơ cho $u = (y, y')$:

$$\frac{du}{dt} = \begin{bmatrix} y' \\ y'' \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 4 & 5 \end{bmatrix} \begin{bmatrix} y \\ y' \end{bmatrix} = Au.$$

Các trị riêng của $A$ là gì? Tìm chúng bằng cách thay $y = e^{\lambda t}$ vào $y'' = 5y' + 4y$.

**11** Nghiệm của $y'' = 0$ là một đường thẳng $y = C + Dt$. Chuyển đổi sang một phương trình ma trận:

$$\frac{d}{dt} \begin{bmatrix} y \\ y' \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} y \\ y' \end{bmatrix} \text{ có nghiệm là } \begin{bmatrix} y \\ y' \end{bmatrix} = e^{At} \begin{bmatrix} y(0) \\ y'(0) \end{bmatrix}.$$

Ma trận $A$ này có $\lambda = 0, 0$ và nó không thể chéo hóa được. Tìm $A^2$ và tính $e^{At} = I + At + \frac{1}{2}A^2 t^2 + \dots$. Nhân $e^{At}$ của bạn với $(y(0), y'(0))$ để kiểm tra đường thẳng $y(t) = y(0) + y'(0)t$.

**12** Thay $y = e^{\lambda t}$ vào $y'' = 6y' - 9y$ để thấy rằng $\lambda = 3$ là một nghiệm kép. Đây là rắc rối; chúng ta cần một nghiệm thứ hai sau $e^{3t}$. Phương trình ma trận là

$$\frac{d}{dt} \begin{bmatrix} y \\ y' \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -9 & 6 \end{bmatrix} \begin{bmatrix} y \\ y' \end{bmatrix}.$$

Chứng tỏ rằng ma trận này có $\lambda = 3, 3$ và chỉ có một đường thẳng vectơ riêng. *Ở đây cũng là rắc rối.* Chứng tỏ rằng nghiệm thứ hai cho $y'' = 6y' - 9y$ là $y = t e^{3t}$.

- **13** (a) Viết hai hàm quen thuộc giải phương trình $d^2y/dt^2 = -9y$. Hàm nào bắt đầu với $y(0) = 3$ và $y'(0) = 0$?
  - (b) Phương trình bậc hai này $y'' = -9y$ tạo ra một phương trình vectơ $u' = Au$:

$$u = \begin{bmatrix} y \\ y' \end{bmatrix} \quad \frac{du}{dt} = \begin{bmatrix} y' \\ y'' \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -9 & 0 \end{bmatrix} \begin{bmatrix} y \\ y' \end{bmatrix} = Au.$$

Tìm $u(t)$ bằng cách sử dụng các trị riêng và vectơ riêng của $A$: $u(0) = (3, 0)$.

**14** Ma trận trong câu hỏi này là lệch đối xứng ($A^T = -A$):

$$\frac{du}{dt} = \begin{bmatrix} 0 & c & -b \\ -c & 0 & a \\ b & -a & 0 \end{bmatrix} u \quad \text{hoặc} \quad \begin{bmatrix} u'_1 = cu_2 - bu_3 \\ u'_2 = au_3 - cu_1 \\ u'_3 = bu_1 - au_2 \end{bmatrix}.$$

- (a) Đạo hàm của $\|u(t)\|^2 = u_1^2 + u_2^2 + u_3^2$ là $2u_1 u_1' + 2u_2 u_2' + 2u_3 u_3'$. Thay $u_1', u_2', u_3'$ để nhận được 0. Khi đó $\|u(t)\|^2$ vẫn bằng $\|u(0)\|^2$.
- (b) *Khi $A$ lệch đối xứng,* $Q = e^{At}$ là *trực giao*. Chứng minh $Q^T = e^{-At}$ từ chuỗi cho $Q = e^{At}$. Từ đó $Q^T Q = I$.

**15** Một nghiệm cụ thể của $du/dt = Au - b$ là $u_p = A^{-1}b$, nếu $A$ có thể nghịch đảo. Các nghiệm thông thường của $du/dt = Au$ mang lại $u_n$. Tìm nghiệm hoàn chỉnh $u = u_p + u_n$:

| (a)   | $\frac{du}{dt} = u - 4$ | (b) | $\frac{du}{dt} = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} u - \begin{bmatrix} 4 \\ 6 \end{bmatrix}$ |
|-------|-------------------------|-----|---------------------------------------------------------------------------------------------------------|

**16** Nếu $c$ không phải là một trị riêng của $A$, hãy thế $u = e^{ct}v$ và tìm một nghiệm cụ thể cho $du/dt = Au - e^{ct}b$. Nó bị phá vỡ như thế nào khi $c$ là một trị riêng của $A$? "Không gian null" của $du/dt = Au$ chứa các nghiệm thông thường $e^{\lambda_i t} x_i$.

**17** Tìm một ma trận $A$ để minh họa cho mỗi khu vực không ổn định trong Hình 6.5:

| (a) | $\lambda_1 < 0$ và $\lambda_2 > 0$ | (b) | $\lambda_1 > 0$ và $\lambda_2 > 0$ | (c) | $\lambda = a \pm ib$ với $a > 0$ |
|-----|-------------------------------------|-----|-------------------------------------|-----|-----------------------------------|

# Các câu hỏi 18-27 là về ma trận mũ $e^{At}$.

**18** Viết năm số hạng của chuỗi vô hạn cho $e^{At}$. Lấy đạo hàm theo $t$ của mỗi số hạng. Chứng minh rằng bạn có bốn số hạng của $Ae^{At}$. Kết luận: $e^{At}u_0$ giải $u' = Au$.

**19** Ma trận $B = \begin{bmatrix} 0 & -1 \\ 0 & 0 \end{bmatrix}$ có $B^2 = 0$. Tìm $e^{Bt}$ từ một chuỗi vô hạn (ngắn). Kiểm tra xem đạo hàm của $e^{Bt}$ có phải là $B e^{Bt}$ không.

**20** Bắt đầu từ $u(0)$ nghiệm tại thời điểm $T$ là $e^{AT}u(0)$. Đi thêm một thời gian $t$ để đạt tới $e^{At} e^{AT} u(0)$. Nghiệm này tại thời điểm $t + T$ cũng có thể được viết là $e^{A(t+T)}u(0)$. Kết luận: $e^{At}$ nhân $e^{AT}$ bằng \_\_\_\_\_\_\_\_\_\_\_\_\_\_.

**21** Viết $A = \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}$ dưới dạng $X \Lambda X^{-1}$. Tìm $e^{At}$ từ $X e^{\Lambda t} X^{-1}$.

- **22** Nếu $A^2 = A$ hãy chứng minh rằng chuỗi vô hạn tạo ra $e^{At} = I + (e^t - 1)A$. Đối với $A = \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}$ trong Bài 21 điều này cho ra $e^{At} = \_\_\_\_\_\_$.
- **23** Thông thường $e^A e^B$ khác với $e^B e^A$. Chúng đều khác với $e^{A+B}$. Kiểm tra điều này bằng cách sử dụng các Bài 21-22 và 19. (Nếu $AB = BA$, cả ba đều giống nhau.)

| $A = \begin{bmatrix} 1 & 4 \\ 0 & 0 \end{bmatrix}$ | $B = \begin{bmatrix} 0 & -4 \\ 0 & 0 \end{bmatrix}$ | $A + B = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ |
|----------------------------------------------------|-----------------------------------------------------|--------------------------------------------------------|

**24** Viết $A = \begin{bmatrix} 1 & 1 \\ 0 & 2 \end{bmatrix}$ thành $X\Lambda X^{-1}$. Nhân $X e^{\Lambda t}X^{-1}$ để tìm ma trận mũ $e^{At}$. Kiểm tra $e^{At}$ và đạo hàm của $e^{At}$ khi $t = 0$.

**25** Đưa $A = \begin{bmatrix} 1 & 3 \\ 0 & 0 \end{bmatrix}$ vào chuỗi vô hạn để tìm $e^{At}$. Đầu tiên tính $A^2$ và $A^n$:

$$e^{At} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} + \begin{bmatrix} t & 3t \\ 0 & 0 \end{bmatrix} + \frac{1}{2} \begin{bmatrix} t^2 & 3t^2 \\ 0 & 0 \end{bmatrix} + \dots = \begin{bmatrix} e^t & 3e^t-3 \\ 0 & 1 \end{bmatrix}.$$

- **26** (Khuyến nghị) Đưa ra hai lý do tại sao ma trận mũ $e^{At}$ không bao giờ là ma trận suy biến:
  - (a) Viết ma trận nghịch đảo của nó.
  - (b) Tại sao các trị riêng này lại khác không? Nếu $Ax = \lambda x$ thì $e^{At}x = \_\_\_\_\_\_ x$.

**27** Tìm một nghiệm $x(t), y(t)$ trở nên lớn khi $t \to \infty$. Để tránh sự không ổn định này, một nhà khoa học đã đổi chỗ hai phương trình:

| $dx/dt = 0x - 4y$  | trở thành | $dy/dt = -2x + 2y$ |
|--------------------|---------|--------------------|
| $dy/dt = -2x + 2y$ |         | $dx/dt = 0x - 4y.$ |

Bây giờ ma trận $\begin{bmatrix} -2 & 2 \\ 0 & -4 \end{bmatrix}$ là ổn định. Nó có các trị riêng âm. Làm sao có thể như vậy được?

# **Bài tập Thử thách (Challenge Problems)**

**28** Căn giữa $y'' = -y$ trong Ví dụ 3 sẽ tạo ra $Y_{n+1} - 2Y_n + Y_{n-1} = -(\Delta t)^2 Y_n$. Điều này có thể được viết thành một phương trình sai phân một bước cho $U = (Y, Z)$:

| $Y_{n+1} = Y_n + \Delta t Z_n$ | $\begin{bmatrix} 1 & 0 \\ \Delta t & 1 \end{bmatrix} \begin{bmatrix} Y_{n+1} \\ Z_{n+1} \end{bmatrix} = \begin{bmatrix} 1 & \Delta t \\ 0 & 1 \end{bmatrix} \begin{bmatrix} Y_n \\ Z_n \end{bmatrix}$ |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Nghịch đảo ma trận ở vế trái để viết biểu thức này dưới dạng $U_{n+1} = AU_n$. Chứng minh rằng $\det A = 1$. Chọn bước thời gian lớn $\Delta t = 1$ và tìm các trị riêng $\lambda_1$ và $\lambda_2 = \bar{\lambda}_1$ của $A$:

$$A = \begin{bmatrix} 1 & 1 \\ -1 & 0 \end{bmatrix}$$
có $|\lambda_1| = |\lambda_2| = 1$. Chứng minh rằng $A^6$ chính xác bằng $I$.

**29** Lựa chọn căn giữa đó *(phương pháp nhảy ếch - leapfrog method)* trong Bài 28 rất thành công đối với các bước thời gian nhỏ $\Delta t$. Nhưng hãy tìm các trị riêng của $A$ với $\Delta t = \sqrt{2}$ và $2$:

| $A = \begin{bmatrix} 1 & \sqrt{2} \\ -\sqrt{2} & -1 \end{bmatrix}$ | và | $A = \begin{bmatrix} 1 & 2 \\ -2 & 3 \end{bmatrix}$ |
|--------------------------------------------------------------------|-----|-----------------------------------------------------|

Cả hai ma trận đều có $|\lambda_1| = 1$. Hãy tính $A^4$ trong cả hai trường hợp và tìm các vectơ riêng của $A$. Giá trị thứ hai $\Delta t = 2$ nằm ở ranh giới của sự mất ổn định. Bất kỳ bước thời gian $\Delta t > 2$ nào cũng sẽ dẫn đến $|\lambda_1| > 1$, và các lũy thừa trong $U_n = A^n U_0$ sẽ bùng nổ.

*Lưu ý* Bạn có thể nói rằng không ai lại tính toán với $\Delta t > 2$. Nhưng nếu một nguyên tử dao động với $y'' = -1000000y$, thì $\Delta t > 0.0002$ sẽ gây ra sự mất ổn định. Phương pháp nhảy ếch có một giới hạn ổn định rất nghiêm ngặt. $Y_{n+1} = Y_n + 3Z_n$ và $Z_{n+1} = Z_n - 3Y_{n+1}$ sẽ bùng nổ vì $\Delta t = 3$ là quá lớn. Ma trận có $|\lambda_1| > 1$.

**30** Một ý tưởng tốt khác cho $y'' = -y$ là phương pháp hình thang (nửa bước tiến / nửa bước lùi). *Đây có thể là cách tốt nhất để giữ cho* $(Y_n, Z_n)$ *nằm hoàn toàn trên một vòng tròn.*

| Hình thang | $\begin{bmatrix} 1 & -\Delta t/2 \\ \Delta t/2 & 1 \end{bmatrix} \begin{bmatrix} Y_{n+1} \\ Z_{n+1} \end{bmatrix} = \begin{bmatrix} 1 & \Delta t/2 \\ -\Delta t/2 & 1 \end{bmatrix} \begin{bmatrix} Y_n \\ Z_n \end{bmatrix}$ |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|

- (a) Nghịch đảo ma trận bên trái để viết phương trình này dưới dạng $U_{n+1} = AU_n$. *Chứng minh rằng* $A$ *là một ma trận trực giao:* $A^T A = I$. **Những điểm này** $U_n$ **không bao giờ rời khỏi vòng tròn.** $A = (I - B)^{-1}(I + B)$ luôn là một ma trận trực giao nếu $B^T = -B$.
- (b) (Tùy chọn MATLAB) Thực hiện 32 bước từ $U_0 = (1, 0)$ đến $U_{32}$ với $\Delta t = 2\pi/32$. Liệu $U_{32} = U_0$? Tôi nghĩ rằng có một sai số nhỏ.

**31** *Cosin của một ma trận* được định nghĩa giống như $e^A$, bằng cách sao chép chuỗi cho $\cos t$:

$$\cos t = 1 - \frac{1}{2!}t^2 + \frac{1}{4!}t^4 - \dots \quad \cos A = I - \frac{1}{2!}A^2 + \frac{1}{4!}A^4 - \dots$$

(a) Nếu $Ax = \lambda x$, hãy nhân mỗi số hạng với $x$ để tìm trị riêng của $\cos A$.

(b) Tìm các trị riêng của $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$ với các vectơ riêng $(1, 1)$ và $(1, -1)$. Từ các trị riêng và vectơ riêng của $\cos A$, hãy tìm ma trận $C = \cos A$.

- (c) Đạo hàm bậc hai của $\cos(At)$ là $-A^2 \cos(At)$.

$$u(t) = \cos(At)u(0)$$
giải phương trình $\frac{d^2u}{dt^2} = -A^2u$ bắt đầu từ $u'(0) = 0$.

Xây dựng $u(t) = \cos(At)u(0)$ bằng ba bước thông thường cho ma trận $A$ cụ thể đó:

- **1.** Khai triển $u(0) = (4, 2) = c_1 x_1 + c_2 x_2$ theo các vectơ riêng.
- **2.** Nhân những vectơ riêng đó với \_\_\_\_\_\_ và \_\_\_\_\_\_ (thay vì $e^{\lambda t}$).
- **3.** Cộng các nghiệm lại $u(t) = c_1 \_\_\_\_\_\_ x_1 + c_2 \_\_\_\_\_\_ x_2$.

- **32** Giải thích một trong ba phép chứng minh sau cho việc bình phương của $e^A$ là $e^{2A}$.
  - **1.** Giải với $e^A$ từ $t = 0$ đến 1 và sau đó từ 1 đến 2 đồng tình với $e^{2A}$ từ 0 đến 2.
  - **2.** Bình phương của chuỗi $(I + A + \frac{1}{2}A^2 + \dots)^2$ khớp với $I + 2A + \frac{1}{2}(2A)^2 + \dots = e^{2A}$.
  - **3.** Nếu $A$ có thể chéo hóa thì $(X e^{\Lambda} X^{-1})(X e^{\Lambda} X^{-1}) = X e^{2\Lambda} X^{-1}$.

# **Ghi chú về một khóa học Phương trình Vi phân**

Chắc chắn các phương trình tuyến tính hệ số không đổi là dễ giải nhất. Phần 6.3 này của cuốn sách cho bạn thấy một phần của một khóa học về phương trình vi phân, nhưng còn nhiều hơn thế:

- **1.** Phương trình bậc hai $mu'' + bu' + ku = 0$ có tầm quan trọng lớn trong các ứng dụng. Các số mũ $\lambda$ trong các nghiệm $u = e^{\lambda t}$ giải phương trình $m\lambda^2 + b\lambda + k = 0$. Hệ số cản $b$ rất quan trọng:
**Giảm chấn dưới mức (Underdamping)** $b^2 < 4mk$
**Giảm chấn tới hạn (Critical damping)** $b^2 = 4mk$
**Giảm chấn quá mức (Overdamping)** $b^2 > 4mk$
Điều này quyết định liệu $\lambda_1$ và $\lambda_2$ là nghiệm thực, nghiệm kép hay nghiệm phức. Với các $\lambda$ phức, nghiệm $u(t)$ dao động khi nó suy giảm.
- **2.** Các phương trình của chúng ta không có số hạng cưỡng bức (forcing term) $f(t)$. Chúng ta đang tìm "nghiệm không gian null" (nullspace solution). Đối với $u_n(t)$, chúng ta cần cộng thêm một nghiệm cụ thể $u_p(t)$ để cân bằng lực $f(t)$:

**Đầu vào $f(s)$ tại các thời điểm $s$ nhân với Hệ số tăng trưởng $e^{A(t-s)}$ Cộng các đầu ra tại thời điểm $t$**
$$u_{\text{particular}} = \int_0^t e^{A(t-s)} f(s) ds.$$

Nghiệm này cũng có thể được khám phá và nghiên cứu bằng *biến đổi Laplace* — đó là cách thức đã được thiết lập để chuyển đổi phương trình vi phân tuyến tính thành đại số tuyến tính.

Trong các ứng dụng thực tế, các phương trình vi phân phi tuyến được giải bằng phương pháp số. Một phương pháp tiêu chuẩn có độ chính xác tốt là "Runge-Kutta" — được đặt theo tên của những người khám phá ra nó. Việc phân tích có thể tìm ra các nghiệm hằng số cho $du/dt = f(u)$. Đó là các nghiệm $u(t) = Y$ với $f(Y) = 0$ và $du/dt = 0$: *không có sự di chuyển*. Chúng ta cũng có thể hiểu sự ổn định hoặc mất ổn định ở gần $u = Y$. Càng xa $Y$, máy tính càng phải tiếp quản.

Khóa học cơ bản này là chủ đề trong giáo trình của tôi (đi kèm với cuốn này) về *Phương trình Vi phân và Đại số Tuyến tính*: **math.mit.edu/dela**.

# **6.4 Ma trận Đối xứng (Symmetric Matrices)**

**1** Một ma trận đối xứng $S$ có $n$ **trị riêng thực** $\lambda_i$ và $n$ **vectơ riêng trực chuẩn** $q_1, \dots, q_n$.
**2** Mọi ma trận thực đối xứng $S$ đều có thể chéo hóa: $S = Q\Lambda Q^{-1} = Q\Lambda Q^T$.
**3** Số lượng các trị riêng dương của $S$ bằng số lượng các phần tử chốt (pivots) dương.
**4** Các ma trận phản đối xứng $A = -A^T$ có các $\lambda$ *thuần ảo* và *các vectơ riêng $q$ trực chuẩn (phức)*.
**5** Phần 9.2 giải thích tại sao phép kiểm tra $S = S^T$ trở thành $\bar{S} = S^T$ đối với *các ma trận phức*. $S = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} = S^T$ có các $\lambda$ thực là $1, -1$. $A = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix} = -A^T$ có $\lambda = i, -i$.

Không quá lời khi nói rằng ma trận đối xứng $S$ là ma trận quan trọng nhất mà thế giới từng thấy - trong lý thuyết đại số tuyến tính và cả trong các ứng dụng. Chúng ta sẽ đi ngay vào câu hỏi then chốt về tính đối xứng. Không chỉ là câu hỏi, mà còn là câu trả lời gồm hai phần.

*Điều gì đặc biệt về $Sx = \lambda x$ khi $S$ đối xứng?*

Chúng ta tìm kiếm những tính chất đặc biệt của các trị riêng $\lambda$ và các vectơ riêng $x$ khi $S = S^T$.

Phép chéo hóa $S = X\Lambda X^{-1}$ sẽ phản ánh tính đối xứng của $S$. Chúng ta nhận được một vài gợi ý bằng cách lấy chuyển vị để có $S^T = (X^{-1})^T \Lambda X^T$. Chúng giống nhau vì $S = S^T$. Có thể nào $X^{-1}$ trong dạng đầu tiên bằng với $X^T$ trong dạng thứ hai không? Khi đó $X^T X = I$. Điều đó làm cho mỗi vectơ riêng trong $X$ trực giao với các vectơ riêng khác khi $S = S^T$. Đây là những sự thật then chốt:

- **1. Một ma trận đối xứng chỉ có** *các trị riêng thực.*
- **2. Các** *vectơ riêng* **có thể được chọn sao cho** *trực chuẩn (orthonormal).*

$n$ vectơ riêng trực chuẩn đó đi vào các cột của $X$. Mọi ma trận đối xứng đều có thể chéo hóa. *Ma trận vectơ riêng $X$ của nó trở thành một ma trận trực giao* $Q$. Các ma trận trực giao có $Q^{-1} = Q^T$ — điều mà chúng ta nghi ngờ về ma trận vectơ riêng là đúng. Để ghi nhớ điều đó, chúng ta viết $Q$ thay vì $X$, khi chúng quy định các vectơ riêng trực chuẩn.

Tại sao chúng ta sử dụng từ "chọn"? Bởi vì các vectơ riêng không *bắt buộc* phải là các vectơ đơn vị. Độ dài của chúng là do chúng ta quyết định. Chúng ta sẽ chọn các vectơ đơn vị — các vectơ riêng có độ dài bằng 1, chúng trực chuẩn chứ không chỉ là trực giao. Khi đó $A = X\Lambda X^{-1}$ ở dạng đặc biệt và cụ thể của nó là $S = Q\Lambda Q^T$ đối với các ma trận đối xứng.

**(Định lý Phổ - Spectral Theorem)** Mọi ma trận đối xứng đều có phân tích $S = Q\Lambda Q^T$ với các trị riêng thực trong $\Lambda$ và các vectơ riêng trực chuẩn nằm ở các cột của $Q$:

| Chéo hóa đối xứng | $S = Q\Lambda Q^{-1} = Q\Lambda Q^T$ | $Q^{-1} = Q^T$ |
|---------------------------|--------------------------------------|----------------|

Thật dễ dàng để thấy rằng $Q\Lambda Q^T$ là đối xứng. Lấy chuyển vị của nó. Bạn sẽ nhận được $(Q^T)^T \Lambda^T Q^T$, cũng chính là $Q\Lambda Q^T$ một lần nữa. Phần khó hơn là chứng minh rằng mọi ma trận đối xứng đều có các $\lambda$ thực và các $x$ trực chuẩn. Đây là *"định lý phổ"* trong toán học và *"định lý trục chính (principal axis theorem)"* trong hình học và vật lý. Chúng ta phải chứng minh nó! Không có lựa chọn nào khác. Tôi sẽ tiếp cận việc chứng minh theo ba bước:

- **1.** Bằng một ví dụ, cho thấy các $\lambda$ thực trong $\Lambda$ và các $x$ trực chuẩn trong $Q$.
- **2.** Bằng một phép chứng minh cho những sự thật đó khi không có trị riêng nào bị lặp lại.
- **3.** Bằng một phép chứng minh cho phép các trị riêng lặp lại (ở cuối phần này).

**Ví dụ 1** Tìm các $\lambda$ và các $x$ khi $S = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$ và $S - \lambda I = \begin{bmatrix} 1 - \lambda & 2 \\ 2 & 4 - \lambda \end{bmatrix}$.

**Lời giải** Định thức của $S - \lambda I$ là $\lambda^2 - 5\lambda$. Các trị riêng là 0 và 5 *(đều là số thực)*. Chúng ta có thể thấy chúng trực tiếp: $\lambda = 0$ là một trị riêng vì $S$ là ma trận suy biến, và $\lambda = 5$ khớp với *vết* dọc theo đường chéo của $S$: $0 + 5$ bằng với $1 + 4$.

Hai vectơ riêng là $(2, -1)$ và $(1, 2)$ — trực giao nhưng chưa trực chuẩn. Vectơ riêng cho $\lambda = 0$ nằm trong *không gian null* của $A$. Vectơ riêng cho $\lambda = 5$ nằm trong *không gian cột*. Chúng ta tự hỏi, tại sao không gian null và không gian cột lại vuông góc? Định lý Cơ bản nói rằng không gian null vuông góc với *không gian hàng* - chứ không phải không gian cột. Nhưng ma trận của chúng ta *đối xứng*! Không gian hàng và không gian cột của nó là giống nhau. Các vectơ riêng của nó $(2, -1)$ và $(1, 2)$ bắt buộc phải vuông góc (và chúng thực sự vuông góc).

Những vectơ riêng này có độ dài $\sqrt{5}$. Chia chúng cho $\sqrt{5}$ để nhận được các vectơ đơn vị. Đặt các vectơ riêng đơn vị đó vào các cột của $Q$. Khi đó $Q^{-1}SQ$ là $\Lambda$ và $Q^{-1} = Q^T$:

$$Q^{-1}SQ = \frac{1}{\sqrt{5}} \begin{bmatrix} 2 & 1 \\ -1 & 2 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix} \frac{1}{\sqrt{5}} \begin{bmatrix} 2 & -1 \\ 1 & 2 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 5 \end{bmatrix} = \Lambda.$$

Bây giờ đến trường hợp $n \times n$. Các $\lambda$ là số thực khi $S = S^T$ và $Sx = \lambda x$.

**Các Trị riêng Thực** Tất cả các trị riêng của một ma trận thực đối xứng đều là số thực.

*Chứng minh* Giả sử rằng $Sx = \lambda x$. Trừ khi chúng ta biết khác đi, $\lambda$ có thể là một số phức $a + ib$ ($a$ và $b$ thực). *Số phức liên hợp của nó là $\bar{\lambda} = a - ib$.* Tương tự, các thành phần của $x$ có thể là các số phức, và việc đổi dấu phần ảo của chúng sẽ tạo ra $\bar{x}$.

Điều tốt là $\bar{\lambda}$ nhân với $\bar{x}$ luôn là liên hợp của $\lambda$ nhân với $x$. Vì vậy chúng ta có thể lấy liên hợp của $Sx = \lambda x$, nhớ rằng $S$ là thực:

| $S x = \lambda x$ | dẫn tới | $S \bar{x} = \bar{\lambda} \bar{x}$ | Chuyển vị thành | $\bar{x}^T S = \bar{x}^T \bar{\lambda}$ |
|-----|-----------------|----------|-------------------------------------|--------------|

Bây giờ lấy tích vô hướng của phương trình đầu tiên với $\bar{x}^T$ và phương trình cuối cùng với $x$:

| $\bar{x}^T S x = \bar{x}^T \lambda x$ | và cũng | $\bar{x}^T S x = \bar{x}^T \bar{\lambda} x$ | (2) |
|---------------------------------------|----------|---------------------------------------------|-----|

Vế trái giống nhau nên vế phải bằng nhau. Một phương trình có $\lambda$, phương trình kia có $\bar{\lambda}$. Chúng nhân với $\bar{x}^Tx = |x_1|^2 + |x_2|^2 + \dots = \text{bình phương độ dài}$ vốn không bằng 0. *Do đó* $\lambda$ *phải bằng* $\bar{\lambda}$, và $a + ib$ bằng $a - ib$. Vậy $b = 0$ và $\lambda = a = \text{thực}$. Q.E.D.

Các vectơ riêng được tìm từ việc giải phương trình thực $(S - \lambda I)x = 0$. Vì vậy các $x$ cũng là số thực. Sự thật quan trọng là chúng vuông góc với nhau.

**Các Vectơ riêng Trực giao** Các vectơ riêng của một ma trận thực đối xứng (khi chúng tương ứng với các $\lambda$ khác nhau) luôn vuông góc với nhau.

*Chứng minh* Giả sử $Sx = \lambda_1 x$ và $Sy = \lambda_2 y$. Ở đây chúng ta giả sử rằng $\lambda_1 \neq \lambda_2$. Lấy tích vô hướng của phương trình đầu với $y$ và phương trình hai với $x$:

| $(\lambda_1 x)^T y = (Sx)^T y = x^T S^T y = x^T S y = x^T \lambda_2 y$ |
|---------------------------------------------------------------------------------------------------------------------|

Vế trái là $x^T \lambda_1 y$, vế phải là $x^T \lambda_2 y$. Vì $\lambda_1 \neq \lambda_2$, điều này chứng tỏ $x^T y = 0$. Vectơ riêng $x$ (cho $\lambda_1$) vuông góc với vectơ riêng $y$ (cho $\lambda_2$).

**Ví dụ 2** Các vectơ riêng của một ma trận đối xứng $2 \times 2$ có một dạng đặc biệt:

| Không được biết đến rộng rãi | $S = \begin{bmatrix} a & b \\ b & c \end{bmatrix}$ | có | $x_1 = \begin{bmatrix} b \\ \lambda_1 - a \end{bmatrix}$ | và | $x_2 = \begin{bmatrix} \lambda_2 - c \\ b \end{bmatrix}$ | (4) |
|------------------|----------------------------------------------------|-----|----------------------------------------------------------|-----|----------------------------------------------------------|-----|

Điều này có trong Tập bài tập. Điểm cốt lõi ở đây là $x_1$ vuông góc với $x_2$:

$$x_1^T x_2 = b(\lambda_2 - c) + (\lambda_1 - a)b = b(\lambda_1 + \lambda_2 - a - c) = 0.$$

Nó bằng không bởi vì $\lambda_1 + \lambda_2$ bằng với vết $a + c$. Do đó $x_1^T x_2 = 0$. Đôi mắt tinh tường có thể nhận thấy trường hợp đặc biệt $S = I$, khi đó $b$ và $\lambda_1 - a$ và $\lambda_2 - c$ và $x_1$ và $x_2$ đều bằng không. Khi đó $\lambda_1 = \lambda_2 = 1$ bị lặp lại. Nhưng dĩ nhiên $S = I$ có các vectơ riêng vuông góc.

*Các ma trận đối xứng $S$ có ma trận vectơ riêng $Q$ trực giao.* Hãy xem lại điều này:

| Tính đối xứng | $S = X\Lambda X^{-1}$ | trở thành | $S = Q\Lambda Q^T$ | với | $Q^T Q = I$. |
|------------------|----------------------------------------------------|-----|----------------------------------------------------------|-----|----------------------------------------------------------|

Hãy nhớ lại các bước dẫn đến kết quả tuyệt vời này (định lý phổ).

| *Section 6.2* | Viết $Ax_i = \lambda_i x_i$ dưới dạng ma trận | $AX = X\Lambda$ | hoặc | $A = X\Lambda X^{-1}$ |
|---|---|---|---|---|
| *Section 6.4* | Các vectơ trực chuẩn $x_i = q_i$ | cho ta $X = Q$ | $S = Q\Lambda Q^{-1} = Q\Lambda Q^T$ | |

$Q\Lambda Q^T$ trong phương trình (6) có các cột của $Q\Lambda$ nhân với các hàng của $Q^T$. Đây là một phép chứng minh trực tiếp.

**$S$ có các vectơ riêng chính xác**
$$Sq_i = (\lambda_1 q_1 q_1^T + \dots + \lambda_n q_n q_n^T) q_i = \lambda_i q_i$$
Vì các $q$ đó là trực chuẩn.

### **Trị riêng phức của Ma trận thực (Complex Eigenvalues of Real Matrices)**

Đối với bất kỳ ma trận thực nào, $Sx = \lambda x$ cũng đồng nghĩa với $S\bar{x} = \bar{\lambda}\bar{x}$. Đối với một ma trận đối xứng, $\lambda$ và $x$ hóa ra lại là số thực. Hai phương trình đó trở thành giống hệt nhau. Nhưng một ma trận *không đối xứng* hoàn toàn có thể tạo ra $\lambda$ và $x$ là số phức. Khi đó $A\bar{x} = \bar{\lambda}\bar{x}$ là đúng nhưng khác với $Ax = \lambda x$. Chúng ta nhận được một trị riêng phức khác (đó là $\bar{\lambda}$) và một vectơ riêng mới (đó là $\bar{x}$):

**Ví dụ 3** $A = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}$ có $\lambda_1 = \cos \theta + i\sin \theta$ và $\lambda_2 = \cos \theta - i\sin \theta$.

*Đối với ma trận thực, các $\lambda$ phức và $x$ phức đi theo "các cặp liên hợp" (conjugate pairs).*

| | | | | | |
|---|---|---|---|---|---|
| $\lambda = a + ib$ | *Nếu* | $Ax = \lambda x$ | *thì* | $A\bar{x} = \bar{\lambda}\bar{x}$ | (8) |
| $\bar{\lambda} = a - ib$ | | | | | |

Những trị riêng đó là liên hợp của nhau. Chúng là $\lambda$ và $\bar{\lambda}$. Các vectơ riêng cũng phải là $x$ và $\bar{x}$, bởi vì $A$ là ma trận thực:

$$\text{Đây là } \lambda x = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} 1 \\ -i \end{bmatrix} = (\cos \theta + i \sin \theta) \begin{bmatrix} 1 \\ -i \end{bmatrix} \quad (9)$$

$$\text{Đây là } \bar{\lambda} \bar{x} = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} 1 \\ i \end{bmatrix} = (\cos \theta - i \sin \theta) \begin{bmatrix} 1 \\ i \end{bmatrix}.$$

Những vectơ riêng $(1, -i)$ và $(1, i)$ đó là liên hợp phức bởi vì $A$ là số thực.

Đối với ma trận quay này, giá trị tuyệt đối là $|\lambda| = 1$, bởi vì $\cos^2 \theta + \sin^2 \theta = 1$. *Thực tế $|\lambda| = 1$ này đúng đối với các trị riêng của mọi ma trận trực giao $Q$.*

Chúng tôi xin lỗi vì đã để một chút số phức chen ngang vào. Chúng không thể tránh khỏi ngay cả khi ma trận là số thực. Chương 9 sẽ vượt qua các số phức $\lambda$ và các vectơ riêng phức $x$ để tiến tới ma trận phức $A$. Sau đó, bạn sẽ có toàn bộ bức tranh.

Chúng ta kết thúc với hai cuộc thảo luận tùy chọn.

# **Trị riêng và Phần tử chốt (Eigenvalues versus Pivots)**

Các trị riêng của $A$ rất khác biệt so với các phần tử chốt (pivots). Đối với các trị riêng, chúng ta giải $\det(A - \lambda I) = 0$. Đối với các chốt, chúng ta sử dụng phép khử. Mối liên hệ duy nhất cho đến nay là:

*tích của các chốt* = *định thức* = *tích của các trị riêng.*

Chúng ta đang giả sử một tập hợp đầy đủ các phần tử chốt $d_1, \dots, d_n$. Có $n$ trị riêng thực $\lambda_1, \dots, \lambda_n$. Các chốt $d$ và các trị riêng $\lambda$ không giống nhau, nhưng chúng đến từ cùng một ma trận đối xứng. Những $d$ và $\lambda$ đó có một mối liên hệ tiềm ẩn. *Đối với ma trận đối xứng, các phần tử chốt và các trị riêng có cùng dấu:*

*Số lượng trị riêng dương của* $S = S^T$ *bằng với số lượng phần tử chốt dương.* Trường hợp đặc biệt: $S$ có tất cả $\lambda_i > 0$ khi và chỉ khi tất cả các phần tử chốt đều dương.

Trường hợp đặc biệt đó là một sự thật vô cùng quan trọng đối với **ma trận xác định dương (positive definite matrices)** trong Section 6.5.

**Ví dụ 4** Ma trận đối xứng này có một trị riêng dương và một phần tử chốt dương:

| Các dấu khớp nhau | $S = \begin{bmatrix} 3 & 3 \\ 3 & 1 \end{bmatrix}$ | có chốt $1$ và $-8$<br>trị riêng $4$ và $-2$. |
|---|---|---|

Dấu của các phần tử chốt khớp với dấu của các trị riêng, một cộng và một trừ. Điều này có thể sai khi ma trận không đối xứng:

**Ngược dấu:** $B = \begin{bmatrix} 1 & 6 \\ -1 & -4 \end{bmatrix}$ có chốt $1$ và $2$, trị riêng $-1$ và $-2$.

Các phần tử trên đường chéo là một tập hợp số thứ ba và chúng ta không đề cập gì về chúng.

Dưới đây là chứng minh rằng các phần tử chốt và trị riêng có cùng dấu, khi $S = S^T$.

Bạn thấy rõ nhất khi các phần tử chốt được tách ra khỏi các hàng của $U$. Khi đó $S$ là $LDL^T$. Ma trận đường chéo $D$ gồm các chốt nằm giữa các ma trận tam giác $L$ và $L^T$:

| $\begin{bmatrix} 1 & 3 \\ 3 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 3 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 0 & -8 \end{bmatrix} \begin{bmatrix} 1 & 3 \\ 0 & 1 \end{bmatrix}$ | Đây là $S = LDL^T$. Nó đối xứng. |
|---|---|

#### *Theo dõi các trị riêng của $LDL^T$ khi $L$ tiến tới $I$. $S$ thay đổi thành $D$.*

Các trị riêng của $LDL^T$ là 4 và -2. Các trị riêng của $IDI^T$ là 1 và -8 (chính là các chốt!). Các trị riêng đang thay đổi, khi số "3" trong $L$ tiến dần về 0. Nhưng để đổi *dấu*, một trị riêng thực sẽ phải đi qua số 0. Ma trận tại thời điểm đó sẽ là suy biến. Ma trận đang thay đổi của chúng ta luôn có các chốt là 1 và -8, nên nó *không bao giờ* suy biến. Các dấu không thể thay đổi, khi các $\lambda$ tiến tới các $d$.

Chúng ta lặp lại phép chứng minh cho bất kỳ $S = LDL^T$ nào. Dịch chuyển $L$ về phía $I$, bằng cách đưa các phần tử ngoài đường chéo về 0. Các chốt không thay đổi và không bằng 0. Các trị riêng $\lambda$ của $LDL^T$ thay đổi thành các trị riêng $d$ của $IDI^T$. Vì các trị riêng này không thể vượt qua số 0 khi chúng di chuyển thành các phần tử chốt, dấu của chúng không thể thay đổi. **Các $\lambda$ và $d$ có cùng dấu.**

*Điều này kết nối hai nửa của đại số tuyến tính ứng dụng - các phần tử chốt và các trị riêng.*

# **Tất cả các Ma trận Đối xứng đều có thể Chéo hóa (All Symmetric Matrices are Diagonalizable)**

Khi không có trị riêng nào của $A$ bị lặp lại, các vectơ riêng chắc chắn là độc lập. Khi đó $A$ có thể được chéo hóa. Nhưng một trị riêng lặp lại có thể gây ra sự thiếu hụt các vectơ riêng. Điều này *đôi khi* xảy ra đối với ma trận không đối xứng. Nó *không bao giờ* xảy ra đối với ma trận đối xứng. *Luôn có đủ các vectơ riêng để chéo hóa* $S = S^T$.

Đây là một ý tưởng cho một phép chứng minh. Thay đổi $S$ một chút bằng một ma trận đường chéo $\text{diag}(c, 2c, \dots, nc)$. Nếu $c$ rất nhỏ, ma trận đối xứng mới sẽ không có trị riêng lặp lại. Khi đó chúng ta biết nó có một tập hợp đầy đủ các vectơ riêng trực chuẩn. Khi $c \rightarrow 0$, chúng ta thu được $n$ vectơ riêng trực chuẩn của ma trận $S$ ban đầu - ngay cả khi một số trị riêng của $S$ đó bị lặp lại.


*Mọi ma trận vuông $A$ đều có thể phân tích thành $QTQ^{-1}$ trong đó $T$ là ma trận tam giác trên và $Q^T = Q^{-1}$. Nếu $A$ có các trị riêng thực thì $Q$ và $T$ có thể được chọn là ma trận thực:* $Q^T Q = I$.

*Đây là Định lý Schur.* Phép chứng minh của nó sẽ có trên trang web **math.mit.edu/linearalgebra**. Ở đây tôi sẽ chỉ ra cách $T$ là một ma trận đường chéo ($T = \Lambda$) khi $S$ là ma trận đối xứng. Khi đó $S$ là $Q\Lambda Q^T$.

Chúng ta biết rằng mọi ma trận đối xứng $S$ đều có các trị riêng thực, và Schur cho phép các $\lambda$ lặp lại:

$S = QTQ^{-1}$ của Schur có nghĩa là $T = Q^T SQ$. Chuyển vị của nó lại là $Q^T SQ$.

*Ma trận tam giác $T$ đối xứng khi $S^T = S$.* Khi đó $T$ phải là ma trận đường chéo và $T = \Lambda$.

Điều này chứng minh rằng $S = Q\Lambda Q^{-1}$. Ma trận đối xứng $S$ có $n$ vectơ riêng trực chuẩn trong $Q$.

*Ghi chú.* Tôi đã thêm một phép chứng minh khác trong Section 7.2 của cuốn sách này. Phép chứng minh đó cho thấy cách các trị riêng $\lambda$ có thể được mô tả *từng cái một*. Trị riêng lớn nhất $\lambda_1$ là giá trị lớn nhất của $x^T Sx / x^T x$. Sau đó $\lambda_2$ (lớn thứ hai) lại là giá trị lớn nhất đó, nếu chúng ta chỉ cho phép các vectơ $x$ vuông góc với vectơ riêng đầu tiên. Trị riêng thứ ba $\lambda_3$ xuất hiện bằng cách yêu cầu $x^T q_1 = 0$ và $x^T q_2 = 0 \dots$

Phép chứng minh này được đặt trong Chương 7 bởi vì cùng một ý tưởng từng-cái-một đó thành công đối với *các giá trị suy biến của bất kỳ ma trận $A$ nào*. **Các giá trị suy biến đến từ $A^T A$ và $AA^T$.**

#### **■ ÔN TẬP CÁC Ý TƯỞNG CHÍNH (REVIEW OF THE KEY IDEAS) ■**

- **1.** Mọi ma trận đối xứng $S$ đều có *các trị riêng thực* và *các vectơ riêng vuông góc*.
- **2.** Phép chéo hóa trở thành $S = Q\Lambda Q^T$ với một ma trận vectơ riêng trực giao $Q$.
- **3.** Tất cả các ma trận đối xứng đều có thể chéo hóa, ngay cả với các trị riêng lặp lại.
- **4.** Dấu của các trị riêng khớp với dấu của các phần tử chốt, khi $S = S^T$.
- **5.** Mọi ma trận vuông đều có thể được "tam giác hóa" bởi $A = QTQ^{-1}$. Nếu $A = S$ thì $T = \Lambda$.

#### **■ CÁC VÍ DỤ CÓ LỜI GIẢI (WORKED EXAMPLES) ■**

**6.4 A** Ma trận $A$ nào có các trị riêng $\lambda = 1, -1$ và các vectơ riêng $x_1 = (\cos \theta, \sin \theta)$ và $x_2 = (-\sin \theta, \cos \theta)$? Thuộc tính nào trong số những thuộc tính này có thể được dự đoán trước?

$$A = A^T \quad A^2 = I \quad \det A = -1 \quad \text{chốt là + và -} \quad A^{-1} = A$$

**Lời giải** Tất cả những tính chất đó đều có thể được dự đoán! Với các trị riêng thực 1, -1 và các vectơ $x_1$ và $x_2$ trực chuẩn, ma trận $A = Q\Lambda Q^T$ phải đối xứng. Các trị riêng 1 và -1 cho chúng ta biết rằng $A^2 = I$ (vì $\lambda^2 = 1$) và $A^{-1} = A$ (cùng một điều) và $\det A = -1$. Hai phần tử chốt phải dương và âm giống như các trị riêng, vì $A$ đối xứng.

Ma trận sẽ là một phép phản xạ. Các vectơ theo hướng của $x_1$ không bị thay đổi bởi $A$ (vì $\lambda = 1$). Các vectơ theo hướng vuông góc bị đảo ngược (vì $\lambda = -1$). Phép phản xạ $A = Q\Lambda Q^T$ là qua "đường thẳng $\theta$". Viết $c$ cho $\cos \theta$ và $s$ cho $\sin \theta$:

$$A = \begin{bmatrix} c & -s \\ s & c \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} \begin{bmatrix} c & s \\ -s & c \end{bmatrix} = \begin{bmatrix} c^2 - s^2 & 2cs \\ 2cs & s^2 - c^2 \end{bmatrix} = \begin{bmatrix} \cos 2\theta & \sin 2\theta \\ \sin 2\theta & -\cos 2\theta \end{bmatrix}.$$

Lưu ý rằng $x = (1, 0)$ biến thành $Ax = (\cos 2\theta, \sin 2\theta)$ trên đường thẳng $2\theta$. Và $(\cos 2\theta, \sin 2\theta)$ phản xạ qua đường thẳng $\theta$ để trở lại $x = (1, 0)$.

**6.4 B** Tìm các trị riêng và vectơ riêng (sin và cosin rời rạc) của $A_3$ và $B_4$.

$$A_3 = \begin{bmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{bmatrix} \quad B_4 = \begin{bmatrix} 1 & -1 & 0 & 0 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ 0 & 0 & -1 & 1 \end{bmatrix}$$

Mẫu $-1, 2, -1$ trong cả hai ma trận là một "sai phân bậc hai". Điều này giống như đạo hàm bậc hai. Khi đó $Ax = \lambda x$ và $Bx = \lambda x$ giống như $d^2x/dt^2 = \lambda x$. Nó có các vectơ riêng $x = \sin kt$ và $x = \cos kt$ vốn là các cơ sở cho chuỗi Fourier.

$A_n$ và $B_n$ dẫn đến "sin rời rạc" và "cosin rời rạc", đây là các cơ sở cho *Biến đổi Fourier Rời rạc (Discrete Fourier Transform)*. DFT này hoàn toàn là trung tâm đối với mọi lĩnh vực xử lý tín hiệu kỹ thuật số. Lựa chọn ưa thích nhất cho JPEG trong xử lý hình ảnh là $B_8$ với kích thước $n = 8$.

**Lời giải** Các trị riêng của $A_3$ là $\lambda = 2 - \sqrt{2}$ và $2$ và $2 + \sqrt{2}$ (xem 6.3 B). Tổng của chúng là 6 (vết của $A_3$) và tích của chúng là 4 (định thức). Ma trận vectơ riêng mang lại "Biến đổi Sin Rời rạc" và các vectơ riêng nằm trên các đường cong sin.

$$
\text{Sin} = \begin{bmatrix} 1 & \sqrt{2} & 1 \\ \sqrt{2} & 0 & -\sqrt{2} \\ 1 & -\sqrt{2} & 1 \end{bmatrix} \quad \text{Cosin} = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & \sqrt{2} - 1 & -1 & 1 - \sqrt{2} \\ 1 & 1 - \sqrt{2} & -1 & \sqrt{2} - 1 \\ 1 & -1 & 1 & -1 \end{bmatrix}
$$

**Ma trận Sin = Các vectơ riêng của $A_3$**

**Ma trận Cosin = Các vectơ riêng của $B_4$**

Các trị riêng của $B_4$ là $\lambda = 2 - \sqrt{2}$ và $2$ và $2 + \sqrt{2}$ và $0$ (giống như $A_3$, cộng thêm trị riêng 0). Vết vẫn là 6, nhưng định thức bây giờ bằng không. Ma trận vectơ riêng $C$ mang lại "Biến đổi Cosin Rời rạc" 4 điểm. Đồ thị trên Web cho thấy hai vectơ riêng đầu tiên nằm trên các đường cong cosin như thế nào. (Tất cả các vectơ riêng của $B$ cũng vậy.) Các vectơ riêng này khớp với cosin ở các *điểm giữa* $\pi/8, 3\pi/8, 5\pi/8, 7\pi/8$.

# **Tập bài tập 6.4 (Problem Set 6.4)**

**1** Những ma trận $E^{-1} S E$ nào sau đây sẽ đối xứng với các trị riêng 1 và -1?

$E = A^T$ không làm được. $E = A^{-1}$ không làm được. $E = Q$ sẽ thành công. Vì vậy $E$ phải là một ma trận trực giao.

**2** Giả sử $S = S^T$. Khi nào $E^{-1} S E$ cũng đối xứng với cùng các trị riêng như $S$?

(a) Chuyển vị $E^{-1} S E$ để thấy rằng nó vẫn đối xứng khi $E =$ \_\_\_\_\_.
(b) $E^{-1} S E$ đồng dạng với $S$ (cùng trị riêng) khi $E =$ \_\_\_\_\_.

Kết hợp (a) và (b) lại. Các ma trận đối xứng đồng dạng với $S$ trông giống như $(\_\_)S(\_\_)$.

**3** Viết $A$ dưới dạng $S + N$, ma trận đối xứng $S$ cộng với ma trận phản đối xứng $N$:

$$A = \begin{bmatrix} 1 & 2 & 4 \\ 4 & 3 & 0 \\ 8 & 6 & 5 \end{bmatrix} = S + N \quad (S^T = S \text{ và } N^T = -N).$$

Đối với bất kỳ ma trận vuông nào, $S = \frac{1}{2}(A + A^T)$ và $N =$ \_\_\_\_\_ cộng lại bằng $A$.

**4** Nếu $C$ đối xứng, hãy chứng minh rằng $A^T C A$ cũng đối xứng. (Chuyển vị nó.) Khi $A$ là ma trận $6 \times 3$, kích thước của $C$ và $A^T C A$ là bao nhiêu?

**5** Tìm các trị riêng và các vectơ riêng đơn vị của

$$S = \begin{bmatrix} 2 & 2 & 2 \\ 2 & 0 & 0 \\ 2 & 0 & 0 \end{bmatrix}.$$

**6** Tìm một ma trận trực giao $Q$ chéo hóa $S = \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix}$. $\Lambda$ là gì?

**7** Tìm một ma trận trực giao $Q$ chéo hóa ma trận đối xứng này:

$$S = \begin{bmatrix} 1 & 0 & 2 \\ 0 & -1 & -2 \\ 2 & -2 & 0 \end{bmatrix}.$$

**8** Tìm *tất cả* các ma trận trực giao chéo hóa $S = \begin{bmatrix} 9 & 12 \\ 12 & 16 \end{bmatrix}$.

**9** (a) Tìm một ma trận đối xứng $\begin{bmatrix} 1 & b \\ b & 1 \end{bmatrix}$ có một trị riêng âm.
(b) Làm sao bạn biết nó phải có một phần tử chốt âm?
(c) Làm sao bạn biết nó không thể có hai trị riêng âm?

**10** Nếu $A^3 = 0$ thì các trị riêng của $A$ phải là \_\_\_\_\_. Hãy cho một ví dụ mà $A \neq 0$. Nhưng nếu $A$ là ma trận đối xứng, hãy chéo hóa nó để chứng minh rằng $A$ phải là ma trận không.

**11** Nếu $\lambda = a + ib$ là một trị riêng của ma trận thực $A$, thì số phức liên hợp của nó $\bar{\lambda} = a - ib$ cũng là một trị riêng. (Nếu $Ax = \lambda x$ thì cũng có $A\bar{x} = \bar{\lambda}\bar{x}$: một cặp liên hợp $\lambda$ và $\bar{\lambda}$.) Giải thích tại sao mọi ma trận thực $3 \times 3$ đều có ít nhất một trị riêng thực.

**12** Đây là một "phép chứng minh" nhanh rằng các trị riêng của mọi ma trận thực $A$ đều là số thực:

Phép chứng minh sai: $Ax = \lambda x$ cho ta $x^T Ax = \lambda x^T x$ nên $\lambda = \frac{x^T Ax}{x^T x} = \frac{\text{thực}}{\text{thực}}$

Hãy tìm điểm sai sót trong lý luận này - một giả định ngầm không có căn cứ. Bạn có thể kiểm tra các bước đó trên ma trận quay $90^\circ$ $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ với $\lambda = i$ và $x = (i, 1)$.


# **6.5 Ma trận Xác định Dương (Positive Definite Matrices)**

Vấn đề đầu tiên là nhận biết các ma trận xác định dương. Bạn có thể nói, chỉ cần tìm tất cả các trị riêng và kiểm tra $\lambda > 0$. Đó chính xác là điều chúng ta muốn tránh. Tính toán trị riêng tốn rất nhiều công sức. Khi cần các $\lambda$, chúng ta có thể tính toán chúng. Nhưng nếu chúng ta chỉ muốn biết rằng tất cả các trị riêng đều dương, thì có những cách nhanh hơn. Dưới đây là hai mục tiêu của phần này:

- Tìm các *bài kiểm tra nhanh (quick tests)* trên một ma trận đối xứng để đảm bảo *các trị riêng dương*.
- Giải thích các ứng dụng quan trọng của tính xác định dương.

Mọi trị riêng đều là số thực vì ma trận là ma trận đối xứng.

Bắt đầu với ma trận $2 \times 2$. Khi nào thì $S = \begin{bmatrix} a & b \\ b & c \end{bmatrix}$ có $\lambda_1 > 0$ và $\lambda_2 > 0$?

*Kiểm tra: Các trị riêng của $S$ là số dương khi và chỉ khi $a > 0$ và $ac - b^2 > 0$.*

$$
\begin{align*}
S_1 &= \begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix} \text{ không xác định dương vì } ac - b^2 = 1 - 4 < 0 \\
S_2 &= \begin{bmatrix} 1 & -2 \\ -2 & 6 \end{bmatrix} \text{ xác định dương vì } a = 1 \text{ và } ac - b^2 = 6 - 4 > 0 \\
S_3 &= \begin{bmatrix} -1 & 2 \\ 2 & -6 \end{bmatrix} \text{ không xác định dương (ngay cả khi } \det A = +2) \text{ vì } a = -1
\end{align*}
$$

Các trị riêng $3$ và $-1$ của $S_1$ xác nhận rằng $S_1$ *không* xác định dương. Vết dương $3 - 1 = 2$, nhưng định thức âm $(3)(-1) = -3$. Và $S_3 = -S_2$ là xác định *âm (negative definite)*. Hai trị riêng dương cho $S_2$, hai trị riêng âm cho $S_3$.

*Phép chứng minh rằng bài kiểm tra $2 \times 2$ được thông qua khi $\lambda_1 > 0$ và $\lambda_2 > 0$.* Tích của chúng $\lambda_1 \lambda_2$ là định thức nên $ac - b^2 > 0$. Tổng của chúng $\lambda_1 + \lambda_2$ là vết nên $a + c > 0$. Khi đó $a$ và $c$ đều dương (nếu $a$ hoặc $c$ không dương thì điều kiện $ac - b^2 > 0$ sẽ thất bại). Câu hỏi 1 đảo ngược lại lập luận để cho thấy rằng các bài kiểm tra $a > 0$ và $ac > b^2$ đảm bảo $\lambda_1 > 0$ và $\lambda_2 > 0$.

Bài kiểm tra này sử dụng định thức $1 \times 1$ là $a$ và định thức $2 \times 2$ là $ac - b^2$. Khi $S$ có kích thước $3 \times 3$, $\det S > 0$ là phần thứ ba của bài kiểm tra. Bài kiểm tra tiếp theo yêu cầu *các phần tử chốt dương*.

**Kiểm tra: Các trị riêng của $S$ là số dương khi và chỉ khi các phần tử chốt đều dương:**

$$a > 0 \quad \text{và} \quad \frac{ac - b^2}{a} > 0.$$

$a > 0$ được yêu cầu trong cả hai bài kiểm tra. Do đó $ac > b^2$ cũng được yêu cầu, cho bài kiểm tra định thức và bây giờ là bài kiểm tra phần tử chốt. Vấn đề là nhận ra tỷ lệ đó chính là *phần tử chốt thứ hai* của $S$:

$$\begin{bmatrix} a & b \\ b & c \end{bmatrix} \xrightarrow{\text{Chốt đầu tiên là } a} \begin{bmatrix} a & b \\ 0 & c - \frac{b}{a}b \end{bmatrix} \xrightarrow{\text{Chốt thứ hai là } c - \frac{b^2}{a} = \frac{ac - b^2}{a}}$$

Điều này kết nối hai phần lớn của đại số tuyến tính. **Các trị riêng dương có nghĩa là các phần tử chốt dương và ngược lại.** Mỗi phần tử chốt là tỷ lệ của các định thức góc trên bên trái. Các phần tử chốt cung cấp một bài kiểm tra nhanh cho $\lambda > 0$, và chúng tính toán nhanh hơn rất nhiều so với các trị riêng. Thật thỏa mãn khi thấy các phần tử chốt, định thức và các trị riêng kết hợp lại với nhau trong khóa học này.

**Ví dụ $3 \times 3$** $S = \begin{bmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{bmatrix}$ là ma trận xác định dương.
Các trị riêng $1, 1, 4$
Các định thức $2$ và $3$ và $4$
Các phần tử chốt $2$ và $3/2$ và $4/3$

$S - I$ sẽ là *bán xác định dương (semidefinite)*: các trị riêng $0, 0, 3$. $S - 2I$ là *không xác định (indefinite)* bởi vì $\lambda = -1, -1, 2$. Bây giờ đến một cách nhìn khác về các ma trận đối xứng có các trị riêng dương.

### **Định nghĩa dựa trên Năng lượng (Energy-based Definition)**

Từ $Sx = \lambda x$, nhân với $x^T$ để được $x^T Sx = \lambda x^T x$. Vế phải là một số $\lambda$ dương nhân với một số dương $x^T x = \|x\|^2$. Vì vậy vế trái $x^T Sx$ là số dương đối với bất kỳ vectơ riêng nào.

**Điểm quan trọng:** Ý tưởng mới là $x^T Sx$ là *số dương đối với mọi vectơ $x$ khác không*, không chỉ các vectơ riêng. Trong nhiều ứng dụng, con số $x^T Sx$ (hoặc $\frac{1}{2}x^T Sx$) này là **năng lượng (energy)** trong hệ thống. Yêu cầu về năng lượng dương đưa ra *một định nghĩa khác* về ma trận xác định dương. Tôi nghĩ định nghĩa dựa trên năng lượng này là định nghĩa cơ bản nhất.

Các trị riêng và phần tử chốt là hai cách tương đương để kiểm tra yêu cầu mới $x^T Sx > 0$.

**Định nghĩa:** *S là xác định dương nếu $x^T Sx > 0$ đối với mọi vectơ $x$ khác không:*

$$\text{Cỡ } 2 \times 2 \quad x^T S x = \begin{bmatrix} x & y \end{bmatrix} \begin{bmatrix} a & b \\ b & c \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = ax^2 + 2bxy + cy^2 > 0. \quad (1)$$

Bốn phần tử $a, b, b, c$ cung cấp bốn phần của $x^T Sx$. Từ $a$ và $c$ đến các bình phương thuần túy $ax^2$ và $cy^2$. Từ $b$ và $b$ ngoài đường chéo đến các phần tử chéo $bxy$ và $byx$ (chúng giống nhau). Cộng bốn phần đó lại với nhau cho ra $x^T Sx$. Định nghĩa dựa trên năng lượng này dẫn đến một sự thật cơ bản:

### *Nếu S và T là đối xứng và xác định dương, thì S + T cũng vậy.*

**Lý do:** $x^T (S+T)x$ đơn giản là $x^T Sx + x^T Tx$. Hai số hạng đó đều dương (với $x \neq 0$) nên $S + T$ cũng xác định dương. Các phần tử chốt và các trị riêng không dễ dàng theo dõi khi các ma trận được cộng lại, nhưng các năng lượng thì chỉ việc cộng vào nhau.

$x^T Sx$ cũng kết nối với cách cuối cùng của chúng ta để nhận biết một ma trận xác định dương. Bắt đầu với bất kỳ ma trận $A$ nào, có thể là hình chữ nhật. Chúng ta biết rằng $S = A^T A$ là ma trận vuông và đối xứng. Hơn thế nữa, $S$ sẽ xác định dương khi $A$ có các cột độc lập tuyến tính:

*Kiểm tra: Nếu các cột của $A$ độc lập tuyến tính, thì $S = A^T A$ là ma trận xác định dương.*

Một lần nữa, các trị riêng và phần tử chốt lại không dễ tính toán. Nhưng con số $x^T Sx$ giống hệt với $x^T A^T Ax$. $x^T A^T Ax$ chính xác là $(Ax)^T (Ax) = \|Ax\|^2$ - một phép chứng minh quan trọng khác bằng dấu ngoặc đơn! Vectơ $Ax$ đó không bằng không khi $x \neq 0$ (đây là ý nghĩa của các cột độc lập tuyến tính). Khi đó $x^T Sx$ là số dương $\|Ax\|^2$ và ma trận $S$ xác định dương.

Hãy để tôi tập hợp lý thuyết này lại, thành *năm phát biểu tương đương* về tính xác định dương. Bạn sẽ thấy ý tưởng then chốt đó kết nối toàn bộ chủ đề đại số tuyến tính như thế nào: các phần tử chốt, định thức, các trị riêng và bình phương tối thiểu (từ $A^T A$). Tiếp theo là các ứng dụng.

### *Khi một ma trận đối xứng S có một trong năm thuộc tính này, thì nó có tất cả chúng:*

- **1.** Tất cả $n$ phần tử chốt của $S$ đều dương.
- **2.** Tất cả $n$ định thức góc trên bên trái đều dương.
- **3.** Tất cả $n$ trị riêng của $S$ đều dương.
- **4.** $x^T Sx$ là số dương ngoại trừ tại $x = 0$. Đây là định nghĩa *dựa trên năng lượng*.
- **5.** $S$ bằng $A^T A$ với một ma trận $A$ có *các cột độc lập tuyến tính*.

Các "định thức góc trên bên trái" có kích thước $1 \times 1, 2 \times 2, \dots, n \times n$. Cái cuối cùng là định thức của toàn bộ ma trận $S$. Định lý này gắn kết toàn bộ khóa học đại số tuyến tính lại với nhau. 

**Ví dụ 1** Kiểm tra các ma trận đối xứng $S$ và $T$ này xem có xác định dương hay không:

$$S = \begin{bmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{bmatrix} \quad \text{và} \quad T = \begin{bmatrix} 2 & -1 & b \\ -1 & 2 & -1 \\ b & -1 & 2 \end{bmatrix}$$

**Lời giải** Các phần tử chốt của $S$ là $2$ và $3/2$ và $4/3$, tất cả đều dương. Các định thức góc trên bên trái của nó là $2$ và $3$ và $4$, tất cả đều dương. Các trị riêng của $S$ là $2 - \sqrt{2}$ và $2$ và $2 + \sqrt{2}$, tất cả đều dương. Điều đó hoàn thành các bài kiểm tra 1, 2 và 3. Bất kỳ một bài kiểm tra nào cũng đều mang tính quyết định!

Tôi có ba ứng cử viên $A_1, A_2, A_3$ để đề xuất cho $S = A^T A$. Tất cả chúng đều cho thấy rằng $S$ xác định dương. $A_1$ là một ma trận sai phân bậc nhất, $4 \times 3$, tạo ra mẫu $-1, 2, -1$ trong $S$:

$$S = A_1^T A_1 = \begin{bmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{bmatrix} = \begin{bmatrix} 1 & -1 & 0 & 0 \\ 0 & 1 & -1 & 0 \\ 0 & 0 & 1 & -1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \\ 0 & 0 & -1 \end{bmatrix}$$

Ba cột của $A_1$ là độc lập tuyến tính. Do đó $S$ là xác định dương.


| Kiểm tra trên $T$ | $\det T = 4 + 2b - b^2 = (1 + b)(4 - 2b)$ | phải dương. |
|---|---|---|

Tại $b = -1$ và $b = 2$, chúng ta có $\det T = 0$. *Ở giữa $b = -1$ và $b = 2$, ma trận $T$ này là xác định dương.* Phần tử ở góc $b = 0$ trong ma trận $S$ nằm an toàn giữa $-1$ và $2$.

# **Ma trận Bán xác định Dương (Positive Semidefinite Matrices)**

Thường thì chúng ta ở ranh giới của tính xác định dương. Định thức bằng 0. Trị riêng nhỏ nhất bằng 0. Năng lượng trong vectơ riêng của nó là $x^T Sx = x^T 0x = 0$. Những ma trận ở ranh giới này được gọi là *bán xác định dương (positive semidefinite)*. Dưới đây là hai ví dụ (không khả nghịch):

| $S = \begin{bmatrix} 2 & 2 \\ 2 & 4 \end{bmatrix}$ và $T = \begin{bmatrix} 2 & -1 & -1 \\ -1 & 2 & -1 \\ -1 & -1 & 2 \end{bmatrix}$ là bán xác định dương. |
|---|

$S$ có các trị riêng 5 và 0. Các định thức góc trên bên trái của nó là 1 và 0. Hạng của nó chỉ là 1. Ma trận $S$ này phân tích thành $A^T A$ với **các cột phụ thuộc tuyến tính** trong $A$:

| Các cột phụ thuộc trong $A$ | $\begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 2 & 0 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix}$ |
|---|---|
| $S$ bán xác định dương | |

Nếu 4 được tăng lên bởi bất kỳ số nhỏ nào, ma trận $S$ sẽ trở thành xác định dương.

Ma trận vòng $T$ cũng có định thức bằng không (đã tính ở trên khi $b = -1$). $T$ là suy biến. Vectơ riêng $x = (1, 1, 1)$ có $Tx = \mathbf{0}$ và năng lượng $x^T Tx = 0$. Các vectơ $x$ theo tất cả các hướng khác đều cho năng lượng dương. $T$ này có thể được viết dưới dạng $A^T A$ theo nhiều cách, nhưng $A$ sẽ luôn có các cột *phụ thuộc tuyến tính*, với $(1, 1, 1)$ nằm trong không gian null của nó:

**Sai phân bậc hai**
$$T = \begin{bmatrix} 2 & -1 & -1 \\ -1 & 2 & -1 \\ -1 & -1 & 2 \end{bmatrix} = \begin{bmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \\ -1 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & -1 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix}$$

Các ma trận bán xác định dương có tất cả các $\lambda \geq 0$ và tất cả $x^T Sx \geq 0$. Những bất đẳng thức yếu đó ($\geq$ **thay vì** $>$) bao gồm cả $S$ xác định dương và cả các ma trận suy biến ở ranh giới.

#### **Hình elip $ax^2 + 2bxy + cy^2 = 1$**

Hãy nghĩ về một hình elip bị nghiêng $x^T Sx = 1$. Tâm của nó là $(0, 0)$, như trong Hình 6.7a. Xoay nó để thẳng hàng với các trục tọa độ (trục $X$ và $Y$). Đó là Hình 6.7b. Hai hình ảnh này cho thấy hình học đằng sau phép phân tích $S = Q\Lambda Q^{-1} = Q\Lambda Q^T$:

- **1.** Hình elip bị nghiêng được liên kết với $S$. Phương trình của nó là $x^T Sx = 1$.
- **2.** Hình elip thẳng hàng được liên kết với $\Lambda$. Phương trình của nó là $X^T \Lambda X = 1$.
- **3.** Ma trận quay làm thẳng hàng hình elip là ma trận vectơ riêng $Q$.

**Ví dụ 2** Tìm các trục của hình elip bị nghiêng $5x^2 + 8xy + 5y^2 = 1$ này.

**Lời giải** Bắt đầu với ma trận xác định dương tương ứng với phương trình này:

| Phương trình là | $\begin{bmatrix} x & y \end{bmatrix} \begin{bmatrix} 5 & 4 \\ 4 & 5 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = 1.$ | Ma trận là | $S = \begin{bmatrix} 5 & 4 \\ 4 & 5 \end{bmatrix}.$ |
|---|---|---|---|

Hình 6.7: Hình elip bị nghiêng $5x^2 + 8xy + 5y^2 = 1$. Khi thẳng hàng nó là $9X^2 + Y^2 = 1$.

Các vectơ riêng là $\begin{bmatrix} 1 \\ 1 \end{bmatrix}$ và $\begin{bmatrix} 1 \\ -1 \end{bmatrix}$. Chia cho $\sqrt{2}$ để có các vectơ đơn vị. Khi đó $S = Q\Lambda Q^T$:

| **Các vectơ riêng trong** $Q$ | $S = \begin{bmatrix} 5 & 4 \\ 4 & 5 \end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} 9 & 0 \\ 0 & 1 \end{bmatrix} \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$ |
|---|---|
| **Các trị riêng 9 và 1** | |

Bây giờ nhân với $\begin{bmatrix} x & y \end{bmatrix}$ ở bên trái và $\begin{bmatrix} x \\ y \end{bmatrix}$ ở bên phải để có $x^T Sx = (x^T Q)\Lambda (Q^T x)$:

$$x^T S x = \text{tổng các bình phương} \quad 5x^2 + 8xy + 5y^2 = 9 \left( \frac{x+y}{\sqrt{2}} \right)^2 + 1 \left( \frac{x-y}{\sqrt{2}} \right)^2. \quad (2)$$

Các hệ số không phải là các phần tử chốt 5 và 9/5 từ $D$, chúng là các trị riêng 9 và 1 từ $\Lambda$. Bên trong các bình phương là các vectơ riêng $q_1 = (1, 1)/\sqrt{2}$ và $q_2 = (1, -1)/\sqrt{2}$.

*Các trục của hình elip nghiêng hướng theo các vectơ riêng đó.* Điều này giải thích tại sao $S = Q\Lambda Q^T$ được gọi là "định lý trục chính (principal axis theorem)" - nó hiển thị các trục. Không chỉ các hướng trục (từ các vectơ riêng) mà còn cả độ dài trục (từ các trị riêng). Để thấy tất cả, hãy sử dụng các chữ in hoa cho các tọa độ mới làm thẳng hàng hình elip:

| Thẳng hàng | $\frac{x + y}{\sqrt{2}} = X$ | và | $\frac{x - y}{\sqrt{2}} = Y$ | và | $9X^2 + Y^2 = 1.$ |
|---|---|---|---|---|---|

Giá trị lớn nhất của $X^2$ là $1/9$. Điểm cuối của trục ngắn hơn có $X = 1/3$ và $Y = 0$. Lưu ý: Trị riêng *lớn hơn* $\lambda_1 = 9$ mang lại trục *ngắn hơn*, có nửa độ dài $1/\sqrt{9} = 1/3$. Trị riêng nhỏ hơn $\lambda_2 = 1$ mang lại độ dài lớn hơn $1/\sqrt{1} = 1$.

Trong hệ $xy$, các trục nằm dọc theo các vectơ riêng của $S$. Trong hệ $XY$, các **trục nằm dọc theo các vectơ riêng của $\Lambda$** - các trục tọa độ. Tất cả đều đến từ $S = Q\Lambda Q^T$. $S = Q\Lambda Q^T$ là xác định dương khi tất cả $\lambda_i > 0$. Đồ thị của $x^T Sx = 1$ là một hình elip:

**Hình elip**
$$[x \ y] Q \Lambda Q^T \begin{bmatrix} x \\ y \end{bmatrix} = [X \ Y] \Lambda \begin{bmatrix} X \\ Y \end{bmatrix} = \lambda_1 X^2 + \lambda_2 Y^2 = 1. \quad (3)$$

Các trục hướng dọc theo các vectơ riêng của $S$. Các nửa độ dài là $1/\sqrt{\lambda_1}$ và $1/\sqrt{\lambda_2}$.

$S = I$ mang lại đường tròn $x^2 + y^2 = 1$. Nếu một trị riêng là số âm (đổi chỗ 4 và 5 trong $S$), hình elip đổi thành *hyperbol*. Tổng các bình phương trở thành một *hiệu của các bình phương:* $9X^2 - Y^2 = 1$. Đối với ma trận xác định âm như $S = -I$, với cả hai $\lambda$ đều âm, đồ thị của $-x^2 - y^2 = 1$ hoàn toàn không có điểm nào.

Nếu $S$ có kích thước $n \times n$, $x^T Sx = 1$ là một "ellipsoid" trong $\mathbb{R}^n$. Các trục của nó là các vectơ riêng của $S$.

### **Ứng dụng Quan trọng: Kiểm tra Cực tiểu (Test for a Minimum)**

Hàm $F(x, y)$ có đạt cực tiểu nếu $\partial F/\partial x = 0$ và $\partial F/\partial y = 0$ tại điểm $(x, y) = (0, 0)$ không?

Đối với $f(x)$, bài kiểm tra cực tiểu đến từ giải tích: $df/dx = 0$ và $d^2f/dx^2 > 0$. Hai biến trong $F(x, y)$ tạo ra một ma trận đối xứng $S$. Nó chứa *bốn đạo hàm bậc hai*. **$d^2f/dx^2$ dương đổi thành $S$ xác định dương:**

**Đạo hàm bậc hai**
$$S = \begin{bmatrix} \partial^2 F / \partial x^2 & \partial^2 F / \partial x \partial y \\ \partial^2 F / \partial y \partial x & \partial^2 F / \partial y^2 \end{bmatrix}$$

*$F(x, y)$ có cực tiểu nếu $\partial F/\partial x = \partial F/\partial y = 0$ và $S$ xác định dương.*

Lý do: $S$ tiết lộ các số hạng vô cùng quan trọng $ax^2 + 2bxy + cy^2$ gần $(x, y) = (0, 0)$. Các đạo hàm bậc hai của $F$ là $2a, 2b, 2b, 2c$. Đối với $F(x, y, z)$, ma trận $S$ sẽ có kích thước $3 \times 3$.

#### **■ ÔN TẬP CÁC Ý TƯỞNG CHÍNH ■**

- **1.** Các ma trận xác định dương có các trị riêng dương và các phần tử chốt dương.
- **2.** Một bài kiểm tra nhanh được cho bởi các định thức góc trên bên trái: $a > 0$ và $ac - b^2 > 0$.
- **3.** Đồ thị của năng lượng $x^T Sx$ sau đó là một "cái bát" đi lên từ $x = 0$: $x^T Sx = ax^2 + 2bxy + cy^2$ là số dương ngoại trừ tại $(x, y) = (0, 0)$.
- **4.** $S = A^T A$ tự động xác định dương nếu $A$ có các cột độc lập tuyến tính.
- **5.** Ellipsoid $x^T Sx = 1$ có các trục nằm dọc theo các vectơ riêng của $S$. Độ dài là $1/\sqrt{\lambda}$.
- **6.** Cực tiểu của $F(x, y)$ đạt được nếu đạo hàm bậc nhất bằng 0 và ma trận đạo hàm bậc hai xác định dương.

#### **■ CÁC VÍ DỤ CÓ LỜI GIẢI ■**

**6.5 A** Các phép phân tích tuyệt vời của một ma trận đối xứng là $S = LDL^T$ từ các phần tử chốt và hệ số nhân, và $S = Q\Lambda Q^T$ từ các trị riêng và vectơ riêng. Hãy thử các bài kiểm tra $n \times n$ này trên `pascal(6)` và `ones(6)` và `hilb(6)` cũng như các ma trận khác trong thư viện của MATLAB.

`pascal(6)` là xác định *dương* vì tất cả các phần tử chốt của nó đều là 1 (Ví dụ 2.6 A).

`ones(6)` là *bán* xác định dương vì các trị riêng của nó là 0, 0, 0, 0, 0, 6.

$H = \text{hilb}(6)$ là xác định *dương* ngay cả khi `eig(H)` cho thấy các trị riêng rất gần với không.

**Ma trận Hilbert:** $x^T Hx = \int_0^1 (x_1 + x_2 s + \dots + x_n s^{n-1})^2 ds > 0, \quad H_{ij} = 1/(i+j-1)$.

`rand(6) + rand(6)'` có thể xác định dương hoặc không. *Thử nghiệm chỉ cho ra 2 kết quả dương trong 20000 lần.*

`n = 20000; p = 0; for k = 1:n, A = rand(6); p = p + all(eig(A + A') > 0); end, p/n`

**6.5 B** *Khi nào thì ma trận khối đối xứng* 
$$M = \begin{bmatrix} A & B \\ B^T & C \end{bmatrix}$$
*là xác định dương?*

**Lời giải** Nhân hàng đầu tiên của $M$ với $B^T A^{-1}$ và trừ đi từ hàng thứ hai, để nhận được một khối số không. *Phần bù Schur (Schur complement)* $S = C - B^T A^{-1} B$ xuất hiện ở góc:

$$\begin{bmatrix} I & 0 \\ -B^T A^{-1} & I \end{bmatrix} \begin{bmatrix} A & B \\ B^T & C \end{bmatrix} = \begin{bmatrix} A & B \\ 0 & C - B^T A^{-1} B \end{bmatrix} = \begin{bmatrix} A & B \\ 0 & S \end{bmatrix} \quad (4)$$

*Hai khối $A$ và $S$ đó phải xác định dương.* Các phần tử chốt của chúng chính là các phần tử chốt của $M$.

**6.5 C** Tìm các trị riêng của ma trận ba đường chéo $S$ kích thước $n \times n$ với các phần tử -1, 2, -1 (ma trận yêu thích của tôi).

**Lời giải** Cách tốt nhất là đoán $\lambda$ và $x$. Sau đó kiểm tra $Sx = \lambda x$. Việc đoán không thể hiệu quả đối với hầu hết các ma trận, nhưng các trường hợp đặc biệt là một phần lớn của toán học (thuần túy và ứng dụng).

Chìa khóa ẩn trong một phương trình vi phân. Ma trận sai phân bậc hai $S$ giống như một *đạo hàm bậc hai*, và những trị riêng đó dễ nhìn thấy hơn nhiều:

| Trị riêng $\lambda_1, \lambda_2, \dots$ | $\frac{d^2 y}{dx^2} = \lambda y(x)$ | với | $y(0) = 0$ | (5) |
|---|---|---|---|---|
| Hàm riêng $y_1, y_2, \dots$ | | | $y(1) = 0$ |

Thử $y = \sin cx$. Đạo hàm bậc hai của nó là $y'' = -c^2 \sin cx$. Vì vậy trị riêng trong (5) sẽ là $\lambda = -c^2$, miễn là $y = \sin cx$ thỏa mãn các điều kiện điểm biên $y(0) = 0 = y(1)$.

Chắc chắn $\sin 0 = 0$ (đây là nơi các hàm cosin bị loại bỏ). Ở đầu kia $x = 1$, chúng ta cần $y(1) = \sin c = 0$. Số $c$ phải là $k\pi$, một bội số của $\pi$. Khi đó $\lambda$ là $-k^2 \pi^2$.

| Trị riêng $\lambda = -k^2\pi^2$ | $\frac{d^2}{dx^2} \sin k\pi x = -k^2\pi^2 \sin k\pi x.$ | (6) |
|---|---|---|
| Hàm riêng $y = \sin k\pi x$ | |

Bây giờ chúng ta quay lại ma trận $S$ và đoán các vectơ riêng của nó. Chúng đến từ $\sin k\pi x$ tại $n$ điểm $x = h, 2h, \dots, nh$, cách đều nhau giữa 0 và 1. Khoảng cách $\Delta x$ là $h = 1/(n + 1)$, vì vậy điểm thứ $(n + 1)$ có $(n + 1)h = 1$. Nhân vectơ sin $x$ đó với $S$:

$$Sx = \lambda_k x = (2 - 2 \cos k\pi h) x \quad (7)$$
$$x = (\sin k\pi h, \dots, \sin nk\pi h).$$

# **Tập bài tập 6.5 (Problem Set 6.5)**

**Các câu hỏi 1-13 nói về các bài kiểm tra tính xác định dương.**

**1** Giả sử các bài kiểm tra $2 \times 2$ với $a > 0$ và $ac - b^2 > 0$ được thông qua. Khi đó $c > b^2/a > 0$.
(i) $\lambda_1$ và $\lambda_2$ có *cùng dấu* vì tích $\lambda_1 \lambda_2$ bằng \_\_\_\_\_.
(ii) Dấu đó là dương vì $\lambda_1 + \lambda_2$ bằng \_\_\_\_\_.
*Kết luận:* Các bài kiểm tra $a > 0, ac - b^2 > 0$ đảm bảo các trị riêng dương $\lambda_1, \lambda_2$.

**2** Ma trận nào trong số $S_1, S_2, S_3, S_4$ có hai trị riêng dương? Sử dụng một bài kiểm tra, đừng tính toán các $\lambda$. Đồng thời tìm một vectơ $x$ sao cho $x^T S_1 x < 0$, để cho thấy $S_1$ không xác định dương.

| $S_1 = \begin{bmatrix} 5 & 6 \\ 6 & 7 \end{bmatrix}$ | $S_2 = \begin{bmatrix} -1 & -2 \\ -2 & -5 \end{bmatrix}$ | $S_3 = \begin{bmatrix} 1 & 10 \\ 10 & 100 \end{bmatrix}$ | $S_4 = \begin{bmatrix} 1 & 10 \\ 10 & 101 \end{bmatrix}$ |
|---|---|---|---|

**3** Đối với các số $b$ và $c$ nào thì các ma trận này xác định dương?
$$S = \begin{bmatrix} 1 & b \\ b & 9 \end{bmatrix} \quad S = \begin{bmatrix} 2 & 4 \\ 4 & c \end{bmatrix} \quad S = \begin{bmatrix} c & b \\ b & c \end{bmatrix}$$
Với các phần tử chốt trong $D$ và số nhân trong $L$, hãy phân tích từng $A$ thành $LDL^T$.

**4** Hàm số $f = ax^2 + 2bxy + cy^2$ cho mỗi ma trận này là gì? Hoàn thành bình phương để viết mỗi $f$ dưới dạng tổng của một hoặc hai bình phương $f = d_1(\dots)^2 + d_2(\dots)^2$.
$$S_1 = \begin{bmatrix} 1 & 2 \\ 2 & 9 \end{bmatrix} \quad S_2 = \begin{bmatrix} 1 & 3 \\ 3 & 9 \end{bmatrix} \quad f = \begin{bmatrix} x & y \end{bmatrix} \begin{bmatrix} S \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$$

**5** Viết $f(x, y) = x^2 + 4xy + 3y^2$ dưới dạng một *hiệu* của các bình phương và tìm một điểm $(x, y)$ tại đó $f$ âm. Không có cực tiểu tại $(0, 0)$ mặc dù $f$ có các hệ số dương.

**6** Hàm số $f(x, y) = 2xy$ chắc chắn có một điểm yên ngựa và không có cực tiểu tại $(0, 0)$. Ma trận đối xứng $S$ nào tạo ra $f$ này? Các trị riêng của nó là gì?

**7** Kiểm tra xem $A^T A$ có xác định dương trong từng trường hợp không: $A$ cần các cột độc lập.
$$A = \begin{bmatrix} 1 & 2 \\ 0 & 3 \end{bmatrix} \quad A = \begin{bmatrix} 1 & 1 \\ 1 & 2 \\ 2 & 1 \end{bmatrix} \quad A = \begin{bmatrix} 1 & 1 & 2 \\ 1 & 2 & 1 \\ 1 & 1 & 1 \end{bmatrix}$$

**8** Hàm số $f(x, y) = 3(x + 2y)^2 + 4y^2$ là dương ngoại trừ tại $(0, 0)$. Ma trận $S$ trong $f = \begin{bmatrix} x & y \end{bmatrix} S \begin{bmatrix} x \\ y \end{bmatrix}$ là gì? Kiểm tra xem các phần tử chốt của $A$ có phải là 3 và 4 không.

**9** Tìm ma trận $S$ kích thước $3 \times 3$ và các phần tử chốt, hạng, trị riêng, và định thức của nó:
$$\begin{bmatrix} x_1 & x_2 & x_3 \end{bmatrix} \begin{bmatrix} S \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = 4(x_1 - x_2 + 2x_3)^2.$$

**10** Các ma trận đối xứng $3 \times 3$ nào $S$ và $T$ tạo ra các dạng toàn phương này?
$x^T Sx = 2(x_1^2 + x_2^2 + x_3^2 - x_1 x_2 - x_2 x_3)$. Tại sao $S$ xác định dương?
$x^T Tx = 2(x_1^2 + x_2^2 + x_3^2 - x_1 x_2 - x_1 x_3 - x_2 x_3)$. Tại sao $T$ bán xác định dương?

**11** Tính toán ba định thức góc trên bên trái của $S$ để xác định tính xác định dương. Kiểm chứng rằng các tỷ số của chúng mang lại phần tử chốt thứ hai và thứ ba.
$$\text{Các chốt} = \text{tỷ số các định thức} \quad S = \begin{bmatrix} 2 & 2 & 0 \\ 2 & 5 & 3 \\ 0 & 3 & 8 \end{bmatrix}.$$

**12** Đối với các số $c$ và $d$ nào thì $S$ và $T$ xác định dương? Kiểm tra 3 định thức của chúng:
$$S = \begin{bmatrix} c & 1 & 1 \\ 1 & c & 1 \\ 1 & 1 & c \end{bmatrix} \quad \text{và} \quad T = \begin{bmatrix} 1 & 2 & 3 \\ 2 & d & 4 \\ 3 & 4 & 5 \end{bmatrix}.$$

**13** Tìm một ma trận với $a > 0$ và $c > 0$ và $a + c > 2b$ có một trị riêng âm.

**Các bài tập từ 14-20 nói về các ứng dụng của các bài kiểm tra.**

**14** Nếu $S$ xác định dương thì $S^{-1}$ xác định dương. Cách chứng minh tốt nhất: Các trị riêng của $S^{-1}$ đều dương bởi vì \_\_\_\_\_. *Cách chứng minh thứ hai* (chỉ cho kích thước $2 \times 2$):
Các phần tử của $S^{-1} = \frac{1}{ac - b^2} \begin{bmatrix} c & -b \\ -b & a \end{bmatrix}$ vượt qua các bài kiểm tra định thức \_\_\_\_\_.

**15** Nếu $S$ và $T$ xác định dương, tổng $S + T$ của chúng là xác định dương. Các phần tử chốt và trị riêng không thuận tiện cho $S + T$. Tốt hơn là sử dụng $x^T (S + T)x > 0$. Ngoài ra $S = A^T A$ và $T = B^T B$ cho $S + T = \begin{bmatrix} A \\ B \end{bmatrix}^T \begin{bmatrix} A \\ B \end{bmatrix}$ với các cột độc lập tuyến tính.

**16** Một ma trận xác định dương không thể có một số không (hoặc tệ hơn, một số âm) trên đường chéo chính của nó. Hãy chỉ ra rằng ma trận này không thỏa mãn $x^T Sx > 0$:
$$\begin{bmatrix} x_1 & x_2 & x_3 \end{bmatrix} \begin{bmatrix} 4 & 1 & 1 \\ 1 & 0 & 2 \\ 1 & 2 & 5 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} \text{ không dương khi } (x_1, x_2, x_3) = (\dots, \dots, \dots).$$

**17** Một phần tử trên đường chéo $s_{jj}$ của một ma trận đối xứng không thể nhỏ hơn tất cả các $\lambda$. Nếu như vậy, thì $S - s_{jj}I$ sẽ có \_\_\_\_\_ trị riêng và sẽ xác định dương. Nhưng $S - s_{jj}I$ có một \_\_\_\_\_ trên đường chéo chính.

**18** Nếu $Sx = \lambda x$ thì $x^T Sx =$ \_\_\_\_\_. Tại sao con số này lại dương khi $\lambda > 0$?

**19** Đảo ngược Bài toán 18 để chỉ ra rằng nếu *tất cả* $\lambda > 0$ *thì* $x^T Sx > 0$. Chúng ta phải thực hiện điều này cho mọi $x$ khác không, không chỉ các vectơ riêng. Vì vậy hãy viết $x$ như một tổ hợp của các vectơ riêng và *giải thích tại sao tất cả các "số hạng chéo"* $x_i^T x_j = 0$. Khi đó $x^T Sx$ là $(c_1 x_1 + \dots + c_n x_n)^T (c_1 \lambda_1 x_1 + \dots + c_n \lambda_n x_n) = c_1^2 \lambda_1 x_1^T x_1 + \dots + c_n^2 \lambda_n x_n^T x_n > 0$.

**20** Hãy đưa ra một lý do nhanh tại sao mỗi phát biểu sau là đúng:
(a) Mọi ma trận xác định dương đều khả nghịch.
(b) Ma trận chiếu xác định dương duy nhất là $P = I$.
(c) Một ma trận đường chéo với các phần tử trên đường chéo dương là xác định dương.
(d) Một ma trận đối xứng với định thức dương có thể không xác định dương!

**Các bài toán 21-24 sử dụng các trị riêng; Các bài toán 25-27 dựa trên các phần tử chốt.**

**21** Đối với những giá trị $s$ và $t$ nào thì $S$ và $T$ có tất cả $\lambda > 0$ (do đó xác định dương)?
$$S = \begin{bmatrix} s & -4 & -4 \\ -4 & s & -4 \\ -4 & -4 & s \end{bmatrix} \quad \text{và} \quad T = \begin{bmatrix} t & 3 & 0 \\ 3 & t & 4 \\ 0 & 4 & t \end{bmatrix}$$

**22** Từ $S = Q\Lambda Q^T$, tính căn bậc hai đối xứng xác định dương $Q\sqrt{\Lambda}Q^T$ của mỗi ma trận. Kiểm tra rằng căn bậc hai này mang lại $A^T A = S$:
$$S = \begin{bmatrix} 5 & 4 \\ 4 & 5 \end{bmatrix} \quad \text{và} \quad S = \begin{bmatrix} 10 & 6 \\ 6 & 10 \end{bmatrix}.$$

**23** Bạn có thể đã thấy phương trình cho một hình elip là $x^2/a^2 + y^2/b^2 = 1$. $a$ và $b$ là gì khi phương trình được viết dưới dạng $\lambda_1 x^2 + \lambda_2 y^2 = 1$? Hình elip $9x^2 + 4y^2 = 1$ có các trục với nửa độ dài $a = \dots$ và $b = \dots$.

**24** Vẽ hình elip nghiêng $x^2 + xy + y^2 = 1$ và tìm các nửa độ dài của các trục của nó từ các trị riêng của ma trận $S$ tương ứng.

**25** Với các phần tử chốt dương trong $D$, phân tích $S = LDL^T$ trở thành $L\sqrt{D}\sqrt{D}L^T$. (Căn bậc hai của các chốt mang lại $D = \sqrt{D}\sqrt{D}$.) Khi đó $C = \sqrt{D}L^T$ mang lại *phân tích Cholesky* $A = C^T C$, đây là dạng "đối xứng hóa của $LU$":
Từ $C = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}$ tìm $S$. Từ $S = \begin{bmatrix} 4 & 8 \\ 8 & 25 \end{bmatrix}$ tìm $C = \text{chol}(S)$.

**26** Trong phân tích Cholesky $S = C^T C$, với $C = \sqrt{D}L^T$, căn bậc hai của các phần tử chốt nằm trên đường chéo của $C$. Tìm $C$ (tam giác trên) cho
$$S = \begin{bmatrix} 9 & 0 & 0 \\ 0 & 1 & 2 \\ 0 & 2 & 8 \end{bmatrix} \quad \text{và} \quad S = \begin{bmatrix} 1 & 1 & 1 \\ 2 & 2 & 2 \\ 1 & 2 & 7 \end{bmatrix}$$

**27** Phân tích đối xứng $S = LDL^T$ có nghĩa là $x^T Sx = x^T LDL^T x$:
$$\begin{bmatrix} x & y \end{bmatrix} \begin{bmatrix} a & b \\ b & c \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} x & y \end{bmatrix} \begin{bmatrix} 1 & 0 \\ b/a & 1 \end{bmatrix} \begin{bmatrix} a & 0 \\ 0 & (ac - b^2)/a \end{bmatrix} \begin{bmatrix} 1 & b/a \\ 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}.$$
Vế trái là $ax^2 + 2bxy + cy^2$. Vế phải là $a(x + \frac{b}{a}y)^2 + \frac{ac - b^2}{a}y^2$. Phần tử chốt thứ hai hoàn thành bình phương! Thử nghiệm với $a = 2, b = 4, c = 10$.

**28** Không cần nhân $S = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} 2 & 0 \\ 0 & 5 \end{bmatrix} \begin{bmatrix} \cos \theta & \sin \theta \\ -\sin \theta & \cos \theta \end{bmatrix}$, hãy tìm
(a) định thức của $S$
(b) các trị riêng của $S$
(c) các vectơ riêng của $S$
(d) một lý do tại sao $S$ là ma trận đối xứng xác định dương.

**29** Đối với $F_1(x, y) = \frac{1}{4}x^4 + x^2 y + y^2$ và $F_2(x, y) = x^3 + xy - x$, hãy tìm các ma trận đạo hàm bậc hai $S_1$ và $S_2$:
$$\text{Kiểm tra cực tiểu} \quad S = \begin{bmatrix} \partial^2 F / \partial x^2 & \partial^2 F / \partial x \partial y \\ \partial^2 F / \partial y \partial x & \partial^2 F / \partial y^2 \end{bmatrix} \text{ là xác định dương}$$
$S_1$ là xác định dương nên $F_1$ lõm lên (= lồi). Tìm điểm cực tiểu của $F_1$. Tìm điểm yên ngựa của $F_2$ (chỉ tìm ở những nơi đạo hàm bậc nhất bằng không).

**30** Đồ thị của $z = x^2 + y^2$ là một cái bát mở lên trên. Đồ thị của $z = x^2 - y^2$ là một cái yên ngựa. Đồ thị của $z = -x^2 - y^2$ là một cái bát úp xuống dưới. Bài kiểm tra nào trên $a, b, c$ để $z = ax^2 + 2bxy + cy^2$ có một điểm yên ngựa tại $(x, y) = (0, 0)$?

**31** Những giá trị nào của $c$ cho ra một cái bát và những giá trị $c$ nào cho ra một điểm yên ngựa đối với đồ thị của $z = 4x^2 + 12xy + cy^2$? Mô tả đồ thị này tại giá trị biên của $c$.

### Cực tiểu của Hàm số $F(x, y, z)$

Bạn mong đợi những bài kiểm tra nào cho một điểm cực tiểu? Đầu tiên là độ dốc bằng không:

**Các đạo hàm bậc nhất bằng không** $\frac{\partial F}{\partial x} = \frac{\partial F}{\partial y} = \frac{\partial F}{\partial z} = 0$ tại điểm cực tiểu.

Tiếp theo là phiên bản đại số tuyến tính của bài kiểm tra giải tích thông thường $d^2 f / dx^2 > 0$:

**Ma trận đạo hàm bậc hai $S$ là xác định dương** 
$$S = \begin{bmatrix} F_{xx} & F_{xy} & F_{xz} \\ F_{yx} & F_{yy} & F_{yz} \\ F_{zx} & F_{zy} & F_{zz} \end{bmatrix}$$

Ở đây $F_{xy} = \frac{\partial}{\partial x} \left( \frac{\partial F}{\partial y} \right) = \frac{\partial}{\partial y} \left( \frac{\partial F}{\partial x} \right) = F_{yx}$ là một đạo hàm bậc hai 'hỗn hợp'.

### **Các bài toán thử thách (Challenge Problems)**

**32** Một *nhóm* các ma trận không suy biến bao gồm $AB$ và $A^{-1}$ nếu nó bao gồm $A$ và $B$. "Các tích và các nghịch đảo luôn nằm trong nhóm." Nhóm nào trong số này là các nhóm (như ở Bài 2.7.37)? Hãy phát minh ra một "nhóm con" của hai nhóm này (không phải chỉ riêng rẽ $I = \text{nhóm nhỏ nhất}$).
(a) Các ma trận đối xứng xác định dương $S$.
(b) Các ma trận trực giao $Q$.
(c) Tất cả các hàm mũ $e^{tA}$ của một ma trận cố định $A$.
(d) Các ma trận $P$ có các trị riêng dương.
(e) Các ma trận $D$ có định thức bằng 1.

**33** Khi $S$ và $T$ đối xứng và xác định dương, $ST$ có thể thậm chí không đối xứng. Nhưng các trị riêng của nó vẫn dương. Bắt đầu từ $STx = \lambda x$ và lấy tích vô hướng với $Tx$. Sau đó chứng minh $\lambda > 0$.

**34** Viết ma trận sin $Q$ kích thước $5 \times 5$ từ Ví dụ có lời giải 6.5 C, chứa các vectơ riêng của $S$ khi $n = 5$ và $h = 1/6$. Nhân $SQ$ để thấy năm $\lambda$. Tổng các $\lambda$ phải bằng vết 10. Tích của chúng phải bằng $\det S = 6$.

**35** Giả sử $C$ xác định dương (nên $y^T Cy > 0$ bất cứ khi nào $y \neq 0$) và $A$ có các cột độc lập (nên $Ax \neq 0$ bất cứ khi nào $x \neq 0$). Áp dụng bài kiểm tra năng lượng cho $x^T A^T CAx$ để cho thấy rằng $S = A^T C A$ là xác định dương: *ma trận then chốt trong kỹ thuật.*

**36 Quan trọng!** Giả sử $S$ xác định dương với các trị riêng $\lambda_1 \geq \lambda_2 \geq \dots \geq \lambda_n$.
(a) Các trị riêng của ma trận $\lambda_1 I - S$ là gì? Nó có bán xác định dương không?
(b) Làm thế nào điều đó dẫn đến $\lambda_1 x^T x \geq x^T Sx$ đối với mọi $x$?
(c) Rút ra kết luận này: **Giá trị lớn nhất của** $x^T Sx / x^T x$ là $\lambda_1$.

**37** Đối với $a$ và $c$ nào thì ma trận này xác định dương? Đối với $a$ và $c$ nào thì nó bán xác định dương (điều này bao gồm cả xác định)?
$$S = \begin{bmatrix} a & a & a \\ a & a + c & a - c \\ a & a - c & a + c \end{bmatrix} \quad \text{Có thể dùng cả 5 bài kiểm tra.}$$
Năng lượng $x^T Sx$ bằng $a(x_1 + x_2 + x_3)^2 + c(x_2 - x_3)^2$.

# **Bảng Các Trị riêng và Vectơ riêng (Table of Eigenvalues and Eigenvectors)**

Các tính chất của một ma trận được phản ánh trong các trị riêng và vectơ riêng của nó như thế nào? Câu hỏi này là nền tảng trong suốt Chương 6. Một bảng sắp xếp các sự thật chính có thể sẽ hữu ích. Dưới đây là các tính chất đặc biệt của các trị riêng $\lambda_i$ và các vectơ riêng $x_i$.

| Thuộc tính Ma trận | Trị riêng $\lambda$ | Vectơ riêng $x$ |
|---|---|---|
| **Đối xứng:** $S^T = S = Q\Lambda Q^T$ | các trị riêng thực | trực giao $x_i^T x_j = 0$ |
| **Trực giao:** $Q^T = Q^{-1}$ | tất cả $|\lambda| = 1$ | trực giao $x_i^T x_j = 0$ |
| **Phản đối xứng:** $A^T = -A$ | các $\lambda$ ảo | Trực giao $x_i^T x_j = 0$ |
| **Hermitian phức:** $\bar{A}^T = A$ | số thực | trực giao $x_i^T x_j = 0$ |
| **Xác định dương:** $x^T Sx > 0$ | tất cả $\lambda > 0$ | trực giao vì $S^T = S$ |
| **Markov:** $m_{ij} > 0, \sum m_{ij} = 1$ | $\lambda_{\text{max}} = 1$ | trạng thái ổn định $x > 0$ |
| **Đồng dạng:** $A = BCB^{-1}$ | $\lambda(A) = \lambda(C)$ | $B$ nhân vectơ riêng của $C$ |
| **Phép chiếu:** $P = P^2 = P^T$ | $\lambda = 1; 0$ | không gian cột; không gian null |
| **Phép quay mặt phẳng: cos-sin** | $e^{i\theta}$ và $e^{-i\theta}$ | $x = (1, i)$ và $(1, -i)$ |
| **Phép phản xạ:** $I - 2uu^T$ | $\lambda = -1; 1, \dots, 1$ | $u$; toàn bộ mặt phẳng $u^\perp$ |
| **Hạng 1:** $uv^T$ | $\lambda = v^T u; 0, \dots, 0$ | $u$; toàn bộ mặt phẳng $v^\perp$ |
| **Nghịch đảo:** $A^{-1}$ | $1/\lambda(A)$ | giữ nguyên vectơ riêng của $A$ |
| **Dịch chuyển:** $A + cI$ | $\lambda(A) + c$ | giữ nguyên vectơ riêng của $A$ |
| **Lũy thừa Ổn định:** $A^n \rightarrow 0$ | tất cả $|\lambda| < 1$ | bất kỳ vectơ riêng nào |
| **Hàm mũ Ổn định:** $e^{At} \rightarrow 0$ | tất cả $\text{Re}(\lambda) < 0$ | bất kỳ vectơ riêng nào |
| **Hoán vị Vòng:** $P_{i,i+1} = 1, P_{n,1} = 1$ | $\lambda_k = e^{2\pi i k/n} = \text{căn của } 1$ | $x_k = (1, \lambda_k, \dots, \lambda_k^{n-1})$ |
| **Circulant:** $c_0 I + c_1 P + \dots$ | $\lambda_k = c_0 + c_1 e^{2\pi i k/n} + \dots$ | $x_k = (1, \lambda_k, \dots, \lambda_k^{n-1})$ |
| **Ba đường chéo:** $-1, 2, -1$ | $\lambda_k = 2 - 2 \cos(k\pi/(n+1))$ | $x_k = (\sin(k\pi/(n+1)), \dots)$ |
| **Chéo hóa được:** $A = X\Lambda X^{-1}$ | nằm trên đường chéo của $\Lambda$ | các cột của $X$ độc lập |
| **Schur:** $A = QTQ^{-1}$ | nằm trên đường chéo của $T$ | các cột của $Q$ |
| **Jordan:** $A = BJB^{-1}$ | nằm trên đường chéo của $J$ | mỗi khối cho 1 vectơ riêng |
| **SVD:** $A = U\Sigma V^T$ | $r$ giá trị suy biến trong $\Sigma$ | vectơ riêng của $A^T A, AA^T$ trong $V, U$ |

