# Gốc-đối ngẫu (primal-dual) Thuật toán


<!-- PAGE 1664 -->

## 47.6 Gốc-đối ngẫu (primal-dual) Thuật toán

Cho (P2) là bài toán quy hoạch tuyến tính (linear program) trong tiêu chuẩn tạo thành
$$maximizecx$$
$$subject toAx = b and x \ge 0,$$
Ở đâu $A$ là một ma trận cỡ $m \times  n$ của hạng (rank) $m$, và $(D)$ là đối ngẫu (đối ngẫu (dual)) của nó cho trước bởi
$$minimizeyb$$
$$subject toyA \ge c,$$
Ở đâu $y \in (\mathbb{R}^{m})^{*}$.
$$First we may assume that b \ge 0 by changing every equation \sum_{j}  n=1 a_{ij}x_{j} = b_{i} with b_{i} < 0$$
$$to \sum_{j}  n=1 -a_{ij}x_{j} = -b_{i}. If we happen to have some feasible solution y of the dual program$$
$(D)$, ta biết từ Định lý 47.13 rằng nghiệm chấp nhận được (feasible solution) $x$ của (P2) là nghiệm tối ưu (optimal solution) khi và chỉ khi các phương trình trong $(*_{P})$ đúng. Nếu ta ký hiệu bởi $J$ tập con của ${1, \dots  , n}$ cho mà các đẳng thức
$$yA^{j}= c_{j}$$
Đúng, thì theo Định lý 47.13 nghiệm chấp nhận được (feasible solution) $x$ của (P2) là nghiệm tối ưu (optimal solution) khi và chỉ khi
$$x_{j} = 0for all j \in /J.$$
$$\mathbb{R}^{n}$$
Cho |J| $= p$ và $N = {1, \dots  , n}$ - $J$. ở trên suggests nhìn cho $x \in$ sao cho
$$\sum_{j\in J}  x_{j}A^{j} = b$$
$$x_{j} \ge 0for all j \in J$$
$$x_{j} = 0for all j \in /J,$$
Hoặc tương đương
$$A_{J}x_{J} = b,x_{J} \ge 0,(*_{1})$$
Và
$$x_{N} = 0_{n-p}.$$
Đến search cho như vậy $x$, ta chỉ cần đến nhìn cho chấp nhận được (feasible) $x_{J}$, và cho điều này ta có thể sử dụng Bị thu hẹp Gốc (primal) bài toán quy hoạch tuyến tính (linear program) (RP) được định nghĩa như sau:
$$maximize-(\xi_{1}  + \cdots  + \xi_{m} )$$
$$subject to \begin{pmatrix} A_{J} & I_{m} \end{pmatrix} \begin{pmatrix} x_{J} \\ \xi \end{pmatrix} = b and x, \xi  \ge 0.$$

<!-- PAGE 1665 -->
Vì bởi giả thiết $b \ge 0$ và hàm mục tiêu (objective function) là bị chặn ở trên bởi $0$, điều này bài toán quy hoạch tuyến tính (linear program) có nghiệm tối ưu (optimal solution) $(x_{J}^{*}, \xi^{*}$).
$$\mathbb{R}^{n}$$
Nếu $\xi^{*} = 0$, thì vectơ $u^{*} \in$ cho trước bởi $u_{J}^{*} = x_{J}^{*}$ và $u_{N}^{*} = 0_{n-p}$ là nghiệm tối ưu (optimal solution) của $(P)$. Ngược lại, $\xi^{*} > 0$ và ta có được thất bại để giải $(*_{1})$. Tuy nhiên ta có thể thử để sử dụng $\xi^{*}$ đến cải thiện $y$. Cho điều này xét Đối ngẫu (dual) (DRP) của $(RP)$:
$$minimizezb$$
$$subject tozA_{J} \ge 0$$
$$z \ge -1_{m}^{\top}.$$
Nhận thấy rằng Bài toán quy hoạch (DRP) có cùng hàm mục tiêu (objective function) như ban đầu Đối ngẫu (dual) Bài toán quy hoạch $(D)$. Ta biết theo Định lý 47.12 rằng nghiệm tối ưu (optimal solution) $(x_{J}^{*}, \xi^{*}$) của $(RP)$ cho ta nghiệm tối ưu (optimal solution) $z^{*}$ của $(DRP)$ sao cho
$$z^{*}b = -(\xi_{1}^{*}  + \cdots  + \xi_{m}^{*} ) < 0.$$
Thực ra, nếu $K^{*}$ là cơ sở (basis) liên kết với $(x_{J}^{*}, \xi^{*}$) và nếu ta viết
$$A =$$
$$b \begin{pmatrix} A_{J} & I_{m} \end{pmatrix}$$
Và $c = [0_{p}^{\top}$ - $1^{\top}]$, thì theo Định lý 47.12 ta có $b$
$$z^{*}=c_{K*}A_{K*}^{-1}= -1_{m}^{\top} -(\overline{c}_{K*})_{(p+1,...,p+m)},$$
$$bb$$
Ở đâu $(\overline{c}_{K*})_{(p+1,...,p+m)}$ ký hiệu vectơ hàng (row vector) của rút gọn chi phí trong cuối cùng bảng đơn hình (tableau) tương ứng với cuối cùng $m$ các cột. Nếu ta viết
$$y(\theta ) = y + \theta z^{*},$$
Thì mới giá trị của hàm mục tiêu (objective function) của $(D)$ là
$$y(\theta )b = yb + \theta z^{*}b,(*_{2})$$
Và vì $z^{*}b < 0$, ta có chance của improving hàm mục tiêu (objective function) của $(D)$, nghĩa là, giảm giá trị của nó cho $\theta  > 0$ nhỏ đủ nếu $y(\theta$) là chấp nhận được (feasible) cho $(D)$. Điều này sẽ là trường hợp khi và chỉ khi $y(\theta )A \ge c$ khi và chỉ khi
$$yA + \theta z^{*}A \ge c.(*_{3})$$
Bây giờ vì $y$ là nghiệm chấp nhận được (feasible solution) của $(D)$ ta có yA $\ge c$, do đó nếu $z^{*}A \ge 0$, thì $(*_{3})$ được thỏa mãn và $y(\theta$) là nghiệm của $(D)$ với mọi $\theta  > 0$, mà có nghĩa là $(D)$ là không bị chặn. Nhưng điều này suy ra rằng $(P)$ là không chấp nhận được (feasible).

<!-- PAGE 1666 -->
Cho chúng ta lấy closer nhìn tại các bất đẳng thức $z^{*}A \ge 0$. Cho $j \in J$, vì $z^{*}$ là nghiệm tối ưu (optimal solution) của $(DRP)$, ta biết rằng $z^{*}A_{J} \ge 0$, do đó nếu $z^{*}A^{j} \ge 0$ với mọi $j \in N$, thì (P2) là không chấp nhận được (feasible). Ngược lại, tồn tại một $j \in N = {1, \dots  , n}$ - $J$ sao cho
$$z^{*}A^{j}< 0,$$
Và khi đó vì bởi định nghĩa của $N$ ta có $yA^{j} > c_{j}$ với mọi $j \in N$, nếu ta chọn $\theta$ sao cho
$$-$$
$$0 < \theta  \le \frac{yA^{j}c_{j}}{-z^{*}A^{j}} j \in N, z^{*}A^{j}< 0,$$
Thì ta giảm hàm mục tiêu (objective function) $y(\theta )b =$ yb $+ \theta z^{*}b$ của $(D)$ (vì $z^{*}b < 0)$. Vì vậy ta chọn tốt nhất $\theta$, cụ thể là
$$-



$$
$$\theta^{+} = \min \frac{yA^{j}c_{j}}{-z^{*}A^{j}} j \in /J, z^{*}A^{j}< 0> 0.(*_{4})$$
Tiếp theo ta update $y$ đến $y^{+} = y(\theta^{+}$) $= y + \theta^{+} z^{*}$, ta create mới bị thu hẹp gốc (primal) với mới tập con
$$J^{+}= {j \in {1, \dots  , n} | y^{+}A^{j}= c_{j}},$$
Và repeat process. Ở đây là các bước của gốc-đối ngẫu (primal-dual) thuật toán. Bước $1$. Tìm một số nghiệm chấp nhận được (feasible solution) $y$ của Đối ngẫu (dual) Bài toán quy hoạch $(D)$. Ta sẽ chỉ ra sau này
$$that this is always possible.$$
Bước $2$. Tính
$$J^{+}= {j \in {1, \dots  , n} | yA^{j}= c_{j}}.$$
Bước $3$. Tập hợp $J = J^{+}$ và giải Bài toán (RP) bằng cách sử dụng thuật toán đơn hình (simplex algorithm), bắt đầu
$$from the optimal solution determined during the previous round, obtaining the$$
$$optimal solution (x_{J}^{*}, \xi^{*} ) with the basis K^{*}.$$
Bước $4$.
$$If \xi^{*} = 0, then stop with an optimal solution u^{*}for (P) such that u_{J}^{*} = x_{J}^{*} and the$$
$$other components of u^{*}are zero.$$
$$Else let$$
$$z^{*}= -1_{m}^{\top} -(\overline{c}_{K*})_{(p+1,...,p+m)},$$
$$be the optimal solution of (DRP) corresponding to (x_{J}^{*}, \xi^{*} ) and the basis K^{*}.$$
$$If z^{*}A^{j}\ge 0 for all j \in /J, then stop; the Program (P) has no feasible solution.$$

<!-- PAGE 1667 -->
$$Else compute$$
$$-



$$
$$\theta^{+} = \min- \frac{yA^{j}c_{j}}{z^{*}A^{j}} j \in /J, z^{*}A^{j}< 0,y^{+}= y + \theta^{+} z^{*},$$
$$and$$
$$J^{+}= {j \in {1, \dots  , n} | y^{+}A^{j}= c_{j}}.$$
$$Go back to Step 3.$$
Sau đây mệnh đề chỉ ra rằng tại mỗi vòng lặp ta có thể bắt đầu Bài toán quy hoạch (RP) với nghiệm tối ưu (optimal solution) thu được tại trước đó vòng lặp.

> **Mệnh đề 47.14.** Mọi $j \in J$ sao cho $A^{j}$ là trong cơ sở (basis) của nghiệm tối ưu (optimal solution) $\xi^{*}$ thuộc đến tiếp theo chỉ số tập hợp $J^{+}$.

*Chứng minh.* Như vậy chỉ số $j \in J$ tương ứng với biến $\xi_{j}$ sao cho $\xi_{j}  > 0$, do đó bởi độ bù lỏng (complementary slackness), ràng buộc $z^{*}A^{j} \ge 0$ của Đối ngẫu (dual) Bài toán quy hoạch (DRP) phải là đẳng thức, nghĩa là, $z^{*}A^{j} = 0$. Nhưng khi đó ta có
$$y^{+}A^{j}= yA^{j}+ \theta^{+} z^{*}A^{j}= c_{j},$$
Mà chỉ ra rằng $j \in J^{+}$. Nếu $(u^{*}, \xi^{*}$) với cơ sở (basis) $K^{*}$ là nghiệm tối ưu (optimal solution) của Bài toán quy hoạch (RP), Mệnh đề 47.14 cùng với cuối cùng tính chất của Định lý 47.12 cho phép chúng ta đến restart (RP) trong Bước $3$ với $(u^{*}, \xi^{*} )_{K*}$ như ban đầu nghiệm (với cơ sở (basis) $K^{*})$. Với mọi $j \in J$ - $J^{+}$, cột $j$ là deleted, và với mọi $j \in J^{+}$ - $J$, mới cột $A^{j}$ được tính bằng cách nhân $A_{K*}^{-1}$ và
$$b$$
$A^{j}$, nhưng $A_{K*}^{-1}$ là ma trận $\Gamma^{*}$ [1:m; $p +$ 1:p $+ m]$ bao gồm của cuối cùng $m$ các cột của $\Gamma^{*}$ trong
$$b$$
Cuối cùng bảng đơn hình (tableau), và mới rút gọn $\overline{c}_{j}$ được cho bởi $c_{j}$ - $z^{*}A^{j}$. Reusing nghiệm tối ưu (optimal solution) của trước đó (RP) có thể cải thiện efficiency một cách đáng kể. Một cái khác then chốt nhận xét là rằng với mọi chỉ số $j_{0} \in N$ sao cho $\theta^{+} = (yA^{j0}$ - $c_{j0})/(-z^{*}A^{j0})$, ta có
$$y^{+}A_{j0} = yA_{j0} + \theta^{+} z^{*}A^{j0}= c_{j0},$$
Và do đó $j_{0} \in J^{+}$. sự kiện này rằng được sử dụng để đảm bảo rằng gốc-đối ngẫu (primal-dual) thuật toán kết thúc trong hữu hạn số của các bước (bằng cách sử dụng phần tử trụ (pivot) quy tắc rằng ngăn cản cycling); xem Papadimitriou và Steiglitz $[139]$ (Định lý 5.4). Nó vẫn còn đến thảo luận cách mà đến chọn một số ban đầu nghiệm chấp nhận được (feasible solution) $y$ của Đối ngẫu (dual) Bài toán quy hoạch $(D)$. Nếu $c_{j} \le 0$ cho $j = 1, \dots  , n$, thì ta có thể chọn $y = 0$. Nếu ta là dealing với cực tiểu hóa bài toán, trọng số $c_{j}$ là thường không âm, do đó từ điểm của quan điểm của cực đại hóa ta sẽ có $-c_{j} \le 0$ với mọi $j$, và ta sẽ là able để sử dụng $y = 0$ như bắt đầu điểm. Đi quay lại đến của ta bài toán gốc (primal problem) trong cực đại hóa tạo thành và đối ngẫu (đối ngẫu (dual)) của nó trong cực tiểu hóa tạo thành, ta vẫn cần đến deal với tình huống ở đâu $c_{j} > 0$ với một số $j$, trong mà trường hợp ở đó

<!-- PAGE 1668 -->
Có thể không là bất kỳ hiển nhiên $y$ chấp nhận được (feasible) cho $(D)$. Preferably ta sẽ like để tìm như vậy $y$ rất cheaply. Có một mẹo/kỹ thuật đến deal với tình huống này. Ta chọn một số rất lớn dương số $M$ và cộng đến tập hợp của các phương trình Ax $= b$ mới phương trình
$$x_{1} + \cdots  + x_{n} + x_{n+1} = M,$$
Với mới biến $x_{n+1}$ có ràng buộc là không âm. Nếu Bài toán quy hoạch $(P)$ có nghiệm chấp nhận được (feasible solution), như vậy $M$ tồn tại. Thực ra nó có thể được hiển thị rằng với mọi cơ bản nghiệm chấp nhận được (feasible solution) $u = (u_{1}, \dots  , u_{n})$, mỗi $|u_{i}|$ là bị chặn bởi một số biểu thức tùy thuộc chỉ trên $A$ và $b$; xem Papadimitriou và Steiglitz $[139]$ (Bổ đề 2.1). chứng minh là không khó và relies trên sự kiện rằng nghịch đảo của ma trận có thể được được biểu diễn theo nhất định các định thức (adjugates). Không may là, điều này cận chứa $m$! như nhân tử, mà làm cho nó khá impractical. Có được cộng mới phương trình ở trên, ta thu được mới tập hợp của các phương trình
$$\begin{pmatrix} A \\ 0_{n} \\ 1_{n}^{\top} & 1 \end{pmatrix} \begin{pmatrix} x \\ x_{n+1} \end{pmatrix} = \begin{pmatrix} b \\ M \end{pmatrix} ,$$
Với $x \ge 0, x_{n+1} \ge 0$, và mới hàm mục tiêu (objective function) cho trước bởi
$$\begin{pmatrix} c & 0 \end{pmatrix} \begin{pmatrix} x \\ x_{n+1} \end{pmatrix} = cx.$$
Đối ngẫu (dual) của ở trên bài toán quy hoạch tuyến tính (linear program) là
$$minimizeyb + y_{m+1}M$$
$$subject toyA^{j}+ y_{m+1} \ge c_{j}j = 1, \dots  , n$$
$$y_{m+1} \ge 0.$$
Nếu $c_{j} > 0$ với một số $j$, nhận thấy rằng dạng tuyến tính (linear form) $y$ cho trước bởi
$$e$$
$$($$
$$0if 1 \le i \le m$$
$$y_{i} =$$
$$emax_{1\le j\le n}{c_{j}} > 0$$
Là nghiệm chấp nhận được (feasible solution) của mới đối ngẫu (dual) bài toán quy hoạch. Trong thực tế, ta có thể chọn $M$ là số close đến lớn nhất số nguyên representable trên máy tính đang được sử dụng. Đây là một ví dụ của gốc-đối ngẫu (primal-dual) thuật toán cho trước trong Math $588$ lớp các lưu ý của $T$. Molla $[132]$.

> **Ví dụ 47.3.** Xét sau đây bài toán quy hoạch tuyến tính (linear program) trong tiêu chuẩn tạo thành:
$$Maximize-x_{1} -3x_{2} -3x_{3} -x_{4}$$
$$subject to \begin{pmatrix} 3 & 4 & -3 & 1 \\ 3 & -2 & 6 & -1 \\ 6 & 4 & 0 & 1 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \\ x_{4} \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ 4 \end{pmatrix} and x_{1}, x_{2}, x_{3}, x_{4} \ge 0.$$

<!-- PAGE 1669 -->
Liên kết Đối ngẫu (dual) Bài toán quy hoạch $(D)$ là
$$Minimize2y_{1} + y_{2} + 4y_{3}$$
$$subject to \begin{pmatrix} y_{1} & y_{2} & y_{3} \end{pmatrix} \begin{pmatrix} 3 & 4 & -3 & 1 \\ 3 & -2 & 6 & -1 \\ 6 & 4 & 0 & 1 \end{pmatrix} \ge \begin{pmatrix} -1 & -3 & -3 & -1 \end{pmatrix} .$$
Ta initialize gốc-đối ngẫu (primal-dual) thuật toán với đối ngẫu (dual) chấp nhận được (feasible) điểm $y = (-1/3 0 0)$. Nhận thấy rằng chỉ thứ nhất bất đẳng thức của $(D)$ là thực sự đẳng thức, và do đó $J = {1}$. Ta tạo thành Bị thu hẹp Gốc (primal) Bài toán quy hoạch (RP1)
$$Maximize-(\xi_{1}  + \xi_{2}  + \xi_{3} )$$
$$subject to \begin{pmatrix} 3 & 1 & 0 & 0 \\ 3 & 0 & 1 & 0 \\ 6 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x_{1} \\ \xi_{1} \\ \xi_{2} \\ \xi_{3} \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ 4 \end{pmatrix} and x_{1}, \xi_{1} , \xi_{2} , \xi_{3}  \ge 0.$$
Ta bây giờ giải (RP1) thông qua thuật toán đơn hình (simplex algorithm). ban đầu bảng đơn hình (tableau) với $K = (2, 3, 4)$ và $J = {1}$ là
$$\frac{\overline{x}_{1}\overline{\xi}_{1}\overline{\xi}_{2}\overline{\xi}_{3}}{712000}$$
$$\xi_{1}  = 23100.$$
$$\xi_{2}  = 13010$$
$$\frac{\xi_{3} = 46001}{(x_{1}, \xi_{1} , \xi_{2} , \xi_{3} )=(0, 2, 1, 4),}$$
Cho (RP1), cˆ $= (0, -1, -1, -1)$, và khác không rút gọn chi phí được cho bởi
$$0 -(-1 -1 -1) \begin{pmatrix} 3 \\ 3 \\ 6 \end{pmatrix} = 12.$$
Vì ở đó là chỉ một khác không rút gọn chi phí, ta phải tập hợp $j^{+} = 1$. Vì $min{\xi_{1} /3, \xi_{2} /3, \xi_{3} /6} = 1/3$, ta xem rằng $k^{-} = 3$ và $K = (2, 1, 4)$. Do đó ta phần tử trụ (pivot) qua đỏ circled $3$ (cụ thể là ta chia hàng $2$ bởi $3$, và thì trừ $3\times$ (hàng $2)$ từ hàng $1, 6\times$ (hàng $2)$ từ hàng $3$, và thu được bảng đơn hình (tableau)
$$\frac{12\times (row2)fromrow0),to}{x_{1}\xi_{1} \xi_{2} \xi_{3}}$$
$$\frac{30040}{\xi_{1} = 101-10} -$$
$$.$$
$$x_{1} = 1/3101/30$$
$$\frac{\xi_{3} = 20021}{RP} -$$
Tại điều này giai đoạn thuật toán đơn hình (simplex algorithm) cho ($1)$ kết thúc vì có không có dương rút gọn chi phí. Vì trên trái góc của cuối cùng bảng đơn hình (tableau) là không không, ta tiến hành với Bước $4$ của gốc (primal) đối ngẫu (dual) thuật toán và tính
$$z^{*}= (-1 -1 -1) -(0 -4 0) = (-1 3 -1),$$

<!-- PAGE 1670 -->
$$yA^{2} -c_{2} = (-1/3 0 0) \begin{pmatrix} 4 \\ -2 \\ 4 \end{pmatrix} + 3 = \frac{5}{3} ,z^{*}A^{2} = -(-1 3 -1) \begin{pmatrix} 4 \\ -2 \\ 4 \end{pmatrix} = 14,$$
$$yA^{4} -c_{4} = (-1/3 0 0) \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} + 1 = \frac{2}{3} ,z^{*}A^{4} = -(-1 3 -1) \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} = 5,$$
Do đó
$$ $$
$$\theta^{+} = \min \frac{5}{42} , \frac{2}{15} = \frac{5}{42} ,$$
Và ta kết luận rằng mới nghiệm chấp nhận được (feasible solution) cho $(D)$ là
$$y^{+}= (-1/3 0 0) + \frac{5}{42} (-1 3 -1) = (-19/42 5/14 -5/42).$$
Khi ta thế $y^{+}$ vào $(D)$, ta discover rằng thứ nhất hai các ràng buộc là các đẳng thức, và rằng mới $J$ là $J = {1, 2}$. mới Rút gọn Gốc (primal) (RP2) là
$$Maximize-(\xi_{1}  + \xi_{2}  + \xi_{3} )$$
$$subject to \begin{pmatrix} 3 & 4 & 1 & 0 & 0 \\ 3 & -2 & 0 & 1 & 0 \\ 6 & 4 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ \xi_{1} \\ \xi_{2} \\ \xi_{3} \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ 4 \end{pmatrix} and x_{1}, x_{2}, \xi_{1} , \xi_{2} , \xi_{3}  \ge 0.$$
Một lần một lần nữa, ta giải (RP2) thông qua thuật toán đơn hình (simplex algorithm), ở đâu cˆ $= (0, 0, -1, -1, -1), (x_{1}, x_{2}, \xi_{1} , \xi_{2} , \xi_{3}$) $= (1/3, 0, 1, 0, 2)$ và $K = (3, 1, 5)$. ban đầu bảng đơn hình (tableau) là thu được từ cuối cùng bảng đơn hình (tableau) của trước đó (RP1) bằng cách cộng cột tương ứng biến $x_{2}$, cụ thể là
$$A_{K}^{-1}b A^{2} = \begin{pmatrix} 1 & -1 & 0 \\ 0 & 1/3 & 0 \\ 0 & 2 & 1 \end{pmatrix} \begin{pmatrix} 4 \\ -2 \\ 4 \end{pmatrix} = \begin{pmatrix} 6 \\ -2/3 \\ 8 \end{pmatrix} ,$$
$$-$$
Với
$$\overline{c}_{2} = c_{2} -z^{*}A^{2} = 0 - \begin{pmatrix} -1 & 3 & -1 \end{pmatrix} \begin{pmatrix} 4 \\ -2 \\ 4 \end{pmatrix} = 14,$$
Và ta thu được
$$\frac{\overline{x}_{1}\overline{x}_{2}\overline{\xi}_{1}\overline{\xi}_{2}\overline{\xi}_{3}}{30140-40}$$
$$\xi_{1}  = 1061-10.$$
$$x_{1} = 1/31-2/301/30$$
$$\xi_{3}  = 2080-21$$

<!-- PAGE 1671 -->
Lưu ý rằng $j^{+} = 2$ vì chỉ dương rút gọn chi phí xảy ra trong cột $2$. Cũng nhận thấy rằng vì $min{\xi_{1} /6, \xi_{3} /8} = \xi_{1} /6 = 1/6$, ta tập hợp $k^{-} = 3, K = (2, 1, 5)$ và phần tử trụ (pivot) dọc theo đỏ $6$ để thu được bảng đơn hình (tableau)
$$\frac{\overline{x}_{1}\overline{x}_{2}\overline{\xi}_{1}\overline{\xi}_{2}\overline{\xi}_{3}}{2/300-7/3-5/30}$$
$$x_{2} = 1/6011/6-1/60.$$
$$x_{1} = 4/9101/92/90$$
$$\frac{\xi_{3} = 2/3004/32/31}{Since the reduced costs are either zero or negative the simplex algorithm terminates, and} --$$
Ta tính
$$z^{*}= (-1 -1 -1) -(-7/3 -5/3 0) = (4/3 2/3 -1),$$
$$y^{+}A^{4} -c_{4} = (-19/42 5/14 -5/42) \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} + 1 = 1/14,$$
$$z^{*}A^{4} = -(4/3 2/3 -1) \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} = 1/3,$$
Do đó
$$\theta^{+} = \frac{3}{14} ,$$
$$y^{+}= (-19/42 5/14 -5/42) + \frac{5}{14} (4/3 2/3 -1) = (-1/6 1/2 -1/3).$$
Khi ta plug $y^{+}$ vào $(D)$, ta discover rằng thứ nhất, thứ hai, và thứ tư các ràng buộc là các đẳng thức, mà suy ra $J = {1, 2, 4}$. Do đó mới Bị thu hẹp Gốc (primal) (RP3) là Cực đại hóa - $(\xi_{1}  + \xi_{2}  + \xi_{3}$)
$$subject to \begin{pmatrix} 3 & 4 & 1 & 1 & 0 & 0 \\ 3 & -2 & -1 & 0 & 1 & 0 \\ 6 & 4 & 1 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ x_{4} \\ \xi_{1} \\ \xi_{2} \\ \xi_{3} \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ 4 \end{pmatrix} and x_{1}, x_{2}, x_{4}, \xi_{1} , \xi_{2} , \xi_{3}  \ge 0.$$
Ban đầu bảng đơn hình (tableau) cho (RP3), với ˆc $= (0, 0, 0, -1, -1, -1), (x_{1}, x_{2}, x_{4}, \xi_{1} , \xi_{2} , \xi_{3}$) $= (4/9, 1/6, 0, 0, 0, 2/3)$ và $K = (2, 1, 6)$, là thu được từ cuối cùng bảng đơn hình (tableau) của trước đó (RP2) bằng cách cộng cột tương ứng biến $x_{4}$, cụ thể là
$$A_{K}^{-1}b A^{4} = \begin{pmatrix} 1/6 & -1/6 & 0 \\ 1/9 & 2/9 & 0 \\ 4/3 & 2/3 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1/3 \\ -1/9 \\ 1/3 \end{pmatrix} ,$$
$$--$$

<!-- PAGE 1672 -->
Với
$$\overline{c}_{4} = c_{4} -z^{*}A^{4} = 0 - \begin{pmatrix} 4/3 & 2/3 & -1 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} = 1/3,$$
Và ta thu được
$$x_{1}x_{2}x_{4}\xi_{1} \xi_{2} \xi_{3}$$
$$2/3001/3-7/3-5/30$$
$$x_{2} = 1/6011/31/6-1/60.$$
$$x_{1} = 4/910-1/91/92/90$$
$$\xi_{3}  = 2/3001/3-4/3-2/31$$
Vì chỉ dương rút gọn chi phí xảy ra trong cột $3$, ta tập hợp $j^{+} = 3$. Hơn nữa vì $min{x_{2}/(1/3), \xi_{3} /(1/3)} = x_{2}/(1/3) = 1/2$, ta cho $k^{-} = 2, K = (3, 1, 6)$, và phần tử trụ (pivot) xung quanh đỏ circled $1/3$ để thu được
$$x_{1}x_{2}x_{4}\xi_{1} \xi_{2} \xi_{3}$$
$$1/20-10-5/2-3/20$$
$$x_{4} = 1/20311/2-1/20.$$
$$x_{1} = 1/211/301/61/60$$
$$\xi_{3}  = 1/20-10-3/2-1/21$$
Tại điều này giai đoạn có không có dương rút gọn chi phí, và ta phải tính
$$z^{*}= (-1 -1 -1) -(-5/2 -3/2 0) = (3/2 1/2 -1),$$
$$y^{+}A^{3} -c_{3} = (-1/6 1/2 -1/3) \begin{pmatrix} -3 \\ 6 \\ 0 \end{pmatrix} + 3 = 13/2,$$
$$z^{*}A^{3} = -(3/2 1/2 -1) \begin{pmatrix} -3 \\ 6 \\ 0 \end{pmatrix} = 3/2,$$
Do đó
$$\theta^{+}  = \frac{13}{3} ,$$
$$y^{+}= (-1/6 1/2 -1/3) + \frac{13}{3} (3/2 1/2 -1) = (19/3 8/3 -14/3).$$

<!-- PAGE 1673 -->
Ta plug $y^{+}$ vào $(D)$ và discover rằng thứ nhất, thứ ba, và thứ tư các ràng buộc là các đẳng thức. Do đó, $J = {1, 3, 4}$ và Bị thu hẹp Gốc (primal) (RP4) là Cực đại hóa - $(\xi_{1}  + \xi_{2}  + \xi_{3}$)
$$subject to \begin{pmatrix} 3 & -3 & 1 & 1 & 0 & 0 \\ 3 & 6 & -1 & 0 & 1 & 0 \\ 6 & 0 & 1 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{3} \\ x_{4} \\ \xi_{1} \\ \xi_{2} \\ \xi_{3} \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ 4 \end{pmatrix} and x_{1}, x_{3}, x_{4}, \xi_{1} , \xi_{2} , \xi_{3}  \ge 0.$$
Ban đầu bảng đơn hình (tableau) cho (RP4), với cˆ $= (0, 0, 0, -1, -1, -1), (x_{1}, x_{3}, x_{4}, \xi_{1} , \xi_{2} , \xi_{3}$) $= (1/2, 0, 1/2, 0, 0, 1/2)$ và $K = (3, 1, 6)$ là thu được từ cuối cùng bảng đơn hình (tableau) của trước đó (RP3) bằng cách thay thế cột tương ứng với biến $x_{2}$ bởi cột tương ứng với biến $x_{3}$, cụ thể là
$$A_{K}^{-1}b A^{3} = \begin{pmatrix} 1/2 & -1/2 & 0 \\ 1/6 & 1/6 & 0 \\ 3/2 & 1/2 & 1 \end{pmatrix} \begin{pmatrix} -3 \\ 6 \\ 0 \end{pmatrix} = \begin{pmatrix} -9/2 \\ 1/2 \\ 3/2 \end{pmatrix} ,$$
$$--$$
Với
$$\overline{c}_{3} = c_{3} -z^{*}A^{3} = 0 - \begin{pmatrix} 3/2 & 1/2 & -1 \end{pmatrix} \begin{pmatrix} -3 \\ 6 \\ 0 \end{pmatrix} = 3/2,$$
Và ta thu được
$$x_{1}x_{3}x_{4}\xi_{1} \xi_{2} \xi_{3}$$
$$1/203/20-5/2-3/20$$
$$x_{4} = 1/20-9/211/2-1/20$$
$$.$$
$$x_{1} = 1/211/201/61/60$$
$$\xi_{3}  = 1/203/20-3/2-1/21$$
Bởi analyzing đỉnh/trên hàng của rút gọn chi phí, ta xem rằng $j^{+} = 2$. Hơn nữa, vì $min{x_{1}/(1/2), \xi_{3} /(3/2)} = \xi_{3} /(3/2) = 1/3$, ta cho $k^{-} = 6, K = (3, 1, 2)$, và phần tử trụ (pivot) dọc theo đỏ circled $3/2$ để thu được
$$x_{1}x_{3}x_{4}\xi_{1} \xi_{2} \xi_{3}$$
$$0000-1-1-1$$
$$x_{4} = 2001-4-23.$$
$$x_{1} = 1/31002/31/3-1/3$$
$$x_{3} = 1/3010-1-1/32/3$$
Vì trên trái góc của cuối cùng bảng đơn hình (tableau) là không và rút gọn chi phí là tất cả $\le 0$, ta là cuối cùng được hoàn tất. Thì $y = (19/3 8/3 -14/3)$ là nghiệm tối ưu (optimal solution) của $(D)$, nhưng nhiều hơn/thêm
