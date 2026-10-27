# Các bài tập


<!-- PAGE 799 -->
$\bullet$ Bình phương tối thiểu (least squares) các bài tập. $\bullet$ Sự tồn tại của bình phương tối thiểu (least squares) nghiệm của nhỏ nhất chuẩn (norm) (Định lý 23.1). $\bullet$ nghịch đảo giả (pseudo-inverse) $A^{+}$ của ma trận $A. \bullet$ bình phương tối thiểu (least squares) nghiệm của nhỏ nhất chuẩn (norm) được cho bởi nghịch đảo giả (pseudo-inverse) (Định lý 23.2) $\bullet$ Phép chiếu các tính chất của nghịch đảo giả (pseudo-inverse). $\bullet$ nghịch đảo giả (pseudo-inverse) của ma trận chuẩn tắc (normal matrix). $\bullet$ Penrose đặc trưng của nghịch đảo giả (pseudo-inverse). $\bullet$ Dữ liệu compression và SVD. $\bullet$ Tốt nhất xấp xỉ của hạng (rank) $< r$ của ma trận. $\bullet$ Phân tích thành phần chính (PCA). $\bullet$ Ôn tập/tổng quan của cơ bản statistical các khái niệm: có nghĩa, phương sai, hiệp phương sai, hiệp phương sai ma trận. $\bullet$ được tâm dữ liệu, trọng tâm. $\bullet$ chính các thành phần (PCA). $\bullet$ Rayleigh–Ritz định lý (Định lý 23.10). $\bullet$ chính định lý: SVD cho ta PCA (Định lý 23.11). $\bullet$ Tốt nhất afin xấp xỉ. $\bullet$ SVD cho ta tốt nhất afin xấp xỉ (Định lý 23.12). $\bullet$ Mặt recognition, eigenfaces.

## 23.7 Các bài tập

Bài toán 23.1. Xét quá xác định hệ trong đơn lẻ biến $x$:
$$a_{1}x = b_{1}, \dots  , a_{m}x = b_{m},$$
Với $a_{1}^{2} + \cdots  + a_{m}^{2}$ ̸ $= 0$. Chứng minh rằng bình phương tối thiểu (least squares) nghiệm của nhỏ nhất chuẩn (norm) được cho bởi
$$x^{+} = \frac{a_{1}b_{1} + + a_{m}b_{m}}{a_{1}^{2}+ \cdots  + a_{m}^{2}} \cdots .$$

<!-- PAGE 800 -->
Bài toán 23.2. Cho $X$ là $m \times  n$ thực ma trận. Với mọi chặt dương hằng số $K > 0$, ma trận $X^{\top}X + KI_{n}$ là khả nghịch. Chứng minh rằng giới hạn của ma trận $(X^{\top}X + KI_{n})^{-1}X^{\top}$ khi $K$ đi đến không bằng nghịch đảo giả (pseudo-inverse) $X^{+}$ của $X$.
Bài toán 23.3. Sử dụng Matlab để tìm nghịch đảo giả (pseudo-inverse) của ma trận cỡ $8 \times  6$
$$A = \begin{pmatrix} 64 & 2 & 3 & 61 & 60 & 6 \\ 9 & 55 & 54 & 12 & 13 & 51 \\ 17 & 47 & 46 & 20 & 21 & 43 \\ 40 & 26 & 27 & 37 & 36 & 30 \\ 32 & 34 & 35 & 29 & 28 & 38 \\ 41 & 23 & 22 & 44 & 45 & 19 \\ 49 & 15 & 14 & 52 & 53 & 11 \\ 8 & 58 & 59 & 5 & 4 & 62 \end{pmatrix} .$$
Nhận thấy rằng các tổng của các cột là tất cả bằng $260$. Cho $b$ là vectơ có số chiều $8$ có các tọa độ là tất cả bằng $256$. Tìm nghiệm $x^{+}$ của hệ Ax $= b$.
Bài toán 23.4. mục đích của bài toán này là để chỉ ra rằng Mệnh đề 23.9 (Eckart– Young định lý) cũng nghiệm đúng cho Chuẩn Frobenius (Frobenius norm). bài toán này được điều chỉnh từ Strang $[177]$, Mục I.9. Giả sử ma trận cỡ $m\times n$ $B$ của hạng (rank) nhiều nhất $k$ cực tiểu hóa $\|A$ - $B\|_{F}$. Bắt đầu với SVD của $B$,
$$B = V \begin{pmatrix} D & 0 \\ 0 & 0 \end{pmatrix} U^{\top} ,$$
Ở đâu $D$ là đường chéo $k \times  k$ ma trận. Ta có thể viết
$$A = V \begin{pmatrix} L + E + R & F \\ G & H \end{pmatrix} U^{\top} ,$$
Ở đâu $L$ là chặt tam giác dưới (lower triangular) trong thứ nhất $k$ các hàng, $E$ là đường chéo, và $R$ là chặt tam giác trên (upper triangular), và cho
$$C = V \begin{pmatrix} L + D + R & F \\ 0 & 0 \end{pmatrix} U^{\top} ,$$
Mà rõ ràng có hạng (rank) $\le k$.
$(1)$ Chứng minh rằng
$$\|A -B\|_{F}^{2} = \|A -C\|_{F}^{2} + \|L\|_{F}^{2} + \|R\|_{F}^{2} + \|F\|_{F}^{2} .$$
Vì $\|A$ - $B\|_{F}$ là tối tiểu, chỉ ra rằng $L = R = F = 0$. Tương tự, chỉ ra rằng $G = 0$.

<!-- PAGE 801 -->
$(2)$ Ta có
$$V^{\top} AU = \begin{pmatrix} E & 0 \\ 0 & H \end{pmatrix} ,V^{\top} BU = \begin{pmatrix} D & 0 \\ 0 & 0 \end{pmatrix} ,$$
Ở đâu $E$ là đường chéo, do đó suy ra rằng $1. D = diag(\sigma_{1} , \dots  , \sigma_{k}$). $2$. các giá trị kỳ dị (singular values) của $H$ phải là nhỏ nhất $n$ - $k$ các giá trị kỳ dị (singular values) của $A. 3$. cực tiểu của $\|A$ - $B\|_{F}$ phải là $\|H\|_{F} = (\sigma_{k+1}^{2}  + \cdots  + \sigma_{r}^{2} )^{1/2}$.
Bài toán 23.5. Chứng minh rằng closest hạng (rank) $1$ xấp xỉ (trong $\|\|_{2})$ của ma trận
$$A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix}$$
Là
$$A_{1} = \frac{3}{2} \begin{pmatrix} 1 & 1 \\ 3 & 3 \end{pmatrix} .$$
Chỉ ra rằng Eckart–Young định lý không thỏa mãn cho chuẩn toán tử (operator norm) $\|\|_{\infty}$ bởi việc tìm hạng (rank) $1$ ma trận $B$ sao cho $\|A$ - $B\|_{\infty} < \|A$ - $A_{1}\|_{\infty}$.
Bài toán 23.6. Tìm closest hạng (rank) $1$ xấp xỉ (trong $\|\|_{2})$ cho các ma trận
$$A = \begin{pmatrix} 3 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix} ,A = \begin{pmatrix} 0 & 3 \\ 2 & 0 \end{pmatrix} ,A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} .$$
Bài toán 23.7. Tìm closest hạng (rank) $1$ xấp xỉ (trong $\|\|_{2})$ cho ma trận
$$A = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} .$$
Bài toán 23.8. Cho $S$ là thực đối xứng xác định dương (SPD) ma trận và cho $S = U\Sigma U^{\top}$ là sự chéo hóa của $S$. Chứng minh rằng closest hạng (rank) $1$ ma trận (trong $L^{2}-norm)$ đến $S$ là $u_{1}\sigma_{1} u_{1}^{\top}$, ở đâu $u_{1}$ là cột thứ nhất của $U$.

<!-- PAGE 802 -->
