# Tốt nhất Afin Xấp xỉ


<!-- PAGE 794 -->
Nói chung, vì SVD của $X$ là không duy nhất, chính các hướng $u_{1}, \dots  , u_{d}$ là không duy nhất. Điều này có thể xảy ra khi dữ liệu tập hợp có một số rotational các phép đối xứng, và trong như vậy trường hợp, PCA là không rất tốt phương pháp cho analyzing dữ liệu tập hợp.

## 23.5 Tốt nhất Afin Xấp xỉ

Bài toán rất close đến PCA (và based trên bình phương tối thiểu (least squares)) là đến tốt nhất xấp xỉ dữ liệu tập hợp của $n$ các điểm $X_{1}, \dots  , X_{n}$, với $X_{i} \in \mathbb{R}^{d}$, bởi $p$ chiều không gian con afin (affine subspace) $A$ của $\mathbb{R}^{d}$, với $1 \le p \le d$ - $1$ (thuật ngữ hạng (rank) $d$ - $p$ cũng được sử dụng). Thứ nhất xét $p = d -1$. Thì $A = A_{1}$ là afin siêu phẳng (hyperplane) (trong $\mathbb{R}^{d})$, và nó được cho bởi phương trình của tạo thành
$$a_{1}x_{1} + \cdots  + a_{d}x_{d} + c = 0.$$
Bởi tốt nhất xấp xỉ, ta có nghĩa rằng $(a_{1}, \dots  , a_{d}, c)$ giải thuần nhất hệ phương trình tuyến tính
$$\begin{pmatrix} x_{1 1} & \cdots & x_{1d} & 1 \\ \vdots & \vdots & \vdots & \vdots \\ x_{n1} & \cdots & x_{n d} & 1 \end{pmatrix} \begin{pmatrix} a_{1} \\ \vdots \\ a_{d} \\ c \end{pmatrix} = \begin{pmatrix} 0 \\ \vdots \\ 0 \\ 0 \end{pmatrix}$$
Trong bình phương tối thiểu (least squares) nghĩa, subject đến điều kiện rằng $a = (a_{1}, \dots  , a_{d})$ là unit vectơ, nghĩa là, $a^{\top}a = 1$, ở đâu $X_{i} = (x_{i1}, \cdots  , x_{i d})$. Nếu ta tạo thành ma trận đối xứng (symmetric matrix)
$$1^{\top}$$
$$\begin{pmatrix} x_{1 1} & \cdots & x_{1d} \\ \vdots & \vdots & \vdots & \vdots \\ x_{n1} & \cdots & x_{n d} & 1 \end{pmatrix} \begin{pmatrix} x_{1 1} & \cdots & x_{1d} & 1 \\ \vdots & \vdots & \vdots & \vdots \\ x_{n1} & \cdots & x_{n d} & 1 \end{pmatrix}$$
Liên quan trong chuẩn tắc/bình thường các phương trình, ta xem rằng đáy/dưới hàng (và cột cuối cùng) của rằng ma trận là
$$n\mu_{1} \cdots n\mu_{d} n,$$
$$where n\mu_{j}  = \sum_{i}  n=1 x_{i j} is n times the mean of the column C_{j} of X.$$
Vì vậy, nếu $(a_{1}, \dots  , a_{d}, c)$ là bình phương tối thiểu (least squares) nghiệm, nghĩa là, nghiệm của chuẩn tắc/bình thường các phương trình, ta phải có
$$n\mu_{1} a_{1} + \cdots  + n\mu_{d} a_{d} + nc = 0,$$
Rằng là,
$$a_{1}\mu_{1}  + \cdots  + a_{d}\mu_{d}  + c = 0,$$
Mà có nghĩa là siêu phẳng (hyperplane) $A_{1}$ phải đi qua qua trọng tâm $\mu$ của dữ liệu các điểm $X_{1}, \dots  , X_{n}$. Thì ta có thể viết lại ban đầu hệ đối với được tâm dữ liệu $X_{i}$ - $\mu$, tìm rằng biến $c$ các bỏ ra, thu được hệ
$$(X -\mu )a = 0,$$

<!-- PAGE 795 -->
Ở đâu $a = (a_{1}, \dots  , a_{d})$. Do đó, ta là nhìn cho unit vectơ việc giải $(X$ - $\mu )a = 0$ trong bình phương tối thiểu (least squares) nghĩa, nghĩa là, một số sao cho $a^{\top}a = 1$ cực tiểu hóa
$$a^{\top}(X -\mu )^{\top}(X -\mu )a.$$
Tính một số SVD $V DU^{\top}$ của $X -\mu$, ở đâu chính đường chéo của $D$ bao gồm của các giá trị kỳ dị (singular values) $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{d}$ của $X$ - $\mu$ arranged trong descending thứ tự. Thì
$$a^{\top}(X -\mu )^{\top}(X -\mu )a = a^{\top}UD^{2}U^{\top} a,$$
Ở đâu $D^{2} = diag(\sigma_{1}^{2} , \dots  , \sigma_{d}^{2}$) là ma trận đường chéo (diagonal matrix), do đó chọn là cột cuối cùng trong $U$ (tương ứng với nhỏ nhất trị riêng (eigenvalue) $\sigma_{d}^{2}$ của $(X$ - $\mu )^{\top}(X$ - $\mu$)). Điều này là nghiệm đến của ta tốt nhất fit bài toán. Vì vậy, nếu $U_{d-1}$ là tuyến tính siêu phẳng (hyperplane) được định nghĩa bởi, nghĩa là,
$$\mathbb{R}^{d}$$
$$U_{d-1} = {u \in | \langle u, a\rangle = 0},$$
Ở đâu là cột cuối cùng trong $U$ với một số SVD $V DU^{\top}$ của $X$ - $\mu$, ta có được hiển thị rằng afin siêu phẳng (hyperplane) $A_{1} = \mu  + U_{d-1}$ là tốt nhất xấp xỉ của dữ liệu tập hợp $X_{1}, \dots  , X_{n}$ trong bình phương tối thiểu (least squares) nghĩa. Nó là dễ để chỉ ra rằng điều này siêu phẳng (hyperplane) $A_{1} = \mu  + U_{d-1}$ cực tiểu hóa tổng của square các khoảng cách của mỗi $X_{i}$ đến của nó phép chiếu trực giao (orthogonal projection) lên $A_{1}$. Cũng, vì $U_{d-1}$ là phần bù trực giao (orthogonal complement) của, cột cuối cùng của $U$, ta xem rằng $U_{d-1}$ được sinh (spanned) bởi thứ nhất d-1 các cột của $U$, nghĩa là, thứ nhất $d$ - $1$ chính các hướng của $X$ - $\mu$. Tất cả điều này có thể được suy rộng/tổng quát hóa đến tốt nhất (d-k)-dimensional không gian con afin (affine subspace) $A_{k}$ approximating $X_{1}, \dots  , X_{n}$ trong bình phương tối thiểu (least squares) nghĩa $(1 \le k \le d -1)$. Như vậy không gian con afin (affine subspace) $A_{k}$ là cut ra bởi $k$ độc lập các siêu phẳng $H_{i}$ (với $1 \le i \le k)$, mỗi cho trước bởi một số phương trình
$$a_{i1}x_{1} + \cdots  + a_{i d}x_{d} + c_{i} = 0.$$
Nếu ta viết $a_{i} = (a_{i1}, \cdots  , a_{i d})$, đến nói rằng $H_{i}$ là độc lập có nghĩa là $a_{1}, \dots  , a_{k}$ là độc lập tuyến tính (linearly independent). Thực ra, ta có thể giả sử rằng $a_{1}, \dots  , a_{k}$ tạo thành trực chuẩn hệ. Thì việc tìm tốt nhất $(d$ - k)-dimensional không gian con afin (affine subspace) $A_{k}$ tương đương với đến việc giải thuần nhất hệ phương trình tuyến tính
$$\begin{pmatrix} X & 1 & 0 & \cdots & 0 & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ 0 & 0 & 0 & \cdots & 0 & X & 1 \end{pmatrix} \begin{pmatrix} a_{1} \\ c_{1} \\ \vdots \\ a_{k} \\ c_{k} \end{pmatrix} = \begin{pmatrix} 0 \\ \vdots \\ 0 \end{pmatrix} ,$$

<!-- PAGE 796 -->
Trong bình phương tối thiểu (least squares) nghĩa, subject đến các điều kiện $a_{i}^{\top} a_{j} = \delta_{i j}$, với mọi $i, j$ với $1 \le i, j \le k$, ở đâu ma trận của hệ là khối ma trận đường chéo (diagonal matrix) bao gồm của $k$ đường chéo các khối $(X, 1)$, ở đâu $1$ ký hiệu vectơ cột (column vector) $(1, \dots  , 1) \in \mathbb{R}^{n}$. Một lần nữa nó là dễ để xem rằng mỗi siêu phẳng (hyperplane) $H_{i}$ phải đi qua qua trọng tâm $\mu$ của $X_{1}, \dots  , X_{n}$, và bởi switching đến được tâm dữ liệu $X_{i}$ - $\mu$ ta thu được hệ
$$\begin{pmatrix} X-\mu & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & X-\mu \end{pmatrix} \begin{pmatrix} a_{1} \\ \vdots \\ a_{k} \end{pmatrix} = \begin{pmatrix} 0 \\ \vdots \\ 0 \end{pmatrix} ,$$
Với $a_{i}^{\top} a_{j} = \delta_{i j}$ với mọi $i, j$ với $1 \le i, j \le k$. Nếu $V DU^{\top} = X -\mu$ là SVD phân rã, nó là dễ để xem rằng bình phương tối thiểu (least squares) nghiệm của hệ này được cho bởi cuối cùng $k$ các cột của $U$, giả sử rằng chính đường chéo của $D$ bao gồm của các giá trị kỳ dị (singular values) $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{d}$ của $X -\mu$ arranged trong descending thứ tự. Nhưng bây giờ $(d$ -k)-dimensional không gian con $U_{d-k}$ cut ra bởi các siêu phẳng được định nghĩa bởi $a_{1}, \dots  , a_{k}$ là đơn giản phần bù trực giao (orthogonal complement) của $(a_{1}, \dots  , a_{k})$, mà là không gian con được sinh (spanned) bởi thứ nhất $d$ - $k$ các cột của $U$. Do đó tốt nhất (d-k)-dimensional afin subpsace $A_{k}$ approximating $X_{1}, \dots  , X_{n}$ trong bình phương tối thiểu (least squares) nghĩa là
$$A_{k} = \mu  + U_{d-k},$$
Ở đâu $U_{d-k}$ là không gian con tuyến tính được sinh (spanned) bởi thứ nhất d-k chính các hướng của $X-\mu$, nghĩa là, thứ nhất d-k các cột của $U$. Hệ quả là, ta thu được sau đây thú vị interpretation của PCA (thực sự, chính các hướng):

> **Định lý 23.12.** Cho $X$ là một ma trận cỡ $n \times  d$ của dữ liệu các điểm $X_{1}, \dots  , X_{n}$, và cho $\mu$ là trọng tâm của $X_{i}’s$. Nếu $X$ - $\mu  = V DU^{\top}$ là SVD phân rã của $X$ - $\mu$ và nếu chính đường chéo của $D$ bao gồm của các giá trị kỳ dị (singular values) $\sigma_{1}  \ge \sigma_{2}  \ge \cdots  \ge \sigma_{d}$, thì tốt nhất $(d$ - k)- dimensional afin xấp xỉ $A_{k}$ của $X_{1}, \dots  , X_{n}$ trong bình phương tối thiểu (least squares) nghĩa được cho bởi
$$A_{k} = \mu  + U_{d-k},$$
Ở đâu $U_{d-k}$ là không gian con tuyến tính được sinh (spanned) bởi thứ nhất $d$ - $k$ các cột của $U$, thứ nhất $d$ - $k$ chính các hướng của $X$ - $\mu  (1 \le k \le d$ - $1)$.

> **Ví dụ 23.11.** Đi quay lại đến Ví dụ 23.10, tốt nhất 1-dimensional afin xấp xỉ $A_{1}$ là afin đường thẳng chuyển qua $(\mu_{1} , \mu_{2}$) $=$ (1824.4, 5.6) của hướng $u_{1} =$ (0.9995, 0.0325).

> **Ví dụ 23.12.** Giả sử trong dữ liệu tập hợp của Ví dụ 23.5 rằng ta cộng month của birth của mọi mathematician như đặc trưng (feature). Ta thu được kết quả sau dữ liệu tập hợp.

<!-- PAGE 797 -->
$$Namemonthyearlength$$
$$Carl Friedrich Gauss417770$$
$$Camille Jordan1183812$$
$$Adrien-Marie Legendre917520$$
$$Bernhard Riemann9182615$$
$$David Hilbert118622$$
$$Henri Poincar´e418545$$
$$Emmy Noether318820$$
$$Karl Weierstrass1018150$$
$$Eugenio Beltrami1018352$$
$$Hermann Schwarz1184320$$
Có nghĩa của cột thứ nhất là 5.2, và được tâm dữ liệu tập hợp là cho trước ở dưới.
$$Namemonthyearlength$$
$$Carl Friedrich Gauss-1.2-51.4-5.6$$
$$Camille Jordan-4.29.66.4$$
$$Adrien-Marie Legendre3.8-76.4-5.6$$
$$Bernhard Riemann3.8-2.49.4$$
$$David Hilbert-4.233.6-3.6$$
$$Henri Poincar´e-1.225.6-0.6$$
$$Emmy Noether-2.253.6-5.6$$
$$Karl Weierstrass4.813.4-5.6$$
$$Eugenio Beltrami4.86.6-3.6$$
$$Hermann Schwarz-4.214.614.4$$
Chạy SVD trên điều này dữ liệu tập hợp ta thu được
$$U = \begin{pmatrix} 0.0394 & 0.1717 & 0.9844 \\ -0.9987 & 0.0390 & 0.0332 \\ 0.0327 & 0.9844 & 0.1730 \end{pmatrix} ,D = \begin{pmatrix} 117.0706 & 0 & 0 \\ 0 & 22.0390 & 0 \\ 0 & 0 & 10.1571 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} ,$$
$$--$$
