# Phân rã QR (QR-decomposition) Bằng cách sử dụng Householder Các ma trận


<!-- PAGE 512 -->
$$s(u) = vu$$
$$H$$
$$v-u$$
$$Figure 13.3: In \mathbb{R}^{3}, the (hyper)plane perpendicular to v -u reflects u onto v.$$

## 13.2 Phân rã QR (QR-decomposition) Bằng cách sử dụng Householder Các ma trận

Thứ nhất ta phát biểu kết quả geometrically. Khi translated theo Householder các ma trận, ta thu được sự kiện advertised trước đó rằng mọi ma trận (không nhất thiết khả nghịch) có Phân rã QR (QR-decomposition).

> **Mệnh đề 13.3.** Cho $E$ là không tầm thường Không gian Euclid (Euclidean space) có số chiều $n$. Với mọi cơ sở trực chuẩn (orthonormal basis) $(e_{1}, \dots , e_{n})$ và với mọi bộ $n$ của các vectơ $(v_{1}, \dots , v_{n})$, có một dãy của $n$ các phép đẳng cự $h_{1}, \dots  , h_{n}$ sao cho $h_{i}$ là siêu phẳng (hyperplane) phép đối xứng (reflection) hoặc đồng nhất thức, và nếu $(r_{1}, \dots  , r_{n})$ là các vectơ cho trước bởi
$$r_{j} = h_{n} \circ \cdots  \circ h_{2} \circ h_{1}(v_{j}),$$
Thì mọi $r_{j}$ là tổ hợp tuyến tính (linear combination) của các vectơ $(e_{1}, \dots  , e_{j}), 1 \le j \le n$. Tương đương, ma trận $R$ có các cột là các thành phần của $r_{j}$ trên cơ sở (basis) $(e_{1}, \dots  , e_{n})$ là tam giác trên (upper triangular) ma trận. Hơn nữa, $h_{i}$ có thể được được chọn sao cho đường chéo các phần tử (entries) của $R$ là không âm.

*Chứng minh.* Ta tiến hành bằng quy nạp theo $n$. Cho $n = 1$, ta có $v_{1} = \lambda e_{1}$ với một số $\lambda  \in \mathbb{R}$. Nếu $\lambda  \ge 0$, ta cho $h_{1} =$ id, khác nếu $\lambda  < 0$, ta cho $h_{1} =$ -id, phép đối xứng (reflection) về gốc. Cho $n \ge 2$, ta thứ nhất có để tìm $h_{1}$. Cho
$$r_{1,1} = \|v_{1}\|.$$

<!-- PAGE 513 -->
Nếu $v_{1} = r_{1,1}e_{1}$, ta cho $h_{1} =$ id. Ngược lại, tồn tại duy nhất một siêu phẳng (hyperplane) phép đối xứng (reflection) $h_{1}$ sao cho
$$h_{1}(v_{1}) = r_{1,1} e_{1},$$
Được định nghĩa sao cho
$$2  \cdot$$
$$h_{1}(u) = u - \frac{(u w_{1})}{\|w_{1}\|^{2}} w_{1}$$
Với mọi $u \in E$, ở đâu
$$w_{1} = r_{1,1} e_{1} -v_{1}.$$
Ánh xạ $h_{1}$ là phép đối xứng (reflection) về siêu phẳng (hyperplane) $H_{1}$ trực giao đến vectơ $w_{1} = r_{1,1} e_{1}$ - $v_{1}$. Xem Hình 13.4. Đặt
$$vH$$
$$11$$
$$e$$
$$2$$
$$re$$
$$1,11$$
$$Figure 13.4: The construction of h_{1} in Proposition 13.3.$$
$$r_{1} = h_{1}(v_{1}) = r_{1,1} e_{1},$$
Hiển nhiên là $r_{1}$ thuộc đến không gian con được sinh (spanned) bởi $e_{1}$, và $r_{1,1} = \|v_{1}\|$ là không âm. Tiếp theo giả sử rằng ta có tìm thấy $k$ các ánh xạ tuyến tính (linear maps) $h_{1}, \dots  , h_{k}$, siêu phẳng (hyperplane) các phép đối xứng hoặc đồng nhất thức, ở đâu $1 \le k \le n$ - $1$, sao cho nếu $(r_{1}, \dots  , r_{k})$ là các vectơ cho trước bởi
$$r_{j} = h_{k} \circ \cdots  \circ h_{2} \circ h_{1}(v_{j}),$$
Thì mọi $r_{j}$ là tổ hợp tuyến tính (linear combination) của các vectơ $(e_{1}, \dots  , e_{j}), 1 \le j \le k$. Xem Hình 13.5. các vectơ $(e_{1}, \dots  , e_{k})$ tạo thành cơ sở (basis) cho không gian con được ký hiệu bởi $U_{k}'$, các vectơ $(e_{k+1}, \dots  , e_{n})$ tạo thành cơ sở (basis) cho không gian con được ký hiệu bởi $U_{k}''$, các không gian con $U_{k}'$ và $U_{k}''$ là trực giao, và $E = U_{k}'  \oplus U_{k}''$. Cho
$$u_{k+1} = h_{k} \circ \cdots  \circ h_{2} \circ h_{1}(v_{k+1}).$$
Ta có thể viết
$$u_{k+1} = u_{k+1}' + u_{k+1}'',$$

<!-- PAGE 514 -->
$$e directione direction$$
$$33$$
$$h$$
$$1$$
$$v$$
$$2$$
$$\overline{v}\overline{e direction}\overline{v}\overline{e direction}$$
$$\overline{1}\overline{2} r1\overline{2}$$
$$1$$
$$e direction1e direction$$
$$1$$
$$Figure 13.5: The construction of r_{1} = h_{1}(v_{1}) in Proposition 13.3.$$
Ở đâu $u_{k+1}' \in U_{k}'$ và $u_{k+1}'' \in U_{k}''$. Xem Hình 13.6. Cho
$$r_{k+1,k+1} = \|u_{k+1}''\|.$$
Nếu $u_{k+1}'' = r_{k+1,k+1} e_{k+1}$, ta cho $h_{k+1} =$ id. Ngược lại, tồn tại duy nhất một siêu phẳng (hyperplane) phép đối xứng (reflection) $h_{k+1}$ sao cho
$$h_{k+1}(u_{k+1}'') = r_{k+1,k+1} e_{k+1},$$
Được định nghĩa sao cho
$$2  \cdot$$
$$h_{k+1}(u) = u - \frac{(u w_{k+1})}{\|w_{k+1}\|^{2}} w_{k+1}$$
Với mọi $u \in E$, ở đâu
$$w_{k+1} = r_{k+1,k+1} e_{k+1} -u_{k+1}''.$$
Ánh xạ $h_{k+1}$ là phép đối xứng (reflection) về siêu phẳng (hyperplane) $H_{k+1}$ trực giao đến vectơ $w_{k+1} = r_{k+1,k+1} e_{k+1}-u_{k+1}''$. Tuy nhiên, vì $u_{k+1}'', e_{k+1} \in U_{k}''$ và $U_{k}'$ là trực giao đến $U_{k}''$, không gian con $U_{k}'$ được chứa trong $H_{k+1}$, và do đó, các vectơ $(r_{1}, \dots  , r_{k})$ và $u_{k+1}'$, mà thuộc đến $U_{k}'$, là bất biến dưới $h_{k+1}$. Điều này chứng tỏ rằng
$$h_{k+1}(u_{k+1}) = h_{k+1}(u_{k+1}') + h_{k+1}(u_{k+1}'') = u_{k+1}' + r_{k+1,k+1} e_{k+1}$$
Là tổ hợp tuyến tính (linear combination) của $(e_{1}, \dots  , e_{k+1})$. Đặt
$$r_{k+1} = h_{k+1}(u_{k+1}) = u_{k+1}' + r_{k+1,k+1} e_{k+1},$$
Vì $u_{k+1} = h_{k} \circ \cdots  \circ h_{2} \circ h_{1}(v_{k+1})$, vectơ
$$r_{k+1} = h_{k+1} \circ \cdots  \circ h_{2} \circ h_{1}(v_{k+1})$$
Là tổ hợp tuyến tính (linear combination) của $(e_{1}, \dots  , e_{k+1})$. Xem Hình 13.7. hệ số của $r_{k+1}$ trên $e_{k+1}$ là $r_{k+1,k+1} = \|u_{k+1}''\|$, mà là không âm. Điều này kết luận quy nạp bước, và do đó chứng minh.

<!-- PAGE 515 -->
$$e direction$$
$$e direction3$$
$$3$$
$$h(v)$$
$$h(v12$$
$$12)v$$
$$2$$
$$\overline{u}\overline{‘’}\overline{e direction}\overline{2}$$
$$\overline{e direction} 2u‘$$
$$\overline{2} 2$$
$$e direction1$$
$$e direction$$
$$2$$

![Figure 13.6](../../assets/ch13/fig_13_6.png)

**Hình 13.6:** cách xây dựng của $u_{2} = h_{1}(v_{2})$ và phân rã của nó như $u_{2} = u_{2}' + u_{2}''$.
Các nhận xét:
$(1)$ Vì mọi $h_{i}$ là siêu phẳng (hyperplane) phép đối xứng (reflection) hoặc đồng nhất thức,
$$\rho  = h_{n} \circ \cdots  \circ h_{2} \circ h_{1}$$
Là phép đẳng cự (isometry).
$(2)$ Nếu ta cho phép âm đường chéo các phần tử (entries) trong $R$, cuối cùng phép đẳng cự (isometry) $h_{n}$ có thể được bỏ qua.
$(3)$ Thay vì của chọn $r_{k,k} = \|u_{k}''\|$, mà có nghĩa là
$$w_{k} = r_{k,k} e_{k} -u_{k}'',$$
Ở đâu $1 \le k \le n$, nó có thể được ưu tiên hơn đến chọn $r_{k,k} = -\|u_{k}''\|$ nếu điều này làm cho $\|w_{k}\|^{2}$ lớn hơn, trong mà trường hợp
$$w_{k} = r_{k,k} e_{k} + u_{k}''.$$
Thật vậy, vì định nghĩa của $h_{k}$ liên quan đến phép chia bởi $\|w_{k}\|^{2}$, nó là desirable để tránh phép chia bởi rất nhỏ các số.
$(4)$ phương pháp cũng áp dụng đến bất kỳ bộ $m$ của các vectơ $(v_{1}, \dots  , v_{m})$, với $m \le n$. Thì $R$ là tam giác trên (upper triangular) $m \times  m$ ma trận và $Q$ là một ma trận cỡ $n \times  m$ với trực giao các cột $(Q^{\top}Q = I_{m})$. Ta để lại định thức con (minor) adjustments đến phương pháp như một bài tập đến độc giả Mệnh đề 13.3 một cách trực tiếp cho ta Phân rã QR (QR-decomposition) theo Householder các phép biến đổi (xem Strang $[175, 176]$, Golub và Van Loan $[83]$, Trefethen và Bau $[182]$, Kincaid và Cheney $[105]$, hoặc Ciarlet $[41])$.

<!-- PAGE 516 -->
$$e direction3$$
$$u‘’$$
$$2$$
$$\overline{h}\overline{(u}\overline{‘’}\overline{)}\overline{e direction} 2$$
$$e direction22$$
$$2$$
$$e direction1$$
$$e direction3$$
$$h(v2)$$
$$1$$
$$\overline{u}\overline{‘}\overline{e direction}$$
$$e direction\overline{2} 2$$
$$2h h(v2)$$
$$21$$
$$e direction1$$
$$Figure 13.7: The construction of h_{2} and r_{2} = h_{2} \circ h_{1}(v_{2}) in Proposition 13.3.$$

> **Định lý 13.4.** Với mọi thực $n \times  n$ ma trận $A$, có một dãy $H_{1}, \dots , H_{n}$ của các ma trận, ở đâu mỗi $H_{i}$ là hoặc Ma trận Householder hoặc đồng nhất thức, và tam giác trên (upper triangular) ma trận $R$ sao cho
$$R = H_{n} \cdots  H_{2}H_{1}A.$$
Như hệ quả, có một cặp của các ma trận $Q, R$, ở đâu $Q$ là trực giao và $R$ là tam giác trên (upper triangular), sao cho $A = QR$ (Phân rã QR (QR-decomposition) của $A)$. Hơn nữa, $R$ có thể được được chọn sao cho của nó đường chéo các phần tử (entries) là không âm.

*Chứng minh.* cột thứ $j$ của $A$ có thể được được quan điểm như vectơ $v_{j}$ trên cơ sở chính tắc (canonical basis) $(e_{1}, \dots  , e_{n}) \mathbb{E}^{n}$ của (ở đâu $(e_{j})_{i} = 1$ nếu $i = j$, và $0$ ngược lại, $1 \le i, j \le n)$. Áp dụng Mệnh đề 13.3 đến $(v_{1}, \dots  , v_{n})$, có một dãy của $n$ các phép đẳng cự $h_{1}, \dots  , h_{n}$ sao cho $h_{i}$ là siêu phẳng (hyperplane) phép đối xứng (reflection) hoặc đồng nhất thức, và nếu $(r_{1}, \dots  , r_{n})$ là các vectơ cho trước bởi
$$r_{j} = h_{n} \circ \cdots  \circ h_{2} \circ h_{1}(v_{j}),$$
Thì mọi $r_{j}$ là tổ hợp tuyến tính (linear combination) của các vectơ $(e_{1}, \dots  , e_{j}), 1 \le j \le n$. Đặt $R$ là ma trận có các cột là các vectơ $r_{j}$, và $H_{i}$ ma trận liên kết với $h_{i}$, rõ ràng là
$$R = H_{n} \cdots  H_{2}H_{1}A,$$

<!-- PAGE 517 -->
Ở đâu $R$ là tam giác trên (upper triangular) và mọi $H_{i}$ là hoặc Ma trận Householder hoặc đồng nhất thức. Tuy nhiên, $h_{i} \circ h_{i} =$ id với mọi $i, 1 \le i \le n$, và do đó
$$v_{j} = h_{1} \circ h_{2} \circ \cdots  \circ h_{n}(r_{j})$$
Với mọi $j, 1 \le j \le n$. Nhưng $\rho  = h_{1} \circ h_{2} \circ \cdots  \circ h_{n}$ là phép đẳng cự (isometry) được biểu diễn bởi ma trận trực giao (orthogonal matrix) $Q = H_{1}H_{2} \cdots  H_{n}$. Rõ ràng là $A = QR$, ở đâu $R$ là tam giác trên (upper triangular). Như ta được lưu ý trong Mệnh đề 13.3, đường chéo các phần tử (entries) của $R$ có thể được được chọn là không âm.
Các nhận xét:
$(1)$ Đặt
$$A_{k+1} = H_{k} \cdots  H_{2}H_{1}A,$$
Với $A_{1} = A, 1 \le k \le n$, chứng minh của Mệnh đề 13.3 có thể được interpreted theo phép tính của dãy của các ma trận $A_{1}, \dots  , A_{n+1} = R$. ma trận $A_{k+1}$ có hình dạng
$$A_{k+1} = \begin{pmatrix} \times & \times & \times & u_{1}^{k+1} & \times & \times & \times & \times \\ 0 & \times & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ 0 & 0 & \times & u_{k}^{k+1} & \times & \times & \times & \times \\ 0 & 0 & 0 & u^{k+1} & \times & \times & \times & \times \\ 0 & 0 & 0 & u_{k}^{kk+1+1} & \times & \times & \times & \times \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \vdots \\ 0 & 0 & 0 & u_{n1}^{k+1} & \times & \times & \times & \times \\ 0 & 0 & 0 & u_{n}^{k+1-} & \times & \times & \times & \times \end{pmatrix} ,$$
Ở đâu $(k +$ 1)th cột của ma trận là vectơ
$$u_{k+1} = h_{k} \circ \cdots  \circ h_{2} \circ h_{1}(v_{k+1}),$$
Và do đó
$$u_{k+1}' = \begin{pmatrix} u_{1}^{k+1}, \dots  , u_{k}^{k+1} \end{pmatrix}$$
Và
$$u_{k+1}'' = \begin{pmatrix} u_{k+1}^{k+1}, u_{k+2}^{k+1}, \dots  , u_{n}^{k+1} \\ k + 1areallzero, \end{pmatrix} .$$
Nếu cuối cùng $n -k -1$ các phần tử (entries) trong cột ở đó là không có gì đến thực hiện, và ta cho $H_{k+1} =$ I. Ngược lại, ta kill các phần tử này $n$ - $k$ - $1$ các phần tử (entries) bằng cách nhân $A_{k+1}$ trên trái bởi Ma trận Householder $H_{k+1}$ sending
$$\begin{pmatrix} 0, \dots  , 0, u_{k+1}^{k+1}, \dots  , u_{n}^{k+1} \end{pmatrix} to(0, \dots  , 0, r_{k+1,k+1}, 0, \dots  , 0),$$
Ở đâu $r_{k+1,k+1} = \|(u_{k+1}^{k+1}, \dots  , u_{n}^{k+1})\|$.

<!-- PAGE 518 -->
$(2)$ Nếu $A$ là khả nghịch và đường chéo các phần tử (entries) của $R$ là dương, nó có thể được được hiển thị rằng $Q$ và $R$ là duy nhất.
$(3)$ Nếu ta cho phép âm đường chéo các phần tử (entries) trong $R$, ma trận $H_{n}$ có thể được bỏ qua $(H_{n} =$ I).
$(4)$ phương pháp cho phép phép tính của định thức (determinant) của $A$. Ta có
$$\det(A) = (-1)^{m}r_{1,1} \cdots  r_{n,n},$$
Ở đâu $m$ là số của Householder các ma trận (không đồng nhất thức) trong số $H_{i}$.
$(5)$ “số điều kiện (condition number)” của ma trận $A$ được bảo toàn (xem Strang $[176]$, Golub và Van Loan $[83]$, Trefethen và Bau $[182]$, Kincaid và Cheney $[105]$, hoặc Ciarlet $[41])$. Điều này là rất tốt cho số tính ổn định.
$(6)$ phương pháp cũng áp dụng đến rectangular $m \times  n$ ma trận. Nếu $m \ge n$, thì $R$ là $n \times  n$ tam giác trên (upper triangular) ma trận và $Q$ là một ma trận cỡ $m \times  n$ sao cho $Q^{\top}Q = I_{n}$. sau đây Matlab các hàm cài đặt Nhân tử hóa QR (QR-factorization) phương pháp của thực square (có thể suy biến) ma trận $A$ bằng cách sử dụng Householder các phép đối xứng chính hàm houseqr tính tam giác trên (upper triangular) ma trận $R$ thu được bằng cách áp dụng Householder các phép đối xứng đến $A$. Nó làm cho sử dụng của hàm house, mà tính unit vectơ $u$ sao cho cho trước vectơ $x \in \mathbb{R}^{p}$, Householder phép biến đổi $P =$ I $-2uu^{\top}$ các tập hợp đến không tất cả các phần tử (entries) trong $x$ nhưng phần tử thứ nhất $x_{1}$. Nó chỉ áp dụng nếu $\|x(2$: $p)\|_{1} = |x_{2}|+\cdots +|x_{p}| > 0$. Vì các phép tính được thực hiện trong floating điểm, ta sử dụng tolerance nhân tử tol, và nếu $\|x(2$: $p)\|_{1} \le$ tol, thì ta trả về $u = 0$, mà indicates rằng tương ứng Householder phép biến đổi là đồng nhất thức. để tạo sure rằng $\|Px\|$ là như lớn như khả dĩ/có thể, ta chọn uu $= x + sign(x_{1}) \|x\|_{2} e_{1}$, ở đâu dấu(z) $= 1$ nếu $z \ge 0$ và dấu(z) $= -1$ nếu $z < 0$. Lưu ý rằng kết quả là, đường chéo các phần tử (entries) trong $R$ có thể là âm. Ta sẽ lấy care của điều này vấn đề sau này. hàm $s =$ signe(x) % nếu $x >= 0$, thì signe(x) $= 1$ % khác nếu $x < 0$ thì signe(x) $= -1$ % nếu $x < 0 s = -1$; khác $s = 1$; kết thúc/cuối kết thúc/cuối

<!-- PAGE 519 -->
Hàm [uu, $u] =$ house(x) % Điều này các xây dựng chưa chuẩn hóa vectơ uu % định nghĩa Phép đối xứng Householder rằng % các không điểm tất cả nhưng thứ nhất các phần tử (entries) trong $x$. % $u$ được chuẩn hóa vectơ $uu/||uu||$ % tol $= 2*10^(-15)$; % tolerance uu $= x; p =$ kích thước(x,1); % tính $l^1-norm$ của x(2:p,1) n1 $=$ tổng(abs(x(2:p,1))); nếu n1 $<=$ tol $u =$ các không điểm(p,1); uu $= u$; khác $l =$ sqrt(x’*x); % $l^2$ chuẩn (norm) của $x$ uu(1) $=$ x(1) $+$ signe(x(1))*l; $u = uu/sqrt(uu’*uu)$; kết thúc/cuối kết thúc/cuối Householder các phép biến đổi là recorded trong mảng (array) $u$ của $n$ - $1$ các vectơ. Có nhiều hơn/thêm efficient implementations, nhưng cho sake của clarity ta trình bày sau đây phiên bản. hàm $[R, u] =$ houseqr() % hàm này tính tam giác trên (upper triangular) $R$ trong QR nhân tử hóa % của $A$ bằng cách sử dụng Householder các phép đối xứng, và ẩn biểu diễn % của $Q$ như dãy của $n$ - $1$ các vectơ $u_i$ biểu diễn Householder % các phép đối xứng $n =$ kích thước(, $1); R = A; u =$ các không điểm(n,n-1); cho $i =$ 1:n-1 [~, u(i:n,i)] $=$ house(R(i:n,i)); nếu u(i:n,i) $==$ các không điểm(n - $i +$ 1,1)
$$R(i+1:n,i) = zeros(n - i,1);$$
Khác
$$R(i:n,i:n) = R(i:n,i:n) - 2*u(i:n,i)*(u(i:n,i)’*R(i:n,i:n));$$
Kết thúc/cuối kết thúc/cuối kết thúc/cuối

<!-- PAGE 520 -->
Nếu chỉ $R$ là mong muốn, thì houseqr thực hiện job. Trong thứ tự để thu được $R$, ta cần đến compose Householder các phép biến đổi. Ta trình bày đơn giản phương pháp mà là không hầu hết efficient (có một cách để tránh nhân explicity Householder các ma trận). hàm buildhouse creates Phép đối xứng Householder từ vectơ $v$. hàm $P =$ buildhouse(v,i) % hàm này xây dựng Phép đối xứng Householder % [I $0$ ] % $[0$ PP] % từ Phép đối xứng Householder % $PP =$ I - 2uu*uu’ % ở đâu uu $=$ v(i:n) % Nếu uu $= 0$ thì $P$ - I % $n =$ kích thước(v,1); nếu v(i:n) $==$ các không điểm(n - $i +$ 1,1) $P =$ eye(n); khác $PP =$ eye(n - $i + 1)$ - 2*v(i:n)*v(i:n)’; $P =$ [eye(i-1) các không điểm(i-1, $n$ - $i + 1)$; các không điểm(n - $i + 1, i$ - $1)$ PP]; kết thúc/cuối kết thúc/cuối hàm buildQ xây dựng ma trận $Q$ trong Phân rã QR (QR-decomposition) của $A$. hàm $Q =$ buildQ(u) % Xây dựng ma trận $Q$ trong QR phân rã % của nxn ma trận $A$ bằng cách sử dụng Householder các ma trận, % ở đâu $u$ là biểu diễn của $n$ - $1$ % Phép đối xứng Householder bởi danh sách $u$ của các vectơ produced bởi % houseqr $n =$ kích thước(u,1); $Q =$ buildhouse(u(:,1),1); cho $i =$ 2:n-1 $Q =$ Q*buildhouse(u(:,i),i); kết thúc/cuối kết thúc/cuối hàm buildhouseQR tính Nhân tử hóa QR (QR-factorization) của $A$. Tại kết thúc/cuối, nếu một số các phần tử (entries) trên đường chéo của $R$ là âm, nó creates đường chéo ma trận trực giao (orthogonal matrix) $P$ sao cho $PR$ có không âm đường chéo các phần tử (entries), sao cho $A =$ (QP)(PR) là mong muốn Nhân tử hóa QR (QR-factorization) của $A$.

<!-- PAGE 521 -->
Hàm [Q,R] $=$ buildhouseQR() % % Tính QR phân rã của square % ma trận $A$ (có thể suy biến) bằng cách sử dụng Householder các phép đối xứng $n =$ kích thước(,1); [R,u] $=$ houseqr(); $Q =$ buildQ(u); % Produces ma trận $R$ có đường chéo các phần tử (entries) là % không âm $P =$ eye(n); cho $i =$ 1:n nếu R(i,i) $< 0$
$$P(i,i) = -1;$$
Kết thúc/cuối kết thúc/cuối $Q =$ Q*P; $R =$ P*R; kết thúc/cuối

> **Ví dụ 13.1.** Xét ma trận
$$A = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 2 & 3 & 4 & 5 \\ 3 & 4 & 5 & 6 \\ 4 & 5 & 6 & 7 \end{pmatrix} .$$
Chạy hàm buildhouseQR, ta thu được
$$Q = \begin{pmatrix} 0.1826 & 0.8165 & 0.4001 & 0.3741 \\ 0.3651 & 0.4082 & -0.2546 & -0.7970 \\ 0.5477 & -0.0000 & -0.6910 & 0.4717 \\ 0.7303 & 0.4082 & 0.5455 & 0.0488 \end{pmatrix}$$
$$--$$
Và
$$R = \begin{pmatrix} 5.4772 & 7.3030 & 9.1287 & 10.9545 \\ 0 & 0.8165 & 1.6330 & 2.4495 \\ 0 & -0.0000 & 0.0000 & 0.0000 \\ 0 & 0.0000 & 0 & 0.0000 \end{pmatrix} .$$
$$-$$
Nhận thấy rằng $A$ có hạng (rank) $2$. độc giả nên kiểm tra rằng $A = QR$.
Nhận xét: Curiously, chạy Matlab built-in hàm qr, cùng $R$ là thu được (sai khác cột các dấu) nhưng khác nhau $Q$ là thu được (cuối cùng hai các cột là khác nhau).
