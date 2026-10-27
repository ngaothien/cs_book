# Các không gian vectơ


<!-- PAGE 69 -->
Trên tất cả các ma trận ' của hạng (rank) nhiều nhất $k$, với một số cho trước $k \ll min{m, n}$. Một số advantages của hạng thấp (low-rank) xấp xỉ là: $1$. Fewer các phần tử là cần thiết để biểu diễn $A$; cụ thể là, k(m $+ n)$ thay vì của mn. Do đó ít hơn storage và fewer các phép toán là cần thiết đến reconstruct $A. 2$. Thường, process cho thu được phân rã exposes underlying cấu trúc của dữ liệu. Do đó, nó có thể turn ra rằng “hầu hết” của đáng kể dữ liệu là concentrated dọc theo một số các hướng được gọi là chính các hướng. Hạng thấp (low-rank) các phân rã của tập hợp của dữ liệu có multitude của các ứng dụng trong kỹ thuật, bao gồm cả máy tính khoa học (especially máy tính thị giác), statistics, và máy học (learning). Như ta sẽ xem sau này trong Chương $23$, phân rã giá trị kỳ dị (SVD) (SVD) cung cấp rất satisfactory nghiệm đến hạng thấp (low-rank) xấp xỉ bài toán. Vẫn, trong nhiều các trường hợp, dữ liệu các tập hợp là do đó lớn rằng một cái khác ingredient là cần thiết: randomization. Tuy nhiên, như bước thứ nhất, tuyến tính đại số thường cho ta tốt ban đầu nghiệm. Ta sẽ bây giờ là nhiều hơn/thêm precise như đến những gì các loại của các phép toán được phép trên các vectơ. Trong late 1880’s, khái niệm của không gian vectơ (vector space) emerged như thuận tiện và unifying khung lý thuyết cho làm việc với “tuyến tính” objects. axiomatic định nghĩa của các không gian vectơ đã là thứ nhất cho trước bởi Peano trong $1888$ và đã là anticipated bởi Grassmann.

## 3.2 Các không gian vectơ

$$\mathbb{R}^{n}$$
Với mọi $n \ge 1$, cho là tập hợp của các bộ $n$ $x = (x_{1}, \dots  , x_{n})$. Phép cộng có thể được được mở rộng đến $\mathbb{R}^{n}$ như sau: $(x_{1}, \dots  , x_{n}) + (y_{1}, \dots  , y_{n}) = (x_{1} + y_{1}, \dots  , x_{n} + y_{n})$.
$$\mathbb{R}\mathbb{R}^{n} \mathbb{R}^{n}$$
Ta có thể cũng định nghĩa phép toán $\cdot$: $\times \to$ như sau: $\lambda  \cdot  (x_{1}, \dots  , x_{n}) = (\lambda x_{1}, \dots  , \lambda x_{n})$. thu được đại số cấu trúc có một số thú vị các tính chất, những phần tử đó của không gian vectơ (vector space). Tuy nhiên, giữ trong mind rằng các không gian vectơ là không chỉ đại số
$$objects; they are also geometric objects.$$
Các không gian vectơ được định nghĩa như sau.

> **Định nghĩa 3.1.** Cho trước trường $K$ (với phép cộng $+$ và phép nhân *), không gian vectơ (vector space) trên $K$ (hoặc vectơ $K$ không gian) là tập hợp $E$ (của các vectơ) cùng với hai các phép toán $+_{E}$: $E \times  E \to E$ (được gọi là vectơ phép cộng),và $\cdot_{E}$: $K \times  E \to E$ (được gọi là vô hướng (scalar) phép nhân) thỏa mãn sau đây các điều kiện với mọi $\alpha , \beta  \in K$ và tất cả $u, v \in E$;
(V0) $E$ là nhóm Abel (abelian group) w.r.t. $+_{E}$, với phần tử đơn vị (identity element) $0_{E}$;

<!-- PAGE 70 -->
(V1) $\alpha  \cdot_{E}  (u +_{E} v) = (\alpha  \cdot_{E}  u) +_{E} (\alpha  \cdot_{E}  v)$;
(V2) $(\alpha  + \beta$) $\cdot_{E}  u = (\alpha  \cdot_{E}  u) +_{E} (\beta  \cdot_{E}  u)$;
(V3) $(\alpha$ * $\beta$) $\cdot_{E}  u = \alpha  \cdot_{E}  (\beta  \cdot_{E}  u)$;
(V4) $1 \cdot_{E}  u = u$. Trong (V1), $+$ ký hiệu phép cộng trong trường $K$, và trong (V3), * ký hiệu phép nhân trong $K$. Cho trước $\alpha , \beta  \in K$ và $v \in E$, để đơn giản của ký hiệu, phần tử $\alpha  \cdot_{E}  v$ được ký hiệu bởi $\alpha v$ và $\alpha$ * $\beta$ bởi $\alpha \beta$. trường $K$ là thường được gọi là trường của các vô hướng. Trừ khi specified ngược lại hoặc trừ khi ta là dealing với một vài khác nhau các trường, trong rest của điều này chương, ta giả sử rằng tất cả vectơ $K$ các không gian được định nghĩa đối với cố định trường $K$. Do đó, ta sẽ refer đến vectơ $K$ không gian đơn giản như không gian vectơ (vector space). Trong hầu hết các trường hợp, trường $K$ sẽ là trường $\mathbb{R}$ của các số thực. Từ (V0), không gian vectơ (vector space) luôn luôn chứa null vectơ $0_{E}$, và do đó là khác rỗng. Từ (V1), ta thu được $\alpha  \cdot_{E}  0_{E} = 0_{E}$, và $\alpha  \cdot_{E}  (-_{E}v) = -_{E}(\alpha  \cdot_{E}  v)$. Từ (V2), ta thu được $0 \cdot_{E}  v = 0_{E}$, và $(-\alpha$) $\cdot_{E}  v = -_{E}(\alpha  \cdot_{E}  v)$. Một cái khác quan trọng hệ quả của axioms là sau đây sự kiện:

> **Mệnh đề 3.1.** Với mọi $u \in E$ và bất kỳ $\lambda  \in K$, nếu $\lambda  \neq  0$ và $\lambda  \cdot_{E}  u = 0_{E}$, thì $u = 0_{E}$.

*Chứng minh.* Thật vậy, vì $\lambda  \neq  0$, nó có multiplicative nghịch đảo $\lambda^{-1}$, do đó từ $\lambda  \cdot_{E}  u = 0_{E}$, ta thu được
$$\lambda^{-1} \cdot_{E}  (\lambda  \cdot_{E}  u) = \lambda^{-1} \cdot_{E}  0_{E}.$$
Tuy nhiên, ta chỉ được quan sát rằng $\lambda^{-1} \cdot_{E}  0_{E} = 0_{E}$, và từ (V3) và (V4), ta có
$$\lambda^{-1} \cdot_{E}  (\lambda  \cdot_{E}  u) = (\lambda^{-1} \lambda ) \cdot_{E}  u = 1 \cdot_{E}  u = u,$$
Và ta suy ra rằng $u = 0_{E}$.
Nhận xét: Một có thể tự hỏi liệu axiom (V4) là một cách thực cần thiết. Có thể nó là derived từ
$$\mathbb{R}^{n}$$
Khác axioms? câu trả lời là không có. Ví dụ, một có thể lấy $E =$ và định nghĩa $\mathbb{R} \mathbb{R}^{n} \mathbb{R}^{n} \cdot$: $\times \to$ bởi
$$\lambda  \cdot  (x_{1}, \dots  , x_{n}) = (0, \dots  , 0)$$
$$\mathbb{R}^{n} \mathbb{R}$$
Với mọi $(x_{1}, \dots  , x_{n}) \in$ và tất cả $\lambda  \in$. Axioms (V0)–(V3) là tất cả được thỏa mãn, nhưng (V4) không thỏa mãn. Ít hơn tầm thường các ví dụ có thể được cho trước bằng cách sử dụng khái niệm của cơ sở (basis), mà có không đã được được định nghĩa vẫn chưa. trường $K$ chính nó có thể được được quan điểm như không gian vectơ (vector space) trên chính nó, phép cộng của các vectơ đang là phép cộng trong trường, và phép nhân bởi vô hướng (scalar) đang là phép nhân trong trường.

<!-- PAGE 71 -->
Một quickly realizes rằng mặc dù nó là của course quan trọng đến distinguish giữa phép cộng $+_{E}$ trong $E$ với phép cộng $+$ trong trường $K$, không vectơ $0_{E}$ trong $E$ với không $0$ trong trường, và phép nhân $\cdot_{E}$ bởi vô hướng (scalar) (trong trường $K)$ với phép nhân * (hoặc $\cdot$) trong trường, bằng cách sử dụng tất cả các phần tử này các chỉ số dưới trở thành notational burden. Do đó, trừ khi confusion có thể phát sinh, ta ký hiệu phép cộng trong $E$ và $K$ bởi cùng ký hiệu $+$, không trong $E$ và trong $K$ bởi $0$, và vô hướng (scalar) phép nhân bởi $\cdot$ (ta chẵn/ngay cả viết $\alpha u$ thay vì của $\alpha  \cdot u)$. Systematic sử dụng của khác nhau các ký hiệu cho ký hiệu các vô hướng (nói $\alpha , \beta , \gamma , \delta , \lambda$) và các vectơ nói $(u, v, x, y, z)$ là thường đủ để tránh confusion. để tránh confusing không trong $E$ và không trong $K$, ta có thể sử dụng $0$ cho không vectơ.

> **Ví dụ 3.1.** $1$. các trường $\mathbb{R}$ và $\mathbb{C}$ là các không gian vectơ trên $\mathbb{R}$.
$$\mathbb{R}^{n}  \mathbb{C}^{n}  \mathbb{R}$$
$2$. các nhóm và là các không gian vectơ trên, với vô hướng (scalar) phép nhân cho trước bởi
$$\lambda (x_{1}, \dots  , x_{n}) = (\lambda x_{1}, \dots  , \lambda x_{n}),$$
$$\mathbb{R}\mathbb{R}^{n} \mathbb{C}^{n} \mathbb{C}^{n}$$
Với mọi $\lambda  \in$ và với $(x_{1}, \dots  , x_{n}) \in$ hoặc $(x_{1}, \dots  , x_{n}) \in$, và là không gian vectơ (vector space) trên $\mathbb{C}$ với vô hướng (scalar) phép nhân như ở trên, nhưng với $\lambda  \in \mathbb{C}. 3$. vành $\mathbb{R}[X]_{n}$ của các đa thức của bậc nhiều nhất $n$ với thực các hệ số là không gian vectơ (vector space) trên $\mathbb{R}$, và vành $\mathbb{C}[X]_{n}$ của các đa thức của bậc nhiều nhất $n$ với phức các hệ số là không gian vectơ (vector space) $over\mathbb{C}$, với vô hướng (scalar) phép nhân $\lambda \cdot$ P(X) của đa thức
$$P(X) = a_{0}X^{m}+ a_{1}X^{m-1}+ \cdots  + a_{m-1}X + a_{m}$$
(với $a_{i} \in \mathbb{R}$ hoặc $a_{i} \in \mathbb{C})$ bởi vô hướng (scalar) $\lambda$ (trong $\mathbb{R}$ hoặc $\mathbb{C})$, với $m \le n$, cho trước bởi
$$\lambda  \cdot  P(X) = \lambda a_{0}X^{m}+ \lambda a_{1}X^{m-1}+ \cdots  + \lambda a_{m-1}X + \lambda a_{m}.$$
$4$. $ring\mathbb{R}[X]$ của tất cả các đa thức với thực các hệ số là không gian vectơ (vector space) $over\mathbb{R}$, và vành $\mathbb{C}[X]$ của tất cả các đa thức với phức các hệ số là không gian vectơ (vector space) trên $\mathbb{C}$, với cùng vô hướng (scalar) phép nhân như ở trên. $5$. vành của $n \times  n$ các ma trận $M_{n}(\mathbb{R})$ là không gian vectơ (vector space) trên $\mathbb{R}. 6$. tập hợp của $m \times  n$ các ma trận $M_{m,n}(\mathbb{R})$ là không gian vectơ (vector space) trên $\mathbb{R}. 7$. vành $\mathcal{C}(a, b)$ của liên tục các hàm $f$: (, $b) \to \mathbb{R}$ là không gian vectơ (vector space) trên $\mathbb{R}$, với vô hướng (scalar) phép nhân $\lambda f$ của hàm $f$: (, $b) \to \mathbb{R}$ bởi vô hướng (scalar) $\lambda  \in \mathbb{R}$ cho trước bởi
$$(\lambda f)(x) = \lambda f(x),for all x \in (a, b).$$
