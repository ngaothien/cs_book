# Tóm tắt


<!-- PAGE 1939 -->
Ở đâu $A$ là một ma trận cỡ $m \times  n$, $F$ là một ma trận cỡ $p \times  n$, và hoặc $A$ có hạng (rank) $n$ hoặc $F$ có hạng (rank) $n$. bài toán này được chuyển đổi đến ADMM bài toán
$$minimize\|Ax -b\|_{2}^{2} + \tau  \|z\|_{1}$$
$$subject to Fx -z = 0,$$
$$and the corresponding ADMM procedure (in scaled form) is$$
$$x^{k+1}= (A^{\top}A + \rho F^{\top}F)^{-1}(A^{\top}b + \rho F^{\top}(z^{k}-u^{k}))$$
$$z^{k+1}= S_{\tau /\rho}(Fx^{k+1}+ u^{k})$$
$$u^{k+1}= u^{k}+ Fx^{k+1}-z^{k+1}.$$
$(6)$ Nhóm Lasso. Điều này tổng quát hóa của $(3)$. Ở đây ta giả sử rằng $x$ là split như $x = (x_{1}, \dots  , x_{N})$, với $x_{i} \in \mathbb{R}_{i}^{n}$ và $n_{1} + \cdots  + x_{N} = n$, và regularizing số hạng $\|x\|_{1}$ được thay thế bởi
$$\sum_{i}  N=1 \|x_{i}\|_{2}. When n_{i} = 1, this reduces to (3). The z-update of the ADMM   procedure$$
Cần đến được sửa đổi. Ta định nghĩa soft thresholding toán tử $\mathcal{S}_{c}$: $\mathbb{R}^{m} \to \mathbb{R}^{m}$ cho trước bởi
$$\mathcal{S}_{c}(v) = \begin{pmatrix} c \\ 1 - \\ \|v \end{pmatrix} \|_{2+}v,$$
Với $\mathcal{S}_{c}(0) = 0$. Thì z-update bao gồm của $N$ updates
$$z_{i}^{k+1}=\mathcal{S}_{\tau /\rho}(x_{i}^{k+1}+ u^{k}),i = 1, \dots  , N.$$
Phương pháp có thể được được mở rộng đến deal với overlapping các nhóm; xem Boyd et al. $[28]$ (Mục 6.4). Có nhiều nhiều hơn/thêm các ứng dụng của ADMM được thảo luận trong Boyd et al. $[28]$, bao gồm cả consensus và sharing. Xem cũng Strang $[177]$ cho ngắn gọn overview.

## 52.9 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ Tăng đối ngẫu (dual ascent). $\bullet$ Augmented Hàm Lagrange (Lagrangian). $\bullet$ Hình phạt (penalty) tham số. $\bullet$ Phương pháp của các nhân tử. $\bullet$ ADMM (phương pháp đổi hướng nhân tử (ADMM)).
