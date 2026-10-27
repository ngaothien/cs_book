# Các ma trận Hadamard


<!-- PAGE 171 -->
Nếu các cột của $W^{-1}$ là $w_{1}', \dots  , w_{2n}'$, thì
$$h_{ij} = w_{i}'(w_{j}')^{\top}.$$
Ta để lại nó như bài tập để tính các cơ sở $(w_{ij})$ và $(h_{ij})$ cho $n = 2$, và đến display tương ứng các ảnh bằng cách sử dụng command imagesc.

## 5.6 Các ma trận Hadamard

Ở đó là một cái khác nổi tiếng họ của các ma trận somewhat đồng dạng đến Haar các ma trận, nhưng các ma trận này có các phần tử (entries) $+1$ và $-1$ (không có không các phần tử (entries)).

> **Định nghĩa 5.6.** thực $n \times  n$ ma trận $H$ là Ma trận Hadamard (Hadamard matrix) nếu $h_{ij} = \pm 1$ với mọi $i, j$ sao cho $1 \le i, j \le n$ và nếu
$$H^{\top}H = nI_{n}.$$
Do đó các cột của Ma trận Hadamard (Hadamard matrix) là đôi một trực giao. Bởi vì $H$ là ma trận vuông (square matrix), phương trình $H^{\top}H = nI_{n}$ chỉ ra rằng $H$ là khả nghịch, do đó ta cũng có $HH^{\top} = nI_{n}$. sau đây các ma trận là ví dụ của Các ma trận Hadamard:
$$H_{2} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} ,H_{4} = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & -1 & 1 & -1 \\ 1 & 1 & -1 & -1 \\ 1 & 1 & 1 & 1 \end{pmatrix} ,$$
$$--$$
Và
$$H_{8} = \begin{pmatrix} 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\ 1 & -1 & 1 & -1 & 1 & -1 & 1 & -1 \\ 1 & 1 & -1 & -1 & 1 & 1 & -1 & -1 \\ 1 & -1 & -1 & 1 & 1 & -1 & -1 & 1 \\ 1 & 1 & 1 & 1 & -1 & -1 & -1 & -1 \\ 1 & -1 & 1 & -1 & -1 & 1 & -1 & 1 \\ 1 & 1 & -1 & -1 & -1 & -1 & 1 & 1 \\ 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \end{pmatrix} .$$
$$----$$
Tự nhiên câu hỏi là để xác định dương các số nguyên $n$ cho mà Ma trận Hadamard (Hadamard matrix) có số chiều $n$ tồn tại, nhưng đáng ngạc nhiên là điều này là mở bài toán. Hadamard giả thuyết là rằng với mọi dương số nguyên của tạo thành $n =$ 4k, có một Ma trận Hadamard (Hadamard matrix) có số chiều $n$. Những gì là đã biết là cần điều kiện và khác nhau đủ các điều kiện.

> **Định lý 5.1.** Nếu $H$ là $n \times  n$ Ma trận Hadamard (Hadamard matrix), thì hoặc $n = 1, 2$, hoặc $n =$ 4k với một số dương số nguyên $k$.

<!-- PAGE 172 -->
Sylvester đã giới thiệu họ của Các ma trận Hadamard và được chứng minh rằng có Các ma trận Hadamard có số chiều $n = 2^{m}$ với mọi $m \ge 1$ bằng cách sử dụng sau đây cách xây dựng.

> **Mệnh đề 5.2.** (Sylvester, $1867)$ Nếu $H$ là Ma trận Hadamard (Hadamard matrix) có số chiều $n$, thì ma trận khối (block matrix) có số chiều 2n,
$$\begin{pmatrix} H & H \\ H & -H \end{pmatrix} ,$$
Là Ma trận Hadamard (Hadamard matrix). Nếu ta bắt đầu với
$$H_{2} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} ,$$
Ta thu được vô hạn họ của đối xứng Các ma trận Hadamard thường được gọi là Sylvester– Các ma trận Hadamard và được ký hiệu bởi $H_{2m}$. Sylvester–Các ma trận Hadamard $H_{2}, H_{4}$ và $H_{8}$ được hiển thị trên trước đó trang. Trong $1893$, Hadamard gave các ví dụ của Các ma trận Hadamard cho $n = 12$ và $n = 20$. Tại trình bày, Các ma trận Hadamard là đã biết với mọi $n =$ 4k $\le 1000$, ngoại trừ cho $n = 668, 716$, và $892$. Các ma trận Hadamard có khác nhau các ứng dụng đến sai số đúng codes, tín hiệu processing, và số tuyến tính đại số; xem Seberry, Wysocki và Wysocki $[160]$ và Tropp $[183]$. Ví dụ, có một code based trên $H_{32}$ rằng có thể đúng $7$ các sai số trong bất kỳ 32-bit encoded khối, và có thể detect eighth. Điều này code đã được sử dụng trên Mariner spacecraft trong $1969$ đến transmit pictures quay lại đến earth. Với mọi $m \ge 0$, từng khúc afin các hàm $plf((H_{2m})_{i})$ liên kết với $2^{m}$ các hàng của Sylvester–Ma trận Hadamard (Hadamard matrix) $H_{2m}$ là các hàm trên $[0, 1]$ đã biết như Walsh các hàm. Nó là thông lệ đến chỉ số các phần tử này $2^{m}$ các hàm bởi các số nguyên $0, 1, \dots  , 2^{m}-1$ trong như vậy cách rằng Walsh hàm Wal(k, $t)$ bằng hàm $plf((H_{2m})_{i})$ liên kết với Hàng $i$ của $H_{2m}$ rằng chứa $k$ thay đổi của các dấu giữa liên tiếp các nhóm của $+1$ và liên tiếp các nhóm của $-1$. Ví dụ, thứ năm hàng của $H_{8}$, cụ thể là
$$\begin{pmatrix} 1 & -1 & -1 & 1 & 1 & -1 & -1 & 1 \end{pmatrix} ,$$
Có năm liên tiếp các khối của $+1s$ và -1s, bốn dấu thay đổi giữa các phần tử này các khối, và do đó là liên kết với Wal(4, $t)$. Đặc biệt, Walsh các hàm tương ứng với các hàng của $H_{8}$ (từ đỉnh/trên xuống) là: Wal(0, $t)$, Wal(7, $t)$, Wal(3, $t)$, Wal(4, $t)$, Wal(1, $t)$, Wal(6, $t)$, Wal(2, $t)$, Wal(5, $t)$. Bởi vì của connection giữa Sylvester–Các ma trận Hadamard và Walsh các hàm, Sylvester–Các ma trận Hadamard được gọi là Walsh–Các ma trận Hadamard bởi một số các tác giả. Với mọi $m$, $2^{m}$ Walsh các hàm là đôi một trực giao. đếm được tập hợp của Walsh các hàm Wal(k, $t)$ với mọi $m \ge 0$ và tất cả $k$ sao cho $0 \le k \le 2^{m}$ - $1$ có thể được được thứ tự trong
