# Ky Fan Các chuẩn và Schatten Các chuẩn


<!-- PAGE 763 -->
Có thể cũng được sử dụng để xác định hạng (rank) của ma trận khi khác các phương pháp chẳng hạn như Phép khử Gauss (Gaussian elimination) produce rất nhỏ các phần tử trụ. Một của chính các ứng dụng của SVD là phép tính của nghịch đảo giả (pseudo-inverse). Pseudo-inverses là then chốt đến nghiệm của khác nhau tối ưu hóa các bài tập, đặc biệt phương pháp của bình phương tối thiểu (least squares). Điều này topic được thảo luận trong chương tiếp theo (Chương $23)$. Các ứng dụng của material của điều này chương có thể được tìm thấy trong Strang $[176, 175]$; Ciarlet $[41]$; Golub và Van Loan $[83]$, mà chứa nhiều khác references; Demmel $[48]$; và Trefethen và Bau $[182]$.

## 22.5 Ky Fan Các chuẩn và Schatten Các chuẩn

Các giá trị kỳ dị (singular values) của ma trận có thể được được sử dụng để định nghĩa khác nhau các chuẩn trên các ma trận mà có tìm thấy recent các ứng dụng trong quantum information lý thuyết và trong spectral đồ thị lý thuyết. Sau đây Horn và Johnson $[99]$ (Mục 3.4) ta có thể tạo sau đây các định nghĩa:

> **Định nghĩa 22.5.** Với mọi ma trận $A \in M_{m,n}(\mathbb{C})$, cho $q = min{m, n}$, và nếu $\sigma_{1}  \ge \cdots  \ge \sigma_{q}$ là các giá trị kỳ dị (singular values) của $A$, với mọi $k$ với $1 \le k \le q$, cho
$$N_{k}(A) = \sigma_{1}  + \cdots  + \sigma_{k} ,$$
Được gọi là Ky Fan k-norm của $A$. Tổng quát hơn, với mọi $p \ge 1$ và bất kỳ $k$ với $1 \le k \le q$, cho
$$N_{k;p}(A) = (\sigma_{1}^{p}  + \cdots  + \sigma_{k}^{p} )^{1/p},$$
Được gọi là Ky Fan p-k-norm của $A$. Khi $k = q, N_{q;p}$ cũng được gọi là Schatten p-norm. Nhận thấy rằng khi $k = 1, N_{1}(A) = \sigma_{1}$, và Ky Fan chuẩn (norm) $N_{1}$ là đơn giản spectral chuẩn (norm) từ Chương $9$, mà là chuẩn ma trận phụ thuộc (subordinate matrix norm) liên kết với Euclidean chuẩn (norm). Khi $k = q$, Ky Fan chuẩn (norm) $N_{q}$ được cho bởi
$$N_{q}(A) = \sigma_{1}  + \cdots  + \sigma_{q}  = \mathrm{tr}((A^{*}A)^{1/2})$$
Và được gọi là vết (trace) chuẩn (norm) hoặc nuclear chuẩn (norm). Khi $p = 2$ và $k = q$, Ky Fan $N_{q;2}$ chuẩn (norm) được cho bởi
$$p$$
$$N_{k;2}(A) = (\sigma_{1}^{2}  + \cdots  + \sigma_{q}^{2} )^{1/2}=\overline{\mathrm{tr}(}\overline{A}^{*}\overline{A}\overline{) =} \|A\|_{F} ,$$
Mà là Chuẩn Frobenius (Frobenius norm) của $A$. Nó có thể được được hiển thị rằng $N_{k}$ và $N_{k;p}$ là unitarily bất biến các chuẩn, và rằng khi $m = n$, chúng là các chuẩn ma trận; xem Horn và Johnson $[99]$ (Mục 3.4, Hệ quả 3.4.4 và Bài toán $3)$.
