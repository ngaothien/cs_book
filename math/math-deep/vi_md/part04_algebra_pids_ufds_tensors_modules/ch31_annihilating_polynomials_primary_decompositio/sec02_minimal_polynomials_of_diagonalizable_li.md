# Tối tiểu Các đa thức của Chéo hóa được (diagonalizable) Các ánh xạ tuyến tính (linear maps)


<!-- PAGE 1107 -->

## 31.2 Tối tiểu Các đa thức của Chéo hóa được (diagonalizable)

$$Linear Maps$$
Trong mục này ta chứng minh rằng nếu đa thức tối tiểu (minimal polynomial) $m_{f}$ của ánh xạ tuyến tính (linear map) $f$ là của tạo thành
$$m_{f} = (X -\lambda_{1} ) \cdots  (X -\lambda_{k} )$$
Cho phân biệt các vô hướng $\lambda_{1} , \dots  , \lambda_{k}  \in K$, thì $f$ là chéo hóa được (diagonalizable). Điều này là powerful kết quả rằng có số của implications. Nhưng thứ nhất ta cần của một vài các tính chất của bất biến các không gian con. Cho trước ánh xạ tuyến tính (linear map) $f$: $E \to E$, nhắc lại rằng không gian con $W$ của $E$ là bất biến dưới $f$ nếu
$$\mathbb{R}^{2} \mathbb{R}^{2}$$
F(u) $\in W$ với mọi $u \in W$. Ví dụ, nếu $f$: $\to$ là f(x, $y) = (-x, y)$, trục $y$ là bất biến dưới $f$.

> **Mệnh đề 31.3.** Cho $W$ là không gian con của $E$ bất biến dưới ánh xạ tuyến tính (linear map) $f$: $E \to E$ (ở đâu $E$ là hữu hạn chiều). Thì đa thức tối tiểu (minimal polynomial) của thu hẹp $f$ | $W$ của $f$ đến $W$ chia hết đa thức tối tiểu (minimal polynomial) của $f$, và đa thức đặc trưng (characteristic polynomial) của $f$ | $W$ chia hết đa thức đặc trưng (characteristic polynomial) của $f$. Phác thảo của chứng minh. then chốt ingredient là rằng ta có thể chọn cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $E$ trong mà $(e_{1}, \dots  , e_{k})$ là cơ sở (basis) của $W$. ma trận của $f$ trên cơ sở (cơ sở (basis)) này là ma trận khối (block matrix) của tạo thành
$$A = \begin{pmatrix} B & C \\ 0 & D \end{pmatrix} ,$$
Ở đâu $B$ là một ma trận cỡ $k \times  k$, $D$ là $(n$ - $k) \times  (n$ - $k)$ ma trận, và $C$ là $k \times  (n$ - $k)$ ma trận. Thì
$$\det(XI -A) = \det(XI -B) \det(XI -D),$$
Mà suy ra phát biểu về characteristic các đa thức. Hơn nữa,
$$A^{i}= \begin{pmatrix} B^{i} & C_{i} \\ 0 & D^{i} \end{pmatrix} ,$$
Với một số $k \times  (n$ - $k)$ ma trận $C_{i}$. Suy ra rằng bất kỳ đa thức mà annihilates $A$ cũng annihilates $B$ và $D$. Do đó đa thức tối tiểu (minimal polynomial) của $B$ chia hết đa thức tối tiểu (minimal polynomial) của $A$. Cho tiếp theo bước, có ít nhất hai các cách đến tiến hành. Ta có thể sử dụng old-fashion lập luận bằng cách sử dụng Lagrange interpolants, hoặc ta có thể sử dụng slight tổng quát hóa của khái niệm của linh hóa tử (annihilator). Ta chọn thứ hai phương pháp bởi vì nó minh họa một cách đẹp lũy thừa của chính các lý tưởng. Những gì ta cần là khái niệm của dẫn tử (conductor) (cũng được gọi là transporter).

> **Định nghĩa 31.2.** Cho $f$: $E \to E$ là ánh xạ tuyến tính (linear map) trên không gian vectơ hữu hạn chiều $E$, cho $W$ là bất biến không gian con của $f$, và cho $u$ là bất kỳ vectơ trong $E$. tập hợp $S_{f}(u, W)$ bao gồm của tất cả các đa thức $q \in$ K[X] sao cho q(f)(u) $\in W$ được gọi là f-conductor của $u$ vào $W$.

<!-- PAGE 1108 -->
Nhận thấy rằng đa thức tối tiểu (minimal polynomial) $m_{f}$ của $f$ luôn luôn thuộc đến $S_{f}(u, W)$, do đó điều này là không tầm thường tập hợp. Cũng, nếu $W = (0)$, thì $S_{f}(u, (0))$ là chỉ linh hóa tử (annihilator) của $f$. then chốt tính chất của $S_{f}(u, W)$ là rằng nó là lý tưởng (ideal).

> **Mệnh đề 31.4.** Nếu $W$ là bất biến không gian con cho $f$, thì với mỗi $u \in E$, f-conductor $S_{f}(u, W)$ là lý tưởng (ideal) trong K[X]. Ta để lại chứng minh như đơn giản bài tập, bằng cách sử dụng sự kiện rằng nếu $W$ bất biến dưới $f$, thì $W$ là bất biến dưới mọi đa thức q(f) trong $S_{f}(u, W)$. Vì $S_{f}(u, W)$ là lý tưởng (ideal), nó được sinh bởi duy nhất chuẩn hóa (monic) đa thức $q$ của nhỏ nhất bậc, và bởi vì đa thức tối tiểu (minimal polynomial) $m_{f}$ của $f$ là trong $S_{f}(u, W)$, đa thức $q$ chia hết $m$.

> **Định nghĩa 31.3.** duy nhất chuẩn hóa (monic) đa thức mà sinh ra $S_{f}(u, W)$ được gọi là dẫn tử (conductor) của $u$ vào $W$.
$$\mathbb{R}^{2} \mathbb{R}^{2}$$

> **Ví dụ 31.1.** Ví dụ, giả sử $f$: $\to$ ở đâu f(x, $y) = (x, 0)$. Nhận thấy rằng
$$W = {(x, 0) \in \mathbb{R}^{2}} is invariant under f. By representing f as \begin{pmatrix} 1 & 0 \\ 0 & 0 \\ wesay \end{pmatrix} , we see that m_{f}(X) =$$
$\chi_{f} (X) = X^{2}$ - $X$. Cho $u = (0, y)$. Thì $S_{f}(u, W) = (X)$ và $X$ là dẫn tử (conductor) của $u$ vào $W$.

> **Mệnh đề 31.5.** Cho $f$: $E \to E$ là ánh xạ tuyến tính (linear map) trên hữu hạn chiều không gian $E$ và giả sử rằng đa thức tối tiểu (minimal polynomial) $m$ của $f$ là của tạo thành
$$m = (X -\lambda_{1} )^{r1}\cdots  (X -\lambda_{k} )^{rk},$$
Ở đâu các trị riêng (eigenvalues) $\lambda_{1} , \dots  , \lambda_{k}$ của $f$ thuộc đến $K$. Nếu $W$ là thực sự/đúng đắn không gian con của $E$ mà là bất biến dưới $f$, thì có một vectơ $u \in E$ với các tính chất sau đây:
() $u \in / W$;
$(b) (f$ - $\lambda$ id)(u) $\in W$, với một số trị riêng (eigenvalue) $\lambda$ của $f$.

*Chứng minh.* Nhận thấy rằng () và $(b)$ cùng nhau assert rằng dẫn tử (conductor) của $u$ vào $W$ là đa thức của tạo thành $X$ - $\lambda_{i}$. Chọn bất kỳ vectơ $v \in E$ không trong $W$, và cho $g$ là dẫn tử (conductor) của $v$ vào $W$, i.e. g(f)(v) $\in W$. Vì $g$ chia hết $m$ và $v \in / W$, đa thức $g$ là không hằng số, và do đó nó là của tạo thành
$$g = (X -\lambda_{1} )^{s1}\cdots  (X -\lambda_{k} )^{sk},$$
Với ít nhất một số $s_{i} > 0$. Chọn một số chỉ số $j$ sao cho $s_{j} > 0$. Thì $X$ - $\lambda_{j}$ là nhân tử của $g$, do đó ta có thể viết
$$g = (X -\lambda_{j} )q.(*)$$

<!-- PAGE 1109 -->
Theo định nghĩa của $g$, vectơ $u =$ q(f)(v) không thể là trong $W$, vì ngược lại $g$ sẽ không là của tối tiểu bậc. Tuy nhiên, (*) suy ra rằng
$$(f -\lambda_{j} id)(u) = (f -\lambda_{j} id)(q(f)(v))$$
$$= g(f)(v)$$
Là trong $W$, mà kết luận chứng minh. Ta có thể bây giờ chứng minh chính kết quả của điều này mục.

> **Định lý 31.6.** Cho $f$: $E \to E$ là ánh xạ tuyến tính (linear map) trên hữu hạn chiều không gian $E$. Thì $f$ là chéo hóa được (diagonalizable) khi và chỉ khi của nó đa thức tối tiểu (minimal polynomial) $m$ là của tạo thành
$$m = (X -\lambda_{1} ) \cdots  (X -\lambda_{k} ),$$
Ở đâu $\lambda_{1} , \dots  , \lambda_{k}$ là phân biệt các phần tử của $K$.

*Chứng minh.* Ta đã đã chỉ ra trong Mệnh đề 31.2 rằng nếu $f$ là chéo hóa được (diagonalizable), thì của nó đa thức tối tiểu (minimal polynomial) là của ở trên tạo thành (ở đâu $\lambda_{1} , \dots  , \lambda_{k}$ là phân biệt các trị riêng (eigenvalues) của $f)$. Cho điều ngược lại, cho $W$ là không gian con được sinh (spanned) bởi tất cả các vectơ riêng (eigenvectors) của $f$. Nếu $W \neq  E$, vì $W$ là bất biến dưới $f$, theo Mệnh đề 31.5, tồn tại một vectơ $u \in / W$ sao cho với một số $\lambda_{j}$, ta có
$$(f -\lambda_{j} id)(u) \in W.$$
Cho $v = (f$ - $\lambda_{j}$ id)(u) $\in W$. Vì $v \in W$, ta có thể viết
$$v = w_{1} + \cdots  + w_{k}$$
Ở đâu $f(w_{i}) = \lambda_{i} w_{i}$ (hoặc $w_{i} = 0$ hoặc $w_{i}$ là vectơ riêng (eigenvector) cho $\lambda_{i}$), và do đó với mọi đa thức $h$, ta có
$$h(f)(v) = h(\lambda_{1} )w_{1} + \cdots  + h(\lambda_{k} )w_{k},$$
Mà chỉ ra rằng h(f)(v) $\in W$ với mọi đa thức $h$. Ta có thể viết
$$m = (X -\lambda_{j} )q$$
Với một số đa thức $q$, và cũng
$$q -q(\lambda_{j} ) = p(X -\lambda_{j} )$$
Với một số đa thức $p$. Ta biết rằng p(f)(v) $\in W$, và vì $m$ là đa thức tối tiểu (minimal polynomial) của $f$, ta có
$$0 = m(f)(u) = (f -\lambda_{j} id)(q(f)(u)),$$
Mà suy ra rằng q(f)(u) $\in W$ (hoặc q(f)(u) $= 0$, hoặc nó là vectơ riêng (eigenvector) liên kết với $\lambda_{j}$). Tuy nhiên,
$$q(f)(u) -q(\lambda_{j} )u = p(f)((f -\lambda_{j} id)(u)) = p(f)(v),$$
Và vì p(f)(v) $\in W$ và q(f)(u) $\in W$, ta kết luận rằng $q(\lambda_{j} )u \in W$. Nhưng, $u \in / W$, mà suy ra rằng $q(\lambda_{j}$) $= 0$, do đó $\lambda_{j}$ là gấp đôi nghiệm (root) của $m$, một mâu thuẫn. Vì vậy, ta phải có $W = E$.
