# Tạo ra QR Phương pháp Nhiều hơn/thêm Efficient Bằng cách sử dụng Shifts


<!-- PAGE 675 -->

## 18.3 Tạo ra QR Phương pháp Nhiều hơn/thêm Efficient

$$Using Shifts$$
Đến cải thiện efficiency và cope với các cặp của phức liên hợp các trị riêng (eigenvalues) trong trường hợp của thực các ma trận, sau đây các bước được lấy:
$(1)$ một cách ban đầu rút gọn ma trận $A$ đến trên Hessenberg tạo thành, như $A = UHU^{*}$. Thì áp dụng QR-algorithm đến $H$ (thực sự, đến của nó unreduced Hessenberg các khối). Nó là dễ để xem rằng các ma trận $H_{k}$ produced bởi QR thuật toán vẫn là trên Hessenberg.
$(2)$ Đến accelerate sự hội tụ, sử dụng shifts, và đến deal với các cặp của phức liên hợp các trị riêng (eigenvalues), sử dụng gấp đôi shifts.
$(3)$ Thay vì của việc tính toán Nhân tử hóa QR (QR-factorization) một cách tường minh trong khi thực hiện shift, perform ẩn shift mà tính $A_{k+1} = Q_{k}^{*}A_{k}Q_{k}$ mà không có có để tính QRfactorization (của $A_{k}$ - $\sigma_{k}$ I), và tương tự trong trường hợp của gấp đôi shift. Điều này là hầu hết intricate modification của cơ bản QR thuật toán và ta sẽ không thảo luận nó ở đây. phương pháp này là thường referred như bulge chasing. Chi tiết về điều này kỹ thuật cho thực các ma trận có thể được tìm thấy trong Demmel $[48]$ (Mục 4.4.8) và Golub và Van Loan $[83]$ (Mục 7.5). Watkins các thảo luận QR thuật toán với shifts như bulge chasing phương pháp trong nhiều hơn/thêm tổng quát trường hợp của phức các ma trận $[193, 194]$. Cho chúng ta repeat quan trọng nhận xét được tạo trong mục trước. Nếu ta bắt đầu với ma trận $H$ trong trên Hessenberg tạo thành, nếu tại bất kỳ giai đoạn của QR thuật toán ta tìm rằng một số subdiagonal phần tử (entry) $(H_{k})_{p+1p} = 0$ hoặc là rất nhỏ, thì $H_{k}$ là của tạo thành
$$H_{k} = \begin{pmatrix} H_{11} & H_{12} \\ 0 & H_{22} \end{pmatrix} ,$$
Ở đâu cả hai $H_{11}$ và $H_{22}$ là trên Hessenberg các ma trận (với $H_{11}$ một ma trận cỡ $p \times  p$ và $H_{22}$ $(n$ - $p) \times  (n$ - $p)$ ma trận), và các trị riêng (eigenvalues) của $H_{k}$ là các trị riêng (eigenvalues) của $H_{11}$ và $H_{22}$. Ví dụ, trong ma trận
$$H = \begin{pmatrix} * & * & * & * & * \\ h_{21} & * & * & * & * \\ 0 & h_{32} & * & * & * \\ 0 & 0 & h_{43} & * & * \\ 0 & 0 & 0 & h_{54} \end{pmatrix} ,$$
$$*$$
Nếu $h_{43} = 0$, thì ta có ma trận khối (block matrix)
$$H = \begin{pmatrix} * & * & * & * & * \\ h_{21} & * & * & * & * \\ 0 & h_{32} & * & * & * \\ 0 & 0 & 0 & * & * \\ 0 & 0 & 0 & h_{54} \end{pmatrix} .$$
$$*$$

<!-- PAGE 676 -->
Thì ta có thể một cách đệ quy áp dụng QR thuật toán đến $H_{11}$ và $H_{22}$. Đặc biệt, nếu $(H_{k})_{nn-1} = 0$ hoặc là rất nhỏ, thì $(H_{k})_{nn}$ là tốt xấp xỉ của trị riêng (eigenvalue), do đó ta có thể xóa hàng cuối cùng và cột cuối cùng của $H_{k}$ và áp dụng QR thuật toán đến điều này ma trận con. Điều này process được gọi là deflation. Nếu $(H_{k})_{n-1n-2} = 0$ hoặc là rất nhỏ, thì $2 \times  2$ “góc khối”
$$\begin{pmatrix} (H_{k})_{n-1n-1} & (H_{k})_{n-1n} \\ (H_{k})_{nn-1} & (H_{k})_{nn} \end{pmatrix}$$
Xuất hiện, và các trị riêng (các trị riêng (eigenvalues)) của nó có thể được được tính ngay lập tức bởi việc giải toàn phương phương trình. Thì ta deflate $H_{k}$ bởi xóa của nó cuối cùng hai các hàng và của nó cuối cùng hai các cột và áp dụng QR thuật toán đến điều này ma trận con. Do đó nó sẽ dường như desirable đến sửa đổi cơ bản QR thuật toán sao cho ở trên các tình huống phát sinh, và điều này là những gì shifts là designed cho. Chính xác hơn, dưới các giả thiết của Định lý 18.1, nó có thể được được hiển thị (xem Ciarlet $[41]$, Mục 6.3) rằng phần tử (entry) $(A_{k})_{ij}$ với $i > j$ hội tụ đến $0$ như $|\lambda_{i} /\lambda_{j} |^{k}$ hội tụ đến $0$. Cũng, nếu ta cho $r_{i}$ được định nghĩa bởi
$$







$$
$$r_{1} = \frac{\lambda_{2}}{\lambda_{1}} ,r_{i} = \max \frac{\lambda_{i}}{\lambda_{i-1}} , \frac{\lambda_{i+1}}{\lambda_{i}} ,2 \le i \le n -1,r_{n} = \frac{\lambda_{n}}{\lambda_{n-1}} ,$$
Thì có một hằng số $C$ (độc lập của $k)$ sao cho
$$|(A_{k})_{ii} -\lambda_{i} | \le Cr_{i}^{k} ,1 \le i \le n.$$
Đặc biệt, nếu $H$ là trên Hessenberg, thì phần tử (entry) $(H_{k})_{i+1i}$ hội tụ đến $0$ như $|\lambda_{i+1} /\lambda_{i} |^{k}$ hội tụ đến $0$. Do đó nếu ta chọn $\sigma_{k}$ close đến $\lambda_{i}$, ta kỳ vọng rằng $(H_{k}$ - $\sigma_{k} I)_{i+1i}$ hội tụ đến $0$ như $|(\lambda_{i+1}  -\sigma_{k} )/(\lambda_{i}  -\sigma_{k} )|^{k}$ hội tụ đến $0$, và điều này tỉ số là nhiều nhỏ hơn hơn $1$ như $\sigma_{k}$ là closer đến $\lambda_{i}$. Typically, ta áp dụng shift đến accelerate sự hội tụ đến $\lambda_{n}$ (do đó $i = n$ - $1)$. Trong trường hợp này, cả hai $(H_{k} -\sigma_{k} I)_{nn-1}$ và $|(H_{k} -\sigma_{k} I)_{nn} -\lambda_{n}$ | hội tụ đến $0$ như $|(\lambda_{n}  -\sigma_{k} )/(\lambda_{n-1}  -\sigma_{k} )|^{k}$ hội tụ đến $0$. shift là sau đây được sửa đổi QR-steps (switching quay lại đến tùy ý ma trận $A$, vì shift kỹ thuật áp dụng nói chung). Chọn một số $\sigma_{k}$, hy vọng là close đến một số trị riêng (eigenvalue) của $A$ (nói chung, $\lambda_{n}$), và QR-factor $A_{k}$ - $\sigma_{k}$ I như
$$A_{k} -\sigma_{k} I = Q_{k}R_{k},$$
Và thì tạo thành
$$A_{k+1} = R_{k}Q_{k} + \sigma_{k} I.$$
Vì
$$A_{k+1} = R_{k}Q_{k} + \sigma_{k} I$$
$$= Q_{k}^{*}Q_{k}R_{k}Q_{k} + Q_{k}^{*}Q_{k}\sigma_{k}$$
$$= Q_{k}^{*}(Q_{k}R_{k} + \sigma_{k} I)Q_{k}$$
$$= Q_{k}^{*}A_{k}Q_{k},$$

<!-- PAGE 677 -->
$A_{k+1}$ là đồng dạng đến $A_{k}$, như trước. Nếu $A_{k}$ là trên Hessenberg, thì nó là dễ để xem rằng $A_{k+1}$ là cũng trên Hessenberg. Nếu $A$ là trên Hessenberg và nếu $\sigma_{i}$ là chính xác bằng trị riêng (eigenvalue), thì $A_{k}$ - $\sigma_{k}$ I là suy biến, và tạo thành Nhân tử hóa QR (QR-factorization) sẽ detect rằng $R_{k}$ có một số đường chéo phần tử (entry) bằng $0$. Giả sử rằng QR-algorithm trả về $(R_{k})_{nn} = 0$ (nếu không, lập luận là dễ dàng được điều chỉnh), thì hàng cuối cùng của $R_{k}Q_{k}$ là $0$, do đó hàng cuối cùng của $A_{k+1} = R_{k}Q_{k} + \sigma_{k}$ I kết thúc với $\sigma_{k}$ (tất cả khác các phần tử (entries) đang là không), do đó ta là trong trường hợp ở đâu ta có thể deflate $A_{k}$ (và $\sigma_{k}$ là thật vậy trị riêng (eigenvalue)). câu hỏi vẫn còn, những gì là tốt lựa chọn cho shift $\sigma_{k}$? Giả sử một lần nữa rằng $H$ là trong trên Hessenberg tạo thành, hóa ra là khi $(H_{k})_{nn-1}$ là nhỏ đủ, thì tốt lựa chọn cho $\sigma_{k}$ là $(H_{k})_{nn}$. Thực ra, tốc độ của sự hội tụ là toàn phương, mà có nghĩa là xấp xỉ/đại khái rằng số của đúng digits các gấp đôi tại mọi vòng lặp. lý do là rằng shifts là related đến một cái khác phương pháp đã biết như nghịch đảo vòng lặp, và như vậy phương pháp hội tụ rất fast. Cho further explanations về điều này connection, xem Demmel $[48]$ (Mục 4.4.4) và Trefethen và Bau $[182]$ (Lecture $29)$. Một nên vẫn là cautious rằng QR phương pháp với shifts thực hiện không nhất thiết hội tụ, và rằng của ta sự hội tụ chứng minh không có dài hơn áp dụng, bởi vì thay vì của có đồng nhất thức $A^{k} = P_{k}\mathcal{R}_{k}$, ta có
$$(A -\sigma_{k} I) \cdots  (A -\sigma_{2} I)(A -\sigma_{1} I) = P_{k}\mathcal{R}_{k}.$$
Của course, QR thuật toán các khuyên ngay lập tức khi ứng dụng đến ma trận trực giao (orthogonal matrix) $A$. Điều này là cũng trường hợp khi $A$ là đối xứng nhưng không xác định dương (positive definite). Ví dụ, cả hai QR thuật toán và QR thuật toán với shifts khuyên trên ma trận
$$A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} .$$
Trong trường hợp của các ma trận đối xứng, Wilkinson invented shift mà helps QR thuật toán với shifts để tạo progress. Một lần nữa, nhìn tại thấp hơn góc của $A_{k}$, nói
$$B = \begin{pmatrix} a_{n-1} & b_{n-1} \\ b_{n-1} & a_{n} \end{pmatrix} ,$$
Wilkinson shift chọn trị riêng (eigenvalue) của $B$ closer đến $a_{n}$. Nếu ta cho
$$-$$
$$\delta  = \frac{a_{n-1}a_{n}}{2} ,$$
Nó là dễ để xem rằng các trị riêng (eigenvalues) của $B$ được cho bởi
$$q$$
$$\lambda  = \frac{a_{n} + a_{n-1}}{2} \pm \delta^{2}  + b_{n-1}^{2}.$$

<!-- PAGE 678 -->
Suy ra rằng
$$q$$
$$\lambda  -a_{n} = \delta  \pm \delta^{2} + b_{n-1}^{2},$$
Và từ điều này nó là dễ để xem rằng trị riêng (eigenvalue) closer đến $a_{n}$ được cho bởi
$$\mu  = a_{n} - \frac{sign(\delta )b_{n-1}^{2}}{(|\delta | +p\overline{\delta}^{2}\overline{+}\overline{b}_{n-1}^{2})} .$$
Nếu $\delta  = 0$, thì ta chọn arbitrarily một của hai các trị riêng (eigenvalues). Nhận thấy rằng Wilkinson shift ứng dụng đến ma trận
$$A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$
Là hoặc $+1$ hoặc $-1$, và trong một bước, deflation xảy ra và thuật toán kết thúc successfully. Ta bây giờ thảo luận gấp đôi shifts, mà là intended đến deal với các cặp của phức liên hợp các trị riêng (eigenvalues). Ta giả sử rằng $A$ là thực ma trận. Với mọi phức số $\sigma_{k}$ với khác không imaginary phần, gấp đôi shift bao gồm của sau đây các bước:
$$A_{k} -\sigma_{k} I = Q_{k}R_{k}$$
$$A_{k+1} = R_{k}Q_{k} + \sigma_{k} I$$
$$A_{k+1} -\overline{\sigma}_{k}I = Q_{k+1}R_{k+1}$$
$$A_{k+2} = R_{k+1}Q_{k+1} +\overline{\sigma}_{k}I.$$
Từ phép tính được tạo cho đơn lẻ shift, ta có $A_{k+1} = Q_{k}^{*}A_{k}Q_{k}$ và $A_{k+2} = Q_{k+1}^{*}A_{k+1}Q_{k+1}$, do đó ta thu được
$$A_{k+2} = Q_{k+1}^{*}Q_{k}^{*}A_{k}Q_{k}Q_{k+1}.$$
Các ma trận $Q_{k}$ là phức, do đó ta sẽ kỳ vọng rằng $A_{k}$ là cũng phức, nhưng đáng chú ý ta có thể giữ các tích $Q_{k}Q_{k+1}$ thực, và do đó $A_{k}$ cũng thực. Điều này là một cách cao desirable để tránh phức arithmetic, mà là nhiều hơn/thêm expensive. Nhận thấy rằng vì
$$Q_{k+1}R_{k+1} = A_{k+1} -\overline{\sigma}_{k}I = R_{k}Q_{k} + (\sigma_{k}  -\overline{\sigma}_{k})I,$$
Ta có
$$Q_{k}Q_{k+1}R_{k+1}R_{k} = Q_{k}(R_{k}Q_{k} + (\sigma_{k}  -\overline{\sigma}_{k})I)R_{k}$$
$$= Q_{k}R_{k}Q_{k}R_{k} + (\sigma_{k}  -\overline{\sigma}_{k})Q_{k}R_{k}$$
$$= (A_{k} -\sigma_{k} I)^{2}+ (\sigma_{k}  -\overline{\sigma}_{k})(A_{k} -\sigma_{k} I)$$
$$= A_{k}^{2} -2(\mathcal{ℜ}\sigma_{k} )A_{k} + |\sigma_{k} |^{2}I.$$

<!-- PAGE 679 -->
Nếu ta giả sử bởi quy nạp rằng ma trận $A_{k}$ là thực (với $k = 2\ell +1, \ell \ge 0)$, thì ma trận $S = A_{k}^{2}$ - $2(\mathcal{ℜ}\sigma_{k} )A_{k} + |\sigma_{k} |^{2}I$ là cũng thực, và vì $Q_{k}Q_{k+1}$ là unita và $R_{k+1}R_{k}$ là tam giác trên (upper triangular), ta xem rằng
$$S = Q_{k}Q_{k+1}R_{k+1}R_{k}$$
Là Nhân tử hóa QR (QR-factorization) của thực ma trận $S$, do đó $Q_{k}Q_{k+1}$ và $R_{k+1}R_{k}$ có thể được được chọn là thực các ma trận, trong mà trường hợp $(Q_{k}Q_{k+1})^{*}$ là cũng thực, và do đó
$$A_{k+2} = Q_{k+1}^{*}Q_{k}^{*}A_{k}Q_{k}Q_{k+1} = (Q_{k}Q_{k+1})^{*}A_{k}Q_{k}Q_{k+1}$$
Là thực. Hệ quả là, nếu $A_{1} = A$ là thực, thì $A_{2\ell+1}$ là thực với mọi $\ell \ge 0$. chiến lược rằng bao gồm trong chọn $\sigma_{k}$ và $\overline{\sigma}_{k}$ như phức liên hợp các trị riêng (eigenvalues) của góc khối
$$\begin{pmatrix} (H_{k})_{n-1n-1} & (H_{k})_{n-1n} \\ (H_{k})_{nn-1} & (H_{k})_{nn} \end{pmatrix}$$
Được gọi là Francis shift (ở đây ta là giả sử rằng $A$ có là rút gọn đến trên Hessenberg tạo thành). Nó nên được lưu ý rằng có các ma trận cho mà không shift bởi $(H_{k})_{nn}$ cũng không Francis shift hoạt động. Chẳng hạn, hoán vị ma trận
$$A = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$$
Có các trị riêng (eigenvalues) $e^{i2\pi /3}, e^{i4\pi /3}, +1$, và không của ở trên shifts áp dụng đến ma trận
$$\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} .$$
Tuy nhiên, shift bởi $1$ thực hiện hoạt động/công trình. Có khác các loại của các ma trận cho mà QR thuật toán thực hiện không hội tụ. Demmel cho ví dụ của các ma trận của tạo thành
$$\begin{pmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & h & 0 \\ 0 & -h & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$
Ở đâu $h$ là nhỏ. Các thuật toán cài đặt QR thuật toán với shifts và gấp đôi shifts perform “exceptional” shifts mọi $10$ shifts. Despite sự kiện rằng QR thuật toán có đã được perfected vì 1960’s, nó là vẫn mở bài toán để tìm shift chiến lược rằng các đảm bảo sự hội tụ của tất cả các ma trận. Ẩn shifting là based trên kết quả đã biết như ẩn $Q$ định lý. định lý này nói rằng rằng nếu $A$ là rút gọn đến trên Hessenberg tạo thành như $A = UHU^{*}$ và nếu $H$ là unreduced
