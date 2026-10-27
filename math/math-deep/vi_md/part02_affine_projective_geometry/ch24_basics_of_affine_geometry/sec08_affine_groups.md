# Afin Các nhóm


<!-- PAGE 841 -->
Nó là dễ để kiểm tra rằng điểm $a = (6, -3)$ là cố định bởi $f$, mà có nghĩa là f() $= a$, do đó bởi translating tọa độ hệ quy chiếu (frame) đến gốc, ánh xạ afin (affine map) behaves like ánh xạ tuyến tính (linear map). Nếu $f$: $E \to$ E' là song ánh (bijective) ánh xạ afin (affine map), cho trước bất kỳ ba thẳng hàng các điểm, $b, c$ trong $E$, với $a \neq  b$, ở đâu, nói, $c = (1$ - $\lambda )a + \lambda b$, vì $f$ bảo toàn các tâm tỉ cự, ta có f(c) $= (1-\lambda )f(a)+\lambda$ f(b), mà chỉ ra rằng f(), f(b), f(c) là thẳng hàng trong E'. Có một điều ngược lại đến tính chất này, mà là đơn giản hơn đến phát biểu khi ground trường là $K = \mathbb{R}$. điều ngược lại phát biểu rằng cho trước bất kỳ song ánh (bijective) hàm $f$: $E \to$ E' giữa hai thực các không gian afin của cùng số chiều $n \ge 2$, nếu $f$ các ánh xạ bất kỳ ba thẳng hàng các điểm đến thẳng hàng các điểm, thì $f$ là afin. chứng minh là khá dài (xem Berger $[11]$ hoặc Samuel $[148])$. Cho trước ba thẳng hàng các điểm, $b, c$, ở đâu ̸ $= c$, ta có $b = (1$ - $\beta )a + \beta c$ với một số duy nhất $\beta$, và ta định nghĩa tỉ số của dãy, $b, c$, như
$$ratio(a, b, c) = \frac{\beta}{(1 -\beta )} = \frac{\longrightarrow ab}{bc} \longrightarrow ,$$
Miễn là/được cung cấp rằng $\beta  \neq  1$, i.e., $b \neq  c$. Khi $b = c$, ta agree rằng tỉ số(, $b, c) = \infty$. Ta warn của ta độc giả rằng khác các tác giả định nghĩa tỉ số của, $b, c$ như -tỉ số(, $b, c) =_{-\to bc}^{-\to ba}$. Vì các ánh xạ afin bảo toàn các tâm tỉ cự, rõ ràng là các ánh xạ afin bảo toàn tỉ số của ba các điểm.

## 24.8 Afin Các nhóm

Ta bây giờ lấy quick nhìn tại song ánh (bijective) các ánh xạ afin. Cho trước không gian afin (affine space) $E$, tập hợp của afin các song ánh $f$: $E \to E$ là rõ ràng nhóm, được gọi là afin nhóm của $E$, và được ký hiệu bởi
$$\longrightarrow$$
GA(E). Nhắc lại rằng nhóm của song ánh (bijective) các ánh xạ tuyến tính (linear maps) của không gian vectơ (vector space) $E$ được ký hiệu bởi $\longrightarrow \longrightarrow \longrightarrow$ GL(E). Thì, ánh xạ $f \mapsto f$ định nghĩa đồng cấu nhóm (group homomorphism) $L$: GA(E) $\to$ GL(E). hạt nhân (kernel) của ánh xạ này là tập hợp của các phép tịnh tiến trên $E$. tập con của tất cả các ánh xạ tuyến tính (linear maps) của tạo thành $\lambda  id_{E}\longrightarrow$, ở đâu $\lambda  \in \mathbb{R} -{0}$, là nhóm con của $\longrightarrow$ GL(E), và được ký hiệu là $by\mathbb{R}^{*}id_{E}\longrightarrow$ (ở đâu $\lambda  id_{E}\longrightarrow  (u) = \lambda u, and\mathbb{R}^{*} =\mathbb{R}-{0})$. nhóm con DIL(E) $= L^{-1}(\mathbb{R}^{*}id_{E}\longrightarrow$) của GA(E) là một cách cụ thể thú vị. Hóa ra là nó là rời nhau hợp của các phép tịnh tiến và của các phép vị tự của tỉ số $\lambda$ ̸ $= 1$. các phần tử của DIL(E) được gọi là afin các phép vị tự. Cho trước bất kỳ điểm $a \in E$, và bất kỳ vô hướng (scalar) $\lambda  \in \mathbb{R}$, phép vị tự (dilatation) hoặc trung tâm phép vị tự (dilatation) (hoặc homothety) của tâm và tỉ số $\lambda$ là ánh xạ $H_{a,\lambda}$ được định nghĩa sao cho
$$\longrightarrow$$
$$H_{a,\lambda}(x) = a + \lambda ax,$$
Với mọi $x \in E$.
Nhận xét: thuật ngữ thực hiện không dường như là một cách phổ dụng agreed upon. các số hạng afin phép vị tự (dilatation) và trung tâm phép vị tự (dilatation) được sử dụng bởi Pedoe $[141]$. Snapper và Troyer sử dụng số hạng

<!-- PAGE 842 -->
Dilation cho afin phép vị tự (dilatation) và magnification cho trung tâm phép vị tự (dilatation) $[168]$. Samuel sử dụng homothety cho trung tâm phép vị tự (dilatation), trực tiếp phép tịnh tiến của French “homoth´etie” $[148]$. Vì dilation là shorter hơn phép vị tự (dilatation) và somewhat dễ hơn đến pronounce, perhaps ta nên sử dụng rằng! Nhận thấy rằng $H_{a,\lambda}(a) = a$, và khi $\lambda  \neq  0$ và $x \neq$, $H_{a,\lambda}(x)$ là trên đường thẳng được định nghĩa bởi
$$\longrightarrow$$
Và $x$, và là thu được bởi “scaling” ax bởi $\lambda$. Hình 24.21 chỉ ra effect của trung tâm phép vị tự (dilatation) của tâm $d$. tam giác (, $b, c)$ là magnified đến tam giác (', b', c'). Lưu ý cách mà mọi đường thẳng là mapped đến song song đường thẳng.
$$a$$
$$a$$
$$bb$$
$$d$$
$$c$$
$$c$$
$$Figure 24.21: The effect of a central dilatation H_{d,\lambda}(x).$$
$$-\longrightarrow$$
Khi $\lambda  = 1, H_{a,1}$ là đồng nhất thức. Lưu ý rằng $H_{a,\lambda} = \lambda  id_{E}\longrightarrow$. Khi $\lambda  \neq  0$, rõ ràng là $H_{a,\lambda}$ là afin song ánh. Ta kiểm chứng được ngay rằng
$$H_{a,\lambda} \circ H_{a,\mu} = H_{a,\lambda \mu}.$$
Ta có kết quả sau hữu ích kết quả.
$$\longrightarrow$$

> **Mệnh đề 24.9.** Cho trước bất kỳ không gian afin (affine space) $E$, với mọi afin song ánh $f \in$ GA(E), nếu $f = \lambda  id_{E}\longrightarrow$, với một số $\lambda  \in \mathbb{R}^{*}$ với $\lambda  \neq  1$, thì tồn tại duy nhất một điểm $c \in E$ sao cho $f = H_{c,\lambda}$.

*Chứng minh.* chứng minh là trực tiếp/dễ dàng, và được bỏ qua. Nó là cũng cho trước trong Gallier $[71]$.
$$\longrightarrow$$
Rõ ràng, nếu $f = id_{E}\longrightarrow$, ánh xạ afin (affine map) $f$ là phép tịnh tiến. Do đó, nhóm của afin các phép vị tự DIL(E) là rời nhau hợp của các phép tịnh tiến và của các phép vị tự của tỉ số $\lambda  \neq  0, 1$. Afin các phép vị tự có thể được cho trước một cách thuần túy hình học đặc trưng.
