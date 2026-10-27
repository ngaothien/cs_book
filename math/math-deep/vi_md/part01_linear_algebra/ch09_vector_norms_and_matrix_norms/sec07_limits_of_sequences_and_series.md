# Các giới hạn của Các dãy và Chuỗi


<!-- PAGE 374 -->
May mắn thay, mọi ma trận cỡ $n \times m$ $A$ có thể được viết dưới dạng
$$A = V DU^{\top}$$
Ở đâu $U$ và $V$ là trực giao và $D$ là rectangular ma trận đường chéo (diagonal matrix) với non-negative các phần tử (entries) (phân rã giá trị kỳ dị (SVD), hoặc SVD); xem Chương $22$. SVD có thể được được sử dụng để giải vô nghiệm/không tương thích hệ. Nó được hiển thị trong Chương $23$ rằng có một vectơ $x$ của nhỏ nhất chuẩn (norm) cực tiểu hóa $\|Ax$ - $b\|_{2}$. Nó được cho bởi (Penrose) nghịch đảo giả (pseudo-inverse) của $A$ (chính nó cho trước bởi SVD). Nó có đã được được quan sát rằng việc giải trong bình phương tối thiểu (least-squares) nghĩa có thể cho cũng nhiều trọng số đến “outliers,” rằng là, các điểm rõ ràng bên ngoài best-fit mặt phẳng. Trong trường hợp này, nó được ưu tiên hơn để cực tiểu hóa ($\ell^{1}$ -chuẩn (norm))
$$\sum_{i=1}^{n}  |ax_{i} + by_{i} + d -z_{i}|.$$
Điều này thực hiện không xuất hiện là tuyến tính bài toán, nhưng ta có thể sử dụng mẹo/kỹ thuật đến chuyển đổi điều này cực tiểu hóa bài toán vào bài toán quy hoạch tuyến tính (linear program) (mà có nghĩa là bài toán liên quan đến tuyến tính các ràng buộc). Lưu ý rằng |x| $= max{x, -x}$. Do đó bởi giới thiệu mới các biến $e_{1}, \dots  , e_{n}$, của ta cực tiểu hóa bài toán là tương đương đến bài toán quy hoạch tuyến tính (linear program) (LP):
$$minimizee_{1} + \cdots  + e_{n}$$
$$subject toax_{i} + by_{i} + d -z_{i} \le e_{i}$$
$$-(ax_{i} + by_{i} + d -z_{i}) \le e_{i}$$
$$1 \le i \le n.$$
Nhận thấy rằng các ràng buộc là tương đương đến
$$e_{i} \ge |ax_{i} + by_{i} + d -z_{i}|,1 \le i \le n.$$
Cho nghiệm tối ưu (optimal solution), ta phải có đẳng thức, vì ngược lại ta có thể giảm một số $e_{i}$ và thu được chẵn/ngay cả tốt hơn nghiệm. Của course, ta là không có dài hơn dealing với “thuần túy” tuyến tính đại số, vì của ta các ràng buộc là các bất đẳng thức. Ta ưu tiên không thu được vào quy hoạch tuyến tính (linear programming) phải bây giờ, nhưng ở trên ví dụ cung cấp tốt lý do đến learn nhiều hơn/thêm về quy hoạch tuyến tính (linear programming)!

## 9.7 Các giới hạn của Các dãy và Chuỗi

$\mathbb{R} \mathbb{C} n$
$$If x \in  or x \in  and if |x| < 1, it is well known that the sums \sum_{k}  x^{k}= 1+x+x^{2}+\cdots +x^{n}$$
Hội tụ đến giới hạn $1/(1$ - $x)$ khi $n$ đi đến vô cực, và $we^{=0}$ viết
$$\sum_{k=0}^{\infty}  x^{k} = \frac{1}{1 -x} .$$

<!-- PAGE 375 -->
Ví dụ,
$$\sum_{k=0}^{\infty}  \frac{1}{2^{k}} = 2.$$
Tương tự, các tổng
$$S_{n} = \sum_{k=0}^{n}  \frac{x^{k}}{k!}$$
$$\mathbb{R} \mathbb{C}$$
Hội tụ đến $e^{x}$ khi $n$ đi đến vô cực, với mọi $x$ (trong hoặc). Những gì nếu ta thay thế $x$ bởi thực hoặc phức $n \times  n$ ma trận $A$?
$$n nAk$$
$$The partial sums \sum_{k}  A^{k}and \sum_{k}  =0 still make sense, but we have to define what is$$
Giới hạn của dãy $of^{=0}$ các ma trận. $This^{k!}$ có thể được được thực hiện trong bất kỳ không gian vectơ định chuẩn (normed vector space).

> **Định nghĩa 9.13.** Cho $(E, \|\|)$ là không gian vectơ định chuẩn (normed vector space). dãy $(u_{n})_{n\in N}$ trong $E$ là bất kỳ hàm $u: \mathbb{N} \to E$. Với mọi $v \in E$, dãy $(u_{n})$ hội tụ đến $v$ (và $v$ là giới hạn của dãy $(u_{n}))$ nếu với mọi $\epsilon  > 0$, tồn tại một số nguyên $N > 0$ sao cho
$$\|u_{n} -v\|< \epsilon for all n \ge N.$$
Thường ta giả sử rằng dãy được chỉ số $by\mathbb{N}-{0}$, nghĩa là, của nó số hạng thứ nhất là $u_{1}$ thay vì $u_{0}$. Nếu dãy $(u_{n})$ hội tụ đến $v$, khi đó vì bởi tam giác bất đẳng thức
$$\|u_{m} -u_{n}\|\le \|u_{m} -v\|+ \|v -u_{n}\|,$$
Ta xem rằng với mọi $\epsilon  > 0$, ta có thể tìm $N > 0$ sao cho $\|u_{m}$ - $v\| < \epsilon /2$ và $\|u_{n}$ - $v\| < \epsilon /2$ với mọi $m, n \ge N$, và do đó
$$\|u_{m} -u_{n}\|< \epsilon for all m, n \ge N.$$
Ở trên tính chất là cần cho convergent dãy, nhưng không nhất thiết đủ. Ví dụ, nếu $E = \mathbb{Q}$, có các dãy của các hữu tỷ thỏa mãn ở trên điều kiện, nhưng
$$whose limit is not a rational number. For example, the sequence \sum_{k}  n1 converges to e, and$$
$$the sequence \sum_{k}  n=0(-1)_{2k+1}^{k1} converges to \pi /4, but e and \pi /4 are^{=1k!} not rational (in fact, they$$
Là transcendental). $However,\mathbb{R}$ được xây dựng $from\mathbb{Q}$ để đảm bảo rằng các dãy với ở trên tính chất hội tụ, và do đó là $\mathbb{C}$.

> **Định nghĩa 9.14.** Cho trước không gian vectơ định chuẩn (normed vector space) $(E, \|\|)$, dãy $(u_{n})$ là Dãy Cauchy (Cauchy sequence) nếu với mọi $\epsilon  > 0$, tồn tại một $N > 0$ sao cho
$$\|u_{m} -u_{n}\|< \epsilon for all m, n \ge N.$$
Nếu mọi Dãy Cauchy (Cauchy sequence) hội tụ, thì ta nói rằng $E$ là đầy đủ. đầy đủ các không gian vectơ định chuẩn cũng được gọi là một Không gian Banach (Banach space).

<!-- PAGE 376 -->
Cơ bản tính chất $of\mathbb{R}$ là rằng nó là đầy đủ. Nó suy ra ngay lập tức $that\mathbb{C}$ là cũng đầy đủ. Nếu $E$ là hữu hạn chiều thực hoặc phức không gian vectơ (vector space), vì bất kỳ hai các chuẩn là tương đương, ta có thể chọn $\ell^{\infty}$ chuẩn (norm), và thì bởi chọn cơ sở (basis) trong $E$, dãy $(u_{n})$ của các vectơ trong $E$ hội tụ khi và chỉ khi $n$ các dãy của các tọa độ $(u_{n}^{i}) (1 \le i \le n)$ hội tụ, do đó bất kỳ hữu hạn chiều thực hoặc phức không gian vectơ (vector space) là Không gian Banach (Banach space). Cho chúng ta bây giờ xét sự hội tụ của chuỗi.
$$Definition 9.15. Given a normed vector space (E, \|\|), a series is an infinite sum \sum_{k}  \infty =0 u_{k}$$
Của các phần tử $u_{k} \in E$. Ta ký hiệu bởi $S_{n}$ riêng tổng của thứ nhất $n + 1$ các phần tử,
$$S_{n} = \sum_{k=0}^{n}  u_{k}.$$
$$Definition 9.16. We say that the series \sum_{k}  \infty  u_{k} converges to the limit v \in E if the sequence$$
$(S_{n})$ hội tụ đến $v$, i.e., cho trước bất kỳ $\epsilon  > 0,^{=0}$ tồn tại một dương số nguyên $N$ sao cho với mọi $n \ge N$,
$$\|S_{n} -v\|< \epsilon .$$
Trong trường hợp này, ta nói rằng chuỗi là convergent. Ta nói rằng chuỗi $\infty  u_{k}$ hội tụ
$$absolutely\infty  \|\| \sum_{k}  =0$$
$$if the series of norms \sum_{k}  =0u_{k}is convergent.$$
$$If the series \sum_{k}  \infty =0 u_{k} converges to v, since for all m, n with m > n we have$$
$$\sum_{k=0}^{m}  u_{k} -S_{n} = \sum_{k=0}^{m}  u_{k} - \sum_{k=0}^{n}  u_{k} = \sum_{k=n+1}^{m}  u_{k},$$
$$if we let m go to infinity (with n fixed), we see that the series \sum_{k}  \infty =n+1 u_{k} converges and that$$
$$v -S_{n} = \sum_{k=n+1}^{\infty}  u_{k}.$$
Có chuỗi rằng là convergent nhưng không một cách tuyệt đối convergent; ví dụ, chuỗi
$$\sum_{k=1}^{\infty}  \frac{(1)^{k-1}}{k} -$$
$$converges to \ln 2, but \sum_{k}  \infty =1\overline{k} 1 does not converge (this sum is infinite).$$
Nếu $E$ là đầy đủ, điều ngược lại là enormously hữu ích kết quả.
$$Proposition 9.19. Assume (E, \|\|) is a complete normed vector space. If a series \sum_{k}  \infty =0 u_{k}$$
Là một cách tuyệt đối convergent, thì nó là convergent.
