# Afin Các siêu phẳng


<!-- PAGE 847 -->
$$a$$
$$a$$
$$bb$$
$$d$$
$$c$$
$$c$$
$$Figure 24.25: Desargues’s theorem (affine version).$$
Desargues’s định lý được minh họa trong Hình 24.25. Có một fancier phiên bản của Desargues’s định lý, nhưng nó là dễ hơn để chứng minh nó bằng cách sử dụng xạ ảnh hình học. Nó nên được lưu ý rằng trong axiomatic các trình bày của xạ ảnh hình học, Desargues’s định lý là related đến tính kết hợp của ground trường $K$ (trong trình bày trường hợp, $K = \mathbb{R})$. Cũng, Desargues’s định lý cho ta hình học đặc trưng của afin các phép vị tự. afin phép vị tự (dilatation) $f$ trên không gian afin (affine space) $E$ là song ánh rằng các ánh xạ mọi đường thẳng $D$ đến đường thẳng f(D) song song đến $D$. Ta để lại chứng minh như một bài tập.

## 24.10 Afin Các siêu phẳng

Ta bây giờ xét afin các dạng và afin các siêu phẳng. Trong Mục 24.5 ta được quan sát rằng tập hợp $L$ của các nghiệm của phương trình
$$ax + by = c$$
$$\mathbb{A}^{2}$$
Là không gian con afin (affine subspace) của có số chiều $1$, thực ra, đường thẳng (miễn là/được cung cấp rằng và $b$ là không cả hai null). Nó sẽ là một cách bằng nhau dễ để chỉ ra rằng tập hợp $P$ của các nghiệm của phương trình
$$ax + by + cz = d$$
$$\mathbb{A}^{3}$$
Là không gian con afin (affine subspace) của có số chiều $2$, thực ra, mặt phẳng (miễn là/được cung cấp rằng, $b, c$ là không tất cả null). Tổng quát hơn, tập hợp $H$ của các nghiệm của phương trình
$$\lambda_{1} x_{1} + \cdots  + \lambda_{m} x_{m} = \mu$$
Là không gian con afin (affine subspace) $of\mathbb{A}^{m}$, và nếu $\lambda_{1} , \dots  , \lambda_{m}$ là không tất cả null, hóa ra là nó là không gian con có số chiều $m$ - $1$ được gọi là siêu phẳng (hyperplane).

<!-- PAGE 848 -->
Ta có thể interpret phương trình
$$\lambda_{1} x_{1} + \cdots  + \lambda_{m} x_{m} = \mu$$
$$\mathbb{R}^{m} \mathbb{R}$$
Theo ánh xạ $f$: $\to$ được định nghĩa sao cho
$$f(x_{1}, \dots  , x_{m}) = \lambda_{1} x_{1} + \cdots  + \lambda_{m} x_{m} -\mu$$
Với mọi $(x_{1}, \dots  , x_{m}) \in \mathbb{R}^{m}$. Ta kiểm chứng được ngay rằng ánh xạ này là afin, và tập hợp $H$ của các nghiệm của phương trình
$$\lambda_{1} x_{1} + \cdots  + \lambda_{m} x_{m} = \mu$$
$$\mathbb{A}^{m} \mathbb{R}$$
Là null tập hợp, hoặc hạt nhân (kernel), của ánh xạ afin (affine map) $f$: $\to$, trong nghĩa rằng
$$\mathbb{A}^{m}$$
$$H = f^{-1}(0) = {x \in | f(x) = 0},$$
Ở đâu $x = (x_{1}, \dots  , x_{m})$. Do đó, nó là thú vị đến xét afin các dạng, mà là chỉ các ánh xạ afin $f$: $E \to \mathbb{R}$ từ không gian afin (affine space) đến $\mathbb{R}$. Unlike các dạng tuyến tính $f^{*}$, cho mà Ker $f^{*}$ là không bao giờ rỗng (vì nó luôn luôn chứa vectơ $0)$, nó là khả dĩ/có thể rằng $f^{-1} (0) = \emptyset$ cho afin tạo thành $f$. Cho trước ánh xạ afin (affine map) $f$: $E \to \mathbb{R}$, ta cũng ký hiệu $f^{-1} (0)$ bởi Ker $f$, và ta gọi nó hạt nhân (kernel) của $f$. Nhắc lại rằng (afin) siêu phẳng (hyperplane) là không gian con afin (affine subspace) của đối chiều (codimension) $1$. relationship giữa afin các siêu phẳng và afin các dạng được cho bởi sau đây mệnh đề.

> **Mệnh đề 24.14.** Cho $E$ là không gian afin (affine space). Các tính chất sau đây đúng:
() Cho trước bất kỳ nonconstant afin tạo thành $f$: $E \to \mathbb{R}$, của nó hạt nhân (kernel) $H =$ Ker $f$ là siêu phẳng (hyperplane).
$(b)$ Với mọi siêu phẳng (hyperplane) $H$ trong $E$, có một nonconstant afin tạo thành $f$: $E \to \mathbb{R}$ sao cho $H =$ Ker $f$. Với mọi khác afin tạo thành $g: E \to \mathbb{R}$ sao cho $H =$ Ker $g$, tồn tại một $\lambda  \in \mathbb{R}$ sao cho $g = \lambda f$ (với $\lambda  \neq  0)$.
$(c)$ Cho trước bất kỳ siêu phẳng (hyperplane) $H$ trong $E$ và bất kỳ (nonconstant) afin tạo thành $f$: $E \to \mathbb{R}$ sao cho $H =$ Ker $f$, mọi siêu phẳng (hyperplane) H' song song đến $H$ được định nghĩa bởi nonconstant afin tạo thành $g$ sao cho g() $=$ f() - $\lambda$, với mọi $a \in E$ và một số $\lambda  \in \mathbb{R}$.

*Chứng minh.* chứng minh là trực tiếp/dễ dàng, và được bỏ qua. Nó là cũng cho trước trong Gallier $[71]$. Khi $E$ là có số chiều $n$, cho trước hệ quy chiếu afin (affine frame) $(a_{0}, (u_{1}, \dots  , u_{n}))$ của $E$ với gốc $a_{0}$, nhắc lại từ Định nghĩa 24.5 rằng mọi điểm của $E$ có thể được được biểu diễn một cách duy nhất như $x = a_{0} + x_{1}u_{1} + \cdots  + x_{n}u_{n}$, ở đâu $(x_{1}, \dots  , x_{n})$ là các tọa độ của $x$ đối với hệ quy chiếu afin (affine frame) $(a_{0}, (u_{1}, \dots  , u_{n}))$.
