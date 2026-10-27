# Thay phiên Đa tuyến tính Các ánh xạ


<!-- PAGE 223 -->
Và
$${j_{1}, \dots  , j_{q}, \dots  j_{k}},$$
Ở đâu $i_{p} = i$ và $j_{q} = j$, vì
$$\tau (\pi (\pi^{-1} (i_{p}))) = \tau (i_{p}) = \tau (i) = j = j_{q}$$
Và
$$\tau (\pi (\pi^{-1} (j_{q}))) = \tau (j_{q}) = \tau (j) = i = i_{p},$$
Ta xem rằng các lớp $J_{l}$ và $J_{m}$ merge vào đơn lẻ lớp, và do đó, số của các lớp liên kết với $\tau  \circ \pi$ là $r$ - $1$, và $\epsilon (\tau  \circ \pi$) $= (-1)^{n-r+1} = -(-1)^{n-r} = -\epsilon (\pi$). Bây giờ, cho $\pi  = \tau_{m}  \circ \dots  \circ \tau_{1}$ là bất kỳ tích của các phép chuyển vị. Bởi phần thứ nhất của mệnh đề, ta có
$$\epsilon (\pi ) = (-1)^{m-1}\epsilon (\tau_{1} ) = (-1)^{m-1}(-1) = (-1)^{m},$$
Vì $\epsilon (\tau_{1}$) $= -1$ cho phép chuyển vị.
Nhận xét: Khi $\pi  = id_{n}$ là đồng nhất thức hoán vị, vì ta agreed rằng hợp thành của $0$ các phép chuyển vị là đồng nhất thức, nó nó vẫn đúng rằng $(-1)^{0} = \epsilon$ (id) $= +1$. Từ mệnh đề, ta thấy ngay rằng $\epsilon (\pi' \circ \pi$) $= \epsilon (\pi' )\epsilon (\pi$). Đặc biệt, vì $\pi^{-1} \circ \pi  = id_{n}$, ta thu được $\epsilon (\pi^{-1}$) $= \epsilon (\pi$). Ta có thể bây giờ tiến hành với định nghĩa của các định thức.

## 7.2 Thay phiên Đa tuyến tính Các ánh xạ

Thứ nhất ta định nghĩa đa tuyến tính các ánh xạ, đối xứng đa tuyến tính các ánh xạ, và thay phiên đa tuyến tính các ánh xạ.
Nhận xét: Hầu hết của các định nghĩa và các kết quả được trình bày trong mục này cũng đúng khi $K$ là vành giao hoán (commutative ring) và khi ta xét các môđun trên $K$ (các môđun tự do, khi các cơ sở là cần thiết). Cho $E_{1}, \dots  , E_{n}$, và $F$, là các không gian vectơ trên trường $K$, ở đâu $n \ge 1$.

> **Định nghĩa 7.3.** hàm $f$: $E_{1} \times  \dots  \times  E_{n} \to F$ là ánh xạ đa tuyến tính (multilinear map) (hoặc $n$-tuyến tính ánh xạ) nếu nó là tuyến tính trong mỗi lập luận, giữ những cái khác cố định. Nhiều hơn/thêm một cách tường minh, với mọi $i, 1 \le i \le n$, với mọi $x_{1} \in E_{1}, \dots , x_{i-1} \in E_{i-1}, x_{i+1} \in E_{i+1}, \dots , x_{n} \in E_{n}$, với mọi $x, y \in E_{i}$, với mọi $\lambda  \in K$,
$$f(x_{1}, \dots  , x_{i-1}, x + y, x_{i+1}, \dots  , x_{n}) = f(x_{1}, \dots  , x_{i-1}, x, x_{i+1}, \dots  , x_{n})$$
$$+ f(x_{1}, \dots  , x_{i-1}, y, x_{i+1}, \dots  , x_{n}),$$
$$f(x_{1}, \dots  , x_{i-1}, \lambda x, x_{i+1}, \dots  , x_{n}) = \lambda f(x_{1}, \dots  , x_{i-1}, x, x_{i+1}, \dots  , x_{n}).$$

<!-- PAGE 224 -->
Khi $F = K$, ta gọi $f$ $n$-tuyến tính tạo thành (hoặc dạng đa tuyến tính (multilinear form)). Nếu $n \ge 2$ và $E_{1} = E_{2} = \dots  = E_{n}$, $n$-tuyến tính ánh xạ $f$: $E \times  \dots  \times  E \to F$ được gọi là đối xứng, nếu $f(x_{1}, \dots  , x_{n}) = f(x_{\pi(1)}, \dots  , x_{\pi(n)})$ với mọi hoán vị $\pi$ trên ${1, \dots  , n}$. $n$-tuyến tính ánh xạ $f$: $E\times \dots \times E \to F$ được gọi là thay phiên, nếu $f(x_{1}, \dots  , x_{n}) = 0$ bất cứ khi nào $x_{i} = x_{i+1}$ với một số $i, 1 \le i \le n$ - $1$ (nói cách khác, khi hai kề nhau các đối số/lập luận là bằng nhau). Nó thực hiện không có harm đến agree rằng khi $n = 1$, ánh xạ tuyến tính (linear map) được xét là cả hai đối xứng và thay phiên, và ta sẽ thực hiện do đó. Khi $n = 2$, 2-ánh xạ tuyến tính (linear map) $f$: $E_{1} \times  E_{2} \to F$ được gọi là một ánh xạ song tuyến tính (bilinear map). Ta có đã được thấy một vài các ví dụ của song tuyến tính các ánh xạ. Phép nhân $\cdot$: $K \times  K \to K$ là ánh xạ song tuyến tính (bilinear map), treating $K$ như không gian vectơ (vector space) trên chính nó. phép toán $\langle$ -, $-\rangle$: $E^{*} \times  E \to K$ áp dụng dạng tuyến tính (linear form) đến vectơ là ánh xạ song tuyến tính (bilinear map). Đối xứng song tuyến tính các ánh xạ (và đa tuyến tính các ánh xạ) đóng quan trọng vai trò trong hình học (trong các tích, các dạng toàn phương) và trong vi phân vi tích phân (các đạo hàm riêng). ánh xạ song tuyến tính (bilinear map) là đối xứng nếu f(u, $v) =$ f(v, $u)$, với mọi $u, v \in E$. Thay phiên đa tuyến tính các ánh xạ thỏa mãn sau đây đơn giản nhưng then chốt các tính chất.

> **Mệnh đề 7.3.** Cho $f$: $E \times  \dots  \times  E \to F$ là $n$-tuyến tính thay phiên ánh xạ, với $n \ge 2$. Các tính chất sau đây đúng: $(1)$
$$f(\dots  , x_{i}, x_{i+1}, \dots ) = -f(\dots  , x_{i+1}, x_{i}, \dots )$$
$(2)$
$$f(\dots  , x_{i}, \dots  , x_{j}, \dots ) = 0,$$
Ở đâu $x_{i} = x_{j}$, và $1 \le i < j \le n. (3)$
$$f(\dots  , x_{i}, \dots  , x_{j}, \dots ) = -f(\dots  , x_{j}, \dots  , x_{i}, \dots ),$$
Ở đâu $1 \le i < j \le n. (4)$
$$f(\dots  , x_{i}, \dots ) = f(\dots  , x_{i} + \lambda x_{j}, \dots ),$$
Với mọi $\lambda  \in K$, và ở đâu $i \neq  j$.

*Chứng minh.* $(1)$ Bởi tính đa tuyến tính ứng dụng hai lần, ta có
$$f(\dots  , x_{i} + x_{i+1}, x_{i} + x_{i+1}, \dots ) = f(\dots  , x_{i}, x_{i}, \dots ) + f(\dots  , x_{i}, x_{i+1}, \dots )$$
$$+ f(\dots  , x_{i+1}, x_{i}, \dots ) + f(\dots  , x_{i+1}, x_{i+1}, \dots ),$$
Và vì $f$ là thay phiên, điều này cho ta
$$0 = f(\dots  , x_{i}, x_{i+1}, \dots ) + f(\dots  , x_{i+1}, x_{i}, \dots ),$$

<!-- PAGE 225 -->
Rằng là, $f(\dots  , x_{i}, x_{i+1}, \dots$) $= -f(\dots  , x_{i+1}, x_{i}, \dots$).
$(2)$ Nếu $x_{i} = x_{j}$ và $i$ và $j$ là không kề nhau, ta có thể interchange $x_{i}$ và $x_{i+1}$, và thì $x_{i}$ và $x_{i+2}$, etc, cho đến khi $x_{i}$ và $x_{j}$ trở thành kề nhau. Bởi $(1)$,
$$f(\dots  , x_{i}, \dots  , x_{j}, \dots ) = \epsilon f(\dots  , x_{i}, x_{j}, \dots ),$$
Ở đâu $\epsilon  = +1$ hoặc $-1$, nhưng $f(\dots  , x_{i}, x_{j}, \dots$) $= 0$, vì $x_{i} = x_{j}$, và $(2)$ nghiệm đúng.
$(3)$ suy ra từ $(2)$ như trong $(1). (4)$ là immediate hệ quả của $(2)$. Mệnh đề 7.3 sẽ bây giờ được sử dụng để chỉ ra cơ bản tính chất của thay phiên đa tuyến tính các ánh xạ. Thứ nhất ta cần để mở rộng ma trận ký hiệu little bit. Cho $E$ là không gian vectơ (vector space) trên $K$. Cho trước một ma trận cỡ $n \times  n$ $A = (a_{i j})$ trên $K$, ta có thể định nghĩa ánh xạ L(): $E^{n} \to E^{n}$ như sau:
$$L(A)_{1}(u) = a_{1 1}u_{1} + \cdots  + a_{1n}u_{n},$$
$$\dots$$
$$L(A)_{n}(u) = a_{n1}u_{1} + \cdots  + a_{n n}u_{n},$$
Với mọi $u_{1}, \dots  , u_{n} \in E$ và với $u = (u_{1}, \dots  , u_{n})$. Ta kiểm chứng được ngay rằng L() là tuyến tính. Thì cho trước hai ma trận cỡ $n\times n$ $A = (a_{i j})$ và $B = (b_{i j})$, bởi repeating các phép tính thiết lập tích của các ma trận (chỉ trước Định nghĩa 3.12), ta có thể chỉ ra rằng
$$L(AB) = L(A) \circ L(B).$$
Nó là thì thuận tiện để sử dụng ma trận ký hiệu đến mô tả effect của ánh xạ tuyến tính (linear map) L(), như
$$\begin{pmatrix} L(A)_{1}(u) \\ L(A)_{2}(u) \\ \vdots \\ L(A)_{n}(u) \end{pmatrix} = \begin{pmatrix} a_{1 1} & a_{1 2} & \dots & a_{1n} \\ a_{2 1} & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \dots & a_{n n} \end{pmatrix} \begin{pmatrix} u_{1} \\ u_{2} \\ \vdots \\ u_{n} \end{pmatrix} .$$

> **Bổ đề 7.4.** Cho $f$: $E \times  \dots  \times  E \to F$ là $n$-tuyến tính thay phiên ánh xạ. Cho $(u_{1}, \dots  , u_{n})$ và $(v_{1}, \dots  , v_{n})$ là hai các họ của $n$ các vectơ, sao cho,
$$v_{1} = a_{1 1}u_{1} + \cdots  + a_{n1}u_{n},$$
$$\dots$$
$$v_{n} = a_{1n}u_{1} + \cdots  + a_{n n}u_{n}.$$
Tương đương, đặt
$$A = \begin{pmatrix} a_{1 1} & a_{1 2} & \dots & a_{1n} \\ a_{2 1} & a_{2 2} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \dots & a_{n n} \end{pmatrix} ,$$

<!-- PAGE 226 -->
Giả sử rằng ta có
$$\begin{pmatrix} v_{1} \\ v_{2} \\ \vdots \\ v_{n} \end{pmatrix} = A^{\top} \begin{pmatrix} u_{1} \\ u_{2} \\ \vdots \\ u_{n} \end{pmatrix} .$$
Thì,
$$f(v_{1}, \dots  , v_{n}) = \begin{pmatrix} \epsilon (\pi )a_{\pi(1) 1} \cdots  a_{\pi(n)n} \\ \pi \end{pmatrix} \sum_{\in Sn}  f(u_{1}, \dots  , u_{n}),$$
Ở đâu tổng các miền giá trị (range) trên tất cả các hoán vị $\pi$ trên ${1, \dots  , n}$.

*Chứng minh.* Expanding $f(v_{1}, \dots  , v_{n})$ bởi tính đa tuyến tính, ta thu được tổng của các số hạng của tạo thành
$$a_{\pi(1) 1} \cdots  a_{\pi(n)n}f(u_{\pi(1)}, \dots  , u_{\pi(n)}),$$
Với mọi khả dĩ/có thể các hàm $\pi$: ${1, \dots  , n} \to {1, \dots  , n}$. Tuy nhiên, bởi vì $f$ là thay phiên, chỉ các số hạng cho mà $\pi$ là hoán vị là khác không. Theo Mệnh đề 7.1, mọi hoán vị $\pi$ là tích của các phép chuyển vị, và theo Mệnh đề 7.2, tính chẵn lẻ $\epsilon (\pi$) của số của các phép chuyển vị chỉ phụ thuộc vào $\pi$. Thì áp dụng Mệnh đề 7.3 $(3)$ đến mỗi phép chuyển vị trong $\pi$, ta thu được
$$a_{\pi(1) 1} \cdots  a_{\pi(n)n}f(u_{\pi(1)}, \dots  , u_{\pi(n)}) = \epsilon (\pi )a_{\pi(1) 1} \cdots  a_{\pi(n)n}f(u_{1}, \dots  , u_{n}).$$
Do đó, ta thu được biểu thức của bổ đề. Cho trường hợp của $n = 2$, chứng minh chi tiết của Bổ đề 7.4 trở thành
$$f(v_{1}, v_{2}) = f(a_{11}u_{1} + a_{21}u_{2}, a_{12}u_{1} + a_{22}u_{2})$$
$$= f(a_{11}u_{1} + a_{21}u_{2}, a_{12}u_{1}) + f(a_{11}u_{1} + a_{21}u_{2}, a_{22}u_{2})$$
$$= f(a_{11}u_{1}, a_{12}u_{1}) + f(a_{21}u_{2}, a_{12}u_{1}) + f(a_{11}u_{1}, a_{22}u_{2}) + f(a_{21}u_{2}, a_{22}u_{2})$$
$$= a_{11}a_{12}f(u_{1}, u_{1}) + a_{21}a_{12}f(u_{2}, u_{1}) + a_{11}a_{22}f(u_{1}, u_{2}) + a_{21}a_{22}f(u_{2}, u_{2})$$
$$= a_{21}a_{12}f(u_{2}, u_{1})a_{11}a_{22}f(u_{1}, u_{2})$$
$$= (a_{11}a_{22} -a_{12}a_{22}) f(u_{1}, u_{2}).$$
Hy vọng là độc giả sẽ recognize đại lượng $a_{11}a_{22} -a_{12}a_{22}$. Nó là định thức (determinant) của ma trận cỡ $2 \times  2$
$$A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} .$$
Điều này là không có accident. đại lượng
$$\det(A) = \sum_{\pi\in Sn}  \epsilon (\pi )a_{\pi(1) 1} \cdots  a_{\pi(n)n}$$
