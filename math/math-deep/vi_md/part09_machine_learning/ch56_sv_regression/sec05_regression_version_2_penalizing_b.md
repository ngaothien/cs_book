# -Hồi quy Phiên bản 2; Penalizing b


<!-- PAGE 2137 -->
Đối ngẫu (dual) Bài toán quy hoạch $\epsilon$ -SV Hồi quy:
$$minimize \frac{1}{2} \sum_{i,j=1}^{m}  (\lambda_{i}  -\mu_{i} )(\lambda_{j}  -\mu_{j} )x_{i}^{\top} x_{j} + \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} )y_{i} + \epsilon \sum_{i=1}^{m}  (\lambda_{i}  + \mu_{i} )$$
$$subject to$$
$$\sum_{i=1}^{m}  \lambda_{i}  - \sum_{i=1}^{m}  \mu_{i}  = 0$$
$$0 \le \lambda_{i}  \le \frac{C}{m} ,0 \le \mu_{i}  \le \frac{C}{m} ,i = 1, \dots  , m,$$
Cực tiểu hóa trên $\alpha$ và $\mu$. ràng buộc
$$\sum_{i=1}^{m}  \lambda_{i}  + \sum_{i=1}^{m}  \mu_{i}  \le C\nu$$
$$is gone but the extra term \epsilon \sum_{i}  m=1(\lambda_{i}  + \mu_{i} ) has been added to the dual function, to prevent$$
$\lambda_{i}$ và $\mu_{i}$ từ blowing lên. Có một hiển nhiên kernelized phiên bản của $\epsilon$ -SV hồi quy. Nó là dễ để chỉ ra rằng $\nu$ -SV hồi quy subsumes $\epsilon$ -SV hồi quy, trong nghĩa rằng nếu $\nu$ -SV hồi quy thành công và cho ta $w, b, \epsilon  > 0$, thì $\epsilon$ -SV hồi quy với cùng $C$ và cùng giá trị của $\epsilon$ cũng thành công và trả về cùng cặp $(w, b)$. Cho nhiều hơn/thêm chi tiết trên các phương pháp này, xem Sch¨olkopf, Smola, Williamson, và Bartlett $[153]$.
$$Remark: The linear penalty function \sum_{i}  m=1(\xi_{i} +\xi_{i}' ) can be replaced by the quadratic penalty$$
$$function \sum_{i}  m(\xi_{i}^{2}  + \xi_{i}^{'2}  ); see Shawe–Taylor and Christianini [165] (Chapter 7). In this case,$$
Nó là dễ $to^{=1}$ xem rằng cho nghiệm tối ưu (optimal solution) ta phải có $\xi_{i}  \ge 0$ và $\xi_{i}'  \ge 0$, do đó ta có thể bỏ qua các ràng buộc $\xi_{i}  \ge 0$ và $\xi_{i}'  \ge 0$. Ta phải cũng có $\gamma  = 0$ do đó ta bỏ qua biến $\gamma$ cũng vậy. Nó có thể được được hiển thị rằng $\xi  = (m/2C)\lambda$ và $\xi' = (m/2C)\mu$. bài toán này là rất đồng dạng đến Lề mềm (soft margin) SVM $(SVM_{s4})$ được thảo luận trong Mục 54.13. 56.5 $\nu$ -Hồi quy Phiên bản $2$; Penalizing $b$ Vẫn chưa một cái khác biến thể của $\nu$ -SV hồi quy là đến cộng $term^{1}b^{2}$ đến hàm mục tiêu (objective function). Ta sẽ xem rằng việc giải đối ngẫu (dual) không chỉ xác định $w but^{2}$ cũng $b$ và $\epsilon$ (miễn là/được cung cấp nhẹ điều kiện trên $\nu$). Ta muốn để giải sau đây bài toán quy hoạch:

<!-- PAGE 2138 -->
Bài toán quy hoạch $\nu$ -SV Hồi quy Phiên bản $2$
$$minimize \frac{1}{2} w^{\top}w + \frac{1}{2} b^{2} + C \begin{pmatrix} 1 \\ \nu \epsilon  + & (\xi_{i}  + \xi_{i}' ) \\ m \end{pmatrix} \sum_{i=1}^{m}$$
$$subject to$$
$$w^{\top}x_{i} + b -y_{i} \le \epsilon  + \xi_{i} ,\xi_{i}  \ge 0i = 1, \dots  , m$$
$$-w^{\top}x_{i} -b + y_{i} \le \epsilon  + \xi_{i}' ,\xi_{i}'  \ge 0i = 1, \dots  , m,$$
Cực tiểu hóa trên các biến $w, b, \epsilon , \xi$, và $\xi'$. ràng buộc $\epsilon  \ge 0$ được bỏ qua vì bài toán có không có nghiệm nếu $\epsilon  < 0$. Ta để lại nó như một bài tập để chỉ ra rằng mới Hàm Lagrange (Lagrangian) là
$$!$$
$$L(w, b, \lambda , \mu , \xi , \xi' , \epsilon , \alpha , \beta ) = \frac{1}{2} w^{\top}w + w^{\top} \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} )x_{i}$$
$$!$$
$$+ \epsilon C\nu  - \sum_{i=1}^{m}  (\lambda_{i}  + \mu_{i} )+ \sum_{i=1}^{m}  \xi_{i} \begin{pmatrix} C \\ -\lambda_{i}  -\alpha_{i} \\ m \end{pmatrix}$$
$$!$$
$$+$$
$$+ \sum_{i=1}^{m}  \xi_{i}' \begin{pmatrix} C \\ -\mu_{i}  -\beta_{i} \\ m \end{pmatrix} + \frac{1}{2} b^{2} b \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} )- \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} )y_{i}.$$
Nếu ta tập hợp Laplacian $\nabla L_{w,\epsilon ,b,\xi ,\xi'}$ đến không ta thu được các phương trình
$$w = \sum_{i=1}^{m}  (\mu_{i}  -\lambda_{i} )x_{i} = X^{\top}(\mu  -\lambda )(*_{w})$$
$$C\nu  - \sum_{i=1}^{m}  (\lambda_{i}  + \mu_{i} ) = 0$$
$$b + \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} ) = 0$$
$$\frac{C}{m} -\lambda  -\alpha  = 0, \frac{C}{m} -\mu  -\beta  = 0.$$
Ta thu được mới phương trình
$$b = - \sum_{i=1}^{m}  (\lambda_{i}  -\mu_{i} ) = -(1_{m}^{\top}\lambda  -1_{m}^{\top}\mu )(*_{b})$$
Xác định $b$, mà thay thế phương trình
$$\sum_{i=1}^{m}  \lambda_{i}  - \sum_{i=1}^{m}  \mu_{i}  = 0.$$

<!-- PAGE 2139 -->
Plugging quay lại $w$ từ $(*_{w})$ và $b$ từ $(*_{b})$ vào Hàm Lagrange (Lagrangian) ta thu được
$$-$$
$$G(\lambda , \mu , \alpha , \beta ) = - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} P \begin{pmatrix} \lambda \\ \mu \end{pmatrix} -q^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + \frac{1}{2} b^{2}b^{2}$$
$$= - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} P \begin{pmatrix} \lambda \\ \mu \end{pmatrix} -q^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} - \frac{1}{2} b^{2}$$
$$= - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{m}1_{m}^{\top} & -1_{m}1_{m}^{\top} \\ P+ & -1_{m}1_{m}^{\top} & 1_{m}1_{m}^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} -q^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} ,$$
Với
$$P = \begin{pmatrix} XX^{\top} & -XX^{\top} \\ -XX^{\top} & XX^{\top} \end{pmatrix} = \begin{pmatrix} K & -K \\ -K & K \end{pmatrix}$$
Và
$$q = \begin{pmatrix} y \\ -y \end{pmatrix} .$$
Mới đối ngẫu (dual) bài toán quy hoạch là Đối ngẫu (dual) Bài toán quy hoạch $\nu$ -SV Hồi quy Phiên bản $2$
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{m}1_{m}^{\top} & -1_{m}1_{m}^{\top} \\ P+ & -1_{m}1_{m}^{\top} & 1_{m}1_{m}^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + q^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{m}  \lambda_{i}  + \sum_{i=1}^{m}  \mu_{i}  = C\nu$$
$$0 \le \lambda_{i}  \le \frac{C}{m} ,0 \le \mu_{i}  \le \frac{C}{m} ,i = 1, \dots  , m.$$
Định nghĩa 56.1 và Định nghĩa 56.2 là unchanged. Ta có kết quả sau phiên bản của Mệnh đề 56.2 chỉ ra rằng $p_{f}, q_{f}, p_{m}$ $q_{m}$ có trực tiếp influence trên lựa chọn của $\nu$.

> **Mệnh đề 56.7.**
$(1)$ Cho $p_{f}$ là số của các điểm $x_{i}$ sao cho $\lambda_{i}  = C/m$, và cho $q_{f}$ là số của các điểm $x_{i}$ sao cho $\mu_{i}  = C/m$. Ta có $p_{f} + q_{f} \le m\nu$.
$(2)$ Cho $p_{m}$ là số của các điểm $x_{i}$ sao cho $\lambda_{i}  > 0$, và cho $q_{m}$ là số của các điểm $x_{i}$ sao cho $\mu_{i}  > 0$. Ta có $p_{m} + q_{m} \ge m\nu$.
$(3)$ Nếu $p_{f} \ge 1$ hoặc $q_{f} \ge 1$, thì $\nu  \ge 1/m$.

*Chứng minh.* $(1)$ Cho $K_{\lambda}$ và $K_{\mu}$ là các tập hợp của các chỉ số tương ứng với các điểm thất bại lề (margin),
$$K_{\lambda} = {i \in {1, \dots  , m} | \lambda_{i}  = C/m}$$
$$K_{\mu} = {i \in {1, \dots  , m} | \mu_{i}  = C/m}.$$

<!-- PAGE 2140 -->
Theo Định nghĩa $p_{f} = |K_{\lambda}|, q_{f} = |K_{\mu}|$. Vì phương trình
$$\sum_{i=1}^{m}  \lambda_{i}  + \sum_{j=1}^{m}  \mu_{j}  = C\nu$$
Nghiệm đúng, theo định nghĩa của $K_{\lambda}$ và $K_{\mu}$ ta có
$$(p_{f} + q_{f}) \frac{C}{m} = \sum_{i\in K\lambda}  \lambda_{i}  + \sum_{j\in K\mu}  \mu_{j}  \le \sum_{i=1}^{m}  \lambda_{i}  + \sum_{j=1}^{m}  \mu_{j}  = C\nu ,$$
Mà suy ra rằng
$$p_{f} + q_{f} \le m\nu .$$
$(2)$ Cho $I_{\lambda >0}$ và $I_{\mu >0}$ là các tập hợp của các chỉ số
$$I_{\lambda >0} = {i \in {1, \dots  , m} | \lambda_{i}  > 0}$$
$$I_{\mu >0} = {i \in {1, \dots  , m} | \mu_{i}  > 0}.$$
Theo Định nghĩa $p_{m} = |I_{\lambda >0}|, q_{m} = |I_{\mu >0}|$. Ta có
$$\sum_{i=1}^{m}  \lambda_{i}  + \sum_{j=1}^{m}  \mu_{j}  = \sum_{i\in I\lambda >0}  \lambda_{i}  + \sum_{j\in I\mu >0}  \mu_{j}  = C\nu .$$
Vì $\lambda_{i}  \le C/m$ và $\mu_{j}  \le C/m$, ta thu được
$$C\nu  \le (p_{m} + q_{m}) \frac{C}{m} ,$$
Rằng là, $p_{m} + q_{m} \ge m\nu$.
$(3)$ suy ra ngay lập tức từ $(1)$. Mệnh đề 56.7 cho ta sau đây các cận trên $\nu$:
$$\frac{p_{f}+ q_{f}}{m} \le \nu  \le \frac{p_{m} + q_{m}}{m} .$$
Một lần nữa, nhỏ hơn $\nu$ là, wider $\epsilon$ -dải phẳng (slab) là, và lớn hơn $\nu$ là, narrower $\epsilon$ -dải phẳng (slab) là.
Nhận xét: Nó có thể được được hiển thị rằng với mọi nghiệm tối ưu (optimal solution) với w̸ $= 0$ và $\epsilon  > 0$, nếu các bất đẳng thức $(p_{f} + q_{f})/m < \nu  < 1$ đúng, thì một số điểm $x_{i}$ là hỗ trợ/giá (support) vectơ. chứng minh là về cơ bản Trường hợp 1b trong chứng minh của Mệnh đề 56.4. Ta để lại chi tiết như một bài tập.

<!-- PAGE 2141 -->
Mới đối ngẫu (dual) bài toán quy hoạch được giải bằng cách sử dụng ADMM. $(2m+1)\times$ 4m ma trận $A_{3}$ tương ứng với equational các ràng buộc
$$\sum_{i=1}^{m}  \lambda_{i}  + \sum_{i=1}^{m}  \mu_{i}  = C\nu$$
$$\lambda  + \alpha  = \frac{C}{m} ,\mu  + \beta  = \frac{C}{m} ,$$
Được cho bởi
$$A_{3} = \begin{pmatrix} 1_{m}^{\top} & 1_{m}^{\top} & 0_{m}^{\top} & 0_{m}^{\top} \\ I_{m} & 0_{m,m} & I_{m} & 0_{m,m} \\ 0_{m,m} & I_{m} & 0_{m,m} & I_{m} \end{pmatrix} .$$
Ta để lại nó như một bài tập để chỉ ra rằng $A_{3}$ có hạng (rank) 2m $+ 1$. Ta định nghĩa vectơ $c_{3}$ (có số chiều 2m $+ 1)$ như
$$c_{3} = \begin{pmatrix} C\nu \\ C1_{2m} \\ \overline{m} \end{pmatrix} .$$
Vì có 4m Các nhân tử Lagrange (Lagrange multipliers) $(\lambda , \mu , \alpha , \beta$), ta cần đến pad 2m $\times$ 2m ma trận
$$P_{3} = P + \begin{pmatrix} 1_{m}1_{m}^{\top} & -1_{m}1_{m}^{\top} \\ -1_{m}1_{m}^{\top} & 1_{m}1_{m}^{\top} \end{pmatrix} with zeros to make it into a 4m \times  4m matrix$$
$$P_{3a} = \begin{pmatrix} P_{3} & 0_{2m,2m} \\ 0_{2m,2m} & 0_{2m,2m} \end{pmatrix} .$$
Tương tự, ta pad $q$ với các không điểm để tạo nó vectơ $q_{3a}$ có số chiều 4m,
$$q_{3a} = \begin{pmatrix} q \\ 0_{2m} \end{pmatrix} .$$
Nó vẫn còn để tính $\epsilon$. Ther là hai các phương pháp đến thực hiện điều này. thứ nhất phương pháp giả sử Tiêu chuẩn Lề (margin) Giả thiết, mà là rằng tồn tại một $i_{0}$ sao cho $0 < \lambda_{i0}  < C/m$ hoặc tồn tại một $j_{0}$ sao cho $0 < \mu_{j0}  < C/m$; nói cách khác, tồn tại một hỗ trợ/giá (support) vectơ của loại/kiểu $1$. Bởi độ bù lỏng (complementary slackness) các điều kiện, $\xi_{i0}  = 0$ hoặc $\xi_{j0}'  = 0$, do đó ta có hoặc $w^{\top}x_{i0} + b$ - $y_{i0} = \epsilon$ hoặc $-w^{\top}x_{j0}$ - $b + y_{j0} = \epsilon$, mà xác định $\epsilon$. Do số tính mất ổn định, khi viết máy tính bài toán quy hoạch nó được ưu tiên hơn để tính các danh sách của các chỉ số $I_{\lambda}$ và $I_{\mu}$ cho trước bởi
$$I_{\lambda} = {i \in {1, \dots  , m} | 0 < \lambda_{i}  < C/m}$$
$$I_{\mu} = {j \in {1, \dots  , m} | 0 < \mu_{j}  < C/m}.$$

<!-- PAGE 2142 -->
Thì nó là dễ để xem rằng ta có thể tính $\epsilon$ bằng cách sử dụng sau đây lấy trung bình các công thức: nếu $I_{\lambda} \neq  \emptyset$, thì
$$\epsilon  = w^{\top} \begin{pmatrix} x_{i} \\ i \end{pmatrix} \sum_{\in I\lambda}  /|I_{\lambda}| + b - \begin{pmatrix} y_{i} \\ i \end{pmatrix} \sum_{\in I\lambda}  /|I_{\lambda}|,$$
Và nếu $I_{\mu} \neq  \emptyset$, thì
$$\epsilon  = -w^{\top} \begin{pmatrix} x_{j} \end{pmatrix} \sum_{j\in I\mu}  /|I_{\mu}| -b + \begin{pmatrix} y_{i} \\ i \end{pmatrix} \sum_{\in I\mu}  /|I_{\mu}|.$$
Thứ hai phương pháp sử dụng đối ngẫu. Dưới nhẹ điều kiện, biểu diễn rằng khoảng cách đối ngẫu (duality gap) là không, ta có thể xác định $\epsilon$ theo $\lambda , \mu$ và $b$. Điều này là bởi vì các điểm $x_{i}$ rằng thất bại lề (margin), mà có nghĩa là $\lambda_{i}  = C/m$ hoặc $\mu_{i}  = C/m$, là chỉ các điểm cho mà $\xi_{i}  > 0$ hoặc $\xi_{i}'  > 0$. Nhưng trong trường hợp này ta có hoạt động ràng buộc
$$w^{\top}x_{i} + b -y_{i} = \epsilon  + \xi_{i} (*_{\xi})$$
Hoặc
$$-w^{\top}x_{i} -b + y_{i} = \epsilon  + \xi_{i}' ,(*_{\xi'})$$
Do đó $\xi_{i}$ và $\xi_{i}'$ có thể được được biểu diễn theo $w$ và $b$. Vì khoảng cách đối ngẫu (duality gap) là không cho nghiệm tối ưu (optimal solution), giá trị tối ưu (optimal value) của gốc (primal) bằng giá trị tối ưu (optimal value) của đối ngẫu (dual). Bằng cách sử dụng sự kiện rằng
$$w = X^{\top}(\mu  -\lambda )$$
$$b = -(1_{m}^{\top}\lambda  -1_{m}^{\top}\mu ) = \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} -1_{m} \\ 1_{m} \end{pmatrix}$$
Ta thu được biểu thức cho giá trị tối ưu (optimal value) của gốc (primal). Thứ nhất ta có
$$\frac{1}{2} w^{\top}w + \frac{1}{2} b^{2}= \frac{1}{2} (\lambda^{\top} -\mu^{\top} )XX^{\top}(\lambda  -\mu ) + \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{m}1_{m}^{\top} & -1_{m}1_{m}^{\top} \\ -1_{m}1_{m}^{\top} & 1_{m}1_{m}^{\top} \\ \lambda  \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$= \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \mu \end{pmatrix} ,$$
$$\begin{pmatrix} 1_{m}1_{m}^{\top} & -1_{m}1_{m}^{\top} \\ P+ & -1_{m}1_{m}^{\top} & 1_{m}1_{m}^{\top} \end{pmatrix}$$
Với
$$P = \begin{pmatrix} XX^{\top} & -XX^{\top} \\ -XX^{\top} & XX^{\top} \end{pmatrix} .$$
Cho $K_{\lambda}$ và $K_{\mu}$ là các tập hợp của các chỉ số tương ứng với các điểm thất bại lề (margin),
$$K_{\lambda} = {i \in {1, \dots  , m} | \lambda_{i}  = C/m}$$
$$K_{\mu} = {i \in {1, \dots  , m} | \mu_{i}  = C/m}.$$

<!-- PAGE 2143 -->
Bởi vì $\lambda_{i} \mu_{i}  = 0$, các tập hợp $K_{\lambda}$ và $K_{\mu}$ là rời nhau. Nhận thấy rằng từ Định nghĩa 56.2 ta có $p_{f} = |K_{\lambda}|$ và $q_{f} = |K_{\mu}|$. Thì bởi $(*_{\xi})$ và $(*_{\xi'})$, ta có
$$\sum_{i=1}^{m}  (\xi_{i}  + \xi_{i}' ) = \sum_{i\in K\lambda}  \xi_{i}  + \sum_{j\in K\mu}  \xi_{j}'$$
$$= \sum_{i\in K\lambda}  (w^{\top}x_{i} + b -y_{i} -\epsilon ) + \sum_{j\in K\mu}  (-w^{\top}x_{j} -b + y_{j} -\epsilon )$$
$$= w^{\top} \begin{pmatrix} x_{i} - & x_{j} \end{pmatrix} \sum_{i\in K\lambda}  \sum_{j\in K\mu}  - \sum_{i\in K\lambda}  y_{i} + \sum_{j\in K\mu}  y_{j} + (p_{f} -q_{f})b -(p_{f} + q_{f})\epsilon .$$
Giá trị tối ưu (optimal value) của đối ngẫu (dual) được cho bởi
$$- \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{m}1_{m}^{\top} & -1_{m}1_{m}^{\top} \\ P+ & -1_{m}1_{m}^{\top} & 1_{m}1_{m}^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} -q^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} ,$$
Với
$$q = \begin{pmatrix} y \\ -y \end{pmatrix} .$$
Biểu diễn rằng khoảng cách đối ngẫu (duality gap) là không ta có
$$\frac{1}{2} w^{\top}w + \frac{1}{2} b^{2} + C\nu \epsilon  + \frac{C}{m} \sum_{i=1}^{m}  (\xi_{i}  + \xi_{i}' )$$
$$= - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{m}1_{m}^{\top} & -1_{m}1_{m}^{\top} \\ P+ & -1_{m}1_{m}^{\top} & 1_{m}1_{m}^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} -q^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} ,$$
Rằng là,
$$\frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{m}1_{m}^{\top} & -1_{m}1_{m}^{\top} \\ P+ & -1_{m}1_{m}^{\top} & 1_{m}1_{m}^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + C\nu \epsilon$$
$$+ \frac{C}{m} \begin{pmatrix}  \\ w^{\top} & x_{i} - & x_{j} \end{pmatrix} \sum_{i\in K\lambda}  \sum_{j\in K\mu}  \sum_{i\in K\lambda}  \sum_{j\in K\mu}$$
$$\begin{pmatrix} - & y_{i} + & y_{j}+ (p_{f}-q_{f})b -(p_{f}+ q_{f})\epsilon \\ 1 &  &  \end{pmatrix}$$
$$= -2 \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{m}1_{m}^{\top} & -1_{m}1_{m}^{\top} \\ P+ & -1_{m}1_{m}^{\top} & 1_{m}1_{m}^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} -q^{\top} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} .$$
Việc giải cho $\epsilon$ ta thu được
$$C \begin{pmatrix} p_{f}+ q_{f} \\ \nu  - \\ m \end{pmatrix} \epsilon  = - \begin{pmatrix} \lambda^{\top} & \mu^{\top} \\  \end{pmatrix} \begin{pmatrix} 1_{m}1_{m}^{\top} & -1_{m}1_{m}^{\top} \\ P+ & -11_{m}^{\top} & 11^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} - \begin{pmatrix} y^{\top} & -y^{\top} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$- \frac{C}{m} \begin{pmatrix}  \\ w^{\top} & x_{i} - & x_{j} \end{pmatrix} \begin{pmatrix} - & y_{i} + & y_{j}+ (p_{f}-q_{f})b \end{pmatrix} \sum_{i\in K\lambda}  \sum_{j\in K\mu}^{m}  \sum_{i\in K\lambda}^{mm}  \sum_{j\in K\mu}  ,$$
