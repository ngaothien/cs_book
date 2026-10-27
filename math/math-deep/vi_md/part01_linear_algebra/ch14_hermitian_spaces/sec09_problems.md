# Các bài tập


<!-- PAGE 564 -->

## 14.9 Các bài tập

Bài toán 14.1. Cho $(E, \langle$ -, $-\rangle$) là Không gian Hermite (Hermitian space) của hữu hạn số chiều. Chứng minh rằng nếu $f$: $E \to E$ là tự liên hợp (self-adjoint) ánh xạ tuyến tính (linear map) (rằng là, $f^{*} = f)$, thì $\langle$ f(x), $x\rangle \in \mathbb{R}$ với mọi $x \in E$.
Bài toán 14.2. Chứng minh phân cực các đồng nhất thức của Mệnh đề 14.1.
Bài toán 14.3. Cho $E$ là thực Không gian Euclid (Euclidean space). Cho ví dụ của khác không ánh xạ tuyến tính (linear map) $f$: $E \to E$ sao cho $\langle$ f(u), $u\rangle = 0$ với mọi $u \in E$.
Bài toán 14.4. Chứng minh Mệnh đề 14.9.
Bài toán 14.5. $(1)$ Chứng minh rằng mọi ma trận trong SU(2) là của tạo thành
$$\mathbb{R}$$
$$A = \begin{pmatrix} a + ib & c + id \\ -c + id & a -ib \end{pmatrix} ,a^{2}+ b^{2}+ c^{2}+ d^{2}= 1, a, b, c, d \in ,$$
$(2)$ Chứng minh rằng các ma trận
$$\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} , \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix} , \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} , \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}$$
Tất cả thuộc đến SU(2) và là độc lập tuyến tính (linearly independent) trên $\mathbb{C}$.
$(3)$ Chứng minh rằng tuyến tính sinh (span) của SU(2) trên $\mathbb{C}$ là phức không gian vectơ (vector space) $M_{2}(\mathbb{C})$ của tất cả phức $2 \times  2$ các ma trận.
Bài toán 14.6. mục đích của bài toán này là để chứng minh rằng tuyến tính sinh (span) của SU(n) trên $\mathbb{C}$ là $M_{n}(\mathbb{C})$ với mọi $n \ge 3$. Một cách để chứng minh kết quả này là đến thích nghi phương pháp của Bài toán 12.12, do đó please ôn tập/tổng quan bài toán này. Mọi phức ma trận $A \in M_{n}(\mathbb{C})$ có thể được viết dưới dạng
$$-$$
$$A = \frac{A + A^{*}}{2} + \frac{AA^{*}}{2}$$
Ở đâu thứ nhất ma trận là Hermite và thứ hai ma trận là skew-Hermitian. Nhận thấy rằng nếu $A = (z_{ij})$ là Ma trận Hermite (Hermitian matrix), nghĩa là $A^{*} = A$, thì $z_{ji} = \overline{z}_{ij}$, do đó nếu $z_{ij} = a_{ij} + ib_{ij}$ với $a_{ij}, b_{ij} \in \mathbb{R}$, thì $a_{ij} = a_{ji}$ và $b_{ij} = -b_{ji}$. Mặt khác, nếu $A = (z_{ij})$ là ma trận phản Hermite (skew-Hermitian matrix), nghĩa là $A^{*} = -A$, thì $z_{ji} = -\overline{z}_{ij}$, do đó $a_{ij} = -a_{ji}$ và $b_{ij} = b_{ji}$. Hermite và skew-Các ma trận Hermite thực hiện không tạo thành phức các không gian vectơ bởi vì chúng là không đóng dưới phép nhân bởi phức số, nhưng ta có thể thu được xung quanh bài toán này bởi treating thực phần và phức phần của các ma trận này một cách tách và bằng cách sử dụng phép nhân bởi các số thực.

<!-- PAGE 565 -->
$(1)$ Xét các ma trận của tạo thành
$$R_{c}^{i,j} = \begin{pmatrix} 1 \\ \ddots \\ 1 \\ 0 & 0 & \cdots & 0 & i \\ 0 & 1 & \cdots & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & 1 & 0 \\ i & 0 & \cdots & 0 & 0 \\ 1 \\ \ddots \\ 1 \end{pmatrix} .$$
Chứng minh rằng $(R_{c}^{i,j} )^{*}R_{c}^{i,j} =$ I và $det(R_{c}^{i,j}$) $= +1$. Sử dụng các ma trận $R^{i,j}, R_{c}^{i,j} \in$ SU(n) và các ma trận $(R^{i,j}-(R^{i,j})^{*})/2$ (từ Bài toán 12.12) đến tạo thành thực phần của ma trận phản Hermite (skew-Hermitian matrix) và các ma trận $(R_{c}^{i,j}$ - $(R_{c}^{i,j} )^{*})/2$ đến tạo thành imaginary phần của ma trận phản Hermite (skew-Hermitian matrix). Suy ra rằng các ma trận trong SU(n) sinh (span) tất cả skew-Các ma trận Hermite.
$(2)$ Xét các ma trận của tạo thành Loại/kiểu $1$
$$S_{c}^{1,2}= \begin{pmatrix} 0 & -i & 0 & 0 & \dots & 0 \\ i & 0 & 0 & 0 & \dots & 0 \\ 0 & 0 & -1 & 0 & \dots & 0 \\ 0 & 0 & 0 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & 0 & \dots & 1 \end{pmatrix} .$$
Loại/kiểu $2$
$$S_{c}^{i,i+1}= \begin{pmatrix} -1 \\ 1 \\ \ddots \\ 1 \\ 0 & -i \\ i & 0 \\ 1 \\ \ddots \\ 1 \end{pmatrix} .$$

<!-- PAGE 566 -->
Loại/kiểu $3$
$$S_{c}^{i,j}= \begin{pmatrix} 1 \\ \ddots \\ 1 \\ 0 & 0 & \cdots & 0 & -i \\ 0 & -1 & \cdots & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & 1 & 0 \\ i & 0 & \cdots & 0 & 0 \\ 1 \\ \ddots \\ 1 \end{pmatrix} .$$
Chứng minh rằng $S^{i,j}, S_{c}^{i,j} \in$ SU(n), và bằng cách sử dụng các ma trận đường chéo như trong Bài toán 12.12, chứng minh rằng các ma trận $S^{i,j}$ có thể được sử dụng để tạo thành thực phần của Ma trận Hermite (Hermitian matrix) và các ma trận $S_{c}^{i,j}$ có thể được sử dụng để tạo thành imaginary phần của Ma trận Hermite (Hermitian matrix).
$(3)$ Sử dụng $(1)$ và $(2)$ để chứng minh rằng các ma trận trong SU(n) sinh (span) tất cả Các ma trận Hermite. Suy ra rằng SU(n) sinh ra $M_{n}(\mathbb{C})$ cho $n \ge 3$.
Bài toán 14.7. Xét phức ma trận
$$A = \begin{pmatrix} i & 1 \\ 1 & -i \end{pmatrix} .$$
Kiểm tra rằng ma trận này là đối xứng nhưng không Hermite. Chứng minh rằng
$$\det(\lambda I -A) = \lambda^{2} ,$$
Và do đó các trị riêng (eigenvalues) của $A$ là $0, 0$.
Bài toán 14.8. Cho $(E, \langle$ -, $-\rangle$) là Không gian Hermite (Hermitian space) của hữu hạn số chiều và cho $f$: $E \to E$ là ánh xạ tuyến tính (linear map). Chứng minh rằng các điều kiện sau đây là tương đương.
$(1) f \circ f^{*} = f^{*} \circ f (f$ là chuẩn tắc/bình thường).
$(2) \langle$ f(x), $f(y)\rangle = \langle f^{*} (x), f^{*} (y)\rangle$ với mọi $x, y \in E$.
$(3) \|f(x)\| = \|f^{*} (x)\|$ với mọi $x \in E$.
$(4)$ ánh xạ $f$ có thể được được chéo hóa đối với cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors).
$(5)$ Ở đó tồn tại một số các ánh xạ tuyến tính (linear maps) $g, h: E \to E$ sao cho, $g = g^{*}, \langle x, g(x)\rangle \ge 0$ với mọi $x \in E, h^{-1} = h^{*}$, và $f = g \circ h = h \circ g$.
$(6)$ Ở đó tồn tại một số ánh xạ tuyến tính (linear map) $h: E \to E$ sao cho $h^{-1} = h^{*}$ và $f^{*} = h \circ f$.

<!-- PAGE 567 -->
$(7)$ Có một đa thức $P$ (với phức các hệ số) sao cho $f^{*} =$ P(f).
Bài toán 14.9. Nhắc lại từ Bài toán 13.7 rằng phức $n\times n$ ma trận $H$ là trên Hessenberg nếu $h_{jk} = 0$ với mọi $(j, k)$ sao cho $j$ - $k \ge 0$. Thích nghi chứng minh của Bài toán 13.7 để chứng minh rằng cho trước bất kỳ phức ma trận cỡ $n \times n$ $A$, có $n$ - $2 \ge 1$ phức các ma trận $H_{1}, \dots  , H_{n-2}$, Householder các ma trận hoặc đồng nhất thức, sao cho
$$B = H_{n-2} \cdots  H_{1}AH_{1} \cdots  H_{n-2}$$
Là trên Hessenberg.
Bài toán 14.10. Chứng minh rằng tất cả $y \in \mathbb{C}^{n}$,
$$\|y\|_{1}^{D} = \|y\|_{\infty}$$
$$\|y\|_{\infty}^{D}= \|y\|_{1}$$
$$\|y\|_{2}^{D} = \|y\|_{2} .$$
Bài toán 14.11. mục đích của bài toán này là đến đầy đủ mỗi của các ma trận $A_{0}, B_{0}, C_{0}$ của Mục 14.7 đến ma trận $A$ trong như vậy cách rằng nuclear chuẩn (norm) $\|A\|_{N}$ được cực tiểu hóa.
$(1)$ Chứng minh rằng squares $\sigma_{1}^{2}$ và $\sigma_{2}^{2}$ của các giá trị kỳ dị (singular values) của
$$A = \begin{pmatrix} 1 & 2 \\ c & d \end{pmatrix}$$
Là các không điểm của phương trình
$$\lambda^{2} -(5 + c^{2}+ d^{2})\lambda  + (2c -d)^{2}= 0.$$
$(2)$ Bằng cách sử dụng sự kiện rằng
$$q$$
$$\|A\|_{N} = \sigma_{1}  + \sigma_{2}  =\sigma_{1}^{2}  + \sigma_{2}^{2}  + 2\sigma_{1} \sigma_{2} ,$$
Chứng minh rằng
$$+ + 2$$
$$\|A\|_{N}^{2} = 5 + c^{2} d^{2}|2c -d|.$$
Xét các trường hợp ở đâu 2c - $d \ge 0$ và 2c - $d \le 0$, và chỉ ra rằng trong cả hai các trường hợp ta phải có $c =$ -2d, và rằng cực tiểu của f(c, $d) = 5 + c^{2} + d^{2} +$ 2|2c - d| là đạt được bởi $c = d = 0$. Kết luận rằng ma trận $A$ completing $A_{0}$ rằng cực tiểu hóa $\|A\|_{N}$ là
$$A = \begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix} .$$
$(3)$ Chứng minh rằng squares $\sigma_{1}^{2}$ và $\sigma_{2}^{2}$ của các giá trị kỳ dị (singular values) của
$$A = \begin{pmatrix} 1 & b \\ c & 4 \end{pmatrix}$$

<!-- PAGE 568 -->
Là các không điểm của phương trình
$$\lambda^{2} -(17 + b^{2}+ c^{2})\lambda  + (4 -bc)^{2}= 0.$$
$(4)$ Chứng minh rằng
$$+ + 2$$
$$\|A\|_{N}^{2} = 17 + b^{2} c^{2}|4 -bc|.$$
Xét các trường hợp ở đâu $4$ - bc $\ge 0$ và $4$ - bc $\le 0$, và chỉ ra rằng trong cả hai các trường hợp ta phải có $b^{2} = c^{2}$. Thì chỉ ra rằng cực tiểu của f(c, $d) = 17+b^{2}+c^{2}+2|4-bc|$ là đạt được bởi $b = c$ với $-2 \le b \le 2$. Kết luận rằng các ma trận $A$ completing $B_{0}$ rằng cực tiểu hóa $\|A\|_{N}$ được cho bởi
$$A = \begin{pmatrix} 1 & b \\ b & 4 \end{pmatrix} ,-2 \le b \le 2.$$
$(5)$ Chứng minh rằng squares $\sigma_{1}^{2}$ và $\sigma_{2}^{2}$ của các giá trị kỳ dị (singular values) của
$$A = \begin{pmatrix} 1 & 2 \\ 3 & d \end{pmatrix}$$
Là các không điểm của phương trình
$$\lambda^{2} -(14 + d^{2})\lambda  + (6 -d)^{2}= 0$$
$(6)$ Chứng minh rằng
$$+ 2$$
$$\|A\|_{N}^{2} = 14 + d^{2}|6 -d|.$$
Xét các trường hợp ở đâu $6$ - $d \ge 0$ và $6$ - $d \le 0$, và chỉ ra rằng cực tiểu của f(c, $d) = 14 + d^{2} +$ 2|6 - d| là đạt được bởi $d = 1$. Kết luận rằng ma trận $A$ completing $C_{0}$ rằng cực tiểu hóa $\|A\|_{N}$ được cho bởi
$$A = \begin{pmatrix} 1 & 2 \\ 3 & 1 \end{pmatrix} .$$
Bài toán 14.12. Chứng minh Định lý 14.32 khi $E$ là hữu hạn chiều Không gian Hermite (Hermitian space).
