# Bốn Cơ bản Các không gian con


<!-- PAGE 445 -->

*Chứng minh.* Từ
$$\langle f^{\top} (\phi ), u\rangle = \langle \phi , f(u)\rangle$$
Với mọi $\phi  \in F^{*}$ và tất cả $u \in E$, ta xem rằng nếu $u \in$ Ker $(f)$, thì $\langle f^{\top} (\phi$), $u\rangle = \langle \phi , 0\rangle = 0$, mà có nghĩa là $f^{\top} (\phi$) $\in$ (Ker $(f))^{0}$, và do đó, Im $f^{\top} \subseteq$ (Ker $(f))^{0}$. Cho điều ngược lại, vì dim(E) là hữu hạn, ta có
$$\dim((\mathrm{Ker} (f))^{0}) = \dim(E) -\dim(\mathrm{Ker} (f)) = \dim(\mathrm{Im} f),$$
Nhưng ta chỉ được chứng minh rằng dim(Im $f^{\top}$) $=$ dim(Im $f)$, do đó ta thu được
$$\dim((\mathrm{Ker} (f))^{0}) = \dim(\mathrm{Im} f^{\top} ),$$
Và vì Im $f^{\top} \subseteq$ (Ker $(f))^{0}$, ta thu được
$$\mathrm{Im} f^{\top} = (\mathrm{Ker} (f))^{0},$$
Như đã khẳng định.
Các nhận xét: $1$. Bởi đối ngẫu định lý, vì (Ker $(f))^{00} =$ Ker $(f)$, ở trên phương trình cho ta một cái khác chứng minh của sự kiện rằng
$$\mathrm{Ker} (f) = (\mathrm{Im} f^{\top} )^{0},$$
Khi $E$ là hữu hạn chiều. $2$. phương trình
$$\mathrm{Im} f^{\top} = (\mathrm{Ker} (f))^{0}$$
Là thực sự hợp lệ chẵn/ngay cả nếu khi $E$ nếu vô hạn chiều, nhưng ta sẽ không chứng minh điều này ở đây.

## 11.8 Bốn Cơ bản Các không gian con

Cho trước ánh xạ tuyến tính (linear map) $f$: $E \to F$ (ở đâu $E$ và $F$ là hữu hạn chiều), Mệnh đề 11.11 revealed rằng bốn các không gian
$$\mathrm{Im} f, \mathrm{Im} f^{\top} , \mathrm{Ker} f, \mathrm{Ker} f^{\top}$$
Đóng đặc biệt vai trò. Chúng là thường được gọi là cơ bản các không gian con liên kết với $f$. các không gian này là related trong intimate cách thức, vì Mệnh đề 11.11 chỉ ra rằng
$$\mathrm{Ker} f = (\mathrm{Im} f^{\top} )^{0}$$
$$\mathrm{Ker} f^{\top} = (\mathrm{Im} f)^{0},$$

<!-- PAGE 446 -->
Và Định lý 11.12 chỉ ra rằng
$$rk(f) = rk(f^{\top} ).$$
Nó là instructive đến translate các quan hệ này theo các ma trận (thực sự, nhất định tuyến tính đại số các cuốn sách tạo big deal về điều này!). Nếu dim(E) $= n$ và dim(F) $= m$, cho trước bất kỳ cơ sở (basis) $(u_{1}, \dots  , u_{n})$ của $E$ và cơ sở (basis) $(v_{1}, \dots  , v_{m})$ của $F$, ta biết rằng $f$ được biểu diễn bởi một ma trận cỡ $m \times  n$ $A = (a_{i j})$, ở đâu cột thứ $j$ của $A$ bằng $f(u_{j})$ trên cơ sở (basis) $(v_{1}, \dots  , v_{m})$. Hơn nữa, chuyển vị (transpose) ánh xạ $f^{\top}$ được biểu diễn bởi ma trận cỡ $n \times  m$ $A^{\top}$ (đối với đối ngẫu (dual) các cơ sở). Hệ quả là, bốn cơ bản các không gian
$$\mathrm{Im} f, \mathrm{Im} f^{\top} , \mathrm{Ker} f, \mathrm{Ker} f^{\top}$$
Tương ứng với
$$\mathbb{R}^{m}$$
$(1)$ cột không gian của $A$, được ký hiệu bởi Im $A$ hoặc $\mathcal{R}(A)$; điều này là không gian con của được sinh (spanned) bởi các cột của $A$, mà tương ứng với ảnh (image) Im $f$ của $f$.
$(2)$ hạt nhân (kernel) hoặc không gian hạch (nullspace) của $A$, được ký hiệu bởi Ker $A$ hoặc $\mathcal{N}(A)$; điều này là không gian con của $\mathbb{R}^{n}$
$$\mathbb{R}^{n}$$
Bao gồm của tất cả các vectơ $x \in$ sao cho Ax $= 0$.
$$\mathbb{R}^{n}$$
$(3)$ hàng không gian của $A$, được ký hiệu bởi Im $A^{\top}$ hoặc $\mathcal{R}(A^{\top})$; điều này là không gian con của được sinh (spanned) bởi các hàng của $A$, hoặc tương đương, được sinh (spanned) bởi các cột của $A^{\top}$, mà tương ứng với ảnh (image) Im $f^{\top}$ của $f^{\top}$.
$(4)$ trái hạt nhân (kernel) hoặc trái không gian hạch (nullspace) của $A$ được ký hiệu bởi Ker $A^{\top}$ hoặc $\mathcal{N}(A^{\top})$; điều này là hạt nhân (kernel)
$$\mathbb{R}^{m} \mathbb{R}^{m}$$
(không gian hạch (nullspace)) của $A^{\top}$, không gian con của bao gồm của tất cả các vectơ $y \in$ sao cho $A^{\top}y = 0$, hoặc tương đương, $y^{\top}A = 0$. Nhắc lại rằng số chiều $r$ của Im $f$, mà là cũng bằng số chiều của cột không gian Im $A = \mathcal{R}(A)$, là hạng (rank) của $A$ (và $f)$. Thì, một số của ta trước đó các kết quả có thể được reformulated như sau: $1$. cột không gian $\mathcal{R}(A)$ của $A$ có số chiều $r. 2$. không gian hạch (nullspace) $\mathcal{N}(A)$ của $A$ có số chiều $n$ - $r. 3$. hàng không gian $\mathcal{R}(A^{\top})$ có số chiều $r. 4$. trái không gian hạch (nullspace) $\mathcal{N}(A^{\top})$ của $A$ có số chiều $m$ - $r$. ở trên các phát biểu constitute những gì Strang gọi Cơ bản Định lý của Tuyến tính Đại số, Phần I (xem Strang $[176])$. hai các phát biểu
$$\mathrm{Ker} f = (\mathrm{Im} f^{\top} )^{0}$$
$$\mathrm{Ker} f^{\top} = (\mathrm{Im} f)^{0}$$
Translate đến

<!-- PAGE 447 -->
$(1)$ không gian hạch (nullspace) của $A$ là trực giao của hàng không gian của $A$.
$(2)$ trái không gian hạch (nullspace) của $A$ là trực giao của cột không gian của $A$. ở trên các phát biểu constitute những gì Strang gọi Cơ bản Định lý của Tuyến tính Đại số, Phần II (xem Strang $[176])$. Vì các vectơ được biểu diễn bởi các vectơ cột và các dạng tuyến tính bởi các vectơ hàng (trên
$$\mathbb{R}^{n}$$
Cơ sở (basis) trong $E$ hoặc $F)$, vectơ $x \in$ là trực giao đến dạng tuyến tính (linear form) $y$ khi và chỉ khi
$$yx = 0.$$
$$\mathbb{R}^{n}$$
Thì, vectơ $x \in$ là trực giao đến hàng không gian của $A$ khi và chỉ khi $x$ là trực giao đến mọi hàng của $A$, cụ thể là Ax $= 0$, mà là tương đương đến sự kiện rằng $x$ thuộc đến không gian hạch (nullspace) của $A$.
$$\mathbb{R}^{m}$$
Tương tự, vectơ cột (column vector) $y \in$ (biểu diễn dạng tuyến tính (linear form) trên đối ngẫu (dual) cơ sở (basis) của $F^{*})$ thuộc đến không gian hạch (nullspace) của $A^{\top}$ khi và chỉ khi $A^{\top}y = 0$, khi và chỉ khi $y^{\top}A = 0$, mà có nghĩa là dạng tuyến tính (linear form) cho trước bởi $y^{\top}$ (trên cơ sở (basis) trong $F)$ là trực giao đến cột không gian của $A$. Vì $(2)$ là tương đương đến sự kiện rằng cột không gian của $A$ bằng trực giao của trái không gian hạch (nullspace) của $A$, ta thu được sau đây tiêu chuẩn cho solvability của phương trình của tạo thành Ax $= b$: phương trình Ax $= b$ có nghiệm khi và chỉ khi với mọi $y \in \mathbb{R}^{m}$, nếu $A^{\top}y = 0$, thì $y^{\top}b = 0$. Thật vậy, điều kiện trên vế phải nói rằng rằng $b$ là trực giao đến trái không gian hạch (nullspace) của $A$; nghĩa là, $b$ thuộc đến cột không gian của $A$. Điều này tiêu chuẩn có thể được cheaper để kiểm tra rằng kiểm tra một cách trực tiếp rằng $b$ được sinh (spanned) bởi các cột của $A$. Ví dụ, nếu ta xét hệ
$$x_{1} -x_{2} = b_{1}$$
$$x_{2} -x_{3} = b_{2}$$
$$x_{3} -x_{1} = b_{3}$$
Mà, trong ma trận tạo thành, được viết Ax $= b$ như ở dưới:
$$\begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \\ 1 & 0 & 1 \end{pmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \end{pmatrix} = \begin{pmatrix} b_{1} \\ b_{2} \\ b_{3} \end{pmatrix} ,$$
$$-$$
Ta xem rằng các hàng của ma trận $A$ cộng sai khác $0$. Thực ra, nó là dễ đến convince chính chúng ta rằng trái không gian hạch (nullspace) của $A$ được sinh (spanned) bởi $y = (1, 1, 1)$, và do đó hệ là giải được khi và chỉ khi $y^{\top}b = 0$, cụ thể là
$$b_{1} + b_{2} + b_{3} = 0.$$
Lưu ý rằng ở trên tiêu chuẩn có thể cũng được phát biểu một cách âm như sau:
$$\mathbb{R}^{m}$$
Phương trình Ax $= b$ có không có nghiệm khi và chỉ khi tồn tại một $y \in$ sao cho $A^{\top}y = 0$ và $y^{\top}b \neq  0$.
