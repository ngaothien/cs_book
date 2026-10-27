# Các phương pháp của Jacobi, Gauss–Seidel, và Relaxation


<!-- PAGE 394 -->
Với $e_{0} = u_{0} -u = v_{0} -u$. Một lần nữa, theo Mệnh đề 10.2, với mọi $\epsilon  > 0$, tồn tại một tự nhiên
$$ee$$
Số $N(\epsilon$) sao cho nếu $k \ge N(\epsilon$), thì
$$\sup\|B_{1}^{k}e_{0}\|^{1/k}\le \rho (B_{1}) + \epsilon .$$
$$\|e0\|=1$$
Hơn nữa, với mọi $k \ge N(\epsilon$), tồn tại một vectơ $e_{0} = e_{0}(k)$ (với một số phù hợp lựa chọn của $u_{0})$ sao cho
$$\|e_{0}\|= 1and\|B_{2}^{k}e_{0}\|^{1/k}= \|B_{2}^{k}\|^{1/k}\ge \rho (B_{2}),$$
Mà suy ra Phát biểu $(2)$. Trong light của ở trên, ta xem rằng khi ta investigate mới các phương pháp lặp, ta có đến deal với sau đây hai các bài tập: $1$. Cho trước phương pháp lặp (iterative method) với ma trận $B$, xác định liệu phương pháp là convergent. Điều này liên quan đến xác định liệu $\rho (B) < 1$, hoặc tương đương liệu có một chuẩn ma trận phụ thuộc (subordinate matrix norm) sao cho $\|B\| < 1$. Theo Mệnh đề 9.12, điều này suy ra rằng I - $B$ là khả nghịch (vì $\|- B\| = \|B\|$, Mệnh đề 9.12 áp dụng). $2$. Cho trước hai convergent các phương pháp lặp, compare chúng. phương pháp lặp (iterative method) mà là faster là rằng có ma trận có nhỏ hơn bán kính phổ (spectral radius). Ta bây giờ thảo luận ba các phương pháp lặp cho việc giải các hệ phương trình tuyến tính: $1$. Jacobi’s phương pháp $2$. Gauss–Seidel’s phương pháp $3$. phương pháp nới lỏng (relaxation method).

## 10.3 Description của Các phương pháp của Jacobi,

$$Gauss–Seidel, and Relaxation$$
Các phương pháp được mô tả trong mục này là instances của sau đây scheme: Cho trước hệ phương trình tuyến tính Ax $= b$, với $A$ khả nghịch, giả sử ta có thể viết $A$ trong tạo thành
$$A = M -N,$$
Với $M$ khả nghịch, và “dễ đến nghịch đảo,” mà có nghĩa là $M$ là close đến đang là đường chéo hoặc tam giác ma trận (perhaps bởi các khối). Thì Au $= b$ là tương đương đến
$$Mu = Nu + b,$$
Rằng là,
$$u = M^{-1} Nu + M^{-1} b.$$

<!-- PAGE 395 -->
Vì vậy, ta là trong tình huống được mô tả trong trước đó các mục với $B = M^{-1} N$ và $c = M^{-1} b$. Thực ra, vì $A = M$ - $N$, ta có
$$B = M^{-1} N = M^{-1} (M -A) = I -M^{-1} A,(*)$$
Mà chỉ ra rằng I - $B = M^{-1} A$ là khả nghịch. phương pháp lặp (iterative method) liên kết với ma trận $B = M^{-1} N$ được cho bởi
$$u_{k+1} = M^{-1} Nu_{k} + M^{-1} b,k \ge 0,(\dagger )$$
Bắt đầu từ bất kỳ tùy ý vectơ $u_{0}$. Từ thực tế điểm của quan điểm, ta thực hiện không nghịch đảo $M$, và thay vì ta giải một cách lặp các hệ
$$Mu_{k+1} = Nu_{k} + b,k \ge 0.$$
Khác nhau các phương pháp tương ứng với khác nhau các cách của chọn $M$ và $N$ từ $A$. thứ nhất hai các phương pháp chọn $M$ và $N$ như rời nhau submatrices của $A$, nhưng phương pháp nới lỏng (relaxation method) cho phép một số overlapping của $M$ và $N$. Đến mô tả khác nhau các lựa chọn của $M$ và $N$, nó là thuận tiện đến viết $A$ theo ba submatrices $D, E, F$, như
$$A = D -E -F,$$
Ở đâu chỉ khác không các phần tử (entries) trong $D$ là đường chéo các phần tử (entries) trong $A$, chỉ khác không các phần tử (entries) trong $E$ là các âm của khác không các phần tử (entries) trong $A$ ở dưới đường chéo, và chỉ khác không các phần tử (entries) trong $F$ là các âm của khác không các phần tử (entries) trong $A$ ở trên đường chéo. Nhiều hơn/thêm một cách tường minh, nếu
$$A = \begin{pmatrix} a_{11} & a_{12} & a_{13} & \cdots & a_{1n-1} & a_{1n} \\ a_{21} & a_{22} & a_{23} & \cdots & a_{2n-1} & a_{2n} \\ a_{31} & a_{32} & a_{33} & \cdots & a_{3n-1} & a_{3n} \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ a_{n-1 1} & a_{n-1 2} & a_{n-1 3} & \cdots & a_{n-1n-1} & a_{n-1n} \\ a_{n1} & a_{n2} & a_{n3} & a_{n n-1} & a_{n n} \end{pmatrix} ,$$
$$\cdots$$
Thì
$$D = \begin{pmatrix} a_{11} & 0 & 0 & \cdots & 0 & 0 \\ 0 & a_{22} & 0 & \cdots & 0 & 0 \\ 0 & 0 & a_{33} & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \cdots & a_{n-1n-1} & 0 \\ 0 & 0 & 0 & 0 & a_{n n} \end{pmatrix} ,$$
$$\cdots$$

<!-- PAGE 396 -->
$$-E = \begin{pmatrix} 0 & 0 & 0 & \cdots & 0 & 0 \\ a_{21} & 0 & 0 & \cdots & 0 & 0 \\ a_{31} & a_{32} & 0 & \cdots & 0 & 0 \\ \vdots & \vdots & \ddots & \ddots & \vdots & \vdots \\ a_{n-1 1} & a_{n-1 2} & a_{n-1 3} & \ddots & 0 & 0 \\ a_{n1} & a_{n2} & a_{n3} & a_{n n-1} & 0 \end{pmatrix} , -F = \begin{pmatrix} 0 & a_{12} & a_{13} & \cdots & a_{1n-1} & a_{1n} \\ 0 & 0 & a_{23} & \cdots & a_{2n-1} & a_{2n} \\ 0 & 0 & 0 & \ddots & a_{3n-1} & a_{3n} \\ \vdots & \vdots & \vdots & \ddots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & 0 & a_{n-1n} \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix} .$$
$$\cdots \cdots$$
Trong Jacobi’s phương pháp, ta giả sử rằng tất cả đường chéo các phần tử (entries) trong $A$ là khác không, và ta chọn
$$M = D$$
$$N = E + F,$$
Sao cho bởi (*),
$$B = M^{-1} N = D^{-1}(E + F) = I -D^{-1}A.$$
Như matter của ký hiệu, ta cho
$$J = I -D^{-1}A = D^{-1}(E + F),$$
Mà được gọi là Jacobi’s ma trận. tương ứng phương pháp, Jacobi’s phương pháp lặp (iterative method), tính dãy $(u_{k})$ bằng cách sử dụng recurrence
$$u_{k+1} = D^{-1}(E + F)u_{k} + D^{-1}b,k \ge 0.$$
Trong thực tế, ta một cách lặp giải các hệ
$$Du_{k+1} = (E + F)u_{k} + b,k \ge 0.$$
Nếu ta viết $u_{k} = (u_{1}^{k}, \dots  , u_{n}^{k})$, ta giải một cách lặp sau đây hệ: $a_{11}u_{1}^{k+1} = -a_{12}u_{2}^{k} -a_{13}u_{3}^{k} \cdots -a_{1n}u_{n}^{k} + b_{1} a_{22}u_{2}^{k+1} = -a_{21}u_{1}^{k} -a_{23}u_{3}^{k} \cdots -a_{2n}u_{n}^{k} + b_{2}$
$$\vdots \vdots \vdots$$
$$.$$
$a_{n-1n-1}u_{n}^{k+1} = -a_{n-1 1}u_{1}^{k} \cdots -a_{n-1n-2}u_{n-2}^{k} -a_{n-1n}u_{n}^{k} + b_{n-1} a_{n n}u_{n}^{k+1-1} = -a_{n1}u_{1}^{k} -a_{n2}u_{2}^{k} \cdots -a_{n n-1}u_{n-1}^{k} + b_{n}$ Trong Matlab một bước của Jacobi vòng lặp là đạt được bởi sau đây hàm: hàm $v =$ Jacobi2(,b,u) $n =$ kích thước(,1); $v =$ các không điểm(n,1); cho $i =$ 1:n
$$v(i,1)= u(i,1) + (-A(i,:)*u + b(i))/A(i,i);$$
Kết thúc/cuối kết thúc/cuối

<!-- PAGE 397 -->
Trong thứ tự đến chạy $m$ vòng lặp các bước, chạy sau đây hàm: hàm $u =$ jacobi(,b,u0,m) $u =$ u0; cho $j =$ 1:m $u =$ Jacobi2(,b,u); kết thúc/cuối kết thúc/cuối

> **Ví dụ 10.1.** Xét hệ phương trình tuyến tính
$$\begin{pmatrix} 2 & -1 & 0 & 0 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ 0 & 0 & 1 & 2 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \\ x_{4} \end{pmatrix} = \begin{pmatrix} 25 \\ -24 \\ 21 \\ 15 \end{pmatrix} .$$
$$--$$
Ta kiểm tra ngay lập tức rằng nghiệm là
$$x_{1} = 11, x_{2} = -3, x_{3} = 7, x_{4} = -4.$$
Nó là dễ để xem rằng Jacobi ma trận là
$$J = \frac{1}{2} \begin{pmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix} .$$
Sau $10$ Jacobi các vòng lặp, ta tìm xấp xỉ nghiệm
$$x_{1} = 10.2588, x_{2} = -2.5244, x_{3} = 5.8008, x_{4} = -3.7061.$$
Sau $20$ các vòng lặp, ta tìm xấp xỉ nghiệm
$$x_{1} = 10.9110, x_{2} = -2.9429, x_{3} = 6.8560, x_{4} = -3.9647.$$
Sau $50$ các vòng lặp, ta tìm xấp xỉ nghiệm
$$x_{1} = 10.9998, x_{2} = -2.9999, x_{3} = 6.9998, x_{4} = -3.9999,$$
Và Sau $60$ các vòng lặp, ta tìm xấp xỉ nghiệm
$$x_{1} = 11.0000, x_{2} = -3.0000, x_{3} = 7.0000, x_{4} = -4.0000,$$
Đúng sai khác ít nhất bốn decimals. Nó có thể được được hiển thị (xem Bài toán 10.6) rằng các trị riêng (eigenvalues) của $J$ là
$$\cos \begin{pmatrix} \pi \\ 5 \end{pmatrix} , \cos \begin{pmatrix} 2\pi \\ 5 \end{pmatrix} , \cos \begin{pmatrix} 3\pi \\ 5 \end{pmatrix} , \cos \begin{pmatrix} 4\pi \\ 5 \end{pmatrix} ,$$

<!-- PAGE 398 -->
Do đó bán kính phổ (spectral radius) của $J = B$ là
$$\rho (J) = \cos \begin{pmatrix} \pi \\ 5 \end{pmatrix} = 0.8090 < 1.$$
Theo Định lý 10.3, Jacobi’s phương pháp hội tụ cho ma trận của ví dụ này. Nhận thấy rằng ta có thể thử đến “speed lên” phương pháp bằng cách sử dụng mới giá trị $u_{1}^{k+1}$ thay vì của $u_{1}^{k}$ trong việc giải cho $u_{2}^{k+2}$ bằng cách sử dụng thứ hai các phương trình, và tổng quát hơn, sử dụng $u_{1}^{k+1}, \dots  , u_{i-1}^{k+1}$ thay vì của $u_{1}^{k}, \dots  , u_{i-1}^{k}$ trong việc giải cho $u_{i}^{k+1}$ trong phương trình thứ $i$. Điều này nhận xét dẫn đến đến hệ $a_{11}u^{k+1} = -a_{12}u_{2}^{k} -a_{13}u_{3}^{k} \cdots -a_{1n}u_{n}^{k} + b_{1} a_{22}u_{2}^{k1+1} = -a_{21}u_{1}^{k+1} -a_{23}u_{3}^{k} \cdots -a_{2n}u_{n}^{k} + b_{2} \vdots \vdots \vdots a_{n-1n-1}u_{n}^{k+1} = -a_{n-1 1}u_{1}^{k+1} \cdots -a_{n-1n-2}u_{n-2}^{k+1} -a_{n-1n}u_{n}^{k} + b_{n-1} a_{n n}u_{n}^{k+1-1} = -a_{n1}u_{1}^{k+1} -a_{n2}u_{2}^{k+1} \cdots -a_{n n-1}u_{n-1}^{k+1} + b_{n}$, mà, trong ma trận tạo thành, được viết
$$Du_{k+1} = Eu_{k+1} + Fu_{k} + b.$$
Bởi vì $D$ là khả nghịch và $E$ là tam giác dưới (lower triangular), ma trận $D$ - $E$ là khả nghịch, do đó ở trên phương trình là tương đương đến
$$u_{k+1} = (D -E)^{-1}Fu_{k} + (D -E)^{-1}b,k \ge 0.$$
Ở trên tương ứng với chọn $M$ và $N$ là
$$M = D -E$$
$$N = F,$$
Và ma trận $B$ được cho bởi
$$B = M^{-1} N = (D -E)^{-1}F.$$
Vì $M = D$ - $E$ là khả nghịch, ta biết rằng I - $B = M^{-1} A$ là cũng khả nghịch. phương pháp rằng ta chỉ được mô tả là phương pháp lặp (iterative method) của Gauss–Seidel, và ma trận $B$ được gọi là ma trận của Gauss–Seidel và được ký hiệu bởi $\mathcal{L}_{1}$, với
$$\mathcal{L}_{1} = (D -E)^{-1}F.$$
Một của advantages của phương pháp của Gauss–Seidel là rằng là đòi hỏi chỉ một nửa của memory được sử dụng bởi Jacobi’s phương pháp, vì ta chỉ cần
$$u_{1}^{k+1}, \dots  , u_{i-1}^{k+1} , u_{i+1}^{k}, \dots  , u_{n}^{k}$$
Để tính $u_{i}^{k+1}$. Ta cũng chỉ ra rằng trong nhất định quan trọng các trường hợp (ví dụ, nếu $A$ là ma trận ba đường chéo (tridiagonal matrix)), phương pháp của Gauss–Seidel hội tụ faster hơn Jacobi’s phương pháp (trong trường hợp này, chúng cả hai hội tụ hoặc diverge simultaneously). Trong Matlab một bước của Gauss–Seidel vòng lặp là đạt được bởi sau đây hàm:

<!-- PAGE 399 -->
Hàm $u =$ GaussSeidel3(,b,u) $n =$ kích thước(,1); cho $i =$ 1:n u(i,1) $=$ u(i,1) $+$ (-(i,:)*u $+ b(i))/A(i,i)$; kết thúc/cuối kết thúc/cuối Nó là đáng chú ý rằng chỉ difference với Jacobi2 là rằng cùng biến $u$ được sử dụng trên cả hai vế của assignment. Trong thứ tự đến chạy $m$ vòng lặp các bước, chạy sau đây hàm: hàm $u =$ GaussSeidel1(,b,u0,m) $u =$ u0; cho $j =$ 1:m $u =$ GaussSeidel3(,b,u); kết thúc/cuối kết thúc/cuối

> **Ví dụ 10.2.** Xét cùng hệ phương trình tuyến tính
$$\begin{pmatrix} 2 & -1 & 0 & 0 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ 0 & 0 & 1 & 2 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \\ x_{4} \end{pmatrix} = \begin{pmatrix} 25 \\ -24 \\ 21 \\ 15 \end{pmatrix}$$
$$--$$
Như trong Ví dụ 10.1, có nghiệm là
$$x_{1} = 11, x_{2} = -3, x_{3} = 7, x_{4} = -4.$$
Sau $10$ Gauss–Seidel các vòng lặp, ta tìm xấp xỉ nghiệm
$$x_{1} = 10.9966, x_{2} = -3.0044, x_{3} = 6.9964, x_{4} = -4.0018.$$
Sau $20$ các vòng lặp, ta tìm xấp xỉ nghiệm
$$x_{1} = 11.0000, x_{2} = -3.0001, x_{3} = 6.9999, x_{4} = -4.0000.$$
Sau $25$ các vòng lặp, ta tìm xấp xỉ nghiệm
$$x_{1} = 11.0000, x_{2} = -3.0000, x_{3} = 7.0000, x_{4} = -4.0000,$$
Đúng sai khác ít nhất bốn decimals. Ta nhận thấy rằng cho ví dụ này, Gauss–Seidel’s phương pháp hội tụ về hai lần như fast như Jacobi’s phương pháp. Nó sẽ được hiển thị trong Mệnh đề 10.8 rằng cho ma trận ba đường chéo (tridiagonal matrix), bán kính phổ (spectral radius) của Gauss–Seidel ma trận $\mathcal{L}_{1}$ được cho bởi
$$\rho (\mathcal{L}_{1}) = (\rho (J))^{2},$$
Do đó của ta nhận xét là consistent với lý thuyết.

<!-- PAGE 400 -->
Mới ingredient trong phương pháp nới lỏng (relaxation method) là đến incorporate phần của ma trận $D$ vào $N$: ta định nghĩa $M$ và $N$ bởi
$$M = \frac{D}{\omega} -E$$
$$-$$
$$N = \frac{1\omega}{\omega} D + F,$$
Ở đâu $\omega  \neq  0$ là thực tham số là suitably được chọn. Thực sự, ta chỉ ra trong Mục 10.4 rằng cho phương pháp nới lỏng (relaxation method) đến hội tụ, ta phải có $\omega  \in (0, 2)$. Lưu ý rằng trường hợp $\omega  = 1$ tương ứng với phương pháp của Gauss–Seidel. Nếu ta giả sử rằng tất cả đường chéo các phần tử (entries) của $D$ là khác không, ma trận $M$ là khả nghịch. ma trận $B$ được ký hiệu bởi $\mathcal{L}_{\omega}$ và được gọi là ma trận của relaxation, với
$$-1$$
$$\mathcal{L}_{\omega} = \begin{pmatrix} D \\ -E \\ \omega \end{pmatrix} \begin{pmatrix} 1 -\omega \\ D + F \\ \omega \end{pmatrix} = (D -\omega E)^{-1}((1 -\omega )D + \omega F).$$
Số $\omega$ được gọi là tham số của relaxation. Khi $\omega  > 1$, phương pháp nới lỏng (relaxation method) là đã biết như successive overrelaxation, abbreviated như SOR. Tại thứ nhất glance relaxation ma trận $\mathcal{L}_{\omega}$ dường như nhiều nhiều hơn/thêm phức tạp hơn Gauss– Seidel ma trận $\mathcal{L}_{1}$, nhưng lặp hệ liên kết với phương pháp nới lỏng (relaxation method) là rất đồng dạng đến phương pháp của Gauss–Seidel, và là khá đơn giản. Thật vậy, hệ liên kết với phương pháp nới lỏng (relaxation method) được cho bởi
$$\begin{pmatrix} D \\ -E \\ \omega \end{pmatrix} u_{k+1} = \begin{pmatrix} 1 -\omega \\ D + F \\ \omega \end{pmatrix} u_{k} + b,$$
Mà là tương đương đến
$$(D -\omega E)u_{k+1} = ((1 -\omega )D + \omega F)u_{k} + \omega b,$$
Và có thể được được viết
$$Du_{k+1} = Du_{k} -\omega (Du_{k} -Eu_{k+1} -Fu_{k} -b).$$
Một cách tường minh, điều này là hệ $a_{11}u_{1}^{k+1} = a_{11}u_{1}^{k}$ - $\omega (a_{11}u_{1}^{k} + a_{12}u_{2}^{k} + a_{13}u_{3}^{k} + \cdots  + a_{1n-2}u_{n-2}^{k} + a_{1n-1}u_{n-1}^{k} + a_{1n}u_{n}^{k}$ - $b_{1}) a_{22}u_{2}^{k+1} = a_{22}u_{2}^{k}$ - $\omega (a_{21}u_{1}^{k+1} + a_{22}u_{2}^{k} + a_{23}u_{3}^{k} + \cdots  + a_{2n-2}u_{n-2}^{k} + a_{2n-1}u_{n-1}^{k} + a_{2n}u_{n}^{k}$ - $b_{2})$
$$\vdots$$
$a_{n n}u_{n}^{k+1} = a_{n n}u_{n}^{k}$ - $\omega (a_{n1}u_{1}^{k+1} + a_{n2}u_{2}^{k+1} + \cdots  + a_{n n-2}u_{n-2}^{k+1} + a_{n n-1}u_{n-1}^{k+1} + a_{n n}u_{n}^{k}$ - $b_{n})$. Trong Matlab một bước của relaxation vòng lặp là đạt được bởi sau đây hàm:

<!-- PAGE 401 -->
Hàm $u =$ relax3(,b,u,omega) $n =$ kích thước(,1); cho $i =$ 1:n u(i,1) $=$ u(i,1) $+$ omega*(-(i,:)*u $+ b(i))/A(i,i)$; kết thúc/cuối kết thúc/cuối Nhận thấy rằng hàm relax3 là thu được từ hàm GaussSeidel3 bởi đơn giản inserting $\omega$ trong trước của biểu thức (-(i, $:)*u+b(i))/A(i, i)$. Trong thứ tự đến chạy $m$ vòng lặp các bước, chạy sau đây hàm: hàm $u =$ relax(,b,u0,omega,m) $u =$ u0; cho $j =$ 1:m $u =$ relax3(,b,u,omega); kết thúc/cuối kết thúc/cuối

> **Ví dụ 10.3.** Xét cùng hệ phương trình tuyến tính như trong Các ví dụ 10.1 và 10.2, có nghiệm là
$$x_{1} = 11, x_{2} = -3, x_{3} = 7, x_{4} = -4.$$
Sau $10$ relaxation các vòng lặp với $\omega  =$ 1.1, ta tìm xấp xỉ nghiệm
$$x_{1} = 11.0026, x_{2} = -2.9968, x_{3} = 7.0024, x_{4} = -3.9989.$$
Sau $10$ các vòng lặp với $\omega  =$ 1.2, ta tìm xấp xỉ nghiệm
$$x_{1} = 11.0014, x_{2} = -2.9985, x_{3} = 7.0010, x_{4} = -3.9996.$$
Sau $10$ các vòng lặp với $\omega  =$ 1.3, ta tìm xấp xỉ nghiệm
$$x_{1} = 10.9996, x_{2} = -3.0001, x_{3} = 6.9999, x_{4} = -4.0000.$$
Sau $10$ các vòng lặp với $\omega  =$ 1.27, ta tìm xấp xỉ nghiệm
$$x_{1} = 11.0000, x_{2} = -3.0000, x_{3} = 7.0000, x_{4} = -4.0000,$$
Đúng sai khác ít nhất bốn decimals. Ta nhận thấy rằng cho ví dụ này phương pháp của relaxation với $\omega  =$ 1.27 hội tụ faster hơn phương pháp của Gauss–Seidel. Điều này nhận xét sẽ là confirmed theo Mệnh đề 10.10. Những gì vẫn còn được thực hiện là để tìm các điều kiện rằng đảm bảo sự hội tụ của phương pháp nới lỏng (relaxation method) (và Gauss–Seidel phương pháp), nghĩa là: $1$. Tìm các điều kiện trên $\omega$, cụ thể là một số khoảng/đoạn $I \subseteq \mathbb{R}$ sao cho $\omega  \in$ I suy ra $\rho (\mathcal{L}_{\omega}) < 1$; ta sẽ chứng minh rằng $\omega  \in (0, 2)$ là cần điều kiện.
