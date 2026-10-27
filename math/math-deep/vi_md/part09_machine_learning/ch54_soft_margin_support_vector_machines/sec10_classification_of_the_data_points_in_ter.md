# Phân loại của Dữ liệu Các điểm theo (SVMs3)


<!-- PAGE 2029 -->
Với $K_{s} = 1/(p + q)$. Tracing qua derivation của đối ngẫu (dual) bài toán quy hoạch, ta thu được Đối ngẫu (dual) của Lề mềm (soft margin) hạt nhân (kernel) SVM $(SVM_{s3})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} \begin{pmatrix} 1_{p}1_{p}^{\top} & -1_{p}1_{q}^{\top} \\ K + & -1_{q}1_{p}^{\top} & 1_{q}1_{q}^{\top} \end{pmatrix} \begin{pmatrix}\end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = \nu$$
$$0 \le \lambda_{i}  \le K_{s},i = 1, \dots  , p$$
$$0 \le \mu_{j}  \le K_{s},j = 1, \dots  , q,$$
Ở đâu $K$ là hạt nhân (kernel) ma trận của Mục 54.1. Ta thu được
$$w = \sum_{i=1}^{p}  \lambda_{i} \phi (u_{i}) - \sum_{j=1}^{q}  \mu_{j} \phi (v_{j})$$
$$b = - \sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j} .$$
Phân loại hàm
$$f(x) = sgn(\langle w, \phi (x)\rangle -b)$$
Được cho bởi
$$f(x) = sgn \begin{pmatrix} \lambda_{i} (\kappa (u_{i}, x) + 1) - & \mu_{j} (\kappa (v_{j}, x) + 1) \end{pmatrix} \sum_{i=1}^{p}  \sum_{j=1}^{q}  .$$

## 54.10 Phân loại của Dữ liệu Các điểm theo \nu

$$(SVM)$$
$$s3$$
Các phương trình $(\dagger$) và hình hộp các bất đẳng thức
$$0 \le \lambda_{i}  \le K_{s},0 \le \mu_{j}  \le K_{s}$$
Cũng suy ra sau đây các sự kiện (nhắc lại rằng $\delta  = \eta / \|w\|)$:

> **Mệnh đề 54.5.** Nếu Bài toán $(SVM_{s3})$ có nghiệm tối ưu (optimal solution) với $w \neq  0$ và $\eta  > 0$ thì sau đây các sự kiện đúng:

<!-- PAGE 2030 -->
$(1)$ Cho $p_{f}$ là số của các điểm $u_{i}$ sao cho $\lambda_{i}  = K_{s}$, và cho $q_{f}$ số của các điểm $v_{j}$ sao cho $\mu_{j}  = K_{s}$. Thì $p_{f} + q_{f} \le (p + q)\nu$.
$(2)$ Cho $p_{m}$ là số của các điểm $u_{i}$ sao cho $\lambda_{i}  > 0$, và cho $q_{m}$ số của các điểm $v_{j}$ sao cho $\mu_{j}  > 0$. Thì $p_{m} + q_{m} \ge (p + q)\nu$. Ta có $p_{m} + q_{m} \ge 1$.
$(3)$ Nếu $p_{f} \ge 1$ hoặc $q_{f} \ge 1$, thì $\nu  \ge 1/(p + q)$.

*Chứng minh.* $(1)$ Nhắc lại rằng cho nghiệm tối ưu (optimal solution) với $w \neq  0$ và $\eta  > 0$ ta có phương trình
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = \nu .$$
Vì có $p_{f}$ các điểm $u_{i}$ sao cho $\lambda_{i}  = K_{s} = 1/(p + q)$ và $q_{f}$ các điểm $v_{j}$ sao cho $\mu_{j}  = K_{s} = 1/(p + q)$, ta có
$$\nu  = \sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  \ge \frac{p_{f}+ q_{f}}{p + q} ,$$
Do đó
$$p_{f} + q_{f} \le \nu (p + q).$$
$(2)$ Nếu
$$I_{\lambda >0} = {i \in {1, \dots  , p} | \lambda_{i}  > 0}andp_{m} = |I_{\lambda >0}|$$
Và
$$I_{\mu >0} = {j \in {1, \dots  , q} | \mu_{j}  > 0}andq_{m} = |I_{\mu >0}|,$$
Thì
$$\nu  = \sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  = \sum_{i\in I\lambda >0}  \lambda_{i}  + \sum_{j\in I\mu >0}  \mu_{j} ,$$
Và vì $\lambda_{i} , \mu_{j}  \le K_{s} = 1/(p + q)$, ta có
$$\nu  = \sum_{i\in I\lambda >0}  \lambda_{i}  + \sum_{j\in I\mu >0}  \mu_{j}  \le \frac{p_{m} + q_{m}}{p + q} ,$$
Mà cho ta
$$p_{m} + q_{m} \ge \nu (p + q).$$
Ta đã được lưu ý trước đó rằng $p_{m} + q_{m} \ge 1$.
$(3)$ Điều này suy ra ngay lập tức từ $(1)$.
