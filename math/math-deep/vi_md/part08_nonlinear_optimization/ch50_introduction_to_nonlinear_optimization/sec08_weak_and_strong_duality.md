# Yếu và Đối ngẫu mạnh (strong duality)


<!-- PAGE 1816 -->
Của course, $sup_{\mu\in Rm} G(\mu$) và $sup_{(\mu ,\nu)\in Rm\times Rn} G(\mu , \nu$) là một cách tổng quát khác nhau, nhưng lưu ý rằng
$$b$$
$$+++$$
$$\mathbb{R}_{+}^{n}$$
$G(\mu$) $= G(\mu , \nu$) khi và chỉ khi tồn tại một $\nu  \in$ sao cho $A^{\top}\mu -\nu +c = 0$ khi và chỉ khi $A^{\top}\mu +c \ge 0$. Vì vậy, $b$ việc tìm $sup_{(\mu ,\nu)\in Rm\times Rn} G(\mu , \nu$) là tương đương đến có ràng buộc Bài toán $(D_{1})$
$$++$$
$$maximize-b^{\top}\mu$$
$$subject to A^{\top}\mu  \ge -c, \mu  \ge 0.$$
Ở trên bài toán là đối ngẫu (dual) của Bài toán quy hoạch tuyến tính (linear program) $(P)$. Trong tóm tắt, đối ngẫu (dual) hàm $G$ của sơ cấp Bài toán $(P)$ thường chứa hidden bất đẳng thức các ràng buộc rằng định nghĩa của nó miền xác định, và đôi khi nó là khả dĩ/có thể để tạo các phần tử này miền xác định các ràng buộc $\psi_{1} (\mu$) $\le 0, \dots  , \psi_{p} (\mu$) $\le 0$ tường minh, để định nghĩa mới hàm $G$ rằng phụ thuộc chỉ
$$b$$
Trên $q < m$ của các biến $\mu_{i}$ và được định nghĩa với mọi các giá trị $\mu_{i}  \ge 0$ của các phần tử này các biến, và đến thay thế Cực đại hóa Bài toán $(D)$, tìm $sup_{\mu\in Rm} G(\mu$), bởi có ràng buộc Bài toán
$$+$$
$(D_{1})$
$$maximizeG(\mu )$$
$$b$$
$$subject to \psi_{i} (\mu ) \le 0,i = 1, \dots  , p.$$
Bài toán $(D_{1})$ là khác nhau từ Đối ngẫu (dual) Bài toán quy hoạch $(D)$, nhưng nó là tương đương đến $(D)$ như cực đại hóa bài toán.

## 50.8 Yếu và Đối ngẫu mạnh (strong duality)

Một cái khác quan trọng tính chất của đối ngẫu (dual) hàm $G$ là rằng nó cung cấp thấp hơn cận trên giá trị của hàm mục tiêu (objective function) $J$. Thật vậy, ta có
$$G(\mu ) \le L(u, \mu ) \le J(u)for all u \in U and all \mu  \in \mathbb{R}_{+}^{m},(\dagger )$$
Vì $\mu  \ge 0$ và $\phi_{i} (u) \le 0$ cho $i = 1, \dots  , m$, do đó
$$G(\mu ) = vinf\in \Omega L(v, \mu ) \le L(u, \mu ) = J(u) + \sum_{i=1}^{m}  \mu_{i} \phi_{i} (u) \le J(u).$$
Nếu Bài toán gốc (primal problem) $(P)$ có cực tiểu được ký hiệu $p^{*}$ và Bài toán đối ngẫu (dual problem) $(D)$ có cực đại được ký hiệu $d^{*}$, thì ở trên bất đẳng thức suy ra rằng
$$d^{*}\le p^{*}(\dagger_{w} )$$
Đã biết như đối ngẫu yếu (weak duality). Tương đương, với mọi nghiệm tối ưu (optimal solution) $\lambda^{*}$ của bài toán đối ngẫu (dual problem) và mọi nghiệm tối ưu (optimal solution) $u^{*}$ của bài toán gốc (primal problem), ta có
$$G(\lambda^{*} ) \le J(u^{*}).(\dagger_{w'} )$$
Đặc biệt, nếu $p^{*} = -\infty$, mà có nghĩa là bài toán gốc (primal problem) là không bị chặn ở dưới, thì bài toán đối ngẫu (dual problem) là unfeasible. Ngược lại, nếu $d^{*} = +\infty$, mà có nghĩa là bài toán đối ngẫu (dual problem) là không bị chặn ở trên, thì bài toán gốc (primal problem) là unfeasible.

<!-- PAGE 1817 -->

> **Định nghĩa 50.10.** difference $p^{*}-d^{*} \ge 0$ được gọi là tối ưu khoảng cách đối ngẫu (duality gap). Nếu khoảng cách đối ngẫu (duality gap) là không, nghĩa là, $p^{*} = d^{*}$, thì ta nói rằng đối ngẫu mạnh (strong duality) nghiệm đúng. Chẵn/ngay cả khi khoảng cách đối ngẫu (duality gap) là chặt dương, bất đẳng thức $(\dagger_{w}$) có thể được helpful để tìm thấp hơn cận trên giá trị tối ưu (optimal value) của bài toán gốc (primal problem) rằng là khó để giải, vì bài toán đối ngẫu (dual problem) là luôn luôn lồi. Nếu bài toán gốc (primal problem) và bài toán đối ngẫu (dual problem) là chấp nhận được (feasible) và nếu tối ưu các giá trị $p^{*}$ và $d^{*}$ là hữu hạn và $p^{*} = d^{*}$ (không có khoảng cách đối ngẫu (duality gap)), thì độ bù lỏng (complementary slackness) các điều kiện đúng cho bất đẳng thức các ràng buộc.

> **Mệnh đề 50.16.** (Độ bù lỏng (complementary slackness)) Cho trước Cực tiểu hóa Bài toán $(P)$
$$minimizeJ(v)$$
$$subject to \phi_{i} (v) \le 0,i = 1, \dots  , m,$$
Và đối ngẫu (đối ngẫu (dual)) của nó Bài toán $(D)$
$$maximizeG(\mu )$$
$$subject to \mu  \in \mathbb{R}_{+}^{m},$$
Nếu cả hai $(P)$ và $(D)$ là chấp nhận được (feasible), $u \in U$ là nghiệm tối ưu (optimal solution) của $(P), \lambda  \in \mathbb{R}_{+}^{m}$ là nghiệm tối ưu (optimal solution) của $(D)$, và J(u) $= G(\lambda$), thì
$$\sum_{i=1}^{m}  \lambda_{i} \phi_{i} (u) = 0.$$
Nói cách khác, nếu ràng buộc $\phi_{i}$ là không hoạt động tại $u$, thì $\lambda_{i}  = 0$.

*Chứng minh.* Vì J(u) $= G(\lambda$) ta có J(u) $= G(\lambda$)
$$= infJ(v) + \sum_{i=1}^{m}  \lambda_{i} \phi_{i} (v)!by definition of G$$
$$v\in \Omega$$
$$\le J(u) + \sum_{i=1}^{m}  \lambda_{i} \phi_{i} (u)the greatest lower bound is a lower bound$$
$$\le J(u)since \lambda_{i}  \ge 0, \phi_{i} (u) \le 0.$$
$$which implies that \sum_{i}  m=1 \lambda_{i} \phi_{i} (u) = 0.$$
Đi quay lại đến Ví dụ 50.5, ta xem rằng đối ngẫu yếu (weak duality) nói rằng rằng với mọi nghiệm chấp nhận được (feasible solution)
$$\mathbb{R}^{n}$$
$u$ của Bài toán gốc (primal problem) $(P)$, nghĩa là, một số $u \in$ sao cho
$$Au \le b, u \ge 0,$$

<!-- PAGE 1818 -->
$$\mathbb{R}^{m}$$
Và với mọi nghiệm chấp nhận được (feasible solution) $\mu  \in$ của Bài toán đối ngẫu (dual problem) $(D_{1})$, nghĩa là,
$$A^{\top}\mu  \ge -c, \mu  \ge 0,$$
Ta có
$$-b^{\top}\mu  \le c^{\top}u.$$
Thực sự, nếu $u$ và $\lambda$ là tối ưu, thì ta biết từ Định lý 47.7 rằng đối ngẫu mạnh (strong duality) nghiệm đúng, cụ thể là $-b^{\top}\mu  = c^{\top}u$, nhưng chứng minh của sự kiện này là không tầm thường. sau đây định lý các thiết lập link giữa các nghiệm của Bài toán gốc (primal problem)
$(P)$ và những phần tử đó của Bài toán đối ngẫu (dual problem) $(D)$. Nó cũng cho đủ các điều kiện cho khoảng cách đối ngẫu (duality gap) là không.

> **Định lý 50.17.** Xét Cực tiểu hóa Bài toán $(P)$:
$$minimizeJ(v)$$
$$subject to \phi_{i} (v) \le 0,i = 1, \dots  , m,$$
Ở đâu các hàm $J$ và $\phi_{i}$ được định nghĩa trên một số mở tập con $\Omega$ của hữu hạn chiều Euclidean không gian vectơ (vector space) $V$ (tổng quát hơn, thực Không gian Hilbert (Hilbert space) $V$).
$(1)$ Giả sử các hàm $\phi_{i}$: $\Omega \to \mathbb{R}$ là liên tục, và rằng với mọi $\mu  \in \mathbb{R}_{+}^{m}$, Bài toán $(P_{\mu})$:
$$minimizeL(v, \mu )$$
$$subject to v \in \Omega ,$$
Có duy nhất nghiệm $u_{\mu}$, sao cho
$$L(u_{\mu}, \mu ) = infL(v, \mu ) = G(\mu ),$$
$$v\in \Omega$$
Và hàm $\mu  \mapsto u_{\mu}$ là liên tục (trên $\mathbb{R}_{+}^{m})$. Thì hàm $G$ là khả vi (differentiable) với mọi $\mu  \in \mathbb{R}_{+}^{m}$, và
$$G_{\mu}'(\xi ) = \sum_{i=1}^{m}  \xi_{i} \phi_{i} (u_{\mu})for all \xi  \in \mathbb{R}^{m}.$$
Nếu $\lambda$ là bất kỳ nghiệm của Bài toán $(D)$:
$$maximizeG(\mu )$$
$$subject to \mu  \in \mathbb{R}_{+}^{m},$$
Thì nghiệm $u_{\lambda}$ của tương ứng bài toán $(P_{\lambda})$ là nghiệm của Bài toán $(P)$.

<!-- PAGE 1819 -->
$(2)$ Giả sử Bài toán $(P)$ có một số nghiệm $u \in U$, và rằng $\Omega$ là lồi (mở), các hàm $\phi_{i}  (1 \le i \le m)$ và $J$ là lồi và khả vi (differentiable) tại $u$, và rằng các ràng buộc là qualified. Thì Bài toán $(D)$ có nghiệm $\lambda  \in \mathbb{R}_{+}^{m}$, và J(u) $= G(\lambda$); rằng là, khoảng cách đối ngẫu (duality gap) là không.

*Chứng minh.* $(1)$ Của ta mục tiêu là để chứng minh rằng với mọi nghiệm $\lambda$ của Bài toán $(D)$, cặp $(u_{\lambda}, \lambda$) là điểm yên ngựa (saddle point) của $L$. Theo Định lý 50.15(1), điểm $u_{\lambda} \in U$ là nghiệm của Bài toán $(P)$. Vì $\lambda  \in \mathbb{R}_{+}^{m}$ là nghiệm của Bài toán $(D)$, theo định nghĩa của $G(\lambda$) và vì $u_{\lambda}$ thỏa mãn Bài toán $(P_{\lambda})$, ta có
$$G(\lambda ) = infL(v, \lambda ) = L(u_{\lambda}, \lambda ),$$
$$v\in \Omega$$
Mà là một của hai các phương trình đặc trưng hóa điểm yên ngựa (saddle point). Trong thứ tự để chứng minh phương trình thứ hai đặc trưng hóa điểm yên ngựa (saddle point),
$$supL(u_{\mu}, \mu ) = L(u_{\lambda}, \lambda ),$$
$$\mu \in \mathbb{R} m$$
$$+$$
Ta sẽ bắt đầu bởi chứng minh rằng hàm $G$ là khả vi (differentiable) với mọi $\mu  \in \mathbb{R}_{+}^{m}$, trong thứ tự là able để áp dụng Định lý 40.9 để kết luận rằng vì $G$ có cực đại tại $\lambda$, nghĩa là, $-G$ có cực tiểu tại $\lambda$, thì $-G_{\lambda}'(\mu$ - $\lambda$) $\ge 0$ với mọi $\mu  \in \mathbb{R}_{+}^{m}$. Thực ra, ta chứng minh rằng
$$G_{\mu}'(\xi ) = \sum_{i=1}^{m}  \xi_{i} \phi_{i} (u_{\mu})for all \xi  \in \mathbb{R}^{m}.(*_{deriv})$$
Xét bất kỳ hai các điểm $\mu$ và $\mu  + \xi$ trong $\mathbb{R}_{+}^{m}$. Theo định nghĩa của $u_{\mu}$ ta có
$$L(u_{\mu}, \mu ) \le L(u_{\mu+\xi}, \mu ),$$
Mà có nghĩa là
$$J(u_{\mu}) + \sum_{i=1}^{m}  \mu_{i} \phi_{i} (u_{\mu}) \le J(u_{\mu+\xi}) + \sum_{i=1}^{m}  \mu_{i} \phi_{i} (u_{\mu+\xi}),(*_{1})$$
$$and since G(\mu ) = L(u_{\mu}, \mu ) = J(u_{\mu}) + \sum_{i}  m \mu_{i} \phi_{i} (u_{\mu}) and G(\mu  + \xi ) = L(u_{\mu+\xi}, \mu  + \xi ) =$$
$$J(u_{\mu+\xi}) + \sum_{i}  m=1(\mu_{i}  + \xi_{i} )\phi_{i} (u_{\mu+\xi}), we have^{=1}$$
$$G(\mu  + \xi ) -G(\mu ) = J(u_{\mu+\xi}) -J(u_{\mu}) + \sum_{i=1}^{m}  (\mu_{i}  + \xi_{i} )\phi_{i} (u_{\mu+\xi}) - \sum_{i=1}^{m}  \mu_{i} \phi_{i} (u_{\mu}).(*_{2})$$
Vì $(*_{1})$ có thể được viết dưới dạng
$$0 \le J(u_{\mu+\xi}) -J(u_{\mu}) + \sum_{i=1}^{m}  \mu_{i} \phi_{i} (u_{\mu+\xi}) - \sum_{i=1}^{m}  \mu_{i} \phi_{i} (u_{\mu}),$$

<!-- PAGE 1820 -->
$$by adding \sum_{i}  m=1 \xi_{i} \phi_{i} (u_{\mu+\xi}) to both sides of the above inequality and using (*_{2}) we get$$
$$\sum_{i=1}^{m}  \xi_{i} \phi_{i} (u_{\mu+\xi}) \le G(\mu  + \xi ) -G(\mu ).(*_{3})$$
Theo định nghĩa của $u_{\mu+\xi}$ ta có
$$L(u_{\mu+\xi}, \mu  + \xi ) \le L(u_{\mu}, \mu  + \xi ),$$
Mà có nghĩa là
$$J(u_{\mu+\xi}) + \sum_{i=1}^{m}  (\mu_{i}  + \xi_{i} )\phi_{i} (u_{\mu+\xi}) \le J(u_{\mu}) + \sum_{i=1}^{m}  (\mu_{i}  + \xi_{i} )\phi_{i} (u_{\mu}).(*_{4})$$
Điều này có thể được viết dưới dạng
$$J(u_{\mu+\xi}) -J(u_{\mu}) + \sum_{i=1}^{m}  (\mu_{i}  + \xi_{i} )\phi_{i} (u_{\mu+\xi}) - \sum_{i=1}^{m}  (\mu_{i}  + \xi_{i} )\phi_{i} (u_{\mu}) \le 0,$$
$$and by adding \sum_{i}  m=1 \xi_{i} \phi_{i} (u_{\mu}) to both sides of the above inequality and using (*_{2}) we get$$
$$G(\mu  + \xi ) -G(\mu ) \le \sum_{i=1}^{m}  \xi_{i} \phi_{i} (u_{\mu}).(*_{5})$$
Bởi đặt $(*_{3})$ và $(*_{5})$ cùng nhau ta thu được
$$\sum_{i=1}^{m}  \xi_{i} \phi_{i} (u_{\mu+\xi}) \le G(\mu  + \xi ) -G(\mu ) \le \sum_{i=1}^{m}  \xi_{i} \phi_{i} (u_{\mu}).(*_{6})$$
Hệ quả là tồn tại một $\theta  \in [0, 1]$ sao cho
$$G(\mu  + \xi ) -G(\mu ) = (1 -\theta ) \begin{pmatrix} \xi_{i} \phi_{i} (u_{\mu}) \end{pmatrix} \sum_{i=1}^{m}  + \theta \begin{pmatrix} \xi_{i} \phi_{i} (u_{\mu+\xi}) \end{pmatrix} \sum_{i=1}^{m}$$
$$= \sum_{i=1}^{m}  \xi_{i} \phi_{i} (u_{\mu}) + \theta \begin{pmatrix} \xi_{i} (\phi_{i} (u_{\mu+\xi}) -\phi_{i} (u_{\mu})) \end{pmatrix} \sum_{i=1}^{m}  .$$
Vì bởi giả thiết các hàm $\mu  \mapsto u_{\mu}$ (từ $\mathbb{R}_{+}^{m}$ đến $\Omega$) và $\phi_{i}$: $\Omega \to \mathbb{R}$ là liên tục, với mọi $\mu  \in \mathbb{R}_{+}^{m}$ ta có thể viết
$$G(\mu  + \xi ) -G(\mu ) = \sum_{i=1}^{m}  \xi_{i} \phi_{i} (u_{\mu}) + \|\xi \|\epsilon (\xi ),with lim_{\xi\mapsto0} \epsilon (\xi ) = 0,(*_{7})$$

<!-- PAGE 1821 -->
Với mọi $\|\|$ chuẩn (norm) trên $\mathbb{R}^{m}$. Phương trình $(*_{7})$ chỉ ra rằng $G$ là khả vi (differentiable) với mọi $\mu  \in \mathbb{R}_{+}^{m}$, và rằng
$$G_{\mu}'(\xi ) = \sum_{i=1}^{m}  \xi_{i} \phi_{i} (u_{\mu})for all \xi  \in \mathbb{R}^{m}.(*_{8})$$
Thực sự có một nhỏ bài toán, cụ thể là rằng khái niệm của đạo hàm đã được định nghĩa cho hàm được định nghĩa trên tập mở (open set), nhưng $\mathbb{R}_{+}^{m}$ là không mở. difficulty chỉ phát sinh để đảm bảo rằng đạo hàm là duy nhất, nhưng trong trường hợp của chúng ta ta có duy nhất biểu thức cho đạo hàm do đó không có bài toán như far như định nghĩa đạo hàm. Ở đó là vẫn potential bài toán, mà là rằng ta sẽ like để áp dụng Định lý 40.9 để kết luận rằng vì $G$ có cực đại tại $\lambda$, nghĩa là, $-G$ có cực tiểu tại $\lambda$, thì
$$-G_{\lambda}'(\mu  -\lambda ) \ge 0for all \mu  \in \mathbb{R}_{+}^{m},(*_{9})$$
Nhưng các giả thiết của Định lý 40.9 đòi hỏi miền xác định của hàm là mở. May mắn thay, close examination của chứng minh của Định lý 40.9 chỉ ra rằng chứng minh vẫn nghiệm đúng với $U =\mathbb{R}_{+}^{m}$. Vì vậy, $(*_{8})$ nghiệm đúng, Định lý 40.9 là hợp lệ, mà trong turn suy ra
$$G_{\lambda}'(\mu  -\lambda ) \le 0for all \mu  \in \mathbb{R}_{+}^{m},(*_{10})$$
Mà, bằng cách sử dụng biểu thức cho $G_{\lambda}'$ cho trước trong $(*_{8})$ cho
$$\sum_{i=1}^{m}  \mu_{i} \phi_{i} (u_{\lambda}) \le \sum_{i=1}^{m}  \lambda_{i} \phi_{i} (u_{\lambda}),for all \mu  \in \mathbb{R}_{+}^{m}.(*_{11})$$
Hệ quả là của $(*_{11})$, ta thu được
$$L(u_{\lambda}, \mu ) = J(u_{\lambda}) + \sum_{i=1}^{m}  \mu_{i} \phi_{i} (u_{\lambda})$$
$$\le J(u_{\lambda}) + \sum_{i=1}^{m}  \lambda_{i} \phi_{i} (u_{\lambda}) = L(u_{\lambda}, \lambda ),$$
Với mọi $\mu  \in \mathbb{R}_{+}^{m}$, nghĩa là,
$$L(u_{\lambda}, \mu ) \le L(u_{\lambda}, \lambda ),for all \mu  \in \mathbb{R}_{+}^{m},(*_{12})$$
Mà suy ra thứ hai bất đẳng thức
$$supL(u_{\mu}, \mu ) = L(u_{\lambda}, \lambda )$$
$$\mu \in \mathbb{R} m$$
$$+$$
Phát biểu rằng $(u_{\lambda}, \lambda$) là điểm yên ngựa (saddle point). Vì vậy, $(u_{\lambda}, \lambda$) là điểm yên ngựa (saddle point) của $L$, như đã khẳng định.
$(2)$ các giả thiết là chính xác những phần tử đó cần thiết theo Định lý 50.15(2), do đó tồn tại một $\lambda  \in \mathbb{R}_{+}^{m}$ sao cho $(u, \lambda$) là điểm yên ngựa (saddle point) của Hàm Lagrange (Lagrangian) $L$, và theo Định lý 50.15(1) ta có J(u) $=$ L(u, $\lambda$). Theo Mệnh đề 50.14, ta có
$$J(u) = L(u, \lambda ) = infL(v, \lambda ) = supinfL(v, \mu ),$$
$$v\in \Omega \mu \in \mathbb{R} mv\in \Omega$$
$$+$$

<!-- PAGE 1822 -->
Mà có thể được được viết lại như
$$J(u) = G(\lambda ) = supG(\mu ).$$
$$\mu \in \mathbb{R} m$$
$$+$$
Nói cách khác, Bài toán $(D)$ có nghiệm, và J(u) $= G(\lambda$).
Nhận xét: Lưu ý rằng Định lý 50.17(2) có thể có đã là thu được hệ quả là của Định lý 50.15(2), nhưng đối ngẫu (dual) hàm $G$ đã là không vẫn chưa được định nghĩa. Nếu $(u, \lambda$) là điểm yên ngựa (saddle point) của Hàm Lagrange (Lagrangian) $L$ (được định nghĩa trên $\Omega \times \mathbb{R}_{+}^{m})$, thì theo Mệnh đề 50.14, vectơ $\lambda$ là nghiệm của Bài toán $(D)$. Ngược lại, dưới các giả thiết của Phần $(1)$ của Định lý 50.17, nếu $\lambda$ là nghiệm của Bài toán $(D)$, thì $(u_{\lambda}, \lambda$) là điểm yên ngựa (saddle point) của $L$. Hệ quả là, dưới ở trên các giả thiết, tập hợp của các nghiệm của Bài toán đối ngẫu (dual problem) $(D)$ trùng nhau với tập hợp của thứ hai các đối số/lập luận $\lambda$ của saddle các điểm $(u, \lambda$) của $L$. Trong một số nghĩa, kết quả này là “đối ngẫu (dual)” của kết quả được phát biểu trong Định lý 50.15, cụ thể là rằng tập hợp của các nghiệm của Bài toán $(P)$ trùng với với tập hợp của thứ nhất các đối số/lập luận $u$ của saddle các điểm $(u, \lambda$) của $L$. Một cách trực quan, trong Định lý 50.17(1), các giả thiết nói rằng nếu $G(\mu$) có thể được “được tính một cách đẹp,” trong nghĩa rằng tồn tại duy nhất một điểm cực tiểu hóa $u_{\mu}$ của L(v, $\mu$) (với $v \in \Omega$) sao cho $G(\mu$) $= L(u_{\mu}, \mu$), và nếu maximizer $\lambda$ của $G(\mu$) (với $\mu  \in \mathbb{R}_{+}^{m})$ có thể được được xác định, thì $u_{\lambda}$ cho ta cực tiểu giá trị của $J$, nghĩa là, $p^{*} = J(u_{\lambda})$. Nếu các ràng buộc là qualified và nếu các hàm $J$ và $\phi_{i}$ là lồi và khả vi (differentiable), khi đó vì KKT các điều kiện đúng, khoảng cách đối ngẫu (duality gap) là zero; nghĩa là,
$$G(\lambda ) = L(u_{\lambda}, \lambda ) = J(u_{\lambda}).$$

> **Ví dụ 50.6.** Đi quay lại đến Ví dụ 50.5 ở đâu ta được xét bài toán quy hoạch tuyến tính (linear program) $(P)$
$$minimizec^{\top}v$$
$$subject to Av \le b, v \ge 0,$$
Với $A$ một ma trận cỡ $m \times  n$, Hàm Lagrange (Lagrangian) L(v, $\mu , \nu$) được cho bởi
$$L(v, \mu , \nu ) = -b^{\top}\mu  + (c + A^{\top}\mu  -\nu )^{\top}v,$$
Và ta tìm thấy rằng đối ngẫu (dual) hàm $G(\mu , \nu$) $= inf_{v\in Rn}$ L(v, $\mu , \nu$) là cho trước với mọi $\mu  \ge 0$ và $\nu  \ge 0$ bởi
$$($$
$$-b^{\top}\mu if A^{\top}\mu  -\nu  + c = 0,$$
$$G(\mu , \nu ) =$$
$$-\infty otherwise.$$
$$\mathbb{R}^{n}$$
Các giả thiết của Định lý 50.17(1) một cách nhất định thất bại vì có một cách vô hạn $u_{\mu ,\nu} \in$ sao cho $G(\mu , \nu$) $= inf_{v\in Rn}$ L(v, $\mu , \nu$) $= L(u_{\mu ,\nu}, \mu , \nu$). Vì vậy, đối ngẫu (dual) hàm $G$ là không có help trong việc tìm nghiệm của Bài toán gốc (primal problem) $(P)$. Như ta đã thấy trước đó, nếu ta xét được sửa đổi bài toán đối ngẫu (dual problem) $(D_{1})$ thì đối ngẫu mạnh (strong duality) nghiệm đúng, nhưng điều này thực hiện không suy ra từ Định lý 50.17, và khác nhau chứng minh là cần thiết.

<!-- PAGE 1823 -->
Do đó, ta có somewhat counter-intuitive tình huống rằng tổng quát lý thuyết của Lagrange đối ngẫu thực hiện không áp dụng, ít nhất một cách trực tiếp, đến quy hoạch tuyến tính (linear programming), sự kiện rằng là không một cách đủ emphasized trong nhiều các trình bày. tách treatment của đối ngẫu là cần thiết. Unlike trường hợp của quy hoạch tuyến tính (linear programming), mà cần tách treatment, Định lý 50.17 áp dụng đến tối ưu hóa bài toán liên quan đến lồi toàn phương hàm mục tiêu (objective function) và tập hợp của afin bất đẳng thức các ràng buộc. Do đó trong một số nghĩa, lồi toàn phương quy hoạch là đơn giản hơn hơn quy hoạch tuyến tính (linear programming)!

> **Ví dụ 50.7.** Xét toàn phương hàm mục tiêu (objective function)
$$J(v) = \frac{1}{2} v^{\top}Av -v^{\top}b,$$
Ở đâu $A$ là một ma trận cỡ $n \times  n$ mà là đối xứng xác định dương (SPD), $b \in \mathbb{R}^{n}$, và các ràng buộc là afin bất đẳng thức các ràng buộc của tạo thành
$$Cv \le d,$$
Ở đâu $C$ là một ma trận cỡ $m \times  n$ và $d \in \mathbb{R}^{m}$. Cho time đang là, ta thực hiện không giả sử rằng $C$ có hạng (rank) $m$. Vì $A$ là đối xứng xác định dương (SPD), $J$ là lồi chặt (strictly convex), như được suy ra theo Mệnh đề 40.11 (xem Ví dụ 40.6). Hàm Lagrange (Lagrangian) của điều này tối ưu hóa toàn phương (quadratic optimization) bài toán được cho bởi
$$L(v, \mu ) = \frac{1}{2} v^{\top}Av -v^{\top}b + (Cv -d)^{\top}\mu$$
$$= \frac{1}{2} v^{\top}Av -v^{\top}(b -C^{\top}\mu ) -\mu^{\top} d.$$
Vì $A$ là đối xứng xác định dương (SPD), theo Mệnh đề 42.2, hàm $v \mapsto$ L(v, $\mu$) có duy nhất cực tiểu thu được cho nghiệm $u_{\mu}$ của hệ phương trình tuyến tính
$$Av = b -C^{\top}\mu ;$$
Rằng là,
$$u_{\mu} = A^{-1}(b -C^{\top}\mu ).$$
Điều này chỉ ra rằng Bài toán $(P_{\mu})$ có duy nhất nghiệm mà phụ thuộc một cách liên tục trên $\mu$. Thì với mọi nghiệm $\lambda$ của bài toán đối ngẫu (dual problem), $u_{\lambda} = A^{-1}(b$ - $C^{\top}\lambda$) là nghiệm tối ưu (optimal solution) của bài toán gốc (primal problem).

<!-- PAGE 1824 -->
Ta tính $G(\mu$) như sau:
$$G(\mu ) = L(u_{\mu}, \mu ) = \frac{1}{2} u_{\mu}^{\top} Au_{\mu} -u_{\mu}^{\top} (b -C^{\top}\mu ) -\mu^{\top} d$$
$$= \frac{1}{2} u_{\mu}^{\top} (b -C^{\top}\mu ) -u_{\mu}^{\top} (b -C^{\top}\mu ) -\mu^{\top} d$$
$$= - \frac{1}{2} u_{\mu}^{\top} (b -C^{\top}\mu ) -\mu^{\top} d$$
$$= - \frac{1}{2} (b -C^{\top}\mu )^{\top}A^{-1}(b -C^{\top}\mu ) -\mu^{\top} d$$
$$= - \frac{1}{2} \mu^{\top} CA^{-1}C^{\top}\mu  + \mu^{\top} (CA^{-1}b -d) - \frac{1}{2} b^{\top}A^{-1}b.$$
Vì $A$ là đối xứng xác định dương (SPD), ma trận $CA^{-1}C^{\top}$ là đối xứng nửa xác định dương (positive semidefinite). Vì $A^{-1}$ là cũng đối xứng xác định dương (SPD), $\mu^{\top} CA^{-1}C^{\top}\mu  = 0 iff(C^{\top}\mu )^{\top}A^{-1}(C^{\top}\mu$) $= 0$ khi và chỉ khi $C^{\top}\mu  = 0$ suy ra $\mu  = 0$, nghĩa là, Ker $C^{\top} = (0)$, mà là tương đương đến Im(C) $= \mathbb{R}^{m}$, cụ thể là nếu $C$ có hạng (rank) $m$ (trong mà trường hợp, $m \le n)$. Do đó $CA^{-1}C^{\top}$ là đối xứng xác định dương (SPD) khi và chỉ khi $C$ có hạng (rank) $m$. Ta đã chỉ ra chỉ sau Định lý 49.8 rằng phiếm hàm $v \mapsto (1/2)v^{\top}Av$ là elliptic khi và chỉ khi $A$ là đối xứng xác định dương (SPD), và Định lý 49.8 chỉ ra rằng elliptic phiếm hàm là bức (coercive), mà là giả thiết được sử dụng trong Định lý 49.4. Vì vậy, theo Định lý 49.4, nếu các bất đẳng thức Cx $\le d$ có nghiệm, bài toán gốc (primal problem) có duy nhất nghiệm. Trong trường hợp này, hệ quả là, theo Định lý 50.17(2), hàm $-G(\mu$) luôn luôn có cực tiểu, mà là duy nhất nếu $C$ có hạng (rank) $m$. sự kiện rằng $-G(\mu$) có cực tiểu là không hiển nhiên khi $C$ có hạng (rank) $< m$, vì trong điều này trường hợp $CA^{-1}C^{\top}$ là không khả nghịch. Ta cũng kiểm chứng dễ dàng rằng gradien của $G$ được cho bởi
$$\nabla G_{\mu} = Cu_{\mu} -d = -CA^{-1}C^{\top}\mu  + CA^{-1}b -d.$$
Nhận thấy rằng vì $CA^{-1}C^{\top}$ là đối xứng nửa xác định dương (positive semidefinite), $-G(\mu$) là lồi. Vì vậy, nếu $C$ có hạng (rank) $m$, nghiệm của Bài toán $(P)$ là thu được bởi việc tìm duy nhất nghiệm $\lambda$ của phương trình
$$-CA^{-1}C^{\top}\mu  + CA^{-1}b -d = 0,$$
Và thì cực tiểu $u_{\lambda}$ của Bài toán $(P)$ được cho bởi
$$u_{\lambda} = A^{-1}(b -C^{\top}\lambda ).$$
Nếu $C$ có hạng (rank) $< m$, thì ta có thể tìm $\lambda  \ge 0$ bởi việc tìm nghiệm chấp nhận được (feasible solution) của bài toán quy hoạch tuyến tính (linear program) có tập hợp của các ràng buộc được cho bởi
$$-CA^{-1}C^{\top}\mu  + CA^{-1}b -d = 0,$$
Bằng cách sử dụng tiêu chuẩn phương pháp của cộng không âm bù/lỏng các biến $\xi_{1} , \dots  , \xi_{m}$ và cực đại hóa $-(\xi_{1}  + \cdots  + \xi_{m}$).
