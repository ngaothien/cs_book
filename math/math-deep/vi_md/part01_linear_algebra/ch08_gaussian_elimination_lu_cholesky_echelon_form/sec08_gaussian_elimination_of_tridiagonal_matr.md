# Phép khử Gauss (Gaussian elimination) của Ba đường chéo Các ma trận


<!-- PAGE 290 -->

## 8.8 Phép khử Gauss (Gaussian elimination) của Ba đường chéo Các ma trận

Xét ma trận ba đường chéo (tridiagonal matrix)
$$A = \begin{pmatrix} b_{1} & c_{1} \\ a_{2} & b_{2} & c_{2} \\ a_{3} & b_{3} & c_{3} \\ \ddots & \ddots & \ddots \\ a_{n-2} & b_{n-2} & c_{n-2} \\ a_{n-1} & b_{n-1} & c_{n-1} \\ a_{n} & b_{n} \end{pmatrix} .$$
Định nghĩa dãy
$$\delta_{0}  = 1,\delta_{1}  = b_{1},\delta_{k}  = b_{k}\delta_{k-1}  -a_{k}c_{k-1}\delta_{k-2} ,2 \le k \le n.$$

> **Mệnh đề 8.7.** Nếu $A$ là ma trận ba đường chéo (tridiagonal matrix) ở trên, thì $\delta_{k}  =$ det((1: $k, 1$: $k))$ cho $k = 1, \dots  , n$.

*Chứng minh.* Bởi expanding det((1: $k, 1$: $k))$ đối với của nó hàng cuối cùng, mệnh đề suy ra bằng quy nạp theo $k$.

> **Định lý 8.8.** Nếu $A$ là ma trận ba đường chéo (tridiagonal matrix) ở trên và $\delta_{k}  \neq  0$ cho $k = 1, \dots  , n$, thì $A$ có sau đây Nhân tử hóa LU (LU-factorization):
$$A = \begin{pmatrix} 1 \\ \delta_{0} \\ a_{2} & 1 \\ \delta_{1} \\ \delta_{1} \\ a_{3} & 1 \\ \delta_{2} \\ \ddots & \ddots \\ \delta_{n-3} \\ a_{n-1} & 1 \\ \delta_{n-2} \\ \delta_{n-2} \\ a_{n} & 1 \end{pmatrix} \begin{pmatrix} \delta_{1} \\ c_{1} \\ \delta_{0} \\ \delta_{2} \\ c_{2} \\ \delta_{1} \\ \delta_{3} \\ c_{3} \\ \delta_{2} \\ \ddots & \ddots \\ \delta_{n-1} \\ c_{n-1} \\ \delta_{n-2} \\ \delta_{n} \\ \delta_{n-1} \end{pmatrix} .$$
$$\delta_{n-1}$$

*Chứng minh.* Vì $\delta_{k}  =$ det((1: $k, 1$: $k)) \neq  0$ cho $k = 1, \dots  , n$, theo Định lý 8.5 (và Mệnh đề 8.2), ta biết rằng $A$ có duy nhất Nhân tử hóa LU (LU-factorization). Vì vậy, nó suffices để kiểm tra rằng proposed nhân tử hóa hoạt động. Ta dễ dàng kiểm tra rằng
$$(LU)_{k k+1}=c_{k},1 \le k \le n -1$$
$$(LU)_{k k-1}=a_{k},2 \le k \le n$$
$$(LU)_{k l}=0,|k -l| \ge 2$$
$$(LU)_{1 1}= \frac{\delta_{1}}{\delta_{0}} = b_{1}$$
$$(LU)_{k k}= \frac{a_{k}c_{k-1}\delta_{k-2}  + \delta_{k}}{\delta_{k-1}} = b_{k},2 \le k \le n,$$

<!-- PAGE 291 -->
Vì $\delta_{k}  = b_{k}\delta_{k-1}$ - $a_{k}c_{k-1}\delta_{k-2}$. Suy ra rằng có một đơn giản phương pháp để giải hệ phương trình tuyến tính Ax $= d$ ở đâu $A$ là ba đường chéo (và $\delta_{k}  \neq  0$ cho $k = 1, \dots  , n)$. Cho điều này, nó là thuận tiện đến “squeeze” ma trận đường chéo (diagonal matrix) $\Delta$ được định nghĩa sao cho $\Delta_{k k}  = \delta_{k} /\delta_{k-1}$ vào nhân tử hóa sao cho $A = (L\Delta )(\Delta^{-1} U)$, và nếu ta cho
$$z_{1} = \frac{c_{1}}{b_{1}} ,z_{k} = c_{k} \frac{\delta_{k-1}}{\delta_{k}} ,2 \le k \le n -1,z_{n} = \frac{\delta_{n}}{\delta_{n-1}} = b_{n} -a_{n}z_{n-1},$$
$A = (L\Delta )(\Delta^{-1} U)$ được viết như
$$A = \begin{pmatrix} c_{1} \\ z_{1} & c_{2} \\ a_{2} \\ z_{2} & c_{3} \\ a_{3} \\ z_{3} \\ \ddots & \ddots \\ c_{n-1} \\ a_{n-1} \\ z_{n-1} \\ a_{n} & z_{n} \end{pmatrix} \begin{pmatrix} 1 & z_{1} \\ 1 & z_{2} \\ 1 & z_{3} \\ \ddots & \ddots \\ 1 & z_{n-2} \\ 1 & z_{n-1} \\ 1 \end{pmatrix} .$$
Hệ quả là, hệ Ax $= d$ có thể được được giải bởi xây dựng ba các dãy: Thứ nhất, dãy
$$z_{1} = \frac{c_{1}}{b_{1}} ,z_{k} = \frac{c_{k}}{b_{k} -a_{k}z_{k-1}} ,k = 2, \dots  , n -1,z_{n} = b_{n} -a_{n}z_{n-1},$$
Tương ứng với recurrence $\delta_{k}  = b_{k}\delta_{k-1}$ - $a_{k}c_{k-1}\delta_{k-2}$ và thu được bằng cách chia cả hai vế của phương trình này bởi $\delta_{k-1}$, tiếp theo
$$w_{1} = \frac{d_{1}}{b_{1}} ,w_{k} = \frac{d_{k}a_{k}w_{k-1}}{b_{k} -a_{k}z_{k-1}} -,k = 2, \dots  , n,$$
Tương ứng với việc giải hệ $L\Delta w = d$, và cuối cùng
$$x_{n} = w_{n},x_{k} = w_{k} -z_{k}x_{k+1},k = n -1, n -2, \dots  , 1,$$
Tương ứng với việc giải hệ $\Delta^{-1}$ Ux $= w$.
Nhận xét: Nó có thể được được kiểm chứng rằng điều này đòi hỏi 3(n - $1)$ các phép cộng, 3(n - $1)$ các phép nhân, và 2n các phép chia, tổng của 8n-6 các phép toán, mà là nhiều ít hơn rằng $O(2n^{3}/3)$ cần thiết bởi Phép khử Gauss (Gaussian elimination) nói chung. Ta bây giờ xét đặc biệt trường hợp của đối xứng xác định dương (SPD) các ma trận $(SPD$ các ma trận).
