# Định nghĩa của Định thức (determinant)


<!-- PAGE 227 -->
Là thực ra giá trị của định thức (determinant) của $A$ (mà, như ta sẽ xem một cách ngắn, là cũng bằng định thức (determinant) của $A^{\top})$. Tuy nhiên, làm việc một cách trực tiếp với ở trên định nghĩa là khá awkward, và ta sẽ tiến hành thông qua slightly indirect route
Nhận xét: độc giả có thể có đã được puzzled bởi sự kiện rằng nó là chuyển vị (transpose) ma trận $A^{\top}$ thay vì $A$ chính nó rằng xuất hiện trong Bổ đề 7.4. lý do là rằng nếu ta muốn generic số hạng trong định thức (determinant) là
$$\epsilon (\pi )a_{\pi(1) 1} \cdots  a_{\pi(n)n},$$
Ở đâu hoán vị áp dụng đến chỉ số thứ nhất, thì ta có đến biểu diễn $v_{j}s$ theo $u_{i}s$ theo $A^{\top}$ như ta đã thực hiện. Hơn nữa, vì
$$v_{j} = a_{1j}u_{1} + \cdots  + a_{i j}u_{i} + \cdots  + a_{n j}u_{n},$$
Ta xem rằng $v_{j}$ tương ứng với cột thứ $j$ của ma trận $A$, và do đó định thức (determinant) được quan điểm như hàm của các cột của $A$. literature là split trên điều này điểm. Một số các tác giả ưu tiên để định nghĩa định thức (determinant) như ta đã thực hiện. Những cái khác sử dụng $A$ chính nó, mà tương đương với đến quan điểm det như hàm của các hàng, trong mà trường hợp ta thu được biểu thức
$$\sum_{\sigma\in Sn}  \epsilon (\sigma )a_{1\sigma(1)} \cdots  a_{n \sigma(n)}.$$
Hệ quả 7.7 chỉ ra rằng các phần tử này hai các biểu thức là bằng nhau, do đó nó không’t matter mà được chọn. Điều này là matter của taste.

## 7.3 Định nghĩa của Định thức (determinant)

Nhắc lại rằng tập hợp tất cả square các ma trận cỡ $n \times n$ với các hệ số trong trường $K$ được ký hiệu bởi $M_{n}(K)$.

> **Định nghĩa 7.4.** định thức (determinant) được định nghĩa như bất kỳ ánh xạ
$$D: M_{n}(K) \to K,$$
Mà, khi được quan điểm như ánh xạ trên $(K^{n})^{n}$, i.e., ánh xạ của $n$ các cột của ma trận, là $n$-tuyến tính thay phiên và sao cho $D(I_{n}) = 1$ cho ma trận đơn vị (identity matrix) $I_{n}$. Tương đương, ta có thể xét không gian vectơ (vector space) $E$ có số chiều $n$, một số cố định cơ sở (basis) $(e_{1}, \dots  , e_{n})$, và định nghĩa
$$D: E^{n}\to K$$
Như $n$-tuyến tính thay phiên ánh xạ sao cho $D(e_{1}, \dots  , e_{n}) = 1$.

<!-- PAGE 228 -->
Thứ nhất ta sẽ chỉ ra rằng như vậy các ánh xạ $D$ tồn tại, bằng cách sử dụng quy nạp định nghĩa rằng cũng cho đệ quy phương pháp cho việc tính toán các định thức. Thực sự, ta sẽ định nghĩa họ $(\mathcal{D}_{n})_{n\ge1}$ của (hữu hạn) các tập hợp của các ánh xạ $D: M_{n}(K) \to K$. Thứ hai ta sẽ chỉ ra rằng các định thức là thực ra một cách duy nhất được định nghĩa, nghĩa là, ta sẽ chỉ ra rằng $each\mathcal{D}_{n}$ bao gồm của đơn lẻ ánh xạ. Điều này sẽ chỉ ra equivalence của trực tiếp định nghĩa det() của Bổ đề 7.4 với quy nạp định nghĩa D(). Cuối cùng, ta sẽ chứng minh một số cơ bản các tính chất của các định thức, bằng cách sử dụng tính duy nhất định lý. Cho trước ma trận $A \in M_{n}(K)$, ta ký hiệu của nó $n$ các cột bởi $A^{1}, \dots  , A^{n}$. Trong thứ tự đến mô tả đệ quy process để định nghĩa định thức (determinant) ta cần khái niệm của định thức con (minor).

> **Định nghĩa 7.5.** Cho trước bất kỳ ma trận cỡ $n\times n$ với $n \ge 2$, với mọi hai các chỉ số $i, j$ với $1 \le i, j \le n$, cho $A_{ij}$ là $(n$ - $1) \times  (n$ - $1)$ ma trận thu được bởi xóa Hàng $i$ và Cột $j$ từ $A$ và được gọi là định thức con (minor):
$$A_{ij} = \begin{pmatrix} \times \\ \times \\ \times & \times & \times & \times & \times & \times & \times \\ \times \\ \times \\ \times \end{pmatrix} .$$
$$\times$$
Ví dụ, nếu
$$A = \begin{pmatrix} 2 & -1 & 0 & 0 & 0 \\ -1 & 2 & -1 & 0 & 0 \\ 0 & -1 & 2 & -1 & 0 \\ 0 & 0 & -1 & 2 & -1 \\ 0 & 0 & 0 & 1 & 2 \end{pmatrix}$$
$$-$$
Thì
$$A_{2 3} = \begin{pmatrix} 2 & -1 & 0 & 0 \\ 0 & -1 & -1 & 0 \\ 0 & 0 & 2 & -1 \\ 0 & 0 & 1 & 2 \end{pmatrix} .$$
$$-$$

> **Định nghĩa 7.6.** Với mọi $n \ge 1$, ta định nghĩa hữu hạn tập hợp $\mathcal{D}_{n}$ của các ánh xạ $D: M_{n}(K) \to K$ một cách quy nạp như sau: Khi $n = 1, \mathcal{D}_{1}$ bao gồm của đơn lẻ ánh xạ $D$ sao cho, D() $= a$, ở đâu $A = (a)$, với $a \in K$. Giả sử rằng $\mathcal{D}_{n-1}$ có đã được được định nghĩa, ở đâu $n \ge 2$. Thì $\mathcal{D}_{n}$ bao gồm của tất cả các ánh xạ $D$ sao cho, với một số $i, 1 \le i \le n$,
$$D(A) = (-1)^{i+1}a_{i1}D(A_{i1}) + \cdots  + (-1)^{i+n}a_{i n}D(A_{i n}),$$
Ở đâu với mọi $j, 1 \le j \le n, D(A_{i j})$ là kết quả của áp dụng bất kỳ $D$ trong $\mathcal{D}_{n-1}$ đến định thức con (minor) $A_{i j}$.

<!-- PAGE 229 -->
 Ta confess rằng sử dụng của cùng letter $D$ cho member của $\mathcal{D}_{n}$ đang được định nghĩa, và cho members của $\mathcal{D}_{n-1}$, có thể là slightly confusing. Ta được xét bằng cách sử dụng các chỉ số dưới đến distinguish, nhưng điều này dường như đến complicate things unnecessarily. Một nên không worry cũng nhiều anyway, vì nó sẽ turn ra rằng mỗi $\mathcal{D}_{n}$ chứa chỉ một ánh xạ. Mỗi $(-1)^{i+j}D(A_{i j})$ được gọi là phần bù đại số (cofactor) của $a_{i j}$, và quy nạp biểu thức cho D() được gọi là một Laplace expansion của $D$ theo hàng thứ $i$. Cho trước ma trận $A \in M_{n}(K)$, mỗi D() được gọi là một định thức (determinant) của $A$. Ta có thể nghĩ của mỗi member $of\mathcal{D}_{n}$ như thuật toán đến tính giá trị “” định thức (determinant) của $A$. chính điểm là rằng các phần tử này các thuật toán, mà một cách đệ quy tính giá trị định thức (determinant) bằng cách sử dụng tất cả khả dĩ/có thể Laplace hàng expansions, tất cả cho cùng kết quả, det(). Ta sẽ chứng minh một cách ngắn rằng D() là một cách duy nhất được định nghĩa (tại moment, nó là không rõ ràng rằng $\mathcal{D}_{n}$ bao gồm của đơn lẻ ánh xạ). Giả sử sự kiện này, cho trước một ma trận cỡ $n \times n$ $A = (a_{i j})$,
$$A = \begin{pmatrix} a_{1 1} & a_{1 2} & \dots & a_{1n} \\ a_{2 1} & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \dots & a_{n n} \end{pmatrix} ,$$
Định thức (định thức (determinant)) của nó được ký hiệu bởi D() hoặc det(), hoặc nhiều hơn/thêm một cách tường minh bởi
$$a_{1 1}a_{1 2}\dots a_{1n}$$
$$a_{2 1}a_{2 2}\dots a_{2n}$$
$$\det(A) =\vdots \vdots \ddots \vdots .$$
$$a_{n1}a_{n2}\dots a_{n n}$$
Cho chúng ta thứ nhất xét một số các ví dụ.

> **Ví dụ 7.1.** $1$. Khi $n = 2$, nếu
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} ,$$
Thì bởi expanding theo bất kỳ hàng, ta có
$$D(A) = ad -bc.$$
$2$. Khi $n = 3$, nếu
$$A = \begin{pmatrix} a_{1 1} & a_{1 2} & a_{1 3} \\ a_{2 1} & a_{2 2} & a_{2 3} \\ a_{3 1} & a_{3 2} & a_{3 3} \end{pmatrix} ,$$

<!-- PAGE 230 -->
Thì bởi expanding theo hàng thứ nhất, ta có
$$a_{2 2}a_{2 3}



$a_{2 1}a_{2 3}$



$a_{2 1}a_{2 2}$$$
$$D(A) = a_{1 1} -a_{1 2} + a_{1 3} ,$$
$$a_{3 2}a_{3 3}a_{3 1}a_{3 3}a_{3 1}a_{3 2}$$
Rằng là,
$$D(A) = a_{1 1}(a_{2 2}a_{3 3} -a_{3 2}a_{2 3}) -a_{1 2}(a_{2 1}a_{3 3} -a_{3 1}a_{2 3}) + a_{1 3}(a_{2 1}a_{3 2} -a_{3 1}a_{2 2}),$$
Mà cho tường minh công thức
$$D(A) = a_{1 1}a_{2 2}a_{3 3} + a_{2 1}a_{3 2}a_{1 3} + a_{3 1}a_{1 2}a_{2 3} -a_{1 1}a_{3 2}a_{2 3} -a_{2 1}a_{1 2}a_{3 3} -a_{3 1}a_{2 2}a_{1 3}.$$
Ta bây giờ chỉ ra rằng mỗi $D \in D_{n}$ là định thức (determinant) (ánh xạ).

> **Bổ đề 7.5.** Với mọi $n \ge 1$, với mọi $D \in D_{n}$ như đã định nghĩa trong Định nghĩa 7.6, $D$ là ánh xạ đa tuyến tính thay phiên sao cho $D(I_{n}) = 1$.

*Chứng minh.* Bằng quy nạp theo $n$, hiển nhiên là $D(I_{n}) = 1$. Cho chúng ta bây giờ chứng minh rằng $D$ là đa tuyến tính. Cho chúng ta chỉ ra rằng $D$ là tuyến tính trong mỗi cột. Xét bất kỳ Cột $k$. Vì D() $= (-1)^{i+1}a_{i1}D(A_{i1}) + \cdots  + (-1)^{i+j}a_{i j}D(A_{i j}) + \cdots  + (-1)^{i+n}a_{i n}D(A_{i n})$, nếu $j \neq  k$, thì bởi quy nạp, $D(A_{i j})$ là tuyến tính trong Cột $k$, và $a_{i j}$ thực hiện không thuộc đến Cột $k$, do đó $(-1)^{i+j}a_{i j}D(A_{i j})$ là tuyến tính trong Cột $k$. Nếu $j = k$, thì $D(A_{i j})$ không phụ thuộc vào Cột $k = j$, vì $A_{i j}$ là thu được từ $A$ bởi xóa Hàng $i$ và Cột $j = k$, và $a_{i j}$ thuộc đến Cột $j = k$. Do đó, $(-1)^{i+j}a_{i j}D(A_{i j})$ là tuyến tính trong Cột $k$. Hệ quả là, trong tất cả các trường hợp, $(-1)^{i+j}a_{i j}D(A_{i j})$ là tuyến tính trong Cột $k$, và do đó, D() là tuyến tính trong Cột $k$. Cho chúng ta bây giờ chứng minh rằng $D$ là thay phiên. Giả sử rằng hai kề nhau các cột của $A$ là bằng nhau, nói $A^{k} = A^{k+1}$. Giả sử rằng j̸ $= k$ và j̸ $= k + 1$. Thì ma trận $A_{i j}$ có hai đồng nhất kề nhau các cột, và theo giả thiết quy nạp, $D(A_{i j}) = 0$. còn lại các số hạng của D() là
$$(-1)^{i+k}a_{i k}D(A_{i k}) + (-1)^{i+k+1}a_{i k+1}D(A_{i k+1}).$$
Tuy nhiên, hai các ma trận $A_{i k}$ và $A_{i k+1}$ là bằng nhau, vì ta là giả sử rằng Các cột $k$ và $k + 1$ của $A$ là đồng nhất và $A_{i k}$ là thu được từ $A$ bởi xóa Hàng $i$ và Cột $k$ trong khi $A_{i k+1}$ là thu được từ $A$ bởi xóa Hàng $i$ và Cột $k + 1$. Tương tự, $a_{i k} = a_{i k+1}$, vì Các cột $k$ và $k + 1$ của $A$ là bằng nhau. Nhưng khi đó, $(-1)^{i+k}a_{i k}D(A_{i k}) + (-1)^{i+k+1}a_{i k+1}D(A_{i k+1}) = (-1)^{i+k}a_{i k}D(A_{i k})$ - $(-1)^{i+k}a_{i k}D(A_{i k}) = 0$. Điều này chỉ ra rằng $D$ là thay phiên và các đầy đủ chứng minh. Bổ đề 7.5 chỉ ra sự tồn tại của các định thức. Ta bây giờ chứng minh của chúng tính duy nhất.

<!-- PAGE 231 -->

> **Định lý 7.6.** Với mọi $n \ge 1$, với mọi $D \in D_{n}$, với mọi ma trận $A \in M_{n}(K)$, ta có
$$D(A) = \sum_{\pi\in Sn}  \epsilon (\pi )a_{\pi(1) 1} \cdots  a_{\pi(n)n},$$
Ở đâu tổng các miền giá trị (range) trên tất cả các hoán vị $\pi$ trên ${1, \dots  , n}$. Hệ quả là, $\mathcal{D}_{n}$ bao gồm của đơn lẻ ánh xạ với mọi $n \ge 1$, và ánh xạ này được cho bởi ở trên tường minh công thức.

*Chứng minh.* Xét tiêu chuẩn cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $K^{n}$, ở đâu $(e_{i})_{i} = 1$ và $(e_{i})_{j} = 0$, cho j̸ $= i$. Thì mỗi cột $A^{j}$ của $A$ tương ứng với vectơ $v_{j}$ có các tọa độ trên cơ sở (basis) $(e_{1}, \dots  , e_{n})$ là các thành phần của $A^{j}$, nghĩa là, ta có thể viết
$$v_{1} = a_{1 1}e_{1} + \cdots  + a_{n1}e_{n},$$
$$\dots$$
$$v_{n} = a_{1n}e_{1} + \cdots  + a_{n n}e_{n}.$$
Vì theo Bổ đề 7.5, mỗi $D$ là đa tuyến tính thay phiên ánh xạ, bằng cách áp dụng Bổ đề 7.4, ta thu được
$$D(A) = D(v_{1}, \dots  , v_{n}) = \begin{pmatrix} \epsilon (\pi )a_{\pi(1) 1} \cdots  a_{\pi(n)n} \\ \pi \end{pmatrix} \sum_{\in Sn}  D(e_{1}, \dots  , e_{n}),$$
Ở đâu tổng các miền giá trị (range) trên tất cả các hoán vị $\pi$ trên ${1, \dots  , n}$. Nhưng $D(e_{1}, \dots  , e_{n}) = D(I_{n})$, và theo Bổ đề 7.5, ta có $D(I_{n}) = 1$. Do đó,
$$D(A) = \sum_{\pi\in Sn}  \epsilon (\pi )a_{\pi(1) 1} \cdots  a_{\pi(n)n},$$
Ở đâu tổng các miền giá trị (range) trên tất cả các hoán vị $\pi$ trên ${1, \dots  , n}$. Từ bây giờ trên ta sẽ favor ký hiệu det() trên D() cho định thức (determinant) của ma trận vuông (square matrix).
Nhận xét: Có một hình học interpretation của các định thức mà ta tìm khá illuminating. Cho trước $n$ các vectơ độc lập tuyến tính (linearly independent) $(u_{1}, \dots  , u_{n})$ trong $\mathbb{R}^{n}$, tập hợp
$$P_{n} = {\lambda_{1} u_{1} + \cdots  + \lambda_{n} u_{n} | 0 \le \lambda_{i}  \le 1, 1 \le i \le n}$$
Được gọi là một parallelotope. Nếu $n = 2$, thì $P_{2}$ là hình bình hành và nếu $n = 3$, thì $P_{3}$ là parallelepiped, skew hình hộp có $u_{1}, u_{2}, u_{3}$ như ba của của nó góc các vế/cạnh. Xem Các hình 7.1 và 7.2. Thì hóa ra là $det(u_{1}, \dots  , u_{n})$ được dấu thể tích của parallelotope $P_{n}$ (ở đâu thể tích có nghĩa là $n$ chiều thể tích). dấu của điều này thể tích accounts cho định hướng của $P_{n}$ trong $\mathbb{R}^{n}$. Ta có thể bây giờ chứng minh một số các tính chất của các định thức.

<!-- PAGE 232 -->
$$u = (1,1)$$
$$2$$
$$u = (1,0)1$$
$$\mathbb{R}^{w}$$

![Figure 7.1](../../assets/ch07/fig_7_1.png)

**Hình 7.1:** hình bình hành trong được sinh (spanned) bởi các vectơ $u_{1} = (1, 0)$ và $u_{2} = (1, 1)$.

> **Hệ quả 7.7.** Với mọi ma trận $A \in M_{n}(K)$, ta có det() $= det(A^{\top})$.

*Chứng minh.* Theo Định lý 7.6, ta có
$$\det(A) = \sum_{\pi\in Sn}  \epsilon (\pi )a_{\pi(1) 1} \cdots  a_{\pi(n)n},$$
Ở đâu tổng các miền giá trị (range) trên tất cả các hoán vị $\pi$ trên ${1, \dots  , n}$. Vì hoán vị là khả nghịch, mọi tích
$$a_{\pi(1) 1} \cdots  a_{\pi(n)n}$$
Có thể được được viết lại như
$$a_{1\pi-1(1)} \cdots  a_{n \pi-1(n)},$$
Và vì $\epsilon (\pi^{-1}$) $= \epsilon (\pi$) và tổng được lấy trên tất cả các hoán vị trên ${1, \dots  , n}$, ta có
$$\sum_{\pi\in Sn}  \epsilon (\pi )a_{\pi(1) 1} \cdots  a_{\pi(n)n} = \sum_{\sigma\in Sn}  \epsilon (\sigma )a_{1\sigma(1)} \cdots  a_{n \sigma(n)},$$
Ở đâu $\pi$ và $\sigma$ miền giá trị (range) trên tất cả các hoán vị. Nhưng ta kiểm chứng được ngay rằng
$$\det(A^{\top}) = \sum_{\sigma\in Sn}  \epsilon (\sigma )a_{1\sigma(1)} \cdots  a_{n \sigma(n)}.$$
Hữu ích hệ quả của Hệ quả 7.7 là rằng định thức (determinant) của ma trận là cũng đa tuyến tính thay phiên ánh xạ của các hàng của nó. sự kiện này, combined với sự kiện rằng định thức (determinant) của ma trận là đa tuyến tính thay phiên ánh xạ của các cột của nó, là thường hữu ích cho việc tìm short-cuts trong việc tính toán các định thức. Ta minh họa điều này điểm trên sau đây ví dụ mà chỉ ra lên trong đa thức nội suy.

<!-- PAGE 233 -->
$$u = (1,1,1)$$
$$3$$
$$u = (0,1,0)$$
$$2$$
$$u = (1,1,0)$$
$$1$$
$$\mathbb{R}^{3}$$

![Figure 7.2](../../assets/ch07/fig_7_2.png)

**Hình 7.2:** parallelepiped trong được sinh (spanned) bởi các vectơ $u_{1} = (1, 1, 0), u_{2} = (0, 1, 0)$, và $u_{3} = (0, 0, 1)$.

> **Ví dụ 7.2.** Xét so-called Vandermonde định thức (determinant)
$$11\dots 1$$
$$x_{1}x_{2}\dots x_{n}$$
$$V (x_{1}, \dots  , x_{n}) =x_{1}^{2}x_{2}^{2}\dots x_{n}^{2}.$$
$$\vdots \vdots \ddots \vdots$$
$$x_{1}^{n-1}x_{2}^{n-1}\dots x_{n}^{n-1}$$
Ta khẳng định rằng
$$V (x_{1}, \dots  , x_{n}) = \prod_{\le i<j\le}  (x_{j} -x_{i}),$$
$$1n$$
Với $V (x_{1}, \dots  , x_{n}) = 1$, khi $n = 1$. Ta chứng minh nó bằng quy nạp theo $n \ge 1$. trường hợp $n = 1$ là hiển nhiên. Giả sử $n \ge 2$. Ta tiến hành như sau: nhân Hàng $n$ - $1$ bởi $x_{1}$ và trừ nó từ Hàng $n$ (hàng cuối cùng), thì nhân Hàng $n$ - $2$ bởi $x_{1}$ và trừ nó từ Hàng $n$ - $1$, etc, nhân Hàng $i$ - $1$ bởi $x_{1}$ và trừ nó từ hàng $i$, cho đến khi ta đạt tới Hàng $1$. Ta thu được

<!-- PAGE 234 -->
Sau đây định thức (determinant):
$$11\dots 1$$
$$0x_{2} -x_{1}\dots x_{n} -x_{1}$$
$$V (x_{1}, \dots  , x_{n}) =0x_{2}(x_{2} -x_{1})\dots x_{n}(x_{n} -x_{1}).$$
$$\vdots \vdots \ddots \vdots$$
$$0x_{2}^{n-2}(x_{2} -x_{1})\dots x_{n}^{n-2}(x_{n} -x_{1})$$
Bây giờ expanding định thức (định thức (determinant)) này theo cột thứ nhất và bằng cách sử dụng tính đa tuyến tính, ta có thể nhân tử $(x_{i}$ - $x_{1})$ từ cột của chỉ số $i$ - $1$ của ma trận thu được bởi xóa hàng thứ nhất và cột thứ nhất, và do đó
$$V (x_{1}, \dots  , x_{n}) = (x_{2} -x_{1})(x_{3} -x_{1}) \cdots  (x_{n} -x_{1})V (x_{2}, \dots  , x_{n}),$$
Mà các thiết lập quy nạp bước.

> **Ví dụ 7.3.** định thức (determinant) của tam giác trên (upper triangular) các ma trận và tổng quát hơn của các ma trận khối rằng là khối tam giác trên (upper triangular) có đáng chú ý tạo thành. Nhắc lại rằng một ma trận cỡ $n\times n$ $A = (a_{ij})$ là tam giác trên (upper-triangular) nếu nó là của tạo thành
$$A = \begin{pmatrix} a_{11} & \times & \times & \cdots & \times \\ 0 & a_{22} & \times & \cdots & \times \\ 0 & 0 & \ddots & \cdots & \vdots \\ \vdots & \vdots & \ddots & \ddots & \vdots \\ 0 & 0 & 0 & 0 & a_{nn} \end{pmatrix} ,$$
Rằng là, $a_{ij} = 0$ với mọi $i > j, 1 \le i, j \le n$. Bằng cách sử dụng $n$ - $1$ lần Laplace expansion đối với cột thứ nhất ta obain
$$\det(A) = a_{11}a_{22} \cdots  a_{nn}.$$
Tương tự, nếu $A$ là $n \times  n$ ma trận khối (block matrix) mà là khối tam giác trên (upper triangular),
$$A = \begin{pmatrix} A_{11} & \times & \times & \cdots & \times \\ 0 & A_{22} & \times & \cdots & \times \\ 0 & 0 & \ddots & \ddots & \vdots \\ \vdots & \vdots & \ddots & \ddots & \vdots \\ 0 & 0 & 0 & 0 & A_{pp} \end{pmatrix} ,$$
Ở đâu mỗi $A_{ii}$ là một ma trận cỡ $n_{i} \times  n_{i}$, với $n_{1} + \cdots  + n_{p} = n$, mỗi khối $\times$ ở trên đường chéo trong position $(i, j)$ cho $i < j$ là một ma trận cỡ $n_{i} \times  n_{j}$, và mỗi khối trong position $(i, j)$ cho $i > j$ là $n_{i} \times  n_{j}$ không ma trận, thì nó có thể được được hiển thị bằng quy nạp theo $p \ge 1$ rằng
$$\det(A) = \det(A_{11}) \det(A_{22}) \cdots  \det(A_{pp}).$$

<!-- PAGE 235 -->
Bổ đề 7.4 có thể được reformulated một cách đẹp như sau.

> **Mệnh đề 7.8.** Cho $f$: $E \times  \dots  \times  E \to F$ là $n$-tuyến tính thay phiên ánh xạ. Cho $(u_{1}, \dots  , u_{n})$ và $(v_{1}, \dots  , v_{n})$ là hai các họ của $n$ các vectơ, sao cho
$$v_{1} = a_{1 1}u_{1} + \cdots  + a_{1n}u_{n},$$
$$\dots$$
$$v_{n} = a_{n1}u_{1} + \cdots  + a_{n n}u_{n}.$$
Tương đương, đặt
$$A = \begin{pmatrix} a_{1 1} & a_{1 2} & \dots & a_{1n} \\ a_{2 1} & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \dots & a_{n n} \end{pmatrix} ,$$
Giả sử rằng ta có
$$\begin{pmatrix} v_{1} \\ v_{2} \\ \vdots \\ v_{n} \end{pmatrix} = A \begin{pmatrix} u_{1} \\ u_{2} \\ \vdots \\ u_{n} \end{pmatrix} .$$
Thì,
$$f(v_{1}, \dots  , v_{n}) = \det(A)f(u_{1}, \dots  , u_{n}).$$

*Chứng minh.* chỉ difference với Bổ đề 7.4 là rằng ở đây ta là bằng cách sử dụng $A^{\top}$ thay vì của $A$. Do đó, theo Bổ đề 7.4 và Hệ quả 7.7, ta thu được mong muốn kết quả. Hệ quả là, ta thu được rất hữu ích tính chất rằng định thức (determinant) của tích của các ma trận là tích của các định thức của các ma trận này.

> **Mệnh đề 7.9.** Với mọi hai các ma trận cỡ $n\times n$ $A$ và $B$, ta có det(AB) $=$ det() det(B).

*Chứng minh.* Ta sử dụng Mệnh đề 7.8 như sau: cho $(e_{1}, \dots  , e_{n})$ là tiêu chuẩn cơ sở (basis) của $K^{n}$, và cho
$$\begin{pmatrix} w_{1} \\ w_{2} \\ \vdots \\ w_{n} \end{pmatrix} = AB \begin{pmatrix} e_{1} \\ e_{2} \\ \vdots \\ e_{n} \end{pmatrix} .$$
Thì ta thu được
$$\det(w_{1}, \dots  , w_{n}) = \det(AB) \det(e_{1}, \dots  , e_{n}) = \det(AB),$$
