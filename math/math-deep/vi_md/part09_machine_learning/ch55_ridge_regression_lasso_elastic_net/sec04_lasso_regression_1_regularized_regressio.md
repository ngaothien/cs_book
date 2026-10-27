# Lasso Hồi quy (1-Regularized Hồi quy)


<!-- PAGE 2088 -->

## 55.4 Lasso Hồi quy (\ell 1-Regularized Hồi quy)

Chính weakness của hồi quy Ridge (ridge regression) là rằng estimated trọng số vectơ $w$ thường có nhiều khác không các hệ số. Hệ quả là, hồi quy Ridge (ridge regression) thực hiện không scale lên tốt. Trong thực tế ta cần các phương pháp capable của handling millions của các tham số, hoặc nhiều hơn/thêm. cách đến encourage sparsity của vectơ $w$, mà có nghĩa là nhiều các tọa độ của $w$ là không, là đến thay thế toàn phương hình phạt (penalty) hàm $\tau w^{\top}w = \tau  \|w\|_{2}^{2}$ bởi hình phạt (penalty) hàm $\tau  \|w\|_{1}$, với $\ell^{2}$ -chuẩn (norm) được thay thế bởi $\ell^{1}$ -chuẩn (norm). phương pháp này đã là thứ nhất proposed bởi Tibshirani xung quanh $1996$, dưới name lasso, mà stands cho “least tuyệt đối selection và shrinkage toán tử.” phương pháp này là cũng đã biết như $\ell^{1}$ -regularized hồi quy, nhưng điều này là không như cute như “lasso,” mà được sử dụng predominantly.
$$\mathbb{R}^{n} \mathbb{R}$$
Cho trước tập hợp của huấn luyện (training) dữ liệu ${(x_{1}, y_{1}), \dots  , (x_{m}, y_{m})}$, với $x_{i} \in$ và $y_{i} \in$, nếu $X$ là ma trận cỡ $m \times  n$
$$X = \begin{pmatrix} x_{1}^{\top} \\ \vdots \\ x_{m}^{\top} \end{pmatrix} ,$$
Trong mà các vectơ hàng $x_{i}^{\top}$ là các hàng của $X$, thì lasso hồi quy là sau đây tối ưu hóa bài toán Bài toán quy hoạch (lasso1):
$$minimize \frac{1}{2} \xi^{\top} \xi  + \tau  \|w\|_{1}$$
$$subject to$$
$$y -Xw = \xi ,$$
Cực tiểu hóa trên $\xi$ và $w$, ở đâu $\tau  > 0$ là một số hằng số xác định influence của regularizing số hạng $\|w\|_{1}$. hàm mục tiêu (objective function) được biểu diễn theo $w$ là
$$J(w) = \frac{1}{2} (Xw -y)^{\top}(Xw -y) + \tau  \|w\|_{1}$$
$$= \frac{1}{2} w^{\top}X^{\top}Xw -w^{\top}X^{\top}y + \frac{1}{2} y^{\top}y + \tau  \|w\|_{1} .$$
Hàm này là lồi, nhưng không nhất thiết lồi chặt (strictly convex). Vì nó là không âm, nó có cực tiểu, nhưng nói chung nó là không đạt được bởi duy nhất $w$. difficulty với regularizing số hạng $\|w\|_{1} = |w_{1}| + \cdots  + |w_{n}|$ là rằng ánh xạ $w \mapsto \|w\|_{1}$ là không khả vi (differentiable) với mọi $w$. Điều này difficulty có thể được overcome bằng cách sử dụng các dưới gradien, nhưng đối ngẫu (dual) của ở trên bài toán quy hoạch có thể cũng là thu được trong sơ cấp cách thức bằng cách sử dụng mẹo/kỹ thuật rằng ta đã được sử dụng, mà là rằng nếu $x \in \mathbb{R}$, thì
$$|x| = \max{x, -x}.$$

<!-- PAGE 2089 -->
$$\mathbb{R}^{n}$$
Bằng cách sử dụng điều này mẹo/kỹ thuật, bởi giới thiệu vectơ $\epsilon  \in$ của không âm các biến, ta có thể viết lại lasso cực tiểu hóa như sau: Bài toán quy hoạch lasso chỉnh quy hóa (regularization) (lasso2):
$$minimize \frac{1}{2} \xi^{\top} \xi  + \tau 1_{n}^{\top} \epsilon$$
$$subject to$$
$$y -Xw = \xi$$
$$w \le \epsilon$$
$$-w \le \epsilon .$$
Cực tiểu hóa trên $\xi , w$ và $\epsilon$, với $y, \xi  \in \mathbb{R}^{m}$, và $w, \epsilon , 1_{n} \in \mathbb{R}^{n}$. các ràng buộc $w \le \epsilon$ và $-w \le \epsilon$ là tương đương đến $|w_{i}| \le \epsilon_{i}$ cho $i = 1, \dots  , n$, do đó cho nghiệm tối ưu (optimal solution) ta phải có $\epsilon  \ge 0$ và $|w_{i}| = \epsilon_{i}$, nghĩa là, $\|w\|_{1} = \epsilon_{1}  + \cdots  + \epsilon_{n}$. Hàm Lagrange (Lagrangian) $L(\xi , w, \epsilon , \lambda , \alpha_{+} , \alpha_{-}$) được cho bởi
$$L(\xi , w, \epsilon , \lambda , \alpha_{+} , \alpha_{-} ) = \frac{1}{2} \xi^{\top} \xi  + \tau 1_{n}^{\top} \epsilon  + \lambda^{\top} (y -Xw -\xi )$$
$$+ \alpha_{+}^{\top} (w -\epsilon ) + \alpha_{-}^{\top} (-w -\epsilon )$$
$$= \frac{1}{2} \xi^{\top} \xi  -\xi^{\top} \lambda  + \lambda^{\top} y$$
$$+ \epsilon^{\top} (\tau 1_{n} -\alpha_{+}  -\alpha_{-} ) + w^{\top}(\alpha_{+}  -\alpha_{-} -X^{\top}\lambda ),$$
$$\mathbb{R}^{m} \mathbb{R}_{+}^{n}$$
Với $\lambda  \in$ và $\alpha_{+} , \alpha_{-} \in$. Vì hàm mục tiêu (objective function) là lồi và các ràng buộc là afin (và do đó qualified), Hàm Lagrange (Lagrangian) $L$ có cực tiểu đối với gốc (primal) các biến, $\xi , w, \epsilon$ khi và chỉ khi $\nabla L_{\xi ,w,\epsilon} = 0$. Vì gradien $\nabla L_{\xi ,w,\epsilon}$ được cho bởi
$$\nabla L_{\xi ,w,\epsilon} = \begin{pmatrix} \xi  -\lambda \\ \alpha_{+}  -\alpha_{-} -X^{\top}\lambda \\ \tau 1_{n} & \alpha_{+} & \alpha_{-} \end{pmatrix} ,$$
$$- -$$
Ta thu được các phương trình
$$\xi  = \lambda$$
$$\alpha_{+}  -\alpha_{-} = X^{\top}\lambda$$
$$\alpha_{+}  + \alpha_{-} = \tau 1_{n}.$$
Bằng cách sử dụng các phương trình này, đối ngẫu (dual) hàm $G(\lambda , \alpha_{+} , \alpha_{-}$) $= min_{\xi ,w,\epsilon} L$ được cho bởi
$$G(\lambda , \alpha_{+} , \alpha_{-} ) = \frac{1}{2} \xi^{\top} \xi  -\xi^{\top} \lambda  + \lambda^{\top} y = \frac{1}{2} \lambda^{\top} \lambda  -\lambda^{\top} \lambda  + \lambda^{\top} y$$
$$= - \frac{1}{2} \lambda^{\top} \lambda  + \lambda^{\top} y = - \frac{1}{2} \begin{pmatrix} \|y -\lambda \|_{2}^{2}-\|y\|_{2}^{2} \end{pmatrix} ,$$

<!-- PAGE 2090 -->
Do đó
$$G(\lambda , \alpha_{+} , \alpha_{-} ) = - \frac{1}{2} \begin{pmatrix} \|y -\lambda \|_{2}^{2}-\|y\|_{2}^{2} \\ minimumof( \end{pmatrix} .$$
Vì $\alpha_{+} , \alpha_{-} \ge 0$, với mọi $i \in {1, \dots  , n}$ $\alpha_{+} )_{i}$ - $(\alpha_{-} )_{i}$ là $-\tau$, và cực đại là $\tau$. Nếu ta nhắc lại rằng với mọi $z \in \mathbb{R}^{n}$,
$$\|z\|_{\infty}= \max |z_{i}|,$$
$$1\le i\le n$$
Suy ra rằng các ràng buộc
$$\alpha_{+}  + \alpha_{-} = \tau 1_{n}$$
$$X^{\top}\lambda  = \alpha_{+}  -\alpha_{-}$$
Là tương đương đến
$$X^{\top}\lambda_{\infty} \le \tau .$$
Ở trên là tương đương đến 2n các ràng buộc
$$-\tau  \le (X^{\top}\lambda )_{i} \le \tau ,1 \le i \le n.$$
Vì vậy, đối ngẫu (dual) lasso bài toán quy hoạch được cho bởi
$$maximize- \frac{1}{2} \begin{pmatrix} \|y -\lambda \|_{2}^{2}-\|y\|_{2}^{2} \end{pmatrix}$$
$$subject to$$
$$X^{\top}\lambda_{\infty} \le \tau ,$$
Mà (vì $\|y\|_{2}^{2}$ là hằng số số hạng) là tương đương đến Bài toán quy hoạch (Dlasso2):
$$minimize \frac{1}{2} \|y -\lambda \|_{2}^{2}$$
$$subject to$$
$$X^{\top}\lambda_{\infty} \le \tau ,$$
Cực tiểu hóa trên $\lambda  \in \mathbb{R}^{m}$. Một cách để giải lasso hồi quy là để sử dụng đối ngẫu (dual) bài toán quy hoạch để tìm $\lambda  = \xi$, và thì để sử dụng quy hoạch tuyến tính (linear programming) để tìm $w$ bởi việc giải bài toán quy hoạch tuyến tính (linear program) phát sinh từ lasso gốc (primal) bởi giữ $\xi$ hằng số. tốt nhất cách là để sử dụng ADMM như được giải thích trong Mục 52.8(4). Có cũng số của variations của hạ gradien (gradient descent); xem Hastie, Tibshirani, và Wainwright $[92]$. Trong lý thuyết, nếu ta biết hỗ trợ/giá (support) của $w$ và các dấu của các thành phần của nó, thì $w$ được xác định như ta bây giờ giải thích.

<!-- PAGE 2091 -->
Xét theo ràng buộc $y$ - Xw $= \xi$ và sự kiện rằng cho nghiệm tối ưu (optimal solution) ta phải có $\xi  = \lambda$, sau đây điều kiện phải đúng:
$$X^{\top}(Xw -y)_{\infty}\le \tau .(*)$$
Cũng nhận thấy rằng cho nghiệm tối ưu (optimal solution), ta có
$$-$$
$$\frac{1}{2} \|y -Xw\|_{2}^{2} + w^{\top}X^{\top}(y -Xw) = \frac{1}{2} \|y\|^{2}w^{\top}X^{\top}y + \frac{1}{2} w^{\top}X^{\top}Xw + w^{\top}X^{\top}y -w^{\top}X^{\top}Xw$$
$$= \frac{1}{2} \begin{pmatrix} \|y\|_{2}^{2}-\|Xw\|_{2}^{2} \end{pmatrix}$$
$$= \frac{1}{2} \begin{pmatrix} \|y\|_{2}^{2}-\|y -\lambda \|_{2}^{2} \end{pmatrix} = G(\lambda ).$$
Vì hàm mục tiêu (objective function) là lồi và constaints là qualified, theo Định lý 50.19(2) khoảng cách đối ngẫu (duality gap) là không, do đó cho tối ưu các nghiệm của gốc (primal) và đối ngẫu (dual), $G(\lambda$) $= L(\xi , w, \epsilon$), nghĩa là
$$\frac{1}{2} \|y -Xw\|_{2}^{2} + w^{\top}X^{\top}(y -Xw) = \frac{1}{2} \|\xi \|_{2}^{2} + \tau  \|w\|_{1} = \frac{1}{2} \|y -Xw\|_{2}^{2} + \tau  \|w\|_{1} ,$$
Mà cho ta phương trình
$$w^{\top}X^{\top}(y -Xw) = \tau  \|w\|_{1} .(**_{1})$$
Ở trên là tích vô hướng (inner product) của $w$ và $X^{\top}(y$ - Xw), do đó bất cứ khi nào $w_{i}$ ̸ $= 0$, vì $\|w\|_{1} = |w_{1}| + \cdots  + |w_{n}|$, xét theo (*), ta phải có $(X^{\top}(y$ - $Xw))_{i} = \tau sgn(w_{i})$. Nếu
$$S = {i \in {1, \dots  , n} | w_{i} \neq  0},(\dagger )$$
Nếu $X_{S}$ ký hiệu ma trận bao gồm của các cột của $X$ được chỉ số bởi $S$, và nếu $w_{S}$ ký hiệu vectơ bao gồm của khác không các thành phần của $w$, thì ta có
$$X_{S}^{\top} (y -X_{S}w_{S}) = \tau sgn(w_{S}).(**_{2})$$
Ta cũng có
$$X_{S}^{\top} (y -X_{S}w_{S})_{\infty}\le \tau ,(**_{3})$$
Ở đâu $\overline{S}$ là phần bù của $S$. Phương trình $(**_{2})$ cho ta
$$X_{S}^{\top} X_{S}w_{S} = X_{S}^{\top} y -\tau sgn(w_{S}),$$
Do đó nếu $X_{S}^{\top} X_{S}$ là khả nghịch (mà sẽ là trường hợp nếu các cột của $X$ là độc lập tuyến tính (linearly independent)), ta thu được
$$w_{S} = (X_{S}^{\top} X_{S})^{-1}(X_{S}^{\top} y -\tau sgn(w_{S})).(**_{4})$$
Trong lý thuyết, nếu ta biết hỗ trợ/giá (support) của $w$ và các dấu của các thành phần của nó, thì $w_{S}$ được xác định, nhưng trong thực tế điều này là useless vì bài toán là để tìm hỗ trợ/giá (support) và dấu của nghiệm.
