# Các ma trận của Các ánh xạ tuyến tính (linear maps) và Phép nhân bởi Các khối


<!-- PAGE 189 -->
$$f(x,y) = (x,y,0)$$
$$u = (1,1)$$
$$2$$
$$v = (0,0,1)$$
$$3$$
$$\overline{u = (1,0)}$$
$$1$$
$$v = f(u ) = (1,0,0)$$
$$11v  = f(u ) = (1,1,0)$$
$$22$$
$$E = R^{2}$$
$$r(x,y,z) = (x,y)F = R^{3}$$
$$\mathbb{R}^{2}  \mathbb{R}^{3}$$

![Figure 6.2](../../assets/ch06/fig_6_2.png)

**Hình 6.2:** Cho $f$: $E \to F$ là đơn ánh (injective) ánh xạ tuyến tính (linear map) từ đến cho trước bởi f(x, $y) =$
$$\mathbb{R}^{3} \mathbb{R}^{2}$$
$(x, y, 0)$. Thì toàn ánh (surjective) phép co rút (retraction) được cho bởi $r: \to$ được cho bởi r(x, $y, z) = (x, y)$. Nhận thấy rằng $r(v_{1}) = u_{1}, r(v_{2}) = u_{2}$, và $r(v_{3}) = 0$.

## 6.2 Các ma trận của Các ánh xạ tuyến tính (linear maps) và Phép nhân bởi

$$Blocks$$
Các tổng trực tiếp cho fairly dễ justification của ma trận khối phép nhân. then chốt ý tưởng là rằng biểu diễn của ánh xạ tuyến tính (linear map) $f$: $E \to F$ trên cơ sở (basis) $(u_{1}, \dots  , u_{n})$ của $E$ và cơ sở (basis) $(v_{1}, \dots  , v_{m})$ của $F$ bởi ma trận $A = (a_{ij})$ của các vô hướng (trong $K)$ có thể được suy rộng/tổng quát hóa đến biểu diễn của $f$ trên tổng trực tiếp (direct sum) phân rã $E = E_{1} \oplus \cdots  \oplus E_{n}$ của $E$ và tổng trực tiếp (direct sum) phân rã $F = F_{1} \oplus \cdots  \oplus F_{m}$ của $F$ theo ma trận $(f_{ij})$ của các ánh xạ tuyến tính (linear maps) $f_{ij}$: $E_{j} \to F_{i}$. Futhermore, phép nhân ma trận (matrix multiplication) của vô hướng (scalar) các ma trận mở rộng một cách tự nhiên đến phép nhân ma trận (matrix multiplication) của các ma trận của các ánh xạ tuyến tính (linear maps). Ta đơn giản có đến thay thế phép nhân của các vô hướng trong $K$ bởi hợp thành của các ánh xạ tuyến tính (linear maps). Cho $E$ và $F$ là hai các không gian vectơ và giả sử rằng chúng được biểu diễn như các tổng trực tiếp
$$nm$$
$$E =ME_{j},F =MF_{i}.$$
$$j=1i=1$$

> **Định nghĩa 6.6.** Cho trước bất kỳ ánh xạ tuyến tính (linear map) $f$: $E \to F$, ta định nghĩa các ánh xạ tuyến tính (linear maps) $f_{ij}$: $E_{j} \to F_{i}$ như sau. Cho $pr_{i}^{F}$: $F \to F_{i}$ là phép chiếu của $F = F_{1} \oplus \cdots  \oplus F_{m}$ lên $F_{i}$. Nếu $f_{j}$: $E_{j} \to F$ là thu hẹp của $f$ đến $E_{j}$, mà có nghĩa là với mọi vectơ $x_{j} \in E_{j}$,
$$f_{j}(x_{j}) = f(x_{j}),$$
Thì ta định nghĩa ánh xạ $f_{ij}$: $E_{j} \to F_{i}$ bởi
$$f_{ij} = pr_{i}^{F} \circ f_{j},$$

<!-- PAGE 190 -->
Sao cho nếu $x_{j} \in E_{j}$, thì
$$f(x_{j}) = f_{j}(x_{j}) = \sum_{i=1}^{m}  f_{ij}(x_{j}),with f_{ij}(x_{j}) \in F_{i}.(\dagger_{1} )$$
Nhận thấy rằng ta là summing trên chỉ số $i$, mà eventually tương ứng với summing các phần tử (entries) trong cột thứ $j$ của ma trận biểu diễn $f$; xem Định nghĩa 6.7. Ta xem rằng với mọi vectơ $x = x_{1} + \cdots  + x_{n} \in E$, với $x_{j} \in E_{j}$, ta có
$$f(x) = \sum_{j=1}^{n}  f_{j}(x_{j}) = \sum_{j=1}^{n}  \sum_{i=1}^{m}  f_{ij}(x_{j}) = \sum_{i=1j}^{m}  \sum_{=1}^{n}  f_{ij}(x_{j}).$$
Nhận thấy rằng ngược lại, cho trước họ $(f_{ij})_{1\le i\le m,1\le j\le n}$ của các ánh xạ tuyến tính (linear maps) $f_{ij}$: $E_{j} \to F_{i}$, ta thu được ánh xạ tuyến tính (linear map) $f$: $E \to F$ được định nghĩa sao cho với mọi $x = x_{1} + \cdots  + x_{n} \in E$, với $x_{j} \in E_{j}$, ta có
$$f(x) = \sum_{i=1j}^{m}  \sum_{=1}^{n}  f_{ij}(x_{j}).$$
Hệ quả là, nó là dễ để kiểm tra rằng có một đẳng cấu giữa các không gian vectơ
$$Hom(E, F)and \prod_{1\le i\le m}  Hom(E_{j}, F_{i}).$$
$$1\le j\le n$$

> **Ví dụ 6.1.** Giả sử rằng $E = E_{1} \oplus E_{2}$ và $F = F_{1} \oplus F_{2} \oplus F_{3}$, và rằng ta có sáu các ánh xạ $f_{ij}$: $E_{j} \to F_{i}$ cho $i = 1, 2, 3$ và $j = 1, 2$. Với mọi $x = x_{1} + x_{2}$, với $x_{1} \in E_{1}$ và $x_{2} \in E_{2}$, ta có
$$y_{1} = f_{11}(x_{1}) + f_{12}(x_{2}) \in F_{1}$$
$$y_{2} = f_{21}(x_{1}) + f_{22}(x_{2}) \in F_{2}$$
$$y_{3} = f_{31}(x_{1}) + f_{32}(x_{2}) \in F_{3},$$
$$f_{1}(x_{1}) = f_{11}(x_{1}) + f_{21}(x_{1}) + f_{31}(x_{1})$$
$$f_{2}(x_{2}) = f_{12}(x_{2}) + f_{22}(x_{2}) + f_{32}(x_{2}),$$
Và
$$f(x) = f_{1}(x_{1}) + f_{2}(x_{2}) = y_{1} + y_{2} + y_{3}$$
$$= f_{11}(x_{1}) + f_{12}(x_{2}) + f_{21}(x_{1}) + f_{22}(x_{2}) + f_{31}(x_{1}) + f_{32}(x_{2}).$$
Các phương trình này suggest ma trận ký hiệu
$$\begin{pmatrix} y_{1} \\ y_{2} \\ y_{3} \end{pmatrix} = \begin{pmatrix} f_{11} & f_{12} \\ f_{21} & f_{22} \\ f_{31} & f_{32} \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} .$$

<!-- PAGE 191 -->
Nói chung ta tiến hành như sau. Với mọi $x = x_{1} + \cdots  + x_{n}$ với $x_{j} \in E_{j}$, nếu $y =$ f(x), vì $F = F_{1} \oplus \cdots  \oplus F_{m}$, vectơ $y \in F$ có duy nhất phân rã $y = y_{1} + \cdots  + y_{m}$
$$with y_{i} \in F_{i}, and since f_{ij} : E_{j} \to F_{i}, we have \sum_{j}  n f_{ij}(x_{j}) \in F_{i}, so \sum_{j}  n=1 f_{ij}(x_{j}) \in F_{i} is the$$
Thành phần thứ $i$ của f(x) trên tổng trực tiếp (direct sum) $F = F_{1}^{=1} \oplus \cdots  \oplus F_{m}$; tương đương
$$pr_{i}^{F} (f(x)) = \sum_{j=1}^{n}  f_{ij}(x_{j}),1 \le i \le m.$$
Hệ quả là, ta có
$$y_{i} = \sum_{j=1}^{n}  f_{ij}(x_{j}),1 \le i \le m.(\dagger_{2} )$$
Điều này time ta là summing trên chỉ số $j$, mà eventually tương ứng với nhân hàng thứ $i$ của ma trận biểu diễn $f$ bởi bộ $n$ $(x_{1}, \dots  , x_{n})$; xem Định nghĩa 6.7. Tất cả điều này suggests tổng quát hóa của ma trận ký hiệu Ax, ở đâu $A$ là ma trận của các vô hướng và $x$ là vectơ cột (column vector) của các vô hướng, cụ thể là đến viết
$$\begin{pmatrix} y_{1} \\ \vdots \\ y_{m} \end{pmatrix} = \begin{pmatrix} f_{1 1} & \dots & f_{1n} \\ \vdots & \ddots & \vdots \\ f_{m1} & \dots & f_{m n} \end{pmatrix} \begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix} ,(\dagger_{3} )$$
Mà là abbreviation cho $m$ các phương trình
$$y_{i} = \sum_{j=1}^{n}  f_{ij}(x_{j}),i = 1, \dots  , m.$$
Interpretation của phép nhân của một ma trận cỡ $m \times  n$ của các ánh xạ tuyến tính (linear maps) $f_{ij}$ bởi vectơ cột (column vector) của $n$ các vectơ $x_{j} \in E_{j}$ là để áp dụng mỗi $f_{ij}$ đến $x_{j}$ để thu được $f_{ij}(x_{j})$ và đến tổng trên chỉ số $j$ để thu được thứ $i$ output vectơ. Điều này là tổng quát hóa của nhân vô hướng (scalar) $a_{ij}$ bởi vô hướng (scalar) $x_{j}$. Cũng lưu ý rằng cột thứ $j$ của ma trận $(f_{ij})$ bao gồm của các ánh xạ $(f_{1j}, \dots  , f_{mj})$ sao cho $(f_{1j}(x_{j}), \dots  , f_{mj}(x_{j}))$ là các thành phần của $f(x_{j}) = f_{j}(x_{j})$ trên tổng trực tiếp (direct sum) $F = F_{1} \oplus \cdots  \oplus F_{m}$. Trong trường hợp đặc biệt trong mà mỗi $E_{j}$ và mỗi $F_{i}$ là một chiều, điều này là tương đương đến chọn cơ sở (basis) $(u_{1}, \dots  , u_{n})$ trong $E$ sao cho $E_{j}$ là một chiều không gian con $E_{j} = Ku_{j}$, và cơ sở (basis) $(v_{1}, \dots  , v_{m})$ trong $F_{j}$ sao cho $F_{i}$ là một chiều không gian con $F_{i} = Kv_{i}$. Trong trường hợp này mọi vectơ $x \in E$ được biểu diễn như $x = x_{1}u_{1} + \cdots  + x_{n}u_{n}$, ở đâu $x_{i} \in K$ là các vô hướng và tương tự mọi vectơ $y \in F$ được biểu diễn như $y = y_{1}v_{1} + \cdots  + y_{m}v_{m}$, ở đâu $y_{i} \in K$ là các vô hướng. Mỗi ánh xạ tuyến tính (linear map) $f_{ij}$: $E_{j} \to F_{i}$ là ánh xạ giữa một chiều các không gian $Ku_{j}$ và $Kv_{i}$, do đó nó là của tạo thành $f_{ij}(x_{j}u_{j}) = a_{ij}x_{j}v_{i}$, với $x_{j} \in K$, và do đó ma trận $(f_{ij})$ của các ánh xạ tuyến tính (linear maps) $f_{ij}$ là trong tương ứng một-một (bijection) với ma trận $(a_{ij})$ của các vô hướng trong $K$, và Phương trình $(\dagger_{3}$) ở đâu $x_{j}$ và $y_{i}$ là các vectơ là tương đương đến cùng familar phương trình ở đâu $x_{j}$ và $y_{i}$ là vô hướng (scalar) các tọa độ của $x$ và $y$ trên respective các cơ sở.

<!-- PAGE 192 -->

> **Định nghĩa 6.7.** Cho $E$ và $F$ là hai các không gian vectơ và giả sử rằng chúng được biểu diễn như các tổng trực tiếp
$$nm$$
$$E =ME_{j},F =MF_{i}.$$
$$j=1i=1$$
Cho trước bất kỳ ánh xạ tuyến tính (linear map) $f$: $E \to F$, nếu $(f_{ij})_{1\le i\le m,1\le j\le n}$ là familiy của các ánh xạ tuyến tính (linear maps) $f_{ij}$: $E_{j} \to F_{i}$ được định nghĩa trong Định nghĩa 6.6, ma trận cỡ $m \times  n$ của các ánh xạ tuyến tính (linear maps)
$$M(f) = \begin{pmatrix} f_{1 1} & \dots & f_{1n} \\ \vdots & \ddots & \vdots \\ f_{m1} & \dots & f_{m n} \end{pmatrix}$$
Được gọi là ma trận của $f$ đối với các phân rã $n  E_{j}$, và $m  F_{i}$ của $E$ và
$$as direct sums. \bigoplus_{j}  =1 \bigoplus_{i}  =1$$
$F$ Với mọi $x = x_{1} + \cdots  + x_{n} \in E$ với $x_{j} \in E_{j}$ và bất kỳ $y = y_{1} + \cdots  + y_{m} \in F$ với $y_{i} \in F_{i}$, ta có $y =$ f(x) khi và chỉ khi
$$\begin{pmatrix} y_{1} \\ \vdots \\ y_{m} \end{pmatrix} = \begin{pmatrix} f_{1 1} & \dots & f_{1n} \\ \vdots & \ddots & \vdots \\ f_{m1} & \dots & f_{m n} \end{pmatrix} \begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix} ,$$
Ở đâu phương trình ma trận ở trên có nghĩa là hệ của $m$ các phương trình
$$y_{i} = \sum_{j=1}^{n}  f_{ij}(x_{j}),i = 1 \dots  , m,(\dagger )$$
Nghiệm đúng. Nhưng bây giờ ta có thể cũng promote phép nhân ma trận (matrix multiplication). Giả sử ta có thứ ba không gian $G$ được viết như tổng trực tiếp (direct sum). Nó là nhiều hơn/thêm thuận tiện đến viết
$$pnm$$
$$E =ME_{k},F =MF_{j},G =MG_{i}.$$
$$k=1j=1i=1$$
Giả sử ta cũng có hai các ánh xạ tuyến tính (linear maps) $f$: $E \to F$ và $g: F \to G$. Bây giờ ta có ma trận cỡ $n \times  p$ của các ánh xạ tuyến tính (linear maps) $B = (f_{jk})$ và ma trận cỡ $m \times  n$ của các ánh xạ tuyến tính (linear maps) $A = (g_{ij})$. Ta sẽ like để tìm ma trận cỡ $m \times  p$ liên kết với $g \circ f$. Theo định nghĩa của $f_{k}$: $E_{k} \to F$ và $f_{jk}$: $E_{k} \to F_{j}$, nếu $x_{k} \in E_{k}$, thì
$$f_{k}(x_{k}) = f(x_{k}) = \sum_{j=1}^{n}  f_{jk}(x_{k}),with f_{jk}(x_{k}) \in F_{j},(*_{1})$$
Và tương tự, theo định nghĩa của $g_{j}$: $F_{j} \to G$ và $g_{ij}$: $F_{j} \to G_{i}$, nếu $y_{j} \in F_{j}$, thì
$$g_{j}(y_{j}) = g(y_{j}) = \sum_{i=1}^{m}  g_{ij}(y_{j}),with g_{ij}(y_{j}) \in G_{i}.(*_{2})$$

<!-- PAGE 193 -->
Nếu ta viết $h = g \circ f$, ta cần để tìm các ánh xạ $h_{k}$: $E_{k} \to G$, với
$$h_{k}(x_{k}) = h(x_{k}) = (g \circ f)(x_{k}),$$
Và $h_{ik}$: $E_{k} \to G_{i}$ cho trước bởi
$$h_{ik} = pr_{i}^{G} \circ h_{k}.$$
Ta có
$$h_{k}(x_{k}) = (g \circ f)(x_{k}) = g(f(x_{k})) = g(f_{k}(x_{k}))$$
$$= g \begin{pmatrix} f_{jk}(x_{k}) \end{pmatrix} \sum_{j=1}^{n}  by (*_{1})$$
$$= \sum_{j=1}^{n}  g(f_{jk}(x_{k})) = \sum_{j=1}^{n}  g_{j}(f_{jk}(x_{k}))since g is linear$$
$$= \sum_{j=1}^{n}  \sum_{i=1}^{m}  g_{ij}(f_{jk}(x_{k})) = \sum_{i=1j}^{m}  \sum_{=1}^{n}  g_{ij}(f_{jk}(x_{k})),by (*_{2})$$
$$and since \sum_{j}  n=1 g_{ij}(f_{jk}(x_{k})) \in G_{i}, we conclude that$$
$$h_{ik}(x_{k}) = \sum_{j=1}^{n}  g_{ij}(f_{jk}(x_{k})) = \sum_{j=1}^{n}  (g_{ij} \circ f_{jk})(x_{k}),(*_{3})$$
Mà có thể cũng được biểu diễn như
$$h_{ik} = \sum_{j=1}^{n}  g_{ij} \circ f_{jk}.(*_{4})$$
Phương trình $(*_{4})$ là chính xác tương tự của công thức cho phép nhân của các ma trận của các vô hướng! Ta chỉ có đến thay thế phép nhân bởi hợp thành. ma trận cỡ $m \times  p$ của các ánh xạ tuyến tính (linear maps) $(h_{ik})$ là “tích” AB của các ma trận của các ánh xạ tuyến tính (linear maps) $A = (g_{ij})$ và $B = (f_{jk})$, ngoại trừ rằng phép nhân được thay thế bởi hợp thành. Trong tóm tắt ta chỉ được chứng minh kết quả sau đây.

> **Mệnh đề 6.12.** Cho $E, F, G$ là ba các không gian vectơ được biểu diễn như các tổng trực tiếp
$$pnm$$
$$E =ME_{k},F =MF_{j},G =MG_{i}.$$
$$k=1j=1i=1$$
Với mọi hai các ánh xạ tuyến tính (linear maps) $f$: $E \to F$ và $g: F \to G$, cho $B = (f_{jk})$ là ma trận cỡ $n \times  p$ của các ánh xạ tuyến tính (linear maps) liên kết với $f$ (đối với phân rã của $E$ và $F$ như các tổng trực tiếp) và cho $A = (g_{ij})$ là ma trận cỡ $m \times  n$ của các ánh xạ tuyến tính (linear maps) liên kết với $g$ (đối với phân rã của $F$ và $G$ như các tổng trực tiếp). Thì ma trận cỡ $m \times  p$ $C = (h_{ik})$ của các ánh xạ tuyến tính (linear maps)

<!-- PAGE 194 -->
Liên kết với $h = g \circ f$ (đối với phân rã của $E$ và $G$ như các tổng trực tiếp) được cho bởi
$$C = AB,$$
Với
$$h_{ik} = \sum_{j=1}^{n}  g_{ij} \circ f_{jk},1 \le i \le m, 1 \le k \le p.$$
Ta sẽ sử dụng Mệnh đề 6.12 đến justify quy tắc cho khối phép nhân của các ma trận. difficulty là một cách hầu hết notational. Một lần nữa giả sử rằng $E$ và $F$ được biểu diễn như các tổng trực tiếp
$$nm$$
$$E =ME_{j},F =MF_{i},$$
$$j=1i=1$$
Và cho $f$: $E \to F$ là ánh xạ tuyến tính (linear map). Hơn nữa, giả sử rằng $E$ có hữu hạn cơ sở (basis) $(u_{t})_{t\in T}$, ở đâu $T$ là rời nhau hợp $T = T_{1} \cup \cdots  \cup T_{n}$ của khác rỗng các tập con $T_{j}$ sao cho $(u_{t})_{t\in Tj}$ là cơ sở (basis) của $E_{j}$, và tương tự $F$ có hữu hạn cơ sở (basis) $(v_{s})_{s\in S}$, ở đâu $S$ là rời nhau hợp $S = S_{1} \cup \cdots  \cup S_{m}$ của khác rỗng các tập con $S_{i}$ sao cho $(v_{s})_{s\in Si}$ là cơ sở (basis) của $F_{i}$. Cho $M =$ |S|, $N =$ |T|, $s_{i} = |S_{i}|$, và cho $t_{j} = |T_{j}|$. Vì $s_{i}$ là số của các phần tử trong cơ sở (basis) $(v_{s})_{s\in Si}$ của $F_{i}$ và $F = F_{1} \oplus \cdots  \oplus F_{m}$, ta có $M =$ dim(F) $= s_{1} + \cdots  + s_{m}$. Tương tự, vì $t_{j}$ là số của các phần tử trong cơ sở (basis) $(u_{t})_{t\in Tj}$ của $E_{j}$ và $E = E_{1} \oplus \cdots  \oplus E_{n}$, ta có $N =$ dim(E) $= t_{1} + \cdots  + t_{n}$. Cho $A = (a_{st})_{(s,t)\in S\times T}$ là (thông thường) $M \times  N$ ma trận của các vô hướng (trong $K)$ biểu diễn $f$ đối với cơ sở (basis) $(u_{t})_{t\in T}$ của $E$ và cơ sở (basis) $(v_{s})_{s\in S}$ của $F$ với $M = r_{1} + \cdots  + r_{m}$ và $N = s_{1} + \cdots  + s_{n}$, mà có nghĩa là với mọi $t \in T$, tth cột của $A$ bao gồm của các thành phần $a_{st}$ của $f(u_{t})$ trên cơ sở (basis) $(v_{s})_{s\in S}$, như trong bắt đầu của Mục 4.1. Với mọi $i$ và bất kỳ $j$ sao cho $1 \le i \le m$ và $1 \le j \le n$, ta có thể tạo thành ma trận cỡ $s_{i} \times  t_{j}$ $A_{Si,Tj}$ thu được bởi xóa tất cả các hàng trong $A$ của chỉ số $s \in / S_{i}$ và tất cả các cột trong $A$ của chỉ số $t \in / T_{j}$. ma trận $A_{Si,Tj}$ là họ có chỉ số (indexed family) $(a_{st})_{(s,t)\in Si\times Tj}$, như được giải thích tại bắt đầu của Mục 4.1. Nhận thấy rằng ma trận $A_{Si,Tj}$ là thực sự ma trận biểu diễn ánh xạ tuyến tính (linear map) $f_{ij}$: $E_{j} \to F_{i}$ của Định nghĩa 6.7 đối với cơ sở (basis) $(u_{t})_{t\in Tj}$ của $E_{j}$ và cơ sở (basis) $(v_{s})_{s\in Si}$ của $F_{i}$, trong nghĩa rằng với mọi $t \in T_{j}$, tth cột của $A_{Si,Tj}$ bao gồm của các thành phần $a_{st}$ của $f_{ij}(u_{t})$ trên cơ sở (basis) $(v_{s})_{s\in Si}$.

> **Định nghĩa 6.8.** Cho trước một ma trận cỡ $M \times  N$ $A$ (với các phần tử (entries) trong $K)$, ta định nghĩa ma trận cỡ $m \times  n$ $(A_{ij})_{1\le i\le m,1\le j\le n}$ có phần tử (entry) $A_{ij}$ là ma trận $A_{ij} = A_{Si,Tj}, 1 \le i \le m, 1 \le j \le n$, và ta gọi nó ma trận khối (block matrix) của $A$ liên kết với các phân hoạch $S = S_{1} \cup \cdots  \cup S_{m}$ và $T = T_{1} \cup \cdots \cup T_{n}$. ma trận $A_{Si,Tj}$ là một ma trận cỡ $s_{i} \times t_{j}$ được gọi là $(i$, j)th khối của điều này ma trận khối (block matrix). Ở đây ta chạy vào notational dilemma mà thực hiện không dường như là addressed trong literature. Horn và Johnson $[98]$ (Mục 0.7) định nghĩa được phân hoạch các ma trận như ta thực hiện, nhưng chúng thực hiện không propose ký hiệu cho các ma trận khối.

<!-- PAGE 195 -->
Bài toán là rằng ma trận khối (block matrix) $(A_{ij})_{1\le i\le m,1\le j\le n}$ là không bằng ban đầu ma trận $A$. Thứ nhất của tất cả, ma trận khối (block matrix) là $m \times  n$ và các phần tử (các phần tử (entries)) của nó là các ma trận, nhưng ma trận $A$ là $M \times  N$ và các phần tử (các phần tử (entries)) của nó là các vô hướng. Nhưng chẵn/ngay cả nếu ta nghĩ của ma trận khối (block matrix) như một ma trận cỡ $M \times  N$ của các vô hướng, một số các hàng và một số các cột của ban đầu ma trận $A$ có thể có đã được permuted do lựa chọn của các phân hoạch $S = S_{1} \cup \cdots  \cup S_{m}$ và $T = T_{1} \cup \cdots  \cup T_{n}$; xem

> **Ví dụ 6.3.** Ta propose đến ký hiệu ma trận khối (block matrix) $(A_{ij})_{1\le i\le m,1\le j\le n}$ bởi $[A]$. Điều này là không hoàn toàn satisfactory vì tất cả information về các phân hoạch của $S$ và $T$ là lost, nhưng ít nhất điều này cho phép chúng ta đến distinguish giữa $A$ và ma trận khối (block matrix) phát sinh từ $A$. là hoàn toàn chặt chẽ ta có thể tiến hành như sau. Cho $[m] = {1, \dots  , m}$ và $[n] = {1, \dots  , n}$.

> **Định nghĩa 6.9.** Với mọi hai hữu hạn các tập hợp của các chỉ số $S$ và $T$, một ma trận cỡ $S \times  T$ $A$ là $S \times$ T-họ có chỉ số (indexed family) với các giá trị trong $K$, nghĩa là, hàm
$$A: S \times  T \to K.$$
Ký hiệu không gian của $S \times  T$ các ma trận với các phần tử (entries) trong $K$ bởi $M_{S,T}(K)$. một ma trận cỡ $S \times T$ $A$ là $S \times$ T-họ có chỉ số (indexed family) $(a_{st})_{(s,t)\in S\times T}$, nhưng tiêu chuẩn biểu diễn của ma trận bởi rectangular mảng (array) của các vô hướng là không khá đúng bởi vì nó giả sử rằng các hàng được chỉ số bởi các chỉ số trong “chính tắc chỉ số tập hợp” $[m]$ và rằng các cột được chỉ số bởi các chỉ số trong “chính tắc chỉ số tập hợp” $[n]$. Cũng chỉ số các tập hợp cần không được thứ tự, nhưng trong thực tế chúng là, do đó nếu $S = {s_{1}, \dots  , s_{m}}$ và $T = {t_{1}, \dots  , t_{n}}$, ta ký hiệu một ma trận cỡ $S \times  T$ $A$ bởi rectangular mảng (array)
$$A = \begin{pmatrix} a_{s1t1} & \cdots & a_{s1tn} \\ \vdots & \ddots & \vdots \\ a_{smt1} & \cdots & a_{smtn} \end{pmatrix} .$$
Chẵn/ngay cả nếu chỉ số các tập hợp là không được thứ tự, tích của một ma trận cỡ $R\times S$ $A$ và của một ma trận cỡ $S \times T$ $B$ được xác định tốt (well-defined) và $C = AB$ là một ma trận cỡ $R \times  T$ (ở đâu $R, S, T$ là hữu hạn chỉ số các tập hợp); xem Mệnh đề 6.13. Thì $m \times  n$ ma trận khối (block matrix) $X$ được cảm sinh bởi hai các phân hoạch $S = S_{1} \cup \cdots  \cup S_{m}$ và $T = T_{1} \cup \cdots  \cup T_{n}$ là $[m] \times$ [n]-họ có chỉ số (indexed family)
$$X : [m] \times  [n] \to \prod_{)\in[m]\times}  M_{Si,Tj}(K),$$
$$(i,j[n]$$
Sao cho X(i, $j) \in M_{Si,Tj}(K)$, mà có nghĩa là X(i, $j)$ là một ma trận cỡ $S_{i} \times  T_{j}$ với các phần tử (entries) trong $K$. ánh xạ $X$ cũng định nghĩa ma trận cỡ $M \times  N$ $A = (a_{st})_{s\in S,t\in T}$, với
$$a_{st} = X(i, j)_{st},$$

<!-- PAGE 196 -->
Với mọi $s \in S_{i}$ và bất kỳ $j \in T_{j}$, do đó thực ra $X = [A]$ và X(i, $j) = A_{Si,Tj}$. Nhưng nhớ rằng ta abbreviate X(i, $j)$ như $X_{ij}$, do đó $(i$, j)th phần tử (entry) trong ma trận khối (block matrix) $[A]$ của $A$ liên kết với các phân hoạch $S = S_{1} \cup \cdots  \cup S_{m}$ và $T = T_{1} \cup \cdots  \cup T_{n}$ nên được ký hiệu bởi $[A]_{ij}$. để cực tiểu hóa ký hiệu ta sẽ sử dụng đơn giản hơn ký hiệu $A_{ij}$. Schematically ta biểu diễn ma trận khối (block matrix) $[A]$ như
$$[A] = \begin{pmatrix} A_{S1,T1} & \cdots & A_{S1,Tn} \\ \vdots & \ddots & \vdots \\ A_{Sm,T1} & \cdots & A_{Sm,Tn} \end{pmatrix} or simply as[A] = \begin{pmatrix} A_{11} & \cdots & A_{1n} \\ \vdots & \ddots & \vdots \\ A_{m1} & \cdots & A_{mn} \end{pmatrix} .$$
Trong được đơn giản hóa ký hiệu ta lose information về chỉ số các tập hợp của các khối.
Nhận xét: Nó là dễ để kiểm tra rằng tập hợp của $m \times  n$ các ma trận khối được cảm sinh bởi hai các phân hoạch $S = S_{1} \cup \cdots  \cup S_{m}$ và $T = T_{1} \cup \cdots  \cup T_{n}$ là không gian vectơ (vector space). Thực ra, nó là đẳng cấu đến tổng trực tiếp (direct sum)
$$MM_{Si,Tj}(K).$$
$$(i,j)\in [m]\times [n]$$
Phép cộng và rescaling là performed blockwise.

> **Ví dụ 6.2.** Cho $S = {1, 2, 3, 4, 5, 6}$, với $S_{1} = {1, 2}, S_{2} = {3}, S_{3} = {4, 5, 6}$, và $T = {1, 2, 3, 4, 5}$, với $T_{1} = {1, 2}, T_{2} = {3, 4}, T_{3} = {5}$, và Thì $s_{1} = 2, s_{2} = 1, s_{3} = 3$ và $t_{1} = 2, t_{2} = 2, t_{3} = 1$. ban đầu ma trận là một ma trận cỡ $6 \times  5$ $A = (a_{ij})$. Schematically ta thu được một ma trận cỡ $3 \times  3$ của chín các khối. ở đâu $A_{11}, A_{12}, A_{13}$ là respectively $2 \times  2, 2 \times  2$ và $2 \times  1, A_{21}, A_{22}, A_{23}$ là respectively $1 \times  2, 1 \times  2$ và $1 \times  1$, và $A_{31}, A_{32}, A_{33}$ là respectively $3 \times  2, 3 \times  2$ và $3 \times  1$, như được minh họa ở dưới.
$$[A] = \begin{pmatrix} A_{11} & A_{12} & A_{13} \\ A_{21} & A_{22} & A_{23} \\ A_{31} & A_{32} & A_{33} \end{pmatrix} = \begin{pmatrix} a_{11} & a_{12} & a_{13} & a_{14} & a_{15} \\ a_{21} & a_{22} & a_{23} & a_{24} & a_{25} \\ a_{31} & a_{32} & a_{33} & a_{34} & a_{35} \\ a_{41} & a_{42} & a_{43} & a_{44} & a_{45} \\ a_{51} & a_{52} & a_{53} & a_{54} & a_{55} \\ a_{61} & a_{62} & a_{63} & a_{64} & a_{65} \end{pmatrix} .$$
Technically, các khối là thu được từ $A$ theo các tập con $S_{i}, T_{j}$. Ví dụ,
$$a_{13}a_{14}$$
$$A_{12} = A_{{1,2},{3,4}} =.$$
$$a_{23}a_{24}$$

> **Ví dụ 6.3.** Cho $S = {1, 2, 3}$, với $S_{1} = {1, 3}, S_{2} = {2}$, và $T = {1, 2, 3}$, với $T_{1} = {1, 3}, T_{2} = {2}$. Thì $s_{1} = 2, s_{2} = 1$, và $t_{1} = 2, t_{2} = 1$. khối $2 \times  2$ ma trận $[A]$ liên kết với ở trên các phân hoạch là
$$[A] = \begin{pmatrix} A_{{1,3},{1,3}} & A_{{1,3},{2}} \\ A_{{2},{1,3}} & A_{{2},{2}} \end{pmatrix} = \begin{pmatrix} a_{11} & a_{13} & a_{12} \\ a_{31} & a_{33} & a_{32} \\ a_{21} & a_{23} & a_{22} \end{pmatrix} .$$
$$\begin{bmatrix}\end{bmatrix} \begin{bmatrix}\end{bmatrix}$$

<!-- PAGE 197 -->
Nhận thấy rằng $[A]$ được quan điểm như $3 \times  3$ vô hướng (scalar) ma trận là một cách xác định khác nhau từ
$$A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} .$$
Trong thực tế, $S = {1, \dots  , M}$ và $T = {1, \dots  , N}$, do đó có các song ánh $\alpha_{i}$: ${1, \dots  , s_{i}} \to S_{i}$ và $\beta_{j}$: ${1, \dots  , t_{j}} \to T_{j}, 1 \le i \le m, 1 \le j \le n$. Mỗi $s_{i} \times  t_{j}$ ma trận $A_{Si,Tj}$ được xét như ma trận con của $A$, điều này là tại sao các hàng được chỉ số bởi $S_{i}$ và các cột được chỉ số bởi
$$T_{j}, but this matrix can also be viewed as an s_{i} \times  t_{j} matrix A_{ij}' = \begin{pmatrix} (a_{ij}')_{st} \\ },with \end{pmatrix} by itself, with the$$
Các hàng được chỉ số bởi ${1, \dots  , s_{i}}$ và các cột được chỉ số bởi ${1, \dots  , t_{j}$
$$(a_{ij}')_{st} = a_{\alpha(s)\beta(t)},1 \le s \le s_{i}, 1 \le t \le t_{j}.$$
Symbolic các hệ like Matlab có commands để xây dựng như vậy các ma trận. Nhưng là careful rằng đến đặt ma trận chẳng hạn như $A_{ij}'$ quay lại vào $A$ tại đúng hàng và cột locations đòi hỏi quan điểm ma trận này như $A_{Si,Tj}$. Symbolic các hệ like Matlab cũng có commands đến assign các vectơ hàng và các vectơ cột đến cụ thể các hàng hoặc các cột của ma trận. Technically, là hoàn toàn chặt chẽ, các ma trận $A_{Si,Tj}$ và $A_{ij}'$ là khác nhau, chẵn/ngay cả dù chúng chứa cùng các phần tử (entries). lý do chúng là khác nhau là rằng trong $A_{Si,Tj}$ các phần tử (entries) được chỉ số bởi chỉ số các tập hợp $S_{i}$ và $T_{j}$, nhưng trong $A_{ij}'$ chúng được chỉ số bởi chỉ số các tập hợp ${1, \dots  , s_{i}}$ và ${1, \dots  , t_{j}}$. Điều này phụ thuộc liệu ta quan điểm $A_{Si,Tj}$ như ma trận con của $A$ hoặc như ma trận trên của nó own. Trong hầu hết các trường hợp, các phân hoạch $S = S_{1} \cup \cdots  \cup S_{m}$ và $T = T_{1} \cup \cdots  \cup T_{n}$ được chọn sao cho
$$S_{i} = {s | s_{1} + \cdots  + s_{i-1} + 1 \le s \le s_{1} + \cdots  + s_{i}}$$
$$T_{j} = {t | t_{1} + \cdots  + t_{i-1} + 1 \le t \le t_{1} + \cdots  + t_{j}},$$
Với $s_{i} = |S_{i}| \ge 1, t_{j} = |T_{j}| \ge 1, 1 \le i \le m, 1 \le j \le n$. Cho $i = 1$, ta có $S_{1} = {1, \dots  , s_{1}}$ và $T_{1} = {1, \dots  , t_{1}}$. Điều này có nghĩa là ta phân hoạch vào liên tiếp các tập con của liên tiếp các số nguyên và ta bảo toàn thứ tự của các cơ sở. Trong trường hợp này, $[A]$ có thể được được quan điểm như $A$. Nhưng các kết quả về khối phép nhân đúng trong tổng quát trường hợp. Cuối cùng ta tackle khối phép nhân. Nhưng thứ nhất ta nhận thấy rằng phép tính được tạo trong Mục 4.2 có thể được ngay lập tức được điều chỉnh đến các ma trận được chỉ số bởi tùy ý hữu hạn chỉ số các tập hợp I, $J, K$, không cần của tạo thành ${1, \dots  , p}, {1, \dots  , n}, {1, \dots  , m}$. Ta cần điều này đến deal với các tích của các ma trận xảy ra như các khối trong khác các ma trận, vì như vậy các ma trận là của tạo thành $A_{Si,Tj}$, etc. Ta có thể chứng minh ngay lập tức kết quả sau đây generalizing Phương trình $(4)$ được chứng minh trong Mục 4.2 (cũng xem thứ tư phương trình của Mệnh đề 4.2).

> **Mệnh đề 6.13.** Cho I, $J, K$ là bất kỳ khác rỗng hữu hạn chỉ số các tập hợp. Nếu I $\times  J$ ma trận $A = (a_{ij})_{(i,j)\in I\times J}$ biểu diễn ánh xạ tuyến tính (linear map) $g: F \to G$ đối với cơ sở (basis) $(v_{j})_{j\in J}$ của $F$ và cơ sở (basis) $(w_{i})_{i\in I}$ của $G$ và nếu ma trận cỡ $J \times  K$ $B = (b_{jk})_{(j,k)\in J\times K}$ biểu diễn ánh xạ tuyến tính (linear map) $f$: $E \to F$ đối với cơ sở (basis) $(u_{k})_{k\in K}$ của $E$ và cơ sở (basis) $(v_{j})_{j\in J}$ của $F$, thì

<!-- PAGE 198 -->
I $\times  K$ ma trận $C = (c_{ik})_{(i,k)\in I\times K}$ biểu diễn ánh xạ tuyến tính (linear map) $g \circ f$: $E \to G$ đối với cơ sở (basis) $(u_{k})_{k\in K}$ của $E$ và cơ sở (basis) $(w_{i})_{i\in I}$ của $G$ được cho bởi
$$C = AB,$$
Ở đâu với mọi $i \in$ I và tất cả $k \in K$,
$$c_{ik} = \sum_{j\in J}  a_{ij}b_{jk}.$$
Cho $E, F, G$ là ba các không gian vectơ được biểu diễn như các tổng trực tiếp
$$pnm$$
$$E =ME_{k},F =MF_{j},G =MG_{i},$$
$$k=1j=1i=1$$
Và cho $f$: $E \to F$ và $g: F \to G$ là hai các ánh xạ tuyến tính (linear maps). Hơn nữa, giả sử rằng $E$ có hữu hạn cơ sở (basis) $(u_{t})_{t\in T}$, ở đâu $T$ là rời nhau hợp $T = T_{1} \cup \cdots  \cup T_{p}$ của khác rỗng các tập con $T_{k}$ sao cho $(u_{t})_{t\in Tk}$ là cơ sở (basis) của $E_{k}, F$ có hữu hạn cơ sở (basis) $(v_{s})_{s\in S}$, ở đâu $S$ là rời nhau hợp $S = S_{1} \cup \cdots  \cup S_{n}$ của khác rỗng các tập con $S_{j}$ sao cho $(v_{s})_{s\in Sj}$ là cơ sở (basis) của $F_{j}$, và $G$ có hữu hạn cơ sở (basis) $(w_{r})_{r\in R}$, ở đâu $R$ là rời nhau hợp $R = R_{1} \cup \cdots  \cup R_{m}$ của khác rỗng các tập con $R_{i}$ sao cho $(w_{r})_{r\in Ri}$ là cơ sở (basis) của $G_{i}$. Cũng cho $M =$ |R|, $N =$ |S|, $P =$ |T|, $r_{i} = |R_{i}|, s_{j} = |S_{j}|, t_{k} = |T_{k}|$, sao cho $M =$ dim(G) $= r_{1} + \cdots  + r_{m}, N =$ dim(F) $= s_{1} + \cdots  + s_{n}$, và $P =$ dim(E) $= t_{1} + \cdots  + t_{p}$. Cho $B$ là ma trận cỡ $N \times  P$ biểu diễn $f$ đối với cơ sở (basis) $(u_{t})_{t\in T}$ của $E$ và cơ sở (basis) $(v_{s})_{s\in S}$ của $F$, cho $A$ là ma trận cỡ $M \times N$ biểu diễn $g$ đối với cơ sở (basis) $(v_{s})_{s\in S}$ của $F$ và cơ sở (basis) $(w_{r})_{r\in R}$ của $G$, và cho $C$ là ma trận cỡ $M \times  P$ biểu diễn $h = g \circ f$ đối với cơ sở (basis) cơ sở (basis) $(u_{t})_{t\in T}$ của $E$ và cơ sở (basis) $(w_{r})_{r\in R}$ của $G$. ma trận $[A]$ là $m \times  n$ ma trận khối (block matrix) của $r_{i} \times  s_{j}$ các ma trận $A_{ij} (1 \le i \le m, 1 \le j \le n)$, ma trận $[B]$ là $n \times  p$ ma trận khối (block matrix) của $s_{j} \times  t_{k}$ các ma trận $B_{jk} (1 \le j \le n, 1 \le k \le p)$, và ma trận $[C]$ là $m \times  p$ ma trận khối (block matrix) của $r_{i} \times  t_{k}$ các ma trận $C_{ik} (1 \le i \le m, 1 \le k \le p)$. Hơn nữa, là precise, $A_{ij} = A_{Ri,Sj}, B_{jk} = B_{Sj,Tk}$, và $C_{ik} = C_{Ri,Tk}$. Bây giờ nhắc lại rằng ma trận $A_{Ri,Sj}$ biểu diễn ánh xạ tuyến tính (linear map) $g_{ij}$: $F_{j} \to G_{i}$ đối với cơ sở (basis) $(v_{s})_{s\in Sj}$ của $F_{j}$ và cơ sở (basis) $(w_{r})_{r\in Ri}$ của $G_{i}$, ma trận $B_{Sj,Tk}$ biểu diễn ánh xạ tuyến tính (linear map) $f_{jk}$: $E_{k} \to F_{j}$ đối với cơ sở (basis) $(u_{t})_{t\in Tk}$ của $E_{k}$ và cơ sở (basis) $(v_{s})_{s\in Sj}$ của $F_{j}$, và ma trận $C_{Ri,Tk}$ biểu diễn ánh xạ tuyến tính (linear map) $h_{ik}$: $E_{k} \to G_{i}$ đối với cơ sở (basis) $(u_{t})_{t\in Tk}$ của $E_{k}$ và cơ sở (basis) $(w_{r})_{r\in Ri}$ của $G_{i}$. Theo Mệnh đề 6.12, $h_{ik}$ được cho bởi công thức
$$h_{ik} = \sum_{j=1}^{n}  g_{ij} \circ f_{jk},1 \le i \le m, 1 \le k \le p,(*_{5})$$

<!-- PAGE 199 -->
Và vì ma trận $A_{Ri,Sj}$ biểu diễn $g_{ij}$: $F_{j} \to G_{i}$, ma trận $B_{Sj,Tk}$ biểu diễn $f_{jk}$: $E_{k} \to F_{j}$, và ma trận $C_{Ri,Tk}$ biểu diễn $h_{ik}$: $E_{k} \to G_{i}$, do đó $(*_{5})$ suy ra phương trình ma trận
$$C_{ik} = \sum_{j=1}^{n}  A_{ij}B_{jk},1 \le i \le m, 1 \le k \le p,(*_{6})$$
Thiết lập (khi combined với Mệnh đề 6.13) sự kiện rằng $[C] =$ [][B], cụ thể là tích $C = AB$ của các ma trận $A$ và $B$ có thể được performed bởi các khối, bằng cách sử dụng cùng tích công thức trên các ma trận rằng được sử dụng trên các vô hướng. Ta record ở trên sự kiện trong sau đây mệnh đề.

> **Mệnh đề 6.14.** Cho $M, N, P$ là bất kỳ dương các số nguyên, và cho ${1, \dots  , M} = R_{1}\cup \cdots \cup R_{m}, {1, \dots  , N} = S_{1} \cup \cdots  \cup S_{n}$, và ${1, \dots  , P} = T_{1} \cup \cdots  \cup T_{p}$ là bất kỳ các phân hoạch vào khác rỗng các tập con $R_{i}, S_{j}, T_{k}$, và viết $r_{i} = |R_{i}|, s_{j} = |S_{j}|$ và $t_{k} = |T_{k}| (1 \le i \le m, 1 \le j \le n, 1 \le k \le p)$. Cho $A$ là một ma trận cỡ $M \times  N$, cho $[A]$ là tương ứng $m \times  n$ ma trận khối (block matrix) của $r_{i} \times  s_{j}$ các ma trận $A_{ij} (1 \le i \le m, 1 \le j \le n)$, và cho $B$ là một ma trận cỡ $N \times  P$ và $[B]$ là tương ứng $n \times  p$ ma trận khối (block matrix) của $s_{j} \times  t_{k}$ các ma trận $B_{jk} (1 \le j \le n, 1 \le k \le p)$. Thì ma trận cỡ $M \times  P$ $C = AB$ tương ứng với $m \times  p$ ma trận khối (block matrix) $[C]$ của $r_{i} \times  t_{k}$ các ma trận $C_{ik} (1 \le i \le m, 1 \le k \le p)$, và ta có
$$[C] = [A][B],$$
Mà có nghĩa là
$$C_{ik} = \sum_{j=1}^{n}  A_{ij}B_{jk},1 \le i \le m, 1 \le k \le p.$$
Nhận xét: tích $A_{ij}B_{jk}$ của các khối $A_{ij}$ và $B_{jk}$, mà là một cách thực các ma trận $A_{Ri,Sj}$ và $B_{Sj,Tk}$, có thể được được tính bằng cách sử dụng các ma trận $A_{ij}'$ và $B_{jk}'$ (được thảo luận sau Ví dụ 6.3) rằng được chỉ số bởi “chính tắc” chỉ số các tập hợp ${1, \dots  , r_{i}}, {1, \dots  , s_{j}}$ và ${1, \dots  , t_{k}}$. Nhưng sau việc tính toán $A_{ij}'B_{jk}'$, ta có đến remember đến insert nó như khối trong $[C]$ bằng cách sử dụng đúng chỉ số các tập hợp $R_{i}$ và $T_{k}$. Điều này là dễ dàng đạt được trong Matlab.

> **Ví dụ 6.4.** Xét phân hoạch của chỉ số tập hợp $R = {1, 2, 3, 4, 5, 6}$ cho trước bởi $R_{1} = {1, 2}, R_{2} = {3}, R_{3} = {4, 5, 6}$; của chỉ số tập hợp $S = {1, 2, 3}$ cho trước bởi $S_{1} = {1, 2}, S_{2} = {3}$; và của chỉ số tập hợp $T = {1, 2, 3, 4, 5, 6}$ cho trước bởi $T_{1} = {1}, T_{2} = {2, 3}, T_{3} = {4, 5, 6}$. Cho $[A]$ là $3 \times  2$ ma trận khối (block matrix)
$$[A] = \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \\ A_{31} & A_{32} \end{pmatrix} = \begin{pmatrix}  &  &  \\  &  &  \\  &  &  \\  &  &  \end{pmatrix} \begin{bmatrix}\end{bmatrix} \begin{bmatrix}\end{bmatrix}$$
$$\begin{bmatrix}\end{bmatrix} \begin{bmatrix}\end{bmatrix}$$

<!-- PAGE 200 -->
Ở đâu $A_{11}, A_{12}$ là $2 \times  2, 2 \times  1; A_{21}, A_{22}$ là $1 \times  2, 1 \times  1$; và $A_{31}, A_{32}$ là $3 \times  2, 3 \times  1$, và $[B]$ là $2 \times  3$ ma trận khối (block matrix)
$$[B] = \begin{pmatrix} B_{11} & B_{12} & B_{13} \\ B_{21} & B_{22} & B_{23} \end{pmatrix} = \begin{pmatrix}  &  &  &  &  \\  &  &  &  &  \end{pmatrix} ,$$
$$\begin{bmatrix}\end{bmatrix} \begin{bmatrix}\end{bmatrix} \begin{bmatrix}\end{bmatrix}$$
Ở đâu $B_{11}, B_{12}, B_{13}$ là $2 \times  1, 2 \times  2, 2 \times  3$; và $B_{21}, B_{22}, B_{23}$ là $1 \times  1, 1 \times  2, 1 \times  3$. Thì $[C] =$ [][B] là $3 \times  3$ ma trận khối (block matrix)
$$[C] = \begin{pmatrix} C_{11} & C_{12} & C_{13} \\ C_{21} & C_{22} & C_{23} \\ C_{31} & C_{32} & C_{33} \end{pmatrix} = \begin{pmatrix}  &  &  &  &  \\  &  &  &  &  \\  &  &  &  &  \\  &  &  &  &  \end{pmatrix} \begin{bmatrix}\end{bmatrix} \begin{bmatrix}\end{bmatrix} \begin{bmatrix}\end{bmatrix} ,$$
$$\begin{bmatrix}\end{bmatrix} \begin{bmatrix}\end{bmatrix} \begin{bmatrix}\end{bmatrix}$$
Ở đâu $C_{11}, C_{12}, C_{13}$ là $2\times 1, 2\times 2, 2\times 3; C_{21}, C_{22}, C_{23}$ là $1\times 1, 1\times 2, 1\times 3$; và $C_{31}, C_{32}, C_{33}$ là $3 \times  1, 3 \times  2, 3 \times  3$. Ví dụ,
$$C_{32} = A_{31}B_{12} + A_{32}B_{22}.$$

> **Ví dụ 6.5.** ví dụ này minh họa một số của subtleties có đến thực hiện với phân hoạch của chỉ số các tập hợp. Xét ma trận cỡ $1 \times  3$
$$A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \end{pmatrix}$$
Và ma trận cỡ $3 \times  2$
$$B = \begin{pmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \\ b_{31} & b_{32} \end{pmatrix} .$$
Xét phân hoạch của chỉ số tập hợp $R = {1}$ cho trước bởi $R_{1} = {1}$; của chỉ số tập hợp $S = {1, 2, 3}$ cho trước bởi $S_{1} = {1, 3}, S_{2} = {2}$; và của chỉ số tập hợp $T = {1, 2}$ cho trước bởi $T_{1} = {2}, T_{2} = {1}$. tương ứng các ma trận khối là $1 \times  2$ ma trận khối (block matrix)
$$[A] = \begin{pmatrix} A_{{1},{1,3}} & A_{{1},{2}} \end{pmatrix} = \begin{pmatrix} a_{11} & a_{13} \end{pmatrix} \begin{bmatrix} a_{12} \end{bmatrix} \begin{bmatrix}\end{bmatrix} ,$$
Và $2 \times  2$ ma trận khối (block matrix)
$$[B] = \begin{pmatrix} B_{{1,3},{2}} & B_{{1,3},{1}} \\ B_{{2},{2}} & B_{{2},{1}} \end{pmatrix} = \begin{pmatrix} b_{12} & b_{11} \\ b_{32} & b_{31} \\ b_{22} & b_{21} \end{pmatrix} .$$
$$\begin{bmatrix}\end{bmatrix} \begin{bmatrix}\end{bmatrix}$$

<!-- PAGE 201 -->
Tích của $1 \times  2$ ma trận khối (block matrix) $[A]$ và $2 \times  2$ ma trận khối (block matrix) $[B]$ là $1 \times  2$ ma trận khối (block matrix) $[C]$ cho trước bởi
$$[C] = [A][B] = \begin{pmatrix} a_{11} & a_{13} \end{pmatrix} \begin{bmatrix} a_{12} \end{bmatrix} \begin{bmatrix}\end{bmatrix} \begin{pmatrix} b_{12} & b_{11} \\ b_{32} & b_{31} \\ b_{22} & b_{21} \end{pmatrix}$$
$$\begin{bmatrix}\end{bmatrix} \begin{bmatrix}\end{bmatrix}$$
$$= \begin{pmatrix}  & b_{12} & b_{11} \\ a_{11} & a_{13} b_{32} & +a_{12}b_{22} & a_{11} & a_{13} b_{31} & +a_{12}b_{21} \\ a_{11}b_{12} + a_{13}b_{32} + a_{12}b_{22} & a_{11}b_{11} + a_{13}b_{31} + a_{12}b_{21} \end{pmatrix} \begin{bmatrix}\end{bmatrix} \begin{bmatrix}\end{bmatrix} \begin{bmatrix}\end{bmatrix} \begin{bmatrix}\end{bmatrix} \begin{bmatrix}\end{bmatrix} \begin{bmatrix}\end{bmatrix}$$
$$= \begin{pmatrix} a_{11}b_{12} + a_{12}b_{22} + a_{13}b_{32} \end{pmatrix} \begin{bmatrix} a_{11}b_{11} + a_{12}b_{21} + a_{13}b_{31} \end{bmatrix} \begin{bmatrix}\end{bmatrix}$$
$$= \begin{pmatrix}\end{pmatrix} \begin{bmatrix}\end{bmatrix} \begin{bmatrix}\end{bmatrix} .$$
Ma trận khối (block matrix) $[C]$ là thu được từ ma trận cỡ $1 \times  2$ $C = AB$ bằng cách sử dụng các phân hoạch của $R = {1}$ cho trước bởi $R_{1} = {1}$ và của $T = {1, 2}$ cho trước bởi $T_{1} = {2}, T_{2} = {1}$, do đó
$$[C] = \begin{pmatrix} C_{{1},{2}} & C_{{1},{1}} \end{pmatrix} ,$$
Mà có nghĩa là $[C]$ là thu được từ $C$ bởi hoán vị của nó hai các cột. Vì
$$C = AB = \begin{pmatrix} a_{11} & a_{12} & a_{13} \end{pmatrix} \begin{pmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \\ b_{31} & b_{32} \end{pmatrix}$$
$$= \begin{pmatrix} a_{11}b_{11} + a_{12}b_{21} + a_{13}b_{31} & a_{11}b_{12} + a_{12}b_{22} + a_{13}b_{32} \end{pmatrix} ,$$
Ta có confirmed rằng $[C]$ là đúng.

> **Ví dụ 6.6.** Ma trận khối phép nhân là rất effective phương pháp để chứng minh rằng nếu tam giác trên (upper-triangular) ma trận $A$ là khả nghịch, thì nghịch đảo của nó là cũng tam giác trên (upper-triangular). Ta tiến hành bằng quy nạp theo dimensiopn $n$ của $A$. Nếu $n = 1$, thì $A = (a)$, ở đâu là vô hướng (scalar), do đó $A$ là khả nghịch khi và chỉ khi $a \neq  0$, và $A^{-1} = (a^{-1})$, mà là một cách tầm thường tam giác trên (upper-triangular). Cho quy nạp bước ta có thể viết $(n + 1) \times  (n + 1)$ tam giác trên (upper triangular) ma trận $A$ trong khối tạo thành như
$$A = \begin{pmatrix} T & U \\ 0_{1,n} & \alpha \end{pmatrix} ,$$
Ở đâu $T$ là $n \times  n$ tam giác trên (upper triangular) ma trận, $U$ là một ma trận cỡ $n \times  1$ và $\alpha  \in \mathbb{R}$. Giả sử rằng $A$ là khả nghịch và cho $B$ là nghịch đảo của nó, được viết trong khối tạo thành như
$$B = \begin{pmatrix} C & V \\ W & \beta \end{pmatrix} ,$$
Ở đâu $C$ là một ma trận cỡ $n \times  n$, $V$ là một ma trận cỡ $n \times  1$, $W$ là một ma trận cỡ $1 \times  n$, và $\beta  \in \mathbb{R}$. Vì $B$ là nghịch đảo của $A$, ta có $AB = I_{n+1}$, mà cho ta
$$\begin{pmatrix} T & U \\ 0_{1,n-1} & \alpha \end{pmatrix} \begin{pmatrix} C & V \\ W & \beta \end{pmatrix} = \begin{pmatrix} I_{n} & 0_{n,1} \\ 0_{1,n} & 1 \end{pmatrix} .$$
