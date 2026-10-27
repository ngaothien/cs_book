# Các phép đẳng cự Liên kết với Các dạng nửa tuyến tính


<!-- PAGE 1030 -->
Nếu $\phi_{1}$ và $\phi_{2}$ là đối xứng các dạng song tuyến tính, thì $f^{*l}  = f^{*r}$. Điều này cũng nghiệm đúng nếu $\phi$ là $\epsilon$ -Hermite. Thật vậy, vì
$$\phi_{2} (u, f(x)) = \phi_{1} (f^{*r} (u), x),$$
Ta thu được
$$\overline{\epsilon \phi}_{2}\overline{(}\overline{f}\overline{(}\overline{x}\overline{)}\overline{, u}\overline{) =}\overline{\epsilon \phi}_{1}\overline{(}\overline{x, f}^{*r} \overline{(}\overline{u}\overline{))},$$
Và vì $\lambda  \mapsto \overline{\lambda}$ là phép đối hợp (involution), ta thu được
$$\phi_{2} (f(x), u) = \phi_{1} (x, f^{*r} (u)).$$
Vì ta cũng có
$$\phi_{2} (f(x), u) = \phi_{1} (x, f^{*l} (u)),$$
Ta thu được
$$\phi_{1} (x, f^{*r} (u)) = \phi_{1} (x, f^{*l} (u))for all x \in E_{1}, and all u \in E_{2},$$
Và vì $\phi_{1}$ là không suy biến, ta kết luận rằng $f^{*l}  = f^{*r}$. Bất cứ khi nào $f^{*l}  = f^{*r}$, ta sử dụng đơn giản hơn ký hiệu $f^{*}$. Nếu $f$: $E_{1} \to E_{2}$ và $g: E_{1} \to E_{2}$ là hai các ánh xạ tuyến tính (linear maps), ta có các tính chất sau đây:
$$(f + g)^{*l}= f^{*l}+ g^{*l}$$
$$id^{*l}= id$$
$$(\lambda f)^{*l}=\overline{\lambda f}^{*l},$$
Và tương tự cho phải các liên hợp (adjoint). Nếu $E_{3}$ là một cái khác không gian, $\phi_{3}$ là dạng nửa tuyến tính (sesquilinear form) trên $E_{3}$, và nếu $l_{\phi2}$ và $r_{\phi2}$ là song ánh (bijective), thì với mọi các ánh xạ tuyến tính (linear maps) $f$: $E_{1} \to E_{2}$ và $g: E_{2} \to E_{3}$, ta có
$$(g \circ f)^{*l}= f^{*l}\circ g^{*l},$$
Và tương tự cho phải các liên hợp (adjoint). Hơn nữa, nếu $E_{1} = E_{2} = E$ và $\phi$: $E \times  E \to K$ là $\epsilon$ -Hermite, với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$ (nhắc lại rằng trong điều này trường hợp $f^{*l}  = f^{*r}  = f^{*}$), ta có
$$f^{**} =\overline{\epsilon \epsilon f.}$$

## 29.5 Các phép đẳng cự Liên kết với Các dạng nửa tuyến tính

Khái niệm của liên hợp (adjoint) là tốt công cụ đến investigate khái niệm của phép đẳng cự (isometry) giữa các không gian được trang bị các dạng nửa tuyến tính. Thứ nhất, ta định nghĩa mêtric các ánh xạ và các phép đẳng cự.

> **Định nghĩa 29.15.** Nếu $(E_{1}, \phi_{1}$) và $(E_{2}, \phi_{2}$) là hai các cặp của các không gian và nửa tuyến tính (sesquilinear) các ánh xạ $\phi_{1}$: $E_{1} \times  E_{1} \to K$ và $\phi_{2}$: $E_{2} \times  E_{2} \to K$, mêtric ánh xạ từ $(E_{1}, \phi_{1}$) đến $(E_{2}, \phi_{2}$) là ánh xạ tuyến tính (linear map) $f$: $E_{1} \to E_{2}$ sao cho
$$\phi_{1} (u, v) = \phi_{2} (f(u), f(v))for all u, v \in E_{1}.$$
Ta nói rằng $\phi_{1}$ và $\phi_{2}$ là tương đương khi và chỉ khi có một mêtric ánh xạ $f$: $E_{1} \to E_{2}$ mà là song ánh (bijective). Như vậy mêtric ánh xạ được gọi là một phép đẳng cự (isometry).

<!-- PAGE 1031 -->
Bài toán của phân loại các dạng nửa tuyến tính sai khác equivalence là quan trọng nhưng rất khó bài toán. Việc giải bài toán này phụ thuộc intimately trên các tính chất của trường $K$, và đầy đủ câu trả lời là chỉ đã biết trong một vài các trường hợp. bài toán là dễ dàng được giải cho $K = \mathbb{R}, K = \mathbb{C}$. Nó cũng được giải cho hữu hạn các trường và cho $K = \mathbb{Q}$ (các hữu tỷ), nhưng nghiệm là đáng ngạc nhiên là liên quan! Nó là khó đến nói anything thú vị nếu $\phi_{1}$ là suy biến và nếu ánh xạ tuyến tính (linear map) $f$ thực hiện không có các liên hợp (adjoint). tiếp theo một vài các mệnh đề tạo sử dụng của tự nhiên các điều kiện trên $\phi_{1}$ rằng cho hữu ích tiêu chuẩn cho đang là mêtric ánh xạ.

> **Mệnh đề 29.16.** Với cùng các giả định như trong Định nghĩa 29.14 (mà suy ra rằng $\phi_{1}$ là không suy biến), nếu $f$: $E_{1} \to E_{2}$ là song ánh (bijective) ánh xạ tuyến tính (linear map), thì ta có
$$\phi_{1} (x, y) = \phi_{2} (f(x), f(y))for all x, y \in E_{1} iff$$
$$f^{-1}= f^{*l}= f^{*r}.$$

*Chứng minh.* Ta có
$$\phi_{1} (x, y) = \phi_{2} (f(x), f(y))$$
Khi và chỉ khi
$$\phi_{1} (x, y) = \phi_{2} (f(x), f(y)) = \phi_{1} (x, f^{*l} (f(y))$$
Khi và chỉ khi
$$\phi_{1} (x, (id -f^{*l}\circ f)(y)) = 0for all x \in E_{1} and all y \in E_{2}.$$
Vì $\phi_{1}$ là không suy biến, ta phải có
$$f^{*l}\circ f = id,$$
Mà suy ra rằng $f^{-1} = f^{*l}$. Tương tự,
$$\phi_{1} (x, y) = \phi_{2} (f(x), f(y))$$
Khi và chỉ khi
$$\phi_{1} (x, y) = \phi_{2} (f(x), f(y)) = \phi_{1} (f^{*r} (f(x)), y)$$
Khi và chỉ khi
$$\phi_{1} ((id -f^{*r}\circ f)(x), y) = 0for all x \in E_{1} and all y \in E_{2}.$$
Vì $\phi_{1}$ là không suy biến, ta phải có
$$f^{*r}\circ f = id,$$
Mà suy ra rằng $f^{-1} = f^{*r}$. Vì vậy, $f^{-1} = f^{*l} = f^{*r}$. Cho điều ngược lại, thực hiện các phép tính trong reverse. Như hệ quả, ta thu được sau đây quan trọng mệnh đề.

<!-- PAGE 1032 -->

> **Mệnh đề 29.17.** Nếu $\phi$: $E \times  E \to K$ là nửa tuyến tính (sesquilinear) ánh xạ, và nếu $l_{\phi}$ và $r_{\phi}$ là song ánh (bijective), với mọi song ánh (bijective) ánh xạ tuyến tính (linear map) $f$: $E \to E$, thì ta có
$$\phi (f(x), f(y)) = \phi (x, y)for all x, y \in E iff$$
$$f^{-1}= f^{*l}= f^{*r}.$$
Ta cũng có sau đây các sự kiện.

> **Mệnh đề 29.18.** $(1)$ Nếu $\phi$: $E \times  E \to K$ là nửa tuyến tính (sesquilinear) ánh xạ và nếu $l_{\phi}$ là đơn ánh (injective), thì với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$, nếu
$$\phi (f(x), f(y)) = \phi (x, y)for all x, y \in E,(*)$$
Thì $f$ là đơn ánh (injective).
$(2)$ Nếu $E$ là hữu hạn chiều và nếu $\phi$ là không suy biến, thì các ánh xạ tuyến tính (linear maps) $f$: $E \to E$ thỏa mãn (*) tạo thành nhóm. nghịch đảo của $f$ được cho bởi $f^{-1} = f^{*}$.

*Chứng minh.* $(1)$ Nếu f(x) $= 0$, thì
$$\phi (x, y) = \phi (f(x), f(y)) = \phi (0, f(y)) = 0for all y \in E.$$
Vì $l_{\phi}$ là đơn ánh (injective), ta phải có $x = 0$, và do đó $f$ là đơn ánh (injective).
$(2)$ Nếu $E$ là hữu hạn chiều, vì ánh xạ tuyến tính (linear map) thỏa mãn (*) là đơn ánh (injective), nó là song ánh. Theo Mệnh đề 29.17, ta có $f^{-1} = f^{*}$. Ta cũng có $\phi$ (f(x), f(y)) $= \phi ((f^{*} \circ$ f)(x), $y) = \phi (x, y) = \phi ((f \circ f^{*} )(x), y) = \phi (f^{*} (x), f^{*} (y))$, mà chỉ ra rằng $f^{*}$ thỏa mãn (*). Nếu $\phi$ (f(x), f(y)) $= \phi (x, y)$ với mọi $x, y \in E$ và $\phi$ (g(x), g(y)) $= \phi (x, y)$ với mọi $x, y \in E$, thì ta có
$$\phi ((g \circ f)(x), (g \circ f)(y)) = \phi (f(x), f(y)) = \phi (x, y)for all x, y \in E.$$
Hiển nhiên, đồng nhất thức ánh xạ $id_{E}$ thỏa mãn (*). Vì vậy, tập hợp của các ánh xạ tuyến tính (linear maps) thỏa mãn (*) là nhóm. ở trên considerations motivate sau đây định nghĩa.

> **Định nghĩa 29.16.** Cho $\phi$: $E \times  E \to K$ là nửa tuyến tính (sesquilinear) ánh xạ, và giả sử rằng $E$ là hữu hạn chiều và rằng $\phi$ là không suy biến. ánh xạ tuyến tính (linear map) $f$: $E \to E$ là phép đẳng cự (isometry) của $E$ (đối với $\phi$) khi và chỉ khi
$$\phi (f(x), f(y)) = \phi (x, y)for all x, y \in E.$$
Tập hợp tất cả các phép đẳng cự của $E$ là nhóm được ký hiệu bởi $Isom(\phi$).

<!-- PAGE 1033 -->
Nếu $\phi$ là đối xứng, thì nhóm $Isom(\phi$) được ký hiệu là $O(\phi$) và được gọi là trực giao nhóm của $\phi$. Nếu $\phi$ là thay phiên, thì nhóm $Isom(\phi$) được ký hiệu là $Sp(\phi$) và được gọi là nhóm symplectic (symplectic group) của $\phi$. Nếu $\phi$ là $\epsilon$ -Hermite, thì nhóm $Isom(\phi$) được ký hiệu là $U_{\epsilon}(\phi$) và được gọi là $\epsilon$ -unita nhóm của $\phi$. Khi $\epsilon  = 1$, ta bỏ $\epsilon$ và chỉ nói unita nhóm. Nếu $(e_{1}, \dots  , e_{n})$ là cơ sở (basis) của $E, \phi$ được biểu diễn bởi ma trận cỡ $n \times  n$ $M$, và $f$ được biểu diễn bởi ma trận cỡ $n \times  n$ $A$, vì $A^{-1} = A^{*l} = A^{*r} = M^{-1}A^{*}M$, thì ta tìm rằng $f \in Isom(\phi$) khi và chỉ khi
$$A^{*}MA = M,$$
Và $A^{-1}$ được cho bởi $A^{-1} = M^{-1}A^{*}M$. Nhiều hơn/thêm specifically, ta định nghĩa sau đây các nhóm, bằng cách sử dụng các ma trận $I_{p,q}, J_{m,m}$ và $A_{m,m}$ được định nghĩa tại kết thúc/cuối của Mục 29.1.
$(1) K =\mathbb{R}$. Ta có
$$O(n) = {A \in M_{n}(\mathbb{R}) | A^{\top}A = I_{n}}$$
$$O(p, q) = {A \in M_{p+q}(\mathbb{R}) | A^{\top}I_{p,q}A = I_{p,q}}$$
$$Sp(2n,\mathbb{R}) = {A \in M_{2n}(\mathbb{R}) | A^{\top}J_{n,n}A = J_{n,n}}$$
$$SO(n) = {A \in M_{n}(\mathbb{R}) | A^{\top}A = I_{n}, \det(A) = 1}$$
$$SO(p, q) = {A \in M_{p+q}(\mathbb{R}) | A^{\top}I_{p,q}A = I_{p,q}, \det(A) = 1}.$$
Nhóm O(n) là trực giao nhóm, $Sp(2n,\mathbb{R})$ là thực nhóm symplectic (symplectic group), và Do đó(n) là đặc biệt trực giao nhóm. Ta có thể định nghĩa nhóm
$${A \in M_{2n}(\mathbb{R}) | A^{\top}A_{n,n}A = A_{n,n}},$$
Nhưng nó là đẳng cấu đến O(n, $n)$.
$(2) K =\mathbb{C}$. Ta có
$$U(n) = {A \in M_{n}(\mathbb{C}) | A^{*}A = I_{n}}$$
$$U(p, q) = {A \in M_{p+q}(\mathbb{C}) | A^{*}I_{p,q}A = I_{p,q}}$$
$$Sp(2n,\mathbb{C}) = {A \in M_{2n}(\mathbb{C}) | A^{\top}J_{n,n}A = J_{n,n}}$$
$$SU(n) = {A \in M_{n}(\mathbb{C}) | A^{*}A = I_{n}, \det(A) = 1}$$
$$SU(p, q) = {A \in M_{p+q}(\mathbb{C}) | A^{*}I_{p,q}A = I_{p,q}, \det(A) = 1}.$$
Nhóm U(n) là unita nhóm, $Sp(2n,\mathbb{C})$ là phức nhóm symplectic (symplectic group), và SU(n) là đặc biệt unita nhóm. Nó có thể được được hiển thị rằng nếu $A \in Sp(2n,\mathbb{R})$ hoặc nếu $A \in Sp(2n,\mathbb{C})$, thì det() $= 1$.
