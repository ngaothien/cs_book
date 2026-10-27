# Các bài tập


<!-- PAGE 1129 -->
$\bullet$ Bất biến không gian con. $\bullet$ f-conductor của $u$ vào $W$; dẫn tử (conductor) của $u$ vào $W. \bullet$ Chéo hóa được (diagonalizable) các ánh xạ tuyến tính (linear maps). $\bullet$ Giao hoán các họ của các ánh xạ tuyến tính (linear maps). $\bullet$ Phân rã sơ cấp (primary decomposition). $\bullet$ Suy rộng/tổng quát hóa các vectơ riêng (eigenvectors). $\bullet$ Lũy linh (nilpotent) ánh xạ tuyến tính (linear map). $\bullet$ Chuẩn tắc/bình thường tạo thành của lũy linh (nilpotent) ánh xạ tuyến tính (linear map). $\bullet$ Jordan phân rã. $\bullet$ Khối Jordan (Jordan block). $\bullet$ Jordan ma trận. $\bullet$ Jordan chuẩn tắc/bình thường tạo thành. $\bullet$ Các hệ của bậc nhất tuyến tính vi phân các phương trình.

## 31.8 Các bài tập

Bài toán 31.1. Cho trước ánh xạ tuyến tính (linear map) $f$: $E \to E$, chứng minh rằng tập hợp Ann(f) của các đa thức rằng annihilate $f$ là lý tưởng (ideal).
Bài toán 31.2. Cung cấp chi tiết của Mệnh đề 31.3.
Bài toán 31.3. Chứng minh rằng f-conductor $S_{f}(u, W)$ là lý tưởng (ideal) trong K[X] (Mệnh đề 31.4).
Bài toán 31.4. Chứng minh rằng các đa thức $g_{1}, \dots  , g_{k}$ được sử dụng trong chứng minh của Định lý 31.10 là một cách tương đối nguyên tố.
Bài toán 31.5. Tìm đa thức tối tiểu (minimal polynomial) của ma trận
$$A = \begin{pmatrix} 6 & -3 & -2 \\ 4 & -1 & -2 \\ 10 & 5 & 3 \end{pmatrix} .$$
$$--$$
Bài toán 31.6. Tìm Jordan phân rã của ma trận
$$A = \begin{pmatrix} 3 & 1 & -1 \\ 2 & 2 & -1 \\ 2 & 2 & 0 \end{pmatrix} .$$

<!-- PAGE 1130 -->
Bài toán 31.7. Cho $f$: $E \to E$ là ánh xạ tuyến tính (linear map) trên không gian vectơ hữu hạn chiều. Chứng minh rằng nếu $f$ có hạng (rank) $1$, thì hoặc $f$ là chéo hóa được (diagonalizable) hoặc $f$ là lũy linh (nilpotent) nhưng không cả hai.
Bài toán 31.8. Tìm Dạng Jordan (Jordan form) của ma trận
$$A = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3 \\ 0 & 0 & 0 & 0 \end{pmatrix} .$$
Bài toán 31.9. Cho $N$ là $3 \times  3$ lũy linh (nilpotent) ma trận trên $\mathbb{C}$. Chứng minh rằng ma trận $A =$ I $+ (1/2)N$ - $(1/8)N^{2}$ thỏa mãn phương trình
$$A^{2}= I + N.$$
Nói cách khác, $A$ là square nghiệm (root) của I $+ N$. Tổng quát hóa ở trên sự kiện đến bất kỳ $n \times  n$ lũy linh (nilpotent) ma trận $N$ trên $\mathbb{C}$ bằng cách sử dụng nhị thức chuỗi cho $(1 + t)^{1/2}$.
Bài toán 31.10. Cho $K$ là algebraically đóng trường (ví dụ, $K = \mathbb{C})$. Chứng minh rằng mọi $4 \times  4$ ma trận là đồng dạng đến Jordan ma trận của sau đây tạo thành:
$$\lambda_{1} 000\lambda 100$$
$$0\lambda_{2} 00,0\lambda 00, \begin{pmatrix} \lambda & 1 & 0 & 0 \\ 0 & \lambda & 1 & 0 \\ 0 & 0 & \lambda & 0 \\ 0 & 0 & 0 & \lambda_{4} \end{pmatrix} ,$$
$$00\lambda_{3} 000\lambda_{3} 0$$
$$$$
$$000\lambda_{4} 000\lambda_{4}$$
$$\lambda 100\lambda 100$$
$$0\lambda 000\lambda 10$$
$$,.$$
$$00\mu 100\lambda 1$$
$$$$
$$000\mu 000\lambda$$
Bài toán 31.11. Trong bài toán này trường $K$ là của characteristic $0$. Xét $(r \times  r)$ Khối Jordan (Jordan block)
$$J_{r}(\lambda ) = \begin{pmatrix} \lambda & 1 & 0 & \cdots & 0 \\ 0 & \lambda & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \ddots & \vdots \\ 0 & 0 & 0 & \ddots & 1 \\ 0 & 0 & 0 & \lambda \end{pmatrix} .$$
$$\cdots$$
Chứng minh rằng với mọi đa thức f(X), ta có
$$f(J_{r}(\lambda )) = \begin{pmatrix} f(\lambda ) & f_{1}(\lambda ) & f_{2}(\lambda ) & \cdots & f_{r-1}(\lambda ) \\ 0 & f(\lambda ) & f_{1}(\lambda ) & \cdots & f_{r-2}(\lambda ) \\ \vdots & \vdots & \ddots & \ddots & \vdots \\ 0 & 0 & 0 & \ddots & f_{1}(\lambda ) \\ 0 & 0 & 0 & f(\lambda ) \end{pmatrix} ,$$
$$\cdots$$

<!-- PAGE 1131 -->
Ở đâu
$$f_{k}(X) = \frac{f^{(k)}(X)}{k!} ,$$
Và $f^{(k)} (X)$ là đạo hàm thứ $k$ của f(X).

<!-- PAGE 1132 -->
