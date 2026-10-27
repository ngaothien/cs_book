# Biểu diễn của Các ánh xạ tuyến tính (linear maps) bởi Các ma trận


<!-- PAGE 125 -->
Chương $4$ Các ma trận và Các ánh xạ tuyến tính (linear maps) Trong chương này, tất cả các không gian vectơ được định nghĩa trên tùy ý trường $K$. Cho sake của concreteness, độc giả có thể safely giả sử rằng $K =\mathbb{R}$.

## 4.1 Biểu diễn của Các ánh xạ tuyến tính (linear maps) bởi Các ma trận

Mệnh đề 3.20 chỉ ra rằng cho trước hai các không gian vectơ $E$ và $F$ và cơ sở (basis) $(u_{j})_{j\in J}$ của $E$, mọi ánh xạ tuyến tính (linear map) $f$: $E \to F$ là một cách duy nhất được xác định bởi họ $(f(u_{j}))_{j\in J}$ của các ảnh dưới $f$ của các vectơ trong cơ sở (basis) $(u_{j})_{j\in J}$. Nếu ta cũng có cơ sở (basis) $(v_{i})_{i\in I}$ của $F$, thì mọi vectơ $f(u_{j})$ có thể được được viết trong duy nhất cách như
$$f(u_{j}) = \sum_{i\in I}  a_{i j}v_{i},$$
Ở đâu $j \in J$, cho họ của các vô hướng $(a_{i j})_{i\in I}$. Do đó, đối với hai các cơ sở $(u_{j})_{j\in J}$ của $E$ và $(v_{i})_{i\in I}$ của $F$, ánh xạ tuyến tính (linear map) $f$ là hoàn toàn được xác định bởi “I ma trận cỡ $\times J$” M(f) $= (a_{i j})_{(i,j)\in I\times J}$.
Nhận xét: Lưu ý rằng ta intentionally assigned chỉ số tập hợp $J$ đến cơ sở (basis) $(u_{j})_{j\in J}$ của $E$, và chỉ số tập hợp $I$ đến cơ sở (basis) $(v_{i})_{i\in I}$ của $F$, sao cho các hàng của ma trận M(f) liên kết với $f$: $E \to F$ được chỉ số bởi I, và các cột của ma trận M(f) được chỉ số bởi $J$. Hiển nhiên, điều này gây ra một cách nhẹ unpleasant reversal. Nếu ta đã có được xét các cơ sở $(u_{i})_{i\in I}$ của $E$ và $(v_{j})_{j\in J}$ của $F$, ta sẽ thu được một ma trận cỡ $J \times I$ M(f) $= (a_{j i})_{(j,i)\in J\times I}$. Không có matter những gì ta thực hiện, ở đó sẽ là reversal! Ta decided đến stick đến các cơ sở $(u_{j})_{j\in J}$ của $E$ và $(v_{i})_{i\in I}$ của $F$, sao cho ta thu được I ma trận cỡ $\times J$ M(f), biết rằng ta có thể occasionally suffer từ điều này decision! Khi I và $J$ là hữu hạn, và nói, khi |I| $= m$ và |J| $= n$, ánh xạ tuyến tính (linear map) $f$ được xác định bởi ma trận M(f) có các phần tử (entries) trong cột thứ $j$ là các thành phần của
$$125$$

<!-- PAGE 126 -->
Vectơ $f(u_{j})$ trên cơ sở (basis) $(v_{1}, \dots  , v_{m})$, nghĩa là, ma trận
$$M(f) = \begin{pmatrix} a_{1 1} & a_{1 2} & \dots & a_{1n} \\ a_{2 1} & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{m n} \end{pmatrix}$$
Có phần tử (entry) trên Hàng $i$ và Cột $j$ là $a_{i j} (1 \le i \le m, 1 \le j \le n)$. Ta sẽ bây giờ chỉ ra rằng khi $E$ và $F$ có hữu hạn số chiều, các ánh xạ tuyến tính (linear maps) có thể được rất một cách thuận tiện được biểu diễn bởi các ma trận, và rằng hợp thành của các ánh xạ tuyến tính (linear maps) tương ứng với phép nhân ma trận (matrix multiplication). Ta sẽ suy ra khá closely thanh lịch trình bày phương pháp do Emil Artin. Cho $E$ và $F$ là hai các không gian vectơ, và giả sử rằng $E$ có hữu hạn cơ sở (basis) $(u_{1}, \dots  , u_{n})$ và rằng $F$ có hữu hạn cơ sở (basis) $(v_{1}, \dots  , v_{m})$. Nhắc lại rằng ta có được hiển thị rằng mọi vectơ $x \in E$ có thể được được viết trong duy nhất cách như
$$x = x_{1}u_{1} + \cdots  + x_{n}u_{n},$$
Và tương tự mọi vectơ $y \in F$ có thể được được viết trong duy nhất cách như
$$y = y_{1}v_{1} + \cdots  + y_{m}v_{m}.$$
Cho $f$: $E \to F$ là ánh xạ tuyến tính (linear map) giữa $E$ và $F$. Thì với mọi $x = x_{1}u_{1} + \cdots  + x_{n}u_{n}$ trong $E$, bởi tính tuyến tính, ta có
$$f(x) = x_{1}f(u_{1}) + \cdots  + x_{n}f(u_{n}).$$
Cho
$$f(u_{j}) = a_{1j}v_{1} + \cdots  + a_{m j}v_{m},$$
Hoặc nhiều hơn/thêm ngắn gọn,
$$f(u_{j}) = \sum_{i=1}^{m}  a_{i j}v_{i},$$
Với mọi $j, 1 \le j \le n$. Điều này có thể được được biểu diễn bởi viết các hệ số $a_{1j}, a_{2j}, \dots  , a_{mj}$ của $f(u_{j})$ trên cơ sở (basis) $(v_{1}, \dots  , v_{m})$, như cột thứ $j$ của ma trận, như được hiển thị dưới đây:
$$f(u_{1})f(u_{2})\dots f(u_{n})$$
$$v_{1}$$
$$v_{2}\vdots \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{pmatrix} .$$
$$v_{m}$$
Thì thế vế phải của mỗi $f(u_{j})$ vào biểu thức cho f(x), ta thu được
$$f(x) = x_{1}( \sum_{i=1}^{m}  a_{i1}v_{i}) + \cdots  + x_{n}( \sum_{i=1}^{m}  a_{i n}v_{i}),$$

<!-- PAGE 127 -->
Mà, bởi regrouping các số hạng để thu được tổ hợp tuyến tính (linear combination) của $v_{i}$, cho ta
$$f(x) = ( \sum_{j=1}^{n}  a_{1j}x_{j})v_{1} + \cdots  + ( \sum_{j=1}^{n}  a_{m j}x_{j})v_{m}.$$
Do đó, đặt f(x) $= y = y_{1}v_{1} + \cdots  + y_{m}v_{m}$, ta có
$$y_{i} = \sum_{j=1}^{n}  a_{i j}x_{j}(1)$$
Với mọi $i, 1 \le i \le m$. để tạo things nhiều hơn/thêm concrete, cho chúng ta treat trường hợp ở đâu $n = 3$ và $m = 2$. Trong trường hợp này,
$$f(u_{1}) = a_{11}v_{1} + a_{21}v_{2}$$
$$f(u_{2}) = a_{12}v_{1} + a_{22}v_{2}$$
$$f(u_{3}) = a_{13}v_{1} + a_{23}v_{2},$$
Mà trong ma trận tạo thành được biểu diễn bởi
$$f(u_{1})f(u_{2})f(u_{3})$$
$$v_{1}$$
$$v_{2} \begin{pmatrix} a \\ 11 & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \end{pmatrix} ,$$
Và với mọi $x = x_{1}u_{1} + x_{2}u_{2} + x_{3}u_{3}$, ta có
$$f(x) = f(x_{1}u_{1} + x_{2}u_{2} + x_{3}u_{3})$$
$$= x_{1}f(u_{1}) + x_{2}f(u_{2}) + x_{3}f(u_{3})$$
$$= x_{1}(a_{11}v_{1} + a_{21}v_{2}) + x_{2}(a_{12}v_{1} + a_{22}v_{2}) + x_{3}(a_{13}v_{1} + a_{23}v_{2})$$
$$= (a_{11}x_{1} + a_{12}x_{2} + a_{13}x_{3})v_{1} + (a_{21}x_{1} + a_{22}x_{2} + a_{23}x_{3})v_{2}.$$
Hệ quả là, vì
$$y = y_{1}v_{1} + y_{2}v_{2},$$
Ta có
$$y_{1} = a_{11}x_{1} + a_{12}x_{2} + a_{13}x_{3}$$
$$y_{2} = a_{21}x_{1} + a_{22}x_{2} + a_{23}x_{3}.$$
Điều này agrees với phương trình ma trận
$$\begin{pmatrix} y_{1} \\ y_{2} \end{pmatrix} = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \end{pmatrix} .$$
Ta bây giờ formalize biểu diễn của các ánh xạ tuyến tính (linear maps) bởi các ma trận.

<!-- PAGE 128 -->

> **Định nghĩa 4.1.** Cho $E$ và $F$ là hai các không gian vectơ, và cho $(u_{1}, \dots  , u_{n})$ là cơ sở (basis) cho $E$, và $(v_{1}, \dots  , v_{m})$ là cơ sở (basis) cho $F$. Mỗi vectơ $x \in E$ được biểu diễn trong cơ sở (basis) $(u_{1}, \dots  , u_{n})$ như $x = x_{1}u_{1} + \cdots  + x_{n}u_{n}$ được biểu diễn bởi ma trận cột
$$M(x) = \begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix}$$
Và tương tự với mỗi vectơ $y \in F$ được biểu diễn trong cơ sở (basis) $(v_{1}, \dots  , v_{m})$. Mọi ánh xạ tuyến tính (linear map) $f$: $E \to F$ được biểu diễn bởi ma trận M(f) $= (a_{i j})$, ở đâu $a_{i j}$ là thành phần thứ $i$ của vectơ $f(u_{j})$ trên cơ sở (basis) $(v_{1}, \dots  , v_{m})$, i.e., ở đâu
$$f(u_{j}) = \sum_{i=1}^{m}  a_{i j}v_{i},for every j, 1 \le j \le n.$$
Các hệ số $a_{1j}, a_{2j}, \dots  , a_{mj}$ của $f(u_{j})$ trên cơ sở (basis) $(v_{1}, \dots  , v_{m})$ tạo thành cột thứ $j$ của ma trận M(f) được hiển thị dưới đây:
$$f(u_{1})f(u_{2})\dots f(u_{n})$$
$$v_{1}$$
$$v_{2}\vdots \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{pmatrix} .$$
$$v_{m}$$
Ma trận M(f) liên kết với ánh xạ tuyến tính (linear map) $f$: $E \to F$ được gọi là ma trận của $f$ đối với các cơ sở $(u_{1}, \dots  , u_{n})$ và $(v_{1}, \dots  , v_{m})$. Khi $E = F$ và cơ sở (basis) $(v_{1}, \dots  , v_{m})$ là đồng nhất đến cơ sở (basis) $(u_{1}, \dots  , u_{n})$ của $E$, ma trận M(f) liên kết với $f$: $E \to E$ (như ở trên) được gọi là ma trận của $f$ đối với cơ sở (basis) $(u_{1}, \dots  , u_{n})$.
Nhận xét: Như trong nhận xét sau Định nghĩa 3.12, không có lý do giả sử rằng các vectơ trong các cơ sở $(u_{1}, \dots  , u_{n})$ và $(v_{1}, \dots  , v_{m})$ được thứ tự trong bất kỳ cụ thể cách. Tuy nhiên, nó là thường thuận tiện giả sử thứ tự tự nhiên. Khi điều này là do đó, các tác giả đôi khi refer đến ma trận M(f) như ma trận của $f$ đối với được thứ tự các cơ sở $(u_{1}, \dots  , u_{n})$ và $(v_{1}, \dots  , v_{m})$. Cho chúng ta minh họa biểu diễn của ánh xạ tuyến tính (linear map) bởi ma trận trong concrete tình huống. Cho $E$ là vectơ $space\mathbb{R}[x]_{4}$ của các đa thức của bậc nhiều nhất $4$, cho $F$ là không gian vectơ (vector space) $\mathbb{R}[x]_{3}$ của các đa thức của bậc nhiều nhất $3$, và cho ánh xạ tuyến tính (linear map) là đạo hàm ánh xạ $d$: rằng là,
$$d(P + Q) = dP + dQ$$
$$d(\lambda P) = \lambda dP,$$

<!-- PAGE 129 -->
Với $\lambda  \in \mathbb{R}$. Ta chọn $(1, x, x^{2}, x^{3}, x^{4})$ như cơ sở (basis) của $E$ và $(1, x, x^{2}, x^{3})$ như cơ sở (basis) của $F$. Thì ma trận cỡ $4 \times  5$ $D$ liên kết với $d$ là thu được bởi biểu diễn đạo hàm $dx^{i}$ của mỗi cơ sở (basis) vectơ $x^{i}$ cho $i = 0, 1, 2, 3, 4$ trên cơ sở (basis) $(1, x, x^{2}, x^{3})$. Ta tìm
$$D = \begin{pmatrix} 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 2 & 0 & 0 \\ 0 & 0 & 0 & 3 & 0 \\ 0 & 0 & 0 & 0 & 4 \end{pmatrix} .$$
Nếu $P$ ký hiệu đa thức
$$P = 3x^{4}-5x^{3}+ x^{2}-7x + 5,$$
Ta có
$$dP = 12x^{3}-15x^{2}+ 2x -7.$$
Đa thức $P$ được biểu diễn bởi vectơ $(5, -7, 1, -5, 3)$, đa thức dP được biểu diễn bởi vectơ $(-7, 2$, -15, $12)$, và ta có
$$\begin{pmatrix} 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 2 & 0 & 0 \\ 0 & 0 & 0 & 3 & 0 \\ 0 & 0 & 0 & 0 & 4 \end{pmatrix} \begin{pmatrix} 5 \\ -7 \\ 1 \\ -5 \\ 3 \end{pmatrix} = \begin{pmatrix} -7 \\ 2 \\ -15 \\ 12 \end{pmatrix} ,$$
Như được kỳ vọng! hạt nhân (kernel) (không gian hạch (nullspace)) của $d$ bao gồm của các đa thức của bậc $0$, nghĩa là, hằng số các đa thức. Vì vậy dim(Ker $d) = 1$, và từ
$$\dim(E) = \dim(\mathrm{Ker} d) + \dim(\mathrm{Im} d)$$
(xem Định lý 6.16), ta thu được dim(Im $d) = 4$ (vì dim(E) $= 5)$. Cho fun, cho chúng ta hình ra ánh xạ tuyến tính (linear map) từ không gian vectơ (vector space) $\mathbb{R}[x]_{3}$ đến không gian vectơ (vector space) $\mathbb{R}[x]_{4}$ cho trước bởi phép lấy tích phân (việc tìm primitive, hoặc anti-derivative) của $x^{i}$, cho $i = 0, 1, 2, 3)$.
$$The 5 \times  4 matrix S representing \int  with respect to the same bases as before is$$
$$S = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 1/2 & 0 & 0 \\ 0 & 0 & 1/3 & 0 \\ 0 & 0 & 0 & 1/4 \end{pmatrix} .$$
Ta kiểm chứng rằng $DS = I_{4}$,
$$\begin{pmatrix} 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 2 & 0 & 0 \\ 0 & 0 & 0 & 3 & 0 \\ 0 & 0 & 0 & 0 & 4 \end{pmatrix} \begin{pmatrix} 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 1/2 & 0 & 0 \\ 0 & 0 & 1/3 & 0 \\ 0 & 0 & 0 & 1/4 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} .$$
