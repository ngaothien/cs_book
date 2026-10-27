# Không gian Hilbert (Hilbert space) 2(K) và Riesz–Fischer Định lý


<!-- PAGE 2158 -->
Với mọi hữu hạn tập con I của $K$, ta thu được
$$\|u -v\|\le u - \sum_{i\in I}  c_{i}u_{i} + \sum_{i\in I}  c_{i}u_{i} -v$$
$$\le u - \sum_{i\in I}  c_{i}u_{i} + \sum_{i\in I}  \lambda_{i} u_{i} -v$$
$$\le u - \sum_{i\in I}  c_{i}u_{i} + \|v -w\|+w - \sum_{i\in I}  \lambda_{i} u_{i},$$
Và do đó
$$\|u -v\|\le \|v -w\|+ 2\epsilon .$$
Vì điều này nghiệm đúng với mọi $\epsilon  > 0$, ta có
$$\|u -v\|\le \|v -w\|$$
Với mọi $w \in V$, i.e. $\|v$ - $u\| =$ d(v, $V$), với $u \in V$, mà chứng tỏ rằng $u = p_{V} (v)$.

## .2 Không gian Hilbert (Hilbert space) \ell 2(K) và Riesz–Fischer

$$Theorem$$
Mệnh đề.2 suggests nhìn tại không gian của các dãy $(z_{k})_{k\in K}$ (ở đâu $z_{k} \in \mathbb{C})$ sao cho $(|z_{k}|^{2})_{k\in K}$ là khả tổng. Thật vậy, như vậy các không gian là Các không gian Hilbert, và hóa ra là mọi Không gian Hilbert (Hilbert space) là đẳng cấu đến một của những phần tử đó. Như vậy các không gian là vô hạn chiều phiên bản
$$\mathbb{C}^{n}$$
Của các không gian dưới thông thường Euclidean chuẩn (norm).

> **Định nghĩa A.3.** Cho trước bất kỳ khác rỗng chỉ số tập hợp $K$, không gian $\ell (K)$ là tập hợp tất cả các dãy
$$\mathbb{C}$$
$$(z_{k})_{k\in K}, where z_{k} \in , such that (|z_{k}|^{2})_{k\in K} is summable, i.e., \sum_{k}^{2}  \in K |z_{k}|^{2}< \infty .$$
Các nhận xét:
$(1)$ Khi $K$ là hữu hạn tập hợp của cardinality $n, \ell^{2} (K)$ là đẳng cấu đến $\mathbb{C}^{n}$.
$$\mathbb{N}\mathbb{N}$$
$(2)$ Khi $K =$, không gian $\ell^{2}$ () tương ứng với không gian $\ell^{2}$ của Ví dụ $2$ trong Mục 14.1. Trong rằng ví dụ, ta được khẳng định rằng $\ell^{2}$ đã là Không gian Hermite (Hermitian space), và thực ra, Không gian Hilbert (Hilbert space). Ta bây giờ chứng minh sự kiện này với mọi chỉ số tập hợp $K$.

> **Mệnh đề A.3.** Cho trước bất kỳ khác rỗng chỉ số tập hợp $K$, không gian $\ell^{2} (K)$ là Không gian Hilbert (Hilbert space) dưới Hermite tích
$$\langle (x_{k})_{k\in K}, (y_{k})_{k\in K}\rangle = \sum_{k\in K}  x_{k}\overline{y}_{k}.$$
Không gian con bao gồm của các dãy $(z_{k})_{k\in K}$ sao cho $z_{k} = 0$, ngoại trừ perhaps cho một cách hữu hạn nhiều $k$, là trù mật không gian con của $\ell^{2} (K)$.

<!-- PAGE 2159 -->

*Chứng minh.* Thứ nhất ta cần để chứng minh rằng $\ell^{2} (K)$ là không gian vectơ (vector space). Giả sử rằng $(x_{k})_{k\in K}$ và $(y_{k})_{k\in K}$ là trong $\ell^{2} (K)$. Điều này có nghĩa là $(|x_{k}|^{2})_{k\in K}$ và $(|y_{k}|^{2})_{k\in K}$ là khả tổng, mà, xét theo Mệnh đề.1(2), là tương đương đến sự tồn tại của một số dương các cận $A$ và $B$ như vậy
$$that \sum_{ik}  |x_{i}|^{2}< A and \sum_{i}  |y_{i}|^{2}< B, for every finite subset I of K.To prove that$$
$(|x_{k} + y^{\in I}|^{2})_{k\in K}$ là $summable,^{\in I}$ nó là đủ để chứng minh rằng tồn tại một $C > 0$ sao cho
$$\sum_{i}  \in I |x_{i} + y_{i}|^{2}< C for every finite subset I of K. However, the parallelogram inequality$$
Suy ra rằng
$$\sum_{i\in I}  |x_{i} + y_{i}|^{2}\le \sum_{i\in I}  2(|x_{i}|^{2}+ |y_{i}|^{2}) \le 2(A + B),$$
Với mọi hữu hạn tập con I của $K$, và ta kết luận theo Mệnh đề.1(2). Tương tự, với mọi $\lambda  \in \mathbb{C}$,
$$\sum_{i\in I}  |\lambda x_{i}|^{2}\le \sum_{i\in I}  |\lambda |^{2}|x_{i}|^{2}\le |\lambda |^{2}A,$$
Và $(\lambda_{k} x_{k})_{k\in K}$ là khả tổng. Vì vậy, $\ell^{2} (K)$ là không gian vectơ (vector space). Bởi Cauchy-Schwarz bất đẳng thức,
$$\sum_{i\in I}  |x_{i}\overline{y}_{i}| \le \sum_{i\in I}  |x_{i}||y_{i}| \le \begin{pmatrix} |x_{i} \end{pmatrix} \sum_{i\in I}  |^{21/2} \begin{pmatrix} |xy_{i} \end{pmatrix} \sum_{i\in I}  |^{21/2}\le \sum_{i\in I}  (|x_{i}|^{2}+ |y_{i}|^{2})/2 \le (A + B)/2,$$
Với mọi hữu hạn tập con I của $K$. Cho thứ ba bất đẳng thức ta được sử dụng sự kiện rằng
$$4CD \le (C + D)^{2},$$
$$(with C = \sum_{i}  \in I |x_{i}|^{2}and D = \sum  i\in I |y_{i}|^{2}) which is equivalent to$$
$$(C -D)^{2}\ge 0.$$
Theo Mệnh đề.1(2), $(|x_{k}\overline{y}_{k}|)_{k\in K}$ là khả tổng. thông lệ language là rằng $(x_{k}\overline{y}_{k})_{k\in K}$ là một cách tuyệt đối khả tổng. Tuy nhiên, nó là tiêu chuẩn sự kiện rằng điều này suy ra rằng $(x_{k}\overline{y}_{k})_{k\in K}$ là khả tổng (Với mọi $\epsilon  > 0$, tồn tại một hữu hạn tập con I của $K$ sao cho
$$\sum_{j\in J}  |x_{j}\overline{y}_{j}| < \epsilon$$
Với mọi hữu hạn tập con $J$ của $K$ sao cho I $\cap J = \emptyset$, và do đó
$$| \sum_{j\in J}  x_{j}\overline{y}_{j}| \le \sum_{i\in J}  |x_{j}\overline{y}_{j}| < \epsilon ,$$
Chứng minh rằng $(x_{k}\overline{y}_{k})_{k\in K}$ là Cauchy họ, và do đó khả tổng). Ta vẫn có để chứng minh rằng $\ell^{2} (K)$ là đầy đủ. Xét dãy $((\lambda_{k}^{n} )_{k\in K})_{n\ge1}$ của các dãy $(\lambda_{k}^{n} )_{k\in K} \in \ell^{2} (K)$, và giả sử rằng nó là Dãy Cauchy (Cauchy sequence). Điều này có nghĩa là với mọi $\epsilon  > 0$, tồn tại một $N \ge 1$ sao cho
$$\sum_{k\in K}  |\lambda_{k}^{m}  -\lambda_{k}^{n} |^{2}< \epsilon^{2}$$

<!-- PAGE 2160 -->
Với mọi $m, n \ge N$. Với mọi cố định $k \in K$, điều này suy ra rằng
$$|\lambda_{k}^{m}  -\lambda_{k}^{n} | < \epsilon$$
Với mọi $m, n \ge N$, mà chỉ ra rằng $(\lambda_{k}^{n} )_{n\ge1}$ là Dãy Cauchy (Cauchy sequence) trong $\mathbb{C}$. Vì $\mathbb{C}$ là đầy đủ, dãy $(\lambda_{k}^{n} )_{n\ge1}$ có giới hạn $\lambda_{k}  \in \mathbb{C}$. Ta khẳng định rằng $(\lambda_{k} )_{k\in K} \in \ell^{2} (K)$ và rằng điều này là giới hạn của $((\lambda_{k}^{n} )_{k\in K})_{n\ge1}$. Cho trước bất kỳ $\epsilon  > 0$, sự kiện rằng $((\lambda_{k}^{n} )_{k\in K})_{n\ge1}$ là Dãy Cauchy (Cauchy sequence) suy ra rằng tồn tại một $N \ge 1$ sao cho với mọi hữu hạn tập con I của $K$, ta có
$$\sum_{i\in I}  |\lambda_{i}^{m}  -\lambda_{i}^{n}  |^{2}< \epsilon /4$$
Với mọi $m, n \ge N$. Cho $p =$ |I|. Thì
$$|\lambda_{i}^{m}  -\lambda_{i}^{n}  | < \frac{\sqrt{\epsilon}}{2\overline{p}} \sqrt$$
Với mọi $i \in$ I. Vì $\lambda_{i}$ là giới hạn của $(\lambda_{i}^{n}  )_{n\ge1}$, ta có thể tìm một số $n$ lớn đủ sao cho
$$|\lambda_{i}^{n}  -\lambda_{i} | < \frac{\sqrt{\epsilon}}{2\overline{p}} \sqrt$$
Với mọi $i \in$ I. Vì
$$|\lambda_{i}^{m}  -\lambda_{i} | \le |\lambda_{i}^{m}  -\lambda_{i}^{n}  | + |\lambda_{i}^{n}  -\lambda_{i} |,$$
Ta thu được
$$\sqrt$$
$$\overline{\epsilon}$$
$$|\lambda_{i}^{m}  -\lambda_{i} | <\sqrt p,$$
Và do đó,
$$\sum_{i\in I}  |\lambda_{i}^{m}  -\lambda_{i} |^{2}< \epsilon ,$$
Với mọi $m \ge N$. Vì ở trên nghiệm đúng với mọi hữu hạn tập con I của $K$, theo Mệnh đề.1(2), ta thu được
$$\sum_{k\in K}  |\lambda_{k}^{m}  -\lambda_{k} |^{2}< \epsilon ,$$
Với mọi $m \ge N$. Điều này chứng tỏ rằng $(\lambda_{k}^{m}$ - $\lambda_{k} )_{k\in K} \in \ell^{2} (K)$ với mọi $m \ge N$, và vì $\ell^{2} (K)$ là không gian vectơ (vector space) và $(\lambda_{k}^{m}  )_{k\in K} \in \ell^{2} (K)$ với mọi $m \ge 1$, ta thu được $(\lambda_{k} )_{k\in K} \in \ell^{2} (K)$. Tuy nhiên,
$$\sum_{k\in K}  |\lambda_{k}^{m}  -\lambda_{k} |^{2}< \epsilon$$
Với mọi $m \ge N$, có nghĩa là dãy $(\lambda_{k}^{m}  )_{k\in K}$ hội tụ đến $(\lambda_{k} )_{k\in K} \in \ell^{2} (K)$. sự kiện rằng không gian con bao gồm của các dãy $(z_{k})_{k\in K}$ sao cho $z_{k} = 0$ ngoại trừ perhaps cho một cách hữu hạn nhiều $k$ là trù mật không gian con của $\ell^{2} (K)$ là trái như dễ bài tập.

<!-- PAGE 2161 -->
Nhận xét: không gian con bao gồm của tất cả các dãy $(z_{k})_{k\in K}$ sao cho $z_{k} = 0$, ngoại trừ perhaps cho một cách hữu hạn nhiều $k$, cung cấp ví dụ của không gian con mà là không đóng trong $\ell^{2} (K)$. Thật vậy, không gian này là chặt được chứa trong $\ell^{2} (K)$, vì có đếm được các dãy của khác không các phần tử trong $\ell^{2} (K)$ (tại sao?). Ta chỉ cần hai nhiều hơn/thêm các mệnh đề trước đang là able để chứng minh rằng mọi Không gian Hilbert (Hilbert space) là đẳng cấu đến một số $\ell^{2} (K)$.

> **Mệnh đề A.4.** Cho $E$ là Không gian Hilbert (Hilbert space), và $(u_{k})_{k\in K}$ họ trực giao (orthogonal family) trong $E$. Các tính chất sau đây đúng:
$(1)$ Với mọi họ $(\lambda_{k} )_{k\in K} \in \ell^{2} (K)$, họ $(\lambda_{k} u_{k})_{k\in K}$ là khả tổng. Hơn nữa,
$$v = \sum_{k}  \lambda_{k} u_{k} is the only vector such that c_{k} = \lambda_{k}  for all k \in K, where the c_{k} are the$$
$Fourier^{\in K}$ các hệ số của $v$.
$$(2) For any two families (\lambda_{k} )_{k\in K} \in \ell^{2} (K) and (\mu_{k} )_{k\in K} \in \ell^{2} (K), if v = \sum_{k}  \in K \lambda_{k} u_{k} and$$
$$w = \sum_{k}  \in K \mu_{k} u_{k}, we have the following equation, also called Parseval identity:$$
$$\langle v, w\rangle = \sum_{k\in K}  \lambda_{k} \overline{\mu}_{k}.$$

*Chứng minh.* $(1)$ sự kiện rằng $(\lambda_{k} )_{k\in K} \in \ell^{2} (K)$ có nghĩa là $(|\lambda_{k} |^{2})_{k\in K}$ là khả tổng. chứng minh cho trước trong Mệnh đề.2 $(3)$ áp dụng đến họ $(|\lambda |^{2})_{k\in K}$ (thay vì của $(|c_{k}|^{2})_{k\in K})$, và cho ta
$$the fact that (\lambda_{k} u_{k})_{k\in K} is summable. Letting v = \sum_{k}^{k}  \in K \lambda_{k} u_{k}, recall that c_{k} = \langle v, u_{k}\rangle /\|u_{k}\|^{2}.$$
Chọn một số $k \in K$. Vì $\langle$ -, $-\rangle$ là liên tục, với mọi $\epsilon  > 0$, tồn tại một $\eta  > 0$ sao cho
$$| \langle v, u_{k}\rangle -\langle w, u_{k}\rangle | < \epsilon \|u_{k}\|^{2}$$
Bất cứ khi nào
$$\|v -w\|< \eta .$$
Tuy nhiên, vì với mọi $\eta  > 0$, tồn tại một hữu hạn tập con I của $K$ sao cho
$$v - \sum_{j\in J}  \lambda_{j} u_{j} < \eta$$
Với mọi hữu hạn tập con $J$ của $K$ sao cho $I \subseteq J$, ta có thể chọn $J =$ I $\cup {k}$ và đặt
$$w = \sum_{j}  \in J \lambda_{j} u_{j} we get$$
$$\langle v, u_{k}\rangle -* \sum_{j\in J}  \lambda_{j} u_{j}, u_{k}+




$< \epsilon \|u_{k}\|^{2}.$$$ Tuy nhiên,
$$\langle v, u_{k}\rangle = c_{k}\|u_{k}\|^{2}and* \sum_{j\in J}  \lambda_{j} u_{j}, u_{k}+= \lambda_{k} \|u_{k}\|^{2},$$
Và do đó, ở trên chứng tỏ rằng $|c_{k}$ - $\lambda_{k}$ | $< \epsilon$ với mọi $\epsilon  > 0$, và do đó, rằng $c_{k} = \lambda_{k}$.

<!-- PAGE 2162 -->
$(2)$ Vì $\langle$ -, $-\rangle$ là liên tục, với mọi $\epsilon  > 0$, có một số $\eta_{1}  > 0$ và $\eta_{2}  > 0$, sao cho
$$| \langle x, y\rangle | < \epsilon$$
$$whenever \|x\|< \eta_{1}  and \|y\|< \eta_{2} . Since v = \sum_{k}  \in K \lambda_{k} u_{k} and w = \sum  k\in K \mu_{k} u_{k}, there is some$$
Hữu hạn tập con $I_{1}$ của $K$ sao cho
$$v - \sum_{j\in J}  \lambda_{j} u_{j} < \eta_{1}$$
Với mọi hữu hạn tập con $J$ của $K$ sao cho $I_{1} \subseteq J$, và tồn tại một hữu hạn tập con $I_{2}$ của $K$ sao cho
$$w - \sum_{j\in J}  \mu_{j} u_{j} < \eta_{2}$$
Với mọi hữu hạn tập con $J$ của $K$ sao cho $I_{2} \subseteq J$. Đặt $I = I_{1} \cup I_{2}$, ta thu được
$$*+$$
$$v - \sum_{i\in I}  \lambda_{i} u_{i}, w - \sum_{i\in I}  \mu_{i} u_{i} < \epsilon .$$
Hơn nữa,
$$*+$$
$$\langle v, w\rangle =v - \sum_{i\in I}  \lambda_{i} u_{i} + \sum_{i\in I}  \lambda_{i} u_{i}, w - \sum_{i\in I}  \mu_{i} u_{i} + \sum_{i\in I}  \mu_{i} u_{i}$$
$$*+$$
$$=v - \sum_{i\in I}  \lambda_{i} u_{i}, w - \sum_{i\in I}  \mu_{i} u_{i}+ \sum_{i\in I}  \lambda_{i} \overline{\mu}_{i},$$
$$since the u_{i} are orthogonal to v - \sum_{i}  \lambda_{i} u_{i} and w - \sum_{i}  \mu_{i} u_{i} for all i \in I. This proves that$$
Với mọi $\epsilon  > 0$, tồn tại một $finite^{\in I}$ tập con I của $K such^{\in I}$ rằng
$$\langle v, w\rangle - \sum_{i\in I}  \lambda_{i} \overline{\mu}_{i} < \epsilon .$$
Ta đã biết từ Mệnh đề.3 rằng $(\lambda_{k} \overline{\mu}_{k})_{k\in K}$ là khả tổng, và vì $\epsilon  > 0$ là tùy ý ta thu được
$$\langle v, w\rangle = \sum_{k\in K}  \lambda_{k} \overline{\mu}_{k}.$$
Tiếp theo mệnh đề phát biểu các tính chất đặc trưng hóa Hilbert các cơ sở (tổng trực giao các họ).

> **Mệnh đề A.5.** Cho $E$ là Không gian Hilbert (Hilbert space), và cho $(u_{k})_{k\in K}$ là họ trực giao (orthogonal family) trong $E$. Các tính chất sau đây là tương đương:

<!-- PAGE 2163 -->
$(1)$ họ $(u_{k})_{k\in K}$ là tổng họ trực giao (orthogonal family).
$(2)$ Với mọi vectơ $v \in E$, nếu $(c_{k})$ là Fourier các hệ số của $v$, thì họ
$$(c_{k}u_{k})_{k\in K} is summable and v = \sum_{k}^{k\in K}  \in K c_{k}u_{k}.$$
$(3)$ Với mọi vectơ $v \in E$, ta có Parseval đồng nhất thức:
$$\|v\|^{2}= \sum_{k\in K}  |c_{k}|^{2}.$$
$(4)$ Với mọi vectơ $u \in E$, nếu $\langle u, u_{k}\rangle = 0$ với mọi $k \in K$, thì $u = 0$. Xem Hình.2.
$$v, u$$
$$k$$
$$form c  =$$
$$v=\Sigma_{ckuk} k\overline{2}$$
$$u$$
$$k       Kek$$
$$\overline{E}_{=k}^{V = span(u  )}$$
**Hình A.2:** schematic illustration của Mệnh đề.5. Vì $(u_{k})_{k\in K}$ là Hilbert cơ sở (basis), $V = E$. Thì cho trước vectơ của $E$, nếu ta tạo thành Fourier các hệ số $c_{k}$, thì tạo thành
$$Fourier series \sum_{k}  \in K c_{k}u_{k}, we are ensured that v is equal to its Fourier series.$$

*Chứng minh.* equivalence của $(1), (2)$, và $(3)$ là immediate hệ quả của Mệnh đề.2 và Mệnh đề.4.
$(4)$ Nếu $(u_{k})_{k\in K}$ là tổng họ trực giao (orthogonal family) và $\langle u, u_{k}\rangle = 0$ với mọi $k \in K$, vì $u =$
$$\sum_{k}  \in K c_{k}u_{k} where c_{k} = \langle u, u_{k}\rangle /\|u_{k}\|^{2}, we have c_{k} = 0 for all k \in K, and u = 0.$$
Ngược lại, giả sử rằng bao đóng (closure) $V$ của $(u_{k})_{k\in K}$ là khác nhau từ $E$. Thì theo Mệnh đề 48.7, ta có $E = V \oplus V^{\perp}$, ở đâu $V^{\perp}$ là phần bù trực giao (orthogonal complement) của $V$, và $V^{\perp}$ là không tầm thường vì V̸ $= E$. Hệ quả là, tồn tại một khác không vectơ $u \in V^{\perp}$. Nhưng khi đó $u$ là trực giao đến mọi vectơ trong $V$, và đặc biệt,
$$\langle u, u_{k}\rangle = 0$$
Với mọi $k \in K$, mà, bởi giả định, suy ra rằng $u = 0$, contradicting sự kiện rằng $u \neq 0$.

<!-- PAGE 2164 -->
Các nhận xét:
$(1)$ Nếu $E$ là Không gian Hilbert (Hilbert space) và $(u_{k})_{k\in K}$ là tổng họ trực giao (orthogonal family) trong $E$, có một đơn giản hơn lập luận để chứng minh rằng $u = 0$ nếu $\langle u, u_{k}\rangle = 0$ với mọi $k \in K$ based trên tính liên tục của $\langle$ -, $-\rangle$. lập luận là để chứng minh rằng giả định suy ra rằng $\langle v, u\rangle = 0$ với mọi $v \in E$. Vì $\langle$ -, $-\rangle$ là xác định dương (positive definite), điều này suy ra rằng $u = 0$. Bởi tính liên tục của $\langle$ -, $-\rangle$, với mọi $\epsilon  > 0$, tồn tại một $\eta  > 0$ sao cho với mọi hữu hạn tập con I của $K$, với mọi họ $(\lambda_{i} )_{i\in I}$, với mọi $v \in E$,
$$\langle v, u\rangle -* \sum_{i\in I}  \lambda_{i} u_{i}, u+




$< \epsilon$$$ bất cứ khi nào
$$v - \sum_{i\in I}  \lambda_{i} u_{i} < \eta .$$
Vì $(u_{k})_{k\in K}$ là trù mật trong $E$, với mọi $v \in E$, tồn tại một hữu hạn tập con I của $K$ và một số họ $(\lambda_{i} )_{i\in I}$ sao cho
$$v - \sum_{i\in I}  \lambda_{i} u_{i} < \eta ,$$
$$and since by assumption, \sum_{i}  \in I \lambda_{i} u_{i}, u= 0, we get$$
$$|\langle v, u\rangle | < \epsilon .$$
Vì điều này nghiệm đúng với mọi $\epsilon  > 0$, ta phải có $\langle v, u\rangle = 0$
$(2)$ Nếu $V$ là bất kỳ khác rỗng tập con của $E$, loại của lập luận được sử dụng trong trước đó nhận xét có thể được được sử dụng để chứng minh rằng $V^{\perp}$ là đóng (chẵn/ngay cả nếu $V$ là không), và rằng $V^{\perp \perp}$ là bao đóng (closure) của $V$. Ta sẽ bây giờ chứng minh rằng mọi Không gian Hilbert (Hilbert space) có một số Hilbert cơ sở (basis). Điều này đòi hỏi bằng cách sử dụng cơ bản định lý từ tập hợp lý thuyết đã biết như Zorn’s bổ đề, mà ta quickly ôn tập/tổng quan. Cho trước bất kỳ tập hợp $X$ với riêng thứ tự $\le$, nhắc lại rằng khác rỗng tập con $C$ của $X$ là dây chuyền/xích nếu nó là một cách tổng được thứ tự (i.e., với mọi $x, y \in C$, hoặc $x \le y$ hoặc $y \le x)$. khác rỗng tập con $Y$ của $X$ là bị chặn khi và chỉ khi tồn tại một $b \in X$ sao cho $y \le b$ với mọi $y \in Y$. Một số $m \in X$ là cực đại khi và chỉ khi với mọi $x \in X, m \le x$ suy ra rằng $x = m$. Ta có thể bây giờ phát biểu Zorn’s bổ đề. Cho nhiều hơn/thêm chi tiết, xem Rudin $[145]$, Lang $[113]$, hoặc Artin $[7]$.

> **Mệnh đề A.6.** (Zorn’s bổ đề) Cho trước bất kỳ khác rỗng một cách riêng được thứ tự tập hợp $X$, nếu mọi
(khác rỗng) dây chuyền/xích trong $X$ là bị chặn, thì $X$ có một số cực đại phần tử.

<!-- PAGE 2165 -->
Ta có thể bây giờ chứng minh sự tồn tại của Hilbert các cơ sở. Ta định nghĩa riêng thứ tự trên các họ $(u_{k})_{k\in K}$ như sau: với mọi hai các họ $(u_{k})_{k\in K1}$ và $(v_{k})_{k\in K2}$, ta nói rằng
$$(u_{k})_{k\in K1} \le (v_{k})_{k\in K2}$$
Khi và chỉ khi $K_{1} \subseteq K_{2}$ và $u_{k} = v_{k}$ với mọi $k \in K_{1}$. Điều này là rõ ràng riêng thứ tự.

> **Mệnh đề A.7.** Cho $E$ là Không gian Hilbert (Hilbert space). Cho trước bất kỳ họ trực giao (orthogonal family) $(u_{k})_{k\in K}$ trong $E$, có một tổng họ trực giao (orthogonal family) $(u_{l})_{l\in L}$ chứa $(u_{k})_{k\in K}$.

*Chứng minh.* Xét tập hợp $\mathcal{S}$ của tất cả trực giao các họ greater hơn hoặc bằng họ $B = (u_{k})_{k\in K}$. Ta khẳng định rằng mọi dây chuyền/xích trong $\mathcal{S}$ là bị chặn. Thật vậy, nếu $C = (C_{l})_{l\in L}$ là dây chuyền/xích trong $\mathcal{S}$, ở đâu $C_{l} = (u_{k,l})_{k\in Kl}$, hợp họ
$$(u_{k})_{k}, where u_{k} = u_{k,l} whenever k \in K_{l},$$
$$\bigcup_{\in l\in}  L Kl$$
Là rõ ràng trên cận cho $C$, và ta kiểm chứng được ngay rằng nó là họ trực giao (orthogonal family). Bởi Zorn’s Bổ đề.6, có một cực đại họ $(u_{l})_{l\in L}$ chứa $(u_{k})_{k\in K}$. Nếu $(u_{l})_{l\in L}$ là không trù mật trong $E$, thì của nó bao đóng (closure) $V$ là chặt được chứa trong $E$, và theo Mệnh đề 48.7, phần bù trực giao (orthogonal complement) $V^{\perp}$ của $V$ là không tầm thường vì V̸ $= E$. Hệ quả là, tồn tại một khác không vectơ $u \in V^{\perp}$. Nhưng khi đó $u$ là trực giao đến mọi vectơ trong $(u_{l})_{l\in L}$, và ta có thể tạo thành họ trực giao (orthogonal family) chặt greater hơn $(u_{l})_{l\in L}$ bằng cách cộng $u$ đến điều này họ, contradicting maximality của $(u_{l})_{l\in L}$. Vì vậy, $(u_{l})_{l\in L}$ là trù mật trong $E$, và do đó nó là Hilbert cơ sở (basis).
Nhận xét: Nó là khả dĩ/có thể để chứng minh rằng tất cả Hilbert các cơ sở cho Không gian Hilbert (Hilbert space) $E$ có chỉ số các tập hợp $K$ của cùng cardinality. Cho chứng minh, xem Bourbaki $[27]$.

> **Định nghĩa A.4.** Không gian Hilbert (Hilbert space) $E$ là khả ly nếu của nó Hilbert các cơ sở là đếm được. Tại cuối cùng, ta có thể chứng minh rằng mọi Không gian Hilbert (Hilbert space) là đẳng cấu đến một số Không gian Hilbert (Hilbert space) $\ell^{2} (K)$ với một số phù hợp $K$.

> **Định lý A.8.** (Riesz–Fischer) Với mọi Không gian Hilbert (Hilbert space) $E$, tồn tại một khác rỗng tập hợp $K$ sao cho $E$ là đẳng cấu đến Không gian Hilbert (Hilbert space) $\ell^{2} (K)$. Nhiều hơn/thêm specifically, với mọi Hilbert cơ sở (basis) $(u_{k})_{k\in K}$ của $E$, các ánh xạ $f$: $\ell^{2} (K) \to E$ và $g: E \to \ell^{2} (K)$ được định nghĩa sao cho
$$f ((\lambda_{k} )_{k\in K}) = \sum_{k\in K}  \lambda_{k} u_{k}andg(u) = \begin{pmatrix} \langle u, u_{k}\rangle /\|u_{k} \end{pmatrix} \|_{k\in K}^{2} = (c_{k})_{k\in K},$$
Là song ánh (bijective) tuyến tính các phép đẳng cự sao cho $g \circ f =$ id và $f \circ g =$ id.

*Chứng minh.* Theo Mệnh đề.4 $(1)$, ánh xạ $f$ được xác định tốt (well-defined), và nó là rõ ràng tuyến tính. Theo Mệnh đề.2 $(3)$, ánh xạ $g$ được xác định tốt (well-defined), và nó là cũng rõ ràng tuyến tính. Theo Mệnh đề.2 (2b), ta có
$$f(g(u)) = u = \sum_{k\in K}  c_{k}u_{k},$$

<!-- PAGE 2166 -->
Và theo Mệnh đề.4 $(1)$, ta có
$$g(f ((\lambda_{k} )_{k\in K})) = (\lambda_{k} )_{k\in K},$$
Và do đó $g \circ f =$ id và $f \circ g =$ id. Theo Mệnh đề.4 $(2)$, ánh xạ tuyến tính (linear map) $g$ là phép đẳng cự (isometry). Vì vậy, $f$ là tuyến tính song ánh và phép đẳng cự (isometry) giữa $\ell^{2} (K)$ và $E$, với nghịch đảo $g$.
Nhận xét: tính toàn ánh của ánh xạ $g: E \to \ell^{2} (K)$ là đã biết như Riesz–Fischer định lý. Có được thực hiện tất cả điều này khó hoạt động/công trình, ta phác thảo cách mà các kết quả này áp dụng đến Fourier chuỗi. Một lần nữa ta refer độc giả đến Rudin $[145]$ hoặc Lang $[115, 116]$ cho toàn diện trình bày. Cho $\mathcal{C}(T)$ ký hiệu tập hợp tất cả periodic liên tục các hàm $f$: $[-\pi , \pi$ ] $\to \mathbb{C}$ với period $2\pi$. Có một Không gian Hilbert (Hilbert space) $L^{2}(T)$ chứa $\mathcal{C}(T)$ và sao cho $\mathcal{C}(T)$ là trù mật trong $L^{2}(T)$, có tích vô hướng (inner product) được cho bởi
$$\langle f, g\rangle = \int_{-}^{}  \pi f(x)\overline{g}\overline{(}\overline{x}\overline{)} dx.$$
$$\pi$$
Không gian Hilbert (Hilbert space) $L^{2}(T)$ là không gian của Lebesgue square-integrable periodic các hàm (của period $2\pi$). Hóa ra là họ $(e^{ikx})_{k\in Z}$ là tổng họ trực giao (orthogonal family) trong $L^{2}(T)$, bởi vì nó là đã trù mật trong $\mathcal{C}(T)$ (chẳng hạn, xem Rudin $[145])$. Thì Riesz–Fischer định lý nói rằng rằng với mọi họ $(c_{k})_{k\in Z}$ của phức các số sao cho
$$\sum_{k\in Z}  |c_{k}|^{2}< \infty ,$$
Tồn tại duy nhất một hàm $f \in L^{2}(T)$ sao cho $f$ bằng của nó Fourier chuỗi
$$f(x) = \sum_{k\in Z}  c_{k}e^{ikx},$$
Ở đâu Fourier các hệ số $c_{k}$ của $f$ được cho bởi công thức
$$c_{k} = \frac{1}{2\pi} \int_{-}^{}  \pi f(t)e^{-ikt}dt.$$
$$\pi$$
Parseval định lý nói rằng rằng
$$\sum_{k=-\infty}^{+\infty}  c_{k}\overline{d}_{k} = \frac{1}{2\pi} \int_{-}^{}  \pi f(t)\overline{g}\overline{(}\overline{t}\overline{)} dt$$
$$\pi$$
Với mọi $f, g \in L^{2}(T)$, ở đâu $c_{k}$ và $d_{k}$ là Fourier các hệ số của $f$ và $g$.
