# (r,s)-Các tenxơ như Đa tuyến tính Các ánh xạ


<!-- PAGE 1205 -->
33.8 $(r$, s)-Các tenxơ như Đa tuyến tính Các ánh xạ Như ta chỉ được quan sát, Mệnh đề 33.25 cho phép chúng ta đến quan điểm không gian của $(r$, s)-các tenxơ $T^{r,s} (V$) như không gian của đa tuyến tính các ánh xạ
$$T : (V^{*})^{r}\times  V^{s}\to K,$$
Điểm của quan điểm rằng hóa ra là technically rất fruitful trong vi phân hình học.

> **Định nghĩa 33.16.** không gian $Hom((V^{*})^{r}, V^{s}; K)$ của đa tuyến tính các ánh xạ $T$: $(V^{*})^{r} \times  V^{s} \to K$ được ký hiệu là $\mathcal{T}^{r,s} (V$). Ví dụ, Dieudonn´e $[51]$, O’Neill $[137]$ và Sakai $[147]$ sử dụng định nghĩa này. Mệnh đề 33.25 chỉ ra rằng ánh xạ $\mu^{r,s}$: $T^{r,s}(V$) $\to T^{r,s}(V$) là đẳng cấu. Cho điều này lý do,
$$\mathcal{T}^{r,s} \mathcal{T}^{0,1}  \mathcal{T}^{1,0}  \sim$$
Các phần tử của $(V$) cũng được gọi là các tenxơ. Lưu ý rằng $(V$) là $V^{*}$, và $(V$) là $V^{**} = V$, bằng cách sử dụng chính tắc đẳng cấu $u \mapsto eval_{u}$.
Nhận xét: tenxơ các không gian, $T^{r,s} (V$) $(resp,\mathcal{T}^{r,s} (V$)) cũng được ký hiệu $T_{s}^{r}  (V$) (resp. $\mathcal{T}_{s}^{r}  (V$)). tenxơ $\alpha  \in T^{r,s} (V$) được nói là contravariant trong thứ nhất $r$ các đối số/lập luận và hiệp biến trong cuối cùng $s$ các đối số/lập luận. Điều này thuật ngữ refers đến cách các tenxơ behave dưới tọa độ thay đổi. Cho trước cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $V$, nếu $(e_{1}^{*}, \dots  , e_{n}^{*})$ ký hiệu đối ngẫu (dual) cơ sở (basis), thì các tenxơ
$$e_{i1} \otimes \cdots  \otimes e_{ir} \otimes e_{j1}^{*} \otimes \cdots  \otimes e_{js}^{*}$$
Tạo thành cơ sở (basis) của $T^{r,s} (V$), do đó mọi tenxơ $\alpha  \in T^{r,s} (V$) được cho bởi biểu thức của tạo thành
$$\alpha  = \sum_{i1,...,ir}  a_{j1...js}^{i1...ir}e_{i1} \otimes \cdots  \otimes e_{ir} \otimes e_{j1}^{*} \otimes \cdots  \otimes e_{js}^{*}.$$
$$j1,...,js$$
Bằng cách sử dụng đẳng cấu $\mu^{r,s}$, đa tuyến tính các ánh xạ
$$\mu^{r,s} (e_{i1} \otimes \cdots  \otimes e_{ir} \otimes e_{j1}^{*} \otimes \cdots  \otimes e_{js}^{*})$$
Tạo thành cơ sở (basis) của $\mathcal{T}^{r,s} (V$), do đó mọi tenxơ $T \in T^{r,s} (V$) có thể được một cách duy nhất được viết như
$$T = \sum_{i1,...,ir}  a_{j1...js}^{i1...ir}\mu^{r,s} (e_{i1} \otimes \cdots  \otimes e_{ir} \otimes e_{j1}^{*} \otimes \cdots  \otimes e_{js}^{*}).$$
$$j1,...,js$$
Vì $e_{j}^{*}(e_{i}) = \delta_{ij}$, nhận thấy rằng
$$T(e_{i1}^{*}, \dots  , e_{ir}^{*}, e_{j1}, \dots  , e_{js}) = a_{j1...js}^{i1...ir}.$$
Nó là thông lệ đến bỏ $\mu^{r,s}$ và quan điểm
$$e_{i1} \otimes \cdots  \otimes e_{ir} \otimes e_{j1}^{*} \otimes \cdots  \otimes e_{js}^{*}$$

<!-- PAGE 1206 -->
Như tương ứng ánh xạ đa tuyến tính (multilinear map) trong $\mathcal{T}^{r,s} (V$). để đơn giản hóa ký hiệu, ta thường viết $\mu$ thay vì của $\mu^{r,s}$. Tại thứ nhất, practice của dropping $\mu$ có thể được khá confusing, nhưng một tìm khá quickly rằng bằng cách sử dụng không gian $\mathcal{T}^{r,s} (V$) thay vì của không gian $T^{r,s} (V$) là nhiều hơn/thêm thuận tiện đến deal với tenxơ các trường. tradition trong cổ điển tenxơ ký hiệu là để sử dụng thấp hơn các chỉ số trên các vectơ và trên các chỉ số trên các dạng tuyến tính, và trong accordance đến Einstein phép lấy tổng quy ước (hoặc Einstein ký hiệu), position của các chỉ số trên các hệ số là reversed. Einstein phép lấy tổng quy ước (đã encountered trong Mục 33.1) là giả sử rằng phép lấy tổng là performed với mọi các giá trị của mọi chỉ số rằng xuất hiện simultaneously một lần như trên chỉ số và một lần như thấp hơn chỉ số. Theo điều này quy ước, dạng tuyến tính (linear form) $e_{i}^{*}$ đối ngẫu (dual) đến cơ sở (basis) vectơ $e_{i}$ được ký hiệu bởi $e^{i}$, và (suppressing ánh xạ $\mu^{r,s}$), tenxơ $\alpha  \in T^{r,s} (V$) được viết
$$\alpha  = a_{j1...js}^{i1...ir}e_{i1} \otimes \cdots  \otimes e_{ir} \otimes e^{j1}\otimes \cdots  \otimes e^{js}.$$
Older quan điểm của các tenxơ là rằng chúng là multidimensional các mảng (array) của các hệ số,
$$\begin{pmatrix} a_{j1...js}^{i1...ir} \\ (see \end{pmatrix} ,$$
Subject đến các quy tắc cho thay đổi của các cơ sở Mệnh đề 33.29). Từ bây giờ trên cho đến khi Mục 33.10 ta sẽ sử dụng Einstein phép lấy tổng quy ước. Nó thực hiện rút gọn considerably số của phép lấy tổng các dấu.

> **Mệnh đề 33.26.** $space\mathcal{T}^{1,1} (V$) là đẳng cấu đến không gian Hom(V, $V$) của các ánh xạ tuyến tính (linear maps) từ $V$ đến chính nó.

*Chứng minh.* Thật vậy, nếu $T \in T^{1,1} (V$), ta thu được ánh xạ tuyến tính (linear map) $f$: $V \to V$ được định nghĩa sao cho với mọi $u \in V$,
$$\theta (f(u)) = T(\theta , u),\theta  \in V^{*} .$$
Nếu ta chọn cơ sở (basis) $(e_{1}, \dots  , e_{n})$ trong $V$ và nếu $T$ được biểu diễn như
$$T = a_{j}^{i}e_{i} \otimes e^{j},$$
Thì với mọi cơ sở (basis) vectơ $e_{j}$, dạng tuyến tính (linear form) T(-, $e_{j})$ trên $V^{*}$ là $(1$, 0)-tenxơ $\mu (a_{j}^{i}e_{i})$, cụ thể là, việc tính giá trị của dạng tuyến tính (linear form) trong $V^{*}$ tại $a_{j}^{i}e_{i} \in V$. Do đó $(1$, 1)-tenxơ $T$ định nghĩa ánh xạ tuyến tính (linear map) $f$: $V \to V$ cho trước bởi
$$f(e_{j}) = a_{j}^{i}e_{i},$$
Và ta xem rằng ma trận biểu diễn $f$ trên cơ sở (basis) $(e_{1}, \dots  , e_{n})$ là $(a_{j}^{i})$. Lưu ý gấp đôi interpretation của $a_{j}^{i}e_{i}$. Ta có thể quan điểm nó như vectơ trong $V$ (tổ hợp tuyến tính (linear combination) của các vectơ $e_{i}$ trong $V$), hoặc như (multi)ánh xạ tuyến tính (linear map) trong $\mathcal{T}^{1,0} (V$), ở đâu điều này time, $e_{i}$ là một cách thực $\mu (e_{i})$, cụ thể là dạng tuyến tính (linear form) $v \mapsto v(e_{i})$, với $v \in V^{*}$. Với mọi vectơ $u = u^{j}e_{j} \in V$, ta có
$$f(u) = f(u^{j}e_{j}) = u^{j}f(e_{j}) = u^{j}a_{j}^{i}e_{i} = a_{j}^{i}u^{j}e_{i} \in V,$$
Do đó tọa độ thứ $i$ $f(u)^{i}$ của f(u) được cho bởi $f(u)^{i} = a_{j}^{i}u^{j}$, confirming rằng $(a_{j}^{i})$ là ma trận biểu diễn $f$.

<!-- PAGE 1207 -->
 Lưu ý rằng trong ở trên phép tính, $(1$, 1)-tenxơ $(a_{j}^{i})$ ký hiệu ma trận $A$ ở đâu trên chỉ số $i$ là hàng chỉ số và thấp hơn chỉ số $j$ là cột chỉ số, bởi vì ta một cách ẩn được giả sử rằng các tọa độ $u^{j}$ của vectơ $u$ constitute vectơ cột (column vector) và rằng f(u) cũng được biểu diễn bởi vectơ cột (column vector), sao cho $f(u)^{i} = a_{j}^{i}u^{j}$ là tích
$$f(u)^{i} = \begin{pmatrix} a_{1}^{i} & \cdots & a_{j}^{i} & \cdots & a_{n}^{i} \end{pmatrix} \begin{pmatrix} u^{1} \\ \vdots \\ u^{j} \\ \vdots \\ u^{n} \end{pmatrix}$$
Của hàng thứ $i$ của ma trận $A$ bởi vectơ cột (column vector) có phần tử thứ $j$ là $u^{j}$. phương trình $f(e_{j}) = a_{j}^{i}e_{i}$ có thể được symbolically được viết như
$$f(e_{j}) = \begin{pmatrix} e_{1} & \cdots & e_{i} & \cdots & e_{n} \end{pmatrix} \begin{pmatrix} a_{j}^{1} \\ \vdots \\ a_{j}^{i} \\ \vdots \\ a_{j}^{n} \end{pmatrix} ,$$
Ở đâu vectơ cột (column vector) ở trên là cột thứ $j$ của ma trận $A$. Đến recap,
$$\begin{pmatrix} f(u)^{1} \\ \vdots \\ f(u)^{n} \end{pmatrix} = A \begin{pmatrix} u^{1} \\ \vdots \\ u^{n} \end{pmatrix} , \begin{pmatrix} f(e_{1}) & \cdots & f(e_{n}) \end{pmatrix} = \begin{pmatrix} e_{1} & \cdots & e_{n} \end{pmatrix} A.$$
Đối ngẫu (dual) interpretation của $(1$, 1)-tenxơ $(a_{j}^{i})$ bao gồm trong quan điểm các tọa độ $u^{j}$ của vectơ $u$ như tạo thành vectơ hàng (row vector), trong mà trường hợp f(u) cũng được biểu diễn bởi vectơ hàng (row vector), sao cho $f(u)^{i} = a_{j}^{i}u^{j}$ là tích
$$f(u)^{i} = \begin{pmatrix} u^{1} & \cdots & u^{j} & \cdots & u^{n} \end{pmatrix} \begin{pmatrix} a_{1}^{i} \\ \vdots \\ a_{j}^{i} \\ \vdots \\ a_{n}^{i} \end{pmatrix} ,$$
Ở đâu vectơ cột (column vector) ở trên là chuyển vị (transpose) của hàng thứ $i$ của $A$, mà có nghĩa là ma trận liên quan là chuyển vị (transpose) $A^{\top}$ của ma trận $A$. Trong điều này điểm của quan điểm, phương trình $f(e_{j}) = a_{j}^{i}e_{i}$ có thể được symbolically được viết như
$$f(e_{j}) = \begin{pmatrix} a_{j}^{1} & \cdots & a_{j}^{i} & \cdots & a_{j}^{n} \end{pmatrix} \begin{pmatrix} e_{1} \\ \vdots \\ e_{i} \\ \vdots \\ e_{n} \end{pmatrix} ,$$

<!-- PAGE 1208 -->
Ở đâu vectơ hàng (row vector) ở trên là chuyển vị (transpose) của cột thứ $j$ của ma trận $A$. Một lần nữa, ma trận liên quan là chuyển vị (transpose) $A^{\top}$ của $A$. Đến recap,
$$\begin{pmatrix} f(u)^{1} & \cdots & f(u)^{n} \end{pmatrix} = \begin{pmatrix} u^{1} & \cdots & u^{n} \end{pmatrix} A^{\top}, \begin{pmatrix} f(e_{1}) \\ \vdots \\ f(e_{n}) \end{pmatrix} = A^{\top} \begin{pmatrix} e_{1} \\ \vdots \\ e_{n} \end{pmatrix} .$$
Do đó, trong đối ngẫu (dual) interpretation, cho trước $(1, 1)$ tenxơ $(a_{j}^{i})$, nó làm cho nghĩa đến quan điểm thấp hơn chỉ số $j$ như hàng chỉ số và trên chỉ số $i$ như cột chỉ số. Ta thường swap $i$ và $j$ sao cho biểu thức $(a_{i}^{j})$ ký hiệu ma trận ở đâu thấp hơn chỉ số $i$ là hàng chỉ số và trên chỉ số $j$ là cột chỉ số. Với điều này quy ước, ma trận $A^{\top}$ ở trên trở thành ma trận $A$, vì
$$f(e_{i}) = \begin{pmatrix} a_{i}^{1} & \cdots & a_{i}^{j} & \cdots & a_{i}^{n} \end{pmatrix} \begin{pmatrix} e_{1} \\ \vdots \\ e_{j} \\ \vdots \\ e_{n} \end{pmatrix} = a_{i}^{j}e_{j}.$$
Đối ngẫu (dual) interpretation được sử dụng ở dưới trong Mệnh đề 33.29. Mệnh đề 33.26 tổng quát hóa đến $(1$, s)-các tenxơ như sau.

> **Mệnh đề 33.27.** $space\mathcal{T}^{1,s} (V$) là đẳng cấu đến không gian $Hom(V^{s}$; $V$) của đa tuyến tính các ánh xạ từ $V^{s}$ đến $V$.

*Chứng minh.* Thật vậy, nếu $T \in T^{1,s}(V$), ta thu được ánh xạ đa tuyến tính (multilinear map) $f$: $V^{s} \to V$ được định nghĩa sao cho tất cả $u_{1}, \dots  , u_{s} \in V$,
$$\theta (f(u_{1}, \dots  , u_{s})) = T(\theta , u_{1}, \dots  , u_{s}),\theta  \in V^{*} .$$
Nếu ta chọn cơ sở (basis) $(e_{1}, \dots  , e_{n})$ trong $V$ và nếu $T$ được biểu diễn như
$$T = a_{j1...js}^{i}e_{i} \otimes e^{j1}\otimes \cdots  \otimes e^{js},$$
Thì với mọi cơ sở (basis) các vectơ $e_{j1}, \dots  , e_{js}$, dạng đa tuyến tính (multilinear form) T(-, $e_{j1}, \dots  , e_{js})$ trên $V^{*}$ là $(1$, 0)-tenxơ $\mu (a_{j1...js}^{i}e_{i})$, cụ thể là, việc tính giá trị của dạng tuyến tính (linear form) trong $V^{*}$ tại $a_{j1...js}^{i}e_{i} \in V$. Do đó $(1$, s)-tenxơ $T$ định nghĩa ánh xạ đa tuyến tính (multilinear map) $f$: $V^{s} \to V$ cho trước bởi
$$f(e_{j1}, \dots  , e_{js}) = a_{j1...js}^{i}e_{i}.$$
Ngược lại, ánh xạ đa tuyến tính (multilinear map) $f$: $V^{s} \to V$ cho ta $(1$, s)-tenxơ $T \in T^{1,s}(V$) cho trước bởi
$$T(\theta , u_{1}, \dots  , u_{s}) = \theta (f(u_{1}, \dots  , u_{s})),$$
Với mọi $\theta  \in V^{*}$ và tất cả $u_{1}, \dots  , u_{s} \in V$.

<!-- PAGE 1209 -->
Bằng cách sử dụng đẳng cấu $\mu$: $T^{r,s} (V$) $\to T^{r,s} (V$), nó là không khó để chỉ ra rằng tích tenxơ (tensor product)
$$\mathcal{T}^{r1,s1} (V ) \times  T^{r2,s2} (V ) \longrightarrow T^{r1+r2,s1+s2} (V )$$
Được định nghĩa như sau.

> **Định nghĩa 33.17.** Cho hai các tenxơ $T_{1} \in T^{r1,s1} (V$) và $T_{2} \in T^{r2,s2} (V$), của chúng tích tenxơ (tensor product) $T_{1} \otimes T_{2}$ là ánh xạ đa tuyến tính (multilinear map) trong $\mathcal{T}^{r1+r2,s1+s2} (V$) được định nghĩa như sau:
$$(T_{1} \otimes T_{2})(\omega^{1} , \dots  , \omega^{r1} , \theta^{1} , \dots  , \theta^{r2} , v_{1}, \dots  , v_{s1}, y_{1}, \dots  , y_{s2})$$
$$= T_{1}(\omega^{1} , \dots  , \omega^{r1} , v_{1}, \dots  , v_{s1})T_{2}(\theta^{1} , \dots  , \theta^{r2} , y_{1}, \dots  , y_{s2}),$$
$$\in   \le  \le  \in  \le  \le  \in   \le  \le  \in$$
Với mọi $\omega^{i1} V^{*} (1 i_{1} r_{1}), v_{j1} V (1 j_{1} s_{1}), \theta^{i2} V^{*} (1 i_{2} r_{2}), y_{j2} V (1 \le j_{2} \le s_{2})$. Ta kiểm tra ngay lập tức rằng nếu $T_{1} \in T^{r1,s1} (V$) và $T_{2} \in T^{r2,s2} (V$), thì
$$\mu^{r1+r2,s1+s2} (T_{1} \otimes T_{2}) = \mu^{r1,s1} (T_{1}) \otimes \mu^{r2,s2} (T_{2}),$$
Ở đâu tích tenxơ (tensor product) trên trái là tích tenxơ (tensor product) trên $T^{r1,s1} (V$) $\times  T^{r2,s2} (V$) từ Định nghĩa 33.15, và tích tenxơ (tensor product) trên phải là tích tenxơ (tensor product) trên $\mathcal{T}^{r1,s1} (V$) $\times \mathcal{T}^{r2,s2} (V$) từ Định nghĩa 33.17. Nếu $V$ và $W$ là hai các không gian vectơ, với mọi ánh xạ tuyến tính (linear map) $\phi$: $V \to W$, nhắc lại rằng chuyển vị (transpose) $\phi^{\top}$ của $\phi$ là ánh xạ tuyến tính (linear map) $\phi^{\top}$: $W^{*} \to V^{*}$ cho trước bởi
$$\phi^{\top} (\omega ) = \omega  \circ \phi ,\omega  \in W^{*} .$$
Nếu $\phi$: $V \to W$ là tuyến tính đẳng cấu, nó cảm sinh ánh xạ tuyến tính (linear map) $\phi_{s}^{r}$: $\mathcal{T}^{r,s} (V$) $\to T^{r,s} (W)$ được định nghĩa như sau.

> **Định nghĩa 33.18.** Cho $\phi$: $V \to W$ là tuyến tính đẳng cấu của hữu hạn chiều các không gian vectơ. ánh xạ $\phi_{s}^{r}$: $\mathcal{T}^{r,s} (V$) $\to T^{r,s} (W)$ được định nghĩa như sau. Với mọi $T \in T^{r,s} (V$),
$$(\phi_{s}^{r} T)(\theta^{1} , \dots  , \theta^{r} , v_{1}, \dots  , v_{s}) = T(\phi^{\top} (\theta^{1} ), \dots  , \phi^{\top} (\theta^{r} ), \phi^{-1} (v_{1}), \dots  , \phi^{-1} (v_{s})),$$
Với mọi $\theta^{1} , \dots  , \theta^{r} \in W^{*}$ và tất cả $v_{1}, \dots  , v_{s} \in W$. Vì $\phi^{-1}$ và $\phi^{\top}$ là tuyến tính, $\phi_{s}^{r} T$ là đa tuyến tính, do đó trong $\mathcal{T}^{r,s}(W)$. sau đây mệnh đề được hiển thị trong Abraham và Marsden $[1]$ (Mệnh đề 1.7.4).

> **Mệnh đề 33.28.** Cho $\phi$: $E \to F$ và $\psi$: $F \to G$ là hai tuyến tính các đẳng cấu của hữu hạn chiều các không gian vectơ. Các tính chất sau đây đúng.
$(1) (\psi  \circ \phi )_{s}^{r} = \psi_{s}^{r}  \circ \phi_{s}^{r}$.
$(2)$ Nếu id: $E \to E$ là đồng nhất thức, thì $id_{s}^{r}$: $\mathcal{T}^{r,s} (E) \to T^{r,s} (E)$ là cũng đồng nhất thức.
$(3)$ ánh xạ $\phi_{s}^{r}$: $\mathcal{T}^{r,s}(E) \to T^{r,s}(F)$ là tuyến tính đẳng cấu và $(\phi_{s}^{r} )^{-1} = (\phi^{-1} )_{s}^{r}$.

<!-- PAGE 1210 -->
Tiếp theo mệnh đề cho các công thức cho các thành phần của $\phi_{s}^{r} T$ theo các thành phần của $T$ đối với các cơ sở của $E$ và $F$. Cho $(e_{1}, \dots  , e_{n})$ là cơ sở (basis) của $E, (f_{1}, \dots  , f_{n})$ là cơ sở (basis) của $F$, và cho $(e^{1}, \dots  , e^{n})$ là đối ngẫu (dual) cơ sở (basis) của $E^{*}$ và $(f^{1} , \dots  , f^{n}$) là đối ngẫu (dual) cơ sở (basis) của $F^{*}$. Nếu $A = (a_{i}^{j})$ là ma trận biểu diễn $\phi$ trong đối ngẫu (dual) interpretation cho trước (trong Einstein ký hiệu) bởi
$$\phi (e_{i}) = a_{i}^{j}f_{j},$$
Cụ thể là,
$$\begin{pmatrix} \phi (e_{1}) \\ \vdots \\ \phi (e_{n}) \end{pmatrix} = A \begin{pmatrix} f_{1} \\ \vdots \\ f_{n} \end{pmatrix} ,$$
Thì nó đã biết rằng ma trận biểu diễn $\phi^{\top}$ (cũng trong đối ngẫu (dual) interpretation) đối với đối ngẫu (dual) các cơ sở $(f^{1} , \dots  , f^{n}$) và $(e^{1}, \dots  , e^{n})$ là chuyển vị (transpose) $A^{\top}$ của ma trận $A$ (xem Gallier và Quaintance $[76]$, Mục 10.6). Điều này có nghĩa là
$$\phi^{\top} (f^{i} ) = a_{j}^{i}e^{j},$$
Ở đâu phép chuyển vị tương ứng với sự kiện rằng các chỉ số $i$ và $j$ là raised khi chuyển từ các vectơ đến đối ngẫu (đối ngẫu (dual)) của chúng. Nếu $B = (b_{i}^{j})$ ký hiệu nghịch đảo của $A$, thì ta có
$$\phi^{-1} (f_{i}) = b_{i}^{j}e_{j}.$$
Ta dễ dàng thu được kết quả sau đây.

> **Mệnh đề 33.29.** Cho $\phi$: $E \to F$ là tuyến tính đẳng cấu, $(e_{1}, \dots  , e_{n})$ là cơ sở (basis) của $E$, và $(f_{1}, \dots  , f_{n})$ là cơ sở (basis) của $F$. Nếu $A = (a_{i}^{j})$ là ma trận biểu diễn $\phi$ trong đối ngẫu (dual) interpretation như ở trên và $B = (b_{i}^{j})$ là nghịch đảo của nó, với mọi $T \in T^{r,s} (E)$ với các thành phần đối với cơ sở (basis) $\otimes \cdots \otimes  \otimes  \cdots \otimes$, các thành phần của với đối với $t_{j...js}^{i1...ir}  e_{i1} e_{ir} e^{j1} e^{js}  \phi_{s}^{r} T to^{1}$ cơ sở (basis) $f_{i1'} \otimes \cdots  \otimes f_{i'r} \otimes f_{1}^{j'} \cdots  \otimes f^{js'}$ được cho bởi
$$(t')_{j'...j'}^{i'1...i'r} = t_{j1...js}^{i1...ir}a_{i1}^{i'1} \cdots  a_{ir}^{i'r} \cdots  b_{j'}^{j1} \cdots  b_{j'}^{js}.$$
$$1s1s$$
Nhận thấy rằng Einstein phép lấy tổng quy ước pays offin tránh nhiều phép lấy tổng
$$symbols ( \sum  ).$$
Trong trường hợp đặc biệt khi $E = F$ và $\phi$ là đồng nhất thức, ta thu được công thức biểu diễn cách mà các thành phần của tenxơ thay đổi dưới chuyển cơ sở (change of basis). Điều này làm cho connection với old-fashion phương pháp cho định nghĩa các tenxơ. Một cái khác phép toán trên tổng quát các tenxơ, ánh xạ co (contraction), là hữu ích trong vi phân hình học.
