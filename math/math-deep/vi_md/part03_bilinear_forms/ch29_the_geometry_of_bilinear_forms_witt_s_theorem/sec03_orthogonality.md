# Tính trực giao


<!-- PAGE 1023 -->
Mệnh đề 29.5 cũng nghiệm đúng cho các dạng nửa tuyến tính và ma trận của chúng các biểu diễn. Nhận thấy rằng nếu $\phi$ là Hermite tạo thành $(E = F)$ và nếu $K$ thực hiện không có characteristic $2$, thì theo Định lý 29.10, có một cơ sở (basis) của $E$ đối với mà ma trận $M$ biểu diễn $\phi$ là ma trận đường chéo (diagonal matrix). Nếu $K = \mathbb{C}$, thì các phần tử (các phần tử (entries)) này là thực, và điều này cho phép chúng ta đến phân loại hoàn toàn Hermite các dạng.

> **Mệnh đề 29.11.** Cho trước bất kỳ Hermite tạo thành $\phi$: $E \times  E \to \mathbb{C}$ với dim(E) $= n$, có một cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $E$ sao cho
$$\Phi \begin{pmatrix} x_{i}e_{i} \end{pmatrix} \sum_{i=1}^{n}  = \sum_{i=1}^{p}  x_{i}^{2} - \sum_{i=p+1}^{p+q}  x_{i}^{2} ,$$
Với $0 \le p, q$ và $p + q \le n$. chứng minh của Mệnh đề 29.11 là cùng như thực trường hợp của Mệnh đề 29.6. Sylvester’s inertia luật (Mệnh đề 29.7) cũng nghiệm đúng cho Hermite các dạng: $p$ và $q$ chỉ phụ thuộc vào $\phi$.

## 29.3 Tính trực giao

Trong mục này ta giả sử rằng ta là dealing với dạng nửa tuyến tính (sesquilinear form) $\phi$: $E \times  F \to K$. Ta cho phép tự đẳng cấu $\lambda  \mapsto \overline{\lambda}$ là đồng nhất thức, trong mà trường hợp $\phi$ là dạng song tuyến tính (bilinear form). Điều này cách, ta có thể deal với các tính chất shared bởi các dạng song tuyến tính và các dạng nửa tuyến tính trong uniform cách thức. Tính trực giao là như vậy tính chất.

> **Định nghĩa 29.12.** Cho trước dạng nửa tuyến tính (sesquilinear form) $\phi$: $E \times F \to K$, ta nói rằng hai các vectơ $u \in E$ và $v \in F$ là trực giao (hoặc liên hợp) nếu $\phi (u, v) = 0$. Hai các tập con E' $\subseteq E$ và F' $\subseteq F$ là trực giao nếu $\phi (u, v) = 0$ với mọi $u \in$ E' và tất cả $v \in$ F'. Cho trước không gian con $U$ của $E$, phải trực giao không gian của $U$, được ký hiệu $U^{\perp}$, là không gian con của $F$ cho trước bởi
$$U^{\perp} = {v \in F | \phi (u, v) = 0for all u \in U},$$
Và cho trước không gian con $V$ của $F$, trái trực giao không gian của $V$, được ký hiệu $V^{\perp}$, là không gian con của $E$ cho trước bởi
$$V^{\perp} = {u \in E | \phi (u, v) = 0for all v \in V }.$$
Khi $E$ và $F$ là phân biệt, ở đó là little chance của confusing phải trực giao không gian con $U^{\perp}$ của không gian con $U$ của $E$ và trái trực giao không gian con $V^{\perp}$ của không gian con $V$ của $F$. Tuy nhiên, nếu $E = F$, thì $\phi (u, v) = 0$ thực hiện không nhất thiết suy ra rằng $\phi (v, u) = 0$, nghĩa là, tính trực giao là không nhất thiết đối xứng. Do đó, nếu cả hai $U$ và $V$ là các tập con của $E$, có một notational ambiguity nếu $U = V$. Trong trường hợp này, ta có thể viết $U^{\perp r}$ cho phải trực giao và $U^{\perp l}$ cho trái trực giao. ở trên thảo luận brings lên sau đây điểm: Khi là tính trực giao đối xứng?

<!-- PAGE 1024 -->
Nếu $\phi$ là song tuyến tính, nó được hiển thị trong $E$. Artin $[6]$ (và trong Jacobson $[101])$ rằng tính trực giao là đối xứng khi và chỉ khi hoặc $\phi$ là đối xứng hoặc $\phi$ là thay phiên $(\phi (u, u) = 0$ với mọi $u \in E)$. Nếu $\phi$ là nửa tuyến tính (sesquilinear), câu trả lời là nhiều hơn/thêm phức tạp. Ngoài trước đó hai các trường hợp, có một thứ ba khả năng:
$$\phi (u, v) =\overline{\epsilon \phi}\overline{(}\overline{v, u}\overline{)} for all u, v \in E,$$
Ở đâu $\epsilon$ là một số khác không phần tử trong $K$. Ta nói rằng $\phi$ là $\epsilon$ -Hermite. Nhận thấy rằng
$$\phi (u, u) =\overline{\epsilon \epsilon \phi}(u, u),$$
Do đó nếu $\phi$ là không thay phiên, thì $\phi (u, u) \neq  0$ với một số $u$, và ta phải có $\overline{\epsilon \epsilon} = 1$. hầu hết chung/phổ biến các trường hợp là $1. \epsilon  = 1$, trong mà trường hợp $\phi$ là Hermite, và $2. \epsilon  = -1$, trong mà trường hợp $\phi$ là skew-Hermitian. Nếu $\phi$ là thay phiên và $K$ là không của characteristic $2$, thì phương trình (*) từ Mục 29.2 suy ra rằng tự đẳng cấu $\lambda  \mapsto \overline{\lambda}$ phải là đồng nhất thức nếu $\phi$ là khác không. Nếu do đó, $\phi$ là phản đối xứng, do đó $\epsilon  = -1$. Trong tóm tắt, nếu $\phi$ là hoặc đối xứng, thay phiên, hoặc $\epsilon$ -Hermite, thì tính trực giao là đối xứng, và nó làm cho nghĩa đến talk về trực giao không gian con $U^{\perp}$ của $U$. Nhận thấy rằng nếu $\phi$ là $\epsilon$ -Hermite, thì
$$r_{\phi} = \epsilon l_{\phi}.$$
Điều này là bởi vì
$$l_{\phi}(u)(y) =\overline{\phi}\overline{(}\overline{u, y}\overline{)}$$
$$r_{\phi}(u)(y) = \phi (y, u)$$
$$=\overline{\epsilon \phi}\overline{(}\overline{u, y}\overline{)},$$
Do đó $r_{\phi} = \epsilon l_{\phi}$. Nếu $E$ và $F$ là hữu hạn chiều với các cơ sở $(e_{1}, \dots  , e_{m})$ và $(f_{1}, \dots  , f_{n})$, và nếu $\phi$ được biểu diễn bởi ma trận cỡ $n \times  m$ $M$, thì $\phi$ là $\epsilon$ -Hermite khi và chỉ khi
$$M = \epsilon M^{*} ,$$
Ở đâu $M^{*} = (\overline{M})^{\top}$ (như thông thường). Điều này captures sau đây các loại của quen thuộc các ma trận: $1$. Các ma trận đối xứng $(\epsilon  = 1) 2$. Các ma trận phản đối xứng $(\epsilon  = -1)$

<!-- PAGE 1025 -->
$3$. Các ma trận Hermite $(\epsilon  = 1) 4$. Skew-Các ma trận Hermite $(\epsilon  = -1)$. Đi quay lại đến dạng nửa tuyến tính (sesquilinear form) $\phi$: $E \times  F \to K$, với mọi không gian con $U$ của $E$, nó là dễ để kiểm tra rằng
$$U \subseteq (U^{\perp} )^{\perp},$$
Và rằng với mọi không gian con $V$ của $F$, ta có
$$V \subseteq (V^{\perp} )^{\perp}.$$
Để đơn giản của ký hiệu, ta viết $U^{\perp \perp}$ thay vì của $(U^{\perp} )^{\perp}$ (và $V^{\perp \perp}$ thay vì của $(V^{\perp} )^{\perp})$. Cho trước bất kỳ hai các không gian con $U_{1}$ và $U_{2}$ của $E$, nếu $U_{1} \subseteq U_{2}$, thì $U_{2}^{\perp}  \subseteq U_{1}^{\perp}$. Thật vậy, nếu $v \in U_{2}^{\perp}$ thì $\phi (u_{2}, v) = 0$ với mọi $u_{2} \in U_{2}$, và vì $U_{1} \subseteq U_{2}$ điều này suy ra rằng $\phi (u_{1}, v) = 0$ với mọi $u_{1} \in U_{1}$, mà chỉ ra rằng $v \in U_{1}^{\perp}$. Tương tự với mọi hai các không gian con $V_{1}, V_{2}$ của $F$, nếu $V_{1} \subseteq V_{2}$, thì $V_{2}^{\perp}  \subseteq V_{1}^{\perp}$. Hệ quả là,
$$U^{\perp} = U^{\perp \perp \perp} ,V^{\perp} = V^{\perp \perp \perp} .$$
Thứ nhất, ta có $U^{\perp} \subseteq U^{\perp \perp \perp}$. Thứ hai, từ $U \subseteq U^{\perp \perp}$, ta thu được $U^{\perp \perp \perp} \subseteq U^{\perp}$, do đó $U^{\perp} = U^{\perp \perp \perp}$. khác phương trình được chứng minh là đồng dạng cách. Nhận thấy rằng $\phi$ là không suy biến khi và chỉ khi $E^{\perp} = {0}$ và $F^{\perp} = {0}$. Hơn nữa, vì
$$\phi (u + x, v) = \phi (u, v)$$
$$\phi (u, v + y) = \phi (u, v)$$
Với mọi $x \in F^{\perp}$ và bất kỳ $y \in E^{\perp}$, ta xem rằng ta thu được bởi chuyển đến thương dạng nửa tuyến tính (sesquilinear form)
$$[\phi ]: (E/F^{\perp} ) \times  (F/E^{\perp}) \to K$$
Mà là không suy biến.

> **Mệnh đề 29.12.** Với mọi dạng nửa tuyến tính (sesquilinear form) $\phi$: $E \times  F \to K$, không gian $E/F^{\perp}$ là hữu hạn chiều khi và chỉ khi không gian $F/E^{\perp}$ là hữu hạn chiều; nếu do đó, $dim(E/F^{\perp}$) $= dim(F/E^{\perp})$.
$$Proof. \frac{Since}{(E/F^{\perp})} the sesquilinear form [\phi \frac{]:(E/F^{\perp}}{(F/E^{\perp})} ) \times  (F/E^{\perp}) \to K is nondegenerate, the maps$$
$l_{[\phi]}$: $\to (F/E^{\perp})^{*}$ và $r_{[\phi]}$: $\to (E/F^{\perp} )^{*}$ là đơn ánh (injective). Nếu $dim(E/F^{\perp}$) $=$
$$m, \frac{thendim(}{F/E^{\perp}))} E/F^{\perp} ) = \dim((E/F^{\perp} )^{*}), so by injectivity of r_{[\phi]}, we have \dim(F/E^{\perp}) =$$
$$\dim(( \le m. \frac{A similar reasoning using the injectivity of}{E/F^{\perp}))} l_{[\phi]} applies if \dim(F/E^{\perp}) = n,$$
Và ta thu được $dim(E/F^{\perp}$) $=$ dim(($\le n$. Vì vậy, $dim(E/F^{\perp}$) $= m$ là hữu hạn khi và chỉ khi $dim(F/E^{\perp}) = n$ là hữu hạn, trong mà trường hợp $m = n$ theo Mệnh đề 29.1(d).

<!-- PAGE 1026 -->
Nếu $U$ là không gian con của không gian $E$, nhắc lại rằng đối chiều (codimension) của $U$ là số chiều của $E/U$, mà là cũng bằng số chiều của bất kỳ không gian con $V$ sao cho $E$ là tổng trực tiếp (direct sum) của $U$ và $V (E = U \oplus V$). Mệnh đề 29.12 suy ra sau đây hữu ích sự kiện.

> **Mệnh đề 29.13.** Cho $\phi$: $E\times F \to K$ là bất kỳ không suy biến dạng nửa tuyến tính (sesquilinear form). không gian con $U$ của $E$ có hữu hạn số chiều khi và chỉ khi $U^{\perp}$ có hữu hạn đối chiều (codimension) trong $F$. Nếu dim(U) là hữu hạn, thì $codim(U^{\perp}$) $=$ dim(U), và $U^{\perp \perp} = U$.

*Chứng minh.* Vì $\phi$ là không suy biến $E^{\perp} = {0}$ và $F^{\perp} = {0}$, do đó Mệnh đề 29.12 ứng dụng đến thu hẹp của $\phi$ đến $U \times  F$ suy ra rằng không gian con $U$ của $E$ có hữu hạn số chiều khi và chỉ khi $U^{\perp}$ có hữu hạn đối chiều (codimension) trong $F$, và rằng nếu dim(U) là hữu hạn, thì $codim(U^{\perp}$) $=$ dim(U). Vì $U^{\perp}$ và $U^{\perp \perp}$ là trực giao, và vì $codim(U^{\perp}$) là hữu hạn, $dim(U^{\perp \perp}$) là hữu hạn và ta có $dim(U^{\perp \perp}$) $= codim(U^{\perp \perp \perp}$) $= codim(U^{\perp}$) $=$ dim(U). Vì $U \subseteq U^{\perp \perp}$, ta phải có $U = U^{\perp \perp}$.

> **Mệnh đề 29.14.** Cho $\phi$: $E \times F \to K$ là bất kỳ dạng nửa tuyến tính (sesquilinear form). Cho trước bất kỳ hai các không gian con $U$ và $V$ của $E$, ta có
$$(U + V )^{\perp}= U^{\perp} \cap V^{\perp} .$$
Hơn nữa, nếu $\phi$ là không suy biến và nếu $U$ và $V$ là hữu hạn chiều, thì
$$(U \cap V )^{\perp}= U^{\perp} + V^{\perp} .$$

*Chứng minh.* Nếu $w \in (U + V )^{\perp}$, thì $\phi (u + v, w) = 0$ với mọi $u \in U$ và tất cả $v \in V$. Đặc biệt, với $v = 0$, ta có $\phi (u, w) = 0$ với mọi $u \in U$, và với $u = 0$, ta có $\phi (v, w) = 0$ với mọi $v \in V$, do đó $w \in U^{\perp} \cap V^{\perp}$. Ngược lại, nếu $w \in U^{\perp} \cap V^{\perp}$, thì $\phi (u, w) = 0$ với mọi $u \in U$ và $\phi (v, w) = 0$ với mọi $v \in V$. Bởi tính song tuyến tính, $\phi (u + v, w) = \phi (u, w) + \phi (v, w) = 0$, mà chỉ ra rằng $w \in (U + V )^{\perp}$. Vì vậy, thứ nhất đồng nhất thức nghiệm đúng. Bây giờ, giả sử rằng $\phi$ là không suy biến và rằng $U$ và $V$ là hữu hạn chiều, và cho $W = U^{\perp} + V^{\perp}$. Bằng cách sử dụng phương trình rằng ta chỉ được thiết lập và sự kiện rằng $U$ và $V$ là hữu hạn chiều, theo Mệnh đề 29.13, ta thu được
$$W^{\perp} = U^{\perp \perp} \cap V^{\perp \perp} = U \cap V.$$
Ta có thể áp dụng Mệnh đề 29.12 đến thu hẹp của $\phi$ đến $U \times  W$ (vì $U^{\perp} \subseteq W$ và $W^{\perp} \subseteq U)$, và ta thu được
$$\dim(U/W^{\perp} ) = \dim(U/(U \cap V )) = \dim(W/U^{\perp} ).$$
Nếu $T$ là supplement của $U^{\perp}$ trong $W$ sao cho $W = U^{\perp} \oplus T$ và nếu $S$ là supplement của $W$ trong $E$ sao cho $E = W \oplus S$, thì codim(W) $=$ dim(S), dim(T) $= dim(W/U^{\perp}$), và ta có tổng trực tiếp (direct sum)
$$E = U^{\perp} \oplus T \oplus S$$

<!-- PAGE 1027 -->
Mà suy ra rằng
$$\dim(T) = codim(U^{\perp} ) -\dim(S) = codim(U^{\perp} ) -codim(W)$$
Do đó
$$\dim(U/(U \cap V )) = \dim(W/U^{\perp} ) = codim(U^{\perp} ) -codim(W),$$
Và vì $codim(U^{\perp}$) $=$ dim(U), ta suy ra rằng
$$\dim(U \cap V ) = codim(W).$$
Tuy nhiên, theo Mệnh đề 29.13, ta có dim(U $\cap V$) $=$ codim((U $\cap V )^{\perp})$, do đó codim(W) $=$ codim((U $\cap V )^{\perp})$, và vì $W \subseteq W^{\perp \perp} = (U \cap V )^{\perp}$, ta phải có $W = (U \cap V )^{\perp}$, như đã khẳng định. Xét theo Mệnh đề 29.12, ta có thể tạo sau đây định nghĩa.

> **Định nghĩa 29.13.** Cho $\phi$: $E \times  F \to K$ là bất kỳ dạng nửa tuyến tính (sesquilinear form). Nếu $E/F^{\perp}$ và $F/E^{\perp}$ là hữu hạn chiều, thì của chúng chung/phổ biến số chiều được gọi là hạng (rank) của tạo thành $\phi$. Nếu $E/F^{\perp}$ và $F/E^{\perp}$ có vô hạn số chiều, ta nói rằng $\phi$ có vô hạn hạng (rank). Không đáng ngạc nhiên là, hạng (rank) của $\phi$ là related đến các hạng (rank) của $l_{\phi}$ và $r_{\phi}$.

> **Mệnh đề 29.15.** Cho $\phi$: $E \times  F \to K$ là bất kỳ dạng nửa tuyến tính (sesquilinear form). Nếu $\phi$ có hữu hạn hạng (rank) $r$, thì $l_{\phi}$ và $r_{\phi}$ có cùng hạng (rank), mà bằng $r$.

*Chứng minh.* Bởi vì với mọi $u \in E$,
$$l_{\phi}(u)(y) =\overline{\phi}\overline{(}\overline{u, y}\overline{)} for all y \in F,$$
Và với mọi $v \in F$,
$$r_{\phi}(v)(x) = \phi (x, v)for all x \in E,$$
Rõ ràng là hạt nhân (kernel) của $l_{\phi}$: $\overline{E} \to F^{*}$ bằng $F^{\perp}$ và rằng, hạt nhân (kernel) của $r_{\phi}$: $\overline{F} \to E^{*}$ bằng $E^{\perp}$. Vì vậy, $rank(l_{\phi}) =$ dim(Im $l_{\phi}) = dim(E/F^{\perp}$) $= r$, và tương tự $rank(r_{\phi}) = dim(F/E^{\perp}) = r$.
Nhận xét: Nếu dạng nửa tuyến tính (sesquilinear form) $\phi$ được biểu diễn bởi ma trận $n \times  m$ ma trận $M$ đối với các cơ sở $(e_{1}, \dots  , e_{m})$ trong $E$ và $(f_{1}, \dots  , f_{n})$ trong $F$, nó có thể được được hiển thị rằng ma trận biểu diễn $l_{\phi}$ đối với các cơ sở $(e_{1}, \dots  , e_{m})$ và $(f_{1}^{*} , \dots  , f_{n}^{*})$ là $\overline{M}$, và rằng ma trận biểu diễn $r_{\phi}$ đối với các cơ sở $(f_{1}, \dots  , f_{n})$ và $(e_{1}^{*}, \dots  , e_{m}^{*})$ là $M^{\top}$. Suy ra rằng hạng (rank) của $\phi$ bằng hạng (rank) của $M$.
