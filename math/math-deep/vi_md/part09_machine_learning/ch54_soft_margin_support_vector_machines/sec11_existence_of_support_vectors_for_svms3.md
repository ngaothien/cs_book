# Sự tồn tại của Hỗ trợ/giá (support) Các vectơ cho (SVMs3)


<!-- PAGE 2031 -->
Lưu ý rằng nếu $\nu$ được chọn sao cho $\nu  < 1/(p + q)$, thì $p_{f} = q_{f} = 0$, mà có nghĩa là không có cái nào của dữ liệu các điểm là misclassified; nói cách khác, $u_{i}s$ và $v_{j}s$ là một cách tuyến tính khả ly. Do đó ta xem rằng nếu $u_{i}s$ và $v_{j}s$ là không một cách tuyến tính khả ly ta phải chọn $\nu$ sao cho $1/(p + q) \le \nu  \le 1$ cho phương pháp đến succeed. Thực ra, theo Mệnh đề 54.5, ta phải chọn $\nu$ sao cho
$$\frac{p_{f}+ q_{f}}{p + q} \le \nu  \le \frac{p_{m} + q_{m}}{p + q} .$$
Hơn nữa, trong thứ tự là able để xác định $b$, ta phải có chặt bất đẳng thức
$$\frac{p_{f}+ q_{f}}{p + q} < \nu .$$

## 54.11 Sự tồn tại của Hỗ trợ/giá (support) Các vectơ cho (SVM)

$$s3$$
Sau đây mệnh đề là phiên bản của Mệnh đề 54.2 cho Bài toán $(SVM_{s3})$.

> **Mệnh đề 54.6.** Với mọi nghiệm tối ưu (optimal solution) $(w, b, \eta , \epsilon , \xi$) của Bài toán $(SVM_{s3})$ với $w \neq  0$ và $\eta  > 0$, nếu $\nu  < 1$ và nếu không có $u_{i}$ là hỗ trợ/giá (support) vectơ và không có $v_{j}$ là hỗ trợ/giá (support) vectơ, thì ở đó là một cái khác nghiệm tối ưu (optimal solution) sao cho một số $u_{i0}$ hoặc một số $v_{j0}$ là hỗ trợ/giá (support) vectơ.

*Chứng minh.* Ta có thể giả sử rằng $K_{s} = 1/(p + q)$ và ta tiến hành bởi mâu thuẫn. Do đó ta giả sử rằng với mọi $i \in {1, \dots  , p}$, nếu $\epsilon_{i}  = 0$, thì ràng buộc $w^{\top}u_{i}$ - $b \ge \eta$ là không hoạt động, cụ thể là $w^{\top}u_{i} -b > \eta$, và với mọi $j \in {1, \dots  , q}$, nếu $\xi_{j}  = 0$, thì ràng buộc $-w^{\top}v_{j} +b \ge \eta$ là không hoạt động, cụ thể là $-w^{\top}v_{j} + b > \eta$. Cho $E_{\lambda} = {i \in {1, \dots  , p}$ | $\epsilon_{i}  > 0}$ và cho $E_{\mu} = {j \in {1, \dots  , q}$ | $\xi_{j}  > 0}$. Theo Định nghĩa, $p_{sf} = |E_{\lambda}|, q_{sf} = |E_{\mu}|, p_{sf} \le p_{f}$ và $q_{sf} \le q_{f}$, do đó theo Mệnh đề 54.1,
$$\frac{p_{sf}+ q_{sf}}{p + q} \le \frac{p_{f}+ q_{f}}{p + q} \le \nu .$$
Vì vậy, nếu $\nu  < 1$, thì $p_{sf} + q_{sf} < p + q$, mà suy ra rằng hoặc tồn tại một $i \in / E_{\lambda}$ sao cho $\epsilon_{i}  = 0$ hoặc tồn tại một $j \in / E_{\mu}$ sao cho $\xi_{j}  = 0$. Bởi độ bù lỏng (complementary slackness) tất cả các ràng buộc cho mà $i \in E_{\lambda}$ và $j \in E_{\mu}$ là hoạt động, do đó của ta các giả thiết là
$$w^{\top}u_{i} -b = \eta  -\epsilon_{i} \epsilon_{i}  > 0i \in E_{\lambda}$$
$$-w^{\top}v_{j} + b = \eta  -\xi_{j} \xi_{j}  > 0j \in E_{\mu}$$
$$w^{\top}u_{i} -b > \eta i \in /E_{\lambda}$$
$$-w^{\top}v_{j} + b > \eta j \in /E_{\mu},$$
Và hoặc tồn tại một $i \in / E_{\lambda}$ hoặc tồn tại một $j \in / E_{\mu}$. Của ta chiến lược, như được minh họa trong Các hình 54.8 và 54.9, là đến tăng chiều rộng $\eta$ của dải phẳng (slab) giữ tách siêu phẳng (hyperplane) unchanged. Cho chúng ta chọn $\theta$ sao cho
$$\theta  = \min{w^{\top}u_{i} -b -\eta , -w^{\top}v_{j} + b -\eta  | i \in /E_{\lambda}, j \in /E_{\mu}}.$$

<!-- PAGE 2032 -->
Của ta các giả thiết suy ra rằng $\theta  > 0$. Ta có thể viết
$$w^{\top}u_{i} -b = \eta  + \theta  -(\epsilon_{i}  + \theta )\epsilon_{i}  + \theta  > 0i \in E_{\lambda}$$
$$-w^{\top}v_{j} + b = \eta  + \theta  -(\xi_{j}  + \theta )\xi_{j}  + \theta  > 0j \in E_{\mu}$$
$$w^{\top}u_{i} -b \ge \eta  + \theta i \in /E_{\lambda}$$
$$-w^{\top}v_{j} + b \ge \eta  + \theta j \in /E_{\mu},$$
Và bởi lựa chọn của $\theta$, hoặc
$$w^{\top}u_{i} -b = \eta  + \theta for some i \in /E_{\lambda}$$
Hoặc
$$-w^{\top}v_{j} + b = \eta  + \theta for some j \in /E_{\mu}.$$
Ban đầu giá trị của hàm mục tiêu (objective function) là
$$\omega (0) = \frac{1}{2} w^{\top}w + \frac{1}{2} b^{2} -\nu \eta  + \frac{1}{p + q} \sum_{i\in E\lambda}  \sum_{j\in E\mu}  ,$$
$$\begin{pmatrix} \epsilon_{i}  + & \xi_{j} \end{pmatrix}$$
Và mới giá trị là
$$\omega (\theta ) = \frac{1}{2} w^{\top}w + \frac{1}{2} b^{2} -\nu (\eta  + \theta ) + \frac{1}{p + q} \sum_{i\in E\lambda}  \sum_{j\in E\mu}$$
$$\begin{pmatrix} (\epsilon_{i}  + \theta ) + & (\xi_{j} + \theta ) \\  & p_{sf}+ \end{pmatrix}$$
$$= \frac{1}{2} w^{\top}w + \frac{1}{2} b^{2} -\nu \eta  + \frac{1}{p + q} \sum_{i\in E\lambda}  \sum_{j\in E\mu}  - \begin{pmatrix} q_{sf} \\ \nu  - \\ p + q \end{pmatrix} \theta .$$
$$\begin{pmatrix} \epsilon_{i}  + & \xi_{j} \end{pmatrix}$$
Theo Mệnh đề 54.1,
$$\frac{p_{sf}+ q_{sf}}{p + q} \le \frac{p_{f}+ q_{f}}{p + q} \le \nu ,$$
Do đó
$$\nu  - \frac{p_{sf}+ q_{sf}}{p + q} \ge 0,$$
Và do đó $\omega (\theta$) $\le \omega (0)$. Nếu bất đẳng thức là chặt, thì điều này contradicts tính tối ưu của ban đầu nghiệm. Vì vậy, $\omega (\theta$) $= \omega (0)$ và $(w, b, \eta  + \theta , \epsilon  + \theta , \xi  + \theta$) là nghiệm tối ưu (optimal solution) sao cho hoặc
$$w^{\top}u_{i} -b = \eta  + \theta for some i \in /E_{\lambda}$$
Hoặc
$$-w^{\top}v_{j} + b = \eta  + \theta for some j \in /E_{\mu},$$
Như mong muốn. Mệnh đề 54.6 không thể là strengthened đến khẳng định rằng tồn tại một hỗ trợ/giá (support) vectơ $u_{i0}$ và một số hỗ trợ/giá (support) vectơ $v_{j0}$. Ta tìm thấy các ví dụ cho mà ở trên điều kiện không thỏa mãn cho $\nu$ lớn đủ. chứng minh của Mệnh đề 54.6 reveals rằng $(p_{sf} + q_{sf})/(p + q)$ là tới hạn/quan trọng giá trị cho $\nu$. nếu giá trị này là tránh được ta có kết quả sau hệ quả.
