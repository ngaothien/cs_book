# Trực giao Các phép chiếu và Các phép đối hợp


<!-- PAGE 553 -->

## 14.6 Trực giao Các phép chiếu và Các phép đối hợp

Trong mục này ta bắt đầu bởi giả sử rằng trường $K$ là không trường của characteristic $2$. Nhắc lại rằng ánh xạ tuyến tính (linear map) $f$: $E \to E$ là phép đối hợp (involution) khi và chỉ khi $f^{2} =$ id, và là lũy đẳng (idempotent) khi và chỉ khi $f^{2} = f$. Ta biết từ Mệnh đề 6.9 rằng nếu $f$ là lũy đẳng (idempotent), thì
$$E = \mathrm{Im}(f) \oplus \mathrm{Ker} (f),$$
Và rằng thu hẹp của $f$ đến ảnh (ảnh (image)) của nó là đồng nhất thức. Cho điều này lý do, tuyến tính lũy đẳng (idempotent) ánh xạ được gọi là một phép chiếu. connection giữa các phép đối hợp và các phép chiếu được cho bởi sau đây đơn giản mệnh đề.

> **Mệnh đề 14.22.** Với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$, ta có $f^{2} =$ id $iff_{2}^{1}(id$ - $f)$ là phép chiếu $iff_{2}^{1}(id + f)$ là phép chiếu; trong trường hợp này, $f$ bằng difference của hai $projections_{2}^{1}$ (id $+ f) and_{2}^{1}$ (id - $f)$.

*Chứng minh.* Ta có
$$2$$
$$\begin{pmatrix} 1 \\ (id -f) \\ 2 \end{pmatrix} = \frac{1}{4} (id -2f + f^{2})$$
Do đó
$$2$$
$$\begin{pmatrix} 1 \\ (id -f) \\ 2 \end{pmatrix} = \frac{1}{2} (id -f)iff f^{2}= id.$$
Ta cũng có
$$2$$
$$\begin{pmatrix} 1 \\ (id + f) \\ 2 \end{pmatrix} = \frac{1}{4} (id + 2f + f^{2}),$$
Do đó
$$2$$
$$\begin{pmatrix} 1 \\ (id + f) \\ 2 \end{pmatrix} = \frac{1}{2} (id + f)iff f^{2}= id.$$
Hiển nhiên, $f =_{2}^{1}$ (id $+ f) -_{2}^{1}(id$ - $f)$.

> **Mệnh đề 14.23.** Với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$, cho $U^{+} =$ Ker $(_{2}^{1}(id$ - $f))$ và cho $U^{-} = Im(_{2}^{1}(id$ - $f))$. Nếu $f^{2} =$ id, thì
$$U^{+}= \mathrm{Ker} \begin{pmatrix} 1 \\ (id -f) \\ 2 \end{pmatrix} = \mathrm{Im} \begin{pmatrix} 1 \\ (id + f) \\ 2 \end{pmatrix} ,$$
Và do đó, f(u) $= u$ trên $U^{+}$ và f(u) $= -u$ trên $U^{-}$.

*Chứng minh.* Nếu $f^{2} =$ id, thì
$$(id -f) \circ (id + f) = id -f^{2}= id -id = 0,$$
Mà suy ra rằng
$$\mathrm{Im} \begin{pmatrix} 1 \\ (id + f) \\ 2 \end{pmatrix} \subseteq \mathrm{Ker} \begin{pmatrix} 1 \\ (id -f) \\ 2 \end{pmatrix} .$$

<!-- PAGE 554 -->
$$Conversely, if u \in Ker_{2}^{1} \begin{pmatrix} (id -f) \end{pmatrix} , then f(u) = u, so$$
$$\frac{1}{2} (id + f)(u) = \frac{1}{2} (u + u) = u,$$
Và do đó
$$\mathrm{Ker} \begin{pmatrix} 1 \\ (id -f) \\ 2 \end{pmatrix} \subseteq \mathrm{Im} \begin{pmatrix} 1 \\ (id + f) \\ 2 \end{pmatrix} .$$
Vì vậy,
$$U^{+}= \mathrm{Ker} \begin{pmatrix} 1 \\ (id -f) \\ 2 \end{pmatrix} = \mathrm{Im} \begin{pmatrix} 1 \\ (id + f) \\ 2 \end{pmatrix} ,$$
Và do đó, f(u) $= u$ trên $U^{+}$ và f(u) $= -u$ trên $U^{-}$. Ta bây giờ giả sử rằng $K =\mathbb{C}$. các phép đối hợp của $E$ rằng là unita các phép biến đổi được đặc trưng hóa như sau.

> **Mệnh đề 14.24.** Cho $f \in$ GL(E) là phép đối hợp (involution). Các tính chất sau đây là tương đương:
() ánh xạ $f$ là unitary; nghĩa là, $f \in$ U(E).
$(b)$ các không gian con $U^{-} = Im(_{2}^{1}(id$ - $f))$ và $U^{+} = Im(_{2}^{1}(id + f))$ là trực giao. Hơn nữa, nếu $E$ là hữu hạn chiều, thì () và $(b)$ là tương đương đến $(c)$ ở dưới:
$(c)$ ánh xạ là tự liên hợp (self-adjoint); nghĩa là, $f = f^{*}$.

*Chứng minh.* Nếu $f$ là unita, thì từ $\langle$ f(u), $f(v)\rangle = \langle u, v\rangle$ với mọi $u, v \in E$, ta xem rằng nếu $u \in U^{+}$ và $v \in U^{-}$, ta thu được
$$\langle u, v\rangle = \langle f(u), f(v)\rangle = \langle u, -v\rangle = -\langle u, v\rangle ,$$
Do đó $2\langle u, v\rangle = 0$, mà suy ra $\langle u, v\rangle = 0$, nghĩa là, $U^{+}$ và $U^{-}$ là trực giao. Do đó, () suy ra $(b)$. Ngược lại, nếu $(b)$ nghiệm đúng, vì f(u) $= u$ trên $U^{+}$ và f(u) $= -u$ trên $U^{-}$, ta xem rằng $\langle$ f(u), $f(v)\rangle = \langle u, v\rangle$ nếu $u, v \in U^{+}$ hoặc nếu $u, v \in U^{-}$. Vì $E = U^{+} \oplus U^{-}$ và vì $U^{+}$ và $U^{-}$ là trực giao, ta cũng có $\langle$ f(u), $f(v)\rangle = \langle u, v\rangle$ với mọi $u, v \in E$, và $(b)$ suy ra (). Nếu $E$ là hữu hạn chiều, liên hợp (adjoint) $f^{*}$ của $f$ tồn tại, và ta biết rằng $f^{-1} = f^{*}$. Vì $f$ là phép đối hợp (involution), $f^{2} =$ id, mà suy ra rằng $f^{*} = f^{-1} = f$. unita phép đối hợp (involution) là đồng nhất thức trên $U^{+} = Im(_{2}^{1}(id + f))$, và f(v) $= -v$ với mọi $\oplus v \in U^{-} = Im(_{2}^{1}(id-f))$. Hơn nữa, $E$ là trực giao tổng trực tiếp (direct sum) $E = U^{+} U^{-}$. Ta nói rằng $f$ là trực giao phép đối xứng (reflection) về $U^{+}$. Trong trường hợp đặc biệt khi $U^{+}$ là siêu phẳng (hyperplane), ta nói rằng $f$ là siêu phẳng (hyperplane) phép đối xứng (reflection). Ta đã studied siêu phẳng (hyperplane) các phép đối xứng trong Euclidean trường hợp; xem Chương $13$.

<!-- PAGE 555 -->
Nếu $f$: $E \to E$ là phép chiếu $(f^{2} = f)$, thì
$$(id -2f)^{2}= id -4f + 4f^{2}= id -4f + 4f = id,$$
Do đó id - 2f là phép đối hợp (involution). Hệ quả là, ta thu được kết quả sau đây.

> **Mệnh đề 14.25.** Nếu $f$: $E \to E$ là phép chiếu $(f^{2} = f)$, thì Ker $(f)$ và Im(f) là trực giao khi và chỉ khi $f^{*} = f$.

*Chứng minh.* Áp dụng Mệnh đề 14.24 đến $g =$ id - 2f. Vì id - $g =$ 2f ta có
$$U^{+}= \mathrm{Ker} \begin{pmatrix} 1 \\ (id -g) \\ 2 \end{pmatrix} = \mathrm{Ker} (f)$$
Và
$$U^{-} = \mathrm{Im} \begin{pmatrix} 1 \\ (id -g) \\ 2 \end{pmatrix} = \mathrm{Im}(f),$$
Mà chứng minh mệnh đề. phép chiếu sao cho $f = f^{*}$ được gọi là một phép chiếu trực giao (orthogonal projection). Nếu $(a_{1} \dots  , a_{k})$ là $k$ các vectơ độc lập tuyến tính (linearly independent) trong $\mathbb{R}^{n}$, cho chúng ta xác định ma trận $P$ của
$$\mathbb{R}^{n}$$
Phép chiếu trực giao (orthogonal projection) lên không gian con của được sinh (spanned) bởi $(a_{1}, \dots  , a_{k})$. Cho $A$ là ma trận cỡ $n\times k$ có cột thứ $j$ bao gồm của các tọa độ của vectơ $a_{j}$ trên cơ sở chính tắc (canonical basis) $(e_{1}, \dots  , e_{n})$. Bất kỳ vectơ trong không gian con $(a_{1}, \dots  , a_{k})$ là tổ hợp tuyến tính (linear combination) của tạo thành Ax, với một số $x \in \mathbb{R}^{k}$. Cho trước bất kỳ $y \in \mathbb{R}^{n}$, phép chiếu trực giao (orthogonal projection) Py $=$ Ax của $y$ lên không gian con được sinh (spanned) bởi $(a_{1}, \dots  , a_{k})$ là vectơ Ax sao cho $y$ - Ax là trực giao đến không gian con được sinh (spanned) bởi $(a_{1}, \dots  , a_{k})$ (chứng minh nó). Điều này có nghĩa là $y$ - Ax là trực giao đến mọi $a_{j}$, mà được biểu diễn bởi
$$A^{\top}(y -Ax) = 0;$$
Rằng là,
$$A^{\top}Ax = A^{\top}y.$$
Ma trận $A^{\top}A$ là khả nghịch bởi vì $A$ có đầy đủ hạng (rank) $k$, do đó ta thu được
$$x = (A^{\top}A)^{-1}A^{\top}y,$$
Và do đó
$$Py = Ax = A(A^{\top}A)^{-1}A^{\top}y.$$
Vì vậy, ma trận $P$ của phép chiếu lên không gian con được sinh (spanned) bởi $(a_{1} \dots  , a_{k})$ được cho bởi
$$P = A(A^{\top}A)^{-1}A^{\top}.$$
Độc giả nên kiểm tra rằng $P^{2} = P$ và $P^{\top} = P$.
