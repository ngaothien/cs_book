# Các họ có chỉ số; Tổng Ký hiệu i I ai


<!-- PAGE 72 -->
$8$. rất quan trọng ví dụ của không gian vectơ (vector space) là tập hợp của các ánh xạ tuyến tính (linear maps) giữa hai các không gian vectơ được định nghĩa trong Mục 11.1. Đây là một ví dụ rằng sẽ prepare chúng ta cho không gian vectơ (vector space) của các ánh xạ tuyến tính (linear maps). Cho $X$ là bất kỳ khác rỗng tập hợp và cho $E$ là không gian vectơ (vector space). Tập hợp tất cả các hàm $f$: $X \to E$ có thể được được tạo vào không gian vectơ (vector space) như sau: Cho trước bất kỳ hai các hàm $f$: $X \to E$ và $g: X \to E$, cho $(f + g): X \to E$ được định nghĩa sao cho
$$(f + g)(x) = f(x) + g(x)$$
Với mọi $x \in X$, và với mọi $\lambda  \in \mathbb{R}$, cho $\lambda f$: $X \to E$ được định nghĩa sao cho
$$(\lambda f)(x) = \lambda f(x)$$
Với mọi $x \in X$. axioms của không gian vectơ (vector space) là dễ dàng được kiểm chứng. Cho $E$ là không gian vectơ (vector space). Ta sẽ like để định nghĩa quan trọng các khái niệm của tổ hợp tuyến tính (linear combination) và sự độc lập tuyến tính (linear independence). Trước định nghĩa các phần tử này các khái niệm, ta cần đến thảo luận strategic lựa chọn mà, tùy thuộc cách mà nó là settled, có thể rút gọn hoặc tăng headaches trong dealing với các khái niệm chẳng hạn như các tổ hợp tuyến tính và sự phụ thuộc tuyến tính (linear dependence) (hoặc independence). vấn đề có đến thực hiện với bằng cách sử dụng các tập hợp của các vectơ versus các dãy của các vectơ.
$$3.3Indexed Families; the Sum Notation \sum  i\in I ai$$
Của ta experience cho ta biết chúng ta rằng nó được ưu tiên hơn để sử dụng các dãy của các vectơ; chẵn/ngay cả tốt hơn, các họ có chỉ số của các vectơ. (Ta là không alone trong có opted cho các dãy trên các tập hợp, và ta là trong tốt company; ví dụ, Artin $[7]$, Axler $[10]$, và Lang $[113]$ sử dụng các dãy. Tuy nhiên, một số prominent các tác giả chẳng hạn như Lax $[117]$ sử dụng các tập hợp. Ta để lại nó đến độc giả đến conduct survey trên điều này vấn đề.) Cho trước tập hợp $A$, nhắc lại rằng dãy được thứ tự bộ $n$ $(a_{1}, \dots  , a_{n}) \in A^{n}$ của các phần tử từ $A$, với một số tự nhiên số $n$. các phần tử của dãy cần không là phân biệt và thứ tự là quan trọng. Ví dụ, $(a_{1}, a_{2}, a_{1})$ và $(a_{2}, a_{1}, a_{1})$ là hai phân biệt các dãy trong $A^{3}$. Của chúng underlying tập hợp là ${a_{1}, a_{2}}$. Những gì ta chỉ được định nghĩa là hữu hạn các dãy, mà có thể cũng được quan điểm như các hàm từ ${1, 2, \dots  , n}$ đến tập hợp $A$; phần tử thứ $i$ của dãy $(a_{1}, \dots  , a_{n})$ là ảnh (image) của $i$ dưới hàm. Điều này viewpoint là fruitful, bởi vì nó cho phép chúng ta để định nghĩa (countably) vô hạn các dãy như các hàm $s: \mathbb{N} \to A$. Nhưng khi đó, tại sao giới hạn chính chúng ta đến được thứ tự các tập hợp chẳng hạn như ${1, \dots  , n}$ hoặc $\mathbb{N}$ như chỉ số các tập hợp? chính vai trò của chỉ số tập hợp là đến nhãn mỗi phần tử một cách duy nhất, và thứ tự của các nhãn là không then chốt, mặc dù thuận tiện. Do đó, nó là tự nhiên để định nghĩa khái niệm của họ có chỉ số (indexed family).

<!-- PAGE 73 -->
$$A_{I}$$
$$I\in I$$

> **Định nghĩa 3.2.** Cho trước tập hợp $A$, I-họ có chỉ số (indexed family) của các phần tử của $A$, cho ngắn họ, là hàm: I $\to A$ ở đâu I là bất kỳ tập hợp được quan điểm như chỉ số tập hợp. Vì hàm được xác định bởi của nó đồ thị
$${(i, a(i)) | i \in I},$$
Họ có thể được được quan điểm như tập hợp của các cặp $a = {(i$, (i)) | $i \in I}$. Cho notational simplicity, ta viết $a_{i}$ thay vì của (i), và ký hiệu họ $a = {(i$, (i)) | $i \in I}$ bởi $(a_{i})_{i\in I}$. Ví dụ, nếu $I = {r, g, b, y}$ và $A =\mathbb{N}$, tập hợp của các cặp
$$a = {(r, 2), (g, 3), (b, 2), (y, 11)}$$
Là họ có chỉ số (indexed family). phần tử $2$ xuất hiện hai lần trong họ với hai phân biệt các nhãn $r$ và $b$. Khi được chỉ số tập hợp $I$ là một cách tổng được thứ tự, họ $(a_{i})_{i\in I}$ là thường được gọi là I-sequence. một cách thú vị, các tập hợp có thể được được quan điểm như đặc biệt các trường hợp của các họ. Thật vậy, tập hợp $A$ có thể được được quan điểm như -họ có chỉ số (indexed family) ${(a$,) | $a \in I}$ tương ứng với đồng nhất thức hàm.
Nhận xét: họ có chỉ số (indexed family) nên không là confused với đa tập hợp (multiset). Cho trước bất kỳ tập hợp $A$, đa tập hợp (multiset) là đồng dạng đến tập hợp, ngoại trừ rằng các phần tử của $A$ có thể xảy ra nhiều hơn một lần. Ví dụ, nếu $A = {a, b, c, d}$, thì ${a$,,, $b, c, c, d, d}$ là đa tập hợp (multiset). Mỗi phần tử xuất hiện với nhất định bội (multiplicity), nhưng thứ tự của các phần tử thực hiện không matter. Ví dụ, có bội (multiplicity) $3$. một cách hình thức, đa tập hợp (multiset) là hàm $s: A \to \mathbb{N}$, hoặc tương đương tập hợp của các cặp ${(a, i)$ | $a \in A}$. Do đó, đa tập hợp (multiset) là -họ có chỉ số (indexed family) của các phần tử từ $\mathbb{N}$, nhưng không $a \mathbb{N}-indexed$ họ, vì phân biệt các phần tử có thể có cùng bội (multiplicity) (chẳng hạn như $c$ $d$ trong ví dụ ở trên). họ có chỉ số (indexed family) là tổng quát hóa của dãy, nhưng đa tập hợp (multiset) là tổng quát hóa của tập hợp. Ta cũng cần đến lấy care của annoying technicality, mà là để định nghĩa các tổng của
$$form \sum_{i}  \in I a_{i}, where I is any finite index set and (a_{i})_{i\in I} is a family of elements in some set$$
Equiped với nhị phân phép toán $+: A \times  A \to A$ mà là kết hợp (Axiom (G1)) và giao hoán. Điều này sẽ đến lên khi ta định nghĩa các tổ hợp tuyến tính. vấn đề là rằng nhị phân phép toán $+$ chỉ cho ta biết chúng ta cách mà để tính $a_{1} + a_{2}$ cho hai các phần tử của $A$, nhưng nó thực hiện không cho biết chúng ta những gì là tổng của ba của nhiều hơn/thêm các phần tử. Ví dụ, cách mà nên $a_{1} + a_{2} + a_{3}$ được định nghĩa? Những gì ta có đến thực hiện là để định nghĩa $a_{1}+a_{2}+a_{3}$ bằng cách sử dụng dãy của các bước mỗi liên quan đến hai các phần tử, và có hai khả dĩ/có thể các cách đến thực hiện điều này: $a_{1} +(a_{2} +a_{3})$ và $(a_{1} +a_{2})+a_{3}$. Nếu của ta phép toán $+$ là không kết hợp, các phần tử này là khác nhau các giá trị. Nếu nó kết hợp, thì $a_{1}+(a_{2}+a_{3}) = (a_{1} + a_{2}) + a_{3}$, nhưng khi đó có vẫn sáu khả dĩ/có thể các hoán vị của các chỉ số $1, 2, 3$, và nếu $+$ là không giao hoán, các giá trị này là một cách tổng quát khác nhau. Nếu của ta phép toán là giao hoán, thì tất cả sáu các hoán vị có cùng giá trị. Do đó, nếu $+$ là kết hợp và giao hoán,
$$it seems intuitively clear that a sum of the form \sum_{i}  \in I a_{i} does not depend on the order of the$$
Các phép toán được sử dụng để tính nó.

<!-- PAGE 74 -->
Điều này là thật vậy trường hợp, nhưng chặt chẽ chứng minh đòi hỏi quy nạp, và như vậy chứng minh là đáng ngạc nhiên là liên quan. Độc giả có thể accept mà không có chứng minh sự kiện rằng các tổng của tạo thành
$$\sum_{i}  a_{i} are indeed well defined, and jump directly to Definition 3.3. For those who want to$$
$see^{\in I}$ gory chi tiết, ở đây ta đi.
$$First, we define sums \sum_{i}  a_{i}, where I is a finite sequence of distinct natural numbers,$$
Nói $I = (i_{1}, \dots  , i_{m})$. Nếu $I = (^{\in I}i_{1}, \dots  , i_{m})$ với $m \ge 2$, ta ký hiệu dãy $(i_{2}, \dots  , i_{m})$ bởi I $-{i_{1}}$. Ta tiến hành bằng quy nạp theo kích thước $m$ của I. Cho
$$\sum_{i\in I}  a_{i} = a_{i1},if m = 1,$$
$$\sum_{i\in I}  a_{i} = a_{i1} + \begin{pmatrix} a_{i} \\ i & } \end{pmatrix} \sum_{\in I-{i1}  ,if m > 1.$$
Ví dụ, nếu $I = (1, 2, 3, 4)$, ta có
$$\sum_{i\in I}  a_{i} = a_{1} + (a_{2} + (a_{3} + a_{4})).$$
Nếu phép toán $+$ là không kết hợp, nhóm của các số hạng matters. Chẳng hạn, nói chung
$$a_{1} + (a_{2} + (a_{3} + a_{4})) \neq  (a + a_{2}) + (a_{3} + a_{4}).$$
$$However, if the operation + is associative, the sum \sum_{i}^{1}  \in I a_{i} should not depend on the grouping$$
Của các phần tử trong I, như dài như thứ tự của chúng được bảo toàn. Ví dụ, nếu $I = (1, 2, 3, 4, 5), J_{1} = (1, 2)$, và $J_{2} = (3, 4, 5)$, ta kỳ vọng rằng
$$\sum_{i\in I}  a_{i} = \begin{pmatrix} a_{j} \end{pmatrix} \sum_{j\in J1}  + \begin{pmatrix} a_{j} \end{pmatrix} \sum_{j\in J2}  .$$
Điều này thật vậy trường hợp, như ta có kết quả sau mệnh đề.

> **Mệnh đề 3.2.** Cho trước bất kỳ khác rỗng tập hợp $A$ được trang bị kết hợp nhị phân phép toán $+: A \times  A \to A$, với mọi khác rỗng hữu hạn dãy I của phân biệt tự nhiên các số và với mọi phân hoạch của I vào $p$ khác rỗng các dãy $I_{k1}, \dots  , I_{kp}$, với một số khác rỗng dãy $K = (k_{1}, \dots  , k_{p})$ của phân biệt tự nhiên các số sao cho $k_{i} < k_{j}$ suy ra rằng $\alpha  < \beta$ với mọi $\alpha  \in I_{ki}$ và tất cả $\beta  \in I_{kj}$, với mọi dãy $(a_{i})_{i\in I}$ của các phần tử trong $A$, ta có
$$\sum_{\alpha\in I}  a_{\alpha} = \sum_{k\in K}  \begin{pmatrix} a_{\alpha} \end{pmatrix} \sum_{\alpha\in Ik}  .$$

*Chứng minh.* Ta tiến hành bằng quy nạp theo kích thước $n$ của I. Nếu $n = 1$, thì ta phải có $p = 1$ và $I_{k1} =$ I, do đó mệnh đề nghiệm đúng một cách tầm thường.

<!-- PAGE 75 -->
$$A_{I}$$
$$I\in I$$
Tiếp theo, giả sử $n > 1$. Nếu $p = 1$, thì $I_{k1} =$ I và công thức là tầm thường, do đó giả sử rằng $p \ge 2$ và viết $J = (k_{2}, \dots  , k_{p})$. Có hai các trường hợp. Trường hợp $1$. dãy $I_{k1}$ có đơn lẻ phần tử, nói $\beta$, mà là phần tử thứ nhất của I. Trong trường hợp này, viết $C$ cho dãy thu được từ I bởi xóa của nó phần tử thứ nhất $\beta$. Theo Định nghĩa,
$$\sum_{\alpha\in I}  a_{\alpha} = a_{\beta} + \begin{pmatrix} a_{\alpha} \end{pmatrix} \sum_{\alpha\in C}  ,$$
$$and \sum_{\alpha\in Ik}  \sum_{j\in J}  \sum_{\alpha\in Ij}$$
$$\sum_{k\in K}  \begin{pmatrix} a_{\alpha} \end{pmatrix} = a_{\beta} + \begin{pmatrix}  \\ a_{\alpha} \end{pmatrix} \begin{pmatrix}\end{pmatrix} .$$
Vì |C| $= n$ - $1$, theo giả thiết quy nạp, ta có
$$\begin{pmatrix} a_{\alpha} \end{pmatrix} \sum_{\alpha\in C}  = \sum_{j\in J}  \begin{pmatrix} a_{\alpha} \end{pmatrix} \sum_{\alpha\in Ij}  ,$$
Mà cho ta của ta đồng nhất thức. Trường hợp $2$. dãy $I_{k1}$ có ít nhất hai các phần tử. Trong trường hợp này, cho $\beta$ là phần tử thứ nhất của I (và do đó của $I_{k1})$, cho I' là dãy thu được từ I bởi xóa của nó phần tử thứ nhất $\beta$, cho $I_{k1}'$ là dãy thu được từ $I_{k1}$ bởi xóa của nó phần tử thứ nhất $\beta$, và cho $I_{ki}' = I_{ki}$ cho $i = 2, \dots  , p$. Nhắc lại rằng $J = (k_{2}, \dots  , k_{p})$ và $K = (k_{1}, \dots  , k_{p})$. dãy I' có $n$ - $1$ các phần tử, do đó theo giả thiết quy nạp ứng dụng đến I' và I', ta thu được
$$\sum_{\alpha\in I'}  a_{\alpha} = \sum_{k\in K}  \begin{pmatrix} a_{\alpha} \end{pmatrix} \sum_{\alpha\in Ik'}  = \begin{pmatrix} a_{\alpha} \\ \alpha \end{pmatrix} \sum_{\in Ik'1}  + \begin{pmatrix}  \\ a_{\alpha} \end{pmatrix} \sum_{j\in J}  \begin{pmatrix}\end{pmatrix} \sum_{\alpha\in Ij}^{ki}  .$$
Nếu ta cộng lefthand vế/cạnh đến $a_{\beta}$, theo Định nghĩa ta thu được
$$\sum_{\alpha\in I}  a_{\alpha}.$$
Nếu ta cộng righthand vế/cạnh đến $a_{\beta}$, bằng cách sử dụng tính kết hợp và định nghĩa của được chỉ số tổng, ta thu được
$$a_{\beta} + \begin{pmatrix}  \\ a_{\alpha} \\ \alpha \end{pmatrix} \begin{pmatrix}  &  \\ + & a_{\alpha} \end{pmatrix} \sum_{\in Ik'1}  \begin{pmatrix}\end{pmatrix} \sum_{j\in J}  \begin{pmatrix}\end{pmatrix} \sum_{\alpha\in Ij}  = \begin{pmatrix}  \\ a_{\beta} + & a_{\alpha} \\ \alpha \end{pmatrix} \begin{pmatrix}\end{pmatrix} \sum_{\in Ik'1}  + \begin{pmatrix}  \\ a_{\alpha} \end{pmatrix} \sum_{j\in J}  \begin{pmatrix}\end{pmatrix} \sum_{\alpha\in Ij}$$
$$= \begin{pmatrix} a_{\alpha} \end{pmatrix} \sum_{\in Ik1}  + \begin{pmatrix}  \\ a_{\alpha} \end{pmatrix} \sum_{j\in J}  \begin{pmatrix}\end{pmatrix} \sum_{\alpha\in Ij}$$
$$= \sum_{k\in K}^{\alpha}  \begin{pmatrix} a_{\alpha} \end{pmatrix} \sum_{\alpha\in Ik}  ,$$
Như đã khẳng định.

<!-- PAGE 76 -->
$$If I = (1, \dots  , n), we also write \sum_{=1ii}  n a_{i} instead of \sum_{i}  a_{i}. Since + is associative, Propo-$$
$$sition 3.2 shows that the sum \sum_{1i}  n a^{=1} is independent of^{\in I} the grouping of its elements, which$$
Justifies sử dụng ký hiệu $a  + \cdots  + a_{n}$ (mà không có bất kỳ parentheses). Nếu ta cũng giả sử rằng của ta kết hợp nhị phân phép toán trên $A$ là giao hoán, thì ta
$$can show that the sum \sum_{i}  \in I a_{i} does not depend on the ordering of the index set I.$$

> **Mệnh đề 3.3.** Cho trước bất kỳ khác rỗng tập hợp $A$ được trang bị kết hợp và giao hoán nhị phân phép toán $+: A \times  A \to A$, với mọi hai khác rỗng hữu hạn các dãy I và $J$ của phân biệt tự nhiên các số sao cho $J$ là hoán vị của I (nói cách khác, underlying các tập hợp của I và $J$ là đồng nhất), với mọi dãy $(a_{i})_{i\in I}$ của các phần tử trong $A$, ta có
$$\sum_{\alpha\in I}  a_{\alpha} = \sum_{\alpha\in J}  a_{\alpha}.$$

*Chứng minh.* Ta tiến hành bằng quy nạp theo số $p$ của các phần tử trong I. Nếu $p = 1$, ta có $I = J$ và mệnh đề nghiệm đúng một cách tầm thường. Nếu $p > 1$, để đơn giản hóa ký hiệu, giả sử rằng $I = (1, \dots  , p)$ và rằng $J$ là hoán vị $(i_{1}, \dots  , i_{p})$ của I. Thứ nhất, giả sử rằng $2 \le i_{1} \le$ p-1, cho J' là dãy thu được từ $J$ bởi xóa $i_{1}$, I' là dãy thu được từ I bởi xóa $i_{1}$, và cho $P = (1, 2, \dots  , i_{1}-1)$ và $Q = (i_{1} +1, \dots$, p-1, $p)$. Nhận thấy rằng dãy I' là concatenation của các dãy $P$ và $Q$. Theo giả thiết quy nạp ứng dụng đến J' và I', và thì theo Mệnh đề 3.2 ứng dụng đến I' và của nó phân hoạch $(P, Q)$, ta có
$$\sum_{\alpha\in J'}  a_{\alpha} = \sum_{\alpha\in I'}  a_{\alpha} = \begin{pmatrix} a_{i} \end{pmatrix} \sum_{i=1}^{i1-1}  + \begin{pmatrix} a_{i} \end{pmatrix} \sum_{i=i1+1}^{p}  .$$
Nếu ta cộng lefthand vế/cạnh đến $a_{i1}$, theo Định nghĩa ta thu được
$$\sum_{\alpha\in J}  a_{\alpha}.$$
Nếu ta cộng righthand vế/cạnh đến $a_{i1}$, ta thu được
$$a_{i1} + \begin{pmatrix}  \\ a_{i} \end{pmatrix} \begin{pmatrix}  \\ + & a_{i} \end{pmatrix} \sum_{i=1}^{i1-1}  \begin{pmatrix}\end{pmatrix} \sum_{i=i1+1}^{p}  .$$
Bằng cách sử dụng tính kết hợp, ta thu được
$$a_{i1} + \begin{pmatrix}  \\ a_{i} \end{pmatrix} \begin{pmatrix}  \\ + & a_{i} \end{pmatrix} \sum_{i=1}^{i1-1}  \begin{pmatrix}\end{pmatrix} \sum_{i=i1+1}^{p}  = \begin{pmatrix}  \\ a_{i1}+ & a_{i} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \sum_{i=1}^{i1-1}  + \begin{pmatrix} a_{i} \end{pmatrix} \sum_{i=i1+1}^{p}  ,$$

<!-- PAGE 77 -->
$$A_{I}$$
$$I\in I$$
Thì bằng cách sử dụng tính kết hợp và tính giao hoán một vài lần (nhiều hơn/thêm một cách chặt chẽ, bằng cách sử dụng quy nạp trên $i_{1}$ - $1)$, ta thu được
$$\begin{pmatrix}  \\ a_{i1}+ & a_{i} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \sum_{i=1}^{i1-1}  + \begin{pmatrix} a_{i} \end{pmatrix} \sum_{i=i1+1}^{p}  = \begin{pmatrix} a_{i} \end{pmatrix} \sum_{i=1}^{i1-1}  + a_{i1} + \begin{pmatrix} a_{i} \end{pmatrix} \sum_{i=i1+1}^{p}$$
$$= \sum_{i=1}^{p}  a_{i},$$
Như đã khẳng định. các trường hợp ở đâu $i_{1} = 1$ hoặc $i_{1} = p$ là treated tương tự, nhưng trong đơn giản hơn cách thức vì hoặc $P =$ () hoặc $Q =$ () (ở đâu () ký hiệu rỗng dãy).
$$Having done all this, we can now make sense of sums of the form \sum_{i}  a_{i}, for any finite$$
Được chỉ số tập hợp $I$ và bất kỳ họ $a = (a_{i})_{i\in I}$ của các phần tử trong $A$, ở đâu $A$ là $a^{\in I}$ tập hợp được trang bị nhị phân phép toán $+$ mà là kết hợp và giao hoán. Thật vậy, vì I là hữu hạn, nó là trong song ánh với tập hợp ${1, \dots  , n}$ với một số $n \in \mathbb{N}$, và bất kỳ tổng thứ tự ⪯ trên I tương ứng với hoán vị $I_{⪯}$ của ${1, \dots  , n}$ (ở đâu ta đồng nhất
$$permutation with its image). For any total ordering ⪯on I, we define \sum_{i}  \in I,⪯a_{i} as$$
$$\sum_{i\in I,⪯}  a_{i} = \sum_{j\in I⪯}  a_{j}.$$
Thì với mọi khác tổng thứ tự ⪯' trên I, ta có
$$\sum_{i\in I,⪯'}  a_{i} = \sum_{j\in I⪯'}  a_{j},$$
Và vì $I_{⪯}$ và $I_{⪯'}$ là khác nhau các hoán vị của ${1, \dots  , n}$, theo Mệnh đề 3.3, ta có
$$\sum_{j\in I⪯}  a_{j} = \sum_{j\in I⪯'}  a_{j}.$$
$$Therefore, the sum \sum_{i}  \in a_{i} does not depend on the total ordering on I. We define the sum$$
$$\sum_{i}  \in I a_{i} as the common^{I,⪯} value \sum_{i}  \in I,⪯a_{i} for all total orderings ⪯of I.$$
Ở đây là một số các ví dụ với $A =\mathbb{R}$:
$$\sqrt\sqrt\sqrt$$
$$1. If I = {1, 2, 3}, a = {(1, 2), (2, -3), (3,\overline{2)}}, then \sum_{i}  \in I a_{i} = 2 -3 +\overline{2 =} -1 +\overline{2.}$$
$$\sqrt\sqrt\sqrt$$
$$2. If I = {2, 5, 7}, a = {(2, 2), (5, -3), (7,\overline{2)}}, then \sum_{i}  \in I a_{i} = 2 -3 +\overline{2 =} -1 +\overline{2.}$$
$$3. If I = {r, g, b}, a = {(r, 2), (g, -3), (b, 1)}, then \sum_{i}  \in I a_{i} = 2 -3 + 1 = 0.$$
