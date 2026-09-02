# **Chương 10**

# **Các Ứng dụng**

# **10.1 Đồ thị và Mạng lưới (Graphs and Networks)**

Trong nhiều năm, tôi đã thấy một mô hình xuất hiện quá thường xuyên, và tôi thấy nó rất cơ bản và hữu ích, đến mức tôi luôn đặt nó lên hàng đầu. Mô hình này bao gồm *các nút (nodes) được nối với nhau bởi các cạnh (edges).* Nó được gọi là một *đồ thị (graph).*

Các đồ thị thuộc loại thông thường hiển thị các hàm $f(x)$. Các đồ thị thuộc loại nút-cạnh này dẫn đến các ma trận. Phần này nói về *ma trận liên thuộc (incidence matrix)* của một đồ thị - cho biết $n$ nút được kết nối như thế nào bởi $m$ cạnh. Thông thường $m > n$, có nhiều cạnh hơn nút.

Đối với bất kỳ ma trận $m \times n$ nào, có hai không gian con cơ bản trong $\mathbb{R}^n$ và hai không gian trong $\mathbb{R}^m$. Chúng là các không gian hàng và không gian hạt nhân của $A$ và $A^T$. Các *số chiều $r, n-r$* và *$r, m-r$* của chúng đến từ định lý quan trọng nhất trong đại số tuyến tính. Phần thứ hai của định lý đó là sự *trực giao (orthogonality)* của không gian hàng và không gian hạt nhân. Mục tiêu của chúng ta là chỉ ra cách các ví dụ từ đồ thị làm sáng tỏ Định lý Cơ bản của Đại số Tuyến tính này.

Khi tôi xây dựng một *đồ thị* và *ma trận liên thuộc* của nó, các số chiều của không gian con sẽ dễ dàng được phát hiện. Nhưng chúng ta muốn chính các không gian con đó - và sự trực giao sẽ giúp ích. Điều thiết yếu là kết nối các không gian con với đồ thị mà chúng bắt nguồn. Bằng cách chuyên biệt hóa cho các ma trận liên thuộc, **các định luật của đại số tuyến tính trở thành các định luật của Kirchhoff.** Xin đừng bối rối bởi những từ ngữ như "dòng điện (current)" và "điện áp (voltage)". Những ma trận chữ nhật này là tuyệt vời nhất.

Mỗi phần tử của một ma trận liên thuộc là 0, 1 hoặc -1. Điều này tiếp tục được giữ nguyên trong quá trình khử. Tất cả các phần tử chốt và hệ số nhân đều là $\pm 1$. Do đó cả hai nhân tử trong $A = LU$ cũng chứa 0, 1, -1. Các ma trận không gian hạt nhân cũng vậy! Cả bốn không gian con đều có các vectơ cơ sở với những thành phần đặc biệt đơn giản này. Các ma trận không phải được bịa ra cho một cuốn sách giáo khoa, chúng đến từ một mô hình thực sự thiết yếu trong toán học thuần túy và ứng dụng.

#### **Ma trận Liên thuộc (The Incidence Matrix)**

Hình 10.1 hiển thị một đồ thị với $m = 6$ cạnh và $n = 4$ nút. Ma trận $A$ kích thước $6 \times 4$ cho biết nút nào được kết nối với cạnh nào. Hàng đầu tiên $-1, 1, 0, 0$ cho thấy cạnh đầu tiên đi *từ nút 1 đến nút 2* (-1 cho nút 1 vì mũi tên đi ra, +1 cho nút 2 vì mũi tên đi vào).

Số thứ tự hàng trong $A$ là số thứ tự cạnh, số thứ tự cột 1, 2, 3, 4 là số thứ tự nút!

Hình 10.1: Đồ thị đầy đủ (complete graph) với $m = 6$ cạnh và $n = 4$ nút: Ma trận liên thuộc $A$ kích thước $6 \times 4$.

Bạn có thể viết ma trận bằng cách nhìn vào đồ thị. Đồ thị thứ hai có cùng bốn nút nhưng chỉ có ba cạnh. Ma trận liên thuộc $B$ của nó có kích thước $3 \times 4$.

Hình 10.1*: Cây (tree) với 3 cạnh và 4 nút và không có vòng lặp (no loops). Khi đó $B$ có các hàng độc lập tuyến tính.

Đồ thị đầu tiên là *đồ thị đầy đủ* - mọi cặp nút đều được kết nối bởi một cạnh. Đồ thị thứ hai là một *cây* - đồ thị *không có vòng lặp khép kín*. Đó là hai thái cực. Số lượng cạnh tối đa là $\frac{1}{2}n(n - 1) = 6$ và số lượng tối thiểu để duy trì kết nối là $n - 1 = 3$.

*Phép khử làm suy giảm mọi đồ thị thành một cái cây.* Các vòng lặp tạo ra các hàng phụ thuộc tuyến tính trong $A$ và các hàng zero trong các dạng bậc thang $U$ và $R$. Hãy nhìn vào vòng lặp lớn từ các cạnh 1, 2, 3 trong đồ thị đầu tiên, dẫn đến một hàng zero trong $U$:
$$\begin{bmatrix} -1 & 1 & 0 & 0 \\ -1 & 0 & 1 & 0 \\ 0 & -1 & 1 & 0 \end{bmatrix} \longrightarrow \begin{bmatrix} -1 & 1 & 0 & 0 \\ 0 & -1 & 1 & 0 \\ 0 & 0 & 1 & 0 \end{bmatrix} \longrightarrow \begin{bmatrix} -1 & 1 & 0 & 0 \\ 0 & -1 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

Những bước đó là điển hình. Khi các cạnh 1 và 2 chia sẻ nút 1, phép khử tạo ra "cạnh lối tắt (shortcut edge)" mà không có nút 1. Nếu đồ thị đã có cạnh lối tắt này tạo thành một vòng lặp, thì phép khử sẽ cho ra một hàng số 0. Khi lớp bụi mù tan đi, chúng ta có một cái cây.

Một ý tưởng tự gợi lên: *Các hàng phụ thuộc tuyến tính khi các cạnh tạo thành một vòng lặp.* Các hàng độc lập tuyến tính đến từ các cây. Đây là chìa khóa cho không gian hàng. Chúng ta đang giả định rằng đồ thị là liên thông, và các mũi tên có thể đi theo bất kỳ hướng nào. Trên mỗi cạnh, *dòng chảy cùng chiều với mũi tên là "dương".* Dòng chảy ngược chiều được tính là âm. Dòng chảy có thể là dòng điện, tín hiệu, lực - hoặc thậm chí là dầu, khí đốt hoặc nước.

**Khi $x_1, x_2, x_3, x_4$ là các điện áp tại các nút, $Ax$ cho ra sự chênh lệch điện áp:**
$$Ax = \begin{bmatrix} -1 & 1 & 0 & 0 \\ -1 & 0 & 1 & 0 \\ 0 & -1 & 1 & 0 \\ -1 & 0 & 0 & 1 \\ 0 & -1 & 0 & 1 \\ 0 & 0 & -1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} = \begin{bmatrix} x_2 - x_1 \\ x_3 - x_1 \\ x_3 - x_2 \\ x_4 - x_1 \\ x_4 - x_2 \\ x_4 - x_3 \end{bmatrix} \quad (1)$$

Để tôi nhắc lại. Ma trận liên thuộc $A$ là một ma trận sai phân. Vectơ đầu vào $x$ cho ra các điện áp, vectơ đầu ra $Ax$ cho ra sự chênh lệch điện áp (dọc theo các cạnh từ 1 đến 6). Nếu các điện áp bằng nhau, sự chênh lệch bằng không. Điều này cho chúng ta biết không gian hạt nhân của $A$.

**1** *Không gian hạt nhân (nullspace)* chứa các nghiệm của $Ax = 0$. Cả sáu sự chênh lệch điện áp đều bằng 0. Điều này có nghĩa là: *Tất cả bốn điện áp đều bằng nhau.* Mọi $x$ trong không gian hạt nhân đều là **vectơ hằng số:** $x = (c, c, c, c)$. Không gian hạt nhân của $A$ là một đường thẳng trong $\mathbb{R}^n$ - số chiều của nó là $n - r = 1$.

Ma trận liên thuộc thứ hai $B$ có cùng không gian hạt nhân. Nó chứa **(1, 1, 1, 1):**
$$\text{1 chiều} \quad Bx = \begin{bmatrix} -1 & 1 & 0 & 0 \\ 0 & -1 & 1 & 0 \\ 0 & 0 & -1 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}.$$

Chúng ta có thể tăng hoặc giảm tất cả các điện áp cùng một lượng $c$, mà không làm thay đổi sự chênh lệch. Có một "hằng số tùy ý" trong các điện áp. Hãy so sánh điều này với phát biểu tương tự đối với các hàm số. Chúng ta có thể nâng hoặc hạ một hàm số lên một lượng $C$, mà không làm thay đổi đạo hàm của nó.

Giải tích thêm "+C" vào các tích phân bất định. Lý thuyết đồ thị thêm $(c, c, c, c)$ vào vectơ $x$. Đại số tuyến tính thêm bất kỳ vectơ $x_n$ nào trong không gian hạt nhân vào một nghiệm cụ thể của $Ax = b$.

"+C" biến mất trong giải tích khi một tích phân xác định bắt đầu tại một điểm đã biết. Tương tự như vậy, không gian hạt nhân biến mất khi chúng ta cố định $x_4 = 0$. Ẩn số $x_4$ bị loại bỏ và cột thứ tư của $A$ và $B$ cũng vậy (những cột đó nhân với $x_4$). Các kỹ sư điện sẽ nói rằng nút 4 đã được "nối đất (grounded)".

**2** *Không gian hàng (row space)* chứa tất cả các tổ hợp tuyến tính của sáu hàng. Số chiều của nó chắc chắn không phải là 6. Phương trình $r + (n - r) = n$ phải là $3 + 1 = 4$. Hạng là $r = 3$, như chúng ta đã thấy từ phép khử. Sau 3 cạnh, chúng ta bắt đầu hình thành các vòng lặp! Các hàng mới không độc lập tuyến tính.

Làm thế nào chúng ta có thể nhận biết được liệu $v = (v_1, v_2, v_3, v_4)$ có nằm trong không gian hàng hay không? Cách chậm là tổ hợp các hàng. Cách nhanh là bằng sự trực giao:

*$v$ nằm trong không gian hàng khi và chỉ khi nó vuông góc với $(1, 1, 1, 1)$ trong không gian hạt nhân.*

Vectơ $v = (0, 1, 2, 3)$ không vượt qua bài kiểm tra này - tổng các thành phần của nó là 6. Vectơ $(-6, 1, 2, 3)$ nằm trong không gian hàng: $-6 + 1 + 2 + 3 = 0$. Vectơ đó bằng $6(\text{hàng 1}) + 5(\text{hàng 3}) + 3(\text{hàng 6})$.

Mỗi hàng của $A$ cộng lại bằng không. Điều này phải đúng đối với mọi vectơ trong không gian hàng.

**3** *Không gian cột (column space)* chứa tất cả các tổ hợp tuyến tính của bốn cột. Chúng ta kỳ vọng có ba cột độc lập, vì đã có ba hàng độc lập. Ba cột đầu tiên của $A$ là độc lập (bất kỳ ba cột nào cũng vậy). Nhưng cả bốn cột cộng lại thành vectơ không, điều này một lần nữa nói lên rằng $(1, 1, 1, 1)$ nằm trong không gian hạt nhân. *Làm thế nào chúng ta có thể nhận biết được liệu một vectơ $b$ cụ thể có nằm trong không gian cột của một ma trận liên thuộc hay không?*

**Câu trả lời thứ nhất** Cố gắng giải $Ax = b$. Cách này bỏ lỡ mọi sự hiểu biết sâu sắc. Như trước đây, sự trực giao đưa ra một câu trả lời tốt hơn. Bây giờ chúng ta đi đến hai định luật nổi tiếng của Kirchhoff về lý thuyết mạch - định luật điện áp và định luật dòng điện (**KVL** và **KCL**). Đó là những biểu hiện tự nhiên của "các định luật" đại số tuyến tính. Đặc biệt thú vị khi thấy vai trò then chốt của không gian hạt nhân bên trái.

**Câu trả lời thứ hai** $Ax$ là vectơ chênh lệch điện áp $x_i - x_j$. Nếu chúng ta cộng các chênh lệch xung quanh một vòng lặp kín trong đồ thị, chúng sẽ triệt tiêu nhau còn lại zero. Xung quanh tam giác lớn được tạo bởi các cạnh 1, 3, -2 (*mũi tên đi ngược lại trên cạnh 2*) các chênh lệch triệt tiêu:

**Tổng các chênh lệch là 0**
$$(x_2 - x_1) + (x_3 - x_2) - (x_3 - x_1) = 0$$

*Định luật Điện áp của Kirchhoff: Các thành phần của $Ax = b$ cộng lại bằng không xung quanh mọi vòng lặp.*

*Xung quanh tam giác lớn:*
$$b_1 + b_3 - b_2 = 0$$

Bằng cách kiểm tra từng vòng lặp, Định luật Điện áp quyết định xem $b$ có nằm trong không gian cột hay không. $Ax = b$ có thể được giải chính xác khi các thành phần của $b$ thỏa mãn tất cả các sự phụ thuộc tuyến tính tương tự như các hàng của $A$. Khi đó phép khử dẫn đến $0 = 0$, và hệ $Ax = b$ là nhất quán.

**4** *Không gian hạt nhân bên trái (left nullspace)* chứa các nghiệm của $A^T y = 0$. Số chiều của nó là $m - r = 6 - 3$:
$$\text{Định luật Dòng điện} \quad A^T y = \begin{bmatrix} -1 & -1 & 0 & -1 & 0 & 0 \\ 1 & 0 & -1 & 0 & -1 & 0 \\ 0 & 1 & 1 & 0 & 0 & -1 \\ 0 & 0 & 0 & 1 & 1 & 1 \end{bmatrix} \begin{bmatrix} y_1 \\ y_2 \\ y_3 \\ y_4 \\ y_5 \\ y_6 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \\ 0 \end{bmatrix} \quad (2)$$

Số lượng phương trình thực sự là $r = 3$ chứ không phải $n = 4$. Lý do: Bốn phương trình cộng lại thành $0 = 0$. Phương trình thứ tư tự động tuân theo ba phương trình đầu tiên.

Các phương trình có nghĩa là gì? Phương trình đầu tiên cho biết $-y_1 - y_2 - y_4 = 0$. *Dòng chảy thực (net flow) đi vào nút 1 bằng không.* Phương trình thứ tư cho biết $y_4 + y_5 + y_6 = 0$. *Dòng chảy đi vào nút 4 trừ đi dòng chảy đi ra bằng không.* Các phương trình $A^T y = 0$ là nổi tiếng và cơ bản:

### *Định luật Dòng điện của Kirchhoff: $A^T y = 0$. Dòng chảy đi vào bằng dòng chảy đi ra tại mỗi nút.*

Định luật này xứng đáng có vị trí đầu tiên trong số các phương trình của toán học ứng dụng. Nó thể hiện *"sự bảo toàn (conservation)"* và *"sự liên tục (continuity)"* và *"sự cân bằng (balance)"*. Không có gì bị mất đi, không có gì được thêm vào. Khi các dòng điện hoặc các lực được cân bằng, phương trình cần giải là $A^T y = 0$. Chú ý một thực tế tuyệt đẹp rằng ma trận trong phương trình cân bằng này là chuyển vị của ma trận liên thuộc $A$.

Các nghiệm thực tế của $A^T y = 0$ là gì? Các dòng điện phải tự cân bằng. Cách dễ nhất là **chảy quanh một vòng lặp.** Nếu một đơn vị dòng điện đi vòng quanh tam giác lớn (đi tới trên cạnh 1 và 3, đi lùi trên 2), sáu dòng điện là $y = (1, -1, 1, 0, 0, 0)$. Điều này thỏa mãn $A^T y = 0$. *Mọi dòng điện vòng lặp đều là một nghiệm của Định luật Dòng điện.* Dòng chảy đi vào bằng dòng chảy đi ra tại mọi nút. Một vòng lặp nhỏ hơn đi tới trên cạnh 1, đi tới trên 5, đi lùi trên 4. Khi đó $y = (1, 0, 0, -1, 1, 0)$ cũng nằm trong không gian hạt nhân bên trái.

Chúng ta kỳ vọng có ba $y$ độc lập tuyến tính: $m - r = 6 - 3 = 3$. Ba vòng lặp nhỏ trong đồ thị là độc lập tuyến tính. Tam giác lớn dường như cho ra $y$ thứ tư, nhưng dòng chảy đó là tổng của các dòng chảy xung quanh các vòng lặp nhỏ. *Các dòng chảy xung quanh 3 vòng lặp nhỏ là một cơ sở cho không gian hạt nhân bên trái.*

Ma trận liên thuộc $A$ bắt nguồn từ một đồ thị liên thông với $n$ nút và $m$ cạnh. Không gian hàng và không gian cột có số chiều $r = n - 1$. Không gian hạt nhân của $A$ và $A^T$ có số chiều là 1 và $m - n + 1$:

- $N(A)$: Các vectơ hằng $(c, c, \dots, c)$ tạo nên không gian hạt nhân của $A$: $\text{số chiều} = 1$.
- $C(A^T)$: Các cạnh của bất kỳ cây nào cho ra $r$ hàng độc lập tuyến tính của $A$: $r = n - 1$.
- $C(A)$ Định luật Điện áp: Các thành phần của $Ax$ cộng lại bằng không xung quanh tất cả các vòng lặp: $\text{số chiều} = n - 1$.
- $N(A^T)$ Định luật Dòng điện: $A^T y = (\text{dòng đi vào}) - (\text{dòng đi ra}) = 0$ được giải quyết bằng các dòng điện vòng lặp. *Có $m - r = m - n + 1$ vòng lặp nhỏ độc lập trong đồ thị.*

Đối với mọi đồ thị trên một mặt phẳng, đại số tuyến tính mang lại *Công thức Euler:* Định lý 1 trong topo học! 
$(\text{số lượng nút}) - (\text{số lượng cạnh}) + (\text{số lượng vòng lặp nhỏ}) = 1.$

Đây là $(n) - (m) + (m - n + 1) = 1$. Đồ thị trong ví dụ của chúng ta có $4 - 6 + 3 = 1$.

Một tam giác đơn có (3 nút) - (3 cạnh) + (1 vòng lặp). Trên một cây 10 nút với 9 cạnh và không có vòng lặp, số đếm Euler là $10 - 9 + 0$. Tất cả các đồ thị phẳng đều dẫn đến kết quả 1.

Hình tiếp theo cho thấy một mạng lưới với một nguồn dòng điện. Định luật Dòng điện Kirchhoff thay đổi từ $A^T y = 0$ thành $A^T y = f$, để cân bằng với nguồn $f$ từ bên ngoài. *Dòng điện đi vào mỗi nút vẫn bằng dòng điện đi ra.* Sáu cạnh sẽ có các độ dẫn điện (conductances) $c_1, \dots, c_6$, và nguồn dòng điện đi vào nút 1. Nguồn đi ra từ nút 4 để giữ sự cân bằng tổng thể (vào = ra). Bài toán là: *Tìm các dòng điện $y_1, \dots, y_6$ trên sáu cạnh.* Các dòng chảy trong mạng lưới bây giờ dẫn chúng ta từ ma trận liên thuộc $A$ đến ma trận Laplacian $A^T A$.

#### **Điện áp và Dòng điện và $A^T Ax = f$**

Chúng ta bắt đầu với các điện áp $x = (x_1, \dots, x_n)$ tại các nút. Cho đến nay chúng ta có $Ax$ để tìm chênh lệch điện áp $x_i - x_j$ dọc theo các cạnh. Và chúng ta có Định luật Dòng điện $A^T y = 0$ để tìm các dòng điện trên cạnh $y = (y_1, \dots, y_m)$. Nếu tất cả các điện trở trong mạng lưới đều bằng 1, Định luật Ohm sẽ phù hợp với $y = Ax$. Khi đó $A^T y = A^T Ax = 0$. Chúng ta đã đến gần nhưng chưa hoàn toàn đến đích.

Nếu không có bất kỳ nguồn nào, nghiệm của $A^T Ax = 0$ sẽ chỉ là không có dòng chảy: $x = 0$ và $y = 0$. Tôi có thể thấy ba cách để tạo ra $x \neq 0$ và $y \neq 0$.

1. Gán điện áp cố định $x_i$ cho một hoặc nhiều nút.
2. Thêm pin (nguồn điện áp) vào một hoặc nhiều cạnh.
3. Thêm các nguồn dòng điện đi vào một hoặc nhiều nút. Xem Hình 10.2.

Hình 10.2: Các dòng điện $y_1$ đến $y_6$ trong một mạng lưới với một nguồn $S$ từ nút 4 sang nút 1.

*Ví dụ* Hình 10.2 bao gồm một nguồn dòng điện $S$ từ nút 4 sang nút 1. Dòng điện đó sẽ chảy ngược lại qua mạng lưới đến nút 4. Một số dòng điện $y_4$ sẽ đi trực tiếp trên cạnh 4. Dòng điện khác sẽ đi theo đường vòng từ nút 1 đến 2 đến 4, hoặc 1 đến 3 đến 4. Bằng tính đối xứng, tôi kỳ vọng không có dòng điện ($y_3 = 0$) từ nút 2 sang nút 3. Giải các phương trình mạng lưới sẽ xác nhận điều này. **Ma trận trong các phương trình đó là $A^T A$, ma trận Laplacian của đồ thị:**
$$\begin{bmatrix} -1 & -1 & 0 & -1 & 0 & 0 \\ 1 & 0 & -1 & 0 & -1 & 0 \\ 0 & 1 & 1 & 0 & 0 & -1 \\ 0 & 0 & 0 & 1 & 1 & 1 \end{bmatrix} \begin{bmatrix} -1 & 1 & 0 & 0 \\ -1 & 0 & 1 & 0 \\ 0 & -1 & 1 & 0 \\ -1 & 0 & 0 & 1 \\ 0 & -1 & 0 & 1 \\ 0 & 0 & -1 & 1 \end{bmatrix} = \begin{bmatrix} 3 & -1 & -1 & -1 \\ -1 & 3 & -1 & -1 \\ -1 & -1 & 3 & -1 \\ -1 & -1 & -1 & 3 \end{bmatrix} = A^T A$$

Ma trận Laplacian đó không khả nghịch! Chúng ta không thể giải cho cả bốn điện thế vì $(1, 1, 1, 1)$ nằm trong không gian hạt nhân của $A$ và $A^T A$. *Một nút phải được nối đất.* Đặt $x_4 = 0$ sẽ loại bỏ hàng và cột thứ tư, và điều này để lại một ma trận $3 \times 3$ khả nghịch. Bây giờ chúng ta giải $A^T Ax = f$ cho các điện thế chưa biết $x_1, x_2, x_3$, với nguồn $S$ đi vào nút 1:

| Điện áp<br>$A^T Ax = f$ | $\begin{bmatrix} 3 & -1 & -1 \\ -1 & 3 & -1 \\ -1 & -1 & 3 \end{bmatrix}$ | $\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$ | $= \begin{bmatrix} S \\ 0 \\ 0 \end{bmatrix}$ | cho ra | $\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$ | $= \begin{bmatrix} S/2 \\ S/4 \\ S/4 \end{bmatrix}$ |
|--------------------------|---------------------------------------------------------------------------|---------------------------------------------------|---------------------------------------------|-------|---------------------------------------------------|-----------------------------------------------------|
| Dòng điện<br>$y = -Ax$    | $\begin{bmatrix} y_1 \\ y_2 \\ y_3 \\ y_4 \\ y_5 \\ y_6 \end{bmatrix}$    | $= - \begin{bmatrix} -1 & 1 & 0 \\ -1 & 0 & 1 \\ 0 & -1 & 1 \\ -1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -1 \end{bmatrix}$ | $\begin{bmatrix} S/2 \\ S/4 \\ S/4 \end{bmatrix}$ | $= \begin{bmatrix} S/4 \\ S/4 \\ 0 \\ S/2 \\ S/4 \\ S/4 \end{bmatrix}$ | | |

Một nửa dòng điện đi trực tiếp trên cạnh 4. Đó là $y_4 = S/2$. Không có dòng điện nào chạy từ nút 2 sang nút 3. Tính đối xứng đã chỉ ra $y_3 = 0$ và bây giờ lời giải đã chứng minh điều đó.

*Thừa nhận sai sót.* Tôi nhớ ra rằng dòng điện chảy từ điện áp cao đến điện áp thấp. Điều đó tạo ra dấu trừ trong $y = -Ax$. Và dạng đúng của Định luật Ohm sẽ là $Ry = -Ax$ khi các điện trở trên các cạnh không phải tất cả đều bằng 1. *Độ dẫn điện (Conductances)* gọn gàng hơn so với điện trở: $C = R^{-1} =$ ma trận đường chéo. **Bây giờ chúng ta trình bày Định luật Ohm** $y = -CAx$.

#### **Mạng lưới và $A^T C A$**

Trong một mạng lưới thực tế, dòng điện $y$ dọc theo một cạnh là tích của hai con số. Một con số là chênh lệch giữa các điện thế $x$ ở hai đầu của cạnh. Chênh lệch điện áp này là $Ax$ và nó thúc đẩy dòng chảy. Con số kia $c$ là *"độ dẫn điện" -* đo lường mức độ dễ dàng để dòng điện đi qua.

Trong vật lý và kỹ thuật, $c$ được quyết định bởi vật liệu. Đối với dòng điện, $c$ cao đối với kim loại và thấp đối với nhựa. Đối với chất siêu dẫn, $c$ gần như vô hạn. Nếu chúng ta xem xét sự kéo giãn đàn hồi, $c$ có thể thấp đối với kim loại và cao hơn đối với nhựa. Trong kinh tế học, $c$ đo lường khả năng của một cạnh hoặc chi phí của nó.

Tóm lại, đồ thị được biết đến từ ma trận liên thuộc $A$ của nó. Điều này cho biết các kết nối nút-cạnh. Một *mạng lưới* tiến xa hơn, và gán một độ dẫn điện $c$ cho mỗi cạnh. *Các con số $c_1, \dots, c_m$ này đi vào "ma trận độ dẫn điện (conductance matrix)" $C$ - đây là ma trận đường chéo.*

Đối với một mạng lưới điện trở, độ dẫn điện là $c = 1 / (\text{điện trở})$. Ngoài các Định luật Kirchhoff cho toàn bộ hệ thống các dòng điện, chúng ta có Định luật Ohm cho từng dòng điện. Định luật Ohm kết nối dòng điện $y_1$ trên cạnh 1 với chênh lệch điện áp $x_2 - x_1$:

#### *Định luật Ohm: Dòng điện dọc theo cạnh = độ dẫn điện nhân với chênh lệch điện áp.*

Định luật Ohm cho cả $m$ dòng điện là $y = -CAx$. Vectơ $Ax$ cho ra các chênh lệch điện thế, và $C$ nhân với các độ dẫn điện. Kết hợp Định luật Ohm với Định luật Dòng điện Kirchhoff $A^T y = 0$, chúng ta nhận được $A^T C Ax = 0$. Đây *gần như* là phương trình trung tâm cho các dòng chảy mạng lưới. Điều duy nhất sai là con số không ở vế phải! Mạng lưới cần năng lượng từ bên ngoài - một nguồn điện áp hoặc một nguồn dòng điện - để khiến điều gì đó xảy ra.

*Lưu ý về dấu.* Trong lý thuyết mạch, chúng ta thay đổi từ $Ax$ thành $-Ax$. Dòng chảy là từ điện thế cao hơn đến điện thế thấp hơn. Có dòng điện (dương) từ nút 1 đến nút 2 khi $x_1 - x_2$ dương - trong khi $Ax$ được xây dựng để mang lại $x_2 - x_1$. Dấu trừ trong vật lý và kỹ thuật điện là dấu cộng trong kỹ thuật cơ khí và kinh tế học. $Ax$ so với $-Ax$ là một cơn đau đầu chung nhưng không thể tránh khỏi.

*Lưu ý về toán học ứng dụng.* Mỗi ứng dụng mới đều có dạng riêng của Định luật Ohm. Đối với lò xo, đó là Định luật Hooke. Ứng suất (stress) $y$ bằng (độ đàn hồi $C$) nhân (độ giãn $Ax$). Đối với dẫn nhiệt, $Ax$ là gradient nhiệt độ. Đối với dòng chảy dầu, đó là gradient áp suất. Đối với hồi quy bình phương tối thiểu trong thống kê (Chương 12), $C^{-1}$ là ma trận hiệp phương sai.

Các cuốn sách giáo khoa *Introduction to Applied Mathematics* và *Computational Science and Engineering* (Nhà xuất bản Wellesley-Cambridge) của tôi thực tế được xây dựng dựa trên $A^T C A$. Đây là chìa khóa cho sự cân bằng trong các phương trình ma trận và cũng trong các phương trình vi phân. Toán học ứng dụng có tính tổ chức cao hơn bề ngoài của nó! *Trong các bài toán mới, tôi đã học cách quan tâm đến $A^T C A$.*

### **Tập bài tập 10.1 (Problem Set 10.1)**

**Các bài từ 1-7 và 8-14 nói về các ma trận liên thuộc của những đồ thị này.**

**1** Viết ma trận liên thuộc $A$ kích thước $3 \times 3$ cho đồ thị hình tam giác. Hàng đầu tiên có -1 ở cột 1 và +1 ở cột 2. Những vectơ $(x_1, x_2, x_3)$ nào nằm trong không gian hạt nhân của nó? Làm thế nào bạn biết rằng $(1, 0, 0)$ không nằm trong không gian hàng của nó?
**2** Viết $A^T$ cho đồ thị hình tam giác. Tìm một vectơ $y$ trong không gian hạt nhân của nó. Các thành phần của $y$ là các dòng điện trên các cạnh - có bao nhiêu dòng điện chạy quanh tam giác?
**3** Khử $x_1$ và $x_2$ từ phương trình thứ ba để tìm ma trận bậc thang $U$. Cây nào tương ứng với hai hàng khác không của $U$?
$$-x_1 + x_2 = b_1$$
$$-x_1 + x_3 = b_2$$
$$-x_2 + x_3 = b_3$$
**4** Chọn một vectơ $(b_1, b_2, b_3)$ để $Ax = b$ có thể giải được, và một vectơ $b$ khác không cho phép giải. Những $b$ đó liên quan thế nào đến $y = (1, -1, 1)$?
**5** Chọn một vectơ $(f_1, f_2, f_3)$ để $A^T y = f$ có thể giải được, và một vectơ $f$ không cho phép giải. Những $f$ đó liên quan thế nào đến $x = (1, 1, 1)$? Phương trình $A^T y = f$ là định luật \_\_\_\_\_ của Kirchhoff.
**6** Nhân các ma trận để tìm $A^T A$. Chọn một vectơ $f$ để $A^T Ax = f$ có thể giải được, và giải tìm $x$. Đặt những điện thế $x$ và các dòng điện $y = -Ax$ và nguồn dòng $f$ đó lên đồ thị hình tam giác. Các độ dẫn điện là 1 vì $C = I$.
**7** Với các độ dẫn điện $c_1 = 1$ và $c_2 = c_3 = 2$, nhân các ma trận để tìm $A^T C A$. Đối với $f = (1, 0, -1)$, hãy tìm một nghiệm cho $A^T C Ax = f$. Viết các điện thế $x$ và dòng điện $y = -C Ax$ trên đồ thị hình tam giác, khi nguồn dòng $f$ đi vào nút 1 và đi ra từ nút 3.
**8** Viết ma trận liên thuộc $A$ kích thước $5 \times 4$ cho đồ thị hình vuông có hai vòng lặp. Tìm một nghiệm cho $Ax = 0$ và hai nghiệm cho $A^T y = 0$.
**9** Tìm hai yêu cầu đối với các $b$ để năm sự chênh lệch $x_2 - x_1, x_3 - x_1, x_3 - x_2, x_4 - x_2, x_4 - x_3$ bằng với $b_1, b_2, b_3, b_4, b_5$. Bạn đã tìm thấy định luật \_\_\_\_\_ của Kirchhoff xung quanh hai \_\_\_\_\_ trong đồ thị.
**10** Đưa $A$ về dạng bậc thang $U$ của nó. Ba hàng khác không tạo ra ma trận liên thuộc cho đồ thị nào? Bạn đã tìm thấy một cây trong đồ thị hình vuông - hãy tìm bảy cây còn lại.
**11** Nhân các ma trận để tìm $A^T A$ và đoán xem các phần tử của nó bắt nguồn từ đồ thị như thế nào:
(a) Đường chéo của $A^T A$ cho biết có bao nhiêu \_\_\_\_\_ đi vào mỗi nút.
(b) Các phần tử ngoài đường chéo -1 hoặc 0 cho biết cặp nút nào được \_\_\_\_\_.
**12** Tại sao mỗi câu phát biểu sau đây đúng với $A^T A$? *Trả lời cho $A^T A$ chứ không phải $A$.*
(a) Không gian hạt nhân của nó chứa $(1, 1, 1, 1)$. Hạng của nó là $n - 1$.
(b) Nó là nửa xác định dương (positive semidefinite) nhưng không xác định dương (positive definite).
(c) Bốn giá trị riêng của nó là số thực và dấu của chúng là \_\_\_\_\_.
**13** Với độ dẫn điện $c_1 = c_2 = 2$ và $c_3 = c_4 = c_5 = 3$, hãy nhân các ma trận $A^T C A$. Tìm một nghiệm cho $A^T C Ax = f = (1, 0, 0, -1)$. Viết các điện thế $x$ và dòng điện $y = -C Ax$ này lên các nút và cạnh của đồ thị hình vuông.
**14** Ma trận $A^T C A$ không khả nghịch. Những vectơ $x$ nào nằm trong không gian hạt nhân của nó? Tại sao $A^T C Ax = f$ có nghiệm khi và chỉ khi $f_1 + f_2 + f_3 + f_4 = 0$?
**15** Một đồ thị liên thông có 7 nút và 7 cạnh có bao nhiêu vòng lặp?
**16** Đối với đồ thị có 4 nút, 6 cạnh và 3 vòng lặp, hãy thêm một nút mới. Nếu bạn kết nối nó với một nút cũ, công thức Euler trở thành ( ) - ( ) + ( ) = 1. Nếu bạn kết nối nó với hai nút cũ, công thức Euler trở thành ( ) - ( ) + ( ) = 1.
**17** Giả sử $A$ là ma trận liên thuộc $12 \times 9$ từ một đồ thị liên thông (nhưng chưa biết).
(a) Có bao nhiêu cột của $A$ là độc lập tuyến tính?
(b) Điều kiện nào trên $f$ làm cho việc giải $A^T y = f$ trở nên khả thi?
(c) Các phần tử trên đường chéo của $A^T A$ cho biết số lượng cạnh đi vào mỗi nút. Tổng của các phần tử đường chéo đó là bao nhiêu?
**18** Tại sao một đồ thị đầy đủ với $n = 6$ nút lại có $m = 15$ cạnh? Một cây kết nối 6 nút có \_\_\_\_\_ cạnh.

*Lưu ý.* *Ma trận hợp thức (stoichiometric matrix)* trong hóa học là một ma trận liên thuộc "tổng quát hóa" quan trọng. Các phần tử của nó cho thấy lượng của mỗi chất hóa học (mỗi cột) đi vào mỗi phản ứng (mỗi hàng).

# **10.2 Các ma trận trong Kỹ thuật (Matrices in Engineering)**

Phần này sẽ cho thấy các bài toán kỹ thuật tạo ra các ma trận đối xứng $K$ như thế nào (thường $K$ là xác định dương). "Lý do đại số tuyến tính" cho tính đối xứng và tính xác định dương là dạng $K = A^T A$ và $K = A^T C A$ của chúng. "Lý do vật lý" là biểu thức $\frac{1}{2} u^T K u$ đại diện cho *năng lượng - và* năng lượng không bao giờ âm. Ma trận $C$, thường là ma trận đường chéo, chứa các hằng số vật lý dương như độ dẫn điện, độ cứng hoặc độ khuếch tán.

Các ví dụ tốt nhất của chúng ta đến từ kỹ thuật cơ khí, dân dụng và hàng không. $K$ là *ma trận độ cứng (stiffness matrix)*, và $K^{-1}f$ là phản ứng của cấu trúc đối với các lực $f$ từ bên ngoài. Mục 10.1 đã chuyển sang kỹ thuật điện - các ma trận đến từ mạng lưới và mạch điện. Các bài tập liên quan đến kỹ thuật hóa học và tôi có thể tiếp tục kể! Kinh tế học, quản lý và thiết kế kỹ thuật sẽ đến ở phần sau của chương này (chìa khóa là tối ưu hóa).

Kỹ thuật dẫn đến đại số tuyến tính theo hai cách, trực tiếp và gián tiếp:

*Cách trực tiếp.* Bài toán vật lý chỉ có một số lượng hữu hạn các phần tử. Các định luật kết nối vị trí hoặc vận tốc của chúng là *tuyến tính* (chuyển động không quá lớn hoặc quá nhanh). Các định luật được biểu diễn bằng các *phương trình ma trận*.

*Cách gián tiếp.* Hệ thống vật lý là "liên tục". Thay vì các khối lượng riêng lẻ, mật độ khối lượng, các lực và vận tốc là các hàm số của $x$ hoặc $x, y$ hoặc $x, y, z$. Các định luật được biểu diễn bằng các *phương trình vi phân. Để tìm ra các nghiệm chính xác, chúng ta xấp xỉ bằng các phương trình sai phân hữu hạn (finite difference equations) hoặc phương trình phần tử hữu hạn (finite element equations).*

Cả hai cách đều tạo ra phương trình ma trận và đại số tuyến tính. Tôi thực sự tin rằng bạn không thể làm kỹ thuật hiện đại nếu không có các ma trận.

Ở đây chúng tôi trình bày các phương trình cân bằng $Ku = f$. Với chuyển động, $M \frac{d^2u}{dt^2} + Ku = f$ trở thành động lực học. Khi đó chúng ta sẽ sử dụng các giá trị riêng từ $Kx = \lambda Mx$, hoặc các sai phân hữu hạn.

## **Từ Phương trình Vi phân đến Phương trình Ma trận (Differential Equation to Matrix Equation)**

Các phương trình vi phân là liên tục. Ví dụ cơ bản của chúng ta sẽ là $-\frac{d^2u}{dx^2} = f(x)$. Các phương trình ma trận là rời rạc. Ví dụ cơ bản của chúng ta sẽ là $K_0 u = f$. Bằng cách thực hiện bước chuyển từ đạo hàm bậc hai sang sai phân bậc hai, bạn sẽ thấy được bức tranh toàn cảnh trong một không gian rất ngắn. *Bắt đầu với các điều kiện biên cố định ở cả hai đầu $x = 0$ và $x = 1$:*

| Bài toán giá trị biên cố định-cố định (Fixed-fixed) | $-\frac{d^2u}{dx^2} = 1$ với $u(0) = 0$ và $u(1) = 0$. | (1) |
|------------------------------------|-----------------------------------------------------------|-----|

Phương trình vi phân đó là tuyến tính. Một nghiệm riêng là $u_p = -\frac{1}{2}x^2$ (khi đó $\frac{d^2u}{dx^2} = -1$). Chúng ta có thể thêm bất kỳ hàm nào "trong không gian hạt nhân". Thay vì giải $Ax = 0$ cho một vectơ $x$, chúng ta giải $-\frac{d^2u}{dx^2} = 0$ cho một hàm $u_n(x)$. (Điểm chính: Vế phải bằng không.)

Các nghiệm của không gian hạt nhân là $u_n(x) = C + Dx$ (một không gian hạt nhân 2 chiều cho một phương trình vi phân bậc hai). Nghiệm tổng quát là $u_p + u_n$:

| Nghiệm tổng quát của | $-\frac{d^2u}{dx^2} = 1$ | $u(x) = -\frac{1}{2}x^2 + C + Dx.$ | $(2)$ |
|----------------------|--------------------------|------------------------------------|-------|

Bây giờ tìm $C$ và $D$ từ hai điều kiện biên: Đặt $x = 0$ và sau đó $x = 1$. Tại
$$x = 0, u(0) = 0 \text{ bắt buộc } C = 0. \text{ Tại } x = 1, u(1) = 0 \text{ bắt buộc } -\frac{1}{2} + D = 0. \text{ Khi đó } D = \frac{1}{2}: u(x) = -\frac{1}{2}x^2 + \frac{1}{2}x = \frac{1}{2}(x - x^2) \text{ giải bài toán giá trị biên cố định-cố định. (3)}$$

### **Sai phân Thay thế Đạo hàm (Differences Replace Derivatives)**

Để có được các ma trận thay vì đạo hàm, chúng ta có ba lựa chọn cơ bản - *sai phân tiến (forward), lùi (backward) hoặc trung tâm (centered).* Bắt đầu với đạo hàm bậc nhất và sai phân bậc nhất:

| $\frac{du}{dx} \approx$ | $\frac{u(x + \Delta x) - u(x)}{\Delta x}$ | hoặc | $\frac{u(x) - u(x - \Delta x)}{\Delta x}$ | hoặc | $\frac{u(x + \Delta x) - u(x - \Delta x)}{2\Delta x}$ |
|-------------------------|-------------------------------------------|----|-------------------------------------------|----|-------------------------------------------------------|

Giữa $x = 0$ và $x = 1$, chúng ta chia khoảng thành $n + 1$ phần bằng nhau. Các phần có chiều rộng $\Delta x = 1/(n + 1)$. Các giá trị của $u$ tại các điểm chia (breakpoints) $\Delta x, 2\Delta x, \dots$ sẽ là các ẩn số $u_1$ đến $u_n$ trong phương trình ma trận $Ku = f$ của chúng ta:

Nghiệm cần tính toán: $u = (u_1, u_2, \dots, u_n) \approx (u(\Delta x), u(2\Delta x), \dots, u(n\Delta x))$.

Các giá trị bằng không $u_0 = u_{n+1} = 0$ đến từ các điều kiện biên $u(0) = u(1) = 0$.

*Thay thế đạo hàm trong $-\frac{d}{dx}(\frac{du}{dx}) = 1$ bằng các sai phân tiến và lùi:*
$$\frac{1}{(\Delta x)^2} \begin{bmatrix} 1 & -1 & 0 & 0 \\ 0 & 1 & -1 & 0 \\ 0 & 0 & 1 & -1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & -1 \\ 0 & 0 & -1 \end{bmatrix} \begin{bmatrix} u_1 \\ u_2 \\ u_3 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} \quad (4)$$

Đây là phương trình ma trận của chúng ta khi $n = 3$ và $\Delta x = 1/4$. Hai ma trận sai phân bậc nhất là chuyển vị của nhau! Phương trình là $A^T Au = (\Delta x)^2 f$. Khi chúng ta nhân $A^T A$, chúng chúng ta nhận được ma trận sai phân bậc hai xác định dương $K_0$:

| $K_0 u = (\Delta x)^2 f$ | $\begin{bmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{bmatrix} \begin{bmatrix} u_1 \\ u_2 \\ u_3 \end{bmatrix} = \frac{1}{16} \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$ | cho ra | $\begin{bmatrix} u_1 \\ u_2 \\ u_3 \end{bmatrix} = \frac{1}{32} \begin{bmatrix} 3 \\ 4 \\ 3 \end{bmatrix}$ | (5) |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------------------------------------------------------------------------------------------------|-----|

Thực tế tuyệt vời trong ví dụ này là các con số $u_1, u_2, u_3$ đó hoàn toàn chính xác! Chúng khớp với nghiệm thực $u = \frac{1}{2}(x - x^2)$ tại ba điểm lưới $x = 1/4, 2/4, 3/4$. Hình 10.3 cho thấy nghiệm thực (đường cong liên tục) và các xấp xỉ $u_1, u_2, u_3$ (nằm chính xác trên đường cong). Đường cong này là một parabol.

Hình 10.3: Các nghiệm của $-\frac{d^2u}{dx^2} = 1$ và $K_0 u = (\Delta x)^2 f$ với các biên cố định-cố định.

Làm thế nào để giải thích câu trả lời hoàn hảo này, nằm ngay trên đồ thị của $u(x)$? Trong phương trình ma trận, $K_0 = A^T A$ là một "ma trận sai phân bậc hai". Nó đưa ra một xấp xỉ trung tâm cho $-\frac{d^2u}{dx^2}$. Tôi đã bao gồm dấu trừ vì đạo hàm bậc nhất là *phản đối xứng (antisymmetric)*. Bản thân đạo hàm bậc hai là *âm (negative)*:
"Chuyển vị" của $\frac{d}{dx}$ là $-\frac{d}{dx}$. Khi đó $(-\frac{d}{dx})(\frac{d}{dx})$ là xác định dương.

Bạn có thể thấy điều đó trong các ma trận $A$ và $A^T$. Chuyển vị của $A =$ *sai phân tiến* là $A^T =$ -*sai phân lùi*. Tôi không muốn chọn một sai phân trung tâm $\frac{u(x+\Delta x)-u(x-\Delta x)}{2\Delta x}$. Sai phân trung tâm là tốt nhất cho sai phân bậc nhất, nhưng khi đó sai phân bậc hai $A^T A$ sẽ kéo dài từ $u(x + 2\Delta x)$ đến $u(x - 2\Delta x)$: không tốt.

Bây giờ chúng ta có thể giải thích các câu trả lời hoàn hảo, nằm chính xác trên đường cong thực $u(x) = \frac{1}{2}(x - x^2)$. Các sai phân bậc hai $-1, 2, -1$ là hoàn toàn chính xác đối với các đường thẳng $y = x$ và parabol $y = x^2$!

| $y = x$ | $-\frac{d^2y}{dx^2} = 0$ | $-(x + \Delta x) + 2x - (x - \Delta x) = 0(\Delta x)^2$ |
|---------|--------------------------|---------------------------------------------------------|

| $y = x^2$ | $-\frac{d^2y}{dx^2} = -2$ | $-(x + \Delta x)^2 + 2x^2 - (x - \Delta x)^2 = -2(\Delta x)^2$ |
|-----------|---------------------------|----------------------------------------------------------------|

Điều kỳ diệu tiếp tục đối với $y = x^3$. Kết quả đúng $-\frac{d^2y}{dx^2} = -6x$ được tạo ra bởi sai phân bậc hai. Nhưng đối với $y = x^4$, chúng ta trở lại mặt đất. Sai phân bậc hai không khớp chính xác với $-y'' = -12x^2$. Các xấp xỉ $u_1, u_2, u_3$ sẽ không nằm trên đồ thị của $u(x)$.

## **Đầu Cố định và Đầu Tự do và Hệ số Biến thiên $c(x)$ (Fixed End and Free End and Variable Coefficient)**

Để thấy hai khả năng mới, tôi sẽ thay đổi phương trình và cả một điều kiện biên:
$$-\frac{d}{dx} \left( (1+x) \frac{du}{dx} \right) = f(x) \text{ với } u(0) = 0 \text{ và } \frac{du}{dx}(1) = 0. \quad (6)$$

Đầu $x = 1$ bây giờ là **tự do (free)**. Không có sự hỗ trợ nào ở đầu đó. "Một thanh treo chỉ được cố định ở đỉnh." Không có lực nào tác dụng ở đầu tự do $x = 1$. Điều đó chuyển thành $\frac{du}{dx} = 0$ thay vì điều kiện cố định $u = 0$ tại $x = 1$.

Sự thay đổi khác nằm ở hệ số $c(x) = 1 + x$. Độ cứng của thanh đang thay đổi khi bạn đi từ $x = 0$ đến $x = 1$. Có thể chiều rộng của nó đang thay đổi, hoặc vật liệu thay đổi. Hệ số $1 + x$ này sẽ mang một ma trận mới $C$ vào phương trình sai phân.

Vì $u_4$ không còn được cố định ở mức 0, nó trở thành một ẩn số mới. Ma trận sai phân lùi $A$ có kích thước $4 \times 4$. Và phép nhân với $c(x) = 1 + x$ trở thành một ma trận đường chéo $C$ - nhân với $1 + \Delta x, \dots, 1 + 4\Delta x$ tại các điểm lưới. Dưới đây là $A^T, C$, và $A$:
$$A^T C A = \begin{bmatrix} 1 & -1 & 0 & 0 \\ 0 & 1 & -1 & 0 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1.25 & & & \\ & 1.5 & & \\ & & 1.75 & \\ & & & 2.0 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 & 0 \\ -1 & 1 & 0 & 0 \\ 0 & -1 & 1 & 0 \\ 0 & 0 & -1 & 1 \end{bmatrix}. \quad (7)$$

Ma trận $K = A^T C A$ này sẽ đối xứng và xác định dương! Đối xứng vì $(A^T C A)^T = A^T C^T A^T = A^T C A$. Xác định dương vì nó vượt qua bài kiểm tra năng lượng: $A$ có các cột độc lập tuyến tính, do đó $Ax \neq 0$ khi $x \neq 0$.
$$\text{Năng lượng} = x^T A^T C A x = (Ax)^T C (Ax) > 0 \text{ với mọi } x \neq 0, \text{ bởi vì } Ax \neq 0.$$

Khi bạn nhân các ma trận $A^T A$ và $A^T C A$ cho sự kết hợp cố định-tự do này, hãy xem cách số 1 thay thế số 2 ở góc cuối của $A^T A$. Phương trình thứ tư đó có $u_4 - u_3$, một sai phân bậc nhất (không phải bậc hai) đến từ điều kiện biên tự do $\frac{du}{dx} = 0$.

Hãy chú ý trong $A^T C A$ cách $c_1, c_2, c_3, c_4$ đến từ $c(x) = 1 + x$ trong phương trình (7). Trước đây các $c$ chỉ đơn giản là $1, 1, 1, 1$. Dưới đây là các ma trận **cố định-tự do (fixed-free)**:
$$A^T A = \begin{bmatrix} 2 & -1 & & \\ -1 & 2 & -1 & \\ & -1 & 2 & -1 \\ & & -1 & 1 \end{bmatrix} \quad A^T C A = \begin{bmatrix} c_1 + c_2 & -c_2 & & \\ -c_2 & c_2 + c_3 & -c_3 & \\ & -c_3 & c_3 + c_4 & -c_4 \\ & & -c_4 & c_4 \end{bmatrix}. \quad (8)$$

# **Các Điều kiện Biên Tự do-Tự do (Free-free Boundary Conditions)**

Giả sử cả hai đầu của thanh đều tự do. Bây giờ $\frac{du}{dx} = 0$ tại cả $x = 0$ và $x = 1$. Không có gì giữ thanh tại chỗ! Về mặt vật lý, nó không ổn định - nó có thể di chuyển mà không cần lực. Về mặt toán học, tất cả các hàm hằng số như $u = 1$ đều thỏa mãn các điều kiện tự do này. **Về mặt đại số, các ma trận của chúng ta $A^T A$ và $A^T C A$ sẽ không khả nghịch:**

| Các ví dụ tự do-tự do | $A^T A = \begin{bmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{bmatrix}$ | $A^T C A = \begin{bmatrix} c_0 & -c_0 & 0 \\ -c_0 & c_0 + c_1 & -c_1 \\ 0 & -c_1 & c_1 \end{bmatrix}$ |
|-------------------------|---------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Ẩn số $u_0, u_1, u_2$ | | |
| $\Delta x = 0.5$ | | |

Vectơ $(1, 1, 1)$ nằm trong cả hai không gian hạt nhân. Điều này khớp với $u(x) = 1$ trong bài toán liên tục. $A^T Au = f$ và $A^T C Au = f$ với điều kiện tự do-tự do nói chung là không thể giải được.

Trước khi giải thích thêm các ví dụ vật lý, cho phép tôi viết ra sáu trong số các ma trận. Ma trận ba đường chéo $K_0$ xuất hiện nhiều lần trong cuốn sách này. Bây giờ chúng ta đang thấy các ứng dụng của nó. Tất cả các ma trận này đều đối xứng, và bốn ma trận đầu tiên là xác định dương:

| $K_0 = A_0^T A_0 = \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}$ | $A_0^T C_0 A_0 = \begin{bmatrix} c_1 + c_2 & -c_2 \\ -c_2 & c_2 + c_3 \end{bmatrix}$ |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Cố định-cố định | Đã bao gồm hằng số lò xo |

| $K_1 = A_1^T A_1 = \begin{bmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{bmatrix}$ | $A_1^T C_1 A_1 = \begin{bmatrix} c_1 + c_2 & -c_2 & 0 \\ -c_2 & c_2 + c_3 & -c_3 \\ 0 & -c_3 & c_3 \end{bmatrix}$ |
|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| **Cố định-tự do** | **Đã bao gồm hằng số lò xo** |

$$K_{\text{singular}} = \begin{bmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{bmatrix} \quad K_{\text{circular}} = \begin{bmatrix} 2 & -1 & -1 \\ -1 & 2 & -1 \\ -1 & -1 & 2 \end{bmatrix}$$
Tự do-tự do                      Chu kỳ $u(0) = u(1)$

Các ma trận $K_0, K_1, K_{\text{singular}}$ và $K_{\text{circular}}$ có $C = I$ cho đơn giản. Điều này có nghĩa là tất cả các "hằng số lò xo" đều là $c_i = 1$. Chúng tôi đã đưa $A_0^T C_0 A_0$ và $A_1^T C_1 A_1$ vào để cho thấy các hằng số lò xo đi vào ma trận như thế nào (mà không làm thay đổi tính xác định dương của nó). Mục tiêu tiếp theo của chúng ta là thấy các ma trận độ cứng tương tự này trong các bài toán kỹ thuật khác.

**Một Dãy Lò xo và Khối lượng (A Line of Springs and Masses)**

Hình 10.4 cho thấy ba khối lượng $m_1, m_2, m_3$ được nối bởi một dãy các lò xo. Trường hợp cố định-cố định có bốn lò xo, với đầu trên và đầu dưới được cố định. Điều đó dẫn đến $K_0$ và $A_0^T C_0 A_0$. Trường hợp cố định-tự do chỉ có ba lò xo; khối lượng thấp nhất treo tự do. Điều đó sẽ dẫn đến $K_1$ và $A_1^T C_1 A_1$. Một bài toán **tự do-tự do** tạo ra $K_{\text{singular}}$.

Chúng ta muốn các phương trình cho các chuyển động của khối lượng $u$ và sức căng của lò xo $y$:
$u = (u_1, u_2, u_3) =$ chuyển động của các khối lượng (đi xuống là dương)
$y = (y_1, y_2, y_3, y_4)$ hoặc $(y_1, y_2, y_3) =$ sức căng trong các lò xo

Hình 10.4: Các dãy lò xo và khối lượng: các đầu **cố định-cố định** và **cố định-tự do**.

Khi một khối lượng di chuyển xuống dưới, độ dịch chuyển của nó là dương ($u_j > 0$). Đối với các lò xo, lực kéo căng là dương và lực nén là âm ($y_i < 0$). Khi chịu lực kéo căng, lò xo bị giãn ra nên nó kéo các khối lượng vào trong. Mỗi lò xo bị chi phối bởi Định luật Hooke của riêng nó $y = ce$: (lực kéo căng $y$) = (hằng số lò xo $c$) nhân (khoảng cách giãn $e$).

Công việc của chúng ta là liên kết các phương trình một-lò xo $y = ce$ này thành một phương trình vectơ $Ku = f$ cho toàn bộ hệ thống. Vectơ lực $f$ đến từ trọng lực. Hằng số hấp dẫn $g$ sẽ nhân với từng khối lượng để tạo ra các lực hướng xuống $f = (m_1g, m_2g, m_3g)$.

Bài toán thực sự là tìm ma trận độ cứng (**cố định-cố định** và **cố định-tự do**). Cách tốt nhất để tạo ra $K$ là qua ba bước, chứ không phải một. Thay vì kết nối trực tiếp các chuyển động $u_j$ với các lực $f_i$, tốt hơn nhiều là nên kết nối từng vectơ với vectơ tiếp theo trong danh sách này:
$u =$ Chuyển động của $n$ khối lượng $= (u_1, \dots, u_n)$
$e =$ Độ giãn của $m$ lò xo $= (e_1, \dots, e_m)$
$y =$ Nội lực trong $m$ lò xo $= (y_1, \dots, y_m)$
$f =$ Ngoại lực tác dụng lên $n$ khối lượng $= (f_1, \dots, f_n)$

Một khuôn khổ tuyệt vời cho toán học ứng dụng kết nối $u$ với $e$ với $y$ với $f$. Khi đó $A^T C Au = f$:

Chúng ta sẽ viết ra các ma trận $A$ và $C$ và $A^T$ cho hai ví dụ, đầu tiên với các đầu cố định và sau đó với đầu dưới tự do. Hãy tha thứ cho sự đơn giản của các ma trận này, chính dạng của chúng mới là điều quan trọng. Đặc biệt là sự xuất hiện của $A$ cùng với $A^T$.

*Độ giãn $e$ là khoảng cách kéo căng -* các lò xo bị giãn ra bao xa. Ban đầu không có sự kéo căng - hệ thống đang nằm trên bàn. Khi nó trở thành phương thẳng đứng và dựng đứng, trọng lực tác động. Các khối lượng di chuyển xuống dưới những khoảng cách $u_1, u_2, u_3$. Mỗi lò xo bị giãn hoặc nén một lượng $e_i = u_i - u_{i-1}$, *chênh lệch về độ dịch chuyển của hai đầu của nó:*

| **Sự giãn ra của từng lò xo** | Lò xo thứ nhất: | $e_1 = u_1$ | (đầu trên cố định nên $u_0 = 0$) |
|----------------------------------|-----------------------|-----------------------------------------------------|------------------------------------------------------|
| | Lò xo thứ hai: | $e_2 = u_2 - u_1$ | |
| | Lò xo thứ ba: | $e_3 = u_3 - u_2$ | |
| | Lò xo thứ tư: | $e_4 = -u_3$ | (đầu dưới cố định nên $u_4 = 0$) |

Nếu cả hai đầu di chuyển cùng một khoảng cách, lò xo đó không bị giãn: $u_j = u_{j-1}$ và $e_j = 0$. Ma trận trong bốn phương trình đó là một *ma trận sai phân* $4 \times 3$ $A$, và $e = Au$:
$$\text{Khoảng cách giãn (elongations)} \quad e = Au \quad \text{là} \quad \begin{bmatrix} e_1 \\ e_2 \\ e_3 \\ e_4 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \\ 0 & 0 & -1 \end{bmatrix} \begin{bmatrix} u_1 \\ u_2 \\ u_3 \end{bmatrix}. \quad (9)$$

Phương trình tiếp theo $y = Ce$ kết nối độ giãn lò xo $e$ với sức căng lò xo $y$. *Đây là Định luật Hooke $y_i = c_i e_i$ cho từng lò xo riêng biệt.* Nó là "định luật cấu thành (constitutive law)" phụ thuộc vào vật liệu trong lò xo. Một lò xo mềm có $c$ nhỏ, do đó một lực $y$ vừa phải có thể tạo ra độ giãn $e$ lớn. Định luật tuyến tính của Hooke gần như chính xác đối với các lò xo thực, trước khi chúng bị kéo căng quá mức và vật liệu trở nên dẻo.

Vì mỗi lò xo có định luật riêng của nó, ma trận trong $y = Ce$ là một ma trận đường chéo $C$:
**Định luật Hooke** $y = Ce \implies \begin{bmatrix} y_1 \\ y_2 \\ y_3 \\ y_4 \end{bmatrix} = \begin{bmatrix} c_1 & & & \\ & c_2 & & \\ & & c_3 & \\ & & & c_4 \end{bmatrix} \begin{bmatrix} e_1 \\ e_2 \\ e_3 \\ e_4 \end{bmatrix}. \quad (10)$

Kết hợp $e = Au$ với $y = Ce$, các lực của lò xo (lực kéo căng) là $y = CAu$.

Cuối cùng là phương trình cân bằng, định luật cơ bản nhất của toán học ứng dụng. Nội lực từ các lò xo cân bằng với ngoại lực tác dụng lên các khối lượng. Mỗi khối lượng bị kéo hoặc đẩy bởi lực lò xo $y_j$ phía trên nó. Từ bên dưới nó cảm nhận lực lò xo $y_{j+1}$ cộng với $f_j$ từ trọng lực. Do đó $y_j = y_{j+1} + f_j$ hay $f_j = y_j - y_{j+1}$:
$$\begin{aligned}
 \text{Cân bằng lực} \quad & f_1 = y_1 - y_2 \\
 f = A^T y \quad & f_2 = y_2 - y_3 \\
 & f_3 = y_3 - y_4 
 \end{aligned} \quad \implies \quad \begin{bmatrix} f_1 \\ f_2 \\ f_3 \end{bmatrix} = \begin{bmatrix} 1 & -1 & 0 & 0 \\ 0 & 1 & -1 & 0 \\ 0 & 0 & 1 & -1 \end{bmatrix} \begin{bmatrix} y_1 \\ y_2 \\ y_3 \\ y_4 \end{bmatrix}. \quad (11)$$

*Ma trận đó là $A^T$! Phương trình cân bằng lực là $f = A^T y$.* Tự nhiên chuyển vị các hàng và các cột của ma trận $e - u$ để tạo ra ma trận $f - y$. Đây là vẻ đẹp của khuôn khổ này, rằng $A^T$ xuất hiện cùng với $A$. Ba phương trình kết hợp thành $K_0 u = f$.
$$\left\{ \begin{array}{l} e = Au \\ y = Ce \\ f = A^T y \end{array} \right\} \quad \text{kết hợp thành} \quad A^T C A u = f \quad \text{hoặc} \quad K u = f$$
$K = A^T C A$ là **ma trận độ cứng (stiffness matrix)** (cơ học).
$K = A^T C A$ là **ma trận độ dẫn điện (conductance matrix)** (mạng lưới).

Các chương trình phần tử hữu hạn dành nỗ lực lớn để lắp ráp $K = A^T C A$ từ hàng ngàn mảnh nhỏ hơn. Chúng ta tìm $K$ cho bốn lò xo (**cố định-cố định**) bằng cách nhân $A^T$ với $C A$:
$$\begin{bmatrix} 1 & -1 & 0 & 0 \\ 0 & 1 & -1 & 0 \\ 0 & 0 & 1 & -1 \end{bmatrix} \begin{bmatrix} c_1 & 0 & 0 \\ -c_2 & c_2 & 0 \\ 0 & -c_3 & c_3 \\ 0 & 0 & -c_4 \end{bmatrix} = \begin{bmatrix} c_1 + c_2 & -c_2 & 0 \\ -c_2 & c_2 + c_3 & -c_3 \\ 0 & -c_3 & c_3 + c_4 \end{bmatrix}$$

Nếu tất cả các lò xo đều giống nhau, với $c_1 = c_2 = c_3 = c_4 = 1$, thì $C = I$. Ma trận độ cứng rút gọn thành $A^T A$. Nó trở thành ma trận $-1, 2, -1$ đặc biệt $K_0$.

Hãy chú ý sự khác biệt giữa $A^T A$ từ kỹ thuật và $LU$ từ đại số tuyến tính. Ma trận $A$ từ bốn lò xo có kích thước $4 \times 3$. Các ma trận tam giác từ phép khử là ma trận vuông. Ma trận độ cứng $K$ được lắp ráp từ $A^T A$, và sau đó được chia nhỏ thành $LU$. Một bước là toán học ứng dụng, bước kia là toán học tính toán. Mỗi $K$ được xây dựng từ các ma trận chữ nhật và phân tích thành các ma trận vuông.

Cho phép tôi liệt kê một số tính chất của $K = A^T C A$. Bạn đã biết gần như tất cả chúng:

1. $K$ là **ma trận ba đường chéo (tridiagonal)**, vì khối lượng 3 không kết nối với khối lượng 1.
2. $K$ là **đối xứng**, vì $C$ đối xứng và $A^T$ đi kèm với $A$.
3. $K$ là **xác định dương**, vì $c_i > 0$ và $A$ có các **cột độc lập tuyến tính**.
4. $K^{-1}$ là một **ma trận đầy đủ (full matrix)** (không thưa thớt) với **tất cả các phần tử đều dương**.

Tính chất 4 dẫn đến một sự thật quan trọng về $u = K^{-1}f$: Nếu tất cả các lực đều hướng xuống ($f_j > 0$) thì tất cả các chuyển động đều hướng xuống ($u_j > 0$). Chú ý rằng "dương" khác với "xác định dương". $K^{-1}$ là dương ($K$ thì không). Cả hai đều xác định dương.

**Ví dụ 1** Giả sử tất cả $c_i = c$ và $m_j = m$. Tìm các chuyển động $u$ và sức căng $y$.

Tất cả các lò xo đều giống nhau và tất cả các khối lượng đều giống nhau. Nhưng tất cả các chuyển động và độ giãn và sức căng sẽ không giống nhau. $K^{-1}$ bao gồm $\frac{1}{c}$ vì $A^T C A$ bao gồm $c$:
$$\text{Các chuyển động} \quad u = K^{-1}f = \frac{1}{4c} \begin{bmatrix} 3 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 3 \end{bmatrix} \begin{bmatrix} mg \\ mg \\ mg \end{bmatrix} = \frac{mg}{c} \begin{bmatrix} 3/2 \\ 2 \\ 3/2 \end{bmatrix}$$

Độ dịch chuyển $u_2$, đối với khối lượng ở giữa, lớn hơn $u_1$ và $u_3$. Các đơn vị là chính xác: lực $mg$ chia cho lực trên một đơn vị chiều dài $c$ cho ra một chiều dài $u$. Khi đó
$$\text{Khoảng cách giãn} \quad e = Au = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \\ 0 & 0 & -1 \end{bmatrix} \frac{mg}{c} \begin{bmatrix} 3/2 \\ 2 \\ 3/2 \end{bmatrix} = \frac{mg}{c} \begin{bmatrix} 3/2 \\ 1/2 \\ -1/2 \\ -3/2 \end{bmatrix}.$$

**Cảnh báo:** *Thông thường bạn không thể viết $K^{-1} = A^{-1}K^{-1}(A^T)^{-1}$.*

Ba ma trận bị trộn lẫn vào nhau bởi $A^T C A$, và chúng không thể dễ dàng gỡ ra được. Nói chung, $A^T y = f$ có nhiều nghiệm. Và bốn phương trình $Au = e$ thường sẽ không có nghiệm với ba ẩn. Nhưng $A^T C A$ mang lại nghiệm chính xác cho cả ba phương trình trong khuôn khổ. Chỉ khi $m = n$ và các ma trận là ma trận vuông thì chúng ta mới có thể đi từ $y = (A^T)^{-1} f$ đến $e = C^{-1} y$ rồi đến $u = A^{-1}e$. Chúng ta sẽ thấy điều đó ngay bây giờ.

#### **Đầu Cố định và Đầu Tự do (Fixed End and Free End)**

Bỏ đi lò xo thứ tư. Tất cả các ma trận trở thành $3 \times 3$. Quy luật không thay đổi! Ma trận $A$ mất hàng thứ tư và (tất nhiên) $A^T$ mất cột thứ tư. Ma trận độ cứng mới $K_1$ trở thành tích của các ma trận vuông:
$$A_1^T C_1 A_1 = \begin{bmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} c_1 & & \\ & c_2 & \\ & & c_3 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix}.$$

Cột bị thiếu của $A^T$ và hàng của $A$ đã nhân với $c_4$ bị thiếu. Vì vậy cách nhanh nhất để tìm $A^T C A$ mới là đặt $c_4 = 0$ trong cái cũ:
| **CỐ ĐỊNH TỰ DO** | $A_1^T C_1 A_1 = \begin{bmatrix} c_1 + c_2 & -c_2 & 0 \\ -c_2 & c_2 + c_3 & -c_3 \\ 0 & -c_3 & c_3 \end{bmatrix}$ | . | (12) |
|-------------------|-------------------------------------------------------------------------------------------------------------------|---|------|

**Ví dụ 2** Nếu $c_1 = c_2 = c_3 = 1$ và $C = I$, đây là ma trận ba đường chéo $-1, 2, -1$ $K_1$. Phần tử cuối cùng của $K_1$ là 1 thay vì 2 vì lò xo ở phía dưới là tự do. Giả sử tất cả $m_j = m$:
| Cố định-tự do | $u = K_1^{-1} f = \frac{1}{c} \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 2 \\ 1 & 2 & 3 \end{bmatrix} \begin{bmatrix} mg \\ mg \\ mg \end{bmatrix} = \frac{mg}{c} \begin{bmatrix} 3 \\ 5 \\ 6 \end{bmatrix}$ |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Những chuyển động đó lớn hơn trường hợp tự do-tự do. Con số 3 xuất hiện trong $u_1$ vì cả ba khối lượng đều đang kéo lò xo đầu tiên xuống. Khối lượng tiếp theo di chuyển một đoạn bằng 3 đó cộng thêm một khoảng bằng 2 từ các khối lượng bên dưới nó. Khối lượng thứ ba tụt xuống nhiều hơn nữa ($3 + 2 + 1 = 6$). Độ giãn $e = Au$ trong các lò xo hiển thị những con số 3, 2, 1 đó:
| $e = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix} \frac{mg}{c} \begin{bmatrix} 3 \\ 5 \\ 6 \end{bmatrix} = \frac{mg}{c} \begin{bmatrix} 3 \\ 2 \\ 1 \end{bmatrix}$ |
|---------------------------------------------------------------------------|

# **Hai Đầu Tự do:** $K$ là **Suy biến (Two Free Ends: $K$ is Singular)**

Sự tự do ở *cả hai đầu* đồng nghĩa với rắc rối. Toàn bộ đường thẳng có thể di chuyển. $A$ có kích thước $2 \times 3$:
| TỰ DO-TỰ DO | $\begin{bmatrix} e_1 \\ e_2 \end{bmatrix} = \begin{bmatrix} u_2 - u_1 \\ u_3 - u_2 \end{bmatrix} = \begin{bmatrix} -1 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix} \begin{bmatrix} u_1 \\ u_2 \\ u_3 \end{bmatrix}$ | (13) |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------|------|

Bây giờ có một nghiệm khác không cho $Au = 0$. *Các khối lượng có thể di chuyển mà không làm giãn các lò xo.* Toàn bộ đường thẳng có thể dịch chuyển một khoảng $u = (1, 1, 1)$ và điều này để lại $e = (0, 0)$:
| $Au = \begin{bmatrix} -1 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} =$ không có sự kéo giãn. \quad (14) |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

$Au = 0$ chắc chắn dẫn đến $A^T C Au = 0$. Khi đó $A^T C A$ chỉ là *nửa xác định dương (positive semidefinite)*, không có $c_1$ và $c_4$. Các phần tử chốt sẽ là $c_2$ và $c_3$ và *không có phần tử chốt thứ ba*. Hạng chỉ là 2:
$$\begin{bmatrix} -1 & 0 \\ 1 & -1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} c_2 & & \\ & c_3 \end{bmatrix} \begin{bmatrix} -1 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix} = \begin{bmatrix} c_2 & -c_2 & 0 \\ -c_2 & c_2 + c_3 & -c_3 \\ 0 & -c_3 & c_3 \end{bmatrix} \quad (15)$$

Hai giá trị riêng sẽ là số dương nhưng $x = (1, 1, 1)$ là một vectơ riêng tương ứng với $\lambda = 0$. Chúng ta có thể giải $A^T C Au = f$ chỉ cho những vectơ đặc biệt $f$. Các lực phải cộng lại thành $f_1 + f_2 + f_3 = 0$, nếu không toàn bộ dãy lò xo (với cả hai đầu tự do) sẽ cất cánh như một quả tên lửa.

### **Vòng Lò xo (Circle of Springs)**

Một lò xo thứ ba sẽ hoàn thành vòng tròn từ khối lượng 3 trở lại khối lượng 1. Điều này không làm cho $K$ khả nghịch - ma trận độ cứng $K_{\text{circular}}$ vẫn là suy biến:
| $A_{\text{circular}}^T A_{\text{circular}} = \begin{bmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \\ -1 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & -1 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix} = \begin{bmatrix} 2 & -1 & -1 \\ -1 & 2 & -1 \\ -1 & -1 & 2 \end{bmatrix}, \quad (16)$ |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Các phần tử chốt duy nhất là 2 và $\frac{3}{2}$. Các giá trị riêng là 3 và 3 và 0. Định thức bằng không. Không gian hạt nhân vẫn chứa $x = (1, 1, 1)$, khi tất cả các khối lượng di chuyển cùng nhau. Vectơ chuyển động $(1, 1, 1)$ này nằm trong không gian hạt nhân của $A_{\text{circular}}$ và $K_{\text{circular}} = A^T C A$.

Cho phép tôi tóm tắt phần này. Tôi hy vọng ví dụ này sẽ giúp bạn kết nối giải tích với đại số tuyến tính, thay thế các phương trình vi phân bằng các phương trình sai phân. Nếu bước $\Delta x$ của bạn đủ nhỏ, bạn sẽ có một lời giải hoàn toàn thỏa đáng.

Phương trình là
$$-\frac{d}{dx} \left( c(x) \frac{du}{dx} \right) = f(x)$$
với $u(0) = 0$ và $\left[ u(1) \text{ hoặc } \frac{du}{dx}(1) \right] = 0$.

Chia thanh thành $N$ đoạn có chiều dài $\Delta x$. Thay $\frac{du}{dx}$ bằng $Au$ và $-\frac{dy}{dx}$ bằng $A^T y$. Bây giờ $A$ và $A^T$ bao gồm $1/\Delta x$. Các điều kiện biên là $u_0 = 0$ và $[u_N = 0 \text{ hoặc } y_N = 0]$. Ba bước $-d/dx$ và $c(x)$ và $d/dx$ tương ứng với $A^T$ và $C$ và $A$:
$$f = A^T y \quad \text{và} \quad y = Ce \quad \text{và} \quad e = Au \quad \text{cho ra} \quad A^T C Au = f.$$

Đây là một ví dụ cơ bản trong khoa học và kỹ thuật tính toán.

1. Lập mô hình bài toán bằng một phương trình vi phân.
2. Rời rạc hóa phương trình vi phân thành một phương trình sai phân.
3. Hiểu và giải phương trình sai phân (và các điều kiện biên!).
4. Diễn giải nghiệm; hình dung nó; thiết kế lại nếu cần.

Mô phỏng số đã trở thành một nhánh thứ ba của khoa học, bên cạnh thực nghiệm và suy luận. Việc thiết kế bằng máy tính cho chiếc Boeing 777 ít tốn kém hơn nhiều so với việc sử dụng một hầm gió.

Hai cuốn sách *Introduction to Applied Mathematics* và *Computational Science and Engineering* (Nhà xuất bản Wellesley-Cambridge) phát triển toàn bộ chủ đề này xa hơn - hãy xem trang của khóa học **math.mit.edu/18085** với các bài giảng video (Các bài giảng cũng có trên **ocw.mit.edu** và **YouTube**). Tôi hy vọng cuốn sách này giúp bạn nhìn thấy khuôn khổ đằng sau các phép tính.

### **Tập bài tập 10.2 (Problem Set 10.2)**

**1** Chứng minh rằng $\det(A_0^T C_0 A_0) = c_1 c_2 c_3 + c_1 c_3 c_4 + c_1 c_2 c_4 + c_2 c_3 c_4$. Cũng tìm $\det(A_1^T C_1 A_1)$ trong ví dụ cố định-tự do.
**2** Tìm nghịch đảo của $A_1^T C_1 A_1$ trong ví dụ cố định-tự do bằng cách nhân $A_1^{-1} C_1^{-1} (A_1^T)^{-1}$.
**3** Trong trường hợp tự do-tự do khi $A^T C A$ trong phương trình (15) là suy biến, hãy cộng ba phương trình $A^T C Au = f$ để thấy rằng chúng ta cần $f_1 + f_2 + f_3 = 0$. Tìm một nghiệm cho $A^T C Au = f$ khi các lực $f = (-1, 0, 1)$ tự cân bằng. Tìm tất cả các nghiệm!
**4** Cả hai điều kiện biên cho phương trình vi phân tự do-tự do là $du/dx = 0$:
$$-\frac{d}{dx} \left( c(x) \frac{du}{dx} \right) = f(x) \quad \text{với} \quad \frac{du}{dx} = 0 \quad \text{ở cả hai đầu.}$$
Tích phân hai vế để chỉ ra rằng lực $f(x)$ phải tự cân bằng, $\int f(x) dx = 0$, nếu không thì không có nghiệm. Nghiệm tổng quát là một nghiệm riêng $u(x)$ cộng với bất kỳ hằng số nào. Hằng số tương ứng với $u = (1, 1, 1)$ trong không gian hạt nhân của $A^T C A$.
**5** Trong bài toán cố định-tự do, ma trận $A$ là vuông và khả nghịch. Chúng ta có thể giải $A^T y = f$ tách biệt với $Au = e$. Hãy làm tương tự đối với phương trình vi phân:
Giải
$$-\frac{dy}{dx} = f(x)$$
với $y(1) = 0$. Vẽ đồ thị $y(x)$ nếu $f(x) = 1$.
**6** Ma trận $3 \times 3$ $K_1 = A_1^T C_1 A_1$ trong phương trình (6) tách thành ba "ma trận phần tử (element matrices)" $c_1 E_1 + c_2 E_2 + c_3 E_3$. Viết ra những thành phần đó, một cho mỗi $c$. Chỉ ra cách chúng đến từ phép nhân *cột nhân hàng* của $A_1^T C_1 A_1$. Đây là cách các ma trận độ cứng của phần tử hữu hạn thực sự được lắp ráp.
**7** Đối với năm lò xo và bốn khối lượng với cả hai đầu cố định, các ma trận $A$ và $C$ và $K$ là gì? Với $C = I$, giải $Ku = \text{ones}(4)$.
**8** So sánh nghiệm $u = (u_1, u_2, u_3, u_4)$ trong Bài tập 7 với nghiệm của bài toán liên tục $-u'' = 1$ với $u(0) = 0$ và $u(1) = 0$. Parabol $u(x)$ sẽ tương ứng tại $x = \frac{1}{5}, \frac{2}{5}, \frac{3}{5}, \frac{4}{5}$ với $u$ - liệu có một hệ số $(\Delta x)^2$ cần tính đến không?
**9** Giải bài toán cố định-tự do $-u'' = mg$ với $u(0) = 0$ và $u'(1) = 0$. So sánh $u(x)$ tại $x = \frac{1}{3}, \frac{2}{3}, 1$ với vectơ $u = (3mg, 5mg, 6mg)$ trong Ví dụ 2.
**10** Giả sử $c_1 = c_2 = c_3 = c_4 = 1, m_1 = 2$ và $m_2 = m_3 = 1$. Giải $A^T C Au = (2, 1, 1)$ cho dãy lò xo cố định-cố định này. Khối lượng nào di chuyển nhiều nhất ($u$ lớn nhất)?
**11** (MATLAB) Tìm độ dịch chuyển $u(1), \dots, u(100)$ của 100 khối lượng được nối bằng các lò xo đều có $c = 1$. Mỗi lực là $f(i) = 0.01$. In các đồ thị của $u$ với các đầu **cố định-cố định** và **cố định-tự do**. Lưu ý rằng $\text{diag}(\text{ones}(n, 1), d)$ là một ma trận với $n$ số một dọc theo đường chéo $d$. Lệnh in này sẽ vẽ đồ thị một vectơ $u$:
| `plot(u, '+')` ; | `xlabel('mass number')` ; | `ylabel('movement')` ; |
|-------------------------|-----------------------------------------|--------------------------------------|
**12** (MATLAB) Kỹ thuật hóa học có một đạo hàm bậc nhất $du/dx$ từ vận tốc chất lỏng cũng như $d^2u/dx^2$ từ sự khuếch tán. Thay thế $du/dx$ bằng một sai phân *tiến*, rồi một sai phân *trung tâm*, rồi một sai phân *lùi*, với $\Delta x = \frac{1}{10}$. Vẽ ba đồ thị nghiệm số của bạn của phương trình
$$-\frac{d^2u}{dx^2} + 10 \frac{du}{dx} = 1$$
với $u(0) = u(1) = 0$.
*Phương trình đối lưu-khuếch tán (convection-diffusion equation)* này xuất hiện ở khắp mọi nơi. Nó biến đổi thành phương trình Black-Scholes cho giá quyền chọn trong toán tài chính.
Bài 12 được phát triển thành bài tập về nhà MATLAB đầu tiên trong khóa học 18.085 của tôi về Khoa học và Kỹ thuật Tính toán tại MIT. Video trên *ocw.mit.edu*.

# **10.3 Ma trận Markov, Quần thể và Kinh tế học (Markov Matrices, Population, and Economics)**

Phần này viết về *các ma trận dương:* mọi $a_{ij} > 0$. Sự thật then chốt có thể phát biểu rất nhanh: *Giá trị riêng lớn nhất là số thực và dương và vectơ riêng của nó cũng vậy.* Trong kinh tế học, sinh thái học, động lực học quần thể và bước đi ngẫu nhiên, sự thật đó tiến xa một chặng đường dài:

| Markov | $\lambda_{\max} = 1$ | Quần thể | $\lambda_{\max} > 1$ | Tiêu dùng | $\lambda_{\max} < 1$ |
|--------|----------------------|------------|----------------------|-------------|----------------------|

$\lambda_{\max}$ kiểm soát các lũy thừa của $A$. Chúng ta sẽ thấy điều này trước tiên đối với $\lambda_{\max} = 1$.

#### **Ma trận Markov (Markov Matrices)**

Nhân một vectơ dương $u_0$ nhiều lần với ma trận $A$ này:

| Ma trận Markov | $A = \begin{bmatrix} .8 & .3 \\ .2 & .7 \end{bmatrix}$ | $u_1 = Au_0$ | $u_2 = Au_1 = A^2u_0$ |
|---------------|--------------------------------------------------------|--------------|-----------------------|

Sau $k$ bước, chúng ta có $A^k u_0$. Các vectơ $u_1, u_2, u_3, \dots$ sẽ tiến tới một *"trạng thái ổn định (steady state)"* $u_{\infty} = (.6, .4)$. Kết quả cuối cùng này không phụ thuộc vào vectơ xuất phát $u_0$. *Đối với mọi $u_0 = (a, 1 - a)$ chúng ta đều hội tụ về cùng một $u_{\infty} = (.6, .4)$.* Câu hỏi đặt ra là tại sao.

Phương trình trạng thái ổn định $Au_{\infty} = u_{\infty}$ làm cho $u_{\infty}$ trở thành *một vectơ riêng ứng với giá trị riêng 1:*

| Trạng thái ổn định | $\begin{bmatrix} .8 & .3 \\ .2 & .7 \end{bmatrix} \begin{bmatrix} .6 \\ .4 \end{bmatrix} = \begin{bmatrix} .6 \\ .4 \end{bmatrix} = u_{\infty}.$ |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------|

Việc nhân với $A$ không làm thay đổi $u_{\infty}$. Nhưng điều này không giải thích được tại sao có quá nhiều vectơ $u_0$ lại dẫn đến $u_{\infty}$. Các ví dụ khác có thể có một trạng thái ổn định, nhưng nó không nhất thiết phải có tính thu hút:

| Không phải Markov | $B = \begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix}$ | có trạng thái ổn định không thu hút | $B \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ |
|------------|----------------------------------------------------|-----------------------------------|---------------------------------------------------------------------------------|

Trong trường hợp này, vectơ bắt đầu $u_0 = (0, 1)$ sẽ cho $u_1 = (0, 2)$ và $u_2 = (0, 4)$. Các thành phần thứ hai được nhân đôi. Theo ngôn ngữ của các giá trị riêng, $B$ có $\lambda = 1$ nhưng cũng có $\lambda = 2$ - điều này tạo ra sự không ổn định. Thành phần của $u$ dọc theo vectơ riêng không ổn định đó bị nhân với $\lambda$, và $|\lambda| > 1$ có nghĩa là sự bùng nổ (blowup).

Phần này viết về hai tính chất đặc biệt của $A$ đảm bảo *trạng thái ổn định vững bền (stable steady state).* Những tính chất này định nghĩa một *ma trận Markov* dương, và $A$ ở trên là một ví dụ cụ thể:

**Ma trận Markov**
**1.** *Mọi phần tử của $A$ đều dương: $a_{ij} > 0$.*
**2.** *Mọi cột của $A$ đều có tổng bằng 1.*

Cột 2 của $B$ có tổng bằng 2 chứ không phải 1. Khi $A$ là ma trận Markov, có hai sự thật xuất hiện ngay lập tức:
Bởi vì 1: Nhân một $u_0 \geq 0$ với $A$ tạo ra một $u_1 = Au_0 \geq 0$.
Bởi vì 2: Nếu các thành phần của $u_0$ cộng lại bằng 1, thì các thành phần của $u_1 = Au_0$ cũng vậy.

*Lý do:* Các thành phần của $u_0$ có tổng bằng 1 khi $\begin{bmatrix} 1 & 1 \end{bmatrix} u_0 = 1$. Điều này đúng cho từng cột của $A$ theo Tính chất 2. Sau đó theo phép nhân ma trận $\begin{bmatrix} 1 & \dots & 1 \end{bmatrix} A = \begin{bmatrix} 1 & \dots & 1 \end{bmatrix}$:
Những sự thật tương tự cũng áp dụng cho $u_2 = Au_1$ và $u_3 = Au_2$. Mọi vectơ $A^k u_0$ đều không âm với các thành phần có tổng bằng 1. Đây là *"các vectơ xác suất (probability vectors)."* Giới hạn $u_{\infty}$ cũng là một vectơ xác suất - nhưng chúng ta phải chứng minh rằng có một giới hạn. Chúng ta sẽ chỉ ra rằng $\lambda_{\max} = 1$ cho một ma trận Markov dương.

**Ví dụ 1** Tỷ lệ xe cho thuê ở Denver ban đầu là $l_0 = .02$. Tỷ lệ ở ngoài Denver là $.98$. Mỗi tháng, 80% xe ở Denver ở lại Denver (và 20% rời đi). Đồng thời 5% xe ở ngoài đi vào (95% ở lại bên ngoài). Điều này có nghĩa là các tỷ lệ $u_0 = (.02, .98)$ được nhân với $A$:
| Tháng đầu tiên | $A = \begin{bmatrix} .80 & .05 \\ .20 & .95 \end{bmatrix}$ | dẫn đến | $u_1 = Au_0 = A \begin{bmatrix} .02 \\ .98 \end{bmatrix} = \begin{bmatrix} .065 \\ .935 \end{bmatrix}$ |
|-------------|------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------|

Chú ý rằng $.065 + .935 = 1$. Tất cả các xe đều được tính đến. Mỗi bước nhân với $A$:
**Tháng tiếp theo** $\quad u_2 = Au_1 = (.09875, .90125)$. Đây là $A^2 u_0$.

Tất cả các vectơ này đều dương vì $A$ là ma trận dương. Mỗi vectơ $u_k$ sẽ có các thành phần có tổng bằng 1. Thành phần đầu tiên đã tăng từ $.02$ và ô tô đang di chuyển về phía Denver. Điều gì sẽ xảy ra về lâu dài?

Phần này liên quan đến các lũy thừa của ma trận. Việc hiểu $A^k$ là ứng dụng đầu tiên và tốt nhất của chúng ta về chéo hóa. Nơi mà $A^k$ có thể phức tạp, thì ma trận đường chéo $\Lambda^k$ lại đơn giản. Ma trận vectơ riêng $X$ kết nối chúng: $A^k$ bằng $X \Lambda^k X^{-1}$. Ứng dụng mới cho các ma trận Markov sử dụng các giá trị riêng (trong $\Lambda$) và các vectơ riêng (trong $X$). Chúng ta sẽ chỉ ra rằng $u_{\infty}$ **là một vectơ riêng của** $A$ **tương ứng với** $\lambda = 1$.

Vì mọi cột của $A$ đều có tổng bằng 1, nên không có gì bị mất đi hay được thêm vào. Chúng ta đang di chuyển xe cho thuê hoặc các quần thể, và không có xe hơi hay con người nào đột nhiên xuất hiện (hoặc biến mất). Các tỷ lệ cộng lại bằng 1 và ma trận $A$ giữ chúng theo cách đó. Câu hỏi là chúng được phân bố như thế nào sau $k$ khoảng thời gian - điều này dẫn chúng ta đến $A^k$.

**Lời giải** $A^k u_0$ cho các tỷ lệ trong và ngoài Denver sau $k$ bước. Chúng ta chéo hóa $A$ để hiểu $A^k$. Các giá trị riêng là $\lambda_1 = 1$ và $\lambda_2 = .75$ (vết là 1.75).
| $Ax = \lambda x$ | $A \begin{bmatrix} .2 \\ .8 \end{bmatrix} = 1 \begin{bmatrix} .2 \\ .8 \end{bmatrix}$ | và | $A \begin{bmatrix} -1 \\ 1 \end{bmatrix} = .75 \begin{bmatrix} -1 \\ 1 \end{bmatrix}$ |
|------------------|---------------------------------------------------------------------------------------|-----|---------------------------------------------------------------------------------------|

Vectơ xuất phát $u_0$ là tổ hợp của $x_1$ và $x_2$, trong trường hợp này với các hệ số $1$ và $.18$:
| Tổ hợp các vectơ riêng | $u_0 = \begin{bmatrix} .02 \\ .98 \end{bmatrix} = \begin{bmatrix} .2 \\ .8 \end{bmatrix} + .18 \begin{bmatrix} -1 \\ 1 \end{bmatrix}$ |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------|

Bây giờ nhân với $A$ để tìm $u_1$. Các vectơ riêng được nhân với $\lambda_1 = 1$ và $\lambda_2 = .75$:
| Mỗi $x$ được nhân với $\lambda$ | $u_1 = 1 \begin{bmatrix} .2 \\ .8 \end{bmatrix} + (.75)(.18) \begin{bmatrix} -1 \\ 1 \end{bmatrix}$ |
|-------------------------------------|---------------------------------------------------------------------------------------------------|

Mỗi tháng, một $\lambda = .75$ khác sẽ nhân với vectơ $x_2$. Vectơ riêng $x_1$ không thay đổi:
| Sau $k$ bước | $u_k = A^k u_0 = 1^k \begin{bmatrix} .2 \\ .8 \end{bmatrix} + (.75)^k (.18) \begin{bmatrix} -1 \\ 1 \end{bmatrix}$ |
|-----------------|------------------------------------------------------------------------------------------------------------------|

Phương trình này tiết lộ điều gì sẽ xảy ra. *Vectơ riêng $x_1$ với $\lambda = 1$ là trạng thái ổn định.* Vectơ riêng còn lại $x_2$ biến mất vì $|\lambda| < 1$. Càng thực hiện nhiều bước, chúng ta càng tiến gần đến $u_{\infty} = (.2, .8)$. Ở giới hạn, $\frac{2}{10}$ số xe ở Denver và $\frac{8}{10}$ ở bên ngoài. Đây là mô hình cho các chuỗi Markov, ngay cả khi bắt đầu từ $u_0 = (0, 1)$:

Nếu $A$ là một ma trận Markov *dương* (các phần tử $a_{ij} > 0$, mỗi cột có tổng bằng 1), thì $\lambda_1 = 1$ lớn hơn bất kỳ giá trị riêng nào khác. Vectơ riêng $x_1$ là *trạng thái ổn định:*
| $u_k = c_1 x_1 + c_2(\lambda_2)^k x_2 + \dots + c_n(\lambda_n)^k x_n$ | *luôn luôn tiến tới* | $u_{\infty} = c_1 x_1$ |
|-------------------------------------------------------------------|--------------------------|------------------|

Điểm đầu tiên là để thấy rằng $\lambda = 1$ là một giá trị riêng của $A$. *Lý do:* Mọi cột của $A - I$ đều có tổng bằng $1 - 1 = 0$. Các hàng của $A - I$ cộng lại thành một hàng toàn số không. Các hàng đó phụ thuộc tuyến tính, nên $A - I$ là ma trận suy biến. Định thức của nó bằng không và $\lambda = 1$ là một giá trị riêng.

Điểm thứ hai là không có giá trị riêng nào có thể có $|\lambda| > 1$. Với một giá trị riêng như vậy, các lũy thừa $A^k$ sẽ tăng lên. Nhưng $A^k$ cũng là một ma trận Markov! $A^k$ có các phần tử dương vẫn có tổng bằng 1 - và điều đó khiến nó không còn chỗ để trở nên lớn.

Một sự chú ý lớn được dành cho khả năng có một giá trị riêng khác có $|\lambda| = 1$.

**Ví dụ 2** $A = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ không có trạng thái ổn định vì $\lambda_2 = -1$.
Ma trận này gửi tất cả ô tô từ bên trong Denver ra bên ngoài, và ngược lại. Các lũy thừa $A^k$ luân phiên giữa $A$ và $I$. Vectơ riêng thứ hai $x_2 = (-1, 1)$ sẽ được nhân với $\lambda_2 = -1$ ở mỗi bước - và không trở nên nhỏ hơn: Không có trạng thái ổn định.

Giả sử các phần tử của $A$ hoặc bất kỳ lũy thừa nào của $A$ đều *dương - không cho phép số 0*. Trong trường hợp "chính quy (regular)" hay "nguyên thủy (primitive)" này, $\lambda = 1$ lớn hơn hẳn bất kỳ giá trị riêng nào khác. Các lũy thừa $A^k$ tiến tới ma trận hạng một có trạng thái ổn định trong mọi cột.

**Ví dụ 3 ("Mọi người đều di chuyển")** Bắt đầu với ba nhóm. Tại mỗi bước thời gian, một nửa của nhóm 1 đi đến nhóm 2 và một nửa còn lại đi đến nhóm 3. Các nhóm khác cũng *chia đôi và di chuyển.* Thực hiện một bước từ quần thể xuất phát $p_1, p_2, p_3$:
$$\text{Quần thể mới} \quad u_1 = Au_0 = \begin{bmatrix} 0 & \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & 0 & \frac{1}{2} \\ \frac{1}{2} & \frac{1}{2} & 0 \end{bmatrix} \begin{bmatrix} p_1 \\ p_2 \\ p_3 \end{bmatrix} = \begin{bmatrix} \frac{1}{2}p_2 + \frac{1}{2}p_3 \\ \frac{1}{2}p_1 + \frac{1}{2}p_3 \\ \frac{1}{2}p_1 + \frac{1}{2}p_2 \end{bmatrix}.$$

$A$ là một ma trận Markov. Không có ai được sinh ra hoặc mất đi. $A$ chứa các số không, điều này đã gây rắc rối trong Ví dụ 2. Nhưng sau hai bước trong ví dụ mới này, các số không biến mất khỏi $A^2$:
**Ma trận hai bước (Two-step matrix)**
$$u_2 = A^2 u_0 = \begin{bmatrix} \frac{1}{2} & \frac{1}{4} & \frac{1}{4} \\ \frac{1}{4} & \frac{1}{2} & \frac{1}{4} \\ \frac{1}{4} & \frac{1}{4} & \frac{1}{2} \end{bmatrix} \begin{bmatrix} p_1 \\ p_2 \\ p_3 \end{bmatrix}$$

Các giá trị riêng của $A$ là $\lambda_1 = 1$ (vì $A$ là Markov) và $\lambda_2 = \lambda_3 = -1/2$. Đối với $\lambda_1 = 1$, *vectơ riêng $x_1 = (1/3, 1/3, 1/3)$ sẽ là trạng thái ổn định.* Khi ba quần thể bằng nhau chia đôi và di chuyển, các quần thể lại bằng nhau. Bắt đầu từ $u_0 = (8, 16, 32)$, chuỗi Markov tiến tới trạng thái ổn định của nó:
| $u_0 = \begin{bmatrix} 8 \\ 16 \\ 32 \end{bmatrix}$ | $u_1 = \begin{bmatrix} 24 \\ 20 \\ 12 \end{bmatrix}$ | $u_2 = \begin{bmatrix} 16 \\ 18 \\ 22 \end{bmatrix}$ | $u_3 = \begin{bmatrix} 20 \\ 19 \\ 17 \end{bmatrix}$ |
|-----------------------------------------------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|

Bước tới $u_4$ sẽ chia đôi một số người. Điều này không thể tránh khỏi. Tổng dân số là $8 + 16 + 32 = 56$ ở mỗi bước. Trạng thái ổn định là 56 nhân $(1/3, 1/3, 1/3)$. Bạn có thể thấy ba quần thể đang tiến lại gần, nhưng không bao giờ đạt tới, giới hạn cuối cùng $56/3$ của chúng.

Bài tập thử thách 6.7.16 đã tạo ra một ma trận Markov $A$ từ số lượng liên kết giữa các trang web. Trạng thái ổn định $u$ sẽ cung cấp các thứ hạng của Google. *Google tìm $u$ bằng một cuộc đi dạo ngẫu nhiên theo các liên kết (lướt web ngẫu nhiên).* Vectơ riêng đó đến từ việc đếm tỷ lệ phần trăm số lượt truy cập vào mỗi trang web - một cách nhanh chóng để tính toán trạng thái ổn định.

Độ lớn $|\lambda_2|$ của giá trị riêng thứ hai kiểm soát tốc độ hội tụ về trạng thái ổn định.

#### **Định lý Perron-Frobenius (Perron-Frobenius Theorem)**

Một định lý ma trận thống trị chủ đề này. Định lý Perron-Frobenius áp dụng khi mọi $a_{ij} \geq 0$. Không có yêu cầu nào về việc các cột phải có tổng bằng 1. Chúng ta sẽ chứng minh dạng gọn nhất, khi mọi $a_{ij} > 0$: bất kỳ ma trận dương $A$ nào (không nhất thiết phải xác định dương!).

*Perron-Frobenius cho $A > 0$: Tất cả các con số trong $Ax = \lambda_{\max} x$ đều dương hẳn.*

*Chứng minh.* Ý tưởng then chốt là xem xét tất cả các số $t$ sao cho $Ax \geq tx$ cho một vectơ không âm $x$ nào đó (khác $x = 0$). Chúng ta đang cho phép dấu bất đẳng thức trong $Ax \geq tx$ để có nhiều ứng cử viên dương nhỏ $t$. Đối với giá trị lớn nhất $t_{\max}$ (đạt được), chúng ta sẽ chứng minh rằng *đẳng thức xảy ra: $Ax = t_{\max} x$.*

Nếu không, nếu $Ax \geq t_{\max} x$ không phải là một đẳng thức, hãy nhân với $A$. Vì $A$ dương nên điều đó tạo ra một bất đẳng thức ngặt $A^2 x > t_{\max} Ax$. Do đó vectơ dương $y = Ax$ thỏa mãn $Ay > t_{\max} y$, và $t_{\max}$ có thể được tăng lên. Sự mâu thuẫn này buộc phải có đẳng thức $Ax = t_{\max} x$, và *chúng ta có một giá trị riêng.* Vectơ riêng của nó $x$ là dương vì ở vế trái của đẳng thức đó, $Ax$ chắc chắn là dương.

Để thấy rằng không có giá trị riêng nào có thể lớn hơn $t_{\max}$, giả sử $Az = \lambda z$. Vì $\lambda$ và $z$ có thể liên quan đến số âm hoặc số phức, chúng ta lấy giá trị tuyệt đối: $|A| |z| = |Az| \leq |\lambda| |z|$ theo "bất đẳng thức tam giác." $|z|$ này là một vectơ không âm, vì vậy $|\lambda|$ này là một trong những ứng cử viên khả dĩ $t$. Do đó $|\lambda|$ không thể vượt quá $t_{\max}$ - đây chính là $\lambda_{\max}$.

### **Sự tăng trưởng Quần thể (Population Growth)**

Chia quần thể thành ba nhóm tuổi: tuổi < 20, tuổi 20 đến 39, và tuổi 40 đến 59. Tại năm $T$ quy mô của những nhóm đó là $n_1, n_2, n_3$. Hai mươi năm sau, quy mô đã thay đổi vì ba lý do: sinh ra, chết đi, và già đi.

1. **Sinh sản (Reproduction):** $n_1^{\text{new}} = F_1 n_1 + F_2 n_2 + F_3 n_3$ tạo ra một thế hệ mới.
2. **Sống sót (Survival):** $n_2^{\text{new}} = P_1 n_1$ và $n_3^{\text{new}} = P_2 n_2$ tạo ra các thế hệ già hơn.

Tỷ lệ sinh sản là $F_1, F_2, F_3$ ($F_2$ lớn nhất). *Ma trận Leslie $A$* có thể trông như thế này:
$$\begin{bmatrix} n_1 \\ n_2 \\ n_3 \end{bmatrix}_{\text{new}} = \begin{bmatrix} F_1 & F_2 & F_3 \\ P_1 & 0 & 0 \\ 0 & P_2 & 0 \end{bmatrix} \begin{bmatrix} n_1 \\ n_2 \\ n_3 \end{bmatrix}_{\text{old}} = \begin{bmatrix} .04 & 1.1 & .01 \\ .08 & 0 & 0 \\ 0 & .92 & 0 \end{bmatrix} \begin{bmatrix} n_1 \\ n_2 \\ n_3 \end{bmatrix}_{\text{old}}.$$

Đây là hình thức dự phóng dân số đơn giản nhất, ma trận $A$ giống nhau ở mỗi bước. Trong một mô hình thực tế, $A$ sẽ thay đổi theo thời gian (từ môi trường hoặc các yếu tố bên trong). Các giáo sư có thể muốn bao gồm một nhóm thứ tư, tuổi $\geq 60$, nhưng chúng ta không cho phép điều đó.

Ma trận có $A \geq 0$ nhưng không phải $A > 0$. Định lý Perron-Frobenius vẫn áp dụng vì $A^3 > 0$. Giá trị riêng lớn nhất là $\lambda_{\max} \approx 1.06$. Bạn có thể quan sát các thế hệ di chuyển, bắt đầu từ $n_2 = 1$ ở thế hệ giữa:
| $eig(A) =$ | $1.06$ | $A^2 =$ | $\begin{bmatrix} 1.08 & 0.05 & .00 \\ 0.04 & 1.08 & .00 \\ 0.90 & 0 & 0 \end{bmatrix}$ | $A^3 =$ | $\begin{bmatrix} 1.00 & 1.19 & .00 \\ 0.06 & 0.05 & .00 \\ 0.04 & 0.99 & .00 \end{bmatrix}$ |
|------------|------|---------|----------------------------------------------------------------------------------------|---------|---------------------------------------------------------------------------------------------|

Một khởi đầu nhanh sẽ đến từ $u_0 = (0, 1, 0)$. Nhóm giữa đó sẽ sinh sản $1.1$ và cũng sống sót $.92$. Thế hệ mới nhất và già nhất nằm trong $u_1 = (1.1, 0, .92) = \text{cột 2 của } A$. Sau đó $u_2 = Au_1 = A^2 u_0$ là cột thứ hai của $A^2$. Các con số ban đầu (độ quá độ) phụ thuộc rất nhiều vào $u_0$, nhưng *tốc độ tăng trưởng tiệm cận (asymptotic growth rate)* $\lambda_{\max}$ *là giống nhau từ mọi điểm xuất phát.* Vectơ riêng của nó $x = (.63, .58, .51)$ cho thấy cả ba nhóm phát triển đều đặn cùng nhau.

Cuốn sách của Caswell về *Mô hình Quần thể Ma trận (Matrix Population Models)* nhấn mạnh phân tích độ nhạy. Mô hình không bao giờ chính xác hoàn toàn. Nếu các chữ $F$ hoặc $P$ trong ma trận thay đổi 10%, liệu $\lambda_{\max}$ có đi xuống dưới 1 (điều này có nghĩa là tuyệt chủng) không? Bài tập 19 sẽ chỉ ra rằng sự thay đổi ma trận $\Delta A$ tạo ra sự thay đổi giá trị riêng $\Delta \lambda = y^T (\Delta A)x$. Ở đây $x$ và $y^T$ là các vectơ riêng bên phải và bên trái của $A$, với $Ax = \lambda x$ và $A^T y = \lambda y$.

### **Đại số Tuyến tính trong Kinh tế học: Ma trận Tiêu dùng (Linear Algebra in Economics: The Consumption Matrix)**

Một bài luận dài về đại số tuyến tính trong kinh tế học sẽ không phù hợp ở đây. Một lưu ý ngắn gọn về một ma trận có vẻ hợp lý. *Ma trận tiêu dùng (consumption matrix)* cho biết bao nhiêu lượng mỗi đầu vào (input) đi vào một đơn vị đầu ra (output). Điều này mô tả khía cạnh sản xuất của nền kinh tế.

**Ma trận tiêu dùng** Chúng ta có $n$ ngành công nghiệp như hóa chất, thực phẩm và dầu mỏ. Để sản xuất một đơn vị hóa chất có thể cần .2 đơn vị hóa chất, .3 đơn vị thực phẩm và .4 đơn vị dầu mỏ. Những con số đó đi vào hàng 1 của ma trận tiêu dùng $A$:
$$\begin{bmatrix} \text{đầu ra hóa chất} \\ \text{đầu ra thực phẩm} \\ \text{đầu ra dầu mỏ} \end{bmatrix} = \begin{bmatrix} .2 & .3 & .4 \\ .4 & .4 & .1 \\ .5 & .1 & .3 \end{bmatrix} \begin{bmatrix} \text{đầu vào hóa chất} \\ \text{đầu vào thực phẩm} \\ \text{đầu vào dầu mỏ} \end{bmatrix}.$$

Hàng 2 cho thấy các đầu vào để sản xuất thực phẩm - sử dụng nhiều hóa chất và thực phẩm, không dùng nhiều dầu mỏ. Hàng 3 của $A$ hiển thị các đầu vào được tiêu thụ để tinh chế một đơn vị dầu mỏ. Ma trận tiêu dùng thực tế của Hoa Kỳ năm 1958 chứa 83 ngành. Các mô hình trong thập niên 1990 lớn hơn và chính xác hơn nhiều. Chúng tôi đã chọn một ma trận tiêu dùng có một vectơ riêng thuận tiện.

Bây giờ là câu hỏi: Nền kinh tế này có thể đáp ứng được các nhu cầu (demands) $y_1, y_2, y_3$ đối với hóa chất, thực phẩm và dầu mỏ không? Để làm được điều đó, các đầu vào $p_1, p_2, p_3$ sẽ phải cao hơn - bởi vì một phần của $p$ được tiêu thụ trong quá trình sản xuất $y$. Đầu vào là $p$ và lượng tiêu thụ là $Ap$, phần còn lại là đầu ra $p - Ap$. Lượng sản xuất ròng (net production) này chính là phần đáp ứng nhu cầu $y$:
**Bài toán** Tìm một vectơ $p$ sao cho $p - Ap = y$ hoặc $p = (I - A)^{-1}y$.

Có vẻ như câu hỏi về đại số tuyến tính là liệu $I - A$ có khả nghịch hay không. Nhưng bài toán còn nhiều điều hơn thế. Vectơ $y$ gồm các sản lượng cần thiết là không âm, và $A$ cũng vậy. Các mức sản xuất trong $p = (I - A)^{-1}y$ cũng phải không âm. Câu hỏi thực sự là:
**Khi nào $(I - A)^{-1}$ là một ma trận không âm?**

Đây là phép thử nghiệm trên $(I - A)^{-1}$ đối với một nền kinh tế có năng suất, có thể đáp ứng bất kỳ nhu cầu nào. Nếu $A$ nhỏ so với $I$, thì $Ap$ nhỏ so với $p$. Có nhiều sản lượng. Nếu $A$ quá lớn, thì quá trình sản xuất tiêu thụ quá nhiều và không thể đáp ứng được nhu cầu $y$.

"Nhỏ" hoặc "lớn" được quyết định bởi giá trị riêng lớn nhất $\lambda_1$ của $A$ (là số dương):
- Nếu $\lambda_1 > 1$ thì $(I - A)^{-1}$ có các phần tử âm.
- Nếu $\lambda_1 = 1$ thì $(I - A)^{-1}$ không tồn tại.
- Nếu $\lambda_1 < 1$ thì $(I - A)^{-1}$ không âm như mong muốn.

Điểm chính yếu là điểm cuối cùng. Cách suy luận sử dụng một công thức đẹp đẽ cho $(I - A)^{-1}$, mà chúng tôi sẽ đưa ra ngay bây giờ. Chuỗi vô hạn quan trọng nhất trong toán học là **chuỗi cấp số nhân (geometric series)** $1 + x + x^2 + \dots$. Chuỗi này có tổng bằng $1/(1 - x)$ miễn là $x$ nằm trong khoảng giữa $-1$ và $1$. Khi $x = 1$, chuỗi là $1 + 1 + 1 + \dots = \infty$. Khi $|x| \geq 1$ các số hạng $x^n$ không tiến tới không và chuỗi không có cơ hội hội tụ.

Công thức đẹp cho $(I - A)^{-1}$ là **chuỗi cấp số nhân của ma trận (geometric series of matrices):**
**Chuỗi cấp số nhân**
$$(I - A)^{-1} = I + A + A^2 + A^3 + \dots$$

Nếu bạn nhân chuỗi $S = I + A + A^2 + \dots$ với $A$, bạn sẽ nhận được chuỗi y hệt ngoại trừ phần $I$. Do đó $S - AS = I$, tức là $(I - A)S = I$. Chuỗi có tổng là $S = (I - A)^{-1}$ nếu nó hội tụ. *Và nó hội tụ nếu tất cả các giá trị riêng của $A$ có $|\lambda| < 1$.*

Trong trường hợp của chúng ta $A \geq 0$. Tất cả các số hạng của chuỗi đều không âm. Tổng của nó là $(I - A)^{-1} \geq 0$.

**Ví dụ 4** $A = \begin{bmatrix} .2 & .3 & .4 \\ .4 & .4 & .1 \\ .5 & .1 & .3 \end{bmatrix}$ có $\lambda_{\max} = \mathbf{.9}$ và $(I - A)^{-1} = \frac{1}{93} \begin{bmatrix} 41 & 25 & 27 \\ 33 & 36 & 24 \\ 34 & 23 & 36 \end{bmatrix}$.
Nền kinh tế này có năng suất. $A$ nhỏ so với $I$, vì $\lambda_{\max}$ là .9. Để đáp ứng nhu cầu $y$, hãy bắt đầu từ $p = (I - A)^{-1}y$. Sau đó $Ap$ được tiêu thụ trong sản xuất, để lại $p - Ap$. Đây là $(I - A)p = y$, và nhu cầu được đáp ứng.

**Ví dụ 5**
$$A = \begin{bmatrix} 0 & 4 \\ 1 & 0 \end{bmatrix}$$
có $\lambda_{\max} = 2$ và $(I - A)^{-1} = -\frac{1}{3} \begin{bmatrix} 1 & 4 \\ 1 & 1 \end{bmatrix}$.

Ma trận tiêu dùng $A$ này quá lớn. Các nhu cầu không thể được đáp ứng, vì sản xuất tiêu thụ nhiều hơn những gì nó tạo ra. Chuỗi $I + A + A^2 + \dots$ không hội tụ về $(I - A)^{-1}$ vì $\lambda_{\max} > 1$. Chuỗi ngày càng lớn trong khi $(I - A)^{-1}$ thực ra là số âm.
Giống như vậy, $1 + 2 + 4 + \dots$ thực sự không phải là $1/(1 - 2) = -1$. Nhưng cũng không hoàn toàn sai!

### **Tập bài tập 10.3 (Problem Set 10.3)**

**Các câu hỏi từ 1-12 về ma trận Markov và các giá trị riêng cùng các lũy thừa của chúng.**

**1** Tìm các giá trị riêng của ma trận Markov này (tổng của chúng là vết):
$$A = \begin{bmatrix} .90 & .15 \\ .10 & .85 \end{bmatrix}.$$
Vectơ riêng trạng thái ổn định cho giá trị riêng $\lambda_1 = 1$ là gì?
**2** Chéo hóa ma trận Markov trong Bài tập 1 thành $A = X \Lambda X^{-1}$ bằng cách tìm vectơ riêng còn lại của nó:
$$A = \begin{bmatrix} & & & \\ & & 1 & \\ & & & 1 \\ & & & 1 \end{bmatrix} \begin{bmatrix} 1 & & & \\ & .75 & & \\ & & .75 & \\ & & & .75 \end{bmatrix}.$$
Giới hạn của $A^k = X \Lambda^k X^{-1}$ là gì khi $\Lambda^k = \begin{bmatrix} 1 & 0 \\ 0 & .75^k \end{bmatrix}$ tiến tới $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$?
**3** Các giá trị riêng và các vectơ riêng trạng thái ổn định của các ma trận Markov này là gì?
$$A = \begin{bmatrix} 1 & .2 \\ 0 & .8 \end{bmatrix} \quad A = \begin{bmatrix} .2 & 1 \\ .8 & 0 \end{bmatrix} \quad A = \begin{bmatrix} \frac{1}{2} & \frac{1}{4} & \frac{1}{4} \\ \frac{1}{4} & \frac{1}{2} & \frac{1}{4} \\ \frac{1}{4} & \frac{1}{4} & \frac{1}{2} \end{bmatrix}.$$
**4** Đối với mọi ma trận Markov $4 \times 4$, vectơ riêng nào của $A^T$ tương ứng với giá trị riêng (đã biết) $\lambda = 1$?
**5** Mỗi năm có 2% thanh niên trở thành người già và 3% người già chết đi. (Không có người sinh ra.) Tìm trạng thái ổn định cho
$$\begin{bmatrix} \text{trẻ} \\ \text{già} \\ \text{chết} \end{bmatrix}_{k+1} = \begin{bmatrix} .98 & .00 & 0 \\ .02 & .97 & 0 \\ .00 & .03 & 1 \end{bmatrix} \begin{bmatrix} \text{trẻ} \\ \text{già} \\ \text{chết} \end{bmatrix}_k.$$
**6** Đối với một ma trận Markov, tổng các thành phần của $x$ bằng tổng các thành phần của $Ax$. Nếu $Ax = \lambda x$ với $\lambda \neq 1$, chứng minh rằng các thành phần của vectơ riêng không ở trạng thái ổn định $x$ này có tổng bằng không.

**7** Tìm các giá trị riêng và vectơ riêng của $A$. Giải thích tại sao $A^k$ tiến tới $A^\infty$:
$$A = \begin{bmatrix} .8 & .3 \\ .2 & .7 \end{bmatrix} \quad A^\infty = \begin{bmatrix} .6 & .6 \\ .4 & .4 \end{bmatrix}.$$
Bài tập thử thách: Những ma trận Markov nào tạo ra trạng thái ổn định $(.6, .4)$ đó?

**8** Vectơ riêng trạng thái ổn định của một ma trận hoán vị là $(\frac{1}{4}, \frac{1}{4}, \frac{1}{4}, \frac{1}{4})$. Trạng thái này *không* đạt được khi $u_0 = (0, 0, 0, 1)$. Các vectơ $u_1$ và $u_2$ và $u_3$ và $u_4$ là gì? Bốn giá trị riêng của $P$, là nghiệm của $\lambda^4 = 1$, là gì?
$$\text{Ma trận hoán vị} = \text{Ma trận Markov} \quad P = \begin{bmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \end{bmatrix}.$$

**9** Chứng minh rằng bình phương của một ma trận Markov cũng là một ma trận Markov.

**10** Nếu $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ là một ma trận Markov, các giá trị riêng của nó là 1 và \_\_\_\_\_. Vectơ riêng trạng thái ổn định là $x_1 = \text{\_\_\_\_\_}$.

**11** Điền đầy đủ $A$ thành một ma trận Markov và tìm vectơ riêng trạng thái ổn định. Khi $A$ là một ma trận Markov đối xứng, tại sao $x_1 = (1, \dots, 1)$ lại là trạng thái ổn định của nó?
$$A = \begin{bmatrix} .7 & .1 & .2 \\ .1 & .6 & .3 \\ - & - & - \end{bmatrix}.$$

**12** Phương trình vi phân Markov không phải là $du/dt = Au$ mà là $du/dt = (A - I)u$. Đường chéo là số âm, phần còn lại của $A - I$ là số dương. Các cột có tổng bằng 0, không phải 1.
Tìm $\lambda_1$ và $\lambda_2$ cho $B = A - I = \begin{bmatrix} -.2 & .3 \\ .2 & -.3 \end{bmatrix}$. Tại sao $A - I$ có $\lambda_1 = 0$?
Khi $e^{\lambda_1 t}$ và $e^{\lambda_2 t}$ nhân với $x_1$ và $x_2$, trạng thái ổn định khi $t \rightarrow \infty$ là gì?

**Các câu hỏi từ 13-15 về đại số tuyến tính trong kinh tế học.**

**13** Mỗi hàng của ma trận tiêu dùng trong Ví dụ 4 có tổng bằng .9. Tại sao điều đó làm cho $\lambda = .9$ trở thành một giá trị riêng, và vectơ riêng là gì?
**14** Nhân $I + A + A^2 + A^3 + \dots$ với $I - A$ để được $I$. Chuỗi có tổng là $(I - A)^{-1}$. Đối với $A = \begin{bmatrix} 0 & .5 \\ 1 & 0 \end{bmatrix}$, tìm $A^2$ và $A^3$ và sử dụng quy luật để tính tổng chuỗi.
**15** Đối với ma trận nào trong số những ma trận này thì $I + A + A^2 + \dots$ cho ra một ma trận không âm $(I - A)^{-1}$? Khi đó nền kinh tế có thể đáp ứng bất kỳ nhu cầu nào:
| $A = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ | $A = \begin{bmatrix} 0 & 4 \\ .2 & 0 \end{bmatrix}$ | $A = \begin{bmatrix} .5 & 1 \\ .5 & 0 \end{bmatrix}$ |
|----------------------------------------------------|-----------------------------------------------------|------------------------------------------------------|
Nếu nhu cầu là $y = (2, 6)$, các vectơ $p = (I - A)^{-1}y$ là gì?

**16** (Markov một lần nữa) Ma trận này có định thức bằng không. Các giá trị riêng của nó là gì?
$$A = \begin{bmatrix} .4 & .2 & .3 \\ .2 & .4 & .3 \\ .4 & .4 & .4 \end{bmatrix}.$$
Tìm giới hạn của $A^k u_0$ bắt đầu từ $u_0 = (1, 0, 0)$ và sau đó $u_0 = (100, 0, 0)$.

**17** Nếu $A$ là một ma trận Markov, tại sao $I + A + A^2 + \dots$ không có tổng bằng $(I - A)^{-1}$?
**18** Đối với ma trận Leslie, hãy chứng tỏ rằng $\det(A - \lambda I) = 0$ cho ra $F_1 \lambda^2 + F_2 P_1 \lambda + F_3 P_1 P_2 = \lambda^3$. Vế phải $\lambda^3$ lớn hơn khi $\lambda \rightarrow \infty$. Vế trái lớn hơn tại $\lambda = 1$ nếu $F_1 + F_2 P_1 + F_3 P_1 P_2 > 1$. Trong trường hợp đó, hai vế bằng nhau tại một giá trị riêng $\lambda_{\max} > 1$: *sự tăng trưởng.*
**19** *Độ nhạy của các giá trị riêng:* Sự thay đổi ma trận $\Delta A$ tạo ra sự thay đổi giá trị riêng $\Delta \lambda$. *Những thay đổi $\Delta \lambda_1, \dots, \Delta \lambda_n$ nằm trên đường chéo của* $(X^{-1} \Delta A X)$.
**Thử thách:** Bắt đầu từ $AX = X\Lambda$. Các vectơ riêng và giá trị riêng thay đổi một lượng $\Delta X$ và $\Delta \Lambda$:
$$(A + \Delta A)(X + \Delta X) = (X + \Delta X)(\Lambda + \Delta \Lambda) \text{ trở thành } A(\Delta X) + (\Delta A)X = X(\Delta \Lambda) + (\Delta X)\Lambda.$$
Các số hạng nhỏ $(\Delta A)(\Delta X)$ và $(\Delta X)(\Delta \Lambda)$ bị bỏ qua. *Nhân phương trình cuối cùng với* $X^{-1}$. Từ các số hạng bên trong, phần đường chéo của $X^{-1}(\Delta A)X$ cho $\Delta \Lambda$ như chúng ta muốn. *Tại sao các số hạng bên ngoài $X^{-1}A\Delta X$ và $X^{-1}\Delta X\Lambda$ lại triệt tiêu nhau trên đường chéo?*
| Giải thích $X^{-1}A = \Lambda X^{-1}$ và sau đó | $\text{diag}(\Lambda X^{-1} \Delta X) = \text{diag}(X^{-1} \Delta X \Lambda)$ |

**20** Giả sử $B > A > 0$, nghĩa là mỗi $b_{ij} > a_{ij} > 0$. Làm thế nào thảo luận về Perron-Frobenius chỉ ra rằng $\lambda_{\max}(B) > \lambda_{\max}(A)$?

# **10.4 Quy hoạch Tuyến tính (Linear Programming)**

Quy hoạch tuyến tính là đại số tuyến tính cộng với hai ý tưởng mới: *bất đẳng thức (inequalities)* và *cực tiểu hóa (minimization).* Điểm xuất phát vẫn là một phương trình ma trận $Ax = b$. Nhưng các nghiệm duy nhất được chấp nhận là *không âm (nonnegative).* Chúng ta yêu cầu $x \geq 0$ (nghĩa là không có thành phần nào của $x$ có thể âm). Ma trận có $n > m$, nhiều ẩn hơn phương trình. Nếu có bất kỳ nghiệm $x \geq 0$ nào cho $Ax = b$, thì có lẽ có rất nhiều. Quy hoạch tuyến tính chọn ra nghiệm $x^* \geq 0$ cực tiểu hóa chi phí:

> *Chi phí là $c_1 x_1 + \dots + c_n x_n$. Vectơ chiến thắng $x^*$ là nghiệm không âm của $Ax = b$ có chi phí nhỏ nhất.*

Vì vậy, một bài toán quy hoạch tuyến tính bắt đầu với một ma trận $A$ và hai vectơ $b$ và $c$:
- **i)** $A$ có $n > m$: ví dụ $A = \begin{bmatrix} 1 & 1 & 2 \end{bmatrix}$ (một phương trình, ba ẩn)
- **ii)** $b$ có $m$ thành phần cho $m$ phương trình $Ax = b$: ví dụ $b = \begin{bmatrix} 4 \end{bmatrix}$
- **iii)** *Vectơ chi phí (cost vector)* $c$ có $n$ thành phần: ví dụ $c = \begin{bmatrix} 5 & 3 & 8 \end{bmatrix}$.

Khi đó bài toán là cực tiểu hóa $c \cdot x$ với các yêu cầu $Ax = b$ và $x \geq 0$:
*Cực tiểu hóa* $5x_1 + 3x_2 + 8x_3$ *với điều kiện* $x_1 + x_2 + 2x_3 = 4$ *và* $x_1, x_2, x_3 \geq 0$.

Chúng ta đã nhảy ngay vào bài toán mà không giải thích nó xuất phát từ đâu. Quy hoạch tuyến tính thực chất là ứng dụng quan trọng nhất của toán học vào quản lý. Việc phát triển thuật toán nhanh nhất và mã code nhanh nhất có tính cạnh tranh rất cao. Bạn sẽ thấy rằng tìm $x^*$ khó hơn giải $Ax = b$, vì các yêu cầu bổ sung: $x^* \geq 0$ và chi phí tối thiểu $c^T x^*$. Chúng tôi sẽ giải thích bối cảnh, và *phương pháp đơn hình (simplex method)* nổi tiếng, và *các phương pháp điểm trong (interior point methods)*, sau khi giải quyết ví dụ.

Đầu tiên hãy xem xét các "ràng buộc": $Ax = b$ và $x \geq 0$. Phương trình $x_1 + x_2 + 2x_3 = 4$ cho một mặt phẳng trong không gian ba chiều. Tính không âm $x_1 \geq 0, x_2 \geq 0, x_3 \geq 0$ chặt mặt phẳng xuống thành một hình tam giác. Nghiệm $x^*$ phải nằm trong tam giác $PQR$ ở Hình 10.5.

Bên trong tam giác đó, mọi thành phần của $x$ đều dương. Trên các cạnh của $PQR$, một thành phần bằng không. Tại các góc $P$ và $Q$ và $R$, hai thành phần bằng không. *Nghiệm tối ưu $x^*$ sẽ là một trong những góc đó!* Bây giờ chúng ta sẽ chỉ ra lý do tại sao.

Tam giác chứa tất cả các vectơ $x$ thỏa mãn $Ax = b$ và $x \geq 0$. Những $x$ đó được gọi là *các điểm khả thi (feasible points)*, và tam giác là *tập khả thi (feasible set)*. Những điểm này là các ứng cử viên được phép trong việc cực tiểu hóa $c \cdot x$, đây là bước cuối cùng:
*Tìm $x^*$ trong tam giác $PQR$ để cực tiểu hóa chi phí $5x_1 + 3x_2 + 8x_3$.*

Các vectơ có chi phí *bằng không* nằm trên mặt phẳng $5x_1 + 3x_2 + 8x_3 = 0$. Mặt phẳng đó không gặp tam giác. Chúng ta không thể đạt được chi phí bằng không trong khi vẫn đáp ứng các yêu cầu về $x$. Vì vậy hãy tăng chi phí $C$ cho đến khi mặt phẳng $5x_1 + 3x_2 + 8x_3 = C$ gặp tam giác. Khi $C$ tăng lên, chúng ta có *các mặt phẳng song song di chuyển về phía tam giác.*

Hình 10.5: Tam giác chứa tất cả các nghiệm không âm: $Ax = b$ và $x \geq 0$. Nghiệm có chi phí thấp nhất $x^*$ là một góc $P, Q,$ hoặc $R$ của tập khả thi này.

Mặt phẳng đầu tiên $5x_1 + 3x_2 + 8x_3 = C$ chạm vào tam giác có chi phí cực tiểu $C$. *Điểm mà nó chạm vào là nghiệm $x^*$.* Điểm chạm này phải là một trong các góc $P$ hoặc $Q$ hoặc $R$. Một mặt phẳng chuyển động không thể chạm tới bên trong tam giác trước khi nó chạm vào một góc! Vì vậy hãy kiểm tra chi phí $5x_1 + 3x_2 + 8x_3$ tại mỗi góc:
| $P = (4, 0, 0)$ tốn $20$ | $Q = (0, 4, 0)$ tốn $12$ | $R = (0, 0, 2)$ tốn $16$. |
|--------------------------|--------------------------|---------------------------|

Người chiến thắng là $Q$. Khi đó $x^* = (0, 4, 0)$ giải được bài toán quy hoạch tuyến tính.

Nếu vectơ chi phí $c$ bị thay đổi, các mặt phẳng song song sẽ bị nghiêng. Đối với những thay đổi nhỏ, $Q$ vẫn là người chiến thắng. Đối với chi phí $c \cdot x = 5x_1 + 4x_2 + 7x_3$, điểm tối ưu $x^*$ di chuyển đến $R = (0, 0, 2)$. Chi phí cực tiểu bây giờ là $7 \cdot 2 = 14$.

**Lưu ý 1** Một số chương trình quy hoạch tuyến tính *tối đa hóa lợi nhuận* thay vì cực tiểu hóa chi phí. Toán học hầu như giống nhau. Các mặt phẳng song song bắt đầu với một giá trị lớn của $C$, thay vì một giá trị nhỏ. Chúng di chuyển về phía gốc tọa độ (thay vì ra xa), khi $C$ nhỏ dần. *Điểm chạm đầu tiên vẫn là một góc.*

**Lưu ý 2** Các yêu cầu $Ax = b$ và $x \geq 0$ có thể là không thể thỏa mãn. Phương trình $x_1 + x_2 + x_3 = -1$ không thể giải được với $x \geq 0$. *Tập khả thi đó là rỗng.*

**Lưu ý 3** Cũng có thể xảy ra trường hợp tập khả thi là *không bị chặn (unbounded).* Nếu yêu cầu là $x_1 + x_2 - 2x_3 = 4$, vectơ dương lớn $(100, 100, 98)$ bây giờ là một ứng cử viên. Vectơ lớn hơn $(1000, 1000, 998)$ cũng vậy. Mặt phẳng $Ax = b$ không còn bị chặt thành một tam giác nữa. Hai góc $P$ và $Q$ vẫn là các ứng cử viên cho $x^*$, nhưng $R$ đã di chuyển ra vô cực.

**Lưu ý 4** Với một tập khả thi không bị chặn, chi phí cực tiểu có thể là $-\infty$ *(âm vô cực).* Giả sử chi phí là $-x_1 - x_2 + x_3$. Khi đó vectơ $(100, 100, 98)$ có giá $C = -102$. Vectơ $(1000, 1000, 998)$ có giá $C = -1002$. Chúng ta đang được trả tiền để đưa vào $x_1$ và $x_2$, thay vì phải trả chi phí. Trong các ứng dụng thực tế điều này sẽ không xảy ra. Nhưng về mặt lý thuyết, $A, b,$ và $c$ có thể tạo ra những hình tam giác và chi phí không mong đợi.

#### **Bài toán Nguyên thủy và Đối ngẫu (The Primal and Dual Problems)**

Bài toán đầu tiên này sẽ khớp với $A, b, c$ trong ví dụ đó. Các ẩn số $x_1, x_2, x_3$ đại diện cho số giờ làm việc của một Tiến sĩ, một sinh viên và một cỗ máy. Chi phí mỗi giờ là \$5, \$3, và \$8. *(Tôi xin lỗi vì mức lương thấp như vậy).* Số giờ không thể âm: $x_1 \geq 0, x_2 \geq 0, x_3 \geq 0$. Tiến sĩ và sinh viên giải quyết được một bài tập về nhà mỗi giờ. *Cỗ máy giải được hai bài toán trong một giờ.* Về nguyên tắc, họ có thể chia nhau số bài tập về nhà, trong đó có bốn bài cần giải: $x_1 + x_2 + 2x_3 = 4$.

*Bài toán là hoàn thành bốn bài tập với chi phí cực tiểu $c^T x$.*

Nếu cả ba cùng làm việc, công việc mất một giờ: $x_1 = x_2 = x_3 = 1$. Chi phí là $5 + 3 + 8 = 16$. Nhưng chắc chắn Tiến sĩ nên nhường việc cho sinh viên (người cũng nhanh như vậy và chi phí thấp hơn - bài toán này đang trở nên thực tế). Khi sinh viên làm việc hai giờ và cỗ máy làm việc một giờ, chi phí là $6 + 8$ và tất cả bốn bài tập đều được giải. Chúng ta đang ở trên cạnh $QR$ của tam giác vì Tiến sĩ không làm việc: $x_1 = 0$. Nhưng điểm tốt nhất là toàn bộ công việc do sinh viên làm (tại $Q$) hoặc toàn bộ công việc do cỗ máy làm (tại $R$). Trong ví dụ này, sinh viên giải bốn bài tập trong bốn giờ với giá \$12 - chi phí cực tiểu.

Với chỉ một phương trình trong $Ax = b$, góc $(0, 4, 0)$ chỉ có một thành phần khác không. *Khi $Ax = b$ có $m$ phương trình, các góc có $m$ phần tử khác không.* Chúng ta giải $Ax = b$ cho $m$ biến đó, với $n - m$ biến tự do được đặt bằng không. Nhưng không giống như Chương 3, *chúng ta không biết phải chọn $m$ biến nào.*

Số lượng góc có thể có là số cách chọn $m$ thành phần trong số $n$ thành phần. Con số "$n$ chọn $m$" này liên quan nhiều đến cờ bạc và xác suất. Với $n = 20$ ẩn và $m = 8$ phương trình (vẫn là những con số nhỏ), "tập khả thi" có thể có $\frac{20!}{8!12!}$ góc. Con số đó là $(20)(19)\dots(13) = 5,079,110,400$.

Việc kiểm tra ba góc để tìm chi phí cực tiểu là ổn. Việc kiểm tra năm tỷ góc không phải là cách làm tốt. Phương pháp đơn hình được mô tả dưới đây nhanh hơn nhiều.

*Bài toán đối ngẫu (The Dual Problem)* Trong quy hoạch tuyến tính, các bài toán đi theo cặp. Có một bài toán cực tiểu và một bài toán cực đại - bài gốc và "đối ngẫu" của nó. Bài toán ban đầu được xác định bởi một ma trận $A$ và hai vectơ $b$ và $c$. Bài toán đối ngẫu chuyển vị $A$ và hoán đổi $b$ và $c$: *Cực đại hóa $b \cdot y$.* Đây là đối ngẫu cho ví dụ của chúng ta:

**Một kẻ gian lận đề nghị giải các bài tập về nhà bằng cách bán câu trả lời.** Giá là $y$ đô la mỗi bài, hay tổng cộng là $4y$. (Lưu ý cách $b = 4$ đã đi vào chi phí). Kẻ gian lận phải rẻ bằng hoặc hơn Tiến sĩ, sinh viên hoặc cỗ máy: $y \leq 5$ và $y \leq 3$ và $2y \leq 8$. (Lưu ý cách $c = (5, 3, 8)$ đã đi vào các ràng buộc bất đẳng thức). Kẻ gian lận cực đại hóa thu nhập $4y$.

*Bài toán đối ngẫu: Cực đại hóa $b \cdot y$ với điều kiện $A^T y \leq c$*

Mức cực đại xảy ra khi $y = 3$. Thu nhập là $4y = 12$. Cực đại trong bài toán đối ngẫu (\$12) bằng cực tiểu trong bài toán gốc (\$12). *Cực đại = cực tiểu* là tính đối ngẫu.

*Nếu một trong hai bài toán có một vectơ tốt nhất ($x^*$ hoặc $y^*$) thì bài toán kia cũng vậy. Chi phí cực tiểu $c \cdot x^*$ bằng thu nhập cực đại $b \cdot y^*$*

Cuốn sách này bắt đầu với bức tranh hàng và bức tranh cột. "Định lý đối ngẫu" đầu tiên là về hạng: Số hàng độc lập bằng số cột độc lập. Định lý đó, giống như định lý này, dễ dàng đối với các ma trận nhỏ. Chi phí cực tiểu = thu nhập cực đại được chứng minh trong giáo trình *Đại số Tuyến tính và Ứng dụng* của chúng tôi. Một dòng sẽ thiết lập nửa dễ dàng của định lý: *Thu nhập của kẻ gian lận $b^T y$ không thể vượt quá chi phí trung thực:*
$$\text{Nếu } Ax = b, x \geq 0, A^T y \leq c \text{ thì } b^T y = (Ax)^T y = x^T (A^T y) \leq x^T c. \quad (1)$$

Định lý đối ngẫu đầy đủ nói rằng khi $b^T y$ đạt cực đại và $x^T c$ đạt cực tiểu, chúng bằng nhau: $b \cdot y^* = c \cdot x^*$. Nhìn vào bước cuối cùng trong (1), với dấu $\leq$:
Tích vô hướng của $x \geq 0$ và $s = c - A^T y \geq 0$ cho $x^T s \geq 0$. Điều này có nghĩa là $x^T A^T y \leq x^T c$.

*Đẳng thức cần $x^T s = 0$. Vì vậy nghiệm tối ưu có $x_j^* = 0$ hoặc $s_j^* = 0$ đối với mỗi $j$.*

### **Phương pháp Đơn hình (The Simplex Method)**

Phép khử là con ngựa thồ cho các phương trình tuyến tính. Phương pháp đơn hình là con ngựa thồ cho các bất đẳng thức tuyến tính. Chúng ta không thể dành cho phương pháp đơn hình nhiều không gian như phép khử, nhưng ý tưởng có thể rõ ràng. *Phương pháp đơn hình đi từ một góc đến một góc lân cận có chi phí thấp hơn.* Cuối cùng (và khá nhanh trong thực tế) nó đạt tới góc có chi phí cực tiểu.

Một *góc (corner)* là một vectơ $x \geq 0$ thỏa mãn $m$ phương trình $Ax = b$ với tối đa $m$ thành phần dương. *Còn lại $n - m$ thành phần bằng không.* (Đó là các biến tự do. Phép thế ngược cho $m$ biến cơ sở. Tất cả các biến phải không âm nếu không $x$ là một góc giả). Đối với một *góc lân cận (neighboring corner)*, một thành phần bằng không của $x$ trở thành dương và một thành phần dương trở thành không.

*Phương pháp đơn hình phải quyết định thành phần nào "đi vào" (trở thành số dương), và thành phần nào "rời đi" (trở thành số không). Sự trao đổi đó được chọn sao cho làm giảm tổng chi phí. Đây là một bước của phương pháp đơn hình, di chuyển về phía $x^*$.*

Dưới đây là kế hoạch tổng thể. Nhìn vào từng thành phần bằng không tại góc hiện tại. Nếu nó thay đổi từ 0 thành 1, các thành phần khác không còn lại phải điều chỉnh để giữ cho $Ax = b$. Tìm $x$ mới bằng phép thế ngược và tính toán sự thay đổi trong tổng chi phí $c \cdot x$. Sự thay đổi này là "chi phí rút gọn (reduced cost)" $r$ của thành phần mới. *Biến đi vào (entering variable)* là biến mang lại *âm nhiều nhất* $r$. Đây là mức giảm chi phí lớn nhất cho một đơn vị của biến mới.

**Ví dụ 1** Giả sử góc hiện tại là $P = (4, 0, 0)$, với Tiến sĩ làm tất cả công việc (chi phí là \$20). Nếu sinh viên làm việc một giờ, chi phí của $x = (3, 1, 0)$ giảm xuống còn \$18. Chi phí rút gọn là $r = -2$. Nếu cỗ máy làm việc một giờ, thì $x = (2, 0, 1)$ cũng có giá \$18. Chi phí rút gọn cũng là $r = -2$. Trong trường hợp này, phương pháp đơn hình có thể chọn sinh viên hoặc cỗ máy làm biến đi vào.

Ngay cả trong ví dụ nhỏ này, bước đầu tiên có thể không đi ngay đến $x^*$ tốt nhất. Phương pháp chọn biến đi vào trước khi nó biết cần phải đưa vào bao nhiêu của biến đó. Chúng ta đã tính $r$ khi biến đi vào thay đổi từ 0 thành 1, nhưng một đơn vị có thể là quá nhiều hoặc quá ít. Giờ đây phương pháp chọn biến rời đi (Tiến sĩ). Nó di chuyển đến góc $Q$ hoặc $R$ trong hình.

Càng đưa nhiều biến đi vào, chi phí càng thấp. Điều này phải dừng lại khi một trong các thành phần dương (đang điều chỉnh để giữ $Ax = b$) chạm mức không. *Biến rời đi là biến dương đầu tiên chạm mức không.* Khi điều đó xảy ra, một góc lân cận đã được tìm thấy. Sau đó bắt đầu lại (từ góc mới) để tìm các biến tiếp theo đi vào và rời đi.

**Khi tất cả các chi phí rút gọn đều dương, góc hiện tại là tối ưu $x^*$.** Không thành phần bằng không nào có thể trở thành dương mà không làm tăng $c \cdot x$. Không biến mới nào nên đi vào. Bài toán đã được giải (và chúng ta có thể chỉ ra rằng $y^*$ cũng được tìm thấy).

**Lưu ý** Thường thì $x^*$ đạt được trong $cm$ bước, với $c$ không lớn. Nhưng đã có những ví dụ được phát minh ra sử dụng một số lượng bước đơn hình theo hàm mũ. Cuối cùng một cách tiếp cận khác đã được phát triển, được đảm bảo đạt tới $x^*$ trong ít bước hơn (nhưng khó hơn). Các phương pháp mới di chuyển qua phần *bên trong (interior)* của tập khả thi.

**Ví dụ 2** Cực tiểu hóa chi phí $c \cdot x = 3x_1 + x_2 + 9x_3 + x_4$. Các ràng buộc là $x \geq 0$ và hai phương trình $Ax = b$:
| $x_1 + 2x_3 + x_4 = 4$ | $m = 2$ | phương trình |
|------------------------|---------|-----------|
| $x_2 + x_3 - x_4 = 2$  | $n = 4$ | ẩn. |

Một góc xuất phát là $x = (4, 2, 0, 0)$ có chi phí $c \cdot x = 14$. Nó có $m = 2$ phần tử khác không và $n - m = 2$ phần tử bằng không. Các số không là $x_3$ và $x_4$. Câu hỏi là liệu $x_3$ hay $x_4$ nên đi vào (trở thành khác không). Thử một đơn vị của mỗi biến:
| $\text{Nếu } x_3 = 1 \text{ và } x_4 = 0,$ | thì $x = (2, 1, 1, 0)$ tốn 16. |
|--------------------------------------------|-----------------------------------|
| $\text{Nếu } x_4 = 1 \text{ và } x_3 = 0,$ | thì $x = (3, 3, 0, 1)$ tốn 13. |

So sánh các chi phí đó với 14. Chi phí rút gọn của $x_3$ là $r = 2$, dương và vô dụng. Chi phí rút gọn của $x_4$ là $r = -1$, âm và hữu ích. *Biến đi vào là $x_4$.*

Bao nhiêu lượng $x_4$ có thể đi vào? Một đơn vị của $x_4$ làm $x_1$ giảm từ 4 xuống 3. Bốn đơn vị sẽ làm $x_1$ giảm từ 4 xuống không (trong khi $x_2$ tăng lên đến 6). *Biến rời đi là $x_1$.* Góc mới là $x = (0, 6, 0, 4)$, chỉ tốn $c \cdot x = 10$. Đây là $x^*$ tối ưu, nhưng để biết điều đó, chúng ta phải thử một bước đơn hình khác từ $(0, 6, 0, 4)$. Giả sử $x_1$ hoặc $x_3$ cố gắng đi vào:
| **Bắt đầu từ góc (0, 6, 0, 4)** | $x_1 = 1$ và $x_3 = 0$ | $x = (1, 5, 0, 3)$ tốn 11. |
|-------------------------------------------|-------------------------------------|--------------------------------|
|                                           | $x_2 = 1$      | $x = (0, 7, 1, 2)$ tốn 14.     |

Các chi phí đó cao hơn 10. Cả hai $r$ đều dương - việc di chuyển là không có lợi. Góc hiện tại $(0, 6, 0, 4)$ là nghiệm $\mathbf{x}^*$.

Các tính toán này có thể được hợp lý hóa. Mỗi bước đơn hình giải ba hệ tuyến tính với cùng ma trận $B$. (Đây là ma trận $m \times m$ giữ $m$ cột cơ sở của $A$). Khi một cột đi vào và một cột cũ rời đi, có một cách nhanh chóng để cập nhật $B^{-1}$. Đó là cách hầu hết các mã lập trình tổ chức phương pháp đơn hình.

Giáo trình *Khoa học và Kỹ thuật Tính toán* của chúng tôi bao gồm một đoạn mã ngắn với các bình luận. (Mã cũng có trên **math.mit.edu/cse**). Điểm $\mathbf{y}^*$ tốt nhất giải $m$ phương trình $A^T \mathbf{y}^* = \mathbf{c}$ trong $m$ thành phần khác không trong $\mathbf{x}^*$. Khi đó chúng ta có tính tối ưu $\mathbf{x}^T \mathbf{s} = 0$ và đây là tính đối ngẫu: *Hoặc là $\mathbf{x}_j^* = 0$ hoặc phần "thừa" (slack) trong $\mathbf{s}^* = \mathbf{c} - A^T \mathbf{y}^*$ có $s_j^* = 0$.*

Khi $\mathbf{x}^* = (0, 4, 0)$ là góc tối ưu $\mathbf{Q}$, giá của kẻ gian lận được thiết lập bởi $y^* = 3$.

## Các Phương pháp Điểm trong (Interior Point Methods)

Phương pháp đơn hình di chuyển dọc theo các cạnh của tập khả thi, cuối cùng đến được góc tối ưu $\mathbf{x}^*$. **Các phương pháp điểm trong di chuyển bên trong tập khả thi** (nơi $\mathbf{x} > 0$). Các phương pháp này hy vọng đi trực tiếp hơn đến $\mathbf{x}^*$. Chúng hoạt động tốt.

Một cách để ở bên trong là đặt một rào cản ở biên. Thêm chi phí bổ sung dưới dạng một *logarit bùng nổ* khi bất kỳ biến $x_j$ nào chạm mức không. Vectơ tốt nhất có $\mathbf{x} > 0$. Số $\theta$ là một tham số nhỏ mà chúng ta di chuyển về số không.
$$\text{Bài toán rào cản} \quad \text{Cực tiểu hóa} \quad \mathbf{c}^T \mathbf{x} - \theta (\log x_1 + \dots + \log x_n) \quad \text{với điều kiện} \quad A\mathbf{x} = \mathbf{b} \quad (2)$$

Chi phí này phi tuyến tính (nhưng bản thân quy hoạch tuyến tính đã là phi tuyến từ các bất đẳng thức). Các ràng buộc $x_j \geq 0$ không cần thiết vì $\log x_j$ trở thành vô hạn tại $x_j = 0$.

Rào cản đưa ra một *bài toán xấp xỉ* đối với mỗi $\theta$. $m$ ràng buộc $A\mathbf{x} = \mathbf{b}$ có các nhân tử Lagrange $y_1, \dots, y_m$. Đây là cách tốt để giải quyết các ràng buộc.
$$\mathbf{y} \text{ từ Lagrange} \quad L(\mathbf{x}, \mathbf{y}, \theta) = \mathbf{c}^T \mathbf{x} - \theta (\sum \log x_i) - \mathbf{y}^T (A\mathbf{x} - \mathbf{b}) \quad (3)$$

$\partial L / \partial \mathbf{y} = 0$ đưa trở lại $A\mathbf{x} = \mathbf{b}$. Các đạo hàm $\partial L / \partial x_j$ rất thú vị!
$$\text{Tính tối ưu trong bài toán rào cản} \quad \frac{\partial L}{\partial x_j} = c_j - \frac{\theta}{x_j} - (A^T \mathbf{y})_j = 0 \quad \text{tức là} \quad \mathbf{x}_j \mathbf{s}_j = \theta. \quad (4)$$

Bài toán thực sự có $x_j \mathbf{s}_j = 0$. Bài toán rào cản có $x_j \mathbf{s}_j = \theta$. Các nghiệm $\mathbf{x}^*(\theta)$ nằm trên *đường dẫn trung tâm (central path)* tới $\mathbf{x}^*(0)$. $n$ phương trình tối ưu $x_j \mathbf{s}_j = \theta$ đó là phi tuyến tính, và chúng ta giải chúng lặp đi lặp lại bằng phương pháp Newton.

Các $\mathbf{x}, \mathbf{y}, \mathbf{s}$ hiện tại sẽ thỏa mãn $A\mathbf{x} = \mathbf{b}, \mathbf{x} \geq \mathbf{0}$ và $A^T \mathbf{y} + \mathbf{s} = \mathbf{c}$, nhưng không thỏa mãn $x_j \mathbf{s}_j = \theta$. Phương pháp Newton thực hiện một bước $\Delta \mathbf{x}, \Delta \mathbf{y}, \Delta \mathbf{s}$. Bằng cách bỏ qua số hạng bậc hai $\Delta \mathbf{x} \Delta \mathbf{s}$
trong $(x + \Delta x)(s + \Delta s) = 0$, các hiệu chỉnh trong $x, y, s$ đến từ các phương trình tuyến tính:
|             | $A \Delta x = 0$                                     |     |
|-------------|------------------------------------------------------|-----|
| Bước Newton | $A^T \Delta y + \Delta s = 0$                        | (5) |
|             | $s_j \Delta x_j + x_j \Delta s_j = \theta - x_j s_j$ |     |

Vòng lặp Newton có sự hội tụ bậc hai đối với mỗi $\theta$, và sau đó $\theta$ tiến tới 0. Khoảng cách đối ngẫu $x^T s$ thường xuống dưới $10^{-8}$ sau 20 đến 60 bước. Lời giải thích trong giáo trình *Khoa học và Kỹ thuật Tính toán* của tôi đi chi tiết vào một bước Newton, đối với ví dụ có bốn bài tập về nhà. Tôi không có ý định rằng sinh viên cuối cùng phải làm tất cả công việc, nhưng $x^*$ lại hóa ra như vậy.

Phương pháp điểm trong này được sử dụng gần như "nguyên trạng" trong phần mềm thương mại, cho một lớp lớn các bài toán tối ưu hóa tuyến tính và phi tuyến tính.

### **Tập bài tập 10.4 (Problem Set 10.4)**

**1** Vẽ khu vực trong mặt phẳng $xy$ nơi $x + 2y = 6$ và $x \geq 0$ và $y \geq 0$. Điểm nào trong "tập khả thi" này cực tiểu hóa chi phí $c = x + 3y$? Điểm nào cho chi phí cực đại? Những điểm đó nằm ở các góc.
**2** Vẽ khu vực trong mặt phẳng $xy$ nơi $x + 2y \leq 6$, $2x + y \leq 6$, $x \geq 0$, $y \geq 0$. Nó có bốn góc. Góc nào cực tiểu hóa chi phí $c = 2x - y$?
**3** Các góc của tập $x_1 + 2x_2 - x_3 = 4$ với $x_1, x_2, x_3$ đều $\geq 0$ là gì? Chứng tỏ rằng chi phí $x_1 + 2x_3$ có thể rất âm trong tập khả thi này. Đây là một ví dụ về chi phí không bị chặn: không có mức cực tiểu.
**4** Bắt đầu tại $x = (0, 0, 2)$ nơi cỗ máy giải quyết cả bốn bài toán với giá \$16. Di chuyển đến $x = (0, 1, 1.5)$ để tìm chi phí rút gọn $r$ (khoản tiết kiệm mỗi giờ) cho công việc của sinh viên. Tìm $r$ cho Tiến sĩ bằng cách di chuyển đến $x = (1, 0, 1.5)$ với 1 giờ làm việc của Tiến sĩ.
**5** Bắt đầu Ví dụ 1 từ góc của Tiến sĩ $(4, 0, 0)$ với $c$ đổi thành $\begin{bmatrix} 5 & 3 & 7 \end{bmatrix}$. Chứng tỏ rằng $r$ tốt hơn cho cỗ máy ngay cả khi tổng chi phí thấp hơn cho sinh viên. Phương pháp đơn hình thực hiện hai bước, đầu tiên chuyển đến cỗ máy và sau đó chuyển đến sinh viên cho $x^*$.
**6** Chọn một vectơ chi phí $c$ khác để Tiến sĩ nhận được công việc. Viết lại bài toán đối ngẫu (thu nhập cực đại cho kẻ gian lận).
**7** Bài tập về nhà gồm sáu bài mà Tiến sĩ làm nhanh nhất đưa ra ràng buộc thứ hai $2x_1 + x_2 + x_3 = 6$. Sau đó $x = (2, 2, 0)$ cho thấy hai giờ làm việc của Tiến sĩ và sinh viên đối với mỗi bài tập về nhà. Điểm $x$ này có cực tiểu hóa chi phí $c^T x$ với $c = (5, 3, 8)$ không?
**8** Hai bài toán này cũng đối ngẫu với nhau. Hãy chứng minh tính đối ngẫu yếu, rằng luôn luôn có $y^T b \leq c^T x$:
*Bài toán nguyên thủy* Cực tiểu hóa $c^T x$ với $Ax \geq b$ và $x \geq 0$.
*Bài toán đối ngẫu* Cực đại hóa $y^T b$ với $A^T y \leq c$ và $y \geq 0$.

# **10.5 Chuỗi Fourier: Đại số Tuyến tính cho Hàm số (Fourier Series: Linear Algebra for Functions)**

Phần này đi từ số chiều hữu hạn đến số chiều *vô hạn (infinite dimensions)*. Tôi muốn giải thích đại số tuyến tính trong không gian vô hạn chiều, và cho thấy rằng nó vẫn hoạt động. Bước đầu tiên: nhìn lại. Cuốn sách này bắt đầu với các vectơ, tích vô hướng và các tổ hợp tuyến tính. Chúng ta bắt đầu bằng cách chuyển đổi những ý tưởng cơ bản đó sang trường hợp vô hạn - phần còn lại sẽ theo sau.

Việc một vectơ có vô số thành phần có ý nghĩa gì? Có hai câu trả lời khác nhau, cả hai đều đúng:
- **1.** Vectơ dài vô hạn: $v = (v_1, v_2, v_3, \dots)$. Nó có thể là $(1, \frac{1}{2}, \frac{1}{4}, \dots)$.
- **2.** Vectơ là một hàm $f(x)$. Nó có thể là $v = \sin x$.

Chúng ta sẽ đi theo cả hai hướng. Sau đó ý tưởng về chuỗi Fourier sẽ kết nối chúng lại với nhau.

Sau các vectơ là *tích vô hướng (dot products)*. Tích vô hướng tự nhiên của hai vectơ vô hạn $(v_1, v_2, \dots)$ và $(w_1, w_2, \dots)$ là một chuỗi vô hạn:
| Tích vô hướng | $v \cdot w = v_1 w_1 + v_2 w_2 + \cdots$ | (1) |
|-------------|------------------------------------------|-----|

Điều này mang đến một câu hỏi mới, điều chưa từng xảy ra với chúng ta đối với các vectơ trong $\mathbb{R}^n$. Tổng vô hạn này có cộng lại thành một số hữu hạn không? Chuỗi này có hội tụ không? Đây là sự khác biệt đầu tiên và lớn nhất giữa hữu hạn và vô hạn.

Khi $v = w = (1, 1, 1, \dots)$, tổng chắc chắn không hội tụ. Trong trường hợp đó $v \cdot w = 1 + 1 + 1 + \dots$ là vô hạn. Vì $v$ bằng $w$, chúng ta thực sự đang tính $v \cdot v = \|v\|^2$, bình phương độ dài. Vectơ $(1, 1, 1, \dots)$ có chiều dài vô hạn. *Chúng ta không muốn vectơ đó.* Vì chúng ta đang đặt ra các quy tắc, nên chúng ta không cần phải đưa nó vào. Các vectơ duy nhất được phép là những vectơ có chiều dài hữu hạn:

**ĐỊNH NGHĨA** Vectơ $v = (v_1, v_2, \dots)$ và hàm số $f(x)$ nằm trong *"không gian Hilbert"* vô hạn chiều của chúng ta khi và chỉ khi độ dài $\|v\|$ và $\|f\|$ của chúng là hữu hạn:
| $\|v\|^2 = v \cdot v = v_1^2 + v_2^2 + v_3^2 + \dots$ | phải cộng lại thành một số hữu hạn. |
|----------------------------------------------------------------------------------|------------------------------|
| $\|f\|^2 = (f, f) = \int_0^{2\pi} (f(x))^2 dx$                                   | phải là một tích phân hữu hạn.   |

**Ví dụ 1** Vectơ $v = (1, \frac{1}{2}, \frac{1}{4}, \dots)$ được đưa vào không gian Hilbert, vì độ dài của nó là $2 / \sqrt{3}$. Chúng ta có một chuỗi cấp số nhân có tổng là $4/3$. Chiều dài của $v$ là căn bậc hai:
Bình phương chiều dài
$$v \cdot v = 1 + \frac{1}{4} + \frac{1}{16} + \dots = \frac{1}{1 - \frac{1}{4}} = \frac{4}{3}$$

*Câu hỏi* Nếu $v$ và $w$ có chiều dài hữu hạn, tích vô hướng của chúng có thể lớn đến mức nào?
*Trả lời* Tổng $v \cdot w = v_1 w_1 + v_2 w_2 + \dots$ cũng cộng lại thành một số hữu hạn. Chúng ta có thể lấy tích vô hướng một cách an toàn. Bất đẳng thức Schwarz vẫn đúng:
| Bất đẳng thức Schwarz | $|v \cdot w| \leq \|v\| \|w\|.$ | (2) |
|--------------------|---------------------------------------------------------------------|-----|

Tỷ số của $v \cdot w$ so với $\|v\| \|w\|$ vẫn là $\cos \theta$ (góc giữa $v$ và $w$). Ngay cả trong không gian vô hạn chiều, $|\cos \theta|$ không lớn hơn 1.

Bây giờ chuyển qua các hàm. Đó là các "vectơ". Không gian các hàm $f(x), g(x), h(x), \dots$ được định nghĩa cho $0 \leq x \leq 2\pi$ theo một cách nào đó phải lớn hơn $\mathbb{R}^n$. *Tích vô hướng của $f(x)$ và $g(x)$ là gì? Độ dài của $f(x)$ là gì?*

Điểm then chốt trong trường hợp liên tục: *Các tổng được thay thế bằng các tích phân.* Thay vì tổng của $v_j$ nhân với $w_j$, tích vô hướng là tích phân của $f(x)$ nhân với $g(x)$. Đổi "dấu chấm" thành dấu ngoặc đơn có dấu phẩy, và đổi các từ "tích vô hướng (dot product)" thành *tích vô hướng (inner product):*

**ĐỊNH NGHĨA** *Tích vô hướng* của $f(x)$ và $g(x)$, và *bình phương độ dài* của $f(x)$, là
| $(f, g) = \int_0^{2\pi} f(x)g(x) dx$ | và | $\|f\|^2 = \int_0^{2\pi} (f(x))^2 dx$ | (3) |
|--------------------------------------|-----|---------------------------------------|-----|

Khoảng $[0, 2\pi]$ nơi các hàm được định nghĩa có thể thay đổi sang một khoảng khác như $[0, 1]$ hoặc $(-\infty, \infty)$. Chúng tôi chọn $2\pi$ vì các ví dụ đầu tiên của chúng ta là $\sin x$ và $\cos x$.

**Ví dụ 2** Độ dài của $f(x) = \sin x$ đến từ tích vô hướng của nó với chính nó:
$$(f, f) = \int_0^{2\pi} (\sin x)^2 dx = \pi$$
. Độ dài của $\sin x$ là $\sqrt{\pi}$.

Đó là một tích phân tiêu chuẩn trong giải tích - không thuộc phần đại số tuyến tính. Bằng cách viết $\sin^2 x$ dưới dạng $\frac{1}{2} - \frac{1}{2}\cos 2x$, chúng ta thấy nó đi trên và dưới giá trị trung bình của nó $\frac{1}{2}$. Nhân giá trị trung bình đó với độ dài khoảng $2\pi$ để được câu trả lời $\pi$.

Quan trọng hơn: $\sin x$ *và* $\cos x$ *trực giao (orthogonal) trong không gian hàm:* $(f, g) = 0$
| Tích vô hướng bằng 0 | $\int_0^{2\pi} \sin x \cos x \, dx = \int_0^{2\pi} \frac{1}{2} \sin 2x \, dx = \left[-\frac{1}{4} \cos 2x\right]_0^{2\pi} = 0. \quad (4)$ |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------|

Số không này không phải là sự tình cờ. Nó rất quan trọng đối với khoa học. Tính trực giao vượt xa hai hàm $\sin x$ và $\cos x$, đến một danh sách vô tận các sin và cos. Danh sách này chứa $\cos 0x$ (chính là $1$), $\sin x$, $\cos x$, $\sin 2x$, $\cos 2x$, $\sin 3x$, $\cos 3x, \dots$
*Mọi hàm trong danh sách đó đều trực giao với mọi hàm khác trong danh sách.*

#### **Chuỗi Fourier (Fourier Series)**

Chuỗi Fourier của một hàm $f(x)$ là sự khai triển của nó thành các hàm sin và cos:
$$f(x) = a_0 + a_1 \cos x + b_1 \sin x + a_2 \cos 2x + b_2 \sin 2x + \cdots. \quad (5)$$

Chúng ta có một cơ sở trực giao! Các vectơ trong "không gian hàm" là tổ hợp của các hàm sin và cos. Trên khoảng từ $x = 2\pi$ đến $x = 4\pi$, tất cả các hàm của chúng ta lặp lại những gì chúng đã làm từ $0$ đến $2\pi$. Chúng *"tuần hoàn (periodic)."* Khoảng cách giữa các lần lặp lại là chu kỳ $2\pi$.

Hãy nhớ rằng: Danh sách là vô hạn. Chuỗi Fourier là một chuỗi vô hạn. Chúng ta đã tránh vectơ $v = (1, 1, 1, \dots)$ vì chiều dài của nó là vô hạn, bây giờ chúng ta tránh một hàm như $\frac{1}{2} + \cos x + \cos 2x + \cos 3x + \dots$. *(Lưu ý:* Đây là $\pi$ lần **hàm delta** $\delta(x)$ nổi tiếng. Nó là một "đỉnh (spike)" vô cực phía trên một điểm duy nhất. Tại $x = 0$ chiều cao của nó $\frac{1}{2} + 1 + 1 + \dots$ là vô hạn. Tại tất cả các điểm nằm trong $0 < x < 2\pi$ chuỗi này cộng lại theo một cách trung bình nào đó bằng không). Tích phân của $\delta(x)$ là 1. Nhưng $\int \delta^2(x) = \infty$, do đó các hàm delta không được cho phép vào không gian Hilbert.

Tính độ dài của một tổng điển hình $f(x)$:
$$\begin{aligned} (f, f) &= \int_0^{2\pi} (a_0 + a_1 \cos x + b_1 \sin x + a_2 \cos 2x + \cdots)^2 dx \\ &= \int_0^{2\pi} (a_0^2 + a_1^2 \cos^2 x + b_1^2 \sin^2 x + a_2^2 \cos^2 2x + \cdots) dx \\ \|f\|^2 &= 2\pi a_0^2 + \pi(a_1^2 + b_1^2 + a_2^2 + \cdots). \end{aligned} \quad (6)$$

Bước từ dòng 1 sang dòng 2 đã sử dụng tính trực giao. Tất cả các tích như $\cos x \cos 2x$ lấy tích phân cho ra không. Dòng 2 chứa những gì còn lại - tích phân của mỗi sin và cos bình phương. Dòng 3 đánh giá các tích phân đó. (Tích phân của $1^2$ là $2\pi$, trong khi tất cả các tích phân khác cho $\pi$). Nếu chúng ta chia chúng cho độ dài của chúng, các hàm của chúng ta sẽ trở nên *trực chuẩn (orthonormal):*
$$\frac{1}{\sqrt{2\pi}}, \frac{\cos x}{\sqrt{\pi}}, \frac{\sin x}{\sqrt{\pi}}, \frac{\cos 2x}{\sqrt{\pi}}, \dots$$
là một cơ sở trực chuẩn cho không gian hàm của chúng ta.

Đây là các vectơ đơn vị. Chúng ta có thể kết hợp chúng với các hệ số $A_0, A_1, B_1, A_2, \dots$ để tạo ra một hàm $F(x)$. Sau đó $2\pi$ và $\pi$ sẽ biến mất khỏi công thức tính độ dài.
| Chiều dài hàm = chiều dài vectơ | $\|F\|^2 = (F, F) = A_0^2 + A_1^2 + B_1^2 + A_2^2 + \dots \quad (7)$ |
|---------------------------------|------------------------------------------------------------------|

Đây là điểm quan trọng, đối với $f(x)$ cũng như $F(x)$. *Hàm có độ dài hữu hạn chính xác khi vectơ hệ số có độ dài hữu hạn.* Chuỗi Fourier cho chúng ta một sự kết hợp hoàn hảo giữa các không gian Hilbert đối với các hàm số và đối với các vectơ. Hàm nằm trong $L^2$, các hệ số Fourier của nó nằm trong $\ell^2$.

Không gian hàm chứa $f(x)$ một cách chính xác khi không gian Hilbert chứa vectơ $v = (a_0, a_1, b_1, \dots)$ gồm các hệ số Fourier của $f(x)$. Cả hai đều phải có độ dài hữu hạn.

**Ví dụ 3** Giả sử $f(x)$ là một "sóng vuông (square wave)", bằng 1 đối với $0 \leq x < \pi$. Sau đó $f(x)$ giảm xuống -1 đối với $\pi \leq x < 2\pi$. $+1$ và $-1$ lặp lại mãi mãi. $f(x)$ này là một hàm lẻ giống như các hàm sin, và tất cả các hệ số cos của nó đều bằng không. Chúng ta sẽ tìm chuỗi Fourier của nó, chỉ chứa các sin:
| **Sóng vuông** | $f(x) = \frac{4}{\pi} \left[ \frac{\sin x}{1} + \frac{\sin 3x}{3} + \frac{\sin 5x}{5} + \dots \right].$ | (8) |
|--------------------|---------------------------------------------------------------------------------------------------------|-----|

Độ dài của hàm này là $2\pi$ vì tại mọi điểm $(f(x))^2$ là $(-1)^2$ hoặc $(+1)^2$:
$$\|f\|^2 = \int_0^{2\pi} (f(x))^2 dx = \int_0^{2\pi} 1 dx = 2\pi.$$

Tại $x = 0$ các hàm sin bằng không và chuỗi Fourier bằng không. Đây là điểm giữa của bước nhảy từ -1 lên +1. Chuỗi Fourier cũng thú vị khi $x = \pi/2$. Tại điểm này, sóng vuông bằng 1, và các hàm sin trong (8) luân phiên giữa +1 và -1:
$$\text{Công thức cho } \pi \quad 1 = \frac{4}{\pi} \left( 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots \right). \quad (9)$$

Nhân với $\pi$ để tìm một công thức kỳ diệu $4(1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots)$ cho con số nổi tiếng đó.

### Các Hệ số Fourier (The Fourier Coefficients)

Làm thế nào để chúng ta tìm thấy các $a$ và $b$ nhân với các hàm cos và sin? Đối với một hàm $f(x)$ cho trước, chúng ta đang yêu cầu các hệ số Fourier của nó là $a_k$ và $b_k$:
$$\text{Chuỗi Fourier} \quad f(x) = a_0 + a_1 \cos x + b_1 \sin x + a_2 \cos 2x + \cdots.$$

**Đây là cách để tìm $a_1$. Nhân cả hai vế với $\cos x$. Sau đó lấy tích phân từ 0 đến $2\pi$.** Chìa khóa là tính trực giao! Tất cả các tích phân ở vế phải đều bằng không, ngoại trừ $\cos^2 x$:
$$\text{Đối với hệ số } a_1 \quad \int_0^{2\pi} f(x) \cos x \, dx = \int_0^{2\pi} a_1 \cos^2 x \, dx = \pi a_1. \quad (10)$$

Chia cho $\pi$ và bạn có $a_1$. Để tìm bất kỳ $a_k$ nào khác, nhân chuỗi Fourier với $\cos kx$. Lấy tích phân từ 0 đến $2\pi$. Sử dụng tính trực giao, do đó chỉ có tích phân của $a_k \cos^2 kx$ là còn lại. Tích phân đó là $\pi a_k$, và chia cho $\pi$:
$$a_k = \frac{1}{\pi} \int_0^{2\pi} f(x) \cos kx \, dx \quad \text{và tương tự} \quad b_k = \frac{1}{\pi} \int_0^{2\pi} f(x) \sin kx \, dx. \quad (11)$$

Ngoại lệ là $a_0$. Lần này chúng ta nhân với $\cos 0x = 1$. Tích phân của 1 là $2\pi$:
$$\text{Hệ số tự do (Constant term)} \quad a_0 = \frac{1}{2\pi} \int_0^{2\pi} f(x) \cdot 1 \, dx = \text{giá trị trung bình của } f(x). \quad (12)$$

Tôi đã sử dụng những công thức đó để tìm các hệ số Fourier cho sóng vuông trong phương trình (8). Tích phân của $f(x) \cos kx$ là không. Tích phân của $f(x) \sin kx$ là $4/k$ cho $k$ lẻ.

### So sánh Đại số Tuyến tính trong $\mathbb{R}^n$ (Compare Linear Algebra in $\mathbb{R}^n$)

Không gian Hilbert vô hạn chiều rất giống với không gian $n$ chiều $\mathbb{R}^n$. Giả sử các vectơ khác không $v_1, \dots, v_n$ trực giao trong $\mathbb{R}^n$. Chúng ta muốn viết vectơ $b$ (thay vì hàm $f(x)$) như một tổ hợp của những $v$ đó:
$$\text{Chuỗi trực giao hữu hạn} \quad b = c_1 v_1 + c_2 v_2 + \cdots + c_n v_n. \quad (13)$$

Nhân cả hai vế với $v_1^T$. Sử dụng tính trực giao, để $v_1^T v_2 = 0$. Chỉ còn lại số hạng $c_1$:
$$\text{Hệ số } c_1 \quad v_1^T b = c_1 v_1^T v_1 + 0 + \cdots + 0. \quad \text{Do đó } c_1 = v_1^T b / v_1^T v_1. \quad (14)$$

Mẫu số $v_1^T v_1$ là bình phương độ dài, giống như $\pi$ trong phương trình (11). Tử số $v_1^T b$ là tích vô hướng giống như $\int f(x) \cos kx \, dx$. **Các hệ số rất dễ tìm khi các**
*vectơ cơ sở trực giao.* Chúng ta chỉ đang thực hiện các phép chiếu một chiều, để tìm các thành phần dọc theo mỗi vectơ cơ sở.

Các công thức thậm chí còn tốt hơn khi các vectơ là trực chuẩn. Khi đó chúng ta có các vectơ đơn vị trong ma trận $Q$. Các mẫu số $v_k^T v_k$ đều bằng 1. Bạn biết $c_k = v_k^T b$ ở một dạng khác:
**Phương trình cho các $c$** $c_1 v_1 + \dots + c_n v_n = b$ hoặc $\begin{bmatrix} v_1 & \dots & v_n \end{bmatrix} \begin{bmatrix} c_1 \\ \vdots \\ c_n \end{bmatrix} = b$.
$Qc = b$ cho ra $c = Q^T b$. Lần lượt từng hàng, đây là $c_k = q_k^T b$.

Chuỗi Fourier giống như có một ma trận với vô số cột trực giao. Những cột đó là các hàm cơ sở $1, \cos x, \sin x, \dots$. Sau khi chia cho độ dài của chúng, chúng ta có một "ma trận trực giao vô hạn". Nghịch đảo của nó là chuyển vị của nó, $Q^T$. Tính trực giao là thứ làm giảm một chuỗi các số hạng xuống còn một số hạng duy nhất, khi chúng ta tính tích phân.

### **Tập bài tập 10.5 (Problem Set 10.5)**

**1** Lấy tích phân đẳng thức lượng giác $2 \cos jx \cos kx = \cos(j + k)x + \cos(j - k)x$ để chỉ ra rằng $\cos jx$ trực giao với $\cos kx$, với điều kiện $j \neq k$. Kết quả là gì khi $j = k$?
**2** Cho thấy rằng $1, x$, và $x^2 - \frac{1}{3}$ là trực giao, khi tích phân đi từ $x = -1$ đến $x = 1$. Viết $f(x) = 2x^2$ dưới dạng một tổ hợp của các hàm trực giao đó.
**3** Tìm một vectơ $(w_1, w_2, w_3, \dots)$ trực giao với $v = (1, \frac{1}{2}, \frac{1}{4}, \dots)$. Tính độ dài $\|w\|$ của nó.
**4** Ba *đa thức Legendre (Legendre polynomials)* đầu tiên là $1, x$, và $x^2 - \frac{1}{3}$. Chọn $c$ sao cho đa thức thứ tư $x^3 - cx$ trực giao với ba đa thức đầu tiên. Tất cả các tích phân đều đi từ -1 đến 1.
**5** Đối với sóng vuông $f(x)$ trong Ví dụ 3 nhảy từ 1 xuống -1, hãy chứng tỏ rằng
$$\int_0^{2\pi} f(x) \cos x \, dx = 0 \quad \int_0^{2\pi} f(x) \sin x \, dx = 4 \quad \int_0^{2\pi} f(x) \sin 2x \, dx = 0.$$
Ba hệ số Fourier nào xuất phát từ những tích phân đó?
**6** Sóng vuông có $\|f\|^2 = 2\pi$. Vậy (6) mang lại tổng đáng chú ý nào cho $\pi$?
**7** Vẽ đồ thị sóng vuông. Sau đó vẽ đồ thị bằng tay tổng của hai số hạng sin trong chuỗi của nó, hoặc vẽ bằng máy tổng của 2, 3 và 10 số hạng. *Hiện tượng Gibbs (Gibbs phenomenon)* nổi tiếng là sự dao động vượt qua bước nhảy (điều này không mất đi khi có nhiều số hạng hơn).
**8** Tìm độ dài của các vectơ này trong không gian Hilbert:
(a) $\mathbf{v} = \left( \frac{1}{\sqrt{1}}, \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{4}}, \frac{1}{\sqrt{8}}, \dots \right)$
(b) $\mathbf{v} = \left( 1, a, a^2, \dots \right)$
(c) $f(x) = 1 + \sin x$

**9** Tính các hệ số Fourier $a_k$ và $b_k$ đối với $f(x)$ được định nghĩa từ 0 đến $2\pi$:
(a) $f(x) = 1$ cho $0 \leq x \leq \pi$, $f(x) = 0$ cho $\pi < x < 2\pi$
(b) $f(x) = x$.
**10** Khi $f(x)$ có chu kỳ $2\pi$, tại sao tích phân của nó từ $-\pi$ đến $\pi$ giống như từ $0$ đến $2\pi$? Nếu $f(x)$ là một hàm *lẻ*, $f(-x) = -f(x)$, hãy chứng tỏ rằng $\int_{-\pi}^\pi f(x) dx$ là không. Các hàm lẻ chỉ có các số hạng sin, các hàm chẵn chỉ có các hàm cos.
**11** Sử dụng các đồng nhất thức lượng giác, tìm hai số hạng trong chuỗi Fourier cho $f(x)$:
(a) $f(x) = \cos^2 x$      (b) $f(x) = \cos\left(x + \frac{\pi}{3}\right)$      (c) $f(x) = \sin^3 x$.
**12** Các hàm $1, \cos x, \sin x, \cos 2x, \sin 2x, \dots$ là một cơ sở cho không gian Hilbert. Viết các đạo hàm của năm hàm đầu tiên này dưới dạng các tổ hợp của cùng năm hàm đó. "Ma trận đạo hàm" $5 \times 5$ cho các hàm này là gì?
**13** Tìm các hệ số Fourier $a_k$ và $b_k$ của xung vuông $F(x)$ có tâm tại $x = 0$: $F(x) = 1/h$ cho $|x| \leq h/2$ và $F(x) = 0$ cho $h/2 < |x| \leq \pi$. Khi $h \rightarrow 0$, $F(x)$ này tiếp cận một hàm delta. Tìm các giới hạn của $a_k$ và $b_k$.

Phần 4.1 của cuốn *Khoa học và Kỹ thuật Tính toán* giải thích chuỗi sin, chuỗi cos, chuỗi hoàn chỉnh và chuỗi phức $\sum c_k e^{ikx}$ trên **math.mit.edu/cse**. Phần 9.3 của cuốn sách này giải thích *Biến đổi Fourier Rời rạc (Discrete Fourier Transform).* Đây là "chuỗi Fourier cho các vectơ" và nó được tính toán bởi Biến đổi Fourier Nhanh (Fast Fourier Transform). Thuật toán nhanh đó xuất phát nhanh chóng từ các số phức đặc biệt $z = e^{i\theta} = \cos \theta + i\sin \theta$
khi góc là $\theta = 2\pi k/n$.

# **10.6 Đồ họa Máy tính (Computer Graphics)**

Đồ họa máy tính liên quan đến hình ảnh. Hình ảnh được di chuyển xung quanh. Tỷ lệ của chúng bị thay đổi. Ba chiều được chiếu xuống thành hai chiều. Tất cả các thao tác chính đều được thực hiện bởi các ma trận - nhưng hình dạng của những ma trận này thật đáng ngạc nhiên.

*Các phép biến đổi của không gian ba chiều được thực hiện với các ma trận $4 \times 4$.* Bạn sẽ mong đợi $3 \times 3$. Lý do của sự thay đổi là một trong bốn thao tác chính không thể được thực hiện bằng phép nhân ma trận $3 \times 3$. Dưới đây là bốn thao tác:

**Tịnh tiến (Translation - dời gốc tọa độ đến một điểm khác $P_0 = (x_0, y_0, z_0)$)**
**Đổi tỷ lệ (Rescaling - nhân với $c$ theo mọi hướng hoặc bởi các hệ số khác nhau $c_1, c_2, c_3$)**
**Phép quay (Rotation - quanh một trục đi qua gốc tọa độ hoặc một trục đi qua $P_0$)**
**Phép chiếu (Projection - lên một mặt phẳng đi qua gốc tọa độ hoặc một mặt phẳng đi qua $P_0$)**

Tịnh tiến là thao tác dễ nhất - chỉ cần cộng $(x_0, y_0, z_0)$ vào mọi điểm. Nhưng điều này không tuyến tính! Không có ma trận $3 \times 3$ nào có thể di chuyển gốc tọa độ. Do đó, chúng ta đổi tọa độ của gốc tọa độ thành $(0, 0, 0, 1)$. Đây là lý do tại sao các ma trận lại là $4 \times 4$. *"Tọa độ thuần nhất (homogeneous coordinates)"* của điểm $(x, y, z)$ là $(x, y, z, 1)$ và bây giờ chúng ta sẽ cho thấy cách chúng hoạt động.

**1. Tịnh tiến (Translation)** Tịnh tiến toàn bộ không gian ba chiều dọc theo vectơ $v_0$. Gốc tọa độ di chuyển đến $(x_0, y_0, z_0)$. Vectơ $v_0$ này được thêm vào mọi điểm $v$ trong $\mathbb{R}^3$. Sử dụng tọa độ thuần nhất, ma trận $4 \times 4$ $T$ tịnh tiến toàn bộ không gian một khoảng $v_0$:
$$\text{Ma trận tịnh tiến} \quad T = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ x_0 & y_0 & z_0 & 1 \end{bmatrix}$$

Quan trọng: *Đồ họa máy tính làm việc với các vectơ hàng.* Chúng ta có vectơ hàng nhân ma trận thay vì ma trận nhân vectơ cột. Bạn có thể nhanh chóng kiểm tra rằng $\begin{bmatrix} 0 & 0 & 0 & 1 \end{bmatrix} T = \begin{bmatrix} x_0 & y_0 & z_0 & 1 \end{bmatrix}$.

Để di chuyển các điểm $(0, 0, 0)$ và $(x, y, z)$ đi một đoạn $v_0$, hãy chuyển sang tọa độ thuần nhất $(0, 0, 0, 1)$ và $(x, y, z, 1)$. Sau đó nhân với $T$. Một vectơ hàng nhân với $T$ cho ra một vectơ hàng. *Mọi $v$ đều di chuyển tới $v + v_0$:* $\begin{bmatrix} x & y & z & 1 \end{bmatrix} T = \begin{bmatrix} x+x_0 & y+y_0 & z+z_0 & 1 \end{bmatrix}$.

Đầu ra cho biết bất kỳ $v$ nào sẽ di chuyển đến đâu. (Nó đi tới $v + v_0$). Quá trình tịnh tiến hiện đạt được bằng một ma trận, điều mà không thể thực hiện được trong $\mathbb{R}^3$.

**2. Thay đổi tỷ lệ (Scaling)** Để làm cho một bức tranh vừa với một trang, chúng tôi thay đổi chiều rộng và chiều cao của nó. Máy photocopy sẽ thu nhỏ một hình xuống còn 90%. Trong đại số tuyến tính, chúng ta nhân với $.9$ lần ma trận đơn vị. Ma trận đó thông thường là $2 \times 2$ cho một mặt phẳng và $3 \times 3$ cho một khối ba chiều. Trong đồ họa máy tính, với các tọa độ thuần nhất, ma trận này *lớn hơn một kích thước:*

**Đổi tỷ lệ mặt phẳng:**
$$S = \begin{bmatrix} .9 & & \\ & .9 & \\ & & 1 \end{bmatrix}$$
     **Đổi tỷ lệ một khối không gian:** $S = \begin{bmatrix} c & 0 & 0 & 0 \\ 0 & c & 0 & 0 \\ 0 & 0 & c & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$.

*Quan trọng: $S$ không phải là $cI$.* Chúng ta giữ số "1" ở góc dưới cùng. Khi đó $\begin{bmatrix} x & y & 1 \end{bmatrix}$ nhân với $S$ cho ra đáp án đúng trong hệ tọa độ thuần nhất. Gốc tọa độ vẫn ở vị trí bình thường vì $\begin{bmatrix} 0 & 0 & 1 \end{bmatrix} S = \begin{bmatrix} 0 & 0 & 1 \end{bmatrix}$.

Nếu chúng ta thay đổi số 1 đó thành $c$, kết quả sẽ rất kỳ lạ. *Điểm $(cx, cy, cz, c)$ giống như $(x, y, z, 1)$.* Tính chất đặc biệt của tọa độ thuần nhất là *nhân với $cI$ không làm di chuyển điểm.* Gốc tọa độ trong $\mathbb{R}^3$ có tọa độ thuần nhất $(0, 0, 0, 1)$ và $(0, 0, 0, c)$ với mọi số $c$ khác không. Đây là ý tưởng đằng sau từ "thuần nhất (homogeneous)".

Việc thay đổi tỷ lệ có thể khác nhau theo các hướng khác nhau. Để đưa một bức tranh có kích thước trọn một trang vừa vào nửa trang, hãy lấy tỷ lệ theo hướng $y$ là $\frac{1}{2}$. Để tạo lề, hãy lấy tỷ lệ theo hướng $x$ là $\frac{3}{4}$. Ma trận đồ họa là đường chéo nhưng không phải $2 \times 2$. Nó là $3 \times 3$ để thay đổi tỷ lệ của một mặt phẳng và $4 \times 4$ để thay đổi tỷ lệ của một không gian:

**Các ma trận đổi tỷ lệ**
$$S = \begin{bmatrix} \frac{3}{4} & & \\ & \frac{1}{2} & \\ & & 1 \end{bmatrix}$$
và $S = \begin{bmatrix} c_1 & & & \\ & c_2 & & \\ & & c_3 & \\ & & & 1 \end{bmatrix}$.

Ma trận $S$ cuối cùng thay đổi tỷ lệ theo các hướng $x, y, z$ bởi các số dương $c_1, c_2, c_3$. Cột phụ trong tất cả các ma trận này giữ lại số 1 ở cuối mỗi vectơ.

*Tóm tắt* Ma trận đổi tỷ lệ $S$ có cùng kích thước với ma trận tịnh tiến $T$. Chúng có thể được nhân với nhau. Để tịnh tiến rồi sau đó đổi tỷ lệ, nhân $vTS$. Để đổi tỷ lệ và sau đó tịnh tiến, nhân $vST$. Chúng có khác nhau không? *Có.*

Điểm $(x, y, z)$ trong $\mathbb{R}^3$ có tọa độ thuần nhất $(x, y, z, 1)$ trong $\mathbb{P}^3$. "Không gian xạ ảnh (projective space)" này không giống như $\mathbb{R}^4$. Nó vẫn là không gian ba chiều. Để đạt được điều đó, $(cx, cy, cz, c)$ cũng chính là điểm $(x, y, z, 1)$. Những điểm của không gian xạ ảnh $\mathbb{P}^3$ đó thực chất là những đường thẳng đi qua gốc tọa độ trong $\mathbb{R}^4$.

Đồ họa máy tính sử dụng các phép biến đổi *affine (affine transformations)*, *tuyến tính cộng với dịch chuyển.* Một phép biến đổi affine $T$ được thực hiện trên $\mathbb{P}^3$ bởi một ma trận $4 \times 4$ với cột thứ tư đặc biệt:
$$A = \begin{bmatrix} a_{11} & a_{12} & a_{13} & 0 \\ a_{21} & a_{22} & a_{23} & 0 \\ a_{31} & a_{32} & a_{33} & 0 \\ a_{41} & a_{42} & a_{43} & 1 \end{bmatrix} = \begin{bmatrix} T(1, 0, 0) & 0 \\ T(0, 1, 0) & 0 \\ T(0, 0, 1) & 0 \\ T(0, 0, 0) & 1 \end{bmatrix}.$$

Ma trận $3 \times 3$ thông thường cho chúng ta ba đầu ra, cái này cho ra bốn. Các đầu ra thông thường đến từ các đầu vào $(1, 0, 0)$ và $(0, 1, 0)$ và $(0, 0, 1)$. Khi phép biến đổi là tuyến tính, ba đầu ra tiết lộ mọi thứ. Khi phép biến đổi là affine, ma trận cũng chứa đầu ra từ $(0, 0, 0)$. Khi đó chúng ta biết độ dịch chuyển.

**3. Phép quay (Rotation)** Một phép quay trong $\mathbb{R}^2$ hoặc $\mathbb{R}^3$ đạt được bằng một ma trận trực giao $Q$. Định thức là $+1$. (Với định thức $-1$, chúng ta có thêm một phép phản xạ qua gương). Hãy bao gồm cột thừa khi bạn sử dụng các tọa độ thuần nhất!
| Phép quay mặt phẳng | $Q = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}$ | trở thành | $R = \begin{bmatrix} \cos \theta & -\sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{bmatrix}$ |
|----------------|---------------------------------------------------------------------------------------------|---------|------------------------------------------------------------------------------------------------------------------|

Ma trận này quay mặt phẳng quanh gốc tọa độ. **Làm thế nào chúng ta sẽ xoay quanh một điểm khác** $(4, 5)$? Câu trả lời làm nổi bật vẻ đẹp của tọa độ thuần nhất. **Tịnh tiến** $(4, 5)$ đến $(0, 0)$, **sau đó quay một góc $\theta$, rồi tịnh tiến** $(0, 0)$ **trở lại** $(4, 5)$:
$$v_{T_-RT_+} = \begin{bmatrix} x & y & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -4 & -5 & 1 \end{bmatrix} \begin{bmatrix} \cos \theta & -\sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 4 & 5 & 1 \end{bmatrix}.$$

Tôi sẽ không thực hiện phép nhân. Vấn đề là áp dụng lần lượt từng ma trận: $v$ tịnh tiến thành $v_{T_-}$, sau đó quay thành $v_{T_-R}$, và tịnh tiến trở lại thành $v_{T_-RT_+}$. Bởi vì mỗi điểm $\begin{bmatrix} x & y & 1 \end{bmatrix}$ là một vectơ hàng, $T_-$ hoạt động trước. Tâm quay $(4, 5)$ — hay nói cách khác là $(4, 5, 1)$ — di chuyển trước tiên đến $(0, 0, 1)$. Phép quay không thay đổi nó. Sau đó $T_+$ di chuyển nó trở lại $(4, 5, 1)$. Tất cả diễn ra như mong đợi. Điểm $(4, 6, 1)$ di chuyển tới $(0, 1, 1)$, sau đó quay một góc $\theta$ và di chuyển trở lại.

Trong không gian ba chiều, mọi phép quay $Q$ đều xoay quanh một trục. Trục không di chuyển - nó là một đường các vectơ riêng với $\lambda = 1$. Giả sử trục nằm dọc theo hướng $z$. Số 1 trong $Q$ là để giữ nguyên trục $z$, số 1 thêm vào trong $R$ là để giữ nguyên gốc tọa độ:
$$Q = \begin{bmatrix} \cos \theta & -\sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{bmatrix} \quad \text{và} \quad R = \begin{bmatrix} Q & 0 \\ 0 & 1 \end{bmatrix}.$$

Bây giờ giả sử phép quay là quanh vectơ đơn vị $a = (a_1, a_2, a_3)$. Với trục $a$ này, ma trận quay $Q$ nằm trong $R$ gồm ba phần:
$$Q = (\cos \theta)I + (1 - \cos \theta) \begin{bmatrix} a_1^2 & a_1 a_2 & a_1 a_3 \\ a_1 a_2 & a_2^2 & a_2 a_3 \\ a_1 a_3 & a_2 a_3 & a_3^2 \end{bmatrix} - \sin \theta \begin{bmatrix} 0 & a_3 & -a_2 \\ -a_3 & 0 & a_1 \\ a_2 & -a_1 & 0 \end{bmatrix}. \quad (1)$$

Trục không di chuyển vì $aQ = a$. Khi $a = (0, 0, 1)$ nằm trên trục $z$, $Q$ này trở thành $Q$ trước đó — đối với phép quay quanh trục $z$.

Phép biến đổi tuyến tính $Q$ luôn nằm ở khối trên bên trái của $R$. Dưới nó ta thấy các số 0, bởi vì phép quay giữ nguyên gốc tọa độ. Khi chúng không phải là số 0, phép biến đổi là affine và gốc tọa độ di chuyển.

**4. Phép chiếu (Projection)** Trong một khóa học đại số tuyến tính, hầu hết các mặt phẳng đều đi qua gốc tọa độ. Trong đời thực, hầu hết không đi qua. Một mặt phẳng đi qua gốc tọa độ là một không gian vectơ. Các mặt phẳng khác là các không gian affine, đôi khi được gọi là "mặt phẳng (flats)". Không gian affine là thứ được tạo ra từ việc tịnh tiến một không gian vectơ.

Chúng ta muốn chiếu các vectơ ba chiều lên các mặt phẳng. Bắt đầu với một mặt phẳng đi qua gốc tọa độ, có vectơ pháp tuyến đơn vị là $n$. (Chúng ta sẽ giữ $n$ là một vectơ cột). Các vectơ trong mặt phẳng thỏa mãn $n^T v = 0$. **Phép chiếu thông thường lên mặt phẳng là ma trận $I - nn^T$.** Để chiếu một vectơ, nhân với ma trận này. Vectơ $n$ được chiếu thành 0, và các vectơ trong mặt phẳng $v$ được chiếu thành chính nó:
$$(I - nn^T)n = n - n(n^T n) = 0 \quad \text{và} \quad (I - nn^T)v = v - n(n^T v) = v.$$

Trong tọa độ thuần nhất ma trận chiếu trở thành $4 \times 4$ (nhưng gốc tọa độ không di chuyển):
$$\text{Phép chiếu lên mặt phẳng } n^T v = 0 \quad P = \begin{bmatrix} I - nn^T & 0 \\ 0 & 1 \end{bmatrix}.$$

Bây giờ hãy chiếu lên một mặt phẳng $n^T(v - v_0) = 0$ *không* đi qua gốc tọa độ. Một điểm trên mặt phẳng là $v_0$. Đây là một không gian affine (hay *flat*). Nó giống như nghiệm của $Av = b$ khi vế phải không bằng 0. Một nghiệm riêng phần $v_0$ được cộng vào không gian hạt nhân — để tạo ra một không gian affine.

Phép chiếu lên mặt phẳng affine có ba bước. Tịnh tiến $v_0$ đến gốc tọa độ bởi $T_-$. Chiếu dọc theo hướng $n$, và tịnh tiến trở lại dọc theo vectơ hàng $v_0$:
$$\text{Phép chiếu lên một mặt phẳng affine (flat)} \quad T_-PT_+ = \begin{bmatrix} I & 0 \\ -v_0 & 1 \end{bmatrix} \begin{bmatrix} I - nn^T & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} I & 0 \\ v_0 & 1 \end{bmatrix}.$$

Tôi nhận ra rằng $T_-$ và $T_+$ là các ma trận nghịch đảo: tịnh tiến đi và tịnh tiến trở lại. Chúng giống như các ma trận sơ cấp trong Chương 2.

Các bài tập sẽ bao gồm các ma trận phản xạ, còn được gọi là *ma trận gương (mirror matrices)*. Đây là loại thứ năm cần thiết trong đồ họa máy tính. Một sự phản xạ di chuyển mỗi điểm đi xa gấp đôi so với phép chiếu - **sự phản xạ đi xuyên qua mặt phẳng và ra phía bên kia**. Vì vậy, hãy đổi phép chiếu $I - nn^T$ thành $I - 2nn^T$ để được ma trận gương.

Ma trận $P$ cho một phép chiếu "song song". Tất cả các điểm di chuyển song song với $n$, cho đến khi chúng chạm vào mặt phẳng. Lựa chọn khác trong đồ họa máy tính là phép chiếu "phối cảnh (perspective)". Loại này phổ biến hơn vì nó bao gồm phép thu ngắn. Với phối cảnh, một vật thể trông lớn hơn khi nó lại gần hơn. Thay vì giữ nguyên sự song song với $n$ (và song song với nhau), các đường chiếu hướng *về phía mắt* — tâm của phép chiếu. Đây là cách chúng ta cảm nhận được chiều sâu trong một bức ảnh hai chiều.

Vấn đề cơ bản của đồ họa máy tính bắt đầu với một cảnh và một vị trí nhìn. Lý tưởng nhất, hình ảnh trên màn hình là những gì người xem sẽ nhìn thấy. Hình ảnh đơn giản nhất chỉ gán một bit cho mỗi thành phần hình ảnh nhỏ — được gọi là một *pixel*. Nó là sáng hoặc tối. Điều này tạo ra một bức tranh đen trắng không có bóng. Bạn sẽ không tán thành. Trong thực tế, chúng ta gán các mức đổ bóng từ $0$ đến $2^8$ đối với ba màu như đỏ, xanh lục, và xanh lam. Điều đó có nghĩa là $8 \times 3 = 24$ bit cho mỗi pixel. Nhân với số lượng pixel, và chúng ta cần rất nhiều bộ nhớ!

Về mặt vật lý, *bộ đệm khung mành (raster frame buffer)* sẽ điều hướng chùm electron. Nó quét giống như một chiếc tivi. Chất lượng được kiểm soát bởi số lượng pixel và số lượng bit trên mỗi pixel. Trong lĩnh vực này, văn bản tiêu chuẩn là *Computer Graphics: Principles and Practice* (Đồ họa Máy tính: Các Nguyên lý và Thực hành) của Hughes, Van Dam, McGuire, Skylar, Foley, Feiner và Akeley (phiên bản thứ 3, Addison-Wesley, 2014). Các ghi chú của Ronald Goldman và Tony DeRose cũng là những tài liệu tham khảo tuyệt vời.

#### **• TÓM TẮT CÁC Ý TƯỞNG TRỌNG TÂM •**

**1.** Đồ họa máy tính cần cả thao tác dịch chuyển $T(v) = v + v_0$ lẫn các thao tác tuyến tính $T(v) = Av$.
**2.** Một phép dịch chuyển trong $\mathbb{R}^n$ có thể được thực hiện bởi một ma trận bậc $n + 1$, sử dụng các tọa độ thuần nhất.
**3.** Thành phần dư 1 trong $\begin{bmatrix} x & y & z & 1 \end{bmatrix}$ được giữ nguyên khi tất cả các ma trận đều có các số $0, 0, 0, 1$ ở cột cuối cùng.

#### **Tập bài tập 10.6 (Problem Set 10.6)**

**1** Một điểm điển hình trong $\mathbb{R}^3$ là $x\mathbf{i} + y\mathbf{j} + z\mathbf{k}$. Các vectơ tọa độ $\mathbf{i}, \mathbf{j}$ và $\mathbf{k}$ là $(1, 0, 0), (0, 1, 0), (0, 0, 1)$. Tọa độ của điểm là $(x, y, z)$. Điểm này trong đồ họa máy tính là $x\mathbf{i} + y\mathbf{j} + z\mathbf{k} +$ **gốc tọa độ**. Tọa độ thuần nhất của nó là $(\_ , \_ , \_ , \_ )$. Các tọa độ khác cho cùng một điểm đó là $(\_ , \_ , \_ , \_ )$.
**2** Một phép biến đổi tuyến tính $T$ được xác định khi chúng ta biết $T(\mathbf{i}), T(\mathbf{j}), T(\mathbf{k})$. Đối với phép biến đổi affine chúng ta cũng cần $T(\_\_\_)$. Điểm đầu vào $(x, y, z, 1)$ được biến đổi thành $xT(\mathbf{i}) + yT(\mathbf{j}) + zT(\mathbf{k}) + \_\_\_$.
**3** Nhân ma trận $T$ kích thước $4 \times 4$ để tịnh tiến dọc theo $(1, 4, 3)$ với ma trận $T_1$ để tịnh tiến dọc theo $(0, 2, 5)$. Tích $TT_1$ là sự tịnh tiến dọc theo \_\_\_.
**4** Viết ma trận $S$ kích thước $4 \times 4$ làm thay đổi tỷ lệ một hằng số $c$. Nhân $ST$ và cả $TS$, trong đó $T$ là phép tịnh tiến đi một đoạn $(1, 4, 3)$. Để phóng to hình ảnh xung quanh điểm trung tâm $(1, 4, 3)$, bạn sẽ sử dụng $vST$ hay $vTS$?
**5** Ma trận tỷ lệ $S$ nào (trong tọa độ thuần nhất, nên là kích thước $3 \times 3$) sẽ tạo ra một trang hình vuông kích thước $1 \times 1$ từ một trang tiêu chuẩn $8.5 \times 11$?
**6** Ma trận $4 \times 4$ nào sẽ dời góc của hình lập phương về gốc tọa độ và sau đó nhân tất cả các chiều dài với 2? Góc của hình lập phương ban đầu nằm tại $(1, 1, 2)$.
**7** Khi ba ma trận trong phương trình 1 nhân với vectơ đơn vị $a$, hãy chỉ ra rằng chúng cho kết quả $(\cos \theta)a$ và $(1 - \cos \theta)a$ và $\mathbf{0}$. Phép cộng cho ra $aQ = a$ và trục quay không bị thay đổi.
**8** Nếu $b$ vuông góc với $a$, nhân với ba ma trận trong 1 ta được $(\cos \theta)b$ và $0$ và một vectơ vuông góc với $b$. Vậy $Qb$ tạo một góc $\theta$ với $b$. *Đây là phép quay.*
**9** Ma trận chiếu $3 \times 3$ $I - nn^T$ lên mặt phẳng $\frac{2}{3}x + \frac{2}{3}y + \frac{1}{3}z = 0$ là gì? Trong tọa độ thuần nhất, hãy thêm các phần tử $0, 0, 0, 1$ dưới dạng hàng và cột bổ sung trong $P$.
**10** Với cùng một ma trận $P$ kích thước $4 \times 4$, nhân $T_- P T_+$ để tìm ma trận chiếu lên mặt phẳng $\frac{2}{3}x + \frac{2}{3}y + \frac{1}{3}z = 1$. Phép tịnh tiến $T_-$ dời một điểm trên mặt phẳng đó (chọn một điểm) đến $(0, 0, 0, 1)$. Ma trận nghịch đảo $T_+$ dời nó trở lại.
**11** Chiếu $(3, 3, 3)$ lên các mặt phẳng đó. Sử dụng $P$ ở Bài 9 và $T_-PT_+$ ở Bài 10.
**12** Nếu bạn chiếu một hình vuông lên một mặt phẳng, bạn sẽ có được hình gì?
**13** Nếu bạn chiếu một hình lập phương lên một mặt phẳng, hình chiếu có dạng đường bao gì? Hãy đặt mặt phẳng chiếu vuông góc với một đường chéo của hình lập phương.
**14** Ma trận gương $3 \times 3$ làm phản xạ qua mặt phẳng $n^T v = 0$ là $M = I - 2nn^T$. Hãy tìm điểm phản xạ của điểm $(3, 3, 3)$ qua mặt phẳng $\frac{2}{3}x + \frac{2}{3}y + \frac{1}{3}z = 0$.
**15** Tìm phản xạ của điểm $(3, 3, 3)$ qua mặt phẳng $\frac{2}{3}x + \frac{2}{3}y + \frac{1}{3}z = 1$. Thực hiện ba bước $T_-MT_+$ bằng ma trận $4 \times 4$: dùng $T_-$ tịnh tiến sao cho mặt phẳng đi qua gốc tọa độ, phản xạ điểm vừa dời $(3, 3, 3, 1)T_-$ qua mặt phẳng đó, sau đó dời lại nhờ $T_+$.
**16** Vectơ nối giữa gốc tọa độ $(0, 0, 0, 1)$ và điểm $(x, y, z, 1)$ là hiệu $v = \_\_\_$. Trong tọa độ thuần nhất, các vectơ kết thúc bằng \_\_\_. Vì vậy, chúng ta cộng một \_\_\_ với một điểm, chứ không phải cộng một điểm với một điểm.
**17** Nếu bạn chỉ nhân tọa độ *cuối cùng* của mỗi điểm để có được $(x, y, z, c)$, bạn sẽ đổi tỷ lệ toàn bộ không gian theo số lượng là \_\_\_. Sở dĩ như vậy vì điểm $(x, y, z, c)$ giống như $(\_ , \_ , \_ , 1)$.

# **10.7 Đại số Tuyến tính cho Mật mã (Linear Algebra for Cryptography)**

**1** Các bộ mã có thể sử dụng các trường hữu hạn làm bảng chữ cái: các chữ cái trong thông điệp trở thành các số $0, 1, \dots, p - 1$.
**2** Các con số được cộng và nhân *(mod $p$).* Chia cho $p$, giữ lại phần dư.
**3** Mật mã Hill nhân các khối thông điệp với một ma trận bí mật $E$ *(mod $p$).*
**4** Để giải mã, nhân mỗi khối với ma trận nghịch đảo $D$ *(mod $p$).* Đây không phải là một bộ mã bảo mật lắm!

**Mật mã học (Cryptography) là nói về mã hóa và giải mã thông điệp.** Các ngân hàng lúc nào cũng làm việc này với các thông tin tài chính. Đáng ngạc nhiên là các thuật toán hiện đại có thể liên quan tới các mảng toán học cực kỳ sâu sắc. "Các đường cong Elliptic" đóng vai trò quan trọng trong mật mã học, cũng giống như trong chứng minh mang tính chấn động của Andrew Wiles đối với Định lý Cuối cùng của Fermat.

Phần này sẽ không đi xa đến vậy! Nhưng nó sẽ là trải nghiệm đầu tiên của chúng ta *với các trường hữu hạn (finite fields)* và *không gian vectơ hữu hạn.* Trường cho $\mathbb{R}^n$ chứa tất cả các số thực. Trường cho "số học mô-đun" chỉ chứa $p$ số nguyên $0, 1, \dots, p - 1$. Từng có vô số vectơ trong $\mathbb{R}^n$ — bây giờ sẽ chỉ có $p^n$ thông điệp có độ dài $n$ trong không gian thông điệp. Bảng chữ cái từ A đến Z là hữu hạn (chẳng hạn như $p = 26$).

Các đoạn mã trong phần này sẽ dễ bị bẻ khóa - chúng quá đơn giản đối với mục đích bảo mật thực tế. Sức mạnh của máy tính đòi hỏi mật mã phức tạp hơn, vì sức mạnh đó sẽ nhanh chóng phát hiện ra một ma trận mã hóa nhỏ. Nhưng một bộ mã ma trận (Mật mã Hill) sẽ cho phép chúng ta thấy đại số tuyến tính hoạt động theo một phương thức mới.

Tất cả các tính toán trong quá trình mã hóa và giải mã của chúng ta sẽ là **"mod $p$".** Nhưng các khái niệm trọng tâm của tính độc lập tuyến tính, cơ sở, ma trận nghịch đảo và định thức vẫn tồn tại sau sự thay đổi này. Chúng ta sẽ làm "đại số tuyến tính với các trường hữu hạn". Dưới đây là ý nghĩa của thuật ngữ *mod $p$:*
| $2 \equiv 2 \pmod{5}$ | có nghĩa là $27 - 2$ chia hết cho 5  |
|-----------------------|----------------------------------------|
| $y \equiv x \pmod{p}$ | có nghĩa là $y - x$ chia hết cho $p$ |

Việc chia $y$ cho 5 sẽ cho ra một trong năm phần dư có thể có: $x = 0, 1, 2, 3, 4$. Tất cả các số $5, -5, 10, -10, \dots$ chia không dư đều đồng dư với không *(mod $5$).* Các số $y = 6, -4, 11, -9, \dots$ đều đồng dư với $x = 1 \pmod{5}$.

Chúng tôi sử dụng từ **đồng dư (congruent)** cho ký hiệu $\equiv$ và chúng tôi gọi đây là "số học mô-đun (modular arithmetic)". Mỗi số nguyên $y$ sẽ cho ra một trong các giá trị $x = 0, 1, 2, \dots, p - 1$.

*Lý thuyết này hoạt động tốt nhất nếu $p$ là một số nguyên tố.* Với $p = 26$ chữ cái từ A đến Z, thật không may là chúng ta không bắt đầu với một số nguyên tố $p$. Mật mã có thể giải quyết vấn đề này.

#### **Số học Mô-đun (Modular Arithmetic)**

Đại số tuyến tính dựa trên các tổ hợp tuyến tính của các vectơ. Bây giờ các vectơ của chúng ta $(x_1, \dots, x_n)$ là các chuỗi số nguyên giới hạn ở $x = 0, 1, \dots, p - 1$. Tất cả các tính toán đều cho ra các số nguyên này khi chúng ta làm việc *"mod $p$".* Điều này có nghĩa là: *Mọi số nguyên $y$ nằm ngoài phạm vi đó đều được chia cho $p$ và $x$ là phần dư:*
| $y = qp + x$ | $y \equiv x \pmod{p}$ | $y$ chia cho $p$ dư $x$ |
|---------------|-----------------------|--------------------------------------|

**Phép cộng** *mod* 3: $10 \equiv 1 \pmod{3}$ và $16 \equiv 1 \pmod{3}$ và $10 + 16 \equiv 1 + 1 \pmod{3}$
Tôi có thể cộng 10 + 16 và chia 26 cho 3 để lấy số dư là 2.
Hoặc tôi có thể chỉ cộng các phần dư $1 + 1$ để ra cùng câu trả lời 2.

**Phép cộng** *mod* 2: $11 \equiv 1 \pmod{2}$ và $17 \equiv 1 \pmod{2}$ và $11 + 17 = 28 \equiv 0 \pmod{2}$
Các số dư được cộng thành $1 + 1$ *nhưng đây không phải là $2$.* Bước cuối cùng là $2 \equiv 0 \pmod{2}$.

**Phép cộng** *mod $p$* hoàn toàn hợp lý. **Phép nhân** *mod $p$* cũng vậy. Ví dụ với $p = 3$:
$10 \equiv 1 \pmod{3}$ nhân với $16 \equiv 1 \pmod{3}$ cho ra $1 \times 1 = 1$, tức là $160 \equiv 1 \pmod{3}$.
$5 \equiv 2 \pmod{3}$ nhân với $8 \equiv 2 \pmod{3}$ cho ra $2 \times 2 = 4 \equiv 1$, tức là $40 \equiv 1 \pmod{3}$.

Kết luận: Chúng ta có thể cộng và nhân theo modulo $p$ một cách an toàn. Vì vậy chúng ta có thể tạo các tổ hợp tuyến tính. Đây là thao tác trọng tâm trong đại số tuyến tính. **Nhưng chúng ta có thể chia không?**

Trong trường số thực, nghịch đảo là $1 / y$ (đối với bất kỳ số nào trừ $y = 0$). Điều này có nghĩa là: Chúng ta tìm thấy một số thực $z$ khác sao cho $yz = 1$. Tính khả nghịch là một yêu cầu đối với một trường. **Sự đảo ngược có luôn khả thi không** đối với *mod $p$?* Đối với mỗi số $y = 1, \dots, p - 1$, liệu ta có thể tìm được số $z = 1, \dots, p - 1$ sao cho $yz \equiv 1 \pmod{p}$?

Các ví dụ $3 \times 4 \equiv 1 \pmod{11}$ và $2 \times 6 \equiv 1 \pmod{11}$ và $5 \times 9 \equiv 1 \pmod{11}$ đều thành công. Bạn có thể giải $7z \equiv 1 \pmod{11}$ không? Nghịch đảo các con số sẽ là chìa khóa để nghịch đảo các ma trận.

Hãy để tôi cho thấy rằng việc nghịch đảo theo *mod $p$* gặp vấn đề khi $p$ không phải là số nguyên tố. Ví dụ $p = 26$ phân tích thành $2 \times 13$. **Khi đó $y = 2$ không thể có nghịch đảo $z \pmod{26}$.** Yêu cầu $2z \equiv 1 \pmod{26}$ không thể thỏa mãn vì $2z$ và $26$ đều là số chẵn.

Tương tự 5 không có nghịch đảo $z$ khi $p$ là 25. Chúng ta không thể giải $5z \equiv 1 \pmod{25}$. Số $5z - 1$ không bao giờ là bội số của 5, do đó nó không thể là bội số của 25.

**Phép nghịch đảo mọi $y$ ($0 < y < p$) sẽ khả thi khi và chỉ khi $p$ là số nguyên tố.**

Quá trình nghịch đảo cần các số $y, 2y, 3y, \dots, py$ có các số dư khác nhau khi chia cho $p$.

Nếu $my$ và $ny$ có cùng phần dư $x$ thì $(m - n)y$ sẽ chia hết cho $p$.

Số nguyên tố $p$ sẽ phải là ước của $m - n$ hoặc của $y$. Cả hai đều không thể.

*Do đó $y, 2y, \dots, py$ có các số dư khác nhau:* **Một trong các số dư đó phải là $x = 1$.**

## Máy Enigma và Mật mã Hill (The Enigma Machine and the Hill Cipher)

Lester Hill đã công bố bộ mã của ông (hệ thống của ông về mã hóa và giải mã) trên tạp chí American Mathematical Monthly (1929). Ý tưởng rất đơn giản, nhưng theo một cách nào đó nó đã khởi đầu quá trình chuyển đổi mật mã học từ ngôn ngữ học sang toán học. Các bộ mã cho đến thời điểm đó chủ yếu là pha trộn các bảng chữ cái và sắp xếp lại các thông điệp. **Mã Enigma** được Hải quân Đức sử dụng trong Thế chiến II là một bước tiến khổng lồ — sử dụng các cỗ máy mà đối với chúng ta trông giống như những chiếc máy tính sơ khai. Người Anh đã thiết lập Bletchley Park để phá mã Enigma. Họ đã thuê những người giải câu đố và các chuyên gia ngôn ngữ. Và do may mắn, họ cũng có được Alan Turing.

Tôi không biết liệu bạn đã xem bộ phim về ông ấy chưa: *The Imitation Game* (Trò chơi mô phỏng). Rất nhiều trong số đó là không thực tế (giống như *Good Will Hunting* và *A Beautiful Mind* tại MIT). Nhưng ý tưởng cốt lõi về việc phá mã Enigma là chính xác, sử dụng những điểm yếu của con người trong quá trình mã hóa và phát sóng. Bộ tư lệnh hải quân Đức đã công khai gửi đi các mệnh lệnh được mã hóa của họ - biết rằng các đoạn mã quá phức tạp để có thể bị bẻ khóa (nếu không có những điểm yếu đó). Việc bẻ khóa đòi hỏi các thiết bị điện tử của Anh phải vô hiệu hóa các thiết bị điện tử của Đức. Nó cũng đòi hỏi một thiên tài.

Alan Turing chắc chắn là một thiên tài — nhà toán học xuất chúng nhất của nước Anh. Cuộc đời ông cuối cùng là một bi kịch và ông đã tự kết liễu nó vào năm 1954. Cuốn tiểu sử của Andrew Hodges rất xuất sắc. Turing đến Bletchley Park ngay sau ngày Ba Lan bị xâm lược. Phải dành lời khen cho Winston Churchill vì ông đã hỗ trợ nhanh chóng và toàn diện khi cần đến sự hỗ trợ của ông.

Cỗ máy Enigma có các bánh răng và bánh xe. Mật mã Hill chỉ cần một ma trận. Đó là bộ mã sẽ được giải thích bây giờ, sử dụng đại số tuyến tính. Bạn sẽ thấy quá trình giải mã liên quan đến các ma trận nghịch đảo như thế nào. Tất cả các bước đều sử dụng số học mô-đun, nhân và nghịch đảo *mod p*.

Tôi sẽ theo dõi phần trình bày súc tích của Giáo sư Spickler của Đại học Salisbury, thứ ông đã công bố trên Web: [facultyfp.salisbury.edu/despickler/personal/index.asp](http://facultyfp.salisbury.edu/despickler/personal/index.asp)

## Số học Mô-đun với Ma trận (Modular Arithmetic with Matrices)

Cộng, trừ, và nhân là tất cả những gì chúng ta cần đối với $Ax$ (ma trận nhân vectơ). Để nhân *mod p* chúng ta có thể nhân các số nguyên trong $A$ với các số nguyên trong $x$ như bình thường — và sau đó thay thế mọi thành phần của $Ax$ bằng giá trị của nó *mod p*.

**Các câu hỏi then chốt:** Khi nào chúng ta có thể giải $Ax \equiv b \pmod{p}$? Chúng ta vẫn có bốn không gian con $C(A), N(A), C(A^T), N(A^T)$ chứ? Chúng vẫn trực giao từng đôi một chứ? Liệu vẫn có một ma trận nghịch đảo *mod p* bất cứ khi nào định thức của $A$ khác không *mod p* không? Tôi rất vui khi nói rằng ba câu trả lời cuối cùng là *có* (nhưng câu hỏi về nghịch đảo yêu cầu $p$ phải là một số nguyên tố).

Chúng ta có thể tìm $A^{-1} \pmod{p}$ bằng phép khử Gauss-Jordan, rút gọn $\begin{bmatrix} A & I \end{bmatrix}$ thành $\begin{bmatrix} I & A^{-1} \end{bmatrix}$ như trong Phần 2.5. Hoặc chúng ta có thể sử dụng các định thức và ma trận phần bù đại số $C$ trong công thức $A^{-1} = (\det A)^{-1} C^T$. Tôi sẽ làm việc *mod 3* với một ma trận số nguyên $A$ kích thước $2 \times 2$:

$$\begin{bmatrix} A & I \end{bmatrix} = \begin{bmatrix} 2 & 0 & 1 & 0 \\ 2 & 1 & 0 & 1 \end{bmatrix} \rightarrow \begin{bmatrix} 2 & 0 & 1 & 0 \\ 0 & 1 & 2 & 1 \end{bmatrix} \rightarrow \begin{matrix} \text{nhân hàng 1} \\ \text{với } 2^{-1} \equiv 2 \end{matrix} \rightarrow \begin{bmatrix} 1 & 0 & 2 & 0 \\ 0 & 1 & 2 & 1 \end{bmatrix} = \begin{bmatrix} I & A^{-1} \end{bmatrix}$$

Thật tình cờ $A^{-1} \equiv A$! Nhân $A$ với $A \pmod{3}$ mang lại ma trận đơn vị:
$$A^2 = AA^{-1} = \begin{bmatrix} 2 & 0 \\ 2 & 1 \end{bmatrix} \begin{bmatrix} 2 & 0 \\ 2 & 1 \end{bmatrix} = \begin{bmatrix} 4 & 0 \\ 6 & 1 \end{bmatrix} \equiv \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \pmod{3}.$$

Định thức của $A$ là 2, và công thức phần bù đại số từ Phần 5.3 cũng cho $A^{-1} \equiv A$:
$$\begin{bmatrix} 2 & 0 \\ 2 & 1 \end{bmatrix}^{-1} = 2^{-1} \begin{bmatrix} 1 & -0 \\ -2 & 2 \end{bmatrix} \equiv 2 \begin{bmatrix} 1 & -0 \\ -2 & 2 \end{bmatrix} \equiv \begin{bmatrix} 2 & 0 \\ 2 & 1 \end{bmatrix} \pmod{3}.$$

**Định lý.** $A^{-1}$ tồn tại $\pmod{p}$ khi và chỉ khi $(\det A)^{-1}$ tồn tại $\pmod{p}$.
Yêu cầu là: $\det A$ và $p$ không có ước chung.

## Mã hóa bằng Mật mã Hill (Encryption with the Hill Cipher)

Mật mã ban đầu sử dụng các chữ cái từ A đến Z với $p = 26$. Hill đã chọn một ma trận mã hóa $E$ kích thước $n \times n$ sao cho $\det E$ không chia hết cho 2 hoặc 13. Khi đó số $\det E$ có một nghịch đảo $\pmod{26}$ và ma trận $E$ cũng vậy. Ma trận nghịch đảo $E^{-1} \equiv D \pmod{26}$ sẽ là ma trận giải mã dùng để giải mã thông điệp.

Bây giờ chuyển đổi mỗi chữ cái của thông điệp thành một số từ 0 đến 25. Sự lựa chọn hiển nhiên từ $A = 0$ đến $Z = 25$ là có thể chấp nhận được bởi vì ma trận sẽ làm cho bộ mã này mạnh hơn.

Bỏ qua các khoảng trắng và chia thông điệp thành các khối $v_1, v_2, \dots$ có kích thước $n$.
Sau đó nhân mỗi khối thông điệp $(\pmod{p})$ với ma trận mã hóa $E$.
Thông điệp đã được mã hóa là $Ev_1, Ev_2, \dots$ và bạn biết người giải mã sẽ làm gì.

$$\text{Ví dụ của Spickler có } D = E^{-1} = \begin{bmatrix} 2 & 3 & 15 \\ 5 & 8 & 12 \\ 1 & 13 & 4 \end{bmatrix}^{-1} \equiv \begin{bmatrix} 10 & 19 & 16 \\ 4 & 23 & 7 \\ 17 & 5 & 19 \end{bmatrix} \pmod{26}.$$

Tất nhiên một người giải mã sẽ không biết $E$ hay $D$. Và kích thước khối $n$ nói chung cũng không được biết. Đối với các ma trận mà Hill đã nghĩ đến, $n$ sẽ không quá lớn và máy tính có thể nhanh chóng khám phá ra $E$ và $D$.

Tôi không chắc liệu Mật mã của Hill có trở nên rất khó bẻ khóa hay không bằng cách chọn các ma trận rất lớn và một số nguyên tố lớn $p$. Và bằng cách mã hóa thông điệp đã mã hóa lần thứ hai, sử dụng kích thước khối $n_2$ khác và ma trận lớn $E_2$ và số nguyên tố lớn $p_2$.

## Các Trường Hữu hạn và Các Không gian Vectơ Hữu hạn (Finite Fields and Finite Vector Spaces)

Trong đại số, một trường $\mathbf{F}$ là một tập hợp các số vô hướng có thể được cộng và nhân và lấy nghịch đảo (trừ số 0 không thể lấy nghịch đảo). Các ví dụ quen thuộc là tập số thực $\mathbf{R}$ và tập số phức $\mathbf{C}$ và tập số hữu tỷ $\mathbf{Q}$ (chứa mọi tỷ số $p/q$ của các số nguyên). Từ một trường bạn xây dựng các vectơ $v = (f_1, f_2, \dots, f_n)$. Từ các tổ hợp tuyến tính của các vectơ bạn xây dựng các không gian vectơ. Vì vậy đại số tuyến tính bắt đầu bằng một trường $\mathbf{F}$.

Tôi đã dạy học trong mười năm từ một cuốn sách giáo khoa bắt đầu bằng các trường. Trên con đường đi đến $\mathbf{R}^n$, chúng tôi đã đánh mất rất nhiều sinh viên. Đó là một tín hiệu — trọng tâm đã bị đặt sai chỗ nếu chúng tôi muốn khóa học trở nên hữu ích. Tôi tin rằng cách đúng đắn là tìm hiểu $\mathbf{R}^n$ và các không gian con của nó trước tiên, như các bạn đang làm. Sau đó bạn có thể xem xét các trường và không gian vectơ khác với một câu hỏi tự nhiên trong đầu: *Có gì mới khi trường không phải là $\mathbf{R}$?*

Những trang này đang đặt ra câu hỏi đó cho các trường hữu hạn. Các khả năng trở nên hạn chế hơn nhưng cũng vô cùng thú vị. Điểm khởi đầu (và chưa hẳn là điểm kết thúc) là trường hữu hạn $\mathbf{F}_p$. Nó chỉ chứa các số $0, 1, \dots, p - 1$ và $p$ là một số nguyên tố. Trước tiên tôi sẽ tập trung vào trường $\mathbf{F}_2$ chỉ có 2 phần tử "0" và "1". Bạn có thể coi 0 và 1 như "chẵn" và "lẻ" vì các quy tắc cộng và nhân được tuân theo bởi các số chẵn và số lẻ: chẵn + lẻ = *lẻ* và chẵn $\times$ lẻ = *chẵn*.

| Bảng phép cộng | 0 | 1 |   | Bảng phép nhân | 0 | 1 |
|----------------|---|---|---|----------------|---|---|
| **0**          | 0 | 1 |   | **0**          | 0 | 0 |
| **1**          | 1 | 0 |   | **1**          | 0 | 1 |

Đây là phép cộng và phép nhân *"mod 2"*.

Từ trường $\mathbf{F}_2$ này chúng ta có thể xây dựng các vectơ như $v = (0, 0, 1)$ và $w = (1, 0, 1)$. Có ba thành phần với hai lựa chọn cho mỗi thành phần: có tổng cộng $2^3 = 8$ vectơ khác nhau trong không gian vectơ $(\mathbf{F}_2)^3$. Bạn biết các yêu cầu đối với một không gian con và những khả năng mà nó mở ra:

(a) Không gian con không chiều chỉ chứa $\mathbf{0} = (0, 0, 0)$.
(b) Các không gian con một chiều chứa $\mathbf{0}$ và một vectơ như $v$. Chú ý rằng $v + v = \mathbf{0}$!
(c) Các không gian con hai chiều có cơ sở như $v$ và $w$ và 4 vectơ $\mathbf{0}, v, w, v + w$.
(d) Không gian con ba chiều đầy đủ $(\mathbf{F}_2)^3$ với 8 vectơ.

Các cơ sở có thể có cho $(\mathbf{F}_2)^3$ là gì? Cơ sở tiêu chuẩn chứa $(1, 0, 0)$ và $(0, 1, 0)$ và $(0, 0, 1)$. Các vectơ đó là độc lập tuyến tính và chúng sinh ra $(\mathbf{F}_2)^3$. Tám tổ hợp của chúng với các hệ số 0 và 1 lấp đầy toàn bộ $(\mathbf{F}_2)^3$.

Thế còn các ma trận nhân với các vectơ đó thì sao? Các ma trận sẽ là $1 \times 3$, hoặc $2 \times 3$, hoặc $3 \times 3$. Khi chúng là $3 \times 3$, chúng ta có thể hỏi liệu chúng có khả nghịch không. Định thức của chúng chỉ có thể là 0 (ma trận suy biến) hoặc 1 (ma trận khả nghịch). Hãy để tôi dành cho bạn niềm vui của việc quyết định xem những ma trận này có khả nghịch hay không. *Và làm thế nào bạn tìm thấy nghịch đảo?*
$$A = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix} \quad B = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{bmatrix} \quad C = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{bmatrix}$$

Trong số $2^9$ ma trận có thể có trên $\mathbf{F}_2$, tôi đoán rằng phần lớn là suy biến.

Để kết thúc cuộc thảo luận này về $\mathbf{F}_2$, tôi đề cập đến một trường có $2^2 = 4$ phần tử. Nó sẽ không đến từ phép nhân *(mod 4)*, vì 4 không phải là số nguyên tố. Phép nhân 2 với 2 sẽ cho 0 (và 2 không có nghịch đảo): *không phải là một trường.* Nhưng chúng ta có thể bắt đầu bằng các số 0 và 1 trong $\mathbf{F}_2$ và phát minh ra thêm hai số $a$ và $1 + a$ — miễn là chúng tuân theo hai quy tắc sau: $(a + a = 0)$ và $(a \times a = 1 + a)$. Khi đó $a$ và $1 + a$ là nghịch đảo của nhau. Không rõ ràng lắm!

| Cộng   | 0     | 1     | $a$   | $1+a$ | Nhân   | 0 | 1     | $a$   | $1+a$ |
|--------|-------|-------|-------|-------|--------|---|-------|-------|-------|
| 0      | 0     | 1     | $a$   | $1+a$ | 0      | 0 | 0     | 0     | 0     |
| 1      | 1     | 0     | $1+a$ | $a$   | 1      | 0 | 1     | $a$   | $1+a$ |
| $a$    | $a$   | $1+a$ | 0     | 1     | $a$    | 0 | $a$   | $1+a$ | 1     |
| $1+a$  | $1+a$ | $a$   | 1     | 0     | $1+a$  | 0 | $1+a$ | 1     | $a$   |

Ngoài $p = 2$, chúng ta có các trường $\mathbf{F}_p$ đối với tất cả các số nguyên tố $p$. Chúng sử dụng phép cộng và phép nhân *mod p*. Chúng là bảng chữ cái cho các bộ mã. Chúng cung cấp các thành phần cho các vectơ $v = (f_1, \dots, f_n)$ trong không gian $(\mathbf{F}_p)^n$. Chúng cung cấp các phần tử cho các ma trận nhân với các vectơ đó. Các trường $\mathbf{F}_p$ này là các trường hữu hạn được sử dụng thường xuyên nhất.

Các trường hữu hạn duy nhất khác có $p^k$ phần tử. Ví dụ trên về $0, 1, a, 1+a$ có $2^2 = 4$ phần tử. Chúng ta sẽ dừng ở đó và an toàn quay trở lại với $\mathbf{R}$.

### **Tập bài tập 10.7 (Problem Set 10.7)**

**1** Nếu bạn nhân $n$ số nguyên (chẵn hoặc lẻ), khi nào câu trả lời là lẻ? Dịch sang phép nhân *(mod 2)*: Nếu bạn nhân các số 0 và 1, khi nào câu trả lời là 1?
**2** Nếu bạn cộng $n$ số nguyên (chẵn hoặc lẻ), khi nào tổng các con số là lẻ? Dịch sang phép cộng các số 0 và 1 *(mod 2)*. Khi nào chúng cộng lại thành 1?
**3** (a) Nếu $Y_1 = x_1$ và $Y_2 = x_2$, tại sao $Y_1 + Y_2 = x_1 + x_2$? Tất cả đều *mod p. Gợi ý:* $Y_1 = pq_1 + x_1$ và $Y_2 = pq_2 + x_2$. Bây giờ hãy cộng $Y_1 + Y_2$.
(b) Bạn có chắc chắn rằng $x_1 + x_2$ nhỏ hơn $p$ không? *Không.* Đưa ra một ví dụ nơi có một số $x$ nhỏ hơn với $(Y_1 + Y_2) \equiv x \pmod{p}$.
**4** $p = 39$ không phải là số nguyên tố. Tìm một số $a$ không có nghịch đảo $z \pmod{39}$. Điều này có nghĩa là $az \equiv 1 \pmod{39}$ không có nghiệm. Sau đó tìm một ma trận $A$ kích thước $2 \times 2$ không có ma trận nghịch đảo $Z \pmod{39}$. Điều này có nghĩa là $AZ \equiv I \pmod{39}$ không có nghiệm.
**5** Chứng tỏ rằng $y \equiv x \pmod{p}$ dẫn đến $-y \equiv -x \pmod{p}$.
**6** Tìm một ma trận có các cột độc lập trong $\mathbf{R}^2$ nhưng có các cột phụ thuộc *(mod 5).*
**7** Tất cả các ma trận $2 \times 2$ gồm các số 0 và 1 mà khả nghịch *(mod 2)* là gì?
**8** Không gian hàng của $A$ vẫn có trực giao với không gian hạt nhân trong số học mô-đun *(mod 11)* không? Các cơ sở của các không gian con đó có còn là cơ sở *(mod 11)* không?
**9** (Mật mã Hill) Chia thông điệp THISWHOLEBOOKISINCODE thành các khối gồm 3 chữ cái. Thay thế mỗi chữ cái bằng một con số từ 1 đến 26 (theo thứ tự bảng chữ cái bình thường). Nhân mỗi khối với ma trận $L$ kích thước $3 \times 3$ có số 1 trên và dưới đường chéo. Thông điệp đã mã hóa (bằng số) là gì và bạn sẽ giải mã nó như thế nào?
**10** Giả sử bạn biết thông điệp gốc (văn bản thô). Giả sử bạn cũng thấy thông điệp đã mã hóa. Bạn sẽ bắt đầu như thế nào để khám phá ra ma trận trong Mật mã Hill? Đối với một thông điệp rất dài, bạn có kỳ vọng sẽ thành công không?
