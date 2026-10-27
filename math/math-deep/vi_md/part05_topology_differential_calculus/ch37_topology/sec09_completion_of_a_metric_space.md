# Đầy đủ hóa của Không gian mêtric (metric space)


<!-- PAGE 1410 -->

*Chứng minh.* Giả sử $x \in \overline{A}$. Theo Mệnh đề 37.13, tồn tại một dãy $(a_{n})$ của các điểm $a_{n} \in A$ mà hội tụ đến $x$. Hệ quả là $(a_{n})$ là Dãy Cauchy (Cauchy sequence) trong $E$, và do đó Dãy Cauchy (Cauchy sequence) trong $A$ (vì $a_{n} \in A$ với mọi $n)$. Vì $A$ là đầy đủ, dãy $(a_{n})$ có giới hạn $a \in A$, nhưng vì $E$ là không gian mêtric (metric space) nó là Hausdorff, do đó $a = x$, mà chỉ ra rằng $x \in A$; nghĩa là, $A$ là đóng.

> **Mệnh đề 37.51.** Cho $(E, d)$ là không gian mêtric (metric space), và cho $A$ là tập con của $E$. Nếu $E$ là đầy đủ và nếu $A$ là đóng trong $E$, thì $A$ là đầy đủ.

*Chứng minh.* Cho $(a_{n})$ là Dãy Cauchy (Cauchy sequence) trong $A$. dãy $(a_{n})$ là cũng Dãy Cauchy (Cauchy sequence) trong $E$, và vì $E$ là đầy đủ, nó có giới hạn $x \in E$. Nhưng $a_{n} \in A$ với mọi $n$, do đó theo Mệnh đề 37.13 ta phải có $x \in \overline{A}$. Vì $A$ là đóng, thực sự $x \in A$, mà chứng tỏ rằng $A$ là đầy đủ. tùy ý không gian mêtric (metric space) $(E, d)$ là không nhất thiết đầy đủ, nhưng có một cách xây dựng của không gian mêtric (metric space) (E,d) sao cho $E$ là đầy đủ, và có một liên tục (đơn ánh (injective)) khoảng cách-
$$b b b$$
Bảo toàn ánh xạ $\phi$: $E \to E$ sao cho $\phi (E)$ là trù mật trong $E$. Điều này là tổng quát hóa của
$$b b$$
Cách xây dựng của tập hợp $\mathbb{R}$ của thực các số từ tập hợp $\mathbb{Q}$ của hữu tỷ các số theo Các dãy Cauchy. cách xây dựng này có thể được ngay lập tức được điều chỉnh đến không gian vectơ định chuẩn (normed vector space) $(E, \|\|)$ đến embed $(E, \|\|)$ vào đầy đủ không gian vectơ định chuẩn (normed vector space) $(E, \|\|_{E})$ (Không gian Banach (Banach space)).
$$b$$
$$b$$
Cách xây dựng này được sử dụng heavily trong phép lấy tích phân lý thuyết, ở đâu $E$ là tập hợp của các hàm.

## 37.9 Đầy đủ hóa của Không gian mêtric (metric space)

Trong thứ tự để chứng minh loại của tính duy nhất kết quả cho đầy đủ hóa (E,d) của không gian mêtric (metric space)
$$b b$$
$(E, d)$, ta cần kết quả sau đây về mở rộng liên tục đều (uniformly continuous) hàm. Nhắc lại rằng $E_{0}$ là trù mật trong $E$ khi và chỉ khi $\overline{E}_{0} = E$. Vì $E$ là không gian mêtric (metric space), theo Mệnh đề 37.13, điều này có nghĩa là với mọi $x \in E$, tồn tại một dãy $(x_{n})$ hội tụ đến $x$, với $x_{n} \in E_{0}$.

> **Định lý 37.52.** Cho $E$ và $F$ là hai các không gian mêtric, cho $E_{0}$ là trù mật không gian con của $E$, và cho $f_{0}$: $E_{0} \to F$ là hàm liên tục (continuous function). Nếu $f_{0}$ là liên tục đều (uniformly continuous) và nếu $F$ là đầy đủ, thì tồn tại duy nhất một liên tục đều (uniformly continuous) hàm $f$: $E \to F$ mở rộng $f_{0}$.

*Chứng minh.* Ta suy ra Schwartz’s chứng minh; xem Schwartz $[155]$ (Chương XI, Mục $3$, Định lý $1)$. Bước $1$. Ta bắt đầu bởi xây dựng hàm $f$: $E \to F$ mở rộng $f_{0}$. Vì $E_{0}$ là trù mật trong $E$, với mọi $x \in E$, tồn tại một dãy $(x_{n})$ hội tụ đến $x$, với $x_{n} \in E_{0}$. Thì dãy $(x_{n})$ là Dãy Cauchy (Cauchy sequence) trong $E$. Ta khẳng định rằng $(f_{0}(x_{n}))$ là Dãy Cauchy (Cauchy sequence) trong $F$. Chứng minh của khẳng định. Với mọi $\epsilon  > 0$, vì $f_{0}$ là liên tục đều (uniformly continuous), tồn tại một $\eta  > 0$ sao cho với mọi $(y, z) \in E_{0}$, nếu d(y, $z) \le \eta$, thì $d(f_{0}(y), f_{0}(z)) \le \epsilon$. Vì $(x_{n})$ là Dãy Cauchy (Cauchy sequence) với $x_{n} \in E_{0}$, tồn tại một số nguyên $p > 0$ sao cho nếu $m, n \ge p$, thì $d(x_{m}, x_{n}) \le \eta$, do đó $d(f_{0}(x_{m}), f_{0}(x_{n})) \le \epsilon$, mà chứng tỏ rằng $(f_{0}(x_{n}))$ là Dãy Cauchy (Cauchy sequence) trong $F$.

<!-- PAGE 1411 -->
Vì $F$ là đầy đủ và $(f_{0}(x_{n}))$ là Dãy Cauchy (Cauchy sequence) trong $F$, dãy $(f_{0}(x_{n}))$ hội tụ đến một số phần tử của $F$; ký hiệu điều này phần tử bởi f(x). Bước $2$. Cho chúng ta bây giờ chỉ ra rằng f(x) không phụ thuộc vào dãy $(x_{n})$ hội tụ đến $x$. Giả sử rằng $(x_{n}')$ và $(x_{n}'')$ là hai các dãy của các phần tử trong $E_{0}$ hội tụ đến $x$. Thì mixed dãy
$$x_{0}', x_{0}'', x_{1}', x_{1}'', \dots  , x_{n}', x_{n}'', \dots  ,$$
Cũng hội tụ đến $x$. Suy ra rằng dãy
$$f_{0}(x_{0}'), f_{0}(x_{0}''), f_{0}(x_{1}'), f_{0}(x_{1}''), \dots  , f_{0}(x_{n}'), f_{0}(x_{n}''), \dots  ,$$
Là Dãy Cauchy (Cauchy sequence) trong $F$, và vì $F$ là đầy đủ, nó hội tụ đến một số phần tử của $F$, mà suy ra rằng các dãy $(f_{0}(x_{n}'))$ và $(f_{0}(x_{n}''))$ hội tụ đến cùng giới hạn. Như tóm tắt, ta có được định nghĩa hàm $f$: $E \to F$ bởi
$$f(x) = limf_{0}(x_{n}).$$
$$n\mapsto \infty$$
Với mọi dãy $(x_{n})$ hội tụ đến $x$, với $x_{n} \in E_{0}$. Bước $3$. hàm $f$ mở rộng $f_{0}$. Vì mọi phần tử $x \in E_{0}$ là giới hạn của hằng số dãy $(x_{n})$ với $x_{n} = x$ với mọi $n \ge 0$, theo Định nghĩa f(x) là giới hạn của dãy $(f_{0}(x_{n}))$, mà là hằng số dãy với giá trị $f_{0}(x)$, do đó f(x) $= f_{0}(x)$; nghĩa là, $f$ mở rộng $f_{0}$. Bước $4$. Ta bây giờ chứng minh rằng $f$ là liên tục đều (uniformly continuous). Vì $f_{0}$ là liên tục đều (uniformly continuous), với mọi $\epsilon  > 0$, tồn tại một $\eta  > 0$ sao cho nếu, $b \in E_{0}$ và d(, $b) \le \eta$, thì $d(f_{0}(a), f_{0}(b)) \le \epsilon$. Xét bất kỳ hai các điểm $x, y \in E$ sao cho d(x, $y) \le \eta /2$. Ta khẳng định rằng d(f(x), f(y)) $\le \epsilon$, mà chỉ ra rằng $f$ là liên tục đều (uniformly continuous). Cho $(x_{n})$ là dãy của các điểm trong $E_{0}$ hội tụ đến $x$, và cho $(y_{n})$ là dãy của các điểm trong $E_{0}$ hội tụ đến $y$. Bởi tam giác bất đẳng thức,
$$d(x_{n}, y_{n}) \le d(x_{n}, x) + d(x, y) + d(y, y_{n}) = d(x, y) + d(x_{n}, x) + d(y_{n}, y),$$
Và vì $(x_{n})$ hội tụ đến $x$ và $(y_{n})$ hội tụ đến $y$, tồn tại một số nguyên $p > 0$ sao cho với mọi $n \ge p$, ta có $d(x_{n}, x) \le \eta /4$ và $d(y_{n}, y) \le \eta /4$, và do đó
$$d(x_{n}, y_{n}) \le d(x, y) + \frac{\eta}{2} .$$
Vì ta được giả sử rằng d(x, $y) \le \eta /2$, ta thu được $d(x_{n}, y_{n}) \le \eta$ với mọi $n \ge p$, và bởi uniform tính liên tục của $f_{0}$, ta thu được
$$d(f_{0}(x_{n}), f_{0}(y_{n})) \le \epsilon$$
Với mọi $n \ge p$. Vì khoảng cách hàm trên $F$ là cũng liên tục, và vì $(f_{0}(x_{n}))$ hội tụ đến f(x) và $(f_{0}(y_{n}))$ hội tụ đến f(y), ta suy ra rằng dãy $(d(f_{0}(x_{n}), f_{0}(y_{n})))$ hội tụ đến d(f(x), f(y)). Điều này suy ra rằng d(f(x), f(y)) $\le \epsilon$, như mong muốn.

<!-- PAGE 1412 -->
Bước $5$. Nó vẫn còn để chứng minh rằng $f$ là duy nhất. Vì $E_{0}$ là trù mật trong $E$, với mọi $x \in E$, tồn tại một dãy $(x_{n})$ hội tụ đến $x$, với $x_{n} \in E_{0}$. Vì $f$ mở rộng $f_{0}$ và vì $f$ là liên tục, ta thu được
$$f(x) = limf_{0}(x_{n}),$$
$$n\mapsto \infty$$
Mà chỉ phụ thuộc vào $f_{0}$ và $x$, và chỉ ra rằng $f$ là duy nhất.
Nhận xét: Nó có thể được được hiển thị rằng định lý không có dài hơn nghiệm đúng nếu ta hoặc bỏ qua giả thiết rằng $F$ là đầy đủ hoặc bỏ qua rằng $f_{0}$ là liên tục đều (uniformly continuous). Ví dụ, nếu $E_{0} \neq  E$ và nếu ta cho $F = E_{0}$ và $f_{0}$ là đồng nhất thức hàm, nó là dễ để xem rằng $f_{0}$ không thể được mở rộng đến hàm liên tục (continuous function) từ $E$ đến $E_{0}$ (với mọi $x \in E$ - $E_{0}$, bất kỳ continous mở rộng $f$ của $f_{0}$ sẽ thỏa mãn f(x) $= x$, mà là absurd vì $x \in / E_{0})$. Nếu $f_{0}$ là liên tục nhưng không liên tục đều (uniformly continuous), counter-example có thể được cho trước bằng cách sử dụng $E =\mathbb{R} =\mathbb{R} \cup {\infty$ } được tạo vào không gian mêtric (metric space), $E_{0} =\mathbb{R}, F =\mathbb{R}$, và $f_{0}$ đồng nhất thức hàm; cho chi tiết, xem Schwartz $[155]$ (Chương XI, Mục $3$, trang $134)$.

> **Định nghĩa 37.39.** Nếu $(E, d_{E})$ và $(F, d_{F})$ là hai các không gian mêtric, thì hàm $f$: $E \to F$ là distance-preserving, hoặc phép đẳng cự (isometry), nếu
$$d_{F}(f(x), f(y)) = d_{E}(x, y),for all for all x, y \in E.$$
Nhận thấy rằng phép đẳng cự (isometry) phải là đơn ánh (injective), bởi vì nếu f(x) $=$ f(y), thì $d_{F}(f(x)$, f(y)) $= 0$, và vì $d_{F}(f(x)$, f(y)) $= d_{E}(x, y)$, ta thu được $d_{E}(x, y) = 0$, nhưng $d_{E}(x, y) = 0$ suy ra rằng $x = y$. Cũng, phép đẳng cự (isometry) là liên tục đều (uniformly continuous) (vì ta có thể chọn $\eta  = \epsilon$ đến thỏa mãn điều kiện của uniform tính liên tục). Tuy nhiên, phép đẳng cự (isometry) là không nhất thiết toàn ánh (surjective). Ta bây giờ cho cách xây dựng của đầy đủ hóa của không gian mêtric (metric space). cách xây dựng này là chỉ tổng quát hóa của cổ điển cách xây dựng của $\mathbb{R}$ từ $\mathbb{Q}$ bằng cách sử dụng Các dãy Cauchy.

> **Định lý 37.53.** Cho $(E, d)$ là bất kỳ không gian mêtric (metric space). Có một không gian mêtric đầy đủ (E,d)
$$b b$$
Được gọi là đầy đủ hóa của $(E, d)$, và distance-preserving (liên tục đều (uniformly continuous)) ánh xạ $\phi$: $E \to E$ sao cho $\phi (E)$ là trù mật trong $E$, và sau đây mở rộng tính chất nghiệm đúng: với mọi $b  b$ không gian mêtric đầy đủ $F$ và với mọi liên tục đều (uniformly continuous) hàm $f$: $E \to F$, tồn tại duy nhất một liên tục đều (uniformly continuous) hàm $f$: $E \to F$ sao cho
$$b b$$
$$f =f \circ \phi ,$$
$$b$$
Như được minh họa trong sau đây biểu đồ.
$$EE$$
$$\overline{@}^{\phi}\overline{@} b$$
$$\overline{@}@$$
$$@@$$
$$@@^{fb}$$
$$f$$
$$F.$$
Hệ quả là, với mọi hai các đầy đủ hóa $(E_{1},d_{1})$ và $(E_{2},d_{2})$ của $(E, d)$, tồn tại duy nhất một
$$b b b b$$
Song ánh (bijective) phép đẳng cự (isometry) betwen $(E_{1},d_{1})$ và $(E_{2},d_{2})$.
$$b b b b$$

<!-- PAGE 1413 -->

*Chứng minh.* Xét tập hợp $\mathcal{E}$ của tất cả Các dãy Cauchy $(x_{n})$ trong $E$, và định nghĩa quan hệ $\sim$ trên $\mathcal{E}$ như sau:
$$(x_{n}) \sim (y_{n})iff limd(x_{n}, y_{n}) = 0.$$
$$n\mapsto \infty$$
Nó là dễ để kiểm tra rằng $\sim$ là quan hệ tương đương (equivalence relation) trên $\mathcal{E}$, và cho $E =\mathcal{E}/ \sim$ là thương
$$b$$
Tập hợp, nghĩa là, tập hợp của các lớp tương đương modulo $\sim$. Của ta mục tiêu là để chỉ ra rằng ta có thể endow $E$ với khoảng cách rằng làm cho nó vào không gian mêtric đầy đủ thỏa mãn các điều kiện của $b$ định lý. Ta tiến hành trong một vài các bước. Bước $1$. Thứ nhất, cho chúng ta xây dựng hàm $\phi$: $E \to E$. Với mọi $a \in E$, ta có
$$b$$
Hằng số dãy $(a_{n})$ sao cho $a_{n} = a$ với mọi $n \ge 0$, mà là hiển nhiên Dãy Cauchy (Cauchy sequence). Cho $\phi (a) \in E$ là lớp tương đương (equivalence class) $[(a_{n})]$ của hằng số dãy $(a_{n})$ với $a_{n} = a$ với mọi
$$b$$
$n$. Theo định nghĩa của $\sim$, lớp tương đương (equivalence class) $\phi$ () là cũng lớp tương đương (equivalence class) của tất cả các dãy hội tụ đến. ánh xạ $a \mapsto \phi$ () là đơn ánh (injective) bởi vì không gian mêtric (metric space) là Hausdorff, do đó nếu $a \neq  b$, thì dãy hội tụ đến thực hiện không hội tụ đến $b$. Sau có được định nghĩa khoảng cách trên $E$, ta sẽ kiểm tra rằng $\phi$ là phép đẳng cự (isometry).
$$b$$
Bước $2$. Cho chúng ta bây giờ định nghĩa khoảng cách trên $E$. Cho $\alpha  = [(a_{n})]$ và $\beta  = [(b_{n})]$ là hai
$$b$$
Các lớp tương đương của Các dãy Cauchy trong $E$. tam giác bất đẳng thức suy ra rằng $d(a_{m}, b_{m}) \le d(a_{m}, a_{n}) + d(a_{n}, b_{n}) + d(b_{n}, b_{m}) = d(a_{n}, b_{n}) + d(a_{m}, a_{n}) + d(b_{m}, b_{n})$ và $d(a_{n}, b_{n}) \le d(a_{n}, a_{m}) + d(a_{m}, b_{m}) + d(b_{m}, b_{n}) = d(a_{m}, b_{m}) + d(a_{m}, a_{n}) + d(b_{m}, b_{n})$, mà suy ra rằng
$$|d(a_{m}, b_{m}) -d(a_{n}, b_{n})| \le d(a_{m}, a_{n}) + d(b_{m}, b_{n}).$$
Vì $(a_{n})$ và $(b_{n})$ là Các dãy Cauchy, suy ra rằng $(d(a_{n}, b_{n}))$ là Dãy Cauchy (Cauchy sequence) của không âm các số thực. $Since\mathbb{R}$ là đầy đủ, dãy $(d(a_{n}, b_{n}))$ có giới hạn, mà ta ký hiệu bởi $d(\alpha , \beta$); rằng là, ta tập hợp $b$
$$d(\alpha , \beta ) = limd(a_{n}, b_{n}),\alpha  = [(a_{n})], \beta  = [(b_{n})].$$
$$b$$
$$n\mapsto \infty$$
Bước $3$. Cho chúng ta kiểm tra rằng $d(\alpha , \beta$) không phụ thuộc vào Các dãy Cauchy $(a_{n})$ và
$$b$$
$(b_{n})$ được chọn trong các lớp tương đương $\alpha$ và $\beta$. Nếu $(a_{n}) \sim (a_{n}')$ và $(b_{n}) \sim (b_{n}')$, thì $lim_{n\mapsto \infty} d(a_{n}, a_{n}') = 0$ và $lim_{n\mapsto \infty} d(b_{n}, b_{n}') = 0$, và vì
$$d(a_{n}', b_{n}') \le d(a_{n}', a_{n}) + d(a_{n}, b_{n}) + d(b_{n}, b_{n}') = d(a_{n}, b_{n}) + d(a_{n}, a_{n}') + d(b_{n}, b_{n}')$$
Và
$$d(a_{n}, b_{n}) \le d(a_{n}, a_{n}') + d(a_{n}', b_{n}') + d(b_{n}', b_{n}) = d(a_{n}', b_{n}') + d(a_{n}, a_{n}') + d(b_{n}, b_{n}')$$

<!-- PAGE 1414 -->
Ta có
$$|d(a_{n}, b_{n}) -d(a_{n}', b_{n}')| \le d(a_{n}, a_{n}') + d(b_{n}, b_{n}'),$$
Do đó ta có $lim_{n\mapsto \infty} d(a_{n}', b_{n}') = lim_{n\mapsto \infty} d(a_{n}, b_{n}) = d(\alpha , \beta$). Vì vậy, $d(\alpha , \beta$) là thật vậy tốt
$$b b$$
Được định nghĩa. Bước $4$. Cho chúng ta kiểm tra rằng $\phi$ là thật vậy phép đẳng cự (isometry). Cho trước bất kỳ hai các phần tử $\phi$ () và $\phi (b)$ trong $E$, vì chúng là các lớp tương đương của
$$b$$
Hằng số các dãy $(a_{n})$ và $(b_{n})$ sao cho $a_{n} = a$ và $b_{n} = b$ với mọi $n$, hằng số dãy $(d(a_{n}, b_{n}))$ với $d(a_{n}, b_{n}) =$ d(, $b)$ với mọi $n$ hội tụ đến d(, $b)$, do đó theo Định nghĩa $d(\phi (a), \phi (b)) = lim_{n\mapsto \infty} d(a_{n}, b_{n}) =$ d(, $b)$, mà chỉ ra rằng $\phi$ là phép đẳng cự (isometry). $b$ Bước $5$. Cho chúng ta kiểm chứng rằng $d$ là mêtric trên $E$. Theo Định nghĩa hiển nhiên là $d(\alpha , \beta$) $=$
$$b b b$$
$d(\beta , \alpha$). Nếu $\alpha$ và $\beta$ là hai phân biệt các lớp tương đương, thì với mọi Dãy Cauchy (Cauchy sequence) $(a_{n}) b$ trong lớp tương đương (equivalence class) $\alpha$ và với mọi Dãy Cauchy (Cauchy sequence) $(b_{n})$ trong lớp tương đương (equivalence class) $\beta$, các dãy $(a_{n})$ và $(b_{n})$ là inequivalent, mà có nghĩa là $lim_{n\mapsto \infty} d(a_{n}, b_{n}) \neq  0$, nghĩa là, $d(\alpha , \beta$) $\neq  0$. Hiển nhiên, $d(\alpha , \alpha$) $= 0. b  b$ Với mọi các lớp tương đương $\alpha  = [(a_{n})], \beta  = [(b_{n})]$, và $\gamma  = [(c_{n})]$, ta có tam giác bất đẳng thức
$$d(a_{n}, c_{n}) \le d(a_{n}, b_{n}) + d(b_{n}, c_{n}),$$
Do đó bởi tính liên tục của khoảng cách hàm, bởi chuyển đến giới hạn, ta thu được
$$d(\alpha , \gamma ) \le d(\alpha , \beta ) +d(\beta , \gamma ),$$
$$bb b$$
Mà là tam giác bất đẳng thức cho $d$. Vì vậy, $d$ là khoảng cách trên $E$.
$$b b b$$
Bước $6$. Cho chúng ta chứng minh rằng $\phi (E)$ là trù mật trong $E$. Với mọi $\alpha  = [(a_{n})]$, cho $(x_{n})$ là hằng số
$$b$$
Dãy sao cho $x_{k} = a_{n}$ với mọi $k \ge 0$, sao cho $\phi (a_{n}) = [(x_{n})]$. Thì ta có
$$d(\alpha , \phi (a_{n})) = limd(a_{m}, a_{n}) \le supd(a_{p}, a_{q}).$$
$$b$$
$$m\mapsto \infty p,q\ge n$$
Vì $(a_{n})$ là Dãy Cauchy (Cauchy sequence), $sup_{p,q\ge n} d(a_{p}, a_{q})$ tiến tới đến $0$ như $n$ đi đến vô cực, do đó
$$limd(\alpha , \phi (a_{n})) = 0,$$
$$n\mapsto \infty$$
Mà có nghĩa là dãy $(\phi (a_{n}))$ hội tụ đến $\alpha$, và $\phi (E)$ là thật vậy trù mật trong $E$.
$$b$$
Bước $7$. Cuối cùng, cho chúng ta chứng minh rằng không gian mêtric (metric space) $E$ là đầy đủ.
$$b$$
Cho $(\alpha_{n}$) là Dãy Cauchy (Cauchy sequence) trong $E$. Vì $\phi (E)$ là trù mật trong $E$, với mọi $n > 0$, ở đó
$$b b$$
Một số $a_{n} \in E$ sao cho
$$db(\alpha_{n} , \phi (a_{n})) \le \frac{1}{n} .$$
Vì
$$db(\phi (a_{m}), \phi (a_{n})) \le db(\phi (a_{m}), \alpha_{m} ) + db(\alpha_{m} , \alpha_{n} ) + db(\alpha_{n} , \phi (a_{n})) \le db(\alpha_{m} , \alpha_{n} ) + \frac{1}{m} + \frac{1}{n} ,$$

<!-- PAGE 1415 -->
Và vì $(\alpha_{m}$) là Dãy Cauchy (Cauchy sequence), do đó là $(\phi (a_{n}))$, và như $\phi$ là phép đẳng cự (isometry), dãy $(a_{n})$ là Dãy Cauchy (Cauchy sequence) trong $E$. Cho $\alpha  \in E$ là lớp tương đương (equivalence class) của $(a_{n})$. Vì
$$b$$
$$d(\alpha , \phi (a_{n})) = limd(a_{m}, a_{n})$$
$$b$$
$$m\mapsto \infty$$
Và $(a_{n})$ là Dãy Cauchy (Cauchy sequence), ta suy ra rằng dãy $(\phi (a_{n}))$ hội tụ đến $\alpha$, và vì $d(\alpha_{n} , \phi (a_{n})) \le 1/n$ với mọi $n > 0$, dãy $(\alpha_{n}$) cũng hội tụ đến $\alpha$. Bước $8$. Cho chúng ta chứng minh mở rộng tính chất. Cho $F$ là bất kỳ không gian mêtric đầy đủ và cho $f$: $E \to F$ là bất kỳ liên tục đều (uniformly continuous) hàm. hàm $\phi$: $E \to E$ là phép đẳng cự (isometry)
$$b$$
Và song ánh giữa $E$ và của nó ảnh (image) $\phi (E)$, do đó của nó nghịch đảo $\phi^{-1}$: $\phi (E) \to E$ là cũng phép đẳng cự (isometry), và do đó là liên tục đều (uniformly continuous). Nếu ta cho $g = f \circ \phi^{-1}$, thì $g: \phi (E) \to F$ là liên tục đều (uniformly continuous) hàm, và $\phi (E)$ là trù mật trong $E$, do đó theo Định lý 37.52 có một
$$b$$
Duy nhất liên tục đều (uniformly continuous) hàm $f$: $E \to F$ mở rộng $g = f \circ \phi^{-1}$; xem biểu đồ
$$b b$$
Ở dưới:
$$E\overline{R}\overline{R}^{\phi-1}\phi (E)\subseteq E$$
$$\overline{R}\overline{R} Db$$
$$\overline{R} RD$$
$$RRDD$$
$$RRD^{g}$$
$$RRDD$$
$$RRD$$
$$fRRD _{b}^{f}$$
$$RR"$$
$$($$
$$F$$
Điều này có nghĩa là
$$f|\phi (E) = f \circ \phi^{-1} ,$$
$$b$$
Mà suy ra rằng
$$(f|\phi (E)) \circ \phi  = f,$$
$$b$$
Rằng là, $f = f \circ \phi$, như được minh họa trong biểu đồ ở dưới:
$$b$$
$$EE$$
$$\overline{@}^{\phi}\overline{@} b$$
$$\overline{@}@$$
$$@@$$
$$@@^{fb}$$
$$f$$
$$F$$
Nếu $h: E \to F$ là bất kỳ khác liên tục đều (uniformly continuous) hàm sao cho $f = h \circ \phi$, thì
$$b$$
$g = f \circ \phi^{-1} = h|\phi (E)$, do đó $h$ là liên tục đều (uniformly continuous) hàm mở rộng $g$, và theo Định lý 37.52, ta có có $h = f$, do đó $f$ là thật vậy duy nhất.
$$b b$$
Bước $9$. Tính duy nhất của đầy đủ hóa (E,d) sai khác song ánh (bijective) phép đẳng cự (isometry).
$$b b$$
Cho $(E_{1},d_{1})$ và $(E_{2},d_{2})$ là bất kỳ hai các đầy đủ hóa của $(E, d)$. Thì ta có hai uniformly
$$b b b b$$
Liên tục các phép đẳng cự $\phi_{1}$: $E \to E_{1}$ và $\phi_{2}$: $E \to E_{2}$, do đó bởi duy nhất mở rộng tính chất,
$$bb$$
Ở đó tồn tại duy nhất liên tục đều (uniformly continuous) các ánh xạ $\phi_{2}$: $E_{1} \to E_{2}$ và $\phi_{1}$: $E_{2} \to E_{1}$ sao cho
$$c bb c bb$$
Sau đây các biểu đồ giao hoán:
$$EE_{1}EE_{2}$$
$$\overline{>}^{\phi1}\overline{>} b\overline{@}^{\phi2}\overline{@} b$$
$$\overline{>}>\overline{@}@$$
$$>>@@$$
$$\phi >\phi 2\phi @\phi 1$$
$$2>c1@c$$
$$E_{2}E_{1}.$$
$$bb$$

<!-- PAGE 1416 -->
Hệ quả là ta có kết quả sau giao hoán các biểu đồ:
$$E_{2}E_{1}$$
$$?b?b$$
$$ ~$$
$$  ~~$$
$$\phi 2 \phi 1~$$
$$ \phi 1~\phi 2$$
$$ _{\phi} c~c$$
$$ ~_{\phi}$$
$$~$$
$$EE_{1}EE_{2}$$
$$\overline{>}\overline{>}^{1}b\overline{@}\overline{@}^{2}b$$
$$\overline{>}>\overline{@}@$$
$$>>@@$$
$$\phi >\phi 2\phi @\phi 1$$
$$2>c1@c$$
$$E_{2}E_{1}.$$
$$bb$$
Tuy nhiên, $id_{Eb1}$ và $id_{Eb2}$ là liên tục đều (uniformly continuous) các hàm tạo ra sau đây các biểu đồ giao hoán
$$EE_{1}EE_{2}$$
$$\overline{>}^{\phi1}\overline{>} b\overline{?}^{\phi2}\overline{?} b$$
$$\overline{>}>\overline{?}?$$
$$>>id??id$$
$$\phi >> bE1\phi ?? bE2$$
$$12$$
$$E_{1}E_{2},$$
$$bb$$
Do đó bởi tính duy nhất của các mở rộng ta phải có
$$\phi_{1}  \circ \phi_{2}  = id_{Eb1}and\phi_{2}  \circ \phi_{1}  = id_{Eb2}.$$
$$cccc$$
Điều này chứng tỏ rằng $\phi_{1}$ và $\phi_{2}$ là mutual các nghịch đảo. Bây giờ, vì $\phi_{2}  = \phi_{2}  \circ \phi_{1}$, ta có
$$c c c$$
$$\phi_{2} |\phi_{1} (E) = \phi_{2}  \circ \phi_{1}^{-1}  ,$$
$$c$$
Và vì $\phi_{1}^{-1}$ và $\phi_{2}$ là các phép đẳng cự, do đó là $\phi_{2} |\phi_{1} (E)$. Nhưng ta đã thấy trước đó rằng $\phi_{2}$ là
$$c c$$
Uniform liên tục mở rộng của $\phi_{2} |\phi_{1} (E)$ và $\phi_{1} (E)$ là trù mật trong $E_{1}$, do đó với mọi hai các phần tử
$$c b$$
$\alpha , \beta  \in E_{1}$, nếu $(a_{n})$ và $(b_{n})$ là các dãy trong $\phi_{1} (E)$ hội tụ đến $\alpha$ và $\beta$, ta có
$$b$$
$$d_{2}((\phi_{2} |\phi_{1} (E))(a_{n}), ((\phi_{2} |\phi_{1} (E))(b_{n})) =d_{1}(a_{n}, b_{n}),$$
$$bcc b$$
Và bởi chuyển đến giới hạn ta thu được
$$d_{2}(\phi_{2} (\alpha ),\phi_{2} (\beta )) =d_{1}(\alpha , \beta ),$$
$$bc c b$$
Mà chỉ ra rằng $\phi_{2}$ là phép đẳng cự (isometry) (tương tự, $\phi_{1}$ là phép đẳng cự (isometry)).
$$c c$$
Các nhận xét: $1$. Ngoại trừ cho Bước $8$ và Bước $9$, chứng minh của Định lý 37.53 là chứng minh cho trước trong Schwartz $[155]$ (Chương XI, Mục $4$, Định lý $1)$, và Kormogorov và Fomin $[108]$ (Chương $2$, Mục $7$, Định lý $4). 2$. cách xây dựng của $E$ relies trên tính đầy đủ của $\mathbb{R}$, và do đó nó không thể được sử dụng đến
$$b$$
$construct\mathbb{R} from\mathbb{Q}$. Tuy nhiên, cách xây dựng này có thể được được sửa đổi đến cho cách xây dựng của $\mathbb{R}$ từ $\mathbb{Q}$. Ta chỉ ra trong Mục 37.12 rằng Định lý 37.53 cho ta cách xây dựng của đầy đủ hóa của không gian vectơ định chuẩn (normed vector space).
