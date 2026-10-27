# Sự tồn tại của Các nghiệm của Tối ưu hóa Bài toán


<!-- PAGE 1707 -->

## 49.2 Sự tồn tại của Các nghiệm của Tối ưu hóa

$$Problem$$
Ta bắt đầu với trường hợp ở đâu $U$ là đóng nhưng có thể không bị chặn tập con của $\mathbb{R}^{n}$. Trong trường hợp này sau đây loại/kiểu của các hàm phát sinh.

> **Định nghĩa 49.1.** nhận giá trị thực (real-valued) hàm $J$: $V \to \mathbb{R}$ được định nghĩa trên không gian vectơ định chuẩn (normed vector space) $V$ là bức (coercive) khi và chỉ khi với mọi dãy $(v_{k})_{k\ge1}$ của các vectơ $v_{k} \in V$, nếu $lim_{k\mapsto \infty} \|v_{k}\| = \infty$, thì
$$limJ(v_{k}) = +\infty .$$
$$k\mapsto \infty$$
Ví dụ, hàm f(x) $= x^{2}+2x$ là bức (coercive), nhưng afin hàm f(x) $= ax+b$ là không.
$$\mathbb{R}^{n} \mathbb{R}^{n} \mathbb{R}$$

> **Mệnh đề 49.1.** Cho $U$ là khác rỗng, đóng tập con của, và cho $J$: $\to$ là hàm liên tục (continuous function) mà là bức (coercive) nếu $U$ là không bị chặn. Thì có một least một phần tử $\mathbb{R}^{n} u \in$ sao cho
$$u \in UandJ(u) = \inf J(v).$$
$$v\in U$$

*Chứng minh.* Vì $U \neq  \emptyset$, chọn bất kỳ $u_{0} \in U$. Vì $J$ là bức (coercive), tồn tại một $r > 0$ sao cho với mọi $v \in \mathbb{R}^{n}$, nếu $\|v\| > r$ thì $J(u_{0}) <$ J(v). Suy ra rằng $J$ được cực tiểu hóa trên tập hợp
$$\mathbb{R}^{n}$$
$$U_{0} = U \cap {v \in | \|v\|\le r}.$$
$$\mathbb{R}^{n}$$
Vì $U$ là đóng và vì hình cầu đóng (closed ball) ${v \in$ | $\|v\|\le r}$ là compắc, $U_{0}$ là compắc, nhưng ta biết rằng bất kỳ hàm liên tục (continuous function) trên tập compắc (compact set) có cực tiểu mà là đạt được. then chốt điểm trong ở trên chứng minh là sự kiện rằng $U_{0}$ là compắc. Trong thứ tự đến tổng quát hóa Mệnh đề 49.1 đến trường hợp của vô hạn dimensional không gian vectơ (vector space), ta cần một số additional các giả định, và hóa ra là tính lồi của $U$ và của hàm $J$ là đủ. then chốt là rằng lồi, đóng và bị chặn các tập con của Không gian Hilbert (Hilbert space) là “yếu compắc.”

> **Định nghĩa 49.2.** Cho $V$ là Không gian Hilbert (Hilbert space). dãy $(u_{k})_{k\ge1}$ của các vectơ $u_{k} \in V$ hội tụ yếu nếu tồn tại một $u \in V$ sao cho
$$lim\langle v, u_{k}\rangle = \langle v, u\rangle for every v \in V .$$
$$k\mapsto \infty$$
Nhắc lại rằng Hibert không gian là khả ly nếu nó có đếm được Hilbert cơ sở (basis) (xem Định nghĩa.4). Cũng, trong Không gian Euclid (Euclidean space) (của hữu hạn số chiều) $V$, tích vô hướng (inner product) cảm sinh đẳng cấu giữa $V$ và của nó đối ngẫu (dual) $V^{*}$. Trong trường hợp của chúng ta, ta cần đẳng cấu $\sharp$ từ $V^{*}$ đến $V$ được định nghĩa sao cho với mọi dạng tuyến tính (linear form) $\omega  \in V^{*}$, vectơ $\omega^{\sharp} \in V$ là một cách duy nhất được định nghĩa bởi phương trình
$$\omega (v) = \langle v, \omega^{\sharp} \rangle for all v \in V .$$

<!-- PAGE 1708 -->
$$\mathbb{R}$$
Trong Không gian Hilbert (Hilbert space), không gian đối ngẫu (dual space) V' là tập hợp tất cả liên tục các dạng tuyến tính $\omega$: $V \to$, và sự tồn tại của đẳng cấu $\sharp$ giữa V' và $V$ được cho bởi Riesz biểu diễn định lý; xem Mệnh đề 48.9. định lý này cho phép tổng quát hóa của khái niệm của gradien. Thật vậy, nếu $f$: $V \to \mathbb{R}$ là hàm được định nghĩa trên Không gian Hilbert (Hilbert space) $V$ và nếu $f$ là khả vi (differentiable) tại một số điểm $u \in V$, thì theo Định nghĩa, đạo hàm $df_{u}$: $V \to \mathbb{R}$ là liên tục dạng tuyến tính (linear form), do đó bởi Riesz biểu diễn định lý (Mệnh đề 48.9) tồn tại duy nhất một vectơ, được ký hiệu $\nabla f_{u} \in V$, sao cho
$$df_{u}(v) = \langle v, \nabla f_{u}\rangle for all v \in V .$$

> **Định nghĩa 49.3.** duy nhất vectơ $\nabla f_{u}$ sao cho
$$df_{u}(v) = \langle v, \nabla f_{u}\rangle for all v \in V$$
Được gọi là gradien của $f$ tại $u$. Tương tự, vì đạo hàm thứ hai $D^{2}f_{u}$: $V \to$ V' của $f$ cảm sinh liên tục dạng song tuyến tính đối xứng từ $V \times V to\mathbb{R}$, theo Mệnh đề 48.10, tồn tại duy nhất một liên tục tự liên hợp (self-adjoint) ánh xạ tuyến tính (linear map) $\nabla^{2} f_{u}$: $V \to V$ sao cho
$$D^{2}f_{u}(v, w) = \langle \nabla^{2} f_{u}(v), w\rangle for all v, w \in V .$$
Ánh xạ $\nabla^{2} f_{u}$ là tổng quát hóa của Hessian. tiếp theo định lý là khá tổng quát kết quả về sự tồn tại của các cực tiểu của các hàm lồi được định nghĩa trên lồi các miền. chứng minh là khá liên quan và có thể được được bỏ qua upon thứ nhất reading.

> **Định lý 49.2.** Cho $U$ là khác rỗng, lồi, đóng tập con của khả ly Không gian Hilbert (Hilbert space) $V$, và cho $J$: $V \to \mathbb{R}$ là lồi, khả vi (differentiable) hàm mà là bức (coercive) nếu $U$ là không bị chặn. Thì có một least một phần tử $u \in V$ sao cho
$$u \in UandJ(u) = \inf J(v).$$
$$v\in U$$

*Chứng minh.* Như trong chứng minh của Mệnh đề 49.1, vì hàm $J$ là bức (coercive), ta có thể giả sử rằng $U$ là bị chặn và lồi (tuy nhiên, nếu $V$ vô hạn dimensional, thì $U$ là không compắc nói chung). chứng minh tiến hành trong bốn các bước. Bước $1$. Xét cực tiểu hóa dãy $(u_{k})_{k\ge0}$, cụ thể là dãy của các phần tử $u_{k} \in V$ sao cho
$$u_{k} \in Ufor all k \ge 0,limJ(u_{k}) = \inf J(v).$$
$$k\mapsto \infty v\in U$$
Tại điều này giai đoạn, nó là khả dĩ/có thể rằng $inf_{v\in U}$ J(v) $= -\infty$, nhưng ta sẽ xem rằng điều này là thực sự không thể. Tuy nhiên, vì $U$ là bị chặn, dãy $(u_{k})_{k\ge0}$ là bị chặn. Của ta mục tiêu là để chứng minh rằng tồn tại một dãy con của $(w_{\ell})_{\ell\ge0}$ của $(u_{k})_{k\ge0}$ rằng hội tụ yếu. Vì dãy $(u_{k})_{k\ge0}$ là bị chặn tồn tại một hằng số $C > 0$ sao cho $\|u_{k}\|\le C$ với mọi $k \ge 0$. Thì bởi Cauchy–Schwarz bất đẳng thức, với mọi $v \in V$ ta có
$$|\langle v, u_{k}\rangle | \le \|v\|\|u_{k}\|\le C \|v\|,$$

<!-- PAGE 1709 -->
Mà chỉ ra rằng dãy $(\langle v, u_{k}\rangle )_{k\ge0}$ là bị chặn. Vì $V$ là khả ly Không gian Hilbert (Hilbert space), có một đếm được họ $(v_{k})_{k\ge0}$ của các vectơ $v_{k} \in V$ mà là trù mật trong $V$. Vì dãy $(\langle v_{1}, u_{k}\rangle )_{k\ge0}$ là bị chặn (trong $\mathbb{R})$, ta có thể tìm convergent dãy con $(\langle v_{1}, u_{i1(j)}\rangle )_{j\ge0}$. Tương tự, vì dãy $(\langle v_{2}, u_{i1(j)}\rangle )_{j\ge0}$ là bị chặn, ta có thể tìm convergent dãy con $(\langle v_{2}, u_{i2(j)}\rangle )_{j\ge0}$, và nói chung, vì dãy $(\langle v_{k}, u_{ik-1(j)}\rangle )_{j\ge0}$ là bị chặn, ta có thể tìm convergent dãy con $(\langle v_{k}, u_{ik(j)}\rangle )_{j\ge0}$. Ta thu được kết quả sau vô hạn mảng (array):
$$\begin{pmatrix} \langle v_{1}, u_{i1(1)}\rangle & \langle v_{2}, u_{i2(1)}\rangle & \cdots & \langle v_{k}, u_{ik(1)}\rangle & \cdots \\ \langle v_{1}, u_{i1(2)}\rangle & \langle v_{2}, u_{i2(2)}\rangle & \cdots & \langle v_{k}, u_{ik(2)}\rangle & \cdots \\ \vdots & \vdots & \vdots & \vdots & \vdots \\ \langle v_{1}, u_{i1(k)}\rangle & \langle v_{2}, u_{i2(k)}\rangle & \cdots & \langle v_{k}, u_{ik(k)}\rangle & \cdots \\ \vdots & \vdots & \vdots & \vdots & \vdots \end{pmatrix}$$
Xét “đường chéo” dãy $(w_{\ell})_{\ell\ge0}$ được định nghĩa bởi
$$w_{\ell}= u_{i\ell(\ell)},\ell \ge 0.$$
Ta là đi để chứng minh rằng với mọi $v \in V$, dãy $(\langle v, w_{\ell}\rangle )_{\ell\ge0}$ có giới hạn. Bởi cách xây dựng, với mọi $k \ge 0$, dãy $(\langle v_{k}, w_{\ell}\rangle )_{\ell\ge0}$ có giới hạn, mà là giới hạn của dãy $(\langle v_{k}, u_{ik(j)}\rangle )_{j\ge0}$, vì dãy $(i_{\ell}(\ell ))_{\ell\ge0}$ là dãy con của mọi dãy $(i_{\ell}(j))_{j\ge0}$ với mọi $\ell \ge 0$. Chọn bất kỳ $v \in V$ và bất kỳ $\epsilon  > 0$. Vì $(v_{k})_{k\ge0}$ là trù mật trong $V$, tồn tại một $v_{k}$ sao cho
$$\|v -v_{k}\|\le \epsilon /(4C).$$
Thì ta có
$$|\langle v, w_{\ell}\rangle -\langle v, w_{m}\rangle | = |\langle v, w_{\ell}-w_{m}\rangle |$$
$$= |\langle v_{k} + v -v_{k}, w_{\ell}-w_{m}\rangle |$$
$$= |\langle v_{k}, w_{\ell}-w_{m}\rangle + \langle v -v_{k}, w_{\ell}-w_{m}\rangle |$$
$$\le |\langle v_{k}, w_{\ell}\rangle -\langle v_{k}, w_{m}\rangle | + |\langle v -v_{k}, w_{\ell}-w_{m}\rangle |.$$
Bởi Cauchy–Schwarz và vì $\|w_{\ell}$ - $w_{m}\|\le \|w_{\ell}\| + \|w_{m}\|\le C + C =$ 2C,
$$|\langle v -v_{k}, w_{\ell}-w_{m}\rangle | \le \|v -v_{k}\|\|w_{\ell}-w_{m}\|\le (\epsilon /(4C))2C = \epsilon /2,$$
Do đó
$$|\langle v, w_{\ell}\rangle -\langle v, w_{m}\rangle | \le |\langle v_{k}, w_{\ell}-w_{m}\rangle | + \epsilon /2.$$
Với phần tử $v_{k}$ held cố định, bởi trước đó lập luận dãy $(\langle v_{k}, w_{\ell}\rangle )_{\ell\ge0}$ hội tụ, do đó nó là Dãy Cauchy (Cauchy sequence). Hệ quả là tồn tại một $\ell_{0}$ (tùy thuộc trên $\epsilon$ và $v_{k})$ sao cho
$$|\langle v_{k}, w_{\ell}\rangle -\langle v_{k}, w_{m}\rangle | \le \epsilon /2for all \ell , m \ge \ell_{0} ,$$

<!-- PAGE 1710 -->
Do đó ta thu được
$$|\langle v, w_{\ell}\rangle -\langle v, w_{m}\rangle | \le \epsilon /2 + \epsilon /2 = \epsilon for all \ell , m \ge \ell_{0} .$$
Điều này chứng tỏ rằng dãy $(\langle v, w_{\ell}\rangle )_{\ell\ge0}$ là Dãy Cauchy (Cauchy sequence), và do đó nó hội tụ. Định nghĩa hàm $g: V \to \mathbb{R}$ bởi
$$g(v) = lim\langle v, w_{\ell}\rangle ,for all v \in V .$$
$$\ell \mapsto \infty$$
Vì
$$|\langle v, w_{\ell}\rangle | \le \|v\|\|w_{\ell}\|\le C \|v\|for all \ell \ge 0,$$
Ta có
$$|g(v)| \le C \|v\|,$$
Do đó $g$ là liên tục ánh xạ tuyến tính (linear map). Bởi Riesz biểu diễn định lý (Mệnh đề 48.9), tồn tại duy nhất một $u \in V$ sao cho
$$g(v) = \langle v, u\rangle for all v \in V ,$$
Mà chỉ ra rằng
$$lim\langle v, w_{\ell}\rangle = \langle v, u\rangle for all v \in V ,$$
$$\ell \mapsto \infty$$
Cụ thể là dãy con $(w_{\ell})_{\ell\ge0}$ của dãy $(u_{k})_{k\ge0}$ hội tụ yếu đến $u \in V$. Bước $2$. Ta chứng minh rằng “yếu giới hạn” $u$ của dãy $(w_{\ell})_{\ell\ge0}$ thuộc đến $U$. Xét phép chiếu $p_{U}(u)$ của $u \in V$ lên đóng tập lồi (convex set) $U$. Vì $w_{\ell} \in U$, theo Mệnh đề 48.5(2) và sự kiện rằng $U$ là lồi và đóng, ta có
$$\langle p_{U}(u) -u, w_{\ell}-p_{U}(u)\rangle \ge 0for all \ell \ge 0.$$
Yếu sự hội tụ của dãy $(w_{\ell})_{\ell\ge0}$ đến $u$ suy ra rằng
$$0 \le lim\langle p_{U}(u) -u, w_{\ell}-p_{U}(u)\rangle = \langle p_{U}(u) -u, u -p_{U}(u)\rangle$$
$$\ell \mapsto \infty$$
$$= -\|p_{U}(u) -u\|\le 0,$$
Do đó $\|p_{U}(u)$ - $u\| = 0$, mà có nghĩa là $p_{U}(u) = u$, và do đó $u \in U$. Bước $3$. Ta chứng minh rằng
$$J(v) \le lim infJ(z_{\ell})$$
$$\ell \mapsto \infty$$
Với mọi dãy $(z_{\ell})_{\ell\ge0}$ hội tụ yếu đến một số phần tử $v \in V$. Vì $J$ được giả sử là khả vi (differentiable) và lồi, theo Mệnh đề 40.11(1) ta có
$$J(v) + \langle \nabla J_{v}, z_{\ell}-v\rangle \le J(z_{\ell})for all \ell \ge 0,$$
