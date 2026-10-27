# Chuyển vị (transpose) của Ánh xạ tuyến tính (linear map) và của Ma trận


<!-- PAGE 436 -->
Ta để lại như một bài tập sự kiện rằng mọi không gian con V̸ $= E$ của không gian vectơ (vector space) $E$ là giao của tất cả các siêu phẳng rằng chứa $V$. Ta bây giờ xét khái niệm của chuyển vị (transpose) của ánh xạ tuyến tính (linear map) và của ma trận.

## 11.6 Chuyển vị (transpose) của Ánh xạ tuyến tính (linear map) và của Ma trận

Cho trước ánh xạ tuyến tính (linear map) $f$: $E \to F$, nó là khả dĩ/có thể để định nghĩa ánh xạ $f^{\top}$: $F^{*} \to E^{*}$ mà có một số thú vị các tính chất.

> **Định nghĩa 11.5.** Cho trước ánh xạ tuyến tính (linear map) $f$: $E \to F$, chuyển vị (transpose) $f^{\top}$: $F^{*} \to E^{*}$ của $f$ là ánh xạ tuyến tính (linear map) được định nghĩa sao cho
$$f^{\top} (v^{*}) = v^{*}\circ f,for every v^{*}\in F^{*} ,$$
Như được hiển thị trong biểu đồ ở dưới:
$$EF$$
$$\overline{B}^{f}\overline{B}$$
$$\overline{B} B$$
$$BB$$
$$BB^{v*}$$
$$f\top (v*)$$
$$K.$$
Tương đương, ánh xạ tuyến tính (linear map) $f^{\top}$: $F^{*} \to E^{*}$ được định nghĩa sao cho
$$\langle v^{*}, f(u)\rangle = \langle f^{\top} (v^{*}), u\rangle ,(*)$$
Với mọi $u \in E$ và tất cả $v^{*} \in F^{*}$. Nó là dễ để kiểm chứng rằng các tính chất sau đây đúng:
$$(f + g)^{\top}= f^{\top} + g^{\top}$$
$$(g \circ f)^{\top}= f^{\top} \circ g^{\top}$$
$$id_{E}^{\top} = id_{E*}.$$
 Lưu ý reversal của hợp thành trên vế phải của $(g \circ f)^{\top} = f^{\top} \circ g^{\top}$. phương trình $(g \circ f)^{\top} = f^{\top} \circ g^{\top}$ suy ra sau đây hữu ích mệnh đề.

> **Mệnh đề 11.8.** Nếu $f$: $E \to F$ là bất kỳ ánh xạ tuyến tính (linear map), thì các tính chất sau đây đúng:
$(1)$ Nếu $f$ là đơn ánh (injective), thì $f^{\top}$ là toàn ánh (surjective).
$(2)$ Nếu $f$ là toàn ánh (surjective), thì $f^{\top}$ là đơn ánh (injective).

<!-- PAGE 437 -->

*Chứng minh.* Nếu $f$: $E \to F$ là đơn ánh (injective), thì nó có phép co rút (retraction) $r: F \to E$ sao cho $r \circ f = id_{E}$, và nếu $f$: $E \to F$ là toàn ánh (surjective), thì nó có mục $s: F \to E$ sao cho $f \circ s = id_{F}$. Bây giờ nếu $f$: $E \to F$ là đơn ánh (injective), thì ta có
$$(r \circ f)^{\top}= f^{\top} \circ r^{\top}= id_{E*},$$
Mà suy ra rằng $f^{\top}$ là toàn ánh (surjective), và nếu $f$ là toàn ánh (surjective), thì ta có
$$(f \circ s)^{\top}= s^{\top}\circ f^{\top} = id_{F*},$$
Mà suy ra rằng $f^{\top}$ là đơn ánh (injective). sau đây mệnh đề cho tự nhiên interpretation của đối ngẫu (dual) $(E/U)^{*}$ của không gian thương (quotient space) $E/U$.

> **Mệnh đề 11.9.** Với mọi không gian con $U$ của không gian vectơ (vector space) $E$, nếu $p: E \to E/U$ là chính tắc toàn ánh lên $E/U$, thì $p^{\top}$ là đơn ánh (injective) và
$$\mathrm{Im}(p^{\top}) = U^{0}= (\mathrm{Ker} (p))^{0}.$$
Vì vậy, $p^{\top}$ là tuyến tính đẳng cấu giữa $(E/U)^{*}$ và $U^{0}$.

*Chứng minh.* Vì $p$ là toàn ánh (surjective), theo Mệnh đề 11.8, ánh xạ $p^{\top}$ là đơn ánh (injective). Hiển nhiên, $U =$ Ker $(p)$. Nhận thấy rằng $Im(p^{\top})$ bao gồm của tất cả các dạng tuyến tính $\psi  \in E^{*}$ sao cho $\psi  = \phi  \circ p$ với một số $\phi  \in (E/U)^{*}$, và vì Ker $(p) = U$, ta có $U \subseteq$ Ker $(\psi$). Ngược lại với mọi dạng tuyến tính (linear form) $\psi  \in E^{*}$, nếu $U \subseteq$ Ker $(\psi$), thì $\psi$ các nhân tử qua $E/U$ như $\psi  = \overline{\psi} \circ p$ như được hiển thị trong sau đây giao hoán biểu đồ
$$EE/U$$
$$\overline{C}^{p}\overline{C}$$
$$\overline{C} C$$
$$CC$$
$$CC$$
$$\psi C^{\psi}!$$
$$K,$$
Ở đâu $\overline{\psi}: E/U \to K$ được cho bởi
$$\overline{\psi}(\overline{v}) = \psi (v),v \in E,$$
$$where \overline{v} \in E/U denotes the equivalence class of v \in E. \frac{The}{v'} map \overline{\psi} does  not depend on the$$
Representative được chọn trong lớp tương đương (equivalence class) $\overline{v}$, vì nếu $=\overline{v}$, nghĩa là v' - $v = u \in U$, thì $\psi$ (v') $= \psi (v + u) = \psi (v) + \psi (u) = \psi (v) + 0 = \psi (v)$. Vì vậy, ta có
$$\mathrm{Im}(p^{\top}) = {\phi  \circ p | \phi  \in (E/U)^{*}}$$
$$= {\psi : E \to K | U \subseteq \mathrm{Ker} (\psi )}$$
$$= U^{0} ,$$
Mà chứng minh kết quả của chúng ta.

<!-- PAGE 438 -->
Mệnh đề 11.9 cho ta một cái khác chứng minh của phần $(b)$ của đối ngẫu định lý (định lý 11.4) rằng thực hiện không liên quan đến sự tồn tại của các cơ sở (trong vô hạn số chiều).

> **Mệnh đề 11.10.** Với mọi không gian vectơ (vector space) $E$ và bất kỳ không gian con $V$ của $E$, ta có $V^{00} = V$.

*Chứng minh.* Ta bắt đầu bởi observing rằng $V^{0} = V^{000}$. Điều này là bởi vì, với mọi không gian con $U$ của $E^{*}$, ta có $U \subseteq U^{00}$, do đó $V^{0} \subseteq V^{000}$. Hơn nữa, $V \subseteq V^{00}$ nghiệm đúng, và với mọi hai các không gian con $M, N$ của $E$, nếu $M \subseteq N$ thì $N^{0} \subseteq N^{0}$, do đó ta thu được $V^{000} \subseteq V^{0}$. Viết $V_{1} = V^{00}$, sao cho $V_{1}^{0} = V^{000} = V^{0}$. Ta muốn để chứng minh rằng $V_{1} = V$. Vì $V \subseteq V_{1} = V^{00}$, phép chiếu chính tắc (canonical projection) $p_{1}$: $E \to E/V_{1}$ các nhân tử như $p_{1} = f \circ p$ như trong biểu đồ ở dưới,
$$EE/V$$
$$\overline{C}^{p}\overline{C}$$
$$\overline{C} C$$
$$CC$$
$$CCf$$
$$p1C$$
$$!$$
$$E/V_{1}$$
Ở đâu $p: E \to E/V$ là phép chiếu chính tắc (canonical projection) lên $E/V$ và $f$: $E/V \to E/V_{1}$ là thương ánh xạ được cảm sinh bởi $p_{1}$, với $f(\overline{u}_{E/V}$) $= p_{1}(u) = \overline{u}_{E/V1}$, với mọi $u \in E$ (vì $V \subseteq V_{1}$, nếu $u$ - u' $= v \in V$, thì $u$ - u' $= v \in V_{1}$, do đó $p_{1}(u) = p_{1}(u'))$. Vì $p_{1}$ là toàn ánh (surjective), do đó là $f$. Ta muốn để chứng minh rằng $f$ là thực sự đẳng cấu, và cho điều này, nó là đủ để chỉ ra rằng $f$ là đơn ánh (injective). Bởi transposing tất cả các ánh xạ, ta thu được giao hoán biểu đồ
$$\top$$
$$E^{*}(E/V )^{*}$$
$$\overline{d}^{p}\overline{HHHHHHHHHH}$$
$$f\top$$
$$p\top$$
$$1$$
$$(E/V_{1})^{*},$$
Nhưng theo Mệnh đề 11.9, các ánh xạ $p^{\top}: (E/V )^{*} \to V^{0}$ và $p_{1}^{\top}$: $(E/V_{1})^{*} \to V_{1}^{0}$ là đẳng cấu, và vì $V^{0} = V_{1}^{0}$, ta có kết quả sau biểu đồ ở đâu cả hai $p^{\top}$ và $p_{1}^{\top}$ là các đẳng cấu:
$$\top$$
$$V^{0} (E/V )^{*}$$
$$\overline{d}^{p}\overline{HHHHHHHHHH}$$
$$f\top$$
$$p\top$$
$$1$$
$$(E/V_{1})^{*}.$$
Vì vậy, $f^{\top} = (p^{\top})^{-1}\circ p_{1}^{\top}$ là đẳng cấu. Ta khẳng định rằng điều này suy ra rằng $f$ là đơn ánh (injective). Nếu $f$ là không đơn ánh (injective), thì tồn tại một $x \in E/V$ sao cho x̸ $= 0$ và f(x) $= 0$, do đó với mọi $\phi  \in (E/V_{1})^{*}$, ta có $f^{\top} (\phi )(x) = \phi$ (f(x)) $= 0$. Tuy nhiên, ở đó là dạng tuyến tính (linear form) $\psi  \in (E/V )^{*}$ sao cho $\psi (x) = 1$, do đó $\psi  \neq  f^{\top} (\phi$) với mọi $\phi  \in (E/V_{1})^{*}$, contradicting sự kiện rằng $f^{\top}$ là toàn ánh (surjective). để tìm như vậy dạng tuyến tính (linear form) $\psi$, chọn bất kỳ supplement $W$ của Kx trong $E/V$, sao cho $E/V =$ Kx $\oplus W (W$ là siêu phẳng (hyperplane) trong $E/V$ không chứa $x)$, và định nghĩa $\psi$ là không

<!-- PAGE 439 -->
Trên $W$ và $1$ trên $x.^{1}$ Vì vậy, $f$ là đơn ánh (injective), và vì ta đã biết rằng nó là toàn ánh (surjective), nó là song ánh (bijective). Điều này có nghĩa là chính tắc ánh xạ $f$: $E/V \to E/V_{1}$ với $V \subseteq V_{1}$ là đẳng cấu, mà suy ra rằng $V = V_{1} = V^{00}$ (ngược lại, nếu $v \in V_{1}$ - $V$, thì $p_{1}(v) = 0$, do đó f(p(v)) $= p_{1}(v) = 0$, nhưng p(v) $\neq  0$ vì $v \in / V$, và $f$ là không đơn ánh (injective)). sau đây mệnh đề chỉ ra relationship giữa tính trực giao và phép chuyển vị.

> **Mệnh đề 11.11.** Cho trước ánh xạ tuyến tính (linear map) $f$: $E \to F$, với mọi không gian con $V$ của $E$, ta có
$$f(V )^{0}= (f^{\top})^{-1}(V^{0}) = {w^{*}\in F^{*}| f^{\top}(w^{*}) \in V^{0}}.$$
Hệ quả là,
$$\mathrm{Ker} f^{\top} = (\mathrm{Im} f)^{0}.$$
Ta cũng có
$$\mathrm{Ker} f = (\mathrm{Im} f^{\top} )^{0}.$$

*Chứng minh.* Ta có
$$\langle w^{*}, f(v)\rangle = \langle f^{\top} (w^{*}), v\rangle ,$$
Với mọi $v \in E$ và tất cả $w^{*} \in F^{*}$, và do đó, ta có $\langle w^{*}, f(v)\rangle = 0$ với mọi $v \in V$, i.e. $w^{*} \in$ f(V $)^{0}$ khi và chỉ khi $\langle f^{\top}(w^{*}), v\rangle = 0$ với mọi $v \in V$ khi và chỉ khi $f^{\top}(w^{*}) \in V^{0}$, i.e. $w^{*} \in (f^{\top})^{-1}(V^{0})$, chứng minh rằng
$$f(V )^{0}= (f^{\top})^{-1}(V^{0}).$$
Vì ta đã được quan sát rằng $E^{0} = (0)$, đặt $V = E$ trong ở trên đồng nhất thức ta thu được rằng
$$\mathrm{Ker} f^{\top} = (\mathrm{Im} f)^{0}.$$
Từ phương trình
$$\langle w^{*}, f(v)\rangle = \langle f^{\top} (w^{*}), v\rangle ,$$
Ta suy ra rằng $v \in$ (Im $f^{\top})^{0}$ khi và chỉ khi $\langle f^{\top}(w^{*}), v\rangle = 0$ với mọi $w^{*} \in F^{*}$ khi và chỉ khi $\langle w^{*}, f(v)\rangle = 0$ với mọi $w^{*} \in F^{*}$. Giả sử rằng $v \in$ (Im $f^{\top} )^{0}$. Nếu ta chọn cơ sở (basis) $(w_{i})_{i\in I}$ của $F$, thì ta có các dạng tuyến tính $w_{i}^{*}$: $F \to K$ sao cho $w_{i}^{*} (w_{j}) = \delta_{ij}$, và vì ta phải có $\langle w_{i}^{*} , f(v)\rangle = 0$ với mọi $i \in$ I và $(w_{i})_{i\in I}$ là cơ sở (basis) của $F$, ta kết luận rằng f(v) $= 0$, và do đó $v \in$ Ker $f$ (điều này là bởi vì $\langle w_{i}^{*} , f(v)\rangle$ là hệ số của f(v) liên kết với cơ sở (basis) vectơ $w_{i})$. Ngược lại, nếu $v \in$ Ker $f$, thì $\langle w^{*}, f(v)\rangle = 0$ với mọi $w^{*} \in F^{*}$, do đó ta kết luận rằng $v \in$ (Im $f^{\top} )^{0}$. Vì vậy, $v \in$ (Im $f^{\top})^{0}$ khi và chỉ khi $v \in$ Ker $f$; nghĩa là,
$$\mathrm{Ker} f = (\mathrm{Im} f^{\top} )^{0},$$
Như đã khẳng định. $\overline{1}\overline{Using} \overline{Zorn’s} \overline{lemma,} \overline{we} \overline{pick} \overline{W} \overline{maximal}$ trong số tất cả các không gian con của $E/V$ sao cho Kx $\cap W = (0)$; thì, $E/V =$ Kx $\oplus W$.

<!-- PAGE 440 -->
Sau đây định lý chỉ ra relationship giữa hạng (rank) của $f$ và hạng (rank) của $f^{\top}$.

> **Định lý 11.12.** Cho trước ánh xạ tuyến tính (linear map) $f$: $E \to F$, các tính chất sau đây đúng.
() đối ngẫu (dual) (Im $f)^{*}$ của Im $f$ là đẳng cấu đến Im $f^{\top} = f^{\top} (F^{*}$); rằng là,
$$\sim$$
$$(\mathrm{Im} f)^{*}= \mathrm{Im} f^{\top}.$$
$(b)$ Nếu $F$ là hữu hạn dimensional, thì rk(f) $= rk(f^{\top}$).

*Chứng minh.* () Xét các ánh xạ tuyến tính (linear maps)
$$pj$$
$$E\longrightarrow \mathrm{Im} f\longrightarrow F,$$
$$pfj$$
Ở đâu $E \longrightarrow$ Im $f$ là toàn ánh (surjective) ánh xạ được cảm sinh bởi $E \longrightarrow F$, và Im $f \longrightarrow F$ là đơn ánh (injective) inclusion ánh xạ của Im $f$ vào $F$. Theo Định nghĩa, $f = j \circ p$. để đơn giản hóa ký hiệu,
$$p$$
Cho $I =$ Im $f$. Theo Mệnh đề 11.8, vì $E \longrightarrow$ I là toàn ánh (surjective), $I^{*p\top}\longrightarrow E^{*}$ là đơn ánh (injective), và
$$j$$
Vì Im $f \longrightarrow F$ là đơn ánh (injective), $F^{*j\top}\longrightarrow I^{*}$ là toàn ánh (surjective). Vì $f = j \circ p$, ta cũng có
$$f^{\top} = (j \circ p)^{\top}= p^{\top}\circ j^{\top},$$
$$j\top p\top$$
Và vì $F^{*} \longrightarrow I^{*}$ là toàn ánh (surjective), và $I^{*} \longrightarrow E^{*}$ là đơn ánh (injective), ta có đẳng cấu giữa (Im $f)^{*}$ và $f^{\top} (F^{*}$).
$(b)$ Ta đã được lưu ý rằng Phần () của Định lý 11.4 chỉ ra rằng dim(F) $= dim(F^{*}$), với mọi không gian vectơ (vector space) $F$ của hữu hạn số chiều. Hệ quả là, dim(Im $f) =$ dim((Im $f)^{*})$, và do đó, bởi Phần () ta có rk(f) $= rk(f^{\top}$).
Nhận xét: Khi cả hai $E$ và $F$ là hữu hạn chiều, ở đó là cũng đơn giản chứng minh của $(b)$ rằng không’t sử dụng kết quả của Phần (). Theo Định lý 11.4(c)
$$\dim(\mathrm{Im} f) + \dim((\mathrm{Im} f)^{0}) = \dim(F),$$
Và theo Định lý 6.16
$$\dim(\mathrm{Ker} f^{\top} ) + \dim(\mathrm{Im} f^{\top} ) = \dim(F^{*} ).$$
Hơn nữa, theo Mệnh đề 11.11, ta có
$$\mathrm{Ker} f^{\top} = (\mathrm{Im} f)^{0},$$
Và vì $F$ là hữu hạn chiều dim(F) $= dim(F^{*}$), do đó ta suy ra
$$\dim(\mathrm{Im} f) + \dim((\mathrm{Im} f)^{0}) = \dim((\mathrm{Im} f)^{0}) + \dim(\mathrm{Im} f^{\top} ),$$
Mà cho ta dim(Im $f) =$ dim(Im $f^{\top}$); rằng là, rk(f) $= rk(f^{\top}$).

<!-- PAGE 441 -->

> **Mệnh đề 11.13.** Nếu $f$: $E \to F$ là bất kỳ ánh xạ tuyến tính (linear map), thì sau đây các đồng nhất thức đúng:
$$\mathrm{Im} f^{\top} = (\mathrm{Ker} (f))^{0}$$
$$\mathrm{Ker} (f^{\top} ) = (\mathrm{Im} f)^{0}$$
$$\mathrm{Im} f = (\mathrm{Ker} (f^{\top} )^{0}$$
$$\mathrm{Ker} (f) = (\mathrm{Im} f^{\top} )^{0}.$$

*Chứng minh.* phương trình Ker $(f^{\top}) =$ (Im $f)^{0}$ có đã đã được được chứng minh trong Mệnh đề 11.11. Bởi đối ngẫu định lý (Ker $(f))^{00} =$ Ker $(f)$, do đó từ Im $f^{\top} =$ (Ker $(f))^{0}$ ta thu được Ker $(f) =$ (Im $f^{\top})^{0}$. Tương tự, (Im $f)^{00} =$ Im $f$, do đó từ Ker $(f^{\top}) =$ (Im $f)^{0}$ ta thu được Im $f =$ (Ker $(f^{\top} )^{0}$. Vì vậy, những gì là trái được chứng minh là rằng Im $f^{\top} =$ (Ker $(f))^{0}$. Cho $p: E \to E/Ker (f)$ là chính tắc toàn ánh, $\overline{f}\overline{:} E/Ker (f) \to$ Im $f$ là đẳng cấu được cảm sinh bởi $f$, và $j$: Im $f \to F$ là inclusion ánh xạ. Thì, ta có
$$f = j \circ \overline{f} \circ p,$$
Mà suy ra rằng
$$f^{\top} = p^{\top}\circ \overline{f}^{\top}\circ j^{\top}.$$
Vì $p$ là toàn ánh (surjective), $p^{\top}$ là đơn ánh (injective), vì $j$ là đơn ánh (injective), $j^{\top}$ là toàn ánh (surjective), và vì $\overline{f}$ là song ánh (bijective), $\overline{f}^{\top}$ là cũng song ánh (bijective). Suy ra rằng $(E/Ker (f))^{*} = Im(\overline{f}^{\top} \circ j^{\top})$, và ta có
$$\mathrm{Im} f^{\top} = \mathrm{Im} p^{\top}.$$
Vì $p: E \to E/Ker (f)$ là chính tắc toàn ánh, theo Mệnh đề 11.9 ứng dụng đến $U =$ Ker $(f)$, ta thu được
$$\mathrm{Im} f^{\top} = \mathrm{Im} p^{\top}= (\mathrm{Ker} (f))^{0},$$
Như đã khẳng định. Trong tóm tắt, phương trình
$$\mathrm{Im} f^{\top} = (\mathrm{Ker} (f))^{0}$$
Áp dụng trong bất kỳ số chiều, và nó suy ra rằng
$$\mathrm{Ker} (f) = (\mathrm{Im} f^{\top} )^{0}.$$
Sau đây mệnh đề chỉ ra relationship giữa ma trận biểu diễn ánh xạ tuyến tính (linear map) $f$: $E \to F$ và ma trận biểu diễn của nó chuyển vị (transpose) $f^{\top}$: $F^{*} \to E^{*}$.

> **Mệnh đề 11.14.** Cho $E$ và $F$ là hai các không gian vectơ, và cho $(u_{1}, \dots  , u_{n})$ là cơ sở (basis) cho $E$ và $(v_{1}, \dots  , v_{m})$ là cơ sở (basis) cho $F$. Cho trước bất kỳ ánh xạ tuyến tính (linear map) $f$: $E \to F$, nếu M(f) là $m \times$ n- ma trận biểu diễn $f$ w.r.t. các cơ sở $(u_{1}, \dots  , u_{n})$ và $(v_{1}, \dots  , v_{m})$, thì ma trận cỡ $n \times m$ $M(f^{\top}$) biểu diễn $f^{\top}$: $F^{*} \to E^{*}$ w.r.t. đối ngẫu (dual) các cơ sở $(v_{1}^{*}, \dots  , v_{m}^{*})$ và $(u_{1}^{*}, \dots  , u_{n}^{*})$ là chuyển vị (transpose) $M(f)^{\top}$ của M(f).

<!-- PAGE 442 -->

*Chứng minh.* Nhắc lại rằng phần tử (entry) $a_{i j}$ trong hàng $i$ và cột $j$ của M(f) là tọa độ thứ $i$ của $f(u_{j})$ trên cơ sở (basis) $(v_{1}, \dots  , v_{m})$. Theo định nghĩa của $v_{i}^{*}$, ta có $\langle v_{i}^{*} , f(u_{j})\rangle = a_{i j}$. phần tử (entry) $a_{j i}^{\top}$ trong hàng $j$ và cột $i$ của $M(f^{\top})$ là tọa độ thứ $j$ của
$$f^{\top} (v_{i}^{*} ) = a_{1i}^{\top}u_{1}^{*} + \cdots  + a_{j i}^{\top}u_{j}^{*} + \cdots  + a_{n i}^{\top}u_{n}^{*}$$
Trên cơ sở (basis) $(u_{1}^{*}, \dots  , u_{n}^{*})$, mà là chỉ $a_{j i}^{\top} = f^{\top}(v_{i}^{*} )(u_{j}) = \langle f^{\top}(v_{i}^{*}$), $u_{j}\rangle$. Vì
$$\langle v_{i}^{*} , f(u_{j})\rangle = \langle f^{\top}(v_{i}^{*} ), u_{j}\rangle ,$$
Ta có $a_{i j} = a_{j i}^{\top}$, chứng minh rằng $M(f^{\top}) = M(f)^{\top}$. Ta bây giờ có thể cho rất ngắn chứng minh của sự kiện rằng hạng (rank) của ma trận bằng hạng (rank) của chuyển vị (chuyển vị (transpose)) của nó.

> **Mệnh đề 11.15.** Cho trước một ma trận cỡ $m \times  n$ $A$ trên trường $K$, ta có rk() $= rk(A^{\top})$.

*Chứng minh.* ma trận $A$ tương ứng với ánh xạ tuyến tính (linear map) $f$: $K^{n} \to K^{m}$, và theo Định lý 11.12, rk(f) $= rk(f^{\top}$). Theo Mệnh đề 11.14, ánh xạ tuyến tính (linear map) $f^{\top}$ tương ứng với $A^{\top}$. Vì rk() $=$ rk(f), và $rk(A^{\top}) = rk(f^{\top}$), ta kết luận rằng rk() $= rk(A^{\top})$. Do đó, cho trước một ma trận cỡ $m\times n$ $A$, cực đại số của các cột độc lập tuyến tính bằng cực đại số của các hàng độc lập tuyến tính. Có khác các cách của chứng minh sự kiện này rằng thực hiện không liên quan đến không gian đối ngẫu (dual space), nhưng thay vì một số sơ cấp các phép biến đổi trên các hàng và các cột. Mệnh đề 11.15 ngay lập tức cho ta sau đây tiêu chuẩn cho xác định hạng (rank) của ma trận:

> **Mệnh đề 11.16.** Cho trước bất kỳ ma trận cỡ $m\times n$ $A$ trên trường $K$ (typically $K =\mathbb{R}$ hoặc $K =\mathbb{C})$, hạng (rank) của $A$ là cực đại tự nhiên số $r$ sao cho có một khả nghịch $r\times r$ ma trận con của $A$ thu được bởi chọn $r$ các hàng và $r$ các cột của $A$. Ví dụ, ma trận cỡ $3 \times  2$
$$A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \\ a_{31} & a_{32} \end{pmatrix}$$
Có hạng (rank) $2$ khi và chỉ khi một của ba $2 \times  2$ các ma trận
$$\begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} \begin{pmatrix} a_{11} & a_{12} \\ a_{31} & a_{32} \end{pmatrix} \begin{pmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{pmatrix}$$
Là khả nghịch. Nếu ta combine Mệnh đề 7.11 với Mệnh đề 11.16, ta thu được kết quả sau tiêu chuẩn cho việc tìm hạng (rank) của ma trận.
