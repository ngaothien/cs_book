# Các tổng quát hóa của Phương pháp Newton (Newton's method)


<!-- PAGE 1525 -->
Trường hợp của thực hàm suggests sau đây phương pháp cho việc tìm các không điểm của hàm $f$: $\Omega \to Y$, với $\Omega \subseteq X$: cho trước bắt đầu điểm $x_{0} \in \Omega$, dãy $(x_{k})$ được định nghĩa bởi
$$x_{k+1} = x_{k} -(f' (x_{k}))^{-1}(f(x_{k}))(*)$$
Với mọi $k \ge 0$. Cho ở trên để tạo nghĩa, nó phải là ensured rằng
$(1)$ Tất cả các điểm $x_{k}$ vẫn là trong phạm vi $\Omega$.
$(2)$ hàm $f$ là khả vi (differentiable) trong phạm vi $\Omega$.
$(3)$ đạo hàm f' $(x)$ là song ánh từ $X$ đến $Y$ với mọi $x \in \Omega$. Các phần tử này là khá demanding các điều kiện nhưng có đủ các điều kiện rằng đảm bảo rằng chúng là met. Một cái khác thực tế vấn đề là rằng nó có thể là rất một cách chi phí để tính (f' $(x_{k}))^{-1}$ tại mọi vòng lặp bước. Trong mục tiếp theo ta investigate các tổng quát hóa của Newton’s phương pháp mà address các vấn đề rằng ta chỉ được thảo luận.

## 41.2 Các tổng quát hóa của Newton’s Phương pháp

$$\mathbb{R}^{n} \mathbb{R}\mathbb{R}^{n}$$
Giả sử rằng $f$: $\Omega \to$ được cho bởi $n$ các hàm $f_{i}$: $\Omega \to$, ở đâu $\Omega \subseteq$. Trong trường hợp này, việc tìm không của $f$ là tương đương đến việc giải hệ
$$f_{1}(a_{1} \dots  , a_{n}) = 0$$
$$f_{2}(a_{1} \dots  , a_{n}) = 0$$
$$\vdots$$
$$f_{n}(a_{1} \dots  , a_{n}) = 0.$$
Trong tiêu chuẩn Newton phương pháp, vòng lặp bước được cho bởi (*), cụ thể là
$$x_{k+1} = x_{k} -(f' (x_{k}))^{-1}(f(x_{k})),$$
Và nếu ta định nghĩa $\Delta x_{k}$ như $\Delta x_{k} = x_{k+1}$ - $x_{k}$, ta xem rằng $\Delta x_{k} =$ -(f' $(x_{k}))^{-1}(f(x_{k}))$, do đó $\Delta x_{k}$ là thu được bởi việc giải phương trình
$$f' (x_{k})\Delta x_{k} = -f(x_{k}),$$
Và thì ta tập hợp $x_{k+1} = x_{k} + \Delta x_{k}$. tổng quát hóa là như sau. Biến thể $1$. đơn lẻ vòng lặp của Newton’s phương pháp bao gồm trong việc giải hệ phương trình tuyến tính
$$(J(f)(x_{k}))\Delta x_{k} = -f(x_{k}),$$

<!-- PAGE 1526 -->
Và thì đặt
$$x_{k+1} = x_{k} + \Delta x_{k},$$
$$where J(f)(x_{k}) =_{\partial x}^{\partial fi} \begin{pmatrix} (x_{k}) \\ \overline{j} \\ verycostly \end{pmatrix} is the Jacobian matrix of f at x_{k}.$$
Nói chung nó là để tính $J(f)(x_{k})$ tại mỗi vòng lặp và thì để giải tương ứng hệ phương trình tuyến tính. Nếu phương pháp hội tụ, liên tiếp các vectơ $x_{k}$ nên khác nhau chỉ little, như cũng tương ứng các ma trận $J(f)(x_{k})$. Do đó, ta là đã dẫn đến đến một vài các biến thể của Newton’s phương pháp. Biến thể $2$. Điều này biến thể bao gồm trong giữ cùng ma trận cho $p$ liên tiếp các bước (ở đâu $p$ là một số cố định số nguyên $\ge 2)$:
$$x_{k+1} = x_{k} -(f' (x_{0}))^{-1}(f(x_{k})),0 \le k \le p -1$$
$$x_{k+1} = x_{k} -(f' (x_{p}))^{-1}(f(x_{k})),p \le k \le 2p -1$$
$$\vdots$$
$$x_{k+1} = x_{k} -(f' (x_{rp}))^{-1}(f(x_{k})),rp \le k \le (r + 1)p -1$$
$$\vdots$$
Biến thể $3$. Tập hợp $p = \infty$, nghĩa là, sử dụng cùng ma trận f' $(x_{0})$ với mọi các vòng lặp, mà dẫn đến đến các vòng lặp của tạo thành
$$x_{k+1} = x_{k} -(f' (x_{0}))^{-1}(f(x_{k})),k \ge 0,$$
Biến thể $4$. Thay thế f' $(x_{0})$ bởi cụ thể ma trận $A_{0}$ mà là dễ đến nghịch đảo:
$$x_{k+1} = x_{k} -A_{0}^{-1} f(x_{k}),k \ge 0.$$
Trong cuối cùng hai các trường hợp, nếu khả dĩ/có thể, ta sử dụng LU nhân tử hóa của f' $(x_{0})$ hoặc $A_{0}$ đến speed lên phương pháp. Trong một số các trường hợp, nó có thể chẵn/ngay cả khả dĩ/có thể đến tập hợp $A_{0} =$ I. ở trên considerations dẫn đến chúng ta đến định nghĩa của suy rộng/tổng quát hóa Newton phương pháp, như trong Ciarlet $[41]$ (Chương $7)$. Nhắc lại rằng ánh xạ tuyến tính (linear map) $f \in$ L(E; $F)$ được gọi là một đẳng cấu khi và chỉ khi $f$ là liên tục, song ánh (bijective), và $f^{-1}$ là cũng liên tục.

> **Định nghĩa 41.1.** Nếu $X$ và $Y$ là hai các không gian vectơ định chuẩn và nếu $f$: $\Omega \to Y$ là hàm từ một số mở tập con $\Omega$ của $X$, suy rộng/tổng quát hóa Newton phương pháp cho việc tìm các không điểm của $f$ bao gồm của
$(1) A$ dãy của các họ $(A_{k}(x))$ của tuyến tính các đẳng cấu từ $X$ đến $Y$, với mọi $x \in \Omega$ và tất cả các số nguyên $k \ge 0$;
$(2)$ Một số bắt đầu điểm $x_{0} \in \Omega$;

<!-- PAGE 1527 -->
$(3) A$ dãy $(x_{k})$ của các điểm của $\Omega$ được định nghĩa bởi
$$x_{k+1} = x_{k} -(A_{k}(x_{\ell}))^{-1}(f(x_{k})),k \ge 0,(**)$$
Ở đâu với mọi số nguyên $k \ge 0$, số nguyên $\ell$ thỏa mãn điều kiện
$$0 \le \ell \le k.$$
Với $\Delta x_{k} = x_{k+1}$ - $x_{k}$, Phương trình (**) là tương đương đến việc giải phương trình
$$A_{k}(x_{\ell})(\Delta x_{k}) = -f(x_{k})$$
Và đặt $x_{k+1} = x_{k} + \Delta x_{k}$. hàm $A_{k}(x)$ thường phụ thuộc vào f'. Định nghĩa 41.1 cho chúng ta đủ flexibility đến capture tất cả các tình huống rằng ta có một cách trước đó được thảo luận:
$$FunctionIndex$$
Biến thể $1: A_{k}(x) =$ f' $(x), \ell = k$ Biến thể $2: A_{k}(x) =$ f' $(x), \ell = min{rp, k}$, nếu rp $\le k \le (r +$ 1)p - $1, r \ge 0$ Biến thể $3: A_{k}(x) =$ f' $(x), \ell = 0$ Biến thể $4: A_{k}(x) = A_{0}$, ở đâu $A_{0}$ là tuyến tính đẳng cấu từ $X$ đến $Y$. trường hợp thứ nhất tương ứng với Newton’s ban đầu phương pháp và những cái khác đến các biến thể rằng ta chỉ được thảo luận. Ta có thể cũng có $A_{k}(x) = A_{k}$, cố định tuyến tính đẳng cấu độc lập của $x \in \Omega$.

> **Ví dụ 41.2.** Xét ma trận hàm $f$ cho trước bởi
$$f(X) = A -X^{-1},$$
Với $A$ và $X$ khả nghịch $n \times  n$ các ma trận. Nếu ta áp dụng Biến thể $1$ của Newton’s phương pháp bắt đầu với bất kỳ ma trận cỡ $n \times  n$ $X_{0}$, vì đạo hàm của hàm $g$ cho trước bởi g(X) $= X^{-1}$ là $dg_{X}(Y$) $= -X^{-1}Y X^{-1}$, ta có
$$f_{X}' (Y ) = X^{-1}Y X^{-1},$$
Do đó
$$(f_{X}' )^{-1}(Y ) = XY X$$
Và Newton bước là
$$X_{k+1} = X_{k} -(f_{Xk}' )^{-1}(f(X_{k})) = X_{k} -X_{k}(A -X_{k}^{-1} )X_{k},$$
Mà cho ta dãy $(X_{k})$ với
$$X_{k+1} = X_{k}(2I -AX_{k}),k \ge 0.$$
Trong Bài toán 41.5, nó được hiển thị rằng Newton’s phương pháp hội tụ đến $A^{-1}$ khi và chỉ khi bán kính phổ (spectral radius) của I - $X_{0}A$ là chặt nhỏ hơn hơn $1$, nghĩa là, $\rho$ (I - $X_{0}A) < 1$.

<!-- PAGE 1528 -->
Sau đây định lý inspired bởi Newton–Kantorovich định lý cho đủ các điều kiện rằng đảm bảo rằng dãy $(x_{k})$ được xây dựng bởi suy rộng/tổng quát hóa Newton phương pháp hội tụ đến không của $f$ close đến $x_{0}$. Mặc dù khá technical, các điều kiện này là không rất đáng ngạc nhiên.

> **Định lý 41.1.** Cho $X$ là Không gian Banach (Banach space), cho $f$: $\Omega \to Y$ là khả vi (differentiable) trên mở tập con $\Omega \subseteq X$, và giả sử rằng có các hằng số $r, M, \beta  > 0$ sao cho nếu ta cho
$$B = {x \in X | \|x -x_{0}\|\le r} \subseteq \Omega ,$$
Thì $(1)$
$$supsup

$A_{k}^{-1} (x)_{L(Y;X)} \le$ M,$$
$$k\ge 0x\in B$$
$(2) \beta  < 1$ và
$$supsup\|f' (x) -A_{k}(x')\|_{L(X;Y)} \le \frac{\beta}{M}$$
$$k\ge 0x,x'\in B$$
$(3)$
$$\|f(x_{0})\|\le \frac{r}{M} (1 -\beta ).$$
Thì dãy $(x_{k})$ được định nghĩa bởi
$$x_{k+1} = x_{k} -A_{k}^{-1} (x_{\ell})(f(x_{k})),0 \le \ell \le k$$
Là hoàn toàn được chứa trong phạm vi $B$ và hội tụ đến không của $f$, mà là chỉ không của $f$ trong $B$. Hơn nữa, sự hội tụ là hình học, mà có nghĩa là
$$\| -\|$$
$$\|x_{k} -a\|\le \frac{x_{1}x_{0}}{1 -\beta} \beta^{k} .$$

*Chứng minh.* Ta suy ra Ciarlet $[41]$ (Định lý 7.5.1, Mục 7.5). chứng minh có ba các bước. Bước $1$. Ta thiết lập sau đây các bất đẳng thức với mọi $k \ge 1$.
$$\|x_{k} -x_{k-1}\|\le M \|f(x_{k-1})\|(a)$$
$$\|x_{k} -x_{0}\|\le r(x_{k} \in B)(b)$$
$$\|f(x_{k})\|\le \frac{\beta}{M} \|x_{k} -x_{k-1}\|.(c)$$
Ta tiến hành bằng quy nạp theo $k$, bắt đầu với base trường hợp $k = 1$. Vì
$$x_{1} = x_{0} -A_{0}^{-1} (x_{0})(f(x_{0})),$$

<!-- PAGE 1529 -->
Ta có $x_{1}$ - $x_{0} = -A_{0}^{-1} (x_{0})(f(x_{0}))$, do đó bởi $(1)$ và $(3)$ và vì $0 < \beta  < 1$, ta có
$$\|x_{1} -x_{0}\|\le M \|f(x_{0})\|\le r(1 -\beta ) \le r,$$
Thiết lập () và $(b)$ cho $k = 1$. Ta cũng có $f(x_{0}) = -A_{0}(x_{0})(x_{1}$ - $x_{0})$, do đó $-f(x_{0})$ - $A_{0}(x_{0})(x_{1}$ - $x_{0}) = 0$ và do đó
$$f(x_{1}) = f(x_{1}) -f(x_{0}) -A_{0}(x_{0})(x_{1} -x_{0}).$$
Bởi có nghĩa giá trị định lý (Mệnh đề 39.12) ứng dụng đến hàm $x \mapsto f(x)-A_{0}(x_{0})(x)$, bởi $(2)$, ta thu được
$$\|f(x_{1})\|\le \sup\|f' (x) -A_{0}(x_{0})\|\|x_{1} -x_{0}\|\le \frac{\beta}{M} \|x_{1} -x_{0}\|,$$
$$x\in B$$
Mà là $(c)$ cho $k = 1$. Ta bây giờ thiết lập quy nạp bước. Vì theo Định nghĩa
$$x_{k} -x_{k-1} = -A_{k-1}^{-1}(x_{\ell})(f(x_{k-1})),0 \le \ell \le k -1,$$
Bởi $(1)$ và sự kiện rằng theo giả thiết quy nạp cho $(b), x_{\ell} \in B$, ta thu được
$$\|x_{k} -x_{k-1}\|\le M \|f(x_{k-1})\|,$$
Mà chứng minh () cho $k$. Hệ quả là, vì theo giả thiết quy nạp cho $(c)$,
$$\|f(x_{k-1})\|\le \frac{\beta}{M} \|x_{k-1} -x_{k-2}\|,$$
Ta thu được
$$\|x_{k} -x_{k-1}\|\le M \|f(x_{k-1})\|\le \beta  \|x_{k-1} -x_{k-2}\|,(*_{1})$$
Và bởi repeating bước này,
$$\|x_{k} -x_{k-1}\|\le \beta^{k-1} \|x_{1} -x_{0}\|.(*_{2})$$
Bằng cách sử dụng $(*_{2})$ và $(3)$, ta thu được
$$!$$
$$\|x_{k} -x_{0}\|\le \sum_{j=1}^{k}  \|x_{j} -x_{j-1}\|\le \sum_{j=1}^{k}  \beta^{j-1} \|x_{1} -x_{0}\|$$
$$\| -\|$$
$$\le \frac{x_{1}x_{0}}{1 -\beta} \le \frac{M}{1 -\beta} \|f(x_{0})\|\le r,$$
Mà chứng tỏ rằng $x_{k} \in B$, mà là $(b)$ cho $k$. Vì
$$x_{k} -x_{k-1} = -A_{k-1}^{-1}(x_{\ell})(f(x_{k-1}))$$

<!-- PAGE 1530 -->
Ta cũng có $f(x_{k-1}) = -A_{k-1}(x_{\ell})(x_{k}$ - $x_{k-1})$, do đó ta có
$$f(x_{k}) = f(x_{k}) -f(x_{k-1}) -A_{k-1}(x_{\ell})(x_{k} -x_{k-1}),$$
Và như trong base trường hợp, áp dụng có nghĩa giá trị định lý (Mệnh đề 39.12) đến hàm $x \mapsto$ f(x) - $A_{k-1}(x_{\ell})(x)$, bởi $(2)$, ta thu được
$$\|f(x_{k})\|\le \sup\|f' (x) -A_{k-1}(x_{\ell})\|\|x_{k} -x_{k-1}\|\le \frac{\beta}{M} \|x_{k} -x_{k-1}\|,$$
$$x\in B$$
Chứng minh $(c)$ cho $k$. Bước $2$. Chứng minh rằng $f$ có không trong $B$. Đến thực hiện điều này ta chứng minh rằng $(x_{k})$ là Dãy Cauchy (Cauchy sequence). Điều này là bởi vì, bằng cách sử dụng $(*_{2})$, ta có
$$!$$
$$\|x_{k+j} -x_{k}\|\le \sum_{i=0}^{j-1}  \|x_{k+i+1} -x_{k+i}\|\le \beta^{k} \sum_{i=0}^{j-1}  \beta^{i} \|x_{1} -x_{0}\|$$
$$\le \frac{\beta^{k}}{1 -\beta} \|x_{1} -x_{0}\|,$$
Với mọi $k \ge 0$ và tất cả $j \ge 0$, chứng minh rằng $(x_{k})$ là Dãy Cauchy (Cauchy sequence). Vì $B$ là hình cầu đóng (closed ball) trong đầy đủ không gian vectơ định chuẩn (normed vector space), $B$ là đầy đủ và Dãy Cauchy (Cauchy sequence) $(x_{k})$ hội tụ đến giới hạn $a \in B$. Vì $f$ là liên tục trên $\Omega$ (bởi vì nó là khả vi (differentiable)), bởi $(c)$ ta thu được
$$\beta$$
$$\|f(a)\|= lim\|f(x_{k})\|\le  lim\|x_{k} -x_{k-1}\|= 0,$$
$$k\mapsto \infty \overline{M}_{k\mapsto \infty}$$
Mà cho ta f() $= 0$. Vì
$$\|x_{k+j} -x_{k}\|\le \frac{\beta^{k}}{1 -\beta} \|x_{1} -x_{0}\|,$$
Nếu ta cho $j$ tiến tới đến vô cực, ta thu được bất đẳng thức
$$\|x_{k} -a\|= \|a -x_{k}\|\le \frac{\beta^{k}}{1 -\beta} \|x_{1} -x_{0}\|,$$
Mà là cuối cùng phát biểu của định lý. Bước $3$. Chứng minh rằng $f$ có duy nhất không trong $B$. Giả sử f() $=$ f(b) $= 0$ với, $b \in B$. Vì $A_{0}^{-1} (x_{0})(A_{0}(x_{0})(b$ - $a)) = b$ - $a$, ta có
$$b -a = -A_{0}^{-1} (x_{0})(f(b) -f(a) -A_{0}(x_{0})(b -a)),$$
Mà bởi $(1)$ và $(2)$ và có nghĩa giá trị định lý suy ra rằng
$$\|b -a\|\le

$A_{0}^{-1} (x_{0})$

$\sup\|f' (x) -A_{0}(x_{0})\|\|b -a\|\le \beta  \|b -a\|.$$$
$$x\in B$$
Vì $0 < \beta  < 1$, bất đẳng thức $\|b$ - $a\|\le \beta  \|b$ - $a\|$ là chỉ khả dĩ/có thể nếu $a = b$.

<!-- PAGE 1531 -->
Nó nên được quan sát rằng các điều kiện của Định lý 41.1 là typically khá stringent. Nó có thể được được hiển thị rằng Định lý 41.1 áp dụng đến hàm $f$ của Ví dụ 41.1 cho trước bởi f(x) $= x^{2}$ - $\alpha$ với $\alpha  > 0$, với mọi $x_{0} > 0$ sao cho
$$\frac{6}{7} \alpha  \le x_{0}^{2} \le \frac{6}{5} \alpha ,$$
$$\sqrt$$
Với $\beta  = 2/5, r = (1/6)x_{0}, M = 3/(5x_{0})$. Như vậy các giá trị của $x_{0}$ là khá close đến $\overline{\alpha}$. Nếu ta giả sử rằng ta đã biết rằng một số phần tử $a \in \Omega$ là không của $f$, tiếp theo định lý cho đủ các điều kiện cho đặc biệt phiên bản của suy rộng/tổng quát hóa Newton phương pháp đến hội tụ. Cho điều này đặc biệt phương pháp tuyến tính các đẳng cấu $A_{k}(x)$ là độc lập của $x \in \Omega$.

> **Định lý 41.2.** Cho $X$ là Không gian Banach (Banach space) và cho $f$: $\Omega \to Y$ là khả vi (differentiable) trên mở tập con $\Omega \subseteq X$. Nếu $a \in \Omega$ là điểm sao cho f() $= 0$, nếu f' () là tuyến tính đẳng cấu, và nếu tồn tại một $\lambda$ với $0 < \lambda  < 1/2$ sao cho
$$\sup\|A_{k} -f' (a)\|_{L(X;Y)} \le \frac{\lambda}{\|(f'(a))^{-1}\|_{L(Y;X)}} ,$$
$$k\ge 0$$
Thì có một hình cầu đóng (closed ball) $B$ của tâm sao cho với mọi $x_{0} \in B$, dãy $(x_{k})$ được định nghĩa bởi
$$x_{k+1} = x_{k} -A_{k}^{-1} (f(x_{k})),k \ge 0,$$
Là hoàn toàn được chứa trong phạm vi $B$ và hội tụ đến, mà là chỉ không của $f$ trong $B$. Hơn nữa, sự hội tụ là hình học, mà có nghĩa là
$$\|x_{k} -a\|\le \beta^{k} \|x_{0} -a\|,$$
Với một số $\beta  < 1$. chứng minh của Định lý 41.2 có thể được tìm thấy trong Ciarlet $[41]$ (Mục 7.5). Cho sake của tính đầy đủ, ta phát biểu phiên bản của Newton–Kantorovich định lý mà tương ứng với trường hợp ở đâu $A_{k}(x) =$ f' $(x)$. Trong điều này instance, mạnh hơn kết quả có thể được thu được especially regarding trên các cận, và ta phát biểu phiên bản do Gragg và Tapia mà xuất hiện trong Bài toán 7.5-4 của Ciarlet $[41]$.

> **Định lý 41.3.** (Newton–Kantorovich) Cho $X$ là Không gian Banach (Banach space), và cho $f$: $\Omega \to Y$ là khả vi (differentiable) trên mở tập con $\Omega \subseteq X$. Giả sử rằng ở đó tồn tại ba dương các hằng số $\lambda , \mu , \nu$ và điểm $x_{0} \in \Omega$ sao cho
$$0 < \lambda \mu \nu  \le \frac{1}{2} ,$$

<!-- PAGE 1532 -->
Và nếu ta cho
$$-\sqrt$$
$$\overline{-}$$
$$\rho^{-} = \frac{1\overline{1}\overline{2}\overline{\lambda \mu \nu}}{\sqrt\mu \nu}$$
$$\overline{-}$$
$$\rho^{+} = \frac{1 +\overline{1}\overline{2}\overline{\lambda \mu \nu}}{\mu \nu}$$
$$B = {x \in X | \|x -x_{0}\|< \rho^{-} }$$
$$\Omega^{+} = {x \in \Omega | \|x -x_{0}\|< \rho^{+} },$$
Thì $\overline{B} \subseteq \Omega$, f' $(x_{0})$ là đẳng cấu của $\mathcal{L}(X; Y$), và
$$(f'(x_{0}))^{-1}

$\le \mu$,$$
$$(f'(x_{0}))^{-1}f(x_{0})

$\le \lambda$,$$
$$\sup \|f'(x) -f'(y)\|\le \nu  \|x -y\|.$$
$$x,y\in \Omega +$$
Thì f' $(x)$ là đẳng cấu của $\mathcal{L}(X; Y$) với mọi $x \in B$, và dãy được định nghĩa bởi
$$x_{k+1} = x_{k} -(f' (x_{k}))^{-1}(f(x_{k})),k \ge 0$$
Là hoàn toàn được chứa trong phạm vi hình cầu $B$ và hội tụ đến không của $f$ mà là chỉ không của $f$ trong $\Omega^{+}$. Cuối cùng, nếu ta viết $\theta  = \rho^{-} /\rho^{+}$, thì ta có kết quả sau các cận:
$$\overline{-}$$
$$\|x_{k} -a\|\le \frac{2\sqrt{1}\overline{2}\overline{\lambda \mu \nu}}{\lambda \mu \nu} \frac{\theta^{2k}}{1 -\theta^{2k}} \|x_{1} -x_{0}\|if \lambda \mu \nu  < \frac{1}{2}$$
$$\| -\|$$
$$\|x_{k} -a\|\le \frac{x_{1}x_{0}}{2^{k-1}} if \lambda \mu \nu  = \frac{1}{2} ,$$
Và
$$\| -\|$$
$$\frac{2x_{k+1}x_{k}}{1 +p(1 + 4\theta^{2k} (1 + \theta^{2k} )^{-2})} \le \|x_{k} -a\|\le \theta^{2k-1} \|x_{k} -x_{k-1}\|.$$
Ta có thể bây giờ specialize Các định lý 41.1 và 41.2 đến search của các không điểm của đạo hàm $\mathbb{R}$ J': $\Omega \to$ E', của hàm $J$: $\Omega \to$, với $\Omega \subseteq E$. đạo hàm thứ hai J'' của $J$ là
$$\mathbb{R}$$
Liên tục dạng song tuyến tính (bilinear form) J'': $E \times  E \to$, nhưng là là thuận tiện đến quan điểm nó như ánh xạ tuyến tính (linear map) trong $\mathcal{L}(E$, E'); liên tục dạng tuyến tính (linear form) J''(u) được cho bởi J''(u)(v) $=$ J''(u, $v)$. Trong của ta tiếp theo định lý, mà suy ra ngay lập tức từ Định lý 41.1, ta giả sử rằng $A_{k}(x)$ là các đẳng cấu trong $\mathcal{L}(E$, E').

> **Định lý 41.4.** Cho $E$ là Không gian Banach (Banach space), cho $J$: $\Omega \to \mathbb{R}$ là hai lần khả vi (differentiable) trên mở tập con $\Omega \subseteq E$, và giả sử rằng có các hằng số $r, M, \beta  > 0$ sao cho nếu ta cho
$$B = {x \in E | \|x -x_{0}\|\le r} \subseteq \Omega ,$$
Thì

<!-- PAGE 1533 -->
$(1)$
$$supsup

$A_{k}^{-1} (x)_{L(E';E)} \le$ M,$$
$$k\ge 0x\in B$$
$(2) \beta  < 1$ và
$$\sup\ge \sup'\in \|J''(x) -A_{k}(x')\|_{L(E;E')} \le \frac{\beta}{M}$$
$$k0x,xB$$
$(3)$
$$\|J'(x_{0})\|\le \frac{r}{M} (1 -\beta ).$$
Thì dãy $(x_{k})$ được định nghĩa bởi
$$x_{k+1} = x_{k} -A_{k}^{-1} (x_{\ell})(J'(x_{k})),0 \le \ell \le k$$
Là hoàn toàn được chứa trong phạm vi $B$ và hội tụ đến không của J', mà là chỉ không của J' trong $B$. Hơn nữa, sự hội tụ là hình học, mà có nghĩa là
$$\| -\|$$
$$\|x_{k} -a\|\le \frac{x_{1}x_{0}}{1 -\beta} \beta^{k} .$$
Trong tiếp theo định lý, mà suy ra ngay lập tức từ Định lý 41.2, ta giả sử rằng $A_{k}(x)$ là các đẳng cấu trong $\mathcal{L}(E$, E') rằng là độc lập của $x \in \Omega$.

> **Định lý 41.5.** Cho $E$ là Không gian Banach (Banach space) và cho $J$: $\Omega \to \mathbb{R}$ là hai lần khả vi (differentiable) trên mở tập con $\Omega \subseteq E$. Nếu $a \in \Omega$ là điểm sao cho J'() $= 0$, nếu J''() là tuyến tính đẳng cấu, và nếu tồn tại một $\lambda$ với $0 < \lambda  < 1/2$ sao cho
$$\sup\ge \|A_{k} -J''(a)\|_{L(E;E')} \le \frac{\lambda}{\|(J''(a))^{-1}\|_{L(E';E)}} ,$$
$$k0$$
Thì có một hình cầu đóng (closed ball) $B$ của tâm sao cho với mọi $x_{0} \in B$, dãy $(x_{k})$ được định nghĩa bởi
$$x_{k+1} = x_{k} -A_{k}^{-1} (J'(x_{k})),k \ge 0,$$
Là hoàn toàn được chứa trong phạm vi $B$ và hội tụ đến, mà là chỉ không của J' trong $B$. Hơn nữa, sự hội tụ là hình học, mà có nghĩa là
$$\|x_{k} -a\|\le \beta^{k} \|x_{0} -a\|,$$
Với một số $\beta  < 1$. Khi $E = \mathbb{R}^{n}$, Newton phương pháp cho trước theo Định lý 41.4 cho ta vòng lặp bước của tạo thành
$$x_{k+1} = x_{k} -A_{k}^{-1} (x_{\ell})\nabla J(x_{k}),0 \le \ell \le k,$$
