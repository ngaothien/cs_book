# Một số Hữu ích Các đẳng cấu cho Các tích tenxơ


<!-- PAGE 1187 -->

*Chứng minh.* Với mỗi $k, 1 \le k \le n$, mọi $v^{k} \in E_{k}$ có thể được được viết một cách duy nhất như
$$v^{k} = \sum_{j\in Ik}  v_{j}^{k} u_{j}^{k},$$
Với một số họ của các vô hướng $(v_{j}^{k} )_{j\in Ik}$. Cho $F$ là bất kỳ không tầm thường không gian vectơ (vector space). Ta chỉ ra rằng với mọi họ
$$(w_{i1,...,in})_{(i1,...,in)\in I1\times...\times In},$$
Của các vectơ trong $F$, tồn tại một ánh xạ tuyến tính (linear map) $h: E_{1} \otimes \cdots  \otimes E_{n} \to F$ sao cho
$$h(u_{i1}^{1} \otimes \cdots  \otimes u_{in}^{n}) = w_{i1,...,in}.$$
Thì theo Mệnh đề 33.4, suy ra rằng
$$(u_{i1}^{1} \otimes \cdots  \otimes u_{in}^{n})_{(i1,...,in)\in I1\times...\times In}$$
Là độc lập tuyến tính (linearly independent). Tuy nhiên, vì $(u_{i}^{k} )_{i\in Ik}$ là cơ sở (basis) cho $E_{k}$, $u_{i1}^{1} \otimes \cdots  \otimes u_{in}^{n}$ cũng sinh $E_{1} \otimes \cdots  \otimes E_{n}$, và do đó, chúng tạo thành cơ sở (basis) của $E_{1} \otimes \cdots  \otimes E_{n}$. Ta định nghĩa hàm $f$: $E_{1} \times  \cdots  \times  E_{n} \to F$ như sau: Với mọi $n$ khác rỗng hữu hạn các tập con $J_{1}, \dots  , J_{n}$ sao cho $J_{k} \subseteq I_{k}$ cho $k = 1, \dots  , n$,
$$f( \sum_{j1\in J1}  v_{j1}^{1}u_{j1}^{1}, \dots  , \sum_{jn\in Jn}  v_{jn}^{n}u_{jn}^{n}) = \sum_{J1,...,jn}  v_{j1}^{1} \cdots  v_{jn}^{n} w_{j1,...,jn}.$$
$$j1\in \in Jn$$
Ta kiểm chứng được ngay rằng $f$ là đa tuyến tính. Bởi phổ dụng ánh xạ tính chất của tích tenxơ (tensor product), ánh xạ tuyến tính (linear map) $f_{\otimes}: E_{1} \otimes \cdots  \otimes E_{n} \to F$ sao cho $f = f_{\otimes} \circ \phi$, là mong muốn ánh xạ $h$. Đặc biệt, khi mỗi $I_{k}$ là hữu hạn và của kích thước $m_{k} = dim(E_{k})$, ta xem rằng số chiều của tích tenxơ (tensor product) $E_{1} \otimes \cdots  \otimes E_{n}$ là $m_{1} \cdots  m_{n}$. Như hệ quả của Mệnh đề 33.12, nếu $(u_{i}^{k} )_{i\in Ik}$ là cơ sở (basis) cho $E_{k}, 1 \le k \le n$, thì mọi tenxơ $z \in E_{1} \otimes \cdots  \otimes E_{n}$ có thể được được viết trong duy nhất cách như
$$z = \sum_{n)\in I1}  \lambda_{i1,...,in}  u_{i1}^{1} \otimes \cdots  \otimes u_{in}^{n},$$
$$(i1,...,i\times ...\times In$$
Với một số duy nhất họ của các vô hướng $\lambda_{i1,...,in}  \in K$, tất cả không ngoại trừ cho hữu hạn số.

## 33.4 Một số Hữu ích Các đẳng cấu cho Các tích tenxơ


> **Mệnh đề 33.13.** Cho trước ba các không gian vectơ $E, F, G$, tồn tại duy nhất chính tắc các đẳng cấu
$(1)  \otimes  \sim  \otimes E F = F E$

<!-- PAGE 1188 -->
$(2)  \otimes  \otimes  \sim  \otimes  \otimes  \sim  \otimes  \otimes (E F) G = E (F G) = E F G$
$(3)  \oplus  \otimes  \sim  \otimes  \oplus  \otimes (E F) G = (E G) (F G)$
$(4)  \otimes  \sim K E = E$ sao cho respectively
$$(a) u \otimes v \mapsto v \otimes u$$
$$(b) (u \otimes v) \otimes w \mapsto u \otimes (v \otimes w) \mapsto u \otimes v \otimes w$$
$$(c) (u, v) \otimes w \mapsto (u \otimes w, v \otimes w)$$
$$(d) \lambda  \otimes u \mapsto \lambda u.$$

*Chứng minh.* Ngoại trừ cho $(3)$, các phần tử này các đẳng cấu được chứng minh bằng cách sử dụng phổ dụng ánh xạ tính chất của các tích tenxơ.
$(1)$ ánh xạ từ $E \times  F$ đến $F \otimes E$ cho trước bởi $(u, v) \mapsto v \otimes u$ là rõ ràng song tuyến tính, do đó nó cảm sinh duy nhất tuyến tính $\alpha$: $E \otimes F \to F \otimes E$ tạo ra sau đây biểu đồ giao hoán
$$\iota \otimes  /$$
$$E \times  FE \otimes F$$
$$L\overline{L}$$
$$\overline{L} L$$
$$LL$$
$$LL\alpha$$
$$LL$$
$$%$$
$$F \otimes E,$$
Sao cho
$$\alpha (u \otimes v) = v \otimes u,for all u \in E and all v \in F.$$
Tương tự, ánh xạ từ $F \times  E$ đến $E \otimes F$ cho trước bởi $(v, u) \mapsto u \otimes v$ là rõ ràng song tuyến tính, do đó nó cảm sinh duy nhất tuyến tính $\beta$: $F \otimes E \to E \otimes F$ tạo ra sau đây biểu đồ giao hoán
$$F \times  E^{\iota\otimes} /F \otimes E$$
$$LL$$
$$\overline{L} L$$
$$LL$$
$$LL\beta$$
$$LL$$
$$%$$
$$E \otimes F,$$
Sao cho
$$\beta (v \otimes u) = u \otimes v,for all u \in E and all v \in F.$$
Ta kiểm chứng được ngay rằng
$$(\beta  \circ \alpha )(u \otimes v) = u \otimes vand(\alpha  \circ \beta )(v \otimes u) = v \otimes u$$
Với mọi $u \in E$ và tất cả $v \in F$. Vì các tenxơ của tạo thành $u \otimes v$ sinh (span) $E \otimes F$ và tương tự các tenxơ của tạo thành $v \otimes u$ sinh (span) $F \otimes E$, ánh xạ $\beta  \circ \alpha$ là thực sự đồng nhất thức trên $E \otimes F$, và tương tự $\alpha  \circ \beta$ là đồng nhất thức trên $F \otimes E$, do đó $\alpha$ và $\beta$ là các đẳng cấu.

<!-- PAGE 1189 -->
$(2)$ Fix một số $w \in G$. ánh xạ
$$(u, v) \mapsto u \otimes v \otimes w$$
Từ $E \times F$ đến $E \otimes F \otimes G$ là song tuyến tính, và do đó có một ánh xạ tuyến tính (linear map) $f_{w}$: $E \otimes F \to E \otimes F \otimes G$ tạo ra sau đây biểu đồ giao hoán
$$\iota \otimes  /$$
$$E \times  FE \otimes F$$
$$O\overline{O}$$
$$\overline{O} O$$
$$OO$$
$$OOf$$
$$OOw$$
$$O'$$
$$E \otimes F \otimes G,$$
Với $f_{w}(u \otimes v) = u \otimes v \otimes w$. Tiếp theo xét ánh xạ
$$(z, w) \mapsto f_{w}(z),$$
Từ $(E \otimes F) \times  G$ vào $E \otimes F \otimes G$. Nó là dễ dàng được thấy là song tuyến tính, và do đó nó cảm sinh ánh xạ tuyến tính (linear map) $f$: $(E \otimes F) \otimes G \to E \otimes F \otimes G$ tạo ra sau đây biểu đồ giao hoán
$$(E \otimes F) \times  G^{\iota\otimes} /(E \otimes F) \otimes G$$
$$RR$$
$$RR$$
$$RR$$
$$RR$$
$$RRf$$
$$RR$$
$$R($$
$$E \otimes F \otimes G,$$
Với f((u $\otimes v) \otimes w) = u \otimes v \otimes w$. Cũng xét ánh xạ
$$(u, v, w) \mapsto (u \otimes v) \otimes w$$
Từ $E \times F \times G$ đến $(E \otimes F)\otimes G$. Nó là trilinear, và do đó có một ánh xạ tuyến tính (linear map) $g: E \otimes F \otimes G \to (E \otimes F) \otimes G$ tạo ra sau đây biểu đồ giao hoán
$$\iota \otimes  /$$
$$E \times  F \times  GE \otimes F \otimes G$$
$$QQ$$
$$QQ$$
$$QQ$$
$$QQ$$
$$QQg$$
$$QQ$$
$$Q($$
$$(E \otimes F) \otimes G,$$
Với g(u $\otimes v \otimes w) = (u \otimes v) \otimes w$. Rõ ràng, $f \circ g$ và $g \circ f$ là đồng nhất thức các ánh xạ, và do đó $f$ và $g$ là các đẳng cấu. khác trường hợp là đồng dạng.
$(3)$ Cho trước cố định không gian vectơ (vector space) $G$, với mọi hai các không gian vectơ $M$ và $N$ và mọi ánh xạ tuyến tính (linear map) $f$: $M \to N$, cho $\tau_{G} (f) = f \otimes id_{G}$ là duy nhất ánh xạ tuyến tính (linear map) tạo ra sau đây biểu đồ giao hoán.
$$M \times  G^{\iota M\otimes} /M \otimes G$$
$$f\times idGf\otimes idG$$
$$N \times  G_{\iota N\otimes} /N \otimes G$$

<!-- PAGE 1190 -->
Đồng nhất thức (*) được chứng minh trong Mệnh đề 33.10 chỉ ra rằng nếu $g: N \to P$ là một cái khác ánh xạ tuyến tính (linear map), thì $\tau_{G} (g) \circ \tau_{G} (f) = (g \otimes id_{G}) \circ (f \otimes id_{G}) = (g \circ f) \otimes (id_{G} \circ id_{G}) = (g \circ f) \otimes id_{G} = \tau_{G} (g \circ f)$. Rõ ràng, $\tau_{G} (0) = 0$, và trực tiếp phép tính trên các phần tử sinh cũng chỉ ra rằng
$$\tau_{G} (id_{M}) = (id_{M} \otimes id_{G}) = id_{M\otimes G},$$
Và rằng nếu f': $M \to N$ là một cái khác ánh xạ tuyến tính (linear map), thì
$$\tau_{G} (f + f' ) = \tau_{G} (f) + \tau_{G} (f' ).$$
Trong fancy các số hạng, $\tau_{G}$ là functor. Bây giờ, nếu $E \oplus F$ là tổng trực tiếp (direct sum), nó là tiêu chuẩn sự kiện của tuyến tính đại số rằng nếu $\pi_{E}$: $E \oplus F \to E$ và $\pi_{F}$: $E \oplus F \to F$ là phép chiếu các ánh xạ, thì $\pi_{E}  \circ \pi_{E}  = \pi_{E} \pi_{F}  \circ \pi_{F}  = \pi_{F} \pi_{E}  \circ \pi_{F}  = 0 \pi_{F}  \circ \pi_{E}  = 0 \pi_{E}  + \pi_{F}  = id_{E\oplus F}$. Nếu ta áp dụng $\tau_{G}$ đến các phần tử này identites, ta thu được $\tau_{G} (\pi_{E}$) $\circ \tau_{G} (\pi_{E}$) $= \tau_{G} (\pi_{E}$) $\tau_{G} (\pi_{F}$) $\circ \tau_{G} (\pi_{F}$) $= \tau_{G} (\pi_{F}$) $\tau_{G} (\pi_{E}$) $\circ \tau_{G} (\pi_{F}$) $= 0 \tau_{G} (\pi_{F}$) $\circ \tau_{G} (\pi_{E}$) $= 0 \tau_{G} (\pi_{E}$) $+ \tau_{G} (\pi_{F}$) $= id_{(E\oplus F)\otimes G}$. Nhận thấy rằng $\tau_{G} (\pi_{E}$) $= \pi_{E}  \otimes id_{G}$ là ánh xạ từ $(E \oplus F) \otimes G$ lên $E \otimes G$ và rằng $\tau_{G} (\pi_{F}$) $= \pi_{F}  \otimes id_{G}$ là ánh xạ từ $(E \oplus F) \otimes G$ lên $F \otimes G$, và bởi tuyến tính đại số, ở trên các phương trình có nghĩa rằng ta có tổng trực tiếp (direct sum)
$$\otimes  \oplus  \otimes  \sim  \oplus  \otimes$$
$$(EG)(FG)= (EF)G.$$
$(4)$ Ta có ánh xạ tuyến tính (linear map) $\epsilon$: $E \to K \otimes E$ cho trước bởi
$$\epsilon (u) = 1 \otimes u,for all u \in E.$$
Ánh xạ $(\lambda , u) \mapsto \lambda u$ từ $K \times  E$ đến $E$ là song tuyến tính, do đó nó cảm sinh duy nhất ánh xạ tuyến tính (linear map) $\eta$: $K \otimes E \to E$ tạo ra sau đây biểu đồ giao hoán
$$K \times  E^{\iota\otimes} /K \otimes E$$
$$LL$$
$$\overline{L} L$$
$$LL$$
$$LL\eta$$
$$LL$$
$$L%$$
$$E,$$
Sao cho $\eta (\lambda  \otimes u) = \lambda u$, với mọi $\lambda  \in K$ và tất cả $u \in E$. Ta có
$$(\eta  \circ \epsilon )(u) = \eta (1 \otimes u) = 1u = u,$$
Và
$$(\epsilon  \circ \eta )(\lambda  \otimes u) = \epsilon (\lambda u) = 1 \otimes (\lambda u) = \lambda (1 \otimes u) = \lambda  \otimes u,$$
Mà chỉ ra rằng cả hai $\epsilon  \circ \eta$ và $\eta  \circ \epsilon$ là đồng nhất thức, do đó $\epsilon$ và $\eta$ là các đẳng cấu.
