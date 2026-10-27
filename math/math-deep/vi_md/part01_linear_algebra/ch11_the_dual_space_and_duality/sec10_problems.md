# Các bài tập


<!-- PAGE 449 -->
$\bullet$ ma trận của chuyển vị (transpose) ánh xạ $f^{\top}$ bằng chuyển vị (transpose) của ma trận của ánh xạ $f$ (Mệnh đề 11.14). $\bullet$ Cho bất kỳ ma trận cỡ $m \times  n$ $A$,
$$rk(A) = rk(A^{\top}).$$
$\bullet$ Đặc trưng của hạng (rank) của ma trận theo cực đại khả nghịch ma trận con (Mệnh đề 11.16). $\bullet$ bốn cơ bản các không gian con:
$$\mathrm{Im} f, \mathrm{Im} f^{\top} , \mathrm{Ker} f, \mathrm{Ker} f^{\top} .$$
$\bullet$ cột không gian, không gian hạch (nullspace), hàng không gian, và trái không gian hạch (nullspace) (của ma trận). $\bullet$ Tiêu chuẩn cho solvability của phương trình của tạo thành Ax $= b$ theo trái không gian hạch (nullspace).

## 11.10 Các bài tập

Bài toán 11.1. Chứng minh các tính chất sau đây của phép chuyển vị:
$$(f + g)^{\top}= f^{\top} + g^{\top}$$
$$(g \circ f)^{\top}= f^{\top} \circ g^{\top}$$
$$id_{E}^{\top} = id_{E*}.$$
Bài toán 11.2. Cho $(u_{1}, \dots  , u_{n-1})$ là $n$ - $1$ các vectơ độc lập tuyến tính (linearly independent) $u_{i} \in \mathbb{C}^{n}$. Chứng minh rằng hyperlane $H$ được sinh (spanned) bởi $(u_{1}, \dots  , u_{n-1})$ là không gian hạch (nullspace) của dạng tuyến tính (linear form)
$$x \mapsto \det(u_{1}, \dots  , u_{n-1}, x),x \in \mathbb{C}^{n}.$$
Chứng minh rằng nếu $A$ là ma trận cỡ $n \times  n$ có các cột là $(u_{1}, \dots  , u_{n-1}, x)$, và nếu $c_{i} = (-1)^{i+n} det(A_{in})$ là phần bù đại số (cofactor) của $a_{in} = x_{i}$ cho $i = 1, \dots  , n$, thì $H$ được định nghĩa bởi phương trình
$$c_{1}x_{1} + \cdots  + c_{n}x_{n} = 0.$$
$$\mathbb{R}^{n} \mathbb{R}^{n} \mathbb{R}$$
Bài toán 11.3. $(1)$ Cho $\phi$: $\times \to$ là ánh xạ được định nghĩa bởi
$$\phi ((x_{1}, \dots  , x_{n}), (y_{1}, \dots  , y_{n})) = x_{1}y_{1} + \cdots  + x_{n}y_{n}.$$
Chứng minh rằng $\phi$ là song tuyến tính không suy biến cặp. Suy ra rằng $(\mathbb{R}^{n})^{*}$ là đẳng cấu đến $\mathbb{R}^{n}$. Chứng minh rằng $\phi (x, x) = 0$ khi và chỉ khi $x = 0$.

<!-- PAGE 450 -->
$$\mathbb{R}^{4} \mathbb{R}^{4} \mathbb{R}$$
$(2)$ Cho $\phi_{L}$: $\times \to$ là ánh xạ được định nghĩa bởi
$$\phi_{L} ((x_{1}, x_{2}, x_{3}, x_{4}), (y_{1}, y_{2}, y_{3}, , y_{4})) = x_{1}y_{1} -x_{2}y_{2} -x_{3}y_{3} -x_{4}y_{4}.$$
Chứng minh rằng $\phi$ là song tuyến tính không suy biến cặp.
$$\mathbb{R}^{4}$$
Chỉ ra rằng ở đó tồn tại khác không các vectơ $x \in$ sao cho $\phi_{L} (x, x) = 0$.
$$\mathbb{R}^{4}$$
Nhận xét: không gian vectơ (vector space) được trang bị ở trên dạng song tuyến tính (bilinear form) được gọi là Lorentz tạo thành được gọi là Minkowski không gian.
Bài toán 11.4. Cho trước bất kỳ hai các không gian con $V_{1}, V_{2}$ của không gian vectơ hữu hạn chiều $E$, chứng minh rằng
$$(V_{1} + V_{2})^{0}= V_{1}^{0} \cap V_{2}^{0}$$
$$(V_{1} \cap V_{2})^{0}= V_{1}^{0} + V_{2}^{0} .$$
Beware rằng trong phương trình thứ hai, $V_{1}$ và $V_{2}$ là các không gian con của $E$, không $E^{*}$.
$$and ($$
Hint. để chứng minh phương trình thứ hai, chứng minh inclusions $V_{1}^{0} +V_{2}^{0} \subseteq (V_{1}\cap V_{2})^{0} V_{1}\cap V_{2})^{0} \subseteq V_{1}^{0}  + V_{2}^{0}$. Chứng minh thứ hai inclusion là little khó/tinh tế. Thứ nhất, chứng minh rằng ta có thể chọn không gian con $W_{1}$ của $V_{1}$ và không gian con $W_{2}$ của $V_{2}$ sao cho $1. V_{1}$ là tổng trực tiếp (direct sum) $V_{1} = (V_{1} \cap V_{2}) \oplus W_{1}. 2. V_{2}$ là tổng trực tiếp (direct sum) $V_{2} = (V_{1} \cap V_{2}) \oplus W_{2}. 3. V_{1} + V_{2}$ là tổng trực tiếp (direct sum) $V_{1} + V_{2} = (V_{1} \cap V_{2}) \oplus W_{1} \oplus W_{2}$.
Bài toán 11.5. $(1)$ Cho $A$ là bất kỳ ma trận cỡ $n \times  n$ sao cho tổng của các phần tử (entries) của mọi hàng của $A$ là cùng (nói $c_{1})$, và tổng của các phần tử (entries) của mọi cột của $A$ là cùng (nói $c_{2})$. Chứng minh rằng $c_{1} = c_{2}$.
$(2)$ Chứng minh rằng với mọi $n \ge 2$, 2n - $2$ các phương trình asserting rằng tổng của các phần tử (entries) của mọi hàng của $A$ là cùng, và tổng của các phần tử (entries) của mọi cột của $A$ là cùng là lineary độc lập. Ví dụ, khi $n = 4$, ta có kết quả sau $6$ các phương trình
$$a_{11} + a_{12} + a_{13} + a_{14} -a_{21} -a_{22} -a_{23} -a_{24} = 0$$
$$a_{21} + a_{22} + a_{23} + a_{24} -a_{31} -a_{32} -a_{33} -a_{34} = 0$$
$$a_{31} + a_{32} + a_{33} + a_{34} -a_{41} -a_{42} -a_{43} -a_{44} = 0$$
$$a_{11} + a_{21} + a_{31} + a_{41} -a_{12} -a_{22} -a_{32} -a_{42} = 0$$
$$a_{12} + a_{22} + a_{32} + a_{42} -a_{13} -a_{23} -a_{33} -a_{43} = 0$$
$$a_{13} + a_{23} + a_{33} + a_{43} -a_{14} -a_{24} -a_{34} -a_{44} = 0.$$
Hint. Nhóm các phương trình như above; nghĩa là, thứ nhất danh sách $n$ - $1$ các phương trình relating các hàng, và thì danh sách $n$ - $1$ các phương trình relating các cột. Chứng minh rằng thứ nhất $n$ - $1$ các phương trình

<!-- PAGE 451 -->
Là độc lập tuyến tính (linearly independent), và rằng cuối cùng $n$ - $1$ các phương trình là cũng độc lập tuyến tính (linearly independent). Thì, tìm relationship giữa hai các nhóm của các phương trình rằng sẽ cho phép bạn để chứng minh rằng chúng sinh (span) không gian con $V^{r}$ và $V^{c}$ sao cho $V^{r} \cap V^{c} = (0)$.
$(3)$ Bây giờ xét magic squares. Như vậy các ma trận thỏa mãn hai các điều kiện về tổng của các phần tử (entries) trong mỗi hàng và trong mỗi cột là cùng số, và cũng additional hai các ràng buộc rằng chính descending và chính ascending các đường chéo cộng sai khác điều này chung/phổ biến số. Traditionally, nó là cũng cần thiết rằng các phần tử (entries) trong magic square là dương các số nguyên, nhưng ta sẽ xét suy rộng/tổng quát hóa magic square với tùy ý thực các phần tử (entries). Ví dụ, trong trường hợp $n = 4$, ta có kết quả sau hệ của $8$ các phương trình:
$$a_{11} + a_{12} + a_{13} + a_{14} -a_{21} -a_{22} -a_{23} -a_{24} = 0$$
$$a_{21} + a_{22} + a_{23} + a_{24} -a_{31} -a_{32} -a_{33} -a_{34} = 0$$
$$a_{31} + a_{32} + a_{33} + a_{34} -a_{41} -a_{42} -a_{43} -a_{44} = 0$$
$$a_{11} + a_{21} + a_{31} + a_{41} -a_{12} -a_{22} -a_{32} -a_{42} = 0$$
$$a_{12} + a_{22} + a_{32} + a_{42} -a_{13} -a_{23} -a_{33} -a_{43} = 0$$
$$a_{13} + a_{23} + a_{33} + a_{43} -a_{14} -a_{24} -a_{34} -a_{44} = 0$$
$$a_{22} + a_{33} + a_{44} -a_{12} -a_{13} -a_{14} = 0$$
$$a_{41} + a_{32} + a_{23} -a_{11} -a_{12} -a_{13} = 0.$$
Nói chung, phương trình liên quan đến descending đường chéo là
$$a_{22} + a_{33} + \cdots  + a_{nn} -a_{12} -a_{13} -\cdots  -a_{1n} = 0(r)$$
Và phương trình liên quan đến ascending đường chéo là
$$a_{n1} + a_{n-12} + \cdots  + a_{2n-1} -a_{11} -a_{12} -\cdots  -a_{1n-1} = 0.(c)$$
Chứng minh rằng nếu $n \ge 3$, thì 2n các phương trình asserting rằng ma trận là suy rộng/tổng quát hóa magic square là độc lập tuyến tính (linearly independent). Hint. Các phương trình là một cách thực các dạng tuyến tính, do đó tìm một số ma trận annihilated bởi tất cả các phương trình ngoại trừ phương trình $r$, và một số ma trận annihilated bởi tất cả các phương trình ngoại trừ phương trình $c$.
Bài toán 11.6. Cho $U_{1}, \dots  , U_{p}$ là một số các không gian con của không gian vectơ (vector space) $E$, và giả sử rằng chúng tạo thành tổng trực tiếp (direct sum) $U = U_{1} \oplus \cdots  \oplus U_{p}$. Cho $j_{i}$: $U_{i} \to U_{1} \oplus \cdots  \oplus U_{p}$ là chính tắc các đơn ánh, và cho $\pi_{i}$: $U_{1}^{*}  \times  \cdots  \times  U_{p}^{*} \to U_{i}^{*}$ là chính tắc các phép chiếu. Chứng minh rằng có một đẳng cấu $f$ từ $(U_{1} \oplus \cdots  \oplus U_{p})^{*}$ đến $U_{1}^{*}  \times  \cdots  \times  U_{p}^{*}$ sao cho
$$\pi_{i}  \circ f = j_{i}^{\top} ,1 \le i \le p.$$
Bài toán 11.7. Cho $U$ và $V$ là hai các không gian con của không gian vectơ (vector space) $E$ sao cho $E = U \oplus V$. Chứng minh rằng
$$E^{*}= U^{0}\oplus V^{0}.$$

<!-- PAGE 452 -->
