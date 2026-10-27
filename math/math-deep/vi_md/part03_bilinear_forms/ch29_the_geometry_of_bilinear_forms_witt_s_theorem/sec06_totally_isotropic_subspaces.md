# một cách tổng Đẳng hướng Các không gian con


<!-- PAGE 1034 -->

## 29.6 một cách tổng Đẳng hướng Các không gian con

Trong mục này, ta deal với $\epsilon$ -Hermite các dạng, $\phi$: $E \times  E \to K$. Nói chung, $E$ có thể có các không gian con $U$ sao cho $U \cap U^{\perp} \neq  (0)$, hoặc tệ hơn, sao cho $U \subseteq U^{\perp}$ (rằng là, $\phi$ là không trên $U)$. Ta sẽ xem rằng như vậy các không gian con đóng then chốt trong phân rã của $E$ vào trực giao các không gian con.

> **Định nghĩa 29.17.** Cho trước $\epsilon$ -Hermite các dạng $\phi$: $E \times  E \to K$, khác không vectơ $u \in E$ được nói là đẳng hướng nếu $\phi (u, u) = 0$. Nó là thuận tiện đến xét $0$ là đẳng hướng. Cho trước bất kỳ không gian con $U$ của $E$, không gian con rad(U) $= U \cap U^{\perp}$ được gọi là radical của $U$. Ta nói rằng
$(i) U$ là suy biến nếu rad(U) $\neq  (0)$ (tương đương nếu tồn tại một khác không vectơ $u \in U$ sao cho $x \in U^{\perp}$). Ngược lại, ta nói rằng $U$ là không suy biến.
(ii) $U$ là một cách tổng đẳng hướng nếu $U \subseteq U^{\perp}$ (tương đương nếu thu hẹp của $\phi$ đến $U$ là không). Theo Định nghĩa, tầm thường không gian con $U = (0) (= {0})$ là không suy biến. Nhận thấy rằng không gian con $U$ là không suy biến khi và chỉ khi thu hẹp của $\phi$ đến $U$ là không suy biến. suy biến không gian con đôi khi được gọi là một đẳng hướng không gian con. Khác các tác giả nói rằng không gian con $U$ là đẳng hướng nếu nó chứa một số (khác không) vectơ đẳng hướng (isotropic vector). không gian con mà có không có khác không vectơ đẳng hướng (isotropic vector) là thường được gọi là dị hướng. không gian của tất cả đẳng hướng các vectơ là nón thường được gọi là light nón (thuật ngữ coming từ lý thuyết của relativity). Điều này là không là confused với nón của silence (từ Thu được Smart)! Nó nên cũng được lưu ý rằng một số các tác giả (chẳng hạn như Serre) sử dụng số hạng đẳng hướng thay vì của một cách tổng đẳng hướng. apparent lack của tiêu chuẩn thuật ngữ là hầu như như xấu như trong đồ thị lý thuyết! Rõ ràng là bất kỳ tổng trực tiếp (direct sum) của đôi một trực giao một cách tổng đẳng hướng các không gian con là một cách tổng đẳng hướng. Do đó, mọi một cách tổng đẳng hướng không gian con được chứa trong một số cực đại một cách tổng đẳng hướng không gian con. Ở đây là một cái khác sự kiện rằng ta sẽ sử dụng tất cả time: nếu $V$ là một cách tổng đẳng hướng không gian con và nếu $U$ là không gian con của $V$, thì $U$ là một cách tổng đẳng hướng. Điều này là bởi vì theo Định nghĩa $V$ là đẳng hướng nếu $V \subseteq V^{\perp}$, và vì $U \subseteq V$ ta thu được $V^{\perp} \subseteq U^{\perp}$, do đó $U \subseteq V \subseteq V^{\perp} \subseteq U^{\perp}$, mà chỉ ra rằng $U$ là một cách tổng đẳng hướng. Thứ nhất, cho chúng ta chỉ ra rằng trong thứ tự đến sudy $\epsilon$ -Hermite tạo thành trên không gian $E$, nó suffices đến thu hẹp của ta attention đến không suy biến các dạng.

> **Mệnh đề 29.19.** Cho trước $\epsilon$ -Hermite tạo thành $\phi$: $E \times  E \to K$ trên $E$, ta có:
() Nếu $U$ và $V$ là bất kỳ hai trực giao các không gian con của $E$, thì
$$rad(U + V ) = rad(U) + rad(V ).$$
$(b)$ rad(rad(E)) $=$ rad(E).

<!-- PAGE 1035 -->
$(c)$ Nếu $U$ là bất kỳ không gian con supplementary đến rad(E), sao cho
$$E = rad(E) \oplus U,$$
Thì $U$ là không suy biến, và rad(E) và $U$ là trực giao.

*Chứng minh.* () Nếu $U$ và $V$ là trực giao, thì $U \subseteq V^{\perp}$ và $V \subseteq U^{\perp}$. Ta thu được
$$rad(U + V ) = (U + V ) \cap (U + V )^{\perp}$$
$$= (U + V ) \cap U^{\perp} \cap V^{\perp}$$
$$= U \cap U^{\perp} \cap V^{\perp} + V \cap U^{\perp} \cap V^{\perp}$$
$$= U \cap U^{\perp} + V \cap V^{\perp}$$
$$= rad(U) + rad(V ).$$
$(b)$ Theo Định nghĩa, rad(E) $= E^{\perp}$, và hiển nhiên $E = E^{\perp \perp}$, do đó ta thu được
$$rad(rad(E)) = E^{\perp}\cap E^{\perp \perp}= E^{\perp}\cap E = E^{\perp}= rad(E).$$
$(c)$ Nếu $E =$ rad(E) $\oplus U$, theo định nghĩa của rad(E), các không gian con rad(E) và $U$ là trực giao. Từ () và $(b)$, ta thu được
$$rad(E) = rad(E) + rad(U).$$
Vì rad(U) $= U \cap U^{\perp} \subseteq U$ và vì rad(E) $\oplus U$ là tổng trực tiếp (direct sum), ta có tổng trực tiếp (direct sum)
$$rad(E) = rad(E) \oplus rad(U),$$
Mà suy ra rằng rad(U) $= (0)$; nghĩa là, $U$ là không suy biến. Mệnh đề 29.19(c) chỉ ra rằng thu hẹp của $\phi$ đến bất kỳ supplement $U$ của rad(E) là không suy biến và $\phi$ là không trên rad(U), do đó ta có thể thu hẹp của ta attention đến không suy biến các dạng. sau đây là cũng then chốt kết quả.

> **Mệnh đề 29.20.** Cho trước $\epsilon$ -Hermite tạo thành $\phi$: $E \times  E \to K$ trên $E$, nếu $U$ là hữu hạn chiều không suy biến không gian con của $E$, thì $E = U \oplus U^{\perp}$.

*Chứng minh.* Bởi giả thiết, thu hẹp $\phi_{U}$ của $\phi$ đến $U$ là không suy biến, do đó nửa tuyến tính (semilinear) ánh xạ $r_{\phi U}$: $U \to U^{*}$ là đơn ánh (injective). Vì $U$ là hữu hạn chiều, $r_{\phi U}$ là thực sự song ánh (bijective), do đó với mọi $v \in E$, nếu ta xét dạng tuyến tính (linear form) trong $U^{*}$ cho trước bởi $u \mapsto \phi (u, v) (u \in U)$, tồn tại duy nhất một $v_{0} \in U$ sao cho
$$\phi (u, v_{0}) = \phi (u, v)for all u \in U;$$
Rằng là, $\phi (u, v$ - $v_{0}) = 0$ với mọi $u \in U$, do đó $v$ - $v_{0} \in U^{\perp}$. Suy ra rằng $v = v_{0} + v$ - $v_{0}$, với $v_{0} \in U$ và $v_{0}$ - $v \in U^{\perp}$, và vì $U$ là không suy biến $U \cap U^{\perp} = (0)$, và $E = U \oplus U^{\perp}$. Như hệ quả của Mệnh đề 29.20, ta thu được kết quả sau đây.

<!-- PAGE 1036 -->

> **Mệnh đề 29.21.** Cho trước $\epsilon$ -Hermite tạo thành $\phi$: $E\times E \to K$ trên $E$, nếu $\phi$ là không suy biến và nếu $U$ là hữu hạn chiều không gian con của $E$, thì rad(U) $= rad(U^{\perp}$), và các điều kiện sau đây là tương đương:
$(i) U$ là không suy biến.
(ii) $U^{\perp}$ là không suy biến.
(iii) $E = U \oplus U^{\perp}$.

*Chứng minh.* Theo Định nghĩa, $rad(U^{\perp}$) $= U^{\perp} \cap U^{\perp \perp}$, và vì $\phi$ là không suy biến và $U$ là hữu hạn chiều, $U^{\perp \perp} = U$, do đó $rad(U^{\perp}$) $= U^{\perp} \cap U^{\perp \perp} = U \cap U^{\perp} =$ rad(U). Theo Mệnh đề 29.20, $(i)$ suy ra (iii). Nếu $E = U \oplus U^{\perp}$, thì rad(U) $= U \cap U^{\perp} = (0)$, do đó $U$ là không suy biến và (iii) suy ra $(i)$. Vì $rad(U^{\perp}$) $=$ rad(U), (iii) cũng suy ra (ii). Bây giờ, nếu $U^{\perp}$ là không suy biến, ta có $U^{\perp} \cap U^{\perp \perp} = (0)$, và vì $U \subseteq U^{\perp \perp}$, ta thu được
$$U \cap U^{\perp} \subseteq U^{\perp \perp} \cap U^{\perp} = (0),$$
Mà chỉ ra rằng $U$ là không suy biến, chứng minh implication (ii) $=\Rightarrow (i)$. Nếu $E$ là hữu hạn chiều, ta có kết quả sau các kết quả.

> **Mệnh đề 29.22.** Cho trước $\epsilon$ -Hermite tạo thành $\phi$: $E \times  E \to K$ trên hữu hạn chiều không gian $E$, nếu $\phi$ là không suy biến, thì với mọi không gian con $U$ của $E$ ta có
$(i)$ dim(U) $+ dim(U^{\perp}$) $=$ dim(E).
(ii) $U^{\perp \perp} = U$.

*Chứng minh.* $(i)$ Vì $\phi$ là không suy biến và $E$ là hữu hạn chiều, nửa tuyến tính (semilinear) ánh xạ $l_{\phi}$: $E \to E^{*}$ là song ánh (bijective). Bởi phép chuyển vị, inclusion $i: U \to E$ cho ta toàn ánh $r: E^{*} \to U^{*}$ (với r(f) $= f \circ i$ với mọi $f \in E^{*}$; ánh xạ $f \circ i$ là thu hẹp của dạng tuyến tính (linear form) $f$ đến $U)$. Suy ra rằng nửa tuyến tính (semilinear) ánh xạ $r \circ l_{\phi}$: $E \to U^{*}$ cho trước bởi
$$(r \circ l_{\phi})(x)(u) =\overline{\phi}\overline{(}\overline{x, u}\overline{)} x \in E, u \in U$$
Là toàn ánh (surjective), và hạt nhân (hạt nhân (kernel)) của nó là $U^{\perp}$. Do đó, ta có
$$\dim(U^{*} ) + \dim(U^{\perp} ) = \dim(E),$$
Và vì dim(U) $= dim(U^{*}$) bởi vì $U$ là hữu hạn chiều, ta thu được
$$\dim(U) + \dim(U^{\perp} ) = \dim(U^{*} ) + \dim(U^{\perp} ) = \dim(E).$$
(ii) Áp dụng ở trên công thức đến $U^{\perp}$, ta suy ra rằng dim(U) $= dim(U^{\perp \perp}$). Vì $U \subseteq U^{\perp \perp}$, ta phải có $U^{\perp \perp} = U$.

<!-- PAGE 1037 -->
Nhận xét: Ta đã được chứng minh trong Mệnh đề 29.13 rằng nếu $U$ là hữu hạn chiều, thì $codim(U^{\perp}$) $=$ dim(U) và $U^{\perp \perp} = U$, nhưng nó không’t hurt đến cho một cái khác chứng minh. Nhận thấy rằng
$(i)$ suy ra rằng
$$\dim(U) + \dim(rad(U)) \le \dim(E).$$
Ta có thể bây giờ tiến hành với Witt phân rã, nhưng trước rằng, ta quickly lấy care của cấu trúc định lý cho thay phiên các dạng song tuyến tính (trường hợp ở đâu $\phi (u, u) = 0$ với mọi $u \in E)$. Cho dạng song tuyến tính thay phiên, không gian $E$ là một cách tổng đẳng hướng. Ví dụ trong số chiều $2$, ma trận
$$B = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$$
Định nghĩa thay phiên tạo thành cho trước bởi
$$\phi ((x_{1}, y_{1}), (x_{2}, y_{2})) = x_{1}y_{2} -x_{2}y_{1}.$$
Trường hợp này là đáng ngạc nhiên là tổng quát.

> **Mệnh đề 29.23.** Cho $\phi$: $E \times  E \to K$ là dạng song tuyến tính thay phiên trên $E$. Nếu $u, v \in E$ là hai (khác không) các vectơ sao cho $\phi (u, v) = \lambda  \neq  0$, thì $u$ và $v$ là độc lập tuyến tính (linearly independent). Nếu ta cho $u_{1} = \lambda^{-1} u$ và $v_{1} = v$, thì $\phi (u_{1}, v_{1}) = 1$, và thu hẹp của $\phi$ đến mặt phẳng được sinh (spanned) bởi $u_{1}$ và $v_{1}$ được biểu diễn bởi ma trận
$$\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} .$$

*Chứng minh.* Nếu $u$ và $v$ đã là phụ thuộc tuyến tính (linearly dependent), như $u, v \neq  0$, ta có thể viết $v = \mu u$ với một số $\mu  \neq  0$, nhưng khi đó, vì $\phi$ là thay phiên, ta sẽ có
$$\lambda  = \phi (u, v) = \phi (u, \mu u) = \mu \phi (u, u) = 0,$$
Contradicting sự kiện rằng $\lambda  \neq  0$. rest là hiển nhiên. Mệnh đề 29.23 cho ta mặt phẳng được sinh (spanned) bởi hai các vectơ $u_{1}, v_{1}$ sao cho $\phi (u_{1}, u_{1}) = \phi (v_{1}, v_{1}) = 0$ và $\phi (u_{1}, v_{1}) = 1$. Như vậy mặt phẳng được gọi là một mặt phẳng hyperbolic (hyperbolic plane). Nếu $E$ là hữu hạn chiều, ta thu được kết quả sau định lý.

> **Định lý 29.24.** Cho $\phi$: $E \times  E \to K$ là dạng song tuyến tính thay phiên trên không gian $E$ của hữu hạn số chiều $n$. Thì, có một tổng trực tiếp (direct sum) phân rã của $E$ vào đôi một trực giao các không gian con
$$E = W_{1} \oplus \cdots  \oplus W_{r} \oplus rad(E),$$
Ở đâu mỗi $W_{i}$ là mặt phẳng hyperbolic (hyperbolic plane) và rad(E) $= E^{\perp}$. Vì vậy, có một cơ sở (basis) của $E$ của tạo thành
$$(u_{1}, v_{1}, \dots  , u_{r}, v_{r}, w_{1}, \dots  , w_{n-2r}),$$

<!-- PAGE 1038 -->
Đối với mà ma trận biểu diễn $\phi$ là khối ma trận đường chéo (diagonal matrix) $M$ của tạo thành
$$M = \begin{pmatrix} J & 0 \\ J \\ \ddots \\ J \\ 0 & 0_{n-2r} \end{pmatrix} ,$$
Với
$$J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} .$$

*Chứng minh.* Nếu $\phi  = 0$, thì $E = E^{\perp}$ và ta được thực hiện. Ngược lại, có hai khác không các vectơ $u, v \in E$ sao cho $\phi (u, v) \neq  0$, do đó theo Mệnh đề 29.23, ta thu được mặt phẳng hyperbolic (hyperbolic plane) $W_{2}$ được sinh (spanned) bởi hai các vectơ $u_{1}, v_{1}$ sao cho $\phi (u_{1}, v_{1}) = 1$. không gian con $W_{1}$ là không suy biến (ví dụ, det(J) $= -1)$, do đó theo Mệnh đề 29.21, ta thu được tổng trực tiếp (direct sum)
$$E = W_{1} \oplus W_{1}^{\perp}  .$$
Theo Mệnh đề 29.14, ta cũng có
$$E^{\perp}= (W_{1} \oplus W_{1}^{\perp}  ) = W_{1}^{\perp} \cap W_{1}^{\perp \perp}= rad(W_{1}^{\perp}  ).$$
Theo giả thiết quy nạp ứng dụng đến $W_{1}^{\perp}$, ta thu được định lý của chúng ta. sau đây hệ quả suy ra ngay lập tức.

> **Mệnh đề 29.25.** Cho $\phi$: $E \times  E \to K$ là dạng song tuyến tính thay phiên trên không gian $E$ của hữu hạn số chiều $n$.
$(1)$ hạng (rank) của $\phi$ là chẵn/ngay cả.
$(2)$ Nếu $\phi$ là không suy biến, thì dim(E) $= n$ là chẵn/ngay cả.
$(3)$ Hai thay phiên các dạng song tuyến tính $\phi_{1}$: $E_{1} \times E_{1} \to K$ và $\phi_{2}$: $E_{2} \times E_{2} \to K$ là tương đương khi và chỉ khi $dim(E_{1}) = dim(E_{2})$ và $\phi_{1}$ và $\phi_{2}$ có cùng hạng (rank). chỉ phần rằng đòi hỏi chứng minh là phần $(3)$, mà là trái như dễ bài tập. Nếu $\phi$ là không suy biến, thì $n =$ 2r, và cơ sở (basis) của $E$ như trong Định lý 29.24 được gọi là một symplectic cơ sở (basis). không gian $E$ được gọi là một hyperbolic không gian (hoặc symplectic không gian). Nhận thấy rằng nếu ta reorder các vectơ trong cơ sở (basis)
$$(u_{1}, v_{1}, \dots  , u_{r}, v_{r}, w_{1}, \dots  , w_{n-2r})$$
Để thu được cơ sở (basis)
$$(u_{1}, \dots  , u_{r}, v_{1}, \dots  v_{r}, w_{1}, \dots  , w_{n-2r}),$$

<!-- PAGE 1039 -->
Thì ma trận biểu diễn $\phi$ trở thành
$$\begin{pmatrix} 0 & I_{r} & 0 \\ -I_{r} & 0 & 0 \\ 0 & 0 & 0_{n-2r} \end{pmatrix} .$$
Điều này một cách cụ thể đơn giản ma trận là thường được ưu tiên hơn, especially khi dealing với các ma trận (symplectic các ma trận) biểu diễn các phép đẳng cự của $\phi$ (trong mà trường hợp $n =$ 2r). Như warm lên cho Mệnh đề 29.29 của tiếp theo mục, ta chứng minh tương tự của Mệnh đề 29.23 trong trường hợp của dạng song tuyến tính đối xứng.

> **Mệnh đề 29.26.** Cho $\phi$: $E\times E \to K$ là không suy biến dạng song tuyến tính đối xứng với $K$ trường của characteristic khác nhau từ $2$. Với mọi khác không vectơ đẳng hướng (isotropic vector) $u$, ở đó là một cái khác khác không vectơ đẳng hướng (isotropic vector) $v$ sao cho $\phi (u, v) = 2$, và $u$ và $v$ là độc lập tuyến tính (linearly independent). Trong cơ sở (basis) $(u, v/2)$, thu hẹp của $\phi$ đến mặt phẳng được sinh (spanned) bởi $u$ và $v/2$ là của tạo thành
$$\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} .$$

*Chứng minh.* Vì $\phi$ là không suy biến, tồn tại một khác không vectơ $z$ sao cho (rescaling $z$ nếu cần) $\phi (u, z) = 1$. Nếu
$$v = 2z -\phi (z, z)u,$$
Khi đó vì $\phi (u, u) = 0$ và $\phi (u, z) = 1$, lưu ý rằng
$$\phi (u, v) = \phi (u, 2z -\phi (z, z)u) = 2\phi (u, z) -\phi (z, z)\phi (u, u) = 2,$$
Và
$$\phi (v, v) = \phi (2z -\phi (z, z)u, 2z -\phi (z, z)u)$$
$$= 4\phi (z, z) -4\phi (z, z)\phi (u, z) + \phi (z, z)^{2}\phi (u, u)$$
$$= 4\phi (z, z) -4\phi (z, z) = 0.$$
Nếu $u$ và $z$ đã là phụ thuộc tuyến tính (linearly dependent), như $u, z \neq  0$, ta có thể viết $z = \mu u$ với một số $\mu  \neq  0$, nhưng khi đó, ta sẽ có
$$\phi (u, z) = \phi (u, \mu u) = \mu \phi (u, u) = 0,$$
Contradicting sự kiện rằng $\phi (u$, z)̸ $= 0$. Thì $u$ và $v =$ 2z - $\phi (z$, z)u là cũng độc lập tuyến tính (linearly independent), vì ngược lại $z$ có thể được biểu diễn như bội của $u$. rest là hiển nhiên. Mệnh đề 29.26 cho ta mặt phẳng được sinh (spanned) bởi hai các vectơ $u_{1}, v_{1}$ sao cho $\phi (u_{1}, u_{1}) = \phi (v_{1}, v_{1}) = 0$ và $\phi (u_{1}, v_{1}) = 1$. Như vậy mặt phẳng được gọi là một Artinian mặt phẳng. Mệnh đề 29.26 cũng chỉ ra rằng khác không đẳng hướng các vectơ đến trong cặp. Mệnh đề 29.26 có sau đây hệ quả mà có các ứng dụng trong số lý thuyết; xem Serre $[163]$, Chương IV.
