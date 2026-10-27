# Handling Đẳng thức Các ràng buộc một cách tường minh


<!-- PAGE 1825 -->

## 50.9 Handling Đẳng thức Các ràng buộc một cách tường minh

Đôi khi nó là desirable đến handle đẳng thức các ràng buộc một cách tường minh (chẳng hạn, điều này là những gì Boyd và Vandenberghe thực hiện, xem $[29])$. chỉ difference là rằng Các nhân tử Lagrange (Lagrange multipliers) liên kết với đẳng thức các ràng buộc là không cần thiết là không âm, như ta bây giờ chỉ ra. Xét Tối ưu hóa Bài toán (P')
$$minimizeJ(v)$$
$$subject to \phi_{i} (v) \le 0,i = 1, \dots  , m$$
$$\psi_{j} (v) = 0,j = 1, \dots  , p.$$
Ta treat mỗi đẳng thức ràng buộc $\psi_{j} (u) = 0$ như conjunction của các bất đẳng thức $\psi_{j} (u) \le 0$ và $-\psi_{j} (u) \le 0$, và ta associate Các nhân tử Lagrange (Lagrange multipliers) $\lambda  \in \mathbb{R}_{+}^{m}$, và $\nu^{+} , \nu^{-} \in \mathbb{R}_{+}^{p}$. Giả sử rằng các ràng buộc là qualified, theo Định lý 50.5, KKT các điều kiện là
$$J_{u}' + \sum_{i=1}^{m}  \lambda_{i} (\phi_{i}' )_{u} + \sum_{j=1}^{p}  \nu_{j}^{+}  (\psi_{j}' )_{u} - \sum_{j=1}^{p}  \nu_{j}^{-}  (\psi_{j}' )_{u} = 0,$$
Và
$$\sum_{i=1}^{m}  \lambda_{i} \phi_{i} (u) + \sum_{j=1}^{p}  \nu_{j}^{+}  \psi_{j} (u) - \sum_{j=1}^{p}  \nu_{j}^{-}  \psi_{j} (u) = 0,$$
Với $\lambda  \ge 0, \nu^{+} \ge 0, \nu^{-} \ge 0$. Vì $\psi_{j} (u) = 0$ cho $j = 1, \dots  , p$, các phương trình này có thể được được viết lại như
$$J_{u}' + \sum_{i=1}^{m}  \lambda_{i} (\phi_{i}' )_{u} + \sum_{j=1}^{p}  (\nu_{j}^{+}  -\nu_{j}^{-}  )(\psi_{j}' )_{u} = 0,$$
Và
$$\sum_{i=1}^{m}  \lambda_{i} \phi_{i} (u) = 0$$
Với $\lambda  \ge 0, \nu^{+} \ge 0, \nu^{-} \ge 0$, và nếu ta giới thiệu $\nu_{j}  = \nu_{j}^{+}$ - $\nu_{j}^{-}$ ta thu được kết quả sau KKT các điều kiện cho các bài toán quy hoạch với tường minh đẳng thức các ràng buộc:
$$J_{u}' + \sum_{i=1}^{m}  \lambda_{i} (\phi_{i}' )_{u} + \sum_{j=1}^{p}  \nu_{j} (\psi_{j}' )_{u} = 0,$$
Và
$$\sum_{i=1}^{m}  \lambda_{i} \phi_{i} (u) = 0$$
$$\mathbb{R}^{p}$$
Với $\lambda  \ge 0$ và $\nu  \in$ tùy ý.

<!-- PAGE 1826 -->
Bây giờ ta giả sử rằng các hàm $\phi_{i}$ và $\psi_{j}$ là lồi. Như ta được giải thích chỉ sau Định nghĩa 50.6, nonaffine đẳng thức các ràng buộc là không bao giờ qualified. Do đó, trong thứ tự đến tổng quát hóa Định lý 50.6 đến tường minh đẳng thức các ràng buộc, ta giả sử rằng đẳng thức các ràng buộc $\psi_{j}$ là afin.

> **Định lý 50.18.** Cho $\phi_{i}$: $\Omega \to \mathbb{R}$ là $m$ lồi bất đẳng thức các ràng buộc và $\psi_{j}$: $\Omega \to \mathbb{R}$ là $p$ afin đẳng thức các ràng buộc được định nghĩa trên một số mở lồi tập con $\Omega$ của hữu hạn chiều Euclidean không gian vectơ (vector space) $V$ (tổng quát hơn, thực Không gian Hilbert (Hilbert space) $V$), cho $J$: $\Omega \to \mathbb{R}$ là một số hàm, cho $U$ là cho trước bởi
$$U = {x \in \Omega | \phi_{i} (x) \le 0, \psi_{j} (x) = 0, 1 \le i \le m, 1 \le j \le p},$$
Và cho $u \in U$ là bất kỳ điểm sao cho các hàm $\phi_{i}$ và $J$ là khả vi (differentiable) tại $u$.
$(1)$ Nếu $J$ có cực tiểu địa phương (local minimum) tại $u$ đối với $U$, và nếu các ràng buộc là qualified, thì ở đó tồn tại một số các vectơ $\lambda  \in \mathbb{R}_{+}^{m}$ và $\nu  \in \mathbb{R}^{p}$, sao cho KKT điều kiện đúng:
$$J_{u}' + \sum_{i=1}^{m}  \lambda_{i} (u)(\phi_{i}' )_{u} + \sum_{j=1}^{p}  \nu_{j} (\psi_{j}' )_{u} = 0,$$
Và
$$\sum_{i=1}^{m}  \lambda_{i} (u)\phi_{i} (u) = 0,\lambda_{i}  \ge 0,i = 1, \dots  , m.$$
Tương đương, theo các gradien, ở trên các điều kiện được biểu diễn như
$$\nabla J_{u} + \sum_{i=1}^{m}  \lambda_{i} \nabla (\phi_{i} )_{u} + \sum_{j=1}^{p}  \nu_{j} \nabla (\psi_{j} )_{u} = 0$$
Và
$$\sum_{i=1}^{m}  \lambda_{i} (u)\phi_{i} (u) = 0,\lambda_{i}  \ge 0,i = 1, \dots  , m.$$
$(2)$ Ngược lại, nếu thu hẹp của $J$ đến $U$ là lồi và nếu ở đó tồn tại các vectơ $\lambda  \in \mathbb{R}_{+}^{m}$ và
$$\mathbb{R}^{p}$$
$\nu  \in$ sao cho KKT các điều kiện đúng, thì hàm $J$ có (toàn cục) cực tiểu tại $u$ đối với $U$. Hàm Lagrange (Lagrangian) L(v, $\lambda , \nu$) của Bài toán (P') được định nghĩa như
$$L(v, \mu , \nu ) = J(v) + \sum_{i=1}^{m}  \mu_{i} \phi_{i} (v) + \sum_{j=1}^{p}  \nu_{i} \psi_{j} (v),$$
Ở đâu $v \in \Omega , \mu  \in \mathbb{R}_{+}^{m}$, và $\nu  \in \mathbb{R}^{p}$.

<!-- PAGE 1827 -->
$$\mathbb{R}_{+}^{m}\mathbb{R}^{p} \mathbb{R}$$
Hàm $G:  \times \to$ cho trước bởi
$$G(\mu , \nu ) = infL(v, \mu , \nu )\mu  \in \mathbb{R}_{+}^{m}, \nu  \in \mathbb{R}^{p}$$
$$v\in \Omega$$
Được gọi là Lagrange đối ngẫu (dual) hàm (hoặc đối ngẫu (dual) hàm), và Bài toán đối ngẫu (dual problem) (D') là
$$maximizeG(\mu , \nu )$$
$$subject to \mu  \in \mathbb{R}_{+}^{m}, \nu  \in \mathbb{R}^{p}.$$
Nhận thấy rằng Các nhân tử Lagrange (Lagrange multipliers) $\nu$ là không bị thu hẹp là không âm. Định lý 50.15 và Định lý 50.17 là ngay lập tức suy rộng/tổng quát hóa đến Bài toán (P'). Ta chỉ phát biểu mới phiên bản của 50.17, để lại mới phiên bản của Định lý 50.15 như một bài tập.

> **Định lý 50.19.** Xét cực tiểu hóa bài toán (P'):
$$minimizeJ(v)$$
$$subject to \phi_{i} (v) \le 0,i = 1, \dots  , m$$
$$\psi_{j} (v) = 0,j = 1, \dots  , p.$$
Ở đâu các hàm $J, \phi_{i}$ được định nghĩa trên một số mở tập con $\Omega$ của hữu hạn chiều Euclidean không gian vectơ (vector space) $V$ (tổng quát hơn, thực Không gian Hilbert (Hilbert space) $V$), và các hàm $\psi_{j}$ là afin.
$(1)$ Giả sử các hàm $\phi_{i}$: $\Omega \to \mathbb{R}$ là liên tục, và rằng với mọi $\mu  \in \mathbb{R}_{+}^{m}$ và mọi $\nu  \in \mathbb{R}^{p}$, Bài toán $(P_{\mu ,\nu})$:
$$minimizeL(v, \mu , \nu )$$
$$subject to v \in \Omega ,$$
Có duy nhất nghiệm $u_{\mu ,\nu}$, sao cho
$$L(u_{\mu ,\nu}, \mu , \nu ) = infL(v, \mu , \nu ) = G(\mu , \nu ),$$
$$v\in \Omega$$
Và hàm $(\mu , \nu$) $\mapsto u_{\mu ,\nu}$ là liên tục (trên $\mathbb{R}_{+}^{m} \times \mathbb{R}^{p})$. Thì hàm $G$ là khả vi (differentiable) với mọi $\mu  \in \mathbb{R}_{+}^{m}$ và tất cả $\nu  \in \mathbb{R}^{p}$, và
$$\mathbb{R}^{m} \mathbb{R}^{p}$$
$$G_{\mu ,\nu}'(\xi , \zeta ) = \sum_{i=1}^{m}  \xi_{i} \phi_{i} (u_{\mu ,\nu}) + \sum_{j=1}^{p}  \zeta_{j} \psi_{j} (u_{\mu ,\nu})for all \xi  \in and all \zeta  \in .$$
Nếu $(\lambda , \eta$) là bất kỳ nghiệm của Bài toán $(D)$:
$$maximizeG(\mu , \nu )$$
$$subject to \mu  \in \mathbb{R}_{+}^{m}, \nu  \in \mathbb{R}^{p},$$
Thì nghiệm $u_{\lambda ,\eta}$ của tương ứng Bài toán $(P_{\lambda ,\eta})$ là nghiệm của Bài toán (P').
