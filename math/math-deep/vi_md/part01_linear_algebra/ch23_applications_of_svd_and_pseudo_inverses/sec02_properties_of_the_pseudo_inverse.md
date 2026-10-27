# Các tính chất của Nghịch đảo giả (pseudo-inverse)


<!-- PAGE 776 -->

## 23.2 Các tính chất của Nghịch đảo giả (pseudo-inverse)

Ta bắt đầu điều này mục với mệnh đề mà cung cấp cách để tính toán nghịch đảo giả (pseudo-inverse) của một ma trận cỡ $m \times  n$ $A$ mà không có thứ nhất xác định SVD nhân tử hóa.

> **Mệnh đề 23.3.** Khi $A$ có đầy đủ hạng (rank), nghịch đảo giả (pseudo-inverse) $A^{+}$ có thể được biểu diễn dưới dạng $A^{+} = (A^{\top}A)^{-1}A^{\top}$ khi $m \ge n$, và như $A^{+} = A^{\top}(AA^{\top})^{-1}$ khi $n \ge m$. Trong trường hợp thứ nhất $(m \ge n)$, nhận thấy rằng $A^{+}A =$ I, do đó $A^{+}$ là nghịch đảo trái (left inverse) của $A$; trong trường hợp thứ hai $(n \ge m)$, ta có $AA^{+} =$ I, do đó $A^{+}$ là nghịch đảo phải (right inverse) của $A$.

*Chứng minh.* Nếu $m \ge n$ và $A$ có đầy đủ hạng (rank) $n$, ta có
$$A = V \begin{pmatrix} \Lambda \\ 0_{m-n,n} \end{pmatrix} U^{\top}$$
Với $\Lambda$ $n \times  n$ đường chéo ma trận khả nghịch (invertible matrix) (với dương các phần tử (entries)), do đó
$$A^{+}= U \begin{pmatrix} \Lambda^{-1} & 0_{n,m-n} \end{pmatrix} V^{\top}.$$
Ta tìm rằng
$$A^{\top}A = U \begin{pmatrix} \Lambda & 0_{n,m-n} \end{pmatrix} V^{\top} V \begin{pmatrix} \Lambda \\ 0_{m-n,n} \end{pmatrix} U^{\top} = U\Lambda^{2} U^{\top} ,$$
Mà cho ta
$$(A^{\top}A)^{-1}A^{\top}= U\Lambda^{-2} U^{\top} U \begin{pmatrix} \Lambda & 0_{n,m-n} \\ rankn,then \end{pmatrix} V^{\top} = U \begin{pmatrix} \Lambda^{-1} & 0_{n,m-n} \end{pmatrix} V^{\top} = A^{+}.$$
Vì vậy, nếu $m \ge n$ và $A$ có đầy đủ
$$A^{+}= (A^{\top}A)^{-1}A^{\top}.$$
Nếu $n \ge m$ và $A$ có đầy đủ hạng (rank) $m$, thì
$$A = V \begin{pmatrix} \Lambda & 0_{m,n-m} \\ (with \end{pmatrix} U^{\top}$$
Với $\Lambda$ $m \times  m$ đường chéo ma trận khả nghịch (invertible matrix) dương các phần tử (entries)), do đó
$$A^{+}= U \begin{pmatrix} \Lambda^{-1} \\ 0_{n-m,m} \end{pmatrix} V^{\top}.$$
Ta tìm rằng
$$AA^{\top}= V \begin{pmatrix} \Lambda & 0_{m,n-m} \end{pmatrix} U^{\top} U \begin{pmatrix} \Lambda \\ 0_{n-m,m} \end{pmatrix} V^{\top} = V \Lambda^{2} V^{\top} ,$$
Mà cho ta
$$A^{\top}(AA^{\top})^{-1}= U \begin{pmatrix} \Lambda \\ 0_{n-m,m} \end{pmatrix} V^{\top}V \Lambda^{-2} V^{\top}= U \begin{pmatrix} \Lambda^{-1} \\ 0_{n-m,m} \end{pmatrix} V^{\top}= A^{+}.$$
Vì vậy, nếu $n \ge m$ và $A$ có đầy đủ hạng (rank) $m$, thì $A^{+} = A^{\top}(AA^{\top})^{-1}$.

<!-- PAGE 777 -->
$$For example, if A = \begin{pmatrix} 1 & 2 \\ 2 & 3 \\ 0 & 1 \end{pmatrix} , then A has \mathrm{rank} 2 and since m \ge n, A^{+} = (A^{\top}A)^{-1}A^{\top}$$
Ở đâu
$$8^{-1}$$
$$A^{+}= \begin{pmatrix} 5 \\ 8 & 14 \end{pmatrix} A^{\top}= \begin{pmatrix} 7/3 & -4/3 \\ -4/3 & 5/6 \end{pmatrix} \begin{pmatrix} 1 & 2 & 0 \\ 2 & 3 & 1 \end{pmatrix} = \begin{pmatrix} -1/3 & 2/3 & -4/3 \\ 1/3 & -1/6 & 5/6 \end{pmatrix} .$$
$$If A = \begin{pmatrix} 1 & 2 & 3 & 0 \\ 0 & 1 & 1 & -1 \end{pmatrix} , since A has \mathrm{rank} 2 and n \ge m, then A^{+}= A^{\top}(AA^{\top})^{-1}where$$
$$A^{+} = A^{\top} \begin{pmatrix} 14 \\ 5 & 3 \end{pmatrix} 5^{-1}= \begin{pmatrix} 1 & 0 \\ 2 & 1 \\ 3 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 3/17 & -5/17 \\ -5/17 & 14/17 \end{pmatrix} = \begin{pmatrix} 3/17 & -5/17 \\ 1/17 & 4/17 \\ 4/17 & -1/17 \\ 5/17 & 14/17 \end{pmatrix} .$$
$$--$$
Cho $A = V \Sigma U^{\top}$ là SVD cho bất kỳ ma trận cỡ $m \times  n$ $A$. Nó là dễ để kiểm tra rằng cả hai $AA^{+}$ và $A^{+}A$ là các ma trận đối xứng. Thực ra,
$$AA^{+}= V \Sigma U^{\top}U\Sigma^{+} V^{\top}= V \Sigma \Sigma^{+} V^{\top}= V \begin{pmatrix} I_{r} & 0 \\ 0 & 0_{m-r} \end{pmatrix} V^{\top}$$
Và
$$A^{+}A = U\Sigma^{+} V^{\top} V \Sigma U^{\top} = U\Sigma^{+} \Sigma U^{\top} = U \begin{pmatrix} I_{r} & 0 \\ 0 & 0_{n-r} \end{pmatrix} U^{\top} .$$
Từ ở trên các biểu thức ta ngay lập tức suy ra rằng
$$AA^{+}A=A,$$
$$A^{+}AA^{+}=A^{+},$$
Và rằng
$$(AA^{+})^{2}=AA^{+},$$
$$(A^{+}A)^{2}=A^{+}A,$$
Do đó cả hai $AA^{+}$ và $A^{+}A$ là trực giao các phép chiếu (vì chúng là cả hai đối xứng).

> **Mệnh đề 23.4.** ma trận $AA^{+}$ là phép chiếu trực giao (orthogonal projection) lên miền giá trị (range) của $A$ và $A^{+}A$ là phép chiếu trực giao (orthogonal projection) lên $Ker(A)^{\perp} = Im(A^{\top})$, miền giá trị (range) của $A^{\top}$.

*Chứng minh.* Hiển nhiên, ta có $range(AA^{+}) \subseteq$ miền giá trị (range)(), và với mọi $y =$ Ax $\in$ miền giá trị (range)(), vì $AA^{+}A = A$, ta có
$$AA^{+}y = AA^{+}Ax = Ax = y,$$

<!-- PAGE 778 -->
Do đó ảnh (image) của $AA^{+}$ là thật vậy miền giá trị (range) của $A$. Nó là cũng rõ ràng rằng Ker() $\subseteq Ker(A^{+}A)$, và vì $AA^{+}A = A$, ta cũng có $Ker(A^{+}A) \subseteq$ Ker(), và do đó
$$\mathrm{Ker}(A^{+}A) = \mathrm{Ker}(A).$$
Vì $A^{+}A$ là đối xứng, $range(A^{+}A) = range((A^{+}A)^{\top}) = Ker(A^{+}A)^{\perp} = Ker(A)^{\perp}$, như đã khẳng định.
$$\mathbb{R}^{m}$$

> **Mệnh đề 23.5.** tập hợp miền giá trị (range)() $= range(AA^{+})$ bao gồm của tất cả các vectơ $y \in$ sao cho
$$V^{\top} y = \begin{pmatrix} z \\ 0 \end{pmatrix} ,$$
Với $z \in \mathbb{R}^{r}$.

*Chứng minh.* Thật vậy, nếu $y =$ Ax, thì
$$V^{\top} y = V^{\top} Ax = V^{\top} V \Sigma U^{\top} x = \Sigma U^{\top} x = \begin{pmatrix} \Sigma_{r} & 0 \\ 0 & 0_{m-r} \end{pmatrix} U^{\top} x = \begin{pmatrix} z \\ 0 \end{pmatrix} ,$$
Ở đâu $\Sigma_{r}$ là $r \times  r$ ma trận đường chéo (diagonal matrix) $diag(\sigma_{1} , \dots  , \sigma_{r}$). Ngược lại, nếu $V^{\top} y = (_{0}^{z}$), thì $y = V (_{0}^{z}$), và
$$AA^{+}y = V \begin{pmatrix} I_{r} & 0 \\ 0 & 0_{m-r} \end{pmatrix} V^{\top} y$$
$$= V \begin{pmatrix} I_{r} & 0 \\ 0 & 0_{m-r} \end{pmatrix} V^{\top} V \begin{pmatrix} z \\ 0 \end{pmatrix}$$
$$= V \begin{pmatrix} I_{r} & 0 \\ 0 & 0_{m-r} \\  \end{pmatrix} \begin{pmatrix} z \\ 0 \end{pmatrix}$$
$$= V \begin{pmatrix} z \\ 0 \end{pmatrix} = y,$$
Mà chỉ ra rằng $y$ thuộc đến miền giá trị (range) của $A$. Tương tự, ta có kết quả sau kết quả.
$$\mathbb{R}^{n}$$

> **Mệnh đề 23.6.** tập hợp $range(A^{+}A) = Ker(A)^{\perp}$ bao gồm của tất cả các vectơ $y \in$ sao cho
$$U^{\top} y = \begin{pmatrix} z \\ 0 \end{pmatrix} ,$$
Với $z \in \mathbb{R}^{r}$.

<!-- PAGE 779 -->

*Chứng minh.* Nếu $y = A^{+}Au$, thì
$$y = A^{+}Au = U \begin{pmatrix} I_{r} & 0 \\ 0 & 0_{n-r} \end{pmatrix} U^{\top} u = U \begin{pmatrix} z \\ 0 \end{pmatrix} ,$$
Với một số $z \in \mathbb{R}^{r}$. Ngược lại, nếu $U^{\top} y = (_{0}^{z}$), thì $y = U (_{0}^{z}$), và do đó
$$A^{+}AU \begin{pmatrix} z \\ 0 \end{pmatrix} = U \begin{pmatrix} I_{r} & 0 \\ 0 & 0_{n-r} \end{pmatrix} U^{\top} U \begin{pmatrix} z \\ 0 \end{pmatrix}$$
$$= U \begin{pmatrix} I_{r} & 0 \\ 0 & 0_{n-r} \\  \end{pmatrix} \begin{pmatrix} z \\ 0 \end{pmatrix}$$
$$= U \begin{pmatrix} z \\ 0 \end{pmatrix} = y,$$
Mà chỉ ra rằng $y \in range(A^{+}A)$. Tương tự các kết quả đúng cho phức các ma trận, nhưng trong trường hợp này, $V$ và $U$ là các ma trận unita và $AA^{+}$ và $A^{+}A$ là Hermite trực giao các phép chiếu. Nếu $A$ là ma trận chuẩn tắc (normal matrix), mà có nghĩa là $AA^{\top} = A^{\top}A$, thì có một intimate relationship giữa SVD’s của $A$ và khối các sự chéo hóa của $A$. Hệ quả là, nghịch đảo giả (pseudo-inverse) của ma trận chuẩn tắc (normal matrix) $A$ có thể được thu được một cách trực tiếp từ khối sự chéo hóa của $A$. Nếu $A$ là (thực) ma trận chuẩn tắc (normal matrix), thì ta biết từ Định lý 17.18 rằng $A$ có thể được khối được chéo hóa đối với ma trận trực giao (orthogonal matrix) $U$ như
$$A = U\Lambda U^{\top} ,$$
Ở đâu $\Lambda$ là (thực) khối ma trận đường chéo (diagonal matrix)
$$\Lambda  = \mathrm{diag}(B_{1}, \dots  , B_{n}),$$
Bao gồm hoặc của $2 \times  2$ các khối của tạo thành
$$B_{j} = \begin{pmatrix} \lambda_{j} & -\mu_{j} \\ \mu_{j} & \lambda_{j} \end{pmatrix}$$
Với $\mu_{j}  \neq  0$, hoặc của một chiều các khối $B_{k} = (\lambda_{k}$). Thì ta có kết quả sau mệnh đề:

> **Mệnh đề 23.7.** Với mọi (thực) ma trận chuẩn tắc (normal matrix) $A$ và bất kỳ khối sự chéo hóa $A = U\Lambda U^{\top}$ của $A$ như ở trên, nghịch đảo giả (pseudo-inverse) của $A$ được cho bởi
$$A^{+}= U\Lambda^{+} U^{\top},$$
Ở đâu $\Lambda^{+}$ là nghịch đảo giả (pseudo-inverse) của $\Lambda$. Hơn nữa, nếu
$$\Lambda  = \begin{pmatrix} \Lambda_{r} & 0 \\ 0 & 0 \end{pmatrix} ,$$

<!-- PAGE 780 -->
Ở đâu $\Lambda_{r}$ có hạng (rank) $r$, thì
$$\Lambda^{+} = \begin{pmatrix} \Lambda_{r}^{-1} & 0 \\ 0 & 0 \end{pmatrix} .$$

*Chứng minh.* Giả sử rằng $B_{1}, \dots  , B_{p}$ là $2\times 2$ các khối và rằng $\lambda_{2p+1} , \dots  , \lambda_{n}$ là vô hướng (scalar) các phần tử (entries).
$$We know \frac{that}{\lambda_{j}^{2} + \mu_{j}^{2}} the numbers \lambda_{j}  \pm  i\mu_{j} , and the \lambda_{2p+k}  are the eigenvalues of A. Let \rho_{2j-1}  =$$
$q p \rho_{2j}  =   = \overline{det(}\overline{B}_{i}\overline{)}$ cho $j = 1, \dots  , p, \rho_{j}  = |\lambda_{j}$ | cho $j =$ 2p $+ 1, \dots  , r$. Nhân $U$ bởi phù hợp hoán vị ma trận, ta có thể giả sử rằng các khối của $\Lambda$ được thứ tự sao cho $\rho_{1}  \ge \rho_{2}  \ge \cdots  \ge \rho_{r}  > 0$. Thì nó là dễ để xem rằng
$$AA^{\top}= A^{\top}A = U\Lambda U^{\top} U\Lambda^{\top} U^{\top} = U\Lambda \Lambda^{\top} U^{\top} ,$$
Với
$$\Lambda \Lambda^{\top} = \mathrm{diag}(\rho_{1}^{2} , \dots  , \rho_{r}^{2} , 0, \dots  , 0),$$
Do đó $\rho_{1}  \ge \rho_{2}  \ge \cdots  \ge \rho_{r}  > 0$ là các giá trị kỳ dị (singular values) $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{r}  > 0$ của $A$. Định nghĩa ma trận đường chéo (diagonal matrix)
$$\Sigma  = \mathrm{diag}(\sigma_{1} , \dots  , \sigma_{r} , 0, \dots  , 0),$$
$$where r = \mathrm{rank}(A), \sigma_{1}  \ge \cdots  \ge \sigma_{r}  > 0 and the block diagonalp \frac{matrix}{\det(B_{i}),} \Theta  defined such that$$
Khối $B_{i}$ trong $\Lambda$ được thay thế bởi khối $\sigma^{-1} B_{i}$ ở đâu $\sigma  =$ khác không vô hướng (scalar) $\lambda_{j}$ được thay thế $\lambda_{j} /|\lambda_{j}$ |, và đường chéo không được thay thế bởi $1$. Nhận thấy rằng $\Theta$ là ma trận trực giao (orthogonal matrix) và
$$\Lambda  = \Theta \Sigma .$$
Nhưng khi đó ta có thể viết
$$A = U\Lambda U^{\top} = U\Theta \Sigma U^{\top} ,$$
Và ta nếu cho $V = U\Theta$, vì $U$ là trực giao và $\Theta$ là cũng trực giao, $V$ là cũng trực giao và $A = V \Sigma U^{\top}$ là SVD cho $A$. Bây giờ ta thu được
$$A^{+}= U\Sigma^{+} V^{\top}= U\Sigma^{+} \Theta^{\top} U^{\top}.$$
Tuy nhiên, vì $\Theta$ là ma trận trực giao (orthogonal matrix), $\Theta^{\top} = \Theta^{-1}$, và đơn giản phép tính chỉ ra rằng
$$\Sigma^{+} \Theta^{\top} = \Sigma^{+} \Theta^{-1} = \Lambda^{+} ,$$
Mà cho ta công thức
$$A^{+}= U\Lambda^{+} U^{\top}.$$
Cũng nhận thấy rằng $\Lambda_{r}$ là khả nghịch và
$$\Lambda^{+} = \begin{pmatrix} \Lambda_{r}^{-1} & 0 \\ 0 & 0 \end{pmatrix} .$$
Vì vậy, nghịch đảo giả (pseudo-inverse) của ma trận chuẩn tắc (normal matrix) có thể được được tính một cách trực tiếp từ bất kỳ khối sự chéo hóa của $A$, như đã khẳng định.
