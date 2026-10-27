# Subgradients and Subdifferentials  (Pages 1857–1902)

## Sections

- [Extended Real-Valued Convex Functions](sec01_extended_real_valued_convex_functions.md) (pp. 1859–1867)
- [Subgradients and Subdifferentials](sec02_subgradients_and_subdifferentials.md) (pp. 1868–1879)
- [Basic Properties of Subgradients and Subdifferentials](sec03_basic_properties_of_subgradients_and_sub.md) (pp. 1880–1885)
- [Additional Properties of Subdifferentials](sec04_additional_properties_of_subdifferential.md) (pp. 1886–1889)
- [The Minimum of a Proper Convex Function](sec05_the_minimum_of_a_proper_convex_function.md) (pp. 1890–1896)
- [Generalization of the Lagrangian Framework](sec06_generalization_of_the_lagrangian_framewo.md) (pp. 1897–1899)
- [Summary](sec07_summary.md) (pp. 1900–1901)
- [Problems](sec08_problems.md) (pp. 1902–1902)

## Figures

- `fig_51_1.png` (Page 1860): Figure 51.1: Let f : R →R ∪{−∞, +∞} be given by f(x) = x3 for x ∈R. Its graph in R2
- `fig_51_2.png` (Page 1861): Figure 51.2: Let f : R →R ∪{−∞, +∞} be given by f(x) = x2 for x ∈R. Its graph in R2
- `fig_51_3.png` (Page 1862): Figure 51.3: The epigraph of the concave function f(x) = −x2 if x ≥0 and +∞otherwise.
- `fig_51_4.png` (Page 1863): Figure 51.4: The improper convex function of Example 51.2 and its epigraph depicted as a rose colored region of R2.
- `fig_51_5.png` (Page 1866): Figure 51.5: The proper convex function of Example 51.3 and its closure. These two functions only differ at the relative boundary point of dom(f), namely x = 1.
- `fig_51_6.png` (Page 1867): Figure 51.6: The proper convex function of Example 51.4. When intersected by vertical planes of the form x = α, for α > 0, the trace is an upward parabola. When α is close to zero, this parabola approximates the positive z axis.
- `fig_51_7.png` (Page 1868): Figure 51.7: Figure (a) illustrates the proper convex function of Example 51.4. Figure (b) illustrates the approach to (0, 0) along the planar parabolic curve (y2/2, y). Then f(y2/2, y) = 1 and Figure b shows the intersection of the surface with the plane z = 1.
- `fig_51_8.png` (Page 1870): Figure 51.8: The affine hyperplane H = {x ∈R3 | x + y + z −2 = 0}. The half space H+ faces the viewer and contains the point (0, 0, 10), while the half space H−is behind H and contains the point (0, 0, 0).
- `fig_51_9.png` (Page 1871): Figure 51.9: Let ϕ: R →R be the affine form ϕ(x) = x + 1. Let ω: R2 →R be the affine form ω(x, α) = x + 1 −α. The hyperplane H = ω−1(0) is the red line with equation x −α + 1 = 0.
- `fig_51_10.png` (Page 1872): Figure 51.10: Let C be the solid peach tetrahedron in R3. The green plane H is a supporting hyperplane to the point x since x ∈H and C ⊆H+, i.e. H only intersects C on the edge containing x and so the tetrahedron lies in “front” of H.
- `fig_51_11.png` (Page 1873): Figure 51.11: Let C be the solid peach tetrahedron in R3. The small upside-down magenta tetrahedron is the translate of NC(a). Figure (a) shows that the normal cone is separated from C by the horizontal green supporting hyperplane. Figure (b) shows that any vector u ∈NC(a) does not make an acute angle with a line segment in C emanating from a.
- `fig_51_12.png` (Page 1874): Figure 51.12: Let C be the solid peach tetrahedron in R3. The green plane H defined by ϕ(z) = ⟨z, u⟩−c is a supporting hyperplane to C at a. The pink normal to H, namely the vector u, is also normal to C at a.
- `fig_51_13.png` (Page 1875): Figure 51.13: Let f : R →R∪{−∞, +∞} be the piecewise function defined by f(x) = x+1 for x ≥1 and f(x) = −1
- `fig_51_14.png` (Page 1876): Figure 51.14: Figure (1) shows the graph in R3 of f(x, y) = ∥(x, y)∥2 =
- `fig_51_15.png` (Page 1877): Figure 51.15: Figure (1) shows the graph in R3 of f(x, y) = ∥(x, y)∥∞= sup{|x|, |y|}. Figure (2) shows the supporting hyperplane with normal (1
- `fig_51_16.png` (Page 1878): Figure 51.16: The graph of the function in Example 51.7.
- `fig_51_17.png` (Page 1879): Figure 51.17: Figure (1) illustrates epi(f), where epi(f) is contained in a vertical plane of affine dimension 2. Figure (2) illustrates the magenta open subset {(x, µ) ∈R2 | x ∈ int(P), α < µ} of epi(f). Figure (3) illustrates the vertical line segment {(z, µ) ∈R2 | f(z) ≤µ ≤α + β + 1}.
- `fig_51_18.png` (Page 1880): Figure 51.18: The graph of the partial function f(x) = −√x and its red vertical supporting hyperplane at x = 0.
- `fig_51_19.png` (Page 1881): Figure 51.19: Let f : R2 →R∪{−∞, +∞} be the function whose graph (in R3) is the surface of the peach pyramid. The top figure illustrates that f ′(x; u) is the slope of the slanted burnt orange line, while the bottom figure depicts the line associated with limλ↑0
- `fig_51_20.png` (Page 1883): Figure 51.20: The graph of the ReLU function.
- `fig_51_21.png` (Page 1885): Figure 51.21: The graph of the function from Example 51.11 with a view along the positive x axis.
- `fig_51_22.png` (Page 1887): Figure 51.22: Let f be the proper convex function whose graph in R3 is the peach polyhedral surface. The sublevel set C = {z ∈R2 | f(z) ≤f(x)} is the orange square which is closed on three sides. Then the normal cone NC(x) is the closure of the convex cone spanned by ∂f(x).
- `fig_51_23.png` (Page 1889): Figure 51.23: Let f : R →R∪{−∞, +∞} be the piecewise function defined by f(x) = x+1 for x ≥1 and f(x) = −1
- `fig_51_24.png` (Page 1891): Figure 51.24: Let f be the proper convex function whose graph is the surface of the upward facing pink trough. The minimum set of f is the light pink square of R2 which maps to the bottom surface of the trough in R3. For any x in the minimum set, f ′(x; y) ≥0, a fact substantiated by Proposition 51.34.
- `fig_51_25.png` (Page 1893): Figure 51.25: The graphs of the two functions discussed in Example 51.12. The graph of f(x, y) = 2x+y2 slopes ”downward” along the negative x-axis, reflecting the fact that (−u, 0) is a direction of recession.
- `fig_51_26.png` (Page 1894): Figure 51.26: The graph of the partial function f(x) = 1 x for x > 0. The graph of this function decreases along the x-axis since 1 is a direction of recession.
