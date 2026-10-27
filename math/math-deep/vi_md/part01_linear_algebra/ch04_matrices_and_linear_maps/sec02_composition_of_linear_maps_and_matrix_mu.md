# Hợp thành của Các ánh xạ tuyến tính (linear maps) và Phép nhân ma trận (matrix multiplication)


<!-- PAGE 130 -->
Điều này là được kỳ vọng bởi cơ bản định lý của vi tích phân vì đạo hàm của tích phân trả về hàm. Như ta sẽ một cách ngắn xem, ở trên ma trận tích tương ứng với điều này phiếm hàm hợp thành. phương trình $DS = I_{4}$ chỉ ra rằng $S$ là đơn ánh (injective) và có $D$ như nghịch đảo trái (left inverse). Tuy nhiên, SD $\neq  I_{5}$, và thay vì
$$\begin{pmatrix} 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 1/2 & 0 & 0 \\ 0 & 0 & 1/3 & 0 \\ 0 & 0 & 0 & 1/4 \end{pmatrix} \begin{pmatrix} 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 2 & 0 & 0 \\ 0 & 0 & 0 & 3 & 0 \\ 0 & 0 & 0 & 0 & 4 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix} ,$$
Bởi vì hằng số các đa thức (các đa thức của bậc $0)$ thuộc đến hạt nhân (kernel) của $D$.

## 4.2 Hợp thành của Các ánh xạ tuyến tính (linear maps) và Ma trận

$$Multiplication$$
Cho chúng ta bây giờ xét cách mà hợp thành của các ánh xạ tuyến tính (linear maps) được biểu diễn theo các cơ sở. Cho $E, F$, và $G$, là ba các vectơ các không gian với respective các cơ sở $(u_{1}, \dots  , u_{p})$ cho $E, (v_{1}, \dots  , v_{n})$ cho $F$, và $(w_{1}, \dots  , w_{m})$ cho $G$. Cho $g: E \to F$ và $f$: $F \to G$ là các ánh xạ tuyến tính (linear maps). Như được giải thích trước đó, $g: E \to F$ được xác định bởi các ảnh của cơ sở (basis) các vectơ $u_{j}$, và $f$: $F \to G$ được xác định bởi các ảnh của cơ sở (basis) các vectơ $v_{k}$. Ta sẽ like đến understand cách mà $f \circ g: E \to G$ được xác định bởi các ảnh của cơ sở (basis) các vectơ $u_{j}$.
Nhận xét: Lưu ý rằng ta là xét các ánh xạ tuyến tính (linear maps) $g: E \to F$ và $f$: $F \to G$, thay vì của $f$: $E \to F$ và $g: F \to G$, mà cho ta hợp thành $f \circ g: E \to G$ thay vì của $g \circ f$: $E \to G$. Của ta perhaps unusual lựa chọn là motivated bởi sự kiện rằng nếu $f$ được biểu diễn bởi ma trận M(f) $= (a_{i k})$ và $g$ được biểu diễn bởi ma trận M(g) $= (b_{k j})$, thì $f \circ g: E \to G$ được biểu diễn bởi tích $AB$ của các ma trận $A$ và $B$. Nếu ta đã có adopted khác lựa chọn ở đâu $f$: $E \to F$ và $g: F \to G$, thì $g \circ f$: $E \to G$ sẽ được biểu diễn bởi tích $BA$. Personally, ta tìm nó dễ hơn đến remember công thức cho phần tử (entry) trong Hàng $i$ và Cột $j$ của tích của hai các ma trận khi tích này được viết bởi AB, thay vì BA. Hiển nhiên, điều này là matter của taste! Ta sẽ có đến live với của ta perhaps unorthodox lựa chọn. Do đó, cho
$$f(v_{k}) = \sum_{i=1}^{m}  a_{i k}w_{i},$$
Với mọi $k, 1 \le k \le n$, và cho
$$g(u_{j}) = \sum_{k=1}^{n}  b_{k j}v_{k},$$

<!-- PAGE 131 -->
Với mọi $j, 1 \le j \le p$; trong ma trận tạo thành, ta có
$$f(v_{1})f(v_{2})\dots f(v_{n})$$
$$w_{1}$$
$$w_{2}\vdots \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{pmatrix}$$
$$w_{m}$$
Và
$$g(u_{1})g(u_{2})\dots g(u_{p})$$
$$v_{1}$$
$$v_{2}\vdots \begin{pmatrix} b_{11} & b_{12} & \dots & b_{1p} \\ b_{21} & b_{22} & \dots & b_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ b_{n1} & b_{n2} & \dots & b_{np} \end{pmatrix} .$$
$$v_{n}$$
Bởi trước đó considerations, với mọi
$$x = x_{1}u_{1} + \cdots  + x_{p}u_{p},$$
Đặt g(x) $= y = y_{1}v_{1} + \cdots  + y_{n}v_{n}$, ta có
$$y_{k} = \sum_{j=1}^{p}  b_{k j}x_{j}(2)$$
Với mọi $k, 1 \le k \le n$, và với mọi
$$y = y_{1}v_{1} + \cdots  + y_{n}v_{n},$$
Đặt f(y) $= z = z_{1}w_{1} + \cdots  + z_{m}w_{m}$, ta có
$$z_{i} = \sum_{k=1}^{n}  a_{i k}y_{k}(3)$$
Với mọi $i, 1 \le i \le m$. Thì nếu $y =$ g(x) và $z =$ f(y), ta có $z =$ f(g(x)), và xét theo $(2)$ và $(3)$, ta có
$$z_{i} = \sum_{k=1}^{n}  a_{i k}( \sum_{j=1}^{p}  b_{k j}x_{j})$$
$$= \sum_{k=1j}^{n}  \sum_{=1}^{p}  a_{i k}b_{k j}x_{j}$$
$$= \sum_{j=1}^{p}  \sum_{k=1}^{n}  a_{i k}b_{k j}x_{j}$$
$$= \sum_{j=1}^{p}  ( \sum_{k=1}^{n}  a_{i k}b_{k j})x_{j}.$$

<!-- PAGE 132 -->
Do đó, định nghĩa $c_{i j}$ sao cho
$$c_{i j} = \sum_{k=1}^{n}  a_{i k}b_{k j},$$
Cho $1 \le i \le m$, và $1 \le j \le p$, ta có
$$z_{i} = \sum_{j=1}^{p}  c_{i j}x_{j}(4)$$
Đồng nhất thức $(4)$ chỉ ra rằng hợp thành của các ánh xạ tuyến tính (linear maps) tương ứng với tích của các ma trận. Thì cho trước ánh xạ tuyến tính (linear map) $f$: $E \to F$ được biểu diễn bởi ma trận M(f) $= (a_{i j})$ w.r.t. các cơ sở $(u_{1}, \dots  , u_{n})$ và $(v_{1}, \dots  , v_{m})$, bởi Phương trình $(1)$, cụ thể là
$$y_{i} = \sum_{j=1}^{n}  a_{i j}x_{j}1 \le i \le m,$$
Và định nghĩa của phép nhân ma trận (matrix multiplication), phương trình $y =$ f(x) tương ứng với phương trình ma trận M(y) $=$ M(f)M(x), nghĩa là,
$$\begin{pmatrix} y_{1} \\ \vdots \\ y_{m} \end{pmatrix} = \begin{pmatrix} a_{1 1} & \dots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{m1} & \dots & a_{m n} \end{pmatrix} \begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix} .$$
Nhắc lại rằng
$$\begin{pmatrix} a_{1 1} & a_{1 2} & \dots & a_{1n} \\ a_{2 1} & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{m n} \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ \vdots \\ x_{n} \end{pmatrix} = x_{1} \begin{pmatrix} a_{1 1} \\ a_{2 1} \\ \vdots \\ a_{m1} \end{pmatrix} + x_{2} \begin{pmatrix} a_{1 2} \\ a_{2 2} \\ \vdots \\ a_{m2} \end{pmatrix} + \cdots  + x_{n} \begin{pmatrix} a_{1n} \\ a_{2n} \\ \vdots \\ a_{m n} \end{pmatrix} .$$
Đôi khi, nó là cần đến incorporate các cơ sở $(u_{1}, \dots  , u_{n})$ và $(v_{1}, \dots  , v_{m})$ trong ký hiệu cho ma trận M(f) biểu diễn $f$ đối với các phần tử này các cơ sở. Điều này hóa ra là phức tạp enterprise! Ta propose sau đây course của action:

> **Định nghĩa 4.2.** Viết $\mathcal{U} = (u_{1}, \dots  , u_{n})$ và $\mathcal{V} = (v_{1}, \dots  , v_{m})$ cho các cơ sở của $E$ và $F$, và ký hiệu bởi $M_{U,V}(f)$ ma trận của $f$ đối với các cơ sở $\mathcal{U}$ và $\mathcal{V}$. Hơn nữa, viết $x_{U}$ cho các tọa độ M(x) $= (x_{1}, \dots  , x_{n})$ của $x \in E$ w.r.t. cơ sở (basis) $\mathcal{U}$ và viết $y_{V}$ cho các tọa độ M(y) $= (y_{1}, \dots  , y_{m})$ của $y \in F$ w.r.t. cơ sở (basis) $\mathcal{V}$. Thì
$$y = f(x)$$

<!-- PAGE 133 -->
Được biểu diễn trong ma trận tạo thành bởi
$$y_{V} = M_{U,V}(f) x_{U}.$$
Khi $\mathcal{U} =\mathcal{V}$, ta abbreviate $M_{U,V}(f)$ như $M_{U}(f)$. ở trên ký hiệu dường như reasonable, nhưng nó có slight disadvantage rằng trong biểu thức $M_{U,V}(f)x_{U}$, input lập luận $x_{U}$ mà là fed đến ma trận $M_{U,V}(f)$ thực hiện không xuất hiện tiếp theo đến chỉ số dưới $\mathcal{U}$ trong $M_{U,V}(f)$. Ta có thể có được sử dụng ký hiệu $M_{V,U}(f)$, và một số people thực hiện rằng. Nhưng khi đó, ta tìm bit confusing $that\mathcal{V}$ đến $before\mathcal{U}$ khi $f$ các ánh xạ từ không gian $E$ với cơ sở (basis) $\mathcal{U}$ đến không gian $F$ với cơ sở (basis) $\mathcal{V}$. Do đó, ta ưu tiên để sử dụng ký hiệu $M_{U,V}(f)$. Là biết rằng khác các tác giả chẳng hạn như Meyer $[129]$ sử dụng ký hiệu $[f]_{U,V}$, và những cái khác chẳng hạn như Dummit và Foote $[55]$ sử dụng ký hiệu $M_{U}^{V}  (f)$, thay vì của $M_{U,V}(f)$. Điều này thu được tệ hơn! Bạn có thể tìm ký hiệu $M_{V}^{U}  (f)$ (như trong Lang $[113]), or_{U}[f]_{V}$, hoặc khác strange các ký hiệu. Định nghĩa 4.2 chỉ ra rằng hàm mà associates đến ánh xạ tuyến tính (linear map) $f$: $E \to F$ ma trận M(f) w.r.t. các cơ sở $(u_{1}, \dots  , u_{n})$ và $(v_{1}, \dots  , v_{m})$ có tính chất rằng phép nhân ma trận (matrix multiplication) tương ứng với hợp thành của các ánh xạ tuyến tính (linear maps). Điều này cho phép chúng ta đến transfer các tính chất của các ánh xạ tuyến tính (linear maps) đến các ma trận. Ở đây là illustration của điều này kỹ thuật:

> **Mệnh đề 4.1.** $(1)$ Cho trước bất kỳ các ma trận $A \in M_{m,n}(K), B \in M_{n,p}(K)$, và $C \in M_{p,q}(K)$, ta có
$$(AB)C = A(BC);$$
Rằng là, phép nhân ma trận (matrix multiplication) là kết hợp.
$(2)$ Cho trước bất kỳ các ma trận $A, B \in M_{m,n}(K)$, và $C, D \in M_{n,p}(K)$, với mọi $\lambda  \in K$, ta có
$$(A + B)C = AC + BC$$
$$A(C + D) = AC + AD$$
$$(\lambda A)C = \lambda (AC)$$
$$A(\lambda C) = \lambda (AC),$$
Sao cho phép nhân ma trận (matrix multiplication) $\cdot$: $M_{m,n}(K) \times  M_{n,p}(K) \to M_{m,p}(K)$ là song tuyến tính.

*Chứng minh.* $(1)$ Mọi $m \times  n$ ma trận $A = (a_{i j})$ định nghĩa hàm $f_{A}$: $K^{n} \to K^{m}$ cho trước bởi
$$f_{A}(x) = Ax,$$
Với mọi $x \in K^{n}$. Ta kiểm chứng được ngay rằng $f_{A}$ là tuyến tính và rằng ma trận $M(f_{A})$ biểu diễn $f_{A}$ trên chính tắc các cơ sở trong $K^{n}$ và $K^{m}$ bằng $A$. Thì Công thức $(4)$ chứng tỏ rằng
$$M(f_{A} \circ f_{B}) = M(f_{A})M(f_{B}) = AB,$$
Do đó ta thu được
$$M((f_{A} \circ f_{B}) \circ f_{C}) = M(f_{A} \circ f_{B})M(f_{C}) = (AB)C$$

<!-- PAGE 134 -->
Và
$$M(f_{A} \circ (f_{B} \circ f_{C})) = M(f_{A})M(f_{B} \circ f_{C}) = A(BC),$$
Và vì hợp thành của các hàm là kết hợp, ta có $(f_{A} \circ f_{B}) \circ f_{C} = f_{A} \circ (f_{B} \circ f_{C})$, mà suy ra rằng
$$(AB)C = A(BC).$$
$(2)$ Ta kiểm chứng được ngay rằng nếu $f_{1}, f_{2} \in Hom_{K}(E, F), A, B \in M_{m,n}(K), (u_{1}, \dots  , u_{n})$ là bất kỳ cơ sở (basis) của $E$, và $(v_{1}, \dots  , v_{m})$ là bất kỳ cơ sở (basis) của $F$, thì
$$M(f_{1} + f_{2}) = M(f_{1}) + M(f_{2})$$
$$f_{A+B} = f_{A} + f_{B}.$$
Thì ta có
$$(A + B)C = M(f_{A+B})M(f_{C})$$
$$= M(f_{A+B} \circ f_{C})$$
$$= M((f_{A} + f_{B}) \circ f_{C}))$$
$$= M((f_{A} \circ f_{C}) + (f_{B} \circ f_{C}))$$
$$= M(f_{A} \circ f_{C}) + M(f_{B} \circ f_{C})$$
$$= M(f_{A})M(f_{C}) + M(f_{B})M(f_{C})$$
$$= AC + BC.$$
Phương trình (C $+ D) = AC + AD$ được chứng minh trong đồng dạng cách thức, và cuối cùng hai các phương trình là dễ dàng được kiểm chứng. Ta có thể cũng có được kiểm chứng tất cả các đồng nhất thức bởi tạo ra ma trận các phép tính. Lưu ý rằng Mệnh đề 4.1 suy ra rằng không gian vectơ (vector space) $M_{n}(K)$ của các ma trận vuông là
(không giao hoán) vành với unit $I_{n}$. (Nó chẵn/ngay cả chỉ ra rằng $M_{n}(K)$ là kết hợp đại số.) sau đây mệnh đề phát biểu chính các tính chất của ánh xạ $f \mapsto$ M(f) giữa Hom(E, $F)$ và $M_{m,n}$. Trong ngắn, nó là đẳng cấu của các không gian vectơ.

> **Mệnh đề 4.2.** Cho trước ba các không gian vectơ $E, F, G$, với respective các cơ sở $(u_{1}, \dots  , u_{p}), (v_{1}, \dots  , v_{n})$, và $(w_{1}, \dots  , w_{m})$, ánh xạ $M$: Hom(E, $F) \to M_{n,p}$ rằng associates ma trận M(g) đến ánh xạ tuyến tính (linear map) $g: E \to F$ thỏa mãn các tính chất sau đây với mọi $x \in E$, tất cả $g, h: E \to F$, và tất cả $f$: $F \to G$:
$$M(g(x)) = M(g)M(x)$$
$$M(g + h) = M(g) + M(h)$$
$$M(\lambda g) = \lambda M(g)$$
$$M(f \circ g) = M(f)M(g),$$

<!-- PAGE 135 -->
Ở đâu M(x) là vectơ cột (column vector) liên kết với vectơ $x$ và M(g(x)) là vectơ cột (column vector) liên kết với g(x), như được giải thích trong Định nghĩa 4.1. Do đó, $M$: Hom(E, $F) \to M_{n,p}$ là đẳng cấu của các không gian vectơ, và khi $p = n$ và cơ sở (basis) $(v_{1}, \dots  , v_{n})$ là đồng nhất đến cơ sở (basis) $(u_{1}, \dots  , u_{p}), M$: Hom(E, $E) \to M_{n}$ là đẳng cấu của các vành.

*Chứng minh.* Rằng M(g(x)) $=$ M(g)M(x) đã được hiển thị theo Định nghĩa 4.2 hoặc tương đương bởi Công thức $(1)$. các đồng nhất thức M(g $+ h) =$ M(g) $+$ M(h) và $M(\lambda g) = \lambda$ M(g) là trực tiếp/dễ dàng, và M(f $\circ g) =$ M(f)M(g) suy ra từ Đồng nhất thức $(4)$ và định nghĩa của phép nhân ma trận (matrix multiplication). ánh xạ $M$: Hom(E, $F) \to M_{n,p}$ là rõ ràng đơn ánh (injective), và vì mọi ma trận định nghĩa ánh xạ tuyến tính (linear map) (xem Mệnh đề 4.1), nó là cũng toàn ánh (surjective), và do đó song ánh (bijective). Xét theo ở trên các đồng nhất thức, nó là đẳng cấu (và tương tự cho $M$: Hom(E, $E) \to M_{n}$, ở đâu Mệnh đề 4.1 được sử dụng để chỉ ra rằng $M_{n}$ là vành). Xét theo Mệnh đề 4.2, nó dường như được ưu tiên hơn để biểu diễn các vectơ từ không gian vectơ (vector space) của hữu hạn số chiều như các vectơ cột thay vì các vectơ hàng. Do đó, từ bây giờ trên, ta sẽ
$$\mathbb{R}^{n}$$
Ký hiệu các vectơ của (hoặc tổng quát hơn, của $K^{n})$ như các vectơ cột. Ta được giải thích trong Mục 3.9 rằng nếu không gian $E$ là hữu hạn chiều và có hữu hạn cơ sở (basis) $(u_{1}, \dots  , u_{n})$, thì dạng tuyến tính (linear form) $f^{*}$: $E \to K$ được biểu diễn bởi vectơ hàng (row vector) của các hệ số
$$\begin{pmatrix} f^{*}(u_{1}) & \cdots & f^{*}(u_{n}) \end{pmatrix} ,(1)$$
Trên các cơ sở $(u_{1}, \dots  , u_{n})$ và $1$ (trong $K)$, và rằng trên đối ngẫu (dual) cơ sở (basis) $(u_{1}^{*}, \dots  , u_{n}^{*})$ của $E^{*}$, dạng tuyến tính (linear form) $f^{*}$ được biểu diễn bởi cùng các hệ số, nhưng như vectơ cột (column vector)
$$\begin{pmatrix} f^{*}(u_{1}) \\ \vdots \\ f^{*}(u_{n}) \end{pmatrix} ,(2)$$
Mà là chuyển vị (transpose) của vectơ hàng (row vector) trong $(1)$. Điều này là đặc biệt trường hợp của nhiều hơn/thêm tổng quát hiện tượng. ánh xạ tuyến tính (linear map) $f$: $E \to F$ cảm sinh ánh xạ $f^{\top}$: $F^{*} \to E^{*}$ được gọi là chuyển vị (transpose) của $f$ (lưu ý rằng $f^{\top}$ các ánh xạ $F^{*}$ đến $E^{*}$, không $E^{*}$ đến $F^{*}$), và nếu $(u_{1} \dots  , u_{n})$ là cơ sở (basis) của $E, (v_{1} \dots  , v_{m})$ là cơ sở (basis) của $F$, và nếu $f$ được biểu diễn bởi ma trận cỡ $m \times  n$ $A$ trên các phần tử này các cơ sở, thì trên đối ngẫu (dual) các cơ sở $(v_{1}^{*}, \dots  , v_{m}^{*})$ và $(u_{1}^{*}, \dots  , u_{n}^{*})$, ánh xạ tuyến tính (linear map) $f^{\top}$ được biểu diễn bởi $A^{\top}$, chuyển vị (transpose) của ma trận $A$. Điều này là bởi vì trên cơ sở (basis) $(v_{1}, \dots  , v_{m})$, dạng tuyến tính (linear form) $\phi  \in F^{*}$ được biểu diễn bởi vectơ hàng (row vector)
$$\lambda  = \begin{pmatrix} \phi (v_{1}) & \cdots & \phi (v_{m}) \\ representedbythe \end{pmatrix} ,$$
Và ta định nghĩa $f^{\top} (\phi$) như dạng tuyến tính (linear form) vectơ hàng (row vector)
$$\lambda A$$
