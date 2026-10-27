# Việc giải SVM (SVMs3) Bằng cách sử dụng ADMM


<!-- PAGE 2033 -->

> **Định lý 54.7.** Với mọi nghiệm tối ưu (optimal solution) $(w, b, \eta , \epsilon , \xi$) của Bài toán $(SVM_{s3})$ với w̸ $= 0$ và $\eta  > 0$, nếu
$$(p_{sf} + q_{sf})/(p + q) < \nu  < 1,$$
Thì một số $u_{i0}$ hoặc một số $v_{j0}$ là hỗ trợ/giá (support) vectơ. chứng minh tiến hành bởi mâu thuẫn bằng cách sử dụng Mệnh đề 54.6 (cho rất đồng dạng chứng minh, xem chứng minh của Định lý 54.3).

## 54.12 Việc giải SVM (SVM) Bằng cách sử dụng ADMM

$$s3$$
Trong thứ tự để giải $(SVM_{s3})$ bằng cách sử dụng ADMM ta cần đến viết ma trận tương ứng với các ràng buộc trong equational tạo thành,
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = K_{m}$$
$$\lambda_{i}  + \alpha_{i}  = K_{s},i = 1, \dots  , p$$
$$\mu_{j}  + \beta_{j}  = K_{s},j = 1, \dots  , q$$
Với $K_{m} = (p + q)K_{s}\nu$. Điều này là $(p + q + 1) \times$ 2(p $+ q)$ ma trận $A$ cho trước bởi
$$A = \begin{pmatrix} 1_{p}^{\top} & 1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} \\ I_{p} & 0_{p,q} & I_{p} & 0_{p,q} \\ 0_{q,p} & I_{q} & 0_{q,p} & I_{q} \end{pmatrix} .$$
Ta để lại nó như một bài tập để chứng minh rằng $A$ có hạng (rank) $p + q + 1$. vế phải là
$$c = \begin{pmatrix} K_{m} \\ K_{s}1_{p+q} \end{pmatrix} .$$
Đối xứng nửa xác định dương (positive semidefinite) $(p+q)\times (p+q)$ ma trận $P$ định nghĩa toàn phương phiếm hàm là
$$P = X^{\top}X + \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} ,withX = \begin{pmatrix} -u_{1} & \cdots & -u_{p} & v_{1} & \cdots & v_{q} \end{pmatrix} ,$$
Và
$$q = 0_{p+q}.$$
Vì có 2(p $+q)$ Các nhân tử Lagrange (Lagrange multipliers) $(\lambda , \mu , \alpha , \beta$), ma trận cỡ $(p +q)\times (p +q)$ $P$ phải là augmented với không’s để tạo nó 2(p $+ q) \times$ 2(p $+ q)$ ma trận $P_{a}$ cho trước bởi
$$P_{a} = \begin{pmatrix} P & 0_{p+q,p+q} \\ 0_{p+q,p+q} & 0_{p+q,p+q} \end{pmatrix} ,$$

<!-- PAGE 2034 -->
Và tương tự $q$ là augmented với các không điểm như vectơ
$$q_{a} = 0_{2(p+q)}.$$
Matlab các bài toán quy hoạch cài đặt ở trên phương pháp là cho trước trong Phụ lục $B$, Mục B.3. Ta ran của ta bài toán quy hoạch trên cùng input dữ liệu các điểm được sử dụng trong Mục 54.8, cụ thể là u16 $= 10.1*randn(2,30)+7$; v16 $=$ -10.1*randn(2,30)-7; [~,~,~,~,~,~,w3] $= runSVMs3b(0.365,rho,u16,v16,1/60)$ Ta được chọn $K = 1/60$ và khác nhau các giá trị của $\nu$ bắt đầu với $\nu  =$ 0.365, mà xuất hiện là nhỏ nhất giá trị cho mà phương pháp hội tụ; xem Hình 54.16.
$$30$$
$$20$$
$$10$$
$$0$$
$$-10$$
$$-20$$
$$-30$$
$$-30-20-10010203040$$
$$Figure 54.16: Running (SVM_{s3}) on two sets of 30 points; \nu  = 0.365.$$
Ta có $p_{f} = 10, q_{f} = 10, p_{m} = 12$ và $q_{m} = 11$, như opposed đến $p_{f} = 10, q_{f} = 11, p_{m} = 12, q_{m} = 12$, mà đã là thu được bởi chạy $(SVM_{s2'})$; xem Hình 54.11. slightly narrower lề (margin) là đạt được. Tiếp theo ta ran của ta bài toán quy hoạch với $\nu  =$ 0.5, xem Hình 54.17. Ta có $p_{f} = 13, q_{f} = 16, p_{m} = 14$ và $q_{m} = 17$. Ta cũng ran của ta bài toán quy hoạch với $\nu  =$ 0.71, xem Hình 54.18. Ta có $p_{f} = 21, q_{f} = 21, p_{m} = 22$ và $q_{m} = 22$. giá trị $\nu  =$ 0.7 là giá trị kỳ dị (singular value) cho mà có không có hỗ trợ/giá (support) các vectơ và $\nu  = (p_{f} + q_{f})/(p + q)$.

<!-- PAGE 2035 -->
Cuối cùng ta ran của ta bài toán quy hoạch với $\nu  =$ 0.98, xem Hình 54.19. Ta có $p_{f} = 28, q_{f} = 30, p_{m} = 29$ và $q_{m} = 30$. Bởi vì số hạng $(1/2)b^{2}$ được cộng đến hàm mục tiêu (objective function) được cực tiểu hóa, hóa ra là $(SVM_{s3})$ cho ta các giá trị của $b$ và $\eta$ rằng là nhỏ hơn hơn các giá trị được trả về bởi $(SVM_{s2'})$. Điều này là lý do tại sao nhỏ hơn lề (margin) chiều rộng có thể là thu được cho $\nu  =$ 0.365. Mặt khác, $(SVM_{s3})$ là unable đến đạt được như big lề (margin) như $(SVM_{s2'})$ cho các giá trị của $\nu  \ge$ 0.97, bởi vì tách đường thẳng produced bởi $(SVM_{s3})$ là thấp hơn hơn tách đường thẳng produced bởi $(SVM_{s2'})$.
$$30$$
$$20$$
$$10$$
$$0$$
$$-10$$
$$-20$$
$$-30$$
$$-30-20-10010203040$$
$$Figure 54.17: Running (SVM_{s3}) on two sets of 30 points; \nu  = 0.5.$$

<!-- PAGE 2036 -->
$$30$$
$$20$$
$$10$$
$$0$$
$$-10$$
$$-20$$
$$-30$$
$$-30-20-10010203040$$
$$Figure 54.18: Running (SVM_{s3}) on two sets of 30 points; \nu  = 0.71.$$
$$30$$
$$20$$
$$10$$
$$0$$
$$-10$$
$$-20$$
$$-30$$
$$-30-20-10010203040$$
$$Figure 54.19: Running (SVM_{s3}) on two sets of 30 points; \nu  = 0.98.$$
