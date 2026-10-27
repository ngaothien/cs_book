# Hermite Trường hợp; Phép lặp Lanczos (Lanczos iteration)


<!-- PAGE 685 -->
Khi $\|r_{n}\|_{2} = \|H_{n}y -\|b\|_{2}e_{1}\|_{2}$ được xét nhỏ đủ, ta dừng và xấp xỉ
$$e$$
Nghiệm của Ax $= b$ là thì
$$x_{n} = U_{n}y.$$
Có các cách của improving efficiency của “naive” phiên bản của GMRES rằng ta chỉ được trình bày; xem Trefethen và Bau $[182]$ (Lecture $35)$. Ta bây giờ xét trường hợp ở đâu $A$ là Hermite (hoặc đối xứng) ma trận.

## 18.6 Hermite Trường hợp; Phép lặp Lanczos (Lanczos iteration)

Nếu $A$ là $m\times m$ đối xứng hoặc Ma trận Hermite (Hermitian matrix), thì Arnoldi’s phương pháp là đơn giản hơn và nhiều nhiều hơn/thêm efficient. Thật vậy, trong trường hợp này, nó là dễ để xem rằng trên Hessenberg các ma trận $H_{n}$ là cũng đối xứng (Hermite respectively), và do đó ba đường chéo. Cũng, các trị riêng (eigenvalues) của $A$ và $H_{n}$ là thực. Nó là thuận tiện đến viết
$$H_{n} = \begin{pmatrix} \alpha_{1} & \beta_{1} \\ \beta_{1} & \alpha_{2} & \beta_{2} \\ \beta_{2} & \alpha_{3} & \ddots \\ \ddots & \ddots & \beta_{n-1} \\ \beta_{n-1} & \alpha_{n} \end{pmatrix} .$$
Recurrence $(*_{2})$ của Mục 18.4 trở thành three-term recurrence
$$Au_{n} = \beta_{n-1} u_{n-1} + \alpha_{n} u_{n} + \beta_{n} u_{n+1}.(*_{6})$$
Ta cũng có $\alpha_{n}  = u_{n}^{*}Au_{n}$, do đó Arnoldi’s thuật toán trở thành sau đây thuật toán đã biết như Lanczos’ thuật toán (hoặc Phép lặp Lanczos (Lanczos iteration)). trong khuyên trên $j$ từ $1$ đến $n$ có đã được được khử và được thay thế bởi đơn lẻ assignment. Cho trước tùy ý khác không vectơ $b \in \mathbb{C}^{m}$, cho $u_{1} = b/ \|b\|$; cho $n = 1, 2, 3, \dots$ thực hiện $z := Au_{n}; \alpha_{n}  := u_{n}^{*}z; z := z$ - $\beta_{n-1} u_{n-1}$ - $\alpha_{n} u_{n} \beta_{n}  := \|z\|$; nếu $\beta_{n}  = 0$ quit $u_{n+1} = z/\beta_{n}$ Khi $\beta_{n}  = 0$, ta nói rằng ta có breakdown của Phép lặp Lanczos (Lanczos iteration). Các phiên bản của Mệnh đề 18.5 và Định lý 18.6 áp dụng đến Phép lặp Lanczos (Lanczos iteration). Ngoài ra đang là nhiều nhiều hơn/thêm efficient hơn Phép lặp Arnoldi (Arnoldi iteration), Phép lặp Lanczos (Lanczos iteration) có advantage rằng Rayleigh–Ritz phương pháp cho việc tìm một số của các trị riêng (eigenvalues) của $A$ như các trị riêng (eigenvalues)
