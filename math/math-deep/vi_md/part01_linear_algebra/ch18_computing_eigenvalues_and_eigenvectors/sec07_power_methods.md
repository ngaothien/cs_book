# Lũy thừa Các phương pháp


<!-- PAGE 686 -->
Của đối xứng (respectively Hermite) ma trận ba đường chéo (tridiagonal matrix) $H_{n}$ áp dụng, nhưng có nhiều hơn/thêm các phương pháp cho việc tìm các trị riêng (eigenvalues) của đối xứng (respectively Hermite) ba đường chéo các ma trận. Cũng các định lý về sai số estimates tồn tại. phiên bản của Phép lặp Lanczos (Lanczos iteration) cho trước ở trên có thể chạy vào các bài tập trong floating điểm arithmetic. Những gì xảy ra là rằng các vectơ $u_{j}$ có thể lose tính chất của đang là trực giao, do đó nó có thể là cần đến reorthogonalize chúng. Cho nhiều hơn/thêm trên tất cả điều này, xem Demmel $[48]$ (Chương $7$, đặc biệt Mục 7.2-7.4). phiên bản của GMRES bằng cách sử dụng Phép lặp Lanczos (Lanczos iteration) được gọi là MINRES. Ta close của ta ngắn gọn survey của các phương pháp cho việc tính toán các trị riêng (eigenvalues) và các vectơ riêng (eigenvectors) của ma trận với quick thảo luận của hai các phương pháp đã biết như lũy thừa các phương pháp.

## 18.7 Lũy thừa Các phương pháp

Cho $A$ là $m \times  m$ phức hoặc thực ma trận. Có hai lũy thừa các phương pháp, cả hai của mà cho một trị riêng (eigenvalue) và một vectơ riêng (eigenvector) liên kết với vectơ này:
$(1)$ Lũy thừa vòng lặp.
$(2)$ Nghịch đảo (lũy thừa) vòng lặp. Lũy thừa vòng lặp chỉ hoạt động nếu ma trận $A$ có trị riêng (eigenvalue) $\lambda$ của lớn nhất môđun/độ lớn, mà có nghĩa là nếu $\lambda_{1} , \dots  , \lambda_{m}$ là các trị riêng (eigenvalues) của $A$, thì
$$|\lambda_{1} | > |\lambda_{2} | \ge \cdots  \ge |\lambda_{m} | \ge 0.$$
Đặc biệt, nếu $A$ là thực ma trận, thì $\lambda_{1}$ phải là thực (vì ngược lại có hai phức liên hợp các trị riêng (eigenvalues) của cùng lớn nhất môđun/độ lớn). Nếu ở trên điều kiện được thỏa mãn, thì lũy thừa vòng lặp cho ta $\lambda_{1}$ và một số vectơ riêng (eigenvector) liên kết với nó. phương pháp là đơn giản đủ: Chọn một số ban đầu unit vectơ $x^{0}$ và tính sau đây dãy $(x^{k})$, ở đâu
$$x^{k+1}= \frac{Ax^{k}}{\|Ax^{k}\|} ,k \ge 0.$$
Ta sẽ kỳ vọng rằng $(x^{k})$ hội tụ đến vectơ riêng (eigenvector) liên kết với $\lambda_{1}$, nhưng điều này là không khá đúng. sau đây các kết quả được chứng minh trong Serre $[162]$ (Mục 13.5.1). Thứ nhất giả sử rằng $\lambda_{1}  \neq  0$. Ta có
$$lim

$Ax^{k}$

$= |\lambda_{1}$ |.$$
$$k\mapsto \infty$$
Nếu $A$ là phức ma trận mà có duy nhất phức trị riêng (eigenvalue) $\lambda_{1}$ của lớn nhất môđun/độ lớn, thì
$$k$$
$$v = klim\mapsto \infty \begin{pmatrix} \overline{\lambda}_{1} \\ |\lambda_{1} | \end{pmatrix} x^{k}$$

<!-- PAGE 687 -->
Là unit vectơ riêng (eigenvector) của $A$ liên kết với $\lambda_{1}$. Nếu $\lambda_{1}$ là thực, thì
$$v = limx^{k}$$
$$k\mapsto \infty$$
Là unit vectơ riêng (eigenvector) của $A$ liên kết với $\lambda_{1}$. Thực sự một số điều kiện trên $x^{0}$ là cần thiết: $x^{0}$ phải có khác không thành phần trong không gian riêng (eigenspace) $E$ liên kết với $\lambda_{1}$ (trong bất kỳ tổng trực tiếp (direct sum) $\mathbb{C}^{m}$ của trong mà $E$ là summand). trị riêng (eigenvalue) $\lambda_{1}$ là tìm thấy như sau. Nếu $\lambda_{1}$ là phức, và nếu $v_{j}$ ̸ $= 0$ là bất kỳ khác không tọa độ của $v$, thì
$$\lambda_{1}  = klim\mapsto \infty \frac{(Ax^{k})_{j}}{x_{j}^{k}} .$$
Nếu $\lambda_{1}$ là thực, thì ta có thể định nghĩa dãy $(\lambda^{(k)}$) bởi
$$\lambda^{(k+1)} = (x^{k+1})^{*}Ax^{k+1},k \ge 0,$$
Và ta có
$$\lambda_{1}  = lim\lambda^{(k)} .$$
$$k\mapsto \infty$$
Thật vậy, trong trường hợp này, vì $v = lim_{k\mapsto \infty} x^{k}$ và $v$ là unit vectơ riêng (eigenvector) cho $\lambda_{1}$, ta có
$$lim\lambda^{(k)} = lim(x^{k+1})^{*}Ax^{k+1}= v^{*}Av = \lambda_{1} v^{*}v = \lambda_{1} .$$
$$k\mapsto \infty k\mapsto \infty$$
Lưu ý rằng vì $x^{k+1}$ là unit vectơ, $(x^{k+1})^{*}Ax^{k+1}$ là Rayleigh tỉ số. Nếu $A$ là Ma trận Hermite (Hermitian matrix), thì các trị riêng (eigenvalues) là thực và ta có thể nói nhiều hơn/thêm về tốc độ của sự hội tụ, mà là không great (chỉ tuyến tính). Cho chi tiết, xem Trefethen và Bau $[182]$ (Lecture $27)$. Nếu $\lambda_{1}  = 0$, thì tồn tại một lũy thừa $\ell < m$ sao cho $Ax^{\ell} = 0$. nghịch đảo vòng lặp phương pháp là designed để tìm vectơ riêng (eigenvector) liên kết với trị riêng (eigenvalue) $\lambda$ của $A$ cho mà ta biết tốt xấp xỉ $\mu$. Chọn một số ban đầu unit vectơ $x^{0}$ và tính sau đây các dãy $(w^{k})$ và $(x^{k})$, ở đâu $w^{k+1}$ là nghiệm của hệ
$$(A -\mu I)w^{k+1}= x^{k}equivalentlyw^{k+1}= (A -\mu I)^{-1}x^{k},k \ge 0,$$
Và
$$x^{k+1}= \frac{w^{k+1}}{\|w^{k+1}\|} ,k \ge 0.$$
Kết quả sau đây được chứng minh trong Ciarlet $[41]$ (Định lý 6.4.1).
