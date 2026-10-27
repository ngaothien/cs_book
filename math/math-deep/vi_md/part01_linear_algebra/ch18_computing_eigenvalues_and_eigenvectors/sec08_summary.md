# Tóm tắt


<!-- PAGE 688 -->

> **Mệnh đề 18.7.** Cho $A$ là $m \times  m$ chéo hóa được (diagonalizable) (phức hoặc thực) ma trận với các trị riêng (eigenvalues) $\lambda_{1} , \dots  , \lambda_{m}$, và cho $\lambda  = \lambda_{\ell}$ là tùy ý trị riêng (eigenvalue) của $A$ (không cần đơn giản). Với mọi $\mu$ sao cho
$$\mu  \neq  \lambda and|\mu  -\lambda | < |\mu  -\lambda_{j} |for all j \neq  \ell ,$$
Nếu $x^{0}$ thực hiện không thuộc đến không gian con được sinh (spanned) bởi các vectơ riêng (eigenvectors) liên kết với các trị riêng (eigenvalues) $\lambda_{j}$ với $j \neq  \ell$, thì
$$klim\mapsto \infty \begin{pmatrix} (\lambda  -\mu )^{k} \\ |\lambda  -\mu |^{k} \end{pmatrix} x^{k}= v,$$
Ở đâu $v$ là vectơ riêng (eigenvector) liên kết với $\lambda$. Hơn nữa, nếu cả hai $\lambda$ và $\mu$ là thực, ta có
$$limx^{k}= vif \mu  < \lambda ,$$
$$k\mapsto \infty$$
$$lim(-1)^{k}x^{k}= vif \mu  > \lambda .$$
$$k\mapsto \infty$$
Cũng, nếu ta định nghĩa dãy $(\lambda^{(k)}$) bởi
$$\lambda^{(k+1)} = (x^{k+1})^{*}Ax^{k+1},$$
Thì
$$lim\lambda^{(k+1)} = \lambda .$$
$$k\mapsto \infty$$
Điều kiện của $x^{0}$ có thể dường như khá stringent, nhưng trong thực tế, vectơ $x^{0}$ được chọn tại ngẫu nhiên thường thỏa mãn nó. Nếu $A$ là Ma trận Hermite (Hermitian matrix), thì ta có thể nói nhiều hơn/thêm. Đặc biệt, nghịch đảo vòng lặp thuật toán có thể được được sửa đổi để tạo sử dụng của một cách mới được tính $\lambda^{(k+1)}$ thay vì của $\mu$, và chẵn/ngay cả faster sự hội tụ là đạt được. Như vậy phương pháp được gọi là Rayleigh thương vòng lặp. Khi nó hội tụ (mà là cho hầu như tất cả $x^{0})$, phương pháp này eventually đạt được bậc ba sự hội tụ, mà là đáng chú ý. Về cơ bản, điều này có nghĩa là số của đúng digits là tripled tại mọi vòng lặp. Cho nhiều hơn/thêm chi tiết, xem Trefethen và Bau $[182]$ (Lecture $27)$ và Demmel $[48]$ (Mục 5.3.2).

## 18.8 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ QR vòng lặp, QR thuật toán. $\bullet$ Trên Hessenberg các ma trận. $\bullet$ Ma trận Householder.
