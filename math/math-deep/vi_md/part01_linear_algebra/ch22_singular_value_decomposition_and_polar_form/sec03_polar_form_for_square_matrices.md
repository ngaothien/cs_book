# Dạng cực (polar form) cho Các ma trận vuông


<!-- PAGE 757 -->

## 22.3 Dạng cực (polar form) cho Các ma trận vuông

Khái niệm closely related đến SVD là dạng cực (polar form) của ma trận.

> **Định nghĩa 22.4.** cặp $(R, S)$ sao cho $A = RS$ với $R$ trực giao và $S$ đối xứng nửa xác định dương (positive semidefinite) được gọi là một phân rã cực (polar decomposition) của $A$. Định lý 22.5 suy ra rằng với mọi thực $n\times n$ ma trận $A$, tồn tại một ma trận trực giao (orthogonal matrix) $R$ và một số nửa xác định dương (positive semidefinite) ma trận đối xứng (symmetric matrix) $S$ sao cho
$$A = RS.$$
Điều này là dễ để chỉ ra và ta sẽ chứng minh nó ở dưới. Hơn nữa, $R, S$ là duy nhất nếu $A$ là khả nghịch, nhưng điều này là khó hơn để chứng minh; xem Bài toán 22.9. Ví dụ, ma trận
$$A = \frac{1}{2} \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & -1 & -1 \\ 1 & -1 & 1 & -1 \\ 1 & 1 & 1 & 1 \end{pmatrix}$$
$$--$$
Là cả hai trực giao và đối xứng, và $A = RS$ với $R = A$ và $S =$ I, mà suy ra rằng một số của các trị riêng (eigenvalues) của $A$ là âm.
Nhận xét: Trong phức trường hợp, phân rã cực (polar decomposition) phát biểu rằng với mọi phức $n \times  n$ ma trận $A$, tồn tại một ma trận unita (unitary matrix) $U$ và một số nửa xác định dương (positive semidefinite) Ma trận Hermite (Hermitian matrix) $H$ sao cho
$$A = UH.$$
Nó là dễ đến đi từ dạng cực (polar form) đến SVD, và ngược lại. Cho trước SVD $A = V D U^{\top}$, cho $R = V U^{\top}$ và $S = UD U^{\top}$. Rõ ràng là $R$ là trực giao và rằng $S$ là nửa xác định dương (positive semidefinite) đối xứng, và
$$RS = V U^{\top} UD U^{\top} = V D U^{\top} = A.$$

> **Ví dụ 22.5.** Nhắc lại từ Ví dụ 22.4 rằng $A = V DU^{\top}$ ở đâu $V = I_{2}$ và
$$11!$$
$$\overline{\sqrt}\overline{\sqrt}$$
$$A = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} ,U =\overline{\sqrt} 1\overline{2}-_{2}^{\sqrt21},D = \begin{pmatrix} \sqrt \\ \overline{2} & 0 \\ 0 & 0 \end{pmatrix} .$$
$$\overline{2}$$
Tập hợp $R = V U^{\top} = U$ và
$$11!$$
$$\overline{\sqrt}\overline{\sqrt}$$
$$S = UDU^{\top} =\overline{2}\overline{2}.$$
$$\overline{\sqrt} 1\overline{\sqrt} 1$$
$$\overline{2}\overline{2}$$
$$\sqrt$$
Vì $S =_{2}^{\sqrt1}A^{\top}A, S$ có các trị riêng (eigenvalues) $\overline{2}$ và $0$. Ta để lại nó đến độc giả để kiểm tra rằng $A = RS$.

<!-- PAGE 758 -->
Đi khác cách, cho trước phân rã cực (polar decomposition) $A = R_{1}S$, ở đâu $R_{1}$ là trực giao và $S$ là nửa xác định dương (positive semidefinite) đối xứng, có một ma trận trực giao (orthogonal matrix) $R_{2}$ và nửa xác định dương (positive semidefinite) ma trận đường chéo (diagonal matrix) $D$ sao cho $S = R_{2}D R_{2}^{\top}$, và do đó
$$A = R_{1}R_{2}D R_{2}^{\top} = V D U^{\top},$$
Ở đâu $V = R_{1}R_{2}$ và $U = R_{2}$ là trực giao.
$$Example 22.6. Let A = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} and A = R_{1}S, where R_{1} = \begin{pmatrix} \sqrt & \sqrt \\ 1/\sqrt{2} & 1/\sqrt{2} \\ 1/ & 2 & -1/ & 2 \end{pmatrix} and S =$$
$$\begin{pmatrix} \sqrt & \sqrt \\ 1/\sqrt{2} & 1/\sqrt{2} \\ 1/ & 2 & 1/ & 2 \end{pmatrix} . This is the polar decomposition of Example 22.5. Observe that$$
$$11! 11!$$
$$\overline{\sqrt}\overline{\sqrt}\overline{\sqrt}\overline{\sqrt}$$
$$S =\overline{\sqrt} 1\overline{2}-_{2}^{\sqrt21} \begin{pmatrix} \sqrt \\ \overline{2} & 0 \\ 0 & 0 \end{pmatrix} \overline{\sqrt} 1\overline{2}-_{2}^{\sqrt21}= R_{2}DR_{2}^{\top} .$$
$$\overline{2}\overline{2}$$
$$Set U = R_{2} and V = R_{1}R_{2} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} to obtain the SVD decomposition of Example 22.4.$$
Các trị riêng (eigenvalues) và các giá trị kỳ dị (singular values) của ma trận là typically không related trong bất kỳ hiển nhiên cách. Ví dụ, ma trận cỡ $n \times  n$
$$A = \begin{pmatrix} 1 & 2 & 0 & 0 & \dots & 0 & 0 \\ 0 & 1 & 2 & 0 & \dots & 0 & 0 \\ 0 & 0 & 1 & 2 & \dots & 0 & 0 \\ \vdots & \vdots & \ddots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & \dots & 0 & 1 & 2 & 0 \\ 0 & 0 & \dots & 0 & 0 & 1 & 2 \\ 0 & 0 & \dots & 0 & 0 & 0 & 1 \end{pmatrix}$$
Có trị riêng (eigenvalue) $1$ với bội (multiplicity) $n$, nhưng của nó các giá trị kỳ dị (singular values), $\sigma_{1}  \ge \cdots  \ge \sigma_{n}$, mà là dương square các nghiệm của các trị riêng (eigenvalues) của ma trận $B = A^{\top}A$ với
$$B = \begin{pmatrix} 1 & 2 & 0 & 0 & \dots & 0 & 0 \\ 2 & 5 & 2 & 0 & \dots & 0 & 0 \\ 0 & 2 & 5 & 2 & \dots & 0 & 0 \\ \vdots & \vdots & \ddots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & \dots & 2 & 5 & 2 & 0 \\ 0 & 0 & \dots & 0 & 2 & 5 & 2 \\ 0 & 0 & \dots & 0 & 0 & 2 & 5 \end{pmatrix}$$
Có wide spread, vì
$$\frac{\sigma_{1}}{\sigma_{n}} = cond_{2}(A) \ge 2^{n-1}.$$
