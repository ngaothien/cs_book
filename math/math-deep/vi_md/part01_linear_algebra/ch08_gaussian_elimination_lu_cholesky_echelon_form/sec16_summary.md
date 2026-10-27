# Tóm tắt


<!-- PAGE 325 -->

> **Mệnh đề 8.27.** Cho $E$ là bất kỳ không gian vectơ hữu hạn chiều. Với mọi phép trượt (transvection) $\tau_{\phi ,u}  (u \neq  0)$ và mọi ánh xạ tuyến tính (linear map) $g \in$ GL(E), ánh xạ $g \circ \tau_{\phi ,u}  \circ g^{-1}$ là phép trượt (transvection) của siêu phẳng (hyperplane) g(H) và hướng g(u) (rằng là, $g \circ \tau_{\phi ,u}  \circ g^{-1} = \tau_{\phi\circ g-1,g(u)}$). Với mọi khác
$$̸$$
Phép trượt (transvection) $\tau_{\psi ,u'}$ (u' $= 0)$, tồn tại một $g \in$ GL(E) như vậy $\tau_{\psi ,u'}  = g \circ \tau_{\phi ,u}  \circ g^{-1}$; nói cách khác bất kỳ hai các phép trượt $(\neq$ id) là liên hợp trong GL(E). Hơn thế nữa, nếu $n \ge 3$, thì tuyến tính đẳng cấu $g$ như ở trên có thể được được chọn sao cho $g \in$ SL(E).

*Chứng minh.* Ta chỉ cần để chứng minh rằng nếu $n \ge 3$, thì với mọi hai các phép trượt $\tau_{\phi ,u}$ và $\tau_{\psi ,u'} (u$, u' $\neq  0)$, tồn tại một $g \in$ SL(E) sao cho $\tau_{\psi ,u'}  = g\circ \tau_{\phi ,u} \circ g^{-1}$. Như trước, ta chọn cơ sở (basis) $(v, u, e_{2}, \dots  , e_{n-1})$ ở đâu $(u, e_{2}, \dots  , e_{n-1})$ là cơ sở (basis) của $H$, ta chọn cơ sở (basis) (v', u', $e_{2}', \dots  , e_{n-1}')$ ở đâu (u', $e_{2}', \dots  , e_{n-1}')$ là cơ sở (basis) của H', và ta định nghĩa $g$ như duy nhất ánh xạ tuyến tính (linear map) sao cho g(v) $=$ v', g(u) $=$ u', và $g(e_{i}) = e_{i}'$, cho $i = 1, \dots  , n$ - $1$. Nhưng trong trường hợp này, cả hai $H$ và H' $=$ g(H) có số chiều ít nhất $2$, do đó trong bất kỳ cơ sở (basis) của H' bao gồm cả u', tồn tại một cơ sở (basis) vectơ $e_{2}'$ độc lập của u', và ta có thể rescale $e_{2}'$ trong như vậy cách rằng ma trận của $g$ trên hai các cơ sở có định thức (determinant) $+1$.

## 8.16 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ Một thực hiện không giải (lớn) các hệ phương trình tuyến tính bởi việc tính toán các định thức. $\bullet$ Tam giác trên (upper-triangular) (tam giác dưới (lower-triangular)) các ma trận. $\bullet$ Việc giải bởi back-substitution (forward-substitution). $\bullet$ Phép khử Gauss (Gaussian elimination). $\bullet$ Hoán vị các hàng. $\bullet$ phần tử trụ (pivot) của phép khử bước; chọn phần tử trụ. $\bullet$ Phép chuyển vị ma trận; sơ cấp ma trận. $\bullet$ Phép khử Gauss (Gaussian elimination) định lý (Định lý 8.1). $\bullet$ Gauss-Jordan nhân tử hóa. $\bullet$ Nhân tử hóa LU (LU-factorization); Cần và đủ điều kiện cho sự tồn tại của Nhân tử hóa LU (LU-factorization) (Mệnh đề 8.2). $\bullet$ LDU-factorization. $\bullet$ “PA $= LU$ định lý” (Định lý 8.5). $\bullet  LDL^{\top}-factorization$ của ma trận đối xứng (symmetric matrix).
