# Độ bù lỏng (complementary slackness) Các điều kiện


<!-- PAGE 1653 -->

> **Hệ quả 47.10.** Gốc (primal) Bài toán quy hoạch $(P)$ có nghiệm tối ưu (optimal solution) khi và chỉ khi sau đây tập hợp của các ràng buộc là satisfiable:
$$Ax \le b$$
$$yA \ge c$$
$$cx \ge yb$$
$$x \ge 0, y \ge 0_{m}^{\top}.$$
Thực ra, với mọi nghiệm chấp nhận được (feasible solution) $(x^{*}, y^{*})$ của ở trên hệ, $x^{*}$ là nghiệm tối ưu (optimal solution) của
$(P)$ và $y^{*}$ là nghiệm tối ưu (optimal solution) của $(D)$

## 47.3 Độ bù lỏng (complementary slackness) Các điều kiện

Một cái khác hữu ích hệ quả của đối ngẫu mạnh (strong duality) định lý là kết quả sau đây đã biết như equilibrium định lý.

> **Định lý 47.11.** (Equilibrium Định lý) Với mọi Bài toán quy hoạch tuyến tính (linear program) $(P)$ và đối ngẫu (đối ngẫu (dual)) của nó Bài toán quy hoạch tuyến tính (linear program) $(D)$ (với tập hợp của các bất đẳng thức Ax $\le b$ ở đâu $A$ là một ma trận cỡ $m \times  n$, và hàm mục tiêu (objective function) $x \mapsto$ cx), với mọi nghiệm chấp nhận được (feasible solution) $x$ của $(P)$ và bất kỳ nghiệm chấp nhận được (feasible solution) $y$ của $(D), x$ và $y$ là tối ưu các nghiệm khi và chỉ khi
$$y_{i} = 0for all i for which \sum_{j}  n=1 a_{ij}x_{j} < b_{i}(*_{D})$$
Và
$$x_{j} = 0for all j for which \sum_{i}  m=1 y_{i}a_{ij} > c_{j}.(*_{P})$$

*Chứng minh.* Thứ nhất giả sử rằng $(*_{D})$ và $(*_{P})$ đúng. các phương trình trong $(*_{D})$ nói rằng $y_{i} = 0$ trừ khi
$$\sum_{j}  n=1 a_{ij}x_{j} = b_{i}, hence$$
$$yb = \sum_{i=1}^{m}  y_{i}b_{i} = \sum_{i=1}^{m}  y \sum_{ij=1}^{n}  a_{ij}x_{j} = \sum_{i=1j}^{m}  \sum_{=1}^{n}  y_{i}a_{ij}x_{j}.$$
$$Similarly, the equations in (*_{P}) say that x_{j} = 0 unless \sum_{i}  m=1 y_{i}a_{ij} = c_{j}, hence$$
$$cx = \sum_{j=1}^{n}  c_{j}x_{j} = \sum_{j=1}^{n}  \sum_{i=1}^{m}  y_{i}a_{ij}x_{j}.$$
Hệ quả là, ta thu được
$$cx = yb.$$
Bởi đối ngẫu yếu (weak duality) (Mệnh đề 47.6), ta có
$$cx \le yb = cx$$
