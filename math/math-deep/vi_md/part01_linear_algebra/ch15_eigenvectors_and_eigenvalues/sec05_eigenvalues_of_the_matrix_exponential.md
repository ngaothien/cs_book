# Các trị riêng (eigenvalues) của Ma trận Hàm mũ


<!-- PAGE 587 -->
Mệnh đề 15.11 suy ra rằng với mọi chéo hóa được (diagonalizable) ma trận $A$, nếu ta định nghĩa $\Gamma (A)$ bởi
$$\Gamma (A) = \inf{cond(P) | P^{-1} AP = D},$$
Thì với mọi trị riêng (eigenvalue) $\lambda$ của $A + \Delta A$, ta có
$$\mathbb{C}^{n}$$
$$\lambda  \in \bigcup_{k=1}^{n}  {z \in | |z -\lambda_{k} | \le \Gamma (A) \|\Delta A\|}.$$

> **Định nghĩa 15.6.** số $\Gamma (A) = inf{cond(P)$ | $P^{-1} AP = D}$ được gọi là điều kiện của $A$ tương đối đến trị riêng (eigenvalue) bài toán. Nếu $A$ là ma trận chuẩn tắc (normal matrix), vì theo Định lý 17.22, $A$ có thể được được chéo hóa đối với ma trận unita (unitary matrix) $U$, và vì cho spectral chuẩn (norm) $\|U\|_{2} = 1$, ta xem rằng $\Gamma (A) = 1$. Vì vậy, các ma trận chuẩn tắc là rất tốt conditionned w.r.t. trị riêng (eigenvalue) bài toán. Thực ra, với mọi trị riêng (eigenvalue) $\lambda$ của $A + \Delta A$ (với $A$ chuẩn tắc/bình thường), ta có
$$\mathbb{C}^{n}$$
$$\lambda  \in \bigcup_{k=1}^{n}  {z \in | |z -\lambda_{k} | \le \|\Delta A\|_{2}}.$$
Nếu $A$ và $A+\Delta A$ là cả hai đối xứng (hoặc Hermite), có sharper các kết quả; xem Mệnh đề 17.28. Lưu ý rằng ma trận $A(\epsilon$) từ bắt đầu của mục là không chuẩn tắc/bình thường.

## 15.5 Các trị riêng (eigenvalues) của Ma trận Hàm mũ

Schur phân rã cho ta đặc trưng của các trị riêng (eigenvalues) của ma trận hàm mũ $e^{A}$ theo các trị riêng (eigenvalues) của ma trận $A$. Thứ nhất ta có kết quả sau mệnh đề.

> **Mệnh đề 15.12.** Cho $A$ và $U$ là (thực hoặc phức) các ma trận và giả sử rằng $U$ là khả nghịch. Thì
$$e^{UAU-1}= Ue^{A}U^{-1} .$$

*Chứng minh.* tầm thường quy nạp chỉ ra rằng
$$UA^{p}U^{-1}= (UAU^{-1})^{p},$$
Và do đó
$$e^{UAU-1} = \sum_{p\ge0}  \frac{(UAU^{-1})^{p}}{p!} = \sum_{p\ge0}  \frac{UA^{p}U^{-1}}{p!}$$
$$= U \sum_{p\ge0}  \frac{A^{p}}{p!} !U^{-1}  = Ue^{A}U^{-1} ,$$
Như đã khẳng định.

<!-- PAGE 588 -->

> **Mệnh đề 15.13.** Cho trước bất kỳ phức $n \times  n$ ma trận $A$, nếu $\lambda_{1} , \dots  , \lambda_{n}$ là các trị riêng (eigenvalues) của, thì là các trị riêng (eigenvalues) của. Hơn nữa, nếu là vectơ riêng (eigenvector) của $A  e^{\lambda1}, \dots  , e^{\lambda n}  e^{A}  u  A$ cho $\lambda_{i}$, thì $u$ là vectơ riêng (eigenvector) của $e^{A}$ cho $e^{\lambda i}$.

*Chứng minh.* Theo Định lý 15.5, có một ma trận khả nghịch (invertible matrix) $P$ và tam giác trên (upper triangular) ma trận $T$ sao cho
$$A = PTP^{-1} .$$
Theo Mệnh đề 15.12,
$$e^{PTP-1}= Pe^{T}P^{-1} .$$
$$Tp$$
$$Note that e^{T}= \sum_{p}  \ge   is upper triangular since T^{p}is upper triangular for all p \ge 0. If$$
$\lambda_{1} , \lambda_{2} , \dots  , \lambda_{n}$ là $the^{0p!}$ đường chéo các phần tử (entries) của $T$, các tính chất của phép nhân ma trận (matrix multiplication), khi combined với quy nạp trên $p$, suy ra rằng đường chéo các phần tử (entries) của $T^{p}$ là $\lambda_{1}^{p} , \lambda_{2}^{p} , \dots  , \lambda_{n}^{p}$.
$$\lambda p$$
$$This in turn implies that the diagonal entries of e^{T}are \sum_{p}  \ge \overline{i} = e^{\lambda i}for 1 \le i \le n. Since$$
$A$ và $T$ là đồng dạng các ma trận, ta biết rằng chúng có $the^{0p!}$ cùng các trị riêng (eigenvalues), cụ thể là đường chéo các phần tử (entries) $\lambda_{1} , \dots  , \lambda_{n}$ của $T$. Vì $e^{A} = e^{PTP-1} = Pe^{T}P^{-1}$, và $e^{T}$ là tam giác trên (upper triangular), ta sử dụng cùng lập luận để kết luận rằng cả hai $e^{A}$ và $e^{T}$ có cùng các trị riêng (eigenvalues), mà là đường chéo các phần tử (entries) của $e^{T}$, ở đâu đường chéo các phần tử (entries) của $e^{T}$ là của tạo thành $e^{\lambda1}, \dots  , e^{\lambda n}$. Bây giờ, nếu $u$ là vectơ riêng (eigenvector) của $A$ cho trị riêng (eigenvalue) $\lambda$, đơn giản quy nạp chỉ ra rằng $u$ là vectơ riêng (eigenvector) của $A^{n}$ cho trị riêng (eigenvalue) $\lambda^{n}$, từ mà là suy ra rằng
$$   $$
$$e^{A}u =I + \frac{A}{1!} + \frac{A^{2}}{2!} + \frac{A^{3}}{3!} + \dots u = u + Au + \frac{A^{2}}{2!} u + \frac{A^{3}}{3!} u + \dots$$
$$  $$
$$= u + \lambda u + \frac{\lambda^{2}}{2!} u + \frac{\lambda^{3}}{3!} u + \cdots  =1 + \lambda  + \frac{\lambda^{2}}{2!} + \frac{\lambda^{3}}{3!} + \dots u = e^{\lambda}u,$$
Mà chỉ ra rằng $u$ là vectơ riêng (eigenvector) của $e^{A}$ cho $e^{\lambda}$. Hệ quả là, ta thu được kết quả sau kết quả.

> **Mệnh đề 15.14.** Với mọi phức (hoặc thực) ma trận vuông (square matrix) $A$, ta có
$$\det(e^{A}) = e^{\mathrm{tr}(A)},$$
Ở đâu tr() là vết (trace) của $A$, i.e., tổng $a_{1 1} + \cdots  + a_{n n}$ của của nó đường chéo các phần tử (entries).

*Chứng minh.* vết (trace) của ma trận $A$ bằng tổng của các trị riêng (eigenvalues) của $A$. định thức (determinant) của ma trận bằng tích của các trị riêng (các trị riêng (eigenvalues)) của nó, và nếu $\lambda_{1} , \dots  , \lambda_{n}$ là các trị riêng (eigenvalues) của $A$, thì theo Mệnh đề 15.13, $e^{\lambda1}, \dots  , e^{\lambda n}$ là các trị riêng (eigenvalues) của $e^{A}$, và do đó
$$\det \begin{pmatrix} e^{A} \end{pmatrix} = e^{\lambda1}\cdots  e^{\lambda n}= e^{\lambda1+\cdot \cdot \cdot+\lambda n}= e^{\mathrm{tr}(A)},$$
Như mong muốn.
