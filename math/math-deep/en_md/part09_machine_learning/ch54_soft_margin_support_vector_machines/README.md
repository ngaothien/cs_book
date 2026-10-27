# Soft Margin Support Vector Machines (Pages 1967–2070)

## Sections

- [Soft Margin Support Vector Machines; (SVMs1)](sec01_soft_margin_support_vector_machines_svms.md) (pp. 1970–1984)
- [Solving SVM (SVMs1) Using ADMM](sec02_solving_svm_svms1_using_admm.md) (pp. 1985–1985)
- [Soft Margin Support Vector Machines; (SVMs2)](sec03_soft_margin_support_vector_machines_svms.md) (pp. 1986–1992)
- [Solving SVM (SVMs2) Using ADMM](sec04_solving_svm_svms2_using_admm.md) (pp. 1993–1993)
- [Soft Margin Support Vector Machines; (SVMs2')](sec05_soft_margin_support_vector_machines_svms.md) (pp. 1994–2004)
- [Classification of the Data Points in Terms of  (SVMs2')](sec06_classification_of_the_data_points_in_ter.md) (pp. 2005–2007)
- [Existence of Support Vectors for (SVMs2')](sec07_existence_of_support_vectors_for_svms2.md) (pp. 2008–2017)
- [Solving SVM (SVMs2') Using ADMM](sec08_solving_svm_svms2_using_admm.md) (pp. 2018–2021)
- [Soft Margin Support Vector Machines; (SVMs3)](sec09_soft_margin_support_vector_machines_svms.md) (pp. 2022–2028)
- [Classification of the Data Points in Terms of  (SVMs3)](sec10_classification_of_the_data_points_in_ter.md) (pp. 2029–2030)
- [Existence of Support Vectors for (SVMs3)](sec11_existence_of_support_vectors_for_svms3.md) (pp. 2031–2032)
- [Solving SVM (SVMs3) Using ADMM](sec12_solving_svm_svms3_using_admm.md) (pp. 2033–2036)
- [Soft Margin SVM; (SVMs4)](sec13_soft_margin_svm_svms4.md) (pp. 2037–2044)
- [Solving SVM (SVMs4) Using ADMM](sec14_solving_svm_svms4_using_admm.md) (pp. 2045–2046)
- [Soft Margin SVM; (SVMs5)](sec15_soft_margin_svm_svms5.md) (pp. 2047–2050)
- [Solving SVM (SVMs5) Using ADMM](sec16_solving_svm_svms5_using_admm.md) (pp. 2051–2052)
- [Summary and Comparison of the SVM Methods](sec17_summary_and_comparison_of_the_svm_method.md) (pp. 2053–2065)
- [Problems](sec18_problems.md) (pp. 2066–2070)

## Figures

- `fig_54_1.png` (Page 1967): Figure 54.1: Two examples of the SVM separation problem. The left figure is SVM in R2, while the right figure is SVM in R3.
- `fig_54_2.png` (Page 1971): Figure 54.2: The blue margin half space associated with w⊤x −b −δ = 0.
- `fig_54_3.png` (Page 1972): Figure 54.3: The red margin half space associated with w⊤x −b + δ = 0.
- `fig_54_4.png` (Page 1978): Figure 54.4: When 0 < λi < K, ui is contained within the blue margin hyperplane. When 0 < µj < K, vj is contained within the red margin hyperplane.
- `fig_54_5.png` (Page 1979): Figure 54.5: Figure (1) illustrates the case of ui contained in the margin and occurs when ϵi = 0. Figure (1) also illustrates the case of vj contained in the margin when ξj = 0. The left illustration of Figure (2) is when ui is inside the margin yet still on the correct side of the separating hyperplane w⊤x −b = 0. Similarly, vj is inside the margin on the correct side of the separating hyperplane. The right illustration depicts ui and vj on the separating hyperplane. Figure (3) illustrations a misclassification of ui and vj.
- `fig_54_6.png` (Page 1980): Figure 54.6: When λi = 0, ui is correctly classified outside the blue margin. When µj = 0, vj is correctly classified outside the red margin.
- `fig_54_7.png` (Page 2009): Figure 54.7: In this illustration points with errors are denoted by open circles. In the original, upper left configuration, there is no blue support vector. By raising the pink separating hyperplane and increasing the margin, we end up with a blue support vector.
- `fig_54_8.png` (Page 2011): Figure 54.8: In this illustration points with errors are denoted by open circles. In the original, upper left configuration, there is no blue support vector and no red support vector. By increasing the margin, we end up with a red support vector and reduce to Case 1a.
- `fig_54_9.png` (Page 2012): Figure 54.9: In this illustration points with errors are denoted by open circles. In the original, upper left configuration, there is no blue support vector and no red support vector. By increasing the margin, we end up with a blue support vector and reduce to Case 2a.
- `fig_54_10.png` (Page 2013): Figure 54.10: In this illustration points with errors are denoted by open circles. In the original, upper left configuration, there is no red support vector. By lowering the pink separating hyperplane and increasing the margin, we end up with a red support vector.
- `fig_54_11.png` (Page 2021): Figure 54.11: Running (SVMs2′) on two sets of 30 points; ν = 0.37.
- `fig_54_13.png` (Page 2021): Figure 54.13: Running (SVMs2′) on two sets of 30 points; ν = 0.71.
- `fig_54_12.png` (Page 2022): Figure 54.12: Running (SVMs2′) on two sets of 30 points; ν = 0.51.
- `fig_54_14.png` (Page 2023): Figure 54.14: Running (SVMs2′) on two sets of 30 points; ν = 0.95.
- `fig_54_15.png` (Page 2024): Figure 54.15: Running (SVMs2′) on two sets of 30 points; ν = 0.97.
- `fig_54_16.png` (Page 2034): Figure 54.16: Running (SVMs3) on two sets of 30 points; ν = 0.365.
- `fig_54_17.png` (Page 2035): Figure 54.17: Running (SVMs3) on two sets of 30 points; ν = 0.5.
- `fig_54_18.png` (Page 2036): Figure 54.18: Running (SVMs3) on two sets of 30 points; ν = 0.71.
- `fig_54_19.png` (Page 2036): Figure 54.19: Running (SVMs3) on two sets of 30 points; ν = 0.98.
- `fig_54_20.png` (Page 2040): Figure 54.20: When λi = 0, ui is correctly classified on or outside the blue margin. When µj = 0, vj is correctly classified on or outside outside the red margin.
- `fig_54_21.png` (Page 2041): Figure 54.21: The classification of points for SVMs4 when the Lagrange multipliers are positive. The left illustration of Figure (1) is when ui is inside the margin yet still on the correct side of the separating hyperplane w⊤x −b = 0. Similarly, vj is inside the margin on the correct side of the separating hyperplane. The right illustration depicts ui and vj on the separating hyperplane. Figure (2) illustrations a misclassification of ui and vj.
- `fig_54_22.png` (Page 2047): Figure 54.22: Running (SVMs4) on two sets of 30 points; K = 190.
- `fig_54_23.png` (Page 2048): Figure 54.23: Running (SVMs4) on two sets of 30 points; K = 1/12000.
- `fig_54_24.png` (Page 2052): Figure 54.24: Running (SVMs5) on two sets of 30 points; K = 190.
- `fig_54_25.png` (Page 2053): Figure 54.25: Running (SVMs5) on two sets of 30 points; K = 1/13000.
