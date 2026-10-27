# Các cơ sở của Đối xứng Các lũy thừa


<!-- PAGE 1218 -->

> **Định nghĩa 33.23.** Đối xứng các tenxơ trong $S^{n}(E)$ được gọi là đối xứng n-tensors, và các tenxơ của tạo thành $u_{1} \odot \cdots  \odot u_{n}$, ở đâu $u_{i} \in E$, được gọi là đơn giản (hoặc phân rã được) đối xứng n- các tenxơ. Những phần tử đó đối xứng n-tensors rằng là không đơn giản là thường được gọi là compound đối xứng n-tensors. Cho trước các ánh xạ tuyến tính (linear maps) $f$: $E \to$ E', vì ánh xạ $\iota_{\odot}' \circ (f \times  f)$ là song tuyến tính và đối xứng, tồn tại duy nhất một ánh xạ tuyến tính (linear map) $f \odot f$: $S^{2}(E) \to S^{2}(E')$ tạo ra sau đây biểu đồ giao hoán.
$$\iota \odot  /$$
$$E^{2}S^{2}(E)$$
$$f\times ff\odot f$$
$$(E')^{2} /S^{2}(E').$$
$$\overline{\iota}\overline{'}$$
$$\odot$$
Nhận thấy rằng $f \odot f$ được xác định bởi
$$(f \odot f)(u \odot v) = f(u) \odot f(v).$$

> **Mệnh đề 33.36.** Cho trước bất kỳ hai các ánh xạ tuyến tính (linear maps) $f$: $E \to$ E' và f': E' $\to$ E'',ta có
$$(f'\circ f) \odot (f'\circ f) = (f'\odot f') \circ (f \odot f).$$
Bằng cách sử dụng chứng minh các kỹ thuật của Mệnh đề 33.13 $(3)$, ta có thể chỉ ra sau đây tính chất của tenxơ đối xứng (symmetric tensor) các tích.

> **Mệnh đề 33.37.** Ta có kết quả sau đẳng cấu:
$$\oplus  \sim^{n} M \otimes$$
$$S^{n}(EF)=S^{k}(E)S^{n-k}(F).$$
$$k=0$$
Tổng quát hóa đến tenxơ đối xứng (symmetric tensor) tích $f \odot \cdots  \odot f$ của $n \ge 3$ copies của ánh xạ tuyến tính (linear map) $f$: $E \to$ E' là immediate, và trái đến độc giả.

## 33.11 Các cơ sở của Đối xứng Các lũy thừa

Các vectơ $u_{1} \odot \cdots  \odot u_{m}$ ở đâu $u_{1}, \dots  , u_{m} \in E$ sinh $S^{m}(E)$, nhưng chúng là không độc lập tuyến tính (linearly independent). Ta sẽ chứng minh phiên bản của Mệnh đề 33.12 cho tenxơ đối xứng (symmetric tensor) các lũy thừa bằng cách sử dụng các đa tập hợp. Nhắc lại rằng (hữu hạn) đa tập hợp (multiset) trên tập hợp $I$ là hàm $M$: I $\to \mathbb{N}$, sao cho M(i) $\neq  0$
$$\mathbb{N}^{(I)}$$
Cho một cách hữu hạn nhiều $i \in$ I. Tập hợp tất cả các đa tập hợp trên I được ký hiệu là như và ta cho dom(M) $= {i \in$ I | M(i) $\neq  0}$, hữu hạn tập hợp của các phần tử trong I rằng thực sự xảy ra trong $M$.
$$size of the multiset M is |M| = \sum_{a}  \in A M(a).$$

<!-- PAGE 1219 -->
Đến giải thích ý tưởng của chứng minh, xét trường hợp khi $m = 2$ và $E$ có số chiều $3$. Cho trước cơ sở (basis) $(e_{1}, e_{2}, e_{3})$ của $E$, ta sẽ like để chứng minh rằng
$$e_{1} \odot e_{1},e_{1} \odot e_{2},e_{1} \odot e_{3},e_{2} \odot e_{2},e_{2} \odot e_{3},e_{3} \odot e_{3}$$
Là độc lập tuyến tính (linearly independent). để chứng minh điều này, nó suffices để chỉ ra rằng với mọi không gian vectơ (vector space) $F$, nếu $w_{11}, w_{12}, w_{13}, w_{22}, w_{23}, w_{33}$ là bất kỳ các vectơ trong $F$, thì có một đối xứng ánh xạ song tuyến tính (bilinear map) $h: E^{2} \to F$ sao cho
$$h(e_{i}, e_{j}) = w_{ij},1 \le i \le j \le 3.$$
Bởi vì $h$ cho ta duy nhất ánh xạ tuyến tính (linear map) $h_{\odot}: S^{2}(E) \to F$ sao cho
$$h_{\odot}(e_{i} \odot e_{j}) = w_{ij},1 \le i \le j \le 3,$$
Theo Mệnh đề 33.4, các vectơ
$$e_{1} \odot e_{1},e_{1} \odot e_{2},e_{1} \odot e_{3},e_{2} \odot e_{2},e_{2} \odot e_{3},e_{3} \odot e_{3}$$
Là độc lập tuyến tính (linearly independent). Điều này suggests understanding cách mà đối xứng song tuyến tính hàm $f$: $E^{2} \to F$ được biểu diễn theo của nó các giá trị $f(e_{i}, e_{j})$ trên cơ sở (basis) các vectơ $(e_{1}, e_{2}, e_{3})$, và điều này có thể được được thực hiện dễ dàng. Bằng cách sử dụng tính song tuyến tính và tính đối xứng, ta thu được $f(u_{1}e_{1} + u_{2}e_{2} + u_{3}e_{3}, v_{1}e_{1} + v_{2}e_{2} + v_{3}e_{3}) = u_{1}v_{1}f(e_{1}, e_{1}) + (u_{1}v_{2} + u_{2}v_{1})f(e_{1}, e_{2})$
$$+ (u_{1}v_{3} + u_{3}v_{1})f(e_{1}, e_{3}) + u_{2}v_{2}f(e_{2}, e_{2})$$
$$+ (u_{2}v_{3} + u_{3}v_{2})f(e_{2}, e_{3}) + u_{3}v_{3}f(e_{3}, e_{3}).$$
Vì vậy, cho trước $w_{11}, w_{12}, w_{13}, w_{22}, w_{23}, w_{33} \in F$, hàm $h$ cho trước bởi
$$h(u_{1}e_{1} + u_{2}e_{2} + u_{3}e_{3}, v_{1}e_{1} + v_{2}e_{2} + v_{3}e_{3}) = u_{1}v_{1}w_{11} + (u_{1}v_{2} + u_{2}v_{1})w_{12}$$
$$+ (u_{1}v_{3} + u_{3}v_{1})w_{13} + u_{2}v_{2}w_{22}$$
$$+ (u_{2}v_{3} + u_{3}v_{2})w_{23} + u_{3}v_{3}w_{33}$$
Là rõ ràng song tuyến tính đối xứng, và bởi cách xây dựng $h(e_{i}, e_{j}) = w_{ij}$, do đó nó thực hiện job. tổng quát hóa của điều này lập luận đến bất kỳ $m \ge 2$ và đến không gian $E$ của bất kỳ số chiều (chẵn/ngay cả vô hạn) là conceptually rõ ràng, nhưng notationally phức tạp. Nếu dim(E) $= n$ và nếu $(e_{1}, \dots  , e_{n})$
$$is a basis  of E, for any m vectors v_{j} = \sum_{i}  n=1 u_{i,j}e_{i} in E, for any symmetric multilinear map$$
$f$: $E^{m} \to F$, ta có $f(v_{1}, \dots  , v_{m})$
$$= \sum_{\cdot \cdot \cdot+kn}  \sum_{In={1}  \prod_{i1\in I1}  u_{1,i1}!\cdots \prod_{in\in In}  u_{n,in}!!f(e_{1}, \dots  , e_{1}, \dots  , e_{n}, \dots  , e_{n}).$$
$k + =m$ I $\cup \cdot \cdot \cdot \cup ,...,m}$ | ${z$ } | ${z$ } $1 1$ k1 kn
$$Ii\cap Ij=\emptyset , i\neq j, |Ij|=kj$$

<!-- PAGE 1220 -->

> **Định nghĩa 33.24.** Cho trước bất kỳ tập hợp $J$ của $n \ge 1$ các phần tử, nói $J = {j_{1}, \dots  , j_{n}}$, và cho trước bất kỳ $m \ge 2$, với mọi dãy $(k_{1} \dots  , k_{n})$ của tự nhiên các số $k_{i} \in \mathbb{N}$ sao cho $k_{1} + \cdots  + k_{n} = m$, đa tập hợp (multiset) $M$ của kích thước $m$
$$M = {j_{1}, \dots  , j_{1}, j_{2}, \dots  , j_{2}, \dots  , j_{n}, \dots  , j_{n}}$$
$$|{z}|{z}|{z}$$
$$k1k2kn$$
Được ký hiệu bởi M(m, $J, k_{1}, \dots  , k_{n})$. Lưu ý rằng $M(j_{i}) = k_{i}$, cho $i = 1, \dots  , n$. Cho trước bất kỳ $k \ge 1$, và bất kỳ $u \in E$, ta ký hiệu $u \odot \cdots  \odot u$ như $u^{\odot k}$.
$$|{z}$$
$$k$$
Ta có thể bây giờ chứng minh sau đây mệnh đề.

> **Mệnh đề 33.38.** Cho trước không gian vectơ (vector space) $E$, nếu $(e_{i})_{i\in I}$ là cơ sở (basis) cho $E$, thì họ của các vectơ
$$\begin{pmatrix} e_{i1}^{\odot M(i1)}\odot \cdots  \odot e_{ik}^{\odot M(ik)} \end{pmatrix} M\in \mathbb{N}(I), |M|=m,$$
$${i1,...,ik}=dom(M)$$
Là cơ sở (basis) của đối xứng thứ $m$ tenxơ lũy thừa $S^{m}(E)$.

*Chứng minh.* chứng minh là rất đồng dạng đến rằng của Mệnh đề 33.12. Thứ nhất giả sử rằng $E$ có hữu hạn
$$\mathbb{N}^{(I)}$$
Số chiều $n$. Trong điều này trường hợp $I = {1, \dots  , n}$, và bất kỳ đa tập hợp (multiset) $M \in$ của kích thước |M| $= m$ là của tạo thành M(m, ${1, \dots  , n}, k_{1}, \dots  , k_{n})$, với $k_{i} =$ M(i) và $k_{1} + \cdots  + k_{n} = m$. Với mọi không tầm thường không gian vectơ (vector space) $F$, với mọi họ của các vectơ
$$(w_{M})_{M\in N(I),|M|=m},$$
Ta chỉ ra sự tồn tại của đối xứng ánh xạ đa tuyến tính (multilinear map) $h: S^{m}(E) \to F$, sao cho với mọi $\mathbb{N}^{(I)} M \in$ với |M| $= m$, ta có
$$h(e_{i1}^{\odot M(i1)}\odot \cdots  \odot e_{ik}^{\odot M(ik)}) = w_{M},$$
Ở đâu ${i_{1}, \dots  , i_{k}} =$ dom(M). Ta định nghĩa ánh xạ $f$: $E^{m} \to F$ như sau: với mọi $m$ các vectơ
$$v_{1}, \dots  , v_{m} \in E we can write v_{k} = \sum_{i}  n=1 u_{i,k}e_{i} for k = 1, \dots  , m and we set$$
$f(v_{1}, \dots  , v_{m})$
$$= \sum_{\cdot \cdot \cdot+kn}  \sum_{In={1}  \prod_{i1\in I1}  u_{1,i1}!\cdots \prod_{in\in In}  u_{n,in}!!w_{M(m,{1,...,n},k1,...,kn)}.$$
$$k1+=mI1\cup \cdot \cdot \cdot \cup ,...,m}$$
$$Ii\cap Ij=\emptyset , i\neq j, |Ij|=kj$$
Nó là không khó để kiểm chứng rằng $f$ là đối xứng và đa tuyến tính. Bởi phổ dụng ánh xạ tính chất của tenxơ đối xứng (symmetric tensor) tích, ánh xạ tuyến tính (linear map) $f_{\odot}: S^{m}(E) \to F$ sao cho $f = f_{\odot} \circ \phi$, là mong muốn ánh xạ $h$. Thì theo Mệnh đề 33.4, suy ra rằng họ
$$\begin{pmatrix} e_{i1}^{\odot M(i1)}\odot \cdots  \odot e_{ik}^{\odot M(ik)} \end{pmatrix} M\in \mathbb{N}(I), |M|=m,$$
$${i1,...,ik}=dom(M)$$
