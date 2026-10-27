# Witt Phân rã


<!-- PAGE 1040 -->

> **Mệnh đề 29.27.** Nếu $\Phi$ là bất kỳ không suy biến dạng toàn phương (quadratic form) (trên trường của characteristic $= 2)$ sao cho tồn tại một khác không vectơ $x \in E$ với $\Phi (x) = 0$, thì với mọi $\alpha  \in K$, tồn tại một $y \in E$ sao cho $\Phi (y) = \alpha$.

*Chứng minh.* Vì bởi giả thiết tồn tại một khác không vectơ $u \in E$ với $\Phi (u) = 0$, theo Mệnh đề 29.26 ở đó là một cái khác vectơ đẳng hướng (isotropic vector) $v$ sao cho $u$ và $v$ là độc lập tuyến tính (linearly independent) và sao cho (sau rescaling) $\phi (u, v) = 1$. Thì với mọi $\alpha  \in K$, kiểm tra rằng
$$\Phi \begin{pmatrix} \alpha \\ u + & v \\ 2 \end{pmatrix} = \alpha ,$$
Như mong muốn.
Nhận xét: Một số các tác giả refer đến ở trên mặt phẳng như mặt phẳng hyperbolic (hyperbolic plane). Berger (và những cái khác) điểm ra rằng điều này thuật ngữ là undesirable bởi vì khái niệm của mặt phẳng hyperbolic (hyperbolic plane) đã tồn tại trong vi phân hình học và refers đến rất khác nhau object. Ta để lại nó như exercice đến hình ra rằng nhóm của các phép đẳng cự của Artinian mặt phẳng, tập hợp tất cả $2 \times  2$ các ma trận $A$ sao cho
$$A^{\top} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} ,$$
Bao gồm của tất cả các ma trận của tạo thành
$$\begin{pmatrix} \lambda & 0 \\ 0 & \lambda^{-1} \end{pmatrix} or \begin{pmatrix} 0 & \lambda \\ \lambda^{-1} & 0 \end{pmatrix} ,\lambda  \in K -{0}.$$
Đặc biệt, nếu $K =\mathbb{R}$, thì nhóm này được ký hiệu O(1, $1)$ có bốn liên thông các thành phần. Ta bây giờ turn đến Witt phân rã.

## 29.7 Witt Phân rã

Từ bây giờ trên, $\phi$: $E \times  E \to K$ là $\epsilon$ -Hermite tạo thành. sau đây giả định sẽ là cần thiết: Tính chất $(T)$. Với mọi $u \in E$, tồn tại một $\alpha  \in K$ sao cho $\phi (u, u) = \alpha  +\overline{\epsilon \alpha}$. Tính chất $(T)$ là luôn luôn được thỏa mãn nếu $\phi$ là thay phiên, hoặc nếu $K$ là của characteristic $\neq  2$ và $\epsilon  = \pm 1$, với $\alpha  =_{2}^{1} \phi (u, u)$. sau đây (bizarre) technical bổ đề sẽ là cần thiết.

> **Bổ đề 29.28.** Cho $\phi$ là $\epsilon$ -Hermite tạo thành trên $E$ và giả sử rằng $\phi$ thỏa mãn tính chất $(T)$. Với mọi một cách tổng đẳng hướng không gian con $U \neq  (0)$ của $E$, với mọi $x \in E$ không trực giao đến $U$, và với mọi $\alpha  \in K$, tồn tại một $y \in U$ sao cho
$$\phi (x + y, x + y) = \alpha  +\overline{\epsilon \alpha .}$$

<!-- PAGE 1041 -->
$$Proof. By property (T), \frac{wehave}{\epsilon \phi (x, y),} \phi (x, x) = \beta  +\overline{\epsilon \beta} for some \beta  \in K. For any y \in U, since \phi$$
Là $\epsilon$ -Hermite, $\phi (y, x) =$ và vì $U$ là một cách tổng đẳng hướng $\phi (y, y) = 0$, do đó ta có
$$\phi (x + y, x + y) = \phi (x, x) + \phi (x, y) + \phi (y, x) + \phi (y, y)$$
$$= \beta  +\overline{\epsilon \beta} + \phi (x, y) +\overline{\epsilon \phi}\overline{(}\overline{x, y}\overline{)}$$
$$= \beta  + \phi (x, y) + \epsilon \overline{(}\overline{\beta}\overline{+}\overline{\phi}\overline{(}\overline{x, y}\overline{)}.$$
Vì $x$ là không trực giao đến $U$, hàm $y \mapsto \phi (x, y) + \beta$ là không hằng số hàm. Hệ quả là, hàm này lấy giá trị $\alpha$ với một số $y \in U$, mà chứng minh bổ đề.

> **Định nghĩa 29.18.** Cho $\phi$ là $\epsilon$ -Hermite tạo thành trên $E$. yếu Witt phân rã của $E$ là bộ ba $(U$, U', $W)$, sao cho
$(i) E = U \oplus$ U' $\oplus W$ (tổng trực tiếp (direct sum)).
(ii) $U$ và U' là một cách tổng đẳng hướng.
(iii) $W$ là không suy biến và trực giao đến $U \oplus$ U'. Ta nói rằng yếu Witt phân rã $(U$, U', $W)$ là không tầm thường nếu U̸ $= (0)$ và U' $\neq  (0)$. Hơn nữa, nếu $E$ là hữu hạn chiều, thì dim(U) $=$ dim(U') và trong phù hợp cơ sở (basis), ma trận biểu diễn $\phi$ là của tạo thành
$$\begin{pmatrix} 0 & A & 0 \\ \epsilon A & 0 & 0 \\ 0 & 0 & B \end{pmatrix}$$
Ta nói rằng $\phi$ là neutral tạo thành nếu nó là không suy biến, $E$ là hữu hạn chiều, và nếu $W = (0)$. Trong trường hợp này, ma trận $B$ là missing. Witt phân rã cho mà $W$ có không có khác không đẳng hướng các vectơ $(W$ là dị hướng) được gọi là một Witt phân rã. Nhận thấy rằng nếu $\Phi$ là không suy biến, thì ta có tầm thường yếu Witt phân rã thu được bởi đặt $U =$ U' $= (0)$ và $W = E$. Do đó yếu Witt phân rã là informative chỉ nếu $E$ là không dị hướng (tồn tại một khác không vectơ đẳng hướng (isotropic vector), i.e. một số u̸ $= 0$ sao cho $\Phi (u) = 0)$, trong mà trường hợp hầu hết informative không tầm thường yếu Witt các phân rã là những phần tử đó cho mà $W$ là dị hướng và $U$ và U' là như big như khả dĩ/có thể. Đôi khi, ta sử dụng ký hiệu $U_{1}^{\perp}\oplus U_{2}$ đến indicate rằng trong tổng trực tiếp (direct sum) $U_{1} \oplus U_{2}$, các không gian con $U_{1}$ và $U_{2}$ là trực giao. Thì, trong Định nghĩa 29.18, ta có thể viết rằng $E = (U \oplus$ U' $)^{\perp}\oplus W$. bước thứ nhất trong chỉ ra sự tồn tại của Witt phân rã là điều này.

<!-- PAGE 1042 -->

> **Mệnh đề 29.29.** Cho $\phi$ là $\epsilon$ -Hermite tạo thành trên $E$, giả sử rằng $\phi$ là không suy biến và thỏa mãn tính chất $(T)$, và cho $U$ là bất kỳ một cách tổng đẳng hướng không gian con của $E$ của hữu hạn số chiều dim(U) $= r \ge 1$.
$(1)$ Nếu U' là bất kỳ một cách tổng đẳng hướng không gian con có số chiều $r$ và nếu $U'\cap U^{\perp} = (0)$, thì $U \oplus$ U' là không suy biến, và với mọi cơ sở (basis) $(u_{1}, \dots  , u_{r})$ của $U$, có một cơ sở (basis) $(u_{1}', \dots  , u_{r}')$ của U' sao cho $\phi (u_{i}, u_{j}') = \delta_{ij}$, với mọi $i, j = 1, \dots  , r$.
$(2)$ Nếu $W$ là bất kỳ một cách tổng đẳng hướng không gian con có số chiều nhiều nhất $r$ và nếu $W \cap U^{\perp} = (0)$, thì tồn tại một một cách tổng đẳng hướng không gian con U' với dim(U') $= r$ sao cho $W \subseteq$ U' và U' $\cap U^{\perp} = (0)$.

*Chứng minh.* $(1)$ Cho $\phi'$ là thu hẹp của $\phi$ đến $U \times$ U'. Vì U' $\cap U^{\perp} = (0)$, với mọi $v \in$ U', nếu $\phi (u, v) = 0$ với mọi $u \in U$, thì $v = 0$. Do đó, $\phi'$ là không suy biến (ta chỉ có để kiểm tra trên trái vì $\phi$ là $\epsilon$ -Hermite). Thì, assertion về các cơ sở suy ra từ phiên bản của Mệnh đề 29.3 cho các dạng nửa tuyến tính. Vì $U$ là một cách tổng đẳng hướng, $U \subseteq U^{\perp}$, và vì U' $\cap U^{\perp} = (0)$, ta phải có U' $\cap U = (0)$, mà chỉ ra rằng ta có tổng trực tiếp (direct sum) $U \oplus$ U'. Nó vẫn còn để chứng minh rằng $U +$ U' là không suy biến. Nhận thấy rằng
$$H = (U + U' ) \cap (U + U' )^{\perp}= (U + U' ) \cap U^{\perp} \cap U^{'\perp} .$$
Vì $U$ là một cách tổng đẳng hướng, $U \subseteq U^{\perp}$, và vì U' $\cap U^{\perp} = (0)$, ta có
$$(U + U') \cap U^{\perp}= (U \cap U^{\perp}) + (U'\cap U^{\perp}) = U + (0) = U,$$
Do đó $H = U \cap U^{'\perp}$. Vì $\phi'$ là không suy biến, $U \cap U^{'\perp} = (0)$, do đó $H = (0)$ và $U +$ U' là không suy biến.
$(2)$ Ta tiến hành bởi descending quy nạp trên $s =$ dim(W). base trường hợp $s = r$ là tầm thường. Cho quy nạp bước, nó suffices để chứng minh rằng nếu $s < r$, thì có một một cách tổng đẳng hướng không gian con W' chứa $W$ sao cho dim(W') $= s + 1$ và W' $\cap U^{\perp} = (0)$. Vì $s =$ dim(W) $<$ dim(U), thu hẹp của $\phi$ đến $U \times  W$ là suy biến. Vì $W \cap U^{\perp} = (0)$, ta phải có $U \cap W^{\perp} \neq  (0)$. Ta khẳng định rằng
$$̸$$
$$W^{\perp}\subseteq W + U^{\perp}.$$
Nếu ta đã có
$$W^{\perp} \subseteq W + U^{\perp} ,$$
Thì bởi vì $U$ và $W$ là hữu hạn chiều và $\phi$ là không suy biến, theo Mệnh đề 29.13, $U^{\perp \perp} = U$ và $W^{\perp \perp} = W$, do đó bằng cách lấy các trực giao, $W^{\perp} \subseteq W + U^{\perp}$ sẽ cho
$$(W + U^{\perp} )^{\perp}\subseteq W^{\perp \perp} ,$$
Rằng là,
$$W^{\perp} \cap U \subseteq W,$$

<!-- PAGE 1043 -->
Do đó $W^{\perp} \cap U \subseteq W \cap U$, và vì $U$ là một cách tổng đẳng hướng, $U \subseteq U^{\perp}$, mà cho ta
$$W^{\perp} \cap U \subseteq W \cap U \subseteq W \cap U^{\perp} = (0),$$
Contradicting sự kiện rằng $U \cap W^{\perp} \neq  (0)$. Vì vậy, tồn tại một $u \in W^{\perp}$ sao cho $u \in / W +U^{\perp}$. Vì $U \subseteq U^{\perp}$, ta có thể cộng đến $u$ bất kỳ vectơ $z \in W^{\perp} \cap U \subseteq U^{\perp}$ sao cho $u + z \in W^{\perp}$ và $u + z \in / W + U^{\perp}$ (nếu $u + z \in W + U^{\perp}$, vì $z \in U^{\perp}$, thì $u \in W + U^{\perp}$, một mâu thuẫn). Vì $W^{\perp} \cap$ U̸ $= (0)$ là một cách tổng đẳng hướng và $u \in / W + U^{\perp} = (W^{\perp} \cap U)^{\perp}$, ta có thể invoke Bổ đề 29.28 để tìm $z \in W^{\perp} \cap U$ sao cho $\phi (u + z, u + z) = 0$. Xem Hình 29.1. Nếu ta viết $x = u + z$, thì $x \in / W + U^{\perp}$, do đó W' $= W +$ Kx là một cách tổng đẳng hướng không gian con có số chiều $s + 1$. Hơn nữa, ta khẳng định rằng W' $\cap U^{\perp} = 0$.
$$U$$
$$0zUt$$
$$W$$
$$u$$
$$W$$
$$E$$
$$Figure 29.1: A schematic illustration of W and x = u + z$$
Ngược lại, ta sẽ có $y = w + \lambda x \in U^{\perp}$, với một số $w \in W$ và một số $\lambda  \in K$, và thì ta sẽ có $\lambda x = -w + y \in W + U^{\perp}$. Nếu $\lambda  \neq  0$, thì $x \in W + U^{\perp}$, một mâu thuẫn. Vì vậy, $\lambda  = 0, y = w$, và vì $y \in U^{\perp}$ và $w \in W$, ta có $y \in W \cap U^{\perp} = (0)$, mà có nghĩa là $y = 0$. Vì vậy, W' là cần thiết không gian con và điều này các đầy đủ chứng minh. Ở đây là một số các hệ quả của Mệnh đề 29.29. Nếu ta tập hợp $W = (0)$ trong Mệnh đề 29.29(2), thì ta thu được sau đây định lý chỉ ra rằng nếu $E$ là không dị hướng (tồn tại một khác không vectơ đẳng hướng (isotropic vector)) thì yếu không tầm thường Witt các phân rã tồn tại.

> **Định lý 29.30.** Cho $\phi$ là $\epsilon$ -Hermite tạo thành trên $E$ mà là không suy biến và thỏa mãn tính chất $(T)$. Với mọi một cách tổng đẳng hướng không gian con $U$ của $E$ của hữu hạn số chiều $r \ge 1$, tồn tại một một cách tổng đẳng hướng không gian con U' có số chiều $r$ sao cho $U \cap$ U' $= (0)$ và $U \oplus$ U' là không suy biến. Hệ quả là, nếu $E$ là không dị hướng, thì $(U$, U', $(U \oplus$ U' $)^{\perp})$ là yếu không tầm thường Witt phân rã cho $E$. Hơn nữa, theo Mệnh đề 29.29(1), khối $A$ trong ma trận của $\phi$ là ma trận đơn vị (identity matrix).

<!-- PAGE 1044 -->

> **Mệnh đề 29.31.** Bất kỳ hai $\epsilon$ -Hermite neutral các dạng thỏa mãn tính chất $(T)$ được định nghĩa trên các không gian của cùng số chiều là tương đương. sau đây mệnh đề chỉ ra rằng mọi không gian con $U$ của $E$ có thể được được nhúng vào không suy biến không gian con. Nó là cần thiết để chứng minh phiên bản của Witt mở rộng định lý (Định lý 29.48).

> **Mệnh đề 29.32.** Cho $\phi$ là $\epsilon$ -Hermite tạo thành trên $E$ mà là không suy biến và thỏa mãn tính chất $(T)$. Với mọi không gian con $U$ của $E$ của hữu hạn số chiều, nếu ta viết
$$U = V^{\perp}\oplus W,$$
Với một số phần bù trực giao (orthogonal complement) $W$ của $V =$ rad(U), và nếu ta cho $r =$ dim(rad(U)), thì tồn tại một một cách tổng đẳng hướng không gian con V' có số chiều $r$ sao cho $V \cap$ V' $= (0)$, và $(V \oplus V')^{\perp}\oplus W =$ V' $\oplus U$ là không suy biến. Hơn nữa, bất kỳ phép đẳng cự (isometry) $f$ từ $U$ vào một cái khác không gian (E', $\phi'$) ở đâu $\phi'$ là $\epsilon$ -Hermite tạo thành thỏa mãn cùng các giả định như $\phi$ có thể được được mở rộng đến phép đẳng cự (isometry) trên $(V \oplus$ V' $)^{\perp}\oplus W$.

*Chứng minh.* Vì $W$ là không suy biến, $W^{\perp}$ là cũng không suy biến, và $V \subseteq W^{\perp}$. Vì vậy, ta có thể áp dụng Định lý 29.30 đến thu hẹp của $\phi$ đến $W^{\perp}$ và đến $V$ để thu được cần thiết V'. Ta biết rằng $V \oplus$ V' là không suy biến và trực giao đến $W$, mà là cũng không suy biến,
$$\oplus$$
Do đó $(V \oplus V')^{\perp}\oplus W =$ V' $U$ là không suy biến. Ta để lại thứ hai phát biểu về mở rộng $f$ như một bài tập (sử dụng sự kiện rằng f(U) $=$ f(V $)^{\perp}\oplus$ f(W), ở đâu $V_{1} =$ f(V) là một cách tổng đẳng hướng có số chiều $r$, để tìm một cái khác một cách tổng đẳng hướng susbpace $V_{1}'$ có số chiều $r$ sao cho $V_{1} \cap V_{1}'  = (0)$ và $V_{1} \oplus V_{1}'$ là trực giao đến f(W)).
$$\oplus$$
Không gian con $(V \oplus V')^{\perp}\oplus W =$ V' $U$ là thường được gọi là không suy biến đầy đủ hóa của $U$. không gian con $V \oplus$ V' được gọi là một Artinian không gian. Mệnh đề 29.29 chỉ ra rằng $V \oplus$ V' có cơ sở (basis) $(u_{1}, v_{1}, \dots  , u_{r}, v_{r})$ bao gồm của các vectơ $u_{i} \in V$ và $v_{j} \in$ V' sao cho $\phi (u_{i}, u_{j}) = \delta_{ij}$. không gian con được sinh (spanned) bởi $(u_{i}, v_{i})$ là Artinian mặt phẳng, do đó $V \oplus$ V' là trực giao tổng trực tiếp (direct sum) của $r$ Artinian các mặt phẳng. Như vậy không gian là thường được ký hiệu bởi $Ar_{2r}$. Trong thứ tự để thu được mạnh hơn phiên bản của Witt phân rã khi $\phi$ có một số khác không vectơ đẳng hướng (isotropic vector) và $W$ là dị hướng ta bây giờ sharpen Mệnh đề 29.29

> **Định lý 29.33.** Cho $\phi$ là $\epsilon$ -Hermite tạo thành trên $E$ mà là không suy biến và thỏa mãn tính chất $(T)$. Cho $U_{1}$ và $U_{2}$ là hai một cách tổng đẳng hướng cực đại các không gian con của $E$, với $U_{1}$ hoặc $U_{2}$ của hữu hạn số chiều $\ge 1$. Viết $U = U_{1} \cap U_{2}$, cho $S_{1}$ là supplement của $U$ trong $U_{1}$ và $S_{2}$ là supplement của $U$ trong $U_{2}$ (sao cho $U_{1} = U \oplus S_{1}, U_{2} = U \oplus S_{2})$, và cho $S = S_{1} + S_{2}$. Thì, ở đó tồn tại hai các không gian con $W$ và $D$ của $E$ sao cho:
() các không gian con $S, U + W$, và $D$ là không suy biến và đôi một trực giao.

<!-- PAGE 1045 -->
$(b)$ Ta có tổng trực tiếp (direct sum) $E = S^{\perp}\oplus (U \oplus W)^{\perp}\oplus D$.
$(c)$ không gian con $D$ chứa không có khác không vectơ đẳng hướng (isotropic vector) $(D$ là dị hướng).
$(d)$ không gian con $W$ là một cách tổng đẳng hướng. Hơn nữa, $U_{1}$ và $U_{2}$ là cả hai hữu hạn dimensional, và ta có $dim(U_{1}) = dim(U_{2})$, dim(W) $=$ dim(U), $dim(S_{1}) = dim(S_{2})$, và codim(D) $= 2 dim(F_{1})$.

*Chứng minh.* Thứ nhất nhận thấy rằng nếu $X$ là một cách tổng đẳng hướng cực đại không gian con của $E$, thì bất kỳ vectơ đẳng hướng (isotropic vector) $x \in E$ trực giao đến $X$ phải thuộc đến $X$, vì ngược lại, $X +$ Kx sẽ là một cách tổng đẳng hướng không gian con chặt chứa $X$, contradicting maximality của $X$. Hệ quả là, nếu $x_{i}$ là bất kỳ vectơ đẳng hướng (isotropic vector) sao cho $x_{i} \in U_{i}^{\perp}$ (cho $i = 1, 2)$, thì $x_{i} \in U_{i}$. Ta khẳng định rằng
$$S_{1} \cap S_{2}^{\perp} = (0)andS_{2} \cap S_{1}^{\perp} = (0).$$
Giả sử rằng $y \in S_{1}$ là trực giao đến $S_{2}$. Vì $U_{1} = U \oplus S_{1}$ và $U_{1}$ là một cách tổng đẳng hướng, $y$ là trực giao đến $U_{1}$, và do đó trực giao đến $U$, sao cho $y$ là trực giao đến $U_{2} = U \oplus S_{2}$. Vì $S_{1} \subseteq U_{1}$ và $U_{1}$ là một cách tổng đẳng hướng, $y$ là vectơ đẳng hướng (isotropic vector) trực giao đến $U_{2}$, mà bởi trước đó nhận xét suy ra rằng $y \in U_{2}$. Thì, vì $S_{1} \subseteq U_{1}$ và $U \oplus S_{1}$ là tổng trực tiếp (direct sum), ta có
$$y \in S_{1} \cap U_{2} = S_{1} \cap U_{1} \cap U_{2} = S_{1} \cap U = (0).$$
Vì vậy $S_{1} \cap S_{2}^{\perp} = (0)$. đồng dạng chứng minh chỉ ra rằng $S_{2} \cap S_{1}^{\perp} = (0)$. Nếu $U_{1}$ là hữu hạn chiều (trường hợp ở đâu $U_{2}$ là hữu hạn chiều là đồng dạng), thì $S_{1}$ là hữu hạn chiều, do đó theo Mệnh đề 29.13, $S_{1}^{\perp}$ có hữu hạn đối chiều (codimension). Vì $S_{2}\cap S_{1}^{\perp} = (0)$, và vì bất kỳ supplement của $S_{1}^{\perp}$ có hữu hạn số chiều, ta phải có
$$\dim(S_{2}) \le codim(S_{1}^{\perp} ) = \dim(S_{1}).$$
Bởi đồng dạng lập luận, $dim(S_{1}) \le dim(S_{2})$, do đó ta có
$$\dim(S_{1}) = \dim(S_{2}).$$
Theo Mệnh đề 29.29(1), ta kết luận rằng $S = S_{1} + S_{2}$ là không suy biến. Theo Mệnh đề 29.21, không gian con $N = S^{\perp} = (S_{1} + S_{2})^{\perp}$ là không suy biến. Vì $U_{1} = U \oplus S_{1}, U_{2} = U \oplus S_{2}$, và $U_{1}, U_{2}$ là một cách tổng đẳng hướng, $U$ là trực giao đến $S_{1}$ và đến $S_{2}$, do đó $U \subseteq N$. Vì $U$ là một cách tổng đẳng hướng, theo Mệnh đề 29.30 ứng dụng đến $N$, có một một cách tổng đẳng hướng không gian con $W$ của $N$ sao cho dim(W) $=$ dim(U), $U \cap W = (0)$, và $U + W$ là không suy biến. Hệ quả là, $(d)$ được thỏa mãn bởi $W$. Đến thỏa mãn () và $(b)$, ta chọn $D$ là trực giao của $U \oplus W$ trong $N$. Thì, $N = (U \oplus W)^{\perp}\oplus D$ và $E = S^{\perp}\oplus N$, do đó $E = S^{\perp}\oplus (U \oplus W)^{\perp}\oplus D$. Như đến $(c)$, vì $D$ là trực giao $U \oplus W, D$ là trực giao đến $U$, và vì $D \subseteq N$ và $N$ là trực giao đến $S_{1} + S_{2}, D$ là trực giao đến $S_{1}$, do đó $D$ là trực giao đến $U_{1} = U \oplus S_{1}$. Nếu $y \in D$

<!-- PAGE 1046 -->
Là bất kỳ vectơ đẳng hướng (isotropic vector), vì $y \in U_{1}^{\perp}$, bởi trước đó nhận xét, $y \in U_{1}$, do đó $y \in D \cap U_{1}$. Nhưng, $D \subseteq N$ với $N \cap (S_{1} + S_{2}) = (0)$, và $D \cap (U + W) = (0)$, do đó $D \cap (U + S_{1}) = D \cap U_{1} = (0)$, mà cho ta $y = 0$. các phát biểu về số chiều là dễ dàng thu được. Cuối cùng, Định lý 29.33 cho ta mạnh tạo thành của Witt phân rã trong mà $W$ là anistropic. Cho trước bất kỳ ma trận $A \in M_{n}(K)$, ta nói rằng $A$ là xác định nếu $x^{\top}Ax \neq  0$ với mọi $x \in K^{n}$.

> **Định lý 29.34.** Cho $\phi$ là $\epsilon$ -Hermite tạo thành trên $E$ mà là không suy biến và thỏa mãn tính chất $(T)$.
$(1)$ Bất kỳ hai một cách tổng đẳng hướng cực đại các không gian của hữu hạn số chiều có cùng số chiều.
$(2)$ Với mọi một cách tổng đẳng hướng cực đại không gian con $U$ của hữu hạn số chiều $r \ge 1$, ở đó là một cái khác một cách tổng đẳng hướng cực đại không gian con U' có số chiều $r$ sao cho $U \cap$ U' $= (0)$, và $U \oplus$ U' là không suy biến. Hơn nữa, nếu $D = (U \oplus U')^{\perp}$, thì $(U$, U', $D)$ là Witt phân rã của $E$; nghĩa là, có không có khác không đẳng hướng các vectơ trong $D (D$ là dị hướng).
$(3)$ Nếu $E$ có hữu hạn số chiều $n \ge 1$ và tồn tại một khác không vectơ đẳng hướng (isotropic vector) cho $\phi  (E$ là không dị hướng), thì $E$ có không tầm thường Witt phân rã $(U$, U', $D)$ như trong $(2)$. Có một cơ sở (basis) của $E$ sao cho
$$(a) if \phi  is alternating (\epsilon  = -1 and \lambda  = \overline{\lambda} for all \lambda  \in K), then n = 2m and \phi  is$$
$$represented by a matrix of the form$$
$$\begin{pmatrix} 0 & I_{m} \\ -I_{m} & 0 \end{pmatrix}$$
$$(b) if \phi  is symmetric (\epsilon  = +1 and \lambda  = \overline{\lambda} for all \lambda  \in K), then \phi  is represented by a$$
$$matrix of the form$$
$$\begin{pmatrix} 0 & I_{r} & 0 \\ I_{r} & 0 & 0 \\ 0 & 0 & P \end{pmatrix} ,$$
$$where either n = 2r and P does not occur, or n > 2r and P is a definite symmetric$$
$$matrix.$$
$$(c) if \phi  is \epsilon -Hermitian (the involutive automorphism \lambda  \mapsto \overline{\lambda} is not the identity), then$$
$$\phi  is represented by a matrix of the form$$
$$\begin{pmatrix} 0 & I_{r} & 0 \\ \epsilon I_{r} & 0 & 0 \\ 0 & 0 & P \end{pmatrix} ,$$
$$where either n = 2r and P does not occur, or n > 2r and P is a definite matrix$$
$$such that P^{*} = \epsilon P.$$

<!-- PAGE 1047 -->

*Chứng minh.* Phần $(1)$ suy ra từ Định lý 29.33. Theo Mệnh đề 29.30, ta thu được một cách tổng đẳng hướng không gian con U' có số chiều $r$ sao cho $U \cap$ U' $= (0)$. Bằng cách áp dụng Định lý 29.33 đến $U_{1} = U$ và $U_{2} =$ U', ta thu được $U = W = (0)$, mà chứng minh $(2)$. Phần $(3)$ là immediate hệ quả của $(2)$. Hệ quả là của Định lý 29.34, ta tạo sau đây định nghĩa.

> **Định nghĩa 29.19.** Cho $E$ là không gian vectơ (vector space) của hữu hạn số chiều $n$, và cho $\phi$ là $\epsilon$ -Hermite tạo thành trên $E$ mà là không suy biến và thỏa mãn tính chất $(T)$. chỉ số (hoặc Witt chỉ số) $\nu$ của $\phi$, là chung/phổ biến số chiều của tất cả một cách tổng đẳng hướng cực đại các không gian con của $E$. Ta có $2\nu  \le n$. Neutral các dạng chỉ tồn tại nếu $n$ là chẵn/ngay cả, trong mà trường hợp, $\nu  = n/2$. Các dạng của chỉ số $\nu  = 0$ có không có khác không đẳng hướng các vectơ. Khi $K = \mathbb{R}$, điều này được thỏa mãn bởi xác định dương (positive definite) hoặc âm xác định đối xứng các dạng. Khi $K = \mathbb{C}$, điều này được thỏa mãn bởi xác định dương (positive definite) hoặc âm xác định Hermite các dạng. không gian vectơ (vector space) của neutral Hermite tạo thành $(\epsilon  = +1)$ là Artinian không gian, và không gian vectơ (vector space) của neutral thay phiên tạo thành là hyperbolic không gian. Nếu trường $K$ là algebraically đóng, ta có thể mô tả tất cả không suy biến các dạng toàn phương.

> **Mệnh đề 29.35.** Nếu $K$ là algebraically đóng và $E$ có số chiều $n$, thì với mọi không suy biến dạng toàn phương (quadratic form) $\Phi$, có một cơ sở (basis) $(e_{1}, \dots  , e_{n})$ sao cho $\Phi$ được cho bởi
$$\Phi \sum_{i-1}^{n}  =( \sum_{imi}  m=1 x_{i}x_{m+i}if n = 2m$$
$$\begin{pmatrix} x_{i}e_{i} \end{pmatrix} \sum  =1 x_{i}x_{m+i} + x_{2m+1}^{2}if n = 2m + 1.$$

*Chứng minh.* Ta hoạt động/công trình với dạng cực (polar form) $\phi$ của $\Phi$. Cho $U_{1}$ và $U_{2}$ là một số một cách tổng đẳng hướng các không gian con sao cho $U_{1} \cap U_{2} = (0)$ cho trước theo Định lý 29.34, và cho $q$ là của chúng chung/phổ biến số chiều. Thì, $W = U = (0)$. Vì ta có thể chọn các cơ sở $(e_{1}, \dots  e_{q})$ trong $U_{1}$ và $(e_{q+1}, \dots  , e_{2q})$ trong $U_{2}$ sao cho $\phi (e_{i}, e_{i+q}) = 0$, cho $i, j = 1, \dots  , q$, nó suffices đến chứng tỏ rằng dim(D) $\le 1$. Nếu $x, y \in D$ với $x \neq  0$, từ đồng nhất thức
$$\Phi (y -\lambda x) = \Phi (y) -\lambda \phi (x, y) + \lambda^{2} \Phi (x)$$
Và sự kiện rằng $\Phi (x) \neq  0$ vì $x \in D$ và $x \neq  0$, ta xem rằng phương trình $\Phi (y$ - $\lambda y) = 0$ có ít nhất một nghiệm. Vì $\Phi (z) \neq  0$ với mọi khác không $z \in D$, ta thu được $y = \lambda x$, và do đó dim(D) $\le 1$, như đã khẳng định. Mệnh đề 29.35 chỉ ra rằng với mọi không suy biến dạng toàn phương (quadratic form) $\Phi$ trên algebraically đóng trường, nếu dim(E) $=$ 2m hoặc dim(E) $=$ 2m $+ 1$ với $m \ge 1$, thì $\Phi$ có một số khác không vectơ đẳng hướng (isotropic vector).
