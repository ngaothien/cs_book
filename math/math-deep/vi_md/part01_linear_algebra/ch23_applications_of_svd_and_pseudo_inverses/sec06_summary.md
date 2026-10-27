# Tóm tắt


<!-- PAGE 798 -->
Và
$$V D = \begin{pmatrix} 51.4683 & 3.3013 & -3.8569 \\ -9.9623 & -6.6467 & -2.7082 \\ 76.6327 & 3.1845 & 0.2348 \\ 2.2393 & -8.6943 & 5.2872 \\ -33.6038 & 4.1334 & -3.6415 \\ -25.5941 & 1.3833 & -0.4350 \\ -53.4333 & 7.2258 & -1.3547 \\ -13.0100 & 6.8594 & 4.2010 \\ -6.2843 & 4.6254 & 4.3212 \\ 15.2173 & 14.3266 & 1.1581 \end{pmatrix} , X -\mu  = \begin{pmatrix} -1.2000 & -51.4000 & -5.6000 \\ -4.2000 & 9.6000 & 6.4000 \\ 3.8000 & -76.4000 & -5.6000 \\ 3.8000 & -2.4000 & 9.4000 \\ -4.2000 & 33.6000 & -3.6000 \\ -1.2000 & 25.6000 & -0.6000 \\ -2.2000 & 53.6000 & -5.6000 \\ 4.8000 & 13.4000 & -5.6000 \\ 4.8000 & 6.6000 & -3.6000 \\ 4.2000 & 14.6000 & 14.4000 \end{pmatrix} .$$
$$----$$
Thứ nhất chính hướng $u_{1} =$ (0.0394, -0.9987, -0.0327) là basically opposite của trục $y$, và hầu hết đáng kể đặc trưng (feature) là year của birth. thứ hai chính hướng $u_{2} =$ (0.1717, 0.0390, -0.9844) là close đến opposite của trục $z$, và thứ hai hầu hết đáng kể đặc trưng (feature) là lenght của beards. tốt nhất afin mặt phẳng được sinh (spanned) bởi các vectơ $u_{1}$ và $u_{2}$. Có nhiều các ứng dụng của PCA đến dữ liệu compression, số chiều reduction, và pattern giải tích/phân tích. cơ bản ý tưởng là rằng trong nhiều các trường hợp, cho trước dữ liệu tập hợp $X_{1}, \dots  , X_{n}$, với $X_{i} \in \mathbb{R}^{d}$, chỉ “nhỏ” tập con của $m < d$ của các đặc trưng là cần thiết đến mô tả dữ liệu tập hợp accurately. Nếu $u_{1}, \dots  , u_{d}$ là chính các hướng của $X -\mu$, thì thứ nhất $m$ các phép chiếu của dữ liệu (thứ nhất $m$ chính các thành phần, i.e., thứ nhất $m$ các cột của $V D)$ lên thứ nhất $m$ chính các hướng biểu diễn dữ liệu mà không có nhiều mất mát (loss) của information. Do đó, thay vì của bằng cách sử dụng ban đầu dữ liệu các điểm $X_{1}, \dots  , X_{n}$, với $X_{i} \in \mathbb{R}^{d}$, ta có thể sử dụng của chúng các phép chiếu lên thứ nhất $m$
$$\mathbb{R}^{m}$$
Chính các hướng $Y_{1}, \dots  , Y_{m}$, ở đâu $Y_{i} \in$ và $m < d$, thu được compressed phiên bản của ban đầu dữ liệu tập hợp. Ví dụ, PCA được sử dụng trong máy tính thị giác cho mặt recognition. Sirovitch và Kirby
$(1987)$ dường như là thứ nhất đến có đã có ý tưởng của bằng cách sử dụng PCA đến compress facial các ảnh. Chúng đã giới thiệu số hạng eigenpicture đến refer đến chính các hướng, $u_{i}$. Tuy nhiên, tường minh mặt recognition thuật toán đã là cho trước chỉ sau này bởi Turk và Pentland $(1991)$. Chúng renamed eigenpictures như eigenfaces. Cho chi tiết trên topic của eigenfaces, xem Forsyth và Ponce $[65]$ (Chương $22$, Mục 22.3.2), ở đâu bạn sẽ cũng tìm chính xác references đến Turk và Pentland’s papers. Một cái khác thú vị ứng dụng của PCA là đến recognition của handwritten digits. Như vậy ứng dụng được mô tả trong Hastie, Tibshirani, và Friedman, $[91]$ (Chương $14$, Mục 14.5.1).

## 23.6 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới:
