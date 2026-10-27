# Sự hội tụ Các phương pháp cho Ba đường chéo Các ma trận


<!-- PAGE 405 -->

> **Mệnh đề 10.7.** Cho trước bất kỳ ma trận $A = D$ - $E$ - $F$, với $A$ và $D$ khả nghịch, với mọi $\omega  \neq  0$, ta có
$$\rho (\mathcal{L}_{\omega}) \ge |\omega  -1|,$$
$$-1$$
$$where \mathcal{L}_{\omega} = \begin{pmatrix} D-E \\ \overline{\omega} \end{pmatrix} \begin{pmatrix} 1-\omega D + F \\ \overline{\omega} \\ \omega & (0, 2). \end{pmatrix} . Therefore, the relaxation method (possibly by blocks)$$
Thực hiện không hội tụ trừ khi $\in$ Nếu ta cho phép $\omega$ là phức, thì ta phải có
$$|\omega  -1| < 1$$
Cho phương pháp nới lỏng (relaxation method) đến hội tụ.

*Chứng minh.* Nhận thấy rằng tích $\lambda_{1}  \cdots  \lambda_{n}$ của các trị riêng (eigenvalues) $of\mathcal{L}_{\omega}$, mà bằng $det(\mathcal{L}_{\omega})$, được cho bởi
$$\lambda_{1}  \cdots  \lambda_{n}  = \det(\mathcal{L}_{\omega}) = \frac{\det}{\det} \begin{pmatrix} 1 -\omega \\ D + F \\ \omega \\ D &  \end{pmatrix} = (1 -\omega )^{n}.$$
$$\begin{pmatrix} -E \\ \omega \end{pmatrix}$$
Suy ra rằng
$$\rho (\mathcal{L}_{\omega}) \ge |\lambda_{1}  \cdots  \lambda_{n} |^{1/n}= |\omega  -1|.$$
Chứng minh là cùng nếu $\omega  \in \mathbb{C}$.

## 10.5 Sự hội tụ của Các phương pháp của Jacobi,

$$Gauss–Seidel, and Relaxation for$$
$$Tridiagonal Matrices$$
Ta bây giờ xét trường hợp ở đâu $A$ là ma trận ba đường chéo (tridiagonal matrix), có thể bởi các khối. Trong trường hợp này, ta thu được precise các kết quả về bán kính phổ (spectral radius) của $J$ và $\mathcal{L}_{\omega}$, và hệ quả là, về sự hội tụ của các phương pháp này. Ta cũng thu được một số information về tốc độ của sự hội tụ của các phương pháp này. Ta bắt đầu với trường hợp $\omega  = 1$, mà là technically dễ hơn đến deal với. sau đây mệnh đề cho chúng ta precise relationship giữa spectral radii $\rho (J)$ và $\rho (\mathcal{L}_{1})$ của Jacobi ma trận và Gauss–Seidel ma trận.

> **Mệnh đề 10.8.** Cho $A$ là ma trận ba đường chéo (tridiagonal matrix) (có thể bởi các khối). Nếu $\rho (J)$ là bán kính phổ (spectral radius) của Jacobi ma trận và $\rho (\mathcal{L}_{1})$ là bán kính phổ (spectral radius) của Gauss–Seidel ma trận, thì ta có
$$\rho (\mathcal{L}_{1}) = (\rho (J))^{2}.$$
Hệ quả là, phương pháp của Jacobi và phương pháp của Gauss–Seidel cả hai hội tụ hoặc cả hai diverge simultaneously (chẵn/ngay cả khi $A$ là ba đường chéo bởi các khối); khi chúng hội tụ, phương pháp của Gauss–Seidel hội tụ faster hơn Jacobi’s phương pháp.

<!-- PAGE 406 -->

*Chứng minh.* Ta bắt đầu với preliminary kết quả. Cho $A(\mu$) là ma trận ba đường chéo (tridiagonal matrix) bởi khối của tạo thành
$$A(\mu ) = \begin{pmatrix} A_{1} & \mu^{-1} C_{1} & 0 & 0 & \cdots & 0 \\ \mu B_{1} & A_{2} & \mu^{-1} C_{2} & 0 & \cdots & 0 \\ 0 & \ddots & \ddots & \ddots & \cdots & \vdots \\ \vdots & \cdots & \ddots & \ddots & \ddots & 0 \\ 0 & \cdots & 0 & \mu B_{p-2} & A_{p-1} & \mu^{-1} C_{p-1} \\ 0 & 0 & \mu B_{p-1} & A_{p} \end{pmatrix} ,$$
$$\cdots \cdots$$
Thì
$$\det(A(\mu )) = \det(A(1)),\mu  \neq  0.$$
Để chứng minh sự kiện này, tạo thành khối ma trận đường chéo (diagonal matrix)
$$P(\mu ) = \mathrm{diag}(\mu I_{1}, \mu^{2} I_{2}, \dots  , \mu^{p} I_{p}),$$
Ở đâu $I_{j}$ là ma trận đơn vị (identity matrix) của cùng số chiều như khối $A_{j}$. Thì nó là dễ để xem rằng
$$A(\mu ) = P(\mu )A(1)P(\mu )^{-1},$$
Và do đó,
$$\det(A(\mu )) = \det(P(\mu )A(1)P(\mu )^{-1}) = \det(A(1)).$$
Vì Jacobi ma trận là $J = D^{-1}(E + F)$, các trị riêng (eigenvalues) của $J$ là các không điểm của đa thức đặc trưng (characteristic polynomial)
$$p_{J}(\lambda ) = \det(\lambda I -D^{-1}(E + F)),$$
Và do đó, chúng là cũng các không điểm của đa thức
$$q_{J}(\lambda ) = \det(\lambda D -E -F) = \det(D)p_{J}(\lambda ).$$
Tương tự, vì Gauss–Seidel ma trận là $\mathcal{L}_{1} = (D -E)^{-1}F$, các không điểm của đa thức đặc trưng (characteristic polynomial)
$$p_{L1}(\lambda ) = \det(\lambda I -(D -E)^{-1}F)$$
Là cũng các không điểm của đa thức
$$q_{L1}(\lambda ) = \det(\lambda D -\lambda E -F) = \det(D -E)p_{L1}(\lambda ).$$
Vì $A = D$ - $E$ - $F$ là ba đường chéo (hoặc ba đường chéo bởi các khối), $\lambda^{2} D$ - $\lambda^{2} E$ - $F$ là cũng ba đường chéo (hoặc ba đường chéo bởi các khối), và bằng cách sử dụng của ta preliminary kết quả với $\mu  = \lambda  \neq  0$ bắt đầu với ma trận $\lambda^{2} D$ - $\lambda E$ - $\lambda F$, ta thu được
$$\lambda^{n} q_{J}(\lambda ) = \det(\lambda^{2} D -\lambda E -\lambda F) = \det(\lambda^{2} D -\lambda^{2} E -F) = q_{L1}(\lambda^{2} ).$$
Bởi tính liên tục, ở trên phương trình cũng nghiệm đúng cho $\lambda  = 0$. Nhưng khi đó ta suy ra rằng:

<!-- PAGE 407 -->
$1$. Với mọi $\beta  \neq  0$, nếu $\beta$ là trị riêng (eigenvalue) của $\mathcal{L}_{1}$, thì $\beta^{1/2}$ và $-\beta^{1/2}$ là cả hai các trị riêng (eigenvalues) của $J$, ở đâu $\beta^{1/2}$ là một của phức square các nghiệm của $\beta$. $2$. Với mọi $\alpha  \neq  0, \alpha$ là các trị riêng (eigenvalues) của $J$ khi và chỉ khi $-\alpha$ là các trị riêng (eigenvalues) của $J$, và nếu $\alpha$ là các trị riêng (eigenvalues) của $J$, thì $\alpha^{2}$ là trị riêng (eigenvalue) của $\mathcal{L}_{1}$. ở trên ngay lập tức suy ra rằng $\rho (\mathcal{L}_{1}) = (\rho (J))^{2}$. Ta bây giờ xét nhiều hơn/thêm tổng quát tình huống ở đâu $\omega$ là bất kỳ thực trong $(0, 2)$.

> **Mệnh đề 10.9.** Cho $A$ là ma trận ba đường chéo (tridiagonal matrix) (có thể bởi các khối), và giả sử rằng các trị riêng (eigenvalues) của Jacobi ma trận là tất cả thực. Nếu $\omega  \in (0, 2)$, thì phương pháp của Jacobi và phương pháp của relaxation cả hai hội tụ hoặc cả hai diverge simultaneously (chẵn/ngay cả khi $A$ là ba đường chéo bởi các khối). Khi chúng hội tụ, hàm $\omega  \mapsto \rho (\mathcal{L}_{\omega})$ (cho $\omega  \in (0, 2))$ có duy nhất cực tiểu bằng $\omega_{0}$ - $1$ cho
$$\omega_{0}  = \frac{2}{1 +p1 -(\rho (J))^{2}} ,$$
Ở đâu $1 < \omega_{0}  < 2$ nếu $\rho (J) > 0$.

*Chứng minh.* chứng minh là rất technical và có thể được tìm thấy trong Serre $[162]$ và Ciarlet $[41]$. Như trong chứng minh của trước đó mệnh đề, ta bắt đầu bởi chỉ ra rằng các trị riêng (eigenvalues) của ma trận $\mathcal{L}_{\omega}$ là các không điểm của đa thức
$$q_{L\omega}(\lambda ) = \det \begin{pmatrix} \lambda  + \omega  -1 \\ D -\lambda E -F \\ \omega \end{pmatrix} = \det \begin{pmatrix} D \\ -E \\ \omega \end{pmatrix} p_{L\omega}(\lambda ),$$
Ở đâu $p_{L\omega}(\lambda$) là đa thức đặc trưng (characteristic polynomial) của $\mathcal{L}_{\omega}$. Thì bằng cách sử dụng preliminary sự kiện từ Mệnh đề 10.8, nó là dễ để chỉ ra rằng
$$q_{L\omega}(\lambda^{2} ) = \lambda^{n} q_{J} \begin{pmatrix} \lambda^{2}  + \omega  -1 \\ \lambda \omega \end{pmatrix} ,$$
Với mọi $\lambda  \in \mathbb{C}$, với $\lambda  \neq  0$. Điều này time ta không thể mở rộng ở trên phương trình đến $\lambda  = 0$. Điều này dẫn đến chúng ta đến xét phương trình
$$\frac{\lambda^{2} + \omega 1}{\lambda \omega} -= \alpha ,$$
Mà là tương đương đến
$$\lambda^{2} -\alpha \omega \lambda  + \omega  -1 = 0,$$
Với mọi $\lambda  \neq  0$. Vì $\lambda  \neq  0$, ở trên equivalence thực hiện không đúng cho $\omega  = 1$, nhưng điều này là không bài toán vì trường hợp $\omega  = 1$ có đã đã được được xét trong trước đó mệnh đề. Thì ta có thể chỉ ra sau đây:

<!-- PAGE 408 -->
$1$. Với mọi $\beta  \neq  0$, nếu $\beta$ là trị riêng (eigenvalue) của $\mathcal{L}_{\omega}$, thì
$$- -$$
$$\frac{\beta  + \omega 1}{\beta^{1/2} \omega} ,- \frac{\beta  + \omega 1}{\beta^{1/2} \omega}$$
Là các trị riêng (eigenvalues) của $J. 2$. Với mọi $\alpha  \neq  0$, nếu $\alpha$ và $-\alpha$ là các trị riêng (eigenvalues) của $J$, thì $\mu_{+} (\alpha , \omega$) và $\mu_{-} (\alpha , \omega$) là các trị riêng (eigenvalues) của $\mathcal{L}_{\omega}$, ở đâu $\mu_{+} (\alpha , \omega$) và $\mu_{-} (\alpha , \omega$) là squares của các nghiệm của phương trình
$$\lambda^{2} -\alpha \omega \lambda  + \omega  -1 = 0.$$
Suy ra rằng
$$\rho (\mathcal{L}_{\omega}) =\max{\max(|\mu_{+} (\alpha , \omega )|, |\mu_{-} (\alpha , \omega )|)},$$
$$\alpha  | pJ(\alpha )=0$$
Và vì ta là giả sử rằng $J$ có thực các nghiệm, ta là đã dẫn đến đến study hàm
$$M(\alpha , \omega ) = \max{|\mu_{+} (\alpha , \omega )|, |\mu_{-} (\alpha , \omega )|},$$
Ở đâu $\alpha  \in \mathbb{R}$ và $\omega  \in (0, 2)$. Thực sự, bởi vì $M(-\alpha , \omega$) $= M(\alpha , \omega$), nó là chỉ cần đến xét trường hợp ở đâu $\alpha  \ge 0$. Lưu ý rằng cho $\alpha  \neq  0$, các nghiệm của phương trình
$$\lambda^{2} -\alpha \omega \lambda  + \omega  -1 = 0.$$
Là
$$\frac{\alpha \omega \sqrt{\alpha}^{2}\overline{\omega}^{2}\overline{4}\overline{\omega}\overline{+ 4}}{2} \pm  \overline{-}.$$
Trong turn, điều này dẫn đến đến xét các nghiệm của phương trình
$$\omega^{2} \alpha^{2} -4\omega  + 4 = 0,$$
Mà là
$$\frac{2(1\sqrt{1}\overline{\alpha}^{2})}{\alpha^{2}} \pm \overline{-},$$
Cho $\alpha  \neq  0$. Vì ta có
$$\overline{-} \overline{-} -\overline{-}$$
$$\frac{2(1 +\sqrt{1}\overline{\alpha}^{2})}{\alpha^{2}} = \frac{2(1 +\sqrt{1}\overline{\alpha}^{2})(1\sqrt{1}\overline{\alpha}^{2})}{\alpha^{2} (1 -1 -\alpha^{2} )} \sqrt= \frac{2}{1 -1 -\alpha^{2}} \sqrt$$
Và
$$-\overline{-} \overline{-} -\overline{-}$$
$$\frac{2(1\sqrt{1}\overline{\alpha}^{2})}{\alpha^{2}} = \frac{2(1 +\sqrt{1}\overline{\alpha}^{2})(1\sqrt{1}\overline{\alpha}^{2})}{\alpha^{2} (1 +1 -\alpha^{2} )} \sqrt= \frac{2}{1 +1 -\alpha^{2}} \sqrt,$$
Các phần tử này các nghiệm là
$$\omega_{0} (\alpha ) = \frac{2}{1 +1 -\alpha^{2}} \sqrt,\omega_{1} (\alpha ) = \frac{2}{1 -1 -\alpha^{2}} \sqrt.$$

<!-- PAGE 409 -->
Nhận thấy rằng biểu thức cho $\omega_{0} (\alpha$) là chính xác biểu thức trong phát biểu của mệnh đề của chúng ta! rest của chứng minh bao gồm trong analyzing variations của hàm $M(\alpha , \omega$) bởi xét khác nhau các trường hợp cho $\alpha$. Trong kết thúc/cuối, ta tìm rằng cực tiểu của $\rho (\mathcal{L}_{\omega})$ là thu được cho $\omega_{0} (\rho (J))$. chi tiết là tẻ nhạt/dài dòng và ta bỏ qua chúng. độc giả sẽ tìm đầy đủ các chứng minh trong Serre $[162]$ và Ciarlet $[41]$. Combining các kết quả của Định lý 10.6 và Mệnh đề 10.9, ta thu được kết quả sau kết quả mà cho precise information về spectral radii của các ma trận $J, \mathcal{L}_{1}$, và $\mathcal{L}_{\omega}$.

> **Mệnh đề 10.10.** Cho $A$ là ma trận ba đường chéo (tridiagonal matrix) (có thể bởi các khối) mà là Hermite xác định dương (positive definite). Thì các phương pháp của Jacobi, Gauss–Seidel, và relaxation, tất cả hội tụ cho $\omega  \in (0, 2)$. Tồn tại duy nhất một tối ưu relaxation tham số
$$\omega_{0}  = \frac{2}{1 +p1 -(\rho (J))^{2}} ,$$
Sao cho
$$\rho (\mathcal{L}_{\omega0}) =\inf \rho (\mathcal{L}_{\omega}) = \omega_{0}  -1.$$
$$0<\omega <2$$
Hơn nữa, nếu $\rho (J) > 0$, thì
$$\rho (\mathcal{L}_{\omega0}) < \rho (\mathcal{L}_{1}) = (\rho (J))^{2}< \rho (J),$$
Và nếu $\rho (J) = 0$, thì $\omega_{0}  = 1$ và $\rho (\mathcal{L}_{1}) = \rho (J) = 0$.

*Chứng minh.* Trong thứ tự để áp dụng Mệnh đề 10.9, ta có để kiểm tra rằng $J = D^{-1}(E + F)$ có thực các trị riêng (eigenvalues). Tuy nhiên, nếu $\alpha$ là bất kỳ trị riêng (eigenvalue) của $J$ và nếu $u$ là bất kỳ tương ứng vectơ riêng (eigenvector), thì
$$D^{-1}(E + F)u = \alpha u$$
Suy ra rằng
$$(E + F)u = \alpha Du,$$
Và vì $A = D$ - $E$ - $F$, ở trên chỉ ra rằng $(D$ -)u $= \alpha$ Du, nghĩa là,
$$Au = (1 -\alpha )Du.$$
Hệ quả là,
$$u^{*}Au = (1 -\alpha )u^{*}Du,$$
Và vì $A$ và $D$ là Hermite xác định dương (positive definite), ta có $u^{*}Au > 0$ và $u^{*}Du > 0$ vì u̸ $= 0$, mà chứng tỏ rằng $\alpha  \in \mathbb{R}$. rest suy ra từ Định lý 10.6 và Mệnh đề 10.9.
Nhận xét: Nó được ưu tiên hơn đến overestimate thay vì underestimate relaxation tham số khi tối ưu relaxation tham số là không đã biết chính xác.
