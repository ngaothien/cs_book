# Symplectic Các nhóm


<!-- PAGE 1048 -->

## 29.8 Symplectic Các nhóm

Trong mục này, ta là dealing với không suy biến thay phiên tạo thành $\phi$ trên không gian vectơ (vector space) $E$ có số chiều $n$. Như ta đã thấy trước đó, $n$ phải là chẵn/ngay cả, nói $n =$ 2m. Theo Định lý 29.24, có một tổng trực tiếp (direct sum) phân rã của $E$ vào đôi một trực giao các không gian con
$$E = W_{1}^{\perp}\oplus \cdots^{\perp} \oplus W_{m},$$
Ở đâu mỗi $W_{i}$ là mặt phẳng hyperbolic (hyperbolic plane). Mỗi $W_{i}$ có cơ sở (basis) $(u_{i}, v_{i})$, với $\phi (u_{i}, u_{i}) = \phi (v_{i}, v_{i}) = 0$ và $\phi (u_{i}, v_{i}) = 1$, cho $i = 1, \dots  , m$. Trong cơ sở (basis)
$$(u_{1}, \dots  , u_{m}, v_{1}, \dots  , v_{m}),$$
$\phi$ được biểu diễn bởi ma trận
$$J_{m,m} = \begin{pmatrix} 0 & I_{m} \\ -I_{m} & 0 \end{pmatrix} .$$
Nhóm symplectic (symplectic group) Sp(2m, $K)$ là nhóm của các phép đẳng cự của $\phi$. các ánh xạ trong Sp(2m, $K)$ được gọi là symplectic các ánh xạ. Đối với ở trên cơ sở (basis), Sp(2m, $K)$ là nhóm của 2m $\times$ 2m các ma trận $A$ sao cho
$$A^{\top}J_{m,m}A = J_{m,m}.$$
Các ma trận thỏa mãn ở trên đồng nhất thức được gọi là symplectic các ma trận. Trong mục này, ta chỉ ra rằng Sp(2m, $K)$ là nhóm con của SL(2m, $K)$ (rằng là, det() $= +1$ với mọi $A \in$ Sp(2m, $K))$, và ta chỉ ra rằng Sp(2m, $K)$ được sinh bởi đặc biệt các ánh xạ tuyến tính (linear maps) được gọi là symplectic các phép trượt. Thứ nhất, ta để lại nó như dễ bài tập để chỉ ra rằng Sp(2, $K) =$ SL(2, $K)$. độc giả nên cũng chứng minh rằng Sp(2m, $K)$ có nhóm con đẳng cấu đến GL(m, $K)$. Tiếp theo ta đặc trưng hóa symplectic các ánh xạ $f$ rằng để lại cố định mọi vectơ trong một số cho trước siêu phẳng (hyperplane) $H$, nghĩa là,
$$f(v) = vfor all v \in H.$$
Vì $\phi$ là không suy biến, theo Mệnh đề 29.22, trực giao $H^{\perp}$ của $H$ là đường thẳng (rằng là, $dim(H^{\perp}) = 1)$. Với mọi $u \in E$ và mọi $v \in H$, vì $f$ là phép đẳng cự (isometry) và f(v) $= v$ với mọi $v \in H$, ta có
$$\phi (f(u) -u, v) = \phi (f(u), v) -\phi (u, v)$$
$$= \phi (f(u), v) -\phi (f(u), f(v))$$
$$= \phi (f(u), v -f(v)))$$
$$= \phi (f(u), 0) = 0,$$
Mà chỉ ra rằng f(u) - $u \in H^{\perp}$ với mọi $u \in E$. Vì vậy, $f$ - id là ánh xạ tuyến tính (linear map) từ $E$ vào đường thẳng $H^{\perp}$ có hạt nhân (kernel) chứa $H$, mà có nghĩa là tồn tại một khác không vectơ $w \in H^{\perp}$ và một số dạng tuyến tính (linear form) $\psi$ sao cho
$$f(u) = u + \psi (u)w,u \in E.$$

<!-- PAGE 1049 -->
Vì $f$ là phép đẳng cự (isometry), ta phải có $\phi$ (f(u), f(v)) $= \phi (u, v)$ với mọi $u, v \in E$, mà có nghĩa là
$$\phi (u, v) = \phi (f(u), f(v))$$
$$= \phi (u + \psi (u)w, v + \psi (v)w)$$
$$= \phi (u, v) + \psi (u)\phi (w, v) + \psi (v)\phi (u, w) + \psi (u)\psi (v)\phi (w, w)$$
$$= \phi (u, v) + \psi (u)\phi (w, v) -\psi (v)\phi (w, u),$$
Mà cho ta
$$\psi (u)\phi (w, v) = \psi (v)\phi (w, u)for all u, v \in E.$$
Vì $\phi$ là không suy biến, ta có thể chọn một số $v_{0}$ sao cho $\phi (w, v_{0}) \neq  0$, và ta thu được $\psi (u)\phi (w, v_{0}) = \psi (v_{0})\phi (w, u)$ với mọi $u \in E$; nghĩa là,
$$\psi (u) = \lambda \phi (w, u)for all u \in E,$$
Với một số $\lambda  \in K$. Vì vậy, $f$ là của tạo thành
$$f(u) = u + \lambda \phi (w, u)w,for all u \in E.$$
Nó là cũng rõ ràng rằng mọi $f$ của ở trên tạo thành là symplectic ánh xạ. Nếu $\lambda  = 0$, thì $f =$ id. Ngược lại, nếu $\lambda$ ̸ $= 0$, thì f(u) $= u$ khi và chỉ khi $\phi (w, u) = 0$ khi và chỉ khi $u \in (Kw)^{\perp} = H$, ở đâu $H$ là siêu phẳng (hyperplane). Do đó, $f$ fixes mọi vectơ trong siêu phẳng (hyperplane) $H$. Lưu ý rằng vì $\phi$ là thay phiên, $\phi (w, w) = 0$, mà có nghĩa là $w \in H$. Trong tóm tắt, ta có được đặc trưng hóa tất cả symplectic các ánh xạ rằng để lại mọi vectơ trong một số siêu phẳng (hyperplane) cố định, và ta tạo sau đây định nghĩa.

> **Định nghĩa 29.20.** Cho trước không suy biến thay phiên tạo thành $\phi$ trên không gian $E$, symplectic phép trượt (transvection) (của hướng $w)$ là ánh xạ tuyến tính (linear map) $f$ của tạo thành
$$f(u) = u + \lambda \phi (w, u)w,for all u \in E,$$
Với một số khác không $w \in E$ và một số $\lambda  \in K$. Nếu $\lambda  \neq  0$, không gian con của các vectơ trái cố định bởi $f$ là siêu phẳng (hyperplane) $H = (Kw)^{\perp}$. ánh xạ $f$ cũng được ký hiệu $\tau_{w,\lambda}$. Nhận thấy rằng
$$\tau_{w,\lambda}  \circ \tau_{w,\mu}  = \tau_{w,\lambda+\mu}$$
Và $\tau_{w,\lambda}  =$ id khi và chỉ khi $\lambda  = 0$. ở trên chỉ ra rằng $det(\tau_{w,\lambda}$) $= 1$, vì khi $\lambda  \neq  0$, ta có $\tau_{w,\lambda}  = (\tau_{w,\lambda /2} )^{2}$. Của ta tiếp theo mục tiêu là để chỉ ra rằng nếu $u$ và $v$ là bất kỳ hai khác không các vectơ trong $E$, thì có một đơn giản symplectic ánh xạ $f$ sao cho f(u) $= v$.

> **Mệnh đề 29.36.** Cho trước bất kỳ hai khác không các vectơ $u, v \in E$, có một symplectic ánh xạ $f$ sao cho f(u) $= v$, và $f$ là hoặc symplectic phép trượt (transvection), hoặc hợp thành của hai symplectic các phép trượt.

<!-- PAGE 1050 -->

*Chứng minh.* Có hai các trường hợp. Trường hợp $1. \phi (u, v) \neq  0$. Trong trường hợp này, $u \neq  v$, vì $\phi (u, u) = 0$. Cho chúng ta nhìn cho symplectic phép trượt (transvection) của tạo thành $\tau_{v-u,\lambda}$. Ta muốn
$$v = u + \lambda \phi (v -u, u)(v -u) = u + \lambda \phi (v, u)(v -u),$$
Mà cho ta
$$(\lambda \phi (v, u) -1)(v -u) = 0.$$
Vì $\phi (u, v) \neq  0$ và $\phi (v, u) = -\phi (u, v)$, ta có thể chọn $\lambda  = \phi (v, u)^{-1}$ và $\tau_{v-u,\lambda}$ các ánh xạ $u$ đến $v$. Trường hợp $2. \phi (u, v) = 0$. Nếu $u = v$, sử dụng $\tau_{u,0}  =$ id. Bây giờ, giả sử $u \neq  v$. Ta khẳng định rằng nó là khả dĩ/có thể đến chọn một số $w \in E$ sao cho $\phi (u, w) \neq  0$ và $\phi (v, w) \neq  0$. Thật vậy, nếu $(Ku)^{\perp} = (Kv)^{\perp}$, thì chọn bất kỳ khác không vectơ $w$ không trong siêu phẳng (hyperplane) $(Ku)^{\perp}$. Othwerwise, $(Ku)^{\perp}$ và $(Kv)^{\perp}$ là hai phân biệt các siêu phẳng, do đó không được chứa trong khác (chúng có cùng số chiều), do đó chọn bất kỳ khác không vectơ $w_{1}$ sao cho $w_{1} \in (Ku)^{\perp}$ và $w_{1} \in / (Kv)^{\perp}$, và chọn bất kỳ khác không vectơ $w_{2}$ sao cho $w_{2} \in (Kv)^{\perp}$ và $w_{2} \in / (Ku)^{\perp}$. Nếu ta cho $w = w_{1} + w_{2}$, thì $\phi (u, w) = \phi (u, w_{2}) \neq  0$, và $\phi (v, w) = \phi (v, w_{1}) \neq  0$. Từ trường hợp $1$, ta có một số symplectic phép trượt (transvection) $\tau_{w-u,\lambda1}$ sao cho $\tau_{w-u,\lambda1} (u) = w$, và một số symplectic phép trượt (transvection) $\tau_{v-w,\lambda2}$ sao cho $\tau_{v-w,\lambda2} (w) = v$, do đó hợp thành $\tau_{v-w,\lambda2}  \circ \tau_{w-u,\lambda1}$ các ánh xạ $u$ đến $v$. Tiếp theo, ta sẽ like để mở rộng Mệnh đề 29.36 đến hai hyperbolic các mặt phẳng $W_{1}$ và $W_{2}$.

> **Mệnh đề 29.37.** Cho trước bất kỳ hai hyperbolic các mặt phẳng $W_{1}$ và $W_{2}$ cho trước bởi các cơ sở $(u_{1}, v_{1})$ và $(u_{2}, v_{2})$ (với $\phi (u_{i}, u_{i}) = \phi (v_{i}, v_{i}) = 0$ và $\phi (u_{i}, v_{i}) = 1$, cho $i = 1, 2)$, có một symplectic ánh xạ $f$ sao cho $f(u_{1}) = u_{2}, f(v_{1}) = v_{2}$, và $f$ là hợp thành của nhiều nhất bốn symplectic các phép trượt.

*Chứng minh.* Từ Mệnh đề 29.36, ta có thể ánh xạ $u_{1}$ đến $u_{2}$, bằng cách sử dụng ánh xạ $f$ mà là hợp thành của nhiều nhất hai symplectic các phép trượt. Nói $v_{3} = f(v_{1})$. Ta khẳng định rằng có một ánh xạ $g$ sao cho $g(u_{2}) = u_{2}$ và $g(v_{3}) = v_{2}$, và $g$ là hợp thành của nhiều nhất hai symplectic các phép trượt. Nếu do đó, $g \circ f$ các ánh xạ cặp $(u_{1}, v_{1})$ đến cặp $(u_{2}, v_{2})$, và $g \circ f$ bao gồm của nhiều nhất bốn symplectic các phép trượt. Do đó, ta cần để chứng minh sau đây khẳng định: Khẳng định. Nếu $(u, v)$ và $(u$, v') là hyperbolic các cơ sở xác định hai hyperbolic các mặt phẳng, thì có một symplectic ánh xạ $g$ sao cho g(u) $= u$, g(v) $=$ v', và $g$ là hợp thành của nhiều nhất hai symplectic các phép trượt. Có hai trường hợp. Trường hợp $1. \phi (v$, v') $\neq  0$. Trong trường hợp này, có một symplectic phép trượt (transvection) $\tau_{v'-v,\lambda}$ sao cho $\tau_{v'-v,\lambda} (v) =$ v'. Ta cũng có
$$\phi (u, v'-v) = \phi (u, v') -\phi (u, v) = 1 -1 = 0.$$

<!-- PAGE 1051 -->
Vì vậy, $\tau_{v'-v,\lambda} (u) = u$, và $g = \tau_{v'-v,\lambda}$ thực hiện job. Trường hợp $2. \phi (v$, v') $= 0$. Thứ nhất, kiểm tra rằng $(u, u + v)$ là cũng hyperbolic cơ sở (basis). Hơn nữa,
$$\phi (v, u + v) = \phi (v, u) + \phi (v, v) = \phi (v, u) = -1 \neq  0.$$
Do đó, có một symplectic phép trượt (transvection) $\tau_{v,\lambda1}$ sao cho $\tau_{u,\lambda1} (v) = u + v$ và $\tau_{u,\lambda1} (u) = u$. Ta cũng có
$$\phi (u + v, v') = \phi (u, v') + \phi (v, v') = \phi (u, v') \neq  1 = 0,$$
Do đó có một symplectic phép trượt (transvection) $\tau_{v'-u-v,\lambda2}$ sao cho $\tau_{v'-u-v,\lambda2} (u + v) =$ v'. Vì
$$\phi (u, v'-u -v) = \phi (u, v') -\phi (u, u) -\phi (u, v) = 1 -0 -1 = 0,$$
Ta có $\tau_{v'-u-v,\lambda2} (u) = u$. Thì, hợp thành $g = \tau_{v'-u-v,\lambda2}  \circ \tau_{u,\lambda1}$ là sao cho g(u) $= u$ và g(v) $=$ v'. Ta sẽ sử dụng Mệnh đề 29.37 trong quy nạp lập luận để chứng minh rằng symplectic các phép trượt sinh nhóm symplectic (symplectic group). Thứ nhất, tạo nhận xét sau đây: Nếu $U$ là không suy biến không gian con của $E$, sao cho
$$E = U^{\perp}\oplus U^{\perp},$$
Và nếu $\tau$ là phép trượt (transvection) của $H^{\perp}$, thì ta có thể tạo thành ánh xạ tuyến tính (linear map) $id_{U}^{\perp}\oplus \tau$ có thu hẹp đến $U$ là đồng nhất thức và có thu hẹp đến $U^{\perp}$ là $\tau$, và $id_{U}^{\perp}\oplus \tau$ là phép trượt (transvection) của $E$.

> **Định lý 29.38.** nhóm symplectic (symplectic group) Sp(2m, $K)$ được sinh bởi symplectic các phép trượt. Với mọi phép trượt (transvection) $f \in$ Sp(2m, $K)$, ta có det(f) $= 1$.

*Chứng minh.* Cho $G$ là nhóm con của Sp(2m, $K)$ được sinh bởi các phép trượt. Ta cần để chứng minh rằng $G =$ Sp(2m, $K)$. Cho $(u_{1}, v_{1}, \dots  , u_{m}, v_{m})$ là symplectic cơ sở (basis) của $E$, và cho $f \in$ Sp(2m, $K)$ là bất kỳ symplectic ánh xạ. Thì, $f$ các ánh xạ $(u_{1}, v_{1}, \dots  , u_{m}, v_{m})$ đến một cái khác symplectic cơ sở (basis) $(u_{1}', v_{1}', \dots  , u_{m}', v_{m}')$. Nếu ta chứng minh rằng tồn tại một $g \in G$ sao cho $g(u_{i}) = u_{i}'$ và $g(v_{i}) = v_{i}'$ cho $i = 1, \dots  , m$, thì $f = g$ và $G =$ Sp(2m, $K)$. Ta sử dụng quy nạp trên $i$ để chứng minh rằng tồn tại một $g_{i} \in G$ sao cho $g_{i}$ các ánh xạ $(u_{1}, v_{1}, \dots  , u_{i}, v_{i})$ đến $(u_{1}', v_{1}', \dots  , u_{i}', v_{i}')$. base trường hợp $i = 1$ suy ra từ Mệnh đề 29.37. Cho quy nạp bước, giả sử rằng ta có một số $g_{i} \in G$ ánh xạ $(u_{1}, v_{1}, \dots  , u_{i}, v_{i})$ đến $(u_{1}', v_{1}', \dots  , u_{i}', v_{i}')$, và cho $(u_{i+1}'', v_{i+1}'', \dots  , u_{m}'', v_{m}'')$ là ảnh (image) của $(u_{i+1}, v_{i+1}, \dots  , u_{m}, v_{m})$ bởi $g_{i}$. Nếu $U$ là không gian con được sinh (spanned) bởi $(u_{1}', v_{1}', \dots  , u_{m}', v_{m}')$, thì mỗi mặt phẳng hyperbolic (hyperbolic plane) $W_{i+k}'$ cho trước bởi $(u_{i+k}', v_{i+k}')$ và mỗi mặt phẳng hyperbolic (hyperbolic plane) $W_{i+k}''$ cho trước bởi $(u_{i+k}'', v_{i+k}'')$ thuộc đến
