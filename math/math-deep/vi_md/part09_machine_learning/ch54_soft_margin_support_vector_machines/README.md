# Lề mềm (soft margin) Các máy vectơ hỗ trợ (SVMs) (Các trang 1967–2070)

## Các mục

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

## Các hình

- `fig_54_1.png` (Trang 1967): Hình 54.1: Hai các ví dụ của SVM separation bài toán. trái hình là SVM trong R2, trong khi phải hình là SVM trong R3.
- `fig_54_2.png` (Trang 1971): Hình 54.2: xanh lam lề (margin) một nửa không gian liên kết với w⊤x −b −δ = 0.
- `fig_54_3.png` (Trang 1972): Hình 54.3: đỏ lề (margin) một nửa không gian liên kết với w⊤x −b + δ = 0.
- `fig_54_4.png` (Trang 1978): Hình 54.4: Khi 0 < λi < K, ui được chứa trong phạm vi xanh lam lề (margin) siêu phẳng (hyperplane). Khi 0 < µj < K, vj được chứa trong phạm vi đỏ lề (margin) siêu phẳng (hyperplane).
- `fig_54_5.png` (Trang 1979): Hình 54.5: Hình (1) minh họa trường hợp của ui được chứa trong lề (margin) và xảy ra khi ϵi = 0. Hình (1) cũng minh họa trường hợp của vj được chứa trong lề (margin) khi ξj = 0. trái illustration của Hình (2) là khi ui là bên trong lề (margin) vẫn chưa vẫn trên đúng vế/cạnh của tách siêu phẳng (hyperplane) w⊤x −b = 0. Tương tự, vj là bên trong lề (margin) trên đúng vế/cạnh của tách siêu phẳng (hyperplane). phải illustration depicts ui và vj trên tách siêu phẳng (hyperplane). Hình (3) illustrations misclassification của ui và vj.
- `fig_54_6.png` (Trang 1980): Hình 54.6: Khi λi = 0, ui là một cách chính xác được phân loại bên ngoài xanh lam lề (margin). Khi µj = 0, vj là một cách chính xác được phân loại bên ngoài đỏ lề (margin).
- `fig_54_7.png` (Trang 2009): Hình 54.7: Trong điều này illustration các điểm với các sai số được ký hiệu bởi mở các đường tròn. Trong ban đầu, trên trái configuration, không có xanh lam hỗ trợ/giá (support) vectơ. Bởi raising hồng tách siêu phẳng (hyperplane) và tăng lề (margin), ta kết thúc/cuối lên với xanh lam hỗ trợ/giá (support) vectơ.
- `fig_54_8.png` (Trang 2011): Hình 54.8: Trong điều này illustration các điểm với các sai số được ký hiệu bởi mở các đường tròn. Trong ban đầu, trên trái configuration, không có xanh lam hỗ trợ/giá (support) vectơ và không có đỏ hỗ trợ/giá (support) vectơ. Bởi tăng lề (margin), ta kết thúc/cuối lên với đỏ hỗ trợ/giá (support) vectơ và rút gọn đến Trường hợp 1a.
- `fig_54_9.png` (Trang 2012): Hình 54.9: Trong điều này illustration các điểm với các sai số được ký hiệu bởi mở các đường tròn. Trong ban đầu, trên trái configuration, không có xanh lam hỗ trợ/giá (support) vectơ và không có đỏ hỗ trợ/giá (support) vectơ. Bởi tăng lề (margin), ta kết thúc/cuối lên với xanh lam hỗ trợ/giá (support) vectơ và rút gọn đến Trường hợp 2a.
- `fig_54_10.png` (Trang 2013): Hình 54.10: Trong điều này illustration các điểm với các sai số được ký hiệu bởi mở các đường tròn. Trong ban đầu, trên trái configuration, không có đỏ hỗ trợ/giá (support) vectơ. Bởi thấp hơn hồng tách siêu phẳng (hyperplane) và tăng lề (margin), ta kết thúc/cuối lên với đỏ hỗ trợ/giá (support) vectơ.
- `fig_54_11.png` (Trang 2021): Hình 54.11: Chạy (SVMs2′) trên hai các tập hợp của 30 các điểm; ν = 0.37.
- `fig_54_13.png` (Trang 2021): Hình 54.13: Chạy (SVMs2′) trên hai các tập hợp của 30 các điểm; ν = 0.71.
- `fig_54_12.png` (Trang 2022): Hình 54.12: Chạy (SVMs2′) trên hai các tập hợp của 30 các điểm; ν = 0.51.
- `fig_54_14.png` (Trang 2023): Hình 54.14: Chạy (SVMs2′) trên hai các tập hợp của 30 các điểm; ν = 0.95.
- `fig_54_15.png` (Trang 2024): Hình 54.15: Chạy (SVMs2′) trên hai các tập hợp của 30 các điểm; ν = 0.97.
- `fig_54_16.png` (Trang 2034): Hình 54.16: Chạy (SVMs3) trên hai các tập hợp của 30 các điểm; ν = 0.365.
- `fig_54_17.png` (Trang 2035): Hình 54.17: Chạy (SVMs3) trên hai các tập hợp của 30 các điểm; ν = 0.5.
- `fig_54_18.png` (Trang 2036): Hình 54.18: Chạy (SVMs3) trên hai các tập hợp của 30 các điểm; ν = 0.71.
- `fig_54_19.png` (Trang 2036): Hình 54.19: Chạy (SVMs3) trên hai các tập hợp của 30 các điểm; ν = 0.98.
- `fig_54_20.png` (Trang 2040): Hình 54.20: Khi λi = 0, ui là một cách chính xác được phân loại trên hoặc bên ngoài xanh lam lề (margin). Khi µj = 0, vj là một cách chính xác được phân loại trên hoặc bên ngoài bên ngoài đỏ lề (margin).
- `fig_54_21.png` (Trang 2041): Hình 54.21: phân loại của các điểm cho SVMs4 khi Các nhân tử Lagrange (Lagrange multipliers) là dương. trái illustration của Hình (1) là khi ui là bên trong lề (margin) vẫn chưa vẫn trên đúng vế/cạnh của tách siêu phẳng (hyperplane) w⊤x −b = 0. Tương tự, vj là bên trong lề (margin) trên đúng vế/cạnh của tách siêu phẳng (hyperplane). phải illustration depicts ui và vj trên tách siêu phẳng (hyperplane). Hình (2) illustrations misclassification của ui và vj.
- `fig_54_22.png` (Trang 2047): Hình 54.22: Chạy (SVMs4) trên hai các tập hợp của 30 các điểm; K = 190.
- `fig_54_23.png` (Trang 2048): Hình 54.23: Chạy (SVMs4) trên hai các tập hợp của 30 các điểm; K = 1/12000.
- `fig_54_24.png` (Trang 2052): Hình 54.24: Chạy (SVMs5) trên hai các tập hợp của 30 các điểm; K = 190.
- `fig_54_25.png` (Trang 2053): Hình 54.25: Chạy (SVMs5) trên hai các tập hợp của 30 các điểm; K = 1/13000.
