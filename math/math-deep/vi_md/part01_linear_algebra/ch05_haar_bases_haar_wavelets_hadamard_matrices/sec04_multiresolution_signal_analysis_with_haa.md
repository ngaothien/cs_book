# Multiresolution Tín hiệu Giải tích/phân tích với Các cơ sở Haar


<!-- PAGE 162 -->
Nó có thể được được hiển thị rằng $\otimes$ là kết hợp và rằng
$$(A \otimes B)(C \otimes D) = AC \otimes BD$$
$$(A \otimes B)^{\top}= A^{\top}\otimes B^{\top},$$
Bất cứ khi nào AC và BD là tốt được định nghĩa. Thì ta kiểm chứng được ngay rằng $W_{n}$ được cho bởi sau đây neat đệ quy các phương trình:
$$W_{n} = \begin{pmatrix} 1 \\ W_{n-1} \otimes & 1 \end{pmatrix} \begin{pmatrix} 1 \\ I_{2n-1}\otimes & -1 \end{pmatrix} \begin{pmatrix}\end{pmatrix} ,$$
Với $W_{0} = (1)$. Nếu ta cho
$$B_{1} = 2 \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$$
Và cho $n \ge 1$,
$$B_{n+1} = 2 \begin{pmatrix} B_{n} & 0 \\ 0 & I_{2n} \end{pmatrix} ,$$
Thì nó là không khó để sử dụng Kronecker tích formulation của $W_{n}$ để thu được chặt chẽ chứng minh của phương trình
$$W_{n}^{\top}  W_{n} = B_{n},for all n \ge 1.$$
Ở trên phương trình đưa ra gọn gàng justification của sự kiện rằng các cột của $W_{n}$ là đôi một trực giao. Nhận thấy rằng phải khối (của kích thước $2^{n} \times  2^{n-1})$ chỉ ra rõ ràng cách mà chi tiết các hệ số trong thứ hai một nửa của vectơ $c$ được cộng và được trừ đến các phần tử (entries) trong thứ nhất một nửa của một cách riêng reconstructed vectơ sau $n$ - $1$ các bước.

## 5.4 Multiresolution Tín hiệu Giải tích/phân tích với Các cơ sở Haar

Quan trọng và attractive đặc trưng (feature) của Cơ sở Haar (Haar basis) là rằng nó cung cấp multiresolution giải tích/phân tích của tín hiệu. Thật vậy, cho trước tín hiệu $u$, nếu $c = (c_{1}, \dots  , c_{2n})$ là vectơ của của nó Haar các hệ số, các hệ số với thấp chỉ số cho coarse information về $u$, và các hệ số với cao chỉ số biểu diễn fine information. Ví dụ, nếu $u$ là audio tín hiệu tương ứng với Mozart concerto được đóng bởi orchestra, $c_{1}$ tương ứng với “kiến thức nền tảng noise,” $c_{2}$ đến bass, $c_{3}$ đến thứ nhất cello, $c_{4}$ đến thứ hai cello, $c_{5}, c_{6}, c_{7}, c_{7}$ đến violas, thì violins, etc. Điều này multiresolution đặc trưng (feature) của wavelets có thể được exploited đến compress tín hiệu, nghĩa là, để sử dụng fewer các hệ số để biểu diễn nó. Đây là một ví dụ. Xét tín hiệu
$$u = (2.4, 2.2, 2.15, 2.05, 6.8, 2.8, -1.1, -1.3),$$
Có Haar biến đổi là
$$c = (2, 0.2, 0.1, 3, 0.1, 0.05, 2, 0.1).$$

<!-- PAGE 163 -->
Piecewise-linear các đường cong tương ứng với $u$ và $c$ được hiển thị trong Hình 5.6. Vì một số của các hệ số trong $c$ là nhỏ (nhỏ hơn hơn hoặc bằng 0.2) ta có thể compress $c$ bằng cách thay thế chúng bởi $0$. Ta thu được
$$c_{2} = (2, 0, 0, 3, 0, 0, 2, 0),$$
Và reconstructed tín hiệu là
$$u_{2} = (2, 2, 2, 2, 7, 3, -1, -1).$$
Piecewise-linear các đường cong tương ứng với $u_{2}$ và $c_{2}$ được hiển thị trong Hình 5.7.
$$73$$
$$6$$
$$2.5$$
$$5$$
$$42$$
$$3$$
$$1.5$$
$$2$$
$$11$$
$$0$$
$$0.5$$
$$1$$
$$20\overline{0}\overline{0.1}\overline{0.2}\overline{0.3}\overline{0.4}\overline{0.5}\overline{0.6}\overline{0.7}\overline{0.8}\overline{0.9} 1$$
$$\overline{0}\overline{0.1}\overline{0.2}\overline{0.3}\overline{0.4}\overline{0.5}\overline{0.6}\overline{0.7}\overline{0.8}\overline{0.9} 1$$
$$Figure 5.6: A signal and its Haar transform.$$
$$73$$
$$6$$
$$2.5$$
$$5$$
$$2$$
$$4$$
$$31.5$$
$$2$$
$$1$$
$$1$$
$$0.5$$
$$0$$
$$1\overline{0}\overline{0.1}\overline{0.2}\overline{0.3}\overline{0.4}\overline{0.5}\overline{0.6}\overline{0.7}\overline{0.8}\overline{0.9} 10\overline{0}\overline{0.1}\overline{0.2}\overline{0.3}\overline{0.4}\overline{0.5}\overline{0.6}\overline{0.7}\overline{0.8}\overline{0.9} 1$$
$$Figure 5.7: A compressed signal and its compressed Haar transform.$$
Thú vị (và amusing) ứng dụng của Wavelet Haar (Haar wavelets) là đến compression của audio các tín hiệu. Hóa ra là nếu của bạn loại/kiểu load handel trong Matlab audio file sẽ là loaded trong vectơ được ký hiệu bởi $y$, và nếu bạn loại/kiểu sound(y), máy tính sẽ đóng điều này piece của music. Bạn có thể chuyển đổi $y$ đến vectơ của nó của Haar các hệ số $c$. độ dài của $y$ là $73113$,
