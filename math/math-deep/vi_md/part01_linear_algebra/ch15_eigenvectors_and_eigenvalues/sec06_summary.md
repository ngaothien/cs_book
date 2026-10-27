# Tóm tắt


<!-- PAGE 589 -->
Nếu $B$ là skew ma trận đối xứng (symmetric matrix), vì tr(B) $= 0$, ta suy ra rằng $det(e^{B}) = e^{0} = 1$. Điều này cho phép chúng ta để thu được kết quả sau đây. Nhắc lại rằng (thực) không gian vectơ (vector space) của skew các ma trận đối xứng được ký hiệu bởi $\mathfrak{so}(n)$.

> **Mệnh đề 15.15.** Với mọi skew ma trận đối xứng (symmetric matrix) $B \in \mathfrak{so}(n)$, ta có $e^{B} \in$ Do đó(n), nghĩa là, $e^{B}$ là phép quay.

*Chứng minh.* Theo Mệnh đề 9.24, $e^{B}$ là ma trận trực giao (orthogonal matrix). Vì tr(B) $= 0$, ta suy ra rằng $det(e^{B}) = e^{0} = 1$. Vì vậy, $e^{B} \in$ Do đó(n). Mệnh đề 15.15 chỉ ra rằng ánh xạ $B \mapsto e^{B}$ là ánh xạ exp: $\mathfrak{so}(n) \to$ Do đó(n). Nó là không đơn ánh (injective), nhưng nó có thể được được hiển thị (bằng cách sử dụng một của các định lý phổ) rằng nó là toàn ánh (surjective). Nếu $B$ là (thực) ma trận đối xứng (symmetric matrix), thì
$$(e^{B})^{\top}= e^{B\top}= e^{B},$$
Do đó $e^{B}$ là cũng đối xứng. Vì các trị riêng (eigenvalues) $\lambda_{1} , \dots  , \lambda_{n}$ của $B$ là thực, theo Mệnh đề 15.13, vì các trị riêng (eigenvalues) của $e^{B}$ là $e^{\lambda1}, \dots  , e^{\lambda n}$ và $\lambda_{i}$ là thực, ta có $e^{\lambda i} > 0$ cho $i = 1, \dots  , n$, mà suy ra rằng $e^{B}$ là đối xứng xác định dương (SPD). Thực ra, nó có thể được được hiển thị rằng với mọi đối xứng xác định dương (SPD) ma trận $A$, tồn tại duy nhất một ma trận đối xứng (symmetric matrix) $B$ sao cho $A = e^{B}$; xem Gallier $[73]$.

## 15.6 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ Ma trận đường chéo (diagonal matrix). $\bullet$ Các trị riêng (eigenvalues), các vectơ riêng (eigenvectors); không gian riêng (eigenspace) liên kết với trị riêng (eigenvalue). $\bullet$ Đa thức đặc trưng (characteristic polynomial). $\bullet$ Vết (trace). $\bullet$ Đại số và hình học bội (multiplicity). $\bullet$ các không gian riêng (eigenspace) liên kết với phân biệt các trị riêng (eigenvalues) tạo thành tổng trực tiếp (direct sum) (Mệnh đề 15.3). $\bullet$ Reduction của ma trận đến tam giác trên (upper-triangular) ma trận. $\bullet$ Schur phân rã. $\bullet$ Gershgorin’s discs có thể được sử dụng để locate các trị riêng (eigenvalues) của phức ma trận; xem Các định lý 15.9 và 15.10. $\bullet$ điều kiện của trị riêng (eigenvalue) các bài tập. $\bullet$ Các trị riêng (eigenvalues) của ma trận hàm mũ. công thức $det(e^{A}) = e^{tr(A)}$.
