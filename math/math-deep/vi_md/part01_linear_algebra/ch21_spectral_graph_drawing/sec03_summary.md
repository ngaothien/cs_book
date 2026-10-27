# Tóm tắt


<!-- PAGE 744 -->
Fuller (1895–1983). Montr´eal Biosph`ere là ví dụ của geodesic dome designed bởi Buckminster Fuller. $A =$ đầy đủ(bucky); $D =$ diag(tổng()); $L = D$ - $A; [v, e] =$ eig(L); gplot(, $v(:, [2 3]))$ đúng trên; gplot(,v(:, $[2 3])$, ’o’) Hình 21.5 chỉ ra đồ thị drawing của Buckyball. Điều này picture dường như bit squashed cho hai các lý do. Thứ nhất, nó là một cách thực 3-dimensional đồ thị; thứ hai, $\lambda_{2}  =$ 0.2434 là bộ ba trị riêng (eigenvalue). (Thực sự, Laplacian của $L$ có nhiều bội các trị riêng (eigenvalues).) Những gì ta nên
$$\mathbb{R}^{3}$$
Một cách thực thực hiện là đến plot điều này đồ thị trong bằng cách sử dụng ba trực chuẩn các vectơ riêng (eigenvectors) liên kết với $\lambda_{2}$.
$$0.25$$
$$0.2$$
$$0.15$$
$$0.1$$
$$0.05$$
$$0$$
$$-0.05$$
$$-0.1$$
$$-0.15$$
$$-0.2$$
$$-0.25\overline{-0.25}\overline{-0.2}\overline{-0.15}\overline{-0.1}\overline{-0.05}\overline{0}\overline{0.05}\overline{0.1}\overline{0.15}\overline{0.2}\overline{0.25}$$
$$Figure 21.5: Drawing of the graph of the Buckyball.$$
3D picture của đồ thị của Buckyball là produced bởi sau đây Matlab bài toán quy hoạch, và ảnh (ảnh (image)) của nó được hiển thị trong Hình 21.6. Nó trông tốt hơn! $[x, y] =$ gplot(, $v(:, [2 3])); [x, z] =$ gplot(, $v(:, [2 4]))$; plot3(x,y,z)

## 21.3 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ Đồ thị drawing.

<!-- PAGE 745 -->
$$0.25$$
$$0.2$$
$$0.15$$
$$0.1$$
$$0.05$$
$$0$$
$$-0.05$$
$$-0.1$$
$$-0.15$$
$$-0.2$$
$$-0.25$$
$$0.4$$
$$0.2$$
$$0$$
$$0.20.3$$
$$-0.200.1$$
$$-0.2-0.1$$
$$-0.4-0.4-0.3$$
$$Figure 21.6: Drawing of the graph of the Buckyball in \mathbb{R}^{3}.$$
$\bullet$ Ma trận của đồ thị drawing. $\bullet$ Balanced đồ thị drawing. $\bullet$ Năng lượng $\mathcal{E}(R)$ của đồ thị drawing. $\bullet$ Trực giao đồ thị drawing. $\bullet$ Delaunay tam giác phân. $\bullet$ Buckyball.

<!-- PAGE 746 -->
