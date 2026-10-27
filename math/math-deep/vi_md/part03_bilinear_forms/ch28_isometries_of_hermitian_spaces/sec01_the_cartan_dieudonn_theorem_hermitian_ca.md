# Cartan–Dieudonné Định lý, Hermite Trường hợp


<!-- PAGE 997 -->
Chương $28$ Các phép đẳng cự của Các không gian Hermite

## 28.1 Cartan–Dieudonn´e Định lý,

$$Hermitian Case$$
Cartan-Dieudonn´e định lý có thể được suy rộng/tổng quát hóa (Định lý 28.2), nhưng điều này đòi hỏi cho phép mới các loại của siêu phẳng (hyperplane) các phép đối xứng rằng ta gọi Hermite các phép đối xứng. Sau thực hiện do đó, mọi phép đẳng cự (isometry) trong U(n) có thể luôn luôn được viết như hợp thành của nhiều nhất $n$ Hermite các phép đối xứng (cho $n \ge 2)$. Tốt hơn vẫn chưa, mọi phép quay trong SU(n) có thể được biểu diễn dưới dạng hợp thành của nhiều nhất 2n - $2$ (tiêu chuẩn) siêu phẳng (hyperplane) các phép đối xứng! Điều này suy ra rằng mọi unita phép biến đổi trong U(n) là hợp thành của nhiều nhất 2n-1 các phép đẳng cự, với nhiều nhất một Hermite phép đối xứng (reflection), khác các phép đẳng cự đang là (tiêu chuẩn) siêu phẳng (hyperplane) các phép đối xứng. then chốt Mệnh đề 13.2 là sai như là, và cần là amended. Phân rã QR (QR-decomposition) của tùy ý phức các ma trận theo Householder các ma trận có thể cũng là suy rộng/tổng quát hóa, bằng cách sử dụng mẹo/kỹ thuật. Trong thứ tự đến tổng quát hóa Cartan–Dieudonn´e định lý và Phân rã QR (QR-decomposition) theo Householder các phép biến đổi, ta cần đến giới thiệu mới các loại của siêu phẳng (hyperplane) các phép đối xứng. Điều này là không một cách thực đáng ngạc nhiên, vì trong Hermite trường hợp, có suy rộng/không thực sự các phép đẳng cự có định thức (determinant) có thể được bất kỳ unit phức số. Siêu phẳng (hyperplane) các phép đối xứng là suy rộng/tổng quát hóa như sau.

> **Định nghĩa 28.1.** Cho $E$ là Không gian Hermite (Hermitian space) của hữu hạn số chiều. Với mọi siêu phẳng (hyperplane) $H$, với mọi khác không vectơ $w$ trực giao đến $H$, sao cho $E = H \oplus G$, ở đâu $G =\mathbb{C} w$, Hermite phép đối xứng (reflection) về $H$ của góc $\theta$ là ánh xạ tuyến tính (linear map) của tạo thành $\rho_{H, \theta}$: $E \to E$, được định nghĩa sao cho
$$\rho_{H, \theta} (u) = p_{H}(u) + e^{i\theta}p_{G}(u),$$
$$̸$$
Với mọi unit phức số $e^{i\theta} = 1$ (i.e. $\theta$ ̸ $= k2\pi$). Với mọi khác không vectơ $w \in E$, ta ký hiệu bởi $\rho_{w,\theta}$ Hermite phép đối xứng (reflection) cho trước bởi $\rho_{H,\theta}$, ở đâu $H$ là siêu phẳng (hyperplane) trực giao đến $w$.
$$997$$

<!-- PAGE 998 -->
Vì $u = p_{H}(u) + p_{G}(u)$, Hermite phép đối xứng (reflection) $\rho_{w, \theta}$ cũng được biểu diễn như
$$\rho_{w, \theta} (u) = u + (e^{i\theta}-1)p_{G}(u),$$
Hoặc như
$$1)  \cdot$$
$$\rho_{w, \theta} (u) = u + (e^{i\theta}- \frac{(u w)}{\|w\|^{2}} w.$$
Lưu ý rằng trường hợp của tiêu chuẩn siêu phẳng (hyperplane) phép đối xứng (reflection) là thu được khi $e^{i\theta} = -1$, i.e., $\theta  = \pi$. Ta để lại như dễ bài tập để kiểm tra rằng $\rho_{w, \theta}$ là thật vậy phép đẳng cự (isometry), và rằng nghịch đảo của $\rho_{w, \theta}$ là $\rho_{w,-\theta}$. Nếu ta chọn cơ sở trực chuẩn (orthonormal basis) $(e_{1}, \dots  , e_{n})$ sao cho $(e_{1}, \dots  , e_{n-1})$ là cơ sở trực chuẩn (orthonormal basis) của $H$, ma trận của $\rho_{w, \theta}$ là
$$\begin{pmatrix} I_{n-1} & 0 \\ 0 & e^{i\theta} \end{pmatrix}$$
Ta bây giờ đến đến chính surprise. Cho trước bất kỳ hai phân biệt các vectơ $u$ và $v$ sao cho $\|u\| = \|v\|$, ở đó isn’t luôn luôn siêu phẳng (hyperplane) phép đối xứng (reflection) ánh xạ $u$ đến $v$, nhưng điều này có thể được được thực hiện bằng cách sử dụng hai Hermite các phép đối xứng!

> **Mệnh đề 28.1.** Cho $E$ là bất kỳ không tầm thường Không gian Hermite (Hermitian space).
$(1)$ Với mọi hai các vectơ $u, v \in E$ sao cho $u \neq  v$ và $\|u\| = \|v\|$, nếu $u \cdot  v = e^{i\theta}|u \cdot$ v|, thì (thông thường) phép đối xứng (reflection) $s$ về siêu phẳng (hyperplane) trực giao đến vectơ $v$ - $e^{-i\theta}u$ là sao cho s(u) $= e^{i\theta}v$.
$(2)$ Với mọi khác không vectơ $v \in E$, với mọi unit phức số $e^{i\theta} \neq  1$, có một Hermite phép đối xứng (reflection) $\rho_{v,\theta}$ sao cho
$$\rho_{v,\theta} (v) = e^{i\theta}v.$$
Hệ quả là, cho $u$ và $v$ như trong $(1)$, ta có $\rho_{v,-\theta}  \circ$ s(u) $= v$.

*Chứng minh.* $(1)$ Xét (thông thường) phép đối xứng (reflection) về siêu phẳng (hyperplane) trực giao đến $w = v -e^{-i\theta}u$. Ta có
$$2  \cdot  -$$
$$s(u) = u - \frac{(u (ve^{-i\theta}u))}{\|v -e^{-i\theta}u\|^{2}} (v -e^{-i\theta}u).$$
Ta cần để tính
$$-2u \cdot  (v -e^{-i\theta}u)and(v -e^{-i\theta}u) \cdot  (v -e^{-i\theta}u).$$
Vì $u \cdot  v = e^{i\theta}|u \cdot$ v|, ta có
$$e^{-i\theta}u \cdot  v = |u \cdot  v|ande^{i\theta}v \cdot  u = |u \cdot  v|.$$
Bằng cách sử dụng ở trên và sự kiện rằng $\|u\| = \|v\|$, ta thu được
$$-2u \cdot  (v -e^{-i\theta}u) = 2e^{i\theta}\|u\|^{2}-2u \cdot  v,$$
$$= 2e^{i\theta}(\|u\|^{2}-|u \cdot  v|),$$

<!-- PAGE 999 -->
Và
$$(v -e^{-i\theta}u) \cdot  (v -e^{-i\theta}u) = \|v\|^{2}+ \|u\|^{2}-e^{-i\theta}u \cdot  v -e^{i\theta}v \cdot  u,$$
$$= 2(\|u\|^{2}-|u \cdot  v|),$$
Và do đó,
$$2  \cdot  -$$
$$- \frac{(u (ve^{-i\theta}u))}{\|(v -e^{-i\theta}u)\|^{2}} (v -e^{-i\theta}u) = e^{i\theta}(v -e^{-i\theta}u).$$
Nhưng khi đó,
$$s(u) = u + e^{i\theta}(v -e^{-i\theta}u) = u + e^{i\theta}v -u = e^{i\theta}v,$$
Và s(u) $= e^{i\theta}v$, như đã khẳng định.
$(2)$ Điều này phần là dễ hơn. Xét Hermite phép đối xứng (reflection)
$$1)  \cdot$$
$$\rho_{v,\theta} (u) = u + (e^{i\theta}- \frac{(u v)}{\|v\|^{2}} v.$$
Ta có
$$1)  \cdot$$
$$\rho_{v,\theta} (v) = v + (e^{i\theta}- \frac{(v v)}{\|v\|^{2}} v,$$
$$= v + (e^{i\theta}-1)v,$$
$$= e^{i\theta}v.$$
Do đó, $\rho_{v,\theta} (v) = e^{i\theta}v$. Vì $\rho_{v,\theta}$ là tuyến tính, thay đổi lập luận $v$ đến $e^{i\theta}v$, ta thu được
$$\rho_{v,-\theta} (e^{i\theta}v) = v,$$
Và do đó, $\rho_{v,-\theta}  \circ$ s(u) $= v$.
Các nhận xét:
$(1)$ Nếu ta sử dụng vectơ $v + e^{-i\theta}u$ thay vì của $v$ - $e^{-i\theta}u$, ta thu được s(u) $= -e^{i\theta}v$.
$(2)$ Nhất định các tác giả, chẳng hạn như Kincaid và Cheney $[105]$ và Ciarlet $[41]$, sử dụng vectơ $u + e^{i\theta}v$ thay vì của của ta vectơ $v + e^{-i\theta}u$. effect của điều này lựa chọn là rằng chúng cũng thu được s(u) $= -e^{i\theta}v$.
$(3)$ Nếu $v = \|u\|e_{1}$, ở đâu $e_{1}$ là cơ sở (basis) vectơ, $u \cdot  e_{1} = a_{1}$, ở đâu $a_{1}$ là chỉ hệ số của $u$ trên cơ sở (basis) vectơ $e_{1}$. Thì, vì $u \cdot  e_{1} = e^{i\theta}|a_{1}|$, lựa chọn của cộng dấu trong vectơ $\|u\|e_{1} + e^{-i\theta}u$ có effect rằng hệ số của vectơ này trên $e_{1}$ là $\|u\| + |a_{1}|$, và không có cancellations lấy place, mà được ưu tiên hơn cho số tính ổn định (ta cần đến chia bởi square chuẩn (norm) của vectơ này).

<!-- PAGE 1000 -->
Phần cuối cùng của Mệnh đề 28.1 chỉ ra rằng Cartan–Dieudonn´e là salvaged, vì ta có thể send $u$ đến $v$ bởi dãy của hai Hermite các phép đối xứng khi $u \neq  v$ và $\|u\| = \|v\|$, và vì nghịch đảo của Hermite phép đối xứng (reflection) là Hermite phép đối xứng (reflection). Thực sự, bởi vì ta là trên phức trường, ánh xạ tuyến tính (linear map) luôn luôn có (phức) các trị riêng (eigenvalues), và ta có thể thu được slightly được cải thiện kết quả.

> **Định lý 28.2.** Cho $E$ là Không gian Hermite (Hermitian space) có số chiều $n \ge 1$. Mọi phép đẳng cự (isometry) $f \in$ U(E) là hợp thành $f = \rho_{n}  \circ \rho_{n-1}  \circ \cdots  \circ \rho_{1}$ của $n$ các phép đẳng cự $\rho_{j}$, ở đâu mỗi $\rho_{j}$ là hoặc đồng nhất thức hoặc Hermite phép đối xứng (reflection) (có thể tiêu chuẩn siêu phẳng (hyperplane) phép đối xứng (reflection)). Khi $n \ge 2$, đồng nhất thức là hợp thành của bất kỳ siêu phẳng (hyperplane) phép đối xứng (reflection) với chính nó.

*Chứng minh.* Ta chứng minh bằng quy nạp theo $n$ rằng có một cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors) $(u_{1}, \dots  , u_{n})$ của $f$ sao cho
$$f(u_{j}) = e^{i\theta j}u_{j},$$
Ở đâu $e^{i\theta j}$ là trị riêng (eigenvalue) liên kết với $u_{j}$, với mọi $j, 1 \le j \le n$. Khi $n = 1$, mọi phép đẳng cự (isometry) $f \in$ U(E) là hoặc đồng nhất thức hoặc Hermite phép đối xứng (reflection) $\rho_{\theta}$, vì với mọi khác không vectơ $u$, ta có f(u) $= e^{i\theta}u$ với một số $\theta$. Ta cho $u_{1}$ là bất kỳ khác không unit vectơ. Cho chúng ta bây giờ xét trường hợp ở đâu $n \ge 2$. Vì $\mathbb{C}$ là algebraically đóng, đa thức đặc trưng (characteristic polynomial) det(f - $\lambda$ id) của $f$ có $n$ phức các nghiệm mà phải là tạo thành $e^{i\theta}$, vì chúng có tuyệt đối giá trị $1$. Chọn bất kỳ như vậy trị riêng (eigenvalue) $e^{i\theta1}$, và chọn bất kỳ vectơ riêng (eigenvector) $u_{1} \neq  0$ của $f$ cho $e^{i\theta1}$ của unit độ dài. Nếu $F =\mathbb{C} u_{1}$ là không gian con được sinh (spanned) bởi $u_{1}$, ta có f(F) $= F$, vì $f(u_{1}) = e^{i\theta1}u_{1}$. Vì f(F) $= F$ và $f$ là phép đẳng cự (isometry), nó là dễ để xem rằng $f(F^{\perp}$) $\subseteq F^{\perp}$, và theo Mệnh đề 14.13, ta có $E = F \oplus F^{\perp}$. Hơn nữa, hiển nhiên là thu hẹp của $f$ đến $F^{\perp}$ là unita. Vì dim $(F^{\perp}$) $= n$ - $1$, ta có thể áp dụng giả thiết quy nạp (induction hypothesis) đến $F^{\perp}$, và ta thu được cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors) $(u_{2}, \dots  , u_{n})$ cho $F^{\perp}$ sao cho
$$f(u_{j}) = e^{i\theta j}u_{j},$$
Ở đâu $e^{i\theta j}$ là trị riêng (eigenvalue) liên kết với $u_{j}$, với mọi $j, 2 \le j \le n$ Vì $E = F \oplus F^{\perp}$ và $F = \mathbb{C} u_{1}$, khẳng định được chứng minh. Nhưng khi đó, nếu $\rho_{j}$ là Hermite phép đối xứng (reflection) về siêu phẳng (hyperplane) $H_{j}$ trực giao đến $u_{j}$ và của góc $\theta_{j}$, hiển nhiên là
$$f = \rho_{\theta n}  \circ \cdots  \circ \rho_{\theta1} .$$
Khi $n \ge 2$, ta có id $= s \circ s$ với mọi phép đối xứng (reflection) $s$.
Các nhận xét:
$(1)$ Bất kỳ phép đẳng cự (isometry) $f \in$ U(n) có thể được biểu diễn như $f = \rho_{\theta} \circ g$, ở đâu $g \in$ SU(n) là phép quay, và $\rho_{\theta}$ là Hermite phép đối xứng (reflection). Thật vậy, bởi ở trên định lý, đối với cơ sở (basis) $(u_{1}, \dots  , u_{n})$, det(f) $= e^{i(\theta1+\cdot \cdot \cdot+\theta n)}$, và đặt $\theta  = \theta_{1}  +\cdots +\theta_{n}$ và $\rho_{\theta}$ là Hermite

<!-- PAGE 1001 -->
Phép đối xứng (reflection) về siêu phẳng (hyperplane) trực giao đến $u_{1}$ và của góc $\theta$, vì $\rho_{\theta}  \circ \rho_{-\theta}  =$ id, ta có
$$f = (\rho_{\theta}  \circ \rho_{-\theta} ) \circ f = \rho_{\theta}  \circ (\rho_{-\theta}  \circ f).$$
Đặt $g = \rho_{-\theta}  \circ f$, hiển nhiên là det(g) $= 1$. Hệ quả là, có một song ánh giữa $S^{1} \times$ SU(n) và U(n), ở đâu $S^{1}$ là unit đường tròn (mà tương ứng với nhóm của phức các số $e^{i\theta}$ của unit độ dài). Thực ra, nó là phép đồng phôi (homeomorphism).
$(2)$ Ta abandoned style của chứng minh được sử dụng trong định lý 27.1, bởi vì trong Hermite trường hợp, các trị riêng (eigenvalues) và các vectơ riêng (eigenvectors) luôn luôn tồn tại, và chứng minh là đơn giản hơn rằng cách (trong thực trường hợp, phép đẳng cự (isometry) có thể không có bất kỳ thực các trị riêng (eigenvalues)!). sacrifice là rằng định lý cho ta không có information trên số của (tiêu chuẩn) siêu phẳng (hyperplane) các phép đối xứng. Ta sẽ rectify tình huống này một cách ngắn. Ta sẽ bây giờ reveal đẹp mẹo/kỹ thuật (tìm thấy trong Mneimn´e và Testard $[131])$ rằng cho phép chúng ta để chứng minh rằng mọi phép quay trong SU(n) là hợp thành của nhiều nhất 2n - $2$ (tiêu chuẩn) siêu phẳng (hyperplane) các phép đối xứng. Cho những gì suy ra, nó là nhiều hơn/thêm thuận tiện đến ký hiệu tiêu chuẩn phép đối xứng (reflection) về siêu phẳng (hyperplane) $H$ như $h_{u}$ (nó là tầm thường rằng các phần tử này không phụ thuộc vào lựa chọn của $u$ trong $H^{\perp})$. Thì, cho trước bất kỳ hai phân biệt trực giao các vectơ $u, v$ sao cho $\|u\| = \|v\|$, xét hợp thành $\rho_{v,-\theta}  \circ \rho_{u, \theta}$. mẹo/kỹ thuật là rằng điều này hợp thành có thể được biểu diễn dưới dạng hai tiêu chuẩn siêu phẳng (hyperplane) các phép đối xứng! Điều này wonderful sự kiện được chứng minh trong tiếp theo Mệnh đề.

> **Mệnh đề 28.3.** Cho $E$ là không tầm thường Không gian Hermite (Hermitian space). Với mọi hai phân biệt trực giao các vectơ $u, v$ sao cho $\|u\| = \|v\|$, ta có
$$\rho_{v,-\theta}  \circ \rho_{u, \theta}  = h_{v-u} \circ h_{v-e-i\theta u} = h_{u+v} \circ h_{u+ei\theta v}.$$

*Chứng minh.* Vì $u$ và $v$ là trực giao, mỗi một là trong siêu phẳng (hyperplane) trực giao đến khác, và do đó,
$$\rho_{u, \theta} (u) = e^{i\theta}u,$$
$$\rho_{u, \theta} (v) = v,$$
$$\rho_{v,-\theta} (u) = u,$$
$$\rho_{v,-\theta} (v) = e^{-i\theta}v,$$
$$h_{v-u}(u) = v,$$
$$h_{v-u}(v) = u,$$
$$h_{v-e-i\theta u}(u) = e^{i\theta}v,$$
$$h_{v-e-i\theta u}(v) = e^{-i\theta}u.$$
Hệ quả là, bằng cách sử dụng tính tuyến tính,
$$\rho_{v,-\theta}  \circ \rho_{u, \theta} (u) = e^{i\theta}u,$$
$$\rho_{v,-\theta}  \circ \rho_{u, \theta} (v) = e^{-i\theta}v,$$
$$h_{v-u} \circ h_{v-e-i\theta u}(u) = e^{i\theta}u,$$
$$h_{v-u} \circ h_{v-e-i\theta u}(v) = e^{-i\theta}v,$$

<!-- PAGE 1002 -->
Và vì cả hai $\rho_{v,-\theta}  \circ \rho_{u, \theta}$ và $h_{v-u}\circ h_{v-e-i\theta u}$ là đồng nhất thức trên phần bù trực giao (orthogonal complement) của ${u, v}$, chúng là bằng nhau. Vì ta cũng có
$$h_{u+v}(u) = -v,$$
$$h_{u+v}(v) = -u,$$
$$h_{u+ei\theta v}(u) = -e^{i\theta}v,$$
$$h_{u+ei\theta v}(v) = -e^{-i\theta}u,$$
Ta kiểm chứng được ngay rằng
$$h_{v-u} \circ h_{v-e-i\theta u} = h_{u+v} \circ h_{u+ei\theta v}.$$
Ta sẽ sử dụng Mệnh đề 28.3 như sau.

> **Mệnh đề 28.4.** Cho $E$ là không tầm thường Không gian Hermite (Hermitian space), và cho $(u_{1}, \dots  , u_{n})$ là một số cơ sở trực chuẩn (orthonormal basis) cho $E$. Với mọi $\theta_{1} , \dots  , \theta_{n}$ sao cho $\theta_{1}  + \cdots  + \theta_{n}  = 0$, nếu $f \in$ U(n) là phép đẳng cự (isometry) được định nghĩa sao cho
$$f(u_{j}) = e^{i\theta j}u_{j},$$
Với mọi $j, 1 \le j \le n$, thì $f$ là phép quay $(f \in$ SU(n)), và
$$f = \rho_{un, \theta n}  \circ \cdots  \circ \rho_{u1, \theta1}$$
$$= \rho_{un,-(\theta1+\cdot \cdot \cdot+\theta n-1)}  \circ \rho_{un-1, \theta1+\cdot \cdot \cdot+\theta n-1}  \circ \cdots  \circ \rho_{u2,-\theta1}  \circ \rho_{u1, \theta1}$$
$$= h_{un-un-1} \circ h_{un-e-i(\theta1+\cdot \cdot \cdot+\theta n-1)un-1} \circ \cdots  \circ h_{u2-u1} \circ h_{u2-e-i\theta1u1}$$
$$= h_{un-1+un} \circ h_{un-1+ei(\theta1+\cdot \cdot \cdot+\theta n-1)un} \circ \cdots  \circ h_{u1+u2} \circ h_{u1+ei\theta1u2}.$$

*Chứng minh.* Nó là hiển nhiên từ các định nghĩa rằng
$$f = \rho_{un, \theta n}  \circ \cdots  \circ \rho_{u1, \theta1} ,$$
Và vì định thức (determinant) của $f$ là
$$D(f) = e^{i\theta1}\cdots  e^{i\theta n}= e^{i(\theta1+\cdot \cdot \cdot+\theta n)}$$
Và $\theta_{1}  + \cdots  + \theta_{n}  = 0$, ta có D(f) $= e^{0} = 1$, và $f$ là phép quay. Đặt $f_{k} = \rho_{uk,-(\theta1+\cdot \cdot \cdot+\theta k-1)}  \circ \rho_{uk-1, \theta1+\cdot \cdot \cdot+\theta k-1}  \circ \cdots  \circ \rho_{u3,-(\theta1+\theta2)}  \circ \rho_{u2, \theta1+\theta2}  \circ \rho_{u2,-\theta1}  \circ \rho_{u1, \theta1}$, ta chứng minh bằng quy nạp theo $k, 2 \le k \le n$, rằng
$$e^{i\theta j}u_{j}if 1 \le j \le k -1,$$
$$$$
$$$$
$$f_{k}(u_{j}) =e^{-i(\theta1+\cdot \cdot \cdot+\theta k-1)}u_{k}if j = k, and$$
$$u_{j}if k + 1 \le j \le n.$$
$$$$

<!-- PAGE 1003 -->
Base trường hợp đã là treated trong Mệnh đề 28.3. Bây giờ, chứng minh của Mệnh đề 28.3 cũng đã chỉ ra rằng
$$\rho_{uk+1,-(\theta1+\cdot \cdot \cdot+\theta k)}  \circ \rho_{uk, \theta1+\cdot \cdot \cdot+\theta k} (u_{k}) = e^{i(\theta1+\cdot \cdot \cdot+\theta k)}u_{k},$$
$$\rho_{uk+1,-(\theta1+\cdot \cdot \cdot+\theta k)}  \circ \rho_{uk, \theta1+\cdot \cdot \cdot+\theta k} (u_{k+1}) = e^{-i(\theta1+\cdot \cdot \cdot+\theta k)}u_{k+1},$$
Và do đó, bằng cách sử dụng giả thiết quy nạp (induction hypothesis) cho $k (2 \le k \le n$ - $1)$, ta có $f_{k+1}(u_{j}) = \rho_{uk+1,-(\theta1+\cdot \cdot \cdot+\theta k)}  \circ \rho_{uk, \theta1+\cdot \cdot \cdot+\theta k}  \circ f_{k}(u_{j}) = e^{i\theta j}u_{j}, 1 \le j \le k$ - $1, f_{k+1}(u_{k}) = \rho_{uk+1,-(\theta1+\cdot \cdot \cdot+\theta k)}  \circ \rho_{uk, \theta1+\cdot \cdot \cdot+\theta k}  \circ f_{k}(u_{k}) = e^{i(\theta1+\cdot \cdot \cdot+\theta k)}e^{-i(\theta1+\cdot \cdot \cdot+\theta k-1)}u_{k} = e^{i\theta k}u_{k}, f_{k+1}(u_{k+1}) = \rho_{uk+1,-(\theta1+\cdot \cdot \cdot+\theta k)}  \circ \rho_{uk, \theta1+\cdot \cdot \cdot+\theta k}  \circ f_{k}(u_{k+1}) = e^{-i(\theta1+\cdot \cdot \cdot+\theta k)}u_{k+1}, f_{k+1}(u_{j}) = \rho_{uk+1,-(\theta1+\cdot \cdot \cdot+\theta k)}  \circ \rho_{uk, \theta1+\cdot \cdot \cdot+\theta k}  \circ f_{k}(u_{j}) = u_{j}, k + 1 \le j \le n$, mà chứng minh quy nạp bước. Như tóm tắt, ta được chứng minh rằng
$$($$
$$e^{i\theta j}u_{j}if 1 \le j \le n -1,$$
$$f_{n}(u_{j}) =$$
$$e^{-i(\theta1+\cdot \cdot \cdot+\theta n-1)}u_{n}when j = n,$$
Nhưng vì $\theta_{1}  +\cdots +\theta_{n}  = 0$, ta có $\theta_{n}  = -(\theta_{1}  +\cdots +\theta_{n-1}$), và cuối cùng biểu thức là thực ra
$$f_{n}(u_{n}) = e^{i\theta n}u_{n}.$$
Vì vậy, ta được chứng minh rằng $f = \rho_{un, \theta n}  \circ \cdots  \circ \rho_{u1, \theta1}  = \rho_{un,-(\theta1+\cdot \cdot \cdot+\theta n-1)}  \circ \rho_{un-1, \theta1+\cdot \cdot \cdot+\theta n-1}  \circ \cdots  \circ \rho_{u2,-\theta1}  \circ \rho_{u1, \theta1}$, và bằng cách sử dụng Mệnh đề 28.3, ta cũng có
$$f = \rho_{un,-(\theta1+\cdot \cdot \cdot+\theta n-1)}  \circ \rho_{un-1, \theta1+\cdot \cdot \cdot+\theta n-1}  \circ \cdots  \circ \rho_{u2,-\theta1}  \circ \rho_{u1, \theta1}$$
$$= h_{un-un-1} \circ h_{un-e-i(\theta1+\cdot \cdot \cdot+\theta n-1)un-1} \circ \cdots  \circ h_{u2-u1} \circ h_{u2-e-i\theta1u1}$$
$$= h_{un-1+un} \circ h_{un-1+ei(\theta1+\cdot \cdot \cdot+\theta n-1)un} \circ \cdots  \circ h_{u1+u2} \circ h_{u1+ei\theta1u2},$$
Mà các đầy đủ chứng minh. Ta cuối cùng thu được của ta được cải thiện phiên bản của Cartan–Dieudonn´e định lý.

> **Định lý 28.5.** Cho $E$ là Không gian Hermite (Hermitian space) có số chiều $n \ge 1$. Mọi phép quay $f \in$ SU(E) khác nhau từ đồng nhất thức là hợp thành của nhiều nhất 2n-2 tiêu chuẩn siêu phẳng (hyperplane) các phép đối xứng. Mọi phép đẳng cự (isometry) $f \in$ U(E) khác nhau từ đồng nhất thức là hợp thành của nhiều nhất 2n - $1$ các phép đẳng cự, tất cả tiêu chuẩn siêu phẳng (hyperplane) các phép đối xứng, ngoại trừ cho có thể một Hermite phép đối xứng (reflection). Khi $n \ge 2$, đồng nhất thức là hợp thành của bất kỳ phép đối xứng (reflection) với chính nó.

<!-- PAGE 1004 -->

*Chứng minh.* Theo Định lý 28.2, $f \in$ SU(n) có thể được viết dưới dạng hợp thành
$$\rho_{un, \theta n}  \circ \cdots  \circ \rho_{u1, \theta1} ,$$
Ở đâu $(u_{1}, \dots  , u_{n})$ là cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors). Vì $f$ là phép quay, det(f) $= 1$, và điều này suy ra rằng $\theta_{1}  + \cdots  + \theta_{n}  = 0$. Theo Mệnh đề 28.4,
$$f = h_{un-un-1} \circ h_{un-e-i(\theta1+\cdot \cdot \cdot+\theta n-1)un-1} \circ \cdots  \circ h_{u2-u1} \circ h_{u2-e-i\theta1u1},$$
Hợp thành của 2n - $2$ siêu phẳng (hyperplane) các phép đối xứng. Nói chung, nếu $f \in$ U(n), bởi nhận xét sau Định lý 28.2, $f$ có thể được viết dưới dạng $f = \rho_{\theta}  \circ g$, ở đâu $g \in$ SU(n) là phép quay, và $\rho_{\theta}$ là Hermite phép đối xứng (reflection). Ta kết luận bằng cách áp dụng những gì ta chỉ được chứng minh đến $g$. Như hệ quả của Định lý 28.5, sau đây thú vị kết quả có thể được được hiển thị (điều này là không khó, thực hiện nó!). Thứ nhất, nhắc lại rằng ánh xạ tuyến tính (linear map) $f$: $E \to E$ là tự liên hợp (self-adjoint) (hoặc Hermite) khi và chỉ khi $f = f^{*}$. Thì, nhóm con của U(n) được sinh bởi Hermite các phép đẳng cự bằng nhóm
$$SU(n)^{\pm}= {f \in U(n) | \det(f) = \pm 1}.$$
Tương đương, $SU(n)^{\pm}$ bằng nhóm con của U(n) được sinh bởi siêu phẳng (hyperplane) các phép đối xứng. bài toán này đã có đã được trái mở bởi Dieudonn´e trong $[49]$. Evidently, nó đã là settled vì publication của thứ ba ấn bản của cuốn sách $[49]$. Inspection của chứng minh của Mệnh đề 27.4 reveals rằng mệnh đề này cũng nghiệm đúng cho Các không gian Hermite. Do đó, khi $n \ge 3$, hợp thành của bất kỳ hai siêu phẳng (hyperplane) các phép đối xứng bằng hợp thành của hai flips. Hệ quả là, phiên bản của Định lý 27.5 nghiệm đúng cho các phép quay trong Không gian Hermite (Hermitian space) có số chiều ít nhất $3$.

> **Định lý 28.6.** Cho $E$ là Hermitan không gian có số chiều $n \ge 3$. Mọi phép quay $f \in$ SU(E) là hợp thành của chẵn/ngay cả số của flips $f = f_{2k}\circ \cdots \circ f_{1}$, ở đâu $k \le$ n-1. Hơn nữa, nếu $u \neq  0$ là bất biến dưới $f$ (i.e. $u \in$ Ker $(f$ - id)), ta có thể chọn cuối cùng flip $f_{2k}$ sao cho $u \in F_{2k}^{\perp}$, ở đâu $F_{2k}$ là không gian con có số chiều $n$ - $2$ xác định $f_{2k}$.

*Chứng minh.* Nó là đồng nhất đến rằng của Định lý 27.5, ngoại trừ rằng nó sử dụng Định lý 28.5 thay vì của Định lý 27.1. phần thứ hai của Mệnh đề cũng nghiệm đúng, bởi vì nếu u̸ $= 0$ là vectơ riêng (eigenvector) của $f$ cho $1$, thì $u$ là một của các vectơ trong cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors) được sử dụng trong 28.2. chi tiết là để lại như một bài tập. Ta bây giờ chỉ ra rằng Phân rã QR (QR-decomposition) theo (phức) Householder các ma trận nghiệm đúng cho phức các ma trận. Ta cần phiên bản của Mệnh đề 28.1 và mẹo/kỹ thuật tại kết thúc/cuối của lập luận, nhưng chứng minh là basically unchanged.

<!-- PAGE 1005 -->

> **Mệnh đề 28.7.** Cho $E$ là không tầm thường Không gian Hermite (Hermitian space) có số chiều $n$. Cho trước bất kỳ cơ sở trực chuẩn (orthonormal basis) $(e_{1}, \dots  , e_{n})$, với mọi bộ $n$ của các vectơ $(v_{1}, \dots  , v_{n})$, có một dãy của $n$ - $1$ các phép đẳng cự $h_{1}, \dots  , h_{n-1}$, sao cho $h_{i}$ là siêu phẳng (hyperplane) phép đối xứng (reflection) hoặc đồng nhất thức, và nếu $(r_{1}, \dots  , r_{n})$ là các vectơ cho trước bởi
$$r_{j} = h_{n-1} \circ \cdots  \circ h_{2} \circ h_{1}(v_{j})1 \le j \le n,$$
Thì mọi $r_{j}$ là tổ hợp tuyến tính (linear combination) của các vectơ $(e_{1}, \dots  , e_{j}), (1 \le j \le n)$. Tương đương, ma trận $R$ có các cột là các thành phần của $r_{j}$ trên cơ sở (basis) $(e_{1}, \dots  , e_{n})$ là tam giác trên (upper triangular) ma trận. Hơn nữa, nếu ta cho phép một nhiều hơn/thêm phép đẳng cự (isometry) $h_{n}$ của tạo thành
$$h_{n} = \rho_{en, \phi n}  \circ \cdots  \circ \rho_{e1,\phi1}$$
Sau $h_{1}, \dots  , h_{n-1}$, ta có thể đảm bảo rằng đường chéo các phần tử (entries) của $R$ là không âm.

*Chứng minh.* chứng minh là rất đồng dạng đến chứng minh của Mệnh đề 13.3, nhưng nó cần được sửa đổi little bit vì Mệnh đề 28.1 là weaker hơn Mệnh đề 13.2. Ta giải thích cách mà đến sửa đổi quy nạp bước, để lại base trường hợp và rest của chứng minh như một bài tập. Như trong chứng minh của Mệnh đề 13.3, các vectơ $(e_{1}, \dots  , e_{k})$ tạo thành cơ sở (basis) cho không gian con được ký hiệu như $U_{k}'$, các vectơ $(e_{k+1}, \dots  , e_{n})$ tạo thành cơ sở (basis) cho không gian con được ký hiệu như $U_{k}''$, các không gian con $U_{k}'$ và $U_{k}''$ là trực giao, và $E = U_{k}' \oplus U_{k}''$. Cho
$$u_{k+1} = h_{k} \circ \cdots  \circ h_{2} \circ h_{1}(v_{k+1}).$$
Ta có thể viết
$$u_{k+1} = u_{k+1}' + u_{k+1}'',$$
Ở đâu $u_{k+1}' \in U_{k}'$ và $u_{k+1}'' \in U_{k}''$. Cho
$$r_{k+1,k+1} =

$u_{k+1}''$

$,ande^{i\theta k+1}|u_{k+1}'' \cdot  e_{k+1}| = u_{k+1}'' \cdot  e_{k+1}.$$$ If $u_{k+1}'' = e^{i\theta k+1}r_{k+1,k+1} e_{k+1}$, we let $h_{k+1} =$ id. Otherwise, by Proposition 28.1, there is a unique hyperplane reflection $h_{k+1}$ sao cho
$$h_{k+1}(u_{k+1}'') = e^{i\theta k+1}r_{k+1,k+1} e_{k+1},$$
Ở đâu $h_{k+1}$ là phép đối xứng (reflection) về siêu phẳng (hyperplane) $H_{k+1}$ trực giao đến vectơ
$$w_{k+1} = r_{k+1,k+1} e_{k+1} -e^{-i\theta k+1}u_{k+1}''.$$
Tại kết thúc/cuối của quy nạp, ta có tam giác ma trận $R$, nhưng đường chéo các phần tử (entries) $e^{i\theta j}r_{j, j}$ của $R$ có thể là phức. Đặt
$$h_{n+1} = \rho_{en,-\theta n}  \circ \cdots  \circ \rho_{e1,-\theta1} ,$$
Ta nhận thấy rằng đường chéo các phần tử (entries) của ma trận của các vectơ
$$r_{j}' = h_{n+1} \circ h_{n} \circ \cdots  \circ h_{2} \circ h_{1}(v_{j})$$
Là tam giác với không âm các phần tử (entries).
