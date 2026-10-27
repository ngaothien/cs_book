# Các vectơ riêng (eigenvectors) và Các trị riêng (eigenvalues) của Ánh xạ tuyến tính (linear map)


<!-- PAGE 569 -->
Chương $15$ Các vectơ riêng (eigenvectors) và Các trị riêng (eigenvalues) Trong chương này tất cả các không gian vectơ được định nghĩa trên tùy ý trường $K$. Cho sake của concreteness, độc giả có thể safely giả sử rằng $K =\mathbb{R}$ hoặc $K =\mathbb{C}$.

## 15.1 Các vectơ riêng (eigenvectors) và Các trị riêng (eigenvalues) của Ánh xạ tuyến tính (linear map)

Cho trước không gian vectơ hữu hạn chiều $E$, cho $f$: $E \to E$ là bất kỳ ánh xạ tuyến tính (linear map). Nếu bởi luck có một cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $E$ đối với mà $f$ được biểu diễn bởi ma trận đường chéo (diagonal matrix)
$$D = \begin{pmatrix} \lambda_{1} & 0 & \dots & 0 \\ 0 & \lambda_{2} & \ddots & \vdots \\ \vdots & \ddots & \ddots & 0 \\ 0 & \dots & 0 & \lambda_{n} \end{pmatrix} ,$$
Thì action của $f$ trên $E$ là rất đơn giản; trong mọi “hướng” $e_{i}$, ta có
$$f(e_{i}) = \lambda_{i} e_{i}.$$
Ta có thể nghĩ của $f$ như phép biến đổi rằng stretches hoặc shrinks không gian dọc theo hướng $e_{1}, \dots  , e_{n}$ (ít nhất nếu $E$ là thực không gian vectơ (vector space)). Theo các ma trận, ở trên tính chất translates vào sự kiện rằng có một ma trận khả nghịch (invertible matrix) $P$ và ma trận đường chéo (diagonal matrix) $D$ sao cho ma trận $A$ có thể được được nhân tử như
$$A = PDP^{-1} .$$
Khi điều này xảy ra, ta nói rằng $f$ (hoặc $A)$ là chéo hóa được (diagonalizable), $\lambda_{i}$ ’s được gọi là các trị riêng (eigenvalues) của $f$, và $e_{i}’s$ là các vectơ riêng (eigenvectors) của $f$. Ví dụ, ta sẽ xem rằng mọi ma trận đối xứng (symmetric matrix) có thể được được chéo hóa. Không may là, không mọi ma trận có thể được được chéo hóa. Ví dụ, ma trận
$$A_{1} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$
$$569$$

<!-- PAGE 570 -->
Có thể’t được chéo hóa. Đôi khi ma trận không thỏa mãn là chéo hóa được (diagonalizable) bởi vì các trị riêng (các trị riêng (eigenvalues)) của nó thực hiện không thuộc đến trường của các hệ số, chẳng hạn như
$$A_{2} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} ,$$
Có các trị riêng (eigenvalues) là $\pm i$. Điều này là không serious bài toán bởi vì $A_{2}$ có thể được được chéo hóa trên phức các số. Tuy nhiên, $A_{1}$ là “fatal” trường hợp! Thật vậy, các trị riêng (các trị riêng (eigenvalues)) của nó là cả hai $1$ và bài toán là rằng $A_{1}$ thực hiện không có đủ các vectơ riêng (eigenvectors) đến sinh (span) $E$. tiếp theo tốt nhất thing là rằng có một cơ sở (basis) đối với mà $f$ được biểu diễn bởi tam giác trên (upper triangular) ma trận. Trong trường hợp này ta nói rằng $f$ có thể được triangularized, hoặc rằng $f$ là triangularizable. Như ta sẽ xem trong Mục 15.2, nếu tất cả các trị riêng (eigenvalues) của $f$ thuộc đến trường của các hệ số $K$, thì $f$ có thể được triangularized. Đặc biệt, điều này là trường hợp nếu $K =\mathbb{C}$. Bây giờ alternative đến triangularization là đến xét biểu diễn của $f$ đối với hai các cơ sở $(e_{1}, \dots  , e_{n})$ và $(f_{1}, \dots  , f_{n})$, thay vì đơn lẻ cơ sở (basis). Trong trường hợp này, nếu $K = \mathbb{R}$ hoặc $K = \mathbb{C}$, hóa ra là ta có thể chẵn/ngay cả chọn các phần tử này các cơ sở là trực chuẩn, và ta thu được ma trận đường chéo (diagonal matrix) $\Sigma$ với không âm các phần tử (entries), sao cho
$$f(e_{i}) = \sigma_{i} f_{i},1 \le i \le n.$$
Khác không $\sigma_{i}$ ’s là các giá trị kỳ dị (singular values) của $f$, và tương ứng biểu diễn là phân rã giá trị kỳ dị (SVD), hoặc SVD. SVD đóng rất quan trọng vai trò trong các ứng dụng, và sẽ được xét trong chi tiết trong Chương $22$. Trong mục này ta focus trên khả năng của diagonalizing ánh xạ tuyến tính (linear map), và ta giới thiệu relevant các khái niệm đến thực hiện do đó. Cho trước không gian vectơ (vector space) $E$ trên trường $K$, cho id ký hiệu đồng nhất thức ánh xạ trên $E$. khái niệm của trị riêng (eigenvalue) của ánh xạ tuyến tính (linear map) $f$: $E \to E$ được định nghĩa trên vô hạn chiều không gian $E$ là khá tinh tế bởi vì nó không thể được định nghĩa theo các vectơ riêng (eigenvectors) như trong hữu hạn chiều trường hợp. bài toán là rằng ánh xạ $\lambda$ id $-f$ (với $\lambda  \in \mathbb{C})$ có thể là noninvertible (bởi vì nó là không toàn ánh (surjective)) và vẫn chưa đơn ánh (injective). Trong hữu hạn số chiều điều này không thể xảy ra, do đó cho đến khi further notice ta giả sử rằng $E$ là của hữu hạn số chiều $n$.

> **Định nghĩa 15.1.** Cho trước bất kỳ không gian vectơ (vector space) $E$ của hữu hạn số chiều $n$ và bất kỳ ánh xạ tuyến tính (linear map) $f$: $E \to E$, vô hướng (scalar) $\lambda  \in K$ được gọi là một trị riêng (eigenvalue), hoặc thực sự/đúng đắn giá trị, hoặc characteristic giá trị của $f$ nếu tồn tại một khác không vectơ $u \in E$ sao cho
$$f(u) = \lambda u.$$
Tương đương, $\lambda$ là trị riêng (eigenvalue) của $f$ nếu Ker $(\lambda$ id - $f)$ là không tầm thường (i.e., Ker $(\lambda$ id - $f) \neq  {0})$ khi và chỉ khi $\lambda$ id-f là không khả nghịch (điều này là ở đâu sự kiện rằng $E$ là hữu hạn chiều được sử dụng; ánh xạ tuyến tính (linear map) từ $E$ đến chính nó là đơn ánh (injective) khi và chỉ khi nó là khả nghịch). vectơ $u \in E$ được gọi là một vectơ riêng (eigenvector), hoặc thực sự/đúng đắn vectơ, hoặc characteristic vectơ của $f$ nếu $u \neq  0$ và nếu tồn tại một $\lambda  \in K$ sao cho
$$f(u) = \lambda u;$$

<!-- PAGE 571 -->
Vô hướng (scalar) $\lambda$ là thì trị riêng (eigenvalue), và ta nói rằng $u$ là vectơ riêng (eigenvector) liên kết với $\lambda$. Cho trước bất kỳ trị riêng (eigenvalue) $\lambda  \in K$, không tầm thường không gian con Ker $(\lambda$ id - $f)$ bao gồm của tất cả các vectơ riêng (eigenvectors) liên kết với $\lambda$ cùng với không vectơ; không gian con này được ký hiệu bởi $E_{\lambda}(f)$, hoặc $E(\lambda , f)$, hoặc chẵn/ngay cả bởi $E_{\lambda}$, và được gọi là không gian riêng (eigenspace) liên kết với $\lambda$, hoặc thực sự/đúng đắn không gian con liên kết với $\lambda$. Lưu ý rằng phân biệt các vectơ riêng (eigenvectors) có thể tương ứng với cùng trị riêng (eigenvalue), nhưng phân biệt các trị riêng (eigenvalues) tương ứng với rời nhau các tập hợp của các vectơ riêng (eigenvectors).
Nhận xét: Như ta emphasized trong nhận xét sau đây Định nghĩa 9.5, ta đòi hỏi vectơ riêng (eigenvector) là khác không. Điều này requirement dường như đến có nhiều hơn/thêm benefits hơn inconveniences, chẵn/ngay cả dù nó có thể được xét somewhat inelegant bởi vì tập hợp tất cả các vectơ riêng (eigenvectors) liên kết với trị riêng (eigenvalue) là không không gian con vì không vectơ là excluded. tiếp theo mệnh đề chỉ ra rằng các trị riêng (eigenvalues) của ánh xạ tuyến tính (linear map) $f$: $E \to E$ là các nghiệm của đa thức liên kết với $f$.

> **Mệnh đề 15.1.** Cho $E$ là bất kỳ không gian vectơ (vector space) của hữu hạn số chiều $n$ và cho $f$ là bất kỳ ánh xạ tuyến tính (linear map) $f$: $E \to E$. các trị riêng (eigenvalues) của $f$ là các nghiệm (trong $K)$ của đa thức
$$\det(\lambda  id -f).$$

*Chứng minh.* vô hướng (scalar) $\lambda  \in K$ là trị riêng (eigenvalue) của $f$ khi và chỉ khi tồn tại một vectơ $u \neq  0$ trong $E$ sao cho
$$f(u) = \lambda u$$
Khi và chỉ khi
$$(\lambda  id -f)(u) = 0$$
$iff(\lambda$ id - $f)$ là không khả nghịch khi và chỉ khi, theo Mệnh đề 7.13,
$$\det(\lambda  id -f) = 0.$$
Xét theo importance của đa thức $det(\lambda$ id-f), ta có kết quả sau định nghĩa.

> **Định nghĩa 15.2.** Cho trước bất kỳ không gian vectơ (vector space) $E$ có số chiều $n$, với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$, đa thức $P_{f}(X) = \chi_{f} (X) =$ det(X id - $f)$ được gọi là đa thức đặc trưng (characteristic polynomial) của $f$. Với mọi ma trận vuông (square matrix) $A$, đa thức $P_{A}(X) = \chi_{A} (X) =$ det(XI - $A)$ được gọi là đa thức đặc trưng (characteristic polynomial) của $A$. Lưu ý rằng ta đã encountered đa thức đặc trưng (characteristic polynomial) trong Mục 7.7; xem Định nghĩa 7.9.

<!-- PAGE 572 -->
Cho trước bất kỳ cơ sở (basis) $(e_{1}, \dots  , e_{n})$, nếu $A =$ M(f) là ma trận của $f$ w.r.t. $(e_{1}, \dots  , e_{n})$, ta có thể tính đa thức đặc trưng (characteristic polynomial) $\chi_{f} (X) =$ det(X id - $f)$ của $f$ bởi expanding sau đây định thức (determinant):
$$X -a_{1 1}-a_{1 2}\dots -a_{1n}$$
$$-a_{2 1}X -a_{2 2}\dots -a_{2n}$$
$$\det(XI -A) =\vdots \vdots \ddots \vdots .$$
$$-a_{n1}-a_{n2}\dots X -a_{n n}$$
Nếu ta expand định thức (định thức (determinant)) này, ta tìm rằng
$$\chi_{A} (X) = \det(XI -A) = X^{n}-(a_{1 1} + \cdots  + a_{n n})X^{n-1}+ \cdots  + (-1)^{n}\det(A).$$
Tổng tr() $= a_{1 1} +\cdots +a_{n n}$ của đường chéo các phần tử của $A$ được gọi là vết (trace) của $A$. Vì ta được chứng minh trong Mục 7.7 rằng đa thức đặc trưng (characteristic polynomial) chỉ phụ thuộc vào ánh xạ tuyến tính (linear map) $f$, ở trên chỉ ra rằng tr() có cùng giá trị với mọi các ma trận $A$ biểu diễn $f$. Do đó, vết (trace) của ánh xạ tuyến tính (linear map) là xác định tốt (well-defined); ta có tr(f) $=$ tr() với mọi ma trận $A$ biểu diễn $f$.
Nhận xét: đa thức đặc trưng (characteristic polynomial) của ánh xạ tuyến tính (linear map) đôi khi được định nghĩa như det(f - $X$ id). Vì
$$\det(f -X id) = (-1)^{n}\det(X id -f),$$
Điều này làm cho về cơ bản không có difference nhưng phiên bản det(X id - $f)$ có nhỏ advantage rằng hệ số của $X^{n}$ là $+1$. Nếu ta viết $\chi_{A} (X) =$ det(XI - $A) = X^{n}$ - $\tau_{1} (A)X^{n-1} + \cdots  + (-1)^{k}\tau_{k} (A)X^{n-k} + \cdots  + (-1)^{n}\tau_{n} (A)$, thì ta chỉ được chứng minh rằng
$$\tau_{1} (A) = \mathrm{tr}(A)and\tau_{n} (A) = \det(A).$$
Nó là cũng khả dĩ/có thể đến biểu diễn $\tau_{k} (A)$ theo các định thức của nhất định submatrices của $A$. Với mọi khác rỗng được thứ tự tập con, $I \subseteq {1, \dots  , n}$, nói $I = {i_{1} < \cdots  < i_{k}}$, cho $A_{I,I}$ là $k \times  k$ ma trận con của $A$ có cột thứ $j$ bao gồm của các phần tử $a_{ihij}$, ở đâu $h = 1, \dots  , k$. Tương đương, $A_{I,I}$ là ma trận thu được từ $A$ bởi thứ nhất chọn các cột có các chỉ số thuộc đến I, và thì các hàng có các chỉ số cũng thuộc đến I. Thì nó có thể được được hiển thị rằng
$$\tau_{k} (A) = \sum_{\subseteq {1,...,n}  \det(A_{I,I});$$
$$I}$$
$$I={i1,...,ik}$$
$$i1<\cdot \cdot \cdot <ik$$

<!-- PAGE 573 -->
Xem Jacobson $[101]$, Mục 3.10, chỉ sau Công thức $(33)$. Nếu tất cả các nghiệm, $\lambda_{1} , \dots  , \lambda_{n}$, của đa thức det(XI $-A)$ thuộc đến trường $K$, thì ta có thể viết
$$\chi_{A} (X) = \det(XI -A) = (X -\lambda_{1} ) \cdots  (X -\lambda_{n} ),$$
Ở đâu một số của $\lambda_{i}$ ’s có thể xuất hiện nhiều hơn một lần. Hệ quả là, $\chi_{A} (X) =$ det(XI - $A) = X^{n}$ - $\sigma_{1} (\lambda )X^{n-1} + \cdots  + (-1)^{k}\sigma_{k} (\lambda )X^{n-k} + \cdots  + (-1)^{n}\sigma_{n} (\lambda$), ở đâu
$$\sigma_{k} (\lambda ) = \sum_{\subseteq {1,...,n}  \prod_{}i\in I}  \lambda_{i} ,$$
$$I$$
$$|I|=k$$
Thứ $k$ sơ cấp đối xứng đa thức (hoặc hàm) của $\lambda_{i}$ ’s, ở đâu $\lambda  = (\lambda_{1} , \dots  , \lambda_{n}$). sơ cấp đối xứng đa thức $\sigma_{k} (\lambda$) là thường được ký hiệu $E_{k}(\lambda$), nhưng điều này ký hiệu có thể là confusing trong context của tuyến tính đại số. Cho $n = 5$, sơ cấp đối xứng các đa thức được liệt kê ở dưới:
$$\sigma_{0} (\lambda ) = 1$$
$$\sigma_{1} (\lambda ) = \lambda_{1}  + \lambda_{2}  + \lambda_{3}  + \lambda_{4}  + \lambda_{5}$$
$$\sigma_{2} (\lambda ) = \lambda_{1} \lambda_{2}  + \lambda_{1} \lambda_{3}  + \lambda_{1} \lambda_{4}  + \lambda_{1} \lambda_{5}  + \lambda_{2} \lambda_{3}  + \lambda_{2} \lambda_{4}  + \lambda_{2} \lambda_{5}$$
$$+ \lambda_{3} \lambda_{4}  + \lambda_{3} \lambda_{5}  + \lambda_{4} \lambda_{5}$$
$$\sigma_{3} (\lambda ) = \lambda_{3} \lambda_{4} \lambda_{5}  + \lambda_{2} \lambda_{4} \lambda_{5}  + \lambda_{2} \lambda_{3} \lambda_{5}  + \lambda_{2} \lambda_{3} \lambda_{4}  + \lambda_{1} \lambda_{4} \lambda_{5}$$
$$+ \lambda_{1} \lambda_{3} \lambda_{5}  + \lambda_{1} \lambda_{3} \lambda_{4}  + \lambda_{1} \lambda_{2} \lambda_{5}  + \lambda_{1} \lambda_{2} \lambda_{4}  + \lambda_{1} \lambda_{2} \lambda_{3}$$
$$\sigma_{4} (\lambda ) = \lambda_{1} \lambda_{2} \lambda_{3} \lambda_{4}  + \lambda_{1} \lambda_{2} \lambda_{3} \lambda_{5}  + \lambda_{1} \lambda_{2} \lambda_{4} \lambda_{5}  + \lambda_{1} \lambda_{3} \lambda_{4} \lambda_{5}  + \lambda_{2} \lambda_{3} \lambda_{4} \lambda_{5}$$
$$\sigma_{5} (\lambda ) = \lambda_{1} \lambda_{2} \lambda_{3} \lambda_{4} \lambda_{5} .$$
Vì
$$\chi_{A} (X) = X^{n}-\tau_{1} (A)X^{n-1}+ \cdots  + (-1)^{k}\tau_{k} (A)X^{n-k}+ \cdots  + (-1)^{n}\tau_{n} (A)$$
$$= X^{n}-\sigma_{1} (\lambda )X^{n-1}+ \cdots  + (-1)^{k}\sigma_{k} (\lambda )X^{n-k}+ \cdots  + (-1)^{n}\sigma_{n} (\lambda ),$$
Ta có
$$\sigma_{k} (\lambda ) = \tau_{k} (A),k = 1, \dots  , n,$$
Và đặc biệt, tích của các trị riêng (eigenvalues) của $f$ bằng det() $=$ det(f), và tổng của các trị riêng (eigenvalues) của $f$ bằng vết (trace) tr() $=$ tr(f), của $f$; cho record,
$$\mathrm{tr}(f) = \lambda_{1}  + \cdots  + \lambda_{n}$$
$$\det(f) = \lambda_{1}  \cdots  \lambda_{n} ,$$
Ở đâu $\lambda_{1} , \dots  , \lambda_{n}$ là các trị riêng (eigenvalues) của $f$ (và $A)$, ở đâu một số của $\lambda_{i}$ ’s có thể xuất hiện nhiều hơn một lần. Đặc biệt, $f$ là không khả nghịch khi và chỉ khi nó admits $0$ có trị riêng (eigenvalue) (vì $f$ là suy biến khi và chỉ khi $\lambda_{1}  \cdots  \lambda_{n}  =$ det(f) $= 0)$.

<!-- PAGE 574 -->
Nhận xét: Tùy thuộc trên trường $K$, đa thức đặc trưng (characteristic polynomial) $\chi_{A} (X) =$ det(XI - $A)$ có thể hoặc có thể không có các nghiệm trong $K$. Điều này motivates xét algebraically đóng các trường, mà là các trường $K$ sao cho mọi đa thức với các hệ số trong $K$ có tất cả của nó nghiệm (root) trong $K$. Ví dụ, trên $K =\mathbb{R}$, không mọi đa thức có thực các nghiệm. Nếu ta xét ma trận
$$A = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} ,$$
Thì đa thức đặc trưng (characteristic polynomial) det(XI - $A)$ có không có thực các nghiệm trừ khi $\theta  = k\pi$. Tuy nhiên, trên trường $\mathbb{C}$ của phức các số, mọi đa thức có các nghiệm. Ví dụ, ma trận ở trên có các nghiệm cos $\theta  \pm  i$ sin $\theta  = e^{\pm i\theta}$.
Nhận xét: Nó là khả dĩ/có thể để chỉ ra rằng mọi ánh xạ tuyến tính (linear map) $f$ trên phức không gian vectơ (vector space) $E$ phải có một số (phức) trị riêng (eigenvalue) mà không có có recourse đến các định thức (và đa thức đặc trưng (characteristic polynomial)). Cho $n =$ dim(E), chọn bất kỳ khác không vectơ $u \in E$, và xét dãy
$$u, f(u), f^{2} (u), \dots  , f^{n} (u).$$
Vì ở trên dãy có $n + 1$ các vectơ và $E$ có số chiều $n$, các vectơ này phải là phụ thuộc tuyến tính (linearly dependent), do đó có một số phức các số $c_{0}, \dots  , c_{m}$, không tất cả không, sao cho
$$c_{0}f^{m} (u) + c_{1}f^{m-1} (u) + \cdots  + c_{m}u = 0,$$
Ở đâu $m \le n$ là lớn nhất số nguyên sao cho hệ số của $f^{m} (u)$ là khác không $(m$ phải exits vì ta có không tầm thường tuyến tính dependency). Bây giờ bởi vì $field\mathbb{C}$ là algebraically đóng, đa thức
$$c_{0}X^{m}+ c_{1}X^{m-1}+ \cdots  + c_{m}$$
Có thể được viết dưới dạng tích của tuyến tính các nhân tử như
$$c_{0}X^{m}+ c_{1}X^{m-1}+ \cdots  + c_{m} = c_{0}(X -\lambda_{1} ) \cdots  (X -\lambda_{m} )$$
Với một số phức các số $\lambda_{1} , \dots  , \lambda_{m}  \in \mathbb{C}$, không nhất thiết phân biệt. Nhưng khi đó vì $c_{0} \neq  0$,
$$c_{0}f^{m} (u) + c_{1}f^{m-1} (u) + \cdots  + c_{m}u = 0$$
Là tương đương đến
$$(f -\lambda_{1}  id) \circ \cdots  \circ (f -\lambda_{m}  id)(u) = 0.$$
Nếu tất cả các ánh xạ tuyến tính (linear maps) $f$ - $\lambda_{i}$ id đã là đơn ánh (injective), thì $(f$ - $\lambda_{1}$ id) $\circ \cdots  \circ (f$ - $\lambda_{m}$ id) sẽ là đơn ánh (injective), contradicting sự kiện rằng $u \neq  0$. Vì vậy, một số ánh xạ tuyến tính (linear map) $f$ - $\lambda_{i}$ id phải có không tầm thường hạt nhân (kernel), mà có nghĩa là tồn tại một $v \neq  0$ sao cho
$$f(v) = \lambda_{i} v;$$
Rằng là, $\lambda_{i}$ là một số trị riêng (eigenvalue) của $f$ và $v$ là một số vectơ riêng (eigenvector) của $f$. Như đẹp như ở trên lập luận là, nó thực hiện không cung cấp phương pháp cho việc tìm các trị riêng (eigenvalues) của $f$, và chẵn/ngay cả nếu ta ưu tiên tránh các định thức như nhiều như khả dĩ/có thể, ta là forced đến deal với đa thức đặc trưng (characteristic polynomial) det(X id - $f)$.

<!-- PAGE 575 -->

> **Định nghĩa 15.3.** Cho $A$ là một ma trận cỡ $n \times  n$ trên trường $K$. Giả sử rằng tất cả các nghiệm của đa thức đặc trưng (characteristic polynomial) $\chi_{A} (X) =$ det(XI - $A)$ của $A$ thuộc đến $K$, mà có nghĩa là ta có thể viết
$$\det(XI -A) = (X -\lambda_{1} )^{k1}\cdots  (X -\lambda_{m} )^{km},$$
Ở đâu $\lambda_{1} , \dots  , \lambda_{m}  \in K$ là phân biệt các nghiệm của det(XI - $A)$ và $k_{1} + \cdots  + k_{m} = n$. số nguyên $k_{i}$ được gọi là đại số bội (multiplicity) của trị riêng (eigenvalue) $\lambda_{i}$, và số chiều của không gian riêng (eigenspace) $E_{\lambda i} = Ker(\lambda_{i}$ I - $A)$ được gọi là hình học bội (multiplicity) của $\lambda_{i}$. Ta ký hiệu đại số bội (multiplicity) của $\lambda_{i}$ bởi $alg(\lambda_{i}$), và của nó hình học bội (multiplicity) bởi $geo(\lambda_{i}$). Theo Định nghĩa, tổng của đại số các bội bằng $n$, nhưng tổng của hình học các bội có thể được chặt nhỏ hơn.

> **Mệnh đề 15.2.** Cho $A$ là một ma trận cỡ $n\times n$ trên trường $K$ và giả sử rằng tất cả các nghiệm của đa thức đặc trưng (characteristic polynomial) $\chi_{A} (X) =$ det(XI $-A)$ của $A$ thuộc đến $K$. Với mọi trị riêng (eigenvalue) $\lambda_{i}$ của $A$ trong $K$, hình học bội (multiplicity) của $\lambda_{i}$ là luôn luôn ít hơn hoặc bằng của nó đại số bội (multiplicity), nghĩa là,
$$geo(\lambda_{i} ) \le alg(\lambda_{i} ).$$

*Chứng minh.* để xem điều này, nếu $n_{i}$ là số chiều của không gian riêng (eigenspace) $E_{\lambda i}$ liên kết với trị riêng (eigenvalue) $\lambda_{i}$, ta có thể tạo thành cơ sở (basis) của $K^{n}$ thu được bởi chọn cơ sở (basis) của $E_{\lambda i}$ và completing điều này độc lập tuyến tính (linearly independent) họ đến cơ sở (basis) của $K^{n}$. Đối với điều này mới cơ sở (basis), ma trận của chúng ta là của tạo thành
$$A'= \begin{pmatrix} \lambda_{i} I_{ni} & B \\ 0 & D \end{pmatrix} ,$$
Và đơn giản định thức (determinant) phép tính chỉ ra rằng
$$- - -  -$$
$$\det(XIA) = \det(XIA') = (X\lambda_{i} )^{ni}\det(XI_{n-ni}D).$$
Vì vậy, $(X -\lambda_{i} )^{ni}$ chia hết đa thức đặc trưng (characteristic polynomial) của ', và do đó, đa thức đặc trưng (characteristic polynomial) của $A$. Suy ra rằng $n_{i}$ là ít hơn hoặc bằng đại số bội (multiplicity) của $\lambda_{i}$. sau đây mệnh đề chỉ ra thú vị tính chất của các không gian riêng (eigenspace).

> **Mệnh đề 15.3.** Cho $E$ là bất kỳ không gian vectơ (vector space) của hữu hạn số chiều $n$ và cho $f$ là bất kỳ ánh xạ tuyến tính (linear map). Nếu $u_{1}, \dots  , u_{m}$ là các vectơ riêng (eigenvectors) liên kết với đôi một phân biệt các trị riêng (eigenvalues) $\lambda_{1} , \dots  , \lambda_{m}$ của $f$ (trong $K)$, thì họ $(u_{1}, \dots  , u_{m})$ là độc lập tuyến tính (linearly independent).

*Chứng minh.* Giả sử rằng $(u_{1}, \dots  , u_{m})$ là phụ thuộc tuyến tính (linearly dependent). Thì tồn tại $\mu_{1} , \dots  , \mu_{k}  \in K$ sao cho
$$\mu_{1} u_{i1} + \cdots  + \mu_{k} u_{ik} = 0,$$
Ở đâu $1 \le k \le m, \mu_{i}$ ̸ $= 0$ với mọi $i, 1 \le i \le k, {i_{1}, \dots  , i_{k}} \subseteq {1, \dots  , m}$, và không có thực sự/đúng đắn họ con của $(u_{i1}, \dots  , u_{ik})$ là phụ thuộc tuyến tính (linearly dependent) (nói cách khác, ta xét dependency quan hệ với $k$ tối tiểu). Áp dụng $f$ đến điều này dependency quan hệ, ta thu được
$$\mu_{1} \lambda_{i1} u_{i1} + \cdots  + \mu_{k} \lambda_{ik} u_{ik} = 0,$$

<!-- PAGE 576 -->
Và nếu ta nhân ban đầu dependency quan hệ bởi $\lambda_{i1}$ và trừ nó từ ở trên, ta thu được
$$\mu_{2} (\lambda_{i2}  -\lambda_{i1} )u_{i2} + \cdots  + \mu_{k} (\lambda_{ik}  -\lambda_{i1} )u_{ik} = 0,$$
Mà là không tầm thường tuyến tính dependency trong số thực sự/đúng đắn họ con của $(u_{i1}, \dots  , u_{ik})$ vì $\lambda_{j}$ là tất cả phân biệt và $\mu_{i}$ là khác không, một mâu thuẫn. Như hệ quả của Mệnh đề 15.3 ta có kết quả sau kết quả.

> **Hệ quả 15.4.** Nếu $\lambda_{1} , \dots  , \lambda_{m}$ là tất cả đôi một phân biệt các trị riêng (eigenvalues) của $f$ (trong $K)$, ở đâu $m \le n)$, ta có tổng trực tiếp (direct sum)
$$E_{\lambda1} \oplus \cdots  \oplus E_{\lambda m}$$
Của các không gian riêng (eigenspace) $E_{\lambda i}$. Không may là, nó là không luôn luôn trường hợp rằng
$$E = E_{\lambda1} \oplus \cdots  \oplus E_{\lambda m}.$$
Khi nó thực hiện là captured bởi sau đây định nghĩa.

> **Định nghĩa 15.4.** Nếu tất cả phân biệt các trị riêng (eigenvalues) $\lambda_{1} , \dots  , \lambda_{m}$ của $f$ thuộc đến $K$ và
$$E = E_{\lambda1} \oplus \cdots  \oplus E_{\lambda m},$$
Ta nói rằng $f$ là chéo hóa được (diagonalizable) (và tương tự với mọi ma trận liên kết với $f)$. Thật vậy, chọn cơ sở (basis) trong mỗi $E_{\lambda i}$, ta thu được ma trận mà là ma trận đường chéo (diagonal matrix) bao gồm của các trị riêng (eigenvalues), mỗi $\lambda_{i}$ xảy ra số của lần bằng số chiều của $E_{\lambda i}$. Điều này xảy ra nếu đại số bội (multiplicity) và hình học bội (multiplicity) của mọi trị riêng (eigenvalue) là bằng nhau. Đặc biệt, khi đa thức đặc trưng (characteristic polynomial) có $n$ phân biệt các nghiệm trong $K$, thì hình học bội (multiplicity) và hình học bội (multiplicity) của mọi trị riêng (eigenvalue) bằng $1$, do đó $f$ là chéo hóa được (diagonalizable). Nó có thể cũng được hiển thị rằng các ma trận đối xứng có thực các trị riêng (eigenvalues) và có thể được được chéo hóa. Cho âm ví dụ, ta để lại nó như bài tập để chỉ ra rằng ma trận
$$M = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$
Không thể được chéo hóa, chẵn/ngay cả dù $1$ là trị riêng (eigenvalue). bài toán là rằng không gian riêng (eigenspace) của $1$ chỉ có số chiều $1$. ma trận
$$A = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$$
Không thể được chéo hóa hoặc, bởi vì nó có không có thực các trị riêng (eigenvalues), trừ khi $\theta  = k\pi$. Tuy nhiên, trên trường của phức các số, nó có thể được được chéo hóa.
