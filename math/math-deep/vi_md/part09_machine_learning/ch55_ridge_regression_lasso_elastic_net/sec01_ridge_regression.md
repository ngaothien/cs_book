# Hồi quy Ridge (ridge regression)


<!-- PAGE 2072 -->
Nó. Một của tốt nhất các phương pháp relies trên ADMM (xem Mục 52.8) và được thảo luận trong Mục 55.4. lasso phương pháp có một số limitations, đặc biệt khi số $m$ của dữ liệu là nhỏ hơn hơn số chiều $n$ của dữ liệu. Điều này xảy ra trong một số các ứng dụng trong genetics và medicine. May mắn thay có một cách đến combine tốt nhất các đặc trưng của hồi quy Ridge (ridge regression) và lasso, mà là để sử dụng hai regularizing các số hạng: $1$. $\ell^{2}$ -số hạng $(1/2)K \|w\|_{2}^{2}$ như trong hồi quy Ridge (ridge regression) (với $K > 0). 2$. $\ell^{1}$ -số hạng $\tau  \|w\|_{1}$ như trong lasso. phương pháp này là đã biết như mạng đàn hồi (elastic net) hồi quy và được thảo luận trong Mục 55.6. Nó retains hầu hết của desirable các đặc trưng của hồi quy Ridge (ridge regression) và lasso, và các khử một số của của chúng weaknesses. Hơn nữa, nó là effectively được giải bởi ADMM.

## 55.1 Hồi quy Ridge (ridge regression)

Bài toán của việc giải quá xác định hoặc underdetermined hệ phương trình tuyến tính Aw $= y$, ở đâu $A$ là một ma trận cỡ $m \times  n$, phát sinh như “học (learning) bài toán” trong mà ta quan sát dãy của dữ liệu $((a_{1}, y_{1}), \dots  , (a_{m}, y_{m}))$, được quan điểm như input-output các cặp của một số unknown hàm $f$ rằng ta là cố gắng đến infer, ở đâu $a_{i}$ là các hàng của ma trận $A$ và $y_{i} \in \mathbb{R}$. các giá trị $y_{i}$ đôi khi được gọi là labels hoặc responses. đơn giản nhất loại của hàm là tuyến tính hàm
$$\mathbb{R}^{n}$$
F(x) $= x^{\top}w$, ở đâu $w \in$ là vectơ của các hệ số thường được gọi là trọng số vectơ, hoặc đôi khi estimator. Trong statistical literature $w$ là thường được ký hiệu bởi $\beta$. Vì bài toán là quá xác định và vì của ta các nhận xét có thể là subject đến các sai số, ta có thể’t giải cho $w$ chính xác như nghiệm của hệ Aw $= y$, do đó thay vì ta giải least-square bài toán của cực tiểu hóa $\|Aw$ - $y\|_{2}^{2}$. Trong Mục 23.1 ta đã chỉ ra rằng bài toán này có thể được được giải bằng cách sử dụng nghịch đảo giả (pseudo-inverse). Ta biết rằng các điểm cực tiểu hóa $w$ là các nghiệm của chuẩn tắc/bình thường các phương trình $A^{\top}Aw = A^{\top}y$, nhưng khi $A^{\top}A$ là không khả nghịch, như vậy nghiệm là không duy nhất do đó một số tiêu chuẩn có được sử dụng đến chọn trong số các nghiệm này. Một nghiệm là đến chọn duy nhất vectơ $w^{+}$ của nhỏ nhất Euclidean chuẩn (norm) $\|w^{+}\|_{2}$ rằng cực tiểu hóa $\|Aw$ - $y\|_{2}^{2}$. nghiệm $w^{+}$ được cho bởi $w^{+} = A^{+}y$, ở đâu $A^{+}$ là pseudoinverse của $A$. ma trận $A^{+}$ là thu được từ SVD của $A$, nói $A = V \Sigma U^{\top}$. Cụ thể là, $A^{+} = U\Sigma^{+} V^{\top}$, ở đâu $\Sigma^{+}$ là ma trận thu được từ $\Sigma$ bằng cách thay thế mọi khác không giá trị kỳ dị (singular value) $\sigma_{i}$ trong $\Sigma$ bởi $\sigma_{i}^{-1}$, để lại tất cả các không điểm trong place, và thì transposing. difficulty với điều này cách tiếp cận là rằng nó đòi hỏi biết liệu giá trị kỳ dị (singular value) là không hoặc rất nhỏ nhưng khác không. rất nhỏ khác không giá trị kỳ dị (singular value) $\sigma$ trong $\Sigma$ cho ta rất lớn giá trị $\sigma^{-1}$ trong $\Sigma^{+}$, nhưng $\sigma  = 0$ vẫn còn $0$ trong $\Sigma^{+}$. Điều này discontinuity hiện tượng là không desirable và một cái khác cách là đến control kích thước của $w$ bằng cách cộng chỉnh quy hóa (regularization) số hạng đến $\|Aw$ - $y\|^{2}$, và tự nhiên candidate là $\|w\|^{2}$.

<!-- PAGE 2073 -->
Nó là thông lệ đến rename mỗi vectơ cột (column vector) $a_{i}^{\top}$ như $x_{i}$ (ở đâu $x_{i} \in \mathbb{R}^{n})$ và đến rename input dữ liệu ma trận $A$ như $X$, sao cho vectơ hàng (row vector) $x_{i}^{\top}$ là các hàng của ma trận cỡ $m \times  n$ $X$
$$X = \begin{pmatrix} x_{1}^{\top} \\ \vdots \\ x_{m}^{\top} \end{pmatrix} .$$
Của ta tối ưu hóa bài toán, được gọi là hồi quy Ridge (ridge regression), là Bài toán quy hoạch (RR1):
$$minimize\|y -Xw\|^{2}+ K \|w\|^{2},$$
Mà bởi giới thiệu mới biến $\xi  = y$ - Xw có thể được được viết lại như Bài toán quy hoạch (RR2):
$$minimize\xi^{\top} \xi  + Kw^{\top}w$$
$$subject to$$
$$y -Xw = \xi ,$$
Ở đâu $K > 0$ là một số hằng số xác định influence của regularizing số hạng $w^{\top}w$, và ta cực tiểu hóa trên $\xi$ và $w$. hàm mục tiêu (objective function) của thứ nhất phiên bản của của ta cực tiểu hóa bài toán có thể được biểu diễn dưới dạng
$$J(w) = \|y -Xw\|^{2}+ K \|w\|^{2}$$
$$= (y -Xw)^{\top}(y -Xw) + Kw^{\top}w$$
$$= y^{\top}y -2w^{\top}X^{\top}y + w^{\top}X^{\top}Xw + Kw^{\top}w$$
$$= w^{\top}(X^{\top}X + KI_{n})w -2w^{\top}X^{\top}y + y^{\top}y.$$
Ma trận $X^{\top}X$ là đối xứng nửa xác định dương (positive semidefinite) và $K > 0$, do đó ma trận $X^{\top}X+KI_{n}$ là xác định dương (positive definite). Suy ra rằng
$$J(w) = w^{\top}(X^{\top}X + KI_{n})w -2w^{\top}X^{\top}y + y^{\top}y$$
Là lồi chặt (strictly convex), do đó theo Định lý 40.13(2)-(4), nó có duy nhất cực tiểu khi và chỉ khi $\nabla J_{w} = 0$. Vì
$$\nabla J_{w} = 2(X^{\top}X + KI_{n})w -2X^{\top}y,$$
Ta suy ra rằng
$$w = (X^{\top}X + KI_{n})^{-1}X^{\top}y.(*_{wp})$$
Có một thú vị connection giữa ma trận $(X^{\top}X+KI_{n})^{-1}X^{\top}$ và pseudoinverse $X^{+}$ của $X$.

<!-- PAGE 2074 -->

> **Mệnh đề 55.1.** giới hạn của ma trận $(X^{\top}X + KI_{n})^{-1}X^{\top}$ khi $K > 0$ đi đến không là nghịch đảo giả (pseudo-inverse) $X^{+}$ của $X$.

*Chứng minh.* để chỉ ra điều này cho $X = V \Sigma U^{\top}$ là SVD của $X$. Thì
$$(X^{\top}X + KI_{n}) = U\Sigma^{\top} V^{\top} V \Sigma U^{\top} + KI_{n} = U(\Sigma^{\top} \Sigma  + KI_{n})U^{\top} ,$$
Do đó $(X^{\top}X + KI_{n})^{-1}X^{\top} = U(\Sigma^{\top} \Sigma  + KI_{n})^{-1}U^{\top} U\Sigma^{\top} V^{\top} = U(\Sigma^{\top} \Sigma  + KI_{n})^{-1}\Sigma^{\top} V^{\top}$. đường chéo các phần tử (entries) trong ma trận $(\Sigma^{\top} \Sigma  + KI_{n})^{-1}\Sigma^{\top}$ là
$$\frac{\sigma_{i}}{\sigma_{i}^{2} +} K ,if \sigma_{i}  > 0,$$
Và không nếu $\sigma_{i}  = 0$. Tất cả nondiagonal các phần tử (entries) là không. Khi $\sigma_{i}  > 0$ và $K > 0$ đi đến $0$,
$$Klim\mapsto 0 \frac{\sigma_{i}}{\sigma_{i}^{2} + K} = \sigma_{i}^{-1}  ,$$
Do đó
$$lim(\Sigma^{\top} \Sigma  + KI_{n})^{-1}\Sigma^{\top} = \Sigma^{+} ,$$
$$K\mapsto 0$$
Mà suy ra rằng
$$lim(X^{\top}X + KI_{n})^{-1}X^{\top}= X^{+}.$$
$$K\mapsto 0$$
Đối ngẫu (dual) hàm của thứ nhất formulation của bài toán của chúng ta là hằng số hàm (với giá trị cực tiểu của $J)$ do đó nó là không hữu ích, nhưng thứ hai formulation của bài toán của chúng ta cho ta thú vị bài toán đối ngẫu (dual problem). Hàm Lagrange (Lagrangian) là
$$L(\xi , w, \lambda ) = \xi^{\top} \xi  + Kw^{\top}w + (y -Xw -\xi )^{\top}\lambda$$
$$= \xi^{\top} \xi  + Kw^{\top}w -w^{\top}X^{\top}\lambda  -\xi^{\top} \lambda  + \lambda^{\top} y,$$
Với $\lambda , \xi , y \in \mathbb{R}^{m}$. Hàm Lagrange (Lagrangian) $L(\xi , w, \lambda$), như hàm của $\xi$ và $w$ với $\lambda$ held cố định, là hiển nhiên lồi, thực ra lồi chặt (strictly convex). Đến derive đối ngẫu (dual) hàm $G(\lambda$) ta cực tiểu hóa $L(\xi , w, \lambda$) đối với $\xi$ và $w$. Vì $L(\xi , w, \lambda$) là (chặt) lồi như hàm của $\xi$ và $w$, theo Định lý 40.13(4), nó có cực tiểu khi và chỉ khi của nó gradien $\nabla L_{\xi ,w}$ là không (thực ra, theo Định lý 40.13(2), duy nhất cực tiểu vì hàm là lồi chặt (strictly convex)). Vì
$$\nabla L_{\xi ,w} = \begin{pmatrix} 2\xi  -\lambda \\ 2Kw -X^{\top}\lambda \end{pmatrix} ,$$
Ta thu được
$$\lambda  = 2\xi$$
$$\xi$$
$$w = \frac{1}{2} K X^{\top}\lambda  = X^{\top}K .$$
