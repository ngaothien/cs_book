# Định lý phổ (spectral theorem) cho Chuẩn tắc/bình thường Các ánh xạ tuyến tính (linear maps)


<!-- PAGE 631 -->

## 17.3 Định lý phổ (spectral theorem) cho Chuẩn tắc/bình thường Các ánh xạ tuyến tính (linear maps)

Cho trước Không gian Euclid (Euclidean space) $E$, của ta tiếp theo bước là để chỉ ra rằng với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$ tồn tại một không gian con $W$ có số chiều $1$ hoặc $2$ sao cho f(W) $\subseteq W$. Khi dim(W) $= 1$, không gian con $W$ là thực sự không gian riêng (eigenspace) với một số thực trị riêng (eigenvalue) của $f$. Hơn nữa, khi $f$ là chuẩn tắc/bình thường, có một không gian con $W$ có số chiều $1$ hoặc $2$ sao cho f(W) $\subseteq W$ và $f^{*} (W) \subseteq W$. difficulty là rằng các trị riêng (eigenvalues) của $f$ là không nhất thiết thực. Một cách để thu được xung quanh bài toán này là đến complexify cả hai không gian vectơ (vector space) $E$ và tích vô hướng (inner product) $\langle$ -, $-\rangle$ như ta đã thực hiện trong Mục 17.2. Cho trước bất kỳ không gian con $W$ của Không gian Euclid (Euclidean space) $E$, nhắc lại rằng phần bù trực giao (orthogonal complement) $W^{\perp}$ của $W$ là không gian con được định nghĩa sao cho
$$W^{\perp} = {u \in E | \langle u, w\rangle = 0, for all w \in W}.$$
Nhắc lại từ Mệnh đề 12.11 rằng $E = W \oplus W^{\perp}$ (điều này có thể được dễ dàng được hiển thị, ví dụ, bởi xây dựng cơ sở trực chuẩn (orthonormal basis) của $E$ bằng cách sử dụng Gram–Schmidt trực chuẩn hóa quy trình). cùng kết quả cũng nghiệm đúng cho Các không gian Hermite; xem Mệnh đề 14.13. Như warm lên cho chứng minh của Định lý 17.12, cho chúng ta chứng minh rằng mọi tự liên hợp (self-adjoint) ánh xạ trên Không gian Euclid (Euclidean space) có thể được được chéo hóa đối với cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors).

> **Định lý 17.8.** (Định lý phổ (spectral theorem) cho tự liên hợp (self-adjoint) các ánh xạ tuyến tính (linear maps) trên Không gian Euclid (Euclidean space)) Cho trước Không gian Euclid (Euclidean space) $E$ có số chiều $n$, với mọi tự liên hợp (self-adjoint) ánh xạ tuyến tính (linear map) $f$: $E \to E$, có một cơ sở trực chuẩn (orthonormal basis) $(e_{1}, \dots  , e_{n})$ của các vectơ riêng (eigenvectors) của $f$ sao cho ma trận của $f$ w.r.t. cơ sở (cơ sở (basis)) này là ma trận đường chéo (diagonal matrix)
$$\begin{pmatrix} \lambda_{1} & \dots \\ \lambda_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & \lambda_{n} \end{pmatrix} ,$$
Với $\lambda_{i}  \in \mathbb{R}$.

*Chứng minh.* Ta tiến hành bằng quy nạp theo số chiều $n$ của $E$ như sau. Nếu $n = 1$, kết quả là tầm thường. Giả sử bây giờ rằng $n \ge 2$. Từ Mệnh đề 17.6, tất cả các trị riêng (eigenvalues) của $f$ là thực, do đó chọn một số trị riêng (eigenvalue) $\lambda  \in \mathbb{R}$, và cho $w$ là một số vectơ riêng (eigenvector) cho $\lambda$. Bằng cách chia $w$ bởi chuẩn (chuẩn (norm)) của nó, ta có thể giả sử rằng $w$ là unit vectơ. Cho $W$ là không gian con có số chiều $1$ được sinh (spanned) bởi $w$. Rõ ràng, f(W) $\subseteq W$. Ta khẳng định rằng $f(W^{\perp}$) $\subseteq W^{\perp}$, ở đâu $W^{\perp}$ là phần bù trực giao (orthogonal complement) của $W$. Thật vậy, với mọi $v \in W^{\perp}$, nghĩa là, nếu $\langle v, w\rangle = 0$, bởi vì $f$ là tự liên hợp (self-adjoint) và f(w) $= \lambda w$, ta có
$$\langle f(v), w\rangle = \langle v, f(w)\rangle$$
$$= \langle v, \lambda w\rangle$$
$$= \lambda \langle v, w\rangle = 0$$

<!-- PAGE 632 -->
Vì $\langle v, w\rangle = 0$. Vì vậy,
$$f(W^{\perp} ) \subseteq W^{\perp} .$$
Rõ ràng, thu hẹp của $f$ đến $W^{\perp}$ là tự liên hợp (self-adjoint), và ta kết luận bằng cách áp dụng giả thiết quy nạp (induction hypothesis) đến $W^{\perp}$ (có số chiều là $n$ - $1)$. Ta bây giờ đến quay lại đến chuẩn tắc/bình thường các ánh xạ tuyến tính (linear maps). Một của then chốt các điểm trong chứng minh của Định lý 17.8 là rằng ta tìm thấy không gian con $W$ với tính chất rằng f(W) $\subseteq W$ suy ra rằng $f(W^{\perp}$) $\subseteq W^{\perp}$. Nói chung, điều này thực hiện không xảy ra, nhưng chuẩn tắc/bình thường các ánh xạ thỏa mãn mạnh hơn tính chất mà các đảm bảo rằng như vậy không gian con tồn tại. sau đây mệnh đề cung cấp điều kiện rằng sẽ cho phép chúng ta để chỉ ra rằng chuẩn tắc/bình thường ánh xạ tuyến tính (linear map) có thể được được chéo hóa. Nó thực sự nghiệm đúng với mọi ánh xạ tuyến tính (linear map). Ta tìm thấy inspiration cho mệnh đề này trong Berger $[11]$.

> **Mệnh đề 17.9.** Cho trước Không gian Hermite (Hermitian space) $E$, với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$ và bất kỳ
$$subspace W of E, if f(W) \subseteq W, then f^{*} \begin{pmatrix} W^{\perp} \end{pmatrix} \subseteq W^{\perp} . Consequently, if f(W) \subseteq W and$$
$$f^{*} (W) \subseteq W, then f \begin{pmatrix} W^{\perp} \\ then \end{pmatrix} \subseteq W^{\perp} and f^{*} \begin{pmatrix} W^{\perp} \end{pmatrix} \subseteq W^{\perp} .$$

*Chứng minh.* Nếu $u \in W^{\perp}$,
$$\langle w, u\rangle = 0for all w \in W.$$
Tuy nhiên,
$$\langle f(w), u\rangle = \langle w, f^{*} (u)\rangle ,$$
Và f(W) $\subseteq W$ suy ra rằng f(w) $\in W$. Vì $u \in W^{\perp}$, ta thu được
$$0 = \langle f(w), u\rangle = \langle w, f^{*} (u)\rangle ,$$
Mà chỉ ra rằng $\langle w, f^{*} (u)\rangle = 0$ với mọi $w \in W$, nghĩa là, $f^{*} (u) \in W^{\perp}$. Vì vậy, ta có $f^{*} (W^{\perp}$) $\subseteq W^{\perp}$.
$$We just proved that if f(W) \subseteq W, then f^{*} \begin{pmatrix} W^{\perp} \\ f^{**}( \end{pmatrix} \subseteq W^{\perp} . If we also have f^{*} (W) \subseteq W,$$
Thì bằng cách áp dụng ở trên sự kiện đến $f^{*}$, ta thu được $W^{\perp}$) $\subseteq W^{\perp}$, và vì $f^{**} = f$, điều này là chỉ $f(W^{\perp}$) $\subseteq W^{\perp}$, mà chứng minh thứ hai phát biểu của mệnh đề. Rõ ràng là ở trên mệnh đề cũng nghiệm đúng cho Các không gian Euclid. Mặc dù ta là ready để chứng minh rằng với mọi chuẩn tắc/bình thường ánh xạ tuyến tính (linear map) $f$ (trên Không gian Hermite (Hermitian space)) có một cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors) (xem Định lý 17.13 ở dưới), ta bây giờ trả về đến thực Các không gian Euclid.

> **Mệnh đề 17.10.** Nếu $f$: $E \to E$ là ánh xạ tuyến tính (linear map) và $w = u +$ iv là vectơ riêng (eigenvector) của $f_{C}$: $E_{C} \to E_{C}$ cho trị riêng (eigenvalue) $z = \lambda  + i\mu$, ở đâu $u, v \in E$ và $\lambda , \mu  \in \mathbb{R}$, thì
$$f(u) = \lambda u -\mu vandf(v) = \mu u + \lambda v.(*)$$
Hệ quả là,
$$f_{C}(u -iv) = f(u) -if(v) = (\lambda  -i\mu )(u -iv),$$
Mà chỉ ra rằng $\overline{w} = u$ - iv là vectơ riêng (eigenvector) của $f_{C}$ cho $\overline{z} = \lambda$ - $i\mu$.

<!-- PAGE 633 -->

*Chứng minh.* Vì
$$f_{C}(u + iv) = f(u) + if(v)$$
Và
$$f_{C}(u + iv) = (\lambda  + i\mu )(u + iv) = \lambda u -\mu v + i(\mu u + \lambda v),$$
Ta có
$$f(u) = \lambda u -\mu vandf(v) = \mu u + \lambda v.$$
Bằng cách sử dụng sự kiện này, ta có thể chứng minh sau đây mệnh đề.

> **Mệnh đề 17.11.** Cho trước Không gian Euclid (Euclidean space) $E$, với mọi chuẩn tắc/bình thường ánh xạ tuyến tính (linear map) $f$: $E \to E$, nếu $w = u +$ iv là vectơ riêng (eigenvector) của $f_{C}$ liên kết với trị riêng (eigenvalue) $z = \lambda  + i\mu$ (ở đâu $u, v \in E$ và $\lambda , \mu  \in \mathbb{R})$, nếu $\mu  \neq  0$ (i.e., $z$ là không thực) thì $\langle u, v\rangle = 0$ và $\langle u, u\rangle = \langle v, v\rangle$, mà suy ra rằng $u$ và $v$ là độc lập tuyến tính (linearly independent), và nếu $W$ là không gian con được sinh (spanned) bởi $u$ và $v$, thì f(W) $= W$ và $f^{*} (W) = W$. Hơn nữa, đối với (trực giao) cơ sở (basis) $(u, v)$, thu hẹp của $f$ đến $W$ có ma trận
$$\begin{pmatrix} \lambda & \mu \\ -\mu & \lambda \end{pmatrix} .$$
Nếu $\mu  = 0$, thì $\lambda$ là thực trị riêng (eigenvalue) của $f$, và hoặc $u$ hoặc $v$ là vectơ riêng (eigenvector) của $f$ cho $\lambda$. Nếu $W$ là không gian con được sinh (spanned) bởi $u$ nếu $u \neq  0$, hoặc được sinh (spanned) bởi $v \neq  0$ nếu $u = 0$, thì f(W) $\subseteq W$ và $f^{*} (W) \subseteq W$.

*Chứng minh.* Vì $w = u +$ iv là vectơ riêng (eigenvector) của $f_{C}$, theo Định nghĩa nó là khác không, và hoặc $u \neq  0$ hoặc $v \neq  0$. Mệnh đề 17.10 suy ra rằng $u$ - iv là vectơ riêng (eigenvector) của $f_{C}$ cho $\lambda$ - $i\mu$. Nó là dễ để kiểm tra rằng $f_{C}$ là chuẩn tắc/bình thường. Tuy nhiên, nếu $\mu  \neq  0$, thì $\lambda  + i\mu  \neq  \lambda$ - $i\mu$, và từ Mệnh đề 17.4, các vectơ $u +$ iv và $u$ - iv là trực giao w.r.t. $\langle$ -, $-\rangle_{C}$, nghĩa là,
$$\langle u + iv, u -iv\rangle_{C}  = \langle u, u\rangle -\langle v, v\rangle + 2i\langle u, v\rangle = 0.$$
Do đó ta thu được $\langle u, v\rangle = 0$ và $\langle u, u\rangle = \langle v, v\rangle$, và vì $u \neq  0$ hoặc $v \neq  0, u$ và $v$ là độc lập tuyến tính (linearly independent). Vì
$$f(u) = \lambda u -\mu vandf(v) = \mu u + \lambda v$$
Và vì theo Mệnh đề 17.3 $u +$ iv là vectơ riêng (eigenvector) của $f_{C}^{*}$ cho $\lambda$ - $i\mu$, ta có
$$f^{*} (u) = \lambda u + \mu vandf^{*} (v) = -\mu u + \lambda v,$$
Và do đó f(W) $= W$ và $f^{*} (W) = W$, ở đâu $W$ là không gian con được sinh (spanned) bởi $u$ và $v$. Khi $\mu  = 0$, ta có
$$f(u) = \lambda uandf(v) = \lambda v,$$
Và vì $u \neq  0$ hoặc $v \neq  0$, hoặc $u$ hoặc $v$ là vectơ riêng (eigenvector) của $f$ cho $\lambda$. Nếu $W$ là không gian con được sinh (spanned) bởi $u$ nếu u̸ $= 0$, hoặc được sinh (spanned) bởi $v$ nếu $u = 0$, hiển nhiên là f(W) $\subseteq W$ và $f^{*} (W) \subseteq W$. Lưu ý rằng $\lambda  = 0$ là khả dĩ/có thể, và điều này là tại sao $\subseteq$ không thể được thay thế bởi $=$.

<!-- PAGE 634 -->
Bắt đầu của chứng minh của Mệnh đề 17.11 thực sự chỉ ra rằng với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$ tồn tại một không gian con $W$ sao cho f(W) $\subseteq W$, ở đâu $W$ có số chiều $1$ hoặc $2$. Nói chung, nó không’t dường như khả dĩ/có thể để chứng minh rằng $W^{\perp}$ là bất biến dưới $f$. Tuy nhiên, điều này xảy ra khi $f$ là chuẩn tắc/bình thường. Ta có thể cuối cùng chứng minh của ta thứ nhất chính định lý.

> **Định lý 17.12.** (Chính định lý phổ (spectral theorem)) Cho trước Không gian Euclid (Euclidean space) $E$ có số chiều $n$, với mọi chuẩn tắc/bình thường ánh xạ tuyến tính (linear map) $f$: $E \to E$, có một cơ sở trực chuẩn (orthonormal basis) $(e_{1}, \dots  , e_{n})$ sao cho ma trận của $f$ w.r.t. cơ sở (cơ sở (basis)) này là khối ma trận đường chéo (diagonal matrix) của tạo thành
$$\begin{pmatrix} A_{1} & \dots \\ A_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & A_{p} \end{pmatrix}$$
Sao cho mỗi khối $A_{j}$ là hoặc một chiều ma trận (i.e., thực vô hướng (scalar)) hoặc twodimensional ma trận của tạo thành
$$A_{j} = \begin{pmatrix} \lambda_{j} & -\mu_{j} \\ \mu_{j} & \lambda_{j} \end{pmatrix} ,$$
Ở đâu $\lambda_{j} , \mu_{j}  \in \mathbb{R}$, với $\mu_{j}  > 0$.

*Chứng minh.* Ta tiến hành bằng quy nạp theo số chiều $n$ của $E$ như sau. Nếu $n = 1$, kết quả là tầm thường. Giả sử bây giờ rằng $n \ge 2$. Thứ nhất, vì $\mathbb{C}$ là algebraically đóng (i.e., mọi đa thức có nghiệm (root) trong $\mathbb{C})$, ánh xạ tuyến tính (linear map) $f_{C}$: $E_{C} \to E_{C}$ có một số trị riêng (eigenvalue) $z = \lambda  + i\mu$ (ở đâu $\lambda , \mu  \in \mathbb{R})$. Cho $w = u +$ iv là một số vectơ riêng (eigenvector) của $f_{C}$ cho $\lambda  + i\mu$ (ở đâu $u, v \in E)$. Ta có thể bây giờ áp dụng Mệnh đề 17.11. Nếu $\mu  = 0$, thì hoặc $u$ hoặc $v$ là vectơ riêng (eigenvector) của $f$ cho $\lambda  \in \mathbb{R}$. Cho $W$ là không gian con có số chiều $1$ được sinh (spanned) bởi $e_{1} = u/\|u\|$ nếu $u \neq  0$, hoặc bởi $e_{1} = v/\|v\|$ ngược lại. Hiển nhiên là f(W) $\subseteq W$ và $f^{*} (W) W$. trực giao $W^{\perp}$ của $W$ có số chiều $n$ - $1$, và bởi
$$Proposition 17.9, we have f \begin{pmatrix} \subseteq \\ W^{\perp} \\ the \end{pmatrix} \subseteq W^{\perp} . But the restriction of f to W^{\perp} is also normal,$$
Và ta kết luận bằng cách áp dụng giả thiết quy nạp (induction hypothesis) đến $W^{\perp}$. Nếu $\mu  \neq  0$, thì $\langle u, v\rangle = 0$ và $\langle u, u\rangle = \langle v, v\rangle$, và nếu $W$ là không gian con được sinh (spanned) bởi $u/\|u\|$ và $v/\|v\|$, thì f(W) $= W$ và $f^{*} (W) = W$. Ta cũng biết rằng thu hẹp của $f$ đến $W$ có ma trận
$$\begin{pmatrix} \lambda & \mu \\ -\mu & \lambda \end{pmatrix}$$
Đối với cơ sở (basis) $(u/\|u\|, v/\|v\|)$. Nếu $\mu  < 0$, ta cho $\lambda_{1}  = \lambda , \mu_{1}  = -\mu , e_{1} = u/\|u\|$, và $e_{2} = v/\|v\|$. Nếu $\mu  > 0$, ta cho $\lambda_{1}  = \lambda , \mu_{1}  = \mu , e_{1} = v/\|v\|$, và $e_{2} = u/\|u\|$. Trong tất cả các trường hợp, dễ dàng kiểm chứng được rằng ma trận của thu hẹp của $f$ đến $W$ w.r.t. cơ sở trực chuẩn (orthonormal basis) $(e_{1}, e_{2})$ là
$$A_{1} = \begin{pmatrix} \lambda_{1} & -\mu_{1} \\ \mu_{1} & \lambda_{1} \end{pmatrix} ,$$

<!-- PAGE 635 -->
Ở đâu $\lambda_{1} , \mu_{1}  \in \mathbb{R}$, với $\mu_{1}  > 0$. Tuy nhiên, $W^{\perp}$ có số chiều $n -2$, và theo Mệnh đề 17.9,
$$f \begin{pmatrix} W^{\perp} \end{pmatrix} \subseteq W^{\perp} . Since the restriction of f to W^{\perp} is also normal, we conclude by applying$$
Giả thiết quy nạp (induction hypothesis) đến $W^{\perp}$. Sau điều này một cách tương đối khó hoạt động/công trình, ta có thể dễ dàng thu được một số đẹp chuẩn tắc/bình thường các dạng cho các ma trận của tự liên hợp (self-adjoint), phản tự liên hợp (skew-self-adjoint), và trực giao các ánh xạ tuyến tính (linear maps). Tuy nhiên, cho sake của tính đầy đủ (và vì ta có tất cả các công cụ đến do đó thực hiện), ta đi quay lại đến trường hợp của Không gian Hermite (Hermitian space) và chỉ ra rằng chuẩn tắc/bình thường các ánh xạ tuyến tính (linear maps) có thể được được chéo hóa đối với cơ sở trực chuẩn (orthonormal basis). chứng minh là slight tổng quát hóa của chứng minh của Định lý 17.6.

> **Định lý 17.13.** (Định lý phổ (spectral theorem) cho chuẩn tắc/bình thường các ánh xạ tuyến tính (linear maps) trên Không gian Hermite (Hermitian space)) Cho trước Không gian Hermite (Hermitian space) $E$ có số chiều $n$, với mọi chuẩn tắc/bình thường ánh xạ tuyến tính (linear map) $f$: $E \to E$ có một cơ sở trực chuẩn (orthonormal basis) $(e_{1}, \dots  , e_{n})$ của các vectơ riêng (eigenvectors) của $f$ sao cho ma trận của $f$ w.r.t. cơ sở (cơ sở (basis)) này là ma trận đường chéo (diagonal matrix)
$$\begin{pmatrix} \lambda_{1} & \dots \\ \lambda_{2} & \dots \\ \vdots & \vdots & \ddots & \vdots \\ \dots & \lambda_{n} \end{pmatrix} ,$$
Ở đâu $\lambda_{j}  \in \mathbb{C}$.

*Chứng minh.* Ta tiến hành bằng quy nạp theo số chiều $n$ của $E$ như sau. Nếu $n = 1$, kết quả là tầm thường. Giả sử bây giờ rằng $n \ge 2$. Vì $\mathbb{C}$ là algebraically đóng (i.e., mọi đa thức có nghiệm (root) trong $\mathbb{C})$, ánh xạ tuyến tính (linear map) $f$: $E \to E$ có một số trị riêng (eigenvalue) $\lambda  \in \mathbb{C}$, và cho $w$ là một số unit vectơ riêng (eigenvector) cho $\lambda$. Cho $W$ là không gian con có số chiều $1$ được sinh (spanned) bởi $w$. Rõ ràng, f(W) $\subseteq W$. Theo Mệnh đề 17.3, $w$ là vectơ riêng (eigenvector) của $f^{*}$ cho $\overline{\lambda}$, và do đó $f^{*} (W) \subseteq W$. Theo Mệnh đề 17.9, ta cũng có $f(W^{\perp}$) $\subseteq W^{\perp}$. thu hẹp của $f$ đến $W^{\perp}$ là vẫn chuẩn tắc/bình thường, và ta kết luận bằng cách áp dụng giả thiết quy nạp (induction hypothesis) đến $W^{\perp}$ (có số chiều là $n$ - $1)$. Định lý 17.13 suy ra rằng (phức) tự liên hợp (self-adjoint), phản tự liên hợp (skew-self-adjoint), và trực giao các ánh xạ tuyến tính (linear maps) có thể được được chéo hóa đối với cơ sở trực chuẩn (orthonormal basis) của các vectơ riêng (eigenvectors). Trong điều này latter trường hợp, dù, trực giao ánh xạ được gọi là một unita ánh xạ. Mệnh đề 17.5 cũng chỉ ra rằng các trị riêng (eigenvalues) của tự liên hợp (self-adjoint) ánh xạ tuyến tính (linear map) là thực, và Mệnh đề 17.7 chỉ ra rằng các trị riêng (eigenvalues) của skew tự liên hợp (self-adjoint) ánh xạ là thuần túy imaginary hoặc không, và rằng các trị riêng (eigenvalues) của unita ánh xạ có tuyệt đối giá trị $1$.
Nhận xét: Có một điều ngược lại đến Định lý 17.13, cụ thể là, nếu có một cơ sở trực chuẩn (orthonormal basis) $(e_{1}, \dots  , e_{n})$ của các vectơ riêng (eigenvectors) của $f$, thì $f$ là chuẩn tắc/bình thường. Ta để lại dễ chứng minh như một bài tập. Trong mục tiếp theo ta specialize Định lý 17.12 đến tự liên hợp (self-adjoint), phản tự liên hợp (skew-self-adjoint), và trực giao các ánh xạ tuyến tính (linear maps). Do additional cấu trúc, ta thu được nhiều hơn/thêm precise chuẩn tắc/bình thường các dạng.
