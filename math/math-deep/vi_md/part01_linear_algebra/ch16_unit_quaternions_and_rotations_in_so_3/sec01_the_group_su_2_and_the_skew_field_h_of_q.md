# Nhóm SU(2) và Skew Trường H của Các quaternion


<!-- PAGE 601 -->
Chương $16$ Các quaternion đơn vị và Các phép quay trong Do đó(3) Điều này chương là devoted đến biểu diễn của các phép quay trong Do đó(3) theo các quaternion đơn vị. Vì ta đã được định nghĩa unita các nhóm SU(n), quickest cách đến giới thiệu các quaternion đơn vị là để định nghĩa chúng như các phần tử của nhóm SU(2). skew $field\mathbb{H}$ của các quaternion và nhóm SU(2) của các quaternion đơn vị được thảo luận trong Mục 16.1. Trong Mục 16.2, ta định nghĩa đồng cấu $r$: SU(2) $\to$ Do đó(3) và chứng minh rằng hạt nhân (hạt nhân (kernel)) của nó là ${-I, I}$. Ta tính ma trận quay (rotation matrix) $R_{q}$ liên kết với phép quay $r_{q}$ được cảm sinh bởi quaternion đơn vị (unit quaternion) $q$ trong Mục 16.3. Trong Mục 16.4, ta chứng minh rằng đồng cấu $r$: SU(2) $\to$ Do đó(3) là toàn ánh (surjective) bởi providing thuật toán để xây dựng quaternion từ ma trận quay (rotation matrix). Trong Mục 16.5 ta định nghĩa hàm mũ ánh xạ exp: $\mathfrak{su}(2) \to$ SU(2) ở đâu $\mathfrak{su}(2)$ là thực không gian vectơ (vector space) của skew-Hermitian $2 \times  2$ các ma trận với không vết (trace). Ta chứng minh rằng hàm mũ ánh xạ exp: $\mathfrak{su}(2) \to$ SU(2) là toàn ánh (surjective) và cho thuật toán cho việc tìm lôgarit. Ta thảo luận quaternion nội suy và chứng minh nổi tiếng slerp nội suy công thức do Ken Shoemake trong Mục 16.6. công thức này được sử dụng trong rô-bốt học và máy tính đồ họa đến deal với nội suy các bài tập. Trong Mục 16.7, ta chứng minh rằng không có “đẹp” mục $s$: Do đó(3) $\to$ SU(2) của đồng cấu $r$: SU(2) $\to$ Do đó(3), trong nghĩa rằng bất kỳ mục của $r$ là không đồng cấu cũng không liên tục.

## 16.1 Nhóm SU(2) của Các quaternion đơn vị và

$$\mathbb{H}$$
$$Skew Field of Quaternions$$

> **Định nghĩa 16.1.** các quaternion đơn vị là các phần tử của nhóm SU(2), cụ thể là nhóm của $2 \times  2$ phức các ma trận của tạo thành
$$\begin{pmatrix} \alpha & \beta \\ -\beta & \overline{\alpha} \end{pmatrix} \alpha , \beta  \in \mathbb{C}, \overline{\alpha \alpha} +\overline{\beta \beta} = 1.$$
Các quaternion là các phần tử của thực không gian vectơ (vector space) $\mathbb{H} =\mathbb{R}$ SU(2).
$$601$$

<!-- PAGE 602 -->
Cho $1, i, j, k$ là các ma trận
$$1 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} ,i = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix} ,j = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} ,k = \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix} ,$$
Thì $\mathbb{H}$ là tập hợp tất cả các ma trận của tạo thành
$$X = a1 + bi + cj + dk,a, b, c, d \in \mathbb{R}.$$
Thật vậy, mọi ma trận trong $\mathbb{H}$ là của tạo thành
$$X = \begin{pmatrix} a + ib & c + id \\ -(c -id) & a -ib \end{pmatrix} ,a, b, c, d \in \mathbb{R}.$$
Nó là dễ (nhưng bit tẻ nhạt/dài dòng) để kiểm chứng rằng các quaternion $1, i, j, k$ thỏa mãn nổi tiếng các đồng nhất thức discovered bởi Hamilton:
$$i^{2}= j^{2}= k^{2}= ijk = -1,$$
$$ij = -ji = k,$$
$$jk = -kj = i,$$
$$ki = -ik = j.$$
Do đó, các quaternion là tổng quát hóa của phức các số, nhưng có ba square các nghiệm của $-1$ và phép nhân là không giao hoán. Cho trước bất kỳ hai các quaternion $X = a1+bi+cj+dk$ và $Y = a'1+b'i+c'j+d'k$, Hamilton’s nổi tiếng công thức
$$XY = (aa'-bb'-cc'-dd')1 + (ab'+ ba'+ cd'-dc')i$$
$$+ (ac'+ ca'+ db'-bd')j + (ad'+ da'+ bc'-cb')k$$
Trông mysterious, nhưng nó là đơn giản kết quả của nhân hai các ma trận
$$X = \begin{pmatrix} a + ib & c + id \\ -(c -id) & a -ib \end{pmatrix} andY = \begin{pmatrix} a' + ib' & c'+ id' \\ -(c'-id') & a'-ib' \end{pmatrix} .$$
Nó là worth không rằng công thức này đã là discovered một cách độc lập bởi Olinde Rodrigues trong $1840$, một vài years trước Hamilton (Veblen và Young $[190])$. Tuy nhiên, Rodrigues đã là làm việc với khác nhau formalism, thuần nhất các phép biến đổi, và he đã thực hiện không discover các quaternion. Nếu
$$X = \begin{pmatrix} a + ib & c + id \\ -(c -id) & a -ib \end{pmatrix} ,a, b, c, d \in \mathbb{R},$$
Ta kiểm chứng được ngay rằng
$$XX^{*}= X^{*}X = (a^{2}+ b^{2}+ c^{2}+ d^{2})1.$$
