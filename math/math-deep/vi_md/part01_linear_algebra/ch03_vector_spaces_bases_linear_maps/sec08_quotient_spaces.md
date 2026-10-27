# Các không gian thương


<!-- PAGE 111 -->

> **Định nghĩa 3.23.** Khi $E = F$, ánh xạ tuyến tính (linear map) $f$: $E \to E$ cũng được gọi là một tự đồng cấu. không gian Hom(E, $E)$ cũng được ký hiệu bởi Kết thúc/cuối(E). Nó là cũng quan trọng đến lưu ý rằng hợp thành confers đến Hom(E, $E)$ vành cấu trúc. Thật vậy, hợp thành là phép toán $\circ$: Hom(E, $E) \times$ Hom(E, $E) \to$ Hom(E, $E)$, mà là kết hợp và có đồng nhất thức $id_{E}$, và distributivity các tính chất đúng:
$$(g_{1} + g_{2}) \circ f = g_{1} \circ f + g_{2} \circ f;$$
$$g \circ (f_{1} + f_{2}) = g \circ f_{1} + g \circ f_{2}.$$
Vành Hom(E, $E)$ là ví dụ của không giao hoán vành. Nó là dễ dàng được thấy rằng tập hợp của song ánh (bijective) các ánh xạ tuyến tính (linear maps) $f$: $E \to E$ là nhóm dưới hợp thành.

> **Định nghĩa 3.24.** Song ánh (bijective) các ánh xạ tuyến tính (linear maps) $f$: $E \to E$ cũng được gọi là các tự đẳng cấu. nhóm của các tự đẳng cấu của $E$ được gọi là tổng quát tuyến tính nhóm (của $E)$, và nó được ký hiệu bởi GL(E), hoặc bởi Aut(E), hoặc khi $E =\mathbb{R}^{n}$, bởi $GL(n,\mathbb{R})$, hoặc chẵn/ngay cả bởi GL(n). Mặc dù trong điều này cuốn sách, ta sẽ không có nhiều occasions để sử dụng các không gian thương, chúng là cơ bản trong đại số. tiếp theo mục có thể được bỏ qua cho đến khi cần thiết.

## 3.8 Các không gian thương

Cho $E$ là không gian vectơ (vector space), và cho $M$ là bất kỳ không gian con của $E$. không gian con $M$ cảm sinh quan hệ $\equiv_{M}$ trên $E$, được định nghĩa như sau: Với mọi $u, v \in E, u \equiv_{M}  v$ khi và chỉ khi $u$ - $v \in M$. Ta có kết quả sau đơn giản mệnh đề.

> **Mệnh đề 3.25.** Cho trước bất kỳ không gian vectơ (vector space) $E$ và bất kỳ không gian con $M$ của $E$, quan hệ $\equiv_{M}$ là quan hệ tương đương (equivalence relation) với sau đây hai congruential các tính chất: $1$. Nếu $u_{1} \equiv_{M}  v_{1}$ và $u_{2} \equiv_{M}  v_{2}$, thì $u_{1} + u_{2} \equiv_{M}  v_{1} + v_{2}$, và $2$. nếu $u \equiv_{M}  v$, thì $\lambda u \equiv_{M}  \lambda v$.

*Chứng minh.* Hiển nhiên là $\equiv_{M}$ là quan hệ tương đương (equivalence relation). Lưu ý rằng $u_{1} \equiv_{M}  v_{1}$ và $u_{2} \equiv_{M}  v_{2}$ là tương đương đến $u_{1}$ - $v_{1} = w_{1}$ và $u_{2}$ - $v_{2} = w_{2}$, với $w_{1}, w_{2} \in M$, và do đó,
$$(u_{1} + u_{2}) -(v_{1} + v_{2}) = w_{1} + w_{2},$$
Và $w_{1} + w_{2} \in M$, vì $M$ là không gian con của $E$. Do đó, ta có $u_{1} + u_{2} \equiv_{M}  v_{1} + v_{2}$. Nếu $u$ - $v = w$, với $w \in M$, thì
$$\lambda u -\lambda v = \lambda w,$$
Và $\lambda w \in M$, vì $M$ là không gian con của $E$, và do đó $\lambda u \equiv_{M}  \lambda v$.
