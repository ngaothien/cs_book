# Việc giải SVM (SVMs2) Bằng cách sử dụng ADMM


<!-- PAGE 1993 -->
Đối ngẫu (dual) của Lề mềm (soft margin) hạt nhân (kernel) SVM $(SVM_{s2})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} K \begin{pmatrix} \lambda \\ \mu \end{pmatrix} - \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} 1_{p+q}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$0 \le \lambda_{i}  \le K,i = 1, \dots  , p$$
$$0 \le \mu_{j}  \le K,j = 1, \dots  , q,$$
Ở đâu $K$ là $\ell \times  \ell$ hạt nhân (kernel) ma trận đối xứng (symmetric matrix) (với $\ell = p + q)$ cho trước tại kết thúc/cuối của Mục 54.1. Ta cũng tìm rằng
$$w = \sum_{i=1}^{p}  \lambda_{i} \phi (u_{i}) - \sum_{j=1}^{q}  \mu_{j} \phi (v_{j}),$$
Do đó
$$b = \frac{1}{2} \begin{pmatrix} \lambda_{i} (\kappa (u_{i}, u_{i0}) + \kappa (u_{i}, v_{j0})) - & \mu_{j} (\kappa (v_{j}, u_{i0}) + \kappa (v_{j}, v_{j0})) \end{pmatrix} \sum_{i=1}^{p}  \sum_{j=1}^{q}  ,$$
Và phân loại hàm
$$f(x) = sgn(\langle w, \phi (x)\rangle -b)$$
Được cho bởi
$$$$
$$f(x) = sgn \sum_{i=1}^{p}  \lambda_{i} (2\kappa (u_{i}, x) -\kappa (u_{i}, u_{i0}) -\kappa (u_{i}, v_{j0}))$$
$$$$
$$- \sum_{j=1}^{q}  \mu_{j} (2\kappa (v_{j}, x) -\kappa (v_{j}, u_{i0}) -\kappa (v_{j}, v_{j0})).$$

## 54.4 Việc giải SVM (SVM) Bằng cách sử dụng ADMM

$$s2$$
Trong thứ tự để giải $(SVM_{s2})$ bằng cách sử dụng ADMM ta cần đến viết ma trận tương ứng với các ràng buộc trong equational tạo thành,
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\lambda_{i}  + \alpha_{i}  = K,i = 1, \dots  , p$$
$$\mu_{j}  + \beta_{j}  = K,j = 1, \dots  , q.$$
