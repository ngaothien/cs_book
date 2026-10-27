# Các bài tập


<!-- PAGE 1940 -->
$\bullet$ x-update, z-update, $\lambda$ -update. $\bullet$ Scaled tạo thành của ADMM. $\bullet$ Phần dư (residual), đối ngẫu (dual) phần dư (residual). $\bullet$ Stopping các tiêu chuẩn. $\bullet$ Proximity toán tử, proximal cực tiểu hóa. $\bullet$ Toàn phương quy hoạch. $\bullet$ KKT các phương trình. $\bullet$ Soft thresholding toán tử. $\bullet$ Shrinkage toán tử. $\bullet$ Least tuyệt đối deviation. $\bullet$ Cơ sở (basis) pursuit. $\bullet$ Tổng quát $\ell^{1}$ -regularized mất mát (loss) cực tiểu hóa. $\bullet$ Lasso chỉnh quy hóa (regularization). $\bullet$ Suy rộng/tổng quát hóa lasso chỉnh quy hóa (regularization). $\bullet$ Nhóm lasso.

## 52.10 Các bài tập

Bài toán 52.1. Trong phương pháp của các nhân tử được mô tả trong Mục 52.2, chứng minh rằng chọn $\alpha^{k} = \rho$ các đảm bảo rằng $(u^{k+1}, \lambda^{k+1}$) thỏa mãn phương trình
$$\nabla J_{uk+1} + A^{\top}\lambda^{k+1} = 0.$$
Bài toán 52.2. Chứng minh rằng Bất đẳng thức (A1) suy ra từ Các bất đẳng thức (A2) và (A3) (xem chứng minh của Định lý 52.1). Cho help consult Phụ lục $A$ của Boyd et al. $[28]$.
Bài toán 52.3. Xét Ví dụ 52.8. Chứng minh rằng nếu $f = I_{C}$, indicator hàm của khác rỗng đóng tập lồi (convex set) $C$, thì
$$x^{+}= arg minx \begin{pmatrix} I_{C}(x) + (\rho /2) \|x -v\|_{2}^{2} \end{pmatrix} = \Pi_{C} (v),$$
Phép chiếu trực giao (orthogonal projection) của $v$ lên $C$. Trong trường hợp đặc biệt khi $C =\mathbb{R}_{+}^{n}$ (thứ nhất orthant), thì
$$x^{+}= (v)_{+},$$
Vectơ thu được bằng cách đặt âm các thành phần của $v$ đến không.

<!-- PAGE 1941 -->
Bài toán 52.4. Chứng minh rằng soft thresholding toán tử $S_{c}$ từ Mục 52.8 thỏa mãn các phương trình
$$S_{c}(v) = (v -c)_{+} -(-v -c)_{+},$$
Và
$$S_{c}(v) = (1 -c/|v|)_{+}v,v \neq  0.$$
Bài toán 52.5. Rederive công thức
$$v -cif v > c$$
$$$$
$$$$
$$S_{c}(v) =0if |v| \le c$$
$$v + cif v < -c$$
$$$$
Bằng cách sử dụng các dưới gradien.
Bài toán 52.6. Trong cơ sở (basis) pursuit (xem Mục 52.8 $(2))$ chứng minh rằng
$$x^{k+1}= (I -A^{\top}(AA^{\top})^{-1}A)(z^{k}-u^{k}) + A^{\top}(AA^{\top})^{-1}b.$$
Bài toán 52.7. Cài đặt (trong Matlab) ADMM ứng dụng đến lasso chỉnh quy hóa (regularization) như được mô tả trong Mục 52.6 $(4)$. stopping tiêu chuẩn nên là based trên tính chấp nhận được tolerances $\epsilon^{pri}$ và $\epsilon^{dual}$, nói $10^{-4}$, và trên cực đại số của vòng lặp các bước, nói $10000$. Có một xây dựng trong Matlab hàm wthresh cài đặt soft thresholding. Bạn có thể sử dụng Matlab command randn đến create ngẫu nhiên dữ liệu tập hợp $X$ và ngẫu nhiên response vectơ $y$ (xem help menu trong Matlab dưới lasso). Thử khác nhau các giá trị của $\rho$ và $\tau$. Bạn sẽ nhận thấy rằng lựa chọn của $\rho$ greatly affects tốc độ của sự hội tụ của quy trình.

<!-- PAGE 1942 -->
