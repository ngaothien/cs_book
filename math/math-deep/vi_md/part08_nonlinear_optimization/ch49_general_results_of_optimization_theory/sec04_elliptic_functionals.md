# Elliptic Các phiếm hàm


<!-- PAGE 1718 -->

## 49.4 Elliptic Các phiếm hàm

Ta bắt đầu bởi định nghĩa khái niệm của elliptic phiếm hàm mà tổng quát hóa khái niệm của toàn phương hàm được định nghĩa bởi đối xứng xác định dương (SPD) ma trận. Elliptic các phiếm hàm là tốt được điều chỉnh đến các loại của các phương pháp lặp được mô tả trong mục này và lend themselves tốt đến giải tích/phân tích của sự hội tụ của các phương pháp này.

> **Định nghĩa 49.7.** Cho trước Không gian Hilbert (Hilbert space) $V$, phiếm hàm $J$: $V \to \mathbb{R}$ được nói là elliptic nếu nó là một cách liên tục khả vi (differentiable) trên $V$, và nếu tồn tại một hằng số $\alpha  > 0$ sao cho
$$\langle \nabla J_{v} -\nabla J_{u}, v -u\rangle \ge \alpha  \|v -u\|^{2}for all u, v \in V .$$
Sau đây mệnh đề gathers các tính chất của elliptic các phiếm hàm rằng sẽ được sử dụng sau này đến analyze sự hội tụ của khác nhau hạ gradien (gradient descent) các phương pháp.

> **Định lý 49.8.** Cho $V$ là Không gian Hilbert (Hilbert space).
$(1)$ elliptic phiếm hàm $J$: $V \to \mathbb{R}$ là lồi chặt (strictly convex) và bức (coercive). Hơn nữa, nó thỏa mãn đồng nhất thức
$$J(v) -J(u) \ge \langle \nabla J_{u}, v -u\rangle + \frac{\alpha}{2} \|v -u\|^{2}for all u, v \in V .$$
$(2)$ Nếu $U$ là khác rỗng, lồi, đóng tập con của Không gian Hilbert (Hilbert space) $V$ và nếu $J$ là elliptic phiếm hàm, thì Bài toán $(P)$,
$$findu$$
$$such that u \in U and J(u) = \inf J(v)$$
$$v\in U$$
Có duy nhất nghiệm.
$(3)$ Giả sử tập hợp $U$ là lồi và rằng phiếm hàm $J$ là elliptic. Thì phần tử $u \in U$ là nghiệm của Bài toán $(P)$ khi và chỉ khi nó thỏa mãn điều kiện
$$\langle \nabla J_{u}, v -u\rangle \ge 0for every v \in U$$
Trong tổng quát trường hợp, hoặc
$$\nabla J_{u} = 0 if U = V .$$
$(4) A$ phiếm hàm $J$ mà là hai lần khả vi (differentiable) trong $V$ là elliptic khi và chỉ khi
$$\langle \nabla^{2} J_{u}(w), w\rangle \ge \alpha  \|w\|^{2}for all u, w \in V .$$

<!-- PAGE 1719 -->

*Chứng minh.* $(1)$ Vì $J$ là $C^{1}-function$, bởi Taylor’s công thức với tích phân phần dư trong trường hợp $m = 0$ (Định lý 39.26), ta thu được
$$J(v) -J(u) = \int_{0}^{}  1dJ_{u+t(v-u)}(v -u)dt$$
$$= \int_{0}^{}  1\langle \nabla J_{u+t(v-u)}, v -u\rangle dt$$
$$= \langle \nabla J_{u}, v -u\rangle + \int_{0}^{}  1\langle \nabla J_{u+t(v-u)} -\nabla J_{u}, v -u\rangle dt$$
$$= \langle \nabla J_{u}, v -u\rangle + \int_{0}^{}  1 \frac{J_{u+t(v-u)}J_{u}, t(vu)}{t} \langle \nabla  -\nabla  -\rangle dt$$
$$1$$
$$\ge \langle \nabla J_{u}, v -u\rangle + \int_{0}^{}  \alpha t \|v -u\|^{2} dtsince J is elliptic$$
$$.$$
$$= \langle \nabla J_{u}, v -u\rangle + \frac{\alpha}{2} \|v -u\|^{2}$$
Bằng cách sử dụng bất đẳng thức
$$J(v) -J(u) \ge \langle \nabla J_{u}, v -u\rangle + \frac{\alpha}{2} \|v -u\|^{2}for all u, v \in V ,$$
Theo Mệnh đề 40.11(2), vì
$$J(v) > J(u) + \langle \nabla J_{u}, v -u\rangle for all u, v \in V , v \neq  u,$$
Hàm $J$ là lồi chặt (strictly convex). Nó là bức (coercive) bởi vì (bằng cách sử dụng Cauchy–Schwarz)
$$J(v) \ge J(0) + \langle \nabla J_{0}, v\rangle + \frac{\alpha}{2} v\|^{2}$$
$$,$$
$$\ge J(0) -\|\nabla J_{0}\|\|v\|+ \frac{\|\alpha}{2} \|v\|^{2}$$
Và số hạng $(-\|\nabla J_{0}\| +_{2}^{\alpha}  \|v\|) \|v\|$ đi đến $+\infty$ khi $\|v\|$ tiến tới đến $+\infty$.
$(2)$ Vì bởi $(1)$ phiếm hàm $J$ là bức (coercive), theo Định lý 49.2, Bài toán $(P)$ có nghiệm. Vì $J$ là lồi chặt (strictly convex), theo Định lý 40.13(2), nó có duy nhất cực tiểu.
$(3)$ Các phần tử này là chỉ các điều kiện của Định lý 40.13(3, $4)$.
$(4)$ Nếu $J$ là hai lần khả vi (differentiable), ta đã chỉ ra trong Mục 39.6 rằng ta có
$$-$$
$$D^{2}J_{u}(w, w) = D_{w}(DJ)(u) = \theta lim\mapsto 0 \frac{DJ_{u+\theta w}(w)DJ_{u}(w)}{\theta} ,$$
Và vì
$$D^{2}J_{u}(w, w) = \langle \nabla^{2} J_{u}(w), w\rangle$$
$$DJ_{u+\theta w}(w) = \langle \nabla J_{u+\theta w}, w\rangle$$
$$DJ_{u}(w) = \langle \nabla J_{u}, w\rangle ,$$

<!-- PAGE 1720 -->
Và vì $J$ là elliptic, với mọi $u, w \in V$ ta có thể viết
$$\langle \nabla  -\nabla \rangle$$
$$\langle \nabla^{2} J_{u}(w), w\rangle = \theta lim\mapsto 0 \frac{J_{u+\theta w}J_{u}, w}{\theta}$$
$$\langle \nabla  -\nabla \rangle$$
$$= \theta lim\mapsto 0 \frac{J_{u+\theta w}J_{u}, \theta w}{\theta^{2}}$$
$$\ge \theta  \|w\|^{2}.$$
Ngược lại, giả sử rằng điều kiện
$$\langle \nabla^{2} J_{u}(w), w\rangle \ge \alpha  \|w\|^{2}for all u, w \in V$$
Nghiệm đúng. Nếu ta định nghĩa hàm $g: V \to \mathbb{R}$ bởi
$$g(w) = \langle \nabla J_{w}, v -u\rangle = dJ_{w}(v -u) = D_{v-u}J(w),$$
Ở đâu $u$ và $v$ là cố định các vectơ trong $V$, thì ta có $dg_{u+\theta(v-u)}(v-u) = D_{v-u}g(u+\theta$ (v-u)) $= D_{v-u}D_{v-u}J(u+\theta$ (v-u)) $= D^{2}J_{u+\theta(v-u)}(v-u$, v-u) và ta có thể áp dụng Taylor–MacLaurin công thức (Định lý 39.25 với $m = 0)$ đến $g$, và ta thu được
$$\langle \nabla J_{v} -\nabla J_{u}, v -u\rangle = g(v) -g(u)$$
$$= dg_{u+\theta(v-u)}(v -u)(0 < \theta  < 1)$$
$$= D^{2}J_{u+\theta(v-u)}(v -u, v -u)$$
$$= \langle \nabla^{2} J_{u+\theta(v-u)}(v -u), v -u\rangle$$
$$\ge \alpha  \|v -u\|^{2},$$
Mà chỉ ra rằng $J$ là elliptic.
$$\mathbb{R}^{n} \mathbb{R}$$

> **Hệ quả 49.9.** Nếu $J$: $\to$ là toàn phương hàm cho trước bởi
$$J(v) = \frac{1}{2} \langle Av, v\rangle -\langle b, v\rangle$$
(ở đâu $A$ là đối xứng $n \times  n$ ma trận và $\langle$ -, $-\rangle$ là tiêu chuẩn Eucidean tích vô hướng (inner product)), thì $J$ là elliptic khi và chỉ khi $A$ là xác định dương (positive definite). Điều này hệ quả của Định lý 49.8 bởi vì
$$\langle \nabla^{2} J_{u}(w), w\rangle = \langle Aw, w\rangle \ge \lambda_{1}  \|w\|^{2}$$
Ở đâu $\lambda_{1}$ là nhỏ nhất trị riêng (eigenvalue) của $A$; xem Mệnh đề 17.24 (Rayleigh–Ritz). Lưu ý rằng theo Mệnh đề 17.24 (Rayleigh–Ritz), ta cũng có folllowing hệ quả.
