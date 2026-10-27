# Jordan Phân rã


<!-- PAGE 1119 -->

> **Định nghĩa 31.5.** Nếu $\lambda  \in K$ là trị riêng (eigenvalue) của $f$, ta định nghĩa suy rộng/tổng quát hóa vectơ riêng (eigenvector) của $f$ như khác không vectơ $u \in E$ sao cho
$$(\lambda id -f)^{r}(u) = 0,for some r \ge 1.$$
Chỉ số của $\lambda$ được định nghĩa như nhỏ nhất $r \ge 1$ sao cho
$$\mathrm{Ker} (\lambda id -f)^{r}= \mathrm{Ker} (\lambda id -f)^{r+1}.$$
Rõ ràng là Ker $(\lambda$ id - $f)^{i} \subseteq$ Ker $(\lambda$ id - $f)^{i+1}$ với mọi $i \ge 1$. Theo Định lý 31.11(d), nếu $\lambda  = \lambda_{i}$, chỉ số của $\lambda_{i}$ bằng $r_{i}$.

## 31.5 Jordan Phân rã

Nhắc lại rằng ánh xạ tuyến tính (linear map) $g: E \to E$ được nói là lũy linh (nilpotent) nếu tồn tại một dương số nguyên $r$ sao cho $g^{r} = 0$. Một cái khác quan trọng hệ quả của Định lý 31.11 là rằng $f$ có thể được viết dưới dạng tổng của chéo hóa được (diagonalizable) và lũy linh (nilpotent) ánh xạ tuyến tính (linear map) (mà giao hoán). Ví dụ $\mathbb{R}^{2} \mathbb{R}^{2}  \mathbb{R} f$: là -ánh xạ tuyến tính (linear map) f(x, $y) = (x, x + y)$ với tiêu chuẩn ma trận biểu diễn
$$X_{f} = \begin{pmatrix} \to \\ 1 & 1 \\ 0 & 1 \\ that \end{pmatrix} . A basic calculation shows that m_{f}(x) = \chi_{f} (x) = (x -1)^{2}. By Theorem 31.6$$
Ta biết $f$ là không chéo hóa được (diagonalizable) trên $\mathbb{R}$. Nhưng vì trị riêng (eigenvalue) $\lambda_{1}  = 1$ của $f$ thực hiện thuộc $to\mathbb{R}$, ta có thể sử dụng phép chiếu cách xây dựng inherent trong phạm vi Định lý 31.11 đến viết $f = D + N$, ở đâu $D$ là chéo hóa được (diagonalizable) ánh xạ tuyến tính (linear map) và $N$ là lũy linh (nilpotent) ánh xạ tuyến tính (linear map). chứng minh của Định lý 31.10 suy ra rằng
$$p_{1}^{r1} = (x -1)^{2},g_{1} = 1 = h_{1},\pi_{1}  = g_{1}(f)h_{1}(f) = id.$$
Thì $D = \lambda_{1} \pi_{1}  =$ id, $N = f$ - $D =$ f(x, $y)$ - id(x, $y) = (x, x + y)$ - $(x, y) = (0, y)$, mà là tương đương đến ma trận phân rã
$$X_{f} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} .$$
Ví dụ này suggests rằng đường chéo summand của $f$ là related đến phép chiếu các cách xây dựng liên kết với chứng minh của phân rã sơ cấp (primary decomposition) định lý. Nếu ta viết
$$D = \lambda_{1} \pi_{1}  + \cdots  + \lambda_{k} \pi_{k} ,$$
Ở đâu $\pi_{i}$ là phép chiếu từ $E$ lên không gian con $W_{i}$ được định nghĩa trong chứng minh của Định lý 31.10, vì
$$\pi_{1}  + \cdots  + \pi_{k}  = id,$$

<!-- PAGE 1120 -->
Ta có
$$f = f\pi_{1}  + \cdots  + f\pi_{k} ,$$
Và do đó ta thu được
$$N = f -D = (f -\lambda_{1} id)\pi_{1}  + \cdots  + (f -\lambda_{k} id)\pi_{k} .$$
Ta khẳng định rằng $N = f$ - $D$ là lũy linh (nilpotent) toán tử. Vì bởi cách xây dựng $\pi_{i}$ là các đa thức trong $f$, chúng giao hoán với $f$, bằng cách sử dụng các tính chất của $\pi_{i}$, ta thu được
$$N^{r}= (f -\lambda_{1} id)^{r}\pi_{1}  + \cdots  + (f -\lambda_{k} id)^{r}\pi_{k} .$$
Vì vậy, nếu $r = max{r_{i}}$, ta có $(f$ - $\lambda_{k} id)^{r} = 0$ cho $i = 1, \dots  , k$, mà suy ra rằng
$$N^{r}= 0.$$
Nó vẫn còn để chỉ ra rằng $D$ là chéo hóa được (diagonalizable). Vì $N$ là đa thức trong $f$, nó giao hoán với $f$, và do đó với $D$. Từ
$$D = \lambda_{1} \pi_{1}  + \cdots  + \lambda_{k} \pi_{k} ,$$
Và
$$\pi_{1}  + \cdots  + \pi_{k}  = id,$$
Ta xem rằng $D$ - $\lambda_{i}$ id $= \lambda_{1} \pi_{1}  + \cdots  + \lambda_{k} \pi_{k}$ - $\lambda_{i} (\pi_{1}  + \cdots  + \pi_{k}$)
$$= (\lambda_{1}  -\lambda_{i} )\pi_{1}  + \cdots  + (\lambda_{i-1}  -\lambda_{i} )\pi_{i-1}  + (\lambda_{i+1}  -\lambda_{i} )\pi_{i+1}  + \cdots  + (\lambda_{k}  -\lambda_{i} )\pi_{k} .$$
Vì các phép chiếu $\pi_{j}$ với $j \neq  i$ triệt tiêu trên $W_{i}$, ở trên phương trình suy ra rằng $D$ - $\lambda_{i}$ id triệt tiêu trên $W_{i}$ và rằng $(D$ - $\lambda_{j} id)(W_{i}) \subseteq W_{i}$, và do đó rằng đa thức tối tiểu (minimal polynomial) của $D$ là
$$(X -\lambda_{1} ) \cdots  (X -\lambda_{k} ).$$
Vì $\lambda_{i}$ là phân biệt, theo Định lý 31.6, ánh xạ tuyến tính (linear map) $D$ là chéo hóa được (diagonalizable). Trong tóm tắt ta có được hiển thị rằng khi tất cả các trị riêng (eigenvalues) của $f$ thuộc đến $K$, ở đó tồn tại chéo hóa được (diagonalizable) ánh xạ tuyến tính (linear map) $D$ và lũy linh (nilpotent) ánh xạ tuyến tính (linear map) $N$ sao cho
$$f = D + N$$
$$DN = ND,$$
Và $N$ và $D$ là các đa thức trong $f$.

> **Định nghĩa 31.6.** phân rã của $f$ như $f = D + N$ như ở trên được gọi là một Jordan phân rã. Thực ra, ta có thể chứng minh nhiều hơn/thêm: các ánh xạ $D$ và $N$ là một cách duy nhất được xác định bởi $f$.

<!-- PAGE 1121 -->

> **Định lý 31.12.** (Jordan Phân rã) Cho $f$: $E \to E$ là ánh xạ tuyến tính (linear map) trên không gian vectơ hữu hạn chiều $E$ trên trường $K$. Nếu tất cả các trị riêng (eigenvalues) $\lambda_{1} , \dots  , \lambda_{k}$ của $f$ thuộc đến $K$, thì ở đó tồn tại chéo hóa được (diagonalizable) ánh xạ tuyến tính (linear map) $D$ và lũy linh (nilpotent) ánh xạ tuyến tính (linear map) $N$ sao cho
$$f = D + N$$
$$DN = ND.$$
Hơn nữa, $D$ và $N$ là một cách duy nhất được xác định bởi ở trên các phương trình và chúng là các đa thức trong $f$.

*Chứng minh.* Ta đã được chứng minh sự tồn tại phần. Giả sử ta cũng có $f =$ D' $+$ N', với D'N' $=$ N'D', ở đâu D' là chéo hóa được (diagonalizable), N' là lũy linh (nilpotent), và cả hai là các đa thức trong $f$. Ta cần để chứng minh rằng $D =$ D' và $N =$ N'. Vì D' và N' giao hoán với một một cái khác và $f =$ D' $+$ N', ta xem rằng D' và N' giao hoán với $f$. Thì D' và N' giao hoán với bất kỳ đa thức trong $f$; do đó chúng giao hoán với $D$ và $N$. Từ
$$D + N = D'+ N',$$
Ta thu được
$$D -D'= N'-N,$$
Và $D$, D', $N$, N' giao hoán với một một cái khác. Vì $D$ và D' là cả hai chéo hóa được (diagonalizable) và giao hoán, theo Mệnh đề 31.7, chúng là simultaneousy chéo hóa được (diagonalizable), do đó $D$ - D' là chéo hóa được (diagonalizable). Vì $N$ và N' giao hoán, bởi nhị thức công thức, với mọi $r \ge 1$,
$$(N'-N)^{r}= \sum_{j=0}^{r}  (-1)^{j} \begin{pmatrix} r \\ j \end{pmatrix} (N')^{r-j}N^{j}.$$
Vì cả hai $N$ và N' là lũy linh (nilpotent), ta có $N^{r1} = 0$ và $(N')^{r2} = 0$, với một số $r_{1}, r_{2} > 0$, do đó cho $r \ge r_{1} + r_{2}$, vế phải của ở trên biểu thức là không, mà chỉ ra rằng N' $-N$ là lũy linh (nilpotent). (Thực ra, nó là dễ rằng $r_{1} = r_{2} = n$ hoạt động). Suy ra rằng $D$ - D' $=$ N' - $N$ là cả hai chéo hóa được (diagonalizable) và lũy linh (nilpotent). Rõ ràng, đa thức tối tiểu (minimal polynomial) của lũy linh (nilpotent) ánh xạ tuyến tính (linear map) là của tạo thành $X^{r}$ với một số $r > 0$ (và $r \le$ dim(E)). Nhưng $D$ - D' là chéo hóa được (diagonalizable), do đó của nó đa thức tối tiểu (minimal polynomial) có đơn giản các nghiệm, mà có nghĩa là $r = 1$. Vì vậy, đa thức tối tiểu (minimal polynomial) của $D$ - D' là $X$, mà nói rằng rằng $D$ - D' $= 0$, và thì $N =$ N'. Nếu $K$ là algebraically đóng trường, thì Định lý 31.12 nghiệm đúng. Điều này là trường hợp khi $K = \mathbb{C}$. định lý này rút gọn study của các ánh xạ tuyến tính (linear maps) (từ $E$ đến chính nó) đến study của lũy linh (nilpotent) các toán tử. Có một đặc biệt chuẩn tắc/bình thường tạo thành cho như vậy các toán tử mà được thảo luận trong mục tiếp theo.
