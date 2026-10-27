# Các dạng tuyến tính và Không gian đối ngẫu (dual space)


<!-- PAGE 112 -->
Mệnh đề 3.25 chỉ ra rằng ta có thể định nghĩa phép cộng và phép nhân bởi vô hướng (scalar) trên tập hợp $E/M$ của các lớp tương đương của quan hệ tương đương (equivalence relation) $\equiv_{M}$.

> **Định nghĩa 3.25.** Cho trước bất kỳ không gian vectơ (vector space) $E$ và bất kỳ không gian con $M$ của $E$, ta định nghĩa sau đây các phép toán của phép cộng và phép nhân bởi vô hướng (scalar) trên tập hợp $E/M$ của các lớp tương đương của quan hệ tương đương (equivalence relation) $\equiv_{M}$ như sau: với mọi hai các lớp tương đương $[u], [v] \in E/M$, ta có
$$[u] + [v] = [u + v],$$
$$\lambda [u] = [\lambda u].$$
Theo Mệnh đề 3.25, ở trên các phép toán không phụ thuộc vào cụ thể lựa chọn của representatives trong các lớp tương đương $[u], [v] \in E/M$. Nó là cũng immediate để kiểm chứng rằng $E/M$ là không gian vectơ (vector space). hàm $\pi$: $E \to E/F$, được định nghĩa sao cho $\pi (u) = [u]$ với mọi $u \in E$, là toàn ánh (surjective) ánh xạ tuyến tính (linear map) được gọi là tự nhiên phép chiếu của $E$ lên $E/F$. không gian vectơ (vector space) $E/M$ được gọi là không gian thương (quotient space) của $E$ bởi không gian con $M$. Cho trước bất kỳ ánh xạ tuyến tính (linear map) $f$: $E \to F$, ta biết rằng Ker $f$ là không gian con của $E$, và ta kiểm chứng được ngay rằng Im $f$ là đẳng cấu đến không gian thương (quotient space) $E/Ker f$.

## 3.9 Các dạng tuyến tính và Không gian đối ngẫu (dual space)

Ta đã được quan sát rằng trường $K$ chính nó $(K =\mathbb{R}$ hoặc $K =\mathbb{C})$ là không gian vectơ (vector space) (trên chính nó). không gian vectơ (vector space) Hom(E, $K)$ của các ánh xạ tuyến tính (linear maps) từ $E$ đến trường $K$, các dạng tuyến tính, đóng cụ thể vai trò. Trong mục này, ta chỉ định nghĩa các dạng tuyến tính và chỉ ra rằng mọi không gian vectơ hữu hạn chiều có đối ngẫu (dual) cơ sở (basis). nhiều hơn/thêm advanced trình bày của đối ngẫu (dual) các không gian và đối ngẫu là cho trước trong Chương $11$.

> **Định nghĩa 3.26.** Cho trước không gian vectơ (vector space) $E$, không gian vectơ (vector space) Hom(E, $K)$ của các ánh xạ tuyến tính (linear maps) từ $E$ đến trường $K$ được gọi là không gian đối ngẫu (dual space) (hoặc đối ngẫu (dual)) của $E$. không gian Hom(E, $K)$ cũng được ký hiệu bởi $E^{*}$, và các ánh xạ tuyến tính (linear maps) trong $E^{*}$ được gọi là các dạng tuyến tính, hoặc covectors. không gian đối ngẫu (dual space) $E^{**}$ của không gian $E^{*}$ được gọi là bidual của $E$. Như matter của ký hiệu, các dạng tuyến tính $f$: $E \to K$ sẽ cũng được ký hiệu bởi starred ký hiệu, chẳng hạn như $u^{*}, x^{*}$, etc. Nếu $E$ là không gian vectơ (vector space) của hữu hạn số chiều $n$ và $(u_{1}, \dots  , u_{n})$ là cơ sở (basis) của $E$, với mọi dạng tuyến tính (linear form) $f^{*} \in E^{*}$, với mọi $x = x_{1}u_{1} + \cdots  + x_{n}u_{n} \in E$, bởi tính tuyến tính ta có
$$f^{*} (x) = f^{*} (u_{1})x_{1} + \cdots  + f^{*} (u_{n})x_{n}$$
$$= \lambda_{1} x_{1} + \cdots  + \lambda_{n} x_{n},$$
Với $\lambda_{i}  = f^{*} (u_{i}) \in K$ với mọi $i, 1 \le i \le n$. Do đó, đối với cơ sở (basis) $(u_{1}, \dots  , u_{n})$, dạng tuyến tính (linear form) $f^{*}$ được biểu diễn bởi vectơ hàng (row vector)
$$(\lambda_{1}  \cdots  \lambda_{n} ),$$

<!-- PAGE 113 -->
Ta có
$$f^{*} (x) = \begin{pmatrix} \lambda_{1} & \cdots & \lambda_{n} \end{pmatrix} \begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix} ,$$
Tổ hợp tuyến tính (linear combination) của các tọa độ của $x$, và ta có thể quan điểm dạng tuyến tính (linear form) $f^{*}$ như phương trình tuyến tính. Nếu ta decide để sử dụng vectơ cột (column vector) của các hệ số
$$c = \begin{pmatrix} c_{1} \\ \vdots \\ c_{n} \end{pmatrix}$$
Thay vì của vectơ hàng (row vector), thì dạng tuyến tính (linear form) $f^{*}$ được định nghĩa bởi
$$f^{*} (x) = c^{\top}x.$$
Ở trên ký hiệu là thường được sử dụng trong máy học (learning).
$$\mathbb{R}^{n} \mathbb{R}\mathbb{R}^{n}$$

> **Ví dụ 3.7.** Cho trước bất kỳ khả vi (differentiable) hàm $f$: $\to$, theo Định nghĩa, với mọi $x \in$,
$$\mathbb{R}^{n} \mathbb{R}$$
Đạo hàm toàn phần (total derivative) $df_{x}$ của $f$ tại $x$ là dạng tuyến tính (linear form) $df_{x}$: $\to$ được định nghĩa sao cho với mọi $u = (u_{1}, \dots  , u_{n}) \in \mathbb{R}^{n}$,
$$df_{x}(u) = \begin{pmatrix} \partial f \\ \partial f \\ (x) & \cdots & (x) \\ \partial x_{1} & \partial x_{n} \end{pmatrix} \begin{pmatrix} u_{1} \\ \vdots \\ u_{n} \end{pmatrix} = \sum_{i=1}^{n}  \frac{\partial f}{\partial x_{i}} (x) u_{i}.$$

> **Ví dụ 3.8.** Cho $\mathcal{C}([0, 1])$ là không gian vectơ (vector space) của liên tục các hàm $f$: $[0, 1] \to \mathbb{R}$. ánh xạ $\mathcal{I}$: $\mathcal{C}([0, 1]) \to \mathbb{R}$ cho trước bởi
$$\mathcal{I}(f) = \int_{0}^{}  1f(x)dxfor any f \in C([0, 1])$$
Là dạng tuyến tính (linear form) (phép lấy tích phân).

> **Ví dụ 3.9.** Xét không gian vectơ (vector space) $M_{n}(\mathbb{R})$ của thực $n\times n$ các ma trận. Cho tr: $M_{n}(\mathbb{R}) \to \mathbb{R}$ là hàm cho trước bởi
$$\mathrm{tr}(A) = a_{11} + a_{22} + \cdots  + a_{nn},$$
Được gọi là vết (trace) của $A$. Nó là dạng tuyến tính (linear form). Cho $s: M_{n}(\mathbb{R}) \to \mathbb{R}$ là hàm cho trước bởi
$$s(A) = \sum_{i,j=1}^{n}  a_{ij},$$
Ở đâu $A = (a_{ij})$. Ta kiểm chứng được ngay rằng $s$ là dạng tuyến tính (linear form).

<!-- PAGE 114 -->
Cho trước không gian vectơ (vector space) $E$ và bất kỳ cơ sở (basis) $(u_{i})_{i\in I}$ cho $E$, ta có thể associate đến mỗi $u_{i}$ dạng tuyến tính (linear form) $u_{i}^{*} \in E^{*}$, và $u_{i}^{*}$ có một số đáng chú ý các tính chất.

> **Định nghĩa 3.27.** Cho trước không gian vectơ (vector space) $E$ và bất kỳ cơ sở (basis) $(u_{i})_{i\in I}$ cho $E$, theo Mệnh đề 3.20, với mọi $i \in$ I, tồn tại duy nhất một dạng tuyến tính (linear form) $u_{i}^{*}$ sao cho
$$1if i = j$$
$$u_{i}^{*} (u_{j}) =$$
$$0if i \neq  j,$$
Với mọi $j \in$ I. dạng tuyến tính (linear form) $u_{i}^{*}$ được gọi là tọa độ tạo thành của chỉ số $i$ w.r.t. cơ sở (basis) $(u_{i})_{i\in I}$.
Nhận xét: Cho trước chỉ số tập hợp $I$, các tác giả thường định nghĩa do đó được gọi là “Kronecker ký hiệu” $\delta_{i j}$ sao cho
$$1if i = j$$
$$\delta_{i j}  =$$
$$0if i \neq  j,$$
Với mọi $i, j \in$ I. Thì, $u_{i}^{*} (u_{j}) = \delta_{i j}$. lý do cho thuật ngữ tọa độ tạo thành là như sau: Nếu $E$ có hữu hạn số chiều và nếu $(u_{1}, \dots  , u_{n})$ là cơ sở (basis) của $E$, với mọi vectơ
$$v = \lambda_{1} u_{1} + \cdots  + \lambda_{n} u_{n},$$
Ta có
$$u_{i}^{*} (v) = u_{i}^{*} (\lambda_{1} u_{1} + \cdots  + \lambda_{n} u_{n})$$
$$= \lambda_{1} u_{i}^{*} (u_{1}) + \cdots  + \lambda_{i} u_{i}^{*} (u_{i}) + \cdots  + \lambda_{n} u_{i}^{*} (u_{n})$$
$$= \lambda_{i} ,$$
Vì $u_{i}^{*} (u_{j}) = \delta_{i j}$. Vì vậy, $u_{i}^{*}$ là tuyến tính hàm rằng trả về tọa độ thứ $i$ của vectơ được biểu diễn trên cơ sở (basis) $(u_{1}, \dots  , u_{n})$. sau đây định lý chỉ ra rằng trong finite-dimension, mọi cơ sở (basis) $(u_{1}, \dots  , u_{n})$ của không gian vectơ (vector space) $E$ cho ta cơ sở (basis) $(u_{1}^{*}, \dots  , u_{n}^{*})$ của không gian đối ngẫu (dual space) $E^{*}$, được gọi là đối ngẫu (dual) cơ sở (basis).

> **Định lý 3.26.** (Sự tồn tại của đối ngẫu (dual) các cơ sở) Cho $E$ là không gian vectơ (vector space) có số chiều $n$ trên trường $K$. Các tính chất sau đây đúng: Với mọi cơ sở (basis) $(u_{1}, \dots  , u_{n})$ của $E$, họ của tọa độ các dạng $(u_{1}^{*}, \dots  , u_{n}^{*})$ là cơ sở (basis) của $E^{*}$ (được gọi là đối ngẫu (dual) cơ sở (basis) của $(u_{1}, \dots  , u_{n}))$.

*Chứng minh.* () Nếu $v^{*} \in E^{*}$ là bất kỳ dạng tuyến tính (linear form), xét dạng tuyến tính (linear form)
$$f^{*} = v^{*}(u_{1})u_{1}^{*} + \cdots  + v^{*}(u_{n})u_{n}^{*}.$$
Nhận thấy rằng bởi vì $u_{i}^{*} (u_{j}) = \delta_{i j}$,
$$f^{*} (u_{i}) = (v^{*}(u_{1})u_{1}^{*} + \cdots  + v^{*}(u_{n})u_{n}^{*})(u_{i})$$
$$= v^{*}(u_{1})u_{1}^{*}(u_{i}) + \cdots  + v^{*}(u_{i})u_{i}^{*} (u_{i}) + \cdots  + v^{*}(u_{n})u_{n}^{*}(u_{i})$$
$$= v^{*}(u_{i}),$$

<!-- PAGE 115 -->
Và do đó $f^{*}$ và $v^{*}$ agree trên cơ sở (basis) $(u_{1}, \dots  , u_{n})$, mà suy ra rằng
$$v^{*}= f^{*} = v^{*}(u_{1})u_{1}^{*} + \cdots  + v^{*}(u_{n})u_{n}^{*}.$$
Vì vậy, $(u_{1}^{*}, \dots  , u_{n}^{*})$ sinh ra $E^{*}$. Ta khẳng định rằng covectors $u_{1}^{*}, \dots  , u_{n}^{*}$ là độc lập tuyến tính (linearly independent). Nếu không, ta có không tầm thường sự phụ thuộc tuyến tính (linear dependence)
$$\lambda_{1} u_{1}^{*} + \cdots  + \lambda_{n} u_{n}^{*} = 0^{*},$$
Ở đâu $0^{*}$ ký hiệu dạng tuyến tính (linear form) sao cho $0^{*}(v) = 0$ với mọi $v \in E$ (với $0 \in K)$, và nếu ta áp dụng ở trên dạng tuyến tính (linear form) đến mỗi $u_{i}$, ta có
$$(\lambda_{1} u_{1}^{*} + \cdots  + \lambda_{n} u_{n}^{*})(u_{i}) = \lambda_{1} u_{1}^{*}(u_{i}) + \cdots  + \lambda_{i} u_{i}^{*} (u_{i}) + \cdots  + \lambda_{n} u_{n}^{*}(u_{i}) = \lambda_{i}  = 0,$$
Chứng minh rằng $u_{1}^{*}, \dots  , u_{n}^{*}$ là thật vậy độc lập tuyến tính (linearly independent). Vì vậy, $(u_{1}^{*}, \dots  , u_{n}^{*})$ là cơ sở (basis) của $E^{*}$. Đặc biệt, Định lý 3.26 chỉ ra không gian vectơ hữu hạn chiều và của nó đối ngẫu (dual) $E^{*}$ có me số chiều.

> **Ví dụ 3.10.** Xét vectơ $space\mathbb{R}[X]_{n}$ của các đa thức trong biến $X$ của bậc nhiều nhất $n$ với thực các hệ số. Ta biết rằng nó có cơ sở (basis) $(1, X, X^{2}, \dots  , X^{n})$. Nếu ta viết $e_{i} = X^{i}$, đối ngẫu (dual) cơ sở (basis) các vectơ $e_{i}^{*}$ là các dạng tuyến tính được định nghĩa trên các đa thức mà là một cách duy nhất được định nghĩa bởi các phương trình
$$e_{i}^{*} (e_{j}) = e_{i}^{*} (X^{j}) = \delta_{ij} .$$
Ta có thể đồng nhất một cách tường minh các dạng tuyến tính $e_{i}^{*}$. Thật vậy, với mọi $i$ sao cho $0 \le i \le n$, nếu $D^{(i)}$ là dạng tuyến tính (linear form) được định nghĩa bởi $D^{(i)} = D \circ \cdots  \circ D$, ở đâu $D$ là differentiation toán tử
$$|{z}$$
$$i$$
Trên các đa thức, nói cách khác, với mọi đa thức $P \in \mathbb{R}[X]_{n}, D^{(i)}P$ là kết quả của differentiating $P i$ lần (với $D^{(0)} =$ id), thì $e_{i}^{*}$ cho trước bởi
$$e_{i}^{*} (P) = \frac{1}{i!} (D^{(i)}P)(0)$$
Thực hiện job, vì
$$i!X^{j-i},if j > i$$
$$$$
$$$$
$$D^{(i)}X^{j}=i!,if j = i$$
$$0,if j < i,$$
$$$$
Do đó khi ta tính giá trị $D^{(i)}X^{j}$ tại $0$, ta thu được $\delta_{ij}$. Ta được giải thích chỉ sau Định nghĩa 3.26 rằng nếu không gian $E$ là hữu hạn chiều và có hữu hạn cơ sở (basis) $(u_{1}, \dots  , u_{n})$, thì dạng tuyến tính (linear form) $f^{*}$: $E \to K$ được biểu diễn bởi vectơ hàng (row vector) của các hệ số
$$\begin{pmatrix} f^{*}(u_{1}) & \cdots & f^{*}(u_{n}) \end{pmatrix} .(1)$$
