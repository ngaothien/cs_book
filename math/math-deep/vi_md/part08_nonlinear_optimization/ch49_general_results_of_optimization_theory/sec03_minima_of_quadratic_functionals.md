# Các cực tiểu của Toàn phương Các phiếm hàm


<!-- PAGE 1711 -->
Và theo định nghĩa của yếu sự hội tụ
$$lim\langle \nabla J_{v}, z_{\ell}\rangle = \langle \nabla J_{v}, v\rangle ,$$
$$\ell \mapsto \infty$$
Do đó $lim_{\ell\mapsto \infty}\langle \nabla J_{v}, z_{\ell}$ - $v\rangle = 0$, và theo định nghĩa của lim inf ta thu được
$$J(v) \le lim infJ(z_{\ell})$$
$$\ell \mapsto \infty$$
Với mọi dãy $(z_{\ell})_{\ell\ge0}$ hội tụ yếu đến một số phần tử $v \in V$. Bước $4$. yếu giới hạn $u \in U$ của dãy con $(w_{\ell})_{\ell\ge0}$ extracted từ cực tiểu hóa dãy $(u_{k})_{k\ge0}$ thỏa mãn phương trình
$$J(u) = \inf J(v).$$
$$v\in U$$
Bởi Bước $(1)$ và Bước $(2)$ dãy con $(w_{\ell})_{\ell\ge0}$ của dãy $(u_{k})_{k\ge0}$ hội tụ yếu đến một số phần tử $u \in U$, do đó bởi Bước $(3)$ ta có
$$J(u) \le lim infJ(w_{\ell}).$$
$$\ell \mapsto \infty$$
Mặt khác, theo định nghĩa của $(w_{\ell})_{\ell\ge0}$ như dãy con của $(u_{k})_{k\ge0}$, vì dãy $(J(u_{k}))_{k\ge0}$ hội tụ đến J(v), ta có
$$J(u) \le lim infJ(w_{\ell}) = limJ(u_{k}) = \inf J(v),$$
$$\ell \mapsto \infty k\mapsto \infty v\in U$$
Mà chứng tỏ rằng $u \in U$ đạt được cực tiểu của $J$ trên $U$.
Nhận xét: Định lý 49.2 vẫn nghiệm đúng nếu ta chỉ giả sử rằng $J$ là lồi và liên tục. Nó cũng nghiệm đúng trong reflexive Không gian Banach (Banach space), của mà Các không gian Hilbert là đặc biệt trường hợp; xem Brezis $[31]$, Hệ quả 3.23. Định lý 49.2 là khá tổng quát định lý có chứng minh là khá liên quan. Cho các hàm $J$ của nhất định loại/kiểu, ta có thể thu được sự tồn tại và tính duy nhất các kết quả rằng là dễ hơn để chứng minh. Điều này là đúng đặc biệt cho toàn phương các phiếm hàm.

## 49.3 Các cực tiểu của Toàn phương Các phiếm hàm


> **Định nghĩa 49.4.** Cho $V$ là thực Không gian Hilbert (Hilbert space). hàm $J$: $V \to \mathbb{R}$ được gọi là một toàn phương phiếm hàm nếu nó là của tạo thành
$$J(v) = \frac{1}{2} a(v, v) -h(v),$$
Ở đâu: $V \times  V \to \mathbb{R}$ là dạng song tuyến tính (bilinear form) mà là đối xứng và liên tục, và $h: V \to \mathbb{R}$ là liên tục dạng tuyến tính (linear form).

<!-- PAGE 1712 -->
Định nghĩa 49.4 là tự nhiên mở rộng của khái niệm của toàn phương phiếm hàm trên $\mathbb{R}^{n}$. Thật vậy, theo Mệnh đề 48.10, tồn tại duy nhất một liên tục tự liên hợp (self-adjoint) ánh xạ tuyến tính (linear map) $A: V \to V$ sao cho
$$a(u, v) = \langle Au, v\rangle for all u, v \in V ,$$
Và bởi Riesz biểu diễn định lý (Mệnh đề 48.9), tồn tại duy nhất một $b \in V$ sao cho
$$h(v) = \langle b, v\rangle for all v \in V .$$
Hệ quả là, $J$ có thể được viết dưới dạng
$$J(v) = \frac{1}{2} \langle Av, v\rangle -\langle b, v\rangle for all v \in V .(1)$$
Vì là song tuyến tính và $h$ là tuyến tính, bởi Các mệnh đề 39.3 và 39.5, nhận thấy rằng đạo hàm của $J$ được cho bởi
$$dJ_{u}(v) = a(u, v) -h(v)for all v \in V ,$$
Hoặc tương đương bởi
$$dJ_{u}(v) = \langle Au, v\rangle -\langle b, v\rangle = \langle Au -b, v\rangle ,for all v \in V .$$
Do đó gradien của $J$ được cho bởi
$$\nabla J_{u} = Au -b,(2)$$
Chỉ như trong trường hợp của toàn phương hàm của tạo thành J(v) $= (1/2)v^{\top}Av$ - $b^{\top}v$, ở đâu $A$ là đối xứng $n \times  n$ ma trận và $b \in \mathbb{R}^{n}$. để tìm đạo hàm thứ hai $D^{2}J_{u}$ của $J$ tại $u$ ta tính
$$dJ_{u+v}(w) -dJ_{u}(w) = a(u + v, w) -h(w) -(a(u, w) -h(w)) = a(v, w),$$
Do đó
$$D^{2}J_{u}(v, w) = a(v, w) = \langle Av, w\rangle ,$$
Mà cho ta
$$\nabla^{2} J_{u} = A.(3)$$
Ta sẽ cũng tạo sử dụng của sau đây công thức.

> **Mệnh đề 49.3.** Nếu $J$ là toàn phương phiếm hàm, thì
$$J(u + \rho v) = \frac{\rho^{2}}{2} a(v, v) + \rho (a(u, v) -h(v)) + J(u).$$

<!-- PAGE 1713 -->

*Chứng minh.* Vì là đối xứng song tuyến tính và $h$ là tuyến tính, ta có
$$J(u + \rho v) = \frac{1}{2} a(u + \rho v, u + \rho v) -h(u + \rho v)$$
$$= \frac{\rho^{2}}{2} a(v, v) + \rho a(u, v) + \frac{1}{2} a(u, u) -h(u) -\rho h(v)$$
$$= \frac{\rho^{2}}{2} a(v, v) + \rho (a(u, v) -h(v)) + J(u).$$
Vì $dJ_{u}(v) =$ (u, $v)$ - h(v) $= \langle$ Au - $b, v\rangle$ và $\nabla J_{u} =$ Au - $b$, ta có thể cũng viết
$$J(u + \rho v) = \frac{\rho^{2}}{2} a(v, v) + \rho \langle \nabla J_{u}, v\rangle + J(u),$$
Như đã khẳng định. Ta có kết quả sau định lý về sự tồn tại và tính duy nhất của các cực tiểu của toàn phương các phiếm hàm.

> **Định lý 49.4.** Cho trước bất kỳ thực Không gian Hilbert (Hilbert space) $V$, cho $J$: $V \to \mathbb{R}$ là toàn phương phiếm hàm của tạo thành
$$J(v) = \frac{1}{2} a(v, v) -h(v).$$
Giả sử rằng tồn tại một thực số $\alpha  > 0$ sao cho
$$a(v, v) \ge \alpha  \|v\|^{2}for all v \in V .(*_{\alpha})$$
Nếu $U$ là bất kỳ khác rỗng, đóng, lồi tập con của $V$, thì tồn tại duy nhất một $u \in U$ sao cho
$$J(u) = \inf J(v).$$
$$v\in U$$
Phần tử $u \in U$ thỏa mãn điều kiện
$$a(u, v -u) \ge h(v -u)for all v \in U.(*)$$
Ngược lại (với cùng các giả định trên $U$ như ở trên), nếu phần tử $u \in U$ thỏa mãn (*), thì
$$J(u) = \inf J(v).$$
$$v\in U$$
Nếu $U$ là không gian con của $V$, thì ở trên các bất đẳng thức được thay thế bởi các phương trình
$$a(u, v) = h(v)for all v \in U.(**)$$

*Chứng minh.* then chốt điểm là rằng dạng song tuyến tính (bilinear form) là thực sự tích vô hướng (inner product) trong $V$. Điều này là bởi vì nó là xác định dương (positive definite), vì $(*_{\alpha})$ suy ra rằng
$$\sqrt$$
$$\overline{\alpha} \|v\|\le (a(v, v))^{1/2},$$

<!-- PAGE 1714 -->
Và mặt khác tính liên tục của suy ra rằng
$$a(v, v) \le \|a\|\|v\|^{2},$$
Do đó ta thu được
$$\sqrt$$
$$p$$
$$\overline{\alpha} \|v\|\le (a(v, v))^{1/2}\le \overline{\|}\overline{a}\overline{\|\|} v\|.$$
Ở trên cũng chỉ ra rằng chuẩn (norm) $v \mapsto$ ((v, $v))^{1/2}$ được cảm sinh bởi tích vô hướng (inner product) là tương đương đến chuẩn (norm) được cảm sinh bởi tích vô hướng (inner product) $\langle$ -, $-\rangle$ trên $V$. Do đó $h$ là vẫn liên tục đối với chuẩn (norm) $v \mapsto$ ((v, $v))^{1/2}$. Thì bởi Riesz biểu diễn định lý (Mệnh đề 48.9), tồn tại một duy nhất $c \in V$ sao cho
$$h(v) = a(c, v)for all v \in V .$$
Hệ quả là, ta có thể biểu diễn J(v) như
$$J(v) = \frac{1}{2} a(v, v) -a(c, v) = \frac{1}{2} a(v -c, v -c) - \frac{1}{2} a(c, c).$$
Nhưng khi đó cực tiểu hóa J(v) trên $U$ là tương đương đến cực tiểu hóa ((v $-c, v -c))^{1/2}$ trên $v \in U$, và bởi phép chiếu bổ đề (Mệnh đề 48.5(1)) điều này là tương đương đến việc tìm phép chiếu $p_{U}(c)$ của $c$ trên đóng tập lồi (convex set) $U$ đối với tích vô hướng (inner product). Vì vậy, tồn tại duy nhất một $u = p_{U}(c) \in U$ sao cho
$$J(u) = \inf J(v).$$
$$v\in U$$
Cũng theo Mệnh đề 48.5(2), điều này duy nhất phần tử $u \in U$ được đặc trưng hóa bởi điều kiện
$$a(u -c, v -u) \ge 0for all v \in U.$$
Vì
$$a(u -c, v -u) = a(u, v -u) -a(c, v -u) = a(u, v -u) -h(v -u),$$
Ở trên bất đẳng thức là tương đương đến
$$a(u, v -u) \ge h(v -u)for all v \in U.(*)$$
Nếu $U$ là không gian con của $V$, thì theo Mệnh đề 48.5(3) ta có điều kiện
$$a(u -c, v) = 0for all v \in U,$$
Mà là tương đương đến
$$a(u, v) = a(c, v) = h(v)for all v \in U,(**)$$
Được khẳng định.

<!-- PAGE 1715 -->
Lưu ý rằng tính đối xứng của dạng song tuyến tính (bilinear form) được đóng then chốt vai trò. Cũng, các bất đẳng thức
$$a(u, v -u) \ge h(v -u)for all v \in U$$
Đôi khi được gọi là variational các bất đẳng thức.

> **Định nghĩa 49.5.** dạng song tuyến tính (bilinear form): $V \times  V \to \mathbb{R}$ sao cho tồn tại một thực $\alpha  > 0$ sao cho
$$a(v, v) \ge \alpha  \|v\|^{2}for all v \in V$$
Được nói là bức (coercive). Định lý 49.4 là đặc biệt trường hợp của Stampacchia’s định lý và Lax–Milgram định lý khi $U = V$, và ở đâu là dạng song tuyến tính đối xứng. để chứng minh Stampacchia’s định lý nói chung, ta cần đến nhắc lại ánh xạ co (contraction) ánh xạ định lý.

> **Định nghĩa 49.6.** Cho $(E, d)$ là không gian mêtric (metric space). ánh xạ $f$: $E \to E$ là ánh xạ co (contraction) (hoặc ánh xạ co (contraction) ánh xạ) nếu tồn tại một thực số $k$ sao cho $0 \le k < 1$ và
$$d(f(u), f(v)) \le kd(u, v)for all u, v \in E.$$
Số $k$ là thường được gọi là Lipschitz hằng số. sau đây định lý được chứng minh trong Mục 37.10; xem Định lý 37.54. chứng minh có thể được cũng tìm thấy trong Apostol $[4]$, Dixmier $[52]$, hoặc Schwartz $[156]$, trong số nhiều sources. Cho độc giả’s convenience ta restate định lý này.

> **Định lý 49.5.** (Ánh xạ co (contraction) Ánh xạ Định lý) Cho $(E, d)$ là không gian mêtric đầy đủ. Mọi ánh xạ co (contraction) $f$: $E \to E$ có duy nhất cố định điểm (rằng là, phần tử $u \in E$ sao cho f(u) $= u)$. ánh xạ co (contraction) ánh xạ định lý là cũng đã biết như Banach cố định điểm định lý.

> **Định lý 49.6.** (Lions–Stampacchia) Cho trước Không gian Hilbert (Hilbert space) $V$, cho: $V \times  V \to \mathbb{R}$ là liên tục dạng song tuyến tính (bilinear form) (không nhất thiết đối xứng), cho $h \in$ V' là liên tục dạng tuyến tính (linear form), và cho $J$ là cho trước bởi
$$J(v) = \frac{1}{2} a(v, v) -h(v),v \in V.$$
Nếu là bức (coercive), thì với mọi khác rỗng, đóng, lồi tập con $U$ của $V$, tồn tại duy nhất một $u \in U$ sao cho
$$a(u, v -u) \ge h(v -u)for all v \in U.(*)$$
Nếu là đối xứng, thì $u \in U$ là duy nhất phần tử của $U$ sao cho
$$J(u) = \inf J(v).$$
$$v\in U$$

<!-- PAGE 1716 -->

*Chứng minh.* Như được thảo luận chỉ sau Định nghĩa 49.4, theo Mệnh đề 48.10, tồn tại duy nhất một liên tục ánh xạ tuyến tính (linear map) $A: V \to V$ sao cho
$$a(u, v) = \langle Au, v\rangle for all u, v \in V ,$$
Với $\|A\| = \|a\| = C$, và bởi Riesz biểu diễn định lý (Mệnh đề 48.9), tồn tại duy nhất một $b \in V$ sao cho
$$h(v) = \langle b, v\rangle for all v \in V .$$
Hệ quả là, $J$ có thể được viết dưới dạng
$$J(v) = \frac{1}{2} \langle Av, v\rangle -\langle b, v\rangle for all v \in V .( *_{1})$$
Vì $\|A\| = \|a\| = C$, ta có $\|Av\|\le \|A\|\|v\| = C \|v\|$ với mọi $v \in V$. Bằng cách sử dụng $(*_{1})$, bất đẳng thức (*) là tương đương đến việc tìm $u$ sao cho
$$\langle Au, v -u\rangle \ge \langle b, v -u\rangle for all v \in U.( *_{2})$$
Cho $\rho  > 0$ là hằng số được xác định sau này. Thì $(*_{2})$ là tương đương đến
$$\langle \rho b -\rho Au + u -u, v -u\rangle \le 0for all v \in U.( *_{3})$$
Bởi phép chiếu bổ đề (Mệnh đề 48.5 $(1)$ và $(2)), (*_{3})$ là tương đương đến việc tìm $u \in U$ sao cho
$$u = p_{U}(\rho b -\rho Au + u).( *_{4})$$
Ta là đã dẫn đến đến việc tìm cố định điểm của hàm $F$: $U \to U$ cho trước bởi
$$F(v) = p_{U}(\rho b -\rho Av + v).$$
Theo Mệnh đề 48.6, phép chiếu ánh xạ $p_{U}$ thực hiện không tăng khoảng cách, do đó
$$\|F(v_{1}) -F(v_{2})\|\le \|v_{1} -v_{2} -\rho (Av_{1} -Av_{2})\|.$$
Vì là bức (coercive) ta có
$$a(v, v) \ge \alpha  \|v\|^{2},$$
Vì (v, $v) = \langle$ Av, $v\rangle$ ta có
$$\langle Av, v\rangle \ge \alpha  \|v\|^{2}for all v \in V ,( *_{5})$$
Và vì
$$\|Av\|\le C \|v\|for all v \in V ,( *_{6})$$
Ta thu được
$$\|F(v_{1}) -F(v_{2})\|^{2}\le \|v_{1} -v_{2}\|^{2}-2\rho \langle Av_{1} -Av_{2}, v_{1} -v_{2}\rangle + \rho^{2} \|Av_{1} -Av_{2}\|^{2}$$
$$\le \begin{pmatrix} 1 -2\rho \alpha  + \rho^{2} C^{2} \end{pmatrix} \|v_{1} -v_{2}\|^{2}.$$

<!-- PAGE 1717 -->
Nếu ta chọn $\rho  > 0$ sao cho $\rho  < 2\alpha /C^{2}$, thì
$$k^{2}= 1 -2\rho \alpha  + \rho^{2} C^{2}< 1,$$
Và thì
$$\|F(v_{1}) -F(v_{2})\|\le k \|v_{1} -v_{2}\|,( *_{7})$$
Với $0 \le k < 1$, mà chỉ ra rằng $F$ là ánh xạ co (contraction). Theo Định lý 49.5, ánh xạ $F$ có duy nhất cố định điểm $u \in U$, mà kết luận chứng minh của thứ nhất phát biểu. Nếu là cũng đối xứng, thì thứ hai phát biểu là chỉ phần thứ nhất của Định lý 49.4.
Nhận xét: Nhiều vật lý các bài tập có thể được được biểu diễn theo unknown hàm $u$ rằng thỏa mãn một số bất đẳng thức
$$a(u, v -u) \ge h(v -u)for all v \in U,$$
Với một số tập hợp $U$ của “admissible” các hàm mà là đóng và lồi. dạng song tuyến tính (bilinear form) và dạng tuyến tính (linear form) $h$ là thường cho trước theo các tích phân. ở trên bất đẳng thức được gọi là một variational bất đẳng thức. Trong trường hợp đặc biệt khi $U = V$ ta thu được Lax–Milgram định lý.

> **Định lý 49.7.** (Lax–Milgram’s Định lý) Cho trước Không gian Hilbert (Hilbert space) $V$, cho: $V \times  V \to \mathbb{R}$ là liên tục dạng song tuyến tính (bilinear form) (không nhất thiết đối xứng), cho $h \in$ V' là liên tục dạng tuyến tính (linear form), và cho $J$ là cho trước bởi
$$J(v) = \frac{1}{2} a(v, v) -h(v),v \in V.$$
Nếu là bức (coercive), mà có nghĩa là tồn tại một $\alpha  > 0$ sao cho
$$a(v, v) \ge \alpha  \|v\|^{2}for all v \in V ,$$
Thì tồn tại duy nhất một $u \in V$ sao cho
$$a(u, v) = h(v)for all v \in V .$$
Nếu là đối xứng, thì $u \in V$ là duy nhất phần tử của $V$ sao cho
$$J(u) = \inf J(v).$$
$$v\in V$$
Lax–Milgram định lý đóng quan trọng vai trò trong việc giải tuyến tính elliptic riêng vi phân các phương trình; xem Brezis $[31]$. Ta bây giờ xét khác nhau các phương pháp, đã biết như gradien descents, để tìm các cực tiểu của nhất định các loại của các phiếm hàm.
