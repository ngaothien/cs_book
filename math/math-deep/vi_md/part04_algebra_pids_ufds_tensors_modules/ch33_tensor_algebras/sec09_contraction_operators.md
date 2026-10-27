# Ánh xạ co (contraction) Các toán tử


<!-- PAGE 1211 -->

## 33.9 Ánh xạ co (contraction) Các toán tử


> **Định nghĩa 33.19.** Với mọi $r, s \ge 1$, ánh xạ co (contraction) $c_{i,j}$: $T^{r,s} (V$) $\to T^{r-1,s-1} (V$), với $1 \le i \le r$ và $1 \le j \le s$, là ánh xạ tuyến tính (linear map) được định nghĩa trên các phần tử sinh bởi $c_{i,j}(u_{1} \otimes \cdots  \otimes u_{r} \otimes \omega^{1} \otimes \cdots  \otimes \omega^{s}$)
$$= \omega^{j} (u_{i}) u_{1} \otimes \cdots  \otimes u_{i} \otimes \cdots  \otimes u_{r} \otimes \omega^{1} \otimes \cdots  \otimes \omega^{j} \otimes \cdots  \otimes \omega^{s} ,$$
$$c$$
$$b$$
$u_{i} \in V , \omega^{j} \in V^{*}$, ở đâu hat trên lập luận có nghĩa là nó nên được bỏ qua. Lưu ý rằng vì $T^{r,s}(V$) là tích tenxơ (tensor product) $T^{r,s}(V$) $= V^{\otimes r} \otimes (V^{*})^{\otimes s}$, ánh xạ $c_{i,j}$ là duy nhất tuyến tính mở rộng của ánh xạ đa tuyến tính (multilinear map) từ $V^{r} \times  (V^{*})^{s}$ đến $V^{\otimes r} \otimes (V^{*})^{\otimes s}$ cho trước bởi $c_{i,j}(u_{1}, \dots  , u_{r}, \omega^{1} , \dots  , \omega^{s}$) $= \omega^{j} (u_{i}) u_{1} \otimes \cdots  \otimes u_{i} \otimes \cdots  \otimes u_{r} \otimes \omega^{1} \otimes \cdots  \otimes \omega^{j} \otimes \cdots  \otimes \omega^{s}$.
$$c$$
$$b$$
Vì vậy định nghĩa này là nội tại, nghĩa là, không phụ thuộc vào bất kỳ lựa chọn của cơ sở (basis).
Nhận xét: Lưu ý rằng ký hiệu $c_{i,j}$ là ambiguous, vì technically ta có toán tử $c_{i,j}^{r,s}$: $T^{r,s}(V$) $\to T^{r-1,s-1}(V$) với mọi cặp $r, s \ge 1$, với $1 \le i \le r$ và $1 \le j \le s$, và $c_{i,j}^{s,r}$ ̸ $= c_{i,j}^{r',s'}$ nếu $(r$, s)̸ $=$ (r', s'), $1 \le i \le$ min(r, r') và $1 \le j \le$ min(s, s'). Tuy nhiên nó là thông lệ đến bỏ qua các chỉ số trên $r$ và $s$ và rely trên context đến infer $r$ và $s$. ký hiệu $c_{i,j}$ cũng được sử dụng bởi Gallot, Hulin, Lafontaine $[77]$, nhưng Sakai $[147]$ sử dụng $c_{j}^{i}$, và O’Neill $[137]$ sử dụng $c_{i}^{j}$. Cho chúng ta hình của ta những gì là $c_{1,1}$: $T^{1,1} (V$) $\to \mathbb{R}$, nghĩa là $c_{1,1}$: $V \otimes V^{*} \to \mathbb{R}$. Nếu $(e_{1}, \dots  , e_{n})$ là cơ sở (basis) của $V$ và $(e^{1}, \dots  , e^{n})$ là đối ngẫu (dual) cơ sở (basis), theo Mệnh đề 33.12, mọi $h \in V \otimes V^{*}$ có thể được biểu diễn dưới dạng
$$h = a_{j}^{i} e_{i} \otimes e^{j}.$$
Như
$$c_{1,1}(e_{i} \otimes e^{j}) = \delta_{i,j} ,$$
Ta thu được
$$c_{1,1}(h) = a_{i}^{i}.$$
Nhận xét: Theo Mệnh đề 33.25, $V \otimes V^{*}$ là đẳng cấu $to\mathcal{T}^{1,1} (V$), và theo Mệnh đề 33.26, $\mathcal{T}^{1,1} (V$) là đẳng cấu đến Hom(V, $V$). Do đó ta có thể quan điểm $h \in V \otimes V^{*}$ như ánh xạ tuyến tính (linear map). ma trận của $h$ trên cơ sở (basis) $(e_{1}, \dots  , e_{n})$ là cũng $(a_{j}^{i})$, do đó tr(h) $= a_{i}^{i}$ là vết (vết (trace)) của nó. Vì $c_{1,1}$ được định nghĩa một cách độc lập của bất kỳ cơ sở (basis), $c_{1,1}$ cung cấp nội tại định nghĩa của vết (trace) của ánh xạ tuyến tính (linear map) $h \in$ Hom(V, $V$). khái niệm của ánh xạ co (contraction) transfers đến không gian $\mathcal{T}^{r,s} (V$), nhưng tại thứ nhất glance, ta không’t có nội tại định nghĩa vì nó xuất hiện rằng ta có đến resort đến các cơ sở. Có một cách đến circumvent bài toán này như được giải thích trong O’Neill $[137]$ (Chương $2$, Bổ đề $6)$. bước thứ nhất là để chỉ ra rằng ánh xạ co (contraction) $c_{1,1}$ từ $\mathcal{T}^{1,1} (V$) đến $K$ là intrinsically được định nghĩa.

<!-- PAGE 1212 -->

> **Mệnh đề 33.30.** Tồn tại duy nhất một ánh xạ tuyến tính (linear map) $c_{1,1}$: $\mathcal{T}^{1,1} (V$) $\to K$ sao cho
$$c_{1,1}(\mu (u \otimes \theta )) = \theta (u),u \in V, \theta  \in V^{*} .$$

*Chứng minh.* Nếu ta chọn cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $V$, ta xem ngay lập tức rằng với mọi $T \in T^{1,1} (V$) được biểu diễn như
$$T = t_{j}^{i} e_{i} \otimes e^{j},$$
(một lần nữa, viết $e_{i} \otimes e^{j}$ thay vì của $\mu (e_{i} \otimes e^{j}))$, vì $c_{1,1}(e_{i} \otimes e^{j}) = e^{j}(e_{i}) = \delta_{ij}$, ta phải có
$$c_{1,1}(T) = t_{i}^{i}.$$
Cho trước một cái khác cơ sở (basis) $(f_{1}, \dots  , f_{n})$, nếu cơ sở (cơ sở (basis)) này được biểu diễn theo cơ sở (basis) $(e_{1}, \dots  , e_{n})$ như
$$e_{i} = a_{i}^{j}f_{j},$$
Thì theo Mệnh đề 33.29), ta có
$$f^{i}= a_{j}^{i}e^{j},$$
Do đó nếu $(b_{i}^{j})$ là nghịch đảo của $(a_{i}^{j})$, ta thu được
$$T = t_{j}^{i}a_{i}^{k} b_{l}^{j} f_{k} \otimes f^{l},$$
Và do đó contracted tenxơ trên mới các cơ sở được cho bởi
$$c_{1,1}'(T) = t_{j}^{i}a_{i}^{k} b_{k}^{j}.$$
Nhưng $(b_{i}^{j})$ là nghịch đảo của $(a_{i}^{j})$, do đó $a_{i}^{k} b_{k}^{j} = \delta_{ij}$, mà suy ra theo Mệnh đề 33.29 rằng
$$c_{1,1}'(T) = t_{i}^{i} = c_{1,1}(T).$$
Vì vậy, $c_{1,1}(T)$ là độc lập của lựa chọn của cơ sở (basis). Trong tổng quát trường hợp, ta có kết quả sau kết quả.

> **Mệnh đề 33.31.** Tồn tại duy nhất một ánh xạ tuyến tính (linear map) $c_{i,j}$: $\mathcal{T}^{r,s} (V$) $\to T^{r-1,s-1} (V$), với $1 \le i \le r$ và $1 \le j \le s$, sao cho (omitting ánh xạ $\mu$) $c_{i,j}(u_{1} \otimes \cdots  \otimes u_{r} \otimes \omega^{1} \otimes \cdots  \otimes \omega^{s}$)
$$= \omega^{j} (u_{i}) u_{1} \otimes \cdots  \otimes u_{i} \otimes \cdots  \otimes u_{r} \otimes \omega^{1} \otimes \cdots  \otimes \omega^{j} \otimes \cdots  \otimes \omega^{s} ,$$
$$c$$
$$b$$
$u_{i} \in V , \omega^{j} \in V^{*}$.

<!-- PAGE 1213 -->

*Chứng minh.* Nếu ta chọn cơ sở (basis) $(e_{1} \dots  , e_{n})$ trong $V$, bằng cách sử dụng Einstein phép lấy tổng quy ước, (omitting ánh xạ $\mu$), với mọi $\alpha  \in T^{r,s} (V$), ta có thể viết
$$\alpha  = a_{j1...js}^{i1...ir} e_{i1} \otimes \cdots  \otimes e_{ir} \otimes e^{j1}\otimes \cdots  \otimes e^{js},$$
Và vì $e^{j}(e_{i}) = \delta_{ij}$, ta phải có
$$c_{k,l}(\alpha ) = a_{j1...jl-1mjl+1...js}^{i1...ik-1mik+1...ir} e_{i1} \otimes \cdots  \otimes e_{ik} \otimes \cdots  \otimes e_{ir} \otimes e^{j1}\otimes \cdots  \otimes e_{l}^{j}\otimes \cdots  \otimes e^{js},$$
$$c$$
$$c$$
Ở đâu repeated chỉ số $m$ xuất hiện như superscript trong position $k$ và như chỉ số dưới trong position $l$, do đó theo Einstein phép lấy tổng quy ước,
$$a_{j1...jl-1mjl+1...,js}^{i1...ik-1mik+1...ir}$$
Ký hiệu tổng
$$\sum_{m=1}^{n}  a_{j1...jl-1mjl+1...js}^{i1...ik-1mik+1...ir} .$$
Cho trước một cái khác cơ sở (basis) $(f_{1}, \dots  , f_{n})$, nếu cơ sở (cơ sở (basis)) này được biểu diễn theo cơ sở (basis) $(e_{1}, \dots  , e_{n})$ như
$$e_{i} = a_{i}^{j}f_{j},$$
Thì theo Mệnh đề 33.29, ta có
$$\alpha  = t_{j1...js}^{i1...ir}a_{i1}^{i'1} \cdots  a_{ir}^{i'r} \cdots  b_{j'}^{j1} \cdots  b_{j'}^{js} f_{i1'} \otimes \cdots  \otimes f_{i'r} \otimes f^{j1'} \otimes \cdots  \otimes f^{js'} .$$
$$1s$$
Hệ quả là, contracting trên cặp của các chỉ số $(i_{k}', j_{l}')$, contracted tenxơ trên mới các cơ sở được cho bởi
$$c_{k,l}'(\alpha ) = t_{j1...m...js}^{i1...m...ir}a_{i1}^{i'1} \cdots a_{ik}^{m} \cdots  a_{ir}^{i'r} b_{j'}^{j1} \cdots  cb_{m}^{jl} \cdots  b_{j'}^{js}$$
$$c$$
$$1s$$
$$f_{i1'} \otimes \cdots  \otimes f_{ik'} \otimes \cdots  \otimes f_{i'r} \otimes f^{j1'} \otimes \cdots  \otimes f_{l}^{j'}  \otimes \cdots  \otimes f^{js'} .$$
$$cc$$
Vì $(b_{i}^{j})$ là nghịch đảo của $(a_{i}^{j})$, ta có $a_{ik}^{m}b_{m}^{jl} = \delta_{ikjl}$, mà suy ra rằng
$$c_{k,l}'(\alpha ) = t_{j1...m...js}^{i1...m...ir}a_{i1}^{i'1} \cdots a_{ik}^{m} \cdots  a_{ir}^{i'r} b_{j'}^{j1} \cdots  cb_{m}^{jl} \cdots  b_{j'}^{js}$$
$$c$$
$$1s$$
$$f_{i1'} \otimes \cdots  \otimes f_{ik'} \otimes \cdots  \otimes f_{i'r} \otimes f^{j1'} \otimes \cdots  \otimes f_{l}^{j'}  \otimes \cdots  \otimes f^{js'}$$
$$cc$$
$$= t_{j1...m...js}^{i1...m...ir} e_{i1} \otimes \cdots  \otimes e_{ik} \otimes \cdots  \otimes e_{ir} \otimes e^{j1}\otimes \cdots  \otimes e_{l}^{j}\otimes \cdots  \otimes e^{js}$$
$$c$$
$$c$$
$$= c_{k,l}(\alpha ).$$
Vì vậy, định nghĩa của $c_{k,l}$ là nội tại; nó không phụ thuộc vào lựa chọn của cơ sở (basis). Ta bây giờ turn đến đối xứng các tenxơ.
