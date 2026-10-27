# Dealing với Roundoff Các sai số; Chọn phần tử trụ Strategies


<!-- PAGE 288 -->
Vì $E_{k}^{k} = E_{k}$, ta thu được
$$\cdots$$
$$(E_{1}^{k})^{-1} (E_{k-1}^{k})^{-1}(E_{k}^{k})^{-1}= (I + P_{k}\Lambda_{k-1} )E_{k}^{-1} .$$
Tuy nhiên, theo Định nghĩa
$$I + \Lambda_{k}  = (I + P_{k}\Lambda_{k-1} )E_{k}^{-1} ,$$
Mà chứng tỏ rằng
$$\cdots$$
$$I + \Lambda_{k}  = (E_{1}^{k})^{-1} (E_{k-1}^{k})^{-1}(E_{k}^{k})^{-1},(\dagger )$$
Và các hoàn tất quy nạp bước cho chứng minh của công thức này. Nếu ta áp dụng Phương trình (*) một lần nữa với $k + 1$ trong place của $k$, ta có
$$\cdots$$
$$(E_{1}^{k})^{-1} (E_{k}^{k})^{-1}= I +\mathcal{E}_{1}^{k} + \cdots  +\mathcal{E}_{k}^{k},$$
Và cùng với $(\dagger$), ta thu được,
$$\Lambda_{k}  =\mathcal{E}_{1}^{k} + \cdots  +\mathcal{E}_{k}^{k},$$
Cũng hoàn tất quy nạp bước cho chứng minh của công thức này. Cho $k =$ n-1 trong $(\dagger$), ta thu được mong muốn phương trình: $L =$ I $+ \Lambda_{n-1}$.

## 8.7 Dealing với RoundoffErrors; Chọn phần tử trụ Strategies

Cho chúng ta bây giờ ngắn gọn comment trên lựa chọn của phần tử trụ (pivot). Mặc dù về mặt lý thuyết, bất kỳ phần tử trụ (pivot) có thể được được chọn, khả năng của roundofferrors suy ra rằng nó là không tốt ý tưởng đến chọn rất nhỏ các phần tử trụ. sau đây ví dụ minh họa điều này điểm. Xét hệ phương trình tuyến tính
$$10^{-4}x+y=1$$
$$x+y=2.$$
Vì $10^{-4}$ là khác không, nó có thể được được lấy như phần tử trụ (pivot), và ta thu được
$$10^{-4}x+y=1$$
$$(1 -10^{4})y=2 -10^{4}.$$
Do đó, chính xác nghiệm là
$$-$$
$$x = \frac{10^{4}}{10^{4}-1} ,y = \frac{10^{4}2}{10^{4}-1} .$$
Tuy nhiên, nếu roundofftakes place trên thứ tư digit, thì $10^{4} -1 = 9999$ và $10^{4} -2 = 9998$ sẽ là rounded offboth đến $9990$, và thì nghiệm là $x = 0$ và $y = 1$, rất far từ chính xác nghiệm ở đâu $x \approx 1$ và $y \approx 1$. bài toán là rằng ta được chọn rất nhỏ phần tử trụ (pivot). Nếu thay vì ta hoán vị các phương trình, phần tử trụ (pivot) là $1$, và sau phép khử ta thu được hệ
$$x+y=2$$
$$(1 -10^{-4})y=1 -2 \times  10^{-4}.$$

<!-- PAGE 289 -->
Điều này time, $1$ - $10^{-4} =$ 0.9999 và $1$ - $2 \times  10^{-4} =$ 0.9998 là rounded offto 0.999 và nghiệm là $x = 1, y = 1$, nhiều closer đến chính xác nghiệm. Đến remedy bài toán này, một có thể sử dụng chiến lược của riêng chọn phần tử trụ. Điều này bao gồm của chọn during Bước $k (1 \le k \le n$ - $1)$ một của các phần tử (entries) $a_{i k}^{(k)}$ sao cho
$$|a_{i k}^{(k)} | = \max |a_{p k}^{(k)}|.$$
$$k\le p\le n$$
Bởi cực đại hóa giá trị của phần tử trụ (pivot), ta tránh chia bởi undesirably nhỏ các phần tử trụ.
Nhận xét: $A$ ma trận, $A$, được gọi là chặt cột một cách đường chéo trội khi và chỉ khi
$$|a_{j j}| > \sum_{=1, i\neq j}^{n}  |a_{i j}|,for j = 1, \dots  , n$$
$$i$$
(resp. chặt hàng một cách đường chéo trội khi và chỉ khi
$$|a_{i i}| > \sum_{=1, j\neq}^{n}  |a_{i j}|,for i = 1, \dots  , n.)$$
$$ji$$
Ví dụ, ma trận
$$\begin{pmatrix} 7 & 1 \\ 1\overline{2} & 4 & 1 & 0 \\ \ddots & \ddots & \ddots \\ 0 & 1 & 4 & 1 \\ 1 & 7 \end{pmatrix}$$
$$\overline{2}$$
Của đường cong nội suy bài toán được thảo luận trong Mục 8.1 là chặt cột (và hàng) một cách đường chéo trội. Nó có đã được đã biết cho dài time (trước $1900$, nói bởi Hadamard) rằng nếu ma trận $A$ là chặt cột một cách đường chéo trội (resp. chặt hàng một cách đường chéo trội), thì nó là khả nghịch. Nó có thể cũng được hiển thị rằng nếu $A$ là chặt cột một cách đường chéo trội, thì Phép khử Gauss (Gaussian elimination) với riêng chọn phần tử trụ thực hiện không thực sự đòi hỏi chọn phần tử trụ (xem Bài toán 8.12). Một cái khác chiến lược, được gọi là đầy đủ chọn phần tử trụ, bao gồm trong chọn một số phần tử (entry) $a_{i j}^{(k)}$, ở đâu $k \le i, j \le n$, sao cho
$$|a_{i j}^{(k)} | = \max |a_{p q}^{(k)} |.$$
$$k\le p,q\le n$$
Tuy nhiên, trong phương pháp này, nếu được chọn phần tử trụ (pivot) là không trong cột $k$, nó là cũng cần đến hoán vị các cột. Điều này là đạt được bằng cách nhân trên phải bởi hoán vị ma trận. Tuy nhiên, đầy đủ chọn phần tử trụ tiến tới là cũng expensive trong thực tế, và riêng chọn phần tử trụ là phương pháp của lựa chọn. đặc biệt trường hợp ở đâu Nhân tử hóa LU (LU-factorization) là một cách cụ thể efficient là trường hợp của ba đường chéo các ma trận, mà ta bây giờ xét.
