# Bidual và Chính tắc Pairings


<!-- PAGE 433 -->
Và nó là dễ để xem rằng chúng là độc lập tuyến tính (linearly independent). Vì vậy, không gian $U$ của các dạng tuyến tính trong $E^{*}$ được sinh (spanned) bởi ở trên các dạng tuyến tính (các phương trình) có số chiều $n$ - $1$, và không gian $U^{0}$ của các ma trận thỏa mãn tất cả các phương trình này có số chiều $n^{2}$ - $n + 1$. Nó là không do đó hiển nhiên để tìm cơ sở (basis) cho không gian này. Ta sẽ bây giờ pin xuống relationship giữa không gian vectơ (vector space) $E$ và của nó bidual $E^{**}$.

## 11.4 Bidual và Chính tắc Pairings


> **Mệnh đề 11.5.** Cho $E$ là không gian vectơ (vector space). Các tính chất sau đây đúng:
() ánh xạ tuyến tính (linear map) $eval_{E}$: $E \to E^{**}$ được định nghĩa sao cho
$$eval_{E}(v) = eval_{v}for all v \in E,$$
Rằng là, $eval_{E}(v)(u^{*}) = \langle u^{*}, v\rangle = u^{*}(v)$ với mọi $u^{*} \in E^{*}$, là đơn ánh (injective).
$(b)$ Khi $E$ là của hữu hạn số chiều $n$, ánh xạ tuyến tính (linear map) $eval_{E}$: $E \to E^{**}$ là đẳng cấu (được gọi là chính tắc đẳng cấu).
$$Proof. (a) Let (u_{i})_{i\in I} be a basis of E, and let v = \sum_{i}  \in I v_{i}u_{i}.If eval_{E}(v) = 0, then in$$
Cụ thể $eval_{E}(v)(u_{i}^{*}$) $= 0$ với mọi $u_{i}^{*}$, và vì
$$eval_{E}(v)(u_{i}^{*} ) = \langle u_{i}^{*} , v\rangle = v_{i},$$
Ta có $v_{i} = 0$ với mọi $i \in$ I, nghĩa là, $v = 0$, chỉ ra rằng $eval_{E}$: $E \to E^{**}$ là đơn ánh (injective). Nếu $E$ là của hữu hạn số chiều $n$, theo Định lý 11.4, với mọi cơ sở (basis) $(u_{1}, \dots  , u_{n})$, họ $(u_{1}^{*}, \dots  , u_{n}^{*})$ là cơ sở (basis) của không gian đối ngẫu (dual space) $E^{*}$, và do đó họ $(u_{1}^{**} , \dots  , u_{n}^{**}$) là cơ sở (basis) của bidual $E^{**}$. Điều này chỉ ra rằng dim(E) $= dim(E^{**}) = n$, và vì bởi Phần (), ta biết rằng $eval_{E}$: $E \to E^{**}$ là đơn ánh (injective), thực ra, $eval_{E}$: $E \to E^{**}$ là song ánh (bijective) (theo Mệnh đề 6.19).  Khi không gian vectơ (vector space) $E$ có vô hạn số chiều, $E$ và của nó bidual $E^{**}$ là không bao giờ đẳng cấu. Khi $E$ là của hữu hạn số chiều và $(u_{1}, \dots  , u_{n})$ là cơ sở (basis) của $E$, xét theo chính tắc đẳng cấu $eval_{E}$: $E \to E^{**}$, cơ sở (basis) $(u_{1}^{**} , \dots  , u_{n}^{**}$) của bidual được đồng nhất với $(u_{1}, \dots  , u_{n})$. Mệnh đề 11.5 có thể được reformulated rất fruitfully theo pairings, đáng chú ý hữu ích khái niệm discovered bởi Pontrjagin trong $1931$ (được điều chỉnh từ $E$. Artin $[6]$, Chương $1)$. Cho trước hai các không gian vectơ $E$ và $F$ trên trường $K$, ta nói rằng hàm $\phi$: $E \times  F \to K$ là song tuyến tính nếu với mọi $v \in V$, ánh xạ $u \mapsto \phi (u, v)$ (từ $E$ đến $K)$ là tuyến tính, và với mọi $u \in E$, ánh xạ $v \mapsto \phi (u, v)$ (từ $F$ đến $K)$ là tuyến tính.

> **Định nghĩa 11.4.** Cho trước hai các không gian vectơ $E$ và $F$ trên $K$, cặp giữa $E$ và $F$ là ánh xạ song tuyến tính (bilinear map) $\phi$: $E \times  F \to K$. Như vậy cặp là không suy biến khi và chỉ khi

<!-- PAGE 434 -->
$(1)$ với mọi $u \in E$, nếu $\phi (u, v) = 0$ với mọi $v \in F$, thì $u = 0$, và
$(2)$ với mọi $v \in F$, nếu $\phi (u, v) = 0$ với mọi $u \in E$, thì $v = 0$. cặp $\phi$: $E \times  F \to K$ là thường được ký hiệu bởi $\langle$ -, $-\rangle$: $E \times  F \to K$. Ví dụ, ánh xạ $\langle$ -, $-\rangle$: $E^{*} \times  E \to K$ được định nghĩa trước đó là không suy biến cặp (sử dụng chứng minh của () trong Mệnh đề 11.5). Nếu $E = F$ và $K = \mathbb{R}$, bất kỳ tích vô hướng (inner product) trên $E$ là không suy biến cặp (bởi vì tích vô hướng (inner product) là xác định dương (positive definite)); xem Chương $12$. Khác thú vị không suy biến pairings phát sinh trong đại số ngoài (exterior algebra) và vi phân hình học. Cho trước cặp $\phi$: $E \times  F \to K$, ta có thể định nghĩa hai các ánh xạ $l_{\phi}$: $E \to F^{*}$ và $r_{\phi}$: $F \to E^{*}$ như sau: Với mọi $u \in E$, ta định nghĩa dạng tuyến tính (linear form) $l_{\phi}(u)$ trong $F^{*}$ sao cho
$$l_{\phi}(u)(y) = \phi (u, y)for every y \in F,$$
Và với mọi $v \in F$, ta định nghĩa dạng tuyến tính (linear form) $r_{\phi}(v)$ trong $E^{*}$ sao cho
$$r_{\phi}(v)(x) = \phi (x, v)for every x \in E.$$
Ta có kết quả sau hữu ích mệnh đề.

> **Mệnh đề 11.6.** Cho trước hai các không gian vectơ $E$ và $F$ trên $K$, với mọi không suy biến cặp $\phi$: $E \times  F \to K$ giữa $E$ và $F$, các ánh xạ $l_{\phi}$: $E \to F^{*}$ và $r_{\phi}$: $F \to E^{*}$ là tuyến tính và đơn ánh (injective). Hơn nữa, nếu $E$ và $F$ có hữu hạn số chiều, thì số chiều này là cùng và $l_{\phi}$: $E \to F^{*}$ và $r_{\phi}$: $F \to E^{*}$ là các song ánh.

*Chứng minh.* các ánh xạ $l_{\phi}$: $E \to F^{*}$ và $r_{\phi}$: $F \to E^{*}$ là tuyến tính bởi vì cặp là song tuyến tính. Nếu $l_{\phi}(u) = 0$ (null tạo thành), thì
$$l_{\phi}(u)(v) = \phi (u, v) = 0for every v \in F,$$
Và vì $\phi$ là không suy biến, $u = 0$. Do đó, $l_{\phi}$: $E \to F^{*}$ là đơn ánh (injective). Tương tự, $r_{\phi}$: $F \to E^{*}$ là đơn ánh (injective). Khi $F$ có hữu hạn số chiều $n$, ta có được thấy rằng $F$ và $F^{*}$ có cùng số chiều. Vì $l_{\phi}$: $E \to F^{*}$ là đơn ánh (injective), ta có $m =$ dim(E) $\le$ dim(F) $= n$. cùng lập luận áp dụng đến $E$, và do đó $n =$ dim(F) $\le$ dim(E) $= m$. Nhưng khi đó, dim(E) $=$ dim(F), và $l_{\phi}$: $E \to F^{*}$ và $r_{\phi}$: $F \to E^{*}$ là các song ánh. Khi $E$ có hữu hạn số chiều, không suy biến cặp $\langle$ -, $-\rangle$: $E^{*} \times  E \to K$ cho ta một cái khác chứng minh của sự tồn tại của tự nhiên đẳng cấu giữa $E$ và $E^{**}$. Khi $E = F$, không suy biến cặp được cảm sinh bởi tích vô hướng (inner product) trên $E$ cho ta tự nhiên đẳng cấu giữa $E$ và $E^{*}$ (xem Mục 12.2). Ta bây giờ chỉ ra relationship giữa các siêu phẳng và các dạng tuyến tính.
