# Giao của Các không gian afin


<!-- PAGE 849 -->
Cũng nhắc lại rằng mọi dạng tuyến tính (linear form) $f^{*}$ là sao cho $f^{*} (x) = \lambda_{1} x_{1} + \cdots  + \lambda_{n} x_{n}$, với mọi $x = x_{1}u_{1} + \cdots  + x_{n}u_{n}$ và một số $\lambda_{1} , \dots  , \lambda_{n}  \in \mathbb{R}$. Vì afin tạo thành $f$: $E \to \mathbb{R}$ thỏa mãn
$$\longrightarrow$$
Tính chất $f(a_{0} +x) = f(a_{0})+ f (x)$, ký hiệu $f(a_{0} +x)$ bởi $f(x_{1}, \dots  , x_{n})$, ta xem rằng ta có
$$f(x_{1}, \dots  , x_{n}) = \lambda_{1} x_{1} + \cdots  + \lambda_{n} x_{n} + \mu ,$$
Ở đâu $\mu  = f(a_{0}) \in \mathbb{R}$ và $\lambda_{1} , \dots  , \lambda_{n}  \in \mathbb{R}$. Do đó, siêu phẳng (hyperplane) là tập hợp của các điểm có các tọa độ $(x_{1}, \dots  , x_{n})$ thỏa mãn (afin) phương trình
$$\lambda_{1} x_{1} + \cdots  + \lambda_{n} x_{n} + \mu  = 0.$$

## 24.11 Giao của Các không gian afin

Trong mục này ta lấy closer nhìn tại giao của afin các không gian con. Điều này tiểu mục có thể được được bỏ qua tại thứ nhất reading. Thứ nhất, ta cần kết quả của tuyến tính đại số. Cho trước không gian vectơ (vector space) $E$ và bất kỳ hai các không gian con $M$ và $N$, có một vài thú vị các ánh xạ tuyến tính (linear maps). Ta có chính tắc các đơn ánh $i: M \to M +N$ và $j$: $N \to M +N$, chính tắc các đơn ánh $in_{1}$: $M \to M \oplus N$ và $in_{2}$: $N \to M \oplus N$, và do đó, các đơn ánh $f$: $M \cap N \to M \oplus N$ và $g: M \cap N \to M \oplus N$, ở đâu $f$ là hợp thành của inclusion ánh xạ từ $M \cap N$ đến $M$ với $in_{1}$, và $g$ là hợp thành của inclusion ánh xạ từ $M \cap N$ đến $N$ với $in_{2}$. Thì, ta có các ánh xạ $f + g: M \cap N \to M \oplus N$, và $i$ - $j$: $M \oplus N \to M + N$.

> **Mệnh đề 24.15.** Cho trước không gian vectơ (vector space) $E$ và bất kỳ hai các không gian con $M$ và $N$, với các định nghĩa ở trên,
$$0 \longrightarrow M \cap N^{f+g}\longrightarrow M \oplus N^{i-j}\longrightarrow M + N \longrightarrow 0$$
Là ngắn chính xác dãy, mà có nghĩa là $f + g$ là đơn ánh (injective), $i$ - $j$ là toàn ánh (surjective), và rằng Im $(f + g) =$ Ker $(i$ - $j)$. Hệ quả là, ta có Grassmann quan hệ
$$\dim(M) + \dim(N) = \dim(M + N) + \dim (M \cap N).$$

*Chứng minh.* Hiển nhiên là $i$ - $j$ là toàn ánh (surjective) và rằng $f + g$ là đơn ánh (injective). Giả sử rằng $(i$ - j)(u $+ v) = 0$, ở đâu $u \in M$, và $v \in N$. Thì, i(u) $=$ j(v), và do đó, theo định nghĩa của $i$ và $j$, tồn tại một $w \in M \cap N$, sao cho i(u) $=$ j(v) $= w \in M \cap N$. Theo định nghĩa của $f$ và $g, u =$ f(w) và $v =$ g(w), và do đó Im $(f + g) =$ Ker $(i$ - $j)$, như mong muốn. phần thứ hai của mệnh đề suy ra từ tiêu chuẩn các kết quả của tuyến tính đại số (xem Artin $[7]$, Strang $[176]$, hoặc Lang $[113])$. Ta bây giờ chứng minh đơn giản mệnh đề về giao của afin các không gian con.

> **Mệnh đề 24.16.** Cho trước bất kỳ không gian afin (affine space) $E$, với mọi hai khác rỗng afin các không gian con $M$ và $N$, sau đây các sự kiện đúng:

<!-- PAGE 850 -->
$$\longrightarrow \longrightarrow  \longrightarrow$$
$(1) M \cap N \neq  \emptyset$ khi và chỉ khi ab $\in M + N$ với một số $a \in M$ và một số $b \in N$.
$$\longrightarrow \longrightarrow  \longrightarrow$$
$(2) M \cap N$ bao gồm của đơn lẻ điểm khi và chỉ khi ab $\in M + N$ với một số $a \in M$ và một số $b \in N$,
$$\longrightarrow \longrightarrow$$
Và $M \cap N = {0}$.
$$\longrightarrow  \longrightarrow  \longrightarrow \longrightarrow$$
$(3)$ Nếu $S$ là least không gian con afin (affine subspace) chứa $M$ và $N$, thì $S = M + N +$ Kab (
$$\longrightarrow$$
Không gian vectơ (vector space) $E$ được định nghĩa trên trường $K)$.

*Chứng minh.* $(1)$ Chọn bất kỳ $a \in M$ và bất kỳ $b \in N$, mà là khả dĩ/có thể, vì $M$ và $N$ là khác rỗng. $\longrightarrow \longrightarrow  \longrightarrow \longrightarrow$ Vì $M = {ax$ | $x \in M}$ và $N = {by$ | $y \in N}$, nếu $M \cap N \neq  \emptyset$, với mọi $c \in M \cap N$ ta có $\longrightarrow  \longrightarrow \longrightarrow  \longrightarrow \longrightarrow  \longrightarrow \longrightarrow  \longrightarrow \longrightarrow  \longrightarrow$ ab $=$ ac - bc, với ac $\in M$ và bc $\in N$, và do đó, ab $\in M + N$. Ngược lại, giả sử rằng $\longrightarrow \longrightarrow  \longrightarrow  \longrightarrow  \longrightarrow  \longrightarrow$ ab $\in M + N$ với một số $a \in M$ và một số $b \in N$. Thì ab $=$ ax $+$ bởi, với một số $x \in M$ và một số $y \in N$. Nhưng ta cũng có
$$\longrightarrow  \longrightarrow  \longrightarrow  \longrightarrow$$
$$ab =ax +xy +yb,$$
$$\longrightarrow  \longrightarrow \longrightarrow  \longrightarrow \longrightarrow$$
Và do đó ta thu được $0 =$ xy $+$ yb - bởi, nghĩa là, xy $=$ 2by. Do đó, $b$ là giữa của đoạn thẳng
$$\longrightarrow \longrightarrow$$
$[x, y]$, và vì yx $=$ 2yb, $x =$ 2b - $y$ là tâm tỉ cự (barycenter) của được trọng số các điểm $(b, 2)$ và $(y, -1)$. Do đó $x$ cũng thuộc đến $N$, vì $N$ đang là không gian con afin (affine subspace), nó là đóng dưới các tâm tỉ cự. Do đó, $x \in M \cap N$, và $M \cap N \neq  \emptyset$.
$(2)$ Lưu ý rằng nói chung, nếu $M \cap N \neq  \emptyset$, thì
$$---\longrightarrow  \longrightarrow \longrightarrow$$
$$M \cap N =M \cap N ,$$
Bởi vì
$$---\longrightarrow \longrightarrow \longrightarrow \longrightarrow  \longrightarrow \longrightarrow$$
$$M \cap N = {ab | a, b \in M \cap N} = {ab | a, b \in M} \cap {ab | a, b \in N} =M \cap N .$$
$$---\longrightarrow$$
Vì $M \cap N = c + M \cap N$ với mọi $c \in M \cap N$, ta có
$$\longrightarrow \longrightarrow$$
$$M \cap N = c +M \cap Nfor any c \in M \cap N.$$
$$\longrightarrow \longrightarrow$$
Từ điều này suy ra rằng nếu $M \cap N \neq  \emptyset$, thì $M \cap N$ bao gồm của đơn lẻ điểm khi và chỉ khi $M \cap N = {0}$. sự kiện này cùng với những gì ta được chứng minh trong $(1)$ chứng minh $(2)$.
$(3)$ Điều này là trái như dễ bài tập.
Các nhận xét:
$$\longrightarrow \longrightarrow  \longrightarrow$$
$(1)$ chứng minh của Mệnh đề 24.16 chỉ ra rằng nếu $M \cap$ N̸ $= \emptyset$, thì ab $\in M + N$ với mọi $a \in M$ và tất cả $b \in N$.

<!-- PAGE 851 -->
$(2)$ Mệnh đề 24.16 suy ra rằng với mọi hai khác rỗng afin các không gian con $M$ và $N$, nếu $\longrightarrow  \longrightarrow \longrightarrow  \longrightarrow  \longrightarrow \longrightarrow E = M \oplus N$, thì $M \cap N$ bao gồm của đơn lẻ điểm. Thật vậy, nếu $E = M \oplus N$, thì $\longrightarrow \longrightarrow  \longrightarrow \longrightarrow$ ab $\in E$ với mọi $a \in M$ và tất cả $b \in N$, và vì $M \cap N = {0}$, kết quả suy ra từ phần $(2)$ của mệnh đề. Ta có thể bây giờ phát biểu sau đây mệnh đề.

> **Mệnh đề 24.17.** Cho trước không gian afin (affine space) $E$ và bất kỳ hai khác rỗng afin các không gian con $M$ và $N$, nếu $S$ là least không gian con afin (affine subspace) chứa $M$ và $N$, thì các tính chất sau đây đúng:
$(1)$ Nếu $M \cap N = \emptyset$, thì
$$\longrightarrow  \longrightarrow$$
$$\dim(M) + \dim(N) < \dim(E) + \dim(M +N )$$
Và
$$\longrightarrow \longrightarrow$$
$$\dim(S) = \dim(M) + \dim(N) + 1 -\dim(M \cap N ).$$
$(2)$ Nếu $M \cap N \neq  \emptyset$, thì
$$\dim(S) = \dim(M) + \dim(N) -\dim(M \cap N).$$

*Chứng minh.* chứng minh là không khó, bằng cách sử dụng Mệnh đề 24.16 và Mệnh đề 24.15, nhưng ta để lại nó như một bài tập.

<!-- PAGE 852 -->
