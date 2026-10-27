# Các bất đẳng thức Liên quan đến Phụ thuộc Các chuẩn


<!-- PAGE 362 -->

## 9.4 Các bất đẳng thức Liên quan đến Phụ thuộc Các chuẩn

Trong mục này ta thảo luận hai technical các bất đẳng thức mà sẽ là cần thiết cho nhất định các chứng minh trong cuối cùng ba các mục của điều này chương. Thứ nhất ta chứng minh mệnh đề mà sẽ là cần thiết khi ta deal với số điều kiện (condition number) của ma trận.

> **Mệnh đề 9.12.** Cho $\|\|$ là bất kỳ chuẩn ma trận (matrix norm), và cho $B \in M_{n}(\mathbb{C})$ sao cho $\|B\| < 1$.
$(1)$ Nếu $\|\|$ là chuẩn ma trận phụ thuộc (subordinate matrix norm), thì ma trận $I + B$ là khả nghịch và
$$(I + B)^{-1}

$\le \frac{1}{1 -\|B\|}$.$$
$(2)$ Nếu ma trận của tạo thành I $+ B$ là suy biến, thì $\|B\|\ge 1$ với mọi chuẩn ma trận (matrix norm) (không nhất thiết phụ thuộc).

*Chứng minh.* $(1)$ Nhận thấy rằng (I $+$ B)u $= 0$ suy ra Bu $= -u$, do đó
$$\|u\|= \|Bu\|.$$
Nhắc lại rằng
$$\|Bu\|\le \|B\|\|u\|$$
Với mọi phụ thuộc chuẩn (norm). Vì $\|B\| < 1$, nếu $u \neq  0$, thì
$$\|Bu\|< \|u\|,$$
Mà contradicts $\|u\| = \|Bu\|$. Vì vậy, ta phải có $u = 0$, mà chứng tỏ rằng I $+ B$ là đơn ánh (injective), và do đó song ánh (bijective), i.e., khả nghịch. Thì ta có
$$(I + B)^{-1}+ B(I + B)^{-1}= (I + B)(I + B)^{-1}= I,$$
Do đó ta thu được
$$(I + B)^{-1}= I -B(I + B)^{-1},$$
Mà cho ta
$$(I + B)^{-1}

$\le 1 + \|B\|$

(I $+ B)^{-1}$

,$$ và cuối cùng,
$$(I + B)^{-1}

$\le \frac{1}{1 -\|B\|}$.$$
$(2)$ Nếu I $+ B$ là suy biến, thì $-1$ là trị riêng (eigenvalue) của $B$, và theo Mệnh đề 9.7, ta thu được $\rho (B) \le \|B\|$, mà suy ra $1 \le \rho (B) \le \|B\|$. thứ hai bất đẳng thức là kết quả là rằng là cần thiết đến deal với sự hội tụ của các dãy của các lũy thừa của các ma trận.

<!-- PAGE 363 -->

> **Mệnh đề 9.13.** Với mọi ma trận $A \in M_{n}(\mathbb{C})$ và với mọi $\epsilon  > 0$, tồn tại một chuẩn ma trận phụ thuộc (subordinate matrix norm) $\|\|$ sao cho
$$\|A\|\le \rho (A) + \epsilon .$$

*Chứng minh.* Theo Định lý 15.5, tồn tại một ma trận khả nghịch (invertible matrix) $U$ và một số tam giác trên (upper triangular) ma trận $T$ sao cho
$$A = UTU^{-1} ,$$
Và nói rằng
$$T = \begin{pmatrix} \lambda_{1} & t_{12} & t_{13} & \cdots & t_{1n} \\ 0 & \lambda_{2} & t_{23} & \cdots & t_{2n} \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & \lambda_{n-1} & t_{n-1n} \\ 0 & 0 & \cdots & 0 & \lambda_{n} \end{pmatrix} ,$$
Ở đâu $\lambda_{1} , \dots  , \lambda_{n}$ là các trị riêng (eigenvalues) của $A$. Với mọi $\delta  \neq  0$, định nghĩa ma trận đường chéo (diagonal matrix)
$$D_{\delta} = \mathrm{diag}(1, \delta , \delta^{2} , \dots  , \delta^{n-1} ),$$
Và xét ma trận
$$(UD_{\delta})^{-1}A(UD_{\delta}) = D_{\delta}^{-1} TD_{\delta} = \begin{pmatrix} \lambda_{1} & \delta t_{12} & \delta^{2} t_{13} & \cdots & \delta^{n-1} t_{1n} \\ 0 & \lambda_{2} & \delta t_{23} & \cdots & \delta^{n-2} t_{2n} \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & \lambda_{n-1} & \delta t_{n-1n} \\ 0 & 0 & \cdots & 0 & \lambda_{n} \end{pmatrix} .$$
Bây giờ định nghĩa hàm $\|\|: M_{n}(\mathbb{C}) \to \mathbb{R}$ bởi
$$\|B\|=

$(UD_{\delta})^{-1}B(UD_{\delta})_{\infty},$$$ for every $B \trong M_{n}(\mathbb{C})$. Thì nó là dễ để kiểm chứng rằng ở trên hàm là chuẩn ma trận (matrix norm) phụ thuộc đến chuẩn vectơ (vector norm)
$$v \mapsto

$(UD_{\delta})^{-1}v_{\infty}.$$$ Furthermore, for every $\epsilon > 0$, we can pick $\delta$ sao cho
$$\sum_{j=i+1}^{n}  |\delta^{j-i} t_{ij}| \le \epsilon ,1 \le i \le n -1,$$
Và theo định nghĩa của chuẩn (norm) $\|\|_{\infty}$, ta thu được
$$\|A\|\le \rho (A) + \epsilon ,$$
Mà chỉ ra rằng chuẩn (norm) rằng ta có được xây dựng thỏa mãn cần thiết các tính chất.
