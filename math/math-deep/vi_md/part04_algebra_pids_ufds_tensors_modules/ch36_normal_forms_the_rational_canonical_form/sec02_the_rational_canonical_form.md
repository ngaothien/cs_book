# Dạng chính tắc hữu tỷ (rational canonical form)


<!-- PAGE 1327 -->

## 36.2 Dạng chính tắc hữu tỷ (rational canonical form)

Cho $E$ là không gian vectơ hữu hạn chiều trên trường $K$, và cho $f$: $E \to E$ là tự đồng cấu của $E$. Ta biết từ Mục 36.1 rằng có một K[X]-môđun $E_{f}$ liên kết với $f$, và rằng $E_{f}$ là sinh hữu hạn (finitely generated) môđun xoắn (torsion module) trên PID K[X]. Trong chương này, ta chỉ ra cách mà Các định lý từ Các mục 35.4 và 35.5 cho quan trọng các kết quả về cấu trúc của ánh xạ tuyến tính (linear map) $f$. Nhắc lại rằng linh hóa tử (annihilator) của không gian con $V$ là lý tưởng (ideal) $(p)$ một cách duy nhất được định nghĩa bởi chuẩn hóa (monic) đa thức $p$ được gọi là đa thức tối tiểu (minimal polynomial) của $V$. Của ta thứ nhất kết quả là thu được bởi translating phân rã sơ cấp (primary decomposition) định lý, Định lý 35.19. Nó là không cũng đáng ngạc nhiên rằng ta thu được một lần nữa Định lý 31.10!

> **Định lý 36.4.** (Phân rã sơ cấp (primary decomposition) Định lý) Cho $f$: $E \to E$ là ánh xạ tuyến tính (linear map) trên không gian vectơ hữu hạn chiều $E$ trên trường $K$. Viết đa thức tối tiểu (minimal polynomial) $m$ của $f$ như
$$m = p_{1}^{r1} \cdots  p_{k}^{rk} ,$$
Ở đâu $p_{i}$ là phân biệt bất khả quy (irreducible) chuẩn hóa (monic) các đa thức trên $K$, và $r_{i}$ là dương các số nguyên. Cho
$$W_{i} = \mathrm{Ker} (p_{i}(f)^{ri}),i = 1, \dots  , k.$$
Thì
() $E = W_{1} \oplus \cdots  \oplus W_{k}$.
$(b)$ Mỗi $W_{i}$ là bất biến dưới $f$ và phép chiếu từ $W$ lên $W_{i}$ được cho bởi đa thức trong $f$.
$(c)$ đa thức tối tiểu (minimal polynomial) của thu hẹp $f$ | $W_{i}$ của $f$ đến $W_{i}$ là $p_{i}^{ri}$.
$$\mathbb{R}^{4} \mathbb{R}^{4}$$

> **Ví dụ 36.1.** Cho $f$: $\to$ được định nghĩa như f(x, $y, z, w) = (x + w, y + z, y + z, x + w)$. Theo tiêu chuẩn cơ sở (basis), $f$ có ma trận biểu diễn
$$M = \begin{pmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 \\ 0 & 1 & 1 & 0 \\ 1 & 0 & 0 & 1 \end{pmatrix} .$$
Cơ bản phép tính chỉ ra rằng $\chi_{f} (X) = X^{2}(X$ - $2)^{2}$ và rằng $m_{f}(X) =$ X(X - $2)$. phân rã sơ cấp (primary decomposition) định lý suy ra rằng
$$\mathbb{R}^{4}$$
$$= W_{1} \oplus W_{2},W_{1} = \mathrm{Ker} (M),W_{2} = \mathrm{Ker} (M -2I).$$
Lưu ý rằng Ker $(M)$ tương ứng với không gian riêng (eigenspace) liên kết với trị riêng (eigenvalue) $0$ và có cơ sở (basis) $([-1, 0, 0, 1], [0, -1, 1, 0])$, trong khi Ker $(M$ - 2I) tương ứng với không gian riêng (eigenspace) liên kết với trị riêng (eigenvalue) $2$ và có cơ sở (basis) $([1, 0, 0, 1], [0, 1, 1, 0])$.

<!-- PAGE 1328 -->
Tiếp theo ta áp dụng Các nhân tử bất biến (invariant factors) Phân rã Định lý, Định lý 35.31, đến $E_{f}$. định lý này nói rằng rằng $E_{f}$ là đẳng cấu đến tổng trực tiếp (direct sum)
$$E_{f} \approx K[X]/(p_{1}) \oplus \cdots  \oplus K[X]/(p_{m})$$
Của $m \le n$ xích (cyclic) các môđun, ở đâu $p_{j}$ là một cách duy nhất được xác định chuẩn hóa (monic) các đa thức của bậc ít nhất $1$, sao cho
$$p_{m} | p_{m-1} | \cdots  | p_{1}.$$
Mỗi xích (cyclic) môđun $K[X]/(p_{i})$ là đẳng cấu đến xích (cyclic) không gian con cho $f$, nói $V_{i}$, có đa thức tối tiểu (minimal polynomial) là $p_{i}$. Nó là thông lệ đến renumber các đa thức $p_{i}$ như sau. $n$ các đa thức $q_{1}, \dots  , q_{n}$ được định nghĩa bởi:
$$($$
$$1if 1 \le j \le n -m$$
$$q_{j}(X) =$$
$$p_{n-j+1}(X)if n -m + 1 \le j \le n.$$
Thì ta xem rằng
$$q_{1} | q_{2} | \cdots  | q_{n},$$
Ở đâu thứ nhất $n$ - $m$ các đa thức bằng $1$, và ta có tổng trực tiếp (direct sum)
$$E = E_{1} \oplus \cdots  \oplus E_{n},$$
Ở đâu $E_{i}$ là xích (cyclic) không gian con cho $f$ có đa thức tối tiểu (minimal polynomial) là $q_{i}$. Đặc biệt, $E_{i} = (0)$ cho $i = 1, \dots  , n$ - $m$. Định lý 35.31 cũng nói rằng rằng đa thức tối tiểu (minimal polynomial) của $f$ là $q_{n} = p_{1}$. Ta tổng tất cả điều này lên trong sau đây định lý.

> **Định lý 36.5.** (Xích (cyclic) Phân rã Định lý, Thứ nhất Phiên bản) Cho $f$: $E \to E$ là tự đồng cấu trên vectơ $K$ không gian có số chiều $n$. Ở đó tồn tại $n$ chuẩn hóa (monic) các đa thức $q_{1}, \dots  , q_{n} \in$ K[X] sao cho
$$q_{1} | q_{2} | \cdots  | q_{n},$$
Và $E$ là tổng trực tiếp (direct sum)
$$E = E_{1} \oplus \cdots  \oplus E_{n}$$
Của xích (cyclic) các không gian con $E_{i} = Z(u_{i}; f)$ cho $f$, sao cho đa thức tối tiểu (minimal polynomial) của thu hẹp của $f$ đến $E_{i}$ là $q_{i}$. các đa thức $q_{i}$ thỏa mãn ở trên các điều kiện là duy nhất, và $q_{n}$ là đa thức tối tiểu (minimal polynomial) của $f$. Xét theo phép tịnh tiến điểm $(4)$ tại bắt đầu của Mục 36.1, ta biết rằng trên cơ sở (basis)
$$(u_{i}, f(u_{i}), \dots  , f^{ni-1} (u_{i}))$$

<!-- PAGE 1329 -->
Của xích (cyclic) không gian con $E_{i} = Z(u_{i}; f)$, với $n_{i} = deg(q_{i})$, ma trận của thu hẹp của $f$ đến $E_{i}$ là companion ma trận của $p_{i}(X)$, của tạo thành
$$\begin{pmatrix} 0 & 0 & 0 & \cdots & 0 & -a_{0} \\ 1 & 0 & 0 & \cdots & 0 & -a_{1} \\ 0 & 1 & 0 & \cdots & 0 & -a_{2} \\ \vdots & \ddots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \ddots & 0 & -a_{ni-2} \\ 0 & 0 & 0 & 1 & a_{ni-1} \end{pmatrix} .$$
$$\cdots -$$
Nếu ta đặt tất cả các phần tử này các cơ sở cùng nhau, ta thu được ma trận khối (block matrix) có các khối là của ở trên tạo thành. Vì vậy, ta được chứng minh kết quả sau đây.

> **Định lý 36.6.** (Dạng chính tắc hữu tỷ (rational canonical form), Thứ nhất Phiên bản) Cho $f$: $E \to E$ là tự đồng cấu trên vectơ $K$ không gian có số chiều $n$. Ở đó tồn tại $n$ chuẩn hóa (monic) các đa thức $q_{1}, \dots  , q_{n} \in$ K[X] sao cho
$$q_{1} | q_{2} | \cdots  | q_{n},$$
Với $q_{1} = \cdots  = q_{n-m} = 1$, và cơ sở (basis) của $E$ sao cho ma trận $M$ của $f$ là ma trận khối (block matrix) của tạo thành
$$M = \begin{pmatrix} M_{n-m+1} & 0 & \cdots & 0 & 0 \\ 0 & M_{n-m+2} & \cdots & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & M_{n-1} & 0 \\ 0 & 0 & \cdots & 0 & M_{n} \end{pmatrix} ,$$
Ở đâu mỗi $M_{i}$ là companion ma trận của $q_{i}$. các đa thức $q_{i}$ thỏa mãn ở trên các điều kiện là duy nhất, và $q_{n}$ là đa thức tối tiểu (minimal polynomial) của $f$.

> **Định nghĩa 36.2.** ma trận $M$ như trong Định lý 36.6 được gọi là một ma trận trong hữu tỷ tạo thành. các đa thức $q_{1}, \dots  , q_{n}$ phát sinh trong Các định lý 36.5 và 36.6 được gọi là sự đồng dạng các bất biến (hoặc các nhân tử bất biến (invariant factors)) của $f$. Định lý 36.6 chỉ ra rằng mọi ma trận là đồng dạng đến ma trận trong hữu tỷ tạo thành. Như vậy ma trận là duy nhất. Ví dụ $1$ continued: Ta sẽ tính toán dạng chính tắc hữu tỷ (rational canonical form) cho f(x, $y, z, w) = (x + w, y + z, y + z, x + w)$. difficulty trong việc tìm dạng chính tắc hữu tỷ (rational canonical form) lies trong xác định các nhân tử bất biến (invariant factors) $q_{1}, q_{2}, q_{3}, q_{4}$. Như ta sẽ một cách ngắn discover, các nhân tử bất biến (invariant factors) của $f$ tương ứng với các nhân tử bất biến (invariant factors) của $XI -M$. Xem Các mệnh đề 36.8 và 36.11. các nhân tử bất biến (invariant factors) của $XI$ - $M$ là tìm thấy bởi chuyển đổi $XI$ - $M$ đến Dạng chuẩn tắc Smith (Smith normal form). Mục 36.5 các mô tả algorithmic quy trình cho việc tính toán Dạng chuẩn tắc Smith (Smith normal form) của ma trận. Bằng cách áp dụng methodology của Mục 36.5, ta tìm rằng Dạng chuẩn tắc Smith (Smith normal form) cho

<!-- PAGE 1330 -->
$XI$ - $M$ là
$$\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & X(X-2) & 0 \\ 0 & 0 & 0 & X(X & 2) \end{pmatrix} .$$
$$-$$
Do đó các nhân tử bất biến (invariant factors) của $f$ là $q_{1} = 1 = q_{2}, q_{3} =$ X(X - $2) = q_{4}$, và Định lý 36.5 suy ra rằng
$$\mathbb{R}^{4}$$
$$= E_{1} \oplus E_{2},$$
$$\sim  \mathbb{R} - \sim  \mathbb{R} -$$
Ở đâu $E_{1} = Z(u_{1}, f) = [X]/(X(X 2))$ và $E_{2} = Z(u_{2}, f) = [X]/(X(X 2))$. không gian con $E_{1}$ có cơ sở (basis) $(u_{1}, Mu_{1})$ ở đâu $u_{1} = (1, 0, 1, 0)$ và $Mu_{1} = (1, 1, 1, 1)$, trong khi không gian con $E_{2}$ có cơ sở (basis) $(u_{2}, Mu_{2})$ ở đâu $u_{2} = (0, 0, 1, 0)$ và $Mu_{2} = (0, 1, 1, 0)$. Định lý 36.6 suy ra rằng dạng chính tắc hữu tỷ (rational canonical form) của M(f) là
$$\begin{pmatrix} 0 & 0 & 0 & 0 \\ 1 & 2 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 2 \end{pmatrix} .$$
Theo Mệnh đề 36.2, hai các ánh xạ tuyến tính (linear maps) $f$ và f' là đồng dạng khi và chỉ khi có một đẳng cấu giữa $E_{f}$ và $E_{f'}'$, và do đó bởi tính duy nhất phần của Định lý 35.31, khi và chỉ khi chúng có cùng sự đồng dạng các bất biến $q_{1}, \dots  , q_{n}$.

> **Mệnh đề 36.7.** Nếu $E$ và E' là hai hữu hạn chiều các không gian vectơ và nếu $f$: $E \to E$ và f': E' $\to$ E' là hai các ánh xạ tuyến tính (linear maps), thì $f$ và f' là đồng dạng khi và chỉ khi chúng có cùng sự đồng dạng các bất biến. effect của mở rộng trường $K$ đến trường $L$ là object của tiếp theo mệnh đề.

> **Mệnh đề 36.8.** Cho $f$: $E \to E$ là ánh xạ tuyến tính (linear map) trên vectơ $K$ không gian $E$, và cho $(q_{1}, \dots  , q_{n})$ là sự đồng dạng các bất biến của $f$. Nếu $L$ là trường mở rộng của $K$ (mà có nghĩa là $K \subseteq L)$, và nếu $E_{(L)} = L\otimes_{K}  E$ là không gian vectơ (vector space) thu được bởi mở rộng các vô hướng, và $f_{(L)} = 1_{L} \otimes f$ ánh xạ tuyến tính (linear map) của $E_{(L)}$ được cảm sinh bởi $f$, thì sự đồng dạng các bất biến của $f_{(L)}$ là $(q_{1}, \dots  , q_{n})$ được quan điểm như các đa thức trong L[X].

*Chứng minh.* Ta biết rằng $E_{f}$ là đẳng cấu đến tổng trực tiếp (direct sum)
$$E_{f} \approx K[X]/(q_{1}K[X]) \oplus \cdots  \oplus K[X]/(q_{n}K[X]),$$
Do đó bởi tenxơ với L[X] và bằng cách sử dụng Các mệnh đề 35.12 và 33.13, ta thu được L[X] $\otimes_{K[X]}  E_{f} \approx$ L[X] $\otimes_{K[X]}  (K[X]/(q_{1}K[X]) \oplus \cdots  \oplus K[X]/(q_{n}K[X]))$
$$\approx L[X] \otimes_{K[X]}  (K[X]/(q_{1}K[X])) \oplus \cdots  \oplus L[X] \otimes_{K[X]}  (K[X]/(q_{n}K[X]))$$
$$\approx (K[X]/(q_{1}K[X])) \otimes_{K[X]}  L[X] \oplus \cdots  \oplus (K[X]/(q_{n}K[X])) \otimes_{K[X]}  L[X].$$

<!-- PAGE 1331 -->
Tuy nhiên, theo Mệnh đề 35.14, ta có các đẳng cấu
$$(K[X]/(q_{i}K[X])) \otimes_{K[X]}  L[X] \approx L[X]/(q_{i}L[X]),$$
Do đó ta thu được
$$L[X] \otimes_{K[X]}  E_{f} \approx L[X]/(q_{1}L[X]) \oplus \cdots  \oplus L[X]/(q_{n}L[X]).$$
Vì $E_{f}$ là K[X]-môđun, L[X] môđun $L[X]\otimes_{K[X]}  E_{f}$ là môđun thu được từ $E_{f}$ bởi vành mở rộng K[X] $\subseteq$ L[X]. L-module $E_{(L)} = L\otimes_{K} E$ trở thành L[X]-môđun $E_{(L)f(L)}$ ở đâu
$$f_{(L)} = id_{L} \otimes_{K}  f.$$
Ta có kết quả sau mệnh đề

> **Mệnh đề 36.9.** Với mọi trường mở rộng $K \subseteq L$, và bất kỳ ánh xạ tuyến tính (linear map) $f$: $E \to E$ ở đâu $E$ là vectơ $K$ không gian, có một đẳng cấu giữa L[X]-các môđun L[X] $\otimes_{K[X]}  E_{f}$ và $E_{(L)f(L)}$.

*Chứng minh.* Thứ nhất ta định nghĩa ánh xạ $\alpha$: $L \times  E \to$ L[X] $\otimes_{K[X]}  E_{f}$ bởi
$$\alpha (\lambda , u) = \lambda  \otimes_{K[X]}  u.$$
Ta kiểm chứng được ngay rằng $\alpha$ là K-bilinear, do đó ta thu được $K$-tuyến tính ánh xạ $\alpha$: $L \otimes_{K}  E \to$
$$e$$
L[X] $\otimes_{K[X]}  E_{f}$. Bây giờ $E_{(L)} = L \otimes_{K}  E$ là L[X]-môđun $(L \otimes_{K}  E)_{f(L)}$, và cho chúng ta ký hiệu điều này vô hướng (scalar) phép nhân bởi $\odot$. Đến mô tả $\odot$ nó là đủ để định nghĩa cách mà đơn thức $aX^{k} \in$ L[X] acts trên phần tử sinh $(\lambda  \otimes_{K}  u) \in L \otimes_{K}  E$. Ta có
$$aX^{k}\odot (\lambda  \otimes_{K}  u) = a(id_{L} \otimes_{K}  f)^{k}(\lambda  \otimes_{K}  u)$$
$$= a(\lambda  \otimes_{K}  f^{k} (u))$$
$$= a\lambda  \otimes_{K}  f^{k} (u).$$
Ta khẳng định rằng $\alpha$ là thực sự L[X]-tuyến tính. Thật vậy, ta có
$$e$$
$$\alpha (aX^{k}\odot (\lambda  \otimes_{K}  u)) =\alpha (a\lambda  \otimes_{K}  f^{k}(u))$$
$$e e$$
$$= a\lambda  \otimes_{K[X]}  f^{k} (u),$$
Và bởi định nghĩa của vô hướng (scalar) phép nhân trong K[X]-môđun $E_{f}$, ta có $f^{k} (u) = X^{k}\cdot_{f} u$, do đó ta có
$$\alpha (aX^{k}\odot (\lambda  \otimes_{K}  u)) = a\lambda  \otimes_{K[X]}  f^{k}(u)$$
$$e$$
$$= a\lambda  \otimes_{K[X]}  X^{k}\cdot_{f}  u$$
$$= X^{k}\cdot  (a\lambda  \otimes_{K[X]}  u)$$
$$= aX^{k}\cdot  (\lambda  \otimes_{K[X]}  u),$$
Mà chỉ ra rằng $\alpha$ là L[X]-tuyến tính.
$$e$$

<!-- PAGE 1332 -->
Ta cũng định nghĩa ánh xạ $\beta$: L[X] $\times  E_{f} \to (L \otimes_{K}  E)_{f(L)}$ bởi
$$\beta (q(X), u) = q(X) \odot (1 \otimes_{K}  u).$$
Bằng cách sử dụng phép tính đồng dạng đến phép tính rằng ta chỉ performed, ta có thể kiểm tra rằng $\beta$ là K[X]-song tuyến tính do đó ta thu được ánh xạ $\beta$: L[X] $\otimes_{K[X]}  E_{f} \to (L \otimes_{K}  E)_{f(L)}$. Đến hoàn tất
$$e$$
Chứng minh, nó suffices để chứng minh rằng $\alpha  \circ \beta$ và $\beta  \circ \alpha$ là đồng nhất thức trên các phần tử sinh. Ta có
$$ee ee$$
$\alpha  \circ \beta$ (q(X) $\otimes_{K[X]}  u) = \alpha$ (q(X) $\odot (1 \otimes_{K}  u)) =$ q(X) $\cdot  (1 \otimes_{K[X]}  u)) =$ q(X) $\otimes_{K[X]}  u, e e  e$ và
$$\beta  \circ \alpha (\lambda  \otimes_{K}  u) =\beta (\lambda  \otimes_{K[X]}  u) = \lambda  \odot (1 \otimes_{K}  u) = \lambda  \otimes_{K}  u,$$
$$ee e$$
Mà các hoàn tất chứng minh. Theo Mệnh đề 36.9,
$$E_{(L)f(L)} \approx L[X] \otimes_{K[X]}  E_{f} \approx L[X]/(q_{1}L[X]) \oplus \cdots  \oplus L[X]/(q_{n}L[X]),$$
Mà chỉ ra rằng $(q_{1}, \dots  , q_{n})$ là sự đồng dạng các bất biến của $f_{(L)}$. Mệnh đề 36.8 justifies thuật ngữ “bất biến” trong sự đồng dạng các bất biến. Thật vậy, dưới trường mở rộng $K \subseteq L$, sự đồng dạng các bất biến của $f_{(L)}$ vẫn là cùng. Điều này là không đúng của các ước sơ cấp (elementary divisors), mà phụ thuộc vào trường; thật vậy, bất khả quy (irreducible) đa thức $p \in$ K[X] có thể split trên L[X]. Vì $q_{n}$ là đa thức tối tiểu (minimal polynomial) của $f$, ở trên lập luận cũng chỉ ra rằng đa thức tối tiểu (minimal polynomial) của $f_{(L)}$ vẫn còn cùng dưới trường mở rộng. Mệnh đề 36.8 có sau đây hệ quả.

> **Mệnh đề 36.10.** Cho $K$ là trường và cho $L \supseteq K$ là trường mở rộng của $K$. Với mọi hai các ma trận vuông $A$ và $B$ trên $K$, nếu có một ma trận khả nghịch (invertible matrix) $Q$ trên $L$ sao cho $B = QAQ^{-1}$, thì có một ma trận khả nghịch (invertible matrix) $P$ trên $K$ sao cho $B = PAP^{-1}$. Nhắc lại từ Định lý 36.3 rằng dãy của K[X]-các ánh xạ tuyến tính (linear maps)
$$E/\psi  E/\sigma  E_{f}/ 0/$$
$$0[X][X]$$
Là chính xác, và hệ quả là, $E_{f}$ là đẳng cấu đến thương của E[X] bởi Im(X1 - $\overline{f})$. Hơn nữa, bởi vì $E$ là không gian vectơ (vector space), E[X] là môđun tự do (free module) với cơ sở (basis) $(1\otimes u_{1}, \dots  , 1\otimes u_{n})$, ở đâu $(u_{1}, \dots  , u_{n})$ là cơ sở (basis) của $E$, và vì $\psi$ là đơn ánh (injective), môđun Im(X1 - $\overline{f})$ có hạng (rank) $n$. Theo Định lý 35.31, ta có đẳng cấu
$$E_{f} \approx K[X]/(q_{1}K[X]) \oplus \cdots  \oplus K[X]/(q_{n}K[X]),$$
Và theo Mệnh đề 35.32, $E[X]/Im(X1$ - $\overline{f})$ là đẳng cấu đến tổng trực tiếp (direct sum)
$$E[X]/\mathrm{Im}(X1 -\overline{f}) \approx K[X]/(p_{1}K[X]) \oplus \cdots  \oplus K[X]/(p_{n}K[X]),$$

<!-- PAGE 1333 -->
Ở đâu $p_{1}, \dots  , p_{n}$ là các nhân tử bất biến (invariant factors) của Im(X1 - $\overline{f})$ đối với E[X]. Vì $E_{f} \approx E[X]/Im(X1$ - $\overline{f})$, bởi tính duy nhất phần của Định lý 35.31 và bởi vì các đa thức là chuẩn hóa (monic), ta phải có $p_{i} = q_{i}$, cho $i = 1, \dots  , n$. Vì vậy, ta được chứng minh sau đây then chốt sự kiện:
$$Proposition 36.11. For any linear map f : E \to E over a K-vector space \frac{E}{f} of dimension$$
$n$, sự đồng dạng các bất biến của $f$ bằng các nhân tử bất biến (invariant factors) của Im(X1-) đối với E[X]. Mệnh đề 36.11 là then chốt đến việc tính toán sự đồng dạng các bất biến của ánh xạ tuyến tính (linear map). Điều này có thể được được thực hiện bằng cách sử dụng quy trình đến chuyển đổi $XI$ - $M$ đến của nó Dạng chuẩn tắc Smith (Smith normal form). Các mệnh đề 36.11 và 35.37 cho kết quả sau đây.

> **Mệnh đề 36.12.** Với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$ trên vectơ $K$ không gian $E$ có số chiều $n$, nếu $(q_{1}, \dots  , q_{n})$ là sự đồng dạng các bất biến của $f$, với mọi ma trận $M$ biểu diễn $f$ đối với bất kỳ cơ sở (basis), thì cho $k = 1, \dots  , n$ tích
$$d_{k}(X) = q_{1}(X) \cdots  q_{k}(X)$$
Là ước chung lớn nhất (gcd) của $k \times$ k-minors của ma trận $XI$ - $M$. Lưu ý rằng ma trận $XI -M$ là không có cái nào ngoài ma trận rằng cho ta đa thức đặc trưng (characteristic polynomial) $\chi_{f} (X) =$ det(XI - $M)$ của $f$.

> **Mệnh đề 36.13.** Với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$ trên vectơ $K$ không gian $E$ có số chiều $n$, nếu $(q_{1}, \dots  , q_{n})$ là sự đồng dạng các bất biến của $f$, thì các tính chất sau đây đúng:
$(1)$ Nếu $\chi_{f} (X)$ là đa thức đặc trưng (characteristic polynomial) của $f$, thì
$$\chi_{f} (X) = q_{1}(X) \cdots  q_{n}(X).$$
$(2)$ đa thức tối tiểu (minimal polynomial) m(X) $= q_{n}(X)$ của $f$ chia hết đa thức đặc trưng (characteristic polynomial) $\chi_{f} (X)$ của $f$.
$(3)$ đa thức đặc trưng (characteristic polynomial) $\chi_{f} (X)$ chia hết $m(X)^{n}$.
$(4) E$ là xích (cyclic) cho $f$ khi và chỉ khi m(X) $= \chi_{f} (X)$.

*Chứng minh.* Tính chất $(1)$ suy ra từ Mệnh đề 36.12 cho $k = n$. Nó cũng suy ra từ Định lý 36.6 và sự kiện rằng cho companion ma trận liên kết với $q_{i}$, đa thức đặc trưng (characteristic polynomial) của ma trận này là cũng $q_{i}$. Tính chất $(2)$ là hiển nhiên từ $(1)$. Vì mỗi $q_{i}$ chia hết $q_{i+1}$, mỗi $q_{i}$ chia hết $q_{n}$, do đó của chúng tích $\chi_{f} (X)$ chia hết $m(X)^{n} = q_{n}(X)^{n}$. điều kiện cuối cùng nói rằng rằng $q_{1} = \cdots  = q_{n-1} = 1$, mà có nghĩa là $E_{f}$ có đơn lẻ summand. Nhận thấy rằng Mệnh đề 36.13 cho ta một cái khác chứng minh của Cayley–Hamilton Định lý. Nó cũng suy ra rằng ánh xạ tuyến tính (linear map) là lũy linh (nilpotent) khi và chỉ khi của nó đa thức đặc trưng (characteristic polynomial) là $X^{n}$.
