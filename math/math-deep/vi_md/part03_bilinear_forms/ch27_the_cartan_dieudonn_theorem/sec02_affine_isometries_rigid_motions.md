# Afin Các phép đẳng cự (Cứng Motions)


<!-- PAGE 983 -->
Chứng minh của Bổ đề 27.4 cho ta hai flips $f_{2k-1}$ và $f_{2k}$ sao cho
$$f_{2k}(e_{n-2}) = -e_{n-2}ands_{2k} \circ s_{2k-1} = f_{2k} \circ f_{2k-1},$$
Vì $(n$ - 2)th đường chéo phần tử (entry) trong cả hai các ma trận là $-1$, mà có nghĩa là $e_{n-2} \in F_{2k}^{\perp}$, ở đâu $F_{2k}$ là không gian con có số chiều $n$ - $2$ xác định $f_{2k}$. Vì $u = \|u\|e_{n-2}$, ta cũng có $u \in F_{2k}^{\perp}$.
Các nhận xét:
$(1)$ Nó là dễ để chứng minh rằng nếu $f$ là phép quay trong Do đó(3) và nếu $D$ là của nó trục và $\theta$ là của nó góc của phép quay, thì $f$ là hợp thành của hai flips về các đường thẳng $D_{1}$ và $D_{2}$ trực giao đến $D$ và tạo ra góc $\theta /2$.
$(2)$ Nó là tự nhiên đến ask những gì là tối tiểu số của flips cần thiết để thu được phép quay $f$ (khi $n \ge 3)$. Như cho tùy ý các phép đẳng cự, ta sẽ chứng minh sau này rằng mọi phép quay là hợp thành của $k$ flips, ở đâu
$$k = n -\dim(\mathrm{Ker} (f -id)),$$
Và rằng điều này số là tối tiểu (ở đâu $n =$ dim(E)). Ta bây giờ turn đến afin các phép đẳng cự.

## 27.2 Afin Các phép đẳng cự (Cứng Motions)

Trong còn lại các mục ta study afin các phép đẳng cự. Thứ nhất, ta đặc trưng hóa tập hợp của cố định các điểm của ánh xạ afin (affine map). Bằng cách sử dụng điều này đặc trưng, ta chứng minh rằng mọi afin phép đẳng cự (isometry) $f$ có thể được được viết một cách duy nhất như
$$f = t \circ g,witht \circ g = g \circ t,$$
Ở đâu $g$ là phép đẳng cự (isometry) có cố định điểm, và $t$ là phép tịnh tiến bởi vectơ $\tau$ sao cho $\longrightarrow f (\tau$) $= \tau$, và với một số additional đẹp các tính chất (xem Định lý 27.10). Điều này là gener-
$$\mathbb{R}^{3}$$
Alization của cổ điển kết quả của Chasles về (thực sự/đúng đắn) cứng motions trong (screw motions). Ta chứng minh tổng quát hóa của Cartan–Dieudonn´e định lý cho afin các phép đẳng cự: Mọi phép đẳng cự (isometry) trong Là(n) có thể được viết dưới dạng hợp thành của nhiều nhất $n$ afin các phép đối xứng nếu nó có cố định điểm, hoặc khác như hợp thành của nhiều nhất $n + 2$ afin các phép đối xứng. Ta cũng chứng minh rằng mọi cứng motion trong SE(n) là hợp thành của nhiều nhất $n$ afin flips (cho $n \ge 3)$. Điều này là somewhat đáng ngạc nhiên, xét theo trước đó định lý.

> **Định nghĩa 27.1.** Cho trước bất kỳ hai không tầm thường Euclidean các không gian afin $E$ và $F$ của cùng hữu hạn số chiều $n$, hàm $f$: $E \to F$ là afin phép đẳng cự (isometry) (hoặc cứng ánh xạ) nếu nó là ánh xạ afin (affine map) và
$$----\longrightarrow \longrightarrow$$
$$\|f(a)f(b)\|= \|ab\|,$$
Với mọi, $b \in E$. Khi $E = F$, afin phép đẳng cự (isometry) $f$: $E \to E$ cũng được gọi là một cứng motion.

<!-- PAGE 984 -->
Do đó, afin phép đẳng cự (isometry) là ánh xạ afin (affine map) rằng bảo toàn khoảng cách. Điều này là khá mạnh requirement. Thực ra, ta sẽ chỉ ra rằng với mọi hàm $f$: $E \to F$, giả định rằng
$$----\longrightarrow \longrightarrow$$
$$\|f(a)f(b)\|= \|ab\|,$$
Với mọi, $b \in E$, buộc $f$ là ánh xạ afin (affine map).
Nhận xét: Đôi khi, afin phép đẳng cự (isometry) được định nghĩa như song ánh (bijective) afin phép đẳng cự (isometry). Khi $E$ và $F$ là của hữu hạn số chiều, các định nghĩa là tương đương. sau đây đơn giản bổ đề là để lại như một bài tập.

> **Mệnh đề 27.6.** Cho trước bất kỳ hai không tầm thường Euclidean các không gian afin $E$ và $F$ của cùng hữu hạn số chiều $n$, ánh xạ afin (affine map) $f$: $E \to F$ là afin phép đẳng cự (isometry) khi và chỉ khi của nó liên kết tuyến tính $\longrightarrow  \longrightarrow \longrightarrow$ ánh xạ $f$: $E \to F$ là phép đẳng cự (isometry). afin phép đẳng cự (isometry) là song ánh.
$$\longrightarrow$$
Cho chúng ta bây giờ xét afin các phép đẳng cự $f$: $E \to E$. Nếu $f$ là phép quay, ta gọi $f$ thực sự/đúng đắn (hoặc
$$\longrightarrow$$
Trực tiếp) afin phép đẳng cự (isometry), và nếu $f$ là suy rộng/không thực sự tuyến tính phép đẳng cự (isometry), ta gọi $f$ suy rộng/không thực sự (hoặc skew) afin phép đẳng cự (isometry). Dễ dàng chứng minh được rằng tập hợp của afin các phép đẳng cự $f$: $E \to E$ các dạng
$$\longrightarrow$$
Nhóm, và những phần tử đó cho mà $f$ là phép quay là nhóm con. nhóm của afin các phép đẳng cự, hoặc cứng motions, là nhóm con của afin nhóm GA(E), được ký hiệu bởi Là(E) (hoặc Là(n) khi $E = \mathbb{E}^{n})$. Trong Snapper và Troyer $[168]$ nhóm của cứng motions được ký hiệu bởi Mo(E). Vì ta ký hiệu nhóm của afin các song ánh như GA(E), perhaps ta nên ký hiệu nhóm của afin các phép đẳng cự bởi IA(E) (hoặc EA(E)!). nhóm con của Là(E) bao gồm của trực tiếp cứng motions là cũng nhóm con của SA(E), và nó được ký hiệu bởi SE(E) (hoặc SE(n),
$$\longrightarrow$$
Khi $E = \mathbb{E}^{n})$. các phép tịnh tiến là afin các phép đẳng cự $f$ cho mà $f =$ id, đồng nhất thức
$$\longrightarrow$$
Ánh xạ trên $E$. sau đây bổ đề là counterpart của Bổ đề 12.12 cho các phép đẳng cự giữa Euclidean các không gian vectơ.

> **Mệnh đề 27.7.** Cho trước bất kỳ hai không tầm thường Euclidean các không gian afin $E$ và $F$ của cùng hữu hạn số chiều $n$, với mọi hàm $f$: $E \to F$, các tính chất sau đây là tương đương:
$$----\longrightarrow \longrightarrow$$
$(1) f$ là ánh xạ afin (affine map) và $\|f(a)f(b)\| = \|ab\|$, với mọi, $b \in E$.
$$----\longrightarrow \longrightarrow$$
$(2) \|f(a)f(b)\| = \|ab\|$, với mọi, $b \in E$.

*Chứng minh.* Hiển nhiên, $(1)$ suy ra $(2)$. Trong thứ tự để chứng minh rằng $(2)$ suy ra $(1)$, ta tiến hành như
$$\longrightarrow \longrightarrow$$
Suy ra. Thứ nhất, ta chọn một số tùy ý điểm $\Omega \in E$. Ta định nghĩa ánh xạ $g: E \to F$ sao cho
$$--------\longrightarrow$$
$$g(u) =f(\Omega )f(\Omega + u)$$
Với mọi $u \in E$. Vì
$$--------\longrightarrow$$
$$f(\Omega ) + g(u) = f(\Omega ) +f(\Omega )f(\Omega + u) = f(\Omega + u)$$
