# Tóm tắt


<!-- PAGE 620 -->
Một cái khác cách (do Jean Dieudonn´e) để chứng minh rằng mục $s$ của $\rho$ là không đồng cấu là để chứng minh rằng bất kỳ quaternion đơn vị (unit quaternion) là tích của hai unit thuần túy các quaternion. Thật vậy, nếu $q = [a, u]$ là quaternion đơn vị (unit quaternion), nếu ta cho $q_{1} = [0, u_{1}]$, ở đâu $u_{1}$ là bất kỳ unit vectơ trực giao đến $u$, thì
$$q_{1}q = [-u_{1} \cdot  u, au_{1} + u_{1} \times  u] = [0, au_{1} + u_{1} \times  u] = q_{2}$$
Là khác không unit thuần túy quaternion. Điều này là bởi vì nếu $a \neq  0$ thì $au_{1}+u_{1}\times u \neq  0$ (vì $u_{1}\times u$ là trực giao đến $au_{1} \neq  0)$, và nếu $a = 0$ thì $u \neq  0$, do đó $u_{1} \times  u \neq  0$ (vì $u_{1}$ là trực giao đến $u)$. Nhưng khi đó, $q_{1}^{-1} = [0, -u_{1}]$ là unit thuần túy quaternion và ta có
$$q = q_{1}^{-1} q_{2},$$
Tích của hai thuần túy các quaternion đơn vị. Ta cũng nhận thấy rằng với mọi hai thuần túy các quaternion $q_{1}, q_{2}$, tồn tại một quaternion đơn vị (unit quaternion) $q$ sao cho
$$q_{2} = qq_{1}q^{-1}.$$
Điều này là chỉ restatement của sự kiện rằng nhóm Do đó(3) là transitive. Vì hạt nhân (kernel) của $\rho$: SU(2) $\to$ Do đó(3) là ${I, -I}$, nhóm con s(Do đó(3)) sẽ là nhóm con chuẩn tắc (normal subgroup) của chỉ số $2$ trong SU(2). Thì ta sẽ có toàn ánh (surjective) đồng cấu $\eta$ từ SU(2) lên nhóm thương (quotient group) $SU(2)/s(SO(3))$, mà là đẳng cấu đến ${1, -1}$. Bây giờ, vì bất kỳ hai thuần túy các quaternion là liên hợp của mỗi khác, $\eta$ sẽ có hằng số giá trị trên unit thuần túy các quaternion. Vì $k =$ ij, ta sẽ có
$$\eta (k) = \eta (ij) = (\eta (i))^{2}= 1.$$
Hệ quả là, $\eta$ sẽ ánh xạ tất cả thuần túy các quaternion đơn vị đến $1$. Nhưng vì mọi quaternion đơn vị (unit quaternion) là tích của hai thuần túy các quaternion, $\eta$ sẽ ánh xạ mọi quaternion đơn vị (unit quaternion) đến $1$, contradicting sự kiện rằng nó là toàn ánh (surjective) lên ${-1, 1}$.

## 16.8 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ nhóm SU(2) của các quaternion đơn vị. $\bullet$ skew trường $\mathbb{H}$ của các quaternion. $\bullet$ Hamilton’s các đồng nhất thức. $\bullet$ (thực) không gian vectơ (vector space) $\mathfrak{su}(2)$ của $2 \times  2$ skew Các ma trận Hermite với không vết (trace). $\bullet$ liên hợp (adjoint) biểu diễn của SU(2).
