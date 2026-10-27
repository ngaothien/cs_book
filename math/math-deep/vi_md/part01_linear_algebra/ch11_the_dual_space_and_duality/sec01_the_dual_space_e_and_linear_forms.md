# Không gian đối ngẫu (dual space) E* và Các dạng tuyến tính


<!-- PAGE 415 -->
Chương $11$ Không gian đối ngẫu (dual space) và Đối ngẫu Trong chương này tất cả các không gian vectơ được định nghĩa trên tùy ý trường $K$. Cho sake của concreteness, độc giả có thể safely giả sử rằng $K =\mathbb{R}$.

## 11.1 Không gian đối ngẫu (dual space) E* và Các dạng tuyến tính

Trong Mục 3.9 ta được định nghĩa các dạng tuyến tính, không gian đối ngẫu (dual space) $E^{*} =$ Hom(E, $K)$ của không gian vectơ (vector space) $E$, và đã chỉ ra sự tồn tại của đối ngẫu (dual) các cơ sở cho các không gian vectơ của hữu hạn số chiều. Trong chương này ta lấy deeper nhìn tại connection giữa không gian $E$ và đối ngẫu (đối ngẫu (dual)) của nó không gian $E^{*}$. Như ta sẽ xem một cách ngắn, mọi ánh xạ tuyến tính (linear map) $f$: $E \to F$ cho rise đến ánh xạ tuyến tính (linear map) $f^{\top}$: $F^{*} \to E^{*}$, và hóa ra là trong phù hợp cơ sở (basis), ma trận của $f^{\top}$ là chuyển vị (transpose) của ma trận của $f$. Do đó, khái niệm của không gian đối ngẫu (dual space) cung cấp conceptual explanation của phenomena liên kết với phép chuyển vị. Nhưng nó thực hiện nhiều hơn/thêm, bởi vì nó cho phép chúng ta đến quan điểm phương trình tuyến tính như phần tử của không gian đối ngẫu (dual space) $E^{*}$, và do đó đến quan điểm các không gian con của $E$ như các nghiệm của các tập hợp của các phương trình tuyến tính và vice-versa. relationship giữa các không gian con và các tập hợp của các dạng tuyến tính là essence của đối ngẫu, số hạng mà là thường được sử dụng loosely, nhưng có thể được được tạo precise như song ánh giữa tập hợp của các không gian con của cho trước không gian vectơ (vector space) $E$ và tập hợp của các không gian con của của nó đối ngẫu (dual) $E^{*}$. Trong điều này correspondence, không gian con $V$ của $E$ cho ta không gian con $V^{0}$ của $E^{*}$ bao gồm của tất cả các dạng tuyến tính rằng triệt tiêu trên $V$ (rằng là, có giá trị không với mọi input trong $V$). Xét sau đây tập hợp của hai “các phương trình tuyến tính” trong $\mathbb{R}^{3}$,
$$x -y + z = 0$$
$$x -y -z = 0,$$
Và cho chúng ta tìm ra những gì là của chúng tập hợp $V$ của chung/phổ biến các nghiệm $(x, y, z) \in \mathbb{R}^{3}$. Bằng cách trừ phương trình thứ hai từ thứ nhất, ta thu được 2z $= 0$, và bằng cách cộng hai các phương trình, ta tìm
$$415$$

<!-- PAGE 416 -->
Rằng 2(x - $y) = 0$, do đó tập hợp $V$ của các nghiệm được cho bởi
$$y = x$$
$$z = 0.$$
Điều này là một dimensional không gian con của $\mathbb{R}^{3}$. Geometrically, điều này là đường thẳng của phương trình $y = x$ trong mặt phẳng $z = 0$ như được minh họa bởi Hình 11.1.

![Figure 11.1](../../assets/ch11/fig_11_1.png)

**Hình 11.1:** giao của magenta mặt phẳng $x$ - $y + z = 0$ với blue-gray mặt phẳng $x$ - $y$ - $z = 0$ là hồng đường thẳng $y = x$. Bây giờ tại sao đã thực hiện ta nói rằng ở trên các phương trình là tuyến tính? Bởi vì như các hàm của $(x, y, z)$, cả hai các ánh xạ $f_{1}$: $(x, y, z) \mapsto x$ - $y + z$ và $f_{2}$: $(x, y, z) \mapsto x$ - $y$ - $z$ là tuyến tính. tập hợp của
$$\mathbb{R}^{3}  \mathbb{R}$$
Tất cả như vậy tuyến tính các hàm từ đến là không gian vectơ (vector space); ta được sử dụng sự kiện này đến tạo thành các tổ hợp tuyến tính của “các phương trình” $f_{1}$ và $f_{2}$. Nhận thấy rằng số chiều của không gian con $V$ là $1$. ambient không gian có số chiều $n = 3$ và có hai “độc lập” các phương trình $f_{1}, f_{2}$, do đó nó xuất hiện rằng số chiều dim(V) của không gian con $V$ được định nghĩa bởi $m$ độc lập các phương trình là
$$\dim(V ) = n -m,$$
Mà là thật vậy tổng quát sự kiện (được chứng minh trong Định lý 11.4). Tổng quát hơn, trong $\mathbb{R}^{n}$, phương trình tuyến tính được xác định bởi bộ $n$ $(a_{1}, \dots  , a_{n}) \in \mathbb{R}^{n}$,
$$\mathbb{R}^{n}$$
Và các nghiệm của điều này phương trình tuyến tính được cho bởi các bộ $n$ $(x_{1}, \dots  , x_{n}) \in$ sao cho
$$a_{1}x_{1} + \cdots  + a_{n}x_{n} = 0;$$
Các nghiệm này constitute hạt nhân (kernel) của ánh xạ tuyến tính (linear map) $(x_{1}, \dots  , x_{n}) \mapsto a_{1}x_{1} + \cdots  + a_{n}x_{n}$. ở trên considerations giả sử rằng ta là làm việc trong cơ sở chính tắc (canonical basis) $(e_{1}, \dots  , e_{n})$ của $\mathbb{R}^{n}$, nhưng ta có thể định nghĩa “các phương trình tuyến tính” một cách độc lập của các cơ sở và trong bất kỳ số chiều, bởi

<!-- PAGE 417 -->
Quan điểm chúng như các phần tử của không gian vectơ (vector space) Hom(E, $K)$ của các ánh xạ tuyến tính (linear maps) từ $E$ đến trường $K$.

> **Định nghĩa 11.1.** Cho trước không gian vectơ (vector space) $E$, không gian vectơ (vector space) Hom(E, $K)$ của các ánh xạ tuyến tính (linear maps) từ $E$ đến trường $K$ được gọi là không gian đối ngẫu (dual space) (hoặc đối ngẫu (dual)) của $E$. không gian Hom(E, $K)$ cũng được ký hiệu bởi $E^{*}$, và các ánh xạ tuyến tính (linear maps) trong $E^{*}$ được gọi là các dạng tuyến tính, hoặc covectors. không gian đối ngẫu (dual space) $E^{**}$ của không gian $E^{*}$ được gọi là bidual của $E$. Như matter của ký hiệu, các dạng tuyến tính $f$: $E \to K$ sẽ cũng được ký hiệu bởi starred ký hiệu, chẳng hạn như $u^{*}, x^{*}$, etc. Cho trước không gian vectơ (vector space) $E$ và bất kỳ cơ sở (basis) $(u_{i})_{i\in I}$ cho $E$, ta có thể associate đến mỗi $u_{i}$ dạng tuyến tính (linear form) $u_{i}^{*} \in E^{*}$, và $u_{i}^{*}$ có một số đáng chú ý các tính chất.

> **Định nghĩa 11.2.** Cho trước không gian vectơ (vector space) $E$ và bất kỳ cơ sở (basis) $(u_{i})_{i\in I}$ cho $E$, theo Mệnh đề 3.20, với mọi $i \in$ I, tồn tại duy nhất một dạng tuyến tính (linear form) $u_{i}^{*}$ sao cho
$$1if i = j$$
$$u_{i}^{*} (u_{j}) =$$
$$0if i \neq  j,$$
Với mọi $j \in$ I. dạng tuyến tính (linear form) $u_{i}^{*}$ được gọi là tọa độ tạo thành của chỉ số $i$ w.r.t. cơ sở (basis) $(u_{i})_{i\in I}$. lý do cho thuật ngữ tọa độ tạo thành đã được giải thích trong Mục 3.9. Ta được chứng minh trong Định lý 3.26 rằng nếu $(u_{1}, \dots  , u_{n})$ là cơ sở (basis) của $E$, thì $(u_{1}^{*}, \dots  , u_{n}^{*})$ là cơ sở (basis) của $E^{*}$ được gọi là đối ngẫu (dual) cơ sở (basis).
$$\mathbb{R}^{n}$$
Nếu $(u_{1}, \dots  , u_{n})$ là cơ sở (basis) của (tổng quát hơn $K^{n})$, nó là khả dĩ/có thể để tìm một cách tường minh đối ngẫu (dual) cơ sở (basis) $(u_{1}^{*}, \dots  , u_{n}^{*})$, ở đâu mỗi $u_{i}^{*}$ được biểu diễn bởi vectơ hàng (row vector).

> **Ví dụ 11.1.** Ví dụ, xét các cột của B´ezier ma trận
$$B_{4} = \begin{pmatrix} 1 & -3 & 3 & -1 \\ 0 & 3 & -6 & 3 \\ 0 & 0 & 3 & -3 \\ 0 & 0 & 0 & 1 \end{pmatrix} .$$
Nói cách khác, ta có cơ sở (basis)
$$u_{1} = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} u_{2} = \begin{pmatrix} -3 \\ 3 \\ 0 \\ 0 \end{pmatrix} u_{3} = \begin{pmatrix} 3 \\ -6 \\ 3 \\ 0 \end{pmatrix} u_{4} = \begin{pmatrix} -1 \\ 3 \\ -3 \\ 1 \end{pmatrix} .$$

<!-- PAGE 418 -->
Vì tạo thành $u_{1}^{*}$ được định nghĩa bởi các điều kiện $u_{1}^{*}(u_{1}) = 1, u_{1}^{*}(u_{2}) = 0, u_{1}^{*}(u_{3}) = 0, u_{1}^{*}(u_{4}) = 0$, nó được biểu diễn bởi vectơ hàng (row vector) $(\lambda_{1}  \lambda_{2}  \lambda_{3}  \lambda_{4}$) sao cho
$$\begin{pmatrix} \lambda_{1} & \lambda_{2} & \lambda_{3} & \lambda_{4} \end{pmatrix} \begin{pmatrix} 1 & -3 & 3 & -1 \\ 0 & 3 & -6 & 3 \\ 0 & 0 & 3 & -3 \\ 0 & 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \end{pmatrix} .$$
Điều này suy ra rằng $u_{1}^{*}$ là hàng thứ nhất của nghịch đảo của $B_{4}$. Vì
$$B_{4}^{-1}= \begin{pmatrix} 1 & 1 & 1 & 1 \\ 0 & 1/3 & 2/3 & 1 \\ 0 & 0 & 1/3 & 1 \\ 0 & 0 & 0 & 1 \end{pmatrix} ,$$
Các dạng tuyến tính $(u_{1}^{*}, u_{2}^{*}, u_{3}^{*}, u_{4}^{*})$ tương ứng với các hàng của $B_{4}^{-1}$. Đặc biệt, $u_{1}^{*}$ được biểu diễn bởi $(1 1 1 1)$. ở trên phương pháp hoạt động với mọi $n$. Cho trước bất kỳ cơ sở (basis) $(u_{1}, \dots  , u_{n})$ của $\mathbb{R}^{n}$, nếu $P$ là ma trận cỡ $n \times  n$ có cột thứ $j$ là $u_{j}$, thì đối ngẫu (dual) tạo thành $u_{i}^{*}$ được cho bởi hàng thứ $i$ của ma trận $P^{-1}$. Khi $E$ là của hữu hạn số chiều $n$ và $(u_{1}, \dots  , u_{n})$ là cơ sở (basis) của $E$, theo Định lý 11.4 $(1)$, họ $(u_{1}^{*}, \dots  , u_{n}^{*})$ là cơ sở (basis) của không gian đối ngẫu (dual space) $E^{*}$. Cho chúng ta xem cách mà các tọa độ của dạng tuyến tính (linear form) $\phi^{*} \in E^{*}$ trên đối ngẫu (dual) cơ sở (basis) $(u_{1}^{*}, \dots  , u_{n}^{*})$ biến thiên dưới chuyển cơ sở (change of basis). Cho $(u_{1}, \dots  , u_{n})$ và $(v_{1}, \dots  , v_{n})$ là hai các cơ sở của $E$, và cho $P = (a_{i j})$ là ma trận chuyển cơ sở (change of basis matrix) từ $(u_{1}, \dots  , u_{n})$ đến $(v_{1}, \dots  , v_{n})$, sao cho
$$v_{j} = \sum_{i=1}^{n}  a_{i j}u_{i},$$
Và cho $P^{-1} = (b_{i j})$ là nghịch đảo của $P$, sao cho
$$u_{i} = \sum_{j=1}^{n}  b_{j i}v_{j}.$$
Cho cố định $j$, ở đâu $1 \le j \le n$, ta muốn để tìm các vô hướng $(c_{i})_{i=1}^{n}$ sao cho
$$v_{j}^{*} = c_{1}u_{1}^{*} + c_{2}u_{2}^{*} + \cdots  + c_{n}u_{n}^{*}.$$
Để tìm mỗi $c_{i}$, ta tính giá trị ở trên biểu thức tại $u_{i}$. Vì $u_{i}^{*} (u_{j}) = \delta_{i j}$ và $v_{i}^{*} (v_{j}) = \delta_{i j}$, ta thu được
$$v_{j}^{*}(u_{i}) = (c_{1}u^{*} + c_{2}u_{2}^{*} + \cdots  + c_{n}u_{n}^{*})(u_{i}) = c_{i}$$
$$v_{j}^{*}(u_{i}) = v_{j}^{*}( \sum_{k=1}^{1n}  b_{k i}v_{k}) = b_{j i},$$

<!-- PAGE 419 -->
Và do đó
$$v_{j}^{*} = \sum_{i=1}^{n}  b_{j i}u_{i}^{*} .$$
Đồng dạng các phép tính chỉ ra rằng
$$u_{i}^{*} = \sum_{j=1}^{n}  a_{i j}v_{j}^{*}.$$
Điều này có nghĩa là chuyển cơ sở (change of basis) từ đối ngẫu (dual) cơ sở (basis) $(u_{1}^{*}, \dots  , u_{n}^{*})$ đến đối ngẫu (dual) cơ sở (basis) $(v_{1}^{*}, \dots  , v_{n}^{*})$ là $(P^{-1})^{\top}$. Vì
$$\phi^{*} = \sum_{i=1}^{n}  \phi_{i} u_{i}^{*} = \sum_{i=1}^{n}  \phi \sum_{ij=1}^{n}  a_{ij}v_{j}^{*} = \sum_{j=1}^{n}  \sum_{i=1}^{n}  a_{ij}\phi_{i} !v_{j} = \sum_{i=1}^{n}  \phi_{i}' v_{i}^{*} ,$$
Ta thu được
$$\phi_{j}'  = \sum_{i=1}^{n}  a_{i j}\phi_{i} ,$$
Do đó mới các tọa độ $\phi_{j}'$ được biểu diễn theo old các tọa độ $\phi_{i}$ bằng cách sử dụng ma trận $P^{\top}$. Nếu ta sử dụng các vectơ hàng $(\phi_{1} , \dots  , \phi_{n}$) và $(\phi_{1}' , \dots  , \phi_{n}'$), ta có
$$(\phi_{1}' , \dots  , \phi_{n}' ) = (\phi_{1} , \dots  , \phi_{n} )P.$$
Các phần tử này các sự kiện là summarized trong sau đây mệnh đề.

> **Mệnh đề 11.1.** Cho $(u_{1}, \dots  , u_{n})$ và $(v_{1}, \dots  , v_{n})$ là hai các cơ sở của $E$, và cho $P = (a_{i j})$ là ma trận chuyển cơ sở (change of basis matrix) từ $(u_{1}, \dots  , u_{n})$ đến $(v_{1}, \dots  , v_{n})$, sao cho
$$v_{j} = \sum_{i=1}^{n}  a_{i j}u_{i}.$$
Thì chuyển cơ sở (change of basis) từ đối ngẫu (dual) cơ sở (basis) $(u_{1}^{*}, \dots  , u_{n}^{*})$ đến đối ngẫu (dual) cơ sở (basis) $(v_{1}^{*}, \dots  , v_{n}^{*})$ là $(P^{-1} )^{\top}$, và với mọi dạng tuyến tính (linear form) $\phi$, mới các tọa độ $\phi_{j}'$ của $\phi$ được biểu diễn theo old các tọa độ $\phi_{i}$ của $\phi$ bằng cách sử dụng ma trận $P^{\top}$; rằng là,
$$(\phi_{1}' , \dots  , \phi_{n}' ) = (\phi_{1} , \dots  , \phi_{n} )P.$$
Đến tốt nhất understand trước đó paragraph, nhắc lại Ví dụ 3.1, trong mà $E = \mathbb{R}^{2}, u_{1} = (1, 0), u_{2} = (0, 1)$, và $v_{1} = (1, 1), v_{2} = (-1, 1)$. Thì $P$, ma trận chuyển cơ sở (change of basis matrix) từ $(u_{1}, u_{2})$ đến $(v_{1}, v_{2})$, được cho bởi
$$P = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} ,$$
Với $(v_{1}, v_{2}) = (u_{1}, u_{2})P$, và $(u_{1}, u_{2}) = (v_{1}, v_{2})P^{-1}$, ở đâu
$$P^{-1}= \begin{pmatrix} 1/2 & 1/2 \\ -1/2 & 1/2 \end{pmatrix} .$$

<!-- PAGE 420 -->
Cho $(u_{1}^{*}, u_{2}^{*})$ là đối ngẫu (dual) cơ sở (basis) cho $(u_{1}, u_{2})$ và $(v_{1}^{*}, v_{2}^{*})$ là đối ngẫu (dual) cơ sở (basis) cho $(v_{1}, v_{2})$. Ta khẳng định rằng
$$(v_{1}^{*}, v_{2}^{*}) = (u_{1}^{*}, u_{2}^{*}) \begin{pmatrix} 1/2 & -1/2 \\ 1/2 & 1/2 \end{pmatrix} = (u_{1}^{*}, u_{2}^{*})(P^{-1})^{\top},$$
Thật vậy, vì $v_{1}^{*} = c_{1}u_{1}^{*} + c_{2}u_{2}^{*}$ và $v_{2}^{*} = C_{1}u_{1}^{*} + C_{2}u_{2}^{*}$ ta tìm rằng $c_{1} = v_{1}^{*}(u_{1}) = v_{1}^{*}(1/2v_{1}$ - $1/2v_{2}) = 1/2 c_{2} = v_{1}^{*}(u_{2}) = v_{1}^{*}(1/2v_{1} + 1/2v_{2}) = 1/2 C_{1} = v_{2}^{*}(u_{1}) = v_{2}^{*}(1/2v_{1}$ - $1/2v_{2}) = -1/2 C_{2} = v_{2}^{*}(u_{2}) = v_{1}^{*}(1/2v_{1} + 1/2v_{2}) = 1/2$. Hơn nữa, vì $(u_{1}^{*}, u_{2}^{*}) = (v_{1}^{*}, v_{2}^{*})P^{\top}$ (vì $(v_{1}^{*}, v_{2}^{*}) = (u_{1}^{*}, u_{2}^{*})(P^{\top})^{-1})$, ta tìm rằng $\phi^{*} = \phi_{1} u_{1}^{*} + \phi_{2} u_{2}^{*} = \phi_{1} (v_{1}^{*}$ - $v_{2}^{*}) + \phi_{(} v_{1}^{*} + v_{2}^{*}) = (\phi_{1}  + \phi_{2} )v_{1}^{*} + (-\phi_{1}  + \phi_{2} )v_{2}^{*} = \phi_{1}' v_{1}^{*} + \phi_{2}' v_{2}^{.}$ Do đó
$$\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix} \begin{pmatrix} \phi_{1} \\ \phi_{2} \end{pmatrix} = \begin{pmatrix} \phi_{1}' \\ \phi_{2}' \end{pmatrix} ,$$
Ở đâu
$$P^{\top} = \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix} .$$
Comparing với chuyển cơ sở (change of basis)
$$v_{j} = \sum_{i=1}^{n}  a_{i j}u_{i},$$
Ta lưu ý rằng điều này time, các tọa độ $(\phi_{i}$) của dạng tuyến tính (linear form) $\phi^{*}$ thay đổi trong cùng hướng như chuyển cơ sở (change of basis). Cho điều này lý do, ta nói rằng các tọa độ của các dạng tuyến tính là hiệp biến. Lạm dụng language, nó là thường được nói rằng các dạng tuyến tính là hiệp biến, mà các giải thích tại sao số hạng covector cũng được sử dụng cho dạng tuyến tính (linear form). Nhận thấy rằng nếu $(e_{1}, \dots  , e_{n})$ là cơ sở (basis) của không gian vectơ (vector space) $E$, thì, như ánh xạ tuyến tính (linear map) từ $E$ đến $K$, mọi dạng tuyến tính (linear form) $f \in E^{*}$ được biểu diễn bởi một ma trận cỡ $1 \times  n$, nghĩa là, bởi vectơ hàng (row vector)
$$(\lambda_{1}  \cdots  \lambda_{n} ),$$
Đối với cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $E$, và $1$ của $K$, ở đâu $f(e_{i}) = \lambda_{i}$. vectơ $u =$
$$\sum_{i}  n=1 u_{i}e_{i} \in E is represented by a n \times  1 matrix, that is, by a column vector$$
$$\begin{pmatrix} u_{1} \\ \vdots \\ u_{n} \end{pmatrix} ,$$
Và action của $f$ trên $u$, cụ thể là f(u), được biểu diễn bởi ma trận tích
$$\begin{pmatrix} \lambda_{1} & \cdots & \lambda_{n} \end{pmatrix} \begin{pmatrix} u_{1} \\ \vdots \\ u_{n} \end{pmatrix} = \lambda_{1} u_{1} + \cdots  + \lambda_{n} u_{n}.$$

<!-- PAGE 421 -->
Mặt khác, đối với đối ngẫu (dual) cơ sở (basis) $(e_{1}^{*}, \dots  , e_{n}^{*})$ của $E^{*}$, dạng tuyến tính (linear form) $f$ được biểu diễn bởi vectơ cột (column vector)
$$\begin{pmatrix} \lambda_{1} \\ \vdots \\ \lambda_{n} \end{pmatrix} .$$
Nhận xét: Trong nhiều các văn bản bằng cách sử dụng các tenxơ, các vectơ là thường được chỉ số với thấp hơn các chỉ số. Nếu do đó, nó là nhiều hơn/thêm thuận tiện đến viết các tọa độ của vectơ $x$ trên cơ sở (basis) $(u_{1}, \dots  , u_{n})$ như $(x^{i})$, bằng cách sử dụng trên chỉ số, sao cho
$$x = \sum_{i=1}^{n}  x^{i}u_{i},$$
Và trong chuyển cơ sở (change of basis), ta có
$$v_{j} = \sum_{i=1}^{n}  a_{j}^{i}u_{i}$$
Và
$$x^{i} = \sum_{j=1}^{n}  a_{j}^{i}x^{'j}.$$
Một cách đối ngẫu (dual), các dạng tuyến tính được chỉ số với trên các chỉ số. Thì nó là nhiều hơn/thêm thuận tiện đến viết các tọa độ của covector $\phi^{*}$ trên đối ngẫu (dual) cơ sở (basis) $(u^{*1}, \dots  , u^{*n})$ như $(\phi_{i}$), bằng cách sử dụng thấp hơn chỉ số, sao cho
$$\phi^{*} = \sum_{i=1}^{n}  \phi_{i} u^{*i}$$
Và trong chuyển cơ sở (change of basis), ta có
$$u^{*i} = \sum_{j=1}^{n}  a_{j}^{i}v^{*j}$$
Và
$$\phi_{j}'  = \sum_{i=1}^{n}  a_{j}^{i}\phi_{i} .$$
Với các phần tử này các quy ước, chỉ số của phép lấy tổng xuất hiện một lần trong trên position và một lần trong thấp hơn position, và phép lấy tổng dấu có thể được safely được bỏ qua, mẹo/kỹ thuật do Einstein. Ví dụ, ta có thể viết
$$\phi_{j}'  = a_{j}^{i}\phi_{i}$$
Như abbreviation cho
$$\phi_{j}'  = \sum_{i=1}^{n}  a_{j}^{i}\phi_{i} .$$
