# Vectơ Các trường, Hiệp biến Các đạo hàm, Lie Brackets


<!-- PAGE 1486 -->
Khi $m = 1$, ở trên simplifies đến quen thuộc công thức
$$(g \circ f)'(a) = g'(b)f' (a),$$
Và cho $m = 2$, ta có
$$(g \circ f)^{(2)}(a) = g^{(2)}(b)(f^{(1)}(a))^{2}+ g^{(1)}(b)f^{(2)}(a).$$

## 39.8 Vectơ Các trường, Hiệp biến Các đạo hàm, Lie Brack-

$$ets$$
Trong mục này, ta ngắn gọn xét vectơ các trường và hiệp biến các đạo hàm của vectơ các trường. Như vậy các đạo hàm đóng quan trọng vai trò trong liên tục cơ học. Cho trước được chuẩn (norm) afin
$$\longrightarrow  \longrightarrow \longrightarrow$$
Không gian $(E, E$), vectơ trường trên $(E, E$) là hàm $X$: $E \to E$. Một cách trực quan, vectơ trường assigns vectơ đến mọi điểm trong $E$. Như vậy các vectơ có thể là buộc, velocities, accelerations, etc. Cho trước hai vectơ các trường $X, Y$ được định nghĩa trên một số mở tập con $\Omega$ của $E$, với mọi điểm $a \in \Omega$, ta sẽ like để định nghĩa đạo hàm của $X$ đối với $Y$ tại. Điều này là loại/kiểu của đạo hàm theo hướng (directional derivative) rằng cho variation của $X$ như ta di chuyển dọc theo $Y$, và ta ký hiệu nó bởi $D_{Y}$ X(). đạo hàm $D_{Y}$ X() được định nghĩa như sau.
$$\longrightarrow$$

> **Định nghĩa 39.22.** Cho $(E, E$) được chuẩn (norm) không gian afin (affine space). Cho trước bất kỳ mở tập con $\Omega$ của $E$, cho trước bất kỳ hai vectơ các trường $X$ và $Y$ được định nghĩa trên $\Omega$, với mọi $a \in \Omega$, hiệp biến đạo hàm (hoặc Lie đạo hàm) của $X$ w.r.t. vectơ trường $Y$ tại, được ký hiệu bởi $D_{Y}$ X(), là giới hạn (nếu nó tồn tại)
$$-$$
$$t\to lim0, t\in U \frac{X(a + tY (a))X(a)}{t} ,$$
Ở đâu $U = {t \in \mathbb{R}$ | $a +$ tY $(a) \in \Omega , t \neq  0}$. Nếu $Y$ là hằng số vectơ trường, ta kiểm chứng được ngay rằng ánh xạ
$$X \mapsto D_{Y} X(a)$$
Là ánh xạ tuyến tính (linear map) được gọi là đạo hàm của vectơ trường $X$, và được ký hiệu bởi DX(). Nếu $f$: $E \to \mathbb{R}$ là hàm, ta định nghĩa $D_{Y}$ f() như giới hạn (nếu nó tồn tại)
$$-$$
$$t\to lim0, t\in U \frac{f(a + tY (a))f(a)}{t} ,$$
Ở đâu $U = {t \in \mathbb{R}$ | $a +$ tY $(a) \in \Omega , t \neq  0}$. Nó là đạo hàm theo hướng (directional derivative) của $f$ w.r.t. vectơ trường $Y$ tại, và nó là cũng thường được ký hiệu bởi $Y$ (f)(), hoặc $Y (f)_{a}$. Từ bây giờ trên, ta giả sử rằng tất cả vectơ các trường và tất cả các hàm dưới consideration là trơn (smooth) $(C^{\infty})$. tập hợp $C^{\infty}(\Omega$) của trơn (smooth) $C^{\infty}-functions f$: $\Omega \to \mathbb{R}$ là vành. Cho trước

<!-- PAGE 1487 -->
Trơn (smooth) vectơ trường $X$ và trơn (smooth) hàm $f$ (cả hai trên $\Omega$), vectơ trường fX được định nghĩa sao cho (fX)() $=$ f()X(), và ta kiểm chứng được ngay rằng nó là trơn (smooth). Do đó, tập hợp $\mathcal{X}(\Omega$) của trơn (smooth) vectơ các trường trên $\Omega$ là $C^{\infty}(\Omega$)-môđun. sau đây mệnh đề là để lại như một bài tập. Nó chỉ ra rằng $D_{Y}$ X() là $a \mathbb{R}-bilinear$ ánh xạ trên $\mathcal{X}(\Omega$), là $C^{\infty}(\Omega$)-tuyến tính trong $Y$, và thỏa mãn Leibniz derivation các quy tắc đối với $X$.

> **Mệnh đề 39.28.** hiệp biến đạo hàm $D_{Y}$ X() thỏa mãn các tính chất sau đây:
$$D_{(Y1+Y2)}X(a) = D_{Y1}X(a) + D_{Y2}X(a),$$
$$D_{fY} X(a) = f(a)D_{Y} X(a),$$
$$D_{Y} (X_{1} + X_{2})(a) = D_{Y} X_{1}(a) + D_{Y} X_{2}(a),$$
$$D_{Y} fX(a) = D_{Y} f(a)X(a) + f(a)D_{Y} X(a),$$
Ở đâu $X, Y, X_{1}, X_{2}, Y_{1}, Y_{2}$ là trơn (smooth) vectơ các trường trên $\Omega$, và $f$: $E \to \mathbb{R}$ là trơn (smooth) hàm. Trong vi phân hình học, ở trên các tính chất được lấy như axioms của afin connections, trong thứ tự để định nghĩa hiệp biến các đạo hàm của vectơ các trường trên các đa tạp. Trong nhiều các trường hợp, vectơ trường $Y$ là tiếp tuyến trường của một số trơn (smooth) đường cong $\gamma$: ] - $\eta , \eta [\to E$. Nếu do đó, sau đây mệnh đề nghiệm đúng.

> **Mệnh đề 39.29.** Cho trước trơn (smooth) đường cong $\gamma$: ] - $\eta , \eta [\to E$, đặt $Y$ là vectơ trường được định nghĩa trên $\gamma$ (] - $\eta , \eta$ [) sao cho
$$Y (\gamma (u)) = \frac{d\gamma}{dt} (u),$$
Với mọi vectơ trường $X$ được định nghĩa trên $\gamma$ (] - $\eta , \eta$ [), ta có
$$$$
$$D_{Y} X(a) = \frac{d}{dt} X(\gamma (t))(0),$$
Ở đâu $a = \gamma (0)$. đạo hàm $D_{Y}$ X() là do đó đạo hàm của vectơ trường $X$ dọc theo đường cong $\gamma$, và nó được gọi là hiệp biến đạo hàm của $X$ dọc theo $\gamma$.
$$\longrightarrow$$
Cho trước hệ quy chiếu afin (affine frame) $(O, (u_{1}, \dots  , u_{n}))$ cho $(E, E$), nó là dễ dàng được thấy rằng hiệp biến đạo hàm $D_{Y}$ X() được biểu diễn như sau:
$$D_{Y} X(a) = \sum_{i=1j}^{n}  \sum_{=1}^{n}  \begin{pmatrix} \partial X_{i} \\ Y_{j} \\ \partial x_{j} \end{pmatrix} (a)e_{i}.$$
Một cách tổng quát, $D_{Y}$ X() $\neq  D_{X}Y$ (). đại lượng
$$[X, Y ] = D_{X}Y -D_{Y} X$$
