# Tính duy nhất của RREF


<!-- PAGE 310 -->

## 8.12 Tính duy nhất của RREF Tạo thành

Cho sake của tính đầy đủ, ta chứng minh rằng dạng bậc thang rút gọn theo hàng (RREF) của ma trận là duy nhất. neat chứng minh cho trước ở dưới là borrowed và được điều chỉnh từ $W$. Kahan.

> **Mệnh đề 8.19.** Cho $A$ là bất kỳ ma trận cỡ $m \times  n$. Nếu $U$ và $V$ là hai rút gọn hàng bậc thang các ma trận thu được từ $A$ bằng cách áp dụng hai các dãy của các phép biến đổi sơ cấp trên hàng $E_{1}, \dots  , E_{p}$ và $F_{1}, \dots  , F_{q}$, sao cho
$$U = E_{p} \cdots  E_{1}AandV = F_{q} \cdots  F_{1}A,$$
Thì $U = V$. Nói cách khác, dạng bậc thang rút gọn theo hàng (RREF) của bất kỳ ma trận là duy nhất.

*Chứng minh.* Cho
$$C = E_{p} \cdots  E_{1}F_{1}^{-1} \cdots  F_{q}^{-1}$$
Sao cho
$$U = CVandV = C^{-1}U.$$
Nhắc lại từ Mệnh đề 8.13 rằng $U$ và $V$ có cùng hàng hạng (rank) $r$, và vì $U$ và $V$ là trong rref, điều này là số của khác không các hàng trong cả hai $U$ và $V$. Ta chứng minh bằng quy nạp theo $n$ rằng $U = V$ (và rằng thứ nhất $r$ các cột của $C$ là thứ nhất $r$ các cột trong $I_{m})$. Nếu $r = 0$ thì $A = U = V = 0$ và kết quả là tầm thường. Ta bây giờ giả sử rằng $r \ge 1$. Cho $\ell_{j}^{n}$ ký hiệu cột thứ $j$ của ma trận đơn vị (identity matrix) $I_{n}$, và cho $u_{j} = U\ell_{j}^{n}  , v_{j} = V \ell_{j}^{n}  , c_{j} = C\ell_{j}^{m}$, và $a_{j} = A\ell_{j}^{n}$, là cột thứ $j$ của $U, V , C$, và $A$ respectively. Thứ nhất I khẳng định rằng $u_{j} = 0$ khi và chỉ khi $v_{j} = 0$ khi và chỉ khi $a_{j} = 0$. Thật vậy, nếu $v_{j} = 0$, thì (bởi vì $U = CV$) $u_{j} = Cv_{j} = 0$, và nếu $u_{j} = 0$, thì $v_{j} = C^{-1}u_{j} = 0$. Vì $U = E_{p} \cdots  E_{1}A$, ta cũng thu được $a_{j} = 0$ khi và chỉ khi $u_{j} = 0$. Vì vậy, ta có thể đơn giản hóa của ta task bởi striking ra các cột của các không điểm từ $U, V$, và $A$, vì chúng sẽ có tương ứng các chỉ số. Ta vẫn sử dụng $n$ đến ký hiệu số của các cột của $A$. Nhận thấy rằng bởi vì $U$ và $V$ là rút gọn hàng bậc thang các ma trận với không có không các cột, ta phải có $u_{1} = v_{1} = \ell_{1}^{m}$. Khẳng định. Nếu $U$ và $V$ là rút gọn hàng bậc thang các ma trận mà không có không các cột sao cho $U = CV$, với mọi $k \ge 1$, nếu $k \le m$, thì $\ell_{k}^{m}$ xảy ra trong $U$ khi và chỉ khi $\ell_{k}^{m}$ xảy ra trong $V$, và nếu $\ell_{k}^{m}$ thực hiện xảy ra trong $U$, thì $1. \ell_{k}^{m}$ xảy ra cho cùng cột chỉ số $j_{k}$ trong cả hai $U$ và $V$; $2$. thứ nhất $j_{k}$ các cột của $U$ và $V$ match; $3$. subsequent các cột trong $U$ và $V$ (của cột chỉ số $> j_{k})$ có các tọa độ của chỉ số $k + 1$ qua $m$ là tất cả bằng $0$ cũng match. Cho $n_{k}$ là rightmost chỉ số của như vậy cột, với $n_{k} = j_{k}$ nếu ở đó là không có cái nào.

<!-- PAGE 311 -->
$4$. thứ nhất $k$ các cột của $C$ match thứ nhất $k$ các cột của $I_{m}$. Ta chứng minh điều này khẳng định bằng quy nạp theo $k$. Cho base trường hợp $k = 1$, ta đã biết rằng $u_{1} = v_{1} = \ell_{1}^{m}$. Ta cũng có
$$c_{1} = C\ell_{1}^{m}  = Cv_{1} = u_{1} = \ell_{1}^{m}  .$$
Nếu $v_{j} = \lambda \ell_{1}^{m}$ với một số $\lambda  \in \mathbb{R}$, thì
$$u_{j} = U\ell_{j}^{n}  = CV \ell_{j}^{n}  = Cv_{j} = \lambda C\ell_{1}^{m}  = \lambda c_{1} = \lambda \ell_{1}^{m}  = v_{j}.$$
Đồng dạng lập luận bằng cách sử dụng $C^{-1}$ chỉ ra rằng nếu $u_{j} = \lambda \ell_{1}^{m}$, thì $v_{j} = u_{j}$. Vì vậy, tất cả các cột của $U$ và $V$ tỷ lệ đến $\ell_{1}^{m}$ match, mà các thiết lập base trường hợp. Nhận thấy rằng nếu $\ell_{2}^{m}$ xuất hiện trong $U$, thì nó phải xuất hiện trong cả hai $U$ và $V$ cho cùng chỉ số, và nếu không thì $n_{1} = n$ và $U = V$. Tiếp theo chúng ta bây giờ chứng minh quy nạp bước. Nếu $n_{k} = n$, thì $U = V$ và ta được thực hiện. Nếu $k = r$, thì $C$ là ma trận khối (block matrix) của tạo thành
$$C = \begin{pmatrix} I_{r} & B \\ 0_{m-r,r} & C \end{pmatrix}$$
Và vì cuối cùng $m$ - $r$ các hàng của cả hai $U$ và $V$ là không các hàng, $C$ acts như đồng nhất thức trên thứ nhất $r$ các hàng, và do đó $U = V$. Ngược lại $k < r, n_{k} < n$, và $\ell_{k+1}^{m}$ xuất hiện trong cả hai $U$ và $V$, trong mà trường hợp, bởi $(2)$ và $(3)$ của giả thiết quy nạp (induction hypothesis), nó xuất hiện trong cả hai $U$ và $V$ cho cùng chỉ số, nói $j_{k+1}$. Do đó, $u_{jk+1} = v_{jk+1} = \ell_{k+1}^{m}$. Suy ra rằng
$$c_{k+1} = C\ell_{k+1}^{m}  = Cv_{jk+1} = u_{jk+1} = \ell_{k+1}^{m} ,$$
Do đó thứ nhất $k + 1$ các cột của $C$ match thứ nhất $k + 1$ các cột của $I_{m}$. Xét bất kỳ subsequent cột $v_{j}$ (với $j > j_{k+1})$ có các phần tử beyond $(k +1)th$ tất cả triệt tiêu. Thì $v_{j}$ là tổ hợp tuyến tính (linear combination) của các cột của $V$ đến trái của $v_{j}$, do đó
$$u_{j} = Cv_{j} = v_{j}.$$
Bởi vì thứ nhất $k + 1$ các cột của $C$ match thứ nhất $k + 1$ cột của $I_{m}$. Tương tự, bất kỳ subsequent cột $u_{j}$ (với $j > j_{k+1})$ có các phần tử beyond $(k+1)th$ tất cả triệt tiêu bằng $v_{j}$. Vì vậy, tất cả subsequent các cột trong $U$ và $V$ (của chỉ số $> j_{k+1})$ có các phần tử beyond $(k +$ 1)th tất cả triệt tiêu cũng match, mà các đầy đủ giả thiết quy nạp (induction hypothesis).
Nhận xét: Nhận thấy rằng $C = E_{p} \cdots  E_{1}F_{1}^{-1} \cdots  F_{q}^{-1}$ là không nhất thiết ma trận đơn vị (identity matrix) $I_{m}$. Tuy nhiên, $C = I_{m}$ nếu $r = m (A$ có hàng hạng (rank) $m)$. reduction đến dạng bậc thang theo hàng (row echelon form) cũng cung cấp phương pháp đến mô tả tập hợp của các nghiệm của hệ phương trình tuyến tính của tạo thành Ax $= b$.
