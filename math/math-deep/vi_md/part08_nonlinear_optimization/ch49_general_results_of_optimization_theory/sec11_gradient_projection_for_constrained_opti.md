# Gradien Phép chiếu cho Có ràng buộc Tối ưu hóa


<!-- PAGE 1752 -->
Phương pháp của liên hợp các gradien có thể được suy rộng/tổng quát hóa đến các phiếm hàm rằng là không nhất thiết toàn phương. bước nhảy (stepsize) tham số $\rho_{k}$ là vẫn được xác định bởi đường thẳng search mà bao gồm trong việc tìm $\rho_{k}$ sao cho
$$J(u_{k} -\rho_{k} d_{k}) = \inf J(u_{k} -\rho d_{k}).$$
$$\rho \in \mathbb{R}$$
Điều này là nhiều hơn/thêm khó hơn trong toàn phương trường hợp và nói chung không có đảm bảo rằng $\rho_{k}$ là duy nhất, do đó một số tiêu chuẩn đến chọn $\rho_{k}$ là cần thiết. Thì
$$u_{k+1} = u_{k} -\rho_{k} d_{k},$$
Và tiếp theo descent hướng có thể được được chọn trong hai các cách:
$(1)$ (Polak–Ribi`ere)
$$\langle \nabla  \nabla  -\nabla \rangle$$
$$d_{k} = \nabla J_{uk} + \frac{J_{uk},J_{uk}J_{uk-1}}{\nabla J_{uk-1}^{2}} d_{k-1},$$
$(2)$ (Fletcher–Reeves)
$$\|\nabla \|^{2}$$
$$d_{k} = \nabla J_{uk} + \frac{J_{uk}}{\nabla J_{uk-1}^{2}} d_{k-1}.$$
Liên tiếp các gradien là không có dài hơn trực giao do đó các phương pháp này có thể chạy forever. Có khác nhau đủ các tiêu chuẩn cho sự hội tụ. Trong thực tế, Polak–Ribi`ere phương pháp hội tụ faster. Không có dài hơn bất kỳ đảm bảo rằng các phương pháp này hội tụ đến cực tiểu toàn cục (global minimum).

## 49.11 Gradien Phép chiếu Các phương pháp cho Có ràng buộc

$$Optimization$$
Ta bây giờ xét bài toán của việc tìm cực tiểu của lồi phiếm hàm $J$: $V \to \mathbb{R}$ trên khác rỗng, lồi, đóng tập con $U$ của Không gian Hilbert (Hilbert space) $V$. Theo Định lý 40.13(3), phiếm hàm $J$ có cực tiểu tại $u \in U$ khi và chỉ khi
$$dJ_{u}(v -u) \ge 0for all v \in U,$$
Mà có thể được biểu diễn dưới dạng
$$\langle \nabla J_{u}, v -u\rangle \ge 0for all v \in U.$$
Mặt khác, bởi phép chiếu bổ đề (Mệnh đề 48.5), điều kiện cho vectơ $u \in U$ là phép chiếu của phần tử $w \in V$ lên $U$ là
$$\langle u -w, v -u\rangle \ge 0for all v \in U.$$

<!-- PAGE 1753 -->
Các điều kiện này là hiển nhiên tương tự, và ta có thể tạo điều này analogy nhiều hơn/thêm precise như sau. Nếu $p_{U}$: $V \to U$ là phép chiếu ánh xạ lên $U$, ta có kết quả sau dây chuyền/xích của equivalences: $u \in U$ và J(u) $=$ inf J(v) khi và chỉ khi
$$v\in U$$
$u \in U$ và $\langle \nabla J_{u}, v$ - $u\rangle \ge 0$ với mọi $v \in U$, khi và chỉ khi $u \in U$ và $\langle u$ - $(u$ - $\rho \nabla J_{u}), v$ - $u\rangle \ge 0$ với mọi $v \in U$ và mọi $\rho  > 0$, khi và chỉ khi $u = p_{U}(u$ - $\rho \nabla J_{u})$ với mọi $\rho  > 0$. Nói cách khác, với mọi $\rho  > 0, u \in V$ là fixed-point của hàm $g: V \to U$ cho trước bởi
$$g(v) = p_{U}(v -\rho \nabla J_{v}).$$
Ở trên suggests việc tìm $u$ bởi phương pháp của successive các xấp xỉ cho việc tìm fixed-point của contracting ánh xạ, cụ thể là cho trước bất kỳ ban đầu $u_{0} \in V$, để định nghĩa dãy $(u_{k})_{k\ge0}$ sao cho
$$u_{k+1} = p_{U}(u_{k} -\rho_{k} \nabla J_{uk}),$$
Ở đâu tham số $\rho_{k}  > 0$ được chọn tại mỗi bước. phương pháp này được gọi là projectedgradient phương pháp với biến bước nhảy (stepsize) tham số. Nhận thấy rằng nếu $U = V$, thì điều này là chỉ gradien phương pháp với biến bước nhảy (stepsize). Ta có kết quả sau kết quả về sự hội tụ của phương pháp này.

> **Mệnh đề 49.18.** Cho $J$: $V \to \mathbb{R}$ là một cách liên tục khả vi (differentiable) phiếm hàm được định nghĩa trên Không gian Hilbert (Hilbert space) $V$, và cho $U$ là khác rỗng, lồi, đóng tập con của $V$. Giả sử tồn tại hai các hằng số $\alpha  > 0$ và $M > 0$ sao cho
$$\langle \nabla J_{v} -\nabla J_{u}, v -u\rangle \ge \alpha  \|v -u\|^{2}for all u, v \in V ,$$
Và
$$\|\nabla J_{v} -\nabla J_{u}\|\le M \|v -u\|for all u, v \in V .$$
Nếu tồn tại hai thực nunbers, $b \in \mathbb{R}$ sao cho
$$0 < a \le \rho_{k}  \le b \le \frac{2\alpha}{M^{2}} for all k \ge 0,$$
Thì projected-gradient phương pháp với biến bước nhảy (stepsize) tham số hội tụ. Hơn nữa, tồn tại một hằng số $\beta  > 0$ (tùy thuộc trên $\alpha , M$,, $b)$ sao cho
$$\beta  < 1and\|u_{k} -u\|\le \beta^{k} \|u_{0} -u\|,$$
Ở đâu $u \in M$ là duy nhất cực tiểu của $J$.

<!-- PAGE 1754 -->

*Chứng minh.* Với mọi $\rho_{k}  \ge 0$, định nghĩa hàm $g_{k}$: $V \to U$ bởi
$$g_{k}(v) = p_{U}(v -\rho_{k} \nabla J_{v}).$$
Theo Mệnh đề 48.6, phép chiếu ánh xạ $p_{U}$ có Lipschitz hằng số $1$, do đó bằng cách sử dụng các bất đẳng thức được giả sử đến đúng trong mệnh đề, ta có $\|g_{k}(v_{1})$ - $g_{k}(v_{2})\|^{2} = \|p_{U}(v_{1}$ - $\rho_{k} \nabla J_{v1})$ - $p_{U}(v_{2}$ - $\rho_{k} \nabla J_{v2})\|^{2}$
$$\le \|(v_{1} -v_{2}) -\rho_{k} (\nabla J_{v1} -\nabla J_{v2})\|^{2}$$
$$= \|v_{1} -v_{2}\|^{2}-2\rho_{k} \langle \nabla J_{v1} -\nabla J_{v2}, v_{1} -v_{2}\rangle + \rho_{k}^{2}  \|\nabla J_{v1} -\nabla J_{v2}\|^{2}$$
$$\le \begin{pmatrix} 1 -2\alpha \rho_{k}  + M^{2}\rho_{k}^{2} \end{pmatrix} \|v_{1} -v_{2}\|^{2}.$$
Như trong chứng minh của Mệnh đề 49.14, ta biết rằng nếu và $b$ thỏa mãn các điều kiện $0 < a \le \rho_{k}  \le b \le_{M2}^{2\alpha}$, thì tồn tại một $\beta$ sao cho
$$\begin{pmatrix} 1 -2\alpha \rho_{k}  + M^{2} \end{pmatrix} \rho_{k}^{21/2} \le \beta  < 1for all k \ge 0.$$
Vì cực tiểu hóa điểm $u \in U$ là cố định điểm của $g_{k}$ với mọi $k$, bởi đặt $v_{1} = u_{k}$ và $v_{2} = u$, ta thu được
$$\|u_{k+1} -u\|= \|g_{k}(u_{k}) -g_{k}(u)\|\le \beta  \|u_{k} -u\|,$$
Mà chứng minh sự hội tụ của dãy $(u_{k})_{k\ge0}$. Trong trường hợp của elliptic toàn phương phiếm hàm
$$J(v) = \frac{1}{2} \langle Av, a\rangle -\langle b, v\rangle$$
Được định nghĩa trên $\mathbb{R}^{n}$, lập luận chỉ sau chứng minh của Mệnh đề 49.14 có thể được ngay lập tức được điều chỉnh để chỉ ra rằng sự hội tụ lấy place như dài như, $b$ và $\rho_{k}$ được chọn sao cho
$$0 < a \le \rho_{k}  \le b \le \frac{2}{\lambda_{n}} .$$
Trong lý thuyết, Mệnh đề 49.18 cho đảm bảo của sự hội tụ của projected-gradient phương pháp. Không may là, bởi vì việc tính toán phép chiếu $p_{U}(v)$ effectively là một cách tổng quát không thể, miền giá trị (range) của thực tế các ứng dụng của Mệnh đề 49.18 là khá được giới hạn. Một
$$exception is the case where U is a product \prod_{i}  m[a_{i}, b_{i}] of closed intervals (where a_{i} = -\infty$$
Hoặc $b_{i} = +\infty$ là khả dĩ/có thể). Trong trường hợp này, nó là $not^{=1}$ khó để chỉ ra rằng
$$a_{i}if w_{i} < a_{i}$$
$$$$
$$$$
$$p_{U}(w)_{i} =w_{i}if a_{i} \le w_{i} \le b_{i}$$
$$b_{i}if b_{i} < w_{i}.$$
$$$$
