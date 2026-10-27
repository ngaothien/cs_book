# Witt's Định lý


<!-- PAGE 1059 -->

## 29.10 Witt’s Định lý

Witt’s định lý đã là referred đến như “scandal” bởi Emil Artin. Những gì he có nghĩa bởi điều này là rằng một đã có đến wait cho đến khi $1936$ (Witt $[196])$ đến formulate và chứng minh định lý tại một lần do đó đơn giản trong của nó phát biểu và underlying các khái niệm, và do đó hữu ích trong khác nhau các miền (hình học, arithmetic của toàn phương $forms).^{1}$ Ngoài ra Witt’s ban đầu chứng minh (Witt $[196])$, Chevalley’s chứng minh $[37]$ dường như là “tốt nhất” chứng minh rằng áp dụng đến đối xứng cũng như phản đối xứng trường hợp. chứng minh trong Bourbaki $[24]$ là based trên Chevalley’s chứng minh, và do đó là số của khác các chứng minh. Điều này là một ta suy ra (slightly reorganized). Trong đối xứng trường hợp, Serre’s trình bày là khó đến beat (xem Serre $[163]$, Chương IV). Nhận xét sau đây là một của then chốt ingredients trong chứng minh của Định lý 29.45.

> **Mệnh đề 29.44.** Cho trước hữu hạn chiều không gian $E$ được trang bị $\epsilon$ -Hermitan tạo thành $\phi$, nếu $U_{1}$ và $U_{2}$ là hai các không gian con của $E$ sao cho $U_{1} \cap U_{2} = (0)$ và nếu ta có mêtric các ánh xạ tuyến tính (linear maps) $f_{1}$: $U_{1} \to E$ và $f_{2}$: $U_{2} \to E$ sao cho
$$\phi (f_{1}(u_{1}), f_{2}(u_{2})) = \phi (u_{1}, u_{2})for u_{i} \in U_{i} (i = 1, 2),(*)$$
Thì ánh xạ tuyến tính (linear map) $f$: $U_{1} \oplus U_{2} \to E$ cho trước bởi $f(u_{1} + u_{2}) = f_{1}(u_{1}) + f_{2}(u_{2})$ mở rộng $f_{1}$ và $f_{2}$ và là mêtric. Hơn nữa, nếu $f_{1}$ và $f_{2}$ là đơn ánh (injective), thì do đó nếu $f$.

*Chứng minh.* Thật vậy, vì $f_{1}$ và $f_{2}$ là mêtric và bằng cách sử dụng (*), ta có $\phi (f_{1}(u_{1}) + f_{2}(u_{2}), f_{1}(v_{1}) + f_{2}(v_{2})) = \phi (f_{1}(u_{1}), f_{1}(v_{1})) + \phi (f_{1}(u_{1}), f_{2}(v_{2}))$
$$+ \phi (f_{2}(u_{2}), f_{1}(v_{1})) + \phi (f_{2}(u_{2}), f_{2}(v_{2}))$$
$$= \phi (u_{1}, v_{1}) + \phi (u_{1}, v_{2}) + \phi (u_{2}, v_{1}) + \phi (u_{2}, v_{2})$$
$$= \phi (u_{1} + u_{2}, v_{2} + v_{2}).$$
Do đó $f$ là mêtric ánh xạ mở rộng $f_{1}$ và $f_{2}$.

> **Định lý 29.45.** (Witt, $1936)$ Cho $E$ và E' là hai hữu hạn chiều các không gian respectively được trang bị hai không suy biến $\epsilon$ -Hermitan các dạng $\phi$ và $\phi'$ thỏa mãn điều kiện $(T)$, và giả sử rằng có một phép đẳng cự (isometry) giữa $(E, \phi$) và (E', $\phi'$). Với mọi không gian con $U$ của $E$, mọi đơn ánh (injective) mêtric ánh xạ tuyến tính (linear map) $f$ từ $U$ vào E' mở rộng đến phép đẳng cự (isometry) từ $E$ đến E'.

*Chứng minh.* Vì $(E, \phi$) và (E', $\phi'$) là isometric, ta có thể giả sử rằng E' $= E$ và $\phi' = \phi$ (nếu $h: E \to$ E' là phép đẳng cự (isometry), thì $h^{-1}\circ f$ là đơn ánh (injective) mêtric ánh xạ từ $U$ vào $E$. chi tiết là trái đến độc giả). $\overline{1}\overline{Curiously$, một số references đến Witt’s paper khẳng định của nó date của publication là $1936$, nhưng những cái khác nói $1937.}$ câu trả lời đến điều này mystery là rằng Thể tích $176$ của Crelle Journal đã là published trong bốn các vấn đề. phủ trang của thể tích $176$ mentions year $1937$, nhưng Witt’s paper là dated Có thể $1936$. Điều này là không chỉ paper của Witt xuất hiện trong điều này thể tích!

<!-- PAGE 1060 -->
Ta tiến hành bằng quy nạp theo số chiều $r$ của $U$. Vì chứng minh là khá intricate, ta spell ra tổng quát plan của attack. Cho quy nạp bước, ta thứ nhất chỉ ra rằng ta có thể rút gọn tình huống đến những gì ta gọi Trường hợp $(H)$, cụ thể là rằng không gian con của $U$ trái cố định bởi $f$ là siêu phẳng (hyperplane) $H$ trong $U$. Thì, tập hợp $D = {f(u)$ - $u$ | $u \in U}$ là đường thẳng trong $U$ và hóa ra là $D^{\perp}$ là siêu phẳng (hyperplane) trong $E$. Ta bây giờ giới thiệu Giả thiết $(V)$, mà nói rằng ta có thể tìm không tầm thường không gian con $V$ của $E$ trực giao đến $D$ và sao cho $V \cap U = V \cap$ f(U) $= (0)$. Ta chỉ ra rằng nếu Giả thiết $(V)$ nghiệm đúng, thì $f$ có thể được được mở rộng đến phép đẳng cự (isometry) của $U \oplus V$. Nó là thì khả dĩ/có thể đến further mở rộng $f$ đến phép đẳng cự (isometry) của $E$. để chứng minh rằng Giả thiết $(V)$ nghiệm đúng ta xét hai các trường hợp. Trong Trường hợp (), ta thu được một số $V$ sao cho $E = U \oplus V$ và ta được thực hiện. Trong Trường hợp $(b)$, ta thu được một số $V$ sao cho $D^{\perp} = U \oplus V$. Ta là thì rút gọn đến tình huống ở đâu $U = D^{\perp}$ là siêu phẳng (hyperplane) trong $E$ và $f$ là phép đẳng cự (isometry) của $U$. Đến hoàn tất chứng minh ta chọn bất kỳ $v \in / U$, sao cho $E = U \oplus$ Kv, và ta tìm một số $v_{1} \in E$ sao cho
$$\phi (f(u), v_{1}) = \phi (u, v)for all u \in U$$
$$\phi (v_{1}, v_{1}) = \phi (v, v).$$
Thì, theo Mệnh đề 29.44, ta có thể mở rộng $f$ đến mêtric ánh xạ $g$ của $U +$ Kv $= E$ sao cho g(v) $= v_{1}$. lập luận được sử dụng để tìm $v_{1}$ làm cho sử dụng của $(\dagger$) (xem ở dưới) và là bit khó/tinh tế. Ta cũng làm cho sử dụng của Tính chất $(T)$ trong tạo thành của Bổ đề 29.28. Ta bây giờ đi quay lại đến chứng minh. trường hợp $r = 0$ là tầm thường. Cho quy nạp bước, $r \ge 1$ do đó $U \neq  (0)$, và cho $H$ là bất kỳ siêu phẳng (hyperplane) trong $U$. Cho $f$: $U \to E$ là đơn ánh (injective) mêtric ánh xạ tuyến tính (linear map). Theo giả thiết quy nạp, thu hẹp $f_{0}$ của $f$ đến $H$ mở rộng đến phép đẳng cự (isometry) $g_{0}$ của $E$. Nếu $g_{0}$ mở rộng $f$, ta được thực hiện. Ngược lại, $H$ là không gian con của các phần tử của $U$ trái cố định bởi $g_{0}^{-1} \circ f$. Nếu định lý nghiệm đúng trong tình huống này, cụ thể là không gian con của $U$ trái cố định bởi $g_{0}^{-1} \circ f$ là siêu phẳng (hyperplane) $H$ trong $U$, thì ta có phép đẳng cự (isometry) $g_{1}$ của $E$ mở rộng $g_{0}^{-1} \circ f$, và $g_{0} \circ g_{1}$ là phép đẳng cự (isometry) của $E$ mở rộng $f$. Vì vậy, ta là rút gọn đến sau đây tình huống: Trường hợp $(H)$. không gian con của $U$ trái cố định bởi $f$ là siêu phẳng (hyperplane) $H$ trong $U$. Trong trường hợp này, tập hợp $D = {f(u)$ - $u$ | $u \in U}$ là đường thẳng trong $U$ (một chiều không gian con). Với mọi $u, v \in U$, ta có $\phi$ (f(u), f(v) - $v) = \phi$ (f(u), f(v)) - $\phi$ (f(u), $v) = \phi (u, v)$ - $\phi$ (f(u), $v) = \phi (u$ - f(u), $v)$, nghĩa là
$$\phi (f(u), f(v) -v) = \phi (u -f(u), v)for all u, v \in U,(**)$$
Và nếu $u \in H$, mà có nghĩa là f(u) $= u$, ta thu được $u \in D^{\perp}$. Vì vậy, $H \subseteq D^{\perp}$. Vì $\phi$ là không suy biến, ta có dim(D) $+ dim(D^{\perp}) =$ dim(E), và vì dim(D) $= 1$, không gian con $D^{\perp}$ là siêu phẳng (hyperplane) trong $E$. Giả thiết $(V)$. Ta có thể tìm không tầm thường không gian con $V$ của $E$ trực giao đến $D$ và sao cho $V \cap U = V \cap$ f(U) $= (0)$. Khẳng định. Giả thiết $(V)$ suy ra rằng $f$ có thể được được mở rộng đến phép đẳng cự (isometry) của $U \oplus V$.

<!-- PAGE 1061 -->
Chứng minh của Khẳng định. Nếu Giả thiết $(V)$ nghiệm đúng, thì ta có
$$\phi (f(u), v) = \phi (u, v)for all u \in U and all v \in V ,$$
Vì $\phi$ (f(u), $v)$ - $\phi (u, v) = \phi$ (f(u) - $u, v) = 0$, với f(u) - $u \in D$ và $v \in V$ trực giao đến $D$. Theo Mệnh đề 29.44 với $f_{1} = f$ và $f_{2}$ inclusion của $V$ vào $E$, ta có thể mở rộng $f$ đến đơn ánh (injective) mêtric ánh xạ trên $U \oplus V$ để lại tất cả các vectơ trong $V$ cố định. Trong trường hợp này, tập hợp ${f(w)$ - $w$ | $w \in U \oplus V$ } là vẫn đường thẳng $D$. Ta chỉ ra ở dưới rằng sự kiện rằng $f$ có thể được được mở rộng đến $U \oplus V$ suy ra rằng $f$ có thể được được mở rộng đến toàn bộ của $E$. Có hai các trường hợp. Trong Trường hợp (), $E = U \oplus V$ và ta được thực hiện. Trong trường hợp $(b), D^{\perp} = U \oplus V$ ở đâu $D^{\perp}$ là siêu phẳng (hyperplane) trong $E$ và $f$ là phép đẳng cự (isometry) của $D^{\perp}$. Bởi tinh tế lập luận, ta sẽ chỉ ra rằng $f$ có thể được được mở rộng đến phép đẳng cự (isometry) của $E$. Ta là rút gọn đến chứng minh rằng không gian con $V$ như ở trên tồn tại. Ta distinguish giữa hai các trường hợp. Trường hợp (). U̸ $\subseteq D^{\perp}$. Chứng minh của Trường hợp (). Trong trường hợp này, công thức (**) chỉ ra rằng f(U) là không được chứa trong $D^{\perp}$ (kiểm tra điều này!). Hệ quả là,
$$U \cap D^{\perp}= f(U) \cap D^{\perp}= H.$$
Ta có thể chọn $V$ là bất kỳ supplement của $H$ trong $D^{\perp}$, và ở trên công thức chỉ ra rằng $V \cap U = V \cap$ f(U) $= (0)$. Vì $U \oplus V$ chứa siêu phẳng (hyperplane) $D^{\perp}$ (vì $D^{\perp} = H \oplus V$ và $H \subseteq U)$, và $U \oplus$ V̸ $= D^{\perp}$ (vì $U$ là không được chứa trong $D^{\perp}$ và $V \subseteq D^{\perp})$, ta phải có $E = U \oplus V$, và như ta đã chỉ ra hệ quả là của giả thiết $(V), f$ có thể được được mở rộng đến phép đẳng cự (isometry) của $U \oplus V = E$. Trường hợp $(b). U \subseteq D^{\perp}$. Chứng minh của Trường hợp $(b)$. Trong trường hợp này, công thức (**) chỉ ra rằng f(U) $\subseteq D^{\perp}$ do đó $U +f(U) \subseteq D^{\perp}$, và vì $D = {f(u)$ - $u$ | $u \in U}$, ta có $D \subseteq D^{\perp}$; nghĩa là, đường thẳng $D$ là đẳng hướng. Ta chỉ ra rằng tồn tại một không gian con $V$ của $D^{\perp}$, sao cho
$$D^{\perp}= U \oplus V = f(U) \oplus V.$$
Do đó, trường hợp $(b)$ chỉ ra rằng ta là rút gọn đến tình huống ở đâu $U = D^{\perp}$ và $f$ là phép đẳng cự (isometry) của $U$. Nếu $U =$ f(U) ta chọn $V$ là supplement của $U$ trong $D^{\perp}$. Ngược lại, cho $x \in U$ với $x \in / H$, và cho $y \in$ f(U) với $y \in / H$. Vì f(H) $= H$ (từng điểm), $f$ là đơn ánh (injective), và $H$ là siêu phẳng (hyperplane) trong $U$, ta có
$$U = H \oplus Kx,f(U) = H \oplus Ky.$$

<!-- PAGE 1062 -->
Ta khẳng định rằng $x + y \in / U$. Ngược lại, vì $y = x + y$ - $x$, với $x + y, x \in U$ và vì $y \in$ f(U), ta sẽ có $y \in U \cap$ f(U) $= H$, một mâu thuẫn. Tương tự, $x + y \in /$ f(U). Suy ra rằng
$$U + f(U) = U \oplus K(x + y) = f(U) \oplus K(x + y).$$
Bây giờ, chọn $W$ là bất kỳ supplement của $U +$ f(U) trong $D^{\perp}$ sao cho $D^{\perp} = (U +$ f(U)) $\oplus W$, và cho
$$V = K(x + y) + W.$$
Thì, vì $x \in U, y \in$ f(U), $W \subseteq D^{\perp}$, và $U +$ f(U) $\subseteq D^{\perp}$, ta có $V \subseteq D^{\perp}$. Ta cũng có
$$U \oplus V = U \oplus K(x + y) \oplus W = (U + f(U)) \oplus W = D^{\perp}$$
Và
$$f(U) \oplus V = f(U) \oplus K(x + y) \oplus W = (U + f(U)) \oplus W = D^{\perp},$$
Do đó như ta đã chỉ ra hệ quả là của giả thiết $(V), f$ có thể được được mở rộng đến phép đẳng cự (isometry) của siêu phẳng (hyperplane) $D^{\perp} = U \oplus V$, và $D$ là vẫn đường thẳng ${f(w)$ - $w$ | $w \in U \oplus V$ }. lập luận trong chứng minh của Trường hợp $(b)$ chỉ ra rằng ta là rút gọn đến tình huống ở đâu $U = D^{\perp}$ là siêu phẳng (hyperplane) trong $E$ và $f$ là phép đẳng cự (isometry) của $U$. Nếu ta chọn bất kỳ $v \in / U$, thì $E = U \oplus$ Kv, do đó giả sử ta có thể tìm một số $v_{1} \in E$ sao cho
$$\phi (f(u), v_{1}) = \phi (u, v)for all u \in U$$
$$\phi (v_{1}, v_{1}) = \phi (v, v).$$
Điều kiện thứ nhất là điều kiện (*) của Mệnh đề 29.44, và điều kiện thứ hai khẳng định rằng ánh xạ $\lambda v \mapsto \lambda v_{2}$ từ đường thẳng Kv đến đường thẳng $Kv_{1}$ là mêtric ánh xạ. Thì, theo Mệnh đề 29.44, ta có thể mở rộng $f$ đến mêtric ánh xạ $g$ của $U +$ Kv $= E$ sao cho g(v) $= v_{1}$. để tìm $v_{1}$, cho chúng ta chứng minh rằng với mọi $v \in E$, tồn tại một v' $\in E$ sao cho
$$\phi (f(u), v') = \phi (u, v)for all u \in U.(\dagger )$$
Điều này là bởi vì dạng tuyến tính (linear form) $u \mapsto \phi (f^{-1} (u), v) (u \in U)$ là thu hẹp của dạng tuyến tính (linear form) $\psi  \in E^{*}$, và vì $\phi$ là không suy biến, tồn tại một (duy nhất) v' $\in E$, sao cho
$$\psi (x) = \phi (x, v')for all x \in E,$$
Mà suy ra rằng
$$\phi (u, v') = \phi (f^{-1} (u), v)for all u \in U,$$
Và vì $f$ là tự đẳng cấu của $U$, rằng $(\dagger$) nghiệm đúng. Hơn nữa, nhận thấy rằng công thức $(\dagger$) vẫn nghiệm đúng nếu ta cộng đến v' bất kỳ vectơ $y$ trong $D$, vì f(U) $= U = D^{\perp}$. Vì vậy, với mọi $v_{1} =$ v' $+ y$ với $y \in D$, nếu ta mở rộng $f$ đến ánh xạ tuyến tính (linear map) của $E$ bằng cách đặt g(v) $= v_{1}$, thì bởi $(\dagger$) ta có
$$\phi (g(u), g(v)) = \phi (u, v)for all u \in U.$$

<!-- PAGE 1063 -->
Ta vẫn cần đến chọn $y \in D$ sao cho $v_{1} =$ v' $+ y$ thỏa mãn $\phi (v_{1}, v_{1}) = \phi (v, v)$. Tuy nhiên, vì $v \in / U = D^{\perp}$, vectơ $v$ là không trực giao $D$, và theo Bổ đề 29.28, tồn tại một $y_{0} \in D$ sao cho
$$\phi (v'+ y_{0}, v'+ y_{0}) = \phi (v, v).$$
Thì, nếu ta cho $v_{1} =$ v' $+ y_{0}$, theo Mệnh đề 29.44, ta có thể mở rộng $f$ đến mêtric ánh xạ $g$ của $U +$ Kv $= E$ bằng cách đặt g(v) $= v_{1}$. Vì $\phi$ là không suy biến, $g$ là phép đẳng cự (isometry). thứ nhất hệ quả của Witt’s định lý đôi khi được gọi là Witt’s cancellation định lý.

> **Định lý 29.46.** (Witt Cancellation Định lý) Cho $(E_{1}, \phi_{1}$) và $(E_{2}, \phi_{2}$) là hai các cặp của hữu hạn chiều các không gian và không suy biến $\epsilon$ -Hermite các dạng thỏa mãn điều kiện $(T)$, và giả sử rằng $(E_{1}, \phi_{1}$) và $(E_{2}, \phi_{2}$) là isometric. Với mọi không gian con $U$ của $E_{1}$ và bất kỳ không gian con $V$ của $E_{2}$, nếu có một phép đẳng cự (isometry) $f$: $U \to V$, thì có một phép đẳng cự (isometry) $g: U^{\perp} \to V^{\perp}$.

*Chứng minh.* Nếu $f$: $U \to V$ là phép đẳng cự (isometry) giữa $U$ và $V$, bởi Witt’s định lý (Định lý 29.46), ánh xạ tuyến tính (linear map) $f$ mở rộng đến phép đẳng cự (isometry) $g$ giữa $E_{1}$ và $E_{2}$. Ta khẳng định rằng $g$ các ánh xạ $U^{\perp}$ vào $V^{\perp}$. Điều này là bởi vì nếu $v \in U^{\perp}$, ta có $\phi_{1} (u, v) = 0$ với mọi $u \in U$, do đó
$$\phi_{2} (g(u), g(v)) = \phi_{1} (u, v) = 0for all u \in U,$$
Và vì $g$ là song ánh giữa $U$ và $V$, ta có g(U) $= V$, do đó ta xem rằng g(v) là trực giao đến $V$ với mọi $v \in U^{\perp}$; rằng là, $g(U^{\perp}$) $\subseteq V^{\perp}$. Vì $g$ là mêtric ánh xạ và vì $\phi_{1}$ là không suy biến, thu hẹp của $g$ đến $U^{\perp}$ là phép đẳng cự (isometry) từ $U^{\perp}$ đến $V^{\perp}$. cặp $(E, \phi$) ở đâu $E$ là hữu hạn chiều và $\phi$ là không suy biến $\epsilon$ -Hermite tạo thành là thường được gọi là $\epsilon$ -Không gian Hermite (Hermitian space). Khi $\epsilon  = 1$ và $\phi$ là đối xứng, ta sử dụng số hạng
$$Euclidean space or quadratic space. When \epsilon  = -1 and \phi \frac{is}{\lambda} alternating, we use the term$$
Symplectic không gian. Khi $\epsilon  = 1$ và tự đẳng cấu $\lambda  \mapsto$ là không đồng nhất thức ta sử dụng số hạng Không gian Hermite (Hermitian space), và khi $\epsilon  = -1$, ta sử dụng số hạng skew-Không gian Hermite (Hermitian space). Ta cũng có kết quả sau đây chỉ ra rằng nhóm của các phép đẳng cự của $\epsilon$ -Không gian Hermite (Hermitian space) là transitive trên một cách tổng đẳng hướng các không gian con của cùng số chiều.

> **Định lý 29.47.** Cho $E$ là không gian vectơ hữu hạn chiều và cho $\phi$ là không suy biến $\epsilon$ -Hermite tạo thành trên $E$ thỏa mãn điều kiện $(T)$. Thì với mọi hai một cách tổng đẳng hướng các không gian con $U$ và $V$ của cùng số chiều, có một phép đẳng cự (isometry) $f \in Isom(\phi$) sao cho f(U) $= V$. Hơn nữa, mọi tuyến tính tự đẳng cấu của $U$ được cảm sinh bởi phép đẳng cự (isometry) của $E$.
Nhận xét: Witt’s cancelation định lý có thể được được sử dụng để định nghĩa quan hệ tương đương (equivalence relation) trên $\epsilon$ - Các không gian Hermite và để định nghĩa nhóm cấu trúc trên các phần tử này các lớp tương đương. Điều này cách, ta thu được Witt nhóm, nhưng ta sẽ không thảo luận nó ở đây. Witt’s Định lý có thể được sharpened đến các phép đẳng cự trong $SO(\phi$), nhưng một số điều kiện trên $U$ là cần thiết.

<!-- PAGE 1064 -->

> **Định lý 29.48.** (Witt–Sharpened Phiên bản) Cho $E$ là hữu hạn chiều không gian được trang bị không suy biến đối xứng các dạng song tuyến tính $\phi$. Với mọi không gian con $U$ của $E$, mọi tuyến tính đơn ánh (injective) mêtric ánh xạ $f$ từ $U$ vào $E$ mở rộng đến phép đẳng cự (isometry) $g$ của $E$ với prescribed giá trị $\pm 1$ của det(g) khi và chỉ khi
$$\dim(U) + \dim(rad(U)) < \dim(E) = n.$$
Nếu
$$\dim(U) + \dim(rad(U)) = \dim(E) = n,$$
Và det(f) $= -1$, thì không có $g \in SO(\phi$) mở rộng $f$.

*Chứng minh.* Nếu $g_{1}$ và $g_{2}$ là hai các mở rộng của $f$ sao cho $det(g_{1}) det(g_{2}) = -1$, thì $h = g_{1}^{-1} \circ g_{2}$ là phép đẳng cự (isometry) sao cho det(h) $= -1$, và $h$ để lại mọi vectơ của $U$ cố định. Ngược lại, nếu $h$ là phép đẳng cự (isometry) sao cho det(h) $= -1$, và h(u) $= u$ với mọi $u \in U$, thì với mọi extesnion $g_{1}$ của $f$, ánh xạ $g_{2} = h \circ g_{1}$ là một cái khác mở rộng của $f$ sao cho $det(g_{2}) = -det(g_{1})$. Vì vậy, ta cần để chỉ ra rằng ánh xạ $h$ như ở trên tồn tại.
$$If \dim(U)+\dim(rad(U)) < \dim(E), consider the nondegenerate completion\overline{U} of U \frac{given}{U}$$
Theo Mệnh đề 29.32. Ta biết rằng $dim(\overline{U}) =$ dim(U) $+$ dim(rad(U)) $< n$, và vì là không suy biến, ta có
$$E =\overline{U}^{\perp}\oplus \overline{U}^{\perp},$$
$$̸$$
$$with \overline{U}^{\perp}= (0). Pick any isometry \frac{\tau}{U} of \overline{U}^{\perp}such that \det(\tau ) = -1, and extend it to an$$
Phép đẳng cự (isometry) $h$ của $E$ có thu hẹp đến là đồng nhất thức. Nếu dim(U) $+$ dim(rad(U)) $=$ dim(E) $= n$, thì $U = V^{\perp}\oplus W$ với $V =$ rad(U) và vì $dim(\overline{U}) =$ dim(U) $+$ dim(rad(U)) $= n$, ta có
$$E =\overline{U} = (V \oplus V' )^{\perp}\oplus W,$$
Ở đâu $V \oplus$ V' $= Ar_{2r} = W^{\perp}$ là Artinian không gian. Bất kỳ phép đẳng cự (isometry) $h$ của $E$ mà là đồng nhất thức trên $U$ và với det(h) $= -1$ là đồng nhất thức trên $W$, và do đó nó phải ánh xạ $W^{\perp} = Ar_{2r} = V \oplus$ V' vào chính nó, và thu hẹp h' của $h$ đến $Ar_{2r}$ có det(h') $= -1$. Tuy nhiên, h' là đồng nhất thức trên $V =$ rad(U), một cách tổng đẳng hướng không gian con của $Ar_{2r}$ có số chiều $r$, và theo Mệnh đề 29.42, ta có det(h') $= +1$, một mâu thuẫn. Nó có thể được được hiển thị rằng tâm của $O(\phi$) là ${id, -id}$. Cho further các tính chất của trực giao các nhóm, xem Grove $[86]$, Jacobson $[101]$, Taylor $[180]$, và Artin $[6]$.
