# Hạt nhân (kernel) -SV Hồi quy


<!-- PAGE 2134 -->
$q_{m} = 19$. Có $13$ các điểm chặt bên trong dải phẳng (slab). cuối cùng giá trị của $\nu$ là $\nu  =$ 0.97, xem Hình 56.15. Ta có $p_{f} = 23, q_{f} = 24, p_{m} = 25$ và $q_{m} = 25$. Có $0$ các điểm chặt bên trong dải phẳng (slab). dải phẳng (slab) là do đó narrow rằng nó thực hiện không chứa bất kỳ của các điểm $x_{i}$ trong nó. Chạy bài toán quy hoạch với bất kỳ giá trị $\nu  >$ 0.97 cho ta $\epsilon  = 0$.
$$80$$
$$60$$
$$40$$
$$20$$
$$0$$
$$-20$$
$$-40$$
$$-40-30-20-100102030405060$$
$$Figure 56.15: Running \nu -SV regression on a set of 50 points; \nu  = 0.97.$$

## 56.4 Hạt nhân (kernel) \nu -SV Hồi quy

Vì các công thức cho $w, b$, và f(x),
$$w = \sum_{i=1}^{m}  (\mu_{i}  -\lambda_{i} )x_{i}$$
$$b = \frac{1}{2} \begin{pmatrix} y_{i0}+ y_{j0}-w^{\top}(x_{i0}+ x_{j0}) \end{pmatrix}$$
$$f(x) = \sum_{i=1}^{m}  (\mu_{i}  -\lambda_{i} )x_{i}^{\top} x + b,$$
Chỉ liên quan đến trong các tích trong số dữ liệu các điểm $x_{i}$ và $x$, và vì hàm mục tiêu (objective function) $-G(\alpha , \mu$) của đối ngẫu (dual) bài toán quy hoạch cũng chỉ liên quan đến trong các tích trong số dữ liệu các điểm $x_{i}$, ta có thể kernelize $\nu$ -SV hồi quy phương pháp.

<!-- PAGE 2135 -->
Như trong mục trước, ta giả sử rằng của ta dữ liệu các điểm ${x_{1}, \dots  , x_{m}}$ thuộc đến $set\mathcal{X}$ và ta pretend rằng ta có đặc trưng (feature) không gian $(F, \langle$ -, $-\rangle$) và đặc trưng (feature) phép nhúng (embedding) ánh xạ $\phi$: $\mathcal{X} \to F$, nhưng ta chỉ có access đến hạt nhân (kernel) hàm $\kappa (x_{i}, x_{j}) = \langle \phi (x_{i}), \phi (x_{j})\rangle$. Ta muốn đến perform $\nu$ -SV hồi quy trong đặc trưng (feature) không gian $F$ trên dữ liệu tập hợp ${(\phi (x_{1}), y_{1}), \dots  , (\phi (x_{m}), y_{m})}$. Đi trên trước đó phép tính, ta xem rằng gốc (primal) bài toán quy hoạch được cho bởi Bài toán quy hoạch hạt nhân (kernel) $\nu$ -SV Hồi quy:
$$minimize \frac{1}{2} \langle w, w\rangle + C \begin{pmatrix} 1 \\ \nu \epsilon  + & (\xi_{i}  + \xi_{i}' ) \\ m \end{pmatrix} \sum_{i=1}^{m}$$
$$subject to$$
$$\langle w, \phi (x_{i})\rangle + b -y_{i} \le \epsilon  + \xi_{i} ,\xi_{i}  \ge 0i = 1, \dots  , m$$
$$-\langle w, \phi (x_{i})\rangle -b + y_{i} \le \epsilon  + \xi_{i}' ,\xi_{i}'  \ge 0i = 1, \dots  , m$$
$$\epsilon  \ge 0,$$
Cực tiểu hóa trên các biến $w, \epsilon , b, \xi$, và $\xi'$. Hàm Lagrange (Lagrangian) được cho bởi
$$*+$$
$$L(w, b, \lambda , \mu , \gamma , \xi , \xi' , \epsilon , \alpha , \beta ) = \frac{1}{2} \langle w, w\rangle +w, \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} )\phi (x_{i})$$
$$!$$
$$+ \epsilon C\nu  -\gamma  - \sum_{i=1}^{m}  (\lambda_{i}  + \mu_{i} )+ \sum_{i=1}^{m}  \xi_{i} \begin{pmatrix} C \\ -\lambda_{i}  -\alpha_{i} \\ m \end{pmatrix}$$
$$!$$
$$+ \sum_{i=1}^{m}  \xi_{i}' \begin{pmatrix} C \\ -\mu_{i}  -\beta_{i} \\ m \end{pmatrix} + b \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} )- \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} )y_{i}.$$
Đặt gradien $\nabla L_{w,\epsilon ,b,\xi ,\xi'}$ của Hàm Lagrange (Lagrangian) đến không, ta cũng thu được các phương trình
$$w = \sum_{i=1}^{m}  (\mu_{i}  -\lambda_{i} )\phi (x_{i}),(*_{w})$$
$$\sum_{i=1}^{m}  \lambda_{i}  - \sum_{i=1}^{m}  \mu_{i}  = 0$$
$$\sum_{i=1}^{m}  \lambda_{i}  + \sum_{i=1}^{m}  \mu_{i}  + \gamma  = C\nu$$
$$\lambda  + \alpha  = \frac{C}{m} ,\mu  + \beta  = \frac{C}{m} .$$
Bằng cách sử dụng ở trên các phương trình, ta tìm rằng đối ngẫu (dual) hàm $G$ là độc lập của các biến $\beta , \alpha , \beta$, và ta thu được kết quả sau đối ngẫu (dual) bài toán quy hoạch:

<!-- PAGE 2136 -->
Đối ngẫu (dual) Bài toán quy hoạch hạt nhân (kernel) $\nu$ -SV Hồi quy:
$$minimize \frac{1}{2} \sum_{i,j=1}^{m}  (\lambda_{i}  -\mu_{i} )(\lambda_{j}  -\mu_{j} )\kappa (x_{i}, x_{j}) + \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} )y_{i}$$
$$subject to$$
$$\sum_{i=1}^{m}  \lambda_{i}  - \sum_{i=1}^{m}  \mu_{i}  = 0$$
$$\sum_{i=1}^{m}  \lambda_{i}  + \sum_{i=1}^{m}  \mu_{i}  \le C\nu$$
$$0 \le \lambda_{i}  \le \frac{C}{m} ,0 \le \mu_{i}  \le \frac{C}{m} ,i = 1, \dots  , m,$$
Cực tiểu hóa trên $\alpha$ và $\mu$. Everything ta được nói trước cũng áp dụng đến hạt nhân (kernel) $\nu$ -SV hồi quy phương pháp, ngoại trừ rằng $x_{i}$ được thay thế bởi $\phi (x_{i})$ và rằng tích vô hướng (inner product) $\langle$ -, $-\rangle$ phải được sử dụng, và ta có các công thức
$$w = \sum_{i=1}^{m}  (\mu_{i}  -\lambda_{i} )\phi (x_{i})$$
$$!$$
$$b = \frac{1}{2} y_{i0} + y_{j0} - \sum_{i=1}^{m}  (\mu_{i}  -\lambda_{i} )(\kappa (x_{i}, x_{i0}) + \kappa (x_{i}, x_{j0}))$$
$$f(x) = \sum_{i=1}^{m}  (\mu_{i}  -\lambda_{i} )\kappa (x_{i}, x) + b,$$
Các biểu thức rằng chỉ liên quan đến $\kappa$.
Nhận xét: Có một biến thể của $\nu$ -SV hồi quy thu được bằng cách đặt $\nu  = 0$ và giữ $\epsilon  > 0$ cố định. phương pháp này được gọi là $\epsilon$ -SV hồi quy hoặc (tuyến tính) $\epsilon$ -insensitive SV hồi quy. tương ứng tối ưu hóa bài toán quy hoạch là Bài toán quy hoạch $\epsilon$ -SV Hồi quy:
$$minimize \frac{1}{2} w^{\top}w + \frac{C}{m} \sum_{i=1}^{m}  (\xi_{i}  + \xi_{i}' )$$
$$subject to$$
$$w^{\top}x_{i} + b -y_{i} \le \epsilon  + \xi_{i} ,\xi_{i}  \ge 0i = 1, \dots  , m$$
$$-w^{\top}x_{i} -b + y_{i} \le \epsilon  + \xi_{i}' ,\xi_{i}'  \ge 0i = 1, \dots  , m,$$
Cực tiểu hóa trên các biến $w, b, \xi$, và $\xi'$, giữ $\epsilon$ cố định. Nó là dễ để xem rằng đối ngẫu (dual) bài toán quy hoạch là
