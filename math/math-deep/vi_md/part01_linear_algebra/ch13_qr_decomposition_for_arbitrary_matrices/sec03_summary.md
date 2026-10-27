# Tóm tắt


<!-- PAGE 522 -->

## 13.3 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ Tính đối xứng (hoặc phép đối xứng (reflection)) đối với $F$ và song song đến $G. \bullet$ Trực giao tính đối xứng (hoặc phép đối xứng (reflection)) đối với $F$ và song song đến $G$; các phép đối xứng, flips. $\bullet$ Siêu phẳng (hyperplane) các phép đối xứng và Householder các ma trận. $\bullet  A$ then chốt sự kiện về các phép đối xứng (Mệnh đề 13.2). $\bullet$ Phân rã QR (QR-decomposition) theo Householder các phép biến đổi (Định lý 13.4).

## 13.4 Các bài tập

Bài toán 13.1. $(1)$ Cho trước unit vectơ (-sin $\theta$, cos $\theta$), chứng minh rằng Ma trận Householder được xác định bởi vectơ (-sin $\theta$, cos $\theta$) là
$$\begin{pmatrix} \cos 2\theta & \sin 2\theta \\ \sin 2\theta & -\cos 2\theta \end{pmatrix} .$$
Cho hình học interpretation (i.e., tại sao lựa chọn (-sin $\theta$, cos $\theta$)?).
$(2)$ Cho trước bất kỳ ma trận
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} ,$$
Chứng minh rằng có một Ma trận Householder $H$ sao cho $AH$ là tam giác dưới (lower triangular), i.e.,
$$AH = \begin{pmatrix} a' & 0 \\ c' & d' \end{pmatrix}$$
$$\mathbb{R}$$
Với một số ', c', d' $\in$.
Bài toán 13.2. Cho trước Không gian Euclid (Euclidean space) $E$ có số chiều $n$, nếu $h$ là phép đối xứng (reflection) về một số siêu phẳng (hyperplane) trực giao đến khác không vectơ $u$ và $f$ là bất kỳ phép đẳng cự (isometry), chứng minh rằng $f \circ h \circ f^{-1}$ là phép đối xứng (reflection) về siêu phẳng (hyperplane) trực giao đến f(u).
Bài toán 13.3. $(1)$ Cho trước ma trận
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} ,$$
Chứng minh rằng có Householder các ma trận $G, H$ sao cho
$$GAH = \begin{pmatrix} \cos \theta & \sin \theta \\ \sin \theta & -\cos \theta \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix} = D,$$
