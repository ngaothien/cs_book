# Lề mềm (soft margin) Các máy vectơ hỗ trợ (SVMs); (SVMs2')


<!-- PAGE 1994 -->
Điều này là $(p + q + 1) \times$ 2(p $+ q)$ ma trận $A$ cho trước bởi
$$A = \begin{pmatrix} 1_{p}^{\top} & -1_{q}^{\top} & 0_{p}^{\top} & 0_{q}^{\top} \\ I_{p} & 0_{p,q} & I_{p} & 0_{p,q} \\ 0_{q,p} & I_{q} & 0_{q,p} & I_{q} \end{pmatrix} .$$
Ta để lại nó như một bài tập để chứng minh rằng $A$ có hạng (rank) $p + q + 1$. vế phải là
$$c = \begin{pmatrix} 0 \\ K1_{p+q} \end{pmatrix} .$$
Đối xứng nửa xác định dương (positive semidefinite) $(p+q)\times (p+q)$ ma trận $P$ định nghĩa toàn phương phiếm hàm là
$$P = X^{\top}X,withX = \begin{pmatrix} -u_{1} & \cdots & -u_{p} & v_{1} & \cdots & v_{q} \end{pmatrix} ,$$
Và
$$q = -1_{p+q}.$$
Vì có 2(p $+ q)$ Các nhân tử Lagrange (Lagrange multipliers) $(\lambda , \mu , \alpha , \beta$), ma trận cỡ $(p + q) \times  (p + q)$ $X^{\top}X$ phải là augmented với không’s để tạo nó 2(p $+ q) \times$ 2(p $+ q)$ ma trận $P_{a}$ cho trước bởi
$$P_{a} = \begin{pmatrix} X^{\top}X & 0_{p+q,p+q} \\ 0_{p+q,p+q} & 0_{p+q,p+q} \end{pmatrix} ,$$
Và tương tự $q$ là augmented với các không điểm như vectơ
$$q_{a} = \begin{pmatrix} -1_{p+q} \\ 0_{p+q}. \end{pmatrix}$$

## 54.5 Lề mềm (soft margin) Các máy vectơ hỗ trợ (SVMs); (SVM)

$$s2'$$
Trong mục này ta xét tổng quát hóa của Bài toán $(SVM_{s2})$ cho phiên bản của lề mềm (soft margin) SVM coming từ Bài toán $(SVM_{h2})$ bằng cách cộng extra bậc của freedom, cụ thể là thay vì của lề (margin) $\delta  = 1/ \|w\|$, ta sử dụng lề (margin) $\delta  = \eta / \|w\|$ ở đâu $\eta$ là một số dương hằng số rằng ta muốn để cực đại hóa. Đến thực hiện do đó, ta cộng số hạng $K_{m}\eta$ đến hàm mục tiêu (objective function)
$$(1/2)w^{\top}w as well as the “regularizing term” K_{s} \sum_{i}  \sum  whose purpose is to$$
$$\begin{pmatrix} - \\ p & \epsilon_{i}  + & q & \xi_{j} \\ =1 & j=1 \\ margin)andK_{s}> \end{pmatrix}$$
Tạo $\epsilon$ và $\xi$ thưa (sparse), ở đâu $K_{m} > 0 (m$ refers đến $0 (s$ refers đến thưa (sparse)) là cố định các hằng số rằng có thể được adjusted để xác định influence của $\eta$ và regularizing số hạng.

<!-- PAGE 1995 -->
Lề mềm (soft margin) SVM $(SVM_{s2'})$:
$$minimize \frac{1}{2} w^{\top}w -K_{m}\eta  + K_{s} \begin{pmatrix} \epsilon^{\top} & \xi^{\top} \end{pmatrix} 1_{p+q}$$
$$subject to$$
$$w^{\top}u_{i} -b \ge \eta  -\epsilon_{i} ,\epsilon_{i}  \ge 0i = 1, \dots  , p$$
$$-w^{\top}v_{j} + b \ge \eta  -\xi_{j} ,\xi_{j}  \ge 0j = 1, \dots  , q$$
$$\eta  \ge 0.$$
Điều này phiên bản của SVM bài toán đã là thứ nhất được thảo luận trong Sch¨olkopf, Smola, Williamson, và Bartlett $[153]$ dưới name của $\nu$ -SVC (hoặc $\nu$ -SVM), và cũng được sử dụng trong Sch¨olkopf, Platt, Shawe–Taylor, và Smola $[152]$. $\nu$ -SVC phương pháp cũng được trình bày trong Sch¨olkopf và Smola $[151]$ (mà chứa nhiều nhiều hơn/thêm). difference giữa $\nu$ -SVC phương pháp và phương pháp được trình bày trong Mục 54.3, đôi khi được gọi là C-SVM phương pháp, đã là một cách kỹ lưỡng investigated bởi Chan và Lin $[36]$. Cho bài toán này nó là không có dài hơn rõ ràng rằng nếu $(w, \eta , b, \epsilon , \xi$) là nghiệm tối ưu (optimal solution), thì $w \neq  0$ và $\eta  > 0$. Thực ra, nếu các tập hợp của các điểm là không một cách tuyến tính khả ly và nếu $K_{s}$ được chọn cũng big, Bài toán $(SVM_{s2'})$ có thể thất bại đến có nghiệm tối ưu (optimal solution). Ta chỉ ra rằng trong thứ tự cho bài toán đến có nghiệm ta phải chọn $K_{m}$ và $K_{s}$ sao cho
$$K_{m} \le \min{2pK_{s}, 2qK_{s}}.$$
Nếu ta định nghĩa $\nu$ bởi
$$\nu  = \frac{K_{m}}{(p + q)K_{s}} ,$$
Thì $K_{m} \le min{2pK_{s}, 2qK_{s}}$ là tương đương đến
$$$$
$$\nu  \le \min \frac{2p}{p + q} , \frac{2q}{p + q} \le 1.$$
Lý do cho giới thiệu $\nu$ là rằng $\nu (p + q)/2$ có thể được interpreted như cực đại số của các điểm thất bại đến đạt được lề (margin) $\delta  = \eta / \|w\|$. Ta sẽ chỉ ra sau này rằng nếu các điểm $u_{i}$ và $v_{j}$ là không khả ly, thì ta phải chọn $\nu$ sao cho $\nu  \ge 2/(p + q)$ cho phương pháp đến có nghiệm cho mà $w \neq  0$ và $\eta  > 0$. hàm mục tiêu (objective function) của bài toán của chúng ta là lồi và các ràng buộc là afin. Hệ quả là, theo Định lý 50.17(2) nếu Bài toán gốc (primal problem) $(SVM_{s2'})$ có nghiệm tối ưu (optimal solution), thì bài toán đối ngẫu (dual problem) có nghiệm cũng, và khoảng cách đối ngẫu (duality gap) là không. Điều này thực hiện không ngay lập tức suy ra rằng nghiệm tối ưu (optimal solution) của đối ngẫu (dual) cho ta nghiệm tối ưu (optimal solution) của gốc (primal) bởi vì các giả thiết của Định lý 50.17(1) thất bại đến đúng. Ta chỉ ra rằng nếu bài toán gốc (primal problem) có nghiệm tối ưu (optimal solution) $(w, \eta , \epsilon , \xi , b)$ với w̸ $= 0$, thì bất kỳ nghiệm tối ưu (optimal solution) của bài toán đối ngẫu (dual problem) xác định $\lambda$ và $\mu$, mà trong turn xác định

<!-- PAGE 1996 -->
$w$ thông qua phương trình
$$w = -X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = \sum_{i=1}^{p}  \lambda_{i} u_{i} - \sum_{j=1}^{q}  \mu_{j} v_{j},(*_{w})$$
Và $\eta  \ge 0$. Nó vẫn còn để xác định $b, \eta , \epsilon$ và $\xi$. nghiệm của đối ngẫu (dual) thực hiện không xác định $b, \eta , \epsilon , \xi$ một cách trực tiếp, và ta là không biết của cần và đủ các điều kiện rằng đảm bảo rằng chúng có thể được được xác định. tốt nhất ta có thể thực hiện là để sử dụng KKT các điều kiện. đơn giản nhất đủ điều kiện là những gì ta gọi Tiêu chuẩn Lề (margin) Giả thiết cho $(SVM_{s2'})$: Tồn tại một $i_{0}$ sao cho $0 < \lambda_{i0}  < K_{s}$, và tồn tại một $\mu_{j0}$ sao cho $0 < \mu_{j0}  < K_{s}$. Điều này có nghĩa là tồn tại một hỗ trợ/giá (support) vectơ $u_{i0}$ của loại/kiểu $1$ và tồn tại một hỗ trợ/giá (support) vectơ $v_{j0}$ của loại/kiểu $1$. Trong trường hợp này, thì bởi độ bù lỏng (complementary slackness), nó có thể được được hiển thị rằng $\epsilon_{i0}  = 0, \xi_{i0}  = 0$, và tương ứng các bất đẳng thức là hoạt động, nghĩa là ta có các phương trình
$$w^{\top}u_{i0} -b = \eta ,-w^{\top}v_{j0} + b = \eta ,$$
Do đó ta có thể giải cho $b$ và $\eta$. Khi đó vì bởi độ bù lỏng (complementary slackness), nếu $\epsilon_{i}  > 0$, thì $\lambda_{i}  = K_{s}$ và nếu $\xi_{j}  > 0$, thì $\mu_{j}  = K_{s}$, tất cả các bất đẳng thức tương ứng với như vậy $\epsilon_{i}  > 0$ và $\mu_{j}  > 0$ là hoạt động, và ta có thể giải cho $\epsilon_{i}$ và $\xi_{j}$. tuyến tính các ràng buộc được cho bởi (2(p $+ q) + 1) \times  (n + p + q + 2)$ ma trận cho trước trong khối tạo thành bởi
$$C = \begin{pmatrix} - & 1_{p} \\ X^{\top} & I_{p+q} & -1_{q} & 1_{p+q} \\ 0_{p+q,n} & -I_{p+q} & 0_{p+q} & 0_{p+q} \\ 0_{n}^{\top} & 0_{p+q}^{\top} & 0 & 1 \end{pmatrix} ,$$
$$-$$
Ở đâu $X$ là ma trận cỡ $n \times  (p + q)$
$$X = \begin{pmatrix} -u_{1} & \cdots & -u_{p} & v_{1} & \cdots & v_{q} \end{pmatrix} ,$$
Và tuyến tính các ràng buộc được biểu diễn bởi
$$\begin{pmatrix} - & 1_{p} \\ X^{\top} & I_{p+q} & -1_{q} & 1_{p+q} \\ 0_{p+q,n} & -I_{p+q} & 0_{p+q} & 0_{p+q} \\ 0_{n}^{\top} & 0_{p+q}^{\top} & 0 & 1 \end{pmatrix} \begin{pmatrix} w \\ \epsilon \\ \xi \\ b \\ \eta \end{pmatrix} \le \begin{pmatrix} 0_{p+q} \\ 0_{p+q} \\ 0 \end{pmatrix} .$$
$$-$$
Hàm mục tiêu (objective function) được cho bởi
$$J(w, \epsilon , \xi , b, \eta ) = \frac{1}{2} w^{\top}w -K_{m}\eta  + K_{s} \begin{pmatrix} \epsilon^{\top} & \xi^{\top} \end{pmatrix} 1_{p+q}.$$

<!-- PAGE 1997 -->
Hàm Lagrange (Lagrangian) L(w, $\epsilon , \xi , b, \eta , \lambda , \mu , \alpha , \beta , \gamma$) với $\lambda , \alpha  \in \mathbb{R}_{+}^{p}, \mu , \beta  \in \mathbb{R}_{+}^{q}$, và $\gamma  \in \mathbb{R}_{+}$ được cho bởi
$$L(w, \epsilon , \xi , b, \eta , \lambda , \mu , \alpha , \beta , \gamma ) = \frac{1}{2} w^{\top}w -K_{m}\eta  + K_{s} \begin{pmatrix} \epsilon^{\top} & \xi^{\top} \end{pmatrix} 1_{p+q}$$
$$+ \begin{pmatrix} w^{\top} &  \epsilon^{\top} & \xi^{\top} \end{pmatrix} \begin{pmatrix} b & \eta \end{pmatrix} C^{\top} \begin{pmatrix} \lambda \\ \mu \\ \alpha \\ \beta \\ \gamma \end{pmatrix} .$$
Vì
$$\begin{pmatrix} w^{\top} &  \epsilon^{\top} & \xi^{\top} \end{pmatrix} \begin{pmatrix} b & \eta \end{pmatrix} C^{\top} \begin{pmatrix} \lambda \\ \mu \\ \alpha \\ \beta \\ \gamma \end{pmatrix} = w^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} -\epsilon^{\top} (\lambda  + \alpha ) -\xi^{\top} (\mu  + \beta ) + b(1_{p}^{\top} \lambda  -1_{q}^{\top} \mu )$$
$$+ \eta (1_{p}^{\top} \lambda  + 1_{q}^{\top} \mu ) -\gamma \eta ,$$
Hàm Lagrange (Lagrangian) có thể được viết dưới dạng
$$L(w, \epsilon , \xi , b, \eta , \lambda , \mu , \alpha , \beta , \gamma ) = \frac{1}{2} w^{\top}w -K_{m}\eta  + K_{s}(\epsilon^{\top} 1_{p} + \xi^{\top} 1_{q}) + w^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} -\epsilon^{\top} (\lambda  + \alpha )$$
$$\xi^{\top} (\mu  + \beta ) + b(1_{p}^{\top} \lambda  -1_{q}^{\top} \mu ) + \eta (1_{p}^{\top} \lambda  + 1_{q}^{\top} \mu ) -\gamma \eta$$
$$= \frac{-1}{2} w^{\top}w + w^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} + (1_{p}^{\top} \lambda  + 1_{q}^{\top} \mu  -K_{m} -\gamma )\eta$$
$$+ \epsilon^{\top} (K_{s}1_{p} -(\lambda  + \alpha )) + \xi^{\top} (K_{s}1_{q} -(\mu  + \beta )) + b(1_{p}^{\top} \lambda  -1_{q}^{\top} \mu ).$$
Để tìm đối ngẫu (dual) hàm $G(\lambda , \mu , \alpha , \beta , \gamma$) ta cực tiểu hóa L(w, $\epsilon , \xi , b, \eta , \lambda , \mu , \alpha , \beta , \gamma$) với
$$\mathbb{R}^{n} \mathbb{R}^{p} \mathbb{R}^{q}$$
Đối với đến $w, \epsilon , \xi , b$, và $\eta$. Vì Hàm Lagrange (Lagrangian) là lồi và $(w, \epsilon , \xi , b, \eta$) $\in \times \times \times \mathbb{R} \times \mathbb{R}$, lồi tập mở (open set), theo Định lý 40.13, Hàm Lagrange (Lagrangian) có cực tiểu trong $(w, \epsilon , \xi , b, \eta$) khi và chỉ khi $\nabla L_{w,\epsilon ,\xi ,b,\eta} = 0$, do đó ta tính gradien của nó đối với $w, \epsilon , \xi , b, \eta$, và ta thu được
$$\begin{pmatrix}\end{pmatrix}$$
$$\nabla L_{w,\epsilon ,\xi ,b,\eta} = \begin{pmatrix} \lambda  \\ X & \mu & + w \\ K_{s}1_{p} -(\lambda  + \alpha ) \\ K_{s}1_{q} -(\mu  + \beta ) \\ 1_{p}^{\top}\lambda  -1_{q}^{\top}\mu \\ 1_{p}^{\top}\lambda  + 1_{q}^{\top}\mu & K_{m} & \gamma \end{pmatrix} .$$
$$- -$$
Bằng cách đặt $\nabla L_{w,\epsilon ,\xi ,b,\eta} = 0$ ta thu được các phương trình
$$w = -X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} (*_{w})$$

<!-- PAGE 1998 -->
$$\lambda  + \alpha  = K_{s}1_{p}$$
$$\mu  + \beta  = K_{s}1_{q}$$
$$1_{p}^{\top} \lambda  = 1_{q}^{\top} \mu ,$$
Và
$$1_{p}^{\top} \lambda  + 1_{q}^{\top} \mu  = K_{m} + \gamma .(*_{\gamma})$$
Thứ hai và thứ ba các phương trình là tương đương đến hình hộp các ràng buộc
$$0 \le \lambda_{i} , \mu_{j}  \le K_{s},i = 1, \dots  , p, j = 1, \dots  , q,$$
Và vì $\gamma  \ge 0$ phương trình $(*_{\gamma})$ là tương đương đến
$$1_{p}^{\top} \lambda  + 1_{q}^{\top} \mu  \ge K_{m}.$$
Plugging quay lại $w$ từ $(*_{w})$ vào Hàm Lagrange (Lagrangian), sau simplifications ta thu được
$$G(\lambda , \mu , \alpha , \beta ) = \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \\  \end{pmatrix} - \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$= - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} ,$$
Do đó đối ngẫu (dual) hàm là độc lập của $\alpha , \beta$ và được cho bởi
$$G(\lambda , \mu ) = - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} .$$
Đối ngẫu (dual) bài toán quy hoạch được cho bởi
$$maximize- \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  \ge K_{m}$$
$$0 \le \lambda_{i}  \le K_{s},i = 1, \dots  , p$$
$$0 \le \mu_{j}  \le K_{s},j = 1, \dots  , q.$$
Cuối cùng, đối ngẫu (dual) bài toán quy hoạch là tương đương đến sau đây cực tiểu hóa bài toán quy hoạch:

<!-- PAGE 1999 -->
Đối ngẫu (dual) của Lề mềm (soft margin) SVM $(SVM_{s2'})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  \ge K_{m}$$
$$0 \le \lambda_{i}  \le K_{s},i = 1, \dots  , p$$
$$0 \le \mu_{j}  \le K_{s},j = 1, \dots  , q.$$
Nếu $(w, \eta , \epsilon , \xi , b)$ là nghiệm tối ưu (optimal solution) của Bài toán $(SVM_{s2'})$ với $w \neq  0$ và $\eta  \neq  0$, thì độ bù lỏng (complementary slackness) các điều kiện cho phân loại của các điểm $u_{i}$ và $v_{j}$ theo các giá trị của $\lambda$ và $\mu$. Thật vậy, ta có $\epsilon_{i} \alpha_{i}  = 0$ cho $i = 1, \dots  , p$ và $\xi_{j} \beta_{j}  = 0$ cho $j = 1, \dots  , q$. Cũng, nếu $\lambda_{i}  > 0$, thì tương ứng ràng buộc là hoạt động, và tương tự nếu $\mu_{j}  > 0$. Vì $\lambda_{i}  + \alpha_{i}  = K_{s}$, suy ra rằng $\epsilon_{i} \alpha_{i}  = 0$ khi và chỉ khi $\epsilon_{i} (K_{s}$ - $\lambda_{i}$) $= 0$, và vì $\mu_{j}  + \beta_{j}  = K_{s}$, ta có $\xi_{j} \beta_{j}  = 0$ khi và chỉ khi $\xi_{j} (K_{s}$ - $\mu_{j}$) $= 0$. Do đó nếu $\epsilon_{i}  > 0$, thì $\lambda_{i}  = K_{s}$, và nếu $\xi_{j}  > 0$, thì $\mu_{j}  = K_{s}$. Hệ quả là, nếu $\lambda_{i}  < K_{s}$, thì $\epsilon_{i}  = 0$ và $u_{i}$ là một cách chính xác được phân loại, và tương tự nếu $\mu_{j}  < K_{s}$, thì $\xi_{j}  = 0$ và $v_{j}$ là một cách chính xác được phân loại. Ta có kết quả sau phân loại mà là basically phân loại cho trước trong Mục 54.1 thu được bằng cách thay thế $\delta$ với $\eta$ (nhắc lại rằng $\eta  > 0$ và $\delta  = \eta / \|w\|)$.
$(1)$ Nếu $0 < \lambda_{i}  < K_{s}$, thì $\epsilon_{i}  = 0$ và thứ $i$ bất đẳng thức là hoạt động, do đó
$$w^{\top}u_{i} -b -\eta  = 0.$$
Điều này có nghĩa là $u_{i}$ là trên xanh lam lề (margin) (siêu phẳng (hyperplane) $H_{w,b+\eta}$ của phương trình $w^{\top}x = b + \eta$) và được phân loại một cách chính xác. Tương tự, nếu $0 < \mu_{j}  < K_{s}$, thì $\xi_{j}  = 0$ và
$$w^{\top}v_{j} -b + \eta  = 0,$$
Do đó $v_{j}$ là trên đỏ lề (margin) (siêu phẳng (hyperplane) $H_{w,b-\eta}$ của phương trình $w^{\top}x = b$ - $\eta$) và được phân loại một cách chính xác.
$(2)$ Nếu $\lambda_{i}  = K_{s}$, thì thứ $i$ bất đẳng thức là hoạt động, do đó
$$w^{\top}u_{i} -b -\eta  = -\epsilon_{i} .$$
Nếu $\epsilon_{i}  = 0$, thì điểm $u_{i}$ là trên xanh lam lề (margin). Nếu $\epsilon_{i}  > 0$, thì $u_{i}$ là trong phạm vi mở một nửa không gian bị chặn bởi xanh lam lề (margin) siêu phẳng (hyperplane) $H_{w,b+\eta}$ và chứa

<!-- PAGE 2000 -->
Tách siêu phẳng (hyperplane) $H_{w,b}$; nếu $\epsilon_{i}  \le \eta$, thì $u_{i}$ được phân loại một cách chính xác, và nếu $\epsilon_{i}  > \eta$, thì $u_{i}$ là misclassified $(u_{i}$ lies trên sai vế/cạnh của tách siêu phẳng (hyperplane), đỏ vế/cạnh). Tương tự, nếu $\mu_{j}  = K_{s}$, thì
$$w^{\top}v_{j} -b + \eta  = \xi_{j} .$$
Nếu $\xi_{j}  = 0$, thì điểm $v_{j}$ là trên đỏ lề (margin). Nếu $\xi_{j}  > 0$, thì $v_{j}$ là trong phạm vi mở một nửa không gian bị chặn bởi đỏ lề (margin) siêu phẳng (hyperplane) $H_{w,b-\eta}$ và chứa tách siêu phẳng (hyperplane) $H_{w,b}$; nếu $\xi_{j}  \le \eta$, thì $v_{j}$ được phân loại một cách chính xác, và nếu $\xi_{j}  > \eta$, thì $v_{j}$ là misclassified $(v_{j}$ lies trên sai vế/cạnh của tách siêu phẳng (hyperplane), xanh lam vế/cạnh).
$(3)$ Nếu $\lambda_{i}  = 0$, thì $\epsilon_{i}  = 0$ và thứ $i$ bất đẳng thức có thể hoặc có thể không là hoạt động, do đó
$$w^{\top}u_{i} -b -\eta  \ge 0.$$
Do đó $u_{i}$ là trong đóng một nửa không gian trên xanh lam vế/cạnh bị chặn bởi xanh lam lề (margin) siêu phẳng (hyperplane) $H_{w,b+\eta}$ (của course, được phân loại một cách chính xác). Tương tự, nếu $\mu_{j}  = 0$, thì
$$w^{\top}v_{j} -b + \eta  \le 0$$
Và $v_{j}$ là trong đóng một nửa không gian trên đỏ vế/cạnh bị chặn bởi đỏ lề (margin) siêu phẳng (hyperplane) $H_{w,b-\eta}$ (của course, được phân loại một cách chính xác).

> **Định nghĩa 54.2.** các vectơ $u_{i}$ trên xanh lam lề (margin) $H_{w,b+\eta}$ và các vectơ $v_{j}$ trên đỏ lề (margin) $H_{w,b-\eta}$ được gọi là hỗ trợ/giá (support) các vectơ. Hỗ trợ/giá (support) các vectơ tương ứng với các vectơ $u_{i}$ cho mà $w^{\top}u_{i}$ - $b$ - $\eta  = 0$ (mà suy ra $\epsilon_{i}  = 0)$, và các vectơ $v_{j}$ cho mà $w^{\top}v_{j}$ - $b + \eta  = 0$ (mà suy ra $\xi_{j}  = 0)$. Hỗ trợ/giá (support) các vectơ $u_{i}$ sao cho $0 < \lambda_{i}  < K_{s}$ và hỗ trợ/giá (support) các vectơ $v_{j}$ sao cho $0 < \mu_{j}  < K_{s}$ là hỗ trợ/giá (support) các vectơ của loại/kiểu $1$. Hỗ trợ/giá (support) các vectơ của loại/kiểu $1$ đóng đặc biệt vai trò do đó ta ký hiệu các tập hợp của các chỉ số liên kết với chúng bởi
$$I_{\lambda} = {i \in {1, \dots  , p} | 0 < \lambda_{i}  < K_{s}}$$
$$I_{\mu} = {j \in {1, \dots  , q} | 0 < \mu_{j}  < K_{s}}.$$
Ta ký hiệu của chúng cardinalities bởi $numsvl_{1} = |I_{\lambda}|$ và $numsvm_{1} = |I_{\mu}|$. Hỗ trợ/giá (support) các vectơ $u_{i}$ sao cho $\lambda_{i}  = K_{s}$ và hỗ trợ/giá (support) các vectơ $v_{j}$ sao cho $\mu_{j}  = K_{s}$ là hỗ trợ/giá (support) các vectơ của loại/kiểu $2$. Những phần tử đó hỗ trợ/giá (support) các vectơ $u_{i}$ sao cho $\lambda_{i}  = 0$ và những phần tử đó hỗ trợ/giá (support) các vectơ $v_{j}$ sao cho $\mu_{j}  = 0$ được gọi là exceptional hỗ trợ/giá (support) các vectơ. các vectơ $u_{i}$ cho mà $\lambda_{i}  = K_{s}$ và các vectơ $v_{j}$ cho mà $\mu_{j}  = K_{s}$ được nói đến thất bại lề (margin). các tập hợp của các chỉ số liên kết với các vectơ thất bại lề (margin) được ký hiệu bởi
$$K_{\lambda} = {i \in {1, \dots  , p} | \lambda_{i}  = K_{s}}$$
$$K_{\mu} = {j \in {1, \dots  , q} | \mu_{j}  = K_{s}}.$$
Ta ký hiệu của chúng cardinalities bởi $p_{f} = |K_{\lambda}|$ và $q_{f} = |K_{\mu}|$.

<!-- PAGE 2001 -->
Nó sẽ cũng là hữu ích đến understand cách mà các điểm được phân loại theo $\epsilon_{i}$ (hoặc $\xi_{j}$).
$(1)$ Nếu $\epsilon_{i}  > 0$, thì bởi độ bù lỏng (complementary slackness) $\lambda_{i}  = K_{s}$, do đó phương trình thứ $i$ là hoạt động và bởi $(2)$ ở trên,
$$w^{\top}u_{i} -b -\eta  = -\epsilon_{i} .$$
Vì $\epsilon_{i}  > 0$, điểm $u_{i}$ là chặt trong phạm vi mở một nửa không gian bị chặn bởi xanh lam lề (margin) siêu phẳng (hyperplane) $H_{w,b+\eta}$ và chứa tách siêu phẳng (hyperplane) $H_{w,b}$ (excluding xanh lam siêu phẳng (hyperplane) $H_{w,b+\eta})$; nếu $\epsilon_{i}  \le \eta$, thì $u_{i}$ được phân loại một cách chính xác, và nếu $\epsilon_{i}  > \eta$, thì $u_{i}$ là misclassified. Tương tự, nếu $\xi_{j}  > 0$, thì $v_{j}$ là chặt trong phạm vi mở một nửa không gian bị chặn bởi đỏ lề (margin) siêu phẳng (hyperplane) $H_{w,b-\eta}$ và chứa tách siêu phẳng (hyperplane) $H_{w,b}$ (excluding đỏ siêu phẳng (hyperplane) $H_{w,b-\eta})$; nếu $\xi_{j}  \le \eta$, thì $v_{j}$ được phân loại một cách chính xác, và nếu $\xi_{j}  > \eta$, thì $v_{j}$ là misclassified.
$(2)$ Nếu $\epsilon_{i}  = 0$, thì điểm $u_{i}$ là một cách chính xác được phân loại. Nếu $\lambda_{i}  = 0$, thì bởi $(3)$ ở trên, $u_{i}$ là trong đóng một nửa không gian trên xanh lam vế/cạnh bị chặn bởi xanh lam lề (margin) siêu phẳng (hyperplane) $H_{w,b+\eta}$. Nếu $\lambda_{i}  > 0$, thì bởi $(1)$ và $(2)$ ở trên, điểm $u_{i}$ là trên xanh lam lề (margin). Tương tự, nếu $\xi_{j}  = 0$, thì điểm $v_{j}$ là một cách chính xác được phân loại. Nếu $\mu_{j}  = 0$, thì $v_{j}$ là trong đóng một nửa không gian trên đỏ vế/cạnh bị chặn bởi đỏ lề (margin) siêu phẳng (hyperplane) $H_{w,b-\eta}$, và nếu $\mu_{j}  > 0$, thì điểm $v_{j}$ là trên đỏ lề (margin). Cũng nhận thấy rằng nếu $\lambda_{i}  > 0$, thì $u_{i}$ là trong đóng một nửa không gian bị chặn bởi xanh lam siêu phẳng (hyperplane) $H_{w,b+\eta}$ và chứa tách siêu phẳng (hyperplane) $H_{w,b}$ (bao gồm cả xanh lam siêu phẳng (hyperplane) $H_{w,b+\eta})$. Tương tự, nếu $\mu_{j}  > 0$, thì $v_{j}$ là trong đóng một nửa không gian bị chặn bởi đỏ siêu phẳng (hyperplane) $H_{w,b+\eta}$ và chứa tách siêu phẳng (hyperplane) $H_{w,b}$ (bao gồm cả đỏ siêu phẳng (hyperplane) $H_{w,b+\eta})$.

> **Định nghĩa 54.3.** Các vectơ $u_{i}$ sao cho $\lambda_{i}  > 0$ và các vectơ $v_{j}$ sao cho $\mu_{j}  > 0$ được nói đến có lề (margin) nhiều nhất $\delta$. các tập hợp của các chỉ số liên kết với các vectơ này được ký hiệu bởi
$$I_{\lambda >0} = {i \in {1, \dots  , p} | \lambda_{i}  > 0}$$
$$I_{\mu >0} = {j \in {1, \dots  , q} | \mu_{j}  > 0}.$$
Ta ký hiệu của chúng cardinalities bởi $p_{m} = |I_{\lambda >0}|$ và $q_{m} = |I_{\mu >0}|$. Các vectơ $u_{i}$ sao cho $\epsilon_{i}  > 0$ và các vectơ $v_{j}$ sao cho $\xi_{j}  > 0$ được nói đến chặt thất bại lề (margin). tương ứng các tập hợp của các chỉ số được ký hiệu bởi
$$E_{\lambda} = {i \in {1, \dots  , p} | \epsilon_{i}  > 0}$$
$$E_{\mu} = {j \in {1, \dots  , q} | \xi_{j}  > 0}.$$
Ta viết $p_{sf} = |E_{\lambda}|$ và $q_{sf} = |E_{\mu}|$.

<!-- PAGE 2002 -->
Ta có inclusions $E_{\lambda} \subseteq K_{\lambda}$ và $E_{\mu} \subseteq K_{\mu}$. difference giữa thứ nhất các tập hợp và thứ hai các tập hợp là rằng thứ hai các tập hợp có thể chứa hỗ trợ/giá (support) các vectơ của loại/kiểu $2$ sao cho $\lambda_{i}  = K_{s}$ và $\epsilon_{i}  = 0$, hoặc $\mu_{j}  = K_{s}$ và $\xi_{j}  = 0$. Ta cũng có các phương trình $I_{\lambda} \cup (K_{\lambda}$ - $E_{\lambda}) \cup E_{\lambda} = I_{\lambda >0}$ và $I_{\mu} \cup (K_{\mu}$ - $E_{\mu}) \cup E_{\mu} = I_{\mu >0}$, và các bất đẳng thức $p_{sf} \le p_{f} \le p_{m}$ và $q_{sf} \le q_{f} \le q_{m}$. xanh lam các điểm $u_{i}$ của chỉ số $i \in I_{\lambda >0}$ được phân loại như sau:
$(1)$ Nếu $i \in I_{\lambda}$, thì $u_{i}$ là hỗ trợ/giá (support) vectơ của loại/kiểu $1 (\lambda_{i}  < K_{s})$.
$(2)$ Nếu $i \in K_{\lambda}$ - $E_{\lambda}$, thì $u_{i}$ là hỗ trợ/giá (support) vectơ của loại/kiểu $2 (\lambda_{i}  = K_{s})$.
$(3)$ Nếu $i \in E_{\lambda}$, thì $u_{i}$ chặt không thỏa mãn lề (margin), nghĩa là $\epsilon_{i}  > 0$. Tương tự đỏ các điểm $v_{j}$ của chỉ số $j \in I_{\mu >0}$ được phân loại như sau:
$(1)$ Nếu $j \in I_{\mu}$, thì $v_{j}$ là hỗ trợ/giá (support) vectơ của loại/kiểu $1 (\mu_{j}  < K_{s})$.
$(2)$ Nếu $j \in K_{\mu}$ - $E_{\mu}$, thì $v_{j}$ là hỗ trợ/giá (support) vectơ của loại/kiểu $2 (\mu_{j}  = K_{s})$.
$(3)$ Nếu $j \in E_{\mu}$, thì $v_{j}$ chặt không thỏa mãn lề (margin), nghĩa là $\xi_{j}  > 0$. Lưu ý rằng $p_{m}$ - $p_{f}$ là số của xanh lam hỗ trợ/giá (support) các vectơ của loại/kiểu $1$ và $q_{m}$ - $q_{f}$ là số của đỏ hỗ trợ/giá (support) các vectơ của loại/kiểu $1$. còn lại xanh lam các điểm $u_{i}$ cho mà $\lambda_{i}  = 0$ là hoặc exceptional hỗ trợ/giá (support) các vectơ hoặc chúng là (chặt) trong mở nửa không gian (half-space) tương ứng với xanh lam vế/cạnh. Tương tự, còn lại đỏ các điểm $v_{j}$ cho mà $\mu_{j}  = 0$ là hoặc exceptional hỗ trợ/giá (support) các vectơ hoặc chúng là (chặt) trong mở nửa không gian (half-space) tương ứng với đỏ vế/cạnh. Nó được hiển thị trong Mục 54.8 cách mà đối ngẫu (dual) bài toán quy hoạch được giải bằng cách sử dụng ADMM từ Mục 52.6. Nếu bài toán gốc (primal problem) là giải được, điều này cho ta các nghiệm cho $\lambda$ và $\mu$. Một lần nghiệm cho $\lambda$ và $\mu$ là thu được, ta có
$$w = -X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} = \sum_{i=1}^{p}  \lambda_{i} u_{i} - \sum_{j=1}^{q}  \mu_{j} v_{j}.$$
Như ta được nói trước đó, các giả thiết của Định lý 50.17(2) đúng, do đó nếu bài toán gốc (primal problem) $(SVM_{s2'})$ có nghiệm tối ưu (optimal solution) với $w \neq  0$, thì bài toán đối ngẫu (dual problem) có nghiệm cũng, và khoảng cách đối ngẫu (duality gap) là không. Vì vậy, cho tối ưu các nghiệm ta có
$$L(w, \epsilon , \xi , b, \eta , \lambda , \mu , \alpha , \beta , \gamma ) = G(\lambda , \mu , \alpha , \beta , \gamma ),$$
Mà có nghĩa là
$$\frac{1}{2} w^{\top}w -K_{m}\eta  + K_{s} \begin{pmatrix} \epsilon_{i}  + & \xi_{j} \end{pmatrix} \sum_{i=1}^{p}  \sum_{j=1}^{q}  = - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} ,$$
Và vì
$$w = -X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} ,$$

<!-- PAGE 2003 -->
Ta thu được
$$\frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} -K_{m}\eta  + K_{s} \begin{pmatrix} \epsilon_{i}  + & \xi_{j} \end{pmatrix} \sum_{i=1}^{p}  \sum_{j=1}^{q}  = - \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} ,$$
Mà cho ta
$$\eta  = \frac{K_{s}}{K_{m}} \begin{pmatrix} \epsilon_{i}  + & \xi_{j} \end{pmatrix} \sum_{i=1}^{p}  \sum_{j=1}^{q}  + \frac{1}{K_{m}} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} X^{\top}X \begin{pmatrix} \lambda \\ \mu \end{pmatrix} .(*)$$
Vì vậy, ta confirm rằng $\eta  \ge 0$.
Các nhận xét: Vì ta được chứng minh rằng nếu Bài toán gốc (primal problem) $(SVM_{s2'})$ có nghiệm tối ưu (optimal solution) với $w \neq  0$, thì $\eta  \ge 0$, một có thể tự hỏi tại sao ràng buộc $\eta  \ge 0$ đã là included. Nếu ta xóa điều này ràng buộc, nó là dễ để xem rằng chỉ difference là rằng thay vì của phương trình
$$1_{p}^{\top} \lambda  + 1_{q}^{\top} \mu  = K_{m} + \gamma (*_{1})$$
Ta thu được phương trình
$$1_{p}^{\top} \lambda  + 1_{q}^{\top} \mu  = K_{m}.(*_{2})$$
Nếu $\eta  > 0$, thì bởi độ bù lỏng (complementary slackness) $\gamma  = 0$, trong mà trường hợp $(*_{1})$ và $(*_{2})$ là tương đương. Nhưng nếu $\eta  = 0$, thì $\gamma$ có thể là chặt dương. option đến bỏ qua ràng buộc $\eta  \ge 0$ trong gốc (primal) là slightly advantageous bởi vì thì đối ngẫu (dual) liên quan đến $2(p+q)$ thay vì của $2(p+q)+1$ Các nhân tử Lagrange (Lagrange multipliers), do đó ràng buộc ma trận là $(p + q + 2) \times$ 2(p $+ q)$ ma trận thay vì của $(p + q + 2) \times$ (2(p $+ q) + 1)$ ma trận và ma trận định nghĩa toàn phương phiếm hàm là 2(p $+ q) \times$ 2(p $+ q)$ ma trận thay vì của (2(p $+ q) + 1) \times$ (2(p $+ q) + 1)$ ma trận; xem Mục 54.8. Dưới Tiêu chuẩn Lề (margin) Giả thiết cho $(SVM_{s2'})$, tồn tại một $i_{0}$ sao cho $0 < \lambda_{i0}  < K_{s}$ và một số $j_{0}$ sao cho $0 < \mu_{j0}  < K_{s}$, và bởi độ bù lỏng (complementary slackness) các điều kiện $\epsilon_{i0}  = 0$ và $\xi_{j0}  = 0$, do đó ta có hai hoạt động các ràng buộc
$$w^{\top}u_{i0} -b = \eta ,-w^{\top}v_{j0} + b = \eta ,$$
Và ta có thể giải cho $b$ và $\eta$ và ta thu được
$$b = \frac{w^{\top}u_{i0}+ w^{\top}v_{j0}}{2}$$
$$-$$
$$\eta  = \frac{w^{\top}u_{i0}w^{\top}v_{j0}}{\eta 2}$$
$$\delta  =.$$
$$\|w\|$$
Do số tính mất ổn định, khi viết máy tính bài toán quy hoạch nó được ưu tiên hơn để tính các danh sách của các chỉ số $I_{\lambda}$ và $I_{\mu}$ cho trước bởi
$$I_{\lambda} = {i \in {1, \dots  , p} | 0 < \lambda_{i}  < K_{s}}$$
$$I_{\mu} = {j \in {1, \dots  , q} | 0 < \mu_{j}  < K_{s}}.$$

<!-- PAGE 2004 -->
Thì nó là dễ để xem rằng ta có thể tính $b$ và $\eta$ bằng cách sử dụng sau đây lấy trung bình các công thức:
$$ \sum_{\in I\lambda}  \sum_{\in I\mu}  $$
$$b = w^{\top}/|I_{\lambda}| +/|I_{\mu}|/2$$
$$ \begin{pmatrix} u_{i} \\ i \end{pmatrix} \begin{pmatrix} v_{j} \\ j \end{pmatrix} $$
$$ \sum_{i\in I\lambda}  \sum_{j\in I\mu}  $$
$$\eta  = w^{\top}/|I_{\lambda}| -/|I_{\mu}|/2.$$
$$ \begin{pmatrix} u_{i} \end{pmatrix} \begin{pmatrix} v_{j} \end{pmatrix} $$
“kernelized” phiên bản của Bài toán $(SVM_{s2'})$ là sau đây: Lề mềm (soft margin) hạt nhân (kernel) SVM $(SVM_{s2'})$:
$$minimize \frac{1}{2} \langle w, w\rangle -K_{m}\eta  + K_{s} \begin{pmatrix} \epsilon^{\top} & \xi^{\top} \end{pmatrix} 1_{p+q}$$
$$subject to$$
$$\langle w, \phi (u_{i})\rangle -b \ge \eta  -\epsilon_{i} ,\epsilon_{i}  \ge 0i = 1, \dots  , p$$
$$-\langle w, \phi (v_{j})\rangle + b \ge \eta  -\xi_{j} ,\xi_{j}  \ge 0j = 1, \dots  , q$$
$$\eta  \ge 0.$$
Tracing qua derivation của đối ngẫu (dual) bài toán quy hoạch ta thu được Đối ngẫu (dual) của Lề mềm (soft margin) hạt nhân (kernel) SVM $(SVM_{s2'})$:
$$minimize \frac{1}{2} \begin{pmatrix} \lambda^{\top} & \mu^{\top} \end{pmatrix} K \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
$$subject to$$
$$\sum_{i=1}^{p}  \lambda_{i}  - \sum_{j=1}^{q}  \mu_{j}  = 0$$
$$\sum_{i=1}^{p}  \lambda_{i}  + \sum_{j=1}^{q}  \mu_{j}  \ge K_{m}$$
$$0 \le \lambda_{i}  \le K_{s},i = 1, \dots  , p$$
$$0 \le \mu_{j}  \le K_{s},j = 1, \dots  , q,$$
Ở đâu $K$ là hạt nhân (kernel) ma trận của Mục 54.1. Như trong Mục 54.3, ta thu được
$$w = \sum_{i=1}^{p}  \lambda_{i} \phi (u_{i}) - \sum_{j=1}^{q}  \mu_{j} \phi (v_{j}),$$
