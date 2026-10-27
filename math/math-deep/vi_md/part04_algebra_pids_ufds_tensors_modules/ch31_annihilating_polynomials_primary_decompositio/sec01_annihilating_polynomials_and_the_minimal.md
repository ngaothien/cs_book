# Các đa thức triệt tiêu và Đa thức tối tiểu (minimal polynomial)


<!-- PAGE 1105 -->
Ở đâu $\nu_{i}  = 1$ hoặc $\nu_{i}  = 0$; xem Định lý 31.16. Như hệ quả ta thu được Dạng Jordan (Jordan form); mà liên quan đến các ma trận của tạo thành
$$J_{r}(\lambda ) = \begin{pmatrix} \lambda & 1 & 0 & \cdots & 0 \\ 0 & \lambda & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \ddots & \vdots \\ 0 & 0 & 0 & \ddots & 1 \\ 0 & 0 & 0 & \lambda \end{pmatrix} ,$$
$$\cdots$$
Được gọi là Các khối Jordan; xem Định lý 31.17.

## 31.1 Các đa thức triệt tiêu và Tối tiểu Poly-

$$nomial$$
Cho trước ánh xạ tuyến tính (linear map) $f$: $E \to E$, nó là dễ để kiểm tra rằng tập hợp Ann(f) của các đa thức rằng annihilate $f$ là lý tưởng (ideal). Hơn nữa, khi $E$ là hữu hạn chiều, Cayley–Hamilton Định lý suy ra rằng Ann(f) là không không lý tưởng (ideal). Vì vậy, theo Mệnh đề 30.10, tồn tại duy nhất một chuẩn hóa (monic) đa thức $m_{f}$ rằng sinh ra Ann(f). Các kết quả từ Chương $30$, especially về ước chung lớn nhất (gcd)’s của các đa thức, sẽ đến handy.

> **Định nghĩa 31.1.** Nếu $f$: $E \to E$ là ánh xạ tuyến tính (linear map) trên không gian vectơ hữu hạn chiều $E$, duy nhất chuẩn hóa (monic) đa thức $m_{f}(X)$ rằng sinh ra lý tưởng (ideal) Ann(f) của các đa thức mà annihilate $f$ (linh hóa tử (annihilator) của $f)$ được gọi là đa thức tối tiểu (minimal polynomial) của $f$. đa thức tối tiểu (minimal polynomial) $m_{f}$ của $f$ là chuẩn hóa (monic) đa thức của nhỏ nhất bậc rằng annihilates $f$. Do đó, đa thức tối tiểu (minimal polynomial) chia hết đa thức đặc trưng (characteristic polynomial) $\chi_{f}$, và $deg(m_{f}) \ge 1$. Để đơn giản của ký hiệu, ta thường viết $m$ thay vì của $m_{f}$. Nếu $A$ là bất kỳ ma trận cỡ $n \times  n$, tập hợp Ann() của các đa thức rằng annihilate $A$ là tập hợp của các đa thức
$$p(X) = a_{0}X^{d}+ a_{1}X^{d-1}+ \cdots  + a_{d-1}X + a_{d}$$
Sao cho
$$a_{0}A^{d}+ a_{1}A^{d-1}+ \cdots  + a_{d-1}A + a_{d}I = 0.$$
Rõ ràng là Ann() là khác không lý tưởng (ideal) và của nó duy nhất chuẩn hóa (monic) phần tử sinh được gọi là đa thức tối tiểu (minimal polynomial) của $A$. Ta kiểm tra ngay lập tức rằng nếu $Q$ là ma trận khả nghịch (invertible matrix), thì $A$ và $Q^{-1}AQ$ có cùng đa thức tối tiểu (minimal polynomial). Cũng, nếu $A$ là ma trận của $f$ đối với một số cơ sở (basis), thì $f$ và $A$ có cùng đa thức tối tiểu (minimal polynomial). các không điểm (trong $K)$ của đa thức tối tiểu (minimal polynomial) của $f$ và các trị riêng (eigenvalues) của $f$ (trong $K)$ là intimately related.

> **Mệnh đề 31.1.** Cho $f$: $E \to E$ là ánh xạ tuyến tính (linear map) trên một số không gian vectơ hữu hạn chiều $E$. Thì $\lambda  \in K$ là không của đa thức tối tiểu (minimal polynomial) $m_{f}(X)$ của $f$ khi và chỉ khi $\lambda$ là trị riêng (eigenvalue) của $f$

<!-- PAGE 1106 -->
Khi và chỉ khi $\lambda$ là không của $\chi_{f} (X)$. Vì vậy, tối tiểu và characteristic các đa thức có cùng các không điểm (trong $K)$, ngoại trừ cho các bội.

*Chứng minh.* Thứ nhất giả sử rằng $m(\lambda$) $= 0$ (với $\lambda  \in K$, và viết $m$ thay vì của $m_{f})$. Nếu do đó, bằng cách sử dụng đa thức phép chia, $m$ có thể được được nhân tử như
$$m = (X -\lambda )q,$$
Với deg(q) $<$ deg(m). Vì $m$ là đa thức tối tiểu (minimal polynomial), q(f)̸ $= 0$, do đó tồn tại một khác không vectơ $v \in E$ sao cho $u =$ q(f)(v)̸ $= 0$. Nhưng khi đó, bởi vì $m$ là đa thức tối tiểu (minimal polynomial),
$$0 = m(f)(v)$$
$$= (f -\lambda id)(q(f)(v))$$
$$= (f -\lambda id)(u),$$
Mà chỉ ra rằng $\lambda$ là trị riêng (eigenvalue) của $f$. Ngược lại, giả sử rằng $\lambda  \in K$ là trị riêng (eigenvalue) của $f$. Điều này có nghĩa là với một số $u \neq  0$, ta có f(u) $= \lambda u$. Bây giờ nó là dễ để chỉ ra rằng
$$m(f)(u) = m(\lambda )u,$$
Và vì $m$ là đa thức tối tiểu (minimal polynomial) của $f$, ta có m(f)(u) $= 0$, do đó $m(\lambda )u = 0$, và vì $u \neq  0$, ta phải có $m(\lambda$) $= 0$.

> **Mệnh đề 31.2.** Cho $f$: $E \to E$ là ánh xạ tuyến tính (linear map) trên một số không gian vectơ hữu hạn chiều $E$. Nếu $f$ chéo hóa được (diagonalizable), thì của nó đa thức tối tiểu (minimal polynomial) là tích của phân biệt các nhân tử của bậc $1$.

*Chứng minh.* Nếu ta giả sử rằng $f$ là chéo hóa được (diagonalizable), thì các trị riêng (các trị riêng (eigenvalues)) của nó là tất cả trong $K$, và nếu $\lambda_{1} , \dots  , \lambda_{k}$ là phân biệt các trị riêng (eigenvalues) của $f$, và thì theo Mệnh đề 31.1, đa thức tối tiểu (minimal polynomial) $m$ của $f$ phải là tích của các lũy thừa của các đa thức $(X$ - $\lambda_{i}$). Thực sự, ta khẳng định rằng
$$m = (X -\lambda_{1} ) \cdots  (X -\lambda_{k} ).$$
Cho điều này ta chỉ có để chỉ ra rằng $m$ annihilates $f$. Tuy nhiên, với mọi vectơ riêng (eigenvector) $u$ của $f$, một của các ánh xạ tuyến tính (linear maps) $f$ - $\lambda_{i}$ id sends $u$ đến $0$, do đó
$$m(f)(u) = (f -\lambda_{1} id) \circ \cdots  \circ (f -\lambda_{k} id)(u) = 0.$$
Vì $E$ được sinh (spanned) bởi các vectơ riêng (eigenvectors) của $f$, ta kết luận rằng
$$m(f) = 0.$$
Hóa ra là điều ngược lại của Mệnh đề 31.2 là đúng, nhưng điều này sẽ lấy little hoạt động/công trình để thiết lập nó.
