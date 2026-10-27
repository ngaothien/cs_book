# (r,s)-Các tenxơ


<!-- PAGE 1203 -->
Mà là của ta phép toán nhân trong $E \otimes F$. Điều này phép nhân được xác định bởi
$$(a \otimes b) \cdot  (c \otimes d) = (ac) \otimes (bd).$$
Trong tóm tắt, ta có kết quả sau mệnh đề.

> **Mệnh đề 33.23.** Cho trước hai K-algebra $E$ và $F$, phép toán trên $E \otimes F$ được định nghĩa trên các phần tử sinh bởi
$$(a \otimes b) \cdot  (c \otimes d) = (ac) \otimes (bd)$$
Làm cho $E \otimes F$ vào K-algebra. 33.7 $(r$, s)-Các tenxơ Trong vi phân hình học và trong vật lý nó là cần đến xét slightly nhiều hơn/thêm tổng quát các tenxơ.

> **Định nghĩa 33.14.** Cho trước không gian vectơ (vector space) $V$, với mọi cặp của không âm các số nguyên $(r, s)$, tenxơ không gian $T^{r,s} (V$) của loại/kiểu $(r, s)$ là tích tenxơ (tensor product)
$$T^{r,s}(V ) = V^{\otimes r}\otimes (V^{*})^{\otimes s}= V \otimes \cdots  \otimes V\otimes V^{*}\otimes \cdots  \otimes V^{*},$$
$$|{z}|{z}$$
$$rs$$
Với $T^{0,0} (V$) $= K$. Ta cũng định nghĩa đại số tenxơ (tensor algebra) $T^{\bullet,\bullet} (V$) như tổng trực tiếp (direct sum) (coproduct)
$$T^{\bullet,\bullet} (V ) =MT^{r,s} (V ).$$
$$r,s\ge 0$$
Các tenxơ trong $T^{r,s} (V$) được gọi là thuần nhất của bậc $(r, s)$. Lưu ý rằng các tenxơ trong $T^{r,0} (V$) là chỉ của ta “old các tenxơ” trong $V^{\otimes r}$. Ta tạo $T^{\bullet,\bullet} (V$) vào đại số bởi định nghĩa tích tenxơ (tensor product) các phép toán như sau.

> **Định nghĩa 33.15.** phép nhân các phép toán
$$\otimes : T^{r1,s1} (V ) \times  T^{r2,s2} (V ) \longrightarrow T^{r1+r2,s1+s2} (V )$$
Được định nghĩa sao cho nếu $u = u_{1} \otimes \cdots  \otimes u_{r1} \otimes u_{1}^{*} \otimes \cdots  \otimes u_{s1}^{*}$ và $v = v_{1} \otimes \cdots  \otimes v_{r2} \otimes v_{1}^{*} \otimes \cdots  \otimes v_{s2}^{*}$, thì
$$u \otimes v = u_{1} \otimes \cdots  \otimes u_{r1} \otimes v_{1} \otimes \cdots  \otimes v_{r2} \otimes u_{1}^{*} \otimes \cdots  \otimes u_{s1}^{*} \otimes v_{1}^{*} \otimes \cdots  \otimes v_{s2}^{*}.$$
Ký hiệu bởi $Hom(V^{r}, (V^{*})^{s}; W)$ không gian vectơ (vector space) của tất cả đa tuyến tính các ánh xạ từ $V^{r} \times  (V^{*})^{s}$ đến $W$. Thì ta có phổ dụng ánh xạ tính chất mà khẳng định rằng có một chính tắc đẳng cấu
$$\sim$$
$$Hom(T^{r,s}(V ), W)= Hom(V^{r}, (V^{*})^{s}; W).$$

<!-- PAGE 1204 -->
Đặc biệt,
$$\sim$$
$$(T^{r,s}(V ))^{*}= Hom(V^{r}, (V^{*})^{s}; K).$$
Cho hữu hạn dimensional các không gian vectơ, đối ngẫu của Mục 33.5 là cũng dễ dàng được mở rộng đến tenxơ các không gian $T^{r,s} (V$). Ta định nghĩa cặp
$$T^{r,s} (V^{*} ) \times  T^{r,s} (V ) \longrightarrow K$$
Như sau: nếu
$$v^{*}= v_{1}^{*} \otimes \cdots  \otimes v_{r}^{*} \otimes u_{r+1} \otimes \cdots  \otimes u_{r+s} \in T^{r,s}(V^{*} )$$
Và
$$u = u_{1} \otimes \cdots  \otimes u_{r} \otimes v_{r+1}^{*} \otimes \cdots  \otimes v_{r+s}^{*} \in T^{r,s}(V ),$$
Thì
$$(v^{*}, u) = v_{1}^{*}(u_{1}) \cdots  v_{r+s}^{*}(u_{r+s}).$$
Điều này là không suy biến cặp, và do đó ta thu được chính tắc đẳng cấu
$$\sim$$
$$(T^{r,s}(V ))^{*}= T^{r,s}(V^{*}).$$
Hệ quả là, ta thu được chính tắc đẳng cấu
$$\sim$$
$$T^{r,s}(V^{*})= Hom(V^{r}, (V^{*})^{s}; K).$$
Ta summarize các kết quả này trong sau đây mệnh đề.

> **Mệnh đề 33.24.** Cho $V$ là không gian vectơ (vector space) và cho
$$T^{r,s}(V ) = V^{\otimes r}\otimes (V^{*})^{\otimes s}= V \otimes \cdots  \otimes V\otimes V^{*}\otimes \cdots  \otimes V^{*}.$$
$$|{z}|{z}$$
$$rs$$
Ta có chính tắc các đẳng cấu
$$\sim$$
$$(T^{r,s}(V ))^{*}= T^{r,s}(V^{*}),$$
Và
$$\sim$$
$$T^{r,s}(V^{*})= Hom(V^{r}, (V^{*})^{s}; K).$$
Mệnh đề 33.18 specializes đến trường hợp ở đâu $E_{i} = F_{j} = V$ cho $i = 1, \dots  , r$ và $j = 1, \dots  , s$, và điều này cho ta đặc trưng của $(r$, s)-các tenxơ theo đa tuyến tính các ánh xạ.

> **Mệnh đề 33.25.** Cho $V$ là không gian vectơ hữu hạn chiều. Ta có chính tắc đẳng cấu
$$\mu^{r,s} : T^{r,s}(V ) \to Hom((V^{*})^{r}, V^{s}; K)$$
Cho trước bởi
$$\mu^{r,s} (u_{1} \otimes \cdots  \otimes u_{r} \otimes v_{1}^{*} \otimes \cdots  \otimes v_{s}^{*})(x_{1}^{*}, \dots  , x_{r}^{*}, y_{1}, \dots  , y_{s}) = \prod_{i=1j}^{r}  \prod_{=1}^{s}  x_{i}^{*} (u_{i})v_{j}^{*}(y_{j}),$$
Với mọi $u_{i} \in V, x_{i}^{*} \in V^{*} (1 \le i \le r)$, và tất cả $y_{j} \in V, v_{j}^{*} \in V^{*} (1 \le j \le s)$. Tại thứ nhất glance, điều này quan điểm của các tenxơ như đa tuyến tính các ánh xạ có thể xuất hiện somewhat contorted, nhưng nó là nhiều hơn/thêm thuận tiện để định nghĩa và manipulate tenxơ các trường. Cho điều này lý do, như vậy định nghĩa của các tenxơ như đa tuyến tính các ánh xạ là thường được sử dụng trong literature
