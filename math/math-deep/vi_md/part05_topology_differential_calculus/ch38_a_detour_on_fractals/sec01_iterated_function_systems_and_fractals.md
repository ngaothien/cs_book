# Iterated Hàm Các hệ và Fractals


<!-- PAGE 1433 -->
Chương $38 A$ Detour Trên Fractals

## 38.1 Iterated Hàm Các hệ và Fractals

Pleasant ứng dụng của Hausdorffdistance và của cố định điểm định lý cho contracting các ánh xạ là phương pháp cho định nghĩa lớp của “self-similar” fractals. Cho điều này, ta có thể sử dụng iterated hàm các hệ.

> **Định nghĩa 38.1.** Cho trước không gian mêtric (metric space), $(X, d)$, iterated hàm hệ, cho ngắn, các nếu, là hữu hạn dãy của các hàm, $(f_{1}, \dots  , f_{n})$, ở đâu mỗi $f_{i}$: $X \to X$ là contracting ánh xạ. khác rỗng compắc tập con, $K$, của $X$ là bất biến tập hợp (hoặc attractor) cho các nếu, $(f_{1}, \dots  , f_{n})$, nếu
$$K = f_{1}(K) \cup \cdots  \cup f_{n}(K).$$
Major kết quả về các nếu’s là sau đây:

> **Định lý 38.1.** Nếu $(X, d)$ là khác rỗng không gian mêtric đầy đủ, thì mọi iterated hàm hệ, $(f_{1}, \dots  , f_{n})$, có duy nhất bất biến tập hợp, $A$, mà là khác rỗng compắc tập con của $X$. Hơn nữa, với mọi khác rỗng compắc tập con, $A_{0}$, của $X$, điều này bất biến tập hợp, $A$, nếu giới hạn của dãy, $(A_{m})$, ở đâu $A_{m+1} = f_{1}(A_{m}) \cup \cdots  \cup f_{n}(A_{m})$.

*Chứng minh.* Vì $X$ là đầy đủ, theo Định lý 37.55, không gian $(\mathcal{K}(X), D)$ là không gian mêtric đầy đủ. định lý sẽ suy ra từ Định lý 37.54 nếu ta có thể chỉ ra rằng ánh xạ, $F$: $\mathcal{K}(X) \to$ K(X), được định nghĩa sao cho
$$F(K) = f_{1}(K) \cup \cdots  \cup f_{n}(K),$$
Với mọi khác rỗng tập compắc (compact set), $K$, là contracting ánh xạ. Cho $A, B$ là bất kỳ hai khác rỗng compắc các tập con của $X$ và xét bất kỳ $\eta  \ge$ D(, $B)$. Vì mỗi $f_{i}$: $X \to X$ là contracting ánh xạ, tồn tại một $\lambda_{i}$, với $0 \le \lambda_{i}  < 1$, sao cho
$$d(f_{i}(a), f_{i}(b)) \le \lambda_{i} d(a, b),$$
$$1433$$

<!-- PAGE 1434 -->
Với mọi, $b \in X$. Cho $\lambda  = max{\lambda_{1} , \dots  , \lambda_{n}$ }. Ta khẳng định rằng
$$D(F(A), F(B)) \le \lambda D(A, B).$$
Với mọi $x \in$ F() $= f_{1}(A)\cup \cdots \cup f_{n}(A)$, tồn tại một $a_{i} \in A_{i}$ sao cho $x = f_{i}(a_{i})$ và vì $\eta  \ge$ D(, $B)$, tồn tại một $b_{i} \in B$ sao cho
$$d(a_{i}, b_{i}) \le \eta ,$$
Và do đó,
$$d(x, f_{i}(b_{i})) = d(f_{i}(a_{i}), f_{i}(b_{i})) \le \lambda_{i} d(a_{i}, b_{i}) \le \lambda \eta .$$
Điều này chỉ ra rằng
$$F(A) \subseteq V_{\lambda \eta}(F(B)).$$
Tương tự, ta có thể chứng minh rằng
$$F(B) \subseteq V_{\lambda \eta}(F(A)),$$
Và vì điều này nghiệm đúng với mọi $\eta  \ge$ D(, $B)$, ta được chứng minh rằng
$$D(F(A), F(B)) \le \lambda D(A, B)$$
Ở đâu $\lambda  = max{\lambda_{1} , \dots  , \lambda_{n}$ }. Vì $0 \le \lambda_{i}  < 1$, ta có $0 \le \lambda  < 1$ và $F$ là thật vậy contracting ánh xạ. Định lý 38.1 justifies sự tồn tại của nhiều quen thuộc “self-similar” fractals. Một của tốt nhất đã biết fractals là Sierpinski gasket.

> **Ví dụ 38.1.** Xét equilateral tam giác với các đỉnh, $b, c$, và cho $f_{1}, f_{2}, f_{3}$ là các phép vị tự của các tâm, $b, c$ và tỉ số $1/2$. Sierpinski gasket là bất biến tập hợp của các nếu $(f_{1}, f_{2}, f_{3})$. dilations $f_{1}, f_{2}, f_{3}$ có thể được được định nghĩa một cách tường minh như sau, giả sử rằng
$$\sqrt$$
$a = (-1/2, 0), b = (1/2, 0)$, và $c = (0, \overline{3}/2)$. các ánh xạ co (contraction) $f_{1}, f_{2}, f_{3}$ là specified bởi
$$x'= \frac{1}{2} x - \frac{1}{4} ,$$
$$y'= \frac{1}{2} y,$$
$$x'= \frac{1}{2} x + \frac{1}{4} ,$$
$$y'= \frac{1}{2} y,$$
Và
$$x'= \frac{1}{2} x,$$
$$y'= \frac{1}{2} y + \frac{\sqrt{3}}{4} .$$

<!-- PAGE 1435 -->
$$Figure 38.1: The Sierpinski gasket$$
Ta đã viết Mathematica bài toán quy hoạch rằng iterates bất kỳ hữu hạn số của các ánh xạ afin trên bất kỳ input hình bao gồm của các tổ hợp của các điểm, đường thẳng các đoạn thẳng, và các đa giác (với phần trong (phần trong (interior)) của chúng các điểm). Bắt đầu với các cạnh của tam giác, $b, c$, sau $6$ các vòng lặp, ta thu được picture được hiển thị trong Hình 38.1. Nó là amusing rằng cùng fractal là thu được không có matter những gì ban đầu khác rỗng compắc hình là. Nó là thú vị để xem những gì xảy ra nếu ta bắt đầu với solid tam giác (với phần trong (phần trong (interior)) của nó các điểm). kết quả sau $6$ các vòng lặp được hiển thị trong Hình 38.2. sự hội tụ towards Sierpinski gasket là rất fast. Incidently, có nhiều khác các cách của định nghĩa Sierpinski gasket. đẹp variation trên theme của Sierpinski gasket là Sierpinski dragon.

> **Ví dụ 38.2.** Sierpinski dragon là specified bởi sau đây ba các ánh xạ co (contraction):
$$x'=- \frac{1}{4} x - \frac{\sqrt{3}}{4} y + \frac{3}{4} ,$$
$$y'= \frac{\sqrt3}{4} x - \frac{1}{4} y + \frac{\sqrt3}{4} ,$$
$$x'=- \frac{1}{4\sqrt} x + \frac{\sqrt{3}}{4} y - \frac{3}{4\sqrt} ,$$
$$y'=- \frac{\overline{3}}{4} x - \frac{1}{4} y + \frac{\overline{3}}{4} ,$$
$$x'= \frac{1}{2} x,$$
$$y'= \frac{1}{2} y + \frac{\sqrt{3}}{2} .$$

<!-- PAGE 1436 -->
$$Figure 38.2: The Sierpinski gasket, version 2$$
Kết quả của $7$ các vòng lặp bắt đầu từ đường thẳng đoạn thẳng $(-1, 0), (1, 0))$, được hiển thị trong Hình 38.3. Điều này đường cong hội tụ đến biên (boundary) của Sierpinski gasket. khác nhau loại của fractal là Heighway dragon.

> **Ví dụ 38.3.** Heighway dragon là specified bởi sau đây hai các ánh xạ co (contraction):
$$x'= \frac{1}{2} x - \frac{1}{2} y,$$
$$y'= \frac{1}{2} x + \frac{1}{2} y,$$
$$x'=- \frac{1}{2} x - \frac{1}{2} y,$$
$$y'= \frac{1}{2} x - \frac{1}{2} y + 1.$$
Nó có thể được được hiển thị rằng với mọi số của các vòng lặp, đa giác thực hiện không cross chính nó. Điều này có nghĩa là không có cạnh là traversed hai lần và rằng nếu điểm là traversed hai lần, thì điều này điểm là endpoint của một số cạnh. kết quả của $13$ các vòng lặp, bắt đầu với đường thẳng đoạn thẳng $((0, 0), (0, 1))$, được hiển thị trong Hình 38.4. Heighway dragon hóa ra đến fill đóng và bị chặn tập hợp. Nó có thể cũng được hiển thị rằng mặt phẳng có thể được tiled với copies của Heighway dragon. Một cái khác tốt đã biết ví dụ là Koch đường cong.

<!-- PAGE 1437 -->
$$Figure 38.3: The Sierpinski dragon$$
$$Figure 38.4: The Heighway dragon$$

<!-- PAGE 1438 -->
$$Figure 38.5: The Koch curve$$

> **Ví dụ 38.4.** Koch đường cong là specified bởi sau đây bốn các ánh xạ co (contraction):
$$x'= \frac{1}{3} x - \frac{2}{3} ,$$
$$y'= \frac{1}{3} y,$$
$$x'= \frac{1}{\sqrt6} x - \frac{\sqrt{3}}{6} y - \frac{1}{\sqrt6} ,$$
$$y'= \frac{\overline{3}}{6} x + \frac{1}{6} y + \frac{\overline{3}}{6} ,$$
$$x'= \frac{1}{6} x + \frac{\sqrt{3}}{6} y + \frac{1}{6} ,$$
$$y'=- \frac{\sqrt{3}}{6} x + \frac{1}{6} y + \frac{\sqrt{3}}{6} ,$$
$$x'= \frac{1}{3} x + \frac{2}{3} ,$$
$$y'= \frac{1}{3} y.$$
Koch đường cong là ví dụ của liên tục đường cong mà là nowhere khả vi (differentiable) (bởi vì nó “wiggles” cũng nhiều). Nó là đường cong của vô hạn độ dài. kết quả của $6$ các vòng lặp, bắt đầu với đường thẳng đoạn thẳng $((-1, 0), (1, 0))$, được hiển thị trong Hình 38.5. đường cong thu được bởi đặt ba Kock các đường cong cùng nhau trên các vế/cạnh của equilateral tam giác là đã biết như snowflake đường cong (cho hiển nhiên các lý do, xem ở dưới!).

<!-- PAGE 1439 -->
$$Figure 38.6: The snowflake curve$$

> **Ví dụ 38.5.** snowflake đường cong thu được sau $5$ các vòng lặp được hiển thị trong Hình 38.6. snowflake đường cong là ví dụ của đóng đường cong của vô hạn độ dài cận hữu hạn diện tích. Ta kết luận với một cái khác nổi tiếng ví dụ, biến thể của Hilbert đường cong.

> **Ví dụ 38.6.** Điều này phiên bản của Hilbert đường cong được định nghĩa bởi sau đây bốn các ánh xạ co (contraction):
$$x'= \frac{1}{2} x - \frac{1}{2} ,$$
$$y'= \frac{1}{2} y + 1,$$
$$x'= \frac{1}{2} x + \frac{1}{2} ,$$
$$y'= \frac{1}{2} y + 1,$$
$$x'=- \frac{1}{2} y + 1,$$
$$y'= \frac{1}{2} x + \frac{1}{2} ,$$
$$x'= \frac{1}{2} y -1,$$
$$y'=- \frac{1}{2} x + \frac{1}{2} .$$

<!-- PAGE 1440 -->
$$Figure 38.7: A Hilbert curve$$
Điều này liên tục đường cong là space-filling đường cong, trong nghĩa rằng ảnh (ảnh (image)) của nó là toàn bộ unit square. kết quả của $6$ các vòng lặp, bắt đầu với hai các đường thẳng các đoạn thẳng $((-1, 0), (0, 1))$ và $((0, 1), (1, 0))$, được hiển thị trong Hình 38.7. Cho nhiều hơn/thêm trên iterated hàm các hệ và fractals, ta recommend Edgar $[56]$.
