# Các hoán vị, Signature của Hoán vị


<!-- PAGE 219 -->
Chương $7$ Các định thức Trong chương này tất cả các không gian vectơ được định nghĩa trên tùy ý trường $K$. Cho sake của concreteness, độc giả có thể safely giả sử rằng $K =\mathbb{R}$.

## 7.1 Các hoán vị, Signature của Hoán vị

Điều này chương chứa ôn tập/tổng quan của các định thức và của chúng sử dụng trong tuyến tính đại số. Ta bắt đầu với các hoán vị và signature của hoán vị. Tiếp theo, ta định nghĩa đa tuyến tính các ánh xạ và thay phiên đa tuyến tính các ánh xạ. Các định thức là đã giới thiệu như thay phiên đa tuyến tính các ánh xạ lấy giá trị $1$ trên unit ma trận (sau đây Emil Artin). Nó là thì được hiển thị cách mà để tính định thức (determinant) bằng cách sử dụng Laplace expansion công thức, và connection với thông thường định nghĩa được tạo. Nó được hiển thị cách mà các định thức có thể được sử dụng để nghịch đảo các ma trận và để giải (ít nhất trong lý thuyết!) các hệ của các phương trình tuyến tính (Cramer các công thức). định thức (determinant) của ánh xạ tuyến tính (linear map) được định nghĩa. Ta kết luận bởi định nghĩa đa thức đặc trưng (characteristic polynomial) của ma trận (và của ánh xạ tuyến tính (linear map)) và bởi chứng minh celebrated Cayley-Hamilton định lý mà phát biểu rằng mọi ma trận là “không” của của nó đa thức đặc trưng (characteristic polynomial) (ta cho hai các chứng minh; một tính toán, khác một nhiều hơn/thêm conceptual). Các định thức có thể được được định nghĩa trong một vài các cách. Ví dụ, các định thức có thể được được định nghĩa trong fancy cách theo đại số ngoài (exterior algebra) (hoặc thay phiên đại số) của không gian vectơ (vector space). Ta sẽ suy ra nhiều hơn/thêm algorithmic cách tiếp cận do Emil Artin. Không có matter mà cách tiếp cận là theo sau, ta cần một vài kiến thức chuẩn bị về các hoán vị trên hữu hạn tập hợp. Ta cần để chỉ ra rằng mọi hoán vị trên $n$ các phần tử là tích của các phép chuyển vị, và rằng tính chẵn lẻ của số của các phép chuyển vị liên quan là bất biến của hoán vị. Cho $[n] = {1, 2 \dots  , n}$, ở đâu $n \in \mathbb{N}$, và $n > 0$.

> **Định nghĩa 7.1.** hoán vị trên $n$ các phần tử là song ánh $\pi$: $[n] \to [n]$. Khi $n = 1$, chỉ hàm từ $[1]$ đến $[1]$ là hằng số ánh xạ: $1 \mapsto 1$. Do đó, ta sẽ giả sử rằng $n \ge 2$. phép chuyển vị là hoán vị $\tau$: $[n] \to [n]$ sao cho, với một số $i < j$ (với $1 \le i < j \le n), \tau (i) = j, \tau (j) = i$, và $\tau (k) = k$, với mọi $k \in [n] -{i, j}$. Nói cách khác, phép chuyển vị hoán đổi hai phân biệt các phần tử $i, j \in [n]$. xích (cyclic) hoán vị của thứ tự $k$ (hoặc $k$-chu trình) là
$$219$$

<!-- PAGE 220 -->
Hoán vị $\sigma$: $[n] \to [n]$ sao cho, với một số dãy $(i_{1}, i_{2}, \dots  , i_{k})$ của phân biệt các phần tử của $[n]$ với $2 \le k \le n$,
$$\sigma (i_{1}) = i_{2}, \sigma (i_{2}) = i_{3}, \dots  , \sigma (i_{k-1}) = i_{k}, \sigma (i_{k}) = i_{1},$$
Và $\sigma (j) = j$, cho $j \in [n]-{i_{1}, \dots  , i_{k}}$. tập hợp ${i_{1}, \dots  , i_{k}}$ được gọi là miền xác định của xích (cyclic) hoán vị, và xích (cyclic) hoán vị thường được ký hiệu bởi $(i_{1} i_{2} \dots  i_{k})$. Nếu $\tau$ là phép chuyển vị, rõ ràng, $\tau  \circ \tau  =$ id. Cũng, xích (cyclic) hoán vị của thứ tự $2$ là phép chuyển vị, và cho xích (cyclic) hoán vị $\sigma$ của thứ tự $k$, ta có $\sigma^{k} =$ id. Rõ ràng, hợp thành của hai các hoán vị là hoán vị và mọi hoán vị có nghịch đảo mà là cũng hoán vị. Vì vậy, tập hợp của các hoán vị trên $[n]$ là nhóm thường được ký hiệu $\mathfrak{S}_{n}$. Nó là dễ để chỉ ra bởi quy nạp rằng nhóm $\mathfrak{S}_{n}$ có $n$! các phần tử. Ta sẽ cũng sử dụng thuật ngữ tích của các hoán vị (hoặc các phép chuyển vị), như synonym cho hợp thành của các hoán vị. hoán vị $\sigma$ trên $n$ các phần tử, nói $\sigma (i) = k_{i}$ cho $i = 1, \dots  , n$, có thể được biểu diễn trong phiếm hàm ký hiệu bởi $2 \times  n$ mảng (array)
$$\begin{pmatrix} 1 \\ \cdots & i & \cdots & n \\ k_{1} & \cdots & k_{i} & \cdots & k_{n} \end{pmatrix}$$
Đã biết như Cauchy two-line ký hiệu. Ví dụ, ta có hoán vị $\sigma$ được ký hiệu bởi
$$\begin{pmatrix} 1 & 2 & 3 & 4 & 5 & 6 \\ 2 & 4 & 3 & 6 & 5 & 1 \end{pmatrix} .$$
Nhiều hơn/thêm concise ký hiệu thường được sử dụng trong máy tính khoa học và trong combinatorics là để biểu diễn hoán vị bởi ảnh (ảnh (image)) của nó, cụ thể là bởi dãy
$$\sigma (1) \sigma (2) \cdots  \sigma (n)$$
Được viết như vectơ hàng (row vector) mà không có commas tách các phần tử (entries). ở trên là đã biết như one-line ký hiệu. Ví dụ, trong one-line ký hiệu, của ta trước đó hoán vị $\sigma$ được biểu diễn bởi
$$2 4 3 6 5 1.$$
Lý do cho không enclosing ở trên dãy trong phạm vi parentheses là tránh confusion với ký hiệu cho các chu trình, cho mà là nó thông lệ đến bao gồm parentheses. sau đây mệnh đề chỉ ra importance của xích (cyclic) các hoán vị và các phép chuyển vị.

> **Mệnh đề 7.1.** Với mọi $n \ge 2$, với mọi hoán vị $\pi$: $[n] \to [n]$, có một phân hoạch của $[n]$ vào $r$ các tập con được gọi là orbits của $\pi$, với $1 \le r \le n$, ở đâu mỗi tập hợp $J$ trong điều này phân hoạch là hoặc singleton ${i}$, hoặc nó là của tạo thành
$$J = {i, \pi (i), \pi^{2} (i), \dots  , \pi^{ri-1} (i)},$$

<!-- PAGE 221 -->
Ở đâu $r_{i}$ là nhỏ nhất số nguyên, sao cho, $\pi^{ri} (i) = i$ và $2 \le r_{i} \le n$. Nếu $\pi$ là không đồng nhất thức, thì nó có thể được được viết trong duy nhất cách (sai khác thứ tự) như hợp thành $\pi  = \sigma_{1}  \circ \dots  \circ \sigma_{s}$ của xích (cyclic) các hoán vị với rời nhau các miền, ở đâu $s$ là số của orbits với ít nhất hai các phần tử. Mọi hoán vị $\pi$: $[n] \to [n]$ có thể được viết dưới dạng khác rỗng hợp thành của các phép chuyển vị.

*Chứng minh.* Xét quan hệ $R_{\pi}$ được định nghĩa trên $[n]$ như sau: $iR_{\pi}j$ khi và chỉ khi tồn tại một $k \ge 1$ sao cho $j = \pi^{k} (i)$. Ta khẳng định rằng $R_{\pi}$ là quan hệ tương đương (equivalence relation). Transitivity là hiển nhiên. Ta khẳng định rằng với mọi $i \in [n]$, tồn tại một least $r (1 \le r \le n)$ sao cho $\pi^{r} (i) = i$. Thật vậy, xét sau đây dãy của $n + 1$ các phần tử:
$$\langle i, \pi (i), \pi^{2} (i), \dots  , \pi^{n} (i)\rangle .$$
Vì $[n]$ chỉ có $n$ phân biệt các phần tử, có một số $h, k$ với $0 \le h < k \le n$ sao cho
$$\pi^{h} (i) = \pi^{k} (i),$$
Và vì $\pi$ là song ánh, điều này suy ra $\pi^{k-h} (i) = i$, ở đâu $0 \le k$ - $h \le n$. Do đó, ta được chứng minh rằng tồn tại một số nguyên $m \ge 1$ sao cho $\pi^{m} (i) = i$, do đó ở đó là như vậy nhỏ nhất số nguyên $r$. Hệ quả là, $R_{\pi}$ là reflexive. Nó là đối xứng, vì nếu $j = \pi^{k} (i)$, đặt $r$ là least $r \ge 1$ sao cho $\pi^{r} (i) = i$, thì
$$i = \pi^{kr} (i) = \pi^{k(r-1)} (\pi^{k} (i)) = \pi^{k(r-1)} (j).$$
Bây giờ, với mọi $i \in [n]$, lớp tương đương (equivalence class) (orbit) của $i$ là tập con của $[n]$, hoặc singleton ${i}$ hoặc tập hợp của tạo thành
$$J = {i, \pi (i), \pi^{2} (i), \dots  , \pi^{ri-1} (i)},$$
Ở đâu $r_{i}$ là nhỏ nhất số nguyên sao cho $\pi^{ri} (i) = i$ và $2 \le r_{i} \le n$, và trong trường hợp thứ hai, thu hẹp của $\pi$ đến $J$ cảm sinh xích (cyclic) hoán vị $\sigma_{i}$, và $\pi  = \sigma_{1}  \circ \dots  \circ \sigma_{s}$, ở đâu $s$ là số của các lớp tương đương có ít nhất hai các phần tử. Cho phần thứ hai của mệnh đề, ta tiến hành bằng quy nạp theo $n$. Nếu $n = 2$, có chính xác hai các hoán vị trên $[2]$, phép chuyển vị $\tau$ exchanging $1$ và $2$, và đồng nhất thức. Tuy nhiên, $id_{2} = \tau^{2}$. Bây giờ, cho $n \ge 3$. Nếu $\pi (n) = n$, vì theo giả thiết quy nạp, thu hẹp của $\pi$ đến $[n$ - $1]$ có thể được viết dưới dạng tích của các phép chuyển vị, $\pi$ chính nó có thể được viết dưới dạng tích của các phép chuyển vị. Nếu $\pi (n) = k \neq  n$, đặt $\tau$ là phép chuyển vị sao cho $\tau (n) = k$ và $\tau (k) = n$, rõ ràng là $\tau  \circ \pi$ để lại $n$ bất biến, và theo giả thiết quy nạp, ta có $\tau  \circ \pi  = \tau_{m}  \circ \dots  \circ \tau_{1}$ với một số các phép chuyển vị, và do đó
$$\pi  = \tau  \circ \tau_{m}  \circ \dots  \circ \tau_{1} ,$$
Tích của các phép chuyển vị (vì $\tau  \circ \tau  = id_{n})$.

<!-- PAGE 222 -->
Nhận xét: Khi $\pi  = id_{n}$ là đồng nhất thức hoán vị, ta có thể agree rằng hợp thành của $0$ các phép chuyển vị là đồng nhất thức. phần thứ hai của Mệnh đề 7.1 chỉ ra rằng các phép chuyển vị sinh nhóm của các hoán vị $\mathfrak{S}_{n}$. Trong viết hoán vị $\pi$ như hợp thành $\pi  = \sigma_{1}  \circ \dots  \circ \sigma_{s}$ của xích (cyclic) các hoán vị, rõ ràng là thứ tự của $\sigma_{i}$ thực hiện không matter, vì của chúng các miền là rời nhau. Cho trước hoán vị được viết như tích của các phép chuyển vị, ta bây giờ chỉ ra rằng tính chẵn lẻ của số của các phép chuyển vị là bất biến.

> **Định nghĩa 7.2.** Với mọi $n \ge 2$, vì mọi hoán vị $\pi$: $[n] \to [n]$ định nghĩa phân hoạch của $r$ các tập con trên mà $\pi$ acts hoặc như đồng nhất thức hoặc như xích (cyclic) hoán vị, cho $\epsilon (\pi$), được gọi là signature của $\pi$, được định nghĩa bởi $\epsilon (\pi$) $= (-1)^{n-r}$, ở đâu $r$ là số của các tập hợp trong phân hoạch. Nếu $\tau$ là phép chuyển vị exchanging $i$ và $j$, rõ ràng là phân hoạch liên kết với $\tau$ bao gồm của $n$ - $1$ các lớp tương đương, tập hợp ${i, j}$, và $n$ - $2$ singleton các tập hợp ${k}$, cho $k \in [n] -{i, j}$, và do đó, $\epsilon (\tau$) $= (-1)^{n-(n-1)} = (-1)^{1} = -1$.

> **Mệnh đề 7.2.** Với mọi $n \ge 2$, với mọi hoán vị $\pi$: $[n] \to [n]$, với mọi phép chuyển vị $\tau$, ta có
$$\epsilon (\tau  \circ \pi ) = -\epsilon (\pi ).$$
Hệ quả là, với mọi tích của các phép chuyển vị sao cho $\pi  = \tau_{m}  \circ \dots  \circ \tau_{1}$, ta có
$$\epsilon (\pi ) = (-1)^{m},$$
Mà chỉ ra rằng tính chẵn lẻ của số của các phép chuyển vị là bất biến.

*Chứng minh.* Giả sử rằng $\tau (i) = j$ và $\tau (j) = i$, ở đâu $i < j$. Có hai các trường hợp, tùy thuộc liệu $i$ và $j$ là trong cùng lớp tương đương (equivalence class) $J_{l}$ của $R_{\pi}$, hoặc nếu chúng là trong phân biệt các lớp tương đương. Nếu $i$ và $j$ là trong cùng lớp $J_{l}$, thì nếu
$$J_{l} = {i_{1}, \dots  , i_{p}, \dots  i_{q}, \dots  i_{k}},$$
Ở đâu $i_{p} = i$ và $i_{q} = j$, vì
$$\tau (\pi (\pi^{-1} (i_{p}))) = \tau (i_{p}) = \tau (i) = j = i_{q}$$
Và
$$\tau (\pi (i_{q-1})) = \tau (i_{q}) = \tau (j) = i = i_{p},$$
Rõ ràng là $J_{l}$ splits vào hai các tập con, một của mà là ${i_{p}, \dots  , i_{q-1}}$, và do đó, số của các lớp liên kết với $\tau  \circ \pi$ là $r + 1$, và $\epsilon (\tau  \circ \pi$) $= (-1)^{n-r-1} = -(-1)^{n-r} = -\epsilon (\pi$). Nếu $i$ và $j$ là trong phân biệt các lớp tương đương $J_{l}$ và $J_{m}$, nói
$${i_{1}, \dots  , i_{p}, \dots  i_{h}}$$
