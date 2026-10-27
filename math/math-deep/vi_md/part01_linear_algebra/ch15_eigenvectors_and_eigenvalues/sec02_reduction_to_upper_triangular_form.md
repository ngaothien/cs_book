# Reduction đến Tam giác trên (upper triangular) Tạo thành


<!-- PAGE 577 -->

## 15.2 Reduction đến Tam giác trên (upper triangular) Tạo thành

Không may là, không mọi ánh xạ tuyến tính (linear map) trên phức không gian vectơ (vector space) có thể được được chéo hóa. tiếp theo tốt nhất thing là đến “triangularize,” mà có nghĩa là để tìm cơ sở (basis) trên mà ma trận có không các phần tử (entries) ở dưới chính đường chéo. May mắn thay, như vậy cơ sở (basis) luôn luôn tồn tại. Ta nói rằng ma trận vuông (square matrix) $A$ là tam giác trên (upper triangular) ma trận nếu nó có sau đây hình dạng,
$$\begin{pmatrix} a_{1 1} & a_{1 2} & a_{1 3} & \dots & a_{1n-1} & a_{1n} \\ 0 & a_{2 2} & a_{2 3} & \dots & a_{2n-1} & a_{2n} \\ 0 & 0 & a_{3 3} & \dots & a_{3n-1} & a_{3n} \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \dots & a_{n-1n-1} & a_{n-1n} \\ 0 & 0 & 0 & \dots & 0 & a_{n n} \end{pmatrix} ,$$
I.e., $a_{i j} = 0$ bất cứ khi nào $j < i, 1 \le i, j \le n$.

> **Định lý 15.5.** Cho trước bất kỳ hữu hạn dimensional không gian vectơ (vector space) trên trường $K$, với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$, có một cơ sở (basis) $(u_{1}, \dots  , u_{n})$ đối với mà $f$ được biểu diễn bởi tam giác trên (upper triangular) ma trận (trong $M_{n}(K))$ khi và chỉ khi tất cả các trị riêng (eigenvalues) của $f$ thuộc đến $K$. Tương đương, với mọi $n \times  n$ ma trận $A \in M_{n}(K)$, có một ma trận khả nghịch (invertible matrix) $P$ và tam giác trên (upper triangular) ma trận $T$ (cả hai trong $M_{n}(K))$ sao cho
$$A = PTP^{-1}$$
Khi và chỉ khi tất cả các trị riêng (eigenvalues) của $A$ thuộc đến $K$.

*Chứng minh.* Nếu có một cơ sở (basis) $(u_{1}, \dots  , u_{n})$ đối với mà $f$ được biểu diễn bởi tam giác trên (upper triangular) ma trận $T$ trong $M_{n}(K)$, khi đó vì các trị riêng (eigenvalues) của $f$ là đường chéo các phần tử (entries) của $T$, tất cả các trị riêng (eigenvalues) của $f$ thuộc đến $K$. Cho điều ngược lại, ta tiến hành bằng quy nạp theo số chiều $n$ của $E$. Cho $n = 1$ kết quả là hiển nhiên. Nếu $n > 1$, vì bởi giả định $f$ có tất cả các trị riêng (các trị riêng (eigenvalues)) của nó trong $K$, chọn một số trị riêng (eigenvalue) $\lambda_{1}  \in K$ của $f$, và cho $u_{1}$ là một số tương ứng (khác không) vectơ riêng (eigenvector). Ta có thể tìm $n$ - $1$ các vectơ $(v_{2}, \dots  , v_{n})$ sao cho $(u_{1}, v_{2}, \dots  , v_{n})$ là cơ sở (basis) của $E$, và cho $F$ là không gian con có số chiều $n$ - $1$ được sinh (spanned) bởi $(v_{2}, \dots  , v_{n})$. Trong cơ sở (basis) $(u_{1}, v_{2} \dots  , v_{n})$, ma trận của $f$ là của tạo thành
$$U = \begin{pmatrix} \lambda_{1} & a_{1 2} & \dots & a_{1n} \\ 0 & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ 0 & a_{n2} & \dots & a_{n n} \end{pmatrix} ,$$
Vì của nó cột thứ nhất chứa các tọa độ của $\lambda_{1} u_{1}$ trên cơ sở (basis) $(u_{1}, v_{2}, \dots  , v_{n})$. Nếu ta cho $p: E \to F$ là phép chiếu được định nghĩa sao cho $p(u_{1}) = 0$ và $p(v_{i}) = v_{i}$ khi $2 \le i \le n$, ánh xạ tuyến tính (linear map) $g: F \to F$ được định nghĩa như thu hẹp của $p \circ f$ đến $F$ được biểu diễn bởi

<!-- PAGE 578 -->
$(n$ - $1) \times  (n$ - $1)$ ma trận $V = (a_{i j})_{2\le i,j\le n}$ trên cơ sở (basis) $(v_{2}, \dots  , v_{n})$. Ta cần để chứng minh rằng tất cả các trị riêng (eigenvalues) của $g$ thuộc đến $K$. Tuy nhiên, vì các phần tử (entries) trong cột thứ nhất của $U$ là tất cả không cho $i = 2, \dots  , n$, ta thu được
$$\chi_{U} (X) = \det(XI -U) = (X -\lambda_{1} ) \det(XI -V ) = (X -\lambda_{1} )\chi_{V}  (X),$$
Ở đâu $\chi_{U} (X)$ là đa thức đặc trưng (characteristic polynomial) của $U$ và $\chi_{V}  (X)$ là đa thức đặc trưng (characteristic polynomial) của $V$. Suy ra rằng $\chi_{V}  (X)$ chia hết $\chi_{U} (X)$, và vì tất cả các nghiệm của $\chi_{U} (X)$ là trong $K$, tất cả các nghiệm của $\chi_{V}  (X)$ là cũng trong $K$. Hệ quả là, ta có thể áp dụng giả thiết quy nạp (induction hypothesis), và có một cơ sở (basis) $(u_{2}, \dots  , u_{n})$ của $F$ sao cho $g$ được biểu diễn bởi tam giác trên (upper triangular) ma trận $(b_{i j})_{1\le i,j\le n-1}$. Tuy nhiên,
$$E = Ku_{1} \oplus F,$$
Và do đó $(u_{1}, \dots  , u_{n})$ là cơ sở (basis) cho $E$. Vì $p$ là phép chiếu từ $E = Ku_{1} \oplus F$ lên $F$ và $g: F \to F$ là thu hẹp của $p \circ f$ đến $F$, ta có
$$f(u_{1}) = \lambda_{1} u_{1}$$
Và
$$f(u_{i+1}) = a_{1i}u_{1} + \sum_{j=1}^{i}  b_{i j}u_{j+1}$$
Với một số $a_{1i} \in K$, khi $1 \le i \le$ n-1. Nhưng khi đó ma trận của $f$ đối với $(u_{1}, \dots  , u_{n})$ là tam giác trên (upper triangular). Cho ma trận phiên bản, ta giả sử rằng $A$ là ma trận của $f$ đối với một số cơ sở (basis), Thì ta chỉ được chứng minh rằng có một ma trận chuyển cơ sở (change of basis matrix) $P$ sao cho $A = PTP^{-1}$ ở đâu $T$ là tam giác trên (upper triangular). Nếu $A = PTP^{-1}$ ở đâu $T$ là tam giác trên (upper triangular), lưu ý rằng đường chéo các phần tử (entries) của $T$ là các trị riêng (eigenvalues) $\lambda_{1} , \dots  , \lambda_{n}$ của $A$. Thật vậy, $A$ và $T$ có cùng đa thức đặc trưng (characteristic polynomial). Cũng, nếu $A$ là thực ma trận có các trị riêng (eigenvalues) là tất cả thực, thì $P$ có thể được được chọn đến thực, và nếu $A$ là hữu tỷ ma trận có các trị riêng (eigenvalues) là tất cả hữu tỷ, thì $P$ có thể được được chọn hữu tỷ. Vì bất kỳ đa thức trên $\mathbb{C}$ có tất cả của nó các nghiệm trong $\mathbb{C}$, Định lý 15.5 suy ra rằng mọi phức $n \times  n$ ma trận có thể được triangularized. Nếu $E$ là Không gian Hermite (Hermitian space) (xem Chương $14)$, chứng minh của Định lý 15.5 có thể được dễ dàng được điều chỉnh để chứng minh rằng có một cơ sở trực chuẩn (orthonormal basis) $(u_{1}, \dots  , u_{n})$ đối với mà ma trận của $f$ là tam giác trên (upper triangular). Điều này là thường đã biết như Schur’s bổ đề.

> **Định lý 15.6.** (Schur phân rã) Cho trước bất kỳ ánh xạ tuyến tính (linear map) $f$: $E \to E$ trên phức Không gian Hermite (Hermitian space) $E$, có một cơ sở trực chuẩn (orthonormal basis) $(u_{1}, \dots  , u_{n})$ đối với mà $f$ được biểu diễn bởi tam giác trên (upper triangular) ma trận. Tương đương, với mọi $n \times  n$ ma trận $A \in M_{n}(\mathbb{C})$, có một ma trận unita (unitary matrix) $U$ và tam giác trên (upper triangular) ma trận $T$ sao cho
$$A = UTU^{*} .$$

<!-- PAGE 579 -->
Nếu $A$ là thực và nếu tất cả các trị riêng (các trị riêng (eigenvalues)) của nó là thực, thì có một ma trận trực giao (orthogonal matrix) $Q$ và thực tam giác trên (upper triangular) ma trận $T$ sao cho
$$A = QTQ^{\top}.$$

*Chứng minh.* During quy nạp, ta chọn $F$ là phần bù trực giao (orthogonal complement) của $\mathbb{C} u_{1}$ và ta chọn các cơ sở trực chuẩn (sử dụng Các mệnh đề 14.13 và 14.12). Nếu $E$ là thực Không gian Euclid (Euclidean space) và nếu các trị riêng (eigenvalues) của $f$ là tất cả thực, chứng minh cũng đi qua với thực các ma trận (sử dụng Các mệnh đề 12.11 và 12.10). Nếu $\lambda$ là trị riêng (eigenvalue) của ma trận $A$ và nếu $u$ là vectơ riêng (eigenvector) liên kết với $\lambda$, từ
$$Au = \lambda u,$$
Ta thu được
$$A^{2}u = A(Au) = A(\lambda u) = \lambda Au = \lambda^{2} u,$$
Mà chỉ ra rằng $\lambda^{2}$ là trị riêng (eigenvalue) của $A^{2}$ cho vectơ riêng (eigenvector) $u$. hiển nhiên quy nạp chỉ ra rằng $\lambda^{k}$ là trị riêng (eigenvalue) của $A^{k}$ cho vectơ riêng (eigenvector) $u$, với mọi $k \ge 1$. Bây giờ, nếu tất cả các trị riêng (eigenvalues) $\lambda_{1} , \dots  , \lambda_{n}$ của $A$ là trong $K$, suy ra rằng $\lambda_{1}^{k} , \dots  , \lambda_{n}^{k}$ là các trị riêng (eigenvalues) của $A^{k}$. Tuy nhiên, nó là không hiển nhiên rằng $A^{k}$ thực hiện không có khác các trị riêng (eigenvalues). Thực ra, điều này có thể’t xảy ra, và điều này có thể được được chứng minh bằng cách sử dụng Định lý 15.5.

> **Mệnh đề 15.7.** Cho trước bất kỳ ma trận cỡ $n \times  n$ $A \in M_{n}(K)$ với các hệ số trong trường $K$, nếu tất cả các trị riêng (eigenvalues) $\lambda_{1} , \dots  , \lambda_{n}$ của $A$ là trong $K$, thì với mọi đa thức q(X) $\in$ K[X], các trị riêng (eigenvalues) của q() là chính xác $(q(\lambda_{1}$), $\dots  , q(\lambda_{n}$)).

*Chứng minh.* Theo Định lý 15.5, có một tam giác trên (upper triangular) ma trận $T$ và ma trận khả nghịch (invertible matrix) $P$ (cả hai trong $M_{n}(K))$ sao cho
$$A = PTP^{-1} .$$
Vì $A$ và $T$ là đồng dạng, chúng có cùng các trị riêng (eigenvalues) (với cùng các bội), do đó đường chéo các phần tử (entries) của $T$ là các trị riêng (eigenvalues) của $A$. Vì
$$A^{k}= PT^{k}P^{-1},k \ge 1,$$
Với mọi đa thức q(X) $= c_{0}X^{m} + \cdots  + c_{m-1}X + c_{m}$, ta có
$$q(A) = c_{0}A^{m}+ \cdots  + c_{m-1}A + c_{m}I$$
$$= c_{0}PT^{m}P^{-1}+ \cdots  + c_{m-1}PTP^{-1}+ c_{m}PIP^{-1}$$
$$= P(c_{0}T^{m}+ \cdots  + c_{m-1}T + c_{m}I)P^{-1}$$
$$= Pq(T)P^{-1} .$$
Hơn nữa, nó là dễ để kiểm tra rằng q(T) là tam giác trên (upper triangular) và rằng của nó đường chéo các phần tử (entries) là $q(\lambda_{1}$), $\dots  , q(\lambda_{n}$), ở đâu $\lambda_{1} , \dots  , \lambda_{n}$ là đường chéo các phần tử (entries) của $T$, cụ thể là các trị riêng (eigenvalues) của $A$. Suy ra rằng $q(\lambda_{1}$), $\dots  , q(\lambda_{n}$) là các trị riêng (eigenvalues) của q().

<!-- PAGE 580 -->
$$Remark: There is another way to prove Proposition 15.7 that does \frac{not}{K} use Theorem 15.5,$$
Nhưng thay vì sử dụng sự kiện rằng cho trước bất kỳ trường $K$, ở đó là trường mở rộng của $K (K \subseteq \overline{K})$ sao cho mọi đa thức q(X) $= c_{0}X^{m} + \cdots  + c_{m-1}X + c_{m}$ (của bậc $m \ge 1)$ với các hệ số $c_{i} \in K$ các nhân tử như
$$q(X) = c_{0}(X -\alpha_{1} ) \cdots  (X -\alpha_{n} ),\alpha_{i}  \in \overline{K, i} = 1, \dots  , n.$$
Trường $\overline{K}$ được gọi là một algebraically đóng trường (và đại số bao đóng (closure) của $K)$.
$$Assume that all \frac{eigenvalues}{K} \lambda_{1} , \dots  , \lambda_{n}  of A belong to K. Let q(X) be any polynomial$$
$$(in K[X]) and let \mu  \in  be any eigenvalue of q(A) \frac{(this}{K} means that \mu  is a zero of the$$
Đa thức đặc trưng (characteristic polynomial) $\chi_{q(A)} (X) \in$ K[X] của q(). Vì là algebraically đóng, $\chi_{q(A)} (X)$ có tất cả của nó các nghiệm trong $\overline{K})$. Ta khẳng định rằng $\mu  = q(\lambda_{i}$) với một số trị riêng (eigenvalue) $\lambda_{i}$ của $A$.

*Chứng minh.* (Sau Lax $[117]$, Chương $6). Since\overline{K}$ là algebraically đóng, đa thức $\mu$ -q(X) các nhân tử như
$$\mu  -q(X) = c_{0}(X -\alpha_{1} ) (X -\alpha_{n} ),$$
$$for some \alpha_{i}  \in \overline{K}. Now \mu I -q(A) is a matrix in M_{n}( \frac{\cdots}{K} ), and since \mu  is an eigenvalue of q(A),$$
Nó phải là suy biến. Ta có
$$\mu I -q(A) = c_{0}(A -\alpha_{1} I) \cdots  (A -\alpha_{n} I),$$
Và vì vế trái là suy biến, do đó là vế phải, mà suy ra rằng một số nhân tử $A -\alpha_{i}$ I là suy biến. Điều này có nghĩa là $\alpha_{i}$ là trị riêng (eigenvalue) của $A$, nói $\alpha_{i}  = \lambda_{i}$. Như $\alpha_{i}  = \lambda_{i}$ là không của $\mu$ - q(X), ta thu được
$$\mu  = q(\lambda_{i} ),$$
Mà chứng tỏ rằng $\mu$ là thật vậy của tạo thành $q(\lambda_{i}$) với một số trị riêng (eigenvalue) $\lambda_{i}$ của $A$. Bằng cách sử dụng Định lý 15.6, ta có thể derive hai rất quan trọng các kết quả.

> **Mệnh đề 15.8.** Nếu $A$ là Ma trận Hermite (Hermitian matrix) (i.e. $A^{*} = A)$, thì các trị riêng (các trị riêng (eigenvalues)) của nó là thực và $A$ có thể được được chéo hóa đối với cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors). Trong ma trận các số hạng, có một ma trận unita (unitary matrix) $U$ và thực ma trận đường chéo (diagonal matrix) $D$ sao cho $A = UDU^{*}$. Nếu $A$ là thực ma trận đối xứng (symmetric matrix) (i.e. $A^{\top} = A)$, thì các trị riêng (các trị riêng (eigenvalues)) của nó là thực và $A$ có thể được được chéo hóa đối với cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors). Trong ma trận các số hạng, có một ma trận trực giao (orthogonal matrix) $Q$ và thực ma trận đường chéo (diagonal matrix) $D$ sao cho $A = QDQ^{\top}$.

*Chứng minh.* Theo Định lý 15.6, ta có thể viết $A = UTU^{*}$ ở đâu $T = (t_{ij})$ là tam giác trên (upper triangular) và $U$ là ma trận unita (unitary matrix). Nếu $A^{*} = A$, ta thu được
$$UTU^{*} = UT^{*} U^{*} ,$$
Và điều này suy ra rằng $T = T^{*}$. Vì $T$ là tam giác trên (upper triangular) ma trận, $T^{*}$ là tam giác dưới (lower triangular) ma trận, mà suy ra rằng $T$ là ma trận đường chéo (diagonal matrix). Hơn nữa, vì $T = T^{*}$, ta có
