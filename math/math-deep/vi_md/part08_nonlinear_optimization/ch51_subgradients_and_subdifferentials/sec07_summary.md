# Tóm tắt


<!-- PAGE 1900 -->

> **Định lý 51.43.** (Định lý 28.4, Rockafellar) Cho $(P)$ là thông thường lồi bài toán quy hoạch với
$$\mathbb{R}_{+}^{m}\mathbb{R}^{p} \mathbb{R}^{n}$$
Hàm Lagrange (Lagrangian) L(x, $\lambda , \mu$). Nếu Các nhân tử Lagrange (Lagrange multipliers) $(\lambda^{*} , \mu^{*}$) $\in  \times$ và vectơ $x^{*} \in$ có tính chất rằng
() cận dưới đúng (infimum) của hàm $h = J + m  \lambda_{i}^{*}  \phi_{i}  + p  \mu_{j}^{*} \psi_{j}$ là hữu hạn và bằng
$$optimal value of over, and \sum_{i}  =1 \sum  j=1$$
$$J U$$
$(b)$ vectơ $x^{*}$ là nghiệm tối ưu (optimal solution) của $(P)$ (do đó $x^{*} \in U)$, thì saddle giá trị $L(x^{*}, \lambda^{*} , \mu^{*}$) là giá trị tối ưu (optimal value) $J(x^{*})$ của $(P)$.
$$\mathbb{R}_{+}^{m}\mathbb{R}^{p}$$
Tổng quát hơn, Các nhân tử Lagrange (Lagrange multipliers) $(\lambda^{*} , \mu^{*}$) $\in  \times$ có Tính chất () khi và chỉ khi
$$-\infty < \inf L(x, \lambda^{*} , \mu^{*} ) \le supinf L(x, \lambda , \mu ) = \inf supL(x, \lambda , \mu ),$$
$$x\lambda ,\mu xx\lambda ,\mu$$
Trong mà trường hợp, chung/phổ biến giá trị của cực trị giá trị là giá trị tối ưu (optimal value) của $(P)$. Đặc biệt, nếu $x^{*}$ là nghiệm tối ưu (optimal solution) cho $(P)$, thì $sup_{\lambda ,\mu} G(\lambda , \mu$) $= L(x^{*}, \lambda^{*} , \mu^{*}$) $= J(x^{*})$ (không khoảng cách đối ngẫu (duality gap)). Nhận thấy rằng Định lý 51.43 cho đủ Các điều kiện () và $(b)$ cho khoảng cách đối ngẫu (duality gap) là không. Xét theo Định lý 51.41, các điều kiện này là tương đương đến sự kiện rằng $(x^{*}, \lambda^{*} , \mu^{*}$) là điểm yên ngựa (saddle point) của $L$, hoặc tương đương rằng KKT các điều kiện đúng. Một lần nữa, theo Định lý 51.40, nếu giá trị tối ưu (optimal value) của $(P)$ là hữu hạn và nếu các ràng buộc là qualified, thì Điều kiện () của Định lý 51.43 nghiệm đúng cho $(\lambda , \mu$). Thì sau đây hệ quả của Định lý 51.43 nghiệm đúng.

> **Định lý 51.44.** (Định lý 28.4.1, Rockafellar) Cho $(P)$ là thông thường lồi bài toán quy hoạch thỏa mãn giả thiết của Định lý 51.40, mà có nghĩa là giá trị tối ưu (optimal value) của $(P)$ là
$$\mathbb{R}_{+}^{m}\mathbb{R}^{p}$$
Hữu hạn, và rằng các ràng buộc là qualified. Các nhân tử Lagrange (Lagrange multipliers) $(\lambda , \mu$) $\in  \times$ rằng có tính chất rằng cận dưới đúng (infimum) của hàm $h = J + m  \lambda_{i} \phi_{i}  + p  \mu_{j} \psi_{j}$ là hữu hạn
$$and equal to the optimal value of over are exactly the vectors \sum_{i}  =1 where the^{j=1} \sum  dual function$$
$$J U G$$
Đạt là cận trên đúng (supremum) trên $\mathbb{R}^{n}$. Định lý 51.44 là suy rộng/tổng quát hóa và mạnh hơn phiên bản của Định lý 50.19(2). Phần $(1)$ của Định lý 50.19 đòi hỏi $J$ và $\phi_{i}$ là khả vi (differentiable), do đó nó thực hiện không tổng quát hóa. Nhiều hơn/thêm các kết quả có thể được hiển thị về thông thường lồi các bài toán quy hoạch, và một cái khác lớp của các bài toán quy hoạch được gọi là suy rộng/tổng quát hóa lồi các bài toán quy hoạch. Tuy nhiên, ta thực hiện không cần như vậy resuts cho của ta các mục đích, đặc biệt đến thảo luận ADMM phương pháp. interested độc giả là referred đến Rockafellar $[143]$ (Phần VI, Các mục $28$ và $29)$.

## 51.7 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ Được mở rộng nhận giá trị thực (real-valued) các hàm.

<!-- PAGE 1901 -->
$\bullet$ Trên đồ thị (epigraph) (epi(f)). $\bullet$ Lồi và lõm (được mở rộng nhận giá trị thực (real-valued)) các hàm. $\bullet$ Effective miền xác định (dom(f)). $\bullet$ Thực sự/đúng đắn và suy rộng/không thực sự các hàm lồi. $\bullet$ Sublevel các tập hợp. $\bullet$ Thấp hơn nửa liên tục (semi-continuous) các hàm. $\bullet$ Thấp hơn nửa liên tục (semi-continuous) bao (hull); bao đóng (closure) của hàm lồi (convex function). $\bullet$ Tương đối phần trong (interior) (relint(C)). $\bullet$ Indicator hàm. $\bullet$ Lipschitz điều kiện. $\bullet$ Afin tạo thành, afin siêu phẳng (hyperplane). $\bullet$ Một nửa các không gian. $\bullet$ Tựa/hỗ trợ siêu phẳng (hyperplane). $\bullet$ Chuẩn tắc/bình thường nón tại $a. \bullet$ Dưới gradien (subgradient), dưới gradien (subgradient) bất đẳng thức, vi phân dưới (subdifferential). $\bullet$ Minkowski’s tựa/hỗ trợ siêu phẳng (hyperplane) định lý. $\bullet$ Một phía đạo hàm theo hướng (directional derivative). $\bullet$ Hỗ trợ/giá (support) hàm. $\bullet$ ReLU hàm. $\bullet  \epsilon$ -dưới gradien (subgradient). $\bullet$ Cực tiểu tập hợp của hàm lồi (convex function). $\bullet$ Hướng của recession. $\bullet$ Thông thường lồi các bài toán quy hoạch. $\bullet$ Tập hợp của chấp nhận được (feasible) các nghiệm. $\bullet$ Hàm Lagrange (Lagrangian).
