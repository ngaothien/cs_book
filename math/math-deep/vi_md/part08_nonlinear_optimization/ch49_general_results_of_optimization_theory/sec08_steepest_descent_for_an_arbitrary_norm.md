# Hạ nhanh nhất (steepest descent) cho Tùy ý Chuẩn (norm)


<!-- PAGE 1735 -->
Một cái khác quy tắc cho chọn bước nhảy (stepsize) là Armijo’s quy tắc. các phương pháp này, và những cái khác, được thảo luận trong chi tiết trong Berstekas $[17]$. Boyd và Vandenberghe thảo luận hạ nhanh nhất (steepest descent) các phương pháp cho khác nhau các loại của các chuẩn ngoài ra Euclidean chuẩn (norm); xem Boyd và Vandenberghe $[29]$ (Mục 9.4). Ở đây là ngắn gọn tóm tắt.

## 49.8 Hạ nhanh nhất (steepest descent) cho Tùy ý Chuẩn (norm)

Ý tưởng là để tạo $\langle \nabla J_{uk}, d_{k}\rangle$ như âm như khả dĩ/có thể. để tạo câu hỏi sensible, ta có đến giới hạn kích thước của $d_{k}$ hoặc chuẩn hóa bởi độ dài của $d_{k}$. Cho $\|\|$ là bất kỳ chuẩn (norm) trên $\mathbb{R}^{n}$. Nhắc lại từ Mục 14.7 rằng đối ngẫu (dual) chuẩn (norm) được định nghĩa bởi
$$\|y\|^{D}= \sup|\langle x, y\rangle |.$$
$$x\in \mathbb{R} n$$
$$\|x\|=1$$

> **Định nghĩa 49.8.** được chuẩn hóa hạ nhanh nhất (steepest descent) hướng (đối với chuẩn (norm) $\|\|)$ là bất kỳ unit vectơ $d_{nsd,k}$ mà đạt được cực tiểu của tập hợp của các số thực
$${\langle \nabla J_{uk}, d\rangle | \|d\|= 1}.$$
Theo Định nghĩa, $\|d_{nsd,k}\| = 1$. chưa chuẩn hóa hạ nhanh nhất (steepest descent) hướng $d_{sd,k}$ được định nghĩa như
$$d_{sd,k} = \|\nabla J_{uk}\|^{D}d_{nsd,k}.$$
Nó có thể được được hiển thị rằng
$$\langle \nabla J_{uk}, d_{sd,k}\rangle = -(\|\nabla J_{uk}\|^{D})^{2};$$
Xem Boyd và Vandenberghe $[29]$ (Mục 9.4). hạ nhanh nhất (steepest descent) phương pháp (đối với chuẩn (norm) $\|\|)$ bao gồm của sau đây các bước: Cho trước bắt đầu điểm $u_{0} \in$ dom(J) thực hiện: repeat
$(1)$ Tính hạ nhanh nhất (steepest descent) hướng $d_{sd,k}$.
$(2)$ Đường thẳng search. Perform chính xác hoặc backtracking đường thẳng search để tìm $\rho_{k}$.
$(3)$ Update. $u_{k+1} = u_{k} + \rho_{k} d_{sd,k}$.

<!-- PAGE 1736 -->
Cho đến khi stopping tiêu chuẩn được thỏa mãn. Nếu $\|\|$ là $\ell^{2}$ -chuẩn (norm), thì ta xem ngay lập tức rằng $d_{sd,k} = -\nabla J_{uk}$, do đó trong trường hợp này phương pháp trùng với với hạ nhanh nhất (steepest descent) phương pháp cho Euclidean chuẩn (norm) như đã định nghĩa tại bắt đầu của Mục 49.6 trong $(3)$ và $(4)$. Nếu $P$ là đối xứng xác định dương (SPD) ma trận, nó là dễ để xem rằng $\|z\|_{P} = (z^{\top}Pz)^{1/2} = P^{1/2}z_{2}$ là chuẩn (norm). Thì nó có thể được được hiển thị rằng được chuẩn hóa hạ nhanh nhất (steepest descent) hướng là
$$d_{nsd,k} = -(\nabla J_{uk}^{\top}P^{-1}\nabla J_{uk})^{-1/2}P^{-1}\nabla J_{uk},$$
Đối ngẫu (dual) chuẩn (norm) là $\|z\|^{D} =$

$P^{-1/2}z_{2}$, và hạ nhanh nhất (steepest descent) hướng đối với $\|\|_{P}$ được cho bởi
$$d_{sd,k} = -P^{-1} \nabla J_{uk}.$$
Judicious lựa chọn cho $P$ có thể speed lên tốc độ của sự hội tụ của hạ gradien (gradient descent) phương pháp; xem xem Boyd và Vandenberghe $[29]$ (Mục 9.4.1 và Mục 9.4.4). Nếu $\|\|$ là $\ell^{1}$ -chuẩn (norm), thì nó có thể được được hiển thị rằng $d_{nsd,k}$ được xác định như sau: cho $i$ là bất kỳ chỉ số cho mà $\|\nabla J_{uk}\|_{\infty} = |(\nabla J_{uk})_{i}|$. Thì
$$d_{nsd,k} = -sign \begin{pmatrix} \partial J \\ (u_{k}) \\ \partial x_{i} \end{pmatrix} e_{i},$$
Ở đâu $e_{i}$ là vectơ cơ sở chính tắc thứ $i$, và
$$d_{sd,k} = - \frac{\partial J}{\partial x_{i}} (u_{k})e_{i}.$$
Cho nhiều hơn/thêm chi tiết, xem Boyd và Vandenberghe $[29]$ (Mục 9.4.2 và Mục 9.4.4). Nó cũng được hiển thị trong Boyd và Vandenberghe $[29]$ (Mục 9.4.3) rằng hạ nhanh nhất (steepest descent) phương pháp hội tụ với mọi chuẩn (norm) $\|\|$ và bất kỳ chặt hàm lồi (convex function) $J$. Một của chính các mục tiêu trong designing hạ gradien (gradient descent) phương pháp là để đảm bảo rằng sự hội tụ nhân tử là như nhỏ như khả dĩ/có thể, mà có nghĩa là phương pháp hội tụ như quickly như khả dĩ/có thể. Máy học (learning) có đã được catalyst cho việc tìm như vậy các phương pháp. phương pháp được thảo luận trong Strang $[177]$ (Chương VI, Mục $4)$ bao gồm trong cộng momentum số hạng đến gradien. Trong phương pháp này, $u_{k+1}$ và $d_{k+1}$ được xác định bởi sau đây hệ của các phương trình:
$$u_{k+1} = u_{k} -\rho d_{k}$$
$$d_{k+1} -\nabla J_{uk+1} = \beta d_{k}.$$
Của course mẹo/kỹ thuật là đến chọn $\rho$ và $\beta$ trong như vậy cách rằng sự hội tụ nhân tử là như nhỏ như khả dĩ/có thể. Nếu $J$ được cho bởi toàn phương phiếm hàm, nói $(1/2)u^{\top}Au$ - $b^{\top}u$, thì $\nabla J_{uk+1} = Au_{k+1}-b$ do đó ta thu được hệ phương trình tuyến tính. Hóa ra là tốc độ của sự hội tụ của
