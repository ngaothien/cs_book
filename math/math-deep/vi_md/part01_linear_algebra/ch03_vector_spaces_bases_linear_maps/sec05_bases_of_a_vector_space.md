# Các cơ sở của Không gian vectơ (vector space)


<!-- PAGE 86 -->
Nhận xét: khái niệm của tổ hợp tuyến tính (linear combination) có thể cũng được định nghĩa cho vô hạn chỉ số các tập hợp I.
$$To ensure that a sum \sum_{i}  \in I \lambda_{i} u_{i} makes sense, we restrict our attention to families of finite$$
Hỗ trợ/giá (support).

> **Định nghĩa 3.5.** Cho trước bất kỳ trường $K$, họ của các vô hướng $(\lambda_{i} )_{i\in I}$ có hữu hạn hỗ trợ/giá (support) nếu $\lambda_{i}  = 0$ với mọi $i \in$ I - $J$, với một số hữu hạn tập con $J$ của I. Nếu $(\lambda_{i} )_{i\in I}$ là họ của các vô hướng của hữu hạn hỗ trợ/giá (support), với mọi không gian vectơ (vector space) $E$ trên $K$, với mọi
$$(possibly infinite) family (u_{i})_{i\in I} of vectors u_{i} \in E, we define the linear combination \sum_{i}  \lambda_{i} u_{i}$$
$$as the finite linear combination \sum_{j}  \in  \lambda_{j} u_{j}, where J is any finite subset of I such that^{\in I} \lambda_{i}  = 0$$
Với mọi $i \in$ I - $J$. Nói chung, $results^{J}$ được phát biểu cho hữu hạn các họ cũng đúng cho các họ của hữu hạn hỗ trợ/giá (support).

## 3.5 Các cơ sở của Không gian vectơ (vector space)

Cho trước không gian vectơ (vector space) $E$, cho trước họ $(v_{i})_{i\in I}$, tập con $V$ của $E$ bao gồm của null vectơ $0$ và của tất cả các tổ hợp tuyến tính của $(v_{i})_{i\in I}$ là dễ dàng được thấy là không gian con của $E$. họ $(v_{i})_{i\in I}$ là economical cách của biểu diễn toàn bộ không gian con $V$, nhưng như vậy họ sẽ là chẵn/ngay cả nicer nếu nó đã là không redundant. Các không gian con có như vậy “efficient” họ sinh (generating family) (được gọi là cơ sở (basis)) đóng quan trọng vai trò và motivate sau đây định nghĩa.

> **Định nghĩa 3.6.** Cho trước không gian vectơ (vector space) $E$ và không gian con $V$ của $E$, họ $(v_{i})_{i\in I}$ của các vectơ $v_{i} \in V$ sinh ra $V$ hoặc sinh ra $V$ khi và chỉ khi với mọi $v \in V$, tồn tại một họ $(\lambda_{i} )_{i\in I}$ của các vô hướng trong $K$ sao cho
$$v = \sum_{i\in I}  \lambda_{i} v_{i}.$$
Ta cũng nói rằng các phần tử của $(v_{i})_{i\in I}$ là các phần tử sinh của $V$ và rằng $V$ được sinh (spanned) bởi $(v_{i})_{i\in I}$, hoặc được sinh bởi $(v_{i})_{i\in I}$. Nếu không gian con $V$ của $E$ được sinh bởi hữu hạn họ $(v_{i})_{i\in I}$, ta nói rằng $V$ là sinh hữu hạn (finitely generated). họ $(u_{i})_{i\in I}$ rằng sinh ra $V$ và là độc lập tuyến tính (linearly independent) được gọi là một cơ sở (basis) của $V$.

> **Ví dụ 3.4.** $1. In\mathbb{R}^{3}$, các vectơ $(1, 0, 0), (0, 1, 0)$, và $(0, 0, 1)$, được minh họa trong Hình 3.9, tạo thành cơ sở (basis).
$$\mathbb{R}^{4}$$
$2$. các vectơ $(1, 1, 1, 1), (1, 1, -1, -1), (1, -1, 0, 0), (0, 0, 1, -1)$ tạo thành cơ sở (basis) của đã biết như Cơ sở Haar (Haar basis). cơ sở (cơ sở (basis)) này và của nó tổng quát hóa đến số chiều $2^{n}$ là then chốt trong wavelet lý thuyết. $3$. Trong không gian con của các đa thức trong $\mathbb{R}[X]$ của bậc nhiều nhất $n$, các đa thức $1, X, X^{2}, \dots  , X^{n}$ tạo thành cơ sở (basis).
$$4. The Bernstein polynomials \begin{pmatrix} n \\ k \end{pmatrix} (1 -X)^{n-k}X^{k}for k = 0, \dots  , n, also form a basis of$$
Rằng không gian. các đa thức này đóng major vai trò trong lý thuyết của spline các đường cong.

<!-- PAGE 87 -->
Thứ nhất then chốt kết quả của tuyến tính đại số là rằng mọi không gian vectơ (vector space) $E$ có cơ sở (basis). Ta bắt đầu với then chốt bổ đề mà formalizes mechanism cho xây dựng cơ sở (basis) incrementally.

> **Bổ đề 3.7.** Cho trước độc lập tuyến tính (linearly independent) họ $(u_{i})_{i\in I}$ của các phần tử của không gian vectơ (vector space) $E$, nếu $v \in E$ là không tổ hợp tuyến tính (linear combination) của $(u_{i})_{i\in I}$, thì họ $(u_{i})_{i\in I} \cup_{k}  (v)$ thu được bằng cách cộng $v$ đến họ $(u_{i})_{i\in I}$ là độc lập tuyến tính (linearly independent) (ở đâu $k \in /$ I).
$$Proof. Assume that \mu v + \sum_{i}  \lambda_{i} u_{i} = 0, for any family (\lambda_{i} )_{i\in I} of scalars in K. If \mu  \neq  0, then$$
$$\mu  has an inverse (because^{\in I} K is a field), and thus we have v = - \sum_{i}  \in I(\mu^{-1} \lambda_{i} )u_{i}, showing$$
Rằng $v$ là tổ hợp tuyến tính (linear combination) của $(u_{i})_{i\in I}$ và contradicting giả thiết. Do đó, $\mu  = 0$. Nhưng
$$then, we have \sum_{i}  \lambda_{i} u_{i} = 0, and since the family (u_{i})_{i\in I} is linearly independent, we have$$
$\lambda_{i}  = 0$ với mọi $i \in I^{\in I}$. tiếp theo định lý nghiệm đúng nói chung, nhưng chứng minh là nhiều hơn/thêm sophisticated cho các không gian vectơ rằng thực hiện không có hữu hạn tập hợp của các phần tử sinh. Do đó, trong chương này, ta chỉ chứng minh định lý cho sinh hữu hạn (finitely generated) các không gian vectơ.

> **Định lý 3.8.** Cho trước bất kỳ hữu hạn họ $S = (u_{i})_{i\in I}$ sinh không gian vectơ (vector space) $E$ và bất kỳ độc lập tuyến tính (linearly independent) họ con $L = (u_{j})_{j\in J}$ của $S$ (ở đâu $J \subseteq$ I), có một cơ sở (basis) $B$ của $E$ sao cho $L \subseteq B \subseteq S$.

*Chứng minh.* Xét tập hợp của độc lập tuyến tính (linearly independent) các họ $B$ sao cho $L \subseteq B \subseteq S$. Vì tập hợp này là khác rỗng và hữu hạn, nó có một số cực đại phần tử (rằng là, họ con $B = (u_{h})_{h\in H}$ của $S$ với $H \subseteq$ I của cực đại cardinality), nói $B = (u_{h})_{h\in H}$. Ta khẳng định rằng $B$ sinh ra $E$. Thật vậy, nếu $B$ thực hiện không sinh $E$, thì tồn tại một $u_{p} \in S$ rằng là không tổ hợp tuyến tính (linear combination) của các vectơ trong $B$ (vì $S$ sinh ra $E)$, với $p \in / H$. Thì theo Bổ đề 3.7, họ B' $= (u_{h})_{h\in H\cup {p}}$ là độc lập tuyến tính (linearly independent), và vì $L \subseteq B \subset$ B' $\subseteq S$, điều này contradicts maximality của $B$. Do đó, $B$ là cơ sở (basis) của $E$ sao cho $L \subseteq B \subseteq S$.
Nhận xét: Định lý 3.8 cũng nghiệm đúng cho các không gian vectơ rằng là không sinh hữu hạn (finitely generated). Trong trường hợp này, bài toán là để đảm bảo sự tồn tại của cực đại độc lập tuyến tính (linearly independent) họ $B$ sao cho $L \subseteq B \subseteq S$. sự tồn tại của như vậy cực đại họ có thể được được hiển thị bằng cách sử dụng Zorn’s bổ đề, xem Phụ lục $C$ và references cho trước ở đó. tình huống ở đâu đầy đủ generality của Định lý 3.8 là cần thiết là trường hợp của vectơ
$$\sqrt$$
Không gian $\mathbb{R}$ trên trường của các hệ số $\mathbb{Q}$. các số $1$ và $\overline{2}$ là độc lập tuyến tính (linearly independent)
$$\sqrt$$
Trên $\mathbb{Q}$, do đó theo Định lý 3.8, độc lập tuyến tính (linearly independent) họ $L = (1, \overline{2)}$ có thể được được mở rộng đến cơ sở (basis) $B$ của $\mathbb{R}$. Vì $\mathbb{R}$ là uncountable và $\mathbb{Q}$ là đếm được, như vậy cơ sở (basis) phải là uncountable! khái niệm của cơ sở (basis) có thể cũng được định nghĩa theo khái niệm của cực đại độc lập tuyến tính (linearly independent) họ và tối tiểu họ sinh (generating family).

<!-- PAGE 88 -->

> **Định nghĩa 3.7.** Cho $(v_{i})_{i\in I}$ là họ của các vectơ trong không gian vectơ (vector space) $E$. Ta nói rằng $(v_{i})_{i\in I}$ cực đại độc lập tuyến tính (linearly independent) họ của $E$ nếu nó là độc lập tuyến tính (linearly independent), và nếu với mọi vectơ $w \in E$, họ $(v_{i})_{i\in I} \cup_{k}  {w}$ thu được bằng cách cộng $w$ đến họ $(v_{i})_{i\in I}$ là phụ thuộc tuyến tính (linearly dependent). Ta nói rằng $(v_{i})_{i\in I}$ tối tiểu họ sinh (generating family) của $E$ nếu nó sinh ra $E$, và nếu với mọi chỉ số $p \in$ I, họ $(v_{i})_{i\in I-{p}}$ thu được bởi removing $v_{p}$ từ họ $(v_{i})_{i\in I}$ thực hiện không sinh (span) $E$. sau đây mệnh đề cho hữu ích các tính chất đặc trưng hóa cơ sở (basis) là immediate hệ quả của Bổ đề 3.7.

> **Mệnh đề 3.9.** Cho trước không gian vectơ (vector space) $E$, với mọi họ $B = (v_{i})_{i\in I}$ của các vectơ của $E$, các tính chất sau đây là tương đương:
$(1) B$ là cơ sở (basis) của $E$.
$(2) B$ là cực đại độc lập tuyến tính (linearly independent) họ của $E$.
$(3) B$ là tối tiểu họ sinh (generating family) của $E$.

*Chứng minh.* Ta sẽ thứ nhất chứng minh equivalence của $(1)$ và $(2)$. Giả sử $(1)$. Vì $B$ là cơ sở (basis), nó là độc lập tuyến tính (linearly independent) họ. Ta khẳng định rằng $B$ là cực đại độc lập tuyến tính (linearly independent) họ. Nếu $B$ là không cực đại độc lập tuyến tính (linearly independent) họ, thì tồn tại một vectơ $w \in E$ sao cho họ B' thu được bằng cách cộng $w$ đến $B$ là độc lập tuyến tính (linearly independent). Tuy nhiên, vì $B$ là cơ sở (basis) của $E$, vectơ $w$ có thể được biểu diễn dưới dạng tổ hợp tuyến tính (linear combination) của các vectơ trong $B$, contradicting sự kiện rằng B' là độc lập tuyến tính (linearly independent). Ngược lại, giả sử $(2)$. Ta khẳng định rằng $B$ sinh ra $E$. Nếu $B$ thực hiện không sinh (span) $E$, thì tồn tại một vectơ $w \in E$ mà là không tổ hợp tuyến tính (linear combination) của các vectơ trong $B$. Theo Bổ đề 3.7, họ B' thu được bằng cách cộng $w$ đến $B$ là độc lập tuyến tính (linearly independent). Vì $B$ là thực sự/đúng đắn họ con của B', điều này contradicts giả định rằng $B$ là cực đại độc lập tuyến tính (linearly independent) họ. Vì vậy, $B$ phải sinh (span) $E$, và vì $B$ là cũng độc lập tuyến tính (linearly independent), nó là cơ sở (basis) của $E$. Bây giờ ta sẽ chứng minh equivalence của $(1)$ và $(3)$. Một lần nữa, giả sử $(1)$. Vì $B$ là cơ sở (basis), nó là họ sinh (generating family) của $E$. Ta khẳng định rằng $B$ là tối tiểu họ sinh (generating family). Nếu $B$ là không tối tiểu họ sinh (generating family), thì có một thực sự/đúng đắn họ con B' của $B$ rằng sinh ra $E$. Thì, mọi $w \in B$ -B' có thể được biểu diễn dưới dạng tổ hợp tuyến tính (linear combination) của các vectơ từ B', contradicting sự kiện rằng $B$ là độc lập tuyến tính (linearly independent). Ngược lại, giả sử $(3)$. Ta khẳng định rằng $B$ là độc lập tuyến tính (linearly independent). Nếu $B$ là không độc lập tuyến tính (linearly independent), thì một số vectơ $w \in B$ có thể được biểu diễn dưới dạng tổ hợp tuyến tính (linear combination) của các vectơ trong B' $= B -{w}$. Vì $B$ sinh ra $E$, họ B' cũng sinh ra $E$, nhưng B' là thực sự/đúng đắn họ con của $B$, contradicting minimality của $B$. Vì $B$ sinh ra $E$ và là độc lập tuyến tính (linearly independent), nó là cơ sở (basis) của $E$. thứ hai then chốt kết quả của tuyến tính đại số là rằng với mọi hai các cơ sở $(u_{i})_{i\in I}$ và $(v_{j})_{j\in J}$ của không gian vectơ (vector space) $E$, chỉ số các tập hợp I và $J$ có cùng cardinality. Đặc biệt, nếu $E$ có

<!-- PAGE 89 -->
Hữu hạn cơ sở (basis) của $n$ các phần tử, mọi cơ sở (basis) của $E$ có $n$ các phần tử, và số nguyên $n$ được gọi là số chiều của không gian vectơ (vector space) $E$. để chứng minh thứ hai then chốt kết quả, ta có thể sử dụng sau đây replacement bổ đề do Steinitz. kết quả này chỉ ra relationship giữa hữu hạn độc lập tuyến tính (linearly independent) các họ và hữu hạn các họ của các phần tử sinh của không gian vectơ (vector space). Ta bắt đầu với phiên bản của bổ đề mà là bit informal, nhưng dễ hơn đến understand hơn precise và nhiều hơn/thêm hình thức formulation cho trước trong Mệnh đề 3.11. technical difficulty có đến thực hiện với sự kiện rằng một số của các chỉ số cần là renamed.

> **Mệnh đề 3.10.** (Replacement bổ đề, phiên bản $1)$ Cho trước không gian vectơ (vector space) $E$, cho $(u_{1}, \dots  , u_{m})$ là bất kỳ hữu hạn độc lập tuyến tính (linearly independent) họ trong $E$, và cho $(v_{1}, \dots  , v_{n})$ là bất kỳ hữu hạn họ sao cho mọi $u_{i}$ là tổ hợp tuyến tính (linear combination) của $(v_{1}, \dots  , v_{n})$. Thì ta phải có $m \le n$, và có một replacement của $m$ của các vectơ $v_{j}$ bởi $(u_{1}, \dots  , u_{m})$, sao cho sau renaming một số của các chỉ số của $v_{j}s$, các họ $(u_{1}, \dots  , u_{m}, v_{m+1}, \dots  , v_{n})$ và $(v_{1}, \dots  , v_{n})$ sinh cùng không gian con của $E$.

*Chứng minh.* Ta tiến hành bằng quy nạp theo $m$. Khi $m = 0$, họ $(u_{1}, \dots  , u_{m})$ là rỗng, và mệnh đề nghiệm đúng một cách tầm thường. Cho quy nạp bước, ta có độc lập tuyến tính (linearly independent) họ $(u_{1}, \dots  , u_{m}, u_{m+1})$. Xét độc lập tuyến tính (linearly independent) họ $(u_{1}, \dots  , u_{m})$. Theo giả thiết quy nạp, $m \le n$, và có một replacement của $m$ của các vectơ $v_{j}$ bởi $(u_{1}, \dots  , u_{m})$, sao cho sau renaming một số của các chỉ số của vs, các họ $(u_{1}, \dots  , u_{m}, v_{m+1}, \dots  , v_{n})$ và $(v_{1}, \dots  , v_{n})$ sinh cùng không gian con của $E$. vectơ $u_{m+1}$ có thể cũng được biểu diễn như tổ hợp tuyến tính (linear combination) của $(v_{1}, \dots  , v_{n})$, và vì $(u_{1}, \dots  , u_{m}, v_{m+1}, \dots  , v_{n})$ và $(v_{1}, \dots  , v_{n})$ sinh cùng không gian con, $u_{m+1}$ có thể được biểu diễn dưới dạng tổ hợp tuyến tính (linear combination) của $(u_{1}, \dots  , u_{m}, v_{m+1}, \dots , v_{n})$, nói
$$u_{m+1} = \sum_{i=1}^{m}  \lambda_{i} u_{i} + \sum_{j=m+1}^{n}  \lambda_{j} v_{j}.$$
Ta khẳng định rằng $\lambda_{j}  \neq  0$ với một số $j$ với $m + 1 \le j \le n$, mà suy ra rằng $m + 1 \le n$. Ngược lại, ta sẽ có
$$u_{m+1} = \sum_{i=1}^{m}  \lambda_{i} u_{i},$$
Không tầm thường sự phụ thuộc tuyến tính (linear dependence) của $u_{i}$, mà là không thể vì $(u_{1}, \dots  , u_{m+1})$ là độc lập tuyến tính (linearly independent). Vì vậy, $m + 1 \le n$, và sau renaming các chỉ số nếu cần, ta có thể giả sử rằng $\lambda_{m+1}  \neq  0$, do đó ta thu được
$$v_{m+1} = - \sum_{i=1}^{m}  (\lambda_{m+1}^{-1} \lambda_{i} )u_{i} -\lambda_{m+1}^{-1} u_{m+1} - \sum_{j=m+2}^{n}  (\lambda_{m+1}^{-1} \lambda_{j} )v_{j}.$$
Nhận thấy rằng các họ $(u_{1}, \dots  , u_{m}, v_{m+1}, \dots  , v_{n})$ và $(u_{1}, \dots  , u_{m+1}, v_{m+2}, \dots  , v_{n})$ sinh cùng không gian con, vì $u_{m+1}$ là tổ hợp tuyến tính (linear combination) của $(u_{1}, \dots  , u_{m}, v_{m+1}, \dots  , v_{n})$ và $v_{m+1}$

<!-- PAGE 90 -->
Là tổ hợp tuyến tính (linear combination) của $(u_{1}, \dots  , u_{m+1}, v_{m+2}, \dots  , v_{n})$. Vì $(u_{1}, \dots  , u_{m}, v_{m+1}, \dots  , v_{n})$ và $(v_{1}, \dots  , v_{n})$ sinh cùng không gian con, ta kết luận rằng $(u_{1}, \dots  , u_{m+1}, v_{m+2}, \dots  , v_{n})$ và và $(v_{1}, \dots  , v_{n})$ sinh cùng không gian con, mà kết luận giả thiết quy nạp (induction hypothesis). Đây là một ví dụ minh họa replacement bổ đề. Xét các dãy $(u_{1}, u_{2}, u_{3})$ và $(v_{1}, v_{2}, v_{3}, v_{4}, v_{5})$, ở đâu $(u_{1}, u_{2}, u_{3})$ là độc lập tuyến tính (linearly independent) họ và với $u_{i}s$ được biểu diễn theo $v_{j}s$ như sau:
$$u_{1} = v_{4} + v_{5}$$
$$u_{2} = v_{3} + v_{4} -v_{5}$$
$$u_{3} = v_{1} + v_{2} + v_{3}.$$
Từ phương trình thứ nhất ta thu được
$$v_{4} = u_{1} -v_{5},$$
Và bằng cách thế trong phương trình thứ hai ta có
$$u_{2} = v_{3} + v_{4} -v_{5} = v_{3} + u_{1} -v_{5} -v_{5} = u_{1} + v_{3} -2v_{5}.$$
Từ ở trên phương trình ta thu được
$$v_{3} = -u_{1} + u_{2} + 2v_{5},$$
Và do đó
$$u_{3} = v_{1} + v_{2} + v_{3} = v_{1} + v_{2} -u_{1} + u_{2} + 2v_{5}.$$
Cuối cùng, ta thu được
$$v_{1} = u_{1} -u_{2} + u_{3} -v_{2} -2v_{5}$$
Vì vậy ta có
$$v_{1} = u_{1} -u_{2} + u_{3} -v_{2} -2v_{5}$$
$$v_{3} = -u_{1} + u_{2} + 2v_{5}$$
$$v_{4} = u_{1} -v_{5},$$
Mà chỉ ra rằng $(u_{1}, u_{2}, u_{3}, v_{2}, v_{5})$ sinh ra cùng không gian con như $(v_{1}, v_{2}, v_{3}, v_{4}, v_{5})$. các vectơ $(v_{1}, v_{3}, v_{4})$ có đã được được thay thế bởi $(u_{1}, u_{2}, u_{3})$, và các vectơ trái trên là $(v_{2}, v_{5})$. Ta có thể rename chúng $(v_{4}, v_{5})$. Cho sake của tính đầy đủ, ở đây là nhiều hơn/thêm hình thức phát biểu của replacement bổ đề (và chứng minh của nó).

> **Mệnh đề 3.11.** (Replacement bổ đề, phiên bản $2)$ Cho trước không gian vectơ (vector space) $E$, cho $(u_{i})_{i\in I}$ là bất kỳ hữu hạn độc lập tuyến tính (linearly independent) họ trong $E$, ở đâu |I| $= m$, và cho $(v_{j})_{j\in J}$ là bất kỳ hữu hạn họ sao cho mọi $u_{i}$ là tổ hợp tuyến tính (linear combination) của $(v_{j})_{j\in J}$, ở đâu |J| $= n$. Thì tồn tại một tập hợp $L$ và đơn ánh $\rho$: $L \to J$ (relabeling hàm) sao cho $L \cap I = \emptyset$, |L| $= n$ - $m$, và các họ $(u_{i})_{i\in I} \cup (v_{\rho(l)})_{l\in L}$ và $(v_{j})_{j\in J}$ sinh cùng không gian con của $E$. Đặc biệt, $m \le n$.

<!-- PAGE 91 -->

*Chứng minh.* Ta tiến hành bằng quy nạp theo |I| $= m$. Khi $m = 0$, họ $(u_{i})_{i\in I}$ là rỗng, và mệnh đề nghiệm đúng một cách tầm thường với $L = J (\rho$ là đồng nhất thức). Giả sử |I| $= m + 1$. Xét độc lập tuyến tính (linearly independent) họ $(u_{i})_{i\in(I-{p})}$, ở đâu $p$ là bất kỳ member của I. Theo giả thiết quy nạp, tồn tại một tập hợp $L$ và đơn ánh $\rho$: $L \to J$ sao cho $L \cap$ (I $-{p}) = \emptyset$, |L| $=$ n-m, và các họ $(u_{i})_{i\in(I-{p})} \cup (v_{\rho(l)})_{l\in L}$ và $(v_{j})_{j\in J}$ sinh cùng không gian con của $E$. Nếu $p \in L$, ta có thể thay thế $L$ bởi $(L -{p}) \cup {p'}$ ở đâu p' thực hiện không thuộc đến I $\cup L$, và thay thế $\rho$ bởi đơn ánh $\rho'$ mà agrees với $\rho$ trên $L -{p}$ và sao cho $\rho'$ (p') $= \rho (p)$. Do đó, ta có thể luôn luôn giả sử rằng $L \cap I = \emptyset$. Vì $u_{p}$ là tổ hợp tuyến tính (linear combination) của $(v_{j})_{j\in J}$ và các họ $(u_{i})_{i\in(I-{p})} \cup (v_{\rho(l)})_{l\in L}$ và $(v_{j})_{j\in J}$ sinh cùng không gian con của $E, u_{p}$ là tổ hợp tuyến tính (linear combination) của $(u_{i})_{i\in(I-{p})} \cup (v_{\rho(l)})_{l\in L}$. Cho
$$u_{p} = \sum_{(I-{p}  \lambda_{i} u_{i} + \sum_{l\in L}  \lambda_{l} v_{\rho(l)}.(1)$$
$$i\in })$$
Nếu $\lambda_{l}  = 0$ với mọi $l \in L$, ta có
$$\sum_{(I-{p}  \lambda_{i} u_{i} -u_{p} = 0,$$
$$i\in })$$
Contradicting sự kiện rằng $(u_{i})_{i\in I}$ là độc lập tuyến tính (linearly independent). Do đó, $\lambda_{l}  \neq  0$ với một số $l \in L$, nói $l = q$. Vì $\lambda_{q}  \neq  0$, ta có
$$v_{\rho(q)} = \sum_{(I-{p}  (-\lambda_{q}^{-1}  \lambda_{i} )u_{i} + \lambda_{q}^{-1}  u_{p} + \sum_{(L-{q}  (-\lambda_{q}^{-1}  \lambda_{l} )v_{\rho(l)}.(2)$$
$$i\in })l\in })$$
Ta khẳng định rằng các họ $(u_{i})_{i\in(I-{p})} \cup (v_{\rho(l)})_{l\in L}$ và $(u_{i})_{i\in I} \cup (v_{\rho(l)})_{l\in(L-{q})}$ sinh cùng tập con của $E$. Thật vậy, thứ hai họ là thu được từ thứ nhất bằng cách thay thế $v_{\rho(q)}$ bởi $u_{p}$, và vice-versa, và $u_{p}$ là tổ hợp tuyến tính (linear combination) của $(u_{i})_{i\in(I-{p})} \cup (v_{\rho(l)})_{l\in L}$, bởi $(1)$, và $v_{\rho(q)}$ là tổ hợp tuyến tính (linear combination) của $(u_{i})_{i\in I}\cup (v_{\rho(l)})_{l\in(L-{q})}$, bởi $(2)$. Do đó, các họ $(u_{i})_{i\in I}\cup (v_{\rho(l)})_{l\in(L-{q})}$ và $(v_{j})_{j\in J}$ sinh cùng không gian con của $E$, và mệnh đề nghiệm đúng cho $L -{q}$ và thu hẹp của đơn ánh $\rho$: $L \to J$ đến $L -{q}$, vì $L \cap I = \emptyset$ và |L| $= n -m$ suy ra rằng $(L -{q}) \cap I = \emptyset$ và |L $-{q}| = n$ - $(m + 1)$. ý tưởng là rằng $m$ của các vectơ $v_{j}$ có thể được được thay thế bởi độc lập tuyến tính (linearly independent) $u_{i}s$ trong như vậy cách rằng cùng không gian con là vẫn được sinh. mục đích của hàm $\rho$: $L \to J$ là đến chọn $n$ - $m$ các phần tử $j_{1}, \dots  , j_{n-m}$ của $J$ và đến relabel chúng $l_{1}, \dots  , l_{n-m}$ trong như vậy cách rằng các phần tử này mới các chỉ số thực hiện không clash với các chỉ số trong I; điều này cách, các vectơ $v_{j1}, \dots  , v_{jn-m}$ ai “survive” (i.e. là không được thay thế) là relabeled $v_{l1}, \dots  , v_{ln-m}$, và khác $m$ các vectơ $v_{j}$ với $j \in J -{j_{1}, \dots  , j_{n-m}}$ được thay thế bởi $u_{i}$. chỉ số tập hợp của điều này mới họ là I $\cup L$. Thực sự, một có thể chứng minh rằng Mệnh đề 3.11 suy ra Định lý 3.8 khi không gian vectơ (vector space) là sinh hữu hạn (finitely generated). Đặt Định lý 3.8 và Mệnh đề 3.11 cùng nhau, ta thu được kết quả sau cơ bản định lý.

<!-- PAGE 92 -->

> **Định lý 3.12.** (Cơ bản định lý về các cơ sở) Cho $E$ là sinh hữu hạn (finitely generated) không gian vectơ (vector space).
$(1)$ Bất kỳ họ $(u_{i})_{i\in I}$ sinh $E$ chứa họ con $(u_{j})_{j\in J}$ mà là cơ sở (basis) của $E$.
$(2)$ Bất kỳ độc lập tuyến tính (linearly independent) họ $(u_{i})_{i\in I}$ có thể được được mở rộng đến họ $(u_{j})_{j\in J}$ mà là cơ sở (basis) của $E$ (với $I \subseteq J)$.
$(3)$ Hơn nữa, với mọi hai các cơ sở $(u_{i})_{i\in I}$ và $(v_{j})_{j\in J}$ của $E$, ta có |I| $=$ |J| $= n$ với một số cố định số nguyên $n \ge 0$.

*Chứng minh.* phần thứ nhất suy ra ngay lập tức bằng cách áp dụng Định lý 3.8 với $L = \emptyset$ và $S = (u_{i})_{i\in I}$. Cho phần thứ hai, xét họ S' $= (u_{i})_{i\in I} \cup (v_{h})_{h\in H}$, ở đâu $(v_{h})_{h\in H}$ là bất kỳ sinh hữu hạn (finitely generated) họ sinh $E$, và với I $\cap H = \emptyset$. Thì áp dụng Định lý 3.8 đến $L = (u_{i})_{i\in I}$ và đến S'. Cho cuối cùng phát biểu, giả sử rằng $(u_{i})_{i\in I}$ và $(v_{j})_{j\in J}$ là các cơ sở của $E$. Vì $(u_{i})_{i\in I}$ là độc lập tuyến tính (linearly independent) và $(v_{j})_{j\in J}$ sinh ra $E$, Mệnh đề 3.11 suy ra rằng |I| $\le$ |J|. đối xứng lập luận cho ta |J| $\le$ |I|.
Nhận xét: Định lý 3.12 cũng nghiệm đúng cho các không gian vectơ rằng là không sinh hữu hạn (finitely generated). Điều này có thể được được hiển thị như sau. Cho $(u_{i})_{i\in I}$ là cơ sở (basis) của $E$, cho $(v_{j})_{j\in J}$ là họ sinh (generating family) của $E$, và giả sử rằng I là vô hạn. Với mọi $j \in J$, cho $L_{j} \subseteq$ I là hữu hạn tập hợp
$$L_{j} = {i \in I | v_{j} = \sum_{i\in I}  \lambda_{i} u_{i}, \lambda_{i}  \neq  0}.$$
$$Let L = \bigcup_{j}  \in J L_{j}. By definition L \subseteq I, and since (u_{i})_{i\in I} is a basis of E, we must have I = L,$$
Vì ngược lại $(u_{i})_{i\in L}$ sẽ là một cái khác cơ sở (basis) của $E$, và điều này sẽ contradict sự kiện rằng $(u_{i})_{i\in I}$ là độc lập tuyến tính (linearly independent). Hơn nữa, $J$ phải là vô hạn, vì ngược lại, bởi vì
$$the L_{j} are finite, I would be finite. But then, since I = \bigcup_{jj\in jJ}  L_{j} with J infinite and the L_{j}$$
Hữu hạn, bởi tiêu chuẩn kết quả của tập hợp lý thuyết, |I| $\le$ |J|. Nếu $(v )^{\in J}$ là cũng cơ sở (basis), bởi đối xứng lập luận, ta thu được |J| $\le$ |I|, và do đó, |I| $=$ |J| với mọi hai các cơ sở $(u_{i})_{i\in I}$ và $(v_{j})_{j\in J}$ của $E$.

> **Định nghĩa 3.8.** Khi không gian vectơ (vector space) $E$ là không sinh hữu hạn (finitely generated), ta nói rằng $E$ là của vô hạn số chiều. số chiều của sinh hữu hạn (finitely generated) không gian vectơ (vector space) $E$ là chung/phổ biến số chiều $n$ của tất cả của của nó các cơ sở và được ký hiệu bởi dim(E). Rõ ràng, nếu trường $K$ chính nó được quan điểm như không gian vectơ (vector space), thì mọi họ () ở đâu $a \in K$ và $a \neq  0$ là cơ sở (basis). Do đó dim(K) $= 1$. Lưu ý rằng $dim({0}) = 0$. sau đây hữu ích hệ quả của Mệnh đề 3.11 và Định lý 3.12 được sử dụng nhiều.

> **Mệnh đề 3.13.** Cho $E$ là không gian vectơ (vector space) của hữu hạn số chiều $n$ (trên trường $K)$. Các tính chất sau đây đúng.
$(1)$ Nếu $m > n$, bất kỳ họ $(v_{1}, \dots  , v_{m})$ của $m$ các vectơ là phụ thuộc tuyến tính (linearly dependent).

<!-- PAGE 93 -->
$(2)$ Nếu $m < n$, bất kỳ họ $(v_{1}, \dots  , v_{m})$ của $m$ các vectơ thực hiện không sinh (span) $E$.
$(3)$ Bất kỳ độc lập tuyến tính (linearly independent) họ $(v_{1}, \dots  , v_{n})$ của $n$ các vectơ là cơ sở (basis) của $E$.
$(4)$ Bất kỳ sinh họ $(v_{1}, \dots  , v_{n})$ của $n$ các vectơ là cơ sở (basis) của $E$.

*Chứng minh.* chứng minh của (1)-(4) tiến hành bởi mâu thuẫn. Thứ nhất, theo Định lý 3.12, không gian $E$ có một số cơ sở (basis) $(u_{1}, \dots  , u_{n})$.
$(1)$ Ta áp dụng replacement bổ đề (Mệnh đề 3.11) nhưng beware rằng các vai trò của $u_{i}$ và $v_{j}$ là switched. Mỗi vectơ $v_{i}$ có thể được biểu diễn dưới dạng tổ hợp tuyến tính (linear combination) của $(u_{1}, \dots  , u_{n})$. Nếu họ $(v_{1}, \dots  , v_{m})$ là độc lập tuyến tính (linearly independent), vì $m > n$, ta có một mâu thuẫn đến Mệnh đề 3.11.
$(2)$ Nếu họ $(v_{1}, \dots  , v_{m})$ sinh ra $E$, mỗi $u_{i}$ có thể được biểu diễn dưới dạng tổ hợp tuyến tính (linear combination) của $(v_{1}, \dots  , v_{m})$. Nhưng $(u_{1}, \dots  , u_{n})$ là độc lập tuyến tính (linearly independent) họ và $n > m$, contradicting

> **Mệnh đề 3.11.**
$(3)$ Ta áp dụng replacement bổ đề (Mệnh đề 3.11) với các vai trò của $u_{i}$ và $v_{j}$ switched và $m = n$. Mỗi $v_{i}$ là tổ hợp tuyến tính (linear combination) của $(u_{1}, \dots  , u_{n})$ và vì họ $(v_{1}, \dots  , v_{n})$ là độc lập tuyến tính (linearly independent), theo Mệnh đề 3.11, tất cả $u_{j}$ được thay thế bởi $v_{i}$ và chúng sinh (span) cùng không gian, cụ thể là $E$. Một cái khác chứng minh đi như sau. Nếu độc lập tuyến tính (linearly independent) họ $(v_{1}, \dots  , v_{n})$ thực hiện không sinh (span) $E$, theo Định lý 3.12, nó có thể được được mở rộng đến cơ sở (basis) với chặt nhiều hơn $n$ các vectơ, contradicting Định lý 3.12 (và $(1))$.
$(4)$ Nếu họ $(v_{1}, \dots  , v_{n})$ sinh ra $E$ nhưng là không độc lập tuyến tính (linearly independent), thì thực sự/đúng đắn họ con với $m < n$ các vectơ sinh ra $E$. Điều này contradicts $(2)$. Một cái khác chứng minh đi như sau. Nếu họ $(v_{1}, \dots  , v_{n})$ sinh ra $E$ nhưng là không độc lập tuyến tính (linearly independent), theo Định lý 3.12, nó chứa độc lập tuyến tính (linearly independent) họ mà là cơ sở (basis) với chặt ít hơn $n$ các phần tử, contradicting Định lý 3.12 (và $(2))$.

> **Định nghĩa 3.9.** Nếu $E$ là không gian vectơ (vector space) có số chiều $n \ge 1$, với mọi không gian con $U$ của $E$, nếu dim(U) $= 1$, thì $U$ được gọi là một đường thẳng; nếu dim(U) $= 2$, thì $U$ được gọi là một mặt phẳng; nếu dim(U) $=$ n-1, thì $U$ được gọi là một siêu phẳng (hyperplane). Nếu dim(U) $= k$, thì $U$ đôi khi được gọi là một k-plane. Cho $(u_{i})_{i\in I}$ là cơ sở (basis) của không gian vectơ (vector space) $E$. Với mọi vectơ $v \in E$, vì họ $(u_{i})_{i\in I}$ sinh ra $E$, có một họ $(\lambda_{i} )_{i\in I}$ của các vô hướng trong $K$, sao cho
$$v = \sum_{i\in I}  \lambda_{i} u_{i}.$$
Rất quan trọng sự kiện là rằng họ $(\lambda_{i} )_{i\in I}$ là duy nhất.

> **Mệnh đề 3.14.** Cho trước không gian vectơ (vector space) $E$, cho $(u_{i})_{i\in I}$ là họ của các vectơ trong $E$. Cho $v \in E$,
$$and assume that v = \sum_{i}  \in I \lambda_{i} u_{i}. Then the family (\lambda_{i} )_{i\in I} of scalars such that v = \sum_{i}  \in I \lambda_{i} u_{i}$$
Là duy nhất khi và chỉ khi $(u_{i})_{i\in I}$ là độc lập tuyến tính (linearly independent).

<!-- PAGE 94 -->

*Chứng minh.* Thứ nhất, giả sử rằng $(u_{i})_{i\in I}$ là độc lập tuyến tính (linearly independent). Nếu $(\mu_{i} )_{i\in I}$ là một cái khác họ của các vô hướng
$$in K such that v = \sum_{i}  \in I \mu_{i} u_{i}, then we have$$
$$\sum_{i\in I}  (\lambda_{i}  -\mu_{i} )u_{i} = 0,$$
Và vì $(u_{i})_{i\in I}$ là độc lập tuyến tính (linearly independent), ta phải có $\lambda_{i} -\mu_{i}  = 0$ với mọi $i \in$ I, nghĩa là, $\lambda_{i}  = \mu_{i}$ với mọi $i \in$ I. điều ngược lại được hiển thị bởi mâu thuẫn. Nếu $(u_{i})_{i\in I}$ đã là phụ thuộc tuyến tính (linearly dependent), ở đó sẽ là họ $(\mu_{i} )_{i\in I}$ của các vô hướng không tất cả null sao cho
$$\sum_{i\in I}  \mu_{i} u_{i} = 0$$
Và $\mu_{j}  \neq  0$ với một số $j \in$ I. Nhưng khi đó,
$$v = \sum_{i\in I}  \lambda_{i} u_{i} + 0 = \sum_{i\in I}  \lambda_{i} u_{i} + \sum_{i\in I}  \mu_{i} u_{i} = \sum_{i\in I}  (\lambda_{i}  + \mu_{i} )u_{i},$$
Với $\lambda_{j}  \neq  \lambda_{j}  +\mu$ vì $\mu_{j}  \neq  0$, contradicting giả định rằng $(\lambda_{i} )_{i\in I}$ là duy nhất họ
$$such that v = \sum_{i}^{j}  \in I \lambda_{i} u_{i}.$$

> **Định nghĩa 3.10.** Nếu $(u_{i})_{i\in I}$ là cơ sở (basis) của không gian vectơ (vector space) $E$, với mọi vectơ $v \in E$, nếu $(x_{i})_{i\in I}$ là duy nhất họ của các vô hướng trong $K$ sao cho
$$v = \sum_{i\in I}  x_{i}u_{i},$$
Mỗi $x_{i}$ được gọi là thành phần (hoặc tọa độ) của chỉ số $i$ của $v$ đối với cơ sở (basis) $(u_{i})_{i\in I}$. Cho trước trường $K$ và bất kỳ (khác rỗng) tập hợp $I$, ta có thể tạo thành không gian vectơ (vector space) $K^{(I)}$ mà, trong một số nghĩa, là tiêu chuẩn không gian vectơ (vector space) có số chiều |I|.

> **Định nghĩa 3.11.** Cho trước trường $K$ và bất kỳ (khác rỗng) tập hợp $I$, cho $K^{(I)}$ là tập con của cartesian tích $K^{I}$ bao gồm của tất cả các họ $(\lambda_{i} )_{i\in I}$ với hữu hạn hỗ trợ/giá (support) của các vô hướng trong $K.^{1}$ Ta định nghĩa phép cộng và phép nhân bởi vô hướng (scalar) như sau:
$$(\lambda_{i} )_{i\in I} + (\mu_{i} )_{i\in I} = (\lambda_{i}  + \mu_{i} )_{i\in I},$$
Và
$$\lambda  \cdot  (\mu_{i} )_{i\in I} = (\lambda \mu_{i} )_{i\in I}.$$
Ta kiểm chứng được ngay rằng phép cộng và phép nhân bởi vô hướng (scalar) là tốt được định nghĩa. Do đó, $K^{(I)}$ là không gian vectơ (vector space). Hơn nữa, bởi vì các họ với hữu hạn hỗ trợ/giá (support) được xét, họ $(e_{i})_{i\in I}$ của các vectơ $e_{i}$, được định nghĩa sao cho $(e_{i})_{j} = 0$ nếu j̸ $= i$ và $(e_{i})_{i} = 1$, là rõ ràng cơ sở (basis) của không gian vectơ (vector space) $K^{(I)}$. Khi $I = {1, \dots  , n}$, ta ký hiệu $K^{(I)}$ bởi $K^{n}$. hàm $\iota$: I $\to K^{(I)}$, sao cho $\iota (i) = e_{i}$ với mọi $i \in$ I, là rõ ràng đơn ánh.  Khi I là hữu hạn tập hợp, $K^{(I)} = K^{I}$, nhưng điều này là sai khi I là vô hạn. Thực ra, $dim(K^{(I)}) =$
$$when I is infinite.$$
$$\frac{|I|,butdim(K^{I})isstrictlygreater}{WhereK^{I}denotesthesetofallfunctions} 1        from I to K.$$
