# Việc giải SVM (SVMs2') Bằng cách sử dụng ADMM


<!-- PAGE 2018 -->
Ta có các ví dụ ở đâu có một đơn lẻ hỗ trợ/giá (support) vectơ của loại/kiểu $1$ và $\nu  = 2q_{f}/(p + q)$, do đó ở trên phương pháp không thỏa mãn. Curiously, perturbing $\nu$ slightly cho ta nghiệm với một số xanh lam hỗ trợ/giá (support) vectơ của loại/kiểu $1$ và một số đỏ hỗ trợ/giá (support) vectơ của loại/kiểu $1$, và do đó ta có không vẫn chưa tìm thấy ví dụ ở đâu ở trên phương pháp thành công với đơn lẻ hỗ trợ/giá (support) vectơ của loại/kiểu $1$. Điều này suggests đến conduct một số perturbation giải tích/phân tích nhưng nó xuất hiện là không tầm thường. Trong số của nó advantages, hỗ trợ/giá (support) vectơ machinery là conducive đến việc tìm thú vị statistical các cận theo VC số chiều, khái niệm invented bởi Vapnik và Chernovenkis. Ta sẽ không đi vào điều này ở đây và thay vì refer độc giả đến Vapnik $[188]$ (especially, Chương $4$ và Các chương 9-13).

## 54.8 Việc giải SVM (SVM) Bằng cách sử dụng ADMM

$$s2'$$
Trong thứ tự để giải $(SVM_{s2'})$ bằng cách sử dụng ADMM ta cần đến viết ma trận tương ứng với các ràng buộc trong equational tạo thành,
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  -\gamma  = K_{m}$$
$$\lambda_{i}  + \alpha_{i}  = K_{s},i = 1, \dots  , p$$
$$\mu_{j}  + \beta_{j}  = K_{s},j = 1, \dots  , q,$$
Với $K_{m} = (p + q)K_{s}\nu$. Điều này là $(p + q + 2) \times$ (2(p $+ q) + 1)$ ma trận $A$ cho trước bởi
$$A = \begin{pmatrix} 1_{p}^{\top} & -1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} & 0 \\ 1_{p}^{\top} & 1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} & -1 \\ I_{p} & 0_{p,q} & I_{p} & 0_{p,q} & 0_{p} \\ 0_{q,p} & I_{q} & 0_{q,p} & I_{q} & 0_{q} \end{pmatrix} .$$
Quan sát đáng chú ý analogy với ma trận phát sinh trong $\nu$ -hồi quy trong Mục 56.3, ngoại trừ rằng $p = q = m$ và rằng $-1$ được thay thế bởi $+1$. Ta để lại nó như một bài tập để chứng minh rằng $A$ có hạng (rank) $p + q + 2$. vế phải là
$$c = \begin{pmatrix} 0 \\ K_{m} \\ K_{s}1_{p+q} \end{pmatrix} .$$
Đối xứng nửa xác định dương (positive semidefinite) $(p+q)\times (p+q)$ ma trận $P$ định nghĩa toàn phương phiếm hàm là
$$P = X^{\top}X,withX = \begin{pmatrix} -u_{1} & \cdots & -u_{p} & v_{1} & \cdots & v_{q} \end{pmatrix} ,$$

<!-- PAGE 2019 -->
Và
$$q = 0_{p+q}.$$
Vì có 2(p $+ q) + 1$ Các nhân tử Lagrange (Lagrange multipliers) $(\lambda , \mu , \alpha , \beta , \gamma$), ma trận cỡ $(p + q) \times  (p + q)$ $X^{\top}X$ phải là augmented với không’s để tạo nó (2(p $+ q) + 1) \times$ (2(p $+ q) + 1)$ ma trận $P_{a}$ cho trước bởi
$$P_{a} = \begin{pmatrix} X^{\top}X & 0_{p+q,p+q+1} \\ 0_{p+q+1,p+q} & 0_{p+q+1,p+q+1} \end{pmatrix} ,$$
Và tương tự $q$ là augmented với các không điểm như vectơ $q_{a} = 0_{2(p+q)+1}$. Như ta mentioned trong Mục 54.5, vì $\eta  \ge 0$ cho nghiệm tối ưu (optimal solution), ta có thể bỏ ràng buộc $\eta  \ge 0$ từ bài toán gốc (primal problem). Trong trường hợp này có $2(p+q)$ Các nhân tử Lagrange (Lagrange multipliers) $(\lambda , \mu , \alpha , \beta$). Nó là dễ để xem rằng hàm mục tiêu (objective function) của đối ngẫu (dual) là unchanged và tập hợp của các ràng buộc là
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = K_{m}$$
$$\lambda_{i}  + \alpha_{i}  = K_{s},i = 1, \dots  , p$$
$$\mu_{j}  + \beta_{j}  = K_{s},j = 1, \dots  , q,$$
Với $K_{m} = (p + q)K_{s}\nu$. ràng buộc ma trận tương ứng với hệ này của các phương trình là $(p + q + 2) \times$ 2(p $+ q)$ ma trận $A_{2}$ cho trước bởi
$$A_{2} = \begin{pmatrix} 1_{p}^{\top} & -1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} \\ 1_{p}^{\top} & 1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} \\ I_{p} & 0_{p,q} & I_{p} & 0_{p,q} \\ 0_{q,p} & I_{q} & 0_{q,p} & I_{q} \end{pmatrix} .$$
Ta để lại nó như một bài tập để chứng minh rằng $A_{2}$ có hạng (rank) $p + q + 2$. vế phải là
$$c_{2} = \begin{pmatrix} 0 \\ K_{m} \\ K_{s}1_{p+q} \end{pmatrix} .$$
Đối xứng nửa xác định dương (positive semidefinite) $(p+q)\times (p+q)$ ma trận $P$ định nghĩa toàn phương phiếm hàm là
$$P = X^{\top}X,withX = \begin{pmatrix} -u_{1} & \cdots & -u_{p} & v_{1} & \cdots & v_{q} \end{pmatrix} ,$$
Và
$$q = 0_{p+q}.$$

<!-- PAGE 2020 -->
Vì có 2(p $+ q)$ Các nhân tử Lagrange (Lagrange multipliers) ma trận cỡ $(p + q) \times  (p + q)$ $X^{\top}X$ phải là augmented với không’s để tạo nó 2(p $+ q) \times$ 2(p $+ q)$ ma trận $P_{2a}$ cho trước bởi
$$P_{2a} = \begin{pmatrix} X^{\top}X & 0_{p+q,p+q} \\ 0_{p+q,p+q} & 0_{p+q,p+q} \end{pmatrix} ,$$
Và tương tự $q$ là augmented với các không điểm như vectơ $q_{2a} = 0_{2(p+q)}$. Matlab các bài toán quy hoạch cài đặt ở trên phương pháp là cho trước trong Phụ lục $B$, Mục B.2. Ta ran của ta bài toán quy hoạch trên hai các tập hợp của $30$ các điểm mỗi được sinh tại ngẫu nhiên bằng cách sử dụng sau đây code mà gọi hàm runSVMs2pbv3: rho $= 10$; u16 $= 10.1*randn(2,30)+7$; v16 $=$ -10.1*randn(2,30)-7; [~,~,~,~,~,~,w3] $= runSVMs2pbv3(0.37,rho,u16,v16,1/60)$ Ta được chọn $K = 1/60$ và khác nhau các giá trị của $\nu$ bắt đầu với $\nu  =$ 0.37, mà xuất hiện là nhỏ nhất giá trị cho mà phương pháp hội tụ; xem Hình 54.11. Trong ví dụ này, $p_{f} = 10, q_{f} = 11, p_{m} = 12, q_{m} = 12$. toàn phương solver converged sau $8121$ các bước đến đạt tới gốc (primal) và đối ngẫu (dual) các phần dư nhỏ hơn hơn $10^{-10}$. Rút gọn $\nu$ ở dưới $\nu  =$ 0.37 có effect rằng $p_{f}, q_{f}, p_{m}, q_{m}$ giảm nhưng sau đây tình huống phát sinh. Shrinking $\eta$ little bit có effect rằng $p_{f} = 9, q_{f} = 10, p_{m} = 10, q_{m} = 11$. Thì $max{p_{f}, q_{f}} = min{p_{m}, q_{m}} = 10$, do đó chỉ khả dĩ/có thể giá trị cho $\nu$ là $\nu  = 20/60 = 1/3 =$ 0.3333333 $\cdots$. Khi ta chạy của ta bài toán quy hoạch với $\nu  = 1/3$, nó trả về giá trị của $\eta$ ít hơn $10^{-13}$ và giá trị của $w$ có các thành phần là cũng ít hơn $10^{-13}$. Điều này là probably do số precision. Các giá trị của $\nu$ ít hơn $1/3$ gây ra cùng bài toán. Nó xuất hiện rằng hình học của bài toán constrains các giá trị của $p_{f}, q_{f}, p_{m}, q_{m}$ trong như vậy cách rằng nó có không có nghiệm ngoài $w = 0$ và $\eta  = 0$. Hình 54.12 chỉ ra kết quả của chạy bài toán quy hoạch với $\nu  =$ 0.51. Ta có $p_{f} = 15, q_{f} = 16, p_{m} = 16, q_{m} = 16$. một cách thú vị, cho $\nu  =$ 0.5, ta chạy vào suy biến tình huống ở đâu ở đó là chỉ một hỗ trợ/giá (support) vectơ và $\nu  = 2p_{f}/(p + q)$.

<!-- PAGE 2021 -->
$$30$$
$$20$$
$$10$$
$$0$$
$$-10$$
$$-20$$
$$-30$$
$$-30-20-10010203040$$
$$Figure 54.11: Running (SVM_{s2'}) on two sets of 30 points; \nu  = 0.37.$$
$$30$$
$$20$$
$$10$$
$$0$$
$$-10$$
$$-20$$
$$-30$$
$$-30-20-10010203040$$
$$Figure 54.13: Running (SVM_{s2'}) on two sets of 30 points; \nu  = 0.71.$$
Tiếp theo Hình 54.13 chỉ ra kết quả của chạy bài toán quy hoạch với $\nu  =$ 0.71. Ta có $p_{f} = 21, q_{f} = 21, p_{m} = 22, q_{m} = 23$. một cách thú vị, cho $\nu  =$ 0.7, ta chạy vào suy biến
