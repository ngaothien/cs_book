# Cayley–Hamilton Định lý


<!-- PAGE 242 -->
Ma trận, theo Hệ quả 4.6, ma trận của $f$ đối với cơ sở (basis) $(v_{1}, \dots  , v_{n})$ là $P^{-1}$ M(f)P. Theo Mệnh đề 7.9, ta có $det(P^{-1}$ M(f)P) $= det(P^{-1}$) det(M(f)) det(P) $= det(P^{-1}$) det(P) det(M(f)) $=$ det(M(f)). Do đó, det(f) là thật vậy độc lập của cơ sở (basis) của $E$.

> **Định nghĩa 7.8.** Cho trước không gian vectơ (vector space) $E$ của hữu hạn số chiều, với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$, ta định nghĩa định thức (determinant) det(f) của $f$ như định thức (determinant) det(M(f)) của ma trận của $f$ trong bất kỳ cơ sở (basis) (vì, từ thảo luận chỉ trước định nghĩa này, định thức (định thức (determinant)) này không phụ thuộc vào cơ sở (basis)). Thì ta có kết quả sau mệnh đề.

> **Mệnh đề 7.13.** Cho trước bất kỳ không gian vectơ (vector space) $E$ của hữu hạn số chiều $n$, ánh xạ tuyến tính (linear map) $f$: $E \to E$ là khả nghịch khi và chỉ khi det(f) $\neq  0$.

*Chứng minh.* ánh xạ tuyến tính (linear map) $f$: $E \to E$ là khả nghịch khi và chỉ khi ma trận của nó M(f) trong bất kỳ cơ sở (basis) là khả nghịch (theo Mệnh đề 4.2), khi và chỉ khi det(M(f)) $\neq  0$, theo Mệnh đề 7.10. Cho trước không gian vectơ (vector space) của hữu hạn số chiều $n$, nó là dễ dàng được thấy rằng tập hợp của song ánh (bijective) các ánh xạ tuyến tính (linear maps) $f$: $E \to E$ sao cho det(f) $= 1$ là nhóm dưới hợp thành. nhóm này là nhóm con của tổng quát tuyến tính nhóm GL(E). Nó được gọi là đặc biệt tuyến tính nhóm (của $E)$, và nó được ký hiệu bởi SL(E), hoặc khi $E = K^{n}$, bởi SL(n, $K)$, hoặc chẵn/ngay cả bởi SL(n).

## 7.7 Cayley–Hamilton Định lý

Ta tiếp theo thảo luận thú vị và quan trọng ứng dụng của Mệnh đề 7.10, Cayley– Hamilton định lý. các kết quả của điều này mục áp dụng đến các ma trận trên bất kỳ vành giao hoán (commutative ring) $K$. Thứ nhất ta cần khái niệm của đa thức đặc trưng (characteristic polynomial) của ma trận.

> **Định nghĩa 7.9.** Nếu $K$ là bất kỳ vành giao hoán (commutative ring), với mọi $n \times  n$ ma trận $A \in M_{n}(K)$, đa thức đặc trưng (characteristic polynomial) $P_{A}(X)$ của $A$ là định thức (determinant)
$$P_{A}(X) = \det(XI -A).$$
Đa thức đặc trưng (characteristic polynomial) $P_{A}(X)$ là đa thức trong K[X], vành của các đa thức trong indeterminate $X$ với các hệ số trong vành $K$. Ví dụ, khi $n = 2$, nếu
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} ,$$
Thì
$$X -a-b$$
$$-$$
$$P_{A}(X) = = X^{2}(a + d)X + ad -bc.$$
$$-cX -d$$

<!-- PAGE 243 -->
Ta có thể thế ma trận $A$ cho biến $X$ trong đa thức $P_{A}(X)$, thu được ma trận $P_{A}$. Nếu ta viết
$$P_{A}(X) = X^{n}+ c_{1}X^{n-1}+ \cdots  + c_{n},$$
Thì
$$P_{A} = A^{n}+ c_{1}A^{n-1}+ \cdots  + c_{n}I.$$
Ta có kết quả sau đáng chú ý định lý.

> **Định lý 7.14.** (Cayley–Hamilton) Nếu $K$ là bất kỳ vành giao hoán (commutative ring), với mọi $n \times  n$ ma trận $A \in M_{n}(K)$, nếu ta cho
$$P_{A}(X) = X^{n}+ c_{1}X^{n-1}+ \cdots  + c_{n}$$
Là đa thức đặc trưng (characteristic polynomial) của $A$, thì
$$P_{A} = A^{n}+ c_{1}A^{n-1}+ \cdots  + c_{n}I = 0.$$

*Chứng minh.* Ta có thể quan điểm ma trận $B = XI$ - $A$ như ma trận với các hệ số trong đa thức vành K[X], và thì ta có thể tạo thành ma trận $B$ mà là chuyển vị (transpose) của ma trận của
$$e$$
Các phần bù đại số (cofactor) của các phần tử của $B$. Mỗi phần tử (entry) trong $B$ là $(n$ - $1) \times  (n$ - $1)$ định thức (determinant), và do đó
$$e$$
Đa thức của bậc hầu hết $n$ - $1$, do đó ta có thể viết $B$ như
$$e$$
$$B = X^{n-1}B_{0} + X^{n-2}B_{1} + \cdots  + B_{n-1},$$
$$e$$
Với một số $n \times  n$ các ma trận $B_{0}, \dots  , B_{n-1}$ với các hệ số trong $K$. Ví dụ, khi $n = 2$, ta có
$$B = \begin{pmatrix} X-a & -b \\ -c & X-d \end{pmatrix} ,Be = \begin{pmatrix} X-d & b \\ c & X-a \end{pmatrix} = X \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + \begin{pmatrix} -d & b \\ c & -a \end{pmatrix} .$$
Theo Mệnh đề 7.10, ta có
$$BB = \det(B)I = P_{A}(X)I.$$
$$e$$
Mặt khác, ta có
$$BB = (XI -A)(X^{n-1}B_{0} + X^{n-2}B_{1} + \cdots  + X^{n-j-1}B_{j} + \cdots  + B_{n-1}),$$
$$e$$
Và bằng cách nhân ra vế phải, ta thu được
$$BB = X^{n}D_{0} + X^{n-1}D_{1} + \cdots  + X^{n-j}D_{j} + \cdots  + D_{n},$$
$$e$$
Với
$$D_{0} = B_{0}$$
$$D_{1} = B_{1} -AB_{0}$$
$$\vdots$$
$$D_{j} = B_{j} -AB_{j-1}$$
$$\vdots$$
$$D_{n-1} = B_{n-1} -AB_{n-2}$$
$$D_{n} = -AB_{n-1}.$$

<!-- PAGE 244 -->
Vì
$$P_{A}(X)I = (X^{n}+ c_{1}X^{n-1}+ \cdots  + c_{n})I,$$
Đẳng thức
$$X^{n}D_{0} + X^{n-1}D_{1} + \cdots  + D_{n} = (X^{n}+ c_{1}X^{n-1}+ \cdots  + c_{n})I$$
Là đẳng thức giữa hai các ma trận, do đó nó đòi hỏi rằng tất cả tương ứng các phần tử (entries) là bằng nhau, và vì các phần tử này là các đa thức, các hệ số của các đa thức này phải là đồng nhất, mà là tương đương đến tập hợp của các phương trình
$$I = B_{0}$$
$$c_{1}I = B_{1} -AB_{0}$$
$$\vdots$$
$$c_{j}I = B_{j} -AB_{j-1}$$
$$\vdots$$
$$c_{n-1}I = B_{n-1} -AB_{n-2}$$
$$c_{n}I = -AB_{n-1},$$
Với mọi $j$, với $1 \le j \le n$ - $1$. Nếu, như trong bảng ở dưới,
$$A^{n}= A^{n}B_{0}$$
$$c_{1}A^{n-1}= A^{n-1}(B_{1} -AB_{0})$$
$$\vdots$$
$$c_{j}A^{n-j}= A^{n-j}(B_{j} -AB_{j-1})$$
$$\vdots$$
$$c_{n-1}A = A(B_{n-1} -AB_{n-2})$$
$$c_{n}I = -AB_{n-1},$$
Ta nhân phương trình thứ nhất bởi $A^{n}$, cuối cùng bởi I, và một cách tổng quát $(j +$ 1)th bởi $A^{n-j}$, khi ta cộng lên tất cả các phần tử này mới các phương trình, ta xem rằng vế phải cộng sai khác $0$, và ta thu được của ta mong muốn phương trình
$$A^{n}+ c_{1}A^{n-1}+ \cdots  + c_{n}I = 0,$$
Như đã khẳng định. Như concrete ví dụ, khi $n = 2$, ma trận
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$
Thỏa mãn phương trình
$$A^{2}-(a + d)A + (ad -bc)I = 0.$$

<!-- PAGE 245 -->
Hầu hết độc giả sẽ probably tìm chứng minh của Định lý 7.14 khá clever nhưng rất mysterious và unmotivated. conceptual difficulty là rằng ta một cách thực cần đến understand cách mà các đa thức trong một biến “act” trên các vectơ theo ma trận $A$. Điều này có thể được được thực hiện và cho ta nhiều hơn/thêm “tự nhiên” chứng minh. Thực sự, lập luận là đơn giản hơn và nhiều hơn/thêm tổng quát nếu ta tự do chính chúng ta từ các ma trận và thay vì xét không gian vectơ hữu hạn chiều $E$ và một số cho trước ánh xạ tuyến tính (linear map) $f$: $E \to E$. Cho trước bất kỳ đa thức p(X) $= a_{0}X^{n} + a_{1}X^{n-1} + \cdots  + a_{n}$ với các hệ số trong trường $K$, ta định nghĩa ánh xạ tuyến tính (linear map) p(f): $E \to E$ bởi
$$p(f) = a_{0}f^{n}+ a_{1}f^{n-1}+ \cdots  + a_{n}id,$$
Ở đâu $f^{k} = f \circ \cdots  \circ f$, k-fold hợp thành của $f$ với chính nó. Lưu ý rằng
$$p(f)(u) = a_{0}f^{n} (u) + a_{1}f^{n-1} (u) + \cdots  + a_{n}u,$$
Với mọi vectơ $u \in E$. Thì ta định nghĩa mới loại của vô hướng (scalar) phép nhân $\cdot$: $K[X]\times E \to E$ bởi các đa thức như sau: với mọi đa thức p(X) $\in$ K[X], với mọi $u \in E$,
$$p(X) \cdot  u = p(f)(u).$$
Nó là dễ để kiểm chứng rằng điều này là “tốt action,” mà có nghĩa là
$$p \cdot  (u + v) = p \cdot  u + p \cdot  v$$
$$(p + q) \cdot  u = p \cdot  u + q \cdot  u$$
$$(pq) \cdot  u = p \cdot  (q \cdot  u)$$
$$1 \cdot  u = u,$$
Với mọi $p, q \in$ K[X] và tất cả $u, v \in E$. Với điều này mới vô hướng (scalar) phép nhân, $E$ là K[X]-môđun. Nếu $p = \lambda$ là chỉ vô hướng (scalar) trong $K$ (đa thức của bậc $0)$, thì
$$\lambda  \cdot  u = (\lambda id)(u) = \lambda u,$$
Mà có nghĩa là $K$ acts trên $E$ bởi vô hướng (scalar) phép nhân như trước. Nếu p(X) $= X$ (đơn thức $X)$, thì
$$X \cdot  u = f(u).$$
Bây giờ nếu ta chọn cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $E$, nếu đa thức p(X) $\in$ K[X] có tính chất rằng
$$p(X) \cdot  e_{i} = 0,i = 1, \dots  , n,$$
Thì điều này có nghĩa là $p(f)(e_{i}) = 0$ cho $i = 1, \dots  , n$, mà có nghĩa là ánh xạ tuyến tính (linear map) p(f) triệt tiêu trên $E$. Ta có thể cũng kiểm tra, như ta đã thực hiện trong Mục 7.2, rằng nếu $A$ và $B$ là hai ma trận cỡ $n \times  n$ và nếu $(u_{1}, \dots  , u_{n})$ là bất kỳ $n$ các vectơ, thì
$$A \cdot \begin{pmatrix} u_{1} \\ B \cdot \vdots \\ u_{n} \end{pmatrix} \begin{pmatrix}\end{pmatrix} = (AB) \cdot \begin{pmatrix} u_{1} \\ \vdots \\ u_{n} \end{pmatrix} .$$

<!-- PAGE 246 -->
Điều này suggests plan của attack cho của ta thứ hai chứng minh của Cayley–Hamilton định lý. Để đơn giản, ta chứng minh định lý cho các không gian vectơ trên trường. chứng minh đi qua cho môđun tự do (free module) trên vành giao hoán (commutative ring).

> **Định lý 7.15.** (Cayley–Hamilton) Với mọi không gian vectơ hữu hạn chiều trên trường $K$, với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$, với mọi cơ sở (basis) $(e_{1}, \dots  , e_{n})$, nếu $A$ là ma trận trên $f$ trên cơ sở (basis) $(e_{1}, \dots  , e_{n})$ và nếu
$$P_{A}(X) = X^{n}+ c_{1}X^{n-1}+ \cdots  + c_{n}$$
Là đa thức đặc trưng (characteristic polynomial) của $A$, thì
$$P_{A}(f) = f^{n}+ c_{1}f^{n-1}+ \cdots  + c_{n}id = 0.$$

*Chứng minh.* Vì các cột của $A$ bao gồm của vectơ $f(e_{j})$ được biểu diễn trên cơ sở (basis) $(e_{1}, \dots  , e_{n})$, ta có
$$f(e_{j}) = \sum_{i=1}^{n}  a_{i j}e_{i},1 \le j \le n.$$
Bằng cách sử dụng của ta action của K[X] trên $E$, ở trên các phương trình có thể được biểu diễn dưới dạng
$$X \cdot  e_{j} = \sum_{i=1}^{n}  a_{i j} \cdot  e_{i},1 \le j \le n,$$
Mà cho ta
$$\sum_{i=1}^{j-1}  -a_{i j} \cdot  e_{i} + (X -a_{j j}) \cdot  e_{j} + \sum_{i=j+1}^{n}  -a_{i j} \cdot  e_{i} = 0,1 \le j \le n.$$
Nhận thấy rằng chuyển vị (transpose) của đa thức đặc trưng (characteristic polynomial) chỉ ra lên, do đó ở trên hệ có thể được viết dưới dạng
$$\begin{pmatrix} X-a_{1 1} & -a_{2 1} & \cdots & -a_{n1} \\ -a_{1 2} & X-a_{2 2} & \cdots & -a_{n2} \\ \vdots & \vdots & \vdots & \vdots \\ -a_{1n} & -a_{2n} & \cdots & X-a_{n n} \end{pmatrix} \cdot \begin{pmatrix} e_{1} \\ e_{2} \\ \vdots \\ e_{n} \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix} .$$
Nếu ta cho $B = XI$ - $A^{\top}$, thì như trong trước đó chứng minh, nếu $B$ là chuyển vị (transpose) của ma trận của
$$e$$
Các phần bù đại số (cofactor) của $B$, ta có
$$BB = \det(B)I = \det(XI -A^{\top})I = \det(XI -A)I = P_{A}I.$$
$$e$$
Nhưng vì
$$B \cdot \begin{pmatrix} e_{1} \\ e_{2} \\ \vdots \\ e_{n} \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix} ,$$
