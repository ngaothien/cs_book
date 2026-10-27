# Phân rã sơ cấp (primary decomposition) Định lý


<!-- PAGE 1113 -->

## 31.4 Phân rã sơ cấp (primary decomposition) Định lý

Nếu $f$: $E \to E$ là ánh xạ tuyến tính (linear map) và $\lambda  \in K$ là trị riêng (eigenvalue) của $f$, nhắc lại rằng không gian riêng (eigenspace) $E_{\lambda}$ liên kết với $\lambda$ là hạt nhân (kernel) của ánh xạ tuyến tính (linear map) $\lambda$ id - $f$. Nếu tất cả các trị riêng (eigenvalues) $\lambda_{1}  \dots  , \lambda_{k}$ của $f$ là trong $K$, nó có thể xảy ra rằng
$$E = E_{\lambda1} \oplus \cdots  \oplus E_{\lambda k},$$
Nhưng nói chung có không đủ các vectơ riêng (eigenvectors) đến sinh (span) $E$. Những gì nếu ta tổng quát hóa khái niệm của vectơ riêng (eigenvector) và nhìn cho (khác không) các vectơ $u$ sao cho
$$(\lambda id -f)^{r}(u) = 0,for some r \ge 1?$$
Hóa ra là nếu đa thức tối tiểu (minimal polynomial) của $f$ là của tạo thành
$$m = (X -\lambda_{1} )^{r1}\cdots  (X -\lambda_{k} )^{rk},$$
Thì $r = r_{i}$ thực hiện job cho $\lambda_{i}$; rằng là, nếu ta cho
$$W_{i} = \mathrm{Ker} (\lambda_{i} id -f)^{ri},$$
Thì
$$E = W_{1} \oplus \cdots  \oplus W_{k}.$$
Kết quả này là rất đẹp nhưng dường như đến đòi hỏi rằng các trị riêng (eigenvalues) của $f$ tất cả thuộc đến $K$. Thực sự, nó là đặc biệt trường hợp của nhiều hơn/thêm tổng quát kết quả liên quan đến nhân tử hóa của đa thức tối tiểu (minimal polynomial) $m$ vào của nó bất khả quy (irreducible) chuẩn hóa (monic) các nhân tử (xem Định lý 30.17),
$$m = p_{1}^{r1} \cdots  p_{k}^{rk} ,$$
Ở đâu $p_{i}$ là phân biệt bất khả quy (irreducible) chuẩn hóa (monic) các đa thức trên $K$.

> **Định lý 31.10.** (Phân rã sơ cấp (primary decomposition) Định lý) Cho $f$: $E \to E$ là ánh xạ tuyến tính (linear map) trên không gian vectơ hữu hạn chiều $E$ trên trường $K$. Viết đa thức tối tiểu (minimal polynomial) $m$ của $f$ như
$$m = p_{1}^{r1} \cdots  p_{k}^{rk} ,$$
Ở đâu $p_{i}$ là phân biệt bất khả quy (irreducible) chuẩn hóa (monic) các đa thức trên $K$, và $r_{i}$ là dương các số nguyên. Cho
$$W_{i} = \mathrm{Ker} (p_{i}^{ri} (f)),i = 1, \dots  , k.$$
Thì
() $E = W_{1} \oplus \cdots  \oplus W_{k}$.
$(b)$ Mỗi $W_{i}$ là bất biến dưới $f$.
$(c)$ đa thức tối tiểu (minimal polynomial) của thu hẹp $f$ | $W_{i}$ của $f$ đến $W_{i}$ là $p_{i}^{ri}$.

<!-- PAGE 1114 -->

*Chứng minh.* mẹo/kỹ thuật là để xây dựng các phép chiếu $\pi_{i}$ bằng cách sử dụng các đa thức $p_{j}^{rj}$ sao cho miền giá trị (range) của $\pi_{i}$ bằng $W_{i}$. Cho
$$g_{i} = m/p_{i}^{ri} = \prod_{j\neq i}  p_{j}^{rj} .$$
Lưu ý rằng
$$p_{i}^{ri} g_{i} = m.$$
Vì $p_{1}, \dots  , p_{k}$ là bất khả quy (irreducible) và phân biệt, chúng là một cách tương đối nguyên tố. Thì bằng cách sử dụng Mệnh đề 30.14, nó là dễ để chỉ ra rằng $g_{1}, \dots  , g_{k}$ là một cách tương đối nguyên tố. Ngược lại, một số bất khả quy (irreducible) đa thức $p$ sẽ chia tất cả của $g_{1}, \dots  , g_{k}$, do đó theo Mệnh đề 30.14 nó sẽ là bằng một của bất khả quy (irreducible) các nhân tử $p_{i}$. Nhưng rằng $p_{i}$ là missing từ $g_{i}$, một mâu thuẫn. Vì vậy, theo Mệnh đề 30.15, ở đó tồn tại một số các đa thức $h_{1}, \dots  , h_{k}$ sao cho
$$g_{1}h_{1} + \cdots  + g_{k}h_{k} = 1.$$
Cho $q_{i} = g_{i}h_{i}$ và cho $\pi_{i}  = q_{i}(f) = g_{i}(f)h_{i}(f)$. Ta có
$$q_{1} + \cdots  + q_{k} = 1,$$
Và vì $m$ chia hết $q_{i}q_{j}$ cho $i \neq  j$, ta thu được
$$\pi_{1}  + \cdots  + \pi_{k}  = id$$
$$\pi_{i} \pi_{j}  = 0,i \neq  j.$$
(Ta một cách ẩn được sử dụng sự kiện rằng nếu $p, q$ là hai các đa thức, các ánh xạ tuyến tính (linear maps) p(f) $\circ$ q(f) và q(f) $\circ$ p(f) là cùng vì p(f) và q(f) là các đa thức trong các lũy thừa của $f$, mà giao hoán.) Composing phương trình thứ nhất với $\pi_{i}$ và bằng cách sử dụng phương trình thứ hai, ta thu được
$$\pi_{i}^{2}  = \pi_{i} .$$
Vì vậy, $\pi_{i}$ là các phép chiếu, và $E$ là tổng trực tiếp (direct sum) của các ảnh của $\pi_{i}$. Thật vậy, mọi $u \in E$ có thể được biểu diễn dưới dạng
$$u = \pi_{1} (u) + \cdots  + \pi_{k} (u).$$
Cũng, nếu
$$\pi_{1} (u) + \cdots  + \pi_{k} (u) = 0,$$
Thì bằng cách áp dụng $\pi_{i}$ ta thu được
$$0 = \pi_{i}^{2}  (u) = \pi_{i} (u),i = 1, \dots  k.$$
Đến hoàn tất chứng minh (), ta cần để chỉ ra rằng
$$W_{i} = \mathrm{Ker} (p_{i}^{ri} (f)) = \pi_{i} (E).$$

<!-- PAGE 1115 -->
Nếu $v \in \pi_{i} (E)$, thì $v = \pi_{i} (u)$ với một số $u \in E$, do đó
$$p_{i}^{ri} (f)(v) = p_{i}^{ri} (f)(\pi_{i} (u))$$
$$= p_{i}^{ri} (f)g_{i}(f)h_{i}(f)(u)$$
$$= h_{i}(f)p_{i}^{ri} (f)g_{i}(f)(u)$$
$$= h_{i}(f)m(f)(u) = 0,$$
Bởi vì $m$ là đa thức tối tiểu (minimal polynomial) của $f$. Vì vậy, $v \in W_{i}$. Ngược lại, giả sử rằng $v \in W_{i} =$ Ker $(p_{i}^{ri} (f))$. Nếu $j \neq  i$, thì $g_{j}h_{j}$ là chia hết bởi $p_{i}^{ri}$, do đó
$$g_{j}(f)h_{j}(f)(v) = \pi_{j} (v) = 0,j \neq  i.$$
Khi đó vì $\pi_{1}  + \cdots  + \pi_{k}  =$ id, ta có $v = \pi_{i} v$, mà chỉ ra rằng $v$ là trong miền giá trị (range) của $\pi_{i}$. Vì vậy, $W_{i} = Im(\pi_{i}$), và điều này các hoàn tất chứng minh của (). Nếu $p_{i}^{ri}$ (f)(u) $= 0$, thì $p_{i}^{ri}$ (f)(f(u)) $= f(p_{i}^{ri}$ (f)(u)) $= 0$, do đó $(b)$ nghiệm đúng. Nếu ta viết $f_{i} = f$ | $W_{i}$, thì $p_{i}^{ri} (f_{i}) = 0$, bởi vì $p_{i}^{ri} (f) = 0$ trên $W_{i}$ (hạt nhân (hạt nhân (kernel)) của nó). Vì vậy, đa thức tối tiểu (minimal polynomial) của $f_{i}$ chia hết $p_{i}^{ri}$. Ngược lại, cho $q$ là bất kỳ đa thức sao cho $q(f_{i}) = 0$ (trên $W_{i})$. Vì $m = p_{i}^{ri} g_{i}$, sự kiện rằng m(f)(u) $= 0$ với mọi $u \in E$ chỉ ra rằng
$$p_{i}^{ri} (f)(g_{i}(f)(u)) = 0,u \in E,$$
Và do đó $Im(g_{i}(f)) \subseteq$ Ker $(p_{i}^{ri} (f)) = W_{i}$. Hệ quả là, vì q(f) là không trên $W_{i}$,
$$q(f)g_{i}(f) = 0for all u \in E.$$
Nhưng khi đó $qg_{i}$ là chia hết bởi đa thức tối tiểu (minimal polynomial) $m = p_{i}^{ri} g_{i}$ của $f$, và vì $p_{i}^{ri}$ và $g_{i}$ là một cách tương đối nguyên tố, bởi Euclid’s mệnh đề, $p_{i}^{ri}$ phải chia $q$. Điều này các hoàn tất chứng minh rằng đa thức tối tiểu (minimal polynomial) của $f_{i}$ là $p_{i}^{ri}$, mà là $(c)$. Đến tốt nhất understand phép chiếu các cách xây dựng của Định lý 31.10, ta cung cấp sau đây hai tường minh các ví dụ của phân rã sơ cấp (primary decomposition) định lý.
$$\mathbb{R}^{3} \mathbb{R}^{3}$$

> **Ví dụ 31.2.** Thứ nhất cho $f$: $\to$ được định nghĩa như f(x, $y, z) = (y, x, z)$. Theo
$$standard basis f is represented by the 3 \times  3 matrix X_{f} := \begin{pmatrix} - \\ 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} . Then a simple$$
Phép tính chỉ ra rằng $m_{f}(x) = \chi_{f} (x) = (x^{2}+1)(x-1)$. Bằng cách sử dụng ký hiệu của trước đó chứng minh tập hợp
$$m = p_{1}p_{2},p_{1} = x^{2}+ 1,p_{2} = x -1.$$
Thì
$$g_{1} = \frac{m}{p_{1}} = x -1,g_{2} = \frac{m}{p_{2}} = x^{2}+ 1.$$

<!-- PAGE 1116 -->
Ta phải tìm $h_{1}, h_{2} \in \mathbb{R}[x]$ sao cho $g_{1}h_{1} + g_{2}h_{2} = 1$. Nói chung điều này là khó phần của phép chiếu cách xây dựng. Nhưng vì ta là chỉ làm việc với hai một cách tương đối nguyên tố các đa thức $g_{1}, g_{2}$, ta có thể áp dụng Euclidean thuật toán đến discover rằng
$$+ 1) = 1$$
$$- \frac{x + 1}{2} (x -1) + \frac{1}{2} (x^{2},$$
Ở đâu $h_{1} = -_{2}^{x+1}$ trong khi $h_{2} =_{2}^{1}$. Theo Định nghĩa
$$\pi_{1}  = g_{1}(f)h_{1}(f) = - \frac{1}{2} (X_{f} -id)(X_{f} + id) = - \frac{1}{2} (X_{f}^{2} -id) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} ,$$
Và
$$\pi_{2}  = g_{2}(f)h_{2}(f) = \frac{1}{2} (X_{f}^{2} + id) = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} .$$
$\mathbb{R}^{3}$ Thì $= W_{1} \oplus W_{2}$, ở đâu
$$000$$
$W_{1} = \pi_{1} (\mathbb{R}^{3}) =$ Ker $(p_{1}(X_{f})) =$ Ker $(X_{f}^{2} +$ id) $=$ Ker $0 0 0 = {(x, y, 0) \in \mathbb{R}^{3}}$,
$$$$
$$001$$
$$-1-10$$
$W_{2} = \pi_{2} (\mathbb{R}^{3}) =$ Ker $(p_{2}(X_{f})) =$ Ker $(X_{f}$ - id) $=$ Ker $1 -1 0 = {(0, 0, z) \in \mathbb{R}^{3}}$.
$$$$
$$000$$
$$\mathbb{R}^{3}$$

> **Ví dụ 31.3.** Cho của ta thứ hai ví dụ của phân rã sơ cấp (primary decomposition) định lý cho $f$: $\to \mathbb{R}^{3}$ được định nghĩa như f(x, $y, z) = (y, -x + z, -y)$, với tiêu chuẩn ma trận biểu diễn $X_{f} =$
$$\begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix} . A simple calculation shows that m_{f}(x) = \chi_{f} (x) = x(x^{2} + 2). Set$$
$$p_{1} = x^{2}+ 2,p_{2} = x,g_{1} = \frac{m_{f}}{p_{1}} = x,g_{2} = \frac{m_{f}}{p_{2}} = x^{2}+ 2.$$
Vì $gcd(g_{1}, g_{2}) = 1$, ta sử dụng Euclidean thuật toán để tìm
$$h_{1} = - \frac{1}{2} x,h_{2} = \frac{1}{2} ,$$
Sao cho $g_{1}h_{1} + g_{2}h_{2} = 1$. Thì
$$\pi_{1}  = g_{1}(f)h_{1}(f) = - \frac{1}{2} X_{f}^{2} = \begin{pmatrix} 1 & 0 & -^{1} \\ 0\overline{2} & 1 & 0^{2} \\ 0 & 1 \end{pmatrix} ,$$
$$-_{2}^{1}$$
$$\overline{2}$$

<!-- PAGE 1117 -->
Trong khi
$$\pi_{2}  = g_{2}(f)h_{2}(f) = \frac{1}{2} (X_{f}^{2} + 2id) = \begin{pmatrix} 1 & 0_{2}^{1} \\ 0\overline{2} & 0 & 0 \\ 1 & 0_{2}^{1} \end{pmatrix} .$$
$$\overline{2}$$
Mặc dù nó là không hoàn toàn hiển nhiên, $\pi_{1}$ và $\pi_{2}$ là thật vậy các phép chiếu vì
$$\pi_{1}^{2}  = \begin{pmatrix} 1 & 0 & -^{1} \\ 0\overline{2} & 1 & 0^{2} \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & -^{1} \\ 0\overline{2} & 1 & 0^{2} \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & -^{1} \\ 0\overline{2} & 1 & 0^{2} \\ 0 & 1 \end{pmatrix} = \pi_{1} ,$$
$$-_{2}^{1}-_{2}^{1}-_{2}^{1}$$
$$\overline{2}\overline{2}\overline{2}$$
Và
$$\pi_{2}^{2}  = \begin{pmatrix} 1 & 0_{2}^{1} \\ 0\overline{2} & 0 & 0 \\ 1 & 0_{2}^{1} \end{pmatrix} \begin{pmatrix} 1 & 0_{2}^{1} \\ 0\overline{2} & 0 & 0 \\ 1 & 0_{2}^{1} \end{pmatrix} = \begin{pmatrix} 1 & 0_{2}^{1} \\ 0\overline{2} & 0 & 0 \\ 1 & 0_{2}^{1} \end{pmatrix} = \pi_{2} .$$
$$\overline{2}\overline{2}\overline{2}$$
Hơn nữa nhận thấy rằng $\pi_{1}  + \pi_{2}  =$ id. phân rã sơ cấp (primary decomposition) định lý suy ra rằng $\mathbb{R}^{3} = W_{1} \oplus W_{2}$ ở đâu
$$W_{1} = \pi_{1} (\mathbb{R}^{3}) = \mathrm{Ker} (p_{1}(f)) = \mathrm{Ker} (X^{2} + 2) = \mathrm{Ker} \begin{pmatrix} 1 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 1 \end{pmatrix} = span{(0, 1, 0), (1, 0, -1)},$$
$W_{2} = \pi_{2} (\mathbb{R}^{3}) =$ Ker $(p_{2}(f)) =$ Ker $(X) = span{(1, 0, 1)}$. Xem Hình 31.1. Nếu tất cả các trị riêng (eigenvalues) của $f$ thuộc đến trường $K$, ta thu được kết quả sau kết quả.

> **Định lý 31.11.** (Phân rã sơ cấp (primary decomposition) Định lý, Phiên bản $2)$ Cho $f$: $E \to E$ là ánh xạ tuyến tính (linear map) trên không gian vectơ hữu hạn chiều $E$ trên trường $K$. Nếu tất cả các trị riêng (eigenvalues) $\lambda_{1} , \dots  , \lambda_{k}$ của $f$ thuộc đến $K$, viết
$$m = (X -\lambda_{1} )^{r1}\cdots  (X -\lambda_{k} )^{rk}$$
Cho đa thức tối tiểu (minimal polynomial) của $f$,
$$\chi_{f}  = (X -\lambda_{1} )^{n1}\cdots  (X -\lambda_{k} )^{nk}$$
Cho đa thức đặc trưng (characteristic polynomial) của $f$, với $1 \le r_{i} \le n_{i}$, và cho
$$W_{i} = \mathrm{Ker} (\lambda_{i} id -f)^{ri},i = 1, \dots  , k.$$
Thì
() $E = W_{1} \oplus \cdots  \oplus W_{k}$.

<!-- PAGE 1118 -->
$$\mathbb{R}^{3}$$

![Figure 31.1](../../assets/ch31/fig_31_1.png)

**Hình 31.1:** tổng trực tiếp (direct sum) phân rã của $= W_{1}\oplus W_{2}$ ở đâu $W_{1}$ là mặt phẳng $x+z = 0$ và $W_{2}$ là đường thẳng t(1, $0, 1)$. sinh các vectơ của $W_{1}$ là trong xanh lam.
$(b)$ Mỗi $W_{i}$ là bất biến dưới $f$.
$(c) dim(W_{i}) = n_{i}$.
$(d)$ đa thức tối tiểu (minimal polynomial) của thu hẹp $f$ | $W_{i}$ của $f$ đến $W_{i}$ là $(X$ - $\lambda_{i} )^{ri}$.

*Chứng minh.* Các phần (), $(b)$ và $(d)$ có đã đã được được chứng minh trong Định lý 31.10, do đó nó vẫn còn để chứng minh $(c)$. Vì $W_{i}$ là bất biến dưới $f$, cho $f_{i}$ là thu hẹp của $f$ đến $W_{i}$. đa thức đặc trưng (characteristic polynomial) $\chi_{fi}$ của $f_{i}$ chia hết $\chi (f)$, và vì $\chi (f)$ có tất cả của nó các nghiệm trong $K$, do đó thực hiện $\chi_{i} (f)$. Theo Định lý 15.5, có một cơ sở (basis) của $W_{i}$ trong mà $f_{i}$ được biểu diễn bởi tam giác trên (upper triangular) ma trận, và vì $(\lambda_{i}$ id - $f)^{ri} = 0$, đường chéo các phần tử (entries) của ma trận này bằng $\lambda_{i}$. Hệ quả là,
$$\chi_{fi}  = (X -\lambda_{i} )^{\dim(Wi)},$$
Và vì $\chi_{fi}$ chia hết $\chi (f)$, ta kết luận hat
$$\dim(W_{i}) \le n_{i},i = 1, \dots  , k.$$
Bởi vì $E$ là tổng trực tiếp (direct sum) của $W_{i}$, ta có $dim(W_{1}) + \cdots  + dim(W_{k}) = n$, và vì $n_{1} + \cdots  + n_{k} = n$, ta phải có
$$\dim(W_{i}) = n_{i},i = 1, \dots  , k,$$
Chứng minh $(c)$.
