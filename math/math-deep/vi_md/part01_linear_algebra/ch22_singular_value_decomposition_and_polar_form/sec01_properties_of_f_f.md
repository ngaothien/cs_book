# Các tính chất của f*f


<!-- PAGE 747 -->
Chương $22$ Phân rã giá trị kỳ dị (SVD) và Dạng cực (polar form)

## 22.1 Các tính chất của f * \circ f

Trong mục này ta giả sử rằng ta là dealing với thực Các không gian Euclid. Cho $f$: $E \to E$ là bất kỳ ánh xạ tuyến tính (linear map). Nói chung, nó có thể không là khả dĩ/có thể đến diagonalize $f$. Ta chỉ ra rằng mọi ánh xạ tuyến tính (linear map) có thể được được chéo hóa nếu ta là sẽ để sử dụng hai các cơ sở trực chuẩn. Điều này là celebrated phân rã giá trị kỳ dị (SVD) (SVD). close cousin của SVD là dạng cực (polar form) của ánh xạ tuyến tính (linear map), mà chỉ ra cách mà ánh xạ tuyến tính (linear map) có thể được decomposed vào của nó một cách thuần túy rotational thành phần (perhaps với flip) và của nó một cách thuần túy stretching phần. then chốt nhận xét là rằng $f^{*} \circ f$ là tự liên hợp (self-adjoint) vì
$$\langle (f^{*} \circ f)(u), v\rangle = \langle f(u), f(v)\rangle = \langle u, (f^{*} \circ f)(v)\rangle .$$
Tương tự, $f \circ f^{*}$ là tự liên hợp (self-adjoint). sự kiện rằng $f^{*} \circ f$ và $f \circ f^{*}$ là tự liên hợp (self-adjoint) là rất quan trọng, bởi vì theo Định lý 17.8, nó suy ra rằng $f^{*} \circ f$ và $f \circ f^{*}$ có thể được được chéo hóa và rằng chúng có thực các trị riêng (eigenvalues). Thực ra, các trị riêng (các trị riêng (eigenvalues)) này là tất cả không âm như được hiển thị trong sau đây mệnh đề.

> **Mệnh đề 22.1.** các trị riêng (eigenvalues) của $f^{*} \circ f$ và $f \circ f^{*}$ là không âm.

*Chứng minh.* Nếu $u$ là vectơ riêng (eigenvector) của $f^{*} \circ f$ cho trị riêng (eigenvalue) $\lambda$, thì
$$\langle (f^{*} \circ f)(u), u\rangle = \langle f(u), f(u)\rangle$$
Và
$$\langle (f^{*} \circ f)(u), u\rangle = \lambda \langle u, u\rangle ,$$
Và do đó
$$\lambda \langle u, u\rangle = \langle f(u), f(u)\rangle ,$$
Mà suy ra rằng $\lambda  \ge 0$, vì $\langle$ -, $-\rangle$ là xác định dương (positive definite). đồng dạng chứng minh áp dụng đến $f \circ f^{*}$.
$$747$$

<!-- PAGE 748 -->
Do đó, các trị riêng (eigenvalues) của $f^{*} \circ f$ là của tạo thành $\sigma_{1}^{2} , \dots  , \sigma_{r}^{2}$ hoặc $0$, ở đâu $\sigma_{i}  > 0$, và tương tự cho $f \circ f^{*}$. ở trên considerations cũng áp dụng đến bất kỳ ánh xạ tuyến tính (linear map) $f$: $E \to F$ giữa hai Các không gian Euclid $(E, \langle$ -, $-\rangle_{1}$) và $(F, \langle$ -, $-\rangle_{2}$). Nhắc lại rằng liên hợp (adjoint) $f^{*}$: $F \to E$ của $f$ là duy nhất ánh xạ tuyến tính (linear map) $f^{*}$ sao cho
$$\langle f(u), v\rangle_{2}  = \langle u, f^{*} (v)\rangle_{1} ,for all u \in E and all v \in F.$$
Thì $f^{*} \circ f$ và $f \circ f^{*}$ là tự liên hợp (self-adjoint) (chứng minh là cùng như trong trước đó trường hợp), và các trị riêng (eigenvalues) của $f^{*} \circ f$ và $f \circ f^{*}$ là không âm.

*Chứng minh.* Nếu $\lambda$ là trị riêng (eigenvalue) của $f^{*} \circ f$ và $u (\neq  0)$ là tương ứng vectơ riêng (eigenvector), ta có
$$\langle (f^{*} \circ f)(u), u\rangle_{1}  = \langle f(u), f(u)\rangle_{2} ,$$
Và cũng
$$\langle (f^{*} \circ f)(u), u\rangle_{1}  = \lambda \langle u, u\rangle_{1} ,$$
Do đó
$$\lambda \langle u, u\rangle_{1} , = \langle f(u), f(u)\rangle_{2} ,$$
Mà suy ra rằng $\lambda  \ge 0$. đồng dạng chứng minh áp dụng đến $f \circ f^{*}$. tình huống là chẵn/ngay cả tốt hơn, vì ta sẽ chỉ ra một cách ngắn rằng $f^{*} \circ f$ và $f \circ f^{*}$ có cùng khác không các trị riêng (eigenvalues).
Nhận xét: Cho trước bất kỳ hai các ánh xạ tuyến tính (linear maps) $f$: $E \to F$ và $g: F \to E$, ở đâu dim(E) $= n$ và dim(F) $= m$, nó có thể được được hiển thị rằng
$$\lambda^{m} \det(\lambda  I_{n} -g \circ f) = \lambda^{n} \det(\lambda  I_{m} -f \circ g),$$
Và do đó $g \circ f$ và $f \circ g$ luôn luôn có cùng khác không các trị riêng (eigenvalues); xem Bài toán 15.14.

> **Định nghĩa 22.1.** Cho trước bất kỳ ánh xạ tuyến tính (linear map) $f$: $E \to F$, square các nghiệm $\sigma_{i}  > 0$ của dương các trị riêng (eigenvalues) của $f^{*} \circ f$ (và $f \circ f^{*}$) được gọi là các giá trị kỳ dị (singular values) của $f$.

> **Định nghĩa 22.2.** tự liên hợp (self-adjoint) ánh xạ tuyến tính (linear map) $f$: $E \to E$ có các trị riêng (eigenvalues) là không âm được gọi là nửa xác định dương (positive semidefinite) (hoặc dương), và nếu $f$ là cũng khả nghịch, $f$ được nói là xác định dương (positive definite). Trong latter trường hợp, mọi trị riêng (eigenvalue) của $f$ là chặt dương. sau đây mệnh đề chỉ ra rằng các điều kiện trên các trị riêng (eigenvalues) của tự liên hợp (self-adjoint) ánh xạ tuyến tính (linear map) được sử dụng để định nghĩa khái niệm của xác định dương (positive definite) ánh xạ tuyến tính (linear map) là tương đương đến điều kiện được sử dụng trong Định nghĩa 8.4. đồng dạng nhưng weaker điều kiện là tương đương đến khái niệm của tự liên hợp (self-adjoint) nửa xác định dương (positive semidefinite) ánh xạ tuyến tính (linear map).

> **Mệnh đề 22.2.** Cho $f$: $E \to E$ là tự liên hợp (self-adjoint) ánh xạ tuyến tính (linear map), ở đâu $E$ là Không gian Euclid (Euclidean space) của hữu hạn số chiều với tích vô hướng (inner product) $\langle -.-\rangle$.

<!-- PAGE 749 -->
$(1)$ các trị riêng (eigenvalues) của $f$ là chặt dương khi và chỉ khi
$$\langle f(u), u\rangle > 0for all u \neq  0.$$
$(2)$ các trị riêng (eigenvalues) của $f$ là không âm khi và chỉ khi
$$\langle f(u), u\rangle \ge 0for all u \neq  0.$$

*Chứng minh.* Vì $f$ là tự liên hợp (self-adjoint), bởi định lý phổ (spectral theorem) (Định lý 17.8), $f$ có thực các trị riêng (eigenvalues) $\lambda_{1} , \dots  , \lambda_{n}$, và tồn tại một cơ sở trực chuẩn (orthonormal basis) $(e_{1}, \dots  , e_{n})$, ở đâu $e_{i}$ là vectơ riêng (eigenvector) cho $\lambda_{i}$. Đối với cơ sở (cơ sở (basis)) này, mọi vectơ $u \in E$ có thể được được viết trong duy nhất cách như
$$u = \sum_{i}  n=1 x_{i}u_{i} for some x_{i} \in \mathbb{R}. Since each e_{i} is eigenvector associated with \lambda_{i}  \in \mathbb{R}, we have$$
$$f \begin{pmatrix} x_{i}e_{i} \end{pmatrix} \sum_{i=1}^{n}  = \sum_{i=1}^{n}  x_{i}f(e_{i}) = \sum_{i=1}^{n}  \lambda_{i} x_{i}e_{i},$$
Và bằng cách sử dụng tính song tuyến tính của tích vô hướng (inner product), ta có
$$*+$$
$$\langle f(u), u\rangle =f \begin{pmatrix} x_{i}e_{i} \end{pmatrix} \sum_{i=1}^{n}  , \sum_{j=1}^{n}  x_{j}e_{j}$$
$$=* \sum_{i=1}^{n}  \lambda_{i} x_{i}e_{i}, \sum_{j=1}^{n}  x_{j}e_{j}+$$
$$= \sum_{i=1j}^{n}  \sum_{=1}^{n}  \lambda_{i} x_{i}x_{j}\langle e_{i}, e_{j}\rangle ,$$
Và vì $(e_{1}, \dots  , e_{n})$, là cơ sở trực chuẩn (orthonormal basis), ta thu được
$$\langle f(u), u\rangle = \sum_{i=1}^{n}  \lambda_{i} x_{i}^{2} .(\dagger )$$
$(1)$ Nếu $\lambda_{i}  > 0$ cho $i = 1, \dots  , n$, với mọi $u \neq  0$, ta có $x_{i} \neq  0$ với một số $i$, do đó $\langle$ f(u), $u\rangle =$
$$\sum_{i}  n=1 \lambda_{i} x_{i}^{2} > 0.$$
Ngược lại, nếu $\langle$ f(u), $u\rangle > 0$ với mọi $u \neq  0$, bởi chọn $u = e_{i}$, ta thu được
$$\langle f(e_{i}), e_{i}\rangle = \langle \lambda_{i} e_{i}, e_{i}\rangle = \lambda_{i} \langle e_{i}, e_{i}\rangle = \lambda_{i} ,$$
Do đó $\lambda_{i}  > 0$ cho $i = 1, \dots  , n$.
$$(2) If \lambda_{i}  \ge 0 for i = 1, \dots  , n, for any u \neq  0, then \langle f(u), u\rangle = \sum_{i}  n=1 \lambda_{i} x_{i}^{2} \ge 0.$$
Ngược lại, nếu $\langle$ f(u), $u\rangle \ge 0$ với mọi $u \neq  0$, bởi chọn $u = e_{i}$, ta thu được
$$\langle f(e_{i}), e_{i}\rangle = \langle \lambda_{i} e_{i}, e_{i}\rangle = \lambda_{i} \langle e_{i}, e_{i}\rangle = \lambda_{i} ,$$
Do đó $\lambda_{i}  \ge 0$ cho $i = 1, \dots  , n$.

<!-- PAGE 750 -->
Mệnh đề 22.2 cũng nghiệm đúng cho tự liên hợp (self-adjoint) các ánh xạ tuyến tính (linear maps) trên phức không gian vectơ (vector space) với Hermite tích vô hướng (inner product). chứng minh là về cơ bản cùng và là để lại như một bài tập đến độc giả. phiên bản của Mệnh đề 22.2 cho các ma trận suy ra ngay lập tức.

> **Mệnh đề 22.3.** Cho $A$ là thực $n \times  n$ ma trận đối xứng (symmetric matrix).
$(1)$ các trị riêng (eigenvalues) của $A$ là chặt dương khi và chỉ khi
$$u^{\top}Au > 0for all u \neq  0.$$
$(2)$ các trị riêng (eigenvalues) của $A$ là không âm khi và chỉ khi
$$u^{\top}Au \ge 0for all u \neq  0.$$
Nó là quan trọng đến lưu ý rằng Mệnh đề 22.3 là sai cho nonsymmetric các ma trận.

> **Ví dụ 22.1.** ma trận
$$A = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$$
Có dương các trị riêng (eigenvalues) $(1, 1)$, nhưng
$$\begin{pmatrix} 1 & -1 \end{pmatrix} \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \end{pmatrix} \begin{pmatrix} -3 \\ -1 \end{pmatrix} = -2.$$

> **Ví dụ 22.2.** ma trận
$$A = \begin{pmatrix} 1 & -2 \\ 2 & 1 \end{pmatrix}$$
Có phức các trị riêng (eigenvalues) $1 +$ 2i, $1$ - 2i, và vẫn chưa
$$\begin{pmatrix} x & y \end{pmatrix} \begin{pmatrix} 1 & -2 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x & y \end{pmatrix} \begin{pmatrix} x -2y \\ 2x + y \end{pmatrix} = x^{2}+ y^{2},$$
Do đó $u^{\top}Au > 0$ với mọi $u \neq  0$. Vì $u^{\top}Au$ là vô hướng (scalar), nếu $A$ là skew ma trận đối xứng (symmetric matrix) $(A^{\top} = -A)$, thì ta xem rằng
$$u^{\top}Au = 0for all u \in \mathbb{R}.$$
Vì vậy, nếu $A$ là thực $n \times  n$ ma trận thì
$$u^{\top}Au = u^{\top}H(A)ufor all u \in \mathbb{R},$$
Ở đâu H() $= (1/2)(A + A^{\top})$ là đối xứng phần của $A$. Điều này các giải thích tại sao khái niệm của xác định dương (positive definite) ma trận là chỉ thú vị cho các ma trận đối xứng. Nhưng nhưng một nên cũng là biết rằng chẵn/ngay cả nếu nonsymmetric ma trận $A$ có “well-behaved” các trị riêng (eigenvalues), của nó đối xứng phần H() có thể không là xác định dương (positive definite).

<!-- PAGE 751 -->

> **Ví dụ 22.3.** ma trận
$$A = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$$
Của Ví dụ 22.1 có dương các trị riêng (eigenvalues) $(1, 1)$, nhưng của nó đối xứng phần
$$H(A) = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$$
Là không xác định dương (positive definite), vì các trị riêng (các trị riêng (eigenvalues)) của nó là $-1, 3$. Beware rằng nếu $A$ là phức ma trận phản Hermite (skew-Hermitian matrix), mà có nghĩa là $A^{*} = -A$, thì
$$(u^{*}Au)^{*}= -u^{*}Au,$$
Nhưng điều này chỉ suy ra rằng thực phần của $u^{*}Au$ là không. Do đó với mọi tùy ý phức ma trận vuông (square matrix) $A$, nói chung,
$$u^{*}Au \neq  u^{*}H(A)u,$$
Ở đâu H() $= (1/2)(A + A^{*})$. Nếu $f$: $E \to F$ là bất kỳ ánh xạ tuyến tính (linear map), ta chỉ đã chỉ ra rằng $f^{*} \circ f$ và $f \circ f^{*}$ là nửa xác định dương (positive semidefinite) tự liên hợp (self-adjoint) các ánh xạ tuyến tính (linear maps). sự kiện này có đáng chú ý hệ quả rằng mọi ánh xạ tuyến tính (linear map) có hai quan trọng các phân rã: $1$. dạng cực (polar form). $2$. phân rã giá trị kỳ dị (SVD) (SVD). wonderful thing về phân rã giá trị kỳ dị (SVD) là rằng ở đó tồn tại hai các cơ sở trực chuẩn $(u_{1}, \dots  , u_{n})$ và $(v_{1}, \dots  , v_{m})$ sao cho, đối với các phần tử này các cơ sở, $f$ là ma trận đường chéo (diagonal matrix) bao gồm của các giá trị kỳ dị (singular values) của $f$ hoặc $0$. Do đó, trong một số nghĩa, $f$ có thể luôn luôn được chéo hóa đối với hai các cơ sở trực chuẩn. SVD là cũng hữu ích công cụ cho việc giải quá xác định các hệ phương trình tuyến tính trong bình phương tối thiểu (least squares) nghĩa và cho dữ liệu giải tích/phân tích, như ta chỉ ra sau này. Thứ nhất ta chỉ ra một số hữu ích relationships giữa các hạt nhân và các ảnh của $f, f^{*} , f^{*} \circ f$, và $f \circ f^{*}$. Nhắc lại rằng nếu $f$: $E \to F$ là ánh xạ tuyến tính (linear map), ảnh (image) Im $f$ của $f$ là không gian con f(E) của $F$, và hạng (rank) của $f$ là số chiều dim(Im $f)$ của ảnh (ảnh (image)) của nó. Cũng nhắc lại rằng (Định lý 6.16)
$$\dim (\mathrm{Ker} f) + \dim (\mathrm{Im} f) = \dim (E),$$
Và rằng (Các mệnh đề 12.11 và 14.13) với mọi không gian con $W$ của $E$,
$$\dim (W) + \dim (W^{\perp} ) = \dim (E).$$

<!-- PAGE 752 -->

> **Mệnh đề 22.4.** Cho trước bất kỳ hai Các không gian Euclid $E$ và $F$, ở đâu $E$ có số chiều $n$ và $F$ có số chiều $m$, với mọi ánh xạ tuyến tính (linear map) $f$: $E \to F$, ta có
$$\mathrm{Ker} f = \mathrm{Ker} (f^{*} \circ f),$$
$$\mathrm{Ker} f^{*} = \mathrm{Ker} (f \circ f^{*} ),$$
$$\mathrm{Ker} f = (\mathrm{Im} f^{*} )^{\perp},$$
$$\mathrm{Ker} f^{*} = (\mathrm{Im} f)^{\perp},$$
$$\dim(\mathrm{Im} f) = \dim(\mathrm{Im} f^{*} ),$$
Và $f, f^{*} , f^{*} \circ f$, và $f \circ f^{*}$ có cùng hạng (rank).

*Chứng minh.* để đơn giản hóa ký hiệu, ta sẽ ký hiệu trong các tích trên $E$ và $F$ bởi cùng ký hiệu $\langle$ -, $-\rangle$ (để tránh các chỉ số dưới). Nếu f(u) $= 0$, thì $(f^{*} \circ$ f)(u) $= f^{*}$ (f(u)) $= f^{*} (0) = 0$, và do đó Ker $f \subseteq$ Ker $(f^{*} \circ f)$. Theo định nghĩa của $f^{*}$, ta có
$$\langle f(u), f(u)\rangle = \langle (f^{*} \circ f)(u), u\rangle$$
Với mọi $u \in E$. Nếu $(f^{*} \circ$ f)(u) $= 0$, vì $\langle$ -, $-\rangle$ là xác định dương (positive definite), ta phải có f(u) $= 0$, và do đó Ker $(f^{*} \circ f) \subseteq$ Ker $f$. Vì vậy,
$$\mathrm{Ker} f = \mathrm{Ker} (f^{*} \circ f).$$
Chứng minh rằng Ker $f^{*} =$ Ker $(f \circ f^{*}$) là đồng dạng. Theo định nghĩa của $f^{*}$, ta có
$$\langle f(u), v\rangle = \langle u, f^{*} (v)\rangle for all u \in E and all v \in F.(*)$$
Điều này ngay lập tức suy ra rằng
$$\mathrm{Ker} f = (\mathrm{Im} f^{*} )^{\perp}andKer f^{*} = (\mathrm{Im} f)^{\perp}.$$
Cho chúng ta giải thích tại sao Ker $f =$ (Im $f^{*} )^{\perp}$, chứng minh của khác phương trình đang là đồng dạng. Bởi vì tích vô hướng (inner product) là xác định dương (positive definite), với mọi $u \in E$, ta có $\bullet  u \in$ Ker $f \bullet$ khi và chỉ khi f(u) $= 0 \bullet$ khi và chỉ khi $\langle$ f(u), $v\rangle = 0$ với mọi $v, \bullet$ bởi (*) khi và chỉ khi $\langle u, f^{*} (v)\rangle = 0$ với mọi $v, \bullet$ khi và chỉ khi $u \in$ (Im $f^{*} )^{\perp}$.
