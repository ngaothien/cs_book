# Lề mềm (soft margin) SVM; (SVMs5)


<!-- PAGE 2047 -->
$$30$$
$$20$$
$$10$$
$$0$$
$$-10$$
$$-20$$
$$-30$$
$$-30-20-10010203040$$
$$Figure 54.22: Running (SVM_{s4}) on two sets of 30 points; K = 190.$$
Của ta thứ hai chạy đã được tạo với $K = 1/12000$; xem Hình 54.23. Ta có $p_{m} = 30$ và $q_{m} = 30$ và ta xem rằng chiều rộng của dải phẳng (slab) là bit excessive. ví dụ này demonstrates rằng lề (margin) các đường thẳng cần không chứa dữ liệu các điểm.

## 54.15 Lề mềm (soft margin) SVM; (SVM)

$$s5$$
Trong mục này ta xét phiên bản của Bài toán $(SVM_{s4})$ trong mà ta cộng số hạng $(1/2)b^{2}$ đến hàm mục tiêu (objective function). Ta cũng bỏ ràng buộc $\eta  \ge 0$ mà là redundant. Lề mềm (soft margin) SVM $(SVM_{s5})$:
$$+ ($$
$$minimize \frac{1}{2} w^{\top}w + \frac{1}{2} b^{2}p + q)K_{s} \begin{pmatrix} 1 \\ -\nu \eta  + & (\epsilon^{\top} \epsilon  + \xi^{\top} \xi ) \\ p + q \end{pmatrix}$$
$$subject to$$
$$w^{\top}u_{i} -b \ge \eta  -\epsilon_{i} ,i = 1, \dots  , p$$
$$-w^{\top}v_{j} + b \ge \eta  -\xi_{j} ,j = 1, \dots  , q,$$
Ở đâu $\nu$ và $K_{s}$ là hai cho trước dương các hằng số. Như ta đã thấy trước đó, nó là thuận tiện đến chọn $K_{s} = 1/(p + q)$. Khi viết máy tính bài toán quy hoạch, nó được ưu tiên hơn giả sử rằng $K_{s}$ là tùy ý. Trong điều này trường hợp $\nu$ phải được thay thế bởi $(p + q)K_{s}\nu$ trong tất cả các công thức. Một của advantages của các phương pháp này là rằng $\epsilon$ được xác định bởi $\lambda , \xi$ được xác định bởi $\mu$ (như trong $(SVM_{s4}))$, và cả hai $\eta$ và $b$ được xác định bởi $\lambda$ và $\mu$. Như trước đó phương pháp, điều này

<!-- PAGE 2048 -->
$$30$$
$$20$$
$$10$$
$$0$$
$$-10$$
$$-20$$
$$-30$$
$$-30-20-10010203040$$
$$Figure 54.23: Running (SVM_{s4}) on two sets of 30 points; K = 1/12000.$$
Phương pháp thực hiện không đòi hỏi hỗ trợ/giá (support) các vectơ để tính $b$. Ta có thể bỏ qua ràng buộc $\eta  \ge 0$, bởi vì cho nghiệm tối ưu (optimal solution) nó có thể được được hiển thị bằng cách sử dụng đối ngẫu rằng $\eta  \ge 0$. drawback của Bài toán quy hoạch $(SVM_{s5})$ là rằng cho cố định $K_{s}$, đại lượng $\delta  = \eta / \|w\|$ và các siêu phẳng $H_{w,b}, H_{w,b+\eta}$ và $H_{w,b-\eta}$ là độc lập của $\nu$. Điều này sẽ được hiển thị trong Định lý 54.9. Do đó phương pháp này là ít hơn flexible hơn $(SVM_{s2'})$ và $(SVM_{s3})$. Hàm Lagrange (Lagrangian) được cho bởi
$$-$$
$$L(w, \epsilon , \xi , b, \eta , \lambda , \mu ) = \frac{1}{2} w^{\top}w + \frac{1}{2} b^{2}\nu \eta  + K_{s}(\epsilon^{\top} \epsilon  + \xi^{\top} \xi ) + w^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$\epsilon^{\top} \lambda  -\xi^{\top} \mu  + b(1_{p}^{\top} \lambda  -1_{q}^{\top} \mu ) + \eta (1_{p}^{\top} \lambda  + 1_{q}^{\top} \mu )$$
$$= \frac{-1}{2} w^{\top}w + w^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + \eta (1_{p}^{\top} \lambda  + 1_{q}^{\top} \mu  -\nu )$$
$$+ K_{s}(\epsilon^{\top} \epsilon  + \xi^{\top} \xi ) -\epsilon^{\top} \lambda  -\xi^{\top} \mu  + b(1_{p}^{\top} \lambda  -1_{q}^{\top} \mu ) + \frac{1}{2} b^{2}.$$
Để tìm đối ngẫu (dual) hàm $G(\lambda , \mu$) ta cực tiểu hóa L(w, $\epsilon , \xi , b, \eta , \lambda , \mu$) đối với $w, \epsilon , \xi , b$, và $\eta$. Vì Hàm Lagrange (Lagrangian) là lồi và $(w, \epsilon , \xi , b, \eta$) $\in \mathbb{R}^{n}\times \mathbb{R}^{p}\times \mathbb{R}^{q}\times \mathbb{R}\times \mathbb{R}$, lồi tập mở (open set), theo Định lý 40.13, Hàm Lagrange (Lagrangian) có cực tiểu trong $(w, \epsilon , \xi , b, \eta$) khi và chỉ khi $\nabla L_{w,\epsilon ,\xi ,b,\eta} = 0$, do đó

<!-- PAGE 2049 -->
Ta tính $\nabla L_{w,\epsilon ,\xi ,b,\eta}$. gradien $\nabla L_{w,\epsilon ,\xi ,b,\eta}$ được cho bởi
$$\begin{pmatrix}\end{pmatrix}$$
$$\nabla L_{w,\epsilon ,\xi ,b,\eta} = \begin{pmatrix} \lambda  \\ w + X & \mu \\ 2K_{s}\epsilon  -\lambda \\ 2K_{s}\xi  -\mu \\ b + 1_{p}^{\top}\lambda  -1_{q}^{\top}\mu \\ 1_{p}^{\top}\lambda  + 1_{q}^{\top}\mu & \nu \end{pmatrix} .$$
$$-$$
Bằng cách đặt $\nabla L_{w,\epsilon ,\xi ,b,\eta} = 0$ ta thu được các phương trình
$$w = -X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} ,(*_{w})$$
$$2K_{s}\epsilon  = \lambda$$
$$2K_{s}\xi  = \mu$$
$$b = -(1_{p}^{\top} \lambda  -1_{q}^{\top} \mu )$$
$$1_{p}^{\top} \lambda  + 1_{q}^{\top} \mu  = \nu .$$
Như ta được nói trước đó, cả hai $w$ $b$ được xác định bởi $\lambda$ và $\mu$. Ta có thể sử dụng các phương trình để thu được sau đây biểu thức cho đối ngẫu (dual) hàm $G(\lambda , \mu , \gamma$),
$$G(\lambda , \mu , \gamma ) = - \frac{1}{4K_{s}} (\lambda^{\top} \lambda  + \mu^{\top} \mu ) - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} - \frac{b^{2}}{2}$$
$$= - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ X^{\top}X+ & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \\ isequivalenttotheminimization \end{pmatrix} \begin{pmatrix} 1 \\ + & I_{p+q} \\ 2K_{s} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} .$$
Hệ quả là đối ngẫu (dual) bài toán quy hoạch bài toán quy hoạch Đối ngẫu (dual) của Lề mềm (soft margin) SVM $(SVM_{s5})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ X^{\top}X+ & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} \begin{pmatrix} 1 \\ + & I_{p+q} \\ 2K_{s} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = \nu$$
$$\lambda_{i}  \ge 0,i = 1, \dots  , p$$
$$\mu_{j}  \ge 0,j = 1, \dots  , q.$$
Nó được hiển thị trong Mục 54.16 cách mà đối ngẫu (dual) bài toán quy hoạch được giải bằng cách sử dụng ADMM từ Mục 52.6. Nếu bài toán gốc (primal problem) là giải được, điều này cho ta các nghiệm cho $\lambda$ và $\mu$. ràng buộc
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = \nu$$

<!-- PAGE 2050 -->
Suy ra rằng hoặc tồn tại một $i_{0}$ sao cho $\lambda_{i0}  > 0$ hoặc tồn tại một $j_{0}$ sao cho $\mu_{j0}  > 0$, do đó ta có $\epsilon_{i0}  > 0$ hoặc $\xi_{j0}  > 0$, mà có nghĩa là ít nhất một điểm là misclassified. Do đó Bài toán $(SVM_{s5})$ nên chỉ được sử dụng khi các tập hợp ${u_{i}}$ và ${v_{j}}$ là không một cách tuyến tính khả ly. Ta có thể sử dụng sự kiện rằng khoảng cách đối ngẫu (duality gap) là $0$ để tìm $\eta$. Ta có
$$\frac{1}{2} w^{\top}w + \frac{b^{2}}{2} -\nu \eta  + K_{s}(\epsilon^{\top} \epsilon  + \xi^{\top} \xi )$$
$$= - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ X^{\top}X+ & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} \begin{pmatrix} 1 \\ + & I_{p+q} \\ 2K_{s} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} ,$$
Do đó ta thu được
$$\nu \eta  = K_{s}(\epsilon^{\top} \epsilon  + \xi^{\top} \xi ) + \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ X^{\top}X+ & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \\  \end{pmatrix} \begin{pmatrix} 1 \\ + & I_{p+q} \\ 4K_{s} \\  \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$= \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ X^{\top}X+ & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} \begin{pmatrix} 1 \\ + & I_{p+q} \\ 2K_{s} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} .$$
Ở trên xác nhận rằng tại tính tối ưu ta có $\eta  \ge 0$.
Nhận xét: Nếu ta thực hiện không giả sử rằng $K_{s} = 1/(p+q)$, thì ở trên công thức phải được thay thế bởi
$$(p + q)K_{s}\nu \eta  = \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ X^{\top}X+ & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \\ 54.8statingthatforafixed \end{pmatrix} \begin{pmatrix} 1 \\ + & I_{p+q} \\ 2K_{s} \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix} .$$
Có một phiên bản của Định lý $K_{s}$, nghiệm đến Bài toán $(SVM_{s5})$ là duy nhất và độc lập của giá trị của $\nu$.

> **Định lý 54.9.** Cho $K_{s}$ và $\nu$ cố định, nếu Bài toán $(SVM_{s5})$ thành công thì nó có duy nhất nghiệm. Nếu Bài toán $(SVM_{s5})$ thành công và trả về $(\lambda , \mu , \eta , w, b)$ cho giá trị $\nu$ và $(\lambda^{\kappa} , \mu^{\kappa} , \eta^{\kappa} , w^{\kappa}, b^{\kappa})$ cho giá trị $\kappa \nu$ với $\kappa  > 0$, thì
$$\lambda^{\kappa} = \kappa \lambda , \mu^{\kappa} = \kappa \mu , \eta^{\kappa} = \kappa \eta , w^{\kappa}= \kappa w, b^{\kappa}= \kappa b.$$
Hệ quả là, $\delta  = \eta / \|w\| = \eta^{\kappa} / \|w^{\kappa}\| = \delta^{\kappa}$, và các siêu phẳng $H_{w,b}, H_{w,b+\eta}$ và $H_{w,b-\eta}$ là độc lập của $\nu$.

*Chứng minh.* chứng minh là dễ sự điều chỉnh của chứng minh của Định lý 54.8 do đó ta chỉ cho phác thảo. hai then chốt các điểm là rằng ma trận
$$P = X^{\top}X + \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} + \frac{1}{2K_{s}} I_{p+q}$$
Là đối xứng xác định dương (SPD) và rằng ta có đơn lẻ equational ràng buộc
$$1_{p}^{\top} \lambda  + 1_{q}^{\top} \mu  = (p + q)K_{s}\nu$$
