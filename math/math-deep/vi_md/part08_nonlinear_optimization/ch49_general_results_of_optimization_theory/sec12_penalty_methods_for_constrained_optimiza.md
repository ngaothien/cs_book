# Hình phạt (penalty) Các phương pháp cho Có ràng buộc Tối ưu hóa


<!-- PAGE 1755 -->
Đặc biệt, điều này là trường hợp nếu
$$\mathbb{R}_{+}^{n}\mathbb{R}^{n}$$
$$U = = {v \in | v \ge 0}$$
Và nếu
$$J(v) = \frac{1}{2} \langle Av, a\rangle -\langle b, v\rangle$$
Là elliptic toàn phương phiếm hàm trên $\mathbb{R}^{n}$. Thì vectơ $u_{k+1} = (u_{1}^{k+1}, \dots  , u_{n}^{k+1})$ là cho trước theo $u_{k} = (u_{1}^{k}, \dots  , u_{n}^{k})$ bởi
$$u_{i}^{k+1}= \max{u_{i}^{k} -\rho_{k} (Au_{k} -b)_{i}, 0},1 \le i \le n.$$

## 49.12 Hình phạt (penalty) Các phương pháp cho Có ràng buộc Tối ưu hóa

Trong trường hợp ở đâu $V = \mathbb{R}^{n}$, một cái khác phương pháp đến deal với có ràng buộc tối ưu hóa là đến incorporate miền xác định $U$ vào hàm mục tiêu (objective function) $J$ bằng cách cộng hình phạt (penalty) hàm.
$$\mathbb{R}^{n} \mathbb{R}^{n} \mathbb{R}$$

> **Định nghĩa 49.11.** Cho trước khác rỗng đóng lồi tập con $U$ của, hàm $\psi$: $\to$ được gọi là một hình phạt (penalty) hàm cho $U$ nếu $\psi$ là lồi và liên tục và nếu sau đây các điều kiện đúng:
$$\psi (v) \ge 0for allv \in \mathbb{R}^{n},and\psi (v) = 0iffv \in U.$$
Sau đây mệnh đề chỉ ra rằng sử dụng của hình phạt (penalty) các hàm rút gọn có ràng buộc tối ưu hóa bài toán đến dãy của không ràng buộc tối ưu hóa các bài tập.
$$\mathbb{R}^{n} \mathbb{R}$$

> **Mệnh đề 49.19.** Cho $J$: $\to$ là liên tục, bức (coercive), chặt hàm lồi (convex function), $U$
$$\mathbb{R}^{n} \mathbb{R}^{n} \mathbb{R}$$
Là khác rỗng, lồi, đóng tập con của, $\psi$: $\to$ là hình phạt (penalty) hàm cho $U$, và cho $\mathbb{R}^{n} \mathbb{R} J_{\epsilon}$: $\to$ là có phạt hàm mục tiêu (objective function) cho trước bởi
$$J_{\epsilon}(v) = J(v) + \frac{1}{\epsilon} \psi (v)for all v \in \mathbb{R}^{n}.$$
$$\mathbb{R}^{n}$$
Thì với mọi $\epsilon  > 0$, tồn tại duy nhất một phần tử $u_{\epsilon} \in$ sao cho
$$J_{\epsilon}(u_{\epsilon}) = \inf J_{\epsilon}(v).$$
$$v\in \mathbb{R} n$$
Hơn nữa, nếu $u \in U$ là duy nhất điểm cực tiểu hóa của $J$ trên $U$, sao cho J(u) $= inf_{v\in U}$ J(v), thì
$$lim u_{\epsilon} = u.$$
$$\epsilon \mapsto 0$$

*Chứng minh.* Nhận thấy rằng vì $J$ là bức (coercive), vì $\psi (v) \ge 0$ với mọi $v \in \mathbb{R}^{n}$, và $J_{\epsilon} = J + (1/\epsilon )\psi$, ta có $J_{\epsilon}(v) \ge$ J(v) với mọi $v \in \mathbb{R}^{n}$, do đó $J_{\epsilon}$ là cũng bức (coercive). Vì $J$ là lồi chặt (strictly convex) và $(1/\epsilon )\psi$ là lồi, nó là ngay lập tức đã kiểm tra rằng $J_{\epsilon} = J + (1/\epsilon )\psi$ là cũng lồi chặt (strictly convex). Thì theo Mệnh đề 49.1 (và sự kiện rằng $J$ và $J_{\epsilon}$ là lồi chặt (strictly convex)), $J$ có duy nhất điểm cực tiểu hóa $u \in U$, và $J_{\epsilon}$ có duy nhất điểm cực tiểu hóa $u_{\epsilon} \in \mathbb{R}^{n}$.

<!-- PAGE 1756 -->
Vì $\psi (u) = 0$ khi và chỉ khi $u \in U$, và $\psi (v) \ge 0$ với mọi $v \in \mathbb{R}^{n}$, ta có $J_{\epsilon}(u) =$ J(u), và vì $u_{\epsilon}$ là điểm cực tiểu hóa của $J_{\epsilon}$ ta có $J_{\epsilon}(u_{\epsilon}) \le J_{\epsilon}(u)$, do đó ta thu được
$$J(u_{\epsilon}) \le J(u_{\epsilon}) + \frac{1}{\epsilon} \psi (u_{\epsilon}) = J_{\epsilon}(u_{\epsilon}) \le J_{\epsilon}(u) = J(u),$$
Rằng là,
$$J(u_{\epsilon}) \le J(u).(*_{1})$$
Vì $J$ là bức (coercive), họ $(u_{\epsilon})_{\epsilon >0}$ là bị chặn. Bởi tính compắc (vì ta là trong $\mathbb{R}^{n})$,
$$\mathbb{R}^{n}$$
Tồn tại một dãy con $(u_{\epsilon(i)})_{i\ge0}$ với $lim_{i\mapsto \infty} \epsilon (i) = 0$ và một số phần tử u' $\in$ sao cho
$$limu_{\epsilon(i)} = u'.$$
$$i\mapsto \infty$$
Từ bất đẳng thức $J(u_{\epsilon}) \le$ J(u) được chứng minh trong $(*_{1})$ và tính liên tục của $J$, ta suy ra rằng
$$J(u') = limJ(u_{\epsilon(i)}) \le J(u).(*_{2})$$
$$i\mapsto \infty$$
Theo định nghĩa của $J_{\epsilon}(u_{\epsilon})$ và $(*_{1})$, ta có
$$0 \le \psi (u_{\epsilon(i)}) \le \epsilon (i)(J(u) -J(u_{\epsilon(i)})),$$
Và vì dãy $(u_{\epsilon(i)})_{i\ge0}$ hội tụ, các số J(u) - $J(u_{\epsilon(i)})$ là bị chặn một cách độc lập của $i$. Hệ quả là, vì $lim_{i\mapsto \infty} \epsilon (i) = 0$ và vì hàm $\psi$ là liên tục, ta có
$$0 = lim\psi (u_{\epsilon(i)}) = \psi (u'),$$
$$i\mapsto \infty$$
Mà chỉ ra rằng u' $\in U$. Vì bởi $(*_{2})$ ta có J(u') $\le$ J(u), và vì cả hai $u$, u' $\in U$ và $u$ là duy nhất điểm cực tiểu hóa của $J$ trên $U$ ta phải có u' $= u$. Therfore u' là duy nhất điểm cực tiểu hóa của $J$ trên $U$. Nhưng khi đó toàn bộ họ $(u_{\epsilon})_{\epsilon >0}$ hội tụ đến $u$ vì ta có thể sử dụng cùng lập luận như ở trên với mọi dãy con của $(u_{\epsilon})_{\epsilon >0}$.
$$\mathbb{R}^{n} \mathbb{R}$$
Lưu ý rằng hàm lồi (convex function) $\psi$: $\to$ là automatically liên tục, do đó giả định của tính liên tục là redundant. Như ứng dụng của Mệnh đề 49.19, nếu $U$ được cho bởi
$$\mathbb{R}^{n}$$
$$U = {v \in | \phi_{i} (v) \le 0, i = 1, \dots  , m},$$
$$\mathbb{R}^{n} \mathbb{R}$$
Ở đâu các hàm $\phi_{i}$: $\to$ là lồi, ta có thể lấy $\psi$ là hàm cho trước bởi
$$\psi (v) = \sum_{i=1}^{m}  \max{\phi_{i} (v), 0}.$$
