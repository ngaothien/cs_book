# Một số Các ứng dụng của Euclidean Hình học


<!-- PAGE 492 -->

*Chứng minh.* Nếu det() $= 0$, bất đẳng thức là tầm thường. Ngược lại, $A$ là xác định dương (positive definite), và theo Định lý 8.10 (Nhân tử hóa Cholesky (Cholesky factorization)), tồn tại duy nhất một tam giác trên (upper triangular) ma trận $B$ với dương đường chéo các phần tử (entries) sao cho
$$A = B^{\top}B.$$
Do đó, det() $= det(B^{\top}B) = det(B^{\top})$ det(B) $= det(B)^{2}$. Nếu ta áp dụng Hadamard bất đẳng thức (Mệnh đề 12.17) đến $B$, ta thu được
$$1/2$$
$$\det(B) \le \prod_{j=1}^{n}  \begin{pmatrix} b_{ij}^{2} \end{pmatrix} \sum_{i=1}^{n}  .(*)$$
Tuy nhiên, đường chéo các phần tử (entries) $a_{jj}$ của $A = B^{\top}B$ là một cách chính xác square các chuẩn $\|B^{j}\|_{2}^{2} =$
$$\sum_{i}  n=1 b_{ij}^{2}, so by squaring (*), we obtain$$
$$\det(A) = \det(B)^{2}\le \prod_{j=1}^{n}  \begin{pmatrix} b_{ij}^{2} \end{pmatrix} \sum_{i=1}^{n}  = \prod_{j=1}^{n}  a_{jj}.$$
Nếu det() $\neq  0$ và đẳng thức nghiệm đúng, thì $B$ phải có trực giao các cột, mà suy ra rằng $B$ là ma trận đường chéo (diagonal matrix), và do đó là $A$. Ta derived thứ hai Hadamard bất đẳng thức (Mệnh đề 12.18) từ thứ nhất (Mệnh đề 12.17). Ta để lại nó như một bài tập để chứng minh rằng thứ nhất Hadamard bất đẳng thức có thể được deduced từ thứ hai Hadamard bất đẳng thức.

## 12.9 Một số Các ứng dụng của Euclidean Hình học

Euclidean hình học có các ứng dụng trong tính toán hình học, đặc biệt Voronoi các biểu đồ và Delaunay các tam giác phân. Trong turn, Voronoi các biểu đồ có các ứng dụng trong motion planning (xem O’Rourke $[138])$. Euclidean hình học cũng có các ứng dụng đến ma trận giải tích/phân tích. Nhắc lại rằng thực $n \times  n$ ma trận $A$ là đối xứng nếu nó bằng của nó chuyển vị (transpose) $A^{\top}$. Một của hầu hết quan trọng các tính chất của các ma trận đối xứng là rằng chúng có thực các trị riêng (eigenvalues) và rằng chúng có thể được được chéo hóa bởi ma trận trực giao (orthogonal matrix) (xem Chương $17)$. Điều này có nghĩa là với mọi ma trận đối xứng (symmetric matrix) $A$, có một ma trận đường chéo (diagonal matrix) $D$ và ma trận trực giao (orthogonal matrix) $P$ sao cho
$$A = PDP^{\top} .$$
Chẵn/ngay cả dù nó là không luôn luôn khả dĩ/có thể đến diagonalize tùy ý ma trận, có khác nhau các phân rã liên quan đến các ma trận trực giao rằng là của great thực tế interest. Ví dụ, với mọi thực ma trận $A$, ở đó là Phân rã QR (QR-decomposition), mà nói rằng rằng thực ma trận $A$ có thể được biểu diễn dưới dạng
$$A = QR,$$
