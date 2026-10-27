# GMRES


<!-- PAGE 684 -->
Tuy nhiên, nếu $A$ là đối xứng (hoặc Hermite) ma trận, thì $H_{n}$ là đối xứng (resp. Hermite) ma trận ba đường chéo (tridiagonal matrix) và nhiều hơn/thêm precise các kết quả có thể được được hiển thị; xem Demmel $[48]$ (Chương $7$, especially Mục 7.2). Ta sẽ xét đối xứng (và Hermitan) trường hợp trong mục tiếp theo, nhưng thứ nhất ta chỉ ra cách mà Phép lặp Arnoldi (Arnoldi iteration) có thể được được sử dụng để tìm các xấp xỉ cho nghiệm của hệ phương trình tuyến tính Ax $= b$ ở đâu $A$ là khả nghịch nhưng của rất lớn số chiều $m$.

## 18.5 GMRES

Giả sử $A$ là khả nghịch $m\times m$ ma trận và cho $b$ là khác không vectơ $in\mathbb{C}^{m}$. Cho $x_{0} = A^{-1}b$, duy nhất nghiệm của Ax $= b$. Nó là không khó để chỉ ra rằng $x_{0} \in K_{n}(A, b)$ với một số $n \le m$. Thực ra, tồn tại duy nhất một chuẩn hóa (monic) đa thức p(z) của tối tiểu bậc $s \le m$ sao cho p()b $= 0$, do đó $x_{0} \in K_{s}(A, b)$. Do đó nó làm cho nghĩa đến search cho nghiệm của Ax $= b$ trong Krylov các không gian có số chiều $m \le s$. ý tưởng là để tìm xấp xỉ $x_{n} \in K_{n}(A, b)$ của $x_{0}$ sao cho $r_{n} = b$ - $Ax_{n}$ được cực tiểu hóa, nghĩa là, $\|r_{n}\|_{2} = \|b$ - $Ax_{n}\|_{2}$ được cực tiểu hóa trên $x_{n} \in K_{n}(A, b)$. Điều này cực tiểu hóa bài toán có thể được được phát biểu như
$$minimize\|r_{n}\|_{2} = \|Ax_{n} -b\|_{2} ,x_{n} \in K_{n}(A, b).$$
Điều này là bình phương tối thiểu (least-squares) bài toán, và ta biết cách mà để giải nó (xem Mục 23.1). đại lượng $r_{n}$ là đã biết như phần dư (residual) và phương pháp mà bao gồm trong cực tiểu hóa $\|r_{n}\|_{2}$ là đã biết như GMRES, cho suy rộng/tổng quát hóa tối tiểu các phần dư. Bây giờ vì $(u_{1}, \dots  , u_{n})$ là cơ sở (basis) của $\mathcal{K}_{n}(A, b)$ (vì $n \le s$, không có breakdown xảy ra, ngoại trừ cho $n = s)$, ta có thể viết $x_{n} = U_{n}y$, do đó của ta cực tiểu hóa bài toán là
$$minimize\|AU_{n}y -b\|_{2} ,y \in \mathbb{C}^{n}.$$
Vì bởi $(*_{1})$ của Mục 18.4, ta có $AU_{n} = U_{n+1}H_{n}$, cực tiểu hóa $\|AU_{n}y$ - $b\|_{2}$ là equiv-
$$e$$
$$\mathbb{C}^{m}$$
Alent đến cực tiểu hóa $\|U_{n+1}H_{n}y$ - $b\|_{2}$ trên. Vì $U_{n+1}H_{n}y$ và $b$ thuộc đến cột
$$ee$$
Không gian của $U_{n+1}$, cực tiểu hóa $\|U_{n+1}H_{n}y$ - $b\|_{2}$ là tương đương đến cực tiểu hóa $\|H_{n}y$ - $U_{n+1}^{*} b\|_{2}$.
$$ee$$
Tuy nhiên, bởi cách xây dựng,
$$U_{n+1}^{*} b = \|b\|_{2}e_{1} \in \mathbb{C}^{n+1},$$
Do đó của ta cực tiểu hóa bài toán có thể được được phát biểu như
$$minimize\|H_{n}y -\|b\|_{2}e_{1}\|_{2},y \in \mathbb{C}^{n}.$$
$$e$$
Xấp xỉ nghiệm của Ax $= b$ là thì
$$x_{n} = U_{n}y.$$
Bắt đầu với $u_{1} = b/ \|b\|_{2}$ và với $n = 1$, GMRES phương pháp chạy $n \le s$ Arnoldi các vòng lặp để tìm $U_{n}$ và $H_{n}$, và thì chạy phương pháp để giải bình phương tối thiểu (least squares) bài toán
$$e$$
$$minimize\|H_{n}y -\|b\|_{2}e_{1}\|_{2},y \in \mathbb{C}^{n}.$$
$$e$$
