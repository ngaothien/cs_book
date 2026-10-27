# Sự hội tụ của Các dãy của Các vectơ và Các ma trận


<!-- PAGE 389 -->
Chương $10$ Các phương pháp lặp cho Việc giải Các hệ phương trình tuyến tính

## 10.1 Sự hội tụ của Các dãy của Các vectơ và Matri-

$$ces$$
Trong Chương $8$ ta được thảo luận một số của chính các phương pháp cho việc giải các hệ của các phương trình tuyến tính. các phương pháp này là trực tiếp các phương pháp, trong nghĩa rằng chúng cho chính xác các nghiệm (giả sử vô hạn precision!). Một cái khác lớp của các phương pháp cho việc giải các hệ phương trình tuyến tính bao gồm trong approximating các nghiệm bằng cách sử dụng các phương pháp lặp. cơ bản ý tưởng là điều này: Cho trước hệ phương trình tuyến tính Ax $= b$ (với $A$ square ma trận khả nghịch (invertible matrix) trong $M_{n}(\mathbb{C}))$, tìm một cái khác ma trận $B \in M_{n}(\mathbb{C})$ và vectơ $c \in \mathbb{C}^{n}$, sao cho $1$. ma trận $I$ - $B$ là khả nghịch $2$. duy nhất nghiệm $x$ của hệ Ax $= b$ là đồng nhất đến duy nhất nghiệm $u$ của
$$e e$$
Hệ
$$u = Bu + c,$$
Và thì bắt đầu từ bất kỳ vectơ $u_{0}$, tính dãy $(u_{k})$ cho trước bởi
$$u_{k+1} = Bu_{k} + c,k \in \mathbb{N}.$$
Dưới nhất định các điều kiện (là clarified soon), dãy $(u_{k})$ hội tụ đến giới hạn $u$
$$e$$
Mà là duy nhất nghiệm của $u =$ Bu $+ c$, và do đó của Ax $= b$. Hệ quả là, nó là quan trọng để tìm các điều kiện rằng đảm bảo sự hội tụ của ở trên các dãy và đến có các công cụ đến compare “tốc độ” của sự hội tụ của các phần tử này các dãy. Do đó, ta bắt đầu với một số tổng quát các kết quả về sự hội tụ của các dãy của các vectơ và các ma trận.
$$389$$

<!-- PAGE 390 -->
Cho $(E, \|\|)$ là không gian vectơ định chuẩn (normed vector space). Nhắc lại từ Mục 9.7 rằng dãy $(u_{k})$ của các vectơ $u_{k} \in E$ hội tụ đến giới hạn $u \in E$, nếu với mọi $\epsilon  > 0$, ở đó một số tự nhiên số $N$ sao cho
$$\|u_{k} -u\|\le \epsilon ,for all k \ge N.$$
Ta viết
$$u = limu_{k}.$$
$$k\mapsto \infty$$
Nếu $E$ là không gian vectơ hữu hạn chiều và dim(E) $= n$, ta biết từ Định lý 9.6 rằng bất kỳ hai các chuẩn là tương đương, và nếu ta chọn chuẩn (norm) $\|\|_{\infty}$, ta xem rằng sự hội tụ của dãy của các vectơ $u_{k}$ là tương đương đến sự hội tụ của $n$ các dãy của các vô hướng được tạo thành bởi các thành phần của các vectơ này (trên bất kỳ cơ sở (basis)). cùng tính chất áp dụng đến không gian vectơ hữu hạn chiều $M_{m,n}(K)$ của $m \times  n$ các ma trận (với $K = \mathbb{R}$ hoặc $K = \mathbb{C})$, mà có nghĩa là sự hội tụ của dãy của các ma trận $A_{k} = (a_{ij}^{(k)}$) là tương đương đến sự hội tụ của $m \times  n$ các dãy của các vô hướng $(a_{ij}^{(k)}$), với $i, j$ cố định $(1 \le i \le m, 1 \le j \le n)$. thứ nhất định lý ở dưới cho cần và đủ điều kiện cho dãy $(B^{k})$ của các lũy thừa của ma trận $B$ đến hội tụ đến không ma trận. Nhắc lại rằng bán kính phổ (spectral radius) $\rho (B)$ của ma trận $B$ là cực đại của moduli $|\lambda_{i}$ | của các trị riêng (eigenvalues) của $B$.

> **Định lý 10.1.** Với mọi ma trận vuông (square matrix) $B$, các điều kiện sau đây là tương đương:
$(1) lim_{k\mapsto \infty} B^{k} = 0$,
$(2) lim_{k\mapsto \infty} B^{k}v = 0$, với mọi các vectơ $v$,
$(3) \rho (B) < 1$,
$(4) \|B\| < 1$, với một số chuẩn ma trận phụ thuộc (subordinate matrix norm) $\|\|$.

*Chứng minh.* Giả sử $(1)$ và cho $\|\|$ là chuẩn vectơ (vector norm) trên $E$ và $\|\|$ là tương ứng chuẩn ma trận (matrix norm). Với mọi vectơ $v \in E$, bởi vì $\|\|$ là chuẩn ma trận (matrix norm), ta có
$$\|B^{k}v\|\le \|B^{k}\|\|v\|,$$
Và vì $lim_{k\mapsto \infty} B^{k} = 0$ có nghĩa là $lim_{k\mapsto \infty} \|B^{k}\| = 0$, ta kết luận rằng $lim_{k\mapsto \infty} \|B^{k}v\| = 0$, nghĩa là, $lim_{k\mapsto \infty} B^{k}v = 0$. Điều này chứng tỏ rằng $(1)$ suy ra $(2)$. Giả sử $(2)$. Nếu ta đã có $\rho (B) \ge 1$, thì ở đó sẽ là một số vectơ riêng (eigenvector) $u(\neq  0)$ và một số trị riêng (eigenvalue) $\lambda$ sao cho
$$Bu = \lambda u,|\lambda | = \rho (B) \ge 1,$$
Nhưng khi đó dãy $(B^{k}u)$ sẽ không hội tụ đến $0$, bởi vì $B^{k}u = \lambda^{k} u$ và $|\lambda^{k}$ | $= |\lambda |^{k} \ge 1$. Suy ra rằng $(2)$ suy ra $(3)$. Giả sử rằng $(3)$ nghiệm đúng, nghĩa là, $\rho (B) < 1$. Theo Mệnh đề 9.13, ta có thể tìm $\epsilon  > 0$ nhỏ đủ rằng $\rho (B) + \epsilon  < 1$, và chuẩn ma trận phụ thuộc (subordinate matrix norm) $\|\|$ sao cho
$$\|B\|\le \rho (B) + \epsilon ,$$

<!-- PAGE 391 -->
Mà là $(4)$. Cuối cùng, giả sử $(4)$. Bởi vì $\|\|$ là chuẩn ma trận (matrix norm),
$$\|B^{k}\|\le \|B\|^{k},$$
Và vì $\|B\| < 1$, ta suy ra rằng $(1)$ nghiệm đúng. sau đây mệnh đề là cần thiết đến study tốc độ của sự hội tụ của các phương pháp lặp.

> **Mệnh đề 10.2.** Với mọi ma trận vuông (square matrix) $B \in M_{n}(\mathbb{C})$ và mọi chuẩn ma trận (matrix norm) $\|\|$, ta có
$$lim\|B^{k}\|^{1/k}= \rho (B).$$
$$k\mapsto \infty$$

*Chứng minh.* Ta biết từ Mệnh đề 9.7 rằng $\rho (B) \le \|B\|$, và vì $\rho (B) = (\rho (B^{k}))^{1/k}$, ta suy ra rằng
$$\rho (B) \le \|B^{k}\|^{1/k}for all k \ge 1.$$
Bây giờ cho chúng ta chứng minh rằng với mọi $\epsilon  > 0$, tồn tại một số nguyên $N(\epsilon$) sao cho
$$\|B^{k}\|^{1/k}\le \rho (B) + \epsilon for all k \ge N(\epsilon ).$$
Cùng với sự kiện rằng
$$\rho (B) \le \|B^{k}\|^{1/k}for all k \ge 1,$$
Ta suy ra rằng $lim_{k\mapsto \infty} \|B^{k}\|^{1/k}$ tồn tại và rằng
$$lim\|B^{k}\|^{1/k}= \rho (B).$$
$$k\mapsto \infty$$
Với mọi cho trước $\epsilon  > 0$, cho $B_{\epsilon}$ là ma trận
$$B_{\epsilon} = \frac{B}{\rho (B) + \epsilon} .$$
Vì $\rho (B_{\epsilon}) < 1$, Định lý 10.1 suy ra rằng $lim_{k\mapsto \infty} B_{\epsilon}^{k} = 0$. Hệ quả là, tồn tại một số nguyên $N(\epsilon$) sao cho với mọi $k \ge N(\epsilon$), ta có
$$\|\|$$
$$\|B_{\epsilon}^{k} \|= \frac{B^{k}}{(\rho (B) + \epsilon )^{k}} \le 1,$$
Mà suy ra rằng
$$\|B^{k}\|^{1/k}\le \rho (B) + \epsilon ,$$
Như đã khẳng định. Ta bây giờ áp dụng ở trên các kết quả đến sự hội tụ của các phương pháp lặp.
