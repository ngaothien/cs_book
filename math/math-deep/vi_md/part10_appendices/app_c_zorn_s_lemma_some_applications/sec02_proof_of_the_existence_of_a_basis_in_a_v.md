# Chứng minh của Sự tồn tại của Cơ sở (basis) trong Không gian vectơ (vector space)


<!-- PAGE 2194 -->
Nhận xét: Như ta được lưu ý, giả thiết của Zorn’s bổ đề suy ra rằng $S$ là khác rỗng (vì rỗng tập hợp phải là bị chặn). một cách riêng được thứ tự tập hợp sao cho mọi dây chuyền/xích là bị chặn đôi khi được gọi là quy nạp. Ta bây giờ cho một số các ứng dụng của Zorn’s bổ đề.

## C.2 Chứng minh của Sự tồn tại của Cơ sở (basis) trong Không gian vectơ (vector space)

Bằng cách sử dụng Zorn’s bổ đề, ta có thể chứng minh rằng Định lý 3.8 nghiệm đúng cho tùy ý các không gian vectơ, và không chỉ cho sinh hữu hạn (finitely generated) các không gian vectơ, như promised trong Chương $3$.

> **Định lý C.2.** Cho trước bất kỳ họ, $S = (u_{i})_{i\in I}$, sinh không gian vectơ (vector space) $E$ và bất kỳ độc lập tuyến tính (linearly independent) họ con, $L = (u_{j})_{j\in J}$, của $S$ (ở đâu $J \subseteq$ I), có một cơ sở (basis), $B$, của $E$ sao cho $L \subseteq B \subseteq S$.

*Chứng minh.* Xét tập hợp $\mathcal{L}$ của độc lập tuyến tính (linearly independent) các họ, $B$, sao cho $L \subseteq B \subseteq S$. Vì $L \in L$, tập hợp này là khác rỗng. Ta khẳng định rằng $\mathcal{L}$ là quy nạp. Xét bất kỳ dây chuyền/xích, $(B_{l})_{l\in\Lambda}$, của
$$linearly independent families B_{l} in\mathcal{L}, and look at B = \bigcup_{l}  \in  B_{l}. The family B is of the form$$
$B = (v_{h})_{h\in H}$, với một số chỉ số tập hợp $H$, và nó phải là $linearly^{\Lambda}$ độc lập. Thật vậy, nếu điều này đã là không đúng, ở đó sẽ là một số họ $(\lambda_{h} )_{h\in H}$ của các vô hướng, của hữu hạn hỗ trợ/giá (support), sao cho
$$\sum_{h\in H}  \lambda_{h} v_{h} = 0,$$
$$where not all \lambda_{h}  are zero. Since B = \bigcup_{l}  B_{l} and only finitely many \lambda_{h}  are nonzero, there$$
Là hữu hạn tập con, $F$, của $\Lambda$, sao cho $v_{h} \in^{\in\Lambda} B_{fh}$ khi và chỉ khi $\lambda_{h}  \neq  0$. Nhưng $(B_{l})_{l\in\Lambda}$ là dây chuyền/xích, và nếu ta cho $f = max{f_{h}$ | $f_{h} \in F}$, thì $v_{h} \in B_{f}$, với mọi $v_{h}$ cho mà $\lambda_{h}  \neq  0$. Do đó,
$$\sum_{h\in H}  \lambda_{h} v_{h} = 0$$
Sẽ là không tầm thường tuyến tính dependency trong số các vectơ từ $B_{f}$, một mâu thuẫn. Vì vậy, $B \in L$, và vì $B$ là hiển nhiên trên cận cho $B_{l}’s$, ta có được chứng minh rằng $\mathcal{L}$ là quy nạp. Bởi Zorn’s bổ đề (Bổ đề C.1), tập hợp $\mathcal{L}$ có một số cực đại phần tử, nói $B = (u_{h})_{h\in H}$. rest của chứng minh là cùng như trong chứng minh của Định lý 3.8, nhưng ta repeat nó cho độc giả’s convenience. Ta khẳng định rằng $B$ sinh ra $E$. Thật vậy, nếu $B$ thực hiện không sinh $E$, thì tồn tại một $u_{p} \in S$ rằng là không tổ hợp tuyến tính (linear combination) của các vectơ trong $B$ (vì $S$ sinh ra $E)$, với $p \in / H$. Thì, theo Bổ đề 3.7, họ B' $= (u_{h})_{h\in H\cup {p}}$ là độc lập tuyến tính (linearly independent), và vì $L \subseteq B \subset$ B' $\subseteq S$, điều này contradicts maximality của $B$. Do đó, $B$ là cơ sở (basis) của $E$ sao cho $L \subseteq B \subseteq S$. Một cái khác quan trọng ứng dụng của Zorn’s bổ đề là sự tồn tại của cực đại các lý tưởng.
