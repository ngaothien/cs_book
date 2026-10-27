# Các bài tập


<!-- PAGE 1965 -->

## 53.6 Các bài tập

Bài toán 53.1. Referring quay lại đến Ví dụ 53.3, chứng minh rằng nếu $\phi_{1}$: $X \to \mathbb{R}_{1}^{n}$ và $\phi_{2}$: $X \to \mathbb{R}_{2}^{n}$ là hai đặc trưng (feature) các ánh xạ và nếu $\kappa_{1} (x, y) = \langle \phi_{1} (x), \phi_{1} (y)\rangle$ và $\kappa_{2} (x, y) = \langle \phi_{2} (x), \phi_{2} (y)\rangle$ là tương ứng hạt nhân (kernel) các hàm, thì ánh xạ được định nghĩa bởi
$$\kappa (x, y) = \kappa_{1} (x, y)\kappa_{2} (x, y)$$
$$\mathbb{R}_{1}^{n} \times \mathbb{R}_{2}^{n}$$
Là hạt nhân (kernel) hàm, cho đặc trưng (feature) không gian và đặc trưng (feature) ánh xạ
$$\phi (x)_{(i,j)} = (\phi_{1} (x))_{i}(\phi_{2} (x))_{j},1 \le i \le n_{1}, 1 \le j \le n_{2}.$$
Bài toán 53.2. Referring quay lại đến Ví dụ 53.3, chứng minh rằng đặc trưng (feature) phép nhúng (embedding) $\phi$: $X \to \mathbb{R}(_{m}^{n+m-1})$
$$given by$$
$$1/2$$
$$\phi_{(i1,...,in)} (x) = \begin{pmatrix} m \\ i_{1} \cdots  i_{n} \end{pmatrix} (\phi_{1} (x))_{1}^{i1} (\phi_{1} (x))_{1}^{i2} \cdots  (\phi_{1} (x))_{1}^{in} ,i_{1} + i_{2} + \cdots  + i_{n} = m, i_{j} \in \mathbb{N},$$
Ở đâu các bộ $n$ $(i_{1}, \dots  , i_{n})$ được thứ tự lexicographically, định nghĩa hạt nhân (kernel) hàm $\kappa$ cho trước bởi $\kappa (x, y) = (\kappa_{1} (x, y))^{m}$.
Bài toán 53.3. Trong Ví dụ 53.6, chứng minh rằng với mọi hai các tập con $A_{1}$ và $A_{2}$ của $D$,
$$\langle \phi (A_{1}), \phi (A_{2})\rangle = 2^{|A1\cap A2|},$$
Số của chung/phổ biến các tập con của $A_{1}$ và $A_{2}$.
Bài toán 53.4. Chứng minh rằng từng điểm giới hạn của các nhân xác định dương là cũng nhân xác định dương (positive definite kernel).
Bài toán 53.5. Chứng minh rằng nếu $\kappa_{1}$ là nhân xác định dương (positive definite kernel), thì
$$\kappa (x, y) =\overline{e}_{2\sigma}^{-\kappa1(x,x)+\kappa1(y,y2)-2\kappa1(x,y)}$$
Là nhân xác định dương (positive definite kernel).

<!-- PAGE 1966 -->
