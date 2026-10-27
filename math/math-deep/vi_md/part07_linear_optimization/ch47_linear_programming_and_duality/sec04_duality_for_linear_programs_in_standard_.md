# Đối ngẫu cho Các bài toán quy hoạch tuyến tính trong Tiêu chuẩn Tạo thành


<!-- PAGE 1654 -->
Với mọi chấp nhận được (feasible) các nghiệm $x$ của $(P)$, do đó $x$ là nghiệm tối ưu (optimal solution) của $(P)$. Tương tự,
$$yb = cx \le yb$$
Với mọi chấp nhận được (feasible) các nghiệm $y$ của $(D)$, do đó $y$ là nghiệm tối ưu (optimal solution) của $(D)$. Bây giờ ta giả sử rằng $x$ là nghiệm tối ưu (optimal solution) của $(P)$ và rằng $y$ là nghiệm tối ưu (optimal solution) của $(D)$. Thì như trong chứng minh của Mệnh đề 47.6,
$$\sum_{j=1}^{n}  c_{j}x_{j} \le \sum_{i=1j}^{m}  \sum_{=1}^{n}  y_{i}a_{ij}x_{j} \le \sum_{i=1}^{m}  y_{i}b_{i}.$$
Bởi đối ngẫu mạnh (strong duality), vì $x$ và $y$ là tối ưu các nghiệm ở trên các bất đẳng thức là thực sự các đẳng thức, do đó đặc biệt ta có
$$\sum_{j=1}^{n}  \begin{pmatrix} c_{j}- & y_{i}a_{ij} \end{pmatrix} \sum_{i=1}^{m}  x_{j} = 0.$$
$$Since x and y are feasible, x_{i} \ge 0 and y_{j} \ge 0, so if \sum_{i}  m=1 y_{i}a_{ij} > c_{j}, we must have x_{j} = 0.$$
Tương tự, ta có
$$\sum_{i=1}^{m}  y_{i} \begin{pmatrix} a_{ij}x_{j}-b_{i} \end{pmatrix} \sum_{j=1}^{m}  = 0,$$
$$so if \sum_{j}  m=1 a_{ij}x_{j} < b_{i}, then y_{i} = 0.$$
Các phương trình trong $(*_{D})$ và $(*_{P})$ là thường được gọi là độ bù lỏng (complementary slackness) các điều kiện. các điều kiện này có thể được exploited để giải cho nghiệm tối ưu (optimal solution) của bài toán gốc (primal problem) với help của bài toán đối ngẫu (dual problem), và ngược lại. Thật vậy, nếu ta guess nghiệm đến một bài toán, thì ta có thể giải cho nghiệm của đối ngẫu (dual) bằng cách sử dụng độ bù lỏng (complementary slackness) các điều kiện, và thì kiểm tra rằng của ta guess đã là đúng. Điều này là essence của gốc-đối ngẫu (primal-dual) phương pháp. Đến trình bày phương pháp này, thứ nhất ta cần đến lấy closer nhìn tại đối ngẫu (dual) của bài toán quy hoạch tuyến tính (linear program) đã trong tiêu chuẩn tạo thành.

## 47.4 Đối ngẫu cho Các bài toán quy hoạch tuyến tính trong Tiêu chuẩn Tạo thành

Cho $(P)$ là bài toán quy hoạch tuyến tính (linear program) trong tiêu chuẩn tạo thành, ở đâu Ax $= b$ với một số $m \times  n$ ma trận của hạng (rank) $m$ và một số hàm mục tiêu (objective function) $x \mapsto$ cx (của course, $x \ge 0)$. để thu được đối ngẫu (dual) của $(P)$ ta chuyển đổi các phương trình Ax $= b$ đến sau đây hệ của các bất đẳng thức liên quan đến (2m) $\times  n$ ma trận:
$$\begin{pmatrix} A \\ -A \end{pmatrix} x \le \begin{pmatrix} b \\ -b \end{pmatrix} .$$

<!-- PAGE 1655 -->
$$\mathbb{R}^{m}$$
Thì nếu ta ký hiệu 2m đối ngẫu (dual) các biến bởi (y', y''), với y', y'' $\in$ ($)^{*}$, đối ngẫu (dual) của ở trên bài toán quy hoạch là
$$minimizey'b -y''b$$
$$subject to \begin{pmatrix} y' & y'' \end{pmatrix} \begin{pmatrix} A \\ -A \end{pmatrix} \ge c and y', y''\ge 0,$$
$$\mathbb{R}^{m}$$
Ở đâu y', y'' $\in$ ($)^{*}$, mà là tương đương đến
$$minimize(y'-y'')b$$
$$subject to(y'-y'')A \ge c and y', y''\ge 0,$$
$$\mathbb{R}^{m}$$
Ở đâu y', y'' $\in$ ($)^{*}$. Nếu ta viết $y =$ y' - y'', ta tìm rằng ở trên bài toán quy hoạch tuyến tính (linear program) là tương đương đến sau đây Bài toán quy hoạch tuyến tính (linear program) $(D)$:
$$minimizeyb$$
$$subject toyA \ge c,$$
Ở đâu $y \in (\mathbb{R}^{m})^{*}$. Nhận thấy rằng $y$ là không cần thiết là không âm; nó là tùy ý. Tiếp theo ta sẽ like đến biết những gì là phiên bản của Định lý 47.8 cho bài toán quy hoạch tuyến tính (linear program) đã trong tiêu chuẩn tạo thành. Điều này là rất đơn giản.

> **Định lý 47.12.** Xét Bài toán quy hoạch tuyến tính (linear program) (P2) trong tiêu chuẩn tạo thành
$$maximizecx$$
$$subject toAx = b and x \ge 0,$$
Và của nó Đối ngẫu (dual) $(D)$ cho trước bởi
$$minimizeyb$$
$$subject toyA \ge c,$$
Ở đâu $y \in (\mathbb{R}^{m})^{*}$. Nếu thuật toán đơn hình (simplex algorithm) ứng dụng đến Bài toán quy hoạch tuyến tính (linear program) (P2) kết thúc với nghiệm tối ưu (optimal solution) $(u^{*}, K^{*})$, ở đâu $u^{*}$ là cơ bản nghiệm chấp nhận được (feasible solution) và $K^{*}$ là cơ sở (basis) cho $u^{*}$, thì $y^{*} = c_{K*}A_{K*}^{-1}$ là nghiệm tối ưu (optimal solution) cho $(D)$ sao cho $cu^{*} = y^{*}b$. Hơn nữa, nếu ta giả sử rằng thuật toán đơn hình (simplex algorithm) được bắt đầu với cơ bản nghiệm chấp nhận được (feasible solution) $(u_{0}, K_{0})$ ở đâu $K_{0} = (n-m+1, \dots  , n)$ (các chỉ số của cuối cùng $m$ các cột của $A)$ và $A_{(n-m+1,...,n)} = I_{m}$ (cuối cùng $m$ các cột của $A$ constitute ma trận đơn vị (identity matrix) $I_{m})$, thì nghiệm tối ưu (optimal solution) $y^{*} = c_{K*}A_{K*}^{-1}$ cho $(D)$ là cho trước theo rút gọn chi phí bởi
$$y^{*}= c_{(n-m+1,...,n)} -(\overline{c}_{K*})_{(n-m+1,...,n)},$$
Và ma trận cỡ $m\times m$ bao gồm của cuối cùng $m$ các cột và cuối cùng $m$ các hàng của cuối cùng bảng đơn hình (tableau) là $A_{K*}^{-1}$.

<!-- PAGE 1656 -->

*Chứng minh.* chứng minh của Định lý 47.8 áp dụng với $A$ thay vì của $A$, và ta có thể chỉ ra rằng
$$b$$
$$c_{K*}A_{K*}^{-1}A_{N*}\ge c_{N*},$$
Và rằng $y^{*} = c_{K*}A_{K*}^{-1}$ thỏa mãn, $cu^{*} = y^{*}b$, và
$$y^{*}A_{K*}= c_{K*}A_{K*}^{-1}A_{K*}= c_{K*},$$
$$y^{*}A_{N*}= c_{K*}A_{K*}^{-1}A_{N*}\ge c_{N*}.$$
Cho $P$ là $n \times  n$ hoán vị ma trận được định nghĩa sao cho
$$AP = \begin{pmatrix} A_{K*} & A_{N*} \end{pmatrix} .$$
Thì ta cũng có
$$cP = \begin{pmatrix} c_{K*} & c_{N*} \\ we \end{pmatrix} ,$$
Và bằng cách sử dụng ở trên các phương trình và các bất đẳng thức thu được
$$y^{*} \begin{pmatrix} A_{K*} & A_{N*} \\ equivalentto \end{pmatrix} \ge \begin{pmatrix} c_{K*} & c_{N*} \end{pmatrix} ,$$
Rằng là, $y^{*}AP \ge$ cP, mà là
$$y^{*}A \ge c,$$
Mà chỉ ra rằng $y^{*}$ là nghiệm chấp nhận được (feasible solution) của $(D)$ (remember, $y^{*}$ là tùy ý do đó không có cần cho ràng buộc $y^{*} \ge 0)$. rút gọn chi phí được cho bởi
$$(\overline{c}_{K*})_{i} = c_{i} -c_{K*}A_{K*}^{-1}A^{i},$$
Và vì cho $j = n -m + 1, \dots  , n$ cột $A^{j}$ là $(j + m$ -n)th cột của ma trận đơn vị (identity matrix) $I_{m}$, ta có
$$(\overline{c}_{K*})_{j} = c_{j} -(c_{K*}A_{K*}^{-1})_{j+m-n}j = n -m + 1, \dots  , n,$$
Rằng là,
$$y^{*}= c_{(n-m+1,...,n)} -(\overline{c}_{K*})_{(n-m+1,...,n)},$$
Như đã khẳng định. Vì cuối cùng $m$ các hàng của cuối cùng bảng đơn hình (tableau) là thu được bằng cách nhân $[u_{0} A]$ bởi $A_{K}^{-1}$, và cuối cùng $m$ các cột của $A$ constitute $I_{m}$, cuối cùng $m$ các hàng và cuối cùng $m$ các cột của $the^{*}$ cuối cùng bảng đơn hình (tableau) constitute $A_{K*}^{-1}$. Cho chúng ta bây giờ lấy nhìn tại độ bù lỏng (complementary slackness) các điều kiện của Định lý 47.11. Nếu ta đi quay lại đến phiên bản của $(P)$ cho trước bởi
$$maximizecx$$
$$subject to \begin{pmatrix} A \\ -A \end{pmatrix} x \le \begin{pmatrix} b \\ -b \end{pmatrix} and x \ge 0,$$
