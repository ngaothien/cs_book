# Haar Biến đổi cho Digital Các ảnh


<!-- PAGE 164 -->
$$0.80.6$$
$$0.60.4$$
$$0.4$$
$$0.2$$
$$0.2$$
$$0$$
$$0$$
$$-0.2$$
$$-0.2$$
$$-0.4$$
$$-0.4$$
$$-0.6-0.6$$
$$-0.8\overline{0}\overline{1}\overline{2}\overline{3}\overline{4}\overline{5}\overline{6} 7-0.8$$
$$\overline{0}\overline{1}\overline{2}\overline{3}\overline{4}\overline{5}\overline{6} 7$$
$$x 104x 104$$
$$Figure 5.8: The signal “handel” and its Haar transform.$$
Do đó thứ nhất tuncate tail của $y$ để thu được vectơ của độ dài $65536 = 2^{16}$. plot của các tín hiệu tương ứng với $y$ và $c$ được hiển thị trong Hình 5.8. Thì chạy bài toán quy hoạch rằng các tập hợp tất cả các hệ số của $c$ có tuyệt đối giá trị là ít hơn rằng 0.05 đến không. Điều này các tập hợp $37272$ các hệ số đến $0$. thu được vectơ $c_{2}$ được chuyển đổi đến tín hiệu $y_{2}$. plot của các tín hiệu tương ứng với $y_{2}$ và $c_{2}$ được hiển thị trong Hình 5.9. Khi bạn loại/kiểu sound(y2), bạn tìm rằng music không’t khác nhau
$$10.6$$
$$0.8$$
$$0.4$$
$$0.6$$
$$0.40.2$$
$$0.2$$
$$0$$
$$0$$
$$-0.2$$
$$-0.2$$
$$-0.4-0.4$$
$$-0.6$$
$$-0.6$$
$$-0.8$$
$$-1\overline{0}\overline{1}\overline{2}\overline{3}\overline{4}\overline{5}\overline{6} 7-0.8$$
$$\overline{0}\overline{1}\overline{2}\overline{3}\overline{4}\overline{5}\overline{6} 7$$
$$x 104x 104$$
$$Figure 5.9: The compressed signal “handel” and its Haar transform.$$
Nhiều từ ban đầu, mặc dù nó sounds ít hơn crisp. Bạn nên đóng với khác các số greater hơn hoặc ít hơn 0.05. Bạn nên hear những gì xảy ra khi bạn loại/kiểu sound(c). Nó đóng music tương ứng với Haar biến đổi $c$ của $y$, và nó là khá funny.

## 5.5 Haar Biến đổi cho Digital Các ảnh

Một cái khác neat tính chất của Haar biến đổi là rằng nó có thể được instantly suy rộng/tổng quát hóa đến các ma trận (chẵn/ngay cả rectangular) mà không có bất kỳ extra effort! Điều này cho phép cho compression của

<!-- PAGE 165 -->
Digital các ảnh. Nhưng thứ nhất ta address vấn đề của normalization của Haar các hệ số. Như ta được quan sát trước đó, ma trận cỡ $2^{n} \times  2^{n}$ $W_{n}$ của Cơ sở Haar (Haar basis) các vectơ có trực giao các cột, nhưng các cột của nó thực hiện không có unit độ dài. Hệ quả là, $W_{n}^{\top}$ là không nghịch đảo của $W_{n}$, nhưng khá ma trận
$$W_{n}^{-1} = D_{n}W_{n}^{\top}$$
$$with D_{n} = \mathrm{diag} \begin{pmatrix} 2^{-n},2^{-n}, 2^{-(n-1)}, 2^{-(n-1)}, 2^{-(n-2)}, \dots  , 2^{-(n-2)}, \dots  , 2^{-1}, \dots  , 2^{-1} \\ |{z}| & {z & }| & {z & } & | & {z & } \\ 20 & 21 & 22 & 2n-1 \end{pmatrix} .$$

> **Định nghĩa 5.5.** ma trận trực giao (orthogonal matrix)
$$H_{n} = W_{n}\overline{D}_{n}^{21}$$
Có các cột được chuẩn hóa Cơ sở Haar (Haar basis) các vectơ, với
$$\overline{D}_{n}^{12} = \mathrm{diag} \begin{pmatrix} \overline{2}_{2}^{-n} ,\overline{2}_{2}^{-n},\overline{2}_{2}^{-n-1},\overline{2}_{2}^{-n-1},\overline{2}_{2}^{-n-2}, \dots  ,\overline{2}_{2}^{-n-2}, \dots  ,\overline{2}_{2}^{-1}, \dots  ,\overline{2}_{2}^{-1} \\ |{z}| & {z & }| & {z & } & | & {z & } \\ 20 & 21 & 22 & 2n-1 \end{pmatrix}$$
Được gọi được chuẩn hóa Haar biến đổi ma trận. Cho trước vectơ (tín hiệu) $u$, ta gọi $c = H_{n}^{\top} u$ được chuẩn hóa Haar các hệ số của $u$. Bởi vì $H_{n}$ là trực giao, $H_{n}^{-1} = H_{n}^{\top}$. Thì moment của phép đối xứng (reflection) chỉ ra rằng ta có đến slightly sửa đổi các thuật toán để tính $H_{n}^{\top} u$ và $H_{n}c$ như sau: Khi việc tính toán dãy của $u^{j}s$, sử dụng
$$\sqrt$$
$$u^{j+1}(2i -1) = (u^{j}(i) + u^{j}(2^{j}+ i))/\overline{2}$$
$$\sqrt$$
$$u^{j+1}(2i) = (u^{j}(i) -u^{j}(2^{j}+ i))/\overline{2},$$
Và khi việc tính toán dãy của $c^{j}s$, sử dụng
$$\sqrt$$
$$c^{j}(i) = (c^{j+1}(2i -1) + c^{j+1}(2i))/\overline{2}$$
$$\sqrt$$
$$c^{j}(2^{j}+ i) = (c^{j+1}(2i -1) -c^{j+1}(2i))/\overline{2}.$$
$$\sqrt$$
Lưu ý rằng things là bây giờ nhiều hơn/thêm đối xứng, tại expense của phép chia bởi $\overline{2.}$ Tuy nhiên, cho dài các vectơ, hóa ra là các phần tử này các thuật toán là một cách số nhiều hơn/thêm stable.
$$\sqrt$$
Nhận xét: Một số các tác giả (ví dụ, Stollnitz, Derose và Salesin $[174])$ rescale $c$ bởi $1/ \overline{2}^{n}$
$$\sqrt$$
Và $u$ bởi $\overline{2}^{n}$. Điều này là bởi vì chuẩn (norm) của cơ sở (basis) các hàm $\psi_{k}^{j}$ là không bằng $1$ (dưới
$$\sqrt \frac{the}{2^{j}} inner product \langle f, g\rangle =^{1} \int_{0}  f(t)g(t)dt). The normalized basis functions are the functions$$
$\psi_{k}^{j}$. Cho chúng ta bây giờ giải thích 2D phiên bản của Haar biến đổi. Ta mô tả phiên bản bằng cách sử dụng ma trận $W_{n}$, phương pháp bằng cách sử dụng $H_{n}$ đang là đồng nhất (ngoại trừ rằng $H_{n}^{-1} = H_{n}^{\top}$, nhưng điều này thực hiện

<!-- PAGE 166 -->
$$\times$$
Không đúng cho $W_{n}^{-1}$). Cho trước một ma trận cỡ $2^{m}  2^{n}$ $A$, ta có thể thứ nhất chuyển đổi các hàng của $A$ đến của chúng Haar các hệ số bằng cách sử dụng Haar biến đổi $W_{n}^{-1}$, thu được ma trận $B$, và thì chuyển đổi các cột của $B$ đến của chúng Haar các hệ số, bằng cách sử dụng ma trận $W_{m}^{-1}$. Bởi vì các cột và các hàng là exchanged trong bước thứ nhất,
$$B = A(W_{n}^{-1}  )^{\top},$$
Và trong bước thứ hai $C = W_{m}^{-1}  B$, do đó, ta có
$$C = W_{m}^{-1}  A(W_{n}^{-1} )^{\top}= D_{m}W_{m}^{\top}AW_{n} D_{n}.$$
Trong khác hướng, cho trước một ma trận cỡ $2^{m} \times  2^{n}$ $C$ của Haar các hệ số, ta reconstruct ma trận $A$ (ảnh (image)) bởi thứ nhất áp dụng $W_{m}$ đến các cột của $C$, thu được $B$, và thì $W_{n}^{\top}$ đến các hàng của $B$. Vì vậy
$$A = W_{m}CW_{n}^{\top}  .$$
Của course, ta không’t thực sự có đến nghịch đảo $W_{m}$ và $W_{n}$ và perform ma trận các phép nhân. Ta chỉ có để sử dụng của ta các thuật toán bằng cách sử dụng lấy trung bình và differencing. Đây là một ví dụ. Nếu dữ liệu ma trận (ảnh (image)) là ma trận cỡ $8 \times  8$
$$A = \begin{pmatrix} 64 & 2 & 3 & 61 & 60 & 6 & 7 & 57 \\ 9 & 55 & 54 & 12 & 13 & 51 & 50 & 16 \\ 17 & 47 & 46 & 20 & 21 & 43 & 42 & 24 \\ 40 & 26 & 27 & 37 & 36 & 30 & 31 & 33 \\ 32 & 34 & 35 & 29 & 28 & 38 & 39 & 25 \\ 41 & 23 & 22 & 44 & 45 & 19 & 18 & 48 \\ 49 & 15 & 14 & 52 & 53 & 11 & 10 & 56 \\ 8 & 58 & 59 & 5 & 4 & 62 & 63 & 1 \end{pmatrix} ,$$
Thì áp dụng của ta các thuật toán, ta tìm rằng
$$C = \begin{pmatrix} 32.5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 4 & -4 & 4 & -4 \\ 0 & 0 & 0 & 0 & 4 & -4 & 4 & -4 \\ 0 & 0 & 0.5 & 0.5 & 27 & -25 & 23 & -21 \\ 0 & 0 & -0.5 & -0.5 & -11 & 9 & -7 & 5 \\ 0 & 0 & 0.5 & 0.5 & -5 & 7 & -9 & 11 \\ 0 & 0 & 0.5 & 0.5 & 21 & 23 & 25 & 27 \end{pmatrix} .$$
$$----$$
Như ta có thể xem, $C$ có nhiều hơn/thêm không các phần tử (entries) hơn $A$; nó là compressed phiên bản của $A$. Ta có thể

<!-- PAGE 167 -->
Further compress $C$ bằng cách đặt đến $0$ tất cả các phần tử (entries) của tuyệt đối giá trị nhiều nhất 0.5. Thì ta thu được
$$C_{2} = \begin{pmatrix} 32.5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 4 & -4 & 4 & -4 \\ 0 & 0 & 0 & 0 & 4 & -4 & 4 & -4 \\ 0 & 0 & 0 & 0 & 27 & -25 & 23 & -21 \\ 0 & 0 & 0 & 0 & -11 & 9 & -7 & 5 \\ 0 & 0 & 0 & 0 & -5 & 7 & -9 & 11 \\ 0 & 0 & 0 & 0 & 21 & 23 & 25 & 27 \end{pmatrix} .$$
$$--$$
Ta tìm rằng reconstructed ảnh (image) là
$$A_{2} = \begin{pmatrix} 63.5 & 1.5 & 3.5 & 61.5 & 59.5 & 5.5 & 7.5 & 57.5 \\ 9.5 & 55.5 & 53.5 & 11.5 & 13.5 & 51.5 & 49.5 & 15.5 \\ 17.5 & 47.5 & 45.5 & 19.5 & 21.5 & 43.5 & 41.5 & 23.5 \\ 39.5 & 25.5 & 27.5 & 37.5 & 35.5 & 29.5 & 31.5 & 33.5 \\ 31.5 & 33.5 & 35.5 & 29.5 & 27.5 & 37.5 & 39.5 & 25.5 \\ 41.5 & 23.5 & 21.5 & 43.5 & 45.5 & 19.5 & 17.5 & 47.5 \\ 49.5 & 15.5 & 13.5 & 51.5 & 53.5 & 11.5 & 9.5 & 55.5 \\ 7.5 & 57.5 & 59.5 & 5.5 & 3.5 & 61.5 & 63.5 & 1.5 \end{pmatrix} ,$$
Mà là pretty close đến ban đầu ảnh (image) ma trận $A$. Hóa ra là Matlab có wonderful command, ảnh (image)(X) (cũng imagesc(X), mà thường thực hiện tốt hơn job), mà displays ma trận $X$ có ảnh (image) trong mà mỗi phần tử (entry) được hiển thị như little square có gray mức là tỷ lệ đến số giá trị của rằng phần tử (entry) (lighter nếu giá trị là cao hơn, darker nếu giá trị là closer đến không; âm các giá trị là treated như không). các ảnh tương ứng với $A$ và $C$ được hiển thị trong Hình 5.10.
$$Figure 5.10: An image and its Haar transform.$$
Compressed các ảnh tương ứng với $A_{2}$ và $C_{2}$ được hiển thị trong Hình 5.11. compressed

<!-- PAGE 168 -->
$$Figure 5.11: Compressed image and its Haar transform.$$
Các phiên bản xuất hiện là indistinguishable từ các ban đầu! Nếu ta sử dụng được chuẩn hóa các ma trận $H_{m}$ và $H_{n}$, thì các phương trình relating ảnh (image) ma trận $A$ và của nó được chuẩn hóa Haar biến đổi $C$ là
$$C = H_{m}^{\top}AH_{n}$$
$$A = H_{m}CH_{n}^{\top} .$$
Haar biến đổi có thể cũng được sử dụng đến send lớn các ảnh progressively trên internet. Thật vậy, ta có thể bắt đầu sending Haar các hệ số của ma trận $C$ bắt đầu từ coarsest các hệ số (cột thứ nhất từ đỉnh/trên xuống, thì cột thứ hai, etc.), và tại receiving kết thúc/cuối ta có thể bắt đầu reconstructing ảnh (image) như soon như ta có received đủ dữ liệu. Nhận thấy rằng thay vì của performing tất cả rounds của lấy trung bình và differencing trên mỗi hàng và mỗi cột, ta có thể perform riêng encoding (và decoding). Ví dụ, ta có thể perform đơn lẻ round của lấy trung bình và differencing với mỗi hàng và mỗi cột. kết quả là ảnh (image) bao gồm của bốn subimages, ở đâu đỉnh/trên trái quarter là coarser phiên bản của ban đầu, và rest (bao gồm của ba pieces) chứa finest chi tiết các hệ số. Ta có thể cũng perform hai rounds của lấy trung bình và differencing, hoặc ba rounds, etc. thứ hai round của lấy trung bình và differencing là ứng dụng đến đỉnh/trên trái quarter của ảnh (image). một cách tổng quát, thứ $k$ round là ứng dụng đến $2^{m+1-k} \times  2^{n+1-k}$ ma trận con bao gồm của thứ nhất $2^{m+1-k}$ các hàng và thứ nhất $2^{n+1-k}$ các cột $(1 \le k \le n)$ của ma trận thu được tại kết thúc/cuối của trước đó round. Điều này process được minh họa trên ảnh (image) được hiển thị trong Hình 5.12. kết quả của performing một round, hai rounds, ba rounds, và chín rounds của lấy trung bình được hiển thị trong Hình 5.13. Vì của ta các ảnh có kích thước $512 \times  512$, chín rounds của lấy trung bình cho ta Haar biến đổi, displayed như ảnh (image) trên đáy/dưới phải. ban đầu ảnh (image) có hoàn toàn disappeared! Ta để lại nó như fun bài tập đến sửa đổi các thuật toán liên quan đến lấy trung bình và differencing đến perform $k$ rounds của $averaging/differencing$. reconstruction thuật toán là little khó/tinh tế.

<!-- PAGE 169 -->
$$Figure 5.12: Original drawing by Durer.$$
Đẹp và dễ dàng accessible account của wavelets và của chúng sử dụng trong ảnh (image) processing và máy tính đồ họa có thể được tìm thấy trong Stollnitz, Derose và Salesin $[174]$. rất chi tiết account là cho trước trong Strang và và Nguyen $[178]$, nhưng điều này cuốn sách giả sử fair lượng của kiến thức nền tảng trong tín hiệu processing. Ta có thể tìm dễ dàng cơ sở (basis) của $2^{n} \times  2^{n} = 2^{2n}$ các vectơ $w_{ij} (2^{n} \times  2^{n}$ các ma trận) cho ánh xạ tuyến tính (linear map) rằng reconstructs ảnh (image) từ của nó Haar các hệ số, trong nghĩa rằng cho bất kỳ ma trận cỡ $2^{n} \times  2^{n}$ $C$ của Haar các hệ số, ảnh (image) ma trận $A$ được cho bởi
$$A = \sum_{i=1j}^{2n}  \sum_{=1}^{2n}  c_{ij}w_{ij}.$$
Thật vậy, ma trận $w_{ij}$ được cho bởi so-called tích ngoài (outer product)
$$w_{ij} = w_{i}(w_{j})^{\top}.$$
Tương tự, có một cơ sở (basis) của $2^{n} \times  2^{n} = 2^{2n}$ các vectơ $h_{ij} (2^{n} \times  2^{n}$ các ma trận) cho 2D Haar biến đổi, trong nghĩa rằng cho bất kỳ ma trận cỡ $2^{n} \times  2^{n}$ $A$, của nó ma trận $C$ của Haar các hệ số được cho bởi
$$C = \sum_{i=1j}^{2n}  \sum_{=1}^{2n}  a_{ij}h_{ij}.$$

<!-- PAGE 170 -->

![Figure 5.13](../../assets/ch05/fig_5_13.png)

**Hình 5.13:** Haar tranforms sau một, hai, ba, và chín rounds của lấy trung bình.
