# Sự hội tụ của Các phương pháp


<!-- PAGE 402 -->
$2$. Tìm nếu ở đó tồn tại một số giá trị tối ưu (optimal value) $\omega_{0}$ của $\omega  \in$ I, sao cho
$$\rho (\mathcal{L}_{\omega0}) = \inf \rho (\mathcal{L}_{\omega}).$$
$$\omega \in I$$
Ta sẽ cho riêng các câu trả lời đến ở trên các câu hỏi trong mục tiếp theo. Nó là cũng khả dĩ/có thể để mở rộng các phương pháp của điều này mục bằng cách sử dụng khối các phân rã của tạo thành $A = D$ - $E$ - $F$, ở đâu $D, E$, và $F$ bao gồm của các khối, và $D$ là khả nghịch khối-ma trận đường chéo (diagonal matrix). Xem Hình 10.1.
$$DF$$
$$11$$
$$DF$$
$$22$$
$$EDF$$
$$133$$
$$E$$
$$2$$
$$D$$
$$E4$$
$$3$$

![Figure 10.1](../../assets/ch10/fig_10_1.png)

**Hình 10.1:** schematic biểu diễn của khối phân rã $A = D$ - $E$ - $F$, ở đâu $D = \cup_{i=1}^{4} D_{i}, E = \cup_{i=1}^{3} E_{i}$, và $F = \cup_{i=1}^{3} F_{i}$.

## 10.4 Sự hội tụ của Các phương pháp của Gauss–Seidel và

$$Relaxation$$
Ta bắt đầu với tổng quát tiêu chuẩn cho sự hội tụ của phương pháp lặp (iterative method) liên kết với (phức) Hermite xác định dương (positive definite) ma trận, $A = M$ - $N$. Tiếp theo ta áp dụng kết quả này đến phương pháp nới lỏng (relaxation method).

> **Mệnh đề 10.5.** Cho $A$ là bất kỳ Hermite xác định dương (positive definite) ma trận, được viết như
$$A = M -N,$$
Với $M$ khả nghịch. Thì $M^{*} + N$ là Hermite, và nếu nó là xác định dương (positive definite), thì
$$\rho (M^{-1} N) < 1,$$
Sao cho phương pháp lặp (iterative method) hội tụ.

<!-- PAGE 403 -->

*Chứng minh.* Vì $M = A + N$ và $A$ là Hermite, $A^{*} = A$, do đó ta thu được
$$M^{*} + N = A^{*}+ N^{*} + N = A + N + N^{*} = M + N^{*} = (M^{*} + N)^{*},$$
Mà chỉ ra rằng $M^{*} + N$ là thật vậy Hermite. Bởi vì $A$ là Hermite xác định dương (positive definite), hàm
$$v \mapsto (v^{*}Av)^{1/2}$$
$\mathbb{C}^{n}  \mathbb{R}$ từ đến là chuẩn vectơ (vector norm) $\|\|$, và cho $\|\|$ cũng ký hiệu của nó chuẩn ma trận phụ thuộc (subordinate matrix norm). Ta chứng minh rằng
$$\|M^{-1} N\|< 1,$$
Mà theo Định lý 10.1 chứng tỏ rằng $\rho (M^{-1} N) < 1$. Theo Định nghĩa
$$\|M^{-1} N\|= \|I -M^{-1} A\|= \sup\|v -M^{-1} Av\|,$$
$$\|v\|=1$$
Mà dẫn đến chúng ta đến tính giá trị $\|v$ - $M^{-1} Av\|$ khi $\|v\| = 1$. Nếu ta viết $w = M^{-1}$ Av, bằng cách sử dụng các sự kiện rằng $\|v\| = 1, v = A^{-1}Mw, A^{*} = A$, và $A = M$ - $N$, ta có
$$\|v -w\|^{2}= (v -w)^{*}A(v -w)$$
$$= \|v\|^{2}-v^{*}Aw -w^{*}Av + w^{*}Aw$$
$$= 1 -w^{*}M^{*} w -w^{*}Mw + w^{*}Aw$$
$$= 1 -w^{*}(M^{*} + N)w.$$
Bây giờ vì ta được giả sử rằng $M^{*} + N$ là xác định dương (positive definite), nếu $w \neq  0$, thì $w^{*}(M^{*} +$ N)w $> 0$, và ta kết luận rằng
$$if\|v\|= 1,then\|v -M^{-1} Av\|< 1.$$
Cuối cùng, hàm
$$v \mapsto \|v -M^{-1} Av\|$$
Là liên tục như hợp thành của liên tục các hàm, vì vậy nó đạt được của nó cực đại
$$\mathbb{C}^{n}$$
Trên compắc tập con ${v \in$ | $\|v\| = 1}$, mà chứng tỏ rằng
$$\sup\|v -M^{-1} Av\|< 1,$$
$$\|v\|=1$$
Và các đầy đủ chứng minh. Bây giờ như trong trước đó các mục, ta giả sử rằng $A$ được viết như $A = D$ - $E$ - $F$, với $D$ khả nghịch, có thể trong khối tạo thành. tiếp theo định lý cung cấp đủ điều kiện (mà hóa ra là cũng cần) cho phương pháp nới lỏng (relaxation method) đến hội tụ (và do đó, cho phương pháp của Gauss–Seidel đến hội tụ). định lý này là đã biết như Ostrowski-Reich định lý.

<!-- PAGE 404 -->

> **Định lý 10.6.** Nếu $A = D$ - $E$ - $F$ là Hermite xác định dương (positive definite), và nếu $0 < \omega  < 2$, thì phương pháp nới lỏng (relaxation method) hội tụ. Điều này cũng nghiệm đúng cho khối phân rã của $A$.

*Chứng minh.* Nhắc lại rằng cho phương pháp nới lỏng (relaxation method), $A = M$ - $N$ với
$$M = \frac{D}{\omega} -E$$
$$-$$
$$N = \frac{1\omega}{\omega} D + F,$$
Và bởi vì $D^{*} = D, E^{*} = F$ (vì $A$ là Hermite) và $\omega  \neq  0$ là thực, ta có
$$-  -$$
$$M^{*} + N = \frac{D^{*}}{\omega} -E^{*}+ \frac{1\omega}{\omega} D + F = \frac{2\omega}{\omega} D.$$
Nếu $D$ bao gồm của đường chéo các phần tử (entries) của $A$, thì ta biết từ Mục 8.8 rằng các phần tử (các phần tử (entries)) này là tất cả dương, và vì $\omega  \in (0, 2)$, ta xem rằng ma trận $((2-\omega )/\omega )D$ là xác định dương (positive definite). Nếu $D$ bao gồm của đường chéo các khối của $A$, bởi vì $A$ là dương, xác định, bằng cách chọn các vectơ $z$ thu được bởi chọn khác không vectơ với mỗi khối của $D$ và padding với các không điểm, ta xem rằng mỗi khối của $D$ là xác định dương (positive definite), và do đó $D$ chính nó là xác định dương (positive definite). Vì vậy, trong tất cả các trường hợp, $M^{*} + N$ là xác định dương (positive definite), và ta kết luận bằng cách sử dụng Mệnh đề 10.5.
Nhận xét: Những gì nếu ta cho phép tham số $\omega$ là khác không phức số $\omega  \in \mathbb{C}$? Trong trường hợp này, ta thu được
$$-$$
$$M^{*} + N = \frac{D^{*}}{\overline{\omega}} -E^{*}+ \frac{1\omega}{\omega} D + F = \begin{pmatrix} 1 \\ 1 \\ + & -1 \\ \omega & \overline{\omega} \end{pmatrix} D.$$
Nhưng,
$$-  - - -  -| -|^{2}$$
$$\frac{1}{\omega} + \frac{1}{\overline{\omega}} -1 = \frac{\omega  +\overline{\omega}\overline{\omega \omega}}{\overline{\omega \omega}} = \frac{1(\omega 1)(\overline{\omega} 1)}{|\omega |^{2}} = \frac{1\omega 1}{|\omega |^{2}} ,$$
Do đó phương pháp nới lỏng (relaxation method) cũng hội tụ cho $\omega  \in \mathbb{C}$, miễn là/được cung cấp rằng
$$|\omega  -1| < 1.$$
Điều kiện này rút gọn đến $0 < \omega  < 2$ nếu $\omega$ là thực. Không may là, Định lý 10.6 thực hiện không áp dụng đến Jacobi’s phương pháp, nhưng trong đặc biệt các trường hợp, Mệnh đề 10.5 có thể được được sử dụng để chứng minh của nó sự hội tụ. Trên dương vế/cạnh, nếu ma trận là chặt cột (hoặc hàng) một cách đường chéo trội, thì nó có thể được được hiển thị rằng phương pháp của Jacobi và phương pháp của Gauss–Seidel cả hai hội tụ. phương pháp nới lỏng (relaxation method) cũng hội tụ nếu $\omega  \in (0, 1]$, nhưng điều này là không rất hữu ích kết quả bởi vì speed-up của sự hội tụ thường xảy ra cho $\omega  > 1$. Ta bây giờ chứng minh rằng, mà không có bất kỳ giả định trên $A = D$ - $E$ - $F$, ngoài sự kiện rằng $A$ và $D$ là khả nghịch, trong thứ tự cho phương pháp nới lỏng (relaxation method) đến hội tụ, ta phải có $\omega  \in (0, 2)$.
