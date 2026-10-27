# Các không gian xạ ảnh


<!-- PAGE 876 -->
Những gì ta chỉ được phác thảo là tổng quát phương pháp đến deal với hữu tỷ các đường cong. Ta có thể sử dụng của ta “hat cách xây dựng” đến embed afin $space\mathcal{E}$ vào không gian vectơ (vector space) $\mathcal{E}$ có một nhiều hơn/thêm dimen-
$$b$$
$$sion, then construct the projective space P \begin{pmatrix} \mathcal{E} b \end{pmatrix} . This turns out to be the “projective com-$$
$$pletion” of the affine space \mathcal{E}. Then we can define a rational curve in P \begin{pmatrix} \mathcal{E} b \end{pmatrix} , basically as the$$
Trung tâm phép chiếu của đa thức đường cong trong $\mathcal{E}$ quay lại lên $P$. cùng cách tiếp cận có thể được được sử dụng
$$to deal with rational surfaces.  b \begin{pmatrix} \mathcal{E} b \\ Due to the lack of space, such a presentation is omitted. \end{pmatrix} How-$$
Ever, nó có thể được tìm thấy trên web; xem $http://www.cis.upenn.edu/ jean/gbooks/geom2.html$.
$$e$$
Tổng quát hơn, bổ sung xạ ảnh (projective completion) của không gian afin (affine space) là rất thuận tiện công cụ đến handle “các điểm tại vô cực” trong gọn gàng cách thức. Điều này chương chứa ngắn gọn trình bày của các khái niệm của xạ ảnh hình học. sau đây các khái niệm được trình bày: các không gian xạ ảnh, xạ ảnh các hệ quy chiếu, thuần nhất các tọa độ, xạ ảnh các ánh xạ, xạ ảnh các siêu phẳng, multiprojective các ánh xạ, afin patches. bổ sung xạ ảnh (projective completion) của không gian afin (affine space) được trình bày bằng cách sử dụng “hat cách xây dựng.” các định lý của Pappus và Desargues được chứng minh, bằng cách sử dụng phương pháp trong mà các điểm là “sent đến vô cực.” Ta cũng thảo luận tỉ số kép (cross-ratio) và đối ngẫu. chương kết thúc với rất ngắn gọn explanation của sử dụng của phức hóa của không gian xạ ảnh (projective space) trong thứ tự để định nghĩa khái niệm của góc và tính trực giao trong xạ ảnh đặt. Ta cũng bao gồm ngắn mục trên các ứng dụng của xạ ảnh hình học, notably đến máy tính thị giác (camera calibration), efficient communication, và error-correcting codes.

## 26.2 Các không gian xạ ảnh

Như trong trường hợp của afin hình học, của ta trình bày của xạ ảnh hình học là khá sketchy. Cho systematic treatment của xạ ảnh hình học, ta recommend Berger $[11, 12]$, Samuel $[148]$, Pedoe $[141]$, Coxeter $[45, 46, 43, 44]$, Beutelspacher và Rosenbaum $[22]$, Fresnel $[66]$, Sidler $[167]$, Tisseron $[181]$, Lehmann và Bkouche $[119]$, Vienne $[191]$, và cổ điển treatise bởi Veblen và Young $[189, 190]$, mà, mặc dù slightly old-fashioned, là một cách xác định worth reading. Emil Artin’s nổi tiếng cuốn sách $[6]$ chứa, trong số khác things, axiomatic trình bày của xạ ảnh hình học, và wealth của hình học material được trình bày từ đại số điểm của quan điểm. Khác “oldies nhưng goodies” bao gồm đẹp các cuốn sách bởi Darboux $[47]$ và Klein $[106]$. Cho development của xạ ảnh hình học addressing delicate bài toán của định hướng, xem Stolfi[173], và cho cách tiếp cận geared towards máy tính đồ họa, xem Penna và Patterson $[142]$. Thứ nhất, ta định nghĩa các không gian xạ ảnh, cho phép trường $K$ là tùy ý (mà thực hiện không có harm, và là cần thiết đến cho phép hữu hạn và phức các không gian xạ ảnh). Xấp xỉ/đại khái speaking, mọi xạ ảnh khái niệm là tuyến tính–đại số khái niệm “sai khác một vô hướng.” Cho các không gian, điều này được tạo precise như sau.

> **Định nghĩa 26.1.** Cho trước không gian vectơ (vector space) $E$ trên trường $K$, không gian xạ ảnh (projective space) P(E) được cảm sinh bởi $E$ là tập hợp $(E -{0})/ \sim$ của các lớp tương đương của khác không các vectơ trong $E$ dưới

<!-- PAGE 877 -->
Quan hệ tương đương (equivalence relation) $\sim$ được định nghĩa sao cho với mọi $u, v \in E -{0}$,
$$u \sim viffv = \lambda u, for some \lambda  \in K -{0}.$$
Phép chiếu chính tắc (canonical projection) $p: (E -{0}) \to$ P(E) là hàm associating lớp tương đương (equivalence class) $[u]_{\sim}$ modulo $\sim$ đến u̸ $= 0$. số chiều dim(P(E)) của P(E) được định nghĩa như sau: Nếu $E$ là của vô hạn số chiều, thì dim(P(E)) $=$ dim(E), và nếu $E$ có hữu hạn số chiều, dim(E) $= n \ge 1$ thì dim(P(E)) $= n$ - $1$. một cách toán học, không gian xạ ảnh (projective space) P(E) là tập hợp của các lớp tương đương của các vectơ trong $E$. spirit của xạ ảnh hình học là đến quan điểm lớp tương đương (equivalence class) p(u) $= [u]_{\sim}$ như “atomic” object, forgetting internal cấu trúc của lớp tương đương (equivalence class). Cho điều này lý do, nó là thông lệ đến gọi lớp tương đương (equivalence class) $a = [u]_{\sim}$ điểm (toàn bộ lớp tương đương (equivalence class) $[u]_{\sim}$ là collapsed vào đơn lẻ object được quan điểm như điểm).
Các nhận xét:
$(1)$ Nếu ta quan điểm $E$ như không gian afin (affine space), thì với mọi khác không vectơ $u \in E$, vì
$$[u]_{\sim}= {\lambda u | \lambda  \in K, \lambda  \neq  0},$$
Đặt
$$Ku = {\lambda u | \lambda  \in K}$$
Ký hiệu không gian con có số chiều $1$ được sinh (spanned) bởi $u$, ánh xạ
$$[u]_{\sim}\mapsto Ku$$
Từ P(E) đến tập hợp của một chiều các không gian con của $E$ là rõ ràng song ánh, và vì các không gian con có số chiều $1$ tương ứng với các đường thẳng qua gốc trong $E$, ta có thể quan điểm P(E) như tập hợp của các đường thẳng trong $E$ chuyển qua gốc. Do đó, không gian xạ ảnh (projective space) P(E) có thể được được quan điểm như tập hợp thu được từ $E$ khi các đường thẳng qua gốc là treated như các điểm. Tuy nhiên, điều này là somewhat deceptive quan điểm. Thật vậy, tùy thuộc trên cấu trúc của không gian vectơ (vector space) $E$, đường thẳng (qua gốc) trong $E$ có thể là fairly phức object, và treating đường thẳng chỉ như điểm là một cách thực mental game. Ví dụ, $E$ có thể là không gian vectơ (vector space) của thực thuần nhất các đa thức P(x, $y, z)$ của bậc $2$ trong ba các biến $x, y, z$ (cộng null đa thức), và “đường thẳng” (qua gốc) trong $E$ tương ứng với đại số đường cong của bậc $2$. các nhiều của chi tiết cần là filled trong, nhưng xấp xỉ/đại khái speaking, đường cong được định nghĩa bởi $P$ là “không quỹ tích của P,” i.e., tập hợp của các điểm $(x, y, z) \in P(\mathbb{R}^{3})$ (hoặc perhaps trong $P(\mathbb{C}^{3}))$ cho mà P(x, $y, z) = 0$. Ta sẽ đến quay lại đến điều này điểm trong Mục 26.4 sau có đã giới thiệu thuần nhất các tọa độ. Tổng quát hơn, $E$ có thể là không gian vectơ (vector space) của thuần nhất các đa thức của bậc $m$ trong $3$ hoặc nhiều hơn/thêm các biến (cộng null đa thức), và các đường thẳng trong $E$ tương ứng với

<!-- PAGE 878 -->
Như vậy objects như đại số các đường cong, đại số các mặt, và đại số varieties. điểm của quan điểm ở đâu phức object chẳng hạn như đường cong hoặc mặt là treated như điểm trong (xạ ảnh) không gian là thực sự rất fruitful và là một của các chúng của đại số hình học (xem Fulton $[67]$ hoặc Harris $[90])$.
$(2)$ Khi dim(E) $= 1$, ta có dim(P(E)) $= 0$. Khi $E = {0}$, ta có P(E) $= \emptyset$. Bởi quy ước, ta cho nó số chiều $-1$. Ta ký hiệu không gian xạ ảnh (projective space) $P(K^{n+1})$ bởi $\mathbb{P}_{K}^{n}$. Khi $K = \mathbb{R}$, ta cũng ký hiệu $\mathbb{P}_{R}^{n}$ bởi $\mathbb{RP}^{n}$, và khi $K = \mathbb{C}$, ta ký hiệu $\mathbb{P}_{C}^{n}$ bởi $\mathbb{CP}^{n}$. không gian xạ ảnh (projective space) $\mathbb{P}_{K}^{0}$ là (xạ ảnh) điểm. không gian xạ ảnh (projective space) $\mathbb{P}_{K}^{1}$ được gọi là một xạ ảnh đường thẳng. không gian xạ ảnh (projective space) $\mathbb{P}_{K}^{2}$ được gọi là một xạ ảnh mặt phẳng. không gian xạ ảnh (projective space) P(E) có thể được visualized trong sau đây cách. Để đơn giản, giả sử
$$\mathbb{R}^{n+1} \mathbb{RP}^{n}$$
Rằng $E =$, và do đó P(E) $=$ (cùng lập luận áp dụng đến $E = K^{n+1}$, ở đâu $K$ là bất kỳ trường). Cho $H$ là afin siêu phẳng (hyperplane) bao gồm của tất cả các điểm $(x_{1}, \dots  , x_{n+1})$ sao cho $x_{n+1} = 1$. Mọi khác không vectơ $u$ trong $E$ xác định đường thẳng $D$ chuyển qua gốc, và điều này đường thẳng cắt siêu phẳng (hyperplane) $H$ trong duy nhất điểm, trừ khi $D$ là song song đến $H$. Khi $D$ là song song đến $H$, đường thẳng tương ứng với lớp tương đương (equivalence class) của $u$ có thể được thought của như điểm tại vô cực, thường được ký hiệu bởi $u_{\infty}$. Do đó, không gian xạ ảnh (projective space) P(E) có thể được được quan điểm như tập hợp của các điểm trong siêu phẳng (hyperplane) $H$, cùng với các điểm tại vô cực liên kết với các đường thẳng trong siêu phẳng (hyperplane) $H_{\infty}$ của phương trình $x_{n+1} = 0$. Ta sẽ đến quay lại đến điều này điểm của quan điểm khi ta xét bổ sung xạ ảnh (projective completion) của không gian afin (affine space). Hình 26.3 minh họa ở trên
$$\mathbb{R}^{2} \mathbb{R}^{3}$$
Biểu diễn của không gian xạ ảnh (projective space) cho $E =$ và $E =$.
$$[v]~[u]~[v]~[u]~$$
$$y = 1$$
$$z = 1$$
$$vu$$
$$u\infty$$
$$u\infty$$
$$(i.)$$
$$(ii.)$$
$$\mathbb{RP}^{1}  \mathbb{RP}^{2}$$
$$Figure 26.3: The hyperplane model representations ofand.$$
Ta refer đến ở trên mô hình của P(E) như siêu phẳng (hyperplane) mô hình. Trong điều này mô hình một số

<!-- PAGE 879 -->
$$\mathbb{R}^{n+1}$$
Siêu phẳng (hyperplane) $H_{\infty}$ (qua gốc) trong là singled ra, và các điểm của P(E) phát sinh từ siêu phẳng (hyperplane) $H_{\infty}$ là declared là “các điểm tại vô cực.” mục đích của afin siêu phẳng (hyperplane) $H$ song song đến $H_{\infty}$ và phân biệt từ $H_{\infty}$ là để thu được các ảnh cho khác các điểm trong P(E) (i.e., những phần tử đó rằng phát sinh từ các đường thẳng không được chứa trong $H_{\infty})$. Nó nên được lưu ý rằng lựa chọn của mà các điểm nên được xét như vô hạn là tương đối đến lựa chọn của $H_{\infty}$. quan điểm nhất định các điểm của P(E) như các điểm tại vô cực là thuận tiện cho thu được mental picture của P(E), nhưng ở đó là không có gì nội tại về rằng. Các điểm của P(E) là tất cả bằng nhau, và trừ khi một số additional cấu trúc trong đã giới thiệu trong P(E) (chẳng hạn như siêu phẳng (hyperplane)), điểm trong P(E) không’t biết liệu nó là vô hạn! khái niệm của điểm tại vô cực là một cách thực afin khái niệm. Điều này điểm sẽ được tạo precise trong Mục 26.8.
$$\mathbb{RP}^{n} \mathbb{R}^{n+1}$$
Một lần nữa, cho $= P($), thay vì của xét siêu phẳng (hyperplane) $H$, ta có thể xét n-sphere $S^{n}$ của tâm $0$ và bán kính $1$, i.e., tập hợp của các điểm $(x_{1}, \dots  , x_{n+1})$ sao cho
$$x_{1}^{2} + \cdots  + x_{n}^{2} + x_{n+1}^{2} = 1.$$
Trong trường hợp này, mọi đường thẳng $D$ qua tâm của mặt cầu cắt mặt cầu $S^{n}$ trong hai
$$\mathbb{RP}^{n}$$
Antipodal các điểm $a_{+}$ và $a_{-}$. không gian xạ ảnh (projective space) là không gian thương (quotient space) thu được từ mặt cầu $S^{n}$ bởi đồng nhất antipodal các điểm $a_{+}$ và $a_{-}$. Nó là khó đến visualize như vậy object! Ta gọi điều này mô hình của P(E) cầu mô hình. Xem Hình 26.4.
$$y$$
$$x$$
$$x$$
$$xy$$
$$x$$
$$(i.)$$
$$(ii.)$$
$$\mathbb{RP}^{1}  \mathbb{RP}^{2}$$
$$Figure 26.4: The spherical model representations ofand.$$
Nhiều hơn/thêm tinh tế cách xây dựng bao gồm trong xét (trên) half-sphere thay vì của mặt cầu, ở đâu trên half-sphere $S_{+}^{n}$ là tập hợp của các điểm trên mặt cầu $S^{n}$ sao cho $x_{n+1} \ge 0$. Điều này time, mọi đường thẳng qua tâm cắt (trên) half-sphere trong đơn lẻ điểm, ngoại trừ trên biên (boundary) của half-sphere, ở đâu nó cắt trong hai antipodal các điểm $a_{+}$
$$\mathbb{RP}^{n}$$
Và $a_{-}$. Do đó, không gian xạ ảnh (projective space) là không gian thương (quotient space) thu được từ (trên)

<!-- PAGE 880 -->
$$x$$
$$xx$$
$$(i.)$$
$$x$$
$$x$$
$$(ii.)$$
$$\mathbb{RP}^{1}  \mathbb{RP}^{2}$$
$$Figure 26.5: The half-spherical model representations ofand.$$
Half-sphere $S_{+}^{n}$ bởi đồng nhất antipodal các điểm $a_{+}$ và $a_{-}$ trên biên (boundary) của half-sphere. Ta gọi điều này mô hình của P(E) half-spherical mô hình; xem Hình 26.5. Khi $n = 2$, ta thu được đường tròn. Khi $n = 3$, trên half-sphere là đồng phôi
$$\mathbb{RP}^{2}$$
Đến đóng đĩa (nói, bởi phép chiếu trực giao (orthogonal projection) lên mặt phẳng $xy$), và là trong song ánh với đóng đĩa trong mà antipodal các điểm trên biên (biên (boundary)) của nó (unit đường tròn) có đã được được đồng nhất. Điều này là khó đến visualize! Trong điều này mô hình của thực không gian xạ ảnh (projective space), xạ ảnh các đường thẳng là great semicircles trên trên half-sphere, với antipodal các điểm trên biên (boundary) được đồng nhất. Biên (boundary) các điểm tương ứng với các điểm tại vô cực. Bởi phép chiếu trực giao (orthogonal projection), các phần tử này great semicircles tương ứng với semiellipses, với antipodal các điểm trên biên (boundary) được đồng nhất. Traveling dọc theo như vậy xạ ảnh “đường thẳng,” khi ta đạt tới biên (boundary) điểm, ta “wrap xung quanh”! Nói chung, trên half-sphere $S_{+}^{n}$ là đồng phôi đến đóng unit hình cầu trong $\mathbb{R}^{n}$, có biên (boundary) là $(n$ - 1)-mặt cầu $S^{n-1}$. Ví dụ, không gian xạ ảnh (projective space) $\mathbb{RP}^{3}  \mathbb{R}^{3}$ là trong song ánh với đóng unit hình cầu trong, với antipodal các điểm trên biên (biên (boundary)) của nó (mặt cầu $S^{2})$ được đồng nhất!
Các nhận xét:
$(1) A$ không gian xạ ảnh (projective space) P(E) có đã được được định nghĩa như tập hợp mà không có bất kỳ tôpô cấu trúc. Khi trường $K$ là hoặc trường $\mathbb{R}$ của các số thực hoặc trường $\mathbb{C}$ của phức các số, không gian vectơ (vector space) $E$ là không gian tôpô (topological space). Do đó, phép chiếu ánh xạ $p: (E -{0}) \to$ P(E) cảm sinh tôpô trên không gian xạ ảnh (projective space) P(E), cụ thể là thương tôpô. Điều này có nghĩa là tập con $V$ của P(E) là mở khi và chỉ khi $p^{-1}(V$) là tập mở (open set) trong $E$. Thì, cho
$$\mathbb{RP}^{n}$$
Ví dụ, hóa ra là thực không gian xạ ảnh (projective space) là đồng phôi đến không gian
