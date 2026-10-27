# Unita Nhóm, Các ma trận unita


<!-- PAGE 545 -->
Các nhận xét:
$(i)$ Trong Euclidean trường hợp, ta được chứng minh rằng giả định
$$\|f(v) -f(u)\|= \|v -u\|for all u, v \in E and f(0) = 0(2')$$
Suy ra $(3)$. Cho điều này ta được sử dụng phân cực đồng nhất thức
$$2u \cdot  v = \|u\|^{2}+ \|v\|^{2}-\|u -v\|^{2}.$$
Trong Hermite trường hợp phân cực đồng nhất thức liên quan đến phức số $i$. Thực ra, implication (2') suy ra $(3)$ là sai trong Hermite trường hợp! Liên hợp $z \mapsto \overline{z}$ thỏa mãn (2') vì
$$|\overline{z}_{2} -\overline{z}_{1}| = |\overline{z}_{2}\overline{-}\overline{z}_{1}| = |z_{2} -z_{1}|,$$
Và vẫn chưa, nó là không tuyến tính!
(ii) Nếu ta sửa đổi $(2)$ bởi thay đổi điều kiện thứ hai bởi bây giờ đòi hỏi rằng ở đó là một số $\tau  \in E$ sao cho
$$f(\tau  + iu) = f(\tau ) + i(f(\tau  + u) -f(\tau ))$$
Với mọi $u \in E$, thì hàm $g: E \to E$ được định nghĩa sao cho
$$g(u) = f(\tau  + u) -f(\tau )$$
Thỏa mãn old các điều kiện của $(2)$, và implications $(2) \to (3)$ và $(3) \to (1)$ chứng minh rằng $g$ là tuyến tính, và do đó rằng $f$ là afin. Xét theo thứ nhất nhận xét, một số điều kiện liên quan đến $i$ là cần thiết trên $f$, ngoài sự kiện rằng $f$ là distance-preserving.

## 14.4 Unita Nhóm, Các ma trận unita

Trong mục này, như mirror ảnh (image) của của ta treatment của các phép đẳng cự của Không gian Euclid (Euclidean space), ta explore một số của cơ bản các tính chất của unita nhóm và của các ma trận unita. Như immediate hệ quả của Gram–Schmidt trực chuẩn hóa quy trình, ta thu được Phân rã QR (QR-decomposition) cho các ma trận khả nghịch. Trong Hermite khung lý thuyết, ma trận của liên hợp (adjoint) của ánh xạ tuyến tính (linear map) là không cho trước bởi chuyển vị (transpose) của ban đầu ma trận, nhưng bởi liên hợp của ban đầu ma trận. Cho độc giả’s convenience ta nhắc lại sau đây các định nghĩa từ Mục 9.2.

> **Định nghĩa 14.8.** Cho trước phức $m \times  n$ ma trận $A$, chuyển vị (transpose) $A^{\top}$ của $A$ là $n \times  m$
$$matrix A^{\top}= \begin{pmatrix} a_{i j}^{\top} \end{pmatrix} defined such that$$
$$a_{i j}^{\top} = a_{j i},$$
Và liên hợp $\overline{A}$ của $A$ là ma trận cỡ $m \times  n$ $\overline{A} = (b_{i j})$ được định nghĩa sao cho
$$b_{i j} =\overline{a}_{i j}$$
Với mọi $i, j, 1 \le i \le m, 1 \le j \le n$. liên hợp (adjoint) $A^{*}$ của $A$ là ma trận được định nghĩa sao cho
$$A^{*}\overline{= (}\overline{A}^{\top}\overline{) =} \begin{pmatrix}\end{pmatrix} \overline{A}^{\top}.$$

<!-- PAGE 546 -->

> **Mệnh đề 14.15.** Cho $E$ là bất kỳ Không gian Hermite (Hermitian space) của hữu hạn số chiều $n$, và cho $f$: $E \to E$ là bất kỳ ánh xạ tuyến tính (linear map). Các tính chất sau đây đúng:
$(1)$ ánh xạ tuyến tính (linear map) $f$: $E \to E$ là phép đẳng cự (isometry) khi và chỉ khi
$$f \circ f^{*} = f^{*} \circ f = id.$$
$(2)$ Với mọi cơ sở trực chuẩn (orthonormal basis) $(e_{1}, \dots  , e_{n})$ của $E$, nếu ma trận của $f$ là $A$, thì ma trận của $f^{*}$ là liên hợp (adjoint) $A^{*}$ của $A$, và $f$ là phép đẳng cự (isometry) khi và chỉ khi $A$ thỏa mãn các đồng nhất thức
$$A A^{*}= A^{*}A = I_{n},$$
Ở đâu $I_{n}$ ký hiệu ma trận đơn vị (identity matrix) của thứ tự $n$, khi và chỉ khi các cột của $A$ tạo thành cơ sở trực chuẩn (orthonormal basis) của $\mathbb{C}^{n}$, khi và chỉ khi các hàng của $A$ tạo thành cơ sở trực chuẩn (orthonormal basis) của $\mathbb{C}^{n}$.

*Chứng minh.* $(1)$ chứng minh là đồng nhất đến rằng của Mệnh đề 12.14 $(1)$.
$(2)$ Nếu $(e_{1}, \dots  , e_{n})$ là cơ sở trực chuẩn (orthonormal basis) cho $E$, cho $A = (a_{i j})$ là ma trận của $f$, và cho $B = (b_{i j})$ là ma trận của $f^{*}$. Vì $f^{*}$ được đặc trưng hóa bởi
$$f^{*} (u) \cdot  v = u \cdot  f(v)$$
Với mọi $u, v \in E$, bằng cách sử dụng sự kiện rằng nếu $w = w_{1}e_{1} + \cdots  + w_{n}e_{n}$, ta có $w_{k} = w \cdot  e_{k}$, với mọi $k, 1 \le k \le n$; đặt $u = e_{i}$ và $v = e_{j}$, ta thu được
$$b_{j i} = f^{*} (e_{i}) \cdot  e_{j} = e_{i} \cdot  f(e_{j}) =\overline{f}\overline{(}\overline{e}_{j}\overline{)}\overline{\cdot}\overline{e}_{i} =\overline{a}_{i j},$$
Với mọi $i, j, 1 \le i, j \le n$. Do đó, $B = A^{*}$. Bây giờ nếu $X$ và $Y$ là tùy ý các ma trận trên cơ sở (basis) $(e_{1}, \dots  , e_{n})$, ký hiệu như thông thường cột thứ $j$ của $X$ bởi $X^{j}$, và tương tự cho $Y$, đơn giản phép tính chỉ ra rằng
$$Y^{*}X = (X^{j}\cdot  Y^{i})_{1\le i,j\le n}.$$
Thì ta kiểm chứng được ngay rằng nếu $X = Y = A$, thì $A^{*}A = A A^{*} = I_{n}$ khi và chỉ khi các vectơ cột $(A^{1}, \dots  , A^{n})$ tạo thành cơ sở trực chuẩn (orthonormal basis). Do đó, từ $(1)$, ta xem rằng $(2)$ là rõ ràng. Mệnh đề 12.14 chỉ ra rằng nghịch đảo của phép đẳng cự (isometry) $f$ là của nó liên hợp (adjoint) $f^{*}$. Mệnh đề 12.14 cũng motivates sau đây định nghĩa.

> **Định nghĩa 14.9.** phức $n \times  n$ ma trận là ma trận unita (unitary matrix) nếu
$$A A^{*}= A^{*}A = I_{n}.$$
Các nhận xét:

<!-- PAGE 547 -->
$(1)$ các điều kiện $A A^{*} = I_{n}, A^{*}A = I_{n}$, và $A^{-1} = A^{*}$ là tương đương. Cho trước bất kỳ hai các cơ sở trực chuẩn $(u_{1}, \dots  , u_{n})$ và $(v_{1}, \dots  , v_{n})$, nếu $P$ là ma trận chuyển cơ sở (change of basis matrix) từ $(u_{1}, \dots  , u_{n})$ đến $(v_{1}, \dots  , v_{n})$, nó là dễ để chỉ ra rằng ma trận $P$ là unita. chứng minh của Mệnh đề 14.14 $(3)$ cũng chỉ ra rằng nếu $f$ là phép đẳng cự (isometry), thì ảnh (image) của cơ sở trực chuẩn (orthonormal basis) $(u_{1}, \dots  , u_{n})$ là cơ sở trực chuẩn (orthonormal basis).
$(2)$ Bằng cách sử dụng tường minh công thức cho định thức (determinant), ta xem ngay lập tức rằng
$$\det(\overline{A}\overline{) = \det(}\overline{A}\overline{)}.$$
Nếu $f$ là unita phép biến đổi và $A$ là ma trận của nó đối với bất kỳ cơ sở trực chuẩn (orthonormal basis), từ $AA^{*} =$ I, ta thu được
$$\det(AA^{*}) = \det(A) \det(A^{*}) = \det(A\overline{)\det(}\overline{A}^{\top}\overline{) = \det(} A\overline{)\det(}\overline{A}\overline{) =} | \det(A)|^{2},$$
Và do đó | det()| $= 1$. Rõ ràng là các phép đẳng cự của Không gian Hermite (Hermitian space) có số chiều $n$ tạo thành nhóm, và rằng các phép đẳng cự của định thức (determinant) $+1$ tạo thành nhóm con. Điều này dẫn đến đến sau đây định nghĩa.

> **Định nghĩa 14.10.** rất quan trọng ví dụ của các ma trận unita là miễn là/được cung cấp bởi Fourier các ma trận (sai khác
$$\sqrt$$
Nhân tử của $\overline{n})$, các ma trận rằng phát sinh trong khác nhau các phiên bản của rời rạc Fourier biến đổi. Cho nhiều hơn/thêm trên điều này topic, xem các bài tập, và Strang $[175, 178]$. nhóm SU(2) hóa ra là nhóm của các quaternion đơn vị, invented bởi Hamilton. nhóm này đóng quan trọng vai trò trong biểu diễn của các phép quay trong Do đó(3) được sử dụng trong máy tính đồ họa và rô-bốt học; xem Chương $16$. Bây giờ rằng ta có định nghĩa của ma trận unita (unitary matrix), ta có thể giải thích cách mà Gram– Schmidt trực chuẩn hóa quy trình ngay lập tức cho ta Phân rã QR (QR-decomposition) cho các ma trận.

> **Định nghĩa 14.11.** Cho trước bất kỳ phức $n\times n$ ma trận $A$, Phân rã QR (QR-decomposition) của $A$ là bất kỳ cặp của $n \times  n$ các ma trận $(U, R)$, ở đâu $U$ là ma trận unita (unitary matrix) và $R$ là tam giác trên (upper triangular) ma trận sao cho $A = UR$.

> **Mệnh đề 14.16.** Cho trước bất kỳ $n \times  n$ phức ma trận $A$, nếu $A$ là khả nghịch, thì có một ma trận unita (unitary matrix) $U$ và tam giác trên (upper triangular) ma trận $R$ với dương đường chéo các phần tử (entries) sao cho $A = UR$. chứng minh là một cách tuyệt đối cùng như trong thực trường hợp!
Nhận xét: Nếu $A$ là khả nghịch và nếu $A = U_{1}R_{1} = U_{2}R_{2}$ là hai QR-decompositions cho $A$, thì
$$R_{1}R_{2}^{-1}= U_{1}^{*} U_{2}.$$
