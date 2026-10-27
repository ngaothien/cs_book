# Tóm tắt


<!-- PAGE 1128 -->
Ta thu được
$$tB = t \begin{pmatrix} 3 & 1 & 0 \\ 0 & 3 & 1 \\ 0 & 0 & 3 \end{pmatrix} = 3tI_{3} + \begin{pmatrix} 0 & t & 0 \\ 0 & 0 & t \\ 0 & 0 & 0 \end{pmatrix}$$
Và do đó
$$e^{tB} = \begin{pmatrix} e^{3t} & 0 & 0 \\ 0 & e^{3t} & 0 \\ 0 & 0 & e^{3t} \end{pmatrix} \begin{pmatrix} 1 & t & (1/2)t^{2} \\ 0 & 1 & t \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} e^{3t} & te^{3t} & (1/2)t^{2}e^{3t} \\ 0 & e^{3t} & te^{3t} \\ 0 & 0 & e^{3t} \end{pmatrix} .$$
Các cột của $e^{tB}$ tạo thành cơ sở (basis) của không gian của các nghiệm của hệ của tuyến tính vi phân các phương trình
$$\frac{dY_{1}}{dt} = 3Y_{1} + Y_{2}$$
$$\frac{dY_{2}}{dt} = 3Y_{2} + Y_{3}$$
$$\frac{dY_{3}}{dt} = 3Y_{3},$$
Trong ma trận tạo thành,
$$\begin{pmatrix} dY\overline{1} \\ \overline{dt} \\ dY\overline{2} \\ \overline{dt} \\ dY\overline{3} \end{pmatrix} = \begin{pmatrix} 3 & 1 & 0 \\ 0 & 3 & 1 \\ 0 & 0 & 3 \end{pmatrix} \begin{pmatrix} Y_{1} \\ Y_{2} \\ Y_{3} \end{pmatrix} .$$
$$\overline{dt}$$
Một cách tường minh, tổng quát nghiệm của ở trên hệ là
$$\begin{pmatrix} Y_{1} \\ Y_{2} \\ Y_{3} \end{pmatrix} = c_{1} \begin{pmatrix} e^{3t} \\ 0 \\ 0 \end{pmatrix} + c_{2} \begin{pmatrix} te^{3t} \\ e^{3t} \\ 0 \end{pmatrix} + c_{3} \begin{pmatrix} (1/2)t^{2}e^{3t} \\ te^{3t} \\ e^{3t} \end{pmatrix} ,$$
Với $c_{1}, c_{2}, c_{3} \in \mathbb{R}$. Việc giải các hệ của bậc nhất tuyến tính vi phân các phương trình được thảo luận trong Artin $[7]$ và nhiều hơn/thêm extensively trong Hirsh và Smale $[96]$.

## 31.7 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ Các lý tưởng, chính các lý tưởng, lớn nhất chung/phổ biến các ước. $\bullet$ Chuẩn hóa (monic) đa thức, bất khả quy (irreducible) đa thức, một cách tương đối nguyên tố các đa thức. $\bullet$ Linh hóa tử (annihilator) của ánh xạ tuyến tính (linear map). $\bullet$ Đa thức tối tiểu (minimal polynomial) của ánh xạ tuyến tính (linear map).
