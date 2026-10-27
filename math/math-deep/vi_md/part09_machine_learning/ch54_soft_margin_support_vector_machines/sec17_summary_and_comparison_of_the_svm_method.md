# Tóm tắt và Comparison của SVM Các phương pháp


<!-- PAGE 2053 -->
$$30$$
$$20$$
$$10$$
$$0$$
$$-10$$
$$-20$$
$$-30$$
$$-30-20-10010203040$$
$$Figure 54.25: Running (SVM_{s5}) on two sets of 30 points; K = 1/13000.$$
Của ta thứ hai chạy đã được tạo với $K = 1/13000$; xem Hình 54.25. Ta có $p_{m} = 30$ và $q_{m} = 30$ và ta xem rằng chiều rộng của dải phẳng (slab) là bit excessive. ví dụ này demonstrates rằng lề (margin) các đường thẳng cần không chứa dữ liệu các điểm. Phương pháp $(SVM_{s5})$ luôn luôn trả về giá trị cho $b$ và $\eta$ nhỏ hơn hơn giá trị được trả về bởi $(SVM_{s4})$ (bởi vì của số hạng $(1/2)b^{2}$ được cộng đến hàm mục tiêu (objective function)) nhưng trong ví dụ này difference là cũng nhỏ là noticed.

## 54.17 Tóm tắt và Comparison của SVM Các phương pháp

Trong chương này ta được xét sáu các biến thể cho việc giải lề mềm (soft margin) nhị phân phân loại bài toán cho hai các tập hợp của các điểm ${u_{i}}_{i=1}^{p}$ và ${v_{j}}_{j=1}^{q}$ bằng cách sử dụng hỗ trợ/giá (support) vectơ phân loại các phương pháp. mục tiêu là để tìm tách siêu phẳng (hyperplane) $H_{w,b}$ của phương trình $w^{\top}x -b = 0$. Ta cũng thử để tìm hai “lề (margin) các siêu phẳng” $H_{w,b+\delta}$ của phương trình $w^{\top}x$ - $b$ - $\delta  = 0$ (xanh lam lề (margin) siêu phẳng (hyperplane)) và $H_{w,b-\delta}$ của phương trình $w^{\top}x$ - $b + \delta  = 0$ (đỏ lề (margin) siêu phẳng (hyperplane)) sao cho $\delta$ là như big như khả dĩ/có thể và vẫn chưa số của misclassified các điểm được cực tiểu hóa, mà là đạt được bởi cho phép sai số $\epsilon_{i}  \ge 0$ với mọi điểm $u_{i}$, trong nghĩa rằng ràng buộc
$$w^{\top}u_{i} -b \ge \delta  -\epsilon_{i}$$
Nên đúng, và sai số $\xi_{j}  \ge 0$ với mọi điểm $v_{j}$, trong nghĩa rằng ràng buộc
$$-w^{\top}v_{j} + b \ge \delta  -\xi_{j}$$

<!-- PAGE 2054 -->
Nên đúng. mục tiêu là đến design hàm mục tiêu (objective function) rằng cực tiểu hóa $\epsilon$ và $\xi$ và các cực đại hóa $\delta$. tối ưu hóa bài toán nên cũng giải cho $w$ và $b$, và cho điều này một số ràng buộc có là placed trên $w$. Một cái khác mục tiêu là đến thử để sử dụng đối ngẫu (dual) bài toán quy hoạch để giải tối ưu hóa bài toán, bởi vì các nghiệm liên quan đến trong các tích, và do đó bài toán là amenable đến tổng quát hóa bằng cách sử dụng hạt nhân (kernel) các hàm. thứ nhất attempt, mà là để sử dụng hàm mục tiêu (objective function)
$$J(w, \epsilon , \xi , b, \delta ) = -\delta  + K \begin{pmatrix} \epsilon^{\top} & \xi^{\top} \end{pmatrix} 1_{p+q}$$
Và ràng buộc $w^{\top}w \le 1$, thực hiện không hoạt động/công trình rất tốt bởi vì điều này ràng buộc cần là guarded bởi Nhân tử Lagrange (Lagrange multiplier) $\gamma  \ge 0$, và kết quả là, cực tiểu hóa Hàm Lagrange (Lagrangian) $L$ để tìm đối ngẫu (dual) hàm $G$ cho phương trình cho việc giải $w$ của tạo thành
$$2\gamma w = -X^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} ,$$
Nhưng nếu các tập hợp ${u_{i}}_{i=1}^{p}$ và ${v_{j}}_{j=1}^{q}$ là không một cách tuyến tính khả ly, thì nghiệm tối ưu (optimal solution) có thể xảy ra cho $\gamma  = 0$, trong mà trường hợp nó là không thể để xác định $w$. Điều này là Bài toán $(SVM_{s1})$ được xét trong Mục 54.1. Lề mềm (soft margin) SVM $(SVM_{s1})$:
$$minimize-\delta  + K \begin{pmatrix} \epsilon_{i}  + & \xi_{j} \end{pmatrix} \sum_{i=1}^{p}  \sum_{j=1}^{q}$$
$$subject to$$
$$w^{\top}u_{i} -b \ge \delta  -\epsilon_{i} ,\epsilon_{i}  \ge 0i = 1, \dots  , p$$
$$-w^{\top}v_{j} + b \ge \delta  -\xi_{j} ,\xi_{j}  \ge 0j = 1, \dots  , q$$
$$w^{\top}w \le 1.$$
Nó là thông lệ đến viết $\ell = p + q$. Nó được hiển thị trong Mục 54.1 rằng đối ngẫu (dual) bài toán quy hoạch là tương đương đến sau đây cực tiểu hóa bài toán quy hoạch:

<!-- PAGE 2055 -->
Đối ngẫu (dual) của Lề mềm (soft margin) SVM $(SVM_{s1})$:
$$minimize \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = 1$$
$$0 \le \lambda_{i}  \le K,i = 1, \dots  , p$$
$$0 \le \mu_{j}  \le K,j = 1, \dots  , q.$$
Các điểm $u_{i}$ và $v_{j}$ là một cách tự nhiên được phân loại theo các giá trị của $\lambda_{i}$ và $\mu_{j}$. các số của các điểm trong mỗi category có trực tiếp influence trên lựa chọn của tham số $K$. Cho chúng ta summarize một số của các then chốt items từ Định nghĩa 54.1. các vectơ $u_{i}$ trên xanh lam lề (margin) $H_{w,b+\delta}$ và các vectơ $v_{j}$ trên đỏ lề (margin) $H_{w,b-\delta}$ được gọi là hỗ trợ/giá (support) các vectơ. Hỗ trợ/giá (support) các vectơ tương ứng với các vectơ $u_{i}$ cho mà $w^{\top}u_{i}$ - $b$ - $\delta  = 0$ (mà suy ra $\epsilon_{i}  = 0)$, và các vectơ $v_{j}$ cho mà $w^{\top}v_{j}$ - $b + \delta  = 0$ (mà suy ra $\xi_{j}  = 0)$. Hỗ trợ/giá (support) các vectơ $u_{i}$ sao cho $0 < \lambda_{i}  < K$ và hỗ trợ/giá (support) các vectơ $v_{j}$ sao cho $0 < \mu_{j}  < K$ là hỗ trợ/giá (support) các vectơ của loại/kiểu $1$. Hỗ trợ/giá (support) các vectơ của loại/kiểu $1$ đóng đặc biệt vai trò do đó ta ký hiệu các tập hợp của các chỉ số liên kết với chúng bởi
$$I_{\lambda} = {i \in {1, \dots  , p} | 0 < \lambda_{i}  < K}$$
$$I_{\mu} = {j \in {1, \dots  , q} | 0 < \mu_{j}  < K}.$$
Ta ký hiệu của chúng cardinalities bởi $numsvl_{1} = |I_{\lambda}|$ và $numsvm_{1} = |I_{\mu}|$. các vectơ $u_{i}$ cho mà $\lambda_{i}  = K$ và các vectơ $v_{j}$ cho mà $\mu_{j}  = K$ được nói đến thất bại lề (margin). các tập hợp của các chỉ số liên kết với các vectơ thất bại lề (margin) được ký hiệu bởi
$$K_{\lambda} = {i \in {1, \dots  , p} | \lambda_{i}  = K}$$
$$K_{\mu} = {j \in {1, \dots  , q} | \mu_{j}  = K}.$$
Ta ký hiệu của chúng cardinalities bởi $p_{f} = |K_{\lambda}|$ và $q_{f} = |K_{\mu}|$. Các vectơ $u_{i}$ sao cho $\lambda_{i}  > 0$ và các vectơ $v_{j}$ sao cho $\mu_{j}  > 0$ được nói đến có lề (margin) nhiều nhất $\delta$. các tập hợp của các chỉ số liên kết với các vectơ này được ký hiệu bởi
$$I_{\lambda >0} = {i \in {1, \dots  , p} | \lambda_{i}  > 0}$$
$$I_{\mu >0} = {j \in {1, \dots  , q} | \mu_{j}  > 0}.$$

<!-- PAGE 2056 -->
Ta ký hiệu của chúng cardinalities bởi $p_{m} = |I_{\lambda >0}|$ và $q_{m} = |I_{\mu >0}|$. Hiển nhiên, $p_{f} \le p_{m}$ và $q_{f} \le q_{m}$. Có $p$ - $p_{m}$ các điểm $u_{i}$ được phân loại một cách chính xác trên xanh lam vế/cạnh và bên ngoài $\delta$ -dải phẳng (slab) và có $q -q_{m}$ các điểm $v_{j}$ được phân loại một cách chính xác trên đỏ vế/cạnh và bên ngoài $\delta$ -dải phẳng (slab). Một cách trực quan xanh lam điểm rằng không thỏa mãn lề (margin) là trên sai vế/cạnh của xanh lam lề (margin) và đỏ điểm rằng không thỏa mãn lề (margin) là trên sai vế/cạnh của đỏ lề (margin). Nó có thể được được hiển thị rằng rằng $K$ phải được chọn sao cho
$$ $$
$$\max \frac{1}{2p_{m}} , \frac{1}{2q_{m}} \le K \le \min \frac{1}{2p_{f}} , \frac{1}{2q_{f}} .$$
$$If the optimal value is 0, then \gamma  = 0 and X \begin{pmatrix} \lambda \\ \mu \\ > \end{pmatrix} = 0, so in this case it is not possible$$
Để xác định $w$. Tuy nhiên, nếu giá trị tối ưu (optimal value) là $0$, thì một lần nghiệm cho $\lambda$ và $\mu$ là thu được, ta có
$$1/2$$
$$\gamma  = \frac{1}{2} \begin{pmatrix}   \\ \lambda^{\top} & \mu^{\top} \\  \end{pmatrix} \begin{pmatrix} \lambda \\ X^{\top}X & \mu \end{pmatrix} \begin{pmatrix}\end{pmatrix}$$
$$w = \frac{1}{2\gamma} \begin{pmatrix} \lambda_{i} u_{i} - & \mu_{j} v_{j} \end{pmatrix} \sum_{i=1}^{p}  \sum_{j=1}^{q}  ,$$
Do đó ta thu được
$$\sum_{i=1}^{p}  \lambda_{i} u_{i} - \sum_{j=1}^{q}  \mu_{j} v_{j}$$
$$w =,$$
$$\overline{1}\overline{/}\overline{2}$$
$$\begin{pmatrix} \overline{ } & \overline{}\lambda \\ \lambda^{\top} & \mu^{\top} X^{\top}X & \mu \\ holds,thenband\delta \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix}\end{pmatrix}$$
Nếu sau đây nhẹ giả thiết có thể được tìm thấy. Tiêu chuẩn Lề (margin) Giả thiết cho $(SVM_{s1})$. Tồn tại một chỉ số $i_{0}$ sao cho $0 < \lambda_{i0}  < K$ và tồn tại một chỉ số $j_{0}$ sao cho $0 < \mu_{j0}  < K$. Điều này có nghĩa là một số $u_{i0}$ là hỗ trợ/giá (support) vectơ của loại/kiểu $1$ trên xanh lam lề (margin), và một số $v_{j0}$ là hỗ trợ/giá (support) vectơ của loại/kiểu $1$ trên đỏ lề (margin). Nếu Tiêu chuẩn Lề (margin) Giả thiết cho $(SVM_{s1})$ nghiệm đúng, thì $\epsilon_{i0}  = 0$ và $\mu_{j0}  = 0$, và ta có hoạt động các phương trình
$$w^{\top}u_{i0} -b = \delta and-w^{\top}v_{j0} + b = \delta ,$$
Và ta thu được giá trị của $b$ và $\delta$ như
$$b = \frac{1}{2} w^{\top}(u_{i0} + v_{j0})$$
$$\delta  = \frac{1}{2} w^{\top}(u_{i0} -v_{j0}).$$

<!-- PAGE 2057 -->
Thứ hai nhiều hơn/thêm successful cách tiếp cận là đến cộng số hạng $(1/2)w^{\top}w$ đến hàm mục tiêu (objective function) và đến bỏ ràng buộc $w^{\top}w \le 1$. Có một vài các biến thể của phương pháp này, tùy thuộc trên lựa chọn của regularizing số hạng liên quan đến $\epsilon$ và $\xi$ (tuyến tính hoặc toàn phương), cách mà lề (margin) là dealt với (một cách ẩn với số hạng $1$ hoặc một cách tường minh với số hạng $\eta$), và liệu số hạng $(1/2)b^{2}$ được cộng đến hàm mục tiêu (objective function) hoặc không. các phương pháp này tất cả share tính chất rằng nếu bài toán gốc (primal problem) có nghiệm tối ưu (optimal solution) với $w \neq  0$, thì bài toán đối ngẫu (dual problem) luôn luôn xác định $w$, và thì dưới nhẹ các điều kiện mà ta gọi tiêu chuẩn lề (margin) các giả thiết, $b$ và $\eta$ có thể được được xác định. Thì $\epsilon$ và $\xi$ có thể được được xác định bằng cách sử dụng các ràng buộc rằng là hoạt động. Khi $(1/2)b^{2}$ được cộng đến hàm mục tiêu (objective function), $b$ được xác định bởi phương trình
$$b = -(1_{p}^{\top} \lambda  -1_{q}^{\top} \mu ).$$
Tất cả các bài tập này là lồi và các ràng buộc là qualified, do đó khoảng cách đối ngẫu (duality gap) là không, và nếu gốc (primal) có nghiệm tối ưu (optimal solution) với $w \neq  0$, thì suy ra rằng $\eta  \ge 0$. Ta bây giờ xét năm các biến thể trong nhiều hơn/thêm chi tiết.
$(1)$ Cơ bản lề mềm (soft margin) SVM: $(SVM_{s2})$.
$$This is the optimization problem in which the regularization term K \begin{pmatrix} \epsilon^{\top} & \xi^{\top} \end{pmatrix} 1_{p+q} is$$
Tuyến tính và lề (margin) $\delta$ được cho bởi $\delta  = 1/ \|w\|$:
$$minimize \frac{1}{2} w^{\top}w + K \begin{pmatrix} \epsilon^{\top} & \xi^{\top} \end{pmatrix} 1_{p+q}$$
$$subject to$$
$$w^{\top}u_{i} -b \ge 1 -\epsilon_{i} ,\epsilon_{i}  \ge 0i = 1, \dots  , p$$
$$-w^{\top}v_{j} + b \ge 1 -\xi_{j} ,\xi_{j}  \ge 0j = 1, \dots  , q.$$
Bài toán này là cổ điển một được thảo luận trong tất cả các cuốn sách trên máy học (learning) hoặc pattern giải tích/phân tích, chẳng hạn Vapnik $[188]$, Bishop $[23]$, và Shawe–Taylor và Christianini $[165]$. Nó được hiển thị trong Mục 54.3 rằng đối ngẫu (dual) bài toán quy hoạch là Đối ngẫu (dual) của Cơ bản lề mềm (soft margin) SVM: $(SVM_{s2})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} - \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$0 \le \lambda_{i}  \le K,i = 1, \dots  , p$$
$$0 \le \mu_{j}  \le K,j = 1, \dots  , q.$$

<!-- PAGE 2058 -->
Ta có thể sử dụng đối ngẫu (dual) bài toán quy hoạch để giải gốc (primal). Một lần $\lambda  \ge 0, \mu  \ge 0$ có đã được tìm thấy, $w$ được cho bởi
$$w = -X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = \sum_{i=1}^{p}  \lambda_{i} u_{i} - \sum_{j=1}^{q}  \mu_{j} v_{j},$$
Nhưng $b$ là không được xác định bởi đối ngẫu (dual). độ bù lỏng (complementary slackness) các điều kiện suy ra rằng nếu $\epsilon_{i}  > 0$, thì $\lambda_{i}  = K$, và nếu $\xi_{j}  > 0$, thì $\mu_{j}  = K$. Hệ quả là, nếu $\lambda_{i}  < K$, thì $\epsilon_{i}  = 0$ và $u_{i}$ là một cách chính xác được phân loại, và tương tự nếu $\mu_{j}  < K$, thì $\xi_{j}  = 0$ và $v_{j}$ là một cách chính xác được phân loại. Tiên nghiệm (a priori) không có gì ngăn cản tình huống ở đâu $\lambda_{i}  = K$ với mọi khác không $\lambda_{i}$ hoặc $\mu_{j}  = K$ với mọi khác không $\mu_{j}$. Nếu điều này xảy ra, ta có thể rerun tối ưu hóa phương pháp với lớn hơn giá trị của $K$. Nếu sau đây nhẹ giả thiết nghiệm đúng thì $b$ có thể được tìm thấy. Tiêu chuẩn Lề (margin) Giả thiết cho $(SVM_{s2})$. Tồn tại một hỗ trợ/giá (support) vectơ $u_{i0}$ của loại/kiểu $1$ trên xanh lam lề (margin), và một số hỗ trợ/giá (support) vectơ $v_{j0}$ của loại/kiểu $1$ trên đỏ lề (margin). Nếu Tiêu chuẩn Lề (margin) Giả thiết cho $(SVM_{s2})$ nghiệm đúng thì $\epsilon_{i0}  = 0$ và $\mu_{j0}  = 0$, và thì ta có hoạt động các phương trình
$$w^{\top}u_{i0} -b = 1and-w^{\top}v_{j0} + b = 1,$$
Và ta thu được
$$b = \frac{1}{2} w^{\top}(u_{i0} + v_{j0}).$$
$(2)$ Cơ bản Lề mềm (soft margin) $\nu$ -SVM Bài toán $(SVM_{s2'})$. Điều này tổng quát hóa của Bài toán $(SVM_{s2})$ cho phiên bản của lề mềm (soft margin) SVM coming từ Bài toán $(SVM_{h2})$, thu được bằng cách cộng extra bậc của freedom, cụ thể là thay vì của lề (margin) $\delta  = 1/ \|w\|$, ta sử dụng lề (margin) $\delta  = \eta / \|w\|$ ở đâu $\eta$ là một số dương hằng số rằng ta muốn để cực đại hóa. Đến thực hiện do đó, ta cộng số hạng $-K_{m}\eta$ đến hàm mục tiêu (objective function). Ta có kết quả sau tối ưu hóa bài toán:
$$minimize \frac{1}{2} w^{\top}w -K_{m}\eta  + K_{s} \begin{pmatrix} \epsilon^{\top} & \xi^{\top} \end{pmatrix} 1_{p+q}$$
$$subject to$$
$$w^{\top}u_{i} -b \ge \eta  -\epsilon_{i} ,\epsilon_{i}  \ge 0i = 1, \dots  , p$$
$$-w^{\top}v_{j} + b \ge \eta  -\xi_{j} ,\xi_{j}  \ge 0j = 1, \dots  , q$$
$$\eta  \ge 0,$$
Ở đâu $K_{m} > 0$ và $K_{s} > 0$ là cố định các hằng số rằng có thể được adjusted để xác định influence của $\eta$ và regularizing số hạng.

<!-- PAGE 2059 -->
Điều này phiên bản của SVM bài toán đã là thứ nhất được thảo luận trong Sch¨olkopf, Smola, Williamson, và Bartlett $[153]$ dưới name của $\nu$ -SVC, và cũng được sử dụng trong Sch¨olkopf, Platt, Shawe– Taylor, và Smola $[152]$. Trong thứ tự cho bài toán đến có nghiệm ta phải chọn $K_{m}$ và $K_{s}$ sao cho
$$K_{m} \le \min{2pK_{s}, 2qK_{s}}.$$
Nó được hiển thị trong Mục 54.5 rằng đối ngẫu (dual) bài toán quy hoạch là Đối ngẫu (dual) của Cơ bản Lề mềm (soft margin) $\nu$ -SVM Bài toán $(SVM_{s2'})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  \ge K_{m}$$
$$0 \le \lambda_{i}  \le K_{s},i = 1, \dots  , p$$
$$0 \le \mu_{j}  \le K_{s},j = 1, \dots  , q.$$
Nếu bài toán gốc (primal problem) có nghiệm tối ưu (optimal solution) với $w \neq  0$, thì bằng cách sử dụng sự kiện rằng khoảng cách đối ngẫu (duality gap) là không ta có thể chỉ ra rằng $\eta  \ge 0$. Do đó ràng buộc $\eta  \ge 0$ có thể được bỏ qua. Như trong trước đó trường hợp $w$ được cho bởi
$$w = -X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = \sum_{i=1}^{p}  \lambda_{i} u_{i} - \sum_{j=1}^{q}  \mu_{j} v_{j},$$
Nhưng $b$ và $\eta$ là không được xác định bởi đối ngẫu (dual). Nếu ta bỏ ràng buộc $\eta  \ge 0$, thì bất đẳng thức
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  \ge K_{m}$$
Được thay thế bởi phương trình
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = K_{m}.$$
Nó thuận tiện để định nghĩa $\nu  > 0$ sao cho
$$\nu  = \frac{K_{m}}{(p + q)K_{s}} ,$$

<!-- PAGE 2060 -->
Sao cho hàm mục tiêu (objective function) J(w, $\epsilon , \xi , b, \eta$) được cho bởi
$$J(w, \epsilon , \xi , b, \eta ) = \frac{1}{2} w^{\top}w + (p + q)K_{s} \begin{pmatrix} 1 \\ -\nu \eta  + &  \epsilon^{\top} & \xi^{\top} \\ p + q \end{pmatrix} \begin{pmatrix} 1_{p+q} \end{pmatrix} .$$
Vì ta thu được tương đương bài toán bởi rescaling bởi chung/phổ biến dương nhân tử, về mặt lý thuyết nó là thuận tiện đến chuẩn hóa $K_{s}$ như
$$K_{s} = \frac{1}{p + q} ,$$
Trong mà trường hợp $K_{m} = \nu$. phương pháp này được gọi là $\nu$ -máy vectơ hỗ trợ (SVM). Dưới Tiêu chuẩn Lề (margin) Giả thiết cho $(SVM_{s2'})$, tồn tại một hỗ trợ/giá (support) vectơ $u_{i0}$ của loại/kiểu $1$ và một số hỗ trợ/giá (support) vectơ $v_{j0}$ của loại/kiểu $1$, và bởi độ bù lỏng (complementary slackness) các điều kiện $\epsilon_{i0}  = 0$ và $\xi_{j0}  = 0$, do đó ta có hai hoạt động các ràng buộc
$$w^{\top}u_{i0} -b = \eta ,-w^{\top}v_{j0} + b = \eta ,$$
Và ta có thể giải cho $b$ và $\eta$ và ta thu được
$$b = \frac{w^{\top}(u_{i0}+ v_{j0})}{2}$$
$$-$$
$$\eta  = \frac{w^{\top}(u_{i0}v_{j0})}{2} .$$
Do số tính mất ổn định, khi viết máy tính bài toán quy hoạch nó được ưu tiên hơn để tính các danh sách của các chỉ số $I_{\lambda}$ và $I_{\mu}$ cho trước bởi
$$I_{\lambda} = {i \in {1, \dots  , p} | 0 < \lambda_{i}  < K_{s}},I_{\mu} = {j \in {1, \dots  , q} | 0 < \mu_{j}  < K_{s}}.$$
Thì $b$ và $\eta$ được cho bởi sau đây lấy trung bình các công thức:
$$ \sum_{\in I\lambda}  \sum_{\in I\mu}  $$
$$b = w^{\top}/|I_{\lambda}| +/|I_{\mu}|/2$$
$$ \begin{pmatrix} u_{i} \\ i \end{pmatrix} \begin{pmatrix} v_{j} \\ j \end{pmatrix} $$
$$ \sum_{i\in I\lambda}  \sum_{j\in I\mu}  $$
$$\eta  = w^{\top}/|I_{\lambda}| -/|I_{\mu}|/2.$$
$$ \begin{pmatrix} u_{i} \end{pmatrix} \begin{pmatrix} v_{j} \end{pmatrix} $$
Mệnh đề 54.1 cho ta các cận trên $\nu$ cho phương pháp đến hội tụ, cụ thể là
$$  $$
$$\max \frac{2p_{f}}{p + q} , \frac{2q_{f}}{p + q} \le \nu  \le \min \frac{2p_{m}}{p + q} , \frac{2q_{m}}{p + q} .$$

<!-- PAGE 2061 -->
Trong Mục 54.7 ta investigate các điều kiện trên $\nu$ rằng đảm bảo rằng một số điểm $u_{i0}$ và một số điểm $v_{j0}$ là hỗ trợ/giá (support) vectơ. Định lý 54.3 chỉ ra rằng với mọi nghiệm tối ưu (optimal solution) $(w, b, \eta , \epsilon , \xi$) của Bài toán $(SVM_{s2'})$ với $w \neq  0$ và $\eta  > 0$, nếu
$$\max{2p_{f}/(p + q), 2q_{f}/(p + q)} < \nu  < \min{2p/(p + q), 2q/(p + q)},$$
Thì một số $u_{i0}$ và một số $v_{j0}$ là hỗ trợ/giá (support) vectơ. Dưới cùng các điều kiện trên $\nu$ Mệnh đề 54.4 chỉ ra rằng $\eta$ và $b$ có thể luôn luôn được xác định theo $(\lambda , \mu$) bằng cách sử dụng đơn lẻ hỗ trợ/giá (support) vectơ.
$(3)$ Lề mềm (soft margin) $\nu$ -SVM Bài toán $(SVM_{s3})$. Điều này là variation của Bài toán $(SVM_{s2'})$ thu được bằng cách cộng số hạng $(1/2)b^{2}$ đến hàm mục tiêu (objective function). kết quả là rằng trong cực tiểu hóa Hàm Lagrange (Lagrangian) để tìm đối ngẫu (dual) hàm $G$, không chỉ $w$ nhưng cũng $b$ được xác định. Ta cũng suppress ràng buộc $\eta  \ge 0$ mà hóa ra là redundant. Nếu $\nu  > (p_{f} +q_{f})/(p+q)$, thì $\eta$ cũng được xác định. sự kiện rằng $b$ và $\eta$ được xác định bởi đối ngẫu (dual) dường như là advantage của Bài toán $(SVM_{s3})$. tối ưu hóa bài toán là
$$+ ($$
$$minimize \frac{1}{2} w^{\top}w + \frac{1}{2} b^{2}p + q)K_{s} \begin{pmatrix} 1 \\ -\nu \eta  + &  \epsilon^{\top} & \xi^{\top} \\ p + q \end{pmatrix} \begin{pmatrix} 1_{p+q} \end{pmatrix}$$
$$subject to$$
$$w^{\top}u_{i} -b \ge \eta  -\epsilon_{i} ,\epsilon_{i}  \ge 0i = 1, \dots  , p$$
$$-w^{\top}v_{j} + b \ge \eta  -\xi_{j} ,\xi_{j}  \ge 0j = 1, \dots  , q.$$
Về mặt lý thuyết nó là thuận tiện giả sử rằng $K_{s} = 1/(p + q)$. Ngược lại, $\nu$ cần được thay thế bởi $(p + q)K_{s}\nu$ trong tất cả các công thức ở dưới. Nó được hiển thị trong Mục 54.13 rằng đối ngẫu (dual) được cho bởi Đối ngẫu (dual) của Lề mềm (soft margin) $\nu$ -SVM Bài toán $(SVM_{s3})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ X^{\top}X+ & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = \nu$$
$$0 \le \lambda_{i}  \le K_{s},i = 1, \dots  , p$$
$$0 \le \mu_{j}  \le K_{s},j = 1, \dots  , q.$$

<!-- PAGE 2062 -->
Một lần nghiệm cho $\lambda$ và $\mu$ là thu được, ta có
$$w = -X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = \sum_{i=1}^{p}  \lambda_{i} u_{i} - \sum_{j=1}^{q}  \mu_{j} v_{j}$$
$$b = - \sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j} .$$
Lưu ý rằng ràng buộc
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
Xảy ra trong đối ngẫu (dual) của Bài toán quy hoạch $(SVM_{s2'})$ có đã được traded cho phương trình
$$b = - \sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}$$
Xác định $b$. Nếu $\nu  > (p_{f} + q_{f})/(p + q)$, thì $\eta$ được xác định bởi biểu diễn rằng khoảng cách đối ngẫu (duality gap) là không. Ta thu được
$$((p + q)\nu  -p_{f} -q_{f})\eta  = (p_{f} -q_{f})b + w^{\top} \begin{pmatrix} v_{j}- & u_{i} \\ j \\  \end{pmatrix} \sum_{\in K\mu}  \sum_{i\in K\lambda}$$
$$+ \frac{1}{K_{s}} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ X^{\top}X+ & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} .$$
Trong thực tế một cái khác cách để tính $\eta$ là giả sử Tiêu chuẩn Lề (margin) Giả thiết cho $(SVM_{s3})$. Dưới Tiêu chuẩn Lề (margin) Giả thiết cho $(SVM_{s3})$, hoặc một số $u_{i0}$ là hỗ trợ/giá (support) vectơ của loại/kiểu $1$ hoặc một số $v_{j0}$ là hỗ trợ/giá (support) vectơ của loại/kiểu $1$. Bởi độ bù lỏng (complementary slackness) các điều kiện $\epsilon_{i0}  = 0$ hoặc $\xi_{j0}  = 0$, do đó ta có
$$w^{\top}u_{i0} -b = \eta ,or-w^{\top}v_{j0} + b = \eta ,$$
Và ta có thể giải cho $\eta$. Như trong $(SVM_{s2'})$ ta thu được nhiều hơn/thêm một cách số stable các công thức bởi lấy trung bình trên các tập hợp $I_{\lambda}$ và $I_{\mu}$. Mệnh đề 54.5 cho các cận $\nu$, cụ thể là
$$\frac{p_{f}+ q_{f}}{p + q} \le \nu  \le \frac{p_{m} + q_{m}}{p + q} .$$
Trong Mục 54.11 ta investigate các điều kiện trên $\nu$ rằng đảm bảo rằng hoặc tồn tại một xanh lam hỗ trợ/giá (support) vectơ $u_{i0}$ hoặc tồn tại một đỏ hỗ trợ/giá (support) vectơ $v_{j0}$. Định lý 54.7 chỉ ra

<!-- PAGE 2063 -->
Rằng với mọi nghiệm tối ưu (optimal solution) $(w, b, \eta , \epsilon , \xi$) của Bài toán $(SVM_{s3})$ với $w \neq  0$ và $\eta  > 0$, nếu
$$(p_{sf} + q_{sf})/(p + q) < \nu  < 1,$$
Thì một số $u_{i0}$ hoặc một số $v_{j0}$ là hỗ trợ/giá (support) vectơ.
$(4)$ Cơ bản Toàn phương Lề mềm (soft margin) $\nu$ -SVM Bài toán $(SVM_{s4})$. Điều này là phiên bản của
$$Problem (SVM_{s2'}) in which instead of using the linear function K_{s} \begin{pmatrix} \epsilon^{\top} & \xi^{\top} \\ The \end{pmatrix} 1_{p+q} as a$$
Regularizing hàm ta sử dụng toàn phương hàm $K(\|\epsilon \|_{2}^{2} + \|\xi \|_{2}^{2})$. tối ưu hóa bài toán là
$$minimize \frac{1}{2} w^{\top}w + (p + q)K_{s} \begin{pmatrix} 1 \\ -\nu \eta  + & (\epsilon^{\top} \epsilon  + \xi^{\top} \xi ) \\ p + q \end{pmatrix}$$
$$subject to$$
$$w^{\top}u_{i} -b \ge \eta  -\epsilon_{i} ,i = 1, \dots  , p$$
$$-w^{\top}v_{j} + b \ge \eta  -\xi_{j} ,j = 1, \dots  , q$$
$$\eta  \ge 0,$$
Ở đâu $\nu$ và $K_{s}$ là hai cho trước dương các hằng số. Như ta đã thấy trước đó, về mặt lý thuyết, nó là thuận tiện đến chọn $K_{s} = 1/(p + q)$. Khi viết máy tính bài toán quy hoạch, nó được ưu tiên hơn giả sử rằng $K_{s}$ là tùy ý. Trong điều này trường hợp $\nu$ cần được thay thế bởi $(p + q)K_{s}\nu$ trong tất cả các công thức thu được với $K_{s} = 1/(p + q)$. Trong phương pháp này, nó là không có dài hơn cần đến đòi hỏi $\epsilon  \ge 0$ và $\xi  \ge 0$, bởi vì nghiệm tối ưu (optimal solution) thỏa mãn các điều kiện này. Một của advantages của các phương pháp này là rằng $\epsilon$ được xác định bởi $\lambda , \xi$ được xác định bởi $\mu$, và $\eta$ và $b$ được xác định bởi $\lambda$ và $\mu$. Ta có thể bỏ qua ràng buộc $\eta  \ge 0$, bởi vì cho nghiệm tối ưu (optimal solution) nó có thể được được hiển thị bằng cách sử dụng đối ngẫu rằng $\eta  \ge 0$; xem Mục 54.14. Cho $K_{s}$ và $\nu$ cố định, nếu Bài toán quy hoạch $(SVM_{s4})$ có nghiệm tối ưu (optimal solution), thì nó là duy nhất; xem

> **Định lý 54.8.** drawback của Bài toán quy hoạch $(SVM_{s4})$ là rằng cho cố định $K_{s}$, đại lượng $\delta  = \eta / \|w\|$ và các siêu phẳng $H_{w,b}, H_{w,b+\eta}$ và $H_{w,b-\eta}$ là độc lập của $\nu$. Điều này được hiển thị trong Định lý 54.8. Do đó phương pháp này là ít hơn flexible hơn $(SVM_{s2'})$ và $(SVM_{s3})$. Nó được hiển thị trong Mục 54.9 rằng đối ngẫu (dual) được cho bởi

<!-- PAGE 2064 -->
Đối ngẫu (dual) của Cơ bản Toàn phương Lề mềm (soft margin) $\nu$ -SVM Bài toán $(SVM_{s4})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1 \\ X^{\top}X+ & K I_{p+q} \\ 2 \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  \ge \nu$$
$$\lambda_{i}  \ge 0,i = 1, \dots  , p$$
$$\mu_{j}  \ge 0,j = 1, \dots  , q.$$
Ở trên bài toán quy hoạch là đồng dạng đến bài toán quy hoạch rằng đã là thu được cho Bài toán $(SVM_{s2'})$ nhưng ma trận $X^{\top}X$ được thay thế bởi ma trận $X^{\top}X + (1/2K)I_{p+q}$, mà là xác định dương (positive definite) vì $K > 0$, và cũng các bất đẳng thức $\lambda_{i}  \le K$ và $\mu_{j}  \le K$ không có dài hơn đúng. Nếu ràng buộc $\eta  \ge 0$ là dropped, thì bất đẳng thức
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  \ge \nu$$
Được thay thế bởi phương trình
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = \nu .$$
Ta thu được $w$ từ $\lambda$ và $\mu$, và $\gamma$, như trong Bài toán $(SVM_{s2'})$; cụ thể là,
$$w = -X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = \sum_{i=1}^{p}  \lambda_{i} u_{i} - \sum_{j=1}^{q}  \mu_{j} v_{j}$$
Và $\eta$ được cho bởi
$$(p + q)K_{s}\nu \eta  = \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1 \\ X^{\top}X+ & I_{p+q} \\ 2K_{s} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} .$$
Các ràng buộc suy ra rằng tồn tại một $i_{o}$ sao cho $\lambda_{i0}  > 0$ và một số $j_{0}$ sao cho $\mu_{j0}  > 0$, mà có nghĩa là ít nhất hai các điểm là misclassified, do đó Bài toán $(SVM_{s4})$ nên chỉ được sử dụng khi các tập hợp ${u_{i}}$ và ${v_{j}}$ là không một cách tuyến tính khả ly. Ta có thể giải cho $b$ bằng cách sử dụng hoạt động các ràng buộc tương ứng với bất kỳ $i_{0}$ sao cho $\lambda_{i0}  > 0$ và bất kỳ $j_{0}$ sao cho $\mu_{j0}  > 0$. Đến cải thiện số tính ổn định ta trung bình trên các tập hợp của các chỉ số $I_{\lambda}$ và $I_{\mu}$.

<!-- PAGE 2065 -->
$(5)$ Toàn phương Lề mềm (soft margin) $\nu$ -SVM Bài toán $(SVM_{s5})$. Điều này là biến thể của Bài toán $(SVM_{s4})$ trong mà ta cộng số hạng $(1/2)b^{2}$ đến hàm mục tiêu (objective function). Ta cũng bỏ ràng buộc $\eta  \ge 0$ mà là redundant. Ta có kết quả sau tối ưu hóa bài toán:
$$+ ($$
$$minimize \frac{1}{2} w^{\top}w + \frac{1}{2} b^{2}p + q)K_{s} \begin{pmatrix} 1 \\ -\nu \eta  + & (\epsilon^{\top} \epsilon  + \xi^{\top} \xi ) \\ p + q \end{pmatrix}$$
$$subject to$$
$$w^{\top}u_{i} -b \ge \eta  -\epsilon_{i} ,i = 1, \dots  , p$$
$$-w^{\top}v_{j} + b \ge \eta  -\xi_{j} ,j = 1, \dots  , q,$$
Ở đâu $\nu$ và $K_{s}$ là hai cho trước dương các hằng số. Như ta đã thấy trước đó, nó là thuận tiện đến chọn $K_{s} = 1/(p + q)$. Khi viết máy tính bài toán quy hoạch, nó được ưu tiên hơn giả sử rằng $K_{s}$ là tùy ý. Trong điều này trường hợp $\nu$ phải được thay thế bởi $(p + q)K_{s}\nu$ trong tất cả các công thức. Một của advantages của các phương pháp này là rằng $\epsilon$ được xác định bởi $\lambda , \xi$ được xác định bởi $\mu$ (như trong $(SVM_{s4}))$, và cả hai $\eta$ và $b$ được xác định bởi $\lambda$ và $\mu$. Ta có thể bỏ qua ràng buộc $\eta  \ge 0$, bởi vì cho nghiệm tối ưu (optimal solution) nó có thể được được hiển thị bằng cách sử dụng đối ngẫu rằng $\eta  \ge 0$. Cho $K_{s}$ và $\nu$ cố định, nếu Bài toán quy hoạch $(SVM_{s5})$ có nghiệm tối ưu (optimal solution), thì nó là duy nhất; xem Định lý 54.9. drawback của Bài toán quy hoạch $(SVM_{s5})$ là rằng cho cố định $K_{s}$, đại lượng $\delta  = \eta / \|w\|$ và các siêu phẳng $H_{w,b}, H_{w,b+\eta}$ và $H_{w,b-\eta}$ là độc lập của $\nu$. Điều này được hiển thị trong Định lý 54.9. Do đó phương pháp này là ít hơn flexible hơn $(SVM_{s2'})$ và $(SVM_{s3})$. Nó được hiển thị trong Mục 54.15 rằng đối ngẫu (dual) của Bài toán quy hoạch $(SVM_{s5})$ được cho bởi Đối ngẫu (dual) của Toàn phương Lề mềm (soft margin) $\nu$ -SVM Bài toán $(SVM_{s5})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ X^{\top}X+ & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} \begin{pmatrix} 1 \\ + & K I_{p+q} \\ 2 \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = \nu$$
$$\lambda_{i}  \ge 0,i = 1, \dots  , p$$
$$\mu_{j}  \ge 0,j = 1, \dots  , q.$$
