# Hermite Các phép đối xứng và Phân rã QR (QR-decomposition)


<!-- PAGE 548 -->
Thì nó là dễ để chỉ ra rằng có một ma trận đường chéo (diagonal matrix) $D$ với đường chéo các phần tử (entries) sao cho $|d_{ii}| = 1$ cho $i = 1, \dots  , n$, và $U_{2} = U_{1}D, R_{2} = D^{*}R_{1}$. Ta có kết quả sau phiên bản của Hadamard bất đẳng thức cho phức các ma trận. chứng minh là về cơ bản cùng như trong Euclidean trường hợp nhưng nó sử dụng Mệnh đề 14.16 thay vì của Mệnh đề 12.16.

> **Mệnh đề 14.17.** (Hadamard) Với mọi phức $n \times  n$ ma trận $A = (a_{ij})$, ta có
$$1/21/2$$
$$| \det(A)| \le \prod_{i=1}^{n}  \begin{pmatrix} |a_{ij}|^{2} \end{pmatrix} \sum_{j=1}^{n}  and| \det(A)| \le \prod_{j=1}^{n}  \begin{pmatrix} |a_{ij}|^{2} \end{pmatrix} \sum_{i=1}^{n}  .$$
Hơn thế nữa, đẳng thức nghiệm đúng khi và chỉ khi hoặc $A$ có trực giao các hàng trong trái bất đẳng thức hoặc trực giao các cột trong phải bất đẳng thức. Ta cũng có sau đây phiên bản của Mệnh đề 12.18 cho Các ma trận Hermite. chứng minh của Mệnh đề 12.18 đi qua bởi vì Phân rã Cholesky (Cholesky decomposition) cho Hermite xác định dương (positive definite) $A$ ma trận nghiệm đúng trong tạo thành $A = B^{*}B$, ở đâu $B$ là tam giác trên (upper triangular) với dương đường chéo các phần tử (entries). chi tiết là trái đến độc giả.

> **Mệnh đề 14.18.** (Hadamard) Với mọi phức $n\times n$ ma trận $A = (a_{ij})$, nếu $A$ là Hermite nửa xác định dương (positive semidefinite), thì ta có
$$\det(A) \le \prod_{i=1}^{n}  a_{ii}.$$
Hơn thế nữa, nếu $A$ là xác định dương (positive definite), thì đẳng thức nghiệm đúng khi và chỉ khi $A$ là ma trận đường chéo (diagonal matrix).

## 14.5 Hermite Các phép đối xứng và Phân rã QR (QR-decomposition)

Nếu $A$ là $n \times  n$ phức ma trận suy biến (singular matrix), tồn tại một (không nhất thiết duy nhất) QRdecomposition $A = QR$ với $Q$ ma trận unita (unitary matrix) mà là tích của Householder các phép đối xứng và $R$ tam giác trên (upper triangular) ma trận, nhưng chứng minh là nhiều hơn/thêm liên quan. Một cách đến tiến hành là đến tổng quát hóa khái niệm của siêu phẳng (hyperplane) phép đối xứng (reflection). Điều này là không một cách thực đáng ngạc nhiên vì trong Hermite trường hợp có suy rộng/không thực sự các phép đẳng cự có định thức (determinant) có thể được bất kỳ unit phức số. Siêu phẳng (hyperplane) các phép đối xứng là suy rộng/tổng quát hóa như sau.

> **Định nghĩa 14.12.** Cho $E$ là Không gian Hermite (Hermitian space) của hữu hạn số chiều. Với mọi siêu phẳng (hyperplane) $H$, với mọi khác không vectơ $w$ trực giao đến $H$, sao cho $E = H \oplus G$, ở đâu $G =\mathbb{C} w$, Hermite phép đối xứng (reflection) về $H$ của góc $\theta$ là ánh xạ tuyến tính (linear map) của tạo thành $\rho_{H, \theta}$: $E \to E$, được định nghĩa sao cho
$$\rho_{H, \theta} (u) = p_{H}(u) + e^{i\theta}p_{G}(u),$$
$$̸$$
Với mọi unit phức số $e^{i\theta} = 1$ (i.e. $\theta$ ̸ $= k2\pi$). Với mọi khác không vectơ $w \in E$, ta ký hiệu bởi $\rho_{w,\theta}$ Hermite phép đối xứng (reflection) cho trước bởi $\rho_{H,\theta}$, ở đâu $H$ là siêu phẳng (hyperplane) trực giao đến $w$.

<!-- PAGE 549 -->
Vì $u = p_{H}(u) + p_{G}(u)$, Hermite phép đối xứng (reflection) $\rho_{w, \theta}$ cũng được biểu diễn như
$$\rho_{w, \theta} (u) = u + (e^{i\theta}-1)p_{G}(u),$$
Hoặc như
$$1)  \cdot$$
$$\rho_{w, \theta} (u) = u + (e^{i\theta}- \frac{(u w)}{\|w\|^{2}} w.$$
Lưu ý rằng trường hợp của tiêu chuẩn siêu phẳng (hyperplane) phép đối xứng (reflection) là thu được khi $e^{i\theta} = -1$, i.e., $\theta  = \pi$. Trong trường hợp này,
$$2  \cdot$$
$$\rho_{w, \pi} (u) = u - \frac{(u w)}{\|w\|^{2}} w,$$
Và ma trận của như vậy phép đối xứng (reflection) là Ma trận Householder, như trong Mục 13.1, ngoại trừ rằng $w$ có thể là phức vectơ. Ta để lại như dễ bài tập để kiểm tra rằng $\rho_{w, \theta}$ là thật vậy phép đẳng cự (isometry), và rằng nghịch đảo của $\rho_{w, \theta}$ là $\rho_{w,-\theta}$. Nếu ta chọn cơ sở trực chuẩn (orthonormal basis) $(e_{1}, \dots  , e_{n})$ sao cho $(e_{1}, \dots  , e_{n-1})$ là cơ sở trực chuẩn (orthonormal basis) của $H$, ma trận của $\rho_{w, \theta}$ là
$$\begin{pmatrix} I_{n-1} & 0 \\ 0 & e^{i\theta} \end{pmatrix}$$
Ta bây giờ đến đến chính surprise. Cho trước bất kỳ hai phân biệt các vectơ $u$ và $v$ sao cho $\|u\| = \|v\|$, ở đó isn’t luôn luôn siêu phẳng (hyperplane) phép đối xứng (reflection) ánh xạ $u$ đến $v$, nhưng điều này có thể được được thực hiện bằng cách sử dụng hai Hermite các phép đối xứng!

> **Mệnh đề 14.19.** Cho $E$ là bất kỳ không tầm thường Không gian Hermite (Hermitian space).
$(1)$ Với mọi hai các vectơ $u, v \in E$ sao cho $u \neq  v$ và $\|u\| = \|v\|$, nếu $u \cdot  v = e^{i\theta}|u \cdot$ v|, thì (thông thường) phép đối xứng (reflection) $s$ về siêu phẳng (hyperplane) trực giao đến vectơ $v$ - $e^{-i\theta}u$ là sao cho s(u) $= e^{i\theta}v$.
$(2)$ Với mọi khác không vectơ $v \in E$, với mọi unit phức số $e^{i\theta} \neq  1$, có một Hermite phép đối xứng (reflection) $\rho_{v,\theta}$ sao cho
$$\rho_{v,\theta} (v) = e^{i\theta}v.$$
Hệ quả là, cho $u$ và $v$ như trong $(1)$, ta có $\rho_{v,-\theta}  \circ$ s(u) $= v$.

*Chứng minh.* $(1)$ Xét (thông thường) phép đối xứng (reflection) về siêu phẳng (hyperplane) trực giao đến $w = v -e^{-i\theta}u$. Ta có
$$2  \cdot  -$$
$$s(u) = u - \frac{(u (ve^{-i\theta}u))}{\|v -e^{-i\theta}u\|^{2}} (v -e^{-i\theta}u).$$
Ta cần để tính
$$-2u \cdot  (v -e^{-i\theta}u)and(v -e^{-i\theta}u) \cdot  (v -e^{-i\theta}u).$$

<!-- PAGE 550 -->
Vì $u \cdot  v = e^{i\theta}|u \cdot$ v|, ta có
$$e^{-i\theta}u \cdot  v = |u \cdot  v|ande^{i\theta}v \cdot  u = |u \cdot  v|.$$
Bằng cách sử dụng ở trên và sự kiện rằng $\|u\| = \|v\|$, ta thu được
$$-2u \cdot  (v -e^{-i\theta}u) = 2e^{i\theta}\|u\|^{2}-2u \cdot  v,$$
$$= 2e^{i\theta}(\|u\|^{2}-|u \cdot  v|),$$
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

<!-- PAGE 551 -->
$(2)$ Nhất định các tác giả, chẳng hạn như Kincaid và Cheney $[105]$ và Ciarlet $[41]$, sử dụng vectơ $u + e^{i\theta}v$ thay vì của vectơ $v + e^{-i\theta}u$. effect của điều này lựa chọn là rằng chúng cũng thu được s(u) $= -e^{i\theta}v$.
$(3)$ Nếu $v = \|u\|e_{1}$, ở đâu $e_{1}$ là cơ sở (basis) vectơ, $u \cdot  e_{1} = a_{1}$, ở đâu $a_{1}$ là chỉ hệ số của $u$ trên cơ sở (basis) vectơ $e_{1}$. Thì, vì $u \cdot  e_{1} = e^{i\theta}|a_{1}|$, lựa chọn của cộng dấu trong vectơ $\|u\|e_{1} + e^{-i\theta}u$ có effect rằng hệ số của vectơ này trên $e_{1}$ là $\|u\| + |a_{1}|$, và không có cancellations lấy place, mà được ưu tiên hơn cho số tính ổn định (ta cần đến chia bởi square chuẩn (norm) của vectơ này). Ta bây giờ chỉ ra rằng Phân rã QR (QR-decomposition) theo (phức) Householder các ma trận nghiệm đúng cho phức các ma trận. Ta cần phiên bản của Mệnh đề 14.19 và mẹo/kỹ thuật tại kết thúc/cuối của lập luận, nhưng chứng minh là basically unchanged.

> **Mệnh đề 14.20.** Cho $E$ là không tầm thường Không gian Hermite (Hermitian space) có số chiều $n$. Cho trước bất kỳ cơ sở trực chuẩn (orthonormal basis) $(e_{1}, \dots  , e_{n})$, với mọi bộ $n$ của các vectơ $(v_{1}, \dots  , v_{n})$, có một dãy của $n$ - $1$ các phép đẳng cự $h_{1}, \dots  , h_{n-1}$, sao cho $h_{i}$ là (tiêu chuẩn) siêu phẳng (hyperplane) phép đối xứng (reflection) hoặc đồng nhất thức, và nếu $(r_{1}, \dots  , r_{n})$ là các vectơ cho trước bởi
$$r_{j} = h_{n-1} \circ \cdots  \circ h_{2} \circ h_{1}(v_{j}),1 \le j \le n,$$
Thì mọi $r_{j}$ là tổ hợp tuyến tính (linear combination) của các vectơ $(e_{1}, \dots  , e_{j}), (1 \le j \le n)$. Tương đương, ma trận $R$ có các cột là các thành phần của $r_{j}$ trên cơ sở (basis) $(e_{1}, \dots  , e_{n})$ là tam giác trên (upper triangular) ma trận. Hơn nữa, nếu ta cho phép một nhiều hơn/thêm phép đẳng cự (isometry) $h_{n}$ của tạo thành
$$h_{n} = \rho_{en, \phi n}  \circ \cdots  \circ \rho_{e1,\phi1}$$
Sau $h_{1}, \dots  , h_{n-1}$, ta có thể đảm bảo rằng đường chéo các phần tử (entries) của $R$ là không âm.

*Chứng minh.* chứng minh là rất đồng dạng đến chứng minh của Mệnh đề 13.3, nhưng nó cần được sửa đổi little bit vì Mệnh đề 14.19 là weaker hơn Mệnh đề 13.2. Ta giải thích cách mà đến sửa đổi quy nạp bước, để lại base trường hợp và rest của chứng minh như một bài tập. Như trong chứng minh của Mệnh đề 13.3, các vectơ $(e_{1}, \dots  , e_{k})$ tạo thành cơ sở (basis) cho không gian con được ký hiệu như $U_{k}'$, các vectơ $(e_{k+1}, \dots  , e_{n})$ tạo thành cơ sở (basis) cho không gian con được ký hiệu như $U_{k}''$, các không gian con $U_{k}'$ và $U_{k}''$ là trực giao, và $E = U_{k}' \oplus U_{k}''$. Cho
$$u_{k+1} = h_{k} \circ \cdots  \circ h_{2} \circ h_{1}(v_{k+1}).$$
Ta có thể viết
$$u_{k+1} = u_{k+1}' + u_{k+1}'',$$
Ở đâu $u_{k+1}' \in U_{k}'$ và $u_{k+1}'' \in U_{k}''$. Cho
$$r_{k+1,k+1} =

$u_{k+1}''$

$,ande^{i\theta k+1}|u_{k+1}'' \cdot  e_{k+1}| = u_{k+1}'' \cdot  e_{k+1}.$$$

<!-- PAGE 552 -->
Nếu $u_{k+1}'' = e^{i\theta k+1}r_{k+1,k+1} e_{k+1}$, ta cho $h_{k+1} =$ id. Ngược lại, theo Mệnh đề 14.19(1) (với $u = u_{k+1}''$ và $v = r_{k+1,k+1} e_{k+1})$, tồn tại duy nhất một siêu phẳng (hyperplane) phép đối xứng (reflection) $h_{k+1}$ sao cho
$$h_{k+1}(u_{k+1}'') = e^{i\theta k+1}r_{k+1,k+1} e_{k+1},$$
Ở đâu $h_{k+1}$ là phép đối xứng (reflection) về siêu phẳng (hyperplane) $H_{k+1}$ trực giao đến vectơ
$$w_{k+1} = r_{k+1,k+1} e_{k+1} -e^{-i\theta k+1}u_{k+1}''.$$
Tại kết thúc/cuối của quy nạp, ta có tam giác ma trận $R$, nhưng đường chéo các phần tử (entries) $e^{i\theta j}r_{j, j}$ của $R$ có thể là phức. Đặt
$$h_{n} = \rho_{en,-\theta n}  \circ \cdots  \circ \rho_{e1,-\theta1} ,$$
Ta nhận thấy rằng đường chéo các phần tử (entries) của ma trận của các vectơ
$$r_{j}' = h_{n} \circ h_{n-1} \circ \cdots  \circ h_{2} \circ h_{1}(v_{j})$$
Là tam giác với không âm các phần tử (entries).
Nhận xét: Cho số tính ổn định, nó được ưu tiên hơn để sử dụng $w_{k+1} = r_{k+1,k+1} e_{k+1} + e^{-i\theta k+1}u_{k+1}''$ thay vì của $w_{k+1} = r_{k+1,k+1} e_{k+1}$ - $e^{-i\theta k+1}u_{k+1}''$. effect của rằng lựa chọn là rằng đường chéo các phần tử (entries) trong $R$ sẽ là của tạo thành $-e^{i\theta j}r_{j, j} = e^{i(\theta j+\pi)}r_{j, j}$. Của course, ta có thể tạo các phần tử (các phần tử (entries)) này nonegative bằng cách áp dụng
$$h_{n} = \rho_{en, \pi-\theta n}  \circ \cdots  \circ \rho_{e1,\pi-\theta1}$$
Sau $h_{n-1}$. Như trong Euclidean trường hợp, Mệnh đề 14.20 ngay lập tức suy ra Phân rã QR (QR-decomposition) cho tùy ý phức các ma trận cỡ $n\times n$, ở đâu $Q$ là bây giờ unita (xem Kincaid và Cheney $[105]$ và Ciarlet $[41])$.

> **Mệnh đề 14.21.** Với mọi phức ma trận cỡ $n \times n$ $A$, có một dãy $H_{1}, \dots  , H_{n-1}$ của các ma trận, ở đâu mỗi $H_{i}$ là hoặc Ma trận Householder hoặc đồng nhất thức, và tam giác trên (upper triangular) ma trận $R$, sao cho
$$R = H_{n-1} \cdots  H_{2}H_{1}A.$$
Như hệ quả, có một cặp của các ma trận $Q, R$, ở đâu $Q$ là unita và $R$ là tam giác trên (upper triangular), sao cho $A = QR$ (Phân rã QR (QR-decomposition) của $A)$. Hơn nữa, $R$ có thể được được chọn sao cho của nó đường chéo các phần tử (entries) là không âm. Điều này có thể được đạt được bởi ma trận đường chéo (diagonal matrix) $D$ với các phần tử (entries) sao cho $|d_{ii}| = 1$ cho $i = 1, \dots  , n$, và ta có $A = QR$ với
$$e e$$
$$Q = H_{1} \cdots  H_{n-1}D,R = D^{*}R,$$
$$ee$$
Ở đâu $R$ là tam giác trên (upper triangular) và có không âm đường chéo các phần tử (entries). $e$

*Chứng minh.* Nó là về cơ bản đồng nhất đến chứng minh của Mệnh đề 13.4, và ta để lại chi tiết như một bài tập. Cho cuối cùng phát biểu, nhận thấy rằng $h_{n} \circ \cdots  \circ h_{1}$ là cũng phép đẳng cự (isometry).
