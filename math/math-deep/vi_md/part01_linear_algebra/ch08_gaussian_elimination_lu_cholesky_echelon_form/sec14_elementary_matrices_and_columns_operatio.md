# Sơ cấp Các ma trận và Các cột Các phép toán


<!-- PAGE 318 -->
Và vì mỗi hàng (và cột) các tổng đến cùng số, điều này chung/phổ biến giá trị (magic tổng) là
$$\frac{n(n^{2}+ 1)}{2} .$$
Nó là dễ để xem rằng có không có chuẩn tắc/bình thường magic squares cho $n = 2$. Cho $n = 3$, magic tổng là $15$, cho $n = 4$, nó là $34$, và cho $n = 5$, nó là $65$. Trong trường hợp $n = 3$, ta có additional điều kiện rằng các hàng và các cột cộng sai khác $15$, do đó ta kết thúc/cuối lên với nghiệm parametrized bởi hai các số $x_{1}, x_{2}$; cụ thể là,
$$\begin{pmatrix} x_{1} + x_{2} -5 & 10 -x_{2} & 10 -x_{1} \\ 20 -2x_{1} -x_{2} & 5 & 2x_{1} + x_{2} -10 \\ x_{1} & x_{2} & 15 & x_{1} & x_{2} \end{pmatrix} .$$
$$- -$$
Do đó, trong thứ tự để tìm chuẩn tắc/bình thường magic square, ta có additional bất đẳng thức các ràng buộc
$$x_{1} + x_{2} > 5$$
$$x_{1} < 10$$
$$x_{2} < 10$$
$$2x_{1} + x_{2} < 20$$
$$2x_{1} + x_{2} > 10$$
$$x_{1} > 0$$
$$x_{2} > 0$$
$$x_{1} + x_{2} < 15,$$
Và tất cả $9$ các phần tử (entries) trong ma trận phải là phân biệt. Sau tẻ nhạt/dài dòng trường hợp giải tích/phân tích, ta discover đáng chú ý sự kiện rằng tồn tại duy nhất một chuẩn tắc/bình thường magic square (sai khác các phép quay và các phép đối xứng):
$$\begin{pmatrix} 2 & 7 & 6 \\ 9 & 5 & 1 \\ 4 & 3 & 8 \end{pmatrix} .$$
Hóa ra là có $880$ khác nhau chuẩn tắc/bình thường magic squares cho $n = 4$, và $275, 305, 224$ chuẩn tắc/bình thường magic squares cho $n = 5$ (sai khác các phép quay và các phép đối xứng). Chẵn/ngay cả cho $n = 4$, nó lấy fair lượng của hoạt động/công trình đến enumerate chúng tất cả! Việc tìm số của magic squares cho $n > 5$ là mở bài toán!

## 8.14 Sơ cấp Các ma trận và Các cột Các phép toán

Thay vì của performing các phép biến đổi sơ cấp trên hàng trên ma trận $A$, ta có thể perform sơ cấp các cột các phép toán, mà có nghĩa là ta nhân $A$ bởi sơ cấp các ma trận trên phải. Như sơ cấp hàng và cột các phép toán, P(i, $k), E_{i,j;\beta}, E_{i,\lambda}$ perform sau đây actions:
