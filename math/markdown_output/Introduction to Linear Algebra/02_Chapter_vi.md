# **Chương 2**

# **Giải Hệ Phương Trình Tuyến Tính (Solving Linear Equations)**

# **2.1 Các Vectơ và Hệ Phương Trình Tuyến Tính**

**Bức tranh cột (column picture)** của $Ax = b$: một tổ hợp của $n$ cột của $A$ tạo ra vectơ $b$.

**Bức tranh cột của** $Ax = b$: một tổ hợp của $n$ cột của $A$ tạo ra vectơ $b$. Đây là một phương trình vectơ $Ax = x_1a_1 + \dots + x_n a_n = b$: các cột của $A$ là $a_1, a_2, \dots, a_n$. Khi $b = 0$, một tổ hợp $Ax$ của các cột bằng *không:* một khả năng là $x = (0, \dots, 0)$. **Bức tranh hàng của** $Ax = b$: $m$ phương trình từ $m$ hàng cho $m$ mặt phẳng giao nhau tại $x$. Một tích vô hướng cho phương trình của mỗi mặt phẳng: (hàng 1) $\cdot x = b_1$, $\dots$, (**hàng** $m$) $\cdot x = b_m$. Khi $b = 0$, tất cả các mặt phẳng (**hàng** $i$) $\cdot x = 0$ đi qua điểm trung tâm $x = (0, 0, \dots, 0)$.

Bài toán trung tâm của đại số tuyến tính là giải một hệ phương trình. Những phương trình đó là tuyến tính, có nghĩa là các ẩn số chỉ được nhân với các hằng số - chúng ta không bao giờ thấy $x$ nhân với $y$. Hệ tuyến tính đầu tiên của chúng ta rất nhỏ. Nhưng bạn sẽ thấy nó dẫn đi xa đến mức nào:

| **Hai phương trình** | $x$  | $- 2y$ | $=$ | 1  |
|----------------------|------|--------|-----|----|
| **Hai ẩn số**        | $3x$ | $+ 2y$ | $=$ | 11 |

Chúng ta bắt đầu *từng hàng một*. Phương trình đầu tiên $x - 2y = 1$ tạo ra một đường thẳng trong mặt phẳng $xy$. Điểm $x = 1$, $y = 0$ nằm trên đường thẳng bởi vì nó thỏa mãn phương trình đó. Điểm $x = 3$, $y = 1$ cũng nằm trên đường thẳng bởi vì $3 - 2 = 1$. Nếu chúng ta chọn $x = 101$, chúng ta tìm được $y = 50$.

Độ dốc của đường thẳng cụ thể này là $1/2$, bởi vì $y$ tăng thêm $1$ khi $x$ thay đổi $2$. Nhưng độ dốc thì quan trọng trong giải tích và đây là đại số tuyến tính!

Hình 2.1 sẽ hiển thị đường thẳng đầu tiên đó $x - 2y = 1$. Đường thẳng thứ hai trong "bức tranh hàng" này đến từ phương trình thứ hai $3x + 2y = 11$. Bạn không thể bỏ lỡ điểm $x = 3$, $y = 1$ nơi hai đường thẳng cắt nhau. *Điểm đó* $(3, 1)$ *nằm trên cả hai đường thẳng và giải cả hai phương trình.*

![](images/_page_41_Figure_2.jpeg)

Hình 2.1: *Bức tranh hàng:* Điểm $(3, 1)$ nơi các đường thẳng giao nhau giải cả hai phương trình.

### **CÁC HÀNG (ROWS)** *Bức tranh hàng hiển thị hai đường thẳng gặp nhau tại một điểm duy nhất (nghiệm).*

Bây giờ hãy chuyển sang bức tranh cột. Tôi muốn nhận dạng cùng một hệ tuyến tính như một "phương trình vectơ". Thay vì các con số, chúng ta cần nhìn thấy các *vectơ*. Nếu bạn tách hệ ban đầu thành các cột của nó thay vì các hàng, bạn sẽ nhận được một phương trình vectơ:

| Tổ hợp bằng $b$ | $x \begin{bmatrix} 1 \\ 3 \end{bmatrix} + y \begin{bmatrix} -2 \\ 2 \end{bmatrix} = \begin{bmatrix} 1 \\ 11 \end{bmatrix} = b.$ | (2) |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------|-----|
|------------------------|---------------------------------------------------------------------------------------------------------------------------------|-----|

Phương trình này có hai vectơ cột ở vế trái. Vấn đề là *tìm tổ hợp của các vectơ đó bằng với vectơ ở vế phải.* Chúng ta nhân cột đầu tiên với $x$ và cột thứ hai với $y$, và cộng lại. Với các lựa chọn đúng $x = 3$ và $y = 1$ (cùng các con số như trước), điều này tạo ra $3$ *(cột 1)* + $1$ *(cột 2)* = $b$.

**CÁC CỘT (COLUMNS)** *Bức tranh cột kết hợp các vectơ cột ở vế trái để tạo ra vectơ $b$ ở vế phải.*

Hình 2.2 là "bức tranh cột" của hai phương trình hai ẩn. Phần đầu tiên hiển thị hai cột riêng biệt, và cột đầu tiên đó được nhân với 3. Phép nhân với một *vô hướng (scalar)* (một con số) này là một trong hai phép toán cơ bản trong đại số tuyến tính:

| Phép nhân vô hướng | $3 \begin{bmatrix} 1 \\ 3 \end{bmatrix} = \begin{bmatrix} 3 \\ 9 \end{bmatrix}$ |
|-----------------------|---------------------------------------------------------------------------------|
|-----------------------|---------------------------------------------------------------------------------|

Nếu các thành phần của một vectơ $v$ là $v_1$ và $v_2$, thì $cv$ có các thành phần $cv_1$ và $cv_2$.

Phép toán cơ bản khác là *phép cộng vectơ*. Chúng ta cộng riêng các thành phần đầu tiên và các thành phần thứ hai. Tổng vectơ là $(1, 11)$, là vectơ $b$ mong muốn.

| Phép cộng vectơ | $\begin{bmatrix} 3 \\ 9 \end{bmatrix} + \begin{bmatrix} -2 \\ 2 \end{bmatrix} = \begin{bmatrix} 1 \\ 11 \end{bmatrix}$ |
|-----------------|------------------------------------------------------------------------------------------------------------------------|
|                 |                                                                                                                        |

Phía bên phải của Hình 2.2 hiển thị phép cộng này. Hai vectơ có màu đen. Tổng dọc theo đường chéo là vectơ $b = (1, 11)$ ở vế phải của các phương trình tuyến tính.

![](images/_page_42_Figure_2.jpeg)

Hình 2.2: *Bức tranh cột:* Một tổ hợp các cột tạo ra vế phải $(1, 11)$.

Nhắc lại: Vế trái của phương trình vectơ là một *tổ hợp tuyến tính (linear combination)* của các cột. Bài toán là tìm đúng các hệ số $x = 3$ và $y = 1$. Chúng ta đang kết hợp phép nhân vô hướng và phép cộng vectơ vào một bước. Bước đó cực kỳ quan trọng, bởi vì nó chứa cả hai phép toán cơ bản: *Nhân với 3 và 1, sau đó cộng lại.*

| Tổ hợp tuyến tính | $3 \begin{bmatrix} 1 \\ 3 \end{bmatrix} + 1 \begin{bmatrix} -2 \\ 2 \end{bmatrix} = \begin{bmatrix} 1 \\ 11 \end{bmatrix}$ |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
|                    |                                                                                                                        |

Tất nhiên nghiệm $x = 3$, $y = 1$ cũng giống như trong bức tranh hàng. Tôi không biết bạn thích bức tranh nào hơn! Tôi nghi ngờ rằng hai đường thẳng cắt nhau quen thuộc hơn lúc ban đầu. Bạn có thể thích bức tranh hàng hơn, nhưng chỉ trong một ngày. Sự ưu tiên của riêng tôi là kết hợp các vectơ cột. Sẽ dễ dàng hơn nhiều để nhìn thấy một tổ hợp của bốn vectơ trong không gian bốn chiều, so với việc hình dung làm thế nào bốn siêu phẳng có thể gặp nhau tại một điểm. *(Thậm chí một siêu phẳng đã đủ khó rồi...)*

*Ma trận hệ số (coefficient matrix)* ở vế trái của các phương trình là ma trận 2 x 2 $A$:

| Ma trận hệ số | $A = \begin{bmatrix} 1 & -2 \\ 3 & 2 \end{bmatrix}$ |
|--------------------|-----------------------------------------------------|
|--------------------|-----------------------------------------------------|

Điều này rất điển hình trong đại số tuyến tính, để nhìn vào một ma trận theo các hàng và theo các cột. Các hàng của nó cho bức tranh hàng và các cột của nó cho bức tranh cột. Cùng các con số, những bức tranh khác nhau, cùng những phương trình. Chúng ta kết hợp những phương trình đó vào một bài toán ma trận $Ax = b$:

| Phương trình ma trận | $\begin{bmatrix} 1 & -2 \\ 3 & 2 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 1 \\ 11 \end{bmatrix}$ |
|-----------------|------------------------------------------------------------------------------------------------------------------------------|
| $Ax = b$        |                                                                                                                              |

Bức tranh hàng liên quan đến hai hàng của $A$. Bức tranh cột kết hợp các cột. Các con số $x = 3$ và $y = 1$ đi vào vectơ $x$. Đây là phép nhân ma trận-vectơ:

| Các tích vô hướng với các hàng | $Ax = b$ | là | $\begin{bmatrix} 1 & -2 \\ 3 & 2 \end{bmatrix} \begin{bmatrix} 3 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 11 \end{bmatrix}$ |
|------------------------|----------|----|------------------------------------------------------------------------------------------------------------------------------|
| Tổ hợp của các cột |          |    |                                                                                                                              |

*Nhìn xa hơn* Chương này sẽ giải $n$ phương trình với $n$ ẩn số (cho mọi $n$). Tôi không đi với tốc độ tối đa, bởi vì các hệ nhỏ cho phép có các ví dụ, hình ảnh và một sự hiểu biết hoàn chỉnh. Bạn có thể tự do đi nhanh hơn, miễn là **phép nhân ma trận và nghịch đảo** trở nên rõ ràng. Hai ý tưởng đó sẽ là chìa khóa cho các ma trận khả nghịch.

Tôi có thể liệt kê bốn bước để hiểu phép khử (elimination) bằng cách sử dụng các ma trận.

- **1.** Phép khử đi từ $A$ đến một ma trận tam giác $U$ bằng một chuỗi các phép toán ma trận $E_{ij}$.
- **2.** Hệ tam giác được giải bằng *phép thế ngược (back substitution):* làm việc từ dưới lên trên.
- **3.** Bằng ngôn ngữ ma trận $A$ được phân tích thành $LU$ = (tam giác dưới) (tam giác trên).
- **4.** Phép khử thành công nếu $A$ khả nghịch. (Nhưng nó có thể cần hoán đổi các hàng.)

Thuật toán được sử dụng nhiều nhất trong khoa học tính toán thực hiện các bước này (MATLAB gọi nó là **lu**). Dạng nhanh nhất của nó là dấu gạch chéo ngược: $x = A \setminus b$. Nhưng đại số tuyến tính vượt ra ngoài các ma trận vuông khả nghịch! Từ các ma trận $m \times n$, $Ax = 0$ có thể có nhiều nghiệm. Những nghiệm đó sẽ đi vào một **không gian vectơ (vector space)**. **Hạng (rank)** của $A$ dẫn đến **số chiều (dimension)** của không gian vectơ đó.

Tất cả điều này sẽ đến trong Chương 3, và tôi không muốn vội vã. Nhưng tôi phải đạt được điều đó.

### **Ba Phương trình Ba Ẩn**

Ba ẩn số là $x, y, z$. Chúng ta có ba phương trình tuyến tính:

$$Ax = b \quad \begin{cases} x + 2y + 3z = 6 \\ 2x + 5y + 2z = 4 \\ 6x - 3y + z = 2 \end{cases} \quad (3)$$

Chúng ta tìm kiếm các con số $x, y, z$ giải cả ba phương trình cùng một lúc. Những con số mong muốn đó có thể tồn tại hoặc không. Đối với hệ này, chúng thực sự tồn tại. Khi số lượng ẩn số khớp với số lượng phương trình, trong trường hợp này là 3 = 3, *thường* có một nghiệm duy nhất.

Trước khi giải bài toán, chúng ta hình dung nó theo cả hai cách:

**HÀNG** *Bức tranh hàng hiển thị ba mặt phẳng cắt nhau tại một điểm duy nhất.*

**CỘT** *Bức tranh cột kết hợp ba cột để tạo ra $b = (6, 4, 2)$.*

Trong bức tranh hàng, mỗi phương trình tạo ra một *mặt phẳng* trong không gian ba chiều. Mặt phẳng đầu tiên trong Hình 2.3 xuất phát từ phương trình đầu tiên $x + 2y + 3z = 6$. Mặt phẳng đó cắt các trục $x$, $y$ và $z$ tại các điểm $(6, 0, 0)$, $(0, 3, 0)$ và $(0, 0, 2)$. Ba điểm đó thỏa mãn phương trình và chúng xác định toàn bộ mặt phẳng.

Vectơ $(x, y, z) = (0, 0, 0)$ không giải được $x + 2y + 3z = 6$. Do đó mặt phẳng đó không chứa gốc tọa độ. Mặt phẳng $x + 2y + 3z = 0$ thì đi qua gốc tọa độ, và nó song song với $x + 2y + 3z = 6$. Khi vế phải tăng lên 6, mặt phẳng song song di chuyển ra xa gốc tọa độ.

Mặt phẳng thứ hai được cho bởi phương trình thứ hai $2x + 5y + 2z = 4$. *Nó giao với mặt phẳng đầu tiên trên một đường thẳng $L$.* Kết quả thông thường của hai phương trình ba ẩn là một đường thẳng $L$ chứa các nghiệm. (Sẽ không như vậy nếu các phương trình là $x + 2y + 3z = 6$ và $x + 2y + 3z = 0$.)

Phương trình thứ ba cho một mặt phẳng thứ ba. Nó cắt đường thẳng $L$ tại một điểm duy nhất. Điểm đó nằm trên cả ba mặt phẳng và nó giải cả ba phương trình. Thật khó để vẽ điểm giao cắt ba lần này hơn là tưởng tượng nó. Ba mặt phẳng gặp nhau tại điểm nghiệm (mà chúng ta chưa tìm thấy). **Dạng cột bây giờ sẽ cho thấy ngay tại sao** $z = 2$.

![](images/_page_44_Picture_5.jpeg)

![](images/_page_44_Diagram_6.jpeg)

Hình 2.3: *Bức tranh hàng:* Hai mặt phẳng giao nhau tại một đường thẳng $L$. Ba mặt phẳng gặp nhau tại một điểm.

*Bức tranh cột bắt đầu với dạng vectơ của các phương trình $Ax = b$:*

| Kết hợp các cột | $x \begin{bmatrix} 1 \\ 2 \\ 6 \end{bmatrix} + y \begin{bmatrix} 2 \\ 5 \\ -3 \end{bmatrix} + z \begin{bmatrix} 3 \\ 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 6 \\ 4 \\ 2 \end{bmatrix} = b.$ | (4) |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|

Các ẩn số là các hệ số $x, y, z$. Chúng ta muốn nhân ba vectơ cột với các con số đúng $x, y, z$ để tạo ra $b = (6, 4, 2)$.

Hình 2.4 hiển thị bức tranh cột này. Các tổ hợp tuyến tính của những cột đó có thể tạo ra bất kỳ vectơ $b$ nào! Tổ hợp tạo ra $b = (6, 4, 2)$ chỉ là 2 lần cột thứ ba. *Các hệ số chúng ta cần là $x = 0$, $y = 0$, và $z = 2$.*

Ba mặt phẳng trong bức tranh hàng gặp nhau tại cùng điểm nghiệm đó $(0, 0, 2)$:

| **Tổ hợp đúng** | $0 \begin{bmatrix} 1 \\ 2 \\ 6 \end{bmatrix} + 0 \begin{bmatrix} 2 \\ 5 \\ -3 \end{bmatrix} + 2 \begin{bmatrix} 3 \\ 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 6 \\ 4 \\ 2 \end{bmatrix}$ |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

![](images/_page_45_Diagram_2.jpeg)

Hình 2.4: *Bức tranh cột: Kết hợp các cột với các trọng số $(x, y, z) = (0, 0, 2)$.*

### **Dạng Ma trận của Phương trình**

Chúng ta có ba hàng trong bức tranh hàng và ba cột trong bức tranh cột (cộng với vế phải). Ba hàng và ba cột chứa chín con số. *Chín con số này điền vào một ma trận 3 x 3 $A$:*

| "Ma trận hệ số" trong $Ax = b$ là | $A =$ | $\begin{bmatrix} 1 & 2 & 3 \\ 2 & 5 & 2 \\ 6 & -3 & 1 \end{bmatrix}$ |
|-----------------------------------------|-------|----------------------------------------------------------------------|
|-----------------------------------------|-------|----------------------------------------------------------------------|

Chữ cái in hoa $A$ đại diện cho tất cả chín hệ số (trong mảng vuông này). Chữ cái $b$ biểu thị vectơ cột với các thành phần 6, 4, 2. Ẩn số $x$ cũng là một vectơ cột, với các thành phần $x, y, z$. (Chúng ta sử dụng chữ in đậm bởi vì nó là một vectơ, $x$ bởi vì nó là một ẩn số.) Theo các hàng, các phương trình là (3), theo các cột chúng là (4), và bằng ma trận chúng là (5):

*Phương trình ma trận $Ax = b$* $\quad \begin{bmatrix} 1 & 2 & 3 \\ 2 & 5 & 2 \\ 6 & -3 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 6 \\ 4 \\ 2 \end{bmatrix}$. (5)

*Câu hỏi cơ bản:* **"Nhân $A$ với $x$" có nghĩa là gì?** Chúng ta có thể nhân theo hàng hoặc theo cột. Dù theo cách nào, $Ax = b$ phải là một phát biểu đúng đắn của ba phương trình. Bạn thực hiện cùng chín phép nhân dù theo cách nào.

*Phép nhân theo các hàng $Ax$* xuất phát từ **các tích vô hướng,** mỗi hàng nhân với cột $x$:

$$Ax = \begin{bmatrix} (\text{hàng } 1) \cdot x \\ (\text{hàng } 2) \cdot x \\ (\text{hàng } 3) \cdot x \end{bmatrix}. \quad (6)$$

*Phép nhân theo các cột $Ax$* là một *tổ hợp của các vectơ cột:*

| $x = x(\text{cột } 1) + y(\text{cột } 2) + z(\text{cột } 3)$ | (7) |
|-----------------------------------------------------------------------|-----|
|-----------------------------------------------------------------------|-----|

Khi chúng ta thay nghiệm $x = (0, 0, 2)$, phép nhân $Ax$ tạo ra $b$:

$$\begin{bmatrix} 1 & 2 & 3 \\ 2 & 5 & 2 \\ 6 & -3 & 1 \end{bmatrix} \begin{bmatrix} 0 \\ 0 \\ 2 \end{bmatrix} = 2 \text{ lần cột } 3 = \begin{bmatrix} 6 \\ 4 \\ 2 \end{bmatrix}.$$

Tích vô hướng từ hàng đầu tiên là $(1, 2, 3) \cdot (0, 0, 2) = 6$. Các hàng khác cho ra các tích vô hướng 4 và 2. *Cuốn sách này coi $Ax$ như một tổ hợp của các cột của $A$.*

**Ví dụ 1** Đây là các ma trận 3 x 3 $A$ và $I$ = ma trận đơn vị, với ba số 1 và sáu số 0:

| $Ax = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 0 & 0 \\ 1 & 0 & 0 \end{bmatrix}$ | $\begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix} = \begin{bmatrix} 4 \\ 4 \\ 4 \end{bmatrix}$ | $Ix = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ | $\begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix} = \begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix}$ |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|

Nếu bạn là một người theo hệ hàng (row person), tích vô hướng của $(1, 0, 0)$ với $(4, 5, 6)$ là 4. Nếu bạn là một người theo hệ cột (column person), tổ hợp tuyến tính $Ax$ là 4 lần cột đầu tiên $(1, 1, 1)$. Trong ma trận $A$ đó, cột thứ hai và thứ ba là các vectơ không.

Ma trận $I$ khác là đặc biệt. Nó có các số 1 trên "đường chéo chính". *Bất kể vectơ nào mà ma trận này nhân vào, vectơ đó không bị thay đổi.* Điều này giống như phép nhân với 1, nhưng dành cho ma trận và vectơ. Ma trận ngoại lệ trong ví dụ này là *ma trận đơn vị (identity matrix)* 3 x 3:

| $I = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ | luôn mang lại phép nhân | $Ix = x$ |
|-------------------------------------------------------------------------|----------------------------------|----------|
|-------------------------------------------------------------------------|----------------------------------|----------|

#### **Ký hiệu Ma trận (Matrix Notation)**

Hàng đầu tiên của ma trận 2 x 2 chứa $a_{11}$ và $a_{12}$. Hàng thứ hai chứa $a_{21}$ và $a_{22}$. Chỉ số đầu tiên chỉ số hàng, do đó $a_{ij}$ là một phần tử ở hàng $i$. Chỉ số thứ hai $j$ chỉ số cột. Nhưng những chỉ số dưới đó không thuận tiện lắm trên bàn phím! Thay vì $a_{ij}$, chúng ta gõ $A(i,j)$. *Phần tử* $a_{57} = A(5, 7)$ *sẽ ở hàng* 5, *cột* 7.

$$A = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix} = \begin{bmatrix} A(1,1) & A(1,2) \\ A(2,1) & A(2,2) \end{bmatrix}$$

Đối với một ma trận $m \times n$, chỉ số hàng $i$ đi từ 1 đến $m$. Chỉ số cột $j$ dừng ở $n$. Có $mn$ phần tử $a_{ij} = A(i, j)$. Một ma trận vuông cấp $n$ có $n^2$ phần tử.

# **Phép nhân trong MATLAB**

Tôi muốn biểu diễn $A$ và $x$ và tích $Ax$ của chúng bằng các lệnh MATLAB. Đây là bước đầu tiên để học ngôn ngữ đó (và các ngôn ngữ khác). Tôi bắt đầu bằng việc định nghĩa $A$ và $x$. Một vectơ $x$ trong $\mathbb{R}^n$ là một ma trận $n \times 1$ (như trong cuốn sách này). Nhập các ma trận *từng hàng một*, và sử dụng dấu chấm phẩy để báo hiệu kết thúc một hàng. Hoặc nhập theo cột và chuyển vị bằng dấu nháy đơn `'`:

| $A = [1 \quad 2 \quad 3; \quad 2 \quad 5 \quad 2; \quad 6 \quad -3 \quad 1]$ |
|------------------------------------------------------------------------------|
| $x = [0 \quad 2 \quad 2]'$                                                   |
| $x = [0; 0; 2]$                                                              |

Có ba cách để nhân $Ax$ trong MATLAB. Trên thực tế, $A * x$ là cách tốt để thực hiện điều đó. MATLAB là một ngôn ngữ cấp cao, và nó hoạt động với các ma trận:

# *Phép nhân ma trận $b = A * x$*

Chúng ta cũng có thể chọn ra hàng đầu tiên của $A$ (như một ma trận nhỏ hơn!). Ký hiệu cho ma trận con $1 \times 3$ đó là $A(1, :)$. **Ở đây ký hiệu dấu hai chấm `:` giữ tất cả các cột của hàng 1.**

**Từng hàng một**
$$b = [A(1,:) * x; A(2,:) * x; A(3,:) * x]$$

Mỗi phần tử của $b$ là một tích vô hướng, hàng nhân với cột, ma trận $1 \times 3$ nhân với ma trận $3 \times 1$.

Cách nhân khác sử dụng các cột của $A$. Cột đầu tiên là ma trận con $3 \times 1$ $A(:, 1)$. Bây giờ ký hiệu hai chấm `:` đứng trước, *để giữ tất cả các hàng của cột 1*. Cột này nhân với $x(1)$ và các cột khác nhân với $x(2)$ và $x(3)$:

**Từng cột một**
$$b = A(:, 1) * x(1) + A(:, 2) * x(2) + A(:, 3) * x(3)$$

Tôi nghĩ rằng các ma trận được lưu trữ theo các cột. Sau đó nhân từng cột một sẽ nhanh hơn một chút. Do đó $A * x$ thực sự được thực thi theo các cột.

### **Các ngôn ngữ lập trình cho Toán học và Thống kê**

Dưới đây là năm ngôn ngữ quan trọng hơn và các lệnh của chúng cho phép nhân $Ax$:

| Julia       | $A * x$          | julialang.org           |
|-------------|------------------|-------------------------|
| Python      | dot($A$, $x$) | python.org              |
| R           | $A \%*\% x$    | r-project.org           |
| Mathematica | $A . x$          | wolfram.com/mathematica |
| Maple       | $A * x$          | maplesoft.com           |

**Julia, Python,** và **R** là các ngôn ngữ mã nguồn mở và miễn phí. R được phát triển đặc biệt cho các ứng dụng trong thống kê. Các phần mềm khác cho thống kê (SAS, JMP, và nhiều cái khác) được mô tả trên phần So sánh các Gói Thống kê của Wikipedia.

**Mathematica** và **Maple** cho phép các phần tử mang tính biểu tượng $a, b, x, \dots$ và không chỉ là các số thực. Cũng như trong Symbolic Toolbox của MATLAB, chúng làm việc với các biểu thức toán học như $x^2x$. Sức mạnh của Mathematica được thấy trong Wolfram Alpha.

**Julia** kết hợp năng suất cao của SciPy hoặc R cho tính toán kỹ thuật với hiệu suất có thể so sánh với C hoặc Fortran. Nó có thể gọi các thư viện Python và C/Fortran. Nhưng nó không phụ thuộc vào các hàm thư viện "vector hóa" (vectorized) để đạt tốc độ; Julia được thiết kế để trở nên nhanh chóng.

Tôi đã truy cập **juliabox.org**. Tôi đã nhấp vào *Sign in via Google* để truy cập không gian gmail của mình. Sau đó tôi nhấp vào *new* ở bên phải và chọn một notebook Julia. Tôi đã chọn 0.4.5 và không phải là một phiên bản đang phát triển. Dòng lệnh Julia xuất hiện ngay lập tức.

Là một người mới bắt đầu, tôi đã tính toán 1 + 1. Để xem câu trả lời, tôi đã nhấn *Shift+Enter*. Tôi cũng học được rằng 1.0 + 1.0 sử dụng dấu phẩy động, nhanh hơn nhiều cho một bài toán lớn. Trang web **math.mit.edu/linearalgebra** sẽ cho thấy một phần sức mạnh của Julia, Python và R.

**Python** là một ngôn ngữ lập trình đa dụng phổ biến. Khi kết hợp với các gói như NumPy và thư viện SciPy, nó cung cấp một môi trường đầy đủ tính năng cho tính toán kỹ thuật. NumPy có các lệnh đại số tuyến tính cơ bản. Tải bản phân phối Anaconda Python từ **https://www.continuum.io** (một tập hợp được đóng gói sẵn của Python và các thư viện toán học quan trọng nhất, với trình cài đặt đồ họa).

**R** là phần mềm miễn phí dùng để tính toán thống kê và đồ họa. Để tải và cài đặt R, hãy truy cập **r-project.org** (tiền tố **https://www.**). Các lệnh được nhắc bởi `>` và R là một ngôn ngữ kịch bản. Nó hoạt động với các danh sách có thể được định hình thành các vectơ và ma trận.

Điều quan trọng là nên đề xuất RStudio cho việc soạn thảo và vẽ đồ thị (và các tài nguyên trợ giúp). Khi bạn tải từ **www.RStudio.com**, một cửa sổ mở ra cho các lệnh R - cùng với các cửa sổ để chỉnh sửa và quản lý các tệp và đồ thị. Báo cho R biết dạng của ma trận cũng như danh sách các phần tử số:

`>A = matrix(c(1, 2, 3, 2, 5, 2, 6, -3, 1), nrow = 3, byrow = TRUE)`
`> x = matrix(c(0, 0, 2), nrow = 3)`

Để xem $A$ và $x$, hãy gõ tên của chúng tại dấu nhắc mới `>`. Để nhân hãy gõ `b = A%*%x`. Chuyển vị bằng `t(A)` và sử dụng `as.matrix` để chuyển một vectơ thành một ma trận.

MATLAB và Julia có một cú pháp rõ ràng hơn cho các tính toán ma trận so với R. Nhưng R đã trở nên rất quen thuộc và được sử dụng rộng rãi. Trang web của cuốn sách này có không gian cho các bản demo thích hợp (bao gồm lệnh *Manipulate*) của **MATLAB** và **Julia** và **Python** và **R.**

#### **• ÔN TẬP CÁC Ý TƯỞNG CHÍNH •**

- **1.** Các phép toán cơ bản trên các vectơ là phép nhân $cv$ và phép cộng vectơ $v + w$.
- **2.** Cùng với nhau, các phép toán đó cho các *tổ hợp tuyến tính (linear combinations)* $cv + dw$.
- **3.** Phép nhân ma trận-vectơ $Ax$ có thể được tính bằng các tích vô hướng, từng hàng một. Nhưng $Ax$ phải được hiểu như là một *tổ hợp của các cột của $A$.*
- **4.** Bức tranh cột: $Ax = b$ yêu cầu một tổ hợp của các cột để tạo ra $b$.
- 5. Bức tranh hàng: Mỗi phương trình trong $Ax = b$ cho một đường thẳng ($n = 2$) hoặc một mặt phẳng ($n = 3$) hoặc một "siêu phẳng" ($n > 3$). Chúng giao nhau tại nghiệm hoặc các nghiệm, nếu có.

#### **• CÁC VÍ DỤ ĐÃ GIẢI •**

**2.1 A** Mô tả bức tranh cột của ba phương trình $Ax = b$ này. Giải bằng cách kiểm tra cẩn thận các cột (thay vì khử):

Nếu các cột (thay vì khử):
$$\begin{array}{ccccccc} x + 3y + 2z = -3 & & & & & & \\ 2x + 2y + 2z = -2 & & \text{có nghĩa là} & & & & \\ 3x + 5y + 6z = -5 & & & & & & \end{array} \quad \begin{bmatrix} 1 & 3 & 2 \\ 2 & 2 & 2 \\ 3 & 5 & 6 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} -3 \\ -2 \\ -5 \end{bmatrix}.$$

**Lời giải** Bức tranh cột yêu cầu một tổ hợp tuyến tính tạo ra $b$ từ ba cột của $A$. Trong ví dụ này $b$ là *trừ đi cột thứ hai.* Vậy nên nghiệm là $x = 0$, $y = -1$, $z = 0$. Để chỉ ra rằng $(0, -1, 0)$ là nghiệm *duy nhất*, chúng ta phải biết rằng "$A$ là khả nghịch" và "các cột là độc lập" và "định thức không bằng không."

Những từ ngữ đó chưa được định nghĩa nhưng bài kiểm tra đến từ phép khử: Chúng ta cần (và cho ma trận này chúng ta tìm thấy) một tập hợp đầy đủ gồm ba phần tử xoay (pivots) khác không.

Giả sử vế phải thay đổi thành $b = (4, 4, 8) =$ tổng của hai cột đầu tiên. Khi đó tổ hợp đúng có $x = 1, y = 1, z = 0$. Nghiệm trở thành $x = (1, 1, 0)$.

**2.1 B** Hệ này *không có nghiệm*. Các mặt phẳng trong bức tranh hàng không gặp nhau tại một điểm. *Không có tổ hợp nào của ba cột tạo ra $b$. Làm thế nào để chỉ ra điều này?*

| $x + 3y + 5z = 4$  | $\begin{bmatrix} 1 & 3 & 5 \\ 1 & 2 & -3 \\ 2 & 5 & 2 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 4 \\ 5 \\ 8 \end{bmatrix} = b$ |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| $x + 2y - 3z = 5$  |                                                                                                                                                                |
| $2x + 5y + 2z = 8$ |                                                                                                                                                                |

*Ý tưởng* Lấy (phương trình 1) + (phương trình 2) - (phương trình 3). Kết quả là $0 = 1$. Hệ này không thể có nghiệm. Chúng ta có thể nói: Vectơ $(1, 1, -1)$ trực giao với cả ba cột của $A$ nhưng *không* trực giao với $b$.

- **(1)** Có bất kỳ hai mặt phẳng nào trong ba mặt phẳng song song với nhau không? Các phương trình của các mặt phẳng song song với $x + 3y + 5z = 4$ là gì?
- **(2)** Lấy tích vô hướng của mỗi cột của $A$ (và cả $b$) với $y = (1, 1, -1)$. Các tích vô hướng đó cho thấy thế nào rằng không có tổ hợp nào của các cột bằng với $b$?
- **(3)** Tìm ba vectơ vế phải $b^*$ và $b^{**}$ và $b^{***}$ khác nhau mà *có* cho phép các nghiệm.

#### **Lời giải**

- **(1)** Các mặt phẳng không gặp nhau tại một điểm, mặc dù không có hai mặt phẳng nào song song. Đối với một mặt phẳng song song với $x + 3y + 5z = 4$, hãy thay đổi số "4". Mặt phẳng song song $x + 3y + 5z = 0$ đi qua gốc tọa độ $(0, 0, 0)$. Và phương trình nhân với bất kỳ hằng số khác không nào vẫn cho cùng một mặt phẳng, như trong $2x + 6y + 10z = 8$.
- **(2)** Tích vô hướng của mỗi cột của $A$ với $y = (1, 1, -1)$ là *bằng không*. Ở vế phải, $y \cdot b = (1, 1, -1) \cdot (4, 5, 8) = 1$ *không bằng không*. $Ax = b$ dẫn đến $0 = 1$: **không có nghiệm.**
- **(3)** Có một nghiệm khi $b$ là một tổ hợp của các cột. Ba lựa chọn $b$ này có các nghiệm bao gồm $x^* = (1, 0, 0)$ và $x^{**} = (1, 1, 1)$ và $x^{***} = (0, 0, 0)$:

$$b^* = \begin{bmatrix} 1 \\ 1 \\ 2 \end{bmatrix} = \text{cột đầu tiên} \quad b^{**} = \begin{bmatrix} 9 \\ 0 \\ 9 \end{bmatrix} = \text{tổng của các cột} \quad b^{***} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$$

## **Bài tập 2.1 (Problem Set 2.1)**

**Các bài toán 1-8 liên quan đến bức tranh hàng và bức tranh cột của $Ax = b$.**

**1** Với $A = I$ (ma trận đơn vị), hãy vẽ các mặt phẳng trong bức tranh hàng. Ba mặt của một hình hộp giao nhau tại nghiệm $x = (x, y, z) = (2, 3, 4)$:

| $1x + 0y + 0z = 2$ |      | $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ | $\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 2 \\ 3 \\ 4 \end{bmatrix}$ |
|--------------------|------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| $0x + 1y + 0z = 3$ | hoặc |                                                                     |                                                                                         |
| $0x + 0y + 1z = 4$ |      |                                                                     |                                                                                         |

Vẽ các vectơ trong bức tranh cột. Hai lần cột 1 cộng ba lần cột 2 cộng bốn lần cột 3 bằng với vế phải $b$.

**2** Nếu các phương trình trong Bài toán 1 được nhân với 2, 3, 4 chúng trở thành $DX = B$:

| $2x + 0y + 0z = 4$  |      | $D\mathbf{X} = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 4 \end{bmatrix}$ | $\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 4 \\ 9 \\ 16 \end{bmatrix} = B$ |
|---------------------|------|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| $0x + 3y + 0z = 9$  | hoặc |                                                                                   |                                                                                              |
| $0x + 0y + 4z = 16$ |      |                                                                                   |                                                                                              |

Tại sao bức tranh hàng lại giống nhau? Nghiệm $X$ có giống như $x$ không? Điều gì đã bị thay đổi trong bức tranh cột - các cột hay là tổ hợp đúng để tạo ra $B$?

**3** Nếu phương trình 1 được cộng vào phương trình 2, thì điều nào trong số này bị thay đổi: các mặt phẳng trong bức tranh hàng, các vectơ trong bức tranh cột, ma trận hệ số, nghiệm số? Các phương trình mới trong Bài toán 1 sẽ là $x = 2$, $x + y = 5$, $z = 4$.

**4** Tìm một điểm có $z = 2$ trên đường thẳng giao tuyến của các mặt phẳng $x + y + 3z = 6$ và $x - y + z = 4$. Tìm điểm có $z = 0$. Tìm một điểm thứ ba nằm giữa hai điểm này.

**5** Phương trình đầu tiên trong số các phương trình này cộng phương trình thứ hai thì bằng phương trình thứ ba:

- $x + y + z = 2$
- $x + 2y + z = 3$
- $2x + 3y + 2z = 5$.

Hai mặt phẳng đầu tiên cắt nhau dọc theo một đường thẳng. Mặt phẳng thứ ba chứa đường thẳng đó, bởi vì nếu $x, y, z$ thỏa mãn hai phương trình đầu thì chúng cũng ____. Các phương trình này có vô số nghiệm (toàn bộ đường thẳng $L$). Hãy tìm ba nghiệm trên $L$.

**6** Dịch chuyển mặt phẳng thứ ba trong Bài toán 5 tới một mặt phẳng song song $2x + 3y + 2z = 9$. Bây giờ ba phương trình không có nghiệm - tại sao *không*? Hai mặt phẳng đầu tiên gặp nhau dọc theo đường thẳng $L$, nhưng mặt phẳng thứ ba không ____ đường thẳng đó.

**7** Trong Bài toán 5 các cột là $(1, 1, 2)$ và $(1, 2, 3)$ và $(1, 1, 2)$. Đây là một "trường hợp suy biến" bởi vì cột thứ ba là ____. Tìm hai tổ hợp của các cột tạo ra $b = (2, 3, 5)$. Điều này chỉ khả thi đối với $b = (4, 6, c)$ nếu $c =$ ____.

**8** Thông thường 4 "mặt phẳng" trong không gian 4 chiều cắt nhau tại một ____. Thông thường 4 vectơ cột trong không gian 4 chiều có thể kết hợp để tạo ra $\mathbf{b}$. Tổ hợp nào của $(1, 0, 0, 0)$, $(1, 1, 0, 0)$, $(1, 1, 1, 0)$, $(1, 1, 1, 1)$ tạo ra $\mathbf{b} = (3, 3, 3, 2)$? Bạn đang giải 4 phương trình nào cho $x, y, z, t$?

**Các Bài toán 9–14 liên quan đến nhân các ma trận và vectơ.**

**9** Tính mỗi $Ax$ bằng các tích vô hướng của các hàng với vectơ cột:

$$(a) \quad \begin{bmatrix} 1 & 2 & 4 \\ -2 & 3 & 1 \\ -4 & 1 & 2 \end{bmatrix} \begin{bmatrix} 2 \\ 2 \\ 3 \end{bmatrix} \quad (b) \quad \begin{bmatrix} 2 & 1 & 0 & 0 \\ 1 & 2 & 1 & 0 \\ 0 & 1 & 2 & 1 \\ 0 & 0 & 1 & 2 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ 1 \\ 2 \end{bmatrix}$$

**10** Tính mỗi $Ax$ trong Bài toán 9 như một tổ hợp của các cột:

$$9(a) \text{ trở thành } Ax = 2 \begin{bmatrix} 1 \\ -2 \\ -4 \end{bmatrix} + 2 \begin{bmatrix} 2 \\ 3 \\ 1 \end{bmatrix} + 3 \begin{bmatrix} 4 \\ 1 \\ 2 \end{bmatrix} = \begin{bmatrix} 2 \\ 3 \\ 1 \end{bmatrix}.$$

Cần bao nhiêu phép nhân riêng biệt cho $Ax$, khi ma trận là "3 x 3"?

**11** Tìm hai thành phần của $Ax$ theo hàng hoặc theo cột:

$$\begin{bmatrix} 2 & 3 \\ 5 & 1 \end{bmatrix} \begin{bmatrix} 4 \\ 2 \end{bmatrix} \quad \text{và} \quad \begin{bmatrix} 3 & 6 \\ 6 & 12 \end{bmatrix} \begin{bmatrix} 2 \\ -1 \end{bmatrix} \quad \text{và} \quad \begin{bmatrix} 1 & 2 & 4 \\ 2 & 0 & 1 \end{bmatrix} \begin{bmatrix} 3 \\ 1 \\ 1 \end{bmatrix}.$$

**12** Nhân $A$ với $x$ để tìm ba thành phần của $Ax$:

$$\begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} \quad \text{và} \quad \begin{bmatrix} 2 & 1 & 3 \\ 1 & 2 & 3 \\ 3 & 3 & 6 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ -1 \end{bmatrix} \quad \text{và} \quad \begin{bmatrix} 2 & 1 \\ 1 & 2 \\ 3 & 3 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}.$$

**13** (a) Một ma trận có $m$ hàng và $n$ cột nhân với một vectơ có ____ thành phần để tạo ra một vectơ có ____ thành phần.
(b) Các mặt phẳng từ $m$ phương trình $Ax = \mathbf{b}$ nằm trong không gian ____ chiều. Tổ hợp của các cột của $A$ nằm trong không gian ____ chiều.

**14** Viết $2x + 3y + z + 5t = 8$ dưới dạng một ma trận $A$ (có bao nhiêu hàng?) nhân với vectơ cột $\mathbf{x} = (x, y, z, t)$ để tạo ra $\mathbf{b}$. Các nghiệm $\mathbf{x}$ lấp đầy một mặt phẳng hoặc "siêu phẳng" trong không gian 4 chiều. *Mặt phẳng đó là 3 chiều và không có thể tích 4 chiều (4D).*

**Các Bài toán 15–22 hỏi về các ma trận tác động theo những cách đặc biệt lên các vectơ.**

**15** (a) Ma trận đơn vị 2 x 2 là gì? $I$ nhân $\begin{bmatrix} x \\ y \end{bmatrix}$ bằng $\begin{bmatrix} x \\ y \end{bmatrix}$.
(b) Ma trận hoán vị (exchange matrix) 2 x 2 là gì? $P$ nhân $\begin{bmatrix} x \\ y \end{bmatrix}$ bằng $\begin{bmatrix} y \\ x \end{bmatrix}$.

**16** (a) Ma trận 2 x 2 nào $R$ quay mọi vectơ một góc $90^\circ$? $R$ nhân $\begin{bmatrix} x \\ y \end{bmatrix}$ là $\begin{bmatrix} \_ \\ \_ \end{bmatrix}$.
(b) Ma trận 2 x 2 nào $R^2$ quay mọi vectơ một góc $180^\circ$?

**17** Tìm ma trận $P$ khi nhân $(x, y, z)$ cho ra $(y, z, x)$. Tìm ma trận $Q$ khi nhân $(y, z, x)$ để đưa về lại $(x, y, z)$.

**18** Ma trận 2 x 2 $E$ nào trừ thành phần thứ nhất khỏi thành phần thứ hai? Ma trận 3 x 3 nào làm điều tương tự?

| $E \begin{bmatrix} 3 \\ 5 \end{bmatrix} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}$ | và | $E \begin{bmatrix} 3 \\ 5 \\ 7 \end{bmatrix} = \begin{bmatrix} 3 \\ 2 \\ 7 \end{bmatrix}$ |
|---------------------------------------------------------------------------------|----|-------------------------------------------------------------------------------------------|
|---------------------------------------------------------------------------------|----|-------------------------------------------------------------------------------------------|

**19** Ma trận 3 x 3 $E$ nào khi nhân với $(x, y, z)$ tạo ra $(x, y, z + x)$? Ma trận $E^{-1}$ nào khi nhân với $(x, y, z)$ tạo ra $(x, y, z - x)$? Nếu bạn nhân $(3, 4, 5)$ với $E$ và sau đó nhân với $E^{-1}$, hai kết quả là ( ____ ) và ( ____ ).

**20** Ma trận 2 x 2 $P_1$ nào hình chiếu vectơ $(x, y)$ lên trục $x$ để tạo ra $(x, 0)$? Ma trận $P_2$ nào chiếu lên trục $y$ để tạo ra $(0, y)$? Nếu bạn nhân $(5, 7)$ với $P_1$ và sau đó nhân với $P_2$, bạn nhận được ( ____ ) và ( ____ ).

**21** Ma trận 2 x 2 $R$ nào quay mọi vectơ một góc $45^\circ$? Vectơ $(1, 0)$ biến thành $(\sqrt{2}/2, \sqrt{2}/2)$. Vectơ $(0, 1)$ biến thành $(-\sqrt{2}/2, \sqrt{2}/2)$. Những điều đó xác định ma trận. Hãy vẽ những vectơ cụ thể này trong mặt phẳng $xy$ và tìm $R$.

**22** Viết tích vô hướng của $(1, 4, 5)$ và $(x, y, z)$ dưới dạng phép nhân ma trận $Ax$. Ma trận $A$ có một hàng. Các nghiệm của $Ax = 0$ nằm trên một ____ vuông góc với vectơ ____. Các cột của $A$ chỉ nằm trong không gian ____ chiều.

**23** Bằng ký hiệu MATLAB, hãy viết các lệnh định nghĩa ma trận $A$ này và các vectơ cột $x$ và $b$. Lệnh nào sẽ kiểm tra xem liệu $Ax = b$ hay không?

| $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ | $x = \begin{bmatrix} 5 \\ -2 \end{bmatrix}$ | $b = \begin{bmatrix} 1 \\ 7 \end{bmatrix}$ |
|----------------------------------------------------|---------------------------------------------|--------------------------------------------|
|----------------------------------------------------|---------------------------------------------|--------------------------------------------|

**24** Các lệnh MATLAB `A = eye(3)` và `v = [3 : 5]'` tạo ra ma trận đơn vị 3 x 3 và vectơ cột $(3, 4, 5)$. Các kết quả từ `A*v` và `v'*v` là gì? (Không cần dùng máy tính!) Nếu bạn yêu cầu `v'*A`, điều gì sẽ xảy ra?

**25** Nếu bạn nhân ma trận toàn số 1 (all-ones matrix) $4 \times 4$ là `A = ones(4)` và cột `v = ones(4, 1)`, thì `A*v` là gì? (Không cần máy tính.) Nếu bạn nhân `B = eye(4) + ones(4)` với `w = zeros(4, 1) + 2*ones(4, 1)`, thì `B*w` là gì?

**Các câu hỏi 26-28 ôn tập các bức tranh hàng và cột trong các không gian 2, 3 và 4 chiều.**

**26** Vẽ bức tranh hàng và cột cho các phương trình $x - 2y = 0$, $x + y = 6$.

**27** Đối với hai phương trình tuyến tính ba ẩn $x, y, z$, bức tranh hàng sẽ hiển thị (2 hay 3) (đường thẳng hay mặt phẳng) trong không gian (2 hay 3) chiều. Bức tranh cột nằm trong không gian (2 hay 3) chiều. Thông thường các nghiệm nằm trên một ____.

**28** Đối với bốn phương trình tuyến tính hai ẩn $x$ và $y$, bức tranh hàng hiển thị bốn ____. Bức tranh cột nằm trong không gian ____ chiều. Các phương trình không có nghiệm trừ khi vectơ vế phải là một tổ hợp của ____.

**29** Bắt đầu với vectơ $u_0 = (1, 0)$. Nhân lặp đi lặp lại với cùng một "ma trận Markov" $A = \begin{bmatrix} .8 & .3 \\ .2 & .7 \end{bmatrix}$. Ba vectơ tiếp theo là $u_1, u_2, u_3$:

$$u_1 = \begin{bmatrix} .8 & .3 \\ .2 & .7 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} .8 \\ .2 \end{bmatrix} \quad u_2 = Au_1 = \underline{\hspace{1cm}} \quad u_3 = Au_2 = \underline{\hspace{1cm}}.$$

Bạn nhận thấy tính chất nào đối với cả bốn vectơ $u_0, u_1, u_2, u_3$?

# **Các Bài toán Thử thách (Challenge Problems)**

**30** Tiếp tục Bài toán 29 từ $u_0 = (1, 0)$ đến $u_7$, và cả từ $v_0 = (0, 1)$ đến $v_7$. Bạn nhận thấy điều gì về $u_7$ và $v_7$? Đây là hai đoạn mã MATLAB, với vòng lặp `while` và `for`. Chúng vẽ đồ thị từ $u_0$ đến $u_7$ và $v_0$ đến $v_7$. Bạn có thể sử dụng các ngôn ngữ khác:

```matlab
u = [1; 0]; A = [.8 .3; .2 .7]; x = u; k = [0 : 7]; 
while size(x,2) <= 7 
    u = A*u; x = [x u]; 
end 
plot(k, x) 

v = [0; 1]; A = [.8 .3; .2 .7]; x = v; k = [0 : 7]; 
for j = 1 : 7 
    v = A*v; x = [x v]; 
end 
plot(k, x)
```

Các vectơ $u$ và $v$ đang tiến tới một trạng thái ổn định (steady state vectors). Hãy đoán vectơ đó và kiểm tra xem $As = s$. Nếu bạn bắt đầu với $s$, bạn sẽ ở lại với $s$.

**31** Hãy sáng tạo ra một ma trận ma thuật (magic matrix) $3 \times 3$ $M_3$ với các phần tử $1, 2, \dots, 9$. Tất cả các hàng và cột và các đường chéo đều cộng lại bằng 15. Hàng đầu tiên có thể là $8, 3, 4$. $M_3$ nhân với $(1, 1, 1)$ là bao nhiêu? $M_4$ nhân với $(1, 1, 1, 1)$ là bao nhiêu nếu một ma trận ma thuật $4 \times 4$ có các phần tử từ $1, \dots, 16$?

**32** Giả sử $u$ và $v$ là hai cột đầu tiên của một ma trận $3 \times 3$ $A$. Cột thứ ba $w$ nào sẽ làm cho ma trận này suy biến? Hãy mô tả một bức tranh cột điển hình của $Ax = b$ trong trường hợp suy biến đó, và một bức tranh hàng điển hình (đối với một $b$ ngẫu nhiên).

**33 Phép nhân với $A$ là một "phép biến đổi tuyến tính" (linear transformation).** Những từ đó có nghĩa là: Nếu $w$ là một tổ hợp của $u$ và $v$, thì $Aw$ cũng là cùng tổ hợp đó của $Au$ và $Av$. Chính "tính tuyến tính" này $Aw = cAu + dAv$ đã mang lại cho chúng ta cái tên *"đại số tuyến tính".*
Bài toán: Nếu $u = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ và $v = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$ thì $Au$ và $Av$ chính là các cột của $A$. Tổ hợp $w = cu + dv$. Nếu $w = \begin{bmatrix} c \\ d \end{bmatrix}$ thì **$Aw$ liên hệ như thế nào với $Au$ và $Av$?**

**34** Bắt đầu từ bốn phương trình $-x_{i+1} + 2x_i - x_{i-1} = i$ (cho $i = 1, 2, 3, 4$ với $x_0 = x_5 = 0$). Viết những phương trình đó dưới dạng ma trận $Ax = b$. Bạn có thể giải chúng cho $x_1, x_2, x_3, x_4$ không?

**35** Một ma trận Sudoku $9 \times 9$ $S$ có các số $1, \dots, 9$ trong mọi hàng và mọi cột, và trong mọi khối $3 \times 3$. Đối với vectơ toàn số 1 $x = (1, \dots, 1)$, thì $Sx$ bằng bao nhiêu? Một câu hỏi hay hơn là: **Những phép hoán đổi hàng nào sẽ tạo ra một ma trận Sudoku khác?** Đồng thời, những phép hoán đổi các khối hàng nào cho một ma trận Sudoku khác? Mục 2.7 sẽ xem xét tất cả các hoán vị (permutations - sắp xếp lại) có thể có của các hàng. Tôi có thể thấy $6$ thứ tự cho 3 hàng đầu tiên, tất cả đều tạo ra ma trận Sudoku. Đồng thời có $6$ hoán vị của 3 hàng tiếp theo, và của 3 hàng cuối cùng. Và có $6$ hoán vị khối cho các khối hàng?

# **2.2 Ý tưởng Phép Khử (The Idea of Elimination)**

1. Đối với $m = n = 3$, có ba phương trình $Ax = b$ và ba ẩn số $x_1, x_2, x_3$.
2. Hai phương trình đầu tiên là $a_{11}x_1 + \dots = b_1$ và $a_{21}x_1 + \dots = b_2$.
3. Nhân phương trình đầu tiên với $a_{21} / a_{11}$ và trừ đi từ phương trình thứ hai: lúc này $x_1$ **bị khử (is eliminated).**
4. Phần tử ở góc $a_{11}$ là "phần tử xoay (pivot)" đầu tiên và tỷ số $a_{21}/a_{11}$ là "số nhân (multiplier)" đầu tiên.
5. Khử $x_1$ khỏi mọi phương trình còn lại $i$ bằng cách trừ đi $a_{i1}/a_{11}$ lần phương trình đầu tiên.
6. Bây giờ $n - 1$ phương trình cuối cùng chứa $n - 1$ ẩn số $x_2, \dots, x_n$. Lặp lại để khử $x_2$.
7. Phép khử sẽ thất bại nếu số không xuất hiện ở vị trí phần tử xoay. Việc hoán đổi hai phương trình có thể cứu vãn nó.

Chương này giải thích một cách có hệ thống để giải các phương trình tuyến tính. Phương pháp này được gọi là *"khử" (elimination)*, và bạn có thể thấy nó ngay lập tức trong ví dụ $2 \times 2$ của chúng ta. Trước khi khử, cả $x$ và $y$ đều xuất hiện trong hai phương trình. Sau khi khử, ẩn số đầu tiên $x$ đã biến mất khỏi phương trình thứ hai $8y = 8$:

| Trước | $x - 2y = 1$<br>$3x + 2y = 11$ | Sau | $x - 2y = 1$<br>$8y = 8$ | (nhân phương trình 1 với 3)<br>(trừ đi để khử 3x) |
|--------|--------------------------------|-------|--------------------------|----------------------------------------------------------|
| <hr/>  |                                |       |                          |                                                          |

Phương trình mới $8y = 8$ ngay lập tức cho $y = 1$. Thế ngược $y = 1$ trở lại phương trình đầu tiên để lại $x - 2 = 1$. Do đó $x = 3$ và nghiệm $(x, y) = (3, 1)$ đã hoàn tất.

Phép khử tạo ra một hệ *tam giác trên (upper triangular system)* - đây là mục tiêu. Các hệ số khác không $1, -2, 8$ tạo thành một tam giác. Hệ thống đó được giải từ dưới lên trên, đầu tiên là $y = 1$ và sau đó là $x = 3$. Quá trình nhanh chóng này được gọi là *phép thế ngược (back substitution)*. Nó được sử dụng cho các hệ tam giác trên có kích thước bất kỳ, sau khi phép khử tạo ra một hình tam giác.

Điểm quan trọng: Các phương trình ban đầu có cùng một nghiệm $x = 3$ và $y = 1$. Hình 2.5 cho thấy mỗi hệ dưới dạng một cặp đường thẳng, cắt nhau tại điểm nghiệm $(3, 1)$. Sau phép khử, các đường thẳng vẫn gặp nhau tại cùng điểm đó. Mỗi bước đều hoạt động với những phương trình đúng.

*Làm thế nào chúng ta đi được từ cặp đường thẳng đầu tiên đến cặp thứ hai?* Chúng ta đã trừ 3 lần phương trình đầu tiên từ phương trình thứ hai. Bước khử $x$ khỏi phương trình 2 là phép toán nền tảng trong chương này. Chúng ta sử dụng nó thường xuyên đến mức chúng ta sẽ xem xét nó thật kỹ:

*Để khử $x$: Trừ một bội số của phương trình 1 từ phương trình 2.*

Ba lần $x - 2y = 1$ cho $3x - 6y = 3$. Khi điều này được trừ khỏi $3x + 2y = 11$, vế phải trở thành $8$. Điểm mấu chốt là $3x$ triệt tiêu với $3x$. Những gì còn lại ở vế trái là $2y - (-6y)$ hoặc $8y$, và $x$ bị khử. Hệ phương trình trở thành dạng tam giác.

Hãy tự hỏi số nhân $c = 3$ đó được tìm thấy như thế nào. Phương trình đầu tiên chứa $1x$. *Vì vậy, phần tử xoay (pivot) đầu tiên là* **1** (hệ số của $x$). Phương trình thứ hai chứa $3x$, **vì vậy số nhân là 3.** Sau đó phép trừ $3x - 3x$ tạo ra số không và hình tam giác.

Bạn sẽ thấy quy tắc số nhân nếu tôi thay đổi phương trình đầu tiên thành $4x - 8y = 4$. (Vẫn là cùng một đường thẳng nhưng phần tử xoay đầu tiên trở thành 4.) Số nhân đúng bây giờ là $c = 3/4$. *Để tìm số nhân; lấy hệ số "3" cần bị khử chia cho phần tử xoay "4":*

| $4x - 8y = 4$  | **Nhân phương trình 1 với $3/4$** | $4x - 8y = 4$ |
|----------------|--------------------------------------------------------|---------------|
| $3x + 2y = 11$ | **Trừ khỏi phương trình 2**                        | $8y = 8$      |

Hệ phương trình cuối cùng có dạng tam giác và phương trình cuối cùng vẫn cho $y = 1$. Phép thế ngược tạo ra $4x - 8 = 4$ và $4x = 12$ và $x = 3$. Chúng ta đã thay đổi các con số nhưng không làm thay đổi các đường thẳng hay nghiệm. *Chia cho phần tử xoay để tìm số nhân đó* $l = 3/4$:

**Phần tử xoay (Pivot)** = *phần tử khác không đầu tiên trong hàng thực hiện việc khử*
**Số nhân (Multiplier)** = *(phần tử cần khử) chia cho (phần tử xoay)* = $\frac{3}{4}$.

Phương trình thứ hai mới bắt đầu với phần tử xoay thứ hai, là 8. Chúng ta sẽ sử dụng nó để khử $y$ khỏi phương trình thứ ba nếu có. *Để giải $n$ phương trình, chúng ta cần $n$ phần tử xoay. Các phần tử xoay nằm trên đường chéo của tam giác sau khi thực hiện phép khử.*

Bạn có thể tự giải các phương trình đó cho $x$ và $y$ mà không cần đọc cuốn sách này. Đây là một bài toán cực kỳ khiêm tốn, nhưng chúng ta sẽ nán lại với nó lâu hơn một chút. Thậm chí đối với một hệ 2 x 2, phép khử có thể thất bại. Bằng cách thấu hiểu khả năng thất bại (khi chúng ta không thể tìm thấy một tập hợp đầy đủ các phần tử xoay), bạn sẽ hiểu toàn bộ quá trình khử.

![](images/_page_56_Figure_9.jpeg)

Hình 2.5: Khử $x$ làm cho đường thẳng thứ hai trở thành đường ngang. Khi đó $8y = 8$ cho ta $y = 1$.

#### **Sự thất bại của Phép khử (Breakdown of Elimination)**

Thông thường, phép khử tạo ra các phần tử xoay đưa chúng ta đến nghiệm. Nhưng sự thất bại hoàn toàn có thể xảy ra. Tại một thời điểm nào đó, phương pháp này có thể yêu cầu chúng ta *chia cho số 0.* Chúng ta không thể làm điều đó. Quá trình buộc phải dừng lại. Có thể có cách để điều chỉnh và tiếp tục - hoặc sự thất bại có thể là không thể tránh khỏi.

Ví dụ 1 thất bại với *không có nghiệm nào cho $0y = 8$.* Ví dụ 2 thất bại với *quá nhiều nghiệm cho $0y = 0$.* Ví dụ 3 thành công bằng cách hoán đổi các phương trình.

Ví dụ 1 thất bại với *không có nghiệm nào cho $0y = 8$.* Ví dụ 2 thất bại với *quá nhiều nghiệm cho $0y = 0$.* Ví dụ 3 thành công bằng cách hoán đổi các phương trình.

![](images/_page_57_Figure_2.jpeg)

Hình 2.6: Bức tranh hàng và bức tranh cột cho Ví dụ 1: *không có nghiệm.*

**Ví dụ 1** *Thất bại vĩnh viễn với không có nghiệm.* Phép khử làm cho điều này rõ ràng:

| <span></span>  | <span></span>      | <span></span> |
|----------------|--------------------|---------------|
| $x - 2y = 1$   | Trừ đi 3 lần   | $x - 2y = 1$  |
| $3x - 6y = 11$ | phương trình 1 từ phương trình 2 | $0y = 8.$     |

*Không có* nghiệm nào cho $0y = 8$. Thông thường chúng ta chia vế phải 8 cho phần tử xoay thứ hai, nhưng *hệ này không có phần tử xoay thứ hai. (Số không không bao giờ được phép làm phần tử xoay!)* Bức tranh hàng và cột trong Hình 2.6 cho thấy lý do tại sao sự thất bại là không thể tránh khỏi. Nếu không có nghiệm, phép khử sẽ khám phá ra thực tế đó bằng cách đi đến một phương trình như $0y = 8$.

Bức tranh hàng của sự thất bại hiển thị các đường thẳng song song - không bao giờ gặp nhau. Một nghiệm phải nằm trên cả hai đường thẳng. Với không có điểm chung, các phương trình không có nghiệm.

Bức tranh cột hiển thị hai cột $(1, 3)$ và $(-2, -6)$ cùng hướng. *Tất cả các tổ hợp của các cột nằm dọc theo một đường thẳng.* Nhưng cột từ vế phải nằm ở một hướng khác $(1, 11)$. Không có tổ hợp nào của các cột có thể tạo ra vế phải này do đó không có nghiệm.

Khi chúng ta thay đổi vế phải thành $(1, 3)$, sự thất bại xuất hiện như là một toàn bộ đường thẳng chứa các điểm nghiệm. Thay vì không có nghiệm, tiếp theo là Ví dụ 2 với vô số nghiệm.

**Ví dụ 2** *Thất bại với vô số nghiệm. Thay đổi $b = (1, 11)$ thành $(1, 3)$.*

| <span></span> | <span></span>      | <span></span> | <span></span>     |
|---------------|--------------------|---------------|-------------------|
| $x - 2y = 1$  | Trừ đi 3 lần   | $x - 2y = 1$  | Vẫn chỉ có        |
| $3x - 6y = 3$ | phương trình 1 từ phương trình 2 | $0y = 0$ .    | **một phần tử xoay.** |

*Mọi $y$* đều thỏa mãn $0y = 0$. Thực sự chỉ có một phương trình $x - 2y = 1$. Ẩn số $y$ là *"tự do (free)".* Sau khi $y$ được chọn tự do, $x$ được xác định là $x = 1 + 2y$.

Trong bức tranh hàng, các đường thẳng song song đã trở thành cùng một đường thẳng. Mọi điểm trên đường thẳng đó đều thỏa mãn cả hai phương trình. Chúng ta có một đường thẳng toàn các nghiệm trong Hình 2.7.

Trong bức tranh cột, $b = (1, 3)$ bây giờ giống hệt như cột 1. Vì vậy chúng ta có thể chọn $x = 1$ và $y = 0$. Chúng ta cũng có thể chọn $x = 0$ và $y = -1/2$; cột 2 nhân với $-1/2$ bằng $b$. Mọi $(x, y)$ giải được bài toán hàng cũng giải được bài toán cột.

![](images/_page_58_Figure_2.jpeg)

Hình 2.7: Bức tranh hàng và cột cho Ví dụ 2: *vô số nghiệm.*

**Thất bại** Đối với $n$ phương trình, chúng ta không nhận được $n$ phần tử xoay
**Phép khử dẫn đến một phương trình $0 \neq 0$** (không có nghiệm) hoặc **$0 = 0$** (nhiều nghiệm)

#### **Sự thành công đi kèm với $n$ phần tử xoay. Nhưng chúng ta có thể phải hoán đổi $n$ phương trình.**

Phép khử có thể đi sai hướng theo một cách thứ ba - nhưng lần này nó có thể được khắc phục. *Giả sử vị trí phần tử xoay đầu tiên chứa số không.* Chúng ta từ chối việc cho phép số không làm một phần tử xoay. Khi phương trình đầu tiên không có số hạng nào liên quan đến $x$, chúng ta có thể hoán đổi nó với một phương trình bên dưới:

#### **Ví dụ 3** *Thất bại tạm thời (số không ở vị trí phần tử xoay). Một phép hoán đổi hàng tạo ra hai phần tử xoay:*

| **Hoán vị** | $0x + 2y = 4$ | Hoán đổi hai  | $3x - 2y = 5$ |
|--------------------|---------------|---------------|---------------|
|                    | $3x - 2y = 5$ | phương trình | $2y = 4.$     |

Hệ mới đã có dạng tam giác. Ví dụ nhỏ này đã sẵn sàng cho phép thế ngược. Phương trình cuối cùng cho $y = 2$, và sau đó phương trình đầu tiên cho $x = 3$. Bức tranh hàng là bình thường (hai đường thẳng cắt nhau). Bức tranh cột cũng bình thường (các vectơ cột không cùng hướng). Các phần tử xoay 3 và 2 là bình thường - nhưng một *phép hoán đổi hàng* đã được yêu cầu.

Ví dụ 1 và 2 là *suy biến (singular)* - không có phần tử xoay thứ hai. Ví dụ 3 là *không suy biến (nonsingular)* có một tập hợp đầy đủ các phần tử xoay và có chính xác một nghiệm. Các phương trình suy biến không có nghiệm hoặc có vô số nghiệm. Các phần tử xoay phải khác không vì chúng ta phải chia cho chúng.

### **Ba phương trình ba ẩn số**

Để hiểu phép khử Gauss, bạn phải vượt ra ngoài các hệ $2 \times 2$. Ba nhân ba là đủ để thấy quy luật. Hiện tại các ma trận là hình vuông - có số lượng hàng và cột bằng nhau. Đây là một hệ $3 \times 3$, được cấu trúc đặc biệt để tất cả các bước khử dẫn đến số nguyên mà không phải phân số:

$$\begin{aligned} 2x + 4y - 2z &= 2 \\ 4x + 9y - 3z &= 8 \\ -2x - 3y + 7z &= 10 \end{aligned} \tag{1}$$

Các bước là gì? Phần tử xoay đầu tiên là phần tử in đậm **2** (phía trên bên trái). Dưới phần tử xoay đó chúng ta muốn khử số **4**. *Số nhân đầu tiên là tỷ số $4/2 = 2$.* Nhân phương trình phần tử xoay với $l_{21} = 2$ và trừ. Phép trừ loại bỏ $4x$ khỏi phương trình thứ hai:

**Bước 1** Trừ 2 lần phương trình 1 khỏi phương trình 2. Điều này để lại $y + z = 4$.

Chúng ta cũng khử $-2x$ khỏi phương trình 3 - vẫn sử dụng phần tử xoay đầu tiên. Cách nhanh chóng là cộng phương trình 1 vào phương trình 3. Sau đó $2x$ triệt tiêu $-2x$. Chúng ta làm chính xác điều đó, nhưng quy tắc trong cuốn sách này là *trừ thay vì cộng*. Quy luật hệ thống có số nhân $l_{31} = -2/2 = -1$. Trừ đi $-1$ lần một phương trình cũng giống như phép cộng:

**Bước 2** Trừ $-1$ lần phương trình 1 khỏi phương trình 3. Điều này để lại $y + 5z = 12$.

Hai phương trình mới chỉ liên quan đến $y$ và $z$. Phần tử xoay thứ hai (in đậm) là 1:

$$\begin{array}{ll} x \text{ đã bị khử} & 1y + 1z = 4 \\ & 1y + 5z = 12 \end{array}$$

Chúng ta đã đạt đến một hệ $2 \times 2$. Bước cuối cùng khử $y$ để biến nó thành $1 \times 1$:

**Bước 3** Trừ phương trình $2_{\text{mới}}$ khỏi $3_{\text{mới}}$. Số nhân là $1/1 = 1$. Sau đó $4z = 8$.

Hệ $Ax = b$ ban đầu đã được biến đổi thành một hệ tam giác trên $Ux = c$:

![]()

Mục tiêu đã đạt được - phép khử xuôi đã hoàn tất từ $A$ đến $U$. **Chú ý các phần tử xoay 2, 1, 4 dọc theo đường chéo của $U$.** Các phần tử xoay 1 và 4 đã bị ẩn trong hệ ban đầu. Phép khử đã đưa chúng ra ngoài. $Ux = c$ đã sẵn sàng cho **phép thế ngược**, diễn ra một cách nhanh chóng:

$$(4z = 8 \text{ cho } z = 2) \quad (y + z = 4 \text{ cho } y = 2) \quad (\text{phương trình 1 cho } x = -1)$$

*Nghiệm là $(x, y, z) = (-1, 2, 2)$.* Bức tranh hàng có ba mặt phẳng từ ba phương trình. Tất cả các mặt phẳng đi qua nghiệm này. Các mặt phẳng ban đầu bị nghiêng, nhưng mặt phẳng cuối cùng $4z = 8$ sau khi khử là mặt phẳng ngang.

Bức tranh cột cho thấy một tổ hợp $Ax$ của các vectơ cột tạo ra vế phải $b$. Các hệ số trong tổ hợp đó là $-1, 2, 2$ (nghiệm):

$$Ax = (-1) \begin{bmatrix} 2 \\ 4 \\ -2 \end{bmatrix} + 2 \begin{bmatrix} 4 \\ 9 \\ -3 \end{bmatrix} + 2 \begin{bmatrix} -2 \\ -3 \\ 7 \end{bmatrix} \text{ bằng } \begin{bmatrix} 2 \\ 8 \\ 10 \end{bmatrix} = b. \tag{3}$$

Các số $x, y, z$ nhân các cột 1, 2, 3 trong $Ax = b$ và cũng trong hệ tam giác $Ux = c$.

#### **Phép khử từ $A$ đến $U$**

Đối với một bài toán $4 \times 4$, hoặc một bài toán $n \times n$, phép khử tiến hành theo cùng một cách. Đây là toàn bộ ý tưởng, cột qua cột từ $A$ đến $U$, khi phép khử Gauss thành công.

**Cột 1.** *Sử dụng phương trình đầu tiên để tạo ra các số không bên dưới phần tử xoay đầu tiên.*

**Cột 2.** *Sử dụng phương trình* **2** *mới để tạo ra các số không bên dưới phần tử xoay thứ hai.*

**Cột 3 đến $n$.** *Tiếp tục đi để tìm tất cả $n$ phần tử xoay và ma trận tam giác trên $U$.*

| Sau cột 2 chúng ta có | $\begin{bmatrix} x & x & x & x \\ 0 & x & x & x \\ 0 & 0 & x & x \\ 0 & 0 & x & x \end{bmatrix}$ | Chúng ta muốn | $\begin{bmatrix} x & x & x & x \\ & x & & \\ & & x & x \\ & & & x \end{bmatrix}$ | (4) |
|------------------------|--------------------------------------------------------------------------------------------------|---------|----------------------------------------------------------------------------------|-----|
|------------------------|--------------------------------------------------------------------------------------------------|---------|----------------------------------------------------------------------------------|-----|

Kết quả của phép khử xuôi là một hệ tam giác trên. Nó không suy biến nếu có một tập hợp đầy đủ $n$ phần tử xoay (không bao giờ bằng không!). *Câu hỏi:* $x$ nào ở bên trái sẽ không bị thay đổi trong quá trình khử vì phần tử xoay đã được biết? Đây là một ví dụ cuối cùng để cho thấy hệ $Ax = b$ ban đầu, hệ tam giác $U x = c$, và nghiệm $(x, y, z)$ từ phép thế ngược:

| <span></span>      | <span></span>   | <span></span>   | <span></span>   | <span></span>   |
|--------------------|-----------------|-----------------|-----------------|-----------------|
| $x + y + z = 6$    | $x + y + z = 6$ | $x + y + z = 6$ | $x + y + z = 6$ | $x + y + z = 6$ |
| $x + 2y + 2z = 9$  | Phép khử xuôi         | $y + z = 3$     | $y + z = 3$     | Phép thế ngược          |
| $x + 2y + 3z = 10$ | Phép khử xuôi         | $z = 1$         | $z = 1$         |                 |

Tất cả các số nhân là 1. Tất cả các phần tử xoay là 1. Tất cả các mặt phẳng gặp nhau tại nghiệm $(3, 2, 1)$. Các cột của $A$ kết hợp với 3, 2, 1 để tạo ra $b = (6, 9, 10)$. Tam giác cho thấy $Ux = c = (6, 3, 1)$.

#### **• ÔN TẬP CÁC Ý TƯỞNG CHÍNH •**

- **1.** Một hệ tuyến tính $(Ax = b)$ trở thành **tam giác trên (upper triangular)** $(Ux = c)$ sau phép khử.
- **2.** Chúng ta **trừ đi** $l_{ij}$ lần phương trình $j$ từ phương trình $i$, để làm cho phần tử $(i, j)$ bằng không.
- **3.** **Số nhân (multiplier)** là $l_{ij} = \text{phần tử cần khử ở hàng } i / \text{phần tử xoay ở hàng } j$. **Các phần tử xoay** không thể bằng không!
- **4.** Khi số không nằm ở vị trí phần tử xoay, **hoán đổi các hàng** nếu có một số khác không bên dưới nó.
- **5.** Hệ tam giác trên $Ux = c$ được giải bằng **phép thế ngược (back substitution)** (bắt đầu từ dưới cùng).
- **6.** Khi **sự thất bại (breakdown)** là vĩnh viễn, $Ax = b$ không có nghiệm hoặc có vô số nghiệm.

#### **• CÁC VÍ DỤ ĐÃ GIẢI •**

**2.2 A** Khi phép khử được áp dụng cho ma trận $A$ này, phần tử xoay thứ nhất và thứ hai là gì? Số nhân $l_{21}$ trong bước đầu tiên ($l_{21}$ nhân hàng 1 *bị trừ* khỏi hàng 2) là gì?

| $A = \begin{bmatrix} 1 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{bmatrix} \longrightarrow \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 1 & 2 \end{bmatrix} \longrightarrow \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix} = U.$ |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Phần tử nào ở vị trí 2, 2 (thay vì 2) sẽ buộc phải hoán đổi các hàng 2 và 3? Tại sao số nhân ở phía dưới bên trái $l_{31} = 0$, trừ đi không lần hàng 1 khỏi hàng 3? *Nếu bạn thay đổi phần tử ở góc từ $a_{33} = 2$ thành $a_{33} = 1$, tại sao phép khử lại thất bại?*

**Lời giải** Phần tử xoay đầu tiên là 1. Số nhân $l_{21}$ là $1 / 1 = 1$. Khi 1 lần hàng 1 bị trừ khỏi hàng 2, phần tử xoay thứ hai hiện ra là một số 1 khác. Nếu phần tử ở giữa ban đầu là 1 thay vì 2, điều đó sẽ buộc phải thực hiện một phép hoán đổi hàng.

Số nhân $l_{31}$ bằng không vì $a_{31} = 0$. Một số không ở đầu một hàng không cần đến phép khử. $A$ này là một *"ma trận dải (band matrix)".* Mọi thứ đều duy trì là số không bên ngoài dải.

Phần tử xoay cuối cùng cũng là 1. Do đó, nếu phần tử góc ban đầu $a_{33} = 2$ giảm đi 1, phép khử sẽ tạo ra 0. **Không có phần tử xoay thứ ba, phép khử thất bại.**

**2.2 B** Giả sử $A$ đã là một *ma trận tam giác* (tam giác trên hoặc tam giác dưới). *Bạn thấy các phần tử xoay của nó ở đâu?* Khi nào thì $Ax = b$ có đúng một nghiệm cho mọi $b$?

**Lời giải** Các phần tử xoay của một ma trận tam giác đã được thiết lập sẵn dọc theo đường chéo chính. *Phép khử thành công khi tất cả những con số đó khác không.* Sử dụng phép thế *ngược* khi $A$ là tam giác trên, đi *xuôi* khi $A$ là tam giác dưới.

**2.2 C** Sử dụng phép khử để đạt tới các ma trận tam giác trên $U$. Giải bằng phép thế ngược hoặc giải thích tại sao điều này là không thể. Các phần tử xoay là gì (không bao giờ bằng không)? Hoán đổi các phương trình khi cần thiết. Sự khác biệt duy nhất là $-x$ trong phương trình cuối cùng.

| **Thành công** | $x + y + z = 7$ | **Thất bại** | $x + y + z = 7$  |
|----------------|-----------------|----------------|------------------|
|                | $x + y - z = 5$ |                | $x + y - z = 5$  |
|                | $x - y + z = 3$ |                | $-x - y + z = 3$ |

**Lời giải** Đối với hệ thứ nhất, trừ phương trình 1 khỏi các phương trình 2 và 3 (các số nhân là $l_{21} = 1$ và $l_{31} = 1$). Phần tử 2, 2 trở thành không, do đó hãy hoán đổi phương trình 2 và 3:

| **Thành công** | $x + y + z = 7$ |                |  | $x + y + z = 7$ |  |
|----------------|-----------------|----------------|--|-----------------|--|
|                | $0y - 2z = -2$  | hoán đổi thành |  | $-2y + 0z = -4$ |  |
|                | $-2y + 0z = -4$ |                |  | $-2z = -2$      |  |

Sau đó phép thế ngược cho $z = 1$ và $y = 2$ và $x = 4$. Các phần tử xoay là $1, -2, -2$.

Đối với hệ thứ hai, trừ phương trình 1 khỏi phương trình 2 như trước. Cộng phương trình 1 vào phương trình 3. Điều này để lại số không ở vị trí 2, 2 *và cũng ở bên dưới nó:*

| Thất bại | $x + y + z = 7$ | Có **không phần tử xoay ở cột 2** (nó là - cột 1)    |  |
|---------|-----------------|-------------------------------------------------------------|--|
|         | $0y - 2z = -2$  | Một bước khử nữa cho ta **$0z = 8$** |  |
|         | $0y + 2z = 10$  | Ba mặt phẳng **không gặp nhau**                          |  |

Mặt phẳng 1 cắt mặt phẳng 2 theo một đường thẳng. Mặt phẳng 1 cắt mặt phẳng 3 theo một đường thẳng song song. *Không có nghiệm.*

Nếu chúng ta thay đổi "3" trong phương trình thứ ba ban đầu thành "-5" thì phép khử sẽ dẫn đến $0 = 0$. Có vô số nghiệm! *Ba mặt phẳng bây giờ cắt nhau dọc theo toàn bộ một đường thẳng.*

Việc thay đổi 3 thành -5 đã di chuyển mặt phẳng thứ ba đến gặp hai mặt phẳng còn lại. Phương trình thứ hai cho $z = 1$. Sau đó, phương trình đầu tiên để lại $x + y = 6$. **Không có phần tử xoay trong cột 2 làm cho $y$ tự do (free)** (các biến tự do có thể nhận bất kỳ giá trị nào). Khi đó $x = 6 - y$.

## **Bài tập 2.2 (Problem Set 2.2)**

**Các bài toán 1-10 liên quan đến phép khử trên các hệ $2 \times 2$.**

**1** Bội số $l_{21}$ nào của phương trình 1 nên được trừ khỏi phương trình 2?

$$\begin{aligned} 2x + 3y &= 1 \\ 10x + 9y &= 11. \end{aligned}$$

Sau khi khử, hãy viết xuống hệ tam giác trên và khoanh tròn hai phần tử xoay. Các số 1 và 11 không ảnh hưởng đến các phần tử xoay - hãy sử dụng chúng bây giờ trong phép thế ngược.

**2** Giải hệ tam giác của Bài toán 1 bằng phép thế ngược, $y$ trước $x$. Xác minh rằng $x$ lần $(2, 10)$ cộng $y$ lần $(3, 9)$ bằng $(1, 11)$. Nếu vế phải thay đổi thành $(4, 44)$, nghiệm mới là gì?

**3** Bội số nào của phương trình 1 nên được *trừ* khỏi phương trình 2?

$$\begin{aligned} 2x - 4y &= 6 \\ -x + 5y &= 0. \end{aligned}$$

Sau bước khử này, hãy giải hệ tam giác. Nếu vế phải thay đổi thành $(-6, 0)$, nghiệm mới là gì?

**4** Bội số $l$ nào của phương trình 1 nên được trừ khỏi phương trình 2 để loại bỏ $c$?

$$\begin{aligned} ax + by &= f \\ cx + dy &= g. \end{aligned}$$

Phần tử xoay đầu tiên là $a$ (giả sử khác không). Phép khử tạo ra công thức nào cho phần tử xoay thứ hai? $y$ bằng bao nhiêu? Phần tử xoay thứ hai bị thiếu khi $ad = bc$: suy biến (singular).

**5** Chọn một vế phải không cho nghiệm nào và một vế phải khác cho vô số nghiệm. Hai trong số những nghiệm đó là gì?

| **Hệ suy biến** |  | $3x + 2y = 10$ |  |  |  |
|------------------------|--|----------------|--|--|--|
|                        |  | $6x + 4y =$    |  |  |  |

**6** Chọn một hệ số $b$ làm cho hệ này suy biến. Sau đó chọn một vế phải $g$ làm cho nó có thể giải được. Tìm hai nghiệm trong trường hợp suy biến đó.

$$\begin{aligned} 2x + by &= 16 \\ 4x + 8y &= g. \end{aligned}$$

**7** Đối với những số $a$ nào thì phép khử thất bại (1) vĩnh viễn (2) tạm thời?

$$ax + 3y = -3$$
$$4x + 6y = 6$$

Giải tìm $x$ và $y$ sau khi khắc phục sự thất bại tạm thời bằng một phép hoán đổi hàng.

**8** Đối với ba số $k$ nào thì phép khử bị thất bại? Trường hợp nào được khắc phục bằng một phép hoán đổi hàng? Trong mỗi trường hợp, số nghiệm là $0$ hay $1$ hay $\infty$?

$$kx + 3y = 6$$
$$3x + ky = -6$$

**9** Kiểm tra nào đối với $b_1$ và $b_2$ quyết định xem hai phương trình này có cho phép một nghiệm hay không? Chúng sẽ có bao nhiêu nghiệm? Vẽ bức tranh cột cho $b = (1, 2)$ và $(1, 0)$.

$$\begin{aligned} 3x - 2y &= b_1 \\ 6x - 4y &= b_2. \end{aligned}$$

**10** Trong mặt phẳng $xy$, hãy vẽ các đường thẳng $x + y = 5$ và $x + 2y = 6$ và phương trình $y = \_\_$ xuất phát từ phép khử. Đường thẳng $5x - 4y = c$ sẽ đi qua nghiệm của các phương trình này nếu $c = \_\_$.

#### **Các bài toán 11-20 nghiên cứu phép khử trên các hệ $3 \times 3$ (và sự thất bại có thể xảy ra).**

**11** (Được đề xuất) Một hệ phương trình tuyến tính không thể có chính xác hai nghiệm. *Tại sao?*
- (a) Nếu $(x, y, z)$ và $(X, Y, Z)$ là hai nghiệm, thì một nghiệm khác là gì?
- (b) Nếu 25 mặt phẳng cắt nhau tại hai điểm, chúng cắt nhau ở đâu nữa?

**12** Rút gọn hệ này về dạng tam giác trên bằng hai phép toán hàng:

- $2x + 3y + z = 8$
- $4x + 7y + 5z = 20$
- $-2y + 2z = 0$.

Khoanh tròn các phần tử xoay. Giải bằng phép thế ngược cho $z, y, x$.

**13** Áp dụng phép khử (khoanh tròn các phần tử xoay) và phép thế ngược để giải:

$$2x - 3y = 3$$
$$4x - 5y + z = 7$$
$$2x - y - 3z = 5.$$

Liệt kê ba phép toán hàng: Trừ \_\_ lần hàng \_\_ khỏi hàng \_\_.

**14** Số $d$ nào buộc phải hoán đổi hàng, và hệ tam giác (không suy biến) đối với $d$ đó là gì? $d$ nào làm cho hệ này suy biến (không có phần tử xoay thứ ba)?

$$\begin{aligned} 2x + 5y + z &= 0 \\ 4x + dy + z &= 2 \\ y - z &= 3. \end{aligned}$$

**15** Số $b$ nào dẫn đến một phép hoán đổi hàng sau đó? $b$ nào dẫn đến thiếu một phần tử xoay? Trong trường hợp suy biến đó, hãy tìm một nghiệm $x, y, z$ khác không.

- $x + by = 0$
- $x - 2y - z = 0$
- $y + z = 0.$

**16** (a) Xây dựng một hệ $3 \times 3$ cần hai phép hoán đổi hàng để đạt được dạng tam giác và một nghiệm.
(b) Xây dựng một hệ $3 \times 3$ cần một phép hoán đổi hàng để tiếp tục, nhưng sau đó lại bị thất bại.

**17** Nếu các hàng 1 và 2 giống nhau, bạn có thể tiến hành phép khử đến đâu (cho phép hoán đổi hàng)? Nếu các cột 1 và 2 giống nhau, phần tử xoay nào bị thiếu?

| **Các hàng bằng nhau** | $2x - y + z = 0$ | $2x + 2y + z = 0$ | **Các cột bằng nhau** |  |  |
|-------------------|------------------|-------------------|----------------------|--|--|
|                   | $2x - y + z = 0$ | $4x + 4y + z = 0$ |                      |  |  |
|                   | $4x + y + z = 2$ | $6x + 6y + z = 2$ |                      |  |  |

**18** Xây dựng một ví dụ $3 \times 3$ có 9 hệ số khác nhau ở vế trái, nhưng các hàng 2 và 3 trở thành số không trong phép khử. Có bao nhiêu nghiệm cho hệ của bạn với $b = (1, 10, 100)$ và bao nhiêu nghiệm với $b = (0, 0, 0)$?

**19** Số $q$ nào làm cho hệ này suy biến và vế phải $t$ nào cho nó vô số nghiệm? Tìm nghiệm có $z = 1$.

- $x + 4y - 2z = 1$
- $x + 7y - 6z = 6$
- $3y + qz = t.$

**20** Ba mặt phẳng có thể không có điểm giao nhau, ngay cả khi không có các mặt phẳng nào song song. Hệ này suy biến nếu hàng 3 của $A$ là một \_\_ của hai hàng đầu tiên. Tìm một phương trình thứ ba không thể giải cùng với $x + y + z = 0$ và $x - 2y - z = 1$.

**21** Tìm các phần tử xoay và nghiệm cho cả hai hệ ($Ax = b$ và $Kx = b$):

| $2x + y = 0$     | $2x - y = 0$      |
|------------------|-------------------|
| $x + 2y + z = 0$ | $-x + 2y - z = 0$ |
| $y + 2z + t = 0$ | $-y + 2z - t = 0$ |
| $z + 2t = 5$     | $-z + 2t = 5$     |

**22** Nếu bạn mở rộng Bài toán 21 theo mẫu $1, 2, 1$ hoặc mẫu $-1, 2, -1$, phần tử xoay thứ năm là gì? Phần tử xoay thứ $n$ là gì? $K$ là ma trận yêu thích của tôi.

**23** Nếu phép khử dẫn đến $x + y = 1$ và $2y = 3$, hãy tìm ba bài toán ban đầu có thể có.

**24** Với hai số $a$ nào thì phép khử sẽ thất bại trên $A = \begin{bmatrix} a & 2 \\ a & a \end{bmatrix}$?

**25** Đối với ba số $a$ nào phép khử sẽ thất bại trong việc đưa ra ba phần tử xoay?

| $A = \begin{bmatrix} a & 2 & 3 \\ a & a & 4 \\ a & a & a \end{bmatrix}$ bị suy biến (singular) với ba giá trị của $a$. |
|---------------------------------------------------------------------------------------------------------------|
|---------------------------------------------------------------------------------------------------------------|

**26** Tìm kiếm một ma trận có tổng các hàng là 4 và 8, và tổng các cột là 2 và $s$:

| Ma trận = $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$ | $a+b=4$ | $a+c=2$ |

|---------------------------------------------------------|---------|---------|
|                                                         | $c+d=8$ | $b+d=s$ |

Bốn phương trình chỉ có thể giải được nếu $s = \_\_$. Khi đó hãy tìm hai ma trận khác nhau có tổng các hàng và cột đúng. *Điểm cộng (Extra credit):* Viết ra hệ $4 \times 4$ $Ax = b$ với $x = (a, b, c, d)$ và biến $A$ thành ma trận tam giác bằng phép khử.

**27** Phép khử theo thứ tự thông thường cho ra ma trận $U$ nào và nghiệm nào cho hệ "tam giác dưới (lower triangular)" này? Chúng ta thực sự đang giải bằng *phép thế xuôi (forward substitution):*

| $3x$              | $=$ 3 |
|-------------------|-------|
| $6x + 2y$         | $=$ 8 |
| $9x - 2y + z = 9$ |       |

**28** Tạo một lệnh MATLAB `A(2, :) = ...` cho hàng 2 mới, để trừ 3 lần hàng 1 khỏi hàng 2 hiện tại nếu ma trận $A$ đã được biết.

## **Các Bài toán Thử thách (Challenge Problems)**

**29** Tìm thử nghiệm các kích thước của phần tử xoay thứ nhất, thứ hai và thứ ba trung bình từ lệnh `[L, U] = lu(rand(3))` của MATLAB. Kích thước trung bình `abs(U(1, 1))` lớn hơn $1/2$ bởi vì `lu` chọn phần tử xoay có sẵn lớn nhất trong cột 1. Ở đây $A = \text{rand}(3)$ có các phần tử ngẫu nhiên giữa $0$ và $1$.

**30** Nếu phần tử góc cuối cùng là $A(5, 5) = 11$ và phần tử xoay cuối cùng của $A$ là $U(5, 5) = 4$, phần tử khác biệt $A(5, 5)$ nào sẽ làm cho $A$ bị suy biến?

**31** Giả sử phép khử biến $A$ thành $U$ mà không cần hoán đổi hàng. Khi đó hàng $j$ của $U$ là tổ hợp của những hàng nào của $A$? Nếu $Ax = 0$, liệu $Ux = 0$ không? Nếu $Ax = b$, liệu $Ux = b$ không? Nếu $A$ bắt đầu là tam giác dưới, ma trận tam giác trên $U$ là gì?

**32** Bắt đầu với 100 phương trình $Ax = 0$ cho 100 ẩn số $x = (x_1, \dots, x_{100})$. Giả sử phép khử rút gọn phương trình thứ 100 thành $0 = 0$, vì vậy hệ bị "suy biến".
  - (a) Phép khử lấy các tổ hợp tuyến tính của các hàng. Vậy hệ suy biến này có tính chất suy biến là: Một số tổ hợp tuyến tính của 100 hàng là \_\_.
  - (b) Các hệ suy biến $Ax = 0$ có vô số nghiệm. Điều này có nghĩa là một số tổ hợp tuyến tính của 100 *cột* là \_\_.
  - (c) Hãy sáng tạo ra một ma trận suy biến $100 \times 100$ không có phần tử không (zero entries).
  - (d) Đối với ma trận của bạn, hãy mô tả bằng lời bức tranh hàng và bức tranh cột của $Ax = 0$. Không cần thiết phải vẽ không gian 100 chiều.

# **2.3 Phép Khử Sử Dụng Các Ma Trận (Elimination Using Matrices)**

**1** Bước đầu tiên nhân các phương trình $Ax = b$ với một ma trận $E_{21}$ để tạo ra $E_{21}Ax = E_{21}b$.
**2** Ma trận $E_{21}A$ đó có một số không ở hàng 2, cột 1 bởi vì $x_1$ bị khử khỏi phương trình 2.
**3** $E_{21}$ là **ma trận đơn vị** (đường chéo của các số 1) trừ đi số nhân $a_{21}/a_{11}$ ở hàng 2, cột 1.
**4** Phép nhân ma trận-ma trận là $n$ phép nhân ma trận-vectơ: $EA = [E\mathbf{a}_1 \dots E\mathbf{a}_n]$.
**5** Chúng ta cũng phải nhân $Eb$! Vì vậy $E$ đang nhân với **ma trận bổ sung (augmented matrix)** $[A \quad b] = [\mathbf{a}_1 \dots \mathbf{a}_n \quad \mathbf{b}]$.
**6** Phép khử nhân $Ax = b$ với $E_{21}, E_{31}, \dots, E_{n1}$, sau đó $E_{32}, E_{42}, \dots, E_{n2}$, và tiếp tục.
**7** **Ma trận hoán đổi hàng (row exchange matrix)** không phải là $E_{ij}$ mà là $P_{ij}$. Để tìm $P_{ij}$, hoán đổi các hàng $i$ và $j$ của $I$.

Phần này đưa ra những ví dụ đầu tiên của chúng ta về **phép nhân ma trận.** Đương nhiên chúng ta bắt đầu với các ma trận chứa nhiều số không. Mục tiêu của chúng ta là xem xét rằng các ma trận *làm điều gì đó. E* tác động lên một vectơ $b$ hoặc một ma trận $A$ để tạo ra một vectơ mới $Eb$ hoặc một ma trận mới $EA$.

Những ví dụ đầu tiên của chúng ta sẽ là các **"ma trận khử (elimination matrices)."** Chúng thực thi các bước khử. Nhân phương trình thứ $j$ với $l_{ij}$ và trừ đi từ phương trình thứ $i$. (Điều này khử $x_j$ khỏi phương trình $i$.) Chúng ta cần rất nhiều các ma trận $E_{ij}$ đơn giản này, một ma trận cho mỗi phần tử khác không cần bị khử bên dưới đường chéo chính.

May mắn thay, chúng ta sẽ không thấy tất cả các ma trận $E_{ij}$ này trong các chương sau. Chúng là những ví dụ tốt để bắt đầu, nhưng có quá nhiều. Chúng có thể kết hợp thành một ma trận tổng thể $E$ thực hiện tất cả các bước cùng một lúc. Cách gọn gàng nhất là kết hợp tất cả các nghịch đảo của chúng $(E_{ij})^{-1}$ thành một ma trận tổng thể $L = E^{-1}$. Đây là mục đích của các trang tiếp theo.

- 1. Để xem mỗi bước là một phép nhân ma trận như thế nào.
- 2. Để tập hợp tất cả những bước $E_{ij}$ đó vào một ma trận khử $E$.
- 3. Để xem mỗi $E_{ij}$ bị nghịch đảo bởi ma trận nghịch đảo $E_{ij}^{-1}$ của nó như thế nào.
- 4. Để tập hợp tất cả những nghịch đảo $E_{ij}^{-1}$ đó (theo đúng thứ tự) vào $L$.

Tính chất đặc biệt của $L$ là tất cả các số nhân $l_{ij}$ đều nằm đúng vị trí. Những con số đó bị trộn lẫn lộn trong $E$ (phép khử xuôi từ $A$ đến $U$). Chúng nằm hoàn hảo trong $L$ (hoàn tác phép khử, trở lại từ $U$ về $A$). Phép nghịch đảo đặt các bước và các ma trận $E_{ij}^{-1}$ của chúng theo thứ tự ngược lại và điều đó ngăn chặn sự trộn lẫn.

Phần này tìm các ma trận $E_{ij}$. Mục 2.4 trình bày bốn cách để nhân các ma trận. Mục 2.5 nghịch đảo từng bước. (Đối với các ma trận khử, chúng ta đã có thể thấy $E_{ij}^{-1}$ ở đây.) Sau đó những nghịch đảo đó đi vào $L$.

#### **Nhân Ma Trận với Vectơ và $Ax = b$**

Ví dụ $3 \times 3$ trong phần trước có dạng ngắn gọn $Ax = b$:

| $2x_1 + 4x_2 - 2x_3 = 2$   | giống như | $\begin{bmatrix} 2 & 4 & -2 \\ 4 & 9 & -3 \\ -2 & -3 & 7 \end{bmatrix}$ | $\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 2 \\ 8 \\ 10 \end{bmatrix}$ |
|----------------------------|----------------|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| $2x_1 + 9x_2 - 3x_3 = 8$   |                |                                                                         |                                                                                                |
| $-2x_1 - 3x_2 + 7x_3 = 10$ |                |                                                                         |                                                                                                |

Chín con số ở bên trái đi vào ma trận $A$. Ma trận đó không chỉ nằm cạnh $x$. *$A$ nhân với $x$.* Quy tắc cho *$A$ nhân $x$* được chọn một cách chính xác để sinh ra ba phương trình.

*Ôn tập về $A$ nhân $x$.* Một ma trận nhân với một vectơ cho ra một vectơ. Ma trận là vuông khi số phương trình (ba) khớp với số ẩn số (ba). Ma trận của chúng ta là $3 \times 3$. Một ma trận vuông tổng quát là $n \times n$. Khi đó vectơ $x$ nằm trong không gian $n$ chiều, ẩn số là $\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$ và nghiệm là $\mathbf{x} = \begin{bmatrix} -1 \\ 2 \\ 2 \end{bmatrix}$.

Điểm mấu chốt: $Ax = b$ đại diện cho dạng hàng và cả dạng cột của các phương trình.

| Dạng cột | $Ax = (-1) \begin{bmatrix} 2 \\ 4 \\ -2 \end{bmatrix} + 2 \begin{bmatrix} 4 \\ 9 \\ -3 \end{bmatrix} + 2 \begin{bmatrix} -2 \\ -3 \\ 7 \end{bmatrix} = \begin{bmatrix} 2 \\ 8 \\ 10 \end{bmatrix} = b.$ |  |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
|             |                                                                                                                                                                                                         |  |

*$Ax$ là một tổ hợp của các cột của $A$.* Để tính từng thành phần của $Ax$, chúng ta sử dụng **dạng hàng** của phép nhân ma trận. *Các thành phần của $Ax$ là các tích vô hướng với các hàng của $A$.* Công thức ngắn gọn cho tích vô hướng đó với $x$ sử dụng "ký hiệu sigma".

Thành phần đầu tiên của $Ax$ ở trên là $(-1)(2) + (2)(4) + (2)(-2)$.

Thành phần thứ $i$ của $Ax$ là $(\text{hàng } i) \cdot \mathbf{x} = a_{i1}x_1 + a_{i2}x_2 + \dots + a_{in}x_n.$

Điều này đôi khi được viết với ký hiệu sigma là $\sum_{j=1}^n a_{ij}x_j$.

$\sum$ là một chỉ thị để cộng. Bắt đầu với $j = 1$ và dừng lại với $j = n$. Tổng bắt đầu với $a_{i1}x_1$ và kết thúc bằng $a_{in}x_n$. Điều đó tạo ra tích vô hướng $(\text{hàng } i) \cdot x$.

Một điểm cần lặp lại về ký hiệu ma trận: Phần tử ở hàng 1, cột 1 (góc trên cùng bên trái) là $a_{11}$. Phần tử ở hàng 1, cột 3 là $a_{13}$. Phần tử ở hàng 3, cột 1 là $a_{31}$. (Số hàng đứng trước số cột.) Từ "phần tử (entry)" đối với ma trận tương ứng với "thành phần (component)" đối với vectơ. Quy tắc chung: $a_{ij} = A(i, j)$ *nằm ở hàng $i$, cột $j$.*

**Ví dụ 1** Ma trận này có $a_{ij} = 2i + j$. Khi đó $a_{11} = 3$. Cũng có $a_{12} = 4$ và $a_{21} = 5$. Đây là $Ax$ theo hàng với các con số và chữ cái:

| $\begin{bmatrix} 3 & 4 \\ 5 & 6 \end{bmatrix} \begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 3 \cdot 2 + 4 \cdot 1 \\ 5 \cdot 2 + 6 \cdot 1 \end{bmatrix}$ | $\begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} a_{11}x_1 + a_{12}x_2 \\ a_{21}x_1 + a_{22}x_2 \end{bmatrix}$ |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### *Một hàng nhân với một cột cho một tích vô hướng.*

$^1$Einstein đã làm ngắn gọn điều này hơn nữa bằng cách bỏ qua $\sum$. Việc lặp lại $j$ trong $a_{ij}x_j$ tự động mang ý nghĩa phép cộng. Ông cũng viết tổng này là $a_i^j x_j$. Do không phải là Einstein, chúng ta bao gồm chữ $\sum$.

## **Dạng Ma Trận của Một Bước Khử**

$Ax = b$ là một dạng thuận tiện cho phương trình ban đầu. Thế còn các bước khử thì sao? Trong ví dụ này, 2 lần phương trình đầu tiên bị trừ đi từ phương trình thứ hai. Ở vế phải, 2 lần thành phần đầu tiên của $b$ bị trừ đi từ thành phần thứ hai.

| Bước đầu tiên | $b = \begin{bmatrix} 2 \\ 8 \\ 10 \end{bmatrix}$ | thay đổi thành | $b_{\text{mới}} = \begin{bmatrix} 2 \\ 4 \\ 10 \end{bmatrix}$ |
|------------|--------------------------------------------------|------------|---------------------------------------------------------------|
|------------|--------------------------------------------------|------------|---------------------------------------------------------------|

Chúng ta muốn thực hiện phép trừ đó với một ma trận! Cùng kết quả $b_{\text{mới}} = Eb$ đạt được khi chúng ta nhân một "ma trận khử" $E$ với $b$. Nó trừ đi $2b_1$ khỏi $b_2$:

| *Ma trận khử là* | $E = \begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ . |
|----------------------------------|----------------------------------------------------------------------------|
|----------------------------------|----------------------------------------------------------------------------|

**Phép nhân với $E$ trừ đi 2 lần hàng 1 khỏi hàng 2.** Các hàng 1 và 3 vẫn giữ nguyên:

| $\begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 2 \\ 8 \\ 10 \end{bmatrix} = \begin{bmatrix} 2 \\ 4 \\ 10 \end{bmatrix}$ | $\begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix} = \begin{bmatrix} b_1 \\ b_2 - 2b_1 \\ b_3 \end{bmatrix}$ |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Các hàng thứ nhất và thứ ba của $E$ xuất phát từ ma trận đơn vị $I$. Chúng không làm thay đổi các số thứ nhất và thứ ba (2 và 10). Thành phần thứ hai mới là số 4 xuất hiện sau bước khử. Đây là $b_2 - 2b_1$.

Rất dễ dàng để mô tả các "ma trận sơ cấp (elementary matrices)" hoặc "ma trận khử (elimination matrices)" giống như $E$ này. *Bắt đầu với ma trận đơn vị $I$. Đổi một trong các số không của nó thành $-l$:*

*Ma trận đơn vị (identity matrix)* có các số 1 trên đường chéo và các số 0 ở các vị trí khác. Khi đó $Ib = b$ đối với mọi $b$. *Ma trận sơ cấp hoặc ma trận khử $E_{ij}$* có thêm phần tử khác không $-l$ ở vị trí $i, j$. Khi đó $E_{ij}$ trừ đi $l$ lần hàng $j$ khỏi hàng $i$.

**Ví dụ 2** Ma trận $E_{31}$ có $-l$ ở vị trí 3, 1:

| Đơn vị | $I = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ | Khử | $E_{31} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -\ell & 0 & 1 \end{bmatrix}$ |
|----------|-------------------------------------------------------------------------|-------------|----------------------------------------------------------------------------------|
|----------|-------------------------------------------------------------------------|-------------|----------------------------------------------------------------------------------|

Khi bạn nhân $I$ với $b$, bạn nhận được $b$. Nhưng $E_{31}$ trừ đi $l$ lần thành phần thứ nhất khỏi thành phần thứ ba. Với $l = 4$, ví dụ này cho $9 - 4 = 5$:

| $Ib =$ | $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ | $\begin{bmatrix} 1 \\ 3 \\ 9 \end{bmatrix} =$ | $\begin{bmatrix} 1 \\ 3 \\ 9 \end{bmatrix}$ | và | $Eb =$ | $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -4 & 1 & 1 \end{bmatrix}$ | $\begin{bmatrix} 1 \\ 3 \\ 9 \end{bmatrix} =$ | $\begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix}$ |
|--------|---------------------------------------------------------------------|-----------------------------------------------|---------------------------------------------|-----|--------|----------------------------------------------------------------------|-----------------------------------------------|---------------------------------------------|
|--------|---------------------------------------------------------------------|-----------------------------------------------|---------------------------------------------|-----|--------|----------------------------------------------------------------------|-----------------------------------------------|---------------------------------------------|

Thế còn vế trái của $Ax = b$ thì sao? Cả hai vế sẽ được nhân với $E_{31}$ này. *Mục đích của $E_{31}$ là tạo ra một số không ở vị trí (3, 1) của ma trận.*

Ký hiệu phù hợp với mục đích này. Bắt đầu với $A$. Áp dụng các $E$ để tạo ra các số không bên dưới các phần tử xoay (chữ $E$ đầu tiên là $E_{21}$). Kết thúc với một ma trận tam giác $U$. Bây giờ chúng ta sẽ xem xét chi tiết vào những bước đó.

Đầu tiên là một điểm nhỏ. Vectơ $x$ giữ nguyên. Nghiệm $x$ không bị thay đổi bởi phép khử. (Đó có thể là nhiều hơn một điểm nhỏ.) Chính ma trận hệ số là thứ bị thay đổi. Khi chúng ta bắt đầu với $Ax = b$ và nhân với $E$, kết quả là $EAx = Eb$. Ma trận mới $EA$ là kết quả của việc *nhân $E$ với $A$.*

**Thú nhận** Các *ma trận khử $E_{ij}$* là những ví dụ tuyệt vời, nhưng bạn sẽ không thấy chúng ở phần sau. Chúng cho thấy cách một ma trận tác động lên các hàng. Bằng cách thực hiện một vài bước khử, chúng ta sẽ thấy cách *nhân các ma trận* (và thứ tự của các $E$ trở nên quan trọng). *Tích và nghịch đảo* đặc biệt rõ ràng đối với các $E$. Đó là hai ý tưởng mà cuốn sách sẽ sử dụng.

## **Phép Nhân Ma Trận (Matrix Multiplication)**

Câu hỏi lớn là: *Làm thế nào chúng ta nhân hai ma trận?* Khi ma trận đầu tiên là $E$, chúng ta biết nên kỳ vọng điều gì cho $EA$. $E$ cụ thể này trừ đi 2 lần hàng 1 khỏi hàng 2. Số nhân là $l = 2$:

| $EA = \begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ | $\begin{bmatrix} 2 & 4 & -2 \\ 4 & 9 & -3 \\ -2 & -3 & 7 \end{bmatrix} = \begin{bmatrix} 2 & 4 & -2 \\ 0 & 1 & 1 \\ -2 & -3 & 7 \end{bmatrix}$ | (với số không) |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------|

Bước này không làm thay đổi hàng 1 và hàng 3 của $A$. Những hàng đó không đổi trong $EA$ - chỉ có hàng 2 là khác. *Hai lần hàng đầu tiên đã bị trừ đi từ hàng thứ hai.* Phép nhân ma trận đồng nhất với phép khử - và hệ phương trình mới là $EAx = Eb$.

$EAx$ là đơn giản nhưng nó bao hàm một ý tưởng tinh tế. Bắt đầu với $Ax = b$. Nhân cả hai vế với $E$ cho $E(Ax) = Eb$. Với phép nhân ma trận, điều này cũng là $(EA)x = Eb$.

#### **Cái thứ nhất là $E$ nhân $Ax$, cái thứ hai là $EA$ nhân $x$. Chúng giống hệt nhau.**

Không cần ngoặc đơn. Chúng ta chỉ viết $EAx$.

Quy tắc đó mở rộng cho một ma trận $C$ với nhiều vectơ cột. Khi nhân $EAC$, bạn có thể thực hiện $AC$ trước hoặc $EA$ trước. Đây là mấu chốt của "luật kết hợp (associative law)" giống như $3 \times (4 \times 5) = (3 \times 4) \times 5$. Nhân 3 với 20, hoặc nhân 12 với 5. Cả hai câu trả lời đều là 60. Quy luật đó dường như rất rõ ràng đến nỗi khó có thể tưởng tượng rằng nó có thể sai.

"Luật giao hoán (commutative law)" $3 \times 4 = 4 \times 3$ trông thậm chí còn hiển nhiên hơn. Nhưng $EA$ thường khác với $AE$. Khi $E$ nhân ở bên phải, nó tác động lên các *cột* của $A$ - không phải các hàng. $AE$ thực sự trừ đi 2 lần cột 2 khỏi cột 1. Vì vậy $EA \neq AE$.

**Luật kết hợp là đúng**
$$A(BC) = (AB)C$$

**Luật giao hoán là sai**
Thường thì $$AB \neq BA$$

Có một yêu cầu khác đối với phép nhân ma trận. Giả sử $B$ chỉ có một cột (cột này là $b$). Luật ma trận-ma trận cho $EB$ phải đồng nhất với luật ma trận-vectơ cho $Eb$. Hơn thế nữa, chúng ta phải có khả năng *nhân các ma trận $EB$ cho từng cột một lúc:*

*Nếu $B$ có nhiều cột $b_1, b_2, b_3$, thì các cột của $EB$ là $Eb_1, Eb_2, Eb_3$.*

| Phép nhân ma trận | $AB = A \begin{bmatrix} b_1 & b_2 & b_3 \end{bmatrix} = \begin{bmatrix} Ab_1 & Ab_2 & Ab_3 \end{bmatrix}$ | (4) |
|-----------------------|---------------------------------------------------|-----|
|-----------------------|---------------------------------------------------|-----|

Điều này đúng cho phép nhân ma trận trong (3). Nếu bạn nhân cột 3 của $A$ với $E$, bạn nhận được chính xác cột 3 của $EA$:

| $\begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} -2 \\ -3 \\ 7 \end{bmatrix} = \begin{bmatrix} -2 \\ 1 \\ 7 \end{bmatrix}$ | $E(\text{cột } j \text{ của } A) = \text{cột } j \text{ của } EA.$ |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|

Yêu cầu này giải quyết với các cột, trong khi phép khử được áp dụng cho các hàng. **Phần tiếp theo mô tả từng phần tử của mọi tích $AB$.** Vẻ đẹp của phép nhân ma trận là cả ba cách tiếp cận *(hàng, cột, toàn bộ ma trận)* đều cho kết quả đúng.

# **Ma Trận $P_{ij}$ cho một Phép Hoán Đổi Hàng**

Để trừ hàng $j$ khỏi hàng $i$ chúng ta sử dụng $E_{ij}$. Để hoán đổi hoặc "hoán vị" các hàng đó, chúng ta sử dụng một ma trận khác $P_{ij}$ (một **ma trận hoán vị - permutation matrix).** Một phép hoán đổi hàng là cần thiết khi số không ở vị trí phần tử xoay. Ở dưới thấp hơn, cột phần tử xoay đó có thể chứa một số khác không. Bằng cách hoán đổi hai hàng, chúng ta có một phần tử xoay và phép khử tiếp tục tiến lên.

Ma trận $P_{23}$ nào hoán đổi hàng 2 với hàng 3? Chúng ta có thể tìm thấy nó bằng cách hoán đổi các hàng của ma trận đơn vị $I$:

| Ma trận hoán vị | $P_{23} =$ | $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}$ |
|--------------------|------------|---------------------------------------------------------------------|
|                    |            |                                                                     |

Đây là một *ma trận hoán đổi hàng.* Nhân với $P_{23}$ sẽ hoán đổi các thành phần 2 và 3 của bất kỳ vectơ cột nào. Do đó nó cũng hoán đổi các hàng 2 và 3 của bất kỳ ma trận nào:

$$\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix} = \begin{bmatrix} 1 \\ 5 \\ 3 \end{bmatrix} \quad \text{và} \quad \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 2 & 4 & 1 \\ 0 & 6 & 3 \\ 0 & 6 & 5 \end{bmatrix} = \begin{bmatrix} 2 & 4 & 1 \\ 0 & 6 & 5 \\ 0 & 0 & 3 \end{bmatrix}.$$

(Note: fixed typo in original text: second matrix should have P23 on the left, but original text shows [1 0 0; 0 1 1; 0 0 1] which is an elementary matrix, but wait, the text says `[1 0 0; 0 0 1; 0 1 0] [1; 3; 5] = [1; 5; 3]` but the printed matrix is `[1 0 0; 0 1 1; 0 0 1]`. Let's correct it to P23 based on context).
Correction:
$$\begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix} = \begin{bmatrix} 1 \\ 5 \\ 3 \end{bmatrix} \quad \text{và} \quad \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} 2 & 4 & 1 \\ 0 & 6 & 3 \\ 0 & 6 & 5 \end{bmatrix} = \begin{bmatrix} 2 & 4 & 1 \\ 0 & 6 & 5 \\ 0 & 6 & 3 \end{bmatrix}.$$

Ở bên phải, $P_{23}$ đang làm những gì nó được tạo ra. Với số không ở vị trí phần tử xoay thứ hai và "6" ở bên dưới nó, phép hoán đổi đưa 6 vào phần tử xoay.

Các ma trận *tác động (act).* Chúng không chỉ nằm ở đó. Chúng ta sẽ sớm gặp các ma trận hoán vị khác, chúng có thể thay đổi thứ tự của nhiều hàng. Các hàng 1, 2, 3 có thể được di chuyển thành 3, 1, 2. $P_{23}$ của chúng ta là một ma trận hoán vị cụ thể - nó hoán đổi các hàng 2 và 3.

**Ma Trận Hoán Đổi Hàng (Row Exchange Matrix)** $P_{ij}$ là ma trận đơn vị với các hàng $i$ và $j$ bị đảo ngược. Khi **"ma trận hoán vị"** $P_{ij}$ này nhân với một ma trận, nó hoán đổi các hàng $i$ và $j$.

Để hoán đổi phương trình 1 và 3 hãy nhân với
$$P_{13} = \begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix}$$

Thông thường các phép hoán đổi hàng không được yêu cầu. Tỷ lệ rất cao là phép khử chỉ sử dụng các $E_{ij}$. Nhưng các $P_{ij}$ luôn sẵn sàng nếu cần, để di chuyển một phần tử xoay lên đường chéo chính.

# **Ma Trận Bổ Sung (The Augmented Matrix)**

Cuốn sách này cuối cùng sẽ vượt xa khỏi phép khử. Ma trận có đủ mọi ứng dụng thực tế, trong đó chúng được nhân với nhau. Điểm khởi đầu tốt nhất của chúng ta là một ma trận vuông $E$ nhân với một ma trận vuông $A$, bởi vì chúng ta đã gặp điều này trong phép khử - và chúng ta biết kỳ vọng kết quả gì cho $EA$. Bước tiếp theo là cho phép một *ma trận chữ nhật (rectangular matrix).* Nó vẫn xuất phát từ các phương trình ban đầu của chúng ta, nhưng bây giờ nó bao gồm cả vế phải $b$.

Ý tưởng chính: Phép khử thực hiện các phép toán hàng giống nhau cho $A$ và $b$. *Chúng ta có thể bao gồm $b$ như một cột bổ sung và theo dõi nó thông qua phép khử.* Ma trận $A$ được mở rộng hay "bổ sung" bởi cột dư $b$:

| Ma trận bổ sung | $\begin{bmatrix} A & b \end{bmatrix} = \begin{bmatrix} 2 & 4 & -2 & 2 \\ 4 & 9 & -3 & 8 \\ -2 & -3 & 7 & 10 \end{bmatrix}$ |
|------------------|------------------------------------------------------------------------------------------------|
|------------------|------------------------------------------------------------------------------------------------|

*Phép khử tác động lên toàn bộ các hàng của ma trận này.* Vế trái và vế phải đều được nhân với $E$, để trừ đi 2 lần phương trình 1 khỏi phương trình 2. Với $\begin{bmatrix} A & b \end{bmatrix}$ những bước đó xảy ra cùng nhau:

| $\begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 2 & 4 & -2 & 2 \\ 4 & 9 & -3 & 8 \\ -2 & -3 & 7 & 10 \end{bmatrix} = \begin{bmatrix} 2 & 4 & -2 & 2 \\ 0 & 1 & 1 & 4 \\ -2 & -3 & 7 & 10 \end{bmatrix}$ |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Hàng thứ hai mới chứa $0, 1, 1, 4$. Phương trình thứ hai mới là $x_2 + x_3 = 4$. Phép nhân ma trận hoạt động theo hàng và đồng thời theo cột:

**HÀNG** Mỗi hàng của $E$ tác động lên $\begin{bmatrix} A & b \end{bmatrix}$ để cho ra một hàng của $\begin{bmatrix} EA & Eb \end{bmatrix}$.

**CỘT** $E$ tác động lên mỗi cột của $\begin{bmatrix} A & b \end{bmatrix}$ để cho ra một cột của $\begin{bmatrix} EA & Eb \end{bmatrix}$.

Chú ý lại từ "tác động (acts)." Điều này là thiết yếu. Các ma trận thực hiện điều gì đó! Ma trận $A$ tác động lên $x$ để tạo ra $b$. Ma trận $E$ hoạt động trên $A$ để cho ra $EA$. Toàn bộ quá trình khử là một chuỗi các phép toán hàng, bí danh của phép nhân ma trận. $A$ đi đến $E_{21}A$ rồi đi đến $E_{31}E_{21}A$. Cuối cùng $E_{32}E_{31}E_{21}A$ là một ma trận tam giác.

Vế phải được bao gồm trong ma trận bổ sung. Kết quả cuối cùng là một hệ phương trình tam giác. Chúng ta dừng lại để làm bài tập về phép nhân với $E$, trước khi viết ra các quy tắc cho tất cả các phép nhân ma trận (bao gồm cả phép nhân khối - block multiplication).

#### **• ÔN TẬP CÁC Ý TƯỞNG CHÍNH •**

- **1.** $Ax = x_1$ lần cột 1 $+ \dots + x_n$ lần cột $n$. Và $(Ax)_i = \sum_{j=1}^n a_{ij}x_j$.
- **2.** Ma trận đơn vị = $I$, ma trận khử = $E_{ij}$ sử dụng $l_{ij}$, ma trận hoán đổi = $P_{ij}$.
- **3.** Nhân $Ax = b$ với $E_{21}$ sẽ trừ đi một bội số $l_{21}$ của phương trình 1 khỏi phương trình 2. Số $-l_{21}$ là phần tử $(2, 1)$ của ma trận khử $E_{21}$.
- **4.** Đối với ma trận bổ sung $\begin{bmatrix} A & b \end{bmatrix}$, bước khử đó cho ra $\begin{bmatrix} E_{21}A & E_{21}b \end{bmatrix}$.
- **5.** Khi $A$ nhân với bất kỳ ma trận $B$ nào, nó nhân với từng cột của $B$ một cách riêng biệt.

#### **• CÁC VÍ DỤ ĐÃ GIẢI •**

**2.3 A** Ma trận $3 \times 3$ $E_{21}$ nào trừ 4 lần hàng 1 khỏi hàng 2? Ma trận $P_{32}$ nào hoán đổi hàng 2 và hàng 3? Nếu bạn nhân $A$ ở *bên phải* thay vì bên trái, hãy mô tả các kết quả $AE_{21}$ và $AP_{32}$.

**Lời giải** Bằng cách thực hiện các phép toán đó trên ma trận đơn vị $I$, chúng ta tìm được

| $E_{21} = \begin{bmatrix} 1 & 0 & 0 \\ -4 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ | và | $P_{32} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}$ |
|-------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------|
|-------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------|

Nhân với $E_{21}$ ở vế phải sẽ trừ 4 lần **cột 2** khỏi **cột 1**. Nhân với $P_{32}$ ở bên phải sẽ hoán đổi **các cột 2** và **3**.

**2.3 B** Viết xuống ma trận bổ sung $\begin{bmatrix} A & b \end{bmatrix}$ với một cột bổ sung:

- $x + 2y + 2z = 1$
- $4x + 8y + 9z = 3$
- $3y + 2z = 1$

Áp dụng $E_{21}$ và sau đó $P_{32}$ để đạt tới một hệ tam giác. Giải bằng phép thế ngược. Ma trận kết hợp $P_{32}E_{21}$ nào sẽ thực hiện cả hai bước cùng một lúc?

**Lời giải** $E_{21}$ loại bỏ **4 ở** cột 1. Nhưng số không cũng xuất hiện ở cột **2:**

| $\begin{bmatrix} A & b \end{bmatrix} =$ | $\begin{bmatrix} 1 & 2 & 2 & 1 \\ 4 & 8 & 9 & 3 \\ 0 & 3 & 2 & 1 \end{bmatrix}$ | và | $E_{21}\begin{bmatrix} A & b \end{bmatrix} =$ | $\begin{bmatrix} 1 & 2 & 2 & 1 \\ 0 & 0 & 1 & -1 \\ 0 & 3 & 2 & 1 \end{bmatrix}$ |
|-------------|---------------------------------------------------------------------------------|-----|-------------------|---------------------------------------------------------------------------------|
|-------------|---------------------------------------------------------------------------------|-----|-------------------|---------------------------------------------------------------------------------|
(Note: E21 subtracts 4 times row 1 from row 2. Row 2 was [4 8 9 3], Row 1 was [1 2 2 1]. 4*Row1 is [4 8 8 4]. So [4 8 9 3] - [4 8 8 4] = [0 0 1 -1]. Corrected the matrix to match this logic, replacing the original OCR error which had 0 0 0 1)

Bây giờ $P_{32}$ hoán đổi các hàng 2 và 3. Phép thế ngược cho ra $z$ sau đó $y$ và $x$.

$$P_{32}E_{21}\begin{bmatrix} A & b \end{bmatrix} = \begin{bmatrix} 1 & 2 & 2 & 1 \\ 0 & 3 & 2 & 1 \\ 0 & 0 & 1 & -1 \end{bmatrix} \quad \text{và} \quad \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \\ -1 \end{bmatrix}$$

Đối với ma trận $P_{32}E_{21}$ thực hiện cả hai bước cùng lúc, hãy *áp dụng* $P_{32}$ *lên* $E_{21}$.

| Một ma trận | $P_{32}E_{21} =$ hoán đổi các hàng của $E_{21} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ -4 & 1 & 0 \end{bmatrix}$ |
|------------|----------------------------------------------------------------------------------------------------------------------|
| Cả hai bước |                                                                                                                      |

**2.3 C** Nhân các ma trận này theo hai cách. Thứ nhất, các hàng của $A$ nhân các cột của $B$. Thứ hai, *các cột của $A$ nhân các hàng của $B$.* Cách làm không thông thường đó tạo ra hai ma trận cộng lại thành $AB$. Cần bao nhiêu phép nhân thông thường tách biệt?

| Cả hai cách | $AB = \begin{bmatrix} 3 & 4 \\ 1 & 5 \\ 2 & 0 \end{bmatrix} \begin{bmatrix} 2 & 4 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 10 & 16 \\ 7 & 9 \\ 4 & 8 \end{bmatrix}$ |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
(Note: corrected typo in original text where (1,2) entry was 1 instead of 16).

**Lời giải** Các hàng của $A$ nhân các cột của $B$ là các tích vô hướng của các vectơ:

| $(\text{hàng } 1) \cdot (\text{cột } 1) = \begin{bmatrix} 3 & 4 \end{bmatrix} \begin{bmatrix} 2 \\ 1 \end{bmatrix} = \mathbf{10}$ | là phần tử $(1, 1)$ của $AB$ |
|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|

| $(\text{hàng } 2) \cdot (\text{cột } 1) = $ | $\begin{bmatrix} 1 & 5 \end{bmatrix}$ | $\begin{bmatrix} 2 \\ 1 \end{bmatrix} = \mathbf{7}$ | là phần tử $(2, 1)$ của $AB$ |
|------------------------|---------------------------------------|-----------------------------------------------------|---------------------------|
|------------------------|---------------------------------------|-----------------------------------------------------|---------------------------|

Chúng ta cần 6 tích vô hướng, mỗi tích cần 2 phép nhân, tổng cộng là 12 ( $3 \cdot 2 \cdot 2$). Cùng một $AB$ xuất phát từ *các cột của $A$ nhân các hàng của $B$.* Một cột nhân với một hàng là một ma trận.

$$AB = \begin{bmatrix} 3 \\ 1 \\ 2 \end{bmatrix} \begin{bmatrix} 2 & 4 \end{bmatrix} + \begin{bmatrix} 4 \\ 5 \\ 0 \end{bmatrix} \begin{bmatrix} 1 & 1 \end{bmatrix} = \begin{bmatrix} 6 & 12 \\ 2 & 4 \\ 4 & 8 \end{bmatrix} + \begin{bmatrix} 4 & 4 \\ 5 & 5 \\ 0 & 0 \end{bmatrix}$$
(Note: fixed typo in original text which had 3x3 matrices instead of outer products of columns and rows).

### **Bài tập 2.3 (Problem Set 2.3)**

**Các bài toán 1-15 liên quan đến các ma trận khử.**

**1** Viết ra các ma trận $3 \times 3$ tạo ra các bước khử này:
  - (a) $E_{21}$ trừ đi 5 lần hàng 1 khỏi hàng 2.

  - (b) $E_{32}$ trừ đi -7 lần hàng 2 khỏi hàng 3.
  - (c) $P$ hoán đổi hàng 1 và 2, sau đó là hàng 2 và 3.

**2** Trong Bài toán 1, áp dụng $E_{21}$ và sau đó $E_{32}$ lên $b = (1, 0, 0)$ cho ra $E_{32}E_{21}b = \_\_$. Áp dụng $E_{32}$ trước $E_{21}$ cho ra $E_{21}E_{32}b = \_\_$. Khi $E_{32}$ đứng trước, hàng \_\_ không bị ảnh hưởng từ hàng 3.

**3** Ba ma trận $E_{21}, E_{31}, E_{32}$ nào đưa $A$ về dạng tam giác $U$?

| $A = \begin{bmatrix} 1 & 1 & 0 \\ 4 & 6 & 1 \\ -2 & 2 & 0 \end{bmatrix}$ | và | $E_{32}E_{31}E_{21}A = U.$ |
|--------------------------------------------------------------------------|-----|----------------------------|
|--------------------------------------------------------------------------|-----|----------------------------|

Nhân các $E$ đó lại để có được một ma trận $M$ thực hiện phép khử: $MA = U$.

**4** Bao gồm $b = (1, 0, 0)$ làm cột thứ tư trong Bài toán 3 để tạo ra $\begin{bmatrix} A & b \end{bmatrix}$. Thực hiện các bước khử trên ma trận bổ sung này để giải $Ax = b$.

**5** Giả sử $a_{33} = 7$ và phần tử xoay thứ ba là 5. **Nếu** bạn thay đổi $a_{33}$ thành 11, phần tử xoay thứ ba là **\_\_. Nếu** bạn thay đổi $a_{33}$ thành \_\_, thì không có phần tử xoay thứ ba.

**6 Nếu** mọi cột của $A$ đều là một bội số của $(1, 1, 1)$, thì $Ax$ luôn là một bội số của $(1, 1, 1)$. Làm một ví dụ $3 \times 3$. Có bao nhiêu phần tử xoay được sinh ra bởi phép khử?

**7** Giả sử $E$ trừ 7 lần hàng 1 khỏi hàng 3.
  - (a) Để *nghịch đảo (invert)* bước đó bạn nên \_\_ 7 lần hàng \_\_ vào hàng \_\_.
  - (b) "Ma trận nghịch đảo" $E^{-1}$ nào thực hiện bước ngược lại đó (sao cho $E^{-1}E = I$)?
  - (c) **Nếu** bước đảo ngược được áp dụng trước (và sau đó là $E$) hãy chỉ ra rằng $EE^{-1} = I$.

**8** *Định thức (determinant)* của $M = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ là $\det M = ad - bc$. Trừ $l$ lần hàng 1 khỏi hàng 2 để tạo ra một $M^*$ mới. Chứng minh rằng $\det M^* = \det M$ đối với mọi $l$. Khi $l = c/a$, tích của các phần tử xoay bằng định thức: $a(d - lb)$ bằng $ad - bc$.

**9** (a) $E_{21}$ trừ hàng 1 khỏi hàng 2 và sau đó $P_{23}$ hoán đổi hàng 2 và hàng 3. Ma trận $M = P_{23}E_{21}$ nào thực hiện cả hai bước cùng một lúc?
  - (b) $P_{23}$ hoán đổi hàng 2 và hàng 3 và sau đó $E_{31}$ trừ hàng 1 khỏi hàng 3. Ma trận $M = E_{31}P_{23}$ nào thực hiện cả hai bước cùng một lúc? Giải thích tại sao các $M$ giống nhau nhưng các $E$ lại khác nhau.

**10** (a) Ma trận $3 \times 3$ $E_{13}$ nào sẽ cộng hàng 3 vào hàng 1?
  - (b) Ma trận nào cộng hàng 1 vào hàng 3 và *đồng thời* cộng hàng 3 vào hàng 1?
  - (c) Ma trận nào cộng hàng 1 vào hàng 3 và *sau đó* cộng hàng 3 vào hàng 1?

**11** Tạo ra một ma trận có $a_{11} = a_{22} = a_{33} = 1$ nhưng phép khử tạo ra hai phần tử xoay âm mà không cần hoán đổi hàng. (Phần tử xoay đầu tiên là 1.)

**12** Nhân các ma trận này:

| $\begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix} \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix} \begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix}$ | $\begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ -1 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 2 & 3 \\ 1 & 3 & 0 \\ 1 & 4 & 0 \end{bmatrix}$ |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|

**13** Giải thích những sự thật này. Nếu cột thứ ba của $B$ toàn bộ là số không, thì cột thứ ba của $EB$ toàn bộ là số không (đối với bất kỳ $E$ nào). Nếu *hàng* thứ ba của $B$ toàn bộ là số không, thì hàng thứ ba của $EB$ có thể *không* là số không.

**14** Ma trận $4 \times 4$ này sẽ cần các ma trận khử $E_{21}$ và $E_{32}$ và $E_{43}$. Những ma trận đó là gì?

$$A = \begin{bmatrix} 2 & -1 & 0 & 0 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ 0 & 0 & -1 & 2 \end{bmatrix}.$$

**15** Viết ra ma trận $3 \times 3$ có $a_{ij} = 2i - 3j$. Ma trận này có $a_{32} = 0$, nhưng phép khử vẫn cần $E_{32}$ để tạo ra số không ở vị trí 3, 2. Bước nào trước đó đã phá hủy số không ban đầu và $E_{32}$ là gì?

#### **Các bài toán 16-23 liên quan đến việc tạo ra và nhân ma trận.**

**16** Viết những bài toán cổ đại này dưới dạng ma trận $2 \times 2$ $Ax = b$ và giải chúng:
  - (a) $X$ nhiều tuổi gấp đôi $Y$ và tổng số tuổi của họ là 33.
  - (b) $(x, y) = (2, 5)$ và $(3, 7)$ nằm trên đường thẳng $y = mx + c$. Tìm $m$ và $c$.

**17** Parabol $y = a + bx + cx^2$ đi qua các điểm $(x, y) = (1, 4)$ và $(2, 8)$ và $(3, 14)$. Tìm và giải một phương trình ma trận cho các ẩn số $(a, b, c)$.

**18** Nhân các ma trận này theo thứ tự $EF$ và $FE$:

| $E = \begin{bmatrix} 1 & 0 & 0 \\ a & 1 & 0 \\ b & 0 & 1 \end{bmatrix}$ | $F = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & c & 1 \end{bmatrix}$ |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
|-------------------------------------------------------------------------|-------------------------------------------------------------------------|

Đồng thời tính $E^2 = EE$ và $F^3 = FFF$. Bạn có thể đoán $F^{100}$.

**19** Nhân các ma trận hoán đổi hàng này theo thứ tự $PQ$ và $QP$ và $P^2$:

| $P = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ | và | $Q = \begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix}$ |
|-------------------------------------------------------------------------|-----|-------------------------------------------------------------------------|
|-------------------------------------------------------------------------|-----|-------------------------------------------------------------------------|

Tìm một ma trận không đường chéo (non-diagonal) khác có bình phương là $M^2 = I$.

**20** (a) Giả sử tất cả các cột của $B$ đều giống nhau. Thế thì tất cả các cột của $EB$ đều giống nhau, bởi vì mỗi cột là $E$ nhân \_\_.
  - (b) Giả sử tất cả các hàng của $B$ đều là $\begin{bmatrix} 1 & 2 & 4 \end{bmatrix}$. Bằng ví dụ hãy chỉ ra rằng tất cả các hàng của $EB$ *không* phải là $\begin{bmatrix} 1 & 2 & 4 \end{bmatrix}$. Sự thật là những hàng đó là \_\_.

**21** Nếu $E$ cộng hàng 1 vào hàng 2 và $F$ cộng hàng 2 vào hàng 1, thì $EF$ có bằng $FE$ không?

**22** Các phần tử của $A$ và $x$ là $a_{ij}$ và $x_j$. Nên thành phần đầu tiên của $Ax$ là $\sum a_{1j}x_j = a_{11}x_1 + \dots + a_{1n}x_n$. Nếu $E_{21}$ trừ hàng 1 khỏi hàng 2, viết công thức cho
  - (a) thành phần thứ ba của $Ax$
  - (b) phần tử $(2, 1)$ của $E_{21}A$
  - (c) phần tử $(2, 1)$ của $E_{21}(E_{21}A)$
  - (d) thành phần thứ nhất của $E_{21}Ax$.

**23** Ma trận khử $E = \begin{bmatrix} 1 & 0 \\ -2 & 1 \end{bmatrix}$ trừ đi 2 lần hàng 1 của $A$ khỏi hàng 2 của $A$. Kết quả là $EA$. Ảnh hưởng của $E(EA)$ là gì? Theo thứ tự ngược lại $AE$, chúng ta đang trừ đi 2 lần \_\_ của $A$ khỏi \_\_. (Hãy làm các ví dụ.)

### **Các bài toán 24-27 bao gồm cột $b$ trong ma trận bổ sung $\begin{bmatrix} A & b \end{bmatrix}$.**

**24** Áp dụng phép khử cho ma trận bổ sung $2 \times 3$ $\begin{bmatrix} A & b \end{bmatrix}$. Hệ tam giác $Ux = c$ là gì? Nghiệm $x$ là gì?

$$Ax = \begin{bmatrix} 2 & 3 \\ 4 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 1 \\ 17 \end{bmatrix}.$$

**25** Áp dụng phép khử cho ma trận bổ sung $3 \times 4$ $\begin{bmatrix} A & b \end{bmatrix}$. Làm sao bạn biết hệ này không có nghiệm? Hãy thay đổi số 6 cuối cùng để *có* một nghiệm.

$$Ax = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 3 & 4 \\ 3 & 5 & 7 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ 6 \end{bmatrix}.$$

**26** Các phương trình $Ax = b$ và $Ax^* = b^*$ có chung ma trận $A$. Ma trận bổ sung kép nào bạn nên sử dụng trong phép khử để giải cả hai phương trình cùng lúc? Hãy giải cả hai phương trình này bằng cách thao tác trên một ma trận $2 \times 4$:

$$\begin{bmatrix} 1 & 4 \\ 2 & 7 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix} \quad \text{và} \quad \begin{bmatrix} 1 & 4 \\ 2 & 7 \end{bmatrix} \begin{bmatrix} u \\ v \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}.$$
(Note: corrected typo from [x 4; 2 7] to [1 4; 2 7] in the first equation based on context).

**27** Chọn các số $a, b, c, d$ trong ma trận bổ sung này sao cho (a) không có nghiệm
  - (b) có vô số nghiệm.

$$\begin{bmatrix} A & b \end{bmatrix} = \begin{bmatrix} 1 & 2 & 3 & a \\ 0 & 4 & 5 & b \\ 0 & 0 & d & c \end{bmatrix}$$

Những số nào trong $a, b, c$ hoặc $d$ không có ảnh hưởng đến tính giải được?

**28** Nếu $AB = I$ và $BC = I$, sử dụng luật kết hợp để chứng minh $A = C$.

# **Các Bài toán Thử thách (Challenge Problems)**

**29** Tìm ma trận tam giác $E$ rút gọn *"Ma trận Pascal"* thành một ma trận Pascal nhỏ hơn:

| Phép khử trên cột 1 | $E$ | $\begin{bmatrix} 1 & 0 & 0 & 0 \\ 1 & 2 & 1 & 0 \\ 1 & 3 & 3 & 0 \end{bmatrix}$ | $E = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 2 \end{bmatrix}$ |  |
|-------------------------|-----|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|--|
|                         |     |                                                                                 |                                                                                     |  |

(Note: omitted the broken table with [1 | 0 | 0 | 0 | = ...] below it, reconstructing what makes sense).

Ma trận $M$ (nhân nhiều $E$) nào rút gọn hoàn toàn Pascal về $I$? Ma trận tam giác của Pascal là ngoại lệ, tất cả các số nhân của nó đều là $l_{ij} = 1$.

**30** Viết $M = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ (Note: reconstructed based on context and typo 'rn i l') thành tích của nhiều thừa số $A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ và $B = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}$. (Note: reconstructed based on context and typos 'D ' and '6 ½').
  - (a) Ma trận $E$ nào trừ hàng 1 khỏi hàng 2 để làm cho hàng 2 của $EM$ nhỏ hơn?
  - (b) Ma trận $F$ nào trừ hàng 2 của $EM$ khỏi hàng 1 để rút gọn hàng 1 của $FEM$?
  - (c) Tiếp tục các $E$ và $F$ cho đến khi (nhiều $E$ và $F$) nhân $(M)$ bằng $(A$ hoặc $B)$.
  - (d) $E$ và $F$ là các nghịch đảo của $A$ và $B$! Chuyển tất cả các $E$ và $F$ sang vế phải sẽ cho bạn kết quả mong muốn $M = \text{tích của các } A \text{ và } B$. Điều này khả thi cho các ma trận nguyên $M = \begin{bmatrix} a & b \\ c & d \end{bmatrix} > 0$ có $ad - bc = 1$.

**31** Tìm các ma trận khử $E_{21}$ sau đó $E_{32}$ sau đó $E_{43}$ để biến $K$ thành $U$:

$$E_{43}E_{32}E_{21}K = U.$$
(Note: corrected = I. to = U. based on context).

**Áp dụng ba bước đó lên ma trận đơn vị $I$,** để **nhân** $E_{43}E_{32}E_{21}$.

# **2.4 Các Quy Tắc cho Các Phép Toán Ma Trận (Rules for Matrix Operations)**

**1** Các ma trận $A$ có $n$ cột nhân với các ma trận $B$ có $n$ hàng: $A_{m \times n} B_{n \times p} = C_{m \times p}$.
**2** Mỗi phần tử trong $AB = C$ là một tích vô hướng: $C_{ij} = (\text{hàng } i \text{ của } A) \cdot (\text{cột } j \text{ của } B)$.
**3** Quy tắc này được chọn sao cho $AB$ **nhân** $C$ **bằng** $A$ **nhân** $BC$. Và $(AB)x = A(Bx)$.
**4** Có nhiều cách hơn để tính $AB$: $(A \text{ nhân các cột của } B)$, $(\text{các hàng của } A \text{ nhân } B)$, $(\text{các cột nhân các hàng})$.
**5** Thông thường $AB = BA$ là không đúng. Trong đa số trường hợp *$A$ không giao hoán với $B$.*
**6** Các ma trận có thể được nhân theo **khối (blocks):** $A = \begin{bmatrix} A_1 & A_2 \end{bmatrix}$ nhân với $B = \begin{bmatrix} B_1 \\ B_2 \end{bmatrix}$ là $A_1B_1 + A_2B_2$.

Tôi sẽ bắt đầu với các sự thật cơ bản. Ma trận là một mảng hình chữ nhật gồm các con số hay "phần tử". Khi $A$ có $m$ hàng và $n$ cột, nó là một ma trận *$m$ nhân $n$*. Các ma trận có thể cộng lại với nhau nếu kích thước (shape) của chúng giống nhau. Chúng có thể nhân với bất kỳ hằng số $c$ nào. Dưới đây là các ví dụ về $A + B$ và $2A$, đối với các ma trận $3 \times 2$:

| $\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 0 & 0 \end{bmatrix} + \begin{bmatrix} 2 & 2 \\ 4 & 2 \\ 9 & 9 \end{bmatrix} = \begin{bmatrix} 3 & 4 \\ 7 & 8 \\ 9 & 9 \end{bmatrix}$ | và | $2 \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 2 & 4 \\ 6 & 8 \\ 0 & 0 \end{bmatrix}$ |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-------------------------------------------------------------------------------------------------------------------|
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-------------------------------------------------------------------------------------------------------------------|

Các ma trận được cộng chính xác giống như cách các vectơ được cộng - từng phần tử một. Chúng ta thậm chí có thể coi một vectơ cột như một ma trận chỉ có một cột (vậy nên $n = 1$). Ma trận $-A$ xuất phát từ phép nhân với $c = -1$ (đảo ngược tất cả các dấu). Cộng $A$ với $-A$ để lại *ma trận không (zero matrix),* với tất cả các phần tử đều bằng không. Tất cả điều này chỉ là ý thức thông thường (common sense).

*Phần tử ở hàng $i$ và cột $j$ được gọi là $a_{ij}$ hoặc $A(i, j)$. Khi đó* các phần tử dọc theo hàng đầu tiên là $a_{11}, a_{12}, \dots, a_{1n}$. Phần tử ở góc dưới bên trái trong ma trận là $a_{m1}$ và góc dưới bên phải là $a_{mn}$. Số hàng $i$ đi từ 1 đến $m$. Số cột $j$ đi từ 1 đến $n$.

Phép cộng ma trận thì dễ. Câu hỏi nghiêm túc là *phép nhân ma trận.* Khi nào chúng ta có thể nhân $A$ với $B$, và tích $AB$ là gì? *Phần này đưa ra 4 cách để tìm $AB$.* Nhưng chúng ta không thể nhân khi $A$ và $B$ đều là $3 \times 2$. Chúng không vượt qua bài kiểm tra sau:

*Để nhân $AB$: Nếu $A$ có $n$ cột, $B$ phải có $n$ hàng.*

Khi $A$ là $3 \times 2$, ma trận $B$ có thể là $2 \times 1$ (một vectơ) hoặc $2 \times 2$ (vuông) hoặc $2 \times 20$. *Mọi cột của $B$ đều được nhân với $A$.* Tôi sẽ bắt đầu phép nhân ma trận theo *cách tích vô hướng (dot product way),* và quay lại với *cách theo cột (column way): A* nhân với các cột của $B$. Cả hai cách đều tuân theo quy tắc sau:

**Quy Luật Cơ Bản của Phép Nhân Ma Trận (Fundamental Law of Matrix Multiplication)** *$AB$ nhân $C$ bằng $A$ nhân $BC$* (1)

Các dấu ngoặc đơn có thể di chuyển một cách an toàn trong $(AB)C = A(BC)$. Đại số tuyến tính phụ thuộc vào định luật này.

Giả sử $A$ là $m \times n$ và $B$ là $n \times p$. Chúng ta có thể nhân. Tích $AB$ là $m \times p$.

$$(m \times n)(n \times p) = (m \times p) \begin{bmatrix} m \text{ hàng} \\ n \text{ cột} \end{bmatrix} \begin{bmatrix} n \text{ hàng} \\ p \text{ cột} \end{bmatrix} = \begin{bmatrix} m \text{ hàng} \\ p \text{ cột} \end{bmatrix}.$$

Một hàng nhân với một cột là một trường hợp cực đoan. Khi đó $1 \times n$ nhân với $n \times 1$. Kết quả sẽ là $1 \times 1$. Số duy nhất đó là "tích vô hướng".

Trong mọi trường hợp $AB$ được lấp đầy bằng các tích vô hướng. Đối với góc trên cùng, phần tử $(1, 1)$ của $AB$ là $(\text{hàng 1 của } A) \cdot (\text{cột 1 của } B)$. Đây là cách thứ nhất, và là cách thông thường, để nhân các ma trận. **Lấy tích vô hướng của mỗi hàng của $A$ với mỗi cột của $B$.**

**1. Phần tử ở hàng $i$ và cột $j$ của $AB$ là $(\text{hàng } i \text{ của } A) \cdot (\text{cột } j \text{ của } B)$.**

Hình 2.8 chọn ra hàng thứ hai ($i = 2$) của một ma trận $A$ kích thước $4 \times 5$. Nó chọn ra cột thứ ba ($j = 3$) của ma trận $B$ kích thước $5 \times 6$. Tích vô hướng của chúng đi vào hàng 2 và cột 3 của $AB$. Ma trận $AB$ có *số hàng bằng với $A$ (4 hàng), và số cột bằng với $B$.*

$$\begin{bmatrix} * \\ a_{i1} & a_{i2} & \dots & a_{i5} \\ * \\ * \end{bmatrix} \begin{bmatrix} * & * & b_{1j} & * & * & * \\ & & b_{2j} & & & \\ & & \vdots & & & \\ & & & b_{5j} & & \end{bmatrix} = \begin{bmatrix} * & * & (AB)_{ij} & * & * & * \\ * & * & * & * & * & \end{bmatrix}$$
A là $4 \times 5$      B là $5 \times 6$       $AB$  là  $(4 \times 5)(5 \times 6) = 4 \times 6$

Hình 2.8: Ở đây $i=2$ và $j=3$. Khi đó $(AB)_{23}$ là **(hàng 2) $\cdot$ (cột 3)** = tổng của $a_{2k}b_{k3}$.

**Ví dụ 1** Các ma trận vuông có thể được nhân với nhau nếu và chỉ nếu chúng có cùng kích thước:

$$\begin{bmatrix} 1 & 1 \\ 2 & -1 \end{bmatrix} \begin{bmatrix} 2 & 2 \\ 3 & 4 \end{bmatrix} = \begin{bmatrix} 5 & 6 \\ 1 & 0 \end{bmatrix}.$$

Tích vô hướng đầu tiên là $1 \cdot 2 + 1 \cdot 3 = 5$. Ba tích vô hướng nữa cho 6, 1 và 0. Mỗi tích vô hướng đòi hỏi hai phép nhân - do đó có tám phép nhân tất cả.

Nếu $A$ và $B$ là $n \times n$, thì $AB$ cũng vậy. Nó chứa $n^2$ tích vô hướng, hàng của $A$ nhân với cột của $B$. Mỗi tích vô hướng cần $n$ phép nhân, vậy nên **việc tính toán $AB$ sử dụng $n^3$ phép nhân riêng biệt**. Với $n = 100$, chúng ta nhân một triệu lần. Với $n = 2$, chúng ta có $n^3 = 8$.

Cho đến gần đây các nhà toán học vẫn nghĩ rằng $AB$ hoàn toàn cần $2^3 = 8$ phép nhân. Thế rồi có người tìm ra cách để thực hiện nó với 7 phép nhân (và thêm các phép cộng). Bằng cách chia các ma trận $n \times n$ thành các khối $2 \times 2$, ý tưởng này cũng làm giảm số lượng phép toán để nhân các ma trận lớn. Thay vì $n^3$ phép nhân, số lượng hiện đã giảm xuống còn $n^{2.376}$. Có lẽ $n^2$ là có thể? Nhưng các thuật toán đó phức tạp đến mức việc tính toán khoa học vẫn được thực hiện theo cách $n^3$ thông thường.

**Ví dụ 2** Giả sử $A$ là một vectơ hàng ($1 \times 3$) và $B$ là một vectơ cột ($3 \times 1$). Khi đó $AB$ là $1 \times 1$ (chỉ một phần tử, tích vô hướng). Mặt khác $B$ nhân $A$ *(một cột nhân một hàng)* là một ma trận đầy đủ $3 \times 3$. Phép nhân này được cho phép!

| Cột nhân hàng                          | $\begin{bmatrix} 0 \\ 1 \\ 2 \end{bmatrix} \begin{bmatrix} 1 & 2 & 3 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 \\ 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix}$ |
|-------------------------------------------|---------------------------------------------------------------------|
| $(n \times 1)(1 \times n) = (n \times n)$ |                                                                     |

Một hàng nhân với một cột là một *tích "trong" (inner product)* - đó là tên gọi khác của tích vô hướng. Một cột nhân với một hàng là một *tích "ngoài" (outer product).* Đây là những trường hợp cực đoan của phép nhân ma trận.

# **Cách Thứ Hai và Thứ Ba: Hàng và Cột (Rows and Columns)**

Nhìn chung, $A$ nhân với mỗi cột của $B$. Kết quả là một cột của $AB$. Trong cột đó, chúng ta đang kết hợp các cột của $A$. *Mỗi cột của $AB$ là một sự kết hợp của các cột của $A$.* Đó là bức tranh cột của phép nhân ma trận:

| 2. Ma trận $A$ nhân với mọi cột của $B$ | $A \begin{bmatrix} b_1 & \cdots & b_p \end{bmatrix} = \begin{bmatrix} Ab_1 & \cdots & Ab_p \end{bmatrix}$ |
|-----------------------------------------|------------------------------------------|
|                                         |                                          |

Bức tranh hàng thì ngược lại. Mỗi hàng của $A$ nhân với toàn bộ ma trận $B$. Kết quả là một hàng của $AB$. **Mọi hàng của $AB$ là một sự kết hợp của các hàng của $B$:**

| 3. Mọi hàng của $A$ nhân với ma trận $B$ | $[\text{hàng } i \text{ của } A] \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 6 & 7 & 8 \end{bmatrix} = [\text{hàng } i \text{ của } AB].$ |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
(Note: corrected the matrix [1 2 3; 4 5 6; 6 7 8] as B based on context).

Chúng ta thấy các phép toán hàng trong phép khử ($E$ nhân $A$). Chẳng mấy chốc chúng ta sẽ thấy các cột trong $AA^{-1} = I$. "Bức tranh hàng-cột" có các tích vô hướng của các hàng với các cột. Các tích vô hướng là cách thông thường để nhân ma trận bằng tay: $mnp$ bước nhân/cộng riêng biệt.

| $AB = (m \times n)(n \times p) = (m \times p)$ | $mp$ tích vô hướng với $n$ bước mỗi cái | (2) |
|------------------------------------------------|---------------------------------------|-----|
|                                                |                                       |     |

# **Cách Thứ Tư: Cột Nhân Hàng (Columns Multiply Rows)**

Có một cách thứ tư để nhân ma trận. Không nhiều người nhận ra điều này quan trọng như thế nào. Tôi cảm thấy như một ảo thuật gia đang giải thích một mánh khóe. Các ảo thuật gia sẽ không làm điều đó nhưng các nhà toán học thì cố gắng. Cách thứ tư đã có trong các lần xuất bản trước của cuốn sách này, nhưng tôi đã không nhấn mạnh nó đủ.

**4. Nhân các cột từ 1 đến $n$ của $A$ với các hàng từ 1 đến $n$ của $B$. Cộng các ma trận đó lại.**

Cột 1 của $A$ nhân với hàng 1 của $B$. Các cột 2 và 3 nhân với các hàng 2 và 3. Sau đó cộng lại:

| $\begin{bmatrix} \text{cột 1} & \text{cột 2} & \text{cột 3} \end{bmatrix} \begin{bmatrix} \text{hàng 1} \\ \text{hàng 2} \\ \text{hàng 3} \end{bmatrix} = (\text{cột 1})(\text{hàng 1}) + (\text{cột 2})(\text{hàng 2}) + (\text{cột 3})(\text{hàng 3}).$ |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
(Note: corrected row matrices format in the equation based on context).

Nếu tôi nhân các ma trận $2 \times 2$ theo cách cột-hàng này, bạn sẽ thấy rằng $AB$ là đúng.

$$AB = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \begin{bmatrix} E & F \\ G & H \end{bmatrix} = \begin{bmatrix} aE + bG & aF + bH \\ cE + dG & cF + dH \end{bmatrix}.$$

| <b>Cộng các cột của $A$ nhân các hàng của $B$</b> | $AB = \begin{bmatrix} a \\ c \end{bmatrix} \begin{bmatrix} E & F \end{bmatrix} + \begin{bmatrix} b \\ d \end{bmatrix} \begin{bmatrix} G & H \end{bmatrix}$ | (3) |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|

Cột $k$ của $A$ nhân với hàng $k$ của $B$. Điều đó cho ra một ma trận (không chỉ là một con số). Sau đó bạn cộng các ma trận đó lại với $k = 1, 2, \dots, n$ để tạo ra $AB$.

Nếu $AB$ là ($m$ nhân $n$) ($n$ nhân $p$) thì sẽ có $n$ ma trận dạng $(\text{cột})(\text{hàng})$. Tất cả chúng đều có kích thước $m \times p$. Điều này sử dụng cùng $mnp$ bước giống như trong các tích vô hướng - nhưng theo một thứ tự mới.

### **Các Quy Luật cho Các Phép Toán Ma Trận (The Laws for Matrix Operations)**

Tôi có thể ghi chép lại sáu quy luật mà các ma trận tuân theo, trong khi nhấn mạnh một quy tắc mà chúng *không* tuân theo? Các ma trận có thể vuông hoặc chữ nhật, và các quy luật liên quan đến $A + B$ đều đơn giản và tất cả đều được tuân theo. Dưới đây là ba luật cộng:

| $A + B = B + A$             | (luật giao hoán - commutative law)  |
|-----------------------------|--------------------|
| $c(A + B) = cA + cB$        | (luật phân phối - distributive law) |
| $A + (B + C) = (A + B) + C$ | (luật kết hợp - associative law). |

Có ba luật nữa đúng cho phép nhân, nhưng $AB = BA$ không phải là một trong số chúng:

| $AB \neq BA$         | ("luật" giao hoán <i>thường bị phá vỡ</i> )               |
|----------------------|-----------------------------------------------------------------|
| $A(B + C) = AB + AC$ | (luật phân phối từ bên trái)                                |
| $(A + B)C = AC + BC$ | (luật phân phối từ bên phải)                               |
| $A(BC) = (AB)C$      | (luật kết hợp cho $ABC$ ) ( <i>không cần dấu ngoặc</i> ). |

Khi $A$ và $B$ không phải là ma trận vuông, $AB$ có kích thước khác với $BA$. Các ma trận này không thể bằng nhau - ngay cả khi cả hai phép nhân đều được cho phép. Đối với các ma trận vuông, hầu như bất kỳ ví dụ nào cũng cho thấy $AB$ khác với $BA$:

| $AB = \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}$ | nhưng | $BA = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ |
|-------------------------------------------------------------------------------------------------------------------------------------------------|-----|-------------------------------------------------------------------------------------------------------------------------------------------------|
|-------------------------------------------------------------------------------------------------------------------------------------------------|-----|-------------------------------------------------------------------------------------------------------------------------------------------------|

Đúng là $AI = IA$. Tất cả các ma trận vuông đều giao hoán với $I$ và cũng giao hoán với $cI$. Chỉ những ma trận $cI$ này mới giao hoán với tất cả các ma trận khác.

Luật $A(B + C) = AB + AC$ được chứng minh cho từng cột một. Bắt đầu với $A(b + c) = Ab + Ac$ đối với cột đầu tiên. Đó là chìa khóa của *mọi thứ - tính tuyến tính (linearity).* Không cần phải nói thêm.

*Luật $A(BC) = (AB)C$ có nghĩa là bạn có thể nhân $BC$ trước hoặc $AB$ trước.* Việc chứng minh trực tiếp thì hơi cồng kềnh (Bài toán 37) nhưng định luật này cực kỳ hữu ích. Chúng ta đã nhấn mạnh nó ở trên; nó là chìa khóa cho cách chúng ta nhân ma trận.

Hãy nhìn vào trường hợp đặc biệt khi $A = B = C =$ ma trận vuông. Khi đó ($A$ nhân $A^2$) bằng với ($A^2$ nhân $A$). Tích theo thứ tự nào cũng là $A^3$. Lũy thừa ma trận $A^p$ tuân theo cùng các quy tắc như các con số:

$$A^p = AAA \cdots A \text{ (} p \text{ thừa số)}$$

$$(A^p)(A^q) = A^{p+q}$$

$$(A^p)^q = A^{pq}.$$

Đó là những luật thông thường cho số mũ. $A^3$ nhân $A^4$ là $A^7$ (bảy thừa số). Nhưng lũy thừa bậc bốn của $A^3$ là $A^{12}$ (mười hai chữ $A$). Khi $p$ và $q$ bằng không hoặc âm, những quy tắc này vẫn đúng, miễn là $A$ có một "lũy thừa -1" - đó là *ma trận nghịch đảo (inverse matrix)* $A^{-1}$. Khi đó $A^0 = I$ là ma trận đơn vị, tương tự như $2^0 = 1$.

Đối với một số, $a^{-1}$ là $1/a$. Đối với một ma trận, ma trận nghịch đảo được viết là $A^{-1}$. (Nó *không* phải là $I/A$, ngoại trừ trong MATLAB.) Mọi con số đều có nghịch đảo ngoại trừ $a = 0$. Quyết định khi nào $A$ có ma trận nghịch đảo là một bài toán trung tâm trong đại số tuyến tính. Phần 2.5 sẽ bắt đầu đưa ra câu trả lời. Phần này là Bản Tuyên ngôn Nhân quyền (Bill of Rights) cho các ma trận, để nói khi nào $A$ và $B$ có thể được nhân với nhau và như thế nào.

## Ma Trận Khối và Phép Nhân Khối (Block Matrices and Block Multiplication)

Chúng ta phải nói thêm một điều nữa về ma trận. Chúng có thể được cắt thành các **khối (blocks)** (chính là các ma trận nhỏ hơn). Điều này thường xảy ra một cách tự nhiên. Đây là một ma trận $4 \times 6$ được chia thành các khối có kích thước $2 \times 2$ — trong ví dụ này mỗi khối chỉ là $I$:

$$\begin{array}{ll} \text{Ma trận } 4 \times 6 & \\ \text{Các khối } 2 \times 2 \text{ cho ra} & \\ \text{Ma trận khối } 2 \times 3 & \end{array} \quad A = \begin{bmatrix} 1 & 0 & 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 & 0 & 1 \\ 1 & 0 & 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 & 0 & 1 \end{bmatrix} = \begin{bmatrix} I & I & I \\ I & I & I \end{bmatrix}.$$

Nếu $B$ cũng có kích thước $4 \times 6$ và kích thước các khối khớp nhau, bạn có thể cộng $A + B$ từng khối một.

Bạn đã từng thấy ma trận khối trước đây rồi. Vectơ vế phải $b$ đã được đặt cạnh $A$ trong "ma trận bổ sung". Khi đó $\begin{bmatrix} A & b \end{bmatrix}$ có hai khối với các kích thước khác nhau. Nhân với một ma trận khử đã cho ra $\begin{bmatrix} EA & Eb \end{bmatrix}$. Không có vấn đề gì khi nhân các khối với các khối, khi hình dạng của chúng cho phép.

**Phép nhân khối (Block multiplication)** Nếu các khối của $A$ có thể nhân với các khối của $B$, thì phép nhân khối của $AB$ được cho phép. Những đường cắt giữa các cột của $A$ phải khớp với những đường cắt giữa các hàng của $B$.

$$\begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix} \begin{bmatrix} B_{11} \\ B_{21} \end{bmatrix} = \begin{bmatrix} A_{11}B_{11} + A_{12}B_{21} \\ A_{21}B_{11} + A_{22}B_{21} \end{bmatrix}. \quad (4)$$

Phương trình này giống hệt như khi các khối là những con số (tức là các khối $1 \times 1$). Chúng ta cẩn thận giữ các $A$ ở phía trước các $B$, vì $BA$ có thể khác nhau.

**Điểm chính yếu (Main point)** Khi các ma trận được tách thành các khối, thường thì sẽ đơn giản hơn để xem chúng hoạt động như thế nào. Ma trận khối của các $I$ ở trên rõ ràng hơn nhiều so với ma trận $A$ $4 \times 6$ ban đầu.

**Ví dụ 3 (Trường hợp đặc biệt quan trọng)** Đặt các khối của $A$ là $n$ cột của nó. Đặt các khối của $B$ là $n$ hàng của nó. Khi đó phép nhân khối $AB$ cộng các *cột nhân với hàng* lại:

| Các cột | $\begin{bmatrix}   & &   \\ a_1 & \cdots & a_n \\   & &   \end{bmatrix}$ | $\begin{bmatrix} -b_1- \\ \vdots \\ -b_n- \end{bmatrix}$ | $= \begin{bmatrix} a_1 b_1 + \cdots + a_n b_n \end{bmatrix}$ | (5) |
|---------|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-----|
|---------|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-----|
(Note: corrected the matrix formatting to match outer product sum).

Đây là Quy tắc 4 để nhân ma trận. Dưới đây là một ví dụ bằng số:

$$\begin{bmatrix} 3 & 4 \\ 1 & 5 \end{bmatrix} \begin{bmatrix} 3 & 2 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 3 \\ 1 \end{bmatrix} \begin{bmatrix} 3 & 2 \end{bmatrix} + \begin{bmatrix} 4 \\ 5 \end{bmatrix} \begin{bmatrix} 1 & 0 \end{bmatrix} = \begin{bmatrix} 9 & 6 \\ 3 & 2 \end{bmatrix} + \begin{bmatrix} 4 & 0 \\ 5 & 0 \end{bmatrix} = \begin{bmatrix} 13 & 6 \\ 8 & 2 \end{bmatrix}.$$
(Note: corrected the math from the original text which had a bunch of errors: [3 4; 1 5]*[3 2; 1 0] = [13 6; 8 2]. The intermediate matrices were totally messed up in the OCR).

*Tóm tắt* Cách thông thường, hàng nhân cột, cho ra bốn tích vô hướng (8 phép nhân). Cách mới, cột nhân hàng, cho ra hai ma trận đầy đủ (cùng 8 phép nhân đó).

**Ví dụ 4 (Phép khử theo khối - Elimination by blocks)** Giả sử cột đầu tiên của $A$ chứa 1, 3, 4. Để biến 3 và 4 thành 0 và 0, nhân hàng chứa phần tử xoay với 3 và 4 rồi trừ đi. Những phép toán hàng đó thực sự là phép nhân bởi các ma trận khử $E_{21}$ và $E_{31}$:

Làm từng cái một
$$E_{21} = \begin{bmatrix} 1 & 0 & 0 \\ -3 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
 và  $E_{31} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -4 & 0 & 1 \end{bmatrix}$.

"Ý tưởng khối" là thực hiện cả hai phép khử với một ma trận $E$. Ma trận đó dọn sạch toàn bộ cột đầu tiên của $A$ bên dưới phần tử xoay $a = 1$:

| <span></span>                                                             | <span></span> | <span></span>                                                       | <span></span> | <span></span>                                                            | <span></span> |
|---------------------------------------------------------------------------|---------------|---------------------------------------------------------------------|---------------|--------------------------------------------------------------------------|---------------|
| $E = \begin{bmatrix} 1 & 0 & 0 \\ -3 & 1 & 0 \\ -4 & 0 & 1 \end{bmatrix}$ | nhân với    | $\begin{bmatrix} 1 & x & x \\ 3 & x & x \\ 4 & x & x \end{bmatrix}$ | để cho ra       | $EA = \begin{bmatrix} 1 & x & x \\ 0 & y & y \\ 0 & z & z \end{bmatrix}$ |               |

Sử dụng ma trận nghịch đảo, một ma trận khối $E$ có thể thực hiện phép khử trên toàn bộ một cột (khối). Giả sử một ma trận có bốn khối $A, B, C, D$. Hãy xem cách $E$ khử $C$ theo khối:

| <b>Phép khử khối</b> | $\begin{bmatrix} I & \mathbf{0} \\ -CA^{-1} & I \end{bmatrix} \begin{bmatrix} A & B \\ C & D \end{bmatrix} = \begin{bmatrix} A & B \\ \mathbf{0} & D - CA^{-1}B \end{bmatrix}. \quad (6)$ |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Phép khử nhân hàng đầu tiên $\begin{bmatrix} A & B \end{bmatrix}$ với $CA^{-1}$ (trước đây là $c/a$). Nó trừ khỏi $C$ để nhận được một khối số không ở cột đầu tiên. Nó trừ khỏi $D$ để có được $S = D - CA^{-1}B$.

Đây là phép khử thông thường, từng cột một - nhưng sử dụng các khối. Khối phần tử xoay là $A$. Khối cuối cùng đó là $D - CA^{-1}B$, giống hệt như $d - cb/a$. Đây được gọi là *phần bù Schur (Schur complement).*

#### **• ÔN TẬP CÁC Ý TƯỞNG CHÍNH •**

- **1.** Phần tử $(i, j)$ của $AB$ là $(\text{hàng } i \text{ của } A) \cdot (\text{cột } j \text{ của } B)$.

- **2.** Một ma trận $m \times n$ nhân với một ma trận $n \times p$ sử dụng $mnp$ phép nhân riêng biệt.
- **3.** $A$ nhân $BC$ bằng $AB$ nhân $C$ (quan trọng một cách đáng ngạc nhiên).
- **4.** $AB$ cũng là tổng của $n$ ma trận này: (cột $j$ của $A$) nhân (hàng $j$ của $B$).
- **5.** Phép nhân khối được cho phép khi hình dạng các khối khớp nhau một cách chính xác.
- **6.** Phép khử khối tạo ra *phần bù Schur (Schur complement)* $D - CA^{-1}B$.

#### **• CÁC VÍ DỤ ĐÃ GIẢI (WORKED EXAMPLES) •**

**2.4 A** Một đồ thị hay một mạng (network) có $n$ nút (nodes). **Ma trận kề (adjacency matrix)** $S$ của nó là $n \times n$. Đây là một ma trận 0-1 với $s_{ij} = 1$ khi nút $i$ và nút $j$ được nối với nhau bởi một cạnh.

(Hình 2.9) Đồ thị vô hướng (Edges go both ways)

**Ma trận kề**
$$S = \begin{bmatrix} 0 & 1 & 1 & 0 \\ 1 & 0 & 1 & 1 \\ 1 & 1 & 0 & 1 \\ 0 & 1 & 1 & 0 \end{bmatrix}$$

Ma trận $S^2$ có một diễn giải hữu ích. $(S^2)_{ij}$ **đếm số lượng đường đi (walks) có độ dài 2** giữa nút $i$ và nút $j$. Giữa các nút 2 và 3, đồ thị có hai đường đi: đi qua 1 hoặc đi qua 4. Từ nút 1 đến nút 1, cũng có hai đường đi: 1-2-1 và 1-3-1.

$$S^2 = \begin{bmatrix} 2 & 1 & 2 & 1 \\ 1 & 2 & 3 & 1 \\ 1 & 1 & 1 & 2 \end{bmatrix} \quad S^3 = \begin{bmatrix} 2 & 5 & 5 & 5 \\ 5 & 5 & 4 & 5 \\ 5 & 5 & 4 & 5 \\ 2 & 5 & 5 & 5 \end{bmatrix}.$$
(Note: $S^2$ and $S^3$ from the original text are truncated/malformed. I'll translate as they are but mention it).

Bạn có thể tìm thấy 5 đường đi có độ dài 3 giữa nút 1 và 2 không?

Câu hỏi thực sự là tại sao $S^N$ lại đếm tất cả các đường đi $N$ bước giữa các cặp nút. Hãy bắt đầu với $S^2$ và nhìn vào phép nhân ma trận bằng các tích vô hướng:

| $(S^2)_{ij} = (\text{hàng } i \text{ của } S) \cdot (\text{cột } j \text{ của } S) = s_{i1}s_{1j} + s_{i2}s_{2j} + s_{i3}s_{3j} + s_{i4}s_{4j}$ | (7) |
|-------------------------------------------------------------------------------------------------------------------------------------------------|-----|
|-------------------------------------------------------------------------------------------------------------------------------------------------|-----|
(Note: corrected $s_{ij}$ to $s_{1j}$ and $s_{2j}$ to $s_{2j}$ based on context).

Nếu có một đường đi 2 bước $i \rightarrow 1 \rightarrow j$, phép nhân đầu tiên cho $s_{i1}s_{1j} = (1)(1) = 1$. Nếu $i \rightarrow 1 \rightarrow j$ *không* phải là một đường đi, thì hoặc là thiếu $i \rightarrow 1$ hoặc là thiếu $1 \rightarrow j$. Vậy nên phép nhân cho $s_{i1}s_{1j} = 0$ trong trường hợp đó.

$(S^2)_{ij}$ đang cộng các số 1 cho tất cả các đường đi 2 bước $i \rightarrow k \rightarrow j$. Nên nó đếm những đường đi đó. Theo cùng một cách $S^N$ sẽ đếm các đường đi $N$ bước, bởi vì chúng là các đường đi $(N-1)$ bước từ $i$ đến $k$ tiếp theo là một bước từ $k$ đến $j$. Phép nhân ma trận hoàn toàn phù hợp để đếm các đường đi trên một đồ thị - các kênh liên lạc giữa các nhân viên trong một công ty.

**2.4 B** Đối với các ma trận này, khi nào thì $AB = BA$? Khi nào thì $BC = CB$? Khi nào thì $A$ nhân $BC$ bằng $AB$ nhân $C$? Hãy đưa ra các điều kiện cho các phần tử $p, q, r, z$ của chúng:

$$A = \begin{bmatrix} p & 0 \\ q & r \end{bmatrix} \quad B = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \quad C = \begin{bmatrix} 0 & z \\ 0 & 0 \end{bmatrix}.$$

Nếu $p, q, r, 1, z$ là các khối $4 \times 4$ thay vì các con số, các câu trả lời có thay đổi không?

**Lời giải** Trước hết, $A$ nhân $BC$ *luôn luôn* bằng $AB$ nhân $C$. Không cần dấu ngoặc đơn trong $A(BC) = (AB)C = ABC$. Nhưng chúng ta phải giữ các ma trận theo thứ tự này:

| Thông thường $AB \neq BA$ | $AB = \begin{bmatrix} p & p \\ q & q+r \end{bmatrix}$ | $BA = \begin{bmatrix} p+q & r \\ q & r \end{bmatrix}$ |
|----------------------|-------------------------------------------------------|-------------------------------------------------------|
|----------------------|-------------------------------------------------------|-------------------------------------------------------|

| Do tình cờ $BC = CB$ | $BC = \begin{bmatrix} 0 & z \\ 0 & 0 \end{bmatrix}$ | $CB = \begin{bmatrix} 0 & z \\ 0 & 0 \end{bmatrix}$ |
|---------------------|-----------------------------------------------------|-----------------------------------------------------|
|---------------------|-----------------------------------------------------|-----------------------------------------------------|

$B$ và $C$ tình cờ giao hoán với nhau. Một phần của lời giải thích là đường chéo của $B$ là $I$, nó giao hoán với tất cả các ma trận $2 \times 2$. Khi $p, q, r, z$ là các khối $4 \times 4$ và số 1 đổi thành $I$, tất cả các tích này vẫn đúng. Vì vậy các câu trả lời là như nhau.

# **Bài Tập 2.4 (Problem Set 2.4)**

#### **Các bài toán 1-16 liên quan đến các quy luật của phép nhân ma trận.**

**1** $A$ là $3 \times 5$, $B$ là $5 \times 3$, $C$ là $5 \times 1$, và $D$ là $3 \times 1$. *Tất cả các phần tử đều là 1.* Phép toán ma trận nào trong số này được phép, và kết quả là gì?

| $BA$ | $AB$ | $ABD$ | $DC$ | $A(B+C)$. |
|------|------|-------|------|------------|
|      |      |       |      |            |

**2** Bạn nhân những hàng hay cột hay ma trận nào để tìm:
  - (a) cột thứ hai của $AB$? 
  - (b) hàng thứ nhất của $AB$?
  - (c) phần tử ở hàng 3, cột 5 của $AB$? 
  - (d) phần tử ở hàng 1, cột 1 của $CDE$?

**3** Cộng $AB$ với $AC$ và so sánh với $A(B+C)$:

| $A = \begin{bmatrix} 1 & 5 \\ 2 & 3 \end{bmatrix}$ | và | $B = \begin{bmatrix} 0 & 2 \\ 0 & 1 \end{bmatrix}$ | và | $C = \begin{bmatrix} 3 & 1 \\ 0 & 0 \end{bmatrix}$ |
|----------------------------------------------------|-----|----------------------------------------------------|-----|----------------------------------------------------|
|----------------------------------------------------|-----|----------------------------------------------------|-----|----------------------------------------------------|

**5** Tính $A^2$ và $A^3$. Đưa ra dự đoán cho $A^5$ và $A^n$:

| $A = \begin{bmatrix} 1 & b \\ 0 & 1 \end{bmatrix}$ | và | $A = \begin{bmatrix} 2 & 2 \\ 0 & 0 \end{bmatrix}$ |
|----------------------------------------------------|-----|----------------------------------------------------|
|----------------------------------------------------|-----|----------------------------------------------------|

**6** Chứng minh rằng $(A+B)^2$ khác với $A^2 + 2AB + B^2$, khi

| $A = \begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix}$ | và | $B = \begin{bmatrix} 1 & 0 \\ 3 & 0 \end{bmatrix}$ |
|----------------------------------------------------|-----|----------------------------------------------------|
|----------------------------------------------------|-----|----------------------------------------------------|

Viết ra quy tắc đúng cho $(A+B)(A+B) = A^2 + \dots + B^2$.

**7** Đúng hay sai. Đưa ra một ví dụ cụ thể khi nó sai:
  - (a) Nếu các cột 1 và 3 của $B$ giống nhau, thì các cột 1 và 3 của $AB$ cũng vậy.
  - (b) Nếu các hàng 1 và 3 của $B$ giống nhau, thì các hàng 1 và 3 của $AB$ cũng vậy.
  - (c) Nếu các hàng 1 và 3 của $A$ giống nhau, thì các hàng 1 và 3 của $ABC$ cũng vậy.
  - (d) $(AB)^2 = A^2 B^2$.

**8** Mỗi hàng của $DA$ và $EA$ liên hệ với các hàng của $A$ như thế nào, khi

| $D = \begin{bmatrix} 3 & 0 \\ 0 & 5 \end{bmatrix}$ | và | $E = \begin{bmatrix} 0 & 1 \\ 0 & 1 \end{bmatrix}$ | và | $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ ? |
|----------------------------------------------------|-----|----------------------------------------------------|-----|------------------------------------------------------|
|----------------------------------------------------|-----|----------------------------------------------------|-----|------------------------------------------------------|

Mỗi cột của $AD$ và $AE$ liên hệ với các cột của $A$ như thế nào?

**9** Hàng 1 của $A$ được cộng vào hàng 2. Điều này cho ra $EA$ ở dưới. Sau đó cột 1 của $EA$ được cộng vào cột 2 để tạo ra $(EA)F$:

$$EA = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} a & b \\ c & d \end{bmatrix} = \begin{bmatrix} a & b \\ a+c & b+d \end{bmatrix}$$
và  $$(EA)F = (EA) \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} a & a+b \\ a+c & a+c+b+d \end{bmatrix}.$$

  - (a) Thực hiện các bước đó theo thứ tự ngược lại. Đầu tiên cộng cột 1 của $A$ vào cột 2 bằng $AF$, sau đó cộng hàng 1 của $AF$ vào hàng 2 bằng $E(AF)$.
  - (b) So sánh với $(EA)F$. Luật nào được tuân theo bởi phép nhân ma trận?

**10** Hàng 1 của $A$ lại được cộng vào hàng 2 để tạo ra $EA$. Sau đó $F$ cộng hàng 2 của $EA$ vào hàng 1. Kết quả là $F(EA)$:

$$F(EA) = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} a & b \\ a+c & b+d \end{bmatrix} = \begin{bmatrix} 2a+c & 2b+d \\ a+c & b+d \end{bmatrix}.$$

  - (a) Thực hiện các bước đó theo thứ tự ngược lại: đầu tiên cộng hàng 2 vào hàng 1 bằng $FA$, sau đó cộng hàng 1 của $FA$ vào hàng 2.
  - (b) Luật nào được tuân theo hoặc không được tuân theo bởi phép nhân ma trận?

**11** Sự thật này vẫn làm tôi ngạc nhiên. Nếu bạn thực hiện một phép toán hàng trên $A$ và sau đó là một phép toán cột, kết quả cũng giống như thể bạn đã thực hiện phép toán cột trước. (Hãy thử xem.) Tại sao điều này lại đúng?

**12** (Ma trận $3 \times 3$) Chọn ma trận $B$ duy nhất sao cho với mọi ma trận $A$:
  - (a) $BA = 4A$
  - (b) $BA = 4B$
  - (c) $BA$ có hàng 1 và 3 của $A$ bị đảo ngược và hàng 2 không đổi
  - (d) Tất cả các hàng của $BA$ đều giống như hàng 1 của $A$.

**13** Giả sử $AB = BA$ và $AC = CA$ đối với hai ma trận cụ thể $B$ và $C$ này:

| $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ | giao hoán với $B = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ | và $C = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ . |
|----------------------------------------------------|------------------------------------------------------------------|----------------------------------------------------------|
|----------------------------------------------------|------------------------------------------------------------------|----------------------------------------------------------|

Chứng minh rằng $a = d$ và $b = c = 0$. Khi đó $A$ là một bội số của $I$. Các ma trận duy nhất giao hoán với $B$ và $C$ và tất cả các ma trận $2 \times 2$ khác là $A = \text{bội số của } I$.

**14** Những ma trận nào sau đây được đảm bảo là bằng $(A-B)^2$: $A^2 - B^2$, $(B-A)^2$, $A^2 - 2AB + B^2$, $A(A-B) - B(A-B)$, $A^2 - AB - BA + B^2$?

**15** Đúng hay sai:
  - (a) Nếu $A^2$ được định nghĩa thì $A$ nhất thiết phải là ma trận vuông.
  - (b) Nếu $AB$ và $BA$ được định nghĩa thì $A$ và $B$ là ma trận vuông.
  - (c) Nếu $AB$ và $BA$ được định nghĩa thì $AB$ và $BA$ là ma trận vuông.
  - (d) Nếu $AB = B$ thì $A = I$.

**16** Nếu $A$ có kích thước $m \times n$, có bao nhiêu phép nhân riêng biệt tham gia khi:
  - (a) $A$ nhân với một vectơ $x$ có $n$ thành phần?
  - (b) $A$ nhân với một ma trận $B$ $n \times p$?
  - (c) $A$ nhân với chính nó để tạo ra $A^2$? Ở đây $m = n$.

**17** Với $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ và $B = \begin{bmatrix} e & f \\ g & h \end{bmatrix}$, hãy tính các câu trả lời này *và không tính thêm gì khác:*
  - (a) cột 2 của $AB$
  - (b) hàng 2 của $AB$
  - (c) hàng 2 của $AA = A^2$
  - (d) hàng 2 của $AAA = A^3$.

**Các Bài toán 18-20 sử dụng $a_{ij}$ cho phần tử ở hàng $i$, cột $j$ của $A$.**

**18** Viết ra ma trận $A$ $3 \times 3$ có các phần tử là:
  - (a) $a_{ij} = \text{giá trị nhỏ nhất của } i \text{ và } j$
  - (b) $a_{ij} = (-1)^{i+j}$
  - (c) $a_{ij} = i/j$.

**19** Bạn sẽ dùng những từ nào để mô tả từng lớp ma trận này? Hãy đưa ra một ví dụ $3 \times 3$ trong mỗi lớp. Ma trận nào thuộc về cả bốn lớp?
  - (a) $a_{ij} = 0$ nếu $i \neq j$
  - (b) $a_{ij} = 0$ nếu $i < j$
  - (c) $a_{ij} = a_{ji}$
  - (d) $a_{ij} = a_{ij}$.

**20** Các phần tử của $A$ là $a_{ij}$. Giả sử rằng các số không không xuất hiện, thì là gì:
  - (a) phần tử xoay đầu tiên?

  - (b) số nhân $l_{31}$ của hàng 1 bị trừ khỏi hàng 3?
  - (c) phần tử mới thay thế $a_{32}$ sau phép trừ đó?
  - (d) phần tử xoay thứ hai?
#### **Các Bài toán 21-24 liên quan đến các lũy thừa của $A$.**

**21** Tính $A^2, A^3, A^4$ và cả $Av, A^2v, A^3v, A^4v$ đối với

$$A = \begin{bmatrix} 0 & 2 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 2 \\ 0 & 0 & 0 & 0 \end{bmatrix} \quad \text{và} \quad v = \begin{bmatrix} x \\ y \\ z \\ t \end{bmatrix}.$$

**22** Bằng cách thử và sai (trial and error) hãy tìm các ma trận $2 \times 2$ thực khác không sao cho $A^2 = -I$, $BC = 0$, $DE = -ED$ (không cho phép $DE = 0$).

**23** (a) Tìm một ma trận khác không $A$ sao cho $A^2 = 0$.
  - (b) Tìm một ma trận có $A^2 \neq 0$ nhưng $A^3 = 0$.

**24** Bằng cách thử nghiệm với $n = 2$ và $n = 3$, hãy dự đoán $A^n$ cho các ma trận này:

| $A_1 = \begin{bmatrix} 2 & 1 \\ 0 & 1 \end{bmatrix}$ | và | $A_2 = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$ | và | $A_3 = \begin{bmatrix} a & b \\ 0 & 0 \end{bmatrix}$ |
|------------------------------------------------------|-----|------------------------------------------------------|-----|------------------------------------------------------|
|------------------------------------------------------|-----|------------------------------------------------------|-----|------------------------------------------------------|

**Các bài toán 25-31 sử dụng** phép nhân cột-hàng và phép nhân khối.

**25** Nhân $A$ với $I$ sử dụng các cột của $A$ ($3 \times 3$) nhân với các hàng của $I$.

**26** Nhân $AB$ sử dụng cột nhân hàng:

| $AB = \begin{bmatrix} 1 & 0 \\ 2 & 4 \\ 2 & 1 \end{bmatrix} \begin{bmatrix} 3 & 3 & 0 \\ 1 & 2 & 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix} \begin{bmatrix} 3 & 3 & 0 \end{bmatrix} + \underline{\underline{\quad}} = \underline{\underline{\quad}}$ . |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**27** Chứng minh rằng tích của các ma trận tam giác trên luôn là ma trận tam giác trên:

| $AB = \begin{bmatrix} x & x & x \\ 0 & x & x \\ 0 & 0 & x \end{bmatrix} \begin{bmatrix} x & x & x \\ 0 & x & x \\ 0 & 0 & x \end{bmatrix} = \begin{bmatrix} * & * & * \\ 0 & * & * \\ 0 & 0 & * \end{bmatrix}$ |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

*Chứng minh bằng cách sử dụng tích vô hướng (Hàng nhân cột)* (Hàng 2 của $A$) $\cdot$ (cột 1 của $B$) $= 0$. Những tích vô hướng nào khác cho ra các số không **?**

*Chứng minh bằng cách sử dụng các ma trận đầy đủ (Cột nhân hàng)* Vẽ các $x$ và $0$ trong (cột 2 của $A$) nhân (hàng 2 của $B$). Cũng chỉ ra (cột 3 của $A$) nhân (hàng 3 của $B$).

**28** Vẽ các đường cắt trong $A$ ($2 \times 3$) và $B$ ($3 \times 4$) và $AB$ để cho thấy mỗi một trong bốn quy tắc nhân thực sự là một phép nhân khối như thế nào:
  - (1) Ma trận $A$ nhân các cột của $B$.
  - (2) Các hàng của $A$ nhân ma trận $B$.
  - (3) Các hàng của $A$ nhân các cột của $B$.
  - (4) Các cột của $A$ nhân các hàng của $B$.
  
**Các cột của** $AB$, **Các hàng của** $AB$, **Tích trong (Inner products)** (các số trong $AB$), **Tích ngoài (Outer products)** (các ma trận cộng lại thành $AB$).

**29** Những ma trận $E_{21}$ và $E_{31}$ nào tạo ra các số không ở các vị trí $(2, 1)$ và $(3, 1)$ của $E_{21}A$ và $E_{31}A$?

$$A = \begin{bmatrix} 2 & 1 & 0 \\ -2 & 0 & 1 \\ 8 & 5 & 3 \end{bmatrix}.$$

Tìm ma trận duy nhất $E = E_{31}E_{21}$ tạo ra cả hai số không cùng một lúc. Nhân $EA$.

**30** Phép nhân khối nói rằng cột 1 bị khử bởi

$$E_A = \begin{bmatrix} 1 & 0 \\ -c/a & I \end{bmatrix} \begin{bmatrix} a & b \\ c & D \end{bmatrix} = \begin{bmatrix} a & b \\ 0 & D - cb/a \end{bmatrix}.$$

Trong Bài toán 29, những con số nào đi vào $c$ và $D$ và $D - cb/a$ là gì?

**31** Với $i^2 = -1$, tích của $(A + iB)$ và $(x + iy)$ là $Ax + iBx + iAy - By$. Sử dụng các khối để tách phần thực không có $i$ ra khỏi phần ảo có nhân với $i$:

| $\begin{bmatrix} A & -B \\ B & A \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} Ax - By \\ Bx + Ay \end{bmatrix}$ | phần thực (real part)      |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------|
|                                                                                                                                       | phần ảo (imaginary part) |

**32** *(Rất quan trọng)* Giả sử bạn giải $Ax = b$ cho ba vế phải đặc biệt $b$:

| $Ax_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$ | và | $Ax_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}$ | và | $Ax_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$ |
|----------------------------------------------------|-----|----------------------------------------------------|-----|----------------------------------------------------|
|----------------------------------------------------|-----|----------------------------------------------------|-----|----------------------------------------------------|

Nếu ba nghiệm $x_1, x_2, x_3$ là các cột của một ma trận $X$, thì $A$ nhân $X$ là gì?

**33** Nếu ba nghiệm trong Câu hỏi 32 là $x_1 = (1, 1, 1)$ và $x_2 = (0, 1, 1)$ và $x_3 = (0, 0, 1)$, hãy giải $Ax = b$ khi $b = (3, 5, 8)$.
Bài toán thử thách: $A$ là gì?

**34** Tìm tất cả các ma trận $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ thỏa mãn $A \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} A$.

**35** Giả sử một "đồ thị vòng tròn (circle graph)" có 4 nút được nối với nhau (theo cả hai hướng) bởi các cạnh tạo thành một vòng tròn. Ma trận kề $S$ của nó từ Ví dụ Đã giải 2.4 A là gì? $S^2$ là gì? Tìm tất cả các đường đi 2 bước được dự đoán bởi $S^2$.

### **Các Bài toán Thử thách (Challenge Problems)**

**36 Câu hỏi thực tế (Practical question)** Giả sử $A$ là $m \times n$, $B$ là $n \times p$, và $C$ là $p \times q$. Khi đó số lượng phép nhân là $mnp$ cho $AB$ cộng với $mpq$ cho $(AB)C$. Cùng một ma trận nhận được từ $A$ nhân với $BC$ với $mnq + npq$ phép nhân riêng biệt. Chú ý $npq$ là cho $BC$.
  - (a) Nếu $A$ là $2 \times 4$, $B$ là $4 \times 7$, và $C$ là $7 \times 10$, bạn thích $(AB)C$ hay $A(BC)$ hơn?
  - (b) Với các vectơ $N$ thành phần, bạn sẽ chọn $(u^Tv)w^T$ hay $u^T(vw^T)$?
  - (c) Chia cho $mnpq$ để chứng minh rằng $(AB)C$ nhanh hơn khi $n^{-1} + q^{-1} < m^{-1} + p^{-1}$.

**37** Để chứng minh rằng $(AB)C = A(BC)$, sử dụng các vectơ cột $b_1, \dots, b_p$ của $B$. Đầu tiên giả sử rằng $C$ chỉ có một cột $c$ với các phần tử $c_1, \dots, c_p$: $AB$ có các cột $Ab_1, \dots, Ab_p$ và khi đó $(AB)c$ bằng $c_1Ab_1 + \dots + c_pAb_p$. $Bc$ có một cột $c_1b_1 + \dots + c_pb_p$ và khi đó $A(Bc)$ bằng $A(c_1b_1 + \dots + c_pb_p)$. *Tính tuyến tính* mang lại sự bằng nhau của hai tổng đó. Điều này chứng minh $(AB)c = A(Bc)$. Điều tương tự cũng đúng cho tất cả các cột khác của $C$. Do đó $(AB)C = A(BC)$.

Áp dụng cho các nghịch đảo: Nếu $BA = I$ và $AC = I$, chứng minh rằng nghịch đảo trái $B$ bằng nghịch đảo phải $C$.

**38** (a) Giả sử $A$ có các hàng $a_1^T, \dots, a_m^T$. Tại sao $A^TA$ lại bằng $a_1a_1^T + \dots + a_ma_m^T$?
  - (b) Nếu $C$ là một ma trận đường chéo với $c_1, \dots, c_m$ trên đường chéo của nó, tìm một tổng tương tự của các cột nhân các hàng đối với $A^TCA$. Đầu tiên hãy làm một ví dụ với $m = n = 2$.

# **2.5 Ma Trận Nghịch Đảo (Inverse Matrices)**

Nếu ma trận vuông $A$ có một nghịch đảo, thì cả $A^{-1}A = I$ và $AA^{-1} = I$. *Thuật toán* để kiểm tra tính khả nghịch (invertibility) là phép khử: $A$ phải có $n$ phần tử xoay (khác không). Phép kiểm tra *đại số* cho tính khả nghịch là định thức của $A$: $\det A$ không được bằng không. *Phương trình* kiểm tra tính khả nghịch là $Ax = 0$: **$x = 0$ phải là nghiệm duy nhất.** Nếu $A$ và $B$ (cùng kích thước) là khả nghịch thì $AB$ cũng vậy: $(AB)^{-1} = B^{-1}A^{-1}$. Phương trình $AA^{-1} = I$ là $n$ phương trình cho $n$ cột của $A^{-1}$. Phương pháp Gauss-Jordan khử $\begin{bmatrix} A & I \end{bmatrix}$ thành $\begin{bmatrix} I & A^{-1} \end{bmatrix}$. Trang cuối của cuốn sách đưa ra 14 điều kiện tương đương để một ma trận vuông $A$ khả nghịch.

Giả sử $A$ là một ma trận vuông. Chúng ta tìm kiếm một *"ma trận nghịch đảo" (inverse matrix)* $A^{-1}$ có cùng kích thước, sao cho $A^{-1}$ *nhân $A$ bằng $I$.* Bất cứ điều gì $A$ làm, $A^{-1}$ sẽ hoàn tác nó (undoes). Tích của chúng là ma trận đơn vị - nó không làm gì đối với một vectơ, nên $A^{-1}Ax = x$. *Nhưng $A^{-1}$ có thể không tồn tại.*

Điều mà một ma trận thường làm nhất là nhân một vectơ $x$. Nhân $Ax = b$ với $A^{-1}$ cho ra $A^{-1}Ax = A^{-1}b$. *Đó là $x = A^{-1}b$.* Tích $A^{-1}A$ giống như nhân với một số rồi chia cho số đó. Một con số có nghịch đảo nếu nó khác không - các ma trận phức tạp hơn và thú vị hơn. Ma trận $A^{-1}$ được gọi là *"A nghịch đảo (A inverse)."*

**ĐỊNH NGHĨA** Ma trận $A$ được gọi là *khả nghịch (invertible)* nếu tồn tại một ma trận $A^{-1}$ "nghịch đảo" $A$:

| <b>Nghịch đảo hai phía</b> | $A^{-1}A = I$ | và | $AA^{-1} = I.$ | (1) |
|--------------------------|---------------|-----|----------------|-----|
|                          |               |     |                |     |

*Không phải tất cả các ma trận đều có nghịch đảo.* Đây là câu hỏi đầu tiên chúng ta đặt ra về một ma trận vuông: $A$ có khả nghịch không? Chúng ta không có ý định tính toán ngay $A^{-1}$. Trong đa số các bài toán, chúng ta không bao giờ tính toán nó! Dưới đây là sáu "ghi chú" về $A^{-1}$.

**Ghi chú 1** *Nghịch đảo tồn tại nếu và chỉ nếu phép khử sinh ra $n$ phần tử xoay* (được phép hoán đổi hàng). Phép khử giải $Ax = b$ mà không cần sử dụng rõ ràng ma trận $A^{-1}$.

**Ghi chú 2** Ma trận $A$ không thể có hai nghịch đảo khác nhau. Giả sử $BA = I$ và cũng có $AC = I$. Khi đó $B = C$, theo "chứng minh bằng dấu ngoặc đơn" này:

| $B(AC) = (BA)C$ | cho ra | $BI = IC$ | hay | $B = C$. | (2) |
|-----------------|-------|-----------|----|-----------|-----|
|-----------------|-------|-----------|----|-----------|-----|

Điều này chứng tỏ rằng một *nghịch đảo trái (left-inverse)* $B$ (nhân từ bên trái) và một *nghịch đảo phải (right-inverse)* $C$ (nhân $A$ từ bên phải để cho ra $AC = I$) phải là *cùng một ma trận.*

**Ghi chú 3** Nếu $A$ khả nghịch, nghiệm duy nhất của $Ax = b$ là $x = A^{-1}b$:

| Nhân | $Ax = b$ | với | $A^{-1}$ | Khi đó | $x = A^{-1}Ax = A^{-1}b$ |
|----------|----------|------|----------|--------|--------------------------|
|          |          |      |          |        |                          |

**Ghi chú 4** (Quan trọng) *Giả sử có một vectơ $x$ khác không sao cho $Ax = 0$. Khi đó $A$ không thể có nghịch đảo.* Không có ma trận nào có thể mang số 0 trở lại thành $x$.

Nếu $A$ khả nghịch, thì $Ax = 0$ chỉ có thể có nghiệm không (zero solution) $x = A^{-1}0 = 0$.

**Ghi chú 5** Một ma trận $2 \times 2$ khả nghịch nếu và chỉ nếu $ad - bc$ khác không:

$$2 \times 2 \text{ Nghịch đảo: } \begin{bmatrix} a & b \\ c & d \end{bmatrix}^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}. \quad (3)$$

Con số $ad - bc$ này là *định thức (determinant)* của $A$. Một ma trận khả nghịch nếu định thức của nó khác không (Chương 5). Bài kiểm tra cho $n$ phần tử xoay thường được quyết định trước khi định thức xuất hiện.

**Ghi chú 6** Một ma trận đường chéo có một nghịch đảo với điều kiện không có phần tử đường chéo nào bằng không:

$$\text{Nếu } A = \begin{bmatrix} d_1 & & \\ & \ddots & \\ & & d_n \end{bmatrix} \text{ thì } A^{-1} = \begin{bmatrix} 1/d_1 & & \\ & \ddots & \\ & & 1/d_n \end{bmatrix}.$$

**Ví dụ 1** Ma trận $2 \times 2$ $A = \begin{bmatrix} 1 & 2 \\ 1 & 2 \end{bmatrix}$ không khả nghịch. Nó thất bại ở bài kiểm tra trong Ghi chú 5, bởi vì $ad - bc$ bằng $2 - 2 = 0$. Nó thất bại ở bài kiểm tra trong Ghi chú 3, bởi vì $Ax = 0$ khi $x = (2, -1)$. Nó thất bại trong việc có hai phần tử xoay như yêu cầu của Ghi chú 1.

Phép khử biến đổi hàng thứ hai của ma trận $A$ này thành một hàng toàn số không.

### Nghịch đảo của Một Tích $AB$

Đối với hai số khác không $a$ và $b$, tổng $a + b$ có thể khả nghịch hoặc không khả nghịch. Các số $a = 3$ và $b = -3$ có nghịch đảo là $\frac{1}{3}$ và $-\frac{1}{3}$. Tổng của chúng $a + b = 0$ không có nghịch đảo. Nhưng tích $ab = -9$ có một nghịch đảo, đó là $\frac{1}{3}$ nhân với $-\frac{1}{3}$.

Đối với hai ma trận $A$ và $B$, tình huống tương tự. Rất khó để nói nhiều về tính khả nghịch của $A + B$. Nhưng *tích $AB$* có một nghịch đảo, nếu và chỉ nếu cả hai yếu tố $A$ và $B$ đều khả nghịch một cách riêng biệt (và cùng kích thước). Điểm quan trọng là $A^{-1}$ và $B^{-1}$ đi theo *thứ tự ngược lại*:

Nếu $A$ và $B$ khả nghịch thì $AB$ cũng vậy. Nghịch đảo của một tích $AB$ là

$$(AB)^{-1} = B^{-1}A^{-1}. \quad (4)$$

Để thấy tại sao thứ tự bị đảo ngược, hãy nhân $AB$ với $B^{-1}A^{-1}$. Ở bên trong đó là $BB^{-1} = I$:

$$\text{Nghịch đảo của } AB \quad (AB)(B^{-1}A^{-1}) = AIA^{-1} = AA^{-1} = I.$$

Chúng ta đã di chuyển các dấu ngoặc đơn để nhân $BB^{-1}$ trước. Tương tự $B^{-1}A^{-1}$ nhân với $AB$ bằng $I$.

$B^{-1}A^{-1}$ minh họa một quy tắc cơ bản của toán học: Các nghịch đảo đi theo thứ tự ngược lại. Đây cũng là một ý thức thông thường: Nếu bạn đi tất rồi mới đi giày, thì thứ đầu tiên phải cởi ra là \_\_. Cùng một thứ tự ngược lại đó áp dụng cho ba hoặc nhiều ma trận:

| Thứ tự ngược | $(ABC)^{-1} = C^{-1}B^{-1}A^{-1}$ | (5) |
|---------------|-----------------------------------|-----|
|               |                                   |     |

**Ví dụ 2** *Nghịch đảo của một ma trận khử.* Nếu $E$ trừ 5 lần hàng 1 khỏi hàng 2, thì $E^{-1}$ *cộng* 5 lần hàng 1 vào hàng 2:

$$E = \begin{bmatrix} 1 & 0 & 0 \\ -5 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \text{ và } E^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 5 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}.$$

Nhân $EE^{-1}$ để nhận được ma trận đơn vị $I$. Cũng nhân $E^{-1}E$ để nhận được $I$. Chúng ta đang cộng và trừ cùng một lượng 5 lần hàng 1. Nếu $AC = I$ thì tự động $CA = I$.

*Đối với các ma trận vuông, một nghịch đảo ở một phía tự động là một nghịch đảo ở phía bên kia.*

**Ví dụ 3** Giả sử $F$ trừ 4 lần hàng 2 khỏi hàng 3, và $F^{-1}$ cộng nó lại:

| $F = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -4 & 1 \end{bmatrix}$ | và | $F^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 4 & 1 \end{bmatrix}$ |
|--------------------------------------------------------------------------|-----|------------------------------------------------------------------------------|
|--------------------------------------------------------------------------|-----|------------------------------------------------------------------------------|

Bây giờ nhân $F$ với ma trận $E$ trong Ví dụ 2 để tìm $FE$. Cũng nhân $E^{-1}$ với $F^{-1}$ để tìm $(FE)^{-1}$. Hãy chú ý đến thứ tự $FE$ và $E^{-1}F^{-1}$!

$$FE = \begin{bmatrix} 1 & 0 & 0 \\ -5 & 1 & 0 \\ \mathbf{20} & -4 & 1 \end{bmatrix} \text{ được nghịch đảo bởi } E^{-1}F^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ \mathbf{5} & 1 & 0 \\ \mathbf{0} & 4 & 1 \end{bmatrix}. \quad (6)$$

Kết quả rất đẹp và chính xác. Tích $FE$ chứa "20" nhưng nghịch đảo của nó thì không. $E$ trừ 5 lần hàng 1 khỏi hàng 2. Sau đó $F$ trừ 4 lần hàng 2 *mới* (đã bị thay đổi bởi hàng 1) khỏi hàng 3. *Theo thứ tự $FE$ này, hàng 3 cảm nhận một tác động từ hàng 1.*

Theo thứ tự $E^{-1}F^{-1}$, tác động đó không xảy ra. Đầu tiên $F^{-1}$ cộng 4 lần hàng 2 vào hàng 3. Sau đó, $E^{-1}$ cộng 5 lần hàng 1 vào hàng 2. Không có 20, vì hàng 3 không thay đổi lại nữa. *Theo thứ tự $E^{-1}F^{-1}$ này, hàng 3 không cảm nhận tác động nào từ hàng 1.*

Đây là lý do tại sao phần tiếp theo chọn $A = LU$, để đi ngược lại từ ma trận tam giác $U$ về $A$. Các số nhân rơi vào đúng vị trí một cách hoàn hảo trong ma trận tam giác dưới $L$.

Theo thứ tự khử, $F$ đi sau $E$. Theo thứ tự ngược lại, $E^{-1}$ đi sau $F^{-1}$. $E^{-1}F^{-1}$ *rất nhanh. Các số nhân 5, 4 rơi vào đúng vị trí dưới đường chéo chứa các số 1.*

## Tính $A^{-1}$ bằng phương pháp Khử Gauss-Jordan

Tôi đã ám chỉ rằng $A^{-1}$ có thể không thực sự cần thiết một cách rõ ràng. Phương trình $Ax = b$ được giải bằng $x = A^{-1}b$. Nhưng không cần thiết hay hiệu quả để tính $A^{-1}$ và nhân nó với $b$. *Phép khử đi trực tiếp đến $x$.* Và phép khử cũng là cách để tính $A^{-1}$, như chúng ta sẽ chỉ ra bây giờ. Ý tưởng Gauss-Jordan là giải $AA^{-1} = I$, *tìm từng cột của $A^{-1}$.*

$A$ nhân cột đầu tiên của $A^{-1}$ (gọi là $x_1$) để cho ra cột đầu tiên của $I$ (gọi là $e_1$). Đây là phương trình $Ax_1 = e_1 = (1, 0, 0)$ của chúng ta. Sẽ có thêm hai phương trình nữa. *Mỗi cột $x_1, x_2, x_3$ của $A^{-1}$ được nhân với $A$ để tạo ra một cột của $I$:*

$$3 \text{ cột của } A^{-1} \quad AA^{-1} = A\begin{bmatrix} x_1 & x_2 & x_3 \end{bmatrix} = \begin{bmatrix} e_1 & e_2 & e_3 \end{bmatrix} = I. \quad (7)$$

Để nghịch đảo một ma trận $3 \times 3$ $A$, chúng ta phải giải ba hệ phương trình: $Ax_1 = e_1$ và $Ax_2 = e_2 = (0, 1, 0)$ và $Ax_3 = e_3 = (0, 0, 1)$. Phương pháp Gauss-Jordan tìm $A^{-1}$ theo cách này.

**Phương pháp Gauss-Jordan tính $A^{-1}$ bằng cách giải tất cả $n$ phương trình cùng một lúc.** Thông thường "ma trận bổ sung" $\begin{bmatrix} A & b \end{bmatrix}$ có một cột bổ sung $b$. Bây giờ chúng ta có ba vế phải $e_1, e_2, e_3$ (khi $A$ là $3 \times 3$). Chúng là các cột của $I$, vậy nên ma trận bổ sung thực chất là ma trận khối $\begin{bmatrix} A & I \end{bmatrix}$. Tôi nhân cơ hội này để nghịch đảo ma trận yêu thích của tôi là $K$, với các số 2 trên đường chéo chính và các số $-1$ kề cạnh các số 2:

$$\begin{aligned} \begin{bmatrix} K & e_1 & e_2 & e_3 \end{bmatrix} &= \begin{bmatrix} 2 & -1 & 0 & 1 & 0 & 0 \\ -1 & 2 & -1 & 0 & 1 & 0 \\ 0 & -1 & 2 & 0 & 0 & 1 \end{bmatrix} && \text{Bắt đầu Gauss-Jordan trên } K \\ &\rightarrow \begin{bmatrix} 2 & -1 & 0 & 1 & 0 & 0 \\ 0 & \frac{3}{2} & -1 & \frac{1}{2} & 1 & 0 \\ 0 & -1 & 2 & 0 & 0 & 1 \end{bmatrix} && (\frac{1}{2} \text{ hàng } 1 + \text{hàng } 2) \\ &\rightarrow \begin{bmatrix} 2 & -1 & 0 & 1 & 0 & 0 \\ 0 & \frac{3}{2} & -1 & \frac{1}{2} & 1 & 0 \\ 0 & 0 & \frac{4}{3} & \frac{1}{3} & \frac{2}{3} & 1 \end{bmatrix} && (\frac{2}{3} \text{ hàng } 2 + \text{hàng } 3) \end{aligned}$$

Chúng ta đã đi được nửa chặng đường đến $K^{-1}$. Ma trận ở ba cột đầu tiên là $U$ (tam giác trên). Các phần tử xoay 2, $\frac{3}{2}, \frac{4}{3}$ nằm trên đường chéo của nó. Gauss sẽ kết thúc bằng thế ngược (back substitution). Đóng góp của Jordan là *tiếp tục với phép khử!* Ông đi trọn con đường để đến **dạng bậc thang rút gọn (reduced echelon form)** $R = I$. Các hàng được cộng vào các hàng phía trên chúng, để tạo ra **các số không phía trên các phần tử xoay**:

$$\begin{aligned} \left( \begin{array}{c} \text{Số không phía trên} \\ \text{phần tử xoay thứ ba} \end{array} \right) &\rightarrow \begin{bmatrix} 2 & -1 & 0 & 1 & 0 & 0 \\ 0 & \frac{3}{2} & 0 & \frac{3}{4} & \frac{3}{2} & \frac{3}{4} \\ 0 & 0 & \frac{4}{3} & \frac{1}{3} & \frac{2}{3} & 1 \end{bmatrix} && (\frac{3}{4} \text{ hàng } 3 + \text{hàng } 2) \\ \left( \begin{array}{c} \text{Số không phía trên} \\ \text{phần tử xoay thứ hai} \end{array} \right) &\rightarrow \begin{bmatrix} 2 & 0 & 0 & \frac{3}{2} & 1 & \frac{1}{2} \\ 0 & \frac{3}{2} & 0 & \frac{3}{4} & \frac{3}{2} & \frac{3}{4} \\ 0 & 0 & \frac{4}{3} & \frac{1}{3} & \frac{2}{3} & 1 \end{bmatrix} && (\frac{2}{3} \text{ hàng } 2 + \text{hàng } 1) \end{aligned}$$

Bước Gauss-Jordan cuối cùng là chia mỗi hàng cho phần tử xoay của nó. Các phần tử xoay mới đều bằng 1.

Chúng ta đã đạt đến $I$ ở nửa đầu của ma trận, bởi vì $K$ khả nghịch. *Ba cột của $K^{-1}$ nằm ở nửa sau của $\begin{bmatrix} I & K^{-1} \end{bmatrix}$:*

| (chia cho 2)              | $\left[ \begin{array}{ccc|ccc} 1 & 0 & 0 & \frac{3}{4} & \frac{1}{2} & \frac{1}{4} \\ 0 & 1 & 0 & \frac{1}{2} & 1 & \frac{1}{2} \\ 0 & 0 & 1 & \frac{1}{4} & \frac{1}{2} & \frac{3}{4} \end{array} \right]$ | $= \begin{bmatrix} I & x_1 & x_2 & x_3 \end{bmatrix} = \begin{bmatrix} I & K^{-1} \end{bmatrix}$. |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|

Bắt đầu từ ma trận $3 \times 6$ $\begin{bmatrix} K & I \end{bmatrix}$, chúng ta kết thúc với $\begin{bmatrix} I & K^{-1} \end{bmatrix}$. Dưới đây là toàn bộ quy trình Gauss-Jordan trên một dòng cho bất kỳ ma trận khả nghịch $A$ nào:

| Gauss-Jordan | Nhân | $\begin{bmatrix} A & I \end{bmatrix}$ | với | $A^{-1}$ | để được | $\begin{bmatrix} I & A^{-1} \end{bmatrix}$ |
|--------------|----------|-----------|------|----------|----------|----------------|
|--------------|----------|-----------|------|----------|----------|----------------|

Các bước khử tạo ra ma trận nghịch đảo đồng thời thay đổi $A$ thành $I$. Đối với các ma trận lớn, chúng ta có lẽ hoàn toàn không cần $A^{-1}$. Nhưng đối với các ma trận nhỏ, việc biết nghịch đảo có thể rất đáng giá. Chúng ta bổ sung ba quan sát về $K^{-1}$: một ví dụ quan trọng.

- **1.** $K$ là ma trận *đối xứng (symmetric)* qua đường chéo chính của nó. Vậy thì $K^{-1}$ cũng đối xứng.
- **2.** $K$ là ma trận *ba đường chéo (tridiagonal)* (chỉ có ba đường chéo khác không). Nhưng $K^{-1}$ là một ma trận dày đặc (dense) không có các số không. Đó là một lý do khác khiến chúng ta không thường xuyên tính toán các ma trận nghịch đảo. Nghịch đảo của một ma trận dải (band matrix) thường là một ma trận dày đặc.
- **3.** *Tích của các phần tử xoay* là $2 (\frac{3}{2}) (\frac{4}{3}) = 4$. Con số 4 này chính là *định thức* của $K$.

| $K^{-1}$ liên quan đến phép chia cho định thức của $K$ | $K^{-1} = \frac{1}{4} \begin{bmatrix} 3 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 3 \end{bmatrix}$ | (8) |
|------------------------------------------------------|------------------------------------------------------------------------------------------|-----|
|------------------------------------------------------|------------------------------------------------------------------------------------------|-----|

**Đây là lý do tại sao một ma trận khả nghịch không thể có định thức bằng không: chúng ta cần phải chia.**

**Ví dụ 4** Tìm $A^{-1}$ bằng phép khử Gauss-Jordan bắt đầu từ $A = \begin{bmatrix} 2 & 3 \\ 4 & 7 \end{bmatrix}$.

$$\begin{bmatrix} A & I \end{bmatrix} = \begin{bmatrix} 2 & 3 & 1 & 0 \\ 4 & 7 & 0 & 1 \end{bmatrix} \rightarrow \begin{bmatrix} 2 & 3 & 1 & 0 \\ 0 & 1 & -2 & 1 \end{bmatrix} \quad (\text{đây là } \begin{bmatrix} U & L^{-1} \end{bmatrix})$$

$$\rightarrow \begin{bmatrix} 2 & 0 & 7 & -3 \\ 0 & 1 & -2 & 1 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 0 & \frac{7}{2} & -\frac{3}{2} \\ 0 & 1 & -2 & 1 \end{bmatrix} \quad (\text{đây là } \begin{bmatrix} I & A^{-1} \end{bmatrix}).$$

**Ví dụ 5** *Nếu $A$ khả nghịch và là tam giác trên, thì $A^{-1}$ cũng vậy.* Bắt đầu với $AA^{-1} = I$.

1. $A$ nhân *cột $j$ của $A^{-1}$* bằng *cột $j$ của $I$*, kết thúc với $n - j$ số không. 
2. Thế ngược giữ nguyên những $n - j$ số không đó ở cuối cột $j$ của $A^{-1}$. 
3. Đặt những cột $\begin{bmatrix} * & \dots & * & 0 & \dots & 0 \end{bmatrix}^T$ đó vào $A^{-1}$ và ma trận đó là tam giác trên!

| $A^{-1} = \begin{bmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{bmatrix}^{-1} = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}$ | Các cột $j = 1$ và $2$ kết thúc<br>bằng $3 - j = 2$ và $1$ số không. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
|                                                                                                                                                         |                                                                |

Mã lệnh cho $X = \text{inv}(A)$ có thể dùng **rref**, dạng bậc thang rút gọn theo hàng từ Chương 3:

| $I = \text{eye } (n)$ ;        | % Định nghĩa ma trận đơn vị $n \times n$                |
|--------------------------------|--------------------------------------------------------|
| $R = \text{rref } (\begin{bmatrix} A & I \end{bmatrix})$ ; | % Khử trên ma trận bổ sung $\begin{bmatrix} A & I \end{bmatrix}$          |
| $X = R(:, n+1:n+n)$            | % Chọn $X = A^{-1}$ từ $n$ cột cuối cùng của $R$. |

$A$ phải khả nghịch, nếu không phép khử không thể rút gọn nó về $I$ (ở nửa trái của $R$).

Gauss-Jordan cho thấy tại sao $A^{-1}$ lại đắt đỏ. Chúng ta giải $n$ phương trình cho $n$ cột của nó. Nhưng tất cả những phương trình đó đều liên quan đến cùng một ma trận $A$ ở vế trái (nơi hầu hết công việc được thực hiện). Tổng chi phí cho $A^{-1}$ là $n^3$ phép nhân và phép trừ. Để giải một phương trình $Ax = b$ duy nhất thì chi phí đó (xem phần tiếp theo) là $n^3/3$.

#### Để giải $Ax = b$ mà không cần $A^{-1}$, chúng ta xử lý *một* cột $b$ để tìm một cột $x$.

### **Số ít (Singular) và Khả nghịch (Invertible)**

Chúng ta quay trở lại câu hỏi trung tâm. Những ma trận nào có nghịch đảo? Phần đầu của phần này đã đề xuất bài kiểm tra phần tử xoay: *$A^{-1}$ tồn tại chính xác khi $A$ có một tập hợp đầy đủ gồm $n$ phần tử xoay.* (Cho phép hoán đổi hàng.) Bây giờ chúng ta có thể chứng minh điều đó bằng phương pháp khử Gauss-Jordan:

- **1.** Với $n$ phần tử xoay, phép khử giải tất cả các phương trình $Ax_i = e_i$. Các cột $x_i$ đi vào $A^{-1}$. Khi đó $AA^{-1} = I$ và $A^{-1}$ ít nhất là một *nghịch đảo phải.*
- **2.** Phép khử thực sự là một chuỗi các phép nhân bởi các ma trận $E$ và $P$ và $D^{-1}$

| Nghịch đảo trái $C$ | $CA = (D^{-1} \dots E \dots P \dots E)A = I.$ | (9) |
|------------------|--------------------------------------------------|-----|
|------------------|--------------------------------------------------|-----|

$D^{-1}$ chia cho các phần tử xoay. Các ma trận $E$ tạo ra các số không bên dưới và bên trên các phần tử xoay. $P$ sẽ hoán đổi các hàng nếu cần (xem Mục 2.7). Ma trận tích trong phương trình (9) hiển nhiên là một *nghịch đảo trái của $A$.* Với $n$ phần tử xoay, chúng ta đã đạt đến $A^{-1}A = I$.

*Nghịch đảo phải bằng nghịch đảo trái.* Đó là Ghi chú 2 ở đầu phần này. Vì vậy, một ma trận vuông với tập hợp đầy đủ các phần tử xoay sẽ luôn có một nghịch đảo hai phía.

Lập luận theo hướng ngược lại bây giờ sẽ cho thấy rằng *$A$ phải có $n$ phần tử xoay nếu $AC = I$.*

- **1.** Nếu $A$ không có $n$ phần tử xoay, phép khử sẽ dẫn đến một *hàng toàn số không.*
- **2.** Những bước khử đó được thực hiện bởi một ma trận khả nghịch $M$. *Vậy nên một hàng của $MA$ bằng không.*
- **3.** Nếu $AC = I$ có thể xảy ra, thì $MAC = M$. Hàng toàn số không của $MA$, nhân với $C$, tạo ra một hàng toàn số không của chính $M$.
- **4.** Một ma trận khả nghịch $M$ không thể có một hàng toàn số không! *$A$ phải* có $n$ phần tử xoay nếu $AC = I$.

Lập luận đó mất bốn bước, nhưng kết quả thì ngắn gọn và quan trọng. $C$ chính là $A^{-1}$. Phép khử cung cấp một bài kiểm tra hoàn chỉnh cho tính khả nghịch của một ma trận vuông. **$A^{-1}$ *tồn tại (và Gauss-Jordan tìm ra nó) chính xác khi $A$ có $n$ phần tử xoay.*** Lập luận ở trên còn cho thấy nhiều hơn thế:

| $\text{Nếu } AC = I \ \text{thì} \ CA = I \ \text{và} \ C = A^{-1}$ | (10) |
|----------------------------------------------------------------|------|
|----------------------------------------------------------------|------|

**Ví dụ 6** Nếu $L$ là ma trận tam giác dưới với các số 1 trên đường chéo, thì $L^{-1}$ cũng vậy.

#### *Một ma trận tam giác là khả nghịch nếu và chỉ nếu không có phần tử trên đường chéo nào bằng không.*

Ở đây $L$ có các số 1 nên $L^{-1}$ cũng có các số 1. Sử dụng phương pháp Gauss-Jordan để xây dựng $L^{-1}$ từ $E_{32}, E_{31}, E_{21}$. Hãy chú ý cách $L^{-1}$ chứa phần tử lạ 11, từ $3$ nhân $5$ trừ $4$.

| Gauss-Jordan<br>trên ma trận tam giác $L$     | $\begin{bmatrix} 1 & 0 & 0 \\ 3 & 1 & 0 \\ 4 & 5 & 1 \end{bmatrix}$ | $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ | 
|---------------------------------------|---------------------------------------------|------------------------------------------------------------------------------------|
|                                       | $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 5 & 1 \end{bmatrix}$ | $\begin{bmatrix} 1 & 0 & 0 \\ -3 & 1 & 0 \\ -4 & 0 & 1 \end{bmatrix}$ | $(3 \text{ lần hàng 1 khỏi hàng 2})$ <br> $(4 \text{ lần hàng 1 khỏi hàng 3})$ <br> $(\text{sau đó 5 lần hàng 2 khỏi hàng 3})$ |
| Nghịch đảo<br>vẫn là<br>tam giác | $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ | $\begin{bmatrix} 1 & 0 & 0 \\ -3 & 1 & 0 \\ 11 & -5 & 1 \end{bmatrix}$ | $\begin{bmatrix} I & L^{-1} \end{bmatrix}$                                                                                                         |

### **Nhận biết một Ma trận Khả nghịch**

Thông thường, phải mất công sức để quyết định xem một ma trận có khả nghịch hay không. Cách thông thường là tìm một tập hợp đầy đủ các phần tử xoay khác không trong phép khử. (Sau đó định thức khác không đến từ việc nhân những phần tử xoay đó.) Nhưng đối với một số ma trận, bạn có thể thấy ngay rằng chúng khả nghịch bởi vì mọi con số $a_{ii}$ trên đường chéo chính của chúng chi phối phần ngoài đường chéo của hàng $i$ đó.

**Các ma trận có đường chéo trội (Diagonally dominant matrices) là khả nghịch.** Mỗi $a_{ii}$ trên đường chéo lớn hơn tổng dọc theo phần còn lại của hàng $i$. Trên mọi hàng,

| $|a_{ii}| > \sum_{j \neq i} |a_{ij}|$ | có nghĩa là | $|a_{ii}| > |a_{i1}| + \dots (\text{bỏ qua } |a_{ii}|) \dots + |a_{in}|$. | (11) |
|---------------------------------------|------------|--------------------------------------------------------------------------|------|

**Các ví dụ.** $A$ có đường chéo trội (3 > 2). $B$ thì không (nhưng vẫn khả nghịch). $C$ là ma trận suy biến (singular).

| $A = \begin{bmatrix} 3 & 1 & 1 \\ 1 & 3 & 1 \\ 1 & 1 & 3 \end{bmatrix}$ | $B = \begin{bmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 3 \end{bmatrix}$ | $C = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 3 \end{bmatrix}$ |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
|-------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|

**Lập luận.** Lấy một vectơ $x$ khác không bất kỳ. *Giả sử thành phần lớn nhất của nó là* $|x_i|$. Khi đó $Ax = 0$ là không thể, bởi vì hàng $i$ của $Ax = 0$ sẽ cần

$$a_{i1}x_1 + \dots + a_{ii}x_i + \dots + a_{in}x_n = 0.$$

Những số đó không thể cộng lại bằng không khi $A$ có đường chéo trội! Độ lớn của $a_{ii}x_i$ (chỉ riêng một số hạng đó) đã lớn hơn tất cả các số hạng khác cộng lại:

**Bởi vì** $|x_j| \leq |x_i|$

$\sum_{j \neq i} |a_{ij}x_j| \leq \sum_{j \neq i} |a_{ij}| |x_i| < |a_{ii}| |x_i|$  bởi vì $a_{ii}$ **chiếm ưu thế (dominates)**

Điều này cho thấy $Ax = 0$ chỉ có thể xảy ra khi $x = 0$. *Vậy nên $A$ là khả nghịch.* Ví dụ $B$ cũng khả nghịch nhưng không hoàn toàn có đường chéo trội: 2 không lớn hơn 1 + 1.

#### **• ÔN TẬP CÁC Ý TƯỞNG CHÍNH (REVIEW OF THE KEY IDEAS) •**

- **1.** Ma trận nghịch đảo cho $AA^{-1} = I$ và $A^{-1}A = I$.
- **2.** $A$ khả nghịch nếu và chỉ nếu nó có $n$ phần tử xoay (cho phép hoán đổi hàng).
- **3.** *Quan trọng.* Nếu $Ax = 0$ cho một vectơ $x$ khác không, thì $A$ không có nghịch đảo.
- **4.** Nghịch đảo của $AB$ là tích ngược lại $B^{-1}A^{-1}$. Và $(ABC)^{-1} = C^{-1}B^{-1}A^{-1}$.
- **5.** Phương pháp Gauss-Jordan giải $AA^{-1} = I$ để tìm $n$ cột của $A^{-1}$. Ma trận bổ sung $\begin{bmatrix} A & I \end{bmatrix}$ được rút gọn theo hàng thành $\begin{bmatrix} I & A^{-1} \end{bmatrix}$.
- **6.** Các ma trận có đường chéo trội là khả nghịch. Mỗi $|a_{ii}|$ chi phối hàng của nó.

#### **• CÁC VÍ DỤ ĐÃ GIẢI (WORKED EXAMPLES) •**

**2.5 A** Nghịch đảo của một **ma trận hiệu (difference matrix)** tam giác $A$ là một **ma trận tổng (sum matrix)** tam giác $S$:

$$\begin{bmatrix} A & I \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 & 1 & 0 & 0 \\ -1 & 1 & 0 & 0 & 1 & 0 \\ 0 & -1 & 1 & 0 & 0 & 1 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 1 & 1 & 0 \\ 0 & -1 & 1 & 0 & 0 & 1 \end{bmatrix} \\ \rightarrow \begin{bmatrix} 1 & 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 & 1 & 1 \end{bmatrix} = \begin{bmatrix} I & A^{-1} \end{bmatrix} = \begin{bmatrix} I & \text{ma trận tổng} \end{bmatrix}.$$

Nếu tôi thay đổi $a_{13}$ thành $-1$, thì tất cả các hàng của $A$ cộng lại bằng không. Phương trình $Ax = 0$ bây giờ sẽ có nghiệm khác không là $x = (1, 1, 1)$. Một tín hiệu rõ ràng: *Ma trận $A$ mới này không thể nghịch đảo được.*

**2.5 B** Ba trong số các ma trận này là khả nghịch, và ba ma trận là suy biến. Hãy tìm nghịch đảo khi nó tồn tại. Đưa ra lý do cho tính không khả nghịch (định thức bằng không, quá ít phần tử xoay, nghiệm khác không đối với $Ax = 0$) cho ba ma trận kia. Các ma trận theo thứ tự $A, B, C, D, S, E$:

$$\begin{bmatrix} 4 & 3 \\ 8 & 6 \end{bmatrix} \quad \begin{bmatrix} 4 & 3 \\ 8 & 7 \end{bmatrix} \quad \begin{bmatrix} 6 & 6 \\ 6 & 0 \end{bmatrix} \quad \begin{bmatrix} 6 & 6 \\ 6 & 6 \end{bmatrix} \quad \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix} \quad \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix}$$

**Lời giải**

$$B^{-1} = \frac{1}{4} \begin{bmatrix} 7 & -3 \\ -8 & 4 \end{bmatrix} \quad C^{-1} = \frac{1}{36} \begin{bmatrix} 0 & 6 \\ 6 & -6 \end{bmatrix} \quad S^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix}$$

$A$ không khả nghịch vì định thức của nó là $4 \cdot 6 - 3 \cdot 8 = 24 - 24 = 0$. $D$ không khả nghịch vì chỉ có một phần tử xoay; hàng thứ hai trở thành số không khi trừ đi hàng đầu tiên. $E$ có hai hàng bằng nhau (và cột thứ hai trừ đi cột thứ nhất bằng không). Nói cách khác $Ex = 0$ có nghiệm $x = (-1, 1, 0)$.

Tất nhiên cả ba lý do cho sự không khả nghịch đều sẽ áp dụng cho mỗi ma trận $A, D, E$.

**2.5 C** Áp dụng phương pháp Gauss-Jordan để nghịch đảo ma trận tam giác "Pascal matrix" $L$ này. Bạn sẽ thấy **tam giác Pascal** - cộng mỗi phần tử với phần tử ở bên trái nó sẽ cho ra phần tử ở bên dưới. Các phần tử của $L$ là các "hệ số nhị thức (binomial coefficients)". Hàng tiếp theo sẽ là 1, 4, 6, 4, 1.

$$\text{Ma trận Pascal tam giác} \quad L = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 2 & 1 & 0 \\ 1 & 3 & 3 & 1 \end{bmatrix} = \text{abs}(\text{pascal}(4,1))$$

**Lời giải** Gauss-Jordan bắt đầu với $\begin{bmatrix} L & I \end{bmatrix}$ và tạo ra các số không bằng cách trừ đi hàng 1:

$$\begin{bmatrix} L & I \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 \\ 1 & 2 & 1 & 0 & 0 & 0 & 1 & 0 \\ 1 & 3 & 3 & 1 & 0 & 0 & 0 & 1 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & -1 & 1 & 0 & 0 \\ 0 & 2 & 1 & 0 & -1 & 0 & 1 & 0 \\ 0 & 3 & 3 & 1 & -1 & 0 & 0 & 1 \end{bmatrix}.$$

Giai đoạn tiếp theo tạo ra các số không bên dưới phần tử xoay thứ hai, sử dụng các số nhân 2 và 3. Sau đó, giai đoạn cuối cùng trừ đi 3 lần hàng 3 mới khỏi hàng 4 mới:

$$\rightarrow \begin{bmatrix} 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & -1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 1 & -2 & 1 & 0 \\ 0 & 0 & 3 & 1 & 2 & -3 & 0 & 1 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & -1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 1 & -2 & 1 & 0 \\ 0 & 0 & 0 & 1 & -1 & 3 & -3 & 1 \end{bmatrix} = \begin{bmatrix} I & L^{-1} \end{bmatrix}.$$

Tất cả các phần tử xoay đều là 1! Nên chúng ta không cần chia các hàng cho các phần tử xoay để lấy $I$. Ma trận nghịch đảo $L^{-1}$ trông giống hệt như bản thân $L$, ngoại trừ các đường chéo đánh số lẻ có dấu trừ.

Mẫu hình này tiếp tục cho các ma trận Pascal $n \times n$. $L^{-1}$ có "các đường chéo luân phiên dấu".

# **Bài Tập 2.5 (Problem Set 2.5)**

**1** Tìm các nghịch đảo (trực tiếp hoặc từ công thức $2 \times 2$) của $A, B, C$:

| $A = \begin{bmatrix} 0 & 3 \\ 4 & 0 \end{bmatrix}$ | và | $B = \begin{bmatrix} 2 & 0 \\ 4 & 2 \end{bmatrix}$ | và | $C = \begin{bmatrix} 3 & 4 \\ 5 & 7 \end{bmatrix}$ |
|----------------------------------------------------|-----|----------------------------------------------------|-----|----------------------------------------------------|
|----------------------------------------------------|-----|----------------------------------------------------|-----|----------------------------------------------------|

**2** Đối với các "ma trận hoán vị" này, hãy tìm $P^{-1}$ bằng cách thử và sai (với các số 1 và 0):

$$P = \begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix} \quad \text{và} \quad P = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{bmatrix}.$$

**3** Giải để tìm cột đầu tiên $(x, y)$ và cột thứ hai $(t, z)$ của $A^{-1}$:

$$\begin{bmatrix} 10 & 20 \\ 20 & 50 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix} \quad \text{và} \quad \begin{bmatrix} 10 & 20 \\ 20 & 50 \end{bmatrix} \begin{bmatrix} t \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}.$$

**4** Chứng minh rằng $\begin{bmatrix} 2 & 2 \\ 3 & 6 \end{bmatrix}$ không khả nghịch bằng cách cố gắng giải $AA^{-1} = I$ để tìm cột 1 của $A^{-1}$:

| $\begin{bmatrix} 2 & 2 \\ 3 & 6 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ | (Đối với một $A$ khác, cột 1 của $A^{-1}$ có thể tìm được nhưng cột 2 thì không?) |
|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|

**5** Tìm một ma trận tam giác trên $U$ (không phải ma trận đường chéo) với $U^2 = I$ có nghĩa là $U = U^{-1}$.

**6** (a) Nếu $A$ khả nghịch và $AB = AC$, chứng minh nhanh rằng $B = C$.
  - (b) Nếu $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$, tìm hai ma trận khác nhau sao cho $AB = AC$.

**7** (Quan trọng) Nếu $A$ có hàng 1 + hàng 2 = hàng 3, chứng minh rằng $A$ không khả nghịch:
  - (a) Giải thích tại sao $Ax = (0, 0, 1)$ không thể có nghiệm. Hãy cộng pt 1 + pt 2.
  - (b) Những vế phải $(b_1, b_2, b_3)$ nào có thể cho phép có một nghiệm cho $Ax = b$?
  - (c) Trong phép khử, điều gì xảy ra với phương trình 3?

**8** Nếu $A$ có cột 1 + cột 2 = cột 3, chứng minh rằng $A$ không khả nghịch:
  - (a) Tìm một nghiệm khác không $x$ cho $Ax = 0$. Ma trận có kích thước $3 \times 3$.
  - (b) Phép khử giữ cho cột 1 + cột 2 = cột 3. Giải thích tại sao không có phần tử xoay thứ ba.

**9** Giả sử $A$ khả nghịch và bạn hoán đổi hai hàng đầu tiên của nó để đạt được $B$. Ma trận mới $B$ có khả nghịch không? Bạn sẽ tìm $B^{-1}$ từ $A^{-1}$ như thế nào?

**10** Tìm các nghịch đảo (bằng bất kỳ cách hợp lệ nào) của

$$A = \begin{bmatrix} 0 & 0 & 0 & 2 \\ 0 & 0 & 3 & 0 \\ 0 & 4 & 0 & 0 \\ 5 & 0 & 0 & 0 \end{bmatrix} \quad \text{và} \quad B = \begin{bmatrix} 3 & 2 & 0 & 0 \\ 4 & 3 & 0 & 0 \\ 0 & 0 & 6 & 5 \\ 0 & 0 & 7 & 6 \end{bmatrix}.$$

**11** (a) Tìm các ma trận khả nghịch $A$ và $B$ sao cho $A + B$ không khả nghịch.
  - (b) Tìm các ma trận suy biến $A$ và $B$ sao cho $A + B$ khả nghịch.

**12** Nếu tích $C = AB$ là khả nghịch ($A$ và $B$ là ma trận vuông), thì bản thân $A$ là khả nghịch. Tìm một công thức cho $A^{-1}$ có liên quan đến $C^{-1}$ và $B$.

**13** Nếu tích $M = ABC$ của ba ma trận vuông là khả nghịch, thì $B$ là khả nghịch. (Cả $A$ và $C$ cũng vậy.) Tìm một công thức cho $B^{-1}$ có liên quan đến $M^{-1}$ và $A$ và $C$.

**14** Nếu bạn cộng hàng 1 của $A$ vào hàng 2 để lấy được $B$, làm thế nào bạn tìm $B^{-1}$ từ $A^{-1}$?

Lưu ý về thứ tự. Nghịch đảo của $B = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} A \end{bmatrix}$ là \_\_\_\_\_.

**15** Chứng minh rằng một ma trận có một cột toàn số không không thể có nghịch đảo.

**16** Nhân $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$ với $\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$. Nghịch đảo của mỗi ma trận là gì nếu $ad \neq bc$?

**17** (a) Ma trận $3 \times 3$ $E$ nào có cùng tác dụng với ba bước này? Trừ hàng 1 khỏi hàng 2, trừ hàng 1 khỏi hàng 3, sau đó trừ hàng 2 khỏi hàng 3.
  - (b) Ma trận $L$ duy nhất nào có cùng tác dụng với ba bước ngược lại này? Cộng hàng 2 vào hàng 3, cộng hàng 1 vào hàng 3, sau đó cộng hàng 1 vào hàng 2.

**18** Nếu $B$ là nghịch đảo của $A^2$, chứng minh rằng $AB$ là nghịch đảo của $A$.

**19** Tìm các số $a$ và $b$ để cho ra nghịch đảo của $5 \cdot \text{eye}(4) - \text{ones}(4, 4)$:

$$\begin{bmatrix} 4 & -1 & -1 & -1 \\ -1 & 4 & -1 & -1 \\ -1 & -1 & 4 & -1 \\ -1 & -1 & -1 & 4 \end{bmatrix}^{-1} = \begin{bmatrix} a & b & b & b \\ b & a & b & b \\ b & b & a & b \\ b & b & b & a \end{bmatrix}.$$

$a$ và $b$ trong nghịch đảo của $6 \cdot \text{eye}(5) - \text{ones}(5, 5)$ là gì?

**20** Chứng minh rằng $A = 4 \cdot \text{eye}(4) - \text{ones}(4, 4)$ *không* khả nghịch: Nhân $A \cdot \text{ones}(4, 1)$.

**21** Có mười sáu ma trận $2 \times 2$ có các phần tử là các số 1 và 0. Bao nhiêu trong số chúng là khả nghịch?

**Các câu hỏi 22-28 nói về phương pháp Gauss-Jordan để tính $A^{-1}$.**

**22** Biến đổi $I$ thành $A^{-1}$ khi bạn rút gọn $A$ về $I$ (bằng các phép toán hàng):

| $\begin{bmatrix} A & I \end{bmatrix} = \begin{bmatrix} 1 & 3 & 1 & 0 \\ 2 & 7 & 0 & 1 \end{bmatrix}$ | và | $\begin{bmatrix} A & I \end{bmatrix} = \begin{bmatrix} 1 & 4 & 1 & 0 \\ 3 & 9 & 0 & 1 \end{bmatrix}$ |
|--------------------------------------------------------------------------|-----|--------------------------------------------------------------------------|
|--------------------------------------------------------------------------|-----|--------------------------------------------------------------------------|

**23** Làm theo ví dụ trong sách $3 \times 3$ nhưng với các dấu cộng trong $A$. Khử phần trên và phần dưới của các phần tử xoay để rút gọn $\begin{bmatrix} A & I \end{bmatrix}$ thành $\begin{bmatrix} I & A^{-1} \end{bmatrix}$:

$$\begin{bmatrix} A & I \end{bmatrix} = \begin{bmatrix} 2 & 1 & 0 & 1 & 0 & 0 \\ 1 & 2 & 1 & 0 & 1 & 0 \\ 0 & 1 & 2 & 0 & 0 & 1 \end{bmatrix}.$$

**24** Sử dụng phép khử Gauss-Jordan trên $\begin{bmatrix} U & I \end{bmatrix}$ để tìm ma trận tam giác trên $U^{-1}$:

| $UU^{-1} = I$ | $\begin{bmatrix} 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & 1 \end{bmatrix}$ | $\begin{bmatrix} x_1 & x_2 & x_3 \end{bmatrix}$ | $= \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ |
|---------------|---------------------------------------------------------------------|-------------------------------------------------|-----------------------------------------------------------------------|
|---------------|---------------------------------------------------------------------|-------------------------------------------------|-----------------------------------------------------------------------|

**25** Tìm $A^{-1}$ và $B^{-1}$ (nếu *chúng tồn tại*) bằng phép khử trên $\begin{bmatrix} A & I \end{bmatrix}$ và $\begin{bmatrix} B & I \end{bmatrix}$:

| $A = \begin{bmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{bmatrix}$ | và | $B = \begin{bmatrix} 2 & -1 & -1 \\ -1 & 2 & -1 \\ -1 & -1 & 2 \end{bmatrix}$ |
|-------------------------------------------------------------------------|-----|-------------------------------------------------------------------------------|

**26** Ba ma trận $E_{21}$ và $E_{12}$ và $D^{-1}$ nào rút gọn $A = \begin{bmatrix} 1 & 2 \\ 2 & 7 \end{bmatrix}$ về ma trận đơn vị? Nhân $D^{-1}E_{12}E_{21}$ để tìm $A^{-1}$.

**27** Nghịch đảo các ma trận $A$ này bằng phương pháp Gauss-Jordan bắt đầu với $\begin{bmatrix} A & I \end{bmatrix}$:

|  | $A = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 3 \\ 0 & 0 & 1 \end{bmatrix}$ | và | $A = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 2 \\ 1 & 2 & 2 \end{bmatrix}$ |
|--|---------------------------------------------------------------------|-----|-------------------------------------------------------------------------|
|--|---------------------------------------------------------------------|-----|-------------------------------------------------------------------------|

**28** Hoán đổi các hàng và tiếp tục với Gauss-Jordan để tìm $A^{-1}$:

$$\begin{bmatrix} A & I \end{bmatrix} = \begin{bmatrix} 0 & 2 & 1 & 0 \\ 2 & 2 & 0 & 1 \end{bmatrix}.$$

**29** Đúng hay sai (với một phản ví dụ nếu sai và một lý do nếu đúng):
  - (a) Một ma trận $4 \times 4$ có một hàng toàn số không thì không khả nghịch.
  - (b) Mọi ma trận có các số 1 dọc theo đường chéo chính đều khả nghịch.
  - (c) Nếu $A$ khả nghịch thì $A^{-1}$ và $A^2$ đều khả nghịch.

**30 (Khuyên làm)** Chứng minh rằng $A$ khả nghịch nếu $a \neq 0$ và $a \neq b$ (tìm các phần tử xoay hoặc $A^{-1}$). Sau đó tìm ba con số $c$ để $C$ không khả nghịch:

$$A = \begin{bmatrix} a & b & b \\ a & a & b \\ a & a & a \end{bmatrix} \quad C = \begin{bmatrix} 2 & c & c \\ c & c & c \\ 8 & 7 & c \end{bmatrix}.$$

**31** Ma trận này có một nghịch đảo đáng chú ý. Tìm $A^{-1}$ bằng phép khử trên $\begin{bmatrix} A & I \end{bmatrix}$. Mở rộng cho một "ma trận luân phiên" $5 \times 5$ và đoán nghịch đảo của nó; sau đó nhân lại để xác nhận.

$$\text{Nghịch đảo } A = \begin{bmatrix} 1 & -1 & 1 & -1 \\ 0 & 1 & -1 & 1 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & 0 & 1 \end{bmatrix} \quad \text{và giải } Ax = (1, 1, 1, 1).$$

**32** Giả sử các ma trận $P$ và $Q$ có các hàng giống như $I$ nhưng theo bất kỳ thứ tự nào. Chúng là các "ma trận hoán vị (permutation matrices)". Chứng minh rằng $P - Q$ là suy biến bằng cách giải $(P - Q)x = 0$.

**33** Tìm và kiểm tra các nghịch đảo (giả sử chúng tồn tại) của các ma trận khối này:

$$\begin{bmatrix} I & 0 \\ C & I \end{bmatrix} \quad \begin{bmatrix} A & 0 \\ C & D \end{bmatrix} \quad \begin{bmatrix} 0 & I \\ I & D \end{bmatrix}.$$

**34** Liệu một ma trận $4 \times 4$ $A$ có thể khả nghịch nếu mọi hàng đều chứa các số 0, 1, 2, 3 theo một thứ tự nào đó? Điều gì xảy ra nếu mọi hàng của $B$ chứa 0, 1, 2, -3 theo một thứ tự nào đó?

**35** Trong Ví dụ Đã giải 2.5 **C**, ma trận Pascal tam giác $L$ có $L^{-1} = DLD$, trong đó ma trận đường chéo $D$ có các phần tử luân phiên 1, -1, 1, -1. Khi đó $LDLD = I$, vậy nghịch đảo của $LD = \text{pascal}(4, 1)$ là gì?

**36** Các ma trận Hilbert có $H_{ij} = 1/(i + j - 1)$. Yêu cầu MATLAB tính nghịch đảo chính xác $6 \times 6$ bằng lệnh invhilb(6). Sau đó yêu cầu nó tính inv(hilb(6)). Làm sao chúng có thể khác nhau, khi máy tính không bao giờ mắc lỗi?

**37** (a) Sử dụng lệnh inv(P) để nghịch đảo ma trận đối xứng $4 \times 4$ $P = \text{pascal}(4)$ của MATLAB.
  - (b) Tạo ma trận tam giác dưới của Pascal $L = \text{abs}(\text{pascal}(4, 1))$ và kiểm tra $P = LL^T$.

**38** Nếu $A = \text{ones}(4)$ và $b = \text{rand}(4, 1)$, làm sao MATLAB cho bạn biết rằng $Ax = b$ vô nghiệm? Đối với trường hợp đặc biệt $b = \text{ones}(4, 1)$, nghiệm nào cho $Ax = b$ được tìm thấy bởi lệnh $A \backslash b$?

### Các Bài toán Thử thách (Challenge Problems)

**39 (Khuyên làm)** $A$ là ma trận $4 \times 4$ với các số 1 trên đường chéo và $-a, -b, -c$ trên đường chéo bên trên. Tìm $A^{-1}$ cho ma trận hai đường chéo (bidiagonal matrix) này.

**40** Giả sử $E_1, E_2, E_3$ là các ma trận đơn vị $4 \times 4$, ngoại trừ $E_1$ có $a, b, c$ ở cột 1 và $E_2$ có $d, e$ ở cột 2 và $E_3$ có $f$ ở cột 3 (bên dưới các số 1). Nhân $L = E_1E_2E_3$ để chứng minh rằng tất cả những phần tử khác không này đều được sao chép vào $L$. $E_1E_2E_3$ theo thứ tự *ngược* với phép khử (vì $E_3$ tác động trước). Nhưng $E_1E_2E_3 = L$ thì theo thứ tự *đúng* để đảo ngược quá trình khử và khôi phục $A$.

**41** Các ma trận đạo hàm bậc hai (second difference matrices) có những nghịch đảo tuyệt đẹp nếu chúng bắt đầu với $T_{11} = 1$ (thay vì $K_{11} = 2$). Đây là ma trận ba đường chéo $3 \times 3$ $T$ và nghịch đảo của nó:

| $T = \begin{bmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{bmatrix}$ | $T^{-1} = \begin{bmatrix} 3 & 2 & 1 \\ 2 & 2 & 1 \\ 1 & 1 & 1 \end{bmatrix}$ |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------|
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------|

**42** Đây là thêm hai ma trận hiệu nữa, cả hai đều quan trọng. *Nhưng chúng có khả nghịch không?*

Một phương pháp tiếp cận là phép khử Gauss-Jordan trên $\begin{bmatrix} T & I \end{bmatrix}$. Tôi thà viết $T$ dưới dạng tích của các hiệu bậc nhất $L$ nhân với $U$. Các nghịch đảo của $L$ và $U$ trong Ví dụ Đã giải 2.5 A là các ma trận tổng, nên ở đây có $T = LU$ và $T^{-1} = U^{-1}L^{-1}$:

$$T = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix} \begin{bmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{bmatrix} \quad T^{-1} = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix}$$

**Câu hỏi. ($4 \times 4$)** Các phần tử xoay của $T$ là gì? Nghịch đảo $4 \times 4$ của nó là gì? Thứ tự ngược lại $UL$ cho ra ma trận nào $T^*$? Nghịch đảo của $T^*$ là gì?

$$\text{Ma trận tuần hoàn (Cyclic) } C = \begin{bmatrix} 2 & -1 & 0 & -1 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ -1 & 0 & -1 & 2 \end{bmatrix} \quad \text{Các đầu tự do (Free ends) } F = \begin{bmatrix} 1 & -1 & 0 & 0 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ 0 & 0 & -1 & 1 \end{bmatrix}.$$

**43** *Phép khử cho một ma trận khối:* Khi bạn nhân hàng khối đầu tiên $\begin{bmatrix} A & B \end{bmatrix}$ với $CA^{-1}$ và trừ đi từ hàng thứ hai $\begin{bmatrix} C & D \end{bmatrix}$, thì *"Phần bù Schur" (Schur complement)* $S$ xuất hiện:

| $\begin{bmatrix} I & 0 \\ -CA^{-1} & I \end{bmatrix} \begin{bmatrix} A & B \\ C & D \end{bmatrix} = \begin{bmatrix} A & B \\ 0 & S \end{bmatrix}$ | $A$ và $D$ là các ma trận vuông |
|---------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
|                                                                                                                                                   | $S = D - CA^{-1}B$.   |

Nhân ở bên phải để trừ $A^{-1}B$ nhân cột khối 1 khỏi cột khối 2.

| $\begin{bmatrix} A & B \\ 0 & S \end{bmatrix} \begin{bmatrix} I & -A^{-1}B \\ 0 & I \end{bmatrix} = ?$ | Tìm $S$ cho | $\begin{bmatrix} A & B \\ C & I \end{bmatrix} = \begin{bmatrix} 2 & 3 & 3 \\ 4 & 1 & 0 \\ 4 & 0 & 1 \end{bmatrix}$ |
|--------------------------------------------------------------------------------------------------------|--------------|--------------------------------------------------------------------------------------------------------------------|
|--------------------------------------------------------------------------------------------------------|--------------|--------------------------------------------------------------------------------------------------------------------|

*Các phần tử xoay khối là $A$ và $S$. Nếu chúng khả nghịch, thì $\begin{bmatrix} A & B \\ C & D \end{bmatrix}$ cũng khả nghịch.*

**44** Đẳng thức $A(I + BA) = (I + AB)A$ kết nối các nghịch đảo của $I + BA$ và $I + AB$ như thế nào? Cả hai cái đó đều khả nghịch hoặc đều suy biến: không hiển nhiên.

# **2.6 Phép khử = Phân tích nhân tử (Elimination = Factorization):** $A = LU$

- **1.** Mỗi bước khử $E_{ij}$ được nghịch đảo bởi $L_{ij}$. Ngoài đường chéo chính hãy đổi $-l_{ij}$ thành $+l_{ij}$.
- **2.** Toàn bộ quá trình khử tiến (forward elimination) (không có sự hoán đổi hàng) được nghịch đảo bởi $L$: $L = (L_{21}L_{31} \dots L_{n1})(L_{32} \dots L_{n2})(L_{43} \dots L_{n3}) \dots (L_{n,n-1})$.
- **3.** Ma trận tích $L$ đó vẫn là tam giác dưới. **Mỗi số nhân $l_{ij}$ nằm ở hàng $i$, cột $j$.**
- **4.** Ma trận gốc $A$ được khôi phục từ $U$ bằng $A = LU = (\text{tam giác dưới}) (\text{tam giác trên})$.
- **5.** Phép khử trên $Ax = b$ chạm đến $Ux = c$. Sau đó thế ngược giải $Ux = c$.
- **6.** Giải một hệ tam giác tiêu tốn $n^2/2$ phép nhân-trừ. Phép khử để tìm $U$ tiêu tốn $n^3/3$.

Sinh viên thường nói rằng các khóa học toán học quá mang tính lý thuyết. Ồ, phần này thì không. Nó gần như hoàn toàn thực tế. Mục tiêu là để mô tả phép khử Gauss theo cách hữu ích nhất. Nhiều ý tưởng chính của đại số tuyến tính, khi bạn nhìn kỹ chúng, thực chất là các *sự phân tích nhân tử (factorizations)* của một ma trận. Ma trận ban đầu $A$ trở thành tích của hai hoặc ba ma trận đặc biệt. Sự phân tích nhân tử đầu tiên - cũng là quan trọng nhất trong thực hành - bây giờ đến từ phép khử. *Các nhân tử $L$ và $U$ là các ma trận tam giác. Sự phân tích nhân tử phát sinh từ phép khử là $A = LU$.*

Chúng ta đã biết $U$, ma trận tam giác trên với các phần tử xoay nằm trên đường chéo của nó. Các bước khử đưa $A$ về $U$. Chúng ta sẽ thấy việc đảo ngược những bước đó (đưa $U$ trở lại $A$) đạt được như thế nào bởi một ma trận tam giác dưới $L$. *Các phần tử của $L$ chính xác là các số nhân $l_{ij}$* - cái đã nhân với hàng xoay $j$ khi nó bị trừ đi khỏi hàng $i$.

Bắt đầu với một ví dụ $2 \times 2$. Ma trận $A$ chứa 2, 1, 6, 8. Con số cần khử là 6. *Trừ đi 3 lần hàng 1 khỏi hàng 2.* Bước đó là $E_{21}$ theo chiều tiến với số nhân $l_{21} = 3$. Bước quay trở lại từ $U$ về $A$ là $L = E_{21}^{-1}$ (một phép cộng sử dụng $+3$):

**Chiều tiến từ $A$ đến $U$:** $E_{21}A = \begin{bmatrix} 1 & 0 \\ -3 & 1 \end{bmatrix} \begin{bmatrix} 2 & 1 \\ 6 & 8 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 0 & 5 \end{bmatrix} = U$
**Quay lại từ $U$ về $A$:** $E_{21}^{-1}U = \begin{bmatrix} 1 & 0 \\ 3 & 1 \end{bmatrix} \begin{bmatrix} 2 & 1 \\ 0 & 5 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 6 & 8 \end{bmatrix} = A.$
(Note: corrected the element 2 in U to 0).

Dòng thứ hai chính là sự phân tích nhân tử $LU = A$ của chúng ta. Thay vì $E_{21}^{-1}$ chúng ta viết $L$. Bây giờ chuyển sang các ma trận lớn hơn với nhiều $E$. *Khi đó $L$ sẽ bao gồm tất cả các nghịch đảo của chúng.*

Mỗi bước từ $A$ đến $U$ nhân với một ma trận $E_{ij}$ để tạo ra số không ở vị trí $(i, j)$. Để giữ điều này rõ ràng, chúng ta sẽ làm việc với trường hợp thường xuyên nhất - *khi không có sự hoán đổi hàng nào liên quan.* Nếu $A$ là $3 \times 3$, chúng ta nhân với $E_{21}$ và $E_{31}$ và $E_{32}$. Các số nhân $l_{ij}$ tạo ra các số không ở các vị trí $(2, 1)$ và $(3, 1)$ và $(3, 2)$ - tất cả đều nằm dưới đường chéo. Phép khử kết thúc với ma trận tam giác trên $U$.

Bây giờ di chuyển các ma trận $E$ sang phía bên kia, *nơi các nghịch đảo của chúng nhân với $U$:*

| $(E_{32}E_{31}E_{21})A = U$ | trở thành | $A = (E_{21}^{-1}E_{31}^{-1}E_{32}^{-1})U$ | tức là | $A = LU$. |
|-----------------------------|---------|--------------------------------------------|----------|------------|
|-----------------------------|---------|--------------------------------------------|----------|------------|

Các nghịch đảo đi theo thứ tự ngược lại, như chúng phải thế. Tích của ba nghịch đảo đó là $L$. *Chúng ta đã đạt đến $A = LU$.* Bây giờ chúng ta dừng lại để hiểu nó.

### **Giải thích và Các ví dụ (Explanation and Examples)**

*Điểm thứ nhất:* Mọi ma trận nghịch đảo $E^{-1}$ đều là *ma trận tam giác dưới.* Phần tử ngoài đường chéo của nó là $l_{ij}$, để đảo ngược phép trừ tạo ra bởi $-l_{ij}$. Đường chéo chính của $E$ và $E^{-1}$ chứa các số 1. Ví dụ của chúng ta ở trên có $l_{21} = 3$ và $E = \begin{bmatrix} 1 & 0 \\ -3 & 1 \end{bmatrix}$ và $L = E^{-1} = \begin{bmatrix} 1 & 0 \\ 3 & 1 \end{bmatrix}$.

*Điểm thứ hai:* Phương trình (2) chỉ ra một ma trận tam giác dưới (tích của các $E_{ij}$) nhân với $A$. Nó cũng chỉ ra tất cả các $E_{ij}^{-1}$ nhân với $U$ để mang $A$ quay trở lại. *Tích tam giác dưới của các nghịch đảo này là $L$.*

Một lý do cho việc làm việc với các nghịch đảo là chúng ta muốn phân tích nhân tử của $A$, chứ không phải $U$. "Dạng nghịch đảo" cho ra $A = LU$. Một lý do khác là chúng ta nhận được một thứ gì đó bổ sung, gần như nhiều hơn những gì chúng ta xứng đáng nhận được. Đây là điểm thứ ba, cho thấy $L$ là hoàn toàn chính xác.

*Điểm thứ ba:* Mỗi số nhân $l_{ij}$ đi thẳng vào đúng vị trí $i, j$ của nó - *không thay đổi* - trong tích của các nghịch đảo tạo thành $L$. Thông thường phép nhân ma trận sẽ trộn lẫn tất cả các con số. Ở đây điều đó không xảy ra. Thứ tự là đúng đắn cho các ma trận nghịch đảo, để giữ cho các chữ $l$ không thay đổi. Lý do được đưa ra dưới đây trong phương trình (2).

Bởi vì mỗi $E^{-1}$ có các số 1 dọc theo đường chéo của nó, điểm tốt đẹp cuối cùng là $L$ cũng vậy.

$A = LU$

*Đây là phép khử không có hoán đổi hàng.* Ma trận tam giác trên $U$ có các phần tử xoay trên đường chéo của nó. Ma trận tam giác dưới $L$ có tất cả các số 1 trên đường chéo của nó. *Các số nhân $l_{ij}$ nằm dưới đường chéo của $L$.*

**Ví dụ 1** Phép khử trừ $\frac{1}{2}$ lần hàng 1 khỏi hàng 2. Bước cuối cùng trừ $\frac{2}{3}$ lần hàng 2 khỏi hàng 3. Ma trận tam giác dưới $L$ có $l_{21} = \frac{1}{2}$ và $l_{32} = \frac{2}{3}$. Nhân $LU$ tạo ra $A$:
(Note: original text had j for 2/3 and 3/3 for L32 and U22, fixing it to be 2/3 based on math).

$$A = \begin{bmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ \frac{1}{2} & 1 & 0 \\ 0 & \frac{2}{3} & 1 \end{bmatrix} \begin{bmatrix} 2 & 1 & 0 \\ 0 & \frac{3}{2} & 1 \\ 0 & 0 & \frac{4}{3} \end{bmatrix} = LU.$$

Số nhân $(3, 1)$ bằng không bởi vì phần tử $(3, 1)$ trong $A$ bằng không. Không cần phép toán nào.

**Ví dụ 2** Đổi phần tử trên cùng bên trái từ 2 trong $A$ thành 1 trong $B$. Các phần tử xoay tất cả đều trở thành 1. Các số nhân tất cả đều là 1. Mẫu hình đó tiếp tục khi $B$ là $4 \times 4$:

$$\text{Mẫu hình đặc biệt} \quad B = \begin{bmatrix} 1 & 1 & 0 & 0 \\ 1 & 2 & 1 & 0 \\ 0 & 1 & 2 & 1 \\ 0 & 0 & 1 & 2 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 \end{bmatrix} \begin{bmatrix} 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 1 \end{bmatrix}.$$

Những ví dụ $LU$ này đang cho thấy một thứ gì đó bổ sung, rất quan trọng trong thực hành. Giả sử không có hoán đổi hàng. Khi nào chúng ta có thể dự đoán được các *số không* trong $L$ và $U$?

> *Khi một hàng của $A$ bắt đầu bằng các số không, hàng tương ứng của $L$ cũng vậy. Khi một cột của $A$ bắt đầu bằng các số không, cột tương ứng của $U$ cũng vậy.*

Nếu một hàng bắt đầu bằng số không, chúng ta không cần bước khử. $L$ có một số không, điều này tiết kiệm thời gian máy tính. Tương tự, các số không ở *đầu* của một cột được giữ lại và chuyển vào $U$. Nhưng xin hãy nhận ra: Các số không ở *giữa* của một ma trận rất có thể sẽ bị lấp đầy, trong khi phép khử quét về phía trước. Bây giờ chúng ta sẽ giải thích tại sao $L$ có các số nhân $l_{ij}$ đúng ở các vị trí, mà không có sự xáo trộn nào.

*Lý do chính tại sao $A$ bằng $LU$:* Hãy tự hỏi về những hàng xoay (pivot rows) bị trừ khỏi các hàng bên dưới. Chúng có phải là những hàng nguyên bản của $A$ không? *Không,* phép khử có lẽ đã làm thay đổi chúng. Chúng có phải là các hàng của $U$ không? *Đúng,* các hàng xoay không bao giờ thay đổi lại nữa. Khi tính toán hàng thứ ba của $U$, chúng ta trừ đi các bội số của các hàng trước đó của $U$ (*chứ không phải các hàng của $A$!*):

| Hàng 3 của $U = (\text{Hàng 3 của } A) - l_{31}(\text{Hàng 1 của } U) - l_{32}(\text{Hàng 2 của } U)$. | (1) |
|----------------------------------------------------------------------------------------------------------|-----|
|----------------------------------------------------------------------------------------------------------|-----|

Viết lại phương trình này để thấy rằng hàng $\begin{bmatrix} l_{31} & l_{32} & 1 \end{bmatrix}$ đang nhân với ma trận $U$:

| (Hàng 3 của $A$) = $l_{31}(\text{Hàng 1 của } U) + l_{32}(\text{Hàng 2 của } U) + 1(\text{Hàng 3 của } U)$. | (2) |
|-------------------------------------------------------------------------------------------------------------|-----|
|-------------------------------------------------------------------------------------------------------------|-----|

*Đây chính xác là hàng 3 của $A = LU$.* Hàng đó của $L$ chứa $l_{31}, l_{32}, 1$. Tất cả các hàng đều trông như thế này, bất kể kích thước của $A$. Với việc không có sự hoán đổi hàng, chúng ta có $A = LU$.

**Cân bằng tốt hơn từ LDU** $A = LU$ là "không đối xứng (unsymmetric)" bởi vì $U$ có các phần tử xoay trên đường chéo của nó trong khi $L$ có các số 1. Điều này rất dễ thay đổi. *Chia $U$ cho một ma trận đường chéo $D$ chứa các phần tử xoay.* Việc đó để lại một ma trận tam giác mới với các số 1 trên đường chéo:

$$\text{Tách } U \text{ thành } \begin{bmatrix} d_1 & & & & \\ & d_2 & & & \\ & & \ddots & & \\ & & & d_n & \\ & & & & \ddots \\ & & & & & 1 \end{bmatrix}$$

Rất thuận tiện (nhưng hơi rắc rối một chút) khi giữ cùng một chữ cái $U$ cho ma trận tam giác mới này. Nó có các số 1 trên đường chéo (giống như $L$). Thay vì dạng $LU$ bình thường, dạng mới có $D$ ở giữa: *Tam giác dưới $L$ nhân đường chéo $D$ nhân tam giác trên $U$.*

### *Sự phân tích nhân tử tam giác có thể được viết là $A = LU$ hoặc $A = LDU$.*

Bất cứ khi nào bạn thấy $LDU$, thì ngầm hiểu rằng $U$ có các số 1 trên đường chéo. *Mỗi hàng được chia cho phần tử khác không đầu tiên của nó - phần tử xoay.* Sau đó $L$ và $U$ được đối xử công bằng trong $LDU$:

| $\begin{bmatrix} 1 & 0 \\ 3 & 1 \end{bmatrix} \begin{bmatrix} 2 & 8 \\ 0 & 5 \end{bmatrix}$ | phân tách tiếp thành | $\begin{bmatrix} 1 & 0 \\ 3 & 1 \end{bmatrix} \begin{bmatrix} 2 & 0 \\ 0 & 5 \end{bmatrix} \begin{bmatrix} 1 & 4 \\ 0 & 1 \end{bmatrix}$ | (3) |
|---------------------------------------------------------------------------------------------|---------------------|---------------------------------------------------------------------------------------------|-----|
|---------------------------------------------------------------------------------------------|---------------------|---------------------------------------------------------------------------------------------|-----|

Các phần tử xoay 2 và 5 đã đi vào $D$. Chia các hàng cho 2 và 5 để lại các hàng $\begin{bmatrix} 1 & 4 \end{bmatrix}$ và $\begin{bmatrix} 0 & 1 \end{bmatrix}$ trong $U$ mới với các số một trên đường chéo. Số nhân 3 vẫn nằm trong $L$.

*Những bài giảng của riêng tôi đôi khi dừng lại ở điểm này.* Tôi đi tiếp sang phần 2.7. Các đoạn văn tiếp theo cho thấy các mã máy tính thực hiện phép khử được tổ chức như thế nào, và chúng mất bao lâu. Nếu có sẵn MATLAB (hoặc bất kỳ phần mềm nào), bạn có thể đo lường thời gian tính toán chỉ bằng cách đếm số giây.

### **Một Hệ Vuông = Hai Hệ Tam Giác (One Square System = Two Triangular Systems)**

Ma trận $L$ chứa đựng bộ nhớ của chúng ta về phép khử Gauss. Nó giữ những con số đã nhân với các hàng xoay, trước khi trừ chúng đi từ các hàng bên dưới. Khi nào chúng ta cần bản ghi chép này và chúng ta sử dụng nó như thế nào trong việc giải $Ax = b$?

Chúng ta cần $L$ ngay khi có một *vế phải $b$.* Các nhân tử $L$ và $U$ đã được quyết định hoàn toàn bởi vế trái (ma trận $A$). Ở vế phải của $Ax = b$, chúng ta sử dụng $L^{-1}$ và sau đó là $U^{-1}$. Bước *Giải (Solve)* đó giải quyết hai ma trận tam giác.

**1** *Phân tích nhân tử (Factor)* (thành $L$ và $U$, bằng phép khử trên ma trận vế trái $A$).
**2** *Giải (Solve)* (phép khử tiến trên $b$ sử dụng $L$, sau đó thế ngược để tìm $x$ sử dụng $U$).

Trước đó, chúng ta đã làm việc trên $A$ và $b$ cùng một lúc. Không có vấn đề gì với việc đó - chỉ cần bổ sung thành $\begin{bmatrix} A & b \end{bmatrix}$. Nhưng hầu hết các mã máy tính đều giữ hai vế tách biệt. Bộ nhớ của phép khử được lưu giữ trong $L$ và $U$, để xử lý $b$ bất cứ khi nào chúng ta muốn. Hướng dẫn sử dụng LAPACK (User's Guide to LAPACK) nhận xét rằng "Tình huống này quá phổ biến và khoản tiết kiệm là quá quan trọng đến mức không có một chương trình con đơn lẻ nào được cung cấp chỉ để giải một hệ duy nhất."

Bước *Giải (Solve)* hoạt động trên $b$ như thế nào? Đầu tiên, áp dụng phép khử tiến cho vế phải (các số nhân được lưu trữ trong $L$, hãy sử dụng chúng ngay bây giờ). Điều này làm thay đổi $b$ thành một vế phải mới $c$. *Chúng ta thực sự đang giải $Lc = b$.* Sau đó phép thế ngược giải $Ux = c$ như thường lệ. Hệ phương trình ban đầu $Ax = b$ được phân tách thành *hai hệ tam giác:*

| Khử tiến và lùi (Forward and backward) | Giải | $Lc = b$ | *và sau đó giải* | $Ux = c$ | (4) |
|----------------------------------------|-------|----------|-----------------------|----------|-----|
|                                        |       |          |                       |          |     |

Để thấy rằng $x$ là chính xác, nhân $Ux = c$ với $L$. Khi đó $LUx = Lc$ chính là $Ax = b$.

Xin nhấn mạnh: Không có *gì mới* về những bước này. Đây chính xác là những gì chúng ta đã làm từ đầu đến giờ. Chúng ta thực sự đã giải hệ tam giác $Lc = b$ khi phép khử tiến tới. Sau đó phép thế ngược tạo ra $x$. Một ví dụ cho thấy những gì chúng ta thực sự đã làm.

**Ví dụ 3** Phép khử tiến (từ trên xuống dưới) trên $Ax = b$ kết thúc ở $Ux = c$:

| $Ax = b$ | $u + 2v = 5$<br>$4u + 9v = 21$ | trở thành | $u + 2v = 5$<br>$v = 1$ | $Ux = c$ |
|----------|--------------------------------|---------|-------------------------|----------|
|          |                                |         |                         |          |

Số nhân là 4, được lưu trong $L$. Vế phải đã sử dụng số 4 đó để biến 21 thành 1:

| $Lc = b$ | Hệ tam giác dưới | $\begin{bmatrix} 1 & 0 \\ 4 & 1 \end{bmatrix} \begin{bmatrix} c_1 \\ c_2 \end{bmatrix} = \begin{bmatrix} 5 \\ 21 \end{bmatrix}$ | cho ra | $c = \begin{bmatrix} 5 \\ 1 \end{bmatrix}$ |
|----------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------|-------|--------------------------------------------|
| $Ux = c$ | Hệ tam giác trên | $\begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} u \\ v \end{bmatrix} = \begin{bmatrix} 5 \\ 1 \end{bmatrix}$  | cho ra | $x = \begin{bmatrix} 3 \\ 1 \end{bmatrix}$ |

$L$ và $U$ có thể được đưa vào $n^2$ vị trí lưu trữ vốn dĩ chứa $A$ (bây giờ có thể quên được).

#### **Chi Phí Của Phép Khử (The Cost of Elimination)**

Một câu hỏi rất thực tế là chi phí - hoặc thời gian tính toán. Chúng ta có thể giải 1000 phương trình trên một máy PC. Còn nếu $n = 100,000$ thì sao? *(Liệu $A$ là ma trận trù mật hay thưa thớt?)* Những hệ lớn luôn xuất hiện trong tính toán khoa học, nơi mà một bài toán ba chiều có thể dễ dàng dẫn đến một triệu ẩn số. Chúng ta có thể để máy tính chạy qua đêm, nhưng chúng ta không thể để nó chạy 100 năm.

Giai đoạn đầu tiên của phép khử tạo ra các số không bên dưới phần tử xoay đầu tiên trong cột 1. Để tìm mỗi phần tử mới bên dưới hàng xoay đòi hỏi một phép nhân và một phép trừ. *Chúng ta sẽ đếm giai đoạn đầu tiên này là $n^2$ phép nhân và $n^2$ phép trừ.* Thực tế thì ít hơn một chút, $n^2 - n$, bởi vì hàng 1 không thay đổi.

Giai đoạn tiếp theo dọn sạch cột thứ hai bên dưới phần tử xoay thứ hai. Ma trận làm việc bây giờ có kích thước $n-1$. Ước tính giai đoạn này bằng $(n-1)^2$ phép nhân và phép trừ. Các ma trận đang ngày càng nhỏ đi khi phép khử tiến tới. Số đếm gần đúng để đạt tới $U$ là tổng các bình phương $n^2 + (n-1)^2 + \dots + 2^2 + 1$.

Có một công thức chính xác $\frac{1}{3}n(n+\frac{1}{2})(n+1)$ cho tổng các bình phương này. Khi $n$ lớn, $\frac{1}{2}$ và 1 không quan trọng. *Con số quan trọng là $\frac{1}{3}n^3$.* Tổng các bình phương giống như tích phân của $x^2$! Tích phân từ 0 đến $n$ là $\frac{1}{3}n^3$:

# *Phép khử trên $A$ yêu cầu khoảng $\frac{1}{3}n^3$ phép nhân và $\frac{1}{3}n^3$ phép trừ.*

Vậy còn vế phải $b$ thì sao? Theo chiều tiến, chúng ta trừ đi các bội số của $b_1$ từ các thành phần bên dưới $b_2, \dots, b_n$. Quá trình này mất $n-1$ bước. Giai đoạn thứ hai chỉ mất $n-2$ bước, bởi vì $b_1$ không liên quan. Giai đoạn cuối cùng của phép khử tiến mất một bước.

Bây giờ bắt đầu phép thế ngược. Việc tính toán $x_n$ sử dụng một bước (chia cho phần tử xoay cuối cùng). Ẩn số tiếp theo sử dụng hai bước. Khi chúng ta chạm đến $x_1$, nó sẽ đòi hỏi $n$ bước ($n-1$ phép thế các ẩn số khác, sau đó chia cho phần tử xoay đầu tiên). Tổng số đếm trên vế phải, từ $b$ đến $c$ đến $x$ - tiến tới đáy và lùi về đỉnh - chính xác là $n^2$:

| $[(n-1) + (n-2) + \dots + 1] + [1 + 2 + \dots + (n-1) + n] = n^2$. | (5) |
|----------------------------------------------------------------------|-----|
|----------------------------------------------------------------------|-----|

Để thấy tổng đó, hãy ghép đôi $(n-1)$ với 1 và $(n-2)$ với 2. Các cặp ghép đó để lại $n$ số hạng, mỗi số hạng bằng $n$. Điều đó tạo ra $n^2$. Vế phải tốn ít chi phí hơn nhiều so với vế trái!

#### **Giải (Solve)** *Mỗi vế phải cần* **$n^2$** *phép nhân và* **$n^2$** *phép trừ.*

Một **ma trận dải (band matrix)** $B$ chỉ có $w$ đường chéo khác không bên dưới và bên trên đường chéo chính của nó. Các phần tử số không nằm ngoài dải vẫn là số không trong phép khử (chúng là số không trong $L$ và $U$).

Việc dọn sạch cột đầu tiên cần $w^2$ phép nhân và phép trừ ($w$ số không cần được tạo ra bên dưới phần tử xoay, mỗi số không sử dụng một hàng xoay có độ dài $w$). Sau đó, việc dọn sạch tất cả $n$ cột, để đạt đến $U$, cần không quá $nw^2$. Điều này tiết kiệm rất nhiều thời gian:

| Ma trận dải | Từ $A$ đến $U$: $\frac{1}{3} n^3$ giảm xuống còn $nw^2$ | Giải: $n^2$ giảm xuống còn $2nw$ |
|-------------|------------------------------------------------|------------------------------|
|-------------|------------------------------------------------|------------------------------|

Một ma trận ba đường chéo (bề rộng dải $w=1$) cho phép tính toán rất nhanh. Đừng lưu trữ các số không!

Trang web của cuốn sách có các Mã giảng dạy (Teaching Codes) để phân tích $A$ thành $LU$ và để giải $Ax = b$. Các mã máy tính chuyên nghiệp sẽ nhìn xuống mỗi cột để tìm *phần tử xoay lớn nhất có sẵn*, để hoán đổi các hàng và giảm thiểu sai số làm tròn.

Lệnh gạch chéo ngược (backslash) trong MATLAB $x = A \backslash b$ kết hợp **Phân tích (Factor)** và **Giải (Solve)** để tìm ra $x$.

*Mất bao lâu để giải $Ax = b$?* Đối với một ma trận ngẫu nhiên cấp $n = 1000$, một khoảng thời gian điển hình trên máy PC là 1 giây. Thời gian này được nhân với khoảng 8 khi $n$ được nhân với 2. Đối với các mã máy tính chuyên nghiệp, hãy truy cập **netlib.org**.

Theo quy tắc $n^3$ này, các ma trận lớn gấp 10 lần (cấp 10.000) sẽ mất một nghìn giây. Các ma trận cấp 100.000 sẽ mất một triệu giây. Điều này quá đắt đỏ nếu không có siêu máy tính, nhưng hãy nhớ rằng đây là những ma trận đầy. Hầu hết các ma trận trong thực tế đều thưa thớt (có nhiều phần tử bằng không). Trong trường hợp đó, $A = LU$ nhanh hơn nhiều.

#### **• ÔN TẬP CÁC Ý TƯỞNG CHÍNH (REVIEW OF THE KEY IDEAS) •**

- **1.** Phép khử Gauss (không có sự hoán đổi hàng) phân tích nhân tử $A$ thành $L$ nhân với $U$.
- **2.** Ma trận tam giác dưới $L$ chứa các số $l_{ij}$ đã nhân với các hàng xoay, đi từ $A$ đến $U$. Tích $LU$ cộng các hàng đó lại để khôi phục $A$.
- **3.** Ở vế phải, chúng ta giải $Lc = b$ (chiều tiến) và $Ux = c$ (chiều lùi).
- **4.** *Phân tích (Factor)*: Có khoảng $\frac{1}{3}n^3$ phép nhân và phép trừ trên vế trái.
- **5.** *Giải (Solve)*: Có $n^2$ phép nhân và phép trừ trên vế phải.
- **6.** Đối với ma trận dải, thay $\frac{1}{3}n^3$ thành $nw^2$ và thay $n^2$ thành $2nw$.

#### **• CÁC VÍ DỤ ĐÃ GIẢI (WORKED EXAMPLES) •**

**2.6 A** Ma trận tam giác dưới Pascal $L$ chứa *"tam giác Pascal"* nổi tiếng. Phép Gauss-Jordan đã nghịch đảo $L$ trong ví dụ đã giải **2.5 C**. Ở đây chúng ta phân tích nhân tử Pascal.

**Ma trận Pascal đối xứng $P$ là tích của các ma trận Pascal tam giác $L$ và $U$.** Ma trận đối xứng $P$ có tam giác Pascal nghiêng đi, sao cho mỗi phần tử là tổng của phần tử ở trên và phần tử ở bên trái. Ma trận đối xứng $P$ $n \times n$ là $\text{pascal}(n)$ trong MATLAB.

**Bài toán:** Thiết lập sự phân tích nhân tử dưới-trên (lower-upper factorization) đáng kinh ngạc $P = LU$.

$$\text{pascal}(4) = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & 2 & 3 & 4 \\ 1 & 3 & 6 & 10 \\ 1 & 4 & 10 & 20 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 2 & 1 & 0 \\ 1 & 3 & 3 & 1 \end{bmatrix} \begin{bmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 1 & 3 \\ 0 & 0 & 0 & 1 \end{bmatrix} = LU.$$

Sau đó dự đoán và kiểm tra hàng và cột tiếp theo cho các ma trận Pascal $5 \times 5$.

**Lời giải** Bạn có thể nhân $LU$ để ra được $P$. Tốt hơn là bắt đầu với ma trận đối xứng $P$ và đi đến ma trận tam giác trên $U$ bằng phép khử:

$$P = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & 2 & 3 & 4 \\ 1 & 3 & 6 & 10 \\ 1 & 4 & 10 & 20 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 2 & 3 \\ 0 & 2 & 5 & 9 \\ 0 & 3 & 9 & 19 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 1 & 3 \\ 0 & 0 & 3 & 10 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 1 & 3 \\ 0 & 0 & 0 & 1 \end{bmatrix} = U.$$

Các số nhân $l_{ij}$ đã đi vào những bước này được đặt một cách hoàn hảo vào trong $L$. Do đó $P = LU$ là một ví dụ đặc biệt gọn gàng. *Lưu ý rằng mọi phần tử xoay đều là 1 trên đường chéo của $U$.*

Phần tiếp theo sẽ cho thấy sự đối xứng tạo ra một mối quan hệ đặc biệt giữa ma trận tam giác $L$ và $U$ như thế nào. Đối với Pascal, $U$ là **"chuyển vị (transpose)"** của $L$.

Bạn có thể kỳ vọng lệnh MATLAB `lu(pascal(4))` tạo ra những ma trận $L$ và $U$ này. Điều đó không xảy ra bởi vì chương trình con `lu` chọn phần tử xoay lớn nhất có sẵn trong mỗi cột. Phần tử xoay thứ hai sẽ đổi từ 1 thành 3. Nhưng "sự phân tích nhân tử Cholesky (Cholesky factorization)" không hoán đổi hàng: $U = \text{chol}(\text{pascal}(4))$.

Chứng minh đầy đủ của $P = LU$ cho tất cả các kích thước của Pascal khá là thú vị. Bài báo "Pascal Matrices" nằm trên trang web của khóa học [web.mit.edu/18.06](http://web.mit.edu/18.06), tài liệu này cũng có sẵn qua *OpenCourseWare* của MIT tại [ocw.mit.edu](http://ocw.mit.edu). Những ma trận Pascal này có rất nhiều tính chất đáng chú ý - chúng ta sẽ gặp lại chúng.

**2.6 B** Bài toán là: Giải $Px = b = (1, 0, 0, 0)^T$. Vế phải này = cột của $I$ có nghĩa là $x$ sẽ là cột đầu tiên của $P^{-1}$. Đó chính là Gauss-Jordan, khớp với các cột của $PP^{-1} = I$. Chúng ta đã biết các ma trận Pascal $L$ và $U$ là các nhân tử của $P$:

**Hai hệ tam giác (Two triangular systems)**      $Lc = b$ (chiều tiến)      $Ux = c$ (chiều lùi).

**Lời giải** Hệ tam giác dưới $Lc = b$ được giải *từ trên xuống dưới*:

$$\begin{array}{lll} c_1 & = 1 & \Rightarrow c_1 = 1 \\ c_1 + c_2 & = 0 & \Rightarrow c_2 = -1 \\ c_1 + 2c_2 + c_3 & = 0 & \Rightarrow c_3 = 1 \\ c_1 + 3c_2 + 3c_3 + c_4 & = 0 & \Rightarrow c_4 = -1 \end{array}$$
cho ra $c = \begin{bmatrix} 1 \\ -1 \\ 1 \\ -1 \end{bmatrix}$

Phép khử tiến chính là phép nhân với $L^{-1}$. Nó tạo ra hệ tam giác trên $Ux = c$. Nghiệm $x$ được đưa ra như thường lệ bằng phép thế ngược, *từ dưới lên trên:*

| $x_1 + x_2 + x_3 + x_4 = 1$ | $x_1 = 4$ | $x_1 = 4$ |
|-----------------------------|-----------|------------|
| $x_2 + 2x_3 + 3x_4 = -1$    | $x_2 = -6$ | $x_2 = -6$ |
| $x_3 + 3x_4 = 1$            | $x_3 = 4$ | $x_3 = 4$ |
| $x_4 = -1$                  | $x_4 = -1$ | $x_4 = -1$ |
(Note: corrected the values in the table based on back substitution of U x = c).

Tôi thấy một mẫu hình trong nghiệm $x$ đó, nhưng tôi không biết nó đến từ đâu. Hãy thử **inv(pascal(4))**.

### **Bài Tập 2.6 (Problem Set 2.6)**

**Các Bài 1-14 tính toán sự phân tích nhân tử** $A = LU$ (và cả $A = LDU$).

**1 (Quan trọng)** Phép khử tiến thay đổi $\begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix} x = b$ thành một hệ tam giác $\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} x = c$:

| $x + y = 5$  | $x + y = 5$ | $\begin{bmatrix} 1 & 1 & 5 \\ 1 & 2 & 7 \end{bmatrix}$ | $\longrightarrow$ | $\begin{bmatrix} 1 & 1 & 5 \\ 0 & 1 & 2 \end{bmatrix}$ |
|--------------|-------------|--------------------------------------------------------|-------------------|--------------------------------------------------------|
| $x + 2y = 7$ | $y = 2$     |                                                        |                   |                                                        |

Bước đó đã trừ đi $l_{21} =$ \_\_ lần hàng 1 khỏi hàng 2. Bước ngược lại *cộng* $l_{21}$ lần hàng 1 vào hàng 2. Ma trận cho bước ngược lại đó là $L =$ \_\_. Nhân $L$ này với hệ tam giác $\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} x = \begin{bmatrix} 5 \\ 2 \end{bmatrix}$ để lấy được \_\_ = \_\_. Bằng chữ cái, $L$ nhân với $Ux = c$ để cho ra \_\_.

**2** Viết ra các hệ tam giác $2 \times 2$ $Lc = b$ và $Ux = c$ từ Bài 1. Kiểm tra xem $c = (5, 2)$ có giải được hệ thứ nhất không. Tìm $x$ giải được hệ thứ hai.

**3 (Chuyển sang $3 \times 3$)** Phép khử tiến thay đổi $Ax = b$ thành một hệ tam giác $Ux = c$:

| $x + y + z = 5$    | $x + y + z = 5$ | $x + y + z = 5$ |
|--------------------|-----------------|-----------------|
| $x + 2y + 3z = 7$  | $y + 2z = 2$    | $y + 2z = 2$    |
| $x + 3y + 6z = 11$ | $2y + 5z = 6$   | $z = 2$         |

Phương trình $z = 2$ trong $Ux = c$ bắt nguồn từ $x + 3y + 6z = 11$ ban đầu trong $Ax = b$ bằng cách trừ đi $l_{31} =$ \_\_ lần phương trình 1 và $l_{32} =$ \_\_ lần phương trình 2 *cuối cùng*. Đảo ngược điều đó để khôi phục $\begin{bmatrix} 1 & 3 & 6 & 11 \end{bmatrix}$ ở hàng cuối cùng của $A$ và $b$ từ những hàng cuối cùng $\begin{bmatrix} 1 & 1 & 1 & 5 \end{bmatrix}$ và $\begin{bmatrix} 0 & 1 & 2 & 2 \end{bmatrix}$ và $\begin{bmatrix} 0 & 0 & 1 & 2 \end{bmatrix}$ trong $U$ và $c$:

Hàng 3 của $\begin{bmatrix} A & b \end{bmatrix} = (l_{31} \text{ Hàng } 1 + l_{32} \text{ Hàng } 2 + 1 \text{ Hàng } 3)$ của $\begin{bmatrix} U & c \end{bmatrix}$.

Trong ký hiệu ma trận, đây là phép nhân với $L$. Vậy nên $A = LU$ và $b = Lc$.

**4** Các hệ tam giác $3 \times 3$ $Lc = b$ và $Ux = c$ từ Bài 3 là gì? Kiểm tra xem $c = (5, 2, 2)$ có giải được hệ thứ nhất không. $x$ nào giải được hệ thứ hai?

**5** Ma trận $E$ nào đưa $A$ về dạng tam giác $EA = U$? Nhân với $E^{-1} = L$ để phân tích $A$ thành $LU$:

$$A = \begin{bmatrix} 2 & 1 & 0 \\ 0 & 4 & 2 \\ 6 & 3 & 5 \end{bmatrix}.$$

**6** Hai ma trận khử $E_{21}$ và $E_{32}$ nào đưa $A$ về dạng tam giác trên $E_{32}E_{21}A = U$? Nhân với $E_{32}^{-1}$ và $E_{21}^{-1}$ để phân tích $A$ thành $LU = E_{21}^{-1}E_{32}^{-1}U$:

$$A = \begin{bmatrix} 1 & 1 & 1 \\ 2 & 4 & 5 \\ 0 & 4 & 0 \end{bmatrix}.$$

**7** Ba ma trận khử $E_{21}, E_{31}, E_{32}$ nào đưa $A$ về dạng tam giác trên $E_{32}E_{31}E_{21}A = U$? Nhân với $E_{32}^{-1}, E_{31}^{-1}$ và $E_{21}^{-1}$ để phân tích $A$ thành $L$ nhân với $U$:

$$A = \begin{bmatrix} 1 & 0 & 1 \\ 2 & 2 & 2 \\ 3 & 4 & 5 \end{bmatrix} \quad L = E_{21}^{-1}E_{31}^{-1}E_{32}^{-1}.$$

**8 Đây là bài toán cho thấy các nghịch đảo $E_{ij}^{-1}$ nhân với nhau như thế nào để cho ra $L$.** Bạn sẽ thấy điều này rõ nhất khi $A$ đã là ma trận tam giác dưới với các số 1 trên đường chéo. **Khi đó $U = I$!**

$$A = L = \begin{bmatrix} 1 & 0 & 0 \\ a & 1 & 0 \\ b & c & 1 \end{bmatrix}.$$

Các ma trận khử $E_{21}, E_{31}, E_{32}$ lần lượt chứa $-a$, sau đó là $-b$, sau đó là $-c$.

  - (a) Nhân $E_{32}E_{31}E_{21}$ để tìm ma trận duy nhất $E$ tạo ra $EA = I$.
  - (b) Nhân $E_{21}^{-1}E_{31}^{-1}E_{32}^{-1}$ để khôi phục $L$.

**Các số nhân $a, b, c$ bị xáo trộn trong $E$ nhưng lại hoàn hảo trong $L$.**

**9** Khi số không xuất hiện ở một vị trí phần tử xoay, $A = LU$ là không thể! (Chúng ta đang yêu cầu các phần tử xoay khác không trong $U$.) Hãy chứng minh trực tiếp tại sao cả hai phương trình này đều là không thể:

$$\begin{bmatrix} 0 & 1 \\ 2 & 3 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ l & 1 \end{bmatrix} \begin{bmatrix} d & e \\ 0 & f \end{bmatrix} \quad \begin{bmatrix} 1 & 1 & 0 \\ 1 & 1 & 2 \\ 1 & 2 & 1 \end{bmatrix} = \begin{bmatrix} 1 & & \\ l & 1 & \\ m & n & 1 \end{bmatrix} \begin{bmatrix} d & e & g \\ 0 & h & i \\ 0 & 0 & j \end{bmatrix}.$$

Những ma trận này cần một sự hoán đổi hàng. Điều đó sử dụng một "ma trận hoán vị" $P$.

**10** Con số $c$ nào dẫn đến số không ở vị trí phần tử xoay thứ hai? Một sự hoán đổi hàng là cần thiết và $A = LU$ sẽ không khả thi. Số $c$ nào tạo ra số không ở vị trí phần tử xoay thứ ba? Khi đó hoán đổi hàng không thể giúp được gì và phép khử thất bại:

$$A = \begin{bmatrix} 1 & c & 0 \\ 2 & 4 & 1 \\ 3 & 5 & 1 \end{bmatrix}.$$

**11** $L$ và $D$ (ma trận phần tử xoay đường chéo) cho ma trận $A$ này là gì? $U$ trong $A = LU$ là gì và $U$ mới trong $A = LDU$ là gì?

| Đã là tam giác rồi | $A = \begin{bmatrix} 2 & 4 & 8 \\ 0 & 3 & 9 \\ 0 & 0 & 7 \end{bmatrix}$ |
|--------------------|-------------------------------------------------------------------------|
|--------------------|-------------------------------------------------------------------------|

**12** $A$ và $B$ đối xứng qua đường chéo (bởi vì 4 = 4). Tìm các phân tích nhân tử ba (triple factorizations) $LDU$ của chúng và cho biết $U$ liên hệ như thế nào với $L$ đối với các ma trận đối xứng này:

| Đối xứng | $A = \begin{bmatrix} 2 & 4 \\ 4 & 11 \end{bmatrix}$ | và | $B = \begin{bmatrix} 1 & 4 & 0 \\ 4 & 12 & 4 \\ 0 & 4 & 0 \end{bmatrix}$ |
|-----------|-----------------------------------------------------|-----|--------------------------------------------------------------------------|
|-----------|-----------------------------------------------------|-----|--------------------------------------------------------------------------|

**13** *(Khuyên làm)* Tính $L$ và $U$ cho ma trận đối xứng $A$:

$$A = \begin{bmatrix} a & a & a & a \\ a & b & b & b \\ a & b & c & c \\ a & b & c & d \end{bmatrix}.$$

Tìm bốn điều kiện cho $a, b, c, d$ để có được $A = LU$ với bốn phần tử xoay.

**14** Ma trận không đối xứng này sẽ có cùng $L$ như trong Bài 13:

$$\text{Tìm } L \text{ và } U \text{ cho } A = \begin{bmatrix} a & r & r & r \\ a & b & s & s \\ a & b & c & t \\ a & b & c & d \end{bmatrix}.$$

Tìm bốn điều kiện cho $a, b, c, d, r, s, t$ để có được $A = LU$ với bốn phần tử xoay.

**Các Bài 15-16 sử dụng $L$ và $U$ (mà không cần $A$) để giải $Ax = b$.**

**15** Giải hệ tam giác $Lc = b$ để tìm $c$. Sau đó giải $Ux = c$ để tìm $x$:

| $L = \begin{bmatrix} 1 & 0 \\ 4 & 1 \end{bmatrix}$ | và | $U = \begin{bmatrix} 2 & 4 \\ 0 & 1 \end{bmatrix}$ | và | $b = \begin{bmatrix} 2 \\ 11 \end{bmatrix}$ |
|----------------------------------------------------|-----|----------------------------------------------------|-----|---------------------------------------------|
|----------------------------------------------------|-----|----------------------------------------------------|-----|---------------------------------------------|

Để an toàn, hãy nhân $LU$ và giải $Ax = b$ như bình thường. Hãy khoanh tròn $c$ khi bạn nhìn thấy nó.

**16** Giải $Lc = b$ để tìm $c$. Sau đó giải $Ux = c$ để tìm $x$. $A$ là gì?

| $L = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix}$ | và | $U = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}$ | và | $b = \begin{bmatrix} 1 \\ 5 \\ 6 \end{bmatrix}$ |
|-------------------------------------------------------------------------|-----|-------------------------------------------------------------------------|-----|-------------------------------------------------|
|-------------------------------------------------------------------------|-----|-------------------------------------------------------------------------|-----|-------------------------------------------------|

**17** (a) Khi bạn áp dụng các bước khử thông thường cho $L$, bạn thu được ma trận nào?

$$L = \begin{bmatrix} 1 & 0 & 0 \\ l_{21} & 1 & 0 \\ l_{31} & l_{32} & 1 \end{bmatrix}.$$

  - (b) Khi bạn áp dụng cùng những bước đó cho $I$, bạn thu được ma trận nào?
  - (c) Khi bạn áp dụng cùng những bước đó cho $LU$, bạn thu được ma trận nào?

**18** Nếu $A = LDU$ và cũng có $A = L_1 D_1 U_1$ với tất cả các nhân tử đều khả nghịch, thì $L = L_1$ và $D = D_1$ và $U = U_1$. *"Ba nhân tử này là duy nhất."*

Suy ra phương trình $L_1^{-1} L D = D_1 U_1 U^{-1}$. Hai vế là ma trận tam giác hay ma trận đường chéo? Suy ra $L = L_1$ và $U = U_1$ (tất cả chúng đều có các số 1 trên đường chéo). Khi đó $D = D_1$.

**19** *Các ma trận ba đường chéo (Tridiagonal matrices)* có các phần tử bằng không ngoại trừ trên đường chéo chính và hai đường chéo liền kề. Phân tích nhân tử những ma trận này thành $A = LU$ và $A = LDL^T$:

$$A = \begin{bmatrix} 1 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{bmatrix} \quad \text{và} \quad A = \begin{bmatrix} a & a & 0 \\ a & a+b & b \\ 0 & b & b+c \end{bmatrix}.$$

**20** Khi $T$ là ma trận ba đường chéo, các nhân tử $L$ và $U$ của nó chỉ có hai đường chéo khác không. Bạn sẽ tận dụng việc biết trước các số không trong $T$ như thế nào, trong một đoạn mã cho phép khử Gauss? Tìm $L$ và $U$.

Ma trận ba đường chéo
$$T = \begin{bmatrix} 1 & 2 & 0 & 0 \\ 2 & 3 & 1 & 0 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 3 & 4 \end{bmatrix}.$$

**21** Nếu $A$ và $B$ có các phần tử khác không ở các vị trí được đánh dấu bằng $x$, những số không nào (được đánh dấu bằng 0) *vẫn là số không* trong các nhân tử $L$ và $U$ của chúng?

$$A = \begin{bmatrix} x & x & x & x \\ x & x & x & x \\ 0 & x & x & x \\ 0 & 0 & x & x \end{bmatrix} \quad B = \begin{bmatrix} x & x & x & 0 \\ x & 0 & x & x \\ 0 & x & x & x \\ 0 & x & x & x \end{bmatrix}.$$

**22** Giả sử bạn thực hiện phép khử hướng lên trên (gần như chưa từng nghe thấy). Sử dụng hàng cuối cùng để tạo ra các số không trong cột cuối cùng (phần tử xoay là 1). Sau đó sử dụng hàng thứ hai để tạo ra số không phía trên phần tử xoay thứ hai. Tìm các nhân tử theo thứ tự bất thường $A = UL$.

| Tam giác trên nhân tam giác dưới | $A = \begin{bmatrix} 5 & 3 & 1 \\ 3 & 3 & 1 \\ 1 & 1 & 1 \end{bmatrix}$ |
|-------------------|-------------------------------------------------------------------------|
|-------------------|-------------------------------------------------------------------------|

**23** *Dễ nhưng quan trọng.* Nếu $A$ có các phần tử xoay 5, 9, 3 với việc không có hoán đổi hàng, các phần tử xoay cho ma trận con $2 \times 2$ ở góc trên bên trái $A_2$ (không có hàng 3 và cột 3) là gì?

# **Các Bài Toán Thử Thách (Challenge Problems)**

**24** Những ma trận khả nghịch nào cho phép $A = LU$ (phép khử không có hoán đổi hàng)? *Một câu hỏi hay!* Hãy xem xét từng ma trận con vuông ở góc trên bên trái $A_k$ của $A$.

*Tất cả các ma trận con $k \times k$ ở góc trên bên trái $A_k$ phải khả nghịch* (**kích thước** $k = 1, \dots, n$).

Giải thích câu trả lời đó: $A_k$ phân tích nhân tử thành \_\_ bởi vì $LU = \begin{bmatrix} L_k & 0 \\ * & * \end{bmatrix} \begin{bmatrix} U_k & * \\ 0 & * \end{bmatrix}$.

**25** Đối với ma trận đạo hàm bậc hai đường chéo hằng $6 \times 6$ $K$, hãy đưa các phần tử xoay và các số nhân vào $K = LU$. ($L$ và $U$ sẽ chỉ có hai đường chéo khác không, bởi vì $K$ có ba đường chéo.) Tìm một công thức cho phần tử $i, j$ của $L^{-1}$, bằng các phần mềm như MATLAB sử dụng inv$(L)$ hoặc bằng cách tìm kiếm một mẫu hình đẹp.

$$\text{ma trận } -1, 2, -1 \quad K = \begin{bmatrix} 2 & -1 & 0 & 0 & 0 & 0 \\ -1 & 2 & -1 & 0 & 0 & 0 \\ 0 & -1 & 2 & -1 & 0 & 0 \\ 0 & 0 & -1 & 2 & -1 & 0 \\ 0 & 0 & 0 & -1 & 2 & -1 \\ 0 & 0 & 0 & 0 & -1 & 2 \end{bmatrix} = \text{toeplitz}([2 \quad -1 \quad 0 \quad 0 \quad 0 \quad 0])$$

**26** Nếu bạn in ra $K^{-1}$, nó trông không đẹp lắm ($6 \times 6$). Nhưng nếu bạn in ra $7 K^{-1}$, ma trận đó trông thật tuyệt vời. Hãy viết ra $7 K^{-1}$ bằng tay, theo mẫu hình này:
**1** Hàng 1 và cột 1 là $(6, 5, 4, 3, 2, 1)$.
**2** Trên và bên trên đường chéo chính, hàng $i$ bằng $i$ nhân với hàng 1.
**3** Trên và bên dưới đường chéo chính, cột $j$ bằng $j$ nhân với cột 1.

Nhân $K$ với $7 K^{-1}$ đó để tạo ra $7I$. Đây là $4 K^{-1}$ cho $n = 3$:

| Trường hợp $3 \times 3$      | $(K)(4K^{-1}) = \begin{bmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{bmatrix} \begin{bmatrix} 3 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 3 \end{bmatrix} = \begin{bmatrix} 4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 4 \end{bmatrix}$ |  |  |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
| Định thức của $K$ này là 4 |                                                                                                                                                                                                                                   |  |  |

# **2.7 Chuyển vị và Hoán vị (Transposes and Permutations)**

- **1.** Chuyển vị của $Ax$ và $AB$ và $A^{-1}$ lần lượt là $x^T A^T$ và $B^T A^T$ và $(A^T)^{-1}$.
- **2.** Tích vô hướng (tích trong) là $x \cdot y = x^T y$. Nó là $(1 \times n)(n \times 1) = (1 \times 1)$. Tích ngoài (outer product) là $xy^T = \text{cột nhân hàng} = (n \times 1)(1 \times n) = \text{ma trận } n \times n$.
- **3.** Ý tưởng đằng sau $A^T$ là $Ax \cdot y$ bằng với $x \cdot A^T y$ bởi vì $(Ax)^T y = x^T A^T y = x^T (A^T y)$.
- **4. Một ma trận đối xứng (symmetric matrix)** có $S^T = S$ (và tích $A^T A$ luôn luôn đối xứng).
- **5. Một ma trận trực giao (orthogonal matrix)** có $Q^T = Q^{-1}$. Các cột của $Q$ là các vectơ đơn vị trực giao.
- **6. Một ma trận hoán vị (permutation matrix)** $P$ có các hàng giống như $I$ (theo bất kỳ thứ tự nào). Có $n!$ thứ tự khác nhau.
- **7.** Khi đó $Px$ đưa các thành phần $x_1, x_2, \dots, x_n$ vào thứ tự mới đó. Và $P^T$ bằng $P^{-1}$.

Chúng ta cần thêm một ma trận nữa, và may mắn thay nó đơn giản hơn nhiều so với ma trận nghịch đảo. Nó là *"chuyển vị (transpose)"* của $A$, được ký hiệu là $A^T$. *Các cột của $A^T$ chính là các hàng của $A$.*

Khi $A$ là một ma trận $m \times n$, thì chuyển vị của nó là $n \times m$:

**Chuyển vị** Nếu $A = \begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 4 \end{bmatrix}$ thì $A^T = \begin{bmatrix} 1 & 0 \\ 2 & 0 \\ 3 & 4 \end{bmatrix}$.

Bạn có thể viết các hàng của $A$ thành các cột của $A^T$. Hoặc bạn có thể viết các cột của $A$ thành các hàng của $A^T$. Ma trận "lật qua" đường chéo chính của nó. Phần tử ở hàng $i$, cột $j$ của $A^T$ đến từ hàng $j$, cột $i$ của ma trận $A$ ban đầu:

**Hoán đổi các hàng và các cột** $$(A^T)_{ij} = A_{ji}$$

Chuyển vị của một ma trận tam giác dưới là ma trận tam giác trên. (Nhưng nghịch đảo của nó vẫn là tam giác dưới.) Chuyển vị của $A^T$ chính là $A$.

*Lưu ý* Ký hiệu của MATLAB cho chuyển vị của $A$ là $A'$. Việc nhập `[1 2 3]` cho ra một vectơ hàng và vectơ cột tương ứng là $v = [1 \quad 2 \quad 3]'$. Để nhập một ma trận $M$ với cột thứ hai $w = [4 \quad 5 \quad 6]'$, bạn có thể định nghĩa $M = [v \quad w]$. Sẽ nhanh hơn nếu nhập theo các hàng và sau đó chuyển vị toàn bộ ma trận: $M = [1 \quad 2 \quad 3 ; 4 \quad 5 \quad 6]'$.

Các quy tắc cho các phép chuyển vị rất trực tiếp. Chúng ta có thể chuyển vị $A + B$ để lấy $(A + B)^T$. Hoặc chúng ta có thể chuyển vị $A$ và $B$ riêng biệt, và sau đó cộng $A^T + B^T$ - với kết quả như nhau. Những câu hỏi nghiêm túc là về chuyển vị của một tích $AB$ và của một nghịch đảo $A^{-1}$.

| Tổng | Chuyển vị của | $A + B$ | là | $A^T + B^T$ | (1) |
|-----|------------------|---------|----|-------------|-----|
|     |                  |         |             |     |

| Tích | Chuyển vị của $AB$ | là | $(AB)^T$ | = | $B^T A^T$ | (2) |
|---------|-----------------------|------|------|---|-------------------|-----|
|         |                       |      |      |                   |     |

| Nghịch đảo | Chuyển vị của | $A^{-1}$ | là | $(A^{-1})^T = (A^T)^{-1}$. | (3) |
|---------|------------------|----------|----|-----------------------------|-----|
|         |                  |          |    |                             |     |

Lưu ý đặc biệt việc $B^T A^T$ đi theo thứ tự ngược lại như thế nào. Đối với các nghịch đảo, thứ tự ngược lại này rất nhanh để kiểm tra: $B^{-1} A^{-1}$ nhân với $AB$ tạo ra $I$. Để hiểu $(AB)^T = B^T A^T$, hãy bắt đầu với $(Ax)^T = x^T A^T$ khi $B$ chỉ là một vectơ:

#### $Ax$ *tổ hợp các cột của* $A$ *trong khi* $x^T A^T$ *tổ hợp các hàng của* $A^T$.

Nó là cùng một sự tổ hợp của cùng những vectơ đó! Trong $A$ chúng là các cột, trong $A^T$ chúng là các hàng. Vậy nên chuyển vị của cột $Ax$ chính là hàng $x^T A^T$. Điều đó phù hợp với công thức $(Ax)^T = x^T A^T$ của chúng ta. Bây giờ chúng ta có thể chứng minh công thức $(AB)^T = B^T A^T$, khi $B$ có một vài cột.

Nếu $B = \begin{bmatrix} x_1 & x_2 \end{bmatrix}$ có hai cột, hãy áp dụng cùng ý tưởng đó cho từng cột. Các cột của $AB$ là $Ax_1$ và $Ax_2$. Các chuyển vị của chúng xuất hiện một cách chính xác ở các hàng của $B^T A^T$:

Chuyển vị $AB = \begin{bmatrix} Ax_1 & Ax_2 & \dots \end{bmatrix}$ cho ra $\begin{bmatrix} x_1^T A^T \\ x_2^T A^T \\ \vdots \end{bmatrix}$ chính là $B^T A^T$. (4)

Câu trả lời đúng $B^T A^T$ xuất hiện từng hàng một. Đây là các con số trong $(AB)^T = B^T A^T$:

| $AB = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 5 & 0 \\ 4 & 1 \end{bmatrix} = \begin{bmatrix} 5 & 0 \\ 9 & 1 \end{bmatrix}$ | và | $B^T A^T = \begin{bmatrix} 5 & 4 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 5 & 9 \\ 0 & 1 \end{bmatrix}$ |
|-------------------------------------------------------------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                 |     |                                                                                                                                                      |

Quy tắc thứ tự ngược lại được mở rộng cho ba hoặc nhiều nhân tử hơn: $(ABC)^T$ bằng $C^T B^T A^T$.

Nếu $A = LDU$ thì $A^T = U^T D^T L^T$. Ma trận phần tử xoay có $D = D^T$.

Bây giờ áp dụng quy tắc tích này bằng cách chuyển vị cả hai vế của $A^{-1}A = I$. Ở một vế, $I^T$ là $I$. Chúng ta xác nhận quy tắc rằng $(A^{-1})^T$ là nghịch đảo của $A^T$. Tích của chúng là $I$:

| Chuyển vị của nghịch đảo | $A^{-1}A = I$ | được chuyển vị thành | $A^T(A^{-1})^T = I$ | (5) |
|----------------------|---------------|------------------|---------------------|-----|
|                      |               |                  |                     |     |

Tương tự $AA^{-1} = I$ dẫn đến $(A^{-1})^T A^T = I$. Chúng ta có thể nghịch đảo ma trận chuyển vị hoặc chúng ta có thể chuyển vị ma trận nghịch đảo. Xin đặc biệt lưu ý: $A^T$ *khả nghịch khi và chỉ khi* $A$ *khả nghịch.*

**Ví dụ 1** Nghịch đảo của $A = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}$ là $A^{-1} = \begin{bmatrix} 1 & 0 \\ -1 & 1 \end{bmatrix}$. Chuyển vị là $A^T = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$.

| $(A^{-1})^T$ | và | $(A^T)^{-1}$ | cả hai đều bằng | $\begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix}$ |
|--------------|-------|--------------|---------------------|-----------------------|
|              |       |              |                     |                       |

## **Ý Nghĩa của Các Tích Vô Hướng (The Meaning of Inner Products)**

Chúng ta đã biết tích vô hướng (tích trong - inner product) của $x$ và $y$. Nó là tổng của các số $x_i y_i$. Bây giờ chúng ta có một cách tốt hơn để viết $x \cdot y$, mà không cần sử dụng dấu chấm kém chuyên nghiệp đó. Thay vào đó hãy sử dụng ký hiệu ma trận:

$T$ **ở bên trong** *Tích vô hướng hoặc tích trong là $x^T y$* $(1 \times n)(n \times 1)$
$T$ **ở bên ngoài** *Tích bậc một (rank one product) hoặc tích ngoài là $xy^T$* $(n \times 1)(1 \times n)$

$x^T y$ là một con số, $xy^T$ là một ma trận. Cơ học lượng tử sẽ viết chúng như là $\langle x | y \rangle$ (tích trong) và $|x\rangle \langle y|$ (tích ngoài). Có lẽ vũ trụ được chi phối bởi đại số tuyến tính. Đây là thêm ba ví dụ nữa nơi tích trong có ý nghĩa:

**Từ cơ học** Công (Work) = (Các chuyển động) (Các lực) = $x^T f$

**Từ mạch điện** Tổn thất nhiệt (Heat loss) = (Các độ sụt áp) (Các dòng điện) = $e^T y$

**Từ kinh tế học** Thu nhập (Income) = (Các số lượng) (Các mức giá) = $q^T p$

Chúng ta đang thực sự tiến gần đến trung tâm của toán học ứng dụng, và có thêm một điểm nữa cần nhấn mạnh. Nó là mối liên hệ sâu sắc hơn giữa các tích trong và chuyển vị của $A$.

Chúng ta đã định nghĩa $A^T$ bằng cách lật ma trận qua đường chéo chính của nó. Đó không phải là toán học. Có một cách tiếp cận tốt hơn đối với phép chuyển vị. *$A^T$ là ma trận làm cho hai tích trong này bằng nhau đối với mọi $x$ và $y$:*

$(Ax)^T y = x^T (A^T y)$    Tích trong của $Ax$ với $y$ = Tích trong của $x$ với $A^T y$

| Bắt đầu với $A = \begin{bmatrix} -1 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix}$ | $x = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$ | $y = \begin{bmatrix} y_1 \\ y_2 \end{bmatrix}$ |
|-------------------------------------------------------------------------|-------------------------------------------------------|------------------------------------------------|
|-------------------------------------------------------------------------|-------------------------------------------------------|------------------------------------------------|

Ở một vế chúng ta có $Ax$ nhân với $y$: $(x_2 - x_1)y_1 + (x_3 - x_2)y_2$

Đó cũng giống như $x_1(-y_1) + x_2(y_1 - y_2) + x_3(y_2)$. Bây giờ $x$ đang nhân với $A^T y$.

| $A^T y$ phải là | $\begin{bmatrix} -y_1 \\ y_1 - y_2 \\ y_2 \end{bmatrix}$ | điều đó tạo ra | $A^T = \begin{bmatrix} -1 & 0 \\ 1 & -1 \\ 0 & 1 \end{bmatrix}$ | như kỳ vọng. |
|--------------------------|----------------------------------------------------------|----------------|-----------------------------------------------------------------|--------------|
|--------------------------|----------------------------------------------------------|----------------|-----------------------------------------------------------------|--------------|

#### **Các Ma Trận Đối Xứng (Symmetric Matrices)**

Đối với một *ma trận đối xứng*, việc chuyển vị $A$ thành $A^T$ không tạo ra sự thay đổi nào. Khi đó $A^T$ bằng $A$. Phần tử ở vị trí $(j, i)$ của nó qua đường chéo chính bằng phần tử ở vị trí $(i, j)$ của nó. Theo ý kiến của tôi, đây là những ma trận quan trọng nhất trong tất cả các ma trận. Chúng ta dành cho các ma trận đối xứng một chữ cái đặc biệt là $S$.

**ĐỊNH NGHĨA** Một *ma trận đối xứng* có $S^T = S$. Điều này có nghĩa là $s_{ji} = s_{ij}$.

$$\text{Các ma trận đối xứng} \quad S = \begin{bmatrix} 1 & 2 \\ 2 & 5 \end{bmatrix} = S^T \quad \text{và} \quad D = \begin{bmatrix} 1 & 0 \\ 0 & 10 \end{bmatrix} = D^T.$$

*Nghịch đảo của một ma trận đối xứng cũng là ma trận đối xứng.* Chuyển vị của $S^{-1}$ là $(S^{-1})^T = (S^T)^{-1} = S^{-1}$. Điều đó nói lên rằng $S^{-1}$ là đối xứng (khi $S$ khả nghịch):

$$\text{Các nghịch đảo đối xứng} \quad S^{-1} = \begin{bmatrix} 5 & -2 \\ -2 & 1 \end{bmatrix} \quad \text{và} \quad D^{-1} = \begin{bmatrix} 1 & 0 \\ 0 & 0.1 \end{bmatrix}.$$

Bây giờ chúng ta tạo ra một ma trận đối xứng $S$ bằng cách *nhân bất kỳ ma trận $A$ nào với $A^T$*.

### Các Tích Đối Xứng $A^T A$ và $AA^T$ và $LDL^T$

Chọn một ma trận $A$ bất kỳ, có thể là hình chữ nhật. Nhân $A^T$ với $A$. Khi đó tích $S = A^T A$ tự động là một ma trận vuông đối xứng:

*Chuyển vị của $A^T A$ là $A^T(A^T)^T$ điều này lại trở về $A^T A$.* (6)

Đó là một chứng minh nhanh chóng cho tính đối xứng của $A^T A$. Chúng ta có thể xem xét phần tử $(i, j)$ của $A^T A$. Nó là tích vô hướng của hàng $i$ của $A^T$ (chính là cột $i$ của $A$) với cột $j$ của $A$. Phần tử $(j, i)$ cũng là tích vô hướng đó, cột $j$ với cột $i$. Do đó $A^T A$ là đối xứng.

Ma trận $AA^T$ cũng đối xứng. (Kích thước của $A$ và $A^T$ cho phép thực hiện phép nhân.) Nhưng $AA^T$ là một ma trận khác với $A^T A$. Theo kinh nghiệm của chúng tôi, hầu hết các bài toán khoa học bắt đầu bằng một ma trận hình chữ nhật $A$ thì cuối cùng sẽ đụng đến $A^T A$ hoặc $AA^T$ hoặc cả hai. Chẳng hạn như trong phương pháp bình phương tối thiểu (least squares).

**Ví dụ 2** Nhân $A = \begin{bmatrix} -1 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix}$ và $A^T = \begin{bmatrix} -1 & 0 \\ 1 & -1 \\ 0 & 1 \end{bmatrix}$ theo cả hai thứ tự.

$$AA^T = \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix} \quad \text{và} \quad A^T A = \begin{bmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{bmatrix} \quad \text{cả hai đều là ma trận đối xứng.}$$

Tích $A^T A$ có kích thước $n \times n$. Ở thứ tự ngược lại, $AA^T$ có kích thước $m \times m$. Cả hai đều đối xứng, với các phần tử trên đường chéo dương (tại sao?). Nhưng ngay cả khi $m = n$, thì rất có khả năng là $A^T A \neq AA^T$. Dấu bằng có thể xảy ra, nhưng đó là điều bất thường.

**Các ma trận đối xứng trong phép khử** $S^T = S$ làm cho phép khử nhanh hơn, bởi vì chúng ta có thể làm việc với một nửa ma trận (cộng thêm đường chéo). Có một sự thật là ma trận tam giác trên $U$ có lẽ không đối xứng. *Tính đối xứng nằm trong tích của ba ma trận* $S = LDU$. Hãy nhớ lại cách mà ma trận đường chéo $D$ gồm các phần tử xoay có thể được chia ra, để chừa lại các số 1 trên đường chéo của cả $L$ và $U$:

$$\begin{bmatrix} 1 & 2 \\ 2 & 7 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 0 & 3 \end{bmatrix} \quad LU \text{ thiếu tính đối xứng của } S$$

$$\begin{bmatrix} 1 & 2 \\ 2 & 7 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 0 & 3 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix} \quad LDL^T \text{ nắm bắt được tính đối xứng của } L \quad \text{Bây giờ } U \text{ là chuyển vị của } L.$$

Khi $S$ là ma trận đối xứng, dạng thông thường $A = LDU$ trở thành $S = LDL^T$. Ma trận $U$ cuối cùng (với các số 1 trên đường chéo) là chuyển vị của $L$ (cũng với các số 1 trên đường chéo). Ma trận đường chéo $D$ chứa các phần tử xoay tự bản thân nó là ma trận đối xứng.

#### *Nếu $S = S^T$ được phân tích nhân tử thành $LDU$ mà không có hoán đổi hàng, thì $U$ chính xác là $L^T$.*

### *Phân tích nhân tử đối xứng của một ma trận đối xứng là $S = LDL^T$.*

Lưu ý rằng chuyển vị của $LDL^T$ tự động là $(L^T)^T D^T L^T$ điều này lại trở về $LDL^T$. Công việc của phép khử được giảm đi một nửa, từ $n^3/3$ phép nhân xuống còn $n^3/6$. Dung lượng lưu trữ cũng giảm đi đáng kể một nửa. Chúng ta chỉ giữ lại $L$ và $D$, chứ không phải $U$ vốn chỉ là $L^T$.

#### **Các Ma Trận Hoán Vị (Permutation Matrices)**

Ma trận chuyển vị đóng một vai trò đặc biệt đối với một *ma trận hoán vị*. Ma trận $P$ này có một số "1" duy nhất trong mỗi hàng và mỗi cột. Khi đó $P^T$ cũng là một ma trận hoán vị - có thể giống như $P$ hoặc có thể khác. Bất kỳ tích $P_1 P_2$ nào cũng lại là một ma trận hoán vị.

Bây giờ chúng ta tạo ra mọi ma trận $P$ từ ma trận đơn vị, bằng cách sắp xếp lại các hàng của $I$.

Ma trận hoán vị đơn giản nhất là $P = I$ *(không có sự hoán đổi)*. Những ma trận đơn giản tiếp theo là các phép hoán đổi hàng $P_{ij}$. Chúng được xây dựng bằng cách hoán đổi hai hàng $i$ và $j$ của $I$. Các phép hoán vị khác sắp xếp lại nhiều hàng hơn. Bằng cách thực hiện tất cả các phép hoán đổi hàng có thể có đối với $I$, chúng ta thu được tất cả các ma trận hoán vị có thể có:

#### **ĐỊNH NGHĨA** *Một ma trận hoán vị $P$ có các hàng của ma trận đơn vị $I$ theo một thứ tự bất kỳ.*

**Ví dụ 3** Có sáu ma trận hoán vị $3 \times 3$. Dưới đây là chúng mà không có các số không:

| <span></span>                                                          | <span></span>                                                          | <span></span>                                                                | <span></span> |
|------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------------|---------------|
| $I = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$      | $P_{21} = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ | $P_{32}P_{21} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{bmatrix}$ |               |
| $P_{31} = \begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix}$ | $P_{32} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}$ | $P_{21}P_{32} = \begin{bmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}$ |               |

*Có $n!$ ma trận hoán vị cấp $n$.* Ký hiệu $n!$ có nghĩa là "$n$ giai thừa", là tích của các số $(1)(2)\dots(n)$. Do đó $3! = (1)(2)(3)$ là 6. Sẽ có 24 ma trận hoán vị cấp $n = 4$. Và 120 phép hoán vị cấp 5.

Chỉ có hai ma trận hoán vị cấp 2, đó là $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ và $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$.

*Quan trọng:* $P^{-1}$ *cũng là một ma trận hoán vị.* Trong số sáu ma trận $P$ kích thước $3 \times 3$ được hiển thị ở trên, bốn ma trận ở bên trái là nghịch đảo của chính chúng. Hai ma trận ở bên phải là nghịch đảo của nhau. Trong tất cả các trường hợp, một phép hoán đổi hàng duy nhất là nghịch đảo của chính nó. Nếu chúng ta lặp lại phép hoán đổi, chúng ta sẽ quay trở lại $I$. Nhưng đối với $P_{32}P_{21}$, các nghịch đảo đi theo thứ tự ngược lại như thường lệ. Nghịch đảo là $P_{21}P_{32}$.

Quan trọng hơn: $P^{-1}$ *luôn luôn giống với* $P^T$. Hai ma trận ở bên phải là chuyển vị - và là nghịch đảo - của nhau. Khi chúng ta nhân $P P^T$, số "1" ở hàng đầu tiên của $P$ gặp số "1" ở cột đầu tiên của $P^T$ (bởi vì hàng đầu tiên của $P$ chính là cột đầu tiên của $P^T$). Nó trượt khỏi các số 1 ở tất cả các cột khác. Do đó $P P^T = I$.

Một chứng minh khác cho $P^T = P^{-1}$ xem xét $P$ như là một tích của các phép hoán đổi hàng. Mỗi phép hoán đổi hàng là chuyển vị của chính nó và là nghịch đảo của chính nó. $P^T$ và $P^{-1}$ cả hai đều xuất phát từ tích của các phép hoán đổi hàng *theo thứ tự ngược lại*. Vì vậy $P^T$ và $P^{-1}$ là giống nhau.

*Các phép hoán vị (hoán đổi hàng trước khi khử) dẫn đến $PA = LU$.*

# **Phân Tích Nhân Tử $PA = LU$ với Việc Hoán Đổi Hàng**

Chúng tôi chắc chắn hy vọng bạn nhớ $A = LU$. Nó bắt đầu với $A = (E_{21}^{-1} \dots E_{ij}^{-1} \dots) U$. Mỗi bước khử được thực hiện bởi một ma trận $E_{ij}$ và nó được nghịch đảo bởi $E_{ij}^{-1}$. Những nghịch đảo đó được nén lại thành một ma trận $L$. Ma trận tam giác dưới $L$ có các số 1 trên đường chéo, và kết quả là $A = LU$.

Đây là một sự phân tích nhân tử tuyệt vời, nhưng nó không phải lúc nào cũng hoạt động. Đôi khi các hoán đổi hàng là cần thiết để tạo ra các phần tử xoay. Khi đó $A = (E^{-1} \dots P^{-1} \dots E^{-1} \dots P^{-1} \dots) U$. Mỗi phép hoán đổi hàng được thực hiện bởi một ma trận $P_{ij}$ và được nghịch đảo bởi chính $P_{ij}$ đó. Bây giờ chúng ta nén những phép hoán đổi hàng đó thành một *ma trận hoán vị $P$ duy nhất*. Điều này mang lại một sự phân tích nhân tử cho mọi ma trận khả nghịch $A$ - điều mà chúng ta tự nhiên muốn có.

Câu hỏi chính là thu thập các $P_{ij}$ ở đâu. Có hai khả năng tốt - thực hiện tất cả các phép hoán đổi trước khi khử, hoặc thực hiện chúng sau các $E_{ij}$. Cách thứ nhất cho ra $PA = LU$. Cách thứ hai có một ma trận hoán vị $P_1$ ở giữa.

- **1.** Các phép hoán đổi hàng có thể được thực hiện *trước*. Tích $P$ của chúng đặt các hàng của $A$ theo đúng thứ tự, sao cho không cần phép hoán đổi nào cho $PA$. *Khi đó $PA = LU$.*
- **2.** Nếu chúng ta giữ lại các phép hoán đổi hàng cho đến *sau khi khử*, các hàng chứa phần tử xoay sẽ ở một thứ tự kỳ lạ. $P_1$ đặt chúng vào đúng thứ tự tam giác trong $U_1$. *Khi đó $A = L_1 P_1 U_1$.*

$PA = LU$ được sử dụng liên tục trong mọi quá trình tính toán. *Chúng ta sẽ tập trung vào dạng này.*

Phân tích nhân tử $A = L_1 P_1 U_1$ có thể tinh tế hơn. Nếu chúng tôi đề cập đến cả hai, thì đó là vì sự khác biệt không được biết đến nhiều. Có lẽ bạn sẽ không dành nhiều thời gian cho dạng nào cả. Xin đừng. Trường hợp quan trọng nhất là có $P = I$, khi $A$ bằng $LU$ và không có phép hoán đổi nào.

Ma trận $A$ này bắt đầu với $a_{11} = 0$. Hoán đổi hàng 1 và hàng 2 để đưa phần tử xoay đầu tiên vào vị trí thông thường của nó. Sau đó đi qua phép khử trên $PA$:

$$\begin{bmatrix} 0 & 1 & 1 \\ 1 & 2 & 9 \\ 2 & 7 & 9 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 2 & 9 \\ 0 & 1 & 1 \\ 2 & 7 & 9 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 2 & 9 \\ 0 & 1 & 1 \\ 0 & 3 & -9 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 2 & 9 \\ 0 & 1 & 1 \\ 0 & 0 & -12 \end{bmatrix}.$$

Ma trận $PA$ có các hàng của nó ở thứ tự tốt, và nó phân tích nhân tử như bình thường thành $LU$:

$$P = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} \quad PA = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 2 & 3 & 1 \end{bmatrix} \begin{bmatrix} 1 & 2 & 9 \\ 0 & 1 & 1 \\ 0 & 0 & -12 \end{bmatrix} = LU. \quad (7)$$

Chúng ta bắt đầu với $A$ và kết thúc với $U$. *Yêu cầu duy nhất là tính khả nghịch của $A$.*

Nếu $A$ khả nghịch, một phép hoán vị $P$ sẽ đặt các hàng của nó theo đúng thứ tự để phân tích nhân tử $PA = LU$. Phải có một tập hợp đầy đủ các phần tử xoay sau các phép hoán đổi hàng để $A$ khả nghịch.

Trong MATLAB, `A([r k], :) = A([k r], :)` hoán đổi hàng $k$ với hàng $r$ bên dưới nó (nơi phần tử xoay thứ $k$ đã được tìm thấy). Khi đó mã `lu` cập nhật $L$ và $P$ và dấu của $P$:

| <span></span>                | $A([r \ k], :) = A([k \ r], :);$               |
|------------------------------|------------------------------------------------|
| **Đây là một phần của**      | $L([r \ k], 1 : k - 1) = L([k \ r], 1 : k - 1);$ |
| $[L, U, P] = \text{lu}(A)$ | $P([r \ k], :) = P([k \ r], :);$                 |
|                              | $\text{sign} = -\text{sign}$                                   |

**"Dấu (sign)"** của $P$ cho biết liệu số lượng các phép hoán đổi hàng là chẵn (sign = +1). Một số lẻ các phép hoán đổi hàng sẽ tạo ra sign = -1. Khi bắt đầu, $P$ là $I$ và sign = +1. Khi có một phép hoán đổi hàng, dấu bị đảo ngược. Giá trị cuối cùng của sign là **định thức của $P$** và nó không phụ thuộc vào thứ tự của các phép hoán đổi hàng.

Đối với $PA$ chúng ta quay trở lại với $LU$ quen thuộc. Trong thực tế, một đoạn mã như `lu(A)` thường không sử dụng phần tử xoay có sẵn đầu tiên. Về mặt toán học chúng ta có thể chấp nhận một phần tử xoay nhỏ - bất cứ điều gì ngoại trừ số không. **Tất cả các đoạn mã tốt đều nhìn dọc theo cột để tìm phần tử xoay lớn nhất.**

Mục 11.1 giải thích tại sao *"partial pivoting"* (chọn phần tử xoay một phần) này làm giảm sai số làm tròn. Khi đó $P$ có thể chứa các phép hoán đổi hàng không cần thiết về mặt đại số. Tuy nhiên vẫn có $PA = LU$.

Lời khuyên của chúng tôi là hãy hiểu các phép hoán vị nhưng hãy để máy tính làm công việc đó. Các tính toán cho $A = LU$ là đủ để làm bằng tay, không cần $P$. Mã giảng dạy (Teaching Code) `splu(A)` phân tích nhân tử $PA = LU$ và `splv(A, b)` giải $Ax = b$ cho mọi ma trận khả nghịch $A$. Chương trình `splu` trên trang web sẽ dừng nếu không thể tìm thấy phần tử xoay nào trong cột $k$. Khi đó $A$ là không khả nghịch.

#### **• ÔN TẬP CÁC Ý TƯỞNG CHÍNH •**

- **1.** Chuyển vị đưa các hàng của $A$ thành các cột của $A^T$. Khi đó $(A^T)_{ij} = A_{ji}$.
- **2.** Chuyển vị của $AB$ là $B^T A^T$. Chuyển vị của $A^{-1}$ là nghịch đảo của $A^T$.
- **3.** Tích vô hướng là $x \cdot y = x^T y$. Khi đó $(Ax)^T y$ bằng tích vô hướng $x^T (A^T y)$.
- **4.** Khi $S$ đối xứng ($S^T = S$), phân tích nhân tử $LDU$ của nó là đối xứng: $S = LDL^T$.
- **5.** Một ma trận hoán vị $P$ có một số 1 trong mỗi hàng và mỗi cột, và $P^T = P^{-1}$.
- **6.** Có $n!$ ma trận hoán vị có kích thước $n$. *Một nửa là chẵn, một nửa là lẻ.*
- **7.** Nếu $A$ khả nghịch thì một phép hoán vị $P$ sẽ sắp xếp lại các hàng của nó để có $PA = LU$.

#### **• CÁC VÍ DỤ ĐÃ GIẢI •**

**2.7 A** Việc áp dụng phép hoán vị $P$ vào các hàng của $S$ phá hủy tính đối xứng của nó:

$$P = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{bmatrix} \quad S = \begin{bmatrix} 1 & 4 & 5 \\ 4 & 2 & 6 \\ 5 & 6 & 3 \end{bmatrix} \quad PS = \begin{bmatrix} 4 & 2 & 6 \\ 5 & 6 & 3 \\ 1 & 4 & 5 \end{bmatrix}$$

Phép hoán vị $Q$ nào áp dụng cho các *cột* của $PS$ sẽ khôi phục tính đối xứng trong $PSQ$? Các số 1, 2, 3 phải quay trở lại đường chéo chính (không nhất thiết phải theo thứ tự). Hãy chứng minh rằng $Q$ là $P^T$, để **tính đối xứng được bảo toàn bởi** $PS P^T$.

**Lời giải** Để khôi phục tính đối xứng và đưa số "2" trở lại đường chéo, cột 2 của $PS$ phải di chuyển đến cột 1. Cột 3 của $PS$ (chứa số "3") phải di chuyển đến cột 2. Khi đó số "1" di chuyển đến vị trí 3, 3. Ma trận hoán vị các cột là $Q$:

| $PS = \begin{bmatrix} 4 & 2 & 6 \\ 5 & 6 & 3 \\ 1 & 4 & 5 \end{bmatrix}$ | $Q = \begin{bmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}$ | $PSQ = \begin{bmatrix} 2 & 6 & 4 \\ 6 & 3 & 5 \\ 4 & 5 & 1 \end{bmatrix}$ | là đối xứng. |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------|
|--------------------------------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------|

*Ma trận $Q$ chính là $P^T$.* Sự lựa chọn này luôn khôi phục tính đối xứng, bởi vì $PS P^T$ được đảm bảo là đối xứng. (Chuyển vị của nó lại chính là $P S P^T$.) Ma trận $Q$ cũng là $P^{-1}$, *bởi vì nghịch đảo của mọi ma trận hoán vị chính là chuyển vị của nó.*

Nếu $D$ là một ma trận đường chéo, chúng ta thấy rằng $PD P^T$ cũng là ma trận đường chéo. Khi $P$ di chuyển hàng 1 xuống hàng 3, thì $P^T$ ở bên phải sẽ di chuyển cột 1 sang cột 3. Phần tử $(1, 1)$ di chuyển xuống $(3, 1)$ và đi qua $(3, 3)$.

**2.7 B** Tìm phân tích nhân tử đối xứng $S = LDL^T$ cho ma trận $S$ ở trên.

**Lời giải** Để phân tích $S$ thành $LDL^T$, chúng ta thực hiện phép khử như bình thường để đi đến $U$:

| $S = \begin{bmatrix} 1 & 4 & 5 \\ 4 & 2 & 6 \\ 5 & 6 & 3 \end{bmatrix} \longrightarrow \begin{bmatrix} 1 & 4 & 5 \\ 0 & -14 & -14 \\ 0 & -14 & -22 \end{bmatrix} \longrightarrow \begin{bmatrix} 1 & 4 & 5 \\ 0 & -14 & -14 \\ 0 & 0 & -8 \end{bmatrix} = U.$ |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Các số nhân là $l_{21} = 4$ và $l_{31} = 5$ và $l_{32} = 1$. **Các phần tử xoay 1, -14, -8 đi vào $D$.** Khi chúng ta chia các hàng của $U$ cho những phần tử xoay đó, $L^T$ sẽ xuất hiện:

| Đối xứng | $S = LDL^T = \begin{bmatrix} 1 & 0 & 0 \\ 4 & 1 & 0 \\ 5 & 1 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0 & -14 & 0 \\ 0 & 0 & -8 \end{bmatrix} \begin{bmatrix} 1 & 4 & 5 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}$ |
|-----------|---------------------------------------------------------------------------------|
|-----------|---------------------------------------------------------------------------------|

Ma trận $S$ này khả nghịch bởi vì *nó có ba phần tử xoay*. Nghịch đảo của nó là $(L^T)^{-1} D^{-1} L^{-1}$ và $S^{-1}$ cũng đối xứng. Các con số 14 và 8 sẽ xuất hiện ở mẫu số của $S^{-1}$. "Định thức" của $S$ là tích của các phần tử xoay $(1)(-14)(-8) = 112$.

**2.7 C** Đối với một ma trận chữ nhật $A$, *ma trận điểm yên ngựa (saddle-point matrix)* $S$ này là đối xứng và quan trọng:

| **Ma trận khối từ bình phương tối thiểu (least squares)** | $S = \begin{bmatrix} I & A \\ A^T & 0 \end{bmatrix} = S^T$ có kích thước $m + n$. |
|--------------------------------------------|-------------------------------------------------------------------------------|
|--------------------------------------------|-------------------------------------------------------------------------------|

Áp dụng phép khử khối để tìm một **phân tích nhân tử khối (block factorization)** $S = LDL^T$. Sau đó kiểm tra tính khả nghịch:

| $S$ khả nghịch | $\iff$ | $A^T A$ khả nghịch | $\iff$ | $Ax \neq 0$ bất cứ khi nào $x \neq 0$ |
|------------------------|--------|-----------------------|--------|---------------------------------|
|                        |        |                       |        |                                 |

**Lời giải** Phần tử xoay khối (block pivot) đầu tiên là $I$. Trừ $A^T$ nhân với hàng 1 khỏi hàng 2:

| Khử khối (Block elimination) | $S = \begin{bmatrix} I & A \\ A^T & 0 \end{bmatrix}$ | đi đến | $\begin{bmatrix} I & A \\ 0 & -A^T A \end{bmatrix}$ | Đây là $U$. |
|-------------------|------------------------------------------------------|---------|-----------------------------------------------------|---------------|
|-------------------|------------------------------------------------------|---------|-----------------------------------------------------|---------------|

Ma trận phần tử xoay khối $D$ chứa $I$ và $-A^T A$. Khi đó $L$ và $L^T$ chứa $A^T$ và $A$:

| Phân tích nhân tử khối | $S = LDL^T = \begin{bmatrix} I & 0 \\ A^T & I \end{bmatrix} \begin{bmatrix} I & 0 \\ 0 & -A^T A \end{bmatrix} \begin{bmatrix} I & A \\ 0 & I \end{bmatrix}$ |
|---------------------|--------------------------------------------------------------|
|                     |                                                              |

$L$ chắc chắn là khả nghịch, với các số 1 trên đường chéo. Nghịch đảo của ma trận ở giữa liên quan đến $(A^T A)^{-1}$. Mục 4.2 trả lời một câu hỏi quan trọng về ma trận $A^T A$:

**Khi nào thì $A^T A$ khả nghịch?** *Câu trả lời:* $A$ *phải có các cột độc lập tuyến tính.* **Khi đó** $Ax = 0$ **chỉ khi** $x = 0$. **Nếu không** $Ax = 0$ **sẽ dẫn đến** $A^T Ax = 0$.

### **Bài Tập 2.7 (Problem Set 2.7)**

**Các câu hỏi 1-7 là về các quy tắc cho ma trận chuyển vị.**

**1** Tìm $A^T$ và $A^{-1}$ và $(A^{-1})^T$ và $(A^T)^{-1}$ cho

$$A = \begin{bmatrix} 1 & 0 \\ 0 & 3 \end{bmatrix} \quad \text{và cũng cho} \quad A = \begin{bmatrix} 1 & c \\ c & 0 \end{bmatrix}.$$

**2** Xác minh rằng $(AB)^T$ bằng $B^T A^T$ nhưng chúng khác với $A^T B^T$:

| $A = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}$ | $B = \begin{bmatrix} 1 & 3 \\ 0 & 1 \end{bmatrix}$ | $AB = \begin{bmatrix} 1 & 3 \\ 2 & 7 \end{bmatrix}$ |
|----------------------------------------------------|----------------------------------------------------|-----------------------------------------------------|
|----------------------------------------------------|----------------------------------------------------|-----------------------------------------------------|

Chứng minh thêm rằng $AA^T$ khác với $A^T A$. Nhưng cả hai ma trận đó đều là

- **3** (a) Ma trận $((AB)^{-1})^T$ bắt nguồn từ $(A^{-1})^T$ và $(B^{-1})^T$. *Theo thứ tự nào?*
- (b) Nếu $U$ là ma trận tam giác trên thì $(U^{-1})^T$ là tam giác \_\_.
- **4** Chứng minh rằng $A^2 = 0$ là có thể xảy ra nhưng $A^T A = 0$ là không thể xảy ra (trừ khi $A =$ ma trận không).

**5** (a) Vectơ hàng $x^T$ nhân với $A$ nhân với cột $y$ tạo ra con số nào?

$$x^T A y = \begin{bmatrix} 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix} \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} = \underline{\hspace{1cm}}.$$

- (b) Đây là hàng $x^T A =$ \_\_ nhân với cột $y = (0, 1, 0)^T$.
- (c) Đây là hàng $x^T = \begin{bmatrix} 0 & 1 \end{bmatrix}$ nhân với cột $Ay =$ \_\_.
- **6** Chuyển vị của một ma trận khối $M = \begin{bmatrix} A & B \\ C & D \end{bmatrix}$ là $M^T =$ \_\_. Hãy kiểm tra một ví dụ. Dưới những điều kiện nào của $A, B, C, D$ thì ma trận khối là đối xứng?
- **7** Đúng hay sai:
  - (a) Ma trận khối $\begin{bmatrix} I & A \\ A & I \end{bmatrix}$ tự động là ma trận đối xứng.
  - (b) Nếu $A$ và $B$ đối xứng thì tích $AB$ của chúng đối xứng.
  - (c) Nếu $A$ không đối xứng thì $A^{-1}$ không đối xứng.
  - (d) Khi $A, B, C$ đối xứng, chuyển vị của $ABC$ là $CBA$.

#### **Các câu hỏi 8-15 là về các ma trận hoán vị.**

**8** Tại sao có $n!$ ma trận hoán vị cấp $n$?
**9** Nếu $P_1$ và $P_2$ là các ma trận hoán vị, thì $P_1 P_2$ cũng vậy. Nó vẫn có các hàng của $I$ theo một thứ tự nào đó. Hãy cho các ví dụ với $P_1 P_2 \neq P_2 P_1$ và $P_3 P_4 = P_4 P_3$.
**10** Có 12 phép hoán vị *"chẵn"* của $(1, 2, 3, 4)$, với một *số chẵn các phép hoán đổi*. Hai trong số đó là $(1, 2, 3, 4)$ không có sự hoán đổi nào và $(4, 3, 2, 1)$ với hai sự hoán đổi. Hãy liệt kê mười phép hoán vị còn lại. Thay vì viết từng ma trận $4 \times 4$, chỉ cần sắp xếp các con số.
**11** Phép hoán vị nào làm cho $PA$ thành ma trận tam giác trên? Những phép hoán vị nào làm cho $P_1 A P_2$ thành ma trận tam giác dưới? *Nhân $A$ ở bên phải với $P_2$ hoán đổi các* \_\_ *của A.*

$$A = \begin{bmatrix} 0 & 0 & 6 \\ 1 & 2 & 3 \\ 0 & 4 & 5 \end{bmatrix}$$

- **12** Giải thích tại sao tích vô hướng của $x$ và $y$ bằng tích vô hướng của $Px$ và $Py$. Khi đó $(Px)^T (Py) = x^T y$ cho chúng ta biết rằng $P^T P = I$ cho bất kỳ phép hoán vị nào. Với $x = (1, 2, 3)$ và $y = (1, 4, 2)$, hãy chọn $P$ để chứng minh rằng $Px \cdot y$ không phải lúc nào cũng bằng $x \cdot Py$.
- **13** (a) Tìm một ma trận hoán vị $3 \times 3$ với $P^3 = I$ (nhưng không phải $P = I$).
- (b) Tìm một phép hoán vị $P$ kích thước $4 \times 4$ với $P^4 \neq I$.
- **14** Nếu $P$ có các số 1 trên đường chéo phụ (antidiagonal) từ $(1, n)$ đến $(n, 1)$, hãy mô tả $PAP$. Lưu ý $P = P^T$.

- **15** Tất cả các ma trận hoán đổi hàng đều đối xứng: $P^T = P$. Khi đó $P^T P = I$ trở thành $P^2 = I$. Các ma trận hoán vị khác có thể đối xứng hoặc không đối xứng.
  - (a) Nếu $P$ đưa hàng 1 đến hàng 4, thì $P^T$ đưa hàng \_\_ đến hàng \_\_. Khi $P^T = P$, các phép hoán đổi hàng đi thành từng cặp và không chồng chéo nhau.
  - (b) Tìm một ví dụ $4 \times 4$ với $P^T = P$ làm di chuyển cả bốn hàng.

**Các câu hỏi 16-21 là về các ma trận đối xứng và phân tích nhân tử của chúng.**

- **16** Nếu $A = A^T$ và $B = B^T$, ma trận nào trong số những ma trận này chắc chắn đối xứng?
- (a) $A^2 - B^2$ (b) $(A + B)(A - B)$ (c) $ABA$ (d) $ABAB$.
- **17** Tìm các ma trận đối xứng $2 \times 2$ $S = S^T$ với những tính chất sau:
  - (a) $S$ không khả nghịch.
  - (b) $S$ khả nghịch nhưng không thể phân tích thành $LU$ (cần có hoán đổi hàng).
  - (c) $S$ có thể phân tích thành $LDL^T$ nhưng không thể thành $LL^T$ (do $D$ có số âm).
- **18** (a) Có bao nhiêu phần tử của $S$ có thể được chọn một cách độc lập, nếu $S = S^T$ có kích thước $5 \times 5$?
- (b) Bằng cách nào $L$ và $D$ (vẫn là $5 \times 5$) mang lại cùng một số lượng sự lựa chọn trong $LDL^T$?
- (c) Có bao nhiêu phần tử có thể được chọn nếu $A$ là *phản đối xứng (skew-symmetric)*? $(A^T = -A)$.
- **19** Giả sử $A$ là ma trận chữ nhật ($m \times n$) và $S$ là ma trận đối xứng ($m \times m$).
  - (a) Chuyển vị $A^T SA$ để chứng minh tính đối xứng của nó. Hình dạng (kích thước) của ma trận này là gì?
- (b) Chứng minh tại sao $A^T A$ không có số âm nào trên đường chéo của nó.
- **20** Phân tích nhân tử các ma trận đối xứng này thành $S = LDL^T$. Ma trận phần tử xoay $D$ là ma trận đường chéo:

| $S = \begin{bmatrix} 1 & 3 \\ 3 & 2 \end{bmatrix}$ | và | $S = \begin{bmatrix} 1 & b \\ b & c \end{bmatrix}$ | và | $S = \begin{bmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{bmatrix}$ |
|----------------------------------------------------|-----|----------------------------------------------------|-----|-----------------------------------------------------------------------------|
|----------------------------------------------------|-----|----------------------------------------------------|-----|-----------------------------------------------------------------------------|

**21** Sau khi phép khử làm sạch cột 1 bên dưới phần tử xoay đầu tiên, hãy tìm ma trận đối xứng $2 \times 2$ xuất hiện ở góc dưới bên phải:

| Bắt đầu từ $S =$ | $\begin{bmatrix} 2 & 4 & 8 \\ 4 & 3 & 9 \\ 8 & 9 & 0 \end{bmatrix}$ | và | $S =$ | $\begin{bmatrix} 1 & b & c \\ b & d & e \\ c & e & f \end{bmatrix}$ |
|------------------|---------------------------------------------------------------------|-----|-------|---------------------------------------------------------------------|
|                  |                                                                     |     |       |                                                                     |

**Các câu hỏi 22-24 là về các phân tích nhân tử** $PA = LU$ **và** $A = L_1 P_1 U_1$.

**22** Tìm các phân tích nhân tử $PA = LU$ (và kiểm tra chúng) cho ma trận $A$.

**23** Tìm một ma trận hoán vị $4 \times 4$ (gọi nó là $A$) cần 3 phép hoán đổi hàng để đi đến kết thúc của phép khử. Đối với ma trận này, các nhân tử $P, L$, và $U$ của nó là gì?
**24** Phân tích ma trận sau thành $PA = LU$. Đồng thời phân tích nó thành $A = L_1 P_1 U_1$ (giữ lại phép hoán đổi hàng 3 cho đến khi 3 lần hàng 1 được trừ khỏi hàng 2):

$$A = \begin{bmatrix} 0 & 1 & 2 \\ 0 & 3 & 8 \\ 2 & 1 & 1 \end{bmatrix}.$$

**25** Chứng minh rằng ma trận đơn vị không thể là tích của ba phép hoán đổi hàng (hoặc năm). Nó có thể là tích của hai phép hoán đổi (hoặc bốn).

**26** (a) Chọn $E_{21}$ để loại bỏ số 3 bên dưới phần tử xoay đầu tiên. Sau đó nhân $E_{21} S E_{21}^T$ để loại bỏ cả hai số 3:

| $A = \begin{bmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 2 & 3 & 4 \end{bmatrix}$ | và | $A = \begin{bmatrix} 1 & 2 & 0 \\ 2 & 4 & 1 \\ 1 & 1 & 1 \end{bmatrix}$ |
|-------------------------------------------------------------------------|-----|-------------------------------------------------------------------------|
|-------------------------------------------------------------------------|-----|-------------------------------------------------------------------------|

| $S = \begin{bmatrix} 1 & 3 & 0 \\ 3 & 11 & 4 \\ 0 & 4 & 9 \end{bmatrix}$ | đang tiến về | $D = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ |
|--------------------------------------------------------------------------|-----------------|-------------------------------------------------------------------------|
|--------------------------------------------------------------------------|-----------------|-------------------------------------------------------------------------|

- (b) Chọn $E_{32}$ để loại bỏ số 4 bên dưới phần tử xoay thứ hai. Sau đó $S$ được rút gọn thành $D$ bởi $E_{32} E_{21} S E_{21}^T E_{32}^T = D$. Nghịch đảo các $E$ để tìm $L$ trong $S = LDL^T$.
- **27** Nếu mỗi hàng của một ma trận $4 \times 4$ chứa các số 0, 1, 2, 3 theo một thứ tự nào đó, ma trận đó có thể đối xứng không?
- **28** Chứng minh rằng không có sự sắp xếp lại hàng và sắp xếp lại cột nào có thể chuyển vị một ma trận thông thường. (Hãy chú ý các phần tử trên đường chéo.)

**Ba câu hỏi tiếp theo là về các ứng dụng của đồng nhất thức** $(Ax)^T y = x^T (A^T y)$.

**29** Các đường dây dẫn điện đi giữa Boston, Chicago, và Seattle. Những thành phố này ở các điện áp $x_B, x_C, x_S$. Với các điện trở đơn vị giữa các thành phố, các dòng điện giữa các thành phố nằm trong $y$:

$$y = Ax \quad \text{là} \quad \begin{bmatrix} y_{BC} \\ y_{CS} \\ y_{BS} \end{bmatrix} = \begin{bmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \\ 1 & 0 & -1 \end{bmatrix} \begin{bmatrix} x_B \\ x_C \\ x_S \end{bmatrix}.$$

- (a) Tìm tổng các dòng điện $A^T y$ đi ra khỏi ba thành phố.
- (b) Xác minh rằng $(Ax)^T y$ phù hợp với $x^T (A^T y)$ - sáu số hạng ở cả hai.

**30** Việc sản xuất $x_1$ xe tải và $x_2$ máy bay cần $x_1 + 50x_2$ tấn thép, $40x_1 + 1000x_2$ pound cao su, và $2x_1 + 50x_2$ tháng lao động. Nếu chi phí đơn vị $y_1, y_2, y_3$ là \$700 cho một tấn, \$3 cho một pound, và \$3000 cho một tháng, thì giá trị của một xe tải và một máy bay là bao nhiêu? Đó là các thành phần của $A^T y$.
**31** $Ax$ cho biết lượng thép, cao su, và lao động để sản xuất $x$ trong Bài 30. Tìm $A$. Khi đó $Ax \cdot y$ là \_\_ của các đầu vào trong khi $x \cdot A^T y$ là giá trị của \_\_.
**32** Ma trận $P$ nhân với $(x, y, z)$ để cho ra $(z, x, y)$ cũng là một ma trận quay. Tìm $P$ và $P^3$. Trục quay $a = (1, 1, 1)$ không di chuyển, nó bằng $Pa$. Góc quay từ $v = (2, 3, -5)$ đến $Pv = (-5, 2, 3)$ là bao nhiêu?
**33** Viết $A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ như là tích $ES$ của một ma trận thao tác hàng cơ sở $E$ và một ma trận đối xứng $S$.
**34** Đây là một phân tích nhân tử mới của $A$ thành $LS$: *tam giác dưới* (với các số 1) *nhân với đối xứng:*

Bắt đầu từ $A = LDU$. Khi đó $A$ bằng $L(U^T)^{-1}$ nhân với $S = U^T DU$.

Tại sao $L(U^T)^{-1}$ là ma trận tam giác dưới? Đường chéo của nó toàn số 1. Tại sao $U^T DU$ đối xứng?

**35** Một *nhóm (group)* các ma trận bao gồm $AB$ và $A^{-1}$ nếu nó bao gồm $A$ và $B$. "Tích và nghịch đảo vẫn nằm trong nhóm." Những tập hợp nào sau đây là các nhóm? Các ma trận tam giác dưới $L$ với các số 1 trên đường chéo, các ma trận đối xứng $S$, các ma trận dương $M$, các ma trận đường chéo khả nghịch $D$, các ma trận hoán vị $P$, các ma trận có $Q^T = Q^{-1}$. *Hãy phát minh ra thêm hai nhóm ma trận nữa.*

### **Các Bài Toán Thử Thách (Challenge Problems)**

- **36** Một ma trận vuông *Tây Bắc (northwest matrix)* $B$ bằng không ở góc Đông Nam, bên dưới đường chéo phụ kết nối $(1, n)$ tới $(n, 1)$. Liệu $B^T$ và $B^2$ có phải là ma trận Tây Bắc không? Liệu $B^{-1}$ sẽ là ma trận Tây Bắc hay Đông Nam? Hình dạng của $BC =$ *Tây Bắc nhân Đông Nam* là gì?
- **37** Nếu bạn lấy các lũy thừa của một ma trận hoán vị, tại sao một số $P^k$ cuối cùng sẽ bằng $I$? Tìm một phép hoán vị $P$ kích thước $5 \times 5$ sao cho lũy thừa nhỏ nhất để bằng $I$ là $P^6$.
- **38** (a) Viết ra bất kỳ ma trận $3 \times 3$ $M$ nào. Tách $M$ thành $S + A$ trong đó $S = S^T$ là đối xứng và $A = -A^T$ là phản đối xứng (anti-symmetric).
- (b) Tìm các công thức cho $S$ và $A$ liên quan đến $M$ và $M^T$. Chúng ta muốn $M = S + A$.
- **39** Giả sử $Q^T$ bằng $Q^{-1}$ (chuyển vị bằng nghịch đảo, vì vậy $Q^T Q = I$).
  - (a) Chứng minh rằng các cột $q_1, \dots, q_n$ là các vectơ đơn vị: $\|q_i\|^2 = 1$.
  - (b) Chứng minh rằng cứ hai cột bất kỳ của $Q$ thì vuông góc với nhau: $q_1^T q_2 = 0$.
  - (c) Tìm một ví dụ $2 \times 2$ với phần tử đầu tiên $q_{11} = \cos \theta$.

# **Chuyển Vị của Đạo Hàm (The Transpose of a Derivative)**

Bạn có cho phép tôi sử dụng một chút vi tích phân không? Nó vô cùng quan trọng nếu không thì tôi đã không rời khỏi đại số tuyến tính. (Đây thực sự là đại số tuyến tính cho các hàm số $x(t)$.) **Ma trận thay đổi thành một đạo hàm** nên $A = d/dt$. Để tìm chuyển vị của ma trận $A$ bất thường này, chúng ta cần định nghĩa tích vô hướng giữa hai hàm số $x(t)$ và $y(t)$.

Tích vô hướng thay đổi từ tổng của $x_k y_k$ thành *tích phân* của $x(t)y(t)$.

| Tích trong của các hàm số | $x^T y = (x, y) = \int_{-\infty}^{\infty} x(t) y(t) dt$ |
|----------------------------|---------------------------------------------------------|
|----------------------------|---------------------------------------------------------|

Từ tích trong này chúng ta biết yêu cầu đối với $A^T$. Từ "adjoint" (liên hợp) đúng hơn từ "transpose" (chuyển vị) khi chúng ta đang làm việc với các đạo hàm.

Chuyển vị của một ma trận có $(Ax)^T y = x^T (A^T y)$. Liên hợp (adjoint) của $A = \frac{d}{dt}$ có

$$(Ax, y) = \int_{-\infty}^{\infty} \frac{dx}{dt} y(t) dt = \int_{-\infty}^{\infty} x(t) \left( -\frac{dy}{dt} \right) dt = (x, A^T y)$$

*Tôi hy vọng bạn nhận ra tích phân từng phần.* Đạo hàm di chuyển từ hàm số thứ nhất $x(t)$ sang hàm số thứ hai $y(t)$. Trong quá trình di chuyển đó, một dấu trừ xuất hiện. Điều này cho chúng ta biết rằng *chuyển vị của đạo hàm là âm đạo hàm.*

Đạo hàm là *phản đối xứng (antisymmetric): A = d/dt và A^T = -d/dt.* Các ma trận đối xứng có $S^T = S$, các ma trận phản đối xứng có $A^T = -A$. Đại số tuyến tính bao gồm cả đạo hàm và tích phân trong Chương 8, *bởi vì cả hai đều là tuyến tính.*

Tính phản đối xứng này của đạo hàm cũng áp dụng cho các ma trận sai phân trung tâm (centered difference matrices).

$$A = \begin{bmatrix} 0 & 1 & 0 & 0 \\ -1 & 0 & 1 & 0 \\ 0 & -1 & 0 & 1 \\ 0 & 0 & -1 & 0 \end{bmatrix} \quad \text{chuyển vị thành} \quad A^T = \begin{bmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & -1 & 0 \\ 0 & 1 & 0 & -1 \\ 0 & 0 & 1 & 0 \end{bmatrix} = -A.$$

Và một ma trận sai phân tiến (forward difference matrix) chuyển vị thành một ma trận sai phân lùi (backward difference matrix), *nhân với -1*. Trong các phương trình vi phân, đạo hàm bậc hai (gia tốc) là đối xứng. Đạo hàm bậc nhất (sự cản tỷ lệ thuận với vận tốc) là *phản đối xứng*.
