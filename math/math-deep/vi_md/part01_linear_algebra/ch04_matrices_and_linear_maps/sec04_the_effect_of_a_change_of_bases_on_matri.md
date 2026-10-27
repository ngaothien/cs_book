# Effect của Thay đổi của Các cơ sở trên Các ma trận


<!-- PAGE 141 -->
Vì vậy, các tọa độ của đa thức $2x^{3}$ - $x + 1$ trên cơ sở (basis) $\mathcal{V}$ là
$$\begin{pmatrix} 1 \\ 2/3 \\ 1/3 \\ 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1/3 & 0 & 0 \\ 1 & 2/3 & 1/3 & 0 \\ 1 & 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \\ 0 \\ 2 \end{pmatrix} ,$$
Và do đó
$$2x^{3}-x + 1 = B_{0}^{3}(x) + \frac{2}{3} B_{1}^{3}(x) + \frac{1}{3} B_{2}^{3}(x) + 2B_{3}^{3}(x).$$

## 4.4 Effect của Thay đổi của Các cơ sở trên Các ma trận

Effect của thay đổi của các cơ sở trên biểu diễn của ánh xạ tuyến tính (linear map) được mô tả trong sau đây mệnh đề.

> **Mệnh đề 4.5.** Cho $E$ và $F$ là các không gian vectơ, cho $\mathcal{U} = (u_{1}, \dots  , u_{n})$ và $\mathcal{U}' = (u_{1}', \dots  , u_{n}')$ là hai các cơ sở của $E$, và cho $\mathcal{V} = (v_{1}, \dots  , v_{m})$ và $\mathcal{V}' = (v_{1}', \dots  , v_{m}')$ là hai các cơ sở của $F$. Cho $P = P_{U',U}$ là ma trận chuyển cơ sở (change of basis matrix) từ $\mathcal{U}$ đến $\mathcal{U}'$, và cho $Q = P_{V',V}$ là ma trận chuyển cơ sở (change of basis matrix) $from\mathcal{V} to\mathcal{V}'$. Với mọi ánh xạ tuyến tính (linear map) $f$: $E \to F$, cho M(f) $= M_{U,V}(f)$ là ma trận liên kết với $f$ w.r.t. các cơ sở $\mathcal{U}$ và $\mathcal{V}$, và cho M' $(f) = M_{U',V'}(f)$ là ma trận liên kết với $f$ w.r.t. các cơ sở $\mathcal{U}'$ và $\mathcal{V}'$. Ta có
$$M' (f) = Q^{-1}M(f)P,$$
Hoặc nhiều hơn/thêm một cách tường minh
$$M_{U',V'}(f) = P_{V',V}^{-1} M_{U,V}(f)P_{U',U} = P_{V,V'}M_{U,V}(f)P_{U',U}.$$

*Chứng minh.* Vì $f$: $E \to F$ có thể được viết dưới dạng $f = id_{F} \circ f \circ id_{E}$, vì $P = P_{U',U}$ là ma trận của $id_{E}$ w.r.t. các cơ sở $(u_{1}', \dots  , u_{n}')$ và $(u_{1}, \dots  , u_{n})$, và $Q^{-1} = P_{V'}^{-1}  = P_{V,V'}$ là ma trận của $id_{F}$ w.r.t. các cơ sở $(v_{1}, \dots  , v_{m})$ và $(v_{1}', \dots  , v_{m}')$ như được minh họa $by^{,V}$ sau đây biểu đồ
$$f\mathcal{V}/$$
$$\mathcal{U}, E, F$$
$$\overline{M}\mathcal{U},\mathcal{V}\overline{(}\overline{f}\overline{)}$$
$$PidP-1id$$
$$U',\mathcal{U} E 'F$$
$$\mathcal{V},\mathcal{V}$$
$$\mathcal{U}', E_{f}^{MU',V'(f)}\mathcal{V}'/, F,$$
Theo Mệnh đề 4.2, ta có M' $(f) = Q^{-1}M(f)P$. Như hệ quả, ta thu được kết quả sau đây.

<!-- PAGE 142 -->

> **Hệ quả 4.6.** Cho $E$ là không gian vectơ (vector space), và cho $\mathcal{U} = (u_{1}, \dots  , u_{n})$ và $\mathcal{U}' = (u_{1}', \dots  , u_{n}')$ là hai các cơ sở của $E$. Cho $P = P_{U',U}$ là ma trận chuyển cơ sở (change of basis matrix) từ $\mathcal{U}$ đến $\mathcal{U}'$. Với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$, cho M(f) $= M_{U}(f)$ là ma trận liên kết với $f$ w.r.t. cơ sở (basis) $\mathcal{U}$, và cho M' $(f) = M_{U'}(f)$ là ma trận liên kết với $f$ w.r.t. cơ sở (basis) $\mathcal{U}'$. Ta có
$$M' (f) = P^{-1} M(f)P,$$
Hoặc nhiều hơn/thêm một cách tường minh,
$$M_{U'}(f) = P_{U',U}^{-1} M_{U}(f)P_{U',U} = P_{U,U'}M_{U}(f)P_{U',U},$$
Như được minh họa bởi sau đây biểu đồ
$$f\mathcal{U}/$$
$$\mathcal{U}, E, E$$
$$\overline{M}\mathcal{U},\overline{(}\overline{f}\overline{)}$$
$$PidP-1id$$
$$U',\mathcal{U} E 'E$$
$$\mathcal{U},\mathcal{U}$$
$$MU'(f)\mathcal{U}'/$$
$$\mathcal{U}', E, E.$$
$$\overline{f}$$

> **Ví dụ 4.3.** Cho $E =\mathbb{R}^{2}, \mathcal{U} = (e_{1}, e_{2})$ ở đâu $e_{1} = (1, 0)$ và $e_{2} = (0, 1)$ là cơ sở chính tắc (canonical basis) các vectơ, cho $\mathcal{V} = (v_{1}, v_{2}) = (e_{1}, e_{1}$ - $e_{2})$, và cho
$$A = \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix} .$$
Ma trận chuyển cơ sở (change of basis matrix) $P = P_{V,U}$ từ $\mathcal{U}$ đến $\mathcal{V}$ là
$$P = \begin{pmatrix} 1 & 1 \\ 0 & -1 \end{pmatrix} ,$$
Và ta kiểm tra rằng
$$P^{-1}= P.$$
Vì vậy, trong cơ sở (basis) $\mathcal{V}$, ma trận biểu diễn ánh xạ tuyến tính (linear map) $f$ được định nghĩa bởi $A$ là
$$A'= P^{-1}AP = PAP = \begin{pmatrix} 1 & 1 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix} = D,$$
Ma trận đường chéo (diagonal matrix). Trong cơ sở (basis) $\mathcal{V}$, nó là rõ ràng những gì action của $f$ là: nó là stretch bởi nhân tử của $2$ trong $v_{1}$ hướng và nó là đồng nhất thức trong $v_{2}$ hướng. Nhận thấy rằng $v_{1}$ và $v_{2}$ là không trực giao. Những gì được xảy ra là rằng ta được chéo hóa ma trận $A$. đường chéo các phần tử (entries) $2$ và $1$ là các trị riêng (eigenvalues) của $A$ (và $f)$, và $v_{1}$ và $v_{2}$ là tương ứng các vectơ riêng (eigenvectors). Ta sẽ đến quay lại đến các trị riêng (eigenvalues) và các vectơ riêng (eigenvectors) sau này.

<!-- PAGE 143 -->

> **Ví dụ 4.4.** Cho $E =\mathbb{R}^{2}, \mathcal{U} = (e_{1}, e_{2})$ ở đâu $e_{1} = (1, 0)$ và $e_{2} = (0, 1)$ là cơ sở chính tắc (canonical basis) các vectơ, cho
$$\mathcal{V} = (v_{1}, v_{2}),withv_{1} = \begin{pmatrix} \cos \phi /2 \\ \sin \phi /2 \end{pmatrix} ,v_{2} = \begin{pmatrix} -\sin \phi /2 \\ \cos \phi /2 \end{pmatrix} ,$$
Và cho $A$ là phép đối xứng (reflection) về đường thẳng tạo ra góc $\phi /2$ với trục $x$ (xem Ví dụ 2.4) cho trước bởi
$$A = \begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix} .$$
Ma trận chuyển cơ sở (change of basis matrix) $P = P_{V,U}$ từ $\mathcal{U}$ đến $\mathcal{V}$ là
$$P = \begin{pmatrix} \cos \phi /2 & -\sin \phi /2 \\ \sin \phi /2 & \cos \phi /2 \end{pmatrix}$$
Và ta kiểm tra rằng
$$P^{-1}= P^{\top}.$$
Bằng cách sử dụng ký hiệu của Ví dụ 2.4, $A = \rho_{\phi}$ và $P$ là ma trận quay (rotation matrix) $P = M_{\phi /2}$. Vì ta được chứng minh rằng
$$\rho_{\phi}  = M_{\phi /2}\rho_{0} M_{-\phi /2}$$
Và nghịch đảo của $M_{\phi /2}$ là $M_{-\phi /2}$, ta thu được
$$M_{-\phi /2}\rho_{\phi} M_{\phi /2} = \rho_{0} .$$
Vì vậy, trong cơ sở (basis) $\mathcal{V}$, ma trận biểu diễn ánh xạ tuyến tính (linear map) $f$ được định nghĩa bởi $A$ là ' $= P^{-1}AP = P^{\top}AP = M_{-\phi /2}\rho_{\phi} M_{\phi /2}$
$$= \begin{pmatrix} \cos \phi /2 & \sin \phi /2 \\ -\sin \phi /2 & \cos \phi /2 \end{pmatrix} \begin{pmatrix} \cos \phi & \sin \phi \\ \sin \phi & -\cos \phi \end{pmatrix} \begin{pmatrix} \cos \phi /2 & -\sin \phi /2 \\ \sin \phi /2 & \cos \phi /2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \rho_{0} ,$$
Ma trận đường chéo (diagonal matrix). Trong cơ sở (basis) $\mathcal{V}$, ma trận $\rho_{0}$ là phép đối xứng (reflection) về trục $x$ (xem Ví dụ 2.4). Trong concrete trường hợp ở đâu $\phi  = \pi /2$,
$$A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$
Là phép đối xứng (reflection) về đường thẳng của phương trình $y = x$ tạo ra góc $\pi /4$ với x-axix và
$$P = \begin{pmatrix} \sqrt & \sqrt \\ \sqrt{2}/2 & -\sqrt{2}/2 \\ 2/2 & 2/2 \end{pmatrix} .$$
Ở trên các ví dụ chỉ ra rằng cùng ánh xạ tuyến tính (linear map) có thể được biểu diễn bởi khác nhau các ma trận. Điều này suggests tạo ra sau đây định nghĩa:

<!-- PAGE 144 -->

> **Định nghĩa 4.5.** hai ma trận cỡ $n\times n$ $A$ và $B$ được nói là đồng dạng khi và chỉ khi tồn tại một ma trận khả nghịch (invertible matrix) $P$ sao cho
$$B = P^{-1} AP.$$
Nó là dễ dàng đã kiểm tra rằng sự đồng dạng là quan hệ tương đương (equivalence relation). Từ của ta trước đó considerations, hai ma trận cỡ $n \times  n$ $A$ và $B$ là đồng dạng khi và chỉ khi chúng biểu diễn cùng ánh xạ tuyến tính (linear map) đối với hai khác nhau các cơ sở. sau đây đáng ngạc nhiên sự kiện có thể được được hiển thị: Mọi ma trận vuông (square matrix) $A$ là đồng dạng đến của nó chuyển vị (transpose) $A^{\top}$. chứng minh đòi hỏi advanced các khái niệm (Dạng Jordan (Jordan form) hoặc sự đồng dạng các bất biến). Nếu $\mathcal{U} = (u_{1}, \dots  , u_{n})$ và $\mathcal{V} = (v_{1}, \dots  , v_{n})$ là hai các cơ sở của $E$, ma trận chuyển cơ sở (change of basis matrix)
$$P = P_{V,U} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{pmatrix}$$
Từ $(u_{1}, \dots  , u_{n})$ đến $(v_{1}, \dots  , v_{n})$ là ma trận có cột thứ $j$ bao gồm của các tọa độ của $v_{j}$ trên cơ sở (basis) $(u_{1}, \dots  , u_{n})$, mà có nghĩa là
$$v_{j} = \sum_{i=1}^{n}  a_{ij}u_{i}.$$
$$It is natural to extend the matrix notation and to express the vector \begin{pmatrix} v_{1} \\ \vdots \\ v_{n} \end{pmatrix} in E^{n} as the$$
$$product of a matrix times the vector \begin{pmatrix} u_{1} \\ \vdots \\ u_{n} \end{pmatrix} in E^{n}, namely as$$
$$\begin{pmatrix} v_{1} \\ v_{2} \\ \vdots \\ v_{n} \end{pmatrix} = \begin{pmatrix} a_{11} & a_{21} & \cdots & a_{n1} \\ a_{12} & a_{22} & \cdots & a_{n2} \\ \vdots & \vdots & \ddots & \vdots \\ a_{1n} & a_{2n} & \cdots & a_{nn} \end{pmatrix} \begin{pmatrix} u_{1} \\ u_{2} \\ \vdots \\ u_{n} \end{pmatrix} ,$$
Nhưng chú ý rằng ma trận liên quan là không $P$, nhưng của nó chuyển vị (transpose) $P^{\top}$. Điều này nhận xét có sau đây hệ quả: nếu $\mathcal{U} = (u_{1}, \dots  , u_{n})$ và $\mathcal{V} = (v_{1}, \dots  , v_{n})$ là hai các cơ sở của $E$ và nếu
$$\begin{pmatrix} v_{1} \\ \vdots \\ v_{n} \end{pmatrix} = A \begin{pmatrix} u_{1} \\ \vdots \\ u_{n} \end{pmatrix} ,$$

<!-- PAGE 145 -->
Rằng là,
$$v_{i} = \sum_{j=1}^{n}  a_{ij}u_{j},$$
Với mọi vectơ $w \in E$, ta có
$$w = \sum_{i=1}^{n}  x_{i}u_{i} = \sum_{k=1}^{n}  y_{k}v_{k} = \sum_{k=1}^{n}  y_{k} \begin{pmatrix} a_{kj}u_{j} \end{pmatrix} \sum_{j=1}^{n}  = \sum_{j=1}^{n}  \begin{pmatrix} a_{kj}y_{k} \end{pmatrix} \sum_{k=1}^{n}  u_{j},$$
Do đó
$$x_{i} = \sum_{k=1}^{n}  a_{kj}y_{k},$$
Mà có nghĩa là (lưu ý inevitable phép chuyển vị) rằng
$$\begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix} = A^{\top} \begin{pmatrix} y_{1} \\ \vdots \\ y_{n} \end{pmatrix} ,$$
Và do đó
$$\begin{pmatrix} y_{1} \\ \vdots \\ y_{n} \end{pmatrix} = (A^{\top})^{-1} \begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix} .$$
Nó là dễ để xem rằng $(A^{\top})^{-1} = (A^{-1})^{\top}$. Cũng, nếu $\mathcal{U} = (u_{1}, \dots  , u_{n}), \mathcal{V} = (v_{1}, \dots  , v_{n})$, và $\mathcal{W} = (w_{1}, \dots  , w_{n})$ là ba các cơ sở của $E$, và nếu ma trận chuyển cơ sở (change of basis matrix) từ $\mathcal{U}$ đến $\mathcal{V}$ là $P = P_{V,U}$ và ma trận chuyển cơ sở (change of basis matrix) từ $\mathcal{V}$ đến $\mathcal{W}$ là $Q = P_{W,V}$, thì
$$\begin{pmatrix} v_{1} \\ \vdots \\ v_{n} \end{pmatrix} = P^{\top} \begin{pmatrix} u_{1} \\ \vdots \\ u_{n} \end{pmatrix} , \begin{pmatrix} w_{1} \\ \vdots \\ w_{n} \end{pmatrix} = Q^{\top} \begin{pmatrix} v_{1} \\ \vdots \\ v_{n} \end{pmatrix} ,$$
Do đó
$$\begin{pmatrix} w_{1} \\ \vdots \\ w_{n} \end{pmatrix} = Q^{\top}P^{\top} \begin{pmatrix} u_{1} \\ \vdots \\ u_{n} \end{pmatrix} = (PQ)^{\top} \begin{pmatrix} u_{1} \\ \vdots \\ u_{n} \end{pmatrix} ,$$
Mà có nghĩa là ma trận chuyển cơ sở (change of basis matrix) $P_{W,U}$ từ $\mathcal{U}$ đến $\mathcal{W}$ là PQ. Điều này chứng tỏ rằng
$$P_{W,U} = P_{V,U}P_{W,V}.$$
Nhận xét: Trong thứ tự để tránh phép chuyển vị liên quan trong viết
$$\begin{pmatrix} v_{1} \\ \vdots \\ v_{n} \end{pmatrix} = P^{\top} \begin{pmatrix} u_{1} \\ \vdots \\ u_{n} \end{pmatrix} ,$$

<!-- PAGE 146 -->
Như nhiều hơn/thêm thuận tiện ký hiệu ta có thể viết
$$\begin{pmatrix} v_{1} & \cdots & v_{n} \end{pmatrix} = \begin{pmatrix} u_{1} & \cdots & u_{n} \end{pmatrix} P.$$
Ở đây ta là định nghĩa tích
$$\begin{pmatrix} u_{1} & \cdots & u_{n} \end{pmatrix} \begin{pmatrix} p_{1j} \\ \vdots \\ p_{nj} \end{pmatrix} (*)$$
$$of a row of vectors \begin{pmatrix} u_{1} & \cdots & u_{n} \end{pmatrix} by the jth column of P as the linear combination$$
$$\sum_{i=1}^{n}  p_{ij}u_{i}.$$
Như vậy định nghĩa là cần thiết vì vô hướng (scalar) phép nhân của vectơ bởi vô hướng (scalar) là chỉ được định nghĩa nếu vô hướng (scalar) là trên trái của vectơ, nhưng trong ma trận biểu thức (*) ở trên, các vectơ là trên trái của các vô hướng! Chẵn/ngay cả dù các ma trận là indispensable vì chúng là major công cụ trong các ứng dụng của tuyến tính đại số, một nên không lose track của sự kiện rằng các ánh xạ tuyến tính (linear maps) là nhiều hơn/thêm cơ bản bởi vì chúng là nội tại
$$objects that do not depend on the choice of bases.$$
Hệ quả là, ta advise độc giả đến thử đến nghĩ theo
$$linear maps rather than reduce everything to matrices.$$
Trong của ta experience, điều này là một cách cụ thể effective khi nó đến đến chứng minh các kết quả về các ánh xạ tuyến tính (linear maps) và các ma trận, ở đâu các chứng minh liên quan đến các ánh xạ tuyến tính (linear maps) là thường nhiều hơn/thêm “conceptual.” Các phần tử này các chứng minh là thường nhiều hơn/thêm tổng quát bởi vì chúng không phụ thuộc vào sự kiện rằng số chiều là hữu hạn. Cũng, thay vì của nghĩ của ma trận phân rã như một cách thuần túy đại số phép toán, nó là thường illuminating đến quan điểm nó như hình học phân rã. Điều này là trường hợp của SVD, mà trong hình học các số hạng nói rằng rằng mọi ánh xạ tuyến tính (linear map) có thể được được nhân tử như phép quay, theo sau bởi rescaling dọc theo trực giao các trục và thì một cái khác phép quay. Sau tất cả,
$$a matrix is a representation of a linear map,$$
Và hầu hết các phân rã của ma trận reflect sự kiện rằng với phù hợp lựa chọn của cơ sở (basis) (hoặc các cơ sở), ánh xạ tuyến tính (linear map) được biểu diễn bởi ma trận có đặc biệt hình dạng. bài toán là thì để tìm như vậy các cơ sở. Vẫn, cho beginner, các ma trận có nhất định irresistible appeal, và ta confess rằng nó lấy nhất định lượng của practice đến đạt tới điểm ở đâu nó trở thành nhiều hơn/thêm tự nhiên đến
