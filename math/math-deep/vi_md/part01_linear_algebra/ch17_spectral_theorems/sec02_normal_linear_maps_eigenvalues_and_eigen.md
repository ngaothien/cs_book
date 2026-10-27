# Chuẩn tắc/bình thường Các ánh xạ tuyến tính (linear maps): Các trị riêng (eigenvalues) và Các vectơ riêng (eigenvectors)


<!-- PAGE 625 -->
Chương $17$ Các định lý phổ trong Euclidean và Các không gian Hermite

## 17.1 Giới thiệu

Mục tiêu của điều này chương là để chỉ ra rằng có đẹp chuẩn tắc/bình thường các dạng cho các ma trận đối xứng, các ma trận phản đối xứng, các ma trận trực giao, và các ma trận chuẩn tắc. định lý phổ (spectral theorem) cho các ma trận đối xứng phát biểu rằng các ma trận đối xứng có thực các trị riêng (eigenvalues) và rằng chúng có thể được được chéo hóa trên cơ sở trực chuẩn (orthonormal basis). định lý phổ (spectral theorem) cho Các ma trận Hermite phát biểu rằng Các ma trận Hermite cũng có thực các trị riêng (eigenvalues) và rằng chúng có thể được được chéo hóa trên phức cơ sở trực chuẩn (orthonormal basis). Chuẩn tắc/bình thường thực các ma trận có thể được khối được chéo hóa trên cơ sở trực chuẩn (orthonormal basis) với các khối có kích thước nhiều nhất hai và có refinements của điều này chuẩn tắc/bình thường tạo thành cho phản đối xứng và các ma trận trực giao. spectral kết quả cho thực các ma trận đối xứng có thể được được sử dụng để chứng minh hai các đặc trưng của các trị riêng (eigenvalues) của ma trận đối xứng (symmetric matrix) theo Rayleigh tỉ số. thứ nhất đặc trưng là Rayleigh–Ritz định lý và thứ hai một là Courant–Fischer định lý. Cả hai các kết quả được sử dụng trong tối ưu hóa lý thuyết và để thu được các kết quả về perturbing các trị riêng (eigenvalues) của ma trận đối xứng (symmetric matrix). Trong chương này tất cả các không gian vectơ là hữu hạn chiều thực hoặc phức các không gian vectơ.

## 17.2 Chuẩn tắc/bình thường Các ánh xạ tuyến tính (linear maps): Các trị riêng (eigenvalues) và Eigenvec-

$$tors$$
Ta bắt đầu bởi studying chuẩn tắc/bình thường các ánh xạ, đến understand cấu trúc của các trị riêng (các trị riêng (eigenvalues)) của chúng và các vectơ riêng (eigenvectors). Điều này mục và tiếp theo ba đã là inspired bởi Lang $[113]$, Artin $[7]$, Mac Lane và Birkhoff[122], Berger $[11]$, và Bertin $[15]$.
$$625$$

<!-- PAGE 626 -->

> **Định nghĩa 17.1.** Cho trước Euclidean hoặc Không gian Hermite (Hermitian space) $E$, ánh xạ tuyến tính (linear map) $f$: $E \to E$ là chuẩn tắc/bình thường nếu
$$f \circ f^{*} = f^{*} \circ f.$$
Ánh xạ tuyến tính (linear map) $f$: $E \to E$ là tự liên hợp (self-adjoint) nếu $f = f^{*}$, phản tự liên hợp (skew-self-adjoint) nếu $f = -f^{*}$, và trực giao nếu $f \circ f^{*} = f^{*} \circ f =$ id. Hiển nhiên, tự liên hợp (self-adjoint), phản tự liên hợp (skew-self-adjoint), hoặc trực giao ánh xạ tuyến tính (linear map) là chuẩn tắc/bình thường ánh xạ tuyến tính (linear map). Của ta thứ nhất mục tiêu là để chỉ ra rằng với mọi chuẩn tắc/bình thường ánh xạ tuyến tính (linear map) $f$: $E \to E$, có một cơ sở trực chuẩn (orthonormal basis) (w.r.t. $\langle$ -, $-\rangle$) sao cho ma trận của $f$ trên cơ sở (cơ sở (basis)) này có especially đẹp tạo thành: nó là khối ma trận đường chéo (diagonal matrix) trong mà các khối là hoặc một chiều các ma trận (i.e., đơn lẻ các phần tử (entries)) hoặc hai chiều các ma trận của tạo thành
$$\begin{pmatrix} \lambda & \mu \\ -\mu & \lambda \end{pmatrix} .$$
Điều này chuẩn tắc/bình thường tạo thành có thể được further refined nếu $f$ là tự liên hợp (self-adjoint), phản tự liên hợp (skew-self-adjoint), hoặc trực giao. Như bước thứ nhất ta chỉ ra rằng $f$ và $f^{*}$ có cùng hạt nhân (kernel) khi $f$ là chuẩn tắc/bình thường.

> **Mệnh đề 17.1.** Cho trước Không gian Euclid (Euclidean space) $E$, nếu $f$: $E \to E$ là chuẩn tắc/bình thường ánh xạ tuyến tính (linear map), thì Ker $f =$ Ker $f^{*}$.

*Chứng minh.* Thứ nhất cho chúng ta chứng minh rằng
$$\langle f(u), f(v)\rangle = \langle f^{*} (u), f^{*} (v)\rangle$$
Với mọi $u, v \in E$. Vì $f^{*}$ là liên hợp (adjoint) của $f$ và $f \circ f^{*} = f^{*} \circ f$, ta có
$$\langle f(u), f(u)\rangle = \langle u, (f^{*} \circ f)(u)\rangle ,$$
$$= \langle u, (f \circ f^{*} )(u)\rangle ,$$
$$= \langle f^{*} (u), f^{*} (u)\rangle .$$
Vì $\langle$ -, $-\rangle$ là xác định dương (positive definite),
$$\langle f(u), f(u)\rangle = 0ifff(u) = 0,$$
$$\langle f^{*} (u), f^{*} (u)\rangle = 0ifff^{*} (u) = 0,$$
Và vì
$$\langle f(u), f(u)\rangle = \langle f^{*} (u), f^{*} (u)\rangle ,$$
Ta có
$$f(u) = 0ifff^{*} (u) = 0.$$
Hệ quả là, Ker $f =$ Ker $f^{*}$.

<!-- PAGE 627 -->
Giả sử một lần nữa rằng $E$ là Không gian Hermite (Hermitian space), nhận thấy rằng Mệnh đề 17.1 cũng nghiệm đúng. Ta suy ra sau đây hệ quả.

> **Mệnh đề 17.2.** Cho trước Không gian Hermite (Hermitian space) $E$, với mọi chuẩn tắc/bình thường ánh xạ tuyến tính (linear map) $f$: $E \to E$, ta có Ker $(f) \cap$ Im(f) $= (0)$.

*Chứng minh.* Giả sử $v \in$ Ker $(f) \cap$ Im(f), mà có nghĩa là $v =$ f(u) với một số $u \in E$, và f(v) $= 0$. Theo Mệnh đề 17.1, Ker $(f) =$ Ker $(f^{*}$), do đó f(v) $= 0$ suy ra rằng $f^{*} (v) = 0$. Hệ quả là,
$$0 = \langle f^{*} (v), u\rangle$$
$$= \langle v, f(u)\rangle$$
$$= \langle v, v\rangle ,$$
Và do đó, $v = 0$. Ta cũng có sau đây then chốt mệnh đề relating các trị riêng (eigenvalues) của $f$ và $f^{*}$.

> **Mệnh đề 17.3.** Cho trước Không gian Hermite (Hermitian space) $E$, với mọi chuẩn tắc/bình thường ánh xạ tuyến tính (linear map) $f$: $E \to E$, vectơ $u$ là vectơ riêng (eigenvector) của $f$ cho trị riêng (eigenvalue) $\lambda$ (trong $\mathbb{C})$ khi và chỉ khi $u$ là vectơ riêng (eigenvector) của $f^{*}$ cho trị riêng (eigenvalue) $\overline{\lambda}$.

*Chứng minh.* Thứ nhất ta kiểm chứng được ngay rằng liên hợp (adjoint) của $f$ - $\lambda$ id là $f^{*}$ - $\overline{\lambda}$ id. Hơn nữa, $f$ - $\lambda$ id là chuẩn tắc/bình thường. Thật vậy,
$$(f -\lambda  id) \circ (f -\lambda  id)^{*}= (f -\lambda  id) \circ (f^{*} -\overline{\lambda} id),$$
$$= f \circ f^{*} -\overline{\lambda f} -\lambda f^{*} +\overline{\lambda \lambda} id,$$
$$= f^{*} \circ f -\lambda f^{*} -\overline{\lambda f} +\overline{\lambda \lambda} id,$$
$$= (f^{*} -\overline{\lambda} id) \circ (f -\lambda  id),$$
$$= (f -\lambda  id)^{*}\circ (f -\lambda  id).$$
Áp dụng Mệnh đề 17.1 đến $f$ - $\lambda$ id, với mọi khác không vectơ $u$, ta xem rằng
$$(f -\lambda  id)(u) = 0iff(f^{*} -\overline{\lambda} id)(u) = 0,$$
Mà là chính xác phát biểu của mệnh đề. tiếp theo mệnh đề chỉ ra rất quan trọng tính chất của chuẩn tắc/bình thường các ánh xạ tuyến tính (linear maps): các vectơ riêng (eigenvectors) tương ứng với phân biệt các trị riêng (eigenvalues) là trực giao.

> **Mệnh đề 17.4.** Cho trước Không gian Hermite (Hermitian space) $E$, với mọi chuẩn tắc/bình thường ánh xạ tuyến tính (linear map) $f$: $E \to E$, nếu $u$ và $v$ là các vectơ riêng (eigenvectors) của $f$ liên kết với các trị riêng (eigenvalues) $\lambda$ và $\mu$ (trong $\mathbb{C})$ ở đâu $\lambda  \neq  \mu$, thì $\langle u, v\rangle = 0$.

<!-- PAGE 628 -->

*Chứng minh.* Cho chúng ta tính $\langle$ f(u), $v\rangle$ trong hai khác nhau các cách. Vì $v$ là vectơ riêng (eigenvector) của $f$ cho $\mu$, theo Mệnh đề 17.3, $v$ là cũng vectơ riêng (eigenvector) của $f^{*}$ cho $\overline{\mu}$, và ta có
$$\langle f(u), v\rangle = \langle \lambda u, v\rangle = \lambda \langle u, v\rangle ,$$
Và
$$\langle f(u), v\rangle = \langle u, f^{*} (v)\rangle = \langle \overline{u, \mu v}\rangle = \mu \langle u, v\rangle ,$$
Ở đâu cuối cùng đồng nhất thức nghiệm đúng bởi vì của semilinearity trong thứ hai lập luận. Do đó
$$\lambda \langle u, v\rangle = \mu \langle u, v\rangle ,$$
Rằng là,
$$(\lambda  -\mu )\langle u, v\rangle = 0,$$
Mà suy ra rằng $\langle u, v\rangle = 0$, vì $\lambda  \neq  \mu$. Ta có thể chỉ ra dễ dàng rằng các trị riêng (eigenvalues) của tự liên hợp (self-adjoint) ánh xạ tuyến tính (linear map) là thực.

> **Mệnh đề 17.5.** Cho trước Không gian Hermite (Hermitian space) $E$, tất cả các trị riêng (eigenvalues) của bất kỳ tự liên hợp (self-adjoint) ánh xạ tuyến tính (linear map) $f$: $E \to E$ là thực.

*Chứng minh.* Cho $z$ (trong $\mathbb{C})$ là trị riêng (eigenvalue) của $f$ và cho $u$ là vectơ riêng (eigenvector) cho $z$. Ta tính $\langle$ f(u), $u\rangle$ trong hai khác nhau các cách. Ta có
$$\langle f(u), u\rangle = \langle zu, u\rangle = z\langle u, u\rangle ,$$
Và vì $f = f^{*}$, ta cũng có
$$\langle f(u), u\rangle = \langle u, f^{*} (u)\rangle = \langle u, f(u)\rangle = \langle u, zu\rangle =\overline{z}\langle u, u\rangle .$$
Do đó,
$$z\langle u, u\rangle =\overline{z}\langle u, u\rangle ,$$
Mà suy ra rằng $z =\overline{z}$, vì $u \neq  0$, và $z$ là thật vậy thực. Ở đó là cũng phiên bản của Mệnh đề 17.5 cho (thực) Không gian Euclid (Euclidean space) $E$ và tự liên hợp (self-adjoint) ánh xạ $f$: $E \to E$ vì mọi thực không gian vectơ (vector space) $E$ có thể được được nhúng vào phức không gian vectơ (vector space) $E_{C}$, và mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$ có thể được được mở rộng đến ánh xạ tuyến tính (linear map) $f_{C}$: $E_{C} \to E_{C}$.

> **Định nghĩa 17.2.** Cho trước thực không gian vectơ (vector space) $E$, cho $E_{C}$ là cấu trúc $E \times  E$ dưới phép cộng phép toán
$$(u_{1}, u_{2}) + (v_{1}, v_{2}) = (u_{1} + v_{1}, u_{2} + v_{2}),$$
Và cho phép nhân bởi phức vô hướng (scalar) $z = x +$ iy được định nghĩa sao cho
$$(x + iy) \cdot  (u, v) = (xu -yv, yu + xv).$$
Không gian $E_{C}$ được gọi là phức hóa của $E$.

<!-- PAGE 629 -->
Dễ dàng chứng minh được rằng cấu trúc $E_{C}$ là phức không gian vectơ (vector space). Nó là cũng immediate rằng
$$(0, v) = i(v, 0),$$
Và do đó, đồng nhất $E$ với không gian con của $E_{C}$ bao gồm của tất cả các vectơ của tạo thành $(u, 0)$, ta có thể viết
$$(u, v) = u + iv.$$
Nhận thấy rằng nếu $(e_{1}, \dots  , e_{n})$ là cơ sở (basis) của $E$ (thực không gian vectơ (vector space)), thì $(e_{1}, \dots  , e_{n})$ là cũng cơ sở (basis) của $E_{C}$ (nhắc lại rằng $e_{i}$ là abbreviation cho $(e_{i}, 0))$. ánh xạ tuyến tính (linear map) $f$: $E \to E$ được mở rộng đến ánh xạ tuyến tính (linear map) $f_{C}$: $E_{C} \to E_{C}$ được định nghĩa sao cho
$$f_{C}(u + iv) = f(u) + if(v).$$
Với mọi cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $E$, ma trận M(f) biểu diễn $f$ trên $(e_{1}, \dots  , e_{n})$ là đồng nhất đến ma trận $M(f_{C})$ biểu diễn $f_{C}$ trên $(e_{1}, \dots  , e_{n})$, ở đâu ta quan điểm $(e_{1}, \dots  , e_{n})$ như cơ sở (basis) của $E_{C}$. Hệ quả là, det(zI - M(f)) $=$ det(zI - $M(f_{C}))$, mà có nghĩa là $f$ và $f_{C}$ có cùng đa thức đặc trưng (characteristic polynomial) (mà có thực các hệ số). Ta biết rằng mọi đa thức của bậc $n$ với thực (hoặc phức) các hệ số luôn luôn có $n$ phức các nghiệm (counted với của chúng bội (multiplicity)), và các nghiệm của det(zI $-M(f_{C}))$ rằng là thực (nếu bất kỳ) là các trị riêng (eigenvalues) của $f$. Tiếp theo ta cần để mở rộng tích vô hướng (inner product) trên $E$ đến tích vô hướng (inner product) trên $E_{C}$. tích vô hướng (inner product) $\langle$ -, $-\rangle$ trên Không gian Euclid (Euclidean space) $E$ được mở rộng đến Hermite xác định dương (positive definite) tạo thành $\langle$ -, $-\rangle_{C}$ trên $E_{C}$ như sau:
$$\langle u_{1} + iv_{1}, u_{2} + iv_{2}\rangle_{C}  = \langle u_{1}, u_{2}\rangle + \langle v_{1}, v_{2}\rangle + i(\langle v_{1}, u_{2}\rangle -\langle u_{1}, v_{2}\rangle ).$$
Dễ dàng kiểm chứng được rằng $\langle$ -, $-\rangle_{C}$ là thật vậy Hermite tạo thành rằng là xác định dương (positive definite), và rõ ràng là $\langle$ -, $-\rangle_{C}$ agrees với $\langle$ -, $-\rangle$ trên thực các vectơ. Thì cho trước bất kỳ ánh xạ tuyến tính (linear map) $f$: $E \to E$, dễ dàng kiểm chứng được rằng ánh xạ $f_{C}^{*}$ được định nghĩa sao cho
$$f_{C}^{*} (u + iv) = f^{*}(u) + if^{*}(v)$$
Với mọi $u, v \in E$ là liên hợp (adjoint) của $f_{C}$ w.r.t. $\langle$ -, $-\rangle_{C}$.

> **Mệnh đề 17.6.** Cho trước Không gian Euclid (Euclidean space) $E$, nếu $f$: $E \to E$ là bất kỳ tự liên hợp (self-adjoint) ánh xạ tuyến tính (linear map), thì mọi trị riêng (eigenvalue) $\lambda$ của $f_{C}$ là thực và là thực sự trị riêng (eigenvalue) của $f$ (mà có nghĩa là tồn tại một thực vectơ riêng (eigenvector) $u \in E$ sao cho f(u) $= \lambda u)$. Vì vậy, tất cả các trị riêng (eigenvalues) của $f$ là thực.

<!-- PAGE 630 -->

*Chứng minh.* Cho $E_{C}$ là phức hóa của $E, \langle$ -, $-\rangle_{C}$ phức hóa của tích vô hướng (inner product) $\langle$ -, $-\rangle$ trên $E$, và $f_{C}$: $E_{C} \to E_{C}$ phức hóa của $f$: $E \to E$. Theo định nghĩa của $f_{C}$ và $\langle$ -, $-\rangle_{C}$, nếu $f$ là tự liên hợp (self-adjoint), ta có $\langle f_{C}(u_{1} + iv_{1}), u_{2} + iv_{2}\rangle_{C}  = \langle f(u_{1}) + if(v_{1}), u_{2} + iv_{2}\rangle_{C}$
$$= \langle f(u_{1}), u_{2}\rangle + \langle f(v_{1}), v_{2}\rangle + i(\langle u_{2}, f(v_{1})\rangle -\langle f(u_{1}), v_{2}\rangle )$$
$$= \langle u_{1}, f(u_{2})\rangle + \langle v_{1}, f(v_{2})\rangle + i(\langle f(u_{2}), v_{1}\rangle -\langle u_{1}, f(v_{2})\rangle )$$
$$= \langle u_{1} + iv_{1}, f(u_{2}) + if(v_{2})\rangle_{C}$$
$$= \langle u_{1} + iv_{1}, f_{C}(u_{2} + iv_{2})\rangle_{C} ,$$
Mà chỉ ra rằng $f_{C}$ là cũng tự liên hợp (self-adjoint) đối với $\langle$ -, $-\rangle_{C}$. Như ta được điểm ra trước đó, $f$ và $f_{C}$ có cùng đa thức đặc trưng (characteristic polynomial) $det(zI-f_{C}) =$ det(zI - $f)$, mà là đa thức với thực các hệ số. Mệnh đề 17.5 chỉ ra rằng các không điểm của det(zI - $f_{C}) =$ det(zI - $f)$ là tất cả thực, và với mỗi thực không $\lambda$ của det(zI - $f)$, ánh xạ tuyến tính (linear map) $\lambda$ id - $f$ là suy biến, mà có nghĩa là tồn tại một khác không $u \in E$ sao cho f(u) $= \lambda u$. Vì vậy, tất cả các trị riêng (eigenvalues) của $f$ là thực.

> **Mệnh đề 17.7.** Cho trước Không gian Hermite (Hermitian space) $E$, với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$, nếu $f$ là skewself-adjoint, thì $f$ có các trị riêng (eigenvalues) rằng là thuần túy imaginary hoặc không, và nếu $f$ là unita, thì $f$ có các trị riêng (eigenvalues) của tuyệt đối giá trị $1$.

*Chứng minh.* Nếu $f$ là phản tự liên hợp (skew-self-adjoint), $f^{*} = -f$, và thì bởi định nghĩa của liên hợp (adjoint) ánh xạ, với mọi trị riêng (eigenvalue) $\lambda$ và bất kỳ vectơ riêng (eigenvector) $u$ liên kết với $\lambda$, ta có
$$\lambda \langle u, u\rangle = \langle \lambda u, u\rangle = \langle f(u), u\rangle = \langle u, f^{*} (u)\rangle = \langle u, -f(u)\rangle = -\langle u, \lambda u\rangle = -\overline{\lambda}\langle u, u\rangle ,$$
Và vì $u \neq  0$ và $\langle$ -, $-\rangle$ là xác định dương (positive definite), $\langle u, u\rangle$ ̸ $= 0$, do đó
$$\lambda  = -\overline{\lambda ,}$$
Mà chỉ ra rằng $\lambda  =$ ir với một số $r \in \mathbb{R}$. Nếu $f$ là unita, thì $f$ là phép đẳng cự (isometry), do đó với mọi trị riêng (eigenvalue) $\lambda$ và bất kỳ vectơ riêng (eigenvector) $u$ liên kết với $\lambda$, ta có
$$|\lambda |^{2}\langle u, u\rangle =\overline{\lambda \lambda}\langle u, u\rangle = \langle \lambda u, \lambda u\rangle = \langle f(u), f(u)\rangle = \langle u, u\rangle ,$$
Và vì $u \neq  0$, ta thu được $|\lambda |^{2} = 1$, mà suy ra
$$|\lambda | = 1.$$
