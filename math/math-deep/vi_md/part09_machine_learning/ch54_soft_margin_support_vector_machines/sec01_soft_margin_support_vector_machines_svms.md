# Lề mềm (soft margin) Các máy vectơ hỗ trợ (SVMs); (SVMs1)


<!-- PAGE 1970 -->
Ví dụ, nếu $p = 2$ và $q = 3$, ta có ma trận
$$K = \begin{pmatrix} \kappa (u_{1}, u_{1}) & \kappa (u_{1}, u_{2}) & -\kappa (u_{1}, v_{1}) & -\kappa (u_{1}, v_{2}) & -\kappa (u_{1}, v_{3}) \\ \kappa (u_{2}, u_{1}) & \kappa (u_{2}, u_{2}) & -\kappa (u_{2}, v_{1}) & -\kappa (u_{2}, v_{2}) & -\kappa (u_{2}, v_{3}) \\ -\kappa (v_{1}, u_{1}) & -\kappa (v_{1}, u_{2}) & \kappa (v_{1}, v_{1}) & \kappa (v_{1}, v_{2}) & \kappa (v_{1}, v_{3}) \\ -\kappa (v_{2}, u_{1}) & -\kappa (v_{2}, u_{2}) & \kappa (v_{2}, v_{1}) & \kappa (v_{2}, v_{2}) & \kappa (v_{2}, v_{3}) \\ \kappa (v_{3}, u_{1}) & \kappa (v_{3}, u_{2}) & \kappa (v_{3}, v_{1}) & \kappa (v_{3}, v_{2}) & \kappa (v_{3}, v_{3}) \end{pmatrix} .$$
$$--$$
Thì phân loại hàm
$$f(x) = sgn(\langle w, \phi (x)\rangle -b)$$
$$\mathbb{R}^{n}$$
Cho các điểm trong ban đầu dữ liệu không gian cũng được biểu diễn solely theo ma trận $K$ và trong các tích $\kappa (u_{i}, x) = \langle \phi (u_{i}), \phi (x)\rangle$ và $\kappa (v_{j}, x) = \langle \phi (v_{j}), \phi (x)\rangle$. Hệ quả là, trong ban đầu dữ liệu không gian $\mathbb{R}^{n}$, hypersurface
$$\mathbb{R}^{n}$$
$$\mathcal{S} = {x \in | \langle w, \phi (x)\rangle -b = 0}$$
Tách dữ liệu các điểm $u_{i}$ và $v_{j}$, nhưng nó là không không gian con afin (affine subspace) $of\mathbb{R}^{n}$. phân loại hàm $f$ cho ta biết chúng ta trên mà “vế/cạnh” của $\mathcal{S}$ là mới dữ liệu điểm $x \in \mathbb{R}^{n}$. Do đó, ta managed đến tách dữ liệu các điểm $u_{i}$ và $v_{j}$ rằng là không khả ly bởi afin siêu phẳng (hyperplane), bởi
$$\mathbb{R}^{n}$$
Nonaffine hypersurface $\mathcal{S}$, bởi giả sử rằng embdedding $\phi$: $\to F$ tồn tại, chẵn/ngay cả dù
$$\mathbb{R}^{n}\mathbb{R}^{n} \mathbb{R}$$
Ta không’t biết những gì nó là, nhưng có access đến $F$ qua hạt nhân (kernel) hàm $\kappa$: $\times \to$ cho trước bởi trong các tích $\kappa (x, y) = \langle \phi (x), \phi (y)\rangle$. Trong thực tế art của bằng cách sử dụng hạt nhân (kernel) phương pháp là đến chọn phải hạt nhân (kernel) (như knight nói rằng trong Indiana Jones, đến “chọn wisely.”). phương pháp của các hạt nhân là rất flexible. Nó cũng áp dụng đến lề mềm (soft margin) các phiên bản của SVM, nhưng cũng đến hồi quy các bài tập, đến phân tích thành phần chính (PCA) (PCA), và đến khác các bài tập phát sinh trong máy học (learning). Ta được thảo luận phương pháp của các hạt nhân trong Chương $53$. Khác toàn diện các trình bày của phương pháp của các hạt nhân là tìm thấy trong Sch¨olkopf và Smola $[151]$ và Shawe–Taylor và Christianini $[165]$. Xem cũng Bishop $[23]$. Ta thứ nhất xét lề mềm (soft margin) SVM phát sinh từ Bài toán $(SVM_{h1})$.

## 54.1 Lề mềm (soft margin) Các máy vectơ hỗ trợ (SVMs); (SVM)

$$s1$$
Trong mục này ta derive đối ngẫu (dual) hàm $G$ liên kết với sau đây phiên bản của lề mềm (soft margin) SVM coming từ Bài toán $(SVM_{h1})$, ở đâu cực đại hóa của lề (margin) $\delta$ có đã được được thay thế bởi cực tiểu hóa của $-\delta$, và ở đâu ta được cộng “regularizing số hạng”
$$K \begin{pmatrix} p & \epsilon_{i}  + & q & \xi_{j} \\ =1 & j=1 \\ \epsilon and\xi haveas \end{pmatrix} \sum_{ii}  \sum_{j}  whose purpose is to make \epsilon  \in \mathbb{R}^{p} and \xi  \in \mathbb{R}^{q} sparse (that is, try to$$
Tạo nhiều các không điểm như khả dĩ/có thể), ở đâu $K > 0$ là cố định hằng số rằng có thể được

<!-- PAGE 1971 -->
Adjusted để xác định influence của điều này regularizing số hạng. Nếu bài toán gốc (primal problem) $(SVM_{s1})$ có nghiệm tối ưu (optimal solution) $(w, \delta , b, \epsilon , \xi$), ta attempt để sử dụng đối ngẫu (dual) hàm $G$ để thu được nó, nhưng ta sẽ xem rằng với điều này cụ thể formulation của bài toán, ràng buộc $w^{\top}w \le 1$ gây ra troubles chẵn/ngay cả dù nó là lồi. Lề mềm (soft margin) SVM $(SVM_{s1})$:
$$minimize-\delta  + K \begin{pmatrix} \epsilon_{i}  + & \xi_{j} \end{pmatrix} \sum_{i=1}^{p}  \sum_{j=1}^{q}$$
$$subject to$$
$$w^{\top}u_{i} -b \ge \delta  -\epsilon_{i} ,\epsilon_{i}  \ge 0i = 1, \dots  , p$$
$$-w^{\top}v_{j} + b \ge \delta  -\xi_{j} ,\xi_{j}  \ge 0j = 1, \dots  , q$$
$$w^{\top}w \le 1.$$
Nó là thông lệ đến viết $\ell = p + q$. Hình 54.2 minh họa đúng lề (margin) một nửa không gian liên kết với $w^{\top}x$ - $b$ - $\delta  = 0$ trong khi Hình 54.3 minh họa đúng lề (margin) một nửa không gian liên kết với $w^{\top}x$ - $b + \delta  = 0$. một cách lý tưởng (ideal), tất cả các điểm nên được chứa trong một của hai đúng shifted lề (margin) các miền được mô tả bởi afin các ràng buộc $w^{\top}u_{i}$ - $b \ge \delta$ - $\epsilon_{i}$, hoặc $-w^{\top}v_{j} + b \ge \delta$ - $\xi_{j}$.
$$w  xT$$
$$- b$$
$$- \delta$$
$$= 0$$
$$Incorrect side of Blue Margin$$
$$w   x - b - \delta  < 0T$$
$$w  xTT$$
$$- bw   x - b - \delta  > 0$$
$$- \delta$$
$$= 0Correct side of Blue Margin$$
$$w T x$$
$$- b$$
$$= 0$$
$$wseparting hyperplane$$
$$xT - b$$
$$+ \delta$$
$$= 0$$
$$Figure 54.2: The blue margin half space associated with w^{\top}x -b -\delta  = 0.$$
Cho bài toán này, bài toán gốc (primal problem) có thể có nghiệm tối ưu (optimal solution) $(w, \delta , b, \epsilon , \xi$) với $\|w\| = 1$ và $\delta  > 0$, nhưng nếu các tập hợp của các điểm là không một cách tuyến tính khả ly thì nghiệm tối ưu (optimal solution) của đối ngẫu (dual) có thể không cho $w$.

<!-- PAGE 1972 -->
$$w T x$$
$$- b$$
$$- \delta  =$$
$$0$$
$$w  x - b$$
$$0 = T$$
$$w   x -b + \delta  < 0T$$
$$Correct side of Red Margin$$
$$Incorrect side of Red Margin$$
$$w Tw   x -b + \delta  > 0T$$
$$x -b + \delta$$
$$= 0$$
$$Figure 54.3: The red margin half space associated with w^{\top}x -b + \delta  = 0.$$
Hàm mục tiêu (objective function) của bài toán của chúng ta là afin và chỉ nonaffine ràng buộc $w^{\top}w \le 1$ là lồi. Điều này ràng buộc là qualified bởi vì với mọi $w \neq  0$ sao cho $w^{\top}w < 1$ và với mọi $\delta  > 0$ và bất kỳ $b$ ta có thể chọn $\epsilon$ và $\xi$ lớn đủ sao cho các ràng buộc được thỏa mãn. Hệ quả là, theo Định lý 50.17(2) nếu bài toán gốc (primal problem) $(SVM_{s1})$ có nghiệm tối ưu (optimal solution), thì bài toán đối ngẫu (dual problem) có nghiệm cũng, và khoảng cách đối ngẫu (duality gap) là không. Không may là điều này thực hiện không suy ra rằng nghiệm tối ưu (optimal solution) của đối ngẫu (dual) cho ta nghiệm tối ưu (optimal solution) của gốc (primal) bởi vì các giả thiết của Định lý 50.17(1) thất bại đến đúng. Nói chung, ở đó có thể không là duy nhất vectơ $(w, \epsilon , \xi , b, \delta$) sao cho
$$\inf L(w, \epsilon , \xi , b, \delta , \lambda , \mu , \alpha , \beta , \gamma ) = G(\lambda , \mu , \alpha , \beta , \gamma ).$$
$$w,\epsilon ,\xi ,b,\delta$$
Nếu các tập hợp ${u_{i}}$ và ${v_{j}}$ là không một cách tuyến tính khả ly, thì bài toán đối ngẫu (dual problem) có thể có nghiệm cho mà $\gamma  = 0$,
$$\sum_{i=1}^{p}  \lambda_{i}  = \sum_{j=1}^{q}  \mu_{j}  = \frac{1}{2} ,$$
Và
$$\sum_{i=1}^{p}  \lambda_{i} u_{i} = \sum_{j=1}^{q}  \mu_{j} v_{j},$$
Sao cho đối ngẫu (dual) hàm $G(\lambda , \mu , \alpha , \beta , \gamma$), mà là riêng hàm, được định nghĩa và có giá trị $G(\lambda , \mu , \alpha , \beta , 0) = 0$. Như vậy cặp $(\lambda , \mu$) tương ứng với các hệ số của hai lồi

<!-- PAGE 1973 -->
Các tổ hợp
$$\sum_{i=1}^{p}  2\lambda_{i} u_{i} = \sum_{j=1}^{q}  2\mu_{j} v_{j}$$
Mà tương ứng với cùng điểm trong (khác rỗng) giao của lồi các bao $conv(u_{1}, \dots  , u_{p})$ và $conv(v_{1}, \dots  , v_{q})$. Hóa ra là chỉ connection giữa $w$ và đối ngẫu (dual) hàm là phương trình
$$2\gamma w = \sum_{i=1}^{p}  \lambda_{i} u_{i} - \sum_{j=1}^{q}  \mu_{j} v_{j},$$
Và khi $\gamma  = 0$ điều này là phương trình là $0 = 0$, do đó bài toán đối ngẫu (dual problem) là useless để xác định $w$. Điều này điểm dường như đến có đã được missed trong literature (ví dụ, trong Shawe–Taylor và Christianini $[165]$, Mục 7.2). Những gì bài toán đối ngẫu (dual problem) thực hiện chỉ ra là rằng $\delta  \ge 0$. Tuy nhiên, nếu $\gamma  \neq  0$, thì $w$ được xác định bởi bất kỳ nghiệm $(\lambda , \mu$) của đối ngẫu (dual). Nó vẫn vẫn còn để tính $\delta$ và $b$, mà có thể được được thực hiện dưới nhẹ giả thiết rằng ta gọi Tiêu chuẩn Lề (margin) Giả thiết. Cho $\lambda  \in \mathbb{R}_{+}^{p}$ là Các nhân tử Lagrange (Lagrange multipliers) liên kết với các bất đẳng thức $w^{\top}u_{i}-b \ge \delta -\epsilon_{i}$, cho $\mu  \in \mathbb{R}_{+}^{q}$ là Các nhân tử Lagrange (Lagrange multipliers) là liên kết với các bất đẳng thức $-w^{\top}v_{j}+b \ge \delta -\xi_{j}$, cho $\alpha  \in \mathbb{R}_{+}^{p}$ là Các nhân tử Lagrange (Lagrange multipliers) liên kết với các bất đẳng thức $\epsilon_{i}  \ge 0, \beta  \in \mathbb{R}_{+}^{q}$ là
$$\mathbb{R}^{+}$$
Các nhân tử Lagrange (Lagrange multipliers) liên kết với các bất đẳng thức $\xi_{j}  \ge 0$, và cho $\gamma  \in$ là Nhân tử Lagrange (Lagrange multiplier) liên kết với bất đẳng thức $w^{\top}w \le 1$. tuyến tính các ràng buộc được cho bởi 2(p $+ q) \times  (n + p + q + 2)$ ma trận cho trước trong khối tạo thành bởi
$$C = \begin{pmatrix} - & 1_{p} \\ X^{\top} & I_{p+q} & -1_{q} & 1_{p+q} \\ 0_{p+q,n} & I_{p+q} & 0_{p+q} & 0_{p+q} \end{pmatrix} ,$$
$$-$$
Ở đâu $X$ là ma trận cỡ $n \times  (p + q)$
$$X = \begin{pmatrix} -u_{1} & \cdots & -u_{p} & v_{1} & \cdots & v_{q} \end{pmatrix} ,$$
Và tuyến tính các ràng buộc được biểu diễn bởi
$$\begin{pmatrix} - & 1_{p} \\ X^{\top} & I_{p+q} & -1_{q} & 1_{p+q} \\ 0_{p+q,n} & I_{p+q} & 0_{p+q} & 0_{p+q} \end{pmatrix} \begin{pmatrix} w \\ \epsilon \\ \xi \\ b \\ \delta \end{pmatrix} \le \begin{pmatrix} 0_{p+q} \\ 0_{p+q} \end{pmatrix} .$$
$$-$$

<!-- PAGE 1974 -->
Nhiều hơn/thêm một cách tường minh, $C$ là sau đây ma trận:
$$C = \begin{pmatrix} -u_{1}^{\top} & -1 & \cdots & 0 & 0 & \cdots & 0 & 1 & 1 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ -u_{p}^{\top} & 0 & \cdots & -1 & 0 & \cdots & 0 & 1 & 1 \\ v_{1}^{\top} & 0 & \cdots & 0 & -1 & \cdots & 0 & -1 & 1 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ v_{q}^{\top} & 0 & \cdots & 0 & 0 & \cdots & -1 & -1 & 1 \\ 0 & -1 & \cdots & 0 & 0 & \cdots & 0 & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ 0 & 0 & \cdots & -1 & 0 & \cdots & 0 & 0 & 0 \\ 0 & 0 & \cdots & 0 & -1 & \cdots & 0 & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ 0 & 0 & 0 & 0 & 1 & 0 & 0 \end{pmatrix} .$$
$$\cdots \cdots -$$
Hàm mục tiêu (objective function) được cho bởi
$$J(w, \epsilon , \xi , b, \delta ) = -\delta  + K \begin{pmatrix} \epsilon^{\top} & \xi^{\top} \\ \mathbb{R}_{+}^{p}, \end{pmatrix} 1_{p+q}.$$
$$\mathbb{R}_{+}^{q}\mathbb{R}^{+}$$
Hàm Lagrange (Lagrangian) L(w, $\epsilon , \xi , b, \delta , \lambda , \mu , \alpha , \beta , \gamma$) với $\lambda , \alpha  \in  \mu , \beta  \in$, và $\gamma  \in$ được cho bởi
$$L(w, \epsilon , \xi , b, \delta , \lambda , \mu , \alpha , \beta , \gamma ) = -\delta  + K \begin{pmatrix} \epsilon^{\top} & \xi^{\top} \end{pmatrix} 1_{p+q}$$
$$+ \begin{pmatrix} w^{\top} &  \epsilon^{\top} & \xi^{\top} \end{pmatrix} \begin{pmatrix} b & \delta \end{pmatrix} C^{\top} \begin{pmatrix} \lambda \\ \mu \\ \alpha \\ \beta \end{pmatrix} + \gamma (w^{\top}w -1).$$
Vì
$$\begin{pmatrix} w^{\top} &  \epsilon^{\top} & \xi^{\top} \end{pmatrix} \begin{pmatrix} b & \delta \end{pmatrix} C^{\top} \begin{pmatrix} \lambda \\ \mu \\ \alpha \\ \beta \end{pmatrix} = w^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} -\epsilon^{\top} (\lambda  + \alpha ) -\xi^{\top} (\mu  + \beta ) + b(1_{p}^{\top} \lambda  -1_{q}^{\top} \mu )$$
$$+ \delta (1_{p}^{\top} \lambda  + 1_{q}^{\top} \mu ),$$
Hàm Lagrange (Lagrangian) có thể được viết dưới dạng
$$L(w, \epsilon , \xi , b, \delta , \lambda , \mu , \alpha , \beta , \gamma ) = -\delta  + K(\epsilon^{\top} 1_{p} + \xi^{\top} 1_{q}) + w^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + \gamma (w^{\top}w -1)$$
$$-\epsilon^{\top} (\lambda  + \alpha ) -\xi^{\top} (\mu  + \beta ) + b(1_{p}^{\top} \lambda  -1_{q}^{\top} \mu ) + \delta (1_{p}^{\top} \lambda  + 1_{q}^{\top} \mu )$$
$$= (1_{p}^{\top} \lambda  + 1_{q}^{\top} \mu  -1)\delta  + w^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + \gamma (w^{\top}w -1)$$
$$+ \epsilon^{\top} (K1_{p} -(\lambda  + \alpha )) + \xi^{\top} (K1_{q} -(\mu  + \beta )) + b(1_{p}^{\top} \lambda  -1_{q}^{\top} \mu ).$$

<!-- PAGE 1975 -->
Để tìm đối ngẫu (dual) hàm $G(\lambda , \mu , \alpha , \beta , \gamma$) ta cực tiểu hóa L(w, $\epsilon , \xi , b, \delta , \lambda , \mu , \alpha , \beta , \gamma$) với
$$\mathbb{R}^{n} \mathbb{R}^{p} \mathbb{R}^{q}$$
Đối với đến $w, \epsilon , \xi , b$, và $\delta$. Vì Hàm Lagrange (Lagrangian) là lồi và $(w, \epsilon , \xi , b, \delta$) $\in \times \times \times \mathbb{R} \times \mathbb{R}$, lồi tập mở (open set), theo Định lý 40.13, Hàm Lagrange (Lagrangian) có cực tiểu trong $(w, \epsilon , \xi , b, \delta$) khi và chỉ khi $\nabla L_{w,\epsilon ,\xi ,b,\delta} = 0$, do đó ta tính gradien đối với $w, \epsilon , \xi , b, \delta$, và ta thu được
$$\begin{pmatrix}\end{pmatrix}$$
$$\nabla L_{w,\epsilon ,\xi ,b,\delta} = \begin{pmatrix} \lambda  \\ X & \mu & + 2\gamma w \\ K1_{p} -(\lambda  + \alpha ) \\ K1_{q} -(\mu  + \beta ) \\ 1_{p}^{\top}\lambda  -1_{q}^{\top}\mu \\ 1_{p}^{\top}\lambda  + 1_{q}^{\top}\mu & 1 \end{pmatrix} .$$
$$-$$
Bằng cách đặt $\nabla L_{w,\epsilon ,\xi ,b,\delta} = 0$ ta thu được các phương trình
$$2\gamma w = -X \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$\lambda  + \alpha  = K1_{p}(*_{w})$$
$$\mu  + \beta  = K1_{q}$$
$$1_{p}^{\top} \lambda  = 1_{q}^{\top} \mu$$
$$1_{p}^{\top} \lambda  + 1_{q}^{\top} \mu  = 1.$$
Thứ hai và thứ ba các phương trình là tương đương đến các bất đẳng thức
$$0 \le \lambda_{i} , \mu_{j}  \le K,i = 1, \dots  , p, j = 1, \dots  , q,$$
Thường được gọi là hình hộp các ràng buộc, và thứ tư và thứ năm các phương trình cho
$$1_{p}^{\top} \lambda  = 1_{q}^{\top} \mu  = \frac{1}{2} .$$
Thứ nhất cho chúng ta xét suy biến trường hợp $\gamma  = 0$. Trong trường hợp này, $(*_{w})$ suy ra rằng
$$X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = 0,$$
Và số hạng $\gamma (w^{\top}w$ - $1)$ là missing từ Hàm Lagrange (Lagrangian), mà xét theo khác bốn các phương trình ở trên rút gọn đến
$$L(w, \epsilon , \xi , b, \delta , \lambda , \mu , \alpha , \beta , 0) = w^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = 0.$$
Trong tóm tắt, ta được chứng minh rằng nếu $\gamma  = 0$, thì
$$pq$$
$$ \sum_{i}  =1 \lambda_{i}  = \sum  j=1 \mu_{j}  =_{2}^{1}$$
$$0if0 \le \lambda_{i}  \le K, i = 1, \dots  , p$$
$$$$
$$$$
$$$$
$$$$
$$G(\lambda , \mu , \alpha , \beta , 0) =0 \le \mu_{j}  \le K, j = 1, \dots  , q$$
$$$$
$$-\infty otherwise$$
$$$$
$$$$
$$$$
$$pq$$
$$and \sum_{i}  =1 \lambda_{i} u_{i} - \sum_{j}  =1 \mu_{j} v_{j} = 0.$$

<!-- PAGE 1976 -->
Geometrically, $(\lambda , \mu$) tương ứng với các hệ số của hai lồi các tổ hợp
$$\sum_{i=1}^{p}  2\lambda_{i} u_{i} = \sum_{j=1}^{q}  2\mu_{j} v_{j}$$
Mà tương ứng với cùng điểm trong giao của lồi các bao $conv(u_{1}, \dots  , u_{p})$ và $conv(v_{1}, \dots  , v_{q})$ khi và chỉ khi các tập hợp ${u_{i}}$ và ${v_{j}}$ là không một cách tuyến tính khả ly. Nếu các tập hợp ${u_{i}}$ và ${v_{j}}$ là một cách tuyến tính khả ly, thì lồi các bao $conv(u_{1}, \dots  , u_{p})$ và $conv(v_{1}, \dots  , v_{q})$ là rời nhau, mà suy ra rằng $\gamma  > 0$. Bây giờ ta giả sử rằng $\gamma  > 0$. Plugging quay lại $w$ từ phương trình $(*_{w})$ vào Hàm Lagrange (Lagrangian), sau simplifications ta thu được
$$G(\lambda , \mu , \alpha , \beta , \gamma ) = - \frac{1}{2\gamma} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + \frac{\gamma}{4\gamma^{2}} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} -\gamma$$
$$= - \frac{1}{4\gamma} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} -\gamma ,$$
Do đó nếu $\gamma  > 0$ đối ngẫu (dual) hàm là độc lập của $\alpha , \beta$ và được cho bởi
$$\lambda ! \sum_{i}  p=1 \lambda_{i}  = \sum  qj=1 \mu_{j}  =_{2}^{1}$$
$$$$
$$-_{4\gamma}^{1}X^{\top}X-\gamma if0 \le \lambda_{i}  \le K, i = 1, \dots  , p$$
$$G(\lambda , \mu , \alpha , \beta , \gamma ) = \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \mu $$
$$0 \le \mu_{j}  \le K, j = 1, \dots  , q$$
$$$$
$$$$
$$-\infty otherwise.$$
$$$$
Vì $X^{\top}X$ là đối xứng nửa xác định dương (positive semidefinite) và $\gamma  \ge 0$, hiển nhiên
$$G(\lambda , \mu , \alpha , \beta , \gamma ) \le 0$$
Với mọi $\gamma  > 0$. đối ngẫu (dual) bài toán quy hoạch được cho bởi
$$maximize- \frac{1}{4\gamma} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} -\gamma if \gamma  > 0$$
$$0if\gamma  = 0$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = 1$$
$$0 \le \lambda_{i}  \le K,i = 1, \dots  , p$$
$$0 \le \mu_{j}  \le K,j = 1, \dots  , q.$$

<!-- PAGE 1977 -->
$$Also, if \gamma  = 0, then X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = 0.$$
Cực đại hóa đối với $\gamma  > 0$ bởi $setting_{\partial \gamma}^{\partial}G(\lambda , \mu , \alpha , \beta , \gamma$) $= 0$ cho ta
$$\gamma^{2} = \frac{1}{4} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} ,$$
Do đó ta thu được
$$1/2$$
$$G(\lambda , \mu ) = - \begin{pmatrix}   & \lambda \\ \lambda^{\top} & \mu^{\top} X^{\top}X & \mu \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix}\end{pmatrix} .$$
$$Finally, since G(\lambda , \mu ) = 0 and X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = 0 if \gamma  = 0, the dual program is equivalent to$$
Sau đây cực tiểu hóa bài toán quy hoạch: Đối ngẫu (dual) của Lề mềm (soft margin) SVM $(SVM_{s1})$:
$$minimize \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = 1$$
$$0 \le \lambda_{i}  \le K,i = 1, \dots  , p$$
$$0 \le \mu_{j}  \le K,j = 1, \dots  , q.$$
Nhận thấy rằng các ràng buộc suy ra rằng $K$ phải được chọn sao cho
$$ $$
$$K \ge \max \frac{1}{2p} , \frac{1}{2q} .$$
Nếu $(w, \delta , b, \epsilon , \xi$) là nghiệm tối ưu (optimal solution) của Bài toán $(SVM_{s1})$, thì độ bù lỏng (complementary slackness) các điều kiện cho phân loại của các điểm $u_{i}$ và $v_{j}$ theo các giá trị của $\lambda$ và $\mu$. Thật vậy, ta có $\epsilon_{i} \alpha_{i}  = 0$ cho $i = 1, \dots  , p$ và $\xi_{j} \beta_{j}  = 0$ cho $j = 1, \dots  , q$. Cũng, nếu $\lambda_{i}  > 0$, thì tương ứng ràng buộc là hoạt động, và tương tự nếu $\mu_{j}  > 0$. Vì $\lambda_{i}  +\alpha_{i}  = K$, suy ra rằng $\epsilon_{i} \alpha_{i}  = 0$ khi và chỉ khi $\epsilon_{i} (K$ - $\lambda_{i}$) $= 0$, và vì $\mu_{j}  + \beta_{j}  = K$, ta có $\xi_{j} \beta_{j}  = 0$ khi và chỉ khi $\xi_{j} (K$ - $\mu_{j}$) $= 0$. Do đó nếu $\epsilon_{i}  > 0$, thì $\lambda_{i}  = K$, và nếu $\xi_{j}  > 0$, thì $\mu_{j}  = K$. Hệ quả là, nếu $\lambda_{i}  < K$, thì $\epsilon_{i}  = 0$ và $u_{i}$ là một cách chính xác được phân loại, và tương tự nếu $\mu_{j}  < K$, thì $\xi_{j}  = 0$ và $v_{j}$ là một cách chính xác được phân loại. Ta có kết quả sau phân loại:

<!-- PAGE 1978 -->
$(1)$ Nếu $0 < \lambda_{i}  < K$, thì $\epsilon_{i}  = 0$ và thứ $i$ bất đẳng thức là hoạt động, do đó
$$w^{\top}u_{i} -b -\delta  = 0.$$
Điều này có nghĩa là $u_{i}$ là trên xanh lam lề (margin) (siêu phẳng (hyperplane) $H_{w,b+\delta}$ của phương trình $w^{\top}x = b + \delta$) và được phân loại một cách chính xác. Tương tự, nếu $0 < \mu_{j}  < K$, thì $\xi_{j}  = 0$ và
$$w^{\top}v_{j} -b + \delta  = 0,$$
Do đó $v_{j}$ là trên đỏ lề (margin) (siêu phẳng (hyperplane) $H_{w,b-\delta}$ của phương trình $w^{\top}x = b$ - $\delta$) và được phân loại một cách chính xác. Xem Hình 54.4.
$$0 <      < K\lambda i$$
$$w   x  - b - T\delta  = 0\mu$$
$$0 <      < Kj$$
$$uw   x -b - T\delta  = 0$$
$$i$$
$$b$$
$$=$$
$$T  xb$$
$$wv=$$
$$x$$
$$jwT$$
$$w   x -b + T\delta  = 0$$
$$Case (1)w   x -b +\delta T = 0$$

![Figure 54.4](../../assets/ch54/fig_54_4.png)

**Hình 54.4:** Khi $0 < \lambda_{i}  < K, u_{i}$ được chứa trong phạm vi xanh lam lề (margin) siêu phẳng (hyperplane). Khi $0 < \mu_{j}  < K, v_{j}$ được chứa trong phạm vi đỏ lề (margin) siêu phẳng (hyperplane).
$(2)$ Nếu $\lambda_{i}  = K$, thì thứ $i$ bất đẳng thức là hoạt động, do đó
$$w^{\top}u_{i} -b -\delta  = -\epsilon_{i} .$$
Nếu $\epsilon_{i}  = 0$, thì điểm $u_{i}$ là trên xanh lam lề (margin). Nếu $\epsilon_{i}  > 0$, thì $u_{i}$ là trong phạm vi mở một nửa không gian bị chặn bởi xanh lam lề (margin) siêu phẳng (hyperplane) $H_{w,b+\delta}$ và chứa tách siêu phẳng (hyperplane) $H_{w,b}$; nếu $\epsilon_{i}  \le \delta$, thì $u_{i}$ được phân loại một cách chính xác, và nếu $\epsilon_{i}  > \delta$, thì $u_{i}$ là misclassified $(u_{i}$ lies trên sai vế/cạnh của tách siêu phẳng (hyperplane), đỏ vế/cạnh). Xem Hình 54.5. Tương tự, nếu $\mu_{j}  = K$, thì
$$w^{\top}v_{j} -b + \delta  = \xi_{j} .$$
Nếu $\xi_{j}  = 0$, thì điểm $v_{j}$ là trên đỏ lề (margin). Nếu $\xi_{j}  > 0$, thì $v_{j}$ là trong phạm vi mở một nửa không gian bị chặn bởi đỏ lề (margin) siêu phẳng (hyperplane) $H_{w,b-\delta}$ và chứa tách siêu phẳng (hyperplane) $H_{w,b}$; nếu $\xi_{j}  \le \delta$, thì $v_{j}$ được phân loại một cách chính xác, và nếu $\xi_{j}  > \delta$, thì $v_{j}$ là misclassified $(v_{j}$ lies trên sai vế/cạnh của tách siêu phẳng (hyperplane), xanh lam vế/cạnh). Xem Hình 54.5.

<!-- PAGE 1979 -->
$$0 < \lambda  < Ki$$
$$uє = 0$$
$$ii$$
$$w  x  - b -\delta  = 0T$$
$$(1)Correctly classified on margin$$
$$w  x - b  = 0T$$
$$vj0 < \mu  < Kj$$
$$w  x - b + \delta  = 0T\xi   = 0j$$
$$\lambda  i = KT$$
$$w  x  - b -\delta  = 0Tw  x  - b -\delta  = 0$$
$$0 < Є  < \delta i\lambda  i = K$$
$$ui\mu   = Kvv$$
$$jju iЄ  = \delta i$$
$$\xi  = \delta jw  x - b  = 0T$$
$$\mu   = Kw  x - b  = 0T$$
$$jv$$
$$0 <  \xi  < \delta jj$$
$$w  x - b + \delta  = 0Tw  x - b + \delta  = 0T$$
$$(2)Correctly classified in slab$$
$$w  x  - b -\delta  = 0T$$
$$\mu   = Kvv$$
$$j\xi  > \delta j(3)Misclassified$$
$$j$$
$$w  x - b  = 0T$$
$$\lambda  i = K$$
$$ui$$
$$Є > \delta i$$
$$w  x - b + \delta  = 0T$$

![Figure 54.5](../../assets/ch54/fig_54_5.png)

**Hình 54.5:** Hình $(1)$ minh họa trường hợp của $u_{i}$ được chứa trong lề (margin) và xảy ra khi $\epsilon_{i}  = 0$. Hình $(1)$ cũng minh họa trường hợp của $v_{j}$ được chứa trong lề (margin) khi $\xi_{j}  = 0$. trái illustration của Hình $(2)$ là khi $u_{i}$ là bên trong lề (margin) vẫn chưa vẫn trên đúng vế/cạnh của tách siêu phẳng (hyperplane) $w^{\top}x$ - $b = 0$. Tương tự, $v_{j}$ là bên trong lề (margin) trên đúng vế/cạnh của tách siêu phẳng (hyperplane). phải illustration depicts $u_{i}$ và $v_{j}$ trên tách siêu phẳng (hyperplane). Hình $(3)$ illustrations misclassification của $u_{i}$ và $v_{j}$.
$(3)$ Nếu $\lambda_{i}  = 0$, thì $\epsilon_{i}  = 0$ và thứ $i$ bất đẳng thức có thể hoặc có thể không là hoạt động, do đó
$$w^{\top}u_{i} -b -\delta  \ge 0.$$
Do đó $u_{i}$ là trong đóng một nửa không gian trên xanh lam vế/cạnh bị chặn bởi xanh lam lề (margin) siêu phẳng (hyperplane) $H_{w,b+\delta}$ (của course, được phân loại một cách chính xác). Tương tự, nếu $\mu_{j}  = 0$, thì
$$w^{\top}v_{j} -b + \delta  \le 0$$
Và $v_{j}$ là trong đóng một nửa không gian trên đỏ vế/cạnh bị chặn bởi đỏ lề (margin) siêu phẳng (hyperplane) $H_{w,b-\delta}$ (của course, được phân loại một cách chính xác). Xem Hình 54.6.

> **Định nghĩa 54.1.** các vectơ $u_{i}$ trên xanh lam lề (margin) $H_{w,b+\delta}$ và các vectơ $v_{j}$ trên đỏ lề (margin) $H_{w,b-\delta}$ được gọi là hỗ trợ/giá (support) các vectơ. Hỗ trợ/giá (support) các vectơ tương ứng với các vectơ $u_{i}$ cho mà $w^{\top}u_{i}$ - $b$ - $\delta  = 0$ (mà suy ra $\epsilon_{i}  = 0)$, và các vectơ $v_{j}$ cho mà $w^{\top}v_{j}$ - $b + \delta  = 0$ (mà

<!-- PAGE 1980 -->
$$u \lambda  = 0$$
$$ii$$
$$є = 0$$
$$i$$
$$Correctly classified outside margin$$
$$w  x  - b -\delta  = 0T$$
$$w  x - b  = 0T$$
$$w  x - b + \delta  = 0T$$
$$\mu  = 0$$
$$vj$$
$$j\xi   = 0$$
$$j$$

![Figure 54.6](../../assets/ch54/fig_54_6.png)

**Hình 54.6:** Khi $\lambda_{i}  = 0, u_{i}$ là một cách chính xác được phân loại bên ngoài xanh lam lề (margin). Khi $\mu_{j}  = 0, v_{j}$ là một cách chính xác được phân loại bên ngoài đỏ lề (margin). suy ra $\xi_{j}  = 0)$. Hỗ trợ/giá (support) các vectơ $u_{i}$ sao cho $0 < \lambda_{i}  < K$ và hỗ trợ/giá (support) các vectơ $v_{j}$ sao cho $0 < \mu_{j}  < K$ là hỗ trợ/giá (support) các vectơ của loại/kiểu $1$. Hỗ trợ/giá (support) các vectơ của loại/kiểu $1$ đóng đặc biệt vai trò do đó ta ký hiệu các tập hợp của các chỉ số liên kết với chúng bởi
$$I_{\lambda} = {i \in {1, \dots  , p} | 0 < \lambda_{i}  < K}$$
$$I_{\mu} = {j \in {1, \dots  , q} | 0 < \mu_{j}  < K}.$$
Ta ký hiệu của chúng cardinalities bởi $numsvl_{1} = |I_{\lambda}|$ và $numsvm_{1} = |I_{\mu}|$. Hỗ trợ/giá (support) các vectơ $u_{i}$ sao cho $\lambda_{i}  = K$ và hỗ trợ/giá (support) các vectơ $v_{j}$ sao cho $\mu_{j}  = K$ là hỗ trợ/giá (support) các vectơ của loại/kiểu $2$. Những phần tử đó hỗ trợ/giá (support) các vectơ $u_{i}$ sao cho $\lambda_{i}  = 0$ và những phần tử đó hỗ trợ/giá (support) các vectơ $v_{j}$ sao cho $\mu_{j}  = 0$ được gọi là exceptional hỗ trợ/giá (support) các vectơ. các vectơ $u_{i}$ cho mà $\lambda_{i}  = K$ và các vectơ $v_{j}$ cho mà $\mu_{j}  = K$ được nói đến thất bại lề (margin). các tập hợp của các chỉ số liên kết với các vectơ thất bại lề (margin) được ký hiệu bởi
$$K_{\lambda} = {i \in {1, \dots  , p} | \lambda_{i}  = K}$$
$$K_{\mu} = {j \in {1, \dots  , q} | \mu_{j}  = K}.$$
Ta ký hiệu của chúng cardinalities bởi $p_{f} = |K_{\lambda}|$ và $q_{f} = |K_{\mu}|$. Các vectơ $u_{i}$ sao cho $\lambda_{i}  > 0$ và các vectơ $v_{j}$ sao cho $\mu_{j}  > 0$ được nói đến có lề (margin) nhiều nhất $\delta$. các tập hợp của các chỉ số liên kết với các vectơ này được ký hiệu bởi
$$I_{\lambda >0} = {i \in {1, \dots  , p} | \lambda_{i}  > 0}$$
$$I_{\mu >0} = {j \in {1, \dots  , q} | \mu_{j}  > 0}.$$
Ta ký hiệu của chúng cardinalities bởi $p_{m} = |I_{\lambda >0}|$ và $q_{m} = |I_{\mu >0}|$.

<!-- PAGE 1981 -->
Hiển nhiên, $I_{\lambda >0} = I_{\lambda} \cup K_{\lambda}$ và $I_{\mu >0} = I_{\mu} \cup K_{\mu}$, do đó $p_{f} \le p_{m}$ và $q_{f} \le q_{m}$. Một cách trực quan xanh lam điểm rằng không thỏa mãn lề (margin) là trên sai vế/cạnh của xanh lam lề (margin) và đỏ điểm rằng không thỏa mãn lề (margin) là trên sai vế/cạnh của đỏ lề (margin). các điểm trong $I_{\lambda >0}$ không trong $K_{\lambda}$ là trên xanh lam lề (margin) và các điểm trong $I_{\mu >0}$ không trong $K_{\mu}$ là trên đỏ lề (margin). Có $p$ - $p_{m}$ các điểm $u_{i}$ được phân loại một cách chính xác trên xanh lam vế/cạnh và bên ngoài $\delta$ -dải phẳng (slab) và có $q$ - $q_{m}$ các điểm $v_{j}$ được phân loại một cách chính xác trên đỏ vế/cạnh và bên ngoài $\delta$ -dải phẳng (slab). Nó là dễ để chỉ ra rằng ta có kết quả sau các cận trên $K$:
$$ $$
$$\max \frac{1}{2p_{m}} , \frac{1}{2q_{m}} \le K \le \min \frac{1}{2p_{f}} , \frac{1}{2q_{f}} .$$
Các bất đẳng thức này thu hẹp lựa chọn của $K$ khá heavily. Nó sẽ cũng là hữu ích đến understand cách mà các điểm được phân loại theo $\epsilon_{i}$ (hoặc $\xi_{j}$).
$(1)$ Nếu $\epsilon_{i}  > 0$, thì bởi độ bù lỏng (complementary slackness) $\lambda_{i}  = K$, do đó phương trình thứ $i$ là hoạt động và bởi $(2)$ ở trên,
$$w^{\top}u_{i} -b -\delta  = -\epsilon_{i} .$$
Vì $\epsilon_{i}  > 0$, điểm $u_{i}$ là trong phạm vi mở một nửa không gian bị chặn bởi xanh lam lề (margin) siêu phẳng (hyperplane) $H_{w,b+\delta}$ và chứa tách siêu phẳng (hyperplane) $H_{w,b}$; nếu $\epsilon_{i}  \le \delta$, thì $u_{i}$ được phân loại một cách chính xác, và nếu $\epsilon_{i}  > \delta$, thì $u_{i}$ là misclassified. Tương tự, nếu $\xi_{j}  > 0$, thì $v_{j}$ là trong phạm vi mở một nửa không gian bị chặn bởi đỏ lề (margin) siêu phẳng (hyperplane) $H_{w,b-\delta}$ và chứa tách siêu phẳng (hyperplane) $H_{w,b}$; nếu $\xi_{j}  \le \delta$, thì $v_{j}$ được phân loại một cách chính xác, và nếu $\xi_{j}  > \delta$, thì $v_{j}$ là misclassified.
$(2)$ Nếu $\epsilon_{i}  = 0$, thì điểm $u_{i}$ là một cách chính xác được phân loại. Nếu $\lambda_{i}  = 0$, thì bởi $(3)$ ở trên, $u_{i}$ là trong đóng một nửa không gian trên xanh lam vế/cạnh bị chặn bởi xanh lam lề (margin) siêu phẳng (hyperplane) $H_{w,b+\delta}$. Nếu $\lambda_{i}  > 0$, thì bởi $(1)$ và $(2)$ ở trên, điểm $u_{i}$ là trên xanh lam lề (margin). Tương tự, nếu $\xi_{j}  = 0$, thì điểm $v_{j}$ là một cách chính xác được phân loại. Nếu $\mu_{j}  = 0$, thì $v_{j}$ là trong đóng một nửa không gian trên đỏ vế/cạnh bị chặn bởi đỏ lề (margin) siêu phẳng (hyperplane) $H_{w,b-\delta}$, và nếu $\mu_{j}  > 0$, thì điểm $v_{j}$ là trên đỏ lề (margin). Nó được hiển thị trong Mục 54.2 cách mà đối ngẫu (dual) bài toán quy hoạch được giải bằng cách sử dụng ADMM từ Mục 52.6. Nếu bài toán gốc (primal problem) là giải được, điều này cho ta các nghiệm cho $\lambda$ và $\mu$.
$$If the optimal value is 0, then \gamma  = 0 and X \begin{pmatrix} \lambda \\ \mu \\ > \end{pmatrix} = 0, so in this case it is not possible$$
Để xác định $w$. Tuy nhiên, nếu giá trị tối ưu (optimal value) là $0$, thì một lần nghiệm cho $\lambda$ và $\mu$ là thu được, bởi $(*_{w})$, ta có
$$\gamma  = \frac{1}{2} 1/2$$
$$\begin{pmatrix}   & \lambda \\ \lambda^{\top} & \mu^{\top} X^{\top}X & \mu \\  \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix}\end{pmatrix}$$
$$w = \frac{1}{2\gamma} \begin{pmatrix} \lambda_{i} u_{i} - & \mu_{j} v_{j} \end{pmatrix} \sum_{i=1}^{p}  \sum_{j=1}^{q}  ,$$

<!-- PAGE 1982 -->
Do đó ta thu được
$$\sum_{i=1}^{p}  \lambda_{i} u_{i} - \sum_{j=1}^{q}  \mu_{j} v_{j}$$
$$w =,$$
$$\overline{1}\overline{/}\overline{2}$$
$$\begin{pmatrix} \overline{ } & \overline{}\lambda \\ \lambda^{\top} & \mu^{\top} X^{\top}X & \mu \\ \lambda_{i} u_{i} & q & \mu_{j} v_{j}a \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix}\end{pmatrix}$$
$$which is the result of making \sum_{i}  p=1  - \sum_{j}  =1   unit vector, since$$
$$X = \begin{pmatrix} -u_{1} & \cdots & -u_{p} & v_{1} & \cdots & v_{q} \end{pmatrix} .$$
Nó vẫn còn để tìm $b$ và $\delta$, mà là không cho trước bởi đối ngẫu (dual) bài toán quy hoạch và cho điều này ta sử dụng độ bù lỏng (complementary slackness) các điều kiện. các phương trình
$$\sum_{i=1}^{p}  \lambda_{i}  = \sum_{j=1}^{q}  \mu_{j}  = \frac{1}{2}$$
Suy ra rằng tồn tại một $i_{0}$ sao cho $\lambda_{i0}  > 0$ và một số $j_{0}$ sao cho $\mu_{j0}  > 0$, nhưng tiên nghiệm (a priori), không có gì ngăn cản tình huống ở đâu $\lambda_{i}  = K$ với mọi khác không $\lambda_{i}$ hoặc $\mu_{j}  = K$ với mọi khác không $\mu_{j}$. Nếu điều này xảy ra, ta có thể rerun tối ưu hóa phương pháp với lớn hơn giá trị của $K$. Nếu sau đây nhẹ giả thiết nghiệm đúng, thì $b$ và $\delta$ có thể được tìm thấy. Tiêu chuẩn Lề (margin) Giả thiết cho $(SVM_{s1})$. Tồn tại một chỉ số $i_{0}$ sao cho $0 < \lambda_{i0}  < K$ và tồn tại một chỉ số $j_{0}$ sao cho $0 < \mu_{j0}  < K$. Điều này có nghĩa là một số $u_{i0}$ là hỗ trợ/giá (support) vectơ của loại/kiểu $1$ trên xanh lam lề (margin), và một số $v_{j0}$ là hỗ trợ/giá (support) của loại/kiểu $1$ trên đỏ lề (margin). Nếu Tiêu chuẩn Lề (margin) Giả thiết cho $(SVM_{s1})$ nghiệm đúng, thì $\epsilon_{i0}  = 0$ và $\mu_{j0}  = 0$, và thì ta có hoạt động các phương trình
$$w^{\top}u_{i0} -b = \delta and-w^{\top}v_{j0} + b = \delta ,$$
Và ta thu được các giá trị của $b$ và $\delta$ như
$$b = \frac{1}{2} (w^{\top}u_{i0} + w^{\top}v_{j0})$$
$$\delta  = \frac{1}{2} (w^{\top}u_{i0} -w^{\top}v_{j0}).$$
Do số tính mất ổn định, khi viết máy tính bài toán quy hoạch nó được ưu tiên hơn để tính các danh sách của các chỉ số $I_{\lambda}$ và $I_{\mu}$ cho trước bởi
$$I_{\lambda} = {i \in {1, \dots  , p} | 0 < \lambda_{i}  < K}$$
$$I_{\mu} = {j \in {1, \dots  , q} | 0 < \mu_{j}  < K}.$$

<!-- PAGE 1983 -->
Thì nó là dễ để xem rằng ta có thể tính $b$ và $\delta$ bằng cách sử dụng sau đây lấy trung bình các công thức:
$$ \sum_{\in I\lambda}  \sum_{\in I\mu}  $$
$$b = w^{\top}/|I_{\lambda}| +/|I_{\mu}|/2$$
$$ \begin{pmatrix} u_{i} \\ i \end{pmatrix} \begin{pmatrix} v_{j} \\ j \end{pmatrix} $$
$$ \sum_{i\in I\lambda}  \sum_{j\in I\mu}  $$
$$\delta  = w^{\top}/|I_{\lambda}| -/|I_{\mu}|/2.$$
$$ \begin{pmatrix} u_{i} \end{pmatrix} \begin{pmatrix} v_{j} \end{pmatrix} $$
Như ta được nói trước đó, các giả thiết của Định lý 50.17(2) đúng, do đó nếu bài toán gốc (primal problem) $(SVM_{s1})$ có nghiệm tối ưu (optimal solution) với $w \neq  0$, thì bài toán đối ngẫu (dual problem) có nghiệm cũng, và khoảng cách đối ngẫu (duality gap) là không. Vì vậy, cho tối ưu các nghiệm ta có
$$L(w, \epsilon , \xi , b, \delta , \lambda , \mu , \alpha , \beta , \gamma ) = G(\lambda , \mu , \alpha , \beta , \gamma ),$$
Mà có nghĩa là
$$1/2$$
$$-\delta  + K \begin{pmatrix} \epsilon_{i}  + & \xi_{j} \end{pmatrix} \sum_{i=1}^{p}  \sum_{j=1}^{q}  = - \begin{pmatrix}   & \lambda \\ \lambda^{\top} & \mu^{\top} X^{\top}X & \mu \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix}\end{pmatrix} ,$$
Do đó ta thu được
$$\delta  = K \sum_{i=1}^{p}  \sum_{j=1}^{q}  +1/2.$$
$$\begin{pmatrix} \epsilon_{i}  + & \xi_{j} \end{pmatrix} \begin{pmatrix}   & \lambda \\ \lambda^{\top} & \mu^{\top} X^{\top}X & \mu \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix}\end{pmatrix}$$
Vì vậy, ta confirm rằng $\delta  \ge 0$. Nó là quan trọng đến lưu ý rằng hàm mục tiêu (objective function) của đối ngẫu (dual) bài toán quy hoạch
$$1/2$$
$$-G(\lambda , \mu ) = \begin{pmatrix}   & \lambda \\ \lambda^{\top} & \mu^{\top} X^{\top}X & \mu \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix}\end{pmatrix}$$
Chỉ liên quan đến trong các tích của $u_{i}$ và $v_{j}$ qua ma trận $X^{\top}X$, và tương tự, phương trình của tối ưu siêu phẳng (hyperplane) có thể được viết dưới dạng
$$1/2$$
$$\sum_{i=1}^{p}  \lambda_{i} u_{i}^{\top} x - \sum_{j=1}^{q}  \mu_{j} v_{j}^{\top} x - \begin{pmatrix}   & \lambda \\ \lambda^{\top} & \mu^{\top} X^{\top}X & \mu \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix}\end{pmatrix} b = 0,$$
Biểu thức rằng chỉ liên quan đến trong các tích của $x$ với $u_{i}$ và $v_{j}$ và trong các tích của $u_{i}$ và $v_{j}$. Như được giải thích tại bắt đầu của điều này chương, điều này là then chốt sự kiện rằng cho phép tổng quát hóa của máy vectơ hỗ trợ (SVM) bằng cách sử dụng phương pháp của các hạt nhân. Ta có thể định nghĩa sau đây “kernelized” phiên bản của Bài toán $(SVM_{s1})$:

<!-- PAGE 1984 -->
Lề mềm (soft margin) hạt nhân (kernel) SVM $(SVM_{s1})$:
$$minimize-\delta  + K \begin{pmatrix} \epsilon_{i}  + & \xi_{j} \end{pmatrix} \sum_{i=1}^{p}  \sum_{j=1}^{q}$$
$$subject to$$
$$\langle w, \phi (u_{i})\rangle -b \ge \delta  -\epsilon_{i} ,\epsilon_{i}  \ge 0i = 1, \dots  , p$$
$$-\langle w, \phi (v_{j})\rangle + b \ge \delta  -\xi_{j} ,\xi_{j}  \ge 0j = 1, \dots  , q$$
$$\langle w, w\rangle \le 1.$$
Tracing qua phép tính rằng đã dẫn đến chúng ta đến đối ngẫu (dual) bài toán quy hoạch với $u_{i}$ được thay thế bởi $\phi (u_{i})$ và $v_{j}$ được thay thế bởi $\phi (v_{j})$, ta tìm sau đây phiên bản của đối ngẫu (dual) bài toán quy hoạch: Đối ngẫu (dual) của Lề mềm (soft margin) hạt nhân (kernel) SVM $(SVM_{s1})$:
$$minimize \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} K \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = 1$$
$$0 \le \lambda_{i}  \le K,i = 1, \dots  , p$$
$$0 \le \mu_{j}  \le K,j = 1, \dots  , q,$$
Ở đâu $K$ là $\ell \times  \ell$ hạt nhân (kernel) ma trận đối xứng (symmetric matrix) (với $\ell = p + q)$ cho trước bởi
$$\kappa (u_{i}, u_{j})1 \le i \le p, 1 \le j \le q$$
$$$$
$$$$
$$-\kappa (u_{i}, v_{j-p})1 \le i \le p, p + 1 \le j \le p + q$$
$$$$
$$K_{ij} =$$
$$-\kappa (v_{i-p}, u_{j})p + 1 \le i \le p + q, 1 \le j \le p$$
$$$$
$$$$
$$\kappa (v_{i-p}, v_{j-q})p + 1 \le i \le p + q, p + 1 \le j \le p + q.$$
$$$$
Ta cũng tìm rằng
$$\sum_{i=1}^{p}  \lambda_{i} \phi (u_{i}) - \sum_{j=1}^{q}  \mu_{j} \phi (v_{j})$$
$$w = .$$
$$\overline{1}\overline{/}\overline{2}$$
$$\begin{pmatrix} \overline{ } & \overline{}\lambda \\ \lambda^{\top} & \mu^{\top} K & \mu \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix}\end{pmatrix}$$
