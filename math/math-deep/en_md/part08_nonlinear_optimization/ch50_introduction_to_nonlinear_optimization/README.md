# Introduction to Nonlinear Optimization (Pages 1763–1856)

## Sections

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

## Figures

- `fig_50_1.png` (Page 1766): Figure 50.1: Let C be the cone determined by the bold orange curve through (0, 0, 1) in the plane z = 1. Then u+C, where u = (0.25, 0.5, 0.5), is the affine translate of C via the vector u.
- `fig_50_2.png` (Page 1767): Figure 50.2: Let U be the pink region in R2 with fuchsia point u ∈U. For any sequence (uk)k≥0 of points in U which converges to u, form the chords uk −u and take the limit to construct the red vector w.
- `fig_50_3.png` (Page 1768): Figure 50.3: Let U be purple region in R2 and u be the designated point on the boundary of U. Figure (i.) illustrates two curves through u and two sequences (uk)k≥0 converging to u. The limit of the chords uk −u corresponds to the tangent vectors for the appropriate curve. Figure (ii.) illustrates the half plane C(u) of feasible directions.
- `fig_50_4.png` (Page 1769): Figure 50.4: Figure (i.) illustrates U as the shaded gray region which lies between the line y = −x and nodal cubic. Figure (ii.) shows the cone of feasible directions, C(0), as the union of the turquoise triangular cone and the turquoise directional ray (−1, 1).
- `fig_50_5.png` (Page 1770): Figure 50.5: Let U be the mint green region in R2 with u = (0, 0). Let (wn)n≥0 be a sequence of vectors (points) along the upper dashed curve which converge to w. By following the dashed orange longitudinal curves, and selecting an appropriate vector(point), we construct the dark green curve in U, which passes through u, and at u has tangent vector proportional to w.
- `fig_50_6.png` (Page 1772): Figure 50.6: Let U be the light purple planar region which lies between the curves y = x2 and y2 = x. Figure (i.) illustrates the boundary point (1, 1) given by the equalities y−x2 = 0 and y2−x = 0. The affine translate of cone of feasible directions, C(1, 1), is illustrated by the pink triangle whose sides are the tangent lines to the boundary curves. Figure (ii.) illustrates the boundary point (1/4, 1/2) given by the equality y2 −x = 0. The affine translate of C(1/4, 1/2) is the lilac half space bounded by the tangent line to y2 = x through (1/4, 1/2).
- `fig_50_7.png` (Page 1773): Figure 50.7: For u = (0, 0), C∗(u) is the sea green half space given by u1 + u2 ≥0. This half space strictly contains C(u), namely the union of the turquoise triangular cone and the directional ray (−1, 1).
- `fig_50_8.png` (Page 1775): Figure 50.8: Figures (i.) and (ii.) illustrate the purple moon shaped region associated with Example 50.2. Figure (i.) also illustrates C(0), the cone of feasible directions, while Figure (ii.) illustrates the strict containment of C(0) in C∗(0).
- `fig_50_9.png` (Page 1776): Figure 50.9: Let U be the peach triangle bounded by the lines y = 0, x = 0, and y = −x+1. Let u satisfy the affine constraint ϕ(x, y) = y + x −1. Since ϕ′
- `fig_50_10.png` (Page 1778): Figure 50.10: Let U be the pink lounge in R2. Let u satisfy the non-affine constraint ϕ1(u). Choose vectors v and w in the half space (ϕ′
- `fig_50_11.png` (Page 1794): Figure 50.11: Two examples of the SVM separation problem. The left figure is SVM in R2, while the right figure is SVM in R3.
- `fig_50_12.png` (Page 1795): Figure 50.12: Two examples in which it is impossible to find purple hyperplanes which separate the red and blue points.
- `fig_50_13.png` (Page 1796): Figure 50.13: In R3, the distance from a point to the plane w⊤x −b = 0 is given by the projection onto the normal w.
- `fig_50_14.png` (Page 1805): Figure 50.14: In R3, the solution to Hard Margin SVMh2 is the purple plane sandwiched between the red plane w⊤x −b + 1 = 0 and the blue plane w⊤x −b −1 = 0, each of which contains the appropriate support vectors ui and vj.
- `fig_50_15.png` (Page 1806): Figure 50.15: The purple line, which is the bisector of the altitude of the isosceles triangle, separates the two red points from the blue point in a manner which satisfies Hard Margin SVMh2.
- `fig_50_16.png` (Page 1807): Figure 50.16: In R3, the solution to Hard Margin SVMh2 for the points u and v is the purple perpendicular planar bisector of u −v.
- `fig_50_17.png` (Page 1809): Figure 50.17: A three-dimensional rendition of a saddle point L(u, λ) for the function L(u, λ) = u2 −λ2. The plane x = u provides a maximum as the apex of a downward opening parabola, while the plane y = λ provides a minimum as the apex of an upward opening parabola.
- `fig_50_18.png` (Page 1810): Figure 50.18: Let Ω= {[t, 0, 0] | 0 ≤t ≤1} and M = {[0, t, 0] | 0 ≤t ≤1}. In Figure (i.), L(u, λ) is the blue slanted quadrilateral whose forward vertex is a saddle point. In Figure (ii.), L(u, λ) is the planar green rectangle composed entirely of saddle points.
- `fig_50_19.png` (Page 1843): Figure 50.19: In R2 the convex hull of the uis, namely the blue hexagon, is separated from the convex hull of the vjs, i.e. the red square, by the purple hyperplane (line) which is the perpendicular bisector to the blue line segment between ui and v1, where this blue line segment is the shortest distance between the two convex polygons.
