# Đẳng thức Có ràng buộc Cực tiểu hóa


<!-- PAGE 1789 -->
Mà suy ra rằng
$$\begin{pmatrix} s_{1}x_{1} & \cdots & s_{n}x_{n} \\ conditions \end{pmatrix} = \mu 1_{n}^{\top} ,$$
Và ta thu được kết quả sau cần cho $f_{\mu}$ đến có cực đại:
$$Ax = b$$
$$A^{\top}y -s = c$$
$$\begin{pmatrix} s_{1}x_{1} & \cdots & s_{n}x_{n} \end{pmatrix} = \mu 1_{n}^{\top}$$
$$s, x > 0.$$
Nó là không khó để chỉ ra rằng nếu gốc (primal) bài toán quy hoạch tuyến tính (linear program) với hàm mục tiêu (objective function) $c^{\top}x$ và equational các ràng buộc Ax $= b$ và đối ngẫu (dual) bài toán quy hoạch với hàm mục tiêu (objective function) $b^{\top}y$ và bất đẳng thức các ràng buộc $A^{\top}y \ge c$ có phần trong (interior) chấp nhận được (feasible) các điểm $x$ và $y$, mà có nghĩa là $x > 0$ và $s > 0$ (ở đâu $s = A^{\top}y$ - $c)$, thì ở trên hệ của các phương trình có duy nhất nghiệm sao cho $x$ là duy nhất maximizer của $f_{\mu}$ trên $U$; xem Matousek và Gardner $[127]$ (Mục 7.2, Bổ đề 7.2.1). một cách cụ thể quan trọng ứng dụng của Mệnh đề 50.9 là tình huống ở đâu $\Omega =\mathbb{R}^{n}$.

## 50.4 Đẳng thức Có ràng buộc Cực tiểu hóa

Trong mục này ta xét sau đây Bài toán quy hoạch $(P)$:
$$minimizeJ(v)$$
$$subject to Av = b, v \in \mathbb{R}^{n},$$
Ở đâu $J$ là lồi khả vi (differentiable) hàm và $A$ là một ma trận cỡ $m \times  n$ của hạng (rank) $m < n$ (số của đẳng thức các ràng buộc là ít hơn số của các biến, và các phần tử này các ràng buộc là độc lập), và $b \in \mathbb{R}^{m}$.
$$\mathbb{R}^{n}\mathbb{R}^{n}$$
Theo Mệnh đề 50.9 (với $\Omega =$), Bài toán quy hoạch $(P)$ có cực tiểu tại $x \in$ nếu
$$\mathbb{R}^{m}$$
Và chỉ nếu ở đó tồn tại một số Các nhân tử Lagrange (Lagrange multipliers) $\lambda  \in$ sao cho sau đây các phương trình đúng:
$$Ax = b(pfeasibilty)$$
$$\nabla J_{x} + A^{\top}\lambda  = 0.(dfeasibility)$$
Tập hợp của các phương trình tuyến tính Ax $= b$ được gọi là gốc (primal) tính chấp nhận được các phương trình và tập hợp của (một cách tổng quát phi tuyến) các phương trình $\nabla J_{x} + A^{\top}\lambda  = 0$ được gọi là tập hợp của đối ngẫu (dual) tính chấp nhận được các phương trình. Nói chung, nó là không thể để giải các phương trình này analytically, do đó ta có để sử dụng số xấp xỉ các quy trình, hầu hết của mà là các biến thể của Newton’s phương pháp. Trong đặc biệt các trường hợp, ví dụ nếu $J$ là toàn phương phiếm hàm, đối ngẫu (dual) tính chấp nhận được các phương trình là cũng tuyến tính, trường hợp rằng ta xét trong nhiều hơn/thêm chi tiết.

<!-- PAGE 1790 -->
Giả sử $J$ là lồi toàn phương phiếm hàm của tạo thành
$$J(x) = \frac{1}{2} x^{\top}Px + q^{\top}x + r,$$
$$\mathbb{R}^{n} \mathbb{R}$$
Ở đâu $P$ là $n \times  n$ đối xứng nửa xác định dương (positive semidefinite) ma trận, $q \in$ và $r \in$. Trong trường hợp này
$$\nabla J_{x} = Px + q,$$
Do đó tính chấp nhận được các phương trình trở thành
$$Ax = b$$
$$Px + q + A^{\top}\lambda  = 0,$$
Mà trong ma trận tạo thành trở thành
$$\begin{pmatrix} P & A^{\top} \\ A & 0 \end{pmatrix} \begin{pmatrix} x \\ \lambda \end{pmatrix} = \begin{pmatrix} -q \\ b \end{pmatrix} .(KKT-eq)$$
Ma trận của hệ phương trình tuyến tính là thường được gọi là KKT-matrix. Nhận thấy rằng KKT ma trận đã là đã encountered trong Mệnh đề 42.3 với khác nhau ký hiệu; ở đó ta đã có $P = A^{-1}, A = B^{\top}, q = b$, và $b = f$. Nếu KKT ma trận là khả nghịch, thì của nó duy nhất nghiệm $(x^{*}, \lambda^{*}$) cho ta duy nhất cực tiểu $x^{*}$ của Bài toán $(P)$. Nếu KKT ma trận là suy biến nhưng Hệ (KKT-eq) là giải được, thì bất kỳ nghiệm $(x^{*}, \lambda^{*}$) cho ta cực tiểu $x^{*}$ của Bài toán $(P)$.

> **Mệnh đề 50.10.** Nếu Hệ (KKT-eq) là không giải được, thì Bài toán quy hoạch $(P)$ là không bị chặn ở dưới.

*Chứng minh.* Ta sử dụng sự kiện được hiển thị trong Mục 30.7, rằng hệ phương trình tuyến tính Bx $= c$ có không có nghiệm khi và chỉ khi tồn tại một $y$ rằng $B^{\top}y = 0$ và $y^{\top}c \neq  0$. Bởi thay đổi $y$ đến $-y$ nếu cần, ta có thể giả sử rằng $y^{\top}c > 0$. Ta áp dụng sự kiện này đến hệ phương trình tuyến tính (KKT-eq), do đó $B$ là KKT-matrix,
$$\mathbb{R}^{n} \mathbb{R}^{m}$$
Mà là đối xứng, và ta thu được điều kiện rằng ở đó tồn tại $v \in$ và $\lambda  \in$ sao cho
$$Pv + A^{\top}\lambda  = 0,Av = 0,-q^{\top}v + b^{\top}\lambda  > 0.$$
Vì ma trận cỡ $m \times  n$ $A$ có hạng (rank) $m$ và $b \in \mathbb{R}^{m}$, hệ Ax $= b$, là giải được, do đó với mọi chấp nhận được (feasible) $x_{0}$ (mà có nghĩa là $Ax_{0} = b)$, vì Av $= 0$, vectơ $x = x_{0} +$ tv là cũng nghiệm chấp nhận được (feasible solution) với mọi $t \in \mathbb{R}$. Bằng cách sử dụng sự kiện rằng Pv $= -A^{\top}\lambda , v^{\top}P = -\lambda^{\top} A$, Av $= 0, x_{0}^{\top} A^{\top} = b^{\top}$, và $P$ là đối xứng, ta có
$$J(x_{0} + tv) = J(x_{0}) + (v^{\top}Px_{0} + q^{\top}v)t + (1/2)(v^{\top}Pv)t^{2}$$
$$= J(x_{0}) + (x_{0}^{\top} Pv + q^{\top}v)t -(1/2)(\lambda^{\top} Av)t^{2}$$
$$= J(x_{0}) + (-x_{0}^{\top} A^{\top}\lambda  + q^{\top}v)t$$
$$= J(x_{0}) -(b^{\top}\lambda  -q^{\top}v)t,$$
Và vì $-q^{\top}v + b^{\top}\lambda  > 0$, ở trên biểu thức đi đến $-\infty$ khi $t$ đi đến $+\infty$.

<!-- PAGE 1791 -->
Nó là hiển nhiên quan trọng đến có các tiêu chuẩn đến decide liệu KKT-matrix là khả nghịch. Có thật vậy như vậy các tiêu chuẩn, như được điểm trong Boyd và Vandenberghe $[29]$ (Chương $10$, Bài tập 10.1).

> **Mệnh đề 50.11.** tính khả nghịch của KKT-matrix
$$\begin{pmatrix} P & A^{\top} \\ A & 0 \end{pmatrix}$$
Là tương đương đến sau đây các điều kiện:
$(1)$ Với mọi $x \in \mathbb{R}^{n}$, nếu Ax $= 0$ với $x \neq  0$, thì $x^{\top}Px > 0$; nghĩa là, $P$ là xác định dương (positive definite) trên hạt nhân (kernel) của $A$.
$(2)$ các hạt nhân của $A$ và $P$ chỉ có $0$ trong chung/phổ biến ((Ker $A) \cap$ (Ker $P) = {0})$.
$(3)$ Tồn tại một $n\times$ (n-m) ma trận $F$ sao cho Im(F) $=$ Ker $(A)$ và $F^{\top}$ PF là đối xứng xác định dương (SPD).
$(4)$ Tồn tại một đối xứng nửa xác định dương (positive semidefinite) ma trận $Q$ sao cho $P + A^{\top}QA$ là đối xứng xác định dương (SPD). Thực ra, $Q =$ I hoạt động. Chứng minh phác thảo. Nhắc lại từ Mệnh đề 6.19 rằng ma trận vuông (square matrix) $B$ là khả nghịch khi và chỉ khi hạt nhân (hạt nhân (kernel)) của nó là rút gọn đến ${0}$; tương đương, với mọi $x$, nếu Bx $= 0$, thì $x = 0$. Giả sử rằng Điều kiện $(1)$ nghiệm đúng. Ta có
$$\begin{pmatrix} P & A^{\top} \\ A & 0 \end{pmatrix} \begin{pmatrix} v \\ w \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
Khi và chỉ khi
$$Pv + A^{\top}w = 0,Av = 0.(*)$$
Ta suy ra rằng
$$v^{\top}Pv + v^{\top}A^{\top}w = 0,$$
Và vì
$$v^{\top}A^{\top}w = (Av)^{\top}w = 0w = 0,$$
Ta thu được $v^{\top}Pv = 0$. Vì Điều kiện $(1)$ nghiệm đúng, bởi vì $v \in$ Ker $A$, ta suy ra rằng $v = 0$. Thì $A^{\top}w = 0$, nhưng vì ma trận cỡ $m \times  n$ $A$ có hạng (rank) $m$, ma trận cỡ $n \times  m$ $A^{\top}$ cũng có hạng (rank) $m$, do đó các cột của nó là độc lập tuyến tính (linearly independent), và do đó $w = 0$. Vì vậy KKT-matrix là khả nghịch. Ngược lại, giả sử rằng KKT-matrix là khả nghịch, vẫn chưa các giả định của Điều kiện
$(1)$ thất bại. Điều này có nghĩa là tồn tại một $v \neq  0$ sao cho Av $= 0$ và $v^{\top}Pv = 0$. Ta khẳng định rằng Pv $= 0$. Điều này là bởi vì nếu $P$ là đối xứng nửa xác định dương (positive semidefinite) ma trận, thì với mọi $v$, ta có $v^{\top}Pv = 0$ khi và chỉ khi Pv $= 0$.

<!-- PAGE 1792 -->
Nếu Pv $= 0$, thì hiển nhiên $v^{\top}Pv = 0$, do đó giả sử điều ngược lại, cụ thể là $v^{\top}Pv = 0$. Vì $P$ là đối xứng nửa xác định dương (positive semidefinite) ma trận, nó có thể được được chéo hóa như
$$P = R^{\top}\Sigma R,$$
Ở đâu $R$ là ma trận trực giao (orthogonal matrix) và $\Sigma$ là ma trận đường chéo (diagonal matrix)
$$\Sigma  = \mathrm{diag}(\lambda_{1} , \dots  , \lambda_{s} , 0, \dots  , 0),$$
Ở đâu $s$ là hạng (rank) của $P$ và $\lambda_{1}  \ge \cdots  \ge \lambda_{s}  > 0$. Thì $v^{\top}Pv = 0$ là tương đương đến
$$v^{\top}R^{\top}\Sigma Rv = 0,$$
Tương đương
$$(Rv)^{\top}\Sigma Rv = 0.$$
Nếu ta viết Rv $= y$, thì ta có
$$0 = (Rv)^{\top}\Sigma Rv = y^{\top}\Sigma y = \sum_{i=1}^{s}  \lambda_{i} y_{i}^{2} ,$$
Và vì $\lambda_{i}  > 0$ cho $i = 1, \dots  , s$, điều này suy ra rằng $y_{i} = 0$ cho $i = 1, \dots  , s$. Hệ quả là, $\Sigma y = \Sigma$ Rv $= 0$, và do đó Pv $= R^{\top}\Sigma$ Rv $= 0$, như đã khẳng định. Vì $v \neq  0$, vectơ $(v, 0)$ là không tầm thường nghiệm của Các phương trình (*), một mâu thuẫn của tính khả nghịch giả định của KKT-matrix. Nhận thấy rằng ta được chứng minh rằng Av $= 0$ và Pv $= 0$ khi và chỉ khi Av $= 0$ và $v^{\top}Pv = 0$, do đó ta dễ dàng thu được sự kiện rằng Điều kiện $(2)$ là tương đương đến tính khả nghịch của KKT-matrix. Các phần
$(3)$ và $(4)$ là để lại như một bài tập. Đặc biệt, nếu $P$ là xác định dương (positive definite), thì Mệnh đề 50.11(4) áp dụng, như ta đã biết từ Mệnh đề 42.3. Trong trường hợp này, ta có thể giải cho $x$ bởi phép khử. Ta thu được
$$x = -P^{-1} (A^{\top}\lambda  + q),where\lambda  = -(AP^{-1} A^{\top})^{-1}(b + AP^{-1} q).$$
Trong thực tế, ta thực hiện không nghịch đảo $P$ và $AP^{-1} A^{\top}$. Thay vì, ta giải các hệ phương trình tuyến tính
$$Pz = q$$
$$PE = A^{\top}$$
$$(AE)\lambda  = -(b + Az)$$
$$Px = -(A^{\top}\lambda  + q).$$
Nhận thấy rằng $(AP^{-1}A^{\top})^{-1}$ là Phần bù Schur (Schur complement) của $P$ trong KKT ma trận. Vì KKT-matrix là đối xứng, nếu nó là khả nghịch, ta có thể chuyển đổi nó đến $LDL^{\top}$ tạo thành bằng cách sử dụng Mệnh đề 8.6. phương pháp này là chỉ thực tế khi bài toán là nhỏ hoặc khi $A$ và $P$ là thưa (sparse).

<!-- PAGE 1793 -->
Nếu KKT-matrix là khả nghịch nhưng $P$ là không, thì ta có thể sử dụng mẹo/kỹ thuật liên quan đến Mệnh đề 50.11. Ta tìm đối xứng nửa xác định dương (positive semidefinite) ma trận $Q$ sao cho $P +A^{\top}QA$ là đối xứng xác định dương (SPD), và vì nghiệm $(v, w)$ của KKT-system nên có Av $= b$, ta cũng có $A^{\top}QAv = A^{\top}Qb$, do đó KKT-system là tương đương đến
$$\begin{pmatrix} P+ A^{\top}QA & A^{\top} \\ A & 0 \end{pmatrix} \begin{pmatrix} v \\ w \end{pmatrix} = \begin{pmatrix} -q + A^{\top}Qb \\ b \end{pmatrix} ,$$
Và vì $P +A^{\top}QA$ là đối xứng xác định dương (SPD), ta có thể giải hệ này bởi phép khử. Một cái khác cách để giải Bài toán $(P)$ là để sử dụng các biến thể của Newton’s phương pháp như được mô tả trong Mục 49.9 dealing với đẳng thức các ràng buộc. Như vậy các phương pháp được thảo luận extensively trong Boyd và Vandenberghe $[29]$ (Chương $10$, Các mục 10.2-10.4). Có hai các biến thể của phương pháp này:
$(1)$ thứ nhất phương pháp, được gọi là chấp nhận được (feasible) bắt đầu Newton phương pháp, giả sử rằng bắt đầu điểm $u_{0}$ là chấp nhận được (feasible), mà có nghĩa là $Au_{0} = b$. Newton bước $d_{nt}$ là chấp nhận được (feasible) hướng, mà có nghĩa là $Ad_{nt} = 0$.
$(2)$ thứ hai phương pháp, được gọi là infeasible bắt đầu Newton phương pháp, thực hiện không giả sử rằng bắt đầu điểm $u_{0}$ là chấp nhận được (feasible), mà có nghĩa là $Au_{0} = b$ có thể không đúng. phương pháp này là little nhiều hơn/thêm phức tạp hơn khác phương pháp. Ta chỉ ngắn gọn thảo luận chấp nhận được (feasible) bắt đầu Newton phương pháp, để lại nó đến độc giả đến consult Boyd và Vandenberghe $[29]$ (Chương $10$, Mục 10.3) cho thảo luận của infeasible bắt đầu Newton phương pháp. Newton bước $d_{nt}$ là nghiệm của hệ phương trình tuyến tính
$$\begin{pmatrix} \nabla^{2} J(x) & A^{\top} \\ A & 0 \end{pmatrix} \begin{pmatrix} d_{nt} \\ w \end{pmatrix} = \begin{pmatrix} -\nabla J_{x} \\ 0 \end{pmatrix} .$$
Newton decrement $\lambda (x)$ được định nghĩa như trong Mục 49.9 như
$$.$$
$$\lambda (x) = (d_{nt}^{\top}\nabla^{2} J(x) d_{nt})^{1/2}= \begin{pmatrix} (\nabla J_{x})^{\top}(\nabla^{2} J(x))^{-1}\nabla \end{pmatrix} J_{x}^{1/2}$$
Newton’s phương pháp với đẳng thức các ràng buộc (với chấp nhận được (feasible) bắt đầu) bao gồm của sau đây các bước: Cho trước bắt đầu điểm $u_{0} \in$ dom(J) với $Au_{0} = b$, và tolerance $\epsilon  > 0$ thực hiện: repeat
$(1)$ Tính Newton bước và decrement $d_{nt,k} = -(\nabla^{2} J(u_{k}))^{-1}\nabla J_{uk}$ và $\lambda (u_{k})^{2} = (\nabla J_{uk})^{\top}(\nabla^{2} J(u_{k}))^{-1}\nabla J_{uk}$.
$(2)$ Stopping tiêu chuẩn. quit nếu $\lambda (u_{k})^{2}/2 \le \epsilon$.
$(3)$ Đường thẳng Search. Perform chính xác hoặc backtracking đường thẳng search để tìm $\rho_{k}$.
