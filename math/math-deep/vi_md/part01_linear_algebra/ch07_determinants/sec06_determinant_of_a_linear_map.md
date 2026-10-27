# Định thức (determinant) của Ánh xạ tuyến tính (linear map)


<!-- PAGE 241 -->

*Chứng minh.* $(1)$ Giả sử rằng Ax $= b$ có đơn lẻ nghiệm $x_{0}$, và giả sử rằng Ay $= 0$ với $y \neq  0$. Thì,
$$A(x_{0} + y) = Ax_{0} + Ay = Ax_{0} + 0 = b,$$
Và $x_{0} + y \neq  x_{0}$ là một cái khác nghiệm của Ax $= b$, contradicting giả thiết rằng Ax $= b$ có đơn lẻ nghiệm $x_{0}$. Do đó, Ax $= 0$ chỉ có tầm thường nghiệm. Bây giờ giả sử rằng Ax $= 0$ chỉ có tầm thường nghiệm. Điều này có nghĩa là các cột $A^{1}, \dots  , A^{n}$ của $A$ là độc lập tuyến tính (linearly independent), và theo Mệnh đề 7.11, ta có det()̸ $= 0$. Cuối cùng, nếu det()̸ $= 0$, theo Mệnh đề 7.10, điều này có nghĩa là $A$ là khả nghịch, và thì với mọi $b$, Ax $= b$ là tương đương đến $x = A^{-1}b$, mà chỉ ra rằng Ax $= b$ có đơn lẻ nghiệm.
$(2)$ Giả sử rằng Ax $= b$. Nếu ta tính
$$\det(A^{1}, \dots  , x_{1}A^{1}+ \cdots  + x_{j}A^{j}+ \cdots  + x_{n}A^{n}, \dots  , A^{n}) = \det(A^{1}, \dots  , b, \dots  , A^{n}),$$
Ở đâu $b$ xảy ra trong thứ $j$ position, bởi tính đa tuyến tính, tất cả các số hạng chứa hai đồng nhất các cột $A^{k}$ cho $k \neq  j$ triệt tiêu, và ta thu được
$$x_{j} \det(A^{1}, \dots  , A^{n}) = \det(A^{1}, \dots  , A^{j-1}, b, A^{j+1}, \dots  , A^{n}),$$
Với mọi $j, 1 \le j \le n$. Vì ta được giả sử rằng det() $= det(A^{1}, \dots  , A^{n}) \neq  0$, ta thu được mong muốn biểu thức.
$(3)$ Lưu ý rằng Ax $= 0$ có khác không nghiệm khi và chỉ khi $A^{1}, \dots  , A^{n}$ là phụ thuộc tuyến tính (linearly dependent) (như được quan sát trong chứng minh của Mệnh đề 7.11), mà, theo Mệnh đề 7.11, là tương đương đến det() $= 0$. Như pleasing như Cramer’s các quy tắc là, nó là thường impractical để giải các hệ của các phương trình tuyến tính bằng cách sử dụng ở trên các biểu thức. Tuy nhiên, công thức này suy ra thú vị sự kiện, mà là rằng nghiệm của hệ Ax $= b$ là liên tục trong $A$ và $b$. Nếu ta giả sử rằng các phần tử (entries) trong $A$ là liên tục các hàm $a_{ij}(t)$ và các phần tử (entries) trong $b$ là là cũng liên tục các hàm $b_{j}(t)$ của thực tham số $t$, vì các định thức là đa thức các hàm của các phần tử (các phần tử (entries)) của chúng, các biểu thức
$$x_{j}(t) = \frac{\det(A^{1}, \dots  , A^{j-1}, b, A^{j+1}, \dots  , A^{n})}{\det(A^{1}, \dots  , A^{j-1}, A^{j}, A^{j+1}, \dots  , A^{n})}$$
Là các tỉ số của các đa thức, và do đó là cũng liên tục như dài như det((t)) là khác không. Tương tự, nếu các hàm $a_{ij}(t)$ và $b_{j}(t)$ là khả vi (differentiable), do đó là $x_{j}(t)$.

## 7.6 Định thức (determinant) của Ánh xạ tuyến tính (linear map)

Cho trước không gian vectơ (vector space) $E$ của hữu hạn số chiều $n$, cho trước cơ sở (basis) $(u_{1}, \dots  , u_{n})$ của $E$, với mọi ánh xạ tuyến tính (linear map) $f$: $E \to E$, nếu M(f) là ma trận của $f$ w.r.t. cơ sở (basis) $(u_{1}, \dots  , u_{n})$, ta có thể định nghĩa det(f) $=$ det(M(f)). Nếu $(v_{1}, \dots  , v_{n})$ là bất kỳ khác cơ sở (basis) của $E$, và nếu $P$ là chuyển cơ sở (change of basis)
