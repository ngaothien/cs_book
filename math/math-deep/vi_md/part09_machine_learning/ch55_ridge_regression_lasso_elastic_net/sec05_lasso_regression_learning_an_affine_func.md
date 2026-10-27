# Lasso Hồi quy; Học (learning) Afin Hàm


<!-- PAGE 2092 -->

## 55.5 Lasso Hồi quy; Học (learning) Afin Hàm

Trong trước đó mục ta được tạo đơn giản hóa giả định rằng ta đã là cố gắng đến learn tuyến tính hàm f(x) $= x^{\top}w$. Đến learn afin hàm f(x) $= x^{\top}w + b$, ta giải sau đây tối ưu hóa bài toán Bài toán quy hoạch (lasso3):
$$minimize \frac{1}{2} \xi^{\top} \xi  + \tau 1_{n}^{\top} \epsilon$$
$$subject to$$
$$y -Xw -b1_{m} = \xi$$
$$w \le \epsilon$$
$$-w \le \epsilon .$$
Nhận thấy rằng như trong trường hợp của hồi quy Ridge (ridge regression), cực tiểu hóa là performed trên $\xi , w, \epsilon$ và $b$, nhưng $b$ là không có phạt trong hàm mục tiêu (objective function). Hàm Lagrange (Lagrangian) liên kết với điều này tối ưu hóa bài toán là
$$L(\xi , w, \epsilon , b, \lambda , \alpha_{+} , \alpha_{-} ) = \frac{1}{2} \xi^{\top} \xi  -\xi^{\top} \lambda  + \lambda^{\top} y -b1_{m}^{\top}\lambda$$
$$+ \epsilon^{\top} (\tau 1_{n} -\alpha_{+}  -\alpha_{-} ) + w^{\top}(\alpha_{+}  -\alpha_{-} -X^{\top}\lambda ),$$
Do đó bằng cách đặt gradien $\nabla L_{\xi ,w,\epsilon ,b}$ đến không ta thu được các phương trình
$$\xi  = \lambda$$
$$\alpha_{+}  -\alpha_{-} = X^{\top}\lambda$$
$$\alpha_{+}  + \alpha_{-} = \tau 1_{n}$$
$$1_{m}^{\top}\lambda  = 0.$$
Bằng cách sử dụng các phương trình này, ta tìm rằng đối ngẫu (dual) hàm là cũng cho trước bởi
$$G(\lambda , \alpha_{+} , \alpha_{-} ) = - \frac{1}{2} \begin{pmatrix} \|y -\lambda \|_{2}^{2}-\|y\|_{2}^{2} \end{pmatrix} ,$$
Và đối ngẫu (dual) lasso bài toán quy hoạch được cho bởi
$$maximize- \frac{1}{2} \begin{pmatrix} \|y -\lambda \|_{2}^{2}-\|y\|_{2}^{2} \end{pmatrix}$$
$$subject to$$
$$X^{\top}\lambda_{\infty} \le \tau$$
$$1_{m}^{\top}\lambda  = 0,$$
Mà là tương đương đến

<!-- PAGE 2093 -->
Bài toán quy hoạch (Dlasso3):
$$minimize \frac{1}{2} \|y -\lambda \|_{2}^{2}$$
$$subject to$$
$$X^{\top}\lambda_{\infty} \le \tau$$
$$1_{m}^{\top}\lambda  = 0,$$
Cực tiểu hóa trên $\lambda  \in \mathbb{R}^{m}$. Một lần $\lambda  = \xi$ và $w$ được xác định, ta thu được $b$ bằng cách sử dụng phương trình
$$b1_{m} = y -Xw -\xi ,$$
Và vì $1_{m}^{\top}1_{m} = m$ và $1_{m}^{\top}\xi  = 1_{m}^{\top}\lambda  = 0$, ở trên cho ta
$$b = \frac{1}{m} 1_{m}^{\top}y - \frac{1}{m} 1_{m}^{\top}Xw - \frac{1}{m} 1_{m}^{\top}\xi  =\overline{y} - \sum_{j=1}^{n}  \overline{X}^{j}w_{j},$$
Ở đâu $\overline{y}$ là có nghĩa của $y$ và $\overline{X}^{j}$ là có nghĩa của cột thứ $j$ của $X$. phương trình
$$b = bb +\overline{y} - \sum_{j=1}^{n}  \overline{X}^{j}w_{j} = bb +\overline{y} -(\overline{X}^{1} \cdots  \overline{X}^{n})w,$$
Có thể được được sử dụng như trong hồi quy Ridge (ridge regression), (xem Mục 55.2), để chỉ ra rằng Bài toán quy hoạch (lasso3) là tương đương đến áp dụng lasso hồi quy (lasso2) mà không có intercept số hạng đến được tâm dữ liệu, bằng cách thay thế $y$ bởi $y = y$ - $\overline{y} 1$ và $X$ bởi $X = X$ - $\overline{X}$. Thì $b$ được cho bởi
$$b b$$
$$- \cdots$$
$$b =\overline{y}(\overline{X}^{1} \overline{X}^{n})w,$$
$$b$$
Ở đâu $w$ là nghiệm cho trước bởi (lasso2). Điều này là phương pháp được mô tả bởi Hastie, Tibshirani, $b$ và Wainwright $[92]$ (Mục 2.2).

> **Ví dụ 55.3.** Ta có thể create dữ liệu tập hợp $(X, y)$ ở đâu $X$ một ma trận cỡ $100\times 5$ và $y$ là $100\times 1$ vectơ bằng cách sử dụng sau đây Matlab bài toán quy hoạch trong mà command randn creates mảng (array) của một cách chuẩn tắc/bình thường distributed các số. $X =$ randn(100,5); ww $= [0; 2; 0; -3; 0]; y =$ X*ww $+$ randn(100,1)*0.1; mục đích của thứ ba đường thẳng là đến cộng một số nhỏ noise đến “output” $X$ * ww. thứ nhất năm các hàng của $X$ là
$$\begin{pmatrix} -1.1658 & -0.0679 & -1.6118 & 0.3199 & 0.4400 \\ -1.1480 & -0.1952 & -0.0245 & -0.5583 & -0.6169 \\ 0.1049 & -0.2176 & -1.9488 & -0.3114 & 0.2748 \\ 0.7223 & -0.3031 & 1.0205 & -0.5700 & 0.6011 \\ 2.5855 & 0.0230 & 0.8617 & 1.0257 & 0.0923 \end{pmatrix} ,$$
$$-$$

<!-- PAGE 2094 -->
Và thứ nhất năm các hàng của $y$ là
$$y = \begin{pmatrix} -1.0965 \\ 1.2155 \\ 0.4324 \\ 1.1902 \\ 3.1346 \end{pmatrix} .$$
Ta ran bài toán quy hoạch cho lasso bằng cách sử dụng ADMM (xem Bài toán 52.7) với khác nhau các giá trị của $\rho$ và $\tau$, bao gồm cả $\rho  = 1$ và $\rho  = 10$. Ta được quan sát rằng bài toán quy hoạch hội tụ nhiều faster cho $\rho  = 10$ hơn cho $\rho  = 1$. Ta plotted các giá trị của năm các thành phần của $w(\tau$) cho các giá trị của $\tau$ từ $\tau  = 0$ đến $\tau  =$ 0.5 bởi increment của 0.02, và được quan sát rằng thứ nhất, thứ ba, và thứ năm tọa độ bỏ basically một cách tuyến tính đến không (giá trị ít hơn rằng $10^{-4})$ xung quanh $\tau  =$ 0.2. Xem Các hình 55.7, 55.8, và 55.9. Điều này behavior cũng được quan sát trong Hastie, Tibshirani, và Wainwright $[92]$ (Mục 2.2).
$$5 \overline{#}\overline{10}\overline{-3}$$
$$2.02$$
$$2$$
$$01.98$$
$$1.96$$
$$-51.94$$
$$1.92$$
$$-101.9$$
$$1.88$$
$$-151.86$$
$$1.84$$
$$-20$$
$$0\overline{0.05}\overline{0.1}\overline{0.15}\overline{0.2}\overline{0.25}\overline{0.3}\overline{0.35}\overline{0.4}\overline{0.45}\overline{0.5} 1.82$$
$$0\overline{0.05}\overline{0.1}\overline{0.15}\overline{0.2}\overline{0.25}\overline{0.3}\overline{0.35}\overline{0.4}\overline{0.45}\overline{0.5}$$
$$Figure 55.7: First and second component of w.$$
$$0.045-2.6$$
$$0.04$$
$$-2.65$$
$$0.035$$
$$-2.7$$
$$0.03$$
$$0.025-2.75$$
$$0.02-2.8$$
$$0.015-2.85$$
$$0.01$$
$$-2.9$$
$$0.005$$
$$-2.95$$
$$0$$
$$-0.005-3$$
$$0\overline{0.05}\overline{0.1}\overline{0.15}\overline{0.2}\overline{0.25}\overline{0.3}\overline{0.35}\overline{0.4}\overline{0.45}\overline{0.5} 0\overline{0.05}\overline{0.1}\overline{0.15}\overline{0.2}\overline{0.25}\overline{0.3}\overline{0.35}\overline{0.4}\overline{0.45}\overline{0.5}$$
$$Figure 55.8: Third and fourth component of w.$$

<!-- PAGE 2095 -->
Cho $\tau  =$ 0.02, ta có
$$w = \begin{pmatrix} 0.00003 \\ 2.01056 \\ -0.00004 \\ -2.99821 \\ 0.00000 \end{pmatrix} ,b = 0.00135.$$
$$\overline{#}\overline{10}\overline{-3}$$
$$2$$
$$0$$
$$-2$$
$$-4$$
$$-6$$
$$-8$$
$$-10$$
$$0\overline{0.05}\overline{0.1}\overline{0.15}\overline{0.2}\overline{0.25}\overline{0.3}\overline{0.35}\overline{0.4}\overline{0.45}\overline{0.5}$$
$$Figure 55.9: Fifth component of w.$$
Điều này trọng số vectơ $w$ là rất close đến ban đầu vectơ ww $= [0; 2; 0; -3; 0]$ rằng ta được sử dụng đến create $y$. Cho lớn các giá trị của $\tau$, trọng số vectơ là về cơ bản không vectơ. Điều này xảy ra cho $\tau  = 235$, ở đâu mọi thành phần của $w$ là ít hơn $10^{-5}$. Một cái khác cách để tìm $b$ là đến cộng số hạng $(C/2)b^{2}$ đến hàm mục tiêu (objective function), với một số dương hằng số $C$, thu được bài toán quy hoạch Bài toán quy hoạch(lasso4):
$$minimize \frac{1}{2} \xi^{\top} \xi  + \tau 1_{n}^{\top} \epsilon  + \frac{1}{2} Cb^{2}$$
$$subject to$$
$$y -Xw -b1_{m} = \xi$$
$$w \le \epsilon$$
$$-w \le \epsilon ,$$
Cực tiểu hóa trên $\xi , w, \epsilon$ và $b$. Điều này time Hàm Lagrange (Lagrangian) là
$$-$$
$$L(\xi , w, \epsilon , b, \lambda , \alpha_{+} , \alpha_{-} ) = \frac{1}{2} \xi^{\top} \xi  -\xi^{\top} \lambda  + \lambda^{\top} y + \frac{C}{2} b^{2}b1_{m}^{\top}\lambda$$
$$+ \epsilon^{\top} (\tau 1_{n} -\alpha_{+}  -\alpha_{-} ) + w^{\top}(\alpha_{+}  -\alpha_{-} -X^{\top}\lambda ),$$

<!-- PAGE 2096 -->
Do đó bằng cách đặt gradien $\nabla L_{\xi ,w,\epsilon ,b}$ đến không ta thu được các phương trình
$$\xi  = \lambda$$
$$\alpha_{+}  -\alpha_{-} = X^{\top}\lambda$$
$$\alpha_{+}  + \alpha_{-} = \tau 1_{n}$$
$$Cb = 1_{m}^{\top}\lambda .$$
Do đó $b$ cũng được xác định, và đối ngẫu (dual) lasso bài toán quy hoạch là đồng nhất đến thứ nhất lasso đối ngẫu (dual) (Dlasso2), cụ thể là
$$minimize \frac{1}{2} \|y -\lambda \|_{2}^{2}$$
$$subject to$$
$$X^{\top}\lambda_{\infty} \le \tau ,$$
Cực tiểu hóa trên $\lambda$. Vì các phương trình $\xi  = \lambda$ và
$$y -Xw -b1_{m} = \xi$$
Đúng, từ Cb $= 1_{m}^{\top}\lambda$ ta thu được
$$1$$
$$\frac{1}{m} 1_{m}^{\top}y - \frac{1}{m} 1_{m}^{\top}Xw -b\overline{m} 1_{m}^{\top}1 = \frac{1}{m} 1_{m}^{\top}\lambda ,$$
Rằng là
$$- \cdots  -$$
$$\overline{y}(\overline{X}^{1} \overline{X}^{n})wb = \frac{C}{m} b,$$
Mà cho ta
$$- \cdots$$
$$b = \frac{m}{m + C} (\overline{y}(\overline{X}^{1} \overline{X}^{n})w).$$
Như trong trường hợp của hồi quy Ridge (ridge regression), defect của cách tiếp cận ở đâu $b$ là cũng có phạt là rằng nghiệm cho $b$ là không bất biến dưới cộng hằng số $c$ đến mỗi giá trị $y_{i}$ Nó là thú vị đến compare behavior của các phương pháp: $1$. Hồi quy Ridge (ridge regression) (RR6') (mà là tương đương đến (RR3)). $2$. Hồi quy Ridge (ridge regression) (RR3b), với $b$ có phạt (bằng cách cộng số hạng $Kb^{2}$ đến hàm mục tiêu (objective function)). $3$. Bình phương tối thiểu (least squares) ứng dụng đến $[X 1]. 4$. (lasso3).
