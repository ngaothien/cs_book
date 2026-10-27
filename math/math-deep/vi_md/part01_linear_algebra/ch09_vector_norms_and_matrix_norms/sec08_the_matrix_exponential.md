# Ma trận Hàm mũ


<!-- PAGE 377 -->
$$Proof. If \sum_{k}  \infty =0 u_{k} is absolutely convergent, then we prove that the sequence (S_{m}) is a Cauchy$$
Sequence; nghĩa là, với mọi $\epsilon  > 0$, tồn tại một $p > 0$ sao cho với mọi $n \ge m \ge p$,
$$\|S_{n} -S_{m}\|\le \epsilon .$$
Nhận thấy rằng
$$\|S_{n} -S_{m}\|= \|u_{m+1} + \cdots  + u_{n}\|\le \|u_{m+1}\|+ \cdots  + \|u_{n}\|,$$
$$and since the sequence \sum_{k}  \infty  \|u_{k}\|converges, it satisfies Cauchy’s criterion. Thus, the se-$$
Quence $(S_{m})$ cũng $satisfies^{=0}$ Cauchy’s tiêu chuẩn, và vì $E$ là đầy đủ không gian vectơ (vector space), dãy $(S_{m})$ hội tụ.
Nhận xét: Nó có thể được được hiển thị rằng nếu $(E, \|\|)$ là không gian vectơ định chuẩn (normed vector space) sao cho mọi một cách tuyệt đối convergent chuỗi là cũng convergent, thì $E$ phải là đầy đủ (xem Schwartz $[156])$.
$$An important corollary of absolute convergence is that if the terms in series \sum_{k}  \infty  u_{k}$$
Là rearranged, thì thu được chuỗi là vẫn một cách tuyệt đối convergent và có $the^{=0}$ cùng tổng. Chính xác hơn, cho $\sigma$ là bất kỳ hoán vị (song ánh) của tự nhiên các số.
$$series \sum_{k}  \infty =0 u_{\sigma(k)} is called a rearrangement of the original series. The following result can be$$
Được hiển thị (xem Schwartz $[156])$.

> **Mệnh đề 9.20.** Giả sử $(E, \|\|)$ là không gian vectơ định chuẩn (normed vector space). Nếu chuỗi $\infty  u$ là conver-
$$gent as well as absolutely convergent, then for every permutation of\mathbb{N}, the series \sum_{k}  =0 \infty$$
$$\sigma \sum_{k}^{k}  =0 u_{\sigma(k)}$$
Là convergent và một cách tuyệt đối convergent, và tổng của nó bằng tổng của ban đầu chuỗi:
$$\sum_{k=0}^{\infty}  u_{\sigma(k)} = \sum_{k=0}^{\infty}  u_{k}.$$
Đặc biệt, nếu $(E, \|\|)$ là đầy đủ không gian vectơ định chuẩn (normed vector space), thì Mệnh đề 9.20 nghiệm đúng. Ta bây giờ áp dụng Mệnh đề 9.19 đến ma trận hàm mũ.

## 9.8 Ma trận Hàm mũ


> **Mệnh đề 9.21.** Với mọi $n \times  n$ thực hoặc phức ma trận $A$, chuỗi
$$\sum_{k=0}^{\infty}  \frac{A^{k}}{k!}$$
Hội tụ một cách tuyệt đối với mọi chuẩn toán tử (operator norm) trên $M_{n}(\mathbb{C})$ (hoặc $M_{n}(\mathbb{R}))$.

<!-- PAGE 378 -->
$$\mathbb{C}^{n}  \mathbb{R}^{n}$$

*Chứng minh.* Chọn bất kỳ chuẩn (norm) trên (hoặc) và cho $\|\|$ là tương ứng chuẩn toán tử (operator norm) trên $M_{n}(\mathbb{C})$. Vì $M_{n}(\mathbb{C})$ có số chiều $n^{2}$, nó là đầy đủ. Theo Mệnh đề 9.19, nó suffices đến
$$n


K$$
$$show that the series of nonnegative reals \sum_{k}  =0A\overline{k}\overline{!} converges. Since \|\|is an operator$$
Chuẩn (norm), điều này chuẩn ma trận (matrix norm), do đó ta có
$$\|\|^{k}$$
$$\sum_{k=0}^{n}  \frac{A^{k}}{k!} \le \sum_{k=0}^{n}  \frac{A}{k!} \le e^{\|A\|}.$$
$$n


K$$
$$Thus, the nondecreasing sequence of positive real numbers \sum_{k}  =0A\overline{k}\overline{!} is bounded by e^{\|A\|},$$
Và bởi cơ bản tính chất của $\mathbb{R}$, nó có least trên cận mà là của nó giới hạn.

> **Định nghĩa 9.17.** Cho $E$ là hữu hạn chiều thực hoặc phức không gian vectơ định chuẩn (normed vector space). Cho bất kỳ ma trận cỡ $n \times  n$ $A$, giới hạn của chuỗi
$$\sum_{k=0}^{\infty}  \frac{A^{k}}{k!}$$
Là hàm mũ của $A$ và được ký hiệu là $e^{A}$.
$$\mathbb{C}$$
Cơ bản tính chất của hàm mũ $x \mapsto e^{x}$ với $x \in$ là
$$\mathbb{C}$$
$$e^{x+y}= e^{x}e^{y},for all x, y \in .$$
Hệ quả là, $e^{x}$ là luôn luôn khả nghịch và $(e^{x})^{-1} = e^{-x}$. Cho các ma trận, bởi vì phép nhân ma trận (matrix multiplication) là không giao hoán, nói chung,
$$e^{A+B}= e^{A}e^{B}$$
Không thỏa mãn! kết quả này là salvaged như sau.

> **Mệnh đề 9.22.** Với mọi hai $n \times  n$ phức các ma trận $A$ và $B$, nếu $A$ và $B$ giao hoán, nghĩa là, $AB = BA$, thì
$$e^{A+B}= e^{A}e^{B}.$$
Chứng minh của Mệnh đề 9.22 có thể được tìm thấy trong Gallier $[73]$. Vì $A$ và $-A$ giao hoán, như hệ quả của Mệnh đề 9.22, ta xem rằng $e^{A}$ là luôn luôn khả nghịch và rằng
$$(e^{A})^{-1}= e^{-A}.$$
Nó là cũng dễ để xem rằng
$$(e^{A})^{\top}= e^{A\top}.$$

<!-- PAGE 379 -->
Nói chung, không có closed-form công thức cho hàm mũ $e^{A}$ của ma trận $A$, nhưng cho skew các ma trận đối xứng có số chiều $2$ và $3$, có tường minh các công thức. Everyone nên enjoy việc tính toán hàm mũ $e^{A}$ ở đâu
$$A = \begin{pmatrix} 0 & -\theta \\ \theta & 0 \end{pmatrix} .$$
Nếu ta viết
$$J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} ,$$
Thì
$$A = \theta J$$
Then chốt tính chất là rằng
$$J^{2}= -I.$$

> **Mệnh đề 9.23.** Nếu $A = \theta J$, thì
$$e^{A}= \cos \theta I + \sin \theta J = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} .$$

*Chứng minh.* Ta có
$$A^{4n}= \theta^{4n} I_{2},$$
$$A^{4n+1}= \theta^{4n+1} J,$$
$$A^{4n+2}= -\theta^{4n+2} I_{2},$$
$$A^{4n+3}= -\theta^{4n+3} J,$$
Và do đó
$$e^{A}= I_{2} + \frac{\theta}{1!} J - \frac{\theta^{2}}{2!} I_{2} - \frac{\theta^{3}}{3!} J + \frac{\theta^{4}}{4!} I_{2} + \frac{\theta^{5}}{5!} J - \frac{\theta^{6}}{6!} I_{2} - \frac{\theta^{7}}{7!} J + \cdots  .$$
Rearranging thứ tự của các số hạng, ta có
$$e^{A}= \begin{pmatrix} \theta^{2} & \theta^{4} & \theta^{6} \\ 1 - & + & - & + \cdots \\ 2! & 4! & 6! \end{pmatrix} I_{2} + \begin{pmatrix} \theta \\ \theta^{3} & \theta^{5} & \theta^{7} \\ - & + & - & + \cdots \\ 1! & 3! & 5! & 7! \end{pmatrix} J.$$
Ta recognize lũy thừa chuỗi cho cos $\theta$ và sin $\theta$, và do đó
$$e^{A}= \cos \theta I_{2} + \sin \theta J,$$
Rằng là
$$e^{A}= \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} ,$$
Như đã khẳng định.
