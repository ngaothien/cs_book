# Các ứng dụng của ADMM đến 1-Chuẩn (norm) Các bài tập


<!-- PAGE 1934 -->
Do đó ta thu được
$$b = w^{\top}(u_{i0} + v_{j0})/2.$$
Cho được cải thiện số tính ổn định, ta có thể trung bình trên các tập hợp của các chỉ số được định nghĩa như $I_{\lambda >0} = {i \in {1, \dots  , p}$ | $\lambda_{i}  > 0}$ và $I_{\mu >0} = {j \in {1, \dots  , q}$ | $\mu_{j}  > 0}$. Ta thu được
$$b = w^{\top} \begin{pmatrix}  \\ u_{i} \end{pmatrix} \begin{pmatrix}  \\ /|I_{\lambda >0}| + & v_{j} \end{pmatrix} \sum_{i\in I\lambda >0}  \begin{pmatrix} /|I_{\mu >0}| \end{pmatrix} \sum_{j\in I\mu >0}  /2.$$
Matlab các bài toán quy hoạch cài đặt ở trên phương pháp là cho trước trong Phụ lục $B$, Mục B.1. Điều này nên convince độc giả rằng ở đó là rất little khoảng cách giữa lý thuyết và practice, mặc dù nó là khá consuming đến tune tolerance các tham số cần thiết đến deal với floatingpoint arithmetric. Hình 52.5 chỉ ra kết quả của chạy Matlab bài toán quy hoạch cài đặt ở trên phương pháp bằng cách sử dụng ADMM trên hai các tập hợp của các điểm của $50$ các điểm mỗi được sinh tại ngẫu nhiên bằng cách sử dụng sau đây Matlab code. u14 $= 10.1*randn(2,50)+18$; v14 $=$ -10.1*randn(2,50)-18; hàm SVMhard2 được gọi là với $\rho  = 10$ như sau [lamb,mu,w] $=$ SVMhard2(10,u14,v14) và produces output được hiển thị trong Hình 52.5. Nhận thấy rằng ở đó là một xanh lam hỗ trợ/giá (support) vectơ và hai đỏ hỗ trợ/giá (support) các vectơ.

## 52.8 Các ứng dụng của ADMM đến \ell 1-Chuẩn (norm) Các bài tập

Một cái khác quan trọng ứng dụng của ADMM là đến $\ell^{1}$ -chuẩn (norm) cực tiểu hóa các bài tập, especially lasso cực tiểu hóa, được thảo luận ở dưới và trong Mục 55.4. Điều này liên quan đến đặc biệt trường hợp của ADMM ở đâu f(x) $= \tau  \|x\|_{1}$ và $A =$ I. Đặc biệt, trong một chiều trường hợp, ta cần để giải cực tiểu hóa bài toán: tìm
$$x^{*}= arg minx \begin{pmatrix} \tau |x| + (\rho /2)(x -v)^{2} \end{pmatrix} ,$$
Với $x, v \in \mathbb{R}$, và $\rho , \tau  > 0$. Cho $c = \tau /\rho$ và viết
$$f(x) = \frac{\tau}{2c} \begin{pmatrix} 2c|x| + (x -v)^{2} \end{pmatrix} .$$
Cực tiểu hóa $f$ trên $x$ là tương đương đến cực tiểu hóa
$$g(x) = 2c|x| + (x -v)^{2}= 2c|x| + x^{2}-2xv + v^{2},$$

<!-- PAGE 1935 -->
$$Figure 52.5: An example of hard margin SVM.$$
Mà là tương đương đến cực tiểu hóa
$$h(x) = x^{2}+ 2(c|x| -xv)$$
Trên $x$. Nếu $x \ge 0$, thì
$$h(x) = x^{2}+ 2(cx -xv) = x^{2}+ 2(c -v)x = (x -(v -c))^{2}-(v -c)^{2}.$$
Nếu $v$ - $c > 0$, nghĩa là, $v > c$, vì $x \ge 0$, hàm $x \mapsto (x$ - $(v$ - $c))^{2}$ có cực tiểu cho $x = v$ - $c > 0$, khác nếu $v$ - $c \le 0$, thì hàm $x \mapsto (x$ - $(v$ - $c))^{2}$ có cực tiểu cho $x = 0$. Nếu $x \le 0$, thì
$$h(x) = x^{2}+ 2(-cx -xv) = x^{2}-2(c + v)x = (x -(v + c))^{2}-(v + c)^{2}.$$
Nếu $v + c < 0$, nghĩa là, $v < -c$, vì $x \le 0$, hàm $x \mapsto (x$ -(v $+ c))^{2}$ có cực tiểu cho $x = v + c$, khác nếu $v + c \ge 0$, thì hàm $x \mapsto (x$ - $(v + c))^{2}$ có cực tiểu cho $x = 0$. Trong tóm tắt, $inf_{x}$ h(x) là hàm của $v$ cho trước bởi
$$v -cif v > c$$
$$$$
$$$$
$$S_{c}(v) =0if |v| \le c$$
$$v + cif v < -c.$$
$$$$
Hàm $S_{c}$ là đã biết như soft thresholding toán tử. đồ thị của $S_{c}$ được hiển thị trong Hình 52.6.

<!-- PAGE 1936 -->
$$Figure 52.6: The graph of S_{c} (when c = 2).$$
Một có thể kiểm tra rằng
$$S_{c}(v) = (v -c)_{+} -(-v -c)_{+},$$
Và cũng
$$S_{c}(v) = (1 -c/|v|)_{+}v,v \neq  0,$$
Mà chỉ ra rằng $S_{c}$ là shrinkage toán tử (nó di chuyển điểm toward không).
$$\mathbb{R}^{n}$$
Toán tử $S_{c}$ được mở rộng đến các vectơ trong thành phần wise, nghĩa là, nếu $x = (x_{1}, \dots  , x_{n})$, thì
$$S_{c}(x) = (S_{c}(x_{1}), \dots  , S_{c}(x_{n})).$$
Ta bây giờ xét một vài $\ell^{1}$ -chuẩn (norm) các bài tập.
$(1)$ Least tuyệt đối deviation. Điều này là bài toán của cực tiểu hóa $\|Ax$ - $b\|_{1}$, thay vì $\|Ax$ - $b\|_{2}$. Least tuyệt đối deviation là nhiều hơn/thêm robust hơn bình phương tối thiểu (least squares) fit bởi vì nó deals tốt hơn với outliers. bài toán có thể được formulated trong ADMM tạo thành như sau:
$$minimize\|z\|_{1}$$
$$subject to Ax -z = b,$$
Với $f = 0$ và $g = \|\|_{1}$. Như thông thường, ta giả sử rằng $A$ là một ma trận cỡ $m \times  n$ của hạng (rank) $n$, sao cho $A^{\top}A$ là khả nghịch. ADMM (trong scaled tạo thành) có thể được biểu diễn dưới dạng
$$x^{k+1}= (A^{\top}A)^{-1}A^{\top}(b + z^{k}-u^{k})$$
$$z^{k+1}= S_{1/\rho}(Ax^{k+1}-b + u^{k})$$
$$u^{k+1}= u^{k}+ Ax^{k+1}-z^{k+1}-b.$$

<!-- PAGE 1937 -->
$(2)$ Cơ sở (basis) pursuit. Điều này là sau đây cực tiểu hóa bài toán:
$$minimize\|x\|_{1}$$
$$subject to Ax = b,$$
Ở đâu $A$ là một ma trận cỡ $m \times  n$ của hạng (rank) $m < n$, và $b \in \mathbb{R}^{m}, x \in \mathbb{R}^{n}$. bài toán là để tìm thưa (sparse) nghiệm đến underdetermined hệ phương trình tuyến tính, mà có nghĩa là nghiệm $x$ với nhiều không các tọa độ. bài toán này đóng trung tâm vai trò trong compressed sensing và statistical tín hiệu processing. Cơ sở (basis) pursuit có thể được được biểu diễn trong ADMM tạo thành như bài toán
$$minimizeI_{C}(x) + \|z\|_{1}$$
$$subject to x -z = 0,$$
$$\mathbb{R}^{n}$$
Với $C = {x \in$ | Ax $= b}$. Nó là dễ để xem rằng ADMM quy trình (trong scaled tạo thành) là
$$x^{k+1}= \Pi_{C} (z^{k}-u^{k})$$
$$z^{k+1}= S_{1/\rho}(x^{k+1}+ u^{k})$$
$$u^{k+1}= u^{k}+ x^{k+1}-z^{k+1},$$
Ở đâu $\Pi_{C}$ là phép chiếu trực giao (orthogonal projection) lên không gian con $C$. Thực ra, nó là không khó để chỉ ra rằng
$$x^{k+1}= (I -A^{\top}(AA^{\top})^{-1}A)(z^{k}-u^{k}) + A^{\top}(AA^{\top})^{-1}b.$$
Trong một số nghĩa, $\ell^{1}$ -cực tiểu hóa bài toán là rút gọn đến dãy của $\ell^{2}$ -chuẩn (norm) các bài tập. Có các cách của improving efficiency của phương pháp; xem Boyd et al. $[28]$ (Mục 6.2)
$(3)$ Tổng quát $\ell^{1}$ -regularized mất mát (loss) cực tiểu hóa. Điều này là sau đây cực tiểu hóa bài toán:
$$minimizel(x) + \tau  \|x\|_{1} ,$$
Ở đâu $l$ là bất kỳ thực sự/đúng đắn đóng và lồi mất mát (loss) hàm, và $\tau  > 0$. Ta chuyển đổi bài toán đến ADMM bài toán:
$$minimizel(x) + \tau  \|z\|_{1}$$
$$subject to x -z = 0.$$

<!-- PAGE 1938 -->
ADMM quy trình (trong scaled tạo thành) là
$$x^{k+1}= arg minx \begin{pmatrix} l(x) + (\rho /2) & x -z^{k} + u_{2}^{k2} \end{pmatrix}$$
$$z^{k+1}= S_{\tau /\rho}(x^{k+1}+ u^{k})$$
$$u^{k+1}= u^{k}+ x^{k+1}-z^{k+1}.$$
X-update là proximal toán tử việc tính giá trị. Nói chung, một cần để áp dụng số quy trình để tính $x^{k+1}$, ví dụ, phiên bản của Newton’s phương pháp. đặc biệt trường hợp ở đâu l(x) $= (1/2) \|Ax$ - $b\|_{2}^{2}$ là một cách cụ thể quan trọng.
$(4)$ Lasso chỉnh quy hóa (regularization). Điều này là sau đây cực tiểu hóa bài toán:
$$minimize(1/2) \|Ax -b\|_{2}^{2} + \tau  \|x\|_{1} .$$
Điều này là tuyến tính hồi quy với regularizing số hạng $\tau  \|x\|_{1}$ thay vì của $\tau  \|x\|_{2}$, đến encourage thưa (sparse) nghiệm. phương pháp này đã là thứ nhất proposed bởi Tibshirani xung quanh $1996$, dưới name lasso, mà stands cho “least tuyệt đối selection và shrinkage toán tử.” phương pháp này là cũng đã biết như $\ell^{1}$ -regularized hồi quy, nhưng điều này là không như cute như “lasso,” mà được sử dụng predominantly. phương pháp này được thảo luận extensively trong Hastie, Tibshirani, và Wainwright $[92]$. lasso cực tiểu hóa được chuyển đổi đến sau đây bài toán trong ADMM tạo thành:
$$minimize \frac{1}{2} \|Ax -b\|_{2}^{2} + \tau  \|z\|_{1}$$
$$subject to x -z = 0.$$
Thì ADMM quy trình (trong scaled tạo thành) là
$$x^{k+1}= (A^{\top}A + \rho I)^{-1}(A^{\top}b + \rho (z^{k}-u^{k}))$$
$$z^{k+1}= S_{\tau /\rho}(x^{k+1}+ u^{k})$$
$$u^{k+1}= u^{k}+ x^{k+1}-z^{k+1}.$$
Vì $\rho  > 0$, ma trận $A^{\top}A+\rho$ I là đối xứng xác định dương (SPD). Lưu ý rằng x-update trông like hồi quy Ridge (ridge regression) bước (xem Mục 55.1). Có khác nhau các tổng quát hóa của lasso.
$(5)$ Suy rộng/tổng quát hóa Lasso chỉnh quy hóa (regularization). Điều này là sau đây cực tiểu hóa bài toán:
$$minimize(1/2) \|Ax -b\|_{2}^{2} + \tau  \|Fx\|_{1} ,$$
