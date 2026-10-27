# Hạt nhân (kernel) Hồi quy Ridge (ridge regression)


<!-- PAGE 2084 -->

![Figure 55.6](../../assets/ch55/fig_55_6.png)

**Hình 55.6:** đồ thị của mặt phẳng f(x, $y) = 1.1706x+1.1401y$ -1.2298 như xấp xỉ fit đến dữ liệu $(X, y_{1})$ của Ví dụ 55.1. Xem Hình 55.6. Ta có thể xem cách mà lựa chọn của $K$ affects quality của nghiệm $(w, b)$ bởi việc tính toán chuẩn (norm) $\|\xi \|_{2}$ của sai số vectơ $\xi  = y$ - Xw - $b1_{m}$. Như trong Ví dụ 55.1 ta chú ý rằng nhỏ hơn $K$ là, nhỏ hơn là chuẩn (chuẩn (norm)) này. Ta cũng nhận thấy rằng cho cho trước giá trị của $K$, Bài toán quy hoạch (RR6') cho slightly nhỏ hơn giá trị của $\|\xi \|_{2}$ hơn (RR3b) thực hiện. Như được điểm ra bởi Hastie, Tibshirani, và Friedman $[91]$ (Mục 3.4), defect của cách tiếp cận ở đâu $b$ là cũng có phạt là rằng nghiệm cho $b$ là không bất biến dưới cộng hằng số $c$ đến mỗi giá trị $y_{i}$. Điều này là không trường hợp cho cách tiếp cận bằng cách sử dụng Bài toán quy hoạch (RR6').

## 55.3 Hạt nhân (kernel) Hồi quy Ridge (ridge regression)

Một thú vị aspect của đối ngẫu (dual) (của hoặc (RR2) hoặc (RR3)) là rằng nó chỉ ra rằng nghiệm $w$ đang là của tạo thành $X^{\top}\alpha$, là tổ hợp tuyến tính (linear combination)
$$w = \sum_{i=1}^{m}  \alpha_{i} x_{i}$$
Của dữ liệu các điểm $x_{i}$, với các hệ số $\alpha_{i}$ tương ứng với đối ngẫu (dual) biến $\lambda  = 2K\alpha$ của đối ngẫu (dual) hàm, và với
$$\alpha  = (XX^{\top}+ KI_{m})^{-1}y.$$
Nếu $m$ là nhỏ hơn hơn $n$, thì nó là nhiều hơn/thêm advantageous để giải cho $\alpha$. Nhưng những gì một cách thực làm cho đối ngẫu (dual) thú vị là rằng với định nghĩa của chúng ta của $X$ như
$$X = \begin{pmatrix} x_{1}^{\top} \\ \vdots \\ x_{m}^{\top} \end{pmatrix} ,$$

<!-- PAGE 2085 -->
Ma trận $XX^{\top}$ bao gồm của trong các tích $x_{i}^{\top} x_{j}$, và tương tự hàm learned f(x) $= x^{\top}w$ có thể được biểu diễn dưới dạng
$$f(x) = \sum_{i=1}^{m}  \alpha_{i} x_{i}^{\top} x,$$
Cụ thể là rằng cả hai $w$ và f(x) là cho trước theo trong các tích $x_{i}^{\top} x_{j}$ và $x_{i}^{\top} x$. sự kiện này là then chốt đến tổng quát hóa đến hồi quy Ridge (ridge regression) trong mà input không gian $\mathbb{R}^{n}$ được nhúng trong lớn hơn (có thể vô hạn dimensional) Không gian Euclid (Euclidean space) $F$ (với tích vô hướng (inner product) $\langle$ -, $-\rangle$) thường được gọi là đặc trưng (feature) không gian, bằng cách sử dụng hàm
$$\mathbb{R}^{n}$$
$$\phi :\to F.$$
Bài toán trở thành (hạt nhân (kernel) hồi quy Ridge (ridge regression)) Bài toán quy hoạch (KRR2):
$$minimize\xi^{\top} \xi  + K\langle w, w\rangle$$
$$subject to$$
$$y_{i} -\langle w, \phi (x_{i})\rangle = \xi_{i} ,i = 1, \dots  , m,$$
Cực tiểu hóa trên $\xi$ và $w$. Lưu ý rằng $w \in F$. bài toán này được thảo luận trong Shawe–Taylor và Christianini $[165]$ (Mục 7.3). Ta sẽ chỉ ra ở dưới rằng nghiệm là chính xác cùng:
$$\alpha  = (G + KI_{m})^{-1}y$$
$$w = \sum_{i=1}^{m}  \alpha_{i} \phi (x_{i})$$
$$\xi  = K\alpha ,$$
Ở đâu $G$ là Gram ma trận cho trước bởi $G_{ij} = \langle \phi (x_{i}), \phi (x_{j})\rangle$. ma trận này cũng được gọi là hạt nhân (kernel) ma trận và là thường được ký hiệu bởi $K$ thay vì của $G$. Trong điều này khung lý thuyết ta có là little careful trong bằng cách sử dụng các gradien vì tích vô hướng (inner product) $\langle$ -, $-\rangle$ trên $F$ là liên quan và $F$ có thể là vô hạn dimensional, nhưng điều này gây ra không có bài toán bởi vì ta có thể sử dụng các đạo hàm, và theo Mệnh đề 39.5 ta có
$$d\langle -, -\rangle_{(u,v)} (x, y) = \langle x, v\rangle + \langle u, y\rangle .$$
Điều này suy ra rằng đạo hàm của ánh xạ $u \mapsto \langle u, u\rangle$ là
$$d\langle -, -\rangle_{u} (x) = 2\langle x, u\rangle .(d_{1})$$

<!-- PAGE 2086 -->
Vì ánh xạ $u \mapsto \langle u, v\rangle$ (với $v$ cố định) là tuyến tính, đạo hàm của nó là
$$d\langle -, v\rangle_{u} (x) = \langle x, v\rangle .(d_{2})$$
Đạo hàm của Hàm Lagrange (Lagrangian)
$$L(\xi , w, \lambda ) = \xi^{\top} \xi  + K\langle w, w\rangle - \sum_{i=1}^{m}  \lambda_{i} \langle \phi (x_{i}), w\rangle -\xi^{\top} \lambda  + \lambda^{\top} y$$
Đối với $\xi$ và $w$ là
$$dL_{\xi ,w} \begin{pmatrix} \xi ,ew \\ e \end{pmatrix} = 2(\xi e)^{\top}\xi  -(\xi e)^{\top}\lambda  +2Kw - \sum_{i=1}^{m}  \lambda_{i} \phi (x_{i}), we,$$
Ở đâu ta được sử dụng $(d$) để tính toán đạo hàm của $\xi^{\top} \xi  + K\langle w, w\rangle$ và $(d_{2})$ để tính toán
$$derivative of - \sum_{i}^{1}  m=1 \lambda_{i} \langle \phi (x_{i}), w\rangle -\xi^{\top} \lambda . We have dL_{\xi ,w} = 0 for all \xi e and we iff$$
$$\begin{pmatrix} \xi ,ew \\ e \end{pmatrix}$$
$$2Kw = \sum_{i=1}^{m}  \lambda_{i} \phi (x_{i})$$
$$\lambda  = 2\xi .$$
Một lần nữa ta định nghĩa $\xi  = K\alpha$, do đó ta có $\lambda  = 2K\alpha$, và
$$w = \sum_{i=1}^{m}  \alpha_{i} \phi (x_{i}).$$
Plugging quay lại vào Hàm Lagrange (Lagrangian) ta thu được
$$G(\alpha ) = K^{2}\alpha^{\top} \alpha  + K \sum_{i,j=1}^{m}  \alpha_{i} \alpha_{j} \langle \phi (x_{i}), \phi (x_{j})\rangle -2K \sum_{i,j=1}^{m}  \alpha_{i} \alpha_{j} \langle \phi (x_{i}), \phi (x_{j})\rangle$$
$$-2K^{2}\alpha^{\top} \alpha  + 2K\alpha^{\top} y$$
$$= -K^{2}\alpha^{\top} \alpha  -K \sum_{i,j=1}^{m}  \alpha_{i} \alpha_{j} \langle \phi (x_{i}), \phi (x_{j})\rangle + 2K\alpha^{\top} y.$$
Nếu $G$ là ma trận cho trước bởi $G_{ij} = \langle \phi (x_{i}), \phi (x_{j})\rangle$, thì ta có
$$G(\alpha ) = -K\alpha^{\top} (G + KI_{m})\alpha  + 2K\alpha^{\top} y.$$
Hàm $G$ là lõm chặt (strictly concave), do đó theo Định lý 40.13(4) nó có cực đại cho
$$\alpha  = (G + KI_{m})^{-1}y,$$
Như đã khẳng định trước đó.

<!-- PAGE 2087 -->
$$\mathbb{R}^{n}$$
Như trong tiêu chuẩn trường hợp của hồi quy Ridge (ridge regression), nếu $F =$ (nhưng tích vô hướng (inner product) $\langle$ -, $-\rangle$ là tùy ý), ta có thể thích nghi ở trên phương pháp đến learn afin hàm f(w) $= x^{\top}w + b$ thay vì của tuyến tính hàm f(w) $= x^{\top}w$, ở đâu $b \in \mathbb{R}$. Điều này time ta giả sử rằng $b$ là của tạo thành
$$-\langle  \cdots \rangle$$
$$b =\overline{y} w, (\overline{X}^{1} \overline{X}^{n}),$$
$$where X^{j}is the j column of the \frac{m}{X^{1}} \times   n \frac{matrix}{X^{n}} X whose ith row is the transpose of the$$
Vectơ cột (column vector) $\phi (x_{i})$, và ở đâu ($\cdots$) được quan điểm như vectơ cột (column vector). Ta có cực tiểu hóa bài toán Bài toán quy hoạch (KRR6'):
$$minimize\xi^{\top} \xi  + K\langle w, w\rangle$$
$$subject to$$
$$[$$
$$y_{i} -\langle w,\phi (x_{i})\rangle = \xi_{i} ,i = 1, \dots  , m,$$
$$b$$
$$[$$
Cực tiểu hóa trên $\xi$ và $w$, ở đâu $\phi (x_{i})$ là $n$ chiều vectơ $\phi (x_{i})$ - $(\overline{X}^{1} \cdots  \overline{X}^{n})$. nghiệm là cho trước theo ma trận $G$ được định nghĩa bởi
$$b$$
$$[ [$$
$$G_{ij} = \langle \phi (x_{i}),\phi (x_{j})\rangle ,$$
$$b$$
Như trước. Ta thu được
$$\alpha  = (G + KI_{m})^{-1}y,$$
$$bb$$
Và theo trước đó phép tính, $b$ được cho bởi
$$b =\overline{y} - \frac{1}{m} 1G b\alpha .$$
Ta được giải thích trong Mục 53.4 cách mà để tính ma trận $G$ từ ma trận $G$.
$$b$$
Vì số chiều của đặc trưng (feature) không gian $F$ có thể là rất lớn, một có thể worry rằng việc tính toán trong các tích $\langle \phi (x_{i}), \phi (x_{j})\rangle$ có thể là rất expensive. Điều này là ở đâu hạt nhân (kernel)
$$\mathbb{R}^{n}$$
Các hàm đến đến rescue. hạt nhân (kernel) hàm $\kappa$ cho phép nhúng (embedding) $\phi$: $\to F$ là ánh xạ $\mathbb{R}^{n} \mathbb{R}^{n} \mathbb{R} \kappa$: $\times \to$ với tính chất rằng
$$\kappa (u, v) = \langle \phi (u), \phi (v)\rangle for all u, v \in \mathbb{R}^{n}.$$
Nếu $\kappa (u, v)$ có thể được được tính trong reasonably cheap cách, và nếu $\phi (u)$ có thể được được tính cheaply, thì trong các tích $\langle \phi (x_{i}), \phi (x_{j})\rangle$ (và $\langle \phi (x_{i}), \phi (x)\rangle$) có thể được được tính cheaply; xem Chương $53$. May mắn thay có tốt hạt nhân (kernel) các hàm. Hai rất tốt sources trên hạt nhân (kernel) các phương pháp là Sch¨olkopf và Smola $[151]$ và Shawe–Taylor và Christianini $[165]$.
