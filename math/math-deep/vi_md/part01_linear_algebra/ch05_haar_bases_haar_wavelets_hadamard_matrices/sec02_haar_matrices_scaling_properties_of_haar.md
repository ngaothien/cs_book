# Haar Các ma trận, Scaling Các tính chất của Wavelet Haar (Haar wavelets)


<!-- PAGE 155 -->
$$6451$$
$$Figure 5.1: The original signal v.$$
$$2$$
$$1$$
$$55$$
$$33$$
$$-1$$
$$-2$$
$$Figure 5.2: First averages and first half differences.$$
Một lần nữa ta tính các trung bình và một nửa differences thu được Hình 5.3. Ta thu được các hệ số $c_{1} = 4$ và $c_{2} = 1$. Lưu ý rằng ban đầu tín hiệu $v$ có thể được reconstructed từ hai các tín hiệu trong Hình 5.2, và tín hiệu trên trái của Hình 5.2 có thể được reconstructed từ hai các tín hiệu trong Hình 5.3. Đặc biệt, dữ liệu từ Hình 5.2 cho chúng ta
$$-$$
$$5 + 1 = \frac{v_{1} + v_{2}}{2} + \frac{v_{1}v_{2}}{-2} = v_{1}$$
$$5 -1 = \frac{v_{1} + v_{2}}{2} - \frac{v_{1}v_{2}}{-2} = v_{2}$$
$$3 + 2 = \frac{v_{3} + v_{4}}{2} + \frac{v_{3}v_{4}}{-2} = v_{3}$$
$$3 -2 = \frac{v_{3} + v_{4}}{2} - \frac{v_{3}v_{4}}{2} = v_{4}.$$

## 5.2 Các cơ sở Haar và Haar Các ma trận, Scaling Các tính chất

$$of Haar Wavelets$$
Phương pháp được thảo luận trong Mục 5.1 có thể được suy rộng/tổng quát hóa đến các tín hiệu của bất kỳ độ dài $2^{n}$. trước đó trường hợp tương ứng với $n = 2$. Cho chúng ta xét trường hợp $n = 3$. Cơ sở Haar (Haar basis)

<!-- PAGE 156 -->
$$11$$
$$4444$$
$$-1-1$$
$$Figure 5.3: Second averages and second half differences.$$
$(w_{1}, w_{2}, w_{3}, w_{4}, w_{5}, w_{6}, w_{7}, w_{8})$ được cho bởi ma trận
$$W = \begin{pmatrix} 1 & 1 & 1 & 0 & 1 & 0 & 0 & 0 \\ 1 & 1 & 1 & 0 & -1 & 0 & 0 & 0 \\ 1 & 1 & -1 & 0 & 0 & 1 & 0 & 0 \\ 1 & 1 & -1 & 0 & 0 & -1 & 0 & 0 \\ 1 & -1 & 0 & 1 & 0 & 0 & 1 & 0 \\ 1 & -1 & 0 & 1 & 0 & 0 & -1 & 0 \\ 1 & -1 & 0 & -1 & 0 & 0 & 0 & 1 \\ 1 & 1 & 0 & 1 & 0 & 0 & 0 & 1 \end{pmatrix} .$$
$$---$$
Các cột của ma trận này là trực giao, và nó là dễ để xem rằng
$$W^{-1}= \mathrm{diag}(1/8, 1/8, 1/4, 1/4, 1/2, 1/2, 1/2, 1/2)W^{\top}.$$
Pattern là bắt đầu đến emerge. Nó trông like thứ hai Cơ sở Haar (Haar basis) vectơ $w_{2}$ là “mother” của tất cả khác cơ sở (basis) các vectơ, ngoại trừ thứ nhất, có mục đích là đến perform lấy trung bình. Thật vậy, nói chung, cho trước
$$w_{2} = (1, \dots  , 1, -1, \dots  , -1),$$
$$|{z}$$
$$2n$$
Khác Cơ sở Haar (Haar basis) các vectơ là thu được bởi “scaling và shifting process.” Bắt đầu từ $w_{2}$, scaling process sinh ra các vectơ
$$w_{3}, w_{5}, w_{9}, \dots  , w_{2j+1}, \dots  , w_{2n-1+1},$$
Sao cho $w_{2j+1+1}$ là thu được từ $w_{2j+1}$ bởi tạo thành hai liên tiếp các khối của $1$ và $-1$ của một nửa kích thước của các khối trong $w_{2j+1}$, và đặt tất cả khác các phần tử (entries) đến không. Nhận thấy rằng $w_{2j+1}$ có $2^{j}$ các khối của $2^{n-j}$ các phần tử. shifting process bao gồm trong shifting các khối của $1$ và $-1$ trong $w_{2j+1}$ đến phải bởi inserting khối của $(k$ - $1)2^{n-j}$ các không điểm từ trái, với $0 \le j \le n -1$ và $1 \le k \le 2^{j}$. Lưu ý rằng của ta quy ước là để sử dụng $j$ như scaling chỉ số và $k$ như shifting chỉ số. Do đó, ta thu được kết quả sau công thức cho $w_{2j+k}$:
$$01 \le i \le (k -1)2^{n-j}$$
$$$$
$$$$
$$1(k -1)2^{n-j}+ 1 \le i \le (k -1)2^{n-j}+ 2^{n-j-1}$$
$$$$
$$w_{2j+k}(i) =$$
$$-1(k -1)2^{n-j}+ 2^{n-j-1}+ 1 \le i \le k2^{n-j}$$
$$$$
$$$$
$$0k2^{n-j}+ 1 \le i \le 2^{n},$$
$$$$

<!-- PAGE 157 -->
Với $0 \le j \le n$ - $1$ và $1 \le k \le 2^{j}$. Của course
$$w_{1} = (1, \dots  , 1).$$
$$|{z}$$
$$2n$$
Ở trên các công thức nhìn little tốt hơn nếu ta thay đổi của ta chỉ số slightly bởi đặt $k$ biến thiên từ $0$ đến $2^{j}$ - $1$, và bằng cách sử dụng chỉ số $j$ thay vì của $2^{j}$.

> **Định nghĩa 5.1.** các vectơ của Cơ sở Haar (Haar basis) có số chiều $2^{n}$ được ký hiệu bởi
$$w_{1}, h_{0}^{0}, h_{0}^{1}, h_{1}^{1}, h_{0}^{2}, h_{1}^{2}, h_{2}^{2}, h_{3}^{2}, \dots  , h_{k}^{j}, \dots  , h_{2n-1-1}^{n-1},$$
Ở đâu
$$01 \le i \le k2^{n-j}$$
$$$$
$$$$
$$1k2^{n-j}+ 1 \le i \le k2^{n-j}+ 2^{n-j-1}$$
$$$$
$$h_{k}^{j}(i) =$$
$$-1k2^{n-j}+ 2^{n-j-1}+ 1 \le i \le (k + 1)2^{n-j}$$
$$$$
$$$$
$$0(k + 1)2^{n-j}+ 1 \le i \le 2^{n},$$
$$$$
Với $0 \le j \le n$ - $1$ và $0 \le k \le 2^{j}$ - $1$. ma trận cỡ $2^{n} \times  2^{n}$ có các cột là các vectơ
$$w_{1}, h_{0}^{0}, h_{0}^{1}, h_{1}^{1}, h_{0}^{2}, h_{1}^{2}, h_{2}^{2}, h_{3}^{2}, \dots  , h_{k}^{j}, \dots  , h_{2n-1-1}^{n-1},$$
(trong rằng thứ tự), được gọi là Haar ma trận có số chiều $2^{n}$, và được ký hiệu bởi $W_{n}$. Hóa ra là có một cách đến understand các phần tử này các công thức tốt hơn nếu ta interpret vectơ $u = (u_{1}, \dots  , u_{m})$ như từng khúc tuyến tính hàm trên khoảng/đoạn $[0, 1)$.

> **Định nghĩa 5.2.** Cho trước vectơ $u = (u_{1}, \dots  , u_{m})$, từng khúc tuyến tính $function^{1}$ plf(u) được định nghĩa sao cho
$$-$$
$$plf(u)(x) = u_{i}, \frac{i1}{m} \le x < \frac{i}{m} , 1 \le i \le m.$$
Trong words, hàm plf(u) có giá trị $u_{1}$ trên khoảng/đoạn $[0, 1/m)$, giá trị $u_{2}$ trên $[1/m, 2/m)$, etc., và giá trị $u_{m}$ trên khoảng/đoạn $[(m$ - $1)/m, 1)$. Ví dụ, từng khúc tuyến tính hàm liên kết với vectơ
$$u = (2.4, 2.2, 2.15, 2.05, 6.8, 2.8, -1.1, -1.3)$$
Được hiển thị trong Hình 5.4. Thì mỗi cơ sở (basis) vectơ $h_{k}^{j}$ tương ứng với hàm
$$\psi_{k}^{j}  = plf(h_{k}^{j}).$$
$\overline{1}\overline{Piecewise} \overline{constant} \overline{function} \overline{might} \overline{be}$ nhiều hơn/thêm accurate name.

<!-- PAGE 158 -->
$$7$$
$$6$$
$$5$$
$$4$$
$$3$$
$$2$$
$$1$$
$$0$$
$$-1$$
$$-2\overline{0}\overline{0.1}\overline{0.2}\overline{0.3}\overline{0.4}\overline{0.5}\overline{0.6}\overline{0.7}\overline{0.8}\overline{0.9} 1$$
$$Figure 5.4: The piecewise linear function plf(u).$$
Đặc biệt, với mọi $n$, Cơ sở Haar (Haar basis) các vectơ
$$h_{0}^{0} = w_{2} = (1, \dots  , 1, -1, \dots  , -1)$$
$$|{z}$$
$$2n$$
Cho cùng từng khúc tuyến tính hàm $\psi$ cho trước bởi
$$1if0 \le x < 1/2$$
$$$$
$$$$
$$\psi (x) =-1if1/2 \le x < 1$$
$$0otherwise,$$
$$$$
Có đồ thị được hiển thị trong Hình 5.5. Nó là dễ để xem rằng $\psi_{k}^{j}$ được cho bởi đơn giản biểu thức
$$1$$
$$1$$
$$0$$
$$-1$$
$$Figure 5.5: The Haar wavelet \psi .$$
$$\psi_{k}^{j} (x) = \psi (2^{j}x -k),0 \le j \le n -1, 0 \le k \le 2^{j}-1.$$
Ở trên công thức làm cho nó rõ ràng rằng $\psi_{k}^{j}$ là thu được từ $\psi$ bởi scaling và shifting.

> **Định nghĩa 5.3.** hàm $\varphi_{0}^{0}  = plf(w_{1})$ là từng khúc tuyến tính hàm với hằng số giá trị $1$ trên $[0, 1)$, và các hàm $\psi_{k}^{j}  = plf(h_{k}^{j})$ cùng với $\varphi_{0}^{0}$ là đã biết như Wavelet Haar (Haar wavelets).

<!-- PAGE 159 -->
Thay vì bằng cách sử dụng $W^{-1}$ đến chuyển đổi vectơ $u$ đến vectơ $c$ của các hệ số trên Cơ sở Haar (Haar basis), và ma trận $W$ đến reconstruct vectơ $u$ từ của nó Haar các hệ số $c$, ta có thể sử dụng faster các thuật toán rằng sử dụng lấy trung bình và differencing. Nếu $c$ là vectơ của Haar các hệ số có số chiều $2^{n}$, ta tính dãy của các vectơ $u^{0}, u^{1}, \dots , u^{n}$ như sau:
$$u^{0}= c$$
$$u^{j+1}= u^{j}$$
$$u^{j+1}(2i -1) = u^{j}(i) + u^{j}(2^{j}+ i)$$
$$u^{j+1}(2i) = u^{j}(i) -u^{j}(2^{j}+ i),$$
Cho $j = 0, \dots  , n$ - $1$ và $i = 1, \dots  , 2^{j}$. reconstructed vectơ (tín hiệu) là $u = u^{n}$. Nếu $u$ là vectơ có số chiều $2^{n}$, ta tính dãy của các vectơ $c^{n}, c^{n-1}, \dots  , c^{0}$ như sau:
$$c^{n}= u$$
$$c^{j}= c^{j+1}$$
$$c^{j}(i) = (c^{j+1}(2i -1) + c^{j+1}(2i))/2$$
$$c^{j}(2^{j}+ i) = (c^{j+1}(2i -1) -c^{j+1}(2i))/2,$$
Cho $j = n$ - $1, \dots  , 0$ và $i = 1, \dots  , 2^{j}$. vectơ trên Cơ sở Haar (Haar basis) là $c = c^{0}$. Ta để lại nó như một bài tập đến cài đặt ở trên các bài toán quy hoạch trong Matlab bằng cách sử dụng hai các biến $u$ và $c$, và bởi xây dựng một cách lặp $2^{j}$. Đây là một ví dụ của conversion của vectơ đến của nó Haar các hệ số cho $n = 3$. Cho trước dãy $u = (31, 29, 23, 17, -6, -8, -2, -4)$, ta thu được dãy $c^{3} = (31, 29, 23, 17, -6, -8, -2, -4)$
$$c^{2}= \begin{pmatrix} 31 + 2923 + 17-6 -8-2 -431 -2923 -17-6 -(-8)-2 -(-4) \\ , & , & , & , & , & , & , \\ 2 & 2 & 2 & 2 & 2 & 2 & 2 & 2 \end{pmatrix}$$
$= (30, 20, -7, -3, 1, 3, 1, 1)$
$$c^{1}= \begin{pmatrix} 30 + 20-7 -330 -20-7 -(-3) \\ , & , & , & , 1, 3, 1, 1 \\ 2 & 2 & 2 & 2 \end{pmatrix}$$
$= (25, -5, 5, -2, 1, 3, 1, 1)$
$$c^{0}= \begin{pmatrix} 25 -525 -(-5) \\ , & , 5, -2, 1, 3, 1, 1 \\ 2 & 2 \end{pmatrix} = (10, 15, 5, -2, 1, 3, 1, 1)$$
Do đó $c = (10, 15, 5, -2, 1, 3, 1, 1)$. Ngược lại, cho trước $c = (10, 15, 5, -2, 1, 3, 1, 1)$, ta thu được
