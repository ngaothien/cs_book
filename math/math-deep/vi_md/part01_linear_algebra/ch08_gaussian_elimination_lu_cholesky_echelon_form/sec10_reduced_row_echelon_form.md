# Dạng bậc thang rút gọn theo hàng (RREF)


<!-- PAGE 301 -->
Các trị riêng (các trị riêng (eigenvalues)) của nó phải là dương. Ta sẽ có đến learn về định lý phổ (spectral theorem) cho các ma trận đối xứng để thiết lập điều này tiêu chuẩn (xem Mệnh đề 22.3). Mệnh đề 8.11 cũng nghiệm đúng cho phức Hermite xác định dương (positive definite) các ma trận, ở đâu trong $(d)$, nhân tử hóa $LDL^{\top}$ được thay thế bởi $LDL^{*}$. Cho nhiều hơn/thêm trên tính ổn định giải tích/phân tích và efficient implementation các phương pháp của Phép khử Gauss (Gaussian elimination), LU-factoring và Cholesky nhân tử, xem Demmel $[48]$, Trefethen và Bau $[182]$, Ciarlet $[41]$, Golub và Van Loan $[83]$, Meyer $[129]$, Strang $[175, 176]$, và Kincaid và Cheney $[105]$.

## 8.10 Dạng bậc thang rút gọn theo hàng (RREF) (RREF)

Phép khử Gauss (Gaussian elimination) được mô tả trong Mục 8.2 có thể cũng là ứng dụng đến rectangular các ma trận. Điều này cho ta phương pháp cho xác định liệu hệ Ax $= b$ là giải được và description của tất cả các nghiệm khi hệ là giải được, với mọi rectangular $m \times  n$ ma trận $A$. Hóa ra là thảo luận là đơn giản hơn nếu ta rescale tất cả các phần tử trụ là $1$, và cho điều này ta cần thứ ba loại của sơ cấp ma trận. Với mọi $\lambda  \neq  0$, cho $E_{i,\lambda}$ là $n\times n$ ma trận đường chéo (diagonal matrix)
$$E_{i,\lambda} = \begin{pmatrix} 1 \\ \ddots \\ 1 \\ \lambda \\ 1 \\ \ddots \\ 1 \end{pmatrix} ,$$
Với $(E_{i,\lambda})_{ii} = \lambda  (1 \le i \le n)$. Lưu ý rằng $E_{i,\lambda}$ là cũng cho trước bởi
$$E_{i,\lambda} = I + (\lambda  -1)e_{i i},$$
Và rằng $E_{i,\lambda}$ là khả nghịch với
$$E_{i,\lambda}^{-1} = E_{i,\lambda-1}.$$
Bây giờ sau $k$ - $1$ phép khử các bước, nếu đáy/dưới portion
$$(a_{kk}^{(k)} , a_{k+1k}^{(k)}, \dots  , a_{mk}^{(k)})$$
Của cột thứ $k$ của current ma trận $A_{k}$ là khác không sao cho phần tử trụ (pivot) $\pi_{k}$ có thể được được chọn, sau hoán vị của các hàng nếu cần, ta cũng chia hàng $k$ bởi $\pi_{k}$ để thu được phần tử trụ (pivot) $1$, và không chỉ thực hiện ta không tất cả các phần tử (entries) $i = k + 1, \dots  , m$ trong cột $k$, nhưng cũng tất cả các phần tử (entries) $i = 1, \dots  , k$ - $1$, sao cho chỉ khác không phần tử (entry) trong cột $k$ là $1$ trong hàng $k$. Các phần tử này hàng các phép toán là đạt được bởi phép nhân trên trái bởi sơ cấp các ma trận. Nếu $a_{kk}^{(k)} = a_{k+1k}^{(k)} = \cdots  = a_{mk}^{(k)} = 0$, ta di chuyển trên đến cột $k + 1$.

<!-- PAGE 302 -->
Khi cột thứ $k$ chứa phần tử trụ (pivot), thứ $k$ giai đoạn của quy trình cho chuyển đổi ma trận đến rref bao gồm của sau đây ba các bước được minh họa ở dưới:
$$\begin{pmatrix} 1 & \times & 0 & \times & \times & \times & \times \\ 0 & 0 & 1 & \times & \times & \times & \times \\ 0 & 0 & 0 & \times & \times & \times & \times \\ 0 & 0 & 0 & \times & \times & \times & \times \\ 0 & 0 & 0 & a_{ik}^{(k)} & \times & \times & \times \\ 0 & 0 & 0 \end{pmatrix} pivot=\Rightarrow \begin{pmatrix} 1 & \times & 0 & \times & \times & \times & \times \\ 0 & 0 & 1 & \times & \times & \times & \times \\ 0 & 0 & 0 & a_{ik}^{(k)} & \times & \times & \times \\ 0 & 0 & 0 & \times & \times & \times & \times \\ 0 & 0 & 0 & \times & \times & \times & \times \\ 0 & 0 & 0 \end{pmatrix} rescale=\Rightarrow$$
$$\times \times \times \times \times \times \times \times$$
$$\begin{pmatrix} 1 & \times & 0 & \times & \times & \times & \times \\ 0 & 0 & 1 & \times & \times & \times & \times \\ 0 & 0 & 0 & 1 & \times & \times & \times \\ 0 & 0 & 0 & \times & \times & \times & \times \\ 0 & 0 & 0 & \times & \times & \times & \times \\ 0 & 0 & 0 \end{pmatrix} elim=\Rightarrow \begin{pmatrix} 1 & \times & 0 & 0 & \times & \times & \times \\ 0 & 0 & 1 & 0 & \times & \times & \times \\ 0 & 0 & 0 & 1 & \times & \times & \times \\ 0 & 0 & 0 & 0 & \times & \times & \times \\ 0 & 0 & 0 & 0 & \times & \times & \times \\ 0 & 0 & 0 & 0 & \times & \times & \times \end{pmatrix} .$$
$$\times \times \times \times$$
Nếu cột thứ $k$ thực hiện không chứa phần tử trụ (pivot), ta đơn giản di chuyển trên đến tiếp theo cột. kết quả là rằng sau performing như vậy phép khử các bước, ta thu được ma trận rằng có đặc biệt hình dạng đã biết như rút gọn hàng bậc thang ma trận, cho ngắn rref. Đây là một ví dụ minh họa điều này process: Bắt đầu từ ma trận
$$A_{1} = \begin{pmatrix} 1 & 0 & 2 & 1 & 5 \\ 1 & 1 & 5 & 2 & 7 \\ 1 & 2 & 8 & 4 & 12 \end{pmatrix} ,$$
Ta perform sau đây các bước
$$A_{1} \longrightarrow A_{2} = \begin{pmatrix} 1 & 0 & 2 & 1 & 5 \\ 0 & 1 & 3 & 1 & 2 \\ 0 & 2 & 6 & 3 & 7 \end{pmatrix} ,$$
Bằng cách trừ hàng $1$ từ hàng $2$ và hàng $3$;
$$A_{2} \longrightarrow \begin{pmatrix} 1 & 0 & 2 & 1 & 5 \\ 0 & 2 & 6 & 3 & 7 \\ 0 & 1 & 3 & 1 & 2 \end{pmatrix} \longrightarrow \begin{pmatrix} 1 & 0 & 2 & 1 & 5 \\ 0 & 1 & 3 & 3/2 & 7/2 \\ 0 & 1 & 3 & 1 & 2 \end{pmatrix} \longrightarrow A_{3} = \begin{pmatrix} 1 & 0 & 2 & 1 & 5 \\ 0 & 1 & 3 & 3/2 & 7/2 \\ 0 & 0 & 0 & 1/2 & 3/2 \end{pmatrix} ,$$
$$--$$
Sau chọn phần tử trụ (pivot) $2$ và hoán vị hàng $2$ và hàng $3$, chia hàng $2$ bởi $2$, và trừ hàng $2$ từ hàng $3$;
$$A_{3} \longrightarrow \begin{pmatrix} 1 & 0 & 2 & 1 & 5 \\ 0 & 1 & 3 & 3/2 & 7/2 \\ 0 & 0 & 0 & 1 & 3 \end{pmatrix} \longrightarrow A_{4} = \begin{pmatrix} 1 & 0 & 2 & 0 & 2 \\ 0 & 1 & 3 & 0 & -1 \\ 0 & 0 & 0 & 1 & 3 \end{pmatrix} ,$$

<!-- PAGE 303 -->
Sau chia hàng $3$ bởi $-1/2$, trừ hàng $3$ từ hàng $1$, và trừ $(3/2) \times$ hàng $3$ từ hàng $2$. Rõ ràng là các cột $1, 2$ và $4$ là độc lập tuyến tính (linearly independent), rằng cột $3$ là tổ hợp tuyến tính (linear combination) của các cột $1$ và $2$, và rằng cột $5$ là tổ hợp tuyến tính (linear combination) của các cột $1, 2, 4$. Nói chung, dãy của các bước dẫn đầu đến rút gọn bậc thang ma trận là không duy nhất. Ví dụ, ta có thể có được chọn $1$ thay vì của $2$ như thứ hai phần tử trụ (pivot) trong ma trận $A_{2}$. Tuy nhiên, rút gọn hàng bậc thang ma trận thu được từ bất kỳ cho trước ma trận là unique; nghĩa là, nó không phụ thuộc vào dãy của các bước rằng là theo sau during reduction process. sự kiện này là không do đó dễ để chứng minh một cách chặt chẽ, nhưng ta sẽ thực hiện nó sau này. Nếu ta muốn để giải hệ phương trình tuyến tính của các phương trình của tạo thành Ax $= b$, ta áp dụng các phép biến đổi sơ cấp trên hàng đến cả hai ma trận $A$ và vế phải $b$. Đến thực hiện điều này một cách thuận tiện, ta tạo thành ma trận mở rộng (augmented matrix) $(A, b)$, mà là ma trận cỡ $m \times  (n + 1)$ thu được bằng cách cộng $b$ như extra cột đến ma trận $A$. Ví dụ nếu
$$A = \begin{pmatrix} 1 & 0 & 2 & 1 \\ 1 & 1 & 5 & 2 \\ 1 & 2 & 8 & 4 \end{pmatrix} andb = \begin{pmatrix} 5 \\ 7 \\ 12 \end{pmatrix} ,$$
Thì ma trận mở rộng (augmented matrix) là
$$(A, b) = \begin{pmatrix} 1 & 0 & 2 & 1 & 5 \\ 1 & 1 & 5 & 2 & 7 \\ 1 & 2 & 8 & 4 & 12 \end{pmatrix} .$$
Bây giờ với mọi ma trận $M$, vì
$$M(A, b) = (MA, Mb),$$
Performing các phép biến đổi sơ cấp trên hàng trên $(A, b)$ là tương đương đến simultaneously performing các phép toán trên cả hai $A$ và $b$. Ví dụ, xét hệ
$$x_{1}+2x_{3}+x_{4}=5$$
$$x_{1}+x_{2}+5x_{3}+2x_{4}=7$$
$$x_{1}+2x_{2}+8x_{3}+4x_{4}=12.$$
Của nó ma trận mở rộng (augmented matrix) là ma trận
$$(A, b) = \begin{pmatrix} 1 & 0 & 2 & 1 & 5 \\ 1 & 1 & 5 & 2 & 7 \\ 1 & 2 & 8 & 4 & 12 \end{pmatrix}$$
Được xét ở trên, do đó reduction các bước ứng dụng đến ma trận này cho hệ
$$x_{1}+2x_{3}=2$$
$$x_{2}+3x_{3}=-1$$
$$x_{4}=3.$$

<!-- PAGE 304 -->
Điều này rút gọn hệ có cùng tập hợp của các nghiệm như ban đầu, và hiển nhiên $x_{3}$ có thể được được chọn arbitrarily. Vì vậy, hệ của chúng ta có một cách vô hạn nhiều các nghiệm cho trước bởi
$$x_{1} = 2 -2x_{3},x_{2} = -1 -3x_{3},x_{4} = 3,$$
Ở đâu $x_{3}$ là tùy ý. sau đây mệnh đề chỉ ra rằng tập hợp của các nghiệm của hệ Ax $= b$ được bảo toàn bởi bất kỳ dãy của hàng các phép toán.

> **Mệnh đề 8.12.** Cho trước bất kỳ ma trận cỡ $m \times  n$ $A$ và bất kỳ vectơ $b \in \mathbb{R}^{m}$, với mọi dãy của các phép biến đổi sơ cấp trên hàng $E_{1}, \dots  , E_{k}$, nếu $P = E_{k} \cdots  E_{1}$ và (', b') $=$ P(, $b)$, thì các nghiệm của Ax $= b$ là cùng như các nghiệm của 'x $=$ b'.

*Chứng minh.* Vì mỗi sơ cấp hàng phép toán $E_{i}$ là khả nghịch, do đó là $P$, và vì (', b') $=$ P(, $b)$, thì ' $= PA$ và b' $=$ Pb. Nếu $x$ là nghiệm của ban đầu hệ Ax $= b$, thì nhân cả hai các vế/cạnh bởi $P$ ta thu được PAx $=$ Pb; nghĩa là, 'x $=$ b', do đó $x$ là nghiệm của mới hệ. Ngược lại, giả sử rằng $x$ là nghiệm của mới hệ, nghĩa là 'x $=$ b'. Thì bởi vì ' $= PA$, b' $=$ Pb, và $P$ là khả nghịch, ta thu được
$$Ax = P^{-1}A'x = P^{-1}b'= b,$$
Do đó $x$ là nghiệm của ban đầu hệ Ax $= b$. Một cái khác quan trọng sự kiện là điều này:

> **Mệnh đề 8.13.** Cho trước một ma trận cỡ $m\times n$ $A$, với mọi dãy của hàng các phép toán $E_{1}, \dots  , E_{k}$, nếu $P = E_{k} \cdots  E_{1}$ và $B = PA$, thì các không gian con được sinh (spanned) bởi các hàng của $A$ và các hàng của $B$ là đồng nhất. Vì vậy, $A$ và $B$ có cùng hàng hạng (rank). Hơn nữa, các ma trận $A$ và $B$ cũng có cùng (cột) hạng (rank).

*Chứng minh.* Vì $B = PA$, từ trước đó nhận xét, các hàng của $B$ là các tổ hợp tuyến tính của các hàng của $A$, do đó sinh (span) của các hàng của $B$ là không gian con của sinh (span) của các hàng của $A$. Vì $P$ là khả nghịch, $A = P^{-1} B$, do đó bởi cùng lập luận sinh (span) của các hàng của $A$ là không gian con của sinh (span) của các hàng của $B$. Vì vậy, các không gian con được sinh (spanned) bởi các hàng của $A$ và các hàng của $B$ là đồng nhất, mà suy ra rằng $A$ và $B$ có cùng hàng hạng (rank). Mệnh đề 8.12 suy ra rằng các hệ Ax $= 0$ và Bx $= 0$ có cùng các nghiệm. Vì Ax là các tổ hợp tuyến tính của các cột của $A$ và Bx là các tổ hợp tuyến tính của các cột của $B$, cực đại số của các cột độc lập tuyến tính trong $A$ bằng cực đại số của các cột độc lập tuyến tính trong $B$; nghĩa là, $A$ và $B$ có cùng hạng (rank).
Nhận xét: các không gian con được sinh (spanned) bởi các cột của $A$ và $B$ có thể được khác nhau! Tuy nhiên, số chiều của chúng phải là cùng. Ta sẽ chỉ ra trong Mục 8.14 rằng hàng hạng (rank) bằng cột hạng (rank). Điều này sẽ cũng được chứng minh trong Mệnh đề 11.15 Cho chúng ta bây giờ định nghĩa một cách chính xác những gì là rút gọn hàng bậc thang ma trận.

<!-- PAGE 305 -->

> **Định nghĩa 8.6.** một ma trận cỡ $m \times  n$ $A$ là rút gọn hàng bậc thang ma trận khi và chỉ khi sau đây các điều kiện đúng:
() thứ nhất khác không phần tử (entry) trong mọi hàng là $1$. Điều này phần tử (entry) được gọi là một phần tử trụ (pivot).
$(b)$ thứ nhất khác không phần tử (entry) của hàng $i + 1$ là đến phải của thứ nhất khác không phần tử (entry) của hàng $i$.
$(c)$ các phần tử (entries) ở trên phần tử trụ (pivot) là không. Nếu ma trận thỏa mãn ở trên các điều kiện, ta cũng nói rằng nó là trong dạng bậc thang rút gọn theo hàng (RREF), cho ngắn rref. Lưu ý rằng Điều kiện $(b)$ suy ra rằng các phần tử (entries) ở dưới phần tử trụ (pivot) là cũng không. Ví dụ, ma trận
$$A = \begin{pmatrix} 1 & 6 & 0 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$
Là rút gọn hàng bậc thang ma trận. Nói chung, ma trận trong rref có sau đây hình dạng:
$$\begin{pmatrix} 1 & 0 & 0 & \times & \times & 0 & 0 & \times \\ 0 & 1 & 0 & \times & \times & 0 & 0 & \times \\ 0 & 0 & 1 & \times & \times & 0 & 0 & \times \\ 0 & 0 & 0 & 0 & 0 & 1 & 0 & \times \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & \times \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \end{pmatrix}$$
Nếu hàng cuối cùng bao gồm của các không điểm, hoặc
$$\begin{pmatrix} 1 & 0 & 0 & \times & \times & 0 & 0 & \times & 0 & \times \\ 0 & 1 & 0 & \times & \times & 0 & 0 & \times & 0 & \times \\ 0 & 0 & 1 & \times & \times & 0 & 0 & \times & 0 & \times \\ 0 & 0 & 0 & 0 & 0 & 1 & 0 & \times & 0 & \times \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & \times & \times & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \end{pmatrix}$$
$$\times$$
Nếu hàng cuối cùng chứa phần tử trụ (pivot). sau đây mệnh đề chỉ ra rằng mọi ma trận có thể được được chuyển đổi đến dạng bậc thang rút gọn theo hàng (RREF) bằng cách sử dụng hàng các phép toán.

> **Mệnh đề 8.14.** Cho trước bất kỳ ma trận cỡ $m \times  n$ $A$, có một dãy của hàng các phép toán $E_{1}, \dots  , E_{k}$ sao cho nếu $P = E_{k} \cdots  E_{1}$, thì $U = PA$ là rút gọn hàng bậc thang ma trận.

<!-- PAGE 306 -->

*Chứng minh.* Ta tiến hành bằng quy nạp theo $m$. Nếu $m = 1$, thì hoặc tất cả các phần tử (entries) trên điều này hàng là không, do đó $A = 0$, hoặc nếu $a_{j}$ là thứ nhất khác không phần tử (entry) trong $A$, cho $P = (a_{j}^{-1}$) (một ma trận cỡ $1 \times  1$); rõ ràng, PA là rút gọn hàng bậc thang ma trận. Bây giờ ta giả sử rằng $m \ge 2$. Nếu $A = 0$, ta được thực hiện, do đó ta giả sử rằng $A \neq  0$. Vì $A \neq  0$, có một leftmost cột $j$ mà là khác không, do đó chọn bất kỳ phần tử trụ (pivot) $\pi  = a_{ij}$ trong cột thứ $j$, hoán vị hàng $i$ và hàng $1$ nếu cần, nhân mới hàng thứ nhất bởi $\pi^{-1}$, và rõ ràng ra khác các phần tử (entries) trong cột $j$ bằng cách trừ phù hợp các bội của hàng $1$. Tại kết thúc/cuối của điều này process, ta có ma trận $A_{1}$ rằng có sau đây hình dạng:
$$A_{1} = \begin{pmatrix} 0 & \cdots & 0 & 1 & * & \cdots & * \\ 0 & \cdots & 0 & 0 & * & \cdots & * \\ \vdots & \vdots & \vdots & \vdots & \vdots \\ 0 & \cdots & 0 & 0 & * & \cdots & * \end{pmatrix} ,$$
Ở đâu * stands cho tùy ý vô hướng (scalar), hoặc nhiều hơn/thêm ngắn gọn
$$A_{1} = \begin{pmatrix} 0 & 1 & B \\ 0 & 0 & D \end{pmatrix} ,$$
Ở đâu $D$ là $(m$ - $1) \times  (n$ - $j)$ ma trận (và $B$ là $1 \times  n$ - $j$ ma trận). Nếu $j = n$, ta được thực hiện. Ngược lại, theo giả thiết quy nạp ứng dụng đến $D$, có một dãy của hàng các phép toán rằng các chuyển đổi $D$ đến rút gọn hàng bậc thang ma trận R', và các phần tử này hàng các phép toán thực hiện không affect hàng thứ nhất của $A_{1}$, mà có nghĩa là $A_{1}$ là rút gọn đến ma trận của tạo thành
$$R = \begin{pmatrix} 0 & 1 & B \\ 0 & 0 & R' \end{pmatrix} .$$
Bởi vì R' là rút gọn hàng bậc thang ma trận, ma trận $R$ thỏa mãn Các điều kiện () và $(b)$ của dạng bậc thang rút gọn theo hàng (RREF). Cuối cùng, các phần tử (entries) ở trên tất cả các phần tử trụ trong R' có thể được được rõ ràng ra bằng cách trừ phù hợp các bội của các hàng của R' chứa phần tử trụ (pivot). thu được ma trận cũng thỏa mãn Điều kiện $(c)$, và quy nạp bước là đầy đủ.
Nhận xét: Có một Matlab hàm named rref rằng các chuyển đổi bất kỳ ma trận đến của nó dạng bậc thang rút gọn theo hàng (RREF). Nếu $A$ là bất kỳ ma trận và nếu $R$ là dạng bậc thang rút gọn theo hàng (RREF) của $A$, phần thứ hai của Mệnh đề 8.13 có thể được sharpened little, vì cấu trúc của rút gọn hàng bậc thang ma trận làm cho nó rõ ràng rằng hạng (hạng (rank)) của nó bằng số của các phần tử trụ.

> **Mệnh đề 8.15.** hạng (rank) của ma trận $A$ bằng số của các phần tử trụ trong của nó rref $R$.
