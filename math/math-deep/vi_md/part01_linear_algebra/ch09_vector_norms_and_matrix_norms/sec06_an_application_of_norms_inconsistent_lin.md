# Ứng dụng của Các chuẩn: Vô nghiệm/không tương thích Các hệ phương trình tuyến tính


<!-- PAGE 373 -->

## 9.6 Ứng dụng của Các chuẩn: Việc giải Vô nghiệm/không tương thích

$$Linear Systems$$
Bài toán của việc giải vô nghiệm/không tương thích hệ phương trình tuyến tính Ax $= b$ thường phát sinh trong thực tế. Điều này là hệ ở đâu $b$ thực hiện không thuộc đến cột không gian của $A$, thường với nhiều hơn/thêm các phương trình hơn các biến. Do đó, như vậy hệ có không có nghiệm. Vẫn chưa ta sẽ vẫn like đến “giải” như vậy hệ, ít nhất một cách xấp xỉ. Như vậy các hệ thường phát sinh khi cố gắng đến fit một số dữ liệu. Ví dụ, ta có thể có tập hợp của 3D dữ liệu các điểm
$${p_{1}, \dots  , p_{n}},$$
Và ta có lý do đến tin rằng các phần tử này các điểm là gần như đồng phẳng. Ta sẽ like để tìm mặt phẳng rằng tốt nhất fits của ta dữ liệu các điểm. Nhắc lại rằng phương trình của mặt phẳng là
$$\alpha x + \beta y + \gamma z + \delta  = 0,$$
Với $(\alpha , \beta , \gamma$) $\neq  (0, 0, 0)$. Do đó, mọi mặt phẳng là hoặc không song song đến trục $x$ $(\alpha  \neq  0)$ hoặc không song song đến trục $y$ $(\beta  \neq  0)$ hoặc không song song đến trục $z$ $(\gamma  \neq  0)$. Nói ta có các lý do đến tin rằng mặt phẳng ta là nhìn cho là không song song đến trục $z$. Nếu ta là sai, trong bình phương tối thiểu (least squares) nghiệm, một của các hệ số, $\alpha , \beta$, sẽ là rất lớn. Nếu $\gamma  \neq  0$, thì ta có thể giả sử rằng của ta mặt phẳng được cho bởi phương trình của tạo thành
$$z = ax + by + d,$$
Và ta sẽ like phương trình này được thỏa mãn với mọi $p_{i}’s$, mà dẫn đến đến hệ của $n$ các phương trình trong $3$ unknowns, $b, d$, với $p_{i} = (x_{i}, y_{i}, z_{i})$;
$$ax_{1} + by_{1} + d = z_{1}$$
$$\vdots \vdots$$
$$ax_{n} + by_{n} + d = z_{n}.$$
Tuy nhiên, nếu $n$ là lớn hơn hơn $3$, như vậy hệ một cách tổng quát có không có nghiệm. Vì ở trên hệ có thể’t được giải chính xác, ta có thể thử để tìm nghiệm (, $b, d)$ rằng cực tiểu hóa bình phương tối thiểu (least-squares) sai số
$$\sum_{i=1}^{n}  (ax_{i} + by_{i} + d -z_{i})^{2}.$$
Điều này là những gì Legendre và Gauss figured ra trong early 1800’s! Nói chung, cho trước hệ phương trình tuyến tính
$$Ax = b,$$
Ta giải bình phương tối thiểu (least squares) bài toán: cực tiểu hóa $\|Ax$ - $b\|_{2}^{2}$.
