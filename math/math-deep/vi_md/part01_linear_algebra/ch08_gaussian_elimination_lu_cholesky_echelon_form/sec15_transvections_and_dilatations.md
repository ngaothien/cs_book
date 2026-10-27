# Các phép trượt và Các phép vị tự


<!-- PAGE 319 -->
$1$. Như hàng phép toán, P(i, $k)$ các hoán vị hàng $i$ và hàng $k. 2$. Như cột phép toán, P(i, $k)$ các hoán vị cột $i$ và cột $k. 3$. nghịch đảo của P(i, $k)$ là P(i, $k)$ chính nó. $4$. Như hàng phép toán, $E_{i,j;\beta}$ cộng $\beta$ lần hàng $j$ đến hàng $i. 5$. Như cột phép toán, $E_{i,j;\beta}$ cộng $\beta$ lần cột $i$ đến cột $j$ (lưu ý switch trong các chỉ số). $6$. nghịch đảo của $E_{i,j;\beta}$ là $E_{i,j;-\beta}. 7$. Như hàng phép toán, $E_{i,\lambda}$ multiplies hàng $i$ bởi $\lambda$. $8$. Như cột phép toán, $E_{i,\lambda}$ multiplies cột $i$ bởi $\lambda$. $9$. nghịch đảo của $E_{i,\lambda}$ là $E_{i,\lambda-1}$. Ta có thể định nghĩa khái niệm của rút gọn cột bậc thang ma trận và chỉ ra rằng mọi ma trận có thể được rút gọn đến duy nhất rút gọn cột bậc thang tạo thành. Bây giờ cho trước bất kỳ ma trận cỡ $m \times  n$ $A$, nếu ta thứ nhất chuyển đổi $A$ đến của nó dạng bậc thang rút gọn theo hàng (RREF) $R$, nó là dễ để xem rằng ta có thể áp dụng sơ cấp cột các phép toán rằng sẽ rút gọn $R$ đến ma trận của tạo thành
$$\begin{pmatrix} I_{r} & 0_{r,n-r} \\ 0_{m-r,r} & 0_{m-r,n-r} \end{pmatrix} ,$$
Ở đâu $r$ là số của các phần tử trụ (thu được during hàng reduction). Vì vậy, với mọi $m\times n$ ma trận $A$, ở đó tồn tại hai các dãy của sơ cấp các ma trận $E_{1}, \dots  , E_{p}$ và $F_{1}, \dots  , F_{q}$, sao cho
$$E_{p} \cdots  E_{1}AF_{1} \cdots  F_{q} = \begin{pmatrix} I_{r} & 0_{r,n-r} \\ 0_{m-r,r} & 0_{m-r,n-r} \end{pmatrix} .$$
Ma trận trên vế phải được gọi là hạng (rank) chuẩn tắc/bình thường tạo thành của $A$. Rõ ràng, $r$ là hạng (rank) của $A$. Như hệ quả ta thu được kết quả sau quan trọng kết quả có chứng minh là immediate.

> **Mệnh đề 8.21.** ma trận $A$ và của nó chuyển vị (transpose) $A^{\top}$ có cùng hạng (rank).
$$⊛$$

## 8.15 Các phép trượt và Các phép vị tự

Trong mục này ta đặc trưng hóa tuyến tính các đẳng cấu của không gian vectơ (vector space) $E$ rằng để lại mọi vectơ trong một số siêu phẳng (hyperplane) cố định. các ánh xạ này turn ra là các ánh xạ tuyến tính (linear maps) rằng được biểu diễn trong một số phù hợp cơ sở (basis) bởi sơ cấp các ma trận của tạo thành $E_{i,j;\beta}$ (các phép trượt) hoặc $E_{i,\lambda}$ (các phép vị tự). Hơn nữa, các phép trượt sinh nhóm SL(E), và các phép vị tự sinh nhóm GL(E).

<!-- PAGE 320 -->
Cho $H$ là bất kỳ siêu phẳng (hyperplane) trong $E$, và chọn một số (khác không) vectơ $v \in E$ sao cho $v \in / H$, sao cho
$$E = H \oplus Kv.$$
Giả sử rằng $f$: $E \to E$ là tuyến tính đẳng cấu sao cho f(u) $= u$ với mọi $u \in H$, và rằng $f$ là không đồng nhất thức. Ta có
$$f(v) = h + \alpha v,for some h \in H and some \alpha  \in K,$$
Với $\alpha  \neq  0$, bởi vì ngược lại ta sẽ có f(v) $= h =$ f(h) vì $h \in H$, contradicting tính đơn ánh của $f (v \neq  h$ vì $v \in / H)$. Với mọi $x \in E$, nếu ta viết
$$x = y + tv,for some y \in H and some t \in K,$$
Thì
$$f(x) = f(y) + f(tv) = y + tf(v) = y + th + t\alpha v,$$
Và vì $\alpha x = \alpha y + t\alpha v$, ta thu được
$$f(x) -\alpha x = (1 -\alpha )y + th$$
$$f(x) -x = t(h + (\alpha  -1)v).$$
Nhận thấy rằng nếu $E$ là hữu hạn chiều, bởi chọn cơ sở (basis) của $E$ bao gồm của $v$ và cơ sở (basis) các vectơ của $H$, thì ma trận của $f$ là tam giác dưới (lower triangular) ma trận có đường chéo các phần tử (entries) là tất cả $1$ ngoại trừ phần tử thứ nhất mà bằng $\alpha$. Vì vậy, det(f) $= \alpha$. Trường hợp $1. \alpha  \neq  1$. Ta có f(x) $= \alpha x$ khi và chỉ khi(1 - $\alpha )y +$ th $= 0$ khi và chỉ khi
$$y = \frac{t}{\alpha  -1} h.$$
Thì nếu ta cho $w = h + (\alpha$ - 1)v, cho $y = (t/(\alpha$ - 1))h, ta có
$$x = y + tv = \frac{t}{\alpha  -1} h + tv = \frac{t}{\alpha  -1} (h + (\alpha  -1)v) = \frac{t}{\alpha  -1} w,$$
Mà chỉ ra rằng f(x) $= \alpha x$ khi và chỉ khi $x \in$ Kw. Lưu ý rằng $w \in / H$, vì $\alpha$ ̸ $= 1$ và $v \in / H$. Vì vậy,
$$E = H \oplus Kw,$$
Và $f$ là đồng nhất thức trên $H$ và magnification bởi $\alpha$ trên đường thẳng $D =$ Kw.

> **Định nghĩa 8.8.** Cho trước không gian vectơ (vector space) $E$, với mọi siêu phẳng (hyperplane) $H$ trong $E$, bất kỳ khác không vectơ $u \in E$ sao cho $u \notin H$, và bất kỳ vô hướng (scalar) $\alpha  \neq  0, 1$, ánh xạ tuyến tính (linear map) $f$ sao cho f(x) $= x$ với mọi $x \in H$ và f(x) $= \alpha x$ với mọi $x \in D =$ Ku được gọi là một phép vị tự (dilatation) của siêu phẳng (hyperplane) $H$, hướng $D$, và scale nhân tử $\alpha$.

<!-- PAGE 321 -->
Nếu $\pi_{H}$ và $\pi_{D}$ là các phép chiếu của $E$ lên $H$ và $D$, thì ta có
$$f(x) = \pi_{H} (x) + \alpha \pi_{D} (x).$$
Nghịch đảo của $f$ được cho bởi
$$f^{-1} (x) = \pi_{H} (x) + \alpha^{-1} \pi_{D} (x).$$
Khi $\alpha  = -1$, ta có $f^{2} =$ id, và $f$ là tính đối xứng về siêu phẳng (hyperplane) $H$ trong hướng $D$. tình huống này bao gồm trực giao các phép đối xứng về $H$. Trường hợp $2. \alpha  = 1$. Trong trường hợp này,
$$f(x) -x = th,$$
Rằng là, f(x) - $x \in$ Kh với mọi $x \in E$. Giả sử rằng siêu phẳng (hyperplane) $H$ là cho trước như hạt nhân (kernel) của một số dạng tuyến tính (linear form) $\phi$, và cho $a = \phi (v)$. Ta có $a \neq  0$, vì $v \in / H$. Với mọi $x \in E$, ta có
$$\phi (x -a^{-1}\phi (x)v) = \phi (x) -a^{-1}\phi (x)\phi (v) = \phi (x) -\phi (x) = 0,$$
Mà chỉ ra rằng $x$ - $a^{-1}\phi$ (x)v $\in H$ với mọi $x \in E$. Vì mọi vectơ trong $H$ là cố định bởi $f$, ta thu được
$$x -a^{-1}\phi (x)v = f(x -a^{-1}\phi (x)v)$$
$$= f(x) -a^{-1}\phi (x)f(v),$$
Do đó
$$f(x) = x + \phi (x)(f(a^{-1}v) -a^{-1}v).$$
Vì f(z) - $z \in$ Kh với mọi $z \in E$, ta kết luận rằng $u = f(a^{-1}v)$ - $a^{-1}v = \beta h$ với một số $\beta  \in K$, do đó $\phi (u) = 0$, và ta có
$$f(x) = x + \phi (x)u,\phi (u) = 0.(*)$$
Ánh xạ tuyến tính (linear map) được định nghĩa như ở trên được ký hiệu bởi $\tau_{\phi ,u}$. Ngược lại với mọi ánh xạ tuyến tính (linear map) $f = \tau_{\phi ,u}$ cho trước bởi Phương trình (*), ở đâu $\phi$ là khác không dạng tuyến tính (linear form) và $u$ là một số vectơ $u \in E$ sao cho $\phi (u) = 0$, nếu $u = 0$, thì $f$ là đồng nhất thức, do đó giả sử rằng $u \neq  0$. Nếu do đó, ta có f(x) $= x$ khi và chỉ khi $\phi (x) = 0$, nghĩa là, khi và chỉ khi $x \in H$. Ta cũng khẳng định rằng nghịch đảo của $f$ là thu được bởi thay đổi $u$ đến $-u$. Thực sự, ta kiểm tra slightly nhiều hơn/thêm tổng quát sự kiện rằng
$$\tau_{\phi ,u}  \circ \tau_{\phi ,w}  = \tau_{\phi ,u+w} .$$
Thật vậy, bằng cách sử dụng sự kiện rằng $\phi (w) = 0$, ta có
$$\tau_{\phi ,u} (\tau_{\phi ,w} (x)) = \tau_{\phi ,w} (x) + \phi (\tau_{\phi ,w} (x))u$$
$$= \tau_{\phi ,w} (x) + (\phi (x) + \phi (x)\phi (w))u$$
$$= \tau_{\phi ,w} (x) + \phi (x)u$$
$$= x + \phi (x)w + \phi (x)u$$
$$= x + \phi (x)(u + w).$$

<!-- PAGE 322 -->
Cho $v = -u$, ta có $\tau_{\phi ,u+v}  = \phi_{\phi ,0}  =$ id, do đó $\tau_{\phi ,u}^{-1}   = \tau_{\phi ,-u}$, như đã khẳng định. Vì vậy, ta được chứng minh rằng mọi tuyến tính đẳng cấu của $E$ rằng để lại mọi vectơ trong một số siêu phẳng (hyperplane) $H$ cố định và có tính chất rằng f(x) - $x \in H$ với mọi $x \in E$ được cho bởi ánh xạ $\tau_{\phi ,u}$ như đã định nghĩa bởi Phương trình (*), ở đâu $\phi$ là một số khác không dạng tuyến tính (linear form) định nghĩa $H$ và $u$ là một số vectơ trong $H$. Ta có $\tau_{\phi ,u}  =$ id khi và chỉ khi $u = 0$.

> **Định nghĩa 8.9.** Cho trước bất kỳ siêu phẳng (hyperplane) $H$ trong $E$, với mọi khác không phi tuyến tạo thành $\phi  \in E^{*}$ định nghĩa $H$ (mà có nghĩa là $H =$ Ker $(\phi$)) và bất kỳ khác không vectơ $u \in H$, ánh xạ tuyến tính (linear map) $f = \tau_{\phi ,u}$ cho trước bởi
$$\tau_{\phi ,u} (x) = x + \phi (x)u,\phi (u) = 0,$$
Với mọi $x \in E$ được gọi là một phép trượt (transvection) của siêu phẳng (hyperplane) $H$ và hướng $u$. ánh xạ $f = \tau_{\phi ,u}$ để lại mọi vectơ trong $H$ cố định, và f(x) - $x \in$ Ku với mọi $x \in E$. ở trên các đối số/lập luận chỉ ra kết quả sau đây.

> **Mệnh đề 8.22.** Cho $f$: $E \to E$ là song ánh (bijective) ánh xạ tuyến tính (linear map) và giả sử rằng f̸ $=$ id và rằng f(x) $= x$ với mọi $x \in H$, ở đâu $H$ là một số siêu phẳng (hyperplane) trong $E$. Nếu tồn tại một khác không vectơ $u \in E$ sao cho $u \in / H$ và f(u) - $u \in H$, thì $f$ là phép trượt (transvection) của siêu phẳng (hyperplane) $H$; ngược lại, $f$ là phép vị tự (dilatation) của siêu phẳng (hyperplane) $H$.

*Chứng minh.* Bằng cách sử dụng ký hiệu như ở trên, với một số $v \in / H$, ta có f(v) $= h + \alpha v$ với $\alpha  \neq  0$, và viết $u = y +$ tv với $y \in H$ và $t \neq  0$ vì $u \in / H$. Nếu f(u) - $u \in H$, từ
$$f(u) -u = t(h + (\alpha  -1)v),$$
Ta thu được $(\alpha$ - 1)v $\in H$, và vì $v \in / H$, ta phải có $\alpha  = 1$, và ta được chứng minh rằng $f$ là phép trượt (transvection). Ngược lại, $\alpha  \neq  0, 1$, và ta được chứng minh rằng $f$ là phép vị tự (dilatation). Nếu $E$ là hữu hạn chiều, thì $\alpha  =$ det(f), do đó ta cũng có kết quả sau đây.

> **Mệnh đề 8.23.** Cho $f$: $E \to E$ là song ánh (bijective) ánh xạ tuyến tính (linear map) của không gian vectơ hữu hạn chiều $E$ và giả sử rằng $f \neq$ id và rằng f(x) $= x$ với mọi $x \in H$, ở đâu $H$ là một số siêu phẳng (hyperplane) trong $E$. Nếu det(f) $= 1$, thì $f$ là phép trượt (transvection) của siêu phẳng (hyperplane) $H$; ngược lại, $f$ là phép vị tự (dilatation) của siêu phẳng (hyperplane) $H$. Giả sử rằng $f$ là phép vị tự (dilatation) của siêu phẳng (hyperplane) $H$ và hướng $u$, và nói det(f) $= \alpha  \neq  0, 1$. Chọn cơ sở (basis) $(u, e_{2}, \dots  , e_{n})$ của $E$ ở đâu $(e_{2}, \dots  , e_{n})$ là cơ sở (basis) của $H$. Thì ma trận của $f$ là của tạo thành
$$\begin{pmatrix} \alpha & 0 & \cdots & 0 \\ 0 & 1 & 0 \\ \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{pmatrix} ,$$

<!-- PAGE 323 -->
Mà là sơ cấp ma trận của tạo thành $E_{1,\alpha}$. Ngược lại, rõ ràng là mọi sơ cấp ma trận của tạo thành $E_{i,\alpha}$ với $\alpha  \neq  0, 1$ là phép vị tự (dilatation). Bây giờ, giả sử rằng $f$ là phép trượt (transvection) của siêu phẳng (hyperplane) $H$ và hướng $u \in H$. Chọn một số $v \in / H$, và chọn một số cơ sở (basis) $(u, e_{3}, \dots  , e_{n})$ của $H$, sao cho $(v, u, e_{3}, \dots  , e_{n})$ là cơ sở (basis) của $E$. Vì f(v) - $v \in$ Ku, ma trận của $f$ là của tạo thành
$$\begin{pmatrix} 1 & 0 & \cdots & 0 \\ \alpha & 1 & 0 \\ \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{pmatrix} ,$$
Mà là sơ cấp ma trận của tạo thành $E_{2,1;\alpha}$. Ngược lại, rõ ràng là mọi sơ cấp ma trận của tạo thành $E_{i,j;\alpha} (\alpha  \neq  0)$ là phép trượt (transvection). sau đây mệnh đề là thú vị bài tập rằng đòi hỏi tốt mastery của các phép biến đổi sơ cấp trên hàng $E_{i,j;\beta}$; xem Các bài tập 8.10 và 8.11.

> **Mệnh đề 8.24.** Cho trước bất kỳ khả nghịch $n \times  n$ ma trận $A$, có một ma trận $S$ sao cho
$$SA = \begin{pmatrix} I_{n-1} & 0 \\ 0 & \alpha \end{pmatrix} = E_{n,\alpha},$$
Với $\alpha  =$ det(), và ở đâu $S$ là tích của sơ cấp các ma trận của tạo thành $E_{i,j;\beta}$; nghĩa là, $S$ là hợp thành của các phép trượt. Đáng ngạc nhiên là, mọi phép trượt (transvection) là hợp thành của hai các phép vị tự!

> **Mệnh đề 8.25.** Nếu trường $K$ là không của characteristic $2$, thì mọi phép trượt (transvection) $f$ của siêu phẳng (hyperplane) $H$ có thể được viết dưới dạng $f = d_{2} \circ d_{1}$, ở đâu $d_{1}, d_{2}$ là các phép vị tự của siêu phẳng (hyperplane) $H$, ở đâu hướng của $d_{1}$ có thể được được chọn arbitrarily.

*Chứng minh.* Chọn một số phép vị tự (dilatation) $d_{1}$ của siêu phẳng (hyperplane) $H$ và scale nhân tử $\alpha  \neq  0, 1$. Thì, $d_{2} = f \circ d_{1}^{-1}$ để lại mọi vectơ trong $H$ cố định, và $det(d_{2}) = \alpha^{-1} \neq  1$. Theo Mệnh đề 8.23, ánh xạ tuyến tính (linear map) $d_{2}$ là phép vị tự (dilatation) của siêu phẳng (hyperplane) $H$, và ta có $f = d_{2} \circ d_{1}$, như đã khẳng định. Nhận thấy rằng trong Mệnh đề 8.25, ta có thể chọn $\alpha  = -1$; nghĩa là, mọi phép trượt (transvection) của siêu phẳng (hyperplane) $H$ là các hợp thành của hai các phép đối xứng về siêu phẳng (hyperplane) $H$, một của mà có thể được được chọn arbitrarily.
Nhận xét: Mệnh đề 8.25 nghiệm đúng như dài như $K \neq  {0, 1}$. sau đây quan trọng kết quả là bây giờ thu được.

> **Định lý 8.26.** Cho $E$ là bất kỳ không gian vectơ hữu hạn chiều trên trường $K$ của characteristic không bằng $2$. Thì nhóm SL(E) được sinh bởi các phép trượt, và nhóm GL(E) được sinh bởi các phép vị tự.

<!-- PAGE 324 -->

*Chứng minh.* Xét bất kỳ $f \in$ SL(E), và cho $A$ là ma trận của nó trong bất kỳ cơ sở (basis). Theo Mệnh đề 8.24, có một ma trận $S$ sao cho
$$SA = \begin{pmatrix} I_{n-1} & 0 \\ 0 & \alpha \end{pmatrix} = E_{n,\alpha},$$
Với $\alpha  =$ det(), và ở đâu $S$ là tích của sơ cấp các ma trận của tạo thành $E_{i,j;\beta}$. Vì det() $= 1$, ta có $\alpha  = 1$, và kết quả được chứng minh. Ngược lại, nếu $f$ là khả nghịch nhưng $f \in /$ SL(E), ở trên phương trình chỉ ra $E_{n,\alpha}$ là phép vị tự (dilatation), $S$ là tích của các phép trượt, và theo Mệnh đề 8.25, mọi phép trượt (transvection) là hợp thành của hai các phép vị tự. Do đó, thứ hai kết quả cũng được chứng minh. Ta kết luận điều này mục bởi chứng minh rằng bất kỳ hai các phép trượt là liên hợp trong GL(E). Cho $\tau_{\phi ,u}  (u \neq  0)$ là phép trượt (transvection) và cho $g \in$ GL(E) là bất kỳ khả nghịch ánh xạ tuyến tính (linear map). Ta có
$$(g \circ \tau_{\phi ,u}  \circ g^{-1})(x) = g(g^{-1}(x) + \phi (g^{-1}(x))u)$$
$$= x + \phi (g^{-1}(x))g(u).$$
Cho chúng ta tìm siêu phẳng (hyperplane) được xác định bởi dạng tuyến tính (linear form) $x \mapsto \phi (g^{-1}(x))$. Điều này là tập hợp của các vectơ $x \in E$ sao cho $\phi (g^{-1}(x)) = 0$, mà nghiệm đúng khi và chỉ khi $g^{-1}(x) \in H$ khi và chỉ khi $x \in$ g(H). Vì vậy, Ker $(\phi \circ g^{-1}) =$ g(H) $=$ H', và ta có g(u) $\in$ g(H) $=$ H', do đó $g\circ \tau_{\phi ,u} \circ g^{-1}$ là phép trượt (transvection) của siêu phẳng (hyperplane) H' $=$ g(H) và hướng u' $=$ g(u) (với u' $\in$ H').
$$̸$$
Ngược lại, cho $\tau_{\psi ,u'}$ là một số phép trượt (transvection) (u' $= 0)$. Chọn một số các vectơ $v$, v' sao cho $\phi (v) = \psi$ (v') $= 1$, sao cho
$$E = H \oplus Kv = H'\oplus Kv'.$$
Có một ánh xạ tuyến tính (linear map) $g \in$ GL(E) sao cho g(u) $=$ u', g(v) $=$ v', và g(H) $=$ H'. để định nghĩa $g$, chọn cơ sở (basis) $(v, u, e_{2}, \dots  , e_{n-1})$ ở đâu $(u, e_{2}, \dots  , e_{n-1})$ là cơ sở (basis) của $H$ và chọn cơ sở (basis) (v', u', $e_{2}', \dots  , e_{n-1}')$ ở đâu (u', $e_{2}', \dots  , e_{n-1}')$ là cơ sở (basis) của H'; thì $g$ được định nghĩa sao cho g(v) $=$ v', g(u) $=$ u', và $g(e_{i}) = g(e_{i}')$, cho $i = 2, \dots  , n$ - $1$. Nếu $n = 2$, thì $e_{i}$ và $e_{i}'$ là missing. Thì, ta có
$$(g \circ \tau_{\phi ,u}  \circ g^{-1})(x) = x + \phi (g^{-1}(x))u'.$$
Bây giờ $\phi  \circ g^{-1}$ cũng xác định siêu phẳng (hyperplane) H' $=$ g(H), do đó ta có $\phi  \circ g^{-1} = \lambda \psi$ với một số khác không $\lambda$ trong $K$. Vì v' $=$ g(v), ta thu được
$$\phi (v) = \phi  \circ g^{-1}(v') = \lambda \psi (v'),$$
Và vì $\phi (v) = \psi$ (v') $= 1$, ta phải có $\lambda  = 1$. Suy ra rằng
$$(g \circ \tau_{\phi ,u}  \circ g^{-1})(x) = x + \psi (x)u'= \tau_{\psi ,u'} (x).$$
Trong tóm tắt, ta được chứng minh hầu như tất cả các phần kết quả sau đây.
