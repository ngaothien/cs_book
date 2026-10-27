# SPD Các ma trận và Các phần bù Schur


<!-- PAGE 1568 -->

## 43.2 Đối xứng xác định dương (SPD) Các ma trận và

$$Schur Complements$$
Nếu ta giả sử rằng của ta ma trận khối (block matrix) $M$ là đối xứng, sao cho $A, D$ là đối xứng và $C = B^{\top}$, thì ta xem theo Mệnh đề 43.1 rằng $M$ được biểu diễn như
$$M = \begin{pmatrix} A & B \\ B^{\top} & D \end{pmatrix} = \begin{pmatrix} I & BD^{-1} \\ 0 & I \end{pmatrix} \begin{pmatrix} A -BD^{-1}B^{\top} & 0 \\ 0 & D \end{pmatrix} \begin{pmatrix} I & BD^{-1\top} \\ 0 & I \end{pmatrix} ,$$
Mà chỉ ra rằng $M$ là đồng dạng đến khối ma trận đường chéo (diagonal matrix) (hiển nhiên, Phần bù Schur (Schur complement), $A$ - $BD^{-1}B^{\top}$, là đối xứng). Hệ quả là, ta có kết quả sau phiên bản của “Schur’s mẹo/kỹ thuật” để kiểm tra liệu $M$ ≻ $0$ cho ma trận đối xứng (symmetric matrix).

> **Mệnh đề 43.3.** Với mọi ma trận đối xứng (symmetric matrix) $M$ của tạo thành
$$M = \begin{pmatrix} A & B \\ B^{\top} & C \end{pmatrix} ,$$
Nếu $C$ là khả nghịch, thì các tính chất sau đây đúng:
$(1) M$ ≻ $0$ khi và chỉ khi $C$ ≻ $0$ và $A$ - $BC^{-1}B^{\top}$ ≻ $0$.
$(2)$ Nếu $C$ ≻ $0$, thì $M$ ⪰ $0$ khi và chỉ khi $A$ - $BC^{-1}B^{\top}$ ⪰ $0$.

*Chứng minh.* $(1)$ Vì $C$ là khả nghịch, ta có
$$M = \begin{pmatrix} A & B \\ B^{\top} & C \end{pmatrix} = \begin{pmatrix} I & BC^{-1} \\ 0 & I \end{pmatrix} \begin{pmatrix} A -BC^{-1}B^{\top} & 0 \\ 0 & C \end{pmatrix} \begin{pmatrix} I & BC^{-1\top} \\ 0 & I \end{pmatrix} .(*)$$
Nhận thấy rằng
$$\begin{pmatrix} I & BC^{-1-1} \\ 0 & I \end{pmatrix} = \begin{pmatrix} I & -BC^{-1} \\ 0 & I \end{pmatrix} ,$$
Do đó (*) cho ta
$$\begin{pmatrix} I & -BC^{-1} \\ 0 & I \end{pmatrix} \begin{pmatrix} A & B \\ B^{\top} & C \end{pmatrix} \begin{pmatrix} I & -BC^{-1\top} \\ 0 & I \end{pmatrix} = \begin{pmatrix} A -BC^{-1}B^{\top} & 0 \\ 0 & C \end{pmatrix} ,$$
Và ta biết rằng với mọi ma trận đối xứng (symmetric matrix) $T$, ở đây $T = M$, và bất kỳ ma trận khả nghịch (invertible matrix) $N$, ở đây
$$N = \begin{pmatrix} I & -BC^{-1} \\ 0 & I \end{pmatrix} ,$$
Ma trận $T$ là xác định dương (positive definite) $(T$ ≻ $0)$ khi và chỉ khi $NTN^{\top}$ (mà là hiển nhiên đối xứng) là xác định dương (positive definite) $(NTN^{\top}$ ≻ $0)$. Nhưng khối ma trận đường chéo (diagonal matrix) là xác định dương (positive definite) khi và chỉ khi mỗi đường chéo khối là xác định dương (positive definite), mà kết luận chứng minh.
$(2)$ Điều này là bởi vì với mọi ma trận đối xứng (symmetric matrix) $T$ và bất kỳ ma trận khả nghịch (invertible matrix) $N$, ta có $T$ ⪰ $0$ khi và chỉ khi $NTN^{\top}$ ⪰ $0$.
