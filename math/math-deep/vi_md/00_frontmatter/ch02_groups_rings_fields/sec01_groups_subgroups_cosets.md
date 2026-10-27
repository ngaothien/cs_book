# 2.1 Nhóm, Nhóm Con, Lớp Ghép (Groups, Subgroups, Cosets)

> **Trang gốc:** 21–44

Tập hợp $\mathbb{R}$ các số thực có hai phép toán $+ : \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ (phép cộng – *addition*) và $* : \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ (phép nhân – *multiplication*) thỏa mãn các tính chất làm cho $\mathbb{R}$ trở thành một nhóm Abel (*abelian group*) dưới phép $+$, và $\mathbb{R} - \{0\} = \mathbb{R}^*$ trở thành một nhóm Abel dưới phép $*$.

Trước khi phát biểu định nghĩa hình thức của một nhóm (*group*), chúng ta bắt đầu với một số ví dụ cụ thể. Nhiều tập hợp các phép biến đổi hình học (*geometric transformations*) mang cấu trúc nhóm:

1. Phép tịnh tiến (*Translations*)
2. Phép quay (*Rotations*)
3. Phép vị tự / Phép phóng đại (*Magnifications*)
4. Phép dời hình cứng (*Rigid motions*), kết hợp giữa phép quay và phép tịnh tiến
5. Phép đối xứng / Phép phản xạ (*Reflections*)
6. Phép biến đổi trực giao (*Orthogonal transformations*, kết hợp giữa phép quay và phép đối xứng)
7. Phép dời hình cứng và phép dời hình cứng ngược hướng (*Rigid motions and indirect rigid motions*)
8. Tổng quát hơn, các phép biến đổi affine khả nghịch (*affine invertible transformations*).

<!-- PAGE 22 -->

> **Ví dụ 2.1 (Example 2.1).** Một phép tịnh tiến (*translation*) trong mặt phẳng $\mathbb{R}^2$ là một ánh xạ $T_u : \mathbb{R}^2 \to \mathbb{R}^2$ được xác định bởi một vectơ
> $$u = \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} \in \mathbb{R}^2, \quad \text{với } u_1, u_2 \in \mathbb{R},$$
> sao cho tác động (*action*) của $T_u$ lên một vectơ (cũng được gọi là điểm)
> $$x = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} \in \mathbb{R}^2, \quad \text{với } x_1, x_2 \in \mathbb{R},$$
> được cho bởi $T_u(x) = x + u$, nghĩa là:
> $$T_u(x) = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} + \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} = \begin{pmatrix} x_1 + u_1 \\ x_2 + u_2 \end{pmatrix}.$$
> Như vậy, điểm $x$ trong mặt phẳng ($\mathbb{R}^2$) được tịnh tiến "dọc theo vectơ $u$".
>
> Ký hiệu tập hợp các phép tịnh tiến trên mặt phẳng $\mathbb{R}^2$ là $T(\mathbb{R}^2)$. Các phép tịnh tiến có thể được hợp thành (*composed*). Cho hai phép tịnh tiến $T_u$ và $T_v$ được xác định bởi
> $$u = \begin{pmatrix} u_1 \\ u_2 \end{pmatrix}, \quad v = \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} \in \mathbb{R}^2,$$
> trước hết ta áp dụng $T_u$ lên $x$, rồi áp dụng $T_v$ lên $T_u(x)$, và ta thu được:
> $$(T_v \circ T_u)(x) = T_v(T_u(x)) = \left(\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} + \begin{pmatrix} u_1 \\ u_2 \end{pmatrix}\right) + \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} x_1 + u_1 \\ x_2 + u_2 \end{pmatrix} + \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}$$
> $$= \begin{pmatrix} (x_1 + u_1) + v_1 \\ (x_2 + u_2) + v_2 \end{pmatrix} = \begin{pmatrix} x_1 + (u_1 + v_1) \\ x_2 + (u_2 + v_2) \end{pmatrix} = T_{u+v}(x),$$
> do đó $T_v \circ T_u$ được xác định bởi vectơ $u + v$, điều này có nghĩa là
> $$T_v \circ T_u = T_{u+v}.$$
>
> Chúng ta vừa định nghĩa một phép toán hai ngôi (*binary operation*)
> $$\circ : T(\mathbb{R}^2) \times T(\mathbb{R}^2) \to T(\mathbb{R}^2)$$
> trên tập hợp các phép tịnh tiến (trên $\mathbb{R}^2$) cho bởi
> $$T_v \circ T_u = T_{u+v}.$$
> Chú ý rằng
> $$T_v \circ T_u = T_u \circ T_v, \tag{Ab}$$
> <!-- PAGE 23 -->
> vì $T_v \circ T_u = T_{u+v} = T_{v+u} = T_u \circ T_v$, và $u + v = v + u$ (với tư cách là các vectơ trong $\mathbb{R}^2$). Ta nói phép toán này có tính giao hoán (*commutative*).
>
> Với $u = 0_2$, tức vectơ không
> $$0_2 = \begin{pmatrix} 0 \\ 0 \end{pmatrix},$$
> ta thu được phép tịnh tiến $T_{0_2}$ giữ nguyên mọi điểm, cụ thể là
> $$T_{0_2}(x) = x, \quad x \in \mathbb{R}^2.$$
> Nhận thấy rằng với mọi phép tịnh tiến $T_u$, ta có
> $$T_u \circ T_{0_2} = T_{0_2} \circ T_u = T_u. \tag{G2}$$
> Ta nói $T_{0_2}$ là phần tử đơn vị (*identity element*) hay phần tử trung hòa (*neutral element*) đối với phép toán hai ngôi $\circ$.
>
> Với ba phép tịnh tiến bất kỳ $T_u, T_v, T_w$, ta có đồng nhất thức
> $$(T_u \circ T_v) \circ T_w = T_u \circ (T_v \circ T_w), \tag{G1}$$
> vì cả hai vế đều bằng $T_{u+v+w}$, do $(u + v) + w = u + (v + w)$ là các vectơ trong $\mathbb{R}^2$. Ta nói phép toán $\circ$ có tính kết hợp (*associative*).
>
> Cũng lưu ý rằng $T_{-u}$ là phần tử nghịch đảo (*inverse*) của $T_u$, theo nghĩa là
> $$T_{-u} \circ T_u = T_{0_2} = T_u \circ T_{-u}, \tag{G3}$$
> bởi vì $T_{-u} \circ T_u = T_{-u+u} = T_{0_2} = T_{u+(-u)} = T_u \circ T_{-u}$.
>
> Vì các Điều kiện G1, G2, G3 (xem Định nghĩa 2.1) đều thỏa mãn đối với phép toán $\circ$ trên tập hợp $T(\mathbb{R}^2)$ gồm các phép tịnh tiến (trên $\mathbb{R}^2$), ta nói tập hợp $T(\mathbb{R}^2)$ là một nhóm (*group*).
>
> Bởi vì điều kiện $(\mathrm{Ab})$ cũng thỏa mãn, ta nói nhóm này là nhóm giao hoán (*commutative*) hay nhóm Abel (*abelian*). Mặt khác, $\mathbb{R}^2$ dưới phép cộng vectơ cũng là một nhóm Abel với phần tử đơn vị là $0_2$.
>
> Ánh xạ $u \mapsto T_u$ là một song ánh (*bijection*) từ nhóm $\mathbb{R}^2$ lên nhóm $T(\mathbb{R}^2)$ các phép tịnh tiến trên $\mathbb{R}^2$. Đây là một đẳng cấu nhóm (*group isomorphism*).
>
> Lưu ý rằng các phần tử của nhóm $T(\mathbb{R}^2)$ là các phép biến đổi (các ánh xạ từ $\mathbb{R}^2$ vào $\mathbb{R}^2$), trong khi các phần tử của $\mathbb{R}^2$ là các vectơ. Việc tổng quát hóa lên $\mathbb{R}^n$ và nhóm các phép tịnh tiến trên $\mathbb{R}^n$ là hoàn toàn tương tự.

<!-- PAGE 24 -->

> **Ví dụ 2.2 (Example 2.2).** Một điểm $(x, y)$ trong mặt phẳng $\mathbb{R}^2$ có thể được xác định bởi tọa độ cực (*polar coordinates*) $(r, \alpha)$ của nó, vì ta có thể viết
> $$\begin{aligned} x &= r \cos \alpha \\ y &= r \sin \alpha, \end{aligned}$$
> với mọi
> $$\begin{pmatrix} x \\ y \end{pmatrix} \in \mathbb{R}^2,$$
> và nếu $(x, y) \neq (0, 0)$, thì $r > 0$ và $\alpha$ được xác định duy nhất nếu ta yêu cầu $0 \le \alpha < 2\pi$.
>
> Một cách tương đương, ta xét $\alpha$ theo modulo $2\pi$, nghĩa là ta coi $\alpha_1$ và $\alpha_2$ là tương đương khi và chỉ khi
> $$\alpha_2 - \alpha_1 = 2\pi k, \quad k \in \mathbb{Z}.$$
> Ta thu được tập hợp các lớp tương đương (*equivalence classes*) $\mathbb{R}/(2\pi\mathbb{Z})$. (Đó là một nhóm dưới phép cộng $\bmod\; 2\pi\mathbb{Z}$!).
>
> Một phép quay (*rotation*) $R_\theta$ một góc $\theta$ là ánh xạ $R_\theta : \mathbb{R}^2 \to \mathbb{R}^2$ cho bởi
> $$\begin{aligned} R_\theta(0, 0) &= (0, 0) \\ R_\theta(r, \alpha) &= (r, \alpha + \theta), \quad (r \neq 0). \end{aligned}$$
> Phép quay $R_\theta$ quay điểm có tọa độ cực $(r, \alpha)$ đi một góc $\theta$ tới điểm $(r, \alpha + \theta)$.
>
> Vì tọa độ cực của $R_\theta(r, \alpha)$ cho tọa độ Đề-các là
> $$(r \cos(\alpha + \theta), r \sin(\alpha + \theta)),$$
> và vì
> $$\begin{aligned} \cos(\alpha + \theta) &= \cos \alpha \cos \theta - \sin \alpha \sin \theta \\ \sin(\alpha + \theta) &= \sin \alpha \cos \theta + \cos \alpha \sin \theta, \end{aligned}$$
> ta thấy rằng dưới dạng ma trận,
> $$\begin{pmatrix} r \cos(\alpha + \theta) \\ r \sin(\alpha + \theta) \end{pmatrix} = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} \begin{pmatrix} r \cos \alpha \\ r \sin \alpha \end{pmatrix}.$$
> Theo tọa độ Đề-các (*cartesian coordinates*) $(x, y)$,
> $$R_\theta \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}.$$
> Sử dụng một số hằng đẳng thức lượng giác, ta kiểm tra được rằng ánh xạ
> $$\theta \mapsto M_\theta = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}, \quad \theta \in \mathbb{R}/2\pi\mathbb{Z},$$
> có tính chất
> $$M_\theta M_\phi = M_{\theta + \phi}.$$
> Ta nói rằng $M_\theta$ là ma trận biểu diễn (*matrix representing*) phép quay $R_\theta$.
> <!-- PAGE 25 -->
> Ta có thể kiểm tra rằng các Điều kiện G1, G2, G3 (xem Định nghĩa 2.1) và $(\mathrm{Ab})$ đều thỏa mãn, nên tập hợp các ma trận có dạng
> $$M_\theta = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix},$$
> ký hiệu là $\mathbf{SO}(2)$, là một nhóm Abel dưới phép nhân ma trận
> $$\cdot : \mathbf{SO}(2) \times \mathbf{SO}(2) \to \mathbf{SO}(2).$$
> Về mặt hình học, $\mathbf{SO}(2)$ là đường tròn đơn vị (*unit circle*), ký hiệu là $S^1$. (Đó cũng là tập hợp các số phức có môđun bằng $1$,
> $$\mathbf{U}(1) = \{\cos \theta + i \sin \theta \mid \theta \in \mathbb{R}/2\pi\mathbb{Z}\}.)$$
> Và nhắc lại rằng $\cos \theta + i \sin \theta = e^{i\theta}$.
>
> Phần tử đơn vị là ma trận $M_0$, với
> $$M_0 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2,$$
> và nghịch đảo của $R_\theta$ là phép quay $R_{-\theta}$, tương ứng với ma trận
> $$M_{-\theta} = \begin{pmatrix} \cos \theta & \sin \theta \\ -\sin \theta & \cos \theta \end{pmatrix}.$$
> Lưu ý rằng phép toán trên $\mathbf{SO}(2)$ là phép nhân ma trận chứ không phải phép cộng ma trận (vì phép cộng sẽ tạo ra các ma trận không còn là phép quay). Chú ý rằng ma trận $M_{-\theta}$ gắn với $R_{-\theta}$ chính là ma trận chuyển vị (*transpose*) của ma trận $M_\theta$ gắn với $R_\theta$.

> **Ví dụ 2.3 (Example 2.3).** Với mọi $r > 0$, ta có phép vị tự / phóng đại (*magnification*) $\mu_r : \mathbb{R}^2 \to \mathbb{R}^2$ với tỷ số $r$, được cho bởi
> $$\mu_r(x) = r \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} rx \\ ry \end{pmatrix}.$$
> Ta ký hiệu tập hợp các phép vị tự trên $\mathbb{R}^2$ là $\mathbf{Mag}(2)$. Ta kiểm tra được ngay rằng (với $r_1, r_2 > 0$),
> $$\mu_{r_1} \circ \mu_{r_2} = \mu_{r_2} \circ \mu_{r_1} = \mu_{r_1 * r_2},$$
> và điều này định nghĩa một phép toán nhân $\cdot : \mathbf{Mag}(2) \times \mathbf{Mag}(2) \to \mathbf{Mag}(2)$ cho bởi
> $$\mu_{r_1} \cdot \mu_{r_2} = \mu_{r_1 * r_2}.$$
> Ta có thể kiểm tra rằng các Điều kiện G1, G2, G3 (xem Định nghĩa 2.1) và $(\mathrm{Ab})$ đều thỏa mãn, do đó ta thu được nhóm giao hoán $\mathbf{Mag}(2)$ với phần tử đơn vị $\mu_1$, và phần tử nghịch đảo của $\mu_r$ là $\mu_{1/r}$.
>
> Tập hợp tất cả các phép hợp thành $\mu_r \circ R_\theta$ tương ứng với tất cả các ma trận có dạng
> $$\begin{pmatrix} r \cos \theta & -r \sin \theta \\ r \sin \theta & r \cos \theta \end{pmatrix}.$$
> <!-- PAGE 26 -->
> Ta dễ dàng kiểm tra được rằng đây chính là tập hợp $\mathbf{SIM}_{\mathbb{R}}(2)$ gồm các ma trận có dạng
> $$\begin{pmatrix} a & -b \\ b & a \end{pmatrix}, \quad a^2 + b^2 \neq 0.$$
> Ma trận nghịch đảo của một ma trận như vậy là
> $$\frac{1}{a^2 + b^2} \begin{pmatrix} a & b \\ -b & a \end{pmatrix}.$$
> Ta có thể kiểm tra rằng các Điều kiện G1, G2, G3 (xem Định nghĩa 2.1) và $(\mathrm{Ab})$ đều thỏa mãn, nên tập hợp $\mathbf{SIM}_{\mathbb{R}}(2)$ dưới phép nhân ma trận là một nhóm giao hoán.

> **Ví dụ 2.4 (Example 2.4).** Ngoài các ma trận quay
> $$M_\theta = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix},$$
> chúng ta hãy bổ sung thêm tất cả các ma trận có dạng
> $$\rho_\phi = \begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix},$$
> được gọi là các phép đối xứng / phản xạ (*reflections*), và lập tất cả các tích khả dĩ.
>
> Trái với những gì ta có thể nghĩ, các ma trận đối xứng không phải là ma trận quay. Trước hết, nếu bạn đã biết định thức (*determinant*) của ma trận là gì, thì các ma trận quay có định thức bằng $+1$, nhưng các phép đối xứng có định thức bằng $-1$. Ngoài ra, nếu ta xét phép đối xứng đặc biệt ứng với $\phi = 0$,
> $$\rho_0 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},$$
> tức là phép đối xứng qua trục $x$ (*$x$-axis*), thì ta có
> $$\begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix} = \begin{pmatrix} \cos \phi & -\sin \phi \\ \sin \phi & \cos \phi \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = M_\phi \rho_0,$$
> do đó
> $$\rho_\phi = M_\phi \rho_0.$$
> Sau này chúng ta sẽ thấy rằng $\rho_\phi = M_{\phi/2} \rho_0 M_{-\phi/2}$, cụ thể là
> $$\begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix} = \begin{pmatrix} \cos \phi/2 & -\sin \phi/2 \\ \sin \phi/2 & \cos \phi/2 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} \cos \phi/2 & \sin \phi/2 \\ -\sin \phi/2 & \cos \phi/2 \end{pmatrix},$$
> điều này có nghĩa về mặt hình học là $\rho_\phi$ là phép đối xứng qua đường thẳng tạo với trục hoành một góc $\phi/2$.
> <!-- PAGE 27 -->
> Chú ý rằng vì
> $$\begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix}^2 = \begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix} \begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix}$$
> $$= \begin{pmatrix} \cos^2 \phi + \sin^2 \phi & \cos \phi \sin \phi - \sin \phi \cos \phi \\ \sin \phi \cos \phi - \cos \phi \sin \phi & \sin^2 \phi + \cos^2 \phi \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix},$$
> nên ta có
> $$\rho_\phi^2 = \rho_\phi \rho_\phi = I_2,$$
> vậy phần tử nghịch đảo của một phép đối xứng chính là bản thân nó.
>
> Ta cũng dễ dàng kiểm chứng được rằng
> $$\rho_0 M_\theta \rho_0 = M_{-\theta}.$$
> Thật vậy,
> $$\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} \cos \theta & -\sin \theta \\ -\sin \theta & -\cos \theta \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$
> $$= \begin{pmatrix} \cos \theta & \sin \theta \\ -\sin \theta & \cos \theta \end{pmatrix} = \begin{pmatrix} \cos(-\theta) & -\sin(-\theta) \\ \sin(-\theta) & \cos(-\theta) \end{pmatrix}.$$
>
> Gọi $\mathbf{O}(2)$ là tập hợp được cho bởi
> $$\begin{aligned} \mathbf{O}(2) &= \mathbf{SO}(2) \cup \{M_\phi \rho_0 \mid M_\phi \in \mathbf{SO}(2)\} \\ &= \mathbf{SO}(2) \cup \{\rho_\phi \mid \phi \in \mathbb{R}/(2\pi\mathbb{Z})\}. \end{aligned}$$
> Vì $\rho_0 \rho_0 = I_2$ và $\rho_0 M_\theta \rho_0 = M_{-\theta}$, các phương trình sau đây thỏa mãn:
> $$\begin{aligned} M_\theta M_\phi &= M_{\theta + \phi} \\ M_\theta \rho_\phi &= M_\theta (M_\phi \rho_0) = (M_\theta M_\phi)\rho_0 = M_{\theta + \phi}\rho_0 = \rho_{\theta + \phi} \\ \rho_\theta M_\phi &= (M_\theta \rho_0)M_\phi = (M_\theta \rho_0)(M_\phi \rho_0 \rho_0) = M_\theta(\rho_0 M_\phi \rho_0)\rho_0 \\ &= (M_\theta M_{-\phi})\rho_0 = M_{\theta - \phi}\rho_0 = \rho_{\theta - \phi} \\ \rho_\theta \rho_\phi &= (M_\theta \rho_0)(M_\phi \rho_0) = M_\theta(\rho_0 M_\phi \rho_0) \\ &= M_\theta M_{-\phi} = M_{\theta - \phi}. \end{aligned}$$
> Tóm lại,
> $$\begin{aligned} M_\theta M_\phi &= M_{\theta + \phi} \tag{RR} \\ M_\theta \rho_\phi &= \rho_{\theta + \phi} \tag{$R\rho$} \\ \rho_\theta M_\phi &= \rho_{\theta - \phi} \tag{$\rho R$} \\ \rho_\theta \rho_\phi &= M_{\theta - \phi}. \tag{$\rho\rho$} \end{aligned}$$
> Sử dụng các phương trình trên, ta có thể kiểm tra rằng các Điều kiện G1, G2, G3 (xem Định nghĩa 2.1) đều thỏa mãn, vì vậy $\mathbf{O}(2)$ là một nhóm dưới phép nhân ma trận. Nhưng nhóm $\mathbf{O}(2)$ không giao hoán! Hãy so sánh $\rho_0 M_\phi$ và $M_\phi \rho_0$.
> <!-- PAGE 28 -->
> Nhóm $\mathbf{O}(2)$ là tích nửa trực tiếp (*semidirect product*) của nhóm $\mathbf{SO}(2)$ và nhóm $\{I_2, \rho_0\}$.
>
> Sử dụng ($\rho R$) và ($R\rho$), ta có
> $$M_{\phi/2}\rho_0 M_{-\phi/2} = M_{\phi/2}\rho_{\phi/2} = \rho_{\phi/2 + \phi/2} = \rho_\phi,$$
> do đó
> $$\rho_\phi = M_{\phi/2}\rho_0 M_{-\phi/2},$$
> hay viết tường minh hơn là
> $$\begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix} = \begin{pmatrix} \cos \phi/2 & -\sin \phi/2 \\ \sin \phi/2 & \cos \phi/2 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} \cos \phi/2 & \sin \phi/2 \\ -\sin \phi/2 & \cos \phi/2 \end{pmatrix}.$$
> Ta nói rằng ma trận $\rho_\phi$ được chéo hóa (*diagonalized*).
>
> Về mặt hình học, đây là phép quay một góc $-\phi/2$, tiếp nối bởi phép đối xứng qua trục $x$, rồi tiếp nối bởi phép quay một góc $\phi/2$.
>
> Cho một điểm $p$, điều này tương đương với việc quay điểm $p$ cùng hệ trục tọa độ có trục hoành là đường thẳng tạo góc $\phi/2$ với trục $x$ và trục tung vuông góc với đường thẳng đó đi một góc $-\phi/2$, sao cho hệ trục tọa độ này (vốn tạo góc $\phi/2$ với hệ trục chuẩn) trùng khít với hệ trục tọa độ chuẩn; sau đó thực hiện phép đối xứng qua trục $x$ lên $M_{-\phi/2}(p)$, và cuối cùng quay $\rho_0(M_{-\phi/2}(p))$ cùng hệ trục tọa độ chuẩn đi một góc $\phi/2$.
>
> Phân tích trên chứng tỏ $\rho_\phi$ là phép đối xứng qua đường thẳng tạo một góc $\phi/2$ với trục $x$.
>
> Theo ($\rho R$), ta thu được
> $$\rho_\phi M_{\phi/2} = \rho_{\phi/2},$$
> hay
> $$\begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix} \begin{pmatrix} \cos \phi/2 & -\sin \phi/2 \\ \sin \phi/2 & \cos \phi/2 \end{pmatrix} = \begin{pmatrix} \cos \phi/2 & \sin \phi/2 \\ \sin \phi/2 & -\cos \phi/2 \end{pmatrix},$$
> điều này cho thấy
> $$\begin{aligned} \begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix} \begin{pmatrix} \cos \phi/2 \\ \sin \phi/2 \end{pmatrix} &= \begin{pmatrix} \cos \phi/2 \\ \sin \phi/2 \end{pmatrix} \\ \begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix} \begin{pmatrix} -\sin \phi/2 \\ \cos \phi/2 \end{pmatrix} &= -\begin{pmatrix} -\sin \phi/2 \\ \cos \phi/2 \end{pmatrix}. \end{aligned}$$
> <!-- PAGE 29 -->
> Ta nói rằng $\begin{pmatrix} \cos \phi/2 \\ \sin \phi/2 \end{pmatrix}$ là một vectơ riêng (*eigenvector*) của $\rho_\phi$ ứng với trị riêng (*eigenvalue*) $1$ và $\begin{pmatrix} -\sin \phi/2 \\ \cos \phi/2 \end{pmatrix}$ là một vectơ riêng của $\rho_\phi$ ứng với trị riêng $-1$.
>
> Ngược lại, sau này chúng ta sẽ thấy rằng một ma trận quay
> $$M_\theta = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$$
> có các trị riêng phức là $\cos \theta \pm i \sin \theta$.
>
> Từ ($\rho\rho$), ta có
> $$\rho_{\phi + \theta}\rho_\phi = M_\theta,$$
> điều này chứng tỏ mọi phép quay góc $\theta$ đều có thể biểu diễn dưới dạng hợp thành của hai phép đối xứng có các trục đối xứng tương ứng với các đường thẳng tạo góc $\phi/2$ và $\phi/2 + \theta/2$ so với trục $x$, tức là hai trục đối xứng tạo với nhau một góc $\theta/2$.
>
> Về mặt hình học, $\mathbf{O}(2)$ là hợp rời (*disjoint union*) của hai đường tròn $S^1$.

> **Ví dụ 2.5 (Example 2.5).** Xét tập hợp $\mathbf{SE}(2)$ gồm các ánh xạ $T_u \circ R_\theta$ thu được bằng cách hợp thành một phép quay và một phép tịnh tiến.
>
> Cho hai ánh xạ như vậy là $T_u \circ R_\theta$ và $T_v \circ R_\phi$, ta có
> $$\begin{aligned} (T_v \circ R_\phi)((T_u \circ R_\theta)(x)) &= (T_v \circ R_\phi)(R_\theta(x) + u) \\ &= R_\phi(R_\theta(x)) + R_\phi(u) + v \\ &= R_{\phi + \theta}(x) + R_\phi(u) + v, \end{aligned}$$
> do đó $(T_v \circ R_\phi) \circ (T_u \circ R_\theta)$ cũng thuộc $\mathbf{SE}(2)$.
>
> Nếu ta ký hiệu $T_u \circ R_\theta$ bởi cặp $(u, R_\theta)$, ta thu được một phép toán nhân $\cdot : \mathbf{SE}(2) \times \mathbf{SE}(2) \to \mathbf{SE}(2)$ trên tập hợp $\mathbf{SE}(2)$ được cho bởi
> $$(v, R_\phi) \cdot (u, R_\theta) = (v + R_\phi(u), R_{\phi + \theta}).$$
> Hãy chú ý tác động của $R_\phi$ lên $u$. Hóa ra $\mathbf{SE}(2)$ là một tích nửa trực tiếp (*semidirect product*) của $\mathbb{R}^2$ và $\mathbf{SO}(2)$.
>
> Lưu ý rằng các phần tử của $\mathbf{SE}(2)$ là các phép biến đổi từ $\mathbb{R}^2$ vào $\mathbb{R}^2$ chứ không phải ma trận. Tuy nhiên, có thể biểu diễn chúng bằng các ma trận $3 \times 3$; xem Mục 24.7.
>
> Các phép tịnh tiến có dạng $(u, R_0)$ (không quay) và các phép quay có dạng $(0_2, R_\theta)$ (không tịnh tiến). Phần tử đơn vị là $(0_2, R_0)$, và nghịch đảo của $(u, R_\theta)$ là $(-R_{-\theta}(u), R_{-\theta})$. Ta có thể kiểm tra rằng các Điều kiện G1, G2, G3 (xem Định nghĩa 2.1) đều thỏa mãn, vì vậy $\mathbf{SE}(2)$ cùng phép nhân trên là một nhóm.
>
> Nhóm $\mathbf{SE}(2)$ không giao hoán. Hãy xét tác động của $R_\theta \circ T_{(1,0)}$ và tác động của $T_{(1,0)} \circ R_\theta$ lên gốc tọa độ.
> <!-- PAGE 30 -->
> Các ánh xạ trong $\mathbf{SE}(2)$ là ánh xạ affine (*affine*), chứ không tuyến tính (*linear*), trừ khi $u = 0$. Về mặt hình học, $\mathbf{SE}(2)$ là mặt trụ $S^1 \times \mathbb{R}^2$. Nó không phải là một không gian compact (*compact space*).
>
> Cùng cách xây dựng trên có thể thực hiện với các cặp $(u, S)$, trong đó $S \in \mathbf{O}(2)$ thay vì $\mathbf{SO}(2)$. Ta thu được nhóm $\mathbf{E}(2)$ ($\mathbf{E}$ viết tắt của Euclidean) gồm các phép dời hình cứng (*rigid motions*) của mặt phẳng ($\mathbb{R}^2$).
>
> Một ánh xạ có dạng $T_u \circ \rho_\phi$ được gọi là một phép dời hình ngược hướng (*indirect motion*). Về mặt kỹ thuật, trong biểu thức trên, ta cần dùng phép biến đổi tuyến tính từ $\mathbb{R}^2$ vào chính nó được xác định bởi ma trận $\rho_\phi$.
>
> Có thể chứng minh rằng $\mathbf{E}(2)$ bao gồm chính xác tất cả các hàm $f : \mathbb{R}^2 \to \mathbb{R}^2$ bảo toàn khoảng cách Euclid (*Euclidean distance*). Xem Mệnh đề 12.13 (không dễ chứng minh!).
>
> Các ma trận trong $\mathbf{SO}(2)$ và $\mathbf{O}(2)$ có tính chất là
> $$SS^\top = S^\top S = I_2,$$
> trong đó $S^\top$ là chuyển vị (*transpose*) của $S$ (đổi chỗ các hàng và các cột). Các ma trận như vậy được gọi là các ma trận trực giao (*orthogonal matrices*).
>
> Để tổng quát hóa các phép quay và phép đối xứng lên $\mathbb{R}^n$ với $n \ge 3$, ta cần xét các ma trận trực giao. Với $n = 3$, chủ đề này đã được nghiên cứu rất sâu rộng (góc Euler, quaternion, biểu diễn mũ, ...).

Bây giờ chúng ta đã sẵn sàng cho định nghĩa hình thức của một nhóm.

> **Định nghĩa 2.1 (Definition 2.1).** Một *nhóm* (*group*) là một tập hợp $G$ được trang bị một phép toán hai ngôi (*binary operation*) $\cdot : G \times G \to G$ gán một phần tử $a \cdot b \in G$ cho mỗi cặp phần tử $a, b \in G$, và có các tính chất sau: $\cdot$ có tính kết hợp (*associative*), có một phần tử đơn vị (*identity element*) $e \in G$, và mọi phần tử trong $G$ đều khả nghịch (*invertible* đối với $\cdot$). Cụ thể hơn, điều này có nghĩa là các phương trình sau đây nghiệm đúng với mọi $a, b, c \in G$:
> - **(G1)** $a \cdot (b \cdot c) = (a \cdot b) \cdot c$. *(tính kết hợp – associativity)*;
> - **(G2)** $a \cdot e = e \cdot a = a$. *(phần tử đơn vị – identity)*;
> - **(G3)** Với mọi $a \in G$, tồn tại $a^{-1} \in G$ sao cho $a \cdot a^{-1} = a^{-1} \cdot a = e$. *(phần tử nghịch đảo – inverse)*.
>
> Một nhóm $G$ được gọi là *nhóm Abel* (*abelian*) hay *nhóm giao hoán* (*commutative*) nếu
> - **(Ab)** $a \cdot b = b \cdot a$ với mọi $a, b \in G$.

Một tập hợp $M$ cùng với một phép toán $\cdot : M \times M \to M$ và một phần tử $e$ chỉ thỏa mãn các Điều kiện (G1) và (G2) được gọi là một *vị nhóm* (*monoid*). Ví dụ, tập hợp $\mathbb{N} = \{0, 1, \dots, n, \dots\}$ các số tự nhiên là một vị nhóm (giao hoán) dưới phép cộng. Tuy nhiên, nó không phải là một nhóm.

Một số ví dụ về nhóm được cho dưới đây.

<!-- PAGE 31 -->

> **Ví dụ 2.6 (Example 2.6).**
> 1. Tập hợp $\mathbb{Z} = \{\dots, -n, \dots, -1, 0, 1, \dots, n, \dots\}$ các số nguyên là một nhóm Abel dưới phép cộng, với phần tử đơn vị là $0$. Tuy nhiên, $\mathbb{Z}^* = \mathbb{Z} - \{0\}$ không phải là một nhóm dưới phép nhân.
> 2. Tập hợp $\mathbb{Q}$ các số hữu tỉ (các phân số $p/q$ với $p, q \in \mathbb{Z}$ và $q \neq 0$) là một nhóm Abel dưới phép cộng, với phần tử đơn vị là $0$. Tập hợp $\mathbb{Q}^* = \mathbb{Q} - \{0\}$ cũng là một nhóm Abel dưới phép nhân, với phần tử đơn vị là $1$.
> 3. Cho một tập hợp khác rỗng bất kỳ $S$, tập hợp các song ánh $f : S \to S$, còn gọi là các *hoán vị* (*permutations*) của $S$, là một nhóm dưới phép hợp thành hàm (tức là tích của $f$ và $g$ là hàm hợp $g \circ f$), với phần tử đơn vị là hàm đồng nhất $\mathrm{id}_S$. Nhóm này không phải là nhóm Abel ngay khi $S$ có nhiều hơn hai phần tử. Nhóm các hoán vị của tập hợp $S = \{1, \dots, n\}$ thường được ký hiệu là $\mathfrak{S}_n$ và được gọi là *nhóm đối xứng* (*symmetric group*) trên $n$ phần tử.
> 4. Với số nguyên dương bất kỳ $p \in \mathbb{N}$, định nghĩa một quan hệ trên $\mathbb{Z}$, ký hiệu là $m \equiv n \pmod{p}$, như sau:
>    $$m \equiv n \pmod{p} \quad \text{khi và chỉ khi} \quad m - n = kp \quad \text{với một số } k \in \mathbb{Z}.$$
>    Bạn đọc có thể dễ dàng kiểm tra rằng đây là một quan hệ tương đương (*equivalence relation*), và hơn nữa, nó tương thích với phép cộng và phép nhân, nghĩa là nếu $m_1 \equiv n_1 \pmod{p}$ và $m_2 \equiv n_2 \pmod{p}$, thì $m_1 + m_2 \equiv n_1 + n_2 \pmod{p}$ và $m_1 m_2 \equiv n_1 n_2 \pmod{p}$. Hệ quả là ta có thể định nghĩa một phép toán cộng và một phép toán nhân trên tập hợp các lớp tương đương ($\bmod\; p$):
>    $$[m] + [n] = [m + n]$$
>    và
>    $$[m] \cdot [n] = [mn].$$
>    Bạn đọc sẽ dễ dàng kiểm tra được rằng phép cộng các lớp thặng dư (*residue classes*) ($\bmod\; p$) cảm sinh một cấu trúc nhóm Abel với $[0]$ là phần tử không. Nhóm này được ký hiệu là $\mathbb{Z}/p\mathbb{Z}$.
> 5. Tập hợp $\mathbb{R}[X]$ gồm tất cả các đa thức một biến $X$ với hệ số thực,
>    $$P(X) = a_0 X^n + a_1 X^{n-1} + \dots + a_{n-1}X + a_n,$$
>    (với $a_i \in \mathbb{R}$), là một nhóm Abel dưới phép cộng đa thức. Phần tử đơn vị là đa thức không (*zero polynomial*).
> 6. Tập hợp các ma trận khả nghịch cấp $n \times n$ với hệ số thực (hoặc phức) là một nhóm dưới phép nhân ma trận, với phần tử đơn vị là ma trận đơn vị $I_n$. Nhóm này được gọi là *nhóm tuyến tính tổng quát* (*general linear group*) và thường được ký hiệu bởi $\mathbf{GL}(n, \mathbb{R})$ (hoặc $\mathbf{GL}(n, \mathbb{C})$).
> 7. Tập hợp các ma trận khả nghịch cấp $n \times n$ là $A$ với hệ số thực (hoặc phức) sao cho $\det(A) = 1$ là một nhóm dưới phép nhân ma trận, với phần tử đơn vị là ma trận đơn vị $I_n$. Nhóm này được gọi là *nhóm tuyến tính đặc biệt* (*special linear group*) và thường được ký hiệu bởi $\mathbf{SL}(n, \mathbb{R})$ (hoặc $\mathbf{SL}(n, \mathbb{C})$).
> <!-- PAGE 32 -->
> 8. Tập hợp các ma trận cấp $n \times n$ là $Q$ với hệ số thực sao cho
>    $$Q Q^\top = Q^\top Q = I_n$$
>    là một nhóm dưới phép nhân ma trận, với phần tử đơn vị là ma trận đơn vị $I_n$; ta có $Q^{-1} = Q^\top$. Nhóm này được gọi là *nhóm trực giao* (*orthogonal group*) và thường được ký hiệu bởi $\mathbf{O}(n)$.
> 9. Tập hợp các ma trận khả nghịch cấp $n \times n$ là $Q$ với hệ số thực sao cho
>    $$Q Q^\top = Q^\top Q = I_n \quad \text{và} \quad \det(Q) = 1$$
>    là một nhóm dưới phép nhân ma trận, với phần tử đơn vị là ma trận đơn vị $I_n$; giống như trong mục (6), ta có $Q^{-1} = Q^\top$. Nhóm này được gọi là *nhóm trực giao đặc biệt* (*special orthogonal group*) hay *nhóm quay* (*rotation group*) và thường được ký hiệu bởi $\mathbf{SO}(n)$.
>
> Các nhóm từ (6)–(9) là không Abel (*nonabelian*) với $n \ge 2$, ngoại trừ $\mathbf{SO}(2)$ là nhóm Abel (nhưng $\mathbf{O}(2)$ không phải là nhóm Abel).

Thông thường người ta ký hiệu phép toán của một nhóm Abel $G$ bởi dấu $+$, và trong trường hợp đó phần tử nghịch đảo $a^{-1}$ của một phần tử $a \in G$ được ký hiệu là $-a$.

Phần tử đơn vị của một nhóm là duy nhất. Thực tế, ta có thể chứng minh một kết quả tổng quát hơn:

> **Mệnh đề 2.1 (Proposition 2.1).** Với mọi phép toán hai ngôi $\cdot : M \times M \to M$, nếu $e' \in M$ là một phần tử đơn vị trái (*left identity*) và nếu $e'' \in M$ là một phần tử đơn vị phải (*right identity*), nghĩa là
> $$e' \cdot a = a \quad \text{với mọi } a \in M \tag{G2l}$$
> và
> $$a \cdot e'' = a \quad \text{với mọi } a \in M, \tag{G2r}$$
> thì $e' = e''$.

*Chứng minh (Proof).* Nếu ta đặt $a = e''$ trong phương trình (G2l), ta được
$$e' \cdot e'' = e'',$$
và nếu ta đặt $a = e'$ trong phương trình (G2r), ta được
$$e' \cdot e'' = e',$$
và do đó
$$e' = e' \cdot e'' = e'',$$
điều phải chứng minh. $\square$

<!-- PAGE 33 -->

Mệnh đề 2.1 suy ra rằng phần tử đơn vị của một vị nhóm (*monoid*) là duy nhất, và vì mọi nhóm đều là vị nhóm nên phần tử đơn vị của một nhóm là duy nhất. Hơn nữa, mọi phần tử trong một nhóm đều có một phần tử nghịch đảo duy nhất. Đây là hệ quả của một tính chất tổng quát hơn đôi chút:

> **Mệnh đề 2.2 (Proposition 2.2).** Trong một vị nhóm $M$ có phần tử đơn vị $e$, nếu một phần tử $a \in M$ có nghịch đảo trái (*left inverse*) $a' \in M$ và nghịch đảo phải (*right inverse*) $a'' \in M$, nghĩa là
> $$a' \cdot a = e \tag{G3l}$$
> và
> $$a \cdot a'' = e, \tag{G3r}$$
> thì $a' = a''$.

*Chứng minh (Proof).* Sử dụng (G3l) và tính chất $e$ là phần tử đơn vị, ta có
$$(a' \cdot a) \cdot a'' = e \cdot a'' = a''.$$
Tương tự, sử dụng (G3r) và tính chất $e$ là phần tử đơn vị, ta có
$$a' \cdot (a \cdot a'') = a' \cdot e = a'.$$
Tuy nhiên, vì $M$ là vị nhóm nên phép toán $\cdot$ có tính kết hợp, suy ra
$$a' = a' \cdot (a \cdot a'') = (a' \cdot a) \cdot a'' = a'',$$
điều phải chứng minh. $\square$

**Nhận xét (Remark):** Các tiên đề (G2) và (G3) có thể được làm yếu đi đôi chút bằng cách chỉ đòi hỏi (G2r) (sự tồn tại phần tử đơn vị phải) và (G3r) (sự tồn tại nghịch đảo phải cho mọi phần tử) (hoặc tương ứng là (G2l) và (G3l)). Việc chứng minh các tiên đề nhóm (G2) và (G3) suy ra từ (G2r) và (G3r) là một bài tập rất tốt.

Một tính chất quan trọng khác về các phần tử khả nghịch trong vị nhóm được phát biểu dưới đây.

> **Mệnh đề 2.3 (Proposition 2.3).** Trong một vị nhóm $M$ có phần tử đơn vị $e$, nếu $a$ và $b$ là các phần tử khả nghịch của $M$, trong đó $a^{-1}$ là nghịch đảo của $a$ và $b^{-1}$ là nghịch đảo của $b$, thì $ab$ khả nghịch và nghịch đảo của nó được cho bởi $(ab)^{-1} = b^{-1}a^{-1}$.

*Chứng minh (Proof).* Sử dụng tính kết hợp và tính chất $e$ là phần tử đơn vị, ta có
$$\begin{aligned}
(ab)(b^{-1}a^{-1}) &= a(b(b^{-1}a^{-1})) && \text{tính kết hợp} \\
&= a((bb^{-1})a^{-1}) && \text{tính kết hợp} \\
&= a(ea^{-1}) && b^{-1} \text{ là nghịch đảo của } b \\
&= aa^{-1} && e \text{ là phần tử đơn vị} \\
&= e. && a^{-1} \text{ là nghịch đảo của } a.
\end{aligned}$$
<!-- PAGE 34 -->
Ta cũng có
$$\begin{aligned}
(b^{-1}a^{-1})(ab) &= b^{-1}(a^{-1}(ab)) && \text{tính kết hợp} \\
&= b^{-1}((a^{-1}a)b) && \text{tính kết hợp} \\
&= b^{-1}(eb) && a^{-1} \text{ là nghịch đảo của } a \\
&= b^{-1}b && e \text{ là phần tử đơn vị} \\
&= e. && b^{-1} \text{ là nghịch đảo của } b.
\end{aligned}$$
Do đó $b^{-1}a^{-1}$ là nghịch đảo của $ab$. $\square$

Chú ý rằng nghịch đảo của $ba$ là $a^{-1}b^{-1}$. Mệnh đề 2.3 suy ra rằng tập hợp các phần tử khả nghịch của một vị nhóm $M$ lập thành một nhóm, với cùng phần tử đơn vị $e$.

> **Định nghĩa 2.2 (Definition 2.2).** Nếu một nhóm $G$ có một số hữu hạn $n$ phần tử, ta nói $G$ là một nhóm có *cấp* (*order*) $n$. Nếu $G$ vô hạn, ta nói $G$ có *cấp vô hạn* (*infinite order*). Cấp của một nhóm thường được ký hiệu bởi $|G|$ (nếu $G$ hữu hạn).

Cho một nhóm $G$, với hai tập con bất kỳ $R, S \subseteq G$, ta đặt
$$RS = \{r \cdot s \mid r \in R, s \in S\}.$$
Đặc biệt, với mọi $g \in G$, nếu $R = \{g\}$, ta viết
$$gS = \{g \cdot s \mid s \in S\},$$
và tương tự, nếu $S = \{g\}$, ta viết
$$Rg = \{r \cdot g \mid r \in R\}.$$
Từ giờ trở đi, ta sẽ lược bỏ dấu nhân và viết $g_1 g_2$ thay cho $g_1 \cdot g_2$.

> **Định nghĩa 2.3 (Definition 2.3).** Cho $G$ là một nhóm. Với mọi $g \in G$, định nghĩa $L_g$, *phép tịnh tiến trái bởi $g$* (*left translation by $g$*), bởi $L_g(a) = ga$ với mọi $a \in G$, và $R_g$, *phép tịnh tiến phải bởi $g$* (*right translation by $g$*), bởi $R_g(a) = ag$ với mọi $a \in G$.

Tính chất đơn giản sau đây thường xuyên được sử dụng.

> **Mệnh đề 2.4 (Proposition 2.4).** Cho một nhóm $G$, các phép tịnh tiến $L_g$ và $R_g$ là các song ánh.

*Chứng minh (Proof).* Ta chứng minh cho $L_g$, phép chứng minh cho $R_g$ hoàn toàn tương tự.
Nếu $L_g(a) = L_g(b)$, thì $ga = gb$, và nhân vào bên trái với $g^{-1}$, ta nhận được $a = b$, nên $L_g$ là đơn ánh (*injective*). Với mọi $b \in G$, ta có $L_g(g^{-1}b) = gg^{-1}b = b$, nên $L_g$ là toàn ánh (*surjective*). Vậy $L_g$ là song ánh (*bijective*). $\square$

> **Định nghĩa 2.4 (Definition 2.4).** Cho một nhóm $G$, một tập con $H$ của $G$ là một *nhóm con* (*subgroup*) của $G$ khi và chỉ khi:
> 1. Phần tử đơn vị $e$ của $G$ cũng thuộc $H$ ($e \in H$);
> <!-- PAGE 35 -->
> 2. Với mọi $h_1, h_2 \in H$, ta có $h_1 h_2 \in H$;
> 3. Với mọi $h \in H$, ta có $h^{-1} \in H$.

Phép chứng minh mệnh đề sau đây được dành làm bài tập.

> **Mệnh đề 2.5 (Proposition 2.5).** Cho một nhóm $G$, một tập con $H \subseteq G$ là một nhóm con của $G$ khi và chỉ khi $H$ khác rỗng và bất cứ khi nào $h_1, h_2 \in H$, thì $h_1 h_2^{-1} \in H$.

Nếu nhóm $G$ hữu hạn, ta có thể sử dụng tiêu chuẩn sau đây.

> **Mệnh đề 2.6 (Proposition 2.6).** Cho một nhóm hữu hạn $G$, một tập con $H \subseteq G$ là một nhóm con của $G$ khi và chỉ khi:
> 1. $e \in H$;
> 2. $H$ đóng kín đối với phép nhân (*closed under multiplication*).

*Chứng minh (Proof).* Ta chỉ cần chứng minh Điều kiện (3) của Định nghĩa 2.4 thỏa mãn. Với mọi $a \in H$, vì phép tịnh tiến trái $L_a$ là song ánh nên thu hẹp (*restriction*) của nó lên $H$ là một đơn ánh, và vì $H$ hữu hạn nên nó cũng là một song ánh. Vì $e \in H$, tồn tại duy nhất $b \in H$ sao cho $L_a(b) = ab = e$. Tuy nhiên, nếu $a^{-1}$ là nghịch đảo của $a$ trong $G$, ta cũng có $L_a(a^{-1}) = aa^{-1} = e$, và do tính đơn ánh của $L_a$, ta suy ra $a^{-1} = b \in H$. $\square$

> **Ví dụ 2.7 (Example 2.7).**
> 1. Với mọi số nguyên $n \in \mathbb{Z}$, tập hợp
>    $$n\mathbb{Z} = \{nk \mid k \in \mathbb{Z}\}$$
>    là một nhóm con của nhóm $\mathbb{Z}$.
> 2. Tập hợp các ma trận
>    $$\mathbf{GL}^+(n, \mathbb{R}) = \{A \in \mathbf{GL}(n, \mathbb{R}) \mid \det(A) > 0\}$$
>    là một nhóm con của nhóm $\mathbf{GL}(n, \mathbb{R})$.
> 3. Nhóm $\mathbf{SL}(n, \mathbb{R})$ là một nhóm con của nhóm $\mathbf{GL}(n, \mathbb{R})$.
> 4. Nhóm $\mathbf{O}(n)$ là một nhóm con của nhóm $\mathbf{GL}(n, \mathbb{R})$.
> 5. Nhóm $\mathbf{SO}(n)$ là một nhóm con của nhóm $\mathbf{O}(n)$, và là một nhóm con của nhóm $\mathbf{SL}(n, \mathbb{R})$.
> <!-- PAGE 36 -->
> 6. Không khó để chỉ ra rằng mọi ma trận quay cấp $2 \times 2$ là $R \in \mathbf{SO}(2)$ đều có thể viết dưới dạng
>    $$R = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}, \quad \text{với } 0 \le \theta < 2\pi.$$
>    Khi đó $\mathbf{SO}(2)$ có thể được xem như một nhóm con của $\mathbf{SO}(3)$ bằng cách đồng nhất ma trận
>    $$R = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$$
>    với ma trận
>    $$Q = \begin{pmatrix} \cos \theta & -\sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$
> 7. Tập hợp các ma trận tam giác trên (*upper-triangular matrices*) cấp $2 \times 2$ có dạng
>    $$\begin{pmatrix} a & b \\ 0 & c \end{pmatrix}, \quad a, b, c \in \mathbb{R},\; a, c \neq 0$$
>    là một nhóm con của nhóm $\mathbf{GL}(2, \mathbb{R})$.
> 8. Tập hợp $V$ gồm bốn ma trận
>    $$\begin{pmatrix} \pm 1 & 0 \\ 0 & \pm 1 \end{pmatrix}$$
>    là một nhóm con của nhóm $\mathbf{GL}(2, \mathbb{R})$ được gọi là *nhóm Klein bốn phần tử* (*Klein four-group*).

> **Định nghĩa 2.5 (Definition 2.5).** Nếu $H$ là một nhóm con của $G$ và $g \in G$ là một phần tử bất kỳ, các tập hợp có dạng $gH$ được gọi là các *lớp ghép trái* (*left cosets*) của $H$ trong $G$ và các tập hợp có dạng $Hg$ được gọi là các *lớp ghép phải* (*right cosets*) của $H$ trong $G$. Các lớp ghép trái (tương ứng, các lớp ghép phải) của $H$ cảm sinh một quan hệ tương đương $\sim$ được định nghĩa như sau: Với mọi $g_1, g_2 \in G$,
> $$g_1 \sim g_2 \quad \text{khi và chỉ khi} \quad g_1 H = g_2 H$$
> (tương ứng, $g_1 \sim g_2$ khi và chỉ khi $H g_1 = H g_2$). Hiển nhiên, $\sim$ là một quan hệ tương đương.

Bây giờ, ta khẳng định tính chất sau:

> **Mệnh đề 2.7 (Proposition 2.7).** Cho một nhóm $G$ và một nhóm con bất kỳ $H$ của $G$, ta có $g_1 H = g_2 H$ khi và chỉ khi $g_2^{-1} g_1 H = H$ khi và chỉ khi $g_2^{-1} g_1 \in H$, với mọi $g_1, g_2 \in G$.

*Chứng minh (Proof).* Nếu ta tác động song ánh $L_{g_2^{-1}}$ lên cả $g_1 H$ và $g_2 H$, ta được $L_{g_2^{-1}}(g_1 H) = g_2^{-1} g_1 H$ và $L_{g_2^{-1}}(g_2 H) = H$, do đó $g_1 H = g_2 H$ khi và chỉ khi $g_2^{-1} g_1 H = H$. Nếu $g_2^{-1} g_1 H = H$, vì $1 \in H$ nên ta suy ra $g_2^{-1} g_1 \in H$. Ngược lại, nếu $g_2^{-1} g_1 \in H$, vì $H$ là một nhóm nên phép tịnh tiến trái $L_{g_2^{-1} g_1}$ là một song ánh của $H$, thành thử $g_2^{-1} g_1 H = H$. Vậy $g_2^{-1} g_1 H = H$ khi và chỉ khi $g_2^{-1} g_1 \in H$. $\square$

<!-- PAGE 37 -->

Từ đó suy ra lớp tương đương của một phần tử $g \in G$ chính là lớp ghép $gH$ (tương ứng, $Hg$). Vì $L_g$ là một song ánh giữa $H$ và $gH$, tất cả các lớp ghép $gH$ đều có cùng lực lượng (*cardinality*). Ánh xạ $L_{g^{-1}} \circ R_g$ là một song ánh giữa lớp ghép trái $gH$ và lớp ghép phải $Hg$, nên chúng cũng có cùng lực lượng. Vì các lớp ghép phân biệt $gH$ tạo thành một phân hoạch (*partition*) của $G$, ta thu được định lý nổi tiếng sau:

> **Mệnh đề 2.8 (Proposition 2.8).** *(Lagrange)* Với mọi nhóm hữu hạn $G$ và mọi nhóm con $H$ của $G$, cấp $h$ của $H$ là ước của cấp $n$ của $G$.

> **Định nghĩa 2.6 (Definition 2.6).** Cho một nhóm hữu hạn $G$ và một nhóm con $H$ của $G$, nếu $n = |G|$ và $h = |H|$, thì tỷ số $n/h$ được ký hiệu bởi $(G : H)$ và được gọi là *chỉ số của $H$ trong $G$* (*index of $H$ in $G$*).

Chỉ số $(G : H)$ chính là số lượng các lớp ghép trái (và phải) của $H$ trong $G$. Mệnh đề 2.8 có thể được phát biểu dưới dạng
$$|G| = (G : H)|H|.$$
Tập hợp các lớp ghép trái của $H$ trong $G$ (nhìn chung không phải là một nhóm) được ký hiệu là $G/H$. Các "điểm" của $G/H$ thu được bằng cách "gom" (*collapsing*) tất cả các phần tử trong cùng một lớp ghép thành một phần tử duy nhất.

> **Ví dụ 2.8 (Example 2.8).**
> 1. Cho $n$ là một số nguyên dương bất kỳ, và xét nhóm con $n\mathbb{Z}$ của $\mathbb{Z}$ (dưới phép cộng). Lớp ghép của một số nguyên bất kỳ $m \in \mathbb{Z}$ là
>    $$m + n\mathbb{Z} = \{m + nk \mid k \in \mathbb{Z}\}.$$
>    Đặc biệt, lớp ghép của $0$ là tập hợp $n\mathbb{Z}$. Bằng cách chia $m$ cho $n$, ta có $m = nq + r$ với $r$ duy nhất sao cho $0 \le r \le n - 1$. Khi đó ta thấy $r$ là phần tử không âm nhỏ nhất thuộc lớp ghép $m + n\mathbb{Z}$. Điều này suy ra có một song ánh giữa các lớp ghép của nhóm con $n\mathbb{Z}$ của $\mathbb{Z}$ và tập hợp các số dư $\{0, 1, \dots, n - 1\}$ modulo $n$, hay tương đương là một song ánh với $\mathbb{Z}/n\mathbb{Z}$.
> 2. Các lớp ghép của $\mathbf{SL}(n, \mathbb{R})$ trong $\mathbf{GL}(n, \mathbb{R})$ là các tập hợp ma trận
>    $$A\mathbf{SL}(n, \mathbb{R}) = \{AB \mid B \in \mathbf{SL}(n, \mathbb{R})\}, \quad A \in \mathbf{GL}(n, \mathbb{R}).$$
>    Vì $A$ khả nghịch nên $\det(A) \neq 0$, và ta có thể viết $A = (\det(A))^{1/n}((\det(A))^{-1/n}A)$ nếu $\det(A) > 0$ và $A = (-\det(A))^{1/n}((-\det(A))^{-1/n}A)$ nếu $\det(A) < 0$. Nhưng ta lại có $(\det(A))^{-1/n}A \in \mathbf{SL}(n, \mathbb{R})$ nếu $\det(A) > 0$ và $-(-\det(A))^{-1/n}A \in \mathbf{SL}(n, \mathbb{R})$ nếu $\det(A) < 0$, nên lớp ghép $A\mathbf{SL}(n, \mathbb{R})$ chứa ma trận
>    $$\begin{aligned} (\det(A))^{1/n}I_n \quad &\text{nếu } \det(A) > 0, \\ -(-\det(A))^{1/n}I_n \quad &\text{nếu } \det(A) < 0. \end{aligned}$$
>    Từ đó suy ra có một song ánh giữa các lớp ghép của $\mathbf{SL}(n, \mathbb{R})$ trong $\mathbf{GL}(n, \mathbb{R})$ và $\mathbb{R}^*$.
> <!-- PAGE 38 -->
> 3. Các lớp ghép của $\mathbf{SO}(n)$ trong $\mathbf{GL}^+(n, \mathbb{R})$ là các tập hợp ma trận
>    $$A\mathbf{SO}(n) = \{AQ \mid Q \in \mathbf{SO}(n)\}, \quad A \in \mathbf{GL}^+(n, \mathbb{R}).$$
>    Có thể chứng minh (bằng cách sử dụng dạng cực – *polar form* của ma trận) rằng tồn tại một song ánh giữa các lớp ghép của $\mathbf{SO}(n)$ trong $\mathbf{GL}^+(n, \mathbb{R})$ và tập hợp các ma trận đối xứng xác định dương (*symmetric, positive, definite matrices*) cấp $n \times n$; đây là các ma trận đối xứng có tất cả các trị riêng đều dương thực sự.
> 4. Các lớp ghép của $\mathbf{SO}(2)$ trong $\mathbf{SO}(3)$ là các tập hợp ma trận
>    $$Q\mathbf{SO}(2) = \{QR \mid R \in \mathbf{SO}(2)\}, \quad Q \in \mathbf{SO}(3).$$
>    Nhóm $\mathbf{SO}(3)$ dịch chuyển các điểm trên mặt cầu $S^2$ trong $\mathbb{R}^3$, cụ thể với mọi $x \in S^2$,
>    $$x \mapsto Qx \quad \text{với mọi phép quay } Q \in \mathbf{SO}(3).$$
>    Ở đây,
>    $$S^2 = \{(x, y, z) \in \mathbb{R}^3 \mid x^2 + y^2 + z^2 = 1\}.$$
>    Gọi $N = (0, 0, 1)$ là cực Bắc (*north pole*) trên mặt cầu $S^2$. Khi đó không khó để chứng minh rằng $\mathbf{SO}(2)$ chính xác là nhóm con của $\mathbf{SO}(3)$ giữ cố định điểm $N$. Hệ quả là mọi phép quay $QR$ trong lớp ghép $Q\mathbf{SO}(2)$ đều ánh xạ $N$ tới cùng một điểm $QN \in S^2$, và có thể chứng minh rằng tồn tại một song ánh giữa các lớp ghép của $\mathbf{SO}(2)$ trong $\mathbf{SO}(3)$ và các điểm trên mặt cầu $S^2$. Tính toàn ánh của ánh xạ này liên quan đến việc tác động của $\mathbf{SO}(3)$ lên $S^2$ có tính bắc cầu (*transitive*), nghĩa là với mọi điểm $x \in S^2$, luôn tồn tại một phép quay $Q \in \mathbf{SO}(3)$ sao cho $QN = x$.

Người ta rất dễ muốn thử định nghĩa một phép toán nhân trên các lớp ghép trái (hoặc các lớp ghép phải) bằng cách đặt
$$(g_1 H)(g_2 H) = (g_1 g_2)H,$$
nhưng nhìn chung phép toán này không xác định tốt (*not well defined*), trừ khi nhóm con $H$ sở hữu một tính chất đặc biệt. Trong Ví dụ 2.8, ta có thể định nghĩa phép nhân các lớp ghép trong trường hợp (1), nhưng không thể định nghĩa được trong các trường hợp (2) và (3).

Tính chất của nhóm con $H$ cho phép định nghĩa một phép toán nhân trên các lớp ghép trái là tính chất đặc trưng của hạt nhân (*kernels*) của các đồng cấu nhóm, dẫn chúng ta đến định nghĩa sau đây.

> **Định nghĩa 2.7 (Definition 2.7).** Cho hai nhóm bất kỳ $G$ và $G'$, một hàm $\phi : G \to G'$ là một *đồng cấu* (*homomorphism*) khi và chỉ khi
> $$\phi(g_1 g_2) = \phi(g_1)\phi(g_2), \quad \text{với mọi } g_1, g_2 \in G.$$

Lấy $g_1 = g_2 = e$ (trong $G$), ta thấy rằng
$$\phi(e) = e',$$
và lấy $g_1 = g$ cùng $g_2 = g^{-1}$, ta thấy rằng
$$\phi(g^{-1}) = (\phi(g))^{-1}.$$

<!-- PAGE 39 -->

> **Ví dụ 2.9 (Example 2.9).**
> 1. Ánh xạ $\phi : \mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ cho bởi $\phi(m) = m \bmod n$ với mọi $m \in \mathbb{Z}$ là một đồng cấu.
> 2. Ánh xạ $\det : \mathbf{GL}(n, \mathbb{R}) \to \mathbb{R}^*$ là một đồng cấu vì $\det(AB) = \det(A)\det(B)$ với hai ma trận $A, B$ bất kỳ. Tương tự, ánh xạ $\det : \mathbf{O}(n) \to \mathbb{R}^*$ là một đồng cấu.

Nếu $\phi : G \to G'$ và $\psi : G' \to G''$ là các đồng cấu nhóm, thì $\psi \circ \phi : G \to G''$ cũng là một đồng cấu. Nếu $\phi : G \to G'$ là một đồng cấu nhóm, và nếu $H \subseteq G$, $H' \subseteq G'$ là hai nhóm con, thì ta dễ dàng kiểm tra được rằng
$$\operatorname{Im} \phi = \phi(H) = \{\phi(g) \mid g \in H\}$$
là một nhóm con của $G'$ và
$$\phi^{-1}(H') = \{g \in G \mid \phi(g) \in H'\}$$
là một nhóm con của $G$. Đặc biệt, khi $H' = \{e'\}$, ta thu được hạt nhân (*kernel*), $\operatorname{Ker} \phi$, của $\phi$.

> **Định nghĩa 2.8 (Definition 2.8).** Nếu $\phi : G \to G'$ là một đồng cấu nhóm, và nếu $H \subseteq G$ là một nhóm con của $G$, thì nhóm con của $G'$,
> $$\operatorname{Im} \phi = \phi(H) = \{\phi(g) \mid g \in H\},$$
> được gọi là *ảnh của $H$ qua $\phi$* (*image of $H$ by $\phi$*), và nhóm con của $G$,
> $$\operatorname{Ker} \phi = \{g \in G \mid \phi(g) = e'\},$$
> được gọi là *hạt nhân của $\phi$* (*kernel of $\phi$*).

> **Ví dụ 2.10 (Example 2.10).**
> 1. Hạt nhân của đồng cấu $\phi : \mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ trong Ví dụ 2.9 là $n\mathbb{Z}$.
> 2. Hạt nhân của đồng cấu $\det : \mathbf{GL}(n, \mathbb{R}) \to \mathbb{R}^*$ là $\mathbf{SL}(n, \mathbb{R})$. Tương tự, hạt nhân của đồng cấu $\det : \mathbf{O}(n) \to \mathbb{R}^*$ là $\mathbf{SO}(n)$.

Đặc trưng sau đây về tính đơn ánh của một đồng cấu nhóm được sử dụng liên tục.

> **Mệnh đề 2.9 (Proposition 2.9).** Nếu $\phi : G \to G'$ là một đồng cấu nhóm, thì $\phi : G \to G'$ là đơn ánh khi và chỉ khi $\operatorname{Ker} \phi = \{e\}$. (Ta cũng viết $\operatorname{Ker} \phi = (0)$.)

*Chứng minh (Proof).* Giả sử $\phi$ là đơn ánh. Vì $\phi(e) = e'$, nếu $\phi(g) = e'$ thì $\phi(g) = \phi(e)$, và do tính đơn ánh của $\phi$ ta buộc phải có $g = e$, vậy $\operatorname{Ker} \phi = \{e\}$.

Ngược lại, giả sử $\operatorname{Ker} \phi = \{e\}$. Nếu $\phi(g_1) = \phi(g_2)$, thì bằng cách nhân vào bên trái với $(\phi(g_1))^{-1}$ ta được
$$e' = (\phi(g_1))^{-1}\phi(g_1) = (\phi(g_1))^{-1}\phi(g_2),$$
<!-- PAGE 40 -->
và vì $\phi$ là một đồng cấu nên $(\phi(g_1))^{-1} = \phi(g_1^{-1})$, do đó
$$e' = (\phi(g_1))^{-1}\phi(g_2) = \phi(g_1^{-1})\phi(g_2) = \phi(g_1^{-1}g_2).$$
Điều này chứng tỏ $g_1^{-1}g_2 \in \operatorname{Ker} \phi$, nhưng vì $\operatorname{Ker} \phi = \{e\}$ nên ta có $g_1^{-1}g_2 = e$, suy ra $g_2 = g_1$, chứng tỏ $\phi$ là đơn ánh. $\square$

Các ánh xạ $g \mapsto L_g$ (trong đó $L_g$ là phép tịnh tiến trái bởi $g$) và $g \mapsto R_g$ (trong đó $R_g$ là phép tịnh tiến phải bởi $g$) là các đồng cấu đơn ánh từ $G$ vào nhóm các song ánh của $G$ (bởi vì $L_{g_1 g_2} = L_{g_1} \circ L_{g_2}$ và $R_{g_1 g_2} = R_{g_2} \circ R_{g_1}$, đồng thời hạt nhân của các đồng cấu này là $\{e\}$).

> **Định nghĩa 2.9 (Definition 2.9).** Ta nói một đồng cấu nhóm $\phi : G \to G'$ là một *đẳng cấu* (*isomorphism*) nếu tồn tại một đồng cấu $\psi : G' \to G$ sao cho
> $$\psi \circ \phi = \mathrm{id}_G \quad \text{và} \quad \phi \circ \psi = \mathrm{id}_{G'}. \tag{$\dagger$}$$
> Nếu $\phi$ là một đẳng cấu, ta nói hai nhóm $G$ và $G'$ là *đẳng cấu với nhau* (*isomorphic*). Khi $G' = G$, một đẳng cấu nhóm được gọi là một *tự đẳng cấu* (*automorphism*).

Lập luận được sử dụng trong chứng minh của Mệnh đề 2.2 cho thấy nếu một đồng cấu nhóm $\phi : G \to G'$ là một đẳng cấu, thì đồng cấu $\psi : G' \to G$ thỏa mãn Điều kiện ($\dagger$) là duy nhất. Đồng cấu này được ký hiệu là $\phi^{-1}$.

Giả sử $\phi : G \to G'$ là một đồng cấu song ánh, và gọi $\phi^{-1}$ là ánh xạ ngược của $\phi$ (với tư cách là một hàm). Khi đó với mọi $a, b \in G'$, ta có
$$\phi(\phi^{-1}(a)\phi^{-1}(b)) = \phi(\phi^{-1}(a))\phi(\phi^{-1}(b)) = ab,$$
và do đó
$$\phi^{-1}(ab) = \phi^{-1}(a)\phi^{-1}(b),$$
chứng tỏ rằng $\phi^{-1}$ là một đồng cấu. Như vậy, chúng ta đã chứng minh được kết quả sau.

> **Mệnh đề 2.10 (Proposition 2.10).** Một đồng cấu nhóm song ánh $\phi : G \to G'$ là một đẳng cấu.

Chú ý rằng tính chất
$$gH = Hg, \quad \text{với mọi } g \in G \tag{$*$}$$
tương đương (bằng cách nhân vào bên phải với $g^{-1}$) với
$$gHg^{-1} = H, \quad \text{với mọi } g \in G,$$
và điều kiện trên lại tương đương với
$$gHg^{-1} \subseteq H, \quad \text{với mọi } g \in G. \tag{$**$}$$
Điều này là do $gHg^{-1} \subseteq H$ kéo theo $H \subseteq g^{-1}Hg$ với mọi $g \in G$.

<!-- PAGE 41 -->

> **Mệnh đề 2.11 (Proposition 2.11).** Cho $\phi : G \to G'$ là một đồng cấu nhóm. Khi đó $H = \operatorname{Ker} \phi$ thỏa mãn Tính chất ($**$), và do đó thỏa mãn Tính chất ($*$).

*Chứng minh (Proof).* Ta có
$$\phi(ghg^{-1}) = \phi(g)\phi(h)\phi(g^{-1}) = \phi(g)e'\phi(g)^{-1} = \phi(g)\phi(g)^{-1} = e',$$
với mọi $h \in H = \operatorname{Ker} \phi$ và mọi $g \in G$. Do đó, theo định nghĩa của $H = \operatorname{Ker} \phi$, ta có $gHg^{-1} \subseteq H$. $\square$

> **Định nghĩa 2.10 (Definition 2.10).** Với mọi nhóm $G$, một nhóm con $N$ của $G$ được gọi là một *nhóm con chuẩn tắc* (*normal subgroup*) của $G$ khi và chỉ khi
> $$gNg^{-1} = N, \quad \text{với mọi } g \in G.$$
> Quan hệ này được ký hiệu bởi $N \triangleleft G$.

Mệnh đề 2.11 cho thấy hạt nhân $\operatorname{Ker} \phi$ của một đồng cấu $\phi : G \to G'$ là một nhóm con chuẩn tắc của $G$.

Lưu ý rằng nếu $G$ là nhóm Abel, thì mọi nhóm con của $G$ đều là nhóm con chuẩn tắc.

Hãy xét Ví dụ 2.7. Cho $R \in \mathbf{SO}(2)$ và $A \in \mathbf{SL}(2, \mathbb{R})$ là các ma trận
$$R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \quad A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}.$$
Khi đó
$$A^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$$
và ta có
$$ARA^{-1} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -2 \\ 1 & -1 \end{pmatrix},$$
và rõ ràng $ARA^{-1} \notin \mathbf{SO}(2)$. Do đó $\mathbf{SO}(2)$ không phải là một nhóm con chuẩn tắc của $\mathbf{SL}(2, \mathbb{R})$. Cùng phản ví dụ này cũng cho thấy $\mathbf{O}(2)$ không phải là một nhóm con chuẩn tắc của $\mathbf{GL}(2, \mathbb{R})$.

Cho $R \in \mathbf{SO}(2)$ và $Q \in \mathbf{SO}(3)$ là các ma trận
$$R = \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \quad Q = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix}.$$
Khi đó
$$Q^{-1} = Q^\top = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix}$$
<!-- PAGE 42 -->
và ta có
$$QRQ^{-1} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -1 & 0 \\ 0 & 0 & -1 \\ 1 & 0 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix}$$
$$= \begin{pmatrix} 0 & 0 & -1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix}.$$
Chú ý rằng $QRQ^{-1} \notin \mathbf{SO}(2)$, nên $\mathbf{SO}(2)$ không phải là một nhóm con chuẩn tắc của $\mathbf{SO}(3)$.

Cho $T$ và $A \in \mathbf{GL}(2, \mathbb{R})$ là các ma trận sau:
$$T = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \quad A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.$$
Ta có
$$A^{-1} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = A,$$
và
$$ATA^{-1} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}.$$
Ma trận $T$ là ma trận tam giác trên, nhưng $ATA^{-1}$ thì không, vì vậy nhóm các ma trận tam giác trên cấp $2 \times 2$ không phải là một nhóm con chuẩn tắc của $\mathbf{GL}(2, \mathbb{R})$.

Cho $Q \in V$ và $A \in \mathbf{GL}(2, \mathbb{R})$ là các ma trận sau:
$$Q = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \quad A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}.$$
Ta có
$$A^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$$
và
$$AQA^{-1} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -2 \\ 0 & -1 \end{pmatrix}.$$
Rõ ràng $AQA^{-1} \notin V$, điều này cho thấy nhóm Klein bốn phần tử không phải là một nhóm con chuẩn tắc của $\mathbf{GL}(2, \mathbb{R})$.

Bạn đọc nên tự kiểm tra rằng các nhóm con $n\mathbb{Z}$, $\mathbf{GL}^+(n, \mathbb{R})$, $\mathbf{SL}(n, \mathbb{R})$, và $\mathbf{SO}(n, \mathbb{R})$ với tư cách là nhóm con của $\mathbf{O}(n, \mathbb{R})$, đều là các nhóm con chuẩn tắc.

Nếu $N$ là một nhóm con chuẩn tắc của $G$, quan hệ tương đương $\sim$ cảm sinh bởi các lớp ghép trái (xem Định nghĩa 2.5) trùng với quan hệ tương đương cảm sinh bởi các lớp ghép phải. Hơn nữa, quan hệ tương đương này là một *tương đẳng* (*congruence*), nghĩa là: Với mọi $g_1, g_2, g'_1, g'_2 \in G$,
<!-- PAGE 43 -->
1. Nếu $g_1 N = g'_1 N$ và $g_2 N = g'_2 N$, thì $g_1 g_2 N = g'_1 g'_2 N$, và
2. Nếu $g_1 N = g_2 N$, thì $g_1^{-1} N = g_2^{-1} N$.

Hệ quả là ta có thể định nghĩa một cấu trúc nhóm trên tập hợp $G/{\sim}$ gồm các lớp tương đương modulo $\sim$, bằng cách đặt
$$(g_1 N)(g_2 N) = (g_1 g_2)N.$$

> **Định nghĩa 2.11 (Definition 2.11).** Cho $G$ là một nhóm và $N$ là một nhóm con chuẩn tắc của $G$. Nhóm thu được bằng cách định nghĩa phép nhân các lớp ghép (trái) bởi
> $$(g_1 N)(g_2 N) = (g_1 g_2)N, \quad g_1, g_2 \in G$$
> được ký hiệu là $G/N$, và được gọi là *nhóm thương của $G$ trên $N$* (*quotient of $G$ by $N$*). Lớp tương đương $gN$ của một phần tử $g \in G$ còn được ký hiệu là $\overline{g}$ (hoặc $[g]$). Ánh xạ $\pi : G \to G/N$ cho bởi
> $$\pi(g) = \overline{g} = gN$$
> là một đồng cấu nhóm được gọi là *phép chiếu chính tắc* (*canonical projection*).

Vì hạt nhân của một đồng cấu là một nhóm con chuẩn tắc, ta thu được kết quả vô cùng hữu ích sau đây.

> **Mệnh đề 2.12 (Proposition 2.12).** Cho một đồng cấu nhóm $\phi : G \to G'$, hai nhóm $G/\operatorname{Ker} \phi$ và $\operatorname{Im} \phi = \phi(G)$ là đẳng cấu với nhau.

*Chứng minh (Proof).* Vì $\phi$ là toàn ánh lên ảnh của nó, ta có thể giả sử $\phi$ là toàn ánh, sao cho $G' = \operatorname{Im} \phi$. Ta định nghĩa một ánh xạ $\overline{\phi} : G/\operatorname{Ker} \phi \to G'$ như sau:
$$\overline{\phi}(\overline{g}) = \phi(g), \quad g \in G.$$
Ta cần kiểm tra rằng định nghĩa của ánh xạ này không phụ thuộc vào phần tử đại diện được chọn trong lớp ghép $\overline{g} = g\operatorname{Ker} \phi$, và nó là một đồng cấu. Nếu $g'$ là một phần tử khác trong lớp ghép $g\operatorname{Ker} \phi$, nghĩa là $g' = gh$ với một $h \in \operatorname{Ker} \phi$ nào đó, thì
$$\phi(g') = \phi(gh) = \phi(g)\phi(h) = \phi(g)e' = \phi(g),$$
vì $\phi(h) = e'$ do $h \in \operatorname{Ker} \phi$. Điều này chứng tỏ rằng
$$\overline{\phi}(\overline{g'}) = \phi(g') = \phi(g) = \overline{\phi}(\overline{g}),$$
nên ánh xạ $\overline{\phi}$ được xác định tốt (*well defined*). Nó là một đồng cấu bởi vì
$$\begin{aligned}
\overline{\phi}(\overline{g}\,\overline{g'}) &= \overline{\phi}(\overline{gg'}) \\
&= \phi(gg') \\
&= \phi(g)\phi(g') \\
&= \overline{\phi}(\overline{g})\overline{\phi}(\overline{g'}).
\end{aligned}$$
Ánh xạ $\overline{\phi}$ là đơn ánh bởi vì $\overline{\phi}(\overline{g}) = e'$ khi và chỉ khi $\phi(g) = e'$, khi và chỉ khi $g \in \operatorname{Ker} \phi$, khi và chỉ khi $\overline{g} = \overline{e}$. Ánh xạ $\overline{\phi}$ là toàn ánh bởi vì $\phi$ là toàn ánh. Vậy $\overline{\phi}$ là một đồng cấu song ánh, và do đó là một đẳng cấu như đã khẳng định. $\square$

<!-- PAGE 44 -->

Mệnh đề 2.12 được gọi là *định lý đẳng cấu thứ nhất* (*first isomorphism theorem*).

Một cách hữu ích để xây dựng các nhóm là phép xây dựng tích trực tiếp (*direct product construction*).

> **Định nghĩa 2.12 (Definition 2.12).** Cho hai nhóm $G$ và $H$, gọi $G \times H$ là tích Đề-các (*Cartesian product*) của hai tập hợp $G$ và $H$ cùng với phép toán nhân $\cdot$ được cho bởi
> $$(g_1, h_1) \cdot (g_2, h_2) = (g_1 g_2, h_1 h_2).$$
> Ta kiểm chứng được ngay rằng $G \times H$ là một nhóm được gọi là *tích trực tiếp* (*direct product*) của $G$ và $H$.

Tương tự, cho $n$ nhóm bất kỳ $G_1, \dots, G_n$, ta có thể định nghĩa tích trực tiếp $G_1 \times \dots \times G_n$ theo cách hoàn toàn tương tự.

Nếu $G$ là một nhóm Abel và $H_1, \dots, H_n$ là các nhóm con của $G$, tình huống sẽ đơn giản hơn. Xét ánh xạ
$$a : H_1 \times \dots \times H_n \to G$$
được cho bởi
$$a(h_1, \dots, h_n) = h_1 + \dots + h_n,$$
sử dụng dấu $+$ cho phép toán của nhóm $G$. Dễ dàng kiểm chứng rằng $a$ là một đồng cấu nhóm, nên ảnh của nó là một nhóm con của $G$, được ký hiệu bởi $H_1 + \dots + H_n$, và được gọi là *tổng của các nhóm $H_i$* (*sum of the groups $H_i$*). Mệnh đề sau đây sẽ cần dùng đến về sau.

> **Mệnh đề 2.13 (Proposition 2.13).** Cho một nhóm Abel $G$, nếu $H_1$ và $H_2$ là hai nhóm con bất kỳ của $G$ sao cho $H_1 \cap H_2 = \{0\}$, thì ánh xạ $a$ là một đẳng cấu
> $$a : H_1 \times H_2 \to H_1 + H_2.$$

*Chứng minh (Proof).* Ánh xạ này là toàn ánh theo định nghĩa, nên ta chỉ cần kiểm tra nó là đơn ánh. Để làm điều này, ta chỉ ra rằng $\operatorname{Ker} a = \{(0, 0)\}$. Ta có $a(a_1, a_2) = 0$ khi và chỉ khi $a_1 + a_2 = 0$ khi và chỉ khi $a_1 = -a_2$. Vì $a_1 \in H_1$ và $a_2 \in H_2$, ta thấy rằng $a_1, a_2 \in H_1 \cap H_2 = \{0\}$, suy ra $a_1 = a_2 = 0$, điều này chứng tỏ $\operatorname{Ker} a = \{(0, 0)\}$. $\square$

Dưới các điều kiện của Mệnh đề 2.13, cụ thể là $H_1 \cap H_2 = \{0\}$, nhóm $H_1 + H_2$ được gọi là *tổng trực tiếp* (*direct sum*) của $H_1$ và $H_2$; nó được ký hiệu bởi $H_1 \oplus H_2$, và ta có đẳng cấu $H_1 \times H_2 \cong H_1 \oplus H_2$.
