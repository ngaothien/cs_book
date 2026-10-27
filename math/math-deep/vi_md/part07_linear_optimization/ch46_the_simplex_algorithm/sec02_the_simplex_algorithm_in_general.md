# Thuật toán đơn hình (simplex algorithm) nói chung


<!-- PAGE 1614 -->
Trong trường hợp thứ nhất, điểm $(1 + \theta , \theta , 0, 3)$ là nghiệm chấp nhận được (feasible solution) với mọi $\theta  \ge 0$ và giá trị của hàm mục tiêu (objective function) nếu $1 + \theta$, và trong trường hợp thứ hai, điểm $(1$ - $\theta , 0, \theta , 3$ - $\theta$) là nghiệm chấp nhận được (feasible solution) iff0 $\le \theta  \le 1$ và giá trị của hàm mục tiêu (objective function) là $1$ - $\theta$. Điều này time, ta là trong tình huống ở đâu các điểm
$$(1 + \theta , \theta , 0, 3) = (1, 0, 0, 3) + \theta (1, 1, 0, 0),\theta  \ge 0$$
Tạo thành vô hạn tia trong tập hợp của chấp nhận được (feasible) các nghiệm, và hàm mục tiêu (objective function) $1 + \theta$ là không bị chặn từ ở trên trên điều này tia. Điều này indicates rằng của ta bài toán quy hoạch tuyến tính (linear program), mặc dù chấp nhận được (feasible), là không bị chặn. Cho chúng ta bây giờ mô tả bước của thuật toán đơn hình (simplex algorithm) nói chung.

## 46.2 Thuật toán đơn hình (simplex algorithm) nói chung

Ta giả sử rằng ta đã có ban đầu đỉnh $u_{0}$ đến bắt đầu từ. Điều này đỉnh tương ứng với cơ bản nghiệm chấp nhận được (feasible solution) với cơ sở (basis) $K_{0}$. Ta sẽ chỉ ra sau này rằng nó là luôn luôn khả dĩ/có thể để tìm cơ bản nghiệm chấp nhận được (feasible solution) của Bài toán quy hoạch tuyến tính (linear program) $(P)$ là tiêu chuẩn tạo thành, hoặc đến detect rằng $(P)$ có không có nghiệm chấp nhận được (feasible solution). ý tưởng đằng sau thuật toán đơn hình (simplex algorithm) là điều này: Cho trước cặp $(u, K)$ bao gồm của cơ bản nghiệm chấp nhận được (feasible solution) $u$ và cơ sở (basis) $K$ cho $u$, tìm một cái khác cặp $(u^{+}, K^{+})$ bao gồm của một cái khác cơ bản nghiệm chấp nhận được (feasible solution) $u^{+}$ và cơ sở (basis) $K^{+}$ cho $u^{+}$, sao cho $K^{+}$ là thu được từ $K$ bởi xóa một số cơ bản chỉ số $k^{-} \in K$ và cộng một số nonbasic chỉ số $j^{+} \in / K$, trong như vậy cách rằng giá trị của hàm mục tiêu (objective function) tăng (preferably chặt). bước mà bao gồm trong swapping các vectơ $A^{k-}$ và $A^{j+}$ được gọi là một chọn phần tử trụ bước. Cho $u$ là cho trước đỉnh tương ứng với cơ bản nghiệm chấp nhận được (feasible solution) với cơ sở (basis) $K$. Vì $m$ các vectơ $A^{k}$ tương ứng với các chỉ số $k \in K$ là độc lập tuyến tính (linearly independent), chúng tạo thành cơ sở (basis), do đó với mọi nonbasic $j \in / K$, ta viết
$$A^{j}= \sum_{k\in K}  \gamma_{k}^{j} A^{k}.(*)$$
$$\mathbb{R}^{m}$$
Ta cho $\gamma_{K}^{j}  \in$ là vectơ cho trước bởi $\gamma_{K}^{j}  = (\gamma_{k}^{j} )_{k\in K}$. Thực sự, vì vectơ $\gamma_{K}^{j}$ phụ thuộc vào $K$, là rất precise ta nên ký hiệu các thành phần của nó bởi $(\gamma_{K}^{j} )_{k}$, nhưng để đơn giản hóa ký hiệu ta thường viết $\gamma_{k}^{j}$ thay vì của $(\gamma_{K}^{j} )_{k}$ (trừ khi confusion phát sinh). Ta sẽ giải thích sau này cách mà các hệ số $\gamma_{k}^{j}$ có thể được được tính efficiently. Vì $u$ là nghiệm chấp nhận được (feasible solution) ta có $u \ge 0$ và Au $= b$, nghĩa là,
$$\sum_{k\in K}  u_{k}A^{k}= b.(**)$$
Với mọi nonbasic $j \in / K$, candidate cho entering cơ sở (basis) $K$, ta thử để tìm mới đỉnh $u(\theta$) rằng các cải thiện hàm mục tiêu (objective function), và cho điều này ta cộng $-\theta A^{j} + \theta A^{j} = 0$ đến $b$ trong

<!-- PAGE 1615 -->
Phương trình (**) và thì thay thế occurrence của $A^{j}$ trong $-\theta A^{j}$ bởi phải hand vế/cạnh của Phương trình (*) để thu được
$$b = \sum_{k\in K}  u_{k}A^{k}-\theta A^{j}+ \theta A^{j}$$
$$= \sum_{k\in K}  u_{k}A^{k} -\theta \begin{pmatrix} \gamma_{k}^{j} A^{k} \end{pmatrix} \sum_{k\in K}  + \theta A^{j}$$
$$= \sum_{k\in K}  \begin{pmatrix} u_{k} -\theta \gamma_{k}^{j} \end{pmatrix} A^{k} + \theta A^{j}.$$
Hệ quả là, vectơ $u(\theta$) xuất hiện trên vế phải của ở trên phương trình cho trước bởi
$$u_{i} -\theta \gamma_{i}^{j} if i \in K$$
$$$$
$$$$
$$u(\theta )_{i} =\theta if i = j$$
$$0if i \in /K \cup {j}$$
$$$$
Automatically thỏa mãn các ràng buộc $Au(\theta$) $= b$, và vectơ này là nghiệm chấp nhận được (feasible solution) khi và chỉ khi
$$\theta  \ge 0andu_{k} \ge \theta \gamma_{k}^{j} for all k \in K.$$
Hiển nhiên $\theta  = 0$ là nghiệm, và nếu
$$



$$
$$\theta^{j} = \min \frac{u_{k}}{\gamma_{k}^{j}} \gamma_{k}^{j}  > 0, k \in K> 0,$$
Thì ta có miền giá trị (range) của chấp nhận được (feasible) các nghiệm cho $0 \le \theta  \le \theta^{j}$. giá trị của hàm mục tiêu (objective function) cho $u(\theta$) là
$$cu(\theta ) = \sum_{k\in K}  c_{k}(u_{k} -\theta \gamma_{k}^{j} ) + \theta c_{j} = cu + \theta \begin{pmatrix} c_{j}- & \gamma_{k}^{j} c_{k} \end{pmatrix} \sum_{k\in K}  .$$
Vì potential thay đổi trong hàm mục tiêu (objective function) là
$$\theta \begin{pmatrix} c_{j}- & \gamma_{k}^{j} c_{k} \end{pmatrix} \sum_{k\in K}$$
$$and \theta  \ge 0, if c_{j} - \sum_{k}  \gamma_{k}^{j} c_{k} \le 0, then the objective function can’t be increased.$$
$$However, if c_{j+} - \sum_{k}^{\in K}  \in K \gamma_{k}^{j+}  c_{k} > 0 for some j^{+}\in /K, and if \theta^{j+} > 0, then the objective$$
Hàm có thể được chặt increased bằng cách chọn bất kỳ $\theta  > 0$ sao cho $\theta  \le \theta^{j+}$, do đó nó là tự nhiên đến không ít nhất một hệ số của $u(\theta$) bởi chọn $\theta  = \theta^{j+}$, mà cũng các cực đại hóa tăng của hàm mục tiêu (objective function). Trong trường hợp này (Trường hợp ở dưới (B2)), ta thu được mới nghiệm chấp nhận được (feasible solution) $u^{+} = u(\theta^{j+}$). Bây giờ, nếu $\theta^{j+} > 0$, thì tồn tại một chỉ số $k \in K$ như vậy $u_{k} > 0, \gamma_{k}^{j+} > 0$, và $\theta^{j+} = u_{k}/\gamma_{k}^{j+}$, do đó ta có thể chọn như vậy chỉ số $k^{-}$ cho vectơ $A^{k-}$ để lại cơ sở (basis) $K$. Ta khẳng định rằng

<!-- PAGE 1616 -->
$K^{+} = (K -{k^{-}}) \cup {j^{+}}$ là cơ sở (basis). Điều này là bởi vì hệ số $\gamma_{k-}^{j+}$ liên kết với cột $A^{k-}$ là khác không (thực ra, $\gamma_{k-}^{j+} > 0)$, do đó Phương trình (*), cụ thể là
$$A^{j+} = \gamma_{k-}^{j+} A^{k-}+ \sum_{K-{k}  \gamma_{k}^{j+}  A^{k},$$
$$k\in -}$$
Cho ta phương trình
$$A^{k-}= (\gamma_{k-}^{j+} )^{-1}A^{j+}- \sum_{K-{k}  (\gamma_{k-}^{j+} )^{-1}\gamma_{k}^{j+}  A^{k},$$
$$k\in -}$$
Và các phương trình này suy ra rằng các không gian con được sinh (spanned) bởi các vectơ $(A^{k})_{k\in K}$ và các vectơ $(A^{k})_{k\in K+}$ là đồng nhất. Tuy nhiên, $K$ là cơ sở (basis) có số chiều $m$ do đó không gian con này có số chiều $m$, và vì $K^{+}$ cũng có $m$ các phần tử, nó phải là cơ sở (basis). Vì vậy, $u^{+} = u(\theta^{j+}$) là cơ bản nghiệm chấp nhận được (feasible solution). ở trên trường hợp là hầu hết chung/phổ biến một, nhưng khác các tình huống có thể phát sinh. Trong những gì suy ra, ta thảo luận tất cả eventualities. Trường hợp $(A)$.
$$We have c_{j} - \sum_{k}  \gamma_{k}^{j} c_{k} \le 0 for all j \in /K. Then it turns out that u is an optimal$$
Nghiệm. $Otherwise,^{\in K}$ ta là trong Trường hợp $(B)$. Trường hợp $(B)$.
$$We have c_{j} - \sum_{k}  \in K \gamma_{k}^{j} c_{k} > 0 for some j \in /K (not necessarily unique). There are three$$
Subcases. Trường hợp (B1). Nếu với một số $j \in / K$ như ở trên ta cũng có $\gamma_{k}^{j}  \le 0$ với mọi $k \in K$, vì $u_{k} \ge 0$ với mọi $k \in K$, điều này places không có thu hẹp trên $\theta$, và hàm mục tiêu (objective function) là không bị chặn ở trên. Điều này là demonstrated bởi Ví dụ 46.3 với $K = {3, 4}$ và $j = 2$ vì $\gamma_{{3,4}}^{2}  = (-1, 0)$. Trường hợp (B2). Tồn tại một chỉ số $j^{+} \in / K$ sao cho simultaneously
$$(1) c_{j+} - \sum_{k}  \gamma_{k}^{j+}  c_{k} > 0, which means that the objective function can potentially be$$
$increased;^{\in K}$
$(2)$ Tồn tại một $k \in K$ sao cho $\gamma_{k}^{j+} > 0$, và với mọi $k \in K$, nếu $\gamma_{k}^{j+} > 0$ thì $u_{k} > 0$, mà suy ra rằng $\theta^{j+} > 0$. Nếu ta chọn $\theta  = \theta^{j+}$ ở đâu
$$



$$
$$\theta^{j+} = \min \frac{u_{k}}{\gamma_{k}^{j+}} \gamma_{k}^{j+} > 0, k \in K> 0,$$

<!-- PAGE 1617 -->
Thì nghiệm chấp nhận được (feasible solution) $u^{+}$ cho trước bởi
$$u_{i} -\theta^{j+} \gamma_{i}^{j+} if i \in K$$
$$$$
$$$$
$$u_{i}^{+} =\theta^{j+} if i = j^{+}$$
$$0if i \in /K \cup {j^{+}}$$
$$$$
Là đỉnh của $\mathcal{P}(A, b)$. Nếu ta chọn bất kỳ chỉ số $k^{-} \in K$ sao cho $\theta^{j+} = u_{k-}/\gamma_{k-}^{j+}$, thì $K^{+} = (K -{k^{-}})\cup {j^{+}}$ là cơ sở (basis) cho $u^{+}$. vectơ $A^{j+}$ enters mới cơ sở (basis) $K^{+}$, và vectơ $A^{k-}$ để lại old cơ sở (basis) $K$. Điều này là chọn phần tử trụ bước. hàm mục tiêu (objective function) tăng chặt. Điều này là demonstrated bởi Ví dụ 46.2 với $K = {3, 4, 5}, j = 1$, và $k = 4$, Thì $\gamma_{{3,4,5}}^{1}  = (-1, 1, 0)$, với $\gamma_{4}^{1}  = 1$. Vì $u = (0, 0, 1, 3, 2), \theta^{1} =_{\gamma1}^{u4} = 3$, và mới tối ưu các nghiệm trở thành $u^{+} = (3, 0, 1$ - 3(-1), $3$ - 3(1), $2$ - 3(0)) $= (3^{4}, 0, 4, 0, 2)$. Trường hợp (B3).
$$There is some index j \in /K such that c_{j} - \sum_{k}  \in K \gamma_{k}^{j} c_{k} > 0, and for each of the indices$$
$j \in / K$ thỏa mãn ở trên tính chất ta có simultaneously
$$(1) c_{j} - \sum_{k}  \gamma_{k}^{j} c_{k} > 0, which means that the objective function can potentially be in-$$
$creased;^{\in K}$
$(2)$ Tồn tại một $k \in K$ sao cho $\gamma_{k}^{j}  > 0$, và $u_{k} = 0$, mà suy ra rằng $\theta^{j} = 0$. Hệ quả là, hàm mục tiêu (objective function) thực hiện không thay đổi. Trong trường hợp này, $u$ là suy biến cơ bản nghiệm chấp nhận được (feasible solution). Ta có thể associate đến $u^{+} = u$ mới cơ sở (basis) $K^{+}$ như sau: Chọn bất kỳ chỉ số $j^{+} \in / K$ sao cho
$$c_{j+} - \sum_{k\in K}  \gamma_{k}^{j+}  c_{k} > 0,$$
Và bất kỳ chỉ số $k^{-} \in K$ sao cho
$$\gamma_{k-}^{j+} > 0,$$
Và cho $K^{+} = (K -{k^{-}}) \cup {j^{+}}$. Như trong Trường hợp (B2), vectơ $A^{j+}$ enters mới cơ sở (basis) $K^{+}$, và vectơ $A^{k-}$ để lại old cơ sở (basis) $K$. Điều này là chọn phần tử trụ bước. Tuy nhiên, hàm mục tiêu (objective function) thực hiện không thay đổi vì $\theta^{j+} = 0$. Điều này là demonstrated bởi Ví dụ 46.1 với $K = {3, 4}, j = 2$, và $k = 3$. Nó là dễ để chứng minh rằng trong Trường hợp $(A)$ cơ bản nghiệm chấp nhận được (feasible solution) $u$ là nghiệm tối ưu (optimal solution), và rằng trong Trường hợp (B1) bài toán quy hoạch tuyến tính (linear program) là không bị chặn. Ta đã được chứng minh rằng trong Trường hợp
(B2) vectơ $u^{+}$ và của nó cơ sở (basis) $K^{+}$ constitutes cơ bản nghiệm chấp nhận được (feasible solution), và chứng minh trong Trường hợp (B3) là đồng dạng. Cho chi tiết, xem Ciarlet $[41]$ (Chương $10)$.

<!-- PAGE 1618 -->
Nó là thuận tiện đến reinterpret khác nhau các trường hợp được xét bởi giới thiệu sau đây các tập hợp:
$$no$$
$$B_{1} =j \in /K | c_{j} - \sum_{k\in K}  \gamma_{k}^{j} c_{k} > 0, maxk\in K \gamma_{k}^{j}  \le 0$$
$$


$$
$$no$$
$$B_{2} =j \in /K | c_{j} - \sum_{k\in K}  \gamma_{k}^{j} c_{k} > 0, maxk\in K \gamma_{k}^{j}  > 0, \min \frac{u_{k}}{\gamma_{k}^{j}} k \in K, \gamma_{k}^{j}  > 0> 0$$
$$


$$
$$no$$
$$B_{3} =j \in /K | c_{j} - \sum_{k\in K}  \gamma_{k}^{j} c_{k} > 0, maxk\in K \gamma_{k}^{j}  > 0, \min \frac{u_{k}}{\gamma_{k}^{j}} k \in K, \gamma_{k}^{j}  > 0= 0,$$
Và
$$no$$
$$B = B_{1} \cup B_{2} \cup B_{3} =j \in /K | c_{j} - \sum_{k\in K}  \gamma_{k}^{j} c_{k} > 0.$$
Thì nó là dễ để xem rằng sau đây equivalences đúng:
$$Case (A) \Leftarrow \Rightarrow B = \emptyset ,Case (B) \Leftarrow \Rightarrow B \neq  \emptyset$$
$$Case (B1) \Leftarrow \Rightarrow B_{1} \neq  \emptyset$$
$$Case (B2) \Leftarrow \Rightarrow B_{2} \neq  \emptyset$$
$$Case (B3) \Leftarrow \Rightarrow B_{3} \neq  \emptyset .$$
Hơn nữa, Các trường hợp $(A)$ và $(B)$, Các trường hợp (B1) và (B3), và Các trường hợp (B2) và (B3) là mutually exclusive, trong khi Các trường hợp (B1) và (B2) là không. Nếu Trường hợp (B1) và Trường hợp (B2) phát sinh simultaneously, ta opt cho Trường hợp (B1) mà nói rằng rằng Bài toán quy hoạch tuyến tính (linear program) $(P)$ là không bị chặn và terminate thuật toán. Ở đây là một vài các nhận xét về phương pháp. Trong Trường hợp (B2), mà là đường đi theo sau bởi thuật toán hầu hết frequently, khác nhau các lựa chọn có được tạo cho chỉ số $j^{+} \in / K$ cho mà $\theta^{j+} > 0$ (mới chỉ số trong $K^{+})$. Tương tự, khác nhau các lựa chọn có được tạo cho chỉ số $k^{-} \in K$ để lại $K$, nhưng như vậy các lựa chọn là typically ít hơn quan trọng. Tương tự trong Trường hợp (B3), khác nhau các lựa chọn có được tạo cho mới chỉ số $j^{+} \in / K$ đi vào $K^{+}$. Trong Các trường hợp (B2) và (B3), các tiêu chuẩn cho tạo ra như vậy các lựa chọn được gọi là phần tử trụ (pivot) các quy tắc. Trường hợp (B3) chỉ phát sinh khi $u$ là suy biến đỉnh. Nhưng chẵn/ngay cả nếu $u$ là suy biến, Trường hợp
(B2) có thể phát sinh nếu $u_{k} > 0$ bất cứ khi nào $\gamma_{k}^{j}  > 0$. Nó có thể cũng xảy ra rằng $u$ là không suy biến nhưng kết quả là của Trường hợp (B2), mới đỉnh $u^{+}$ là suy biến bởi vì ít nhất hai các thành phần $u_{k1}$ - $\theta^{j+} \gamma_{k1}^{j+}$ và $u_{k2}$ - $\theta^{j+} \gamma_{k2}^{j+}$ triệt tiêu với một số phân biệt $k_{1}, k_{2} \in K$. Các trường hợp $(A)$ và (B1) tương ứng với các tình huống ở đâu thuật toán kết thúc, và Trường hợp
(B2) có thể chỉ phát sinh hữu hạn số của lần during execution của thuật toán đơn hình (simplex algorithm), vì hàm mục tiêu (objective function) là chặt increased từ đỉnh đến đỉnh và có chỉ một cách hữu hạn nhiều các đỉnh. Vì vậy, nếu thuật toán đơn hình (simplex algorithm) được bắt đầu trên bất kỳ ban đầu cơ bản nghiệm chấp nhận được (feasible solution) $u_{0}$, thì một của ba mutually exclusive các tình huống có thể phát sinh:

<!-- PAGE 1619 -->
$(1)$ Có một hữu hạn dãy của occurrences của Trường hợp (B2) $and/or$ Trường hợp (B3) kết thúc/cuối với occurrence của Trường hợp $(A)$. Thì cuối cùng đỉnh produced bởi thuật toán là nghiệm tối ưu (optimal solution). Điều này là những gì occurred trong Các ví dụ 46.1 và 46.2.
$(2)$ Có một hữu hạn dãy của occurrences của Trường hợp (B2) $and/or$ Trường hợp (B3) kết thúc/cuối với occurrence của Trường hợp (B1). Ta kết luận rằng bài toán là không bị chặn, và do đó có không có nghiệm. Điều này là những gì occurred trong Ví dụ 46.3.
$(3)$ Có một hữu hạn dãy của occurrences của Trường hợp (B2) $and/or$ Trường hợp (B3), theo sau bởi vô hạn dãy của Trường hợp (B3). Nếu điều này xảy ra, thuật toán visits một số cơ sở (basis) hai lần. Điều này hiện tượng đã biết như cycling. Trong điều này eventually thuật toán không thỏa mãn đến đến đến conclusion. Có các ví dụ cho mà cycling xảy ra, mặc dù điều này là rare trong thực tế. Như vậy ví dụ là cho trước trong Chvatal $[40]$; xem Chương $3$, các trang 31-32, cho ví dụ với bảy các biến và ba các phương trình rằng các chu trình sau sáu các vòng lặp dưới nhất định phần tử trụ (pivot) quy tắc. thứ ba khả năng có thể được tránh được bởi lựa chọn của phù hợp phần tử trụ (pivot) quy tắc. Hai của các phần tử này các quy tắc là Bland’s quy tắc và lexicographic quy tắc; xem Chvatal $[40]$ (Chương $3$, các trang 34-38). Bland’s quy tắc nói rằng: chọn nhỏ nhất của eligible incoming các chỉ số $j^{+} \in / K$, và tương tự chọn nhỏ nhất của eligible outgoing các chỉ số $k^{-} \in K$. Nó có thể được được chứng minh rằng cycling không thể xảy ra nếu Bland’s quy tắc được chọn như phần tử trụ (pivot) quy tắc. chứng minh là rất technical; xem Chvatal $[40]$ (Chương $3$, các trang 37-38), Matousek và Gardner $[127]$ (Chương $5$, Định lý 5.8.1), và Papadimitriou và Steiglitz $[139]$ (Mục 2.7). Vì vậy, giả sử rằng một số ban đầu cơ bản nghiệm chấp nhận được (feasible solution) là miễn là/được cung cấp, và bằng cách sử dụng phù hợp phần tử trụ (pivot) quy tắc (chẳng hạn như Bland’s quy tắc), thuật toán đơn hình (simplex algorithm) luôn luôn kết thúc và hoặc cho ta nghiệm tối ưu (optimal solution) hoặc reports rằng bài toán quy hoạch tuyến tính (linear program) là không bị chặn. Không may là, Bland’s các quy tắc là một của slowest phần tử trụ (pivot) các quy tắc. lựa chọn của phần tử trụ (pivot) quy tắc affects greatly số của chọn phần tử trụ các bước rằng đơn hình (simplex) các thuật toán đi qua. Nó là không của ta intention ở đây đến giải thích khác nhau phần tử trụ (pivot) các quy tắc. Ta đơn giản mention sau đây các quy tắc, referring độc giả đến Matousek và Gardner $[127]$ (Chương $5$, Mục 5.7) hoặc đến các văn bản cited trong Mục 44.1. $1$. Lớn nhất hệ số, hoặc Dantzig’s quy tắc. $2$. Lớn nhất tăng. $3$. Steepest cạnh. $4$. Bland’s Quy tắc. $5$. Ngẫu nhiên cạnh.

<!-- PAGE 1620 -->
Steepest cạnh quy tắc là một của hầu hết popular. ý tưởng là để cực đại hóa tỉ số
$$\frac{c(u^{+}u)}{\|u^{+}-u\|} -.$$
Ngẫu nhiên cạnh quy tắc chọn chỉ số $j^{+} \in / K$ của entering cơ sở (basis) vectơ uniformly tại ngẫu nhiên trong số tất cả eligible các chỉ số. Cho chúng ta bây giờ trả về đến vấn đề của initialization của thuật toán đơn hình (simplex algorithm). Ta sử dụng Bài toán quy hoạch tuyến tính (linear program) $(P)$ đã giới thiệu during chứng minh của Định lý 45.7.
$$b$$
Xét Bài toán quy hoạch tuyến tính (linear program) (P2)
$$maximizecx$$
$$subject toAx = b and x \ge 0,$$
Trong tiêu chuẩn tạo thành ở đâu $A$ là một ma trận cỡ $m \times  n$ của hạng (rank) $m$. Thứ nhất, nhận thấy rằng vì các ràng buộc là các phương trình, ta có thể đảm bảo rằng $b \ge 0$, bởi vì mọi phương trình $a_{i}x = b_{i}$ ở đâu $b_{i} < 0$ có thể được được thay thế bởi $-a_{i}x = -b_{i}$. tiếp theo bước là đến giới thiệu Bài toán quy hoạch tuyến tính (linear program) $(P)$ trong tiêu chuẩn tạo thành
$$b$$
$$maximize-(x_{n+1} + \cdots  + x_{n+m})$$
$$subject toAx = b andx \ge 0,$$
$$b b b$$
Ở đâu $A$ và $x$ được cho bởi $b  b$
$$Ab = \begin{pmatrix} A & I_{m} \end{pmatrix} ,xb = \begin{pmatrix} x_{1} \\ \vdots \\ x_{n+m} \end{pmatrix} .$$
Vì ta được giả sử rằng $b \ge 0$, vectơ $x = (0_{n}, b)$ là nghiệm chấp nhận được (feasible solution) của $(P)$, thực ra cơ bản
$$b b$$
Chấp nhận được (feasible) các nghiệm vì ma trận liên kết với các chỉ số $n+1, \dots  , n+m$ là ma trận đơn vị (identity matrix) $I_{m}$. Hơn nữa, vì $x_{i} \ge 0$ với mọi $i$, hàm mục tiêu (objective function) $-(x_{n+1} + \cdots  + x_{n+m})$ là bị chặn ở trên bởi $0$. Nếu ta execute thuật toán đơn hình (simplex algorithm) với phần tử trụ (pivot) quy tắc rằng ngăn cản cycling, bắt đầu với cơ bản nghiệm chấp nhận được (feasible solution) $(0_{n}, d)$, vì hàm mục tiêu (objective function) là bị chặn bởi $0$, thuật toán đơn hình (simplex algorithm) kết thúc với nghiệm tối ưu (optimal solution) cho trước bởi một số cơ bản nghiệm chấp nhận được (feasible solution), nói
$$\mathbb{R}^{n} \mathbb{R}^{m}$$
$(u^{*}, w^{*})$, với $u^{*} \in$ và $w^{*} \in$. Như trong chứng minh của Định lý 45.7, với mọi nghiệm chấp nhận được (feasible solution) $u \in$ P(, $b)$, vectơ $(u, 0_{m})$
$$̸$$
Là nghiệm tối ưu (optimal solution) của $(P)$. Vì vậy, nếu $w^{*} = 0$, thì $\mathcal{P}(A, b) = \emptyset$, vì ngược lại cho
$$b$$
Mọi nghiệm chấp nhận được (feasible solution) $u \in$ P(, $b)$ vectơ $(u, 0_{m})$ sẽ cho giá trị của hàm mục tiêu (objective function) $-(x_{n+1} + \cdots  + x_{n+m})$ bằng $0$, nhưng $(u^{*}, w^{*})$ cho ta chặt âm giá trị vì $w^{*} \neq  0$.
