# Tóm tắt


<!-- PAGE 1852 -->
Trong trường hợp đặc biệt khi $J$ là elliptic toàn phương phiếm hàm
$$J(v) = \frac{1}{2} \langle Av, v\rangle -\langle b, v\rangle ,$$
Ở đâu $A$ là đối xứng xác định dương (SPD), bởi $(\dagger_{2}$) vòng lặp của Uzawa’s phương pháp cho
$$Au^{k}-b + C^{\top}\lambda^{k} = 0$$
$$\lambda_{i}^{k+1} = \max{(\lambda^{k} + \rho (Cu^{k}-d))_{i}, 0},1 \le i \le m.$$
Định lý 50.21 suy ra rằng Uzawa’s phương pháp hội tụ nếu
$$0 < \rho  < \frac{2\lambda_{1}}{\|C\|_{2}^{2}} ,$$
Ở đâu $\lambda_{1}$ là nhỏ nhất trị riêng (eigenvalue) của $A$. Nếu ta giải cho $u^{k}$ bằng cách sử dụng phương trình thứ nhất, ta thu được
$$\lambda^{k+1} = p_{+}(\lambda^{k} + \rho (-CA^{-1}C^{\top}\lambda^{k} + CA^{-1}b -d)).(*_{7})$$
Trong Ví dụ 50.7 ta đã chỉ ra rằng gradien của đối ngẫu (dual) hàm $G$ được cho bởi
$$\nabla G_{\mu} = Cu_{\mu} -d = -CA^{-1}C^{\top}\mu  + CA^{-1}b -d,$$
Do đó $(*_{7})$ có thể được viết dưới dạng
$$\lambda^{k+1} = p_{+}(\lambda^{k} + \rho \nabla G_{\lambda k});$$
Điều này chỉ ra rằng Uzawa’s phương pháp là thật vậy gradien phương pháp với cố định bước nhảy (stepsize) ứng dụng đến đối ngẫu (dual) bài toán quy hoạch.

## 50.14 Tóm tắt

Chính các khái niệm và các kết quả của điều này chương được liệt kê ở dưới: $\bullet$ nón của chấp nhận được (feasible) các hướng. $\bullet$ Nón với đỉnh. $\bullet$ Hoạt động và không hoạt động các ràng buộc. $\bullet$ Qualified ràng buộc tại $u. \bullet$ Farkas bổ đề. $\bullet$ Farkas–Minkowski bổ đề. $\bullet$ Karush–Kuhn–Tucker tính tối ưu các điều kiện (hoặc KKT-conditions).

<!-- PAGE 1853 -->
$\bullet$ Độ bù lỏng (complementary slackness) các điều kiện. $\bullet$ Suy rộng/tổng quát hóa Các nhân tử Lagrange (Lagrange multipliers). $\bullet$ Qualified lồi ràng buộc. $\bullet$ Hàm Lagrange (Lagrangian) của cực tiểu hóa bài toán. $\bullet$ Đẳng thức có ràng buộc cực tiểu hóa. $\bullet$ KKT ma trận. $\bullet$ Newton’s phương pháp với đẳng thức các ràng buộc (chấp nhận được (feasible) bắt đầu và infeasible bắt đầu). $\bullet$ Lề cứng (hard margin) máy vectơ hỗ trợ (SVM) $\bullet$ Huấn luyện (training) dữ liệu $\bullet$ một cách tuyến tính khả ly các tập hợp của các điểm. $\bullet$ Cực đại lề (margin) siêu phẳng (hyperplane). $\bullet$ Hỗ trợ/giá (support) các vectơ $\bullet$ Saddle các điểm. $\bullet$ Lagrange đối ngẫu (dual) hàm. $\bullet$ Lagrange đối ngẫu (dual) bài toán quy hoạch. $\bullet$ Khoảng cách đối ngẫu (duality gap). $\bullet$ Đối ngẫu yếu (weak duality). $\bullet$ Đối ngẫu mạnh (strong duality). $\bullet$ Handling đẳng thức các ràng buộc trong Hàm Lagrange (Lagrangian). $\bullet$ Đối ngẫu (dual) của Lề cứng (hard margin) SVM $(SVM_{h2}). \bullet$ Liên hợp các hàm và Legendre đối ngẫu (dual) các hàm. $\bullet$ Đối ngẫu (dual) của Lề cứng (hard margin) SVM $(SVM_{h1}). \bullet$ Uzawa’s Phương pháp.
