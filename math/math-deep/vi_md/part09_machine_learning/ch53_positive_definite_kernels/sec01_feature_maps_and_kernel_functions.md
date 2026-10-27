# Đặc trưng (feature) Các ánh xạ và Hạt nhân (kernel) Các hàm


<!-- PAGE 1945 -->
Chương $53$ Các nhân xác định dương Điều này chương là giới thiệu đến các nhân xác định dương và sử dụng của hạt nhân (kernel) các hàm trong máy học (learning). Cho $X$ là khác rỗng tập hợp. Nếu tập hợp $X$ biểu diễn tập hợp của một cách cao phi tuyến dữ liệu, nó có thể là advantageous đến ánh xạ $X$ vào không gian $F$ của nhiều cao hơn số chiều được gọi là đặc trưng (feature) không gian, bằng cách sử dụng hàm $\phi$: $X \to F$ được gọi là đặc trưng (feature) ánh xạ. Điều này ý tưởng là rằng $\phi$ “unwinds” description của objects trong $F$ trong attempt để tạo nó tuyến tính. không gian $F$ là thường không gian vectơ (vector space) được trang bị tích vô hướng (inner product) $\langle$ -, $-\rangle$. Nếu $F$ là vô hạn dimensional, thì ta giả sử rằng nó là Không gian Hilbert (Hilbert space). Nhiều các thuật toán rằng analyze hoặc phân loại dữ liệu tạo sử dụng của trong các tích $\langle \phi (x), \phi (y)\rangle$, ở đâu $x, y \in X$. Các phần tử này các thuật toán tạo sử dụng của hàm $\kappa$: $X \times  X \to \mathbb{C}$ cho trước bởi
$$\kappa (x, y) = \langle \phi (x), \phi (y)\rangle ,x, y \in X,$$
Được gọi là hạt nhân (kernel) hàm. hạt nhân (kernel) mẹo/kỹ thuật là đến pretend rằng ta có đặc trưng (feature) phép nhúng (embedding) $\phi$: $X \to F$ (thực sự unknown), nhưng đến chỉ sử dụng trong các tích $\langle \phi (x), \phi (y)\rangle$ rằng có thể được evaluated bằng cách sử dụng ban đầu dữ liệu qua đã biết hạt nhân (kernel) hàm $\kappa$. Hóa ra là các hàm của tạo thành $\kappa$ như ở trên có thể được được định nghĩa theo điều kiện mà là reminiscent của nửa xác định dương (positive semidefinite) các ma trận (xem Định nghĩa 53.2). Hơn nữa, mọi hàm thỏa mãn Định nghĩa 53.2 phát sinh từ phù hợp đặc trưng (feature) ánh xạ vào Không gian Hilbert (Hilbert space); xem Định lý 53.8. Ta minh họa hạt nhân (kernel) các phương pháp trên hạt nhân (kernel) PCA (xem Mục 53.4).

## 53.1 Đặc trưng (feature) Các ánh xạ và Hạt nhân (kernel) Các hàm


> **Định nghĩa 53.1.** Cho $X$ là khác rỗng tập hợp, cho $H$ là (phức) Không gian Hilbert (Hilbert space), và cho $\phi$: $X \to H$ là hàm được gọi là đặc trưng (feature) ánh xạ. hàm $\kappa$: $X \times  X \to \mathbb{C}$ cho trước bởi
$$\kappa (x, y) = \langle \phi (x), \phi (y)\rangle ,x, y \in X,$$
Được gọi là một hạt nhân (kernel) hàm.
$$1945$$

<!-- PAGE 1946 -->
Nhận xét: $A$ đặc trưng (feature) ánh xạ là thường được gọi là đặc trưng (feature) phép nhúng (embedding), nhưng điều này thuật ngữ là bit misleading bởi vì nó suggests rằng như vậy ánh xạ là đơn ánh (injective), mà là không nhất thiết trường hợp. Không may là điều này thuật ngữ được sử dụng bởi hầu hết people.

> **Ví dụ 53.1.** Giả sử ta có hai đặc trưng (feature) các ánh xạ $\phi_{1}$: $X \to \mathbb{R}_{1}^{n}$ và $\phi_{2}$: $X \to \mathbb{R}_{2}^{n}$, và cho $\kappa_{1} (x, y) = \langle \phi_{1} (x), \phi_{1} (y)\rangle$ và $\kappa_{2} (x, y) = \langle \phi_{2} (x), \phi_{2} (y)\rangle$ là tương ứng hạt nhân (kernel) các hàm (ở đâu $\langle$ -, $-\rangle$ là tiêu chuẩn tích vô hướng (inner product) $on\mathbb{R}^{n})$. Định nghĩa đặc trưng (feature) ánh xạ $\phi$: $X \to \mathbb{R}_{12}^{n+n}$ bởi
$$\phi (x) = (\phi_{1} (x), \phi_{2} (x)),$$
$(n_{1} + n_{2})-tuple$. Ta có $\langle \phi (x), \phi (y)\rangle = \langle (\phi_{1} (x), \phi_{2} (x)), (\phi_{1} (y), \phi_{2} (y))\rangle = \langle \phi_{1} (x), \phi_{1} (y)\rangle + \langle \phi_{2} (x), \phi_{2} (y)\rangle$
$$= \kappa_{1} (x, y) + \kappa_{2} (x, y),$$
Mà chỉ ra rằng ánh xạ $\kappa$ cho trước bởi
$$\kappa (x, y) = \kappa_{1} (x, y) + \kappa_{2} (x, y)$$
Là hạt nhân (kernel) hàm tương ứng với đặc trưng (feature) ánh xạ $\phi$: $X \to \mathbb{R}_{12}^{n+n}$.
$$\mathbb{R}^{2}\mathbb{R}^{3}$$

> **Ví dụ 53.2.** Cho $X$ là tập con của, và cho $\phi_{1}$: $X \to$ là ánh xạ cho trước bởi
$$\sqrt$$
$$\phi_{1} (x_{1}, x_{2}) = (x_{1}^{2}, x_{2}^{2},\overline{2} x_{1}x_{2}).$$
$$\mathbb{R}^{3}$$
Hình 53.1 minh họa $\phi_{1}$: $X \to$ khi $X = {((x_{1}, x_{2})$ | -10 $\le x_{1} \le 10$, -10 $\le x_{2} \le 10}$.
$$\mathbb{R}^{3}$$
Nhận thấy rằng tuyến tính các quan hệ trong đặc trưng (feature) không gian $H =$ tương ứng với toàn phương các quan hệ trong input không gian (của dữ liệu). Ta có
$$\sqrt\sqrt$$
$$\langle \phi_{1} (x), \phi_{1} (y)\rangle = \langle (x_{1}^{2}, x_{2}^{2},\overline{2} x_{1}x_{2}), (y_{1}^{2}, y_{2}^{2},\overline{2} y_{1}y_{2})\rangle$$
$$= x_{1}^{2}y_{1}^{2} + x_{2}^{2}y_{2}^{2} + 2x_{1}x_{2}y_{1}y_{2}$$
$$= (x_{1}y_{1} + x_{2}y_{2})^{2}= \langle x, y\rangle^{2} ,$$
Ở đâu $\langle x, y\rangle$ là thông thường tích vô hướng (inner product) trên $\mathbb{R}^{2}$. Do đó hàm
$$\kappa (x, y) = \langle x, y\rangle^{2}$$
Là hạt nhân (kernel) hàm liên kết với đặc trưng (feature) không gian $\mathbb{R}^{3}$.
$$\mathbb{R}^{4}$$
Nếu ta bây giờ xét ánh xạ $\phi_{2}$: $X \to$ cho trước bởi
$$\phi_{2} (x_{1}, x_{2}) = (x_{1}^{2}, x_{2}^{2}, x_{1}x_{2}, x_{1}x_{2}),$$
Ta kiểm tra ngay lập tức rằng
$$\langle \phi_{2} (x), \phi_{2} (y)\rangle = \kappa (x, y) = \langle x, y\rangle^{2} ,$$
Mà chỉ ra rằng cùng hạt nhân (kernel) có thể phát sinh từ khác nhau các ánh xạ vào khác nhau đặc trưng (feature) các không gian.

<!-- PAGE 1947 -->
$$\sqrt$$

![Figure 53.1](../../assets/ch53/fig_53_1.png)

**Hình 53.1:** parametric mặt $\phi_{1} (x_{1}, x_{2}) = (x_{1}^{2}, x_{2}^{2}, \overline{2} x_{1}x_{2})$ ở đâu -10 $\le x_{1} \le 10$ và -10 $\le x_{2} \le 10$.

> **Ví dụ 53.3.** Ví dụ 53.2 có thể được suy rộng/tổng quát hóa như sau. Giả sử ta có đặc trưng (feature) ánh xạ
$$\mathbb{R}^{n}$$
$\phi_{1}$: $X \to$ và cho $\kappa_{1} (x, y) = \langle \phi_{1} (x), \phi_{1} (y)\rangle$ là tương ứng hạt nhân (kernel) hàm (ở đâu
$$\mathbb{R}^{n}\mathbb{R}^{n} \mathbb{R}^{n}$$
$\langle$ -, $-\rangle$ là tiêu chuẩn tích vô hướng (inner product) trên). Định nghĩa đặc trưng (feature) ánh xạ $\phi$: $X \to \times$ bởi của nó $n^{2}$ các thành phần
$$\phi (x)_{(i,j)} = (\phi_{1} (x))_{i}(\phi_{1} (x))_{j},1 \le i, j \le n,$$
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
Với tích vô hướng (inner product) trên $\times$ cho trước bởi
$$\langle u, v\rangle = \sum_{i,j=1}^{n}  u_{(i,j)}v_{(i,j)}.$$
Thì ta có
$$\langle \phi (x), \phi (y)\rangle = \sum_{i,j=1}^{n}  \phi_{(i,j)} (x)\phi_{(i,j)} (y)$$
$$= \sum_{i,j=1}^{n}  (\phi_{1} (x))_{i}(\phi_{1} (x))_{j}(\phi_{1} (y))_{i}(\phi_{1} (y))_{j}$$
$$= \sum_{i=1}^{n}  (\phi_{1} (x))_{i}(\phi_{1} (y)) \sum_{ij=1}^{n}  (\phi_{1} (x))_{j}(\phi_{1} (y))_{j}$$
$$= (\kappa_{1} (x, y))^{2}.$$

<!-- PAGE 1948 -->
Do đó ánh xạ $\kappa$ cho trước bởi $\kappa (x, y) = (\kappa_{1} (x, y))^{2}$ là hạt nhân (kernel) ánh xạ liên kết với đặc trưng (feature)
$$\mathbb{R}^{n} \mathbb{R}^{n}$$
Ánh xạ $\phi$: $X \to \times$. đặc trưng (feature) ánh xạ $\phi$ là trực tiếp tổng quát hóa của đặc trưng (feature) ánh xạ $\phi_{2}$ của Ví dụ 53.2. ở trên lập luận là ngay lập tức được điều chỉnh để chỉ ra rằng nếu $\phi_{1}$: $X \to \mathbb{R}_{1}^{n}$ và $\phi_{2}$: $X \to \mathbb{R}_{2}^{n}$ là hai đặc trưng (feature) các ánh xạ và nếu $\kappa_{1} (x, y) = \langle \phi_{1} (x), \phi_{1} (y)\rangle$ và $\kappa_{2} (x, y) = \langle \phi_{2} (x), \phi_{2} (y)\rangle$ là tương ứng hạt nhân (kernel) các hàm, thì ánh xạ được định nghĩa bởi
$$\kappa (x, y) = \kappa_{1} (x, y)\kappa_{2} (x, y)$$
$$\mathbb{R}_{1}^{n} \times \mathbb{R}_{2}^{n}$$
Là hạt nhân (kernel) hàm cho đặc trưng (feature) không gian và đặc trưng (feature) ánh xạ
$$\phi (x)_{(i,j)} = (\phi_{1} (x))_{i}(\phi_{2} (x))_{j},1 \le i \le n_{1}, 1 \le j \le n_{2}.$$
$$\mathbb{R}^{n} \mathbb{R}^{n}$$

> **Ví dụ 53.4.** Lưu ý rằng đặc trưng (feature) ánh xạ $\phi$: $X \to \times$ là không rất economical bởi vì nếu i̸ $= j$ thì các thành phần $\phi_{(i,j)} (x)$ và $\phi_{(j,i)} (x)$ là cả hai bằng $(\phi_{1} (x))_{i}(\phi_{1} (x))_{j}$.
$$\mathbb{R}(_{2}^{n+1} )$$
Vì vậy ta có thể định nghĩa nhiều hơn/thêm economical phép nhúng (embedding) $\phi'$: $X \to$ cho trước bởi
$$($$
$$((x))_{i}^{2}i = j,$$
$$\phi' (x)_{(i,j)} =\sqrt \frac{\phi_{1}}{2(} \phi_{1} (x))_{i}(\phi_{1} (x))_{j}i < j,$$
Ở đâu các cặp $(i, j)$ với $1 \le i \le j \le n$ được thứ tự lexicographically. đặc trưng (feature) ánh xạ $\phi$ là trực tiếp tổng quát hóa của đặc trưng (feature) ánh xạ $\phi_{1}$ của Ví dụ 53.2. Nhận thấy rằng $\phi'$ có thể cũng được định nghĩa trong sau đây cách mà làm cho nó dễ hơn đến đến lên với tổng quát hóa đến bất kỳ lũy thừa:
$$1/2$$
$$\phi_{(i1,...,in)}' (x) = \begin{pmatrix} 2 \\ i_{1} \cdots  i_{n} \end{pmatrix} (\phi_{1} (x))_{1}^{i1} (\phi_{1} (x))_{1}^{i2} \cdots  (\phi_{1} (x))_{1}^{in} ,i_{1} + i_{2} + \cdots  + i_{n} = 2, i_{j} \in \mathbb{N},$$
Ở đâu các bộ $n$ $(i_{1}, \dots  , i_{n})$ được thứ tự lexicographically. Nhắc lại rằng với mọi $m \ge 1$ và
$$\mathbb{N}^{m}$$
Bất kỳ $(i_{1}, \dots  , i_{n}) \in$ sao cho $i_{1} + i_{2} + \cdots  + i_{n} = m$, ta có
$$\begin{pmatrix} m \\ i_{1} \cdots  i_{n} \end{pmatrix} = \frac{m!}{i_{1}! \cdots  i_{n}!} .$$
Tổng quát hơn, với mọi $m \ge 2$, bằng cách sử dụng multinomial định lý, ta có thể định nghĩa đặc trưng (feature)
$$\mathbb{R}(_{m}^{n+m-1})$$
Phép nhúng (embedding) $\phi$: $X \to$ định nghĩa hạt nhân (kernel) hàm $\kappa$ cho trước bởi $\kappa (x, y) = (\kappa_{1} (x, y))^{m}$, với $\phi$ cho trước bởi
$$1/2$$
$$\phi_{(i1,...,in)} (x) = \begin{pmatrix} m \\ i_{1} \cdots  i_{n} \end{pmatrix} (\phi_{1} (x))_{1}^{i1} (\phi_{1} (x))_{1}^{i2} \cdots  (\phi_{1} (x))_{1}^{in} ,i_{1} + i_{2} + \cdots  + i_{n} = m, i_{j} \in \mathbb{N},$$
Ở đâu các bộ $n$ $(i_{1}, \dots  , i_{n})$ được thứ tự lexicographically.

<!-- PAGE 1949 -->

> **Ví dụ 53.5.** Với mọi dương thực hằng số $R > 0$, hằng số hàm $\kappa (x, y  R$ là
$$a kernel function corresponding to the feature map \phi : X \to \mathbb{R} given by \phi (x, y) =\sqrt \frac{) =}{R.}$$
$$\mathbb{R}^{n} \mathbb{R}$$
Theo Định nghĩa, hàm $\kappa_{1}'$: $\to$ cho trước bởi $\kappa_{1}' (x, y) = \langle x, y\rangle$ là hạt nhân (kernel) hàm
$$\mathbb{R}^{n}$$
(đặc trưng (feature) ánh xạ là đồng nhất thức ánh xạ từ đến chính nó). Ta chỉ đã thấy rằng với mọi dương thực hằng số $R > 0$, hằng số $\kappa_{2}' (x, y) = R$ là hạt nhân (kernel) hàm. Bởi Ví dụ 53.1, hàm $\kappa_{3}' (x, y) = \kappa_{1}' (x, y) + \kappa_{2}' (x, y)$ là hạt nhân (kernel) hàm, và với mọi số nguyên $d \ge 1$, bởi Ví dụ 53.4, hàm $\kappa_{d}$ cho trước bởi
$$\kappa_{d} (x, y) = (\kappa_{3}' (x, y))^{d}= (\langle x, y\rangle + R)^{d},$$
Là hạt nhân (kernel) hàm trên $\mathbb{R}^{n}$. Bởi nhị thức công thức,
$$\kappa_{d} (x, y) = \sum_{m=0}^{d}  R^{d-m}\langle x, y\rangle^{m} .$$
Bởi Ví dụ 53.1, đặc trưng (feature) ánh xạ của hạt nhân (hạt nhân (kernel)) này hàm là concatenation của các đặc trưng của $d + 1$ hạt nhân (kernel) các ánh xạ $R^{d-m}\langle x, y\rangle^{m}$. Bởi Ví dụ 53.3, các thành phần của đặc trưng (feature) ánh xạ của hạt nhân (kernel) ánh xạ $R^{d-m}\langle x, y\rangle^{m}$ là reweightings của các hàm
$$\phi_{(i1,...,in)} (x) = x_{1}^{i1} x_{2}^{i2} \cdots  x_{n}^{in} ,i_{1} + i_{2} + \cdots  + i_{n} = m,$$
Với $(i_{1}, \dots  , i_{n}) \in \mathbb{N}^{n}$. Do đó các thành phần của đặc trưng (feature) ánh xạ của hạt nhân (kernel) hàm $\kappa_{d}$ là reweightings của các hàm
$$\phi_{(i1,...,in)} (x) = x_{1}^{i1} x_{2}^{i2} \cdots  x_{n}^{in} ,i_{1} + i_{2} + \cdots  + i_{n} \le d,$$
$$with (i_{1}, \dots  , i_{n}) \in \mathbb{N}^{n}. It is easy to see that the dimension of this feature space \begin{pmatrix} is_{d}^{m+d} \\ embedding \end{pmatrix} .$$
Có số của variations của đa thức hạt nhân (kernel) $\kappa_{d}$; all-subsets các hạt nhân, ANOVA các hạt nhân; xem Shawe–Taylor và Christianini $[165]$, Chương III. Trong tiếp theo ví dụ tập hợp $X$ là không không gian vectơ (vector space).

> **Ví dụ 53.6.** Cho $D$ là hữu hạn tập hợp và cho $X = 2^{D}$ là của nó lũy thừa tập hợp. Nếu |D| $= n$,
$$\mathbb{R}^{X} \sim  \mathbb{R}^{2n}$$
Cho $H = =$. Ta là giả sử rằng các tập con của $D$ là enumerated trong một số cách thức sao cho mỗi tọa độ của $\mathbb{R}^{2n}$ tương ứng với một của các phần tử này các tập con. Ví dụ, nếu $D = {1, 2, 3, 4}$, cho $U_{1} = \emptyset U_{2} = {1} U_{3} = {2} U_{4} = {3} U_{5} = {4} U_{6} = {1, 2} U_{7} = {1, 3} U_{8} = {1, 4} U_{9} = {2, 3} U_{10} = {2, 4} U_{11} = {3, 4} U_{12} = {1, 2, 3} U_{13} = {1, 2, 4} U_{14} = {1, 3, 4} U_{15} = {2, 3, 4} U_{16} = {1, 2, 3, 4}$. Cho $\phi$: $X \to H$ là đặc trưng (feature) ánh xạ được định nghĩa như sau: với mọi các tập con $A, U \in X$,
$$($$
$$1if U \subseteq A$$
$$\phi (A)_{U} =$$
$$0otherwise.$$

<!-- PAGE 1950 -->
Ví dụ, nếu $A_{1} = {1, 2, 3}$, ta thu được vectơ
$$\phi ({1, 2, 3}) = (1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0),$$
Và nếu $A_{2} = {2, 3, 4}$, ta thu được vectơ
$$\phi ({2, 3, 4}) = (1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0).$$
Với mọi hai các tập con $A_{1}$ và $A_{2}$ của $D$, nó là dễ để kiểm tra rằng
$$\langle \phi (A_{1}), \phi (A_{2})\rangle = 2^{|A1\cap A2|},$$
Số của chung/phổ biến các tập con của $A_{1}$ và $A_{2}$. Ví dụ, $A_{1} \cap A_{2} = {2, 3}$, và
$$\langle \phi (A_{1}), \phi (A_{2})\rangle = 4.$$
Vì vậy, hàm $\kappa$: $X \times  X \to \mathbb{R}$ cho trước bởi
$$\kappa (A_{1}, A_{2}) = 2^{|A1\cap A2|},A_{1}, A_{2} \subseteq D$$
Là hạt nhân (kernel) hàm. Các hạt nhân trên các họ của các tập hợp có thể được được định nghĩa theo measures.

> **Ví dụ 53.7.** Cho $(D,\mathcal{A})$ là measurable không gian, ở đâu $D$ là khác rỗng tập hợp và $\mathcal{A}$ là $a \sigma$ -đại số trên $D$ (measurable các tập hợp). Cho $X$ là tập con của $\mathcal{A}$. Nếu $\mu$ là dương measure trên $(D,\mathcal{A})$ và nếu $\mu$ là hữu hạn, mà có nghĩa là $\mu (D)$ là hữu hạn, thì ta có thể định nghĩa ánh xạ $\kappa_{1}$: $X \times  X \to \mathbb{R}$ cho trước bởi
$$\kappa_{1} (A_{1}, A_{2}) = \mu (A_{1} \cap A_{2}),A_{1}, A_{2} \in X.$$
Ta có thể chỉ ra rằng $\kappa$ là hạt nhân (kernel) hàm như sau. Cho $H = L_{\mu}^{2}(D,\mathcal{A},\mathbb{R})$ là Không gian Hilbert (Hilbert space) của $\mu$ -square-integrable các hàm với tích vô hướng (inner product)
$$\langle f, g\rangle = \int_{D}  f(s)g(s) d\mu (s),$$
Và cho $\phi$: $X \to H$ là đặc trưng (feature) phép nhúng (embedding) cho trước bởi
$$\phi (A) = \chi_{A} ,A \in X,$$
Characteristic hàm của $A$. Thì ta có
$$\kappa_{1} (A_{1}, A_{2}) = \mu (A_{1} \cap A_{2}) = \int_{D}  \chi_{A1\cap A2} (s) d\mu (s)$$
$$= \int_{D}  \chi_{A1} (s)\chi_{A2} (s) d\mu (s) = \langle \chi_{A1} , \chi_{A2} \rangle$$
$$= \langle \phi (A_{1}), \phi (A_{2})\rangle .$$

<!-- PAGE 1951 -->
Ở trên hạt nhân (kernel) được gọi là giao hạt nhân (kernel). Nếu ta giả sử rằng $\mu$ được chuẩn hóa sao cho $\mu (D) = 1$, thì ta cũng có hợp phần bù hạt nhân (kernel):
$$\kappa_{2} (A_{1}, A_{2}) = \mu (\overline{A}_{1} \cap \overline{A}_{2}) = 1 -\mu (A_{1} \cup A_{2}).$$
Tổng $\kappa_{3}$ của các hạt nhân $\kappa_{1}$ và $\kappa_{2}$ là agreement hạt nhân (kernel):
$$\kappa_{s} (A_{1}, A_{2}) = 1 -\mu (A_{1} -A_{2}) -\mu (A_{2} -A_{1}).$$
Nhiều khác các loại của các hạt nhân có thể được designed, đặc biệt, đồ thị các hạt nhân. Cho toàn diện các trình bày của các hạt nhân, xem Sch¨olkopf và Smola $[151]$ và Shawe–Taylor và Christianini $[165]$. Hạt nhân (kernel) các hàm có sau đây quan trọng tính chất.

> **Mệnh đề 53.1.** Cho $X$ là bất kỳ khác rỗng tập hợp, cho $H$ là bất kỳ (phức) Không gian Hilbert (Hilbert space), cho $\phi$: $X \to H$ là bất kỳ hàm, và cho $\kappa$: $X \times  X \to \mathbb{C}$ là hạt nhân (kernel) cho trước bởi
$$\kappa (x, y) = \langle \phi (x), \phi (y)\rangle ,x, y \in X.$$
Với mọi hữu hạn tập con $S = {x_{1}, \dots  , x_{p}}$ của $X$, nếu $K_{S}$ là ma trận cỡ $p \times  p$
$$K_{S} = (\kappa (x_{j}, x_{i}))_{1\le i,j\le p} = (\langle \phi (x_{j}), \phi (x_{i})\rangle )_{1\le i,j\le p},$$
Thì ta có
$$u^{*}K_{S} u \ge 0,for all u \in \mathbb{C}^{p}.$$

*Chứng minh.* Ta có
$$u^{*}K_{S} u = u^{\top}K_{S}^{\top} \overline{u} = \sum_{i,j=1}^{p}  \kappa (x_{i}, x_{j})u_{i}\overline{u}_{j}$$
$$= \sum_{i,j=1}^{p}  \langle \phi (x), \phi (y)\rangle u_{i}\overline{u}_{j}$$
$$*+2$$
$$= \sum_{i=1}^{p}  u_{i}\phi (x_{i}), \sum_{j=1}^{p}  u_{j}\phi (x_{j})= \sum_{i=1}^{p}  u_{i}\phi (x_{i})\ge 0,$$
Như đã khẳng định.
