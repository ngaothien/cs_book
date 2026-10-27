# Giới thiệu đến Tối ưu hóa phi tuyến (nonlinear optimization) (Các trang 1763–1856)

## Các mục

- [The Cone of Feasible Directions](sec01_the_cone_of_feasible_directions.md) (pp. 1765–1770)
- [Active Constraints and Qualified Constraints](sec02_active_constraints_and_qualified_constra.md) (pp. 1771–1777)
- [The Karush–Kuhn–Tucker Conditions](sec03_the_karush_kuhn_tucker_conditions.md) (pp. 1778–1788)
- [Equality Constrained Minimization](sec04_equality_constrained_minimization.md) (pp. 1789–1793)
- [Hard Margin Support Vector Machine; Version I](sec05_hard_margin_support_vector_machine_versi.md) (pp. 1794–1798)
- [Hard Margin Support Vector Machine; Version II](sec06_hard_margin_support_vector_machine_versi.md) (pp. 1799–1806)
- [Lagrangian Duality and Saddle Points](sec07_lagrangian_duality_and_saddle_points.md) (pp. 1807–1815)
- [Weak and Strong Duality](sec08_weak_and_strong_duality.md) (pp. 1816–1824)
- [Handling Equality Constraints Explicitly](sec09_handling_equality_constraints_explicitly.md) (pp. 1825–1827)
- [Dual of the Hard Margin Support Vector Machine](sec10_dual_of_the_hard_margin_support_vector_m.md) (pp. 1828–1832)
- [Conjugate Function and Legendre Dual Function](sec11_conjugate_function_and_legendre_dual_fun.md) (pp. 1833–1842)
- [Some Techniques to Obtain a More Useful Dual Program](sec12_some_techniques_to_obtain_a_more_useful_.md) (pp. 1843–1846)
- [Uzawa's Method](sec13_uzawa_s_method.md) (pp. 1847–1851)
- [Summary](sec14_summary.md) (pp. 1852–1853)
- [Problems](sec15_problems.md) (pp. 1854–1856)

## Các hình

- `fig_50_1.png` (Trang 1766): Hình 50.1: Cho C là nón được xác định bởi bold cam đường cong qua (0, 0, 1) trong mặt phẳng z = 1. Thì u+C, ở đâu u = (0.25, 0.5, 0.5), là afin translate của C thông qua vectơ u.
- `fig_50_2.png` (Trang 1767): Hình 50.2: Cho U là hồng miền trong R2 với fuchsia điểm u ∈U. Với mọi dãy (uk)k≥0 của các điểm trong U mà hội tụ đến u, tạo thành chords uk −u và lấy giới hạn để xây dựng đỏ vectơ w.
- `fig_50_3.png` (Trang 1768): Hình 50.3: Cho U là tím miền trong R2 và u là designated điểm trên biên (boundary) của U. Hình (i.) minh họa hai các đường cong qua u và hai các dãy (uk)k≥0 hội tụ đến u. giới hạn của chords uk −u tương ứng với tiếp tuyến các vectơ cho thích hợp đường cong. Hình (ii.) minh họa một nửa mặt phẳng C(u) của chấp nhận được (feasible) các hướng.
- `fig_50_4.png` (Trang 1769): Hình 50.4: Hình (i.) minh họa U như shaded gray miền mà lies giữa đường thẳng y = −x và nodal bậc ba. Hình (ii.) chỉ ra nón của chấp nhận được (feasible) các hướng, C(0), như hợp của turquoise tam giác nón và turquoise directional tia (−1, 1).
- `fig_50_5.png` (Trang 1770): Hình 50.5: Cho U là mint xanh lục miền trong R2 với u = (0, 0). Cho (wn)n≥0 là dãy của các vectơ (các điểm) dọc theo trên dashed đường cong mà hội tụ đến w. Bởi sau đây dashed cam longitudinal các đường cong, và chọn thích hợp vectơ(điểm), ta xây dựng dark xanh lục đường cong trong U, mà các đi qua qua u, và tại u có tiếp tuyến vectơ tỷ lệ đến w.
- `fig_50_6.png` (Trang 1772): Hình 50.6: Cho U là light tím phẳng miền mà lies giữa các đường cong y = x2 và y2 = x. Hình (i.) minh họa biên (boundary) điểm (1, 1) cho trước bởi các đẳng thức y−x2 = 0 và y2−x = 0. afin translate của nón của chấp nhận được (feasible) các hướng, C(1, 1), được minh họa bởi hồng tam giác có các vế/cạnh là tiếp tuyến các đường thẳng đến biên (boundary) các đường cong. Hình (ii.) minh họa biên (boundary) điểm (1/4, 1/2) cho trước bởi đẳng thức y2 −x = 0. afin translate của C(1/4, 1/2) là lilac một nửa không gian bị chặn bởi tiếp tuyến đường thẳng đến y2 = x qua (1/4, 1/2).
- `fig_50_7.png` (Trang 1773): Hình 50.7: Cho u = (0, 0), C∗(u) là sea xanh lục một nửa không gian cho trước bởi u1 + u2 ≥0. Điều này một nửa không gian chặt chứa C(u), cụ thể là hợp của turquoise tam giác nón và directional tia (−1, 1).
- `fig_50_8.png` (Trang 1775): Hình 50.8: Các hình (i.) và (ii.) minh họa tím moon shaped miền liên kết với Ví dụ 50.2. Hình (i.) cũng minh họa C(0), nón của chấp nhận được (feasible) các hướng, trong khi Hình (ii.) minh họa chặt containment của C(0) trong C∗(0).
- `fig_50_9.png` (Trang 1776): Hình 50.9: Cho U là peach tam giác bị chặn bởi các đường thẳng y = 0, x = 0, và y = −x+1. Cho u thỏa mãn afin ràng buộc ϕ(x, y) = y + x −1. Vì ϕ′
- `fig_50_10.png` (Trang 1778): Hình 50.10: Cho U là hồng lounge trong R2. Cho u thỏa mãn non-affine ràng buộc ϕ1(u). Chọn các vectơ v và w trong một nửa không gian (ϕ′
- `fig_50_11.png` (Trang 1794): Hình 50.11: Hai các ví dụ của SVM separation bài toán. trái hình là SVM trong R2, trong khi phải hình là SVM trong R3.
- `fig_50_12.png` (Trang 1795): Hình 50.12: Hai các ví dụ trong mà nó là không thể để tìm tím các siêu phẳng mà tách đỏ và xanh lam các điểm.
- `fig_50_13.png` (Trang 1796): Hình 50.13: Trong R3, khoảng cách từ điểm đến mặt phẳng w⊤x −b = 0 được cho bởi phép chiếu lên chuẩn tắc/bình thường w.
- `fig_50_14.png` (Trang 1805): Hình 50.14: Trong R3, nghiệm đến Lề cứng (hard margin) SVMh2 là tím mặt phẳng sandwiched giữa đỏ mặt phẳng w⊤x −b + 1 = 0 và xanh lam mặt phẳng w⊤x −b −1 = 0, mỗi của mà chứa thích hợp hỗ trợ/giá (support) các vectơ ui và vj.
- `fig_50_15.png` (Trang 1806): Hình 50.15: tím đường thẳng, mà là đường phân giác của altitude của isosceles tam giác, tách hai đỏ các điểm từ xanh lam điểm trong cách thức mà thỏa mãn Lề cứng (hard margin) SVMh2.
- `fig_50_16.png` (Trang 1807): Hình 50.16: Trong R3, nghiệm đến Lề cứng (hard margin) SVMh2 cho các điểm u và v là tím vuông góc phẳng đường phân giác của u −v.
- `fig_50_17.png` (Trang 1809): Hình 50.17: ba chiều rendition của điểm yên ngựa (saddle point) L(u, λ) cho hàm L(u, λ) = u2 −λ2. mặt phẳng x = u cung cấp cực đại như đỉnh của downward mở parabol, trong khi mặt phẳng y = λ cung cấp cực tiểu như đỉnh của upward mở parabol.
- `fig_50_18.png` (Trang 1810): Hình 50.18: Cho Ω= {[t, 0, 0] | 0 ≤t ≤1} và M = {[0, t, 0] | 0 ≤t ≤1}. Trong Hình (i.), L(u, λ) là xanh lam slanted quadrilateral có forward đỉnh là điểm yên ngựa (saddle point). Trong Hình (ii.), L(u, λ) là phẳng xanh lục rectangle composed hoàn toàn của saddle các điểm.
- `fig_50_19.png` (Trang 1843): Hình 50.19: Trong R2 bao lồi (convex hull) của uis, cụ thể là xanh lam hexagon, được tách từ bao lồi (convex hull) của vjs, i.e. đỏ square, bởi tím siêu phẳng (hyperplane) (đường thẳng) mà là vuông góc đường phân giác đến xanh lam đường thẳng đoạn thẳng giữa ui và v1, ở đâu điều này xanh lam đường thẳng đoạn thẳng là ngắn nhất khoảng cách giữa hai lồi các đa giác.
