# Giới thiệu đến Tín hiệu Compression Bằng cách sử dụng Wavelet Haar (Haar wavelets)


<!-- PAGE 153 -->
Chương $5$ Các cơ sở Haar, Wavelet Haar (Haar wavelets), Các ma trận Hadamard Trong chương này, ta thảo luận hai các loại của các ma trận rằng có các ứng dụng trong máy tính khoa học và kỹ thuật:
$(1)$ Haar các ma trận và tương ứng Wavelet Haar (Haar wavelets), cơ bản công cụ trong tín hiệu processing và máy tính đồ họa. $2)$ Các ma trận Hadamard mà có các ứng dụng trong sai số đúng codes, tín hiệu processing, và thấp hạng (rank) xấp xỉ.

## 5.1 Giới thiệu đến Tín hiệu Compression Bằng cách sử dụng Haar

$$Wavelets$$
Ta bắt đầu bởi xét Wavelet Haar (Haar wavelets) trong $\mathbb{R}^{4}$. Wavelets đóng quan trọng vai trò trong audio và video tín hiệu processing, especially cho compressing dài các tín hiệu vào nhiều nhỏ hơn các một rằng vẫn retain đủ information sao cho khi chúng được đóng, ta có thể’t xem hoặc hear bất kỳ difference. Xét bốn các vectơ $w_{1}, w_{2}, w_{3}, w_{4}$ cho trước bởi
$$w_{1} = \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \end{pmatrix} w_{2} = \begin{pmatrix} 1 \\ 1 \\ -1 \\ 1 \end{pmatrix} w_{3} = \begin{pmatrix} 1 \\ -1 \\ 0 \\ 0 \end{pmatrix} w_{4} = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 1 \end{pmatrix} .$$
$$--$$
Lưu ý rằng các vectơ này là đôi một trực giao, mà có nghĩa là của chúng tích vô hướng (inner product) là $0$ (xem Mục 12.1, Ví dụ 12.1, và Mục 12.2, Định nghĩa 12.2), do đó chúng là thật vậy độc lập tuyến tính (linearly independent) (xem Mệnh đề 12.4). Cho $\mathcal{W} = {w_{1}, w_{2}, w_{3}, w_{4}}$ là Cơ sở Haar (Haar basis), và cho
$$153$$

<!-- PAGE 154 -->
$\mathcal{U} = {e_{1}, e_{2}, e_{3}, e_{4}}$ là cơ sở chính tắc (canonical basis) $of\mathbb{R}^{4}$. ma trận chuyển cơ sở (change of basis matrix) $W = P_{W,U}$ từ $\mathcal{U}$ đến $\mathcal{W}$ được cho bởi
$$W = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 1 & -1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & 0 & 1 \end{pmatrix} ,$$
$$--$$
Và ta dễ dàng tìm rằng nghịch đảo của $W$ được cho bởi
$$W^{-1}  = \begin{pmatrix} 1/4 & 0 & 0 & 0 \\ 0 & 1/4 & 0 & 0 \\ 0 & 0 & 1/2 & 0 \\ 0 & 0 & 0 & 1/2 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & -1 & -1 \\ 1 & -1 & 0 & 0 \\ 0 & 0 & 1 & 1 \end{pmatrix} .$$
$$-$$
Nhận thấy rằng thứ hai ma trận trong ở trên tích là $W^{\top}$ và thứ nhất ma trận trong tích này là $(W^{\top} W)^{-1}$. Do đó vectơ $v = (6, 4, 5, 1)$ trên $basis\mathcal{U}$ trở thành $c = (c_{1}, c_{2}, c_{3}, c_{4})$ trên Cơ sở Haar (Haar basis) $\mathcal{W}$, với
$$\begin{pmatrix} c_{1} \\ c_{2} \\ c_{3} \\ c_{4} \end{pmatrix} = \begin{pmatrix} 1/4 & 0 & 0 & 0 \\ 0 & 1/4 & 0 & 0 \\ 0 & 0 & 1/2 & 0 \\ 0 & 0 & 0 & 1/2 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & -1 & -1 \\ 1 & -1 & 0 & 0 \\ 0 & 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 6 \\ 4 \\ 5 \\ 1 \end{pmatrix} = \begin{pmatrix} 4 \\ 1 \\ 1 \\ 2 \end{pmatrix} .$$
$$-$$
Cho trước tín hiệu $v = (v_{1}, v_{2}, v_{3}, v_{4})$, ta thứ nhất biến đổi $v$ vào của nó các hệ số $c = (c_{1}, c_{2}, c_{3}, c_{4})$ trên Cơ sở Haar (Haar basis) bởi việc tính toán $c = W^{-1} v$. Nhận thấy rằng
$$c_{1} = \frac{v_{1} + v_{2} + v_{3} + v_{4}}{4}$$
Là overall trung bình giá trị của tín hiệu $v$. hệ số $c_{1}$ tương ứng với kiến thức nền tảng của ảnh (image) (hoặc của sound). Thì, $c_{2}$ cho coarse chi tiết của $v$, trong khi đó, $c_{3}$ cho chi tiết trong phần thứ nhất của $v$, và $c_{4}$ cho chi tiết trong thứ hai một nửa của $v$. Reconstruction của tín hiệu bao gồm trong việc tính toán $v =$ Wc. mẹo/kỹ thuật cho tốt compression là đến throw away một số của các hệ số của $c$ (tập hợp chúng đến không), thu được compressed tín hiệu $c$, và vẫn retain đủ then chốt information sao cho reconstructed tín hiệu $v =$ Wc $b  b b$ trông hầu như như tốt như ban đầu tín hiệu $v$. Do đó, các bước là: input $v \longrightarrow$ các hệ số $c = W^{-1} v \longrightarrow$ compressed $c \longrightarrow$ compressed $v =$ Wc.
$$b bb$$
Điều này loại của compression scheme làm cho hiện đại video conferencing khả dĩ/có thể. Hóa ra là có một faster cách để tìm $c = W^{-1} v$, mà không có thực sự bằng cách sử dụng $W^{-1}$. Điều này có đến thực hiện với multiscale nature của Wavelet Haar (Haar wavelets). Cho trước ban đầu tín hiệu $v = (6, 4, 5, 1)$ được hiển thị trong Hình 5.1, ta tính các trung bình và một nửa differences thu được Hình 5.2. Ta thu được các hệ số $c_{3} = 1$ và $c_{4} = 2$. Thì
