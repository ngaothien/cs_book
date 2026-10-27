# Các tính chất của Gấp đôi Chuyển vị (transpose)


<!-- PAGE 443 -->

> **Mệnh đề 11.17.** Cho trước bất kỳ ma trận cỡ $m\times n$ $A$ trên trường $K$ (typically $K =\mathbb{R}$ hoặc $K =\mathbb{C})$, hạng (rank) của $A$ là cực đại tự nhiên số $r$ sao cho có một $r \times  r$ ma trận con $B$ của $A$ thu được bởi chọn $r$ các hàng và $r$ các cột của $A$, sao cho det(B) $\neq  0$. Điều này là không rất efficient cách của việc tìm hạng (rank) của ma trận. Ta sẽ xem rằng có tốt hơn các cách bằng cách sử dụng khác nhau các phân rã chẳng hạn như LU, QR, hoặc SVD.

## 11.7 Các tính chất của Gấp đôi Chuyển vị (transpose)

Thứ nhất ta có kết quả sau tính chất chỉ ra naturality của eval ánh xạ.

> **Mệnh đề 11.18.** Với mọi ánh xạ tuyến tính (linear map) $f$: $E \to F$, ta có
$$f^{\top \top} \circ eval_{E} = eval_{F} \circ f,$$
Hoặc tương đương sau đây biểu đồ giao hoán:
$$E^{**f\top \top} F^{**}/$$
$$evalEevalF$$
$$E F./$$
$$\overline{f}$$

*Chứng minh.* Với mọi $u \in E$ và mọi $\phi  \in F^{*}$, ta có
$$(f^{\top \top} \circ eval_{E})(u)(\phi ) = \langle f^{\top \top} (eval_{E}(u)), \phi \rangle$$
$$= \langle eval_{E}(u), f^{\top} (\phi )\rangle$$
$$= \langle f^{\top} (\phi ), u\rangle$$
$$= \langle \phi , f(u)\rangle$$
$$= \langle eval_{F}(f(u)), \phi \rangle$$
$$= \langle (eval_{F} \circ f)(u), \phi \rangle$$
$$= (eval_{F} \circ f)(u)(\phi ),$$
Mà chứng tỏ rằng $f^{\top \top} \circ eval_{E} = eval_{F} \circ f$, như đã khẳng định. Nếu $E$ và $F$ là hữu hạn chiều, thì $eval_{E}$ và $eval_{F}$ là các đẳng cấu, do đó Mệnh đề 11.18 chỉ ra rằng
$$f^{\top \top} = eval_{F} \circ f \circ eval_{E}^{-1} .(*)$$
Ở trên phương trình là thường interpreted như sau: nếu ta đồng nhất $E$ với của nó bidual $E^{**}$ và $F$ với của nó bidual $F^{**}$, thì $f^{\top \top} = f$. Điều này là abuse của ký hiệu; chặt chẽ phát biểu là (*). Như hệ quả của Mệnh đề 11.18, ta thu được kết quả sau kết quả.

<!-- PAGE 444 -->

> **Mệnh đề 11.19.** Nếu dim(E) là hữu hạn, thì ta có
$$\mathrm{Ker} (f^{\top \top} ) = eval_{E}(\mathrm{Ker} (f)).$$

*Chứng minh.* Thật vậy, nếu $E$ là hữu hạn chiều, ánh xạ $eval_{E}$: $E \to E^{**}$ là đẳng cấu, do đó mọi $\phi  \in E^{**}$ là của tạo thành $\phi  = eval_{E}(u)$ với một số $u \in E$, ánh xạ $eval_{F}$: $F \to F^{**}$ là đơn ánh (injective), và ta có
$$f^{\top \top} (\phi ) = 0ifff^{\top \top} (eval_{E}(u)) = 0$$
$$iff eval_{F}(f(u)) = 0$$
$$iff f(u) = 0$$
$$iff u \in \mathrm{Ker} (f)$$
$$iff\phi  \in eval_{E}(\mathrm{Ker} (f)),$$
Mà chứng tỏ rằng Ker $(f^{\top \top}$) $= eval_{E}(Ker (f))$.
Các nhận xét: Nếu dim(E) là hữu hạn, sau đây lập luận của Dan Guralnik, sự kiện rằng rk(f) $= rk(f^{\top}$) có thể được được chứng minh bằng cách sử dụng Mệnh đề 11.19.

*Chứng minh.* Ta biết từ Mệnh đề 11.11 ứng dụng đến $f^{\top}$: $F^{*} \to E^{*}$ rằng
$$\mathrm{Ker} (f^{\top \top} ) = (\mathrm{Im} f^{\top} )^{0},$$
Và ta đã chỉ ra trong Mệnh đề 11.19 rằng
$$\mathrm{Ker} (f^{\top \top} ) = eval_{E}(\mathrm{Ker} (f)).$$
Nó suy ra (vì $eval_{E}$ là đẳng cấu) rằng
$$\dim((\mathrm{Im} f^{\top} )^{0}) = \dim(\mathrm{Ker} (f^{\top \top} )) = \dim(\mathrm{Ker} (f)) = \dim(E) -\dim(\mathrm{Im} f),$$
Và vì
$$\dim(\mathrm{Im} f^{\top} ) + \dim((\mathrm{Im} f^{\top} )^{0}) = \dim(E),$$
Ta thu được
$$\dim(\mathrm{Im} f^{\top} ) = \dim(\mathrm{Im} f).$$
Như indicated bởi Dan Guralnik, nếu dim(E) là hữu hạn, ở trên kết quả có thể được được sử dụng để chứng minh kết quả sau đây.

> **Mệnh đề 11.20.** Nếu dim(E) là hữu hạn, thì với mọi ánh xạ tuyến tính (linear map) $f$: $E \to F$, ta có
$$\mathrm{Im} f^{\top} = (\mathrm{Ker} (f))^{0}.$$
