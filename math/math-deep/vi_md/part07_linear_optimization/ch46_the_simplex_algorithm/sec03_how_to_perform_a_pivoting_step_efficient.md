# Cách mà đến Perform Chọn phần tử trụ Bước Efficiently


<!-- PAGE 1621 -->
Ngược lại, $w^{*} = 0$, và $u^{*}$ là nghiệm chấp nhận được (feasible solution) của (P2). Vì $(u^{*}, 0_{m})$ là cơ bản nghiệm chấp nhận được (feasible solution) của $(P)$ các cột tương ứng với khác không các thành phần của $u^{*}$ là một cách tuyến tính
$$b$$
Độc lập. Một số của các tọa độ của $u^{*}$ có thể là bằng $0$, nhưng vì $A$ có hạng (rank) $m$ ta có thể cộng các cột của $A$ để thu được cơ sở (basis) $K^{*}$ liên kết với $u^{*}$, và $u^{*}$ là thật vậy cơ bản nghiệm chấp nhận được (feasible solution) của (P2). Chạy thuật toán đơn hình (simplex algorithm) trên Bài toán quy hoạch tuyến tính (linear program) $P$ để thu được ban đầu chấp nhận được (feasible)
$$b$$
Nghiệm $(u_{0}, K_{0})$ của bài toán quy hoạch tuyến tính (linear program) (P2) được gọi là Phase I của thuật toán đơn hình (simplex algorithm). Chạy thuật toán đơn hình (simplex algorithm) trên Bài toán quy hoạch tuyến tính (linear program) (P2) với một số ban đầu nghiệm chấp nhận được (feasible solution) $(u_{0}, K_{0})$ được gọi là Phase II của thuật toán đơn hình (simplex algorithm). Nếu nghiệm chấp nhận được (feasible solution) của Bài toán quy hoạch tuyến tính (linear program) (P2) là readily available thì Phase I là skipped. Đôi khi, tại kết thúc/cuối của Phase I, nghiệm tối ưu (optimal solution) của (P2) là đã thu được. Trong tóm tắt, ta được chứng minh sau đây sự kiện worth recording.

> **Mệnh đề 46.1.** Với mọi Bài toán quy hoạch tuyến tính (linear program) (P2)
$$maximizecx$$
$$subject toAx = b and x \ge 0,$$
Trong tiêu chuẩn tạo thành, ở đâu $A$ là một ma trận cỡ $m \times  n$ của hạng (rank) $m$ và $b \ge 0$, xét Bài toán quy hoạch tuyến tính (linear program) $(P)$ trong tiêu chuẩn tạo thành
$$b$$
$$maximize-(x_{n+1} + \cdots  + x_{n+m})$$
$$subject toAx = b andx \ge 0.$$
$$b b b$$
Thuật toán đơn hình (simplex algorithm) với phần tử trụ (pivot) quy tắc rằng ngăn cản cycling được bắt đầu trên cơ bản nghiệm chấp nhận được (feasible solution) $x = (0_{n}, b)$ của $(P)$ kết thúc với nghiệm tối ưu (optimal solution) $(u^{*}, w^{*})$.
$$b b$$
$(1)$ Nếu $w^{*} \neq  0$, thì $\mathcal{P}(A, b) = \emptyset$, nghĩa là, Bài toán quy hoạch tuyến tính (linear program) (P2) có không có nghiệm chấp nhận được (feasible solution).
$(2)$ Nếu $w^{*} = 0$, thì $\mathcal{P}(A, b) \neq  \emptyset$, và $u^{*}$ là cơ bản nghiệm chấp nhận được (feasible solution) của (P2) liên kết với một số cơ sở (basis) $K$. Mệnh đề 46.1 chỉ ra rằng xác định liệu đa diện $\mathcal{P}(A, b)$ được định nghĩa bởi hệ của các phương trình Ax $= b$ và các bất đẳng thức $x \ge 0$ là khác rỗng là decidable. Điều này decision quy trình sử dụng fail-safe phiên bản của thuật toán đơn hình (simplex algorithm) (rằng ngăn cản cycling), và chứng minh rằng nó luôn luôn kết thúc và trả về câu trả lời là không tầm thường.

## 46.3 Cách mà đến Perform Chọn phần tử trụ Bước Efficiently

Ta bây giờ thảo luận ngắn gọn cách mà đến perform phép tính của $(u^{+}, K^{+})$ từ cơ bản nghiệm chấp nhận được (feasible solution) $(u, K)$. Trong thứ tự để tránh áp dụng hoán vị các ma trận nó được ưu tiên hơn đến cho phép cơ sở (basis) $K$ là dãy của các chỉ số, có thể ra của thứ tự. Do đó, cho bất kỳ ma trận cỡ $m \times  n$ $A$ (với $m \le n)$

<!-- PAGE 1622 -->
Và bất kỳ dãy $K = (k_{1}, k_{2}, \cdots  , k_{m})$ của $m$ các phần tử với $k_{i} \in {1, \dots  , n}$, ma trận $A_{K}$ ký hiệu ma trận cỡ $m \times  m$ có cột thứ $i$ là $k_{i}th$ cột của $A$, và tương tự với mọi
$$\mathbb{R}^{n} \mathbb{R}^{n}\mathbb{R}^{m}$$
Vectơ $u \in$ (resp. bất kỳ dạng tuyến tính (linear form) $c \in$ ($)^{*})$, vectơ $u_{K} \in$ (dạng tuyến tính (linear form) $c_{K} \in (\mathbb{R}^{m})^{*})$ là vectơ có phần tử thứ $i$ là $k_{i}th$ phần tử (entry) trong $u$ (resp. tuyến tính có phần tử thứ $i$ là $k_{i}th$ phần tử (entry) trong $c)$. Với mỗi nonbasic $j \in / K$, ta có
$$A^{j}= \gamma_{k1}^{j} A^{k1}+ \cdots  + \gamma_{km}^{j} A^{km}= A_{K}\gamma_{K}^{j} ,$$
Do đó vectơ $\gamma_{K}^{j}$ được cho bởi $\gamma_{K}^{j}  = A_{K}^{-1} A^{j}$, nghĩa là, bởi việc giải hệ
$$A_{K}\gamma_{K}^{j}  = A^{j}.(*_{\gamma})$$
Là rất precise, vì vectơ $\gamma_{K}^{j}$ phụ thuộc vào $K$ các thành phần của nó nên được ký hiệu bởi $(\gamma_{K}^{j} )_{ki}$, nhưng như ta được nói trước, để đơn giản hóa ký hiệu ta viết $\gamma_{ki}^{j}$ thay vì của $(\gamma_{K}^{j} )_{ki}$. Trong thứ tự đến decide mà trường hợp áp dụng $((A)$, (B1), (B2), (B3)), ta cần để tính
$$numbers c_{j} - \sum_{k}  \in K \gamma_{k}^{j} c_{k} for all j \in /K. For this, observe that$$
$$c_{j} - \sum_{k\in K}  \gamma_{k}^{j} c_{k} = c_{j} -c_{K}\gamma_{K}^{j}  = c_{j} -c_{K}A_{K}^{-1} A^{j}.$$
Nếu ta viết $\beta_{K}  = c_{K}A_{K}^{-1}$, thì
$$c_{j} - \sum_{k\in K}  \gamma_{k}^{j} c_{k} = c_{j} -\beta_{K} A^{j},$$
$$\mathbb{R}^{m}$$
Và ta xem rằng $\beta_{K}^{\top}  \in$ là nghiệm của hệ $\beta_{K}^{\top}  = (A_{K}^{-1} )^{\top}c_{k}^{\top}$, mà có nghĩa là $\beta_{K}^{\top}$ là nghiệm của hệ
$$A_{K}^{\top}\beta_{K}^{\top}  = c_{K}^{\top}.(*_{\beta})$$
Nhận xét: Nhận thấy rằng vì $u$ là cơ sở (basis) nghiệm chấp nhận được (feasible solution) của $(P)$, ta có $u_{j} = 0$ với mọi $j \in / K$, do đó $u$ là nghiệm của phương trình $A_{K}u_{K} = b$. Hệ quả là, giá trị của hàm mục tiêu (objective function) cho $u$ là cu $= c_{K}u_{K} = c_{K}A_{K}^{-1} b$. sự kiện này sẽ đóng then chốt vai trò trong Mục 47.2 để chỉ ra rằng khi thuật toán đơn hình (simplex algorithm) kết thúc với nghiệm tối ưu (optimal solution) của Bài toán quy hoạch tuyến tính (linear program) $(P)$, thì nó cũng produces nghiệm tối ưu (optimal solution) của Đối ngẫu (dual) Bài toán quy hoạch tuyến tính (linear program) $(D)$. Giả sử rằng ta có cơ bản nghiệm chấp nhận được (feasible solution) $u$, cơ sở (basis) $K$ cho $u$, và rằng ta cũng có ma trận $A_{K}$ cũng vậy của nó nghịch đảo $A_{K}^{-1}$ (perhaps một cách ẩn) và cũng nghịch đảo $(A_{K}^{\top})^{-1}$ của $A_{K}^{\top}$ (perhaps một cách ẩn). Ở đây là description của vòng lặp bước của thuật toán đơn hình (simplex algorithm), sau đây hầu như chính xác Chvatal (Chvatal $[40]$, Chương $7$, Hình hộp 7.1). Vòng lặp Bước của (Revised) Đơn hình (simplex) Phương pháp

<!-- PAGE 1623 -->
$$Step 1. Compute the numbers c_{j} - \sum_{k}  \gamma_{k}^{j} c_{k} = c_{j} -\beta_{K} A^{j}for all j \in /K, and for this,$$
Tính $\beta_{K}^{\top}$ như nghiệm của $system^{\in K}$
$$A_{K}^{\top}\beta_{K}^{\top}  = c_{K}^{\top}.$$
Nếu $c_{j}$ - $\beta_{K} A^{j} \le 0$ với mọi $j \in / K$, dừng và trả về nghiệm tối ưu (optimal solution) $u$ (Trường hợp $(A))$. Bước $2$. Nếu Trường hợp $(B)$ phát sinh, sử dụng phần tử trụ (pivot) quy tắc để xác định mà chỉ số $j^{+} \in / K$ nên enter mới cơ sở (basis) $K^{+}$ (điều kiện $c_{j+}$ - $\beta_{K} A^{j+} > 0$ nên đúng). Bước $3$. Tính $max_{k\in K} \gamma_{k}^{j+}$. Cho điều này, giải hệ phương trình tuyến tính
$$A_{K}\gamma_{K}^{j+}  = A^{j+}.$$
Bước $4$. Nếu $max_{k\in K} \gamma_{k}^{j+} \le 0$, thì dừng và report rằng Bài toán quy hoạch tuyến tính (linear program) $(P)$ là không bị chặn (Trường hợp (B1)). Bước $5$. Nếu $max_{k\in K} \gamma_{k}^{j+} > 0$, sử dụng các tỉ số $u_{k}/\gamma_{k}^{j+}$ với mọi $k \in K$ sao cho $\gamma_{k}^{j+} > 0$ để tính $\theta^{j+}$, và sử dụng phần tử trụ (pivot) quy tắc để xác định mà chỉ số $k^{-} \in K$ sao cho $\theta^{j+} = u_{k-}/\gamma_{k-}^{j+}$ nên để lại $K$ (Trường hợp (B2)). Nếu $max_{k\in K} \gamma_{k}^{j+} = 0$, thì sử dụng phần tử trụ (pivot) quy tắc để xác định mà chỉ số $k^{-}$ cho mà $\gamma_{k-}^{j+} > 0$ nên để lại cơ sở (basis) $K$ (Trường hợp (B3)). Bước $6$. Update $u, K$, và $A_{K}$, đến $u^{+}$ và $K^{+}$, và $A_{K+}$. During bước này, cho trước cơ sở (basis) $K$ specified bởi dãy $K = (k_{1}, \dots  , k_{\ell}, \dots  , k_{m})$, với $k^{-} = k_{\ell}$, thì $K^{+}$ là dãy thu được bằng cách thay thế $k_{\ell}$ bởi incoming chỉ số $j^{+}$, do đó $K^{+} = (k_{1}, \dots  , j^{+}, \dots  , k_{m})$ với $j^{+}$ trong $\ell$ th slot. vectơ $u$ là dễ dàng updated. để tính $A_{K+}$ từ $A_{K}$ ta lấy advantage của sự kiện rằng $A_{K}$ và $A_{K+}$ chỉ khác nhau bởi đơn lẻ cột, cụ thể là $\ell$ th cột $A^{j+}$, mà được cho bởi tổ hợp tuyến tính (linear combination)
$$A^{j+}= A_{K}\gamma_{K}^{j+}  .$$
Để đơn giản hóa ký hiệu, ký hiệu $\gamma_{K}^{j+}$ bởi $\gamma$, và nhắc lại rằng $k^{-} = k_{\ell}$. Nếu $K = (k_{1}, \dots  , k_{m})$, thì
$$\cdots \cdots$$
$A_{K} = [A^{k1}  A^{k-}  A^{im}]$, và vì $A_{K+}$ là kết quả của thay thế $\ell$ th cột $A^{k-}$ của $A_{K}$ bởi cột $A^{j+}$, ta có
$$A_{K+} = [A^{k1}\cdots  A^{j+}\cdots  A^{im}] = [A^{k1}\cdots  A_{K}\gamma  \cdots  A^{im}] = A_{K}E(\gamma ),$$
Ở đâu $E(\gamma$) là sau đây ma trận khả nghịch (invertible matrix) thu được từ ma trận đơn vị (identity matrix) $I_{m}$ bằng cách thay thế của nó $\ell$ th cột bởi $\gamma$:
$$E(\gamma ) = \begin{pmatrix} 1 & \gamma_{1} \\ \ddots & \vdots \\ 1 & \gamma_{\ell-1} \\ \gamma_{\ell} \\ \gamma_{\ell+1} & 1 \\ \vdots & \ddots \\ \gamma_{m} & 1 \end{pmatrix} .$$

<!-- PAGE 1624 -->
Vì $\gamma_{\ell} = \gamma_{k-}^{j+} > 0$, ma trận $E(\gamma$) là khả nghịch, và nó là dễ để kiểm tra rằng nghịch đảo của nó được cho bởi
$$E(\gamma )^{-1} = \begin{pmatrix} 1 & -\gamma_{\ell}^{-1} \gamma_{1} \\ \ddots & \vdots \\ 1 & -\gamma_{\ell}^{-1} \gamma_{\ell-1} \\ \gamma_{\ell}^{-1} \\ -\gamma_{\ell}^{-1} \gamma_{\ell+1} & 1 \\ \vdots & \ddots \\ \gamma_{\ell}^{-1} \gamma_{m} & 1 \end{pmatrix} ,$$
$$-$$
Mà là rất cheap để tính. Ta cũng có
$$A_{K+}^{-1} = E(\gamma )^{-1}A_{K}^{-1} .$$
Hệ quả là, nếu $A_{K}$ và $A_{K}^{-1}$ là available, thì $A_{K+}$ và $A_{K+}^{-1}$ có thể được được tính cheaply theo $A_{K}$ và $A_{K}^{-1}$ và các ma trận của tạo thành $E(\gamma$). Thì các hệ $(*_{\gamma})$ để tìm các vectơ $\gamma_{K}^{j}$ có thể được được giải cheaply. Vì
$$A_{K+}^{\top} = E(\gamma )^{\top}A_{K}^{\top}$$
Và
$$(A_{K+}^{\top})^{-1}= (A_{K}^{\top})^{-1}(E(\gamma )^{\top})^{-1},$$
$$can also be computed cheaply from$$
Các ma trận $A_{K+}^{\top}$ và $(A_{K+}^{\top})^{-1}  A_{K}^{\top}, (A_{K}^{\top})^{-1}$, và các ma trận của tạo thành $E(\gamma )^{\top}$. Do đó các hệ $(*_{\beta})$ để tìm các dạng tuyến tính $\beta_{K}$ có thể cũng được giải cheaply. ma trận của tạo thành $E(\gamma$) được gọi là một eta ma trận; xem Chvatal $[40]$ (Chương $7)$. Ta đã chỉ ra rằng ma trận $A_{Ks}$ thu được sau $s$ các bước của thuật toán đơn hình (simplex algorithm) có thể được viết dưới dạng
$$A_{Ks} = A_{Ks-1}E_{s}$$
Với một số eta ma trận $E_{s}$, do đó $A_{ks}$ có thể được viết dưới dạng tích
$$A_{Ks} = E_{1}E_{2} \cdots  E_{s}$$
Của $s$ eta các ma trận. Như vậy nhân tử hóa được gọi là một eta nhân tử hóa. eta nhân tử hóa có thể được sử dụng để hoặc nghịch đảo $A_{Ks}$ hoặc để giải hệ của tạo thành $A_{Ks}\gamma  = A^{j+}$ một cách lặp. Mà phương pháp là nhiều hơn/thêm efficient phụ thuộc vào sparsity của $E_{i}$. Trong tóm tắt, có cheap các phương pháp cho việc tìm tiếp theo cơ bản nghiệm chấp nhận được (feasible solution) $(u^{+}, K^{+})$ từ $(u, K)$. Ta đơn giản được muốn đến cho độc giả flavor của các phần tử này các kỹ thuật. Ta refer độc giả đến các văn bản trên quy hoạch tuyến tính (linear programming) cho chi tiết các trình bày của các phương pháp cho cài đặt efficiently đơn hình (simplex) phương pháp. Đặc biệt, revised đơn hình (simplex) phương pháp được trình bày trong Chvatal $[40]$, Papadimitriou và Steiglitz $[139]$, Bertsimas và Tsitsiklis $[21]$, và Vanderbei $[187]$.
