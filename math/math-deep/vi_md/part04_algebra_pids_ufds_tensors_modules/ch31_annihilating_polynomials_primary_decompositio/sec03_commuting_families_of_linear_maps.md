# Giao hoán Các họ của Các ánh xạ tuyến tính (linear maps)


<!-- PAGE 1110 -->
Nhận xét: Mệnh đề 31.5 có thể được sử dụng để cho quick chứng minh của Định lý 15.5.

## 31.3 Giao hoán Các họ của Chéo hóa được (diagonalizable) và Trian-

$$gulable Maps$$
Bằng cách sử dụng Định lý 31.6, ta có thể cho ngắn chứng minh về giao hoán chéo hóa được (diagonalizable) các ánh xạ tuyến tính (linear maps).

> **Định nghĩa 31.4.** Nếu $\mathcal{F}$ là họ của các ánh xạ tuyến tính (linear maps) trên không gian vectơ (vector space) $E$, ta nói rằng $\mathcal{F}$ là giao hoán họ khi và chỉ khi $f \circ g = g \circ f$ với mọi $f, g \in F$.

> **Mệnh đề 31.7.** Cho $\mathcal{F}$ là hữu hạn giao hoán họ của chéo hóa được (diagonalizable) các ánh xạ tuyến tính (linear maps) trên không gian vectơ (vector space) $E$. Tồn tại một cơ sở (basis) của $E$ sao cho mọi ánh xạ tuyến tính (linear map) trong $\mathcal{F}$ được biểu diễn trong rằng cơ sở (basis) bởi ma trận đường chéo (diagonal matrix).

*Chứng minh.* Ta tiến hành bằng quy nạp theo $n =$ dim(E). Nếu $n = 1$, ở đó là không có gì để chứng minh. Nếu $n > 1$, có hai các trường hợp. Nếu tất cả các ánh xạ tuyến tính (linear maps) trong $\mathcal{F}$ là của tạo thành $\lambda$ id với một số $\lambda  \in K$, thì mệnh đề nghiệm đúng một cách tầm thường. Trong trường hợp thứ hai, cho $f \in F$ là một số ánh xạ tuyến tính (linear map) trong $\mathcal{F}$ mà là không vô hướng (scalar) bội của đồng nhất thức. Trong trường hợp này, $f$ có ít nhất hai phân biệt các trị riêng (eigenvalues) $\lambda_{1} , \dots  , \lambda_{k}$, và bởi vì $f$ là chéo hóa được (diagonalizable), $E$ là tổng trực tiếp (direct sum) của tương ứng các không gian riêng (eigenspace) $E_{\lambda1}, \dots  , E_{\lambda k}$. Với mọi chỉ số $i$, không gian riêng (eigenspace) $E_{\lambda i}$ là bất biến dưới $f$ và dưới mọi khác ánh xạ tuyến tính (linear map) $g$ trong $\mathcal{F}$, vì với mọi $g \in F$ và bất kỳ $u \in E_{\lambda i}$, bởi vì $f$ và $g$ giao hoán, ta có
$$f(g(u)) = g(f(u)) = g(\lambda_{i} u) = \lambda_{i} g(u)$$
Do đó g(u) $\in E_{\lambda i}$. Cho $\mathcal{F}_{i}$ là họ thu được bởi thu hẹp mỗi $f \in F$ đến $E_{\lambda i}$. Theo Mệnh đề 31.3, đa thức tối tiểu (minimal polynomial) của mọi ánh xạ tuyến tính (linear map) $f$ | $E_{\lambda i}$ trong $\mathcal{F}_{i}$ chia hết đa thức tối tiểu (minimal polynomial) $m_{f}$ của $f$, và vì $f$ là chéo hóa được (diagonalizable), $m_{f}$ là tích của phân biệt tuyến tính các nhân tử, do đó đa thức tối tiểu (minimal polynomial) của $f$ | $E_{\lambda i}$ là cũng tích của phân biệt tuyến tính các nhân tử. Theo Định lý 31.6, ánh xạ tuyến tính (linear map) $f$ | $E_{\lambda i}$ là chéo hóa được (diagonalizable). Vì $k > 1$, ta có $dim(E_{\lambda i}) <$ dim(E) cho $i = 1, \dots  , k$, và theo giả thiết quy nạp, với mỗi $i$ có một cơ sở (basis) của $E_{\lambda i}$ trên mà $f$ | $E_{\lambda i}$ được biểu diễn bởi ma trận đường chéo (diagonal matrix). Vì ở trên lập luận nghiệm đúng với mọi $i$, bởi combining các cơ sở của $E_{\lambda i}$, ta thu được cơ sở (basis) của $E$ sao cho ma trận của mọi ánh xạ tuyến tính (linear map) $f \in F$ được biểu diễn bởi ma trận đường chéo (diagonal matrix).
Nhận xét: Mệnh đề 31.7 cũng nghiệm đúng cho vô hạn giao hoán các họ $\mathcal{F}$ của chéo hóa được (diagonalizable) các ánh xạ tuyến tính (linear maps), bởi vì $E$ đang là hữu hạn dimensional, có một hữu hạn họ con của độc lập tuyến tính (linearly independent) các ánh xạ tuyến tính (linear maps) trong $\mathcal{F}$ sinh $\mathcal{F}$. Ở đó là cũng tương tự kết quả cho giao hoán các họ của các ánh xạ tuyến tính (linear maps) được biểu diễn bởi tam giác trên (upper triangular) các ma trận. để chứng minh điều này ta cần sau đây mệnh đề.

> **Mệnh đề 31.8.** $Let\mathcal{F}$ là khác rỗng hữu hạn giao hoán họ của triangulable các ánh xạ tuyến tính (linear maps) trên không gian vectơ hữu hạn chiều $E$. Cho $W$ là thực sự/đúng đắn không gian con của $E$ mà là bất biến dưới $\mathcal{F}$. Thì tồn tại một vectơ $u \in E$ sao cho:

<!-- PAGE 1111 -->
$1. u \in / W. 2$. Với mọi $f \in F$, vectơ f(u) thuộc đến không gian con $W \oplus$ Ku được sinh (spanned) bởi $W$ và $u$.

*Chứng minh.* Bởi renaming các phần tử của $\mathcal{F}$ nếu cần, ta có thể giả sử rằng $(f_{1}, \dots  , f_{r})$ là cơ sở (basis) của không gian con của Kết thúc/cuối(E) được sinh (spanned) $by\mathcal{F}$. Ta chứng minh bằng quy nạp theo $r$ rằng tồn tại một vectơ $u \in E$ sao cho $1. u \in / W. 2. (f_{i}$ - $\alpha_{i}$ id)(u) $\in W$ cho $i = 1, \dots  , r$, với một số các vô hướng $\alpha_{i}  \in K$. Xét base trường hợp $r = 1$. Vì $f_{1}$ là triangulable, các trị riêng (các trị riêng (eigenvalues)) của nó tất cả thuộc đến $K$ vì chúng là đường chéo các phần tử (entries) của tam giác ma trận liên kết với $f_{1}$ (điều này là dễ hướng của Định lý 15.5), do đó đa thức tối tiểu (minimal polynomial) của $f_{1}$ là của tạo thành
$$m = (X -\lambda_{1} )^{r1}\cdots  (X -\lambda_{k} )^{rk},$$
Ở đâu các trị riêng (eigenvalues) $\lambda_{1} , \dots  , \lambda_{k}$ của $f_{1}$ thuộc đến $K$. Ta kết luận bằng cách áp dụng Mệnh đề 31.5. Tiếp theo giả sử rằng $r \ge 2$ và rằng giả thiết quy nạp (induction hypothesis) nghiệm đúng cho $f_{1}, \dots  , f_{r-1}$. Do đó, có một vectơ $u_{r-1} \in E$ sao cho $1. u_{r-1} \in / W. 2. (f_{i}$ - $\alpha_{i} id)(u_{r-1}) \in W$ cho $i = 1, \dots  , r$ - $1$, với một số các vô hướng $\alpha_{i}  \in K$. Cho
$$V_{r-1} = {w \in E | (f_{i} -\alpha_{i} id)(w) \in W, i = 1, \dots  , r -1}.$$
Rõ ràng, $W \subseteq V_{r-1}$ và $u_{r-1} \in V_{r-1}$. Ta khẳng định rằng $V_{r-1}$ là bất biến dưới $\mathcal{F}$. Điều này là bởi vì, với mọi $v \in V_{r-1}$ và bất kỳ $f \in F$, vì $f$ và $f_{i}$ giao hoán, ta có
$$(f_{i} -\alpha_{i} id)(f(v)) = f((f_{i} -\alpha_{i} id)(v)),1 \le i \le r -1.$$
Bây giờ $(f_{i} -\alpha_{i}$ id)(v) $\in W$ bởi vì $v \in V_{r-1}$, và $W$ là bất biến $under\mathcal{F}$, do đó $f(f_{i} -\alpha_{i}$ id)(v)) $\in W$, nghĩa là, $(f_{i}$ - $\alpha_{i}$ id)(f(v)) $\in W$. Xét thu hẹp $g_{r}$ của $f_{r}$ đến $V_{r-1}$. đa thức tối tiểu (minimal polynomial) của $g_{r}$ chia hết đa thức tối tiểu (minimal polynomial) của $f_{r}$, và vì $f_{r}$ là triangulable, chỉ như ta đã thấy cho $f_{1}$, đa thức tối tiểu (minimal polynomial) của $f_{r}$ là của tạo thành
$$m = (X -\lambda_{1} )^{r1}\cdots  (X -\lambda_{k} )^{rk},$$
Ở đâu các trị riêng (eigenvalues) $\lambda_{1} , \dots  , \lambda_{k}$ của $f_{r}$ thuộc đến $K$, do đó đa thức tối tiểu (minimal polynomial) của $g_{r}$ là của cùng tạo thành. Theo Mệnh đề 31.5, tồn tại một vectơ $u_{r} \in V_{r-1}$ sao cho

<!-- PAGE 1112 -->
$1. u_{r} \in / W. 2. (g_{r}$ - $\alpha_{r} id)(u_{r}) \in W$ với một số các vô hướng $\alpha_{r}  \in K$. Bây giờ vì $u_{r} \in V_{r-1}$, ta có $(f_{i} -\alpha_{i} id)(u_{r}) \in W$ cho $i = 1, \dots  , r -1$, do đó $(f_{i} -\alpha_{i} id)(u_{r}) \in W$ cho $i = 1, \dots  , r$ (vì $g_{r}$ là thu hẹp của $f_{r})$, mà kết luận chứng minh của quy nạp bước. Cuối cùng, vì mọi $f \in F$ là tổ hợp tuyến tính (linear combination) của $(f_{1}, \dots  , f_{r})$, Điều kiện $(2)$ của quy nạp khẳng định suy ra Điều kiện $(2)$ của mệnh đề. Ta có thể bây giờ chứng minh kết quả sau đây.

> **Mệnh đề 31.9.** $Let\mathcal{F}$ là khác rỗng hữu hạn giao hoán họ của triangulable các ánh xạ tuyến tính (linear maps) trên không gian vectơ hữu hạn chiều $E$. Tồn tại một cơ sở (basis) của $E$ sao cho mọi ánh xạ tuyến tính (linear map) trong $\mathcal{F}$ được biểu diễn trong rằng cơ sở (basis) bởi tam giác trên (upper triangular) ma trận.

*Chứng minh.* Cho $n =$ dim(E). Ta xây dựng một cách quy nạp cơ sở (basis) $(u_{1}, \dots  , u_{n})$ của $E$ sao cho nếu $W_{i}$ là không gian con được sinh (spanned) bởi $(u_{1} \dots  , u_{i})$, thì với mọi $f \in F$,
$$f(u_{i}) = a_{1i}^{f}u_{1} + \cdots  + a_{ii}^{f}u_{i},$$
Với một số $a_{ij}^{f} \in K$; nghĩa là, $f(u_{i})$ thuộc đến không gian con $W_{i}$. Ta bắt đầu bằng cách áp dụng Mệnh đề 31.8 đến không gian con $W_{0} = (0)$ để thu được $u_{1}$ sao cho với mọi $f \in F$,
$$f(u_{1}) = \alpha_{1}^{f} u_{1}.$$
Cho quy nạp bước, vì $W_{i}$ bất biến $under\mathcal{F}$, ta áp dụng Mệnh đề 31.8 đến không gian con $W_{i}$, để thu được $u_{i+1} \in E$ sao cho $1. u_{i+1} \in / W_{i}. 2$. Với mọi $f \in F$, vectơ $f(u_{i+1})$ thuộc đến không gian con được sinh (spanned) bởi $W_{i}$ và $u_{i+1}$. Điều kiện $(1)$ suy ra rằng $(u_{1}, \dots  , u_{i}, u_{i+1})$ là độc lập tuyến tính (linearly independent), và Điều kiện $(2)$ có nghĩa là với mọi $f \in F$,
$$f(u_{i+1}) = a_{1i+1}^{f}u_{1} + \cdots  + a_{i+1i+1}^{f}u_{i+1},$$
Với một số $a_{i+1j}^{f} \in K$, thiết lập quy nạp bước. Sau $n$ các bước, mỗi $f \in F$ được biểu diễn bởi tam giác trên (upper triangular) ma trận. Nhận thấy rằng nếu $\mathcal{F}$ bao gồm của đơn lẻ ánh xạ tuyến tính (linear map) $f$ và nếu đa thức tối tiểu (minimal polynomial) của $f$ là của tạo thành
$$m = (X -\lambda_{1} )^{r1}\cdots  (X -\lambda_{k} )^{rk},$$
Với tất cả $\lambda_{i}  \in K$, bằng cách sử dụng Mệnh đề 31.5 thay vì của Mệnh đề 31.8, chứng minh của Mệnh đề 31.9 cho ta một cái khác chứng minh của Định lý 15.5.
