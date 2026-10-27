# Thuật toán đơn hình (simplex algorithm) (Các trang 1605–1638)

## Các mục

- [The Idea Behind the Simplex Algorithm](sec01_the_idea_behind_the_simplex_algorithm.md) (pp. 1605–1613)
- [The Simplex Algorithm in General](sec02_the_simplex_algorithm_in_general.md) (pp. 1614–1620)
- [How to Perform a Pivoting Step Efficiently](sec03_how_to_perform_a_pivoting_step_efficient.md) (pp. 1621–1624)
- [The Simplex Algorithm Using Tableaux](sec04_the_simplex_algorithm_using_tableaux.md) (pp. 1625–1633)
- [Computational Efficiency of the Simplex Method](sec05_computational_efficiency_of_the_simplex_.md) (pp. 1634–1634)
- [Summary](sec06_summary.md) (pp. 1635–1635)
- [Problems](sec07_problems.md) (pp. 1635–1638)

## Các hình

- `fig_46_1.png` (Trang 1607): Hình 46.1: phẳng H-polyhedron liên kết với Ví dụ 46.2. ban đầu cơ bản nghiệm chấp nhận được (feasible solution) là gốc. thuật toán đơn hình (simplex algorithm) thứ nhất di chuyển dọc theo ngang cam đường thẳng đến nghiệm chấp nhận được (feasible solution) tại đỉnh u1. Nó thì di chuyển dọc theo đứng đỏ đường thẳng để thu được tối ưu nghiệm chấp nhận được (feasible solution) u2.
- `fig_46_2.png` (Trang 1610): Hình 46.2: phẳng H-polyhedron liên kết với Ví dụ 46.1. ban đầu cơ bản nghiệm chấp nhận được (feasible solution) là gốc. thuật toán đơn hình (simplex algorithm) di chuyển dọc theo slanted cam đường thẳng đến đỉnh của tam giác.
- `fig_46_3.png` (Trang 1613): Hình 46.3: phẳng H-polyhedron liên kết với Ví dụ 46.3. ban đầu cơ bản nghiệm chấp nhận được (feasible solution) là gốc. thuật toán đơn hình (simplex algorithm) thứ nhất di chuyển dọc theo ngang indigo đường thẳng đến cơ bản nghiệm chấp nhận được (feasible solution) tại đỉnh (1, 0). Bất kỳ tối ưu nghiệm chấp nhận được (feasible solution) xảy ra bởi di chuyển dọc theo biên (boundary) đường thẳng parameterized bởi cam arrow θ(1, 1).
- `fig_46_4.png` (Trang 1633): Hình 46.4: đa diện lồi hữu hạn (polytope) P liên kết với bài toán quy hoạch tuyến tính (linear program) optimized bởi bảng đơn hình (tableau) phương pháp. đỏ arrowed đường đi các vết (trace) progression của đơn hình (simplex) phương pháp từ gốc đến đỉnh (0, 1, 3).
