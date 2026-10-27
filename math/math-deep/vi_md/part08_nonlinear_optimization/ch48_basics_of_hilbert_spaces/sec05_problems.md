# Các bài tập


<!-- PAGE 1701 -->
$\bullet$ Khoảng cách của điểm đến tập con, diameter. $\bullet$ Phép chiếu lên đóng và lồi tập con. $\bullet$ Phần bù trực giao (orthogonal complement) của đóng không gian con. $\bullet$ Đối ngẫu (dual) của Không gian Hilbert (Hilbert space). $\bullet$ Bị chặn tuyến tính toán tử (hoặc phiếm hàm). $\bullet$ Riesz biểu diễn định lý. $\bullet$ Liên hợp (adjoint) của liên tục ánh xạ tuyến tính (linear map). $\bullet$ Farkas–Minkowski bổ đề.

## 48.5 Các bài tập

Bài toán 48.1. Cho $V$ là Không gian Hilbert (Hilbert space). Chứng minh rằng không gian con $W$ của $V$ là trù mật trong $V$ khi và chỉ khi không có khác không vectơ trực giao đến $W$.
Bài toán 48.2. Chứng minh rằng liên hợp (adjoint) thỏa mãn các tính chất sau đây:
$$(f + g)^{*}= f^{*} + g^{*}$$
$$(\lambda f)^{*}=\overline{\lambda f}^{*}$$
$$(f \circ g)^{*}= g^{*}\circ f^{*}$$
$$f^{**} = f.$$
Bài toán 48.3. Chứng minh rằng $\|f^{*} \circ f\| = \|f\|^{2}$.
Bài toán 48.4. Cho $V$ là (thực) Không gian Hilbert (Hilbert space) và cho $C$ là khác rỗng đóng lồi tập con của $V$. Định nghĩa ánh xạ $h: V \to \mathbb{R} \cup {+\infty$ } bởi
$$h(u) = \sup\langle u, v\rangle .$$
$$v\in C$$
Chứng minh rằng
$$C = \bigcap_{u\in V}  {v \in V | \langle u, v\rangle \le h(u)} = \bigcap_{u\in\Lambda C}  {v \in V | \langle u, v\rangle \le h(u)},$$
Ở đâu $\Lambda_{C}  = {u \in V$ | h(u) $\neq  +\infty$ }. Mô tả $\Lambda_{C}$ khi $C$ là cũng không gian con của $V$.
Bài toán 48.5. Cho $A$ là thực $m\times n$ ma trận, và cho $(u_{k})$ là dãy của các vectơ $u_{k} \in \mathbb{R}^{n}$ sao cho $u_{k} \ge 0$. Chứng minh rằng nếu dãy $(Au_{k})$ hội tụ, thì tồn tại một $u \in \mathbb{R}^{n}$ sao cho
$$Au = limAu_{k}andu \ge 0.$$
$$k\mapsto \infty$$

<!-- PAGE 1702 -->
Bài toán 48.6. Cho $V$ là thực Không gian Hilbert (Hilbert space), $(a_{1}, \dots  , a_{m})$ dãy của $m$ các vectơ trong $V , b$ một số vectơ trong $V , (\alpha_{1} , \dots  , \alpha_{m}$) dãy của $m$ thực các số, và $\beta$ một số thực số. Chứng minh rằng inclusion
$${w \in V | \langle a_{i}, w\rangle \ge \alpha_{i} , 1 \le i \le m} \subseteq {w \in V | \langle b, w\rangle \ge \beta }$$
Nghiệm đúng khi và chỉ khi ở đó tồn tại $\lambda_{1} , \dots  , \lambda_{m}  \in \mathbb{R}$ sao cho $\lambda_{i}  \ge 0$ cho $i = 1, \dots  , m$ và
$$b = \sum_{i=1}^{m}  \lambda_{i} a_{i}$$
$$\beta  \le \sum_{i=1}^{m}  \lambda_{i} \alpha_{i} .$$
