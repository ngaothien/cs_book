# điều kiện của Trị riêng (eigenvalue) Các bài tập


<!-- PAGE 585 -->

## 15.4 điều kiện của Trị riêng (eigenvalue) Các bài tập

Sau đây $n \times  n$ ma trận
$$A = \begin{pmatrix} 0 \\ 1 & 0 \\ 1 & 0 \\ \ddots & \ddots \\ 1 & 0 \\ 1 & 0 \end{pmatrix}$$
Có trị riêng (eigenvalue) $0$ với bội (multiplicity) $n$. Tuy nhiên, nếu ta perturb đỉnh/trên rightmost phần tử (entry) của $A$ bởi $\epsilon$, nó là dễ để xem rằng đa thức đặc trưng (characteristic polynomial) của ma trận
$$A(\epsilon ) = \begin{pmatrix} 0 & \epsilon \\ 1 & 0 \\ 1 & 0 \\ \ddots & \ddots \\ 1 & 0 \\ 1 & 0 \end{pmatrix}$$
Là $X^{n}$ - $\epsilon$. Suy ra rằng nếu $n = 40$ và $\epsilon  = 10^{-40}, A(10^{-40})$ có các trị riêng (eigenvalues) $10^{-1}e^{k2\pi i/40}$ với $k = 1, \dots  , 40$. Do đó, ta xem rằng rất nhỏ thay đổi $(\epsilon  = 10^{-40})$ đến ma trận $A$ gây ra đáng kể thay đổi đến các trị riêng (eigenvalues) của $A$ (từ $0$ đến $10^{-1}e^{k2\pi i/40}$). Thật vậy, tương đối sai số là $10^{-39}$. Tệ hơn, do máy precision, vì rất nhỏ các số là treated như $0$, sai số trên phép tính của các trị riêng (eigenvalues) (ví dụ, của ma trận $A(10^{-40}))$ có thể được rất lớn. Điều này hiện tượng là đồng dạng đến hiện tượng được thảo luận trong Mục 9.5 ở đâu ta studied effect của nhỏ perturbation của các hệ số của hệ phương trình tuyến tính Ax $= b$ trên nghiệm của nó. Trong Mục 9.5, ta đã thấy rằng behavior của hệ phương trình tuyến tính dưới nhỏ perturbations là governed bởi số điều kiện (condition number) cond() của ma trận $A$. Trong trường hợp của trị riêng (eigenvalue) bài toán (việc tìm các trị riêng (eigenvalues) của ma trận), ta sẽ xem rằng điều kiện của bài toán phụ thuộc vào số điều kiện (condition number) của ma trận chuyển cơ sở (change of basis matrix) $P$ được sử dụng trong rút gọn ma trận $A$ đến của nó đường chéo tạo thành $D = P^{-1}$ AP, thay vì trên số điều kiện (condition number) của $A$ chính nó. sau đây mệnh đề trong mà ta giả sử rằng $A$ là chéo hóa được (diagonalizable) và rằng chuẩn ma trận (matrix norm) $\|\|$ thỏa mãn đặc biệt điều kiện (được thỏa mãn bởi toán tử các chuẩn $\|\|_{p}$ cho $p = 1, 2, \infty$), là do Bauer và Fike $(1960)$.

> **Mệnh đề 15.11.** Cho $A \in M_{n}(\mathbb{C})$ là chéo hóa được (diagonalizable) ma trận, $P$ là ma trận khả nghịch (invertible matrix), và $D$ là ma trận đường chéo (diagonal matrix) $D = diag(\lambda_{1} , \dots  , \lambda_{n}$) sao cho
$$A = PDP^{-1} ,$$

<!-- PAGE 586 -->
Và cho $\|\|$ là chuẩn ma trận (matrix norm) sao cho
$$\|\mathrm{diag}(\alpha_{1} , \dots  , \alpha_{n} )\|= \max |\alpha_{i} |,$$
$$1\le i\le n$$
Với mọi ma trận đường chéo (diagonal matrix). Thì với mọi perturbation ma trận $\Delta A$, nếu ta viết
$$B_{i} = {z \in \mathbb{C} | |z -\lambda_{i} | \le cond(P) \|\Delta A\|},$$
Với mọi trị riêng (eigenvalue) $\lambda$ của $A + \Delta A$, ta có
$$\lambda  \in \bigcup_{k=1}^{n}  B_{k}.$$

*Chứng minh.* Cho $\lambda$ là bất kỳ trị riêng (eigenvalue) của ma trận $A + \Delta A$. Nếu $\lambda  = \lambda_{j}$ với một số $j$, thì kết quả là tầm thường. Do đó giả sử rằng $\lambda$ ̸ $= \lambda_{j}$ cho $j = 1, \dots  , n$. Trong trường hợp này ma trận $D$ - $\lambda$ I là khả nghịch (vì các trị riêng (các trị riêng (eigenvalues)) của nó là $\lambda$ - $\lambda_{j}$ cho $j = 1, \dots  , n)$, và ta có
$$P^{-1} (A + \Delta A -\lambda I)P = D -\lambda I + P^{-1} (\Delta A)P$$
$$= (D -\lambda I)(I + (D -\lambda I)^{-1}P^{-1} (\Delta A)P).$$
Vì $\lambda$ là trị riêng (eigenvalue) của $A + \Delta A$, ma trận $A + \Delta A$ - $\lambda$ I là suy biến, do đó ma trận
$$I + (D -\lambda I)^{-1}P^{-1} (\Delta A)P$$
Phải cũng là suy biến. Theo Mệnh đề 9.12(2), ta có
$$1 \le

$(D -\lambda I)^{-1}P^{-1}(\Delta$)P

,$$ and since $\|\|$ là chuẩn ma trận (matrix norm),
$$(D -\lambda I)^{-1}P^{-1}(\Delta A)P

$\le$

$(D -\lambda I)^{-1}$



$P^{-1}$

$\|\Delta A\|\|P\|,$$$ do đó ta có
$$1 \le

$(D -\lambda I)^{-1}$



$P^{-1}$

$\|\Delta A\|\|P\|.$$$ Now $(D$ - $\lambda I)^{-1}$ is a diagonal matrix with entries $1/(\lambda_{i}$  - $\lambda$), do đó bởi của ta giả định trên chuẩn (norm),
$$(D -\lambda I)^{-1}

$= \frac{1}{min_{i}(|\lambda_{i}  -\lambda |)}$.$$ As a consequence, since there is some index $k$ for which $min_{i}(|\lambda_{i}$  - $\lambda$ |) $= |\lambda_{k}$  - $\lambda$ |, ta có
$$(D -\lambda I)^{-1}

$= \frac{1}{|\lambda_{k}  -\lambda |}$,$$ và ta thu được
$$|\lambda  -\lambda_{k} | \le

$P^{-1}$

$\|\Delta A\|\|P\|=$ cond(P) $\|\Delta A\|,$$$ mà chứng minh kết quả của chúng ta.
