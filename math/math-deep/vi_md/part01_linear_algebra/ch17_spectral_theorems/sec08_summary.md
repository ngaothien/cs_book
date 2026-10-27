# Tóm tắt


<!-- PAGE 653 -->
Tuy nhiên,
$$\dim(F) + \dim(G) + \dim(H) = i + j + n -k + 1$$
Và $i + j = k + n$, do đó ta có
$$\dim(F \cap G \cap H) \ge i + j + n -k + 1 -2n = k + n + n -k + 1 -2n = 1,$$
Mà chỉ ra rằng $F \cap G \cap H \neq  (0)$. Thì với mọi unit vectơ $z \in F \cap G \cap H \neq  (0)$, ta có
$$\lambda_{k} (A + B) \le z^{\top}(A + B)z,\lambda_{i} (A) \ge z^{\top}Az,\lambda_{j} (B) \ge z^{\top}Bz,$$
Thiết lập mong muốn bất đẳng thức $\lambda_{k} (A + B) \le \lambda_{i} (A) + \lambda_{j} (B)$. Trong trường hợp đặc biệt $i = j = k$, ta thu được
$$\lambda_{1} (A) + \lambda_{1} (B) \le \lambda_{1} (A + B),\lambda_{n} (A + B) \le \lambda_{n} (A) + \lambda_{n} (B).$$
Suy ra rằng $\lambda_{1}$ (như hàm) là lõm, trong khi $\lambda_{n}$ (như hàm) là lồi. Nếu $i = k$ và $j = 1$, ta thu được
$$\lambda_{k} (A) + \lambda_{1} (B) \le \lambda_{k} (A + B),$$
Và nếu $i = k$ và $j = n$, ta thu được
$$\lambda_{k} (A + B) \le \lambda_{k} (A) + \lambda_{n} (B),$$
Và combining chúng, ta thu được
$$\lambda_{k} (A) + \lambda_{1} (B) \le \lambda_{k} (A + B) \le \lambda_{k} (A) + \lambda_{n} (B).$$
Đặc biệt, nếu $B$ là nửa xác định dương (positive semidefinite), vì các trị riêng (các trị riêng (eigenvalues)) của nó là không âm, ta thu được kết quả sau bất đẳng thức đã biết như monotonicity định lý cho đối xứng (hoặc Hermite) các ma trận: nếu $A$ và $B$ là đối xứng (hoặc Hermite) và $B$ là nửa xác định dương (positive semidefinite), thì
$$\lambda_{k} (A) \le \lambda_{k} (A + B)k = 1, \dots  , n.$$
Độc giả là referred đến Horn và Johnson $[98]$ (Các chương $4$ và $7)$ cho rất đầy đủ treatment của ma trận các bất đẳng thức và interlacing các kết quả, và cũng đến Lax $[117]$ và Serre $[162]$.

## 17.8 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ Chuẩn tắc/bình thường các ánh xạ tuyến tính (linear maps), tự liên hợp (self-adjoint) các ánh xạ tuyến tính (linear maps), phản tự liên hợp (skew-self-adjoint) các ánh xạ tuyến tính (linear maps), và trực giao các ánh xạ tuyến tính (linear maps).
