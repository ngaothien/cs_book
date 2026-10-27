# Đối ngẫu Định lý và Một số Các hệ quả


<!-- PAGE 427 -->
Của đại số hình học, đẹp nhưng formidable subject. Cho taste của đại số hình học, xem Lang $[113]$ hoặc Dummit và Foote $[55]$. đối ngẫu định lý (Định lý 11.4) chỉ ra rằng tình huống là nhiều đơn giản hơn nếu ta thu hẹp của ta attention đến tuyến tính các không gian con; trong trường hợp này
$$U =\mathcal{I}(\mathcal{Z}(U))andV =\mathcal{Z}(\mathcal{I}(V )).$$

> **Mệnh đề 11.3.** Ta có $V \subseteq V^{00}$ với mọi không gian con $V$ của $E$, và $U \subseteq U^{00}$ với mọi không gian con $U$ của $E^{*}$.

*Chứng minh.* Thật vậy, với mọi $v \in V$, để chỉ ra rằng $v \in V^{00}$ ta cần để chứng minh rằng $u^{*}(v) = 0$ với mọi $u^{*} \in V^{0}$. Tuy nhiên, $V^{0}$ bao gồm của tất cả các dạng tuyến tính $u^{*}$ sao cho $u^{*}(y) = 0$ với mọi $y \in V$; đặc biệt, cho cố định $v \in V$, ta có $u^{*}(v) = 0$ với mọi $u^{*} \in V^{0}$, như cần thiết. Tương tự, với mọi $u^{*} \in U$, để chỉ ra rằng $u^{*} \in U^{00}$ ta cần để chứng minh rằng $u^{*}(v) = 0$ với mọi $v \in U^{0}$. Tuy nhiên, $U^{0}$ bao gồm của tất cả các vectơ $v$ sao cho $f^{*}(v) = 0$ với mọi $f^{*} \in U$; đặc biệt, cho cố định $u^{*} \in U$, ta có $u^{*}(v) = 0$ với mọi $v \in U^{0}$, như cần thiết. Ta sẽ xem một cách ngắn rằng trong hữu hạn số chiều, ta có $V = V^{00}$ và $U = U^{00}$.  Tuy nhiên, chẵn/ngay cả dù $V = V^{00}$ là luôn luôn đúng, khi $E$ là của vô hạn số chiều, nó là không luôn luôn đúng rằng $U = U^{00}$. Cho trước không gian vectơ (vector space) $E$ và không gian con $U$ của $E$, theo Định lý 3.8, mọi cơ sở (basis) $(u_{i})_{i\in I}$ của $U$ có thể được được mở rộng đến cơ sở (basis) $(u_{j})_{j\in I\cup J}$ của $E$, ở đâu I $\cap J = \emptyset$.

## 11.3 Đối ngẫu Định lý và Một số Các hệ quả

Ta có kết quả sau quan trọng định lý được điều chỉnh từ $E$. Artin $[6]$ (Chương $1)$.

> **Định lý 11.4.** (Đối ngẫu định lý) Cho $E$ là không gian vectơ (vector space). Các tính chất sau đây đúng:
() Với mọi cơ sở (basis) $(u_{i})_{i\in I}$ của $E$, họ $(u_{i}^{*} )_{i\in I}$ của tọa độ các dạng là độc lập tuyến tính (linearly independent).
$(b)$ Với mọi không gian con $V$ của $E$, ta có $V^{00} = V$.
$(c)$ Với mọi không gian con $V$ của hữu hạn đối chiều (codimension) $m$ của $E$, với mọi không gian con $W$ của $E$ sao cho $E = V \oplus W$ (ở đâu $W$ là của hữu hạn số chiều $m)$, với mọi cơ sở (basis) $(u_{i})_{i\in I}$ của $E$ sao cho $(u_{1}, \dots  , u_{m})$ là cơ sở (basis) của $W$, họ $(u_{1}^{*}, \dots  , u_{m}^{*})$ là cơ sở (basis) của trực giao $V^{0}$ của $V$ trong $E^{*}$, sao cho
$$\dim(V^{0} ) = codim(V ).$$
Hơn nữa, ta có $V^{00} = V$.

<!-- PAGE 428 -->
$(d)$ Với mọi không gian con $U$ của hữu hạn số chiều $m$ của $E^{*}$, trực giao $U^{0}$ của $U$ trong $E$ là của hữu hạn đối chiều (codimension) $m$, sao cho
$$codim(U^{0} ) = \dim(U).$$
Hơn nữa, $U^{00} = U$.

*Chứng minh.* () Giả sử rằng
$$\sum_{i\in I}  \lambda_{i} u_{i}^{*} = 0,$$
Cho họ $(\lambda_{i} )_{i\in I}$ (của các vô hướng trong $K)$. Vì $(\lambda_{i} )_{i\in I}$ có hữu hạn hỗ trợ/giá (support), có một hữu hạn tập con $J$ của I sao cho $\lambda_{i}  = 0$ với mọi $i \in$ I - $J$, và ta có
$$\sum_{j\in J}  \lambda_{j} u_{j}^{*} = 0.$$
$$Applying the linear form \sum_{j}  \in J \lambda_{j} u_{j}^{*} to each u_{j} (j \in J), by Definition 11.2, since u_{i}^{*} (u_{j}) = 1$$
Nếu $i = j$ và $0$ ngược lại, ta thu được $\lambda_{j}  = 0$ với mọi $j \in J$, nghĩa là $\lambda_{i}  = 0$ với mọi $i \in$ I (theo định nghĩa của $J$ như hỗ trợ/giá (support)). Do đó, $(u_{i}^{*} )_{i\in I}$ là độc lập tuyến tính (linearly independent).
$(b)$ Rõ ràng, ta có $V \subseteq V^{00}$. Nếu V̸ $= V^{00}$, thì cho $(u_{i})_{i\in I\cup J}$ là cơ sở (basis) của $V^{00}$ sao cho $(u_{i})_{i\in I}$ là cơ sở (basis) của $V$ (ở đâu I $\cap J = \emptyset$). Vì V̸ $= V^{00}, u_{j0} \in V^{00}$ với một số $j_{0} \in J$ (và do đó, $j_{0} \in /$ I). Vì $u_{j0} \in V^{00} , u_{j0}$ là trực giao đến mọi dạng tuyến tính (linear form) trong $V^{0}$. Bây giờ, ta có $u_{j0}^{*}(u_{i}) = 0$ với mọi $i \in$ I, và do đó $u_{j0}^{*} \in V^{0}$. Tuy nhiên, $u_{j0}^{*}(u_{j0}) = 1$, contradicting sự kiện rằng $u_{j0}$ là trực giao đến mọi dạng tuyến tính (linear form) trong $V^{0}$. Do đó, $V = V^{00}$.
$(c)$ Cho $J =$ I $-{1, \dots  , m}$. Mọi dạng tuyến tính (linear form) $f^{*} \in V^{0}$ là trực giao đến mọi $u_{j}$, cho $j \in J$, và do đó, $f^{*} (u_{j}) = 0$, với mọi $j \in J$. Cho như vậy dạng tuyến tính (linear form) $f^{*} \in V^{0}$, cho
$$g^{*}= f^{*} (u_{1})u_{1}^{*} + \cdots  + f^{*}(u_{m})u_{m}^{*}.$$
Ta có $g^{*}(u_{i}) = f^{*} (u_{i})$, với mọi $i, 1 \le i \le m$. Hơn nữa, theo Định nghĩa, $g^{*}$ triệt tiêu trên tất cả $u_{j}$, ở đâu $j \in J$. Do đó, $f^{*}$ và $g^{*}$ agree trên cơ sở (basis) $(u_{i})_{i\in I}$ của $E$, và do đó, $g^{*} = f^{*}$. Điều này chỉ ra rằng $(u_{1}^{*}, \dots  , u_{m}^{*})$ sinh ra $V^{0}$, và vì nó là cũng độc lập tuyến tính (linearly independent) họ, $(u_{1}^{*}, \dots  , u_{m}^{*})$ là cơ sở (basis) của $V^{0}$. Nó là thì hiển nhiên rằng $dim(V^{0}$) $=$ codim(V), và bởi phần $(b)$, ta có $V^{00} = V$.
$(d)$ Cho $(u_{1}^{*}, \dots  , u_{m}^{*})$ là cơ sở (basis) của $U$. Lưu ý rằng ánh xạ $h: E \to K^{m}$ được định nghĩa sao cho
$$h(v) = (u_{1}^{*}(v), \dots  , u_{m}^{*}(v))$$
Với mọi $v \in E$, là ánh xạ tuyến tính (linear map), và rằng hạt nhân (hạt nhân (kernel)) của nó Ker $h$ là một cách chính xác $U^{0}$. Thì, theo Mệnh đề 6.16,
$$E \approx \mathrm{Ker} (h) \oplus \mathrm{Im} h = U^{0}\oplus \mathrm{Im} h,$$
Và vì dim(Im $h) \le m$, ta suy ra rằng $U^{0}$ là không gian con của $E$ của hữu hạn đối chiều (codimension) nhiều nhất $m$, và bởi $(c)$, ta có $dim(U^{00}$) $= codim(U^{0}$) $\le m =$ dim(U). Tuy nhiên, rõ ràng là $U \subseteq U^{00}$, mà suy ra dim(U) $\le dim(U^{00}$), và do đó $dim(U^{00}$) $=$ dim(U) $= m$, và ta phải có $U = U^{00}$.

<!-- PAGE 429 -->
Phần () của Định lý 11.4 chỉ ra rằng
$$\dim(E) \le \dim(E^{*}).$$
Khi $E$ là của hữu hạn số chiều $n$ và $(u_{1}, \dots  , u_{n})$ là cơ sở (basis) của $E$, bởi phần $(c)$, họ $(u_{1}^{*}, \dots  , u_{n}^{*})$ là cơ sở (basis) của không gian đối ngẫu (dual space) $E^{*}$, được gọi là đối ngẫu (dual) cơ sở (basis) của $(u_{1}, \dots  , u_{n})$. sự kiện này đã cũng được chứng minh một cách trực tiếp trong Định lý 3.26. Định nghĩa hàm $\mathcal{E} (\mathcal{E}$ cho các phương trình) từ các không gian con của $E$ đến các không gian con của $E^{*}$ và hàm $\mathcal{Z} (\mathcal{Z}$ cho các không điểm) từ các không gian con của $E^{*}$ đến các không gian con của $E$ bởi
$$\mathcal{E}(V ) = V^{0} ,V \subseteq E$$
$$\mathcal{Z}(U) = U^{0} ,U \subseteq E^{*}.$$
Bởi Các phần $(c)$ và $(d)$ của Định lý 11.4,
$$(\mathcal{Z} \circ E)(V ) = V^{00}= V$$
$$(\mathcal{E} \circ Z)(U) = U^{00}= U,$$
Do đó $\mathcal{Z} \circ E =$ id và $\mathcal{E} \circ Z =$ id, và các ánh xạ $\mathcal{E}$ và $\mathcal{Z}$ là nghịch đảo các song ánh. các ánh xạ này tập hợp lên đối ngẫu giữa các không gian con của $E$ và các không gian con của $E^{*}$. Đặc biệt, mọi không gian con $V \subseteq E$ có số chiều $m$ là tập hợp của chung/phổ biến các không điểm của không gian của các dạng tuyến tính (các phương trình) $V^{0}$, mà có số chiều $n$ - $m$. Điều này xác nhận khẳng định ta được tạo về số chiều của subpsace được định nghĩa bởi tập hợp của các phương trình tuyến tính.  Một nên là careful rằng song ánh này thực hiện không mở rộng đến các không gian con của $E^{*}$ của vô hạn số chiều.  Khi $E$ là của vô hạn số chiều, với mọi cơ sở (basis) $(u_{i})_{i\in I}$ của $E$, họ $(u_{i}^{*} )_{i\in I}$ của tọa độ các dạng là không bao giờ cơ sở (basis) của $E^{*}$. Nó là độc lập tuyến tính (linearly independent), nhưng nó là “cũng nhỏ” đến sinh $E^{*}$. Ví dụ, nếu $E = \mathbb{R}^{(N)}$, ở đâu $\mathbb{N} = {0, 1, 2, \dots$ }, ánh xạ $f$: $E \to \mathbb{R}$ rằng các tổng khác không các tọa độ của vectơ trong $E$ là dạng tuyến tính (linear form), nhưng nó là dễ để xem rằng nó không thể được biểu diễn như tổ hợp tuyến tính (linear combination) của tọa độ các dạng. Hệ quả là, khi $E$ là của vô hạn số chiều, $E$ và $E^{*}$ là không đẳng cấu. Ta bây giờ thảo luận một số các ứng dụng của đối ngẫu định lý.
$$\mathbb{R}^{n}$$
Bài toán $1$. Giả sử rằng $V$ là không gian con của có số chiều $m$ và rằng $(v_{1}, \dots  , v_{m})$ là cơ sở (basis) của $V$. bài toán là để tìm cơ sở (basis) của $V^{0}$. Ta thứ nhất mở rộng $(v_{1}, \dots  , v_{m})$ đến cơ sở (basis) $(v_{1}, \dots  , v_{n}) of\mathbb{R}^{n}$, và thì bởi phần $(c)$ của Định lý 11.4, ta biết rằng $(v_{m+1}^{*}, \dots  , v_{n}^{*})$ là cơ sở (basis) của $V^{0}$.
$$\mathbb{R}^{4}$$

> **Ví dụ 11.6.** Ví dụ, giả sử rằng $V$ là không gian con của được sinh (spanned) bởi hai các vectơ độc lập tuyến tính (linearly independent)
$$v_{1} = \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \end{pmatrix} v_{2} = \begin{pmatrix} 1 \\ 1 \\ -1 \\ 1 \end{pmatrix} ,$$
$$-$$

<!-- PAGE 430 -->
Thứ nhất hai các vectơ của Cơ sở Haar (Haar basis) trong $\mathbb{R}^{4}$. bốn các cột của Haar ma trận
$$W = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 1 & -1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & 0 & 1 \end{pmatrix}$$
$$--$$
Tạo thành cơ sở (basis) của $\mathbb{R}^{4}$, và nghịch đảo của $W$ được cho bởi
$$W^{-1}  = \begin{pmatrix} 1/4 & 0 & 0 & 0 \\ 0 & 1/4 & 0 & 0 \\ 0 & 0 & 1/2 & 0 \\ 0 & 0 & 0 & 1/2 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & -1 & -1 \\ 1 & -1 & 0 & 0 \\ 0 & 0 & 1 & 1 \end{pmatrix} = \begin{pmatrix} 1/4 & 1/4 & 1/4 & 1/4 \\ 1/4 & 1/4 & -1/4 & -1/4 \\ 1/2 & -1/2 & 0 & 0 \\ 0 & 0 & 1/2 & 1/2 \end{pmatrix} .$$
$$--$$
Vì đối ngẫu (dual) cơ sở (basis) $(v_{1}^{*}, v_{2}^{*}, v_{3}^{*}, v_{4}^{*})$ được cho bởi các hàng của $W^{-1}$, cuối cùng hai các hàng của $W^{-1}$,
$$\begin{pmatrix} 1/2 & -1/2 & 0 & 0 \\ 0 & 0 & 1/2 & -1/2 \end{pmatrix} ,$$
Tạo thành cơ sở (basis) của $V^{0}$. Ta cũng thu được cơ sở (basis) bởi rescaling bởi nhân tử $1/2$, do đó các dạng tuyến tính cho trước bởi các vectơ hàng
$$\begin{pmatrix} 1 & -1 & 0 & 0 \\ 0 & 0 & 1 & -1 \end{pmatrix}$$
Tạo thành cơ sở (basis) của $V^{0}$, không gian của các dạng tuyến tính (các phương trình tuyến tính) rằng triệt tiêu trên không gian con $V$. phương pháp rằng ta được mô tả để tìm $V^{0}$ đòi hỏi thứ nhất mở rộng cơ sở (basis) của $V$ và thì nghịch đảo ma trận, nhưng có một nhiều hơn/thêm trực tiếp phương pháp. Thật vậy, cho $A$ là ma trận cỡ $n \times  m$ có các cột là cơ sở (basis) các vectơ $(v_{1}, \dots  , v_{m})$ của $V$. Thì dạng tuyến tính (linear form) $u$ được biểu diễn bởi vectơ hàng (row vector) thuộc đến $V^{0}$ khi và chỉ khi $uv_{i} = 0$ cho $i = 1, \dots  , m$ khi và chỉ khi
$$uA = 0$$
Khi và chỉ khi
$$A^{\top}u^{\top}= 0.$$
Vì vậy, tất cả ta cần đến thực hiện là để tìm cơ sở (basis) của không gian hạch (nullspace) của $A^{\top}$. Điều này có thể được được thực hiện khá effectively bằng cách sử dụng reduction của ma trận đến dạng bậc thang rút gọn theo hàng (RREF) (rref); xem Mục 8.10.

> **Ví dụ 11.7.** Ví dụ, nếu ta reconsider trước đó ví dụ, $A^{\top}u^{\top} = 0$ trở thành
$$\begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & -1 & -1 \end{pmatrix} \begin{pmatrix} u_{1} \\ u_{2} \\ u_{3} \\ u_{4} \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} .$$

<!-- PAGE 431 -->
Vì rref của $A^{\top}$ là
$$\begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 \end{pmatrix} ,$$
Ở trên hệ là tương đương đến
$$\begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} u_{1} \\ u_{2} \\ u_{3} \\ u_{4} \end{pmatrix} = \begin{pmatrix} u_{1} + u_{2} \\ u_{3} + u_{4} \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} ,$$
Ở đâu tự do các biến là liên kết với $u_{2}$ và $u_{4}$. Do đó để xác định cơ sở (basis) cho hạt nhân (kernel) của $A^{\top}$, ta tập hợp $u_{2} = 1, u_{4} = 0$ và $u_{2} = 0, u_{4} = 1$ và thu được cơ sở (basis) cho $V^{0}$ như
$$\begin{pmatrix} 1 & -1 & 0 & 0 \end{pmatrix} , \begin{pmatrix} 0 & 0 & 1 & -1 \end{pmatrix} .$$
Bài toán $2$. Cho chúng ta bây giờ xét bài toán của việc tìm cơ sở (basis) của siêu phẳng (hyperplane) $H$ trong $\mathbb{R}^{n}$ được định nghĩa bởi phương trình
$$c_{1}x_{1} + \cdots  + c_{n}x_{n} = 0.$$
Chính xác hơn, nếu $u^{*}(x_{1}, \dots  , x_{n})$ là dạng tuyến tính (linear form) trong $(\mathbb{R}^{n})^{*}$ cho trước bởi $u^{*}(x_{1}, \dots  , x_{n}) = c_{1}x_{1} + \cdots  + c_{n}x_{n}$, thì siêu phẳng (hyperplane) $H$ là hạt nhân (kernel) của $u^{*}$. Của course ta giả sử rằng một số $c_{j}$ là khác không, trong mà trường hợp dạng tuyến tính (linear form) $u^{*}$ sinh ra một chiều không gian con $U$ của $(\mathbb{R}^{n})^{*}$, và $U^{0} = H$ có số chiều $n$ - $1$. Vì $u^{*}$ là không dạng tuyến tính (linear form) mà là một cách đồng nhất không, có một nhỏ nhất dương chỉ số $j \le n$ sao cho $c_{j} \neq  0$, do đó của ta dạng tuyến tính (linear form) là một cách thực $u^{*}(x_{1}, \dots  , x_{n}) = c_{j}x_{j} + \cdots  + c_{n}x_{n}$. Ta khẳng định rằng sau đây $n$ - $1$ các vectơ (trong $\mathbb{R}^{n})$ tạo thành cơ sở (basis) của $H$:
$$12\dots j -1jj + 1\dots n -1$$
$$1$$
$$2$$
$$\vdots$$
$$j -1 \begin{pmatrix} 1 & 0 & \dots & 0 & 0 & 0 & \dots & 0 \\ 0 & 1 & \dots & 0 & 0 & 0 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & 1 & 0 & 0 & \dots & 0 \\ 0 & 0 & \dots & 0 & -c_{j+1}/c_{j} & -c_{j+2}/c_{j} & \dots & -c_{n}/c_{j} \\ 0 & 0 & \dots & 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & \dots & 0 & 0 & 1 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & 0 & 0 & 0 & \dots & 1 \end{pmatrix}$$
$$j.$$
$$j + 1$$
$$j + 2$$
$$\vdots$$
$$n$$
Nhận thấy rằng $(n-1)\times$ (n-1) ma trận thu được bởi xóa hàng $j$ là ma trận đơn vị (identity matrix), do đó các cột của ở trên ma trận là độc lập tuyến tính (linearly independent). đơn giản phép tính cũng chỉ ra rằng dạng tuyến tính (linear form) $u^{*}(x_{1}, \dots  , x_{n}) = c_{j}x_{j} +\cdots +c_{n}x_{n}$ triệt tiêu trên mọi cột của ở trên

<!-- PAGE 432 -->
Ma trận. Cho concrete ví dụ trong $\mathbb{R}^{6}$, nếu $u^{*}(x_{1}, \dots  , x_{6}) = x_{3} + 2x_{4} + 3x_{5} + 4x_{6}$, ta thu được cơ sở (basis) cho siêu phẳng (hyperplane) $H$ của phương trình
$$x_{3} + 2x_{4} + 3x_{5} + 4x_{6} = 0$$
Cho trước bởi sau đây ma trận:
$$\begin{pmatrix} 1 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & -2 & -3 & -4 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$\mathbb{R}^{n}$$
Bài toán $3$. Ngược lại, cho trước siêu phẳng (hyperplane) $H$ trong cho trước như sinh (span) của $n -1$ một cách tuyến tính các vectơ $(u_{1}, \dots  , u_{n-1})$, nó là khả dĩ/có thể bằng cách sử dụng các định thức để tìm dạng tuyến tính (linear form) $(\lambda_{1} , \dots  , \lambda_{n}$) rằng triệt tiêu trên $H$. Trong trường hợp $n = 3$, ta là nhìn cho vectơ hàng (row vector) $(\lambda_{1} , \lambda_{2} , \lambda_{3}$) sao cho nếu
$$u = \begin{pmatrix} u_{1} \\ u_{2} \\ u_{3} \end{pmatrix} andv = \begin{pmatrix} v_{1} \\ v_{2} \\ v_{3} \end{pmatrix}$$
Là hai các vectơ độc lập tuyến tính (linearly independent), thì
$$\begin{pmatrix} u_{1} & u_{2} & u_{2} \\ v_{1} & v_{2} & v_{2} \end{pmatrix} \begin{pmatrix} \lambda_{1} \\ \lambda_{2} \\ \lambda_{3} \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} ,$$
Và cross-product $u \times  v$ của $u$ và $v$ cho trước bởi
$$u \times  v = \begin{pmatrix} u_{2}v_{3} -u_{3}v_{2} \\ u_{3}v_{1} -u_{1}v_{3} \\ u_{1}v_{2} & u_{2}v_{1} \end{pmatrix}$$
$$-$$
Là nghiệm. Nói cách khác, phương trình của mặt phẳng được sinh (spanned) bởi $u$ và $v$ là
$$(u_{2}v_{3} -u_{3}v_{2})x + (u_{3}v_{1} -u_{1}v_{3})y + (u_{1}v_{2} -u_{2}v_{1})z = 0.$$
Bài toán $4$. Ở đây là một cái khác ví dụ minh họa lũy thừa của Định lý 11.4. Cho $E = M_{n}(\mathbb{R})$, và xét các phương trình asserting rằng tổng của các phần tử (entries) trong mọi hàng của ma trận $A \in M_{n}(\mathbb{R})$ bằng cùng số. Ta có $n$ - $1$ các phương trình
$$\sum_{j=1}^{n}  (a_{ij} -a_{i+1j}) = 0,1 \le i \le n -1,$$
