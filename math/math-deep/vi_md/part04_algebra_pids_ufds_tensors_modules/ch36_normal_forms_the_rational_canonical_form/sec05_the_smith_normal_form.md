# Dạng chuẩn tắc Smith (Smith normal form)


<!-- PAGE 1338 -->
Theo cơ sở (basis) $(x_{1}, x_{2}, x_{3})$, ánh xạ f(x, $y, z) = (x + y + z, y + z, z)$ có Jordan
$$block matrix representation \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix} since$$
$$f(x_{1}) = f(1, 0, 0) = (1, 0, 0) = x_{1}$$
$$f(x_{2}) = f(1, 1, 0) = (2, 1, 0) = x_{1} + x_{2}$$
$$f(x_{3}) = f(1, 0, 1) = (2, 1, 1) = x_{2} + x_{3}.$$
Combining Định lý 36.15 và Mệnh đề 36.16, ta thu được mạnh phiên bản của Dạng Jordan (Jordan form).

> **Định lý 36.17.** (Dạng chính tắc Jordan (Jordan canonical form)) Cho $E$ là hữu hạn chiều vectơ $K$ không gian. Các tính chất sau đây là tương đương:
$(1)$ các trị riêng (eigenvalues) của $f$ tất cả thuộc đến $K$.
$(2)$ Có một cơ sở (basis) của $E$ trong mà ma trận của $f$ là trên (hoặc thấp hơn) tam giác.
$(3)$ Ở đó tồn tại cơ sở (basis) của $E$ trong mà ma trận $A$ của $f$ là Jordan ma trận. Hơn nữa, số của Các khối Jordan $J_{r}(\lambda$) xuất hiện trong $A$, cho cố định $r$ và $\lambda$, là một cách duy nhất được xác định bởi $f$.

*Chứng minh.* implication $(1) =\Rightarrow (3)$ suy ra từ Định lý 36.15 và Mệnh đề 36.16. implications $(3) =\Rightarrow (2)$ và $(2) =\Rightarrow (1)$ là tầm thường. Compared đến Định lý 31.17, mới ingredient là tính duy nhất assertion trong $(3)$, mà là không do đó dễ để chứng minh. Nhận thấy rằng đa thức tối tiểu (minimal polynomial) của $f$ là least chung/phổ biến bội của các đa thức $(X$ - $\lambda )^{r}$ liên kết với Các khối Jordan $J_{r}(\lambda$) xuất hiện trong $A$, và đa thức đặc trưng (characteristic polynomial) của $A$ là tích của các đa thức này. Ta bây giờ trả về đến bài toán của việc tính toán effectively sự đồng dạng các bất biến của ma trận $M$. Theo Mệnh đề 36.11, điều này là tương đương đến việc tính toán các nhân tử bất biến (invariant factors) của $XI$ - $M$. Trong nguyên lý, điều này có thể được được thực hiện bằng cách sử dụng Mệnh đề 35.35. quy trình đến thực hiện điều này effectively cho vành $A =$ K[X] là đến chuyển đổi $XI$ - $M$ đến của nó Dạng chuẩn tắc Smith (Smith normal form). Điều này sẽ cũng cho dạng chính tắc hữu tỷ (rational canonical form) cho $M$.

## 36.5 Dạng chuẩn tắc Smith (Smith normal form)

Dạng chuẩn tắc Smith (Smith normal form) là đặc biệt trường hợp của Mệnh đề 35.35 ứng dụng đến PID K[X] ở đâu $K$ là trường, nhưng nó cũng nói rằng rằng các ma trận $P$ và $Q$ là các tích của sơ cấp các ma trận. Hóa ra là như vậy kết quả nghiệm đúng với mọi Euclidean vành, và chứng minh là basically cùng.

<!-- PAGE 1339 -->
Nhắc lại từ Định nghĩa 30.10 rằng Euclidean vành là miền nguyên (integral domain) $A$ sao cho tồn tại một hàm $\sigma$: $A \to \mathbb{N}$ với sau đây tính chất: Với mọi, $b \in A$ với $b \neq  0$, có một số $q, r \in A$ sao cho
$$a = bq + rand\sigma (r) < \sigma (b).$$
Lưu ý rằng cặp $(q, r)$ là không nhất thiết duy nhất. Ta tạo sử dụng của sơ cấp hàng và cột các phép toán P(i, $k), E_{i,j;\beta}$, và $E_{i,\lambda}$ được mô tả trong Chương $8$, ở đâu ta đòi hỏi vô hướng (scalar) $\lambda$ được sử dụng trong $E_{i,\lambda}$ là unit.

> **Định lý 36.18.** Nếu $M$ là một ma trận cỡ $m \times  n$ trên Euclidean vành $A$, thì ở đó tồn tại một số khả nghịch $n \times  n$ ma trận $P$ và một số khả nghịch $m \times  m$ ma trận $Q$, ở đâu $P$ và $Q$ là các tích của sơ cấp các ma trận, và một ma trận cỡ $m \times  n$ $D$ của tạo thành
$$D = \begin{pmatrix} \alpha_{1} & 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & \alpha_{2} & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ \cdots \\ 0 & 0 & \cdots & \alpha_{r} & 0 & \cdots & 0 \\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ \cdots \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$$
$$\cdots \cdots$$
Với một số khác không $\alpha_{i}  \in A$, sao cho
$(1) \alpha_{1}$ | $\alpha_{2}$ | $\cdots$ | $\alpha_{r}$, và
$(2) M = QDP^{-1}$.

*Chứng minh.* Ta suy ra Jacobson’s chứng minh $[101]$ (Chương $3$, Định lý 3.8). Ta tiến hành bằng quy nạp theo $m + n$. Nếu $m = n = 1$, cho $P = (1)$ và $Q = (1)$. Cho quy nạp bước, nếu $M = 0$, cho $P = I_{n}$ và $Q = I_{m}$. Nếu M̸ $= 0$, stategy là để áp dụng dãy của sơ cấp các phép biến đổi rằng các chuyển đổi $M$ đến ma trận của tạo thành
$$M'  = \begin{pmatrix} \alpha_{1} & 0 & \cdots & 0 \\ 0 \\ \vdots & Y \\ 0 \end{pmatrix}$$
Ở đâu $Y$ là $(m$ - $1) \times  (n$ - 1)-ma trận sao cho $\alpha_{1}$ chia hết mọi phần tử (entry) trong $Y$. Thì, ta tiến hành bằng quy nạp theo $Y$. để tìm M', ta perform sau đây các bước. Bước $1$. Chọn một số khác không phần tử (entry) $a_{ij}$ trong $M$ sao cho $\sigma (a_{ij})$ là tối tiểu. Thì hoán vị cột $j$ và cột $1$, và hoán vị hàng $i$ và hàng $1$, đến bring điều này phần tử (entry) trong position $(1, 1)$. Ta ký hiệu điều này mới ma trận một lần nữa bởi $M$.

<!-- PAGE 1340 -->
Bước 2a. Nếu $m = 1$ đi đến Bước 2b. Nếu $m > 1$, thì có hai các khả năng:
$(i) M$ là của tạo thành
$$\begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ 0 & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ 0 & a_{m2} & \cdots & a_{mn} \end{pmatrix} .$$
Nếu $n = 1$, dừng; khác đi đến Bước 2b.
(ii) Tồn tại một khác không phần tử (entry) $a_{i1} (i > 1)$ ở dưới $a_{11}$ trong cột thứ nhất.
() Nếu tồn tại một phần tử (entry) $a_{k1}$ trong cột thứ nhất sao cho $a_{11}$ thực hiện không chia $a_{k1}$, thì chọn như vậy phần tử (entry) (nói, với nhỏ nhất chỉ số $i$ sao cho $\sigma (a_{i1})$ là tối tiểu), và chia $a_{k1}$ bởi $a_{11}$; nghĩa là, tìm $b_{k}$ và $b_{k1}$ sao cho
$$a_{k1} = a_{11}b_{k} + b_{k1},with\sigma (b_{k1}) < \sigma (a_{11}).$$
Trừ $b_{k}$ lần hàng $1$ từ hàng $k$ và hoán vị hàng $k$ và hàng $1$, để thu được ma trận của tạo thành
$$M = \begin{pmatrix} b_{k1} & b_{k2} & \cdots & b_{kn} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix} .$$
Đi quay lại đến Bước 2a.
$(b)$ Nếu $a_{11}$ chia hết mọi (khác không) phần tử (entry) $a_{i1}$ cho $i \ge 2$, nói $a_{i1} = a_{11}b_{i}$, thì trừ $b_{i}$ lần hàng $1$ từ hàng $i$ cho $i = 2, \dots  , m$; đi đến Bước 2b. Nhận thấy rằng bất cứ khi nào ta trả về đến bắt đầu của Bước 2a, ta có $\sigma (b_{k1}) < \sigma (a_{11})$. Vì vậy, sau hữu hạn số của các bước, ta phải exit Bước 2a với ma trận trong mà tất cả các phần tử (entries) trong cột $1$ nhưng thứ nhất là không và đi đến Bước 2b. Bước 2b. bước này là đạt tới chỉ nếu $n > 1$ và nếu chỉ khác không phần tử (entry) trong cột thứ nhất là $a_{11}$.
() Nếu $M$ là của tạo thành
$$\begin{pmatrix} a_{11} & 0 & \cdots & 0 \\ 0 & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ 0 & a_{m2} & \cdots & a_{mn} \end{pmatrix}$$
Và $m = 1$ dừng; khác đi đến Bước $3$.

<!-- PAGE 1341 -->
$(b)$ Nếu tồn tại một phần tử (entry) $a_{1k}$ trong hàng thứ nhất sao cho $a_{11}$ thực hiện không chia $a_{1k}$, thì chọn như vậy phần tử (entry) (nói, với nhỏ nhất chỉ số $j$ sao cho $\sigma (a_{1j})$ là tối tiểu), và chia $a_{1k}$ bởi $a_{11}$; nghĩa là, tìm $b_{k}$ và $b_{1k}$ sao cho
$$a_{1k} = a_{11}b_{k} + b_{1k},with\sigma (b_{1k}) < \sigma (a_{11}).$$
Trừ $b_{k}$ lần cột $1$ từ cột $k$ và hoán vị cột $k$ và cột $1$, để thu được ma trận của tạo thành
$$M = \begin{pmatrix} b_{1k} & a_{k2} & \cdots & a_{kn} \\ b_{2k} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ b_{mk} & a_{m2} & \cdots & a_{mn} \end{pmatrix} .$$
Đi quay lại đến Bước 2b.
$(c)$ Nếu $a_{11}$ chia hết mọi (khác không) phần tử (entry) $a_{1j}$ cho $j \ge 2$, nói $a_{1j} = a_{11}b_{j}$, thì trừ $b_{j}$ lần cột $1$ từ cột $j$ cho $j = 2, \dots  , n$; đi đến Bước $3$. Như trong Bước 2a, bất cứ khi nào ta trả về đến bắt đầu của Bước 2b, ta có $\sigma (b_{1k}) < \sigma (a_{11})$. Vì vậy, sau hữu hạn số của các bước, ta phải exit Bước 2b với ma trận trong mà tất cả các phần tử (entries) trong hàng $1$ nhưng thứ nhất là không. Bước $3$. bước này là đạt tới chỉ nếu chỉ khác không phần tử (entry) trong hàng thứ nhất là $a_{11}$.
$(i)$ Nếu
$$M = \begin{pmatrix} a_{11} & 0 & \cdots & 0 \\ 0 \\ \vdots & Y \\ 0 \end{pmatrix}$$
Đi đến Bước $4$.
(ii) Nếu Bước 2b ruined cột $1$ mà bây giờ chứa một số khác không phần tử (entry) ở dưới $a_{11}$, đi quay lại đến Bước 2a. Ta perform dãy của thay phiên các bước giữa Bước 2a và Bước 2b. Bởi vì $\sigma$ -giá trị của $(1$, 1)-phần tử (entry) chặt giảm bất cứ khi nào ta reenter Bước 2a và Bước 2b, như vậy dãy phải terminate với ma trận của tạo thành
$$M = \begin{pmatrix} a_{11} & 0 & \cdots & 0 \\ 0 \\ \vdots & Y \\ 0 \end{pmatrix}$$
Bước $4$. Nếu $a_{11}$ chia hết tất cả các phần tử (entries) trong $Y$, dừng.

<!-- PAGE 1342 -->
Ngược lại, tồn tại một cột, nói $j$, sao cho $a_{11}$ thực hiện không chia một số phần tử (entry) $a_{ij}$, do đó cộng cột thứ $j$ đến cột thứ nhất. Điều này cho ta ma trận của tạo thành
$$M = \begin{pmatrix} a_{11} & 0 & \cdots & 0 \\ b_{2j} \\ \vdots & Y \\ b_{mj} \end{pmatrix}$$
Ở đâu phần tử thứ $i$ trong cột $1$ là khác không, do đó đi quay lại đến Bước 2a, Một lần nữa, vì $\sigma$ -giá trị của $(1$, 1)-phần tử (entry) chặt giảm bất cứ khi nào ta reenter Bước 2a và Bước 2b, như vậy dãy phải terminate với ma trận của tạo thành
$$M'  = \begin{pmatrix} \alpha_{1} & 0 & \cdots & 0 \\ 0 \\ \vdots & Y \\ 0 \end{pmatrix}$$
Ở đâu $\alpha_{1}$ chia hết mọi phần tử (entry) trong $Y$. Thì, ta áp dụng giả thiết quy nạp (induction hypothesis) đến $Y$. Nếu PID $A$ là đa thức vành K[X] ở đâu $K$ là trường, $\alpha_{i}$ là khác không các đa thức, do đó ta có thể áp dụng hàng các phép toán đến chuẩn hóa của chúng dẫn đầu các hệ số là $1$. Ta thu được kết quả sau định lý.

> **Định lý 36.19.** (Dạng chuẩn tắc Smith (Smith normal form)) Nếu $M$ là một ma trận cỡ $m \times  n$ trên đa thức vành K[X], ở đâu $K$ là trường, thì ở đó tồn tại một số khả nghịch $n\times n$ ma trận $P$ và một số khả nghịch $m \times  m$ ma trận $Q$, ở đâu $P$ và $Q$ là các tích của sơ cấp các ma trận với các phần tử (entries) trong K[X], và một ma trận cỡ $m \times  n$ $D$ của tạo thành
$$D = \begin{pmatrix} q_{1} & 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & q_{2} & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ \cdots \\ 0 & 0 & \cdots & q_{r} & 0 & \cdots & 0 \\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ \cdots \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$$
$$\cdots \cdots$$
Với một số khác không chuẩn hóa (monic) các đa thức $q_{i} \in$ k[X], sao cho
$(1) q_{1}$ | $q_{2}$ | $\cdots$ | $q_{r}$, và
$(2) M = QDP^{-1}$.

<!-- PAGE 1343 -->
Đặc biệt, nếu ta áp dụng Định lý 36.19 đến ma trận $M$ của tạo thành $M = XI -A$, ở đâu $A$ là ma trận vuông (square matrix), thì det(XI $-A) = \chi_{A} (X)$ là không bao giờ không, và vì $XI -A = QDP^{-1}$ với $P, Q$ khả nghịch, tất cả các phần tử (entries) trong $D$ phải là khác không và ta thu được kết quả sau kết quả chỉ ra rằng sự đồng dạng các bất biến của $A$ có thể được được tính bằng cách sử dụng sơ cấp các phép toán.

> **Định lý 36.20.** Nếu $A$ là một ma trận cỡ $n \times  n$ trên trường $K$, thì ở đó tồn tại một số khả nghịch $n \times  n$ các ma trận $P$ và $Q$, ở đâu $P$ và $Q$ là các tích của sơ cấp các ma trận với các phần tử (entries) trong K[X], và một ma trận cỡ $n \times  n$ $D$ của tạo thành
$$D = \begin{pmatrix} 1 & \cdots & 0 & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \vdots & \vdots \\ 0 & \cdots & 1 & 0 & 0 & \cdots & 0 \\ 0 & \cdots & 0 & q_{1} & 0 & \cdots & 0 \\ 0 & \cdots & 0 & 0 & q_{2} & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & 0 & q_{m} \end{pmatrix}$$
$$\cdots \cdots$$
Với một số khác không chuẩn hóa (monic) các đa thức $q_{i} \in$ k[X] của bậc $\ge 1$, sao cho
$(1) q_{1}$ | $q_{2}$ | $\cdots$ | $q_{m}$,
$(2) q_{1}, \dots  q_{m}$ là sự đồng dạng các bất biến của $A$, và
$(3) XI$ - $A = QDP^{-1}$. ma trận $D$ trong Định lý 36.20 là thường được gọi là Dạng chuẩn tắc Smith (Smith normal form) của $A$, chẵn/ngay cả dù điều này là confusing thuật ngữ vì $D$ là một cách thực Dạng chuẩn tắc Smith (Smith normal form) của $XI$ - $A$. Của course, ta biết từ trước đó hoạt động/công trình rằng trong Định lý 36.19, $\alpha_{1} , \dots  , \alpha_{r}$ là duy nhất, và rằng trong Định lý 36.20, $q_{1}, \dots  , q_{m}$ là duy nhất. Điều này có thể cũng được chứng minh bằng cách sử dụng một số đơn giản các tính chất của các định thức con (minor), nhưng ta để lại nó như một bài tập (cho help, nhìn tại Jacobson $[101]$, Chương $3$, Định lý 3.9). dạng chính tắc hữu tỷ (rational canonical form) của $A$ có thể cũng là thu được từ $Q^{-1}$ và $D$, nhưng thứ nhất, cho chúng ta xét tổng quát hóa của Định lý 36.19 đến PID’s rằng là không nhất thiết Euclidean các vành. Ta cần để tìm “chuẩn (norm)” rằng assigns tự nhiên số $\sigma$ () đến bất kỳ khác không phần tử của PID $A$, trong như vậy cách rằng $\sigma$ () giảm bất cứ khi nào ta trả về đến Bước 2a và Bước 2b. Vì PID là UFD, ta sử dụng số
$$\sigma (a) = k_{1} + \cdots  + k_{r}$$
Của nguyên tố các nhân tử trong nhân tử hóa của nonunit phần tử
$$a = up_{1}^{k1} \cdots  p_{r}^{kr} ,$$

<!-- PAGE 1344 -->
Và ta tập hợp
$$\sigma (u) = 0$$
Nếu $u$ là unit. Ta có thể’t chia anymore, nhưng ta có thể tìm ước chung lớn nhất (gcd)’s và sử dụng Bezout đến mimic phép chia. then chốt ingredient là điều này: với mọi hai khác không các phần tử, $b \in A$, nếu thực hiện không chia $b$ thì cho $d \neq  0$ là ước chung lớn nhất (gcd) của và $b$. Bởi Bezout, ở đó tồn tại $x, y \in A$ sao cho
$$ax + by = d.$$
Ta có thể cũng viết $a =$ td và $b =$ -sd, với một số $s, t \in A$, sao cho tdx - sdy $= d$, mà suy ra rằng
$$tx -sy = 1,$$
Vì $A$ là miền nguyên (integral domain). Nhận thấy rằng
$$\begin{pmatrix} t & -s \\ -y & x \end{pmatrix} \begin{pmatrix} x & s \\ y & t \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} ,$$
Mà chỉ ra rằng cả hai các ma trận trên trái của phương trình là khả nghịch, và do đó là chuyển vị (transpose) của thứ hai một,
$$\begin{pmatrix} x & y \\ s & t \end{pmatrix}$$
(chúng tất cả có định thức (determinant) $1)$. Ta cũng có
$$as + bt = tds -sdt = 0,$$
Do đó
$$\begin{pmatrix} x & y \\ s & t \end{pmatrix} \begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} d \\ 0 \end{pmatrix}$$
Và
$$\begin{pmatrix} a & b \end{pmatrix} \begin{pmatrix} x & s \\ y & t \end{pmatrix} = \begin{pmatrix} d & 0 \end{pmatrix} .$$
Bởi vì thực hiện không chia $b$, của chúng ước chung lớn nhất (gcd) $d$ có chặt fewer nguyên tố các nhân tử hơn, do đó
$$\sigma (d) < \sigma (a).$$
Bằng cách sử dụng các ma trận của tạo thành
$$\begin{pmatrix} x & y & 0 & 0 & \cdots & 0 \\ s & t & 0 & 0 & \cdots & 0 \\ 0 & 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 & \cdots & 1 \end{pmatrix}$$
Với xt - ys $= 1$, ta có thể sửa đổi Các bước 2a và Bước 2b để thu được sau đây định lý.

<!-- PAGE 1345 -->

> **Định lý 36.21.** Nếu $M$ là một ma trận cỡ $m \times  n$ trên PID $A$, thì ở đó tồn tại một số khả nghịch $n \times  n$ ma trận $P$ và một số khả nghịch $m \times  m$ ma trận $Q$, ở đâu $P$ và $Q$ là các tích của sơ cấp các ma trận và các ma trận của tạo thành
$$\begin{pmatrix} x & y & 0 & 0 & \cdots & 0 \\ s & t & 0 & 0 & \cdots & 0 \\ 0 & 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 & \cdots & 1 \end{pmatrix}$$
Với xt - ys $= 1$, và một ma trận cỡ $m \times  n$ $D$ của tạo thành
$$D = \begin{pmatrix} \alpha_{1} & 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & \alpha_{2} & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ \cdots \\ 0 & 0 & \cdots & \alpha_{r} & 0 & \cdots & 0 \\ 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ \cdots \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$$
$$\cdots \cdots$$
Với một số khác không $\alpha_{i}  \in A$, sao cho
$(1) \alpha_{1}$ | $\alpha_{2}$ | $\cdots$ | $\alpha_{r}$, và
$(2) M = QDP^{-1}$. Chứng minh phác thảo. Trong Bước 2a, nếu $a_{11}$ thực hiện không chia $a_{k1}$, thì thứ nhất hoán vị hàng $2$ và hàng $k$ (nếu $k \neq  2)$. Thì, nếu ta viết $a = a_{11}$ và $b = a_{k1}$, nếu $d$ là ước chung lớn nhất (gcd) của và $b$ và nếu $x, y, s, t$ được xác định như được giải thích ở trên, nhân trên trái bởi ma trận
$$\begin{pmatrix} x & y & 0 & 0 & \cdots & 0 \\ s & t & 0 & 0 & \cdots & 0 \\ 0 & 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 & \cdots & 1 \end{pmatrix}$$
Để thu được ma trận của tạo thành
$$\begin{pmatrix} d & a_{12} & \cdots & a_{1n} \\ 0 & a_{22} & \cdots & a_{2n} \\ a_{31} & a_{32} & \cdots & a_{3n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{pmatrix}$$

<!-- PAGE 1346 -->
Với $\sigma (d) < \sigma (a_{11})$. Thì, đi quay lại đến Bước 2a. Trong Bước 2b, nếu $a_{11}$ thực hiện không chia $a_{1k}$, thì thứ nhất hoán vị cột $2$ và cột $k$ (nếu $k \neq  2)$. Thì, nếu ta viết $a = a_{11}$ và $b = a_{1k}$, nếu $d$ là ước chung lớn nhất (gcd) của và $b$ và nếu $x, y, s, t$ được xác định như được giải thích ở trên, nhân trên phải bởi ma trận
$$\begin{pmatrix} x & s & 0 & 0 & \cdots & 0 \\ y & t & 0 & 0 & \cdots & 0 \\ 0 & 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 & \cdots & 1 \end{pmatrix}$$
Để thu được ma trận của tạo thành
$$\begin{pmatrix} d & 0 & a_{13} & \cdots & a_{1n} \\ a_{21} & a_{22} & a_{23} & \cdots & a_{2n} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & a_{m3} & \dots & a_{mn} \end{pmatrix}$$
Với $\sigma (d) < \sigma (a_{11})$. Thì, đi quay lại đến Bước 2b. khác các bước vẫn là cùng. Bất cứ khi nào ta trả về đến Bước 2a hoặc Bước 2b, $\sigma$ -giá trị của $(1$, 1)-phần tử (entry) chặt giảm, do đó toàn bộ quy trình kết thúc. Ta kết luận điều này mục bởi giải thích cách mà dạng chính tắc hữu tỷ (rational canonical form) của ma trận $A$ có thể được thu được từ chính tắc tạo thành $QDP^{-1}$ của $XI$ - $A$. Cho $f$: $E \to E$ là ánh xạ tuyến tính (linear map) trên vectơ $K$ không gian có số chiều $n$. Nhắc lại từ Định lý 36.3 (xem Mục 36.1) rằng như K[X]-môđun, $E_{f}$ là ảnh (image) của môđun tự do (free module) E[X] bởi ánh xạ $\sigma$: E[X] $\to E_{f}$, ở đâu E[X] bao gồm của tất cả các tổ hợp tuyến tính của tạo thành
$$p_{1}e_{1} + \cdots  + p_{n}e_{n},$$
Ở đâu $(e_{1}, \dots  , e_{n})$ là cơ sở (basis) của $E$ và $p_{1}, \dots  , p_{n} \in$ K[X] là các đa thức, và $\sigma$ được cho bởi
$$\sigma (p_{1}e_{1} + \cdots  + p_{n}e_{n}) = p_{1}(f)(e_{1}) + \cdots  + p_{n}(f)(e_{n}).$$
Hơn nữa, hạt nhân (kernel) của $\sigma$ bằng ảnh (image) của ánh xạ $\psi$: E[X] $\to$ E[X], ở đâu
$$\psi (p_{1}e_{1} + \cdots  + p_{n}e_{n}) = Xp_{1}e_{1} + \cdots  + Xp_{n}e_{n} -(p_{1}f(e_{1}) + \cdots  + p_{n}(e_{n})).$$
Ma trận $A$ là biểu diễn của ánh xạ tuyến tính (linear map) $f$ trên cơ sở chính tắc (canonical basis) $(e_{1}, \dots  , e_{n})$ của $E = K^{n}$, và và $XI$ - $A$ là ma trận của $\psi$ đối với cơ sở (basis) $(e_{1}, \dots  , e_{n})$

<!-- PAGE 1347 -->
(trên K[X]). Những gì Định lý 36.20 cho ta biết chúng ta là rằng có K[X]-các cơ sở $(u_{1}, \dots  , u_{n})$ và $(v_{1}, \dots  , v_{n})$ của $E_{f}$ đối với mà ma trận của $\psi$ là $D$. Thì
$$\psi (u_{i}) = v_{i},i = 1, \dots  , n -m,$$
$$\psi (u_{n-m+i}) = q_{i}v_{n-m+i},i = 1, \dots  , m,$$
Và bởi vì $Im(\psi$) $=$ Ker $(\sigma$), điều này suy ra rằng
$$\sigma (v_{i}) = 0,i = 1, \dots  , n -m.$$
Hệ quả là, $w_{1} = \sigma (v_{n-m+1}), \dots  , w_{m} = \sigma (v_{n})$ sinh (span) $E_{f}$ như K[X]-môđun, với $w_{i} \in E$, và ta có
$$M(f) = K[X]w_{1} \oplus \cdots  \oplus K[X]w_{m},$$
Ở đâu $K[X]w_{i} \approx K[X]/(q_{i})$ như xích (cyclic) K[X]-môđun. Vì $Im(\psi$) $=$ Ker $(\sigma$), ta có
$$0 = \sigma (\psi (u_{n-m+i})) = \sigma (q_{i}v_{n-m+i}) = q_{i}\sigma (v_{n-m+i}) = q_{i}w_{i},$$
Do đó như vectơ $K$ không gian, xích (cyclic) không gian con $Z(w_{i}; f) = K[X]w_{i}$ có $q_{i}$ như linh hóa tử (annihilator), và bởi nhận xét từ Mục 36.1, nó có cơ sở (basis) (trên $K)$
$$(w_{i}, f(w_{i}), \dots  , f^{ni-1} (w_{i})),n_{i} = deg(q_{i}).$$
Hơn nữa, trên cơ sở (cơ sở (basis)) này, thu hẹp của $f$ đến $Z(w_{i}; f)$ được biểu diễn bởi companion ma trận của $q_{i}$. Bởi đặt tất cả các phần tử này các cơ sở cùng nhau, ta thu được ma trận khối (block matrix) mà là chính tắc hữu tỷ tạo thành của $f$ (và $A)$. Bây giờ, $XI -A = QDP^{-1}$ là ma trận của $\psi$ đối với cơ sở chính tắc (canonical basis) $(e_{1}, \dots  , e_{n})$ (trên K[X]), và $D$ là ma trận của $\psi$ đối với các cơ sở $(u_{1}, \dots  , u_{n})$ và $(v_{1}, \dots  , v_{n})$ (trên K[X]), mà cho ta biết chúng ta rằng các cột của $Q$ bao gồm của các tọa độ (trong K[X]) của cơ sở (basis) các vectơ $(v_{1}, \dots  , v_{n})$ đối với cơ sở (basis) $(e_{1}, \dots  , e_{n})$. Vì vậy, các tọa độ (trong $K)$ của các vectơ $(w_{1}, \dots  , w_{m})$ sinh $E_{f}$ trên K[X], ở đâu $w_{i} = \sigma (v_{n-m+i})$, là thu được bằng cách thế ma trận $A$ cho $X$ trong các tọa độ của các cột các vectơ của $Q$, và evaluating thu được các biểu thức. Vì
$$D = Q^{-1}(XI -A)P,$$
Ma trận $D$ là thu được từ $A$ bởi dãy của các phép biến đổi sơ cấp trên hàng có tích là $Q^{-1}$ và dãy của sơ cấp cột các phép toán có tích là $P$. Vì vậy, để tính các vectơ $w_{1}, \dots  , w_{m}$ từ $A$, ta đơn giản có đến hình ra cách mà để xây dựng $Q$ từ dãy của các phép biến đổi sơ cấp trên hàng rằng cho $Q^{-1}$. mẹo/kỹ thuật là để sử dụng cột các phép toán đến gather tích của hàng các phép toán trong reverse thứ tự. Thật vậy, nếu $Q^{-1}$ là tích của các phép biến đổi sơ cấp trên hàng
$$Q^{-1}= E_{k} \cdots  E_{2}E_{1},$$

<!-- PAGE 1348 -->
Thì
$$Q = E_{1}^{-1} E_{2}^{-1}\cdots  E_{k}^{-1} .$$
Bây giờ, hàng các phép toán operate trên trái và cột các phép toán operate trên phải, do đó tích $E_{1}^{-1} E_{2}^{-1} \cdots  E_{k}^{-1}$ có thể được được tính từ trái đến phải như dãy của cột các phép toán. Cho chúng ta ôn tập/tổng quan có nghĩa của sơ cấp hàng và cột các phép toán P(i, $k), E_{i,j;\beta}$, và $E_{i,\lambda}. 1$. Như hàng phép toán, P(i, $k)$ các hoán vị hàng $i$ và hàng $k. 2$. Như cột phép toán, P(i, $k)$ các hoán vị cột $i$ và cột $k. 3$. nghịch đảo của P(i, $k)$ là P(i, $k)$ chính nó. $4$. Như hàng phép toán, $E_{i,j;\beta}$ cộng $\beta$ lần hàng $j$ đến hàng $i. 5$. Như cột phép toán, $E_{i,j;\beta}$ cộng $\beta$ lần cột $i$ đến cột $j$ (lưu ý switch trong các chỉ số). $6$. nghịch đảo của $E_{i,j;\beta}$ là $E_{i,j;-\beta}. 7$. Như hàng phép toán, $E_{i,\lambda}$ multiplies hàng $i$ bởi $\lambda$. $8$. Như cột phép toán, $E_{i,\lambda}$ multiplies cột $i$ bởi $\lambda$. $9$. nghịch đảo của $E_{i,\lambda}$ là $E_{i,\lambda-1}$. Cho trước ma trận vuông (square matrix) $A$ (trên $K)$, hàng và cột các phép toán ứng dụng đến $XI -A$ trong chuyển đổi nó đến của nó Dạng chuẩn tắc Smith (Smith normal form) có thể liên quan đến các hệ số rằng là các đa thức và nó là cần đến giải thích những gì là action của phép toán $E_{i,j;\beta}$ trong trường hợp này. Nếu hệ số $\beta$ trong $E_{i,j;\beta}$ là đa thức trên $K$, như hàng phép toán, action của $E_{i,j;\beta}$ trên ma trận $X$ là đến nhân hàng thứ $j$ của $M$ bởi ma trận $\beta (A)$ thu được bằng cách thế ma trận $A$ cho $X$ và thì đến cộng thu được vectơ đến hàng $i$. Tương tự, như cột phép toán, action của $E_{i,j;\beta}$ trên ma trận $X$ là đến nhân cột thứ $i$ của $M$ bởi ma trận $\beta (A)$ thu được bằng cách thế ma trận $A$ cho $X$ và thì đến cộng thu được vectơ đến cột $j$. thuật toán để tính dạng chính tắc hữu tỷ (rational canonical form) của ma trận có thể bây giờ là cho trước. Ta áp dụng sơ cấp cột các phép toán $E_{i}^{-1}$ cho $i = 1, \dots  k$, bắt đầu với ma trận đơn vị (identity matrix). Thuật toán cho Chuyển đổi một ma trận cỡ $n \times  n$ đến Dạng chính tắc hữu tỷ (rational canonical form) Trong khi áp dụng sơ cấp hàng và cột các phép toán để tính Dạng chuẩn tắc Smith (Smith normal form) $D$ của $XI$ - $A$, giữ track của hàng các phép toán và perform sau đây các bước: $1$. Cho P' $= I_{n}$, và với mọi sơ cấp hàng phép toán $E$ thực hiện sau đây:
$$(a) If E = P(i, k), permute column i and column k of P' .$$

<!-- PAGE 1349 -->
$$(b) If E = E_{i,j;\beta}, multiply the ith column of P'by the matrix \beta (A) obtained by$$
$$substituting the matrix A for X, and then subtract the resulting vector from$$
$$column j.$$
$$(c) If E = E_{i,\lambda} where \lambda  \in K, then multiply the ith column of P'by \lambda^{-1} .$$
$2$. Khi bước $(1)$ kết thúc, thứ nhất $n$ - $m$ các cột của P' là không và cuối cùng $m$ là độc lập tuyến tính (linearly independent). Cho $i = 1, \dots  , m$, nhân $(n$ - $m +$ i)th cột $w_{i}$ của P' successively bởi I, $A^{1}, A^{2}, A^{ni-1}$, ở đâu $n_{i}$ là bậc của đa thức $q_{i}$ (xuất hiện trong $D)$, và tạo thành ma trận cỡ $n \times  n$ $P$ bao gồm của các vectơ
$$w_{1}, Aw_{1}, \dots  , A^{n1-1}w_{1}, w_{2}, Aw_{2}, \dots  , A^{n2-1}w_{2}, \dots  , w_{m}, Aw_{m}, \dots  , A^{nm-1}w_{m}.$$
Thì, $P^{-1}$ AP là chính tắc hữu tỷ tạo thành của $A$. Đây là một ví dụ được lấy từ Dummit và Foote $[55]$ (Chương $12$, Mục 12.2). Cho $A$ là ma trận
$$A = \begin{pmatrix} 1 & 2 & -4 & 4 \\ 2 & -1 & 4 & -8 \\ 1 & 0 & 1 & -2 \\ 0 & 1 & 2 & 3 \end{pmatrix} .$$
$$-$$
Một nên kiểm tra rằng sau đây dãy của hàng và cột các phép toán produces Dạng chuẩn tắc Smith (Smith normal form) $D$ của $XI$ - $A$: hàng P(1, $3)$ hàng $E_{1,-1}$ hàng $E_{2,1;2}$ hàng $E_{3,1;-(X-1)}$ cột $E_{1,3;X-1}$ cột $E_{1,4;2}$ hàng P(2, $4) rowE_{2,-1}$ hàng $E_{3,2;2}$ hàng $E_{4,2;-(X+1)}$ cột $E_{2,3;2}$ cột $E_{2,4;X-3}$, với
$$D = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & (X-1)^{2} & 0 \\ 0 & 0 & 0 & (X & 1)^{2} \end{pmatrix} .$$
$$-$$
Thì, áp dụng Bước $1$ của ở trên thuật toán, ta thu được dãy của cột các phép toán: 1 $0 0$ 0 0 $0 1$ 0  $0 0 1$ 0 $0 1 0 0$ P(1,3) $0 1 0 0 E 0 1 0 0 E$   $\longrightarrow$   $\longrightarrow^{1}$ 1,-   $\longrightarrow^{2}$ 2,1,- 0 $0 1$ 0 1 $0 0$ 0 -1 $0 0$ 0       $0 0 0 1 0 0 0 1 0 0 0 1$  $0 0 1$ 0 0 $0 1$ 0 0 $0 1$ 0 $-2 1 0 0 E 0 1 0 0$ P(2,4) $0 0 0 1 E$   $3\longrightarrow^{-I}$,1,   $\longrightarrow$   $\longrightarrow^{1}$ 2,- -1 $0 0$ 0 0 $0 0$ 0 0 $0 0$ 0       $0 0 0 1 0 0 0 1 0 1 0 0$ 0 $0 1$ 0 0 $-2 1$ 0 0 $0 1$ 0 $0 0 0 1 E 0 0 0 1 E 0 0 0 1$   $\longrightarrow^{2}$ 3,2,-   $4\longrightarrow^{+I}$,2;   $=$ P'. 0 $0 0$ 0 0 $0 0$ 0 0 $0 0$ 0       $0 -1 0 0 0 -1 0 0 0 0 0 0$

<!-- PAGE 1350 -->
Bước $2$ của thuật toán cho ta các vectơ
$$\begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} ,A \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ 1 \\ 0 \end{pmatrix} , \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} ,A \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 2 \\ -1 \\ 0 \\ 1 \end{pmatrix} ,$$
Do đó ta thu được
$$P = \begin{pmatrix} 1 & 1 & 0 & 2 \\ 0 & 2 & 1 & -1 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} .$$
Ta tìm rằng
$$P^{-1}  = \begin{pmatrix} 1 & 0 & -1 & -2 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & -2 & 1 \\ 0 & 0 & 0 & 1 \end{pmatrix} ,$$
Và do đó, dạng chính tắc hữu tỷ (rational canonical form) của $A$ là
$$P^{-1} AP = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 2 & 0 & 0 \\ 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 2 \end{pmatrix} .$$
