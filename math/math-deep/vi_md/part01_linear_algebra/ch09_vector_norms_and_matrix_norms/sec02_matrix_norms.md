# Các chuẩn ma trận


<!-- PAGE 349 -->
Nhận xét: Cho $P$ là $n \times  n$ đối xứng xác định dương (SPD) ma trận. Ta kiểm chứng được ngay rằng ánh xạ $x \mapsto \|x\|_{P}$ cho trước bởi
$$\|x\|_{P} = (x^{\top}Px)^{1/2}$$
$$\mathbb{R}^{n}$$
Là chuẩn (norm) trên được gọi là toàn phương chuẩn (norm). Bằng cách sử dụng một số lồi giải tích/phân tích (L¨owner–John
$$\mathbb{R}^{n}$$
Ellipsoid), nó có thể được được hiển thị rằng bất kỳ chuẩn (norm) $\|\|$ trên có thể được approximated bởi toàn phương chuẩn (norm) trong nghĩa rằng có một toàn phương chuẩn (norm) $\|\|_{P}$ sao cho
$$\sqrt$$
$$\|x\|_{P} \le \|x\|\le \overline{n} \|x\|_{P}for all x \in \mathbb{R}^{n};$$
Xem Boyd và Vandenberghe $[29]$, Mục 8.4.1. Tiếp theo ta sẽ xét các chuẩn trên các ma trận.

## 9.2 Các chuẩn ma trận

Để đơn giản của trình bày, ta sẽ xét các không gian vectơ $M_{n}(\mathbb{R})$ và $M_{n}(\mathbb{C})$ của square $n \times  n$ các ma trận. Hầu hết các kết quả cũng đúng cho các không gian $M_{m,n}(\mathbb{R})$ và $M_{m,n}(\mathbb{C})$ của rectangular $m \times  n$ các ma trận. Vì $n \times  n$ các ma trận có thể được được nhân, ý tưởng đằng sau các chuẩn ma trận là rằng chúng nên behave “tốt” đối với phép nhân ma trận (matrix multiplication).

> **Định nghĩa 9.4.** chuẩn ma trận (matrix norm) $\|\|$ trên không gian của square $n \times  n$ các ma trận trong $M_{n}(K)$, với $K =\mathbb{R}$ hoặc $K =\mathbb{C}$, là chuẩn (norm) trên không gian vectơ (vector space) $M_{n}(K)$, với additional tính chất được gọi là submultiplicativity rằng
$$\|AB\|\le \|A\|\|B\|,$$
Với mọi $A, B \in M_{n}(K)$. chuẩn (norm) trên các ma trận thỏa mãn ở trên tính chất là thường được gọi là submultiplicative chuẩn ma trận (matrix norm). Vì $I^{2} =$ I, từ $\|I\| = \|I^{2}\|\le \|I\|^{2}$, ta thu được $\|I\|\ge 1$, với mọi chuẩn ma trận (matrix norm).
$$Before giving examples of matrix norms, we\mathbb{C} need to review \frac{some}{A} basic definitions about$$
Các ma trận. Cho trước bất kỳ ma trận $A = (a_{ij}) \in M_{m,n}($), liên hợp của $A$ là ma trận sao cho
$$\overline{A}_{ij} =\overline{a}_{ij},1 \le i \le m, 1 \le j \le n.$$
Chuyển vị (transpose) của $A$ là ma trận cỡ $n \times  m$ $A^{\top}$ sao cho
$$A_{ij}^{\top} = a_{ji},1 \le i \le m, 1 \le j \le n.$$
Liên hợp (adjoint) của $A$ là ma trận cỡ $n \times  m$ $A^{*}$ sao cho
$$A^{*}\overline{= (}\overline{A}^{\top}\overline{) = (}\overline{A})^{\top}.$$
Khi $A$ là thực ma trận, $A^{*} = A^{\top}$. ma trận $A \in M_{n}(\mathbb{C})$ là Hermite nếu
$$A^{*}= A.$$

<!-- PAGE 350 -->
Nếu $A$ là thực ma trận $(A \in M_{n}(\mathbb{R}))$, ta nói rằng $A$ là đối xứng nếu
$$A^{\top}= A.$$
Ma trận $A \in M_{n}(\mathbb{C})$ là chuẩn tắc/bình thường nếu
$$AA^{*}= A^{*}A,$$
Và nếu $A$ là thực ma trận, nó là chuẩn tắc/bình thường nếu
$$AA^{\top}= A^{\top}A.$$
Ma trận $U \in M_{n}(\mathbb{C})$ là unita nếu
$$UU^{*} = U^{*} U = I.$$
Thực ma trận $Q \in M_{n}(\mathbb{R})$ là trực giao nếu
$$QQ^{\top}= Q^{\top}Q = I.$$
Cho trước bất kỳ ma trận $A = (a_{ij}) \in M_{n}(\mathbb{C})$, vết (trace) tr() của $A$ là tổng của của nó đường chéo các phần tử
$$\mathrm{tr}(A) = a_{11} + \cdots  + a_{nn}.$$
Nó là dễ để chỉ ra rằng vết (trace) là ánh xạ tuyến tính (linear map), sao cho
$$\mathrm{tr}(\lambda A) = \lambda \mathrm{tr}(A)$$
Và
$$\mathrm{tr}(A + B) = \mathrm{tr}(A) + \mathrm{tr}(B).$$
Hơn thế nữa, nếu $A$ là một ma trận cỡ $m \times  n$ và $B$ là một ma trận cỡ $n \times  m$, nó là không khó để chỉ ra rằng
$$\mathrm{tr}(AB) = \mathrm{tr}(BA).$$
Ta cũng ôn tập/tổng quan các trị riêng (eigenvalues) và các vectơ riêng (eigenvectors). Ta content chính chúng ta với định nghĩa liên quan đến các ma trận. nhiều hơn/thêm tổng quát treatment sẽ là cho trước sau này (xem Chương $15)$.

> **Định nghĩa 9.5.** Cho trước bất kỳ ma trận vuông (square matrix) $A \in M_{n}(\mathbb{C})$, phức số $\lambda  \in \mathbb{C}$ là trị riêng (eigenvalue) của $A$ nếu tồn tại một khác không vectơ $u \in \mathbb{C}^{n}$, sao cho
$$Au = \lambda u.$$
$$\mathbb{C}^{n}$$
Nếu $\lambda$ là trị riêng (eigenvalue) của $A$, thì khác không các vectơ $u \in$ sao cho Au $= \lambda u$ được gọi là các vectơ riêng (eigenvectors) của $A$ liên kết với $\lambda$; cùng với không vectơ, các vectơ riêng (các vectơ riêng (eigenvectors)) này tạo thành
$$\mathbb{C}^{n}$$
Không gian con của được ký hiệu bởi $E_{\lambda}(A)$, và được gọi là không gian riêng (eigenspace) liên kết với $\lambda$.

<!-- PAGE 351 -->
Nhận xét: Lưu ý rằng Định nghĩa 9.5 đòi hỏi vectơ riêng (eigenvector) là khác không. somewhat unfortunate hệ quả của điều này requirement là rằng tập hợp của các vectơ riêng (eigenvectors) là không không gian con, vì không vectơ là missing! Trên dương vế/cạnh, bất cứ khi nào các vectơ riêng (eigenvectors) là liên quan, không có cần đến nói rằng chúng là khác không. Ngược lại, chẵn/ngay cả nếu ta cho phép $0$ là vectơ riêng (eigenvector), trong thứ tự cho vô hướng (scalar) $\lambda$ là trị riêng (eigenvalue), ở đó phải là khác không vectơ $u$ sao cho Au $= \lambda u$. Mà không có điều này thu hẹp, vì A0 $= \lambda 0 = 0$ với mọi $\lambda$, mọi vô hướng (scalar) sẽ là vectơ riêng (eigenvector), mà sẽ tạo định nghĩa của trị riêng (eigenvalue) tầm thường và useless. sự kiện rằng các vectơ riêng (eigenvectors) là khác không là một cách ẩn được sử dụng trong tất cả các đối số/lập luận liên quan đến chúng, do đó nó dường như được ưu tiên hơn (nhưng perhaps không như thanh lịch) đến stipulate rằng các vectơ riêng (eigenvectors) nên là khác không. Nếu $A$ là square thực ma trận $A \in M_{n}(\mathbb{R})$, thì ta thu hẹp Định nghĩa 9.5 đến thực các trị riêng (eigenvalues) $\lambda  \in \mathbb{R}$ và thực các vectơ riêng (eigenvectors). Tuy nhiên, nó nên được lưu ý rằng mặc dù mọi phức ma trận luôn luôn có ít nhất một số phức trị riêng (eigenvalue), thực ma trận có thể không có bất kỳ thực các trị riêng (eigenvalues). Ví dụ, ma trận
$$A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$$
Có phức các trị riêng (eigenvalues) $i$ và $-i$, nhưng không có thực các trị riêng (eigenvalues). Do đó, typically chẵn/ngay cả cho thực các ma trận, ta xét phức các trị riêng (eigenvalues). Nhận thấy rằng $\lambda  \in \mathbb{C}$ là trị riêng (eigenvalue) của $A \bullet$ khi và chỉ khi Au $= \lambda u$ với một số khác không vectơ $u \in \mathbb{C}^{n} \bullet  iff(\lambda$ I -)u $= 0 \bullet$ khi và chỉ khi ma trận $\lambda$ I - $A$ định nghĩa ánh xạ tuyến tính (linear map) mà có khác không hạt nhân (kernel), nghĩa là, $\bullet$ khi và chỉ khi $\lambda$ I - $A$ không khả nghịch. Tuy nhiên, từ Mệnh đề 7.10, $\lambda$ I - $A$ là không khả nghịch khi và chỉ khi
$$\det(\lambda I -A) = 0.$$
Bây giờ $det(\lambda$ I - $A)$ là đa thức của bậc $n$ trong indeterminate $\lambda$, thực ra, của tạo thành
$$\lambda^{n} -\mathrm{tr}(A)\lambda^{n-1} + \cdots  + (-1)^{n}\det(A).$$
Do đó ta xem rằng các trị riêng (eigenvalues) của $A$ là các không điểm (cũng được gọi là các nghiệm) của ở trên đa thức. Vì mọi phức đa thức của bậc $n$ có chính xác $n$ các nghiệm, counted với của chúng bội (multiplicity), ta có kết quả sau định nghĩa:

> **Định nghĩa 9.6.** Cho trước bất kỳ square $n \times  n$ ma trận $A \in M_{n}(\mathbb{C})$, đa thức
$$\det(\lambda I -A) = \lambda^{n} -\mathrm{tr}(A)\lambda^{n-1} + \cdots  + (-1)^{n}\det(A)$$

<!-- PAGE 352 -->
Được gọi là đa thức đặc trưng (characteristic polynomial) của $A$. $n$ (không nhất thiết phân biệt) các nghiệm $\lambda_{1} , \dots  , \lambda_{n}$ của đa thức đặc trưng (characteristic polynomial) là tất cả các trị riêng (eigenvalues) của $A$ và constitute phổ (spectrum) của $A$. Ta cho
$$\rho (A) = \max |\lambda_{i} |$$
$$1\le i\le n$$
Là lớn nhất môđun/độ lớn của các trị riêng (eigenvalues) của $A$, được gọi là bán kính phổ (spectral radius) của $A$. Vì các trị riêng (eigenvalues) $\lambda_{1} , \dots  , \lambda_{n}$ của $A$ là các không điểm của đa thức
$$\det(\lambda I -A) = \lambda^{n} -\mathrm{tr}(A)\lambda^{n-1} + \cdots  + (-1)^{n}\det(A),$$
Ta suy ra (xem Mục 15.1 cho chi tiết) rằng
$$\mathrm{tr}(A) = \lambda_{1}  + \cdots  + \lambda_{n}$$
$$\det(A) = \lambda_{1}  \cdots  \lambda_{n} .$$

> **Mệnh đề 9.7.** Với mọi chuẩn ma trận (matrix norm) $\|\|$ trên $M_{n}(\mathbb{C})$ và với mọi square $n \times  n$ ma trận $A \in M_{n}(\mathbb{C})$, ta có
$$\rho (A) \le \|A\|.$$

*Chứng minh.* Cho $\lambda$ là một số trị riêng (eigenvalue) của $A$ cho mà $|\lambda$ | là cực đại, nghĩa là, sao cho $|\lambda$ | $= \rho (A)$. Nếu $u (\neq  0)$ là bất kỳ vectơ riêng (eigenvector) liên kết với $\lambda$ và nếu $U$ là ma trận cỡ $n \times  n$ có các cột là tất cả $u$, thì Au $= \lambda u$ suy ra
$$AU = \lambda U,$$
Và vì
$$|\lambda | \|U\|= \|\lambda U\|= \|AU\|\le \|A\|\|U\|$$
Và $U \neq  0$, ta có $\|U\|̸ = 0$, và thu được
$$\rho (A) = |\lambda | \le \|A\|,$$
Như đã khẳng định. Mệnh đề 9.7 cũng nghiệm đúng với mọi thực chuẩn ma trận (matrix norm) $\|\|$ trên $M_{n}(\mathbb{R})$ nhưng chứng minh là nhiều hơn/thêm tinh tế và đòi hỏi khái niệm của được cảm sinh chuẩn (norm). Ta chứng minh nó sau cho Định nghĩa 9.8. Hóa ra là nếu $A$ là thực $n \times  n$ ma trận đối xứng (symmetric matrix), thì các trị riêng (eigenvalues) của $A$ là tất cả thực và tồn tại một ma trận trực giao (orthogonal matrix) $Q$ sao cho
$$A = Qdiag(\lambda_{1} , \dots  , \lambda_{n} )Q^{\top},$$
Ở đâu $diag(\lambda_{1} , \dots  , \lambda_{n}$) ký hiệu ma trận có chỉ khác không các phần tử (entries) (nếu bất kỳ) là của nó đường chéo các phần tử (entries), mà là (thực) các trị riêng (eigenvalues) của $A$. Tương tự, nếu $A$ là phức $n \times  n$ Ma trận Hermite (Hermitian matrix), thì các trị riêng (eigenvalues) của $A$ là tất cả thực và tồn tại một ma trận unita (unitary matrix) $U$ sao cho
$$A = Udiag(\lambda_{1} , \dots  , \lambda_{n} )U^{*} ,$$

<!-- PAGE 353 -->
Ở đâu $diag(\lambda_{1} , \dots  , \lambda_{n}$) ký hiệu ma trận có chỉ khác không các phần tử (entries) (nếu bất kỳ) là của nó đường chéo các phần tử (entries), mà là (thực) các trị riêng (eigenvalues) của $A$. Xem Chương $17$ cho chứng minh của các kết quả này. Ta bây giờ trả về đến các chuẩn ma trận. Ta bắt đầu với so-called Chuẩn Frobenius (Frobenius norm), mà là chỉ chuẩn (norm) $\|\|_{2}$ trên $\mathbb{C}^{n2}$, ở đâu ma trận cỡ $n \times  n$ $A$ được quan điểm như vectơ thu được bởi concatenating cùng nhau các hàng (hoặc các cột) của $A$. độc giả nên kiểm tra rằng với mọi $n \times  n$ phức ma trận $A = (a_{ij})$,
$$1/2$$
$$\begin{pmatrix} |a_{ij}|^{2} \end{pmatrix} \sum_{i,j=1}^{n}  =p\overline{\mathrm{tr}(}\overline{A}^{*}\overline{A}\overline{) =} p\overline{\mathrm{tr}(}\overline{AA}^{*}\overline{)}.$$

> **Định nghĩa 9.7.** Chuẩn Frobenius (Frobenius norm) $\|\|_{F}$ được định nghĩa sao cho với mọi square $n \times  n$ ma trận $A \in M_{n}(\mathbb{C})$,
$$1/2$$
$$\|A\|_{F} = \begin{pmatrix} |a_{ij}|^{2} \end{pmatrix} \sum_{i,j=1}^{n}  =p\overline{\mathrm{tr}(}\overline{AA}^{*}\overline{) =} p\overline{\mathrm{tr}(}\overline{A}^{*}\overline{A}\overline{)}.$$
Sau đây mệnh đề chỉ ra rằng Chuẩn Frobenius (Frobenius norm) là chuẩn ma trận (matrix norm) thỏa mãn khác đẹp các tính chất.

> **Mệnh đề 9.8.** Chuẩn Frobenius (Frobenius norm) $\|\|_{F}$ trên $M_{n}(\mathbb{C})$ thỏa mãn các tính chất sau đây:
$(1)$ Nó là chuẩn ma trận (matrix norm); nghĩa là, $\|AB\|_{F} \le \|A\|_{F} \|B\|_{F}$, với mọi $A, B \in M_{n}(\mathbb{C})$.
$(2)$ Nó là unitarily bất biến, mà có nghĩa là với mọi các ma trận unita $U, V$, ta có
$$\|A\|_{F} = \|UA\|_{F} = \|AV \|_{F} = \|UAV \|_{F} .$$
$$\sqrt$$
$(3) p\overline{\rho}\overline{(}\overline{A}^{*}\overline{A}\overline{)} \le \|A\|_{F} \le \overline{n} p\overline{\rho}\overline{(}\overline{A}^{*}\overline{A}\overline{)}$, với mọi $A \in M_{n}(\mathbb{C})$.

*Chứng minh.* $(1)$ chỉ tính chất rằng đòi hỏi chứng minh là sự kiện $\|AB\|_{F} \le \|A\|_{F} \|B\|_{F}$. Điều này suy ra từ Cauchy–Schwarz bất đẳng thức:
$$2$$
$$\|AB\|_{F}^{2} = \sum_{i,j=1}^{n}  \sum_{k=1}^{n}  a_{ik}b_{kj}$$
$$\le \sum_{i,j=1}^{n}  \begin{pmatrix} |a_{ih}|^{2} \end{pmatrix} \sum_{h=1}^{n}  \begin{pmatrix} |b_{kj}|^{2} \end{pmatrix} \sum_{k=1}^{n}$$
$$= \begin{pmatrix} |a_{ih}|^{2} \end{pmatrix} \sum_{i,h=1}^{n}  \begin{pmatrix} |b_{kj}|^{2} \end{pmatrix} \sum_{k,j=1}^{n}  = \|A\|_{F}^{2} \|B\|_{F}^{2} .$$
$(2)$ Ta có
$$\|A\|_{F}^{2} = \mathrm{tr}(AA^{*}) = \mathrm{tr}(AV V^{*} A^{*}) = \mathrm{tr}(AV (AV )^{*}) = \|AV \|_{F}^{2} ,$$
