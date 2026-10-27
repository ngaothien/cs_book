# Các bài tập


<!-- PAGE 522 -->

## 13.3 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ Tính đối xứng (hoặc phép đối xứng (reflection)) đối với $F$ và song song đến $G. \bullet$ Trực giao tính đối xứng (hoặc phép đối xứng (reflection)) đối với $F$ và song song đến $G$; các phép đối xứng, flips. $\bullet$ Siêu phẳng (hyperplane) các phép đối xứng và Householder các ma trận. $\bullet  A$ then chốt sự kiện về các phép đối xứng (Mệnh đề 13.2). $\bullet$ Phân rã QR (QR-decomposition) theo Householder các phép biến đổi (Định lý 13.4).

## 13.4 Các bài tập

Bài toán 13.1. $(1)$ Cho trước unit vectơ (-sin $\theta$, cos $\theta$), chứng minh rằng Ma trận Householder được xác định bởi vectơ (-sin $\theta$, cos $\theta$) là
$$\begin{pmatrix} \cos 2\theta & \sin 2\theta \\ \sin 2\theta & -\cos 2\theta \end{pmatrix} .$$
Cho hình học interpretation (i.e., tại sao lựa chọn (-sin $\theta$, cos $\theta$)?).
$(2)$ Cho trước bất kỳ ma trận
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} ,$$
Chứng minh rằng có một Ma trận Householder $H$ sao cho $AH$ là tam giác dưới (lower triangular), i.e.,
$$AH = \begin{pmatrix} a' & 0 \\ c' & d' \end{pmatrix}$$
$$\mathbb{R}$$
Với một số ', c', d' $\in$.
Bài toán 13.2. Cho trước Không gian Euclid (Euclidean space) $E$ có số chiều $n$, nếu $h$ là phép đối xứng (reflection) về một số siêu phẳng (hyperplane) trực giao đến khác không vectơ $u$ và $f$ là bất kỳ phép đẳng cự (isometry), chứng minh rằng $f \circ h \circ f^{-1}$ là phép đối xứng (reflection) về siêu phẳng (hyperplane) trực giao đến f(u).
Bài toán 13.3. $(1)$ Cho trước ma trận
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} ,$$
Chứng minh rằng có Householder các ma trận $G, H$ sao cho
$$GAH = \begin{pmatrix} \cos \theta & \sin \theta \\ \sin \theta & -\cos \theta \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix} = D,$$

<!-- PAGE 523 -->
Ở đâu $D$ là ma trận đường chéo (diagonal matrix), khi và chỉ khi sau đây các phương trình đúng:
$$(b + c) \cos(\theta  + \phi ) = (a -d) \sin(\theta  + \phi ),$$
$$(c -b) \cos(\theta  -\phi ) = (a + d) \sin(\theta  -\phi ).$$
$(2)$ Thảo luận solvability của hệ. Xét sau đây các trường hợp: Trường hợp $1: a$ - $d = a + d = 0$. Trường hợp 2a: $a$ - $d = b + c = 0, a + d \neq  0$. Trường hợp 2b: $a$ - $d = 0, b + c \neq  0, a + d \neq  0$. Trường hợp 3a: $a + d = c$ - $b = 0, a$ - $d \neq  0$. Trường hợp 3b: $a + d = 0, c$ - $b \neq  0, a$ - $d \neq  0$. Trường hợp $4: a + d \neq  0, a$ - $d \neq  0$. Chỉ ra rằng nghiệm trong trường hợp này là
$$$$
$$\theta  = \frac{1}{2} arctan \begin{pmatrix} b \\ + c \\ ba -d \\ + c \end{pmatrix} + arctan \begin{pmatrix} c \\ -b \\ ca + d \\ b \end{pmatrix} ,$$
$$$$
$$\phi  = \frac{1}{2} arctan \begin{pmatrix} a -d \end{pmatrix} -arctan \begin{pmatrix} - \\ a + d \end{pmatrix} .$$
Nếu $b = 0$, chỉ ra rằng thảo luận là đơn giản hơn: basically, xét $c = 0$ hoặc $c \neq  0$.
$(3)$ Biểu diễn everything theo $u =$ cot $\theta$ và $v =$ cot $\phi$, chỉ ra rằng các phương trình trong $(2)$ trở thành
$$(b + c)(uv -1) = (u + v)(a -d),$$
$$(c -b)(uv + 1) = (-u + v)(a + d).$$
Bài toán 13.4. Cho $A$ là $n \times  n$ thực ma trận khả nghịch (invertible matrix).
$(1)$ Chứng minh rằng $A^{\top}A$ là đối xứng xác định dương (SPD).
$(2)$ Sử dụng Nhân tử hóa Cholesky (Cholesky factorization) $A^{\top}A = R^{\top}R$ với $R$ tam giác trên (upper triangular) với dương đường chéo các phần tử (entries) để chứng minh rằng $Q = AR^{-1}$ là trực giao, sao cho $A = QR$ là Nhân tử hóa QR (QR-factorization) của $A$.
Bài toán 13.5. Sửa đổi hàm houseqr sao cho nó áp dụng đến một ma trận cỡ $m \times  n$ với $m \ge n$, đến produce $m \times  n$ tam giác trên (upper-triangular) ma trận có cuối cùng $m$ - $n$ các hàng là các không điểm.
Bài toán 13.6. mục đích của bài toán này là để chứng minh rằng cho trước bất kỳ tự liên hợp (self-adjoint) ánh xạ tuyến tính (linear map) $f$: $E \to E$ (i.e., sao cho $f^{*} = f)$, ở đâu $E$ là Không gian Euclid (Euclidean space) có số chiều $n \ge 3$, cho trước cơ sở trực chuẩn (orthonormal basis) $(e_{1}, \dots  , e_{n})$, có $n$ - $2$ các phép đẳng cự $h_{i}$, siêu phẳng (hyperplane) các phép đối xứng hoặc đồng nhất thức, sao cho ma trận của
$$h_{n-2} \circ \cdots  \circ h_{1} \circ f \circ h_{1} \circ \cdots  \circ h_{n-2}$$

<!-- PAGE 524 -->
Là đối xứng ma trận ba đường chéo (tridiagonal matrix).
$(1)$ Chứng minh rằng với mọi phép đẳng cự (isometry) $f$: $E \to E$, ta có $f = f^{*} = f^{-1}$ khi và chỉ khi $f \circ f =$ id. Chứng minh rằng nếu $f$ và $h$ là tự liên hợp (self-adjoint) các ánh xạ tuyến tính (linear maps) $(f^{*} = f$ và $h^{*} = h)$, thì $h \circ f \circ h$ là tự liên hợp (self-adjoint) ánh xạ tuyến tính (linear map).
$(2)$ Cho $V_{k}$ là không gian con được sinh (spanned) bởi $(e_{k+1}, \dots  , e_{n})$. Tiến hành bởi quy nạp. Cho base trường hợp, tiến hành như sau. Cho
$$f(e_{1}) = a_{1}^{0}e_{1} + \cdots  + a_{n}^{0}e_{n},$$
Và cho
$$r_{1,2} =

$a_{2}^{0}e_{2} + \cdots  + a_{n}^{0}e_{n}$

.$$ Find an isometry $h_{1}$ (phép đối xứng (reflection) hoặc id) sao cho
$$h_{1}(f(e_{1}) -a_{1}^{0}e_{1}) = r_{1,2} e_{2}.$$
Nhận thấy rằng
$$w_{1} = r_{1,2} e_{2} + a_{1}^{0}e_{1} -f(e_{1}) \in V_{1},$$
Và chứng minh rằng $h_{1}(e_{1}) = e_{1}$, sao cho
$$h_{1} \circ f \circ h_{1}(e_{1}) = a_{1}^{0}e_{1} + r_{1,2} e_{2}.$$
Cho $f_{1} = h_{1} \circ f \circ h_{1}$. Giả sử bởi quy nạp rằng
$$f_{k} = h_{k} \circ \cdots  \circ h_{1} \circ f \circ h_{1} \circ \cdots  \circ h_{k}$$
Có ma trận ba đường chéo (tridiagonal matrix) sai khác hàng thứ $k$ và cột, $1 \le k \le n$ - $3$, cho
$$f_{k}(e_{k+1}) = a_{k}^{k}e_{k} + a_{k+1}^{k}e_{k+1} + \cdots  + a_{n}^{k}e_{n},$$
Và cho
$$r_{k+1, k+2} =

$a_{k+2}^{k}e_{k+2} + \cdots  + a_{n}^{k}e_{n}$

.$$ Find an isometry $h_{k+1}$ (phép đối xứng (reflection) hoặc id) sao cho
$$h_{k+1}(f_{k}(e_{k+1}) -a_{k}^{k}e_{k} -a_{k+1}^{k}e_{k+1}) = r_{k+1, k+2} e_{k+2}.$$
Nhận thấy rằng
$$w_{k+1} = r_{k+1, k+2} e_{k+2} + a_{k}^{k}e_{k} + a_{k+1}^{k}e_{k+1} -f_{k}(e_{k+1}) \in V_{k+1},$$
Và chứng minh rằng $h_{k+1}(e_{k}) = e_{k}$ và $h_{k+1}(e_{k+1}) = e_{k+1}$, sao cho
$$h_{k+1} \circ f_{k} \circ h_{k+1}(e_{k+1}) = a_{k}^{k}e_{k} + a_{k+1}^{k}e_{k+1} + r_{k+1, k+2} e_{k+2}.$$

<!-- PAGE 525 -->
Cho $f_{k+1} = h_{k+1} \circ f_{k} \circ h_{k+1}$, và hoàn tất chứng minh.
$(3)$ Chứng minh rằng cho trước bất kỳ đối xứng ma trận cỡ $n\times n$ $A$, có n-2 các ma trận $H_{1}, \dots  , H_{n-2}$, Householder các ma trận hoặc đồng nhất thức, sao cho
$$B = H_{n-2} \cdots  H_{1}AH_{1} \cdots  H_{n-2}$$
Là đối xứng ma trận ba đường chéo (tridiagonal matrix).
$(4)$ Viết máy tính bài toán quy hoạch cài đặt ở trên phương pháp.
Bài toán 13.7. Nhắc lại từ Bài toán 6.6 rằng một ma trận cỡ $n \times  n$ $H$ là trên Hessenberg nếu $h_{jk} = 0$ với mọi $(j, k)$ sao cho $j$ - $k \ge 0$. Thích nghi chứng minh của Bài toán 13.6 để chứng minh rằng cho trước bất kỳ ma trận cỡ $n \times n$ $A$, có $n -2 \ge 1$ các ma trận $H_{1}, \dots  , H_{n-2}$, Householder các ma trận hoặc đồng nhất thức, sao cho
$$B = H_{n-2} \cdots  H_{1}AH_{1} \cdots  H_{n-2}$$
Là trên Hessenberg.
Bài toán 13.8. mục đích của bài toán này là để chứng minh rằng cho trước bất kỳ ánh xạ tuyến tính (linear map) $f$: $E \to E$, ở đâu $E$ là Không gian Euclid (Euclidean space) có số chiều $n \ge 2$, cho trước cơ sở trực chuẩn (orthonormal basis) $(e_{1}, \dots  , e_{n})$, có các phép đẳng cự $g_{i}, h_{i}$, siêu phẳng (hyperplane) các phép đối xứng hoặc đồng nhất thức, sao cho ma trận của
$$g_{n} \circ \cdots  \circ g_{1} \circ f \circ h_{1} \circ \cdots  \circ h_{n}$$
Là thấp hơn bidiagonal ma trận, mà có nghĩa là khác không các phần tử (entries) (nếu bất kỳ) là trên chính descending đường chéo và trên đường chéo ở dưới nó.
$(1)$ Cho $U_{k}'$ là không gian con được sinh (spanned) bởi $(e_{1}, \dots  , e_{k})$ và $U_{k}''$ là không gian con được sinh (spanned) bởi $(e_{k+1}, \dots  , e_{n}), 1 \le k \le n$ - $1$. Tiến hành bởi quy nạp Cho base trường hợp, tiến hành như sau. Cho $v_{1} = f^{*} (e_{1})$ và $r_{1,1} = \|v_{1}\|$. Tìm phép đẳng cự (isometry) $h_{1}$ (phép đối xứng (reflection) hoặc id) sao cho
$$h_{1}(f^{*} (e_{1})) = r_{1,1}e_{1}.$$
Nhận thấy rằng $h_{1}(f^{*} (e_{1})) \in U_{1}'$, sao cho
$$\langle h_{1}(f^{*} (e_{1})), e_{j}\rangle = 0$$
Với mọi $j, 2 \le j \le n$, và kết luận rằng
$$\langle e_{1}, f \circ h_{1}(e_{j})\rangle = 0$$
Với mọi $j, 2 \le j \le n$. Tiếp theo cho
$$u_{1} = f \circ h_{1}(e_{1}) = u_{1}' + u_{1}'',$$
Ở đâu $u_{1}' \in U_{1}'$ và $u_{1}'' \in U_{1}''$, và cho $r_{2,1} = \|u_{1}''\|$. Tìm phép đẳng cự (isometry) $g_{1}$ (phép đối xứng (reflection) hoặc id) sao cho
$$g_{1}(u_{1}'') = r_{2,1}e_{2}.$$

<!-- PAGE 526 -->
Chỉ ra rằng $g_{1}(e_{1}) = e_{1}$,
$$g_{1} \circ f \circ h_{1}(e_{1}) = u_{1}' + r_{2,1}e_{2},$$
Và rằng
$$\langle e_{1}, g_{1} \circ f \circ h_{1}(e_{j})\rangle = 0$$
Với mọi $j, 2 \le j \le n$. Tại kết thúc/cuối của điều này giai đoạn, chỉ ra rằng $g_{1} \circ f \circ h_{1}$ có ma trận sao cho tất cả các phần tử (entries) trên của nó hàng thứ nhất ngoại trừ perhaps thứ nhất là không, và rằng tất cả các phần tử (entries) trên cột thứ nhất, ngoại trừ perhaps thứ nhất hai, là không. Giả sử bởi quy nạp rằng một số các phép đẳng cự $g_{1}, \dots  , g_{k}$ và $h_{1}, \dots  , h_{k}$ có đã được tìm thấy, hoặc các phép đối xứng hoặc đồng nhất thức, và sao cho
$$f_{k} = g_{k} \circ \cdots  \circ g_{1} \circ f \circ h_{1} \cdots  \circ h_{k}$$
Có ma trận mà là thấp hơn bidiagonal sai khác và bao gồm cả hàng và cột $k$, ở đâu $1 \le k \le n$ - $2$. Cho
$$v_{k+1} = f_{k}^{*} (e_{k+1}) = v_{k+1}' + v_{k+1}'',$$
Ở đâu $v_{k+1}' \in U_{k}'$ và $v_{k+1}'' \in U_{k}''$, và cho $r_{k+1, k+1} =$

$v_{k+1}''$

. Tìm phép đẳng cự (isometry) $h_{k+1}$ (phép đối xứng (reflection) hoặc id) sao cho
$$h_{k+1}(v_{k+1}'') = r_{k+1, k+1}e_{k+1}.$$
Chỉ ra rằng nếu $h_{k+1}$ là phép đối xứng (reflection), thì $U_{k}'  \subseteq H_{k+1}$, ở đâu $H_{k+1}$ là siêu phẳng (hyperplane) định nghĩa phép đối xứng (reflection) $h_{k+1}$. Suy ra rằng $h_{k+1}(v_{k+1}') = v_{k+1}'$, và rằng
$$h_{k+1}(f_{k}^{*} (e_{k+1})) = v_{k+1}' + r_{k+1, k+1}e_{k+1}.$$
Nhận thấy rằng $h_{k+1}(f_{k}^{*} (e_{k+1})) \in U_{k+1}'$, sao cho
$$\langle h_{k+1}(f_{k}^{*} (e_{k+1})), e_{j}\rangle = 0$$
Với mọi $j, k + 2 \le j \le n$, và do đó,
$$\langle e_{k+1}, f_{k} \circ h_{k+1}(e_{j})\rangle = 0$$
Với mọi $j, k + 2 \le j \le n$. Tiếp theo cho
$$u_{k+1} = f_{k} \circ h_{k+1}(e_{k+1}) = u_{k+1}' + u_{k+1}'',$$
Ở đâu $u_{k+1}' \in U_{k+1}'$ và $u_{k+1}'' \in U_{k+1}''$, và cho $r_{k+2, k+1} =$

$u_{k+1}''$

. Tìm phép đẳng cự (isometry) $g_{k+1}$ (phép đối xứng (reflection) hoặc id) sao cho
$$g_{k+1}(u_{k+1}'') = r_{k+2, k+1}e_{k+2}.$$
Chỉ ra rằng nếu $g_{k+1}$ là phép đối xứng (reflection), thì $U_{k+1}'  \subseteq G_{k+1}$, ở đâu $G_{k+1}$ là siêu phẳng (hyperplane) định nghĩa phép đối xứng (reflection) $g_{k+1}$. Suy ra rằng $g_{k+1}(e_{i}) = e_{i}$ với mọi $i, 1 \le i \le k + 1$, và rằng
$$g_{k+1} \circ f_{k} \circ h_{k+1}(e_{k+1}) = u_{k+1}' + r_{k+2, k+1}e_{k+2}.$$

<!-- PAGE 527 -->
Vì bởi giả thiết quy nạp (induction hypothesis),
$$\langle e_{i}, f_{k} \circ h_{k+1}(e_{j})\rangle = 0$$
Với mọi $i, j, 1 \le i \le k + 1, k + 2 \le j \le n$, và vì $g_{k+1}(e_{i}) = e_{i}$ với mọi $i, 1 \le i \le k + 1$, kết luận rằng
$$\langle e_{i}, g_{k+1} \circ f_{k} \circ h_{k+1}(e_{j})\rangle = 0$$
Với mọi $i, j, 1 \le i \le k + 1, k + 2 \le j \le n$. Hoàn tất chứng minh.

<!-- PAGE 528 -->
