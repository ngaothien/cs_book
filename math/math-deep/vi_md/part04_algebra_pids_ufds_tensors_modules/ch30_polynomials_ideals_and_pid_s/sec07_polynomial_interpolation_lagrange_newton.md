# Đa thức Nội suy (Lagrange, Newton, Hermite)


<!-- PAGE 1095 -->
Nhận xét: Đặt U(g) $=$ A-V $(g)$, đồng nhất thức $V (g_{1})\cup \cdots \cup V (g_{m}) = V (g_{1} \cdots  g_{m})$ translates đến $U(g_{1}) \cap \cdots  \cap U(g_{m}) = U(g_{1} \cdots  g_{m})$. Điều này suggests để định nghĩa tôpô trên $A$ có cơ sở (basis) của các tập mở bao gồm của các tập hợp U(g). Trong điều này tôpô (được gọi là Zariski tôpô), các tập hợp của tạo thành $V (g)$ là các tập đóng. Cũng, khi $g_{1}, \dots  , g_{m} \in A[X_{1}, \dots  , X_{n}]$ và $n \ge 2$, understanding cấu trúc của các tập đóng của tạo thành $V (g_{1})\cap \cdots \cap V (g_{m})$ là khá khó, và nó là object của đại số hình học (ít nhất, của nó cổ điển phần).  Khi $f \in A[X_{1}, \dots  , X_{n}]$ và $n \ge 2$, một nên không áp dụng Mệnh đề 30.27 abusively. Ví dụ, cho
$$f(X, Y ) = X^{2}+ Y^{2}-1,$$
Được xét như đa thức trong $\mathbb{R}[X, Y$ ]. Vì $\mathbb{R}$ là vô hạn trường và vì
$$-$$
$$f \begin{pmatrix} 1 -t^{2} & 2t \\ , \\ 1 + t^{2} & 1 + t^{2} \end{pmatrix} = \frac{(1t^{2})^{2}}{(1 + t^{2})^{2}} + \frac{(2t)^{2}}{(1 + t^{2})^{2}} -1 = 0,$$
Với mọi $t \in \mathbb{R}$, nó sẽ là tempting đến nói rằng $f = 0$. Nhưng những gì’s sai với ở trên lập luận là rằng có không có hai vô hạn các tập con $R_{1}, R_{2}$ của $\mathbb{R}$ sao cho $f(\alpha_{1} , \alpha_{2}$) $= 0$ với mọi $(\alpha_{1} , \alpha_{2}$) $\in \mathbb{R}^{2}$. Với mọi $\alpha_{1}  \in \mathbb{R}$, có nhiều nhất hai $\alpha_{2}  \in \mathbb{R}$ sao cho $f(\alpha_{1} , \alpha_{2}$) $= 0$. Những gì ví dụ chỉ ra dù, là rằng khác không đa thức $f \in A[X_{1}, \dots  , X_{n}]$ ở đâu $n \ge 2$ có thể có vô hạn số của các không điểm. Điều này là ngược lại với khác không các đa thức trong một các biến trên vô hạn trường (mà có số của các nghiệm bị chặn bởi của chúng bậc). Ta bây giờ nhìn tại đa thức nội suy.

## 30.7 Đa thức Nội suy (Lagrange, Newton,

$$Hermite)$$
Cho $K$ là trường. Thứ nhất, ta xét sau đây nội suy bài toán: Cho trước dãy $(\alpha_{1} , \dots  , \alpha_{m+1}$) của đôi một phân biệt các vô hướng trong $K$ và bất kỳ dãy $(\beta_{1} , \dots  , \beta_{m+1}$) của các vô hướng trong $K$, ở đâu $\beta_{j}$ là không nhất thiết phân biệt, tìm đa thức P(X) của bậc $\le m$ sao cho
$$P(\alpha_{1} ) = \beta_{1} , \dots  , P(\alpha_{m+1} ) = \beta_{m+1} .$$
Thứ nhất, nhận thấy rằng nếu như vậy đa thức tồn tại, thì nó là duy nhất. Thật vậy, điều này là hệ quả của Mệnh đề 30.24. Do đó, ta chỉ có để tìm bất kỳ đa thức của bậc $\le m$. Xét sau đây so-called Lagrange các đa thức:
$$(X -\alpha_{1} ) \cdots  (X -\alpha_{i-1} )(X -\alpha_{i+1} ) \cdots  (X -\alpha_{m+1} )$$
$$L_{i}(X) =.$$
$$(\alpha_{i}  -\alpha_{1} ) \cdots  (\alpha_{i}  -\alpha_{i-1} )(\alpha_{i}  -\alpha_{i+1} ) \cdots  (\alpha_{i}  -\alpha_{m+1} )$$
Lưu ý rằng $L(\alpha_{i}$) $= 1$ và rằng $L(\alpha_{j}$) $= 0$, với mọi $j \neq  i$. Nhưng khi đó,
$$P(X) = \beta_{1} L_{1} + \cdots  + \beta_{m+1} L_{m+1}$$

<!-- PAGE 1096 -->
Là duy nhất mong muốn đa thức, vì rõ ràng, $P(\alpha_{i}$) $= \beta_{i}$. Như vậy đa thức được gọi là một Lagrange interpolant. Cũng lưu ý rằng các đa thức $(L_{1}, \dots  , L_{m+1})$ tạo thành cơ sở (basis) của không gian vectơ (vector space) của tất cả các đa thức của bậc $\le m$. Thật vậy, nếu ta đã có
$$\lambda_{1} L_{1}(X) + \cdots  + \lambda_{m+1} L_{m+1}(X) = 0,$$
Đặt $X$ đến $\alpha_{i}$, ta sẽ thu được $\lambda_{i}  = 0$. Do đó, $L_{i}$ là độc lập tuyến tính (linearly independent), và bởi trước đó lập luận, chúng là tập hợp của các phần tử sinh. Ta ta gọi $(L_{1}, \dots  , L_{m+1})$ Lagrange cơ sở (basis) (của thứ tự $m + 1)$. Nó là đã biết từ số giải tích/phân tích rằng từ tính toán điểm của quan điểm, Lagrange cơ sở (basis) là không rất tốt. Newton proposed một cái khác nghiệm, phương pháp của được chia differences. Xét đa thức P(X) của bậc $\le m$, được gọi là Newton interpolant, P(X) $= \lambda_{0}  + \lambda_{1} (X$ - $\alpha_{1}$) $+ \lambda_{2} (X$ - $\alpha_{1} )(X$ - $\alpha_{2}$) $+ \cdots  + \lambda_{m} (X$ - $\alpha_{1} )(X$ - $\alpha_{2}$) $\cdots  (X$ - $\alpha_{m}$). Thì, $\lambda_{i}$ có thể được được xác định bởi successively đặt $X$ đến, $\alpha_{1} , \alpha_{2} , \dots  , \alpha_{m+1}$. Chính xác hơn, ta định nghĩa một cách quy nạp các đa thức Q(X) và $Q(\alpha_{1} , \dots  , \alpha_{i} , X)$, cho $1 \le i \le m$, như sau:
$$Q(X) = P(X)$$
$$Q_{1}(\alpha_{1} , X) = \frac{Q(X)Q(\alpha_{1} )}{X-\alpha_{1}} -$$
$$-$$
$$Q(\alpha_{1} , \alpha_{2} , X) = \frac{Q(\alpha_{1} , X)Q(\alpha_{1} , \alpha_{2} )}{X-\alpha_{2}}$$
$$\dots$$
$$Q(\alpha_{1} , \dots  , \alpha_{i} , X) = \frac{Q(\alpha_{1} , \dots  , \alpha_{i-1} , X)Q(\alpha_{1} , \dots  , \alpha_{i-1} , \alpha_{i} )}{X-\alpha_{i}} -,$$
$$\dots$$
$$-$$
$$Q(\alpha_{1} , \dots  , \alpha_{m} , X) = \frac{Q(\alpha_{1} , \dots  , \alpha_{m-1} , X)Q(\alpha_{1} , \dots  , \alpha_{m-1} , \alpha_{m} )}{X-\alpha_{m}} .$$
Bằng quy nạp theo $i, 1 \le i \le m$ - $1$, dễ dàng kiểm chứng được rằng
$$Q(X) = P(X),$$
$$Q(\alpha_{1} , \dots  , \alpha_{i} , X) = \lambda_{i}  + \lambda_{i+1} (X -\alpha_{i+1} ) + \cdots  + \lambda_{m} (X -\alpha_{i+1} ) \cdots  (X -\alpha_{m} ),$$
$$Q(\alpha_{1} , \dots  , \alpha_{m} , X) = \lambda_{m} .$$
Từ ở trên các biểu thức, rõ ràng là
$$\lambda_{0}  = Q(\alpha_{1} ),$$
$$\lambda_{i}  = Q(\alpha_{1} , \dots  , \alpha_{i} , \alpha_{i+1} ),$$
$$\lambda_{m}  = Q(\alpha_{1} , \dots  , \alpha_{m} , \alpha_{m+1} ).$$

<!-- PAGE 1097 -->
Biểu thức $Q(\alpha_{1} , \alpha_{2} , \dots  , \alpha_{i+1}$) được gọi là thứ $i$ difference thương. Thì, ta có thể tính $\lambda_{i}$ theo $\beta_{1}  = P(\alpha_{1}$), $\dots  , \beta_{m+1}  = P(\alpha_{m+1}$), bằng cách sử dụng quy nạp các công thức cho $Q(\alpha_{1} , \dots  , \alpha_{i} , X)$ cho trước ở trên, initializing $Q(\alpha_{i}$) sao cho $Q(\alpha_{i}$) $= \beta_{i}$. ở trên phương pháp được gọi là phương pháp của được chia differences và nó là do Newton. astute nhận xét có thể được sử dụng đến optimize phép tính. Nhận thấy rằng nếu $P_{i}(X)$ là đa thức của bậc $\le i$ lấy các giá trị $\beta_{1} , \dots  , \beta_{i+1}$ tại các điểm $\alpha_{1} , \dots  , \alpha_{i+1}$, thì hệ số của $X^{i}$ trong $P_{i}(X)$ là $Q(\alpha_{1} , \alpha_{2} , \dots  , \alpha_{i+1}$), mà là giá trị của $\lambda_{i}$ trong Newton interpolant $P_{i}(X) = \lambda_{0}  + \lambda_{1} (X$ - $\alpha_{1}$) $+ \lambda_{2} (X$ - $\alpha_{1} )(X$ - $\alpha_{2}$) $+ \cdots  + \lambda_{i} (X$ - $\alpha_{1} )(X$ - $\alpha_{2}$) $\cdots  (X$ - $\alpha_{i}$). Hệ quả là, $Q(\alpha_{1} , \alpha_{2} , \dots  , \alpha_{i+1}$) không phụ thuộc vào cụ thể thứ tự của $\alpha_{j}$ và có tốt hơn các cách của việc tính toán nó. Ví dụ, $Q(\alpha_{1} , \alpha_{2} , \dots  , \alpha_{i+1}$) có thể được được tính bằng cách sử dụng
$$-$$
$$Q(\alpha_{1} , \dots  , \alpha_{i+1} ) = \frac{Q(\alpha_{2} , \dots  , \alpha_{i+1} )Q(\alpha_{1} , \dots  , \alpha_{i} )}{\alpha_{i+1}  -\alpha_{1}} .$$
Thì, phép tính có thể được arranged vào tam giác mảng (array) reminiscent của Pascal’s tam giác, như sau: một cách ban đầu, $Q(\alpha_{j}$) $= \beta_{j} , 1 \le j \le m + 1$, và
$$Q(\alpha_{1} )$$
$$Q(\alpha_{1} , \alpha_{2} )$$
$$Q(\alpha_{2} )Q(\alpha_{1} , \alpha_{2} , \alpha_{3} )$$
$$Q(\alpha_{2} , \alpha_{3} )\dots$$
$$Q(\alpha_{3} )Q(\alpha_{2} , \alpha_{3} , \alpha_{4} )$$
$$Q(\alpha_{3} , \alpha_{4} )\dots$$
$$Q(\alpha_{4} )\dots$$
$$\dots$$
Trong điều này phép tính, mỗi successive cột là thu được bởi tạo thành difference các thương của preceeding cột theo công thức
$$Q(\alpha_{k} , \dots  , \alpha_{i+k} ) = \frac{Q(\alpha_{k+1} , \dots  , \alpha_{i+k} )Q(\alpha_{k} , \dots  , \alpha_{i+k-1} )}{\alpha_{i+k}  -\alpha_{k}} -.$$
$\lambda_{i}$ là các phần tử của descending đường chéo. Nhận thấy rằng nếu ta performed ở trên phép tính bắt đầu với đa thức Q(X) của bậc $m$, ta có thể mở rộng nó bởi xét mới cho trước các điểm $\alpha_{m+2} , \alpha_{m+3}$, etc. Thì, từ những gì ta đã thấy ở trên, $(m +$ 1)th cột bao gồm của $\lambda_{m}$ trong biểu thức của Q(X) như Newton interpolant và $(m +$ 2)th cột bao gồm của các không điểm. Như vậy được chia differences được sử dụng trong số giải tích/phân tích.

<!-- PAGE 1098 -->
Newton’s phương pháp có thể được được sử dụng để tính giá trị $P(\alpha$) tại một số $\alpha$ của interpolant P(X) lấy các giá trị $\beta_{1} , \dots  , \beta_{m+1}$ cho (phân biệt) các đối số/lập luận $\alpha_{1} , \dots  , \alpha_{m+1}$. Ta cũng mention rằng quy nạp các phương pháp cho việc tính toán $P(\alpha$) mà không có thứ nhất việc tính toán các hệ số của Newton interpolant tồn tại, ví dụ, Aitken’s phương pháp. Cho phương pháp này, độc giả là referred đến Farin $[59]$. Nó có đã được được quan sát rằng Lagrange interpolants oscillate khá một cách xấu như của chúng bậc tăng, và do đó, điều này làm cho chúng undesirable như stable phương pháp cho nội suy. tiêu chuẩn ví dụ do Runge, là hàm
$$f(x) = \frac{1}{1 + x^{2}} ,$$
Trong khoảng/đoạn $[-5, +5]$. Giả sử uniform distribution của các điểm trên đường cong trong khoảng/đoạn $[-5, +5]$, như bậc của Lagrange interpolant tăng, interpolant chỉ ra wilder và wilder oscillations xung quanh các điểm $x = -5$ và $x = +5$. Điều này hiện tượng trở thành khá noticeable bắt đầu cho bậc $14$, và thu được tệ hơn và tệ hơn. Cho bậc $22$, things là khá xấu! Tương đương, một có thể xét hàm
$$f(x) = \frac{1}{1 + 25x^{2}} ,$$
Trong khoảng/đoạn $[-1, +1]$. Ta bây giờ xét nhiều hơn/thêm tổng quát nội suy bài toán mà sẽ dẫn đến đến Hermite các đa thức. Ta xét sau đây nội suy bài toán: Cho trước dãy $(\alpha_{1} , \dots  , \alpha_{m+1}$) của đôi một phân biệt các vô hướng trong $K$, các số nguyên $n_{1}, \dots  , n_{m+1}$ ở đâu $n_{j} \ge 0$, và $m + 1$ các dãy $(\beta_{j}^{0}  , \dots  , \beta_{j}^{nj}$) của các vô hướng trong $K$, đặt
$$n = n_{1} + \cdots  + n_{m+1} + m,$$
Tìm đa thức $P$ của bậc $\le n$, sao cho
$$P(\alpha_{1} ) = \beta_{1}^{0} ,\dots P(\alpha_{m+1} ) = \beta_{m+1}^{0} ,$$
$$D^{1}P(\alpha_{1} ) = \beta_{1}^{1} ,\dots D^{1}P(\alpha_{m+1} ) = \beta_{m+1}^{1} ,$$
$$\dots$$
$$D^{i}P(\alpha_{1} ) = \beta_{1}^{i} ,\dots D^{i}P(\alpha_{m+1} ) = \beta_{m+1}^{i} ,$$
$$\dots$$
$$D^{n1}P(\alpha_{1} ) = \beta_{1}^{n1}  ,\dots D^{nm+1}P(\alpha_{m+1} ) = \beta_{m+1}^{nm+1}  .$$
Lưu ý rằng ở trên các phương trình constitute $n + 1$ các ràng buộc, và do đó, ta có thể kỳ vọng rằng tồn tại duy nhất một đa thức của bậc $\le n$ thỏa mãn ở trên bài toán. Điều này là thật vậy trường hợp và như vậy đa thức được gọi là một Hermite đa thức. Ta gọi ở trên bài toán Hermite nội suy bài toán.

<!-- PAGE 1099 -->

> **Mệnh đề 30.29.** Hermite nội suy bài toán có duy nhất nghiệm của bậc $\le n$, ở đâu $n = n_{1} + \cdots  + n_{m+1} + m$.

*Chứng minh.* Thứ nhất, ta chứng minh rằng Hermite nội suy bài toán có nhiều nhất một nghiệm. Giả sử rằng $P$ và $Q$ là hai phân biệt các nghiệm của bậc $\le n$. Thì, theo Mệnh đề 30.26 và tiêu chuẩn sau đây nó, $P -Q$ có trong số của nó các nghiệm $\alpha_{1}$ của bội (multiplicity) ít nhất $n_{1}+1, \dots , \alpha_{m+1}$ của bội (multiplicity) ít nhất $n_{m+1} + 1$. Tuy nhiên, theo Định lý 30.23, ta nên có
$$n_{1} + 1 + \cdots  + n_{m+1} + 1 = n_{1} + \cdots  + n_{m+1} + m + 1 \le n,$$
Điều này dẫn đến mâu thuẫn, vì $n = n_{1} + \cdots  + n_{m+1} + m$. Do đó, $P = Q$. Ta là trái với chứng minh sự tồn tại của Hermite interpolant. quick cách đến thực hiện do đó là để sử dụng Mệnh đề 7.12, mà cho ta biết chúng ta rằng cho trước ma trận vuông (square matrix) $A$ trên trường $K$, các tính chất sau đây đúng: Với mọi vectơ cột (column vector) $B$, tồn tại duy nhất một vectơ cột (column vector) $X$ sao cho $AX = B$ khi và chỉ khi chỉ nghiệm đến $AX = 0$ là tầm thường vectơ $X = 0$ khi và chỉ khi D() $\neq  0$. Nếu ta cho $P = y_{0} + y_{1}X + \cdots  + y_{n}X^{n}$, Hermite nội suy bài toán cho ta hệ phương trình tuyến tính của các phương trình trong unknowns $(y_{0}, \dots  , y_{n})$ với một số liên kết $(n+1)\times (n+1)$ ma trận $A$. Bây giờ, hệ $AY = 0$ có nghiệm khi và chỉ khi $P$ có trong số của nó các nghiệm $\alpha_{1}$ của bội (multiplicity) ít nhất $n_{1} + 1, \dots , \alpha_{m+1}$ của bội (multiplicity) ít nhất $n_{m+1} + 1$. Bởi trước đó lập luận, vì $P$ có bậc $\le n$, ta phải có $P = 0$, nghĩa là, $Y = 0$. Điều này kết luận chứng minh. Mệnh đề 30.29 chỉ ra sự tồn tại của duy nhất các đa thức $H_{j}^{i}(X)$ của bậc $\le n$ sao cho $D^{i}H_{j}^{i}(\alpha_{j}$) $= 1$ và $D^{k}H_{j}^{i}(\alpha_{l}$) $= 0$, cho $k \neq  i$ hoặc $l \neq  j, 1 \le j, l \le m + 1, 0 \le i, k \le n_{j}$. các đa thức $H_{j}^{i}$ được gọi là Hermite cơ sở (basis) các đa thức. Một bài toán với Mệnh đề 30.29 là rằng nó thực hiện không cho tường minh cách của việc tính toán Hermite cơ sở (basis) các đa thức. Ta thứ nhất chỉ ra rằng điều này có thể được được thực hiện một cách tường minh trong đặc biệt các trường hợp $n_{1} = \dots  = n_{m+1} = 1$, và $n_{1} = \dots  = n_{m+1} = 2$, và thì suggest phương pháp bằng cách sử dụng suy rộng/tổng quát hóa Newton interpolant. Giả sử rằng $n_{1} = \dots  = n_{m+1} = 1$. Ta thử $H_{j}^{0} =$ ((X - $\alpha_{j}$) $+ b)L_{j}^{2}$, và $H_{j}^{1} =$ (c(X - $\alpha_{j}$) $+ d)L_{j}^{2}$, ở đâu $L_{j}$ là Lagrange interpolant được xác định trước đó. Vì
$$DH_{j}^{0} = aL_{j}^{2} + 2(a(X -\alpha_{j} ) + b)L_{j}DL_{j},$$
Đòi hỏi rằng $H_{j}^{0} (\alpha_{j}$) $= 1, H_{j}^{0} (\alpha_{k}$) $= 0, DH_{j}^{0} (\alpha_{j}$) $= 0$, và $DH_{j}^{0} (\alpha_{k}$) $= 0$, cho $k \neq  j$, suy ra $b = 1$ và $a = -2DL_{j}(\alpha_{j}$). Tương tự, từ requirements $H_{j}^{1} (\alpha_{j}$) $= 0, H_{j}^{1} (\alpha_{k}$) $= 0, DH_{j}^{1} (\alpha_{j}$) $= 1$, và $DH_{j}^{1} (\alpha_{k}$) $= 0, k \neq  j$, ta thu được $c = 1$ và $d = 0$. Do đó, ta có Hermite các đa thức
$$H_{j}^{0} = (1 -2DL_{j}(\alpha_{j} )(X -\alpha_{j} ))L_{j}^{2},H_{j}^{1} = (X -\alpha_{j} )L_{j}^{2}.$$

<!-- PAGE 1100 -->
Trong trường hợp đặc biệt khi $m = 1, \alpha_{1}  = 0$, và $\alpha_{2}  = 1$, ta để lại như một bài tập để chỉ ra rằng Hermite các đa thức là
$$- + 1$$
$$H_{0}^{0} = 2X^{3}3X^{2},$$
$$+ 3$$
$$H_{1}^{0} = -2X^{3}X^{2},$$
$$- +$$
$$H_{0}^{1} = X^{3}2X^{2} X,$$
$$-$$
$$H_{1}^{1} = X^{3}X^{2}.$$
Hệ quả là, đa thức $P$ của bậc $3$ sao cho P(0) $= x_{0}$, P(1) $= x_{1}$, P' $(0) = m_{0}$, và P' $(1) = m_{1}$, có thể được viết dưới dạng P(X) $= x_{0}(2X^{3}$ - $3X^{2} + 1) + m_{0}(X^{3}$ - $2X^{2} + X) + m_{1}(X^{3}$ - $X^{2}) + x_{1}(-2X^{3} + 3X^{2})$. Nếu ta muốn đa thức $P$ của bậc $3$ sao cho P() $= x_{0}$, P(b) $= x_{1}$, P' $(a) = m_{0}$, và P' $(b) = m_{1}$, ở đâu $b \neq$, thì ta có P(X) $= x_{0}(2t^{3}$ - $3t^{2} + 1) + (b$ - $a)m_{0}(t^{3}$ - $2t^{2} + t) + (b$ - $a)m_{1}(t^{3}$ - $t^{2}) + x_{1}(-2t^{3} + 3t^{2})$, ở đâu
$$t = \frac{Xa}{b -a} - .$$
Quan sát presence của extra nhân tử $(b$ - $a)$ trong trước của $m_{0}$ và $m_{1}$, công thức sẽ là sai ngược lại! Ta bây giờ xét trường hợp ở đâu $n_{1} = \dots  = n_{m+1} = 2$. Cho chúng ta thử
$$+$$
$$H_{j}^{i}(X) = (a^{i}(X -\alpha_{j} )^{2} b^{i}(X -\alpha_{j} ) + c^{i})L_{j}^{3},$$
Ở đâu $0 \le i \le 2$. Sparing độc giả một số (tẻ nhạt/dài dòng) các phép tính, ta tìm:
$$H_{j}^{0} (X) = \begin{pmatrix}   & 3 \\ 6(DL_{j}(\alpha_{j} ))^{2}- & D^{2}L_{j}(\alpha_{j} ) \\ 2 \\ 9(DL_{j}(\alpha_{j} ))^{2}(X & \alpha_{j} )^{2} & 3D \end{pmatrix} \begin{pmatrix} (X-\alpha_{j} )^{2}-3DL_{j}(\alpha_{j} )(X-\alpha_{j} ) + 1 \end{pmatrix} L_{j}^{3}(X),$$
$$H_{j}^{1} (X) = \begin{pmatrix} - & - & L_{j}(\alpha_{j} )(X-\alpha_{j} ) \end{pmatrix} L_{j}^{3}(X),$$
$$H_{j}^{2} (X) = \frac{1}{2} (X -\alpha_{j} )^{2}L_{j}^{3}(X).$$
Đi quay lại đến tổng quát bài toán, nó dường như đến chúng ta rằng loại của Newton interpolant sẽ là nhiều hơn/thêm manageable. Cho $P_{0}^{0}  (X) = 1, \cdots P_{j}^{0} (X) = (X$ - $\alpha_{1} )^{n1+1}  (X$ - $\alpha_{j} )^{nj+1}, 1 \le j \le m \cdots P_{0}^{i}(X) = (X$ - $\alpha_{1} )^{i}(X$ - $\alpha_{2} )^{n2+1}  (X$ - $\alpha_{m+1} )^{nm+1+1}, 1 \le i \le n_{1}, \cdots  \cdots P_{j}^{i}(X) = (X$ - $\alpha_{1} )^{n1+1}  (X$ - $\alpha_{j} )^{nj+1}(X$ - $\alpha_{j+1} )^{i}(X$ - $\alpha_{j+2} )^{nj+2+1}  (X$ - $\alpha_{m+1} )^{nm+1+1}$,
$$1 \le j \le m -1, 1 \le i \le n_{j+1},$$
$\cdots P_{m}^{i}(X) = (X$ - $\alpha_{1} )^{n1+1}  (X$ - $\alpha_{m} )^{nm+1}(X$ - $\alpha_{m+1} )^{i}, 1 \le i \le n_{m+1}$,

<!-- PAGE 1101 -->
Và cho
$$j=j+1$$
$$P(X) = \sum_{=0,i=0}^{m,i=n}  \lambda_{j}^{i} P_{j}^{i}(X).$$
$$j$$
Ta có thể nghĩ của P(X) như suy rộng/tổng quát hóa Newton interpolant. Ta có thể tính các đạo hàm $D^{k}P_{j}^{i}$, cho $1 \le k \le n_{j+1}$, và nếu ta nhìn cho Hermite cơ sở (basis) các đa thức $H_{j}^{i}(X)$ sao cho $D^{i}H_{j}^{i}(\alpha_{j}$) $= 1$ và $D^{k}H_{j}^{i}(\alpha_{l}$) $= 0$, cho $k \neq  i$ hoặc $l \neq  j, 1 \le j, l \le m + 1, 0 \le i, k \le n_{j}$, ta tìm rằng ta có để giải tam giác các hệ của các phương trình tuyến tính. Do đó, như trong đơn giản trường hợp $n_{1} = \dots  = n_{m+1} = 0$, ta có thể giải successively cho $\lambda_{j}^{i}$. Hiển nhiên, các phép tính là khá formidable và ta để lại như vậy considerations cho further study.

<!-- PAGE 1102 -->
