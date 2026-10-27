# Sự hội tụ của Các phương pháp lặp


<!-- PAGE 392 -->

## 10.2 Sự hội tụ của Các phương pháp lặp

Nhắc lại rằng các phương pháp lặp cho việc giải hệ phương trình tuyến tính Ax $= b$ (với $A \in M_{n}(\mathbb{C})$ khả nghịch) bao gồm trong việc tìm một số ma trận $B$ và một số vectơ $c$, sao cho I - $B$ là khả nghịch, và duy nhất nghiệm $x$ của Ax $= b$ bằng duy nhất nghiệm $u$ của $u =$ Bu $+ c$. Thì bắt đầu
$$e e$$
Từ bất kỳ vectơ $u_{0}$, tính dãy $(u_{k})$ cho trước bởi
$$u_{k+1} = Bu_{k} + c,k \in \mathbb{N},$$
Và nói rằng phương pháp lặp (iterative method) là convergent khi và chỉ khi
$$limu_{k} =u,$$
$$k\mapsto \infty  e$$
Với mọi ban đầu vectơ $u_{0}$. Ở đây là cơ bản tiêu chuẩn cho sự hội tụ của bất kỳ các phương pháp lặp based trên ma trận $B$, được gọi là ma trận của phương pháp lặp (iterative method).

> **Định lý 10.3.** Cho trước hệ $u = Bu+c$ như ở trên, ở đâu I $-B$ là khả nghịch, sau đây các phát biểu là tương đương:
$(1)$ phương pháp lặp (iterative method) là convergent.
$(2) \rho (B) < 1$.
$(3) \|B\| < 1$, với một số chuẩn ma trận phụ thuộc (subordinate matrix norm) $\|\|$.

*Chứng minh.* Định nghĩa vectơ $e_{k}$ (sai số vectơ) bởi
$$e_{k} = u_{k} -u,$$
$$e$$
Ở đâu $u$ là duy nhất nghiệm của hệ $u =$ Bu $+ c$. Rõ ràng, phương pháp lặp (iterative method) là $e$ convergent khi và chỉ khi
$$lime_{k} = 0.$$
$$k\mapsto \infty$$
Ta khẳng định rằng
$$e_{k} = B^{k}e_{0},k \ge 0,$$
Ở đâu $e_{0} = u_{0}$ - $u$.
$$e$$
Điều này được chứng minh bằng quy nạp theo $k$. base trường hợp $k = 0$ là tầm thường. Theo giả thiết quy nạp, $e_{k} = B^{k}e_{0}$, và vì $u_{k+1} = Bu_{k} + c$, ta thu được
$$u_{k+1} -u = Bu_{k} + c -u,$$
$$ee$$
Và bởi vì $u =$ Bu $+ c$ và $e_{k} = B^{k}e_{0}$ (theo giả thiết quy nạp), ta thu được
$$ee$$
$$u_{k+1} -u = Bu_{k} -Bu = B(u_{k} -u) = Be_{k} = BB^{k}e_{0} = B^{k+1}e_{0},$$
$$eee$$
Chứng minh quy nạp bước. Do đó, phương pháp lặp (iterative method) hội tụ khi và chỉ khi
$$limB^{k}e_{0} = 0.$$
$$k\mapsto \infty$$
Hệ quả là, định lý của chúng ta suy ra theo Định lý 10.1.

<!-- PAGE 393 -->
Tiếp theo mệnh đề là cần thiết đến compare tốc độ của sự hội tụ của các phương pháp lặp. Nó chỉ ra rằng asymptotically, sai số vectơ $e_{k} = B^{k}e_{0}$ behaves tại worst like $(\rho (B))^{k}$.

> **Mệnh đề 10.4.** Cho $\|\|$ là bất kỳ chuẩn vectơ (vector norm), cho $B \in M_{n}(\mathbb{C})$ là ma trận sao cho I - $B$ là khả nghịch, và cho $u$ là duy nhất nghiệm của $u =$ Bu $+ c$.
$$e$$
$(1)$ Nếu $(u_{k})$ là bất kỳ dãy được định nghĩa một cách lặp bởi
$$u_{k+1} = Bu_{k} + c,k \in \mathbb{N},$$
Thì
$$$$
$$limsup\|u_{k} -u\|^{1/k}= \rho (B).$$
$$k\mapsto \infty e$$
$$\|u0-u\|=1$$
$$e$$
$(2)$ Cho $B_{1}$ và $B_{2}$ là hai các ma trận sao cho I - $B_{1}$ và I - $B_{2}$ là khả nghịch, giả sử rằng cả hai $u = B_{1}u + c_{1}$ và $u = B_{2}u + c_{2}$ có cùng duy nhất nghiệm $u$, và xét bất kỳ
$$e$$
Hai các dãy $(u_{k})$ và $(v_{k})$ được định nghĩa một cách quy nạp bởi
$$u_{k+1} = B_{1}u_{k} + c_{1}$$
$$v_{k+1} = B_{2}v_{k} + c_{2},$$
Với $u_{0} = v_{0}$. Nếu $\rho (B_{1}) < \rho (B_{2})$, thì với mọi $\epsilon  > 0$, tồn tại một số nguyên $N(\epsilon$), sao cho với mọi $k \ge N(\epsilon$), ta có
$$\| -\|^{1/k}$$
$$\sup \frac{v_{k}u}{\|u_{k} -ue\|} e\ge \frac{\rho (B_{2})}{\rho (B_{1}) + \epsilon} .$$
$$\|u0-u\|=1$$
$$e$$

*Chứng minh.* Cho $\|\|$ là chuẩn ma trận phụ thuộc (subordinate matrix norm). Nhắc lại rằng
$$u_{k} -u = B^{k}e_{0},$$
$$e$$
Với $e_{0} = u_{0}$ - $u$. Với mọi $k \in \mathbb{N}$, ta có
$$e$$
$$(\rho (B))^{k}= \rho (B^{k}) \le \|B^{k}\|= \sup\|B^{k}e_{0}\|,$$
$$\|e0\|=1$$
Mà suy ra
$$\rho (B) = \sup\|B^{k}e_{0}\|^{1/k}= \|B^{k}\|^{1/k},$$
$$\|e0\|=1$$
Và Phát biểu $(1)$ suy ra từ Mệnh đề 10.2. Bởi vì $u_{0} = v_{0}$, ta có
$$u_{k} -u = B_{1}^{k}e_{0}$$
$$e$$
$$v_{k} -u = B_{2}^{k}e_{0},$$
$$e$$
