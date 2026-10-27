# Ngoài Tenxơ Các lũy thừa


<!-- PAGE 1231 -->
Chương $34$ Ngoài Tenxơ Các lũy thừa và Các đại số ngoài

## 34.1 Ngoài Tenxơ Các lũy thừa

Trong chương này ta xét thay phiên (cũng được gọi là phản đối xứng) đa tuyến tính các ánh xạ và
$$exterior tensor powers (also called alternating tensor powers), denoted \bigwedge  n(E). In many$$
Các đối với thay phiên đa tuyến tính các ánh xạ và ngoài tenxơ các lũy thừa có thể được treated nhiều like tenxơ đối xứng (symmetric tensor) các lũy thừa, ngoại trừ rằng $sgn(\sigma$) cần là inserted trong trước của các công thức hợp lệ cho đối xứng các lũy thừa. Xấp xỉ/đại khái speaking, ta là bây giờ trong world của các định thức thay vì trong world của permanents. Tuy nhiên, có cũng một số cơ bản differences, một của mà đang là rằng
$$the exterior tensor power \bigwedge  n(E) is the trivial vector space (0) when E is finite-dimensional$$
Và khi $n >$ dim(E). Điều này chương cung cấp firm foundations cho understanding vi phân các dạng. Như trong trường hợp của tenxơ đối xứng (symmetric tensor) các lũy thừa, vì ta đã có đại số tenxơ (tensor algebra) T(V), ta có thể tiến hành khá quickly. Nhưng thứ nhất cho chúng ta ôn tập/tổng quan một số cơ bản các định nghĩa và các sự kiện.

> **Định nghĩa 34.1.** Cho $f$: $E^{n} \to F$ là ánh xạ đa tuyến tính (multilinear map). Ta nói rằng $f$ thay phiên khi và chỉ khi với mọi $u_{i} \in E, f(u_{1}, \dots  , u_{n}) = 0$ bất cứ khi nào $u_{i} = u_{i+1}$, với một số $i$ với $1 \le i \le n$ - $1$; nghĩa là, $f(u_{1}, \dots  , u_{n}) = 0$ bất cứ khi nào hai kề nhau các đối số/lập luận là đồng nhất. Ta nói rằng $f$ là phản đối xứng (hoặc anti-symmetric) khi và chỉ khi
$$f(u_{\sigma(1)}, \dots  , u_{\sigma(n)}) = sgn(\sigma )f(u_{1}, \dots  , u_{n}),$$
Với mọi hoán vị $\sigma  \in \mathfrak{S}_{n}$, và tất cả $u_{i} \in E$. Cho $n = 1$, ta agree rằng mọi ánh xạ tuyến tính (linear map) $f$: $E \to F$ là thay phiên. không gian vectơ (vector space) của tất cả đa tuyến tính thay phiên các ánh xạ $f$: $E^{n} \to F$ được ký hiệu là $Alt^{n}(E; F)$. Lưu ý rằng $Alt^{1}(E; F) =$ Hom(E, $F)$. sau đây cơ bản mệnh đề chỉ ra relationship giữa alternation và skew-symmetry.
$$1231$$

<!-- PAGE 1232 -->

> **Mệnh đề 34.1.** Cho $f$: $E^{n} \to F$ là ánh xạ đa tuyến tính (multilinear map). Nếu $f$ là thay phiên, thì các tính chất sau đây đúng:
$(1)$ Với mọi $i$, với $1 \le i \le n$ - $1$,
$$f(\dots  , u_{i}, u_{i+1}, \dots ) = -f(\dots  , u_{i+1}, u_{i}, \dots ).$$
$(2)$ Với mọi hoán vị $\sigma  \in \mathfrak{S}_{n}$,
$$f(u_{\sigma(1)}, \dots  , u_{\sigma(n)}) = sgn(\sigma )f(u_{1}, \dots  , u_{n}).$$
$(3)$ Với mọi $i, j$, với $1 \le i < j \le n$,
$$f(\dots  , u_{i}, \dots  u_{j}, \dots ) = 0whenever u_{i} = u_{j}.$$
Hơn thế nữa, nếu của ta trường $K$ có characteristic khác nhau từ $2$, thì mọi phản đối xứng ánh xạ đa tuyến tính (multilinear map) là thay phiên.

*Chứng minh.* $(1)$ Bởi tính đa tuyến tính ứng dụng hai lần, ta có $f(\dots  , u_{i} + u_{i+1}, u_{i} + u_{i+1}, \dots$) $= f(\dots  , u_{i}, u_{i}, \dots$) $+ f(\dots  , u_{i}, u_{i+1}, \dots$)
$$+ f(\dots  , u_{i+1}, u_{i}, \dots ) + f(\dots  , u_{i+1}, u_{i+1}, \dots ).$$
Vì $f$ là thay phiên, ta thu được
$$0 = f(\dots  , u_{i}, u_{i+1}, \dots ) + f(\dots  , u_{i+1}, u_{i}, \dots );$$
Rằng là, $f(\dots  , u_{i}, u_{i+1}, \dots$) $= -f(\dots  , u_{i+1}, u_{i}, \dots$).
$(2)$ Rõ ràng, đối xứng nhóm, $\mathfrak{S}_{n}$, acts trên $Alt^{n}(E; F)$ trên trái, thông qua
$$\sigma  \cdot  f(u_{1}, \dots  , u_{n}) = f(u_{\sigma(1)}, \dots  , u_{\sigma(n)}).$$
Hệ quả là, $as\mathfrak{S}_{n}$ được sinh bởi các phép chuyển vị (các hoán vị rằng swap chính xác hai các phần tử), vì cho phép chuyển vị, $(2)$ là đơn giản $(1)$, ta suy ra $(2)$ bằng quy nạp theo số của các phép chuyển vị trong $\sigma$.
$(3)$ Có một hoán vị $\sigma$ rằng sends $u_{i}$ và $u_{j}$ respectively đến $u_{1}$ và $u_{2}$. Bởi giả thiết $u_{i} = u_{j}$, do đó ta có $u_{\sigma(1)} = u_{\sigma(2)}$, và như $f$ là thay phiên ta có
$$f(u_{\sigma(1)}, \dots  , u_{\sigma(n)}) = 0.$$
Tuy nhiên, bởi $(2)$,
$$f(u_{1}, \dots  , u_{n}) = sgn(\sigma )f(u_{\sigma(1)}, \dots  , u_{\sigma(n)}) = 0.$$
Bây giờ khi $f$ là phản đối xứng, nếu $\sigma$ là phép chuyển vị swapping $u_{i}$ và $u_{i+1} = u_{i}$, như $sgn(\sigma$) $= -1$, ta thu được
$$f(\dots  , u_{i}, u_{i}, \dots ) = -f(\dots  , u_{i}, u_{i}, \dots ),$$

<!-- PAGE 1233 -->
Sao cho
$$2f(\dots  , u_{i}, u_{i}, \dots ) = 0,$$
Và trong mọi characteristic ngoại trừ $2$, ta kết luận rằng $f(\dots  , u_{i}, u_{i}, \dots$) $= 0$, cụ thể là $f$ là thay phiên. Mệnh đề 34.1 chỉ ra rằng trong mọi characteristic ngoại trừ $2$, thay phiên và skewsymmetric đa tuyến tính các ánh xạ là đồng nhất. Bằng cách sử dụng Mệnh đề 34.1 ta dễ dàng suy ra sau đây then chốt sự kiện.

> **Mệnh đề 34.2.** Cho $f$: $E^{n} \to F$ là ánh xạ đa tuyến tính thay phiên. Với mọi các họ của các vectơ, $(u_{1}, \dots  , u_{n})$ và $(v_{1}, \dots  , v_{n})$, với $u_{i}, v_{i} \in E$, nếu
$$v_{j} = \sum_{i=1}^{n}  a_{ij}u_{i},1 \le j \le n,$$
Thì
$$f(v_{1}, \dots  , v_{n}) = \sum_{\sigma\in Sn}  sgn(\sigma ) a_{\sigma(1),1} \cdots  a_{\sigma(n),n}!f(u_{1}, \dots  , u_{n}) = \det(A)f(u_{1}, \dots  , u_{n}),$$
Ở đâu $A$ là ma trận cỡ $n \times  n$, $A = (a_{ij})$.

*Chứng minh.* Sử dụng Tính chất (ii) của Mệnh đề 34.1. Ta là bây giờ ready để định nghĩa và xây dựng ngoài tenxơ các lũy thừa.

> **Định nghĩa 34.2.** thứ $n$ lũy thừa tenxơ ngoài của không gian vectơ (vector space) $E$, ở đâu $n \ge 1$, là không gian vectơ (vector space) $A$ cùng với ánh xạ đa tuyến tính thay phiên $\phi$: $E^{n} \to A$, sao cho với mọi không gian vectơ (vector space) $F$ và với mọi ánh xạ đa tuyến tính thay phiên $f$: $E^{n} \to F$, tồn tại duy nhất một ánh xạ tuyến tính (linear map) $f_{\wedge}: A \to F$ với
$$f(u_{1}, \dots  , u_{n}) = f_{\wedge}(\phi (u_{1}, \dots  , u_{n})),$$
Với mọi $u_{1}, \dots  , u_{n} \in E$, hoặc cho ngắn
$$f = f_{\wedge}\circ \phi .$$
Tương đương, tồn tại duy nhất một ánh xạ tuyến tính (linear map) $f_{\wedge}$ sao cho sau đây biểu đồ giao hoán:
$$E^{n} /A$$
$$\overline{D}^{\phi}\overline{D}$$
$$\overline{D} D$$
$$DD$$
$$DD^{f\wedge}$$
$$f!$$
$$F.$$
Ở trên tính chất được gọi là phổ dụng ánh xạ tính chất của lũy thừa tenxơ ngoài $(A, \phi$).

<!-- PAGE 1234 -->
Ta bây giờ chỉ ra rằng bất kỳ hai thứ $n$ ngoài tenxơ các lũy thừa $(A_{1}, \phi_{1}$) và $(A_{2}, \phi_{2}$) cho $E$ là đẳng cấu.

> **Mệnh đề 34.3.** Cho trước bất kỳ hai thứ $n$ ngoài tenxơ các lũy thừa $(A_{1}, \phi_{1}$) và $(A_{2}, \phi_{2}$) cho $E$, có một đẳng cấu $h: A_{1} \to A_{2}$ sao cho
$$\phi_{2}  = h \circ \phi_{1} .$$

*Chứng minh.* Thay thế tích tenxơ (tensor product) bởi thứ $n$ lũy thừa tenxơ ngoài trong chứng minh của Mệnh đề 33.5. Ta tiếp theo cho cách xây dựng rằng produces thứ $n$ lũy thừa tenxơ ngoài của không gian vectơ (vector space) $E$.
$$Theorem 34.4. Given a vector space E, an n-th exterior tensor power (^{n} \bigwedge  (E), \phi ) for E$$
Có thể được được xây dựng $(n \ge 1)$. Hơn nữa, ký hiệu $\phi (u_{1}, \dots  , u_{n})$ như $u_{1}\wedge \cdots \wedge u_{n}$, ngoài
$$tensor power \bigwedge  n(E) is generated by the  vectors u_{1} \wedge \cdots  \wedge u_{n}, where u_{1}, \dots  , u_{n} \in E, and for$$
$$every alternating multilinear map f : E^{n}\to F, the unique linear map f_{\wedge}: \bigwedge  n(E) \to F such$$
Rằng $f = f_{\wedge} \circ \phi$ được định nghĩa bởi
$$f_{\wedge}(u_{1} \wedge \cdots  \wedge u_{n}) = f(u_{1}, \dots  , u_{n})$$
Trên các phần tử sinh $u_{1} \wedge \cdots  \wedge u_{n}$ của n(E).
$$\bigwedge$$
Chứng minh phác thảo. Ta có thể cho quick chứng minh bằng cách sử dụng đại số tenxơ (tensor algebra) T(E). Cho $\mathfrak{I}_{a}$ là hai phía lý tưởng (ideal) của T(E) được sinh bởi tất cả các tenxơ của tạo thành $u \otimes u \in E^{\otimes2}$. Thì cho
$$n$$
$$^(E) = E^{\otimes n}/(\mathfrak{I}_{a} \cap E^{\otimes n})$$
$$n$$
$$and let \pi  be the projection \pi : E^{\otimes n}\to \bigwedge  (E). If we let u_{1} \wedge \cdots  \wedge u_{n} = \pi (u_{1} \otimes \cdots  \otimes u_{n}), it$$
$$is easy to check that (^{n} \bigwedge  (E), \wedge ) satisfies the conditions of Theorem 34.4.$$
Nhận xét: Ta có thể cũng định nghĩa
$$n$$
$$^(E) = T(E)/\mathfrak{I}_{a} =M^(E),$$
$$n\ge 0$$
Đại số ngoài (exterior algebra) của $E$. Điều này là phản đối xứng counterpart của S(E), và ta sẽ study nó little sau này.
$$n n$$
$$For simplicity of notation, we may write \bigwedge_{1}  E  \sim for \bigwedge  (E). We also abbreviate “exterior0$$
$$tensor power” as “exterior power.” Clearly, \bigwedge  (E)= E, and it is convenient to set \bigwedge  (E) =$$
$K$.

<!-- PAGE 1235 -->
$$n$$
$$The fact that the map \phi : E^{n}\to \bigwedge  (E) is alternating and multilinear can also be ex-$$
Pressed như sau:
$$u_{1} \wedge \cdots  \wedge (u_{i} + v_{i}) \wedge \cdots  \wedge u_{n}=(u_{1} \wedge \cdots  \wedge u_{i} \wedge \cdots  \wedge u_{n})$$
$$+ (u_{1} \wedge \cdots  \wedge v_{i} \wedge \cdots  \wedge u_{n}),$$
$$u_{1} \wedge \cdots  \wedge (\lambda u_{i}) \wedge \cdots  \wedge u_{n}=\lambda (u_{1} \wedge \cdots  \wedge u_{i} \wedge \cdots  \wedge u_{n}),$$
$$u_{\sigma(1)} \wedge \cdots  \wedge u_{\sigma(n)}=sgn(\sigma ) u_{1} \wedge \cdots  \wedge u_{n},$$
Với mọi $\sigma  \in \mathfrak{S}_{n}$.
$$n$$
$$The map \phi  from E^{n}to \bigwedge  (E) is often denoted \iota_{\wedge} , so that$$
$$\iota_{\wedge} (u_{1}, \dots  , u_{n}) = u_{1} \wedge \cdots  \wedge u_{n}.$$
Định lý 34.4 suy ra kết quả sau đây.

> **Mệnh đề 34.5.** Có một chính tắc đẳng cấu
$$n$$
$$^ \sim$$
$$Hom((E), F)= Alt^{n}(E; F)$$
$$between the vector space of linear maps Hom(^{n} \bigwedge  (E), F) and the vector space of alternating$$
Đa tuyến tính các ánh xạ $Alt^{n}(E; F)$, cho trước bởi ánh xạ tuyến tính (linear map) $-\circ \phi$ được định nghĩa bởi $\mapsto h \circ \phi$, với $h \in$
$$Hom(^{n} \bigwedge  (E), F). In particular, when F = K, we get a canonical isomorphism$$
$$n!*$$
$$^\sim$$
$$(E)= Alt^{n}(E; K).$$
$$Definition 34.3. Tensors \alpha  \in \bigwedge  n(E) are called alternating n-tensors or alternating tensors$$
Của bậc $n$ và ta viết $deg(\alpha$) $= n$. Các tenxơ của tạo thành $u_{1}\wedge \cdots \wedge u_{n}$, ở đâu $u_{i} \in E$, được gọi là đơn giản (hoặc phân rã được) thay phiên n-tensors. Những phần tử đó thay phiên n-tensors rằng là không
$$simple are often called compound alternating n-tensors. Simple tensors u_{1}\wedge \cdots \wedge u_{n} \in \bigwedge  n(E)$$
$$are also called n-vectors and tensors in \bigwedge  n(E^{*}) are often called (alternating) n-forms.$$
Cho trước ánh xạ tuyến tính (linear map) $f$: $E \to$ E', vì ánh xạ $\iota_{\wedge}' \circ (f \times f)$ là song tuyến tính và thay phiên, ở đó
$$is a unique linear map f \wedge f : \bigwedge  2(E) \to \bigwedge_{2}  2(E') making the following diagram commute:$$
$$\iota \wedge /2$$
$$E \bigwedge  (E)$$
$$f\times ff\wedge f$$
$$(E')^{2}\overline{\iota}\overline{'}/ \bigwedge  2(E').$$
$$\wedge$$
$$The map f \wedge f : \bigwedge  2(E) \to \bigwedge  2(E') is determined by$$
$$(f \wedge f)(u \wedge v) = f(u) \wedge f(v).$$
