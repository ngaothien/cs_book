# Đồ thị Clustering Bằng cách sử dụng Được chuẩn hóa Cuts


<!-- PAGE 731 -->

> **Mệnh đề 20.7.** Cho $G = (V, W)$ được trọng số đồ thị. số $c$ của liên thông các thành phần $K_{1}, \dots  , K_{c}$ của underlying đồ thị của $G$ bằng số chiều của không gian hạch (nullspace) của cả hai $L_{sym}$ và $L_{rw}$, mà bằng bội (multiplicity) của trị riêng (eigenvalue) $0$. Hơn nữa, không gian hạch (nullspace) của $L_{rw}$ có cơ sở (basis) bao gồm của indicator các vectơ của liên thông các thành phần của $G$, nghĩa là, các vectơ $(f_{1}, \dots  , f_{m})$ sao cho $f_{j} = 1$ khi và chỉ khi $v_{j} \in K_{i}$ và $f_{j} = 0$ ngược lại. Cho $L_{sym}$, cơ sở (basis) của nullpace là thu được bằng cách nhân ở trên cơ sở (basis) của không gian hạch (nullspace) của $L_{rw}$ bởi $D^{1/2}$. một cách cụ thể thú vị ứng dụng của các toán tử Laplace của đồ thị là đồ thị clustering.

## 20.4 Đồ thị Clustering Bằng cách sử dụng Được chuẩn hóa Cuts

Trong thứ tự đến giải thích bài toán này ta cần một số các định nghĩa.

> **Định nghĩa 20.20.** Cho trước bất kỳ tập con của các nút $A \subseteq V$, ta định nghĩa thể tích vol() của $A$ như tổng của các trọng số của tất cả các cạnh kề nhau đến các nút trong $A$:
$$vol(A) = \sum_{vi\in A}  \sum_{j=1}^{m}  w_{i j}.$$
Cho trước bất kỳ hai các tập con $A, B \subseteq V$ (không nhất thiết phân biệt), ta định nghĩa links(, $B)$ bởi
$$links(A, B) = \sum_{\in A,vj\in}  w_{i j}.$$
$$viB$$
$$The quantity links(\overline{A, A}) = links(\overline{A, A}) (where \overline{A} \frac{=}{A} V -A denotes the complement of A in$$
$V$) measures cách mà nhiều links escape từ $A$ (và). Ta định nghĩa cut của $A$ như
$$cut(A) = links(\overline{A, A}).$$
Khái niệm của thể tích được minh họa trong Hình 20.5 và các khái niệm của cut được minh họa trong Hình 20.6.
$$Figure 20.5: Volume of a set of nodes.$$

<!-- PAGE 732 -->

![Figure 20.6](../../assets/ch20/fig_20_6.png)

**Hình 20.6:** cut liên quan đến tập hợp của các nút trong tâm và các nút trên perimeter. ở trên các khái niệm đóng then chốt vai trò trong lý thuyết của được chuẩn hóa cuts. Điều này đẹp và deeply ban đầu phương pháp thứ nhất published trong Shi và Malik $[166]$, có bây giờ đến là “textbook chương” của máy tính thị giác và máy học (learning). Nó đã là invented bởi Jianbo Shi và Jitendra Malik và đã là chính topic của Shi’s dissertation. phương pháp này đã được mở rộng đến $K \ge 3$ clusters bởi Stella Yu trong her dissertation $[197]$ và là cũng subject của Yu và Shi $[199]$. Cho trước tập hợp của dữ liệu, mục tiêu của clustering là đến phân hoạch dữ liệu vào khác nhau các nhóm theo của chúng similarities. Khi dữ liệu là cho trước theo sự đồng dạng đồ thị $G$, ở đâu trọng số $w_{i j}$ giữa hai các nút $v_{i}$ và $v_{j}$ là measure của sự đồng dạng của $v_{i}$ và $v_{j}$, bài toán có thể được được phát biểu như sau: Tìm phân hoạch $(A_{1}, \dots  , A_{K})$ của tập hợp của các nút $V$ vào khác nhau các nhóm sao cho các cạnh giữa khác nhau các nhóm có rất thấp trọng số (mà indicates rằng các điểm trong khác nhau clusters là dissimilar), và các cạnh trong phạm vi nhóm có cao trọng số (mà indicates rằng các điểm trong phạm vi cùng cluster là đồng dạng). ở trên đồ thị clustering bài toán có thể được formalized như tối ưu hóa bài toán, bằng cách sử dụng khái niệm của cut mentioned trước đó. Nếu ta muốn đến phân hoạch $V$ vào $K$ clusters, ta có thể thực hiện do đó bởi việc tìm phân hoạch $(A_{1}, \dots  , A_{K})$ rằng cực tiểu hóa đại lượng
$$cut(A_{1}, \dots  , A_{K}) = \frac{1}{2} \sum_{i=1}^{K}  cut(A_{i}) = \frac{1}{2} \sum_{i=1}^{K}  links(A_{i}\overline{, A}_{i}).$$
Cho $K = 2$, mincut bài toán là cổ điển bài toán rằng có thể được được giải efficiently, nhưng trong thực tế, nó thực hiện không cho satisfactory các phân hoạch. Thật vậy, trong nhiều các trường hợp, mincut nghiệm tách một đỉnh từ rest của đồ thị. Những gì ta cần là đến design của ta chi phí hàm trong như vậy cách rằng nó các giữ các tập con $A_{i}$ “reasonably lớn” (reasonably balanced). ví dụ của được trọng số đồ thị và phân hoạch của của nó các nút vào hai clusters được hiển thị trong Hình 20.7.
