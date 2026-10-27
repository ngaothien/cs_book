# Liên hợp (adjoint) của Ánh xạ tuyến tính (linear map)


<!-- PAGE 1028 -->

## 29.4 Liên hợp (adjoint) của Ánh xạ tuyến tính (linear map)

Cho $E_{1}$ và $E_{2}$ là hai vectơ $K$ các không gian, và cho $\phi_{1}$: $E_{1}\times E_{1} \to K$ là dạng nửa tuyến tính (sesquilinear form) trên $E_{1}$ và $\phi_{2}$: $E_{2} \times  E_{2} \to K$ là dạng nửa tuyến tính (sesquilinear form) trên $E_{2}$. Nó là cũng khả dĩ/có thể đến deal với nhiều hơn/thêm tổng quát tình huống ở đâu ta có bốn các không gian vectơ $E_{1}, F_{1}, E_{2}, F_{2}$ và hai các dạng nửa tuyến tính $\phi_{1}$: $E_{1} \times  F_{1} \to K$ và $\phi_{2}$: $E_{2} \times  F_{2} \to K$, nhưng ta sẽ để lại điều này tổng quát hóa như một bài tập. Ta cũng giả sử rằng $l_{\phi1}$ và $r_{\phi1}$ là song ánh (bijective), mà suy ra rằng rằng $\phi_{1}$ là không suy biến. Điều này là automatic nếu không gian $E_{1}$ là hữu hạn dimensional và $\phi_{1}$ là không suy biến. Cho trước bất kỳ ánh xạ tuyến tính (linear map) $f$: $E_{1} \to E_{2}$, với mọi cố định $u \in E_{2}$, ta có thể xét dạng tuyến tính (linear form) trong $E_{1}^{*}$ cho trước bởi
$$x \mapsto \phi_{2} (f(x), u),x \in E_{1}.$$
$$\frac{Since}{E_{1}} r_{\phi1} : \overline{E}_{1} \to E_{1}^{*} is bijective, there is a unique y \in E_{1} (because the vector spaces E_{1} and$$
Chỉ khác nhau bởi vô hướng (scalar) phép nhân), sao cho
$$\phi_{2} (f(x), u) = \phi_{1} (x, y),for all x \in E_{1}.$$
Nếu ta ký hiệu điều này duy nhất $y \in E_{1}$ bởi $f^{*l} (u)$, thì ta có
$$\phi_{2} (f(x), u) = \phi_{1} (x, f^{*l} (u)),for all x \in E_{1}, and all u \in E_{2}.$$
Do đó, ta thu được hàm $f^{*l}$: $E_{2} \to E_{1}$. Ta khẳng định rằng hàm này là ánh xạ tuyến tính (linear map). Với mọi $v_{1}, v_{2} \in E_{2}$, ta có
$$\phi_{2} (f(x), v_{1} + v_{2}) = \phi_{2} (f(x), v_{1}) + \phi_{2} (f(x), v_{2})$$
$$= \phi_{1} (x, f^{*l} (v_{1})) + \phi_{1} (x, f^{*l} (v_{2}))$$
$$= \phi_{1} (x, f^{*l} (v_{1}) + f^{*l} (v_{2}))$$
$$= \phi_{1} (x, f^{*l} (v_{1} + v_{2})),$$
Với mọi $x \in E_{1}$. Vì $r_{\phi1}$ là đơn ánh (injective), ta kết luận rằng
$$f^{*l} (v_{1} + v_{2}) = f^{*l} (v_{1}) + f^{*l} (v_{2}).$$
Với mọi $\lambda  \in K$, ta có
$$\phi_{2} (f(x), \lambda v) =\overline{\lambda \phi}_{2}(f(x), v)$$
$$=\overline{\lambda \phi}_{1}(x, f^{*l} (v))$$
$$= \phi_{1} (x, \lambda f^{*l} (v))$$
$$= \phi_{1} (x, f^{*l} (\lambda v)),$$
Với mọi $x \in E_{1}$. Vì $r_{\phi1}$ là đơn ánh (injective), ta kết luận rằng
$$f^{*l} (\lambda v) = \lambda f^{*l} (v).$$

<!-- PAGE 1029 -->
Vì vậy, $f^{*l}$ là tuyến tính. Ta gọi nó trái liên hợp (adjoint) của $f$. Bây giờ, với mọi cố định $u \in E_{2}$, ta có thể xét dạng tuyến tính (linear form) trong $E_{1}^{*}$ cho trước bởi
$$x \mapsto \overline{\phi}_{2}\overline{(}\overline{u, f}\overline{(}\overline{x}\overline{))} x \in E_{1}.$$
Vì $l_{\phi1}$: $\overline{E}_{1} \to E_{1}^{*}$ là song ánh (bijective), tồn tại duy nhất một $y \in E_{1}$ sao cho
$$\overline{\phi}_{2}\overline{(}\overline{u, f}\overline{(}\overline{x}\overline{)) =}\overline{\phi}_{1}\overline{(}\overline{y, x}\overline{)},for all x \in E_{1}.$$
Nếu ta ký hiệu điều này duy nhất $y \in E_{1}$ bởi $f^{*r} (u)$, thì ta có
$$\phi_{2} (u, f(x)) = \phi_{1} (f^{*r} (u), x),for all x \in E_{1}, and all u \in E_{2}.$$
Do đó, ta thu được hàm $f^{*r}$: $E_{2} \to E_{1}$. Như trong trước đó tình huống, nó dễ để kiểm tra rằng $f^{*r}$ là tuyến tính. Ta gọi nó phải liên hợp (adjoint) của $f$. Trong tóm tắt, ta tạo sau đây định nghĩa.

> **Định nghĩa 29.14.** Cho $E_{1}$ và $E_{2}$ là hai vectơ $K$ các không gian, và cho $\phi_{1}$: $E_{1} \times  E_{1} \to K$ và $\phi_{2}$: $E_{2} \times  E_{2} \to K$ là hai các dạng nửa tuyến tính. Giả sử rằng $l_{\phi1}$ và $r_{\phi1}$ là song ánh (bijective), sao cho $\phi_{1}$ là nondegnerate. Với mọi ánh xạ tuyến tính (linear map) $f$: $E_{1} \to E_{2}$, ở đó tồn tại duy nhất các ánh xạ tuyến tính (linear maps) $f^{*l}$: $E_{2} \to E_{1}$ và $f^{*r}$: $E_{2} \to E_{1}$, sao cho
$$\phi_{2} (f(x), u) = \phi_{1} (x, f^{*l} (u)),for all x \in E_{1}, and all u \in E_{2}$$
$$\phi_{2} (u, f(x)) = \phi_{1} (f^{*r} (u), x),for all x \in E_{1}, and all u \in E_{2}.$$
Ánh xạ $f^{*l}$ được gọi là trái liên hợp (adjoint) của $f$, và ánh xạ $f^{*r}$ được gọi là phải liên hợp (adjoint) của $f$. Nếu $E_{1}$ và $E_{2}$ là hữu hạn chiều với các cơ sở $(e_{1}, \dots  , e_{m})$ và $(f_{1}, \dots  , f_{n})$, thì ta có thể hoạt động/công trình ra các ma trận $A^{*l}$ và $A^{*r}$ tương ứng với trái liên hợp (adjoint) $f^{*l}$ và phải liên hợp (adjoint) $f^{*r}$ của $f$. Assumine rằng $f$ được biểu diễn bởi ma trận cỡ $n \times  m$ $A, \phi_{1}$ được biểu diễn bởi ma trận cỡ $m \times  m$ $M_{1}$, và $\phi_{2}$ được biểu diễn bởi ma trận cỡ $n \times  n$ $M_{2}$. Vì
$$\phi_{1} (x, f^{*l} (u)) = (A^{*l}u)^{*}M_{1}x = u^{*}(A^{*l})^{*}M_{1}x$$
$$\phi_{2} (f(x), u) = u^{*}M_{2}Ax$$
Ta tìm rằng $(A^{*l})^{*}M_{1} = M_{2}A$, nghĩa là $(A^{*l})^{*} = M_{2}AM_{1}^{-1}$, và tương tự
$$\phi_{1} (f^{*r} (u), x) = x^{*}M_{1}A^{*r}u$$
$$\phi_{2} (u, f(x)) = (Ax)^{*}M_{2}u = x^{*}A^{*}M_{2}u,$$
Ta có $M_{1}A^{*r} = A^{*}M_{2}$, nghĩa là $A^{*r} = (M_{1})^{-1}A^{*}M_{2}$. Do đó, ta thu được
$$A^{*l}= (M_{1}^{*})^{-1}A^{*}M_{2}^{*}$$
$$A^{*r}= (M_{1})^{-1}A^{*}M_{2}.$$
