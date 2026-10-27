# Tenxơ đối xứng (symmetric tensor) Các lũy thừa


<!-- PAGE 1214 -->

## 33.10 Tenxơ đối xứng (symmetric tensor) Các lũy thừa

Của ta mục tiêu là đến đến lên với khái niệm của tích tenxơ (tensor product) rằng sẽ cho phép chúng ta đến treat đối xứng đa tuyến tính các ánh xạ như các ánh xạ tuyến tính (linear maps). Lưu ý rằng ta có đến thu hẹp chính chúng ta đến đơn lẻ không gian vectơ (vector space) $E$, khá thì $n$ các không gian vectơ $E_{1}, \dots  , E_{n}$, sao cho tính đối xứng làm cho nghĩa.

> **Định nghĩa 33.20.** ánh xạ đa tuyến tính (multilinear map) $f$: $E^{n} \to F$ là đối xứng khi và chỉ khi
$$f(u_{\sigma(1)}, \dots  , u_{\sigma(n)}) = f(u_{1}, \dots  , u_{n}),$$
Với mọi $u_{i} \in E$ và tất cả các hoán vị, $\sigma$: ${1, \dots  , n} \to {1, \dots  , n}$. nhóm của các hoán vị trên ${1, \dots  , n}$ (đối xứng nhóm) được ký hiệu là $\mathfrak{S}_{n}$. không gian vectơ (vector space) của tất cả đối xứng đa tuyến tính các ánh xạ $f$: $E^{n} \to F$ được ký hiệu bởi $Sym^{n}(E; F)$ hoặc $Hom_{symlin}(E^{n}, F)$. Lưu ý rằng $Sym^{1}(E; F) =$ Hom(E, $F)$. Ta có thể tiến hành một cách trực tiếp như trong Định lý 33.6 và xây dựng tenxơ đối xứng (symmetric tensor) các tích từ scratch. Tuy nhiên, vì ta đã có khái niệm của tích tenxơ (tensor product), có một nhiều hơn/thêm economical phương pháp. Thứ nhất ta định nghĩa tenxơ đối xứng (symmetric tensor) các lũy thừa.

> **Định nghĩa 33.21.** thứ $n$ tenxơ đối xứng (symmetric tensor) lũy thừa của không gian vectơ (vector space) $E$, ở đâu $n \ge 1$, là không gian vectơ (vector space) $S$ cùng với đối xứng ánh xạ đa tuyến tính (multilinear map) $\phi$: $E^{n} \to S$ sao cho, với mọi không gian vectơ (vector space) $F$ và với mọi đối xứng ánh xạ đa tuyến tính (multilinear map) $f$: $E^{n} \to F$, tồn tại duy nhất một ánh xạ tuyến tính (linear map) $f_{\odot}: S \to F$, với
$$f(u_{1}, \dots  , u_{n}) = f_{\odot}(\phi (u_{1}, \dots  , u_{n})),$$
Với mọi $u_{1}, \dots  , u_{n} \in E$, hoặc cho ngắn
$$f = f_{\odot}\circ \phi .$$
Tương đương, tồn tại duy nhất một ánh xạ tuyến tính (linear map) $f_{\odot}$ sao cho sau đây biểu đồ giao hoán.
$$E^{n} /S$$
$$\overline{C}^{\phi}\overline{C}$$
$$\overline{C} C$$
$$CC$$
$$CC^{f\odot}$$
$$f!$$
$$F$$
Ở trên tính chất được gọi là phổ dụng ánh xạ tính chất của tenxơ đối xứng (symmetric tensor) lũy thừa $(S, \phi$). Ta tiếp theo chỉ ra rằng bất kỳ hai đối xứng thứ $n$ tenxơ các lũy thừa $(S_{1}, \phi_{1}$) và $(S_{2}, \phi_{2}$) cho $E$ là đẳng cấu.

> **Mệnh đề 33.32.** Cho trước bất kỳ hai đối xứng thứ $n$ tenxơ các lũy thừa $(S_{1}, \phi_{1}$) và $(S_{2}, \phi_{2}$) cho $E$, có một đẳng cấu $h: S_{1} \to S_{2}$ sao cho
$$\phi_{2}  = h \circ \phi_{1} .$$

<!-- PAGE 1215 -->

*Chứng minh.* Thay thế tích tenxơ (tensor product) bởi thứ $n$ tenxơ đối xứng (symmetric tensor) lũy thừa trong chứng minh của Mệnh đề 33.5. Ta bây giờ cho cách xây dựng rằng produces đối xứng thứ $n$ tenxơ lũy thừa của không gian vectơ (vector space) $E$.

> **Định lý 33.33.** Cho trước không gian vectơ (vector space) $E$, đối xứng thứ $n$ tenxơ lũy thừa $(S^{n}(E), \phi$) cho $E$ có thể được được xây dựng $(n \ge 1)$. Hơn nữa, ký hiệu $\phi (u_{1}, \dots  , u_{n})$ như $u_{1} \odot \cdots  \odot u_{n}$, tenxơ đối xứng (symmetric tensor) lũy thừa $S^{n}(E)$ được sinh bởi các vectơ $u_{1}\odot \cdots \odot u_{n}$, ở đâu $u_{1}, \dots  , u_{n} \in E$, và với mọi đối xứng ánh xạ đa tuyến tính (multilinear map) $f$: $E^{n} \to F$, duy nhất ánh xạ tuyến tính (linear map) $f_{\odot}: S^{n}(E) \to F$ sao cho $f = f_{\odot} \circ \phi$ được định nghĩa bởi
$$f_{\odot}(u_{1} \odot \cdots  \odot u_{n}) = f(u_{1}, \dots  , u_{n})$$
Trên các phần tử sinh $u_{1} \odot \cdots  \odot u_{n}$ của $S^{n}(E)$.

*Chứng minh.* tenxơ lũy thừa $E^{\otimes n}$ là cũng big, và do đó ta định nghĩa thích hợp thương. Cho $C$ là không gian con của $E^{\otimes n}$ được sinh bởi các vectơ của tạo thành
$$u_{1} \otimes \cdots  \otimes u_{n} -u_{\sigma(1)} \otimes \cdots  \otimes u_{\sigma(n)},$$
Với mọi $u_{i} \in E$, và tất cả các hoán vị $\sigma$: ${1, \dots  , n} \to {1, \dots  , n}$. Ta khẳng định rằng không gian thương (quotient space) $(E^{\otimes n})/C$ thực hiện job. Cho $p: E^{\otimes n} \to (E^{\otimes n})/C$ là thương ánh xạ, và cho $\phi$: $E^{n} \to (E^{\otimes n})/C$ là ánh xạ cho trước bởi
$$\phi  = p \circ \phi_{0} ,$$
Ở đâu $\phi_{0}$: $E^{n} \to E^{\otimes n}$ là đơn ánh cho trước bởi $\phi_{0} (u_{1}, \dots  , u_{n}) = u_{1} \otimes \cdots  \otimes u_{n}$. Cho chúng ta ký hiệu $\phi (u_{1}, \dots  , u_{n})$ như $u_{1} \odot \cdots  \odot u_{n}$. Rõ ràng là $\phi$ là đối xứng. Vì các vectơ $u_{1} \otimes \cdots  \otimes u_{n}$ sinh $E^{\otimes n}$, và $p$ là toàn ánh (surjective), các vectơ $u_{1} \odot \cdots  \odot u_{n}$ sinh $(E^{\otimes n})/C$. Nó vẫn còn để chỉ ra rằng $((E^{\otimes n})/C, \phi$) thỏa mãn phổ dụng ánh xạ tính chất. Đến điều này kết thúc/cuối ta bắt đầu bởi chứng minh rằng có một ánh xạ $h$ sao cho $f = h \circ \phi$. Cho trước bất kỳ đối xứng ánh xạ đa tuyến tính (multilinear map) $f$: $E^{n} \to F$, theo Định lý 33.6 có một ánh xạ tuyến tính (linear map) $f_{\otimes}: E^{\otimes n} \to F$ sao cho $f = f_{\otimes} \circ \phi_{0}$, như trong biểu đồ ở dưới.
$$/$$
$$E^{n}E^{\otimes n}$$
$$\overline{F}^{\phi0}\overline{F}$$
$$\overline{F} F$$
$$FF$$
$$FF$$
$$fF^{f\otimes}#$$
$$F$$

<!-- PAGE 1216 -->
Tuy nhiên, vì $f$ là đối xứng, ta có $f_{\otimes}(z) = 0$ với mọi $z \in C$. Do đó, ta thu được được cảm sinh ánh xạ tuyến tính (linear map) $h: (E^{\otimes n})/C \to F$ tạo ra sau đây biểu đồ giao hoán.
$$E^{\otimes n}$$
$$y<KK$$
$$yKK$$
$$\phi yyK^{p}$$
$$yKK$$
$$y^{0}yKK$$
$$yK%$$
$$y$$
$$E^{n}f\otimes (E^{\otimes n})/C$$
$$EE$$
$$EErrrrrrrrr$$
$$EE$$
$$EE$$
$$fE"h$$
$$ry$$
$$F$$
Nếu ta định nghĩa h([z]) $= f_{\otimes}(z)$ với mọi $z \in E^{\otimes n}$, ở đâu $[z]$ là lớp tương đương (equivalence class) trong $(E^{\otimes n})/C$ của $z \in E^{\otimes n}$, ở trên biểu đồ chỉ ra rằng $f = h \circ p \circ \phi_{0}  = h \circ \phi$. Ta bây giờ chứng minh tính duy nhất của $h$. Với mọi ánh xạ tuyến tính (linear map) $f_{\odot}: (E^{\otimes n})/C \to F$ sao cho $f = f_{\odot} \circ \phi$, vì $\phi (u_{1}, \dots  , u_{n}) = u_{1} \odot \cdots  \odot u_{n}$ và các vectơ $u_{1} \odot \cdots  \odot u_{n}$ sinh $(E^{\otimes n})/C$, ánh xạ $f_{\odot}$ là một cách duy nhất được định nghĩa bởi
$$f_{\odot}(u_{1} \odot \cdots  \odot u_{n}) = f(u_{1}, \dots  , u_{n}).$$
Vì $f = h \circ \phi$, ánh xạ $h$ là duy nhất, và ta cho $f_{\odot} = h$. Do đó, $S^{n}(E) = (E^{\otimes n})/C$ và $\phi$ constitute đối xứng thứ $n$ tenxơ lũy thừa của $E$. ánh xạ $\phi$ từ $E^{n}$ đến $S^{n}(E)$ là thường được ký hiệu $\iota_{\odot}$, sao cho
$$\iota_{\odot} (u_{1}, \dots  , u_{n}) = u_{1} \odot \cdots  \odot u_{n}.$$
Một lần nữa, actual cách xây dựng là không quan trọng. Những gì là quan trọng là rằng đối xứng lũy thừa thứ $n$ có phổ dụng ánh xạ tính chất đối với đối xứng đa tuyến tính các ánh xạ.
Nhận xét: ký hiệu $\odot$ cho giao hoán phép nhân của tenxơ đối xứng (symmetric tensor) các lũy thừa là không tiêu chuẩn. Một cái khác ký hiệu một cách chung/phổ biến được sử dụng là $\cdot$. Ta thường abbreviate “tenxơ đối xứng (symmetric tensor) lũy thừa” như “đối xứng lũy thừa.” đối xứng lũy thừa $S^{n}(E)$ cũng được ký hiệu $Sym^{n}E$ nhưng ta ưu tiên để sử dụng ký hiệu Sym đến ký hiệu các không gian của đối xứng đa tuyến tính các ánh xạ. Đến
$$n  \sim$$
$$be consistent with the use of \odot , we could have used the notation \bigodot  E. Clearly, S^{1}(E)= E$$
Và nó là thuận tiện đến tập hợp $S^{0}(E) = K$. sự kiện rằng ánh xạ $\phi$: $E^{n} \to S^{n}(E)$ là đối xứng và đa tuyến tính có thể cũng được biểu diễn như sau: $u_{1} \odot \cdots  \odot (v_{i} + w_{i}) \odot \cdots  \odot u_{n} = (u_{1} \odot \cdots  \odot v_{i} \odot \cdots  \odot u_{n}) + (u_{1} \odot \cdots  \odot w_{i} \odot \cdots  \odot u_{n}), u_{1} \odot \cdots  \odot (\lambda u_{i}) \odot \cdots  \odot u_{n} = \lambda (u_{1} \odot \cdots  \odot u_{i} \odot \cdots  \odot u_{n})$,
$$u_{\sigma(1)} \odot \cdots  \odot u_{\sigma(n)} = u_{1} \odot \cdots  \odot u_{n},$$
Với mọi các hoán vị $\sigma  \in \mathfrak{S}_{n}$. cuối cùng đồng nhất thức chỉ ra rằng “phép toán” $\odot$ là giao hoán. Điều này cho phép chúng ta đến quan điểm tenxơ đối xứng (symmetric tensor) $u_{1} \odot \cdots  \odot u_{n}$ như object được gọi là đa tập hợp (multiset).

<!-- PAGE 1217 -->
Cho trước tập hợp $A$, đa tập hợp (multiset) với các phần tử từ $A$ là tổng quát hóa của khái niệm của tập hợp rằng cho phép bội instances của các phần tử từ $A$ đến xảy ra. Ví dụ, nếu $A = {a, b, c, d}$, sau đây là các đa tập hợp:
$$M_{1} = {a, a, b}, M_{2} = {a, a, b, b, c}, M_{3} = {a, a, b, b, c, d, d, d}.$$
Ở đây là một cái khác cách để biểu diễn các đa tập hợp như các bảng chỉ ra các bội của các phần tử trong đa tập hợp (multiset):
$$M_{1} = \begin{pmatrix} a & b & c & d \\ 2 & 1 & 0 & 0 \end{pmatrix} ,M_{2} = \begin{pmatrix} a & b & c & d \\ 2 & 2 & 1 & 0 \end{pmatrix} ,M_{3} = \begin{pmatrix} a & b & c & d \\ 2 & 2 & 1 & 3 \end{pmatrix} .$$
Ở trên là chỉ các đồ thị của các hàm từ tập hợp $A = {a, b, c, d}$ đến $\mathbb{N}$. Điều này suggests sau đây định nghĩa.

> **Định nghĩa 33.22.** hữu hạn đa tập hợp (multiset) $M$ trên tập hợp $A$ là hàm $M$: $A \to \mathbb{N}$ sao cho M() $\neq  0$ cho một cách hữu hạn nhiều $a \in A$. bội (multiplicity) của phần tử $a \in A$ trong $M$ là M(). Tập hợp tất cả các đa tập hợp trên $A$ được ký hiệu bởi $\mathbb{N}^{(A)}$, và ta cho dom(M) $= {a \in A$ | M() $\neq  0}$, mà là hữu hạn tập hợp. tập hợp dom(M) là tập hợp của các phần tử trong $A$ rằng thực sự xảy ra trong
$$M. For any multiset M \in \mathbb{N}^{(A)}, note that \sum_{a}  \in A M(a) makes sense, since \sum_{a}  \in A M(a) =$$
$$\sum_{a}  \in dom( M(a), and dom(M) is finite; this sum is the total number of elements in the$$
$$multiset^{A)} A and is called the size of M. Let |M| = \sum_{a}  \in A M(a).$$
Đi quay lại đến của ta đối xứng các tenxơ, ta có thể quan điểm các tenxơ của tạo thành $u_{1} \odot \cdots  \odot u_{n}$ như các đa tập hợp của kích thước $n$ trên tập hợp $E$. Định lý 33.33 suy ra sau đây mệnh đề.

> **Mệnh đề 33.34.** Có một chính tắc đẳng cấu
$$\sim$$
$$Hom(S^{n}(E), F)= Sym^{n}(E; F),$$
Giữa không gian vectơ (vector space) của các ánh xạ tuyến tính (linear maps) $Hom(S^{n}(E), F)$ và không gian vectơ (vector space) của đối xứng đa tuyến tính các ánh xạ $Sym^{n}(E; F)$ cho trước bởi ánh xạ tuyến tính (linear map) $-\circ \phi$ được định nghĩa bởi $h \mapsto h \circ \phi$, với $h \in Hom(S^{n}(E), F)$.

*Chứng minh.* ánh xạ $h \circ \phi$ là rõ ràng đối xứng đa tuyến tính. Theo Định lý 33.33, với mọi đối xứng ánh xạ đa tuyến tính (multilinear map) $f \in Sym^{n}(E; F)$ tồn tại duy nhất một ánh xạ tuyến tính (linear map) $f_{\odot} \in Hom(S^{n}(E), F)$ sao cho $f = f_{\odot} \circ \phi$, do đó ánh xạ $-\circ \phi$ là song ánh (bijective). nghịch đảo của nó là ánh xạ $f \mapsto f_{\odot}$. Đặc biệt, khi $F = K$, ta thu được sau đây quan trọng sự kiện.

> **Mệnh đề 33.35.** Có một chính tắc đẳng cấu
$$\sim$$
$$(S^{n}(E))^{*}= Sym^{n}(E; K).$$
