# Các ví dụ của Đồ thị Drawings


<!-- PAGE 740 -->
Tọa độ thứ nhất. Điều này sẽ có nghĩa rằng drawing lives trong siêu phẳng (hyperplane) trong $\mathbb{R}^{n}$, mà là undesirable, especially khi $n = 2$, ở đâu tất cả các đỉnh sẽ là thẳng hàng. Điều này là tại sao ta bỏ qua thứ nhất vectơ riêng (eigenvector) $u_{1}$. Nhận thấy rằng với mọi trực giao $n \times  n$ ma trận $Q$, vì
$$\mathrm{tr}(R^{\top}LR) = \mathrm{tr}(Q^{\top}R^{\top}LRQ),$$
Ma trận $RQ$ cũng cho ta cực tiểu trực giao đồ thị drawing. Điều này tương đương với đến áp dụng cứng motion $Q^{\top}$ đến các hàng của $R$.
$$\mathbb{R}^{2}$$
Trong tóm tắt, nếu $\lambda_{2}  > 0$, automatic phương pháp cho drawing đồ thị trong là điều này: $1$. Tính hai nhỏ nhất khác không các trị riêng (eigenvalues) $\lambda_{2}  \le \lambda_{3}$ của toán tử Laplace của đồ thị (graph Laplacian) $L$ (nó là khả dĩ/có thể rằng $\lambda_{3}  = \lambda_{2}$ nếu $\lambda_{2}$ là bội trị riêng (eigenvalue)); $2$. Tính hai unit các vectơ riêng (eigenvectors) $u_{2}, u_{3}$ liên kết với $\lambda_{2}$ và $\lambda_{3}$, và cho $R = [u_{2} u_{3}]$ là ma trận cỡ $m \times  2$ có $u_{2}$ và $u_{3}$ như các cột. $3$. Place đỉnh $v_{i}$ tại điểm có các tọa độ là hàng thứ $i$ của $R$, nghĩa là, $(R_{i1}, R_{i2})$. phương pháp này một cách tổng quát cho pleasing các kết quả, nhưng beware rằng không có đảm bảo rằng phân biệt các nút là assigned phân biệt các ảnh vì $R$ có thể có đồng nhất các hàng. Điều này thực hiện không dường như đến xảy ra thường trong thực tế.

## 21.2 Các ví dụ của Đồ thị Drawings

Ta bây giờ cho số của các ví dụ bằng cách sử dụng Matlab. Một số của các phần tử này là borrowed hoặc được điều chỉnh từ Spielman $[169]$. Ví dụ $1$. Xét đồ thị với bốn các nút có ma trận kề (adjacency matrix) là
$$A = \begin{pmatrix} 0 & 1 & 1 & 0 \\ 1 & 0 & 0 & 1 \\ 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 \end{pmatrix} .$$
Ta sử dụng sau đây bài toán quy hoạch để tính $u_{2}$ và $u_{3}: A = [0 1 1 0; 1 0 0 1; 1 0 0 1; 0 1 1 0]; D =$ diag(tổng()); $L = D$ - $A; [v, e] =$ eigs(L); gplot(, v(:,[3 $2]))$ đúng trên; gplot(, v(:,[3 2]),’o’)

<!-- PAGE 741 -->
$$0.8$$
$$0.6$$
$$0.4$$
$$0.2$$
$$0$$
$$-0.2$$
$$-0.4$$
$$-0.6$$
$$-0.8\overline{-0.8}\overline{-0.6}\overline{-0.4}\overline{-0.2}\overline{0}\overline{0.2}\overline{0.4}\overline{0.6}\overline{0.8}$$
$$Figure 21.1: Drawing of the graph from Example 1.$$
Đồ thị của Ví dụ $1$ được hiển thị trong Hình 21.1. hàm eigs(L) tính sáu lớn nhất các trị riêng (eigenvalues) của $L$ trong giảm thứ tự, và tương ứng các vectơ riêng (eigenvectors). Hóa ra là $\lambda_{2}  = \lambda_{3}  = 2$ là gấp đôi trị riêng (eigenvalue). Ví dụ $2$. Xét đồ thị $G_{2}$ được hiển thị trong Hình 20.3 cho trước bởi ma trận kề (adjacency matrix)
$$A = \begin{pmatrix} 0 & 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 1 & 1 \\ 1 & 1 & 0 & 1 & 0 \\ 0 & 1 & 1 & 0 & 1 \\ 0 & 1 & 0 & 1 & 0 \end{pmatrix} .$$
Ta sử dụng sau đây bài toán quy hoạch để tính $u_{2}$ và $u_{3}: A = [0 1 1 0 0; 1 0 1 1 1; 1 1 0 1 0; 0 1 1 0 1; 0 1 0 1 0]; D =$ diag(tổng()); $L = D$ - $A; [v, e] =$ eig(L); gplot(, $v(:, [2 3]))$ đúng trên gplot(, $v(:, [2$ 3]),’o’) hàm eig(L) (với không có $s$ tại kết thúc/cuối) tính các trị riêng (eigenvalues) của $L$ trong tăng thứ tự. kết quả của drawing đồ thị được hiển thị trong Hình 21.2. Lưu ý rằng nút $v_{2}$ là assigned đến điểm $(0, 0)$, do đó difference giữa điều này drawing và drawing trong Hình 20.3 là rằng drawing của Hình 21.2 là không lồi. Ví dụ $3$. Xét vành đồ thị được định nghĩa bởi ma trận kề (adjacency matrix) $A$ cho trước trong Matlab bài toán quy hoạch được hiển thị dưới đây:

<!-- PAGE 742 -->
$$0.6$$
$$0.4$$
$$0.2$$
$$0$$
$$-0.2$$
$$-0.4$$
$$-0.6$$
$$-0.8\overline{-0.8}\overline{-0.6}\overline{-0.4}\overline{-0.2}\overline{0}\overline{0.2}\overline{0.4}\overline{0.6}\overline{0.8}$$
$$Figure 21.2: Drawing of the graph from Example 2.$$
$A =$ diag(các một(1, 11),1); $A = A +$ ’; (1, $12) = 1$; (12, $1) = 1; D =$ diag(tổng()); $L = D$ - $A; [v, e] =$ eig(L); gplot(, $v(:, [2 3]))$ đúng trên gplot(, $v(:, [2$ 3]),’o’)
$$0.5$$
$$0.4$$
$$0.3$$
$$0.2$$
$$0.1$$
$$0$$
$$-0.1$$
$$-0.2$$
$$-0.3$$
$$-0.4$$
$$-0.5\overline{-0.5}\overline{-0.4}\overline{-0.3}\overline{-0.2}\overline{-0.1}\overline{0}\overline{0.1}\overline{0.2}\overline{0.3}\overline{0.4}\overline{0.5}$$
$$Figure 21.3: Drawing of the graph from Example 3.$$
Nhận thấy rằng ta thu được rất đẹp vành; xem Hình 21.3. Một lần nữa $\lambda_{2}  =$ 0.2679 là gấp đôi trị riêng (eigenvalue) (và do đó là tiếp theo các cặp của các trị riêng (eigenvalues), ngoại trừ cuối cùng, $\lambda_{12}  = 4)$.

<!-- PAGE 743 -->
Ví dụ $4$. Trong ví dụ này được điều chỉnh từ Spielman, ta sinh $20$ một cách ngẫu nhiên được chọn các điểm trong unit square, tính của chúng Delaunay tam giác phân, thì ma trận kề (adjacency matrix) của tương ứng đồ thị, và cuối cùng draw đồ thị bằng cách sử dụng thứ hai và thứ ba các trị riêng (eigenvalues) của Laplacian. $A =$ các không điểm(20,20); xy $=$ rand(20, $2)$; trigs $=$ delaunay(xy(:,1), xy(:,2)); elemtrig $=$ các một(3) - eye(3); cho $i =$ 1:độ dài(trigs), (trigs(i,:),trigs(i,:)) $=$ elemtrig; kết thúc/cuối $A =$ gấp đôi($>0)$; gplot(,xy) $D =$ diag(tổng()); $L = D$ - $A; [v, e] =$ eigs(L, $3$, ’sm’); hình(2) gplot(, $v(:, [2 1]))$ đúng trên gplot(, $v(:, [2$ 1]),’o’) Delaunay tam giác phân của tập hợp của $20$ các điểm và drawing của tương ứng đồ thị được hiển thị trong Hình 21.4. đồ thị drawing trên phải trông nicer hơn đồ thị trên trái nhưng là là không có dài hơn phẳng.
$$0.90.5$$
$$0.80.4$$
$$0.70.3$$
$$0.60.2$$
$$0.50.1$$
$$0.40$$
$$0.3-0.1$$
$$0.2-0.2$$
$$0.1-0.3$$
$$0-0.4\overline{-0.4}\overline{-0.3}\overline{-0.2}\overline{-0.1}\overline{0}\overline{0.1}\overline{0.2}\overline{0.3}\overline{0.4}$$
$$\overline{0}\overline{0.1}\overline{0.2}\overline{0.3}\overline{0.4}\overline{0.5}\overline{0.6}\overline{0.7}\overline{0.8}\overline{0.9} 1$$

![Figure 21.4](../../assets/ch21/fig_21_4.png)

**Hình 21.4:** Delaunay tam giác phân (trái) và drawing của đồ thị từ Ví dụ $4$ (phải). Ví dụ $5$. Của ta cuối cùng ví dụ, cũng borrowed từ Spielman $[169]$, tương ứng với skeleton của “Buckyball,” geodesic dome invented bởi architect Richard Buckminster
