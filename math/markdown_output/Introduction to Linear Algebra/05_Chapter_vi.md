# **Chương 5**

# **Định Thức (Determinants)**

**1** Định thức (determinant) của $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ là $ad - bc$. Ma trận suy biến (singular matrix) $A = \begin{bmatrix} a & b \\ a & b \end{bmatrix}$ có định thức = $\mathbf{0}$.
**2** Hoán vị hàng (Row exchange) $PA = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} a & b \\ c & d \end{bmatrix} = \begin{bmatrix} c & d \\ a & b \end{bmatrix}$ có $\det PA = bc - ad = -\det A$. **đảo dấu (reverses signs)**
**3** Định thức của $\begin{bmatrix} xa + yA & xb + yB \\ c & d \end{bmatrix}$ là $x(ad - bc) + y(Ad - Bc)$. **Định thức tuyến tính theo riêng từng hàng.**
**4** Phép khử (Elimination) $EA = \begin{bmatrix} 1 & 0 \\ -c/a & 1 \end{bmatrix} \begin{bmatrix} a & b \\ c & d \end{bmatrix} = \begin{bmatrix} a & b \\ 0 & d - \frac{c}{a}b \end{bmatrix}$. $\det EA = a(d - \frac{c}{a}b) = ad - bc = \det A$. **tích của các phần tử chốt (pivots) =** $\det A$.
**5** Nếu $A$ có kích thước $n \times n$ thì 1, 2, 3, 4 vẫn đúng: $\det = \mathbf{0}$ khi $A$ là ma trận suy biến, **det đảo dấu** khi các hàng được hoán đổi, det **tuyến tính theo riêng một hàng bất kỳ**, $\det = $ **tích của các phần tử chốt**. Luôn có $\det BA = (\det B)(\det A)$ và $\det A^T = \det A$. Đây là một con số đáng kinh ngạc.

# **5.1 Các Tính Chất Của Định Thức (The Properties of Determinants)**

Định thức của một ma trận vuông là một con số duy nhất. Con số đó chứa một lượng thông tin đáng kinh ngạc về ma trận. Nó cho biết ngay lập tức ma trận đó có khả nghịch hay không. *Định thức bằng không khi ma trận không có nghịch đảo.* Khi $A$ khả nghịch, định thức của $A^{-1}$ là $1/(\det A)$. **Nếu** $\det A = 2$ thì $\det A^{-1} = 1/2$. Thực tế, định thức dẫn đến một công thức cho mọi phần tử trong $A^{-1}$.

Đây là một cách sử dụng định thức - để tìm các công thức cho các ma trận nghịch đảo và các phần tử chốt (pivots) và các nghiệm $A^{-1}b$. Đối với một ma trận lớn, chúng ta hiếm khi sử dụng các công thức đó, bởi vì phép khử nhanh hơn. Đối với một ma trận $2 \times 2$ với các phần tử $a, b, c, d$, định thức của nó là $ad - bc$ cho thấy $A^{-1}$ thay đổi như thế nào khi $A$ thay đổi. Chú ý phép chia cho định thức!

$$A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \quad \text{có nghịch đảo} \quad A^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}. \quad (1)$$

Nhân các ma trận đó để có được $I$. Khi định thức $ad - bc = 0$, chúng ta được yêu cầu chia cho không và chúng ta không thể - khi đó $A$ không có nghịch đảo. (Các hàng song song với nhau khi $a/c = b/d$. Điều này cho $ad = bc$ và $\det A = 0$.) Các hàng phụ thuộc tuyến tính luôn dẫn đến $\det A = 0$.

Định thức cũng liên quan đến các phần tử chốt (pivots). Đối với một ma trận $2 \times 2$, các phần tử chốt là $a$ và $d - (c/a)b$. *Tích của các phần tử chốt là định thức:*

| Tích của các phần tử chốt | $a\left(d - \frac{b}{a}\right) = ad - bc$ | tức là | $\det$. |
|-------------------|-------------------------------------------|----------|------|

Sau một phép hoán vị hàng, các phần tử chốt thay đổi thành $c$ và $b - (a/c)d$. Các phần tử chốt mới đó nhân với nhau để ra $bc - ad$. Phép hoán vị hàng thành $\left[\begin{smallmatrix} c & d \\ a & b \end{smallmatrix}\right]$ đã đảo ngược dấu của định thức.

*Nhìn về phía trước (Looking ahead)* Định thức của một ma trận $n \times n$ có thể được tìm theo ba cách:

1 Nhân $n$ phần tử chốt (với $1$ hoặc $-1$) 
2 Cộng $n!$ số hạng (nhân với $1$ hoặc $-1$) 
3 Kết hợp $n$ định thức nhỏ hơn (nhân với $1$ hoặc $-1$) 

Đây là **công thức phần tử chốt (pivot formula).**
Đây là **"công thức lớn" ("big" formula).**
Đây là **công thức phần phụ đại số (cofactor formula).**

Bạn thấy rằng *các dấu cộng hoặc trừ* - các quyết định giữa $1$ và $-1$ - đóng một vai trò lớn trong các định thức. Điều đó xuất phát từ quy tắc sau cho các ma trận $n \times n$:

### *Định thức đổi dấu khi hai hàng (hoặc hai cột) được hoán đổi.*

Ma trận đơn vị có định thức $+1$. Hoán đổi hai hàng và $\det P = -1$. Hoán đổi thêm hai hàng nữa và hoán vị mới có $\det P = +1$. Một nửa trong tất cả các hoán vị là *chẵn (even)* ($\det P = 1$) và một nửa là *lẻ (odd)* ($\det P = -1$). Bắt đầu từ $I$, một nửa các $P$ bao gồm số chẵn các phép hoán đổi và một nửa yêu cầu một số lẻ. Trong trường hợp $2 \times 2$, $ad$ có dấu cộng và $bc$ có dấu trừ - xuất phát từ phép hoán vị hàng:

| $\det \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = 1$ | và | $\det \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} = -1.$ |
|---------------------------------------------------------|-----|-----------------------------------------------------------|

Quy tắc thiết yếu khác là tính tuyến tính - nhưng trước tiên có một cảnh báo. Tuyến tính không có nghĩa là $\det(A + B) = \det A + \det B$. *Điều này hoàn toàn sai.* Loại tuyến tính đó thậm chí không đúng khi $A = I$ và $B = I$. Quy tắc sai sẽ nói rằng $\det(I + I) = 1 + 1 = 2$. Quy tắc đúng là $\det(2I) = 2^n$. Định thức được nhân với $2^n$ (không chỉ là $2$) khi các ma trận được nhân với $2$.

Chúng ta không định định nghĩa định thức bằng các công thức của nó. Tốt hơn là bắt đầu với các tính chất của nó - *đảo dấu và tính tuyến tính*. Các tính chất này rất đơn giản (Phần 5.1). Chúng chuẩn bị cho các công thức (Phần 5.2). Sau đó đến các ứng dụng, bao gồm ba điều này:

**1.** Định thức cung cấp $A^{-1}$ và $A^{-1}b$ (công thức này được gọi là **Quy tắc Cramer (Cramer's Rule)**).
**2.** Khi các cạnh của một hình hộp là các hàng của $A$, **thể tích (volume)** là $|\det A|$.
**3.** Đối với $n$ con số đặc biệt $\lambda$ được gọi là **trị riêng (eigenvalues)**, định thức của $A - \lambda I$ bằng không. Đây là một ứng dụng thực sự quan trọng và nó chiếm trọn Chương 6.

## Các Tính Chất Của Định Thức

Định thức có ba tính chất cơ bản (quy tắc 1, 2, 3). Bằng cách sử dụng những quy tắc đó, chúng ta có thể tính định thức của bất kỳ ma trận vuông $A$ nào. ***Con số này được viết theo hai cách, $\det A$ và $|A|$.*** Chú ý: Dấu ngoặc vuông cho ma trận, thanh thẳng (bars) cho định thức của nó. Khi $A$ là ma trận $2 \times 2$, các quy tắc 1, 2, 3 dẫn đến kết quả chúng ta mong đợi:

$$\text{Định thức của } \begin{bmatrix} a & b \\ c & d \end{bmatrix} \text{ là } \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc.$$

Từ các quy tắc 1–3 chúng ta sẽ đạt tới các quy tắc 4–10. Hai quy tắc cuối cùng là $\det(AB) = (\det A)(\det B)$ và $\det A^T = \det A$. Chúng ta sẽ kiểm tra tất cả các quy tắc bằng công thức $2 \times 2$, nhưng đừng quên: Các quy tắc áp dụng cho mọi ma trận $A$ kích thước $n \times n$.

Quy tắc 1 (dễ nhất) khớp $\det I = 1$ với thể tích = 1 của một khối lập phương đơn vị.

**1** *Định thức của ma trận đơn vị $n \times n$ là 1.*

$$\begin{vmatrix} 1 & 0 \\ 0 & 1 \end{vmatrix} = 1 \quad \text{và} \quad \begin{vmatrix} 1 & & \\ & \ddots & \\ & & 1 \end{vmatrix} = 1.$$

**2** *Định thức đổi dấu khi hai hàng được hoán đổi* (đảo dấu):

$$\text{Kiểm tra: } \begin{vmatrix} c & d \\ a & b \end{vmatrix} = - \begin{vmatrix} a & b \\ c & d \end{vmatrix} \quad (\text{cả hai vế đều bằng } bc - ad).$$

Nhờ quy tắc này, chúng ta có thể tìm $\det P$ cho mọi ma trận hoán vị. Chỉ cần hoán đổi các hàng của $I$ cho đến khi bạn đạt tới $P$. Khi đó $\det P = +1$ cho một số ***chẵn (even)*** các phép hoán đổi hàng và $\det P = -1$ cho một số ***lẻ (odd)***.

Quy tắc thứ ba phải tạo ra một bước nhảy lớn tới định thức của mọi ma trận.

**3** *Định thức là một hàm tuyến tính đối với từng hàng riêng biệt* (tất cả các hàng khác giữ cố định). Nếu hàng đầu tiên được nhân với $t$, định thức được nhân với $t$. Nếu các hàng đầu tiên được cộng lại, các định thức được cộng lại. Quy tắc này chỉ áp dụng khi các hàng khác không thay đổi! Chú ý $c$ và $d$ giữ nguyên như thế nào:

![](images/_page_258_Figure_34.jpeg)

Trong trường hợp đầu tiên, cả hai vế đều là $tad - tbc$. Sau đó đưa $t$ ra ngoài làm nhân tử. Trong trường hợp thứ hai, cả hai vế đều là $ad + a'd - bc - b'c$. Những quy tắc này vẫn áp dụng khi $A$ là $n \times n$, và ***một hàng thay đổi***.

$$A = \begin{vmatrix} 4 & 8 & 8 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{vmatrix} = 4 \begin{vmatrix} 1 & 2 & 2 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{vmatrix} \quad \text{và} \quad \begin{vmatrix} 4 & 8 & 8 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{vmatrix} = \begin{vmatrix} 4 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{vmatrix} + \begin{vmatrix} 0 & 8 & 8 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{vmatrix}.$$

Kết hợp phép nhân và phép cộng, chúng ta thu được *bất kỳ tổ hợp tuyến tính nào trong một hàng*. Quy tắc 2 cho các phép hoán đổi hàng có thể đưa hàng đó lên hàng đầu tiên và đưa trở lại.

Quy tắc này không có nghĩa là $\det(2I) = 2 \det I$. Để thu được $2I$ chúng ta phải nhân *cả hai* hàng với $2$, và nhân tử $2$ được đưa ra ngoài hai lần:

$$\begin{vmatrix} 2 & 0 \\ 0 & 2 \end{vmatrix} = 2^2 = 4 \quad \text{và} \quad \begin{vmatrix} t & 0 \\ 0 & t \end{vmatrix} = t^2.$$

Điều này giống hệt như diện tích và thể tích. Mở rộng một hình chữ nhật lên gấp $2$ và diện tích của nó tăng lên gấp $4$. Mở rộng một hình hộp $n$ chiều lên gấp $t$ và thể tích của nó tăng lên $t^n$. Mối liên hệ này không phải là ngẫu nhiên — chúng ta sẽ thấy *định thức bằng với thể tích* như thế nào.

Hãy đặc biệt chú ý đến các quy tắc 1–3. Chúng hoàn toàn xác định con số $\det A$. Chúng ta có thể dừng lại ở đây để tìm một công thức cho các định thức $n \times n$ (hơi phức tạp). Chúng ta thích đi dần dần hơn, bởi vì các quy tắc 4–10 làm cho định thức dễ làm việc hơn nhiều.

#### **4 Nếu hai hàng của $A$ bằng nhau, thì $\det A = 0$.**

**Các hàng bằng nhau (Equal rows)**

$$\text{Kiểm tra } 2 \times 2 : \begin{vmatrix} a & b \\ a & b \end{vmatrix} = 0.$$

Quy tắc 4 suy ra từ quy tắc 2. (Hãy nhớ rằng chúng ta phải sử dụng các quy tắc chứ không phải công thức $2 \times 2$.) *Hoán đổi hai hàng bằng nhau*. Định thức $D$ đáng lẽ phải đổi dấu. Nhưng $D$ cũng phải giữ nguyên, bởi vì ma trận không thay đổi. Con số duy nhất với $-D = D$ là $D = 0$ — đây phải là định thức. (Lưu ý: Trong đại số Boolean, lập luận này thất bại, bởi vì $-1 = 1$. Khi đó $D$ được định nghĩa bằng các quy tắc 1, 3, 4.)

Một ma trận có hai hàng bằng nhau thì không có nghịch đảo. Quy tắc 4 làm cho $\det A = 0$. Nhưng các ma trận có thể suy biến và định thức có thể bằng không mà không có các hàng bằng nhau! Quy tắc 5 sẽ là chìa khóa. Chúng ta có thể thực hiện các phép toán hàng (giống như phép khử) mà không làm thay đổi $\det A$.

#### **5 Trừ đi một bội số của một hàng từ một hàng khác giữ nguyên $\det A$.**

**$\ell$ nhân với hàng 1 trừ đi từ hàng 2**

$$\begin{vmatrix} a & b \\ c - \ell a & d - \ell b \end{vmatrix} = \begin{vmatrix} a & b \\ c & d \end{vmatrix}.$$

Quy tắc 3 (tuyến tính) tách vế trái thành vế phải cộng với một số hạng khác $-\ell \begin{vmatrix} a & b \\ a & b \end{vmatrix}$. Số hạng phụ này bằng không theo quy tắc 4: các hàng bằng nhau. Do đó quy tắc 5 là đúng (không chỉ cho $2 \times 2$).

**Kết luận** *Định thức không bị thay đổi bởi các bước khử thông thường từ $A$ thành $U$.* Vì vậy $\det A$ bằng $\det U$. Nếu chúng ta có thể tìm định thức của các ma trận tam giác $U$, chúng ta có thể tìm định thức của tất cả các ma trận $A$. Mỗi lần hoán vị hàng sẽ đảo dấu, do đó luôn có $\det A = \pm \det U$. Quy tắc 5 đã thu hẹp vấn đề về các ma trận tam giác.

#### **6 Một ma trận có một hàng gồm toàn các số không thì $\det A = 0$.**

**Hàng toàn số không (Row of zeros)**

$$\begin{vmatrix} 0 & 0 \\ c & d \end{vmatrix} = 0 \quad \text{và} \quad \begin{vmatrix} a & b \\ 0 & 0 \end{vmatrix} = 0.$$

Để chứng minh dễ dàng, cộng một hàng khác nào đó vào hàng số không. Định thức không bị thay đổi (quy tắc 5). Nhưng ma trận bây giờ có hai hàng bằng nhau. Vì vậy $\det A = 0$ theo quy tắc 4.

**7 Nếu $A$ là ma trận tam giác thì $\det A = a_{11}a_{22} \cdots a_{nn} =$ tích các phần tử trên đường chéo.**

**Tam giác (Triangular)** 
$$\begin{vmatrix} a & b \\ 0 & d \end{vmatrix} = ad \quad \text{và cũng có} \quad \begin{vmatrix} a & 0 \\ c & d \end{vmatrix} = ad.$$

Giả sử tất cả các phần tử trên đường chéo đều khác không. Khử các phần tử ngoài đường chéo bằng phép khử! (Nếu $A$ là ma trận tam giác dưới, hãy trừ các bội số của từng hàng khỏi các hàng thấp hơn. Nếu $A$ là ma trận tam giác trên, hãy trừ khỏi các hàng cao hơn.) Theo quy tắc 5, định thức không thay đổi — và bây giờ ma trận là ma trận đường chéo:

**Ma trận đường chéo (Diagonal matrix)** 
$$\det \begin{bmatrix} a_{11} & & & 0 \\ & a_{22} & & \\ & & \ddots & \\ 0 & & & a_{nn} \end{bmatrix} = (a_{11})(a_{22}) \cdots (a_{nn}).$$

Đưa $a_{11}$ ra ngoài làm nhân tử từ hàng đầu tiên theo quy tắc 3. Sau đó đưa $a_{22}$ ra ngoài từ hàng thứ hai. Cuối cùng đưa $a_{nn}$ ra ngoài từ hàng cuối cùng. Định thức là $a_{11}$ nhân với $a_{22}$ nhân với $\dots$ nhân với $a_{nn}$ nhân với $\det I$. Sau đó quy tắc 1 (được sử dụng cuối cùng!) là $\det I = 1$.

Điều gì xảy ra nếu một phần tử trên đường chéo $a_{ii}$ bằng không? Khi đó ma trận tam giác $A$ là suy biến. Phép khử tạo ra một hàng toàn các số không. Theo quy tắc 5, định thức không thay đổi, và theo quy tắc 6 một hàng toàn số không có nghĩa là $\det A = 0$. Chúng ta đạt tới bài kiểm tra tuyệt vời cho các ma trận **suy biến (singular)** hoặc **khả nghịch (invertible)**.

**8 Nếu $A$ là ma trận suy biến thì $\det A = 0$. Nếu $A$ là ma trận khả nghịch thì $\det A \neq 0$.**

**Suy biến (Singular)** 
$$\begin{bmatrix} a & b \\ c & d \end{bmatrix} \quad \text{suy biến khi và chỉ khi} \quad ad - bc = 0.$$

**Chứng minh** Phép khử đi từ $A$ đến $U$. Nếu $A$ suy biến thì $U$ có một hàng số không. Các quy tắc cho $\det A = \det U = 0$. Nếu $A$ khả nghịch thì $U$ có các phần tử chốt dọc theo đường chéo của nó. Tích của các phần tử chốt khác không (sử dụng quy tắc 7) cho một định thức khác không:

**Nhân các phần tử chốt (Multiply pivots)** 
$$\det A = \pm \det U = \pm (\text{tích của các phần tử chốt}). \quad (2)$$

Các phần tử chốt của một ma trận $2 \times 2$ (nếu $a \neq 0$) là $a$ và $d - (c/a)b$:

**Định thức là** 
$$\begin{vmatrix} a & b \\ c & d \end{vmatrix} = \begin{vmatrix} a & b \\ 0 & d - (c/a)b \end{vmatrix} = ad - bc.$$

*Đây là công thức đầu tiên cho định thức.* MATLAB nhân các phần tử chốt để tìm $\det A$. Dấu trong $\pm \det U$ phụ thuộc vào việc số lần hoán vị hàng là chẵn hay lẻ: $+1$ hoặc $-1$ là định thức của phép hoán vị $P$ đã hoán đổi các hàng.

Khi không có phép hoán vị hàng, $P = I$ và $\det A = \det U = \text{tích của các phần tử chốt}$. Và $\det L = 1$:

| Quy tắc nhân (Product rule) | $\begin{vmatrix} a & b \\ c & d \end{vmatrix} \begin{vmatrix} p & q \\ r & s \end{vmatrix} = \begin{vmatrix} ap + br & aq + bs \\ cp + dr & cq + ds \end{vmatrix}$ |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Khi ma trận $B$ là $A^{-1}$, quy tắc này nói rằng định thức của $A^{-1}$ là $1 / \det A$:

| $A$ nhân với $A^{-1}$ | $AA^{-1} = I$ | suy ra | $(\det A)(\det A^{-1}) = \det I = 1$ . |
|--------------------|---------------|-----|----------------------------------------|

Quy tắc nhân này là quy tắc phức tạp nhất từ trước đến nay. Thậm chí trường hợp $2 \times 2$ cũng cần một chút đại số:

$$|A| |B| = (ad - bc)(ps - qr) = (ap + br)(cq + ds) - (aq + bs)(cp + dr) = |AB|.$$

Đối với trường hợp $n \times n$, đây là một chứng minh gọn gàng rằng $|AB| = |A| |B|$. Khi $|B|$ khác không, hãy xem xét tỷ số $D(A) = |AB|/|B|$. *Kiểm tra xem tỷ số $D(A)$ này có các tính chất 1, 2, 3 hay không.* Khi đó $D(A)$ phải là định thức và chúng ta có $|AB|/|B| = |A|$. Tuyệt vời.

*Tính chất 1 (Định thức của $I$)* Nếu $A = I$ thì tỷ số $D(A)$ trở thành $|B|/|B| = 1$.

*Tính chất 2 (Đảo dấu)* Khi hai hàng của $A$ được hoán đổi, thì hai hàng tương ứng của $AB$ cũng được hoán đổi. Do đó $|AB|$ đổi dấu và tỷ số $|AB|/|B|$ cũng vậy.

*Tính chất 3 (Tuyến tính)* Khi hàng 1 của $A$ được nhân với $t$, thì hàng 1 của $AB$ cũng vậy. Điều này nhân định thức $|AB|$ với $t$. Vì vậy tỷ số $|AB|/|B|$ được nhân với $t$.

Cộng hàng 1 của $A$ vào hàng 1 của $A'$. Khi đó hàng 1 của $AB$ cộng vào hàng 1 của $A'B$. Theo quy tắc 3, các định thức được cộng lại. Sau khi chia cho $|B|$, các tỷ số được cộng lại - đúng như mong muốn.

*Kết luận* Tỷ số $|AB|/|B|$ này có cùng ba tính chất dùng để định nghĩa $|A|$. Do đó nó bằng $|A|$. Điều này chứng minh quy tắc nhân $|AB| = |A||B|$. Trường hợp $|B| = 0$ là riêng biệt và dễ dàng, bởi vì $AB$ suy biến khi $B$ suy biến. Khi đó $|AB| = |A||B|$ là $0 = 0$.

**10** *Chuyển vị $A^T$ có cùng định thức với $A$.*

| Chuyển vị (Transpose) | $\begin{vmatrix} a & b \\ c & d \end{vmatrix} = \begin{vmatrix} a & c \\ b & d \end{vmatrix}$ | vì cả hai vế đều bằng | $ad - bc$ . |
|-----------|-----------------------------------------------------------------------------------------------|------------------------|-------------|

Phương trình $|A^T| = |A|$ trở thành $0 = 0$ khi $A$ suy biến (chúng ta biết rằng $A^T$ cũng suy biến). Nếu không, $A$ có phép phân tích thông thường $PA = LU$. Lấy chuyển vị cả hai vế cho ta $A^TP^T = U^TL^T$. Chứng minh của $|A| = |A^T|$ có được bằng cách sử dụng quy tắc 9 cho các tích:

| So sánh | $\det P \det A = \det L \det U$ | với | $\det A^T \det P^T = \det U^T \det L^T$ |
|---------|---------------------------------|------|-----------------------------------------|

Đầu tiên, $\det L = \det L^T = 1$ (cả hai đều có các số $1$ trên đường chéo). Thứ hai, $\det U = \det U^T$ (các ma trận tam giác này có cùng đường chéo). Thứ ba, $\det P = \det P^T$ (các hoán vị có $P^TP = I$, vì vậy $|P^T||P| = 1$ theo quy tắc 9; do đó $|P|$ và $|P^T|$ đều bằng $1$ hoặc đều bằng $-1$). Vì vậy $L, U, P$ có các định thức giống như $L^T, U^T, P^T$ và điều này để lại $\det A = \det A^T$.

*Bình luận quan trọng về các cột:* Mọi quy tắc cho các hàng đều có thể áp dụng cho các cột (chỉ bằng cách lấy chuyển vị, vì $|A| = |A^T|$). Định thức đổi dấu khi hai cột được hoán đổi. *Một cột toàn số không hoặc hai cột bằng nhau sẽ làm cho định thức bằng không.* Nếu một cột được nhân với $t$, thì định thức cũng vậy. Định thức là một hàm tuyến tính đối với từng cột riêng biệt.

Đã đến lúc dừng lại. Danh sách các tính chất đã đủ dài. Tiếp theo, chúng ta sẽ tìm và sử dụng một công thức hiện cho định thức.

#### **• ÔN TẬP CÁC Ý TƯỞNG THEN CHỐT (REVIEW OF THE KEY IDEAS) •**

**1.** Định thức được định nghĩa bởi $\det I = 1$, sự đảo dấu, và tính tuyến tính trong mỗi hàng.
**2.** Sau phép khử, $\det A$ là $\pm$ (tích của các phần tử chốt).
**3.** Định thức bằng không chính xác khi $A$ không khả nghịch.
**4.** Hai tính chất đáng chú ý là $\det AB = (\det A)(\det B)$ và $\det A^T = \det A$.

#### **• CÁC VÍ DỤ ĐÃ GIẢI (WORKED EXAMPLES) •**

**5.1 A** Áp dụng các phép toán này cho $A$ và tìm định thức của $M_1, M_2, M_3, M_4$:
Trong $M_1$, nhân mỗi phần tử $a_{ij}$ với $(-1)^{i+j}$ tạo ra mô hình dấu bàn cờ.
Trong $M_2$, các hàng 1, 2, 3 của $A$ được *trừ đi* từ các hàng 2, 3, 1.
Trong $M_3$, các hàng 1, 2, 3 của $A$ được *cộng vào* các hàng 2, 3, 1.

*Định thức của $M_1, M_2, M_3$ liên quan như thế nào với định thức của $A$?*

| $\begin{bmatrix} a_{11} & -a_{12} & a_{13} \\ -a_{21} & a_{22} & -a_{23} \\ a_{31} & -a_{32} & a_{33} \end{bmatrix}$ | $\begin{bmatrix} \text{hàng } 1 - \text{hàng } 3 \\ \text{hàng } 2 - \text{hàng } 1 \\ \text{hàng } 3 - \text{hàng } 2 \end{bmatrix}$ | $\begin{bmatrix} \text{hàng } 1 + \text{hàng } 3 \\ \text{hàng } 2 + \text{hàng } 1 \\ \text{hàng } 3 + \text{hàng } 2 \end{bmatrix}$ |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|

**Giải** Ba định thức lần lượt là $\det A$, $0$, và $2 \det A$. Đây là lý do:

| $M_1 = \begin{bmatrix} 1 & & \\ & -1 & \\ & & 1 \end{bmatrix} \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{bmatrix} \begin{bmatrix} 1 & & \\ & -1 & \\ & & 1 \end{bmatrix}$ nên $\det M_1 = (-1)(\det A)(-1)$ . |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

$M_2$ suy biến bởi vì tổng các hàng của nó tạo thành hàng toàn số không. Định thức của nó bằng không.

$M_3$ có thể được tách thành *tám ma trận* theo Quy tắc 3 (tính tuyến tính trong mỗi hàng riêng biệt):

$$
\begin{bmatrix}
\text{hàng } 1 + \text{hàng } 3 \\
\text{hàng } 2 + \text{hàng } 1 \\
\text{hàng } 3 + \text{hàng } 2 
\end{bmatrix}
=
\begin{bmatrix}
\text{hàng } 1 \\
\text{hàng } 2 \\
\text{hàng } 3
\end{bmatrix}
+
\begin{bmatrix}
\text{hàng } 3 \\
\text{hàng } 2 \\
\text{hàng } 3
\end{bmatrix}
+
\begin{bmatrix}
\text{hàng } 1 \\
\text{hàng } 1 \\
\text{hàng } 3
\end{bmatrix}
+ \dots +
\begin{bmatrix}
\text{hàng } 3 \\
\text{hàng } 1 \\
\text{hàng } 2
\end{bmatrix}
$$

Tất cả trừ ma trận đầu tiên và ma trận cuối cùng đều có các hàng lặp lại và định thức bằng không. Ma trận đầu tiên là $A$ và ma trận cuối cùng có *hai* lần hoán đổi hàng. Do đó $\det M_3 = \det A + \det A$. (Hãy thử với $A = I$.)

**5.1 B** Giải thích cách để đạt được định thức này bằng các phép toán hàng:

| det | $\begin{bmatrix} 1-a & 1 & 1 \\ 1 & 1-a & 1 \\ 1 & 1 & 1-a \end{bmatrix} = a^2(3-a).$ | (4) |
|-----|---------------------------------------------------------------------------------------|-----|

**Giải** Trừ hàng 3 từ hàng 1 và sau đó từ hàng 2. Việc này để lại:

$$\det \begin{bmatrix} -a & 0 & a \\ 0 & -a & a \\ 1 & 1 & 1-a \end{bmatrix}.$$

Bây giờ cộng cột 1 vào cột 3, và cộng cột 2 vào cột 3. Điều này để lại một ma trận tam giác dưới với $-a, -a, 3-a$ trên đường chéo: det = $(-a)(-a)(3-a)$.

Định thức bằng không nếu $a = 0$ hoặc $a = 3$. Với $a = 0$, chúng ta có ma trận *toàn số 1* (all-ones matrix), chắc chắn suy biến. Với $a = 3$, mỗi hàng cộng lại bằng không - một lần nữa là suy biến. Những con số $0$ và $3$ đó là các **trị riêng (eigenvalues)** của ma trận toàn số 1. Ví dụ này rất tiết lộ và quan trọng, hướng tới Chương 6.

# **Bài Tập 5.1 (Problem Set 5.1)**

**Các câu hỏi 1-12 về các quy tắc của định thức.**

**1** Nếu một ma trận $4 \times 4$ có $\det A = 1/2$, hãy tìm $\det(2A)$, $\det(-A)$, $\det(A^2)$ và $\det(A^{-1})$.
**2** Nếu một ma trận $3 \times 3$ có $\det A = -1$, hãy tìm $\det(1/2 A)$, $\det(-A)$, $\det(A^2)$ và $\det(A^{-1})$.
**3** Đúng hay sai, với lý do nếu đúng hoặc ví dụ phản chứng nếu sai:
(a) Định thức của $I + A$ là $1 + \det A$.
(b) Định thức của $ABC$ là $|A||B||C|$.
(c) Định thức của $4A$ là $4|A|$.
(d) Định thức của $AB - BA$ là bằng không. Thử với một ví dụ $A = \left[\begin{smallmatrix} 0 & 1 \\ 0 & 0 \end{smallmatrix}\right]$.
**4** Những phép hoán đổi hàng nào chứng tỏ rằng các "ma trận đơn vị ngược" $J_3$ và $J_4$ này có $|J_3| = -1$ nhưng $|J_4| = +1$?

$$\det \begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix} = -1 \quad \text{nhưng} \quad \det \begin{bmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{bmatrix} = +1.$$

**5** Đối với $n = 5, 6, 7$, hãy đếm các phép hoán đổi hàng để hoán vị ma trận đơn vị ngược $J_n$ thành ma trận đơn vị $I_n$. Đề xuất một quy tắc cho mọi kích thước $n$ và dự đoán xem $J_{101}$ có định thức $+1$ hay $-1$.
**6** Chỉ ra cách Quy tắc 6 (định thức = $0$ nếu một hàng toàn số không) suy ra từ Quy tắc 3 như thế nào.
**7** Tìm định thức của các phép quay (rotations) và phép phản xạ (reflections):

| $Q = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}$ | và | $Q = \begin{bmatrix} 1 - 2 \cos^2 \theta & -2 \cos \theta \sin \theta \\ -2 \cos \theta \sin \theta & 1 - 2 \sin^2 \theta \end{bmatrix}$ |
|---------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------------------------------------------------------------------|

**8** Chứng minh rằng mọi ma trận trực giao ($Q^TQ = I$) đều có định thức $1$ hoặc $-1$.
(a) Sử dụng quy tắc nhân $|AB| = |A||B|$ và quy tắc chuyển vị $|Q| = |Q^T|$.
(b) Chỉ sử dụng quy tắc nhân. Nếu $|\det Q| > 1$ thì $\det Q^n = (\det Q)^n$ sẽ bùng nổ. Làm thế nào bạn biết điều này không thể xảy ra với $Q^n$?
**9** Các ma trận này có định thức $0, 1, 2,$ hay $3$?

| $A = \begin{bmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}$ | $B = \begin{bmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{bmatrix}$ | $C = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}$ |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|

**10** Nếu các phần tử trong mỗi hàng của $A$ cộng lại bằng không, hãy giải $Ax = \mathbf{0}$ để chứng minh $\det A = 0$. Nếu các phần tử đó cộng lại bằng $1$, chứng minh rằng $\det(A - I) = 0$. Điều này có nghĩa là $\det A = 1$ không?
**11** Giả sử rằng $CD = -DC$ và tìm điểm sai trong lập luận này: Lấy định thức cho ta $|C||D| = -|D||C|$. Do đó $|C| = 0$ hoặc $|D| = 0$. Một hoặc cả hai ma trận phải là ma trận suy biến. (Điều đó là không đúng.)
**12** Nghịch đảo của một ma trận $2 \times 2$ có vẻ như có định thức = 1:

$$\det A^{-1} = \det \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix} = \frac{ad - bc}{ad - bc} = 1.$$

Có gì sai trong phép tính này? $\det A^{-1}$ đúng là gì?

#### **Các câu hỏi 13-27 sử dụng các quy tắc để tính các định thức cụ thể.**

**13 Đưa $A$ về $U$ và tìm $\det A =$ tích của các phần tử chốt:**

| $A = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 2 \\ 1 & 2 & 3 \end{bmatrix}$ | $A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 2 & 3 \\ 3 & 3 & 3 \end{bmatrix}$ |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------|

**14** Bằng cách áp dụng các phép toán hàng để tạo ra một ma trận tam giác trên $U$, hãy tính:

| det | $\begin{bmatrix} 1 & 2 & 3 & 0 \\ 2 & 6 & 6 & 1 \\ -1 & 0 & 0 & 3 \\ 0 & 2 & 0 & 7 \end{bmatrix}$ | và | det | $\begin{bmatrix} 2 & -1 & 0 & 0 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ 0 & 0 & -1 & 2 \end{bmatrix}$ |
|-----|-----------------------------------------------------------------------------------------------------|-----|-----|---------------------------------------------------------------------------------------------------------|

| $A = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \begin{bmatrix} 1 & -4 & 5 \end{bmatrix}$ | và | $A = \begin{bmatrix} 0 & 1 & 3 \\ -1 & 0 & 4 \\ -3 & -4 & 0 \end{bmatrix}$ |
|------------------------------------------------------------------------------------------|-----|----------------------------------------------------------------------------|

**17** Một ma trận phản xứng có $A^T = -A$. Lắp $a, b, c$ thay cho $1, 3, 4$ trong Câu hỏi 16 và chứng minh rằng $|A| = 0$. Viết ra một ví dụ $4 \times 4$ với $|A| = 1$.

**18** Sử dụng các phép toán hàng để chứng minh rằng "định thức Vandermonde" $3 \times 3$ là

| det | $\begin{bmatrix} 1 & a & a^2 \\ 1 & b & b^2 \\ 1 & c & c^2 \end{bmatrix} = (b-a)(c-a)(c-b).$ |
|-----|----------------------------------------------------------------------------------------------|

**19** Tìm định thức của $U$ và $U^{-1}$ và $U^2$:

| $U = \begin{bmatrix} 1 & 4 & 6 \\ 0 & 2 & 5 \\ 0 & 0 & 3 \end{bmatrix}$ | và | $U = \begin{bmatrix} a & b \\ 0 & d \end{bmatrix}$ |
|-------------------------------------------------------------------------|-----|----------------------------------------------------|

**20** Giả sử bạn thực hiện hai phép toán hàng cùng một lúc, đi từ

| $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$ | thành | $\begin{bmatrix} a - lc & b - ld \\ c - la & d - lb \end{bmatrix}$ |
|------------------------------------------------|----|--------------------------------------------------------------------|

Tìm định thức thứ hai. Nó có bằng $ad - bc$ không?

**21** *Hoán vị hàng:* Cộng hàng 1 của $A$ vào hàng 2, sau đó trừ hàng 2 khỏi hàng 1. Sau đó cộng hàng 1 vào hàng 2 và nhân hàng 1 với $-1$ để đạt được $B$. Các quy tắc nào chỉ ra

| $\det B = \begin{vmatrix} c & d \\ a & b \end{vmatrix}$ bằng $-\det A = -\begin{vmatrix} a & b \\ c & d \end{vmatrix}?$ |
|---------------------------------------------------------------------------------------------------------------------------|

Những quy tắc đó có thể thay thế Quy tắc 2 trong định nghĩa của định thức.

**22** Từ $ad - bc$, tìm định thức của $A$ và $A^{-1}$ và $A - \lambda I$:

| $A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$ | và | $A^{-1} = \frac{1}{3} \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}$ | và | $A - \lambda I = \begin{bmatrix} 2 - \lambda & 1 \\ 1 & 2 - \lambda \end{bmatrix}$ |
|----------------------------------------------------|-----|-----------------------------------------------------------------------|-----|---------------------------------------------------------------------------------|

Hai con số $\lambda$ nào dẫn đến $\det(A - \lambda I) = 0$? Viết ma trận $A - \lambda I$ cho mỗi con số $\lambda$ đó - nó sẽ không khả nghịch.

**23** Từ $A = \begin{bmatrix} 4 & 1 \\ 1 & 4 \end{bmatrix}$, tìm $A^2$ và $A^{-1}$ và $A - \lambda I$ cùng với định thức của chúng. Hai con số $\lambda$ nào dẫn đến $\det(A - \lambda I) = 0$?
**24** Phép khử rút gọn $A$ thành $U$. Khi đó $A = LU$:

$$A = \begin{bmatrix} 3 & 3 & 4 \\ 6 & 8 & 7 \\ -3 & 5 & -9 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & 4 & 1 \end{bmatrix} \begin{bmatrix} 3 & 3 & 4 \\ 0 & 2 & -1 \\ 0 & 0 & -1 \end{bmatrix} = LU.$$

Tìm định thức của $L, U, A, U^{-1}L^{-1}$ và $U^{-1}L^{-1}A$.

**25** Nếu phần tử $i, j$ của $A$ là $i$ nhân với $j$, hãy chứng minh rằng $\det A = 0$. (Ngoại trừ khi $A = [1]$.)
**26** Nếu phần tử $i, j$ của $A$ là $i + j$, hãy chứng minh rằng $\det A = 0$. (Ngoại trừ khi $n = 1$ hoặc $2$.)
**27** Tính định thức của các ma trận này bằng các phép toán hàng:

$$A = \begin{bmatrix} 0 & a & 0 \\ 0 & 0 & b \\ c & 0 & 0 \end{bmatrix} \quad \text{và} \quad B = \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & c \\ d & 0 & 0 & 0 \end{bmatrix} \quad \text{và} \quad C = \begin{bmatrix} a & a & a \\ a & b & b \\ a & b & c \end{bmatrix}.$$

**28** Đúng hay sai (đưa ra lý do nếu đúng hoặc ví dụ $2 \times 2$ nếu sai):
(a) Nếu $A$ không khả nghịch thì $AB$ không khả nghịch.
(b) Định thức của $A$ luôn là tích các phần tử chốt của nó.
(c) Định thức của $A - B$ bằng $\det A - \det B$.
(d) $AB$ và $BA$ có cùng định thức.
**29** Có gì sai trong chứng minh này cho thấy các ma trận chiếu có $\det P = 1$? $P = P^2$ nên $\det P = (\det P)^2$. Khi đó $\det P = 1$.

**30** (Câu hỏi giải tích - Calculus question) Chứng minh rằng các đạo hàm riêng của 
$$\ln(\det A)$$
cho kết quả là $A^{-1}$.

| $f(a, b, c, d) = \ln(ad - bc)$ | dẫn đến | $\begin{bmatrix} \partial f / \partial a & \partial f / \partial c \\ \partial f / \partial b & \partial f / \partial d \end{bmatrix} = A^{-1}$ |
|--------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------|

**31** (MATLAB) Ma trận Hilbert `hilb(n)` có phần tử $i, j$ bằng $1/(i + j - 1)$. In ra các định thức của `hilb(1)`, `hilb(2)`, ..., `hilb(10)`. Các ma trận Hilbert rất khó làm việc! Các phần tử chốt của `hilb(5)` là gì?
**32** (MATLAB) Định thức điển hình (thực nghiệm) của `rand(n)` và `randn(n)` với $n = 50, 100, 200, 400$ là gì? (Và "Inf" có nghĩa là gì trong MATLAB?)
**33** (MATLAB) Tìm định thức lớn nhất của một ma trận $6 \times 6$ gồm các số $1$ và $-1$.
**34** Nếu bạn biết $\det A = 6$, thì định thức của $B$ là bao nhiêu?

| Từ $\det A =$ | hàng 1 |                  | hàng 3 + hàng 2 + hàng 1 |  |
|----------------|-------|--------------------|-----------------------|--|
|                | hàng 2 | = 6 tìm $\det B =$ | hàng 2 + hàng 1         |  |
|                | hàng 3 |                  | hàng 1                 |  |

## 5.2 Hoán Vị (Permutations) và Phần Phụ Đại Số (Cofactors)

1. $2 \times 2$: $ad - bc$ có $2!$ số hạng với các dấu $\pm$. $n \times n$: $\det A$ cộng $n!$ số hạng với các dấu $\pm$.
2. Với $n = 3$, $\det A$ cộng $3! = 6$ số hạng. Hai trong số các số hạng là $+a_{12}a_{23}a_{31}$ và $-a_{13}a_{22}a_{31}$. **Các hàng 1, 2, 3 và các cột 1, 2, 3 xuất hiện đúng một lần trong mỗi số hạng.**
3. Dấu trừ đó xuất hiện vì thứ tự cột 3, 2, 1 cần một lần hoán đổi để khôi phục lại 1, 2, 3.
4. Sáu số hạng bao gồm $+a_{11}a_{22}a_{33} - a_{11}a_{23}a_{32} = a_{11}(a_{22}a_{33} - a_{23}a_{32}) = a_{11}(\text{phần phụ đại số } C_{11})$.
5. Luôn có $\det A = a_{11}C_{11} + a_{12}C_{12} + \dots + a_{1n}C_{1n}$. Các phần phụ đại số (cofactors) là định thức của kích thước $n - 1$.

Máy tính tìm định thức từ các phần tử chốt. Phần này giải thích hai cách khác để làm điều đó. Có một "công thức lớn" sử dụng tất cả $n!$ hoán vị. Có một "công thức phần phụ đại số" (cofactor formula) sử dụng các định thức kích thước $n - 1$. Ví dụ tốt nhất là ma trận $4 \times 4$ yêu thích của tôi:

$$A = \begin{bmatrix} 2 & -1 & 0 & 0 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ 0 & 0 & -1 & 2 \end{bmatrix} \quad \text{có} \quad \det A = 5.$$

Chúng ta có thể tìm định thức này theo cả ba cách: *các phần tử chốt (pivots), công thức lớn (big formula), các phần phụ đại số (cofactors)*.

1. Tích của các phần tử chốt là $2 \cdot \frac{3}{2} \cdot \frac{4}{3} \cdot \frac{5}{4}$. Việc triệt tiêu các phân số tạo ra $5$.
2. "Công thức lớn" trong phương trình (8) có $4! = 24$ số hạng. Chỉ có năm số hạng là khác không:

$$\det A = 16 - 4 - 4 - 4 + 1 = 5.$$

Số 16 đến từ $2 \cdot 2 \cdot 2 \cdot 2$ trên đường chéo của $A$. $-4$ và $+1$ đến từ đâu? Khi bạn có thể tìm thấy năm số hạng đó, bạn đã hiểu công thức (8).

3. Các số $2, -1, 0, 0$ trong hàng đầu tiên nhân với các phần phụ đại số (cofactors) tương ứng của chúng là $4, 3, 2, 1$ từ các hàng khác. Việc đó mang lại $2 \cdot 4 - 1 \cdot 3 = 5$. Các phần phụ đại số đó là các định thức $3 \times 3$. Các phần phụ đại số sử dụng các hàng và cột *không* được sử dụng bởi phần tử ở hàng đầu tiên. *Mỗi số hạng trong một định thức sử dụng mỗi hàng và cột một lần!*

### Công Thức Phần Tử Chốt (The Pivot Formula)

Khi phép khử dẫn đến $A = LU$, các phần tử chốt $d_1, \dots, d_n$ nằm trên đường chéo của ma trận tam giác trên $U$. Nếu không có phép hoán đổi hàng nào liên quan, *nhân những phần tử chốt đó* để tìm định thức:

$$\det A = (\det L)(\det U) = (1)(d_1 d_2 \cdots d_n). \quad (1)$$

Công thức cho $\det A$ này đã xuất hiện trong Phần 5.1, với khả năng xa hơn là có các phép hoán đổi hàng. Khi đó một phép hoán vị xuất hiện thành $PA = LU$. Định thức của $P$ là $-1$ hoặc $+1$.

| $(\det P)(\det A) = (\det L)(\det U)$ | cho ta | $\det A = \pm(d_1d_2 \cdots d_n)$ | (2) |
|---------------------------------------|-------|-----------------------------------|-----|

**Ví dụ 1** Một phép hoán đổi hàng tạo ra các phần tử chốt $4, 2, 1$ và dấu trừ quan trọng đó:

| $A = \begin{bmatrix} 0 & 0 & 1 \\ 0 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$ | $PA = \begin{bmatrix} 4 & 5 & 6 \\ 0 & 2 & 3 \\ 0 & 0 & 1 \end{bmatrix}$ | $\det A = -(4)(2)(1) = -8.$ |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------|-----------------------------|

Số lẻ các phép hoán đổi hàng (cụ thể là một phép hoán đổi) có nghĩa là $\det P = -1$.

Ví dụ tiếp theo không có phép hoán đổi hàng. Đây có thể là ma trận đầu tiên chúng ta đã phân tích thành $LU$ (khi nó là $3 \times 3$). Điều đáng chú ý là chúng ta có thể đi thẳng lên $n \times n$. Các phần tử chốt cho ta định thức. Chúng ta cũng sẽ xem xét cách các định thức cho ra các phần tử chốt.

**Ví dụ 2** Các phần tử chốt đầu tiên của ma trận ba đường chéo (tridiagonal matrix) $A$ này là $2, 3/2, 4/3$. Tiếp theo là $5/4$ và $6/5$ và cuối cùng là $(n+1)/n$. Phân tích ma trận $n \times n$ này bộc lộ định thức của nó:

$$\begin{bmatrix} 2 & -1 & & & & \\ -1 & 2 & -1 & & & \\ & -1 & 2 & & & \\ & & & \ddots & & \\ & & & & -1 & 2 \end{bmatrix} = \begin{bmatrix} 1 & & & & & \\ -\frac{1}{2} & 1 & & & & \\ & -\frac{2}{3} & 1 & & & \\ & & & \ddots & 1 & \\ & & & & -\frac{n-1}{n} & 1 \end{bmatrix} \begin{bmatrix} 2 & -1 & & & & \\ & \frac{3}{2} & -1 & & & \\ & & \frac{4}{3} & -1 & & \\ & & & \ddots & -1 & \\ & & & & & \frac{n+1}{n} \end{bmatrix}$$

Các phần tử chốt nằm trên đường chéo của $U$ (ma trận cuối cùng). Khi nhân $2, 3/2, 4/3, \dots, (n+1)/n$, các phân số bị triệt tiêu. Định thức của ma trận $4 \times 4$ là $5$. Định thức $3 \times 3$ là $4$. *Định thức $n \times n$ là $n+1$:*

| Ma trận $-1, 2, -1$ | $\det A = (2) \left(\frac{3}{2}\right) \left(\frac{4}{3}\right) \cdots \left(\frac{n+1}{n}\right) = n + 1.$ |
|--------------------|-----------------------------------------------------------------------------------------------------------|

Điểm quan trọng: Các phần tử chốt đầu tiên chỉ phụ thuộc vào *góc trên bên trái* của ma trận gốc $A$. Đây là một quy tắc cho tất cả các ma trận mà không có các phép hoán đổi hàng.

Phần tử chốt thứ $k$ xuất phát từ ma trận $k \times k$ $A_k$ ở góc trên bên trái của $A$.

*Định thức của ma trận con góc đó* $A_k$ *là* $d_1 d_2 \cdots d_k$ *(tích $k$ phần tử chốt đầu tiên).*

Ma trận $1 \times 1$ $A_1$ chứa phần tử chốt đầu tiên $d_1$. Đây là $\det A_1$. Ma trận $2 \times 2$ ở góc có $\det A_2 = d_1 d_2$. Cuối cùng định thức $n \times n$ nhân với toàn bộ $n$ phần tử chốt.

Phép khử giải quyết ma trận $A_k$ ở góc trên bên trái trong khi bắt đầu trên toàn bộ ma trận. Chúng ta giả sử không có phép hoán đổi hàng nào - khi đó $A = LU$ và $A_k = L_k U_k$. Lấy một định thức chia cho định thức trước đó ($\det A_k$ chia cho $\det A_{k-1}$) sẽ triệt tiêu tất cả ngoại trừ phần tử chốt mới nhất $d_k$. *Mỗi phần tử chốt là một tỷ số của các định thức:*

| **Các phần tử chốt từ các định thức** | **Phần tử chốt thứ $k$ là $d_k = \frac{d_1 d_2 \cdots d_k}{d_1 d_2 \cdots d_{k-1}} = \frac{\det A_k}{\det A_{k-1}}$** | **(3)** |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|------------|

### **Công Thức Lớn Cho Định Thức (The Big Formula for Determinants)**

Các phần tử chốt rất tốt cho việc tính toán. Chúng tập trung rất nhiều thông tin - đủ để tìm ra định thức. Nhưng thật khó để kết nối chúng với các $a_{ij}$ ban đầu. Phần đó sẽ rõ ràng hơn nếu chúng ta quay trở lại các quy tắc 1-2-3, tính tuyến tính và đảo dấu và $\det I = 1$. Chúng ta muốn rút ra một công thức hiện duy nhất cho định thức, trực tiếp từ các phần tử $a_{ij}$.

*Công thức này có* $n!$ *số hạng.* Kích thước của nó tăng rất nhanh vì $n! = 1, 2, 6, 24, 120, \dots$. Đối với $n = 11$ có khoảng bốn mươi triệu số hạng. Đối với $n = 2$, hai số hạng đó là $ad$ và $bc$. Một nửa các số hạng có dấu trừ (như trong $-bc$). Một nửa còn lại có dấu cộng (như trong $ad$). Đối với $n = 3$, có $3! = (3)(2)(1)$ số hạng. Đây là sáu số hạng đó:

| $[a \ b] = [a \ 0] + [0 \ b]$ | và | $[c \ d] = [c \ 0] + [0 \ d]$ |
|-------------------------------|-----|-------------------------------|

Bây giờ áp dụng tính tuyến tính, đầu tiên trên hàng 1 (giữ nguyên hàng 2) và sau đó trên hàng 2 (giữ nguyên hàng 1):

$$\begin{bmatrix} a & b \\ c & d \end{bmatrix} = \begin{bmatrix} a & b \\ c & d \end{bmatrix} + \begin{bmatrix} 0 & b \\ 0 & d \end{bmatrix} \quad (\text{tách hàng 1})$$

$$= \begin{bmatrix} a & 0 \\ c & 0 \end{bmatrix} + \begin{bmatrix} a & 0 \\ 0 & b \end{bmatrix} + \begin{bmatrix} 0 & b \\ c & 0 \end{bmatrix} + \begin{bmatrix} 0 & b \\ 0 & d \end{bmatrix} \quad (\text{tách hàng 2}).$$

Dòng cuối cùng có $2^2 = 4$ định thức. Định thức thứ nhất và thứ tư bằng không vì một hàng là bội số của hàng kia. Chúng ta còn lại $2! = 2$ định thức để tính:

| $\begin{vmatrix} a & 0 \\ 0 & d \end{vmatrix} + \begin{vmatrix} 0 & b \\ c & 0 \end{vmatrix} = ad \begin{vmatrix} 1 & 0 \\ 0 & 1 \end{vmatrix} + bc \begin{vmatrix} 0 & 1 \\ 1 & 0 \end{vmatrix} = ad - bc.$ |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Việc tách ra đã dẫn đến các ma trận hoán vị. Định thức của chúng mang lại dấu cộng hoặc trừ. Hoán vị cho biết trình tự cột. Trong trường hợp này, trình tự cột là $(1, 2)$ hoặc $(2, 1)$.

Bây giờ thử với $n = 3$. Mỗi hàng tách thành $3$ hàng đơn giản hơn như $\begin{bmatrix} a_{11} & 0 & 0 \end{bmatrix}$. Sử dụng tính tuyến tính trong mỗi hàng, $\det A$ tách thành $3^3 = 27$ định thức đơn giản. Nếu một lựa chọn cột bị lặp lại (chẳng hạn nếu chúng ta cũng chọn hàng $\begin{bmatrix} a_{21} & 0 & 0 \end{bmatrix}$), thì định thức đơn giản đó bằng không. Chúng ta chỉ chú ý khi *các phần tử $a_{ij}$ đến từ các cột khác nhau*, ví dụ như $(3, 1, 2)$:

$$
\begin{vmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{vmatrix}
=
\begin{vmatrix} a_{11} & 0 & 0 \\ 0 & a_{22} & 0 \\ 0 & 0 & a_{33} \end{vmatrix}
+
\begin{vmatrix} 0 & a_{12} & 0 \\ 0 & 0 & a_{23} \\ a_{31} & 0 & 0 \end{vmatrix}
+
\begin{vmatrix} 0 & 0 & a_{13} \\ a_{21} & 0 & 0 \\ 0 & a_{32} & 0 \end{vmatrix}
$$
$$
+
\begin{vmatrix} a_{11} & 0 & 0 \\ 0 & 0 & a_{23} \\ 0 & a_{32} & 0 \end{vmatrix}
+
\begin{vmatrix} 0 & a_{12} & 0 \\ a_{21} & 0 & 0 \\ 0 & 0 & a_{33} \end{vmatrix}
+
\begin{vmatrix} 0 & 0 & a_{13} \\ 0 & a_{22} & 0 \\ a_{31} & 0 & 0 \end{vmatrix}
$$

*Có $3! = 6$ cách để sắp xếp các cột, vì vậy có sáu định thức.* Sáu hoán vị của $(1, 2, 3)$ bao gồm hoán vị đồng nhất (identity permutation) $(1, 2, 3)$ từ $P = I$.

**Số thứ tự cột** = $(1, 2, 3)$, $(2, 3, 1)$, **$(3, 1, 2)$**, $(1, 3, 2)$, $(2, 1, 3)$, $(3, 2, 1)$. (6)

Ba hoán vị cuối cùng là *hoán vị lẻ (odd permutations)* (một lần hoán đổi). Ba hoán vị đầu tiên là *hoán vị chẵn (even permutations)* ($0$ hoặc $2$ lần hoán đổi). Khi trình tự cột là $(3, 1, 2)$, chúng ta đã chọn các phần tử $a_{13}a_{21}a_{32}$ - trình tự cột cụ thể đó đi kèm với dấu cộng ($2$ lần hoán đổi). Định thức của $A$ bây giờ được tách thành sáu số hạng đơn giản. Đưa các phần tử $a_{ij}$ ra ngoài làm nhân tử:

$$
\det A = 
a_{11}a_{22}a_{33} \begin{vmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{vmatrix} + 
a_{12}a_{23}a_{31} \begin{vmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{vmatrix} + 
a_{13}a_{21}a_{32} \begin{vmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{vmatrix} \quad (7)
$$
$$
- a_{11}a_{23}a_{32} \begin{vmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{vmatrix} - 
a_{12}a_{21}a_{33} \begin{vmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{vmatrix} - 
a_{13}a_{22}a_{31} \begin{vmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{vmatrix}
$$

Ba hoán vị đầu tiên (chẵn) có $\det P = +1$, ba hoán vị cuối cùng (lẻ) có $\det P = -1$. Chúng ta đã chứng minh công thức $3 \times 3$ một cách có hệ thống.

Bây giờ bạn có thể thấy công thức cho $n \times n$. Có $n!$ cách sắp xếp các cột. Các cột $(1, 2, \dots, n)$ đi theo mọi trình tự có thể $(\alpha, \beta, \dots, \omega)$. Lấy $a_{1\alpha}$ từ hàng 1, $a_{2\beta}$ từ hàng 2 và cuối cùng là $a_{n\omega}$ từ hàng $n$, định thức chứa tích $a_{1\alpha}a_{2\beta} \cdots a_{n\omega}$ nhân với $+1$ hoặc $-1$. Một nửa các trình tự cột có dấu $-1$.

Định thức của $A$ là tổng của $n!$ định thức đơn giản này, nhân với $1$ hoặc $-1$. Các định thức đơn giản $a_{1\alpha}a_{2\beta} \cdots a_{n\omega}$ chọn *một phần tử từ mỗi hàng và mỗi cột.* Đối với ma trận $5 \times 5$, số hạng $a_{15}a_{22}a_{33}a_{44}a_{51}$ sẽ có $\det P = -1$ do hoán đổi cột 5 và cột 1.

$$
\begin{aligned} 
\det A &= \text{tổng qua tất cả } \mathbf{n!} \text{ hoán vị cột } P = (\alpha, \beta, \dots, \omega) \\ 
&= \sum (\det P) a_{1\alpha} a_{2\beta} \dots a_{n\omega} = \text{CÔNG THỨC LỚN (BIG FORMULA).} 
\end{aligned} \quad (8)
$$

Trường hợp $3 \times 3$ có ba tích "hướng xuống sang phải" (xem Bài tập 28) và ba tích "hướng xuống sang trái". Cảnh báo: Nhiều người tin rằng họ nên làm theo khuôn mẫu này trong trường hợp $4 \times 4$. Họ chỉ lấy 8 tích - nhưng chúng ta cần 24.

**Ví dụ 3** (Định thức của $U$) Khi $U$ là ma trận tam giác trên, chỉ có một trong số $n!$ tích có thể khác không. Số hạng duy nhất này đến từ đường chéo: $\det U = +u_{11}u_{22} \cdots u_{nn}$. Tất cả các trình tự cột khác đều chọn ít nhất một phần tử bên dưới đường chéo, nơi $U$ có các số không. Ngay khi chúng ta chọn một số như $u_{21} = 0$, số hạng đó trong phương trình (8) chắc chắn bằng không.

Tất nhiên $\det I = 1$. Số hạng khác không duy nhất là $+(1)(1) \cdots (1)$ từ đường chéo.

**Ví dụ 4** Giả sử $Z$ là ma trận đơn vị ngoại trừ ở cột 3. Khi đó

Định thức của $Z = \begin{vmatrix} 1 & 0 & a & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & c & 0 \\ 0 & 0 & 1 & 0 \end{vmatrix}$ là $c$. (9)

Số hạng $(1)(1)(c)(1)$ đến từ đường chéo chính mang dấu cộng. Có $4! = 24$ tích (chọn một nhân tử từ mỗi hàng và mỗi cột) nhưng 23 tích còn lại đều bằng không. Lý do: Nếu chúng ta chọn $a, b$, hoặc $d$ từ cột 3, cột đó đã được dùng. Khi đó lựa chọn có sẵn duy nhất từ hàng 3 là số không.

Đây là một lý do khác cho cùng một đáp án. Nếu $c = 0$, thì $Z$ có một hàng toàn số không và $\det Z = c = 0$ là đúng. Nếu $c$ khác không, *sử dụng phép khử.* Trừ các bội số của hàng 3 từ các hàng khác, để loại bỏ $a, b, d$. Điều đó để lại một ma trận đường chéo và $\det Z = c$.

Ví dụ này sẽ sớm được sử dụng cho "Quy tắc Cramer". Nếu chúng ta di chuyển $a, b, c, d$ vào cột đầu tiên của $Z$, định thức là $\det Z = a$. *(Tại sao?)* Thay đổi một cột của $I$ để lại cho $Z$ một định thức dễ dàng, chỉ đến từ đường chéo chính của nó.

**Ví dụ 5** Giả sử $A$ có các số 1 nằm ngay phía trên và phía dưới đường chéo chính. Ở đây $n = 4$:

$A = \begin{bmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{bmatrix}$ và $P = \begin{bmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{bmatrix}$ có **định thức** $1$.

Lựa chọn khác không duy nhất ở hàng đầu tiên là cột 2. Lựa chọn khác không duy nhất ở hàng 4 là cột 3. Khi đó các hàng 2 và 3 *phải* chọn các cột 1 và 4. Nói cách khác $\det P = \det A$. Định thức của $P$ là $+1$ (hai lần hoán đổi để đạt được $2, 1, 4, 3$). Do đó $\det A = +1$.

### **Định Thức Dùng Phần Phụ Đại Số (Determinant by Cofactors)**

Công thức (8) là một định nghĩa trực tiếp của định thức. Nó cung cấp cho bạn mọi thứ cùng một lúc - nhưng bạn phải tiêu hóa nó. Bằng cách nào đó tổng của $n!$ số hạng này phải thỏa mãn các quy tắc 1-2-3 (khi đó tất cả các tính chất khác 4-10 sẽ theo sau). Dễ nhất là $\det I = 1$, đã được kiểm tra.

*Khi bạn tách rời phần tử* $a_{11}$ *hoặc* $a_{12}$ *hoặc* $a_{1n}$ *đến từ hàng đầu tiên*, bạn thấy tính tuyến tính. Đối với ma trận $3 \times 3$, hãy tách 6 số hạng thông thường của định thức thành 3 cặp:

$$\det A = a_{11}(a_{22}a_{33} - a_{23}a_{32}) + a_{12}(a_{23}a_{31} - a_{21}a_{33}) + a_{13}(a_{21}a_{32} - a_{22}a_{31}). \quad (10)$$

Ba đại lượng trong ngoặc đơn đó được gọi là *"các phần phụ đại số (cofactors)".* Chúng là các **định thức** $2 \times 2$, từ các hàng 2 và 3. Hàng đầu tiên đóng góp các phần tử $a_{11}, a_{12}, a_{13}$. *Các hàng bên dưới đóng góp các phần phụ đại số* $C_{11}, C_{12}, C_{13}$. Chắc chắn định thức $a_{11}C_{11} + a_{12}C_{12} + a_{13}C_{13}$ phụ thuộc tuyến tính vào $a_{11}, a_{12}, a_{13}$ - đây là Quy tắc 3.

Phần phụ đại số của $a_{11}$ là $C_{11} = a_{22}a_{33} - a_{23}a_{32}$. Bạn có thể thấy nó trong phép tách này:

$$
\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{bmatrix}
\rightarrow
a_{11} \begin{bmatrix}
a_{22} & a_{23} \\
a_{32} & a_{33}
\end{bmatrix}
$$

Chúng ta vẫn đang chọn *một phần tử từ mỗi hàng và mỗi cột.* Vì $a_{11}$ chiếm hàng 1 và cột 1, nó để lại một định thức $2 \times 2$ làm phần phụ đại số của mình.

Như thường lệ, chúng ta phải quan sát dấu. Định thức $2 \times 2$ đi cùng với $a_{12}$ trông giống như $a_{21}a_{33} - a_{23}a_{31}$. Nhưng trong phần phụ đại số $C_{12}$, *dấu của nó bị đảo ngược.* Khi đó $a_{12}C_{12}$ mới là định thức $3 \times 3$ chính xác. Mô hình dấu cho các phần phụ đại số dọc theo hàng đầu tiên là *cộng-trừ-cộng-trừ. Bạn gạch đi hàng 1 và cột $j$ để có được ma trận con $M_{1j}$ kích thước $n - 1$.* Nhân định thức của nó với dấu $(-1)^{1+j}$ để được phần phụ đại số:

Các phần phụ đại số dọc theo hàng 1 là $C_{1j} = (-1)^{1+j} \det M_{1j}$.

**Khai triển phần phụ đại số là $\det A = a_{11}C_{11} + a_{12}C_{12} + \dots + a_{1n}C_{1n}$ (11)**

Trong công thức lớn (8), các số hạng nhân với $a_{11}$ kết hợp lại để tạo ra $C_{11} = \det M_{11}$. Dấu là $(-1)^{1+1}$, có nghĩa là *cộng*. Phương trình (11) là một dạng khác của phương trình (8) và cũng là phương trình (10), với các phần tử từ hàng 1 nhân với các phần phụ đại số chỉ sử dụng các hàng còn lại.

**Lưu ý:** Bất cứ điều gì khả thi đối với hàng 1 thì đều khả thi đối với hàng $i$. Các phần tử $a_{ij}$ trong hàng đó cũng có các phần phụ đại số $C_{ij}$. Chúng là các định thức cấp $n - 1$, nhân với $(-1)^{i+j}$. Vì $a_{ij}$ giải quyết hàng $i$ và cột $j$, *ma trận con $M_{ij}$ bỏ đi hàng $i$ và cột $j$.* Minh họa dưới đây hiển thị $a_{43}$ và $M_{43}$ (với hàng 4 và cột 3 bị loại bỏ). Dấu $(-1)^{4+3}$ nhân với định thức của $M_{43}$ để ra $C_{43}$. Ma trận dấu hiển thị mô hình dấu $\pm$:

$$A = \begin{bmatrix} \bullet & \bullet & \bullet & \bullet \\ \bullet & \bullet & \bullet & \bullet \\ \bullet & \bullet & \bullet & \bullet \\ \bullet & \bullet & \bullet & \bullet \end{bmatrix} \quad \text{dấu } (-1)^{i+j} = \begin{bmatrix} + & - & + & - \\ - & + & - & + \\ + & - & + & - \\ - & + & - & + \end{bmatrix}$$

Định thức là tích vô hướng của bất kỳ hàng $i$ nào của $A$ với các phần phụ đại số của nó sử dụng các hàng khác:
**CÔNG THỨC PHẦN PHỤ ĐẠI SỐ (COFACTOR FORMULA)** (12)

Mỗi phần phụ đại số $C_{ij}$ (cấp $n-1$, bỏ đi hàng $i$ và cột $j$) bao gồm dấu chính xác của nó:
**Phần phụ đại số**      $C_{ij} = (-1)^{i+j} \det M_{ij}$.

Một định thức cấp $n$ là một tổ hợp của các định thức cấp $n-1$. Một người thích sự đệ quy sẽ tiếp tục. Mỗi định thức con vỡ ra thành các định thức cấp $n-2$. *Chúng ta có thể định nghĩa tất cả các định thức thông qua phương trình (12).* Quy tắc này đi từ cấp $n$ xuống $n-1$ xuống $n-2$ và cuối cùng đến cấp 1. Định nghĩa định thức $1 \times 1$ $|a|$ là con số $a$. Khi đó phương pháp phần phụ đại số đã hoàn chỉnh.

Chúng ta thích xây dựng $\det A$ từ các tính chất của nó (tuyến tính, đảo dấu, $\det I = 1$). Công thức lớn (8) và các công thức phần phụ đại số (10)-(12) suy ra từ những quy tắc đó. Một công thức cuối cùng đến từ quy tắc $\det A = \det A^T$. Chúng ta có thể khai triển theo phần phụ đại số, *dọc theo một cột* thay vì ngang qua một hàng. Dọc theo cột $j$, các phần tử là $a_{1j}$ đến $a_{nj}$. Các phần phụ đại số là $C_{1j}$ đến $C_{nj}$. Định thức là một tích vô hướng:

| Các phần phụ đại số dọc theo cột $j$ | $\det A = a_{1j} C_{1j} + a_{2j} C_{2j} + \dots + a_{nj} C_{nj}$ | (13) |
|---------------------------|------------------------------------------------------------|------|

**Các phần phụ đại số rất hữu ích khi ma trận có nhiều số không - như** trong các ví dụ tiếp theo.

**Ví dụ 6** Ma trận $-1, 2, -1$ (tridiagonal) chỉ có hai số khác không ở hàng đầu tiên. Vì vậy chỉ có hai phần phụ đại số $C_{11}$ và $C_{12}$ liên quan đến định thức. Tôi sẽ làm nổi bật $C_{12}$:

$$\begin{vmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{vmatrix} = 2 \begin{vmatrix} 2 & -1 \\ -1 & 2 \end{vmatrix} - (-1) \begin{vmatrix} -1 & -1 \\ 0 & 2 \end{vmatrix}, \quad (14)$$

Bạn thấy $2$ nhân với $C_{11}$ xuất hiện đầu tiên ở bên phải, từ việc gạch đi hàng 1 và cột 1. Phần phụ đại số $C_{11}$ này có mô hình $-1, 2, -1$ giống hệt với ma trận $A$ gốc - nhưng kích thước nhỏ hơn một bậc.

Để tính $C_{12}$ được in đậm, *hãy sử dụng các phần phụ đại số dọc theo cột đầu tiên của nó.* Số khác không duy nhất nằm ở trên cùng. Nó đóng góp một số $-1$ khác (vậy nên chúng ta quay trở lại dấu trừ). Phần phụ đại số của nó là định thức $-1, 2, -1$ kích thước $2 \times 2$, *nhỏ hơn hai bậc* so với $A$ gốc.

*Tóm tắt: Mỗi định thức $D_n$ cấp $n$ bắt nguồn từ $D_{n-1}$ và $D_{n-2}$:*

| $D_4 = 2D_3 - D_2$ | và nói chung | $D_n = 2D_{n-1} - D_{n-2}$ | (15) |
|--------------------|---------------|----------------------------|------|

Tính toán trực tiếp cho ra $D_2 = 3$ và $D_3 = 4$. Phương trình (14) có $D_4 = 2(4) - 3 = 5$. Các định thức $3, 4, 5$ khớp với công thức $D_n = n + 1$. Khi đó $D_n$ bằng $2n - (n - 1)$. "Đáp án đặc biệt của ma trận ba đường chéo" đó cũng đến từ tích các phần tử chốt trong Ví dụ 2.

**Ví dụ 7** Đây là cùng một ma trận, ngoại trừ phần tử đầu tiên (trên cùng bên trái) bây giờ là $1$:

$$B_4 = \begin{bmatrix} 1 & -1 & & \\ -1 & 2 & -1 & \\ & -1 & 2 & -1 \\ & & -1 & 2 \end{bmatrix}.$$

Tất cả các phần tử chốt của ma trận này hóa ra đều bằng $1$. Nên định thức của nó bằng $1$. Bằng cách nào điều đó lại đến từ các phần phụ đại số? Khai triển theo hàng 1, các phần phụ đại số đều giống với Ví dụ 6. Chỉ cần thay đổi $a_{11} = 2$ thành $b_{11} = 1$:

$$\det B_4 = D_3 - D_2 \quad \text{thay vì} \quad \det A_4 = 2D_3 - D_2.$$

Định thức của $B_4$ là $4 - 3 = 1$. Định thức của mọi $B_n$ là $n - (n - 1) = 1$. Nếu bạn cũng thay đổi số 2 cuối cùng thành 1, tại sao $\det = 0$?

## ■ ÔN TẬP CÁC Ý CHÍNH ■

1. Không có phép hoán đổi hàng nào, $\det A = (\text{tích các phần tử chốt})$. Ở góc trên bên trái của $A$, $\det A_k = (\text{tích của } k \text{ phần tử chốt đầu tiên})$.
2. Mỗi số hạng trong công thức lớn (8) sử dụng mỗi hàng và mỗi cột một lần. Một nửa trong số $n!$ số hạng có dấu cộng (khi $\det P = +1$) và một nửa có dấu trừ.
3. Phần phụ đại số $C_{ij}$ bằng $(-1)^{i+j}$ nhân với định thức nhỏ hơn bỏ đi hàng $i$ và cột $j$ (vì $a_{ij}$ sử dụng hàng và cột đó).
4. Định thức là tích vô hướng của bất kỳ hàng nào của $A$ với hàng các phần phụ đại số của nó. Khi một hàng của $A$ có nhiều số không, chúng ta chỉ cần một vài phần phụ đại số.

## ■ VÍ DỤ CÓ LỜI GIẢI ■

**5.2 A** *Ma trận Hessenberg* là một ma trận tam giác với một đường chéo phụ (extra diagonal). Sử dụng các phần phụ đại số của hàng 1 để chứng minh rằng định thức $4 \times 4$ thỏa mãn quy tắc Fibonacci $|H_4| = |H_3| + |H_2|$. Quy tắc tương tự sẽ tiếp tục cho mọi kích thước, $|H_n| = |H_{n-1}| + |H_{n-2}|$. $|H_n|$ là số Fibonacci nào?

$$H_2 = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix} \quad H_3 = \begin{bmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2 \end{bmatrix} \quad H_4 = \begin{bmatrix} 2 & 1 & & \\ 1 & 2 & 1 & \\ & 1 & 2 & 1 \\ & & 1 & 2 \end{bmatrix}$$

*(Ghi chú: $H_3$ trong bản gốc có vẻ in sai là `[2 1; 1 2 1; 1 1 2]`, ta sửa lại cho đúng ma trận Hessenberg ở đây là ma trận 3 đường chéo).*

**Lời giải** Phần phụ đại số $C_{11}$ đối với $H_4$ là định thức $|H_3|$. Chúng ta cũng cần $C_{12}$ (in đậm):

$$C_{12} = - \begin{vmatrix} \mathbf{1} & \mathbf{1} & \mathbf{0} \\ \mathbf{0} & \mathbf{2} & \mathbf{1} \\ \mathbf{0} & \mathbf{1} & \mathbf{2} \end{vmatrix} = - \begin{vmatrix} 1 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 1 & 2 \end{vmatrix}$$

*(Ghi chú: Bản gốc có phép tách định thức)*
Hàng 2 và 3 giữ nguyên và chúng ta sử dụng tính tuyến tính ở hàng 1. Khi tách ra, hai định thức bên phải là $-|H_3|$ và $+|H_2|$ (theo sách gốc). Vậy định thức $4 \times 4$ là

$$|H_4| = 2C_{11} + 1C_{12} = 2|H_3| - |H_3| + |H_2| = |H_3| + |H_2|.$$

Các con số thực tế là $|H_2| = 3$ và $|H_3| = 5$ (và dĩ nhiên $|H_1| = 2$). Vì $|H_n| = 2, 3, 5, 8, \dots$ tuân theo quy tắc Fibonacci $|H_{n-1}| + |H_{n-2}|$, nên nó phải là $|H_n| = F_{n+2}$.

**5.2 B** Những câu hỏi này sử dụng các dấu $\pm$ (các $P$ chẵn và lẻ) trong công thức lớn cho $\det A$:

1. Nếu $A$ là ma trận $10 \times 10$ toàn số 1, bằng cách nào công thức lớn cho ra $\det A = 0$?
2. Nếu bạn nhân tất cả $n!$ hoán vị với nhau thành một $P$ duy nhất, $P$ là chẵn hay lẻ?
3. Nếu bạn nhân mỗi $a_{ij}$ với phân số $i/j$, tại sao $\det A$ không thay đổi?

**Lời giải** Trong Câu hỏi 1, với mọi $a_{ij} = 1$, tất cả các tích trong công thức lớn (8) sẽ bằng 1. Một nửa trong số chúng đi kèm dấu cộng, và một nửa có dấu trừ. Vậy nên chúng triệt tiêu nhau để lại $\det A = 0$. (Tất nhiên ma trận toàn số 1 là ma trận suy biến. Tôi đang giả sử $n > 1$.)

Trong Câu hỏi 2, nhân $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ cho ra một hoán vị lẻ. Cũng với $3 \times 3$, ba hoán vị lẻ nhân với nhau (theo thứ tự bất kỳ) cho ra hoán vị *lẻ*. Nhưng đối với $n > 3$ tích của tất cả các hoán vị sẽ là hoán vị *chẵn*. Có $n!/2$ hoán vị lẻ và đó là một số chẵn ngay khi $n!$ bao gồm nhân tử 4.

Trong Câu hỏi 3, mỗi $a_{ij}$ được nhân với $i/j$. Vì vậy mỗi tích $a_{1\alpha}a_{2\beta} \cdots a_{n\omega}$ trong công thức lớn được nhân với tất cả các số hàng $i = 1, 2, \dots, n$ và chia cho tất cả các số cột $j = 1, 2, \dots, n$. (Các cột xuất hiện theo một thứ tự hoán vị nào đó!) Khi đó mỗi tích không bị thay đổi và $\det A$ giữ nguyên.

Một cách tiếp cận khác cho Câu hỏi 3: Chúng ta đang nhân ma trận $A$ với ma trận đường chéo $D = \text{diag}(1 : n)$ khi hàng $i$ được nhân với $i$. Và chúng ta đang nhân bên phải với $D^{-1}$ khi cột $j$ bị chia cho $j$. Định thức của $DAD^{-1}$ cũng giống với $\det A$ theo quy tắc tích.

## Bài tập 5.2

**Các bài tập 1–10 sử dụng công thức lớn với $n!$ số hạng:** $|A| = \sum \pm a_{1\alpha}a_{2\beta} \cdots a_{n\omega}$. Mỗi số hạng sử dụng mỗi hàng và mỗi cột một lần.

**1** Tính các định thức của $A, B, C$ từ sáu số hạng. Các hàng của chúng có độc lập không?

$$A = \begin{bmatrix} 1 & 2 & 3 \\ 3 & 1 & 2 \\ 3 & 2 & 1 \end{bmatrix} \quad B = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 4 & 4 \\ 5 & 6 & 7 \end{bmatrix} \quad C = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix}.$$

**2** Tính các định thức của $A, B, C, D$. Các cột của chúng có độc lập không?

$$A = \begin{bmatrix} 1 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{bmatrix} \quad B = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix} \quad C = \begin{bmatrix} A & 0 \\ 0 & A \end{bmatrix} \quad D = \begin{bmatrix} A & 0 \\ 0 & B \end{bmatrix}.$$

**3** Chứng minh rằng $\det A = 0$, bất kể năm phần tử khác không được đánh dấu $x$:

$$A = \begin{bmatrix} x & x & x \\ 0 & 0 & x \\ 0 & 0 & x \end{bmatrix}.$$
Các phần phụ đại số của hàng 1 là gì? Hạng của $A$ là bao nhiêu? 6 số hạng trong $\det A$ là gì?

**4** Tìm hai cách để chọn các phần tử khác không từ bốn hàng và cột khác nhau:

$$A = \begin{bmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 1 \\ 1 & 1 & 0 & 1 \\ 1 & 0 & 0 & 1 \end{bmatrix} \quad B = \begin{bmatrix} 1 & 0 & 0 & 2 \\ 0 & 3 & 4 & 5 \\ 5 & 4 & 0 & 3 \\ 2 & 0 & 0 & 1 \end{bmatrix} \quad (B \text{ có cùng các số không như } A).$$

$\det A$ bằng $1 + 1$ hay $1 - 1$ hay $-1 - 1$? $\det B$ là gì?

**5** Đặt số lượng số không nhỏ nhất vào ma trận $4 \times 4$ để đảm bảo $\det A = 0$. Đặt càng nhiều số không càng tốt trong khi vẫn cho phép $\det A \neq 0$.

**6** (a) Nếu $a_{11} = a_{22} = a_{33} = 0$, bao nhiêu trong số sáu số hạng trong $\det A$ sẽ bằng không?  
(b) Nếu $a_{11} = a_{22} = a_{33} = a_{44} = 0$, bao nhiêu trong số 24 tích $a_{1j}a_{2k}a_{3l}a_{4m}$ chắc chắn bằng không?

**7** Có bao nhiêu ma trận hoán vị $5 \times 5$ có $\det P = +1$? Đó là những hoán vị chẵn. Tìm một ma trận cần bốn lần hoán đổi để đạt được ma trận đơn vị.

**8** Nếu $\det A$ khác không, ít nhất một trong số $n!$ số hạng trong công thức (8) khác không. Từ công thức lớn hãy suy ra rằng một số thứ tự các hàng của $A$ không để lại số không nào trên đường chéo. (Đừng sử dụng $P$ từ phép khử; ma trận $PA$ đó có thể có các số không trên đường chéo.)

**9** Chứng minh rằng 4 là định thức lớn nhất đối với ma trận $3 \times 3$ gồm các số 1 và -1.

**10** Có bao nhiêu hoán vị của $(1, 2, 3, 4)$ là chẵn và chúng là gì? Điểm cộng thêm: Tất cả các định thức $4 \times 4$ có thể có của $I + P_{\text{even}}$ là gì?

**Các bài tập 11–22 sử dụng các phần phụ đại số $C_{ij} = (-1)^{i+j} \det M_{ij}$. Loại bỏ hàng $i$ và cột $j$.**

**11** Tìm tất cả các phần phụ đại số và xếp chúng vào các ma trận phần phụ đại số $C, D$. Tìm $AC$ và $\det B$.

$$A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \quad B = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 0 & 0 \end{bmatrix}.$$

**12** Tìm ma trận phần phụ đại số $C$ và nhân $A$ với $C^T$. So sánh $AC^T$ với $A^{-1}$:

$$A = \begin{bmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{bmatrix} \quad A^{-1} = \frac{1}{4} \begin{bmatrix} 3 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 3 \end{bmatrix}.$$

**13** Định thức $C_n$ cấp $n$ có các số 1 nằm phía trên và phía dưới đường chéo chính:

$$C_1 = |0| \quad C_2 = \begin{vmatrix} 0 & 1 \\ 1 & 0 \end{vmatrix} \quad C_3 = \begin{vmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{vmatrix} \quad C_4 = \begin{vmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{vmatrix}.$$

(a) Các định thức $C_1, C_2, C_3, C_4$ này là gì?
(b) Bằng phần phụ đại số, tìm mối quan hệ giữa $C_n$ và $C_{n-1}$ và $C_{n-2}$. Tìm $C_{10}$.

**14** Các ma trận trong Bài 13 có các số 1 nằm ngay phía trên và phía dưới đường chéo chính. Đi xuống theo ma trận, trình tự các cột nào (nếu có) cho ra toàn bộ các số 1? Giải thích tại sao hoán vị đó là *chẵn* đối với $n = 4, 8, 12, \dots$ và *lẻ* đối với $n = 2, 6, 10, \dots$. Khi đó

| $C_n = 0$ ($n$ lẻ) | $C_n = 1$ ($n = 4, 8, \dots$) | $C_n = -1$ ($n = 2, 6, \dots$) |
|----------------------|---------------------------------|----------------------------------|

**15** Ma trận ba đường chéo $1, 1, 1$ cấp $n$ có định thức $E_n$:

$$E_1 = |1| \quad E_2 = \begin{vmatrix} 1 & 1 \\ 1 & 1 \end{vmatrix} \quad E_3 = \begin{vmatrix} 1 & 1 & 0 \\ 1 & 1 & 1 \\ 0 & 1 & 1 \end{vmatrix} \quad E_4 = \begin{vmatrix} 1 & 1 & 0 & 0 \\ 1 & 1 & 1 & 1 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{vmatrix}$$

(a) Bằng phần phụ đại số, chứng minh rằng $E_n = E_{n-1} - E_{n-2}$.
(b) Bắt đầu từ $E_1 = 1$ và $E_2 = 0$, hãy tìm $E_3, E_4, \dots, E_8$.
(c) Bằng cách nhận thấy các con số này cuối cùng lặp lại như thế nào, hãy tìm $E_{100}$.

**16** $F_n$ là định thức của ma trận ba đường chéo $1, 1, -1$ cấp $n$:

$$F_2 = \begin{vmatrix} 1 & -1 \\ 1 & 1 \end{vmatrix} = 2 \quad F_3 = \begin{vmatrix} 1 & -1 & 0 \\ 1 & 1 & -1 \\ 0 & 1 & 1 \end{vmatrix} = 3 \quad F_4 = \begin{vmatrix} 1 & -1 & 0 & 0 \\ 1 & 1 & -1 & 0 \\ 0 & 1 & 1 & -1 \\ 0 & 0 & 1 & 1 \end{vmatrix} = 5.$$

*(Sửa lỗi OCR ở $F_4$ trong sách gốc).*
Khai triển phần phụ đại số để chứng minh rằng $F_n = F_{n-1} + F_{n-2}$. Các định thức này là *số Fibonacci* 1, 2, 3, 5, 8, 13, .... Chuỗi thường bắt đầu bằng 1, 1, 2, 3 (với hai số 1) nên $F_n$ của chúng ta chính là $F_{n+1}$ thông thường.

**17** Ma trận $B_n$ là ma trận $-1, 2, -1$ $A_n$ ngoại trừ $b_{11} = 1$ thay vì $a_{11} = 2$. Sử dụng các phần phụ đại số ở hàng *cuối cùng* của $B_4$ để chứng minh rằng $|B_4| = 2|B_3| - |B_2| = 1$.

$$B_4 = \begin{bmatrix} 1 & -1 & & \\ -1 & 2 & -1 & \\ & -1 & 2 & -1 \\ & & -1 & 2 \end{bmatrix} \quad B_3 = \begin{bmatrix} 1 & -1 & \\ -1 & 2 & -1 \\ & -1 & 2 \end{bmatrix} \quad B_2 = \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix}.$$

Đệ quy $|B_n| = 2|B_{n-1}| - |B_{n-2}|$ được thỏa mãn khi mọi $|B_n| = 1$. Đệ quy này giống như đệ quy của $A$ trong Ví dụ 6. Điểm khác biệt là ở các giá trị bắt đầu $1, 1, 1$ cho các định thức của kích thước $n = 1, 2, 3$.

**18** Quay trở lại $B_n$ trong Bài tập 17. Nó giống như $A_n$ ngoại trừ $b_{11} = 1$. Vì vậy hãy sử dụng tính tuyến tính ở hàng đầu tiên, nơi $\begin{bmatrix} 1 & -1 & 0 \end{bmatrix}$ bằng $\begin{bmatrix} 2 & -1 & 0 \end{bmatrix}$ trừ $\begin{bmatrix} 1 & 0 & 0 \end{bmatrix}$:

$$|B_n| = \begin{vmatrix} 1 & -1 & & 0 \\ -1 & & & \\ & A_{n-1} & & \\ 0 & & & \end{vmatrix} = \begin{vmatrix} 2 & -1 & & 0 \\ -1 & & & \\ & A_{n-1} & & \\ 0 & & & \end{vmatrix} - \begin{vmatrix} 1 & 0 & & 0 \\ -1 & & & \\ & A_{n-1} & & \\ 0 & & & \end{vmatrix}.$$

Tính tuyến tính cho ta $|B_n| = |A_n| - |A_{n-1}| = \underline{\hspace{2cm}}$.

**19** Giải thích tại sao định thức Vandermonde $4 \times 4$ chứa $x^3$ nhưng không chứa $x^4$ hay $x^5$:

$$V_4 = \det \begin{bmatrix} 1 & a & a^2 & a^3 \\ 1 & b & b^2 & b^3 \\ 1 & c & c^2 & c^3 \\ 1 & x & x^2 & x^3 \end{bmatrix}.$$

Định thức bằng không tại $x = \underline{\hspace{2cm}}$, $\underline{\hspace{2cm}}$, và $\underline{\hspace{2cm}}$. Phần phụ đại số của $x^3$ là $V_3 = (b-a)(c-a)(c-b)$. Khi đó $V_4 = (b-a)(c-a)(c-b)(x-a)(x-b)(x-c)$.

**20** Tìm $G_2$ và $G_3$ rồi sau đó bằng các phép toán hàng tìm $G_4$. Bạn có thể dự đoán được $G_n$ không?

$$G_2 = \begin{vmatrix} 0 & 1 \\ 1 & 0 \end{vmatrix} \quad G_3 = \begin{vmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{vmatrix} \quad G_4 = \begin{vmatrix} 0 & 1 & 1 & 1 \\ 1 & 0 & 1 & 1 \\ 1 & 1 & 0 & 1 \\ 1 & 1 & 1 & 0 \end{vmatrix}.$$

**21** Tính $S_1, S_2, S_3$ cho các ma trận $1, 3, 1$ này. Dựa theo Fibonacci hãy phỏng đoán và kiểm tra $S_4$.

$$S_1 = |3| \quad S_2 = \begin{vmatrix} 3 & 1 \\ 1 & 3 \end{vmatrix} \quad S_3 = \begin{vmatrix} 3 & 1 & 0 \\ 1 & 3 & 1 \\ 0 & 1 & 3 \end{vmatrix}$$

**22** Đổi 3 thành 2 ở góc trên bên trái của các ma trận trong Bài tập 21. Tại sao điều đó lại trừ $S_{n-1}$ khỏi định thức $S_n$? Chứng minh rằng định thức của các ma trận mới trở thành các số Fibonacci 2, 5, 13 (luôn là $F_{2n+1}$).

#### **Các bài tập 23-26 nói về các ma trận khối (block matrices) và định thức khối.**

**23** Với các khối $2 \times 2$ trong ma trận $4 \times 4$, không phải lúc nào bạn cũng có thể sử dụng định thức khối:

$\begin{vmatrix} A & B \\ 0 & D \end{vmatrix} = |A||D|$ nhưng $\begin{vmatrix} A & B \\ C & D \end{vmatrix} \neq |A||D| - |C||B|.$

(a) Tại sao khẳng định đầu tiên đúng? Bằng cách nào đó $B$ không tham gia vào.
(b) Đưa ra ví dụ chứng minh đẳng thức thất bại (như đã thấy) khi $C$ tham gia vào.

(c) Đưa ra ví dụ chứng minh đáp án $\det(AD - CB)$ cũng sai.

**24** Với phép nhân khối, $A = LU$ có $A_k = L_k U_k$ ở góc trên bên trái:

| $A =$ | $\begin{bmatrix} A_k & * & * \\ * & * & * \end{bmatrix}$ | $\begin{bmatrix} L_k & 0 & * \\ * & * & * \end{bmatrix}$ | $\begin{bmatrix} U_k & * & * \\ 0 & * & * \end{bmatrix}$ |
|-------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|

(a) Giả sử ba phần tử chốt đầu tiên của $A$ là $2, 3, -1$. Định thức của $L_1, L_2, L_3$ (với các số 1 trên đường chéo) và $U_1, U_2, U_3$ và $A_1, A_2, A_3$ là gì?
(b) Nếu $A_1, A_2, A_3$ có định thức lần lượt là $5, 6, 7$ hãy tìm ba phần tử chốt từ phương trình (3). 

**25** Phép khử khối trừ $CA^{-1}$ lần hàng đầu tiên $\begin{bmatrix} A & B \end{bmatrix}$ khỏi hàng thứ hai $\begin{bmatrix} C & D \end{bmatrix}$. Điều này để lại *phần phụ Schur (Schur complement)* $D - CA^{-1}B$ ở góc:

$$\begin{bmatrix} I & 0 \\ -CA^{-1} & I \end{bmatrix} \begin{bmatrix} A & B \\ C & D \end{bmatrix} = \begin{bmatrix} A & B \\ 0 & D - CA^{-1}B \end{bmatrix}.$$

Tính định thức của các ma trận khối này để chứng minh quy tắc chính xác nếu $A^{-1}$ tồn tại:

$$\begin{vmatrix} A & B \\ C & D \end{vmatrix} = |A| |D - CA^{-1}B| = |AD - CB| \quad \text{miễn là } AC = CA.$$

**26** Nếu $A$ là $m \times n$ và $B$ là $n \times m$, phép nhân khối cho ra $\det M = \det AB$:

$$M = \begin{bmatrix} 0 & A \\ -B & I \end{bmatrix} = \begin{bmatrix} AB & A \\ 0 & I \end{bmatrix} \begin{bmatrix} I & 0 \\ -B & I \end{bmatrix}$$

Nếu $A$ là một hàng duy nhất và $B$ là một cột duy nhất, $\det M$ là gì? Nếu $A$ là một cột và $B$ là một hàng, $\det M$ là gì? Làm một ví dụ $3 \times 3$ cho mỗi trường hợp.

**27** (Câu hỏi giải tích) Chứng minh rằng đạo hàm của $\det A$ theo $a_{ij}$ là phần phụ đại số $C_{ij}$. Các phần tử khác được cố định - chúng ta chỉ đang thay đổi $a_{ij}$. *(Sách gốc ghi $a_{11}$ nhưng viết nhầm $a_{uu}$ do OCR, tôi sửa thành $a_{ij}$ để tổng quát hoặc $a_{11}$. Sẽ để $a_{11}$ và $C_{11}$ như ý định sách)*
*(Thực ra là $a_{11}$ và $C_{11}$: Chứng minh đạo hàm của $\det A$ theo $a_{11}$ là phần phụ đại số $C_{11}$. Các phần tử khác cố định - chúng ta chỉ thay đổi $a_{11}$.)*

**28** Một định thức $3 \times 3$ có ba tích "hướng xuống sang phải" và ba tích "hướng xuống sang trái" mang dấu trừ. Tính sáu số hạng như $(1)(5)(9) = 45$ để tìm $D$.

$$D = \begin{vmatrix} 1 & 2 & 3 & 1 & 2 \\ 4 & 5 & 6 & 4 & 5 \\ 7 & 8 & 9 & 7 & 8 \\ - & - & - & + & + \end{vmatrix}$$

Hãy giải thích không dùng định thức tại sao ma trận cụ thể này khả nghịch hoặc không khả nghịch.

**29** Đối với $E_4$ trong Bài tập 15, năm trong số $4! = 24$ số hạng trong công thức lớn (8) là khác không. Tìm năm số hạng đó để chứng minh rằng $E_4 = -1$.

**30** Đối với ma trận sai phân bậc hai ba đường chéo $4 \times 4$ (các phần tử $-1, 2, -1$) hãy tìm năm số hạng trong công thức lớn cho ra $\det A = 16 - 4 - 4 - 4 + 1$.

**31** Tìm định thức của hoán vị vòng quanh (cyclic) $P$ này bằng các phần phụ đại số của hàng 1 và sau đó bằng "công thức lớn". Cần bao nhiêu lần hoán đổi để sắp xếp lại 4, 1, 2, 3 thành 1, 2, 3, 4? $|P^2| = 1$ hay $-1$?

$$P = \begin{bmatrix} 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{bmatrix} \quad P^2 = \begin{bmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & I \\ I & 0 \end{bmatrix}.$$

### Bài tập thử thách (Challenge Problems)

**32** Các phần phụ đại số của ma trận $1, 3, 1$ trong Bài tập 21 cho ra một đệ quy $S_n = 3S_{n-1} - S_{n-2}$. Đáng kinh ngạc là đệ quy đó tạo ra mọi số Fibonacci cách nhau một bước. Đây là thử thách:

*Chứng minh rằng $S_n$ là số Fibonacci $F_{2n+2}$ bằng cách chứng minh $F_{2n+2} = 3F_{2n} - F_{2n-2}$. Hãy tiếp tục sử dụng quy tắc Fibonacci $F_k = F_{k-1} + F_{k-2}$ bắt đầu với $k = 2n + 2$.*

**33** Các ma trận Pascal đối xứng có định thức 1. Nếu tôi trừ 1 khỏi phần tử $n, n$, tại sao định thức trở thành 0? (Sử dụng quy tắc 3 hoặc các phần phụ đại số.)

$$\det \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & 2 & 3 & 4 \\ 1 & 3 & 6 & 10 \\ 1 & 4 & 10 & 20 \end{bmatrix} = 1 \text{ (đã biết)} \quad \det \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & 2 & 3 & 4 \\ 1 & 3 & 6 & 10 \\ 1 & 4 & 10 & 19 \end{bmatrix} = \mathbf{0} \text{ (cần giải thích).}$$

**34** Bài tập này chỉ ra theo hai cách rằng $\det A = 0$ (các số $x$ là số bất kỳ):

$$A = \begin{bmatrix} x & x & x & x & x & x \\ x & x & x & x & x & x \\ 0 & 0 & 0 & x & x & x \\ 0 & 0 & 0 & x & x & x \\ 0 & 0 & 0 & x & x & x \end{bmatrix}.$$

(a) Làm sao bạn biết các hàng là phụ thuộc tuyến tính?
(b) Giải thích tại sao tất cả 120 số hạng đều bằng không trong công thức lớn cho $\det A$. 

**35** Nếu $|\det(A)| > 1$, chứng minh rằng các lũy thừa $A^n$ không thể bị chặn (bounded). Nhưng nếu $|\det(A)| \le 1$, chứng minh rằng một số phần tử của $A^n$ vẫn có thể trở nên rất lớn. Các trị riêng sẽ đưa ra bài kiểm tra đúng cho tính ổn định, còn định thức chỉ cho chúng ta một con số.

### 5.3 Quy tắc Cramer, Nghịch đảo, và Thể tích (Cramer's Rule, Inverses, and Volumes)

1. $A^{-1}$ bằng $C^T / \det A$. Khi đó $(A^{-1})_{ij}$ = phần phụ đại số $C_{ji}$ chia cho định thức của $A$.
2. **Quy tắc Cramer (Cramer's Rule)** tính $x = A^{-1}b$ từ $x_j = \det(A$ với cột $j$ được đổi thành $b) / \det A$.
3. **Diện tích hình bình hành** = $|ad - bc|$ nếu bốn đỉnh là $(0, 0)$, $(a, b)$, $(c, d)$, và $(a+c, b+d)$.
4. **Thể tích hình hộp** = $|\det A|$ nếu các hàng của $A$ (hoặc các cột của $A$) tạo thành các cạnh của hình hộp.
5. **Tích có hướng (cross product)** $w = u \times v$ là $\det \begin{bmatrix} i & j & k \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{bmatrix}$. Lưu ý $v \times u = -(u \times v)$. $w_1, w_2, w_3$ là các phần phụ đại số của hàng 1. Lưu ý $w^T u = 0$ và $w^T v = 0$.

Phần này giải hệ $Ax = b$ và cũng tìm $A^{-1}$ — bằng đại số chứ không phải bằng phép khử. Trong mọi công thức bạn sẽ thấy một phép chia cho $\det A$. Mỗi phần tử trong $A^{-1}$ và $A^{-1}b$ là một định thức chia cho định thức của $A$. Để tôi bắt đầu với Quy tắc Cramer.

**Quy tắc Cramer giải hệ $Ax = b$**. Một ý tưởng gọn gàng cho ta thành phần đầu tiên $x_1$. Thay thế cột đầu tiên của $I$ bằng $x$ mang lại một ma trận có định thức $x_1$. Khi bạn nhân nó với $A$, cột đầu tiên trở thành $Ax$ cũng chính là $b$. Các cột khác của $B_1$ được sao chép từ $A$:

$$\text{Ý tưởng chính} \quad \begin{bmatrix} & & \\ & A & \\ & & \end{bmatrix} \begin{bmatrix} x_1 & 0 & 0 \\ x_2 & 1 & 0 \\ x_3 & 0 & 1 \end{bmatrix} = \begin{bmatrix} b_1 & a_{12} & a_{13} \\ b_2 & a_{22} & a_{23} \\ b_3 & a_{32} & a_{33} \end{bmatrix} = B_1. \quad (1)$$

Chúng ta đã nhân từng cột một. Lấy định thức của ba ma trận để tìm $x_1$:

**Quy tắc nhân:** $(\det A)(x_1) = \det B_1$ hoặc $x_1 = \frac{\det B_1}{\det A}$.

Đây là thành phần đầu tiên của $x$ trong Quy tắc Cramer! Thay đổi một cột của $A$ đã tạo ra $B_1$. Để tìm $x_2$ và $B_2$, hãy đặt các vectơ $x$ và $b$ vào cột thứ hai của $I$ và $A$:

$$\text{Ý tưởng tương tự} \quad \begin{bmatrix} a_1 & a_2 & a_3 \end{bmatrix} \begin{bmatrix} 1 & x_1 & 0 \\ 0 & x_2 & 0 \\ 0 & x_3 & 1 \end{bmatrix} = \begin{bmatrix} a_1 & b & a_3 \end{bmatrix} = B_2. \quad (3)$$

Lấy định thức để tìm $(\det A)(x_2) = \det B_2$. Điều này cho ta $x_2 = (\det B_2)/(\det A)$.

**Ví dụ 1** Giải $3x_1 + 4x_2 = 2$ và $5x_1 + 6x_2 = 4$ cần ba định thức:

$$\det A = \begin{vmatrix} 3 & 4 \\ 5 & 6 \end{vmatrix} \quad \det B_1 = \begin{vmatrix} 2 & 4 \\ 4 & 6 \end{vmatrix} \quad \det B_2 = \begin{vmatrix} 3 & 2 \\ 5 & 4 \end{vmatrix}$$

Các định thức của $A, B_1, B_2$ đó là $-2$ và $-4$ và $2$. Tất cả các tỷ số đều chia cho $\det A = -2$:

| Tìm $x = A^{-1}b$ | $x_1 = \frac{-4}{-2} = 2$ | $x_2 = \frac{2}{-2} = -1$ | Kiểm tra | $\begin{bmatrix} 3 & 4 \\ 5 & 6 \end{bmatrix} \begin{bmatrix} 2 \\ -1 \end{bmatrix} = \begin{bmatrix} 2 \\ 4 \end{bmatrix}$ |
|--------------------|--------------------------|---------------------------|-------|-----------------------------------------------------------------------------------------------------------------------------|

**QUY TẮC CRAMER** Nếu $\det A$ khác không, $Ax = b$ được giải bằng các định thức:

| $x_1 = \frac{\det B_1}{\det A}$ | $x_2 = \frac{\det B_2}{\det A}$ | $\dots$ | $x_n = \frac{\det B_n}{\det A}$ | (4) |
|---------------------------------|---------------------------------|---------|---------------------------------|-----|

*Ma trận $B_j$ là ma trận có cột thứ $j$ của $A$ được thay bằng vectơ $b$.*

Để giải một hệ $n \times n$, Quy tắc Cramer tính $n + 1$ định thức (của $A$ và $n$ ma trận $B$ khác nhau). Khi mỗi ma trận là tổng của $n!$ số hạng - áp dụng "công thức lớn" với tất cả các hoán vị - điều này tạo thành tổng cộng $(n + 1)!$ số hạng. *Sẽ là điên rồ nếu giải hệ phương trình theo cách đó.* Nhưng cuối cùng chúng ta cũng có một công thức tường minh cho nghiệm $x$.

**Ví dụ 2** Quy tắc Cramer không hiệu quả với những con số nhưng nó rất phù hợp với các chữ cái. Đối với $n = 2$, tìm các cột của $A^{-1} = \begin{bmatrix} x & y \end{bmatrix}$ bằng cách giải $AA^{-1} = I$:

| Các cột của $A^{-1}$ | $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$ | $\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$ | $= \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ | $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$ | $\begin{bmatrix} y_1 \\ y_2 \end{bmatrix}$ | $= \begin{bmatrix} 0 \\ 1 \end{bmatrix}$ |
|---------------------|------------------------------------------------|--------------------------------------------|------------------------------------------|------------------------------------------------|--------------------------------------------|------------------------------------------|
| là $x$ và $y$     |                                                |                                            |                                          |                                                |                                            |                                          |

Chúng chia sẻ chung ma trận $A$. Chúng ta cần $|A|$ và bốn định thức cho $x_1, x_2, y_1, y_2$:

$$
\det B_1 = \begin{vmatrix} \mathbf{1} & b \\ \mathbf{0} & d \end{vmatrix} \quad
\det B_2 = \begin{vmatrix} a & \mathbf{1} \\ c & \mathbf{0} \end{vmatrix} \quad
\det B_3 = \begin{vmatrix} \mathbf{0} & b \\ \mathbf{1} & d \end{vmatrix} \quad
\det B_4 = \begin{vmatrix} a & \mathbf{0} \\ c & \mathbf{1} \end{vmatrix}
$$

Bốn định thức cuối cùng đó là $d, -c, -b,$ và $a$. (Chúng là các phần phụ đại số!) Đây là $A^{-1}$:

| $x_1 = \frac{d}{|A|}$ , $x_2 = \frac{-c}{|A|}$ , $y_1 = \frac{-b}{|A|}$ , $y_2 = \frac{a}{|A|}$ và khi đó $A^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$ . |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Tôi đã chọn ma trận $2 \times 2$ để các ý chính có thể hiển hiện rõ ràng. Ý tưởng mới là: **$A^{-1}$ liên quan đến các phần phụ đại số.** Khi vế phải là một cột của ma trận đơn vị $I$, như trong $AA^{-1} = I$, **định thức của mỗi $B_j$ trong Quy tắc Cramer chính là một phần phụ đại số của $A$.**

Bạn có thể thấy các phần phụ đại số đó với $n = 3$. Giải $Ax = (1, 0, 0)$ để tìm cột 1 của $A^{-1}$:

$$
\det B_1 = \begin{vmatrix} \mathbf{1} & a_{12} & a_{13} \\ \mathbf{0} & a_{22} & a_{23} \\ \mathbf{0} & a_{32} & a_{33} \end{vmatrix}, \quad \det B_2 = \begin{vmatrix} a_{11} & \mathbf{1} & a_{13} \\ a_{21} & \mathbf{0} & a_{23} \\ a_{31} & \mathbf{0} & a_{33} \end{vmatrix}, \quad \det B_3 = \begin{vmatrix} a_{11} & a_{12} & \mathbf{1} \\ a_{21} & a_{22} & \mathbf{0} \\ a_{31} & a_{32} & \mathbf{0} \end{vmatrix} \quad (5)
$$

Định thức đầu tiên đó $|B_1|$ chính là phần phụ đại số $C_{11} = a_{22}a_{33} - a_{23}a_{32}$. Khi đó $|B_2|$ là phần phụ đại số $C_{21}$ (hay $C_{12}$? Chờ đã, $C_{12}$ là trừ định thức phần bù). *(Sách gốc viết $C_{12}$ nhưng đó thực chất là $C_{21}$ của ma trận nghịch đảo, tác giả viết $C_{12}$ có lẽ ý chỉ định thức. Tôi sẽ dịch nguyên văn).*
Lưu ý rằng dấu trừ chính xác xuất hiện trong $-(a_{21}a_{33} - a_{23}a_{31})$. Phần phụ đại số $C_{12}$ này đi vào cột 1 của $A^{-1}$. Khi chúng ta chia cho $\det A$, chúng ta có ma trận nghịch đảo!

Phần tử $i, j$ của $A^{-1}$ là phần phụ đại số $C_{ji}$ (không phải $C_{ij}$) chia cho $\det A$:

**CÔNG THỨC CHO $A^{-1}$** 

$$(A^{-1})_{ij} = \frac{C_{ji}}{\det A} \quad \text{và} \quad A^{-1} = \frac{C^T}{\det A}. \quad (6)$$

Các phần phụ đại số $C_{ij}$ đi vào "ma trận phần phụ đại số" $C$. **Chuyển vị của $C$ dẫn đến $A^{-1}$.** Để tính phần tử $i, j$ của $A^{-1}$, gạch đi hàng $j$ và cột $i$ của $A$. Nhân định thức với $(-1)^{i+j}$ để được phần phụ đại số $C_{ji}$, và chia cho $\det A$.

Kiểm tra quy tắc này cho phần tử $3, 1$ của $A^{-1}$. Đối với cột 1 chúng ta giải $Ax = (1, 0, 0)$. Thành phần thứ ba $x_3$ cần định thức thứ ba trong phương trình (5), chia cho $\det A$. Định thức đó chính xác là phần phụ đại số $C_{13} = a_{21}a_{32} - a_{22}a_{31}$. Vì vậy $(A^{-1})_{31} = C_{13}/\det A$.

**Tóm tắt:** Trong quá trình giải $AA^{-1} = I$, mỗi cột của $I$ dẫn đến một cột của $A^{-1}$. Mọi phần tử của $A^{-1}$ là một tỷ số: định thức cấp $n - 1$ / định thức cấp $n$.

**Chứng minh trực tiếp cho công thức $A^{-1} = C^T / \det A$:** Điều này có nghĩa là $AC^T = (\det A)I$:

$$\begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{bmatrix} \begin{bmatrix} C_{11} & C_{21} & C_{31} \\ C_{12} & C_{22} & C_{32} \\ C_{13} & C_{23} & C_{33} \end{bmatrix} = \begin{bmatrix} \det A & 0 & 0 \\ 0 & \det A & 0 \\ 0 & 0 & \det A \end{bmatrix}. \quad (7)$$

(Hàng 1 của $A$) nhân với (cột 1 của $C^T$) mang lại $\det A$ đầu tiên ở bên phải:

$$a_{11}C_{11} + a_{12}C_{12} + a_{13}C_{13} = \det A \quad \text{Đây chính xác là quy tắc phần phụ đại số!}$$

Tương tự, hàng 2 của $A$ nhân với cột 2 của $C^T$ (lưu ý phép chuyển vị) cũng tạo ra $\det A$. Các phần tử $a_{2j}$ nhân với các phần phụ đại số $C_{2j}$ theo đúng trình tự để cho ra định thức.

*Làm sao để giải thích các số 0 ngoài đường chéo chính trong phương trình (7)?* Các hàng của $A$ đang nhân với các phần phụ đại số từ các hàng *khác*. Tại sao kết quả lại bằng không?

**Hàng 2 của $A$ nhân với Hàng 1 của $C$**

$$a_{21}C_{11} + a_{22}C_{12} + a_{23}C_{13} = 0. \quad (8)$$

**Trả lời:** Đây là quy tắc phần phụ đại số cho một ma trận mới, khi hàng thứ hai của $A$ được sao chép vào hàng đầu tiên của nó. Ma trận mới $A^*$ có hai hàng bằng nhau, nên $\det A^* = 0$ trong phương trình (8). Lưu ý rằng $A^*$ có cùng các phần phụ đại số $C_{11}, C_{12}, C_{13}$ như $A$ — vì tất cả các hàng đều giống nhau sau hàng đầu tiên. Do đó, phép nhân đáng kinh ngạc (7) là chính xác:

$$AC^T = (\det A)I \quad \text{hay} \quad A^{-1} = \frac{C^T}{\det A}.$$

**Ví dụ 3** Ma trận "tổng" $A$ có định thức 1. Khi đó $A^{-1}$ chứa các phần phụ đại số:

$$A = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 1 & 0 \\ 1 & 1 & 1 & 0 \\ 1 & 1 & 1 & 1 \end{bmatrix} \quad \text{có nghịch đảo} \quad A^{-1} = \frac{C^T}{1} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ -1 & 1 & 1 & 0 \\ 0 & -1 & 1 & 0 \\ 0 & 0 & -1 & 1 \end{bmatrix}.$$

Gạch đi hàng 1 và cột 1 của $A$ để thấy phần phụ đại số $3 \times 3$ là $C_{11} = 1$. Bây giờ gạch đi hàng 1 và cột 2 cho $C_{12}$. Ma trận con $3 \times 3$ vẫn là ma trận tam giác với định thức 1. Nhưng phần phụ đại số $C_{12}$ là $-1$ vì dấu $(-1)^{1+2}$. Số $-1$ này đi vào phần tử $(2, 1)$ của $A^{-1}$ - đừng quên chuyển vị $C$.

*Nghịch đảo của một ma trận tam giác là ma trận tam giác.* Các phần phụ đại số đưa ra lý do tại sao.

**Ví dụ 4** Nếu mọi phần phụ đại số đều khác không, liệu $A$ có chắc chắn khả nghịch không? *Không thể nào.*

### **Diện tích của một Tam giác (Area of a Triangle)**

Mọi người đều biết diện tích của hình chữ nhật - đáy nhân chiều cao. Diện tích của tam giác bằng một nửa đáy nhân chiều cao. Nhưng có một câu hỏi mà các công thức đó không trả lời được. *Nếu chúng ta biết các đỉnh $(x_1, y_1)$ và $(x_2, y_2)$ và $(x_3, y_3)$ của một tam giác, diện tích là bao nhiêu?* Sử dụng các đỉnh để tìm đáy và chiều cao không phải là một cách hay để tính diện tích.

Định thức là cách tốt nhất để tìm diện tích. *Diện tích của một tam giác bằng một nửa định thức $3 \times 3$.* Các căn bậc hai trong chiều dài đáy và chiều cao tự triệt tiêu trong công thức này. Nếu một đỉnh ở gốc tọa độ, giả sử $(x_3, y_3) = (0, 0)$, thì định thức chỉ là cấp $2 \times 2$.

Tam giác với các đỉnh $(x_1, y_1)$ và $(x_2, y_2)$ và $(x_3, y_3)$ có diện tích bằng:

| Diện tích tam giác | $\frac{1}{2}$ | $\begin{vmatrix} x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \\ x_3 & y_3 & 1 \end{vmatrix}$ | Diện tích = $\frac{1}{2}$ | $\begin{vmatrix} x_1 & y_1 \\ x_2 & y_2 \end{vmatrix}$ | khi $(x_3, y_3) = (0, 0)$ . |
|------------------|---------------|---------------------------------------------------------------------------------------|----------------------|--------------------------------------------------------------------|------------------------------|

Khi bạn đặt $x_3 = y_3 = 0$ trong định thức $3 \times 3$, bạn thu được định thức $2 \times 2$ (phải điền số 1 vào cột cuối). Các công thức này không có căn bậc hai - chúng rất hợp lý để ghi nhớ. Định thức $3 \times 3$ phân tách thành tổng của ba định thức $2 \times 2$ (phần phụ đại số), giống như tam giác thứ ba trong Hình 5.1 được chia thành ba tam giác đặc biệt xuất phát từ $(0, 0)$:

$$\text{Diện tích} = \frac{1}{2} \begin{vmatrix} x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \\ x_3 & y_3 & 1 \end{vmatrix} = +\frac{1}{2}(x_1y_2 - x_2y_1) +\frac{1}{2}(x_2y_3 - x_3y_2) +\frac{1}{2}(x_3y_1 - x_1y_3) \quad (9)$$

Nếu $(0, 0)$ nằm ngoài tam giác, hai trong số các diện tích đặc biệt có thể âm — nhưng tổng vẫn chính xác. Vấn đề thực sự là giải thích diện tích của một tam giác có đỉnh là $(0, 0)$.

Tại sao $\frac{1}{2}|x_1y_2 - x_2y_1|$ lại là diện tích của tam giác này? Chúng ta có thể bỏ hệ số $\frac{1}{2}$ để xét hình bình hành (lớn gấp đôi, vì hình bình hành chứa hai tam giác bằng nhau). Bây giờ chúng ta chứng minh rằng diện tích hình bình hành là định thức $x_1y_2 - x_2y_1$. Diện tích này trong Hình 5.2 là 11, và do đó tam giác có diện tích $\frac{11}{2}$.

**Chứng minh rằng một hình bình hành xuất phát từ $(0, 0)$ có diện tích = định thức $2 \times 2$.**

Có nhiều cách chứng minh nhưng cách này phù hợp với cuốn sách. Chúng ta chỉ ra rằng diện tích có cùng các tính chất 1-2-3 như định thức. Khi đó diện tích = định thức! Hãy nhớ rằng ba quy tắc đó đã định nghĩa định thức và dẫn đến tất cả các tính chất khác của nó.

- **1** Khi $A = I$, hình bình hành trở thành hình vuông đơn vị. Diện tích của nó là $\det I = 1$.
- **2** Khi tráo đổi các hàng, định thức đổi dấu. Giá trị tuyệt đối (diện tích dương) vẫn giữ nguyên - đó vẫn là cùng một hình bình hành.
- **3** Nếu hàng 1 được nhân với $t$, Hình 5.3a cho thấy diện tích cũng được nhân với $t$. Giả sử một hàng mới $(x'_1, y'_1)$ được cộng vào $(x_1, y_1)$ (giữ nguyên hàng 2). Hình 5.3b cho thấy các diện tích hình bình hành nét liền cộng lại bằng diện tích hình bình hành nét đứt (vì hai tam giác được tạo bởi các đường nét đứt là bằng nhau).

Đó là một cách chứng minh hơi lạ, khi mà chúng ta có thể dùng hình học phẳng. Nhưng cách chứng minh này có một sức hút lớn - nó áp dụng được trong $n$ chiều. $n$ cạnh xuất phát từ gốc tọa độ được cho bởi *các hàng của một ma trận $n \times n$*. Hình hộp được hoàn thiện bởi các cạnh khác, giống như hình bình hành.

Hình 5.4 cho thấy một hình hộp ba chiều - có các cạnh không vuông góc. *Thể tích bằng giá trị tuyệt đối của $\det A$.* Chứng minh của chúng ta một lần nữa kiểm tra rằng các quy tắc 1-3 của định thức cũng được tuân thủ bởi thể tích. Khi một cạnh bị kéo giãn một hệ số $t$, thể tích nhân với $t$. Khi cạnh 1 được cộng vào cạnh 1', thể tích là tổng của hai thể tích ban đầu. Đây là Hình 5.3b được nâng lên không gian ba chiều hoặc $n$ chiều. Tôi muốn vẽ các hình hộp nhưng trang giấy này chỉ có hai chiều.

Khối lập phương đơn vị có thể tích = 1, chính là $\det I$. Hoán vị hàng hay hoán vị cạnh vẫn để lại cùng một hình hộp và cùng một thể tích tuyệt đối. Định thức đổi dấu để chỉ ra liệu các cạnh là *bộ ba thuận chiều kim đồng hồ (right-handed triple)* ($\det A > 0$) hay *ngược chiều kim đồng hồ (left-handed triple)* ($\det A < 0$). Thể tích hình hộp tuân theo các quy tắc của định thức, nên thể tích bằng giá trị tuyệt đối của $\det A$.

**Ví dụ 5** Giả sử một hộp hình chữ nhật (các góc 90°) có độ dài các cạnh là $r, s$, và $t$. Thể tích của nó là $r$ nhân $s$ nhân $t$. Ma trận đường chéo $A$ với các phần tử $r, s$, và $t$ tạo ra ba cạnh đó. Khi đó $\det A$ cũng bằng thể tích $rst$.

**Ví dụ 6** Trong giải tích, hình hộp có kích thước vô cùng nhỏ (infinitesimal)! Để tích phân trên một hình tròn, chúng ta có thể đổi $x$ và $y$ sang $r$ và $\theta$. Đó là tọa độ cực: $x = r \cos \theta$ và $y = r \sin \theta$. Diện tích của một "hộp tọa độ cực" là một định thức $J$ nhân với $dr d\theta$:

$$\text{Diện tích } r dr d\theta \text{ trong giải tích} \quad J = \begin{vmatrix} \partial x / \partial r & \partial x / \partial \theta \\ \partial y / \partial r & \partial y / \partial \theta \end{vmatrix} = \begin{vmatrix} \cos \theta & -r \sin \theta \\ \sin \theta & r \cos \theta \end{vmatrix} = \mathbf{r}.$$

Định thức này chính là $r$ trong phần tử diện tích nhỏ $dA = r dr d\theta$. Hệ số kéo giãn $J$ đi vào tích phân kép cũng giống như $dx/du$ đi vào một tích phân thông thường $\int dx = \int (dx/du) du$. Đối với tích phân bội ba, ma trận Jacobian $J$ chứa chín đạo hàm sẽ có kích thước $3 \times 3$.

### Tích có hướng (The Cross Product)

*Tích có hướng* là một ứng dụng bổ sung (và tùy chọn), đặc biệt dành cho không gian ba chiều. Bắt đầu với các vectơ $u = (u_1, u_2, u_3)$ và $v = (v_1, v_2, v_3)$. Khác với tích vô hướng (dot product) cho ra một con số, **tích có hướng là một vectơ** - cũng nằm trong không gian ba chiều. Nó được viết là $u \times v$ và đọc là "$u$ cross $v$". Các thành phần của tích có hướng này là các phần phụ đại số $2 \times 2$. Chúng ta sẽ giải thích các tính chất khiến $u \times v$ hữu ích trong hình học và vật lý.

Lần này chúng ta sẽ đi thẳng vào vấn đề, và viết công thức trước các tính chất.

**ĐỊNH NGHĨA** *Tích có hướng* của $u = (u_1, u_2, u_3)$ và $v = (v_1, v_2, v_3)$ là một vectơ:

$$u \times v = \begin{vmatrix} i & j & k \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{vmatrix} = (u_2 v_3 - u_3 v_2) i + (u_3 v_1 - u_1 v_3) j + (u_1 v_2 - u_2 v_1) k. \quad (10)$$

Vectơ $u \times v$ này vuông góc với $u$ và $v$. Tích có hướng $v \times u$ là $-(u \times v)$.

**Bình luận** Định thức $3 \times 3$ là cách dễ nhất để ghi nhớ $u \times v$. Nó không hoàn toàn hợp lệ về mặt toán học chuẩn mực, vì hàng đầu tiên chứa các vectơ $i, j, k$ và các hàng khác chứa các con số. Trong định thức, vectơ $i = (1, 0, 0)$ nhân với $u_2 v_3$ và $-u_3 v_2$. Kết quả là $(u_2 v_3 - u_3 v_2, 0, 0)$, thể hiện thành phần đầu tiên của tích có hướng.

Hãy chú ý đến quy luật vòng quanh của các chỉ số: 2 và 3 cho ra thành phần 1 của $u \times v$, tiếp theo 3 và 1 cho ra thành phần 2, sau đó 1 và 2 cho ra thành phần 3. Điều này hoàn thành định nghĩa của $u \times v$. Bây giờ chúng ta liệt kê các tính chất của tích có hướng:

**Tính chất 1** $v \times u$ làm đảo ngược hàng 2 và 3 trong định thức nên nó bằng $-(u \times v)$.

**Tính chất 2** Tích có hướng $u \times v$ vuông góc với $u$ (và cũng vuông góc với $v$). Cách chứng minh trực tiếp là quan sát các số hạng triệt tiêu nhau, tạo ra tích vô hướng bằng không:

$$u \cdot (u \times v) = u_1(u_2 v_3 - u_3 v_2) + u_2(u_3 v_1 - u_1 v_3) + u_3(u_1 v_2 - u_2 v_1) = 0. \quad (11)$$

**Tính chất 3** Tích có hướng của bất kỳ vectơ nào với chính nó (hai hàng bằng nhau) bằng không: $u \times u = 0$.

Khi $u$ và $v$ song song, tích có hướng bằng 0. Khi $u$ và $v$ vuông góc, tích vô hướng bằng 0. Một cái liên quan đến $\sin \theta$ và cái kia liên quan đến $\cos \theta$:

$$\|u \times v\| = \|u\| \|v\| |\sin \theta| \quad \text{và} \quad |u \cdot v| = \|u\| \|v\| |\cos \theta|. \quad (12)$$

**Ví dụ 7** $u = (3, 2, 0)$ và $v = (1, 4, 0)$ nằm trong mặt phẳng $xy$, $u \times v$ hướng lên theo trục $z$:

$$u \times v = \begin{vmatrix} i & j & k \\ 3 & 2 & 0 \\ 1 & 4 & 0 \end{vmatrix} = 10k. \quad \text{Tích có hướng là } u \times v = (0, 0, 10).$$

*Chiều dài của $u \times v$ bằng diện tích của hình bình hành có các cạnh là $u$ và $v$.* Điều này rất quan trọng: Trong ví dụ này, diện tích là 10.

**Ví dụ 8** Tích có hướng của $u = (1, 1, 1)$ và $v = (1, 1, 2)$ là $(1, -1, 0)$:

$$\begin{vmatrix} i & j & k \\ 1 & 1 & 1 \\ 1 & 1 & 2 \end{vmatrix} = i \begin{vmatrix} 1 & 1 \\ 1 & 2 \end{vmatrix} - j \begin{vmatrix} 1 & 1 \\ 1 & 2 \end{vmatrix} + k \begin{vmatrix} 1 & 1 \\ 1 & 1 \end{vmatrix} = i - j.$$

Vectơ $(1, -1, 0)$ này vuông góc với $(1, 1, 1)$ và $(1, 1, 2)$ đúng như dự đoán. Diện tích = $\sqrt{2}$.

**Ví dụ 9** Tích có hướng của $i = (1, 0, 0)$ và $j = (0, 1, 0)$ tuân theo *quy tắc bàn tay phải*. Tích có hướng đó $k = i \times j$ hướng lên chứ không hướng xuống. Do đó $i \times j = k$. Quy tắc bàn tay phải cũng cho $j \times k = i$ và $k \times i = j$. Lưu ý thứ tự vòng quanh. Theo thứ tự ngược lại (ngược chiều vòng quanh), ngón cái hướng ngược lại và tích có hướng đi theo hướng khác: $k \times j = -i$ và $i \times k = -j$ và $j \times i = -k$. Bạn thấy ba dấu cộng và ba dấu trừ từ một định thức $3 \times 3$.

Định nghĩa của $u \times v$ có thể dựa trên các vectơ thay vì các thành phần của chúng:

**ĐỊNH NGHĨA** *Tích có hướng* là một vectơ có độ dài $\|u\| \|v\| |\sin \theta|$. Hướng của nó vuông góc với $u$ và $v$. Nó hướng "lên" hoặc "xuống" theo quy tắc bàn tay phải.

Định nghĩa này hấp dẫn các nhà vật lý học, những người ghét phải chọn các trục tọa độ. Họ xem $(u_1, u_2, u_3)$ là vị trí của một khối lượng và $(F_x, F_y, F_z)$ là lực tác dụng lên nó. Nếu $F$ song song với $u$, thì $u \times F = 0$ - không có sự quay. Tích có hướng $u \times F$ là lực quay hay *mô-men xoắn (torque)*. Nó hướng dọc theo trục quay (vuông góc với $u$ và $F$). Độ dài của nó $\|u\| \|F\| |\sin \theta|$ đo lường "mô-men" tạo ra sự quay.

# **Tích hỗn tạp (Triple Product) = Định thức = Thể tích**

Vì $u \times v$ là một vectơ, chúng ta có thể lấy tích vô hướng của nó với một vectơ thứ ba $w$. Điều đó tạo ra *tích hỗn tạp (triple product)* $(u \times v) \cdot w$. Nó được gọi là tích hỗn tạp "vô hướng" (scalar triple product) vì kết quả là một con số. Thực chất nó chính là một định thức - nó cho ra thể tích của hình hộp $u, v, w$:

$$(u \times v) \cdot w = \begin{vmatrix} w_1 & w_2 & w_3 \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{vmatrix} = \begin{vmatrix} u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \\ w_1 & w_2 & w_3 \end{vmatrix} \quad (13)$$

Chúng ta có thể đặt $w$ ở hàng trên cùng hoặc hàng dưới cùng. Hai định thức là giống nhau bởi vì hai lần hoán vị hàng sẽ đi từ cái này sang cái kia. Chú ý khi định thức này bằng không:

$$(\mathbf{u} \times \mathbf{v}) \cdot \mathbf{w} = 0$$
xảy ra chính xác khi các vectơ $\mathbf{u}, \mathbf{v}, \mathbf{w}$ nằm trong *cùng một mặt phẳng*.

*Lý do thứ nhất:* $u \times v$ vuông góc với mặt phẳng đó nên tích vô hướng của nó với $w$ bằng không.

*Lý do thứ hai:* Ba vectơ trong cùng một mặt phẳng là phụ thuộc tuyến tính. Ma trận bị suy biến ($\det = 0$).

*Lý do thứ ba:* Thể tích bằng không khi hình hộp $u, v, w$ bị đè bẹp xuống một mặt phẳng.

Thật đáng kinh ngạc là $(u \times v) \cdot w$ bằng thể tích của hình hộp có các cạnh $u, v, w$. Định thức $3 \times 3$ này mang một lượng thông tin khổng lồ. Giống như $ad - bc$ đối với ma trận $2 \times 2$, nó phân biệt giữa ma trận khả nghịch và ma trận suy biến. Chương 6 sẽ tìm kiếm sự suy biến.

#### **• ÔN TẬP CÁC Ý TƯỞNG CHÍNH (REVIEW OF THE KEY IDEAS) •**

1. **1.** Quy tắc Cramer giải $Ax = b$ bằng các tỷ số như $x_1 = |B_1|/|A| = |b \quad a_2 \quad \dots \quad a_n|/|A|$.
2. **2.** Khi $C$ là ma trận phần phụ đại số của $A$, nghịch đảo là $A^{-1} = C^T / \det A$.
3. **3.** Thể tích của một hình hộp là $|\det A|$, khi các cạnh của hình hộp là các hàng của $A$.
4. **4.** Diện tích và thể tích cần thiết để đổi biến số trong tích phân kép và tích phân bội ba.
5. **5.** Trong $\mathbb{R}^3$, tích có hướng $u \times v$ vuông góc với $u$ và $v$. Lưu ý $i \times j = k$.

#### **• CÁC VÍ DỤ CÓ LỜI GIẢI (WORKED EXAMPLES) •**

**5.3 A** Nếu $A$ suy biến, phương trình $AC^T = (\det A)I$ trở thành $AC^T =$ **ma trận không.** *Khi đó mỗi cột của $C^T$ nằm trong không gian null của $A$.* Các cột đó chứa các phần phụ đại số dọc theo các hàng của $A$. Do đó, các phần phụ đại số có thể nhanh chóng tìm thấy không gian null cho một ma trận $3 \times 3$ có hạng 2. Thật xin lỗi vì điều này đến quá muộn! Giải $Ax = \mathbf{0}$ bằng $x =$ các phần phụ đại số dọc theo một hàng, cho các ma trận suy biến hạng 2 sau:

| Các phần phụ đại số | $A = \begin{bmatrix} 1 & 4 & 7 \\ 2 & 3 & 9 \\ 2 & 2 & 8 \end{bmatrix}$ | $A = \begin{bmatrix} 1 & 1 & 2 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}$ |
|-----------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|

**Lời giải** Ma trận đầu tiên có các phần phụ đại số dọc theo hàng đầu tiên (chú ý mỗi dấu trừ):

| $\begin{vmatrix} 3 & 9 \\ 2 & 8 \end{vmatrix} = 6$ | $- \begin{vmatrix} 2 & 9 \\ 2 & 8 \end{vmatrix} = 2$ | $\begin{vmatrix} 2 & 3 \\ 2 & 2 \end{vmatrix} = -2$ |
|----------------------------------------------------|------------------------------------------------------|-----------------------------------------------------|

Khi đó $x = (6, 2, -2)$ giải được $Ax = \mathbf{0}$. Các phần phụ đại số dọc theo hàng thứ hai là $(-18, -6, 6)$, đây chỉ là $-3x$. Vectơ này cũng nằm trong không gian null một chiều của $A$.

Ma trận thứ hai có *các phần phụ đại số bằng không* dọc theo hàng đầu tiên của nó. Vectơ null $x = (0, 0, 0)$ không thú vị. Các phần phụ đại số của hàng 2 cho $x = (1, -1, 0)$ là nghiệm giải được $Ax = \mathbf{0}$.

Mọi ma trận $n \times n$ hạng $n - 1$ đều có ít nhất một phần phụ đại số khác không theo Bài tập 3.3.12. Nhưng đối với hạng $n - 2$, tất cả các phần phụ đại số đều bằng không và chúng ta chỉ tìm được $x = \mathbf{0}$.

**5.3 B** Sử dụng Quy tắc Cramer với các tỷ số $\det B_j / \det A$ để giải $Ax = b$. Đồng thời tìm ma trận nghịch đảo $A^{-1} = C^T / \det A$. Đối với $b = (0, 0, 1)$ này, nghiệm $x$ chính là cột 3 của $A^{-1}$! Những phần phụ đại số nào liên quan đến việc tính cột $x = (x, y, z)$ đó?

| Cột 3 của $A^{-1}$ | $\begin{bmatrix} 2 & 6 & 2 \\ 1 & 4 & 2 \\ 5 & 9 & 0 \end{bmatrix}$ | $\begin{bmatrix} x \\ y \\ z \end{bmatrix}$ | $= \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$ |
|----------------------|---------------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------|

Tìm thể tích của hai hình hộp: các cạnh là *các cột* của $A$ và các cạnh là các hàng của $A^{-1}$.

**Lời giải** Định thức của $B_j$ (với vế phải $b$ đặt vào cột $j$) là

$$
\det B_1 = \begin{vmatrix} \mathbf{0} & 6 & 2 \\ \mathbf{0} & 4 & 2 \\ \mathbf{1} & 9 & 0 \end{vmatrix} \quad \det B_2 = \begin{vmatrix} 2 & \mathbf{0} & 2 \\ 1 & \mathbf{0} & 2 \\ 5 & \mathbf{1} & 0 \end{vmatrix} \quad \det B_3 = \begin{vmatrix} 2 & 6 & \mathbf{0} \\ 1 & 4 & \mathbf{0} \\ 5 & 9 & \mathbf{1} \end{vmatrix}
$$

Đó chính là các phần phụ đại số $C_{31}, C_{32}, C_{33}$ của hàng 3. Tích vô hướng của chúng với hàng 3 là $\det A = 2$:

$$\det A = a_{31}C_{31} + a_{32}C_{32} + a_{33}C_{33} = (5, 9, 0) \cdot (4, -2, 2) = 2.$$

Ba tỷ số $\det B_j / \det A$ cho ba thành phần của $x = (2, -1, 1)$. $x$ này là cột thứ ba của $A^{-1}$ bởi vì $b = (0, 0, 1)$ là cột thứ ba của $I$.

Các phần phụ đại số dọc theo các *hàng* khác của $A$, chia cho $\det A$, cho ta các *cột* khác của $A^{-1}$:

| $A^{-1} = \frac{C^T}{\det A} = \frac{1}{2} \begin{bmatrix} -18 & 18 & 4 \\ 10 & -10 & -2 \\ -11 & 12 & 2 \end{bmatrix}$ | Nhân để kiểm tra | $AA^{-1} = I$ |
|-------------------------------------------------------------------------------------------------------------------------|-------------------|---------------|

Hình hộp từ các cột của $A$ có thể tích = $\det A = 2$. Hình hộp từ các hàng cũng có thể tích bằng 2, vì $|A^T| = |A|$. Hình hộp từ các hàng của $A^{-1}$ có thể tích $1/|A| = 1/2$.

**Bài tập 5.3 (Problem Set 5.3)**

**Các bài tập 1-5 nói về Quy tắc Cramer cho $x = A^{-1}b$.**

**1** Giải các hệ phương trình tuyến tính này bằng Quy tắc Cramer $x_1 = \det B_1 / \det A$:
(a)
$2x_1 + 5x_2 = 1$
$x_1 + 4x_2 = 2$
(b)
$2x_1 + x_2 = 1$
$x_1 + 2x_2 + x_3 = 0$
$x_2 + 2x_3 = 0$.

**2** Sử dụng Quy tắc Cramer để giải tìm $y$ (chỉ mỗi $y$). Gọi định thức $3 \times 3$ là $D$:
(a)
$ax + by = 1$
$cx + dy = 0$
(b)
$ax + by + cz = 1$
$dx + ey + fz = 0$
$gx + hy + iz = 0$.

**3** Quy tắc Cramer thất bại khi $\det A = 0$. Ví dụ (a) không có nghiệm trong khi ví dụ (b) có vô số nghiệm. Các tỷ số $x_1 = \det B_1 / \det A$ trong hai trường hợp này là gì?
(a) $2x_1 + 3x_2 = 1$ và $4x_1 + 6x_2 = 1$ (hai đường thẳng song song)
(b) $2x_1 + 3x_2 = 1$ và $4x_1 + 6x_2 = 2$ (cùng một đường thẳng)

**4** *Chứng minh nhanh quy tắc Cramer.* Định thức là một hàm tuyến tính theo cột 1. Nó bằng không nếu hai cột bằng nhau. Khi $b = Ax = x_1 a_1 + x_2 a_2 + x_3 a_3$ đi vào cột đầu tiên của $A$, định thức của ma trận $B_1$ này là:

$$| b \quad a_2 \quad a_3 | = | x_1 a_1 + x_2 a_2 + x_3 a_3 \quad a_2 \quad a_3 | = | x_1 a_1 \quad a_2 \quad a_3 | = x_1 \det A$$

(a) Công thức nào cho $x_1$ xuất phát từ vế trái = vế phải?
(b) Những bước nào dẫn đến phương trình ở giữa?

**5** Nếu vế phải $b$ là cột đầu tiên của $A$, giải hệ $3 \times 3$ $Ax = b$. Bằng cách nào mỗi định thức trong Quy tắc Cramer dẫn đến nghiệm $x$ này?

**Các bài tập 6–15 nói về $A^{-1} = C^T / \det A$. Hãy nhớ chuyển vị $C$.**

**6** Tìm $A^{-1}$ từ công thức phần phụ đại số $C^T / \det A$. Sử dụng tính đối xứng trong phần (b).

$$(a) \quad A = \begin{bmatrix} 1 & 2 & 0 \\ 0 & 3 & 0 \\ 0 & 7 & 1 \end{bmatrix} \quad (b) \quad A = \begin{bmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{bmatrix}.$$

**7** Nếu tất cả các phần phụ đại số đều bằng không, làm sao bạn biết $A$ không có nghịch đảo? Nếu không có phần phụ đại số nào bằng không, liệu $A$ có chắc chắn khả nghịch không?

**8** Tìm các phần phụ đại số của $A$ và nhân $AC^T$ để tìm $\det A$:

$$A = \begin{bmatrix} 1 & 1 & 4 \\ 1 & 2 & 2 \\ 1 & 2 & 5 \end{bmatrix} \quad \text{và} \quad C = \begin{bmatrix} 6 & -3 & 0 \\ \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot \end{bmatrix} \quad \text{và} \quad AC^T = \underline{\hspace{2cm}}.$$

Nếu bạn đổi số 4 đó thành 100, tại sao $\det A$ không thay đổi?

**9** Giả sử $\det A = 1$ và bạn biết tất cả các phần phụ đại số trong $C$. Làm sao bạn có thể tìm được $A$?

**10** Từ công thức $AC^T = (\det A)I$, chứng minh rằng $\det C = (\det A)^{n-1}$.

**11** Nếu mọi phần tử của $A$ đều là số nguyên, và $\det A = 1$ hoặc $-1$, chứng minh rằng mọi phần tử của $A^{-1}$ đều là số nguyên. Cho một ví dụ $2 \times 2$ không có phần tử không.

**12** Nếu mọi phần tử của $A$ và $A^{-1}$ đều là số nguyên, chứng minh rằng $\det A = 1$ hoặc $-1$. Gợi ý: $\det A$ nhân $\det A^{-1}$ là gì?

**13** Hoàn thành việc tính toán $A^{-1}$ bằng các phần phụ đại số đã bắt đầu ở Ví dụ 5.

**14** $L$ là ma trận tam giác dưới và $S$ là ma trận đối xứng. Giả sử chúng khả nghịch:

$$\text{Để nghịch đảo} \quad L = \begin{bmatrix} a & 0 & 0 \\ b & c & 0 \\ d & e & f \end{bmatrix} \quad \text{và ma trận đối xứng} \quad S = \begin{bmatrix} a & b & d \\ b & c & e \\ d & e & f \end{bmatrix}.$$

(a) Ba phần phụ đại số nào của $L$ bằng không? Khi đó $L^{-1}$ cũng là ma trận tam giác dưới.
(b) Ba cặp phần phụ đại số nào của $S$ bằng nhau? Khi đó $S^{-1}$ cũng là ma trận đối xứng.
(c) Ma trận phần phụ đại số $C$ của một ma trận trực giao $Q$ sẽ là \_\_\_\_\_. Tại sao?

**15** Đối với $n = 5$ ma trận $C$ chứa \_\_\_\_\_ phần phụ đại số. Mỗi phần phụ đại số $4 \times 4$ chứa \_\_\_\_\_ số hạng và mỗi số hạng cần \_\_\_\_\_ phép nhân. So sánh với $5^3 = 125$ phép toán cho thuật toán Gauss-Jordan tính $A^{-1}$ ở Phần 2.4.

**Các bài tập 16–26 nói về diện tích và thể tích bằng định thức.**

**16** (a) Tìm diện tích của hình bình hành có các cạnh $v = (3, 2)$ và $w = (1, 4)$.
(b) Tìm diện tích của tam giác có các cạnh $v$, $w$, và $v + w$. Hãy vẽ nó.
(c) Tìm diện tích của tam giác có các cạnh $v$, $w$, và $w - v$. Hãy vẽ nó.

**17** Một hình hộp có các cạnh từ $(0, 0, 0)$ đến $(3, 1, 1)$ và $(1, 3, 1)$ và $(1, 1, 3)$. Tìm thể tích của nó. Cũng tìm diện tích của mỗi mặt hình bình hành bằng cách sử dụng $\|u \times v\|$.

**18** (a) Các đỉnh của một tam giác là $(2, 1)$ và $(3, 4)$ và $(0, 5)$. Diện tích là bao nhiêu?
(b) Thêm một đỉnh tại $(-1, 0)$ để tạo thành một miền nghiêng (bốn cạnh). Tìm diện tích.

**19** Hình bình hành có các cạnh $(2, 1)$ và $(2, 3)$ có cùng diện tích với hình bình hành có các cạnh $(2, 2)$ và $(1, 3)$. Tìm các diện tích đó từ các định thức $2 \times 2$ và giải thích tại sao chúng phải bằng nhau. (Tôi không thể thấy lý do qua hình vẽ. Hãy viết thư cho tôi nếu bạn thấy.)

**20** Ma trận Hadamard $H$ có các hàng trực giao. Hình hộp là một siêu khối lập phương (hypercube)!

$$\text{Giá trị của } |H| = \begin{vmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & -1 & -1 \\ 1 & -1 & -1 & 1 \\ 1 & -1 & 1 & -1 \end{vmatrix} = \text{thể tích của một siêu khối lập phương trong } \mathbb{R}^4 \text{ là bao nhiêu?}$$

**21** Nếu các cột của một ma trận $4 \times 4$ có độ dài $L_1, L_2, L_3, L_4$, giá trị lớn nhất có thể của định thức (dựa trên thể tích) là bao nhiêu? Nếu tất cả các phần tử của ma trận là 1 hoặc $-1$, độ dài của chúng và định thức lớn nhất là bao nhiêu?

**22** Biểu diễn bằng một hình vẽ cách một hình chữ nhật có diện tích $x_1y_2$ trừ đi một hình chữ nhật có diện tích $x_2y_1$ tạo ra cùng một diện tích với hình bình hành của chúng ta.

**23** Khi các vectơ cạnh $a, b, c$ vuông góc với nhau, thể tích của hình hộp là $\|a\|$ nhân $\|b\|$ nhân $\|c\|$. Ma trận $A^T A$ là \_\_\_\_\_. Tìm $\det A^T A$ và $\det A$.

**24** Hình hộp với các cạnh $i$ và $j$ và $w = 2i + 3j + 4k$ có chiều cao \_\_\_\_\_. Thể tích là bao nhiêu? Ma trận có định thức này là gì? $i \times j$ là gì và tích vô hướng của nó với $w$ là bao nhiêu?

**25** Một hình lập phương $n$ chiều có bao nhiêu đỉnh? Bao nhiêu cạnh? Bao nhiêu mặt $(n - 1)$ chiều? Hình lập phương trong $\mathbb{R}^n$ có các cạnh là các hàng của $2I$ có thể tích \_\_\_\_\_. Một máy tính siêu khối lập phương có các bộ xử lý song song ở các đỉnh với các kết nối dọc theo các cạnh.

**26** Tam giác với các đỉnh $(0, 0), (1, 0), (0, 1)$ có diện tích $\frac{1}{2}$. Hình chóp trong $\mathbb{R}^3$ với bốn đỉnh $(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)$ có thể tích \_\_\_\_\_. Thể tích của một hình chóp trong $\mathbb{R}^4$ với năm đỉnh tại $(0, 0, 0, 0)$ và các hàng của $I$ là bao nhiêu?

**Các bài tập 27–30 nói về các diện tích $dA$ và thể tích $dV$ trong giải tích.**

**27** Tọa độ cực thỏa mãn $x = r \cos \theta$ và $y = r \sin \theta$. Diện tích trong tọa độ cực là $J dr d\theta$:

$$J = \begin{vmatrix} \partial x / \partial r & \partial x / \partial \theta \\ \partial y / \partial r & \partial y / \partial \theta \end{vmatrix} = \begin{vmatrix} \cos \theta & -r \sin \theta \\ \sin \theta & r \cos \theta \end{vmatrix}.$$

**28** Tọa độ cầu $\rho, \phi, \theta$ thỏa mãn $x = \rho \sin \phi \cos \theta$ và $y = \rho \sin \phi \sin \theta$ và $z = \rho \cos \phi$. Tìm ma trận $3 \times 3$ các đạo hàm riêng: $\partial x / \partial \rho, \partial x / \partial \phi, \partial x / \partial \theta$ ở hàng 1. Đơn giản hóa định thức của nó thành $J = \rho^2 \sin \phi$. Khi đó $dV$ trong tọa độ cầu là $\rho^2 \sin \phi d\rho d\phi d\theta$, thể tích của một "hộp tọa độ" vô cùng nhỏ.

**29** Ma trận kết nối $r, \theta$ với $x, y$ nằm trong Bài tập 27. Khả nghịch ma trận $2 \times 2$ đó:

$$J^{-1} = \begin{vmatrix} \partial r / \partial x & \partial r / \partial y \\ \partial \theta / \partial x & \partial \theta / \partial y \end{vmatrix} = \begin{vmatrix} \cos \theta & ? \\ ? & ? \end{vmatrix} = ?$$

Thật đáng ngạc nhiên khi $\partial r / \partial x = \partial x / \partial r$ (trong cuốn *Calculus*, Gilbert Strang, tr. 501). Nhân các ma trận $J$ và $J^{-1}$ cho ta quy tắc dây chuyền $\frac{\partial x}{\partial x} = \frac{\partial x}{\partial r} \frac{\partial r}{\partial x} + \frac{\partial x}{\partial \theta} \frac{\partial \theta}{\partial x} = 1$.

**30** Tam giác với các đỉnh $(0, 0)$, $(6, 0)$, và $(1, 4)$ có diện tích \_\_\_\_\_. Khi bạn quay nó một góc $\theta = 60^\circ$ diện tích là \_\_\_\_\_. Định thức của ma trận quay là

$$J = \begin{vmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{vmatrix} = \begin{vmatrix} \frac{1}{2} & ? \\ ? & ? \end{vmatrix} = ?$$

**Các bài tập 31–38 nói về tích hỗn tạp $(u \times v) \cdot w$ trong không gian ba chiều.**

**31** Một hình hộp có diện tích đáy $\|u \times v\|$. Chiều cao vuông góc của nó là $\|w\| \cos \theta$. Diện tích đáy nhân chiều cao = thể tích = $\|u \times v\| \|w\| \cos \theta$ cũng chính là $(u \times v) \cdot w$. Tính diện tích đáy, chiều cao, và thể tích cho $u = (2, 4, 0)$, $v = (-1, 3, 0)$, $w = (1, 2, 2)$.

**32** Thể tích của cùng một hình hộp đó được cho một cách trực tiếp hơn bởi một định thức $3 \times 3$. Hãy tính định thức đó.

**33** Khai triển định thức $3 \times 3$ trong phương trình (13) theo các phần phụ đại số của hàng $u_1, u_2, u_3$ của nó. Sự khai triển này là tích vô hướng của $u$ với vectơ \_\_\_\_\_.

**34** Tích hỗn tạp nào trong số $(u \times w) \cdot v$ và $(w \times u) \cdot v$ và $(v \times w) \cdot u$ bằng với $(u \times v) \cdot w$? Những thứ tự nào của các hàng $u, v, w$ cho ra định thức đúng?

**35** Cho $P = (1, 0, -1)$ và $Q = (1, 1, 1)$ và $R = (2, 2, 1)$. Chọn $S$ sao cho $PQRS$ là một hình bình hành và tính diện tích của nó. Chọn $T, U, V$ sao cho $OPQRSTUV$ là một hình hộp nghiêng và tính thể tích của nó.

**36** Giả sử $(x, y, z)$ và $(1, 1, 0)$ và $(1, 2, 1)$ nằm trên một mặt phẳng đi qua gốc tọa độ. Định thức nào bằng không? Điều này mang lại phương trình nào cho mặt phẳng?

**37** Giả sử $(x, y, z)$ là một tổ hợp tuyến tính của $(2, 3, 1)$ và $(1, 2, 3)$. Định thức nào bằng không? Điều này mang lại phương trình nào cho mặt phẳng của tất cả các tổ hợp?

**38** (a) Giải thích từ khái niệm thể tích tại sao $\det 2A = 2^n \det A$ cho các ma trận $n \times n$.
(b) Với ma trận kích thước bao nhiêu thì phát biểu sai $\det A + \det A = \det(A + A)$ trở thành đúng?

### **Bài tập thử thách (Challenge Problems)**

**39** Nếu bạn biết tất cả 16 phần phụ đại số của một ma trận khả nghịch $4 \times 4$ $A$, làm sao bạn tìm được $A$?

**40** Giả sử $A$ là ma trận $5 \times 5$. Các phần tử của nó ở hàng 1 nhân với các định thức (phần phụ đại số) ở các hàng 2-5 để cho ra định thức. Bạn có thể đoán một "công thức Jacobi" cho $\det A$ sử dụng các định thức $2 \times 2$ từ các hàng 1-2 *nhân với* các định thức $3 \times 3$ từ các hàng 3-5 không? Hãy kiểm tra công thức của bạn trên ma trận ba đường chéo $-1, 2, -1$ có định thức = 6.

**41** Ma trận $2 \times 2$ $AB = (2 \times 3)(3 \times 2)$ có một "công thức Cauchy-Binet" cho $\det AB$: $\det AB =$ tổng của (định thức $2 \times 2$ trong $A$) $\times$ (định thức $2 \times 2$ trong $B$).
(a) Đoán xem nên sử dụng những định thức $2 \times 2$ nào từ $A$ và $B$.
(b) Kiểm tra công thức của bạn khi các hàng của $A$ là $1, 2, 3$ và $1, 4, 7$ với $B = A^T$.

**42** Công thức lớn có $n!$ số hạng. Nhưng nếu một phần tử của $A$ bằng không, $(n - 1)!$ số hạng sẽ biến mất. Nếu $A$ chỉ có *ba đường chéo*, còn lại bao nhiêu số hạng? Đối với $n = 1, 2, 3, 4$ định thức ba đường chéo có $1, 2, 3, 5$ số hạng. Đó là các số Fibonacci ở Phần 6.2! Chứng minh tại sao một định thức ba đường chéo $5 \times 5$ có $5 + 3 = 8$ số hạng khác không (lại là Fibonacci). Sử dụng các phần phụ đại số của $a_{11}$ và $a_{12}$.

