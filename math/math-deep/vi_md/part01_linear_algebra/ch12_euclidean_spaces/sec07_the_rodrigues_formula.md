# Rodrigues Công thức


<!-- PAGE 484 -->
Nhận xét: Nó là dễ để chỉ ra rằng các điều kiện $A A^{\top} = I_{n}, A^{\top}A = I_{n}$, và $A^{-1} = A^{\top}$, là tương đương. Cho trước bất kỳ hai các cơ sở trực chuẩn $(u_{1}, \dots  , u_{n})$ và $(v_{1}, \dots  , v_{n})$, nếu $P$ là ma trận chuyển cơ sở (change of basis matrix) từ $(u_{1}, \dots  , u_{n})$ đến $(v_{1}, \dots  , v_{n})$, vì các cột của $P$ là các tọa độ
$$of the vectors v_{j} with respect to the basis (u_{1}, \dots  , u_{n}), if v_{j1} = \sum_{i1}  n=1 p_{i1j1}u_{i1} and v_{j2} =$$
$$\sum_{i2}  n=1 p_{i2j2}u_{i2}, since (u_{1}, \dots  , u_{n}) is orthonormal,$$
$$v_{j1} \cdot  v_{j2} = \sum_{i1=1i}^{n}  \sum_{2=1}^{n}  p_{i1j1}p_{i2j2}(u_{i1} \cdot  u_{i2}) = \sum_{i=1}^{n}  p_{ij1}p_{ij2},$$
Và vì $(v_{1}, \dots  , v_{n})$ là trực chuẩn, $v_{j1} \cdot  v_{j2} = \delta_{j1j2}$, do đó các cột của $P$ là trực chuẩn, và theo Mệnh đề 12.14 $(2)$, ma trận $P$ là trực giao. chứng minh của Mệnh đề 12.12 $(3)$ cũng chỉ ra rằng nếu $f$ là phép đẳng cự (isometry), thì ảnh (image) của cơ sở trực chuẩn (orthonormal basis) $(u_{1}, \dots  , u_{n})$ là cơ sở trực chuẩn (orthonormal basis). Students thường ask tại sao các ma trận trực giao là không được gọi là trực chuẩn các ma trận, vì các cột của chúng (và các hàng) là các cơ sở trực chuẩn! I có không có tốt câu trả lời, nhưng các phép đẳng cự thực hiện bảo toàn tính trực giao, và các ma trận trực giao tương ứng với các phép đẳng cự. Nhắc lại rằng định thức (determinant) det(f) của ánh xạ tuyến tính (linear map) $f$: $E \to E$ là độc lập của lựa chọn của cơ sở (basis) trong $E$. Cũng, với mọi ma trận $A \in M_{n}(\mathbb{R})$, ta có det() $= det(A^{\top})$, và với mọi hai ma trận cỡ $n \times  n$ $A$ và $B$, ta có det(AB) $=$ det() det(B). Thì nếu $f$ là phép đẳng cự (isometry), và $A$ là ma trận của nó đối với bất kỳ cơ sở trực chuẩn (orthonormal basis), $A A^{\top} = A^{\top}A = I_{n}$ suy ra rằng $det(A)^{2} = 1$, nghĩa là, hoặc det() $= 1$, hoặc det() $= -1$. Nó là cũng rõ ràng rằng các phép đẳng cự của Không gian Euclid (Euclidean space) có số chiều $n$ tạo thành nhóm, và rằng các phép đẳng cự của định thức (determinant) $+1$ tạo thành nhóm con. Điều này dẫn đến đến sau đây định nghĩa.

> **Định nghĩa 12.7.** Cho trước Không gian Euclid (Euclidean space) $E$ có số chiều $n$, tập hợp của các phép đẳng cự $f$: $E \to E$ các dạng nhóm con của GL(E) được ký hiệu bởi O(E), hoặc O(n) khi $E =\mathbb{R}^{n}$, được gọi là trực giao nhóm (của $E)$. Với mọi phép đẳng cự (isometry) $f$, ta có det(f) $= \pm 1$, ở đâu det(f) ký hiệu định thức (determinant) của $f$. các phép đẳng cự sao cho det(f) $= 1$ được gọi là các phép quay, hoặc thực sự/đúng đắn các phép đẳng cự, hoặc thực sự/đúng đắn trực giao các phép biến đổi, và chúng tạo thành nhóm con của đặc biệt tuyến tính nhóm SL(E) (và của O(E)), được ký hiệu bởi Do đó(E), hoặc Do đó(n) khi $E = \mathbb{R}^{n}$, được gọi là đặc biệt trực giao nhóm (của $E)$. các phép đẳng cự sao cho det(f) $= -1$ được gọi là suy rộng/không thực sự các phép đẳng cự, hoặc suy rộng/không thực sự trực giao các phép biến đổi, hoặc flip các phép biến đổi.

## 12.7 Rodrigues Công thức

Khi $n = 3$ và $A$ là skew ma trận đối xứng (symmetric matrix), nó là khả dĩ/có thể đến hoạt động/công trình ra tường minh công thức cho $e^{A}$. Với mọi $3 \times  3$ thực skew ma trận đối xứng (symmetric matrix)
$$A = \begin{pmatrix} 0 & -c & b \\ c & 0 & -a \\ b & a & 0 \end{pmatrix} ,$$
$$-$$

<!-- PAGE 485 -->
$$\sqrt$$
Nếu ta cho $\theta  = \overline{a}^{2} \overline{+}\overline{b}^{2} \overline{+}\overline{c}^{2}$ và
$$B = \begin{pmatrix} a^{2} & ab & ac \\ ab & b^{2} & bc \\ ac & bc & c^{2} \end{pmatrix} ,$$
Thì ta có kết quả sau kết quả đã biết như Rodrigues’ công thức $(1840)$. (thực) không gian vectơ (vector space) của $n \times  n$ skew các ma trận đối xứng được ký hiệu bởi $\mathfrak{so}(n)$.

> **Mệnh đề 12.15.** hàm mũ ánh xạ exp: $\mathfrak{so}(3) \to$ Do đó(3) được cho bởi
$$-$$
$$e^{A}= \cos \theta  I_{3} + \frac{\sin \theta}{\theta} A + \frac{(1cos \theta )}{\theta^{2}} B,$$
Hoặc, tương đương, bởi
$$-$$
$$e^{A}= I_{3} + \frac{\sin \theta}{\theta} A + \frac{(1cos \theta )}{\theta^{2}} A^{2}$$
Nếu $\theta  \neq  0$, với $e^{03} = I_{3}$. Chứng minh phác thảo. Thứ nhất nhận thấy rằng
$$A^{2}= -\theta^{2} I_{3} + B,$$
Vì
$$$$
$$0-cb$$
$$A^{2} =c0-a \begin{pmatrix} 0 & -c & b \\ c & 0 & -a \\ b & a & 0 \end{pmatrix} = \begin{pmatrix} -c^{2}-b^{2} & ba & ca \\ ab & -c^{2}-a^{2} & cb \\ ac & cb & b^{2} & a^{2} \end{pmatrix}$$
$$-ba0---$$
$$  $$
$$-a^{2}-b^{2}-c^{2}00$$
$$=0-a^{2} -b^{2} -c^{2}0+ \begin{pmatrix} a^{2} & ba & ca \\ ab & b^{2} & cb \\ ac & cb & c^{2} \end{pmatrix}$$
$$00-a^{2}-b^{2}-c^{2}$$
$$= -\theta^{2} I_{3} + B,$$
Và rằng
$$AB = BA = 0.$$
Từ ở trên, suy ra rằng
$$A^{3}= -\theta^{2} A,$$
Và với mọi $k \ge 0$,
$$A^{4k+1}= \theta^{4k} A,$$
$$A^{4k+2}= \theta^{4k} A^{2},$$
$$A^{4k+3}= -\theta^{4k+2} A,$$
$$A^{4k+4}= -\theta^{4k+2} A^{2}.$$

<!-- PAGE 486 -->
Thì chứng minh mong muốn kết quả bởi viết lũy thừa chuỗi cho $e^{A}$ và regrouping các số hạng sao cho lũy thừa chuỗi cho cos $\theta$ và sin $\theta$ chỉ ra lên. Đặc biệt
$$e^{A} = I_{3} + \sum_{p\ge1}  \frac{A^{p}}{p!} = I_{3} + \sum_{p\ge0}  \frac{A^{2p+1}}{(2p + 1)!} + \sum_{p\ge1}  \frac{A^{2p}}{(2p)!}$$
$$= I_{3} + \sum_{p\ge0}  \frac{(1)^{p}\theta^{2p}}{(2p + 1)!} -A + \sum_{p\ge1}  \frac{(1)^{p-1}\theta^{2(p-1)}}{(2p)!} -A^{2}$$
$$--$$
$$= I_{3} + \frac{A}{\theta} \sum_{p\ge0}  \frac{(1)^{p}\theta^{2p+1}}{(2p + 1)!} - \frac{A^{2}}{\theta^{2}} \sum_{p\ge1}  \frac{(1)^{p}\theta^{2p}}{(2p)!}$$
$$-$$
$$= I_{3} + \frac{\sin \theta}{\theta} A - \frac{A^{2}}{\theta^{2}} \sum_{p\ge0}  \frac{(1)^{p}\theta^{2p}}{(2p)!} + \frac{A^{2}}{\theta^{2}}$$
$$-$$
$$= I_{3} + \frac{\sin \theta}{\theta} A + \frac{(1cos \theta )}{\theta^{2}} A^{2},$$
Như đã khẳng định. ở trên các công thức là well-known các công thức biểu diễn phép quay của trục specified bởi vectơ (, $b, c)$ và góc $\theta$. Rodrigues công thức có thể được sử dụng để chỉ ra rằng hàm mũ ánh xạ exp: $\mathfrak{so}(3) \to$ Do đó(3) là toàn ánh (surjective). Cho trước bất kỳ ma trận quay (rotation matrix) $R \in$ Do đó(3), ta có kết quả sau các trường hợp:
$(1)$ trường hợp $R =$ I là tầm thường.
$(2)$ Nếu $R \neq$ I và tr(R) $\neq  -1$, thì
$$



$$
$$\exp^{-1}(R) = \frac{\theta}{2 \sin \theta} (R -R^{T}) 1 + 2 \cos \theta  = \mathrm{tr}(R).$$
(Nhắc lại rằng tr(R) $= r_{1 1} + r_{2 2} + r_{3 3}$, vết (trace) của ma trận $R)$. Thì tồn tại duy nhất một phản đối xứng $B$ với tương ứng $\theta$ thỏa mãn $0 < \theta  < \pi$ sao cho $e^{B} = R$.
$(3)$ Nếu $R \neq$ I và tr(R) $= -1$, thì $R$ là phép quay bởi góc $\pi$ và things là nhiều hơn/thêm phức tạp, nhưng ma trận $B$ có thể được tìm thấy. Ta để lại điều này phần như tốt bài tập: xem
Bài toán 17.8. phép tính của lôgarit của phép quay trong Do đó(3) như được phác thảo ở trên có các ứng dụng trong kinematics, rô-bốt học, và motion nội suy. Như immediate hệ quả của Gram–Schmidt trực chuẩn hóa quy trình, ta thu được Phân rã QR (QR-decomposition) cho các ma trận khả nghịch.
