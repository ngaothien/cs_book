# Trái và Phải Hooks


<!-- PAGE 1251 -->
Ở đâu $A$ là ma trận biểu diễn $v_{j}$ theo $e_{i}$, ta có
$$\langle v_{1} \wedge \cdots  \wedge v_{n}, v_{1} \wedge \cdots  \wedge v_{n}\rangle_{\wedge} = \det(A)^{2}\langle e_{1} \wedge \cdots  \wedge e_{n}, e_{1} \wedge \cdots  \wedge e_{n}\rangle = \det(A)^{2}.$$
Hệ quả là, det() $= p\overline{det(}\overline{\langle}\overline{v}_{i}\overline{, v}_{j}\overline{\rangle}\overline{),}$ và
$$q$$
$$v_{1} \wedge \cdots  \wedge v_{n} =\det(\langle v_{i}, v_{j}\rangle ) e_{1} \wedge \cdots  \wedge e_{n},$$
Từ mà suy ra rằng
$$*(1) = \frac{1}{pdet(\langle v_{i}, v_{j}\rangle )} v_{1} \wedge \cdots  \wedge v_{n}$$
(xem Jost $[104]$, Chương $2$, Bổ đề 2.1.3).
$$⊛$$

## 34.7 Trái và Phải Hooks

Trong mục này tất cả các không gian vectơ được giả sử đến có hữu hạn số chiều. Nói dim(E) $= n$. Bằng cách sử dụng của ta không suy biến cặp
$$pp$$
$$\langle -, -\rangle :^E^{*}\times ^E \longrightarrow K(1 \le p \le n)$$
Được định nghĩa trên các phần tử sinh bởi
$$\langle u_{1}^{*} \wedge \cdots  \wedge u_{p}^{*}, v_{1} \wedge \cdots  \wedge u_{p}\rangle = \det(u_{i}^{*} (v_{j})),$$
Ta định nghĩa khác nhau ánh xạ co (contraction) các phép toán (riêng việc tính giá trị các toán tử)
$$pp+qq$$
$$⌟:^E \times ^E^{*}\longrightarrow ^E^{*}(left hook)$$
Và
$$p+qpq$$
$$⌞:^E^{*}\times ^E \longrightarrow ^E^{*}(right hook),$$
Cũng như các phiên bản thu được bằng cách thay thế $E$ bởi $E^{*}$ và $E^{**}$ bởi $E$. Ta bắt đầu với trái phần trong (interior) tích hoặc trái hook, ⌟.
$$p$$
$$Let u \in \bigwedge  E. For any q such that p + q \le n, multiplication on the right by u is a linear$$
Ánh xạ
$$qp+q$$
$$\wedge_{R} (u):^E \longrightarrow ^E$$
Cho trước bởi
$$v \mapsto v \wedge u$$

<!-- PAGE 1252 -->
$$q$$
$$where v \in \bigwedge  E. The transpose of \wedge_{R} (u) yields a linear map$$
$$* *$$
$$(\wedge_{R} (u))^{\top}: \begin{pmatrix} p+q \\ ^E \end{pmatrix} \longrightarrow \begin{pmatrix} q \\ ^E \end{pmatrix} ,$$
$$which, using the isomorphisms \bigwedge  \sim = \bigwedge_{+q}  p+q E_{*}and \bigwedge  \sim = \bigwedge  q E_{*}, can be viewed$$
$$as a map \begin{pmatrix} p+q E^{*} \end{pmatrix} \begin{pmatrix} q E^{*} \end{pmatrix}$$
$$pq$$
$$(\wedge_{R} (u))^{\top}:^E^{*}\longrightarrow ^E^{*}$$
Cho trước bởi
$$z^{*}\mapsto z^{*}\circ \wedge_{R} (u),$$
$$p+q  ⌟$$
$$where ⌟ z^{*}\in \bigwedge  E^{*}. We denote z^{*}\circ \wedge_{R} (u) by uz^{*}. In terms of our pairing, the adjoint$$
$u$ của $\wedge_{R} (u)$ được định nghĩa bởi
$$\langle u ⌟z^{*}, v\rangle = \langle z^{*}, \wedge_{R} (u)(v)\rangle ;$$
Điều này trong turn dẫn đến đến sau đây định nghĩa.
$$p p+q  ⌟q$$
$$Definition 34.8. Let u \in \bigwedge  E and z^{*}\in \bigwedge  E^{*}. We define uz^{*}\in \bigwedge  E^{*}to be q-vector$$
Một cách duy nhất được xác định bởi
$$⌟q$$
$$\langle uz^{*}, v\rangle = \langle z^{*}, v \wedge u\rangle ,for all v \in \bigwedge  E.$$
Nhận xét: Lưu ý rằng là precise toán tử
$$pp+qq$$
$$⌟:^E \times ^E^{*}\longrightarrow ^E^{*}$$
Phụ thuộc của $p, q$, do đó ta một cách thực được định nghĩa họ của các toán tử $⌟_{p,q}$. Điều này họ của các toán tử $⌟_{p,q}$ cảm sinh ánh xạ
$$⌟:^E \times ^E^{*}\longrightarrow ^E^{*},$$
Với
$$pp+qq$$
$$⌟_{p,q} :^E \times ^E^{*}\longrightarrow ^E^{*}$$
Như đã định nghĩa trước. chung/phổ biến practice là đến bỏ qua các chỉ số dưới của ⌟. Ta kiểm chứng được ngay rằng
$$(u \wedge v) ⌟z^{*}= u ⌟(v ⌟z^{*}),$$
$$k p-k p+q$$
$$for all u \in \bigwedge  E, v \in \bigwedge  E, z^{*}\in \bigwedge  E^{*}since$$
$$\langle (u \wedge v) ⌟z^{*}, w\rangle = \langle z^{*}, w \wedge u \wedge v\rangle = \langle v ⌟z^{*}, w \wedge u\rangle = \langle u ⌟(v ⌟z^{*}), w\rangle ,$$

<!-- PAGE 1253 -->
$$q$$
$$whenever w \in \bigwedge  E. This means that$$
$$⌟:^E \times ^E^{*}\longrightarrow ^E^{*}$$
$$is a left  action of the (noncommutative)  ring \bigwedge  E with multiplication \wedge on \bigwedge  E^{*}, which$$
$$makes \bigwedge  E^{*}into a left \bigwedge  E-module.$$
Bởi interchanging $E$ và $E^{*}$ và bằng cách sử dụng đẳng cấu
$$*$$
$$\sim^{k} ^$$
$$\begin{pmatrix} k \\ ^F \end{pmatrix} =F^{*},$$
Ta có thể cũng định nghĩa một số các ánh xạ
$$pp+qq$$
$$⌟:^E^{*}\times ^E \longrightarrow ^E,$$
Và tạo sau đây định nghĩa.
$$p p+q ⌟q$$
$$Definition 34.9. Let u^{*}\in \bigwedge  E^{*}, and z \in \bigwedge  E. We define u^{*}z \in \bigwedge  as the q-vector$$
Một cách duy nhất được định nghĩa bởi
$$⌟q$$
$$\langle v^{*}\wedge u^{*}, z\rangle = \langle v^{*}, u^{*}z\rangle ,for all v^{*}\in \bigwedge  E^{*}.$$
Như cho trước đó phiên bản, ta có họ của các toán tử $⌟_{p,q}$ mà định nghĩa toán tử
$$⌟:^E^{*}\times ^E \longrightarrow ^E.$$
Ta dễ dàng kiểm chứng rằng
$$(u^{*}\wedge v^{*}) ⌟z = u^{*}⌟(v^{*}⌟z),$$
$$p-k p+q  ⌟$$
$$whenever u^{*} \in \bigwedge  E^{*} , v^{*}\in \bigwedge  E^{*}, and  z \in \bigwedge  E;  so this version ofis a left action of$$
$$the ring \bigwedge  E^{*}on \bigwedge^{k}  E which makes \bigwedge  E into a left \bigwedge  E^{*}-module.$$
Trong thứ tự đến tiến hành bất kỳ further ta cần một số combinatorial các tính chất của cơ sở (basis) của $p E$
$$\bigwedge  constructed from a basis (e_{1}, \dots  , e_{n}) of E. Recall that for any (nonempty) subset$$
$I \subseteq {1, \dots  , n}$, ta cho
$$e_{I} = e_{i1} \wedge \cdots  \wedge e_{ip},$$
Ở đâu $I = {i_{1}, \dots  , i_{p}}$ với $i_{1} < \cdots  < i_{p}$. Ta cũng cho $e_{\emptyset} = 1$. Cho trước bất kỳ hai khác rỗng các tập con $H, L \subseteq {1, \dots  , n}$ cả hai được liệt kê trong tăng thứ tự, nói $H = {h_{1} < \dots  < h_{p}}$ và $L = {\ell_{1}  < \dots  < \ell_{q}$ }, nếu $H$ và $L$ là rời nhau, cho $H \cup L$ là hợp của $H$ và $L$ được xét như được thứ tự dãy
$$(h_{1}, \dots  , h_{p}, \ell_{1} , \dots  , \ell_{q} ).$$
Thì cho
$$0if H \cap L \neq  \emptyset ,$$
$$\rho_{H,L}  =$$
$$(-1)^{\nu}if H \cap L = \emptyset ,$$

<!-- PAGE 1254 -->
Ở đâu
$$\nu  = |{(h, l) | (h, l) \in H \times  L, h > l}|.$$
Nhận thấy rằng khi $H \cap L = \emptyset$, |H| $= p$ và |L| $= q$, số $\nu$ là số của các nghịch đảo của dãy
$$(h_{1}, \cdots  , h_{p}, \ell_{1} , \cdots  , \ell_{q} ),$$
Ở đâu nghịch đảo là cặp $(h_{i}, \ell_{j}$) sao cho $h_{i} > \ell_{j}$.  Trừ khi $p + q = n$, hàm có đồ thị được cho bởi
$$\begin{pmatrix} 1 \\ \cdots & p & p + 1 & \cdots & p + q \\ h_{1} & \cdots & h_{p} & \ell_{1} & \cdots & \ell_{q} \end{pmatrix}$$
Là không hoán vị của ${1, \dots  , n}$. Ta có thể quan điểm $\nu$ như slight tổng quát hóa của khái niệm của số của các nghịch đảo của hoán vị.

> **Mệnh đề 34.18.** Với mọi cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $E$ các tính chất sau đây đúng:
$(1)$ Nếu $H \cap L = \emptyset$, |H| $= p$, và |L| $= q$, thì
$$\rho_{H,L} \rho_{L,H}  = (-1)^{\nu}(-1)^{pq-\nu}= (-1)^{pq}.$$
$(2)$ Cho $H, L \subseteq {1, \dots  , m}$ được liệt kê trong tăng thứ tự, ta có
$$e_{H} \wedge e_{L} = \rho_{H,L} e_{H\cup L}.$$
Tương tự,
$$e_{H}^{*} \wedge e_{L}^{*} = \rho_{H,L} e_{H\cup L}^{*}.$$
$(3)$ Cho trái hook
$$pp+qq$$
$$⌟:^E \times ^E^{*}\longrightarrow ^E^{*},$$
Ta có
$$e_{H} ⌟e_{L}^{*} = 0if H̸ \subseteq L$$
$$e_{H} ⌟e_{L}^{*} = \rho_{L-H,H} e_{L-H}^{*}if H \subseteq L.$$
$(4)$ Cho trái hook
$$pp+qq$$
$$⌟:^E^{*}\times ^E \longrightarrow ^E,$$
Ta có
$$e_{H}^{*} ⌟e_{L} = 0if H̸ \subseteq L$$
$$e_{H}^{*} ⌟e_{L} = \rho_{L-H,H} e_{L-H}if H \subseteq L.$$

<!-- PAGE 1255 -->

*Chứng minh.* Các phần tử này được chứng minh trong Bourbaki $[25]$ (Chương III, §11, Mục $11)$, nhưng các chứng minh của
$(3)$ và $(4)$ là rất concise. Ta elaborate trên các chứng minh của $(2)$ và $(4)$, chứng minh của $(3)$ đang là đồng dạng. Trong $(2)$ nếu $H\cap L \neq  \emptyset$, thì $e_{H}\wedge e_{L}$ chứa một số vectơ hai lần và do đó $e_{H}\wedge e_{L} = 0$. Ngược lại, $e_{H} \wedge e_{L}$ bao gồm của
$$e_{h1} \wedge \cdots  \wedge e_{hp} \wedge e_{\ell1} \wedge \cdots  \wedge e_{\ell q},$$
Và đến thứ tự dãy của các chỉ số trong tăng thứ tự ta cần đến chuyển vị (transpose) bất kỳ hai các chỉ số $(h_{i}, \ell_{j}$) tương ứng với nghịch đảo, mà cho ta $\rho_{H,L} e_{H\cup L}$. Cho chúng ta bây giờ xét $(4)$. Ta có |L| $= p + q$ và |H| $= p$, và vectơ $q$ $e_{H}^{*}$ ⌟ $e_{L}$ được đặc trưng hóa bởi
$$\langle v^{*}, e_{H}^{*} ⌟e_{L}\rangle = \langle v^{*}\wedge e_{H}^{*}, e_{L}\rangle$$
$$q$$
$$for all v^{*}\in \bigwedge  E^{*}. There are two cases.$$
$$q$$
$$Case 1: H̸ \subseteq L. If so, no matter what v^{*}\in \bigwedge  E^{*}is, since H contains some index h$$
Không trong $L$, hth hàng $(e_{h}^{*}(e_{\ell1}), \dots  , e_{h}^{*}(e_{\ell p+q}))$ của định thức (determinant) $\langle v^{*} \wedge e_{H}^{*}, e_{L}\rangle$ phải là không,
$$q E_{*}$$
$$so \langle ⌟v^{*}\wedge e_{H}^{*}, e_{L}\rangle = 0 for all v^{*}\in \bigwedge  , and since the pairing is nongenerate, we must have$$
$e_{H}^{*} e_{L} = 0$. Trường hợp $2: H \subseteq L$. Trong trường hợp này, cho $v^{*} = e_{L-H}^{*}$, bởi $(2)$ ta có
$$\langle e_{L-H}^{*}, e_{H}^{*} ⌟e_{L}\rangle = \langle e_{L-H}^{*} \wedge e_{H}^{*}, e_{L}\rangle = \langle \rho_{L-H,H} e_{L}^{*}, e_{L}\rangle = \rho_{L-H,H} ,$$
Mà cho ta
$$\langle e_{L-H}^{*}, e_{H}^{*} ⌟e_{L}\rangle = \rho_{L-H,H} .$$
$$The q-vector e_{H}^{*} ⌟e_{L} can be written as a linear combination e_{H}^{*} ⌟e_{L} = \sum  J \lambda_{J} e_{J} with |J| = q$$
Do đó
$$\langle e_{L-H}^{*}, e_{H}^{*} ⌟e_{L}\rangle = \sum_{J}  \lambda_{J} \langle e_{L-H}^{*}, e_{J}\rangle .$$
Theo định nghĩa của cặp, $\langle e_{L-H}^{*}, e_{J}\rangle = 0$ trừ khi $J = L$ - $H$, mà có nghĩa là
$$\langle e_{L-H}^{*}, e_{H}^{*} ⌟e_{L}\rangle = \lambda_{L-H} \langle e_{L-H}^{*}, e_{L-H}\rangle = \lambda_{L-H} ,$$
Do đó $\lambda_{L-H}  = \rho_{L-H,H}$, như đã khẳng định. Bằng cách sử dụng Mệnh đề 34.18, ta có

> **Mệnh đề 34.19.** Cho trái hook
$$q+1q$$
$$⌟: E \times ^E^{*}\longrightarrow ^E^{*},$$
$$q+1-s s$$
$$for every u \in E, x^{*}\in \bigwedge  E^{*}, and y^{*}\in \bigwedge  E^{*}, we have$$
$$u ⌟(x^{*}\wedge y^{*}) = (-1)^{s}(u ⌟x^{*}) \wedge y^{*}+ x^{*}\wedge (u ⌟y^{*}).$$

<!-- PAGE 1256 -->

*Chứng minh.* Ta có thể chứng minh ở trên đồng nhất thức giả sử rằng $x^{*}$ và $y^{*}$ là của tạo thành $e_{I}^{*}$ và $e_{J}^{*}$ bằng cách sử dụng Mệnh đề 34.18 và để lại chi tiết như một bài tập cho độc giả.
$$⌟ q$$
$$Thus,: E \times^{q+1} \bigwedge  E^{*}\longrightarrow \bigwedge  E^{*}is almost an anti-derivation, except that the sign (-1)^{s}$$
Là ứng dụng đến sai nhân tử. Ta có đồng dạng đồng nhất thức cho khác phiên bản của trái hook
$$q+1q$$
$$⌟: E^{*}\times ^E \longrightarrow ^E,$$
Cụ thể là
$$u⌟(x \wedge y) = (-1)^{s}(u^{*}⌟x) \wedge y + x \wedge (u^{*}⌟y)$$
$$q+1-s s$$
$$for every u^{*}\in E^{*}, x \in \bigwedge^{*}  E, and y \in \bigwedge  E.$$
Ứng dụng của công thức này khi $q = 3$ và $s = 2$ cho ta thú vị phương trình. Trong
$$2$$
$$this case, u^{*}\in E^{*}and x, y \in \bigwedge  E, so we get$$
$$u^{*}⌟(x \wedge y) = (u^{*}⌟x) \wedge y + x \wedge (u^{*}⌟y).$$
$$2 ⌟$$
$$In particular,⌟ for x =⌟ y, since x \in \bigwedge  E and u^{*}x \in E, Proposition 34.12 implies that$$
$(u^{*} x) \wedge x = x \wedge (u^{*} x)$, và ta thu được
$$u^{*}⌟(x \wedge x) = 2((u^{*}⌟x) \wedge x).(\dagger )$$
Hệ quả là, $(u^{*}$ ⌟ $x) \wedge x = 0$ khi và chỉ khi $u^{*}$ ⌟ $(x \wedge x) = 0$. Ta sẽ sử dụng điều này đồng nhất thức cùng nhau
$$2$$
$$with Proposition 34.25 to prove that a 2-vector x \in \bigwedge  E is decomposable iff x \wedge x = 0.$$
Nó là cũng khả dĩ/có thể để định nghĩa phải phần trong (interior) tích hoặc phải hook ⌞, bằng cách sử dụng phép nhân trên trái thay vì phép nhân trên phải. Thì ta sử dụng các ánh xạ
$$p+qpq$$
$$⌞:^E^{*}\times ^E \longrightarrow ^E^{*}$$
Để tạo sau đây định nghĩa.
$$p p+q ⌞q$$
$$Definition 34.10. Let u \in \bigwedge  E and z^{*}\in \bigwedge  E^{*}. We define z^{*}u \in \bigwedge  E^{*}to be the$$
Vectơ $q$ một cách duy nhất được định nghĩa như
$$⌞q$$
$$\langle z^{*}u, v\rangle = \langle z^{*}, u \wedge v\rangle ,for all v \in \bigwedge  E.$$
Điều này time ta có thể chứng minh rằng
$$z^{*}⌞(u \wedge v) = (z^{*}⌞u) ⌞v,$$
Do đó họ của các toán tử $⌞_{p,q}$ định nghĩa phải action
$$⌞:^E^{*}\times ^E \longrightarrow ^E^{*}$$

<!-- PAGE 1257 -->
$$of the ring \bigwedge  E on \bigwedge  E^{*}which makes \bigwedge  E^{*}into a right \bigwedge  E-module.$$
Tương tự, ta có các ánh xạ
$$p+qpq$$
$$⌞:^E \times ^E^{*}\longrightarrow ^E$$
Mà trong turn dẫn đến đến sau đây đối ngẫu (dual) formation của phải hook.
$$p p+q ⌞q$$
$$Definition 34.11. Let u^{*}\in \bigwedge  E^{*}and z \in \bigwedge  E. We define zu^{*}\in \bigwedge  to be the q-vector$$
Một cách duy nhất được định nghĩa bởi
$$⌞q$$
$$\langle u^{*}\wedge v^{*}, z\rangle = \langle v^{*}, zu^{*}\rangle ,for all v^{*}\in \bigwedge  E^{*}.$$
Ta có thể chứng minh rằng
$$z ⌞(u^{*}\wedge v^{*}) = (z ⌞u^{*}) ⌞v^{*},$$
Do đó họ của các toán tử $⌞_{p,q}$ định nghĩa phải action
$$⌞:^E \times ^E^{*}\longrightarrow ^E$$
$$of the ring \bigwedge  E^{*}on \bigwedge  E which makes \bigwedge_{+q}  E into a right \bigwedge  E^{*}-module.$$
$$⌟p p q$$
$$Since the left hook: \bigwedge  E \times \bigwedge  E^{*}\longrightarrow \bigwedge_{p}  E^{*}is defined by$$
$$⌟ q p+q$$
$$\langle uz^{*}, v\rangle = \langle z^{*}, v \wedge u\rangle ,for all u \in \bigwedge  E, v \in \bigwedge  E and z^{*}\in \bigwedge  E^{*},$$
Phải hook
$$p+qpq$$
$$⌞:^E^{*}\times ^E \longrightarrow ^E^{*}$$
Bởi
$$⌞p q p+q$$
$$\langle z^{*}u, v\rangle = \langle z^{*}, u \wedge v\rangle ,for all u \in \bigwedge  E, v \in \bigwedge  E, and z^{*}\in \bigwedge  E^{*},$$
Và $v \wedge u = (-1)^{pq}u \wedge v$, ta kết luận rằng
$$⌞  ⌟$$
$$z^{*}u = (-1)^{pq}uz^{*}.$$
Tương tự, vì
$$⌟p q p+q$$
$$\langle v^{*}\wedge u^{*}, z\rangle = \langle v^{*}, u^{*}z\rangle ,for all u^{*}\in \bigwedge_{p}  E^{*}, v^{*}\in \bigwedge_{q}  E^{*}and z \in \bigwedge  E$$
$$⌞  p+q$$
$$\langle u^{*}\wedge v^{*}, z\rangle = \langle v^{*}, zu^{*}\rangle ,for all u^{*}\in \bigwedge  E^{*}, v^{*}\in \bigwedge  E^{*}, and z \in \bigwedge  E,$$
Và $v^{*} \wedge u^{*} = (-1)^{pq}u^{*} \wedge v^{*}$, ta có
$$⌞ ⌟$$
$$zu^{*}= (-1)^{pq}u^{*}z.$$
Ta summarize ở trên các sự kiện trong sau đây mệnh đề.

<!-- PAGE 1258 -->

> **Mệnh đề 34.20.** sau đây các đồng nhất thức đúng:
$$⌞  ⌟p p+q$$
$$z^{*}u = (-1)^{pq}uz^{*}for all u \in \bigwedge  E and all z^{*}\in \bigwedge  E^{*}$$
$$⌞ ⌟p p+q$$
$$zu^{*}= (-1)^{pq}u^{*}zfor all u^{*}\in \bigwedge  E^{*}and all z \in \bigwedge  E.$$
Vì vậy trái và phải hooks là không độc lập, và thực ra mỗi một xác định khác. Hệ quả là, ta có thể thu hẹp của ta attention đến chỉ một của hooks, ví dụ trái hook, nhưng có một vài các tình huống ở đâu nó là đẹp để sử dụng cả hai, ví dụ trong Mệnh đề 34.23. phiên bản của Mệnh đề 34.18 nghiệm đúng cho phải hooks, nhưng beware rằng các chỉ số trong $\rho_{L-H,H}$ là permuted. Điều này hoán vị có đến thực hiện với sự kiện rằng trái hook và phải hook là related thông qua dấu nhân tử.

> **Mệnh đề 34.21.** Với mọi cơ sở (basis) $(e_{1}, \dots  , e_{n})$ của $E$ các tính chất sau đây đúng:
$(1)$ Cho phải hook
$$p+qpq$$
$$⌞:^E \times ^E^{*}\longrightarrow ^E$$
Ta có
$$e_{L} ⌞e_{H}^{*} = 0if H̸ \subseteq L$$
$$e_{L} ⌞e_{H}^{*} = \rho_{H,L-H} e_{L-H}if H \subseteq L.$$
$(2)$ Cho phải hook
$$p+qpq$$
$$⌞:^E^{*}\times ^E \longrightarrow ^E^{*}$$
Ta có
$$e_{L}^{*} ⌞e_{H} = 0if H̸ \subseteq L$$
$$e_{L}^{*} ⌞e_{H} = \rho_{H,L-H} e_{L-H}^{*}if H \subseteq L.$$
$$⌟p p+q q$$
$$Remark:⌟p  Our definition  qof  left hooks as left actions: \bigwedge  ⌞E \times \bigwedge_{p+q}  E\longrightarrow \bigwedge  Eqand$$
$$: \bigwedge  ⌞Ep\times^{p+q} \bigwedge_{+q}  E \longrightarrow \bigwedge  E and right hooks as right actionsq : \bigwedge  E^{*}\times^{p} \bigwedge^{*}  E \longrightarrow \bigwedge^{*}  E^{*}$$
$$and: \bigwedge^{*}  E\times^{p} \bigwedge  E^{*}\longrightarrow \bigwedge  E is identical to the definition found in Fulton and Harris [69]$$
(Phụ lục $B)$. Tuy nhiên, độc giả nên là biết rằng điều này là không một cách phổ dụng accepted ký hiệu. Thực ra, trái hook $u^{*}$ ⌟ $z$ được định nghĩa trong Bourbaki $[25]$ là của ta phải hook $z$ ⌞ $u^{*}$, sai khác dấu $(-1)^{p(p-1)/2}$. Điều này có đến thực hiện với sự kiện rằng Bourbaki sử dụng khác nhau cặp mà cũng liên quan đến extra dấu, cụ thể là
$$\langle v^{*}, u^{*}⌟z\rangle = (-1)^{p(p-1)/2}\langle u^{*}\wedge v^{*}, z\rangle .$$

<!-- PAGE 1259 -->
Một của side-effects của điều này lựa chọn là rằng Bourbaki’s phiên bản của Công thức $(4)$ của Mệnh đề 34.18 (Bourbaki $[25]$, Chương III, trang $168)$ là
$$e_{H}^{*} ⌟e_{L} = 0if H̸ \subseteq L$$
$$e_{H}^{*} ⌟e_{L} = (-1)^{p(p-1)/2}\rho_{H,L-H} e_{L-H}if H \subseteq L,$$
Ở đâu |H| $= p$ và |L| $= p + q$. Điều này tương ứng với Công thức $(1)$ của Mệnh đề 34.21 sai khác dấu nhân tử $(-1)^{p(p-1)/2}$, mà ta tìm horribly confusing. Curiously, older ấn bản của Bourbaki $(1958)$ sử dụng cùng cặp như Fulton và Harris $[69]$. lý do (và advantage) cho điều này thay đổi của dấu quy ước là không rõ ràng đến chúng ta. Ta cũng có sau đây phiên bản của Mệnh đề 34.19 cho phải hook.

> **Mệnh đề 34.22.** Cho phải hook
$$q+1q$$
$$⌞:^E^{*}\times  E \longrightarrow ^E^{*},$$
$$r q+1-r$$
$$for every u \in E, x^{*}\in \bigwedge  E^{*}, and y^{*}\in \bigwedge  E^{*}, we have$$
$$(x^{*}\wedge y^{*}) ⌞u = (x^{*}⌞u) \wedge y^{*}+ (-1)^{r}x^{*}\wedge (y^{*}⌞u).$$

*Chứng minh.* chứng minh liên quan đến các định thức có thể được tìm thấy trong Warner $[192]$, Chương $2$.
$$⌞q+1 q$$
$$Thus,: \bigwedge  ⌞Eq+1\times   E \longrightarrow \bigwedge_{*}  Eisq  an anti-derivation. A similar formula holds for the$$
$$the right hook: \bigwedge^{*}  E \times  E\longrightarrow \bigwedge^{*}  E, namely$$
$$(x \wedge y) ⌞u^{*}= (x ⌞u^{*}) \wedge y + (-1)^{r}x \wedge (y ⌞u^{*}),$$
$$r q+1-r$$
$$for every u^{*}\in E, \in \bigwedge  E, and y \in \bigwedge  E. This formula is used by Shafarevitch⌟ [164] to$$
Định nghĩa hook, nhưng beware rằng Shafarevitch sử dụng trái hook ký hiệu $u^{*} x$ thay vì phải hook ký hiệu. Shafarevitch sử dụng thuật ngữ convolution, mà dường như rất unfortunate. Cho $u \in E$, phải hook $z^{*}$ ⌞ $u$ cũng được ký hiệu $i(u)z^{*}$, và được gọi là insertion toán tử hoặc phần trong (interior) tích. Điều này toán tử đóng quan trọng vai trò trong vi phân hình học.
$$Definition 34.12. Let u \in E and z^{*}\in \bigwedge  n+1(E^{*}). If we view z^{*}as an alternating multilinear$$
Ánh xạ trong $Alt^{n+1}(E; K)$, thì ta định nghĩa $i(u)z^{*} \in Alt^{n}(E; K)$ như cho trước bởi
$$(i(u)z^{*})(v_{1}, \dots  , v_{n}) = z^{*}(u, v_{1}, \dots  , v_{n}).$$
$$⌟ ⌞p$$
$$n-Usingp E_{*} the left hookp E_{*}andn- thep E right hookwe can define two linear maps \gamma  : \bigwedge  E \to$$
$$\bigwedge  and \delta : \bigwedge  \to \bigwedge  as follows:$$

<!-- PAGE 1260 -->

> **Định nghĩa 34.13.** Với mọi cơ sở (basis) $(e_{1}, \dots  , e$) của $E$, nếu ta cho $M = {1, \dots  , n}, e = e_{1}\wedge \cdots \wedge e_{n}$,
$$p En-p E_{*}p E_{*}n-p E$$
$$and e^{*}= e_{1}^{*} \wedge \cdots  \wedge e_{n}^{*}, define \gamma  : \bigwedge  \to \bigwedge^{n}  and \delta : \bigwedge  \to \bigwedge  as$$
$$\gamma (u) = u ⌟e^{*}and\delta (v^{*}) = e ⌞v^{*},$$
$$p p$$
$$for all u \in \bigwedge  E and all v^{*}\in \bigwedge  E^{*}.$$
$$p n-p p n-p$$
$$Proposition 34.23. The  linear maps \gamma  : \bigwedge  E \to \bigwedge  E^{*}and \delta : \bigwedge  E^{*}\to \bigwedge  E are$$
Isomorphims, và $\gamma^{-1} = \delta$. các đẳng cấu $\gamma$ và $\delta$ ánh xạ phân rã được các vectơ đến de-
$$p$$
$$composable vectors. Furthermore, if z \in \bigwedge_{p}  E is decomposable, say z = u_{1} \wedge \cdots  \wedge u_{p} for$$
Một số $u_{i} \in E$, thì $\gamma (z) = v_{1}^{*} \wedge \cdots  \wedge v_{n-}^{*}$ với một số $v_{j}^{*} \in E^{*}$, và $v_{j}^{*}(u_{i}) = 0$ với mọi $i, j$.
$$p$$
$$similar p  propertyn -holdsp  for v^{*} \in \bigwedge_{p}  E^{*}and \delta n(-v^{*}p ). If (e_{1}', \dots  , e_{n}') is any other basis of E and$$
$$\gamma'  : \bigwedge  E \to \bigwedge_{'}  E^{*}and \delta' : \bigwedge  E^{*}\to \bigwedge  E are the corresponding isomorphisms, then$$
$\gamma' = \lambda \gamma$ và $\delta = \lambda^{-1} \delta$ với một số khác không $\lambda  \in K$.

*Chứng minh.* Bằng cách sử dụng Các mệnh đề 34.18 và 34.21, với mọi tập con $J \subseteq {1, \dots  , n} = M$ sao cho |J| $= p$, ta có
$$\gamma (e_{J}) = e_{J} ⌟e^{*}= \rho_{M-J,J} e_{M-J}^{*}and\delta (e_{M-J}^{*}) = e ⌞e_{M-J}^{*} = \rho_{M-J,J} e_{J}.$$
Do đó,
$$\delta  \circ \gamma (e_{J}) = \rho_{M-J,J} \rho_{M-J,J} e_{J} = e_{J},$$
Vì $\rho_{M-J,J}  = \pm 1$. đồng dạng kết quả nghiệm đúng cho $\gamma  \circ \delta$. Điều này suy ra rằng
$$\delta  \circ \gamma  = idand\gamma  \circ \delta  = id.$$
Do đó, $\gamma$ và $\delta$ là nghịch đảo các đẳng cấu.
$$p$$
$$If z \in \bigwedge  E is decomposable, then z = u_{1} \wedge \cdots  \wedge u_{p} where u_{1}, \dots  , u_{p} are linearly inde-$$
Pendent vì $z \neq  0$, và ta có thể chọn cơ sở (basis) của $E$ của tạo thành $(u_{1}, \dots  , u_{n})$. Thì ở trên các công thức chỉ ra rằng
$$\gamma (z) = \pm u_{p+1}^{*} \wedge \cdots  \wedge u_{n}^{*}.$$
Vì $(u_{1}^{*}, \dots  , u_{n}^{*})$ là đối ngẫu (dual) cơ sở (basis) của $(u_{1}, \dots  , u_{n})$, ta có $u_{i}^{*} (u_{j}) = \delta_{ij}$, Nếu $(e_{1}', \dots  , e_{n}')$ là bất kỳ
$$n$$
$$other basis of E, because \bigwedge  E has dimension 1, we have$$
$$e_{1}' \wedge \cdots  \wedge e_{n}' = \lambda e_{1} \wedge \cdots  \wedge e_{n}$$
Với một số khác không $\lambda  \in K$, và rest là tầm thường.
$$n-1$$
$$1 E_{*}Applying Proposition 34.23 to the casen where-1 E p = n -1, the isomorphism \gamma  : \bigwedge_{1}  E_{*}E \to$$
$$\bigwedge  maps indecomposable vectors in \bigwedge  to indecomposablen-1  vectors in \bigwedge  = E^{*}.$$
$$But every vector in E^{*}is decomposable, so every vector in \bigwedge  E is decomposable.$$
$$n-1$$
$$Corollary 34.24. If E is a finite-dimensional vector space, then every vector in \bigwedge  E is$$
Phân rã được.
