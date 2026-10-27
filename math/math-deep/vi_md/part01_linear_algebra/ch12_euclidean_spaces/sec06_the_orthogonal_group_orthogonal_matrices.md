# Trực giao Nhóm, Các ma trận trực giao


<!-- PAGE 482 -->
(ii) implication rằng $(3)$ suy ra $(1)$ nghiệm đúng nếu ta cũng giả sử rằng $f$ là toàn ánh (surjective), chẵn/ngay cả nếu $E$ có vô hạn số chiều. Trong $(2)$, khi $f$ thực hiện không thỏa mãn điều kiện f(0) $= 0$, chứng minh chỉ ra rằng $f$ là ánh xạ afin (affine map). Thật vậy, lấy bất kỳ vectơ $\tau$ như gốc, ánh xạ $g$ là tuyến tính, và
$$f(\tau  + u) = f(\tau ) + g(u)for all u \in E.$$
Theo Mệnh đề 24.7, điều này chỉ ra rằng $f$ là afin với liên kết ánh xạ tuyến tính (linear map) $g$. sự kiện này là worth recording như sau đây mệnh đề.

> **Mệnh đề 12.13.** Cho trước bất kỳ hai không tầm thường Các không gian Euclid $E$ và $F$ của cùng hữu hạn số chiều $n$, với mọi hàm $f$: $E \to F$, nếu
$$\|f(v) -f(u)\|= \|v -u\|for all u, v \in E,$$
Thì $f$ là ánh xạ afin (affine map), và của nó liên kết ánh xạ tuyến tính (linear map) $g$ là phép đẳng cự (isometry). Xét theo Mệnh đề 12.12, ta thường abbreviate “tuyến tính phép đẳng cự (isometry)” như “phép đẳng cự (isometry),” trừ khi ta muốn đến emphasize rằng ta là dealing với ánh xạ giữa các không gian vectơ. Ta là bây giờ đi đến lấy closer nhìn tại các phép đẳng cự $f$: $E \to E$ của Không gian Euclid (Euclidean space) của hữu hạn số chiều.

## 12.6 Trực giao Nhóm, Các ma trận trực giao

Trong mục này ta explore một số của cơ bản các tính chất của trực giao nhóm và của các ma trận trực giao.

> **Mệnh đề 12.14.** Cho $E$ là bất kỳ Không gian Euclid (Euclidean space) của hữu hạn số chiều $n$, và cho $f$: $E \to E$ là bất kỳ ánh xạ tuyến tính (linear map). Các tính chất sau đây đúng:
$(1)$ ánh xạ tuyến tính (linear map) $f$: $E \to E$ là phép đẳng cự (isometry) khi và chỉ khi
$$f \circ f^{*} = f^{*} \circ f = id.$$
$(2)$ Với mọi cơ sở trực chuẩn (orthonormal basis) $(e_{1}, \dots  , e_{n})$ của $E$, nếu ma trận của $f$ là $A$, thì ma trận của $f^{*}$ là chuyển vị (transpose) $A^{\top}$ của $A$, và $f$ là phép đẳng cự (isometry) khi và chỉ khi $A$ thỏa mãn các đồng nhất thức
$$A A^{\top}= A^{\top}A = I_{n},$$
Ở đâu $I_{n}$ ký hiệu ma trận đơn vị (identity matrix) của thứ tự $n$, khi và chỉ khi các cột của $A$ tạo thành cơ sở trực chuẩn (orthonormal basis) của $\mathbb{R}^{n}$, khi và chỉ khi các hàng của $A$ tạo thành cơ sở trực chuẩn (orthonormal basis) của $\mathbb{R}^{n}$.

<!-- PAGE 483 -->

*Chứng minh.* $(1)$ ánh xạ tuyến tính (linear map) $f$: $E \to E$ là phép đẳng cự (isometry) khi và chỉ khi
$$f(u) \cdot  f(v) = u \cdot  v,$$
Với mọi $u, v \in E$, khi và chỉ khi
$$f^{*} (f(u)) \cdot  v = f(u) \cdot  f(v) = u \cdot  v$$
Với mọi $u, v \in E$, mà suy ra
$$(f^{*} (f(u)) -u) \cdot  v = 0$$
Với mọi $u, v \in E$. Vì tích vô hướng (inner product) là xác định dương (positive definite), ta phải có
$$f^{*} (f(u)) -u = 0$$
Với mọi $u \in E$, nghĩa là,
$$f^{*} \circ f = id.$$
Nhưng tự đồng cấu $f$ của không gian vectơ hữu hạn chiều rằng có nghịch đảo trái (left inverse) là đẳng cấu, do đó $f \circ f^{*} =$ id. điều ngược lại được thiết lập bởi thực hiện ở trên các bước backward.
$(2)$ Nếu $(e_{1}, \dots  , e_{n})$ là cơ sở trực chuẩn (orthonormal basis) cho $E$, cho $A = (a_{i j})$ là ma trận của $f$, và cho $B = (b_{i j})$ là ma trận của $f^{*}$. Vì $f^{*}$ được đặc trưng hóa bởi
$$f^{*} (u) \cdot  v = u \cdot  f(v)$$
Với mọi $u, v \in E$, bằng cách sử dụng sự kiện rằng nếu $w = w_{1}e_{1} + \cdots  + w_{n}e_{n}$ ta có $w_{k} = w \cdot  e_{k}$ với mọi $k, 1 \le k \le n$, đặt $u = e_{i}$ và $v = e_{j}$, ta thu được
$$b_{j i} = f^{*} (e_{i}) \cdot  e_{j} = e_{i} \cdot  f(e_{j}) = a_{i j},$$
Với mọi $i, j, 1 \le i, j \le n$. Do đó, $B = A^{\top}$. Bây giờ nếu $X$ và $Y$ là tùy ý các ma trận trên cơ sở (basis) $(e_{1}, \dots  , e_{n})$, ký hiệu như thông thường cột thứ $j$ của $X$ bởi $X^{j}$, và tương tự cho $Y$, đơn giản phép tính chỉ ra rằng
$$X^{\top}Y = (X^{i}\cdot  Y^{j})_{1\le i,j\le n}.$$
Thì ta kiểm chứng được ngay rằng nếu $X = Y = A$, thì
$$A^{\top}A = A A^{\top}= I_{n}$$
Khi và chỉ khi các vectơ cột $(A^{1}, \dots  , A^{n})$ tạo thành cơ sở trực chuẩn (orthonormal basis). Do đó, từ $(1)$, ta xem rằng
$(2)$ là rõ ràng (cũng bởi vì các hàng của $A$ là các cột của $A^{\top})$. Mệnh đề 12.14 chỉ ra rằng nghịch đảo của phép đẳng cự (isometry) $f$ là của nó liên hợp (adjoint) $f^{*}$. Nhắc lại rằng tập hợp tất cả thực $n \times  n$ các ma trận được ký hiệu bởi $M_{n}(\mathbb{R})$. Mệnh đề 12.14 cũng motivates sau đây định nghĩa.

> **Định nghĩa 12.6.** thực $n \times  n$ ma trận là ma trận trực giao (orthogonal matrix) nếu
$$A A^{\top}= A^{\top}A = I_{n}.$$
