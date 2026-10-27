# Các bài tập


<!-- PAGE 654 -->
$\bullet$ Các tính chất của các trị riêng (eigenvalues) và các vectơ riêng (eigenvectors) của chuẩn tắc/bình thường ánh xạ tuyến tính (linear map). $\bullet$ phức hóa của thực không gian vectơ (vector space), của ánh xạ tuyến tính (linear map), và của Euclidean tích vô hướng (inner product). $\bullet$ các trị riêng (eigenvalues) của tự liên hợp (self-adjoint) ánh xạ trong Không gian Hermite (Hermitian space) là thực. $\bullet$ các trị riêng (eigenvalues) của tự liên hợp (self-adjoint) ánh xạ trong Không gian Euclid (Euclidean space) là thực. $\bullet$ Mọi tự liên hợp (self-adjoint) ánh xạ tuyến tính (linear map) trên Không gian Euclid (Euclidean space) có cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors). $\bullet$ Mọi chuẩn tắc/bình thường ánh xạ tuyến tính (linear map) trên Không gian Euclid (Euclidean space) có thể được khối được chéo hóa (các khối của kích thước nhiều nhất $2 \times  2)$ đối với cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors). $\bullet$ Mọi chuẩn tắc/bình thường ánh xạ tuyến tính (linear map) trên Không gian Hermite (Hermitian space) có thể được được chéo hóa đối với cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors). $\bullet$ các định lý phổ cho tự liên hợp (self-adjoint), phản tự liên hợp (skew-self-adjoint), và trực giao các ánh xạ tuyến tính (linear maps) (trên Không gian Euclid (Euclidean space)). $\bullet$ các định lý phổ cho chuẩn tắc/bình thường, đối xứng, phản đối xứng, và trực giao (thực) các ma trận. $\bullet$ các định lý phổ cho chuẩn tắc/bình thường, Hermite, skew-Hermitian, và unita (phức) các ma trận. $\bullet$ Rayleigh tỉ số và Rayleigh–Ritz định lý. $\bullet$ Interlacing các bất đẳng thức và Cauchy interlacing định lý. $\bullet$ Poincar´e separation định lý. $\bullet$ Courant–Fischer định lý. $\bullet$ Các bất đẳng thức liên quan đến perturbations của các trị riêng (eigenvalues) của ma trận đối xứng (symmetric matrix). $\bullet$ Weyl các bất đẳng thức.

## 17.9 Các bài tập

Bài toán 17.1. Chứng minh rằng cấu trúc $E_{C}$ đã giới thiệu trong Định nghĩa 17.2 là thật vậy phức không gian vectơ (vector space).

<!-- PAGE 655 -->
Bài toán 17.2. Chứng minh rằng công thức
$$\langle u_{1} + iv_{1}, u_{2} + iv_{2}\rangle_{C}  = \langle u_{1}, u_{2}\rangle + \langle v_{1}, v_{2}\rangle + i(\langle v_{1}, u_{2}\rangle -\langle u_{1}, v_{2}\rangle )$$
Định nghĩa Hermite tạo thành trên $E_{C}$ rằng là xác định dương (positive definite) và rằng $\langle$ -, $-\rangle_{C}$ agrees với $\langle$ -, $-\rangle$ trên thực các vectơ.
Bài toán 17.3. Cho trước bất kỳ ánh xạ tuyến tính (linear map) $f$: $E \to E$, chứng minh ánh xạ $f_{C}^{*}$ được định nghĩa sao cho
$$f_{C}^{*} (u + iv) = f^{*}(u) + if^{*}(v)$$
Với mọi $u, v \in E$ là liên hợp (adjoint) của $f_{C}$ w.r.t. $\langle$ -, $-\rangle_{C}$.
Bài toán 17.4. Cho $A$ là thực đối xứng $n\times n$ ma trận có các trị riêng (eigenvalues) là không âm. Chứng minh rằng với mọi $p > 0$, có một thực ma trận đối xứng (symmetric matrix) $S$ có các trị riêng (eigenvalues) là không âm sao cho $S^{p} = A$.
Bài toán 17.5. Cho $A$ là thực đối xứng $n \times  n$ ma trận có các trị riêng (eigenvalues) là dương.
$(1)$ Chứng minh rằng có một thực ma trận đối xứng (symmetric matrix) $S$ sao cho $A = e^{S}$.
$(2)$ Cho $S$ là thực đối xứng $n \times  n$ ma trận. Chứng minh rằng $A = e^{S}$ là thực đối xứng $n \times  n$ ma trận có các trị riêng (eigenvalues) là dương.
Bài toán 17.6. Cho $A$ là phức ma trận. Chứng minh rằng nếu $A$ có thể được được chéo hóa đối với cơ sở trực chuẩn (orthonormal basis), thì $A$ là chuẩn tắc/bình thường.
$$\mathbb{C}^{n} \mathbb{C}^{n}$$
Bài toán 17.7. Cho $f$: $\to$ là ánh xạ tuyến tính (linear map).
$(1)$ Chứng minh rằng nếu $f$ là chéo hóa được (diagonalizable) và nếu $\lambda_{1} , \dots  , \lambda_{n}$ là các trị riêng (eigenvalues) của $f$, thì $\lambda_{1}^{2} , \dots  , \lambda_{n}^{2}$ là các trị riêng (eigenvalues) của $f^{2}$, và nếu $\lambda_{i}^{2}  = \lambda_{j}^{2}$ suy ra rằng $\lambda_{i}  = \lambda_{j}$, thì $f$ và $f^{2}$ có cùng các không gian riêng (eigenspace).
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
$(2)$ Cho $f$ và $g$ là hai thực tự liên hợp (self-adjoint) các ánh xạ tuyến tính (linear maps) $f, g: \to$. Chứng minh rằng nếu $f$ và $g$ có không âm các trị riêng (eigenvalues) $(f$ và $g$ là positve nửa xác định) và nếu $f^{2} = g^{2}$, thì $f = g$.
Bài toán 17.8. $(1)$ Cho $\mathfrak{so}(3)$ là không gian của $3 \times  3$ skew các ma trận đối xứng
$$$$
$$\mathfrak{so}(3) = \begin{pmatrix} 0 & -c & b \\ c & 0 & -a \\ b & a & 0 \end{pmatrix} a, b, c \in \mathbb{R}.$$
$$-$$
Với mọi ma trận
$$A = \begin{pmatrix} 0 & -c & b \\ c & 0 & -a \\ b & a & 0 \end{pmatrix} \in \mathfrak{so}(3),$$
$$-$$
$$\sqrt$$
Nếu ta cho $\theta  = \overline{a}^{2} \overline{+}\overline{b}^{2} \overline{+}\overline{c}^{2}$, nhắc lại từ Mục 12.7 (Rodrigues công thức) rằng hàm mũ ánh xạ exp: $\mathfrak{so}(3) \to$ Do đó(3) được cho bởi
$$-$$
$$e^{A}= I_{3} + \frac{\sin \theta}{\theta} A + \frac{(1cos \theta )}{\theta^{2}} A^{2},if \theta  \neq  0,$$

<!-- PAGE 656 -->
Với $exp(0_{3}) = I_{3}$.
$(2)$ Chứng minh rằng $e^{A}$ là ma trận trực giao (orthogonal matrix) của định thức (determinant) $+1$, i.e., ma trận quay (rotation matrix).
$(3)$ Chứng minh rằng hàm mũ ánh xạ exp: $\mathfrak{so}(3) \to$ Do đó(3) là toàn ánh (surjective). Cho điều này tiến hành như sau: Chọn bất kỳ ma trận quay (rotation matrix) $R \in$ Do đó(3);
$(1)$ trường hợp $R =$ I là tầm thường.
$(2)$ Nếu $R \neq$ I và tr(R) $\neq  -1$, thì
$$



$$
$$\exp^{-1}(R) = \frac{\theta}{2 \sin \theta} (R -R^{T}) 1 + 2 \cos \theta  = \mathrm{tr}(R).$$
(Nhắc lại rằng tr(R) $= r_{1 1} + r_{2 2} + r_{3 3}$, vết (trace) của ma trận $R)$. Chỉ ra rằng tồn tại duy nhất một phản đối xứng $B$ với tương ứng $\theta$ thỏa mãn $0 < \theta  < \pi$ sao cho $e^{B} = R$.
$(3)$ Nếu R̸ $=$ I và tr(R) $= -1$, thì chứng minh rằng các trị riêng (eigenvalues) của $R$ là $1, -1, -1$, rằng $R = R^{\top}$, và rằng $R^{2} =$ I. Chứng minh rằng ma trận
$$S = \frac{1}{2} (R -I)$$
Là ma trận đối xứng (symmetric matrix) có các trị riêng (eigenvalues) là $-1, -1, 0$. Do đó $S$ có thể được được chéo hóa đối với ma trận trực giao (orthogonal matrix) $Q$ như
$$S = Q \begin{pmatrix} -1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 0 \end{pmatrix} Q^{\top}.$$
Chứng minh rằng tồn tại một skew ma trận đối xứng (symmetric matrix)
$$U = \begin{pmatrix} 0 & -d & c \\ d & 0 & -b \\ c & b & 0 \end{pmatrix}$$
$$-$$
Sao cho
$$U^{2} = S = \frac{1}{2} (R -I).$$
Nhận thấy rằng
$$U^{2}  = \begin{pmatrix} -(c^{2}+ d^{2}) & bc & bd \\ bc & -(b^{2}+ d^{2}) & cd \\ bd & cd & (b^{2}+ c^{2}) \end{pmatrix} ,$$
$$-$$

<!-- PAGE 657 -->
Và sử dụng điều này để kết luận rằng nếu $U^{2} = S$, thì $b^{2} + c^{2} + d^{2} = 1$. Thì chỉ ra rằng
$$$$
$$\exp^{-1}(R) =(2k + 1)\pi \begin{pmatrix} 0 & -d & c \\ d & 0 & -b \\ c & b & 0 \end{pmatrix} , k \in \mathbb{Z},$$
$$-$$
Ở đâu $(b, c, d)$ là bất kỳ unit vectơ sao cho cho tương ứng skew ma trận đối xứng (symmetric matrix) $U$, ta có $U^{2} = S$.
$(4)$ để tìm skew ma trận đối xứng (symmetric matrix) $U$ sao cho $U^{2} = S =_{2}^{1}(R$ - I) như trong $(3)$, ta có thể giải hệ
$$\begin{pmatrix} b^{2}-1 & bc & bd \\ bc & c^{2}-1 & cd \\ bd & cd & d^{2} & 1 \end{pmatrix} = S.$$
$$-$$
Ta ngay lập tức thu được $b^{2}, c^{2}, d^{2}$, và thì, vì một của $b, c, d$ là khác không, nói $b$, nếu ta chọn dương square nghiệm (root) của $b^{2}$, ta có thể xác định $c$ và $d$ từ bc và bd. Cài đặt máy tính bài toán quy hoạch trong Matlab để giải ở trên hệ.
Bài toán 17.9. Nó đã được hiển thị trong Mệnh đề 15.15 rằng hàm mũ ánh xạ là ánh xạ exp: $\mathfrak{so}(n) \to$ Do đó(n), $where\mathfrak{so}(n)$ là không gian vectơ (vector space) của thực $n\times n$ các ma trận phản đối xứng. Sử dụng định lý phổ (spectral theorem) để chứng minh rằng ánh xạ exp: $\mathfrak{so}(n) \to$ Do đó(n) là toàn ánh (surjective).
Bài toán 17.10. Cho $\mathfrak{u}(n)$ là không gian của (phức) $n \times  n$ skew-Các ma trận Hermite $(B^{*} = -B)$ và cho $\mathfrak{su}(n)$ là không gian con của nó bao gồm của skew-Hermitian matrice với không vết (trace) (tr(B) $= 0)$.
$(1)$ Chứng minh rằng nếu $B \in \mathfrak{u}(n)$, thì $e^{B} \in$ U(n), và nếu nếu $B \in \mathfrak{su}(n)$, thì $e^{B} \in$ SU(n). Do đó ta có xác định tốt (well-defined) các ánh xạ exp: $\mathfrak{u}(n) \to$ U(n) và exp: $\mathfrak{su}(n) \to$ SU(n).
$(2)$ Chứng minh rằng ánh xạ exp: $\mathfrak{u}(n) \to$ U(n) là toàn ánh (surjective).
$(3)$ Chứng minh rằng ánh xạ exp: $\mathfrak{su}(n) \to$ SU(n) là toàn ánh (surjective).
Bài toán 17.11. Nhắc lại rằng ma trận $B \in M_{n}(\mathbb{R})$ là phản đối xứng nếu $B^{\top} = -B$. Kiểm tra rằng $set\mathfrak{so}(n)$ của các ma trận phản đối xứng là không gian vectơ (vector space) có số chiều $n(n-1)/2$, và do đó là đẳng cấu đến $\mathbb{R}^{n(n-1)/2}$.
$(1)$ Cho trước ma trận quay (rotation matrix)
$$R = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} ,$$
Ở đâu $0 < \theta  < \pi$, chứng minh rằng có một skew ma trận đối xứng (symmetric matrix) $B$ sao cho
$$R = (I -B)(I + B)^{-1}.$$

<!-- PAGE 658 -->
$(2)$ Chứng minh rằng các trị riêng (eigenvalues) của ma trận phản đối xứng (skew-symmetric matrix) là hoặc $0$ hoặc thuần túy imaginary (rằng là, của tạo thành $i\mu$ cho $\mu  \in \mathbb{R}.)$. Cho $C$: $\mathfrak{so}(n) \to M_{n}(\mathbb{R})$ là hàm (được gọi là Cayley biến đổi của $B)$ cho trước bởi
$$C(B) = (I -B)(I + B)^{-1}.$$
Chứng minh rằng nếu $B$ là phản đối xứng, thì I - $B$ và I $+ B$ là khả nghịch, và do đó $C$ là welldefined. Chứng minh rằng
$$(I + B)(I -B) = (I -B)(I + B),$$
Và rằng
$$(I + B)(I -B)^{-1}= (I -B)^{-1}(I + B).$$
Chứng minh rằng
$$(C(B))^{\top}C(B) = I$$
Và rằng
$$\det C(B) = +1,$$
Sao cho C(B) là ma trận quay (rotation matrix). Hơn nữa, chỉ ra rằng C(B) thực hiện không admit $-1$ như trị riêng (eigenvalue).
$(3)$ Cho Do đó(n) là nhóm của $n \times  n$ các ma trận quay. Chứng minh rằng ánh xạ
$$C : \mathfrak{so}(n) \to SO(n)$$
Là song ánh (bijective) lên tập con của các ma trận quay rằng thực hiện không admit $-1$ như trị riêng (eigenvalue). Chỉ ra rằng nghịch đảo của ánh xạ này được cho bởi
$$B = (I + R)^{-1}(I -R) = (I -R)(I + R)^{-1},$$
Ở đâu $R \in$ Do đó(n) thực hiện không admit $-1$ như trị riêng (eigenvalue).
Bài toán 17.12. Please refer quay lại đến Bài toán 4.6. Cho $\lambda_{1} , \dots  , \lambda_{n}$ là các trị riêng (eigenvalues) của $A$ (không nhất thiết phân biệt). Bằng cách sử dụng Schur’s định lý, $A$ là đồng dạng đến tam giác trên (upper triangular) ma trận $B$, nghĩa là, $A = PBP^{-1}$ với $B$ tam giác trên (upper triangular), và ta có thể giả sử rằng đường chéo các phần tử (entries) của $B$ trong descending thứ tự là $\lambda_{1} , \dots  , \lambda_{n}$.
$(1)$ Nếu $E_{ij}$ được liệt kê theo tổng thứ tự cho trước bởi
$$i = h and j > k$$
$$(i, j) < (h, k)iff$$
$$or i < h.$$
Chứng minh rằng $R_{B}$ là tam giác trên (upper triangular) ma trận có đường chéo các phần tử (entries) là
$$(\lambda_{n} , \dots  , \lambda_{1} , \dots  , \lambda_{n} , \dots  , \lambda_{1} ),$$
$$|{z}$$
$$n2$$

<!-- PAGE 659 -->
Và rằng $L_{B}$ là tam giác trên (upper triangular) ma trận có đường chéo các phần tử (entries) là
$$(\lambda_{1} , \dots  , \lambda_{1} \dots  , \lambda_{n} , \dots  , \lambda_{n} ).$$
$$|{z}|{z}$$
$$nn$$
Hint. Hình ra những gì là $R_{B}(E_{ij}) = E_{ij}B$ và $L_{B}(E_{ij}) = BE_{ij}$.
$(2)$ Sử dụng sự kiện rằng
$$L_{A} = L_{P} \circ L_{B} \circ L_{P}^{-1} ,R_{A} = R_{P}^{-1} \circ R_{B} \circ R_{P},$$
Đến biểu diễn $ad_{A} = L_{A}$ - $R_{A}$ theo $L_{B}$ - $R_{B}$, và kết luận rằng các trị riêng (eigenvalues) của $ad_{A}$ là $\lambda_{i}$ - $\lambda_{j}$, cho $i = 1, \dots  , n$, và cho $j = n, \dots  , 1$.

<!-- PAGE 660 -->
