# Đồ thị Drawing và Năng lượng Cực tiểu hóa


<!-- PAGE 737 -->
Chương $21$ Vẽ đồ thị phổ (spectral graph drawing)

## 21.1 Đồ thị Drawing và Năng lượng Cực tiểu hóa

Cho $G = (V, E)$ là một số undirected đồ thị. Nó là thường desirable đến draw đồ thị, thường trong mặt phẳng nhưng có thể trong 3D, và hóa ra là toán tử Laplace của đồ thị (graph Laplacian) có thể được sử dụng để design đáng ngạc nhiên là tốt các phương pháp. Nói |V | $= m$. ý tưởng là đến assign điểm $\rho (v_{i})$ trong $\mathbb{R}^{n}$ đến đỉnh $v_{i} \in V$, với mọi $v_{i} \in V$, và đến draw đường thẳng đoạn thẳng giữa các điểm $\rho (v_{i})$ và $\rho (v_{j})$ khi và chỉ khi có một cạnh ${v_{i}, v_{j}}$.

> **Định nghĩa 21.1.** Cho $G = (V, E)$ là một số undirected đồ thị với $m$ các đỉnh. đồ thị drawing là hàm $\rho$: $V \to \mathbb{R}^{n}$, với một số $n \ge 1$. ma trận của đồ thị drawing $\rho$ (trong $\mathbb{R}^{n})$ là một ma trận cỡ $m \times  n$ $R$ có hàng thứ $i$ bao gồm của vectơ hàng (row vector) $\rho (v_{i})$ tương ứng với điểm biểu diễn $v_{i}$ trong $\mathbb{R}^{n}$. Cho đồ thị drawing là hữu ích ta muốn $n \le m$; thực ra $n$ nên là nhiều nhỏ hơn hơn $m$, typically $n = 2$ hoặc $n = 3$.

> **Định nghĩa 21.2.** đồ thị drawing là balanced khi và chỉ khi tổng của các phần tử (entries) của mọi cột của ma trận của đồ thị drawing là không, nghĩa là,
$$1^{\top}R = 0.$$
Nếu đồ thị drawing là không balanced, nó có thể được được tạo balanced bởi phù hợp phép tịnh tiến. Ta có thể cũng giả sử rằng các cột của $R$ là độc lập tuyến tính (linearly independent), vì bất kỳ cơ sở (basis) của cột không gian cũng xác định drawing. Do đó, từ bây giờ trên, ta có thể giả sử rằng $n \le m$.
$$\mathbb{R}^{n}$$
Nhận xét: $A$ đồ thị drawing $\rho$: $V \to$ là không cần thiết là đơn ánh (injective), mà có thể kết quả trong suy biến drawings ở đâu phân biệt các đỉnh là drawn như cùng điểm. Cho điều này lý do, ta ưu tiên không để sử dụng thuật ngữ đồ thị phép nhúng (embedding), mà là thường được sử dụng trong literature. Điều này là bởi vì trong vi phân hình học, phép nhúng (embedding) luôn luôn refers đến đơn ánh (injective) ánh xạ. số hạng đồ thị phép dìm (immersion) sẽ là nhiều hơn/thêm thích hợp.
$$737$$

<!-- PAGE 738 -->
Như được giải thích trong Godsil và Royle $[80]$, ta có thể imagine xây dựng vật lý mô hình của $G$ bởi connecting kề nhau các đỉnh (trong $\mathbb{R}^{n})$ bởi đồng nhất springs. Thì nó là tự nhiên đến xét biểu diễn là tốt hơn nếu nó đòi hỏi springs là ít hơn được mở rộng. Ta có thể formalize điều này bởi định nghĩa năng lượng của drawing $R$ bởi
$$\mathcal{E}(R) = \sum_{vi,vj}\in}  \|\rho (v_{i}) -\rho (v_{j})\|^{2},$$
$${E$$
Ở đâu $\rho (v_{i})$ là hàng thứ $i$ của $R$ và $\|\rho (v_{i})$ - $\rho (v_{j})\|^{2}$ là square của Euclidean độ dài của đường thẳng đoạn thẳng joining $\rho (v_{i})$ và $\rho (v_{j})$. Thì, “tốt drawings” là drawings rằng cực tiểu hóa năng lượng $function\mathcal{E}$. Của course, tầm thường biểu diễn tương ứng với không ma trận là tối ưu, do đó ta cần đến impose extra các ràng buộc đến quy tắc ra tầm thường nghiệm. Ta có thể xét nhiều hơn/thêm tổng quát tình huống ở đâu springs là không nhất thiết đồng nhất. Điều này có thể được được mô hình bởi đối xứng trọng số (hoặc stiffness) ma trận $W = (w_{ij})$, với $w_{ij} \ge 0$. Thì của ta năng lượng hàm trở thành
$$\mathcal{E}(R) = \sum_{vi,vj}\in}  w_{ij} \|\rho (v_{i}) -\rho (v_{j})\|^{2}.$$
$${E$$
Hóa ra là hàm này có thể được được biểu diễn theo Laplacian $L = D$ - $W$. sau đây mệnh đề được hiển thị trong Godsil và Royle $[80]$. Ta cho slightly nhiều hơn/thêm chứng minh trực tiếp.

> **Mệnh đề 21.1.** Cho $G = (V, W)$ được trọng số đồ thị, với |V | $= m$ và $W$ $m \times  m$
$$\mathbb{R}^{n}$$
Ma trận đối xứng (symmetric matrix), và cho $R$ là ma trận của đồ thị drawing $\rho$ của $G$ trong (một ma trận cỡ $m\times n$). Nếu $L = D$ - $W$ là chưa chuẩn hóa Laplacian ma trận liên kết với $W$, thì
$$\mathcal{E}(R) = \mathrm{tr}(R^{\top}LR).$$

*Chứng minh.* Vì $\rho (v_{i})$ là hàng thứ $i$ của $R$ (và $\rho (v_{j})$ là hàng thứ $j$ của $R)$, nếu ta ký hiệu cột thứ $k$ của $R$ bởi $R^{k}$, bằng cách sử dụng Mệnh đề 20.4, ta có
$$\mathcal{E}(R) = \sum_{vi,vj}\in}  w_{ij} \|\rho (v_{i}) -\rho (v_{j})\|^{2}$$
$$E$$
$$= \sum_{k=1{}^{{n}  \sum_{vi,vj}\in}  w_{ij}(R_{ik} -R_{jk})^{2}$$
$$E$$
$$= \sum_{k=1}^{n}  \frac{1}{2} \sum_{i,j=1}^{m}  w_{ij}(R_{ik} -R_{jk})^{2}$$
$$= \sum_{k=1}^{n}  (R^{k})^{\top}LR^{k} = \mathrm{tr}(R^{\top}LR),$$
Như đã khẳng định.

<!-- PAGE 739 -->
Vì ma trận $R^{\top}LR$ là đối xứng, nó có thực các trị riêng (eigenvalues). Thực sự, vì $L$ là nửa xác định dương (positive semidefinite), do đó là $R^{\top}LR$. Thì vết (trace) của $R^{\top}LR$ bằng tổng của của nó dương các trị riêng (eigenvalues), và điều này là năng lượng $\mathcal{E}(R)$ của đồ thị drawing. Nếu $R$ là ma trận của đồ thị drawing trong $\mathbb{R}^{n}$, thì với mọi $n \times  n$ ma trận khả nghịch (invertible matrix) $M$, ánh xạ rằng assigns $\rho (v_{i})M$ đến $v_{i}$ là một cái khác đồ thị drawing của $G$, và các phần tử này hai drawings convey cùng lượng của information. Từ điều này điểm của quan điểm, đồ thị drawing được xác định bởi cột không gian của $R$. Vì vậy, nó là reasonable giả sử rằng các cột của $R$ là đôi một trực giao và rằng chúng có unit độ dài. Như vậy ma trận thỏa mãn phương trình $R^{\top}R =$ I.

> **Định nghĩa 21.3.** Nếu ma trận $R$ của đồ thị drawing thỏa mãn phương trình $R^{\top}R =$ I, thì tương ứng drawing được gọi là một trực giao đồ thị drawing. Điều này ở trên điều kiện cũng các quy tắc ra tầm thường drawings. Kết quả sau đây cho ta biết chúng ta cách mà để tìm cực tiểu năng lượng trực giao balanced đồ thị drawings, miễn là/được cung cấp đồ thị là liên thông. Nhắc lại rằng
$$L1 = 0,$$
Như ta đã được quan sát.

> **Định lý 21.2.** Cho $G = (V, W)$ được trọng số đồ thị với |V | $= m$. Nếu $L = D$ - $W$ là
(chưa chuẩn hóa) Laplacian của $G$, và nếu các trị riêng (eigenvalues) của $L$ là $0 = \lambda_{1}  < \lambda_{2}  \le \lambda_{3}  \le \dots  \le \lambda_{m}$,
$$\mathbb{R}^{n}$$
Thì tối tiểu năng lượng của bất kỳ balanced trực giao đồ thị drawing của $G$ trong bằng $\lambda_{2} +\cdots +\lambda_{n+1}$ (đặc biệt, điều này suy ra rằng $n < m)$. ma trận cỡ $m\times n$ $R$ bao gồm của bất kỳ unit các vectơ riêng (eigenvectors) $u_{2}, \dots  , u_{n+1}$ liên kết với $\lambda_{2}  \le \dots  \le \lambda_{n+1}$ cho ta balanced trực giao đồ thị drawing của tối tiểu năng lượng; nó thỏa mãn điều kiện $R^{\top}R =$ I.

*Chứng minh.* Ta trình bày chứng minh cho trước trong Godsil và Royle $[80]$ (Mục 13.4, Định lý 13.4.1). then chốt điểm là rằng tổng của $n$ nhỏ nhất các trị riêng (eigenvalues) của $L$ là thấp hơn cận cho $tr(R^{\top}LR)$. Điều này có thể được được hiển thị bằng cách sử dụng Rayleigh tỉ số lập luận; xem Mệnh đề 17.25 (Poincar´e separation định lý). Thì bất kỳ $n$ các vectơ riêng (eigenvectors) $(u_{1}, \dots  , u_{n})$ liên kết với $\lambda_{1} , \dots  , \lambda_{n}$ đạt được điều này cận. Bởi vì thứ nhất trị riêng (eigenvalue) của $L$ là $\lambda_{1}  = 0$ và bởi vì
$$\sqrt$$
Ta là giả sử rằng $\lambda_{2}  > 0$, ta có $u_{1} = 1/ \overline{m}$. Vì $u_{j}$ là đôi một trực giao
$$\sqrt$$
Cho $i = 2, \dots  , n$ và vì $u_{i}$ là trực giao đến $u_{1} = 1/ \overline{m}$, các phần tử (entries) trong $u_{i}$ cộng sai khác $0$. Hệ quả là, với mọi $\ell$ với $2 \le \ell \le n$, bởi xóa $u_{1}$ và bằng cách sử dụng $(u_{2}, \dots  , u_{\ell})$, ta thu được
$$\mathbb{R}^{\ell-1}$$
Balanced trực giao đồ thị drawing trong với cùng năng lượng như trực giao đồ thị drawing trong $\mathbb{R}^{\ell}$ bằng cách sử dụng $(u_{1}, u_{2}, \dots  , u_{\ell})$. Ngược lại, từ bất kỳ balanced trực giao drawing trong $\mathbb{R}^{\ell-1}  \mathbb{R}^{\ell}$ bằng cách sử dụng $(u_{2}, \dots  , u_{\ell})$, ta thu được trực giao đồ thị drawing trong bằng cách sử dụng $(u_{1}, u_{2}, \dots  , u_{\ell})$ với cùng năng lượng. Vì vậy, cực tiểu năng lượng của balanced trực giao đồ thị
$$\mathbb{R}^{n} \mathbb{R}^{n+1}$$
Drawing trong bằng cực tiểu năng lượng của trực giao đồ thị drawing trong, và điều này cực tiểu là $\lambda_{2}  + \cdots  + \lambda_{n+1}$. Vì $1$ sinh ra không gian hạch (nullspace) của $L$, bằng cách sử dụng $u_{1}$ (mà thuộc đến Ker $L)$ như một của các vectơ trong $R$ sẽ có effect rằng tất cả các điểm biểu diễn các đỉnh của $G$ sẽ có cùng
