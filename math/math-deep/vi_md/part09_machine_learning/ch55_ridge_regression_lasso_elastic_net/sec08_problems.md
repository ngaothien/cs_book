# Các bài tập


<!-- PAGE 2104 -->
Ta có được quan sát rằng lasso dường như đến hội tụ nhiều faster hơn mạng đàn hồi (elastic net) khi $K < 10^{-3}$. Ví dụ, chạy ở trên dữ liệu tập hợp với $K = 10^{-3}$ và $\tau  =$ 0.999 đòi hỏi $140520$ các bước đến đạt được gốc (primal) và đối ngẫu (dual) các phần dư ít hơn $10^{-7}$, nhưng lasso chỉ lấy $86$ các bước đến đạt được cùng bậc của sự hội tụ. Ta được quan sát rằng lớn hơn $K$ là faster là sự hội tụ. Điều này có thể là attributed đến sự kiện rằng ma trận $P$ trở thành nhiều hơn/thêm “xác định dương (positive definite).” Một cái khác nhân tử là rằng ADMM cho lasso giải $n \times  n$ hệ phương trình tuyến tính, nhưng ADMM cho mạng đàn hồi (elastic net) giải 2(n $+ m) \times$ 2(n $+ m)$ hệ phương trình tuyến tính. Do đó chẵn/ngay cả dù mạng đàn hồi (elastic net) thực hiện không suffer từ một số của undesirable các tính chất của hồi quy Ridge (ridge regression) và lasso, nó xuất hiện đến có slower sự hội tụ tốc độ, thực ra nhiều slower khi $K$ là nhỏ (nói $K < 10^{-3})$. Nó cũng xuất hiện rằng mạng đàn hồi (elastic net) có thể là cũng expensive lựa chọn nếu $m$ là nhiều lớn hơn hơn $n$. Further investigations là cần thiết đến gain tốt hơn understanding của sự hội tụ vấn đề.

## 55.7 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ Hồi quy Ridge (ridge regression). $\bullet$ Hạt nhân (kernel) hồi quy Ridge (ridge regression). $\bullet$ Hạt nhân (kernel) các hàm. $\bullet$ Lasso hồi quy. $\bullet$ Mạng đàn hồi (elastic net) hồi quy.

## 55.8 Các bài tập

Bài toán 55.1. Kiểm tra công thức
$$(X^{\top}X + KI_{n})^{-1}X^{\top}= X^{\top}(XX^{\top}+ KI_{m})^{-1},$$
Được phát biểu trong Mục 55.1.
Bài toán 55.2. Cài đặt hồi quy Ridge (ridge regression) phương pháp được mô tả trong Mục 55.1 trong Matlab. Cũng cài đặt hồi quy Ridge (ridge regression) với intercept và compare việc giải Bài toán quy hoạch (DRR3) và Bài toán quy hoạch (RR6') bằng cách sử dụng được tâm dữ liệu.
Bài toán 55.3. Cài đặt hồi quy Ridge (ridge regression) với intercept phương pháp (RR3b) trong Matlab và compare nó với việc giải (RR6') bằng cách sử dụng được tâm dữ liệu.
$$Problem 55.4. Verify \frac{that}{X.} (lasso3) is equivalent to (lasso2) applied to the centered data$$
$y = y$ - $\overline{y} 1$ và $X = X$ - $b  b$
Bài toán 55.5. Kiểm chứng fomulae thu được cho hạt nhân (kernel) hồi quy Ridge (ridge regression) bài toán quy hoạch (KRR6').

<!-- PAGE 2105 -->
Bài toán 55.6. Cài đặt trong Matlab và test (lasso3) cho khác nhau các giá trị của $\rho$ và $\tau$. Viết bài toán quy hoạch đến plot các tọa độ của $w$ như hàm của $\tau$. Compare behavior của lasso với hồi quy Ridge (ridge regression) (RR6'), (RR3b) $(b$ có phạt), và với bình phương tối thiểu (least squares).
Bài toán 55.7. Kiểm tra chi tiết của derivation của đối ngẫu (dual) của mạng đàn hồi (elastic net).
Bài toán 55.8. Viết Matlab bài toán quy hoạch, việc giải đối ngẫu (dual) của mạng đàn hồi (elastic net); sử dụng inspiration từ Mục 56.3. Chạy tests đến compare behavior của hồi quy Ridge (ridge regression), lasso, và mạng đàn hồi (elastic net).
Bài toán 55.9. Chứng minh rằng mạng đàn hồi (elastic net) phương pháp có duy nhất điểm cực tiểu hóa.
Bài toán 55.10. Chứng minh rằng ma trận
$$P = \begin{pmatrix} I_{n} & -I_{n} & -X^{\top} & X^{\top} \\ -I_{n} & I_{n} & X^{\top} & -X^{\top} \\ -X & X & XX^{\top}+ KI_{m} & -XX^{\top}-KI_{m} \\ X & X & XX^{\top} & KI_{m} & XX^{\top}+ KI_{m} \end{pmatrix}$$
$$---$$
Là hầu như xác định dương (positive definite), trong nghĩa rằng
$$\begin{pmatrix} \beta_{+}^{\top} & \beta_{-}^{\top} & \mu_{+}^{\top} & \mu_{-}^{\top} \end{pmatrix} P \begin{pmatrix} \beta_{+} \\ \beta_{-} \\ \mu_{+} \\ \mu_{-} \end{pmatrix} = 0$$
Khi và chỉ khi $\beta_{+}  = \beta_{-}$ và $\mu_{+}  = \mu_{-}$, nghĩa là, $\beta  = 0$ và $\mu  = 0$.

<!-- PAGE 2106 -->
