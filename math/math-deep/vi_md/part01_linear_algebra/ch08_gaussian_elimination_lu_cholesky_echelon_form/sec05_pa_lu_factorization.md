# PA = LU Nhân tử hóa


<!-- PAGE 275 -->

## 8.5 PA = LU Nhân tử hóa

Sau đây dễ mệnh đề chỉ ra rằng, trong nguyên lý, $A$ có thể được premultiplied bởi một số hoán vị ma trận $P$, sao cho $PA$ có thể được được chuyển đổi đến tam giác trên (upper-triangular) tạo thành mà không có bằng cách sử dụng bất kỳ chọn phần tử trụ. Các hoán vị được thảo luận trong một số chi tiết trong Mục 30.3, nhưng cho bây giờ ta chỉ cần định nghĩa này. Cho precise connection giữa khái niệm của hoán vị (như được thảo luận trong Mục 30.3) và hoán vị các ma trận, xem Bài toán 8.16.

> **Định nghĩa 8.3.** hoán vị ma trận là ma trận vuông (square matrix) rằng có đơn lẻ $1$ trong mọi hàng và mọi cột và các không điểm ở mọi nơi khác. Nó được hiển thị trong Mục 30.3 rằng mọi hoán vị ma trận là tích của phép chuyển vị các ma trận (P(i, k)s), và rằng $P$ là khả nghịch với nghịch đảo $P^{\top}$.

> **Mệnh đề 8.4.** Cho $A$ là khả nghịch ma trận cỡ $n \times n$. Tồn tại một hoán vị ma trận $P$ sao cho (PA)(1: $k, 1$: $k)$ là khả nghịch cho $k = 1, \dots  , n$.

*Chứng minh.* trường hợp $n = 1$ là tầm thường, và do đó là trường hợp $n = 2$ (ta swap các hàng nếu cần). Nếu $n \ge 3$, ta tiến hành bởi quy nạp. Vì $A$ là khả nghịch, các cột của nó là độc lập tuyến tính (linearly independent); đặc biệt, của nó thứ nhất $n -1$ các cột là cũng độc lập tuyến tính (linearly independent). Xóa cột cuối cùng của $A$. Vì còn lại $n -1$ các cột là độc lập tuyến tính (linearly independent), có cũng $n -1$ các hàng độc lập tuyến tính trong tương ứng $n \times  (n$ - $1)$ ma trận. Do đó, có một hoán vị của các phần tử này $n$ các hàng sao cho $(n$ - $1) \times  (n$ - $1)$ ma trận bao gồm của thứ nhất $n$ - $1$ các hàng là khả nghịch. Nhưng khi đó có một tương ứng hoán vị ma trận $P_{1}$, sao cho thứ nhất $n$ - $1$ các hàng và các cột của $P_{1}A$ tạo thành ma trận khả nghịch (invertible matrix) '. Áp dụng giả thiết quy nạp (induction hypothesis) đến $(n$ - $1) \times  (n$ - $1)$ ma trận ', ta xem rằng ở đó một số hoán vị ma trận $P_{2}$ (để lại hàng thứ $n$ cố định), sao cho $(P_{2}P_{1}A)(1$: $k, 1$: $k)$ là khả nghịch, cho $k = 1, \dots  , n$ - $1$. Vì $A$ là khả nghịch trong thứ nhất place và $P_{1}$ và $P_{2}$ là khả nghịch, $P_{1}P_{2}A$ là cũng khả nghịch, và ta được thực hiện.
Nhận xét: Một có thể cũng chứng minh Mệnh đề 8.4 bằng cách sử dụng clever reordering của Phép khử Gauss (Gaussian elimination) các bước suggested bởi Trefethen và Bau $[182]$ (Lecture $21)$. Thật vậy, ta biết rằng nếu $A$ là khả nghịch, thì có hoán vị các ma trận $P_{i}$ và các tích của sơ cấp các ma trận $E_{i}$, sao cho
$$A_{n} = E_{n-1}P_{n-1} \cdots  E_{2}P_{2}E_{1}P_{1}A,$$
Ở đâu $U = A_{n}$ là tam giác trên (upper-triangular). Ví dụ, khi $n = 4$, ta có $E_{3}P_{3}E_{2}P_{2}E_{1}P_{1}A = U$. Ta có thể định nghĩa mới các ma trận $E_{1}', E_{2}', E_{3}'$ mà là vẫn các tích của sơ cấp các ma trận sao cho ta có
$$E_{3}'E_{2}'E_{1}'P_{3}P_{2}P_{1}A = U.$$
Thật vậy, nếu ta cho $E_{3}' = E_{3}, E_{2}' = P_{3}E_{2}P_{3}^{-1}$, và $E_{1}' = P_{3}P_{2}E_{1}P_{2}^{-1} P_{3}^{-1}$, ta dễ dàng kiểm chứng rằng mỗi $E_{k}'$ là tích của sơ cấp các ma trận và rằng
$$E_{3}'E_{2}'E_{1}'P_{3}P_{2}P_{1} = E_{3}(P_{3}E_{2}P_{3}^{-1} )(P_{3}P_{2}E_{1}P_{2}^{-1} P_{3}^{-1} )P_{3}P_{2}P_{1} = E_{3}P_{3}E_{2}P_{2}E_{1}P_{1}.$$

<!-- PAGE 276 -->
Nó có thể cũng được chứng minh rằng $E_{1}', E_{2}', E_{3}'$ là tam giác dưới (lower triangular) (xem Định lý 8.5). Nói chung, ta cho
$$E_{k}' = P_{n-1} \cdots  P_{k+1}E_{k}P_{k+1}^{-1} \cdots  P_{n-1}^{-1},$$
Và ta có
$$E_{n-1}' \cdots  E_{1}'P_{n-1} \cdots  P_{1}A = U,$$
Ở đâu mỗi $E_{j}'$ là tam giác dưới (lower triangular) ma trận (xem Định lý 8.5). Nó là đáng chú ý rằng nếu chọn phần tử trụ các bước là cần during Phép khử Gauss (Gaussian elimination), rất đơn giản modification của thuật toán cho việc tìm Nhân tử hóa LU (LU-factorization) cho ta các ma trận $L, U$, và $P$, sao cho $PA = LU$. Đến mô tả điều này mới phương pháp, vì đường chéo các phần tử (entries) của $L$ là 1s, nó là thuận tiện đến viết
$$L = I + \Lambda .$$
Thì trong assembling ma trận $\Lambda$ trong khi performing Phép khử Gauss (Gaussian elimination) với chọn phần tử trụ, ta tạo cùng phép chuyển vị trên các hàng của $\Lambda$ (một cách thực $\Lambda_{k-1}$) rằng ta tạo trên các hàng của $A$ (một cách thực $A_{k})$ during chọn phần tử trụ bước liên quan đến hàng $k$ và hàng $i$. Ta cũng assemble $P$ bởi bắt đầu với ma trận đơn vị (identity matrix) và áp dụng đến $P$ cùng hàng các phép chuyển vị rằng ta áp dụng đến $A$ và $\Lambda$. Đây là một ví dụ minh họa phương pháp này.

> **Ví dụ 8.3.** Cho trước
$$A = A_{1} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 1 & -1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & 0 & 1 \end{pmatrix} ,$$
$$--$$
Ta có kết quả sau dãy của các bước: Ta initialize $\Lambda_{0}  = 0$ và $P_{0} = I_{4}$. thứ nhất phần tử trụ (pivot) là $\pi_{1}  = 1$ trong hàng $1$, và ta trừ hàng $1$ từ các hàng $2, 3$, và $4$. Ta thu được
$$A_{2} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & 0 & -2 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 2 & 1 & 1 \end{pmatrix} \Lambda_{1}  = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix} P_{1} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$---$$
Tiếp theo phần tử trụ (pivot) là $\pi_{2}  = -2$ trong hàng $3$, do đó ta hoán vị hàng $2$ và $3$; ta cũng áp dụng điều này hoán vị đến $\Lambda$ và $P$:
$$A_{3}' = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 2 & 1 & 1 \end{pmatrix} \Lambda_{2}'  = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix} P_{2} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$---$$
Tiếp theo ta trừ hàng $2$ từ hàng $4$ (và cộng $0$ lần hàng $2$ đến hàng $3)$. Ta thu được
$$A_{3} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix} \Lambda_{2}  = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \end{pmatrix} P_{2} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$-$$

<!-- PAGE 277 -->
Tiếp theo phần tử trụ (pivot) là $\pi_{3}  = -2$ trong hàng $3$, và vì thứ tư phần tử (entry) trong cột $3$ là đã không, ta cộng $0$ lần hàng $3$ đến hàng $4$. Ta thu được
$$A_{4} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix} \Lambda_{3}  = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \end{pmatrix} P_{3} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$-$$
Quy trình được hoàn tất, và ta có
$$L = \Lambda_{3}  + I = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix} U = A_{4} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix} P = P_{3} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$-$$
Nó là dễ để kiểm tra rằng thật vậy
$$LU = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & -2 & -1 & 1 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & -1 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix}$$
$$---$$
Và
$$PA = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 1 & -1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & -1 & 0 & 1 \\ 1 & 1 & -1 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix} .$$
$$----$$
Bằng cách sử dụng ý tưởng trong nhận xét trước ở trên ví dụ, ta có thể chứng minh định lý ở dưới mà chỉ ra tính đúng đắn của thuật toán cho việc tính toán $P, L$ và $U$ bằng cách sử dụng đơn giản sự điều chỉnh của Phép khử Gauss (Gaussian elimination). Ta là không biết của chi tiết chứng minh của Định lý 8.5 trong tiêu chuẩn các văn bản. Mặc dù Golub và Van Loan $[83]$ phát biểu phiên bản của định lý này như của chúng Định lý 3.1.4, chúng nói rằng “ chứng minh là phức tạp đánh chỉ số dưới lập luận.” Meyer $[129]$ cũng cung cấp phác thảo của chứng minh (xem kết thúc/cuối của Mục 3.10). Xét theo tình huống này, ta đưa ra đầy đủ chứng minh. Nó thực hiện liên quan đến nhiều các chỉ số dưới và các chỉ số trên, nhưng theo ý kiến của chúng tôi, nó chứa một số các kỹ thuật rằng vượt xa biến đổi ký hiệu.

> **Định lý 8.5.** Với mọi khả nghịch ma trận cỡ $n \times n$ $A$, sau đây đúng:
$(1)$ Tồn tại một hoán vị ma trận $P$, một số tam giác trên (upper-triangular) ma trận $U$, và một số unit tam giác dưới (lower-triangular) ma trận $L$, sao cho $PA = LU$ (nhắc lại, $L_{i i} = 1$ cho $i = 1, \dots  , n)$. Hơn nữa, nếu $P =$ I, thì $L$ và $U$ là duy nhất và chúng là produced kết quả là của Phép khử Gauss (Gaussian elimination) mà không có chọn phần tử trụ.

<!-- PAGE 278 -->
$(2)$ Nếu $E_{n-1} \dots  E_{1}A = U$ là kết quả của Phép khử Gauss (Gaussian elimination) mà không có chọn phần tử trụ, viết như thông thường $A_{k} = E_{k-1} \dots  E_{1}A$ (với $A_{k} = (a_{ij}^{(k)}$)), và cho $\ell_{ik}  = a_{ik}^{(k)} /a_{kk}^{(k)}$, với $1 \le k \le n -1$ và $k + 1 \le i \le n$. Thì
$$L = \begin{pmatrix} 1 & 0 & 0 & \cdots & 0 \\ \ell_{21} & 1 & 0 & \cdots & 0 \\ \ell_{31} & \ell_{32} & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots \\ 0 \\ \ell_{n1} & \ell_{n2} & \ell_{n3} & \cdots & 1 \end{pmatrix} ,$$
Ở đâu cột thứ $k$ của $L$ là cột thứ $k$ của $E_{k}^{-1}$, cho $k = 1, \dots  , n$ - $1$.
$(3)$ Nếu $E_{n-1}P_{n-1} \cdots  E_{1}P_{1}A = U$ là kết quả của Phép khử Gauss (Gaussian elimination) với một số chọn phần tử trụ, viết $A_{k} = E_{k-1}P_{k-1} \cdots  E_{1}P_{1}A$, và định nghĩa $E_{j}^{k}$, với $1 \le j \le n -1$ và $j \le k \le n -1$, sao cho, cho $j = 1, \dots  , n$ - $2$,
$$E_{j}^{j} = E_{j}$$
$$E_{j}^{k} = P_{k}E_{j}^{k-1}P_{k},for k = j + 1, \dots  , n -1,$$
Và
$$E_{n-1}^{n-1} = E_{n-1}.$$
Thì,
$$E_{j}^{k} = P_{k}P_{k-1} \cdots  P_{j+1}E_{j}P_{j+1} \cdots  P_{k-1}P_{k}$$
$$U = E_{n-1}^{n-1} \cdots  E_{1}^{n-1}P_{n-1} \cdots  P_{1}A,$$
Và nếu ta tập hợp
$$P = P_{n-1} \cdots  P_{1}$$
$$L = (E_{1}^{n-1})^{-1}\cdots  (E_{n-1}^{n-1})^{-1},$$
Thì
$$PA = LU.(\dagger_{1} )$$
Hơn nữa,
$$(E_{j}^{k} )^{-1}= I +\mathcal{E}_{j}^{k} ,1 \le j \le n -1, j \le k \le n -1,$$
Ở đâu $\mathcal{E}_{j}^{k}$ là tam giác dưới (lower triangular) ma trận của tạo thành
$$\mathcal{E}_{j}^{k} = \begin{pmatrix} 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & \ddots & \vdots & \vdots & \vdots & \vdots \\ 0 & \cdots & 0 & 0 & \cdots & 0 \\ 0 & \cdots & \ell_{j+1j}^{(k)} & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & \ell_{nj}^{(k)} & 0 & 0 \end{pmatrix} ,$$
$$\cdots \cdots$$

<!-- PAGE 279 -->
Ta có
$$E_{j}^{k} = I -E_{j}^{k} ,$$
Và
$$\mathcal{E}_{j}^{k} = P_{k}\mathcal{E}_{j}^{k-1},1 \le j \le n -2, j + 1 \le k \le n -1,$$
Ở đâu $P_{k} =$ I hoặc khác $P_{k} =$ P(k, $i)$ với một số $i$ sao cho $k + 1 \le i \le n$; nếu $P_{k} \neq$ I, điều này có nghĩa là $(E_{j}^{k} )^{-1}$ là thu được từ $(E_{j}^{k-1})^{-1}$ bởi hoán vị các phần tử (entries) trên các hàng $i$ và $k$ trong cột $j$. Bởi vì các ma trận $(E_{j}^{k} )^{-1}$ là tất cả tam giác dưới (lower triangular), ma trận $L$ là cũng tam giác dưới (lower triangular). Trong thứ tự để tìm $L$, định nghĩa tam giác dưới (lower triangular) $n \times  n$ các ma trận $\Lambda_{k}$ của tạo thành
$$\Lambda_{k}  = \begin{pmatrix} 0 & 0 & 0 & 0 & 0 & \cdots & \cdots & 0 \\ \vdots & \vdots \\ \lambda_{21}^{(k)} & 0 & 0 & 0 & 0 & 0 \\ \ddots & \vdots & \vdots \\ \lambda_{31}^{(k)} & \lambda_{32}^{(k)} & 0 & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ 0 & 0 \\ \lambda_{k+11}^{(k)} & \lambda_{k+12}^{(k)} & \cdots & \lambda_{k+1k}^{(k)} & 0 & \cdots & \cdots & 0 \\ \lambda_{k+21}^{(k)} & \lambda_{k+22}^{(k)} & \cdots & \lambda_{k+2k}^{(k)} & 0 & \ddots & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \ddots & \vdots \\ \lambda_{n1}^{(k)} & \lambda_{n2}^{(k)} & \lambda_{nk}^{(k)} & 0 & 0 \end{pmatrix}$$
$$\cdots \cdots \cdots$$
Đến assemble các cột của $L$ một cách lặp như sau: cho
$$(-\ell_{k+1k}^{(k)} , \dots  , -\ell_{nk}^{(k)}  )$$
Là cuối cùng n-k các phần tử của cột thứ $k$ của $E_{k}$, và định nghĩa $\Lambda_{k}$ một cách quy nạp bằng cách đặt
$$\Lambda_{1}  = \begin{pmatrix} 0 & 0 & \cdots & 0 \\ \ell_{21}^{(1)} & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ \ell_{n1}^{(1)} & 0 & 0 \end{pmatrix} ,$$
$$\cdots$$
Thì cho $k = 2, \dots  , n$ - $1$, định nghĩa
$$\Lambda_{k}'  = P_{k}\Lambda_{k-1} ,(\dagger_{2} )$$

<!-- PAGE 280 -->
Và
$$\Lambda_{k}  = (I + \Lambda_{k}' )E_{k}^{-1}-I = \begin{pmatrix} 0 & 0 & 0 & 0 & 0 & \cdots & \cdots & 0 \\ \vdots & \vdots \\ \lambda_{21}^{'(k-1)} & 0 & 0 & 0 & 0 & 0 \\ \ddots & \vdots & \vdots \\ \lambda_{31}^{'(k-1)} & \lambda_{32}^{'(k-1)} & 0 & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ 0 & 0 \\ \lambda_{k1}^{'(k-1)} & \lambda_{k2}^{'(k-1)} & \cdots & \lambda_{k(k-1)}^{'(k-1)} & 0 & \cdots & \cdots & 0 \\ \lambda_{k+11}^{'(k-1)} & \lambda_{k+12}^{'(k-1)} & \cdots & \lambda_{k+1 (-1)}^{'(k-1)} & \ell_{k+1k}^{(k)} & \ddots & \cdots & 0 \\ \vdots & \vdots & \ddots & \ddots & \vdots & \vdots & \ddots & \vdots \\ \lambda_{n1}^{'(k-1)} & \lambda_{n2}^{'(k-1)} & \lambda_{n k-1}^{'(k-1)} & \ell_{nk}^{(k)} & 0 \end{pmatrix} ,$$
$$\cdots \cdots \cdots$$
Với $P_{k} =$ I hoặc $P_{k} =$ P(k, $i)$ với một số $i > k$. Điều này có nghĩa là trong assembling $L$, hàng $k$ và hàng $i$ của $\Lambda_{k-1}$ cần là permuted khi chọn phần tử trụ bước hoán vị hàng $k$ và hàng $i$ của $A_{k}$ là cần thiết. Thì
$$\cdots$$
$$I + \Lambda_{k}  = (E_{1}^{k})^{-1} (E_{k}^{k})^{-1}$$
$$\Lambda_{k}  =\mathcal{E}_{1}^{k} + \cdots  +\mathcal{E}_{k}^{k},$$
Cho $k = 1, \dots  , n$ - $1$, và vì vậy
$$L = I + \Lambda_{n-1} .$$
Chứng minh của Định lý 8.5, mà là rất technical, là cho trước trong Mục 8.6. Ta emphasize một lần nữa rằng Phần $(3)$ của Định lý 8.5 chỉ ra đáng chú ý sự kiện rằng trong assembling ma trận $L$ trong khi performing Phép khử Gauss (Gaussian elimination) với chọn phần tử trụ, chỉ thay đổi đến thuật toán là để tạo cùng phép chuyển vị trên các hàng của $\Lambda_{k-1}$ rằng ta tạo trên các hàng của $A$ (một cách thực $A_{k})$ during chọn phần tử trụ bước liên quan đến hàng $k$ và hàng $i$. Ta có thể cũng assemble $P$ bởi bắt đầu với ma trận đơn vị (identity matrix) và áp dụng đến $P$ cùng hàng các phép chuyển vị rằng ta áp dụng đến $A$ và $\Lambda$. Đây là một ví dụ minh họa phương pháp này.

> **Ví dụ 8.4.** Xét ma trận
$$A = \begin{pmatrix} 1 & 2 & -3 & 4 \\ 4 & 8 & 12 & -8 \\ 2 & 3 & 2 & 1 \\ 3 & 1 & 1 & 4 \end{pmatrix} .$$
$$---$$
Ta tập hợp $P_{0} = I_{4}$, và ta có thể cũng tập hợp $\Lambda_{0}  = 0$. bước thứ nhất là đến hoán vị hàng $1$ và hàng $2$, bằng cách sử dụng phần tử trụ (pivot) $4$. Ta cũng áp dụng điều này hoán vị đến $P_{0}$:
$$A_{1}' = \begin{pmatrix} 4 & 8 & 12 & -8 \\ 1 & 2 & -3 & 4 \\ 2 & 3 & 2 & 1 \\ 3 & 1 & 1 & 4 \end{pmatrix} P_{1} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$---$$

<!-- PAGE 281 -->
Tiếp theo ta trừ $1/4$ lần hàng $1$ từ hàng $2, 1/2$ lần hàng $1$ từ hàng $3$, và cộng $3/4$ lần hàng $1$ đến hàng $4$, và bắt đầu assembling $\Lambda$:
$$A_{2} = \begin{pmatrix} 4 & 8 & 12 & -8 \\ 0 & 0 & -6 & 6 \\ 0 & -1 & -4 & 5 \\ 0 & 5 & 10 & 10 \end{pmatrix} \Lambda_{1}  = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 1/4 & 0 & 0 & 0 \\ 1/2 & 0 & 0 & 0 \\ 3/4 & 0 & 0 & 0 \end{pmatrix} P_{1} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$--$$
Tiếp theo ta hoán vị hàng $2$ và hàng $4$, bằng cách sử dụng phần tử trụ (pivot) $5$. Ta cũng áp dụng điều này hoán vị đến $\Lambda$ và $P$:
$$A_{3}' = \begin{pmatrix} 4 & 8 & 12 & -8 \\ 0 & 5 & 10 & -10 \\ 0 & -1 & -4 & 5 \\ 0 & 0 & 6 & 6 \end{pmatrix} \Lambda_{2}'  = \begin{pmatrix} 0 & 0 & 0 & 0 \\ -3/4 & 0 & 0 & 0 \\ 1/2 & 0 & 0 & 0 \\ 1/4 & 0 & 0 & 0 \end{pmatrix} P_{2} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix} .$$
$$-$$
Tiếp theo ta cộng $1/5$ lần hàng $2$ đến hàng $3$, và update $\Lambda_{2}'$:
$$A_{3} = \begin{pmatrix} 4 & 8 & 12 & -8 \\ 0 & 5 & 10 & -10 \\ 0 & 0 & -2 & 3 \\ 0 & 0 & 6 & 6 \end{pmatrix} \Lambda_{2}  = \begin{pmatrix} 0 & 0 & 0 & 0 \\ -3/4 & 0 & 0 & 0 \\ 1/2 & -1/5 & 0 & 0 \\ 1/4 & 0 & 0 & 0 \end{pmatrix} P_{2} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix} .$$
$$-$$
Tiếp theo ta hoán vị hàng $3$ và hàng $4$, bằng cách sử dụng phần tử trụ (pivot) $-6$. Ta cũng áp dụng điều này hoán vị đến $\Lambda$ và $P$:
$$A_{4}' = \begin{pmatrix} 4 & 8 & 12 & -8 \\ 0 & 5 & 10 & -10 \\ 0 & 0 & -6 & 6 \\ 0 & 0 & 2 & 3 \end{pmatrix} \Lambda_{3}'  = \begin{pmatrix} 0 & 0 & 0 & 0 \\ -3/4 & 0 & 0 & 0 \\ 1/4 & 0 & 0 & 0 \\ 1/2 & 1/5 & 0 & 0 \end{pmatrix} P_{3} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{pmatrix} .$$
$$--$$
Cuối cùng ta trừ $1/3$ lần hàng $3$ từ hàng $4$, và update $\Lambda_{3}'$:
$$A_{4} = \begin{pmatrix} 4 & 8 & 12 & -8 \\ 0 & 5 & 10 & -10 \\ 0 & 0 & -6 & 6 \\ 0 & 0 & 0 & 1 \end{pmatrix} \Lambda_{3}  = \begin{pmatrix} 0 & 0 & 0 & 0 \\ -3/4 & 0 & 0 & 0 \\ 1/4 & 0 & 0 & 0 \\ 1/2 & 1/5 & 1/3 & 0 \end{pmatrix} P_{3} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{pmatrix} .$$
$$-$$
Hệ quả là, cộng đồng nhất thức đến $\Lambda_{3}$, ta thu được
$$L = \begin{pmatrix} 1 & 0 & 0 & 0 \\ -3/4 & 1 & 0 & 0 \\ 1/4 & 0 & 1 & 0 \\ 1/2 & 1/5 & 1/3 & 1 \end{pmatrix} ,U = \begin{pmatrix} 4 & 8 & 12 & -8 \\ 0 & 5 & 10 & -10 \\ 0 & 0 & -6 & 6 \\ 0 & 0 & 0 & 1 \end{pmatrix} ,P = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{pmatrix} .$$
$$-$$

<!-- PAGE 282 -->
Ta kiểm tra rằng
$$PA = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 2 & -3 & 4 \\ 4 & 8 & 12 & -8 \\ 2 & 3 & 2 & 1 \\ 3 & 1 & 1 & 4 \end{pmatrix} = \begin{pmatrix} 4 & 8 & 12 & -8 \\ -3 & -1 & 1 & -4 \\ 1 & 2 & -3 & 4 \\ 2 & 3 & 2 & 1 \end{pmatrix} ,$$
$$---$$
Và rằng
$$LU = \begin{pmatrix} 1 & 0 & 0 & 0 \\ -3/4 & 1 & 0 & 0 \\ 1/4 & 0 & 1 & 0 \\ 1/2 & 1/5 & 1/3 & 1 \end{pmatrix} \begin{pmatrix} 4 & 8 & 12 & -8 \\ 0 & 5 & 10 & -10 \\ 0 & 0 & -6 & 6 \\ 0 & 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 4 & 8 & 12 & -8 \\ -3 & -1 & 1 & -4 \\ 1 & 2 & -3 & 4 \\ 2 & 3 & 2 & 1 \end{pmatrix} = PA.$$
$$-$$
Lưu ý rằng nếu một sẽ đến overwrite tam giác dưới (lower triangular) phần của evolving ma trận $A$, một có thể store evolving $\Lambda$ ở đó, vì các phần tử (các phần tử (entries)) này sẽ eventually là không anyway! Ở đó là cũng không có cần đến save một cách tường minh hoán vị ma trận $P$. Một có thể thay vì record hoán vị các bước trong extra cột (record vectơ $(\pi (1), \dots  , \pi (n))$ tương ứng với hoán vị $\pi$ ứng dụng đến các hàng). Ta cho độc giả viết như vậy bold và spaceefficient phiên bản của Phân rã LU (LU-decomposition)!
Nhận xét: Trong Matlab hàm lu trả về các ma trận $P, L, U$ liên quan trong $PA = LU$ nhân tử hóa bằng cách sử dụng gọi $[L, U, P] =$ lu(). Như hệ quả của Định lý 8.5(1), ta có thể chỉ ra kết quả sau đây.

> **Mệnh đề 8.6.** Nếu khả nghịch thực ma trận đối xứng (symmetric matrix) $A$ có Phân rã LU (LU-decomposition), thì $A$ có nhân tử hóa của tạo thành
$$A = LDL^{\top},$$
Ở đâu $L$ là tam giác dưới (lower-triangular) ma trận có đường chéo các phần tử (entries) bằng $1$, và ở đâu $D$ bao gồm của các phần tử trụ. Hơn nữa, như vậy phân rã là duy nhất.

*Chứng minh.* Nếu $A$ có Nhân tử hóa LU (LU-factorization), thì nó có LDU nhân tử hóa
$$A = LDU,$$
Ở đâu $L$ là tam giác dưới (lower-triangular), $U$ là tam giác trên (upper-triangular), và đường chéo các phần tử (entries) của cả hai $L$ và $U$ bằng $1$. Vì $A$ là đối xứng, ta có
$$LDU = A = A^{\top}= U^{\top} DL^{\top},$$
Với $U^{\top}$ tam giác dưới (lower-triangular) và $DL^{\top}$ tam giác trên (upper-triangular). Bởi tính duy nhất của Nhân tử hóa LU (LU-factorization) (Phần $(1)$ của Định lý 8.5), ta phải có $L = U^{\top}$ (và $DU = DL^{\top})$, do đó $U = L^{\top}$, như đã khẳng định.
Nhận xét: Nó có thể được được hiển thị rằng Phép khử Gauss (Gaussian elimination) cộng back-substitution đòi hỏi $n^{3}/3+ O(n^{2})$ các phép cộng, $n^{3}/3 + O(n^{2})$ các phép nhân và $n^{2}/2 +$ O(n) các phép chia.
