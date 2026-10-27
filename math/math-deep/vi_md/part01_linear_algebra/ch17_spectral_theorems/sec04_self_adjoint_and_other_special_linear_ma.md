# Tự liên hợp (self-adjoint) và Khác Đặc biệt Các ánh xạ tuyến tính (linear maps)


<!-- PAGE 636 -->

## 17.4 Tự liên hợp (self-adjoint), Phản tự liên hợp (skew-self-adjoint), và Trực giao

$$Linear Maps$$
Ta bắt đầu với tự liên hợp (self-adjoint) các ánh xạ.

> **Định lý 17.14.** Cho trước Không gian Euclid (Euclidean space) $E$ có số chiều $n$, với mọi tự liên hợp (self-adjoint) ánh xạ tuyến tính (linear map) $f$: $E \to E$, có một cơ sở trực chuẩn (orthonormal basis) $(e_{1}, \dots  , e_{n})$ của các vectơ riêng (eigenvectors) của $f$ sao cho ma trận của $f$ w.r.t. cơ sở (cơ sở (basis)) này là ma trận đường chéo (diagonal matrix)
$$\begin{pmatrix} \lambda_{1} & \dots \\ \lambda_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & \lambda_{n} \end{pmatrix} ,$$
Ở đâu $\lambda_{i}  \in \mathbb{R}$.

*Chứng minh.* Ta đã được chứng minh điều này; xem Định lý 17.8. Tuy nhiên, nó là instructive đến cho nhiều hơn/thêm trực tiếp phương pháp không liên quan đến phức hóa của $\langle$ -, $-\rangle$ và Mệnh đề 17.5. Vì $\mathbb{C}$ là algebraically đóng, $f_{C}$ có một số trị riêng (eigenvalue) $\lambda  + i\mu$, và cho $u +$ iv là một số vectơ riêng (eigenvector) của $f_{C}$ cho $\lambda +i\mu$, ở đâu $\lambda , \mu  \in \mathbb{R}$ và $u, v \in E$. Ta đã thấy trong chứng minh của Mệnh đề 17.10 rằng
$$f(u) = \lambda u -\mu vandf(v) = \mu u + \lambda v.$$
Vì $f = f^{*}$,
$$\langle f(u), v\rangle = \langle u, f(v)\rangle$$
Với mọi $u, v \in E$. Áp dụng điều này đến
$$f(u) = \lambda u -\mu vandf(v) = \mu u + \lambda v,$$
Ta thu được
$$\langle f(u), v\rangle = \langle \lambda u -\mu v, v\rangle = \lambda \langle u, v\rangle -\mu \langle v, v\rangle$$
Và
$$\langle u, f(v)\rangle = \langle u, \mu u + \lambda v\rangle = \mu \langle u, u\rangle + \lambda \langle u, v\rangle ,$$
Và do đó ta thu được
$$\lambda \langle u, v\rangle -\mu \langle v, v\rangle = \mu \langle u, u\rangle + \lambda \langle u, v\rangle ,$$
Rằng là,
$$\mu (\langle u, u\rangle + \langle v, v\rangle ) = 0,$$
Mà suy ra $\mu  = 0$, vì hoặc $u \neq  0$ hoặc $v \neq  0$. Vì vậy, $\lambda$ là thực trị riêng (eigenvalue) của $f$. Bây giờ đi quay lại đến chứng minh của Định lý 17.12, chỉ trường hợp ở đâu $\mu  = 0$ áp dụng, và quy nạp chỉ ra rằng tất cả các khối là một chiều.

<!-- PAGE 637 -->
Định lý 17.14 suy ra rằng nếu $\lambda_{1} , \dots  , \lambda_{p}$ là phân biệt thực các trị riêng (eigenvalues) của $f$, và $E_{i}$ là không gian riêng (eigenspace) liên kết với $\lambda_{i}$, thì
$$E = E_{1} \oplus \cdots  \oplus E_{p},$$
Ở đâu $E_{i}$ và $E_{j}$ là trực giao với mọi $i \neq  j$.
Nhận xét: Một cái khác cách để chứng minh rằng tự liên hợp (self-adjoint) ánh xạ có thực trị riêng (eigenvalue) là để sử dụng little bit của vi tích phân. Ta learned như vậy chứng minh từ Herman Gluck. ý tưởng là đến xét nhận giá trị thực (real-valued) hàm $\Phi$: $E \to \mathbb{R}$ được định nghĩa sao cho
$$\Phi (u) = \langle f(u), u\rangle$$
Với mọi $u \in E$. hàm này là $C^{\infty}$, và nếu ta biểu diễn $f$ bởi ma trận $A$ trên một số cơ sở trực chuẩn (orthonormal basis), nó là dễ để tính gradien vectơ
$$\nabla \Phi (X) = \begin{pmatrix} \partial \\ \Phi & \partial \Phi \\ (X), \dots  , & (X) \\ \partial x_{1} & \partial x_{n} \end{pmatrix}$$
Của $\Phi$ tại $X$. Thật vậy, ta tìm rằng
$$\nabla \Phi (X) = (A + A^{\top})X,$$
Ở đâu $X$ là vectơ cột (column vector) của kích thước $n$. Nhưng vì $f$ là tự liên hợp (self-adjoint), $A = A^{\top}$, và do đó
$$\nabla \Phi (X) = 2AX.$$
Tiếp theo bước là để tìm cực đại của hàm $\Phi$ trên mặt cầu
$$\mathbb{R}^{n}$$
$$S^{n-1}= {(x_{1}, \dots  , x_{n}) \in | x_{1}^{2} + \cdots  + x_{n}^{2} = 1}.$$
Vì $S^{n-1}$ là compắc và $\Phi$ là liên tục, và thực ra $C^{\infty}, \Phi$ lấy cực đại tại một số $X$ trên $S^{n-1}$. Nhưng khi đó ta đã biết rõ rằng tại cực trị $X$ của $\Phi$ ta phải có
$$d\Phi_{X} (Y ) = \langle \nabla \Phi (X), Y \rangle = 0$$
Với mọi tiếp tuyến các vectơ $Y$ đến $S^{n-1}$ tại $X$, và do đó $\nabla \Phi (X)$ là trực giao đến tiếp tuyến mặt phẳng tại $X$, mà có nghĩa là
$$\nabla \Phi (X) = \lambda X$$
Với một số $\lambda  \in \mathbb{R}$. Vì $\nabla \Phi (X) =$ 2AX, ta thu được
$$2AX = \lambda X,$$
Và do đó $\lambda /2$ là thực trị riêng (eigenvalue) của $A$ (i.e., của $f)$. Tiếp theo ta xét phản tự liên hợp (skew-self-adjoint) các ánh xạ.

<!-- PAGE 638 -->

> **Định lý 17.15.** Cho trước Không gian Euclid (Euclidean space) $E$ có số chiều $n$, với mọi phản tự liên hợp (skew-self-adjoint) ánh xạ tuyến tính (linear map) $f$: $E \to E$ có một cơ sở trực chuẩn (orthonormal basis) $(e_{1}, \dots  , e_{n})$ sao cho ma trận của $f$ w.r.t. cơ sở (cơ sở (basis)) này là khối ma trận đường chéo (diagonal matrix) của tạo thành
$$\begin{pmatrix} A_{1} & \dots \\ A_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & A_{p} \end{pmatrix}$$
Sao cho mỗi khối $A_{j}$ là hoặc $0$ hoặc hai chiều ma trận của tạo thành
$$A_{j} = \begin{pmatrix} 0 \\ -\mu_{j} \\ \mu_{j} & 0 \end{pmatrix} ,$$
Ở đâu $\mu_{j}  \in \mathbb{R}$, với $\mu_{j}  > 0$. Đặc biệt, các trị riêng (eigenvalues) của $f_{C}$ là thuần túy imaginary của tạo thành $\pm i\mu_{j}$ hoặc $0$.

*Chứng minh.* trường hợp ở đâu $n = 1$ là tầm thường. Như trong chứng minh của Định lý 17.12, $f_{C}$ có một số trị riêng (eigenvalue) $z = \lambda  + i\mu$, ở đâu $\lambda , \mu  \in \mathbb{R}$. Ta khẳng định rằng $\lambda  = 0$. Thứ nhất ta chỉ ra rằng
$$\langle f(w), w\rangle = 0$$
Với mọi $w \in E$. Thật vậy, vì $f = -f^{*}$, ta thu được
$$\langle f(w), w\rangle = \langle w, f^{*} (w)\rangle = \langle w, -f(w)\rangle = -\langle w, f(w)\rangle = -\langle f(w), w\rangle ,$$
Vì $\langle$ -, $-\rangle$ là đối xứng. Điều này suy ra rằng
$$\langle f(w), w\rangle = 0.$$
Áp dụng điều này đến $u$ và $v$ và bằng cách sử dụng sự kiện rằng
$$f(u) = \lambda u -\mu vandf(v) = \mu u + \lambda v,$$
Ta thu được
$$0 = \langle f(u), u\rangle = \langle \lambda u -\mu v, u\rangle = \lambda \langle u, u\rangle -\mu \langle u, v\rangle$$
Và
$$0 = \langle f(v), v\rangle = \langle \mu u + \lambda v, v\rangle = \mu \langle u, v\rangle + \lambda \langle v, v\rangle ,$$
Từ mà, bởi phép cộng, ta thu được
$$\lambda (\langle v, v\rangle + \langle v, v\rangle ) = 0.$$
Vì $u \neq  0$ hoặc $v \neq  0$, ta có $\lambda  = 0$. Thì đi quay lại đến chứng minh của Định lý 17.12, trừ khi $\mu  = 0$, trường hợp ở đâu $u$ và $v$ là trực giao và sinh (span) không gian con có số chiều $2$ áp dụng, và quy nạp chỉ ra rằng tất cả các khối là hai chiều hoặc rút gọn đến $0$.

<!-- PAGE 639 -->
Nhận xét: Một sẽ lưu ý rằng nếu $f$ là phản tự liên hợp (skew-self-adjoint), thì $if_{C}$ là tự liên hợp (self-adjoint) w.r.t. $\langle$ -, $-\rangle_{C}$. Theo Mệnh đề 17.5, ánh xạ $if_{C}$ có thực các trị riêng (eigenvalues), mà suy ra rằng các trị riêng (eigenvalues) của $f_{C}$ là thuần túy imaginary hoặc $0$. Cuối cùng ta xét trực giao các ánh xạ tuyến tính (linear maps).

> **Định lý 17.16.** Cho trước Không gian Euclid (Euclidean space) $E$ có số chiều $n$, với mọi trực giao ánh xạ tuyến tính (linear map) $f$: $E \to E$ có một cơ sở trực chuẩn (orthonormal basis) $(e_{1}, \dots  , e_{n})$ sao cho ma trận của $f$ w.r.t. cơ sở (cơ sở (basis)) này là khối ma trận đường chéo (diagonal matrix) của tạo thành
$$\begin{pmatrix} A_{1} & \dots \\ A_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & A_{p} \end{pmatrix}$$
Sao cho mỗi khối $A_{j}$ là hoặc $1, -1$, hoặc hai chiều ma trận của tạo thành
$$A_{j} = \begin{pmatrix} \cos \theta_{j} & -\sin \theta_{j} \\ \sin \theta_{j} & \cos \theta_{j} \end{pmatrix}$$
Ở đâu $0 < \theta_{j}  < \pi$. Đặc biệt, các trị riêng (eigenvalues) của $f_{C}$ là của tạo thành cos $\theta_{j}  \pm  i$ sin $\theta_{j} , 1$, hoặc $-1$.

*Chứng minh.* trường hợp ở đâu $n = 1$ là tầm thường. Ta kiểm chứng được ngay rằng $f \circ f^{*} = f^{*} \circ f =$ id suy ra rằng $f_{C} \circ f_{C}^{*}  = f_{C}^{*} \circ f_{C} =$ id, do đó ánh xạ $f_{C}$ là unita. Theo Mệnh đề 17.7, các trị riêng (eigenvalues) của $f_{C}$ có tuyệt đối giá trị $1$. Hệ quả là, các trị riêng (eigenvalues) của $f_{C}$ là của tạo thành cos $\theta  \pm  i$ sin $\theta , 1$, hoặc $-1$. định lý thì suy ra ngay lập tức từ Định lý 17.12, ở đâu điều kiện $\mu  > 0$ suy ra rằng sin $\theta_{j}  > 0$, và do đó, $0 < \theta_{j}  < \pi$. Hiển nhiên là ta có thể reorder cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors) cho trước theo Định lý 17.16, sao cho ma trận của $f$ w.r.t. cơ sở (cơ sở (basis)) này là khối ma trận đường chéo (diagonal matrix) của tạo thành
$$\begin{pmatrix} A_{1} & \dots \\ \vdots & \ddots & \vdots & \vdots \\ \dots & A_{r} \\ -I_{q} \\ \dots & I_{p} \end{pmatrix}$$
Ở đâu mỗi khối $A_{j}$ là hai chiều ma trận quay (rotation matrix) $A_{j} \neq  \pm I_{2}$ của tạo thành
$$A_{j} = \begin{pmatrix} \cos \theta_{j} & -\sin \theta_{j} \\ \sin \theta_{j} & \cos \theta_{j} \end{pmatrix}$$
Với $0 < \theta_{j}  < \pi$.

<!-- PAGE 640 -->
Ánh xạ tuyến tính (linear map) $f$ có không gian riêng (eigenspace) E(1, $f) =$ Ker $(f$ - id) có số chiều $p$ cho trị riêng (eigenvalue) $1$, và không gian riêng (eigenspace) E(-1, $f) =$ Ker $(f +$ id) có số chiều $q$ cho trị riêng (eigenvalue) $-1$. Nếu det(f) $= +1 (f$ là phép quay), số chiều $q$ của E(-1, $f)$ phải là chẵn/ngay cả, và các phần tử (entries) trong $-I_{q}$ có thể được được cặp đến tạo thành hai chiều các khối, nếu ta muốn. Trong trường hợp này, mọi phép quay trong Do đó(n) có ma trận của tạo thành
$$\begin{pmatrix} A_{1} & \dots \\ \vdots & \ddots & \vdots \\ \dots & A_{m} \\ \dots & I_{n-2m} \end{pmatrix}$$
Ở đâu thứ nhất $m$ các khối $A_{j}$ là của tạo thành
$$A_{j} = \begin{pmatrix} \cos \theta_{j} & -\sin \theta_{j} \\ \sin \theta_{j} & \cos \theta_{j} \end{pmatrix}$$
Với $0 < \theta_{j}  \le \pi$. Định lý 17.16 có thể được được sử dụng để chứng minh phiên bản của Cartan–Dieudonn´e định lý.

> **Định lý 17.17.** Cho $E$ là Không gian Euclid (Euclidean space) có số chiều $n \ge 2$. Với mọi phép đẳng cự (isometry) $f \in$ O(E), nếu $p =$ dim(E(1, $f)) =$ dim(Ker $(f$ - id)), thì $f$ là hợp thành của $n$ - $p$ các phép đối xứng, và $n$ - $p$ là tối tiểu.

*Chứng minh.* Từ Định lý 17.16 có $r$ các không gian con $F_{1}, \dots  , F_{r}$, mỗi có số chiều $2$, sao cho
$$E = E(1, f) \oplus E(-1, f) \oplus F_{1} \oplus \cdots  \oplus F_{r},$$
Và tất cả summands là đôi một trực giao. Hơn nữa, thu hẹp $r_{i}$ của $f$ đến mỗi $F_{i}$ là phép quay $r_{i} \neq  \pm$ id. Mỗi 2D phép quay $r_{i}$ có thể được viết dưới dạng hợp thành $r_{i} = s_{i}' \circ s_{i}$ của hai các phép đối xứng $s_{i}$ và $s_{i}'$ về các đường thẳng trong $F_{i}$ (tạo thành góc $\theta_{i} /2)$. Ta có thể mở rộng $s_{i}$ và $s_{i}'$ đến siêu phẳng (hyperplane) các phép đối xứng trong $E$ bởi tạo ra chúng đồng nhất thức trên $F_{i}^{\perp}$. Thì
$$s_{r}' \circ s_{r} \circ \cdots  \circ s_{1}' \circ s_{1}$$
Agrees với $f$ trên $F_{1} \oplus \cdots  \oplus F_{r}$ và là đồng nhất thức trên E(1, $f) \oplus$ E(-1, $f)$. Nếu E(-1, $f)$ có cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors) $(v_{1}, \dots  , v_{q})$, đặt $s_{j}''$ là phép đối xứng (reflection) về siêu phẳng (hyperplane) $(v_{j})^{\perp}$, rõ ràng là
$$s_{q}'' \circ \cdots  \circ s_{1}''$$
Agrees với $f$ trên E(-1, $f)$ và là đồng nhất thức trên E(1, $f) \oplus F_{1} \oplus \cdots  \oplus F_{r}$. Nhưng khi đó
$$f = s_{q}'' \circ \cdots  \circ s_{1}'' \circ s_{r}' \circ s_{r} \circ \cdots  \circ s_{1}' \circ s_{1},$$
Hợp thành của 2r $+ q = n$ - $p$ các phép đối xứng.

<!-- PAGE 641 -->
Nếu
$$f = s_{t} \circ \cdots  \circ s_{1},$$
Cho $t$ các phép đối xứng $s_{i}$, rõ ràng là
$$F = \bigcap_{i=1}^{t}  E(1, s_{i}) \subseteq E(1, f),$$
Ở đâu E(1, $s_{i})$ là siêu phẳng (hyperplane) định nghĩa phép đối xứng (reflection) $s_{i}$. Bởi Grassmann quan hệ, nếu ta giao nhau $t \le n$ các siêu phẳng, số chiều của của chúng giao là ít nhất $n$ - $t$. Do đó, n-t $\le p$, nghĩa là, $t \ge$ n-p, và n-p là nhỏ nhất số của các phép đối xứng composing $f$. Như hệ quả của Định lý 17.17, ta thu được kết quả sau sự kiện: Nếu số chiều $n$ của Không gian Euclid (Euclidean space) $E$ là lẻ, thì mọi phép quay $f \in$ Do đó(E) admits $1$ như trị riêng (eigenvalue).

*Chứng minh.* đa thức đặc trưng (characteristic polynomial) det(XI - $f)$ của $f$ có lẻ bậc $n$ và có thực các hệ số, do đó nó phải có một số thực nghiệm (root) $\lambda$. Vì $f$ là phép đẳng cự (isometry), của nó $n$ các trị riêng (eigenvalues) là của tạo thành, $+1, -1$, và $e^{\pm i\theta}$, với $0 < \theta  < \pi$, do đó $\lambda  = \pm 1$. Bây giờ các trị riêng (eigenvalues) $e^{\pm i\theta}$ xuất hiện trong liên hợp các cặp, và vì $n$ là lẻ, số của thực các trị riêng (eigenvalues) của $f$ là lẻ. Điều này suy ra rằng $+1$ là trị riêng (eigenvalue) của $f$, vì ngược lại $-1$ sẽ là chỉ thực trị riêng (eigenvalue) của $f$, và vì của nó bội (multiplicity) là lẻ, ta sẽ có det(f) $= -1$, contradicting sự kiện rằng $f$ là phép quay. Khi $n = 3$, ta thu được kết quả do Euler mà nói rằng rằng mọi 3D phép quay $R$ có bất biến trục $D$, và rằng bị thu hẹp đến mặt phẳng trực giao đến $D$, nó là 2D phép quay. Hơn nữa, nếu (, $b, c)$ là unit vectơ định nghĩa trục $D$ của phép quay $R$ và nếu góc của phép quay là $\theta$, nếu $B$ là ma trận phản đối xứng (skew-symmetric matrix)
$$B = \begin{pmatrix} 0 & -c & b \\ c & 0 & -a \\ b & a & 0 \end{pmatrix} ,$$
$$-$$
Thì Rodigues công thức (Mệnh đề 12.15) phát biểu rằng
$$R = I + \sin \theta B + (1 -\cos \theta )B^{2}.$$
Các định lý của điều này mục và của trước đó mục có thể được ngay lập tức translated theo các ma trận. ma trận các phiên bản của các phần tử này các định lý là thường được sử dụng trong các ứng dụng do đó ta ngắn gọn trình bày chúng trong mục.
