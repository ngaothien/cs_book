# Các bài tập


<!-- PAGE 2066 -->
Điều này time ta thu được $w, b, \eta , \epsilon$ và $\xi$ từ $\lambda$ và $\mu$:
$$w = \sum_{i=1}^{p}  \lambda_{i} u_{i} - \sum_{j=1}^{q}  \mu_{j} v_{j}$$
$$b = - \sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}$$
$$\epsilon  = \frac{\lambda}{2\mu K}$$
$$\xi  =K ,$$
$$2$$
Và
$$(p + q)K_{s}\nu \eta  = \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ X^{\top}X+ & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} \begin{pmatrix} 1 \\ + & I_{p+q} \\ 2K_{s} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} .$$
Ràng buộc
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = \nu$$
Suy ra rằng hoặc tồn tại một $i_{0}$ sao cho $\lambda_{i0}  > 0$ hoặc tồn tại một $j_{0}$ sao cho $\mu_{j0}  > 0$, ta có $\epsilon_{i0}  > 0$ hoặc $\xi_{j0}  > 0$, mà có nghĩa là ít nhất một điểm là misclassified, do đó Bài toán $(SVM_{s5})$ nên chỉ được sử dụng khi các tập hợp ${u_{i}}$ và ${v_{j}}$ là không một cách tuyến tính khả ly. các phương pháp này tất cả có kernelized phiên bản. Ta được cài đặt tất cả các phương pháp này trong Matlab, việc giải đối ngẫu (dual) bằng cách sử dụng ADMM. Từ lý thuyết điểm của quan điểm, Các bài tập $(SVM_{s4})$ và $(SVM_{s5})$ dường như đến có nhiều hơn/thêm advantages hơn những cái khác vì chúng xác định $w, b, \eta$ và $b$ mà không có đòi hỏi bất kỳ điều kiện về hỗ trợ/giá (support) các vectơ của loại/kiểu $1$. Tuy nhiên, từ thực tế điểm của quan điểm, Các bài tập $(SVM_{s4})$ và $(SVM_{s5})$ là ít hơn flexible rằng $(SVM_{s2'})$ và $(SVM_{s3})$, và ta có được quan sát rằng $(SVM_{s4})$ và $(SVM_{s5})$ là unable đến produce như nhỏ lề (margin) $\delta$ như $(SVM_{s2'})$ và $(SVM_{s3})$.

## 54.18 Các bài tập

Bài toán 54.1. Chứng minh sau đây bất đẳng thức
$$ $$
$$\max \frac{1}{2p_{m}} , \frac{1}{2q_{m}} \le K \le \min \frac{1}{2p_{f}} , \frac{1}{2q_{f}}$$
Được phát biểu chỉ sau Định nghĩa 54.1.

<!-- PAGE 2067 -->
Bài toán 54.2. Chứng minh lấy trung bình các công thức
$$ \sum_{\in I\lambda}  \sum_{\in I\mu}  $$
$$b = w^{\top}/|I_{\lambda}| +/|I_{\mu}|/2$$
$$ \begin{pmatrix} u_{i} \\ i \end{pmatrix} \begin{pmatrix} v_{j} \\ j \end{pmatrix} $$
$$ \sum_{i\in I\lambda}  \sum_{j\in I\mu}  $$
$$\delta  = w^{\top}/|I_{\lambda}| -/|I_{\mu}|/2$$
$$ \begin{pmatrix} u_{i} \end{pmatrix} \begin{pmatrix} v_{j} \end{pmatrix} $$
Được phát biểu tại kết thúc/cuối của Mục 54.1.
Bài toán 54.3. Chứng minh rằng ma trận
$$A = \begin{pmatrix} 1_{p}^{\top} & -1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} \\ 1_{p}^{\top} & 1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} \\ I_{p} & 0_{p,q} & I_{p} & 0_{p,q} \\ 0_{q,p} & I_{q} & 0_{q,p} & I_{q} \end{pmatrix}$$
Có hạng (rank) $p + q + 2$.
Bài toán 54.4. Chứng minh rằng đối ngẫu (dual) bài toán quy hoạch của hạt nhân (kernel) phiên bản của $(SVM_{s1})$ được cho bởi: Đối ngẫu (dual) của Lề mềm (soft margin) hạt nhân (kernel) SVM $(SVM_{s1})$:
$$minimize \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} K \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  = \sum_{j=1}^{q}  \mu_{j}  = \frac{1}{2}$$
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
Bài toán 54.5. Chứng minh lấy trung bình công thức
$$\sum_{\in I\lambda}  \sum_{\in I\mu}  $$
$$b = w^{\top} \begin{pmatrix}  \\ u_{i} \\ i \end{pmatrix} \begin{pmatrix}  \\ /|I_{\lambda}| + & v_{j} \\ j \end{pmatrix} /|I_{\mu}|/2$$
Được phát biểu trong Mục 54.3.

<!-- PAGE 2068 -->
Bài toán 54.6. Chứng minh rằng hạt nhân (kernel) phiên bản của Bài toán quy hoạch $(SVM_{s2})$ được cho bởi: Đối ngẫu (dual) của Lề mềm (soft margin) hạt nhân (kernel) SVM $(SVM_{s2})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} K \begin{pmatrix} \lambda \\ \mu \end{pmatrix} - \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$0 \le \lambda_{i}  \le K,i = 1, \dots  , p$$
$$0 \le \mu_{j}  \le K,j = 1, \dots  , q,$$
Ở đâu $K$ là $\ell \times  \ell$ hạt nhân (kernel) ma trận đối xứng (symmetric matrix) (với $\ell = p + q)$ cho trước tại kết thúc/cuối của Mục 54.1.
Bài toán 54.7. Chứng minh rằng ma trận
$$A = \begin{pmatrix} 1_{p}^{\top} & -1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} \\ I_{p} & 0_{p,q} & I_{p} & 0_{p,q} \\ 0_{q,p} & I_{q} & 0_{q,p} & I_{q} \end{pmatrix}$$
Có hạng (rank) $p + q + 1$.
Bài toán 54.8. Chứng minh rằng các ma trận
$$A = \begin{pmatrix} 1_{p}^{\top} & -1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} & 0 \\ 1_{p}^{\top} & 1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} & -1 \\ I_{p} & 0_{p,q} & I_{p} & 0_{p,q} & 0_{p} \\ 0_{q,p} & I_{q} & 0_{q,p} & I_{q} & 0_{q} \end{pmatrix} andA_{2} = \begin{pmatrix} 1_{p}^{\top} & -1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} \\ 1_{p}^{\top} & 1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} \\ I_{p} & 0_{p,q} & I_{p} & 0_{p,q} \\ 0_{q,p} & I_{q} & 0_{q,p} & I_{q} \end{pmatrix}$$
Có hạng (rank) $p + q + 2$.
Bài toán 54.9. Chứng minh rằng hạt nhân (kernel) phiên bản của Bài toán quy hoạch $(SVM_{s2'})$ được cho bởi:

<!-- PAGE 2069 -->
Đối ngẫu (dual) của Lề mềm (soft margin) hạt nhân (kernel) SVM $(SVM_{s2'})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} K \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  \ge K_{m}$$
$$0 \le \lambda_{i}  \le K_{s},i = 1, \dots  , p$$
$$0 \le \mu_{j}  \le K_{s},j = 1, \dots  , q,$$
Ở đâu $K$ là hạt nhân (kernel) ma trận của Mục 54.1.
Bài toán 54.10. Chứng minh các công thức xác định $b$ theo $\eta$ được phát biểu chỉ trước Định lý 54.8.
Bài toán 54.11. Chứng minh rằng ma trận
$$A = \begin{pmatrix} 1_{p}^{\top} & 1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} \\ I_{p} & 0_{p,q} & I_{p} & 0_{p,q} \\ 0_{q,p} & I_{q} & 0_{q,p} & I_{q} \end{pmatrix}$$
Có hạng (rank) $p + q + 1$.
Bài toán 54.12. Chứng minh rằng hạt nhân (kernel) phiên bản của Bài toán quy hoạch $(SVM_{s3})$ được cho bởi: Đối ngẫu (dual) của Lề mềm (soft margin) hạt nhân (kernel) SVM $(SVM_{s3})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ K + & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = \nu$$
$$0 \le \lambda_{i}  \le K_{s},i = 1, \dots  , p$$
$$0 \le \mu_{j}  \le K_{s},j = 1, \dots  , q,$$
Ở đâu $K$ là hạt nhân (kernel) ma trận của Mục 54.1.
Bài toán 54.13. Chứng minh rằng các ma trận
$$1_{p}^{\top}-1_{q}^{\top}0!1_{p}^{\top}-1_{q}^{\top}!$$
$$A =andA_{2} =$$
$$1_{p}^{\top}1_{q}^{\top}-11_{p}^{\top}1_{q}^{\top}$$
Có hạng (rank) $2$.

<!-- PAGE 2070 -->
Bài toán 54.14. Cài đặt Bài toán quy hoạch $(SVM_{s4})$ trong Matlab. Bạn có thể thích nghi các bài toán quy hoạch cho trước trong Mục B.2 và Mục B.3.
Bài toán 54.15. Chứng minh rằng hạt nhân (kernel) phiên bản của Bài toán quy hoạch $(SVM_{s4})$ được cho bởi: Đối ngẫu (dual) của Lề mềm (soft margin) hạt nhân (kernel) SVM $(SVM_{s4})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$\begin{pmatrix} p + q \\ K + & I_{p+q} \\ 2 \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  \ge \nu$$
$$\lambda_{i}  \ge 0,i = 1, \dots  , p$$
$$\mu_{j}  \ge 0,j = 1, \dots  , q,$$
Ở đâu $K$ là hạt nhân (kernel) ma trận của Mục 54.1.
Bài toán 54.16. Cài đặt Bài toán quy hoạch $(SVM_{s5})$ trong Matlab. Bạn có thể thích nghi các bài toán quy hoạch cho trước trong Mục B.2 và Mục B.3.
Bài toán 54.17. Chứng minh rằng hạt nhân (kernel) phiên bản của Bài toán quy hoạch $(SVM_{s5})$ được cho bởi: Đối ngẫu (dual) của Lề mềm (soft margin) hạt nhân (kernel) SVM $(SVM_{s5})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ K + & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} \begin{pmatrix} p + q \\ + & I_{p+q} \\ 2 \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = \nu$$
$$\lambda_{i}  \ge 0,i = 1, \dots  , p$$
$$\mu_{j}  \ge 0,j = 1, \dots  , q,$$
Ở đâu $K$ là hạt nhân (kernel) ma trận của Mục 54.1.
